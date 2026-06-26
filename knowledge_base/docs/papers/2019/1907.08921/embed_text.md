## Introduction

Linear-quadratic-regulator (LQR) has been one of the cornerstones of control theory since Kalman's original work in the 1960s. LQR is formulated around an optimization problem for determining a sequence of (control) inputs to a linear system in order to minimize a given (integral) quadratic cost over an infinite horizon.^11^1We shall not delve into the finite-horizon LQR in this paper. From the theoretical point of view, a fundamental property of LQR synthesis is that the resulting optimal input is in the form of a state feedback; as such, it can be represented as a constant feedback gain on the state of the system. The state feedback gain that "solves" the infinite-horizon LQR problem, in turn, can be obtained by solving the algebraic Riccati equation (ARE). That is, in the traditional approach to LQR design, the state feedback gain is revealed after obtaining the "certificate" or "cost-to-go" for the underlying optimal control problem.^22^2The analogy here would be solving the dual, followed by the recovery of the primal solution. Historically, a large number of works have studied the solution of ARE, including approaches based on iterative algorithms, algebraic solution methods, and semidefinite programming.

Although the cost function plays a fundamental role in the LQR problem, it is generally not "recommended" to directly compute the optimal gain (policy) using this cost function without solving the associated Riccati equation. This approach, in the meantime, is in sharp contrast to how one would typically go about minimizing a cost function over the variable of interest in introductory optimization, say, through gradient descent.^33^3This is essentially due to the dynamic nature of the constraint set. With recent advances in sophisticated statistical and optimization methods, there has been a surge of interest in constructing optimal control strategies directly, viewing control synthesis through the lens of first order methods.^44^4One might as well extrapolate that these methods provide a streamline recipe for learning optimal feedback gains in real-time. Adopting such a point of view has been partially inspired by the application of learning algorithms, such as Reinforcement Learning (RL), where using principles of Dynamic Programming (DP), one can devise real-time model-free methods for both continuous-time and discrete-time LQR. Learning (over time) also has a spatial counterpart, realized in terms of control of distributed systems. Such systems have become increasingly important in recent years; as such, it is desired to design feedback mechanisms that conform to a given sparsity pattern mirroring the underlying interaction topology amongst the various subsystems. That is, each "node" in the network forms its control action by employing local information collected from its neighbors; the corresponding zero pattern in the feedback gain mirrors this locality in the information exchange. Such design problems have gained a lot of attention in the system and control community over the past two decades. However, there remains a host of issues in further understanding such class of problems. For example, in the case of structured synthesis, even the existence of an optimal structured LQR gain is nontrivial to assert. A rather brief sampling of related works on the structured synthesis problem is as follows.^55^5With apologies for not going over a large body of work in this area. In, a combined primal-dual method with a penalty function is employed to obtain a feedback controller with the desired zero pattern. The work proposes a relaxed mixed-integer semidefinite-programming in which the graph topology is enforced through the integer constraints. Directly related to the present work is, where the authors propose a projected gradient descent algorithm for structured synthesis.

In this paper, inspired by the work, we examine first order methods for solving the centralized and distributed LQR problem. In this direction, we first "tweak" the LQR problem formulation, motivated by the well-known fact that the state-feedback law is independent of the initial state of the system. In order to eliminate the dependence on this initial state, we adopt a cost function that sums the traditional LQR cost over a set of linearly independent initial states. This cost function can then be viewed as a well-defined matrix function over stabilizing feedback gains. We argue that this formulation (see §3.2 for details) is necessary for the adoption of first order methods for LQR-type problems. More importantly, in this setting, we show that the cost is smooth, coercive and gradient dominated over its effective domain.^66^6The property was first observed ; in this paper, we provide an alternate proof of this fact. We then proceed to show that the LQR cost over the set of stabilizing state feedback gains does attain a minimum, by showing that all its sub-level sets are compact. Subsequently, using the topological and metrical properties of the set of (static) stabilizing feedback gains, one can conclude that the proposed optimization formulation of LQR synthesis does attain its global minimum. This cost function also gives rise to three types of well-posed flows over the set of stabilizing controllers, namely, gradient flow, natural gradient flow and the quasi-Newton flow. In this direction, we prove that the Lyapunov functionals for these flows decay at an exponential rate and the corresponding trajectories are exponentially stable in the sense of Lyapunov.

We then proceed to discuss the forward Euler discretization of these flows, realized as gradient descent, natural gradient descent and the quasi-Newton iteration (hence, the state feedback gain can be updated iteratively). The problem of solving the LQR using direct gain (policy) update has been addressed , where it is shown that first-order gradient descent in fact converges to the optimal feedback gain.^77^7To be more precise, the work establishes the convergence of cost function; as such, the convergence of iterates, i.e., feedback gains, is not shown explicitly. This setup was also considered , without a convergence analysis. In, the gradient dominated property, is used to guarantee the global convergence of gradient descent and natural gradient descent. The discretization scheme obtained in the present work is consistent with the setup adopted , but in some ways, approaches the problem more directly and indeed, provides a practical choice of stepsize for gradient descent and improves the choice of stepsize for natural gradient descent and quasi-Newton iteraton.^88^8Our approach primary aims to mold the LQR synthesis problem in the spirit of. We show that the stepsizes in the gradient descent natural gradient descent can be obtained via the Lyapunov equations in two consecutive updates; the coerciveness of the cost function on the other hand, ensures that the updated feedback gains remain stabilizing. As such, both the function values and feedback gains converge linearly to the corresponding global minimum. In view of these observations, one can then state that the proposed iterations generate a sequence of stabilizing feedback gains that converge linearly to the optimal LQR gain. Particularly in the case of natural gradient descent we obtain a sequence of value matrices that is monotonically decreasing on the positive semidefinite cone.^99^9The terminology "natural gradient descent" (flow) is reserved for a particular choice of Riemannian metric; see §5 for details. Convergence rate of the quasi-Newton iteration is also analyzed,^1010^10The quasi-Newton iteration is consistent with Hewer's algorithm, essentially a Newton's iteration. However, traditionally, the emphasis has been placed on the convergence of the value matrices, rather than direct policy update. We provide a more transparent motivation as to why the proposed algorithm is a "quasi-Newton" iteration over direct policy space. proving that the corresponding iterates and function values converge quadratically to the global optima.^1111^11The algorithm is referred to as "Gauss-Newton" in and the convergence was only shown to be linear rather than $Q$-quadratic.

Our work also considers the extension of the proposed synthesis framework to the problem of designing feedback gains with an arbitrary sparsity pattern. This setup is inspired by the scheme adopted . In this direction, we propose a formalism to set up the problem where projected gradient descent has a simple realization. In the case of structured synthesis, the LQR cost function is no longer "gradient dominated" and the choice of stepsize can not be generalized from the unstructured case. On the other hand, the proposed stepsize choice in assumes a rather involved analytical form and convergence analysis to first-order stationary point is not straightforward.^1212^12The stepsize sequence described in is asymptotically vanishing. As such, the convergence is only guaranteed if the sequence is square summable but not absolutely summable. However, these conditions were not verified . Furthermore, , it has been stated that the proposed algorithm will converge to a local minimum. This is not necessary valid as gradient descent for nonconvex objectives can in principle only converge to a first-order stationary point. One might invoke an "escaping saddle" type argument here but this requires more work. In this work, we adapt the machinery developed for the unstructured LQR for the structured synthesis: we first define the initial state independent LQR formulation and then show that the cost function can be equivalently defined as the unstructured LQR cost function restricted to the linear space defined by the information-exchange graph; as such, the cost function is smooth in the subspace topology and has a coercive property. Using this setup, we can obtain the gradient and Hessian of the cost function, leading to a natural choice of stepsize by bounding the Hessian over the initial sublevel set. We show this stepsize will guarantee a nonasymptotic sublinear convergence rate to the first-order stationary point.

The remainder of this paper is as follows. The LQR problem statement and related definitions are provided in §3. The averaged LQR cost over a set of linearly independent initial states is also defined in §3. §3.4 introduces the analytical properties of the LQR cost function.. Subsequently, gradient flow, natural (Riemannian) gradient flow and quasi-Newton flow are introduced in §4, §5 and §6, respectively. Discrete realizations of these flows, namely, gradient descent, natural gradient descent and quasi-Newton iterations are addressed in §4.1, §5.1 and §6.1. §7 introduces the formalism for setting up a first order approach for structured LQR synthesis, supplemented with the stepsize selection analysis and sublinear convergence to the first-order stationary point. §8 presents simulation results to illustrate the theoretical contributions of the paper; in §9, we provide a few concluding remarks.

## Notation and Preliminaries

We denote by ${\mathbb{M}}_{n \times m}{({\mathbb{R}})}$ the set of $n \times m$ real matrices and ${\mathbb{G}}{\mathbb{L}}_{n}{({\mathbb{R}})}$ as the set of invertible square matrices; ${\mathbb{R}}^{n}$ denotes the $n$-dimensional real Euclidean space with the $n = 1$ case identified with real number. The set of non-negative numbers is denoted by ${\mathbb{R}}_{+}$ and natural numbers as $\mathbb{N}$; ${\mathbb{S}}_{n}$ denotes the set of $n \times n$ real symmetric matrices. Other notation includes $A^{\top}$, $\rho{(A)}$, $\text{rank}{(A)}$, $\operatorname{\mathbf{T}\mathbf{r}}{(A)}$, $\text{vec}{(A)}$ representing the transpose, spectral radius, rank, trace, and vectorization of the matrix $A$, respectively; $A \otimes B$ is the Kronecker product of matrices $A$ and $B$, and $\text{rbd~}\mathcal{K}$ designates the relative boundary of the set $\mathcal{K}$. The real inner product between a pair of vectors $x$ and $y$ is denoted by $\langle x,y\rangle$. ${\| A\|}_{2}$ denotes the spectral (operator) norm of a square matrix $A$ and ${\| A\|}_{F}$ denotes its Frobenius norm.^1313^132-norm is assumed when we use $\parallel. \parallel$. Lastly, the notation $A \succeq B$ for two symmetric matrices refers to the positive semi-definiteness of their difference $A - B$; analogously for positive definiteness of this difference using $A \succ B$. We let $\lambda_{i}{(A)}$ denote the eigenvalues of a square matrix $A$. These eigenvalues are indexed in an increasing order with respect to their real parts, i.e., If $A$ is symmetic, the ordering becomes ${\lambda_{1}{(A)}} \leq \cdots \leq {\lambda_{n}{(A)}}$. When $A \succeq 0$, ${\| A\|} = {\lambda_{n}{(A)}}$ and we shall use these interchangeably. We use $C^{\omega}{(U)}$ to denote the set of real analytic functions over an open set $U \subseteq {\mathbb{R}}^{n}$. A function $f:U\rightarrow{\mathbb{R}}$ is $C^{\infty}$-smooth if it is infinitely differentiable. A function $f$ is $L$-smooth when $f$ is *continuously differentiable* and its gradient is $L$-Lipschitz, i.e., ${\|{{{\nabla f}{(x)}} - {{\nabla f}{(y)}}}\|} \leq {L{\|{x - y}\|}}$. A pair $(A,B)$ with $A \in {{\mathbb{M}}_{n \times n}{({\mathbb{R}})}}$ and $B \in {{\mathbb{M}}_{n \times m}{({\mathbb{R}})}}$ is called controllable if the Kalman rank condition, is satisfied. Given such system matrices, $\mathcal{S}$ denotes the set of Schur stabilizing feedback gains, We will frequently use several linear algebraic facts on matrix equations; some of these are collected in the following proposition.

