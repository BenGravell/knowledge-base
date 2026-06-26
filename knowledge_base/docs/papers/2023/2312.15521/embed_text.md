## Introduction

In recent years, optimization-based control algorithms have become increasingly popular in industry and academia, in part thanks to the ever-growing computational power of CPUs, and the availability of fast numerical implementations. Arguably, the biggest appeal of optimization-based control techniques is their ability to explicitly account for process constraints in their formulation, allowing for an optimal and safe selection of the control inputs.

A well-known strategy, also commonly used in industry, is model predictive control (MPC). This technique enables feedback by repeatedly solving a numerical optimization problem at every time-step, each time taking into account the current (measured or estimated) state of the system.

Because of its effectiveness in practical applications, researchers have dedicated significant effort to the task of designing MPC controllers. For example, showed that the introduction of an appropriately selected terminal cost can ensure stability and feasibility of the closed-loop. More recently, proposed a design to ensures that the MPC behaves like a linear controller around a specified operating point, with the goal of inheriting the well-known stability and robustness properties of linear controllers. The objective function of an MPC can also be chosen to incentivise learning of an unknown model, as proposed .

MPC design can be viewed as a policy optimization problem. Policy optimization is a well-known problem in reinforcement learning, where the goal is to obtain a control policy that minimizes some performance objective. In common applications, the policy is parameterized with respect to problem parameters, states, or inputs, and gradient-based techniques are used to learn the optimal parameters. In the context of MPC, the design parameters are generally the cost and the constraints of the problem. The challenge when considering model predictive control policies is that MPCs are generally not differentiable.

Recently, differentiable optimization provided a principled way to overcome the nondifferentiability issue. Specifically, proved that, under certain conditions, the optimizer of a quadratic program (QP) is indeed differentiable with respect to design parameters appearing in the cost and the constraints, and that the gradient can be retrieved by applying the implicit function theorem to the KKT conditions of the QP. Since most MPC problems can be written as QPs, this approach effectively allows for the differentiation of MPC policies.

This discovery led to a plethora of applications in the realm of model predictive control. For example, considers the problem of imitation learning, where the tuning parameters are the cost and the model of the linear dynamics of an MPC problem. The idea of utilizing the KKT conditions to obtain derivatives of an optimization problem does not stop with quadratic programs. uses the same technique to compute gradients of a nonlinear optimal control problem, and uses this information to conduct online design of a robust model predictive controller. The goal in this case is to match the performance of a nominal controller. Similarly, introduces a predictive safety filter to ensure safety of the closed-loop operation.

One shortcoming of all approaches mentioned so far is that they rely on the assumption that the optimizer of the MPC problem is continuously differentiable, since the gradient of the optimizer is obtained using the implicit function theorem. It is well-known, however, that this may not be the case, and that the optimizer may not be everywhere differentiable even for simple projection problems.

The continuous differentiability assumption can be relaxed thanks to the recently developed concept of conservative Jacobians. Conservative Jacobians are set-valued objects that extend gradients to almost-everywhere differentiable functions. These objects satisfy important and useful properties generally associated with differentiable functions, like the chain rule of differentiation and the implicit function theorem. Moreover, conservative Jacobians can be used to create first-order optimization schemes with convergence guarantees.

A second limitation of all the approaches mentioned before, is that they all utilize objective functions that concern a single time-step. In most cases, the objective is exclusively open-loop and does not take into account the interaction between the controller and the system dynamics. In this paper, on the other hand, we consider the problem of optimizing the closed-loop trajectory directly by employing a backpropagation-based scheme. Specifically, we compute the conservative Jacobian of the entire closed-loop trajectory with respect to variations of the design parameters by applying the chain rule to the conservative Jacobians of each MPC problem. We then apply a gradient-based scheme to update the value of the parameter to obtain better closed-loop performance.

The idea of using backpropagation to improve closed-loop performance of MPC first appeared in and. However, in these works, the authors focused on linear dynamics and simple MPC schemes with no state constraints, without providing formal convergence guarantees. In this paper, we greatly extend the backpropagation framework, primarily by considering nonlinear system dynamics, nonconvex closed-loop objectives, and by allowing the MPC scheme to contain elements that depend on the current state of the system and / or on the MPC solution computed in the previous time-step. Moreover, we provide a simple extension that can safely recover from infeasibility.

The contributions of this paper can be summarized as follows.

We utilize the backpropagation paradigm to solve a nonconvex closed-loop policy optimization problem where the policy is a parameterized MPC. The MPC utilizes a linearized version of the system dynamics to retain convexity.

We provide convergence guarantees of the policy optimization problem.

We allow the MPC to have cost and constraints that depend on the current state of the system and / or on the solution of the MPC problem in the previous time-steps, allowing for example the possibility of a successive linearization MPC scheme.

We propose a simple extension to deal with cases where the MPC scheme loses feasibility, and provide conditions under which the closed-loop is guaranteed to converge to a safe operation.

To compute the conservative Jacobian of each optimization problem, we adapt and extend the techniques described in to a control theoretic framework. Additionally, we derive problem-specific sufficient conditions under which the nonsmooth implicit function theorem in can be applied. We finally showcase our findings in simulation.

The remainder of this paper is structured as follows. Section III describes the system dynamics (Subsection III-A), the control policy (Subsection III-B), and the policy optimization problem (Subsection III-C). Section IV presents a short recap of conservative Jacobians, their main calculus rule, and a way to minimize such functions with a first-order scheme. Section V demonstrates how the conservative Jacobian of an MPC problem can be computed. Section VI showcases our main algorithmic contribution by describing the backpropagation scheme (Subsection VI-A) and the main optimization algorithm (Subsection VI-B). In Section VII we provide some useful extensions to our scheme; specifically, we present various ways to enforce system dynamics in the MPC problem (Subsection VII-A), we include the possibility of having state-dependent cost and constraints (Subsection VII-B), nonconvex objective functions (Subsection VII-C), and deal with scenarios where the MPC scheme is not feasible (Subsection VII-D). In Section VIII we showcase our methods in simulation.

## Notation

We use $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{R}$ to denote the set of natural, rational, and real numbers, respectively. ${\mathbb{N}}_{> 0}$ is the set of positive real numbers, and ${\mathbb{Z}}_{\lbrack a,b\rbrack}$ is the set of integers $z$ with $a \leq z \leq b$, for some $a \leq b$. ${\mathbb{R}}^{n}$ denotes the space of $n$-dimensional real-valued vectors and ${\mathbb{R}}^{n \times m}$ the space of $n \times m$ real-valued matrices. If $C \subset {\mathbb{R}}^{n}$ is a convex set, we denote with $P_{C}$ the orthogonal projector to the set. Given a matrix $A \in {\mathbb{R}}^{n \times m}$, we use $\mathbf{r}{(A,j)}$ to denote the $j$-th row of $A$ (with $j \in {\mathbb{Z}}_{\lbrack 1,n\rbrack}$), and $\mathbf{c}{(A,i)}$ to denote the $i$-th column of $A$ (with $i \in {\mathbb{Z}}_{\lbrack 1,m\rbrack}$).

## Problem formulation

### III-A System dynamics and constraints

We consider a nonlinear time-invariant system where the state dynamics are given for each time-step $t \in {\mathbb{N}}$ by with $f$ locally Lipschitz and ${\overline{x}}_{0} \in {\mathbb{R}}^{n_{x}}$ known. Without loss of generality, we assume that ${({\overline{x}}_{t},{\overline{u}}_{t})} = 0$ is an equilibrium for 1. The state ${\overline{x}}_{t} \in {\mathbb{R}}^{n_{x}}$ and the input ${\overline{u}}_{t} \in {\mathbb{R}}^{n_{u}}$ are subject to polytopic constraints The control input ${\overline{u}}_{t}$ is determined, at each time-step, by a parameterized control policy $\pi:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{p}}}\rightarrow{\mathbb{R}}^{n_{u}}}$ The parameter vector $p \in {\mathbb{R}}^{n_{p}}$ controls the behavior of the policy $\pi$ at any state ${\overline{x}}_{t}$. We focus on optimization-based policies (specifically, model predictive control). We additionally require $p$ to satisfy the constraint $p \in \mathcal{P}$, for some polytopic set $\mathcal{P}$.

