<!-- arxiv-full-text:v1 {"arxiv_id": "2504.10814", "source": "arxiv-html"} -->

## Introduction

Many applications in finance and engineering require controlling the risk of extreme outcomes. A widely used measure for tail risk is the *conditional value-at-risk* (CVaR), defined as the expected value of losses exceeding a given quantile. CVaR is a coherent and convex risk measure, so optimization problems involving CVaR can be reliably and efficiently solved.

Many practical applications, from portfolio optimization to quantile regression, can be formulated as quadratic programs with CVaR constraints. While these problems are convex and can be reformulated as standard quadratic programs, the number of variables and constraints grows linearly with the number of scenarios. For problems with many scenarios, general-purpose solvers become prohibitively slow or fail entirely. To address this challenge, we develop a fast and scalable method for solving quadratic programs with CVaR constraints.

We present two main contributions. First, we develop an $O(m\log m)$ algorithm for projecting onto CVaR constraints, where $m$ is the number of scenarios. Building on this algorithm, our second contribution is an operator splitting method for solving large-scale CVaR-constrained quadratic programs. The method alternates between solving a linear system and performing parallel projections, onto CVaR constraints using our specialized algorithm and onto box constraints by simple clipping. Numerical examples from several application domains demonstrate that our method outperforms general-purpose solvers by several orders of magnitude on problems with up to millions of scenarios.

### Conditional value-at-risk (CVaR)

The conditional value-at-risk (CVaR) at level $\beta$ is a risk measure that captures the expected value over the worst $(1-\beta)$ fraction of outcomes of a real-valued random variable. For a random variable $X$ representing losses (where larger values are worse), we first define the value-at-risk (VaR) at level $\beta$ as CVaR at level $\beta$ is defined as the expected value of all losses exceeding VaR at level $\beta$, At the same level $\beta$, CVaR provides an upper bound on VaR.

### Sample CVaR

For a finite set of samples $z_{1},\ldots,z_{m}\in{\mbox{\bf R}}$ representing the distribution of losses, Rockafellar and Uryasev showed that the CVaR at level $\beta$, denoted $\phi_{\beta}:{\mbox{\bf R}}^{m}\to{\mbox{\bf R}}$, can be computed as where $(z-\alpha)_{+}=\max\{z-\alpha,0\}$ is the positive part of $z-\alpha$. A CVaR constraint at level $\beta$ can be represented by a set of linear inequality constraints,

### CVaR-constrained quadratic programs

This work presents a customized solver for the CVaR-constrained quadratic program (CVQP), where $x\in{\mbox{\bf R}}^{n}$ is the decision variable. The objective function is defined by a positive semidefinite matrix $P\in{\mbox{\bf S}}^{n}_{+}$ and a vector $q\in{\mbox{\bf R}}^{n}$. The CVaR constraint is defined by quantile level $\beta\in$, threshold $\kappa\in{\mbox{\bf R}}$, and matrix $A\in{\mbox{\bf R}}^{m\times n}$. Additional linear inequality constraints are defined by a matrix $B\in{\mbox{\bf R}}^{p\times n}$, and vectors $l\in\left({{\mbox{\bf R}}\cup\{-\infty\}}\right)^{p}$, $u\in\left({{\mbox{\bf R}}\cup\{\infty\}}\right)^{p}$. Since $P$ is positive semidefinite and the constraints are convex, the CVQP is a convex optimization problem. We focus on the case where $p\ll m$, i.e., the number of additional constraints is much smaller than the number of scenarios.

We assume the CVQP problem is feasible and that $P$, $A$, and $B$ have zero common nullspace, which ensures that the problem is bounded. This condition also implies that the matrix $M=P+\rho(A^{T}A+B^{T}B)$ is positive definite for any $\rho>0$, which is needed for the ADMM linear system solve described in §2. In practice the condition holds when $P$ is positive definite or when $A$ has full column rank.

### CVaR terms in the objective

The CVQP formulation extends to problems with CVaR terms in the objective. Consider the problem Using the translation-equivariance property of CVaR (i.e., $\phi_{\beta}(X+c)=\phi_{\beta}(X)+c$), we introduce an auxiliary variable $t$ and reformulate as Defining the decision variable as the pair $(x,t)$, this is an instance of the standard CVQP form.

### Quadratic program solvers

