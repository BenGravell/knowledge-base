<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Motion Planning with the Half-car Dynamical Model for Autonomous High-speed Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We discuss an implementation of the RRT* optimal motion planning algorithm for the half-car dynamical model to enable autonomous high-speed driving. To develop fast solutions of the associated local steering problem, we observe that the motion of a special point (namely, the front center of oscillation) can be modeled as a double integrator augmented with fictitious inputs. We first map the constraints on tire friction forces to constraints on these augmented inputs, which provides instantaneous, state-dependent bounds on the curvature of geometric paths feasibly traversable by the front center of oscillation. Next, we map the vehicle's actual inputs to the augmented inputs. The local steering problem for the half-car dynamical model can then be transformed to a simpler steering problem for the front center of oscillation, which we solve efficiently by first constructing a curvature-bounded geometric path and then imposing a suitable speed profile on this geometric path. Finally, we demonstrate the efficacy of the proposed motion planner via numerical simulation results.
