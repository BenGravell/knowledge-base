Brax: A Differentiable Physics Engine for Large Scale Rigid Body Simulation

We present Brax, an open source library for rigid body simulation with a focus on performance and parallelism on accelerators, written in JAX. We present results on a suite of tasks inspired by the existing reinforcement learning literature, but remade in our engine. Additionally, we provide reimplementations of PPO, SAC, ES, and direct policy optimization in JAX that compile alongside our environments, allowing the learning algorithm and the environment processing to occur on the same device, and to scale seamlessly on accelerators. Finally, we include notebooks that facilitate training of performant policies on common OpenAI Gym MuJoCo-like tasks in minutes.

## Abstract

We present Brax, an open source library for rigid body simulation with a focus on performance and parallelism on accelerators, written in JAX. We present results on a suite of tasks inspired by the existing reinforcement learning literature, but remade in our engine. Additionally, we provide reimplementations of PPO, SAC, ES, and direct policy optimization in JAX that compile alongside our environments, allowing the learning algorithm and the environment processing to occur on the same device, and to scale seamlessly on accelerators....

\begin{overpic}[width=433.62pt]{brax_initial_release.png} \end{overpic}
Figure 1: The suite of examples environments included in the initial release of Brax. From left to right: ant, fetch, grasp, halfcheetah, and humanoid.

Producing another version of what practitioners commonly use almost definitionally further complicates the landscape of existing benchmarks, but we hope that the development velocity unlocked by our library more than makes up for this extra friction. At the same time, the democratizing effect of releasing an engine that can solve control problems quickly can be double edged: the difference between a piece of democratizing technology and a weapon depends entirely on who is wielding it....

There remains a chance, however, that by releasing a significantly faster engine, we inadvertently dramatically increase the compute spent on reinforcement learning problems, in much the same way building a new highway in a city can counter-intuitively *increase* traffic. At least for our own energy expenditure, the experiments we performed were done in datacenters that are on track to be fully renewably sourced by 2030.

each accelerator core splits the batch into an appropriate number of mini batches for which gradient updates are computed, synced between all cores, and then applied synchronously

Table 1: Observation and action space data for the environments included in Brax.

compile a function that takes a gradient of the loss through a short trajectory

## Summary of Contributions

Brax trains locomotion and dexterous manipulation policies in seconds to minutes using just one modern accelerator. Brax achieves this by making extensive use of auto-vectorization, device-parallelism, just-in-time compilation, and auto-differentiation primitives of the JAX library....
