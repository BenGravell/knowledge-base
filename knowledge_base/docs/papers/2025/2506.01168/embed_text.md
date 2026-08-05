<!-- arxiv-full-text:v1 {"arxiv_id": "2506.01168", "source": "arxiv-html"} -->

## INTRODUCTION

We consider the well-studied optimization problem where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is continuously differentiable. A popular approach to solving, particularly when the dimension $d$ is large, is to use iterative gradient-based methods, such as Gradient Descent (GD) and its accelerated variants.

A central question in the study of iterative methods is that of *worst-case convergence rate* over a class of functions $\mathcal{F}$. In this letter, we consider the *root-convergence factor* (also known as geometric convergence rate), denoted $\rho \in {}$, a notion we make precise in Section 2. Associated with the root-convergence factor are two important concepts:

### Lower bounds

$\rho$ is a *lower bound* for $\mathcal{F}$ if for any algorithm, there exists $f \in \mathcal{F}$ and an algorithm initialization such that the algorithm converges no faster than $\rho$.

### Upper bounds

$\rho$ is an *upper bound* for $\mathcal{F}$ if there exists an algorithm such that for all $f \in \mathcal{F}$ and algorithm initializations, the algorithm converges at least as fast as $\rho$.

If $\mathcal{F}$ has matching lower and upper bounds, this $\rho$ and the corresponding algorithm that achieves it are said to be *minimax optimal* for $\mathcal{F}$.

Generally, adding more structure to a function class, such as convexity or Lipschitz properties, makes the minimax rate faster because iterative algorithms can exploit the additional structure to converge more rapidly. We now provide a brief survey of different function classes and their minimax rates. The relationship between these classes is illustrated in the Venn diagram of Fig. 1.

Figure 1: Venn diagram of different function classes. Blue region: strongly convex functions. Red region: twice continuously differentiable functions. This letter focuses on the shaded intersection of these sets, 𝒮m, L2.

The class $\mathcal{F}_{m,L}$ consists of continuously differentiable functions with sector-bounded gradients. Specifically, there exists $x_{\star} \in {\mathbb{R}}^{d}$ (the optimal point) and constants $0 < m \leq L$ such that ${\left( {{L{({x - x_{\star}})}} - {{\nabla f}{(x)}}} \right)^{\mathsf{T}}\left( {{{\nabla f}{(x)}} - {m{({x - x_{\star}})}}} \right)} \geq 0$ for all $x \in {\mathbb{R}}^{d}$. Functions in this class may be nonconvex but nevertheless have a unique local (and global) minimizer. The minimax rate for $\mathcal{F}_{m,L}$ is $\rho = \frac{\kappa - 1}{\kappa + 1}$ where $\kappa\operatorname{:-}\frac{L}{m}$, and is achieved by GD with stepsize $\alpha = \frac{2}{L + m}$.

The class $\mathcal{S}_{m,L}^{1}$ consists of functions that have Lipschitz gradient with Lipschitz constant $L$ and are strongly convex with parameter $m$. The superscript "1" indicates that $f \in C^{1}$, which follows from Lipschitz gradients. One can show that $\mathcal{S}_{m,L}^{1} \subset \mathcal{F}_{m,L}$. The minimax rate for $\mathcal{S}_{m,L}^{1}$ is $\rho = {1 - \frac{1}{\sqrt{\kappa}}}$, and was recently proved in using an exact characterization of $\mathcal{S}_{m,L}^{1}$ via interpolation conditions and the Performance Estimation paradigm. The same lower bound was obtained in a parallel line of work by viewing algorithms as discrete-time Lur'e systems and applying integral quadratic constraints (IQCs) or dissipativity theory. Specifically, the set $\mathcal{S}_{m,L}^{1}$ was over-approximated using Zames--Falb IQCs, leading to an upper bound that turned out to be exact. The minimax rate for $\mathcal{S}_{m,L}^{1}$ is achieved by the Triple Momentum (TM) Method and the Information Theoretic Exact Method (ITEM).

