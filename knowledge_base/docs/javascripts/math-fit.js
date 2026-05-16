(function () {
  function debounce(fn, wait) {
    var timeout;
    return function () {
      window.clearTimeout(timeout);
      timeout = window.setTimeout(fn, wait);
    };
  }

  function resetMathFit(container, math) {
    container.style.removeProperty("height");
    container.style.removeProperty("max-width");
    container.style.removeProperty("overflow-x");
    container.style.removeProperty("text-align");
    container.style.removeProperty("width");
    container.classList.remove("arithmatex--fit");

    math.style.removeProperty("display");
    math.style.removeProperty("transform");
    math.style.removeProperty("transform-origin");
  }

  function fitDisplayMath() {
    document
      .querySelectorAll(".arithmatex mjx-container[display='true']")
      .forEach(function (container) {
        var math = container.querySelector("mjx-math");
        if (!math) {
          return;
        }

        resetMathFit(container, math);

        var parent = container.parentElement;
        var content = container.closest(".md-content__inner") || container.closest(".md-typeset");
        var containerRect = container.getBoundingClientRect();
        var widths = [window.innerWidth];
        if (containerRect.width) {
          widths.push(containerRect.width);
        }
        if (parent && parent.clientWidth) {
          widths.push(parent.clientWidth);
        }
        if (parent) {
          var parentRect = parent.getBoundingClientRect();
          if (parentRect.width) {
            widths.push(parentRect.width);
          }
        }
        if (content && content.clientWidth) {
          widths.push(content.clientWidth);
        }
        if (content) {
          var contentRect = content.getBoundingClientRect();
          if (contentRect.width) {
            widths.push(contentRect.width);
          }
        }
        var availableWidth = Math.min.apply(Math, widths);
        var mathRect = math.getBoundingClientRect();
        var naturalWidth = Math.max(
          mathRect.width,
          math.scrollWidth,
          math.offsetWidth,
          container.scrollWidth
        );
        var naturalHeight = mathRect.height;

        if (!availableWidth || !naturalWidth || naturalWidth <= availableWidth) {
          return;
        }

        var scale = Math.max(0.1, (availableWidth - 2) / naturalWidth);

        container.classList.add("arithmatex--fit");
        container.style.width = "100%";
        container.style.maxWidth = "100%";
        container.style.height = Math.ceil(naturalHeight * scale) + "px";
        container.style.overflowX = "hidden";
        container.style.textAlign = "center";

        math.style.display = "inline-block";
        math.style.transform = "scale(" + scale + ")";
        math.style.transformOrigin = "center top";
      });
  }

  function scheduleFit() {
    window.requestAnimationFrame(function () {
      fitDisplayMath();
      window.setTimeout(fitDisplayMath, 150);
    });
  }

  function bindMathFit() {
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
      MathJax.startup.promise.then(scheduleFit);
    }

    scheduleFit();
    window.addEventListener("load", scheduleFit);
    window.addEventListener("resize", debounce(scheduleFit, 120));
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindMathFit);
  } else {
    bindMathFit();
  }
})();