### Proposition 2.1

The following relations hold: For matrices $A,B,C$ of appropriate dimensions, ${\text{vec}{({ABC})}} = {{({C^{\top} \otimes A})}\text{vec}{(B)}}$. where ${M,N} \in {{\mathbb{M}}_{n \times m}{({\mathbb{R}})}}$ with $m \leq n$ and $a \in {\mathbb{R}}_{+}$.

Suppose that $A \in {{\mathbb{M}}_{n \times n}{({\mathbb{R}})}}$ has spectral radius bounded by $1$, i.e., ${\rho{(A)}} < 1$. Then has a unique solution, and when $Q \succ 0$ then $X \succ 0$. Moreover, if $\overset{\sim}{X}$ satisfies with $\overset{\sim}{Q} \preceq Q$, then $\overset{\sim}{X} \preceq X$.

If $X,Y$ are both positive definite, then The proofs of these observations can be found.

## Problem Setup and its Analytic Properties

In this section, we provide an overview of LQR, and in particular its modified initial state independent version, as well as a few analytic observations that are of independent interest. Although the reader might know of the extensive LQR literature, we note that some of these observations have only become necessary when the LQR optimization is viewed directly on the set of stabilizing feedback gains.

### Discrete-time LQR

In the standard setup of LQR, we consider a (discrete-time) linear time invariant model of the form, where $A \in {{\mathbb{M}}_{n \times n}{({\mathbb{R}})}}$ and $B \in {{\mathbb{M}}_{n \times m}{({\mathbb{R}})}}$. The LQR problem is the optimization problem of devising a linear feedback gain $K \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$ for which $u_{k} = {- {Kx_{k}}}$, minimizing,^1414^14The condition that $u_{k}$ has the form $- {Kx_{k}}$ is not set a priori in the LQR formulation; this feedback form is typically shown via the adoption of a dynamic programming step. where $x_{0}$ is the initial condition, and the quadratic cost is parameterized by ${0 \preceq Q \in {\mathbb{S}}_{n}},$ and $0 \prec R \in {\mathbb{S}}_{m}$. LQR is traditionally solved via dynamic programming or calculus of variations, leading to the celebrated Algebraic Riccati Equation (ARE).^1515^15For the dynamic programming case, one starts with the finite horizon case, apply the optimality principle, and then identify a solution concept for the infinite horizon case using a limit argument; calculus of variations provide another approach for deriving necessary conditions for LQ-type problems.

### Cost function for direct policy update

In order to update the feedback gain (policy) directly, it will be conceptually appealing to consider the cost as a matrix function over the set of feedback gains. With this aim in mind, we may define $J_{x_{0}}:{{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}\rightarrow{\mathbb{R}}}$ as, for some fixed initial condition $x_{0} \in {\mathbb{R}}^{n}$. Our first task in this direct optimization setup is to determine the domain over which the function is well-defined. In other words, we are interested in the effective domain ${\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}} = {\{{K \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}:{J_{x_{0}}{(K)}} < {+ \infty}}\}}$. Addressing this seemingly natural analytical question turns out to be subtle. If $K$ is stabilizing, i.e., ${\rho{({A - {BK}})}} < 1$, then $K \in {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}}$. In the meantime, for a non-stabilizing $K$, i.e., ${\rho{({A - {BK}})}} \geq 1$, when the system matrix $A - {BK}$ has both stable and unstable modes, if $x_{0}$ is chosen to be in the span of eigenspace corresponding to stable modes, ${J_{x_{0}}{(K)}} < \infty$. That is, $\{{K:{\rho{({A - {BK}})}} < 1}\}$ is a proper subset of $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}$. Indeed, $\{{K:{\rho{({A - {BK}})}} < 1}\}$ is the interior of $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}$. Before proving this, we show that the set of feedback gains for which a fixed vector $x$ is not orthogonal to any eigenvector of the closed-loop system is dense.

### Proposition 3.1

Suppose that $(A,B)$ is controllable and $x \in {\mathbb{R}}^{n}$ is a fixed vector. Then the set, is dense in ${\mathbb{M}}_{m \times n}{({\mathbb{R}})}$.

### Proof

Without loss of generality, we may assume that $x = {(0,\ldots,0,1)}^{\top} \in {\mathbb{R}}^{n}$. We note that, and if $K \in \mathcal{W}^{c}$, then the first $n - 1$ columns of ${\lambdaI} - {({A - {BK}})}$ has rank smaller than $n - 1$ since the non-trivial kernel of the first $n - 1$ columns of ${\lambdaI} - {({A - {BK}})}$ appending $0$ would be an eigenvector orthogonal to $x$. But this condition is equivalent to vanishing all ${({n - 1})} \times {({n - 1})}$ minors of the first $n - 1$ columns of ${\lambdaI} - {({A - {BK}})}$. Each of these minors is a polynomial $p_{j}{(t,K,\lambda)}$ in the entries of $K$ and $\lambda$. Denote $E_{j} = {\{{{(K,\lambda)} \in {{{\mathbb{M}}_{n \times n}{({\mathbb{R}})}} \times {\mathbb{C}}}:{p_{j}{(t,K,\lambda)}} = 0}\}}$. Each set $E_{j}$ is closed in Zariski topology; as such, $\bigcap E_{j}$ is Zariski closed in ${{\mathbb{M}}_{m \times n}{({\mathbb{R}})}} \times {\mathbb{P}}^{1}$, where ${\mathbb{P}}^{1}$ the projective variety. But $\mathcal{W}^{c}$ is precisely the projection of $\bigcap E_{j}$ onto ${missing}M_{n \times n}{({\mathbb{R}})}$. Since this projection is a closed map (in the Zariski topology), $\mathcal{W}^{c}$ is Zariski closed. Consequently as an nonempty set, $\mathcal{W}$ is Zariski open and thus dense. ∎ We are now in the position to prove a result concerning the interior of $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}$.

### Lemma 3.2

Suppose that $x_{0} \in {\mathbb{R}}^{n}$ is fixed. If $J_{x_{0}}$ is defined , then the set of Schur stabilizing feedback gains $\mathcal{S}$ is the interior of $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}$.

### Proof

Clearly $\mathcal{S} \subseteq {\text{int}{({\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}})}}$. On the other hand, let $M \in {{\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}} \smallsetminus \mathcal{S}}$ and every $\varepsilon > 0$, by Proposition 3.1, there is some $N \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$ such that ${\|{M - N}\|}_{F} < \varepsilon$ and the projection of $x_{0}$ onto every eigenvector of $A - {BN}$ is nontrivial. We observe that ${\|{A - {BM} - {({A - {BN}})}}\|}_{F} \leq {{\| B\|}_{F}{\|{M - N}\|}_{F}}$. Since spectral radius is continuous and ${\rho{({A - {BM}})}} \geq 1$, ${\rho{({A - {BN}})}} \geq 1$. As such, ${J_{x_{0}}{(N)}} = \infty$ and $N \notin {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}}$. Hence, $M \notin {\text{int}{({\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}})}}$ and ${\text{int}{({\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}})}} = \mathcal{S}$. ∎ The above lemma implies that $J_{x_{0}}{(K)}$ is not differentiable everywhere on its domain. More precisely, $J_{x_{0}}{(K)}$ is differentiable on $\mathcal{S}$ but non-differentiable on ${\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}} \smallsetminus \mathcal{S}$. This complication is rather unnecessary as we are primarily interested in stabilizing controllers. This motivates us to examine initial condition independent formulation of LQR.^1616^16This is indeed necessary if we want to formulate an unconstrained optimization problem over the set of stabilizing feedback gains.

### Initial condition independent formulation of LQR

Ideally, the objective function $f:{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}\rightarrow{\mathbb{R}}$ for our LQR calculus has an effective domain that coincides with the set of stabilizing feedback gains $\{{K \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}:{\rho{({A - {BK}})}} < 1}\}$. This can be achieved by choosing a set of linearly independent vectors ${\{ x_{0}^{1},\ldots,x_{0}^{n}\}} \subseteq {\mathbb{R}}^{n}$ and defining,^1717^17Of course, one may choose the standard basis $\{ e_{1},\ldots,e_{n}\}$, where $e_{i}$ is the vector with zero entries except a "1" at the $i$th entry; the choice of an arbitrary basis simply retains flexibility.

As such, the function $f$ would be infinite if $K$ is not stabilizing (see Lemma 3.7 for details).

### Remark 3.3

The initial independent formulation is rather natural for general optimal control problems. In such problems, it is often desired to constrain the control synthesis to stabilizing feedback gains. For a learning algorithm that is built around a descent direction, such a formulation allows for an automatic enforcement of this stabilizing feature.

We shall now see that $f$ enjoys several favorable properties, e.g., $f$ is differentiable over its effective domain and $f$ diverges to infinity when $K$ tends to the boundary of this domain, i.e., $f$ is coercive. More importantly, for every $K \in {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(f)}}$, the function $f{(K)}$ can be written as, where $\mathbf{\Sigma}^{j} = {x_{0}^{j}{(x_{0}^{j})}^{\top}}$ and $X$ satisfies the Lyapunov equation, Note that $J_{x_{0}^{j}}{(K)}$ does not necessarily admit the compact form ${J_{x_{0}^{j}}{(K)}} = {\operatorname{\mathbf{T}\mathbf{r}}{({X\mathbf{\Sigma}^{j}})}}$ for every $K \in {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{({J_{x_{0}^{j}}{(K)}})}}$. This is due to the fact that matrix $X$ only makes (mathematical) sense if $K$ is stabilizing, but $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{({J_{x_{0}^{j}}{(K)}})}$ contains non-stabilizing feedback gains; see 3.2.

### Remark 3.4

Alternatively, we could let $x_{0} \sim \mathcal{D}$, where $\mathcal{D}$ denotes some probability distribution, and let As long as the samples span the whole space with probability $1$, the function enjoys same properties as we have defined above. This is indeed the formulation adopted, without discussing its implications on differentiablility and coerciveness of $$.

### Analytical Properties of the LQR cost function

In this section, we investigate the properties of the LQR cost. We will observe that, $f$ is a real analytic function over its domain. $f$ is coercive and has compact sublevel sets.

The Hessian $\nabla^{2}f$ is characterized.

To simplify the notation, in the rest of this paper, we shall denote^1818^18On some occations, we use subscript $M_{K}$ to emphasize the dependence on feedback gain $K$.

Let us recall some of the topological properties of the set of Schur stabilizing feedback gains $\mathcal{S}$; the proofs can be found .

