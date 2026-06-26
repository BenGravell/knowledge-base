<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Iteration for Multiplicative Noise Output Feedback Control

Topics include Policy iteration, Multiplicative noise, Output feedback, Linear quadratic control, Stochastic optimal control, POMDPs, Riccati equation, Dynamic output feedback.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends policy iteration to the partially observed multiplicative-noise linear quadratic setting, where the controller is a linear dynamic output-feedback policy rather than a static state-feedback gain. The main contribution is a coupled estimator-controller Riccati iteration that delivers results much more quickly/with less computation effort than the prior value-iteration approach, in some cases. This points toward scalable policy optimization methods for more general POMDPs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a policy iteration algorithm for solving the multiplicative noise linear quadratic output feedback design problem. The algorithm solves a set of coupled Riccati equations for estimation and control arising from a partially observable Markov decision process (POMDP) under a class of linear dynamic control policies. We show in numerical experiments far faster convergence than a value iteration algorithm, formerly the only known algorithm for solving this class of problem. The results suggest promising future research directions for policy optimization algorithms in more general POMDPs, including the potential to develop novel approximate data-driven approaches when model parameters are not available.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multiplicative noise models can be used to represent myriad phenomena where noise or uncertainty depends on the system state, input, or output. These models have a long history in control theory [wonham1967optimal] and have been utilized in the context of networked control systems [sinopoli2004kalman] robots with distance-dependent sensors such as lidar and optical cameras [dutoit2011robot], turbulent fluid flow [lumley2007stochastic], climate dynamics [majda1999models], biological sensorimotor systems [todorov2005stochastic], neuronal brain networks [breakspear2017dynamic], portfolio optimization and financial markets [primbs2007portfolio] power grids with stochastic inertia [guo2019a], and aerospace systems [gustafson1975design].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, these models have also been used to represent parametric uncertainty and promote robustness in data-driven control and machine learning via, e.g., bootstrapping [gravell2020pmlr], domain randomization [tobin2017domain], and dropout [srivastava2014dropout].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing optimal output feedback controllers for multiplicative noise dynamical systems is particularly challenging because, in marked contrast to classical LQG/$\mathcal{H}_2$ and $\mathcal{H}_\infty$ control design, there is no separation between estimation and control. In particular, a canonical linear quadratic problem features a set of Riccati equations involving cost and covariance matrices for the state and state estimate that are coupled by the multiplicative noise. These equations cannot be solved by direct methods for decoupled Riccati equations [bittanti2012riccati]. The only known solution method is an iterative algorithm akin to value iteration, described in [dekoning1992].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy iteration has been studied extensively in general settings for dynamic programming and reinforcement learning and is closely related to the Newton method [puterman1979convergence,bertsekas2021lessons]. Policy iteration and the Newton method have also been studied extensively for solving the single generalized Riccati equation arising in the linear quadratic state-feedback setting in [kleinman1969,damm2004rational]. However, there is far less known about policy iteration and the Newton method for output feedback control or partially observable Markov decision processes (POMDPs). Various approximate policy iteration schemes have been studied to a limited extent in deterministic and additive noise output feedback linear quadratic problems in [lewis2011,rizvi2018output,yaghmaie2022] and for tabular and nonlinear POMDPs in [hansen1998pomdp, gao2016output]. None of these address the coupled Riccati equations arising in the output-feedback multiplicative noise setting.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is to propose a policy iteration algorithm for multiplicative noise output feedback control design, which solves a set of coupled Riccati equations for estimation and control. We show in numerical experiments far faster convergence than a value iteration algorithm, the only known algorithm for solving this class of problem. We provide an open source implementation of our algorithm to facilitate further research and reproducibility. The results suggest promising future research directions for policy iteration and data-driven output feedback control algorithms for the multiplicative noise problem and other more general POMDPs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. [sec:problem\_formulation] formulates an optimal output feedback control problem for systems with multiplicative noise. [sec:optimal\_control] describes the coupled Riccati equations that determine an optimal policy in a form that motivates policy iteration. Our policy iteration algorithm is proposed in [sec:policy\_iteration]. [sec:numerical\_experiments] presents the numerical experiments, and [sec:conclusion]concludes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Denote the set of real-valued $n \times m$ matrices as $\mathbb{R}^{n \times m}$ and the set of $n \times n$ symmetric positive semidefinite matrices as $\mathbb{S}^{n}_{+}$. Denote the $n \times n$ all-zeros and identity matrices as $0_n$ and $I_n$, respectively. For real-valued matrices $A$ and $B$, denote the transpose as $A^\intercal$, the trace as $\Tr(A)$, and the Frobenius inner product as $\langle A, B \rangle \coloneqq \Tr(A^\top B)$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation: Output Feedback Control with Multiplicative Noise", "weight": 1.0} -->

