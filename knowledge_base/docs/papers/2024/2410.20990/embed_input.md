Reference-Free Formula Drift with Reinforcement Learning: From Driving Data to Tire Energy-Inspired, Real-World Policies

The skill to drift a car - i.e., operate in a state of controlled oversteer like professional drivers - could give future autonomous cars maximum flexibility when they need to retain control in adverse conditions or avoid collisions. We investigate real-time drifting strategies that put the car where needed while bypassing expensive trajectory optimization. To this end, we design a reinforcement learning agent that builds on the concept of tire energy absorption to autonomously drift through changing and complex waypoint configurations while safely staying within track bounds. We achieve zero-shot deployment on the car by training the agent in a simulation environment built on top of a neural stochastic differential equation vehicle model learned from pre-collected driving data. Experiments on a Toyota GR Supra and Lexus LC 500 show that the agent is capable of drifting smoothly through varying waypoint configurations with tracking error as low as 10 cm while stably pushing the vehicles to sideslip angles of up to 63°.

## Introduction

Existing autonomous vehicles are constrained to operate in a conservative driving envelope with low lateral accelerations. However, in certain situations, it may be necessary to temporarily operate the vehicle beyond its natural stability limits to avoid a collision. This style of driving is exemplified by drifting, a challenging cornering technique that involves deliberately saturating the rear tires to make the car slide while countersteering to maintain high sideslip angles. Skilled human drivers display incredible vehicle control and agility in drifting competitions, routinely sliding their cars within inches of concrete walls.

We present the first RL-based drifting approach that

We validate the proposed approach on a full-size Toyota GR Supra and Lexus LC 500. Our results show strong sim-to-real transfer capabilities, high agility, and high waypoint tracking accuracy on several tracks, including those in Figure.

## Conclusion

We propose the first RL-based drifting approach applied to a full-size vehicle that can drift, without a reference trajectory, across a general path defined by waypoints, all while pushing the car to its limits of agility through the principle of maximum tire energy absorption. Extensive experiments with a Toyota GR Supra and Lexus LC 500 demonstrate the effectiveness of the approach.

Although we show promising results in using RL to navigate through complex waypoint configurations with high agility, the current formulation, similar to existing approaches, depends on full state estimation and precise track information. Future research could investigate drifting policies that work by fusing partial state estimates and visual-based measurements from LiDAR or RGB-D cameras. Other interesting future research directions are policies that leverage brake actuators to improve stability and flexibility, adapt to changes in road conditions, and generalize across different platforms or tracks.
