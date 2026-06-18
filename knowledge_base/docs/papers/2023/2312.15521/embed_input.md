<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

BP-MPC: Optimizing the Closed-Loop Performance of MPC Using Backpropagation

Topics include Model predictive control, Backpropagation, Policy optimization, Differentiable control, Model predictive control tuning, Closed-loop performance.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Optimizes MPC costs and constraints by backpropagating closed-loop performance through linearized dynamics and MPC policies. The paper contributes a convergence-backed tuning procedure for improving closed-loop behavior, including a feasibility-loss extension for cases where the MPC problem can fail.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model predictive control (MPC) is pervasive in research and industry. However, designing the cost function and the constraints of the MPC to maximize closed-loop performance remains an open problem. To achieve optimal tuning, we propose a backpropagation scheme that solves a policy optimization problem with nonlinear system dynamics and MPC policies. We enforce the system dynamics using linearization and allow the MPC problem to contain elements that depend on the current system state and on past MPC solutions. Moreover, we propose a simple extension that can deal with losses of feasibility. Our approach, unlike other methods in the literature, enjoys convergence guarantees.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, optimization-based control algorithms have become increasingly popular in industry and academia, in part thanks to the ever-growing computational power of CPUs, and the availability of fast numerical implementations. Arguably, the biggest appeal of optimization-based control techniques is their ability to explicitly account for process constraints in their formulation, allowing for an optimal and safe selection of the control inputs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A well-known strategy, also commonly used in industry, is model predictive control (MPC). This technique enables feedback by repeatedly solving a numerical optimization problem at every time-step, each time taking into account the current (measured or estimated) state of the system.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because of its effectiveness in practical applications, researchers have dedicated significant effort to the task of designing MPC controllers. For example, showed that the introduction of an appropriately selected terminal cost can ensure stability and feasibility of the closed-loop. More recently, proposed a design to ensures that the MPC behaves like a linear controller around a specified operating point, with the goal of inheriting the well-known stability and robustness properties of linear controllers. The objective function of an MPC can also be chosen to incentivise learning of an unknown model, as proposed.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPC design can be viewed as a policy optimization problem. Policy optimization is a well-known problem in reinforcement learning, where the goal is to obtain a control policy that minimizes some performance objective. In common applications, the policy is parameterized with respect to problem parameters, states, or inputs, and gradient-based techniques are used to learn the optimal parameters. In the context of MPC, the design parameters are generally the cost and the constraints of the problem. The challenge when considering model predictive control policies is that MPCs are generally not differentiable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, differentiable optimization provided a principled way to overcome the nondifferentiability issue. Specifically, proved that, under certain conditions, the optimizer of a quadratic program (QP) is indeed differentiable with respect to design parameters appearing in the cost and the constraints, and that the gradient can be retrieved by applying the implicit function theorem to the KKT conditions of the QP. Since most MPC problems can be written as QPs, this approach effectively allows for the differentiation of MPC policies.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This discovery led to a plethora of applications in the realm of model predictive control. For example, considers the problem of imitation learning, where the tuning parameters are the cost and the model of the linear dynamics of an MPC problem. The idea of utilizing the KKT conditions to obtain derivatives of an optimization problem does not stop with quadratic programs. uses the same technique to compute gradients of a nonlinear optimal control problem, and uses this information to conduct online design of a robust model predictive controller. The goal in this case is to match the performance of a nominal controller. Similarly, introduces a predictive safety filter to ensure safety of the closed-loop operation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

One shortcoming of all approaches mentioned so far is that they rely on the assumption that the optimizer of the MPC problem is continuously differentiable, since the gradient of the optimizer is obtained using the implicit function theorem. It is well-known, however, that this may not be the case, and that the optimizer may not be everywhere differentiable even for simple projection problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The continuous differentiability assumption can be relaxed thanks to the recently developed concept of conservative Jacobians. Conservative Jacobians are set-valued objects that extend gradients to almost-everywhere differentiable functions. These objects satisfy important and useful properties generally associated with differentiable functions, like the chain rule of differentiation and the implicit function theorem. Moreover, conservative Jacobians can be used to create first-order optimization schemes with convergence guarantees.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second limitation of all the approaches mentioned before, is that they all utilize objective functions that concern a single time-step. In most cases, the objective is exclusively open-loop and does not take into account the interaction between the controller and the system dynamics. In this paper, on the other hand, we consider the problem of optimizing the closed-loop trajectory directly by employing a backpropagation-based scheme. Specifically, we compute the conservative Jacobian of the entire closed-loop trajectory with respect to variations of the design parameters by applying the chain rule to the conservative Jacobians of each MPC problem. We then apply a gradient-based scheme to update the value of the parameter to obtain better closed-loop performance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The idea of using backpropagation to improve closed-loop performance of MPC first appeared in and. However, in these works, the authors focused on linear dynamics and simple MPC schemes with no state constraints, without providing formal convergence guarantees. In this paper, we greatly extend the backpropagation framework, primarily by considering nonlinear system dynamics, nonconvex closed-loop objectives, and by allowing the MPC scheme to contain elements that depend on the current state of the system and / or on the MPC solution computed in the previous time-step. Moreover, we provide a simple extension that can safely recover from infeasibility.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper can be summarized as follows.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We utilize the backpropagation paradigm to solve a nonconvex closed-loop policy optimization problem where the policy is a parameterized MPC. The MPC utilizes a linearized version of the system dynamics to retain convexity.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide convergence guarantees of the policy optimization problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We allow the MPC to have cost and constraints that depend on the current state of the system and / or on the solution of the MPC problem in the previous time-steps, allowing for example the possibility of a successive linearization MPC scheme.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a simple extension to deal with cases where the MPC scheme loses feasibility, and provide conditions under which the closed-loop is guaranteed to converge to a safe operation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

