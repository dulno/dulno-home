const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const javascriptObfuscator = require('javascript-obfuscator');

function obfuscateJs(jsCode, excludes) {
  const obfuscatedCode = javascriptObfuscator.obfuscate(jsCode, {
    exclude: excludes,
    compact: true,
    controlFlowFlattening: true,
    deadCodeInjection: true,
    disableConsoleOutput: true,
    identifierNamesGenerator: 'hexadecimal',
    stringArrayEncoding: ['base64'],
    stringArray: true,
    stringArrayThreshold: 1,
    transformObjectKeys: true,
    unicodeEscapeSequence: true
  }).getObfuscatedCode();
  return obfuscatedCode;
}

function extractDjangoBlocksInScripts(hash, content) {
  const djangoBlocks = [];
  let variables = "";
  let scripts = "";
  content.replace(/<script>(.*?)<\/script>/gs, (match, jsCode) => {
    scripts += jsCode + "\n";
    return "";
  });
  scripts = scripts.replace(/'\{\{[^}]+\}\}'|"\{\{[^}]+\}\}"|'\{%\s*[^%]+\s*%\}'|"\{%\s*[^%]+\s*%\}"/g, (djangoMatch) => {
    const varName = `var${hash}Var${djangoBlocks.length}`;
    djangoBlocks.push(varName);
    variables += `const ${varName} = ${djangoMatch};\n`;
    return varName;
  });
  return { scripts, djangoBlocks, variables };
}

function replaceIncludes(htmlContent) {
  const regex = /{% include '([^']+)' %}/g;
  let match;
  while ((match = regex.exec(htmlContent)) !== null) {
    const filePath = match[1];
    let fileContent = fs.readFileSync(`/dulno/templates/${filePath}`, 'utf-8')
    htmlContent = htmlContent.replace(match[0], fileContent);
  }
  return htmlContent;
}

function processHtmlFiles(directory) {
  const files = fs.readdirSync(directory);

  files.forEach(file => {
    const filePath = path.join(directory, file);

    if (filePath.includes("node_modules")) {
      return;
    }

    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      processHtmlFiles(filePath);
    } else if (file.endsWith('.html')) {
      let content = replaceIncludes(fs.readFileSync(filePath, 'utf-8'));
      let hash = crypto.createHash('sha256').update(file).digest('hex');
      const {scripts, djangoBlocks, variables } = extractDjangoBlocksInScripts(hash, content);
      content = content.replace(/<script(?!\s+src)[\s\S]*?>[\s\S]*?<\/script>/gi, '');
      const obfuscatedCode = obfuscateJs(scripts, djangoBlocks);
      content += "<script>" + variables + "\n" + obfuscatedCode + "</script>";
      fs.writeFileSync(filePath, content, 'utf-8');
    } else if (file.endsWith('.js')) {
      let content = fs.readFileSync(filePath, 'utf-8');
      fs.writeFileSync(filePath, obfuscateJs(content, []), 'utf-8');
    }
  });
}

processHtmlFiles(process.env.OBFUSCATION_HOME);