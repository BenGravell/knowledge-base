<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider linear programming (LP) problems in infinite dimensional spaces that are in general computationally intractable. Under suitable assumptions, we develop an approximation bridge from the infinite-dimensional LP to tractable finite convex programs in which the performance of the approximation is quantified explicitly. To this end, we adopt the recent developments in two areas of randomized optimization and first order methods, leading to a priori as well as a posterior performance guarantees. We illustrate the generality and implications of our theoretical results in the special case of the long-run average cost and discounted cost optimal control problems for Markov decision processes on Borel spaces. The applicability of the theoretical results is demonstrated through a constrained linear quadratic optimal control problem and a fisheries management problem.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear programming (LP) problems in infinite dimensional spaces appear, among other areas, engineering, economics, operations research and probability theory. Infinite LPs offer remarkable modeling power, subsuming general finite dimensional optimization problems and the generalized moment problem as special cases. They are, however, often computationally formidable, motivating the study of approximations schemes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A particularly rich class of problems that can be modeled as infinite LPs involves Markov decision processes (MDP) and their optimal control. More often than not, it is impossible to obtain explicit solutions to MDP problems, making it necessary to resort to approximation techniques. Such approximations are the core of a methodology known as *approximate dynamic programming*. Interestingly, a wide range of optimal control problems involving MDP can be equivalently expressed as *static* optimization problems over a closed convex set of measures, more specifically, as infinite LPs. This LP reformulation is particularly appealing for dealing with unconventional settings involving additional constraints, secondary costs, information-theoretic considerations, and reachability problems. In addition, the infinite LP reformulation allows one to leverage the developments in the optimization literature, in particular convex approximation techniques, to develop approximation schemes for MDP problems. This will also be the perspective adopted in the present article.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Approximation schemes to tackle infinite LPs have historically been developed for special classes of problems, e.g., the general capacity problem, or the generalized moment problem. The literature on control of MDP with infinite state or action spaces mostly concentrates on approximation schemes with asymptotic performance guarantees, see also the comprehensive book for controlled stochastic differential equations and for reachability problems in a similar setting. From a practical viewpoint, a challenge using these schemes is that the convergence analysis is not constructive and does not lead to explicit error bounds. A wealth of approximation schemes have been proposed in the literature under the names of approximate dynamic programming, neuro-dynamic programming, reinforcement learning, and value and/or policy iteration. Most, however, deal with discrete (finite or at most countable) state and action spaces, while approximation over uncountable spaces remains largely unexplored.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The MDP literature on explicit approximation errors in uncountable settings can, roughly speaking, be divided to two groups in terms of the performance criteria considered: discounted cost, and average cost. Of the two, the discounted cost setting has received more attention as the corresponding dynamic programming operator is a contraction, a useful property to obtain a convergence rate for the approximation error. Examples include the linear programming approach, and also a recent series of works on approximating a probability measure that underlies the random transitions of the dynamics of the system using different discretization procedures. Long-run average cost problems introduce new challenges due to loosing the contraction property. The authors in develop approximation schemes leading to finite but non-convex optimization problems, while investigates the convergence rate of the finite-state approximation to the original (uncountable) MDP problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The approach presented in this article tackles a class of general infinite LPs that, as a special case, cover both long-run discounted and average cost performance criteria in the optimal control of MDP. The resulting approximation is based on finite convex programs that are different from the existing schemes. Closest in spirit to our proposed approximation is the linear programming approach based on constraint sampling. Unlike these works, however, we introduce an additional norm constraint that effectively acts as a *regularizer*. We study in detail the conditions under which this regularizer can be exploited to bound the optimizers of the primal and dual programs, and hence provide an explicit approximation error for the proposed solution.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed approximation scheme involves a restriction of the decision variables from an infinite dimensional space to a finite dimensional subspace, followed by the approximation of the infinite number of constraints by a finite subset; we develop two complementary methods for performing the latter step. The structure of the article is illustrates in Figure 1, where the contributions are summarized as follows: Figure 1. Graphical representation of the article structure and its contributions We introduce a subclass of infinite LPs whose *regularized* semi-infinite restriction enjoys analytical bounds for both primal and dual optimizers (Proposition 3.2. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). The implications for MDP with average cost (Lemma 3.7. ‣ 3.3. Semi-infinite results in the MDP setting ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) and with discounted cost (Lemma A.2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

‣ Appendix A Infinite-Horizon Discounted-Cost Problems ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) are also investigated.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive an explicit error bound between the original infinite LP and the regularized semi-infinite counterpart, providing insights on the impact of the underlying norm structure as well as on how the choice of basis functions contributes to the approximation error (Theorem 3.3. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), Corollary 3.5. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). In the MDP setting, we recover an existing result as a special case (Corollary 3.9. ‣ 3.3. Semi-infinite results in the MDP setting ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We adopt the recent developments from the randomized optimization literature to propose a finite convex program whose solution enjoys a priori probabilistic performance bounds (Theorem 4.4. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). We extend the existing results to offer also an a posteriori bound under a generic underlying norm structure. The required conditions and theoretical assertions are validated in the MDP setting (Corollary 4.12. ‣ 4.2. Randomized results in the MDP setting ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In parallel to the randomized approach, we also utilize the recent developments in the structural convex optimization literature to propose an iterative algorithm for approximating the semi-infinite program. For this purpose, we extend the setting to incorporate unbounded prox-terms with a certain growth rate (Theorem 5.3. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). We illustrate how this extension allows us to deploy the entropy prox-term in the MDP setting (Lemma 5.10. ‣ 5.2. Structural convex optimization results in the MDP setting ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), Corollary 5.8. ‣ 5.2. Structural convex optimization results in the MDP setting ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 2 introduces the main motivation for the work, namely the control of discrete-time MDP and their LP characterization. Using standard results in the literature we embed these MDP in the more general framework of infinite LPs. Section 3 studies the link from infinite LPs to semi-infinite programs. Section 4 presents the approximation of semi-infinite programs based on randomization, while Section 5 approaches the same objective using first-order convex optimization methods. Section 6 summarizes the results in the preceding sections, establishing the approximation error from the original infinite LP to the finite convex counterparts. Section 7 illustrates the theoretical results through a truncated LQG example and a fisheries management problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MDP setting", "weight": 1.0} -->

We briefly recall some standard definitions and refer interested readers to for further details. Consider a *Markov control model* $\left(S,A,{\{{A{(s)}}:{s \in S}\}},Q,\psi \right),$ where $S$ (resp. $A$) is a metric space called the *state space* (resp. *action space*) and for each $s \in S$ the measurable set ${A{(s)}} \subseteq A$ denotes the set of feasible actions when the system is in state $s \in S$. The *transition law* is a stochastic kernel $Q$ on $S$ given the feasible state-action pairs in $K ≔ {\{{(s,a)}:{{s \in S},{a \in {A{(s)}}}}\}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "MDP setting", "weight": 1.0} -->

A stochastic kernel acts on real valued measurable functions $u$ from the left as and on probability measures $\mu$ on $K$ from the right as Finally $\psi:{K\rightarrow{\mathbb{R}}_{+}}$ denotes a measurable function called the *one-stage cost function*. The *admissible history spaces* are defined recursively as $H_{0} ≔ S$ and $H_{t} ≔ {H_{t - 1} \times K}$ for $t \in {\mathbb{N}}$ and the canonical sample space is defined as $\Omega ≔ {({S \times A})}^{\infty}$. All random variables will be defined on the measurable space $(\Omega,\mathcal{G})$ where $\mathcal{G}$ denotes the corresponding product $\sigma$-algebra.

<!-- chunk {"id": "body-0016", "role": "body", "section": "MDP setting", "weight": 1.0} -->

The stochastic process $\left(\Omega,\mathcal{G},{\mathbb{P}}_{\nu}^{\pi},{(s_{t})}_{t \in {\mathbb{N}}_{0}} \right)$ is called a *discrete-time MDP*. For most of the article we consider optimal control problems where the aim is to minimise a long term *average cost* (AC) over the set of admissible policies and initial state measures. We definite the optimal value of the optimal control problem by We emphasize, however, that the results also apply to other performance objective, including the long-run *discounted cost* problem as shown in Appendix A.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Infinite LP characterization", "weight": 1.0} -->

The problem in admits an alternative LP characterization under some mild assumptions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2.1 (Control model)", "weight": 1.0} -->

the set of feasible state-action pairs is the unit hypercube $K = {\lbrack 0,1\rbrack}^{\dim{({S \times A})}}$; the transition law $Q$ is Lipschitz continuous, i.e., there exists $L_{Q} > 0$ such that for all ${k,k'} \in K$ and all continuous functions $u$ the cost function $\psi$ is non-negative and Lipschitz continuous on $K$ with respect to the $\ell_{\infty}$-norm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2.1 (Control model)", "weight": 1.0} -->

Assumption 2.1. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")(i) ‣ Assumption 2.1 (Control model). ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") may seem restrictive, however, essentially it simply requires that the state-action set $K$ is compact. We refer the reader to Example 7.2 where a non-rectangular $K$ is transferred to a hypercube, and to \[26, Chapter 12.3\] for further information about the LP characterization in more general settings.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2.3 (Constrained MDP)", "weight": 1.0} -->

The LP characterization of MDP naturally allows us to incorporate constraints in the form of where the functions $d_{i}:{K\rightarrow{\mathbb{R}}}$ and constants $\ell_{i}$ reflect our desired specifications. To this end, it suffices to introduce auxiliary decision variables $\beta_{i} \in {\mathbb{R}}_{+}$, and in (5. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) replace $\rho$ in the objective with $\rho - {\sum_{i = 1}^{I}{\beta_{i}\ell_{i}}}$ and in the constraint with $\rho - {\sum_{i = 1}^{I}{\beta_{i}d_{i}}}$, see \[23, Theorem 5.2\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2.3 (Constrained MDP)", "weight": 1.0} -->

Our aim is to derive an approximation scheme for a class of such infinite dimensional LPs, including problems of the form (5. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")), that comes with an explicit bound on the approximation error.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Dual pairs of normed vector spaces", "weight": 1.0} -->

The triple $({\mathbb{X}},{\mathbb{C}}, \parallel \cdot \parallel)$ is called a *dual pair* of normed vector spaces if $\mathbb{X}$ and $\mathbb{C}$ are vector spaces; $\left\langle \cdot, \cdot \right\rangle$ is a bilinear form on ${\mathbb{X}} \times {\mathbb{C}}$ that "separates points", i.e., for each nonzero $x \in {\mathbb{X}}$ there is some $c \in {\mathbb{C}}$ such that $\left\langle x,c \right\rangle \neq 0$, for each nonzero $c \in {\mathbb{C}}$ there is some $x \in {\mathbb{X}}$ such that $\left\langle x,c \right\rangle \neq 0$; $\mathbb{X}$ is equipped with the norm $\parallel \cdot

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dual pairs of normed vector spaces", "weight": 1.0} -->

The norm in the vector spaces is used as a means to quantify the performance of the approximation schemes. In particular, we emphasize that the vector spaces are not necessarily complete with respect to these norms.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dual pairs of normed vector spaces", "weight": 1.0} -->

Let $({\mathbb{B}},{\mathbb{Y}}, \parallel \cdot \parallel)$ be another dual pair of normed vector spaces. As there is no danger of confusion, we use the same notation for the potentially different norm and bilinear form for each pair. Let $\mathcal{A}:{{\mathbb{X}}\rightarrow{\mathbb{B}}}$ be a linear operator, and $\mathbb{K}$ be a convex cone in $\mathbb{B}$. Given the fixed elements $c \in {\mathbb{C}}$ and $b \in {\mathbb{B}}$, we define a linear program, hereafter called the *primal* program 16, as where the conic inequality ${\mathcal{A}x} \succeq_{\mathbb{K}}b$ is understood in the sense of ${{\mathcal{A}x} - b} \in {\mathbb{K}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dual pairs of normed vector spaces", "weight": 1.0} -->

Throughout this study we assume that the program 16 has an optimizer (i.e., the infimum is indeed a minimum), the cone $\mathbb{K}$ is closed and the operator $\mathcal{A}$ is continuous where the corresponding topology is the weakest in which the topological duals of $\mathbb{X}$ and $\mathbb{B}$ are $\mathbb{C}$ and $\mathbb{Y}$, respectively. Let $\mathcal{A}^{\ast}:{{\mathbb{Y}}\rightarrow{\mathbb{C}}}$ be the adjoint operator of $\mathcal{A}$ defined by Recall that if $\mathcal{A}$ is weakly continuous, then the adjoint operator $\mathcal{A}^{\ast}$ is well defined as its image is a subset of $\mathbb{C}$ \[26, Proposition 12.2.5\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dual pairs of normed vector spaces", "weight": 1.0} -->

The *dual* program of 16 is denoted by 20 and is given by where ${\mathbb{K}}^{\ast}$ is the dual cone of $\mathbb{K}$ defined as ${{\mathbb{K}}^{\ast} ≔ \left\{ {y \in {\mathbb{Y}}}:{{\left\langle b,y \right\rangle \geq 0},{{\forall b} \in {\mathbb{K}}}} \right\}}.$ It is not hard to see that *weak duality* holds, as An interesting question is when the above assertion holds as an equality. This is known as *zero duality gap*, also referred to as *strong duality* particularly when both 16 and 20 admit an optimizer \[1, p. 52\]. Our study is not directly concerned with conditions under which strong duality between 16 and 20 holds; see \[1, Section 3.6\] for a comprehensive discussion of such conditions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dual pairs of normed vector spaces", "weight": 1.0} -->

The programs 16 and 20 are assumed to be *infinite*, in the sense that the dimensions of the decision spaces ($\mathbb{X}$ in 16, and $\mathbb{Y}$ in 20) as well as the number of constraints are both infinite.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Semi-infinite approximation", "weight": 1.0} -->

Consider a family of linearly independent elements ${\{ x_{n}\}}_{n \in {\mathbb{N}}} \subset {\mathbb{X}}$, and let ${\mathbb{X}}_{n}$ be the finite dimensional subspace generated by the first $n$ elements ${\{ x_{i}\}}_{i \leq n}$. Without loss of generality, we assume that $x_{i}$ are normalized, i.e., ${\| x_{i}\|} = 1$. Restricting the decision space $\mathbb{X}$ of 16 to ${\mathbb{X}}_{n}$, along with an additional norm constraint, yields the program where $\parallel \cdot \parallel_{\Re}$ is a given norm on ${\mathbb{R}}^{n}$ and $\theta_{\mathcal{P}}$ determines the size of the feasible set.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Semi-infinite approximation", "weight": 1.0} -->

In the spirit of dual-paired normed vector spaces, one can approximate $({\mathbb{X}},{\mathbb{C}}, \parallel \cdot \parallel)$ by the finite dimensional counterpart $({\mathbb{R}}^{n},{\mathbb{R}}^{n}, \parallel \cdot \parallel_{\Re})$ where the bilinear form is the standard inner product.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Semi-infinite approximation", "weight": 1.0} -->

Defining the vector $\mathbf{c} ≔ {\lbrack\left\langle x_{1},c \right\rangle,\cdots,\left\langle x_{n},c \right\rangle\rbrack}$, we can rewrite the program as We call 29 a *semi-infinite* program, as the decision variable is a finite dimensional vector $\alpha \in {\mathbb{R}}^{n}$, but the number of constraints is still in general infinite due to the conic inequality. The additional constraint on the norm of $\alpha$ in 29 acts as a *regularizer* and is a key difference between the proposed approximation schemes and existing schemes in the literature. Methods for choosing the parameter $\theta_{\mathcal{P}}$ will be discussed later.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Semi-infinite approximation", "weight": 1.0} -->

Dualizing the conic inequality constraint in 29 and using the dual norm definition leads to a dual counterpart where$\parallel \cdot \parallel_{\Re^{\ast}}$ denotes the dual norm of $\parallel \cdot \parallel_{\Re}$. Note that setting $\theta_{\mathcal{P}} = \infty$ effectively implies that the second term of the objective in 32 introduces $n$ hard constraints ${\mathcal{A}_{n}^{\ast}y} = \mathbf{c}$ (cf.).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.1 (Semi-infinite regularity)", "weight": 1.0} -->

Assumption 3.1. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")(ii) ‣ Assumption 3.1 (Semi-infinite regularity). ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") is closely related to the condition that in the literature of numerical algorithms in infinite dimensional spaces, in particular the Galerkin discretization methods for partial differential equations, is often referred to as the "*inf-sup*" condition, see for a comprehensive survey.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 3.1 (Semi-infinite regularity)", "weight": 1.0} -->

To see this, note that for every $x \in {\mathbb{X}}_{n}$ the definitions in imply that These conditions are in fact equivalent if the norm $\parallel \cdot \parallel_{\Re}$ is induced by the original norm on $\mathbb{X}$, i.e., ${\|\alpha\|}_{\Re} ≔ {\|{\sum_{i = 1}^{n}{\alpha_{i}x_{i}}}\|}$. We note that $\mathcal{A}_{n}^{\ast}$ maps an infinite dimensional space to a finite dimensional one, and as such Assumption 3.1. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")(ii) ‣ Assumption 3.1 (Semi-infinite regularity).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 3.1 (Semi-infinite regularity)", "weight": 1.0} -->

‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") effectively necessitates that the null-space of $\mathcal{A}_{n}^{\ast}$ intersects the positive cone ${\mathbb{K}}^{\ast}$ only at $0$. In the following we show that this regularity condition leads to a zero duality gap between 29 and 32, as well as an upper bound for the dual optimizers. The latter turns out to be a critical quantity for the performance bounds of this study.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3.4 (Impact of norms on semi-infinite approximation)", "weight": 1.0} -->

We note the following concerning the impact of the choice of norms on the approximation error: The only norm that influences the semi-infinite program 29 is $\parallel \cdot \parallel_{\Re}$ on ${\mathbb{R}}^{n}$. When it comes to the approximation error (35. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")), the norm $\parallel \cdot \parallel_{\Re}$ may have an impact on the residual $r_{n}$ only if the set $\mathsf{B}_{n}$ in does not contain $\Pi_{{\mathbb{X}}_{n}}{(x^{\star})}$, the projection $x^{\star}$ on the subspace ${\mathbb{X}}_{n}$, where $x^{\star}$ is an optimizer of the infinite program 16.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3.4 (Impact of norms on semi-infinite approximation)", "weight": 1.0} -->

The norms of the dual pairs of vector spaces only appear in Theorem 3.3. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") to quantify the approximation error. Note that in (35. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) the stronger the norm on $\mathbb{X}$, the higher $\| r_{n}\|$, and the lower ${\| c\|}_{\ast}$ and $\|\mathcal{A}\|$. On the other hand, the stronger the norm on $\mathbb{B}$, the higher $\| b\|$ and $\|\mathcal{A}\|$ and the lower $\gamma$ (cf. Assumption 3.1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3.4 (Impact of norms on semi-infinite approximation)", "weight": 1.0} -->

‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")(ii) ‣ Assumption 3.1 (Semi-infinite regularity). ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3.4 (Impact of norms on semi-infinite approximation)", "weight": 1.0} -->