To compute the conservative Jacobian of each optimization problem, we adapt and extend the techniques described in to a control theoretic framework. Additionally, we derive problem-specific sufficient conditions under which the nonsmooth implicit function theorem in can be applied. We finally showcase our findings in simulation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is structured as follows. Section III describes the system dynamics (Subsection III-A), the control policy (Subsection III-B), and the policy optimization problem (Subsection III-C). Section IV presents a short recap of conservative Jacobians, their main calculus rule, and a way to minimize such functions with a first-order scheme. Section V demonstrates how the conservative Jacobian of an MPC problem can be computed. Section VI showcases our main algorithmic contribution by describing the backpropagation scheme (Subsection VI-A) and the main optimization algorithm (Subsection VI-B). In Section VII we provide some useful extensions to our scheme; specifically, we present various ways to enforce system dynamics in the MPC problem (Subsection VII-A), we include the possibility of having state-dependent cost and constraints (Subsection VII-B), nonconvex objective functions (Subsection VII-C), and deal with scenarios where the MPC scheme is not feasible (Subsection VII-D). In Section VIII we showcase our methods in simulation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A System dynamics and constraints", "weight": 1.0} -->

We consider a nonlinear time-invariant system where the state dynamics are given for each time-step $t \in {\mathbb{N}}$ by

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A System dynamics and constraints", "weight": 1.0} -->

The parameter vector $p \in {\mathbb{R}}^{n_{p}}$ controls the behavior of the policy $\pi$ at any state ${\overline{x}}_{t}$. We focus on optimization-based policies (specifically, model predictive control). We additionally require $p$ to satisfy the constraint $p \in \mathcal{P}$, for some polytopic set $\mathcal{P}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A System dynamics and constraints", "weight": 1.0} -->

The goal of this paper is to minimize an objective function involving $p$ and the closed-loop state and input trajectory ${(\overline{x},\overline{u})}:={({\overline{x}}_{0},\ldots,{\overline{x}}_{T},{\overline{u}}_{0},\ldots,{\overline{u}}_{T})}$ for some finite time interval ${\mathbb{Z}}_{\lbrack 0,T\rbrack}$, under the constraints in 2. The problem is given in 4.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A System dynamics and constraints", "weight": 1.0} -->

where $\mathcal{C}:{{{\mathbb{R}}^{{({T + 1})}n_{x}} \times {\mathbb{R}}^{{({T + 1})}n_{u}} \times {\mathbb{R}}^{n_{p}}}\rightarrow{\mathbb{R}}_{\geq 0}}$ specifies the performance objective. In 4, $T \in {\mathbb{N}}_{> 0}$ should be chosen large enough to reach the desired equilibrium condition. Ideally, the state ${\overline{x}}_{t}$ should converge to the origin for the current choice of $p$. Problem 4 is potentially non-convex since $\mathcal{C}$ may not be a convex function, and $\pi$ and $f$ may not be affine functions. In the following, for simplicity, we consider the case

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A System dynamics and constraints", "weight": 1.0} -->

for some $Q_{x} \in {\mathbb{R}}^{n_{x} \times n_{x}}$ with $Q_{x} \succ 0$. Our method can easily be extended to more general cost functions as described in Subsection VII-C.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A System dynamics and constraints", "weight": 1.0} -->

Before proposing an algorithmic solution to 4, we specify what class of policies $\pi$ we are interested, namely, model predictive control policies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

In this paper, we restrict our attention to MPC policies, where the control input is chosen as the solution of an optimal control problem. Specifically, after measuring the current state ${\overline{x}}_{t}$, we use the knowledge we possess about the system 1 to optimize the future prediction of the state-input trajectories of the system.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

where $A_{t}$, $B_{t}$, and $c_{t}$ are known at runtime and should be chosen to accurately approximate the real dynamics 1 in the vicinity of ${\overline{x}}_{t}$. We use $S_{t}:={(A_{t},B_{t},c_{t})}$ to compactly represent the approximate dynamics at time $t$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

