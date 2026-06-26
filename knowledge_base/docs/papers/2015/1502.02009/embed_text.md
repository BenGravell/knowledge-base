## Introduction

The alternating direction method of multipliers (ADMM) seeks to solve the problem with variables $x \in {\mathbb{R}}^{p}$ and $z \in {\mathbb{R}}^{q}$ and constants $A \in {\mathbb{R}}^{r \times p}$, $B \in {\mathbb{R}}^{r \times q}$, and $c \in {\mathbb{R}}^{r}$. ADMM was introduced in Glowinski & Marroco and Gabay & Mercier. More recently, it has found applications in a variety of distributed settings such as model fitting, resource allocation, and classification. A partial list of examples includes Bioucas-Dias & Figueiredo; Wahlberg et al.; Bird; Forero et al.; Sedghi et al.; Li et al.; Wang & Banerjee; Zhang et al.; Meshi & Globerson; Wang et al.; Aslan et al.; Forouzan & Ihler; Romera-Paredes & Pontil; Behmardi et al.; Zhang & Kwok. See Boyd et al. for an overview.

Part of the appeal of ADMM is the fact that, in many contexts, the algorithm updates lend themselves to parallel implementations. The algorithm is given in Algorithm 1. We refer to $\rho > 0$ as the step-size parameter.

