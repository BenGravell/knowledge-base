Learning Constraints from Demonstrations

Topics include Imitation learning, Learning from demonstrations, Constraints, Integer programming, Hit-and-run sampling, Safe planning.

Learns shared task constraints from safe demonstrations by synthesizing lower-cost unsafe trajectories and fitting a consistent unsafe set with an integer program. The work adds a safety-oriented inverse-learning angle: demonstrations reveal not only costs or policies but also hidden constraints that transfer across dynamics.

We extend the learning from demonstration paradigm by providing a method for learning unknown constraints shared across tasks, using demonstrations of the tasks, their cost functions, and knowledge of the system dynamics and control constraints. Given safe demonstrations, our method uses hit-and-run sampling to obtain lower cost, and thus unsafe, trajectories. Both safe and unsafe trajectories are used to obtain a consistent representation of the unsafe set via solving an integer program. Our method generalizes across system dynamics and learns a guaranteed subset of the constraint. We also provide theoretical analysis on what subset of the constraint can be learnable from safe demonstrations. We demonstrate our method on linear and nonlinear system dynamics, show that it can be modified to work with suboptimal demonstrations, and that it can also be used to learn constraints in a feature space.

## Introduction

Inverse optimal control and inverse reinforcement learning (IOC/IRL) have proven to be powerful tools in enabling robots to perform complex goal-directed tasks. These methods learn a cost function that replicates the behavior of an expert demonstrator when optimized. However, planning for many robotics and automation tasks also requires knowing constraints, which define what states or trajectories are safe....

While constraints are important, it can be impractical for a user to exhaustively program into a robot all the possible constraints it should obey when performing its repertoire of tasks. To avoid this, we consider in this paper the problem of recovering the latent constraints within expert demonstrations that are shared across tasks in the environment. Our method is based on the key insight that each safe, optimal demonstration induces a set of lower-cost trajectories that must be unsafe due to violation of an unknown constraint....

## Conclusion

In this paper we propose an algorithm that learns constraints from demonstrations, which acts as a complementary method to IOC/IRL algorithms. We analyze the properties of our algorithm as well as the theoretical limits of what subset of an unsafe set can be learned from safe demonstrations. The method works well on a variety of system dynamics and can be adapted to work with suboptimal demonstrations. We further show that our method can also learn constraints in a feature space....

After sampling, we can solve Problem 3.2. ‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations") to find an unsafe set consistent with the safe and unsafe trajectories. We now discuss the details of this process. Conservative estimate: One can obtain a conservative estimate of the unsafe set $\mathcal{A}$ from Problem 3.2....

We sample from $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$ to obtain lower-cost trajectories obeying the known constraints using hit-and-run sampling over the set $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$, a method guaranteeing convergence to a uniform distribution of samples over $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$ in the limit; the method is detailed in Algorithm 1 and an illustration is shown in Figure 2....