By using the linear inequality representation of the CVaR constraint, the CVQP can be reformulated as a standard quadratic program and solved with any QP solver. However, when the number of scenarios $m$ is large, this approach becomes prohibitively slow.

### Applications

CVaR-constrained quadratic programs arise in many domains. In portfolio optimization, $x$ represents portfolio weights and $Ax$ gives portfolio losses across $m$ return scenarios; the CVaR constraint limits the expected loss in the worst $(1-\beta)$ fraction of scenarios, while the quadratic objective captures risk-adjusted returns. In supply chain planning, $x$ includes order quantities and routing decisions, with scenarios modeling demand uncertainty and supplier disruptions; CVaR constraints bound extreme total cost realizations. Similar formulations appear in network flow problems with stochastic capacities, facility location and disaster response logistics, energy systems with uncertain generation and prices, and radiation treatment planning, where CVaR constraints replace intractable dose-volume constraints. In control and statistical learning, CVaR provides tractable convex approximations to chance constraints. For a comprehensive review, see.

### Related work

CVaR constraints were introduced by Rockafellar and Uryasev and are now standard in risk-constrained optimization. Our method builds on operator splitting, which decomposes the problem into simpler subproblems: a linear system solve and projections.

The CVaR projection algorithm adds to a family of finite-termination projection methods, including the classical simplex projection and isotonic regression. Concurrently with the development of our CVaR projection algorithm, Roth and Cui released a preprint \[15 algorithms for projection onto the top-k-sum sublevel set")\], later published as \[17 algorithms for projection onto the top-k-sum sublevel set")\], containing two finite termination algorithms for CVaR projection attaining the same complexity. After corresponding with the authors, we were unable to find any equivalence between their algorithms and ours.

Roth and Cui also proposed a second-order computational framework for CVaR-constrained optimization, using a semismooth Newton-based augmented Lagrangian method. As a second-order method, it can achieve superlinear convergence near a solution, while ADMM is a first-order method with an $O(1/k)$ convergence rate. On the other hand, each ADMM iteration is cheap (a single backsolve and parallel projections after an initial factorization), and the method is simple to implement. In our experience, ADMM reaches moderate accuracy in few iterations, which is sufficient for most applications.

### Outline

This paper is organized as follows. In §2, we present an ADMM-based solution method for the CVQP. §3 establishes theoretical foundations for projecting onto CVaR constraints, which we use to develop our $O(m\log m)$ projection algorithm in §4. In §5, we present benchmark results comparing our method against state-of-the-art solvers on portfolio optimization and quantile regression problems with up to millions of scenarios. §6 discusses possible extensions to our method.

## Solution via ADMM

### ADMM

We solve the CVQP by reformulating the problem and applying the alternating direction method of multipliers (ADMM). By introducing auxiliary variables $z\in{\mbox{\bf R}}^{m}$ and $\tilde{z}\in{\mbox{\bf R}}^{p}$, we can rewrite problem as where $\mathcal{C}=\{z\mid\phi_{\beta}(z)\leq\kappa\}$. The auxiliary variables $z$ and $\tilde{z}$ decouple the CVaR constraint from the box constraints, so that each can be handled separately in the ADMM updates below. Here, $I_{\mathcal{C}}$ and $I_{[l,u]}$ are the indicator functions for the sets $\mathcal{C}$ and $\{\tilde{z}\mid l\leq\tilde{z}\leq u\}$, respectively, given by We use the scaled dual variables $u=(1/\rho)y$ and $\tilde{u}=(1/\rho)\tilde{y}$, where $\rho>0$ is a hyperparameter and $y\in{\mbox{\bf R}}^{m}$ and $\tilde{y}\in{\mbox{\bf R}}^{p}$ are the vectors of dual variables associated with the equality constraints $Ax=z$ and $Bx=\tilde{z}$, respectively. We use ADMM with over-relaxation (see for analysis), with over-relaxation parameter $\alpha\in$.

For notational convenience we define the linear system parameters Our assumption on the common nullspace of $P$, $A$, and $B$ implies that $M$ is positive definite. The ADMM updates are The operator $\Pi_{\mathcal{C}}$ is the (Euclidean) projection onto $\mathcal{C}$ and $\Pi_{[l,u]}$ is the projection onto the set $[l,u]\subset{\mbox{\bf R}}^{p}$. The over-relaxation, dual updates, and box projection are all trivial operations; the linear system solve requires one cached factorization of $M$. The main computational bottleneck is the CVaR projection, which we address in §3--4.

