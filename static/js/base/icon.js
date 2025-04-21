const updateIcon = (event) => {
  var iconElements = document.getElementsByClassName("dulno-icon");
  for (var i = 0; i < iconElements.length; i++) {
    if (event.matches) {
      iconElements[i].href = "/static/img/icon-light.ico";
    } else {
      iconElements[i].href = "/static/img/icon-dark.ico";
    }
  }
};

const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
window.addEventListener('DOMContentLoaded', () => updateIcon(mediaQuery));
mediaQuery.addEventListener('change', updateIcon);