Each predicted state and input must satisfy the constraints 2. In addition, we generally impose different constraints on the predicted terminal state $x_{N|t}$, namely

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

The objective function in the MPC is an approximation of the objective in 4, given by

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

where we added a terminal penalty ${\| x_{N|t}\|}_{P}^{2}$ and a penalty on the input, with ${P,R_{u}} \succ 0$. The positive definiteness of $Q_{x}$, $R_{u}$, and $P$ ensures that the problem is strongly convex.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

The MPC problem that is solved online at each time-step is therefore given as follows.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Model predictive control", "weight": 1.0} -->

In this paper, we choose the terminal ingredients (i.e., the terminal cost and the terminal constraints) as tunable parameters, namely by letting $p:={(P,H_{x,N},h_{x,N})}$; however, we can, using the same math and algorithms, choose $p$ as any other element appearing in the cost or in the constraints of 7.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C A projected gradient-based framework", "weight": 1.0} -->

In this section, we rewrite 4 considering the control policy given in 8 and then provide a simple gradient-based algorithm that can be used to solve such a problem. For simplicity, we assume that $S_{t} \equiv S$ and write simply $\text{MPC}{({\overline{x}}_{t},p)}$. We deal with the more complex case where $S_{t}$ is dynamically determined online in Subsection VII-A.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C A projected gradient-based framework", "weight": 1.0} -->

First, combining problem 4 with the cost function 5 and the policy in 7, we obtain the closed-loop control problem in 9. Note that we can remove the input constraints 2b in 4, as these are automatically satisfied if the inputs ${\overline{u}}_{t}$ are obtained from the MPC policy 7.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C A projected gradient-based framework", "weight": 1.0} -->

As shown in Appendix A, 9 can be compactly rewritten as follows.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C A projected gradient-based framework", "weight": 1.0} -->

where $\overline{x}{(p)}$ is the closed loop state trajectory generated by the dynamics 1 under the policy 8 for a given value of $p$. In the following section, we derive an efficient procedure to obtain gradients of the function $\mathcal{C}$ with respect to $p$. Since $\overline{x}$ is generally a nonsmooth function of $p$, we need to utilize a more general version of gradient that applies to nonsmooth functions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conservative Jacobians", "weight": 1.0} -->

In the upcoming sections we repeatedly deal with the problem of minimizing a nonsmooth, nonconvex function. These problems admit a simple solution strategy based on a descent algorithm; however, because of the nonsmoothness, we cannot always guarantee the existence of a gradient. Luckily, we can still devise descent algorithms if the function is almost everywhere differentiable thanks to the concept of conservative Jacobian. This section describes how conservative Jacobians generalize the notion of gradient to functions that are almost everywhere differentiable.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conservative Jacobians", "weight": 1.0} -->

An absolutely continuous curve, or path, is an absolutely continuous function $x:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{n}}$ which admits a derivative $\overset{˙}{x}$ for almost every $t \in {\lbrack 0,1\rbrack}$, and for which ${x{(t)}} - {x{}}$ is the Lebesgue integral of $\overset{˙}{x}$ between $0$ and $t$ for all $t \in {\lbrack 0,1\rbrack}$. Equipped with the definition of path, we can define the concept of conservative Jacobian.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Differentiating the MPC policy", "weight": 1.0} -->

In this section we rewrite 7 in a more convenient form and then show that, under certain conditions, the map MPC$({\overline{x}}_{t},p)$ admits a conservative Jacobian. This Jacobian will later be used to devise a descent algorithm for 9. We begin by rewriting MPC$({\overline{x}}_{t},p)$ as a quadratic program in standard form.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Writing the MPC problem as a QP", "weight": 1.0} -->

The optimal control problem MPC$({\overline{x}}_{t},p)$ is a quadratic program. Following the procedure outlined in Appendix B, we can reformulate the problem in standard form as follows.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Writing the MPC problem as a QP", "weight": 1.0} -->

where we defined $\overline{p}:={({\overline{x}}_{t},p)}$ for simplicity. We denote with $n_{\text{in}}$ and $n_{\text{eq}}$ the number of inequality and equality constraints in 12, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Writing the MPC problem as a QP", "weight": 1.0} -->

Note that the parameter $p$ can potentially affect every element in the cost and in the constraints of QP$(\overline{p})$, whereas the initial condition ${\overline{x}}_{t}$ can only affect the linear parts of the cost and the constraints.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Writing the MPC problem as a QP", "weight": 1.0} -->

It theory, it would be possible to obtain the conservative Jacobian of the solution $y{(\overline{p})}$ of QP$(\overline{p})$ with respect to variations of $\overline{p}$, but this turns out to be unnecessarily complex because of the presence of $\overline{p}$ in the equality and inequality constraints. To greatly simplify the computation of the conservative Jacobian, we prefer to operate on the Lagrange dual problem associated to QP$(\overline{p})$. In this case, the constraints are parameter-independent, as $\overline{p}$ only affects the cost function of the problem.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Writing the MPC problem as a QP", "weight": 1.0} -->

