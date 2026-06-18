## Introduction

Matrix completion is the problem of recovering a low rank matrix from partially observed entries. It has been widely used in collaborative filtering and recommender systems, dimension reduction and multi-class learning. There has been extensive work on designing efficient algorithms for matrix completion with guarantees. One earlier line of results (see and the references therein) rely on convex relaxations. These algorithms achieve strong statistical guarantees, but are quite computationally expensive in practice.

More recently, there has been growing interest in analyzing non-convex algorithms for matrix completion. Let $M \in {\mathbb{R}}^{d \times d}$ be the target matrix with rank $r \ll d$ that we aim to recover, and let $\Omega = {\{{(i,j)}:{M_{i,j}\text{~is observed}}\}}$ be the set of observed entries. These methods are instantiations of optimization algorithms applied to the objective^11^1In this paper, we focus on the symmetric case when the true $M$ has a symmetric decomposition $M = {ZZ^{T}}$. Some of previous papers work on the asymmetric case when $M = {ZW^{T}}$, which is harder than the symmetric case.,

These algorithms are much faster than the convex relaxation algorithms, which is crucial for their empirical success in large-scale collaborative filtering applications.

Most of the theoretical analysis of the nonconvex procedures require careful initialization schemes: the initial point should already be close to optimum^22^2The work of De Sa et al. is an exception, which gives an algorithm that uses fresh samples at every iteration to solve matrix completion (and other matrix problems) approximately.. In fact, Sun and Luo showed that after this initialization the problem is effectively strongly-convex, hence many different optimization procedures can be analyzed by standard techniques from convex optimization.

However, in practice people typically use a random initialization, which still leads to robust and fast convergence. Why can these practical algorithms find the optimal solution in spite of the non-convexity? In this work we investigate this question and show that the matrix completion objective has no spurious local minima. More precisely, we show that any local minimum $X$ of objective function $f{( \cdot )}$ is also a global minimum with ${f{(X)}} = 0$, and recovers the correct low rank matrix $M$.

Our characterization of the structure in the objective function implies that (stochastic) gradient descent from arbitrary starting point converge to a global minimum. This is because gradient descent converges to a local minimum, and every local minimum is also a global minimum.

### Main results

Assume the target matrix $M$ is symmetric and each entry of $M$ is observed with probability $p$ independently ^33^3The entries $(i,j)$ and $(j,i)$ are the same. With probability $p$ we observe both entries and otherwise we observe neither.. We assume $M = {ZZ^{\top}}$ for some matrix $Z \in {\mathbb{R}}^{d \times r}$.

There are two known issues with matrix completion. First, the choice of $Z$ is not unique since $M = {{({ZR})}{({ZR})}^{\top}}$ for any orthonormal matrix $Z$. Our goal is to find one of these equivalent solutions.

Another issue is that matrix completion is impossible when $M$ is "aligned" with standard basis. For example, when $M$ is the identity matrix in its first $r \times r$ block, we will very likely be observing only 0 entries. To address this issue, we make the following standard assumption:

### Assumption 1

For any row $Z_{i}$ of $Z$, we have

Moreover, $Z$ has a bounded condition number ${{{\sigma_{\max}{(Z)}}/\sigma_{\min}}{(Z)}} = \kappa$.

Throughout this paper we think of $\mu$ and $\kappa$ as small constants, and the sample complexity depends polynomially on these two parameters. Also note that this assumption is independent of the choice of $Z$: all $Z$ such that ${ZZ^{T}} = M$ have the same row norms and Frobenius norm.

This assumption is similar to the "incoherence" assumption. Our assumption is the same as the one used in analyzing non-convex algorithms.

We enforce $X$ to also satisfy this assumption by a regularizer

where $R{(X)}$ is a function that penalizes $X$ when one of its rows is too large. See Section 4 and Section 5 for the precise definition. Our main result shows that in this setting, the regularized objective function has no spurious local minimum:

### Theorem 1.1

\[Informal\] All local minimum of the regularized objective (1.2) satisfy ${XX^{T}} = {ZZ^{T}} = M$ when $p \geqslant {{\text{poly}{(\kappa,r,\mu,{\log d})}}/d}$.

Combined with the results in (see Theorem 2.3) ^44^4Theorem 1.1, as state informally above, doesn't guarantee that $f$ satisfies the condition in Theorem 2.3. See its technical version, Theorem 5.3, which shows that the condition of Theorem 2.3 is satisfied., we have,

### Theorem 1.2 (Informal)

With high probability, stochastic gradient descent on the regularized objective (1.2) will converge to a solution $X$ such that ${XX^{T}} = {ZZ^{T}} = M$ in polynomial time from any starting point. Gradient descent will converge to such a point with probability 1 from a random starting point.

Our results are also robust to noise. Even if each entry is corrupted with Gaussian noise of standard deviation ${\mu^{2}{\| Z\|}_{F}^{2}}/d$ (comparable to the magnitude of the entry itself!), we can still guarantee that all the local minima satisfy ${\|{{XX^{T}} - {ZZ^{T}}}\|}_{F} \leqslant \varepsilon$ when $p$ is large enough. See the discussion in Appendix B for results on noisy matrix completion.

Our main technique is to show that every point that satisfies the first and second order necessary conditions for optimality must be a desired solution. To achieve this we use new ideas to analyze the effect of the regularizer and show how it is useful in modifying the first and second order conditions to exclude any spurious local minimum.

### Related Work

### Matrix Completion

The earlier theoretical works on matrix completion analyzed the nuclear norm minimization. This line of work has the cleanest and strongest theoretical guarantees; showed that if ${|\Omega|} \gtrsim {dr\mu^{2}{\log^{2}d}}$ the nuclear norm convex relaxation recovers the exact underlying low rank matrix. The solution can be computed via the solving a convex program in polynomial time. However the primary disadvantage of nuclear norm methods is their computational and memory requirements --- the fastest known provable algorithms require $O{(d^{2})}$ memory and thus at least $O{(d^{2})}$ running time, which could be both prohibitive for moderate to large values of $d$. Many algorithms have been proposed to improve the runtime (either theoretically or empirically) (see, for examples and the reference therein). Burer and Monteiro proposed factorizing the optimization variable $\hat{M} = {XX^{T}}$, and optimizing over $X \in {\mathbb{R}}^{d \times r}$ instead of $\hat{M} \in {\mathbb{R}}^{d \times d}$. This approach only requires $O{({dr})}$ memory, and a single gradient iteration takes time $O{({|\Omega|})}$, so has much lower memory requirement and computational complexity than the nuclear norm relaxation. On the other hand, the factorization causes the optimization problem to be non-convex in $X$, which leads to theoretical difficulties in analyzing algorithms. Keshavan et al. showed that well-initialized gradient descent recovers $M$. The works showed that well-initialized alternating least squares, block coordinate descent, and gradient descent converges $M$. Jain and Netrapalli showed a fast algorithm by iteratively doing gradient descent in the relaxed space and projecting to the set of low-rank matrices. The work analyzes stochastic gradient descent with fresh samples at each iteration from random initialization and shows that it approximately converge to the optimal solution. provided a more unified analysis by showing that with careful initialization many algorithms, including gradient descent and alternating least squares, succeed. accomplished this by showing an analog of strong convexity in the neighborhood of the solution $M$.