It is well known that this ADMM algorithm converges, with a worst-case $O(1/k)$ convergence rate, though linear convergence is commonly observed in practice for quadratic programs.

### Dynamic penalty parameter

While ADMM converges for any fixed penalty parameter $\rho>0$, the convergence rate can be improved by adaptively updating $\rho$. A simple and effective update scheme adjusts $\rho$ based on the relative magnitudes of the primal and dual residuals. When the primal residual is $\mu$ times larger than the dual residual, we multiply $\rho$ by a factor $\tau>1$; when the dual residual is $\mu$ times larger than the primal residual, we divide $\rho$ by $\tau$. Since $\rho$ appears in the matrix $M$, each update requires re-factorizing the linear system. To balance computational cost with convergence benefits, we perform these updates at fixed intervals of $T$ iterations.

### Evaluating the updates

The updates and are trivial to implement. The update is also a very simple clipping operation: where $v=\tilde{z}^{k+1/2}+\tilde{u}^{k}$.

The update can be expressed as $x^{k+1}=-M^{-1}p^{k}$, which requires the solution of a linear system of equations with positive definite coefficient matrix $M$. We factorize $M$ once (for example, a sparse Cholesky or $LDL^{T}$ factorization) so that subsequent solves require only the backsolve. This can substantially improve the efficiency of this step; when $M$ is dense, for example, the first factorization costs $O(n^{3})$ flops, while subsequent solves require only $O(n^{2})$ flops. (When $M$ is sparse the speedup from caching the factorization is smaller than $n$, but still very significant.)

That leaves only the CVaR projection, for which we develop an $O(m\log m)$ algorithm in the next two sections.

### Summary

For convenience we summarize the complete CVQP method in Algorithm 1. The CVaR projection is the main computational bottleneck and uses the $O(m\log m)$ algorithm described in §4.

1:Factorize M = P + ρ(ATA + BTB). 3: Solve linear system. 5: Project onto CVaR constraint; see §4. 6: Clip to box constraints. 7: Update dual variables –. 8: Update ρ and re-factorize M if needed. 9:until primal and dual residuals below tolerance. Algorithm 1 CVQP solver

## CVaR projection preliminaries

We now present preliminaries that motivate our efficient algorithm for evaluating the projection operator $\Pi_{\mathcal{C}}$, i.e., for solving the problem with variable $z\in{\mbox{\bf R}}^{m}$.

The CVaR constraint can be expressed equivalently using the sum of $k$ largest components function, where $z_{}\geq z_{}\geq\cdots\geq z_{[m]}$ are the components of $z$ in nonincreasing order. This is a convex function that sums the $k$ largest elements of a vector (the pointwise maximum of $\binom{m}{k}$ linear functions). Setting $k=(1-\beta)m$ and evaluating the infimum over $\alpha$ in the Rockafellar-Uryasev formula (the minimizer is $\alpha=z_{[k]}$), we obtain $\phi_{\beta}(z)=(1/k)f_{k}(z)$. The constraint $\phi_{\beta}(z)\leq\kappa$ is therefore equivalent to $f_{k}(z)\leq\kappa k$. We rewrite problem as where $d=\kappa k$. We assume $(1-\beta)m\in{\mbox{\bf N}}$ (and round up to the nearest integer if not).

We will use the formulation to derive our CVaR projection algorithm. While this is a computationally tractable convex optimization problem, we seek closed form or computationally efficient ways to evaluate this projection operator. Since merely evaluating $f_{k}$ with $k=(1-\beta)m$ has a complexity of $O(m\log m)$, we desire a similar complexity for the projection operator.

### Sorted projection

Let $P\in{\mbox{\bf R}}^{m\times m}$ be a permutation matrix that sorts $v$ in descending order, i.e., $(Pv)_{1}\geq(Pv)_{2}\geq\cdots\geq(Pv)_{m}$. We will denote the sorted vector $Pv$ as $v^{\prime}$. Since for any $z\in{\mbox{\bf R}}^{m}$, the solution to the projection problem is given by The last equality is the change of variable $u=Pz$. In words, we can sort $v$ in descending order, project the sorted vector $v^{\prime}$, and unsort the result to obtain the projection of $v$ onto the set $\{z\mid f_{k}(z)\leq d\}$.

