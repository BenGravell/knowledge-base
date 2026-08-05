<!-- arxiv-full-text:v1 {"arxiv_id": "2301.05393", "source": "ar5iv"} -->

## Introduction

Motion planning for autonomous vehicles (AVs) is a daunting task, where AVs must share the driving space with other drivers. Driving in shared spaces is inherently an interactive task, i.e., AV's actions affect other nearby vehicles and vice versa. This interaction is evident in dense traffic scenarios where all goal-directed behavior relies on the cooperation of other drivers to achieve the desired goal. To predict the nearby vehicles' trajectories, AVs often rely on simple predictive models such as assuming constant speed for other vehicles, treating them as bounded disturbances, or approximating their trajectories using a set of known trajectories. These models do not capture the inter-vehicle interactions in their predictions. As a result, AVs equipped with such models struggle under challenging scenarios that require interaction with other vehicles.

AVs can be overly defensive and opaque when interacting with other drivers, as they often rely on decoupled prediction and planning techniques. The prediction module anticipates the trajectories of other vehicles, and the planning module uses this information to find a collision-free path. As a result of this decoupling, AVs tend to be conservative and treat other vehicles as dynamic obstacles, resulting in a lack of cooperation. Figure 1 shows two scenarios in which the ego vehicle intends to merge into the left lane, but the inter-vehicle gaps are too narrow. In such scenarios, conservative AVs with decoupled prediction and planning are forced to wait for a long duration. In contrast, we propose an interaction-aware AV that can open up a gap for itself by negotiating with other agents, i.e., by nudging them to either switch lanes (Fig. 1(a)) or change speeds (Fig. 1(b)).

Figure 1: Dense traffic scenarios where the ego vehicle (green) intends to merge to the left lane. The red and green trajectories show the nominal (conservative) and interaction-aware trajectories for the ego vehicles, respectively, and correspondingly, their impact on the other vehicles. Due to interaction with the ego vehicle (green trajectory), in scenario (a), the blue vehicle switches lanes, and in scenario (b), the blue vehicle slows down to create space for the ego vehicle to perform a safe lane-change maneuver.

Reinforcement learning (RL) techniques have been used to learn control policies under interactive or unknown environments. For example, adversarial RL is designed to reach the desired goal under uncertain conditions, and a model-free RL agent is developed for lane-changing control in dense traffic environments. However, these RL methods are not yet appropriate for safety-critical AVs due to their low interpretability and reliability.

Designing interaction-aware planners presents a significant challenge, as predicting the reactions of surrounding vehicles to the ego vehicle's actions is complex and non-trivial. Data-driven approaches, such as those using recurrent neural network architectures, have been effective in capturing the complex interactive behaviors of agents, especially in predicting driver behavior with high accuracy and computational efficiency. Therefore, it is desirable to utilize these data-driven methods to predict other vehicles' interactive behavior while maintaining safety through rigorous control theory and established vehicle dynamics models.

We propose a model predictive control (MPC) based motion planner that incorporates AV's decision and surrounding vehicles' interactive behaviors into safety constraints to perform complex maneuvers. In particular, we provide a mathematical formulation for integrating the neural network's predictions in the MPC controller and provide methods to obtain an (locally) optimal solution. However, the neural network integration and non-linear system dynamics make the optimization highly non-convex and challenging to solve analytically. Thus, prior efforts that integrate neural network prediction into MPC are numerical in nature and rely on heuristic algorithms to generate a finite set of trajectory candidates. In and, the authors generate these candidates by random sampling of control trajectories, and by generating spiral curves from source to target lane, respectively. In, the authors utilize a predefined set of reference trajectory candidates. Instead of solving the optimization, these approaches evaluate the cost of each candidate and choose the minimum cost trajectory that satisfies the safety constraint. Optimality is therefore restricted to trajectory candidates only, and the planner's performance depends on the heuristic algorithm design. In contrast to these prior efforts, we avoid heuristics, detail a proper formalization, and solve the optimization with provable optimality. The optimal solution provides key insights to design better planners and can be leveraged to compare trajectories obtained by other heuristic methods.

The major contributions of this work are twofold: (i) we reformulate a highly complex MPC problem with a non-convex neural network and non-linear system dynamics, and systematically solve it using the Alternating Direction Method of Multiplier (ADMM) with generic assumptions (Section III), and (ii) we investigate the mathematical properties of the ADMM algorithm for solving the MPC with an integrated neural network. Specifically, we provide sufficient conditions on the neural network such that the ADMM algorithm in non-convex optimization converges to a local optimum (Section IV). It is one of the first attempts in the literature toward provable mathematical guarantees for a neural network-integrated MPC.

## Problem Formulation and Controller Design

