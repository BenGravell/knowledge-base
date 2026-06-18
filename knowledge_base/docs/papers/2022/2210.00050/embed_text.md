## Introduction

Intelligent and adaptive systems of the "smart world" that work under operational constraints seek to solve some instance of a constrained optimal control problem for optimizing their performance. Such constrained optimal control problems can now be increasingly solved efficiently using several numerical optimization techniques. For instance, robot path planning in uncertain environments has gained the attention of researchers worldwide as robots are being increasingly deployed to solve many real-world problems. Apart from realistic constraints, reliability of operation of these systems is often thwarted by the ineffective handling of system uncertainties, which can be either deterministic or stochastic.

Control of stochastic systems can be best formulated as a problem of controlling the distribution of trajectories over time subject to constraints. Recently, the finite horizon covariance steering (CS) problem, namely, the problem of steering an initial distribution to a final distribution at a specific final time step subject to linear time varying dynamics has been explored. Specifically, the control problem in the CS problem setting involves steering the mean and the covariance to the desired terminal values. When the decision-making process relies blindly on the functional form of the process that models the stochastic uncertainty, it is known to result in potentially severe miscalculation of risk. For instance, Gaussianity assumptions made in the name of tractability in several modeling regimes are actually rarely justifiable, as the true distribution that governs the uncertain data might be non-Gaussian. Such shortcomings can be mitigated with risk-based stochastic optimization where the risk of wrong decisions can be appropriately handled to result in risk-averse decision making. One such tool is the Distributionally Robust Optimization (DRO) advocated in which enables modelers to explicitly incorporate ambiguity in probability distributions into the optimization problem.

Control of stochastic systems often involves optimizing the system's objective subject to chance constraints, where one assumes that the system uncertainties follow a known distribution and enforces that the system constraints hold with high probability as a function of the decision variables. The number of constraint violations, called the total risk budget, is usually a user-defined a priori specification and is a natural metric to assess risk. Hence, one may consider the problem of finding a risk allocation procedure that will allocate the probability of violating each individual chance constraint at each time step. Given a number of chance constraints across a finite horizon, the total risk budget has to be allocated for all chance constraints across all time steps. It is a common practice to consider a uniform risk allocation, i.e., allocate the same risk for all constraints and across all time steps. However, risk allocation can be optimized as in to reduce the conservatism resulting from a uniform risk allocation. If the probability distribution of the system uncertainties are known exactly, then non-uniform risk allocation can be performed effectively. However, risk allocation optimization with arbitrary distribution of the system uncertainties has not yet been explored till now. This article addresses this shortcoming.

*Contributions:* Since authors in solved the CS problem for the Gaussian case, this article extends it with arbitrary distributions using the theory of distributional robustness (DR). To the best of our knowledge, this article is the first one to extend the CS problem using distributionally robust optimization techniques for both polytopic and convex conic state constraint sets. Our main contributions in this article are as follows:

We extend the covariance steering problem tailored between Gaussian distributions to arbitrary distributions modeled using moment based ambiguity sets.

We enforce distributionally robust risk constraints for both polytopic and convex cone state constraint satisfaction, while solving the covariance steering problem, and obtain the optimal risk allocation through a distributionally robust iterative risk allocation (DR-IRA) algorithm.

We demonstrate our approach using simulation examples and show the effectiveness of the proposed generalization for covariance steering problems between arbitrary distributions in moment-based ambiguity sets.

Following a short summary of notation and preliminaries, the rest of the paper is organized as follows: The main problem statement of distributionally robust covariance steering problem with iterative risk allocation is presented in Section II. Then, the proposed Distributionally Robust Iterative Risk Allocation (DR-IRA) algorithm is discussed in Section III. Subsequently, the proposed approach is demonstrated using simulation results in Section IV. Finally, the paper is concluded in Section V along with directions for future research.

## Notation and Preliminaries

