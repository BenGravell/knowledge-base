The Power of Learned Locally Linear Models for Nonlinear Policy Optimization

Topics include Reinforcement learning, Trajectory optimization, Nonlinear control, Linear models, iLQR, Data-driven control, Model-based.

Provides theoretical grounding for why locally linear models learned from data combined with model-based trajectory optimization (iLQR) can achieve sample efficiency for control of nonlinear systems with unknown dynamics.

A common pipeline in learning-based control is to iteratively estimate a model of system dynamics, and apply a trajectory optimization algorithm - e.g. iLQR - on the learned model to minimize a target cost. This paper conducts a rigorous analysis of a simplified variant of this strategy for general nonlinear systems. We analyze an algorithm which iterates between estimating local linear models of nonlinear system dynamics and performing iLQR-like policy updates. We demonstrate that this algorithm attains sample complexity polynomial in relevant problem parameters, and, by synthesizing locally stabilizing gains, overcomes exponential dependence in problem horizon. Experimental results validate the performance of our algorithm, and compare to natural deep-learning baselines.

## Introduction

Machine learning methods such as model-based reinforcement learning have lead to a number of breakthroughs in key applications across robotics and control. A popular technique in these domains is learning-based model-predictive control (MPC), wherein a model learned from data is used to repeatedly solve online planning problems to control the real system. It has long been understood that solving MPC *exactly*--both with perfectly accurate dynamics and minimization to globally optimality for each planning problem--enjoys numerous beneficial control-theoretic properties.

Contributions. We propose and analyze an alternative to the aforementioned approach of first learning a deep neural model of dynamics, and then performing AutoDiff to conduct the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ update. We consider a simplified setting with fixed initial starting condition.

For our analysis, we treat the underlying system dynamics as continuous and policy as discrete; this reflects real physical systems, is representative of discrete-time simulated environments which update on smaller timescales than learned policies, and renders explicit the effect of discretization size on sample complexity. We consider an interaction model where we query an oracle for trajectories corrupted with measurement (but not process) noise. Our approach enjoys the following theoretical properties.

## Discussion

We observe that Algorithm 1 with feedback-gains consistently outperforms Algorithm 1 without gains, validating the important of locally-stabilized dynamics. Second, we see that the performance of the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ baselines does not significantly improve as more trajectory data is collected. We find that our learned models achieve very low train and test error, over the sampling distribution (i.e., Opt or Rand) used for learning. For Rand, we postulate that the distribution shift incurred by performing RHC via trajectory optimization on the learned model limits the closed-loop performance of our baseline.
