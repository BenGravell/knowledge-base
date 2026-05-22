(function () {
  "use strict";

  var root = document.querySelector("[data-lqr]");
  if (!root) {
    return;
  }

  var A = [
    [0.98, 0.13],
    [0.04, 0.97],
  ];
  var B = [0.02, 0.08];
  var DT = 0.01;
  var PLOT_TIMESTEPS = 100;
  var PLOT_Y_MIN = -5;
  var PLOT_Y_MAX = 2;
  var SETTLING_TIMESTEPS = 5000;
  var INPUT_PENALTY = 1.0;
  var SETTLING_BAND = 0.05;
  var EPS = 1e-10;
  var INITIAL_STATE = [1, 1];
  var STEADY_STATE = [0, 0];
  var DEFAULT_PENALTIES = {
    q1: 2,
    q2: 2,
  };

  var inputs = {
    q1: document.getElementById("lqr-q1"),
    q2: document.getElementById("lqr-q2"),
  };
  var outputs = {
    q1: document.getElementById("lqr-q1-value"),
    q2: document.getElementById("lqr-q2-value"),
    status: document.getElementById("lqr-status"),
    gain: document.getElementById("lqr-gain"),
    eigs: document.getElementById("lqr-eigs"),
    peakInput: document.getElementById("lqr-peak-input"),
    settleTime: document.getElementById("lqr-settle-time"),
    matrixA: document.getElementById("lqr-matrix-a"),
    matrixB: document.getElementById("lqr-matrix-b"),
    matrixQ: document.getElementById("lqr-matrix-q"),
    matrixR: document.getElementById("lqr-matrix-r"),
  };
  var plot = document.getElementById("lqr-plot");

  var resetButton = document.getElementById("lqr-reset");

  function fmt(value, digits) {
    var places = digits == null ? 3 : digits;
    if (!Number.isFinite(value)) {
      return "n/a";
    }
    if (Math.abs(value) < 1e-9) {
      value = 0;
    }
    return value.toFixed(places);
  }

  function readPenalties() {
    return {
      q1: Number(inputs.q1.value),
      q2: Number(inputs.q2.value),
    };
  }

  function mat2Add(X, Y) {
    return [
      [X[0][0] + Y[0][0], X[0][1] + Y[0][1]],
      [X[1][0] + Y[1][0], X[1][1] + Y[1][1]],
    ];
  }

  function mat2Sub(X, Y) {
    return [
      [X[0][0] - Y[0][0], X[0][1] - Y[0][1]],
      [X[1][0] - Y[1][0], X[1][1] - Y[1][1]],
    ];
  }

  function mat2Mul(X, Y) {
    return [
      [
        X[0][0] * Y[0][0] + X[0][1] * Y[1][0],
        X[0][0] * Y[0][1] + X[0][1] * Y[1][1],
      ],
      [
        X[1][0] * Y[0][0] + X[1][1] * Y[1][0],
        X[1][0] * Y[0][1] + X[1][1] * Y[1][1],
      ],
    ];
  }

  function mat2Transpose(X) {
    return [
      [X[0][0], X[1][0]],
      [X[0][1], X[1][1]],
    ];
  }

  function mat2NormDiff(X, Y) {
    return Math.max(
      Math.abs(X[0][0] - Y[0][0]),
      Math.abs(X[0][1] - Y[0][1]),
      Math.abs(X[1][0] - Y[1][0]),
      Math.abs(X[1][1] - Y[1][1])
    );
  }

  function mat2Vec(X, v) {
    return [
      X[0][0] * v[0] + X[0][1] * v[1],
      X[1][0] * v[0] + X[1][1] * v[1],
    ];
  }

  function vecDot(a, b) {
    return a[0] * b[0] + a[1] * b[1];
  }

  function outer2(a, b) {
    return [
      [a[0] * b[0], a[0] * b[1]],
      [a[1] * b[0], a[1] * b[1]],
    ];
  }

  function solveDare(Q, R) {
    var AT = mat2Transpose(A);
    var X = [
      [Q[0][0], Q[0][1]],
      [Q[1][0], Q[1][1]],
    ];
    var iterations = 0;
    var converged = false;

    for (var i = 0; i < 5000; i += 1) {
      var XB = mat2Vec(X, B);
      var s = R + vecDot(B, XB);
      var ATXA = mat2Mul(mat2Mul(AT, X), A);
      var ATXB = mat2Vec(AT, XB);
      var BTXA = mat2Vec(mat2Transpose(A), XB);
      var correction = outer2(ATXB, BTXA).map(function (row) {
        return row.map(function (value) {
          return value / Math.max(Math.abs(s), EPS);
        });
      });
      var Xnext = mat2Sub(mat2Add(Q, ATXA), correction);
      Xnext = [
        [Xnext[0][0], 0.5 * (Xnext[0][1] + Xnext[1][0])],
        [0.5 * (Xnext[0][1] + Xnext[1][0]), Xnext[1][1]],
      ];
      iterations = i + 1;
      if (mat2NormDiff(Xnext, X) < 1e-9) {
        X = Xnext;
        converged = true;
        break;
      }
      X = Xnext;
    }

    var XBfinal = mat2Vec(X, B);
    var denom = R + vecDot(B, XBfinal);
    var BXA = [
      XBfinal[0] * A[0][0] + XBfinal[1] * A[1][0],
      XBfinal[0] * A[0][1] + XBfinal[1] * A[1][1],
    ];
    var safeDenom = Math.max(Math.abs(denom), EPS);
    var K = [-BXA[0] / safeDenom, -BXA[1] / safeDenom];

    return { X: X, K: K, iterations: iterations, converged: converged };
  }

  function simulate(K) {
    var initialX = INITIAL_STATE.slice();
    var x = initialX.slice();
    var rows = [];
    var peakInput = 0;

    for (var i = 0; i < SETTLING_TIMESTEPS; i += 1) {
      var u = K[0] * x[0] + K[1] * x[1];
      rows.push({ t: DT * i, x1: x[0], x2: x[1], u: u });
      peakInput = Math.max(peakInput, Math.abs(u));
      x = [
        A[0][0] * x[0] + A[0][1] * x[1] + B[0] * u,
        A[1][0] * x[0] + A[1][1] * x[1] + B[1] * u,
      ];
    }

    var settleTime = computeSettlingTime(rows, initialX);
    return { rows: rows.slice(0, PLOT_TIMESTEPS), peakInput: peakInput, settleTime: settleTime };
  }

  function settlingThresholds(initialX, steadyState) {
    return initialX.map(function (value, index) {
      return Math.max(Math.abs(value - steadyState[index]) * SETTLING_BAND, EPS);
    });
  }

  function computeSettlingTime(rows, initialX) {
    var thresholds = settlingThresholds(initialX, STEADY_STATE);

    for (var i = 0; i < rows.length; i += 1) {
      var staysInside = true;
      for (var j = i; j < rows.length; j += 1) {
        if (
          Math.abs(rows[j].x1 - STEADY_STATE[0]) > thresholds[0] ||
          Math.abs(rows[j].x2 - STEADY_STATE[1]) > thresholds[1]
        ) {
          staysInside = false;
          break;
        }
      }
      if (staysInside) {
        return rows[i].t;
      }
    }
    return null;
  }

  function closedLoopEigenvalues(K) {
    var M = [
      [A[0][0] + B[0] * K[0], A[0][1] + B[0] * K[1]],
      [A[1][0] + B[1] * K[0], A[1][1] + B[1] * K[1]],
    ];
    var tr = M[0][0] + M[1][1];
    var det = M[0][0] * M[1][1] - M[0][1] * M[1][0];
    var disc = tr * tr - 4 * det;
    if (disc >= 0) {
      var rootDisc = Math.sqrt(disc);
      return [0.5 * (tr + rootDisc), 0.5 * (tr - rootDisc)];
    }
    return [
      { re: 0.5 * tr, im: 0.5 * Math.sqrt(-disc) },
      { re: 0.5 * tr, im: -0.5 * Math.sqrt(-disc) },
    ];
  }

  function renderEigenvalues(target, eigs) {
    var table = document.createElement("table");
    table.className = "lqr-eigen-table";

    eigs.forEach(function (eig) {
      var value = typeof eig === "number" ? { re: eig, im: 0 } : eig;
      var tr = document.createElement("tr");
      var realSign = document.createElement("td");
      var realMagnitude = document.createElement("td");
      var imagSign = document.createElement("td");
      var imagMagnitude = document.createElement("td");
      var imagUnit = document.createElement("td");
      var hasImaginaryPart = Math.abs(value.im) >= 1e-12;

      realSign.className = "lqr-eigen-sign";
      realMagnitude.className = "lqr-eigen-number";
      imagSign.className = "lqr-eigen-sign";
      imagMagnitude.className = "lqr-eigen-number";
      imagUnit.className = "lqr-eigen-unit";

      realSign.textContent = value.re < 0 ? "-" : "";
      realMagnitude.textContent = fmt(Math.abs(value.re), 4);
      imagSign.textContent = hasImaginaryPart ? (value.im < 0 ? "-" : "+") : "";
      imagMagnitude.textContent = hasImaginaryPart ? fmt(Math.abs(value.im), 4) : "";
      imagUnit.textContent = hasImaginaryPart ? "i" : "";

      tr.appendChild(realSign);
      tr.appendChild(realMagnitude);
      tr.appendChild(imagSign);
      tr.appendChild(imagMagnitude);
      tr.appendChild(imagUnit);
      table.appendChild(tr);
    });

    target.replaceChildren(table);
  }

  function getCssVar(name, fallback) {
    var value = getComputedStyle(root).getPropertyValue(name).trim();
    return value || fallback;
  }

  function makeSvgElement(name, attrs) {
    var el = document.createElementNS("http://www.w3.org/2000/svg", name);
    Object.keys(attrs || {}).forEach(function (key) {
      el.setAttribute(key, attrs[key]);
    });
    return el;
  }

  function linePath(rows, key, xScale, yScale) {
    return rows
      .map(function (row, index) {
        var command = index === 0 ? "M" : "L";
        return command + " " + fmt(xScale(row.t), 2) + " " + fmt(yScale(row[key]), 2);
      })
      .join(" ");
  }

  function drawPlot(rows, settleTime) {
    var width = 900;
    var height = 360;
    var margin = { left: 58, right: 18, top: 18, bottom: 44 };
    var innerW = width - margin.left - margin.right;
    var innerH = height - margin.top - margin.bottom;

    var maxT = DT * (PLOT_TIMESTEPS - 1);
    var xScale = function (t) {
      return margin.left + (t / maxT) * innerW;
    };
    var yScale = function (y) {
      return margin.top + (1 - (y - PLOT_Y_MIN) / (PLOT_Y_MAX - PLOT_Y_MIN)) * innerH;
    };

    while (plot.lastChild) {
      plot.removeChild(plot.lastChild);
    }

    var title = makeSvgElement("title", { id: "lqr-plot-title" });
    title.textContent = "Closed-loop LQR response";
    var desc = makeSvgElement("desc", { id: "lqr-plot-desc" });
    desc.textContent = "Line plot of two states and one control input over one second, with dashed guides showing the five-percent settling band and settling time.";
    plot.appendChild(title);
    plot.appendChild(desc);

    var bg = makeSvgElement("rect", { x: 0, y: 0, width: width, height: height, fill: getCssVar("--md-default-bg-color", "#ffffff") });
    plot.appendChild(bg);

    for (var value = PLOT_Y_MIN; value <= PLOT_Y_MAX; value += 1) {
      var y = yScale(value);
      var gridClass = value === 0 ? "lqr-grid-line lqr-grid-line-zero" : "lqr-grid-line";
      plot.appendChild(makeSvgElement("line", { class: gridClass, x1: margin.left, x2: width - margin.right, y1: y, y2: y }));
      var yLabel = makeSvgElement("text", { class: "lqr-tick-label", x: margin.left - 10, y: y + 4, "text-anchor": "end" });
      yLabel.textContent = String(value);
      plot.appendChild(yLabel);
    }

    for (var xi = 0; xi <= 5; xi += 1) {
      var t = (xi / 5) * maxT;
      var x = xScale(t);
      plot.appendChild(makeSvgElement("line", { class: "lqr-grid-line", x1: x, x2: x, y1: margin.top, y2: height - margin.bottom }));
      var xLabel = makeSvgElement("text", { class: "lqr-tick-label", x: x, y: height - 18, "text-anchor": "middle" });
      xLabel.textContent = fmt(t, 1);
      plot.appendChild(xLabel);
    }

    var bandLabelsDrawn = {};
    settlingThresholds(INITIAL_STATE, STEADY_STATE).forEach(function (threshold, index) {
      var key = fmt(threshold, 6);
      if (bandLabelsDrawn[key]) {
        return;
      }
      bandLabelsDrawn[key] = true;
      [STEADY_STATE[index] + threshold, STEADY_STATE[index] - threshold].forEach(function (value) {
        var y = yScale(value);
        plot.appendChild(makeSvgElement("line", {
          class: "lqr-settling-band",
          x1: margin.left,
          x2: width - margin.right,
          y1: y,
          y2: y,
        }));
      });
      var bandLabel = makeSvgElement("text", {
        class: "lqr-settling-band-label",
        x: width - margin.right - 8,
        y: yScale(threshold) - 6,
        "text-anchor": "end",
      });
      bandLabel.textContent = "5% settling band";
      plot.appendChild(bandLabel);
    });

    if (settleTime != null && settleTime >= 0 && settleTime <= maxT) {
      var settleX = xScale(settleTime);
      plot.appendChild(makeSvgElement("line", {
        class: "lqr-settling-time-line",
        x1: settleX,
        x2: settleX,
        y1: margin.top,
        y2: height - margin.bottom,
      }));
      var settleLabel = makeSvgElement("text", {
        class: "lqr-settling-time-label",
        x: settleX,
        y: height - 2,
        "text-anchor": "middle",
      });
      settleLabel.textContent = fmt(settleTime, 2) + " s";
      plot.appendChild(settleLabel);
    }

    plot.appendChild(makeSvgElement("line", { class: "lqr-axis", x1: margin.left, x2: width - margin.right, y1: height - margin.bottom, y2: height - margin.bottom }));
    plot.appendChild(makeSvgElement("line", { class: "lqr-axis", x1: margin.left, x2: margin.left, y1: margin.top, y2: height - margin.bottom }));

    var xAxisLabel = makeSvgElement("text", { class: "lqr-axis-label", x: margin.left + innerW / 2, y: height - 4, "text-anchor": "middle" });
    xAxisLabel.textContent = "time (s)";
    plot.appendChild(xAxisLabel);

    var yAxisLabel = makeSvgElement("text", {
      class: "lqr-axis-label",
      x: 15,
      y: margin.top + innerH / 2,
      transform: "rotate(-90 15 " + (margin.top + innerH / 2) + ")",
      "text-anchor": "middle",
    });
    yAxisLabel.textContent = "value";
    plot.appendChild(yAxisLabel);

    [
      ["x1", "lqr-line lqr-line-state-1"],
      ["x2", "lqr-line lqr-line-state-2"],
      ["u", "lqr-line lqr-line-input"],
    ].forEach(function (series) {
      plot.appendChild(makeSvgElement("path", { class: series[1], d: linePath(rows, series[0], xScale, yScale) }));
    });
  }

  function renderMatrix(target, matrix) {
    var table = document.createElement("table");
    var tbody = document.createElement("tbody");
    matrix.forEach(function (row) {
      var tr = document.createElement("tr");
      row.forEach(function (value) {
        var td = document.createElement("td");
        td.textContent = fmt(value, 2);
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    target.replaceChildren(table);
  }

  function update() {
    var p = readPenalties();
    outputs.q1.textContent = fmt(p.q1, 1);
    outputs.q2.textContent = fmt(p.q2, 1);

    var Q = [
      [p.q1, 0],
      [0, p.q2],
    ];
    var result = solveDare(Q, INPUT_PENALTY);
    var sim = simulate(result.K);
    var eigs = closedLoopEigenvalues(result.K);

    outputs.status.textContent = result.converged ? "Solved in " + result.iterations + " iterations" : "Approximate";
    outputs.gain.textContent = "K = [" + fmt(result.K[0], 4) + ", " + fmt(result.K[1], 4) + "]";
    renderEigenvalues(outputs.eigs, eigs);
    outputs.peakInput.textContent = fmt(sim.peakInput, 3);
    outputs.settleTime.textContent = sim.settleTime == null ? "> " + fmt(DT * SETTLING_TIMESTEPS, 2) + " s" : fmt(sim.settleTime, 2) + " s";

    renderMatrix(outputs.matrixA, A);
    renderMatrix(outputs.matrixB, [[B[0]], [B[1]]]);
    renderMatrix(outputs.matrixQ, Q);
    renderMatrix(outputs.matrixR, [[INPUT_PENALTY]]);
    drawPlot(sim.rows, sim.settleTime);
  }

  Object.keys(inputs).forEach(function (key) {
    inputs[key].addEventListener("input", update);
  });

  resetButton.addEventListener("click", function () {
    inputs.q1.value = DEFAULT_PENALTIES.q1;
    inputs.q2.value = DEFAULT_PENALTIES.q2;
    update();
  });

  var observer = new MutationObserver(update);
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ["data-md-color-scheme"] });

  update();
})();