1: Input: functions f and g, matrices A and B, vector c, parameter ρ 7: until meet stopping criterion Algorithm 1 Alternating Direction Method of Multipliers A popular variant of Algorithm 1 is over-relaxed ADMM, which introduces an additional parameter $\alpha$ and replaces each instance of $Ax_{k + 1}$ in the $z$ and $u$ updates in Algorithm 1 with The parameter $\alpha$ is typically chosen to lie in the interval $(0,2\rbrack$, but we demonstrate in Section 8 that a larger set of choices can lead to convergence. Over-relaxed ADMM is described in Algorithm 2. When $\alpha = 1$, Algorithm 2 and Algorithm 1 coincide. We will analyze Algorithm 2.

1: Input: functions f and g, matrices A and B, vector c, parameters ρ and α 7: until meet stopping criterion Algorithm 2 Over-Relaxed Alternating Direction Method of Multipliers The conventional wisdom that ADMM works well without any tuning, for instance by setting $\rho = 1$, is often not borne out in practice. Algorithm 1 can be challenging to tune, and Algorithm 2 is even harder. We use the machinery developed in this paper to make reasonable recommendations for setting $\rho$ and $\alpha$ when some information about $f$ is available (Section 8).

In this paper, we give an upper bound on the linear rate of convergence of Algorithm 2 for all $\rho$ and $\alpha$ (Theorem 7), and we give a nearly-matching lower bound (Theorem 8).

Importantly, we show that we can prove convergence rates for Algorithm 2 by numerically solving a $4 \times 4$ semidefinite program (Theorem 6). When we change the parameters of Algorithm 2, the semidefinite program changes. Whereas prior work requires a new proof of convergence for every change to the algorithm, our work automates that process.

Our work builds on the integral quadratic constraint framework introduced in Lessard et al., which uses ideas from robust control to analyze optimization algorithms that can be cast as discrete-time linear dynamical systems. Related ideas, in the context of feedback control, appear in Corless; D'Alto & Corless. Our work provides a flexible framework for analyzing variants of Algorithm 1, including those like Algorithm 2 created by the introduction of additional parameters. In Section 7, we compare our results to prior work.

## Preliminaries and Notation

Let $\overline{\mathbb{R}}$ denote the extended real numbers ${\mathbb{R}} \cup {\{{+ \infty}\}}$. Suppose that $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$ is convex and differentiable, and let $\nabla f$ denote the gradient of $f$. We say that $f$ is strongly convex with parameter $m > 0$ if for all ${x,y} \in {\mathbb{R}}^{d}$, we have When $\nabla f$ is Lipschitz continuous with parameter $L$, then For $0 < m \leq L < \infty$, let $S_{d}{(m,L)}$ denote the set of differentiable convex functions $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$ that are strongly convex with parameter $m$ and whose gradients are Lipschitz continuous with parameter $L$. We let $S_{d}{(0,\infty)}$ denote the set of convex functions ${\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}$. In general, we let $\partial f$ denote the subdifferential of $f$. We denote the $d$-dimensional identity matrix by $I_{d}$ and the $d$-dimensional zero matrix by $0_{d}$. We will use the following results.

### Lemma 1

Suppose that $f \in {S_{d}{(m,L)}}$, where $0 < m \leq L < \infty$. Suppose that $b_{1} = {{\nabla f}{(a_{1})}}$ and $b_{2} = {{\nabla f}{(a_{2})}}$. Then

### Proof

The Lipschitz continuity of $\nabla f$ implies the co-coercivity of $\nabla f$, that is Note that ${f{(x)}} - {\frac{m}{2}{\| x\|}^{2}}$ is convex and its gradient is Lipschitz continuous with parameter $L - m$. Applying the co-coercivity condition to this function and rearranging gives which can be put in matrix form to complete the proof. ∎

### Lemma 2

Suppose that $f \in {S_{d}{(0,\infty)}}$, and suppose that $b_{1} \in {\partial{f{(a_{1})}}}$ and $b_{2} \in {\partial{f{(a_{2})}}}$. Then Lemma 2 is simply the statement that the subdifferential of a convex function is a monotone operator.

When $M$ is a matrix, we use $\kappa_{M}$ to denote the condition number of $M$. For example, $\kappa_{A} = {{{\sigma_{1}{(A)}}/\sigma_{p}}{(A)}}$, where $\sigma_{1}{(A)}$ and $\sigma_{p}{(A)}$ denote the largest and smallest singular values of the matrix $A$. When $f \in {S_{d}{(m,L)}}$, we let $\kappa_{f} = \frac{L}{m}$ denote the condition number of $f$. We denote the Kronecker product of matrices $M$ and $N$ by $M \otimes N$.

## ADMM as a Dynamical System

We group our assumptions together in Assumption 3.

### Assumption 3

We assume that $f$ and $g$ are convex, closed, and proper. We assume that for some $0 < m \leq L < \infty$, we have $f \in {S_{p}{(m,L)}}$ and $g \in {S_{q}{(0,\infty)}}$. We assume that $A$ is invertible and that $B$ has full column rank.

The assumption that $f$ and $g$ are closed (their sublevel sets are closed) and proper (they neither take on the value $- \infty$ nor are they uniformly equal to $+ \infty$) is standard.

We begin by casting over-relaxed ADMM as a discrete-time dynamical system with state sequence $(\xi_{k})$, input sequence $(\nu_{k})$, and output sequences $(w_{k}^{1})$ and $(w_{k}^{2})$ satisfying the recursions for particular matrices $\hat{A}$, $\hat{B}$, ${\hat{C}}^{1}$, ${\hat{D}}^{1}$, ${\hat{C}}^{2}$, and ${\hat{D}}^{2}$ (whose dimensions do not depend on any problem parameters).

First define the functions ${\hat{f},\hat{g}}:{{\mathbb{R}}^{r}\rightarrow\overline{\mathbb{R}}}$ via | | $\hat{f}$ | $= {{({\rho^{- 1}f})} \circ A^{- 1}}$ | | \(3\) | where $B^{\dagger}$ is any left inverse of $B$ and where ${\mathbb{I}}_{{im}B}$ is the $\{ 0,\infty\}$-indicator function of the image of $B$. We define $\kappa = {\kappa_{f}\kappa_{A}^{2}}$ and to normalize we define Note that under Assumption 3, To define the relevant sequences, let the sequences $(x_{k})$, $(z_{k})$, and $(u_{k})$ be generated by Algorithm 2 with parameters $\alpha$ and $\rho$. Define the sequences $(r_{k})$ and $(s_{k})$ by $r_{k} = {Ax_{k}}$ and $s_{k} = {Bz_{k}}$ and the sequence $(\xi_{k})$ by We define the sequence $(\nu_{k})$ as in Proposition 4.

### Proposition 4

There exist sequences $(\beta_{k})$ and $(\gamma_{k})$ with $\beta_{k} = {{\nabla\hat{f}}{(r_{k})}}$ and $\gamma_{k} \in {\partial{\hat{g}{(s_{k})}}}$ such that when we define the sequence $(\nu_{k})$ by then $(\xi_{k})$ and $(\nu_{k})$ satisfy (2a) with the matrices

### Proof

Using the fact that $A$ has full rank, we rewrite the update rule for $x$ from Algorithm 2 as Multiplying through by $A$, we can write This implies that where $\beta_{k + 1} = {{\nabla\hat{f}}{(r_{k + 1})}}$. In the same spirit, we rewrite the update rule for $z$ as It follows that there exists some $\gamma_{k + 1} \in {\partial{\hat{g}{(s_{k + 1})}}}$ such that It follows then that where the second equality follows by substituting. Combining and to simplify the $u$ update, we have Together, and confirm the relation in (2a). ∎

### Corollary 5

Define the sequences $(\beta_{k})$ and $(\gamma_{k})$ as in Proposition 4. Define the sequences $(w_{k}^{1})$ and $(w_{k}^{2})$ via Then the sequences $(\xi_{k})$, $(\nu_{k})$, $(w_{k}^{1})$, and $(w_{k}^{2})$ satisfy (2b) and (2c) with the matrices

## Convergence Rates from Semidefinite Programming

Now, in Theorem 6, we make use of the perspective developed in Section 3 to obtain convergence rates for Algorithm 2. This is essentially the same as the main result of Lessard et al., and we include it because it is simple and self-contained.

### Theorem 6

Suppose that Assumption 3 holds. Let the sequences $(x_{k})$, $(z_{k})$, and $(u_{k})$ be generated by running Algorithm 2 with step size $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\rho_{0}}$ and with over-relaxation parameter $\alpha$. Suppose that $(x_{\ast},z_{\ast},u_{\ast})$ is a fixed point of Algorithm 2, and define Fix $0 < \tau < 1$, and suppose that there exist a $2 \times 2$ positive definite matrix $P \succ 0$ and nonnegative constants ${\lambda^{1},\lambda^{2}} \geq 0$ such that the $4 \times 4$ linear matrix inequality | | $0 \succeq$ | $\begin{bmatrix} | | \(11\) | | | | {{\hat{B}}^{\top}P\hat{A}} & {{\hat{B}}^{\top}P\hat{B}} | | | | | | \end{bmatrix}^{\top}\begin{bmatrix} | | | | | | \end{bmatrix}\begin{bmatrix} | | | is satisfied, where $\hat{A}$ and $\hat{B}$ are defined, where ${\hat{C}}^{1}$, ${\hat{D}}^{1}$, ${\hat{C}}^{2}$, and ${\hat{D}}^{2}$ are defined, and where $M^{1}$ and $M^{2}$ are given by Then for all $k \geq 0$, we have

