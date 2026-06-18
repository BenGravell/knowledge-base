High-Dimensional Continuous Control Using Generalized Advantage Estimation

Topics include Policy gradients, Reinforcement learning, Robotics, Neural networks, Online algorithms, Optimization, Control, Learning.

Policy gradient methods are an appealing approach in reinforcement learning because they directly optimize the cumulative reward and can straightforwardly be used with nonlinear function approximators such as neural networks. The two main challenges are the large number of samples typically required, and the difficulty of obtaining stable and steady improvement despite the nonstationarity of the incoming data. We address the first challenge by using value functions to substantially reduce the variance of policy gradient estimates at the cost of some bias, with an exponentially-weighted estimator of the advantage function that is analogous to TD(lambda). We address the second challenge by using trust region optimization procedure for both the policy and the value function, which are represented by neural networks. Our approach yields strong empirical results on highly challenging 3D locomotion tasks, learning running gaits for bipedal and quadrupedal simulated robots, and learning a policy for getting the biped to stand up from starting out lying on the ground.

## Introduction

The typical problem formulation in reinforcement learning is to maximize the expected total reward of a policy. A key source of difficulty is the long time delay between actions and their positive or negative effect on rewards; this issue is called the credit assignment problem in the reinforcement learning literature, and the distal reward problem in the behavioral literature. Value functions offer an elegant solution to the credit assignment problem---they allow us to estimate the goodness of an action before the delayed reward arrives.

We propose a family of policy gradient estimators that significantly reduce variance while maintaining a tolerable level of bias. We call this estimation scheme, parameterized by $\gamma \in {\lbrack 0,1\rbrack}$ and $\lambda \in {\lbrack 0,1\rbrack}$, the generalized advantage estimator (GAE). Related methods have been proposed in the context of online actor-critic methods. We provide a more general analysis, which is applicable in both the online and batch settings, and discuss an interpretation of our method as an instance of reward shaping, where the approximate value function is used to shape the reward.

We present experimental results on a number of highly challenging 3D locomotion tasks, where we show that our approach can learn complex gaits using high-dimensional, general purpose neural network function approximators for both the policy and the value function, each with over $10^{4}$ parameters. The policies perform torque-level control of simulated 3D robots with up to 33 state dimensions and 10 actuators.

We propose the use of a trust region optimization method for the value function, which we find is a robust and efficient way to train neural network value functions with thousands of parameters.

## Discussion

Policy gradient methods provide a way to reduce reinforcement learning to stochastic gradient descent, by providing unbiased gradient estimates. However, so far their success at solving difficult control problems has been limited, largely due to their high sample complexity. We have argued that the key to variance reduction is to obtain good estimates of the advantage function.
