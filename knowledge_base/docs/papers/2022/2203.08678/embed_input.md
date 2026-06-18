<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Programming through the Lens of Semismooth Newton-Type Methods (Extended Version)

Topics include Policy iteration, Value iteration, Control, Markov decision process, Fixed-point iteration, Dynamic programming, Bellman equations, Fixed point.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy iteration and value iteration are at the core of many (approximate) dynamic programming methods. For Markov Decision Processes with finite state and action spaces, we show that they are instances of semismooth Newton-type methods to solve the Bellman equation. In particular, we prove that policy iteration is equivalent to the exact semismooth Newton method and enjoys local quadratic convergence rate. This finding is corroborated by extensive numerical evidence in the fields of control and operations research, which confirms that policy iteration generally requires few iterations to achieve convergence even when the number of policies is vast. We then show that value iteration is an instance of the fixed-point iteration method. In this spirit, we develop a novel locally accelerated version of value iteration with global convergence guarantees and negligible extra computational costs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Approximate dynamic programming (ADP) is a powerful algorithmic strategy to handle stochastic sequential decision making problems arising in a wide range of applications, from control to games and resource allocation, to name a few. At the core of some of the biggest success stories of ADP is an approximate version of policy iteration. In particular, after an extensive offline training phase where an approximation of the optimal cost is produced, one iteration of an approximate version of policy iteration is performed (online learning). Empirical evidence suggests that this final step greatly enhances performance. In particular, Bertsekas in links these success stories to the equivalence between policy iteration and Newton's method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The connection between policy iteration and Newton's method dates back to the late 60's. Puterman and Brumelle were among the first who exploited this connection to study the convergence properties of policy iteration for MDPs with continuous action spaces. More recently, Santos and Ruts exploited this connection to analyze the asymptotic convergence of policy iteration for the discretization of a specific class of MDPs with continuous spaces. Bertsekas in provides a graphical analysis of the connection between policy iteration and Newton's method. He then mathematically formalizes these visual insights by proving local quadratic convergence of policy iteration for Markov Decision Processes (MDPs) with finite state and action spaces. These theoretical results are corroborated by numerous computational examples which demonstrate that policy iteration achieves convergence in a remarkably small number of iterations even in presence of rounding errors and a large number of potential policies. We refer to for an extensive review of the related works.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we consider MDPs with finite state and action spaces and we formally show that policy iteration and value iteration are both instances of semismooth Newton-type methods. The main differences between our analysis and that of Bertsekas are that the latter only focus on policy iteration and does not deploy tools from generalized differentiation, but works in a neighborhood of the solution where the iterations can be expressed as the Newton iterations for some auxiliary continuously differentiable mapping. We then take this connection further by developing a novel version of value iteration inspired by the fixed-point iteration method. In particular, our main contributions are the following.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In Section II-B"), we develop a unified theoretical analysis for the local convergence of semismooth Newton-type methods based on the so-called kappa condition.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In Sections III-A") and III-B"), we formalize mathematically the connection of policy iteration and value iteration with semismooth Newton-type methods using tools from generalized differentiation and results from Section II"). We then discuss the significant algorithmic and theoretical implications of this connection.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In Section III-C"), we design a novel globally convergent and locally accelerated variant of value iteration with negligible additional computational cost per iteration and superior numerical performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

Dynamic Programming (DP) comprises the methods for solving stochastic optimal control problems by solving the Bellman equation. Here we are interested in DP algorithms in the classes of value iteration (VI) and policy iteration (PI). Starting from Equation (3")), we define a nonsmooth mapping $T:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$, known as the Bellman operator, by

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

An analogous linear operator $T^{\pi}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ can be defined for the Bellman equation associated with policy $\pi$ as

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

Given the cost vector $V$, any policy $\pi$ such that

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

is called greedy with respect to the cost $V$. It can be shown that the Bellman operator is contractive and, thanks to the Banach Theorem, admits a unique fixed point $V^{\ast}$. Moreover, the corresponding Picard-Banach iteration converges asymptotically to the fixed point from any initial value $V$, i.e.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

This is at the core of VI, which repeatedly applies the $T$ operator starting from an arbitrary finite cost. The generated sequence linearly converges to $V^{\ast}$ with a $\gamma$-contraction rate.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

An alternative method to solve Equation (3")) is PI (Algorithm 1")). With PI, we start from an arbitrary initial policy and alternate policy evaluation (step 3) and policy improvement (step 4) until convergence. The policy evaluation step at iteration $k$ computes the cost $V^{\pi_{k}}$ associated with the current policy $\pi_{k}$. This requires the solution of a system with $n$ linear equations, which is generally computationally demanding for MDPs with large state spaces. The policy is then updated by extracting a greedy policy associated with $V^{\pi_{k}}$ in the policy improvement step. Unlike VI, PI converges in a finite number of iterations since the policy, and therefore also its cost, are improved at each iteration and since, by the finiteness of $\mathcal{S}$ and $\mathcal{A}$, there only exists a finite number of policies.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