The error bound (35. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) can be further improved when $\mathbb{X}$ is a Hilbert space. In this case, let ${\overline{\mathbb{X}}}_{n}$ denote the orthogonal complement of ${\mathbb{X}}_{n}$. We define the *restricted* norms by It is straightforward to see that by definition ${\| c\|}_{\ast n} \leq {\| c\|}_{\ast}$ and ${\|\mathcal{A}\|}_{n} \leq {\|\mathcal{A}\|}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Semi-infinite results in the MDP setting", "weight": 1.0} -->

We now return to the MDP setting in Section 2, and in particular the AC problem (5. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")), to investigate the application of the proposed approximation scheme. Recall that the AC problem can be recast in an LP framework in the form of 16, see. To complete this transition to the dual pairs, we introduce the spaces The bilinear form between each pair $({\mathbb{X}},{\mathbb{C}})$ and $({\mathbb{B}},{\mathbb{Y}})$ is defined in an obvious way (cf.).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Semi-infinite results in the MDP setting", "weight": 1.0} -->

The linear operator $\mathcal{A}:{{\mathbb{X}}\rightarrow{\mathbb{B}}}$ is defined as ${\mathcal{A}{(\rho,u)}{(s,a)}} ≔ {{{- \rho} - {u{(s)}}} + {Qu{(s,a)}}}$, and it can be shown to be weakly continuous \[26, p. 220\]. On the pair $({\mathbb{X}},{\mathbb{C}})$ we consider the norms A commonly used norm on the set of measures is the total variation whose dual (variational) characterization is associated with $\parallel \cdot \parallel_{\infty}$ in the space of continuous functions \[26, p. 2\]. We note that in the positive cone ${\mathbb{K}}^{\ast} = {\mathcal{M}_{+}{(K)}}$ the total variation and Wasserstein norms indeed coincide.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Semi-infinite results in the MDP setting", "weight": 1.0} -->

