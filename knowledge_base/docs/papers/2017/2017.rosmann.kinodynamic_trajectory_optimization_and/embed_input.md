<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kinodynamic Trajectory Optimization and Control for Car-Like Robots

Topics include Trajectory optimization, Timed elastic Band, Kinodynamic planning, Car-like robots, Motion planning, Autonomous driving.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the Timed Elastic Band (TEB) local planner to handle kinodynamic constraints for car-like (Ackermann-steered) robots. Optimizes trajectories over time-parameterized elastic bands subject to nonholonomic constraints, enabling smooth and feasible path following for vehicles with curvature limitations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel generic formulation of Timed-Elastic-Bands for efficient online motion planning of car-like robots. The planning problem is defined in terms of a finite-dimensional and sparse optimization problem subject to the robots kinodynamic constraints and obstacle avoidance. Control actions are implicitly included in the optimized trajectory. Reliable navigation in dynamic environments is accomplished by augmenting the inner optimization loop with state feedback. The predictive control scheme is real-time capable and responds to obstacles within the robot's perceptual field. Navigation in large and complex environments is achieved in a pure pursuit fashion by requesting intermediate goals from a global planner. Requirements on the initial global path are fairly mild, compliance with the robot kinematics is not required. A comparative analysis with Reeds and Shepp curves and investigation of prototypical car maneuvers illustrate the advantages of the approach.
