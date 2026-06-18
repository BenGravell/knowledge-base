Information Theoretic Model Predictive Q-Learning

Topics include Reinforcement learning, Q-learning, Optimal control, Model predictive control, Predictive control, Robotics, Online algorithms, Optimization, Control, Learning.

Model-free Reinforcement Learning (RL) works well when experience can be collected cheaply and model-based RL is effective when system dynamics can be modeled accurately. However, both assumptions can be violated in real world problems such as robotics, where querying the system can be expensive and real-world dynamics can be difficult to model. In contrast to RL, Model Predictive Control (MPC) algorithms use a simulator to optimize a simple policy class online, constructing a closed-loop controller that can effectively contend with real-world dynamics. MPC performance is usually limited by factors such as model bias and the limited horizon of optimization. In this work, we present a novel theoretical connection between information theoretic MPC and entropy regularized RL and develop a Q-learning algorithm that can leverage biased models. We validate the proposed algorithm on sim-to-sim control tasks to demonstrate the improvements over optimal control and reinforcement learning from scratch. Our approach paves the way for deploying reinforcement learning algorithms on real systems in a systematic manner.

## Introduction

Deep reinforcement learning has generated great interest due to its success on a range of difficult problems including Computer Go and high-dimensional control tasks such as humanoid locomotion. While these methods are extremely general and can learn policies and value functions for complex tasks directly from raw data, they are also sample inefficient, and partially-optimized solutions can be arbitrarily poor, resulting in safety concerns when run on real systems.

One straightforward way to mitigate these issues is to learn a policy or value function entirely in a high-fidelity simulator and then deploy the optimized policy on the real system. However, this approach can fail due to model bias, external disturbances, the subtle differences between the real robot hardware and poorly modeled phenomena such as friction and contact dynamics. Sim-to-real transfer approaches based on domain randomization (DR) and model ensembles aim to make the policy robust by training it to be invariant to varying dynamics....

## Discussion

We presented a theoretical connection between information theoretic MPC and entropy-regularized RL that naturally provides an algorithm to leverage the benefits of both. While the approach is effective on a range of tasks, in the future we wish to investigate the dependence between model error and MPC horizon and adapt the horizon by reasoning about the quality of the Q function, both critical for real-world applications. \\acksThe authors would like to thank Nolan Wagener for insightful discussions for improving the manuscript.

We consider parameterized value functions $Q_{\theta}{(s,a)}$ where parameters $\theta$ are updated by stochastic gradient descent on the loss ${L(\theta)} = {\frac{1}{K}{\sum_{i = 1}^{K}\left( {y_{i} - {Q_{\theta}\left( s_{i},a_{i} \right)}} \right)^{2}}}$ for a batch of $K$ experience tuples $(s,a,c,s^{\prime})$ sampled from a replay buffer. Targets $y_{i}$ are calculated using the Bellman equation as

### Infinite Horizon MPPI Update Rule

FrankaDrawerOpen: based on a real-world manipulation problem from Chebotar et al. where the agent velocity controls a 7DOF Franka Panda arm to open a cabinet drawer. A biased distribution over damping and frictionloss of robot and drawer joints is provided. Every episode lasts 4s after which the arm configuration is randomized....
