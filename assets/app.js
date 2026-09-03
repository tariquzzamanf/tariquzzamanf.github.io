/* =========================================================================
   Md. Tariquzzaman · academic site

   Behavior only. Page content is pre-rendered into the HTML by build.js from
   data.json, so this file never touches the content — it just wires up the
   theme toggle, the mobile menu, the section scroll spy and the tabbed
   personal page. The theme itself is applied by a small inline script in
   <head> so a stored choice cannot flash.
   ========================================================================= */
(function () {
  "use strict";

  /* Book covers: try the local file, then the remote fallback, then draw a
     placeholder from the title and author. */
  window.__cover = function (img) {
    var next = img.getAttribute("data-alt");
    if (next) { img.removeAttribute("data-alt"); img.src = next; return; }
    var box = img.closest ? img.closest(".bcov") : null;
    if (!box) return;
    box.classList.add("placeholder");
    while (box.firstChild) box.removeChild(box.firstChild);
    var t = document.createElement("span");
    t.className = "ph-title";
    t.textContent = box.getAttribute("data-title") || "";
    var a = document.createElement("span");
    a.className = "ph-author";
    a.textContent = box.getAttribute("data-author") || "";
    box.appendChild(t);
    box.appendChild(a);
  };

  function ready() {
    /* --- theme toggle --- */
    var toggle = document.querySelector(".theme-toggle");
    if (toggle) {
      toggle.addEventListener("click", function () {
        var attr = document.documentElement.getAttribute("data-theme");
        var systemDark = window.matchMedia &&
          window.matchMedia("(prefers-color-scheme: dark)").matches;
        var isDark = attr ? attr === "dark" : systemDark;
        var next = isDark ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", next);
        try { localStorage.setItem("theme", next); } catch (e) {}
      });
    }

    /* --- mobile menu --- */
    var burger = document.querySelector(".nav-burger");
    var nav = document.querySelector(".nav");
    if (burger && nav) {
      burger.addEventListener("click", function () { nav.classList.toggle("open"); });
      nav.querySelectorAll(".nav-links a").forEach(function (a) {
        a.addEventListener("click", function () { nav.classList.remove("open"); });
      });
    }

    /* --- side navigation: highlight the section in view --- */
    var spy = document.querySelector(".sidenav[data-spy]");
    if (spy) {
      var pairs = [];
      spy.querySelectorAll("a[href^='#']").forEach(function (link) {
        var sec = document.getElementById(link.getAttribute("href").slice(1));
        if (sec) pairs.push({ sec: sec, link: link });
      });
      var setActive = function () {
        if (!pairs.length) return;
        var y = window.scrollY + 120;
        var current = pairs[0];
        pairs.forEach(function (p) { if (p.sec.offsetTop <= y) current = p; });
        if (window.innerHeight + window.scrollY >=
            document.documentElement.scrollHeight - 2) {
          current = pairs[pairs.length - 1];
        }
        pairs.forEach(function (p) { p.link.classList.toggle("active", p === current); });
      };
      window.addEventListener("scroll", setActive, { passive: true });
      window.addEventListener("resize", setActive);
      setActive();
    }

    /* --- personal page: tabs, synced to the URL hash --- */
    var ptabs = document.querySelectorAll(".ptab-btn");
    if (ptabs.length) {
      var show = function (id) {
        document.querySelectorAll(".ppanel").forEach(function (p) {
          p.classList.toggle("active", p.id === "panel-" + id);
        });
        ptabs.forEach(function (b) {
          b.classList.toggle("active", b.getAttribute("data-tab") === id);
        });
      };
      ptabs.forEach(function (b) {
        b.addEventListener("click", function () {
          var id = b.getAttribute("data-tab");
          show(id);
          if (history.replaceState) history.replaceState(null, "", "#" + id);
          else location.hash = id;
        });
      });
      var initial = (location.hash || "").replace("#", "");
      var valid = Array.prototype.some.call(ptabs, function (b) {
        return b.getAttribute("data-tab") === initial;
      });
      show(valid ? initial : ptabs[0].getAttribute("data-tab"));
      window.addEventListener("hashchange", function () {
        var h = (location.hash || "").replace("#", "");
        if (h) show(h);
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", ready);
  } else {
    ready();
  }
})();