### Proof

Define $r_{k}$, $s_{k}$, $\beta_{k}$, $\gamma_{k}$, $\xi_{k}$, $\nu_{k}$, $w_{k}^{1}$, and $w_{k}^{2}$ as before. Choose $r_{\ast} = {Ax_{\ast}}$, $s_{\ast} = {Bz_{\ast}}$, and such that $(\xi_{\ast},\nu_{\ast},w_{\ast}^{1},w_{\ast}^{2})$ is a fixed point of the dynamics of and satisfying $\beta_{\ast} = {{\nabla\hat{f}}{(r_{\ast})}}$, $\gamma_{\ast} \in {\partial{\hat{g}{(s_{\ast})}}}$. Now, consider the Kronecker product of the right hand side of and $I_{r}$. Multiplying this on the left and on the right by $\begin{bmatrix} {({\xi_{j} - \xi_{\ast}})}^{\top} & {({\nu_{j} - \nu_{\ast}})}^{\top} \end{bmatrix}$ and its transpose, respectively, we find Lemma 1 and (5a) show that the third term on the right hand side of is nonnegative. Lemma 2 and (5b) show that the fourth term on the right hand side of is nonnegative. It follows that Inducting from $j = 0$ to $k - 1$, we see that for all $k$. It follows that The conclusion follows. ∎ For fixed values of $\alpha$, $\rho_{0}$, $\hat{m}$, $\hat{L}$, and $\tau$, the feasibility of is a semidefinite program with variables $P$, $\lambda^{1}$, and $\lambda^{2}$. We perform a binary search over $\tau$ to find the minimal rate $\tau$ such that the linear matrix inequality in is satisfied. The results are shown in Figure 1 for a wide range of condition numbers $\kappa$, for $\alpha = 1.5$, and for several choices of $\rho_{0}$. In Figure 2, we plot the values $- {1/{\log\tau}}$ to show the number of iterations required to achieve a desired accuracy.