The set of real numbers and natural numbers are denoted by $\mathbb{R}$ and $\mathbb{N}$, respectively. The subset of natural numbers between and including $a$ and $b$ with $a < b$ is denoted by $\lbrack a,b\rbrack$. An identity matrix in dimension $n$ is denoted by $I_{n}$. For a non-zero vector $x \in {\mathbb{R}}^{n}$ and a matrix $P \in {\mathbb{S}}_{+ +}^{n}$ or $P \succ 0$, we denote $\left\| x \right\|_{P}^{2} = {x^{\top}Px}$, where ${\mathbb{S}}_{+ +}^{n}$ is the set of all positive definite matrices. We say $P \succ Q$ or $P \succeq Q$ if ${P - Q} \succ 0$ or ${P - Q} \succeq 0$ respectively. We denote by $\mathcal{B}{({\mathbb{R}}^{d})}$ and $\mathcal{P}{({\mathbb{R}}^{d})}$ the Borel $\sigma -$algebra on ${\mathbb{R}}^{d}$ and the space of probability measures on $({\mathbb{R}}^{d},{\mathcal{B}{({\mathbb{R}}^{d})}})$ respectively. A probability distribution with mean $\mu$ and covariance $\Sigma$ is denoted by ${\mathbb{P}}{(\mu,\Sigma)}$ and, specifically $\mathcal{N}_{d}{(\mu,\Sigma)}$, if the distribution is normal in ${\mathbb{R}}^{d}$. The cumulative distribution function (cdf) of the normally distributed random variable is denoted by $\mathbf{\Phi}$. A uniform distribution over a compact set $A$ is denoted by $\mathcal{U}{(A)}$. Given a constant $q \in {\mathbb{R}}_{\geq 1}$, the set of probability measures in $\mathcal{P}{({\mathbb{R}}^{d})}$ with finite $q -$th moment is denoted by ${\mathcal{P}_{q}{({\mathbb{R}}^{d})}}:=\left\{ {\mu \in {\mathcal{P}{({\mathbb{R}}^{d})}}}\mid{{\int_{{\mathbb{R}}^{d}}{\left\| x \right\|^{q}{d\mu}}} < \infty} \right\}$.

## Problem Formulation

Consider a linear, stochastic, discrete and time-varying system as follows

where $x_{k} \in {\mathbb{R}}^{n}$ and $u_{k} \in {\mathbb{R}}^{m}$ is the system state and input at time $k$, respectively and $N$ denotes the total time horizon. Further, $A_{k} \in {\mathbb{R}}^{n \times n}$ is the dynamics matrix, $B_{k} \in {\mathbb{R}}^{n \times m}$ is the input matrix and $D_{k} \in {\mathbb{R}}^{n \times r}$ is the disturbance matrix. The process noise $w_{k} \in {\mathbb{R}}^{r}$ is a zero-mean random vector that is independent and identically distributed across time. We assume that the system state and the process noise is independent of each other at all time steps, meaning that ${{\mathbb{E}}{\lbrack{x_{k}w_{j}}\rbrack}} = 0$, for $0 \leq k \leq j \leq N$. The distribution ${\mathbb{P}}_{w}$ of $w_{k}$ is unknown but is assumed to belong to a moment-based ambiguity set of distributions, $\mathcal{P}^{w}$ given by

Note that there are infinitely many distributions present in the considered set $\mathcal{P}^{w}$. For instance, both multivariate Gaussian and multivariate Laplacian distributions with zero mean and covariance $\Sigma_{w}$ belong to $\mathcal{P}^{w}$ with the latter having heavier tail than the former. We assume that the system is controllable under zero process noise meaning that given any ${x_{0},x_{f}} \in {\mathbb{R}}^{n}$, there exists a sequence of control inputs ${\{ u_{k}\}}_{k = 0}^{N - 1}$ that steers the system state from $x_{0}$ to $x_{f}$. Since the considered system is stochastic, the initial condition $x_{0}$ is subject to a similar uncertainty model as the noise, with the distribution belonging to a moment-based ambiguity set, ${\mathbb{P}}_{x_{0}} \in \mathcal{P}^{x_{0}}$, where

