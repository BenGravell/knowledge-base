<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Iterative Linearized Control: Stable Algorithms and Complexity Guarantees

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We examine popular gradient-based algorithms for nonlinear control in the light of the modern complexity analysis of first-order optimization algorithms. The examination reveals that the complexity bounds can be clearly stated in terms of calls to a computational oracle related to dynamic programming and implementable by gradient back-propagation using machine learning software libraries such as PyTorch or TensorFlow. Finally, we propose a regularized Gauss-Newton algorithm enjoying worst-case complexity bounds and improved convergence behavior in practice. The software library based on PyTorch is publicly available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite horizon discrete time nonlinear control has been studied for decades, with applications ranging from spacecraft dynamics to robot learning. Popular nonlinear control algorithms, such as differential dynamic programming or iterative linear quadratic Gaussian algorithms, are commonly derived using a linearization argument relating the nonlinear control problem to a linear control problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We examine nonlinear control algorithms based on iterative linearization techniques through the lens of the modern complexity analysis of first-order optimization algorithms. We first reformulate the problem as the minimization of an objective that is written as a composition of functions. Owing to this reformulation, we can frame several popular nonlinear control algorithms as first-order optimization algorithms applied to this objective.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We highlight the equivalence of dynamic programming and gradient back-propagation in this framework and underline the central role of the corresponding automatic differentiation oracle in the complexity analysis in terms of convergence to a stationary point of the objective. We show that the number of calls to this automatic differentiation oracle is the relevant complexity measure given the outreach of machine learning software libraries such as PyTorch or TensorFlow.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Along the way we propose several improvements to the iterative linear quadratic regulator (ILQR) algorithm, resulting in an accelerated regularized Gauss-Newton algorithm enjoying a complexity bound in terms of convergence to a stationary point and displaying stable convergence behavior in practice. Regularized Gauss-Newton algorithms give a template for the design of algorithms based on partial linearization with guaranteed convergence. The proposed accelerated regularized Gauss-Newton algorithm is based on a Gauss-Newton linearization step stabilized by a proximal regularization and boosted by a Catalyst extrapolation scheme, potentially accelerating convergence while preserving the worst-case guarantee.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Discrete time control", "weight": 1.0} -->

We first present the framework of finite horizon discrete time nonlinear control.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Exact dynamics", "weight": 1.0} -->

