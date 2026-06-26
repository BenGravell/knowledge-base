<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Matrix Completion Has No Spurious Local Minimum

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Matrix completion is a basic machine learning problem that has wide applications, especially in collaborative filtering and recommender systems. Simple non-convex optimization algorithms are popular and effective in practice. Despite recent progress in proving various non-convex algorithms converge from a good initial point, it remains unclear why random or arbitrary initialization suffices in practice. We prove that the commonly used non-convex objective function for \textit{positive semidefinite} matrix completion has no spurious local minima - all local minima must also be global. Therefore, many popular optimization algorithms such as (stochastic) gradient descent can provably solve positive semidefinite matrix completion with \textit{arbitrary} initialization in polynomial time. The result can be generalized to the setting when the observed entries contain noise. We believe that our main proof strategy can be useful for understanding geometric properties of other statistical problems involving partial or noisy observations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Matrix completion is the problem of recovering a low rank matrix from partially observed entries. It has been widely used in collaborative filtering and recommender systems, dimension reduction and multi-class learning. There has been extensive work on designing efficient algorithms for matrix completion with guarantees. One earlier line of results (see and the references therein) rely on convex relaxations. These algorithms achieve strong statistical guarantees, but are quite computationally expensive in practice.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, there has been growing interest in analyzing non-convex algorithms for matrix completion. Let $M \in {\mathbb{R}}^{d \times d}$ be the target matrix with rank $r \ll d$ that we aim to recover, and let $\Omega = {\{{(i,j)}:{M_{i,j}\text{~is observed}}\}}$ be the set of observed entries. These methods are instantiations of optimization algorithms applied to the objective^11^1In this paper, we focus on the symmetric case when the true $M$ has a symmetric decomposition $M = {ZZ^{T}}$. Some of previous papers work on the asymmetric case when $M = {ZW^{T}}$, which is harder than the symmetric case., These algorithms are much faster than the convex relaxation algorithms, which is crucial for their empirical success in large-scale collaborative filtering applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most of the theoretical analysis of the nonconvex procedures require careful initialization schemes: the initial point should already be close to optimum^22^2The work of De Sa et al. is an exception, which gives an algorithm that uses fresh samples at every iteration to solve matrix completion (and other matrix problems) approximately.. In fact, Sun and Luo showed that after this initialization the problem is effectively strongly-convex, hence many different optimization procedures can be analyzed by standard techniques from convex optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, in practice people typically use a random initialization, which still leads to robust and fast convergence. Why can these practical algorithms find the optimal solution in spite of the non-convexity? In this work we investigate this question and show that the matrix completion objective has no spurious local minima. More precisely, we show that any local minimum $X$ of objective function $f{( \cdot )}$ is also a global minimum with ${f{(X)}} = 0$, and recovers the correct low rank matrix $M$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our characterization of the structure in the objective function implies that (stochastic) gradient descent from arbitrary starting point converge to a global minimum. This is because gradient descent converges to a local minimum, and every local minimum is also a global minimum.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Main results", "weight": 1.0} -->

Assume the target matrix $M$ is symmetric and each entry of $M$ is observed with probability $p$ independently ^33^3The entries $(i,j)$ and $(j,i)$ are the same. With probability $p$ we observe both entries and otherwise we observe neither.. We assume $M = {ZZ^{\top}}$ for some matrix $Z \in {\mathbb{R}}^{d \times r}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Main results", "weight": 1.0} -->

There are two known issues with matrix completion. First, the choice of $Z$ is not unique since $M = {{({ZR})}{({ZR})}^{\top}}$ for any orthonormal matrix $Z$. Our goal is to find one of these equivalent solutions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Main results", "weight": 1.0} -->

Another issue is that matrix completion is impossible when $M$ is "aligned" with standard basis. For example, when $M$ is the identity matrix in its first $r \times r$ block, we will very likely be observing only 0 entries.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Throughout this paper we think of $\mu$ and $\kappa$ as small constants, and the sample complexity depends polynomially on these two parameters. Also note that this assumption is independent of the choice of $Z$: all $Z$ such that ${ZZ^{T}} = M$ have the same row norms and Frobenius norm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

