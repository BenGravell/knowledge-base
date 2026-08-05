<!-- arxiv-full-text:v1 {"arxiv_id": "2307.07086", "source": "ar5iv"} -->

## Introduction

We consider convex approximate dynamic programming (ADP) policies for convex stochastic control problems, which involve systems with known random linear dynamics and convex stage costs. Evaluating an ADP policy reduces to solving a convex optimization problem involving a convex approximate value function. We focus on fitting quadratic approximate value functions, and refer to the associated policies as quadratic approximate dynamic programming (QADP) policies. While QADP policies are optimal for problems with convex quadratic stage cost \[, \], they can also serve as effective heuristics for other problem types. It has been observed that ADP policies can perform well even when using imperfect approximations of the true value function \[ \].

In this work, we propose an approximate value iteration method for finding quadratic approximate value functions for convex stochastic control problems, which we refer to as *value-gradient iteration* (VGI). In principle, an optimal value function may be found by iterating the Bellman operator, which maps real-valued functions on the state space to real-valued functions on the state space. Since it is not possible in general to exactly represent functions on $\text{R}^{n}$, we incorporate a function approximation step after each application of the Bellman operator, a general approach called fitted value iteration (FVI). In our proposed VGI, instead of directly fitting the value function, we fit the gradient of the value function with respect to the state vector.

It is sufficient to approximate the gradient since constant offsets in the value function have no impact on the associated ADP policy. In addition, the gradient of the value function carries more information than the value function itself \[, \]. If the gradient is well approximated at a set of states, then the value function is also well approximated locally around those states, up to an additive constant which does not affect the policy. However, having a good approximation of only the value at a set of states does not imply that the value function is well approximated locally around those states.

Most importantly, VGI is practical to implement for QADP. We show that, when it exists, the gradient of the Bellman operator applied to a convex quadratic function can be obtained at any state by evaluating a particular optimal dual variable associated with the QADP policy. Since the gradient of a convex quadratic is an affine function, in each iteration we fit an affine function to a set of pairs of states and value-gradients. This fitting problem is a convex optimization problem. Therefore, VGI involves solving a sequence of convex optimization problems, which can be carried out reliably.

We also consider several techniques for enhancing the reliability of VGI, including damping, a robust Huber fitting loss, and the incorporation of prior knowledge constraints and regularization. VGI remains effective even when the state space dimension is large relative to the number of fitting samples, as we will demonstrate with several numerical examples. Finally, we note that the computational effort of obtaining a good QADP policy using VGI is small enough that it is comparable to that of simply evaluating the policy through simulation.

### Related work

### Dynamic programming

Dynamic programming (DP) provides techniques for computing the optimal value function and policy for general Markov decision processes. The optimal policy is evaluated by solving an optimization problem, where the control is chosen by minimizing the current stage cost plus the expected value function at the next state. For convex stochastic control problems, this is a convex optimization problem \[ \]. However, it is possible to exactly represent and find the value function in a only few special cases, for example when the state space is discrete, or when we have a convex stochastic control problem with a convex extended quadratic stage cost.

### Approximate dynamic programming

ADP \[ \] methods are heuristics used in stochastic control when the problem cannot be solved by applying DP directly. Typically, these methods either approximate the value function in DP or tune the parameters of a parametric policy. In some contexts, approximate value functions are known as control Lyapunov functions \[, \].

One approach to ADP is to approximate the value function by relaxing the Bellman equation to an inequality, and then solving a convex optimization problem involving a model of the dynamics and stage cost. When the state and input spaces are finite, this leads to a linear program (LP). When the dynamics are affine, the stage cost is quadratic, and the input is constrained to be in a convex set, quadratic approximate value functions can be obtained using semidefinite programming \[, \]. In both cases, the resulting approximate value functions are lower bounds on the true value function.

Other value function approximation methods search for an approximate value function that satisfies the Bellman equation along simulated trajectories. This includes the method proposed in this paper, which is closely related to fitted (or projected) value iteration \[ \]. Other methods, which do not assume that a model of the dynamics and stage cost are available, include $Q$-iteration \[, \], $Q$-learning \[, \], and temporal difference learning \[, \].

Instead of approximating the value function, other ADP techniques directly optimize the parameters of a parametric policy to improve performance along system trajectories. Stochastic gradient descent and its variants have been employed to tune convex optimization control policies and controllers based on Proportional-Integral-Derivative (PID) control \[, ÅHHH93\] and model predictive control (MPC) \[, AJS^+^18\]. Policy gradient methods provide a method for differentiating through policies parametrized by neural networks \[MBM^+^16, SWD^+^17\].

### Reinforcement learning

Reinforcement learning (RL) methods \[, \] can be considered a form of approximate dynamic programming (ADP), although their primary focus is on learning from interactions with the system or a simulator, rather than relying on explicit mathematical models of the system dynamics or stage cost. In this work, we assume that models of the dynamics and stage cost are either known or have been estimated or learned beforehand. This is similar to some model-based RL methods that learn a policy and a model of the dynamics jointly \[, \]. In the context of control, the process of learning the dynamics is typically referred to as system identification.

### Value gradients

When considering a differentiable approximate value function, it is advantageous to have accurate approximations of its derivatives with respect to the state, i.e., the value gradient. If the value gradient is well-approximated along a simulated trajectory, then the approximate value function also provides a good local approximation around that trajectory. Notably, it is only necessary to approximate the value gradient since constant offsets in the approximate value function do not affect the associated policy.

On the other hand, solely having a good approximation of the value function itself along a trajectory does not ensure a good local approximation. In many cases, value function approximation methods rely on stochastic local exploration, such as dithering \[, \], to overcome this limitation. Indeed, value-gradient-based RL methods such as dual heuristic programming (DHP), globalized DHP, value-gradient learning \[, \], and stochastic value gradients \[HWS^+^15, \] have been shown to find better policies using less simulation than value function approximation methods that do not directly approximate the value gradient.

VGI differs from the aforementioned value-gradient-based methods in that it does not require stochastic approximations of the value gradient. Fitted value iteration with value gradients is tractable for convex stochastic control problems, since we can exactly evaluate the gradient of the Bellman operator applied to a convex approximate value function by solving a convex optimization problem.

### Convex optimization control policies

For convex stochastic control, the policy associated with a convex quadratic approximate value function can be evaluated by solving a convex optimization problem, i.e., it is a convex optimization control policy (COCP). COCPs are typically evaluated by solving quadratic programs (QPs), which can often be done efficiently in real-time. Evaluating a COCP may also involve minimizing a more complex convex function, such as one parametrized by a neural network To enable embedded applications, code generation tools like CVXGEN and CVXPYgen \[SBD^+^22\] can be utilized.

Other examples of COCPs include convex model predictive control (MPC) \[, \] and convex approximate dynamic programming \[, \]. COCPs can also be tuned by differentiating through their solution maps \[, AJS^+^18\].