Since our procedure involves computing the conservative Jacobian of the dual optimizer, we must ensure that the dual problem has a unique solution for every value of $\overline{p}$. To this end, we impose the following assumption.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For all parameter vectors $\overline{p}$ in some polytopic set $\mathcal{Y}$, the matrix $Q{(p)}$ in 12 is positive definite, problem 12 is feasible, and it satisfies the linear independence constraint qualification (LICQ).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Recall that problem 12 satisfies the LICQ if given a solution $y{(\overline{p})}$ of the problem, the rows $\mathbf{r}{(G,i)}$ of $G$ associated to the active inequality constraints (i.e., those vectors $v_{i} = {\mathbf{r}{(G,i)}^{\top}}$ for which ${v_{i}y{(\overline{p})}} = g_{i}$) and the rows $\mathbf{r}{(F,i)}$ of $F$ for $i \in {\mathbb{Z}}_{\lbrack 1,n_{\text{eq}}\rbrack}$ are linearly independent. Note that the LICQ assumption is always verified if, for example, the constraints on $x_{k|t}$ and $u_{k|t}$ in 7 are simple box constraints, i.e., given by

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The feasibility condition in Assumption 1 is quite restrictive in practical scenarios. We propose a simple extension of our method that can deal with losses of feasibility in Subsection VII-D.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under Assumption 1, we can obtain the Lagrange dual of QP$(\overline{p})$ following the procedure outlined in Appendix C.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that in D$(\overline{p})$, the parameters $p$ and ${\overline{x}}_{t}$ only affect the quadratic part $H$ and the linear part $h$ of the cost, whereas the matrix $E$ in the constraints is parameter-independent.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Writing the dual as fixed point condition", "weight": 1.0} -->

Our next objective is to synthesize a simple procedure to obtain the conservative Jacobian $\mathcal{J}_{z}$ of the dual optimizer $z$. Later, we will use $\mathcal{J}_{z}$ to obtain the conservative jacobian of the primal optimizer $y$ through 14.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Writing the dual as fixed point condition", "weight": 1.0} -->

To obtain $\mathcal{J}_{z}$, we follow the procedure proposed, namely, we write the optimality conditions of D$(\overline{p})$ as a fixed point equation ${\mathcal{F}{(z,\overline{p})}} = 0$, obtain the conservative Jacobian of $\mathcal{F}$ with respect to $z$ and $\overline{p}$, and apply the implicit function theorem described in Lemma 3. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). Under Assumption 1, we show that the invertibility condition in the statement of Lemma 3. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") is always verified even if the dual problem is not necessarily strongly convex.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Writing the dual as fixed point condition", "weight": 1.0} -->

Since D$(\overline{p})$ is a quadratic program, the following is a well known necessary and sufficient condition for optimality \[17, Theorem 3.67\]:

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Writing the dual as fixed point condition", "weight": 1.0} -->

where $N_{C}$ is the normal cone mapping of $C$ \[17, Example 3.5\]. Leveraging \[18, Corollary 27.3\], we have that 15 is equivalent to

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Writing the dual as fixed point condition", "weight": 1.0} -->

To obtain the conservative Jacobian of $\mathcal{F}$, we need $\mathcal{F}$ to be path-differentiable. This can be easily guaranteed with the following, mild, assumption.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Leveraging Assumption 2, we have the following.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 1", "weight": 1.0} -->

See Remark 3 in Appendix D for more details. The simplicity of this computation is one of the primary reasons why the authors decided to work with the dual 13 instead of the primal 12.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The conservative Jacobian $\mathcal{J}_{y}{(\overline{p})}$ of the primal optimizer $y{(\overline{p})}$ can then easily be retrieved from $\mathcal{J}_{z}{(\overline{p})}$ using 14. For simplicity, define

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-A Backpropagation", "weight": 1.0} -->

In the previous section, we showed how to compute the conservative Jacobian of the MPC map with respect to both the initial condition $x_{0}$, and the design parameter $p$. In this section, we build on this knowledge and describe a simple modular mechanism that can be used to obtain the conservative Jacobian of the entire closed loop trajectory $\overline{x}$ using the individual conservative Jacobians of each optimization problem.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Backpropagation", "weight": 1.0} -->

The paradigm we employ, backpropagation, is far from unknown. In fact, this algorithmic invention had a huge impact in the field of machine learning and optimization. Backpropagation can be used to efficiently construct gradients with respect to design parameters of algorithms involving several successive steps. The idea is to compute the gradients of each step and combine them using the chain rule. This method eliminates redundant calculations, thus improving efficiency.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Backpropagation", "weight": 1.0} -->

In our case, the closed loop dynamics can be expressed as a recursive equation

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-A Backpropagation", "weight": 1.0} -->