The goal of this paper is to minimize an objective function involving $p$ and the closed-loop state and input trajectory ${(\overline{x},\overline{u})}:={({\overline{x}}_{0},\ldots,{\overline{x}}_{T},{\overline{u}}_{0},\ldots,{\overline{u}}_{T})}$ for some finite time interval ${\mathbb{Z}}_{\lbrack 0,T\rbrack}$, under the constraints in 2. The problem is given in 4. where $\mathcal{C}:{{{\mathbb{R}}^{{({T + 1})}n_{x}} \times {\mathbb{R}}^{{({T + 1})}n_{u}} \times {\mathbb{R}}^{n_{p}}}\rightarrow{\mathbb{R}}_{\geq 0}}$ specifies the performance objective. In 4, $T \in {\mathbb{N}}_{> 0}$ should be chosen large enough to reach the desired equilibrium condition. Ideally, the state ${\overline{x}}_{t}$ should converge to the origin for the current choice of $p$. Problem 4 is potentially non-convex since $\mathcal{C}$ may not be a convex function, and $\pi$ and $f$ may not be affine functions. In the following, for simplicity, we consider the case for some $Q_{x} \in {\mathbb{R}}^{n_{x} \times n_{x}}$ with $Q_{x} \succ 0$. Our method can easily be extended to more general cost functions as described in Subsection VII-C.

Before proposing an algorithmic solution to 4, we specify what class of policies $\pi$ we are interested , namely, model predictive control policies.

### III-B Model predictive control

In this paper, we restrict our attention to MPC policies, where the control input is chosen as the solution of an optimal control problem. Specifically, after measuring the current state ${\overline{x}}_{t}$, we use the knowledge we possess about the system 1 to optimize the future prediction of the state-input trajectories of the system.

The predicted trajectories, denoted $x_{t}:={(x_{0|t},\ldots,x_{N|t})} \in {\mathbb{R}}^{{({N + 1})}n_{x}}$ and $u_{t}:={(u_{0|t},\ldots,u_{N|t})} \in {\mathbb{R}}^{{({N + 1})}n_{u}}$, have finite length $N + 1$, where $N \in {\mathbb{N}}_{> 0}$, $N \ll T$, is the prediction horizon of the MPC. The initial state is chosen to be equal to the true state of the system, i.e., $x_{0|t} = {\overline{x}}_{t}$ and, to ensure convexity, we approximate the state dynamics as where $A_{t}$, $B_{t}$, and $c_{t}$ are known at runtime and should be chosen to accurately approximate the real dynamics 1 in the vicinity of ${\overline{x}}_{t}$. We use $S_{t}:={(A_{t},B_{t},c_{t})}$ to compactly represent the approximate dynamics at time $t$.

Each predicted state and input must satisfy the constraints 2. In addition, we generally impose different constraints on the predicted terminal state $x_{N|t}$, namely The objective function in the MPC is an approximation of the objective in 4, given by where we added a terminal penalty ${\| x_{N|t}\|}_{P}^{2}$ and a penalty on the input, with ${P,R_{u}} \succ 0$. The positive definiteness of $Q_{x}$, $R_{u}$, and $P$ ensures that the problem is strongly convex.

The MPC problem that is solved online at each time-step is therefore given as follows.

| | & {{k \in {\mathbb{Z}}_{\lbrack 0,{N - 1}\rbrack}},} \\ | | | At each time-step, after measuring ${\overline{x}}_{t}$ and obtaining $S_{t}$, we solve 7 and choose ${\pi{({\overline{x}}_{t},p)}} = u_{0|t}$, where $u_{0|t}$ is the first entry of the input trajectory. We use $\text{MPC}{({\overline{x}}_{t},S_{t},p)}$ to denote the function that maps a parameter $p$, a nominal system $S_{t}$, and an initial condition ${\overline{x}}_{t}$ to a control input ${\overline{u}}_{t} = u_{0|t}$, so that In this paper, we choose the terminal ingredients (i.e., the terminal cost and the terminal constraints) as tunable parameters, namely by letting $p:={(P,H_{x,N},h_{x,N})}$; however, we can, using the same math and algorithms, choose $p$ as any other element appearing in the cost or in the constraints of 7.

### III-C A projected gradient-based framework

In this section, we rewrite 4 considering the control policy given in 8 and then provide a simple gradient-based algorithm that can be used to solve such a problem. For simplicity, we assume that $S_{t} \equiv S$ and write simply $\text{MPC}{({\overline{x}}_{t},p)}$. We deal with the more complex case where $S_{t}$ is dynamically determined online in Subsection VII-A.

First, combining problem 4 with the cost function 5 and the policy in 7, we obtain the closed-loop control problem in 9. Note that we can remove the input constraints 2b in 4, as these are automatically satisfied if the inputs ${\overline{u}}_{t}$ are obtained from the MPC policy 7.

| | \underset{p}{\text{minimize}} & {\sum\limits_{t = 0}^{T}{\|{\overline{x}}_{t}\|}_{Q_{x}}^{2}} \\ | | | | | \text{subject to} & {{{\overline{x}}_{t + 1} = {f{({\overline{x}}_{t},{\text{MPC}{(p,{\overline{x}}_{t})}})}}},} \\ | | | | | & {{t \in {\mathbb{Z}}_{\lbrack 0,T\rbrack}},} \\ | | | | | & {{{\overline{x}}_{0}\text{~given}}.} | | | As shown in Appendix A, 9 can be compactly rewritten as follows.

| | \underset{p}{\text{minimize}} & {\mathcal{C}{({\overline{x}{(p)}})}} \\ | | | | | \text{subject to} & {{{\mathcal{H}{({\overline{x}{(p)}})}} \leq 0},} | | | where $\overline{x}{(p)}$ is the closed loop state trajectory generated by the dynamics 1 under the policy 8 for a given value of $p$. In the following section, we derive an efficient procedure to obtain gradients of the function $\mathcal{C}$ with respect to $p$. Since $\overline{x}$ is generally a nonsmooth function of $p$, we need to utilize a more general version of gradient that applies to nonsmooth functions.

## Conservative Jacobians

In the upcoming sections we repeatedly deal with the problem of minimizing a nonsmooth, nonconvex function. These problems admit a simple solution strategy based on a descent algorithm; however, because of the nonsmoothness, we cannot always guarantee the existence of a gradient. Luckily, we can still devise descent algorithms if the function is almost everywhere differentiable thanks to the concept of conservative Jacobian. This section describes how conservative Jacobians generalize the notion of gradient to functions that are almost everywhere differentiable.

An absolutely continuous curve, or path, is an absolutely continuous function $x:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{n}}$ which admits a derivative $\overset{˙}{x}$ for almost every $t \in {\lbrack 0,1\rbrack}$, and for which ${x{(t)}} - {x{}}$ is the Lebesgue integral of $\overset{˙}{x}$ between $0$ and $t$ for all $t \in {\lbrack 0,1\rbrack}$. Equipped with the definition of path, we can define the concept of conservative Jacobian.

### Definition 1 (\[15, Section 2\])

Given a locally Lipschitz function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$, we say that $f$ admits $\mathcal{J}_{f}:{{\mathbb{R}}^{n}\rightrightarrows{\mathbb{R}}^{m \times n}}$ as a conservative Jacobian, if $\mathcal{J}_{f}$ is nonempty-valued, outer semi-continuous, locally bounded, and for all paths $x:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{n}}$ and almost all $t \in {\lbrack 0,1\rbrack}$ it holds that A locally Lipschitz function $f$ that admits a conservative Jacobian $\mathcal{J}_{f}$ is called path-differentiable. If $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}^{n}}$ is a function of two arguments, say $p$ and $x$, we use $\mathcal{J}_{f,x}{(\overset{\sim}{p},\overset{\sim}{x})}$ to denote the conservative Jacobian of $f$ viewed as a function of $x$ and evaluated at $(\overset{\sim}{p},\overset{\sim}{x})$. Similarly, $\mathcal{J}_{f,p}{(\overset{\sim}{p},\overset{\sim}{x})}$ denotes the conservative Jacobian of $f$ as a function of $p$.

