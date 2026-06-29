(function () {
  const root = document.querySelector('.kb-home-bento');
  if (!root) return;

  const cards = Array.from(root.querySelectorAll('.kb-bento-card'));
  if (!cards.length) return;

  const activeClass = 'is-hover-active';
  const managedClass = 'is-hover-managed';
  const hasActiveClass = 'has-hover-active';
  const gapClearDelayMs = 150;
  const exitClearDelayMs = 50;
  let clearTimer = 0;

  function cancelClear() {
    if (!clearTimer) return;
    window.clearTimeout(clearTimer);
    clearTimer = 0;
  }

  function clearActive() {
    cancelClear();
    root.classList.remove(hasActiveClass);
    cards.forEach(function (card) {
      card.classList.remove(activeClass);
    });
  }

  function scheduleClear(delay) {
    cancelClear();
    clearTimer = window.setTimeout(clearActive, delay);
  }

  function activate(card) {
    cancelClear();
    cards.forEach(function (candidate) {
      candidate.classList.toggle(activeClass, candidate === card);
    });
    root.classList.add(hasActiveClass);
  }

  root.classList.add(managedClass);

  cards.forEach(function (card) {
    card.addEventListener('pointerenter', function (event) {
      if (event.pointerType === 'touch') return;
      activate(card);
    });

    card.addEventListener('pointerleave', function (event) {
      if (event.pointerType === 'touch') return;
      scheduleClear(gapClearDelayMs);
    });
  });

  root.addEventListener('pointerenter', function (event) {
    if (event.pointerType === 'touch') return;
    cancelClear();
  });

  root.addEventListener('pointerleave', function (event) {
    if (event.pointerType === 'touch') return;
    scheduleClear(exitClearDelayMs);
  });

  root.addEventListener('focusin', function (event) {
    const card = event.target.closest('.kb-bento-card');
    if (!card || !root.contains(card)) return;
    activate(card);
  });

  root.addEventListener('focusout', function () {
    window.requestAnimationFrame(function () {
      if (root.contains(document.activeElement)) return;
      scheduleClear(exitClearDelayMs);
    });
  });
}());