### Non-convex Optimization

Recently, a line of work analyzes non-convex optimization by separating the problem into two aspects: the geometric aspect which shows the function has no spurious local minimum and the algorithmic aspect which designs efficient algorithms can converge to local minimum that satisfy first and (relaxed versions) of second order necessary conditions.

Our result is the first that explains the geometry of the matrix completion objective. Similar geometric results are only known for a few problems: SVD/PCA phase retrieval/synchronization, orthogonal tensor decomposition, dictionary learning. The matrix completion objective requires different tools due to the sampling of the observed entries, as well as carefully managing the regularizer to restrict the geometry. Parallel to our work Bhojanapalli et al. showed similar results for matrix sensing, which is closely related to matrix completion. Loh and Wainwright showed that for many statistical settings that involve missing/noisy data and non-convex regularizers, any stationary point of the non-convex objective is close to global optima; furthermore, there is a unique stationary point that is the global minimum under stronger assumptions.

On the algorithmic side, it is known that second order algorithms like cubic regularization and trust-region algorithms converge to local minima that approximately satisfy first and second order conditions. Gradient descent is also known to converge to local minima from a random starting point. Stochastic gradient descent can converge to a local minimum in polynomial time from any starting point. All of these results can be applied to our setting, implying various heuristics used in practice are guaranteed to solve matrix completion.

## Preliminaries

### Notations

For $\Omega \subset {{\lbrack d\rbrack} \times {\lbrack d\rbrack}}$, let $P_{\Omega}$ be the linear operator that maps a matrix $A$ to $P_{\Omega}{(A)}$, where $P_{\Omega}{(A)}$ has the same values as $A$ on $\Omega$, and $0$ outside of $\Omega$.

We will use the following matrix norms: $\parallel \cdot \parallel_{F}$ the frobenius norm, $\parallel \cdot \parallel$ spectral norm, ${|A|}_{\infty}$ elementwise infinity norm, and ${|A|}_{p\rightarrow q} = {\max_{{\| x\|}_{p} = 1}{\| A\|}_{q}}$. We use the shorthand ${\| A\|}_{\Omega} = {\|{P_{\Omega}A}\|}_{F}$. The trace inner product of two matrices is ${\langle A,B\rangle} = {{tr}{({A^{\top}B})}}$, and $\sigma_{\min}{(X)}$, $\sigma_{\max}{(X)}$ are the smallest and largest singular values of $X$. We also use $X_{i}$ to denote the $i$-th row of a matrix $X$.

### Necessary conditions for Optimality