Conservative Jacobians extend the concept of gradient to nonsmooth almost everywhere differentiable functions. Moreover, the conservative Jacobian $\mathcal{J}_{f}$ coincides with the gradient ${\nabla_{x}f}{(x)}$ almost everywhere, that is, ${\mathcal{J}_{f}{(x)}} = {{\nabla_{x}f}{(x)}}$ a.e. on $x \in {\mathbb{R}}^{n}$ \[10, Theorem 1\]. Interested readers should refer to for a detailed treatment of conservative field theory for nonsmooth differentiation.

The most useful property that conservative Jacobian possess, which is also the reason why these mathematical objects were first introduced , is that they admit the chain rule definition 1. ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). This immediately implies the following composition rule.

### Lemma 1 (\[10, Lemma 6\])

Given two locally lipschitz and path-differentiable functions $f:{{\mathbb{R}}^{n_{x}}\rightarrow{\mathbb{R}}^{n_{p}}}$, $g:{{\mathbb{R}}^{n_{p}}\rightarrow{\mathbb{R}}^{n_{u}}}$, with conservative Jacobians $\mathcal{J}_{f}$ and $\mathcal{J}_{g}$, the function $f \circ g$ is path-differentiable with conservative jacobian ${\mathcal{J}_{f \circ g}{(x)}} = {\mathcal{J}_{g}{(x)}\mathcal{J}_{f}{({g{(x)}})}}$.

Unfortunately, not every locally Lipschitz function is path-differentiable. In this paper, we focus on a specific class of functions that always admit a conservative Jacobian, namely, semi-algebraic functions.

### Definition 2 (\[16, Definitions 2.1.4 and 2.2.5\])

A set $\mathcal{A} \subset {\mathbb{R}}^{n}$ is *semi-algebraic* if it can be written as where ${I,J} \in {\mathbb{N}}_{> 0}$ and for all $i,j$, the functions $P_{ij},Q_{ij}$ are polynomials. A function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is *semi-algebraic* if its graph is a semi-algebraic set, i.e., if $\{{{(x,v)} \in {\mathbb{R}}^{n_{x} + 1}}:{v = {f{(x)}}}\}$ is semi-algebraic.

As mentioned previously, semi-algebraic functions possess the following useful property.

### Lemma 2 (\[10, Proposition 2\])

Let $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be locally Lipschitz and semi-algebraic. Then $f$ admits a conservative Jacobian $\mathcal{J}_{f}$.

A crucial property recently shown in is that path-differentiable functions obey a nonsmooth version of the implicit function theorem.

### Lemma 3 (\[15, Theorem 2\])

Let $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}^{n}}$ be path-differentiable and let $\mathcal{J}_{f}$ be its conservative Jacobian. Suppose ${f{(\overset{\sim}{x},\overset{\sim}{p})}} = 0$ for some $\overset{\sim}{x} \in {\mathbb{R}}^{n}$ and $\overset{\sim}{p} \in {\mathbb{R}}^{p}$. Assume that $\mathcal{J}_{f}$ is convex and that for every ${\lbrack{UV}\rbrack} \in {\mathcal{J}_{f}{(\overset{\sim}{x},\overset{\sim}{p})}}$ the matrix $U$ is invertible. Then there exists a neighborhood ${{\mathcal{N}{(\overset{\sim}{x})}} \times \mathcal{N}}{(\overset{\sim}{p})}$ of $(\overset{\sim}{x},\overset{\sim}{p})$ and a path differentiable function $x:{{\mathcal{N}{(\overset{\sim}{p})}}\rightarrow{\mathcal{N}{(\overset{\sim}{x})}}}$ such that for all $p \in {\mathcal{N}{(\overset{\sim}{p})}}$ it holds that and the conservative Jacobian $\mathcal{J}_{x}$ of $x$ is given for all $p \in {\mathcal{N}{(\overset{\sim}{p})}}$ by Lemma 3. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") will play a major role in the remainder of this paper: specifically, we will use it to obtain the conservative Jacobian of the map MPC$({\overline{x}}_{t},p)$ with respect to both ${\overline{x}}_{t}$ and $p$.

Path-differentiable functions can be minimized using simple projected-gradient based scheme as outlined in Algorithm 1. ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation").

Algorithm 1 Minimization of path-differentiable functions Where we used $P_{\mathcal{P}}$ to denote the projector to the set $\mathcal{P}$. The following results demonstrates that, under certain conditions on the step-size ${\{\alpha_{k}\}}_{k \in {\mathbb{N}}}$, Algorithm 1. ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") is guaranteed to converge to a critical point of $f$.

### Lemma 4 (\[11, Theorem 6.2\])

Assume that $f$ is path-differentiable, that $\mathcal{P}$ is a polytopic set, and that the stepsizes ${\{\alpha_{k}\}}_{k \in {\mathbb{N}}} \subset {\mathbb{R}}_{> 0}$ satisfy Then $x^{k}$ as obtained via Algorithm 1. ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") converges to a critical point of $f$, i.e., a point $\overset{\sim}{x}$ for which $0 \in {\mathcal{J}_{f}{(\overset{\sim}{x})}}$.

## Differentiating the MPC policy

In this section we rewrite 7 in a more convenient form and then show that, under certain conditions, the map MPC$({\overline{x}}_{t},p)$ admits a conservative Jacobian. This Jacobian will later be used to devise a descent algorithm for 9. We begin by rewriting MPC$({\overline{x}}_{t},p)$ as a quadratic program in standard form.

### V-A Writing the MPC problem as a QP

The optimal control problem MPC$({\overline{x}}_{t},p)$ is a quadratic program. Following the procedure outlined in Appendix B, we can reformulate the problem in standard form as follows.

| | {\text{QP}{(\overline{p})}:\mspace{26mu}\operatorname{minimize}\limits_{y}} & {{\frac{1}{2}y^{\top}Q{(p)}y} + {q{({\overline{x}}_{t},p)}^{\top}y}} \\ | | | | | \text{subject to} & {{{F{(p)}y} \leq {f{(p,{\overline{x}}_{t})}}},} \\ | | | where we defined $\overline{p}:={({\overline{x}}_{t},p)}$ for simplicity. We denote with $n_{\text{in}}$ and $n_{\text{eq}}$ the number of inequality and equality constraints in 12, respectively.

Note that the parameter $p$ can potentially affect every element in the cost and in the constraints of QP$(\overline{p})$, whereas the initial condition ${\overline{x}}_{t}$ can only affect the linear parts of the cost and the constraints.

It theory, it would be possible to obtain the conservative Jacobian of the solution $y{(\overline{p})}$ of QP$(\overline{p})$ with respect to variations of $\overline{p}$, but this turns out to be unnecessarily complex because of the presence of $\overline{p}$ in the equality and inequality constraints. To greatly simplify the computation of the conservative Jacobian, we prefer to operate on the Lagrange dual problem associated to QP$(\overline{p})$. In this case, the constraints are parameter-independent, as $\overline{p}$ only affects the cost function of the problem.

Since our procedure involves computing the conservative Jacobian of the dual optimizer, we must ensure that the dual problem has a unique solution for every value of $\overline{p}$. To this end, we impose the following assumption.

### Assumption 1

For all parameter vectors $\overline{p}$ in some polytopic set $\mathcal{Y}$, the matrix $Q{(p)}$ in 12 is positive definite, problem 12 is feasible, and it satisfies the linear independence constraint qualification (LICQ).

