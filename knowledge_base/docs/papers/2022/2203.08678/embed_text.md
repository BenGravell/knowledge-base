## INTRODUCTION

Approximate dynamic programming (ADP) is a powerful algorithmic strategy to handle stochastic sequential decision making problems arising in a wide range of applications, from control to games and resource allocation, to name a few. At the core of some of the biggest success stories of ADP is an approximate version of policy iteration. In particular, after an extensive offline training phase where an approximation of the optimal cost is produced, one iteration of an approximate version of policy iteration is performed (online learning). Empirical evidence suggests that this final step greatly enhances performance. In particular, Bertsekas in links these success stories to the equivalence between policy iteration and Newton's method.

The connection between policy iteration and Newton's method dates back to the late 60's. Puterman and Brumelle were among the first who exploited this connection to study the convergence properties of policy iteration for MDPs with continuous action spaces. More recently, Santos and Ruts exploited this connection to analyze the asymptotic convergence of policy iteration for the discretization of a specific class of MDPs with continuous spaces. Bertsekas in provides a graphical analysis of the connection between policy iteration and Newton's method. He then mathematically formalizes these visual insights by proving local quadratic convergence of policy iteration for Markov Decision Processes (MDPs) with finite state and action spaces. These theoretical results are corroborated by numerous computational examples which demonstrate that policy iteration achieves convergence in a remarkably small number of iterations even in presence of rounding errors and a large number of potential policies. We refer to for an extensive review of the related works.

In this work, we consider MDPs with finite state and action spaces and we formally show that policy iteration and value iteration are both instances of semismooth Newton-type methods. The main differences between our analysis and that of Bertsekas are that the latter only focus on policy iteration and does not deploy tools from generalized differentiation, but works in a neighborhood of the solution where the iterations can be expressed as the Newton iterations for some auxiliary continuously differentiable mapping. We then take this connection further by developing a novel version of value iteration inspired by the fixed-point iteration method. In particular, our main contributions are the following.

In Section II-B"), we develop a unified theoretical analysis for the local convergence of semismooth Newton-type methods based on the so-called kappa condition.

In Sections III-A") and III-B"), we formalize mathematically the connection of policy iteration and value iteration with semismooth Newton-type methods using tools from generalized differentiation and results from Section II"). We then discuss the significant algorithmic and theoretical implications of this connection.

In Section III-C"), we design a novel globally convergent and locally accelerated variant of value iteration with negligible additional computational cost per iteration and superior numerical performance.

Notation. In the following, we use $\parallel \cdot \parallel:{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}$ to denote an arbitrary vector norm, $\parallel \cdot \parallel:{\mathbb{R}}^{d \times d}\rightarrow{\mathbb{R}}$ for its induced matrix norm, $\mathcal{B}{(c,\delta)}$ for the Euclidean ball with center $c \in {\mathbb{R}}^{d}$ and radius $\delta > 0$, $\rho$ for the spectral radius of a matrix, $r'$ for the Jacobian operator of a differentiable function $r:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$, $\mathbf{1}_{d} = \begin{bmatrix} \end{bmatrix}^{\top} \in {\mathbb{R}}^{d}$ and $\text{cl}(\mathcal{T})$ and $\text{int}(\mathcal{T})$ for the closure and the interior of a set $\mathcal{T} \subseteq {\mathbb{R}}^{d}$, respectively.

## BACKGROUND