Figure 1: For α = 1.5 and for several choices of ε in ρ0 = κε, we plot the minimal rate τ for which the linear matrix inequality in is satisfied as a function of κ.

Figure 2: For α = 1.5 and for several choices of ε in ρ0 = κε, we compute the minimal rate τ such that the linear matrix inequality in is satisfied, and we plot −1/log τ as a function of κ.

Note that when $\rho_{0} = \kappa^{\varepsilon}$, the matrix $M^{1}$ is given by and so the linear matrix inequality in depends only on $\kappa$ and not on $\hat{m}$ and $\hat{L}$. Therefore, we will consider step sizes of this form (recall from that $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\rho_{0}}$). The choice $\varepsilon = 0$ is common in the literature, but requires the user to know the strong-convexity parameter $\hat{m}$. We also consider the choice $\varepsilon = 0.5$, which produces worse guarantees, but does not require knowledge of $\hat{m}$.

One weakness of Theorem 6 is the fact that the rate we produce is not given as a function of $\kappa$. To use Theorem 6 as stated, we first specify the condition number (for example, $\kappa = 1000$). Then we search for the minimal $\tau$ such that is feasible. This produces an upper bound on the convergence rate of Algorithm 2 (for example, $\tau = 0.9$). To remedy this problem, in Section 5, we demonstrate how Theorem 6 can be used to obtain the convergence rate of Algorithm 2 as a symbolic function of the step size $\rho$ and the over-relaxation parameter $\alpha$.

## Symbolic Rates for Various $\rho$ and $\alpha$

In Section 4, we demonstrated how to use semidefinite programming to produce numerical convergence rates. That is, given a choice of algorithm parameters and the condition number $\kappa$, we could determine the convergence rate of Algorithm 2. In this section, we show how Theorem 6 can be used to prove symbolic convergence rates. That is, we describe the convergence rate of Algorithm 2 as a function of $\rho$, $\alpha$, and $\kappa$. In Theorem 7, we prove the linear convergence of Algorithm 2 for all choices $\alpha \in {}$ and $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\kappa^{\varepsilon}}$, with $\varepsilon \in {({- \infty},\infty)}$. This result generalizes a number of results in the literature. As two examples, Giselsson & Boyd consider the case $\varepsilon = 0$ and Deng & Yin consider the case $\alpha = 1$ and $\varepsilon = 0.5$.

The rate given in Theorem 7 is loose by a factor of four relative to the lower bound given in Theorem 8. However, weakening the rate by a constant factor eases the proof by making it easier to find a certificate for use .

### Theorem 7

Suppose that Assumption 3 holds. Let the sequences $(x_{k})$, $(z_{k})$, and $(u_{k})$ be generated by running Algorithm 2 with parameter $\alpha \in {}$ and with step size $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\kappa^{\varepsilon}}$, where $\varepsilon \in {({- \infty},\infty)}$. Define $x_{\ast}$, $z_{\ast}$, $u_{\ast}$, $\varphi_{k}$, and $\varphi_{\ast}$ as in Theorem 6. Then for all sufficiently large $\kappa$, we have

### Proof

