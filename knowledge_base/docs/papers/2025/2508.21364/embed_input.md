Multi-Modal Model Predictive Path Integral Control for Collision Avoidance

Topics include Model predictive path integral control, Trajectory optimization, Collision avoidance, Multimodal, Sampling-based control.

Extends MPPI to handle multimodal trajectory distributions for collision avoidance, enabling the controller to simultaneously explore multiple qualitatively different trajectory groups (homotopy classes) rather than collapsing to a single mode.

This paper proposes a novel approach to motion planning and decision-making for automated vehicles, using a multi-modal Model Predictive Path Integral control algorithm. The method samples with Sobol sequences around the prior input and incorporates analytical solutions for collision avoidance. By leveraging multiple modes, the multi-modal control algorithm explores diverse trajectories, such as manoeuvring around obstacles or stopping safely before them, mitigating the risk of sub-optimal solutions. A non-linear single-track vehicle model with a Fiala tyre serves as the prediction model, and tyre force constraints within the friction circle are enforced to ensure vehicle stability during evasive manoeuvres. The optimised steering angle and longitudinal acceleration are computed to generate a collision-free trajectory and to control the vehicle....