Provided that the control law $u_{k}$ is selected as an affine function of state $x_{k}$ at any time $k$, similar moment-based ambiguity sets $\mathcal{P}^{x_{k}}$ can be written for the distribution of states at any time $k \in {\lbrack 1,N\rbrack}$ using the propagated mean and covariance at time $k$. Note that $\mathcal{P}^{x_{k}}$ would *not* be empty at all time steps $k \in {\lbrack 1,N\rbrack}$ as a Gaussian distribution would be a guaranteed member in that set. This is because, Gaussianity is preserved under linear transformations defined by the dynamics. However, the initial state $x_{0}$ need *not* be Gaussian, and thereby it would be *inappropriate* to assume that the final state $x_{N}$ would also be Gaussian. Hence, the terminal state $x_{N}$ is subject to a similar uncertainty model as the $x_{0}$, with its distribution ${\mathbb{P}}_{x_{N}}$ belonging to a moment-based ambiguity set $\mathcal{P}^{x_{N}}$, given by

The objective is to steer the trajectories of from $x_{0} \sim {\mathbb{P}}_{x_{0}} \in \mathcal{P}^{x_{0}}$ to $x_{N} \sim {\mathbb{P}}_{x_{N}} \in \mathcal{P}^{x_{N}}$ in $N$ time steps. This covariance steering objective is usually achieved by minimizing a cost function under specified convex state and input constraints. We define the concatenated variables required for the problem formulation as follows

Using the concatenated variables, can be written as

where the matrices $\mathcal{A},\mathcal{B}$ and $\mathcal{D}$ are of appropriate dimensions containing the time varying system matrices $A_{k},B_{k}$, and $D_{k}$ respectively. See for more details on this transformation. It is evident that ${\mathbb{P}}_{\mathbf{X}}$ is not known exactly but a similar ambiguity set like $\mathcal{P}^{x_{0}}$ can be constructed for ${\mathbb{P}}_{\mathbf{X}}$^11^1Note that ${\mathbb{P}}_{\mathbf{X}}$ is the joint distribution formed with ${{{\mathbb{P}}_{x_{k}},k} = 0},{\ldots,N}$ being its marginal distributions.. That is,

The cost function to optimize is given as follows

where $\overline{Q} = {{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(Q_{0},Q_{1},\ldots,Q_{N - 1})}}$ is the state penalty matrix and $\overline{R} = {{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(R_{0},R_{1},\ldots,R_{N - 1})}}$ is the control penalty matrix with each ${Q_{k} \succeq 0},{R_{k} \succ 0}$ for all $k \in {\lbrack 0,{N - 1}\rbrack}$. Over the whole time horizon, we want the states to respect certain state constraints. Since the state is stochastic, constraint violation can be imposed through a chance constraint formulation. Specifically, a distributionally robust risk constraint formulation is preferred in this setting as the system state need not be Gaussian at any time step $k$. Hence, we impose the following joint distributionally robust risk constraint that limits the worst case probability defined by ${\mathbb{P}}_{\mathbf{X}}$ of state constraint violation to be less than a pre-specified threshold,