We claim that for all sufficiently large $\kappa$, the linear matrix inequality in is satisfied with the rate $\tau = {1 - \frac{\alpha}{2\kappa^{0.5 + {|\varepsilon|}}}}$ and with certificate The matrix on the right hand side of can be expressed as $- {\frac{1}{4}\alpha\kappa^{- 2}M}$, where $M$ is a symmetric $4 \times 4$ matrix whose last row and column consist of zeros. We wish to prove that $M$ is positive semidefinite for all sufficiently large $\kappa$. To do so, we consider the cases $\varepsilon \geq 0$ and $\varepsilon < 0$ separately, though the two cases will be nearly identical. First suppose that $\varepsilon \geq 0$. In this case, the nonzero entries of $M$ are specified by We show that each of the first three leading principal minors of $M$ is positive for sufficiently large $\kappa$. To understand the behavior of the leading principal minors, it suffices to look at their leading terms. For large $\kappa$, the first leading principal minor (which is simple $M_{11}$) is dominated by the term $4\kappa^{\frac{3}{2} - \varepsilon}$, which is positive. Similarly, the second leading principal minor is dominated by the term $16{({2 - \alpha})}\kappa^{\frac{7}{2} - \varepsilon}$, which is positive. When $\varepsilon > 0$, the third leading principal minor is dominated by the term $128{({2 - \alpha})}\kappa^{5}$, which is positive. When $\varepsilon = 0$, the third leading principal minor is dominated by the term $64\alpha{({2 - \alpha})}^{2}\kappa^{5}$, which is positive. Since these leading coefficients are all positive, it follows that for all sufficiently large $\kappa$, the matrix $M$ is positive semidefinite.

Now suppose that $\varepsilon < 0$. In this case, the nonzero entries of $M$ are specified by As before, we show that each of the first three leading principal minors of $M$ is positive. For large $\kappa$, the first leading principal minor (which is simple $M_{11}$) is dominated by the term $8\kappa^{\frac{3}{2} - \varepsilon}$, which is positive. Similarly, the second leading principal minor is dominated by the term $32{({2 - \alpha})}\kappa^{\frac{7}{2} - \varepsilon}$, which is positive. The third leading principal minor is dominated by the term $128{({2 - \alpha})}\kappa^{5}$, which is positive. Since these leading coefficients are all positive, it follows that for all sufficiently large $\kappa$, the matrix $M$ is positive semidefinite.

The result now follows from Theorem 6 by noting that $P$ has eigenvalues $\alpha$ and $2 - \alpha$. ∎ Note that since the matrix $P$ doesn't depend on $\rho$, the proof holds even when the step size changes at each iteration.

## Lower Bounds

In this section, we probe the tightness of the upper bounds on the convergence rate of Algorithm 2 given by Theorem 6. The construction of the lower bound in this section is similar to a construction given in Ghadimi et al..

Let $Q$ be a $d$-dimensional symmetric positive-definite matrix whose largest and smallest eigenvalues are $L$ and $m$ respectively. Let ${f{(x)}} = {\frac{1}{2}x^{\top}Qx}$ be a quadratic and let ${g{(z)}} = {\frac{\delta}{2}{\| z\|}^{2}}$ for some $\delta \geq 0$. Let $A = I_{d}$, $B = {- I_{d}}$, and $c = 0$. With these definitions, the optimization problem in is solved by $x = z = 0$. The updates for Algorithm 2 are given by Solving for $z_{k}$ in (13b) and substituting the result into (13c) gives $u_{k + 1} = {\frac{\delta}{\rho}z_{k + 1}}$. Then eliminating $x_{k + 1}$ and $u_{k}$ from (13b) using (13a) and the fact that $u_{k} = {\frac{\delta}{\rho}z_{k}}$ allows us to express the update rule purely in terms of $z$ as Note that the eigenvalues of $T$ are given by where $\lambda$ is an eigenvalue of $Q$. We will use this setup to construct a lower bound on the worst-case convergence rate of Algorithm 2 in Theorem 8.

### Theorem 8

Suppose that Assumption 3 holds. The worst-case convergence rate of Algorithm 2, when run with step size $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\kappa^{\varepsilon}}$ and over-relaxation parameter $\alpha$, is lower-bounded by

### Proof

First consider the case $\varepsilon \geq 0$. Choosing $\delta = 0$ and $\lambda = m$,, we see that $T$ has eigenvalue When initialized with $z$ as the eigenvector corresponding to this eigenvalue, Algorithm 2 will converge linearly with rate given exactly, which is lower bounded by the expression in when $\varepsilon \geq 0$.

