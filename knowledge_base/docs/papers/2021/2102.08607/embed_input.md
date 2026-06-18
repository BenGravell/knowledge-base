On the Convergence and Sample Efficiency of Variance-Reduced Policy Gradient Method

Policy gradient (PG) gives rise to a rich class of reinforcement learning (RL) methods. Recently, there has been an emerging trend to accelerate the existing PG methods such as REINFORCE by the variance reduction techniques. However, all existing variance-reduced PG methods heavily rely on an uncheckable importance weight assumption made for every single iteration of the algorithms. In this paper, a simple gradient truncation mechanism is proposed to address this issue. Moreover, we design a Truncated Stochastic Incremental Variance-Reduced Policy Gradient (TSIVR-PG) method, which is able to maximize not only a cumulative sum of rewards but also a general utility function over a policy's long-term visiting distribution. We show an tildeO(epsilon^(-3)) sample complexity for TSIVR-PG to find an epsilon-stationary policy. By assuming the overparameterizaiton of policy and exploiting the hidden convexity of the problem, we further show that TSIVR-PG converges to global epsilon-optimal policy with tildeO(epsilon^(-2)) samples.

## Introduction

In this paper, we investigate the theoretical properties of Policy Gradient (PG) methods for Reinforcement Learning (RL). In view of RL as a policy optimization problem, the PG method parameterizes the policy function and conduct gradient ascent search to improve the policy. In this paper, we consider the soft-max policy parameterization

where $(s,a)$ is a state-action pair and $\psi$ is some smooth function. Potentially, one can set the function $\psi$ to be some deep neural network with weights $\theta$ and input $(s,a)$.

where $F$ is a general smooth function, and $\lambda^{\pi_{\theta}}$ denotes the unnormalized state-action occupancy measure (also referred to as the visitation measure). For any policy $\pi$ and initial state distribution $\xi$,

When $F$ is linear, the problem reduces to the standard policy optimization problem where the objective is to maximize a cumulative sum of rewards. When $F$ is nonlinear, problem goes beyond standard Markov decision problems: examples include the max-entropy exploration, risk-sensitive RL, certain set constrained RL, and so .

In this paper, we aim to investigate the convergence and sample efficiency of the PG method, using episodic sampling, for both linear $F$ (i.e., cumulative rewards) and nonlinear $F$ (i.e., general utility).

We propose the TSIVR-PG algorithm to solve problem via episodic sampling. It provides a conceptually simple stochastic gradient approach for solving general utility RL.

We show that TSIVR-PG finds an $\epsilon$-stationary policy using $\overset{\sim}{O}{(\epsilon^{- 3})}$ samples if $F$ and $\psi$ are general smooth functions. When $F$ is concave and $\psi$ satisfies certain overparameterization condition, we show that TSIVR-PG obtains a gloal $\epsilon$-optimal policy using $\overset{\sim}{O}{(\epsilon^{- 2})}$ samples.
