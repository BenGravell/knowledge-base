PBP: Path-based Trajectory Prediction for Autonomous Driving

Trajectory prediction plays a crucial role in the autonomous driving stack by enabling autonomous vehicles to anticipate the motion of surrounding agents. Goal-based prediction models have gained traction in recent years for addressing the multimodal nature of future trajectories. Goal-based prediction models simplify multimodal prediction by first predicting 2D goal locations of agents and then predicting trajectories conditioned on each goal. However, a single 2D goal location serves as a weak inductive bias for predicting the whole trajectory, often leading to poor map compliance, i.e., part of the trajectory going off-road or breaking traffic rules. In this paper, we improve upon goal-based prediction by proposing the Path-based prediction (PBP) approach. PBP predicts a discrete probability distribution over reference paths in the HD map using the path features and predicts trajectories in the path-relative Frenet frame. We applied the PBP trajectory decoder on top of the HiVT scene encoder and report results on the Argoverse dataset.

## Introduction

To safely navigate through traffic while offering passengers a smooth ride, autonomous vehicles need the ability to predict the trajectories of surrounding agents. There is inherent uncertainty in predicting the future, making this a challenging task. Agent trajectories tend to be highly non-linear over long prediction horizons. Additionally, the distribution of future trajectories is multimodal; in a given scene an agent could have multiple plausible goals and could take various paths to each goal.

In spite of these challenges, agent motion is not completely unconstrained. Vehicles tend to follow the direction of motion ascribed to their lanes, make legal turns and lane changes, and stop at stop signs and crosswalks. Bicyclists tend to use the bike lane, and pedestrians tend to walk along sidewalks and crosswalks. High-definition (HD) maps of traffic scenes efficiently represent such constraints on agent motion and have thus been a critical component of autonomous driving datasets.

In this work, we seek to improve upon goal-based trajectory prediction. We argue that reference paths rather than 2D goals are the appropriate HD map element to condition predicted trajectories. We define reference paths as segments of lane centerlines close to the agent of interest that the agent may follow over the prediction horizon. We propose a novel path classifier that predicts a discrete probability distribution over the candidate reference paths and a trajectory completion module that predicts trajectories conditioned on each path in the Frenet frame. Figure shows an overview of our approach.

We propose a novel path-based trajectory prediction (PBP) approach that improves upon traditional goal-based prediction.

We present extensive ablation studies comparing different trajectory decoder approaches on the Argoverse validation set.

## Conclusion

In this paper, we propose PBP, a novel path-based prediction approach. In contrast to the traditional goal-based prediction approaches, PBP performs classification on the whole reference path instead of just the goal endpoint. The additional reference path information improves the path classification accuracy and allows PBP to decode trajectories in the path-relative Frenet frame.