Now suppose that $\varepsilon < 0$. Choosing $\delta = L$ and $\lambda = L$, after multiplying the numerator and denominator of by $\kappa^{0.5 - \varepsilon}$, we see that $T$ has eigenvalue When initialized with $z$ as the eigenvector corresponding to this eigenvalue, Algorithm 2 will converge linearly with rate given exactly by the left hand side of, which is lower bounded by the expression in when $\varepsilon < 0$. ∎ Figure 3 compares the lower bounds given by with the upper bounds given by Theorem 6 for $\alpha = 1.5$ and for several choices of $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\kappa^{\varepsilon}}$ satisfying $\varepsilon \geq 0$. The upper and lower bounds agree visually on the range of choices $\varepsilon$ depicted, demonstrating the practical tightness of the upper bounds given by Theorem 6 for a large range of choices of parameter values.

Figure 3: For α = 1.5 and for several choices ε in ρ0 = κε, we plot −1/log τ as a function of κ, both for the lower bound on τ given by and the upper bound on τ given by Theorem 6. For each choice of ε in {0.5, 0.25, 0}, the lower and upper bounds agree visually. This agreement demonstrates the practical tightness of the upper bounds given by Theorem 6 for a large range of choices of parameter values.

## Related Work

Several recent papers have studied the linear convergence of Algorithm 1 but do not extend to Algorithm 2. Deng & Yin prove a linear rate of convergence for ADMM in the strongly convex case. Iutzeler et al. prove the linear convergence of a specialization of ADMM to a class of distributed optimization problems under a local strong-convexity condition. Hong & Luo prove the linear convergence of a generalization of ADMM to a multiterm objective in the setting where each term can be decomposed as a strictly convex function and a polyhedral function. In particular, this result does not require strong convexity.

More generally, there are a number of results for operator splitting methods in the literature. Lions & Mercier and Eckstein & Ferris analyze the convergence of several operator splitting schemes. More recently, Patrinos et al. prove the equivalence of forward-backward splitting and Douglas--Rachford splitting with a scaled version of the gradient method applied to unconstrained nonconvex surrogate functions (called the forward-backward envelope and the Douglas--Rachford envelope respectively). Goldstein et al. propose an accelerated version of ADMM in the spirit of Nesterov, and prove a $O{({1/k^{2}})}$ convergence rate in the case where $f$ and $g$ are both strongly convex and $g$ is quadratic.

The theory of over-relaxed ADMM is more limited. Eckstein & Bertsekas prove the convergence of over-relaxed ADMM but do not give a rate. More recently, Davis & Yin analyze the convergence rates of ADMM in a variety of settings. Giselsson & Boyd prove the linear convergence of Douglas--Rachford splitting in the strongly-convex setting. They use the fact that ADMM is Douglas--Rachford splitting applied to the dual problem to derive a linear convergence rate for over-relaxed ADMM with a specific choice of step size $\rho$. Eckstein gives convergence results for several specializations of ADMM, and found that over-relaxation with $\alpha = 1.5$ empirically sped up convergence. Ghadimi et al. give some guidance on tuning over-relaxed ADMM in the quadratic case.

Unlike prior work, our framework requires no assumptions on the parameter choices in Algorithm 2. For example, Theorem 6 certifies the linear convergence of Algorithm 2 even for values $\alpha > 2$. In our framework, certifying a convergence rate for an arbitrary choice of parameters amounts to checking the feasibility of a $4 \times 4$ semidefinite program, which is essentially instantaneous, as opposed to formulating a proof.

## Selecting Algorithm Parameters

In this section, we show how to use the results of Section 4 to select the parameters $\alpha$ and $\rho$ in Algorithm 2 and we show the effect on a numerical example.

Recall that given a choice of parameters $\alpha$ and $\rho$ and given the condition number $\kappa$, Theorem 6 gives an upper bound on the convergence rate of Algorithm 2. Therefore, one approach to parameter selection is to do a grid search over the space of parameters for the choice that minimizes the upper bound provided by Theorem 6. We demonstrate this approach numerically for a distributed Lasso problem, but first we demonstrate that the usual range of $$ for the over-relaxation parameter $\alpha$ is too limited, that more choices of $\alpha$ lead to linear convergence. In Figure 4, we plot the largest value of $\alpha$ found through binary search such that is satisfied for some $\tau < 1$ as a function of $\kappa$. Proof techniques in prior work do not extend as easily to values of $\alpha > 2$. In our framework, we simply change some constants in a small semidefinite program.