We consider output-feedback control of the discrete-time stochastic linear dynamical system where $x_t \in \mathbb{R}^n$ is the system state, $u_t \in \mathbb{R}^m$ is the control input, and $y_t \in \mathbb{R}^p$ is the observed output.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation: Output Feedback Control with Multiplicative Noise", "weight": 1.0} -->

The process and observation noises $w_t$ and $v_t$, respectively, are independent across time, have mean zero, and have covariance \mathbb{E} \left[\begin{bmatrix} w_t \\ v_t \end{bmatrix} \begin{bmatrix} w_t \\ v_t \end{bmatrix}^\intercal \right] = The initial state $x_0$ is a random vector drawn from a distribution with mean zero and covariance $X_0$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation: Output Feedback Control with Multiplicative Noise", "weight": 1.0} -->

We consider convex quadratic stage cost in the states and inputs \begin{bmatrix} x_t \\ u_t \end{bmatrix}^\intercal \begin{bmatrix} x_t \\ u_t \end{bmatrix}, \quad This yields the infinite-horizon average-cost multiplicative-noise linear quadratic output feedback control problem \min_{\pi} J(\pi) \coloneqq & \lim_{T \to \infty} \frac{1}{T} \mathbb{E} \left[\sum_{t=0}^{T-1} \ell(x_t, u_t) \right] \\& \text{subject to } eq:true_system, where a control policy $u_t = \pi(y_{0:t}, u_{0:t-1})$ dependent on the input-output history $y_{0:t}:= [y_0,y_1,...,y_t],

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear Dynamic Control Policies", "weight": 1.0} -->

A linear dynamic controller is a widely used class of policy which combines a linear state estimator with a linear state estimate feedback in the form The initial state estimate is chosen as $\hat{x}_0 = 0$, since the initial state has mean zero. Such a controller is fully specified by the triple $(F, K, L)$ where $K \in \mathbb{R}^{m \times n}$ is the control gain, $L \in \mathbb{R}^{n \times p}$ is the state estimator gain, and $F \in \mathbb{R}^{n \times n}$ is the closed-loop model matrix. We will consider the problem [eq:mlqc\_original] with optimization over this special class of linear dynamic controllers. In the classical LQG setting with additive noise-only (where $A_t = A$, $B_t = B$, $C_t = C$), the optimal policy is indeed a linear dynamic controller of the class [eq:linear\_dynamic\_compensator].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear Dynamic Control Policies", "weight": 1.0} -->

However, in the multiplicative noise setting this class may not be optimal.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear Dynamic Control Policies", "weight": 1.0} -->

Due to the multiplicative noise, the state distribution is non-Gaussian even when all primitive distributions are Gaussian, so the Kalman filter is not necessarily the optimal state estimator. To our knowledge, it has not been demonstrated whether there exist conditions under which a nonlinear controller outperforms the optimal linear dynamic controller for the problem eq:mlqc\_original, but this is beyond our scope here.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear Dynamic Control Policies", "weight": 1.0} -->

Nevertheless, the work of [dekoning1992] shows that restricting attention to [eq:linear\_dynamic\_compensator] admits useful stability characterizations and optimal control synthesis equations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

