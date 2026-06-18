DriveIRL: Driving in Real Life with Inverse Reinforcement Learning

Topics include Autonomous driving, Inverse reinforcement learning, Motion planning, Imitation learning, Real-world deployment.

Inverse Reinforcement Learning-based planner demonstrated on a real self-driving car in dense urban traffic. Trained on large-scale human driving logs. The architecture design is critical to the success of the approach: there is a classical trajectory generator (based on Dubins paths, pre-computed acceleration profiles, and access to a clean road geometry model) capable of generating diverse safe trajectories, a safety filter that removes all trajectory candidates that are not forward recursively safe, and the learned model is only for assigning scores to the safety-filtered trajectory candidates. Includes a useful set of standardized evaluation metrics for learned planners (see Appendix A.5).

In this paper, we introduce the first published planner to drive a car in dense, urban traffic using Inverse Reinforcement Learning (IRL). Our planner, DriveIRL, generates a diverse set of trajectory proposals and scores them with a learned model. The best trajectory is tracked by our self-driving vehicle's low-level controller. We train our trajectory scoring model on a 500+ hour real-world dataset of expert driving demonstrations in Las Vegas within the maximum entropy IRL framework. DriveIRL's benefits include: a simple design due to only learning the trajectory scoring function, a flexible and relatively interpretable feature engineering approach, and strong real-world performance. We validated DriveIRL on the Las Vegas Strip and demonstrated fully autonomous driving in heavy traffic, including scenarios involving cut-ins, abrupt braking by the lead vehicle, and hotel pickup/dropoff zones. Our dataset, a part of nuPlan, has been released to the public to help further research in this area.

## Introduction

Self-driving cars have been the focus of significant research and development over the past decade. Some companies are tantalizingly close to deploying commercial self-driving taxi services that would make urban transportation cheaper and safer. Progress in self-driving cars has been largely driven by new datasets that helped fuel dramatic improvements in machine learning approaches to object detection and motion forecasting. However, the critical motion planning and decision-making algorithms that ultimately determine driving behavior have yet to see similar benefits from machine learning.

Classical planning and decision-making algorithms for self-driving cars rely heavily on hand-engineered components. Developers will typically hand-tune the scoring function that determines which behaviors are desirable. Manually adjusting features and weights can be a painstaking process -- improving performance in one area often causes unintended regressions elsewhere. Our planner avoids the need to manually craft detailed features or tune weights by learning these components from expert demonstrations using a maximum entropy IRL framework.

## Conclusions

We introduced DriveIRL: the first learning-based planner to control a car in dense, urban traffic using inverse reinforcement learning. By designing an architecture split into ego trajectory *generation*, *checking*, and *scoring*, we were able to leverage simple and reliable methods for the relatively easy tasks of trajectory generation and safety checking. This architecture allowed the trajectory scoring component of our system to focus on learning nuanced driving behavior important for good performance in dense traffic....

MaxJerk: the maximum jerk ($\ {m/s^{3}}$) along the trajectory.

### Safety filter

We evaluate our model using a variety of metrics to give a full picture of driving. To approximate real-world conditions, we perform a closed-loop replay for each scenario for a duration of 10 seconds. We initialize the ego at the start of the scene, compute a planned trajectory, move along that trajectory for one step, replay the other agents, and repeat. Then, we compute metrics on the resulting executed trajectory as averages over the full scene duration.

Our DriveIRL system works by *generating*, *checking*, and *scoring* trajectories for our vehicle....
