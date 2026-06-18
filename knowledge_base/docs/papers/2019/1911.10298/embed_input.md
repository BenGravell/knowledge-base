CoverNet: Multimodal Behavior Prediction Using Trajectory Sets

We present CoverNet, a new method for multimodal, probabilistic trajectory prediction for urban driving. Previous work has employed a variety of methods, including multimodal regression, occupancy maps, and 1-step stochastic policies. We instead frame the trajectory prediction problem as classification over a diverse set of trajectories. The size of this set remains manageable due to the limited number of distinct actions that can be taken over a reasonable prediction horizon. We structure the trajectory set to a) ensure a desired level of coverage of the state space, and b) eliminate physically impossible trajectories. By dynamically generating trajectory sets based on the agent's current state, we can further improve our method's efficiency. We demonstrate our approach on public, real-world self-driving datasets, and show that it outperforms state-of-the-art methods.

## Introduction

We are motivated by autonomous systems operating in dynamic, interactive, and uncertain environments. Specifically, we focus on the problem of a self-driving car navigating in an urban environment, where it must share the road with a diverse set of other agents, including vehicles, bicyclists, and pedestrians. In this context, reasoning about the possible future states of agents is critical for safe and confident operation. Effective prediction of future agent states depends on both road context (e.g., lane geometry, crosswalks, traffic lights) and the recent behavior of other agents.

Trajectory prediction is inherently challenging due to a wide distribution of agent preferences (e.g., a cautious vs. aggressive) and intents (e.g., turn right vs. go straight). Useful predictions must represent multiple possibilities and their associated likelihoods. Furthermore, we expect that predicted trajectories are physically realizable.

## Conclusion

We introduced CoverNet, a novel method for multimodal, probabilistic trajectory prediction in real-world, urban driving scenarios. By framing this problem as classification over a diverse set of trajectories, we were able to a) ensure a desired level of coverage of the state space, b) eliminate dynamically infeasible trajectories, and c) avoid the issue of mode collapse. We showed that the size of our trajectory sets remain manageable over realistic prediction horizons. Dynamically generating trajectory sets based on the agent's current state further improved performance....

Physics oracle. We introduce a simple and interpretable model that extends classic physics-based models. We use the track's current velocity, acceleration, and yaw rate to compute the following predictions: i) constant velocity and yaw, ii) constant velocity and yaw rate, iii) constant acceleration and yaw, and iv) constant acceleration and yaw rate. The *oracle* is the minimum average point-wise Euclidean distance over the four models.

Figure 2: Overview of trajectory set generation approaches.

Our internal datasets have $F = {10\ Hz}$, while the publicly available nuScenes is sampled at $F = {2\ Hz}$. We include results on two different prediction horizon lengths, namely $H = 3$ seconds and $H = 6$ seconds.

Multimodal regression models appear naturally suited for this task, but may degenerate during training into a single...