We consider infinite horizon discounted cost problems for MDPs $\left\{ \mathcal{S},\mathcal{A},P,g,\gamma \right\}$ comprising a finite state space $\mathcal{S} = \left\{ 1,\ldots,n \right\}$, a finite action space $\mathcal{A} = \left\{ 1,\ldots,m \right\}$, a transition probability function $P:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\lbrack 0,1\rbrack}}$ that defines the probability of ending in state $s'$ when applying action $a$ in state $s$, a stage-cost function $g:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ that associates to each state-action pair a bounded cost, and a discount factor $\gamma \in {}$. Throughout the paper, with a slight abuse of notation we use $\mathcal{A}{(s)}$ to denote the nonempty subset of actions that are allowed at state $s$, ${p_{ss'}{(a)}} = {P{(s,a,s')}}$ for the probability of transitioning to state $s'$ when the system is in state $s$ and action $a \in {\mathcal{A}{(s)}}$ is selected with ${\sum_{s' \in \mathcal{S}}{p_{ss'}{(a)}}} = 1$ for all $s \in \mathcal{S}$ and $a \in {\mathcal{A}{(s)}}$.

A deterministic stationary control policy $\pi:{\mathcal{S}\rightarrow\mathcal{A}}$ is a function that maps states to actions, with ${\pi{(s)}} \in {\mathcal{A}{(s)}}$. We use $\Pi$ to denote the set of all deterministic stationary control policies, from now on simply called policies. At step $t$ of the decision process under the policy $\pi \in \Pi$, the system is in some state $s_{t}$ and the action $a_{t} = {\pi{(s_{t})}}$ is applied. The discounted cost $\gamma^{t}g{(s_{t},a_{t})}$ is accrued and the system transitions to a state $s_{t + 1}$ according to the probability distribution $P{(s_{t},a_{t}, \cdot)}$. This process is repeated leading to the following cumulative discounted cost where $\left\{ s_{0},{\pi{(s_{0})}},s_{1},{\pi{(s_{1})}},\ldots,s_{t},{\pi{(s_{t})}},\ldots \right\}$ is the state-action sequence generated by the MDP under policy $\pi$ with initial state $s_{0}$, and the expected value is taken with respect to the corresponding probability measure over the space of sequences. The transition probability distributions induced by policy $\pi$ can be compactly represented by the rows of an $n \times n$ row-stochastic matrix $\left\lbrack P^{\pi} \right\rbrack_{ss'} = {p_{ss'}{({\pi{(s)}})}}$ for all ${s,s'} \in \mathcal{S}$ and the costs induced by policy $\pi$ by the vector $g^{\pi} = \begin{bmatrix} \end{bmatrix}^{\top} \in {\mathbb{R}}^{n}$. The optimal cost is defined as Any policy $\pi^{\ast} \in \Pi$ that attains the optimal cost is called an optimal policy. Notice that in (2")) we restrict our attention to stationary deterministic policies as in our setting there exists a policy in this class that attains $V^{\ast}$. The optimal cost admits a recursive definition known as the Bellman equation Equation (1")) admits an analogous recursive definition known as the Bellman equation associated with policy $\pi$. In the considered setting, the cost function associated with policy $\pi$ and the optimal cost function can be represented by $V^{\pi} \in {\mathbb{R}}^{n}$ and $V^{\ast} \in {\mathbb{R}}^{n}$, where the $s$-th element is given by (1")) and (2")) evaluated at $s$, respectively.

### II-A Dynamic Programming

Dynamic Programming (DP) comprises the methods for solving stochastic optimal control problems by solving the Bellman equation. Here we are interested in DP algorithms in the classes of value iteration (VI) and policy iteration (PI). Starting from Equation (3")), we define a nonsmooth mapping $T:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$, known as the Bellman operator, by An analogous linear operator $T^{\pi}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ can be defined for the Bellman equation associated with policy $\pi$ as Given the cost vector $V$, any policy $\pi$ such that is called greedy with respect to the cost $V$. It can be shown that the Bellman operator is contractive and, thanks to the Banach Theorem, admits a unique fixed point $V^{\ast}$. Moreover, the corresponding Picard-Banach iteration converges asymptotically to the fixed point from any initial value $V$, i.e.

This is at the core of VI, which repeatedly applies the $T$ operator starting from an arbitrary finite cost. The generated sequence linearly converges to $V^{\ast}$ with a $\gamma$-contraction rate.

An alternative method to solve Equation (3")) is PI (Algorithm 1")). With PI, we start from an arbitrary initial policy and alternate policy evaluation (step 3) and policy improvement (step 4) until convergence. The policy evaluation step at iteration $k$ computes the cost $V^{\pi_{k}}$ associated with the current policy $\pi_{k}$. This requires the solution of a system with $n$ linear equations, which is generally computationally demanding for MDPs with large state spaces. The policy is then updated by extracting a greedy policy associated with $V^{\pi_{k}}$ in the policy improvement step. Unlike VI, PI converges in a finite number of iterations since the policy, and therefore also its cost, are improved at each iteration and since, by the finiteness of $\mathcal{S}$ and $\mathcal{A}$, there only exists a finite number of policies. It is nonetheless important to characterize its convergence rate and asymptotic behavior since, for large state and action spaces, the number of iterations could be prohibitive (exponential in $n$ and $m$). By exploiting the properties of the Bellman operator, we can show that PI is globally $\gamma$-contractive, which is similar to VI. Extensive empirical evidence, however, suggests that PI has superior convergence properties and generally requires considerably fewer iterations than VI. From a computational viewpoint, the per-iteration costs of PI with direct inversion amount to $\mathcal{O}{({n^{3} + {m \cdot n^{2}}})}$ versus the $\mathcal{O}{({m \cdot n^{2}})}$ of VI.

1:Initialization: select an arbitrary initial policy π0 and set k = 0 2:while cost has not converged do 4: $\pi_{k + 1} = \overset{\sim}{\pi}$ with $\overset{\sim}{\pi} \in {\text{GreedyPolicy}{(V^{\pi_{k}})}}$ according to Algorithm 1 Exact Policy Iteration

### II-B Generalized Differentiation & Semismooth Newton-Type Methods

Consider the following nonlinear root finding problem where $r:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is a locally Lipschitz-continuous vector-valued function. A vector $\theta^{\ast} \in {\mathbb{R}}^{d}$ that verifies (6")) is called root or solution of the nonlinear equation (6")). In general, we can not rely on smooth optimization methods to solve (6")) since $r$ can be nonsmooth, so its Jacobian ${r'{(\theta)}} \in {\mathbb{R}}^{d \times d}$ might not exist. We therefore need to introduce some notions of generalized differentiability from nonsmooth analysis, such as the B-differential and Clarke's generalized Jacobian. Since $r$ is a locally Lipschitz-continuous map, the Rademacher Theorem implies that it is differentiable almost everywhere and we denote with $\mathcal{M}_{r}$ the set of all points where $r$ is differentiable. Another fundamental implication of the Rademacher Theorem is the definition of the B-differential of $r$ at $\theta \in {\mathbb{R}}^{d}$ as the set We denote with $\partial{r{(\theta)}}$ Clarke's generalized Jacobian of $r$ at $\theta \in {\mathbb{R}}^{d}$, which is defined as the convex hull of $\partial_{B}{r{(\theta)}}$. Consequently, ${\partial_{B}{r{(\theta)}}} \subseteq {\partial{r{(\theta)}}}$. These sets are always nonempty when evaluated at points where the function is Lipschitz continuous \[9, Proposition 1.51\]. If $r$ is continuously differentiable at $\theta$, then ${\partial{r{(\theta)}}} = {\partial_{B}{r{(\theta)}}} = \left\{ {r'{(\theta)}} \right\}$. Otherwise, $\partial_{B}{r{(\theta)}}$ and, consequently, $\partial{r{(\theta)}}$ are not necessarily singletons.

The B-differential and Clarke's generalized Jacobian are of practical interest only if we can compute at least some of their elements. Because of the lack of sharp calculus rules, this can be done only in few cases, depending on the structure of $r$. For instance, consider the class of piecewise continuously differentiable functions on ${\mathbb{R}}^{d}$, which is formally characterized by the following definition.

### Definition II.1 (PC^1^ functions)

Let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{o}}$ be a continuous vector-valued function and $n_{p}$ be some positive integer. The function $f$ is said to be piecewise continuously differentiable of order $1$ (PC^1^) if there exist finitely many continuously differentiable functions $\left\{ f_{i} \right\}_{i = 1}^{n_{p}}$ on ${\mathbb{R}}^{d}$, called selection functions, such that ${f{(\theta)}} \in \left\{ {f_{i}{(\theta)}} \right\}_{i = 1}^{n_{p}}$ for all $\theta \in {\mathbb{R}}^{d}$. In addition, $f_{i}$ is active at $\overline{\theta} \in {\mathbb{R}}^{n}$ if ${f{(\overline{\theta})}} = {f_{i}{(\overline{\theta})}}$ and essentially active if $\overline{\theta} \in {\text{cl}{({\text{int}{({\{{\theta \in {\mathbb{R}}^{d}}:{{f{(\theta)}} = {f_{i}{(\theta)}}}\}})}})}}$.

We denote with $\mathcal{F}_{f}{(\overline{\theta})}$ the collection of essentially active functions at $\overline{\theta}$. Piecewise affine functions are an example of PC^1^ functions with affine selection functions and are particularly relevant in the context of DP as it will be discussed in Section III").

The following proposition (Lemma 2.10 in ) gives a representation of the B-differential for PC^1^ functions. This representation can be used to determine a $J \in {\partial_{B}{f{(\theta)}}}$ in cases where we can compute the Jacobian matrix of at least one of the essentially active selection functions at $\theta \in {\mathbb{R}}^{d}$.

### Proposition II.2

Let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{o}}$ be a PC^1^ function. The B-differential of $f$ at $\theta \in {\mathbb{R}}^{d}$ is ${{\partial_{B}{f{(\theta)}}} = \left\{ {f_{i}'{(\theta)}}:{f_{i} \in {\mathcal{F}_{f}{(\theta)}}} \right\}}.$

### Example II.3

Consider the following piecewise affine function: ${f{(\theta)}} = {{2\theta} - 5}$ if $\theta > 5$, ${f{(\theta)}} = \theta$ if $\theta = 5$ and ${f{(\theta)}} = {{- {2\theta}} + 15}$ if $\theta < 5$. Then ${\partial_{B}{f{}}} = \left\{ 2,{- 2} \right\}$ since ${\text{int}{({\{{\theta \in {\mathbb{R}}}:{{f{(\theta)}} = \theta}\}})}} = \varnothing$ and ${\partial_{B}{f{(\theta)}}} = {f'{(\theta)}}$ for all $\theta \in {{\mathbb{R}} \smallsetminus \left\{ 5 \right\}}$.

We refer to for more details on the computation of elements in Clarke's generalized Jacobian for piecewise continuous functions and to Chapter 1 in for functions with different structures.

The Newton method is not directly applicable to solve (6")) because of the nonsmoothness. The extension of the Newton method to nonsmooth equations dates back to at least and is generally known as the semismooth Newton method,. Similarly to the Newton method, instead of solving directly (6")), the semismooth Newton method solves a series of linear equations that locally approximate (6")), but the Jacobian matrix in the Newtonian iteration system is replaced by an element from Clarke's generalized Jacobian. In particular, the semismooth Newton method generates a sequence of iterates $\left\{ \theta_{k} \right\}$ where $\theta_{0} \in {\mathbb{R}}^{d}$ is the initial approximation of the root and, for any $k \geq 0$, $\theta_{k + 1}$ is computed as a solution of the linear equation ${{{r{(\theta_{k})}} + {J_{k}\left({\theta_{k + 1} - \theta_{k}} \right)}} = 0},$ with $J_{k} \in {\partial{r{(\theta_{k})}}}$. When $J_{k}$ is nonsingular, then the iterate $\theta_{k + 1}$ can be computed in closed-form as follows Under certain assumptions, the semismooth Newton method enjoys fast local quadratic convergence, but the cost per iteration with direct inversion is in the order of $\mathcal{O}{(d^{3})}$. In addition, as discussed, it may be difficult to obtain an element from Clarke's generalized Jacobian. These are some of the main motivations behind the design of different variants of the semismooth Newton method of the form where $B_{k} \in {\mathbb{R}}^{d \times d}$. These variants, collectively known as semismooth Newton-type methods, can lead to lower computational costs while maintaining acceptable convergence rates. Clearly, if $B_{k} \in {\partial{r{(\theta_{k})}}}$, then we recover the semismooth Newton method. Among the most frequently used semismooth Newton-type methods, we recall the fixed-point iteration method, where $B_{k} = {\alpha_{k}I}$ with $\alpha_{k} \neq 0$.

Before proceeding with the formal characterization of the local convergence rate of semismooth Newton-type methods, we need to introduce the notions of strong semismoothness \[9, Subsection 1.4.2\] and CD-regularity \[9, Remark 1.65\].

### Definition II.4 (strong semismoothness)

A function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{o}}$ is strongly semismooth at $\theta \in {\mathbb{R}}^{d}$ if it is locally Lipschitz-continuous at $\theta$, directionally differentiable at $\theta$ in every direction, and the following estimate holds as $\xi \in {\mathbb{R}}^{d}$ tends to zero

### Definition II.5 (CD/BD-regularity)

A function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{o}}$ is CD-regular (BD-regular) at $\theta \in {\mathbb{R}}^{d}$ if each matrix $J \in {\partial{f{(\theta)}}}$ ($J \in {\partial_{B}{f{(\theta)}}}$) is nonsingular.

The function in Example II.3") is strongly semismooth and BD-regular everywhere, but not CD-regular at $\theta = 5$, since $0 \in {\partial{f{}}}$.

The following theorem characterizes the local contraction of a semismooth Newton-type sequence generated by Algorithm 2"). Similar a-posteriori results based on perturbation analysis can be found .

### Theorem II.6

Let $r:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ be strongly semismooth at $\theta^{\ast} \in {\mathbb{R}}^{d}$, $L > 0$ and $\kappa \in {\lbrack 0,1)}$ a constant. Then the following statements hold.

For any nonsingular matrix $B \in {\mathbb{R}}^{d \times d}$ such that ${\| B^{- 1}\|} \leq L$ and ${\exists J} \in {\partial{r{(\theta)}}}$ for which ${\|{B^{- 1}\left({B - J} \right)}\|} \leq \kappa$, then There exist an open neighborhood of $\theta^{\ast}$ such that, for any $\theta_{0}$ in the neighborhood and any sequence of nonsingular matrices $\left\{ B_{k} \right\} \subseteq {\mathbb{R}}^{d \times d}$ such that, for all $k$, ${\| B_{k}^{- 1}\|} \leq L$ and ${\exists J_{k}} \in {\partial{r{(\theta_{k})}}}$ for which the kappa condition is verified, the sequence $\left\{ \theta_{k} \right\} \subseteq {\mathbb{R}}^{d}$ generated by Algorithm 2") converges to $\theta^{\ast}$ and

### Proof

We start by proving the first assertion. Since ${r{(\theta^{\ast})}} = 0$, We now add and subtract the term $B^{- 1}J{({\theta - \theta^{\ast}})}$, where $J \in {\partial{r{(\theta)}}}$ such that ${\|{B^{- 1}\left({B - J} \right)}\|} \leq \kappa$ By taking the norm on both sides of Equation (12")), we obtain where $(a)$ follows from the triangle inequality, $(b)$ from the sub-multiplicativity of the norm and $(c)$ from the strong semismoothness of $r$. The final result follows from that fact that ${\|{B^{- 1}\left({B - J} \right)}\|} \leq \kappa$. For $\theta_{k} \in {\mathbb{R}}^{d}$, Equation (8")) has a unique solution $\theta_{k + 1}$ given by (14")). In addition, from (9")) it follows that for any $q \in {(\kappa,1)}$, there exists $\delta > 0$ such that the inclusion $\theta_{k} \in {\mathcal{B}{(\theta^{\ast},\delta)}}$ implies that ${\|{\theta_{k + 1} - \theta^{\ast}}\|} \leq {q{\|{\theta_{k} - \theta^{\ast}}\|}}$ and therefore $\theta_{k + 1} \in {\mathcal{B}{(\theta^{\ast},\delta)}}$. It follows that any starting point $\theta_{0} \in {\mathcal{B}{(\theta^{\ast},\delta)}}$ uniquely deﬁnes a speciﬁc sequence of iterates $\left\{ \theta_{k} \right\}$ of Algorithm 2"); this sequence is contained in $\mathcal{B}{(\theta^{\ast},\delta)}$ and converges to $\theta^{\ast}$. Finally, starting from (13")) and by exploiting (14")) and the kappa condition, we obtain (11")). ∎∎ Theorem II.6") shows that the local convergence rate of semismooth Newton-type methods strongly depends on the choice of $\left\{ B_{k} \right\}$. In particular, we obtain quadratic convergence if $\kappa = 0$, superlinear convergence if $\kappa_{k}\rightarrow 0$ as $k\rightarrow\infty$ and linear convergence if $\kappa_{k} = \kappa$ for all $k$ with $\kappa \in {}$.

