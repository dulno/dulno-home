window.addEventListener('load', function () {
  if (Cookie.find("dulno-home-language") != null) {
    return;
  }
  var language = navigator.language || navigator.userLanguage;
  if (language !== "en" && language !== "de") {
    language = "en";
  }
  Cookie.create("dulno-home-language", language, 60 * 60 * 24 * 365);
});