It is nonetheless important to characterize its convergence rate and asymptotic behavior since, for large state and action spaces, the number of iterations could be prohibitive (exponential in $n$ and $m$). By exploiting the properties of the Bellman operator, we can show that PI is globally $\gamma$-contractive, which is similar to VI. Extensive empirical evidence, however, suggests that PI has superior convergence properties and generally requires considerably fewer iterations than VI. From a computational viewpoint, the per-iteration costs of PI with direct inversion amount to $\mathcal{O}{({n^{3} + {m \cdot n^{2}}})}$ versus the $\mathcal{O}{({m \cdot n^{2}})}$ of VI.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Dynamic Programming", "weight": 1.0} -->

1:Initialization: select an arbitrary initial policy π0 and set k = 0
2:while cost has not converged do
4: $\pi_{k + 1} = \overset{\sim}{\pi}$ with $\overset{\sim}{\pi} \in {\text{GreedyPolicy}{(V^{\pi_{k}})}}$ according to
Algorithm 1 Exact Policy Iteration

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Generalized Differentiation & Semismooth Newton-Type Methods", "weight": 1.0} -->

Consider the following nonlinear root finding problem

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Generalized Differentiation & Semismooth Newton-Type Methods", "weight": 1.0} -->

where $r:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is a locally Lipschitz-continuous vector-valued function. A vector $\theta^{\ast} \in {\mathbb{R}}^{d}$ that verifies (6")) is called root or solution of the nonlinear equation (6")). In general, we can not rely on smooth optimization methods to solve (6")) since $r$ can be nonsmooth, so its Jacobian ${r^{\prime}{(\theta)}} \in {\mathbb{R}}^{d \times d}$ might not exist. We therefore need to introduce some notions of generalized differentiability from nonsmooth analysis, such as the B-differential and Clarke's generalized Jacobian.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Generalized Differentiation & Semismooth Newton-Type Methods", "weight": 1.0} -->

Since $r$ is a locally Lipschitz-continuous map, the Rademacher Theorem implies that it is differentiable almost everywhere and we denote with $\mathcal{M}_{r}$ the set of all points where $r$ is differentiable. Another fundamental implication of the Rademacher Theorem is the definition of the B-differential of $r$ at $\theta \in {\mathbb{R}}^{d}$ as the set

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Generalized Differentiation & Semismooth Newton-Type Methods", "weight": 1.0} -->

We denote with $\partial{r{(\theta)}}$ Clarke's generalized Jacobian of $r$ at $\theta \in {\mathbb{R}}^{d}$, which is defined as the convex hull of $\partial_{B}{r{(\theta)}}$. Consequently, ${\partial_{B}{r{(\theta)}}} \subseteq {\partial{r{(\theta)}}}$. These sets are always nonempty when evaluated at points where the function is Lipschitz continuous \[9, Proposition 1.51\]. If $r$ is continuously differentiable at $\theta$, then ${\partial{r{(\theta)}}} = {\partial_{B}{r{(\theta)}}} = \left\{ {r^{\prime}{(\theta)}} \right\}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Generalized Differentiation & Semismooth Newton-Type Methods", "weight": 1.0} -->

Otherwise, $\partial_{B}{r{(\theta)}}$ and, consequently, $\partial{r{(\theta)}}$ are not necessarily singletons.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Generalized Differentiation & Semismooth Newton-Type Methods", "weight": 1.0} -->

