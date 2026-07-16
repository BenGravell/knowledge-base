<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite-Sample Closed-Loop Stability of Model Predictive Path Integral Control for Linear Time-Invariant Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We establish finite-sample closed-loop stability guarantees for Model Predictive Path Integral (MPPI) control applied to discrete-time Linear Time-Invariant (LTI) systems with additive Gaussian process disturbances. The key observation is that, for unconstrained LTI/quadratic systems with the DARE terminal cost, the exact finite-horizon MPC law has the same first control action as the infinite-horizon LQR law for every planning horizon. Thus, finite-sample MPPI can be analyzed as a stochastic perturbation of LQR. First, we show that the MPPI control law approximates the LQR feedback with high probability. The approximation error decomposes into a Monte Carlo term that decreases with the sample count and an infinite-sample temperature bias that persists at finite temperature but vanishes as the temperature is reduced. The resulting constants are written in terms of the horizon-dependent stacked cost matrices, making explicit that the finite-sample certificate is parametrized by the selected planning horizon. Second, we use a Lyapunov perturbation argument to prove practical exponential stability in expectation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On sample paths that remain in a compact Lyapunov sublevel set over a finite operating horizon, the expected state norm decays exponentially up to three residual floors: a process-noise floor, an MPPI approximation floor, and a confidence floor from the per-step sampling failure probability. The sufficient sample threshold is explicit and computable from the DARE solution, LQR stability margin, MPPI sampling parameters, temperature, and planning horizon. In the joint limit of infinite samples and vanishing temperature bias, the result recovers the stochastic LQR stability bound.