This assumption is similar to the "incoherence" assumption. Our assumption is the same as the one used in analyzing non-convex algorithms.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We enforce $X$ to also satisfy this assumption by a regularizer where $R{(X)}$ is a function that penalizes $X$ when one of its rows is too large. See Section 4 and Section 5 for the precise definition.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Matrix Completion", "weight": 1.0} -->

The earlier theoretical works on matrix completion analyzed the nuclear norm minimization. This line of work has the cleanest and strongest theoretical guarantees; showed that if ${|\Omega|} \gtrsim {dr\mu^{2}{\log^{2}d}}$ the nuclear norm convex relaxation recovers the exact underlying low rank matrix. The solution can be computed via the solving a convex program in polynomial time. However the primary disadvantage of nuclear norm methods is their computational and memory requirements --- the fastest known provable algorithms require $O{(d^{2})}$ memory and thus at least $O{(d^{2})}$ running time, which could be both prohibitive for moderate to large values of $d$. Many algorithms have been proposed to improve the runtime (either theoretically or empirically) (see, for examples and the reference therein).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Matrix Completion", "weight": 1.0} -->

Burer and Monteiro proposed factorizing the optimization variable $\hat{M} = {XX^{T}}$, and optimizing over $X \in {\mathbb{R}}^{d \times r}$ instead of $\hat{M} \in {\mathbb{R}}^{d \times d}$. This approach only requires $O{({dr})}$ memory, and a single gradient iteration takes time $O{({|\Omega|})}$, so has much lower memory requirement and computational complexity than the nuclear norm relaxation. On the other hand, the factorization causes the optimization problem to be non-convex in $X$, which leads to theoretical difficulties in analyzing algorithms. Keshavan et al. showed that well-initialized gradient descent recovers $M$. The works showed that well-initialized alternating least squares, block coordinate descent, and gradient descent converges $M$. Jain and Netrapalli showed a fast algorithm by iteratively doing gradient descent in the relaxed space and projecting to the set of low-rank matrices.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Matrix Completion", "weight": 1.0} -->

The work analyzes stochastic gradient descent with fresh samples at each iteration from random initialization and shows that it approximately converge to the optimal solution. provided a more unified analysis by showing that with careful initialization many algorithms, including gradient descent and alternating least squares, succeed. accomplished this by showing an analog of strong convexity in the neighborhood of the solution $M$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Non-convex Optimization", "weight": 1.0} -->

Recently, a line of work analyzes non-convex optimization by separating the problem into two aspects: the geometric aspect which shows the function has no spurious local minimum and the algorithmic aspect which designs efficient algorithms can converge to local minimum that satisfy first and (relaxed versions) of second order necessary conditions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Non-convex Optimization", "weight": 1.0} -->

Our result is the first that explains the geometry of the matrix completion objective. Similar geometric results are only known for a few problems: SVD/PCA phase retrieval/synchronization, orthogonal tensor decomposition, dictionary learning. The matrix completion objective requires different tools due to the sampling of the observed entries, as well as carefully managing the regularizer to restrict the geometry. Parallel to our work Bhojanapalli et al. showed similar results for matrix sensing, which is closely related to matrix completion. Loh and Wainwright showed that for many statistical settings that involve missing/noisy data and non-convex regularizers, any stationary point of the non-convex objective is close to global optima; furthermore, there is a unique stationary point that is the global minimum under stronger assumptions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Non-convex Optimization", "weight": 1.0} -->

On the algorithmic side, it is known that second order algorithms like cubic regularization and trust-region algorithms converge to local minima that approximately satisfy first and second order conditions. Gradient descent is also known to converge to local minima from a random starting point. Stochastic gradient descent can converge to a local minimum in polynomial time from any starting point. All of these results can be applied to our setting, implying various heuristics used in practice are guaranteed to solve matrix completion.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Notations", "weight": 1.0} -->