Recall that problem 12 satisfies the LICQ if given a solution $y{(\overline{p})}$ of the problem, the rows $\mathbf{r}{(G,i)}$ of $G$ associated to the active inequality constraints (i.e., those vectors $v_{i} = {\mathbf{r}{(G,i)}^{\top}}$ for which ${v_{i}y{(\overline{p})}} = g_{i}$) and the rows $\mathbf{r}{(F,i)}$ of $F$ for $i \in {\mathbb{Z}}_{\lbrack 1,n_{\text{eq}}\rbrack}$ are linearly independent. Note that the LICQ assumption is always verified if, for example, the constraints on $x_{k|t}$ and $u_{k|t}$ in 7 are simple box constraints, i.e., given by for some ${x_{\text{min}},x_{\text{max}}} \in {\mathbb{R}}^{n_{x}}$, $x_{\text{min}} < x_{\text{max}}$, and ${u_{\text{min}},u_{\text{max}}} \in {\mathbb{R}}^{n_{u}}$, $u_{\text{min}} < u_{\text{max}}$.

The feasibility condition in Assumption 1 is quite restrictive in practical scenarios. We propose a simple extension of our method that can deal with losses of feasibility in Subsection VII-D.

Under Assumption 1, we can obtain the Lagrange dual of QP$(\overline{p})$ following the procedure outlined in Appendix C.

| | {\text{D}{(\overline{p})}:\mspace{26mu}\operatorname{minimize}\limits_{z}} & {{\frac{1}{2}z^{\top}H{(\overline{p})}z} + {h{(\overline{p})}^{\top}z}} \\ | | | | | \text{subject to} & {{{Ez} \geq 0}.} | | | Note that in D$(\overline{p})$, the parameters $p$ and ${\overline{x}}_{t}$ only affect the quadratic part $H$ and the linear part $h$ of the cost, whereas the matrix $E$ in the constraints is parameter-independent.

The primal solution $y{(\overline{p})}$ can be obtained from the dual solution ${z{(\overline{p})}} = {({\lambda{(\overline{p})}},{\mu{(\overline{p})}})}$ as

### V-B Writing the dual as fixed point condition

Our next objective is to synthesize a simple procedure to obtain the conservative Jacobian $\mathcal{J}_{z}$ of the dual optimizer $z$. Later, we will use $\mathcal{J}_{z}$ to obtain the conservative jacobian of the primal optimizer $y$ through 14.

To obtain $\mathcal{J}_{z}$, we follow the procedure proposed , namely, we write the optimality conditions of D$(\overline{p})$ as a fixed point equation ${\mathcal{F}{(z,\overline{p})}} = 0$, obtain the conservative Jacobian of $\mathcal{F}$ with respect to $z$ and $\overline{p}$, and apply the implicit function theorem described in Lemma 3. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). Under Assumption 1, we show that the invertibility condition in the statement of Lemma 3. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") is always verified even if the dual problem is not necessarily strongly convex.

Since D$(\overline{p})$ is a quadratic program, the following is a well known necessary and sufficient condition for optimality \[17, Theorem 3.67\]: where $N_{C}$ is the normal cone mapping of $C$ \[17, Example 3.5\]. Leveraging \[18, Corollary 27.3\], we have that 15 is equivalent to where $\gamma \in {\mathbb{R}}_{> 0}$ is a positive scalar, $C:={\{{z \in {\mathbb{R}}^{n_{z}}}:{{Ez} \geq 0}\}}$, and $P_{C}:{{\mathbb{R}}^{n_{z}}\rightarrow C}$ is the projector to the set $C$, with $n_{z} = {n_{\text{in}} + n_{\text{eq}}}$.

To obtain the conservative Jacobian of $\mathcal{F}$, we need $\mathcal{F}$ to be path-differentiable. This can be easily guaranteed with the following, mild, assumption.

### Assumption 2

The maps $Q{(p)}$, $q{(\overline{p})}$, $F{(p)}$, $f{(\overline{p})}$, $G{(p)}$, $g{(\overline{p})}$ are locally Lipschitz and semi-algebraic. $Q^{- 1}{(p)}$ is locally Lipschitz.

Leveraging Assumption 2, we have the following.

### Lemma 5

Under Assumptions 2 and 1, $\mathcal{F}$ is jointly path-differentiable in its arguments.

### Proof

The projector $P_{C}$ is given by where $P_{{\mathbb{R}}_{\geq 0}}:{{\mathbb{R}}\rightarrow{\mathbb{R}}_{\geq 0}}$ is the one-dimensional projector to the set of non-negative real numbers The function $P_{{\mathbb{R}}_{\geq 0}}$ is locally Lipschitz and convex, and therefore it is path-differentiable \[10, Proposition 2\]. We conclude that $P_{C}$ is path-differentiable since it is given componentwise by either linear functions ($\mu\mapsto\mu$), or path-differentiable functions ($P_{{\mathbb{R}}_{\geq 0}}$) \[10, Lemma 3\].

Next, the function $z\mapsto{z - {\gamma{({{H{(\overline{p})}z} + {h{(\overline{p})}}})}}}$ is differentiable in $z$, and therefore also path-differentiable in $z$. Moreover, thanks to Assumption 2, we have that both $H$ and $h$ are path-differentiable in $\overline{p}$, since they are constructed as products or sums of semi-algebraic functions (as shown in Appendix C), and these operations preserve both local-Lipschitzness and semi-algebraicity \[19, Corollary 2.9\]. Note that $Q^{- 1}{(p)}$ is also semi-algebraic since it is the inverse of a continuous semi-algebraic map \[19, Exercise 2.14\]. We conclude that $\overline{p}\mapsto{z - {\gamma{({{H{(\overline{p})}z} + {h{(\overline{p})}}})}}}$ is both locally Lipschitz and semi-algebraic in $\overline{p}$; therefore, it is path-differentiable in $\overline{p}$ thanks to Lemma 2. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation").

Since the composition of path-differentiable functions is path-differentiable \[10, Lemma 5\], we conclude that $\mathcal{F}$ is path-differentiable jointly in its arguments. ∎ The conservative Jacobian of the dual variable $z$ can now be readily obtained by applying the implicit function theorem in Lemma 3. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") to the map $\mathcal{F}$.

### Proposition 1

Under Assumptions 2 and 1, the optimizer $z{(\overline{p})}$ of D$(\overline{p})$ is unique and path differentiable for any $p \in \mathcal{Y}$. Its conservative Jacobian $\mathcal{J}_{z}{(\overline{p})}$ containts elements in the form ${- {U^{- 1}V}} \in {\mathcal{J}_{z}{(\overline{p})}}$, where

### Proof

### Remark 1

In practice, $J_{P_{C}}$ can be easily computed as See Remark 3 in Appendix D for more details. The simplicity of this computation is one of the primary reasons why the authors decided to work with the dual 13 instead of the primal 12.

The conservative Jacobian $\mathcal{J}_{y}{(\overline{p})}$ of the primal optimizer $y{(\overline{p})}$ can then easily be retrieved from $\mathcal{J}_{z}{(\overline{p})}$ using 14. For simplicity, define

### Proposition 2

Under Assumptions 2 and 1, the optimizer $y{(\overline{p})}$ of QP$(\overline{p})$ is unique and path differentiable for any $\overline{p} \in \mathcal{Y}$. Its conservative Jacobian $\mathcal{J}_{y}{(\overline{p})}$ contains elements in the form where $Z \in {\mathcal{J}_{z}{(\overline{p})}}$ and $W \in {\mathcal{J}_{\mathcal{G},\overline{p}}{(z,\overline{p})}}$.

### Proof

Follows immediately by applying the chain rule of differentiation to 14. ∎ The algorithm below outlines a procedure to compute the conservative Jacobians $\mathcal{J}_{\text{MPC},z}$ and $\mathcal{J}_{\text{MPC},p}$.