Given an objective function ${f{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, we use ${\nabla f}{(x)}$ to denote the gradient of the function, and ${\nabla^{2}f}{(x)}$ to denote the Hessian of the function (${\nabla^{2}f}{(x)}$ is an $n \times n$ matrix where ${\lbrack{{\nabla^{2}f}{(x)}}\rbrack}_{i,j} = {\frac{\partial^{2}}{\partial{x_{i}{\partial x_{j}}}}f{(x)}}$). It is well known that local minima of the function $f{(x)}$ must satisfy some necessary conditions:

### Definition 2.1

A point $x$ satisfies the first order necessary condition for optimality (later abbreviated as first order optimality condition) if ${{\nabla f}{(x)}} = 0$. A point $x$ satisfies the second order necessary condition for optimality (later abbreviated as second order optimality condition)if ${{\nabla^{2}f}{(x)}} \succeq 0$.

These conditions are necessary for a local minimum because otherwise it is easy to find a direction where the function value decreases. We will also consider a relaxed second order necessary condition, where we only require the smallest eigenvalue of the Hessian ${\nabla^{2}f}{(x)}$ to be not very negative:

### Definition 2.2

For $\tau \geqslant 0$, a point $x$ satisfies the $\tau$-relaxed second order optimality condition, if ${{\nabla^{2}f}{(x)}} \succeq {- {\tau \cdot I}}$.

This relaxation to the second order condition makes the conditions more robust, and allows for efficient algorithms.

### Theorem 2.3

Let $f$ be twice-differentiable function form ${\mathbb{R}}^{d}$ to $\mathbb{R}$. Suppose there exist ${\varepsilon_{0},\tau_{0}} > 0$ and a universal constant $c > 0$ such that if a point $x$ satisfies ${\parallel{{\nabla f}{(x)}}\parallel} \leqslant \varepsilon \leqslant \varepsilon_{0}$ and ${{\nabla^{2}f}{(x)}} \succeq {- {\tau_{0} \cdot I}}$, then $x$ is $\varepsilon^{c}$-close to a global minimum of $f$. Then, many optimization algorithms including cubic regularization, trust-region, and stochastic gradient descent, can find a global minimum of $f$ up to $\delta$ error in $\ell_{2}$ norm in domain in time ${poly}{({1/\delta},{1/\tau_{0}},d)}$.

## Proof Strategy: "simple" proofs are more generalizable

In this section, we demonstrate the key ideas behind our analysis using the rank $r = 1$ case. In particular, we first give a "simple" proof for the fully observed case. Then we show this simple proof can be easily generalized to the random observation case. We believe that this proof strategy is applicable to other statistical problems involving partial/noisy observations. The proof sketches in this section are only meant to be illustrative and may not be fully rigorous in various places. We refer the readers to Section 4 and Section 5 for the complete proofs.

In the rank $r = 1$ case, we assume $M = {zz^{\top}}$, where ${\| z\|} = 1$, and ${\| z\|}_{\infty} \leqslant \frac{\mu}{\sqrt{d}}$. Let $\varepsilon \ll 1$ be the target accuracy that we aim to achieve in this section and let $p = {{\text{poly}{(\mu,{\log d})}}/{({d\varepsilon})}}$.

For simplicity, we focus on the following domain $\mathcal{B}$ of incoherent vectors where the regularizer $R{(x)}$ vanishes,

Inside this domain $\mathcal{B}$, we can restrict our attention to the objective function without the regularizer, defined as,

The global minima of $\overset{\sim}{g}{( \cdot )}$ are $z$ and $- z$ with function value 0. Our goal of this section is to (informally) prove that all the local minima of $\overset{\sim}{g}{( \cdot )}$ are $O{(\sqrt{\varepsilon})}$-close to $\pm z$. In later section we will formally prove that the only local minima are $\pm z$.

### Lemma 3.1 (Partial observation case, informally stated)

Under the setting of this section, in the domain $\mathcal{B}$, all local mimina of the function $\overset{\sim}{g}{( \cdot )}$ are $O{(\sqrt{\varepsilon})}$-close to $\pm z$.

It turns out to be insightful to consider the full observation case when $\Omega = {{\lbrack d\rbrack} \times {\lbrack d\rbrack}}$. The corresponding objective is

Observe that $\overset{\sim}{g}{(x)}$ is a sampled version of the $g{(x)}$, and therefore we expect that they share the same geometric properties. In particular, if $g{(x)}$ does not have spurious local minima then neither does $\overset{\sim}{g}{(x)}$.

### Lemma 3.2 (Full observation case, informally stated)

Under the setting of this section, in the domain $\mathcal{B}$, the function $g{( \cdot )}$ has only two local minima $\{{\pm z}\}$.

Before introducing the "simple" proof, let us first look at a delicate proof that does not generalize well.

### Difficult to Generalize Proof of Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum")

We compute the gradient and Hessian of $g{(x)}$,

Therefore, a critical point $x$ satisfies ${{\nabla g}{(x)}} = {{Mx} - {{\| x\|}^{2}x}} = 0$, and thus it must be an eigenvector of $M$ and ${\| x\|}^{2}$ is the corresponding eigenvalue. Next, we prove that the hessian is only positive definite at the top eigenvector. Let $x$ be an eigenvector with eigenvalue $\lambda = {\| x\|}^{2}$, and $\lambda$ is strictly less than the top eigenvalue $\lambda^{\ast}$. Let $z$ be the top eigenvector. We have that ${\langle z,{{\nabla^{2}g}{(x)}z}\rangle} = {{- {\langle z,{Mz}\rangle}} + {\| x\|}^{2}} = {{- \lambda^{\ast}} + \lambda} < 0$, which shows that $x$ is not a local minimum. Thus only $z$ can be a local minimizer, and it is easily verified that ${\nabla^{2}g}{(z)}$ is indeed positive definite.

The difficulty of generalizing the proof above to the partial observation case is that it uses the properties of eigenvectors heavily. Suppose we want to imitate the proof above for the partial observation case, the first difficulty is how to solve the equation ${\overset{\sim}{g}{(x)}} = {P_{\Omega}{({M - {xx^{\top}}})}x} = 0$. Moreover, even if we could have a reasonable approximation for the critical points (the solution of ${{\nabla\overset{\sim}{g}}{(x)}} = 0$), it would be difficult to examine the Hessian of these critical points without having the orthogonality of the eigenvectors.

### "Simple" and Generalizable proof

The lessons from the subsection above suggest us find an alternative proof for the full observation case which is generalizable. The alternative proof will be simple in the sense that it doesn't use the notion of eigenvectors and eigenvalues. Concretely, the key observation behind most of the analysis in this paper is the following,

Proofs that consist of inequalities that are linear in $\mathbf{1}_{\Omega}$ are often easily generalizable to partial observation case.

Here statements that are linear in $\mathbf{1}_{\Omega}$ mean the statements of the form ${\sum_{ij}{1_{{(i,j)} \in \Omega}T_{ij}}} \leqslant a$. We will call these kinds of proofs "simple" proofs in this section. Roughly speaking, the observation follows from the law of large numbers --- Suppose ${T_{ij},{(i,j)}} \in {{\lbrack d\rbrack} \times {\lbrack d\rbrack}}$ is a sequence of bounded real numbers, then the sampled sum ${\sum_{{(i,j)} \in \Omega}T_{ij}} = {\sum_{i,j}{\mathbf{1}_{{(i,j)} \in \Omega}T_{ij}}}$ is an accurate estimate of the sum $p{\sum_{i,j}T_{ij}}$, when the sampling probability $p$ is relatively large. Then, the mathematical implications of ${p{\sum T_{ij}}} \leqslant a$ are expected to be similar to the implications of ${\sum_{{(i,j)} \in \Omega}T_{ij}} \leqslant a$, up to some small error introduced by the approximation. To make this concrete, we give below informal proofs for Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum") and Lemma 3.1. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum") that only consists of statements that are linear in $\mathbf{1}_{\Omega}$. Readers will see that due to the linearity, the proof for the partial observation case (shown on the right column) is a direct generalization of the proof for the full observation case (shown on the left column) via concentration inequalities (which will be discussed more at the end of the section).

A "simple" proof for Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum").

### Claim 1f

Suppose $x \in \mathcal{B}$ satisfies ${{\nabla g}{(x)}} = 0$, then ${\langle x,z\rangle}^{2} = {\| x\|}^{4}$.

### Proof

Intuitively, this proof says that the norm of a critical point $x$ is controlled by its correlation with $z$. Here at the lasa sampling version of the f aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ∎

### Generalization to Lemma 3.1. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum")

### Claim 1p

Suppose $x \in \mathcal{B}$ satisfies ${{\nabla\overset{\sim}{g}}{(x)}} = 0$, then ${\langle x,z\rangle}^{2} = {{\| x\|}^{4} - \varepsilon}$.

### Proof

Imitating the proof on the left, we have

The last step uses the fact that equation (3.5) and (3.6) are approximately equal up to scaling factor $p$ for any $x \in \mathcal{B}$, since (3.6) is a sampled version of (3.5). ∎

### Claim 2f

If $x \in \mathcal{B}$ has positive Hessian ${{\nabla^{2}g}{(x)}} \succeq 0$, then ${\| x\|}^{2} \geqslant {1/3}$.

### Proof

By the assumption on $x$, we have that ${\langle z,{{\nabla^{2}g}{(x)}z}\rangle} \geqslant 0$. Calculating the quadratic form of the Hessian (see Proposition 4.1 for details),

### Claim 2p

If $x \in \mathcal{B}$ has positive Hessian ${{\nabla^{2}\overset{\sim}{g}}{(x)}} \succeq 0$, then ${\| x\|}^{2} \geqslant {{1/3} - \varepsilon}$.

### Proof

Imitating the proof on the left, calculating the quadratic form over the Hessian at $z$ (see Proposition 4.1), we have aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Here we use the fact that ${\langle z,{{\nabla^{2}\overset{\sim}{g}}{(x)}z}\rangle} \approx {p{\langle z,{{\nabla^{2}g}{(x)}z}\rangle}}$ for any $x \in \mathcal{B}$. ∎

With these two claims, we are ready to prove Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum") and 3.1. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum") by using another step that is linear in $\mathbf{1}_{\Omega}$.

