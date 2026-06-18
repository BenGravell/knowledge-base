Learning Continuous Control Policies by Stochastic Value Gradients

We present a unified framework for learning continuous control policies using backpropagation. It supports stochastic control by treating stochasticity in the Bellman equation as a deterministic function of exogenous noise. The product is a spectrum of general policy gradient algorithms that range from model-free methods with value functions to model-based methods without value functions. We use learned models but only require observations from the environment in- stead of observations from model-predicted trajectories, minimizing the impact of compounded model errors. We apply these algorithms first to a toy stochastic control problem and then to several physics-based control problems in simulation. One of these variants, SVG, shows the effectiveness of learning models, value functions, and policies simultaneously in continuous domains.

## Introduction

Policy gradient algorithms maximize the expectation of cumulative reward by following the gradient of this expectation with respect to the policy parameters. Most existing algorithms estimate this gradient in a model-free manner by sampling returns from the real environment and rely on a likelihood ratio estimator. Such estimates tend to have high variance and require large numbers of samples or, conversely, low-dimensional policy parameterizations.

A second approach to estimate a policy gradient relies on backpropagation instead of likelihood ratio methods. If a differentiable environment model is available, one can link together the policy, model, and reward function to compute an analytic policy gradient by backpropagation of reward along a trajectory. Instead of using entire trajectories, one can estimate future rewards using a learned value function (a critic) and compute policy gradients from subsequences of trajectories. It is also possible to backpropagate analytic action derivatives from a Q-function to compute the policy gradient without a model....

## Discussion

We have shown that two potential problems with value gradient methods, their reliance on planning and restriction to deterministic models, can be exorcised, broadening their relevance to reinforcement learning. We have shown experimentally that the SVG framework can train neural network policies in a robust manner to solve interesting continuous control problems. The framework includes algorithm variants beyond the ones tested in this paper, for example, ones that combine a value function with $k$ steps of back-propagation through a model (SVG(k))....

SVG($\infty$) computes value gradients by backward recursions on finite-horizon trajectories. After every episode, we train the model, $\hat{\mathbf{f}}$, followed by the policy, $\pi$. We provide pseudocode for this in Algorithm 1 ‣ 4 Stochastic value gradients ‣ Learning Continuous Control Policies by Stochastic Value Gradients") but discuss further implementation details in section 5 and in the experiments.

We now re-parameterize the Bellman equation. When re-parameterized, the stochastic policy takes the form $\mathbf{a} = {\pi{(\mathbf{s},\eta;\theta)}}$, and the stochastic environment the form $\mathbf{s}^{\prime} = {\mathbf{f}{(\mathbf{s},\mathbf{a},\xi)}}$ for noise variables $\eta \sim {\rho{(\eta)}}$ and...
