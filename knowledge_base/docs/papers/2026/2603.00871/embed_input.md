<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Hippo: High-performance Interior-Point and Projection-based Solver for Generic Constrained Trajectory Optimization

Topics include Trajectory optimization, Motion planning, Robotics, Robustness, Benchmarks, Optimization, Planning, Control, Hippo, Sequential quadratic programming, Differential dynamic programming, IPM, Quadratic programming.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization is the core of modern model-based robotic control and motion planning. Existing trajectory optimizers, based on sequential quadratic programming (SQP) or differential dynamic programming (DDP), are often limited by their slow computation efficiency, low modeling flexibility, and poor convergence for complex tasks requiring hard constraints. In this paper, we introduce Hippo, a solver that can handle inequality constraints using the interior-point method (IPM) with an adaptive barrier update strategy and hard equality constraints via projection or IPM. Through extensive numerical benchmarks, we show that Hippo is a robust and efficient alternative to existing state-of-the-art solvers for difficult robotic trajectory optimization problems requiring high-quality solutions, such as locomotion and manipulation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Direct multiple shooting (DMS) plays an important role in modern robotic trajectory optimization due to its superior robustness and faster convergence. Several approaches enable faster resolution of the problem by exploiting the temporal sparsity structure in optimal control problems (OCP), using Riccati recursion or block elimination, which are fundamentally equivalent. Although many of them are successfully deployed for Model Predictive Control (MPC), they often fail to solve large-scale or difficult OCPs due to poor convergence and slow computation. These limitations hinder their reliable application to data generation for behavior cloning (BC) or task and motion planning (TAMP). In this paper, we propose a trajectory optimizer designed to address these issues.

