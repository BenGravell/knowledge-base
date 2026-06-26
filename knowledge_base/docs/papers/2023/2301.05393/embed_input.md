<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interaction-Aware Trajectory Planning for Autonomous Vehicles with Analytic Integration of Neural Networks into Model Predictive Control

Topics include Autonomous driving, Interaction-aware planning, Model predictive control, Trajectory prediction, Neural networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Integrates a neural interaction predictor analytically inside an MPC formulation so the planner can reason about other agents responses while optimizing the ego trajectory. The contribution is less a new predictor than a planner architecture that keeps learned interaction models usable inside constrained optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicles (AVs) must share the driving space with other drivers and often employ conservative motion planning strategies to ensure safety. These conservative strategies can negatively impact AV's performance and significantly slow traffic throughput. Therefore, to avoid conservatism, we design an interaction-aware motion planner for the ego vehicle (AV) that interacts with surrounding vehicles to perform complex maneuvers in a locally optimal manner. Our planner uses a neural network-based interactive trajectory predictor and analytically integrates it with model predictive control (MPC). We solve the MPC optimization using the alternating direction method of multipliers (ADMM) and prove the algorithm's convergence. We provide an empirical study and compare our method with a baseline heuristic method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning for autonomous vehicles (AVs) is a daunting task, where AVs must share the driving space with other drivers. Driving in shared spaces is inherently an interactive task, i.e., AV's actions affect other nearby vehicles and vice versa. This interaction is evident in dense traffic scenarios where all goal-directed behavior relies on the cooperation of other drivers to achieve the desired goal. To predict the nearby vehicles' trajectories, AVs often rely on simple predictive models such as assuming constant speed for other vehicles, treating them as bounded disturbances, or approximating their trajectories using a set of known trajectories. These models do not capture the inter-vehicle interactions in their predictions. As a result, AVs equipped with such models struggle under challenging scenarios that require interaction with other vehicles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

AVs can be overly defensive and opaque when interacting with other drivers, as they often rely on decoupled prediction and planning techniques. The prediction module anticipates the trajectories of other vehicles, and the planning module uses this information to find a collision-free path. As a result of this decoupling, AVs tend to be conservative and treat other vehicles as dynamic obstacles, resulting in a lack of cooperation. Figure 1 shows two scenarios in which the ego vehicle intends to merge into the left lane, but the inter-vehicle gaps are too narrow. In such scenarios, conservative AVs with decoupled prediction and planning are forced to wait for a long duration. In contrast, we propose an interaction-aware AV that can open up a gap for itself by negotiating with other agents, i.e., by nudging them to either switch lanes (Fig. 1(a)) or change speeds (Fig. 1(b)).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) techniques have been used to learn control policies under interactive or unknown environments. For example, adversarial RL is designed to reach the desired goal under uncertain conditions, and a model-free RL agent is developed for lane-changing control in dense traffic environments. However, these RL methods are not yet appropriate for safety-critical AVs due to their low interpretability and reliability.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing interaction-aware planners presents a significant challenge, as predicting the reactions of surrounding vehicles to the ego vehicle's actions is complex and non-trivial. Data-driven approaches, such as those using recurrent neural network architectures, have been effective in capturing the complex interactive behaviors of agents, especially in predicting driver behavior with high accuracy and computational efficiency. Therefore, it is desirable to utilize these data-driven methods to predict other vehicles' interactive behavior while maintaining safety through rigorous control theory and established vehicle dynamics models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a model predictive control (MPC) based motion planner that incorporates AV's decision and surrounding vehicles' interactive behaviors into safety constraints to perform complex maneuvers. In particular, we provide a mathematical formulation for integrating the neural network's predictions in the MPC controller and provide methods to obtain an (locally) optimal solution. However, the neural network integration and non-linear system dynamics make the optimization highly non-convex and challenging to solve analytically. Thus, prior efforts that integrate neural network prediction into MPC are numerical in nature and rely on heuristic algorithms to generate a finite set of trajectory candidates. In and, the authors generate these candidates by random sampling of control trajectories, and by generating spiral curves from source to target lane, respectively. In, the authors utilize a predefined set of reference trajectory candidates. Instead of solving the optimization, these approaches evaluate the cost of each candidate and choose the minimum cost trajectory that satisfies the safety constraint. Optimality is therefore restricted to trajectory candidates only, and the planner's performance depends on the heuristic algorithm design.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to these prior efforts, we avoid heuristics, detail a proper formalization, and solve the optimization with provable optimality. The optimal solution provides key insights to design better planners and can be leveraged to compare trajectories obtained by other heuristic methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The major contributions of this work are twofold: (i) we reformulate a highly complex MPC problem with a non-convex neural network and non-linear system dynamics, and systematically solve it using the Alternating Direction Method of Multiplier (ADMM) with generic assumptions (Section III), and (ii) we investigate the mathematical properties of the ADMM algorithm for solving the MPC with an integrated neural network. Specifically, we provide sufficient conditions on the neural network such that the ADMM algorithm in non-convex optimization converges to a local optimum (Section IV). It is one of the first attempts in the literature toward provable mathematical guarantees for a neural network-integrated MPC.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation and Controller Design", "weight": 1.0} -->

We design an MPC controller that leverages interactive behaviors of surrounding $N \in {\mathbb{N}}$ vehicles conditioned on the ego vehicle's future actions. The key to leverage interactions is to integrate a neural network and interactively update controls with step-size ${\Deltat} \in {\mathbb{R}}_{> 0}$ based on its inference (i.e., predicted positions during updates). This section further details the mathematical formulation of the MPC with the neural network.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Objective function", "weight": 1.0} -->

The controller's objective is to move from the current lane to the desired lane as soon as possible while minimizing control effort and ensuring safety and smoothness. Let $x^{\text{ref}}$ denote the maximum longitude coordinate until when the ego must transition to the target lane. Let $\parallel \cdot \parallel$ denote the Euclidean norm. For $x < x^{\text{ref}}$, we utilize the following objective (cost) function $J{({\mathbf{\Delta}{(t)}},{{\mathbf{α}}{(t)}},{{\mathbf{Z}}{(t)}})}$ similar to: where ${\mathbf{\Delta}{(t)}} \in \mathcal{D}$, ${{\mathbf{α}}{(t)}} \in \mathcal{A}$, and ${{\mathbf{Z}}{(t)}} \in \mathcal{Z}$ are the planned steering, acceleration, and state trajectories, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Objective function", "weight": 1.0} -->

$y^{\text{ref}} \in {\mathbb{R}}$ and $v^{\text{ref}} \in {\mathbb{R}}_{> 0}$ are the reference latitude coordinate of the desired lane and desired velocity, respectively, provided by a high-level planner. For a detailed description of each term, we refer the interested readers to.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To simplify the optimization, we linearly approximate the system dynamics before solving the MPC. This is possible because the control inputs obtained through the MPC are only applied for a single time-step, using a receding horizon control approach. As a result, any linearization errors from previous time-steps do not affect the MPC optimization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Safety Constraints", "weight": 1.0} -->

The safety constraints for collision avoidance depend on the nearby vehicles' trajectory prediction and the vehicle shape model. Let $\mathcal{V}$ denote the set of nearby vehicles surrounding the ego vehicle. Let $\phi{(\tau)}$ be a trained neural network that jointly predicts the future trajectories of the ego vehicle and its surrounding vehicles for $T_{pred}$ time-steps into the future based on their trajectories for $T_{obs}$ time-steps in the past. $\phi{(\tau)}$ is given: with $T_{pred} = 1$, where the first column represents the positions of the ego vehicle followed by the positions of $N$ surrounding vehicles.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Safety Constraints", "weight": 1.0} -->

Given the buffer of $T_{obs}$ past observations until time-step $\tau$, the coordinates of vehicle $i \in \mathcal{V}$ at time-step $\tau + 1$ are represented as: Some examples of the neural network $\phi{(\tau)}$ include social generative adversarial network (SGAN) and graph-based spatial-temporal convolutional network (GSTCN).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Interactive predictions over planning horizon $T_{p}$ are computed recursively using $\phi{(t)}$ with $T_{pred} = 1$ based on the latest reactive predictions and ego vehicle positions from the MPC's candidate solution trajectory.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We model the vehicle shape using a single circle to obtain a smooth and continuously differentiable distance measure to enable gradient-based optimization methods. Let $(x,y)$ and $({\hat{x}}_{i},{\hat{y}}_{i})$ be the position of the ego vehicle and the predicted positions of the surrounding vehicles $i \in \mathcal{V}$ (obtained using $\phi{(\tau)}$), respectively. Let ${r,r_{i}} \in {\mathbb{R}}_{> 0}$ be the radius of circles modeling ego vehicle and vehicle $i$, respectively. The safety constraint for the ego vehicle w.r.t vehicle $i$ then reads: where $\epsilon \in {\mathbb{R}}_{> 0}$ is a safety bound.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Using the single circle model, the safety constraints can be conservative, and consequently, the feasible solutions could be restrictive in some situations. We use it for its simplicity and to reduce the number of safety constraints. Some other alternatives for modeling the vehicle shape include the ellipsoid model and three circle model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-D Formulation of the Optimization problem", "weight": 1.0} -->

We now present the complete optimization problem for the receding horizon control in a compact form: In the next section, we solve the optimization using ADMM to determine a safe and interactive ego vehicle's trajectory.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Solving MPC with ADMM", "weight": 1.0} -->

There are many mathematical challenges associated with the MPC problem in Section II. Namely, it has the non-linear system dynamics, non-convex safety constraints, and dependence of the neural network predictions on its predictions in previous time steps ($T_{obs} \neq 1$). We now detail the systematic steps to solve the complex problem using ADMM, addressing the aforementioned mathematical challenges.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Solving MPC with ADMM", "weight": 1.0} -->

First, we construct a Lagrangian by moving the safety constraints, ${{b_{i}{({\mathbf{Z}})}} > 0},{i \in \mathcal{V}}$, in the optimization objective: where $\lambda_{s} \in {\mathbb{R}}_{> 0}^{T_{p}}$ is the vector of Lagrange multipliers.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 4", "weight": 1.0} -->

For theoretical analysis, we incorporate safety constraints into the optimization objective, but for our simulation study, we enforce them as hard constraints.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The optimization problem - is separable and the optimization variables $\mathbf{\Delta},{\mathbf{α}},{\mathbf{Z}}$ are decoupled in the objective function. Following the convention, the augmented Lagrangian is given: where $\rho > 0$ is the ADMM Lagrangian parameter and $\mu$ is the dual variable associated with the constraint. The complete algorithm is given by the Algorithm 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Update $\\mathbf{\\Delta}^{({k + 1})} = {{{argmin}_{\\mathbf{\\Delta} \\in \\mathcal{D}}\\mathcal{L}_{\\rho}}{(\\mathbf{\\Delta},{\\mathbf{α}}^{(k)},\\mathbf{Z}^{(k)})}}$", "weight": 1.0} -->

The sub-optimization problem for $\mathbf{\Delta}^{({k + 1})}$ is given by where $c_{\mathbf{\Delta}}^{(k)} = {{A\mathbf{\Delta}^{(k)}} - {F{(\mathbf{\Delta}^{(k)},{\mathbf{α}}^{(k)},{\mathbf{Z}}^{(k)})}}}$. It is a convex problem; hence, we can use a canonical convex optimization algorithm to find the optimal solution.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Update $\\mathbf{Z}^{({k + 1})} = {{{argmin}_{\\mathbf{Z} \\in \\mathcal{Z}}\\mathcal{L}_{\\rho}}{(\\mathbf{\\Delta}^{({k + 1})},{\\mathbf{α}}^{({k + 1})},\\mathbf{Z})}}$", "weight": 1.0} -->

The sub-optimization problem for ${\mathbf{Z}}^{({k + 1})}$ is given by where $c_{\mathbf{Z}}^{(k)} = {{C{\mathbf{Z}}^{(k)}} - {F{(\mathbf{\Delta}^{({k + 1})},{\mathbf{α}}^{({k + 1})},{\mathbf{Z}}^{(k)})}}}$. Due to the nonconvexity of the neural network in $b_{i}{({\mathbf{Z}})}$, the objective function (16 ‣ III Solving MPC with ADMM ‣ Interaction-Aware Trajectory Planning for Autonomous Vehicles with Analytic Integration of Neural Networks into Model Predictive Control")) is non-convex. We prefer the Quasi-Newton method for optimization to avoid expensive Hessian computation at each step.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Update $\\mathbf{Z}^{({k + 1})} = {{{argmin}_{\\mathbf{Z} \\in \\mathcal{Z}}\\mathcal{L}_{\\rho}}{(\\mathbf{\\Delta}^{({k + 1})},{\\mathbf{α}}^{({k + 1})},\\mathbf{Z})}}$", "weight": 1.0} -->

Hence, we utilize BFGS-SQP method, which employs BFGS Hessian approximations within a sequential quadratic optimization, and does not assume any special structure in the objective or constraints. For a solver, we use PyGranso, a PyTorch-enabled port of GRANSO, that enables gradients computation by back-propagating the neural network's gradients at each iteration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The state trajectory $\mathbf{Z}$ update has a larger complexity in the problem due to the presence of the non-convex neural network predictions. To expedite the $\mathbf{Z}$ update, an offline-trained function approximator such as a neural network can be utilized to estimate the gradients of the original neural network. The training dataset for gradient approximator can be generated using automatic differentiation or central differences approximations with original network.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Henceforth, we refer to our method as ADMM-NNMPC.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence of MPC with ADMM", "weight": 1.0} -->