The following corollary characterizes the local convergence of the exact semismooth Newton method (see also Theorem 2.42 in ).

### Corollary II.7

Let $r$ be strongly semismooth and CD-regular at $\theta^{\ast}$. Provided that $\theta_{0}$ is close enough to $\theta^{\ast}$, the sequence $\left\{ \theta_{k} \right\}$ generated by the semismooth Newton method iteration (7")) with starting point $\theta_{0}$ converges to $\theta^{\ast}$ according to

### Proof

From Proposition 1.51 and Lemma A.6 in it follows that there exists a neighborhood $U$ of $\theta^{\ast}$ and a finite constant $L > 0$ such that $J$ is nonsingular and ${\| J^{- 1}\|} \leq L$ for all $J \in {\partial{r{(\theta)}}}$ and for all $\theta \in U$. The final result follows from Theorem II.6") by setting $B_{k} = J_{k}$ and considering $\theta_{0} \in {\mathcal{B}{(\theta^{\ast},\delta)}}$ with $\delta$ sufficiently small such that ${\mathcal{B}{(\theta^{\ast},\delta)}} \subset U$. ∎∎

### Remark II.8

If at each iteration of the semismooth Newton method we select $J_{k}$ from $\partial_{B}{r{(\theta_{k})}}$, then the CD-regularity assumption can be replaced by the weaker assumption of BD-regularity of $r$ at $\theta^{\ast}$. The proof is analogous but instead of considering $J_{k} \in {\partial{r{(\theta_{k})}}}$ we consider $J_{k} \in {\partial_{B}{r{(\theta_{k})}}}$. See \[9, Remark 2.54\] for a more detailed discussion.

1:Initialization: select θ0 ∈ ℝd, t o l ≥ 0 and set k = 0 3: select Bk ∈ ℝd × d nonsingular and compute Algorithm 2 Semismooth Newton-Type Method

## SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING

In this section we formalize the connection of PI and VI with semismooth Newton-type methods. Such a connection has far-reaching consequences. By adopting this different perspective on DP methods, we can indeed deploy the well-established semismooth Newton-type theory to analyze existing DP methods and design novel ones, with favorable local contraction rates and efficient iterations.

We start by looking at the Bellman equation (3")) as a nonlinear root finding problem, where ${r{(\theta)}} = {\theta - {T\theta}}$, $r:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ and the $s$-th component is We call $r$ the Bellman residual function.

Figure 1: Visualization of the Bellman operator T and corresponding Bellman equation for a 1-dimensional case. The optimal cost V* corresponds to the intersection point of the graph of T V with the 45 degree line. Bertsekas in proves local quadratic convergence of PI for a region that is included in the segments within the curly brackets.

Figure 2: Visualization of the region of attraction for the case of Figure 1 under our analysis. As we can clearly see from this graphical representation, the region of attraction from our analysis can be effectively larger than the one considered .

Clearly, every component is piecewise affine and therefore convex, because it is the sum of the identity map with the negative minimum of a finite collection of affine functions, one per admissible action. Consequently, the Bellman residual function is convex and continuous. Looking at the set of the admissible policies and based on the relation between $T$ and $T^{\pi}$, we can rewrite the Bellman residual function as follows where ${T^{\pi}\theta} = {g^{\pi} + {\gammaP^{\pi}\theta}}$ is an affine function of $\theta$. Consequently, the Bellman residual function is piecewise affine since it is continuous and there exist $|\Pi|$ affine selection functions $\left\{ {\theta - {T^{\pi}\theta}} \right\}_{\pi \in \Pi}$ such that ${r{(\theta)}} \in \left\{ {\theta - {T^{\pi}\theta}} \right\}_{\pi \in \Pi}$ for all $\theta \in {\mathbb{R}}^{n}$. Because of its piecewise affine structure, the Bellman residual function is globally Lipschitz continuous (Proposition 4.2.2 in) and strongly semismooth everywhere (Proposition 7.4.7 in).

The following lemma characterizes the relation between greedy policies and active selection functions at $\theta \in {\mathbb{R}}^{n}$.

### Lemma III.1

Let ${\overset{\sim}{\Pi}}_{\theta} \subseteq \Pi$ denote the set of the greedy policies with respect to the cost-vector $\theta \in {\mathbb{R}}^{n}$. Then ${r{(\theta)}} = {\theta - {T^{\pi}\theta}}$ for all $\pi \in {\overset{\sim}{\Pi}}_{\theta}$. In other terms, $\left\{ {\theta - {T^{\pi}\theta}} \right\}_{\pi \in {\overset{\sim}{\Pi}}_{\theta}}$ is the collection of the active selection functions of $r$ at $\theta$.

### Proof

The proof follows directly from the definition of greedy policy (4")). In particular, a policy $\pi$ is greedy with respect to the cost-vector $\theta \in {\mathbb{R}}^{n}$ if ${T^{\pi}\theta} = {T\theta}$. ∎∎ The next definition introduces the concept of spurious greedy policy, which will later be used together with Proposition II.2") to characterize the B-differential of the Bellman residual function.

### Definition III.2 (spurious greedy policy)

Let $\overline{\theta} \in {\mathbb{R}}^{n}$. $\pi \in {\overset{\sim}{\Pi}}_{\overline{\theta}}$ is a spurious greedy policy for the cost-vector $\overline{\theta}$ if ${{\text{int}{({\{{\theta \in {\mathbb{R}}^{n}}:{{r{(\theta)}} = {\theta - {T^{\pi}\theta}}}\}})}} = \varnothing}.$ In other terms, a greedy policy $\pi \in {\overset{\sim}{\Pi}}_{\theta}$ is spurious if there exist $s \in \mathcal{S}$ for which for all $\epsilon > 0$, $\pi{(s)}$ is not greedy with respect to any ${\overset{\sim}{\theta}}_{s} \neq \theta_{s}$ with ${|{\theta_{s} - {\overset{\sim}{\theta}}_{s}}|} \leq \epsilon$. We denote with ${\overset{\sim}{\Pi}}_{\theta}^{S}$ the subset of ${\overset{\sim}{\Pi}}_{\theta}$ comprising the spurious greedy policies.

The next proposition characterizes the B-differential of the Bellman residual function.

### Proposition III.3

Let $r:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ be the Bellman residual function. The B-differential of $r$ at $\theta \in {\mathbb{R}}^{n}$ is the set In addition, $r$ is globally CD-regular.

### Proof

From the definition of essentially active selection functions and spurious greedy policies, it follows that ${\mathcal{F}_{r}{(\theta)}} = \left\{ {\theta - {T^{\pi}\theta}} \middle| {{\forall\pi} \in {{\overset{\sim}{\Pi}}_{\theta} \smallsetminus {\overset{\sim}{\Pi}}_{\theta}^{S}}} \right\}$. From Proposition II.2") and since $\left( {\theta - {T^{\pi}\theta}} \right)' = {I - {\gammaP^{\pi}}}$ for any $\pi \in \Pi$, we conclude that the B-differential of $r$ is given by the set in (16")). Since $P^{\pi}$ is a row-stochastic matrix, its eigenvalues lie within the unit circle of the complex plane. Thus $I - {\gammaP^{\pi}}$ with $\gamma \in {}$ has no eigenvalue equal to zero. We can therefore conclude that all the matrices in the B-differential of $r$ are nonsingular and therefore $r$ is BD-regular. Finally, since the convex combination of row stochastic matrices is a row stochastic matrix, we can conclude that $r$ is CD-regular. ∎∎

