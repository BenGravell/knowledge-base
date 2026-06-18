Differentiable Integrated Motion Prediction and Planning with Learnable Cost Function for Autonomous Driving

Predicting the future states of surrounding traffic participants and planning a safe, smooth, and socially compliant trajectory accordingly is crucial for autonomous vehicles. There are two major issues with the current autonomous driving system: the prediction module is often separated from the planning module and the cost function for planning is hard to specify and tune. To tackle these issues, we propose a differentiable integrated prediction-planning framework (DIPP) that can also learn the cost function from data. Specifically, our framework uses a differentiable nonlinear optimizer as the motion planner, which takes as input the predicted trajectories of surrounding agents given by the neural network and optimizes the trajectory for the autonomous vehicle, enabling all operations to be differentiable, including the cost function weights. The proposed framework is trained on a large-scale real-world driving dataset to imitate human driving trajectories in the entire driving scene and validated in both open-loop and closed-loop manners....

## Introduction

Figure 1: Three different motion planning paradigms: (a) traditional sequential prediction and planning; (b) end-to-end method; (c) our proposed method.

Making safe, socially-compatible, and human-like decisions is a fundamental capability of autonomous vehicles (AVs). While learning-based end-to-end decision-making methods, such as imitation learning and reinforcement learning, have enjoyed vigorous growth recently, they still lack interpretability, robustness, and safety compared to classic planning-based methods. Nonetheless, to make safe and smooth plans in complex traffic scenarios, the key is to accurately forecast the future trajectories of surrounding traffic participants....

## Conclusions

We propose a novel differentiable integrated multi-agent interactive prediction and motion planning framework, which is trained end-to-end from real-world driving data. A Transformer-based predictor is established to predict joint future trajectories of surrounding agents and provide an initial guess for the planner. The predicted trajectories, initial plan, and learnable cost function are channeled to an optimization-based differentiable motion planner, allowing every component in the framework to be differentiable. The framework is validated on a large-scale urban driving dataset in both open-loop and closed-loop testing....

## Experiments

In addition, obeying traffic lights should be treated as a hard constraint for the AV. Here, we replace the hard constraint with a soft penalty term, which can be assigned with a large cost weight. We assume the AV runs along a predefined route and its running distance is $s_{t}$, which is derived from $s_{t} = {\sum_{t^{\prime} = 1}^{t}{v_{t^{\prime}}\Deltat}}$, and the stop line position (if encountering a red light) on the route is $s_{stop}$. We can formulate the cost of violating traffic lights using the hinge loss:

### IV-D2 Training

In this paper, we propose a novel framework called differentiable integrated prediction and planning (DIPP), as shown in Fig. 1(c). The objective of the DIPP framework is to make the prediction module aware of the downstream planning task, so as to deliver planning-aware prediction results to the motion planner, without altering the established structure of the prediction-planning process....

In summary, the main contributions of this paper are listed as follows:
