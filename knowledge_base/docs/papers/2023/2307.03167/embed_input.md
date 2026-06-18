Risk-Averse Trajectory Optimization via Sample Average Approximation

Topics include Trajectory optimization, Robotics, Uncertainty, Online algorithms, Optimization, Planning.

Trajectory optimization under uncertainty underpins a wide range of applications in robotics. However, existing methods are limited in terms of reasoning about sources of epistemic and aleatoric uncertainty, space and time correlations, nonlinear dynamics, and non-convex constraints. In this work, we first introduce a continuous-time planning formulation with an average-value-at-risk constraint over the entire planning horizon. Then, we propose a sample-based approximation that unlocks an efficient and general-purpose algorithm for risk-averse trajectory optimization. We prove that the method is asymptotically optimal and derive finite-sample error bounds. Simulations demonstrate the high speed and reliability of the approach on problems with stochasticity in nonlinear dynamics, obstacle fields, interactions, and terrain parameters.

## Introduction

Accounting for uncertainty in the design of decision-making systems is key to achieving reliable robotics autonomy. Indeed, modern autonomy stacks account for uncertainty, whether it comes from noisy sensor measurements (e.g., due to perceptually-degraded conditions or a lack of features ), dynamics (e.g., due to disturbances and difficult-to-characterize nonlinearities ), properties of the environment (e.g., due to unknown terrain properties for legged robots and Mars rovers ), or interactions with other agents (e.g., in autonomous driving ).

Although trajectory optimization under uncertainty underpins a wide range of applications, existing approaches often make simplifying assumptions and approximations that reduce the range of problems they can reliably deal with. Specifically, there is a lack of methods capable of simultaneously handling

We proposed an efficient method for risk-averse trajectory optimization. This algorithm hinges on a continuous-time formulation with average-value-at-risk constraints. By approximating the problem using samples, we obtain a smooth, sparse program that allows for efficient numerical resolution. We demonstrated the speed and reliability of the method on problems with sources of epistemic and aleatoric uncertainty that are challenging to tackle with existing approaches.

Due to its generality in handling uncertain nonlinear dynamics and constraints, this work opens exciting future research directions. In particular, the approach could be interfaced with learned models: obstacles could be implicitly represented as deep SDFs or neural radiance fields, deep trajectory forecasting models could be used for planning in autonomous driving, learned terramechanics models could allow more robust legged locomotion, and dynamics could learned online, either to improve control performance or for active data-gathering under risk constraints.

Given $M \in {\mathbb{N}}$ samples and any constants $C > 0$ and $\epsilon \in {(0,\frac{1}{2})}$, define $\delta_{M} = {CM^{({\epsilon - \frac{1}{2}})}}$, and denote the sets of optimal solutions to OCP and $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$ by $S$ and $S_{M}{(\overline{\omega})}$, respectively....
