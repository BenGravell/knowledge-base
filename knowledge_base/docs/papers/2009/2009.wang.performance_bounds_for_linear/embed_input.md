<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Performance Bounds for Linear Stochastic Control

Topics include Stochastic control, Performance bounds, Linear systems, Linear quadratic Gaussian control, Robust control, Optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives performance bounds for linear stochastic control problems, quantifying how controller choices affect expected quadratic costs under uncertainty. The paper is mainly a theory reference for comparing achievable stochastic-control performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop computational bounds on performance for causal state feedback stochastic control with linear dynamics, arbitrary noise distribution, and arbitrary input constraint set. This can be very useful as a comparison with the performance of suboptimal control policies, which we can evaluate using Monte Carlo simulation. Our method involves solving a semidefinite program, a linear optimization problem with linear matrix inequality constraints, a convex optimization problem which can be efficiently solved. Numerical experiments show that the lower bound obtained by our method is often close to the performance achieved by several widely-used suboptimal control policies, which shows that both are nearly optimal. As a by-product, our performance bound yields approximate value functions that can be used as control Lyapunov functions for suboptimal control policies.
