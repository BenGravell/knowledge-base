<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fail-Safe Motion Planning of Autonomous Vehicles

Topics include Autonomous driving, Safe planning, Safety verification, Reachability analysis, Obstacle avoidance, Contingency plan, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a planning architecture that keeps an emergency stop maneuver available while optimizing nominal vehicle motion. Its main value is the explicit pairing of performance-oriented trajectory generation with occupancy-based safety envelopes for unexpected traffic behavior.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Formally verified methods for motion planning are required in order to guarantee safety for autonomous vehicles. In particular, we consider trajectory generation by considering the most probable trajectory of other traffic participants. However, if the surrounding vehicles perform unexpected maneuvers, a collision might be inevitable. In this paper, a fail-safe motion planner is developed, which generates optimal trajectories, yet guarantees safety at all times. Safety is achieved by maintaining an emergency maneuver which can safely bring the host vehicle to a stop while avoiding any collision. The emergency maneuver is computed by considering for a given time horizon the occupancy prediction which encloses all possible trajectories of the other traffic participants. The performance of the approach is evaluated through simulation against real traffic data.