where every state ${\overline{x}}_{t + 1}$ depends solely on its predecessor ${\overline{x}}_{t}$, and the design parameters $p$. To be able to propagate the conservative Jacobians through the dynamics of the system, we require $f$ to admit conservative Jacobians.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The function $f$ is locally Lipschitz and semi-algebraic.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Note that $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p)}$ depends on $\mathcal{J}_{{\overline{x}}_{t}}{(p)}$, and since ${\overline{x}}_{0}$ is given, we have ${\mathcal{J}_{{\overline{x}}_{0}}{(p)}} = 0$. As a result, we can easily construct an algorithm that computes the conservative Jacobian of the closed loop trajectory $\overline{x}$ for a given value of $p$ iteratively. The algorithm, summarized in Algorithm 3, can be implemented online, as the closed-loop is being simulated and the values of ${\overline{x}}_{t}$ are being measured.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The next result formalizes the ideas expressed in this section.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-B Optimization algorithm", "weight": 1.0} -->

Once the conservative Jacobian is available, we can utilize it to update the parameter $p$ with a gradient-based scheme. To guarantee convergence to a local minimum, it suffices to meet the conditions of Algorithm 1. ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). We therefore choose the following update scheme

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B Optimization algorithm", "weight": 1.0} -->

where ${\overline{x}}^{k} = {\overline{x}{(p^{k})}}$, and where $\alpha_{k}$ satisfies the conditions in 11. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). The overall algorithm, that combines all the steps we describes so far, is given below.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-B Optimization algorithm", "weight": 1.0} -->

As long as the map MPC$(\overline{p})$ is well-defined, i.e., the problem MPC$(\overline{p})$ admits a feasible solution throughout the entirety of the execution of Algorithm 4, we have the following.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VII-A Choosing $S_{t}$", "weight": 1.0} -->

The approximate model, denoted $S_{t}$, heavily impacts the control performance, where an accurate model results in better performance. Generally, since the control scheme is deployed in receding horizon (that is, the optimization is repeated at every time-step and only the first entry $u_{0|t}$ of the optimal input trajectory is applied), we only require accurate knowledge of the system locally, in the vicinity of the current state ${\overline{x}}_{t}$. We present here three progressively more accurate choices of $S_{t}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VII-A1 Linearization at a single equilibrium point", "weight": 1.0} -->

The easiest choice is to consider a time-invariant model $S_{t} \equiv S$, where $S$ is obtained by linearizing $f$ at some equilibrium point $(\hat{x},\hat{u})$ (i.e., a point satisfying ${f{(\hat{x},\hat{u})}} = 0$). Specifically, we choose $S = {(A,B,0)}$ with

<!-- chunk {"id": "body-0071", "role": "body", "section": "VII-A1 Linearization at a single equilibrium point", "weight": 1.0} -->

Note that in the computation of $S$ and in the Taylor expansion we implicitly assumed that $f$ is continuously differentiable, a stronger assumption than the one in Assumption 3. If $f$ is not continuously differentiable, we can still utilize this approach by choosing $A$ and $B$ in some other way (in this case however the error bound 24 may fail to hold).

<!-- chunk {"id": "body-0072", "role": "body", "section": "VII-A1 Linearization at a single equilibrium point", "weight": 1.0} -->

Despite its simplicity, linearizing at a single equilibrium point is quite common in the MPC literature and has proved to be successful in many application scenarios, in particular when the control objective is to maintain the state of the system at some desired steady state.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VII-A2 Linearization at the current state", "weight": 1.0} -->

A more accurate approach, that is generally more effective in reference tracking problems, is to update the model based on the current state of the system. Ideally, we would like to construct $S_{t}$ by linearizing $f$ at the current state and input $({\overline{x}}_{t},{\overline{u}}_{t})$. However, ${\overline{u}}_{t}$ is not known until after we find a solution to MPC$(\overline{p})$, and in fact $S_{t}$ plays a role in determining ${\overline{u}}_{t}$. An implementable solution is to replace ${\overline{u}}_{t}$ with $u_{1|{t - 1}}$, that is, with the second entry of the optimal input trajectory computed at time-step $t - 1$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VII-A2 Linearization at the current state", "weight": 1.0} -->

The approximation error between the real dynamics and the linearized dynamics can be computed by considering the Taylor expansion of $f$ around $({\overline{x}}_{t},u_{1|{t - 1}})$

<!-- chunk {"id": "body-0075", "role": "body", "section": "VII-A2 Linearization at the current state", "weight": 1.0} -->

If the input state trajectory $(x_{t},u_{t})$ predicted by the MPC at time $t$ does not deviate significantly from $({\overline{x}}_{t},u_{1|{t - 1}})$, then from 25 we can conclude that the linearized dynamics represent a good approximation of the system.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VII-A2 Linearization at the current state", "weight": 1.0} -->

