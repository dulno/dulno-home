window.addEventListener('load', function () {
  let url = window.location.pathname.replaceAll("/", "");
  if (url === "imprint" || url === "privacy-policy" || url === "terms-of-service") {
    return;
  }
  if (Cookie.find("dulno-cookies") != null) {
    return;
  }
  Swal.fire({
    imageUrl: "/static/img/home/cookie.webp",
    imageWidth: 128,
    imageHeight: 128,
    title: "Cookies",
    html:
      "<p>We use cookies that are essential for the functioning of this website.</p>" +
      "<p>The cookies are required for the following things, for example:</p>" +
      "<ul>" +
      "<li>Language settings</li>" +
      "<li>Theme settings</li>" +
      "<li>Authentication</li>" +
      "</ul>" +
      "<p>You can find more detailed information about the use of cookies in our <a href='/privacy-policy/'>privacy policy</a>.</p>" +
      "<p>Since the existence of these cookies is unavoidable, we cannot do without them under any circumstances. We thank you for your understanding.</p>",
    confirmButtonText: "Understood",
    customClass: {
      htmlContainer: "cookie-banner-container",
    }
  }).then((result) => {
    Cookie.create("dulno-cookies", true, 60 * 60 * 24 * 365);
    window.location.reload();
  });
});