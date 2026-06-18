Differentiable MPC for End-to-end Planning and Control

Topics include Reinforcement learning, Imitation learning, Model predictive control, Predictive control, System identification, Neural networks, Planning, Control, Learning, Differentiable model predictive control.

We present foundations for using Model Predictive Control (MPC) as a differentiable policy class for reinforcement learning in continuous state and action spaces. This provides one way of leveraging and combining the advantages of model-free and model-based approaches. Specifically, we differentiate through MPC by using the KKT conditions of the convex approximation at a fixed point of the controller. Using this strategy, we are able to learn the cost and dynamics of a controller via end-to-end learning. Our experiments focus on imitation learning in the pendulum and cartpole domains, where we learn the cost and dynamics terms of an MPC policy class. We show that our MPC policies are significantly more data-efficient than a generic neural network and that our method is superior to traditional system identification in a setting where the expert is unrealizable.

## Introduction

Model-free reinforcement learning has achieved state-of-the-art results in many challenging domains. However, these methods learn black-box control policies and typically suffer from poor sample complexity and generalization. Alternatively, model-based approaches seek to model the environment the agent is interacting in. Many model-based approaches utilize Model Predictive Control (MPC) to perform complex control tasks. MPC leverages a predictive model of the controlled system and solves an optimization problem online in a receding horizon fashion to produce a sequence of control actions....

Formally, MPC requires that at each time step we solve the optimization problem:

This paper lays the foundations for differentiating and learning MPC-based controllers within reinforcement learning and imitation learning. Our approach, in contrast to the more traditional strategy of "unrolling" a policy, has the benefit that it is much less computationally and memory intensive, with a backward pass that is essentially free given the number of iterations required for a the iLQR optimizer to converge to a fixed point. We have demonstrated our approach in the context of imitation learning, and have highlighted the potential advantages that the approach brings over generic imitation learning and system identification.

We also emphasize that one of the primary contributions of this paper is to define and set up the framework for differentiating through MPC in general. Given the recent prominence of attempting to incorporate planning and control methods into the loop of deep network architectures, the techniques here offer a method for efficiently integrating MPC policies into such situations, allowing these architectures to make use of a very powerful function class that has proven extremely effective in practice....

With some loss function $\ell$ that depends on $x^{\star}$, we can use the approach in Amos and Kolter to obtain the derivatives of $\ell$ with respect to $Q$, $p$, $A$, and $b$ as

where $C_{t,x}$, $c_{t,x}$, and $F_{t,x}$ are the first block-rows of $C_{t}$, $c_{t}$, and $F_{t}$, respectively. Now that we have the optimal trajectory and dual variables, we can compute the gradients of the loss with respect to the parameters....
