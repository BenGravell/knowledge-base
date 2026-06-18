<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Quadrocopter Trajectory Generation and Control

Topics include Aerial robotics, Quadrotor control, Trajectory generation, Time-optimal control, Feasibility constraints, Online planning, Flying machine arena.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a fast trajectory-generation method for quadrotors that explicitly accounts for vehicle dynamics and input limits. The method decouples translational degrees of freedom, computes feasible time-efficient trajectories online, and converts them to control inputs for closed-loop tracking in the Flying Machine Arena.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An algorithm is presented that allows the calculation of flight trajectories for quadrocopters. Trajectory feasibility constraints regarding the vehicle dynamics and input constraints are derived. They are then used in the planning algorithm to guarantee the feasibility of generated trajectories. The translational degrees of freedom of the quadrotor are decoupled, and time-optimal trajectories are found for each degree of freedom separately. The trajectory generation is fast enough to be performed online. Control inputs are calculated from the generated trajectory, and used to achieve closed-loop control similar to model predictive control. The trajectory generation and tracking performance is demonstrated in the ETH Zurich Flying Machine Arena testbed. Experimental results show good performance, with unmodeled aerodynamic effects causing trajectory deviations when decelerating from high speeds. Development potential for the future is highlighted, focusing on improving the performance and correcting for aerodynamic effects.