1:Solve D$(\overline{p})$ and get dual optimizers z = (λ, μ). 2:Compute ${\lbrack{UV}\rbrack} \in {\mathcal{J}_{\mathcal{F}}{(z,\overline{p})}}$ using 19. 3:Compute $Z = {- {U^{- 1}V}} \in {\mathcal{J}_{z}{({\overline{x}}_{t},p)}}$. 4:Compute an element of $\mathcal{J}_{y}{({\overline{x}}_{t},p)}$ using 20. 5:Extract $\mathcal{J}_{\text{MPC},{\overline{x}}_{t}}{({\overline{x}}_{t},p)}$ and $\mathcal{J}_{\text{MPC},p}{({\overline{x}}_{t},p)}$ from $\mathcal{J}_{y}{({\overline{x}}_{t},p)}$. Algorithm 2 Computing $\mathcal{J}_{\text{MPC}}{(\overline{p})}$ Notice that $\mathcal{J}_{\text{MPC},{\overline{x}}_{t}}$ and $\mathcal{J}_{\text{MPC},p}$ are contained in $\mathcal{J}_{y}$, and we can therefore retrieve them by selecting the appropriate entries in $\mathcal{J}_{y}{({\overline{x}}_{t},p)}$.

## Closed-loop optimization scheme

### VI-A Backpropagation

In the previous section, we showed how to compute the conservative Jacobian of the MPC map with respect to both the initial condition $x_{0}$, and the design parameter $p$. In this section, we build on this knowledge and describe a simple modular mechanism that can be used to obtain the conservative Jacobian of the entire closed loop trajectory $\overline{x}$ using the individual conservative Jacobians of each optimization problem.

The paradigm we employ, backpropagation, is far from unknown. In fact, this algorithmic invention had a huge impact in the field of machine learning and optimization. Backpropagation can be used to efficiently construct gradients with respect to design parameters of algorithms involving several successive steps. The idea is to compute the gradients of each step and combine them using the chain rule. This method eliminates redundant calculations, thus improving efficiency.

In our case, the closed loop dynamics can be expressed as a recursive equation where every state ${\overline{x}}_{t + 1}$ depends solely on its predecessor ${\overline{x}}_{t}$, and the design parameters $p$. To be able to propagate the conservative Jacobians through the dynamics of the system, we require $f$ to admit conservative Jacobians.

### Assumption 3

The function $f$ is locally Lipschitz and semi-algebraic.

Under Assumption 3, we can compute the conservative Jacobian $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p)}$ of the state ${\overline{x}}_{t + 1}$ with respect to the design parameters $p$ recursively as follows: Note that $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p)}$ depends on $\mathcal{J}_{{\overline{x}}_{t}}{(p)}$, and since ${\overline{x}}_{0}$ is given, we have ${\mathcal{J}_{{\overline{x}}_{0}}{(p)}} = 0$. As a result, we can easily construct an algorithm that computes the conservative Jacobian of the closed loop trajectory $\overline{x}$ for a given value of $p$ iteratively. The algorithm, summarized in Algorithm 3, can be implemented online, as the closed-loop is being simulated and the values of ${\overline{x}}_{t}$ are being measured.

4: Compute $\mathcal{J}_{\text{MPC}}{({\overline{x}}_{0},p)}$ using Alg. 2. 5: Compute $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p)}$ using 21. 8:Return ${\mathcal{J}_{\overline{x}}{(p)}}:={({\mathcal{J}_{{\overline{x}}_{0}}{(p)}},{\mathcal{J}_{{\overline{x}}_{1}}{(p)}},\ldots,{\mathcal{J}_{{\overline{x}}_{T}}{(p)}})}$.

The next result formalizes the ideas expressed in this section.

### Proposition 3

Under Assumptions 2, 1 and 3, Algorithm 3 produces the conservative Jacobian $\mathcal{J}_{\overline{x}}{(p)}$ of the closed-loop trajectory $\overline{x}$ for any $p$.

### Proof

We use induction. First, ${\mathcal{J}_{{\overline{x}}_{0}}{(p)}} = 0$ since ${\overline{x}}_{0}$ is fixed *a priori*. Next, suppose $\mathcal{J}_{{\overline{x}}_{t}}{(p)}$ has been computed correctly by the algorithm. The correctness of $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p)}$ follows immediately 21 and Lemma 1. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). This concludes the proof. ∎

### VI-B Optimization algorithm

Once the conservative Jacobian is available, we can utilize it to update the parameter $p$ with a gradient-based scheme. To guarantee convergence to a local minimum, it suffices to meet the conditions of Algorithm 1. ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). We therefore choose the following update scheme for any $J = {J_{1}J_{2}}$ with where ${\overline{x}}^{k} = {\overline{x}{(p^{k})}}$, and where $\alpha_{k}$ satisfies the conditions in 11. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"). The overall algorithm, that combines all the steps we describes so far, is given below.

6: Solve ${MPC}{({\overline{x}}_{t},p^{k})}$. 7: Compute $\mathcal{J}_{\text{MPC}}{({\overline{x}}_{t},p^{k})}$ using Alg. 2. 8: Compute $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p^{k})}$ using 21. 11: Store closed-loop ${\overline{x}}^{k}$. 12: Compute $J_{1} \in {\mathcal{J}_{\overline{x}}{(p^{k})}}:={({\mathcal{J}_{{\overline{x}}_{0}}{(p^{k})}},\ldots,{\mathcal{J}_{{\overline{x}}_{T}}{(p^{k})}})}$. 13: Compute J = J1 J2 with $J_{2} \in {\mathcal{J}_{\mathcal{C}}{({\overline{x}}^{k})}}$. Algorithm 4 Closed-loop optimization scheme As long as the map MPC$(\overline{p})$ is well-defined, i.e., the problem MPC$(\overline{p})$ admits a feasible solution throughout the entirety of the execution of Algorithm 4, we have the following.

### Theorem 1

Suppose Assumptions 3, 2 and 1 hold, and that MPC$(\overline{p})$ is feasible for all ${\overline{x}}_{t}$ and $p^{k}$ as setup in Algorithm 4. Then if $\alpha_{k}$ satisfies 11. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation"), $p^{k}$ is guaranteed to converge to a critical point of problem 4.

### Proof

Since $\mathcal{J}_{\overline{x}}{(p^{k})}$ is the conservative Jacobian of $\overline{x}$ with respect to the design parameter $p$ thanks to Proposition 3, we have from Lemma 4. ‣ Definition 1 ([15, Section 2]). ‣ IV Conservative Jacobians ‣ BP-MPC: Optimizing Closed-Loop Performance of MPC using BackPropagation") that the iterates $p^{k}$ are guaranteed to converge to a critical point $\overline{p}$ of the problem Moreover, since the constraints ${\mathcal{H}{({\overline{x}}_{0},p)}} \leq 0$ are automatically satisfied if MPC$(\overline{p})$ is feasible throughout the entire runtime of Algorithm 4, we conclude that the critical point $\overline{p}$ of 23 is also a critical point of 10, which is equivalent to 4. This concludes the proof. ∎

## Extensions

### VII-A Choosing $S_{t}$

The approximate model, denoted $S_{t}$, heavily impacts the control performance, where an accurate model results in better performance. Generally, since the control scheme is deployed in receding horizon (that is, the optimization is repeated at every time-step and only the first entry $u_{0|t}$ of the optimal input trajectory is applied), we only require accurate knowledge of the system locally, in the vicinity of the current state ${\overline{x}}_{t}$. We present here three progressively more accurate choices of $S_{t}$.

### VII-A1 Linearization at a single equilibrium point

The easiest choice is to consider a time-invariant model $S_{t} \equiv S$, where $S$ is obtained by linearizing $f$ at some equilibrium point $(\hat{x},\hat{u})$ (i.e., a point satisfying ${f{(\hat{x},\hat{u})}} = 0$). Specifically, we choose $S = {(A,B,0)}$ with This choice of model provides satisfactory performance as long as the system does not deviate significantly from the equilibrium position, a fact that can be observed by expanding the first-order Taylor series of $f$ around $(\hat{x},\hat{u})$: which yields an approximation error that scales linearly with the distance of $(x,u)$ from $(\hat{x},\hat{u})$: Note that in the computation of $S$ and in the Taylor expansion we implicitly assumed that $f$ is continuously differentiable, a stronger assumption than the one in Assumption 3. If $f$ is not continuously differentiable, we can still utilize this approach by choosing $A$ and $B$ in some other way (in this case however the error bound 24 may fail to hold).