The class $\mathcal{Q}_{m,L} \subset \mathcal{S}_{m,L}^{1}$ consists of quadratic functions of the form ${f{(x)}} = {{x^{\mathsf{T}}Qx} + {p^{\mathsf{T}}x} + r}$, with ${mI_{d}} \preceq Q \preceq {LI_{d}}$, and we have $\mathcal{Q}_{m,L} \subset \mathcal{S}_{m,L}^{1}$. The minimax rate for $\mathcal{Q}_{m,L}$ is $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$. The lower bound was proved by Nemirovsky and Nesterov \[11, §2.1.4\]. There are several minimax optimal methods for $\mathcal{Q}_{m,L}$, the simplest of which is Polyak's Heavy Ball (HB) method \[12, §3.2.1\]. Polyak used Lyapunov's indirect method to show that HB converges *locally* for any $f \in \mathcal{S}_{m,L}^{1}$ provided that $f$ is twice continuously differentiable ($f \in C^{2}$) in a neighborhood of the optimal point. In other words, HB converges on $\mathcal{S}_{m,L}^{1}$ when initialized sufficiently close to the optimal point and enjoys the same fast rate as for $\mathcal{Q}_{m,L}$! If incorrectly initialized, HB need not converge at all on $\mathcal{S}_{m,L}^{1}$.

The aforementioned minimax optimal algorithms are described in Section 2.1 and summarized in Table 1.

Polyak's observation raises an interesting possibility, which forms the starting point for the present work. If we consider the function class $\mathcal{S}_{m,L}^{2}\operatorname{:-}{\mathcal{S}_{m,L}^{1} \cap C^{2}}$, then by Lyapunov's indirect method, any globally convergent method will converge at its *local rate*, which may be faster than the minimax rate of $\mathcal{S}_{m,L}^{1}$. This function class satisfies $\mathcal{Q}_{m,L} \subset \mathcal{S}_{m,L}^{2} \subset \mathcal{S}_{m,L}^{1}$ and may be characterized succinctly as functions whose Hessians satisfy ${mI_{d}} \preceq {{\nabla^{2}f}{(x)}} \preceq {LI_{d}}$. Functions of interest in this category include regularized logistic loss, exponential family negative log-likelihoods with bounded natural parameters, and Moreau envelope smoothing of any $f \in \mathcal{S}_{m,L}^{1}$.

Our main result is a new algorithm, $C^{2}$-Momentum (C2M). We show that C2M achieves an upper bound of $\max\left\{ \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1},\rho_{\text{C2M}} \right\}$ on $\mathcal{S}_{m,L}^{2}$, where $\rho_{\text{C2M}} < {1 - \sqrt{\frac{2}{\kappa}}}$. This corresponds to an iteration complexity that is faster than the minimax rate of $\mathcal{S}_{m,L}^{1}$ by a factor of $\sqrt{2}$.

Notable related works are the recent papers, which use the same idea of optimizing the local convergence rate while enforcing global convergence. Specifically, these works develop re-tunings of HB and TM that converge globally on $\mathcal{F}_{m,L}$ but have optimized local rates because they also assume $f \in C^{2}$ locally near the optimal point.

The rest of this letter is organized as follows. In Section 2 we describe C2M, in Section 3 we prove convergence results, in Section 4 we present some numerical results, and in Section 5 we discuss implications and future directions.

## MAIN RESULT

In this section, we describe our proposed algorithm, state its main convergence result, and use root locus arguments to provide intuition behind the algorithm parameters.

### Algorithm Form

We consider iterative first-order algorithms parameterized by ${\alpha,\beta,\eta} \in {\mathbb{R}}$ of the form for $k \geq 0$ with initial conditions ${x_{0},x_{- 1}} \in {\mathbb{R}}^{d}$. We can interpret such an algorithm as a linear time-invariant (LTI) system $G$ in feedback with the gradient $\nabla f$, where the transfer function^11^1As a slight abuse of notation, we use the same symbol to refer to both an LTI system and its transfer function. from the gradient $u_{k}$ to the point $y_{k}$ at which the gradient is evaluated is A minimal state-space realization of the reduced system $g$ is Despite its simplicity, the form can represent *all* algorithms referenced in Section 1 when $\alpha,\beta,\eta$ are suitably chosen (GD, HB, TM, ITEM, GHB, GAG). Table 1 shows parameters for the minimax methods discussed in Section 1. $\frac{\kappa - 1}{\kappa + 1}$ $\frac{\rho^{2}}{2 - \rho}$ $\frac{\rho^{2}}{{({1 + \rho})}{({2 - \rho})}}$ $1 - \frac{1}{\sqrt{\kappa}}$ $\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$ Table 1: Minimax-optimal methods for several function classes.

