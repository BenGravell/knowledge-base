function makeHeaderTitleClickable() {
  var logo = document.querySelector('a.md-header__button.md-logo');
  var title = document.querySelector('.md-header__title');
  if (!logo || !title || title.dataset.headerLinked) return;
  title.dataset.headerLinked = '1';
  title.style.cursor = 'pointer';
  title.addEventListener('click', function () {
    window.location.href = logo.href;
  });
  title.setAttribute('role', 'link');
  title.setAttribute('tabindex', '0');
  title.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      window.location.href = logo.href;
    }
  });
}

if (typeof document$ !== 'undefined') {
  document$.subscribe(makeHeaderTitleClickable);
} else {
  document.addEventListener('DOMContentLoaded', makeHeaderTitleClickable);
}
