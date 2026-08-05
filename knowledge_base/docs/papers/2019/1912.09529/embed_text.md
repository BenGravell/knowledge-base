<!-- arxiv-full-text:v1 {"arxiv_id": "1912.09529", "source": "ar5iv"} -->

## Introduction

### Convex optimization control policies

We consider the control of a stochastic dynamical system with known dynamics, using a control policy that determines the input or action by solving a convex optimization problem. We call such policies *convex optimization control policies* (COCPs). Many practical policies have this form, including the first modern control policy, the linear quadratic regulator (LQR). In LQR, the convex optimization problem has quadratic objective and linear equality constraints, and so can be solved explicitly, yielding the familiar linear control policy. More modern examples, which rely on more complicated optimization problems such as quadratic programs (QPs), include convex model predictive control (MPC) and convex approximate dynamic programming (ADP). These policies are used in many applications, including robotics, vehicle control, rocket landing, supply chain optimization, and finance.

Control policies in general, and COCPs in particular, are judged by application-specific metrics; these metrics are evaluated using simulation with historical or simulated values of the unknown quantities. In some but not all cases, the metrics have the traditional form of the average value of a given stage cost. We consider here more general metrics that can be functions of the whole state and input trajectories. An example of such a metric is the expected drawdown of a portfolio over some time period, i.e., the expected value of the minimum future value of a portfolio.

In a few cases, the optimal policy for a traditional stochastic control problem has COCP form. A well-known example is LQR. Another generic example is when the dynamics are affine and the stage cost is convex, in which case the Bellman value function is convex, and evaluating the optimal policy reduces to solving a convex optimization problem \[48, §3.3.1\]. While it is nice to know that in this case that the optimal policy has COCP form, we generally cannot express the value function in a form that allows us to evaluate the policy, so this observation is not useful in practice. In a far wider set of cases, a COCP policy is not optimal, but only a good, practical heuristic.

COCPs have some attractive properties compared to other parametrized control policies. When the convex problem to be solved is well chosen, the policy is at least reasonable for any choice of the parameter values over the allowed set. As a specific example, consider a linear control policy parametrized by the gain matrix, which indeed would seem to be the most natural parametrization of a linear policy. The set of gain matrices that lead to a stable closed-loop system (a very minimal performance requirement) can be very complex, even disconnected. In contrast, consider an LQR control policy parametrized by a state and control cost matrix (constrained to be positive definite). In this case any choice of policy yields a stable closed-loop system. It is far easier and safer to tune parameters when any feasible choice leads to at least a reasonable policy.

All control policies are tuned by choosing various parameters that appear in them. In the case of COCPs, the parameters are in the optimization problem that is solved to evaluate the policy. The tuning is usually done based on simulation with historical disturbances (called *back-testing*) or synthetic disturbances. It is often done by hand, or by a crude grid search. A familiar example of this is tuning the weights in an LQR controller to obtain good practical performance.

In this paper we present an automated method for tuning parameters in COCPs to achieve good values of a performance metric. Our method simulates the closed-loop system, i.e., the system with the policy in the loop, and computes an approximate (stochastic) gradient of the expected performance with respect to the parameters. It uses this gradient to update the parameters via a projected stochastic gradient method. Central to our method is the fact that the solution map for convex optimization problems is often differentiable, and its derivative can be efficiently computed. This is combined with relatively new implementations of automatic differentiation, widely used in training neural networks.

Our method is not guaranteed to find the best parameter values, since the performance metric is not a convex function of the COCP parameter values, and we use a local search method. This is not a problem in practice, since in a typical use case, the COCP is initialized with reasonable parameters, and our method is used to tune these parameters to improve the performance (sometimes considerably).

### Related work

### Dynamic programming

The Markov decision process (MDP) is a general stochastic control problem that can be solved in principle using dynamic programming (DP). The optimal policy is evaluated by solving an optimization problem, one that includes a current stage cost and the expected value of cost-to-go or value function at the next state. This optimization problem corresponds to a COCP when the system dynamics are linear or affine and the stage cost is convex. Unfortunately, the value function can be found in a tractable form in only a few cases. A notable tractable case is when the cost is a convex extended quadratic and the dynamics are affine.

### Approximate dynamic programming

ADP refers to heuristic solution methods for stochastic control problems that replace the value function in DP with an approximation, or search over a parametric family of policies \[22, §2.1\].

In many ADP methods, an offline optimization problem is solved to approximate the value function. When there are a finite number of state and inputs, the approximation problem can be written as a linear program (LP) by relaxing the Bellman equation to an inequality. When the dynamics are linear, the cost is quadratic, and the input is constrained to lie in a convex set, an approximate convex quadratic value function can be found by solving a particular semidefinite program (SDP). The quality of the approximation can also be improved by iterating the Bellman inequality. Because the approximate value function is convex quadratic and the dynamics are linear, the resulting policy is a COCP.

