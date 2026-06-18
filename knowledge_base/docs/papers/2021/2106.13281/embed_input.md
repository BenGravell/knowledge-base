Brax: A Differentiable Physics Engine for Large Scale Rigid Body Simulation

We present Brax, an open source library for rigid body simulation with a focus on performance and parallelism on accelerators, written in JAX. We present results on a suite of tasks inspired by the existing reinforcement learning literature, but remade in our engine. Additionally, we provide reimplementations of PPO, SAC, ES, and direct policy optimization in JAX that compile alongside our environments, allowing the learning algorithm and the environment processing to occur on the same device, and to scale seamlessly on accelerators. Finally, we include notebooks that facilitate training of performant policies on common OpenAI Gym MuJoCo-like tasks in minutes.

## Abstract

We present Brax, an open source library for rigid body simulation with a focus on performance and parallelism on accelerators, written in JAX. We present results on a suite of tasks inspired by the existing reinforcement learning literature, but remade in our engine. Additionally, we provide reimplementations of PPO, SAC, ES, and direct policy optimization in JAX that compile alongside our environments, allowing the learning algorithm and the environment processing to occur on the same device, and to scale seamlessly on accelerators.

\begin{overpic}[width=433.62pt]{brax_initial_release.png} \end{overpic}
Figure 1: The suite of examples environments included in the initial release of Brax. From left to right: ant, fetch, grasp, halfcheetah, and humanoid.

## Summary of Contributions

Brax trains locomotion and dexterous manipulation policies in seconds to minutes using just one modern accelerator. Brax achieves this by making extensive use of auto-vectorization, device-parallelism, just-in-time compilation, and auto-differentiation primitives of the JAX library. In doing so, it unlocks simulation of simple rigidbody physics systems in thousands of independent environments across hundreds of connected accelerators. For an individual accelerator, Brax reaches millions of simulation steps per second on environments like OpenAI Gym's MuJoCo Ant. See Sec. 6 for more details, or our Colab to train a policy interactively.

The structure of the paper is as follows: we first provide motivation for our engine in Sec. 2. In Sec. 3, we describe the architecture of Brax, starting from the low level physics primitives, how they interact, and how they can be extended for practitioners interested in physics based simulation. In Sec. 4, we review our ProtoBuf environment specification, and detail how it can be used to construct rich physically simulated tasks, including the suite of tasks bundled in this initial release. In Sec. 5, we tour some of the reinforcement learning algorithms bundled with Brax.

## Limitations and Future Work

In this section, we detail several important limitations and frailties of our engine.
