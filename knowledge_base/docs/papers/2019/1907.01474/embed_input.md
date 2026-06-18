Memory of Motion for Warm-starting Trajectory Optimization

Topics include Trajectory optimization, Motion planning, Robotics, Bayesian methods, Nearest neighbors, Regression, Optimization, Planning, Humanoid robot, Gaussian processes.

Trajectory optimization for motion planning requires good initial guesses to obtain good performance. In our proposed approach, we build a memory of motion based on a database of robot paths to provide good initial guesses. The memory of motion relies on function approximators and dimensionality reduction techniques to learn the mapping between the tasks and the robot paths. Three function approximators are compared: k-Nearest Neighbor, Gaussian Process Regression, and Bayesian Gaussian Mixture Regression. In addition, we show that the memory can be used as a metric to choose between several possible goals, and using an ensemble method to combine different function approximators results in a significantly improved warm-starting performance. We demonstrate the proposed approach with motion planning examples on the dual-arm robot PR2 and the humanoid robot Atlas.

## Introduction

Motion planning for robots with high Degree-of-Freedoms (DoFs) presents many challenges, especially in the presence of constraints such as obstacle avoidance, joint limits, etc. To handle the high-dimensionality and the various constraints, many works focus on *trajectory optimization* methods that attempt to find a locally optimal solution. In this approach, the motion planning problem is formulated as an optimization problem

Other constraints can also be added, e.g. to avoid collisions, to comply with joint limits, etc.

To overcome this problem, our approach builds a *memory of motion* that learns how to provide good initializations (i.e., a *warm-start*) to the solver based on previously solved problems. Functionally, the memory of motion is expected to learn the mapping ${\mathbf{f}}:{{\mathbf{x}}\rightarrow{\mathbf{y}}}$ that maps each task $\mathbf{x}$ to the robot path $\mathbf{y}$. Such mapping can be highly nonlinear and *multimodal* (i.e., one task $\mathbf{x}$ can be associated to several robot paths $\mathbf{y}$), and the dimension of $\mathbf{y}$ is typically very high.

The contribution of this paper is the following. First, we propose the use of function approximation methods to learn the mapping ${\mathbf{f}}{({\mathbf{x}})}$. We consider three methods: $k$-Nearest Neighbor ($k$-NN), Gaussian Process Regressor (GPR) and Bayesian Gaussian Mixture Regression (BGMR), and discuss their different characteristics on various planning problems. We show in particular that BGMR handles multimodal output very well. Furthermore, we show that the memory of motion can be also be used as a metric for choosing optimally between several possible goals.

## Conclusion

We have presented an approach to build a memory of motion to warm-start trajectory optimization solver, and demonstrate through experiments with PR2 and Atlas robots that the warm-start can improve the solver's performance. Function approximators and dimensionality reduction are used to learn the mapping between the task descriptor and the corresponding robot path. Three function approximators are considered: $k$-NN as baseline, GPR, and BGMR, and their different characteristics have been discussed. The use of PCA also improves the solution, although not very significantly, while reducing the memory storage.
