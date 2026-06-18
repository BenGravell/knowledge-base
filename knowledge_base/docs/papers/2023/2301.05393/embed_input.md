Interaction-Aware Trajectory Planning for Autonomous Vehicles with Analytic Integration of Neural Networks into Model Predictive Control

Topics include Autonomous driving, Interaction-aware planning, Model predictive control, Trajectory prediction, Neural networks.

Integrates a neural interaction predictor analytically inside an MPC formulation so the planner can reason about other agents responses while optimizing the ego trajectory. The contribution is less a new predictor than a planner architecture that keeps learned interaction models usable inside constrained optimization.

Autonomous vehicles (AVs) must share the driving space with other drivers and often employ conservative motion planning strategies to ensure safety. These conservative strategies can negatively impact AV's performance and significantly slow traffic throughput. Therefore, to avoid conservatism, we design an interaction-aware motion planner for the ego vehicle (AV) that interacts with surrounding vehicles to perform complex maneuvers in a locally optimal manner. Our planner uses a neural network-based interactive trajectory predictor and analytically integrates it with model predictive control (MPC). We solve the MPC optimization using the alternating direction method of multipliers (ADMM) and prove the algorithm's convergence. We provide an empirical study and compare our method with a baseline heuristic method.

## Introduction

Motion planning for autonomous vehicles (AVs) is a daunting task, where AVs must share the driving space with other drivers. Driving in shared spaces is inherently an interactive task, i.e., AV's actions affect other nearby vehicles and vice versa. This interaction is evident in dense traffic scenarios where all goal-directed behavior relies on the cooperation of other drivers to achieve the desired goal....

AVs can be overly defensive and opaque when interacting with other drivers, as they often rely on decoupled prediction and planning techniques. The prediction module anticipates the trajectories of other vehicles, and the planning module uses this information to find a collision-free path. As a result of this decoupling, AVs tend to be conservative and treat other vehicles as dynamic obstacles, resulting in a lack of cooperation. Figure 1 shows two scenarios in which the ego vehicle intends to merge into the left lane, but the inter-vehicle gaps are too narrow....

### Proof of Theorem 1

Since $C$ is a full rank matrix, ${Im{(C)}} = {\mathbb{R}}^{4T_{p}}$, and hence, $D \in {Im{(C)}}$. Recall that the feasible sets for $\mathbf{\Delta}$, $\mathbf{α}$, and $\mathbf{Z}$ are bounded, i.e., ${\mathbf{\Delta} \in \mathcal{D}},{{\mathbf{α}} \in \mathcal{A}}$, and ${\mathbf{Z}} \in \mathcal{Z}$. Using these results and Lemmas 1-3, the optimization problem satisfies all the assumptions required for convergence of ADMM in non-convex and non-smooth optimization. Utilizing \[29, Theorem 2\] proves the convergence of Algorithm 1 for any sufficiently large $\rho > {\max{\{ 1,{{({1 + {2\sigma_{\min}{(C)}}})}L_{J}M}\}}}$. $\blacksquare$

where $c_{\mathbf{Z}}^{(k)} = {{C{\mathbf{Z}}^{(k)}} - {F{(\mathbf{\Delta}^{({k + 1})},{\mathbf{α}}^{({k + 1})},{\mathbf{Z}}^{(k)})}}}$. Due to the nonconvexity of the neural network in $b_{i}{({\mathbf{Z}})}$, the objective function (16 ‣ III Solving MPC with ADMM ‣ Interaction-Aware Trajectory Planning for Autonomous Vehicles with Analytic Integration of Neural Networks into Model Predictive Control")) is non-convex. We prefer the Quasi-Newton method for optimization to avoid expensive Hessian computation at each step....

In the next section, we solve the optimization using ADMM to determine a safe and interactive ego vehicle's trajectory.

### Lemma 2
