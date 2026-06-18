<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Friction-Adaptive Stochastic Nonlinear Model Predictive Control for Autonomous Vehicles

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper addresses the trajectory-tracking problem under uncertain road-surface conditions for autonomous vehicles. We propose a stochastic nonlinear model predictive controller (SNMPC) that learns a tire-road friction model online using standard automotive-grade sensors. Learning the entire tire-road friction model in real time requires driving in the nonlinear, potentially unstable regime of the vehicle dynamics, using a prediction model that may not have fully converged. To handle this, we formulate the tire-friction model learning in a Bayesian framework, and propose two estimators that learn different aspects of the tire-road friction. The estimators output the estimate of the tire-friction model as well as the uncertainty of the estimate, which expresses the confidence in the model for different driving regimes. The SNMPC exploits the uncertainty estimate in its prediction model to take proper action when the uncertainty is large. We validate the approach in an extensive Monte-Carlo study using real vehicle parameters and in CarSim. The results when comparing to various MPC approaches indicate a substantial reduction in constraint violations, as well as a reduction in closed-loop cost.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also demonstrate the real-time feasibility in automotive-grade processors using a dSPACE MicroAutoBox-II rapid prototyping unit, showing a worst-case computation time of roughly 40ms.
