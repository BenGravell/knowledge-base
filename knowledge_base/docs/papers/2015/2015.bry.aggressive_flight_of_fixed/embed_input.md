<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Aggressive Flight of Fixed-wing and Quadrotor Aircraft in Dense Indoor Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we describe trajectory planning and state estimation algorithms for aggressive flight of micro aerial vehicles in known, obstacle-dense environments. Finding aggressive but dynamically feasible and collision-free trajectories in cluttered environments requires trajectory optimization and state estimation in the full state space of the vehicle, which is usually computationally infeasible on realistic timescales for real vehicles and sensors. We first build on previous work of van Nieuwstadt and Murray and Mellinger and Kumar, to show how a search process can be coupled with optimization in the output space of a differentially flat vehicle model to find aggressive trajectories that utilize the full maneuvering capabilities of a quadrotor. We further extend this work to vehicles with complex, Dubins-type dynamics and present a novel trajectory representation called a “Dubins–Polynomial trajectory”, which allows us to optimize trajectories for fixed-wing vehicles. To provide accurate state estimation for aggressive flight, we show how the Gaussian particle filter can be extended to allow laser rangefinder localization to be combined with a Kalman filter. This formulation allows similar estimation accuracy to particle filtering in the full vehicle state but with an order of magnitude more efficiency.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We conclude with experiments demonstrating the execution of quadrotor and fixed-wing trajectories in cluttered environments. We show results of aggressive flight at speeds of up to 8 m/s for the quadrotor and 11 m/s for the fixed-wing aircraft.
