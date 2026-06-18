CusADi: A GPU Parallelization Framework for Symbolic Expressions and Optimal Control

Topics include Reinforcement learning, Optimal control, Optimization, Control, Learning, CusADi, Compute unified device architecture.

The parallelism afforded by GPUs presents significant advantages in training controllers through reinforcement learning (RL). However, integrating model-based optimization into this process remains challenging due to the complexity of formulating and solving optimization problems across thousands of instances. In this work, we present CusADi, an extension of the CasADi symbolic framework to support the parallelization of arbitrary closed-form expressions on GPUs with CUDA. We also formulate a closed-form approximation for solving general optimal control problems, enabling large-scale parallelization and evaluation of MPC controllers. Our results show a ten-fold speedup relative to similar MPC implementation on the CPU, and we demonstrate the use of CusADi for various applications, including parallel simulation, parameter sweeps, and policy training.

## INTRODUCTION

Using GPUs for robotics is attractive due to their powerful computing and parallelization capabilities compared to CPUs. These advantages are particularly beneficial in training controllers through parallelized simulations and reinforcement learning (RL), evidenced by the success of learned policies in handling complex, high-dimensional tasks \[Miki2022_LearningLocomotion, Cheng2024_ExtremeParkourLegged, Zhuang2023_RobotParkour, Hoeller2020_DeepValueMPC\]....

Moreover, the barrier to creating model-based controllers has been substantially lowered. There exists an ecosystem of software tools that simplify developing, designing, and tuning controllers, such as OCS2, Crocoddyl, rockit, and casadi\[OCS2, Mastalli2020_crocoddyl, Gillis2020_rockit, Andersson2019_casadi\]. casadi's symbolic framework in particular greatly simplifies the process of formulating the costs, constraints, and dynamics of an optimal control problem (OCP).

As a tool, CusADi can be extended in several ways. Parallelism within individual expressions could also be exploited, especially for larger problems as studied in \[Plancher2019_DDPGPU\]. Results from graph theory could be used to identify parallelization opportunities from casadi expression graphs. However, this would have to be balanced against the overhead of starting and synchronizing additional threads.

For future work, the parallelization offered by CusADi opens up several promising directions. To improve the locomotion capabilities of the MIT Humanoid, we plan to learn a residual policy alongside the parallelized MPC with reinforcement learning \[Silver2018_ResidualPolicy\]. Another potential direction is to learn the value function for MPC with parallelized rollouts. The function could then be used to bootstrap value estimates in RL pipelines, similar to \[Grandesso2023_CACTO\], or as a terminal cost for more complex MPC controllers.

### III-B PyTorch Interface

After solving the KKT equations of the QP problem in to obtain step direction ${\delta\mathbf{v}_{k}} = {({\delta\mathbf{z}_{k}},{\delta{\mathbf{λ}}_{k}},{\delta{\mathbf{σ}}_{k}})}$, the solution is updated as $\mathbf{v}_{k + 1} = {\mathbf{v}_{k} + {\alpha\delta\mathbf{v}_{k}}}$, where $\alpha$ is a scalar that determines the acceptable step length via backtracking line search methods, such as the Armijo method \[Armijo1966_LineSearch\]....