We design an MPC controller that leverages interactive behaviors of surrounding $N \in {\mathbb{N}}$ vehicles conditioned on the ego vehicle's future actions. The key to leverage interactions is to integrate a neural network and interactively update controls with step-size ${\Deltat} \in {\mathbb{R}}_{> 0}$ based on its inference (i.e., predicted positions during updates). This section further details the mathematical formulation of the MPC with the neural network.

Motivated , we use bicycle kinematics. The corresponding states are $\lbrack$xy-coordinates, heading angle, speed$\rbrack$ denoted by ${z{(\tau)}} = {\lbrack{x{(\tau)}},{y{(\tau)}},{\psi{(\tau)}},{v{(\tau)}}\rbrack}^{\top}$ for all $\tau \in {\{ 0,\ldots,T_{p}\}}$ and the control inputs are $\lbrack$acceleration, steering angle$\rbrack$ denoted by $\lbrack{a{(\tau)}},{\delta{(\tau)}}\rbrack$ for all $\tau \in {\{ 0,\ldots,{T_{p} - 1}\}}$ with the planning horizon $T_{p} \in {\mathbb{N}}$. For brevity, let $g{(\tau)}$ denote any general function $g{( \cdot )}$ at discrete time-step $\tau \in {\mathbb{Z}}_{\geq 0}$ with respect to (w.r.t) time $t$, i.e. ${g{(\tau)}} \equiv {g{({t + {\tau\Deltat}})}}$.

Then, at any time $t$, we solve the MPC to obtain the optimal control trajectories ${\mathbf{\Delta}^{\ast}{(t)}} \in \mathcal{D} \subset {\mathbb{R}}^{T_{p}}$ and ${{\mathbf{α}}^{\ast}{(t)}} \in \mathcal{A} \subset {\mathbb{R}}^{T_{p}}$, and corresponding optimal state trajectory ${{\mathbf{Z}}^{\ast}{(t)}} \in \mathcal{Z} \subset {\mathbb{R}}^{4T_{p}}$, where:

### II-A Objective function

The controller's objective is to move from the current lane to the desired lane as soon as possible while minimizing control effort and ensuring safety and smoothness. Let $x^{\text{ref}}$ denote the maximum longitude coordinate until when the ego must transition to the target lane. Let $\parallel \cdot \parallel$ denote the Euclidean norm. For $x < x^{\text{ref}}$, we utilize the following objective (cost) function $J{({\mathbf{\Delta}{(t)}},{{\mathbf{α}}{(t)}},{{\mathbf{Z}}{(t)}})}$ similar to: where ${\mathbf{\Delta}{(t)}} \in \mathcal{D}$, ${{\mathbf{α}}{(t)}} \in \mathcal{A}$, and ${{\mathbf{Z}}{(t)}} \in \mathcal{Z}$ are the planned steering, acceleration, and state trajectories, respectively. $y^{\text{ref}} \in {\mathbb{R}}$ and $v^{\text{ref}} \in {\mathbb{R}}_{> 0}$ are the reference latitude coordinate of the desired lane and desired velocity, respectively, provided by a high-level planner. For a detailed description of each term, we refer the interested readers to.

### II-B State Dynamics

Let $\overset{\sim}{\delta},\overset{\sim}{a}$ and $\overset{\sim}{z}$ be the last observed steering input, acceleration input and state of the ego vehicle, respectively. At any time $t$, we linearly approximate the discrete-time kinematic bicycle model of the form ${z{({\tau + 1})}} = {f{({\delta{(\tau)}},{a{(\tau)}},{z{(\tau)}})}}$ about $(\overset{\sim}{\delta},\overset{\sim}{a},\overset{\sim}{z})$ to obtain the equality constraints for the optimization problem. We have where ${\overset{\sim}{A} \in {\mathbb{R}}^{4}},{{\overset{\sim}{B} \in {\mathbb{R}}^{4}},{\overset{\sim}{C} \in {\mathbb{R}}^{4 \times 4}}}$, and $\overset{\sim}{D} \in {\mathbb{R}}^{4}$ are constant matrices given by $\overset{\sim}{A}:=\left. \frac{\partial f}{\partial\delta} \right|_{(\overset{\sim}{\delta},\overset{\sim}{a},\overset{\sim}{z})}$, $\overset{\sim}{B}:=\left. \frac{\partial f}{\partial a} \right|_{(\overset{\sim}{\delta},\overset{\sim}{a},\overset{\sim}{z})}$, $\overset{\sim}{C} = \left. \frac{\partial f}{\partial z} \right|_{(\overset{\sim}{\delta},\overset{\sim}{a},\overset{\sim}{z})}$, and $\overset{\sim}{D}:={{f{(\overset{\sim}{\delta},\overset{\sim}{a},\overset{\sim}{z})}} - {\overset{\sim}{A}\overset{\sim}{\delta}} - {\overset{\sim}{B}\overset{\sim}{a}} - {\overset{\sim}{C}\overset{\sim}{z}}}$, respectively. Hence, the linearized system dynamics is given: The equality constraints based on the system dynamics over the $T_{p}$ planning time-steps can be written as: where ${A \in {\mathbb{R}}^{{4T_{p}} \times T_{p}}},{{B \in {\mathbb{R}}^{{4T_{p}} \times T_{p}}},{C \in {\mathbb{R}}^{{{4T_{p}} \times 4}T_{p}}}}$, and $D \in {\mathbb{R}}^{4T_{p}}$ are constant matrices given: $\mathbf{0}$ and $\mathbf{I}$ denote the zero and identity matrix, respectively.