The B-differential and Clarke's generalized Jacobian are of practical interest only if we can compute at least some of their elements. Because of the lack of sharp calculus rules, this can be done only in few cases, depending on the structure of $r$. For instance, consider the class of piecewise continuously differentiable functions on ${\mathbb{R}}^{d}$, which is formally characterized by the following definition.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example II.3", "weight": 1.0} -->

We refer to for more details on the computation of elements in Clarke's generalized Jacobian for piecewise continuous functions and to Chapter 1 in for functions with different structures.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example II.3", "weight": 1.0} -->

The Newton method is not directly applicable to solve (6")) because of the nonsmoothness. The extension of the Newton method to nonsmooth equations dates back to at least and is generally known as the semismooth Newton method,. Similarly to the Newton method, instead of solving directly (6")), the semismooth Newton method solves a series of linear equations that locally approximate (6")), but the Jacobian matrix in the Newtonian iteration system is replaced by an element from Clarke's generalized Jacobian.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example II.3", "weight": 1.0} -->

In particular, the semismooth Newton method generates a sequence of iterates $\left\{ \theta_{k} \right\}$ where $\theta_{0} \in {\mathbb{R}}^{d}$ is the initial approximation of the root and, for any $k \geq 0$, $\theta_{k + 1}$ is computed as a solution of the linear equation ${{{r{(\theta_{k})}} + {J_{k}\left( {\theta_{k + 1} - \theta_{k}} \right)}} = 0},$ with $J_{k} \in {\partial{r{(\theta_{k})}}}$. When $J_{k}$ is nonsingular, then the iterate $\theta_{k + 1}$ can be computed in closed-form as follows

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example II.3", "weight": 1.0} -->

Under certain assumptions, the semismooth Newton method enjoys fast local quadratic convergence, but the cost per iteration with direct inversion is in the order of $\mathcal{O}{(d^{3})}$. In addition, as discussed, it may be difficult to obtain an element from Clarke's generalized Jacobian. These are some of the main motivations behind the design of different variants of the semismooth Newton method of the form

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example II.3", "weight": 1.0} -->

where $B_{k} \in {\mathbb{R}}^{d \times d}$. These variants, collectively known as semismooth Newton-type methods, can lead to lower computational costs while maintaining acceptable convergence rates. Clearly, if $B_{k} \in {\partial{r{(\theta_{k})}}}$, then we recover the semismooth Newton method. Among the most frequently used semismooth Newton-type methods, we recall the fixed-point iteration method, where $B_{k} = {\alpha_{k}I}$ with $\alpha_{k} \neq 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example II.3", "weight": 1.0} -->

Before proceeding with the formal characterization of the local convergence rate of semismooth Newton-type methods, we need to introduce the notions of strong semismoothness \[9, Subsection 1.4.2\] and CD-regularity \[9, Remark 1.65\].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark II.8", "weight": 1.0} -->

If at each iteration of the semismooth Newton method we select $J_{k}$ from $\partial_{B}{r{(\theta_{k})}}$, then the CD-regularity assumption can be replaced by the weaker assumption of BD-regularity of $r$ at $\theta^{\ast}$. The proof is analogous but instead of considering $J_{k} \in {\partial{r{(\theta_{k})}}}$ we consider $J_{k} \in {\partial_{B}{r{(\theta_{k})}}}$. See \[9, Remark 2.54\] for a more detailed discussion.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark II.8", "weight": 1.0} -->

1:Initialization: select θ0 ∈ ℝd, t o l ≥ 0 and set k = 0
3: select Bk ∈ ℝd × d nonsingular and compute

<!-- chunk {"id": "body-0031", "role": "body", "section": "SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING", "weight": 1.0} -->

In this section we formalize the connection of PI and VI with semismooth Newton-type methods. Such a connection has far-reaching consequences. By adopting this different perspective on DP methods, we can indeed deploy the well-established semismooth Newton-type theory to analyze existing DP methods and design novel ones, with favorable local contraction rates and efficient iterations.

<!-- chunk {"id": "body-0032", "role": "body", "section": "SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING", "weight": 1.0} -->