### Proof of Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum")

By Claim 1f and 2f, we have $x$ satisfies ${\langle x,z\rangle}^{2} \geqslant {\| x\|}^{4} \geqslant {1/9}$. Moreover, we have that ${{\nabla g}{(x)}} = 0$ implies

Then by Claim 1f again we obtain ${\langle x,z\rangle}^{2} = 1$, and therefore $x = {\pm z}$. aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ∎

### Proof of Lemma 3.1. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum")

By Claim 1p and 2p, we have $x$ satisfies ${\langle x,z\rangle}^{2} \geqslant {\| x\|}^{4} \geqslant {{1/9} - {O{(\varepsilon)}}}$. Moreover, we have that ${{\nabla\overset{\sim}{g}}{(x)}} = 0$ implies

Since (3.10) is the sampled version of equation (3.9), we expect they lead to the same conclusion up to some approximation. Then by Claim 1p again we obtain ${\langle x,z\rangle}^{2} = {1 \pm {O{(\varepsilon)}}}$, and therefore $x$ is $O{(\sqrt{\varepsilon})}$-close to either of $\pm z$. ∎

### Subtleties regarding uniform convergence

In the proof sketches above, our key idea is to use concentration inequalities to link the full observation objective $g{(x)}$ with the partial observation counterpart. However, we require a uniform convergence result. For example, we need a statement like "w.h.p over the choice of $\Omega$, equation (3.5) and (3.6) are similar to each other up to scaling". This type of statement is often only true for $x$ inside the incoherent ball $\mathcal{B}$. The fix to this is the regularizer. For non-incoherent $x$, we will use a different argument that uses the property of the regularizer. This is besides the main proof strategy of this section and will be discussed in subsequent sections.

## Warm-up: Rank-1 Case

In this section, using the general proof strategy described in previous section, we provide a formal proof for the rank-1 case. In subsection 4.1, we formally work out the proof sketches of Section 3. In subsection 4.2, we prove that due to the effect of the regularizer, outside incoherent ball $\mathcal{B}$, the objective function doesn't have any local minimum.

In the rank-1 case, the objective function simplifies to,

Here we use the the regularization $R{(x)}$

The parameters $\lambda$ and $\alpha$ will be chosen later as in Theorem 4.2. We will choose $\alpha > {{10\mu}/\sqrt{d}}$ so that ${R{(x)}} = 0$ for incoherent $x$, and thus it only penalizes coherent $x$. Moreover, we note $R{(x)}$ has Lipschitz second order derivative. ^55^5This is the main reason for us to choose $4$-th power instead of $2$-nd power.

We first state the optimality conditions, whose proof is deferred to Appendix A.

### Proposition 4.1

The first order optimality condition of objective (4.1) is,

and the second order optimality condition requires:

Moreover, The $\tau$-relaxed second order optimality condition requires

We give the precise version of Theorem 1.1 for the rank-$1$ case.

### Theorem 4.2

For $p \geqslant \frac{c\mu^{6}{\log^{1.5}d}}{d}$ where $c$ is a large enough absolute constant, set $\alpha = {10\mu\sqrt{1/d}}$ and $\lambda \geqslant {{\mu^{2}p}/\alpha^{2}}$.Then, with high probability over the randomness of $\Omega$, the only points in ${\mathbb{R}}^{d}$ that satisfy both first and second order optimality conditions (or $\tau$-relaxed optimality conditions with $\tau < {0.1p}$) are $z$ and $- z$.

In the rest of this section, we will first prove that when $x$ is constrained to be incoherent (and hence the regularizer is 0 and concentration is straightforward) and satisfies the optimality conditions, then $x$ has to be $z$ or $- z$. Then we go on to explain how the regularizer helps us to change the geometry of those points that are far away from $z$ so that we can rule out them from being local minimum. For simplicity, we will focus on the part that shows a local minimum $x$ must be close enough to $z$.

### Lemma 4.3

In the setting of Theorem 4.2, suppose $x$ satisfies the first-order and second-order optimality condition (4.2) and (4.3). Then when $p$ is defined as in Theorem 4.2,