Optimality is measured through convex costs $h_{t}$, $g_{t}$, on the state and control variables $x_{t}$, $u_{t}$ respectively, defining the discrete time nonlinear control problem where, here and thereafter, the dynamics must be satisfied for $t = {0,\ldots,{\tau - 1}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Costs and penalties", "weight": 1.0} -->

The costs on the trajectory can be used to force the states to follow a given orbit ${\hat{x}}_{1},\ldots,{\hat{x}}_{\tau}$ as which gives a quadratic tracking problem, while the regularization penalties on the control variables are typically quadratic functions The regularization penalties can also encode constraints on the control variable such as the indicator function of a box where $\iota_{S}$ denotes the indicator function of a set $S$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Iterative Linear Control algorithms", "weight": 1.0} -->

We are interested in the complexity analysis of algorithms such as the iterative linear quadratic regulator (ILQR) algorithm as defined, used for exact dynamics, which iteratively computes the solution of where ${\overline{u}}^{(k)}$ is the current command, ${\overline{x}}^{(k)}$ is the corresponding trajectory given, $q_{h_{t}},q_{g_{t}}$ are quadratic approximations of the costs $h_{t},g_{t}$ around respectively $x_{t}^{(k)},u_{t}^{(k)}$ and $\ell_{\phi_{t}}$ is the linearization of $\phi_{t}$ around $(x_{t}^{(k)},u_{t}^{(k)})$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Iterative Linear Control algorithms", "weight": 1.0} -->

The next iterate is then given by ${\overline{u}}^{({k + 1})} = {{\overline{u}}^{(k)} + {\alpha{\overline{v}}^{\ast}}}$ where ${\overline{v}}^{\ast}$ is the solution of and $\alpha$ is a step-size given by a line-search method. To understand this approach, we frame the problem as the minimization of a composition of functions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Iterative Linear Control algorithms", "weight": 1.0} -->

Note that the term ILQR or ILQG has then been used to refer to a variant of the above algorithm that uses the feedback gains computed in the resolution of the linear control problem to control to move along the true trajectory, see.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Formulation as a composite optimization problem", "weight": 1.0} -->

We call an optimization problem a *composite optimization problem* if it consists in the minimization of a composition of functions. For a fixed command $\overline{u} \in {\mathbb{R}}^{\taup}$, denote by ${\overset{\sim}{x}{(\overline{u})}} = {({{\overset{\sim}{x}}_{1}{(\overline{u})}};\ldots;{{\overset{\sim}{x}}_{\tau}{(\overline{u})}})} \in {\mathbb{R}}^{\taud}$ the trajectory given by the exact dynamics, which reads Similarly denote by ${\overset{\sim}{x}{(\overline{u},\overline{w})}} \in {\mathbb{R}}^{\taud}$ the trajectory in the noisy case.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Formulation as a composite optimization problem", "weight": 1.0} -->

Denoting the total cost by ${h{(\overline{x})}} = {\sum_{t = 1}^{\tau}{h_{t}{(x_{t})}}}$, the total penalty by ${g{(\overline{u})}} = {\sum_{t = 0}^{\tau - 1}{g_{t}{(u_{t})}}}$, the control problem with exact dynamics reads and with noisy dynamics, i.e., we obtain a composite optimization problem whose structure can be exploited to derive oracles on the objective.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Oracles in discrete time control", "weight": 1.0} -->

We adopt here the viewpoint of the complexity theory of first-order optimization. Given the composite problem, what are the relevant oracles and what are the complexities of calls to these oracles? We first consider exact dynamics $\phi_{t}$ of the form and unconstrained cost penalties such as.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model minimization", "weight": 1.0} -->

Each step of the optimization algorithm is defined by the minimization of a regularized model of the objective. For example, a *gradient step* on a point $\overline{u}$ with step-size $\gamma$ corresponds to linearizing both $h$ and $\overset{\sim}{x}$ and defining the linear model of the objective $f$, where ${\ell_{h}{({\overline{x} + \overline{y}};\overline{x})}} = {{h{(\overline{x})}} + {{\nabla h}{(\overline{x})}^{\top}\overline{y}}}$ and $\ell_{g}{({\overline{u} + \overline{v}};\overline{u})}$ is defined similarly. Then, this model with a proximal regularization is minimized in order to get the next iterate Different models can be defined to better approximate the objective.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model minimization", "weight": 1.0} -->

For example, if only the mapping $\overset{\sim}{x}$ is linearized, this corresponds to defining the convex model at a point $\overline{u}$ We get then a *regularized Gauss-Newton step* on a point $\overline{u} \in {\mathbb{R}}^{\taup}$ with step size $\gamma > 0$ as Although this model better approximates the objective, its minimization may be computationally expensive for general functions $h$ and $g$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model minimization", "weight": 1.0} -->

A *Levenberg-Marquardt step* with step-size $\gamma$ consists in minimizing the model with a proximal regularization

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model-minimization steps by linear optimal control", "weight": 1.0} -->

Though the chain rule gives an analytic form of the gradient, we can use the definition of a gradient step as an optimization sub-problem to understand its implementation. Formally, the above steps define a model $m_{f}$ of the objective $f$ in on a point $\overline{u}$, as where $m_{h} = {\sum_{t = 1}^{\tau}m_{h_{t}}}$, $m_{g} = {\sum_{t = 0}^{\tau - 1}m_{g_{t}}}$ are models of $h$ and $g$ respectively, composed of models on the individual variables. The model-minimization step with step-size $\gamma$, amounts then to a linear control problem as shown in the following proposition.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

If the models used in are linear or quadratic, the resulting linear control problems can be solved efficiently using dynamic programming, i.e., with a linear cost in $\tau$, as presented in the following proposition. The cost is $\mathcal{O}{({\taup^{3}d^{3}})}$. Details on the implementation for quadratic costs are provided in Appendix B.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

Since the leading dimension of the discrete time control problem is the length of the trajectory $\tau$, all of the above optimization steps have roughly the same cost. This means that, in discrete time control problems, *second order steps such as are roughly as expensive as gradient steps*.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gradient back-propagation as dynamic programming", "weight": 1.0} -->

We illustrate the derivations for a gradient step in the following proposition that shows a cost of $\mathcal{O}{({\tau{({{pd} + d^{2}})}})}$. We recover the well-known gradient back-propagation algorithm used to compute the gradient of the objective. The dynamic programming viewpoint provides here a natural derivation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Noisy dynamics", "weight": 1.0} -->

The model we consider for the state cost is then of the form For simple dynamics $\phi_{t}$, their minimization with an additional proximal term amounts to a linear quadratic Gaussian control problem as stated in the following proposition.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dealing with constraints", "weight": 1.0} -->

For constrained control problems with exact dynamics, the model-minimization steps will amount to linear control problems under constraints, which cannot be solved directly by dynamic programming. However their resolution by an interior point method boils down to solving linear quadratic control problems each of which has a low computational cost as shown before.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dealing with constraints", "weight": 1.0} -->

Formally, the resulting subproblems we are interested in are linear quadratic control problems under constraints of the form where $\mathcal{U}_{t} = {\{ u:{{C_{t}u} \leq d_{t}}\}}$, $q_{h_{t}}$ are convex quadratics, $q_{g_{t}}$ are strongly convex quadratics and $\ell_{t}$ are linear dynamics. Interior point methods introduce a log-barrier function ${\mathcal{B}_{t}{(u)}} = {\log{({d_{t} - {C_{t}u}})}}$ and minimize where $\mu_{k}$ increases along the iterates $k$ of the interior point method. We leave the exploration of constrained problems to future work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Automatic-differentiation oracle", "weight": 1.0} -->

The iterative composition structure we studied so far appears not only in control but more generally in optimization problems that involve successive transformations of a given input as for example in The identification of such structures led to the development of efficient *automatic-differentiation* software libraries able to compute gradients in any graph of computations both in CPUs and GPUs. We present then implementations and complexities of the optimization methods presented before where automatic-differentiation is the computational bottleneck.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Functions and problem definition", "weight": 1.0} -->

We first recall the definition of decomposable functions along the trajectories.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model-minimization steps with automatic-differentiation oracles", "weight": 1.0} -->

Now we precise the feasibility and the complexity of the inner-steps of the steps defined in Section 2 in terms of the class of problems and the automatic-differentiation oracle defined above. The total complexity of the algorithms, when available, are presented in Section 4.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Regularized Gauss-Newton step", "weight": 1.0} -->

In the setting, the regularized Gauss-Newton step amounts to solve For smooth objectives $h$ and $g$, this is a smooth strongly convex problem that can be solved approximately by a linearly convergent first order method, leading to the inexact regularized Gauss-Newton procedures described. The overall cost of an approximated regularized Gauss-Newton step is then given by the following proposition.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Levenberg-Marquardt step", "weight": 1.0} -->

In the setting, the Levenberg-Marquardt step amounts to solve where $q_{h}$ and $q_{g}$ are quadratic approximations of $h$ and $g$ respectively, both being assumed to be twice differentiable. Here, duality offers a fast resolution of the step as shown in the following proposition. It shows that its cost is only ${2d} + 1$ times more than one of a gradient step. Recall also that for $h$, $g$ quadratics the Levenberg-Marquardt step amounts to a regularized Gauss-Newton step.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Composite optimization", "weight": 1.0} -->

Before analyzing the methods of choice for composite optimization, we review classical algorithms for nonlinear control and highlight improvements for better convergence behavior. All algorithms are completely detailed in Appendix C.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

Differential Dynamic Programming (DDP) is presented as a dynamic programming procedure applied to a second order approximation of the Bellman equation. Formally at a given command $\overline{u}$ with associated trajectory $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$, it consists in approximating the cost-to-go functions as where for a function $f{(y)}$, $q_{f}{(y;x)}$ denotes its second order approximation around $x$. The roll-out pass is then performed on the true trajectory as normally done in a dynamic programming procedure. We present an interpretation of DDP as an optimization on the state variables in Appendix D.

<!-- chunk {"id": "body-0033", "role": "body", "section": "ILQR, ILQG", "weight": 1.0} -->

DDP was superseded by the Iterative Linearized Quadratic Regulator (ILQR) method, presented in Section 1. In the case of noisy dynamics, the Linear Quadratic Regulator problem was replaced by a Linear Quadratic Gaussian problem where the objectives are averaged with respect to the noise, the iterative procedure was then called ILQG as presented.

<!-- chunk {"id": "body-0034", "role": "body", "section": "ILQR, ILQG", "weight": 1.0} -->

Prop. 2.1 clarifies that these procedures, as defined, amount to compute to perform a line-search along its direction such that ${f{({\overline{u} + {\alpha{\overline{v}}^{\ast}}})}} \leq {f{(\overline{u})}}$. For ILQR the model $q_{f}$ is defined as, while for ILQG this corresponds to the model defined in with quadratic models $q_{f}$ and $q_{g}$. Compared to a Levenberg-Marquardt step, that reads we see that those procedures do not take into account the inaccuracy of the model far from the current point. Although a line-search can help ensuring convergence, no rate of convergence is known. For quadratics $h_{t},g_{t}$, the Levenberg-Marquardt steps become regularized Gauss-Newton steps whose analysis shows the benefits of the regularization term in (35.

<!-- chunk {"id": "body-0035", "role": "body", "section": "ILQR, ILQG", "weight": 1.0} -->

‣ 4.1 Optimal control methods ‣ 4 Composite optimization ‣ Iterative Linearized Control: Stable Algorithms and Complexity Guarantees")) to ensure convergence to a stationary point.

<!-- chunk {"id": "body-0036", "role": "body", "section": "ILQG", "weight": 1.0} -->

The term ILQG has often been used to refer to an algorithm combining ideas from DDP and ILQR resp.. The general structure proposed then is akin to DDP in the sense that it uses a dynamic programming approach where the cost-to-go functions are approximated. However, as in ILQR, only the first order derivatives of the dynamics are taken into account to approximate the cost-to-go functions. Formally, at a given command $\overline{u}$ with associated trajectory $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$, ILQG consists in approximating the cost-to-go functions as While the cost-to-go functions are the same as, the roll-out pass is then performed on the true trajectory and not the linearized one. The analysis is therefore similar to the one of DDP. We leave it for future work and focus on the original definition of ILQR given.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regularized ILQR via regularized Gauss-Newton", "weight": 1.0} -->

We present convergence guarantees of the regularized Gauss-Newton method for composite optimization problems of the form where $h:{{\mathbb{R}}^{\taud}\rightarrow{\mathbb{R}}}$ and $g:{{\mathbb{R}}^{\taup}\rightarrow{\mathbb{R}}}$ are convex quadratic, and $\overset{\sim}{x}:{{\mathbb{R}}^{\taup}\rightarrow{\mathbb{R}}^{\taud}}$ is differentiable with continuous gradients. The regularized Gauss-Newton method then naturally leads to a regularized ILQR.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regularized ILQR via regularized Gauss-Newton", "weight": 1.0} -->

The regularized Gauss-Newton method consists in iterating, starting from a given ${\overline{u}}_{0}$, We use ${\overline{u}}_{k + 1} = {\text{GN}{(u_{k};\gamma_{k})}}$ to denote hereafter. The convergence is stated in terms of the difference of iterates that, in this case, can directly be linked to the norm of the gradient, denoting $H = {{\nabla^{2}h}{(\overline{x})}}$ and $G = {{\nabla^{2}g}{(\overline{u})}}$, The convergence to a stationary point is guaranteed as long as we are able to get a sufficient decrease condition when minimizing this model as stated in the following proposition.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Accelerated ILQR via accelerated Gauss-Newton", "weight": 1.0} -->

In Algo. 1 we present an accelerated variant of the regularized Gauss-Newton algorithm that blends a regularized Gauss-Newton step and an extrapolated step to potentially capture convexity in the objective. See Appendix F for the proof.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Total complexity with automatic-differentiation oracles", "weight": 1.0} -->

Previous results allow us to state the total complexity of the regularized ILQR algorithm in terms of calls to automatic differentiation oracles as done in the following corollary that combines Cor. 4.4 and Prop. 4.5 with Prop. 3.6. A similar result can be obtained for the accelerated variant. Table 1 summarizes then convergence properties and computational costs of classical methods for discrete time non-linear control.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

We illustrate the performance of the algorithms considered in Sec. 4 including the proposed accelerated regularized Gauss-Newton algorithm on two classical problems drawn: swing-up a pendulum, and move a two-link robot arm.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Control settings", "weight": 1.0} -->

The physical systems we consider below are described by continuous dynamics of the form where ${z{(t)}},{\overset{˙}{z}{(t)}},{\overset{¨}{z}{(t)}}$ denote respectively the position, the speed and the acceleration of the system and $u{(t)}$ is a force applied on the system. The state ${x{(t)}} = {({x_{1}{(t)}},{x_{2}{(t)}})}$ of the system is defined by the position ${x_{1}{(t)}} = {z{(t)}}$ and the speed ${x_{2}{(t)}} = {\overset{˙}{z}{(t)}}$ and the continuous cost is defined as where $T$ is the time of the movement and $h,g$ are given convex costs.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Control settings", "weight": 1.0} -->

The discretization of the dynamics with a time step $\delta$ starting from a given state ${\hat{x}}_{0} = {(z_{0},0)}$ reads then where $\tau = {\lceil{T/\delta}\rceil}$ and the discretized cost reads Figure 1: Control settings considered. From left to right: pendulum, two-link arm robot.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Pendulum", "weight": 1.0} -->

We consider a simple pendulum illustrated in Fig. 1, where $m = 1$ denotes the mass of the bob, $l = 1$ denotes the length of the rod, $\theta$ describes the angle subtended by the vertical axis and the rod, and $\mu = 0.01$ is the friction coefficient. The dynamics are described by The goal is to make the pendulum swing up (i.e. make an angle of $\pi$ radians) and stop at a given time $T$. The cost writes as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Two-link arm", "weight": 1.0} -->

We consider the arm model with two joints (shoulder and elbow), moving in the horizontal plane presented in and illustrated in 1. The dynamics are described by where $\theta = {(\theta_{1},\theta_{2})}$ is the joint angle vector, ${M{(\theta)}} \in {\mathbb{R}}^{2 \times 2}$ is a positive definite symmetric inertia matrix, ${C{(\theta,\overset{˙}{\theta})}} \in {\mathbb{R}}^{2}$ is a vector centripetal and Coriolis forces, $B \in {\mathbb{R}}^{2 \times 2}$ is the joint friction matrix, and ${u{(t)}} \in {\mathbb{R}}^{2}$ is the joint torque that we control. We drop the dependence on $t$ for readability.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Two-link arm", "weight": 1.0} -->

The dynamics are then The expressions of the different variables and parameters are given by where $b_{11} = b_{22} = 0.05$, $b_{12} = b_{21} = 0.025$, $l_{i}$ and $k_{i}$ are respectively the length (30cm, 33cm) and the moment of inertia (0.025kgm^2^, 0.045kgm^2^) of link $i$, $m_{2}$ and $d_{2}$ are respectively the mass (1kg) and the distance (16cm) from the joint center to the center of the mass for the second link.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Two-link arm", "weight": 1.0} -->

The goal is to make the arm reach a feasible target $\theta^{\ast}$ and stop at that point. The objective reads

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

We use the automatic differentiation capabilities of PyTorch to implement the automatic differentiation oracles introduced in Sec. 3. The Gauss-Newton-type steps in Algo. 1 are computed by solving the dual problem associated as presented in Sec. 3.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

In Figure 2, we compare the convergence, in terms of function value and gradient norm, of ILQR (based on Gauss-Newton), regularized ILQR (based on regularized Gauss-Newton), and accelerated regularized ILQR (based on accelerated regularized Gauss-Newton). These algorithms were presented in Sec. 4.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

For ILQR, we use an Armijo line-search to compute the next step. For both the regularized ILQR and the accelerated regularized ILQR, we use a constant step-size sequence tuned after a burn-in phase of 5 iterations. We leave the exploration of more sophisticated line-search strategies for future work.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

The plots show stable convergence of the regularized ILQR on these problems. The proposed accelerated regularized Gauss-Newton algorithm displays stable and fast convergence. Applications of accelerated regularized Gauss-Newton algorithms to reinforcement learning problems would be interesting to explore.