### Remark 1

To simplify the optimization, we linearly approximate the system dynamics before solving the MPC. This is possible because the control inputs obtained through the MPC are only applied for a single time-step, using a receding horizon control approach. As a result, any linearization errors from previous time-steps do not affect the MPC optimization.

### II-C Safety Constraints

The safety constraints for collision avoidance depend on the nearby vehicles' trajectory prediction and the vehicle shape model. Let $\mathcal{V}$ denote the set of nearby vehicles surrounding the ego vehicle. Let $\phi{(\tau)}$ be a trained neural network that jointly predicts the future trajectories of the ego vehicle and its surrounding vehicles for $T_{pred}$ time-steps into the future based on their trajectories for $T_{obs}$ time-steps in the past. $\phi{(\tau)}$ is given: with $T_{pred} = 1$, where the first column represents the positions of the ego vehicle followed by the positions of $N$ surrounding vehicles. Given the buffer of $T_{obs}$ past observations until time-step $\tau$, the coordinates of vehicle $i \in \mathcal{V}$ at time-step $\tau + 1$ are represented as: Some examples of the neural network $\phi{(\tau)}$ include social generative adversarial network (SGAN) and graph-based spatial-temporal convolutional network (GSTCN).

### Remark 2

Interactive predictions over planning horizon $T_{p}$ are computed recursively using $\phi{(t)}$ with $T_{pred} = 1$ based on the latest reactive predictions and ego vehicle positions from the MPC's candidate solution trajectory.

We model the vehicle shape using a single circle to obtain a smooth and continuously differentiable distance measure to enable gradient-based optimization methods. Let $(x,y)$ and $({\hat{x}}_{i},{\hat{y}}_{i})$ be the position of the ego vehicle and the predicted positions of the surrounding vehicles $i \in \mathcal{V}$ (obtained using $\phi{(\tau)}$), respectively. Let ${r,r_{i}} \in {\mathbb{R}}_{> 0}$ be the radius of circles modeling ego vehicle and vehicle $i$, respectively. The safety constraint for the ego vehicle w.r.t vehicle $i$ then reads: where $\epsilon \in {\mathbb{R}}_{> 0}$ is a safety bound.

### Remark 3

Using the single circle model, the safety constraints can be conservative, and consequently, the feasible solutions could be restrictive in some situations. We use it for its simplicity and to reduce the number of safety constraints. Some other alternatives for modeling the vehicle shape include the ellipsoid model and three circle model.

### II-D Formulation of the Optimization problem

We now present the complete optimization problem for the receding horizon control in a compact form: In the next section, we solve the optimization using ADMM to determine a safe and interactive ego vehicle's trajectory.

## Solving MPC with ADMM

There are many mathematical challenges associated with the MPC problem in Section II. Namely, it has the non-linear system dynamics, non-convex safety constraints, and dependence of the neural network predictions on its predictions in previous time steps ($T_{obs} \neq 1$). We now detail the systematic steps to solve the complex problem using ADMM, addressing the aforementioned mathematical challenges.

First, we construct a Lagrangian by moving the safety constraints, ${{b_{i}{({\mathbf{Z}})}} > 0},{i \in \mathcal{V}}$, in the optimization objective: where $\lambda_{s} \in {\mathbb{R}}_{> 0}^{T_{p}}$ is the vector of Lagrange multipliers.

### Remark 4

For theoretical analysis, we incorporate safety constraints into the optimization objective, but for our simulation study, we enforce them as hard constraints.

The optimization problem - is separable and the optimization variables $\mathbf{\Delta},{\mathbf{α}},{\mathbf{Z}}$ are decoupled in the objective function. Following the convention, the augmented Lagrangian is given: where $\rho > 0$ is the ADMM Lagrangian parameter and $\mu$ is the dual variable associated with the constraint. The complete algorithm is given by the Algorithm 1.

