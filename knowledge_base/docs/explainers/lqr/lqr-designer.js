(function () {
  "use strict";

  var root = document.querySelector("[data-lqr-designer]");
  if (!root) {
    return;
  }

  var A = [
    [0.98, 0.13],
    [0.04, 0.97],
  ];
  var B = [0.02, 0.08];
  var DT = 0.01;
  var NUM_TIMESTEPS = 100;
  var EPS = 1e-10;

  var inputs = {
    q1: document.getElementById("lqr-q1"),
    q2: document.getElementById("lqr-q2"),
    r: document.getElementById("lqr-r"),
  };
  var outputs = {
    q1: document.getElementById("lqr-q1-value"),
    q2: document.getElementById("lqr-q2-value"),
    r: document.getElementById("lqr-r-value"),
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

  var presets = {
    balanced: [2, 2, 2],
    fast: [5, 5, 0.7],
    "cheap-input": [2, 2, 0.2],
    gentle: [1, 1, 5],
  };

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
      r: Number(inputs.r.value),
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
    var x = [1, 1];
    var rows = [];
    var peakInput = 0;
    var settleTime = null;

    for (var i = 0; i < NUM_TIMESTEPS; i += 1) {
      var u = K[0] * x[0] + K[1] * x[1];
      rows.push({ t: DT * i, x1: x[0], x2: x[1], u: u });
      peakInput = Math.max(peakInput, Math.abs(u));
      if (settleTime == null && Math.hypot(x[0], x[1]) < 0.05) {
        settleTime = DT * i;
      }
      x = [
        A[0][0] * x[0] + A[0][1] * x[1] + B[0] * u,
        A[1][0] * x[0] + A[1][1] * x[1] + B[1] * u,
      ];
    }

    return { rows: rows, peakInput: peakInput, settleTime: settleTime };
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

  function eigsToString(eigs) {
    return eigs
      .map(function (eig) {
        if (typeof eig === "number") {
          return fmt(eig, 4);
        }
        var sign = eig.im >= 0 ? "+" : "-";
        return fmt(eig.re, 4) + " " + sign + " " + fmt(Math.abs(eig.im), 4) + "i";
      })
      .join(", ");
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

  function drawPlot(rows) {
    var width = 900;
    var height = 360;
    var margin = { left: 58, right: 18, top: 18, bottom: 44 };
    var innerW = width - margin.left - margin.right;
    var innerH = height - margin.top - margin.bottom;
    var values = [];

    rows.forEach(function (row) {
      values.push(row.x1, row.x2, row.u);
    });
    var minY = Math.min.apply(null, values);
    var maxY = Math.max.apply(null, values);
    var pad = Math.max(0.15, 0.1 * (maxY - minY));
    minY -= pad;
    maxY += pad;

    var maxT = DT * (NUM_TIMESTEPS - 1);
    var xScale = function (t) {
      return margin.left + (t / maxT) * innerW;
    };
    var yScale = function (y) {
      return margin.top + (1 - (y - minY) / (maxY - minY || 1)) * innerH;
    };

    while (plot.lastChild) {
      plot.removeChild(plot.lastChild);
    }

    var title = makeSvgElement("title", { id: "lqr-plot-title" });
    title.textContent = "Closed-loop LQR response";
    var desc = makeSvgElement("desc", { id: "lqr-plot-desc" });
    desc.textContent = "Line plot of two states and one control input over one second.";
    plot.appendChild(title);
    plot.appendChild(desc);

    var bg = makeSvgElement("rect", { x: 0, y: 0, width: width, height: height, fill: getCssVar("--md-default-bg-color", "#ffffff") });
    plot.appendChild(bg);

    for (var yi = 0; yi <= 4; yi += 1) {
      var value = minY + (yi / 4) * (maxY - minY);
      var y = yScale(value);
      plot.appendChild(makeSvgElement("line", { class: "lqr-grid-line", x1: margin.left, x2: width - margin.right, y1: y, y2: y }));
      var yLabel = makeSvgElement("text", { class: "lqr-tick-label", x: margin.left - 10, y: y + 4, "text-anchor": "end" });
      yLabel.textContent = fmt(value, 2);
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
    outputs.r.textContent = fmt(p.r, 1);

    var Q = [
      [p.q1, 0],
      [0, p.q2],
    ];
    var result = solveDare(Q, p.r);
    var sim = simulate(result.K);
    var eigs = closedLoopEigenvalues(result.K);

    outputs.status.textContent = result.converged ? "Solved in " + result.iterations + " iterations" : "Approximate";
    outputs.gain.textContent = "K = [" + fmt(result.K[0], 4) + ", " + fmt(result.K[1], 4) + "]";
    outputs.eigs.textContent = eigsToString(eigs);
    outputs.peakInput.textContent = fmt(sim.peakInput, 3);
    outputs.settleTime.textContent = sim.settleTime == null ? "> " + fmt(DT * NUM_TIMESTEPS, 2) + " s" : fmt(sim.settleTime, 2) + " s";

    renderMatrix(outputs.matrixA, A);
    renderMatrix(outputs.matrixB, [[B[0]], [B[1]]]);
    renderMatrix(outputs.matrixQ, Q);
    renderMatrix(outputs.matrixR, [[p.r]]);
    drawPlot(sim.rows);
  }

  Object.keys(inputs).forEach(function (key) {
    inputs[key].addEventListener("input", update);
  });

  root.querySelectorAll("[data-lqr-preset]").forEach(function (button) {
    button.addEventListener("click", function () {
      var preset = presets[button.getAttribute("data-lqr-preset")];
      inputs.q1.value = preset[0];
      inputs.q2.value = preset[1];
      inputs.r.value = preset[2];
      update();
    });
  });

  var observer = new MutationObserver(update);
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ["data-md-color-scheme"] });

  update();
})();