### Optimality conditions

We characterize the optimality conditions of the projection problem; these conditions will be used in §4.3 to prove the correctness of the algorithm. Let $\mathcal{A}=\{a\in\{0,1\}^{m}\mid\mathbf{1}^{T}a=k\}$ be the set of all $\binom{m}{k}$ $k$-hot indicator vectors. Since $f_{k}(z)=\max_{a\in\mathcal{A}}a^{T}z$, the constraint $f_{k}(z)\leq d$ is equivalent to $a^{T}z\leq d$ for all $a\in\mathcal{A}$. We can therefore rewrite problem in the equivalent form where the subscript $i$ enumerates the elements of $\mathcal{A}$.

The KKT conditions tell us a $z,\lambda$ pair is optimal if and only if The optimality conditions motivate an algorithm that solves the KKT system. We will define $z=v-\Delta$, where $\Delta$ is the vector we remove from $v$ to get the projection. The KKT conditions above imply that $\Delta$ is a nonnegative combination of the vectors $a_{i}$ for which $a_{i}^{T}z=d$, i.e., the indicators of the largest $k$ entries of $z$. (Note that there are potentially several such vectors in the presence of ties: consider the largest 2 entries in the vector $$.) Thus, if we can construct a vector $\Delta$ that is a nonnegative combination of largest-$k$ indicator vectors, such that $f_{k}(v-\Delta)=d$, then we have found the projection $z=v-\Delta$.

### Algorithm motivation

We describe at a high level the motivation behind our projection algorithm. We pre-process by sorting and work with the sorted vector $v^{\prime}$, since from §3.1 we know that sort-project-unsort is the same as projecting. We then proceed by incrementally constructing $\Delta$ until the sum of the $k$ largest elements of $v^{\prime}-\Delta$ is equal to $d$.

We want to begin decreasing elements of $v^{\prime}$ until the sum of the $k$ largest elements is equal to $d$. Intuitively, we should decrease the largest $k$ elements without modifying the remaining elements, since they do not affect the sum. We begin by reducing the largest elements uniformly until either the constraint is satisfied, or until the $k$th largest element ties the next element. We reduce each of the $k$ largest elements by the same amount because we are penalized by the sum of squared changes.

If reducing the largest $k$ elements causes elements $k$ and $k+1$ to tie, it is intuitive that the tied elements should be further reduced by the same amount; otherwise a reduction would be applied to an element not in the largest $k$. Since we also want to uniformly decrease the largest elements preceding the tie, we need to decide the ratio of these two reductions. Given this ratio, we reduce the untied and tied entries until either the constraint is satisfied or the next tie occurs.

We will need to determine this ratio at each step of the algorithm, since at a given step of the algorithm, the altered vector $v^{\prime}-\Delta$ will be partitioned into three regions: first the largest $n_{u}\in{\mbox{\bf N}}$ *untied* elements, then the $n_{t}\in{\mbox{\bf N}}$ *tied* elements, and lastly the remaining unaltered elements: The core insight of the algorithm is deriving the ratio of reducing the untied and tied elements; this ratio is derived in §4.

## CVaR projection algorithm

With the preliminaries in place, we now present our CVaR projection algorithm.

### Pre- and post-processing

The CVaR projection algorithm is applied to the vector $v$ sorted in descending order as described in §3.1. The complexity of sorting $v$ and then unsorting the projection is $O(m\log m)$. The sorting and unsorting are in practice carried out with indices; the permutation matrix $P$ is never explicitly formed.

### Algorithm state

The algorithm's state is $j$: the iterate number, $n_{u}$: the number of untied entries, $n_{t}$: the number of tied entries, $\eta$: the decrease to the untied entries, $S$: the sum of the largest $k$ entries, $a_{t}$: the value of the tied entries, $a_{u}$: the value of the last untied entry, $a_{e}$: the value of the first unaltered entry.

The algorithm is initialized with $n_{u}=k$, $n_{t}=0$, $\eta=0$, $S=\sum_{i=1}^{k}v^{\prime}_{i}$, $a_{u}=v^{\prime}_{k}$, and $a_{e}=v^{\prime}_{k+1}$. The algorithm repeats the decrease step described in §4.1 until $S=d$, after which the projection of the sorted $v^{\prime}$, is formed, unsorted, and returned.