Init: states z = z0, controls δ = δ0, a = a0 Surrounding vehicles’ position: 2 Find the optimal control that minimizes the cumulative cost over horizon Tp Init: ${\hat{\mathbf{\Delta}} = \mathbf{\Delta}_{0}},{{\hat{\mathbf{α}} = {\mathbf{α}}_{0}},{{\hat{\mathbf{Z}} = {\mathbf{Z}}_{0}},{\hat{\mu} = \mu_{0}}}}$ 3 while convergence criterion is not met do 4 $\hat{\mathbf{\Delta}}\leftarrow{{{argmin}_{\mathbf{\Delta}}\mathcal{L}_{\rho}}{(\mathbf{\Delta},\hat{\mathbf{α}},\hat{\mathbf{Z}})}}$ 5 $\hat{\mathbf{α}}\leftarrow{{{argmin}_{\mathbf{α}}\mathcal{L}_{\rho}}{(\hat{\mathbf{\Delta}},{\mathbf{α}},\hat{\mathbf{Z}})}}$ 6 $\hat{\mathbf{Z}}\leftarrow{{{argmin}_{\mathbf{Z}}\mathcal{L}_{\rho}}{(\hat{\mathbf{\Delta}},\hat{\mathbf{α}},{\mathbf{Z}})}}$ 7 $\hat{\mu}\leftarrow{\hat{\mu} + {\rho{({F{(\hat{\mathbf{\Delta}},\hat{\mathbf{α}},\hat{\mathbf{Z}})}})}}}$ 11 Update the states through non-linear state dynamics with first elements of controls 12 $z\leftarrow{f{({\lbrack\hat{\mathbf{\Delta}}\rbrack}_{0},{\lbrack\hat{\mathbf{α}}\rbrack}_{0},z)}}$ 14 Observe positions of other vehicles at the current time t Algorithm 1 MPC with ADMM Next, we provide details for solving each of the local optimization problems at iteration $k$, for solving the MPC.

### III-A Update $\mathbf{\Delta}^{({k + 1})} = {{{argmin}_{\mathbf{\Delta} \in \mathcal{D}}\mathcal{L}_{\rho}}{(\mathbf{\Delta},{\mathbf{α}}^{(k)},\mathbf{Z}^{(k)})}}$

The sub-optimization problem for $\mathbf{\Delta}^{({k + 1})}$ is given by where $c_{\mathbf{\Delta}}^{(k)} = {{A\mathbf{\Delta}^{(k)}} - {F{(\mathbf{\Delta}^{(k)},{\mathbf{α}}^{(k)},{\mathbf{Z}}^{(k)})}}}$. It is a convex problem; hence, we can use a canonical convex optimization algorithm to find the optimal solution.

### III-B Update ${\mathbf{α}}^{({k + 1})} = {{{argmin}_{{\mathbf{α}} \in \mathcal{A}}\mathcal{L}_{\rho}}{(\mathbf{\Delta}^{({k + 1})},{\mathbf{α}},\mathbf{Z}^{(k)})}}$

The sub-optimization problem for ${\mathbf{α}}^{({k + 1})}$ is given by where $c_{\mathbf{α}}^{(k)} = {{B{\mathbf{α}}^{(k)}} - {F{(\mathbf{\Delta}^{({k + 1})},{\mathbf{α}}^{(k)},{\mathbf{Z}}^{(k)})}}}$. It is a convex problem; hence, we can use a canonical convex optimization algorithm to find the optimal solution.

### III-C Update $\mathbf{Z}^{({k + 1})} = {{{argmin}_{\mathbf{Z} \in \mathcal{Z}}\mathcal{L}_{\rho}}{(\mathbf{\Delta}^{({k + 1})},{\mathbf{α}}^{({k + 1})},\mathbf{Z})}}$