Following the construction in 29, we consider a collection of $n$-linearly independent, normalized functions ${\{ u_{i}\}}_{i \leq n}$, ${\| u_{i}\|}_{L} = 1$, and define the semi-infinite approximation of the AC problem (5.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Semi-infinite results in the MDP setting", "weight": 1.0} -->

‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) by Comparing with the program 29, we note that the finite dimensional subspace ${\mathbb{X}}_{n} \subset {{{\mathbb{R}} \times \mathcal{L}}{(S)}}$ is the subspace spanned by the basis elements $x_{0} = {}$ and $x_{i} = {(0,u_{i})}$ for all $i \in {\{ 1,\cdots,n\}}$, i.e., the subspace ${\mathbb{X}}_{n}$ is in fact $n + 1$ dimensional. Moreover, the norm constraint in is only imposed on the second coordinate of the decision variables $(\rho,\alpha)$ (i.e., ${\|\alpha\|}_{\Re} \leq \theta_{\mathcal{P}}$).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Semi-infinite results in the MDP setting", "weight": 1.0} -->

The following lemmas address the operator norm and the respective regularity requirements of Assumption 3.1. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") for the program.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3.8 (AC dual optimizers bound)", "weight": 1.0} -->

As opposed to the general LP in Proposition 3.2. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), Lemma 3.7. ‣ 3.3. Semi-infinite results in the MDP setting ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") implies that the dual optimizers for the AC problem is not influenced by the primal norm bound $\theta_{\mathcal{P}}$ and is uniformly bounded by $1$. In fact, this result can be strengthened to ${\| y_{n}^{\star}\|}_{W} = 1$ due to the special minimax structure of the AC program. This refinement is not needed at this stage and we postpone the discussion to Section 5.2. The feature discussed in this remark does, however, not hold for the class of long-run discounted cost problems, see Lemma A.2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 3.8 (AC dual optimizers bound)", "weight": 1.0} -->

