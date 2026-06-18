<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimum Snap Trajectory Generation and Control for Quadrotors

Topics include Minimum snap trajectories, Quadrotor control, Trajectory generation, Differential flatness, Aerial robotics, Polynomial trajectories, Nonlinear control, Indoor flight.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the minimum-snap trajectory formulation for quadrotors, exploiting flat outputs to generate smooth polynomial trajectories through waypoints while respecting corridor and dynamic constraints. Coupled with a nonlinear controller, the method enabled aggressive indoor slalom flight and became a foundational quadrotor trajectory-generation reference.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We address the controller design and the trajectory generation for a quadrotor maneuvering in three dimensions in a tightly constrained setting typical of indoor environments. In such settings, it is necessary to allow for significant excursions of the attitude from the hover state and small angle approximations cannot be justified for the roll and pitch. We develop an algorithm that enables the real-time generation of optimal trajectories through a sequence of 3-D positions and yaw angles, while ensuring safe passage through specified corridors and satisfying constraints on velocities, accelerations and inputs. A nonlinear controller ensures the faithful tracking of these trajectories. Experimental results illustrate the application of the method to fast motion (5-10 body lengths/second) in three-dimensional slalom courses.
