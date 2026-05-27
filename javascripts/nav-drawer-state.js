(function () {
  const storageKey = "kb-primary-nav-open";
  const desktopQuery = window.matchMedia("(min-width: 76.25em)");

  function drawer() {
    return document.getElementById("__drawer");
  }

  function applyStoredState() {
    const input = drawer();
    if (!input || !desktopQuery.matches) return;

    const stored = window.localStorage.getItem(storageKey);
    if (stored === "open" || stored === "closed") {
      input.checked = stored === "open";
      document.documentElement.dataset.kbPrimaryNavState = stored;
    }
  }

  function rememberState(event) {
    if (!desktopQuery.matches) return;
    const state = event.currentTarget.checked ? "open" : "closed";
    window.localStorage.setItem(storageKey, state);
    document.documentElement.dataset.kbPrimaryNavState = state;
  }

  function bindDrawer() {
    const input = drawer();
    if (!input) return;

    applyStoredState();
    input.addEventListener("change", rememberState);
    requestAnimationFrame(() => {
      document.documentElement.classList.add("kb-nav-transitions-ready");
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindDrawer, { once: true });
  } else {
    bindDrawer();
  }
})();
