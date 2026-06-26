<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Global and Local Convergence of Iterative Linear Quadratic Optimization Algorithms for Discrete Time Nonlinear Control

Topics include Trajectory optimization, iLQR, Differential dynamic programming, Convergence analysis, Nonlinear control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes both global and local convergence properties of iterative LQR/DDP algorithms for discrete-time nonlinear control, providing theoretical convergence guarantees under specific regularity conditions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A classical approach for solving discrete time nonlinear control on a finite horizon consists in repeatedly minimizing linear quadratic approximations of the original problem around current candidate solutions. While widely popular in many domains, such an approach has mainly been analyzed locally. We provide detailed convergence guarantees to stationary points as well as local linear convergence rates for the Iterative Linear Quadratic Regulator (ILQR) algorithm and its Differential Dynamic Programming (DDP) variant. For problems without costs on control variables, we observe that global convergence to minima can be ensured provided that the linearized discrete time dynamics are surjective, costs on the state variables are gradient dominated. We further detail quadratic local convergence when the costs are self-concordant. We show that surjectivity of the linearized dynamics hold for appropriate discretization schemes given the existence of a feedback linearization scheme. We present complexity bounds of algorithms based on linear quadratic approximations through the lens of generalized Gauss-Newton methods. Our analysis uncovers several convergence phases for regularized generalized Gauss-Newton algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider nonlinear control problems in discrete time of the form where at the time index $t$, $x_{t}$ is the state of the system, $u_{t}$ is the control applied to the system, $f_{t}$ is the discretized nonlinear dynamic, $h_{t}$ is the cost applied to the system state and the control variable, and ${\overline{x}}_{0}$ is a given fixed initial state.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problems of the form have been tackled in various ways, from direct approaches using nonlinear optimization to convex relaxations using semidefinite optimization. Numerous packages exist for such problems such as CasAdi, Pyomo, JumP, IPOPT, or SNOPT, Crocoddyl, acados. A popular approach proceeds by computing at each iteration the linear quadratic regulator associated to a linear quadratic approximation of the problem around the current candidate solutions. The resulting feedback policy can then be applied on the linearized dynamics as in the Iterative Linear Quadratic Regulator (ILQR) algorithm,. Alternatively, the feedback policy can be applied on the original dynamics, as in the iterative Linear Quadratic Regulator (iLQR) algorithm akin to a Differential Dynamic Programming (DDP) approach. To avoid confusion, we name this second approach Iterative Dynamic Differentiable Programming (IDDP).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

Empirically, these approaches often exhibit fast convergence to efficient or optimal controllers which explain their popularity in applied control, and the renewed interest for linear quadratic control in neuro-dynamic programming and reinforcement learning. The empirical performance of the ILQR and IDDP algorithms are illustrated in Figure 1. The first problem considered in Figure 1 consists in swinging up a pendulum to a vertical position in finite time, the second problem consists in controlling a simple model of a car to be at predefined positions at given times. The detailed experimental setting is presented in Section 5. Most importantly, the costs consists in quadratic state costs bounded below by 0, i.e., of the form ${h_{t}{(x_{t},u_{t})}} = {{({x_{t} - {\hat{x}}_{t}})}^{\top}Q_{t}{({x_{t} - {\hat{x}}_{t}})}}$ for $Q_{t}$ positive definite and ${\hat{x}}_{t}$ a reference state.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

In Figure 1, we plot $c^{(k)}/c^{}$ in log-scale, where $c^{(k)} \geq 0$ denotes the total cost at iteration $k$ computed by means of a gradient descent, an ILQR algorithm or an IDDP algorithm, and $c^{}$ denotes an initial cost given by initializing the control variables at $0$. We observe that both the ILQR and the IDDP algorithms converge to an optimal cost, i.e., $c^{(k)}\rightarrow 0$. Moreover, both algorithms outperform a simple gradient descent and appear to exhibit a fast convergence after some iterations. The empirical behavior illustrated in Figure 1 does not hold for any nonlinear control problem as illustrated in Appendix I with a more realistic model of a car taken from Liniger et al.. Yet, the examples presented in Figure 1 are surprising from an optimization viewpoint as the problems considered escape the usual paradigm of convex or linear optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

The empirical efficiency of ILQR and IDDP on some nonlinear control problems, as the ones illustrated in Figure 1, motivates then the following questions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivation", "weight": 1.0} -->

*What conditions on a discrete time nonlinear control problem ensure algorithms such as ILQR and IDDP converge to a globally optimal solution?* *What convergence behaviors can we expect from these algorithms?* We first present generic convergence results for the ILQR and IDDP algorithms on problems. These results ensure global convergence to stationary points and local convergence to minima in Theorems 2 and 3. However, the aforementioned convergence results do not explain the convergence to *global minima* observed in Figure 1.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation", "weight": 1.0} -->

We then turn our attention to nonlinear control problems without control costs and with time-invariant dynamics $f$, i.e., problems of the form Considering time-invariant dynamics make clearer the relationship with the underlying continuous dynamical system. Generalizations to time-variant systems are pointed out when applicable. However, problems of the form conserve the main challenge of generic discrete time control problems, that is, the nonlinearity of the dynamics, which prevent us from using classical results from convex analysis even if the state costs $h_{t}$ are convex. The nonlinearity of the dynamics distinguish problems from the linear quadratic settings studied, e.g., Fazel et al.; Zhang et al.; Sun and Fazel; Lin et al., for which convergence to global minima of policy methods have been shown by means of algebraic considerations. The absence of costs on controls variables restrict the problem class compared to problems of the form. However, this also allows focusing on the properties of the dynamics to understand the properties of non-convex problems and paves the way to analyze generic problems of the form.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Approach", "weight": 1.0} -->

Our analysis stems from observing that, for strongly convex costs, convergence to global minima of the ILQR or IDDP algorithms is ensured if the linearized dynamics, i.e., the mappings $v\mapsto{{\nabla_{u}f}{(x,u)}^{\top}v}$, are surjective, where ${{\nabla_{u}f}{(x,u)}^{\top}} \in {\mathbb{R}}^{n_{x} \times n_{u}}$ is the Jacobian of the dynamic with respect to the control variable on a state $x$ for a given control $u$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Approach", "weight": 1.0} -->

To quantify the convergence of the ILQR and IDDP algorithms, we consider the existence of a parameter $\sigma$ such that where ${\sigma_{\min}{({{\nabla_{u}f}{(x,u)}})}} = {\inf_{\lambda \in {\mathbb{R}}^{n_{x}}}{{\|{{\nabla_{u}f}{(x,u)}\lambda}\|}_{2}/{\|\lambda\|}_{2}}}$ is the minimal singular value of the transpose Jacobian of the discrete time dynamics $f$ w.r.t. the control variable. Eq. ensures the injectivity of $\lambda\mapsto{{\nabla_{u}f}{(x,u)}\lambda}$ which is equivalent to the surjectivity of $v\mapsto{{\nabla_{u}f}{(x,u)}^{\top}v}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Approach", "weight": 1.0} -->

Our main theorem is then stated below for strongly convex costs provided adequate smoothness assumptions on the costs and the dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Outline", "weight": 1.0} -->

