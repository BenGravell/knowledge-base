On the Convergence and Sample Efficiency of Variance-Reduced Policy Gradient Method

Policy gradient (PG) gives rise to a rich class of reinforcement learning (RL) methods. Recently, there has been an emerging trend to accelerate the existing PG methods such as REINFORCE by the variance reduction techniques. However, all existing variance-reduced PG methods heavily rely on an uncheckable importance weight assumption made for every single iteration of the algorithms. In this paper, a simple gradient truncation mechanism is proposed to address this issue. Moreover, we design a Truncated Stochastic Incremental Variance-Reduced Policy Gradient (TSIVR-PG) method, which is able to maximize not only a cumulative sum of rewards but also a general utility function over a policy's long-term visiting distribution. We show an tildeO(epsilon^(-3)) sample complexity for TSIVR-PG to find an epsilon-stationary policy. By assuming the overparameterizaiton of policy and exploiting the hidden convexity of the problem, we further show that TSIVR-PG converges to global epsilon-optimal policy with tildeO(epsilon^(-2)) samples.

## Introduction

In this paper, we investigate the theoretical properties of Policy Gradient (PG) methods for Reinforcement Learning (RL). In view of RL as a policy optimization problem, the PG method parameterizes the policy function and conduct gradient ascent search to improve the policy. In this paper, we consider the soft-max policy parameterization

where $(s,a)$ is a state-action pair and $\psi$ is some smooth function. Potentially, one can set the function $\psi$ to be some deep neural network with weights $\theta$ and input $(s,a)$. The main problem considered in this paper is the policy optimization for a *general utility* function:

where $\sigma$ is a fixed small constant. We choose $\sigma = 0.125$ in our experiment. The orders of $N,B,m$ are set in the same way as those in section 6.1. For the MaxEnt algorithm, note that in the original paper, the nonlinear objective function assumes the input value is the stationary state distribution $d^{\pi}$, but the input value can easily be changed into our $\lambda$ without changing the steps of the algorithm much. The result is illustrated in Fig. 2. From the result, we may see that our algorithm consistently outperforms the benchmark.

Figure 2: Left: Empirical Evaluation of the Convergence Rate of TSIVR-PG. The optimality gap achieved by TSIVR-PG decreases as the sample size increases, nearly matching the ϵ−2 sample complexity theory (orange line). Right: Performance Curve ofTSIVR-PG and MaxEnt for Maximizing Non-linear Objective Functions. The curve is the median return over 10 runs and the shaded areas are calculated as the $\frac{1}{4}$ and $\frac{3}{4}$ quantiles of the experiment outcomes.

where $\parallel \cdot \parallel$ stands for $L_{2}$ norm and spectral norm for vector and matrix respectively.

Therefore, we can estimate the policy gradient using the typical REINFORCE as long as we pick the "quasi-reward function" as $r:={{\nabla_{\lambda}F}{({\lambda{(\theta)}})}}$. To find this quasi-reward, we need to estimate the state-action occupancy measure $\lambda{(\theta)}$ (unless $F$ is linear).

### Lemma 5.8

where $F$ is a general smooth function, and $\lambda^{\pi_{\theta}}$ denotes the unnormalized state-action occupancy measure (also referred to as the visitation measure). For any policy $\pi$ and initial state distribution $\xi$,
