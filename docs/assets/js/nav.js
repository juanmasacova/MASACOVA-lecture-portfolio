document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.getElementById("nav-toggle");
  var sidebar = document.getElementById("sidebar");
  var backdrop = document.getElementById("nav-backdrop");

  if (!toggle || !sidebar || !backdrop) return;

  function closeNav() {
    sidebar.classList.remove("open");
    backdrop.classList.remove("visible");
    toggle.setAttribute("aria-expanded", "false");
  }

  function toggleNav() {
    var isOpen = sidebar.classList.toggle("open");
    backdrop.classList.toggle("visible", isOpen);
    toggle.setAttribute("aria-expanded", String(isOpen));
  }

  toggle.addEventListener("click", toggleNav);
  backdrop.addEventListener("click", closeNav);
});