### III-A Policy Iteration

We start by introducing an assumption on the sets of the spurious greedy policies, which excludes the presence of selection functions that are active but not essentially active.

### Assumption III.4

We assume that ${\overset{\sim}{\Pi}}_{\theta}^{S} = \varnothing$ for all $\theta \in {\mathbb{R}}^{n}$.

The following proposition characterizes the connection between PI and the semismooth Newton method.

### Proposition III.5

Under Assumption III.4"), PI is an instance of the semismooth Newton method to solve the Bellman residual function (15")). Hence, the local contraction is quadratic.

### Proof

Let $\left\{ \theta_{k}^{\text{PI}} \right\}$ denote the iterates of Algorithm 1"). We show by induction that, through an appropriate choice of $J_{k}$, we can generate iterates $\left\{ \theta_{k}^{\text{N}} \right\}$ of the semismooth Newton method for the Bellman residual function such that $\theta_{k}^{\text{PI}} = \theta_{k}^{\text{N}}$ for all $k$. Assume that $\theta_{k}^{\text{PI}} = \theta_{k}^{\text{N}} = \theta_{k}$ and let $\pi_{k + 1} \in {\overset{\sim}{\Pi}}_{\theta_{k}}$ be the greedy policy selected by PI at the $k$-th policy improvement step. Then, from Algorithm 1"), it follows that ${\theta_{k + 1}^{\text{PI}} = {{({I - {\gammaP^{\pi_{k + 1}}}})}^{- 1}g^{\pi_{k + 1}}}}.$ From Assumption III.4") and Proposition III.3"), we have that $I - {\gammaP^{\pi_{k + 1}}}$ is invertible and belongs to $\partial_{B}{r{(\theta_{k})}}$. Recall in addition that, from the definition of greedy policy, ${T^{\pi_{k + 1}}\theta_{k}} = {T\theta_{k}}$. Therefore, the $({k + 1})$-th semismooth Newton iterate with $J_{k} = {I - {\gammaP^{\pi_{k + 1}}}}$ is The quadratic local contraction follows from Corollary II.7"). ∎∎ The theoretical results of Proposition III.5") are corroborated by extensive empirical evidence that suggests that, in practice, PI leads to faster convergence in terms of number of iterations than VI. Despite its simplicity, the consequences of Proposition III.5") are far-reaching, especially in light of the results in Theorem II.6"). We can develop novel DP methods in the spirit of semismooth Newton-type methods, where the elements in the B-differential are approximated with non-singular matrices that verify the kappa condition (10")). Assumption III.4") allows to directly employ Proposition II.2") and could be further relaxed by considering only the iterates $\theta_{k}$ for $k \geq 0$. In addition, despite its technicality and limited intuitiveness, empirical evidence seems to suggests that it is realistic to assume that ${\overset{\sim}{\Pi}}_{\theta_{k}}^{S} = \varnothing$ for all $k \geq 0$.