where, $\Delta \in {(0,0.5\rbrack}$ denotes the pre-specified total risk budget and $\mathcal{X}_{p}$ denotes the state constraint set to be satisfied. It is assumed to be a convex polytope and so can be represented using intersection of finite number of half-spaces as

where $a_{i} \in {\mathbb{R}}^{n}$ and $b_{i} \in {\mathbb{R}}$. Later in this article, we will extend the case for $\mathcal{X}_{p}$ being a more general convex cone constraint.

### Problem 1

Given the system and a total risk budget $\Delta$, we seek an optimal feedback control policy $\Pi^{\star} = {\lbrack\pi_{0}^{\star},\ldots,\pi_{N - 1}^{\star}\rbrack}$ such that the control inputs $u_{k}^{\star} = {\pi_{k}^{\star}{(x_{k})}}$, $k \in {\lbrack 0,{N - 1}\rbrack}$ steers the system from the ${\mathbb{P}}_{x_{0}}$ belonging to to the ${\mathbb{P}}_{x_{N}}$ belonging to while minimizing the finite-horizon cost function and by respecting the distributionally robust joint risk constraint given in.

## Covariance Steering with Distributionally Robust Risk Allocation

In this section, we describe how to convert the joint distributionally robust risk constraint into individual distributionally robust risk constraints and use this result to steer both the mean and covariance of the initial state to the desired final mean and covariance.

### III-A Propagation of Mean and Covariance

We adopt the following control policy from as follows,

Here $\mathbf{V} = \begin{bmatrix}
v_{0}^{\top} & v_{1}^{\top} & \ldots & v_{N - 1}^{\top}
\end{bmatrix}^{\top} \in {\mathbb{R}}^{Nm}$ and $v_{k} \in {\mathbb{R}}^{m}$ for all $k = {\lbrack 0,{N - 1}\rbrack}$. The concatenated gain matrix $\mathbf{K} \in {\mathbb{R}}^{{{Nm} \times {({N + 1})}}n}$ contains the individual gain matrices $K_{k} \in {\mathbb{R}}^{m \times n}$. The mean and covariance of $\mathbf{Y}$ are given by

where $\Sigma_{\mathbf{W}} = {{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(\Sigma_{w},\ldots,\Sigma_{w})}} \in {\mathbb{R}}^{{{Nr} \times N}r}$. Substituting and into, we can infer that

Similarly, substituting and into, the dynamics of the state mean $\overline{\mathbf{X}}:={{\mathbb{E}}{\lbrack\mathbf{X}\rbrack}}$, and the state covariance $\Sigma_{\mathbf{X}} = {{\mathbb{E}}\left\lbrack {{({\mathbf{X} - \overline{\mathbf{X}}})}{({\mathbf{X} - \overline{\mathbf{X}}})}^{\top}} \right\rbrack}$ can be written as

Note that the initial and the terminal state moments can be expressed as follows

It is evident from and that the component $\mathbf{V}$ of the control law steers the mean of the system from $\mu_{0}$ to $\mu_{f}$ and the component $\mathbf{K}$ of the control law steers the covariance from $\Sigma_{0}$ to $\Sigma_{f}$. In order to make the problem convex, we relax the terminal covariance constraint in as an inequality constraint $\Sigma_{f} \succeq {E_{N}\Sigma_{\mathbf{X}}E_{N}}$ and subsequently reformulate it as a linear matrix inequality (LMI) using the Schur complement as

Note that the cost given by can be decoupled into the cost on the mean and the cost on the covariance as follows

Substituting and, we get

### III-B Distributionally Robust Polytopic Joint Risk Constraints

Given that the state constraint set $\mathcal{X}_{p}$ is assumed to be a convex polytope, the worst case joint probability of violating any of the $M$ state constraints over the horizon $N$ given by can be equivalently written as

Using Boole's inequality, the above joint distributionally robust risk constraint can be decomposed into individual distributionally robust risk constraints at each time step with $\delta_{i,k}$ denoting the individual risk bound^22^2The first and second subscript in $\delta_{i,k}$ denote the constraint defining the state constraint set $\mathcal{X}_{p}$ and the time step respectively. representing the worst case probability of violating the $i$ state constraint at time step $k$. That is, for each time step $k \in {\lbrack 1,N\rbrack}$, and for each half-space $i \in {\lbrack 1,M\rbrack}$ defining the constraint set $\mathcal{X}_{p}$, we have

Using Cantelli's inequality, the individual distributionally robust risk constraint in can be equivalently reformulated as deterministically tightened convex second-order cone constraint on the state mean as described in. That is,

where the DR quantile function ${\mathcal{Q}{(\delta_{i,k})}}:=\sqrt{\delta_{i,k}/{({1 - \delta_{i,k}})}}$ plays a similar role to that of $\mathbf{\Phi}^{- 1}$ corresponding to the Gaussian case. Note that, $\mathcal{Q}{({1 - \delta_{i,k}})}$ is also a monotonically increasing function of the risk, just like $\mathbf{\Phi}^{- 1}$ as shown in Figure 1 and the deterministic constraint tightening defined using it leads to a stronger tightening than the constant associated with the Gaussian chance constrained tightening. This stronger tightening will ensure that the worst case probability of state constraint violation is satisfied for any arbitrary distribution in the ambiguity set. It is clear from that Problem 1 can now be converted into the following convex programming problem.

Figure 1: Comparison of tightening constant for the Gaussian case and the distributionally robust case using the Cantelli’s inequality are shown here for the risk parameter δ ∈ (0, 0.5].

### Problem 2

Given the system and a total risk budget $\Delta$, we seek an optimal feedback control sequence of inputs $\mathbf{V}^{\star},\mathbf{K}^{\star}$ that steers the system from the initial state distribution belonging to with moments given by to the final state distribution belonging to with moments as in and by minimizing the finite-horizon cost function (III-A) and by respecting the DR risk constraint tightening given in.

### III-C Distributionally Robust Risk Allocation Optimization

From Theorem 1 in, the optimal cost obtained from solving Problem 2 will be a monotonically decreasing function of the stage risk budget $\delta_{i,k}$. For brevity of notation, we define the vector of all individual risk bounds over the whole time horizon and across all half-spaces defining the state constraint set $\mathcal{X}_{p}$ as ${\mathbf{δ}} = \begin{bmatrix}
\delta_{1,1} & \ldots & \delta_{M,N}
\end{bmatrix}^{\top} \in {\mathbb{R}}^{MN}$. Recall that in the risk allocation problem, the stage risk budget $\delta_{i,k}$ becomes a decision variable along with $\mathbf{K}$. However, in the distributionally robust risk constraints given by, $\delta_{i,k}$ and $\mathbf{K}$ occur in a bilinear form. A better tractable approach would be to concurrently allocate $\delta_{i,k}$ when solving the optimization Problem 2, so as to minimize the total cost given by (III-A).

### III-C1 Two-Stage Optimization Framework

In the following discussion, we elaborate how to optimally allocate the risk across the time steps and across the constraints defining the state constraint set $\mathcal{X}_{p}$. Following, a two-stage optimization framework is presented here. The upper stage optimization finds the optimal risk allocation ${\mathbf{δ}}^{\star}$ and the lower stage solves the covariance steering problem given by Problem 2 for the optimal controller $\mathbf{U}^{\star}$ given the optimal risk allocation ${\mathbf{δ}}^{\star}$ from the upper stage.

Let the value of the objective function after the lower stage optimization for a given risk allocation $\mathbf{δ}$ be

Then the upper-stage optimization problem can then be formulated as follows:

Note that is a convex optimization problem, given that the objective function $J^{\star}{({\mathbf{δ}})}$ is convex, and $\Delta \in {(0,0.5\rbrack}$. Following Theorem 1 in, the optimal cost can be reduced with each successive iteration by carefully increasing the risk allocations $\delta_{i,k}$. That is, the risk can be lowered by tightening the constraints that are too conservative, and increased by loosening the constraints that are already active. It now remains to define active and inactive constraints in the context of distributionally robust risk allocation. Note that the distributionally robust risk constraint given by can be equivalently written as

Here the quantity ${\overline{\delta}}_{i,k}$ represents the true risk experienced by the optimal trajectories, when using $(\mathbf{V}^{\star},\mathbf{K}^{\star})$. Clearly, the selected risk need not be equal to the actual risk once the optimization is completed. When $\delta_{i,k} = {\overline{\delta}}_{i,k}$, we say that the constraint is active, and is inactive otherwise. Solutions are termed good when the true risk is within a small margin of the allocated risk and the conservative ones correspond to the cases when $\delta_{i,k} > {\overline{\delta}}_{i,k}$.

### III-C2 Distributionally Robust Iterative Risk Allocation (DR-IRA) Algorithm

Starting with some feasible risk allocation ${\mathbf{δ}}^{(j)}$, with $j$ denoting the iteration number, solve Problem 2 to get the optimal controller $(\mathbf{V}_{(j)}^{\star},\mathbf{K}_{(j)}^{\star})$. It is straightforward to observe that using the above optimal controller at iteration $j$ leads to the optimal mean trajectory ${\overline{\mathbf{X}}}_{(\mathbf{j})}^{\star}$ respecting the optimal stage risk budget $\delta_{i,k}^{(j)}$. The risk budget is then successively loosened and tightened according to Algorithm 1 Algorithm ‣ III-C Distributionally Robust Risk Allocation Optimization ‣ III Covariance Steering with Distributionally Robust Risk Allocation ‣ Distributionally Robust Covariance Steering with Optimal Risk Allocation") as in, with the little change in the procedure that we solve the Problem 2 in this paper instead of the Problem 2 mentioned in Algorithm 1 of and this new allocation is fed back to the optimizer. This iterative process generates a sequence of risk allocations by continuously lowering the optimal cost.

Solve Problem 2 with current δ to get $\overline{\delta}$.
N̂← the number of active constraints
for each jth inactive constraint at kth time step do
$\delta_{k}^{(j)}\leftarrow{{\rho\delta_{k}^{(j)}} + {{({1 - \rho})}{\overline{\delta}}_{k}^{(j)}}}$
$\delta_{res}\leftarrow{\Delta - {\sum_{k = 1}^{N}{\sum_{j = 1}^{M}\delta_{k}^{(j)}}}}$
for each jth active constraint at kth time step do
Algorithm 1 The covariance steering algorithm with DR-IRA

### III-D Distributionally Robust Convex Conic Risk Constraints

Constraints of the convex cone forms are usually known to be more prevalent than the polytopic constraints in engineering applications such as spacecraft rendezvous or landing. In the following discussion, we extend our covariance steering formulation to distributionally robust convex cone constraints. Consider the following convex cone state constraint set

We can specify the distributionally robust risk constraint for all time steps $k \in {\lbrack 1,N\rbrack}$ with conic state constraint set $\mathcal{X}_{c}$ as

Notice that is an infinite dimensional constraint and not necessarily convex. Hence, we resort to a convex approximation so that and holds true for all $\Delta \in {(0,0.5\rbrack}$. We first seek to relax as DR quadratic risk constraint and then use the reverse union bound approximation.

### III-D1 Relaxing the DR Conic Risk Constraint

### Lemma 1

Given $\delta_{k} \in {(0,0.5\rbrack}$ for all $k \in {\lbrack 1,N\rbrack}$, the following DR quadratic risk constraint

is a relaxation of the original DR conic risk constraint

### Proof

For each time step $k \in {\lbrack 1,N\rbrack}$, denote $\psi_{i,k}:={{a_{i}^{\top}x_{k}} + b_{i}}$ and $\kappa_{k}:={{c^{\top}{\overline{x}}_{k}} + d}$ with $a_{i}^{\top}$ denoting the i^th^ row of $A$, and observe that can be equivalently written as

### Proposition 1

The DR quadratic constraint is satisfied if the following constraints are satisfied (subscript $k$ dropped for brevity of notation) for some non-negative $f_{1},\ldots,f_{n}$ and $\beta_{1},\ldots,\beta_{n}$:

$\sup\limits_{{\mathbb{P}}_{x} \in \mathcal{P}^{x}}{{\mathbb{P}}_{x}\left\lbrack {{\sum\limits_{i = 1}^{n}\left| \psi_{i} \right|} \leq f_{i}} \right\rbrack}$ ${{\geq {1 - {\beta_{i}\delta}}},{i = {\lbrack 1,N\rbrack}}},$ (40a)
$\sum\limits_{i = 1}^{n}f_{i}^{2}$ ${\leq \kappa^{2}},$ (40b)
$\sum\limits_{i = 1}^{n}\beta_{i}$ ${= 1}.$ (40c)

### Proof

The proof uses the same arguments as in and hence is omitted. ∎

### III-D2 Approximation Using Reverse Union Bound

Note that the constraints given by (40b) can be equivalently written using the mean dynamics given by as

which holds if and only if

### Proposition 2

Let ${\epsilon_{i,k}^{1},\epsilon_{i,k}^{2}} > 0$ for all $i = {1,\ldots,n}$ and $k = {1,\ldots,N}$. Assume that the following convex DR SOC constraints hold true for some $\mathbf{V},\mathbf{K}$, and ${\epsilon_{i,k}^{1} + \epsilon_{i,k}^{2}} \geq {2 - {\beta_{i}\delta_{k}}}$.

${{{a_{i}^{\top}E_{k}\overline{\mathbf{X}}} + {\sqrt{\frac{\epsilon_{i,k}^{1}}{1 - \epsilon_{i,k}^{1}}}\left\| {\Sigma_{\mathbf{Y}}^{\frac{1}{2}}{({I + {\mathcal{B}\mathbf{K}}})}^{\top}E_{k}^{\top}a_{i}} \right\|_{2}}} \leq {f_{i,k} - b_{i}}},$ (43a)
${{{- {a_{i}^{\top}E_{k}\overline{\mathbf{X}}}} + {\sqrt{\frac{\epsilon_{i,k}^{2}}{1 - \epsilon_{i,k}^{2}}}\left\| {\Sigma_{\mathbf{Y}}^{\frac{1}{2}}{({I + {\mathcal{B}\mathbf{K}}})}^{\top}E_{k}^{\top}a_{i}} \right\|_{2}}} \leq {f_{i,k} + b_{i}}}.$ (43b)

Then, the two-sided DR risk constraint given by (40a) holds true as well.

### Proof

It is important to fix $\epsilon_{i,k}^{1}$, and $\epsilon_{i,k}^{2}$ apriori to avoid bilinearity in the decision variables of constraints (43a) and (43b) respectively. Thus, the relaxed DR cone risk constraints given by was approximated using and the alternate approximations (43a) and (43b) of the two-sided DR risk constraint (40a). Note that the constraints, (43a) and (43b) are convex and can be solved using the standard SDP solvers used similarly for the polyhedral counterparts. In terms of computational complexity, notice that there are ${2n} + 1$ SOC constraints per time step and thus ${({{2n} + 1})}N$ SOC constraints in total.

## Numerical Simulations

In this section, we demonstrate the proposed approach using two examples. One dealing with spacecraft proximity operation as in, and the second one using a simple double integrator based path planning as in. The code is available at [https://github.com/venkatramanrenganathan/Covariance-Steering-With-Optimal-DR-Risk-Allocation](https://github.com/venkatramanrenganathan/Covariance-Steering-With-Optimal-DR-Risk-Allocation).

### IV-A Double Integrator Path Planning

### IV-A1 Simulation Setup

We consider a path-planning problem for a vehicle modelled using the following time invariant and stochastic double integrator system dynamics:

We assume $\mu_{0} = \begin{bmatrix}
\end{bmatrix}$ and $\Sigma_{0} = {\text{diag}{(0.1,0.1,0.01,0.01)}}$ and the discretization time step to be ${\Deltat} = 0.2$, with the horizon $N = 15$. We wish to steer the distribution from the above initial state to the final mean $\mu_{f} = 0$ with final covariance $\Sigma_{f} = {0.25\Sigma_{0}}$, while minimizing the cost function with penalty matrices $Q = {\text{diag}{}}$ and $R = {10^{3}I_{2}}$. The state constraints are defined as ${0.2{({x - 1})}} \leq y \leq {- {0.2{({x - 1})}}}$. We impose the joint probability of failure over the whole horizon to be $\Delta = 0.10$, which implies that the worst case probability of violating any state constraint over the whole horizon is less than $10\%$. For the Monte Carlo trials, the disturbances were sampled from a multivariate Laplacian distribution with zero mean and unit covariance. Similarly, the initial state $x_{0}$ was sampled from a multivariate Laplacian distribution with mean $\mu_{0}$ and covariance $\Sigma_{0}$. For comparison, simulations were performed with both Gaussian and distributionally-robust chance constraints.

(a) Gaussian chance constraints.

(b) Distributionally-robust chance constraints.

Figure 2: Comparison of 100 independent Monte Carlo trajectories using Gaussian (a) and DR (b) chance constraints with x0 and noise history {wk} sampled from multivariate Laplacian distributions.

Figure 3: Allocated and true risks with Gaussian chance constraints.

Figure 4: Allocated and true risks with distributionally-robust chance constraints.

### IV-A2 Results & Discussion

The results from 500 independent Monte-Carlo trials are shown in Figure 2. Given that the disturbances were sampled from a multivariate Laplacian distribution, it is evident from Figure 2(a) that some Monte-Carlo trials resulted in a violation of the state constraints as the covariance steering was performed assuming Gaussian disturbances. On the other hand, the distributionally robust risk-constrained covariance steering (Figure 2(b)) ensured that the total risk budget is respected, despite being more conservative. Moreover, all probabilistic state constraints were satisfied. This shows that, assuming Gaussian chance constraints might potentially lead to severe miscalculation of the risk. It is evident from Figures 4 and 4 that the true risk is always upper bounded by the allocated risk regardless of whether a Gaussian or a DR iterative risk allocation is employed.

### IV-B Spacecraft Proximity Operation

### IV-B1 Simulation Setup

We demonstrate the proposed theory using the spacecraft proximity operations problems in orbit as described in albeit with certain parameter changes. We perform three set of simulation here, namely: a) covariance steering with distributionally robust polytopic state risk constraints; b) covariance steering with distributionally robust iterative risk allocation for polytopic state risk constraints; and c) covariance steering with distributionally robust iterative risk allocation for convex conic state risk constraints using reverse union bound approximation. For the case of polytopic state risk constraints, we assume $\mu_{0} = \begin{bmatrix}
\end{bmatrix}$ and $\Sigma_{0} = {0.4\text{diag}{(1,1,1,0.1,0.1,0.1)}}$. We wish to steer the distribution from the above initial state to the final mean $\mu_{f} = 0$ with final covariance $\Sigma_{f} = {0.5\Sigma_{0}}$, while minimizing the cost function with penalty matrices $Q = {\text{diag}{}}$ and $R = {10^{3}I_{3}}$. We impose the joint probability of failure over the whole horizon to be $\Delta = 0.15$. As in the previous example, the disturbances were sampled from a multivariate Laplacian distribution with zero mean and unit covariance. Similarly, the initial state $x_{0}$ was sampled from a multivariate Laplacian distribution with mean $\mu_{0}$ and covariance $\Sigma_{0}$. For the cone constraints, we shift the initial $x$ mean to $\mu_{0}^{} = 10$.

### IV-B2 Results & Discussion

(a) DR chance constraint solution with optimal risk allocation.

(b) DR chance constraint solution with uniform risk allocation.

(c) Gaussian chance constraint solution with optimal risk allocation.

Figure 5: Trajectories of 500 independent Monte Carlo samples for distributionally-robust and Gaussian polytopic chance constraints with 3 σ covariance ellipses. Each subplot displays the projection of the full state onto the x − y plane.

The Monte Carlo results of DR covariance steering are shown in Figure 5, which show the $x - y$ projection of the state trajectories and 3$\sigma$ covariance ellipses for three different risk solutions. Notice that the Gaussian solution in Figure 5(c) remains too close to the boundary of the state space, which implies that under non-Gaussian noises, a CS controller based on Gaussian risk constraints leads to a significant miscalculation of risk. On the other hand, the DR solution in Figure 5(b) steers to the middle of the space to ensure proper constraint satisfaction; but this too is under suboptimal risk placement, from which Figure 5(a) arises as the optimal trajectories corresponding to the optimal risk budget. Figure 6 shows the monotonically decreasing costs with each iteration of the IRA scheme, which implies the optimal risk budget has resulted in the lowest possible cost.

Figure 6: Optimal cost for each DR-IRA algorithm iteration for polytope and cone chance constraints.

Figure 7: Optimal trajectories for 500 independent Monte Carlo trials under DR cone chance constraints.

The simulation results of covariance steering with distributionally robust iterative risk allocation for convex conic state risk constraints using reverse union bound approximation are shown in Figure 7, with the cost versus the iteration trade-off shown in Figure 6. The state trajectories and their 3$\sigma$ dispersions remain well within the cone at all time steps and are robust to any zero mean, unit covariance disturbance.

## Conclusion and Future Directions

In this article we have incorporated an DR-IRA strategy to optimize the worst case probability of violating the state constraints at every time step within the CS problem of a linear stochastic system subject to distributionally robust risk constraints. The use of DR-IRA in the context of CS with distributionally robust risk constraints results in optimal solutions that have a true risk much closer to the intended design requirements, compared to the use of a uniform risk allocation. We also extended the approach to quadratic chance constraints in the form of convex cones. Future work will seek to solve the CS problem with output feedback and also extend the problem setting to handle nonlinear dynamics. Further, the general problem of moment steering involving the first $k \in \mathcal{N}$ moments is interesting to be investigated as well.