The sub-optimization problem for ${\mathbf{Z}}^{({k + 1})}$ is given by where $c_{\mathbf{Z}}^{(k)} = {{C{\mathbf{Z}}^{(k)}} - {F{(\mathbf{\Delta}^{({k + 1})},{\mathbf{α}}^{({k + 1})},{\mathbf{Z}}^{(k)})}}}$. Due to the nonconvexity of the neural network in $b_{i}{({\mathbf{Z}})}$, the objective function (16 ‣ III Solving MPC with ADMM ‣ Interaction-Aware Trajectory Planning for Autonomous Vehicles with Analytic Integration of Neural Networks into Model Predictive Control")) is non-convex. We prefer the Quasi-Newton method for optimization to avoid expensive Hessian computation at each step. Hence, we utilize BFGS-SQP method, which employs BFGS Hessian approximations within a sequential quadratic optimization, and does not assume any special structure in the objective or constraints. For a solver, we use PyGranso, a PyTorch-enabled port of GRANSO, that enables gradients computation by back-propagating the neural network's gradients at each iteration.

### Remark 5

The state trajectory $\mathbf{Z}$ update has a larger complexity in the problem due to the presence of the non-convex neural network predictions. To expedite the $\mathbf{Z}$ update, an offline-trained function approximator such as a neural network can be utilized to estimate the gradients of the original neural network. The training dataset for gradient approximator can be generated using automatic differentiation or central differences approximations with original network.

Henceforth, we refer to our method as ADMM-NNMPC.

## Convergence of MPC with ADMM

Due to the inherent non-convexity of the neural network, the rigorous convergence analysis of ADMM in is not readily applicable. Thus, we extend the convergence analysis of ADMM with an integrated neural network, i.e., the convergence of the inner while loop in Algorithm 1. We first make the following assumptions on the neural network: At any time-step $\tau \in {\lbrack 0,T_{p}\rbrack}$, the neural network's outputs are bounded, i.e. ${|{\phi_{i,x}{(\tau)}}|} \leq s_{x}$ and ${|{\phi_{i,y}{(\tau)}}|} \leq s_{y}$, $i \in \mathcal{V}$, where ${s_{x},s_{y}} \in {\mathbb{R}}_{> 0}$ are constants.

At any time-step $\tau \in {\lbrack 0,T_{p}\rbrack}$, the gradients of the neural network's outputs w.r.t the input ego trajectory exist and are bounded, i.e. ${\|\frac{\partial{\phi_{i,x}{(t)}}}{\partial{\mathbf{Z}}}\|}_{\infty} \leq \theta_{x}$ and ${\|\frac{\partial{\phi_{i,y}{(t)}}}{\partial{\mathbf{Z}}}\|}_{\infty} \leq \theta_{y}$ for all $i \in \mathcal{V}$, where ${\theta_{x},\theta_{y}} \in {\mathbb{R}}_{> 0}$ are constants and $\parallel \cdot \parallel_{\infty}$ is the max. norm of a vector.

At any time-step $\tau \in {\lbrack 0,T_{p}\rbrack}$, the neural network's outputs are Lipschitz differentiable, i.e. ${\|{{{\nabla\phi_{i,x}}{({\mathbf{Z}}_{1})}} - {{\nabla\phi_{i,x}}{({\mathbf{Z}}_{2})}}}\|} \leq {L_{\nabla\phi}{\|{{\mathbf{Z}}_{1} - {\mathbf{Z}}_{2}}\|}}$ and ${\|{{{\nabla\phi_{i,y}}{({\mathbf{Z}}_{1})}} - {{\nabla\phi_{i,y}}{({\mathbf{Z}}_{2})}}}\|} \leq {L_{\nabla\phi}{\|{{\mathbf{Z}}_{1} - {\mathbf{Z}}_{2}}\|}}$ for all $i \in \mathcal{V}$, ${{\mathbf{Z}}_{1},{\mathbf{Z}}_{2}} \in \mathcal{Z}$, where $L_{\nabla\phi} \in {\mathbb{R}}_{> 0}$ is the Lipschitz constant for the neural network's gradient.

Assumptions (A1)-(A3) are sufficient conditions under which the objective function is Lipschitz differentiable, i.e., it is differentiable and its gradient is Lipschitz continuous. This allows us to establish the convergence of Algorithm 1. Assumption (A1) is satisfied for a trained neural network for a bounded input space. Furthermore, neural network outputs can be clipped based on the feasible region. Lastly, neural networks with $C^{2}$ activation functions such as Gaussian Error Linear Unit (GELU) and Smooth Maximum Unit (SMU) satisfy assumptions (A2)-(A3).

### Remark 6

Assumptions (A1)-(A3) are sufficient conditions and not necessary conditions. If the neural network architecture is unknown or it doesn't satisfy the assumptions, knowledge distillation can be used to train a smaller (student) network that satisfies the assumptions from the large (teacher) pre-trained network.

### Theorem 1

\[Convergence of MPC with ADMM\] Under the assumptions (A1)--(A3), the inner while loop in Algorithm 1 converges subsequently for any sufficiently large $\rho > {\max{\{ 1,{{({1 + {2\sigma_{\min}{(C)}}})}L_{J}M}\}}}$, where $\sigma_{\min}{(C)}$ is the smallest positive singular value of $C$ in (II-B), $L_{J}$ is the Lipschitz constant for $J$ , and $M$ is the Lipschitz constant for sub-minimization paths as defined in Lemma 2. Therefore, starting from any $\mathbf{\Delta}^{},{\mathbf{α}}^{},\mathbf{Z}^{},\mu^{}$, it generates a sequence that is bounded, has at least one limit point, and that each limit point $\mathbf{\Delta}^{\ast},{\mathbf{α}}^{\ast},\mathbf{Z}^{\ast},\mu^{\ast}$ is a stationary point of $\mathcal{L}_{\rho}$ satisfying ${{\nabla\mathcal{L}_{\rho}}{(\mathbf{\Delta}^{\ast},{\mathbf{α}}^{\ast},\mathbf{Z}^{\ast},\mu^{\ast})}} = 0$.

We prove Theorem 1 using Lemmas 1-3.

### Lemma 1

\[Feasibility\] Let $Q:={\lbrack A,B\rbrack}$. Then $\text{Im}{(Q)}$ $\subseteq {\text{Im}{(C)}}$, where $\text{Im}{( \cdot )}$ returns the image of a matrix, and ${A,B},$ and $C$ is defined in (II-B).

### Proof

See Appendix -A for the proof. ∎

### Lemma 2

\[Lipschitz sub-minimization paths\] The following statements hold for the optimization problem: For any fixed ${\mathbf{α}},{\mathbf{Z}}$, $H_{1}:{{Im{(A)}}\rightarrow{\mathbb{R}}^{T_{p}}}$ defined by ${H_{1}{(u)}} \triangleq {{argmin}_{\mathbf{\Delta}}{\{{{J{(\mathbf{\Delta},{\mathbf{α}},{\mathbf{Z}})}}:{{A\mathbf{\Delta}} = u}}\}}}$ is unique and a Lipschitz continuous map.

For any fixed $\mathbf{\Delta},{\mathbf{Z}}$, $H_{2}:{{Im{(B)}}\rightarrow{\mathbb{R}}^{T_{p}}}$ defined by ${H_{2}{(u)}} \triangleq {{argmin}_{\mathbf{α}}{\{{{J{(\mathbf{\Delta},{\mathbf{α}},{\mathbf{Z}})}}:{{B{\mathbf{α}}} = u}}\}}}$ is unique and a Lipschitz continuous map.

For any fixed $\mathbf{\Delta},{\mathbf{α}}$, $H_{3}:{{Im{(C)}}\rightarrow{\mathbb{R}}^{4T_{p}}}$ defined by ${H_{3}{(u)}} \triangleq {{argmin}_{\mathbf{Z}}{\{{{J{(\mathbf{\Delta},{\mathbf{α}},{\mathbf{Z}})}}:{{C{\mathbf{Z}}} = u}}\}}}$ is unique and a Lipschitz continuous map, where ${A,B},$ and $C$ is defined in (II-B). Moreover, $H_{1},H_{2},H_{3}$ have a universal Lipschitz constant $M > 0$.

### Proof

See Appendix -B for the proof. ∎

### Lemma 3

\[Lipschitz Differentiability\] Under the assumptions (A1)-(A3), the objective function $J{(\mathbf{\Delta},{\mathbf{α}},\mathbf{Z})}$ in is Lipschitz differentiable.

### Proof

See Appendix -C for the proof. ∎ Proof of Theorem 1: See Appendix -D for the proof. $\blacksquare$ Figure 2: Two lane scenario: (a)-(d) shows the ADMM-NNMPC solution in a two-lane scenario after 0, 5, 7, and 13 time steps, respectively. The ego vehicle (red) opens a gap by nudging the vehicles to change their speeds.

Figure 3: Three lane scenario: (a)-(d) shows the ADMM-NNMPC solution in a three-lane scenario after 0, 3, 5, and 9 time steps, respectively. The ego vehicle (red) opens a gap for itself by nudging the vehicles to transition into the left-most lane.

Weight on divergence from target lane Weight on divergence from target speed Weight on steering angle Weight on steering rate ADMM Lagrangian parameter TABLE I: Objective function coefficients TABLE II: Simulation results for ADMM-NNMPC and NNMPC in the two-lane and three-lane scenario. tm e r g e are the number of time steps taken by the ego vehicle to merge into the target lane. Cmax and dmin are the maximum cost and minimum distance between the ego vehicle and other vehicles at any point of the simulation, respectively.

## Simulation Study

We now present the simulation results for ADMM-NNMPC. Figure 2 and 3 show the vehicles' positions at different time steps in two scenarios in which the ego vehicle (red) intends to merge into the left lane which is occupied by four other vehicles (blue) with a narrow inter-vehicle gap. In the two-lane scenario (Fig. 2), other vehicles can only change their speeds, while in the three-lane scenario (Fig. 3), other vehicles can also move laterally to transition into the leftmost lane. The other vehicles' positions at different time steps match the neural network's predictions, and hence, the ego vehicle's actions affect the trajectory of the other vehicles. In both scenarios, the ego vehicle is able to interact with the other agents and open a gap for itself to merge into.

Figure 4: (a) compares the trajectory (top) and cost (bottom) of the ADMM-NNMPC and NNMPC solutions in the two-lane (left) and three-lane (right) scenarios until xr e f = 25. (b) compares the steering (top) and acceleration (bottom) trajectories for ADMM-NNMPC and NNMPC solutions in the two-lane (left) and three-lane (right) scenarios.

We compare ADMM-NNMPC with a baseline method called NNMPC on the two-lane and three-lane scenarios by utilizing the same cost function (cost function coefficients listed in Table I) and $T_{p} = 8$ time steps. NNMPC generates trajectory candidates by computing a finite set of spiral curves from the source lane to the target lane and selects the candidate with minimum cost. In both methods, we use a trained SGAN neural network for interactive motion prediction of the other vehicles. Table II compares the simulation results for the baseline NNMPC and ADMM-NNMPC in the two-lane and three-lane scenarios. In the two-lane scenario, while the ADMM-NNMPC successfully merges in the left lane, the NNMPC method fails to make a lane change due to limited trajectory candidates. In the three-lane scenario, ADMM-NNMPC successfully switches lanes much faster than NNMPC. Furthermore, ADMM-NNMPC outperforms NNMPC in terms of maximum cost and minimum distance from other vehicles in both scenarios.

Figure 4(a) compares the trajectory (top) and cost (bottom) of the ADMM-NNMPC and NNMPC solutions in the two-lane (left) and three-lane (right) scenarios until $x_{ref} = 25$. In both scenarios, while ADMM-NNMPC successfully merges into the left lane, NNMPC fails to switch lanes before $x_{ref}$ due to limited trajectory candidates. Furthermore, the ADMM-NNMPC's cost is lower than the NNMPC solution at every time step since ADMM-NNMPC solves the optimization. Figure 4(b) compares the steering (top) and acceleration (bottom) trajectories for ADMM-NNMPC and NNMPC solutions in the two-lane (left) and three-lane (right) scenarios. Since ADMM-NNMPC solves for the optimal solution, it actively interacts with the other vehicles to open a gap for itself to merge into. Therefore, the steering trajectory in ADMM-NNMPC is more aggressive that the NNMPC. Lastly, the acceleration gradually changes in ADMM-NNMPC to reach the desired speed while minimizing jerk.

### V-A Limitations and Future Works

Although we reduce the problem complexity by decomposing it into smaller sub-problems, these sub-problems are still complex which makes the approach non-scalable. Furthermore, due to the large neural network size and re-computation of gradients at each iteration, our current implementation runs slower than real-time. Nevertheless, having a slow offline optimization is useful, as it can serve as a benchmark when developing faster heuristic methods, ideally, we would like to increase the efficiency. Our approach can be made faster by training another neural network to estimate the original neural network's gradients and developing faster optimization libraries. Thus, future works include: (i) designing a smaller network trained with knowledge distillation, or (ii) expediting neural network's gradient estimation using an offline-trained function approximator such as a neural network.

## Conclusions

With the importance of motion planning strategies being interaction-aware, e.g., lane changing in dense traffic for autonomous vehicles, this paper investigates mathematical solutions of a model predictive control with a neural network that estimates interactive behaviors. The problem is highly complex due to the non-convexity of the neural network, and we show that the problem can be effectively solved by decomposing it into sub-problems by leveraging the alternating direction method of multipliers (ADMM). This paper further examines the convergence of ADMM in presence of the neural network, which is one of the first attempts in the literature. The simple numerical study supports the provably optimal solutions being effective. The computational burden due to the complexity is still a limitation, and improving the computation efficiency remains for future work. That said, having a provably optimal solution is valuable as a benchmark when developing heuristic methods.

### A Proof of Lemma 1

$C$ in (II-B) is a lower triangular matrix with diagonal entries as $- 1$. Hence, $C$ is a full rank matrix of rank $4T_{p}$, and ${\text{Im}{(C)}} = {\mathbb{R}}^{4T_{p}}$. We have, ${\text{Im}{(Q)}} = \left. \{{y \in {\mathbb{R}}^{4T_{p}}} \middle| {y = {Qx} = {{\lbrack A,B\rbrack}x\text{such that~}x} \in {\mathbb{R}}^{2T_{p}}}\} \right. \subseteq {\mathbb{R}}^{4T_{p}} = {\text{Im}{(C)}}$. $\blacksquare$

### B Proof of Lemma 2

$A$ and $B$ are full column rank matrices of column rank $T_{p}$. Furthermore, $C$ is a full rank matrix of rank $4T_{p}$. Therefore, their null spaces are trivial, and hence, $H_{1},H_{2},H_{3}$ reduces to linear operators and satisfies the Lemma. $\blacksquare$

### C Proof of Lemma 3

$\Phi_{1}{(\mathbf{\Delta})}$, $\Phi_{2}{({\mathbf{α}})}$, and $\Phi_{3}{({\mathbf{Z}})}$ are $C^{2}$ functions, and hence, Lipschitz differentiable. Therefore, to show the Lipschitz differentiability of $J$, it is sufficient to show that $b_{i}{({\mathbf{Z}})}$, $i \in \mathcal{V}$, is Lipschitz differentiable for any $\tau \in {\{ 1,\ldots,T_{p}\}}$. For brevity of space, we define our notations in terms of $w \in {\{ x,y\}}$ where $w$ can either be $x$ or $y$. Let ${q_{w}{(\tau)}}:={2{({{w{(\tau)}} - {\phi_{i,w}{({\tau - 1})}}})}}$. We have Let $T_{k}^{w}:=\left| {\frac{\partial{b_{i}{({\mathbf{Z}}_{1})}}}{\partial{w{(k)}}} - \frac{\partial{b_{i}{({\mathbf{Z}}_{2})}}}{\partial{w{(k)}}}} \right|$ for some ${{\mathbf{Z}}_{1},{\mathbf{Z}}_{2}} \in \mathcal{Z}$, and let $({x^{m}{(\tau)}},{y^{m}{(\tau)}})$ denote the ego vehicle positions in ${\mathbf{Z}}_{m}$, where $m \in {\{ 1,2\}}$. Let $\phi_{i,w}^{{\mathbf{Z}}_{m}}$ denote $\phi_{i,w}$ corresponding to ${\mathbf{Z}}_{m}$. Using assumption (A2) and mean-value theorem, the neural network's outputs are Lipschitz continuous, i.e., ${\|{\phi_{i,w}^{{\mathbf{Z}}_{1}} - \phi_{i,w}^{{\mathbf{Z}}_{2}}}\|} \leq {\theta_{w}{\|{{\mathbf{Z}}_{1} - {\mathbf{Z}}_{2}}\|}}$. Let ${\Deltaw{(\tau)}} = {|{{w^{1}{(\tau)}} - {w^{2}{(\tau)}}}|}$, ${\varphi_{w}{({\tau - 1})}} = {|{{\phi_{i,w}^{{\mathbf{Z}}_{2}}{({\tau - 1})}} - {\phi_{i,w}^{{\mathbf{Z}}_{1}}{({\tau - 1})}}}|}$, and ${\nu_{x}^{w}{({\tau - 1})}} = \left| {\frac{\partial{\phi_{i,w}^{{\mathbf{Z}}_{1}}{({\tau - 1})}}}{\partial{x{(k)}}} - \frac{\partial{\phi_{i,w}^{{\mathbf{Z}}_{2}}{({\tau - 1})}}}{\partial{x{(k)}}}} \right|$. For any $k \in {\{ 1,\ldots,{\tau - 1}\}}$: where $L_{1}:={2{({{\theta_{x}{({1 + \theta_{x}})}} + {\theta_{y}{({1 + \theta_{y}})}} + {{({x_{max} + y_{max} + s_{x} + s_{y}})}L_{\nabla\phi}}})}}$, $x_{\max}$ and $y_{\max}$ are the bounds on the ego vehicle's $x$ and $y$ coordinates, respectively.

Similarly, for $k = \tau$, we have: Similarly, $T_{k}^{y} \leq {L_{1}{\|{{\mathbf{Z}}_{1} - {\mathbf{Z}}_{2}}\|}}$ for any $k \in {\{ 0,\ldots,{\tau - 1}\}}$, and $T_{k}^{y} \leq {L_{3}{\|{{\mathbf{Z}}_{1} - {\mathbf{Z}}_{2}}\|}}$, where $L_{3} = {2{({1 + \theta_{y}})}}$, for $k = \tau$.

Therefore, ${\|{{{\nabla b_{i}}{({\mathbf{Z}}_{1})}} - {{\nabla b_{i}}{({\mathbf{Z}}_{2})}}}\|} \leq {L_{g}{\|{{\mathbf{Z}}_{1} - {\mathbf{Z}}_{2}}\|}}$, where $L_{g} = {T_{p}{({{\max{\{ L_{1},L_{2}\}}} + {\max{\{ L_{1},L_{3}\}}}})}}$. Hence, $J{(\mathbf{\Delta},{\mathbf{α}},{\mathbf{Z}})}$ in is Lipschitz differentiable. $\blacksquare$

### D Proof of Theorem 1

Since $C$ is a full rank matrix, ${Im{(C)}} = {\mathbb{R}}^{4T_{p}}$, and hence, $D \in {Im{(C)}}$. Recall that the feasible sets for $\mathbf{\Delta}$, $\mathbf{α}$, and $\mathbf{Z}$ are bounded, i.e., ${\mathbf{\Delta} \in \mathcal{D}},{{\mathbf{α}} \in \mathcal{A}}$, and ${\mathbf{Z}} \in \mathcal{Z}$. Using these results and Lemmas 1-3, the optimization problem satisfies all the assumptions required for convergence of ADMM in non-convex and non-smooth optimization. Utilizing \[29, Theorem 2\] proves the convergence of Algorithm 1 for any sufficiently large $\rho > {\max{\{ 1,{{({1 + {2\sigma_{\min}{(C)}}})}L_{J}M}\}}}$. $\blacksquare$
