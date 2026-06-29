(function () {
  const storageKey = "kb-primary-nav-open";
  const desktopQuery = window.matchMedia("(min-width: 60em)");

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

  function syncForViewport() {
    const input = drawer();
    if (!input) return;

    if (desktopQuery.matches) {
      applyStoredState();
      return;
    }

    input.checked = false;
    delete document.documentElement.dataset.kbPrimaryNavState;
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

    syncForViewport();
    input.addEventListener("change", rememberState);
    if (typeof desktopQuery.addEventListener === "function") {
      desktopQuery.addEventListener("change", syncForViewport);
    } else if (typeof desktopQuery.addListener === "function") {
      desktopQuery.addListener(syncForViewport);
    }
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