### Outline

In §2, we introduce the convex stochastic control problem and solution methods, via dynamic programming and model predictive control. Approximate dynamic programming with quadratic approximate value functions is described in §3, value-gradient iteration is introduced in §4, and extensions and variations are discussed in §5. In §6, we present three numerical examples: an input-constrained linear quadratic regulator (LQR) problem, a commitments planning problem involving alternative investments, and a supply chain optimization problem.

## Convex stochastic control

### Average-cost convex stochastic control problem

### Dynamics

We consider a dynamical system evolving in discrete time $t = {0,1,2,\ldots}$, with state $x_{t} \in \text{R}^{n}$, input $u_{t} \in \text{R}^{m}$, and affine dynamics where $A_{t} \in \text{R}^{n \times n}$, $B_{t} \in \text{R}^{n \times m}$, and $c_{t} \in \text{R}^{n}$ are random. We assume the dynamics are time-invariant, i.e., $(A_{t},B_{t},c_{t})$ are independent and identically distributed (IID) for different values of $t$. The initial state $x_{0}$ is also random, independent of all $(A_{t},B_{t},c_{t})$. When $A_{t}$, $B_{t}$, or $c_{t}$ are not random, i.e., constant, we write them as $A$, $B$, or $c$.

### Certainty-equivalent dynamics

We denote the expectations of the dynamics matrices as $\overline{A} = {\mathbf{E}A_{t}}$, $\overline{B} = {\mathbf{E}B_{t}}$, and $\overline{c} = {\mathbf{E}c_{t}}$. We refer to the dynamical system with the matrices replaced by their expectations, with initial condition $z_{0} = {\mathbf{E}x_{0}}$, as the certainty-equivalent system (with state $z_{t} \in \text{R}^{n}$ and input $v_{t} \in \text{R}^{m}$).

### State-feedback policy

We consider the time-invariant state feedback policy where $\phi:{\text{R}^{n}\rightarrow\text{R}^{m}}$ is the policy that maps the state to the input. The closed-loop system dynamics are which defines a stochastic process for the state $x_{t}$.

### Stage cost

The stage cost is a function $g:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow{\text{R} \cup {\{\infty\}}}}$, where $g{(x_{t},u_{t})}$ is the cost at time $t$. The stage cost $g$ imposes constraints by taking infinite values at disallowed state-input pairs $(x_{t},u_{t})$. We assume that the stage cost is a closed convex function. Note that the cost function does not depend on time, i.e., it is time-invariant.

In some applications the cost is also random, e.g., of the form ${\overset{\sim}{g}}_{t}{(x_{t},u_{t})}$, where ${\overset{\sim}{g}}_{t}$ is IID, and independent of $A_{t},B_{t},c_{t}$, and therefore also of $x_{t}$. Since we will work with the expected value of the stage cost, we can handle this situation by taking ${g{(x,t)}} = {\mathbf{E}{{\overset{\sim}{g}}_{t}{(x,t)}}}$, where the expectation is over the random stage cost. For simplicity we assume that this expectation may be computed analytically. In other cases, the expectation may be approximated, for example using a sample average.

### Average cost

The infinite-horizon average cost is given by Here, we assume that the limit and expectations exist.

We exclusively consider the average-cost problem, and do not consider the closely-related discounted infinite horizon problem and finite horizon problem, which may have time-varying stage cost. However, our approach is readily extended to those problem settings, as discussed in §5.

### Convex stochastic control problem

The convex stochastic control problem is to choose the policy $\phi$ so as to minimize the cost $J$. We will denote an optimal policy as $\phi^{\star}$, and assume that it exists. We let $J^{\star}$ denote the optimal value, i.e., the cost $J$ with an optimal policy. The data in this problem are the distributions of $(A_{t},B_{t},c_{t})$ (which do not depend on $t$), the distribution of $x_{0}$, and the stage cost function $g$.

### Dynamic programming

The optimal control problem is readily solved, at least in principle, using dynamic programming (DP) \[ \]. An optimal policy may be expressed in terms of a so-called Bellman or optimal value function $V^{\star}:{\text{R}^{n}\rightarrow{\text{R} \cup {\{\infty\}}}}$, which roughly speaking represents the optimal long-term cost of being in a given state.

An optimal policy can be expressed in terms of a value function as If there are multiple minima, we can arbitrarily choose one. The first term in the quantity that is minimized is the immediate stage cost incurred by the input choice $u$. The second term reflects the optimal expected long-term cost of starting from the next state. The optimal policy balances these two costs.

The policy does not change when we add a constant to a value function. Without loss of generality we can remove this ambiguity by insisting that ${V^{\star}{(x^{\text{ref}})}} = 0$, where $x^{\text{ref}}$ is a reference state (for which there is an optimal value function with finite value). The value function is sometimes called a *relative value function*.

### Bellman operator

It can be shown that a value function $V^{\star}$ and the optimal cost $J^{\star}$ satisfy where $\mathcal{T}$ is the *Bellman operator*, given by for $h:{\text{R}^{n}\rightarrow{\text{R} \cup {\{\infty\}}}}$.

It follows that a relative value function is a fixed point of the Bellman operator $\mathcal{T}$, i.e., This fixed point condition implies, with optimal cost $J^{\star} = {\mathcal{T}V^{\star}{(x^{ref})}}$.

### Value iteration

The relative value function $V^{rel}$ may be found by fixed point iteration. Under certain technical conditions, the so-called value iteration (or relative value iteration) converges, i.e., ${V^{k} - {V^{k}{(x^{ref})}}}\rightarrow V^{rel}$ and ${\mathcal{T}V^{k}{(x^{\text{ref}})}}\rightarrow J^{\star}$ \[\].