We start by presenting classical nonlinear control algorithms for problem, i.e., the Iterative Linear Quadratic Regulator (ILQR) and its variant IDDP, a.k.a. iLQR, in Section 2.1 and Section 2.2, and cast them as closed-box oracles. We provide convergence guarantees to stationary points of both algorithms for generic problems of the form, as well as linear local convergence guarantees, in Section 2.3. We analyze the properties of problem with respect to the dynamics $f$ in terms of smoothness and surjectivity of the linearized dynamics in Section 3.1. We further decompose the properties of the dynamic $f$ with respect to the underlying discretization scheme in Section 3.2. We analyze the convergence of the ILQR and IDDP algorithms, respectively, Section 4.2, Section 4.3. In particular, in Section 4.2.1, we demonstrate the convergence to global optima of the ILQR algorithm provided that the costs are gradient dominated, the dynamics have surjective linearizations and both costs and dynamics are smooth.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Outline", "weight": 1.0} -->

We show the *local quadratic convergence* of the ILQR algorithm provided that the costs are self-concordant, the dynamics have surjective linearizations and both costs and dynamics satisfy appropriate smoothness conditions in Section 4.2.2. Theorem 1 is detailed for the ILQR algorithm in Section 4.2.3 and convergence of the IDDP algorithm is analyzed in Section 4.3. Numerical experiments are presented in Section 5 to assess the theoretical findings. We discuss related work in Section 6.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

Additional numerical illustrations of the ILQR and IDDP algorithms can be found in the companion paper and reproduced or further explored by using the companion toolbox

