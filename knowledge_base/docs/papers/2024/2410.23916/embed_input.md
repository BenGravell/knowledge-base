Transformer-based Model Predictive Control: Trajectory Optimization via Sequence Modeling

Topics include Convex optimization, Model predictive control, Predictive control, Trajectory optimization, Robotics, Neural networks, Transformers, Computational complexity, Optimization, Control, Learning.

Model predictive control (MPC) has established itself as the primary methodology for constrained control, enabling general-purpose robot autonomy in diverse real-world scenarios. However, for most problems of interest, MPC relies on the recursive solution of highly non-convex trajectory optimization problems, leading to high computational complexity and strong dependency on initialization. In this work, we present a unified framework to combine the main strengths of optimization-based and learning-based methods for MPC. Our approach entails embedding high-capacity, transformer-based neural network models within the optimization process for trajectory generation, whereby the transformer provides a near-optimal initial guess, or target plan, to a non-convex optimization problem. Our experiments, performed in simulation and the real world onboard a free flyer platform, demonstrate the capabilities of our framework to improve MPC convergence and runtime.

## Introduction

Trajectory generation is crucial to achieving reliable robot autonomy, endowing autonomous systems with the capability to compute a state and control trajectory that simultaneously satisfies constraints and optimizes mission objectives. As a result, trajectory generation problems have been formulated in many practical areas, including space and aerial vehicles, robot motion planning, chemical processes, and more.

Motivated by its widespread applications, a collection of highly effective solution strategies exist for the trajectory generation problem. For example, numerical optimization provides a systematic mathematical framework to specify mission objectives as costs or rewards and enforce state and control specifications via constraints. However, for most problems of interest, the trajectory optimization problem is almost always nonconvex, leading to high computational complexity, strong dependency on initialization, and a lack of guarantees of either obtaining a solution or certifying that a solution does not exist.

Beyond methods based on numerical optimization, recent advances in machine learning (ML) have motivated the application of learning-based methods to the trajectory generation problem. ML approaches are typically highly computationally efficient and can be optimized for (potentially nonconvex) performance metrics from high-dimensional data (e.g., images). However, learning-based methods are often sensitive to distribution shifts in unpredictable ways, whereas optimization-based approaches are more readily characterized both in terms of robustness and out-of-distribution behavior.

In this work, we propose a framework to exploit the specific strengths of optimization-based and learning-based methods for trajectory generation, specifically tailored for MPC formulations (Fig. 1).

We present a framework to combine the strengths of offline learning and online optimization for efficient trajectory generation within MPC formulations.

We investigate design and learning strategies within our framework, assessing the impact of fine-tuning on MPC execution and the benefits of learned terminal cost definitions to mitigate the inherent myopia in short-horizon MPC formulations.