Other methods approximate the cost-to-go by iteratively adjusting the approximate value function to satisfy the Bellman equation. Examples of these methods include projected value iteration or fitted Q-iteration, temporal difference learning, and approximate policy iteration. Notable applications of COCPs here include the use of quadratic approximate cost-to-go functions for input-affine systems with convex cost, which can be approximately fit using projected value iteration, and modeling the state-action cost-to-go function as an input-convex neural network \[7, §6.4\]. Other approximation schemes fit nonconvex value functions, so the resulting policies are not necessarily COCPs. Notably, when the parametrization involves a featurization computed by a deep neural network, the ADP method is an instance of deep reinforcement learning.

Other ADP methods parametrize the policy and tune the parameters directly to improve performance; this is often referred to as policy search or policy approximation \[22, §5.7\]. The most common method is gradient or stochastic gradient search \[63, §7.2\], which is the method we employ in this paper, with a parametrized COCP as the policy. Historically, the most widely used of these policy approximation methods is the Proportional-Integral-Derivative (PID) controller, which indeed can be tuned using gradient methods.

### Reinforcement learning

Reinforcement learning (RL) and adaptive control are essentially equivalent to ADP \[22, §1.4\], but with different notation and different emphasis. RL pays special attention to problems in which one does not possess a mathematical model of the dynamics or the expected cost, but has access to a computational simulator for both. Our method cannot be used directly in this setting, since we assume that we have mathematical descriptions of the dynamics and cost. However, our method might be used after learning a suitable model of the dynamics and cost. Alternatively, COCPs could be used as part of the policy in modern policy gradient or actor-critic algorithms.

### Learning optimization-based policies

Other work has considered tuning optimization-based control policies. For example, there is prior work on learning for MPC, including nonconvex MPC controllers, cost function shaping, differentiable path integral control, and system identification of terminal constraint sets and costs. As far as we are aware, our work is the first to consider the specific class of parametrized convex programs.

### Real-time optimization

COCPs might be considered computationally expensive control policies compared to conventional analytical control policies such as the linear control policy prescribed by LQR. However, this is not the case in practice, thanks to fast embedded solvers and code generation tools that emit solvers specialized to parametric problems. For example, the aerospace and space transportation company SpaceX uses the QP code generation tool CVXGEN to land its rockets. COCPs based on MPC, which have many more variables and constraints than those based on ADP, can also be evaluated very efficiently, even at MHz rates.

### Outline

In §2, we introduce the controller tuning problem that we wish to solve. In §3, we describe some common forms of COCPs. In §4, we propose a heuristic for the controller tuning problem. In §5, we apply our heuristic for tuning COCPs to examples in portfolio optimization, vehicle control, and supply-chain management. We conclude in §6 by discussing extensions and variations.

## Controller tuning problem

### System dynamics

We consider a dynamical system with dynamics given by At time period $t$, $x_{t} \in \text{R}^{n}$ is the state, $u_{t} \in \text{R}^{m}$ is the input or action, $w_{t} \in \mathcal{W}$ is the disturbance, and $f:{{\text{R}^{n} \times \text{R}^{m} \times \mathcal{W}}\rightarrow\text{R}^{n}}$ is the state transition function. The initial state $x_{0}$ and the disturbances $w_{t}$ are random variables. In the traditional stochastic control problem, it is assumed that $x_{0},w_{0},w_{1},\ldots$ are independent, with $w_{0},w_{1},\ldots$ identically distributed. We do not make this assumption.

The inputs are given by a state feedback control policy, where $\phi:{\text{R}^{n}\rightarrow\text{R}^{m}}$ is the policy. In particular, we assume the state $x_{t}$ at time period $t$ is fully observable when the input $u_{t}$ is chosen. It will be clear later that this assumption is not really needed, since our method can be applied to an estimated state feedback policy, either with a fixed state estimator, or with a state estimator that is itself a parametrized convex problem (see §6).

With the dynamics and policy, the state and input trajectories $x_{0},x_{1},\ldots$ and $u_{0},u_{1},\ldots$ form a stochastic process.

### Convex optimization control policies

We specifically consider COCPs, which have the form where $f_{i}$ are convex in $u$ and $g_{i}$ are affine in $u$. To evaluate a COCP we must solve a convex optimization problem, which we assume has a unique solution. The convex optimization problem is given by a *parametrized problem description* \[30, §4.1.4\], in which the vector $\theta \in \Theta \subseteq \text{R}^{p}$ is the parameter ($\Theta$ is the set of allowable parameter values). The value of the parameter $\theta$ (and $x$) specifies a particular problem instance, and it can be adjusted to tune the control policy. The problem we address in this paper is the choice of the parameter $\theta$.

### Performance metric

