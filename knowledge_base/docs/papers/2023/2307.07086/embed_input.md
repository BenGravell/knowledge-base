<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Value-Gradient Iteration with Quadratic Approximate Value Functions

Topics include Real-time systems, Control, Value-gradient iteration.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a method for designing policies for convex stochastic control problems characterized by random linear dynamics and convex stage cost. We consider policies that employ quadratic approximate value functions as a substitute for the true value function. Evaluating the associated control policy involves solving a convex problem, typically a quadratic program, which can be carried out reliably in real-time. Such policies often perform well even when the approximate value function is not a particularly good approximation of the true value function. We propose value-gradient iteration, which fits the gradient of value function, with regularization that can include constraints reflecting known bounds on the true value function. Our value-gradient iteration method can yield a good approximate value function with few samples, and little hyperparameter tuning. We find that the method can find a good policy with computational effort comparable to that required to just evaluate a control policy via simulation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider convex approximate dynamic programming (ADP) policies for convex stochastic control problems, which involve systems with known random linear dynamics and convex stage costs. Evaluating an ADP policy reduces to solving a convex optimization problem involving a convex approximate value function. We focus on fitting quadratic approximate value functions, and refer to the associated policies as quadratic approximate dynamic programming (QADP) policies. While QADP policies are optimal for problems with convex quadratic stage cost, they can also serve as effective heuristics for other problem types. It has been observed that ADP policies can perform well even when using imperfect approximations of the true value function.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose an approximate value iteration method for finding quadratic approximate value functions for convex stochastic control problems, which we refer to as *value-gradient iteration* (VGI). In principle, an optimal value function may be found by iterating the Bellman operator, which maps real-valued functions on the state space to real-valued functions on the state space. Since it is not possible in general to exactly represent functions on $\text{R}^{n}$, we incorporate a function approximation step after each application of the Bellman operator, a general approach called fitted value iteration (FVI). In our proposed VGI, instead of directly fitting the value function, we fit the gradient of the value function with respect to the state vector.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is sufficient to approximate the gradient since constant offsets in the value function have no impact on the associated ADP policy. In addition, the gradient of the value function carries more information than the value function itself. If the gradient is well approximated at a set of states, then the value function is also well approximated locally around those states, up to an additive constant which does not affect the policy. However, having a good approximation of only the value at a set of states does not imply that the value function is well approximated locally around those states.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most importantly, VGI is practical to implement for QADP. We show that, when it exists, the gradient of the Bellman operator applied to a convex quadratic function can be obtained at any state by evaluating a particular optimal dual variable associated with the QADP policy. Since the gradient of a convex quadratic is an affine function, in each iteration we fit an affine function to a set of pairs of states and value-gradients. This fitting problem is a convex optimization problem. Therefore, VGI involves solving a sequence of convex optimization problems, which can be carried out reliably.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also consider several techniques for enhancing the reliability of VGI, including damping, a robust Huber fitting loss, and the incorporation of prior knowledge constraints and regularization. VGI remains effective even when the state space dimension is large relative to the number of fitting samples, as we will demonstrate with several numerical examples. Finally, we note that the computational effort of obtaining a good QADP policy using VGI is small enough that it is comparable to that of simply evaluating the policy through simulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

Dynamic programming (DP) provides techniques for computing the optimal value function and policy for general Markov decision processes. The optimal policy is evaluated by solving an optimization problem, where the control is chosen by minimizing the current stage cost plus the expected value function at the next state. For convex stochastic control problems, this is a convex optimization problem. However, it is possible to exactly represent and find the value function in a only few special cases, for example when the state space is discrete, or when we have a convex stochastic control problem with a convex extended quadratic stage cost.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

ADP methods are heuristics used in stochastic control when the problem cannot be solved by applying DP directly. Typically, these methods either approximate the value function in DP or tune the parameters of a parametric policy. In some contexts, approximate value functions are known as control Lyapunov functions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

One approach to ADP is to approximate the value function by relaxing the Bellman equation to an inequality, and then solving a convex optimization problem involving a model of the dynamics and stage cost. When the state and input spaces are finite, this leads to a linear program (LP). When the dynamics are affine, the stage cost is quadratic, and the input is constrained to be in a convex set, quadratic approximate value functions can be obtained using semidefinite programming. In both cases, the resulting approximate value functions are lower bounds on the true value function.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

Other value function approximation methods search for an approximate value function that satisfies the Bellman equation along simulated trajectories. This includes the method proposed in this paper, which is closely related to fitted (or projected) value iteration. Other methods, which do not assume that a model of the dynamics and stage cost are available, include $Q$-iteration, $Q$-learning, and temporal difference learning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