By adopting the piecewise smooth Newton perspective (see Theorem 7.2.15 in ) we can recover similar results as in Proposition III.5") without the need for Assumption III.4"). In particular, $J$ is selected in the larger set ${\hat{\partial}r{(\theta)}} \supseteq {\partial_{B}{r{(\theta)}}}$ that comprises the Jacobians of all the active selection functions at $\theta$. Clearly $\hat{\partial}r{(\theta)}$ also contains the Jacobians of the active selection functions associated with the spurious greedy policies. With this approach, Assumption III.4") is replaced by the requirement that $\hat{\partial}r{(\theta)}$ is a strong Newton approximation scheme (see Definition 7.2.2 in ).

Also the analysis of Bertsekas in leads to similar conclusions on the local convergence of PI. Unlike our analysis though, Bertsekas considers a neighborhood of the root where the active selection functions are a subset of those active at the root. This allows to remap the iterations to the Newton iterations applied to a system of differentiable equations that has the same fixed point. The downside of this approach is that the effective region of attraction is potentially much larger than the one considered for the technical proof. A clear example is depicted in Figures 1") and 2").

### III-B Value Iteration

In light of the equivalence between PI and the semismooth Newton method to solve (15")), we investigate the connection between VI and semismooth Newton-type methods. In particular, with the following proposition we show that VI is a semismooth Newton-type method where the elements in Clarke's generalized Jacobian are approximated with the identity matrix.

### Proposition III.6

VI is a semismooth Newton-type method to solve the Bellman residual function with $\left\{ B_{k} \right\} = \left\{ I \right\}$.

### Proof

Let $\theta_{k + 1}^{\text{VI}}$ and $\theta_{k + 1}^{\text{N-type}}$ denote the $({k + 1})$-th iterate of VI and the semismooth Newton-type method with $\left\{ B_{k} \right\} = \left\{ I \right\}$, respectively. Assume that $\theta_{k}^{\text{VI}} = \theta_{k}^{\text{N-type}} = \theta_{k}$. Then, from the definition of VI, it follows that ${\theta_{k + 1}^{\text{VI}} = {T\theta_{k}}}.$ From the definition of semismooth Newton-type iterate in (14")) and with the specific choice of $B_{k} = I$, we obtain that ${\theta_{k + 1}^{\text{N-type}} = {\theta_{k} - {I^{- 1}r{(\theta_{k})}}} = {\theta_{k} - \left({\theta_{k} - {T\theta_{k}}} \right)} = {T\theta_{k}} = \theta_{k + 1}^{\text{VI}}}.\blacksquare$ ∎ The classical DP convergence analysis of VI based on the properties of the Bellman operator indicates that VI enjoys a global linear rate of convergence with a $\gamma$-contraction rate. In light of this novel connection between VI and the fixed-point iteration method, we can adopt the semismooth Newton-type theory perspective to study the local convergence of VI. In particular, from the results of Theorem II.6"), we obtain that VI has a local linear contraction rate given by the discount factor as ${\|{I^{- 1}\left({I - \left({I - {\gammaP^{\pi}}} \right)} \right)}\|}_{\infty} = {\gamma{\| P^{\pi}\|}_{\infty}} = \gamma < 1$ for all ${\pi \in \Pi}.$

### III-C $\alpha$-Value Iteration

Proposition III.6") shows that VI is also an instance of the fixed-point iteration method with $\alpha_{k} = 1$ for all $k$. The question that naturally arises is what do the iterates of the fixed-point iteration method correspond to if we allow $\alpha_{k} \neq 1$. In this spirit, we propose to use $\alphaI$ with $\alpha > 0$ to approximate the elements in Clarke's generalized Jacobian.

The following lemma characterizes the iterates of this method, which we call $\alpha$-Value Iteration ($\alpha$-VI).

### Lemma III.7

Consider the semismooth Newton-type iteration for the Bellman residual function with $B_{k} = {\alphaI}$ and $\alpha > 0$. Then

### Proof

We start from the semismooth Newton-type iteration in (14")) and set $B_{k} = {\alphaI}$. The result trivially follows from the definition of the Bellman residual function as ${\theta_{k + 1} = {\theta_{k} - {\frac{1}{\alpha}{({\theta_{k} - {T\theta_{k}}})}}} = {{\frac{\alpha - 1}{\alpha}\theta_{k}} + {\frac{1}{\alpha}T\theta_{k}}}}.\blacksquare$ ∎ Starting from Equation (17")), we can define the operator ${T_{\alpha} = {{\frac{\alpha - 1}{\alpha}I} + {\frac{1}{\alpha}T}}},$ where $I$ is the indentity map and $T$ is the Bellman operator. Notice that when $\alpha = 1$ we recover the Bellman operator and therefore $1$-VI is simply VI. In the following, we are interested in studying the global and local convergence of $\alpha$-VI. We start by studying the properties of the $T_{\alpha}$ operator and its fixed-points.

