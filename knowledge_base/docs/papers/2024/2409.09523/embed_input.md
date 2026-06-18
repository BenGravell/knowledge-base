Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-World Environments

Topics include Motion planning, Autonomous driving, Trajectory optimization, Safety, Real-world deployment, Experimentation.

Optimization-based wrapper that converts any planner's trajectory sketch into a safe, comfortable, dynamically feasible trajectory, enabling rapid real-world testing of experimental ML and classical planners on self-driving vehicles without full safety-stack integration.

Human-level autonomous driving is an ever-elusive goal, with planning and decision making - the cognitive functions that determine driving behavior - posing the greatest challenge. Despite a proliferation of promising approaches, progress is stifled by the difficulty of deploying experimental planners in naturalistic settings. In this work, we propose Lab2Car, an optimization-based wrapper that can take a trajectory sketch from an arbitrary motion planner and convert it to a safe, comfortable, dynamically feasible trajectory that the car can follow. This allows motion planners that do not provide such guarantees to be safely tested and optimized in real-world environments. We demonstrate the versatility of Lab2Car by using it to deploy a machine learning (ML) planner and a classical planner on self-driving cars in Las Vegas. The resulting systems handle challenging scenarios, such as cut-ins, overtaking, and yielding, in complex urban environments like casino pick-up/drop-off areas. Our work paves the way for quickly deploying and evaluating candidate motion planners in realistic settings, ensuring rapid iteration and accelerating progress towards human-level autonomy.

## Introduction

Self-driving cars have achieved remarkable progress towards human-level autonomous driving. Much of this success is owed to progress in ML-based perception and prediction, which can attain a human-like understanding of the scene around the autonomous vehicle (AV). Classical motion planners relying on handcrafted rules have similarly given way to ML-based motion planners that learn the rules of driving from data. ML planning is thought to be more scalable and better positioned to capture the ineffable nuances of human driving behavior than classical planning.

However, deploying ML planners in the real world comes with its own set of challenges, which are often overcome using techniques from classical planning. For one, naïve trajectory regression does not ensure comfort or even basic kinematic feasibility, necessitating post-hoc smoothing or hand-engineered trajectory generation. Ensuring safety poses an even greater challenge, as ML solutions tend to fail on edge cases that compose the long tail of the data distribution....

We envision two use cases for Lab2Car: as training wheels and as a planning component in its own right. For example, an under-trained Urban Driver can be initially deployed with the Stay-behind configuration. This can provide early signal for on-road issues that would be difficult to detect in simulation, such as issues with comfort or starting from stop. Unsafe behavior masked by Lab2Car can be revealed by examining discrepancies between the trajectory sketch and the final trajectory, as well as by resimulation....

Lab2Car streamlines the path from incubating an idea in the lab to testing it on the car, offering early insights into the real-world performance of experimental planners at the initial stages of prototyping. This can allow researchers in academia and industry to focus on promising ideas and rule out dead ends before investing too much effort in polishing them. We believe this can dramatically accelerate progress towards resolving the planning bottleneck in autonomous driving and making a driverless future for all a reality.

## MPC formulation

Detections and predictions for other dynamic road entities, such as vehicles and pedestrians, are represented by time series of convex hulls subsampled to sets of $(x,y)$ points....
