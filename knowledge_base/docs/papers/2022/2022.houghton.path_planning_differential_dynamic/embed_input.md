<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Planning: Differential Dynamic Programming and Model Predictive Path Integral Control on VTOL Aircraft

Topics include Path planning, Trajectory optimization, Differential dynamic programming, Model predictive path integral control, Uncrewed aerial vehicle, VTOL, Survey, Comparative study.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Comparative study applying DDP and MPPI trajectory optimization methods to path planning for VTOL (urban air mobility) aircraft, benchmarking their performance and practical trade-offs on this application domain.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper explores two optimal control approaches, widely used in robotics, to establish their viability as real-time trajectory planners for vehicle configurations envisioned for the emerging aviation sector of Urban Air Mobility (UAM). Differential Dynamic Programming (DDP) enables planning over highly nonlinear dynamics using second-order approximations along a nominal trajectory and displays quadratic convergence to a local solution. Model Predictive Path Integral Control (MPPI) is a stochastic sampling-based algorithm that can optimize for general cost criteria, including potentially highly nonlinear formulations, and supports parallel computation through the use of modern GPU hardware. In this work, DDP was implemented in a model predictive control (MPC) fashion alongside MPPI. The results indicate they are able to successfully transition the aircraft over different flight envelopes and generate trajectories unique to UAM vehicles.
