<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Simultaneous Self-calibration and Navigation Using Trajectory Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a trajectory optimization framework that maximizes observability of one or more user-chosen states in a nonlinear system. Our framework is based on a novel metric for quality of observability that is state-estimator agnostic and offers improved numerical stability over prior methods in some cases where the states of interest do not appear directly in the observation. We apply this metric to trajectory optimization problems for closed-loop self-calibration, maintaining observability while navigating through an environment, and rapidly modifying an already-planned trajectory for online recalibration. We include a statistical procedure to balance observability of several states with heterogeneous units and magnitudes. As an example, we apply our framework to online calibration of GPS–IMU and visual–inertial navigation systems on a quadrotor helicopter. Extensive simulations and a real-robot experiment demonstrate the effectiveness of our framework, showing better convergence of the states and the resulting higher precision in navigation.