<!-- chunk {"id": "body-0017", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

For problems of the form, we demonstrate global convergence to stationary points and local linear convergence to minima of both ILQR and IDDP algorithms under usual regularity assumptions (Theorems 2, 3). For problems of the form, we make the following contributions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

We present sufficient conditions for convergence to a global minimum of the problem through the lens of a *gradient-dominating property* of the objective. Namely, we show that a gradient-dominating property of the objective can be decomposed into the properties of the discrete time dynamic and ensured for appropriate discretization schemes (Lemma 6, Theorem 10).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

We prove that the ILQR algorithm *converges to a global minimum* if the cost is smooth, gradient dominated, and if the dynamic is smooth with non-singular transpose Jacobians (Theorem 13).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

We prove that the ILQR algorithm *converges locally with a quadratic rate* if the cost is smooth and self-concordant, and if the dynamic is smooth with non-singular transpose Jacobians (Theorem 18).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

We show and detail the *global and local convergence* to minima of both ILQR and IDDP algorithms for smooth and strongly convex costs and smooth dynamic with non-singular transpose Jacobians (Theorems 21 and 24).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Inspired from the theoretical findings, we also present a line-search variant of the ILQR algorithm that keep the same global and local convergence guarantees to minima, while not requiring any knowledge of problems constants (Corollary 23).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Nonlinear Control Algorithms", "weight": 1.0} -->

The objective in only depends on the control variables ${\mathbf{u}} = {(u_{0};\ldots;u_{\tau - 1})} \in {\mathbb{R}}^{\tau n_{u}}$ and can be written as Problem consists then in minimizing $\mathcal{J}$. In the following, we always *assume that $\mathcal{J}$ has at least one minimizer $\mathbf{u}^{\ast}$*. The classical ILQR, and IDDP algorithms compute the next iterate as ${{\mathbf{u}}_{next} = {{\mathbf{u}} + {{{Oracle}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}}}},$ for given control variables $\mathbf{u}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Nonlinear Control Algorithms", "weight": 1.0} -->

Here, ${Oracle}_{\nu}{(\mathcal{J})}$ is an oracle, which, given a regularization parameter $\nu$ and control variables $\mathbf{u}$, outputs a direction ${{Oracle}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}$. The original ILQR or IDDP algorithms did not incorporate an additional regularization. Our implementation is a variant that leads to non-asymptotic convergence guarantees of these algorithms.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

Given control variables ${\mathbf{u}} = {(u_{0};\ldots;u_{\tau - 1})}$ with associated trajectory $x_{1},\ldots,x_{\tau}$, and a regularization $\nu > 0$, an Iterative Linear Quadratic Regulator (ILQR) algorithm computes the next command by computing the Linear Quadratic Regulator (LQR) associated with a quadratic approximation of the costs and a linear approximation of the dynamics around the current trajectory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

Formally, the next iterate is computed as ${\mathbf{u}}_{next} = {{\mathbf{u}} + {{{LQR}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}}}$, where The minimum above is well-defined as long as either the costs are convex, or the regularization $\nu$ is large enough. The implementation of the ILQR oracle is presented in Algorithm 1. Its computational scheme is illustrated in Figure 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

Problem is first instantiated in a *forward pass* by collecting all first order or second order information on the dynamics and the costs necessary to pose problem.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

Problem is then solved by dynamic programming.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

Namely, the cost-to-go $c_{t}{(y_{t})}$ from a state $y_{t}$ at time $t$ is computed recursively in a *backward pass* as, starting from ${c_{\tau}{(y_{\tau})}} = {{\frac{1}{2}y_{\tau}^{\top}P_{\tau}y_{\tau}} + {p_{\tau}^{\top}y_{\tau}}}$, where $J_{t}$, $j_{t}$ are computed recursively in line 12 of Algorithm 1. The optimal control at time $t$ from state $y_{t}$ is then given by an affine policy where $K_{t},k_{t}$ are computed in line 13 of Algorithm 1. The cost-to-go functions and policies are well-defined as long as all costs $h_{t}$ are convex or if the regularization $\nu$ is large enough (see

<!-- chunk {"id": "body-0030", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

The solution of the LQR problem, is given by *rolling-out* the policies along the linear trajectories of. The oracle is ${{{LQR}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}} = {(v_{0};\ldots;v_{\tau - 1})}$, where, starting from $y_{0} = 0$, Solving by dynamic programming comes at a linear cost with respect to the length of the trajectory. Namely, in terms of elementary computations, the ILQR oracle has a computational cost Note that, in nonlinear control problems, the state and control dimensions are generally small. On the other hand, the horizon $\tau$ may be large if, for example, for a fixed continuous time horizon, a small discretization stepsize was used to define. The ILQR algorithm keeps a linear complexity with respect to the leading dimension $\tau$ of the problem.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

The linear quadratic problem can also be solved by alternative linear algebra subroutines ranging from matrix-free solvers that take advantage of differentiable programming framework, or by introducing Lagrange multipliers. We refer to Wright, for more details.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Iterative Linear Quadratic Regulator", "weight": 1.0} -->

Overall an ILQR algorithm computes a sequence of iterates as starting from control variables ${\mathbf{u}}^{}$, where $\nu_{k}$ are regularization parameters that may depend on the current iterate and ${LQR}_{\nu}$ is implemented by Algorithm 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Iterative Differential Dynamic Programming", "weight": 1.0} -->

The IDDP algorithm is an instance of a Differential Dynamic Programming (DDP) approach. A DDP approach considers computing approximate solutions of around the current iterate by dynamic programming using approximations of the dynamics and the costs. We refer the reader to, e.g., Jacobson and Mayne; Tassa et al.; Roulet et al. for a detailed presentation. The original DDP approach uses quadratic approximations of the dynamics. Here, we focus on the implementation using linear approximations of the dynamics and quadratic approximations of the costs as used, e.g., Tassa et al.. In this case, a DDP approach amounts to computing the same policies $\pi_{t}$ as an ILQR algorithm but rolling-out the policies along the original dynamics rather than the linearized ones.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Iterative Differential Dynamic Programming", "weight": 1.0} -->

Namely, the oracle output by IDDP is given as as presented in Algorithm 1. The computational complexity of this approach is the same as the one of the ILQR approach. By iterating the above steps, starting from initial control variables ${\mathbf{u}}^{}$, we obtain the iterative Linear Quadratic Regulator (IDDP) algorithm, which computes iterates of the form where the regularization parameters $\nu_{k}$ may depend on the current iterate and ${DDP}_{\nu}$ is implemented by Algorithm 1.\1:Inputs: Controls u = (u0; …; uτ − 1) ∈ ℝτnu, regularization ν > 0, initial state ${\overline{x}}_{0} \in {\mathbb{R}}^{n_{x}}$, horizon τ, dynamic f: ℝnx × ℝnu → ℝnx, costs (ht)t = 1τ, oracle type Oracle ∈ {LQR, DDP}.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Iterative Differential Dynamic Programming", "weight": 1.0} -->

2:Forward pass ⊳ instantiate problem for the given control variables 6: Compute and store Pt = ∇xtxt2ht(xt, ut), Qt = ∇utut2ht(xt, ut), Rt = ∇xtut2ht(xt, ut) 9:Backward pass ⊳ compute optimal policies for problem 12: Compute the cost-to-go functions $c_{t}:{y_{t}\rightarrow{{\frac{1}{2}y_{t}^{\top}J_{t}y_{t}} + {j_{t}^{\top}y_{t}}}}$ defined in as 13: Store the policies πt: yt → Ktyt + kt defined in (2.1) as 15:Roll-out pass ⊳ apply the computed policies along the linearized or the exact dynamics 18: if Oracle is LQR then 19: Compute vt = πt(yt), yt + 1 = Atyt + Btvt 20: else if Oracle is DDP then 24:Output: Control directions v = (v0; …; vτ

<!-- chunk {"id": "body-0036", "role": "body", "section": "Iterative Differential Dynamic Programming", "weight": 1.0} -->

− 1) Algorithm 1 ILQR and IDDP steps for problem

<!-- chunk {"id": "body-0037", "role": "body", "section": "Generic Convergence Guarantees", "weight": 1.0} -->

We start by presenting convergence guarantees of the ILQR and IDDP algorithm for generic problems of the form. First, with an appropriate choice of regularization both algorithms can converge globally to a stationary point at a polynomial rate (Theorem 2). Such a stationary point of $\mathcal{J}$ satisfies naturally necessary optimality conditions for problem as recalled in Appendix B. Note that necessary optimality conditions in discrete time control problem differ from their continuous time counterpart as discussed in detail in Appendix B.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Compared to a Newton method that can converge locally at a quadratic rate on problems of the form, the ILQR and IDDP algorithms converge locally only at linear rate a priori (see also Baumgärtner et al. ). Similarly, the original Differential Dynamic Programming (DDP) approach of Jacobson and Mayne can converge locally at a quadratic rate. However, the local linear convergence rates presented in Theorem 3 do not match the superlinear rates observed in practice in Figure 1 (see also Roulet et al. ). Hence, we consider in the following additional properties of the problem that can uncover both the global convergence of the ILQR and IDDP algorithms as well as their fast local convergence.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conditioning Analysis", "weight": 1.0} -->

To understand the convergence behavior of the ILQR and IDDP algorithms displayed in Figure 1, we consider a restricted class of control problems without control costs of the form. Namely, from now, we consider objectives of the form for ${\mathbf{u}} = {(u_{0};\ldots;u_{\tau - 1})} \in {\mathbb{R}}^{\tau n_{u}}$. Such objectives keep the main difficulty of nonlinear control problems: for nonlinear dynamics $f$, the overall objective $\mathcal{J}$ is non-convex such that convergence to global minima is a priori not guaranteed by even a simple gradient descent. Nevertheless, by decomposing the objective at the scale of the dynamics, and further decomposing the dynamics by an appropriate discretization scheme, we can identify sufficient conditions for convergence to global minima linked to usual notions in nonlinear control. We can then further show the convergence of the ILQR and IDDP algorithms to a global minimum, and detail the several phases of convergence (Sections 4.1, 4.2, 4.3).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Objective Decomposition", "weight": 1.0} -->

The objective $\mathcal{J}$, defined, can be decomposed into (i) the costs associated to a given trajectory, and (ii) the function that, given an input command, outputs the corresponding trajectory, defined below.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Dynamic Decomposition", "weight": 1.0} -->

We have isolated condition as a sufficient condition to ensure convergence of, e.g., a gradient descent, to global minima. It remains to consider whether this assumption can be satisfied on concrete examples. Note that assumption requires $n_{u} \geq n_{x}$. While the underlying continuous control problem may have less control variables than state variables, by considering multiple steps of a simple Euler discretization method, we may still ensure the validity of as illustrated in Example 1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider the continuous time evolution of a pendulum where $\theta$ is the angle with the vertical axis, $\omega$ is the angular speed, $u$ is a torque applied to the pendulum which defines the control we have on the system, and $m$, $l$, $\mu$, $g$ are physical constants of the problem described in Section 5. The state is defined by $x = {(\theta,\omega)}$. Using a simple Euler scheme, the discretized dynamics cannot satisfy, since we would have only one variable $u_{t}$ to control two elements, $\theta_{t},\omega_{t}$, at each time step $t$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 1", "weight": 1.0} -->

On the other hand, one can consider a two-step discretization scheme such that the controls are divided in two variables $u_{t} = {(v_{t},v_{t + {1/2}})}$. The dynamics read then where $\Delta$ is some discretization step. Intuitively, the variable $v_{t + {1/2}}$ fully controls $\omega_{t + 1}$, while the variable $v_{t}$ fully controls $\theta_{t + 1}$. One can verify that the Jacobian of the discretized dynamics $x_{t + 1} = {f{(x_{t},u_{t})}}$ for $u_{t} = {(v_{t},v_{t + {1/2}})}$ are then surjective which then ensure the surjectivity of the overall control of the pendulum in $\tau$ steps and the efficiency of the ILQR and IDDP algorithms as observed in Figure 1 and further justify in Section 4.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1", "weight": 1.0} -->

Formally, in this section, we assume that the discrete time dynamic $f$ can be further decomposed as the control *in* $k$ steps of some elementary discrete time dynamic $\phi$ as defined below. Concretely, $\phi$ may correspond to a single Euler discretization step of some continuous time dynamic. The discrete time dynamic $f$ amounts then to $k$ steps of such Euler discretization scheme and can be formulated as ${f{(x_{t},u_{t})}} = {\phi^{\{ k\}}{(x_{t},u_{t})}}$, for some $k \geq 0$. On the other hand, we consider the costs to be computed only at the scale of the dynamic $f$, i.e., the sampling of the costs and the sampling of the dynamics differ, hence the terminology multi-rate sampling.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

To analyze the convergence of the ILQR and the IDDP algorithms, we consider problem at the scale of the whole trajectory and analyze problem as a compositional problem of the form Note however that the dynamical structure of the problem revealed at the state scale is essential to the implementation of the ILQR and IDDP algorithms. We state our assumptions for convergence at the state scale and translate them at the trajectory scale. A table of all constants introduced for the convergence analysis with their respective units is provided in Appendix A for ease of reference.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 11", "weight": 1.0} -->

We consider convex costs $h_{t}$ that have $L_{h}$-Lipschitz-continuous gradients and $M_{h}$-Lipschitz-continuous Hessians for all $t \in {\{ 1,\ldots,\tau\}}$. We consider the dynamics to be Lipschitz-continuous with Lipschitz continuous Jacobians and satisfying.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 11", "weight": 1.0} -->

In consequence, the total cost $h$ defined in is convex, has $L_{h}$-Lipschitz-continuous gradients and $M_{h}$-Lipschitz-continuous Hessians. The function $g$ defined in is $l_{g}$-Lipschitz-continuous with $L_{g}$-Lipschitz-continuous Jacobians satisfying where $l_{g} = l_{f^{\lbrack\tau\rbrack}}$, $L_{g} = L_{f^{\lbrack\tau\rbrack}}$ are given in and $\sigma_{g} = \sigma_{f^{\lbrack\tau\rbrack}}$ is given.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The ILQR algorithm is a generalized Gauss-Newton algorithm", "weight": 1.0} -->

From a high-level perspective, the ILQR algorithm consists in linearizing the function $g:{{\mathbf{u}}\rightarrow{f^{\lbrack\tau\rbrack}{({\overline{x}}_{0},{\mathbf{u}})}}}$ that encapsulates the dynamics, taking a quadratic approximation of the costs $h$ around the current trajectory ${\mathbf{x}} = {g{({\mathbf{u}})}}$ and minimizing the resulting approximation with an additional regularization.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The ILQR algorithm is a generalized Gauss-Newton algorithm", "weight": 1.0} -->

Formally, as previously observed by Sideris and Bobrow; Roulet et al., the ILQR algorithm is then computing where $\ell_{g}^{\mathbf{u}}$ and $q_{h}^{g{({\mathbf{u}})}}$ are the linear and quadratic approximations of, respectively, the control in $\tau$ steps around $\mathbf{u}$ and the total costs around $g{({\mathbf{u}})}$ as defined in the notations. Equation 26 clearly reveals that the ILQR algorithm amounts to a regularized generalized Gauss-Newton algorithm implemented by a dynamic programming procedure exploiting the structure of the problem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 12", "weight": 1.0} -->

If the function $g$ is surjective and satisfies Assumption, then local quadratic convergence of e.g. a Gauss-Newton method or a Levenberg-Marquardt method (for $h$ quadratic) is known, see Björck, Bergou et al.. For $h$ non-quadratic, local quadratic convergence of generalized Gauss-Newton methods has also been shown in some special cases by Messerer et al.. Compared to these results, we consider deriving a convergence rate decomposed into a first slow convergence phase and a fast local convergence phase. Moreover, we consider quantitative bounds involving the constants in and additional assumptions (self-concordance or gradient dominant assumptions).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Global Convergence Rate to Global Minima", "weight": 1.0} -->

We start by analyzing the ILQR algorithm provided that the costs satisfy a sufficient condition for convergence to global minima, namely gradient dominance, a.k.a. a Polyak-Łojasiewicz inequality. We consider convergence in objective values $\mathcal{J}{({\mathbf{u}})}$ for problem, and analyze the number of iterations $k$ to reach an accuracy $\varepsilon$, that is, such that ${{\mathcal{J}{({\mathbf{u}}^{(k)})}} - {{\min_{{\mathbf{u}} \in {\mathbb{R}}^{\tau n_{u}}}\mathcal{J}}{({\mathbf{u}})}}} \leq \varepsilon$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 14", "weight": 1.0} -->

Consider the case $r = {1/2}$ in Theorem 13. The constants appearing in the bound are (i) the condition number $\rho_{h} = {L_{h}/\mu_{h}}$ of the total cost $h$, (ii) the condition number $\rho_{g} = {l_{g}/\sigma_{g}}$ of the Jacobian of $g$, ${\nabla g}{(\mathbf{u})}$, (iii) a constant $\theta_{h} = {M_{h}/{({2\mu_{h}^{3/2}})}}$ that can be interpreted as a bound on the self-concordance parameter of the cost $h$ if the total costs are strongly convex, (iv) a constant $\theta_{g} = {L_{g}/{({\sigma_{g}^{2}\sqrt{\mu_{h}}})}}$ whose dimension is the same as $\theta_{h}$,

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 14", "weight": 1.0} -->

i.e., the inverse of the squared root of the objective. Finally, the terms $\beta$ and $\alpha$ are additional dimension independent constants that act as additional condition numbers.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 15", "weight": 1.0} -->

The rate of convergence in Theorem 13 for $r = {1/2}$ is composed of $(i)$ a term $\rho_{h}{\ln\left( {\delta_{0}/\varepsilon} \right)}$ that is the linear complexity associated to the computation of ${\min_{\mathbf{x} \in {\mathbb{R}}^{\tau n_{u}}}h}{(\mathbf{x})}$ by a gradient descent on a function $h$ that has Lipschitz-continuous gradients with a gradient dominance property and (ii) a term $4\theta_{g}\sqrt{\delta_{0}}\gamma\left( {{\theta_{g}\sqrt{\delta_{0}}}/\alpha} \right)$ that depends on the initial gap and appropriate condition numbers on the problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 15", "weight": 1.0} -->

To understand the effect of this second term, consider computing the value of the gap $\delta_{j}$ after $j$ iterations such that the complexity of reducing the gap further by a factor ${1/e} \approx {1/2}$ is dominated by the logarithmic term such that we enter a linear phase of convergence. Formally, after $j$ iterations of the algorithm, the remaining number of iterations to reduce the gap further by a factor $1/e$, i.e., reach an accuracy $\varepsilon = {\delta_{j}/e}$, is ${4\theta_{g}\sqrt{\delta_{j}}\gamma\left( {{\theta_{g}\sqrt{\delta_{j}}}/\alpha} \right)} + {2\rho_{h}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 16", "weight": 1.0} -->

For $L_{g} = 0$, the terms depending on $\delta_{0}$ uniquely vanish since $\theta_{g} = 0$ in this case. We then get the classical rates when minimizing a function $h$ that satisfy with a first-order method. The rates can be improved by analyzing the local behavior of the algorithm to take advantage of the quadratic approximations of the total costs $h$ as shown in Section 4.2.2.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 16", "weight": 1.0} -->

If ${1/2} < r < 1$, by integrating $f_{2}$, the number of iterations to converge to an accuracy $\varepsilon$ is at most The bound follows in this case by using that, for ${1/2} < r < 1$, and $a > 0$,

<!-- chunk {"id": "body-0058", "role": "body", "section": "Local Convergence Rate to Minima", "weight": 1.0} -->

As we analyze the ILQR algorithm locally as an approximate Newton method on the costs, we use the notations and assumptions used to analyze a Newton method. Namely, we assume the costs $h_{t}$ to be strictly convex, and we define the norm induced by the Hessian at a point ${\mathbf{x}} \in {\mathbb{R}}^{\tau n_{x}}$ and its dual norm as, respectively, for ${\mathbf{y}} \in {\mathbb{R}}^{\tau n_{x}}$, For a matrix $A \in {\mathbb{R}}^{{{\tau n_{x}} \times \tau}n_{u}}$, we denote ${\| A\|}_{\mathbf{x}} = {\|{{\nabla^{2}h}{({\mathbf{x}})}^{1/2}A}\|}_{2}$ the norm induced by the local geometry of $h$ w.r.t.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Local Convergence Rate to Minima", "weight": 1.0} -->

the Euclidean norm. Finally, we denote the Newton decrement of the cost function, as, for ${\mathbf{x}} \in {\mathbb{R}}^{\tau n_{u}}$, To analyze the local convergence of the ILQR algorithm we consider the costs to be self-concordant. In addition, we consider smoothness properties of the function $g$ with respect to the geometry induced by the Hessian of the costs as presented in the assumptions below.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Assumption 17", "weight": 1.0} -->

In terms of the dynamic and the individual costs, Assumption 17 is satisfied if $h_{t}$ is strongly convex for all $t$ such that the total costs $h$ are strongly convex and if Assumption 11 is also satisfied. In that case, we have Given Assumption 17 and equipped with a stepsize proportional to the Newton decrement, we can show a local quadratic convergence rate of the ILQR algorithm.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 19", "weight": 1.0} -->

If $h$ is a quadratic, such that the algorithm reduces to a Gauss-Newton algorithm and $\vartheta_{h} = 0$, the radius of quadratic convergence reduces to ${\lambda = {1/{({{3\vartheta_{g}} + {2\overline{\nu}}})}}}.$ If in addition, no regularization is in effect, the radius of quadratic convergence reduces to $\lambda = {{1/3}\vartheta_{g}}$, which can be expressed as $1/{({3\theta_{g}\sqrt{\rho_{h}}})}$ if the total cost is $\mu_{h}$ strongly convex with $\theta_{g},\rho_{h}$ defined as in Theorem 13 and $\sigma,L$ expressed using. So up to 3$\sqrt{\rho_{h}}$, the parameter $1/\theta_{g}$ acts again as a radius of fast convergence as in Theorem 13.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 20", "weight": 1.0} -->

For better readability, we simplified the expression of the radius of convergence. A closer look at the proof shows that a non-zero regularization may lead to a larger radius of convergence than no regularization.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Local quadratic convergence rate", "weight": 1.0} -->

By combining (34 ‣ 4.2.2 Local Convergence Rate to Minima ‣ 4.2 Convergence Analysis of ILQR ‣ 4 Convergence Analysis ‣ On Global and Local Convergence of Iterative Linear Quadratic Optimization Algorithms for Discrete Time Nonlinear Control")) and (39 ‣ 4.2.2 Local Convergence Rate to Minima ‣ 4.2 Convergence Analysis of ILQR ‣ 4 Convergence Analysis ‣ On Global and Local Convergence of Iterative Linear Quadratic Optimization Algorithms for Discrete Time Nonlinear Control")) into, we get, as long as ${\lambda_{h}{({g{({\mathbf{u}})}})}} \leq {1/{\max{\{{\sqrt{2\vartheta_{h}\vartheta_{g}}c_{1}},{2\vartheta_{h}\varrho c_{2}},{2\vartheta_{h}c_{2}}\}}}}$, Note that ${c_{1},c_{2}} \leq 1$ and that

<!-- chunk {"id": "body-0064", "role": "body", "section": "Total Complexity", "weight": 1.0} -->

Given Assumption 11, if the total cost is strongly convex then it satisfies the condition of Theorem 13 and Assumption 17 is satisfied with the estimates given. We can then bound the number of iterations to local quadratic convergence and obtain the total complexity bound in this case. The following theorem is the detailed version of Theorem 1.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 22", "weight": 1.0} -->

The rate of convergence can now be separated between three phases, (i) the number of iterations to reach some linear convergence determined by the first term in the complexity bound, (ii) the number of iterations to reach the quadratic convergence rate that is captured by the logarithmic terms in the complexity bound, (iii) the quadratic convergence phase once $\delta_{k}$ is smaller than the gap of local quadratic convergence $\delta$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 22", "weight": 1.0} -->

Proof \Proof of Theorem By using the strong convexity of the costs $h$, we can refine the choice of the regularization to ensure. The validity of the proposed regularization to ensure condition is shown in Lemma 43 in Appendix F. With the proposed regularization, Lemma 44 in Appendix F shows, following the same reasoning as in the proof of Theorem 13, that the number of iterations of the ILQR algorithm needed to reach an accuracy $\varepsilon$ is bounded by with $\rho_{h}$, $\rho_{g}$, $\theta_{h}$, $\theta_{g}$, $\alpha$ defined as in Theorem 13.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 22", "weight": 1.0} -->

Once quadratic convergence is reached the remaining number of iterations is of the order of $O{({\ln{\ln\varepsilon^{- 1}}})}$. \Theorem 21 presents an ideal implementation of the ILQR algorithm given the knowledge of all constants to define the regularizations. This ideal implementation informs us on an appropriate line search strategy for the regularization, namely searching over $\overline{\nu}$ for regularizations of the form $\nu_{k} = {\overline{\nu}{\|{{\nabla h}{({g{({\mathbf{u}}^{(k)})}})}}\|}_{2}}$. We present in Algorithm 2 an implementation of the ILQR algorithm with an adequate line-search procedure that is guaranteed to terminate and maintain the complexity bounds presented in Theorem 21 as formally stated in Corollary 23, whose proof is given in Appendix F.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Convergence Analysis of IDDP", "weight": 1.0} -->

The IDDP algorithm departs from the implementation of usual optimization algorithms for compositional problems as it cannot be formulated as the minimization of an approximation of the objective but rather as an approximate minimization of the objective by dynamic programming, see e.g. Roulet et al. for a detailed overview. Its analysis can nevertheless be pursued by analogy of its implementation with the ILQR algorithm.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Convergence Analysis of IDDP", "weight": 1.0} -->

Namely, the technical Lemmas 46 and 49 in Appendix G decompose the implementation of the IDDP algorithm into the dynamical structure of the problem to quantify an approximation bound between the oracles returned by the ILQR and IDDP algorithm of the form ${\|{{{{DDP}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}} - {{{LQR}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}}}\|}_{2} \leq {\eta{\|{{{LQR}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}}\|}_{2}^{2}}$ for some constant $\eta$ independent of $\mathbf{u}$ and $\nu$, provided that the costs are strongly convex.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Convergence Analysis of IDDP", "weight": 1.0} -->

Equipped with this approximation bound, we consider selecting the regularization of the IDDP algorithm such that i.e., we use the same criterion as for the ILQR algorithm to ensure a sufficient decrease. This choice of regularization is motivated by the implementation of the ILQR and IDDP algorithms which both compute $\frac{1}{2}{\nabla\mathcal{J}}{({\mathbf{u}})}^{\top}{{LQR}_{\nu}{(\mathcal{J})}}{({\mathbf{u}})}$ by dynamic programming; see Roulet et al. for more details. For strongly convex costs, the rule provided in to select the stepsize together with the quadratic approximation bound between the oracles of the ILQR and IDDP algorithm enable us to state a global convergence result for the IDDP algorithm.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 25", "weight": 1.0} -->

The complexity bounds for the IDDP algorithm in Theorem 24 take then the same form as the complexity bounds obtained for the ILQR algorithm in Theorem 21 up to some additional multiplicative factors. Our proof is built on considering IDDP to approximate ILQR. In practice, IDDP appears more efficient than ILQR as illustrated in Figure 1 and other works and alternative proofs may better explain this phenomenon. On the other hand, our implementation and analysis provide theoretical convergence guarantees.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Evaluations", "weight": 1.0} -->

We illustrate numerically the theoretical findings to examine their relevance. In all experiments, we implemented gradient descent (GD), ILQR, IDDP, with a line-search on either the stepsize for GD or the scaled regularization for ILQR and IDDP as in Algorithm 2. The algorithms are run at double precision. They stop if (i) the norm of the gradient of the objective is smaller than $10^{- 16}$, (ii) the linesearch does not find a valid stepize bigger than $10^{- 24}$, (iii) the relative change in costs (${|{c_{k} - c_{k - 1}}|}/{|c_{k}|}$) is smaller than $10^{- 24}$. The code is publicly available at A tutorial notebook is available at

<!-- chunk {"id": "body-0073", "role": "body", "section": "Settings Considered", "weight": 1.0} -->

We consider two simple synthetic control environments: swinging up a pendulum, and controlling a simplified model of a car. Experiments on a more realistic model of a car are presented in Appendix I. In all experiments we consider only a cost on the state variables, i.e., ${h_{t}{(x_{t},u_{t})}} = {h_{t}{(x_{t})}}$. See Roulet et al. for additional experiments with costs on the control variables and other settings.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Swinging up pendulum", "weight": 1.0} -->

We consider swinging up a pendulum vertically through the control of a torque. The state $x = {(\theta,\omega)}$ consists in the angle $\theta$ with the vertical axis and the angular speed $\omega$ as illustrated in Fig 1. The dynamics in continuous time are where $m = 1$ is the mass of the blob, $l = 1$ is the length of the blob, $\mu = 0.01$ is a friction coefficient, $g = 10$ is the gravitational constant. The system is controlled through a torque, $u{(t)}$, applied to the pendulum. We use an Euler discretization scheme for the continuous dynamics with a discretization step $\Delta = {T/\tau}$ for a total time $T = 2$ and a number of discretization steps $\tau = 100$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Swinging up pendulum", "weight": 1.0} -->

For Figure 1, we consider a single cost on the last state. Namely, the objective is to swing up the pendulum to be vertical with for $x_{\tau} = {(\theta_{\tau},\omega_{\tau})}$. In other words, we target ${{\theta{(T)}} = \pi},{{\omega{(T)}} = 0}$ for some time horizon $T$, given ${\theta{}} = 0$, ${\omega{}} = 0$. In some experiments below, we consider variations of the costs, such as considering a cost for each time step or a subsampled cost.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Simple model of a car with tracking costs", "weight": 1.0} -->

We consider a simple model of the car, illustrated in Figure 1. The state consists in $x = {(z_{x},z_{y},\theta,v)}$, where $z = {(z_{x},z_{y})}$ is the position of the car, $\theta$ is the angle between the orientation of the car and the horizontal axis, a.k.a., the yaw, and $v$ is the longitudinal speed. The controls $u = {(a,\delta)}$ consist of the longitudinal acceleration $a$ of the car, and the steering angle $\delta$. For a car of length $l = 1$, the continuous time dynamics of this simplified model of the car are We use a Runge-Kutta method of order 4, a discretization step $\Delta = {T/\tau}$ for a total time $T = 2$, and a number of discretization steps $\tau = 25$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Simple model of a car with tracking costs", "weight": 1.0} -->

The objective consists in minimizing the distance between the position of the car and a reference position on a track. We define a reference track $z^{\ast}{(t)}$ as a continuous spline using a simple track presented by Roulet et al.. The discrete time reference positions are defined as $z_{t}^{\ast} = {z^{\ast}{({\Delta t})}}$. The costs consist then For Figure 1, we consider a subsampled cost equivalent to consider a multistep discretization strategy detailed in Section 3.2. Namely, we subsample the cost every $k = 3$ steps such that the costs are then with $\Delta = {T/{({k\tau})}}$. Below, we consider also costs on every time-step, i.e., $k = 1$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Costs along iterations for the pendulum", "weight": 1.0} -->

For a single final cost, the problem of swinging up the pendulum is equivalent to minimizing the composition of a strongly convex cost with the control in $\tau$ steps of the discrete dynamics of the pendulum. With an Euler discretization of the continuous dynamics of the pendulum, one easily observes that the control in any $k \geq 2$ steps of the discrete dynamics has surjective linearizations as outlined in Section 3. Hence, with a single final quadratic cost, this problem falls under the assumptions of Section 4. The convergence of both ILQR and IDDP algorithms towards a global minimum cost, namely a null cost, is observed in Figure 1.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Costs along iterations for the pendulum", "weight": 1.0} -->

In Figure 4, we consider a cost every $k$ steps, that is for $k \in {\{ 1,2\}}$. We also consider $10$ random initial sequence of control variables, i.e., $u_{t}^{} \sim {\mathcal{N}{(0,\sigma)}}$, for $\sigma = {1/\Delta} = 100$, $t \in {\{ 0,\ldots,{\tau - 1}\}}$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Costs along iterations for the pendulum", "weight": 1.0} -->

By taking $k = 2$, we observe that ILQR and IDDP both converge to a $0$ cost, hence a global minimum, across random initializations. As mentioned above, by taking $k > 1$ convergence to a global minimal cost is predicted by the theory in Section 3 and 4.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Costs along iterations for the pendulum", "weight": 1.0} -->

For $k = 1$, none algorithm converges to 0. However, this does not mean that they do not converge to a global minimum. In fact, one observes that across random initializations, both ILQR and IDDP converge to the same cost. Namely, the standard deviation of the minimum cost computed by these algorithms across random initializations is $10^{- 14}$. This suggests a global convergence behavior to a same minimum. While the theory developed in Section 3 and 4 explains the behavior for $k = 2$, the results for $k = 1$ suggest that convergence to a global minimum may be ensured beyond the sufficient condition. Note that global convergence of ILQR and IDDP to, e.g., stationary points, can be verified on generic problems (Section 2). Such global convergence properties are not sufficient to ensure convergence to global minima. Convergence to global minima require additional properties of the problem itself.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Costs along iteration for the simple model of a car", "weight": 1.0} -->

In Figure 1, we considered a subsampled cost, such that a sufficient condition for convergence to global minima outlined in Section 3.2 may be satisfied. We observe in Figure 1 convergence to a global minimal cost, namely a null cost, for both ILQR and IDDP algorithms.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Costs along iteration for the simple model of a car", "weight": 1.0} -->

In Figure 5, we consider a cost at each time step (no subsampling of the costs, i.e., $k = 1$ in ) with $10$ random initial control sequences, i.e., $u_{t}^{} \sim {\mathcal{N}{(0,\sigma)}}$ for $\sigma = {2/\Delta} = 25$, $t \in {\{ 0,\ldots,{\tau - 1}\}}$. We also repeat the experiment with costs subsampled every $3$ time steps with the same random initializations schemes.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Costs along iteration for the simple model of a car", "weight": 1.0} -->

For subsampled costs, i.e., $k = 3$, we observe convergence to global minimal costs (null costs) for both IDDP and ILQR algorithms across random initializations.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Costs along iteration for the simple model of a car", "weight": 1.0} -->

For non-subsampled costs, i.e., $k = 1$, the costs do not converge to 0. Contrarily to the pendulum case, we observed a discrepancy in the minimal cost reached after $2000$ iterations. ILQR and IDDP reach, on average across initializations, costs of, respectively, $4.61 \cdot 10^{- 2}$ and $5.68 \cdot 10^{- 2}$ with standard deviations across initializations of, respectively, $3.93 \cdot 10^{- 2}$ and $3.75 \cdot 10^{- 2}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Costs along iteration for the simple model of a car", "weight": 1.0} -->

Finally, IDDP converges faster than ILQR in all pendulum examples and in the example of the car with subsampled costs. A similar observation was also made by Liao and Shoemaker and in the companion paper.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Instantaneous rate of convergence", "weight": 1.0} -->

The theoretical findings of Section 4 outline a priori three phases of convergence, sublinear, linear and quadratic. Convergence rates of ILQR and IDDP can be assessed through convergence rates in function values $\rho^{(k)} = {{({c^{({k + 1})} - c^{\ast}})}/{({c^{(k)} - c^{\ast}})}}$ for $c^{\ast}$ the minimal cost as done in Appendix I, or by considering convergence in iterates through $\kappa^{(k)} = {{\|{{\mathbf{u}}^{({k + 1})} - {\mathbf{u}}^{(k)}}\|}_{2}/{\|{{\mathbf{u}}^{(k)} - {\mathbf{u}}^{({k - 1})}}\|}_{2}}$ as done in Figure 6.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Instantaneous rate of convergence", "weight": 1.0} -->

For the simple model of a car, in Figure 6, we observe that the convergence rate in iterations of these algorithms remain close to $1$ for many iterations (the x-axis in Figure 6 is in reverted log-scale). This rate suddenly drops close to convergence akin to a local quadratic local convergence. This shows that the main difficulty of the problem arises for a long first phase of slow convergence.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Surjectivity of the Jacobian", "weight": 1.0} -->

The sufficient condition for convergence to global minima can be assessed by computing the minimal singular value $\sigma_{\min}{({{\nabla f^{\lbrack\tau\rbrack}}{({\mathbf{u}}^{(k)})}})}$ of the transpose Jacobian of the control of $\tau$ steps of the discrete dynamics. In Figure 7, we plot this minimal singular value along the iterations of the ILQR and IDDP algorithms. We consider discrete dynamics defined as the control in $k = 2$ and $k = 3$ steps of the discretization of the continuous dynamics of, respectively, the pendulum and the simple model of a car. Considering discrete dynamics in multiple steps amount to the subsampling of the costs presented in previous experiments.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Surjectivity of the Jacobian", "weight": 1.0} -->

We observe in Figure 7 that $\sigma_{\min}{({{\nabla f^{\lbrack\tau\rbrack}}{({\mathbf{u}}^{(k)})}})}$ is small yet bounded away from $0$ along the iterations. This result concurs with the convergence to global minimal costs of these algorithms observed in the right panels of Figure 4 and Figure 5.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Nonlinear control approaches", "weight": 1.0} -->

Nonlinear control problems of the form stem from the discretization of generic optimal control problems in continuous time of the form Continuous optimal control problems of the form can be tackled in various ways. One can approach the problem from a *dynamic programming* perspective to derive the Hamilton-Jacobi-Bellman equation, a partial differential equation in state space. Alternatively, one can derive necessary optimality conditions for to derive a boundary value problem. Such a method is referred to as an *indirect method* and amounts to an "optimize then discretize" approach. Finally, problem can be tackled by *direct methods* that consider finite dimensional approximations of the original infinite dimensional problem. Direct methods amount to a "discretize then optimize" approach, they can further be split into different approaches. First, one may consider a finite representation of the continuous control $u{(t)}$ as piecewise constant functions whose values $q_{1},\ldots,q_{\tau}$ at each piece define the finite number of degrees of freedom.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Nonlinear control approaches", "weight": 1.0} -->

The problem still involves an ODE in the state variable, ${\overset{˙}{x}{(t)}} = {f{({x{(t)}},{u_{q_{1:\tau}}{(t)}})}}$, albeit a simpler one. Tackling the problem with such a partial discretization is referred to as a *single shooting* method. *Collocation methods* consider discretizing both the states and controls, leading to a formulation like, that can benefit from advanced numerical integration methods. Finally, *multiple shooting* combines both approaches. The system is split in multiple windows and for each window a single shooting method is used. We focus solely on the resulting discrete time nonlinear control problems and refer the interested reader to, e.g., Rawlings et al. for an overview of the approaches mentioned above.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Nonlinear control with local approximations and iterative refinements", "weight": 1.0} -->

One of the first approaches for nonlinear discrete time control problems appear to be the Differential Dynamic Programming (DDP) methods developed by Mayne; Jacobson and Mayne; Mayne and Polak. Its principle is to apply a dynamic programming procedure to the nonlinear system. The associated Bellman equation is approximately solved by considering its quadratic approximation around the current trajectory. A set of policies is computed along this process and applied to the original dynamics as if the true solutions of the Bellman equations were found. A modern account is provided in the companion paper for reference; see also Liao and Shoemaker. Numerous variants of DDP have been developed to account for constraints or noise in the dynamics. Among those, IDDP, a.k.a. iLQR, can be seen to follow the same principle as DDP except that *linear-quadratic* approximations à la Gauss-Newton are used in place of the quadratic approximations of the Bellman equation akin to Newton's method.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Nonlinear control with local approximations and iterative refinements", "weight": 1.0} -->

DDP approaches differ from the implementation of classical optimization algorithms such as a Newton, quasi-Newton or Gauss-Newton method for discrete nonlinear control problems. Bock; Bock and Plitt first presented such approaches referred to as *direct multiple shooting*. Detailed and efficient implementations of Newton's method exploiting the dynamical structure of the problem were presented by Pantoja; Dunn and Bertsekas. A linear algebraic viewpoint on these implementations was presented by Wright, that enabled the use of fast linear solvers exploiting the structure of nonlinear control problems. In particular, Wright presents alternative resolutions of the linear quadratic subproblem using a "Riccati-like" recursion that slightly differs from the resolution by dynamic programming presented here. Wright further developed parallel implementations of algorithms solving the LQR problems. We do not delve into the specific implementations of the oracles used in ILQR or IDDP and rather focus on the global behavior of the algorithms.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Nonlinear control with local approximations and iterative refinements", "weight": 1.0} -->

This viewpoint was further generalized to handle nonlinear inequalities in model predictive control or even generic graphs of computations. The ILQR algorithm can be seen as an instance of direct multiple shooting, namely, an instance of a generalized Gauss-Newton method which uses *linear-quadratic* approximations of the problem decomposed along the dynamics.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Nonlinear control with local approximations and iterative refinements", "weight": 1.0} -->

Detailed implementations of the DDP (quadratic approximation of Bellman equation), the IDDP (linear-quadratic approximation of Bellman equation), Newton (quadratic approximation of the objective) and the ILQR (linear-quadratic approximation of the objective) approaches are presented in the companion paper to highlight their common points and differences.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Nonlinear control with local approximations and iterative refinements", "weight": 1.0} -->

The decomposition of the problem at several scales by means of some quadratic approximations have also been developed and studied by Messerer et al.; Frasch et al.; Verschueren et al.; Houska and Diehl.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Convergence analysis of Gauss-Newton methods", "weight": 1.0} -->

Regularized Gauss-Newton methods, a.k.a. Levenberg-Marquardt methods, have been extensively studied. Global convergence to stationary points at a polynomial rate is established, e.g., Bergou et al.. The results may be extended, provided that the non-linear mappings have surjective Jacobians. Our approach improves on previous results with polynomial rates and our complexity bounds provide explicit dependencies on the initial gap and the region of quadratic convergence. We also depart from previous results using error bounds, such as the ones of Bergou et al. and Yamashita and Fukushima (2001, Eq. (1.6)), in that our assumption on surjective Jacobians is stronger than an error bound.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Convergence analysis of Gauss-Newton methods", "weight": 1.0} -->

Closer to our approach is the work of Nesterov where the assumption of surjective Jacobians is used to provide global convergence guarantees of a *modified* Gauss-Newton method also known as the prox-linear method for nonlinear fitting. Nesterov argues in favor of least un-squared norms methods, as opposed to least squared norms methods, by reasoning in terms of condition numbers irrespective of local subroutine computational complexity. In contrast, we consider twice differentiable costs, for which we build a quadratic model, leading to *generalized* Gauss-Newton methods. In nonlinear control, generalized Gauss-Newton oracles can be implemented efficiently by exploiting the dynamical structure of the problem, while modified Gauss-Newton method oracles may require a computationally expensive line-search. Messerer et al. considered also convergence of generalized Gauss-Newton methods. However, Messerer et al. analyzes such algorithms without regularization, nor linesearch or trust-region techniques, resulting in possibly divergent algorithms or only local convergence guarantees. By adding a regularization scheme, we are able to ensure global convergence, and to provide practical guidance on the choice of regularization (Algorithm 2).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Convergence analysis of Gauss-Newton methods", "weight": 1.0} -->

Baumgärtner et al. also considered the local convergence properties of ILQR, IDDP to determine that they share the same linear convergence rate locally. We consider more general convergence properties towards stationary points, or global minima given additional assumptions. Finally, our results are quantitative, relating the region of quadratic convergence to the smallest singular value of the transposed Jacobian.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Convergence analysis of Gauss-Newton methods", "weight": 1.0} -->

As mentioned earlier, a Newton's method could just as well be implemented to exploit the dynamical structure of the problem. Several caveats lend still in favor of a Gauss-Newton method. First, a Newton's method (or a DDP approach) requires computing and storing the second order information associated to the dynamics at the intermediate states, although the storage issue can be mitigated by an adequate implementation in a differentiable programming framework. Second, Newton's method does not compute a priori descent directions if the Hessian is not positive definite. Hessian modifications may be necessary to ensure a descent direction such that a linesearch can be used. On the other hand, for generic functions, Newton's method is known to converge locally at a quadratic rate, which is a priori not true for a generalized Gauss-Newton method. Our analysis shows that in some nonlinear control problems generalized Gauss-Newton methods can converge with such a local quadratic rate, just as observed empirically.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Convergence analysis of Gauss-Newton methods", "weight": 1.0} -->

Our analysis stems in fact from considering a generalized Gauss-Newton method as an approximate Newton method in the space of the trajectories which enable us to recover the fast local rate of convergence of Newton's method by appropriately controlling the approximation error.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Convergence analysis of differentiable dynamic programming methods", "weight": 1.0} -->

Previous work mainly focused on local convergence guarantees or convergence guarantees towards controls satisfying first-order necessary optimality conditions. The local quadratic convergence analysis of DDP is based on viewing DDP as an approximate Newton method. An alternative proof of local quadratic convergence and an approach based on the method of strong variations are also worth mentioning. Previous work considers additional costs on the control variables and assumes that the Hessian of the overall objective is invertible; see or. In contrast to previous work, we do not consider additional costs on the control variable, and we consider the IDDP algorithm which uses linear-quadratic approximations developed by Tassa et al. and extended by Giftthaler et al.. The IDDP algorithm benefits from a smaller per-iteration cost compared to DDP, as IDDP does not require computing intermediate second-order information associated to the dynamics.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Sufficient conditions for convergence to global minima", "weight": 1.0} -->

Discrete time nonlinear control problems of the form stem from the time discretization of continuous time problems. Necessary optimality conditions for the continuous time control problems are characterized by Pontryagin's maximum principle. However, these optimality conditions cannot be used for the discretized problems since Pontryagin variations in finite dimensional space do not exist. Necessary optimality conditions can be derived from the Karush-Kuhn-Tucker conditions for problem, which are equivalent to first order optimality conditions of the objective in terms of control variables. Sufficient optimality conditions for the continuous time nonlinear control problem were also derived by Mangasarian; Arrow; Kamien and Schwartz. We translate these conditions for the discrete time nonlinear control problem in Appendix B. Unfortunately, such conditions require convexity assumptions of implicitly defined functions that seem difficult to verify in practice. We argue in Section 3.2 that our assumption can be verified on simple instances.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Sufficient conditions for convergence to global minima", "weight": 1.0} -->

Our assumption is based on analyzing the gradient dominating property of the objective of problem in terms of the properties of the dynamic. The gradient dominating property was introduced by Polyak; Łojasiewicz as a sufficient condition to ensure convergence of gradient descent to global minima. Here, we exploit this property to ensure global and local quadratic convergence to global minima of a regularized generalized Gauss-Newton algorithm. From a nonlinear control viewpoint, our assumption translates as the controllability of the discrete linearized trajectories in one step. In a similar spirit, a controllability assumption on the discrete linearized trajectories in *several* steps was considered to analyze the local convergence of MPC controllers by Na and Anitescu following Xu and Anitescu. Compared to Xu and Anitescu; Na and Anitescu, we consider *global* convergence results to minimizers, which justifies a stronger assumption.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Sufficient conditions for convergence to global minima", "weight": 1.0} -->

In addition, compared to Xu and Anitescu; Na and Anitescu, we formally relate our condition to feedback linearization schemes well understood in continuous time and further developed in discrete time by Jakubczyk and Sontag; Jakubczyk; Jayaraman and Chizeck; Aranda-Bricaire et al.; Belikov et al.. In particular, we exploit the existence of a feedback linearization scheme by considering a multi-rate sampling scheme to ensure our sufficient condition. Using multi-rate sampling was proposed in the early work of Grizzle and Kokotovic on discrete time feedback linearization schemes.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Sufficient conditions for convergence to global minima", "weight": 1.0} -->

We consider only understanding the performance of two popular algorithms, ILQR and IDDP. Several variants can be considered. In particular, given the surjectivity of the Jacobian of the dynamics, the problem may also be rephrased as a feasibility problem and tackled differently. Namely, the minimizers $x_{t}^{\ast}$ of the costs $h_{t}$ could be computed offline, and the problem would reduce to fit a nonlinear model of the states, here described by the trajectories given by the dynamics, to the minimizers $x_{t}^{\ast}$. Such feasibility problems may be tackled for example by penalty method as done by Kim and Wright. However, such penalty methods may dismiss the dynamical structure of the problem. Moreover, ILQR or IDDP methods can tackle the original problem at once, rather than deriving a two-stage method consisting in computing first the minimizers of the costs.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have detailed computational complexities of the ILQR and IDDP algorithms for discrete time nonlinear control problems. Our analysis decomposes at several scales. At the scale of the whole trajectory, the problem can be summarized as a compositional objective and analyzed as a Gauss-Newton type algorithm. The trajectories can be detailed at the scale of the dynamic, which reveals the low computational cost of the optimization oracles. Finally, the dynamics can further be detailed in terms of the discretization scheme in order to ensure sufficient conditions for convergence of the algorithms towards global optima.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The sufficient conditions for global convergence are restricted to problems without costs or constraints on the control variables. Moreover, they may not be applicable in usual scenarios with costs that are not subsampled. As future work, one may analyze constraints on the control variables while ensuring a gradient dominating-like property on the objective. Analyzing further the links between feedback linearization schemes and sufficient conditions for global optimality may also reveal the impact of the discretization stepsize on the overall condition number of the problem.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgments and Disclosure of Funding This work was supported by NSF DMS-1839371, DMS-2134012, CCF-2019844, CIFAR-LMB, NSF TRIPODS II DMS-2023166 and faculty research awards. This work was done when Vincent Roulet was at the University of Washington, minor revisions where done when he was at Google. The authors thank Dmitriy Drusvyatskiy, Alexander Liniger, Krishna Pillutla and John Thickstun for fruitful discussions on the paper and their help to develop the numerical experiments. The authors are sincerely grateful to the action editor and the reviewers for their thorough work and the numerous comments that helped us improve on the original manuscript.
