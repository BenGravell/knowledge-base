Differentiable Integrated Motion Prediction and Planning with Learnable Cost Function for Autonomous Driving

Predicting the future states of surrounding traffic participants and planning a safe, smooth, and socially compliant trajectory accordingly is crucial for autonomous vehicles. There are two major issues with the current autonomous driving system: the prediction module is often separated from the planning module and the cost function for planning is hard to specify and tune. To tackle these issues, we propose a differentiable integrated prediction-planning framework (DIPP) that can also learn the cost function from data. Specifically, our framework uses a differentiable nonlinear optimizer as the motion planner, which takes as input the predicted trajectories of surrounding agents given by the neural network and optimizes the trajectory for the autonomous vehicle, enabling all operations to be differentiable, including the cost function weights. The proposed framework is trained on a large-scale real-world driving dataset to imitate human driving trajectories in the entire driving scene and validated in both open-loop and closed-loop manners.

## Introduction

Making safe, socially-compatible, and human-like decisions is a fundamental capability of autonomous vehicles (AVs). While learning-based end-to-end decision-making methods, such as imitation learning and reinforcement learning, have enjoyed vigorous growth recently, they still lack interpretability, robustness, and safety compared to classic planning-based methods. Nonetheless, to make safe and smooth plans in complex traffic scenarios, the key is to accurately forecast the future trajectories of surrounding traffic participants.

In this paper, we propose a novel framework called differentiable integrated prediction and planning (DIPP), as shown in Fig. 1(c). The objective of the DIPP framework is to make the prediction module aware of the downstream planning task, so as to deliver planning-aware prediction results to the motion planner, without altering the established structure of the prediction-planning process.

In

We propose a fully differentiable structured learning framework that integrates prediction and planning modules for autonomous driving, enabling the prediction results better fit to the downstream planning task and the cost function learnable from real-world driving data.

We demonstrate that the proposed framework outperforms the baseline methods in both open-loop and closed-loop tests and conduct an ablation study to investigate the importance of each component.