Under the closed-loop dynamics [eq:closed\_loop\_dynamics\_aug], define the value and covariance matrices at time $t$ recursively by \mathbb{E} \left[{\Phi^\prime_t}^\intercal P^\prime_{t} {\Phi^\prime_t} \mathbb{E} \left[{\Phi^\prime_t} S^\prime_{t} {\Phi^\prime_t}^\intercal with the initial value matrix $P^\prime_0 = Q^\prime$ and the initial second moment matrix $S^\prime_0 = \begin{bmatrix} X_0 & 0 \\ 0 & 0 \end{bmatrix}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

In particular, $S^\prime_{t}$ is the second moment of the augmented state \end{bmatrix}^\intercal while $P^\prime_{t}$ is related to the costs $\ell(x_t, u_t)$ through the relation \mathbb{E} \left[\sum_{t=0}^{T-1} \ell(x_t, u_t) \right] \langle P^\prime_T, S_0^\prime \rangle + \sum_{t=0}^T \langle P^\prime_t, W^\prime \rangle.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

We re-state some definitions from [dekoning1992] that characterize asymptotic behavior of [eq:closed\_loop\_dynamics\_aug].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

System [eq:closed\_loop\_dynamics\_aug] is mean-square compensatable if there exists a controller [eq:linear\_dynamic\_compensator] which renders the augmented system [eq:closed\_loop\_dynamics\_aug] ms-stable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

Assumption. System [eq:closed\_loop\_dynamics\_aug] is mean-square compensatable.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

These operators govern the second moment dynamics [eq:second\_moment\_dynamics] as \Psi(P^\prime_{t}) + Q^\prime, \\Accordingly, the ms-stability of the closed-loop system is characterized by the spectrum of the linear operator $\Psi(\cdot)$, or equivalently of $\Gamma(\cdot)$, since they share the same spectra. Namely, if the spectral radius $\rho(\Psi(\cdot)) < 1$ then the closed-loop system is ms-stable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

\sigma^2_{C,i} {C^\prime_{\Delta, i}}^\intercal \otimes {C^\prime_{\Delta, i}}^\intercal, \nonumber \mathbb{E}[\Phi^\prime_t] \end{bmatrix}, \quad A^\prime_{\Delta, i} \coloneqq \end{bmatrix}, \quad \\B^\prime_{\Delta, i} \coloneqq \end{bmatrix}, \quad C^\prime_{\Delta, i} \coloneqq Note that a dual matrix $\Gamma$ can be computed by dropping all transpose marks (${}^\intercal$) in [eq:second\_moment\_matrix\_builder].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

With such ms-stability, the steady-state value matrix $P^\prime$ and the steady-state second moment $S^\prime$ are found by solving the discrete-time generalized Lyapunov equations P^\prime &= \Psi(P^\prime) + Q^\prime, \\S^\prime &= \Gamma(S^\prime) + W^\prime.% P^\prime &= \mathbb{E} \left[{\Phi^\prime}^\intercal_t P^\prime \Phi^\prime_t \right] + Q^\prime, \\% S^\prime &= \mathbb{E} \left[\Phi^\prime_t S^\prime {\Phi^\prime}^\intercal_t \right] + W^\prime.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

With a slight abuse of notation, the performance criterion [eq:performance] can be expressed and computed as J(F, K, L) = \langle P^\prime, W^\prime \rangle = \langle S^\prime, Q^\prime \rangle. which is finite only when [eq:closed\_loop\_dynamics\_aug] is mean-square compensatable. Solving the generalized Lyapunov equations [eq:dlyap\_aug] to evaluate the performance [eq:performance\_linear] of a given policy will form a basic component of our policy iteration algorithm.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

Also in preparation for the policy iteration algorithm, given $P^\prime, S^\prime$, define P &= \begin{bmatrix} I_n & I_n \end{bmatrix} P^\prime \begin{bmatrix} I_n & I_n \end{bmatrix}^\intercal, \\\hat{P} &= \begin{bmatrix} 0_n & I_n \end{bmatrix} P^\prime \begin{bmatrix} 0_n & I_n \end{bmatrix}^\intercal, \\S &= \begin{bmatrix} I_n & -I_n \end{bmatrix} S \begin{bmatrix} I_n & -I_n \end{bmatrix}, \\\hat{S} &= \begin{bmatrix} 0_n & I_n \end{bmatrix} S^\prime \begin{bmatrix} 0_n & I_n \end{bmatrix}^\intercal.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Closed-Loop Dynamics and Performance Criterion", "weight": 1.0} -->

In particular, the second moment of state estimation error and state estimate are, respectively, S = \lim_{t \to \infty} \mathbb{E}[(x_t - \hat{x}_t)(x_t - \hat{x}_t)^\intercal], \quad \hat{S} = \lim_{t \to \infty} \mathbb{E}[\hat{x}_t \hat{x}_t^\intercal], and $P$, $\hat{P}$have analogous interpretations in terms of the cost.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimal Linear Feedback Control Design", "weight": 1.0} -->

The optimal linear dynamic controller for the multiplicative noise problem [eq:mlqc\_original] can be exactly computed by solving a set of coupled Riccati equations for estimation and control [dekoning1992]. However, in the multiplicative noise setting there is no separation between estimation and control, so the optimal controller gains $(F, K, L)$ must be jointly computed. Here we derive the equations in a form that facilitates the development of the policy iteration algorithm developed in the following section.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimal Linear Feedback Control Design", "weight": 1.0} -->

Note that $\mathcal{G}$ and $\mathcal{H}$ have a block $2 \times 2$ structure whose blocks are referred to with the same subscripts as in $Q$ and $W$ as appropriate. These expressions can be derived from the matrix minimum principle [athans1967] as in [dekoning1992]. Notice that the gains $\mathcal{K}(X)$ and $\mathcal{L}(X)$ depend only on the $\mathcal{G}_{ux}$, $\mathcal{G}_{uu}$, $\mathcal{H}_{xy}$, $\mathcal{H}_{yy}$ blocks of $\mathcal{G}$ and $\mathcal{H}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimal Linear Feedback Control Design", "weight": 1.0} -->

The optimal controller is \big(A + B \mathcal{K}(X^*) - \mathcal{L}(X^*) C, \mathcal{K}(X^*), \mathcal{L}(X^*) \big) where $X^*$ solves [eq:coupled\_riccati] [dekoning1992]. With this controller, the cost and second moment matrices satisfy and thus the optimal controller achieves the optimal cost \begin{bmatrix} I \\ K \end{bmatrix}^\intercal \begin{bmatrix} I \\ K \end{bmatrix}, \begin{bmatrix} I \\ -L \end{bmatrix} \begin{bmatrix} I \\ -L \end{bmatrix}^\intercal, \hat{P} \right\rangle.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimal Linear Feedback Control Design", "weight": 1.0} -->

When the multiplicative noise terms are zero, the coupled Riccati equations reduce to the familiar two decoupled standard algebraic Riccati equations for optimal linear quadratic control and state estimation, which can be solved via several well-known methods such as the dynamic programming techniques of policy iteration and value iteration [bertsekas2012dynamic], convex semidefinite programming [boyd1994linear], and specialized direct linear algebraic methods [bittanti2012riccati]. In contrast, the only known algorithm for solving the coupled Riccati equations [eq:coupled\_riccati] is a value iteration-type algorithm, described in [dekoning1992]. This turns the Riccati equation [eq:gen\_riccati\_tiny] into a recursive update according to Convergence of [eq:value\_iteration] was proved in [dekoning1992]using a homotopic continuation argument that continuously deforms a multiplicative noise-free version of the problem (for which convergence of the value iteration algorithm is well-known) to the original multiplicative noise-driven problem.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy Iteration for Multiplicative Noise Output Feedback Control", "weight": 1.0} -->

In this section, we describe a novel policy iteration algorithm to solve the coupled Riccati equations [eq:coupled\_riccati]. Policy iteration is a well-known method for computing optimal policies in the full state-feedback setting, originating with [kleinman1968iterative, hewer1971iterative]for linear quadratic problems. It consists of two steps: policy evaluation, where the value of the current policy is computed from the dynamics and cost; and policy improvement, where the current policy is improved based on the policy evaluation. However, policy iteration is far less developed in the context of output feedback control problems or POMDPs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Iteration for Multiplicative Noise Output Feedback Control", "weight": 1.0} -->

The form of the coupled Riccati equations in [eq:coupled\_riccati] suggests a policy iteration algorithm analogous to the full state-feedback setting. The operators $\mathcal{G}(X)$ and $\mathcal{H}(X)$ play a role analogous to the state-action value function (also called the Q-function) in reinforcement learning. In particular, for a given cost-covariance matrix variable $X$, the gain operators [eq:coupled\_riccati1\_gains] can be viewed as an update to the control and estimator gains that improves the corresponding value. Combining this with a policy evaluation step from solving the generalized Lyapunov equations [eq:dlyap\_aug] leads to a policy iteration algorithm for the multiplicative noise output feedback control problem detailed in Algorithm [algorithm:policy\_iteration\_exact].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Iteration for Multiplicative Noise Output Feedback Control", "weight": 1.0} -->

Note that the initial policy must be ms-stabilizing so that solutions to [eq:dlyap\_aug] exist; this is a standard assumption in policy iteration [kleinman1968iterative, hewer1971iterative] and policy optimization algorithms [gravell2021tac].

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Iteration for Multiplicative Noise Output Feedback Control", "weight": 1.0} -->

Policy iteration for optimal dynamic output feedback of linear systems with multiplicative noise ms-stabilizing policy $(A + B K^{0} - L^{0} C, K^{0}, L^{0})$, convergence threshold $\epsilon > 0$. Initialize $X^0 \! = \! $, $X^1 \! = \! (\infty, \infty, \infty, \infty)$, $k \! = \! 0$. Compute the value $X^k =(P^k, \hat{P}^k, S^k, \hat{S}^k)$ of the current policy $(A + B K^{k} - L^{k} C, K^{k}, L^{k})$ by finding the solutions ${P^\prime}^k$, ${S^\prime}^k$ to the Lyapunov equations [eq:dlyap\_aug] and using the relations [eq:suboptimal\_value\_matrix].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy Iteration for Multiplicative Noise Output Feedback Control", "weight": 1.0} -->

Update the policy according to Nearly optimal policy $(A + B K^{k} - L^{k} C, K^{k}, L^{k})$

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The algorithms were implemented in Python and executed on a desktop PC with a quad-core Intel i7 6700K 4.0GHz CPU and 16GB RAM; no GPU computing was utilized. Code supporting [sec:numerical\_experiments] is available in the GitHub repository

<!-- chunk {"id": "body-0039", "role": "body", "section": "Pendulum system", "weight": 1.0} -->

As a first example, we examined a particular system representing a forward Euler discretization of the continuous-time dynamics of a pendulum with torque actuation and control-dependent noise. The first and second states represent the angular position and velocity, respectively. The system dimensions were $n = 2, m = 1, p = 1$, $b = 1$, and $a = c = 0$, indicating $A_t$ and $C_t$ were unaffected by multiplicative noise. The problem data were \end{bmatrix}, \quad \end{bmatrix}, \quad \end{bmatrix}, \quad The penalty and additive noise covariance matrices were chosen as $Q = I$ and $W = \text{diag}(0, 0.01, 0.001)$ respectively. The multiplicative noise value $\sigma_{B, 1}$ was varied by scaling by a noise level factor $\eta \in $. Note that the system was open-loop ms-stable; therefore we selected as our initial policy the open-loop policy $(A, 0, 0)$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Pendulum system", "weight": 1.0} -->

The algorithms were terminated once the convergence criterion $\| X^{k} - X^{k-1} \| \leq 10^{-12}$was achieved. [fig:pendulum\_error] compares the policy iteration Algorithm [algorithm:policy\_iteration\_exact] with the value iteration method of [dekoning1992]. The metric used for comparison was e^k &= \max \{ \delta(P^k), \delta(\hat{P}^k), \delta(S^k), \delta(\hat{S}^k) \}, \\\text{where} \quad \delta(M^k) &= \| M^k - M^* \| / \| M^0 - M^* \|, which measures the error of the current solution relative to that of the initial solution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Pendulum system", "weight": 1.0} -->

Relative error vs elapsed wall clock time.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Pendulum system", "weight": 1.0} -->

Performance of value iteration and policy iteration for the pendulum system with various noise levels $\eta$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Pendulum system", "weight": 1.0} -->

- The value iteration algorithm converges much more slowly compared to policy iteration, both in the multiplicative noise-free setting ($\eta = 0$) as well as in the multiplicative noise setting ($\eta > 0$). - The presence of multiplicative noise causes value iteration to converge significantly more slowly, while the proposed policy iteration suffers a much less dramatic slowdown as the noise level $\eta$ increases.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Pendulum system", "weight": 1.0} -->

These observations apply both in terms of iteration count and wall clock time.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Random systems", "weight": 1.0} -->

Next, we report results for systems with randomly generated parameters. The dimensions of each problem were chosen as $n = 2, m = 1, p = 1$ and $a = b = c = 1$. The entries of $A$, $B$ $C$, $A_{\Delta, 1}$, $B_{\Delta, 1}$, $C_{\Delta, 1}$ were randomly drawn from a standard normal distribution. $A$ was scaled to have $\rho(A)$ drawn uniformly random between 0 and 1. The variances $\sigma_{A, 1}^2$, $\sigma_{B, 1}^2$, $\sigma_{C, 1}^2$ were drawn uniform randomly between 0 and 1, then scaled such that the open-loop system with $(A, 0, 0)$ had $\sqrt{\rho(\Psi)} = 1$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Random systems", "weight": 1.0} -->

Finally, the variances $\sigma_{A, 1}^2$, $\sigma_{B, 1}^2$, $\sigma_{C, 1}^2$ were scaled by a factor $\eta$ drawn uniform randomly between 0 and 1. Hence, the systems were always open-loop ms-stable by construction; therefore we selected as our initial policy the open-loop policy $(A, 0, 0)$. The penalty and additive noise covariance matrices were chosen as $Q = I$ and $W = 0.01 I$respectively.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Random systems", "weight": 1.0} -->

The results are plotted in Figure [fig:many\_systems\_vi\_pi\_both\_scatter], where each solved problem instance is represented by a scatter point. It is evident that the proposed policy iteration algorithm converges in far fewer total iterations on almost every problem instance. Due to greater per-iteration computation costs, the benefit in time elapsed is not as large for the policy iteration algorithm overall. However, per-iteration costs can be significantly reduced by using specialized solvers for the generalized Lyapunov equations based on e.g. alternating-direction implicit preconditioning and Krylov subspaces [damm2008direct] and other schemes that take advantage of sparsity in the linear matrix equation. Nevertheless, the greatest benefit was achieved when the multiplicative noise was high relative to the maximum uncertainty that allows mean-square compensatability, which can be seen in the trend of Figure [fig:many\_systems\_vi\_pi\_both\_scatter], mirroring the results observed for the pendulum system in [sec:numerical\_experiments\_pendulum].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Random systems", "weight": 1.0} -->

[sec:numerical\_experiments\_pendulum] and [sec:numerical\_experiments\_random] together suggest that the least computationally costly method of solving [eq:mlqc\_original] may be problem-instance dependent; a reliable indicator of when our policy iteration Algorithm [algorithm:policy\_iteration\_exact] will outperform the value iteration [eq:value\_iteration]remains to be discovered.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Random systems", "weight": 1.0} -->

Ratio of total iterations and time elapsed using value iteration to that using policy iteration.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We proposed a policy iteration algorithm for multiplicative noise optimal output feedback control design. Empirically it converges far faster than a value iteration algorithm, the only other known method for this problem.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Given the intimate connections between policy iteration and the Newton method, we believe there is a connection between our proposed algorithm and the Newton method (or some variation thereof) applied to the coupled Riccati equations Interpreting our algorithm through a Newton lens would allow us to leverage rich theory surrounding the Newton method to obtain theoretical convergence results, in particular a quadratic rate of convergence as in [kleinman1968iterative, hewer1971iterative, damm2001]. Furthermore, establishing a rate of convergence for the value iteration algorithm [eq:value\_iteration], which we conjecture is a linear rate, is, to our knowledge, also an open problem whose solution is required to establish theoretical relative performance claims. We leave this for future work.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Finally, our policy iteration algorithm opens the door to investigate novel approximate policy iteration algorithms that use input-output and state estimate data (instead of knowledge of system parameters) to approximately execute the policy evaluation and policy improvement steps. Many variations of approximate policy iteration have been explored in the full-state feedback setting; see e.g. [bradtke1994adaptive, krauth2019finite, gravell2021approximate]. But there are many open problems, especially for approximate policy iteration in POMDPs. For example, it may be possible to use input-output and state estimate data generated from a given policy to form a least-squares estimate of the cost and covariance operators, and then perform an approximate policy improvement step based on this estimate. We will also explore this and other variations in future work.
