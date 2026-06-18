Escaping High-order Saddles in Policy Optimization for Linear Quadratic Gaussian (LQG) Control

First order policy optimization has been widely used in reinforcement learning. It guarantees to find the optimal policy for the state-feedback linear quadratic regulator (LQR). However, the performance of policy optimization remains unclear for the linear quadratic Gaussian (LQG) control where the LQG cost has spurious suboptimal stationary points. In this paper, we introduce a novel perturbed policy gradient (PGD) method to escape a large class of bad stationary points (including high-order saddles). In particular, based on the specific structure of LQG, we introduce a novel reparameterization procedure which converts the iterate from a high-order saddle to a strict saddle, from which standard random perturbations in PGD can escape efficiently. We further characterize the high-order saddles that can be escaped by our algorithm.

## Introduction

In this paper, we revisit the linear quadratic Gaussian (LQG) control, one of the most fundamental problems in control theory, from a modern optimization view. In brief, we focus on a continuous-time linear time-invariant (LTI) system

where ${{x{(t)}} \in {\mathbb{R}}^{n}},{{{u{(t)}} \in {\mathbb{R}}^{m}},{{y{(t)}} \in {\mathbb{R}}^{p}}}$ are the state, control input, and measurement (output) vector at time $t$, respectively, and $w{(t)}$, $v{(t)}$ are white Gaussian noises with intensity matrices $W \succeq 0$ and $V \succ 0$, respectively. The goal is to design a controller (i.e., policy) based on partial measurements $y{(t)}$ to minimize a quadratic cost

## Conclusions

We have proposed a novel PGD algorithm (cf. Algorithm 1 Control")) to escape high-order saddles of LQG. Our PGD algorithm combines the inherent structure of LQG control with standard perturbation on gradients. We have shown the structure of all stationary points after model reduction (cf. Theorem 1 Control")). We have also introduced a reparameterization procedure with an intriguing transfer function $\mathbf{G}{(s)}$ at any stationary point (cf. Theorem 2 Control")). If ${\mathbf{G}{(s)}} ≢ 0$, we can certify that the high-order saddle can be made as a strict saddle by the reparameterization....

${3)}\Rightarrow 2)$: If $G{(s)}$ is not an identically zero function, then its zero set $\mathcal{Z}$ is a set of finite points. When choosing a stable and symmetric $\Lambda \in {\mathbb{S}}^{n - q}$ randomly, we have ${{eig}{({- \Lambda})}} \nsubseteq \mathcal{Z}$ holds with probability one. Thus, $\overset{\sim}{\mathsf{K}}$ is a strict saddle point with probability one.

As expected, a direct consequence of Lemma 2. ‣ III-A Classification of stationary points ‣ III Stationary Points and Their Hessians ‣ Escaping High-order Saddles in Policy Optimization for Linear Quadratic Gaussian (LQG) Control") is that a stationary point $\mathsf{K}$ of $J_{q}$ remains to be stationary over $\mathcal{C}_{q}$ after any similarity transformation. We can further derive a classification of the stationary points of $J_{n}$ over the set of full-order controllers $\mathcal{C}_{n}$.

The globally optimal controller from 6 Control") is given by

A special case is the linear quadratic regulator (LQR), where we have direct access to the state $x$ (i.e., ${{y{(t)}} = {x{(t)}}},{{{v{(t)}} =...
