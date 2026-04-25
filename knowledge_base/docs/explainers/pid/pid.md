# Proportional Integral Derivative (PID) control

*Proportional Integral Derivative (PID)* is a feedback control scheme which generates control actions as a weighted linear combination of three terms:

1. Proportional to the error
2. Integral of the error
3. Derivative of the error

The weights are referred to as feedback gains, and can be tuned according to model-free heuristics e.g. the [Ziegler–Nichols method](https://en.wikipedia.org/wiki/Ziegler%E2%80%93Nichols_method).

Despite its simplicity, PID is extremely (often surprisingly) effective in practice on a wide variety of systems, even when stochastic disturbances, plant nonlinearities, input delays, and other challenging aspects are present.

## Interactive demo: balancing a cart-pole

The **cart-pole** (inverted pendulum on a cart) is a canonical benchmark for control.
The pole starts tilted and the PID controller applies horizontal forces to the cart to balance it upright.

Tune the gains and press **Disturb** to kick the pole. Notice how:

- **K_p** alone causes oscillation — the controller overshoots.
- Adding **K_d** damps the oscillation (derivative = "predictive braking").
- **K_i** corrects steady-state offset but can cause windup instability if set too high.

<div id="pid-demo-root">
<style>
#pid-demo-root {
  font-family: inherit;
  margin: 1.5em 0;
}
#pid-demo-root canvas {
  display: block;
  width: 100%;
  height: auto;        /* let aspect-ratio drive height */
  border-radius: 6px;
}
#pid-sim-canvas {
  aspect-ratio: 900 / 270;
  background: var(--md-code-bg-color, #f8f8f8);
  border: 1px solid var(--md-default-fg-color--lightest, #e0e0e0);
  margin-bottom: 6px;
}
#pid-plot-canvas {
  aspect-ratio: 900 / 110;
  background: var(--md-code-bg-color, #f8f8f8);
  border: 1px solid var(--md-default-fg-color--lightest, #e0e0e0);
  margin-bottom: 10px;
}
.pid-controls {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 20px;
}
.pid-section {
  display: grid;
  gap: 5px;
}
.pid-section-label {
  font-weight: 700;
  font-size: 0.78em;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--md-default-fg-color--light, #64748b);
  padding-bottom: 3px;
  border-bottom: 1px solid var(--md-default-fg-color--lightest, #dde2ea);
  margin-bottom: 1px;
}
.pid-slider-row {
  display: grid;
  grid-template-columns: 52px 1fr 48px;
  align-items: center;
  gap: 6px;
  font-size: 0.87em;
}
.pid-slider-row label {
  font-weight: 600;
  font-family: var(--md-code-font, monospace);
  text-align: right;
}
.pid-slider-row input[type=range] {
  width: 100%;
  cursor: pointer;
}
.pid-slider-row input[type=range].angle-slider  { accent-color: #dc2626; }
.pid-slider-row input[type=range].pos-slider    { accent-color: #2563eb; }
.pid-slider-row .pid-val {
  font-family: var(--md-code-font, monospace);
  font-size: 0.93em;
  text-align: right;
  min-width: 44px;
}
.pid-btn-row {
  display: flex;
  gap: 7px;
  margin-top: 3px;
  flex-wrap: wrap;
}
.pid-btn-row button {
  padding: 4px 13px;
  border-radius: 5px;
  border: 1px solid currentColor;
  cursor: pointer;
  font-size: 0.85em;
  font-family: inherit;
  background: transparent;
  color: inherit;
  transition: background 0.15s;
}
.pid-btn-row button:hover {
  background: var(--md-accent-fg-color, #2563eb);
  color: #fff;
  border-color: transparent;
}
</style>

<canvas id="pid-sim-canvas" width="900" height="270"></canvas>
<canvas id="pid-plot-canvas" width="900" height="110"></canvas>

<div class="pid-controls">
  <div class="pid-section">
    <div class="pid-section-label">Angle PID (θ → F)</div>
    <div class="pid-slider-row">
      <label>K<sub>p</sub></label>
      <input type="range" class="angle-slider" id="pid-kp" min="0" max="100" step="0.5" value="43">
      <span class="pid-val" id="pid-kp-val">43.0</span>
    </div>
    <div class="pid-slider-row">
      <label>K<sub>i</sub></label>
      <input type="range" class="angle-slider" id="pid-ki" min="0" max="5" step="0.05" value="0">
      <span class="pid-val" id="pid-ki-val">0.00</span>
    </div>
    <div class="pid-slider-row">
      <label>K<sub>d</sub></label>
      <input type="range" class="angle-slider" id="pid-kd" min="0" max="20" step="0.25" value="11">
      <span class="pid-val" id="pid-kd-val">11.0</span>
    </div>
    <div class="pid-btn-row">
      <button id="pid-reset-btn">Reset</button>
      <button id="pid-disturb-btn">Disturb</button>
      <button id="pid-zn-btn">Preset angle</button>
    </div>
  </div>

  <div class="pid-section">
    <div class="pid-section-label">Position PID (x → F)</div>
    <div class="pid-slider-row">
      <label>K<sub>p</sub></label>
      <input type="range" class="pos-slider" id="pid-kpx" min="0" max="15" step="0.1" value="3.2">
      <span class="pid-val" id="pid-kpx-val">3.2</span>
    </div>
    <div class="pid-slider-row">
      <label>K<sub>i</sub></label>
      <input type="range" class="pos-slider" id="pid-kix" min="0" max="2" step="0.05" value="0">
      <span class="pid-val" id="pid-kix-val">0.00</span>
    </div>
    <div class="pid-slider-row">
      <label>K<sub>d</sub></label>
      <input type="range" class="pos-slider" id="pid-kdx" min="0" max="15" step="0.1" value="4.6">
      <span class="pid-val" id="pid-kdx-val">4.6</span>
    </div>
    <div class="pid-btn-row">
      <button id="pid-znx-btn">Preset position</button>
    </div>
  </div>
</div>
</div>

<script>
(function () {
  "use strict";

  // ── LQR preset gains (computed by scripts/compute_lqr_gains.py) ────────────
  // Angle LQR: Q=diag(1,0,10,1), R=0.1
  var PRESET_KP   = 43.0;
  var PRESET_KI   = 0.0;
  var PRESET_KD   = 11.0;
  // Position LQR: Q=diag(1,0,10,1), R=0.1  (POSITIVE sign: push in direction of x)
  var PRESET_KP_X = 3.2;
  var PRESET_KI_X = 0.0;
  var PRESET_KD_X = 4.6;

  // ── Physics constants ──────────────────────────────────────────────────────
  var M = 1.0;    // cart mass (kg)
  var m = 0.1;    // pole mass (kg)
  var l = 0.5;    // pole half-length (m)
  var g = 9.81;   // gravity (m/s²)
  var DT = 1 / 60; // simulation timestep (s) — one per animation frame

  // ── Simulation state ───────────────────────────────────────────────────────
  // [x, xdot, theta, thetadot]   theta=0 → pole upright, theta>0 → tips right
  var state = [0, 0, 0.12, 0];
  var integralErr  = 0;    // angle PID integral
  var prevErr      = 0.12; // angle PID previous error (initialised to theta0)
  var integralErrX = 0;    // position PID integral
  var prevErrX     = 0;    // position PID previous error
  var fallen = false;
  var time = 0;

  // Rolling history for the plot (≈6 s at 60 fps)
  var HISTORY = 360;
  var thetaHist = [];
  var xHist = [];
  var forceHist = [];

  // ── DOM refs ───────────────────────────────────────────────────────────────
  var simCanvas  = document.getElementById("pid-sim-canvas");
  var plotCanvas = document.getElementById("pid-plot-canvas");
  var ctx  = simCanvas.getContext("2d");
  var pctx = plotCanvas.getContext("2d");

  // Scale canvas internal resolution to device pixel ratio for crisp rendering.
  // CSS (width:100%, aspect-ratio) controls the display size; we must not
  // override it with inline style.width/height or the canvas overflows.
  function scaleCanvas(canvas, context) {
    var dpr = window.devicePixelRatio || 1;
    var w = parseInt(canvas.getAttribute("width"));
    var h = parseInt(canvas.getAttribute("height"));
    canvas.width  = w * dpr;
    canvas.height = h * dpr;
    context.scale(dpr, dpr);
  }
  scaleCanvas(simCanvas,  ctx);
  scaleCanvas(plotCanvas, pctx);

  var SIM_W  = parseInt(simCanvas.getAttribute("width")  || 900);
  var SIM_H  = parseInt(simCanvas.getAttribute("height") || 270);
  var PLOT_W = parseInt(plotCanvas.getAttribute("width")  || 900);
  var PLOT_H = parseInt(plotCanvas.getAttribute("height") || 110);

  // ── Gain accessors ─────────────────────────────────────────────────────────
  function getKp()  { return parseFloat(document.getElementById("pid-kp").value); }
  function getKi()  { return parseFloat(document.getElementById("pid-ki").value); }
  function getKd()  { return parseFloat(document.getElementById("pid-kd").value); }
  function getKpX() { return parseFloat(document.getElementById("pid-kpx").value); }
  function getKiX() { return parseFloat(document.getElementById("pid-kix").value); }
  function getKdX() { return parseFloat(document.getElementById("pid-kdx").value); }

  // ── Cartpole ODE ───────────────────────────────────────────────────────────
  // Returns d/dt [x, xdot, theta, thetadot] given state and force F.
  function deriv(s, F) {
    var x = s[0], xd = s[1], th = s[2], thd = s[3];
    var sinT = Math.sin(th), cosT = Math.cos(th);
    var temp  = (F + m * l * thd * thd * sinT) / (M + m);
    var thadd = (g * sinT - cosT * temp) / (l * (4/3 - m * cosT * cosT / (M + m)));
    var xadd  = temp - m * l * thadd * cosT / (M + m);
    return [xd, xadd, thd, thadd];
  }

  // RK4 integration over one timestep DT
  function rk4(s, F) {
    var k1 = deriv(s, F);
    var s2 = s.map(function(v, i) { return v + 0.5 * DT * k1[i]; });
    var k2 = deriv(s2, F);
    var s3 = s.map(function(v, i) { return v + 0.5 * DT * k2[i]; });
    var k3 = deriv(s3, F);
    var s4 = s.map(function(v, i) { return v + DT * k3[i]; });
    var k4 = deriv(s4, F);
    return s.map(function(v, i) {
      return v + (DT / 6) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]);
    });
  }

  // ── PID controllers ────────────────────────────────────────────────────────
  // Angle PID: θ > 0 (leans right) → F > 0 (push right to catch pole)
  // Position PID: x > 0 → F > 0 (push SAME direction: tips pole toward origin,
  //   then angle PID applies strong corrective force that drags cart back).
  //   Counter-intuitive but verified by LQR — the coupling makes it work.
  function pidForce() {
    var th = state[2], x = state[0], xd = state[1];

    // Angle PID
    integralErr = clamp(integralErr + th * DT, -3, 3);
    var dErr = (th - prevErr) / DT;
    prevErr = th;
    var F_angle = getKp() * th + getKi() * integralErr + getKd() * dErr;

    // Position PID (positive sign: tips pole toward origin via angle coupling)
    integralErrX = clamp(integralErrX + x * DT, -5, 5);
    var dErrX = (x - prevErrX) / DT;
    prevErrX = x;
    var F_pos = getKpX() * x + getKiX() * integralErrX + getKdX() * dErrX;

    return clamp(F_angle + F_pos, -15, 15);
  }

  function clamp(v, lo, hi) { return v < lo ? lo : v > hi ? hi : v; }

  // ── Simulation step ────────────────────────────────────────────────────────
  var lastForce = 0;

  function step() {
    if (fallen) return 0;
    var F = pidForce();
    lastForce = F;
    state = rk4(state, F);
    time += DT;
    if (Math.abs(state[2]) > Math.PI / 2) fallen = true;
    return F;
  }

  // ── Drawing — simulation canvas ────────────────────────────────────────────
  var TRACK_Y  = 185;   // px: vertical centre of cart
  var CART_W   = 70;
  var CART_H   = 32;
  var WHEEL_R  = 10;
  var POLE_PX  = 120;   // pole length in pixels  (l = 0.5 m → 120 px/m scale)
  var SCALE    = POLE_PX / l;  // pixels per metre

  // Detect dark scheme via Material theme attribute
  function isDark() {
    var scheme = document.documentElement.getAttribute("data-md-color-scheme");
    return scheme === "slate";
  }

  function fg()      { return isDark() ? "#cdd6f4" : "#1e293b"; }
  function fgDim()   { return isDark() ? "#6c7086" : "#94a3b8"; }
  function bgCode()  { return isDark() ? "#1e1e2e" : "#f8fafc"; }
  function cartCol() { return fallen ? "#ef4444" : "#2563eb"; }
  function poleCol() { return fallen ? "#f97316" : "#16a34a"; }

  function drawSim() {
    var W = SIM_W, H = SIM_H;
    ctx.clearRect(0, 0, W, H);

    var x  = state[0], th = state[2];
    // Cart x in pixels, clamped so it doesn't vanish off screen
    var cartX = clamp(W / 2 + x * SCALE, CART_W * 0.6, W - CART_W * 0.6);

    // ── Track ──────────────────────────────────────────────────────────────
    ctx.beginPath();
    ctx.strokeStyle = fgDim();
    ctx.lineWidth = 2;
    ctx.moveTo(20, TRACK_Y + CART_H / 2 + WHEEL_R);
    ctx.lineTo(W - 20, TRACK_Y + CART_H / 2 + WHEEL_R);
    ctx.stroke();

    // Track end bumpers
    [20, W - 20].forEach(function(bx) {
      ctx.beginPath();
      ctx.strokeStyle = fgDim();
      ctx.lineWidth = 3;
      ctx.moveTo(bx, TRACK_Y + CART_H / 2 + WHEEL_R - 10);
      ctx.lineTo(bx, TRACK_Y + CART_H / 2 + WHEEL_R + 10);
      ctx.stroke();
    });

    // ── Force arrow ────────────────────────────────────────────────────────
    var arrowLen = clamp(lastForce * 4, -60, 60);
    if (Math.abs(arrowLen) > 2) {
      var arrowX0 = cartX + (arrowLen > 0 ? CART_W / 2 : -CART_W / 2);
      var arrowX1 = arrowX0 + arrowLen;
      ctx.beginPath();
      ctx.strokeStyle = "#a855f7";
      ctx.lineWidth = 2.5;
      ctx.moveTo(arrowX0, TRACK_Y);
      ctx.lineTo(arrowX1, TRACK_Y);
      ctx.stroke();
      // Arrowhead
      var dir = arrowLen > 0 ? 1 : -1;
      ctx.beginPath();
      ctx.fillStyle = "#a855f7";
      ctx.moveTo(arrowX1, TRACK_Y);
      ctx.lineTo(arrowX1 - dir * 8, TRACK_Y - 5);
      ctx.lineTo(arrowX1 - dir * 8, TRACK_Y + 5);
      ctx.closePath();
      ctx.fill();
    }

    // ── Cart ───────────────────────────────────────────────────────────────
    ctx.fillStyle = cartCol();
    roundRect(ctx, cartX - CART_W / 2, TRACK_Y - CART_H / 2, CART_W, CART_H, 6);
    ctx.fill();

    // Wheels
    ctx.fillStyle = isDark() ? "#1e293b" : "#0f172a";
    [-0.3, 0.3].forEach(function(dx) {
      ctx.beginPath();
      ctx.arc(cartX + dx * CART_W, TRACK_Y + CART_H / 2, WHEEL_R, 0, 2 * Math.PI);
      ctx.fill();
      ctx.beginPath();
      ctx.fillStyle = fgDim();
      ctx.arc(cartX + dx * CART_W, TRACK_Y + CART_H / 2, 3, 0, 2 * Math.PI);
      ctx.fill();
      ctx.fillStyle = isDark() ? "#1e293b" : "#0f172a";
    });

    // ── Pole ───────────────────────────────────────────────────────────────
    var poleBaseX = cartX;
    var poleBaseY = TRACK_Y - CART_H / 2;
    var poleTipX  = poleBaseX + POLE_PX * Math.sin(th);
    var poleTipY  = poleBaseY - POLE_PX * Math.cos(th);

    ctx.beginPath();
    ctx.strokeStyle = poleCol();
    ctx.lineWidth = 8;
    ctx.lineCap = "round";
    ctx.moveTo(poleBaseX, poleBaseY);
    ctx.lineTo(poleTipX, poleTipY);
    ctx.stroke();

    // Tip ball
    ctx.beginPath();
    ctx.fillStyle = poleCol();
    ctx.arc(poleTipX, poleTipY, 8, 0, 2 * Math.PI);
    ctx.fill();

    // Pivot dot
    ctx.beginPath();
    ctx.fillStyle = isDark() ? "#cdd6f4" : "#1e293b";
    ctx.arc(poleBaseX, poleBaseY, 5, 0, 2 * Math.PI);
    ctx.fill();

    // ── Telemetry ──────────────────────────────────────────────────────────
    ctx.font = "13px monospace";
    ctx.fillStyle = fg();
    var degStr  = (th * 180 / Math.PI).toFixed(1).padStart(6);
    var posStr  = state[0].toFixed(2).padStart(6);
    var fStr    = lastForce.toFixed(1).padStart(6);
    ctx.fillText("θ = " + degStr + "°", 12, 20);
    ctx.fillText("x = " + posStr + " m",           12, 38);
    ctx.fillText("F = " + fStr   + " N",           12, 56);
    ctx.fillText("t = " + time.toFixed(1) + " s",  12, 74);

    if (fallen) {
      ctx.fillStyle = "rgba(239,68,68,0.15)";
      ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = "#dc2626";
      ctx.font = "bold 20px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("Pole fell — press Reset", W / 2, H / 2);
      ctx.textAlign = "left";
    }
  }

  // Polyfill for roundRect (Safari < 16 / older browsers)
  function roundRect(c, x, y, w, h, r) {
    if (c.roundRect) {
      c.beginPath();
      c.roundRect(x, y, w, h, r);
    } else {
      c.beginPath();
      c.moveTo(x + r, y);
      c.lineTo(x + w - r, y);
      c.quadraticCurveTo(x + w, y, x + w, y + r);
      c.lineTo(x + w, y + h - r);
      c.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
      c.lineTo(x + r, y + h);
      c.quadraticCurveTo(x, y + h, x, y + h - r);
      c.lineTo(x, y + r);
      c.quadraticCurveTo(x, y, x + r, y);
      c.closePath();
    }
  }

  // ── Drawing — plot canvas ──────────────────────────────────────────────────
  var PAD = { l: 42, r: 12, t: 14, b: 26 };

  function drawPlot() {
    var W = PLOT_W, H = PLOT_H;
    pctx.clearRect(0, 0, W, H);

    var pw = W - PAD.l - PAD.r;
    var ph = H - PAD.t - PAD.b;
    var midY = PAD.t + ph / 2;

    // Background
    pctx.fillStyle = bgCode();
    pctx.fillRect(PAD.l, PAD.t, pw, ph);

    // Horizontal grid lines at ±30°, 0°
    [-60, -30, 0, 30, 60].forEach(function(deg) {
      var y = midY - (deg / 90) * (ph / 2);
      pctx.beginPath();
      pctx.strokeStyle = deg === 0 ? fgDim() : (isDark() ? "#313244" : "#e2e8f0");
      pctx.lineWidth = deg === 0 ? 1.2 : 0.8;
      pctx.setLineDash(deg === 0 ? [] : [4, 4]);
      pctx.moveTo(PAD.l, y);
      pctx.lineTo(PAD.l + pw, y);
      pctx.stroke();
      pctx.setLineDash([]);

      // Y-axis label
      pctx.fillStyle = fgDim();
      pctx.font = "10px monospace";
      pctx.textAlign = "right";
      pctx.fillText(deg + "°", PAD.l - 4, y + 3.5);
    });

    // Border
    pctx.beginPath();
    pctx.strokeStyle = fgDim();
    pctx.lineWidth = 1;
    pctx.strokeRect(PAD.l, PAD.t, pw, ph);

    if (thetaHist.length < 2) return;

    var n = thetaHist.length;

    // X position line (blue, dashed)
    pctx.beginPath();
    pctx.strokeStyle = "#2563eb";
    pctx.lineWidth = 1.5;
    pctx.setLineDash([5, 4]);
    xHist.forEach(function(xv, i) {
      var px = PAD.l + (i / HISTORY) * pw;
      var py = midY - clamp(xv / 2, -1, 1) * (ph / 2);
      if (i === 0) pctx.moveTo(px, py); else pctx.lineTo(px, py);
    });
    pctx.stroke();
    pctx.setLineDash([]);

    // Angle line (red, solid)
    pctx.beginPath();
    pctx.strokeStyle = "#dc2626";
    pctx.lineWidth = 2;
    thetaHist.forEach(function(th, i) {
      var px = PAD.l + (i / HISTORY) * pw;
      var py = midY - clamp(th / (Math.PI / 2), -1, 1) * (ph / 2);
      if (i === 0) pctx.moveTo(px, py); else pctx.lineTo(px, py);
    });
    pctx.stroke();

    // Legend
    pctx.font = "10px monospace";
    pctx.textAlign = "left";
    pctx.fillStyle = "#dc2626";
    pctx.fillText("— θ (angle)", PAD.l + pw - 110, PAD.t + 11);
    pctx.fillStyle = "#2563eb";
    pctx.fillText("- - x (pos)",           PAD.l + pw - 110, PAD.t + 23);

    // X-axis labels
    pctx.fillStyle = fgDim();
    pctx.textAlign = "center";
    pctx.font = "10px monospace";
    var totalSec = HISTORY * DT;
    [0, 0.25, 0.5, 0.75, 1].forEach(function(frac) {
      var px = PAD.l + frac * pw;
      var sec = (frac - 1) * totalSec;
      pctx.fillText(sec.toFixed(0) + "s", px, H - 4);
    });
  }

  // ── Animation loop ─────────────────────────────────────────────────────────
  function loop() {
    var F = step();
    thetaHist.push(state[2]);
    xHist.push(state[0]);
    forceHist.push(F);
    if (thetaHist.length > HISTORY) { thetaHist.shift(); xHist.shift(); forceHist.shift(); }
    drawSim();
    drawPlot();
    requestAnimationFrame(loop);
  }

  // ── Controls ───────────────────────────────────────────────────────────────
  function resetPIDAngle() { integralErr  = 0; prevErr  = state[2]; }
  function resetPIDPos()   { integralErrX = 0; prevErrX = state[0]; }

  function resetAll() {
    state = [0, 0, 0.12 + (Math.random() - 0.5) * 0.08, 0];
    resetPIDAngle(); resetPIDPos();
    thetaHist = []; xHist = []; forceHist = [];
    time = 0; fallen = false; lastForce = 0;
  }

  document.getElementById("pid-reset-btn").addEventListener("click", resetAll);

  document.getElementById("pid-disturb-btn").addEventListener("click", function () {
    if (fallen) return;
    state[3] += 2.5 * (Math.random() > 0.5 ? 1 : -1);
  });

  document.getElementById("pid-zn-btn").addEventListener("click", function () {
    [["kp", PRESET_KP, 1], ["ki", PRESET_KI, 2], ["kd", PRESET_KD, 1]].forEach(function(g) {
      var el = document.getElementById("pid-" + g[0]);
      el.value = g[1];
      document.getElementById("pid-" + g[0] + "-val").textContent = g[1].toFixed(g[2]);
    });
    resetPIDAngle();
  });

  document.getElementById("pid-znx-btn").addEventListener("click", function () {
    [["kpx", PRESET_KP_X, 1], ["kix", PRESET_KI_X, 2], ["kdx", PRESET_KD_X, 1]].forEach(function(g) {
      var el = document.getElementById("pid-" + g[0]);
      el.value = g[1];
      document.getElementById("pid-" + g[0] + "-val").textContent = g[1].toFixed(g[2]);
    });
    resetPIDPos();
  });

  // Slider labels + reset integral on gain change (avoids windup artefact)
  [["kp", 1], ["ki", 2], ["kd", 1]].forEach(function(pair) {
    var id = pair[0], dec = pair[1];
    var el  = document.getElementById("pid-" + id);
    var val = document.getElementById("pid-" + id + "-val");
    el.addEventListener("input", function () {
      val.textContent = parseFloat(el.value).toFixed(dec);
      resetPIDAngle();
    });
  });

  [["kpx", 1], ["kix", 2], ["kdx", 1]].forEach(function(pair) {
    var id = pair[0], dec = pair[1];
    var el  = document.getElementById("pid-" + id);
    var val = document.getElementById("pid-" + id + "-val");
    el.addEventListener("input", function () {
      val.textContent = parseFloat(el.value).toFixed(dec);
      resetPIDPos();
    });
  });

  loop();
})();
</script>

## Learn more

- ["Advanced PID Control" by Karl J. Åström & Tore Hägglund](https://www.isa.org/products/advanced-pid-control)
- [Proportional–integral–derivative controller - Wikipedia](https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller)
- [Proportional-Integral-Derivative (PID) Controllers - MATLAB](https://www.mathworks.com/help/control/ug/proportional-integral-derivative-pid-controllers.html)
- Benjamin Recht's blog posts, emphasizing the relationship between PID and gradient-based optimization
  - [The Best Things in Life Are Model Free](https://archives.argmin.net/2018/04/19/pid/)
  - [Integral Action](https://www.argmin.net/p/integral-action)
  - [Advanced Simplicity](https://www.argmin.net/p/advanced-simplicity)

## Marimo notebook

A companion [Marimo](https://marimo.io) notebook (`knowledge_base/notebooks/pid_cartpole.py`) runs the same simulation in Python using `numpy`/`scipy` and plots the full trajectory. Run it with:

```bash
marimo run knowledge_base/notebooks/pid_cartpole.py
```

or open it interactively with:

```bash
marimo edit knowledge_base/notebooks/pid_cartpole.py
```