### $C^{2}$-Momentum

### Definition 1 (C2M)

Given parameters ${m,L,\rho} \in {\mathbb{R}}$ with $0 < m \leq L$, $\kappa\operatorname{:-}\frac{L}{m}$, and $\rho \in {}$, the $C^{2}$-Momentum (C2M) algorithm is of the form with parameters The C2M parameters depend on $\rho$, which we choose based on the condition number $\kappa$ of the objective function: where $\rho_{\text{C2M}}$ is the smallest positive root of the polynomial When $\kappa < {9 + {4\sqrt{5}}}$, the parameters of C2M reduce to those of HB in Table 1. For $\kappa \geq {9 + {4\sqrt{5}}}$, we in general want to pick $\rho$ as small as possible, but we will see that proving global asymptotic stability requires a strict inequality, so in practice we can choose $\rho = {\rho_{\text{C2M}} + \varepsilon}$ for some small $\varepsilon > 0$. The C2M stepsizes are defined in terms of the root $\rho_{\text{C2M}}$ of the polynomial $p{(\kappa,\rho)}$. The following result (i) shows that this quantity is well defined in that the polynomial does have a positive root, and (ii) provides bounds on this root that will be used in the analysis. The proof is in Section.1.

### Lemma 1

Suppose $\kappa \geq {9 + {4\sqrt{5}}}$. The polynomial $p{(\kappa,\rho)}$ defined in has exactly one real root $\rho_{\text{C2M}}$ in the open interval $\left( \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1},{1 - \sqrt{\frac{2}{\kappa}}} \right)$. Moreover, $\rho_{\text{C2M}}$ is the smallest positive root and ${p{(\kappa,\rho)}} < 0$ for all $\rho \in \left( \rho_{\text{C2M}},{1 - \sqrt{\frac{2}{\kappa}}} \right\rbrack$.

### Main Result

To describe our main result, we first define the root-convergence factor of an algorithm, which is a way to characterize its rate of convergence; see \[15, §9.2\].

### Definition 2

Let $\{ x_{k}\}$ be a sequence that converges to a point $x_{\star}$. Then, the root-convergence factor of $\{ x_{k}\}$ is Moreover, the worst-case root-convergence factor of an algorithm over a function class $\mathcal{F}$ is the supremum of the root-convergence factors over all sequences produced by the algorithm when applied to a function $f \in \mathcal{F}$.

We now state our main convergence result for C2M over the class $\mathcal{S}_{m,L}^{2}$. A full proof is included in Section 3.

### Theorem 1 (Upper bound for C2M)

Consider the C2M method defined in (5 ‣ 2.2 𝐶²-Momentum ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions")) with parameter $\rho$ chosen according to. An upper bound for the worst-case root-convergence factor of C2M over the function class $\mathcal{S}_{m,L}^{2}$ is $\rho$.

### Root Locus Interpretation

Figure 2: Root locus of C2M. The locus has a double root at z = ρ at gain m and a single root at z = −ρ at gain L.

Before rigorously analyzing the convergence of C2M, we first provide intuition behind the C2M parameters (5 ‣ 2.2 𝐶²-Momentum ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions")) using a root locus argument.

Consider the general algorithm applied to a function $f \in \mathcal{Q}_{m,L} \subset \mathcal{S}_{m,L}^{2}$ with Hessian $Q$. By diagonalizing the Hessian, the iterates separate into $d$ decoupled systems, each in (positive) feedback with an eigenvalue $q_{i}$ of $Q$. Since the objective function is $L$-smooth, $m$-strongly convex, and twice continuously differentiable, its Hessian has eigenvalues in the interval $\lbrack m,L\rbrack$. Therefore, we can study worst-case local convergence by analyzing the eigenvalues of $A + {qBC}$ for $q \in {\lbrack m,L\rbrack}$. These closed-loop eigenvalues are solutions of the root locus $0 = {1 - {qg{(z)}}}$ for $q \in {\lbrack m,L\rbrack}$. The parameters of C2M are the solutions to the following conditions: The root locus passes through $z = {- \rho}$ when $q = L$.

The root locus has a double root at $z = \rho$ when $q = m$.

The visual reasoning for these two conditions is illustrated in Fig. 2, which shows the root locus of $1 - {qg{(z)}}$ as $q$ varies. As $q\rightarrow 0$, the roots are the poles of $g{(z)}$, which are $\beta$ and $1$. These roots meet at $z = \rho$, circle around the zero at $z = \frac{\eta}{1 + \eta}$, then break in on the negative real axis, with one root converging to the zero and the other going to $- \infty$ along the real axis. By enforcing the above two conditions, the root locus remains entirely inside the $\rho$-circle for all $q \in {\lbrack m,L\rbrack}$. In terms of the transfer function, these conditions are that where the last two equations are for the double root. Straightforward calculations show that the parameters (5 ‣ 2.2 𝐶²-Momentum ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions")) for C2M are the unique solution to the equations.

## CONVERGENCE ANALYSIS

We now prove the main convergence result for C2M from 1 ‣ 2.3 Main Result ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions"). Our proof consists of two steps. First, we show that the algorithm is globally asymptotically stable, meaning that the iterates converge to the minimizer of $f$ for all initial conditions. Once we have global convergence, we then show that the worst-case root-convergence factor is $\rho$ by analyzing the linearization of the algorithm about its equilibrium.

### Global Stability via Frequency-Domain Analysis

It is convenient to shift the dynamics of the algorithm about its optimal point $x_{\star}$, which satisfies ${{\nabla f}{(x_{\star})}} = 0$. To this effect, define ${\overset{\sim}{x}}_{k}\operatorname{:-}{x_{k} - x_{\star}}$, ${\overset{\sim}{y}}_{k}\operatorname{:-}{y_{k} - x_{\star}}$, ${\overset{\sim}{u}}_{k} = u_{k}$, and ${\overset{\sim}{f}{(y)}}\operatorname{:-}{f{({y + x_{\star}})}}$. Then, we can rewrite as: Convergence of the algorithm $G$ applied to $f$ is therefore equivalent to convergence of $G$ applied to $\overset{\sim}{f}$. In other words, we may assume without loss of generality that $x_{\star} = 0$.

To verify global asymptotic stability, we use integral quadratic constraints (IQCs). In discrete time, these are defined as follows (see ), where $\ell_{2}^{n}$ denotes the space of square-summable sequences on ${\mathbb{R}}^{n}$.

### Definition 3

Signals $y \in \ell_{2}^{n_{y}}$ and $u \in \ell_{2}^{n_{u}}$ with associated $z$-transforms $\hat{y}{(z)}$ and $\hat{u}{(z)}$ satisfy the IQC defined by a measurable, bounded, and Hermitian matrix-valued function $\Pi:{{\mathbb{T}}\rightarrow{\mathbb{C}}^{{({n_{y} + n_{u}})} \times {({n_{y} + n_{u}})}}}$ if where ${\mathbb{T}}\operatorname{:-}\left\{ {z \in {\mathbb{C}}} \middle| {{|z|} = 1} \right\}$ is the unit circle in the complex plane. A bounded operator $\Delta:{\ell_{2}^{n_{y}}\rightarrow\ell_{2}^{n_{u}}}$ satisfies the IQC defined by $\Pi$ if holds for all $y \in \ell_{2}^{n_{y}}$ with $u = {\Delta{(y)}}$.

It is well known (see for example ) that the gradient of a smooth strongly convex function can be described using IQCs.

### Proposition 1

The operator $\Delta:{\ell_{2}^{d}\rightarrow\ell_{2}^{d}}$ defined by ${({\Delta{(y)}})}_{k}\operatorname{:-}{{\nabla\overset{\sim}{f}}{(y_{k})}}$ for all $k \geq 0$ and $y \in \ell_{2}^{d}$, where $\overset{\sim}{f} \in \mathcal{S}_{m,L}^{1}$ and ${{\nabla\overset{\sim}{f}}{}} = 0$ satisfies the O'Shea--Zames--Falb IQC $\Pi_{m,L} \otimes I_{d}$, where and $h{(z)}$ is any transfer function with impulse response $\{ h_{k}\}$ satisfying $\left\| h \right\|_{1} = {\sum_{k = {- \infty}}^{\infty}{|h_{k}|}} \leq 1$ and $h_{k} \geq 0$ for all $k$.

While $\Delta$ satisfies the IQC $\Pi_{m,L} \otimes I_{d}$, to analyze the interconnection of the algorithm $G$ with $\Delta$ using the main IQC theorem (see 2 ‣ 3.1 Global Stability via Frequency-Domain Analysis ‣ 3 CONVERGENCE ANALYSIS ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions")), we will first need to perform a loop transformation (see, e.g., \[19, §6.6\]) so that the zero operator is contained in the class of transformed uncertainties. Doing so, the feedback interconnection of $G$ and $\Delta$ is equivalent to the feedback interconnection of $\overset{\sim}{G}$ and $\overset{\sim}{\Delta}$, where and the transformed operator is given by Using properties of shifting and scaling the gradient of smooth strongly convex functions \[2, §2.4\], $\overset{\sim}{\Delta}$ satisfies the IQC $\Pi_{{- 1},1} \otimes I_{d}$ if and only if $\Delta$ satisfies the IQC $\Pi_{m,L} \otimes I_{d}$. We are now ready to apply the following main IQC result.

### Proposition 2 (Discrete-time IQC result \[17, Thm. 2\])

Fix $\rho \in {}$. Suppose that $\overset{\sim}{G}$ is stable, $\overset{\sim}{\Delta}$ is a bounded causal operator, and the interconnection of $\overset{\sim}{G}$ and $\overset{\sim}{\Delta}$ is well-posed, for every $\tau \in {\lbrack 0,1\rbrack}$, $\tau\overset{\sim}{\Delta}$ satisfies the IQC $\Pi$, and the following frequency-domain inequality holds: Then the feedback interconnection of $\overset{\sim}{G}$ and $\overset{\sim}{\Delta}$ is stable.

Applying 2 ‣ 3.1 Global Stability via Frequency-Domain Analysis ‣ 3 CONVERGENCE ANALYSIS ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions") therefore yields the following.

### Proposition 3

Algorithm is globally asymptotically stable for all $f \in \mathcal{S}_{m,L}^{1}$ if $\left({1 - {\frac{L + m}{2}g{(z)}}} \right)^{- 1}$ is stable and the following frequency-domain inequality (FDI) holds: where $h{(z)}$ satisfies $\left\| h \right\|_{1} \leq 1$ and $h_{k} \geq 0$ for all $k \in {\mathbb{Z}}$.

### Proof 3.1

The stability condition is equivalent to stability of $\overset{\sim}{G}$. It is straightforward to verify that the interconnection of $\overset{\sim}{G}$ and $\overset{\sim}{\Delta}$ is well-posed and that $\tau\overset{\sim}{\Delta}$ satisfies the IQC $\Pi = {\Pi_{{- 1},1} \otimes I_{d}}$ for all $\tau \in {\lbrack 0,1\rbrack}$. Therefore, the first two conditions in 2 ‣ 3.1 Global Stability via Frequency-Domain Analysis ‣ 3 CONVERGENCE ANALYSIS ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions") hold for the transformed system $\overset{\sim}{G}$ and the IQC $\Pi$. It remains to show that the FDI in (iii) is equivalent to that. To that end, we first write the numerator and denominator of $\overset{\sim}{g}$ as Using this relationship along with ${M^{\mathsf{T}}\Pi_{{- 1},1}M} = \Pi_{m,L}$, the FDI in (iii) of 2 ‣ 3.1 Global Stability via Frequency-Domain Analysis ‣ 3 CONVERGENCE ANALYSIS ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions") is Therefore, the FDI in (iii) is equivalent to that. From 2 ‣ 3.1 Global Stability via Frequency-Domain Analysis ‣ 3 CONVERGENCE ANALYSIS ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions"), the interconnection of $\overset{\sim}{G}$ and $\overset{\sim}{\Delta}$ is stable, which via loop shifting implies the interconnection of $G$ and $\Delta$ is stable. Finally, (input-output) stability means that all signals have bounded norms. Therefore, $\left\| \overset{\sim}{x} \right\| < \infty\Longrightarrow{\lim_{k\rightarrow\infty}{\overset{\sim}{x}}_{k}} = 0\Longrightarrow{\lim_{k\rightarrow\infty}x_{k}} = x_{\star}$.

We use 3 with ${h{(z)}} = z^{- 1}$ to show that C2M is convergent by directly verifying the FDI. First, the condition that $\left({1 - {\frac{L + m}{2}g{(z)}}} \right)^{- 1}$ is bounded follows from the root locus argument in Section 2.4; see the following Section 3.2 for a more rigorous argument. Letting $z = {x + {i\sqrt{1 - x^{2}}}}$ for $x \in {\lbrack{- 1},1\rbrack}$ and substituting the C2M parameters, it is straightforward to verify that the FDI is satisfied when $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$ and $\kappa < {9 + {4\sqrt{5}}}$. In the other case with $\kappa > {9 + {4\sqrt{5}}}$, the FDI reduces to the inequality The right-hand side of is a quadratic in $x$. To show that this inequality holds, we will use the following.

### Lemma 2

Suppose $\rho \in {\lbrack 0,1\rbrack}$ and $\kappa > 1$. Then, Since $\rho < {1 - \sqrt{\frac{2}{\kappa}}}$ by assumption, it follows from 2 that ${\kappa{({1 - \rho})}^{2}} > 2 > {1 + \rho}$. Therefore, the leading coefficient of the quadratic is negative. Maximizing the right-hand side of, this inequality holds if where $p{(\kappa,\rho)}$ is the polynomial. The denominator is positive from the prior argument. Moreover, $p{(\kappa,\rho)}$ is negative for any $\rho \in \left(\rho_{\text{C2M}},{1 - \sqrt{\frac{2}{\kappa}}} \right\rbrack$ by 1, so the FDI is satisfied. Therefore, C2M is globally asymptotically stable for any $\rho$ satisfying.

### Local Convergence

While the root locus interpretation provides intuition behind the local convergence of C2M, we now use Lyapunov's indirect method along with the Jury criterion to systematically prove local convergence; see for similar analyses in other settings. We begin by characterizing the worst-case root convergence factor in terms of the system matrices.

### Lemma 3

The worst-case root-convergence factor of the algorithm over the function class $\mathcal{S}_{m,L}^{2}$ is the maximum spectral radius of $A + {qBC}$ over $q \in {\lbrack m,L\rbrack}$.

### Proof 3.2

From the linear convergence theorem \[15, Thm. 10.1.4\], the root-convergence factor of the algorithm is the spectral radius of its linearization evaluated at the equilibrium. In particular, let $\{ x_{k}\}$ denote the sequence produced by applying algorithm to a function $f \in \mathcal{S}_{m,L}^{2}$ for some initial conditions ${x_{0},x_{- 1}} \in {\mathbb{R}}^{d}$. Let $Q$ denote the Hessian of $f$ evaluated at the minimizer of $f$. Then the root-convergence factor of the sequence $\{ x_{k}\}$ is the spectral radius of the linearization ${A \otimes I_{d}} + {{({BC})} \otimes Q}$, where $\otimes$ denotes the Kronecker product. Since $Q$ is real and symmetric, it is diagonalizable. Applying this diagonalization to the linearized system yields ${A \otimes I_{d}} + {{{({BC})} \otimes \text{diag}}{(q_{1},\ldots,q_{d})}}$, where $q_{1},\ldots,q_{d}$ are the eigenvalues of $Q$. Therefore, the worst-case root-convergence factor over the function class $\mathcal{S}_{m,L}^{2}$ is the maximum spectral radius of $A + {qBC}$ over $q \in {\lbrack m,L\rbrack}$.

Based on 3, we can characterize the worst-case root-convergence factor using the eigenvalues of $A + {qBC}$. We next analyze these eigenvalues using the Jury criterion. Recall that a polynomial $z^{2} + {a_{1}z} + a_{0}$ with real coefficients has roots in the closed unit disk if and only if \[21, §4.5\]^22^2The reference states the results for the roots to be contained in the open unit disk, which is described by the corresponding strict inequalities. Since the roots of a polynomial depend continuously on its coefficients, the corresponding result for the closed unit disk holds with non-strict inequalities.

The characteristic polynomial of the closed-loop system matrix $A + {qBC}$ is the quadratic ${\chi{(z)}} = {z^{2} + {{({{q\alpha{({1 + \eta})}} - {({1 + \beta})}})}z} + {({\beta - {q\alpha\eta}})}}$. Applying the Jury criterion to the scaled polynomial $\chi{({\rho z})}$, the closed-loop eigenvalues are in the closed $\rho$-disk if and only if for all $q \in {\lbrack m,L\rbrack}$. Since each inequality is linear in $q$, it suffices to enforce the inequality at the endpoints $q \in {\{ m,L\}}$. Substituting the C2M parameters, this system of inequalities reduces to The lower bound on $\rho$ is the minimax rate for $\mathcal{Q}_{m,L}$. Since all parameters $\rho$ in satisfy these conditions, we have that all eigenvalues of $A + {qBC}$ are in the $\rho$-disk. Therefore, from 3, the parameter $\rho$ is the worst-case root-convergence factor of C2M, which completes the proof of 1 ‣ 2.3 Main Result ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions").

### Iteration Complexity

It is common in optimization to characterize algorithm convergence using *iteration complexity* \[11, §1.1.2\]. Iteration complexity is an expression for how the worst-case number of iterations $N$ required to reach a specified error $\varepsilon$ scales as a function of problem parameters such as $\kappa$, expressed asymptotically as $\varepsilon\rightarrow 0$ and $\kappa\rightarrow\infty$. If the convergence rate is $\rho$ as defined in 2, then $\left\| {x_{k} - x_{\star}} \right\| \leq {c{(k)}\rho^{k}}$, where $c{(k)}$ grows sub-exponentially in $k$. We seek the smallest $N$ such that ${c{(N)}\rho^{N}} \leq \varepsilon$. Rearranging, we obtain ${{{\log c}{(N)}} + {N{\log\rho}}} \leq {\log\varepsilon}$. Since $c{(N)}$ is sub-exponential, it is dominated by the linear term in $N$ as $\varepsilon\rightarrow 0$ (and therefore $N\rightarrow\infty$), so we neglect it. We are left with $N \geq {\frac{- 1}{\log\rho}{\log\frac{1}{\varepsilon}}}$. Next, we expand $\frac{- 1}{\log\rho}$ as a function of $\kappa\rightarrow\infty$, keeping only the most significant term. For example, if $\rho = {1 - \frac{c}{\sqrt{\kappa}}}$, Based on the minimax rate of TM in Table 1 ($c = 1$), we conclude that $N_{\text{TM}} \gtrsim {\sqrt{\kappa}{\log\frac{1}{\varepsilon}}}$. Similarly, for HB, we have $\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1} = {1 - \frac{2}{\sqrt{\kappa} + 1}} \approx {1 - \frac{2}{\sqrt{\kappa}}}$ ($c = 2$), so $N_{\text{HB}} \gtrsim {\frac{\sqrt{\kappa}}{2}{\log\frac{1}{\varepsilon}}}$.

For C2M, we do not have a nice expression for $\rho_{\text{C2M}}$, but we can nevertheless find an asymptotic analytic expansion for it about $\kappa\rightarrow\infty$, which leads to the bounds Therefore, $c = \sqrt{2}$ and $N_{\text{C2M}} \gtrsim {\frac{\sqrt{\kappa}}{\sqrt{2}}{\log\frac{1}{\varepsilon}}}$. In other words, C2M is faster than TM by a factor of $\sqrt{2}$.

In contrast, GD has iteration complexity $N_{\text{GD}} \gtrsim {\frac{\kappa}{2}{\log\frac{1}{\varepsilon}}}$. In the optimization literature, methods with the $\sqrt{\kappa}$ factor instead of merely $\kappa$ are called *accelerated methods*. We can visualize iteration complexity by plotting $\frac{- 1}{\log\rho}$ versus $\kappa$ on a log-log scale (we omit the $\log\frac{1}{\varepsilon}$ factor); see Fig. 3. We also included a plot for GD (see Table 1).

We see in Fig. 3 that non-accelerated methods (GD, GAG) have an asymptotic slope of $1$ whereas accelerated methods (C2M, TM) have an asymptotic slope of $\frac{1}{2}$.

Figure 3: Iteration complexity of several iterative methods applied to 𝒮m, L2. The proposed C2M method outperforms TM, which is minimax optimal on 𝒮m, L1, by exploiting a faster local convergence rate. Similarly, GAG outperforms GD, which is minimax optimal on ℱm, L.

## NUMERICAL VALIDATION

We simulate our proposed algorithm C2M along with several other first-order methods on a function chosen to showcase worst-case behavior. We used the function \[8, §IV\] where $g{(w)}$ is $\frac{1}{2}w^{2}e^{- {r/w}}$ if $w > 0$ and zero if $w \leq 0$. When $r > 0$ and $0 < m \leq L$ and $\left\| \begin{bmatrix} \end{bmatrix} \right\| = 1$, such functions satisfy $f \in \mathcal{S}_{m,L}^{2}$. We chose the parameters $L = 1$, $m = 10^{- 3}$, $r = 10^{- 3}$, $p = 2$, $a_{1} = {}$, $a_{2} = {(0,0.002)}$, and $b_{1} = b_{2} = 100$. All methods were initialized at $x_{0} = 0$.

In Fig. 4, we plot error as a function of iteration. The function $f$ elicits worst-case behavior from GD, HB, and TM. In other words, GD and TM converge at their respective minimax rates for $\mathcal{F}_{m,L}$ and $\mathcal{S}_{m,L}^{1}$. Since $f \notin \mathcal{Q}_{m,L}$, HB is only locally convergent. In our simulation, we see that HB does not converge; however, if we were to initialize HB sufficiently close to $x_{\star}$, then it would converge at least as fast as the minimax rate for $\mathcal{Q}_{m,L}$. Our proposed C2M exploits additional smoothness in the objective to converge globally at a rate that is always faster than the minimax $\mathcal{S}_{m,L}^{1}$ rate. Likewise, GAG, which is globally convergent on $\mathcal{F}_{m,L}$, is slightly faster than GD, which is minimax-optimal on $\mathcal{F}_{m,L}$.

Figure 4: Simulation results for a function f ∈ 𝒮m, L2 (see Section 4). Solid lines are simulation results for the specified method; black lines are minimax rates for different function classes (see Table 1); the dotted purple line is our theoretical upper bound (worst-case) rate for C2M.

## DISCUSSION

The proposed C2M algorithm is the first method, to the best of the authors' knowledge, that is designed specifically for the function class $\mathcal{S}_{m,L}^{2}$. The minimax rate for this function class, however, is not known, in contrast to the function classes $\mathcal{S}_{m,L}^{1}$ and $\mathcal{Q}_{m,L}$. Finding this minimax rate or even lower bounds are interesting open problems.

The parameters of C2M are related to two other algorithms from the literature. As we have already seen, C2M reduces to HB when $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$. Moreover, the general C2M parameters are identical (after appropriate transformations) to those of GAG \[14, Cor. 1.1\]. This makes sense, since the work also considers the family of algorithms and is optimizing for local convergence. The two cases differ, however, in the choice of $\rho$, since GAG is optimized over the function class $\mathcal{F}_{m,L}$ defined in Section 1 rather than $\mathcal{S}_{m,L}^{2}$.

### 1 Proof of 1

We apply Sturm's theorem \[22, Thm. 2.62\] to $p{(\kappa,\rho)}$ as a polynomial in $\rho$. Define the Sturm sequence where $\text{rem}{}$ denotes the remainder after polynomial division (considered as polynomials in $\rho$), and the sequence terminates when $p_{i}$ is constant, which occurs for $i \leq 7$ since $p$ is degree $7$ in $\rho$. Evaluating the Sturm sequence at $\rho = 0$ and $\rho = 1$ yields 5 sign changes and 3 sign changes, respectively. Therefore, there are two real roots in the interval $$. Moreover, $p$ is positive when $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$, negative when $\rho = {1 - \sqrt{\frac{2}{\kappa}}}$, and positive when $\rho = 1$. By the intermediate value theorem, we conclude that there is exactly one real root in each interval $\left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1},{1 - \sqrt{\frac{2}{\kappa}}} \right)$ and $\left({1 - \sqrt{\frac{2}{\kappa}}},1 \right)$, and the value of $p$ is negative for all $\rho \in \left(\rho_{\text{C2M}},{1 - \sqrt{\frac{2}{\kappa}}} \right\rbrack$. \\QED