<!-- chunk {"id": "body-0004", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

Popular constraint handling techniques are the interior point method (IPM) and the augmented Lagrangian method (ALM). Both have homotopy parameters (i.e., barrier parameters for IPM and penalty parameters for ALM) iteratively reduced to recover the solution to the original OCP.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

IPM converts inequality constraints to slacked equality constraints and relaxes complementary slackness in KKT conditions with an evolving barrier parameter. CALIPSO and robotoc implement a monotonic update rule of IPM, which reduces the barrier parameter when the KKT residual is lower than a threshold. However, it can be sensitive to the choice of initial barrier parameter. acados is an SQP solver based on HPIPM, an IPM-based QP solver with Mehrotra predictor-corrector (MP-C) adaptive barrier update strategy. It represents equality constraints as box-constrained inequalities with zero boundaries. In each SQP iteration, it calls HPIPM to solve the stagewise linear-quadratic (LQ) subproblem to an acceptable accuracy. Recently, piqp combined the proximal method of multipliers (similar to ALM) and IPM using MP-C, and achieved state-of-the-art performance in qpbenchmark.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

ALM transcribes constrained optimization to an unconstrained one by penalizing constraint violation. Specifically, aligator and mim_solver employ an ALM-like algorithm in a semi-smooth Newton form, a variant of the primal-dual active-set strategy (PDAS). The main problem with ALM is its poor convergence in solving inequality-constrained OCPs due to the explicit detection of active sets, and it can easily get trapped in local minima. In contrast, IPM enjoys polynomial convergence complexity thanks to the self-concordance of the barrier design. Another issue with ALMs is the penalty parameter scheduling scheme, which remains an open question. On the contrary, IPM has systematic adaptive barrier update strategies such as MP-C and quality functions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

The two-stage exact minimization framework of acados and mim_solver approximately solves the LQ subproblem in inner loops. For ALM-like methods, this can sometimes be helpful since it increases the chance of finding active sets using cheap recursion over only the value function Jacobians. For IPM, such inner loops can be computationally expensive since the Hessian factorization cannot be reused due to the varying slack and multipliers. Moreover, for nonlinear optimization, such a framework introduces additional solver parameters to control the termination of the inner loops, such as the subproblem tolerances. These parameters can be highly problem-specific and require careful hand-tuning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

IPM and ALM share common sparsity in their stagewise KKT system and thus can be solved in a similar routine: during the recursion, only the primal steps are computed; later in the post-recursion stage, dual steps are reconstructed in parallel. In, it is claimed that this splitting suffers from poor numerical conditioning due to inversion of diagonal coefficients, which may reach extreme values upon quasi-convergence. Instead, chose to use Cholesky LDLT factorization suitable for semi-positive-definite KKT linear systems, at the cost of slower computation due to the high complexity of LDLT and matrix-matrix multiplication with higher dimension. To further speed up the optimization, ocs2 parallelizes the sequential recursion by breaking the causal temporal structure of OCP into several segments so that recursion over each segment can start with the information from the last iteration. This corresponds to the classical parallel-in-time integration to solve initial value problems. Despite the speed improvement, this inconsistency can slow down convergence or even lead to divergence. aligator splits the trajectory using the segmental sensitivities w.r.t.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

the co-states, i.e., the dynamics multipliers at the breakpoints. Although its solution is exact and will not affect convergence, the computation of extra sensitivities and factorization render the speed improvements less promising.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

Apart from specialized OCP solvers, IPOPT is recognized as a generic robust nonlinear programming (NLP) solver and widely used to solve complex multi-contact trajectory optimization problems. In contrast with acados that requires two-stage exact minimization, IPOPT computes the primal-dual Newton step at each SQP iteration with powerful globalization, including feasibility restoration phases and filter line search. Despite its robustness, IPOPT does not exploit the temporal structure in OCPs, which makes it slow and limits its application in robotics. Recently, fatrop was proposed to mimic ipopt while exploiting the KKT block-sparsity of OCPs. However, it is restricted to explicit dynamics and lacks effective parallelism. A summary of the aforementioned solvers is shown in Table. I, Technical University of Munich (TUM), Germany majid.khadiv@tum.de").

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Related Works", "weight": 1.0} -->

Eq.iiiiiiEq./Ineq. - Equality/Inequality constraint handling.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Main Contribution", "weight": 1.0} -->

In this paper, we propose a simplistic solver implementation of regularized IPM and projection-based constrained SQP, namely Hippo. It supports generic OCP formulations including implicit dynamics and cross-timestep pure-state constraints. Similar to IPOPT, at each SQP iteration, Hippo directly solves the approximated QP for the primal-dual Newton step and handles hard equality constraints through either projection or IPM. Inspired, we use the MP-C scheme with a safeguard on the trial complementarity residuals. We show that Hippo can achieve robust convergence for difficult trajectory optimization problems. Furthermore, with a minimal number of tuning parameters and simple yet effective globalization, Hippo does not require careful hand tuning of solver parameters. Our systematic comparison with state-of-the-art solvers demonstrates the superiority of Hippo both in terms of convergence speed and number of problems it can solve.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Constrained Optimal Control", "weight": 1.0} -->

Notations: Throughout this paper, bold characters denote vector/matrix values and normal characters denote scalars. We use $F_{\mathbf{a}}$ to represent $\frac{\partial F}{\partial\mathbf{a}}$, and $F_{\mathbf{a}\mathbf{b}}$ to represent $\frac{\partial^{2}F}{\partial{\mathbf{a}{\partial\mathbf{b}}}}$. $\delta\mathbf{a}$ denotes a change in $\mathbf{a}$. $( \cdot )$ is used as a placeholder for symbols.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Constrained Optimal Control", "weight": 1.0} -->

In this paper, we aim to solve the following generic OCP for a given initial state $\mathbf{x}_{0}$

<!-- chunk {"id": "body-0015", "role": "body", "section": "Constrained Optimal Control", "weight": 1.0} -->

where $N$ is the number of shooting nodes, $\mathbf{x}_{k},\mathbf{u}_{k}$ are the state and input of the $k$th stage, $\mathbf{x}_{N}$ is the terminal state, $l_{N},l_{k}$ are terminal and state-input running costs, $\mathbf{f},{\mathbf{c}\text{~and~}\mathbf{s}}$ specify implicit discrete dynamics (suitable for general integrators), stacked state-input and state-only constraints, respectively. $\mathbf{ψ}$ denotes the state-input inequality constraints, and $\mathbf{\phi}$ denotes state-only inequality constraints.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Constrained Optimal Control", "weight": 1.0} -->

To simplify the notation, we omit the subscript $k$ in the rest of the paper, and use a triplet $(\mathbf{x},\mathbf{u},\mathbf{y})$ to represent the current state, input, and next state of the $k$th stage, i.e., $\mathbf{y}_{k} \equiv \mathbf{x}_{k + 1}$ for $k \in {\lbrack 0,{N - 1}\rbrack}$ and $\mathbf{y}_{N - 1} \equiv \mathbf{x}_{N}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Constrained Optimal Control", "weight": 1.0} -->

In this section, we introduce the efficient projection-based Riccati recursion to solve the equality-constrained OCP without inequalities. In Sec. III, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") we then explain how inequalities are handled with IPM. The overall workflow of the projection-based recursion is shown in Algorithm. 1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de").

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A1 Intermediate stages", "weight": 1.0} -->