Instead of approximating the value function, other ADP techniques directly optimize the parameters of a parametric policy to improve performance along system trajectories. Stochastic gradient descent and its variants have been employed to tune convex optimization control policies and controllers based on Proportional-Integral-Derivative (PID) control \[, ÅHHH93\] and model predictive control (MPC) \[, AJS^+^18\]. Policy gradient methods provide a method for differentiating through policies parametrized by neural networks \[MBM^+^16, SWD^+^17\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

Reinforcement learning (RL) methods can be considered a form of approximate dynamic programming (ADP), although their primary focus is on learning from interactions with the system or a simulator, rather than relying on explicit mathematical models of the system dynamics or stage cost. In this work, we assume that models of the dynamics and stage cost are either known or have been estimated or learned beforehand. This is similar to some model-based RL methods that learn a policy and a model of the dynamics jointly. In the context of control, the process of learning the dynamics is typically referred to as system identification.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Value gradients", "weight": 1.0} -->

When considering a differentiable approximate value function, it is advantageous to have accurate approximations of its derivatives with respect to the state, i.e., the value gradient. If the value gradient is well-approximated along a simulated trajectory, then the approximate value function also provides a good local approximation around that trajectory. Notably, it is only necessary to approximate the value gradient since constant offsets in the approximate value function do not affect the associated policy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Value gradients", "weight": 1.0} -->

On the other hand, solely having a good approximation of the value function itself along a trajectory does not ensure a good local approximation. In many cases, value function approximation methods rely on stochastic local exploration, such as dithering, to overcome this limitation. Indeed, value-gradient-based RL methods such as dual heuristic programming (DHP), globalized DHP, value-gradient learning, and stochastic value gradients \[HWS^+^15, \] have been shown to find better policies using less simulation than value function approximation methods that do not directly approximate the value gradient.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Value gradients", "weight": 1.0} -->

VGI differs from the aforementioned value-gradient-based methods in that it does not require stochastic approximations of the value gradient. Fitted value iteration with value gradients is tractable for convex stochastic control problems, since we can exactly evaluate the gradient of the Bellman operator applied to a convex approximate value function by solving a convex optimization problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

For convex stochastic control, the policy associated with a convex quadratic approximate value function can be evaluated by solving a convex optimization problem, i.e., it is a convex optimization control policy (COCP). COCPs are typically evaluated by solving quadratic programs (QPs), which can often be done efficiently in real-time. Evaluating a COCP may also involve minimizing a more complex convex function, such as one parametrized by a neural network To enable embedded applications, code generation tools like CVXGEN and CVXPYgen \[SBD^+^22\] can be utilized.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

Other examples of COCPs include convex model predictive control (MPC) and convex approximate dynamic programming. COCPs can also be tuned by differentiating through their solution maps \[, AJS^+^18\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Outline", "weight": 1.0} -->

In §2, we introduce the convex stochastic control problem and solution methods, via dynamic programming and model predictive control. Approximate dynamic programming with quadratic approximate value functions is described in §3, value-gradient iteration is introduced in §4, and extensions and variations are discussed in §5. In §6, we present three numerical examples: an input-constrained linear quadratic regulator (LQR) problem, a commitments planning problem involving alternative investments, and a supply chain optimization problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dynamics", "weight": 1.0} -->

We consider a dynamical system evolving in discrete time $t = {0,1,2,\ldots}$, with state $x_{t} \in \text{R}^{n}$, input $u_{t} \in \text{R}^{m}$, and affine dynamics

<!-- chunk {"id": "body-0021", "role": "body", "section": "Dynamics", "weight": 1.0} -->

where $A_{t} \in \text{R}^{n \times n}$, $B_{t} \in \text{R}^{n \times m}$, and $c_{t} \in \text{R}^{n}$ are random. We assume the dynamics are time-invariant, i.e., $(A_{t},B_{t},c_{t})$ are independent and identically distributed (IID) for different values of $t$. The initial state $x_{0}$ is also random, independent of all $(A_{t},B_{t},c_{t})$. When $A_{t}$, $B_{t}$, or $c_{t}$ are not random, i.e., constant, we write them as $A$, $B$, or $c$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Certainty-equivalent dynamics", "weight": 1.0} -->

We denote the expectations of the dynamics matrices as $\overline{A} = {\mathbf{E}A_{t}}$, $\overline{B} = {\mathbf{E}B_{t}}$, and $\overline{c} = {\mathbf{E}c_{t}}$. We refer to the dynamical system with the matrices replaced by their expectations,

<!-- chunk {"id": "body-0023", "role": "body", "section": "State-feedback policy", "weight": 1.0} -->

We consider the time-invariant state feedback policy

<!-- chunk {"id": "body-0024", "role": "body", "section": "State-feedback policy", "weight": 1.0} -->

where $\phi:{\text{R}^{n}\rightarrow\text{R}^{m}}$ is the policy that maps the state to the input. The closed-loop system dynamics are

<!-- chunk {"id": "body-0025", "role": "body", "section": "State-feedback policy", "weight": 1.0} -->

which defines a stochastic process for the state $x_{t}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stage cost", "weight": 1.0} -->

The stage cost is a function $g:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow{\text{R} \cup {\{\infty\}}}}$, where $g{(x_{t},u_{t})}$ is the cost at time $t$. The stage cost $g$ imposes constraints by taking infinite values at disallowed state-input pairs $(x_{t},u_{t})$. We assume that the stage cost is a closed convex function. Note that the cost function does not depend on time, i.e., it is time-invariant.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stage cost", "weight": 1.0} -->

In some applications the cost is also random, e.g., of the form ${\overset{\sim}{g}}_{t}{(x_{t},u_{t})}$, where ${\overset{\sim}{g}}_{t}$ is IID, and independent of $A_{t},B_{t},c_{t}$, and therefore also of $x_{t}$. Since we will work with the expected value of the stage cost, we can handle this situation by taking ${g{(x,t)}} = {\mathbf{E}{{\overset{\sim}{g}}_{t}{(x,t)}}}$, where the expectation is over the random stage cost. For simplicity we assume that this expectation may be computed analytically. In other cases, the expectation may be approximated, for example using a sample average.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Average cost", "weight": 1.0} -->

The infinite-horizon average cost is given by

<!-- chunk {"id": "body-0029", "role": "body", "section": "Average cost", "weight": 1.0} -->

Here, we assume that the limit and expectations exist.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Average cost", "weight": 1.0} -->

We exclusively consider the average-cost problem, and do not consider the closely-related discounted infinite horizon problem and finite horizon problem, which may have time-varying stage cost. However, our approach is readily extended to those problem settings, as discussed in §5.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convex stochastic control problem", "weight": 1.0} -->

The convex stochastic control problem is to choose the policy $\phi$ so as to minimize the cost $J$. We will denote an optimal policy as $\phi^{\star}$, and assume that it exists. We let $J^{\star}$ denote the optimal value, i.e., the cost $J$ with an optimal policy. The data in this problem are the distributions of $(A_{t},B_{t},c_{t})$ (which do not depend on $t$), the distribution of $x_{0}$, and the stage cost function $g$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

The optimal control problem is readily solved, at least in principle, using dynamic programming (DP). An optimal policy may be expressed in terms of a so-called Bellman or optimal value function $V^{\star}:{\text{R}^{n}\rightarrow{\text{R} \cup {\{\infty\}}}}$, which roughly speaking represents the optimal long-term cost of being in a given state.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

An optimal policy can be expressed in terms of a value function as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

If there are multiple minima, we can arbitrarily choose one. The first term in the quantity that is minimized is the immediate stage cost incurred by the input choice $u$. The second term reflects the optimal expected long-term cost of starting from the next state. The optimal policy balances these two costs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

The policy does not change when we add a constant to a value function. Without loss of generality we can remove this ambiguity by insisting that ${V^{\star}{(x^{\text{ref}})}} = 0$, where $x^{\text{ref}}$ is a reference state (for which there is an optimal value function with finite value). The value function

<!-- chunk {"id": "body-0036", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

is sometimes called a *relative value function*.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Bellman operator", "weight": 1.0} -->

It can be shown that a value function $V^{\star}$ and the optimal cost $J^{\star}$ satisfy

<!-- chunk {"id": "body-0038", "role": "body", "section": "Bellman operator", "weight": 1.0} -->

where $\mathcal{T}$ is the *Bellman operator*, given by

<!-- chunk {"id": "body-0039", "role": "body", "section": "Bellman operator", "weight": 1.0} -->

It follows that a relative value function is a fixed point of the Bellman operator $\mathcal{T}$, i.e.,

<!-- chunk {"id": "body-0040", "role": "body", "section": "Value iteration", "weight": 1.0} -->

The relative value function $V^{rel}$ may be found by fixed point iteration. Under certain technical conditions, the so-called value iteration (or relative value iteration)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Value iteration", "weight": 1.0} -->

For future reference we mention a variation on value iteration called *damped value iteration*, which has the form

<!-- chunk {"id": "body-0042", "role": "body", "section": "The value function is convex", "weight": 1.0} -->

The Bellman operator maps convex functions to convex functions, since expectation and partial minimization preserve convexity (see, e.g., \[, §3.2.1, §3.2.5\]). With any convex $V^{1}$ (e.g., the zero function), it follows that all iterates of value iteration are convex, which implies that its limit $V^{\star}$ is convex.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The value function is convex", "weight": 1.0} -->

One implication is that evaluating the policy, i.e., minimizing

<!-- chunk {"id": "body-0044", "role": "body", "section": "The value function is convex", "weight": 1.0} -->

over $u$, is a convex optimization problem. To see this, we observe that ${A_{t}x} + {B_{t}u} + c_{t}$ is an affine function of $u$, so by the affine pre-composition rule, $V^{\star}{({{A_{t}x} + {b_{t}u} + c_{t}})}$ is a convex function of $u$. Adding this to $g{(x,u)}$ and taking expectation preserve convexity, so the function that is minimized is a convex function of $u$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The value function is convex", "weight": 1.0} -->

Since evaluating the policy involves solving a convex optimization problem, we refer to it as a *convex optimization control policy*.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

The dynamic programming approach can only be carried out in practice in special cases. The most widely known example is when the stage cost is a (convex) quadratic function, in which case the optimal control problem is called the *linear quadratic regulator* (LQR). For LQR the Bellman operator preserves convex quadratic functions, so it follows that the limit $V^{\star}$ is also convex quadratic, and the optimal policy is affine, i.e., ${\phi^{\star}{(x)}} = {{Kx} + l}$, where $K \in \text{R}^{m \times n}$ and $l \in \text{R}^{m}$ (see ). Value iteration for LQR can be carried out using basic linear algebra operations, and so is tractable. Most importantly we have a practical way to represent the Bellman iterates, and also their limit, by a finite set of parameters, the coefficients of a quadratic function.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Dynamic programing in the general case", "weight": 1.0} -->

Beyond the special case of LQR described above, there are a handful of other very specific stochastic control problems that are tractable to solve. These cases follow the same general story line as LQR: There is a class of functions that is preserved under the Bellman operator. One example is Merton's portfolio problem, which considers the allocation of wealth between various assets over time, and admits a closed-form solution. Problems with a finite state space may, in principle, be solved by DP, by representing the value function with a table of values. This is referred to as the tabular case. When the state space is continuous but low-dimensional, say, with $n \leq 4$, the region of interest in the state space may be represented using a finite number of points, for example a uniform grid. Tabular DP may then be used, in combination with an interpolation over those points, to give a good approximation of the value function. However, this approach does not scale to problems with larger state dimension, since the number of points needed to represent the value function to a given accuracy grows exponentially with the state dimension.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Dynamic programing in the general case", "weight": 1.0} -->

The challenge in carrying out dynamic programming in more general cases is simple: There is no practical way to represent an arbitrary convex function on $\text{R}^{n}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Certainty-equivalent steady-state optimal state-input pair", "weight": 1.0} -->

For many stochastic control problems, certainty-equivalent approximations may be used to obtain heuristic policies without dynamic programming. In this section we explain the idea of an optimal steady-state certainty-equivalent optimal state-input pair. We start by making two very crude approximations of the stochastic control problem. First, we ignore all uncertainty by replacing the dynamics matrices with their mean values (also called certainty-equivalent). Second, we assume that the system is in steady-state, with constant state $z \in \text{R}^{n}$ and constant input $v \in \text{R}^{m}$, i.e., $z = {{\overline{A}z} + {\overline{B}v} + \overline{c}}$. Then we choose $z$ and $v$ to minimize the objective, which with the assumptions above reduces to $g{(z,v)}$. Thus we solve the convex optimization problem

<!-- chunk {"id": "body-0050", "role": "body", "section": "Certainty-equivalent steady-state optimal state-input pair", "weight": 1.0} -->

with variables $z \in \text{R}^{n}$ and $v \in \text{R}^{m}$. We refer to a solution of this problem $(z^{\star},v^{\star})$ as a certainty-equivalent steady-state optimal (CE-SSO) state-input pair, and denote it as $(x^{sso},u^{sso})$. For some problems, such as the example considered in §6.2, the constant policy ${\phi{(x)}} = u^{sso}$ is a reasonable heuristic.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Certainty-equivalent model predictive control", "weight": 1.0} -->

Certainty-equivalent model predictive control (CE-MPC) is another heuristic policy for stochastic control. CE-MPC is not our focus, but the methods of this paper can also be used to develop a good CE-MPC policy.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Certainty-equivalent model predictive control", "weight": 1.0} -->

To evaluate the CE-MPC policy $\phi^{mpc}{(x)}$, we solve an $H$-step ahead planning problem with certainty-equivalent dynamics. The planning problem is

<!-- chunk {"id": "body-0053", "role": "body", "section": "Certainty-equivalent model predictive control", "weight": 1.0} -->

with variables $z_{1},\ldots,z_{H + 1}$ and $v_{1},\ldots,v_{H}$. The CE-MPC policy is then ${\phi^{mpc}{(x)}} = v_{1}^{\star}$, the first input of an optimal trajectory of the MPC planning problem..

<!-- chunk {"id": "body-0054", "role": "body", "section": "Certainty-equivalent model predictive control", "weight": 1.0} -->

In the CE-MPC problem, $V^{mpc}$ is called the terminal cost. It can be chosen to be zero (particularly when $H$ is large enough), or the indicator function of $x^{sso}$, an optimal certainty-equivalent steady-state state. Another very good choice is $\hat{V}$, an approximation of the value function, which can be found by the methods of this paper.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

In this paper, we consider ADP policies that replace the optimal value function $V^{\star}$ in with a convex approximation $\hat{V}$. The ADP policy is of the form

<!-- chunk {"id": "body-0056", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

(We omit the constant or offset term since it does not affect the associated policy.) If there are multiple minima, we can arbitrarily choose one. When $\hat{V}$ is a convex quadratic function, we refer to as a QADP policy.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

ADP is a heuristic that addresses the issue mentioned above, that there is no practical way to represent an arbitrary convex function on $\text{R}^{n}$. The approximate value function $\hat{V}$ is chosen to approximate $V^{\star}$ in some sense, and to make evaluating the policy tractable. Evaluating $\hat{\phi}$ is always a convex optimization problem; depending on the form of $g$ and $\hat{V}$, the expectation can simplify and the problem can reduce to a common form, such as a quadratic program (QP). When it is not possible to evaluate the expectation in the policy exactly, we can use an estimate obtained by replacing the expectation with a suitable sample average, i.e., a Monte Carlo approximation. ADP often works well in practice, even in cases when $\hat{V}$ is not a particularly good approximation of $V^{\star}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Quadratic approximate value functions", "weight": 1.0} -->

In this paper we focus exclusively on quadratic approximate value functions of the form

<!-- chunk {"id": "body-0059", "role": "body", "section": "Quadratic approximate value functions", "weight": 1.0} -->

where $P \succeq 0$, i.e., $P \in \text{S}_{+}^{n}$, the set of symmetric positive semidefinite (PSD) $n \times n$ matrices.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Quadratic approximate value functions", "weight": 1.0} -->

The QADP policy associated with $\hat{V}$ is parametrized by the $n \times n$ PSD matrix $P$ and $n$-vector $p$, which we collectively refer to as $\theta = {(P,p)}$. All together, the parameter $\theta$ contains

<!-- chunk {"id": "body-0061", "role": "body", "section": "Quadratic approximate value functions", "weight": 1.0} -->

scalar parameters, which has order $n^{2}$. We define $\Theta = {\{\theta\mid{P \succeq 0}\}}$, the set of parameters for which $\hat{V}$ is convex.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Properties of QADP policies", "weight": 1.0} -->

We now consider several properties of the QADP policies which will be useful in the sequel.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Simplifying the expectation", "weight": 1.0} -->

The QADP policy can be simplified, since the expectation of a quadratic function can be expressed analytically in terms of the first and second moments of its argument. Thus we have

<!-- chunk {"id": "body-0064", "role": "body", "section": "Simplifying the expectation", "weight": 1.0} -->

Note that $\mu{(x)}$ depends on $x$, and therefore is not constant, but the other coefficients $M$ and $m$ are constant and depend only on the first and second moments of $A$, $B$, $c$ (and $P$ and $p$). These formulas are derived in §A. Finally, we observe that $M$, $m$, and $\mu{(x)}$ are linear functions of $\theta$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluating the policy", "weight": 1.0} -->

Since $g{(x,u)}$ is convex, evaluating the quadratic ADP policy reduces to solving a deterministic convex optimization problem. When in addition $g{(x,u)}$ is QP-representable, i.e., a convex quadratic function plus a convex piecewise linear function, plus the indicator function of linear inequality and equality constraints, evaluating the QADP policy reduces to solving a QP.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Gradient of the Bellman operator image", "weight": 1.0} -->

Given convex quadratic $\hat{V}$, we may evaluate $\mathcal{T}\hat{V}{(x)}$, the Bellman operator applied to $\hat{V}$ at any state $x$, by solving the convex optimization problem associated with the QADP policy. We can also compute ${\nabla{\mathcal{T}\hat{V}}}{(x)}$, where it is differentiable, and a subgradient otherwise.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Gradient of the Bellman operator image", "weight": 1.0} -->

To do this, we represent $\mathcal{T}\hat{V}{(x)}$ as the optimal value of the convex optimization problem

<!-- chunk {"id": "body-0068", "role": "body", "section": "Fitted value iteration", "weight": 1.0} -->

We begin by reviewing fitted (or projected) value iteration (FVI), which is an approximation of value iteration. The issue with value iteration is that in practice, we cannot exactly represent the function $\mathcal{T}V^{k}$ in the update. FVI addresses this by restricting all approximate value function iterates $V^{k}$ to be convex quadratic functions.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Fitted value iteration", "weight": 1.0} -->

In the $k$th iteration, we choose a set of states $x^{1},\ldots,x^{N}$, and evaluate $\mathcal{T}V^{k}{(x^{i})}$ for each $i = {1,\ldots,N}$. We can evaluate each $\mathcal{T}V^{k}{(x^{i})}$ by evaluating, which is a convex optimization problem. Then, we fit a convex quadratic function $V^{k + {1/2}}$ to those points, such that

<!-- chunk {"id": "body-0070", "role": "body", "section": "Fitted value iteration", "weight": 1.0} -->

This leads to the damped fitted value iteration update

<!-- chunk {"id": "body-0071", "role": "body", "section": "Fitted value iteration", "weight": 1.0} -->

which generates a sequence of convex quadratic functions $V^{k}$, with associated QADP policies.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Fitting convex quadratic functions", "weight": 1.0} -->

One method for finding parameters $\theta = {(P,p)}$ for the convex quadratic function $V^{k + {1/2}}$ is to fit it to a set of points. We first evaluate $v^{i} = {\mathcal{T}V^{k}{(x^{i})}}$ for each $i = {1,\ldots,N}$, and then solve the fitting problem

<!-- chunk {"id": "body-0073", "role": "body", "section": "Fitting convex quadratic functions", "weight": 1.0} -->

with variables $\theta$ and $c \in \text{R}$, where $c$ is a scalar offset. Here $L:{\text{R}\rightarrow\text{R}}$ is a convex fitting loss function, and $r:{{\text{S}^{n} \times \text{R}^{n}}\rightarrow{\text{R} \cup {\{\infty\}}}}$ is a convex regularization function, with infinite values used to impose (convex) constraints on $\theta$. This is a convex optimization problem, since $V^{k + {1/2}}{(x^{i})}$ is a linear function of $\theta$. Possible choices for $L$ include the squared loss or the robust Huber loss, given by

<!-- chunk {"id": "body-0074", "role": "body", "section": "Fitting convex quadratic functions", "weight": 1.0} -->

The Huber loss is a more robust alternative to the square loss, in the presence of outliers. Possible choices for $r$ include $\ell_{2}$ regularization and prior knowledge constraints, and are discussed in §4.3. For simplicity, we consider the standard Huber function, which transitions from the quadratic to absolute value at $M = 1$. In general, $M$ may be tuned by cross-validation, using a procedure similar to that described in §4.3.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Convergence", "weight": 1.0} -->

Convergence guarantees for FVI are available when the approximation error of $\nabla{\mathcal{T}V^{k}}$ is small enough. However, unlike value iteration, FVI is not guaranteed to converge in general. Nevertheless, with an appropriate approximation $\hat{\nabla}\mathcal{T}V^{k}$ and damping parameters $\rho_{k}$, FVI can often find policies with good performance in practice.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Value-gradient iteration", "weight": 1.0} -->

VGI is a special case of FVI, where we fit $V^{k + {1/2}}$ using gradients instead of values. In §3.3, we showed that we can evaluate ${\nabla{\mathcal{T}V^{k}}}{(x)}$ at any state $x$ where $\mathcal{T}V^{k}$ is differentiable, by evaluating a particular optimal Lagrange multiplier. Therefore, we can find $V^{k + {1/2}}$ by fitting its gradient.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Value-gradient iteration", "weight": 1.0} -->

Once we have found $V^{k + {1/2}}$, we apply the damped update to generate the next iterate $V^{k + 1}$. Like in standard FVI, this generates a sequence of convex quadratic functions $V^{k}$, with associated QADP policies.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Fitting the gradient", "weight": 1.0} -->

In this case, we fit an affine function ${{\nabla V^{k + {1/2}}}{(x)}} = {{Px} + p}$ to a set of points, subject to the constraint that $P$ is symmetric positive semidefinite. In each iteration, we evaluate $g^{i} = {{\nabla{\mathcal{T}V^{k}}}{(x^{i})}}$ for each $i = {1,\ldots,N}$, and then solve the fitting problem

<!-- chunk {"id": "body-0079", "role": "body", "section": "Fitting the gradient", "weight": 1.0} -->

with variables $\theta$. Here $L:{\text{R}^{n}\rightarrow\text{R}}$ is a multivariate convex fitting loss function, and $r$ is, like, a convex regularization function. This is also a convex optimization problem, since ${\nabla V^{k + {1/2}}}{(x^{i})}$ is a linear function of $\theta$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Fitting the gradient", "weight": 1.0} -->

Possible choices for $L$ include the squared $\ell_{2}$ norm and the circular Huber loss

<!-- chunk {"id": "body-0081", "role": "body", "section": "Fitting the gradient", "weight": 1.0} -->

which extends the scalar Huber loss to the multivariate case. Like in the scalar case, the circular Huber loss is a more robust alternative to the square function, in the presence of outliers.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Choice of sampling points", "weight": 1.0} -->

An important consideration is the choice of the state samples values $x^{1},\ldots,x^{N}$ at which we evaluate the policy and $\mathcal{T}V^{k}{(x^{i})}$. Ideally the samples should reflect the states that the system is likely to be, i.e., samples from the steady-state distribution of $x_{t}$ under the policy $\phi^{k}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Choice of sampling points", "weight": 1.0} -->

To accomplish this we choose the sample points by simulating the current policy for $N$ steps, using the current policy $\phi^{k}$. In the first iteration $k = 1$, we initialize the simulation at a state chosen at random. In subsequent iterations, we initialize the simulation at the last state in the previous iteration.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Regularization, constraints, and lower bounds", "weight": 1.0} -->

Prior information, if available, can be incorporated as regularization terms or constraints in the fitting problem, through the function $r{(\theta)}$ in the fitting problem. Constraints and lower bounds may be imposed by setting $r$ to have value $\infty$ when $\theta$ is not consistent with the prior information. We now describe a nonexhaustive list of possibilities that may be combined to form $r{(\theta)}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Ridge regularization", "weight": 1.0} -->

We may add an $\ell_{2}$ penalty on the parameters of the value function

<!-- chunk {"id": "body-0086", "role": "body", "section": "Ridge regularization", "weight": 1.0} -->

where $\lambda > 0$ is a scalar regularization parameter and $\parallel \cdot \parallel_{F}$ denotes the Frobenius norm. The $\ell_{2}$ regularization ensures that the fitting problem is well-posed and helps mitigate overfitting, and is sometimes referred to as Tikhonov or ridge regularization.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Ridge regularization", "weight": 1.0} -->

The parameter $\lambda$ is typically chosen using use out-of-sample or cross-validation. To do this we divide the fitting data $(x^{i},v^{i})$ into two sets, the training data and the validation data. We fit $V$ using the training data, for a range of values of $\lambda$, typically on a log scale with upper limits $\lambda^{\max}$ and $\lambda^{\max}$, and then evaluate the average loss on the validation data for each value of $\lambda$. We then choose a value that gives near minimum validation error, with a preference for larger values, i.e., more regularization. This approach is often referred to as grid search. A more thorough method is to use cross-validation, and more sophisticated search methods for evaluating scaling parameters may also be considered; see, for example,.

<!-- chunk {"id": "body-0088", "role": "body", "section": "LASSO regularization", "weight": 1.0} -->

with regularization parameter $\lambda > 0$ is known as LASSO. This regularization is similar to ridge regression in that both shrink the values of the parameters; however, the LASSO is more likely to produce sparse solutions, i.e., $P$ and $p$ with zero-valued entries. Therefore, the LASSO regularization can be particularly useful for weakly coupled systems.

<!-- chunk {"id": "body-0089", "role": "body", "section": "LASSO regularization", "weight": 1.0} -->

Like with ridge regression, the value of $\lambda$ may be tuned using out-of-sample or cross-validation. When multiple regularization terms are used, we can use the same strategy to find a good set of values for each regularization parameter. For example, the case where both ridge and LASSO regularization are employed is known as the elastic net. In this case, the aforementioned grid search strategy may be used to select the two regularization parameters jointly.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Symmetry", "weight": 1.0} -->

In some cases, we may know that the value function $V$ should be symmetric, i.e., ${V{(x)}} = {V{({- x})}}$ for any $x \in \text{R}^{n}$. The LQR example considered in §6.1, for example, satisfies this property. For quadratic approximate value functions, symmetry may be implemented by the constraint $p = 0$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Fixed minimizer", "weight": 1.0} -->

When we can identify a point $x^{\star}$ in the state space that seems to be the best, we may include the constraint ${\operatorname{argmin}_{x}{V{(x)}}} = x^{\star}$ to the fitting problem. This is equivalent to the linear equality constraint ${{Px^{\star}} + p} = 0$. A special case is when $V$ is constrained to be symmetric, in which case $V{(x)}$ is minimized at zero.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

In some cases, a quadratic pointwise lower bound

<!-- chunk {"id": "body-0093", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

on $V^{\star}$ is available up to an additive constant, and may be included as an additional constraint. This may be done by introducing an additional variable $s$, and imposing the pointwise constraint ${V + s} \geq V^{lb}$. This can be expressed as the convex constraint

<!-- chunk {"id": "body-0094", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

as shown in §B. Since $P^{lb} \succeq 0$, this constraint implies that $P \succeq 0$. So when we add a quadratic lower bound constraint to the fitting problem, we no longer need the constraint $P \succeq 0$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

In many cases we can form a convex quadratic lower bound $V^{\text{lb}}$ on the true value function $V^{\star}$. In the simplest case we can take $V^{\star} = 0$ when the stage cost is nonnegative. Another method is to form an LQR relaxation of the problem, i.e., to replace $g$ with a quadratic lower bound, for example, by ignoring constraints on $u$. The resulting LQR problem can be solved exactly, and its value function $V^{lqr}$ is a lower bound on $V^{\star}$. More sophisticated methods for computing a lower bound on the value function involve solving a convex optimization problem or a series of convex problems.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

When the dynamics matrices $A_{t}$ and $B_{t}$ are random, a simpler lower bound may be found by considering the (deterministic) LQR relaxation of the CE problem; see §C.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Policy interpolation", "weight": 1.0} -->

Suppose we have a set of states $x^{1},\ldots,x^{B}$, and require that the policy takes on corresponding values $u^{1},\ldots,u^{B}$, i.e.,

<!-- chunk {"id": "body-0098", "role": "body", "section": "Policy interpolation", "weight": 1.0} -->

In some cases, this constraint has a simple representation. For example, if the stage cost may be written in the form

<!-- chunk {"id": "body-0099", "role": "body", "section": "Policy interpolation", "weight": 1.0} -->

where $h$ is differentiable and $I\left( {{(x,u)} \in C} \right)$ is the indicator function of a polyhedral set $C$, then the constraint may be written as a linear inequality constraint on the parameters $P$ and $p$. First, note that

<!-- chunk {"id": "body-0100", "role": "body", "section": "Policy interpolation", "weight": 1.0} -->

where $\partial{I\left( {{(x,u)} \in C} \right)}$ is the normal cone to $C$ at $(x^{j},u^{j})$. Since $C$ is a polyhedron the normal cone is also a polyhedron \[, §23\], i.e., representable by a set of linear inequality constraints. Next, from we have

<!-- chunk {"id": "body-0101", "role": "body", "section": "Policy interpolation", "weight": 1.0} -->

which is a linear function of $P$ and $p$. Therefore, the policy interpolation constraints may be represented by a set of linear inequality constraints on $P$ and $p$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Input-affine dynamics", "weight": 1.0} -->

The methods presented in this paper can also be applied in cases where the dynamics are nonlinear but input-affine. That is, the dynamics may be written in the form

<!-- chunk {"id": "body-0103", "role": "body", "section": "Input-affine dynamics", "weight": 1.0} -->

In the input-affine case, the ADP policy is of the form

<!-- chunk {"id": "body-0104", "role": "body", "section": "Input-affine dynamics", "weight": 1.0} -->

Since the dynamics are affine in $u$, the expected value $\mathbf{E}{\hat{V}{({{f_{t}{(x)}} + {g_{t}{(x)}u}})}}$ is also affine in $u$, when $\hat{V}$ is convex. When $\hat{V}$ is a convex quadratic function of the form, the expected value may be computed exactly, in terms of the first and second moments of $f_{t}{(x)}$ and $g_{t}{(x)}$. Hence, the policy can still be evaluated by solving a convex optimization problem, and VGI can still be performed in a similar manner.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Discounted infinite-horizon problem", "weight": 1.0} -->

The mean discounted infinite-horizon cost is given by

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discounted infinite-horizon problem", "weight": 1.0} -->

where $\gamma \in {}$ is a discount factor, and the sum and expectations are assumed to exist. In this case, the value function $V^{\star}$ represents the optimal cost-to-go, and the optimal policy is of the form

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discounted infinite-horizon problem", "weight": 1.0} -->

For the discounted infinite-horizon problem, VGI proceeds in the same way, except with the Bellman operator defined as

<!-- chunk {"id": "body-0108", "role": "body", "section": "Finite-horizon problem", "weight": 1.0} -->

In the finite-horizon problem, the cost is given by

<!-- chunk {"id": "body-0109", "role": "body", "section": "Finite-horizon problem", "weight": 1.0} -->

where the stage cost may be time-varying, and the expectations are assumed to exist. In this case, the value function $V_{t}^{\star}$ depends on time, and may be found using a backward recursion. The value iteration starts with

<!-- chunk {"id": "body-0110", "role": "body", "section": "Finite-horizon problem", "weight": 1.0} -->

where the Bellman operator at time $t$ is defined as

<!-- chunk {"id": "body-0111", "role": "body", "section": "Finite-horizon problem", "weight": 1.0} -->

VGI proceeds similarly for the finite-horizon problem, using an analogous function fitting approximation of the Bellman operator.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Parallel simulations", "weight": 1.0} -->

In VGI (and FVI in general), we select $N$ sample points by simulating the current policy. We can also select points from more than one simulated trajectory. To do this we choose the sample points by simulating $K$ different trajectories for $T$ steps each, using the current policy. In iteration $k$, each of these $K$ trajectories gives us $T$ states at which we evaluate the policy $\phi^{k}$, so all together we have $N = {TK}$ states and associated evaluations of $\nabla{\mathcal{T}V^{k}}$ to use in the fitting problem. One advantage of this method is that the $K$ trajectories can be evaluated in parallel.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In this section, we present three numerical examples, which involve a box-constrained LQR problem, a commitment planning problem with an alternative investments fund, and a supply chain optimization problem. Comparisons with other ADP methods are given in §7.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

The code for the examples is available at The ADP policies and VGI method are implemented using CVXPY. In addition, the code generation tool CVXPYgen \[SBD^+^22\] was used to create custom solvers for the ADP policies, implemented in C. The experiments were performed on two cores of an Intel Xeon E5-2640 CPU.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Box-constrained linear quadratic regulator", "weight": 1.0} -->

We first consider a traditional linear quadratic regulator (LQR) problem. The dynamics are time-invariant, and given by

<!-- chunk {"id": "body-0116", "role": "body", "section": "Box-constrained linear quadratic regulator", "weight": 1.0} -->

where $A \in \text{R}^{n \times n}$ and $B^{n \times m}$ are known and fixed, and $c_{t}$ is an IID random variable with zero mean and covariance ${\mathbf{E}{c_{t}c_{t}^{T}}} = C$. The stage cost is given by

<!-- chunk {"id": "body-0117", "role": "body", "section": "Box-constrained linear quadratic regulator", "weight": 1.0} -->

where $Q \succeq 0$, $R \succ 0$, and $u^{\max} > 0$ is a maximum input magnitude, in any component of the input.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Box-constrained linear quadratic regulator", "weight": 1.0} -->

For this problem, a lower bound $J^{\text{lb}}$ on the optimal cost and a quadratic lower bound $V^{\text{lb}}$ on the optimal value function can be found by solving a semidefinite program (SDP). An upper bound on the optimal cost may be found by evaluating the ADP policy using $V^{\text{lb}}$ as the approximate value function.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider a problem instance with $n = 12$ and $m = 3$. The entries of $A$ are chosen IID from a uniform distribution on $\lbrack{- 1},1\rbrack$. The matrix $A$ was then rescaled to have a maximum eigenvalue of 1. The entries of $B$ are chosen IID from a uniform distribution on $\lbrack{- 0.5},0.5\rbrack$. The process noise $c_{t}$ is normally distributed, with zero mean and covariance $0.4I$. The stage cost parameters are given by $Q = I$ and $R = I$, and the maximum input magnitude is $u^{\max} = 0.4$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Results", "weight": 1.0} -->

We carried out VGI for $40$ iterations, starting from the initial value function ${V^{1}{(x)}} = {x^{T}Qx}$. We included the symmetry constraint $p = 0$ in the fitting step. In each iteration, the fitting step was performed using $N = 50$ fitting points, obtained by simulating the current policy. The damping coefficient was fixed to $\rho_{k} = 0.5$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

Our next example is a practical example, and more specific. We consider a fund that invests in $m$ so-called alternative investment classes, such as venture capital, infrastructure projects, direct lending, or private equity. Alternative investments are found in the portfolios of insurance companies, retirement funds, and university endowments. For more details, see \[LBvB^+^22\] and the papers cited therein.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

In each time period (typically quarters) $t = {1,2,\ldots}$, we make nonnegative commitments to the $m$ alternative asset classes. These are amounts we promise to invest, in response to capital calls. Over the next few years, we put money into the investments in response to capital calls, up to the amount of previous commitments. We receive money from each the investments in later years through distributions. Neither the timing nor amounts of the capital calls and distributions are directly under our control, except that the total of the capital calls cannot exceed our total commitments for each asset class.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

We first describe some critical quantities.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

$u_{t} \in \text{R}_{+}^{m}$ denotes the amounts that the investor commits in period $t$, to each of the $m$ asset classes. (These commitments will be the input in our stochastic control problem.)

<!-- chunk {"id": "body-0125", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

$p_{t} \in \text{R}_{+}^{m}$ denotes the amounts that the investor pays in to the investment in response to capital calls in period $t$.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

$d_{t} \in \text{R}_{+}^{m}$ denotes the amount that the investor receives in distributions from the investments in period $t$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

$n_{t} \in \text{R}_{+}^{m}$ denotes the net asset values (NAVs) of the investments in period $t$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

$l_{t} \in \text{R}_{+}^{m}$ denotes the total amount of uncalled commitments, i.e., the difference between the total so far committed and the total so far that has been called. (This is a liability, so we use the symbol $l$.)

<!-- chunk {"id": "body-0129", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

The units for all of these is typically millions of USD.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

A simple dynamical model relating these variables is

<!-- chunk {"id": "body-0131", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

where $r_{t} \in \text{R}_{+ +}^{K}$ is the vector of per-period total returns for the asset classes, assumed to be IID with some known distribution such as log-normal. In words: the value of each investment class in each period is multiplied by its (random) return, increased by the amount paid, and decreased by the amount distributed; the total uncalled commitments is decreased by the capital calls, and increased by new commitments. The calls and distributions are modeled as

<!-- chunk {"id": "body-0132", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

where $\gamma_{t}^{\text{call}}$ and $\gamma_{t}^{\text{dist}}$ are random variables in ${}^{m}$, called the call and distribution intensities. We will assume that these are IID, and independent of $r_{t}$. In words: In each period and for each asset class, a random fraction of the total liability is called, and a random fraction of the NAV is distributed.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

We can express the dynamics as a random linear dynamical system with state $x_{t} = {(n_{t},l_{t})} \in \text{R}^{2m}$ and input $u_{t} \in \text{R}^{m}$, with dynamics matrices

<!-- chunk {"id": "body-0134", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

The goal is to choose commitments so as to reach and maintain a target asset allocation $n^{tar} \in \text{R}_{+}^{m}$, while penalizing deviations of the commitments $u_{t}$ from the CE-SSO commitment $u^{sso} \in \text{R}_{+}^{m}$. We consider stage cost

<!-- chunk {"id": "body-0135", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

where $\lambda > 0$ is a penalty coefficient and $u^{\max} \in \text{R}_{+}^{m}$ are the maximum allowable commitments to each of the asset classes. We take the fixed input $u^{sso}$ is a solution to the certainty-equivalent steady-state problem, with the input cost term $\lambda{\|{u_{t} - u^{sso}}\|}^{2}$ removed from the stage cost.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Commitments in an alternative investments fund", "weight": 1.0} -->

For this problem, we find a quadratic lower bound $V^{\text{lb}}$ on the value function by relaxing the constraints on the input $u_{t}$, replacing $A_{t}$ with $\overline{A}$, and solving the certainty equivalent LQR problem.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider an example with $m = 6$ asset classes. The returns $r_{t}$ are distributed according to a log-normal distribution, i.e., $r_{t} = {\exp{(z_{t})}}$, with $z_{t} \sim {\mathcal{N}{(\mu,\Sigma)}}$. The parameters $\mu$ and $\Sigma$ were chosen such that the mean quarterly returns have means

<!-- chunk {"id": "body-0138", "role": "body", "section": "Numerical example", "weight": 1.0} -->

This leads to annualized returns with means around $20\%$ and standard deviations around $30\%$. The returns are correlated, with correlation matrix

<!-- chunk {"id": "body-0139", "role": "body", "section": "Numerical example", "weight": 1.0} -->

These parameters lead to typical values of call and distribution intensities around $0.14$ and $0.16$ respectively. The target asset values $n^{\text{tar}}$ are chosen to be between 4 and 5, the maximum commitment is $u^{\max} = 3$, and the penalty coefficient was $\lambda = 0.01$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Results", "weight": 1.0} -->

We carried out VGI for $20$ iterations, starting from $V^{1} = V^{lb}$. In each iteration, the fitting step was performed using $N = 50$ fitting points, obtained by simulating the current policy. The damping coefficient was fixed to $\rho_{k} = 0.5$.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

In our final example, we consider the problem of shipping goods efficiently across a network of warehouses to maximize profit. We consider a single-good, multi-echelon supply chain with $\overset{\sim}{n}$ interconnected warehouses, which are represented by nodes in a graph. There are $m$ directed links over which goods can flow; $n_{s}$ links connect suppliers to nodes, $n_{c}$ links connect nodes to consumers, and $m - n_{s} - n_{c}$ links connect nodes to each other.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

The amount of good held at each node at time $t$ is represented by $h_{t} \in \text{R}_{+}^{\overset{\sim}{n}}$. The prices at which we can buy the good from the suppliers are denoted by $p_{t} \in \text{R}_{+}^{n_{s}}$, the fixed prices at which goods can be sold to consumers are denoted by $r \in \text{R}_{+}^{n_{c}}$, and the consumer demand is $d_{t} \in \text{R}_{+}^{n_{c}}$. The prices and demand are random and independent between time points, but are known at time $t$ for planning.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

The dynamics may be expressed as a random linear dynamical system with augmented state $x_{t} = {(h_{t},p_{t},d_{t})}$, input $u_{t} = {(b_{t},s_{t},z_{t})}$, and dynamics matrices

<!-- chunk {"id": "body-0144", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

The prices and demand $p_{t}$ and $d_{t}$ are included in the state since they are known at time $t$ for planning. However, since they are random and independent between time points, the value function need only be a function of $h_{t}$. Moreover, we only require that the stage cost be jointly convex in $(h_{t},u_{t})$.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

The goal is to maximize the revenue from selling goods to customers while minimizing the material costs paid to the suppliers, transportation costs, and holding costs of the goods at each node. Let $\tau \in \text{R}_{+}^{m}$ encode the costs of transporting a unit of good across each link, and $\alpha \in \text{R}_{+}^{n}$ and $\beta \in \text{R}_{+}^{n}$ parametrize the linear and quadratic holding costs of the goods at each node.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

The amounts shipped out should not exceed the current capacities: ${A^{\text{out}}u_{t}} \leq h_{t}$.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

The amounts sold to consumers cannot exceed the current demand: $s_{t} \leq d_{t}$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Supply chain optimization", "weight": 1.0} -->

For this example, we find a quadratic lower bound $V^{\text{lb}}$ on the value function by relaxing the constraints, adding the quadratic penalty ${u_{t}^{T}u_{t}} - {{({1/2})}u_{\max}\mathbf{1}^{\top}u_{t}}$ to the stage cost, and solving the resulting LQR problem. The lower bound is valid, since the added penalty is a pointwise lower bound on the indicator of the input constraints, which is zero for $0 \leq u_{t} \leq u_{\max}$, and infinity otherwise.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Numerical example", "weight": 1.0} -->

The holding cost parameters are $\alpha = \beta = {{(0.01)}\mathbf{1}}$, the transportation cost is $\tau = {{(0.05)}\mathbf{1}}$, and the consumer prices are $r = {{(1.3)}\mathbf{1}}$. The maximum warehouse capacities are $h_{\max} = {{}\mathbf{1}}$, and the maximum link capacities are $u_{\max} = {{}\mathbf{1}}$.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Results", "weight": 1.0} -->

We carried out VGI for $20$ iterations, starting from the quadratic lower bound $V^{lb}$. In each iteration, the fitting step was performed using $N = 50$ fitting points, obtained by simulating the current policy. The damping coefficient was fixed to $\rho_{k} = 0.5$. When solving the fitting problem, we add an $\ell_{2}$ (or ridge) regularization, with coefficient $\lambda = 10^{- 4}$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Results", "weight": 1.0} -->

On average, the VGI policy is able to keep the storage levels close to half capacity for all warehouses. On the other hand, the initial policy tends to put too much stock in the first warehouse with storage ${(h_{t})}_{1}$, which can, on average, buy goods at a lower price from the suppliers. Similarly, the policy tends to under-utilize the third warehouse with storage ${(h_{t})}_{3}$, which experiences lower consumer demand than the fourth warehouse with storage ${(h_{t})}_{4}$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Comparison with other methods", "weight": 1.0} -->

In this section, we evaluate VGI against two related ADP methods for finding a quadratic approximate value function: the standard FVI described in §4.1 and a COCP gradient method. They are iterative methods that follow the same pattern as VGI: at each iteration, we simulate the system for $N$ steps, and then use the resulting data to update the parameters of the quadratic approximate value function.

<!-- chunk {"id": "body-0153", "role": "body", "section": "COCP gradient method", "weight": 1.0} -->

We compare against a gradient based method that updates the parameters $\theta$ of the ADP policy using the derivatives of the cost along simulated trajectories, with respect to $\theta$. At iteration $k$, the policy $\phi^{k}$ with parameters $\theta^{k}$ is used to simulate the system for $N$ steps. The resulting data is used to compute an estimate of the average cost, given by

<!-- chunk {"id": "body-0154", "role": "body", "section": "COCP gradient method", "weight": 1.0} -->

We then compute ${\nabla\hat{J}}{(\theta^{k})}$ using the chain rule, and then update the parameters. This approach is known as backpropagation through time. In our experiments, we use the projected stochastic (sub)gradient rule $\theta^{k + 1} = {\Pi_{\Theta}{({\theta^{k} - {\alpha^{k}{\nabla\hat{J}}{(\theta^{k})}}})}}$, where $\Pi_{\Theta}$ is the projection onto $\Theta$, and $\alpha^{k} > 0$ is a step size.

<!-- chunk {"id": "body-0155", "role": "body", "section": "COCP gradient method", "weight": 1.0} -->

This approach requires derivatives of the policy with respect to its parameters. Those derivatives may be found by applying the implicit function theorem to the optimality conditions of the convex optimization problem associated with the policy \[AAB^+^19, \]. Examples of the COCP gradient method used to find quadratic approximate value functions may be found. In our experiments, we used cvxpylayers to compute the necessary derivatives \[AAB^+^19\].

<!-- chunk {"id": "body-0156", "role": "body", "section": "Results", "weight": 1.0} -->

In general, FVI and COCP gradient methods required more tuning of hyperparameters than VGI to work well. As shown in table 1, VGI achieves the best (or close to the best) performance in all three problems, all using far fewer policy evaluations than the FVI and COCP gradient methods. The costs were evaluated in each case by simulating the policy for ten thousand steps.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Results", "weight": 1.0} -->

VGI used the same hyperparameters as in §6, i.e., $\rho_{k} = 0.5$ and $N = 50$. The method was run for 40 iterations for the box-constrained LQR problem, 20 iterations for the commitments example, and 15 iterations for the supply chain problem.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Results", "weight": 1.0} -->

We now discuss the hyperparameters chosen for FVI and the COCP gradient method. All methods were initialized using the same initial quadratic approximate value function. For the box-constrained LQR problem we used ${V^{1}{(x)}} = {x^{T}Qx}$, and for the other two problems we used ${V^{1}{(x)}} = V^{\text{lb}}$, the quadratic lower bound on $V$ available for each problem.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Box constrained LQR", "weight": 1.0} -->

FVI was run using $N = 400$ policy evaluations, for a total of 50 iterations. The damping parameter was $\rho_{k} = 0.5$, and the symmetry constraint $p = 0$ was incorporated into the fitting problem.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Box constrained LQR", "weight": 1.0} -->

The COCP gradient method was run using $N = 300$ policy evaluations, for a total of 80 iterations. The $300$ sample points were generated by simulating $K = 3$ trajectories each of length $T = 100$, using the procedure described in §5.3. We used a step size of $\alpha^{k} = 0.01$. The method was initialized with $P = I$, and the symmetry constraint $p = 0$ was incorporated into the fitting problem. VGI took 6 seconds to complete, FVI took 29 seconds, and the COCP gradient method took 4 minutes and 10 seconds.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Commitments planning", "weight": 1.0} -->

FVI was run using $N = 200$ policy evaluations, for a total of $20$ iterations. The sample points were generated by simulating $K = 2$ trajectories each of length $T = 100$. The damping parameter was $\rho_{k} = 0.5$.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Commitments planning", "weight": 1.0} -->

The COCP gradient method was run using $N = 200$ policy evaluations, for a total of 100 iterations. The sample points were generated by simulating $K = 2$ trajectories each of length $T = 100$. We used a step size of $\alpha^{k} = 10^{- 4}$. VGI took 5 seconds to complete, FVI took 7 seconds, and the COCP gradient method took 5 minutes.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Supply chain", "weight": 1.0} -->

FVI was run using $N = 800$ policy evaluations, for a total of $20$ iterations. The sample points were generated by simulating $K = 2$ trajectories each of length $T = 400$. The damping parameter was $\rho_{k} = 0.75$. An $\ell_{2}$ regularization with coefficient $\lambda = 10^{- 4}$ was used in the fitting problem.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Supply chain", "weight": 1.0} -->

The COCP gradient method was run using $N = 1000$ policy evaluations, for a total of $70$ iterations. The sample points were generated by simulating $K = 10$ trajectories each of length $T = 100$. We used a step size of $\alpha^{k} = 0.01$. An $\ell_{2}$ regularization with coefficient $\lambda = 10^{- 4}$ was added to the cost. VGI took 2 seconds to complete, FVI took 25 seconds, and the COCP gradient method took 13 minutes.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we propose value-gradient iteration, a method for finding a quadratic approximate value function for convex stochastic control. The method is an approximation of value iteration, and we show how we may compute the gradient of the Bellman operator image to fit the gradient of the approximate value function in each iteration. By fitting the gradient of the approximate value function instead of the approximate value function itself, we can find a good policy using far less simulation data. Indeed, we find that the computational effort of obtaining a good approximate value function is comparable to that of evaluating the policy through simulation.