For $\Omega \subset {{\lbrack d\rbrack} \times {\lbrack d\rbrack}}$, let $P_{\Omega}$ be the linear operator that maps a matrix $A$ to $P_{\Omega}{(A)}$, where $P_{\Omega}{(A)}$ has the same values as $A$ on $\Omega$, and $0$ outside of $\Omega$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Difficult to Generalize Proof of Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum\")", "weight": 1.0} -->

We compute the gradient and Hessian of $g{(x)}$, Therefore, a critical point $x$ satisfies ${{\nabla g}{(x)}} = {{Mx} - {{\| x\|}^{2}x}} = 0$, and thus it must be an eigenvector of $M$ and ${\| x\|}^{2}$ is the corresponding eigenvalue. Next, we prove that the hessian is only positive definite at the top eigenvector. Let $x$ be an eigenvector with eigenvalue $\lambda = {\| x\|}^{2}$, and $\lambda$ is strictly less than the top eigenvalue $\lambda^{\ast}$. Let $z$ be the top eigenvector.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Difficult to Generalize Proof of Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum\")", "weight": 1.0} -->

The difficulty of generalizing the proof above to the partial observation case is that it uses the properties of eigenvectors heavily. Suppose we want to imitate the proof above for the partial observation case, the first difficulty is how to solve the equation ${\overset{\sim}{g}{(x)}} = {P_{\Omega}{({M - {xx^{\top}}})}x} = 0$. Moreover, even if we could have a reasonable approximation for the critical points (the solution of ${{\nabla\overset{\sim}{g}}{(x)}} = 0$), it would be difficult to examine the Hessian of these critical points without having the orthogonality of the eigenvectors.

<!-- chunk {"id": "body-0023", "role": "body", "section": "\"Simple\" and Generalizable proof", "weight": 1.0} -->

The lessons from the subsection above suggest us find an alternative proof for the full observation case which is generalizable. The alternative proof will be simple in the sense that it doesn't use the notion of eigenvectors and eigenvalues. Concretely, the key observation behind most of the analysis in this paper is the following, Proofs that consist of inequalities that are linear in $\mathbf{1}_{\Omega}$ are often easily generalizable to partial observation case.

<!-- chunk {"id": "body-0024", "role": "body", "section": "\"Simple\" and Generalizable proof", "weight": 1.0} -->

Here statements that are linear in $\mathbf{1}_{\Omega}$ mean the statements of the form ${\sum_{ij}{1_{{(i,j)} \in \Omega}T_{ij}}} \leqslant a$. We will call these kinds of proofs "simple" proofs in this section.

<!-- chunk {"id": "body-0025", "role": "body", "section": "\"Simple\" and Generalizable proof", "weight": 1.0} -->

Roughly speaking, the observation follows from the law of large numbers --- Suppose ${T_{ij},{(i,j)}} \in {{\lbrack d\rbrack} \times {\lbrack d\rbrack}}$ is a sequence of bounded real numbers, then the sampled sum ${\sum_{{(i,j)} \in \Omega}T_{ij}} = {\sum_{i,j}{\mathbf{1}_{{(i,j)} \in \Omega}T_{ij}}}$ is an accurate estimate of the sum $p{\sum_{i,j}T_{ij}}$, when the sampling probability $p$ is relatively large.

<!-- chunk {"id": "body-0026", "role": "body", "section": "\"Simple\" and Generalizable proof", "weight": 1.0} -->

Then, the mathematical implications of ${p{\sum T_{ij}}} \leqslant a$ are expected to be similar to the implications of ${\sum_{{(i,j)} \in \Omega}T_{ij}} \leqslant a$, up to some small error introduced by the approximation. To make this concrete, we give below informal proofs for Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum") and Lemma 3.1. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum") that only consists of statements that are linear in $\mathbf{1}_{\Omega}$. Readers will see that due to the linearity, the proof for the partial observation case (shown on the right column) is a direct generalization of the proof for the full observation case (shown on the left column) via concentration inequalities (which will be discussed more at the end of the section).

<!-- chunk {"id": "body-0027", "role": "body", "section": "\"Simple\" and Generalizable proof", "weight": 1.0} -->