### Decrease step

At each step, the algorithm decreases the entries of $z$ along a direction $\delta\in{\mbox{\bf R}}^{m}$ that depends on the current group structure. The update is $z\leftarrow z-s_{0}\delta$, where $s_{0}>0$ is chosen as the largest scaling such that $z$ remains sorted and the sum of its $k$ largest entries stays at least $d$. Three events can limit $s_{0}$: the last untied entry reaches the tied value (*merge*: the untied block shrinks by one), the tied value reaches the first unaltered entry (*absorb*: the tied block grows by one), the sum constraint $S=d$ is met (*termination*).

On every nonterminal step, the tied block grows by one entry (from a merge or an absorb). The algorithm terminates in at most $m$ steps. We handle the first step separately because there is no tied block yet; all subsequent steps share the same general formulas.

### First step

On the first step, $n_{u}=k$ and $n_{t}=0$. The direction is i.e., all $k$ entries decrease uniformly. Since there is no tied block, only absorb and termination can occur, giving $s_{0}=\min(a_{u}-a_{e},~(S-d)/k)$. If $S-s_{0}k=d$, the algorithm terminates with $\eta=s_{0}$. Otherwise, entries $k$ and $k+1$ form a tied block, and the state is updated to The values of $a_{u}$ and $a_{e}$ are updated as in the general step below, using the new $n_{u}$, $n_{t}$, and $\eta$.

### General step

For all subsequent steps, $n_{t}\geq 2$ and $k-n_{u}\geq 1$. The direction is The untied entries decrease at rate $n_{t}/(k-n_{u})>1$, the tied entries at rate $1$, and the unaltered entries are unchanged. Note that $\delta$ is a nonnegative combination of $k$-hot indicator vectors: is the set of $k$-hot indicator vectors whose first $n_{u}$ entries are $1$, with the remaining $k-n_{u}$ ones among entries $n_{u}+1$ through $n_{u}+n_{t}$.

### Scaling the step

We now describe how to compute $s_{0}$ for the general step. Let $z(s)=z-s\delta(n_{u},n_{t},k)$. The scaling $s_{0}$ is the minimum of three candidate step sizes, corresponding to the three events described above.

*Merge.* The step $s_{1}$ at which the last untied entry reaches the tied value, i.e., $z(s_{1})_{n_{u}}=z(s_{1})_{n_{u}+1}$. If $n_{u}=0$, there are no untied entries, and $s_{1}=\infty$. Otherwise, $s_{1}=\left(a_{t}-a_{u}\right)/\left(1-\frac{n_{t}}{k-n_{u}}\right)$.

*Absorb.* The step $s_{2}$ at which the tied value reaches the first unaltered entry, i.e., $z(s_{2})_{n_{u}+n_{t}}=z(s_{2})_{n_{u}+n_{t}+1}$. If $n_{u}+n_{t}=m$, there are no unaltered entries, and $s_{2}=\infty$. Otherwise, since the tied entries decrease at unit rate while $a_{e}$ is unchanged, $s_{2}=a_{t}-a_{e}$.

*Termination.* The step $s_{3}$ at which the sum of the $k$ largest entries equals $d$, i.e., $s_{3}=(S-d)/w$, where $w=n_{u}\frac{n_{t}}{k-n_{u}}+(k-n_{u})$.

The step is $s_{0}=\min\{s_{1},s_{2},s_{3}\}$, and the update is $z\leftarrow z-s_{0}\delta(n_{u},n_{t},k)$.

### Updating the state

Instead of explicitly carrying out this vector subtraction at every step (which would have a complexity of $O(m)$ per iterate), the constant size algorithm state is updated to reflect the change in the vector. The updates are applied in the order shown: The first group ($\eta$, $S$, $a_{t}$) uses the pre-update values of $n_{u}$ and $n_{t}$; the second group ($a_{u}$, $a_{e}$) uses the updated values of $n_{u}$, $n_{t}$, and $\eta$.

### Complexity

