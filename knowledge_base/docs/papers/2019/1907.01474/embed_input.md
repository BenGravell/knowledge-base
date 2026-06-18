Memory of Motion for Warm-starting Trajectory Optimization

Topics include Trajectory optimization, Motion planning, Robotics, Bayesian methods, Nearest neighbors, Regression, Optimization, Planning, Humanoid robot, Gaussian processes.

Trajectory optimization for motion planning requires good initial guesses to obtain good performance. In our proposed approach, we build a memory of motion based on a database of robot paths to provide good initial guesses. The memory of motion relies on function approximators and dimensionality reduction techniques to learn the mapping between the tasks and the robot paths. Three function approximators are compared: k-Nearest Neighbor, Gaussian Process Regression, and Bayesian Gaussian Mixture Regression. In addition, we show that the memory can be used as a metric to choose between several possible goals, and using an ensemble method to combine different function approximators results in a significantly improved warm-starting performance. We demonstrate the proposed approach with motion planning examples on the dual-arm robot PR2 and the humanoid robot Atlas.

## Introduction

Motion planning for robots with high Degree-of-Freedoms (DoFs) presents many challenges, especially in the presence of constraints such as obstacle avoidance, joint limits, etc. To handle the high-dimensionality and the various constraints, many works focus on *trajectory optimization* methods that attempt to find a locally optimal solution. In this approach, the motion planning problem is formulated as an optimization problem

As an example, consider the planning problem depicted in Fig. 1, where the PR2 robot has to move its base around an object or to perform a dual-arm motion to pick items from the shelves. If the task ${\mathbf{x}} = {({\mathbf{q}}_{\text{init}}^{\top},{\mathbf{q}}_{\text{goal}}^{\top})}^{\top}$ is to move from an initial configuration ${\mathbf{q}}_{\text{init}}$ to a goal configuration ${\mathbf{q}}_{\text{goal}}$ while minimizing the total joint velocity, the optimization problem can be written as

## Conclusion

We have presented an approach to build a memory of motion to warm-start trajectory optimization solver, and demonstrate through experiments with PR2 and Atlas robots that the warm-start can improve the solver's performance. Function approximators and dimensionality reduction are used to learn the mapping between the task descriptor and the corresponding robot path. Three function approximators are considered: $k$-NN as baseline, GPR, and BGMR, and their different characteristics have been discussed. The use of PCA also improves the solution, although not very significantly, while reducing the memory storage....

## Experiments

where $\pi_{k}$, ${\mathbf{μ}}_{k}$, and $\mathbf{\Sigma}_{k}$ are the $k$-th component's mixing coefficient, mean, and covariance, respectively. Given a query ${\mathbf{x}}^{\ast}$, the conditional probability of the output ${\mathbf{y}}^{\ast}$ is also a mixture of Gaussians.

### IV-B Planning from a fixed initial configuration to a random goal configuration

Other constraints can also be added, e.g. to avoid collisions, to comply with joint limits, etc.

Such optimization problems are in general non-convex, especially due to the collision constraints, which makes finding the global optimum very difficult. Trajectory optimization methods such as TrajOpt, CHOMP, or STOMP solve the non-convex problem by iteratively optimizing around the current solution....
