<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Polynomial Trajectory Planning for Aggressive Quadrotor Flight in Dense Indoor Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We explore the challenges of planning trajectories for quadrotors through cluttered indoor environments. We extend the existing work on polynomial trajectory generation by presenting a method of jointly optimizing polynomial path segments in an unconstrained quadratic program that is numerically stable for high-order polynomials and large numbers of segments, and is easily formulated for efficient sparse computation. We also present a technique for automatically selecting the amount of time allocated to each segment, and hence the quadrotor speeds along the path, as a function of a single parameter determining aggressiveness, subject to actuator constraints. The use of polynomial trajectories, coupled with the differentially flat representation of the quadrotor, eliminates the need for computationally intensive sampling and simulation in the high dimensional state space of the vehicle during motion planning. Our approach generates high-quality trajecrtories much faster than purely sampling-based optimal kinodynamic planning methods, but sacrifices the guarantee of asymptotic convergence to the global optimum that those methods provide. We demonstrate the performance of our algorithm by efficiently generating trajectories through challenging indoor spaces and successfully traversing them at speeds up to 8 m/s.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A demonstration of our algorithm and flight performance is available :.
