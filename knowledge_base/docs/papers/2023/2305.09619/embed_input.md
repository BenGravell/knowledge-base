The Power of Learned Locally Linear Models for Nonlinear Policy Optimization

Topics include Reinforcement learning, Trajectory optimization, Nonlinear control, Linear models, iLQR, Data-driven control, Model-based.

Provides theoretical grounding for why locally linear models learned from data combined with model-based trajectory optimization (iLQR) can achieve sample efficiency for control of nonlinear systems with unknown dynamics.

A common pipeline in learning-based control is to iteratively estimate a model of system dynamics, and apply a trajectory optimization algorithm - e.g. iLQR - on the learned model to minimize a target cost. This paper conducts a rigorous analysis of a simplified variant of this strategy for general nonlinear systems. We analyze an algorithm which iterates between estimating local linear models of nonlinear system dynamics and performing iLQR-like policy updates. We demonstrate that this algorithm attains sample complexity polynomial in relevant problem parameters, and, by synthesizing locally stabilizing gains, overcomes exponential dependence in problem horizon. Experimental results validate the performance of our algorithm, and compare to natural deep-learning baselines.

### Introduction

Machine learning methods such as model-based reinforcement learning have lead to a number of breakthroughs in key applications across robotics and control. A popular technique in these domains is learning-based model-predictive control (MPC), wherein a model learned from data is used to repeatedly solve online planning problems to control the real system. It has long been understood that solving MPC *exactly*--both with perfectly accurate dynamics and minimization to globally optimality for each planning problem--enjoys numerous beneficial control-theoretic properties.

Unfortunately, the above situation is not reflective of practice. For one, most systems of practical interest are *nonlinear*, and therefore exact global recovery of system dynamics suffers from a curse of dimensionality. And second, the nonlinear dynamics render any natural trajectory planning problem nonconvex, making global optimality elusive. In this work, we focus on learning-based trajectory optimization, the "inner-loop" in MPC. We ask *when can we obtain rigorous guarantees about the solutions to nonlinear trajectory optimization under unknown dynamics?*

Figure 1: Cost suboptimality (𝒥Talg−𝒥T⋆)/𝒥T⋆ versus number of trajectories available to both Algorithm 1 and iLQR baselines. For visualization, the suboptimality is clipped to (10−4,∞).

Though we find that our method outperforms deep-learning baselines (excluding OPT+JacReg) on the simpler inverted pendulum environment, the learning+$\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ approaches fare better on the quadrotor. We suspect that this is attributable to data-reuse, as Algorithm 1 estimates an entirely new model of system dynamics at each iteration. We believe that finding a way to combine the advantages of directly estimating linearized dynamics (observed in Algorithm 1, as well as OPT+JacReg) with the advantages of data-reuse.

### Definition 4.2 (Open-Loop Linearized Dynamics)

### Definition 2.5 (Oracle Dynamics)

What we shall show is that our algorithm (a) finds a policy $\pi$ such that ${\|{{\nabla\mathcal{J}_{T}^{disc}}{(\pi)}}\|}_{\ell_{2}} \leq \epsilon$ is small, (b) by discretization, ${\|{{\nabla\mathcal{J}_{T}^{\pi}}{(\mathbf{u}^{\pi})}}\|}_{\mathcal{L}_{2}{(\mathcal{U})}} \leq {\epsilon + {\mathcal{O}(\tau)}}$ is small (i.e....
