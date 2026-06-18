Dual Approximation Policy Optimization

We propose Dual Approximation Policy Optimization (DAPO), a framework that incorporates general function approximation into policy mirror descent methods. In contrast to the popular approach of using the L_2-norm to measure function approximation errors, DAPO uses the dual Bregman divergence induced by the mirror map for policy projection. This duality framework has both theoretical and practical implications: not only does it achieve fast linear convergence with general function approximation, but it also includes several well-known practical methods as special cases, immediately providing strong convergence guarantees.

## Introduction

Policy gradient methods represent a paradigm shift in reinforcement learning from value-based methods (Watkins Puterman Bertsekas, ) to a more direct approach of policy optimization (Williams Sutton et al. Konda and Tsitsiklis, ). In particular, the natural policy gradient (NPG) method of Kakade inspired later development of trust region policy optimization (TRPO) and proximal policy optimization (PPO) Schulman et al., both with great empirical success.

These successes ignited considerable efforts to understand policy gradient methods from a theoretical perspective. Among them, Neu et al. first connected NPG with the mirror descent (MD) algorithm (Nemirovski and Yudin Beck and Teboulle, ), which led to a more general class of policy mirror descent (PMD) methods. Convergence guarantees for tabular PMD methods progressed from sublinear convergence to linear convergence (Xiao Lan Johnson et al., ). Then the linear convergence results were extended to PMD methods with linear function approximation, and more recently with general function approximation.

DAPO is a novel duality framework for incorporating general function approximation into policy mirror descent methods. Besides the mirror map in policy projection, it uses the dual mirror map for measuring the function approximation error. We establish linear and sublinear convergence rates of DAPO under different step size rules and show that it incorporates state-of-the-art algorithms like SAC as a special case, immediately providing them with strong convergence guarantees.

For future directions, DAPO paves the way for exploring new variants of PMD methods based on different mirror maps, e.g., with the negative Tsallis entropy. Another interesting question to investigate is how to characterize the effects of using inconsistent mirror maps in AMPO.

where $D_{KL}$ is given by ). There are several distinctions between DAPO-KL and DAPO-KL^∗^.

where $\pi^{(k)}$ means $\pi^{\theta^{(k)}}$, and $d_{\rho}^{(k)}$ and ${\hat{Q}}_{s,a}^{(k)}$ are simple notations for $d_{\rho}^{\pi^{(k)}}$ and ${\hat{Q}}_{s,a}^{\pi^{(k)}}$ respectively. This approach is adopted by, e.g., Tomar et al. and Vaswani et al.. However, the optimization problem is no longer convex in $\theta$, and its convergence analysis becomes more challenging.