‣ Appendix A Infinite-Horizon Discounted-Cost Problems ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") in Appendix A.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 3.8 (AC dual optimizers bound)", "weight": 1.0} -->

Now we are in a position to translate Theorem 3.3. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") to the MDP setting for the AC problem (5. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 3.10 (Projection residual)", "weight": 1.0} -->

The residual error $\left\| {u^{\star} - {\Pi_{{\mathbb{U}}_{n}}{(u^{\star})}}} \right\|_{L}$ can be approximated by leveraging results from the literature on universal function approximation. Prior information about the value function $u^{\star}$ may offer explicit quantitative bounds. For instance, for MDP under Assumption 2.1. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") we know that $u^{\star}$ is Lipschitz continuous. For appropriate choice of basis functions, we can therefore ensure a convergence rate of $n^{- {1/{\dim{(S)}}}}$ where $\dim{(S)}$ is the dimension of the state-action set $S$, see for instance for polynomials and for the Fourier basis functions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Semi-infinite to Finite Programs: Randomized Approach", "weight": 1.0} -->

We study conditions under which one can provide a finite approximation to the semi-infinite programs of the form 29, that are in general known to be computationally intractable --- NP-hard \[4, p. 16\]. We approach this goal by deploying tools from two areas, leading to different theoretical guarantees for the proposed solutions. This section focuses on a randomized approach and the next section is dedicated to an iterative gradient-based decent method. The solution of each of these methods comes with a priori as well as a posteriori performance certificates.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