Figure 3: Comparison of PI and α-VI for different values of α. For the benchmark, we consider a randomly generated MDP with 500 states, 10 actions and γ = 0.4. In particular, the state transition matrices and the cost vectors are generated by sampling the values from a uniform distribution on the interval 0, 1).

### Proposition III.8

For any ${\theta,\overline{\theta}} \in {\mathbb{R}}^{n}$ and $\alpha > \frac{1 + \gamma}{2}$, where $\beta = {\frac{|{\alpha - 1}|}{\alpha} + \frac{\gamma}{\alpha}} < 1$. In addition, the optimal cost $\theta^{\ast}$ is the unique fixed-point of $T_{\alpha}$.

### Proof

We start by showing that, if $\alpha > \frac{1 + \gamma}{2}$, the operator is $\beta$-contractive with respect to the infinity norm. For any ${\theta,\overline{\theta}} \in {\mathbb{R}}^{n}$ where $(a)$ follows from the triangle inequality and $(b)$ from the fact that the Bellman operator is $\gamma$-contractive in the inifinity norm. In order for $T_{\alpha}$ to be contractive, we need $\left({\left| \frac{\alpha - 1}{\alpha} \right| + \frac{\gamma}{|\alpha|}} \right) < 1$. For $\alpha \geq 1$, since $\gamma \in {}$, $T_{\alpha}$ is contractive with rate ${{({\alpha - 1})}/\alpha} + {\gamma/\alpha}$. For $\alpha \in {}$, ${\left| \frac{\alpha - 1}{\alpha} \right| + \frac{\gamma}{|\alpha|}} = {\frac{1 - \alpha}{\alpha} + \frac{\gamma}{\alpha}}$ and ${\frac{1 - \alpha}{\alpha} + \frac{\gamma}{\alpha}} < 1$ if and only if $\alpha > \frac{1 + \gamma}{2}$. For $\alpha < 0$, ${\left| \frac{\alpha - 1}{\alpha} \right| + \frac{\gamma}{|\alpha|}} = {\frac{\alpha - 1}{\alpha} - \frac{\gamma}{\alpha}}$ and the inequality ${\frac{\alpha - 1}{\alpha} - \frac{\gamma}{\alpha}} < 1$ is never satisfied since $\gamma \in {}$. We can therefore conclude that if $\alpha > \frac{1 + \gamma}{2}$ then $T_{\alpha}$ is $\beta$-contractive in the infinity norm with $\beta = {{{|{\alpha - 1}|}/\alpha} + {\gamma/\alpha}}$. To verify that $\theta^{\ast}$ is a fixed-point of $T_{\alpha}$, we exploit the definition of $T_{\alpha}$ and the fact that $\theta^{\ast}$ is the unique fixed-point of $T$. In particular, ${{T_{\alpha}\theta^{\ast}} = {{\frac{\alpha - 1}{\alpha}\theta^{\ast}} + {\frac{1}{\alpha}T\theta^{\ast}}} = {{\frac{\alpha - 1}{\alpha}\theta^{\ast}} + {\frac{1}{\alpha}\theta^{\ast}}} = \theta^{\ast}}.$ Uniqueness follows directly from the Banach Theorem \[. ∎∎ The main implication of Proposition III.8") is that, if $\alpha > {{({1 + \gamma})}/2}$, then $\alpha$-VI converges globally to the optimal cost $\theta^{\ast}$ with linear rate $\beta$. The following lemmas characterize the values of $\alpha$ for which $T_{\alpha}$ is a monotone operator and its shift-invariance property, respectively.

### Lemma III.9 (monotonicity)

Let $\alpha \geq 1$. For ${\theta,\overline{\theta}} \in {\mathbb{R}}^{n}$ if $\theta \leq \overline{\theta}$, then ${T_{\alpha}\theta} \leq {T_{\alpha}\overline{\theta}}$.

### Proof

Since $\alpha \geq 1$, $\theta \leq \overline{\theta}$ and $T$ is monotone, it follows that ${{T_{\alpha}\theta} = {{\frac{\alpha - 1}{\alpha}\theta} + {\frac{1}{\alpha}T\theta}} \leq {{\frac{\alpha - 1}{\alpha}\overline{\theta}} + {\frac{1}{\alpha}T\overline{\theta}}} = {T_{\alpha}\overline{\theta}}}.\blacksquare$ ∎

### Lemma III.10 (shift-invariance)

For any $\theta \in {\mathbb{R}}^{n}$ and $b \in {\mathbb{R}}$, then ${T_{\alpha}^{k}\left( {\theta + {b\mathbf{1}_{n}}} \right)} = {{T_{\alpha}^{k}\theta} + {\left( \frac{{\alpha - 1} + \gamma}{\alpha} \right)^{k}b\mathbf{1}_{n}}}$ for $k = {1,2,\ldots}$.

### Proof

Since $T$ is shift-invariant, then The final result follows from repeatedly applying the $T_{\alpha}$ operator. ∎∎ Results similar to Proposition III.8") can be derived for the local contraction rate by considering Theorem II.6") and evaluating the kappa condition with the infinity norm. Unfortunately, using this type of analysis it is not possible to conclude that $\alpha$-VI improves over VI in terms of convergence rate. Instead, we introduce the following proposition, which analyses the asymptotic rate of convergence of $\alpha$-VI via local stability analysis of nonlinear systems. For the sake of simplicity and interpretability, we consider a simplified setting in which the transition probability matrix at the solution has only real and positive eigenvalues. Notice that similar considerations can be made in a more general setting. This approach provides a tighter bound on the local rate of convergence, but is only applicable in a neighborhood of the root where the Bellman residual function is continuously differentiable.