This turns out to be the main challenge. Once we proved $x$ is close, we can apply the result of Sun and Luo (see Lemma C.1. ‣ Appendix C Finding the Exact Factorization ‣ Matrix Completion has No Spurious Local Minimum")), and obtain Theorem 4.2.

### Handling incoherent $x$

To demonstrate the key idea, in this section we restrict our attention to the subset of ${\mathbb{R}}^{d}$ which contains incoherent $x$ with $\ell_{2}$ norm bounded by 1, that is, we consider,

Note that the desired solution $z$ is in $\mathcal{B}$, and the regularization $R{(x)}$ vanishes inside $\mathcal{B}$.

The following lemmas assume $x$ satisfies the first and second order optimality conditions, and deduce a sequence of properties that $x$ must satisfy.

### Lemma 4.4

Under the setting of Theorem 4.2, with high probability over the choice of $\Omega$, for any $x \in \mathcal{B}$ that satisfies second-order optimality condition (4.3) we have,

The same is true if $x \in \mathcal{B}$ only satisfies $\tau$-relaxed second order optimality condition for $\tau \leqslant {0.1p}$.

### Proof

We plug in $v = z$ in the second-order optimality condition (4.3), and obtain that

Intuitively, when restricted to $\Omega$, the squared Frobenius on the LHS and the quadratic form on the RHS should both be approximately a $p$ fraction of the unrestricted case. In fact, both LHS and RHS can be written as the sum of terms of the form $\langle{P_{\Omega}{({uv^{T}})}},{P_{\Omega}{({st^{T}})}}\rangle$, because

Therefore we can use concentration inequalities (Theorem D.1), and simplify the equation

where $\varepsilon = {O{({\mu^{2}\sqrt{\frac{\log d}{pd}}})}}$. Similarly, by Theorem D.1 again, we have

(Note that even we use the $\tau$-relaxed second order optimality condition, the RHS only becomes ${{1.99p{\| z\|}^{4}} - {2p{\langle x,z\rangle}^{2}}} \pm {O{({p\varepsilon})}}$ which does not effect the later proofs.)

Therefore plugging in estimates above back into equation (4.6), we have that

which implies that ${6p{\| x\|}^{2}{\| z\|}^{2}} \geqslant {{2p{\| x\|}^{2}{\| z\|}^{2}} + {4p{\langle x,z\rangle}^{2}}} \geqslant {{2p{\| z\|}^{4}} - {O{({p\varepsilon})}}}$. Using ${\| z\|}^{2} = 1$, and $\varepsilon$ being sufficiently small, we complete the proof. ∎

Next we use first order optimality condition to pin down another property of $x$ -- it has to be close to $z$ after scaling. Note that this doesn't mean directly that $x$ has to be close to $z$ since $x = 0$ also satisfies first order optimality condition (and therefore the conclusion (4.7) below).

### Lemma 4.5

With high probability over the randomness of $\Omega$, for any $x \in \mathcal{B}$ that satisfies first-order optimality condition (4.2), we have that $x$ also satisfies

where $\varepsilon = {\overset{\sim}{O}{({\mu^{3}{({pd})}^{- {1/2}}})}}$.

### Proof

Note that since $x \in \mathcal{B}$, we have ${R{(x)}} = 0$. Therefore first-order optimality condition says that

Again, intuitively we hope ${P_{\Omega}{({zz^{T}})}} \approx {pzz^{T}}$ and ${P_{\Omega}{({xx^{T}})}x} \approx {p{\| x\|}^{2}x}$. These are made precise by the concentration inequalities Lemma D.4 and Theorem D.2 respectively.

By Theorem D.2, we have that with high probability over the choice of $\Omega$, for every $x \in \mathcal{B}$,

where $\varepsilon = {\overset{\sim}{O}{({\mu^{3}{({pd})}^{- {1/2}}})}}$. Similarly, by Lemma D.4, we have that for with high probability over the choice of $\Omega$,

for $\varepsilon = {\overset{\sim}{O}{({\mu^{2}{({pd})}^{- {1/2}}})}}$. Therefore for every $x$,

Plugging in estimates (4.10) and (4.9) into equation (4.8), we complete the proof. ∎

Finally we combine the two optimality conditions and show equation (4.7) implies $xx^{T}$ must be close to $zz^{T}$.

### Lemma 4.6

Suppose vector $x$ satisfies that ${\| x\|}^{2} \geqslant {1/4}$, and that ${\left. \parallel{{{\langle z,x\rangle}z} - {{\| x\|}^{2}x}}\parallel \right. \leqslant \delta}.$ Then for $\delta \in {(0,0.1)}$,

### Proof

We write $z = {{ux} + v}$ where $u \in {\mathbb{R}}$ and $v$ is a vector orthogonal to $x$. Now we know ${{\langle z,x\rangle}z} = {{u^{2}{\| x\|}^{2}x} + {u{\| x\|}^{2}v}}$, therefore

In particular, we know ${|{1 - u^{2}}|} \leqslant {4\delta}$ and ${u{\| v\|}} \leqslant {4\delta}$. This means ${|u|} \in {1 \pm {3\delta}}$ and ${\| v\|} \leqslant {8\delta}$. Now we expand ${xx^{T}} - {zz^{T}}$:

It is clear that all the terms have norm bounded by $O{(\delta)}$, therefore $\left. \parallel{{xx^{\top}} - {zz^{\top}}}\parallel \right._{F}^{2} \leqslant {O{(\delta)}}$. ∎

### Extension to general $x$

Figure 1: Partition of ℝd into regions where our Lemmas apply. For example, Lemma 3.8 rules out the possibility that a point x in the green region is local minimum. Here, The green region is the intersection of ℓ∞ norm ball and ℓ2 norm ball. Both the white region and yellow region have non-zero gradient but for different reasons.

We have shown when $x$ is incoherent and satisfies first and second order optimality conditions, then it must be close to $z$ or $- z$. Now we need to consider more general cases when $x$ may have some very large coordinates. Here the main intuition is that the first order optimality condition with a proper regularizer is enough to guarantee that $x$ cannot have a entry that is too much bigger than $\mu/\sqrt{d}$.

### Lemma 4.7

With high probability over the choice of $\Omega$, for any $x$ that satisfies first-order order optimality condition (4.2), we have

Here we recall that $\alpha$ was chosen to be ${10\mu}/\sqrt{d}$ and $\lambda$ is chosen to be large so that the $\alpha$ dominates the second term $\mu\sqrt{p/\lambda}$ in the setting of Theorem 4.2.

### Proof of Lemma 4.7

Suppose $i^{\star} = {\max_{j}{|x_{j}|}}$. Without loss of generality, suppose $x_{i^{\star}} \geqslant 0$. Suppose $i^{\star}$-th row of $\Omega$ consists of entries with index ${\lbrack i\rbrack} \times S_{i^{\star}}$. If ${|x_{i^{\star}}|} \leqslant {2\alpha}$, we are done. Therefore in the rest of the proof we assume ${|x_{i^{\star}}|} > {2\alpha}$. Note that when $p \geqslant {{c{({\log d})}}/d}$ for sufficiently large constant $c$, with high probability over the choice of $\Omega$, we have ${|S_{i^{\star}}|} \leqslant {2pd}$. In the rest of argument we are working with such an $\Omega$ with ${|S_{i^{\star}}|} \leqslant {2pd}$.

We will compare the $i^{\star}$-th coordinate of LHS and RHS of first-order optimality condition (4.2). For preparation, we have

where the last step we used the fact that ${|S_{i^{\star}}|} \leqslant {2pd}$. Moreover, we have that

Now plugging in the bounds above into the $i^{\star}$-th coordinate of equation (4.2), we obtain

which implies that ${|x_{i^{\star}}|} \leqslant {4\sqrt{{p\mu^{2}}/\lambda}}$. ∎

Setting $\lambda \geqslant {{\mu^{2}p}/\alpha^{2}}$ and $\alpha = {10\mu\sqrt{1/d}}$, Lemma 4.7 ensures that any $x$ that satisfies first-order optimality condition is the following ball,

Then we would like to continue to use arguments similar to Lemma 4.4 and 4.5. However, things have become more complicated as now we need to consider the contribution of the regularizer.

### Lemma 4.8 (Extension of Lemma 4.4)

In the setting of Theorem 4.2, with high probability over the choice of $\Omega$, suppose $x \in \mathcal{B}^{\prime}$ satisfies second-order optimality condition (4.3) or $\tau$-relaxed condition for $\tau \leqslant {0.1p}$, we have ${\| x\|}^{2} \geqslant {1/8}$.

The guarantees and proofs are very similar to Lemma 4.4. The main intuition is that we can restrict our attentions to coordinates whose regularizer is equal to 0. See Section A for details.

We will now deal with first order optimality condition. We first write out the basic extension of Lemma 4.5, which follows from the same proof except we now include the regularizer term.

### Lemma 4.9 (Basic extension of Lemma 4.5)

With high probability over the randomness of $\Omega$, for any $x \in \mathcal{B}^{\prime}$ that satisfies first-order optimality condition (4.2), we have that $x$ also satisfies

where $\varepsilon = {\overset{\sim}{O}{({\mu^{6}{({pd})}^{- {1/2}}})}}$ and $\gamma = {\lambda/{({2p})}} \geqslant 0$.

Next we will show that we can remove the regularizer term, the main observation here is nonzero entries ${\nabla R}{(x)}$ all have the same sign as the corresponding entries in $x$. See Section A for details.

### Lemma 4.10

Suppose $x \in \mathcal{B}^{\prime}$ satisfies that ${\| x\|}^{2} \geqslant {1/8}$, under the same assumption as Lemma 4.9. ‣ 4.2 Extension to general 𝑥 ‣ 4 Warm-up: Rank-1 Case ‣ Matrix Completion has No Spurious Local Minimum"). we have,

Finally we combine Lemma 4.7, Lemma 4.8. ‣ 4.2 Extension to general 𝑥 ‣ 4 Warm-up: Rank-1 Case ‣ Matrix Completion has No Spurious Local Minimum"), Lemma 4.10 and Lemma 4.6 to prove Lemma 4.3. The argument are also summarized in Figure 1, where we partition ${\mathbb{R}}^{d}$ into regions where our lemmas apply.

## Rank-r case

In this section we show how to extend the results in Section 4 to recover matrices of rank $r$. Here we still use the same proof strategy of Section 3. Though for simplicity we only write down the proof for the partial observation case, while the analysis for the full observation case (which was our starting point) can be obtained by substituting ${\lbrack d\rbrack} \times {\lbrack d\rbrack}$ for $\Omega$ everywhere.

Recall that in this case we assume the original matrix $M = {ZZ^{T}}$, where $Z \in {\mathbb{R}}^{d \times r}$. We also assume Assumption 1. The objective function is very similar to the rank 1 case

where ${{R{(X)}} = {\sum_{i = 1}^{d}{r{({\| X_{i}\|})}}}}.$ Recall that ${r{(t)}} = {{({{|t|} - \alpha})}^{4}{\mathbb{I}}_{t \geqslant \alpha}}$. Here $\alpha$ and $\lambda$ are again parameters that we will determined later.

Without loss of generality, we assume that ${\| Z\|}_{F}^{2} = r$ in this section. This implies that ${\sigma_{\max}{(Z)}} \geqslant 1 \geqslant {\sigma_{\min}{(Z)}}$. Now we shall state the first and second order optimality conditions:

### Proposition 5.1

If $X$ is a local optimum of objective function (5.1), its first order optimality condition is,

and the second order optimality condition is equivalent to

Note that the regularizer now is more complicated than the one dimensional case, but luckily we still have the following nice property.

### Proposition 5.2

We have that ${{\nabla R}{(X)}} = {\GammaX}$ where $\Gamma \in {\mathbb{R}}^{d \times d}$ is a diagonal matrix with $\Gamma_{ii} = {\frac{4{({{\| X_{i}\|} - \alpha})}^{4}}{\| X_{i}\|}{\mathbb{I}}_{{\| X_{i}\|} \geqslant \alpha}}$. As a direct consequence, ${\langle{({{\nabla R}{(X)}})}_{i},X_{i}\rangle} \geqslant 0$ for every $i \in {\lbrack d\rbrack}$.

Now we are ready to state the precise version of Theorem 1.1:

### Theorem 5.3

Suppose $p \geqslant {C{\max{\{{\mu^{6}\kappa^{16}r^{4}},{\mu^{4}\kappa^{4}r^{6}}\}}}d^{- 1}{\log^{2}d}}$ where $C$ is a large enough constant. Let ${\alpha = {{32\mu\kappar}/\sqrt{d}}},{\lambda \geqslant {{\mu^{2}rp}/\alpha^{2}}}$. Then with high probability over the randomness of $\Omega$, any local minimum $X$ of $f{( \cdot )}$ satisfies that ${f{(X)}} = 0$, and in particular, ${ZZ^{\top}} = {XX^{\top}}$.

Moreover, If $X$ satisfies that ${\|{{\nabla f}{(X)}}\|}_{F} \leqslant \delta \leqslant {{p\sigma^{3}{(Z)}}/C}$ and ${{\nabla^{2}f}{(X)}} \succeq {- {{{1/C} \cdot \mu^{2}}\kappar^{2}p^{1/2}d^{- {1/2}}I}}$, then $X$ is an approximate global minimum in the sense that ${{\|{{XX^{\top}} - M}\|}_{F}^{2} \leqslant {O{({\delta/p})}}}.$

The proof of this Theorem follows from a similar path as Theorem 4.2. We first notice that because of the regularizer, any matrix $X$ that satisfies first order optimality condition must be somewhat incoherent (this is analogues to Lemma 4.7):

### Lemma 5.4

Suppose ${|S_{i}|} \leqslant {2pd}$. Then for any $X$ satisfies 1st order optimality (5.2), we have

### Proof

Assume $i^{\star} = {{argmax}_{i}{\| X_{i}\|}}$. Suppose the $i$th row of $\Omega$ consists of entries with index ${\lbrack i\rbrack} \times S_{i}$. If ${\| X_{i^{\star}}\|} \leqslant {2\alpha}$, then we are done. Therefore in the rest of the proof we assume ${\| X_{i^{\star}}\|} \geqslant {2\alpha}$.

We will compare the $i$-th row of LHS and RHS of (5.2). For preparation, we have

Then we have that

Therefore we can bound the $\ell_{2}$ norm of LHS of 1st order optimality condition (5.2) by

Next we lowerbound the norm of the RHS of equation (5.2). We have that

which implies that

Using Proposition 5.2 we obtain that

Therefore plugging in equation above and equation (5.6) into 1st order optimality condition (5.2). We obtain that ${\| X_{i^{\star}}\|} \leqslant \sqrt{{8\mu^{2}rp}/\lambda}$ which completes the proof. ∎

Next, we prove a property implied by first order optimality condition, which is similar to Lemma 4.9. ‣ 4.2 Extension to general 𝑥 ‣ 4 Warm-up: Rank-1 Case ‣ Matrix Completion has No Spurious Local Minimum").

### Lemma 5.5

In the setting of Theorem 5.3, with high probability over the choice of $\Omega$, for any $X$ that satisfies 1st order optimality condition (5.2), we have

where $\delta = {O{({\mu^{3}\kappa^{3}r^{2}{\log^{0.75}{(d)}}\sigma_{\max}{(Z)}^{- 3}{({dp})}^{- {1/2}}})}}$ and $\gamma = {\lambda/{({2p})}} \geqslant 0$.

### Proof

If ${\| X\|}_{F} \leqslant \sqrt{r\sigma_{\max}{(Z)}^{2}}$ we are done. When ${\| X\|}_{F} \geqslant \sqrt{r\sigma_{\max}{(Z)}^{2}}$, by Lemma 5.4, we have that ${\max{\| X_{i}\|}} \leqslant {4\alpha} = {O{({{\mu\kappar}/\sqrt{d}})}}$, and therefore ${\max{\| X_{i}\|}} \leqslant {\nu{\| X\|}_{F}}$ with $\nu = {O{({{{\mu\kappa\sqrt{r}}/\sigma_{\max}}{(Z)}})}}$. Then by Theorem D.2, we have that

where $\delta = {O{({\mu^{3}\kappa^{3}r^{2}{\log^{0.75}{(d)}}\sigma_{\max}{(Z)}^{- 3}{({dp})}^{- {1/2}}})}}$. These two imply equation (5.11). Moreover, we have

Suppose $X$ has singular value $\sigma_{1} \geqslant \cdots \geqslant \sigma_{r}$. Then we have $\left. \parallel{ZZ^{\top}X}\parallel \right._{F}^{2} \leqslant {{\|{ZZ^{\top}}\|}^{2}{\| X\|}_{F}^{2}} \leqslant {\sigma_{\max}{(Z)}^{4}{\| X\|}_{F}^{2}} = {\sigma_{\max}{(Z)}^{4}{({\sigma_{1}^{2} + \cdots + \sigma_{r}^{2}})}}$. On the other hand, $\left. \parallel{XX^{\top}X}\parallel \right._{F}^{2} = {\sigma_{1}^{6} + \cdots + \sigma_{r}^{6}}$. Therefore, equation (5.12) implies that

Then we have (by Proposition E.2) we complete the proof.

Now we look at the second order optimality condition, this condition implies the smallest singular value of $X$ is large (similar to Lemma 4.8. ‣ 4.2 Extension to general 𝑥 ‣ 4 Warm-up: Rank-1 Case ‣ Matrix Completion has No Spurious Local Minimum")). Note that this lemma is also true even if $x$ only satisfies relaxed second order optimality condition with $\tau = {0.01p\sigma_{\min}{(Z)}}$.

### Lemma 5.6

In the setting of Theorem 5.3. With high probability over the choice of $\Omega$, suppose $X$ satisfies equation (5.9), (5.4) the 2nd order optimality condition (5.3). Then,

### Proof

Let $J = {\{ i:{{\| X_{i}\|} \leqslant \alpha}\}}$. Let $v \in {\mathbb{R}}^{r}$ such that ${\|{Xv}\|} = {\sigma_{\min}{(X)}}$.. Let $Z_{J}$ be the matrix that has the same $i$-th row as $Z$ for every $i \in J$ and 0 elsewhere.

We claim that ${\sigma_{\min}{(Z_{J})}} \geqslant {\frac{1}{2}\sigma_{\min}{(Z)}}$. Let $L = {{\lbrack d\rbrack} - J}$. Since for any $i \in L$ it holds that ${\| X_{i}\|} \geqslant \alpha$, we have ${{|L|}\alpha^{2}} \leqslant {\| X\|}_{F}^{2} \leqslant {2r\sigma_{\max}{(Z)}^{2}}$ (by equation (5.9)), and it follows that ${|L|} \leqslant {{2r\sigma_{\max}{(Z)}^{2}}/\alpha^{2}}$. Therefore,

Therefore, $Z_{J}$ has column rank exactly $r$. By variational characterization of singular values, we have that for there exists unit vector $z_{J} \in {\text{col-span}{(Z_{J})}}$ such that ${\|{X^{\top}z_{J}}\|} \leqslant {\sigma_{\min}{(X)}}$. Since $z_{J} \in {\text{col-span}{(Z_{J})}}$ is a unit vector, we have that $z_{J}$ can be written as $z_{J} = {Z_{J}\beta}$ where ${{\|\beta\|} \leqslant \frac{1}{\sigma_{\min}{(Z_{J})}} \leqslant {O{({{1/\sigma_{\min}}{(Z)}})}}}.$ Therefore this in turn implies that ${\| z_{J}\|}_{\infty} \leqslant {{\| Z_{J}\|}_{2\rightarrow\infty}{\|\beta\|}} \leqslant {O{({{{\mu\sqrt{r/d}}/\sigma_{\min}}{(Z)}})}} \leqslant {O{({\mu\kappa\sqrt{r/d}})}}$.

We will plug in $V = {z_{J}v^{T}}$ in the 2nd order optimality condition (5.3). Note that since $z_{J} \in {\text{col-span}{(Z_{J})}}$, it is supported on subset $J$, and therefore ${{\nabla^{2}R}{(X)}V} = 0$. Therefore the term about regularization in (5.3) will vanish. For simplicity, let $y = {X^{\top}z_{J}}$, $w = {Xv}$ We obtain that taking $V = {z_{J}v^{\top}}$ in equation (5.3) will result in

Note that we have that ${\| w\|}_{\infty} \leqslant {{\| X\|}_{2\rightarrow\infty}{\| v\|}} \leqslant {\mu\sqrt{r/d}}$. Recalling that ${\| z_{J}\|}_{\infty} \leqslant {O{({\mu\kappa\sqrt{r/d}})}}$, by Theorem D.1, we have that

where $\delta = {O{({\mu^{2}\kappar^{2}{({pd})}^{- {1/2}}})}}$. Then simple algebraic manipulation gives that

Note that ${\langle w,z_{J}\rangle} = {\langle v,{X^{\top}z_{J}}\rangle} = {\langle y,v\rangle}$. Recall that ${\| z_{J}\|} = 1$ and $z \in {\text{col-span}{(Z_{J})}}$, and therefore ${\|{Z^{\top}z_{J}}\|} = {\|{Z_{J}^{\top}z_{J}}\|} \geqslant {\sigma_{\min}^{2}{(Z_{J})}}$. Moreover, recall that ${\| y\|} = {\|{X^{\top}z_{J}}\|} \leqslant {\sigma_{\min}{(X)}}$. Using these with equation (5.14) we obtain that

Therefore together with equation (5.14) and ${\|{Z^{\top}z_{J}}\|} \geqslant {\sigma_{\min}^{2}{(Z_{J})}}$ we obtain that

Therefore combining equation (5.15) and the lower bound on $\sigma_{\min}{(Z_{J})}$ we complete the proof. ∎

Similar as before, we show it is possible to remove the regularizer term here, again the intuition is that the regularizer is always in the same direction as $X$.

### Lemma 5.7

Suppose $X$ satisfies equation (5.4) and (5.13) and (5.10), then for any $\gamma \geqslant 0$,

### Proof

Let $L = {\{ i:{{\| X_{i}\|} \geqslant \alpha}\}}$. For $i \notin L$, we have that ${({{\nabla R}{(X)}})}_{i} = 0$. Therefore it suffices to prove that for every $i \in L$,

It suffices to prove that

By proposition 5.2, we have $\nabla R{(X)})_{i} = \Gamma_{ii}X_{i}$ for $\Gamma_{ii} \geqslant 0$. Then

On the other hand, we have

Therefore combining two equations above we obtain equation (5.17) which completes the proof. ∎

Finally we show the form in Equation (5.16) implies $ZZ^{T}$ is close to $XX^{T}$ (this is similar to Lemma 4.6).

### Lemma 5.8

Suppose $X$ and $Z$ satisfies that ${\sigma_{\min}{(X)}} \geqslant {{{1/4} \cdot \sigma_{\min}}{(Z)}}$ and that

where $\delta \leqslant {{\sigma_{min}^{3}{(Z)}}/C}$ for a large enough constant $C$, then

### Proof

The proof is similar to the one-dimensional case, we will separate $Z$ into the directions that are in column span of $X$ and its orthogonal subspace. We will then show the projection of $Z$ in the column span is close to $X$, and the projection on the orthogonal subspace must be small.

Let $Z = {U + V}$ where $U = {\text{Proj}_{span{(X)}}Z}$ is the projection of $Z$ to the column span of $X$, and $V$ is the projection to the orthogonal subspace. Then since ${V^{T}X} = 0$ we know

Here columns of the first term $UU^{T}X$ are in the column span of $X$, and the columns second term $VU^{T}X$ are in the orthogonal subspace. Therefore,

In particular, both terms should be bounded by $\delta^{2}$. Therefore ${\|{{UU^{T}} - {XX^{T}}}\|}_{F}^{2} \leqslant {{\delta^{2}/\sigma_{min}^{2}}{(X)}} \leqslant {{{16\delta^{2}}/\sigma_{min}^{2}}{(Z)}}$.

Also, we know ${\sigma_{min}{({UU^{T}X})}} \geqslant {{\sigma_{min}{({XX^{T}X})}} - \delta} \geqslant {{\sigma_{min}{(Z)}^{3}}/128}$ if $\delta \leqslant {{\sigma_{min}{(Z)}^{3}}/128}$. Therefore $\sigma_{min}{({U^{T}X})}$ is at least ${{\sigma_{min}{(Z)}^{3}}/{\| Z\|}}128$. Now ${\| V\|}_{F}^{2} \leqslant {{\delta^{2}/\sigma_{min}}{({U^{T}X})}^{2}} \leqslant {O{({{{\delta^{2}{\| Z\|}^{2}}/\sigma_{min}}{(Z)}^{6}})}}$.

Finally, we can bound ${\|{UV^{T}}\|}_{F}$ by ${{\| U\|}{\| V\|}_{F}} \leqslant {{\| Z\|}{\| V\|}_{F}}$ (last inequality is because $U$ is a projection of $Z$), which at least $\Omega{({\| V\|}_{F}^{2})}$ when $\delta \leqslant {{\sigma_{min}{(Z)}^{3}}/128}$, therefore

Last thing we need to prove the main theorem is a result from Sun and Luo, which shows whenever $XX^{T}$ is close to $ZZ^{T}$, the function is essentially strongly convex, and the only points that have $0$ gradient are points where ${XX^{T}} = {ZZ^{T}}$, this is explained in Lemma C.1. ‣ Appendix C Finding the Exact Factorization ‣ Matrix Completion has No Spurious Local Minimum"). Now we are ready to prove Theorem 5.3:

### Proof of Theorem 5.3

Suppose $X$ satisfies 1st and 2nd order optimality condition. Then by Lemma 5.5 and Lemma 5.4, we have that $X$ satisfies equation (5.4), (5.9), (5.10) and (5.11). Then by Lemma 5.6, we obtain that ${\sigma_{\min}{(X)}} \geqslant {{{1/6} \cdot \sigma_{\min}}{(Z)}}$. Now by Lemma 5.7 and equation (5.11), we have that $\left. \parallel{{ZZ^{T}X} - {XX^{T}X}}\parallel \right._{F} \leqslant \delta$ for $\delta \leqslant {{c\sigma_{\min}{(Z)}^{3}}/\kappa^{2}}$ for sufficiently small constant $c$. Then by Lemma 5.8 we obtain that ${\|{{ZZ^{\top}} - {XX^{\top}}}\|}_{F} \leqslant {c\sigma_{\min}{(Z)}^{2}}$ for sufficiently small constant $c$. By Lemma C.1. ‣ Appendix C Finding the Exact Factorization ‣ Matrix Completion has No Spurious Local Minimum"), in this region the only points that satisfy the first order optimality condition must satisfy ${XX^{T}} = {ZZ^{T}}$. ∎

### Handling Noise

To handle noise, notice that we can only hope to get an approximate solution in presence of noise, and to get that our Lemmas only depend on concentration bounds which still apply in the noisy setting. See Section B for details.

## Conclusions

Although the matrix completion objective is non-convex, we showed the objective function has very nice properties that ensures the local minima are also global. This property gives guarantees for many basic optimization algorithms. An important open problem is the robustness of this property under different model assumptions: Can we extend the result to handle asymmetric matrix completion? Is it possible to add weights to different entries (similar to the settings studied in )? Can we replace the objective function with a different distance measure rather than Frobenius norm (which is related to works on 1-bit matrix sensing )? We hope this framework of analyzing the geometry of objective function can be applied to other problems.
