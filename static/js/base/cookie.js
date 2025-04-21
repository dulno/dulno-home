let Cookie = {
  findAll: function () {
    let pairs = document.cookie.split(";");
    let cookies = {};
    for (let i = 0; i < pairs.length; i++){
      let pair = pairs[i].split("=");
      cookies[(pair[0]+'').trim()] = unescape(pair.slice(1).join("="));
    }
    return cookies;
  },

  find: function (name) {
    let cookie = null,
      list = this.findAll();
    let keys = Object.keys(list);
    for (let i = 0; i < keys.length; i++) {
      let key = keys[i];
      if (key === name) {
        cookie = list[key];
      }
    }
    return cookie;
  },

  create: function (name, value, time) {
    let today = new Date(),
      offset = (typeof time == "undefined") ? (1000 * 60 * 60 * 24) : (time * 1000),
      expires_at = new Date(today.getTime() + offset);
    let content = {
      name: escape(value),
      expires: expires_at.toGMTString(),
      path: "/",
      domain: "." + window.location.hostname,
    };
    if (!window.location.hostname.includes("0.0.0.0")) {
      content.secure = true;
    }
    let cookie = Object.keys(content).map(function(key) {
      return [(key === "name") ? name : key, content[key]].join("=");
    }).join(";");
    document.cookie = cookie;
    return this;
  },

  destroy: function (name) {
    this.create(name, "", -1);
  }
};