### Lemma 3.5

The set $\mathcal{S}$ is regular open, contractible, and unbounded when $m \geq 2$ and the boundary $\partial\mathcal{S}$ is precisely the set $\mathcal{B} = {\{{K \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}:{\rho{({A - {BK}})}} = 1}\}}$.

We now observe that $f{(K)}$ is real analytic over $\mathcal{S}$.

### Lemma 3.6

For the LQR cost $$, we have $f \in {C^{\omega}{(\mathcal{S})}}$.

### Proof

For every $K \in \mathcal{S}$, let $X$ be the solution to the Lyapunov equation, Since the eigenvalues of ${I \otimes I} - {A_{K} \otimes A_{K}}$ are $\{{{{1 - {\lambda_{i}{(A_{K})}\lambda_{j}{(A_{K})}}}:i},{j = {1,\ldots,n}}}\}$, ${I \otimes I} - {A_{K}^{\top} \otimes A_{K}^{\top}}$ is invertible. Hence, By Cramer's rule, $X{(K)}$ is a rational function of polynomials in the entries of $K$ and thus the map $K\mapsto{X{(K)}}$ is $C^{\omega}$.^1919^19For a given $K$, $X{(K)}$ will be referred to as the the "cost matrix" as it characterizes the infinite horizon closed loop cost from the current state when this cost is finite. We shall use $X{(K)}$ and $X$ interchangebly. Hence, $f$ can be viewed in terms of the composition,^2020^20Mind that this perspective is only valid in $\mathcal{S}$.

As a composition of $C^{\omega}$ maps, $f$ is thus real analytic.

With the initial condition independent formulation, the function $f$ diverges to infinity smoothly as $K$ approaches the boundary $\partial\mathcal{S}$ or when $K$ diverges to infinity.

### Lemma 3.7

The LQR cost is coercive in the sense that,

### Proof

Suppose that the sequence ${\{ K_{j}\}} \subseteq \mathcal{S}$ and $K_{j}\rightarrow K \in {\partial\mathcal{S}}$. By continuity of the spectral radius, we have ${\rho{({A - {BK_{j}}})}}\rightarrow{\rho{({A - {BK}})}}$. This means that for every $\varepsilon > 0$, there exists some $N = {N{(\varepsilon)}} \in {\mathbb{N}}$ for which ${|{{\rho{({A - {BK_{j}}})}} - {\rho{({A - {BK}})}}}|} < \varepsilon$ for every $j \geq N$. That is $1 > {\rho{({A - {BK_{j}}})}} > {1 - \varepsilon}$ for all $j \geq N$. Let $X$ be the cost matrix associated with $K_{j}$. We observe that, Note that ${\operatorname{\mathbf{T}\mathbf{r}}{({{(A_{K_{j}}^{\top})}^{i}{(A_{K_{j}})}^{i}})}} \geq {\rho{(A_{K_{j}})}^{2i}}$ since, It thus follows that, For any $M > 0$, picking a sufficiently small $\varepsilon$ would lead to ${f{(K_{j})}} \geq M$ for all $j \geq {N{(\varepsilon)}}$.

On the other hand, Thereby, for any $M > 0$, ${f{(K)}} \geq M$ for $\| K\|$ sufficiently large. ∎ With the coercive property in place, i.e., growth to infinity smoothly, we can continuously extend the function to ${\mathbb{M}}_{n \times n}{({\mathbb{R}})}$ as an extended real-valued function which allows $+ \infty$ as a function value. This in turn will imply that all sublevel sets of $f{(K)}$ are compact.^2121^21This can also be proved directly. The condition ${f{(K)}}\rightarrow{+ \infty}$ as ${\| K\|}\rightarrow\infty$ implies that the sublevel sets if $f$ are bounded; condition ${f{(K_{j})}}\rightarrow{+ \infty}$ as $K_{j}\rightarrow K \in {\partial\mathcal{S}}$ implies that every sublevel set is bounded away from the boundary and hence closed in the Euclidean topology. Note the continuity of $f$ only guarantees that the sublevel set is closed in $\mathcal{S}$.

### Corollary 3.7.1

The sublevel set $\mathcal{S}_{\alpha} = {\{{K \in \mathcal{S}:{f{(K)}} \leq \alpha}\}}$ is compact for every $\alpha > 0$.

### Proof

By Lemma 3.7, we can continuously extend $f$ to $\overset{\sim}{f}:{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}$, where, The sublevel sets ${\overset{\sim}{\mathcal{S}}}_{\alpha} = {\{{K \in {{\mathbb{M}}_{n \times n}{({\mathbb{R}})}}:{\overset{\sim}{f}{(K)}} \leq \alpha}\}}$ of $\overset{\sim}{f}$, in the meantime, are compact by Proposition $11.12$. The proof is completed by observing that $\mathcal{S}_{\alpha} = {\overset{\sim}{\mathcal{S}}}_{\alpha}$ when $\alpha$ is finite. ∎ As $f \in {C^{\omega}{(\mathcal{S})}}$, the gradient of $f$ can be characterized explicitly.

### Proposition 3.8

(Proposition $1$ in) For $K \in \mathcal{S}$, ${{\nabla f}{(K)}} = {2\left({{RK} - {B^{\top}X{({A - {BK}})}}} \right)Y}$, where $Y$ solves the Lyapunov matrix equation, We emphasize that Proposition 3.8 only makes sense when $K \in \mathcal{S}$.^2222^22This point has not been discussed. Indeed, it does not even make sense to have $X$ and $Y$ if $K$ is not stabilizing. One is then tempted to set ${{\nabla f}{(K)}} = 0$ to obtain a stationary point. However, since $X$ is a function of $K$, whether or not ${{\nabla f}{(K)}} = 0$ is solvable in $\mathcal{S}$ needs clarification.

### Lemma 3.9

The matrix $K_{\ast} = {{({{B^{\top}X_{\ast}B} + R})}^{- 1}B^{\top}X_{\ast}A}$ is the unique global minimizer of $f{(K)}$^2323^23As we are establishing the global minimizer is unique, throughout the paper we shall use $K_{\ast}$ to denote the global minimizer., where $X_{\ast}$ is the corresponding solution of the Lyapunov equation.^2424^24Here we are not assuming prior knowledge of control theory. Of course, control experts and students alike may readily identify that the solution is indeed the optimal LQR gain via the ARE.

### Proof

Since $(A,B)$ is controllable, $\mathcal{S}$ is nonempty. As such, for some finite $c > 0$, the set $\mathcal{S}_{c} = {\{{K \in \mathcal{S}:{f{(K)}} \leq c}\}}$ is a nonempty compact set. Therefore, $f{(K)}$ achieves its minimum on $\mathcal{S}_{c}$. Note that as $f{(K)}$ is not constant, this minimum must be in the interior of $\mathcal{S}_{c}$ and as such, ${{\nabla f}{(K_{\ast})}} = 0$. Thereby, $K_{\ast} = {{({{B^{\top}X_{\ast}B} + R})}^{- 1}B^{\top}X_{\ast}A}$ must be in $\mathcal{S}$ (this expression is now more precise!). Since $f$ has only stationary point, $K_{\ast}$ must be the global minimum. ∎ Next we derive a formula for the Hessian of $f{(K)}$. The upper bound on the norm of this Hessian will then suggest a viable choice of stepsize for (projected) gradient descent.

### Proposition 3.10

For $K \in \mathcal{S}$, the (self-adjoint) Hessian of the LQR cost $f$ is characterized, where $E \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$ and $X'{(K)}{\lbrack E\rbrack}$ denotes the action of differential of the map $K\mapsto{X{(K)}}$^2525^25To be more precise, the differential of $X:{M_{m \times n}{({\mathbb{R}})}}\rightarrow{M_{n}{({\mathbb{R}})}}$ is a map $X':{M_{m \times n}{({\mathbb{R}})}}\rightarrow{\mathcal{L}{(M_{m \times n},{\mathcal{L}{({M_{m \times n}{({\mathbb{R}})}},{M_{n}{({\mathbb{R}})}})}})}}$, where $\mathcal{L}$ denotes the set of bounded linear maps. As such, ${X'{(K)}} \in {\mathcal{L}{({M_{m \times n}{({\mathbb{R}})}},{M_{n}{({\mathbb{R}})}})}}$ and ${X'{(K)}{\lbrack E\rbrack}} \in {M_{n}{({\mathbb{R}})}}$.^2626^26Recall that $X$ solves the Lyapunov equation and $Y$ solves Lyapunov matrix equation..

### Proof

