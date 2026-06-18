<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Convex Optimization Control Policies

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many control policies used in various applications determine the input or action by solving a convex optimization problem that depends on the current state and some parameters. Common examples of such convex optimization control policies (COCPs) include the linear quadratic regulator (LQR), convex model predictive control (MPC), and convex control-Lyapunov or approximate dynamic programming (ADP) policies. These types of control policies are tuned by varying the parameters in the optimization problem, such as the LQR weights, to obtain good performance, judged by application-specific metrics. Tuning is often done by hand, or by simple methods such as a crude grid search. In this paper we propose a method to automate this process, by adjusting the parameters using an approximate gradient of the performance metric with respect to the parameters. Our method relies on recently developed methods that can efficiently evaluate the derivative of the solution of a convex optimization problem with respect to its parameters. We illustrate our method on several examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

We consider the control of a stochastic dynamical system with known dynamics, using a control policy that determines the input or action by solving a convex optimization problem. We call such policies *convex optimization control policies* (COCPs). Many practical policies have this form, including the first modern control policy, the linear quadratic regulator (LQR). In LQR, the convex optimization problem has quadratic objective and linear equality constraints, and so can be solved explicitly, yielding the familiar linear control policy. More modern examples, which rely on more complicated optimization problems such as quadratic programs (QPs), include convex model predictive control (MPC) and convex approximate dynamic programming (ADP). These policies are used in many applications, including robotics, vehicle control, rocket landing, supply chain optimization, and finance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

Control policies in general, and COCPs in particular, are judged by application-specific metrics; these metrics are evaluated using simulation with historical or simulated values of the unknown quantities. In some but not all cases, the metrics have the traditional form of the average value of a given stage cost. We consider here more general metrics that can be functions of the whole state and input trajectories. An example of such a metric is the expected drawdown of a portfolio over some time period, i.e., the expected value of the minimum future value of a portfolio.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

In a few cases, the optimal policy for a traditional stochastic control problem has COCP form. A well-known example is LQR. Another generic example is when the dynamics are affine and the stage cost is convex, in which case the Bellman value function is convex, and evaluating the optimal policy reduces to solving a convex optimization problem \[48, §3.3.1\]. While it is nice to know that in this case that the optimal policy has COCP form, we generally cannot express the value function in a form that allows us to evaluate the policy, so this observation is not useful in practice. In a far wider set of cases, a COCP policy is not optimal, but only a good, practical heuristic.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

COCPs have some attractive properties compared to other parametrized control policies. When the convex problem to be solved is well chosen, the policy is at least reasonable for any choice of the parameter values over the allowed set. As a specific example, consider a linear control policy parametrized by the gain matrix, which indeed would seem to be the most natural parametrization of a linear policy. The set of gain matrices that lead to a stable closed-loop system (a very minimal performance requirement) can be very complex, even disconnected. In contrast, consider an LQR control policy parametrized by a state and control cost matrix (constrained to be positive definite). In this case any choice of policy yields a stable closed-loop system. It is far easier and safer to tune parameters when any feasible choice leads to at least a reasonable policy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

All control policies are tuned by choosing various parameters that appear in them. In the case of COCPs, the parameters are in the optimization problem that is solved to evaluate the policy. The tuning is usually done based on simulation with historical disturbances (called *back-testing*) or synthetic disturbances. It is often done by hand, or by a crude grid search. A familiar example of this is tuning the weights in an LQR controller to obtain good practical performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

In this paper we present an automated method for tuning parameters in COCPs to achieve good values of a performance metric. Our method simulates the closed-loop system, i.e., the system with the policy in the loop, and computes an approximate (stochastic) gradient of the expected performance with respect to the parameters. It uses this gradient to update the parameters via a projected stochastic gradient method. Central to our method is the fact that the solution map for convex optimization problems is often differentiable, and its derivative can be efficiently computed. This is combined with relatively new implementations of automatic differentiation, widely used in training neural networks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

Our method is not guaranteed to find the best parameter values, since the performance metric is not a convex function of the COCP parameter values, and we use a local search method. This is not a problem in practice, since in a typical use case, the COCP is initialized with reasonable parameters, and our method is used to tune these parameters to improve the performance (sometimes considerably).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

The Markov decision process (MDP) is a general stochastic control problem that can be solved in principle using dynamic programming (DP). The optimal policy is evaluated by solving an optimization problem, one that includes a current stage cost and the expected value of cost-to-go or value function at the next state. This optimization problem corresponds to a COCP when the system dynamics are linear or affine and the stage cost is convex. Unfortunately, the value function can be found in a tractable form in only a few cases. A notable tractable case is when the cost is a convex extended quadratic and the dynamics are affine.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