We start with a lemma suggesting a simple bound on the norm of the operator $\mathcal{A}_{n}$. We will use the bound to quantify the approximation error of our proposed solutions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 4.3 (TB candidate)", "weight": 1.0} -->

Let $g:{{\mathbb{R}}_{+}\rightarrow{\lbrack 0,1\rbrack}}$ be a non-decreasing function such that for any $\kappa \in \mathcal{K}$ we have ${g{(\gamma)}} \leq {{\mathbb{P}}\left\lbrack {\mathsf{B}_{\gamma}{(\kappa)}} \right\rbrack}$, where $\mathsf{B}_{\gamma}{(\kappa)}$ is the open ball centered at $\kappa$ with radius $\gamma$; note that function $g$ depends on the choice of the norm on $\mathbb{Y}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 4.3 (TB candidate)", "weight": 1.0} -->

Then, a candidate for a TB function of the program 52 is where the inverse function is understood as ${g^{- 1}{(\varepsilon)}} ≔ {\sup{\{{\gamma \in {\mathbb{R}}_{+}}:{{g{(\gamma)}} \leq \varepsilon}\}}}$, and /is the constant ratio defined in (47. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 4.3 (TB candidate)", "weight": 1.0} -->

To see this note that according to Definition 4.2. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") we have Thus, if ${p{(\alpha,\zeta)}} \leq \varepsilon$, then ${g{({\gamma{(\zeta)}})}} \leq \varepsilon$ and by construction of the inverse function $g^{- 1}$ we have ${{\zeta{\|{{\mathcal{A}_{n}\alpha} - b}\|}^{- 1}} \leq {g^{- 1}{(\varepsilon)}}}.$ In view of Definition 4.2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 4.3 (TB candidate)", "weight": 1.0} -->

‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), this observation readily suggests that the function ${h{(\alpha,\varepsilon)}} ≔ {{\|{{\mathcal{A}_{n}\alpha} - b}\|}g^{- 1}{(\varepsilon)}}$ is indeed a TB candidate, and the suggested upper bound follows readily from Lemma 4.1. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming").

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.5 (Curse of dimensionality)", "weight": 1.0} -->

The TB function $h$ of Example 4.3. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") may grow exponentially in the dimension of the support set $\mathcal{K}$ (i.e., ${h{(\alpha,\varepsilon)}} \propto \varepsilon^{- {\dim{(\mathcal{K})}}}$). Since $\mathsf{N}{(n, \cdot,\beta)}$ admits a linear growth rate, the a priori bound (54c. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) effectively leads to an exponential number of samples in the precision level $\varepsilon$, an observation related to the curse of dimensionality \[36, Remark 3.9\].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 4.5 (Curse of dimensionality)", "weight": 1.0} -->

To mitigate this inherent computational complexity, one may resort to a more elegant sampling approach so that the required number of samples $\mathsf{N}$ has a sublinear rate in the second argument, see for instance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 4.6 (Optimal choice of $\\theta_{\\mathcal{P}}$)", "weight": 1.0} -->

In view of the a priori error in Theorem 4.4. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), the parameter $\theta_{\mathcal{P}}$ may be chosen so as to minimize the required number of samples. To this end, it suffices to maximize $z_{n}$ defined in (54b. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) over all $\theta_{\mathcal{P}} > {{\| b\|}\gamma^{- 1}}$, see Assumption 3.1. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")(ii) ‣ Assumption 3.1 (Semi-infinite regularity).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 4.6 (Optimal choice of $\\theta_{\\mathcal{P}}$)", "weight": 1.0} -->

‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), where $\theta_{\mathcal{D}}$ is defined in (33. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). One can show that the optimal choice in this respect is analytically available as where $J_{n}^{LB}$ is a lower bound on the optimal value of 29 used in (33. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 4.7 (Norm impact on finite approximation)", "weight": 1.0} -->

Besides to what has already been highlighted in Remark 3.4. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), the choice of norms in the dual pairs of normed vector spaces also has an impact on the function $g^{- 1}{(\varepsilon)}$. More specifically, the stronger the norm in the space $\mathbb{B}$, the larger the balls in the dual space $\mathbb{Y}$, and thus the smaller the function $g^{- 1}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 4.7 (Norm impact on finite approximation)", "weight": 1.0} -->

To prove Theorem 4.4. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") we need a few preparatory results.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Randomized results in the MDP setting", "weight": 1.0} -->

We return to the MDP setting and discuss the implication of Theorem 4.4. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") as the bridge from the semi-infinite program 29 to the finite counterpart 52. Recall the dual pairs of vector spaces setting in with the assigned norms. To construct the finite program 52, we need to sample from the set of extreme points of $\mathcal{P}{(K)}$, i.e., the set of point measures where $\delta_{(s,a)}$ denotes a point probability distribution at ${(s,a)} \in K$. In this view, in order to sample elements from $\mathcal{K}$ it suffices to sample from the state-action feasible pairs ${(s,a)} \in K$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Semi-infinite to Finite Program: Structural convex optimization", "weight": 1.0} -->

