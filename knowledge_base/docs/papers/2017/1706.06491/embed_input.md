Data-Efficient Reinforcement Learning with Probabilistic Model Predictive Control

Topics include Reinforcement learning, Model predictive control, Predictive control, Robotics, Uncertainty, Gaussian processes, Neural networks, Probabilistic models, Planning, Control, Learning, Trial-and-error based reinforcement learning.

Trial-and-error based reinforcement learning (RL) has seen rapid advancements in recent times, especially with the advent of deep neural networks. However, the majority of autonomous RL algorithms require a large number of interactions with the environment. A large number of interactions may be impractical in many real-world applications, such as robotics, and many practical systems have to obey limitations in the form of state space or control constraints. To reduce the number of system interactions while simultaneously handling constraints, we propose a model-based RL framework based on probabilistic Model Predictive Control (MPC). In particular, we propose to learn a probabilistic transition model using Gaussian Processes (GPs) to incorporate model uncertainty into long-term predictions, thereby, reducing the impact of model errors. We then use MPC to find a control sequence that minimises the expected long-term cost. We provide theoretical guarantees for first-order optimality in the GP-based transition models with deterministic approximate inference for long-term planning....

## Introduction

Reinforcement learning (RL) is a principled mathematical framework for experience-based autonomous learning of control policies. Its trial-and-error learning process is one of the most distinguishing features of RL. Despite many recent advances in RL, a main limitation of current RL algorithms remains its data inefficiency, i.e., the required number of interactions with the environment is impractically high. For example, many RL approaches in problems with low-dimensional state spaces and fairly benign dynamics require thousands of trials to learn....

A promising way to increase the data efficiency of RL without inserting task-specific prior knowledge is to learn models of the underlying system dynamics. When a good model is available, it can be used as a faithful proxy for the real environment, i.e., good policies can be obtained from the model without additional interactions with the real system. However, modelling the underlying transition dynamics accurately is challenging and inevitably leads to model errors. To account for model errors, it has been proposed to use probabilistic models....

We proposed an algorithm for data-efficient RL that is based on probabilistic MPC with learned transition models using Gaussian processes. By exploiting Pontryagin's maximum principle our algorithm can naturally deal with state and control constraints. Key to this theoretical underpinning of a practical algorithm was the re-formulation of the optimal control problem with uncertainty propagation via moment matching into an deterministic optimal control problem. MPC allows the learned model to be updated immediately, which leads to an increased robustness with respect to model inaccuracies....

One of the most critical components of our approach is the incorporation of model uncertainty into modelling and planning. In complex environments, model uncertainty drives targeted exploration. It additionally allows us to account for constraints in a risk-averse way, which is important in the early stages of learning.

### Theorem 1

In this section, we provided an algorithmic framework for probabilistic MPC with learned GP models for the underlying system dynamics, where we explicitly use the GP's uncertainty for long-term predictions. In the following section, we will justify this using optimal control theory....
