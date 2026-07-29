(function () {
  const header = document.querySelector("[data-header]");
  const menu = document.querySelector("[data-menu]");
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const params = new URLSearchParams(window.location.search);
  const sent = params.get("sent");
  const subscribed = params.get("subscribed");
  const error = params.get("error");

  function updateHeader() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 18);
  }

  function closeMenu() {
    if (!menu || !menuToggle) return;
    menu.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
    document.body.classList.remove("menu-open");
  }

  if (menu && menuToggle) {
    menuToggle.addEventListener("click", function () {
      const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
      menu.classList.toggle("open", !isOpen);
      menuToggle.setAttribute("aria-expanded", String(!isOpen));
      document.body.classList.toggle("menu-open", !isOpen);
    });

    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 900) closeMenu();
    });
  }

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });

  const route = window.location.pathname.split("/").filter(Boolean)[0] || "home";
  document.querySelectorAll("[data-nav]").forEach(function (link) {
    if (link.dataset.nav === route) link.setAttribute("aria-current", "page");
  });

  const revealItems = document.querySelectorAll(".reveal");
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealItems.forEach(function (item) { item.classList.add("visible"); });
  } else {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -32px" });

    revealItems.forEach(function (item, index) {
      item.style.transitionDelay = Math.min(index % 4, 3) * 60 + "ms";
      observer.observe(item);
    });
  }

  function showMessage(text, type) {
    const status = document.querySelector("[data-form-status]");
    if (!status) return;
    status.hidden = false;
    status.className = "form-status " + (type === "error" ? "form-status-error" : "form-status-success");
    status.textContent = text;
  }

  if (sent === "1") showMessage("Thank you for your message. We’ll be in touch soon.", "success");
  if (subscribed === "1") showMessage("Thanks—DTB will let you know when new insights are published.", "success");
  if (error) showMessage(decodeURIComponent(error), "error");

  document.querySelectorAll("[data-faq-button]").forEach(function (button) {
    button.addEventListener("click", function () {
      const panel = document.getElementById(button.getAttribute("aria-controls"));
      const expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
      if (panel) panel.hidden = expanded;
    });
  });

  const formStarted = document.querySelector("[data-form-started]");
  if (formStarted) formStarted.value = String(Date.now());

  function loadCircuitStyles() {
    if (document.querySelector('link[data-circuit-network]')) return;
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = "/static/css/circuit-network.css?v=20260728-1";
    link.dataset.circuitNetwork = "true";
    document.head.appendChild(link);
  }

  function circuitMarkup(index) {
    const suffix = String(index);
    return [
      '<div class="circuit-network" aria-hidden="true">',
      '<svg viewBox="0 0 1440 720" preserveAspectRatio="none" focusable="false">',
      '<defs>',
      '<linearGradient id="dtbCircuitGold' + suffix + '" x1="0" x2="1"><stop offset="0" stop-color="#ff671d"/><stop offset=".55" stop-color="#f2ad24"/><stop offset="1" stop-color="#ffe0a1"/></linearGradient>',
      '<linearGradient id="dtbCircuitPurple' + suffix + '" x1="0" x2="1"><stop offset="0" stop-color="#7441e8"/><stop offset=".58" stop-color="#a27aff"/><stop offset="1" stop-color="#d3c4ff"/></linearGradient>',
      '<filter id="dtbCircuitGlow' + suffix + '" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
      '</defs>',
      '<g class="circuit-base">',
      '<path class="circuit-trace" d="M-40 142 H190 V248 H420 V116 H680 V306 H900 V174 H1160 V270 H1480"/>',
      '<path class="circuit-trace circuit-trace-purple" d="M-20 548 H240 V432 H520 V604 H790 V386 H1030 V514 H1230 V404 H1480"/>',
      '<path class="circuit-trace" d="M96 -30 V104 H318 V332 H574 V226 H838 V486 H1110 V344 H1352 V760"/>',
      '<path class="circuit-trace circuit-trace-purple" d="M1422 30 H1270 V122 H1000 V54 H744 V188 H462 V72 H214 V208 H-40"/>',
      '<path class="circuit-trace" d="M-40 650 H176 V572 H392 V486 H636 V650 H924 V570 H1170 V642 H1480"/>',
      '</g>',
      '<g class="circuit-live">',
      '<path class="circuit-signal signal-a" style="stroke:url(#dtbCircuitGold' + suffix + ');filter:url(#dtbCircuitGlow' + suffix + ')" d="M-40 142 H190 V248 H420 V116 H680 V306 H900 V174 H1160 V270 H1480"/>',
      '<path class="circuit-signal circuit-signal-purple signal-b" style="stroke:url(#dtbCircuitPurple' + suffix + ');filter:url(#dtbCircuitGlow' + suffix + ')" d="M-20 548 H240 V432 H520 V604 H790 V386 H1030 V514 H1230 V404 H1480"/>',
      '<path class="circuit-signal signal-c" style="stroke:url(#dtbCircuitGold' + suffix + ');filter:url(#dtbCircuitGlow' + suffix + ')" d="M96 -30 V104 H318 V332 H574 V226 H838 V486 H1110 V344 H1352 V760"/>',
      '<path class="circuit-signal circuit-signal-purple signal-d" style="stroke:url(#dtbCircuitPurple' + suffix + ');filter:url(#dtbCircuitGlow' + suffix + ')" d="M1422 30 H1270 V122 H1000 V54 H744 V188 H462 V72 H214 V208 H-40"/>',
      '</g>',
      '<g class="circuit-nodes">',
      '<circle class="circuit-node" cx="190" cy="142" r="4"/><circle class="circuit-node" cx="420" cy="248" r="4"/><circle class="circuit-node" cx="680" cy="116" r="4"/><circle class="circuit-node" cx="900" cy="306" r="4"/><circle class="circuit-node" cx="1160" cy="174" r="4"/>',
      '<circle class="circuit-node circuit-node-purple" cx="240" cy="548" r="4"/><circle class="circuit-node circuit-node-purple" cx="520" cy="432" r="4"/><circle class="circuit-node circuit-node-purple" cx="790" cy="604" r="4"/><circle class="circuit-node circuit-node-purple" cx="1030" cy="386" r="4"/><circle class="circuit-node circuit-node-purple" cx="1230" cy="514" r="4"/>',
      '<circle class="circuit-node-live node-a" cx="420" cy="248" r="3.5"/><circle class="circuit-node-live node-b" cx="790" cy="604" r="3.5"/><circle class="circuit-node-live node-c" cx="838" cy="486" r="3.5"/><circle class="circuit-node-live node-d" cx="744" cy="188" r="3.5"/>',
      '</g>',
      '</svg>',
      '<span class="circuit-ambient a"></span><span class="circuit-ambient b"></span><span class="circuit-ambient c"></span>',
      '</div>'
    ].join("");
  }

  function mountCircuitNetworks() {
    loadCircuitStyles();
    const selectors = [
      ".tech-network-section",
      ".team-section",
      ".testimonial-section",
      ".breakthrough-band",
      ".final-cta",
      ".partnership"
    ];
    const seen = new Set();
    let index = 0;

    selectors.forEach(function (selector) {
      document.querySelectorAll(selector).forEach(function (section) {
        if (seen.has(section) || section.querySelector(":scope > .circuit-network")) return;
        seen.add(section);
        section.insertAdjacentHTML("afterbegin", circuitMarkup(index));
        index += 1;
      });
    });
  }

  mountCircuitNetworks();
})();