Despite its simplicity, linearizing at a single equilibrium point is quite common in the MPC literature and has proved to be successful in many application scenarios, in particular when the control objective is to maintain the state of the system at some desired steady state.

### VII-A2 Linearization at the current state

A more accurate approach, that is generally more effective in reference tracking problems, is to update the model based on the current state of the system. Ideally, we would like to construct $S_{t}$ by linearizing $f$ at the current state and input $({\overline{x}}_{t},{\overline{u}}_{t})$. However, ${\overline{u}}_{t}$ is not known until after we find a solution to MPC$(\overline{p})$, and in fact $S_{t}$ plays a role in determining ${\overline{u}}_{t}$. An implementable solution is to replace ${\overline{u}}_{t}$ with $u_{1|{t - 1}}$, that is, with the second entry of the optimal input trajectory computed at time-step $t - 1$. In this way we obtain: The approximation error between the real dynamics and the linearized dynamics can be computed by considering the Taylor expansion of $f$ around $({\overline{x}}_{t},u_{1|{t - 1}})$ If the input state trajectory $(x_{t},u_{t})$ predicted by the MPC at time $t$ does not deviate significantly from $({\overline{x}}_{t},u_{1|{t - 1}})$, then from 25 we can conclude that the linearized dynamics represent a good approximation of the system.

The variable $u_{1|{t - 1}}$ is itself dependent on both ${\overline{x}}_{t - 1}$ and $p$ (it is part of the optimizer of $\text{MPC}{({\overline{x}}_{t - 1},p)}$), we therefore need to adapt the backpropagation scheme in 21 to account for this fact. We present the updated algorithm in the next section, where we deal with a more general choice of $S_{t}$.

### VII-A3 Linearization along a trajectory

We can achieve even better accuracy by allowing the nominal dynamics to vary across different time-steps within the same MPC problem, that is, by setting Following the strategy above, we can choose each $A_{k|t}$, $B_{k|t}$, and $c_{k|t}$ to be the linearization of $f$ and the approximation error evaluated along the state input-trajectory $(x_{t - 1},u_{t - 1})$: Alternatively, we can use ${\overline{x}}_{t}$ instead of $x_{1|{t - 1}}$. If the decision variables in the MPC problem at time $t - 1$ do not include $u_{N|{t - 1}}$, we can obtain $A_{N - {1|t}}$ by linearizing at $(x_{N|{t - 1}},u_{N - {1|{t - 1}}})$. This strategy is commonly refered as successive linearization in the MPC literature.

Choosing the model with successive linearization, we have that $S_{t}$ depends on the entire solution $y_{t - 1}:={(x_{t - 1},u_{t - 1})}$ of the MPC problem at time $t - 1$, and possibly also on ${\overline{x}}_{t}$. This needs to be taken into account when computing the conservative Jacobian in Algorithm 3. Specifically, the map MPC$({\overline{x}}_{t},p)$ should more correctly be defined as $\text{MPC}{({\overline{x}}_{t},y_{t - 1},p)}$, highlighting the dependency on $y_{t - 1}$. We therefore have where the difference from 21 is the additional term $\mathcal{J}_{\text{MPC},y_{t - 1}}{({\overline{x}}_{t},y_{t - 1},p)}\mathcal{J}_{y_{t - 1}}{(p)}$ which accounts for the dependency of $y_{t - 1}$ on $p$. The term $\mathcal{J}_{y_{t - 1}}{(p)}$ needs to be constructed using a backpropagation algorithm. Defining $y_{t - 1} = {{QP}{({\overline{x}}_{t - 1},y_{t - 2},p)}}$, where the map $QP$ is the same one defined in 12 with the addition of the parameter $y_{t - 2}$, we have Before beginning the simulation of the system, we need to fix a linearization trajectory $y_{- 1}$ for time-step $t = 0$. Naturally, we cannot utilize any previous MPC solution, since $t = 0$ is the first time-step at which we solve the MPC problem. We can choose $y_{- 1}$ either as a fixed and pre-defined trajectory, or let $y_{- 1}$ be part of $p$, thus allowing the optimization process select the value of $y_{- 1}$ that yields the best closed-loop performance.

Below, we provide an algorithmic implementation of the linearization strategy described in paragraphs 2) and 3) of this section.

4: Compute $\mathcal{J}_{\text{MPC}}{({\overline{x}}_{t},y_{t - 1},p)}$ using Alg. 2. 6: Compute $\mathcal{J}_{{\overline{x}}_{t + 1}}{(p)}$ using 26. 9:Return ${\mathcal{J}_{\overline{x}}{(p)}}:={({\mathcal{J}_{{\overline{x}}_{0}}{(p)}},{\mathcal{J}_{{\overline{x}}_{1}}{(p)}},\ldots,{\mathcal{J}_{{\overline{x}}_{T}}{(p)}})}$. Algorithm 5 Backpropagation with linearization Note that we can still employ Algorithm 2 to compute $\mathcal{J}_{\text{MPC}}$ by simply redefining $\overline{p}:={({\overline{x}}_{t},y_{t - 1},p)}$.

### VII-B State-dependent cost and constraints

The closed-loop performance of receding-horizon MPC schemes can be greatly improved by allowing certain elements in the MPC problem to be dependent on the current state of the system. For example, , the authors construct terminal ingredients (cost and constraints) online, utilizing knowledge of the measured state of the system ${\overline{x}}_{t}$. They then demonstrate that this approach enlarges the region of attraction of the scheme.

Our backpropagation framework easily allows to incorporate initial state-dependent elements in the MPC problem. For example, we can choose $H_{x,N}$, $h_{x,N}$, and $P$ to be functions of both $p$ and ${\overline{x}}_{t}$. In this case, problem 7 becomes | | & {{k \in {\mathbb{Z}}_{\lbrack 0,{N - 1}\rbrack}},} \\ | | | | | \text{parameters:} & {{{(H_{x,N},h_{x,N},P)} \sim {({\overline{x}}_{t},p)}},} \\ | | | where $A \sim B$ means that $A$ is a function of $B$. Note that once ${\overline{x}}_{t}$ is available, the state-dependent elements $H_{x,N}$, $h_{x,N}$, and $P$ can be computed explicitly, meaning that the MPC problem we solve at runtime continues to be a quadratic program. The same procedure can be applied to the case where $H_{x}$, $H_{u}$, $h_{x}$, $h_{u}$, or even the cost matrices $Q$ and $R$ are dependent on ${\overline{x}}_{t}$. We leave such cases for future work and emphasize that our framework is flexible to tune almost any component of the underlying MPC problem.

The MPC problem considered so far, i.e., 7, was already dependent on ${\overline{x}}_{t}$, which affected the initial state $x_{0|t}$ of the problem. The difference with 28 is that, in the latter, ${\overline{x}}_{t}$ not only affects $x_{0|t}$, but also other optimization variables through the effect on $H_{x,N}$, $h_{x,N}$, and $P$. Note, however, that 28 can be written as a quadratic program in the form | | \operatorname{minimize}\limits_{y} & {{\frac{1}{2}y^{\top}Q{({\overline{x}}_{t},p)}y} + {q{({\overline{x}}_{t},p)}^{\top}y}} \\ | | | | \text{subject to} & {{{F{({\overline{x}}_{t},p)}y} \leq {f{({\overline{x}}_{t},p)}}},} \\ | | which differs from QP$(\overline{p})$ as given in Subsection V-A only because $Q$, $F$, and $G$ now depend on both ${\overline{x}}_{t}$ and $p$. As a result, we can perform closed-loop optimization using the same algorithmic procedure as in Algorithm 4 without any modification, exception made for the symbolic expression of $Q$, $F$, and $G$ which now depend on $\overline{p} = {({\overline{x}}_{t},p)}$ instead of only $p$.