This section approaches the approximation of the semi-infinite program 29 from an alternative perspective relying on an iterative first order decent method. As opposed to the scenario approach presented in Section 4, that is probabilistic and starts from the program 29, the method of this section is deterministic and starts with the dual counterpart 32, in particular a regularized version of whose solutions can be computed efficiently. It turns out that the regularized solution allows one to reconstruct a nearly feasible solution for both programs 29 and 32, offering a meaningful performance bound for the approximation step from the semi-infinite program to a finite program.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

The basis of our approach is the fast gradient method that significantly improves the theoretical and, in many cases, also the practical convergence speed of the gradient method. The main idea is based on a well known technique of smoothing nonsmooth functions. To simplify the notation, for a given $\theta_{\mathcal{P}}$ we define the sets where $\theta_{\mathcal{D}}$ is the constant defined in (33. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). Recall that in the wake of Proposition 3.2. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") we know that the decision variables of the dual program 32 may be restricted to the set $\mathcal{Y}$ without loss of generality.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

We modify the program 32 with a regularization term scaled with the non-negative parameter $\eta$ and define the *regularized* program where the regularization function $d:{\mathcal{Y}\rightarrow{\mathbb{R}}_{+}}$, also known as the prox-function, is strongly convex. The choice of the prox-function depends on the specific problem structure and may have significant impact on the approximation errors. Given the regularization term $\eta$ and the parameter $\alpha \in {\mathbb{R}}^{n}$, we introduce the auxiliary quantity It is computationally crucial for the solution method proposed in this part that the prox-function allows us to have access to the auxiliary variable $y_{\eta}^{\star}{(\alpha)}$ for each $\alpha \in {\mathbb{R}}^{n}$. This requirement is formalized as follows.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 5.1 (Lipschitz gradient)", "weight": 1.0} -->

Consider the adjoint operator $\mathcal{A}_{n}^{\ast}$ in and the optimizer $y_{\eta}^{\star}{(\alpha)}$ of the auxiliary quantity.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Assumption 5.1 (Lipschitz gradient)", "weight": 1.0} -->

We then define the operator ${\mathbb{T}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n}}$ as More generally, a different norm can be used in the second term in when $\vartheta$ is a different strong convexity parameter. However, we forgo this additional generality to keep the exposition simple. The operator $\mathbb{T}$ is defined implicitly through a finite convex optimization program whose computational complexity may depend on the $\Re$-norm through the constraint set $\mathcal{A}$. For typical norms in ${\mathbb{R}}^{n}$ (e.g., $\parallel \cdot \parallel_{\ell_{p}}$) the pointwise evaluation of the operator $\mathbb{T}$ is computationally tractable.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Assumption 5.1 (Lipschitz gradient)", "weight": 1.0} -->

Furthermore, if $\parallel \cdot \parallel_{\Re} = \parallel \cdot \parallel_{\ell_{2}}$, then the definition of has an explicit analytical description for any pair $(q,\alpha)$ as follows.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 5.4 (Computational complexity)", "weight": 1.0} -->

Adding the prox-function to the problem 32 ensures that the regularized counterpart $\mathcal{D}_{n,\eta}$ admits an efficiency estimate (in terms of iteration numbers) of the order $\mathcal{O}\left( \sqrt{\frac{L}{\eta}\varepsilon^{- 1}} \right)$. To construct a smooth $\varepsilon$-approximation for the original problem 32, the Lipschitz constant $\frac{L}{\eta}$ can be chosen of the order $\mathcal{O}{({\varepsilon^{- 1}{\log{(\varepsilon^{- 1})}}})}$. Thus, the presented gradient scheme has an efficiency estimate of the order $\mathcal{O}\left( {\varepsilon^{- 1}\sqrt{\log{(\varepsilon^{- 1})}}} \right)$, see for a more detailed discussion along similar objective.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 5.5 (Inexact gradient)", "weight": 1.0} -->

The error bounds in Theorem 5.3. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") are introduced based on the availability of the exact first-order information, i.e., it is assumed that at each iteration the vector $r^{(k)}$ that due to the bilinear form potentially involves a multi dimensional integration can be computed exactly. In general, the evaluation of those vectors may only be available approximately. This gives rise to the question of how the fast gradient method performs in the case of *inexact* first-order information. We refer the interested reader to for further details.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 5.5 (Inexact gradient)", "weight": 1.0} -->

The a priori bound proposed by Theorem 5.3. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") involves the positive constants $c,C$, which are used to introduce an upper bound for the proxy-term. These constants potentially depend on $\theta_{\mathcal{D}}$, the size of the dual feasible set, hence also on $\theta_{\mathcal{P}}$. Therefore, unlike the randomized approach in Section 4, it is not immediately clear how $\theta_{\mathcal{P}}$ can be chosen to minimize the complexity of the proposed method, which in this case is the required number of iterations $k$ suggested in (74. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) (cf. Remark 4.6.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 5.5 (Inexact gradient)", "weight": 1.0} -->

‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). In the next section, we shall discuss how to address this issue in the MDP setting for particular constants $c,C$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Structural convex optimization results in the MDP setting", "weight": 1.0} -->

To link the approximation method presented in Section 5.1 to the AC program, let us recall the dual pairs equipped with the norms. To simplify the analysis, we refine the assertion in Lemma 3.7. ‣ 3.3. Semi-infinite results in the MDP setting ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") and argue that the dual optimizers are indeed probability measures, i.e., To see this, one can consider the norm ${\|{(\rho,\alpha)}\|} ≔ {\|\alpha\|}_{\Re}$ and follow similar arguments in the proof of Proposition 3.2. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"). Strictly speaking, this is not a true norm on ${\mathbb{R}}^{n + 1}$ but it does not affect the technical argument, in particular strong duality between 29 and 32. The details are omitted here in the interest of space.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Structural convex optimization results in the MDP setting", "weight": 1.0} -->

We consider the prox-function as a relative entropy defined by where $\lambda$ is the uniform measure supported on the set $K$ and $\frac{dy}{d\lambda} \in {\mathcal{F}_{+}{(K)}}$ is the Radon-Nikodym derivative between two measures $y$ and $\lambda$. One can inspect that the prox-function is indeed a non-negative function. The optimizer of the regularized program $\mathcal{D}_{n,\eta}$ for the AC program is To see, check together with the definitions of the operator $\mathcal{A}_{n}$ in and the AC problem parameters.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 5.11 (Efficient computation of )", "weight": 1.0} -->