At each step, $n_{u}$ either decreases by $1$, or remains the same. At each step, $n_{t}$ increases by $1$. If the algorithm hasn't terminated after $m$ steps, then there are $m$ tied entries, thus the subsequent decrease step will reduce the sum to the desired value, and the algorithm will terminate. Each step of the algorithm has constant complexity, and thus the algorithm (with sorted input) has complexity $O(m)$. Therefore, including the sorting and unsorting, the total complexity of the algorithm is $O(m\log m)$.

### Correctness

At termination, the algorithm returns $z=v^{\prime}-\sum_{t}\delta_{j}$. Note that, each $\delta_{j}$ is a nonnegative combination of largest-$k$ indicator vectors. Thus, the algorithm returns $z$ which satisfies Since the decrease step maintains the monotonicity of $v^{\prime}$, all previous largest-$k$ indicators are still valid indicators of the largest $k$ entries of $z$. Thus, the termination criterion provides that However, and are exactly the KKT conditions for the projection problem described in §3.2. Therefore, the algorithm correctly computes the projection of $v^{\prime}$ onto the set $\{z\mid f_{k}(z)\leq d\}$.

## Numerical experiments

We compare our CVaR projection algorithm and our CVQP solver with two general-purpose solvers, Mosek and Clarabel. We first benchmark the projection algorithm on synthetic instances, then benchmark the CVQP solver on portfolio optimization and quantile regression problems. Code is available at

### Experimental setup

All experiments were run on a Google Cloud n1-highmem-32 instance (32 vCPUs, 208 GB RAM), with a two-hour time limit per solve. For our CVQP solver we use ADMM penalty parameter $\rho^{}=10^{-2}$, over-relaxation parameter $\alpha=1.7$, and update $\rho$ adaptively with parameters $\mu=10$ and $\tau=2$. We stop when primal and dual residuals satisfy absolute tolerance $10^{-4}$ and relative tolerance $10^{-3}$. Mosek and Clarabel are called through CVXPY with default settings. When we tighten our tolerances to $10^{-6}$, objective values agree with both solvers to about four significant figures.

### CVaR projection

We generate random CVaR projection problems with vectors $v\in{\mbox{\bf R}}^{m}$ having entries uniformly distributed on $$, with $k=(1-\beta)m$ and $\beta=0.95$. For each $v$, we set the constraint threshold to $d=\eta f_{k}(v)$ in problem, where $\eta\in$ controls problem difficulty (larger $\eta$ gives easier problems), and project $v$ onto the convex set $\{z\mid f_{k}(z)\leq d\}$.

### Results

Figure 1 shows solve times versus number of scenarios $m$ for $\eta=0.5$, averaged over 10 random instances. Our method solves these problems in $0.51$ ms at $m=10^{4}$ and $1.98$ s at $m=10^{7}$, more than two orders of magnitude faster than both Mosek and Clarabel across all tested sizes. Mosek does not solve instances with $m\geq 3\times 10^{6}$ within the time limit.

Figure 1: CVaR projection solve times, with η = 0.5.

### Portfolio optimization

We consider a portfolio optimization problem with $n$ assets and $m$ return scenarios. The matrix $R\in{\mbox{\bf R}}^{m\times n}$ contains asset returns, where $R_{ij}$ is the return of asset $j$ in scenario $i$. The mean return vector $\mu\in{\mbox{\bf R}}^{n}$ and covariance matrix $\Sigma$ are given by The portfolio optimization problem is with variable $x\in{\mbox{\bf R}}^{n}$ (the portfolio weights), risk aversion parameter $\gamma>0$, and a CVaR constraint bounding the expected loss in the worst $(1-\beta)$ fraction of scenarios.

### CVQP form

The problem maps to CVQP form as

### Problem instances

We generate return scenarios using a two-component Gaussian mixture model where $\omega$ is the probability of normal market conditions, $\nu$ is the mean return per asset (positive in normal conditions, negative in stress periods), and $\sigma>1$ scales the volatility during stress periods. We use parameters

### Results

Figure 2 shows solve times versus number of scenarios $m$ for problems with $n=2000$ assets, averaged over 3 random instances. Our method is faster than both general-purpose solvers by one to three orders of magnitude. Mosek does not solve instances with $m\geq 10^{6}$ within the time limit, and Clarabel does not solve instances with $m\geq 10^{5}$. Our method solves instances with up to one million scenarios in under 26 minutes.

Figure 2: Portfolio optimization solve times, with n = 2000 assets.

### Quantile regression