We note that ${{\nabla f}{(K)}}:{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}\rightarrow{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$. Let ${g{(K)}} = {{\nabla f}{(K)}} = {P{(K)}Y{(K)}}$, where ${P{(K)}} ≔ {2M} = {2{({{RK} - {B^{\top}XA_{K}}})}}$. By Lebnitz' rule, Note that for $E \in {M_{m \times n}{({\mathbb{R}})}}$, the action of ${\nabla g}{(K)}{\lbrack E\rbrack}$ is given,^2727^27Throughout this paper, we use the notation ${\nabla F}{(K)}{\lbrack E\rbrack}$ to denote the action on $E$ of the differential $\nabla F$ evaluated at $K$, i.e., ${\nabla F}{(K)}$. where $P'{(K)}{\lbrack E\rbrack}$ and $Y'{(K)}{\lbrack E\rbrack}$ denote the usual matrix multiplication. Hence, where $X'{(K)}{\lbrack E\rbrack}$ satisfies, Note that $X'{(K)}{\lbrack E\rbrack}$ and $Y'{(K)}{\lbrack E\rbrack}$ are uniquely defined if $K \in \mathcal{S}$ and can be written as, Using the cyclic property of the matrix trace, we observe that, The action of the Hessian can hence be simplified as, We note that as ${\nabla^{2}f}{(K)}$ is self-adjoint, its operator norm can be characterized as,

### Remark 3.11

We note that at $K_{\ast}$, for every $E \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$, the action of Hessian is positive: namely, ${\nabla^{2}f}{(K)}$ is positive definite. This validates that $K_{\ast}$ is a local minimizer--and thus--the global minimizer, as $K_{\ast}$ is the unique stationary point.

We now observe that the LQR cost is a *gradient dominated* function.^2828^28This property is also referred as Polyak-Łojasiewicz condition, as a special case of what had been proposed . The proof of this property in (Corollary 5) is based on a careful comparison of the cost difference in each time step between the optimal policy and a specified policy. Here, we provide an alternate proof of this important property. This alternate approach is more control-theoretic in the sense that it is mainly concerned with the properties of the Lyapunov equation. Moreover, this approach allows determining an upper bound on the gradient dominance coefficient--that in turn--facilitates estimating the iteration compexity of the gradient descent algorithm to reach an $\varepsilon$-precision solution for LQR.

### Lemma 3.12

Let $K_{\ast}$ be the optimal feedback gain. For $K \in \mathcal{S}$, where $Y_{\ast} = {\sum_{j = 0}^{\infty}{{(A_{K_{\ast}})}^{j}\mathbf{\Sigma}{(A_{K_{\ast}}^{\top})}^{j}}}$ and $X_{\ast}$ solves the Lyapunov matrix equation

### Proof

Recall that $M ≔ {{RK} - {BXA_{K}}}$ and $X$ is the solution of. Taking the difference of equations and, i.e., ${} - {}$, we obtain, A few algebraic manipulations now yield, By Proposition 2.1 (part), we note that for every $\alpha > 0$, Picking $\alpha = 1/{(\lambda_{1}{(R + B^{\top}X_{\ast}B)}}$, we then have, Let $Z$ be the solution of the Lyapunov equation, by Proposition 2.1 (part (c)), ${X - X_{\ast}} \preceq Z$ and It thus follows that, where in the last equality we have used the cyclic property of the matrix trace. We note that $Y_{\ast} = {\sum_{j = 0}^{\infty}{{(A_{K_{\ast}})}^{j}\mathbf{\Sigma}{(A_{K_{\ast}}^{\top})}^{j}}}$ is uniquely determined by the system parameters $A,B,Q,R,\mathbf{\Sigma}$. Now where the last inequality follows from Proposition 2.1 (part (d)). It remains to lower bound $\lambda_{1}{(Y)}$ but this is straightforward since, We now provide an estimate of the gradient dominance coefficient, This coefficient determines the linear convergence rate of gradient descent for LQR.

### Proposition 3.13

Over the sublevel set $S_{f{(K_{0})}}$,

### Proof

Essentially, we only need to estimate $\| Y_{\ast}\|$; we shall estimate $\operatorname{\mathbf{T}\mathbf{r}}{(Y_{\ast})}$ instead. We first observe that, Putting $Z = {\sum_{j = 0}^{\infty}{{(A_{K_{\ast}}^{\top})}^{j}{(A_{K_{\ast}})}^{j}}}$, we note that $Z$ solves the Lyapunov equation, Since $I \preceq {{Q/\lambda_{1}}{(Q)}}$, it follows by Proposition 2.1 that $Z \preceq X_{\ast}$, where $X_{\ast}$ solves the Lyapunov equation. Hence,

## Gradient Flow on $\mathcal{S}$

In this section, we show that the LQR cost function gives rise to a well-posed gradient flow, Let us first observe that admits a unique solution for all time $t$.

### Lemma 4.1

For every $K_{0} \in \mathcal{S}$ and $t_{0} \in {\mathbb{R}}$, there exists a unique solution $K_{t} \in {C^{\infty}{({\mathbb{R}},\mathcal{S})}}$ for the initial value problem,

### Proof

Note that $K\mapsto{2\left({{RK} - {B^{\top}X{({A - {BK}})}}} \right)Y}$ is $C^{\infty}$ smooth. The statement now follows from Corollary 3.7.1 and Proposition $3.7$. ∎ We next show that the unique trajectory of is in fact exponentially stable; without loss of generality, we assume that $t_{0} = 0$.

### Theorem 4.2

For $K_{0} \in \mathcal{S}$, denote by $K_{t}$ as the solution of. Then the trajectory $K_{t}$ is globally exponentially stable in the sense of Lyapunov, i.e., where ${\alpha,c} \in {\mathbb{R}}_{+}$ are constants determined by the LQR parameters $A,B,Q,R$ and initial condition $K_{0}$.

To prove this result, we first observe that the Lyapunov functional ${V{(K_{t})}} ≔ {{f{(K_{t})}} - {f{(K_{\ast})}}}$ converges exponentially to the origin.

### Lemma 4.3

For $K_{0} \in \mathcal{S}$, denote by $K_{t}$ as the solution of. Then where $\alpha \in {\mathbb{R}}_{+}$ is constant determined by system parameters $A,B,Q,R$ and $K_{0}$.

### Proof

recall we have proved in Lemma 3.12, It then suffices to observe We are now ready to prove Theorem 4.2.

### Proof

Observe that the Lyapunov functional is smooth, positive definite and radially unbounded;^2929^29In control literature, this is sometimes referred to as weakly coercive; nevertheless, as shown here, this is equivalent to being coercive. thus $K_{t}$ is globally asymptotic stable, i.e., for every $\beta > 0$ and thus, since ${X_{t} - X_{\ast}} \succeq 0$. Moreover since ${\lambda_{1}{(Y)}} \geq 1$, Picking ${2\lambda_{1}{(R)}} > {1/\beta}$, we have It now follows that, Integrating both sides of, Putting $c = {{c'{({{f{(K_{0})}} - {f{(K_{\ast})}}})}}/{({\|{K_{0} - K_{\ast}}\|}_{F}^{2})}}$ now completes the proof. ∎

### Discretization of Gradient Flow

In this section, we examine the discretization of the gradient flow. As we have observed in Lemma 4.3 and Theorem 4.2, both the energy functional and the trajectory of this flow converge exponentially to their respective global minimum. Ideally, a gradient descent algorithm converges linearly for the function values as well as the iterates. In this direction, the forward Euler discretization of the gradient flow yields, where $\eta_{j}$ is a nonnegative stepsize to be determined. The stepsize (or learning rate) should reflect two principles during the iterative process: stay stabilizing and sufficiently decrease the function value. In following, we shall see that the gradient dominated property leads to a stepsize that results in a sufficient decrease in the function values while the coerciveness guarantees that the acquired feedback gain is stabilizing. To begin, we observe that if $K_{j + 1} = {K_{j} - {\eta_{j}{\nabla f}{(K_{j})}}}$, provided that $K_{j}$ and $K_{j + 1}$ are both stabilizing, the difference of the value matrix $X_{j + 1} - X_{j}$ can be characterized as follows.^3030^30This relationship is used.

### Lemma 4.4

If $K_{j + 1} = {K_{j} - {\eta_{j}{\nabla f}{(K_{j})}}}$ and $K_{j},K_{j + 1}$ are both stabilizing, then $Z ≔ {X_{j + 1} - X_{j}}$ solves the Lyapunov matrix equation,

### Proof

Following the same strategy used in the proof of Lemma 3.12, namely, taking the difference of the corresponding Lyapunov matrix equations, we observe that, Substituting ${K_{j + 1} - K_{j}} = {- {2\eta_{j}{({{RK_{j}} - {B^{\top}X_{j}B}})}Y_{j}}}$, we then have, We now observe that with appropriately chosen $\eta_{j}$, we can guarantee a sufficient decrease in the function value while ensuring stabilization (for the analogous result, see the third part of Theorem 7 and Lemma 24).

### Lemma 4.5

Consider the sequence $\{ K_{j}\}$ generated by with stepsize $\eta_{j}$. Denote by $\{ X_{j}\}$ the corresponding Lyapunov matrix solutions with respect to $\{ K_{j}\}$. When then $\{ K_{j}\}$ is stabilizing for every $j \geq 0$. In particular, Before presenting the proof of this result, we shall first outline its basic idea. The crucial property we shall leverage is the compactness of the sublevel sets, analogous to devising the stepsize. If we start at a stabilizing control gain $K$ where the gradient does not vanish and consider the ray of $\{{{K - {\eta{\nabla f}{(K)}}}:\eta \geq 0}\}$, by compactness of the sublevel set, there is some $\zeta$ for which ${f{(K')}} = {f{(K)}}$, where $K' ≔ {K - {\zeta{\nabla f}{(K)}}}$ (See Figure 1). What we shall demonstrate is that with the stepsize $\eta_{j}$ given in the Lemma, if $K_{j + 1}$ stays in the compact sublevel set, then $K_{j + 1}$ must stay in the interior of the sublevel set, namely, ${f{(K_{j + 1})}} < {f{(K_{j})}}$. We then proceed to examine two alternatives: $K_{j + 1}$ is not stabilizing, or $K_{j + 1}$ is stabilizing but ${f{(K_{j + 1})}} > {f{(K_{j})}}$; either alternative would lead to a contradiction.

Figure 1: Gradient descent interacting with the level curves of f.

### Proof

Suppose that the sequence generated by the choice of $\eta_{j}$ is in fact stabilizing (to be proved subsequently!). This is crucial in our analysis as we use the Lyapunov matrix equation for the closed loop system, admitting a solution when $K_{j}$ is stabilizing; without this assumption, the matrix $X_{j}$ is not well-defined. By Lemma 4.4, we have, In order to determine a stepsize $\eta_{j}$ such that ${f{(K_{j + 1})}} < {f{(K_{j})}}$, we consider a univariate function,^3131^31Note that since the products $Y_{j}Y_{j + 1}$ and $M_{j}^{\top}M_{j}Y_{j}$ are not generally symmetric, the inequalities in Proposition 2.1 are not necessarily applicable. where $M = {{RK} - {B^{\top}XA_{K}}}$, $a ≔ {\lambda_{n}{({R + {B^{\top}XB}})}}$, and $Y{(\eta)}$ is the solution of the matrix equation,^3232^32The function is not defined for every $\eta > 0$ but only for an interval for which $K - {\eta2MY}$ is stabilizing.

Note that in defining the function $g$ we have dropped the indices as this function is used to determine stepsize for every iteration. Assuming that the choice of $\eta$ ensures staying in the sublevel set of $f{(K)}$, i.e., ${f{({K - {\eta2MY}})}} \leq {f{(K)}}$, we now examine whether ${g{(\eta)}} > 0$. By the Mean Value Theorem, we have for some $\theta \in {\lbrack 0,\eta\rbrack}$; first note that, where the last inequality follows from Von Neumann's trace inequality.^3333^33An explicit form of the inequality we use here can be found. Noting that ${\| Y^{- 1}\|}_{2} = {{1/\lambda_{1}}{(Y)}}$, ensuring that ${g{(\eta)}} > 0$ reduces to characterizing $\eta$ for which, The largest eigenvalue of $Y{(\theta)}$ and largest singular value of $Y'{(\theta)}$ over the sublevel set $\{{K':{f{(K')}} \leq {f{(K)}}}\}$ can be bounded as, the proof of the latter inequality is deferred to Appendix A‖₂ in Lemma 4.5 ‣ LQR through the Lens of First Order Methods: Discrete-time Case"). Note it now suffices to determine $\eta$ such that ${1 - {b\eta} - {c\eta^{2}}} > 0$. As such, we require that, It remains to show that if $\eta_{j}$ is chosen as above, our two opening assumptions are valid: the sequence $\{ K_{j}\}$ is stabilizing, and $K_{j + 1}$ remains in the sublevel set of $f{(K_{j})}$. We prove these by contradiction. First, note that we can not have $K_{j + 1}$ be stabilizing while $K_{j + 1} \notin S_{f{(K_{j})}}$. Suppose that this is the case. The sublevel set $S_{K_{j}} ≔ {\{{K:{f{(K)}} \leq {f{(K_{j})}}}\}}$ is compact and the ray $\{{{K_{j} - {\zeta{\nabla f}{(K_{j})}}}:\zeta \geq 0}\}$ intersects the boundary of $S_{K_{j}}$ for some $\zeta > 0$; suppose that $K' = {K_{j} - {\zeta'{\nabla f}{(K_{j})}}} \in {\partial S_{K_{j}}}$, where $\zeta'$ is the smallest positive real number for which this intersection occurs, i.e., the first time the ray intersects the boundary. It is clear $\zeta'$ must be greater than $\eta_{j}$ as otherwise we would have $\zeta' < \eta_{j}$ and ${f{({K_{j} - {\zeta'{\nabla f}{(K_{j})}}})}} < {f{(K_{j})}}$, a contradiction^3434^34Note what we proved above is: if a stepsize is strictly smaller than $\eta_{j}$, the function value is strictly decreasing if the gradient is not vanishing.. Now we prove that $K_{j}$ is stabilizing. If not, we must have since otherwise, there exists $s' < \eta_{j}$ such that $s' = \zeta'$ and ${f{(K')}} = {f{(K_{j})}}$, which would also contradict the inequality ${f{(K')}} < {f{(K_{j})}}$. ∎

### Theorem 4.6

Putting $d_{j} = {\max{(b_{j},c_{j})}}$ where $b_{j},c_{j}$ are given in Lemma 4.5, if $\eta_{j} = {\sqrt{\frac{1}{3d_{j}} + \frac{1}{9}} - \frac{1}{3}}$, we have, where $q \in {}$ and $c_{1} > 0$ are constants.

### Remark 4.7

$\eta_{j}$ is acquired by noting that according to Lemma 4.5, Maximizing $\eta_{j} - {d_{j}\eta_{j}^{2}} - {d_{j}\eta_{j}^{3}}$ while esnuring ${1 - {d_{j}\eta_{j}} - {d_{j}\eta_{j}^{2}}} > 0$ yields the desired quantity.

### Proof

Note the proposed stepsize rule satisfies ${1 - {2d_{j}\eta_{j}} - {3d_{j}\eta_{j}^{2}}} = 0$. Putting $r_{j} = {{f{(K_{j})}} - {f{(K_{\ast})}}}$, we observe that with the chosen stepsize $\eta_{j}$, By Proposition B.2, the proposed stepsize is bounded away from $0$, i.e., $\eta_{j} \geq \epsilon$ for some constant $\epsilon > 0$. Hence, the sequence $\{ q_{j}\}$ is upper bounded away from $1$^3535^35It is rather clear $d_{j}$ is lower bounded away from $0$. So ${{d_{j}\eta_{j}^{2}} + {2d_{j}^{2}\eta_{j}^{3}}} > 0$., namely, for every $j$ To show the convergence of the iterates, we first observe that, with $\tau$ is as. It is clear the sequence ${\{\eta_{j}\}} \subseteq {\mathbb{R}}_{+}$ is upper bounded, denoting as $\mu$, namely $\mu \geq \eta_{j}$ for every $j$. The sequence of iterates $\{ K_{j}\}$ is thus Cauchy and converges to some stationary point; however, there is only one stationary point $K_{\ast}$. This implies that ${\lim_{j\rightarrow\infty}K_{j}} = K_{\ast}$ and hence,

### Remark 4.8

In our simulations, the linear rate is much better than what is estimated by the above result.

It is now straightforward to bound the number of iterations needed to reach $\varepsilon$-precision in terms of problem data.

### Corollary 4.8.1

Suppose that $K_{0} \in \mathcal{S}$ and the sequence of stabilizing gains $\{ K_{j}\}$ with stepsize $\eta_{j}$ given in Theorem 4.6 has been generated. Then, for

### Remark 4.9

To obtain the iteration complexity solely in terms of problem data $(A,B,Q,R,\mathbf{\Sigma},K_{0})$, it suffices to note that ${{f{(K_{0})}} - {f{(K_{\ast})}}} \leq {f{(K_{0})}}$ and we may replace ${f{(K_{0})}} - {f{(K_{\ast})}}$ by $f{(K_{0})}$ in the above estimates.

We shall point out this complexity bound is very conservative as in determining stepsize, several crude bounds were used. Empirically, we observe that the actual convergence rate is faster than the one given here.

## Natural Gradient Flow on $\mathcal{S}$

If we inspect the proof of gradient dominated property (Lemma 3.12) and the Lyapunov stability of the gradient system (Theorem 4.2), the positive definite matrix $Y$ does not affect the qualitative nature of these properties. Nevertheless, the matrix $Y$ introduces a constant factor in the corresponding upper bounds. In this section, we consider a family of gradient systems of the form, where $\gamma > 0$ is (real) scalar.^3636^36When $\gamma = 1$, this flow can be viewed as the continuous limit of the natural gradient descent as discussed. As discussed subsequently, such parameterized gradient system can achieve better convergence rate for different values of $\gamma$. Viewing such a gradient flow in the context of a flow on a Riemannian manifold is particularly pertinent.^3737^37We will see that in our case, it is better to choose $\gamma$ other than $\gamma = 1$. In fact, as $\mathcal{S}$ is open, it is a *submanifold* in ${\mathbb{M}}_{m \times n}{({\mathbb{R}})}$. We first observe that the inner product induced by $Y^{\gamma}$, i.e., ${\langle M,N\rangle}_{Y^{\gamma}} = {\operatorname{\mathbf{T}\mathbf{r}}{({M^{\top}NY^{\gamma}})}}$ is a well-defined Riemannian metric over $\mathcal{S}$.

### Proposition 5.1

Over $\mathcal{S}$, the inner product ${\langle \cdot, \cdot \rangle}_{Y{(K)}^{\gamma}}$ induces a Riemannian metric.

### Proof

Note that $Y{(K)}$ is positive definite for every $K \in \mathcal{S}$. It suffices to show that $Y{(K)}$ varies smoothly with $K$. But this follows, We can thus view $\mathcal{S}$ as a Riemannian manifold with metric induced by ${\langle \cdot, \cdot \rangle}_{Y^{\gamma}}$; the function $f:\mathcal{S}\rightarrow{\mathbb{R}}$ is then a scalar-valued function defined on this manifold. Let us now consider the gradient of $f$, denoted by $\text{grad}f$, with respect to the Riemannian metric induced by ${\langle \cdot, \cdot \rangle}_{Y^{\gamma}}$ on $\mathcal{S}$^3838^38We will use standard notitions in Riemmaninan manifold theory. For example, $df$ will denote $1$-form and $\text{grad}f$ will denote the gradient with respect to a Riemannian metric. As we are working in Euclidean space, we implicitly identiy all tangent vectors by stardard isomorphism, i.e., ${T_{K}\mathcal{S}} \approx {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$..

### Proposition 5.2

Over the Riemannian manifold $\left( \mathcal{S},{\langle \cdot, \cdot \rangle}_{Y^{\gamma}} \right)$, ${\text{grad}f} = {2{({{RK} - {B^{\top}XA_{K}}})}Y^{1 - \gamma}}$.

### Proof

It suffices to note that, Now the gradient flow of interest on this manifold is, First recall two inequalities that we encountered previously.

### Proposition 5.3

We observe that with respect to the Riemannian metric, the potential function decays at an exponential rate (compare the difference with the gradient flow in Lemma 4.3).

### Lemma 5.4

For $K_{0} \in \mathcal{S}$, denote $K{(t)}$ as the solution of. Then where $r$ is a constant determined by the system parameters $A,B,Q,R$ and $K_{0}$.

### Proof

The proof proceeds similar to Lemma 4.3. We only need to note that with respect to the Riemannian metric, According to Proposition 5.3, we now have,

### Remark 5.5

Lemma 4.3 shows that the gradient descent converges to the equilibrium point at an exponential rate ${{4\lambda_{1}{({R + {B^{\top}X_{\ast}B}})}\lambda_{1}^{2}{(Y)}}/\lambda_{n}}{(Y_{\ast})}$. Hence, the natural gradient flow modifies the exponential convergence rate of the gradient descent algorithm to ${{4\lambda_{1}{({R + {B^{\top}X_{\ast}B}})}\lambda_{1}{(Y^{2 - \gamma})}}/\lambda_{n}}{(Y_{\ast})}$, by a constant factor of ${{\lambda_{1}{(Y^{2 - \gamma})}}/\lambda_{1}^{2}}{(Y)}$. This factor depends on the largest and smallest eigenvalues of the matrix $Y$. For example, if $\gamma \geq 3$, then ${\lambda_{1}{(Y^{2 - \gamma})}} = {{1/\lambda_{n}}{(Y^{\gamma - 2})}}$.

Over the Riemannian manifold, the Lyapunov functional converges exponentially to the origin via the natural gradient flow, which leads to an exponentially stable trajectory.

### Theorem 5.6

Over $\left( \mathcal{S},{\langle \cdot, \cdot \rangle}_{Y^{\gamma}} \right)$, for the natural gradient flow, the energy functional ${f{(K_{t})}} - {f{(K_{\ast})}}$ converges exponentially to the origin. Moreover, the trajectory $K_{t}$ is exponentially stable in the sense of Lyapunov.

### Proof

Over the Riemannian manifold $\left(\mathcal{S},{\langle \cdot, \cdot \rangle}_{Y^{\gamma}} \right)$, we have, where $d = {\lambda_{1}{({R + {B^{\top}X_{\ast}B}})}\lambda_{1}{(Y^{1 - \gamma})}}$. Hence, ${{\|{K_{t} - K_{\ast}}\|}^{2} \leq {\frac{1}{2d}V{(K_{t})}} \leq {\frac{1}{2d}e^{- {rt}}V{}}}.$ ∎

### Remark 5.7

We note that the convergence rate of trajectory $K_{t}$ is dependent on $\lambda_{1}{(Y)}$ and $\lambda_{n}{(Y)}$. For example, when $\gamma = 1$ and $\mathbf{\Sigma} = {2I}$, then the natural gradient flow converges faster than the gradient flow since ${\lambda_{1}{(Y)}} > 1$. On the other hand, if $\gamma = 1$ and ${\lambda_{1}{(Y)}} < 1$, then gradient flow converges faster than natural gradient flow.^3939^39This can be done by an $\mathbf{\Sigma}$ that has a spectrum bounded by $1$. Simulation results in §8 show that this parameterized gradient flow offers a significant computational advantage for LQR.

We remark that in the particular case of $\gamma = 1$, the natural gradient flow has a favorable property with respect to the induced flow on the value matrix $X_{t}$. Consider again the flow, inducing the flow over the "value" matrix $X_{t} ≔ {X{(K_{t})}}$ given,

### Lemma 5.8

For $K_{0} \in \mathcal{S}$, the gradient flow induces a well-posed flow over the positive semidefinite cone $X_{t}$. Moreover, the trajectory $\{ X_{t}\}$ is monotonically decreasing in Loewner ordering.

### Proof

The well-posedness follows from the well-posedness of $\{ K_{t}\}$. To show that the trajectory is monotonically decreasing, it suffices to observe, where the second inequality follows. ∎ Note that this monotonicity does not hold in general for gradient flow: in this case the flow is dictated by $\mathbf{\Sigma}$ and along the trajectory, one can only guarantee that the function value $\operatorname{\mathbf{T}\mathbf{r}}{({X_{t}\mathbf{\Sigma}})}$ decreases.

### Discretization of Natural Gradient Flow

In this section, we delve into the discretization of natural gradient flow; we shall only consider the case when $\gamma = 1$.^4040^40Other choices can be analyzed in a similar manner. Specifically, we consider the gradient flow, The forward Euler discretization yields, where $\eta_{j}$ is the stepsize to be determined. In discretizing gradient flow, our guideline is to choose a stepsize such that the function value is sufficiently decreased while keeping iterates stabilizing. However, in natural gradient flow with $\gamma = 1$, we observe that by Lemma 5.8: if we follow the natural gradient flow, the value matrix is monotonic with respect to the semidefinite cone. This essentially means that taking a sufficiently small stepsize in the direction of the natural gradient would guarantee a decrease in the value of the Lyapunov matrix solution $X_{t + \delta} \preceq X_{\delta}$. The reader is also referred to (Lemma 15) where a similar stepsize for the natural gradient update has been derived).

### Lemma 5.9

Consider the sequence $\{ K_{j}\}$ generated . Denote by $\{ X_{j}\}$ the corresponding Lyapunov matrix solution with respect to $K_{j}$. If $\eta_{j} \leq {1/{({{\lambda_{n}{(R)}} + {B^{\top}X_{0}B}})}}$, then $K_{j}$ is stabilizing for every $j \geq 0$ and $X_{j + 1} \preceq X_{j}$. In particular, $Z ≔ {X_{j + 1} - X_{j}}$ solves the Lyapunov matrix equation,

### Proof

The proof proceeds similar to Lemma 4.5. First, we suppose that the sequence generated by the choice of $\eta_{j}$ is in fact stabilizing (to be proved subsequently). By Lemma 4.4, Hence, if ${{- {4\eta_{j}I}} + {4\eta_{j}^{2}R} + {4\eta_{j}^{2}B^{\top}X_{j}B}} \preceq 0$, then $X_{j + 1} \preceq X_{j}$. This can be guaranteed by choosing, It now remains to show that if $\eta_{j}$ is chosen as above, the sequence will be stabilizing. Suppose that $K_{j}$ is stabilizing. Note that the sublevel set $\mathcal{S}_{K_{j}} ≔ {\{{K:{f{(K)}} \leq {f{(K_{j})}}}\}}$ is compact and the ray $K_{j} - {\zetaM_{j}}$ intersects the boundary of $\mathcal{S}_{K_{j}}$ for some $\zeta = \zeta' > 0$; suppose that $K' = {K_{j} - {\zeta'M_{j}}} \in {\partial\mathcal{S}_{K_{j}}}$. But this implies that since otherwise, there would exist $s' \leq {{1/\lambda_{n}}{({{B^{\top}X_{j}B} + R})}}$ such that $s' = \zeta'$ and ${f{({K_{j} - {s'M_{j}}})}} = {f{(K_{j})}}$, contradicting ${f{({K_{j} - {s'M}})}} < {f{(K_{j})}}$. ∎ The problem of determining the optimal stepsize can be done by minimizing the expression, over the positive semidefinite cone. This is equivalent to minimizing, at $\eta_{j} \in {\lbrack 0,{{1/\lambda_{n}}{({R + {B^{\top}X_{j}B}})}}\rbrack}$. Obviously, the optimal stepsize should be $\eta_{j} = {1/{({2\lambda_{n}{({R + {B^{\top}X_{j}B}})}})}}$. With this choice of stepsize, the function value converges linearly to the optimal value function.

### Theorem 5.10

If $\eta_{j} = {1/{({2\lambda_{n}{({R + {B^{\top}X_{j}B}})}})}}$, we have, where $q_{0} = {{({1 - {4\lambda_{1}{(R)}}})}/{({\lambda_{n}{(Y_{\ast})}\lambda_{n}{({R + {B^{\top}X_{0}B}})}})}}$ and $c_{2}$ is some positive constant.

### Proof

Putting $r_{j} = {{f{(K_{j})}} - {f{(K_{\ast})}}}$, we observe that with the chosen $\eta_{j}$, | | | {{r_{j} - r_{j + 1}} = {\operatorname{\mathbf{T}\mathbf{r}}{({{({X_{j} - X_{j + 1}})}\mathbf{\Sigma}})}}} & {\geq {\operatorname{\mathbf{T}\mathbf{r}}{({\frac{1}{\lambda_{n}{({R + {B^{\top}X_{j}B}})}}M_{j}^{\top}M_{j}Y_{j + 1}})}}} \\ | | | | | & {\geq {\frac{\| Y_{j + 1}\|}{\lambda_{n}{({R + {B^{\top}X_{j}B}})}}{\operatorname{\mathbf{T}\mathbf{r}}{({M_{j}^{\top}M_{j}})}}}} \\ | | | | | & {{\geq {\frac{4\lambda_{1}{(R)}}{\lambda_{n}{(Y_{\ast})}\lambda_{n}{({R + {B^{\top}X_{j}B}})}}r_{j}}}.} | | It thus follows that, Note that by the choice of stepsize, $\{ X_{j}\}$ monotonically decreases over the positive semidefinite cone and thus $q_{j} \leq q_{0}$ for $j \geq 1$, where, in the last inequality we have used the estimate ${\| Y_{\ast}\|} \leq {{{f{(K_{0})}}/\lambda_{1}}{(Q)}}$ in Proposition 3.13. Thereby, The proof to the convergence of the iterates is almost identical to the one in Theorem 4.6 ∎

### Remark 5.11

We note that the discretization of natural gradient flow can perform better than gradient descent. One can monitor the one step progression $r_{j} - r_{j + 1}$ to confirm such a behavior. This is different from the continuous flows as if ${\lambda_{1}{(Y)}} > 1$, then gradient flow performs better than natural gradient flow.

## Quasi-Newton Flow on $\mathcal{S}$

In this section, we motivate a quasi-Newton flow over the set of stabilizing feedback gains (policy) $\mathcal{S}$.^4141^41The justification for calling this evolution a quasi-Newton flow becomes apparent subseqeuntly. As observed previously, the Hessian of the LQR cost $f{(K)}$ is not positive definite everywhere. As such, there is no well-defined notion of (global) Newton iteration over policy space. However, examining Lemmas 4.4 and 5.9 allows us to derive a local second-order approximation of the LQR cost under the Riemannian metric $Y$. With is metric, recall that the gradient of $f$ is, We now provide the second-order approximation of the cost function.^4242^42Lemma 6.1 can be considered as a slight extension of Lemma $6$. However, the emphasis in was on the asymptotic behavior of the first-order approximation; this setup was subsequently utilized for a different purpose. For our purpose, it is important to prove that for the second-order approximation, the remainder of the approximation is $O{({\|{\DeltaK}\|}^{2})}$.

### Lemma 6.1

When $K$ and $K + {\DeltaK}$ are both stabilizing for sufficiently small $\DeltaK$,^4343^43By openness of $\mathcal{S}$, if $\DeltaK$ is sufficiently small, $K + {\DeltaK}$ is stabilizing provided that $K$ is. then, where $\|{\mathcal{R}{({\DeltaK})}}\|$, the remainder of the approximation, is $O{({\|{\DeltaK}\|}^{2})}$.

### Proof

Suppose that $X_{K + {\DeltaK}}$ and $X_{K}$ are the corresponding value matrices for $K + {\DeltaK}$ and $K$, respectively. By Lemma 4.4, we have, It then follows that, | | | {{f{({K + {\DeltaK}})}} - {f{(K)}}} & {= {\operatorname{\mathbf{T}\mathbf{r}}{({{({X_{K + {\DeltaK}} - X_{K}})}\mathbf{\Sigma}})}}} \\ | | | | | & {{= {{\operatorname{\mathbf{T}\mathbf{r}}{({Y_{K + {\DeltaK}}{({\DeltaK})}^{\top}M_{K}})}} + {\operatorname{\mathbf{T}\mathbf{r}}{({Y_{K + {\DeltaK}}{({\DeltaK})}^{T}{({R + {B^{\top}XB}})}{({\DeltaK})}})}}}},} | | where $Y_{K + {\DeltaK}}$ solves the Lyapunov equation, $Y_{K + {\DeltaK}}$ can be written as $Y_{K + {\DeltaK}} = {\sum_{j = 0}^{\infty}{{(A_{K + {\DeltaK}})}^{j}\mathbf{\Sigma}{(A_{K + {\DeltaK}}^{\top})}^{j}}}$. Note that if we expand the right-hand side of this last expression, we may alternatively write, where $\mathcal{R}_{Y}{({\DeltaK})}$ is the remainder term and consists of polynomials in $\DeltaK$ with smallest degree $1$. Substituting the above equation, we have it is clear that $\mathcal{R}{({\DeltaK})}$ consists of polynomials in $\DeltaK$ with smallest degree ${({\DeltaK})}^{2}$. ∎ Lemma 6.1 essentially states that we have a somewhat "good" local second-order approximation of $f{(K)}$ with respect to the Riemannian metric $Y$. We may now devise a flow to minimize $f{(K)}$ by minimizing this second-order approximation, namely, The analysis presented in §4 and §5 allow us to obtain a streamlined proof of the convergence of this flow; as such, we omit the proof.

### Discretization of Quasi-Newton Flow

The quasi-Newton flow over $\mathcal{S}$ has interesting consequences in terms of its discretization: the forward Euler leads to the iterative procedure with stepsize $\eta_{j}$ to be determined; we shall show that with constant stepsize $\eta = \frac{1}{2}$, both the function value and the iterates will converge quadratically to the optima.

### Remark 6.2

The update is consistent with the Gauss-Newton updates proposed . We have chosen to refer to this update as quasi-Newton in this paper as it is obtained by minimizing a local second-order approximation of the LQR cost at each iteration.

We first observe that if $\eta \leq 1$, the corresponding sequence of value matrices $\{ X_{j}\}$ is monotonically decreasing over the positive semidefinite cone.

### Lemma 6.3

Consider the sequence $\{ K_{j}\}$ generated . Denote by $\{ X_{j}\}$ the corresponding Lyapunov matrix solution with respect to $K_{j}$. If $\eta_{j} < 1$, then $K_{j}$ is stabilizing for every $j \geq 0$ and $X_{j + 1} \preceq X_{j}$. In particular $Z ≔ {X_{j + 1} - X_{j}} \preceq 0$ solves the Lyapunov matrix equation,

### Proof

Suppose that with $\eta_{j} < 1$, the sequence generated by are all stabilizing.^4444^44Similar to the proof to Lemma 5.9, we need this assumption to make sense of defining the corresponding value matrix sequence $\{ X_{j}\}$. Substituting the update rule in yields, It is now clear if $\eta_{j} < 1$, then ${X_{j + 1} - X_{j}} \preceq 0$. To show the choice of $\eta_{j}$ guaranteeing the stability of $A - {BK_{j}}$, we may follow almost the same argument as in the proofs of Lemmas 4.4 and 5.9. ∎ The optimal stepsize for the quasi-Newton iteration is obtained by minimizing the quantity ${- {4\eta}} + {4\eta^{2}}$. As such, the optimal stepsize is $\eta_{j} = {1/2}$ for every $j$. The corresponding update is then equivalent to,

### Remark 6.4

With the optimal choice of stepsize as $\eta = {1/2}$, the quasi-Newton over $K$ coincides with the Hewer' algorithm, obtained by considering the Newton iteration over the ARE. We have thus provided an alternative point view of this algorithm: the algorithm can be obtained directly over the policy space even without the ARE.

### Theorem 6.5

With stepsize $\eta = {1/2}$, the update converges to the global minimum at a Q-quadratic rate. Namely, there exists constants ${c > 0},{c_{3} > 0}$, such that,

### Proof

By Lemma 6.3 and noting ${{RK_{\ast}} - {B^{\top}X_{\ast}A_{K_{\ast}}}} = 0$, we have It then follows that, where the third equality follows from ${({I + N})}^{- 1} = {I - {{({I + N})}^{- 1}N}}$. Hence, To establish the quadratic convergence of iterates, putting $S_{\ast} = {\sum_{\nu = 0}^{\infty}{{(A_{\ast}^{\top})}^{\nu}{(A_{\ast})}^{\nu}}}$, we observe by Proposition 2.1 and equation On the other hand,

## Structured LQR Synthesis

In this section, we consider the problem of designing the feedback gain $K$ over a subspace. In particular, we are primary interested in feedback gains with a desired sparsity pattern. This is a natural formulation of distributed networked systems on an information-exchange graph $\mathcal{G} = {(V,E)}$. In such a setting, structured feedback gains reflecting the underlying interaction network are of particular interest. If the state of only a subset of agents is accessible for control implementation, the feedback gain must have a zero pattern that is compatible with this accessibility requirement, i.e., $K_{ij} = 0$ if ${(i,j)} \notin {E{(\mathcal{G})}}$.

In this section, we are interested in optimizing the LQR cost over the set, where $\mathcal{U}$ is a linear subspace defined by the graph structure, i.e., In light of the central theme of this work, projected gradient descent (PGD) is a natural choice for determining the feedback gain in the set $\mathcal{K}$, optimizing $f$ over $\mathcal{U}$. Such an approach leads to the iteration of the form, where $\eta$ is the stepsize; the choice of this stepsize will be discussed in §7.1. One may note that the geometry of $\mathcal{K}$ can be rather involved. Indeed, this set could have exponentially many path connected components (see). In the meantime, a favorable structure for $A$ and the graph $\mathcal{G}$ would guarantee that $\mathcal{K}$ has only one connected component. This point will not be further discussed in this paper. Herein, we further examine how to update the feedback gain in the path connected component of $\mathcal{K}$, once the algorithm has been initialized in this component.

Even this more modest objective however faces some issues as $\mathcal{K}$ has an intricate geometry and one has to address how to efficiently project onto it. In the sequel, we shall show that the seemingly relaxed update rule, is equivalent to, where $P_{\mathcal{U}}$ denotes the orthogonal projection onto $\mathcal{U}$.

### Theorem 7.1

The updating rule is equivalent to provided the initial condition $K_{0} \in \mathcal{K}$.

In proving this theorem, we will demonstrate that the relaxed updating rule is equivalent to the gradient descent update over a $C^{\infty}$ function $g:\mathcal{K}\rightarrow{\mathbb{R}}$ which is the restriction of $f$, i.e., $g = {f|}_{\mathcal{K}}$. We first establish several favorable properties of $g$.

### Lemma 7.2

The set $\mathcal{K}$ is open in $\mathcal{U}$ and the relative boundary of $\mathcal{K}$ is a subset of the boundary $\mathcal{S}$, i.e., ${\text{rbd~}\mathcal{K}} \subset {\partial\mathcal{S}}$.

### Proof

Since $\mathcal{K} = {\mathcal{U} \cap \mathcal{S}}$ and $\mathcal{S}$ is open in ${\mathbb{M}}_{n \times n}{({\mathbb{R}})}$, the set $\mathcal{K}$ is open in the subspace topology. If $x \in {\text{rbd~}\mathcal{K}}$, then for any $\varepsilon > 0$, ${B_{\varepsilon}{(x)}} \cap \mathcal{U}$ contains points both in $\mathcal{U} \cap \mathcal{S}$ and ${({\mathcal{U} \cap \mathcal{S}})}^{c}$. It follows then that $B_{\varepsilon}{(x)}$ contains points both in $\mathcal{S}$ and $\mathcal{S}^{c}$ and hence $x \in {\partial S}$. ∎ As a consequence of the characterization of the relative boundary, the restriction $g$ is also coercive; first, recall the definition of $\overset{\sim}{f}$ in Corollary 3.7.1.

### Lemma 7.3

Let $\overset{\sim}{g} ≔ {\overset{\sim}{f}{({P_{\mathcal{U}}x})}}:{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}$. Then $\overset{\sim}{g}$ is continuous and infinitely differentiable on $\mathcal{K}$. For $K \in \mathcal{S}$ and $E \in \mathcal{U}$, we have

### Proof

The function $\overset{\sim}{g}$ is continuous as it is a composition of $\overset{\sim}{f}$ and $P_{\mathcal{U}}$. As such $g \in C^{\infty}$ on $\mathcal{K}$ as $f$ is $C^{\infty}$ on $\mathcal{S}$. Furthermore, we note that, In terms of matrix representation in the standard basis and $K \in \mathcal{K}$, Hence, if $K \in \mathcal{K}$ and ${E,F} \in \mathcal{U}$, We are now ready to provide the proof for Theorem 7.1.

### Proof

We note that $g = {\overset{\sim}{g}|}_{\mathcal{K}}$. Based on the initial state independent formulation, ${g{(K)}} < \infty$ implies that $K \in \mathcal{K}$. Thus, if $K_{0} \in \mathcal{K}$, then the update rule is exactly, Therefore, if $\eta$ is chosen sufficiently small for which ${g{(K_{1})}} \leq {g{(K_{0})}}$, then $K_{1} \in \mathcal{K}$. Thereby, the update rule is equivalent to, The statement of the theorem now follows by induction. ∎

### Convergence of Projected Gradient Descent

As we have argued, the projected gradient descent scheme is equivalent to gradient descent on $g$.^4545^45One should note that the analysis in § 4.1 can not be adopted for the projected case. In the analysis of one step progression of gradient descent, the crucial fact is that the difference between $f{(K_{j})}$ and $f{(K_{j + 1})}$ is bounded in terms of product of positive semidefinite matrices. However, in projected case, if we follow the same line of reasoning, we arrive at the term $\mathcal{V} ≔ {\operatorname{\mathbf{T}\mathbf{r}}{({{M_{K}^{\top}{\lbrack{P_{\mathcal{U}}{({M_{K}Y_{K}})}}\rbrack}} + {{\lbrack{P_{\mathcal{U}}{({M_{K}Y_{K}})}}\rbrack}^{\top}M_{K}}})}}$ and there is no clear lower bound for $\mathcal{V}$ in terms of $\operatorname{\mathbf{T}\mathbf{r}}{({{\lbrack{P_{\mathcal{U}}{({M_{K}Y_{K}})}}\rbrack}^{\top}{\lbrack{P_{\mathcal{U}}{({M_{K}Y_{K}})}}\rbrack}})}$. In fact, $\mathcal{V}$ could be negative definite or indefinite in general. Conceptually, the stepsize can be determined as follows: if $K_{0} \in \mathcal{K}$, then the sublevel set $S_{g{(K_{0})}} = {\{{K \in \mathcal{S}:{g{(K)}} \leq {g{(K_{0})}}}\}}$ is compact. As $\|{{\nabla^{2}g}{(K)}}\|$ is continuous, there is a scalar $L > 0$ such that ${\max_{K \in S_{g{(K_{0})}}}{\|{{\nabla^{2}g}{(K)}}\|}} = L$, i.e., the gradient mapping ${\nabla g}{(K)}$ is Lipschitz continuous with rank $L$ on $S_{g{(K_{0})}}$. We may have chosen a constant stepsize $1/L$ if $g$ was a convex function. However, nonconvexity of $g$ and $\mathcal{K}$ introduce additional complications for determining the constant stepsize. In fact, we need to first address whether the sequence ${\{ K_{j}\}}_{j = 0}^{\infty}$ generated by is guaranteed to stay in $\mathcal{K}$.

As in the convergence analysis of $L$-smooth convex functions, at iterate $K_{j}$, a quadratic function majorizing $g{(K)}$ is formulated; in this case, minimizing the quadratic majorizing function will lead to the global minimum. In our case, the quadratic majorant, only majorizes $g{(K)}$ over the sublevel set $S_{g{(K_{0})}}$. Since $\mathcal{K}$ is not convex, it is not straightforward that, is still stabilizing. But the coerciveness of $g$ remedies this complication.

### Lemma 7.4

Let $L = {\sup_{K \in S_{g{(K_{0})}}}{\|{{\nabla^{2}g}{(K)}}\|}}$ and consider the sequence ${\{ K_{j}\}}_{j = 0}^{\infty}$ generated by gradient descent with constant stepsize $\eta = {1/L}$. If $K_{0} \in \mathcal{K}$ then the sequence stays in $\mathcal{K}$.

### Proof

Let ${m{(K;K_{0})}} ≔ {{g{(K_{0})}} + {\langle{{\nabla g}{(K_{0})}},{K - K_{0}}\rangle} + {\frac{L}{2}{\|{K - K_{0}}\|}_{F}^{2}}}$. Since $g_{f{(K_{0})}}$ is compact, the ray $K_{0} - {t{\nabla g}{(K_{0})}}$ will intersect $S_{f{(K_{0})}}$ at a gain other than $K_{0}$; denote it, As the line segment is contained in $\mathcal{S}_{g{(K_{0})}}$, $m{(K)}$ majorizes $g{(K)}$ over the line segement $\lbrack K_{0},K'\rbrack$. We now define a univariate function ${\phi{(t)}} = {Q{({K_{0} - {t{\nabla f}{(K_{0})}}})}}$ and note that $\phi{(t)}$ majorizes $g$ over $\lbrack 0,\xi\rbrack$. We have ${\phi{}} = {g{(K_{0})}}$ and ${\phi{(\xi)}} \geq {g{(K')}} = {g{(K_{0})}}$ since ${K',K_{0}} \in {\partial S_{g{(K_{0})}}}$. By Rolle's Theorem, there exists a stationary point $t \in {(0,\xi)}$ with ${\phi'{(t)}} = 0$. Hence, $t = {K_{0} - {{({1/L})}{\nabla g}{(K_{0})}}}$ is contained in the sublevel set $S_{g{(K_{0})}}$. The proof is now completed by induction. ∎ As we have established the equivalence between the projected gradient descent for $f$ and $g$, and $g$ is smooth and coercive in the subspace $\mathcal{U}$, we immediately establish the sublinear convergence to a first-order stationary point. Note that the operator norm of the Hessian ${\nabla^{2}g}{(K)}$ is given,

### Lemma 7.5

Suppose that $K_{0} \in \mathcal{K}$ and recall that the sublevel set is given by Let $L = {\sup_{K \in S_{g{(K_{0})}}}{\|{{\nabla^{2}g}{(K)}}\|}}$; if the stepsize $\eta$ in is set as $t = {1/L}$, then the sequence ${\{ K_{j}\}}_{j = 0}^{\infty}$ generated by the projected gradient descent convergences to a first-order stationary point at a sublinear rate, i.e.,

### Proof

This is straightforward by Lemma 7.4 and §$1.2.3$ . ∎

### Choosing the stepsize for projected gradient descent

As we have pointed out, choosing an appropriate stepsize is equivalent to estimating the operator norm of the Hessian ${\nabla^{2}g}{(K)}$ over the sublevel set $S_{g{(K_{0})}}$.

### Proposition 7.6

On the sublevel set $S_{g{(K_{0})}}$, we have

### Proof

We only need to observe that for each $K \in \mathcal{K}$, We next provide an estimate of $\|{{\nabla^{2}f}{(K)}}\|$ in terms of the system matrices $A,B$, cost function coefficients $Q,R$, and the initial condition $K_{0}$. Let $\alpha = {f{(K_{0})}}$ and $S_{\alpha} = {\{{K \in \mathcal{S}:{f{(K)}} \leq \alpha}\}}$. For $K \in S_{\alpha}$, ${\operatorname{\mathbf{T}\mathbf{r}}{({X{(K)}\mathbf{\Sigma}})}} \leq {\operatorname{\mathbf{T}\mathbf{r}}{({X_{0}\mathbf{\Sigma}})}}$, where $X_{0}$ is the solution to the Lyapunov equation ${{A_{K_{0}}^{\top}X_{0}A_{K_{0}}} + Q + {K_{0}^{\top}RK_{0}}} = X_{0}$.^4646^46Note that on the sublevel set $S_{\alpha}$, it *does not hold* that $X \preceq X_{0}$ We denote the bound on the operator norm of the Hessian $D^{2}f{(K)}$ on the sublevel set $S_{f{(K_{0})}}$ by $L$; namely, In order to estimate $L$, we first observe that by trianglular inequality and Proposition 2.1, where the second inequality follows from Theorem $2$.

In what follows, we estimate each term in on $S_{f{(K_{0})}}$. This will be achieved by a series of propositions. We first estimate a bound for ${\lambda_{n}{(Y)}},{\operatorname{\mathbf{T}\mathbf{r}}{(Y^{1/2})}},{\|{A_{K}Y^{1/2}}\|}_{2},{\lambda_{n}{({R + {B^{\top}XB}})}}$ on $S_{f{(K_{0})}}$. Recall that $Y$ is the solution of ${{A_{K}YA_{K}^{\top}} + \mathbf{\Sigma}} = Y$, i.e., $Y = {\sum_{j = 0}^{\infty}{{(A_{K})}^{j}\mathbf{\Sigma}{(A_{K}^{\top})}^{j}}}$.

### Proposition 7.7

### Proof

Recall we have already upper bounded $\operatorname{\mathbf{T}\mathbf{r}}{(Y)}$ in Proposition 3.13: ${\operatorname{\mathbf{T}\mathbf{r}}{(Y)}} \leq \frac{f{(K_{0})}}{\lambda_{1}{(Q)}}$^4747^47Indeed, we bound $\operatorname{\mathbf{T}\mathbf{r}}{(Y_{\ast})}$ in Proposition 3.13. But the proof works verbatim for any $Y$ over the sublevel set.. It follows For $R + {B^{\top}XB}$, we have Next, we provide an upper bound for the spectral norm of $X'{(K)}{\lbrack E\rbrack}$ on $S_{f{(K_{0})}}$.

### Proposition 7.8

### Proof

To simplify the notation, let We note that by Proposition 2.1, for every $\zeta > 0$ we have: It then follows that, Conversely, following the reverse path of the above inequalities and using Proposition 2.1, it can be shown that ${X'{(K)}{\lbrack E\rbrack}} \succeq {- {\xiI}}$. As such, ${{\|{X'{(K)}{\lbrack E\rbrack}}\|}_{2} \leq {\xiX}}.$ ∎ Combining all the bounds, we have:

### Lemma 7.9

On the sublevel sets $S_{f{(K_{0})}}$, the gradient ${\nabla f}{(K)}$ is $L$-Lipschitz continuous.

### Proof

It suffices to observe that on $S_{f{(K_{0})}}$, where $\xi$ is the constant defined in Proposition 7.8 and note $\xi$ is only determined by problem data $(A,B,Q,R,\mathbf{\Sigma},K_{0})$. ∎ Lemma 7.9 provides a Lipschitz constant in terms of the LQR parameters $A,B,Q,R$ and initial condition $K_{0}$; hence, a stepsize for gradient descent.

### Remark 7.10

We shall point out that as the projected gradient descent algorithm proceeds the function values $g{(K)}$ decrease. Hence, we can re-estimate the bounds in the above propositions at each iteration. For example, at iteration $K_{j}$, the Lipschtiz constant $L_{K_{j}}$ of ${\nabla g}{(K)}$ over the sublevel set $S_{g{(K_{j})}}$ can be estimated and we may as well use a stepsize $1/L_{K_{j}}$ by Lemma 7.4. The benefit is that this stepsize is certainly larger than $1/L_{f{(K_{0})}}$. In this case, we shall have an increasing sequence of stepsizes ${\{{1/L_{j}}\}}_{j = 0}^{\infty}$ that is bounded from above.

The stepsize rule devised here certainly works for unstructured case (i.e., gradient descent). However, this stepsize is typically smaller than the one we work out in Lemma 4.5. The reason is that here all the terms must be bounded over the whole sublevel set while in Lemma 4.5 we carefully compare one step progression of gradient descent.

## Simulation Results

In this section, we provide a representative set of examples to demonstrate the results reported in this paper.

We first demonstrate the exponential stability of the proposed continuous flows. The system is of form with parameters $(A,B)$, $A \in {\mathbb{R}}^{100 \times 100}$ and $B = I$, guaranteeing the controllability of the system. The entries of $A$ are sampled from a standard normal distribution $\mathcal{N}{}$. We also scale $A$ when necessary to make it stable such that the initial feedback gain can be set as $K_{0} = 0$. The cost matrices $Q,R$ are taken to be identity with appropriate dimensions. For the natural gradient, we simulate the flow with two different Riemannian metrics, one induced by $Y$ and the other by $Y^{2}$. Figure 3 demonstrates the exponential stability of the corresponding trajectories and Figure 3 depicts the exponential stability of the Lyapunov functionals for all flows when $\mathbf{\Sigma} = {0.5I}$. The results are consistent with the observations discussed in §4, §5, and §6. In particular, since ${\lambda_{1}{(Y)}} < 1$, the natural gradient flow converges faster than the gradient flow, and amongst the natural gradient flows, the one with the metric induced by $Y^{2}$ outperforms the one with metric $Y$. Figures 5 and 5 show the convergence results with the same LQR parameters $(A,B,Q,R)$, but the initial state matrix has chosen to be $\mathbf{\Sigma} = {2I}$. These two figures underscore the observations in Remark 5.7: gradient flow outperforms natural gradient flows when ${\lambda_{1}{(Y)}} > 1$.

Figure 2: Exponential stability of trajectory Kt with the initial state matrix Σ = 0.5 I.

Figure 3: Exponential decay of the Lyapunov functional with the initial state matrix Σ = 0.5 I.

Figure 4: Exponential stability of trajectory Kt with the initial state matrix Σ = 2 I.

Figure 5: Exponential decay of the Lyapunov functional with the initial state matrix Σ = 2 I.

Next we examine the discrete realizations of these flows, namely, gradient descent, natural gradient descent and the quasi-Newton iteration (with the same setup for system parameters). With the adaptive stepsize proposed in Theorem 4.6, Figure 7 demonstrates that the sequence of feedback gains generated by gradient descent is stabilizing and converges to the global optimal feedback gain. Moreover, Figure 7 shows that the cost function $f{(K)}$ converges to $f{(K_{\ast})}$ at a linear rate.

Figure 6: Convergence of the relative error for the feedback gain under gradient descent with adaptive stepsize given by 4.5 Figure 7: Convergence of the relative error for the LQR cost under gradient descent In the meantime, Figures 9 and 9 demonstrate the linear convergence of the natural gradient descent algorithm. The stepsize is chosen adptively according to Theorem 5.10; we note the faster convergence of natural gradient descent compared with gradient descent.

Figure 8: Convergence of the relative error for the feedback gain under natural gradient descent with adaptive stepsize given by 4.5 Figure 9: Convergence of the relative error for the LQR cost under natural gradient descent Figures 11 and 11 demonstrate the quadratic convergence for the quasi-Newton iteration. The stepsize is chosen to be $1/2$; in this case, we recover the Hewer's algorithm, enjoying the fastest convergence rate.

Figure 10: Convergence of the relative error for the feedback gain under quasi-Newton with constant stepsize $\frac{1}{2}$ Figure 11: Convergence of the relative error for the LQR cost under natural gradient descent We now examine the projected gradient descent for a system modeled over a $$-lollipop graph.^4848^48A lollipop graph consists of a complete graph on $10$ nodes and a path graph on $10$ nodes. The system matrix $A$ is chosen as the Metropolis-Hastings weight matrix for the graph and $B = I$. The initial gain matrix is chosen as $K_{0} = 0$. In each iteration the feedback gain is updated as, where the projection is equivalent to zeroing out the entries that do not correspond to edges in the graph. Consistent with Lemma 7.5, Figure 13 demonstrates that the sequence of feedback gains is stabilizing and converges to a first-order stationary point. Moreover, Figure 13 depicts the convergence of the cost function $f{(K)}$.

Figure 12: Convergence of the relative error for the feedback gain under projected gradient descent on a lollipop graph.

Figure 13: Convergence of the relative error for the LQR cost under projected gradient descent on a lollipop graph.

## Concluding Remarks

The paper considers LQR through the lens of first order methods--an LQR calculus--where control synthesis is viewed directly in terms of optimizing an objective function over the set of stabilizing feedback gains. Using this narrative, we proceed to examine gradient descent and its various extensions for solving the LQR problem. The LQR objective is constructed over a set of linearly independent initial states to eliminate the dependency of the optimal policy on the initial state and encode closed loop stability. It is shown that the corresponding cost function is smooth, coercive and gradient dominated (this latter fact was previously reported in the literature; we provide an alternate approach for its proof). We next discussed three types of well-posed flows over the set of stabilizing controllers: gradient flow, natural gradient flow and the quasi-Newton flow. We subsequently examine the discretization of these flows, and show that their realizations using the forward Euler method, i.e., gradient descent, natural gradient flow and quasi-Newton iterations, lead to algorithms with linear convergence rate and quadratic convergence rate. Finally, we consider projected gradient descent for solving structured LQR. In this direction, we provided a stepsize rule which leads to the sublinear convergence to the first-order stationary point.
