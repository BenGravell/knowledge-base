Reciprocal Velocity Obstacles for Real-time Multi-agent Navigation

Topics include Collision avoidance, Multi-agent navigation, Velocity obstacles, Reciprocal planning, Real-time planning, Crowd simulation.

Introduces reciprocal velocity obstacles, where each agent assumes shared responsibility for avoiding collisions. The idea yields real-time multi-agent navigation without centralized coordination and underlies later ORCA-style collision-avoidance methods.

In this paper, we propose a new concept - the "Reciprocal Velocity Obstacle"- for real-time multi-agent navigation. We consider the case in which each agent navigates independently without explicit communication with other agents. Our formulation is an extension of the Velocity Obstacle concept, which was introduced for navigation among (passively) moving obstacles. Our approach takes into account the reactive behavior of the other agents by implicitly assuming that the other agents make a similar collision-avoidance reasoning. We show that this method guarantees safe and oscillation-free motions for each of the agents. We apply our concept to navigation of hundreds of agents in densely populated environments containing both static and moving obstacles, and we show that real-time and scalable performance is achieved in such challenging scenarios.