Given $m$ data points with features $u_{i}\in{\mbox{\bf R}}^{n}$ and responses $y_{i}\in{\mbox{\bf R}}$, the $\tau$-quantile regression problem is with variables $x\in{\mbox{\bf R}}^{n}$ and $x_{0}\in{\mbox{\bf R}}$, where $\rho_{\tau}(z)=\tau(z)_{+}+(1-\tau)(z)_{-}$ is the tilted $\ell_{1}$ penalty and $\tau\in$ is the quantile level. The asymmetric penalty weighs underpredictions $\tau/(1-\tau)$ times more than overpredictions, so the optimal prediction is the conditional $\tau$-quantile of $y$ given $u$, rather than the conditional mean.

### CVaR reformulation

Defining the feature matrix $U\in{\mbox{\bf R}}^{m\times n}$ with rows $u_{i}^{T}$, the response vector $y\in{\mbox{\bf R}}^{m}$, and $\bar{u}=\frac{1}{m}\sum_{i=1}^{m}u_{i}$, we use the identity $\rho_{\tau}(z)=(1-\tau)(-z)+(z)_{+}$ to write the objective as where $\bar{y}=\frac{1}{m}\sum_{i=1}^{m}y_{i}$. The terms involving $x_{0}$ can be written as which is $(1-\tau)$ times the sample CVaR formula evaluated at $\alpha=x_{0}$. Minimizing over $x_{0}$ yields the infimum in the CVaR definition. Since $\bar{y}$ is constant and $(1-\tau)>0$, the problem reduces to with variable $x\in{\mbox{\bf R}}^{n}$. Introducing an epigraph variable $t$ for the CVaR term gives

### CVQP form

We introduce an auxiliary variable $s$ with the constraint $s=1$, and define $\tilde{x}=(x,t,s)\in{\mbox{\bf R}}^{n+2}$. The CVQP parameters, with CVaR level $\beta=\tau$, are

### Problem instances

We generate features $u_{i}\in{\mbox{\bf R}}^{n}$ with independent standard normal entries, a vector with entries $\beta_{j}\sim\mathcal{N}(0,1/(1+j))$, and responses $y_{i}=u_{i}^{T}\beta+\epsilon_{i}$, where $\epsilon_{i}$ follows a $t$-distribution with 5 degrees of freedom scaled by $0.1$. We use quantile level $\tau=0.9$.

### Results

Figure 3 shows solve times versus number of scenarios $m$ for quantile regression problems with $n=500$ features, averaged over 3 random instances. Our method is faster than both Mosek and Clarabel across all tested sizes, by a factor ranging from about 5 to over 100. Mosek does not solve instances with $m>10^{6}$ within the time limit, and Clarabel does not solve instances with $m\geq 3\times 10^{5}$. Our method scales to $m=10^{7}$ scenarios.

Figure 3: Quantile regression solve times, with n = 500 features.

## Extensions and variations

Our method extends to more general problems and admits several practical variations.

### More general constraints on $\tilde{z}$

When projection onto a set $\mathcal{C}$ is efficient (via a closed-form solution or a fast algorithm), we can directly handle constraints of the form $\tilde{z}\in\mathcal{C}$ in place of the box constraints $l\leq\tilde{z}\leq u$.

### Extensions to the $x$-update

The method extends to additional constraints on $x$ or nonquadratic objective functions. The $x$-update then becomes where $f$ is any convex function (not just quadratic), $G\in{\mbox{\bf R}}^{p^{\prime}\times n}$, and $\mathcal{D}\subseteq{\mbox{\bf R}}^{p^{\prime}}$ is a convex set. Using a standard solver with warm-starting, the per-iteration cost remains manageable, though typically higher than solving the original linear system.

### Equilibration

Equilibration as a preprocessing step often improves ADMM convergence, particularly for problems with poorly scaled data.

### Warm starting

Two effective strategies for choosing the initial point are solving with a reduced set of scenarios and using that solution to initialize the full problem, and using a quadratic approximation of the CVaR constraint to compute an initial point. Similarly, the sorting step in the CVaR projection can be warm-started using the sorted order from the previous ADMM iteration. Since the projection input changes only slightly between iterations, the sorted order is nearly preserved, and an adaptive sorting algorithm can exploit this to reduce the per-iteration cost in practice.