We judge the performance of a control policy, or choice of control policy parameter $\theta$, by the average value of a cost over trajectories of length $T$. Here the horizon $T$ is chosen large enough so that the average over $T$ time steps is close enough to the long term average. We denote the trajectories over $t = {0,\ldots,T}$ as where $N = {{({T + 1})}n}$ and $M = {{({T + 1})}m}$. These state, input, and disturbance trajectories are random variables, with distributions that depend on the parameter $\theta$.

The cost is provided by a function $\psi:{{\text{R}^{N} \times \text{R}^{M} \times \mathcal{W}^{T + 1}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$. Infinite values of $\psi$ can be interpreted as encoding constraints on the trajectories. A policy is judged by the expected value of this cost, We emphasize that $J$ depends on the control policy parameter $\theta$, since $x_{1},\ldots,x_{T}$ and $u_{0},\ldots,u_{T}$ depend on $\theta$.

We mention that the traditional cost function is separable, with the form where $g:{{\text{R}^{n} \times \text{R}^{m} \times \mathcal{W}}\rightarrow{\text{R} \cup {\{\infty\}}}}$ is a stage cost function. However, we do not require a cost function that is separable across time.

### Evaluating $J{(\theta)}$

We generally cannot evaluate $J{(\theta)}$ exactly. Instead, assuming that we can sample the initial state and the disturbances, we can compute a Monte Carlo approximation of it. In the simplest version, we generate $K$ independent trajectories and form the approximation This computation requires carrying out $K$ simulations over $T$ time steps, which involves solving $K{({T + 1})}$ convex optimization problems to evaluate $u_{t}^{i}$, $t = {0,\ldots,T}$, $i = {1,{\ldotsK}}$.

Evidently, $\hat{J}{(\theta)}$ is an unbiased approximation of $J{(\theta)}$, meaning The quality of this approximation increases as $K$ increases, since where $\operatorname{\mathbf{v}\mathbf{a}\mathbf{r}}$ denotes the variance; i.e., the variance goes to $0$ as $K$ gets large. Of course more sophisticated methods can be used to approximately evaluate $J{(\theta)}$, e.g., importance sampling (see).

### Controller tuning problem

The controller tuning problem has the form with variable $\theta$. This is the problem we seek to solve in this paper.

## Examples of COCPs

In this section we describe some common COCPs.

### Optimal (dynamic programming) policy

In the traditional stochastic control setting, the cost function is the average of stage costs computed by a function $g$, as, and $x_{0},w_{0},w_{1},\ldots$ are independent. Under some technical conditions, the optimal policy for $T\rightarrow\infty$, i.e., the policy that minimizes $J$ over all possible state feedback policies, and not just those of COCP form, has the form where $V:{\text{R}^{n}\rightarrow\text{R}}$ is the optimal cost-to-go or Bellman value function. This form of the optimal policy is sometimes called the dynamic programming (DP) form. When $f$ is affine in $x$ and $u$, and $g$ is convex in $x$ and $u$, it can be shown that the value function $V$ is convex \[48, §3.3.1\], so the expression to be minimized above is convex in $u$, and the optimal policy has COCP form (with no parameter $\theta$).

Unfortunately the optimal value function $V$ can be expressed in tractable form in only a few special cases. One well-known one is LQR, which has dynamics and stage cost with $A \in \text{R}^{n \times n}$, $B \in \text{R}^{n \times m}$, $Q \in \text{S}_{+}^{n}$ (the set of $n \times n$ symmetric positive semidefinite matrices), $R \in \text{S}_{+ +}^{m}$ (the set of symmetric positive definite matrices), and $w \sim {\mathcal{N}{(0,\Sigma)}}$. In this special case we can compute the value function, which is a convex quadratic ${V{(x)}} = {x^{T}Px}$, and the optimal policy has the form Note that we can consider the policy above as a COCP, if we consider $P$ as our parameter $\theta$ (constrained to be positive semidefinite). Another option is to take $P = {\theta^{T}\theta}$, where $\theta \in \text{R}^{n \times n}$, so the COCP has objective

### Approximate dynamic programming policy

An ADP or control-Lyapunov policy has the form where $\hat{V}$ is an approximation of the value function for which the minimization over $u$ above is tractable. When $g$ is convex in $u$, $f$ is affine in $u$, and $\hat{V}$ is convex, the minimization above is a convex optimization problem. With a suitable parametrization of $\hat{V}$, this policy has COCP form.

### Model predictive control policy

Suppose the cost function has the form, with stage cost $g$. In an MPC policy, the input is determined by solving an approximation to the control problem over a short horizon, where the unknown disturbances are replaced by predictions, and applying only the first input. A terminal cost function $g_{H}$ is often included in the optimization.

An MPC policy has the form where $H$ is the planning horizon and ${\hat{w}}_{0},\ldots,{\hat{w}}_{H - 1}$ are the predicted disturbances. This optimization problem has variables $u_{0},\ldots,u_{H - 1}$ and $x_{0},\ldots,x_{H}$; however, the $\operatorname{argmin}$ is over $u_{0}$ since in MPC we only apply the first input.

When $f$ is affine in $(x,u)$, $g$ is convex in $(x,u)$, and the terminal cost function $g_{H}$ is convex, the minimization above is a convex optimization problem. With a suitable parametrization of the terminal cost function $g_{H}$, the MPC policy has COCP form. When $f$ is not affine or $g$ is not convex, they can be replaced with parametrized convex approximations. The function that predicts the disturbances can also be parametrized (see §6).

## Solution method

Solving the controller tuning problem exactly is in general hard, especially when the number of parameters $p$ is large, so we will solve it approximately. Historically, many practitioners have used derivative-free methods to tune the parameters in control policies. Some of these methods include CMA-ES and other evolutionary strategies, Bayesian optimization, grid search, and random search. Many more methods are catalogued . These methods can certainly yield improvements over an initialization; however, they often converge very slowly.

### A gradient-based method

It is well-known that first-order optimization methods, which make use of derivatives, can outperform derivative-free methods. In this paper, we apply the projected stochastic (sub)gradient method to approximately solve. That is, starting with initial parameters $\theta^{0}$, at iteration $k$, we simulate the system and compute $\hat{J}{(\theta^{k})}$. We then compute an unbiased stochastic gradient of $J$, $g^{k} = {{\nabla\hat{J}}{(\theta^{k})}}$, by the chain rule or backpropagation through time (BPTT), and update the parameters according to the rule $\theta^{k + 1} = {\Pi_{\Theta}{({\theta^{k} - {\alpha^{k}g^{k}}})}}$, where $\Pi_{\Theta}{(\theta)}$ denotes the Euclidean projection of $\theta$ onto $\Theta$ and $\alpha^{k} > 0$ is a step size. Of course more sophisticated methods can be used to update the parameters, for example, those that employ momentum, variance reduction, or second-order information (see and the references therein for some of these methods).

### Computing $g^{k}$

The computation of $g^{k}$ requires differentiating through the dynamics $f$, the cost $\psi$, and, notably, the solution map $\phi$ of a convex optimization problem. Methods for differentiating through special subclasses of convex optimization have existed for many decades; for example, literature on differentiating through QPs dates back to at least the 1960s. Similarly, it is well known that if the objective function and constraint functions of a convex optimization problem are all smooth, and some regularity conditions are satisfied, then its derivative can be computed by differentiating through the KKT optimality conditions. Until very recently, however, it was not generically possible to differentiate through a convex optimization problem with nondifferentiable objective or constraints; recent work has shown how to efficiently and easily compute this derivative.

### Non-differentiability

Until this point, we have assumed the differentiability of all of the functions involved ($f$, $\psi$, and $\phi$). In real applications, these functions very well may not be differentiable everywhere. So long as the functions are differentiable almost everywhere, however, it is reasonable to speak of applying a projected stochastic gradient method to. At non-differentiable points, we compute a heuristic quantity. For example, at some non-differentiable points of $\phi$, a certain matrix fails to be invertible, and we compute a least-squares approximation of the derivative instead, as . In this sense, we overload the notation ${\nabla f}{(x)}$ to denote a gradient when $f$ is differentiable at $x$, or some heuristic quantity (a "gradient") when $f$ is not differentiable at $x$. In practice, as our examples in §5 demonstrate, we find that this method works well. Indeed, most neural networks that are trained today are not differentiable (e.g., the rectified linear unit or positive part is a nondifferentiable activation function that is widely used) or even subdifferentiable (since neural networks are usually nonconvex), but it is nonetheless possible to train them, successfully, using stochastic "gradient" descent.

## Examples

In this section, we present examples that illustrate our method. Our control policies were implemented using CVXPY, and we used cvxpylayers and PyTorch to differentiate through them; cvxpylayers uses the open-source package SCS to solve convex optimization problems. For each example, we give the dynamics, the cost, the COCP under consideration, and the result of applying our method to a numerical instance.

In the numerical instances, we pick the number of simulations $K$ so that the variance of $\hat{J}{(\theta)}$ is sufficiently small, and we tune the step-size schedule $\alpha^{k}$ for each problem. BPTT is susceptible to exploding and vanishing gradients, which can make learning difficult. This issue can be mitigated by gradient clipping and regularization, which we do in some of our experiments.

### LQR

We first apply our method to the classical LQR problem, with dynamics and cost where $A \in \text{R}^{n \times n}$, $B \in \text{R}^{n \times m}$, $Q \in \text{S}_{+}^{n}$, $R \in \text{S}_{+ +}^{m}$, and $w \sim {\mathcal{N}{(0,\Sigma)}}$.

### Policy

We use the COCP with parameter $\theta \in \text{R}^{n \times n}$. This policy is linear, of the form ${\phi{(x)}} = {Gx}$, with This COCP is clearly over-parametrized; for example, for any orthogonal matrix $U$, $U\theta$ gives the identical policy as $\theta$. If the matrix $\theta^{T}\theta$ satisfies a particular algebraic Riccati equation involving $A$, $B$, $Q$, and $R$, then is optimal (over all control policies) for the case $T\rightarrow\infty$.

Figure 1: Tuning an LQR policy.

### Numerical example

We consider a numerical example with $n = 4$ states, $m = 2$ inputs, and $T = 100$. The entries of $A$ and $B$ were sampled from the standard normal distribution, and we scaled $A$ such that its spectral radius was one. The cost matrices are $Q = I$ and $R = I$, and the noise covariance is $W = {{(0.25)}I}$. We initialize $\theta$ with the identity. We trained our policy for 50 iterations, using $K = 6$ simulations per step, starting with a step size of 0.5 that was decreased to 0.1 after 25 iterations. Figure 1 plots the average cost of the COCP during learning versus the average cost of the optimal LQR policy (in the case $T\rightarrow\infty$). Our method appears to converge to near the optimal cost in just 10 iterations.

### Box-constrained LQR

A box-constrained LQR problem has the same dynamics and cost as LQR, with an additional constraint ${\| u_{t}\|}_{\infty} \leq u_{\max}$: Unlike the LQR problem, in general, there is no known exact solution to the box-constrained problem, analytical or otherwise. Sophisticated methods can be used, however, to compute a lower bound on the true optimal cost.

### Policy

Our COCP is an ADP policy with a quadratic value function: with parameter $\theta \in \text{R}^{n \times n}$. The lower bound found in yields a policy that has this same form, for a particular value of $\theta$.

### Numerical example

We use $n = 8$ states, $m = 2$ inputs, $T = 100$, $u_{\max} = 0.1$, and data generated as in the LQR example above. The lower bounding technique from yields a lower bound on optimal cost of around 11. It also suggests a particular value of $\theta$, which gives average cost around 13, an upper bound on the optimal cost that we suspect is the true optimal average cost. We initialize our COCP with $\theta = P^{1/2}$, where $P$ comes from the cost-to-go function for the unconstrained (LQR) problem. Figure 2 plots the expected cost of our COCP, and the expected cost of the upper and lower bounds suggested . Our method converges to roughly the same cost as the upper bound.

Figure 2: Tuning a box-constrained LQR policy.

### Tuning a Markowitz policy to maximize utility

In 1952, Markowitz introduced an optimization-based method for the allocation of financial portfolios, which trades off risk (measured as return variance), and (expected) return. While the original formulation involved only a quadratic objective and linear equality constraints (very much like LQR), with the addition of other constraints and terms, Markowitz's method becomes a sophisticated COCP. The parameters are the data that appear in the convex problem solved to determine the trades to execute in each time period.

In this example, we learn the parameters in a Markowitz policy to maximize a utility on the realized returns. We will use notation , representing the state by $w_{t}$, the control by $z_{t}$, and the disturbance by $r_{t}$.

The portfolio under consideration has $n$ assets. The dollar value of the portfolio in period $t$ is denoted by $v_{t}$, which we assume to be positive. Our holdings in period $t$, normalized by the portfolio value, are denoted by $w_{t} \in \text{R}^{n}$; the normalization ensures that ${\mathbf{1}^{T}w_{t}} = 1$. The number $v_{t}{(w_{t})}_{i}$ is the dollar value of our position in asset $i$ (${(w_{t})}_{i} < 0$ corresponds to a short position). In each period, we re-allocate our holdings by executing trades $z_{t} \in \text{R}^{n}$, which are also normalized by $v_{t}$. Selling or shorting asset $i$ corresponds to ${(z_{t})}_{i} < 0$, and purchasing it corresponds to ${(z_{t})}_{i} > 0$. Trades incur transaction costs $\kappa^{T}{|z_{t}|}$, where $\kappa \in \text{R}_{+ +}^{n}$ (the set of positive $n$-vectors) is the vector of transaction cost rates and the absolute value is applied elementwise. Shorting also incurs a cost, which we express by $\nu^{T}{({w_{t} + z_{t}})}_{-}$, where $\nu \in \text{R}_{+ +}^{n}$ is the vector of stock loan rates and ${( \cdot )}_{-}$ is the negative part. We impose the condition that trades are self-financing, i.e., we must withdraw enough cash to pay the transaction and shorting costs incurred by our trades. This can be expressed as ${{\mathbf{1}^{T}z_{t}} + {\kappa^{T}{|z_{t}|}} + {\nu^{T}{({w_{t} + z_{t}})}_{-}}} \leq 0$.

The holdings evolve according to the dynamics where $r_{t} \in \text{R}_{+}^{n}$ are the total returns (which are IID) and $\circ$ is the elementwise product. The denominator in this expression is the return realized by executing the trade $z_{t}$.

Our goal is to minimize the average negative utility of the realized returns, as measured by a utility function $U:{\text{R}\rightarrow\text{R}}$. Letting $W$, $Z$ and $R$ denote the state, input, and disturbance trajectories, the cost function is where $I:{\text{R}^{n}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ enforces the self-financing condition: $I{(z_{t})}$ is $0$ when ${{\mathbf{1}^{T}z_{t}} + {\kappa^{T}{|z_{t}|}} + {\nu^{T}{({w_{t} + z_{t}})}_{-}}} \leq 0$ and $+ \infty$ otherwise.

### Policy

We consider policies that compute $z_{t}$ as with variables $w^{+}$ and $z$ and parameters $\theta = {(\mu,\gamma,S)}$, where $\mu \in \text{R}^{n}$, $\gamma \in \text{R}_{+}$, and $S \in \text{R}^{n \times n}$. In a Markowitz formulation, $\mu$ is set to the empirical mean $\mu^{mark}$ of the returns, and $S$ is set to the square root of the return covariance $\Sigma^{mark}$. With these values for the parameters, the linear term in the objective represents the expected return of the post-trade portfolio $w^{+}$, and the quadratic term represents the risk. A trade-off between the risk and return is determined by the choice of the risk-aversion parameter $\gamma$. We mention that it is conventional to parametrize a Markowitz policy with a matrix $\Sigma \in \mathbf{S}_{+}^{n}$, rewriting the quadratic term as $w_{}^{+ T}\Sigmaw^{+}$; as in the LQR example, our policy is over-parametrized.

In addition to the self-financing condition, there are many other constraints one may want to impose on the trade vector and the post-trade portfolio, including constraints on the portfolio leverage and turnover, many of which are convex. For various examples of such constraints, see \[29, §4.4, §4.5\].

### Numerical example

Figure 3: Tuning a Markowitz policy.

We use $n = 12$ ETFs as the universe of assets, AGG, VTI, VNQ, XLF, XLV, XLY, XLP, XLU, XLI, XLE, IBB, and ITA.

For the transaction rates and stock loan rates, we use $\kappa = \nu = {{(0.001)}\mathbf{1}}$, or $0.1$ percent. We assume the investor is somewhat risk-averse, with utility function The policy is initialized with $\mu = \mu^{mark}$, $S = {(\Sigma^{mark})}^{1/2}$, and $\gamma = 15$. Each simulation starts with the portfolio obtained by solving with variable $w \in \text{R}^{n}$. The portfolio evolves according to returns sampled from a log-normal distribution. This distribution was fit to monthly returns (including dividends) from Dec. 2006 through Dec. 2018, retrieved from the Center for Research in Security Prices.

Figure 4: Simulated holdings (top row) and trades (bottom row) for untuned (left column) and tuned (right column) policies.

We train the policy using stochastic gradient descent over $400$ iterations, with a horizon of $T = 24$ months and $K = 10$ simulations to evaluate $\hat{J}{(\theta)}$. (The step size is initialized to $10^{- 3}$, halved every $100$ iterations.) Figure 3 plots the per-iteration cost on a held-out random seed while training. The policy's performance improved by approximately $32$ percent, decreasing from an initial cost of $- 0.004$ to $- 0.0053$.

Figure 4 plots simulated holdings and trades before and after tuning. Throughout the simulations, both the untuned and tuned policies regulated or re-balanced their holdings to track the initial portfolio, making small trades when their portfolios began to drift. The parameter $\mu$ was adjusted from its initial value, In particular, the entry corresponding to AGG, a bond ETF, decreased from $1.003$ to $0.999$, and the entry for ITA, an aerospace and defense ETF, increased from $1.011$ to $1.013$; this observation is consistent with the plotted simulated holdings.

Tuning had essentially no effect on $\gamma$, which decreased from $15$ to $14.99$. The difference between $\Sigma^{mark}$ and $S^{T}S$, however, was significant: the median absolute percentage deviation between the entries of these two quantities was $2.6$ percent.

### Tuning a vehicle controller to track curved paths

We consider a vehicle moving relative to a smooth path, with state and input Here, at time period $t$, $e_{t}$ is the lateral path deviation ($m$), $\Delta\psi_{t}$ is the heading deviation from the path ($rad$), $v_{t}$ is the velocity ($m/s$), $v_{t}^{des}$ is the desired velocity ($m/s$), $\kappa_{t}$ is the current curvature (i.e., inverse radius) of the path ($1/m$), $a_{t}$ is the acceleration ($m/s^{2}$), and $z_{t} ≔ {{\tan{(\delta_{t})}} - {L\kappa_{t}}}$, where $\delta_{t}$ is the wheel angle ($rad$) and $L$ is the vehicle's wheelbase ($m$).

### Dynamics

We consider kinematic bicycle model dynamics in path coordinates, discretized at $h = {0.2\ s}$, with random processes for $v_{t}^{des}$ and $\kappa_{t}$, of the form The disturbances $w_{1},w_{2},w_{3}$ represent uncertainty in our model, and $w_{4},\ldots,w_{7}$ form the random process for the desired speed and path.

### Cost

Our goal is to travel the desired speed ($v_{t} \approx v_{t}^{des}$), while tracking the path ($e_{t} \approx 0$, ${\Delta\psi} \approx 0$) and expending minimal control effort ($a_{t} \approx 0$, $z_{t} \approx 0$). We consider the cost for positive $\lambda_{1},\ldots,\lambda_{4}$ (with proper units), where for given maximum acceleration magnitude $a_{\max}$ ($m/s^{2}$) and maximum wheel angle magnitude $\delta_{\max}$ ($rad$).

### Policy

We consider a COCP that computes $(a_{t},z_{t})$ as with parameters $\theta = {(S,q)}$, where $S \in \text{R}^{4 \times 4}$ and $q \in \text{R}^{4}$. The additional variable $y \in \text{R}^{4}$ represents relevant portions of the next state, since $y_{1} = e_{t + 1}$, $y_{2} = {\Delta\psi_{t + 1}}$, $y_{3} = {v_{t + 1} - {\mathbf{E}{\lbrack v_{t + 1}^{des}\rbrack}}}$, and $y_{4} \approx e_{t + 2}$ (since it assumes $a_{t} = 0$). Therefore, this COCP is an ADP policy and the term ${\|{Sy}\|}_{2}^{2} + {q^{T}y}$ can be interpreted as the approximate value function.

Figure 5: Tuning a vehicle controller.

Figure 6: Left: untuned policy. Right: tuned policy. Black line is the path and the gray triangles represent the position and orientation of the vehicle. The tuned policy is able to track the path better and go faster.

### Numerical example

We consider a numerical example with We use the initial state $x_{0} = {(.5,.1,3,4.5,0)}$. We run the stochastic gradient method for $100$ iterations using $K = 6$ simulations and a step size of 0.1. We initialize the parameters with $S = I$ and $q = 0$. Over the course of learning, the cost decreased from $3.978$ to $0.971$. Figure 5 plots per-iteration cost on a held-out random seed while training. Figure 6 plots untuned and tuned sample paths on a single held-out instance. The resulting parameters are

### Tuning a supply chain policy to maximize profit

Supply chain management considers how to ship goods across a network of warehouses to maximize profit. In this example, we consider a single-good supply chain with $n$ nodes representing interconnected warehouses linked to suppliers and consumers by $m$ directed links over which goods can flow. There are $k$ links connecting suppliers to warehouses and $c$ links connecting warehouses to consumers. The remaining $m - k - c$ links are internode links.

We represent the amount of good held at each node as $h_{t} \in \text{R}_{+}^{n}$ (the set of nonnegative $n$-vectors). The prices at which we can buy the good from the suppliers are denoted $p_{t} \in \text{R}_{+}^{k}$, the (fixed) prices at which we can sell the goods to consumers are denoted $r \in \text{R}_{+}^{c}$, and the customer demand is denoted $d_{t} \in \text{R}_{+}^{c}$. Our inputs are $b_{t} \in \text{R}_{+}^{k}$, the quantity of the good that we buy from the suppliers, $s_{t} \in \text{R}_{+}^{c}$, the quantity that we sell to the consumers, and $z_{t} \in \text{R}_{+}^{m - k - c}$, the quantity that we ship across the internode links. The state and inputs are The system dynamics are where $A^{in} \in \text{R}^{n \times m}$ and $A^{out} \in \text{R}^{n \times m}$; $A_{ij}^{{in}{({out})}}$ is $1$ if link $j$ enters (exits) node $i$ and $0$ otherwise.

The input and state are constrained in several ways. Warehouses have maximum capacities given by $h_{\max} \in \text{R}_{+}^{n}$, i.e., $h_{t} \leq h_{\max}$ (where the inequalities are elementwise), and links have maximum capacities given by $u_{\max} \in \text{R}_{+}^{m}$, i.e., $u_{t} \leq u_{\max}$. In addition, the amount of goods shipped out of a node cannot be more than the amount on hand, or ${A^{out}u_{t}} \leq h_{t}$. Finally, we require that we sell no more than the demand, or $s_{t} \leq d_{t}$.

We model the unknown future supplier prices and demands as random disturbances $w_{t} = {(p_{t + 1},d_{t + 1})}$ with joint log-normal distribution, i.e., ${\log w_{t}} = {({\log p_{t + 1}},{\log d_{t + 1}})} \sim {\mathcal{N}{(\mu,\Sigma)}}$.

The goal of our supply chain is to maximize profit, which depends on several quantities. Our payment to the suppliers is $p_{t}^{T}b_{t}$, we obtain revenues $r^{T}s_{t}$ for selling the good to consumers, and we incur a shipment cost $\tau^{T}z_{t}$, where $\tau \in \text{R}_{+}^{m - k - c}$ is the cost of shipping a unit of good across the internode links. We also incur a cost for holding or storing $h_{t}$ in the warehouses; this is represented by a quadratic function ${\alpha^{T}h_{t}} + {\beta^{T}h_{t}^{2}}$, where ${\alpha,\beta} \in \text{R}_{+ +}^{n}$ and the square is elementwise. Our cost is our average negative profit, or Here, $I{(x_{t},u_{t})}$ enforces the constraints mentioned above; $I{(x_{t},u_{t})}$ is 0 if $x_{t}$ and $u_{t}$ lie in the set and $+ \infty$ otherwise.

### Policy

The policy seeks to maximize profit by computing $(b_{t},s_{t},z_{t})$ as where the parameters are $\theta = {(S,q)}$ with $S \in \text{R}^{n \times n}$ and $q \in \text{R}^{n}$. This COCP is an ADP policy and we can interpret the term ${- {\|{Sh^{+}}\|}_{2}^{2}} - {q^{T}h^{+}}$ as our approximate value function applied to the next state.

### Numerical example

Figure 7: Tuning a supply chain policy.

We consider a supply chain over horizon $T = 20$ with $n = 4$ nodes, $m = 8$ links, $k = 2$ supply links, and $c = 2$ consumer links. The initial value of the network storage is chosen uniformly between $0$ and $h_{\max}$, i.e., $h_{0} \sim {\mathcal{U}{(0,h_{\max})}}$. The log supplier prices and consumer demands have mean and covariance Therefore, the supplier prices have mean $(1.02,1.13)$ and the consumer demands have mean $(1.02,1.52)$. The consumer prices are $r = {{(1.4)}\mathbf{1}}$. We set the maximum nodes capacity to $h_{\max} = {{}\mathbf{1}}$ and links capacity to $u_{\max} = {{}\mathbf{1}}$. The storage cost parameters are $\alpha = \beta = {{(0.01)}\mathbf{1}}$. Node $1$ is connected to the supplier with lower average price and node $4$ to the consumer with higher demand.

We initialize the parameters of our policy to $S = I$ and $q = {- h_{\max}}$. In this way, the approximate value function is centered at $h_{\max}/2$ so that we try to keep the storage of each node at medium capacity.

We ran our method over $200$ iterations, with $K = 10$ using the stochastic gradient method with step size $0.05$. Figure 7 shows the per-iteration cost on a held-out random seed while training. Over the course of training the cost decreased by $22.35$ percent from $- 0.279$ to $- 0.341$. The resulting parameters are The diagonal of $S^{T}S$ shows that the learned policy especially penalizes storing goods in nodes connected to more expensive suppliers, e.g., node $2$, or to consumers with lower demand, e.g., node $3$.

Figure 8: Supply chain network. Left: untuned policy. Right: tuned policy. Colors indicate the normalized shipments between 0 and 1.

Figure 9: Left: untuned policy. Right: tuned policy. Supply chain storage ht for each node over time.

Figure 8 shows the supply chain structure and displays the average shipment, normalized between $0$ and $1$; figure 9 the simulated storage $h_{t}$ for the untuned and tuned policy on a held-out random seed.

## Extensions and variations

### Estimation

Our approach is not limited to tuning policies for control. As we alluded to before, our approach can also be used to learn convex optimization state estimators, for example Kalman filters or moving horizon estimators. The setup is exactly the same, in that we learn or tune parameters that appear in the state estimation procedure to maximize some performance metric. (A similar approach was adopted , where the authors fit parameters in a Kalman smoother to observed data.) Also, since COCPs are applied to the estimated state, we can in fact jointly tune parameters in the COCP along with the parameters in the state estimator.

### Prediction

In an MPC policy, one could tune parameters in the function that predicts the disturbances together with the controller parameters. As a specific example, we mention that the parameters in a Markowitz policy, such as the expected return, could be computed using a parametrized prediction function, and this function could be tuned jointly with the other parameters in the COCP.

### Nonconvex optimization control policies (NCOCPs)

An NCOCP is an optimization-based control policy that is evaluated by solving a *nonconvex* optimization problem. Parameters in NCOCPs can be tuned in the same way that we tune COCPs in this paper. Although the solution to a nonconvex optimization problem might be nonunique or hard to find, one can differentiate a local solution map to a smooth nonconvex optimization problem by implicitly differentiating the KKT conditions. This is done , where the authors define an MPC-based NCOCP.
