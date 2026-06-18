PBP: Path-based Trajectory Prediction for Autonomous Driving

Trajectory prediction plays a crucial role in the autonomous driving stack by enabling autonomous vehicles to anticipate the motion of surrounding agents. Goal-based prediction models have gained traction in recent years for addressing the multimodal nature of future trajectories. Goal-based prediction models simplify multimodal prediction by first predicting 2D goal locations of agents and then predicting trajectories conditioned on each goal. However, a single 2D goal location serves as a weak inductive bias for predicting the whole trajectory, often leading to poor map compliance, i.e., part of the trajectory going off-road or breaking traffic rules. In this paper, we improve upon goal-based prediction by proposing the Path-based prediction (PBP) approach. PBP predicts a discrete probability distribution over reference paths in the HD map using the path features and predicts trajectories in the path-relative Frenet frame. We applied the PBP trajectory decoder on top of the HiVT scene encoder and report results on the Argoverse dataset....

## Introduction

To safely navigate through traffic while offering passengers a smooth ride, autonomous vehicles need the ability to predict the trajectories of surrounding agents. There is inherent uncertainty in predicting the future, making this a challenging task. Agent trajectories tend to be highly non-linear over long prediction horizons. Additionally, the distribution of future trajectories is multimodal; in a given scene an agent could have multiple plausible goals and could take various paths to each goal.

In spite of these challenges, agent motion is not completely unconstrained. Vehicles tend to follow the direction of motion ascribed to their lanes, make legal turns and lane changes, and stop at stop signs and crosswalks. Bicyclists tend to use the bike lane, and pedestrians tend to walk along sidewalks and crosswalks. High-definition (HD) maps of traffic scenes efficiently represent such constraints on agent motion and have thus been a critical component of autonomous driving datasets....

## Conclusion

In this paper, we propose PBP, a novel path-based prediction approach. In contrast to the traditional goal-based prediction approaches, PBP performs classification on the whole reference path instead of just the goal endpoint. The additional reference path information improves the path classification accuracy and allows PBP to decode trajectories in the path-relative Frenet frame....

We concatenate the agent feature ${\mathbf{F}}_{a}$, path feature ${\mathbf{F}}_{p}$, and agent-path pair feature ${\mathbf{F}}_{a,{(p,i)}}$ together and run them through another MLP network to predict the probability distribution over all candidate paths of the agent, trained with the cross-entropy loss as $\mathcal{L}_{cls}$. We decide the ground-truth reference path $r_{GT}^{a}$ of the agent $a$ based on its ground-truth future trajectory ${\{{\mathbf{P}}^{a}\}}_{Future}$, similar to the ground-truth goal selection in goal-based prediction....

### III-B Overall architecture

### IV-A Dataset

Prior works have leveraged HD maps for trajectory prediction in two distinct ways. First, the HD map is often used as an input to the model. Early works use rasterized HD maps and CNN encoders. More recent works directly encode vectorized HD maps using PointNet encoders, graph neural networks \[\] or transformer layers....