Due to the inherent non-convexity of the neural network, the rigorous convergence analysis of ADMM in is not readily applicable. Thus, we extend the convergence analysis of ADMM with an integrated neural network, i.e., the convergence of the inner while loop in Algorithm 1. We first make the following assumptions on the neural network: At any time-step $\tau \in {\lbrack 0,T_{p}\rbrack}$, the neural network's outputs are bounded, i.e. ${|{\phi_{i,x}{(\tau)}}|} \leq s_{x}$ and ${|{\phi_{i,y}{(\tau)}}|} \leq s_{y}$, $i \in \mathcal{V}$, where ${s_{x},s_{y}} \in {\mathbb{R}}_{> 0}$ are constants.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergence of MPC with ADMM", "weight": 1.0} -->

Assumptions (A1)-(A3) are sufficient conditions under which the objective function is Lipschitz differentiable, i.e., it is differentiable and its gradient is Lipschitz continuous. This allows us to establish the convergence of Algorithm 1. Assumption (A1) is satisfied for a trained neural network for a bounded input space. Furthermore, neural network outputs can be clipped based on the feasible region. Lastly, neural networks with $C^{2}$ activation functions such as Gaussian Error Linear Unit (GELU) and Smooth Maximum Unit (SMU) satisfy assumptions (A2)-(A3).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Assumptions (A1)-(A3) are sufficient conditions and not necessary conditions. If the neural network architecture is unknown or it doesn't satisfy the assumptions, knowledge distillation can be used to train a smaller (student) network that satisfies the assumptions from the large (teacher) pre-trained network.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation Study", "weight": 1.0} -->

We now present the simulation results for ADMM-NNMPC. Figure 2 and 3 show the vehicles' positions at different time steps in two scenarios in which the ego vehicle (red) intends to merge into the left lane which is occupied by four other vehicles (blue) with a narrow inter-vehicle gap. In the two-lane scenario (Fig. 2), other vehicles can only change their speeds, while in the three-lane scenario (Fig. 3), other vehicles can also move laterally to transition into the leftmost lane. The other vehicles' positions at different time steps match the neural network's predictions, and hence, the ego vehicle's actions affect the trajectory of the other vehicles. In both scenarios, the ego vehicle is able to interact with the other agents and open a gap for itself to merge into.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Study", "weight": 1.0} -->

We compare ADMM-NNMPC with a baseline method called NNMPC on the two-lane and three-lane scenarios by utilizing the same cost function (cost function coefficients listed in Table I) and $T_{p} = 8$ time steps. NNMPC generates trajectory candidates by computing a finite set of spiral curves from the source lane to the target lane and selects the candidate with minimum cost. In both methods, we use a trained SGAN neural network for interactive motion prediction of the other vehicles. Table II compares the simulation results for the baseline NNMPC and ADMM-NNMPC in the two-lane and three-lane scenarios. In the two-lane scenario, while the ADMM-NNMPC successfully merges in the left lane, the NNMPC method fails to make a lane change due to limited trajectory candidates. In the three-lane scenario, ADMM-NNMPC successfully switches lanes much faster than NNMPC. Furthermore, ADMM-NNMPC outperforms NNMPC in terms of maximum cost and minimum distance from other vehicles in both scenarios.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Limitations and Future Works", "weight": 1.0} -->

Although we reduce the problem complexity by decomposing it into smaller sub-problems, these sub-problems are still complex which makes the approach non-scalable. Furthermore, due to the large neural network size and re-computation of gradients at each iteration, our current implementation runs slower than real-time. Nevertheless, having a slow offline optimization is useful, as it can serve as a benchmark when developing faster heuristic methods, ideally, we would like to increase the efficiency. Our approach can be made faster by training another neural network to estimate the original neural network's gradients and developing faster optimization libraries. Thus, future works include: (i) designing a smaller network trained with knowledge distillation, or (ii) expediting neural network's gradient estimation using an offline-trained function approximator such as a neural network.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions", "weight": 1.0} -->

With the importance of motion planning strategies being interaction-aware, e.g., lane changing in dense traffic for autonomous vehicles, this paper investigates mathematical solutions of a model predictive control with a neural network that estimates interactive behaviors. The problem is highly complex due to the non-convexity of the neural network, and we show that the problem can be effectively solved by decomposing it into sub-problems by leveraging the alternating direction method of multipliers (ADMM). This paper further examines the convergence of ADMM in presence of the neural network, which is one of the first attempts in the literature. The simple numerical study supports the provably optimal solutions being effective. The computational burden due to the complexity is still a limitation, and improving the computation efficiency remains for future work. That said, having a provably optimal solution is valuable as a benchmark when developing heuristic methods.
