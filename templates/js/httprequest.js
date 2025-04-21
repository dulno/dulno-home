class HttpRequest {
  static PREFIX = "{{request_prefix}}";

  constructor(url, method, headers, data) {
    this.url = url;
    this.method = method;
    this.headers = headers;
    this.data = data;
  }

  send(callback) {
    let self = this;
    if (self.headers === undefined) {
      self.headers = [];
    }
    let headers = [...self.headers];
    headers.push({key: "Content-Type", value: "application/json"});
    const xhr = new XMLHttpRequest();
    xhr.open(self.method, HttpRequest.PREFIX + self.url);
    for (const entry of headers) {
      xhr.setRequestHeader(entry.key, entry.value);
    }
    xhr.onload = function (e) {
      callback(this.status, xhr.responseText);
    };
    xhr.onerror = function (e) {
      callback(-1, "");
    };
    xhr.send(JSON.stringify(self.data));
  }
}