For future reference we mention a variation on value iteration called *damped value iteration*, which has the form where $\rho_{k} \in {(0,1\rbrack}$ with ${\sum_{k}{\rho_{k}{({1 - \rho_{k}})}}} = \infty$. Damped value iteration also satisfies ${V^{k} - {V^{k}{(x^{ref})}}}\rightarrow V^{rel}$ and ${\mathcal{T}V^{k}{(x^{\text{ref}})}}\rightarrow J^{\star}$ under certain technical conditions.

### The value function is convex

The Bellman operator maps convex functions to convex functions, since expectation and partial minimization preserve convexity (see, e.g., \[, §3.2.1, §3.2.5\]). With any convex $V^{1}$ (e.g., the zero function), it follows that all iterates of value iteration are convex, which implies that its limit $V^{\star}$ is convex.

One implication is that evaluating the policy, i.e., minimizing over $u$, is a convex optimization problem. To see this, we observe that ${A_{t}x} + {B_{t}u} + c_{t}$ is an affine function of $u$, so by the affine pre-composition rule, $V^{\star}{({{A_{t}x} + {b_{t}u} + c_{t}})}$ is a convex function of $u$. Adding this to $g{(x,u)}$ and taking expectation preserve convexity, so the function that is minimized is a convex function of $u$.

Since evaluating the policy involves solving a convex optimization problem, we refer to it as a *convex optimization control policy*.

### Linear quadratic regulator

The dynamic programming approach can only be carried out in practice in special cases. The most widely known example is when the stage cost is a (convex) quadratic function, in which case the optimal control problem is called the *linear quadratic regulator* (LQR). For LQR the Bellman operator preserves convex quadratic functions, so it follows that the limit $V^{\star}$ is also convex quadratic, and the optimal policy is affine, i.e., ${\phi^{\star}{(x)}} = {{Kx} + l}$, where $K \in \text{R}^{m \times n}$ and $l \in \text{R}^{m}$ (see ). Value iteration for LQR can be carried out using basic linear algebra operations, and so is tractable. Most importantly we have a practical way to represent the Bellman iterates, and also their limit, by a finite set of parameters, the coefficients of a quadratic function.

### Dynamic programing in the general case

Beyond the special case of LQR described above, there are a handful of other very specific stochastic control problems that are tractable to solve. These cases follow the same general story line as LQR: There is a class of functions that is preserved under the Bellman operator. One example is Merton's portfolio problem, which considers the allocation of wealth between various assets over time, and admits a closed-form solution. Problems with a finite state space may, in principle, be solved by DP, by representing the value function with a table of values. This is referred to as the tabular case. When the state space is continuous but low-dimensional, say, with $n \leq 4$, the region of interest in the state space may be represented using a finite number of points, for example a uniform grid. Tabular DP may then be used, in combination with an interpolation over those points, to give a good approximation of the value function. However, this approach does not scale to problems with larger state dimension, since the number of points needed to represent the value function to a given accuracy grows exponentially with the state dimension.

The challenge in carrying out dynamic programming in more general cases is simple: There is no practical way to represent an arbitrary convex function on $\text{R}^{n}$.

### Certainty-equivalent steady-state optimal state-input pair

For many stochastic control problems, certainty-equivalent approximations may be used to obtain heuristic policies without dynamic programming. In this section we explain the idea of an optimal steady-state certainty-equivalent optimal state-input pair. We start by making two very crude approximations of the stochastic control problem. First, we ignore all uncertainty by replacing the dynamics matrices with their mean values (also called certainty-equivalent). Second, we assume that the system is in steady-state, with constant state $z \in \text{R}^{n}$ and constant input $v \in \text{R}^{m}$, i.e., $z = {{\overline{A}z} + {\overline{B}v} + \overline{c}}$. Then we choose $z$ and $v$ to minimize the objective, which with the assumptions above reduces to $g{(z,v)}$. Thus we solve the convex optimization problem with variables $z \in \text{R}^{n}$ and $v \in \text{R}^{m}$. We refer to a solution of this problem $(z^{\star},v^{\star})$ as a certainty-equivalent steady-state optimal (CE-SSO) state-input pair, and denote it as $(x^{sso},u^{sso})$. For some problems, such as the example considered in §6.2, the constant policy ${\phi{(x)}} = u^{sso}$ is a reasonable heuristic.

### Certainty-equivalent model predictive control

Certainty-equivalent model predictive control (CE-MPC) is another heuristic policy for stochastic control \[, \]. CE-MPC is not our focus, but the methods of this paper can also be used to develop a good CE-MPC policy.

To evaluate the CE-MPC policy $\phi^{mpc}{(x)}$, we solve an $H$-step ahead planning problem with certainty-equivalent dynamics. The planning problem is with variables $z_{1},\ldots,z_{H + 1}$ and $v_{1},\ldots,v_{H}$. The CE-MPC policy is then ${\phi^{mpc}{(x)}} = v_{1}^{\star}$, the first input of an optimal trajectory of the MPC planning problem..

In the CE-MPC problem, $V^{mpc}$ is called the terminal cost. It can be chosen to be zero (particularly when $H$ is large enough), or the indicator function of $x^{sso}$, an optimal certainty-equivalent steady-state state. Another very good choice is $\hat{V}$, an approximation of the value function, which can be found by the methods of this paper.

## Quadratic approximate dynamic programming

### Approximate dynamic programming

In this paper, we consider ADP policies that replace the optimal value function $V^{\star}$ in with a convex approximation $\hat{V}$. The ADP policy is of the form (We omit the constant or offset term since it does not affect the associated policy.) If there are multiple minima, we can arbitrarily choose one. When $\hat{V}$ is a convex quadratic function, we refer to as a QADP policy.

ADP is a heuristic that addresses the issue mentioned above, that there is no practical way to represent an arbitrary convex function on $\text{R}^{n}$ \[ \]. The approximate value function $\hat{V}$ is chosen to approximate $V^{\star}$ in some sense, and to make evaluating the policy tractable. Evaluating $\hat{\phi}$ is always a convex optimization problem; depending on the form of $g$ and $\hat{V}$, the expectation can simplify and the problem can reduce to a common form, such as a quadratic program (QP). When it is not possible to evaluate the expectation in the policy exactly, we can use an estimate obtained by replacing the expectation with a suitable sample average, i.e., a Monte Carlo approximation. ADP often works well in practice, even in cases when $\hat{V}$ is not a particularly good approximation of $V^{\star}$ \[, \].

### Quadratic approximate value functions

In this paper we focus exclusively on quadratic approximate value functions of the form where $P \succeq 0$, i.e., $P \in \text{S}_{+}^{n}$, the set of symmetric positive semidefinite (PSD) $n \times n$ matrices.

The QADP policy associated with $\hat{V}$ is parametrized by the $n \times n$ PSD matrix $P$ and $n$-vector $p$, which we collectively refer to as $\theta = {(P,p)}$. All together, the parameter $\theta$ contains scalar parameters, which has order $n^{2}$. We define $\Theta = {\{\theta\mid{P \succeq 0}\}}$, the set of parameters for which $\hat{V}$ is convex.

### Properties of QADP policies

We now consider several properties of the QADP policies which will be useful in the sequel.

### Simplifying the expectation

The QADP policy can be simplified, since the expectation of a quadratic function can be expressed analytically in terms of the first and second moments of its argument. Thus we have Note that $\mu{(x)}$ depends on $x$, and therefore is not constant, but the other coefficients $M$ and $m$ are constant and depend only on the first and second moments of $A$, $B$, $c$ (and $P$ and $p$). These formulas are derived in §A. Finally, we observe that $M$, $m$, and $\mu{(x)}$ are linear functions of $\theta$.

### Evaluating the policy

Since $g{(x,u)}$ is convex, evaluating the quadratic ADP policy reduces to solving a deterministic convex optimization problem. When in addition $g{(x,u)}$ is QP-representable, i.e., a convex quadratic function plus a convex piecewise linear function, plus the indicator function of linear inequality and equality constraints, evaluating the QADP policy reduces to solving a QP.

### Gradient of the Bellman operator image

Given convex quadratic $\hat{V}$, we may evaluate $\mathcal{T}\hat{V}{(x)}$, the Bellman operator applied to $\hat{V}$ at any state $x$, by solving the convex optimization problem associated with the QADP policy. We can also compute ${\nabla{\mathcal{T}\hat{V}}}{(x)}$, where it is differentiable, and a subgradient otherwise.

To do this, we represent $\mathcal{T}\hat{V}{(x)}$ as the optimal value of the convex optimization problem where we have introduced the variable $\overset{\sim}{x}$. Let ${\nu^{\star}{(x)}} \in \text{R}^{n}$ represent the optimal Lagrange multiplier associated with the constraint $\overset{\sim}{x} = x$. Then, we have ${{\nabla{\mathcal{T}\hat{V}}}{(x)}} = {- {\nu^{\star}{(x)}}}$ when the gradient exists \[, §5.6\]. Otherwise, $- {\nu^{\star}{(x)}}$ is a subgradient, i.e., ${- {\nu^{\star}{(x)}}} \in {\partial{\mathcal{T}\hat{V}{(x)}}}$.

## Value-gradient iteration

### Fitted value iteration

We begin by reviewing fitted (or projected) value iteration (FVI), which is an approximation of value iteration \[ \]. The issue with value iteration is that in practice, we cannot exactly represent the function $\mathcal{T}V^{k}$ in the update. FVI addresses this by restricting all approximate value function iterates $V^{k}$ to be convex quadratic functions.

In the $k$th iteration, we choose a set of states $x^{1},\ldots,x^{N}$, and evaluate $\mathcal{T}V^{k}{(x^{i})}$ for each $i = {1,\ldots,N}$. We can evaluate each $\mathcal{T}V^{k}{(x^{i})}$ by evaluating, which is a convex optimization problem. Then, we fit a convex quadratic function $V^{k + {1/2}}$ to those points, such that This leads to the damped fitted value iteration update which generates a sequence of convex quadratic functions $V^{k}$, with associated QADP policies.

### Fitting convex quadratic functions

One method for finding parameters $\theta = {(P,p)}$ for the convex quadratic function $V^{k + {1/2}}$ is to fit it to a set of points. We first evaluate $v^{i} = {\mathcal{T}V^{k}{(x^{i})}}$ for each $i = {1,\ldots,N}$, and then solve the fitting problem with variables $\theta$ and $c \in \text{R}$, where $c$ is a scalar offset. Here $L:{\text{R}\rightarrow\text{R}}$ is a convex fitting loss function, and $r:{{\text{S}^{n} \times \text{R}^{n}}\rightarrow{\text{R} \cup {\{\infty\}}}}$ is a convex regularization function, with infinite values used to impose (convex) constraints on $\theta$. This is a convex optimization problem, since $V^{k + {1/2}}{(x^{i})}$ is a linear function of $\theta$. Possible choices for $L$ include the squared loss or the robust Huber loss, given by The Huber loss is a more robust alternative to the square loss, in the presence of outliers. Possible choices for $r$ include $\ell_{2}$ regularization and prior knowledge constraints, and are discussed in §4.3. For simplicity, we consider the standard Huber function, which transitions from the quadratic to absolute value at $M = 1$. In general, $M$ may be tuned by cross-validation, using a procedure similar to that described in §4.3.

### Convergence

Convergence guarantees for FVI are available when the approximation error of $\nabla{\mathcal{T}V^{k}}$ is small enough \[, \]. However, unlike value iteration, FVI is not guaranteed to converge in general \[, \]. Nevertheless, with an appropriate approximation $\hat{\nabla}\mathcal{T}V^{k}$ and damping parameters $\rho_{k}$, FVI can often find policies with good performance in practice.

### Value-gradient iteration

VGI is a special case of FVI, where we fit $V^{k + {1/2}}$ using gradients instead of values. In §3.3, we showed that we can evaluate ${\nabla{\mathcal{T}V^{k}}}{(x)}$ at any state $x$ where $\mathcal{T}V^{k}$ is differentiable, by evaluating a particular optimal Lagrange multiplier. Therefore, we can find $V^{k + {1/2}}$ by fitting its gradient.

That is, we choose ${V^{k + {1/2}}{(x)}} = {{{({1/2})}x^{T}Px} + {p^{T}x}}$ such that $P \succeq 0$ and Once we have found $V^{k + {1/2}}$, we apply the damped update to generate the next iterate $V^{k + 1}$. Like in standard FVI, this generates a sequence of convex quadratic functions $V^{k}$, with associated QADP policies.

### Fitting the gradient

In this case, we fit an affine function ${{\nabla V^{k + {1/2}}}{(x)}} = {{Px} + p}$ to a set of points, subject to the constraint that $P$ is symmetric positive semidefinite. In each iteration, we evaluate $g^{i} = {{\nabla{\mathcal{T}V^{k}}}{(x^{i})}}$ for each $i = {1,\ldots,N}$, and then solve the fitting problem with variables $\theta$. Here $L:{\text{R}^{n}\rightarrow\text{R}}$ is a multivariate convex fitting loss function, and $r$ is, like, a convex regularization function. This is also a convex optimization problem, since ${\nabla V^{k + {1/2}}}{(x^{i})}$ is a linear function of $\theta$.

Possible choices for $L$ include the squared $\ell_{2}$ norm and the circular Huber loss which extends the scalar Huber loss to the multivariate case. Like in the scalar case, the circular Huber loss is a more robust alternative to the square function, in the presence of outliers.

### Choice of sampling points

An important consideration is the choice of the state samples values $x^{1},\ldots,x^{N}$ at which we evaluate the policy and $\mathcal{T}V^{k}{(x^{i})}$. Ideally the samples should reflect the states that the system is likely to be , i.e., samples from the steady-state distribution of $x_{t}$ under the policy $\phi^{k}$.

To accomplish this we choose the sample points by simulating the current policy for $N$ steps, using the current policy $\phi^{k}$. In the first iteration $k = 1$, we initialize the simulation at a state chosen at random. In subsequent iterations, we initialize the simulation at the last state in the previous iteration.

### Regularization, constraints, and lower bounds

Prior information, if available, can be incorporated as regularization terms or constraints in the fitting problem, through the function $r{(\theta)}$ in the fitting problem. Constraints and lower bounds may be imposed by setting $r$ to have value $\infty$ when $\theta$ is not consistent with the prior information. We now describe a nonexhaustive list of possibilities that may be combined to form $r{(\theta)}$.

### Ridge regularization

We may add an $\ell_{2}$ penalty on the parameters of the value function where $\lambda > 0$ is a scalar regularization parameter and $\parallel \cdot \parallel_{F}$ denotes the Frobenius norm. The $\ell_{2}$ regularization ensures that the fitting problem is well-posed and helps mitigate overfitting, and is sometimes referred to as Tikhonov or ridge regularization \[, \].

The parameter $\lambda$ is typically chosen using use out-of-sample or cross-validation. To do this we divide the fitting data $(x^{i},v^{i})$ into two sets, the training data and the validation data. We fit $V$ using the training data, for a range of values of $\lambda$, typically on a log scale with upper limits $\lambda^{\max}$ and $\lambda^{\max}$, and then evaluate the average loss on the validation data for each value of $\lambda$. We then choose a value that gives near minimum validation error, with a preference for larger values, i.e., more regularization. This approach is often referred to as grid search. A more thorough method is to use cross-validation, and more sophisticated search methods for evaluating scaling parameters may also be considered; see, for example,.

### LASSO regularization

The $\ell_{1}$ penalty with regularization parameter $\lambda > 0$ is known as LASSO. This regularization is similar to ridge regression in that both shrink the values of the parameters; however, the LASSO is more likely to produce sparse solutions, i.e., $P$ and $p$ with zero-valued entries. Therefore, the LASSO regularization can be particularly useful for weakly coupled systems.

Like with ridge regression, the value of $\lambda$ may be tuned using out-of-sample or cross-validation. When multiple regularization terms are used, we can use the same strategy to find a good set of values for each regularization parameter. For example, the case where both ridge and LASSO regularization are employed is known as the elastic net. In this case, the aforementioned grid search strategy may be used to select the two regularization parameters jointly.

### Symmetry

In some cases, we may know that the value function $V$ should be symmetric, i.e., ${V{(x)}} = {V{({- x})}}$ for any $x \in \text{R}^{n}$. The LQR example considered in §6.1, for example, satisfies this property. For quadratic approximate value functions, symmetry may be implemented by the constraint $p = 0$.

### Fixed minimizer

When we can identify a point $x^{\star}$ in the state space that seems to be the best, we may include the constraint ${\operatorname{argmin}_{x}{V{(x)}}} = x^{\star}$ to the fitting problem. This is equivalent to the linear equality constraint ${{Px^{\star}} + p} = 0$. A special case is when $V$ is constrained to be symmetric, in which case $V{(x)}$ is minimized at zero.

### Lower bounds

In some cases, a quadratic pointwise lower bound on $V^{\star}$ is available up to an additive constant, and may be included as an additional constraint. This may be done by introducing an additional variable $s$, and imposing the pointwise constraint ${V + s} \geq V^{lb}$. This can be expressed as the convex constraint as shown in §B. Since $P^{lb} \succeq 0$, this constraint implies that $P \succeq 0$. So when we add a quadratic lower bound constraint to the fitting problem, we no longer need the constraint $P \succeq 0$.

In many cases we can form a convex quadratic lower bound $V^{\text{lb}}$ on the true value function $V^{\star}$. In the simplest case we can take $V^{\star} = 0$ when the stage cost is nonnegative. Another method is to form an LQR relaxation of the problem, i.e., to replace $g$ with a quadratic lower bound, for example, by ignoring constraints on $u$. The resulting LQR problem can be solved exactly, and its value function $V^{lqr}$ is a lower bound on $V^{\star}$. More sophisticated methods for computing a lower bound on the value function involve solving a convex optimization problem or a series of convex problems.

When the dynamics matrices $A_{t}$ and $B_{t}$ are random, a simpler lower bound may be found by considering the (deterministic) LQR relaxation of the CE problem; see §C.

### Policy interpolation

Suppose we have a set of states $x^{1},\ldots,x^{B}$, and require that the policy takes on corresponding values $u^{1},\ldots,u^{B}$, i.e., This condition may be written as where $\partial{g{(x^{j},u^{j})}}$ is the set of subgradients of $g{(x,u)}$ with respect to $u$, evaluated at $(x^{j},u^{j})$.

In some cases, this constraint has a simple representation. For example, if the stage cost may be written in the form where $h$ is differentiable and $I\left({{(x,u)} \in C} \right)$ is the indicator function of a polyhedral set $C$, then the constraint may be written as a linear inequality constraint on the parameters $P$ and $p$. First, note that where $\partial{I\left({{(x,u)} \in C} \right)}$ is the normal cone to $C$ at $(x^{j},u^{j})$. Since $C$ is a polyhedron the normal cone is also a polyhedron \[, §23\], i.e., representable by a set of linear inequality constraints. Next, from we have which is a linear function of $P$ and $p$. Therefore, the policy interpolation constraints may be represented by a set of linear inequality constraints on $P$ and $p$.

## Extensions and variations

### Input-affine dynamics

The methods presented in this paper can also be applied in cases where the dynamics are nonlinear but input-affine. That is, the dynamics may be written in the form where $f_{t}:{\text{R}^{n}\rightarrow\text{R}^{n}}$ and $B_{t}:{\text{R}^{n}\rightarrow\text{R}^{n \times m}}$ are random functions. We again assume that $(f_{t},g_{t})$ are IID for different values of $t$. The affine dynamics described in §2 are a special case, where ${f_{t}{(x)}} = {{A_{t}x} + c_{t}}$ and ${g_{t}{(x)}} = B_{t}$.

In the input-affine case, the ADP policy is of the form Since the dynamics are affine in $u$, the expected value $\mathbf{E}{\hat{V}{({{f_{t}{(x)}} + {g_{t}{(x)}u}})}}$ is also affine in $u$, when $\hat{V}$ is convex. When $\hat{V}$ is a convex quadratic function of the form, the expected value may be computed exactly, in terms of the first and second moments of $f_{t}{(x)}$ and $g_{t}{(x)}$. Hence, the policy can still be evaluated by solving a convex optimization problem, and VGI can still be performed in a similar manner.

### Alternative cost functions

### Discounted infinite-horizon problem

The mean discounted infinite-horizon cost is given by where $\gamma \in {}$ is a discount factor, and the sum and expectations are assumed to exist. In this case, the value function $V^{\star}$ represents the optimal cost-to-go, and the optimal policy is of the form For the discounted infinite-horizon problem, VGI proceeds in the same way, except with the Bellman operator defined as for $h:{\text{R}^{n}\rightarrow{\text{R} \cup {\{\infty\}}}}$.

### Finite-horizon problem

In the finite-horizon problem, the cost is given by where the stage cost may be time-varying, and the expectations are assumed to exist. In this case, the value function $V_{t}^{\star}$ depends on time, and may be found using a backward recursion. The value iteration starts with and then proceeds as where the Bellman operator at time $t$ is defined as for $h:{\text{R}^{n}\rightarrow{\text{R} \cup {\{\infty\}}}}$.

VGI proceeds similarly for the finite-horizon problem, using an analogous function fitting approximation of the Bellman operator.

### Parallel simulations

In VGI (and FVI in general), we select $N$ sample points by simulating the current policy. We can also select points from more than one simulated trajectory. To do this we choose the sample points by simulating $K$ different trajectories for $T$ steps each, using the current policy. In iteration $k$, each of these $K$ trajectories gives us $T$ states at which we evaluate the policy $\phi^{k}$, so all together we have $N = {TK}$ states and associated evaluations of $\nabla{\mathcal{T}V^{k}}$ to use in the fitting problem. One advantage of this method is that the $K$ trajectories can be evaluated in parallel.

## Numerical examples

In this section, we present three numerical examples, which involve a box-constrained LQR problem, a commitment planning problem with an alternative investments fund, and a supply chain optimization problem. Comparisons with other ADP methods are given in §7.

The code for the examples is available at The ADP policies and VGI method are implemented using CVXPY \[, \]. In addition, the code generation tool CVXPYgen \[SBD^+^22\] was used to create custom solvers for the ADP policies, implemented in C. The experiments were performed on two cores of an Intel Xeon E5-2640 CPU.

### Box-constrained linear quadratic regulator

We first consider a traditional linear quadratic regulator (LQR) problem. The dynamics are time-invariant, and given by where $A \in \text{R}^{n \times n}$ and $B^{n \times m}$ are known and fixed, and $c_{t}$ is an IID random variable with zero mean and covariance ${\mathbf{E}{c_{t}c_{t}^{T}}} = C$. The stage cost is given by where $Q \succeq 0$, $R \succ 0$, and $u^{\max} > 0$ is a maximum input magnitude, in any component of the input.

For this problem, a lower bound $J^{\text{lb}}$ on the optimal cost and a quadratic lower bound $V^{\text{lb}}$ on the optimal value function can be found by solving a semidefinite program (SDP). An upper bound on the optimal cost may be found by evaluating the ADP policy using $V^{\text{lb}}$ as the approximate value function.

### Numerical example

We consider a problem instance with $n = 12$ and $m = 3$. The entries of $A$ are chosen IID from a uniform distribution on $\lbrack{- 1},1\rbrack$. The matrix $A$ was then rescaled to have a maximum eigenvalue of 1. The entries of $B$ are chosen IID from a uniform distribution on $\lbrack{- 0.5},0.5\rbrack$. The process noise $c_{t}$ is normally distributed, with zero mean and covariance $0.4I$. The stage cost parameters are given by $Q = I$ and $R = I$, and the maximum input magnitude is $u^{\max} = 0.4$.

### Results

We carried out VGI for $40$ iterations, starting from the initial value function ${V^{1}{(x)}} = {x^{T}Qx}$. We included the symmetry constraint $p = 0$ in the fitting step. In each iteration, the fitting step was performed using $N = 50$ fitting points, obtained by simulating the current policy. The damping coefficient was fixed to $\rho_{k} = 0.5$.

Figure 1 shows the average cost versus the number of policy evaluations used to generate the data for the fitting step. Also plotted are the SDP-based upper and lower bounds and the average cost of the CE-MPC policy with a horizon of $H = 30$. In this example, VGI converges to a slightly better cost than that of the CE-MPC policy.

Figure 1: VGI for the box-constrained LQR problem.

### Commitments in an alternative investments fund

Our next example is a practical example, and more specific. We consider a fund that invests in $m$ so-called alternative investment classes, such as venture capital, infrastructure projects, direct lending, or private equity. Alternative investments are found in the portfolios of insurance companies, retirement funds, and university endowments. For more details, see \[LBvB^+^22\] and the papers cited therein.

In each time period (typically quarters) $t = {1,2,\ldots}$, we make nonnegative commitments to the $m$ alternative asset classes. These are amounts we promise to invest, in response to capital calls. Over the next few years, we put money into the investments in response to capital calls, up to the amount of previous commitments. We receive money from each the investments in later years through distributions. Neither the timing nor amounts of the capital calls and distributions are directly under our control, except that the total of the capital calls cannot exceed our total commitments for each asset class.

We first describe some critical quantities. $u_{t} \in \text{R}_{+}^{m}$ denotes the amounts that the investor commits in period $t$, to each of the $m$ asset classes. (These commitments will be the input in our stochastic control problem.) $p_{t} \in \text{R}_{+}^{m}$ denotes the amounts that the investor pays in to the investment in response to capital calls in period $t$. $d_{t} \in \text{R}_{+}^{m}$ denotes the amount that the investor receives in distributions from the investments in period $t$. $n_{t} \in \text{R}_{+}^{m}$ denotes the net asset values (NAVs) of the investments in period $t$. $l_{t} \in \text{R}_{+}^{m}$ denotes the total amount of uncalled commitments, i.e., the difference between the total so far committed and the total so far that has been called. (This is a liability, so we use the symbol $l$.)

The units for all of these is typically millions of USD.

A simple dynamical model relating these variables is where $r_{t} \in \text{R}_{+ +}^{K}$ is the vector of per-period total returns for the asset classes, assumed to be IID with some known distribution such as log-normal. In words: the value of each investment class in each period is multiplied by its (random) return, increased by the amount paid, and decreased by the amount distributed; the total uncalled commitments is decreased by the capital calls, and increased by new commitments. The calls and distributions are modeled as where $\gamma_{t}^{\text{call}}$ and $\gamma_{t}^{\text{dist}}$ are random variables in ${}^{m}$, called the call and distribution intensities. We will assume that these are IID, and independent of $r_{t}$. In words: In each period and for each asset class, a random fraction of the total liability is called, and a random fraction of the NAV is distributed.

We can express the dynamics as a random linear dynamical system with state $x_{t} = {(n_{t},l_{t})} \in \text{R}^{2m}$ and input $u_{t} \in \text{R}^{m}$, with dynamics matrices The goal is to choose commitments so as to reach and maintain a target asset allocation $n^{tar} \in \text{R}_{+}^{m}$, while penalizing deviations of the commitments $u_{t}$ from the CE-SSO commitment $u^{sso} \in \text{R}_{+}^{m}$. We consider stage cost where $\lambda > 0$ is a penalty coefficient and $u^{\max} \in \text{R}_{+}^{m}$ are the maximum allowable commitments to each of the asset classes. We take the fixed input $u^{sso}$ is a solution to the certainty-equivalent steady-state problem, with the input cost term $\lambda{\|{u_{t} - u^{sso}}\|}^{2}$ removed from the stage cost.

For this problem, we find a quadratic lower bound $V^{\text{lb}}$ on the value function by relaxing the constraints on the input $u_{t}$, replacing $A_{t}$ with $\overline{A}$, and solving the certainty equivalent LQR problem.

### Numerical example

We consider an example with $m = 6$ asset classes. The returns $r_{t}$ are distributed according to a log-normal distribution, i.e., $r_{t} = {\exp{(z_{t})}}$, with $z_{t} \sim {\mathcal{N}{(\mu,\Sigma)}}$. The parameters $\mu$ and $\Sigma$ were chosen such that the mean quarterly returns have means and standard deviations This leads to annualized returns with means around $20\%$ and standard deviations around $30\%$. The returns are correlated, with correlation matrix The components of $\gamma_{t}^{\text{call}}$ and $\gamma_{t}^{\text{dist}}$ are independent and beta-distributed, such that ${(\gamma_{t}^{\text{call}})}_{i} \sim {{Beta}{(\alpha_{i}^{\text{call}},\beta_{i}^{\text{call}})}}$, where $\alpha_{i}^{call} = 2$ for $i = {1,\ldots,m}$, and The distribution intensities were also beta distributed, such that ${(\gamma_{t}^{\text{dist}})}_{i} \sim {{Beta}{(\alpha_{i}^{\text{dist}},\beta_{i}^{\text{dist}})}}$, where $\alpha_{i}^{dist} = 3$ for $i = {1,\ldots,m}$, and These parameters lead to typical values of call and distribution intensities around $0.14$ and $0.16$ respectively. The target asset values $n^{\text{tar}}$ are chosen to be between 4 and 5, the maximum commitment is $u^{\max} = 3$, and the penalty coefficient was $\lambda = 0.01$.

Figure 2: VGI for the commitments planning problem.

Figure 3: Commitments, NAV, and uncalled commitments for one asset class. The policy found by VGI makes commitments when the NAV dips below the target value.

### Results

We carried out VGI for $20$ iterations, starting from $V^{1} = V^{lb}$. In each iteration, the fitting step was performed using $N = 50$ fitting points, obtained by simulating the current policy. The damping coefficient was fixed to $\rho_{k} = 0.5$.

Figure 2 plots the average cost versus the number of policy evaluations used, along with the average cost of the CE-MPC policy with a horizon of $H = 30$. Our method converges to a policy that is 25% better than the CE-MPC policy. It is able to significantly outperform the CE-MPC policy because it accounts for the correlation between the returns $r_{t}$. The CE-MPC policy, on the other hand, only accounts for the average returns. The average costs were computed by simulating the system for ten thousand steps.

Figure 3 shows an example trajectory of asset value, liability, and commitments made for one of the six asset classes, using the ADP policy found by VGI. The policy makes commitments when the asset value dips below the target value.

Figure 4: Supply chain network.

### Supply chain optimization

In our final example, we consider the problem of shipping goods efficiently across a network of warehouses to maximize profit. We consider a single-good, multi-echelon supply chain with $\overset{\sim}{n}$ interconnected warehouses, which are represented by nodes in a graph. There are $m$ directed links over which goods can flow; $n_{s}$ links connect suppliers to nodes, $n_{c}$ links connect nodes to consumers, and $m - n_{s} - n_{c}$ links connect nodes to each other.

The amount of good held at each node at time $t$ is represented by $h_{t} \in \text{R}_{+}^{\overset{\sim}{n}}$. The prices at which we can buy the good from the suppliers are denoted by $p_{t} \in \text{R}_{+}^{n_{s}}$, the fixed prices at which goods can be sold to consumers are denoted by $r \in \text{R}_{+}^{n_{c}}$, and the consumer demand is $d_{t} \in \text{R}_{+}^{n_{c}}$. The prices and demand are random and independent between time points, but are known at time $t$ for planning. The inputs are $b_{t} \in \text{R}_{+}^{n_{s}}$, amounts bought from the suppliers, $s_{t} \in \text{R}_{+}^{n_{c}}$, the amounts sold to the consumers, and $z_{t} \in \text{R}_{+}^{m - n_{s} - n_{c}}$, the amounts transported across inter-node links. The dynamics are given by where ${A^{\text{in}},A^{\text{out}}} \in \text{R}^{n \times m}$; $A_{ij}^{\text{in (out)}}$ is 1 if link $j$ enters (exits) node $i$ and 0 otherwise.

The dynamics may be expressed as a random linear dynamical system with augmented state $x_{t} = {(h_{t},p_{t},d_{t})}$, input $u_{t} = {(b_{t},s_{t},z_{t})}$, and dynamics matrices such that $x_{t} \in \text{R}^{n}$ with $n = {\overset{\sim}{n} + n_{s} + n_{c}}$ and $u_{t} \in \text{R}^{m}$.

The prices and demand $p_{t}$ and $d_{t}$ are included in the state since they are known at time $t$ for planning. However, since they are random and independent between time points, the value function need only be a function of $h_{t}$. Moreover, we only require that the stage cost be jointly convex in $(h_{t},u_{t})$.

The goal is to maximize the revenue from selling goods to customers while minimizing the material costs paid to the suppliers, transportation costs, and holding costs of the goods at each node. Let $\tau \in \text{R}_{+}^{m}$ encode the costs of transporting a unit of good across each link, and $\alpha \in \text{R}_{+}^{n}$ and $\beta \in \text{R}_{+}^{n}$ parametrize the linear and quadratic holding costs of the goods at each node.

The stage cost is where $I{(x_{t},u_{t})}$ is the indicator function that encodes the following constraints: The warehouses have maximum capacity $h_{\max} > 0$: $0 \leq h_{t + 1} \leq h_{\max}$.

The links have maximum capacity $u_{\max} > 0$: $0 \leq u_{t} \leq u_{\max}$.

The amounts shipped out should not exceed the current capacities: ${A^{\text{out}}u_{t}} \leq h_{t}$.

The amounts sold to consumers cannot exceed the current demand: $s_{t} \leq d_{t}$.

For this example, we find a quadratic lower bound $V^{\text{lb}}$ on the value function by relaxing the constraints, adding the quadratic penalty ${u_{t}^{T}u_{t}} - {{({1/2})}u_{\max}\mathbf{1}^{\top}u_{t}}$ to the stage cost, and solving the resulting LQR problem. The lower bound is valid, since the added penalty is a pointwise lower bound on the indicator of the input constraints, which is zero for $0 \leq u_{t} \leq u_{\max}$, and infinity otherwise.

### Numerical example

We consider a network with $\overset{\sim}{n} = 4$ warehouses, $n_{s} = 2$ suppliers, $n_{c} = 2$ consumers, and $m = 8$ links. The network is illustrated in Figure 4. The supplier prices $p_{t}$ and customer demands $d_{t}$ are log-normally distributed, such that ${\log p_{t}} \sim {\mathcal{N}{(\mu_{p},\Sigma_{p})}}$ and ${\log d_{t}} \sim {\mathcal{N}{(\mu_{d},\Sigma_{d})}}$, with The holding cost parameters are $\alpha = \beta = {{(0.01)}\mathbf{1}}$, the transportation cost is $\tau = {{(0.05)}\mathbf{1}}$, and the consumer prices are $r = {{(1.3)}\mathbf{1}}$. The maximum warehouse capacities are $h_{\max} = {{}\mathbf{1}}$, and the maximum link capacities are $u_{\max} = {{}\mathbf{1}}$.

### Results

We carried out VGI for $20$ iterations, starting from the quadratic lower bound $V^{lb}$. In each iteration, the fitting step was performed using $N = 50$ fitting points, obtained by simulating the current policy. The damping coefficient was fixed to $\rho_{k} = 0.5$. When solving the fitting problem, we add an $\ell_{2}$ (or ridge) regularization, with coefficient $\lambda = 10^{- 4}$.

Figure 5 shows the average cost versus the number of policy evaluations used, along with the average cost of the CE-MPC policy with a horizon of $H = 30$. Our method converges to roughly the same cost as the CE-MPC policy.

Figure 6 shows the storage $h_{t}$ for each of the four warehouses over time, for the initial policy using $V^{\text{lb}}$ and the final policy after VGI. The plots show average trajectories over 500 simulations, each initialized with a state in ${\lbrack 0,h_{\max}\rbrack}^{4}$, chosen uniformly at random.

On average, the VGI policy is able to keep the storage levels close to half capacity for all warehouses. On the other hand, the initial policy tends to put too much stock in the first warehouse with storage ${(h_{t})}_{1}$, which can, on average, buy goods at a lower price from the suppliers. Similarly, the policy tends to under-utilize the third warehouse with storage ${(h_{t})}_{3}$, which experiences lower consumer demand than the fourth warehouse with storage ${(h_{t})}_{4}$.

Figure 5: VGI for the supply chain problem.

Figure 6: Supply chain storage ht for each warehouse over time. Left: initial ADP policy using Vlb. Right: final policy after VGI.

## Comparison with other methods

In this section, we evaluate VGI against two related ADP methods for finding a quadratic approximate value function: the standard FVI described in §4.1 and a COCP gradient method. They are iterative methods that follow the same pattern as VGI: at each iteration, we simulate the system for $N$ steps, and then use the resulting data to update the parameters of the quadratic approximate value function.

### COCP gradient method

We compare against a gradient based method that updates the parameters $\theta$ of the ADP policy using the derivatives of the cost along simulated trajectories, with respect to $\theta$. At iteration $k$, the policy $\phi^{k}$ with parameters $\theta^{k}$ is used to simulate the system for $N$ steps. The resulting data is used to compute an estimate of the average cost, given by We then compute ${\nabla\hat{J}}{(\theta^{k})}$ using the chain rule, and then update the parameters. This approach is known as backpropagation through time. In our experiments, we use the projected stochastic (sub)gradient rule $\theta^{k + 1} = {\Pi_{\Theta}{({\theta^{k} - {\alpha^{k}{\nabla\hat{J}}{(\theta^{k})}}})}}$, where $\Pi_{\Theta}$ is the projection onto $\Theta$, and $\alpha^{k} > 0$ is a step size.

This approach requires derivatives of the policy with respect to its parameters. Those derivatives may be found by applying the implicit function theorem to the optimality conditions of the convex optimization problem associated with the policy \[AAB^+^19, \]. Examples of the COCP gradient method used to find quadratic approximate value functions may be found. In our experiments, we used cvxpylayers to compute the necessary derivatives \[AAB^+^19\].

### Results

In general, FVI and COCP gradient methods required more tuning of hyperparameters than VGI to work well. As shown in table 1, VGI achieves the best (or close to the best) performance in all three problems, all using far fewer policy evaluations than the FVI and COCP gradient methods. The costs were evaluated in each case by simulating the policy for ten thousand steps.

VGI used the same hyperparameters as in §6, i.e., $\rho_{k} = 0.5$ and $N = 50$. The method was run for 40 iterations for the box-constrained LQR problem, 20 iterations for the commitments example, and 15 iterations for the supply chain problem.

We now discuss the hyperparameters chosen for FVI and the COCP gradient method. All methods were initialized using the same initial quadratic approximate value function. For the box-constrained LQR problem we used ${V^{1}{(x)}} = {x^{T}Qx}$, and for the other two problems we used ${V^{1}{(x)}} = V^{\text{lb}}$, the quadratic lower bound on $V$ available for each problem.

Table 1: Comparison of cost and number of policy evaluations used (in thousands)

### Box constrained LQR

FVI was run using $N = 400$ policy evaluations, for a total of 50 iterations. The damping parameter was $\rho_{k} = 0.5$, and the symmetry constraint $p = 0$ was incorporated into the fitting problem.

The COCP gradient method was run using $N = 300$ policy evaluations, for a total of 80 iterations. The $300$ sample points were generated by simulating $K = 3$ trajectories each of length $T = 100$, using the procedure described in §5.3. We used a step size of $\alpha^{k} = 0.01$. The method was initialized with $P = I$, and the symmetry constraint $p = 0$ was incorporated into the fitting problem. VGI took 6 seconds to complete, FVI took 29 seconds, and the COCP gradient method took 4 minutes and 10 seconds.

### Commitments planning

FVI was run using $N = 200$ policy evaluations, for a total of $20$ iterations. The sample points were generated by simulating $K = 2$ trajectories each of length $T = 100$. The damping parameter was $\rho_{k} = 0.5$.

The COCP gradient method was run using $N = 200$ policy evaluations, for a total of 100 iterations. The sample points were generated by simulating $K = 2$ trajectories each of length $T = 100$. We used a step size of $\alpha^{k} = 10^{- 4}$. VGI took 5 seconds to complete, FVI took 7 seconds, and the COCP gradient method took 5 minutes.

### Supply chain

FVI was run using $N = 800$ policy evaluations, for a total of $20$ iterations. The sample points were generated by simulating $K = 2$ trajectories each of length $T = 400$. The damping parameter was $\rho_{k} = 0.75$. An $\ell_{2}$ regularization with coefficient $\lambda = 10^{- 4}$ was used in the fitting problem.

The COCP gradient method was run using $N = 1000$ policy evaluations, for a total of $70$ iterations. The sample points were generated by simulating $K = 10$ trajectories each of length $T = 100$. We used a step size of $\alpha^{k} = 0.01$. An $\ell_{2}$ regularization with coefficient $\lambda = 10^{- 4}$ was added to the cost. VGI took 2 seconds to complete, FVI took 25 seconds, and the COCP gradient method took 13 minutes.

## Conclusion

In this work, we propose value-gradient iteration, a method for finding a quadratic approximate value function for convex stochastic control. The method is an approximation of value iteration, and we show how we may compute the gradient of the Bellman operator image to fit the gradient of the approximate value function in each iteration. By fitting the gradient of the approximate value function instead of the approximate value function itself, we can find a good policy using far less simulation data. Indeed, we find that the computational effort of obtaining a good approximate value function is comparable to that of evaluating the policy through simulation.
