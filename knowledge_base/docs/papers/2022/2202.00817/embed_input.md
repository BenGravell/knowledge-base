Do Differentiable Simulators Give Better Policy Gradients?

Topics include Policy gradients, Reinforcement learning, Robustness, Planning, Control, Learning.

Differentiable simulators promise faster computation time for reinforcement learning by replacing zeroth-order gradient estimates of a stochastic objective with an estimate based on first-order gradients. However, it is yet unclear what factors decide the performance of the two estimators on complex landscapes that involve long-horizon planning and control on physical systems, despite the crucial relevance of this question for the utility of differentiable simulators. We show that characteristics of certain physical systems, such as stiffness or discontinuities, may compromise the efficacy of the first-order estimator, and analyze this phenomenon through the lens of bias and variance. We additionally propose an alpha-order gradient estimator, with alpha in, which correctly utilizes exact gradients to combine the efficiency of first-order estimates with the robustness of zero-order methods. We demonstrate the pitfalls of traditional estimators and the advantages of the alpha-order estimator on some numerical examples.

## Introduction

Consider the problem of minimizing a *stochastic objective*,

At the heart of many algorithms for reinforcement learning (RL) lies *zeroth-order* estimation of the gradient $\nabla F$. Yet, in domains that deal with structured systems, such as linear control, physical simulation, or robotics, it is possible to obtain *exact* gradients of $f$, which can also be used to construct a *first-order* estimate of $\nabla F$. The availability of both options begs the question: given access to exact gradients of $f$, which estimator should we prefer?

Do differentiable simulators give better policy gradients? We have shown that the answer depends intricately on the underlying characteristics of the physical systems. While Lipschitz continuous systems with reasonably bounded gradients may enjoy fast convergence given by the low variance of first-order estimators, using the gradients of differentiable simulators may *hurt* for problems that involve nearly/strictly discontinuous landscapes, stiff dynamics, or chaotic systems....

These limitations of using differentiable simulators for planning and control need to be addressed from both the design of simulator and algorithms: from the simulator side, we have shown that certain modeling decisions such as stiffness of contact dynamics can have significant underlying consequences in the performance of policy optimization that uses gradients from these simulators. From the algorithm side, we have shown we can automate the procedure of deciding which one to use online via interpolation.

### Example 3.7

Under Assumption 2.1 and Assumption 2.2, the ZoBG is an unbiased estimator of the stochastic objective.

### A robust interpolation protocol

In stochastic optimization, the theoretical benefits of using first-order estimates of $\nabla F$ over zeroth-order ones have mainly been understood through the lens of variance and convergence rates: the first-order estimator often (*not always*) results in much less variance compared to the zeroth-order one, which leads to faster convergence rates to a local minima of general nonconvex smooth objective functions.

However, the landscape of RL objectives that involve long-horizon sequential decision making (e.g. policy optimization) is challenging to analyze, and convergence properties in these landscapes are relatively poorly understood, except for structured...