ADP refers to heuristic solution methods for stochastic control problems that replace the value function in DP with an approximation, or search over a parametric family of policies \[22, §2.1\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

In many ADP methods, an offline optimization problem is solved to approximate the value function. When there are a finite number of state and inputs, the approximation problem can be written as a linear program (LP) by relaxing the Bellman equation to an inequality. When the dynamics are linear, the cost is quadratic, and the input is constrained to lie in a convex set, an approximate convex quadratic value function can be found by solving a particular semidefinite program (SDP). The quality of the approximation can also be improved by iterating the Bellman inequality. Because the approximate value function is convex quadratic and the dynamics are linear, the resulting policy is a COCP.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

Other methods approximate the cost-to-go by iteratively adjusting the approximate value function to satisfy the Bellman equation. Examples of these methods include projected value iteration or fitted Q-iteration, temporal difference learning, and approximate policy iteration. Notable applications of COCPs here include the use of quadratic approximate cost-to-go functions for input-affine systems with convex cost, which can be approximately fit using projected value iteration, and modeling the state-action cost-to-go function as an input-convex neural network \[7, §6.4\]. Other approximation schemes fit nonconvex value functions, so the resulting policies are not necessarily COCPs. Notably, when the parametrization involves a featurization computed by a deep neural network, the ADP method is an instance of deep reinforcement learning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

Other ADP methods parametrize the policy and tune the parameters directly to improve performance; this is often referred to as policy search or policy approximation \[22, §5.7\]. The most common method is gradient or stochastic gradient search \[63, §7.2\], which is the method we employ in this paper, with a parametrized COCP as the policy. Historically, the most widely used of these policy approximation methods is the Proportional-Integral-Derivative (PID) controller, which indeed can be tuned using gradient methods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Reinforcement learning", "weight": 1.0} -->

Reinforcement learning (RL) and adaptive control are essentially equivalent to ADP \[22, §1.4\], but with different notation and different emphasis. RL pays special attention to problems in which one does not possess a mathematical model of the dynamics or the expected cost, but has access to a computational simulator for both. Our method cannot be used directly in this setting, since we assume that we have mathematical descriptions of the dynamics and cost. However, our method might be used after learning a suitable model of the dynamics and cost. Alternatively, COCPs could be used as part of the policy in modern policy gradient or actor-critic algorithms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning optimization-based policies", "weight": 1.0} -->

Other work has considered tuning optimization-based control policies. For example, there is prior work on learning for MPC, including nonconvex MPC controllers, cost function shaping, differentiable path integral control, and system identification of terminal constraint sets and costs. As far as we are aware, our work is the first to consider the specific class of parametrized convex programs.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Real-time optimization", "weight": 1.0} -->

COCPs might be considered computationally expensive control policies compared to conventional analytical control policies such as the linear control policy prescribed by LQR. However, this is not the case in practice, thanks to fast embedded solvers and code generation tools that emit solvers specialized to parametric problems. For example, the aerospace and space transportation company SpaceX uses the QP code generation tool CVXGEN to land its rockets. COCPs based on MPC, which have many more variables and constraints than those based on ADP, can also be evaluated very efficiently, even at MHz rates.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Outline", "weight": 1.0} -->

In §2, we introduce the controller tuning problem that we wish to solve. In §3, we describe some common forms of COCPs. In §4, we propose a heuristic for the controller tuning problem. In §5, we apply our heuristic for tuning COCPs to examples in portfolio optimization, vehicle control, and supply-chain management. We conclude in §6 by discussing extensions and variations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "System dynamics", "weight": 1.0} -->

We consider a dynamical system with dynamics given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "System dynamics", "weight": 1.0} -->

At time period $t$, $x_{t} \in \text{R}^{n}$ is the state, $u_{t} \in \text{R}^{m}$ is the input or action, $w_{t} \in \mathcal{W}$ is the disturbance, and $f:{{\text{R}^{n} \times \text{R}^{m} \times \mathcal{W}}\rightarrow\text{R}^{n}}$ is the state transition function. The initial state $x_{0}$ and the disturbances $w_{t}$ are random variables. In the traditional stochastic control problem, it is assumed that $x_{0},w_{0},w_{1},\ldots$ are independent, with $w_{0},w_{1},\ldots$ identically distributed. We do not make this assumption.

<!-- chunk {"id": "body-0021", "role": "body", "section": "System dynamics", "weight": 1.0} -->

The inputs are given by a state feedback control policy,

<!-- chunk {"id": "body-0022", "role": "body", "section": "System dynamics", "weight": 1.0} -->

where $\phi:{\text{R}^{n}\rightarrow\text{R}^{m}}$ is the policy. In particular, we assume the state $x_{t}$ at time period $t$ is fully observable when the input $u_{t}$ is chosen. It will be clear later that this assumption is not really needed, since our method can be applied to an estimated state feedback policy, either with a fixed state estimator, or with a state estimator that is itself a parametrized convex problem (see §6).

<!-- chunk {"id": "body-0023", "role": "body", "section": "System dynamics", "weight": 1.0} -->

With the dynamics and policy, the state and input trajectories $x_{0},x_{1},\ldots$ and $u_{0},u_{1},\ldots$ form a stochastic process.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

We specifically consider COCPs, which have the form

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convex optimization control policies", "weight": 1.0} -->

