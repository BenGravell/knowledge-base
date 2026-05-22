# LQR

The *Linear Quadratic Regulator (LQR)* is an optimal feedback control scheme for linear systems with quadratic state and input costs.

The demo solves the discrete algebraic Riccati equation in the browser and redraws the closed-loop response as the penalties change.

<link rel="stylesheet" href="lqr.css">

<div id="lqr" class="lqr" data-lqr>
  <section class="lqr-plot-panel" aria-label="Closed-loop system response">
    <div class="lqr-panel-head">
      <h2>System Response</h2>
      <div class="lqr-legend" aria-label="Plot legend">
        <span><i class="lqr-swatch lqr-swatch-state-1"></i>State 1</span>
        <span><i class="lqr-swatch lqr-swatch-state-2"></i>State 2</span>
        <span><i class="lqr-swatch lqr-swatch-input"></i>Input</span>
      </div>
    </div>
    <svg id="lqr-plot" class="lqr-plot" viewBox="0 0 900 360" role="img" aria-labelledby="lqr-plot-title lqr-plot-desc">
      <title id="lqr-plot-title">Closed-loop LQR response</title>
      <desc id="lqr-plot-desc">Line plot of two states and one control input over one second.</desc>
    </svg>
  </section>

  <section class="lqr-readout-grid" aria-label="Computed LQR values">
    <div class="lqr-readout">
      <div class="lqr-readout-label">Gain</div>
      <div class="lqr-code" id="lqr-gain"></div>
    </div>
    <div class="lqr-readout">
      <div class="lqr-readout-label">Closed-loop Eigenvalues</div>
      <div class="lqr-code" id="lqr-eigs"></div>
    </div>
    <div class="lqr-readout">
      <div class="lqr-readout-label">Peak Input</div>
      <div class="lqr-code" id="lqr-peak-input"></div>
    </div>
    <div class="lqr-readout">
      <div class="lqr-readout-label">Settling Time</div>
      <div class="lqr-code" id="lqr-settle-time"></div>
    </div>
  </section>

  <section class="lqr-matrix-grid" aria-label="System matrices">
    <div class="lqr-matrix">
      <div class="lqr-matrix-label">A</div>
      <div id="lqr-matrix-a"></div>
    </div>
    <div class="lqr-matrix">
      <div class="lqr-matrix-label">B</div>
      <div id="lqr-matrix-b"></div>
    </div>
    <div class="lqr-matrix">
      <div class="lqr-matrix-label">Q</div>
      <div id="lqr-matrix-q"></div>
    </div>
    <div class="lqr-matrix">
      <div class="lqr-matrix-label">R</div>
      <div id="lqr-matrix-r"></div>
    </div>
  </section>

  <section class="lqr-controls" aria-label="LQR penalty controls">
    <div class="lqr-control-head">
      <h2>Penalty Weights</h2>
      <div class="lqr-status" id="lqr-status">Ready</div>
    </div>

    <div class="lqr-slider-grid">
      <label class="lqr-slider">
        <span>State 1</span>
        <input id="lqr-q1" type="range" min="0" max="5" step="0.1" value="2">
        <output id="lqr-q1-value">2.0</output>
      </label>
      <label class="lqr-slider">
        <span>State 2</span>
        <input id="lqr-q2" type="range" min="0" max="5" step="0.1" value="2">
        <output id="lqr-q2-value">2.0</output>
      </label>
    </div>

    <div class="lqr-action-row">
      <button type="button" id="lqr-reset">Reset</button>
    </div>
  </section>
</div>

<script src="lqr.js"></script>

## What To Notice

Increasing a state penalty makes deviations in that state more expensive, so the controller spends more input to drive it down. The input penalty is fixed at \(R = 1.0\), so the sliders expose the trade-off between the two state coordinates rather than the state-input trade-off.

The readout shows the **5% settling time**: the time after which every system state remains within 5% of its initial deviation from its steady-state value. We initialize all states to 1 and this is a regulation task with all steady-state values zero, so the 5% band is at \(\pm 0.05\).

The discrete-time system has linear dynamics

$$
x_{k+1} = A x_k + B u_k
$$

where

$$
A = I + 0.01 \begin{bmatrix}-2 & 13 \\\\ 4 & -3\end{bmatrix},
\qquad
B = 0.01 \begin{bmatrix}2 \\\\ 8\end{bmatrix}.
$$

For each setting, the browser solves the discrete algebraic Riccati equation

$$
P = Q + A^\top P A - A^\top P B(R + B^\top P B)^{-1}B^\top P A
$$

calculates the gain matrix

$$
K = -(R + B^\top P B)^{-1}B^\top P A.
$$

and simulates the system in closed-loop under the feedback policy

$$
u_t = K x_t
$$

## Links

- [LQR source](https://github.com/BenGravell/lqr-designer)
- [Underactuated Robotics: Linear Quadratic Regulators](https://underactuated.mit.edu/lqr.html)
- [Stanford EE363 lecture slides](https://web.stanford.edu/class/ee363/lectures.html)