Figure 4: As a function of κ, we plot the largest value of α such that is satisfied for some τ < 1. In this figure, we set ε = 0 in ρ0 = κε.

### Distributed Lasso

Following Deng & Yin, we give a numerical demonstration with a distributed Lasso problem of the form Each $A_{i}$ is a tall matrix with full column rank, and so the first term in the objective will be strongly convex and its gradient will be Lipschitz continuous. As in Deng & Yin, we choose $N = 5$ and $\mu = 0.1$. Each $A_{i}$ is generated by populating a $600 \times 500$ matrix with independent standard normal entries and normalizing the columns. We generate each $b_{i}$ via $b_{i} = {{A_{i}x^{0}} + \varepsilon_{i}}$, where $x^{0}$ is a sparse $500$-dimensional vector with $250$ independent standard normal entries, and $\varepsilon_{i} \sim {\mathcal{N}{(0,{10^{- 3}I})}}$.

In Figure 5, we compute the upper bounds on the convergence rate given by Theorem 6 for a grid of values of $\alpha$ and $\rho$. Each line corresponds to a fixed choice of $\alpha$, and we plot only a subset of the values of $\alpha$ to keep the plot manageable. We omit points corresponding to parameter values for which the linear matrix inequality in was not feasible for any value of $\tau < 1$.

Figure 5: We compute the upper bounds on the convergence rate given by Theorem 6 for eighty-five values of α evenly spaced between 0.1 and 2.2 and fifty values of ρ geometrically spaced between 0.1 and 10. Each line corresponds to a fixed choice of α, and we show only a subset of the values of α to keep the plot manageable. We omit points corresponding to parameter values for which is not feasible for any value of τ < 1. This analysis suggests choosing α = 2.0 and ρ = 1.7.

In Figure 6, we run Algorithm 2 for the same values of $\alpha$ and $\rho$. We then plot the number of iterations needed for $z_{k}$ to reach within $10^{- 6}$ of a precomputed reference solution. We plot lines corresponding to only a subset of the values of $\alpha$ to keep the plot manageable, and we omit points corresponding to parameter values for which Algorithm 2 exceeded $1000$ iterations. For the most part, the performance of Algorithm 2 as a function of $\rho$ closely tracked the performance predicted by the upper bounds in Figure 5. Notably, smaller values of $\alpha$ seem more robust to poor choices of $\rho$. The parameters suggested by our analysis perform close to the best of any parameter choices.

Figure 6: We run Algorithm 2 for eighty-five values of α evenly spaced between 0.1 and 2.2 and fifty value of ρ geometrically spaced between 0.1 and 10. We plot the number of iterations required for zk to reach within 10−6 of a precomputed reference solution. We show only a subset of the values of α to keep the plot manageable. We omit points corresponding to parameter values for which Algorithm 2 exceeded 1000 iterations.

## Discussion

We showed that a framework based on semidefinite programming can be used to prove convergence rates for the alternating direction method of multipliers and allows a unified treatment of the algorithm's many variants, which arise through the introduction of additional parameters. We showed how to use this framework for establishing convergence rates, as in Theorem 6 and Theorem 7, and how to use this framework for parameter selection in practice, as in Section 8. The potential uses are numerous. This framework makes it straightforward to propose new algorithmic variants, for example, by introducing new parameters into Algorithm 2 and using Theorem 6 to see if various settings of these new parameters give rise to improved guarantees.

In the case that Assumption 3 does not hold, the most likely cause is that we lack the strong convexity of $f$. One approach to handling this is to run Algorithm 2 on the modified function ${f{(x)}} + {\frac{\delta}{2}{\| x\|}^{2}}$. By completing the square in the $x$ update, we see that this amounts to an extremely minor algorithmic modification (it only affects the $x$ update).

It should be clear that other operator splitting methods such as Douglas--Rachford splitting and forward-backward splitting can be cast in this framework and analyzed using the tools presented here.