A "simple" proof for Lemma 3.2. ‣ 3 Proof Strategy: “simple” proofs are more generalizable ‣ Matrix Completion has No Spurious Local Minimum").

<!-- chunk {"id": "body-0028", "role": "body", "section": "Subtleties regarding uniform convergence", "weight": 1.0} -->

In the proof sketches above, our key idea is to use concentration inequalities to link the full observation objective $g{(x)}$ with the partial observation counterpart. However, we require a uniform convergence result. For example, we need a statement like "w.h.p over the choice of $\Omega$, equation (3.5) and (3.6) are similar to each other up to scaling". This type of statement is often only true for $x$ inside the incoherent ball $\mathcal{B}$. The fix to this is the regularizer. For non-incoherent $x$, we will use a different argument that uses the property of the regularizer. This is besides the main proof strategy of this section and will be discussed in subsequent sections.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Warm-up: Rank-1 Case", "weight": 1.0} -->

In this section, using the general proof strategy described in previous section, we provide a formal proof for the rank-1 case. In subsection 4.1, we formally work out the proof sketches of Section 3. In subsection 4.2, we prove that due to the effect of the regularizer, outside incoherent ball $\mathcal{B}$, the objective function doesn't have any local minimum.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Warm-up: Rank-1 Case", "weight": 1.0} -->

In the rank-1 case, the objective function simplifies to, Here we use the the regularization $R{(x)}$ The parameters $\lambda$ and $\alpha$ will be chosen later as in Theorem 4.2. We will choose $\alpha > {{10\mu}/\sqrt{d}}$ so that ${R{(x)}} = 0$ for incoherent $x$, and thus it only penalizes coherent $x$. Moreover, we note $R{(x)}$ has Lipschitz second order derivative. ^55^5This is the main reason for us to choose $4$-th power instead of $2$-nd power.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Warm-up: Rank-1 Case", "weight": 1.0} -->

We first state the optimality conditions, whose proof is deferred to Appendix A.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Handling incoherent $x$", "weight": 1.0} -->

To demonstrate the key idea, in this section we restrict our attention to the subset of ${\mathbb{R}}^{d}$ which contains incoherent $x$ with $\ell_{2}$ norm bounded by 1, that is, we consider, Note that the desired solution $z$ is in $\mathcal{B}$, and the regularization $R{(x)}$ vanishes inside $\mathcal{B}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Handling incoherent $x$", "weight": 1.0} -->

The following lemmas assume $x$ satisfies the first and second order optimality conditions, and deduce a sequence of properties that $x$ must satisfy.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Extension to general $x$", "weight": 1.0} -->

We have shown when $x$ is incoherent and satisfies first and second order optimality conditions, then it must be close to $z$ or $- z$. Now we need to consider more general cases when $x$ may have some very large coordinates. Here the main intuition is that the first order optimality condition with a proper regularizer is enough to guarantee that $x$ cannot have a entry that is too much bigger than $\mu/\sqrt{d}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Rank-r case", "weight": 1.0} -->

In this section we show how to extend the results in Section 4 to recover matrices of rank $r$. Here we still use the same proof strategy of Section 3. Though for simplicity we only write down the proof for the partial observation case, while the analysis for the full observation case (which was our starting point) can be obtained by substituting ${\lbrack d\rbrack} \times {\lbrack d\rbrack}$ for $\Omega$ everywhere.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Handling Noise", "weight": 1.0} -->

To handle noise, notice that we can only hope to get an approximate solution in presence of noise, and to get that our Lemmas only depend on concentration bounds which still apply in the noisy setting. See Section B for details.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Although the matrix completion objective is non-convex, we showed the objective function has very nice properties that ensures the local minima are also global. This property gives guarantees for many basic optimization algorithms. An important open problem is the robustness of this property under different model assumptions: Can we extend the result to handle asymmetric matrix completion? Is it possible to add weights to different entries (similar to the settings studied in )? Can we replace the objective function with a different distance measure rather than Frobenius norm (which is related to works on 1-bit matrix sensing )? We hope this framework of analyzing the geometry of objective function can be applied to other problems.