where $f_{i}$ are convex in $u$ and $g_{i}$ are affine in $u$. To evaluate a COCP we must solve a convex optimization problem, which we assume has a unique solution. The convex optimization problem is given by a *parametrized problem description* \[30, §4.1.4\], in which the vector $\theta \in \Theta \subseteq \text{R}^{p}$ is the parameter ($\Theta$ is the set of allowable parameter values). The value of the parameter $\theta$ (and $x$) specifies a particular problem instance, and it can be adjusted to tune the control policy. The problem we address in this paper is the choice of the parameter $\theta$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Performance metric", "weight": 1.0} -->

We judge the performance of a control policy, or choice of control policy parameter $\theta$, by the average value of a cost over trajectories of length $T$. Here the horizon $T$ is chosen large enough so that the average over $T$ time steps is close enough to the long term average. We denote the trajectories over $t = {0,\ldots,T}$ as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Performance metric", "weight": 1.0} -->

where $N = {{({T + 1})}n}$ and $M = {{({T + 1})}m}$. These state, input, and disturbance trajectories are random variables, with distributions that depend on the parameter $\theta$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Performance metric", "weight": 1.0} -->

The cost is provided by a function $\psi:{{\text{R}^{N} \times \text{R}^{M} \times \mathcal{W}^{T + 1}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$. Infinite values of $\psi$ can be interpreted as encoding constraints on the trajectories. A policy is judged by the expected value of this cost,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Performance metric", "weight": 1.0} -->

We emphasize that $J$ depends on the control policy parameter $\theta$, since $x_{1},\ldots,x_{T}$ and $u_{0},\ldots,u_{T}$ depend on $\theta$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Performance metric", "weight": 1.0} -->

We mention that the traditional cost function is separable, with the form

<!-- chunk {"id": "body-0031", "role": "body", "section": "Performance metric", "weight": 1.0} -->

where $g:{{\text{R}^{n} \times \text{R}^{m} \times \mathcal{W}}\rightarrow{\text{R} \cup {\{\infty\}}}}$ is a stage cost function. However, we do not require a cost function that is separable across time.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Evaluating $J{(\\theta)}$", "weight": 1.0} -->

We generally cannot evaluate $J{(\theta)}$ exactly. Instead, assuming that we can sample the initial state and the disturbances, we can compute a Monte Carlo approximation of it. In the simplest version, we generate $K$ independent trajectories

<!-- chunk {"id": "body-0033", "role": "body", "section": "Evaluating $J{(\\theta)}$", "weight": 1.0} -->

This computation requires carrying out $K$ simulations over $T$ time steps, which involves solving $K{({T + 1})}$ convex optimization problems to evaluate $u_{t}^{i}$, $t = {0,\ldots,T}$, $i = {1,{\ldotsK}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Evaluating $J{(\\theta)}$", "weight": 1.0} -->

Evidently, $\hat{J}{(\theta)}$ is an unbiased approximation of $J{(\theta)}$, meaning

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluating $J{(\\theta)}$", "weight": 1.0} -->

The quality of this approximation increases as $K$ increases, since

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluating $J{(\\theta)}$", "weight": 1.0} -->

where $\operatorname{\mathbf{v}\mathbf{a}\mathbf{r}}$ denotes the variance; i.e., the variance goes to $0$ as $K$ gets large. Of course more sophisticated methods can be used to approximately evaluate $J{(\theta)}$, e.g., importance sampling (see ).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Controller tuning problem", "weight": 1.0} -->

The controller tuning problem has the form

<!-- chunk {"id": "body-0038", "role": "body", "section": "Controller tuning problem", "weight": 1.0} -->

with variable $\theta$. This is the problem we seek to solve in this paper.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Examples of COCPs", "weight": 1.0} -->

In this section we describe some common COCPs.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Optimal (dynamic programming) policy", "weight": 1.0} -->

In the traditional stochastic control setting, the cost function is the average of stage costs computed by a function $g$, as, and $x_{0},w_{0},w_{1},\ldots$ are independent. Under some technical conditions, the optimal policy for $T\rightarrow\infty$, i.e., the policy that minimizes $J$ over all possible state feedback policies, and not just those of COCP form, has the form

<!-- chunk {"id": "body-0041", "role": "body", "section": "Optimal (dynamic programming) policy", "weight": 1.0} -->

where $V:{\text{R}^{n}\rightarrow\text{R}}$ is the optimal cost-to-go or Bellman value function. This form of the optimal policy is sometimes called the dynamic programming (DP) form. When $f$ is affine in $x$ and $u$, and $g$ is convex in $x$ and $u$, it can be shown that the value function $V$ is convex \[48, §3.3.1\], so the expression to be minimized above is convex in $u$, and the optimal policy has COCP form (with no parameter $\theta$).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Optimal (dynamic programming) policy", "weight": 1.0} -->

Unfortunately the optimal value function $V$ can be expressed in tractable form in only a few special cases. One well-known one is LQR, which has dynamics and stage cost

<!-- chunk {"id": "body-0043", "role": "body", "section": "Optimal (dynamic programming) policy", "weight": 1.0} -->

with $A \in \text{R}^{n \times n}$, $B \in \text{R}^{n \times m}$, $Q \in \text{S}_{+}^{n}$ (the set of $n \times n$ symmetric positive semidefinite matrices), $R \in \text{S}_{+ +}^{m}$ (the set of symmetric positive definite matrices), and $w \sim {\mathcal{N}{(0,\Sigma)}}$. In this special case we can compute the value function, which is a convex quadratic ${V{(x)}} = {x^{T}Px}$, and the optimal policy has the form

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimal (dynamic programming) policy", "weight": 1.0} -->

Note that we can consider the policy above as a COCP, if we consider $P$ as our parameter $\theta$ (constrained to be positive semidefinite). Another option is to take $P = {\theta^{T}\theta}$, where $\theta \in \text{R}^{n \times n}$, so the COCP has objective

<!-- chunk {"id": "body-0045", "role": "body", "section": "Approximate dynamic programming policy", "weight": 1.0} -->

An ADP or control-Lyapunov policy has the form

<!-- chunk {"id": "body-0046", "role": "body", "section": "Approximate dynamic programming policy", "weight": 1.0} -->

where $\hat{V}$ is an approximation of the value function for which the minimization over $u$ above is tractable. When $g$ is convex in $u$, $f$ is affine in $u$, and $\hat{V}$ is convex, the minimization above is a convex optimization problem. With a suitable parametrization of $\hat{V}$, this policy has COCP form.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Model predictive control policy", "weight": 1.0} -->

Suppose the cost function has the form, with stage cost $g$. In an MPC policy, the input is determined by solving an approximation to the control problem over a short horizon, where the unknown disturbances are replaced by predictions, and applying only the first input. A terminal cost function $g_{H}$ is often included in the optimization.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Model predictive control policy", "weight": 1.0} -->

An MPC policy has the form

<!-- chunk {"id": "body-0049", "role": "body", "section": "Model predictive control policy", "weight": 1.0} -->

where $H$ is the planning horizon and ${\hat{w}}_{0},\ldots,{\hat{w}}_{H - 1}$ are the predicted disturbances. This optimization problem has variables $u_{0},\ldots,u_{H - 1}$ and $x_{0},\ldots,x_{H}$; however, the $\operatorname{argmin}$ is over $u_{0}$ since in MPC we only apply the first input.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Model predictive control policy", "weight": 1.0} -->

When $f$ is affine in $(x,u)$, $g$ is convex in $(x,u)$, and the terminal cost function $g_{H}$ is convex, the minimization above is a convex optimization problem. With a suitable parametrization of the terminal cost function $g_{H}$, the MPC policy has COCP form. When $f$ is not affine or $g$ is not convex, they can be replaced with parametrized convex approximations. The function that predicts the disturbances can also be parametrized (see §6).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Solution method", "weight": 1.0} -->

Solving the controller tuning problem exactly is in general hard, especially when the number of parameters $p$ is large, so we will solve it approximately. Historically, many practitioners have used derivative-free methods to tune the parameters in control policies. Some of these methods include CMA-ES and other evolutionary strategies, Bayesian optimization, grid search, and random search. Many more methods are catalogued. These methods can certainly yield improvements over an initialization; however, they often converge very slowly.

<!-- chunk {"id": "body-0052", "role": "body", "section": "A gradient-based method", "weight": 1.0} -->

It is well-known that first-order optimization methods, which make use of derivatives, can outperform derivative-free methods. In this paper, we apply the projected stochastic (sub)gradient method to approximately solve. That is, starting with initial parameters $\theta^{0}$, at iteration $k$, we simulate the system and compute $\hat{J}{(\theta^{k})}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "A gradient-based method", "weight": 1.0} -->

We then compute an unbiased stochastic gradient of $J$, $g^{k} = {{\nabla\hat{J}}{(\theta^{k})}}$, by the chain rule or backpropagation through time (BPTT), and update the parameters according to the rule $\theta^{k + 1} = {\Pi_{\Theta}{({\theta^{k} - {\alpha^{k}g^{k}}})}}$, where $\Pi_{\Theta}{(\theta)}$ denotes the Euclidean projection of $\theta$ onto $\Theta$ and $\alpha^{k} > 0$ is a step size. Of course more sophisticated methods can be used to update the parameters, for example, those that employ momentum, variance reduction, or second-order information (see and the references therein for some of these methods).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Computing $g^{k}$", "weight": 1.0} -->

The computation of $g^{k}$ requires differentiating through the dynamics $f$, the cost $\psi$, and, notably, the solution map $\phi$ of a convex optimization problem. Methods for differentiating through special subclasses of convex optimization have existed for many decades; for example, literature on differentiating through QPs dates back to at least the 1960s. Similarly, it is well known that if the objective function and constraint functions of a convex optimization problem are all smooth, and some regularity conditions are satisfied, then its derivative can be computed by differentiating through the KKT optimality conditions. Until very recently, however, it was not generically possible to differentiate through a convex optimization problem with nondifferentiable objective or constraints; recent work has shown how to efficiently and easily compute this derivative.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Non-differentiability", "weight": 1.0} -->

Until this point, we have assumed the differentiability of all of the functions involved ($f$, $\psi$, and $\phi$). In real applications, these functions very well may not be differentiable everywhere. So long as the functions are differentiable almost everywhere, however, it is reasonable to speak of applying a projected stochastic gradient method to. At non-differentiable points, we compute a heuristic quantity. For example, at some non-differentiable points of $\phi$, a certain matrix fails to be invertible, and we compute a least-squares approximation of the derivative instead, as. In this sense, we overload the notation ${\nabla f}{(x)}$ to denote a gradient when $f$ is differentiable at $x$, or some heuristic quantity (a "gradient") when $f$ is not differentiable at $x$. In practice, as our examples in §5 demonstrate, we find that this method works well.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Non-differentiability", "weight": 1.0} -->

Indeed, most neural networks that are trained today are not differentiable (e.g., the rectified linear unit or positive part is a nondifferentiable activation function that is widely used) or even subdifferentiable (since neural networks are usually nonconvex), but it is nonetheless possible to train them, successfully, using stochastic "gradient" descent.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section, we present examples that illustrate our method. Our control policies were implemented using CVXPY, and we used cvxpylayers and PyTorch to differentiate through them; cvxpylayers uses the open-source package SCS to solve convex optimization problems. For each example, we give the dynamics, the cost, the COCP under consideration, and the result of applying our method to a numerical instance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Examples", "weight": 1.0} -->

In the numerical instances, we pick the number of simulations $K$ so that the variance of $\hat{J}{(\theta)}$ is sufficiently small, and we tune the step-size schedule $\alpha^{k}$ for each problem. BPTT is susceptible to exploding and vanishing gradients, which can make learning difficult. This issue can be mitigated by gradient clipping and regularization, which we do in some of our experiments.

<!-- chunk {"id": "body-0059", "role": "body", "section": "LQR", "weight": 1.0} -->

We first apply our method to the classical LQR problem, with dynamics and cost

<!-- chunk {"id": "body-0060", "role": "body", "section": "Policy", "weight": 1.0} -->

with parameter $\theta \in \text{R}^{n \times n}$. This policy is linear, of the form ${\phi{(x)}} = {Gx}$, with

<!-- chunk {"id": "body-0061", "role": "body", "section": "Policy", "weight": 1.0} -->

This COCP is clearly over-parametrized; for example, for any orthogonal matrix $U$, $U\theta$ gives the identical policy as $\theta$. If the matrix $\theta^{T}\theta$ satisfies a particular algebraic Riccati equation involving $A$, $B$, $Q$, and $R$, then is optimal (over all control policies) for the case $T\rightarrow\infty$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider a numerical example with $n = 4$ states, $m = 2$ inputs, and $T = 100$. The entries of $A$ and $B$ were sampled from the standard normal distribution, and we scaled $A$ such that its spectral radius was one. The cost matrices are $Q = I$ and $R = I$, and the noise covariance is $W = {{(0.25)}I}$. We initialize $\theta$ with the identity. We trained our policy for 50 iterations, using $K = 6$ simulations per step, starting with a step size of 0.5 that was decreased to 0.1 after 25 iterations. Figure 1 plots the average cost of the COCP during learning versus the average cost of the optimal LQR policy (in the case $T\rightarrow\infty$). Our method appears to converge to near the optimal cost in just 10 iterations.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Box-constrained LQR", "weight": 1.0} -->

Unlike the LQR problem, in general, there is no known exact solution to the box-constrained problem, analytical or otherwise. Sophisticated methods can be used, however, to compute a lower bound on the true optimal cost.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Policy", "weight": 1.0} -->

with parameter $\theta \in \text{R}^{n \times n}$. The lower bound found in yields a policy that has this same form, for a particular value of $\theta$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We use $n = 8$ states, $m = 2$ inputs, $T = 100$, $u_{\max} = 0.1$, and data generated as in the LQR example above. The lower bounding technique from yields a lower bound on optimal cost of around 11. It also suggests a particular value of $\theta$, which gives average cost around 13, an upper bound on the optimal cost that we suspect is the true optimal average cost. We initialize our COCP with $\theta = P^{1/2}$, where $P$ comes from the cost-to-go function for the unconstrained (LQR) problem. Figure 2 plots the expected cost of our COCP, and the expected cost of the upper and lower bounds suggested. Our method converges to roughly the same cost as the upper bound.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

In 1952, Markowitz introduced an optimization-based method for the allocation of financial portfolios, which trades off risk (measured as return variance), and (expected) return. While the original formulation involved only a quadratic objective and linear equality constraints (very much like LQR), with the addition of other constraints and terms, Markowitz's method becomes a sophisticated COCP. The parameters are the data that appear in the convex problem solved to determine the trades to execute in each time period.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

In this example, we learn the parameters in a Markowitz policy to maximize a utility on the realized returns. We will use notation, representing the state by $w_{t}$, the control by $z_{t}$, and the disturbance by $r_{t}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

The portfolio under consideration has $n$ assets. The dollar value of the portfolio in period $t$ is denoted by $v_{t}$, which we assume to be positive. Our holdings in period $t$, normalized by the portfolio value, are denoted by $w_{t} \in \text{R}^{n}$; the normalization ensures that ${\mathbf{1}^{T}w_{t}} = 1$. The number $v_{t}{(w_{t})}_{i}$ is the dollar value of our position in asset $i$ (${(w_{t})}_{i} < 0$ corresponds to a short position). In each period, we re-allocate our holdings by executing trades $z_{t} \in \text{R}^{n}$, which are also normalized by $v_{t}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

Selling or shorting asset $i$ corresponds to ${(z_{t})}_{i} < 0$, and purchasing it corresponds to ${(z_{t})}_{i} > 0$. Trades incur transaction costs $\kappa^{T}{|z_{t}|}$, where $\kappa \in \text{R}_{+ +}^{n}$ (the set of positive $n$-vectors) is the vector of transaction cost rates and the absolute value is applied elementwise. Shorting also incurs a cost, which we express by $\nu^{T}{({w_{t} + z_{t}})}_{-}$, where $\nu \in \text{R}_{+ +}^{n}$ is the vector of stock loan rates and ${( \cdot )}_{-}$ is the negative part. We impose the condition that trades are self-financing, i.e., we must withdraw enough cash to pay the transaction and shorting costs incurred by our trades.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

The holdings evolve according to the dynamics

<!-- chunk {"id": "body-0071", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

where $r_{t} \in \text{R}_{+}^{n}$ are the total returns (which are IID) and $\circ$ is the elementwise product. The denominator in this expression is the return realized by executing the trade $z_{t}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Tuning a Markowitz policy to maximize utility", "weight": 1.0} -->

Our goal is to minimize the average negative utility of the realized returns, as measured by a utility function $U:{\text{R}\rightarrow\text{R}}$. Letting $W$, $Z$ and $R$ denote the state, input, and disturbance trajectories, the cost function is

<!-- chunk {"id": "body-0073", "role": "body", "section": "Policy", "weight": 1.0} -->

with variables $w^{+}$ and $z$ and parameters $\theta = {(\mu,\gamma,S)}$, where $\mu \in \text{R}^{n}$, $\gamma \in \text{R}_{+}$, and $S \in \text{R}^{n \times n}$. In a Markowitz formulation, $\mu$ is set to the empirical mean $\mu^{mark}$ of the returns, and $S$ is set to the square root of the return covariance $\Sigma^{mark}$. With these values for the parameters, the linear term in the objective represents the expected return of the post-trade portfolio $w^{+}$, and the quadratic term represents the risk. A trade-off between the risk and return is determined by the choice of the risk-aversion parameter $\gamma$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Policy", "weight": 1.0} -->

We mention that it is conventional to parametrize a Markowitz policy with a matrix $\Sigma \in \mathbf{S}_{+}^{n}$, rewriting the quadratic term as ${}_{}^{}\Sigmaw^{+}$; as in the LQR example, our policy is over-parametrized.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Policy", "weight": 1.0} -->

In addition to the self-financing condition, there are many other constraints one may want to impose on the trade vector and the post-trade portfolio, including constraints on the portfolio leverage and turnover, many of which are convex. For various examples of such constraints, see \[29, §4.4, §4.5\].

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We use $n = 12$ ETFs as the universe of assets,

<!-- chunk {"id": "body-0077", "role": "body", "section": "Numerical example", "weight": 1.0} -->

AGG, VTI, VNQ, XLF, XLV, XLY, XLP, XLU, XLI, XLE, IBB, and ITA.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Numerical example", "weight": 1.0} -->

For the transaction rates and stock loan rates, we use $\kappa = \nu = {{(0.001)}\mathbf{1}}$, or $0.1$ percent. We assume the investor is somewhat risk-averse, with utility function

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical example", "weight": 1.0} -->

The policy is initialized with $\mu = \mu^{mark}$, $S = {(\Sigma^{mark})}^{1/2}$, and $\gamma = 15$. Each simulation starts with the portfolio obtained by solving

<!-- chunk {"id": "body-0080", "role": "body", "section": "Numerical example", "weight": 1.0} -->

with variable $w \in \text{R}^{n}$. The portfolio evolves according to returns sampled from a log-normal distribution. This distribution was fit to monthly returns (including dividends) from Dec. 2006 through Dec. 2018, retrieved from the Center for Research in Security Prices.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We train the policy using stochastic gradient descent over $400$ iterations, with a horizon of $T = 24$ months and $K = 10$ simulations to evaluate $\hat{J}{(\theta)}$. (The step size is initialized to $10^{- 3}$, halved every $100$ iterations.) Figure 3 plots the per-iteration cost on a held-out random seed while training. The policy's performance improved by approximately $32$ percent, decreasing from an initial cost of $- 0.004$ to $- 0.0053$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In particular, the entry corresponding to AGG, a bond ETF, decreased from $1.003$ to $0.999$, and the entry for ITA, an aerospace and defense ETF, increased from $1.011$ to $1.013$; this observation is consistent with the plotted simulated holdings.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Numerical example", "weight": 1.0} -->

Tuning had essentially no effect on $\gamma$, which decreased from $15$ to $14.99$. The difference between $\Sigma^{mark}$ and $S^{T}S$, however, was significant: the median absolute percentage deviation between the entries of these two quantities was $2.6$ percent.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Tuning a vehicle controller to track curved paths", "weight": 1.0} -->

We consider a vehicle moving relative to a smooth path, with state and input

<!-- chunk {"id": "body-0085", "role": "body", "section": "Tuning a vehicle controller to track curved paths", "weight": 1.0} -->

Here, at time period $t$, $e_{t}$ is the lateral path deviation ($m$), $\Delta\psi_{t}$ is the heading deviation from the path ($rad$), $v_{t}$ is the velocity ($m/s$), $v_{t}^{des}$ is the desired velocity ($m/s$), $\kappa_{t}$ is the current curvature (i.e., inverse radius) of the path ($1/m$), $a_{t}$ is the acceleration ($m/s^{2}$), and $z_{t} ≔ {{\tan{(\delta_{t})}} - {L\kappa_{t}}}$, where $\delta_{t}$ is the wheel angle ($rad$) and $L$ is the vehicle's wheelbase ($m$).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Dynamics", "weight": 1.0} -->

We consider kinematic bicycle model dynamics in path coordinates, discretized at $h = {0.2\ s}$, with random processes for $v_{t}^{des}$ and $\kappa_{t}$, of the form

<!-- chunk {"id": "body-0087", "role": "body", "section": "Dynamics", "weight": 1.0} -->

The disturbances $w_{1},w_{2},w_{3}$ represent uncertainty in our model, and $w_{4},\ldots,w_{7}$ form the random process for the desired speed and path.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Cost", "weight": 1.0} -->

Our goal is to travel the desired speed ($v_{t} \approx v_{t}^{des}$), while tracking the path ($e_{t} \approx 0$, ${\Delta\psi} \approx 0$) and expending minimal control effort ($a_{t} \approx 0$, $z_{t} \approx 0$). We consider the cost

<!-- chunk {"id": "body-0089", "role": "body", "section": "Cost", "weight": 1.0} -->

for positive $\lambda_{1},\ldots,\lambda_{4}$ (with proper units), where

<!-- chunk {"id": "body-0090", "role": "body", "section": "Cost", "weight": 1.0} -->

for given maximum acceleration magnitude $a_{\max}$ ($m/s^{2}$) and maximum wheel angle magnitude $\delta_{\max}$ ($rad$).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We use the initial state $x_{0} = {(.5,.1,3,4.5,0)}$. We run the stochastic gradient method for $100$ iterations using $K = 6$ simulations and a step size of 0.1. We initialize the parameters with $S = I$ and $q = 0$. Over the course of learning, the cost decreased from $3.978$ to $0.971$. Figure 5 plots per-iteration cost on a held-out random seed while training. Figure 6 plots untuned and tuned sample paths on a single held-out instance. The resulting parameters are

<!-- chunk {"id": "body-0092", "role": "body", "section": "Tuning a supply chain policy to maximize profit", "weight": 1.0} -->

Supply chain management considers how to ship goods across a network of warehouses to maximize profit. In this example, we consider a single-good supply chain with $n$ nodes representing interconnected warehouses linked to suppliers and consumers by $m$ directed links over which goods can flow. There are $k$ links connecting suppliers to warehouses and $c$ links connecting warehouses to consumers. The remaining $m - k - c$ links are internode links.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Tuning a supply chain policy to maximize profit", "weight": 1.0} -->

We represent the amount of good held at each node as $h_{t} \in \text{R}_{+}^{n}$ (the set of nonnegative $n$-vectors). The prices at which we can buy the good from the suppliers are denoted $p_{t} \in \text{R}_{+}^{k}$, the (fixed) prices at which we can sell the goods to consumers are denoted $r \in \text{R}_{+}^{c}$, and the customer demand is denoted $d_{t} \in \text{R}_{+}^{c}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Tuning a supply chain policy to maximize profit", "weight": 1.0} -->

Our inputs are $b_{t} \in \text{R}_{+}^{k}$, the quantity of the good that we buy from the suppliers, $s_{t} \in \text{R}_{+}^{c}$, the quantity that we sell to the consumers, and $z_{t} \in \text{R}_{+}^{m - k - c}$, the quantity that we ship across the internode links. The state and inputs are

<!-- chunk {"id": "body-0095", "role": "body", "section": "Tuning a supply chain policy to maximize profit", "weight": 1.0} -->

The input and state are constrained in several ways. Warehouses have maximum capacities given by $h_{\max} \in \text{R}_{+}^{n}$, i.e., $h_{t} \leq h_{\max}$ (where the inequalities are elementwise), and links have maximum capacities given by $u_{\max} \in \text{R}_{+}^{m}$, i.e., $u_{t} \leq u_{\max}$. In addition, the amount of goods shipped out of a node cannot be more than the amount on hand, or ${A^{out}u_{t}} \leq h_{t}$. Finally, we require that we sell no more than the demand, or $s_{t} \leq d_{t}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Tuning a supply chain policy to maximize profit", "weight": 1.0} -->

We model the unknown future supplier prices and demands as random disturbances $w_{t} = {(p_{t + 1},d_{t + 1})}$ with joint log-normal distribution, i.e., ${\log w_{t}} = {({\log p_{t + 1}},{\log d_{t + 1}})} \sim {\mathcal{N}{(\mu,\Sigma)}}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Tuning a supply chain policy to maximize profit", "weight": 1.0} -->

The goal of our supply chain is to maximize profit, which depends on several quantities. Our payment to the suppliers is $p_{t}^{T}b_{t}$, we obtain revenues $r^{T}s_{t}$ for selling the good to consumers, and we incur a shipment cost $\tau^{T}z_{t}$, where $\tau \in \text{R}_{+}^{m - k - c}$ is the cost of shipping a unit of good across the internode links. We also incur a cost for holding or storing $h_{t}$ in the warehouses; this is represented by a quadratic function ${\alpha^{T}h_{t}} + {\beta^{T}h_{t}^{2}}$, where ${\alpha,\beta} \in \text{R}_{+ +}^{n}$ and the square is elementwise. Our cost is our average negative profit, or

<!-- chunk {"id": "body-0098", "role": "body", "section": "Policy", "weight": 1.0} -->

The policy seeks to maximize profit by computing $(b_{t},s_{t},z_{t})$ as

<!-- chunk {"id": "body-0099", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider a supply chain over horizon $T = 20$ with $n = 4$ nodes, $m = 8$ links, $k = 2$ supply links, and $c = 2$ consumer links. The initial value of the network storage is chosen uniformly between $0$ and $h_{\max}$, i.e., $h_{0} \sim {\mathcal{U}{(0,h_{\max})}}$. The log supplier prices and consumer demands have mean and covariance

<!-- chunk {"id": "body-0100", "role": "body", "section": "Numerical example", "weight": 1.0} -->

Therefore, the supplier prices have mean $(1.02,1.13)$ and the consumer demands have mean $(1.02,1.52)$. The consumer prices are $r = {{(1.4)}\mathbf{1}}$. We set the maximum nodes capacity to $h_{\max} = {{}\mathbf{1}}$ and links capacity to $u_{\max} = {{}\mathbf{1}}$. The storage cost parameters are $\alpha = \beta = {{(0.01)}\mathbf{1}}$. Node $1$ is connected to the supplier with lower average price and node $4$ to the consumer with higher demand.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We initialize the parameters of our policy to $S = I$ and $q = {- h_{\max}}$. In this way, the approximate value function is centered at $h_{\max}/2$ so that we try to keep the storage of each node at medium capacity.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We ran our method over $200$ iterations, with $K = 10$ using the stochastic gradient method with step size $0.05$. Figure 7 shows the per-iteration cost on a held-out random seed while training. Over the course of training the cost decreased by $22.35$ percent from $- 0.279$ to $- 0.341$. The resulting parameters are

<!-- chunk {"id": "body-0103", "role": "body", "section": "Numerical example", "weight": 1.0} -->

The diagonal of $S^{T}S$ shows that the learned policy especially penalizes storing goods in nodes connected to more expensive suppliers, e.g., node $2$, or to consumers with lower demand, e.g., node $3$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Estimation", "weight": 1.0} -->

Our approach is not limited to tuning policies for control. As we alluded to before, our approach can also be used to learn convex optimization state estimators, for example Kalman filters or moving horizon estimators. The setup is exactly the same, in that we learn or tune parameters that appear in the state estimation procedure to maximize some performance metric. (A similar approach was adopted, where the authors fit parameters in a Kalman smoother to observed data.) Also, since COCPs are applied to the estimated state, we can in fact jointly tune parameters in the COCP along with the parameters in the state estimator.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Prediction", "weight": 1.0} -->

In an MPC policy, one could tune parameters in the function that predicts the disturbances together with the controller parameters. As a specific example, we mention that the parameters in a Markowitz policy, such as the expected return, could be computed using a parametrized prediction function, and this function could be tuned jointly with the other parameters in the COCP.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Nonconvex optimization control policies (NCOCPs)", "weight": 1.0} -->

An NCOCP is an optimization-based control policy that is evaluated by solving a *nonconvex* optimization problem. Parameters in NCOCPs can be tuned in the same way that we tune COCPs in this paper. Although the solution to a nonconvex optimization problem might be nonunique or hard to find, one can differentiate a local solution map to a smooth nonconvex optimization problem by implicitly differentiating the KKT conditions. This is done, where the authors define an MPC-based NCOCP.
