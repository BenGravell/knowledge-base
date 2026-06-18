Differentiable MPC for End-to-end Planning and Control

Topics include Reinforcement learning, Imitation learning, Model predictive control, Predictive control, System identification, Neural networks, Planning, Control, Learning, Differentiable model predictive control.

We present foundations for using Model Predictive Control (MPC) as a differentiable policy class for reinforcement learning in continuous state and action spaces. This provides one way of leveraging and combining the advantages of model-free and model-based approaches. Specifically, we differentiate through MPC by using the KKT conditions of the convex approximation at a fixed point of the controller. Using this strategy, we are able to learn the cost and dynamics of a controller via end-to-end learning. Our experiments focus on imitation learning in the pendulum and cartpole domains, where we learn the cost and dynamics terms of an MPC policy class. We show that our MPC policies are significantly more data-efficient than a generic neural network and that our method is superior to traditional system identification in a setting where the expert is unrealizable.

## Introduction

Model-free reinforcement learning has achieved state-of-the-art results in many challenging domains. However, these methods learn black-box control policies and typically suffer from poor sample complexity and generalization. Alternatively, model-based approaches seek to model the environment the agent is interacting . Many model-based approaches utilize Model Predictive Control (MPC) to perform complex control tasks. MPC leverages a predictive model of the controlled system and solves an optimization problem online in a receding horizon fashion to produce a sequence of control actions.

Formally,

In this paper, we consider the task of learning MPC-based policies in an end-to-end fashion, illustrated in fig. 1. That is, we treat MPC as a generic policy class $u = {\pi{(x_{init};C,f)}}$ parameterized by some representations of the cost $C$ and dynamics model $f$. By differentiating *through* the optimization problem, we can learn the costs and dynamics model to perform a desired task.

Still, efficiently differentiating through a complex policy class like MPC is challenging. Previous work with similar aims has either simply unrolled and differentiated through a simple optimization procedure or has considered generic optimization solvers that do not scale to the size of MPC problems. This paper makes the following two contributions to this space.

## Conclusion

This paper lays the foundations for differentiating and learning MPC-based controllers within reinforcement learning and imitation learning. Our approach, in contrast to the more traditional strategy of "unrolling" a policy, has the benefit that it is much less computationally and memory intensive, with a backward pass that is essentially free given the number of iterations required for a the iLQR optimizer to converge to a fixed point. We have demonstrated our approach in the context of imitation learning, and have highlighted the potential advantages that the approach brings over generic imitation learning and system identification.