### Proposition III.11 (asymptotic local contraction rate)

Assume that $r{(\theta^{\ast})}$ is continuously differentiable in a neighborhood of $\theta^{\ast}$ and that $P^{\pi^{\ast}}$ has only real and positive eigenvalues. Let $\alpha \in {({1/{({1 + \gamma})}},1)}$ and $\alpha$-VI converges linearly to $\theta^{\ast}$ with asymptotic contraction rate $\overset{\sim}{\beta} < \gamma$.

### Proof

We start by linearizing $\theta_{k + 1} = {T_{\alpha}\theta_{k}}$ at $\theta^{\ast}$ via the first-order Taylor expansion Since $\theta^{\ast} = {T_{\alpha}\theta^{\ast}}$ and ${({T_{\alpha}\theta^{\ast}})}' = {{\frac{({\alpha - 1})}{\alpha}I} + {\frac{\gamma}{\alpha}P^{\pi^{\ast}}}}$ for any optimal policy $\pi^{\ast}$, then Therefore the asymptotic convergence rate is determined by the spectral radius of $I - {\frac{1}{\alpha}\left({I - {\gammaP^{\pi^{\ast}}}} \right)}$. In particular, since ${\rho\left({I - {\frac{1}{\alpha}\left({I - {\gammaP^{\pi^{\ast}}}} \right)}} \right)} \leq {\max\left\{ \left| {1 - \frac{1 - \gamma}{\alpha}} \right|,\left| {1 - \frac{1}{\alpha}} \right| \right\}}$, we study different cases based on the values of $\alpha$. When $\alpha \geq {1 - {\gamma/2}}$, then ${\max\left\{ \left| {1 - \frac{1 - \gamma}{\alpha}} \right|,\left| {1 - \frac{1}{\alpha}} \right| \right\}} = {1 - \frac{1 - \gamma}{\alpha}}$. In this case we get a contraction for any $\alpha \geq {1 - {\gamma/2}}$ since the inequality ${1 - \frac{1 - \gamma}{\alpha}} < 1$ is verified for any $\alpha > 0$. In addition, if $\alpha \in {\lbrack{1 - {\gamma/2}},1\rbrack}$, then we improve over the rate of VI since ${1 - \frac{1 - \gamma}{\alpha}} \leq \gamma$. For $\alpha < {1 - {\gamma/2}}$, ${\max\left\{ \left| {1 - \frac{1 - \gamma}{\alpha}} \right|,\left| {1 - \frac{1}{\alpha}} \right| \right\}} = {\frac{1}{\alpha} - 1}$ and we get a contraction if $\alpha \in {({1/2},{1 - {\gamma/2}})}$. In addition, if $\alpha \in {\lbrack{1/{({1 + \gamma})}},{1 - {\gamma/2}})}$, then ${\frac{1}{\alpha} - 1} \leq \gamma$ and therefore we improve over the rate of VI. ∎∎ By combining the results of Propositions III.8") and III.11 ‣ III-C 𝛼-Value Iteration ‣ III SEMISMOOTH NEWTON-TYPE DYNAMIC PROGRAMMING ‣ Dynamic Programming Through the Lens of Semismooth Newton-Type Methods (Extended Version)") we obtain that, by setting ${\max\left\{ \frac{1}{1 + \gamma},\frac{1 + \gamma}{2} \right\}} < \alpha < 1$, $\alpha$-VI converges globally with a linear rate and its asymptotic linear rate of convergence is strictly better than that of VI. The numerical experiments in Figures 3") and 4") corroborate our theoretical findings and demonstrate the competitive performance of $\alpha$-VI. In addition, since our analysis is not tight, in practice we obtain convergence for a wider range of $\alpha$ as depicted in Figure 4"). The code is available at Figure 4: Empirical global contraction rate of α-VI for different values of α and comparison of α-VI and PI for a randomly generated MDP with 500 states, 10 actions and γ = 0.4. The maximum acceleration is quite dramatic and is obtained for α ≈ 0.6.

## CONCLUSIONS & FUTURE WORK

We developed a unified convergence analysis for semismooth Newton-type methods based on the kappa condition. We then proved that PI and VI are semismooth Newton-type methods. In particular, Propositions III.5") and III.6") reveal that PI and VI sit at the two opposite sides in the spectrum of semismooth Newton-type methods: PI enjoys local quadratic contraction but its costs per iteration are demanding; instead, VI is based on a coarse approximation of the elements in Clarke's generalized Jacobian which allows to drastically reduce the costs per iteration at the price of downgrading the local quadratic convergence to a linear one. This connection has far-reaching consequences on the theoretical and algorithmic side. We can both deploy the semismooth Newton-type theory to analyze the local convergence properties of existing DP methods and, taking inspiration from the existing semismooth Newton-type methods, design novel DP algorithms that achieve different trade-offs of local contraction rate and costs per iteration. In this spirit, we proposed an extension of VI with global convergence guarantees and asymptotically faster contraction rate. This novel locally accelerated version of VI comes with negligible additional computational costs and leads to great improvement in performance, as demonstrated by our numerical experiments.

Finally, another promising future direction consists in formalizing and exploiting the connection between inexact semismooth Newton methods and optimistic policy iteration-type algorithms.