We start by looking at the Bellman equation (3")) as a nonlinear root finding problem, where ${r{(\theta)}} = {\theta - {T\theta}}$, $r:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ and the $s$-th component is

<!-- chunk {"id": "body-0033", "role": "body", "section": "SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING", "weight": 1.0} -->

We call $r$ the Bellman residual function.

<!-- chunk {"id": "body-0034", "role": "body", "section": "SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING", "weight": 1.0} -->

Clearly, every component is piecewise affine and therefore convex, because it is the sum of the identity map with the negative minimum of a finite collection of affine functions, one per admissible action. Consequently, the Bellman residual function is convex and continuous. Looking at the set of the admissible policies and based on the relation between $T$ and $T^{\pi}$, we can rewrite the Bellman residual function as follows

<!-- chunk {"id": "body-0035", "role": "body", "section": "SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING", "weight": 1.0} -->

where ${T^{\pi}\theta} = {g^{\pi} + {\gammaP^{\pi}\theta}}$ is an affine function of $\theta$. Consequently, the Bellman residual function is piecewise affine since it is continuous and there exist $|\Pi|$ affine selection functions $\left\{ {\theta - {T^{\pi}\theta}} \right\}_{\pi \in \Pi}$ such that ${r{(\theta)}} \in \left\{ {\theta - {T^{\pi}\theta}} \right\}_{\pi \in \Pi}$ for all $\theta \in {\mathbb{R}}^{n}$. Because of its piecewise affine structure, the Bellman residual function is globally Lipschitz continuous (Proposition 4.2.2 in ) and strongly semismooth everywhere (Proposition 7.4.7 in ).

<!-- chunk {"id": "body-0036", "role": "body", "section": "SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING", "weight": 1.0} -->

The following lemma characterizes the relation between greedy policies and active selection functions at $\theta \in {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Policy Iteration", "weight": 1.0} -->

We start by introducing an assumption on the sets of the spurious greedy policies, which excludes the presence of selection functions that are active but not essentially active.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption III.4", "weight": 1.0} -->

The following proposition characterizes the connection between PI and the semismooth Newton method.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Value Iteration", "weight": 1.0} -->

In light of the equivalence between PI and the semismooth Newton method to solve (15")), we investigate the connection between VI and semismooth Newton-type methods. In particular, with the following proposition we show that VI is a semismooth Newton-type method where the elements in Clarke's generalized Jacobian are approximated with the identity matrix.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C $\\alpha$-Value Iteration", "weight": 1.0} -->

Proposition III.6") shows that VI is also an instance of the fixed-point iteration method with $\alpha_{k} = 1$ for all $k$. The question that naturally arises is what do the iterates of the fixed-point iteration method correspond to if we allow $\alpha_{k} \neq 1$. In this spirit, we propose to use $\alphaI$ with $\alpha > 0$ to approximate the elements in Clarke's generalized Jacobian.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C $\\alpha$-Value Iteration", "weight": 1.0} -->

The following lemma characterizes the iterates of this method, which we call $\alpha$-Value Iteration ($\alpha$-VI).

<!-- chunk {"id": "body-0042", "role": "body", "section": "CONCLUSIONS & FUTURE WORK", "weight": 1.0} -->

We developed a unified convergence analysis for semismooth Newton-type methods based on the kappa condition. We then proved that PI and VI are semismooth Newton-type methods. In particular, Propositions III.5") and III.6") reveal that PI and VI sit at the two opposite sides in the spectrum of semismooth Newton-type methods: PI enjoys local quadratic contraction but its costs per iteration are demanding; instead, VI is based on a coarse approximation of the elements in Clarke's generalized Jacobian which allows to drastically reduce the costs per iteration at the price of downgrading the local quadratic convergence to a linear one. This connection has far-reaching consequences on the theoretical and algorithmic side. We can both deploy the semismooth Newton-type theory to analyze the local convergence properties of existing DP methods and, taking inspiration from the existing semismooth Newton-type methods, design novel DP algorithms that achieve different trade-offs of local contraction rate and costs per iteration. In this spirit, we proposed an extension of VI with global convergence guarantees and asymptotically faster contraction rate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "CONCLUSIONS & FUTURE WORK", "weight": 1.0} -->

This novel locally accelerated version of VI comes with negligible additional computational costs and leads to great improvement in performance, as demonstrated by our numerical experiments.

<!-- chunk {"id": "body-0044", "role": "body", "section": "CONCLUSIONS & FUTURE WORK", "weight": 1.0} -->

Finally, another promising future direction consists in formalizing and exploiting the connection between inexact semismooth Newton methods and optimistic policy iteration-type algorithms.