When the transition kernel $Q$ and the basis functions $u_{i}$ are such that the relation involves integration of exponentials of polynomials over simple sets (e.g., box or a simplex), one may utilize efficient methods that require solving a hierarchy of semidefinite programming problems to generate upper and lower bounds which asymptotically converge to the true value of integral, see \[32, Section 12.2\] and. It is also worth noting that a straightforward computation of for a small parameter $\eta$ may be numerically difficult due to the exponential functions. This issue can, however, be circumvented by a numerically stable technique presented in \[39, p. 148\].

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 5.11 (Efficient computation of )", "weight": 1.0} -->

Regarding the choice of $\theta_{\mathcal{P}}$, in similar spirit to Section 4, one can target minimizing the complexity of the a priori bound, in other words the number of iterations $k$ in (74. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")). In the setting of Corollary 5.8. ‣ 5.2. Structural convex optimization results in the MDP setting ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), one can observe that the smaller the parameter $\theta_{\mathcal{P}}$, the lower the number of the required iterations, leading to the choice described as.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Full Infinite to Finite Programs", "weight": 1.0} -->

The intention in this short section is to combine the two-step process from infinite to semi-infinite programs in Section 3 and from semi-infinite to finite programs in Section 4 and 5, and hence establish a link from the original infinite program to finite counterparts. We only present the final result for the general infinite programs without discussing its implication in the MDP setting, as it is essentially a similar assertion.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We present two numerical examples to illustrate the solution methods and corresponding performance bounds. Throughout this section we consider the norm $\parallel \cdot \parallel_{\Re} = \parallel \cdot \parallel_{\ell_{2}}$, leading to $= /\sqrt{n}$ in (47. ‣ 4.1. Randomized approach ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")), and we choose the Fourier basis functions.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 1: truncated LQG", "weight": 1.0} -->

Consider the linear system with quadratic stage cost ${\psi{(s,a)}} = {{qs^{2}} + {ra^{2}}}$, where $q \geq 0$ and $r > 0$ are given constants. We assume that $S = A = {\lbrack{- L},L\rbrack}$ and the parameters ${\vartheta,\rho} \in {\mathbb{R}}$ are known. The disturbances ${\{\xi_{t}\}}_{t \in {\mathbb{N}}}$ are i.i.d. random variables generated by a truncated normal distribution with known parameters $\mu$ and $\sigma$, independent of the initial state $s_{0}$. Thus, the process $\xi_{t}$ has a distribution density where $\phi$ is the probability density function of the standard normal distribution, and $\Phi$ is its cumulative distribution function. The transition kernel $Q$ has a density function $q{(\left.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example 1: truncated LQG", "weight": 1.0} -->

y \middle| {s,a} \right.)}$, i.e., ${Q{(\left. B \middle| {s,a} \right.)}} = {\int_{B}{q{(\left. y \middle| {s,a} \right.)}{dy}}}$ for all $B \in {\mathcal{B}(S)}$, that is given by In the special case that $L = {+ \infty}$ the above problem represents the classical LQG problem, whose solution can be obtained via the algebraic Riccati equation \[6, p. 372\]. By a simple change of coordinates it can be seen that the presented system fulfills Assumption 2.1. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"). The following lemma provides the technical parameters required for the proposed error bounds.

<!-- chunk {"id": "body-0079", "role": "body", "section": "*Simulation details:*", "weight": 1.0} -->

(d) Zoomed version of the average cost for different n Figure 2. The objective performance Jn, NAC is computed using for Example 7.1. The red dotted line denoted by JAC is the optimal solution approximated by n = 103 and N = 106.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

We implement the methodology presented in Section 4.2, resulting in a finite random convex program as in (65. ‣ 4.2. Randomized results in the MDP setting ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")), where the uniform distribution on $K = {S \times A} = {\lbrack{- L},L\rbrack}^{2}$ is used to draw the random samples. Figures 2(a), 2(b), and 2(c) visualize three cases with different number of basis functions $n \in {\{ 2,10,100\}}$, respectively. To show the impact of the additional norm constraint, in each case two approximation settings are examined: the constrained (regularized) one proposed in this article (i.e., $\theta_{\mathcal{P}} < \infty$), and the unconstrained one (i.e., $\theta_{\mathcal{P}} = \infty$).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

In the former we choose the bound suggested by (68b). In the latter, the resulting optimization programs of (65. ‣ 4.2. Randomized results in the MDP setting ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")) may happen to be unbounded, particularly when the number of samples $N$ is low; numerically, we capture the behavior of the unbounded $\theta_{\mathcal{P}}$ through a large bound such as $\theta = 10^{6}$. In each sub-figure, the colored tubes represent the results of $400$ independent experiments (shaded areas) as well as the mean value across different experiments (solid and dashed lines) of the objective performance $J_{n,N}^{AC}$ as a function of the sample size $N$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

The simulation results suggest three interesting features concerning $n$, the number of basis functions: The higher the number of basis functions, the smaller the approximation error (i.e., asymptotic distance for $N\rightarrow\infty$ to the red dotted line), the lower the variance of approximation with respect to the sampling distribution for each $N$, and the slower the convergence behavior with respect to the sample size $N$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

The features (i) ‣ Randomized approach: ‣ 7.1. Example 1: truncated LQG ‣ 7. Numerical Examples ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") and (ii) ‣ Randomized approach: ‣ 7.1. Example 1: truncated LQG ‣ 7. Numerical Examples ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") are positive impacts of increasing the number of basis functions. While (i) ‣ Randomized approach: ‣ 7.1. Example 1: truncated LQG ‣ 7. Numerical Examples ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") is predicted by Corollary 3.9.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

‣ 3.3. Semi-infinite results in the MDP setting ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), since the error due to the projection term becomes smaller, it is not entirely clear how to formally explain (ii) ‣ Randomized approach: ‣ 7.1. Example 1: truncated LQG ‣ 7. Numerical Examples ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"). On the contrary, the feature (iii) ‣ Randomized approach: ‣ 7.1. Example 1: truncated LQG ‣ 7. Numerical Examples ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") is indeed a negative impact, as a high number of basis functions requires a large number of samples $N$ to produce reasonable approximation errors. This phenomena can be justified through the lens of Corollary 4.12.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