The variable $u_{1|{t - 1}}$ is itself dependent on both ${\overline{x}}_{t - 1}$ and $p$ (it is part of the optimizer of $\text{MPC}{({\overline{x}}_{t - 1},p)}$), we therefore need to adapt the backpropagation scheme in 21 to account for this fact. We present the updated algorithm in the next section, where we deal with a more general choice of $S_{t}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

We can achieve even better accuracy by allowing the nominal dynamics to vary across different time-steps within the same MPC problem, that is, by setting

<!-- chunk {"id": "body-0078", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

Alternatively, we can use ${\overline{x}}_{t}$ instead of $x_{1|{t - 1}}$. If the decision variables in the MPC problem at time $t - 1$ do not include $u_{N|{t - 1}}$, we can obtain $A_{N - {1|t}}$ by linearizing at $(x_{N|{t - 1}},u_{N - {1|{t - 1}}})$. This strategy is commonly refered as successive linearization in the MPC literature.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

Choosing the model with successive linearization, we have that $S_{t}$ depends on the entire solution $y_{t - 1}:={(x_{t - 1},u_{t - 1})}$ of the MPC problem at time $t - 1$, and possibly also on ${\overline{x}}_{t}$. This needs to be taken into account when computing the conservative Jacobian in Algorithm 3. Specifically, the map MPC$({\overline{x}}_{t},p)$ should more correctly be defined as $\text{MPC}{({\overline{x}}_{t},y_{t - 1},p)}$, highlighting the dependency on $y_{t - 1}$. We therefore have

<!-- chunk {"id": "body-0080", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

where the difference from 21 is the additional term $\mathcal{J}_{\text{MPC},y_{t - 1}}{({\overline{x}}_{t},y_{t - 1},p)}\mathcal{J}_{y_{t - 1}}{(p)}$ which accounts for the dependency of $y_{t - 1}$ on $p$. The term $\mathcal{J}_{y_{t - 1}}{(p)}$ needs to be constructed using a backpropagation algorithm. Defining $y_{t - 1} = {{QP}{({\overline{x}}_{t - 1},y_{t - 2},p)}}$, where the map $QP$ is the same one defined in 12 with the addition of the parameter $y_{t - 2}$, we have

<!-- chunk {"id": "body-0081", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

Before beginning the simulation of the system, we need to fix a linearization trajectory $y_{- 1}$ for time-step $t = 0$. Naturally, we cannot utilize any previous MPC solution, since $t = 0$ is the first time-step at which we solve the MPC problem. We can choose $y_{- 1}$ either as a fixed and pre-defined trajectory, or let $y_{- 1}$ be part of $p$, thus allowing the optimization process select the value of $y_{- 1}$ that yields the best closed-loop performance.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

Below, we provide an algorithmic implementation of the linearization strategy described in paragraphs 2) and 3) of this section.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VII-A3 Linearization along a trajectory", "weight": 1.0} -->

Note that we can still employ Algorithm 2 to compute $\mathcal{J}_{\text{MPC}}$ by simply redefining $\overline{p}:={({\overline{x}}_{t},y_{t - 1},p)}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VII-B State-dependent cost and constraints", "weight": 1.0} -->

The closed-loop performance of receding-horizon MPC schemes can be greatly improved by allowing certain elements in the MPC problem to be dependent on the current state of the system. For example the authors construct terminal ingredients (cost and constraints) online, utilizing knowledge of the measured state of the system ${\overline{x}}_{t}$. They then demonstrate that this approach enlarges the region of attraction of the scheme.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VII-B State-dependent cost and constraints", "weight": 1.0} -->

Our backpropagation framework easily allows to incorporate initial state-dependent elements in the MPC problem. For example, we can choose $H_{x,N}$, $h_{x,N}$, and $P$ to be functions of both $p$ and ${\overline{x}}_{t}$. In this case, problem 7 becomes

<!-- chunk {"id": "body-0086", "role": "body", "section": "VII-B State-dependent cost and constraints", "weight": 1.0} -->

where $A \sim B$ means that $A$ is a function of $B$. Note that once ${\overline{x}}_{t}$ is available, the state-dependent elements $H_{x,N}$, $h_{x,N}$, and $P$ can be computed explicitly, meaning that the MPC problem we solve at runtime continues to be a quadratic program. The same procedure can be applied to the case where $H_{x}$, $H_{u}$, $h_{x}$, $h_{u}$, or even the cost matrices $Q$ and $R$ are dependent on ${\overline{x}}_{t}$. We leave such cases for future work and emphasize that our framework is flexible to tune almost any component of the underlying MPC problem.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VII-B State-dependent cost and constraints", "weight": 1.0} -->

The MPC problem considered so far, i.e., 7, was already dependent on ${\overline{x}}_{t}$, which affected the initial state $x_{0|t}$ of the problem. The difference with 28 is that, in the latter, ${\overline{x}}_{t}$ not only affects $x_{0|t}$, but also other optimization variables through the effect on $H_{x,N}$, $h_{x,N}$, and $P$. Note, however, that 28 can be written as a quadratic program in the form

<!-- chunk {"id": "body-0088", "role": "body", "section": "VII-B State-dependent cost and constraints", "weight": 1.0} -->

which differs from QP$(\overline{p})$ as given in Subsection V-A only because $Q$, $F$, and $G$ now depend on both ${\overline{x}}_{t}$ and $p$. As a result, we can perform closed-loop optimization using the same algorithmic procedure as in Algorithm 4 without any modification, exception made for the symbolic expression of $Q$, $F$, and $G$ which now depend on $\overline{p} = {({\overline{x}}_{t},p)}$ instead of only $p$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Using the technique outline above, one can easily incorporate cost matrices $Q_{x}$ and $R_{u}$ that also depend on $y_{t - 1}$, for example by linearizing the possibly nonlinear cost function $\mathcal{C}$ along the trajectory $y_{t - 1}$ and adding sufficient regularization to ensure the positive definiteness of both $Q_{x}$ and $R_{u}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VII-C Non-convex cost", "weight": 1.0} -->

Our framework easily extends to scenarios where the quadratic cost in 4 is replaced with more sophisticated costs that can possibly involve other terms in addition to $\overline{x}$. Consider, for example, the following problem

<!-- chunk {"id": "body-0091", "role": "body", "section": "VII-C Non-convex cost", "weight": 1.0} -->

where $y:={(y_{0},\ldots,y_{T})}$ and $z = {(z_{0},\ldots,z_{T})}$ represent the collection of all the primal-dual optimizers of MPC. The matrix $I_{u}$ selects from $y_{t}$ the entry corresponding to $u_{0|t}$. Note that we can include any of the optimization variables in the cost and still manage to efficiently compute the gradient of the objective by storing the conservative Jacobians $\mathcal{J}_{y_{t}}{(p)}$ and $\mathcal{J}_{z_{t}}{(p)}$ and then applying the Leibniz rule

<!-- chunk {"id": "body-0092", "role": "body", "section": "VII-C Non-convex cost", "weight": 1.0} -->

The conservative Jacobians $\mathcal{J}_{y}$ and $\mathcal{J}_{z}$ are already available as a by-product of Algorithm 2.

<!-- chunk {"id": "body-0093", "role": "body", "section": "VII-C Non-convex cost", "weight": 1.0} -->

To ensure that Lemma 5 is still applicable, we only require $\mathcal{C}$ to be path-differentiable jointly in its arguments. Under this condition, the results of Theorem 1 still hold. Note that the class of path-differentiable functions is quite large, and comprises a large selection of non convex functions.

<!-- chunk {"id": "body-0094", "role": "body", "section": "VII-D Dealing with infeasibility", "weight": 1.0} -->

So far, we did not concern ourselves with the situation where 7 does not admit a feasible solution. This can happen frequently in practice, since the gradient-based optimization scheme is modifying the behavior of MPC$({\overline{x}}_{t},p)$, without any guarantees that the resulting closed-loop will produce states ${\overline{x}}_{t}$ for which MPC$({\overline{x}}_{t},p)$ admits a solution. There is, however, a simple procedure that can be used to recover from infeasible scenarios by leveraging the formulation in 29. The modification comprises two steps: first we need to modify MPC$({\overline{x}}_{t},p)$ to ensure its feasibility, then we change the cost function $\mathcal{C}$ to ensure that $p$ is chosen to minimize constraint violations.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VII-D Dealing with infeasibility", "weight": 1.0} -->

First of all, we need to modify MPC$({\overline{x}}_{t},p)$ to ensure that the optimization problem admits a solution for every value of ${\overline{x}}_{t}$ and $p$. In MPC$({\overline{x}}_{t},p)$, the input constraints can always be satisfied, since $u_{t}$ is a decision variable. The problematic constraints are only those involving the state variable $x_{t}$. We reformulate 7 by introducing new optimization variables (namely, $\epsilon_{t}$) that relax the state constraints.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VII-D Dealing with infeasibility", "weight": 1.0} -->

To avoid unnecessary constraint violation, we penalize nonzero values of $\epsilon_{t}$ with the penalty function $P_{\epsilon}$, chosen as

<!-- chunk {"id": "body-0097", "role": "body", "section": "VII-D Dealing with infeasibility", "weight": 1.0} -->

for some ${c_{1},c_{2}} > 0$. If $c_{2}$ is large enough, one can prove that $P_{\epsilon}$ is an exact penalty function.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Simulation example", "weight": 1.0} -->

All simulation are done in CasADi with the active set solver qpOASES on a laptop with $32$ GB of RAM and an Intel(R) Core (TM) processor i7-1165G7 @ 2.80GHz. The code is available and open source^11^1At the link Table I shows the average computation time for each closed-loop iteration for all simulation examples.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

We begin by deploying our optimization scheme to solve problem 9 for a double integrator

<!-- chunk {"id": "body-0100", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

The closed loop objective is to minimize

<!-- chunk {"id": "body-0101", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

with $Q_{x} = I$ and $R_{u} = 10^{- 4}$. The MPC utilizes the same cost matrices $Q_{x}$ and $R_{u}$, moreover, we parameterize the terminal cost $P$ in 7 as

<!-- chunk {"id": "body-0102", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

and choose $p = {(p_{1},p_{2},p_{3})}$. Note that this choice of $P$ ensures $P \succ 0$ for all $p$. The initial design is $p^{0} = {(0.1,0,0.1)}$. We choose a very short horizon of $N = 5$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

where $\eta \in {(0.5,1\rbrack}$ and $\rho > 0$ are design parameters. Since the term $k$ in the denominator eventually dominates, this choice of stepsizes fullfills the assumptions in Theorem 1 for any $\eta \in {(0.5,1\rbrack}$ and $\rho > 0$, and the iterates ${\{ p^{k}\}}_{k \in {\mathbb{N}}}$ are therefore guaranteed to converge to a critical point of 9.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

The best achievable performance $\mathcal{C}^{\ast} = \mathcal{C}^{200} = 5249.13$ is attained with parameter

<!-- chunk {"id": "body-0105", "role": "body", "section": "VIII-A Linear example", "weight": 1.0} -->

This parameter choice produces better performance than the one obtained with $P$ chosen as the solution of the discrete time Riccati equation, i.e.,

<!-- chunk {"id": "body-0106", "role": "body", "section": "VIII-B Nonlinear example", "weight": 1.0} -->

We now deploy our scheme to the following nonlinear system

<!-- chunk {"id": "body-0107", "role": "body", "section": "VIII-B Nonlinear example", "weight": 1.0} -->

and with the same objective 36. We use the linearization strategy described in Subsection VII-A3 and choose an even shorter horizon $N = 3$. We use the same parameterization and update rule as in Subsection VIII-A.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VIII-C Loss of feasibility example", "weight": 1.0} -->

In this section we consider the same system and cost as in Subsection VIII-B with tighter constraints

<!-- chunk {"id": "body-0109", "role": "body", "section": "VIII-C Loss of feasibility example", "weight": 1.0} -->

In this case, the MPC problem quickly becomes infeasible; therefore, we utilize the soft-constrained version in 30 with penalty parameters $c_{1} = 1$ and $c_{2} = 10$. By applying the same optimization scheme as in Subsection VIII-B, with cost as in 36, we obtain the trajectories in Figure 5.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VIII-C Loss of feasibility example", "weight": 1.0} -->

Note that after $300$ iterations the closed-loop trajectory has converged to a steady-state where constraints are violated (in particular, the constraint on the second entry of the state is not satisfied between time-step $4$ and $8$). This is not surprising since the upper-level objective function $\mathcal{C}$ does not include any information about constraint violation. The closed loop cost after $300$ iteration is $\mathcal{C}_{300} = 347.076$, which is significantly smaller than the best achievable cost (with constraint satisfaction), equal to $\mathcal{C}^{\ast} = 353.266$. The value of $p$ after $300$ iterations is

<!-- chunk {"id": "body-0111", "role": "body", "section": "VIII-C Loss of feasibility example", "weight": 1.0} -->

If we use the objective function in 34 with ${P_{\epsilon}{(\epsilon)}} = {200\mathbf{1}^{\top}\epsilon}$ (where $\epsilon:={(\epsilon_{1},\epsilon_{2},\ldots,\epsilon_{T})}$ contains the slack variables of all the optimization problems, each of which spans $N$ time-steps, and $\mathbf{1}$ is the vector of all ones), we obtain the trajectory in Figure 6, where the constraints are satisfied and $\epsilon = 0$. In this case, the effect of a penalty on the constraint violation induces the optimization algorithm to favor values of $p$ that maintain small constraint violations. This happens at the cost of a worse closed-loop performance, which becomes now equal to the best safe performance $\mathcal{C}^{\ast}$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a backpropagation algorithm to optimally design an MPC scheme to maximize closed-loop performance. The cost and the constraints in the MPC can depend on the current state of the system, as well as on past solutions of previous MPC problems. This allows, for example, the utilization of the successive linearization strategy.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We employed conservative Jacobians to compute the sensitivity of the closed-loop trajectory with respect to variations of the design parameter. Leveraging a non-smooth version of the implicit function theorem, we derived sufficient conditions under which the gradient-based optimization procedure converges to a critical point of the problem.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We extended our framework to cases where the MPC problem becomes infeasible using nonsmooth penalty functions. We derived conditions under which the closed-loop is guaranteed to converge to a safe solution.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Current work focuses on deploying our optimization scheme on more realistic real-life examples. Future work will focus on extending our scheme to scenarios where the system dynamics are only partially known and / or affected by stochastic noise.
