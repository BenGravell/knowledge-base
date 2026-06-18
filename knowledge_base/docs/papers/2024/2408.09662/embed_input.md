CusADi: A GPU Parallelization Framework for Symbolic Expressions and Optimal Control

Topics include Reinforcement learning, Optimal control, Optimization, Control, Learning, CusADi, Compute unified device architecture.

The parallelism afforded by GPUs presents significant advantages in training controllers through reinforcement learning (RL). However, integrating model-based optimization into this process remains challenging due to the complexity of formulating and solving optimization problems across thousands of instances. In this work, we present CusADi, an extension of the CasADi symbolic framework to support the parallelization of arbitrary closed-form expressions on GPUs with CUDA. We also formulate a closed-form approximation for solving general optimal control problems, enabling large-scale parallelization and evaluation of MPC controllers. Our results show a ten-fold speedup relative to similar MPC implementation on the CPU, and we demonstrate the use of CusADi for various applications, including parallel simulation, parameter sweeps, and policy training.

## INTRODUCTION

Using GPUs for robotics is attractive due to their powerful computing and parallelization capabilities compared to CPUs. These advantages are particularly beneficial in training controllers through parallelized simulations and reinforcement learning (RL), evidenced by the success of learned policies in handling complex, high-dimensional tasks \[Miki2022_LearningLocomotion, Cheng2024_ExtremeParkourLegged, Zhuang2023_RobotParkour, Hoeller2020_DeepValueMPC\].

In this work, we present CusADi, an extension of the casadi symbolic framework with CUDA for parallel evaluation on the GPU^11^1Repository and videos: CusADi code-generates and compiles symbolic functions from casadi, enabling parallel evaluation for any specified batch size. Algorithms and optimizations formulated symbolically for a single instance can then be evaluated simultaneously for thousands on the GPU. CusADi serves as a bridge for embedding model-based techniques and expressions from casadi into RL environments, offering speedups of up to 10-100x compared to parallel CPU evaluation, depending on data transfer overhead.

We show several examples highlighting robotics applications with CusADi. First, we formulate a closed-form approximation to the OCP that is amenable for parallelization and deploy MPC across thousands of environments in IsaacGym \[Makoviychuk2021_isaacgym\], as shown in Fig. 1, with training iterations roughly 11x faster than in \[Jenelten2024_DTC\]. Second, we demonstrate how dynamic quantities, such as the centroidal momentum or composite rigid-body inertia, can be symbolically expressed in casadi, computed in parallel with CusADi, and used to augment the observations and rewards in a training environment.

## Conclusion

In this work, we extend the symbolic framework of casadi so that arbitrary closed-form expressions can be parallelized on the GPU with CUDA and formulate a closed-form approximation to the OCP to evaluate MPC in parallel at a large-scale.

As a tool, CusADi can be extended in several ways. Parallelism within individual expressions could also be exploited, especially for larger problems as studied in \[Plancher2019_DDPGPU\]. Results from graph theory could be used to identify parallelization opportunities from casadi expression graphs. However, this would have to be balanced against the overhead of starting and synchronizing additional threads.