‣ 4.2. Randomized results in the MDP setting ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") where the approximation errors grows proportionally to $n$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

Algorithm 1 was implemented with the parameters described in Corollary 5.8. ‣ 5.2. Structural convex optimization results in the MDP setting ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") leading to deterministic upper and lower bounds ($J_{n,\eta}^{UB}$ and $J_{n,\eta}^{LB}$, respectively) for the cost function $J_{n}^{AC}$, see also Theorem 5.3. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"). These bounds are computationally appealing as they provide a posteriori bounds on the approximation error that often is significantly smaller than the a priori bounds given by Theorem 5.3. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming").

<!-- chunk {"id": "body-0087", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

This behavior can be seen in the simulation results summarized in Figure 3 where the number of basis functions is $n = 10$. Similar to Figure 2, the red dotted line is the optimal value of the original infinite program 16, which we approximated by using $10^{3}$ basis functions and $10^{6}$ iterations of Algorithm 1; it coincides with the one from the randomized method.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

(a) A priori error ε and a posteriori error Jn, ηUB − Jn, ηLB (b) Upper bound Jn, ηUB and lower bound Jn, ηLB Figure 3. The results and error bounds are obtained by Algorithm 1 with n = 10 for Example 7.1. The red dotted line is the optimal solution computed as indicated in Figure 2.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Example 2: A fisheries management problem", "weight": 1.0} -->

A natural approximation approach toward dynamic programming problems goes through a discretization scheme (e.g., discretization the state and/or action spaces). The main objective of this example is to compare the proposed LP-based approximation of this article with more standard discretization schemes. To this end, we borrow an example from \[24, Section 1.3\] and compare our results with the recent discretization method proposed. Consider the population growth model, known as Ricker model, where ${\vartheta_{1},\vartheta_{2}} \in {\mathbb{R}}_{+}$, $s_{t}$ is the population size in season $t$, and $a_{t}$ is the population to be left for spawning for the next season, i.e., the difference $s_{t} - a_{t}$ is the amount of fish captured in season $t$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Example 2: A fisheries management problem", "weight": 1.0} -->

Since the population left for spawning cannot be greater than the total population, for each $s \in S$, the set of admissible actions is ${A{(s)}} = {\lbrack\underset{¯}{\kappa},s\rbrack}$. To fulfill Assumption 2.1. ‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")(i) ‣ Assumption 2.1 (Control model).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Example 2: A fisheries management problem", "weight": 1.0} -->

‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), following the transformation suggested, we equivalently reformulate the above problem using the dynamics where the admissible actions set is now the state-independent set $A = {\lbrack\underset{¯}{\kappa},\overline{\kappa}\rbrack}$, and the running reward function is ${\psi{(a,s)}} = {\varphi{({s - a})}\mathbf{1}_{\{{s \geq a}\}}}$. The noise process ${(\xi_{t})}_{t \in {\mathbb{N}}}$ is a sequence of i.i.d. random variables which have a uniform density function $g$ supported on the interval $\lbrack 0,\lambda\rbrack$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Example 2: A fisheries management problem", "weight": 1.0} -->

Thus, the corresponding kernel is Note that to make the model consistent, we must have ${\vartheta_{1}a{\exp{({{- {\vartheta_{2}a}} + \xi})}}} \in {\lbrack\underset{¯}{\kappa},\overline{\kappa}\rbrack}$ for all ${(a,\xi)} \in {{\lbrack\underset{¯}{\kappa},\overline{\kappa}\rbrack} \times {\lbrack 0,\lambda\rbrack}}$. By defining an appropriate change of coordinate similar to Lemma 7.1. ‣ 7.1. Example 1: truncated LQG ‣ 7. Numerical Examples ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), Assumption 2.1.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Example 2: A fisheries management problem", "weight": 1.0} -->

‣ 2.2. Infinite LP characterization ‣ 2. Motivation: Control of MDP and LP Characterization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") are fulfilled; we refer the reader to \[42, Section 7.2\] for further information and detailed analysis.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

We implement the methodology presented in Section 4.2, resulting in a finite random convex program (65. ‣ 4.2. Randomized results in the MDP setting ‣ 4. Semi-infinite to Finite Programs: Randomized Approach ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming")), where the uniform distribution on $K = {S \times A} = {\lbrack\underset{¯}{\kappa},\overline{\kappa}\rbrack}^{2}$ is used to draw the random samples. Figure 4 illustrates three cases with the number of basis functions $n \in {\{ 2,10,100\}}$ and the bound (68b). The colored tubes represent the results between $\lbrack{10\%},{90\%}\rbrack$ quantiles (shaded areas) as well as the means (solid lines) across $400$ independent experiments of the objective performance $J_{n,N}^{AC}$ as a function of the sample size $N$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Randomized approach", "weight": 1.0} -->

It is interesting to note that in this example the optimal solution is captured even with $2$ basis functions and only $N = 20$ random samples. This becomes even more attractive when we compare the results with a direct discretization scheme depicted in \[42, Figure 2\].

<!-- chunk {"id": "body-0096", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

Similar to the LQG example in Section 7.1, we also implement the smoothing methodology for the case of $n = 10$. The simulation results are reported in Figure 5.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Structural convex optimization", "weight": 1.0} -->

(a) A priori error ε and a posteriori error Jn, ηUB − Jn, ηLB (b) Upper bound Jn, ηUB and lower bound Jn, ηLB Figure 5. The results and error bounds are obtained by Algorithm 1 with n = 10 for Example 7.2. The red dotted line is the optimal solution computed as indicated in Figure 4.