### Remark 2

Using the technique outline above, one can easily incorporate cost matrices $Q_{x}$ and $R_{u}$ that also depend on $y_{t - 1}$, for example by linearizing the possibly nonlinear cost function $\mathcal{C}$ along the trajectory $y_{t - 1}$ and adding sufficient regularization to ensure the positive definiteness of both $Q_{x}$ and $R_{u}$.

### VII-C Non-convex cost

Our framework easily extends to scenarios where the quadratic cost in 4 is replaced with more sophisticated costs that can possibly involve other terms in addition to $\overline{x}$. Consider, for example, the following problem | | \underset{p\in\mathcal{X}}{\text{minimize}} & {\mathcal{C}{(\overline{x},y,z,p)}} \\ | | | | | \text{subject to} & {{{(y_{t},z_{t})} \sim {{MPC}{({\overline{x}}_{t},y_{t - 1},p)}}},} \\ | | | | | & {{t \in {\mathbb{Z}}_{\lbrack 0,T\rbrack}},} \\ | | | | | & {{{\overline{x}}_{0},y_{- 1},{z_{- 1}\text{given}}},} | | | where $y:={(y_{0},\ldots,y_{T})}$ and $z = {(z_{0},\ldots,z_{T})}$ represent the collection of all the primal-dual optimizers of MPC. The matrix $I_{u}$ selects from $y_{t}$ the entry corresponding to $u_{0|t}$. Note that we can include any of the optimization variables in the cost and still manage to efficiently compute the gradient of the objective by storing the conservative Jacobians $\mathcal{J}_{y_{t}}{(p)}$ and $\mathcal{J}_{z_{t}}{(p)}$ and then applying the Leibniz rule The conservative Jacobians $\mathcal{J}_{y}$ and $\mathcal{J}_{z}$ are already available as a by-product of Algorithm 2.

To ensure that Lemma 5 is still applicable, we only require $\mathcal{C}$ to be path-differentiable jointly in its arguments. Under this condition, the results of Theorem 1 still hold. Note that the class of path-differentiable functions is quite large, and comprises a large selection of non convex functions.

### VII-D Dealing with infeasibility

So far, we did not concern ourselves with the situation where 7 does not admit a feasible solution. This can happen frequently in practice, since the gradient-based optimization scheme is modifying the behavior of MPC$({\overline{x}}_{t},p)$, without any guarantees that the resulting closed-loop will produce states ${\overline{x}}_{t}$ for which MPC$({\overline{x}}_{t},p)$ admits a solution. There is, however, a simple procedure that can be used to recover from infeasible scenarios by leveraging the formulation in 29. The modification comprises two steps: first we need to modify MPC$({\overline{x}}_{t},p)$ to ensure its feasibility, then we change the cost function $\mathcal{C}$ to ensure that $p$ is chosen to minimize constraint violations.

First of all, we need to modify MPC$({\overline{x}}_{t},p)$ to ensure that the optimization problem admits a solution for every value of ${\overline{x}}_{t}$ and $p$. In MPC$({\overline{x}}_{t},p)$, the input constraints can always be satisfied, since $u_{t}$ is a decision variable. The problematic constraints are only those involving the state variable $x_{t}$. We reformulate 7 by introducing new optimization variables (namely, $\epsilon_{t}$) that relax the state constraints.

| | \operatorname{minimize}\limits_{x_{t},u_{t},\epsilon_{t}} & {{P_{\epsilon}{(\epsilon_{t})}} + {\| x_{N|t}\|}_{P}^{2} + {\sum\limits_{k = 0}^{N - 1}{\| x_{k|t}\|}_{Q}^{2}} + {\| u_{k|t}\|}_{R}^{2}} \\ | | | | | & {{k \in {\mathbb{Z}}_{\lbrack 0,{N - 1}\rbrack}},} \\ | | | To avoid unnecessary constraint violation, we penalize nonzero values of $\epsilon_{t}$ with the penalty function $P_{\epsilon}$, chosen as for some ${c_{1},c_{2}} > 0$. If $c_{2}$ is large enough, one can prove that $P_{\epsilon}$ is an exact penalty function.

### Lemma 6 (\[23, Theorem 1\])

Problem 30 has the same solution as 7 as long as 7 admits a solution and $c_{2} > {\|\lambda\|}_{\infty}$, where $\lambda$ are the multipliers associated to the inequality constraints affecting the state in 7.

We use ${(y_{t},u_{0|t},\epsilon_{t})} \sim {{MPC}{({\overline{x}}_{t},y_{t - 1},p)}}$ to denote that the variables $(y_{t},u_{0|t},\epsilon_{t})$ are obtained from the solution of the optimization problem ${MPC}{({\overline{x}}_{t},y_{t - 1},p)}$ described in 30. Moreover, since 30 is a quadratic program satisfying Assumptions 1 and 2, we can follow the strategy outlined in Algorithm 2 to compute the conservative Jacobians $\mathcal{J}_{y_{t}}$, $\mathcal{J}_{u_{0|t}}$, and $\mathcal{J}_{\epsilon_{t}}$, which are now functions of the variables ${\overline{x}}_{t}$, $y_{t - 1}$, and $p$.

The modification proposed in 30 ensures that the MPC problem always has a feasible solution. However, this is not enough: we also need to modify the objective function $\mathcal{C}$ in 29 to ensure that, if possible, $p$ is chosen to have zero constraint violations. This can be accomplished by introducing a penalty function in the objective of 29: | | \text{minimize} & {{\sum\limits_{t = 0}^{T}{\|{\overline{x}}_{t}\|}_{Q}^{2}} + {\mathcal{P}_{\epsilon}{(\epsilon)}}} \\ | | | | | \text{subject to} & {{{(y_{t},u_{0|t},\epsilon_{t})} \sim {{MPC}{({\overline{x}}_{t},y_{t - 1},p)}}},} \\ | | | | | & {{{\overline{x}}_{0},{y_{- 1}\text{given}}},} \\ | | | | | & {{t \in {\mathbb{Z}}_{\lbrack 0,T\rbrack}},} | | | where $\epsilon:={(\epsilon_{0},\ldots,\epsilon_{T})}$ and for some $c_{3} > 0$. The introduction of $\mathcal{P}_{\epsilon}$ should ensure that the solution of 32 satisfies $\epsilon_{t} = 0$ for all $t \in {\mathbb{Z}}_{\lbrack 0,{T - 1}\rbrack}$. If this is the case, the optimizers $x_{t}$ and $u_{t}$ of each MPC problem 30 satisfy the nominal constraints 2, thus ensuring that $\overline{x}$ and $\overline{u}$ do too.

With some reformulation, we can equivalently write 32 as where $\mathcal{C}$ and $\epsilon$ are locally Lipschitz functions of $p$, and $\epsilon$ is the function that maps $p$ to the value of $\epsilon$ that solves 32. To ensure closed-loop constraint satisfaction, we would like to solve problem 34 with the additional condition that ${\epsilon{(p)}} = 0$: | | \underset{p}{minimize} & {\mathcal{C}{(p)}} \\ | | | | | \text{subject to} & {{{\epsilon{(p)}} = 0}.} | | | Under certain conditions on $\mathcal{P}_{\epsilon}$ and on the nature of the minimizers of 35, we can prove that 34 and 35 are equivalent. For this, we need the following definition.

### Definition 3

Let $p^{\ast}$ be such that ${\epsilon{(p^{\ast})}} = 0$. Problem 35 is calm at $p^{\ast}$ if there exists some $\overline{\alpha} \geq 0$ and some $\epsilon > 0$ such that for all $(p,u)$ with ${\|{p - p^{\ast}}\|} \leq \epsilon$ and ${\epsilon{(p)}} = u$, we have Calmness is a rather weak regularity condition that is verified in many situations. In finite dimensions, it holds for a dense subset of the perturbations \[24, Proposition 2.1\]. For calm minimizers of 34, we have the following.