which itself can be viewed as a constrained optimization problem. Similar to previous works, we introduce the stagewise Lagrangian $Q$-function of (2, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) as

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A1 Intermediate stages", "weight": 1.0} -->

In this work, we adopt a Gauss-Newton-like LQ approximation of (3, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) as, i.e., 1) all constraints are linearly approximated, and 2) the cost and value function $V$ are quadratically approximated. The corresponding KKT conditions can be written in the following recursive form

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A1 Intermediate stages", "weight": 1.0} -->

where ${\mathbf{ξ}} = {\lbrack\mathbf{u}^{\top},\mathbf{y}^{\top},{\mathbf{λ}}^{\top}\rbrack}^{\top}$. By solving (4, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")), its solution is

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A2 Terminal node", "weight": 1.0} -->

The Riccati recursion can then be performed backward: starting from the terminal node $V_{\mathbf{N}}$ derivatives, (4, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) is solved sequentially for $\delta{\mathbf{ξ}}$ sensitivities; $V{(\mathbf{y})}$ derivatives of the previous stage are updated by the chain rule of differentiation

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

By the definitions of $\mathbf{h}$ and $\mathbf{λ}$, the KKT system (4, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) can be expanded into

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

where the RHS are generic terms in $\mathbf{k}_{0}$ or $\mathbf{K}_{0}$. Null-space projection can be used to solve the above saddle-point problem. The invertibility of $\mathbf{f}_{\mathbf{y}}$ holds for common integrator dynamics in robotics, such as generic explicit/implicit Euler/RK4 integrators. Therefore, assuming invertible $\mathbf{f}_{\mathbf{y}}$, the following can then be introduced to facilitate later factorization of (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")):

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

whereby the nullspace basis ${\lbrack\mathbf{Z}_{\mathbf{u}}^{\top},\mathbf{Z}_{\mathbf{y}}^{\top}\rbrack}^{\top}$ of the LHS equality constraint Jacobians $\mathbf{h}_{\mathbf{u},\mathbf{y}}:={\lbrack\mathbf{h}_{\mathbf{u}},\mathbf{h}_{\mathbf{y}}\rbrack}$ (the $3 \times 2$ bottom left corner of (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"))) can be derived as

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

where $\mathbf{Z}_{\mathbf{u}},\mathbf{Z}_{\mathbf{y}}$ are respectively the nullspace basis $\mathcal{N}$ of the constraint Jacobians corresponding to $\mathbf{u},\mathbf{y}$. We can then split the primal solution ${\delta\mathbf{u}},{\delta\mathbf{y}}$ to (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) by

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

Similar to, by substituting (10, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) into (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) and left-multiplying the result by $\lbrack\mathbf{Z}_{u}^{\top},\mathbf{Z}_{y}^{\top}\rbrack$, (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) can be projected into the nullspace of $\mathbf{h}$ as

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

This reduced system is applicable to various constrained dynamics, particularly those involving contact dynamics. When no $\mathbf{s},\mathbf{c}$ is involved, $\mathbf{Z}_{\mathbf{u}} \equiv \mathbf{I}$ and $\mathbf{Z}_{\mathbf{y}} \equiv {- \mathbf{F}_{\mathbf{u}}}$, ${\delta\hat{(\cdot)}} = 0$, constituting classical Riccati recursion such as.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Projection-based Factorization", "weight": 1.0} -->

By solving (11, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) for $\delta\mathbf{z}$, we can recover the full primal step by (10, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"))

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

(Rank deficient constraint Jacobians) We use Eigen full pivoting LU factorization to compute (9, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) and the pseudoinverse solutions of the primal and dual steps. It features a threshold-based decision of nonzero pivots; thus, it can be relatively robust against poor numerical conditions. In practice, especially with contacts, a specially regularized factorizer such as the one in can be employed to obtain bounded approximate solutions and nullspace projectors. When the constraint Jacobians are highly rank-deficient, regularization might be insufficient to get valid Newton steps, and the solver can converge to infeasible stationary points. In such cases, globalization strategies should be employed to escape such situations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2", "weight": 1.0} -->

(Recursive nullspace projection) The derivation of the nullspace basis in (9, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) is inspired by the classical hierarchical QP-based whole body controllers. It can be further extended if parts of the projected ${\overline{\mathbf{h}}}_{u}$ are invertible, such as the case of lifted inverse dynamics with contacts, where one can use the inverse of the Delassus matrix to further derive an analytical nullspace projector.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Data: Initial trajectory of x, u, cost functions lk, lN, dynamics f, constraints c, s, ψ, ϕ and their multipliers
3in parallel for each node ⊳ Pre-solving steps
4 Update LQ approximation of the OCP. 5 Nullspace factorization to compute, $\delta\hat{(\cdot)}$ in and the precomputable parts of,. 6 Jacobian/Hessian modification by IPM. 8for k = N − 1 to 0 do ⊳ Backward recursion
9 Vy ← Vxk + 1, Vyy ← Vxxk + 1. 11 Update Qzz and ${\overline{\mathbf{y}}}_{0}$ for k0, K0 respectively. 12 Solve nullspace KKT system for Kz. 13 Update Vxxk, Vxk using.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 2", "weight": 1.0} -->

15in parallel for each node ⊳ Post-solving steps
20in parallel for each node ⊳ Post-rollout steps
22 ${\delta\mathbf{u}} = {{\mathbf{Z}_{\mathbf{u}}\delta\mathbf{z}} - {\delta\hat{\mathbf{u}}}}$. Algorithm 1 Single Iteration of SQP

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Value Function Derivative Propagation", "weight": 1.0} -->

Naively updating $V$ derivatives by (6, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) requires computing full primal and dual first-order sensitivities, leading to high computational cost in the recursion stage. However, the residual-sensitivity-products (RSPs) ${\mathbf{k}_{0}^{\top}\mathbf{K}_{\mathbf{ξ}}},{\mathbf{K}_{0}^{\top}\mathbf{K}_{\mathbf{ξ}}}$ can be transformed into a more computationally efficient form by exploiting the projection.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Value Function Derivative Propagation", "weight": 1.0} -->

By merging it with the primal part of the RSP, and splitting ${\delta\mathbf{u}^{r}},{\delta\mathbf{y}^{r}}$ into the nullspace and pseudoinverse steps by (10, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")), we have that for the current stage, ${\forall{( \cdot )}} \in {\{\mathbf{x},{\mathbf{x}\mathbf{x}}\}}$,

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Value Function Derivative Propagation", "weight": 1.0} -->

which is the $V_{\mathbf{y}/{\mathbf{y}\mathbf{y}}}$ of the previous stage as in (6, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")). In this way, we only need to compute the sensitivities in the nullspace during the recursion. Note that the parts unrelated to value function derivatives can be precomputed in parallel.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-D Linear Forward Rollout", "weight": 1.0} -->

To construct the full Newton step of all decision variables, linear forward rollouts are performed initially for $\delta\mathbf{y}$ using $\mathbf{k}_{\mathbf{y}},\mathbf{K}_{\mathbf{y}}$. The rest primal and dual steps are later constructed in parallel using the updated $\delta\mathbf{x}$ (from $\delta\mathbf{y}$). Note that the nonlinear rollout widely used in DDPs is not applied here since a linear rollout reconstructs the true Newton step and enjoys more solid theoretical convergence guarantees.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sparsity-Preserving Constraint Handling", "weight": 1.0} -->

In this section, we introduce a sparsity-preserving parallelizable regularized IPM implementation for both inequality constraints and rank-deficient equality constraints.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Regularized Primal-Dual Interior Point Method", "weight": 1.0} -->

Extending the equality constrained OCP to the full problem in (1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) with inequality constraints $\mathbf{g}$ results in a new Lagrangian $\overset{\sim}{Q}$ and its corresponding LQ-approximated KKT conditions

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A Regularized Primal-Dual Interior Point Method", "weight": 1.0} -->

where $\mathbf{ν}$ is the stacked inequality multiplier of $\mathbf{g}$, $\overset{\sim}{\mathcal{K}},{\overset{\sim}{\mathbf{k}}}_{0},{\overset{\sim}{\mathbf{K}}}_{0}$ are defined similarly to (4, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) but w.r.t. $\overset{\sim}{Q}$, $\odot$ denotes element-wise product. Note that $\mathbf{g}_{\mathbf{λ}} = \mathbf{0}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A Regularized Primal-Dual Interior Point Method", "weight": 1.0} -->

(15, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) can be transformed into an equality-constrained problem via the primal-dual interior point method, by introducing slack variables $\mathbf{t}$ into (15d, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) and relaxing the complementary slackness (15e, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) with a barrier parameter $\mu$, i.e., the perturbed KKT condition

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A Regularized Primal-Dual Interior Point Method", "weight": 1.0} -->

which is a bilinear system due to ${\mathbf{ν}} \odot \mathbf{t}$. Linearizing (16, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) w.r.t. ${\mathbf{ν}},\mathbf{t}$ results in the following new KKT system

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A Regularized Primal-Dual Interior Point Method", "weight": 1.0} -->

where $\mathbf{T} = {\text{diag}{(\mathbf{t})}}$, $\mathbf{N} = {\text{diag}{({\mathbf{ν}})}}$, $\rho$ is the multiplier regularization parameter to avoid ill-conditioning when $\mathbf{t}\rightarrow 0$. We can then exploit the structure of (17, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"))

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-A Regularized Primal-Dual Interior Point Method", "weight": 1.0} -->

Due to the diagonal nature of $\mathbf{T}_{\rho}^{- 1}\mathbf{N}$ and the definition of $\mathbf{g}$, $Q_{\mathbf{u}\mathbf{y}}$ will still be zero. Therefore, the sparsity in (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) is preserved. With the splitting in (18, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")), $({\mathbf{ν}},\mathbf{t})$-steps of different shooting nodes can be computed in parallel after the sequential forward rollout instead of solving the whole KKT system (17, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) directly.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Adaptive Barrier Strategy", "weight": 1.0} -->

We implemented the MP-C variant from to adaptively adjust the barrier parameter $\mu$. In the predictor step, (7, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) is factorized and the primal steps and IPM variables are computed with $\mu = 0$. The new $\mu$ is then computed as

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Adaptive Barrier Strategy", "weight": 1.0} -->

where $\sigma$ is the recentering parameter bounded within $\lbrack 0,1\rbrack$ and $n_{\text{ipm}}$ is the total dimension of IPM constraints. In the corrector step, the Lagrangian Jacobian is modified with the updated $\mu$ and a corrector term ${{\delta{\mathbf{ν}}} \odot \delta}\mathbf{t}$. The Riccati recursion is performed again to update the value function Jacobians $V_{\mathbf{x}}$ with the previous KKT factorization from the predictor step.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Adaptive Barrier Strategy", "weight": 1.0} -->

where $\alpha^{\max},\alpha_{\mathbf{ν}}^{\max}$ are respectively primal (including $\mathbf{t}$) and inequality dual step size bounds ($\tau = 0.995$ in our setting). We also implemented a safeguarding mechanism that will only accept the corrector term if the trial complementarity does not increase.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C Iterative Refinement", "weight": 1.0} -->

When the SQP with IPM is close to convergence, its poor numerical condition may cause relatively high error in the stationary condition and slow down convergence to high-accuracy solutions. If necessary, iterative refinement can be employed to reduce the error by setting the RHS $\mathbf{k}_{0}$ to be the stationarity residual and performing the recursion similar to the corrector step.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-D Fixed-size Backtracking Line Search", "weight": 1.0} -->

Similar to IPOPT, our solver applies $\alpha \leq \alpha^{\max}$ to both primal and equality dual steps, and $\alpha_{\mathbf{ν}} \leq \alpha_{\mathbf{ν}}^{\max}$ only to inequality dual steps. A simple fixed-step-size backtracking line-search is employed, which decreases $\alpha$ by a fixed step ${\Delta\alpha}:={\alpha^{\max}/n_{\text{ls}}}$ for a maximum number of trials $n_{\text{ls}}$ when no progress is made in both primal and dual residuals.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-D Fixed-size Backtracking Line Search", "weight": 1.0} -->

If it cannot find any descent step, to escape from such local stationary point, the solver 1) scales $\alpha^{\max}$ from (23, Technical University of Munich (TUM), Germany majid.khadiv@tum.de")) to be no higher than a predefined minimal value $\alpha^{\min}$ and 2) resets $\mu = 1$ and re-initialize the IPM slacks and multipliers. In practice, we found $\alpha^{\min} =$ $0.01$ a robust choice.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-E Equality Constraint Handling via IPM", "weight": 1.0} -->

When an equality constraint is potentially rank-deficient as introduced in Remark 1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"), projection-based handling might lead to severe difficulties for convergence. Similar to acados, such equality constraints can be transformed into box constraints with zero boundaries, i.e., ${{\mathbf{h} + \mathbf{t}_{p}} = \mathbf{0}},{{{\mathbf{t}_{n} - \mathbf{h}} = {\mathbf{0},\mathbf{t}_{p}}},{\mathbf{t}_{n} \succeq 0}}$, where $\mathbf{t}_{p},\mathbf{t}_{n}$ represent the bilateral slack variables and they will be pushed to zero simultaneously by IPM to ensure feasibility.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-F Implementation", "weight": 1.0} -->

The optimizer is implemented in C++ based on Eigen and BLASFEO. It also provides a code-generation pipeline for highly-optimized function derivative evaluation, based on CasADi and Pinocchio.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

Inner Loopiviviv’lin’ means only updating zero-order sensitivities. ’quad’ means com- puting new Newton steps of the LQ subproblems.
Param Update Scheme

<!-- chunk {"id": "body-0053", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

iterative refinement (lin)
per outer loop

<!-- chunk {"id": "body-0054", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

hpipm qp loops (quad)
reset per outer loop

<!-- chunk {"id": "body-0055", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

aligator(p)vvvthe serial version of aligator does not have inner loop w.r.t. SQP steps
iterative refinement (lin)
if primal res. &gt; tol

<!-- chunk {"id": "body-0056", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

ADMM step (lin)
per fixed num. updates

<!-- chunk {"id": "body-0057", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

In this section, we benchmark Hippo against prior works fatrop (commit 9a290fd ), acados (commit 6111f01), aligator (commit af2826), mim_solver (commit bd8852a) in two representative examples to show the robustness of our solver: 1) UR5 reaching to test its capability of handling rank-deficient hard constraints, and 2) Go2 locomotion to test its convergence under intermittent contacts in multi-contact settings commonly used in optimization-driven TAMP \dhédin2025simultaneouscontactsequencepatch,. Note that these are different from common MPC settings, which are usually simpler with good warm starts and do not require exact resolution (e.g. real-time iteration scheme that emphasizes timing per QP ). For all experiments, we carefully tuned the parameters of aligator and mim_solver such that they can solve as many problems as possible. Table. II, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") provides more details about each solver.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Benchmarks and Discussion", "weight": 1.0} -->

A test is marked 'Success' if the $L_{\infty}$ KKT residual (including constraint violation, stationarity, and complementarity) is below absolute tolerance. To ensure fair comparison, all tested solvers used linear rollout and line search; forward whole-body dynamics were used for problem formulation. For each test, the costs and initialization were unified for all solvers. The hardware platform is AMD Ryzen 9 7945HX. All solvers were compiled with -march=native. Hippo(i) represents tests with non-dynamics equality constraint handled as Sec. III-E, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"). Note that due to implementation limitations of fatrop, its total wall timing reported later will be the sum of solver-only timing and $\frac{\text{function-evaluation timing}}{\text{number of threads}}$ for comparison. However, in practice, the wall time of fatrop will be much higher due to the lack of parallelization of the solver and the inefficient evaluation of functions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

Paramvivivibarrier parameter for IPM and penalty parameter for ALM/ADMM.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

5/20viiviivii(..) the number of fixed inner steps to update the penalty parameters.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

In this experiment, we borrow the UR5 reaching task, i.e.,

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

where $\mathcal{U}$ denotes uniform distribution. Each target is paired with a random initial configuration uniformly sampled from $\mathcal{U}{\lbrack{- 1},1\rbrack}$ as. The target is added as a hard constraint $\mathbf{m}$ for the terminal state, i.e.,

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

where $\mathbf{M}_{N} \in {SE{}}$ is the terminal end-effector placement and $\ominus$ denotes the $SE{}$ difference and $\log$ is the logarithmic map from $SE{}$ to ${\mathfrak{s}}{\mathfrak{e}}{}$. The trajectory horizon is $N = 50$, with a timestep of $20$ms. State and torque limits are included. Each test runs on 4 threads. The solver settings are shown in Table. III, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") and the result is shown in Fig. 1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"). The termination absolute tolerance is 1e-3. We used the serial version of aligator (marked by (s)), because we encountered numerical issues with its parallel version (denoted as aligator(p)).

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

For fatrop, we use the compiled version of its code-generated CasADi OptiStack interface to maximize its performance. We used a high iteration limit from for the ALM baselines since they often require more iterations to converge. Two sets of parameters of mim_solver were used as recorded in Table III, Technical University of Munich (TUM), Germany majid.khadiv@tum.de").

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

36/81viiiviiiviiiOnly 36 out of the 81 solutions have acceptable slack values (≤1e-3).

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

tixixix‘#‘: number of solved problems; ‘t‘: average timing per QP (ms)

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

As shown in Fig. 1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") and Table. IV, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"), Hippo(i) solved more problems than Hippo due to the potential Jacobian rank-deficiency of $\mathbf{m}$ but with more iterations. Benefiting from the ipopt globalization scheme, fatrop solved more tests than Hippo but still fewer than Hippo(i). acados only works with heavily penalized slacks to push the primal residual below the tolerance and consequently prone to local infeasible minima. aligator and mim_solver solved similar numbers of problems to Hippo(i) with more iterations. This demonstrates that our regularized IPM-based equality-constraint handling is more robust and efficient, despite requiring more iterations than pure projection, since $\mu$ must be gradually driven to zero.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

It is worth noting that Hippo does not solve QP subproblems the fastest due to the generic nullspace projection. In contrast, fatrop and the HPIPM backbone of acados fully exploit the efficient BLASFEO; aligator and mim_solver utilize pinocchio to directly eliminate the contact forces by computing its derivative w.r.t. the kinematic states. The speed advantage of hippo is typically due to its lower number of QP iterations, since it converges with fewer iterations and does not require exact minimization of subproblems. fatrop also showed a similar speed advantage. On the contrary, each SQP step of mim_solver and acados can take a large number of inner iterations but make little progress, especially if the subproblem is already ill-conditioned, e.g., mim_solver/ data in Fig. 1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de").

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-A UR5 Random Reaching", "weight": 1.0} -->

As discussed in Remark 1, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"), for ill-posed OCPs, escaping local infeasible points by taking primal steps via globalization is more effective than exact minimization of LQ subproblems. In our practice, we found that acados and mim_solver are highly sensitive to their inner-loop settings.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

Paramxxxbarrier parameter for IPM and penalty parameter for ALM/ADMM

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

100xixixi(..) the number of fixed steps to update the penalty parameters

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

RSxiixiixiiR: reduced; S: simple; F: full; H: hard. ’#’: number of solved problems. ’t’: average timing (ms) per QP.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

In this experiment, we formulate a generic quadruped locomotion problem where the robot moves towards two randomly sampled reference base x-y positions within a rectangular area centered around the robot initial position (i.e., the origin). Two gaits (trot and hopping) are tested, and each is added to the OCP as explicit phase contact constraints. The termination absolute tolerance is 1e-3. We provide two difficulty levels of the randomly sampled references. Let $\mathbf{r}_{1},\mathbf{r}_{2}$ be the desired base position after the first and last step, respectively. The simple version samples $\mathbf{r}_{2}$ from a small region, and then uses the middle point as $\mathbf{r}_{1}$, i.e.,

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

The hard version samples from a larger area for two unrelated $\mathbf{r}_{1},\mathbf{r}_{2}$, leading to larger movements, i.e.,

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

The regularization cost for this example assigns higher weights to base states, emphasizing the tracking of position references. Joint and torque limits are included. No foot references are provided, similarly to. We tested two constraint settings: 1) "full" with friction cone and position-level contact constraint ${\lbrack v_{c,x},v_{c,y},{v_{c,z} + {100z_{c}}}\rbrack}^{\top} = \mathbf{0}$ where $v_{c,{( \cdot )}}$ are the linear contact velocities and $z_{c}$ is the foot height; 2) "reduced" without the friction cone and only the zero-contact-velocity constraints, while $z_{c}$ is penalized. The ALM solver parameters are recorded in Table. V, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"); the IPM ones are the same as Table.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

III, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"). To our best effort, fatrop is tested with direct CasADi OptiStack interface since we were not able to compile the over-sized code-generated file. The results for this scenario are shown in Fig. 2, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") and Table. VI, Technical University of Munich (TUM), Germany majid.khadiv@tum.de").

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

Hippo and Hippo(i) solved nearly all problems except for the reduced hard setting. The failures stemmed from the simplistic globalization scheme III-D, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") that results in small steps upon quasi-convergence. Conversely, fatrop leveraged the systematic ipopt globalization and solved all tests. acados solved fewer cases and failed reduced hopping tests completely. These observations indicate that reduced OCPs with penalties rather than constraints are prone to degeneracy and require systematic globalization. It explains the performance drop of Hippo and the catastrophic failure of acados.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

Moreover, the local minima of such OCPs could be infeasible, as seen in the acados results from Table IV, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") of Sec. IV-A, Technical University of Munich (TUM), Germany majid.khadiv@tum.de"), and thus being less useful for constraint-based planning such as \[30, dhédin2025simultaneouscontactsequencepatch, 34\]. In strictly constrained full settings, Hippo/Hippo(i) demonstrated the fastest speed and comparable robustness to fatrop, even in hopping tests where fatrop took fewer QP iterations. This shows the effectiveness of the parallelism and globalization of our solver in handling constrained OCPs. In contrast, despite a higher iteration budget, aligator and mim_solver could only solve parts of the reduced tests and failed all full settings.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-B Go2 2-step Locomotion", "weight": 1.0} -->

These results again corroborate the superior robustness and convergence of IPM over ALM as discussed in Sec. I-A, Technical University of Munich (TUM), Germany majid.khadiv@tum.de") and IV-A, Technical University of Munich (TUM), Germany majid.khadiv@tum.de").

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduced Hippo, a minimalistic implementation of interior-point and projection-based SQP. Hippo demonstrated robust convergence in the benchmark of hard examples against existing state-of-the-art solvers without a heavy workload on solver parameter tuning. As a generic constrained trajectory optimizer, Hippo could be helpful for data generation for IL and optimization-driven TAMP. For future work, more comprehensive globalization strategies, such as the IPOPT feasibility restoration phase and filter line search, could be integrated into the solver framework to further enhance its robustness.
