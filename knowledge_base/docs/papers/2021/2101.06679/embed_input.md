End-to-end Interpretable Neural Motion Planner

In this paper, we propose a neural motion planner (NMP) for learning to drive autonomously in complex urban scenarios that include traffic-light handling, yielding, and interactions with multiple road-users. Towards this goal, we design a holistic model that takes as input raw LIDAR data and a HD map and produces interpretable intermediate representations in the form of 3D detections and their future trajectories, as well as a cost volume defining the goodness of each position that the self-driving car can take within the planning horizon. We then sample a set of diverse physically possible trajectories and choose the one with the minimum learned cost. Importantly, our cost volume is able to naturally capture multi-modality. We demonstrate the effectiveness of our approach in real-world driving data captured in several cities in North America. Our experiments show that the learned cost volume can generate safer planning than all the baselines.

## Introduction

Self-driving vehicles (SDVs) are going to revolutionize the way we live. Building reliable SDVs at scale is, however, not a solved problem. As is the case in many application domains, the field of autonomous driving has been transformed in the past few years by the success of deep learning. Existing approaches that leverage this technology can be characterized into two main frameworks: end-to-end driving and traditional engineering stacks.

Figure 1: Our end-to-end interpretable neural motion planner (NMP). Backbone network takes LiDAR data and maps as inputs, and outputs bounding boxes of other actors for future timesteps (perception), as well as a cost volume for planning with T filters. Next, for each trajectory proposal from the sampler, its cost is indexed from different filters of the cost volume and summed together. The trajectory with the minimal cost will be our final planning.

## Conclusion

We have proposed a neural motion planner that learns to drive safely while following traffic rules. We have designed a holistic model that takes LiDAR data and an HD map and produces interpretable intermediate representations in the form of 3D detections and their future trajectories, as well as a cost map defining the goodness of each position that the self-driving car can take within the planning horizon. Our planer then sample a set of physically possible trajectories and chooses the one with the minimum learned cost....

Here, $\mathbf{s}{(\xi)}$ defines a Clothoid curve on a 2D plane, indexed by the distance $\xi$ to reference point $\mathbf{s}_{\mathbf{0}}$, $a$ is a scaling factor, $\mathbf{T}_{\mathbf{0}}$ and $\mathbf{N}_{\mathbf{0}}$ are the tangent and normal vector of this curve at point $\mathbf{s}_{\mathbf{0}}$. $S{(\xi)}$ and $C{(\xi)}$ are called the Fresnel integral, and can be efficiently computed....

Access to a map is also a key for accurate motion planning, as we need to drive according to traffic rules (e.g., stop at a red light, follow the lane, change lanes only when allowed). Towards this goal, we exploit HD maps that contain information about the semantics of the scene such as the location of lanes, their boundary type (e.g., solid, dashed) and the location of stop signs....