### Proposition 4

\[24, Theorem 2.1\] The set of local minima $p^{\ast}$ of 35 for which 35 is calm at $p^{\ast}$ coincide with the local minima of 34 provided that the penalty parameter $c_{3}$ in 33 is chosen at least as large as the calmness modulus.

Generally, it may be challenging to obtain an accurate estimate of the calmness module. Nevertheless, for practical purposes, a large enough value of $c_{3}$ tipically produces the desired effect $\epsilon = 0$.

With this in mind, we can use Algorithm 4 replacing $\mathcal{C}$ with $\mathcal{C} + \mathcal{P}_{\epsilon}$ and the MPC problem 7 with 30. If $c_{2}$ and $c_{3}$ are chosen sufficiently large, and under the calmness assumption in Proposition 4, we can guarantee convergence to a critical point of the problem with constraints 35.

## Simulation example

All simulation are done in CasADi with the active set solver qpOASES on a laptop with $32$ GB of RAM and an Intel(R) Core (TM) processor i7-1165G7 @ 2.80GHz. The code is available and open source^11^1At the link Table I shows the average computation time for each closed-loop iteration for all simulation examples.

Loss of feasibility with penalty (ρ = 0.1, η = 1) Table I: Average computation times per iteration

### VIII-A Linear example

We begin by deploying our optimization scheme to solve problem 9 for a double integrator with ${\overline{x}}_{0} = {}$ and with the constraints The closed loop objective is to minimize with $Q_{x} = I$ and $R_{u} = 10^{- 4}$. The MPC utilizes the same cost matrices $Q_{x}$ and $R_{u}$, moreover, we parameterize the terminal cost $P$ in 7 as and choose $p = {(p_{1},p_{2},p_{3})}$. Note that this choice of $P$ ensures $P \succ 0$ for all $p$. The initial design is $p^{0} = {(0.1,0,0.1)}$. We choose a very short horizon of $N = 5$.

We choose the stepsize as where $\eta \in {(0.5,1\rbrack}$ and $\rho > 0$ are design parameters. Since the term $k$ in the denominator eventually dominates, this choice of stepsizes fullfills the assumptions in Theorem 1 for any $\eta \in {(0.5,1\rbrack}$ and $\rho > 0$, and the iterates ${\{ p^{k}\}}_{k \in {\mathbb{N}}}$ are therefore guaranteed to converge to a critical point of 9.

Figure 1 shows the evolution of the difference between the best achievable tracking cost and the current closed-loop cost incurred by 7 in percentage as the number of iterations grow (for different values of $\rho$ and $\eta$). In other words, we plot the quantity ${({\mathcal{C}_{k} - \mathcal{C}^{\ast}})}/\mathcal{C}^{\ast}$, where $\mathcal{C}_{k}$ is the closed-loop cost at iteration $k$ and $\mathcal{C}^{\ast}$ is the best achievable closed-loop cost, obtained by using an MPC controller with a control horizon longer than $30$ time steps (time after which the system reaches the origin). Note how the difference between $\mathcal{C}_{k}$ and $\mathcal{C}^{\ast}$ is negligible (less than $0.001\%$) after only a few iterations in both cases.

Figure 2 shows the closed-loop trajectories of the states and the input under different control policies. In violet we can see the trajectory under 7 without any closed loop optimization with $p_{1} = p_{3} = 0.1$ and $p_{2} = 0$. In orange, the MPC has been optimized in closed loop for $200$ iterations. Note that this trajectory coincides with the one produced by the best available controller, plotted in blue.

The best achievable performance $\mathcal{C}^{\ast} = \mathcal{C}^{200} = 5249.13$ is attained with parameter This parameter choice produces better performance than the one obtained with $P$ chosen as the solution of the discrete time Riccati equation, i.e., which yields a closed-loop cost of $5252.37$.

Figure 1: Percentage difference between closed-loop cost and best achievable cost over different iterations for double integrator dynamics.

Figure 2: Comparison of closed-loop state and input trajectories for double integrator dynamics.

### VIII-B Nonlinear example

We now deploy our scheme to the following nonlinear system with ${\overline{x}}_{0} = {}$, with constraints and with the same objective 36. We use the linearization strategy described in Subsection VII-A3 and choose an even shorter horizon $N = 3$. We use the same parameterization and update rule as in Subsection VIII-A.

Figure 3 compares the performance of 7 at iteration $0$ and iteration $200$ against the best possible control action, namely, any nonlinear MPC controller with horizon larger than $30$. Note from Figure 4 how the difference in performance goes from about $35\%$ to less than $0.1\%$ after less than $25$ iterations (for $\eta = 0.6$).

Figure 3: Comparison of closed-loop state and input trajectories for nonlinear dynamics.

Figure 4: Percentage difference between closed-loop cost and best achievable cost over different iterations for nonlinear dynamics.

### VIII-C Loss of feasibility example

In this section we consider the same system and cost as in Subsection VIII-B with tighter constraints In this case, the MPC problem quickly becomes infeasible; therefore, we utilize the soft-constrained version in 30 with penalty parameters $c_{1} = 1$ and $c_{2} = 10$. By applying the same optimization scheme as in Subsection VIII-B, with cost as in 36, we obtain the trajectories in Figure 5.

Figure 5: Comparison of closed-loop state and input trajectories for double nonlinear dynamics with more strict state constraints. Note how the closed-loop fails to satisfy the state constraints at iteration 300.

Note that after $300$ iterations the closed-loop trajectory has converged to a steady-state where constraints are violated (in particular, the constraint on the second entry of the state is not satisfied between time-step $4$ and $8$). This is not surprising since the upper-level objective function $\mathcal{C}$ does not include any information about constraint violation. The closed loop cost after $300$ iteration is $\mathcal{C}_{300} = 347.076$, which is significantly smaller than the best achievable cost (with constraint satisfaction), equal to $\mathcal{C}^{\ast} = 353.266$. The value of $p$ after $300$ iterations is If we use the objective function in 34 with ${P_{\epsilon}{(\epsilon)}} = {200\mathbf{1}^{\top}\epsilon}$ (where $\epsilon:={(\epsilon_{1},\epsilon_{2},\ldots,\epsilon_{T})}$ contains the slack variables of all the optimization problems, each of which spans $N$ time-steps, and $\mathbf{1}$ is the vector of all ones), we obtain the trajectory in Figure 6, where the constraints are satisfied and $\epsilon = 0$. In this case, the effect of a penalty on the constraint violation induces the optimization algorithm to favor values of $p$ that maintain small constraint violations. This happens at the cost of a worse closed-loop performance, which becomes now equal to the best safe performance $\mathcal{C}^{\ast}$. The final value of $p$ is also different: Figure 6: Comparison of closed-loop state and input trajectories for double nonlinear dynamics with more strict state constraints and with penalization of the constraint violation. The penalty on the constraint violation ensures that the MPC at iteration 300 satisfies the state constraints.

## Conclusion

In this paper, we proposed a backpropagation algorithm to optimally design an MPC scheme to maximize closed-loop performance. The cost and the constraints in the MPC can depend on the current state of the system, as well as on past solutions of previous MPC problems. This allows, for example, the utilization of the successive linearization strategy.

We employed conservative Jacobians to compute the sensitivity of the closed-loop trajectory with respect to variations of the design parameter. Leveraging a non-smooth version of the implicit function theorem, we derived sufficient conditions under which the gradient-based optimization procedure converges to a critical point of the problem.

We extended our framework to cases where the MPC problem becomes infeasible using nonsmooth penalty functions. We derived conditions under which the closed-loop is guaranteed to converge to a safe solution.

Current work focuses on deploying our optimization scheme on more realistic real-life examples. Future work will focus on extending our scheme to scenarios where the system dynamics are only partially known and / or affected by stochastic noise.
