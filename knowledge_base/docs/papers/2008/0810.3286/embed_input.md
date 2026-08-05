<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Singular Value Thresholding Algorithm for Matrix Completion

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces a novel algorithm to approximate the matrix with minimum nuclear norm among all matrices obeying a set of convex constraints. This problem may be understood as the convex relaxation of a rank minimization problem, and arises in many important applications as in the task of recovering a large matrix from a small subset of its entries (the famous Netflix problem). Off-the-shelf algorithms such as interior point methods are not directly amenable to large problems of this kind with over a million unknown entries. This paper develops a simple first-order and easy-to-implement algorithm that is extremely efficient at addressing problems in which the optimal solution has low rank. The algorithm is iterative and produces a sequence of matrices (X^k, Y^k) and at each step, mainly performs a soft-thresholding operation on the singular values of the matrix Y^k. There are two remarkable features making this attractive for low-rank matrix completion problems. The first is that the soft-thresholding operation is applied to a sparse matrix; the second is that the rank of the iterates X^k is empirically nondecreasing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Both these facts allow the algorithm to make use of very minimal storage space and keep the computational cost of each iteration low. We provide numerical examples in which 1,000 by 1,000 matrices are recovered in less than a minute on a modest desktop computer. We also demonstrate that our approach is amenable to very large scale problems by recovering matrices of rank about 10 with nearly a billion unknowns from just about 0.4% of their sampled entries. Our methods are connected with linearized Bregman iterations for l1 minimization, and we develop a framework in which one can understand these algorithms in terms of well-known Lagrange multiplier algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Motivation", "weight": 1.0} -->

There is a rapidly growing interest in the recovery of an unknown low-rank or approximately low-rank matrix from very limited information. This problem occurs in many areas of engineering and applied science such as machine learning, control and computer vision, see. As a motivating example, consider the problem of recovering a data matrix from a sampling of its entries. This routinely comes up whenever one collects partially filled out surveys, and one would like to infer the many missing entries. In the area of recommender systems, users submit ratings on a subset of entries in a database, and the vendor provides recommendations based on the user's preferences. Because users only rate a few items, one would like to infer their preference for unrated items; this is the famous Netflix problem. Recovering a rectangular matrix from a sampling of its entries is known as the matrix completion problem. The issue is of course that this problem is extraordinarily ill posed since with fewer samples than entries, we have infinitely many completions. Therefore, it is apparently impossible to identify which of these candidate solutions is indeed the "correct" one without some additional information.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

In many instances, however, the matrix we wish to recover has low rank or approximately low rank. For instance, the Netflix data matrix of all user-ratings may be approximately low-rank because it is commonly believed that only a few factors contribute to anyone's taste or preference. In computer vision, inferring scene geometry and camera motion from a sequence of images is a well-studied problem known as the structure-from-motion problem. This is an ill-conditioned problem for objects may be distant with respect to their size, or especially for "missing data" which occur because of occlusion or tracking failures. However, when properly stacked and indexed, these images form a matrix which has very low rank (e.g. rank 3 under orthography). Other examples of low-rank matrix fitting abound; e.g. in control (system identification), machine learning (multi-class learning) and so. Having said this, the premise that the unknown has (approximately) low rank radically changes the problem, making the search for solutions feasible since the lowest-rank solution now tends to be the right one.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

In a recent paper, Candès and Recht showed that matrix completion is not as ill-posed as people thought. Indeed, they proved that most low-rank matrices can be recovered exactly from most sets of sampled entries even though these sets have surprisingly small cardinality, and more importantly, they proved that this can be done by solving a simple convex optimization problem. To state their results, suppose to simplify that the unknown matrix ${\mathbf{M}} \in {\mathbb{R}}^{n \times n}$ is square, and that one has available $m$ sampled entries $\{{\mathbf{M}}_{ij}:{{(i,j)} \in \Omega}\}$ where $\Omega$ is a random subset of cardinality $m$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

Then proves that most matrices $\mathbf{M}$ of rank $r$ can be perfectly recovered by solving the optimization problem provided that the number of samples obeys for some positive numerical constant $C$.^11^1Note that an $n \times n$ matrix of rank $r$ depends upon $r{({{2n} - r})}$ degrees of freedom. In (1.1), the functional ${\|{\mathbf{X}}\|}_{\ast}$ is the nuclear norm of the matrix $\mathbf{M}$, which is the sum of its singular values. The optimization problem (1.1) is convex and can be recast as a semidefinite program. In some sense, this is the tightest convex relaxation of the NP-hard rank minimization problem since the nuclear ball $\{{\mathbf{X}}:{{\|{\mathbf{X}}\|}_{\ast} \leq 1}\}$ is the convex hull of the set of rank-one matrices with spectral norm bounded by one.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

Another interpretation of Candès and Recht's result is that under suitable conditions, the rank minimization program (1.3) and the convex program (1.1) are formally equivalent in the sense that they have exactly the same unique solution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

Because minimizing the nuclear norm both provably recovers the lowest-rank matrix subject to constraints (see for related results) and gives generally good empirical results in a variety of situations, it is understandably of great interest to develop numerical methods for solving (1.1). In, this optimization problem was solved using one of the most advanced semidefinite programming solvers, namely, SDPT3. This solver and others like SeDuMi are based on interior-point methods, and are problematic when the size of the matrix is large because they need to solve huge systems of linear equations to compute the Newton direction. In fact, SDPT3 can only handle $n \times n$ matrices with $n \leq 100$. Presumably, one could resort to iterative solvers such as the method of conjugate gradients to solve for the Newton step but this is problematic as well since it is well known that the condition number of the Newton system increases rapidly as one gets closer to the solution. In addition, none of these general purpose solvers use the fact that the solution may have low rank.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

We refer the reader to for some recent progress on interior-point methods concerning some special nuclear norm-minimization problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

This paper develops the singular value thresholding algorithm for approximately solving the nuclear norm minimization problem (1.1) and by extension, problems of the form where $\mathcal{A}$ is a linear operator acting on the space of $n_{1} \times n_{2}$ matrices and ${\mathbf{b}} \in {\mathbb{R}}^{m}$. This algorithm is a simple first-order method, and is especially well suited for problems of very large sizes in which the solution has low rank. We sketch this algorithm in the special matrix completion setting and let $\mathcal{P}_{\Omega}$ be the orthogonal projector onto the span of matrices vanishing outside of $\Omega$ so that the $(i,j)$th component of $\mathcal{P}_{\Omega}{({\mathbf{X}})}$ is equal to $X_{ij}$ if ${(i,j)} \in \Omega$ and zero otherwise.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

Our problem may be expressed as with optimization variable ${\mathbf{X}} \in {\mathbb{R}}^{n_{1} \times n_{2}}$. Fix $\tau > 0$ and a sequence ${\{\delta_{k}\}}_{k \geq 1}$ of scalar step sizes. Then starting with ${\mathbf{Y}}^{0} = 0 \in {\mathbb{R}}^{n_{1} \times n_{2}}$, the algorithm inductively defines until a stopping criterion is reached. In (1.6), $\text{shrink}{({\mathbf{Y}},\tau)}$ is a nonlinear function which applies a soft-thresholding rule at level $\tau$ to the singular values of the input matrix, see Section 2 for details. The key property here is that for large values of $\tau$, the sequence $\{{\mathbf{X}}^{k}\}$ converges to a solution which very nearly minimizes (1.5).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

Hence, at each step, one only needs to compute at most one singular value decomposition and perform a few elementary matrix additions. Two important remarks are in order: Sparsity. For each $k \geq 0$, ${\mathbf{Y}}^{k}$ vanishes outside of $\Omega$ and is, therefore, sparse, a fact which can be used to evaluate the shrink function rapidly.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

Low-rank property. The matrices ${\mathbf{X}}^{k}$ turn out to have low rank, and hence the algorithm has minimum storage requirement since we only need to keep principal factors in memory.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Algorithm outline", "weight": 1.0} -->

Our numerical experiments demonstrate that the proposed algorithm can solve problems, in Matlab, involving matrices of size $30,{000 \times 30},000$ having close to a billion unknowns in 17 minutes on a standard desktop computer with a 1.86 GHz CPU (dual core with Matlab's multithreading option enabled) and 3 GB of memory. As a consequence, the singular value thresholding algorithm may become a rather powerful computational tool for large scale matrix completion.

<!-- chunk {"id": "body-0016", "role": "body", "section": "General formulation", "weight": 1.0} -->

The singular value thresholding algorithm can be adapted to deal with other types of convex constraints. For instance, it may address problems of the form where each $f_{i}$ is a Lipschitz convex function (note that one can handle linear equality constraints by considering pairs of affine functionals). In the simpler case where the $f_{i}$'s are affine functionals, the general algorithm goes through a sequence of iterations which greatly resemble (1.6). This is useful because this enables the development of numerical algorithms which are effective for recovering matrices from a small subset of sampled entries possibly contaminated with noise.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contents and notations", "weight": 1.0} -->

The rest of the paper is organized as follows. In Section 2, we derive the singular value thresholding (SVT) algorithm for the matrix completion problem, and recasts it in terms of a well-known Lagrange multiplier algorithm. In Section 3, we extend the SVT algorithm and formulate a general iteration which is applicable to general convex constraints. In Section 4, we establish the convergence results for the iterations given in Sections 2 and 3. We demonstrate the performance and effectiveness of the algorithm through numerical examples in Section 5, and review additional implementation details. Finally, we conclude the paper with a short discussion in Section 6.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The Singular Value Thresholding Algorithm", "weight": 1.0} -->

This section introduces the singular value thresholding algorithm and discusses some of its basic properties. We begin with the definition of a key building block, namely, the singular value thresholding operator.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The singular value shrinkage operator", "weight": 1.0} -->

Consider the singular value decomposition (SVD) of a matrix ${\mathbf{X}} \in {\mathbb{R}}^{n_{1} \times n_{2}}$ of rank $r$ where $\mathbf{U}$ and $\mathbf{V}$ are respectively $n_{1} \times r$ and $n_{2} \times r$ matrices with orthonormal columns, and the singular values $\sigma_{i}$ are positive (unless specified otherwise, we will always assume that the SVD of a matrix is given in the reduced form above). For each $\tau \geq 0$, we introduce the soft-thresholding operator $\mathcal{D}_{\tau}$ defined as follows: where $t_{+}$ is the positive part of $t$, namely, $t_{+} = {\max{(0,t)}}$. In words, this operator simply applies a soft-thresholding rule to the singular values of $\mathbf{X}$, effectively shrinking these towards zero.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The singular value shrinkage operator", "weight": 1.0} -->

This is the reason why we will also refer to this transformation as the singular value shrinkage operator. Even though the SVD may not be unique, it is easy to see that the singular value shrinkage operator is well defined and we do not elaborate further on this issue. In some sense, this shrinkage operator is a straightforward extension of the soft-thresholding rule for scalars and vectors. In particular, note that if many of the singular values of $\mathbf{X}$ are below the threshold $\tau$, the rank of $\mathcal{D}_{\tau}{({\mathbf{X}})}$ may be considerably lower than that of $\mathbf{X}$, just like the soft-thresholding rule applied to vectors leads to sparser outputs whenever some entries of the input are below threshold.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The singular value shrinkage operator", "weight": 1.0} -->

The singular value thresholding operator is the proximity operator associated with the nuclear norm. Details about the proximity operator can be found in e.g..

<!-- chunk {"id": "body-0022", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

We are now in the position to introduce the singular value thresholding algorithm. Fix $\tau > 0$ and a sequence $\{\delta_{k}\}$ of positive step sizes. Starting with ${\mathbf{Y}}_{0}$, inductively define for $k = {1,2,\ldots}$, until a stopping criterion is reached (we postpone the discussion this stopping criterion and of the choice of step sizes). This shrinkage iteration is very simple to implement. At each step, we only need to compute an SVD and perform elementary matrix operations. With the help of a standard numerical linear algebra package, the whole algorithm can be coded in just a few lines.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

Before addressing further computational issues, we would like to make explicit the relationship between this iteration and the original problem (1.1). In Section 4, we will show that the sequence $\{{\mathbf{X}}^{k}\}$ converges to the unique solution of an optimization problem closely related to (1.1), namely, Furthermore, it is intuitive that the solution to this modified problem converges to that of (1.5) as $\tau\rightarrow\infty$ as shown in Section 3. Thus by selecting a large value of the parameter $\tau$, the sequence of iterates converges to a matrix which nearly minimizes (1.1).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

As mentioned earlier, there are two crucial properties which make this algorithm ideally suited for matrix completion.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

Low-rank property. A remarkable empirical fact is that the matrices in the sequence $\{{\mathbf{X}}^{k}\}$ have low rank (provided, of course, that the solution to (2.8) has low rank). We use the word "empirical" because all of our numerical experiments have produced low-rank sequences but we cannot rigorously prove that this is true in general. The reason for this phenomenon is, however, simple: because we are interested in large values of $\tau$ (as to better approximate the solution to (1.1)), the thresholding step happens to 'kill' most of the small singular values and produces a low-rank output. In fact, our numerical results show that the rank of ${\mathbf{X}}^{k}$ is nondecreasing with $k$, and the maximum rank is reached in the last steps of the algorithm, see Section 5.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

Thus, when the rank of the solution is substantially smaller than either dimension of the matrix, the storage requirement is low since we could store each ${\mathbf{X}}^{\mathbf{k}}$ in its SVD form (note that we only need to keep the current iterate and may discard earlier values).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

Sparsity. Another important property of the SVT algorithm is that the iteration matrix ${\mathbf{Y}}^{k}$ is sparse. Since ${\mathbf{Y}}^{0} = \mathbf{0}$, we have by induction that ${\mathbf{Y}}^{k}$ vanishes outside of $\Omega$. The fewer entries available, the sparser ${\mathbf{Y}}^{k}$. Because the sparsity pattern $\Omega$ is fixed throughout, one can then apply sparse matrix techniques to save storage. Also, if ${|\Omega|} = m$, the computational cost of updating ${\mathbf{Y}}^{k}$ is of order $m$. Moreover, we can call subroutines supporting sparse matrix computations, which can further reduce computational costs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Shrinkage iterations", "weight": 1.0} -->

One such subroutine is the SVD. However, note that we do not need to compute the entire SVD of ${\mathbf{Y}}^{k}$ to apply the singular value thresholding operator. Only the part corresponding to singular values greater than $\tau$ is needed. Hence, a good strategy is to apply the iterative Lanczos algorithm to compute the first few singular values and singular vectors. Because ${\mathbf{Y}}^{k}$ is sparse, ${\mathbf{Y}}^{k}$ can be applied to arbitrary vectors rapidly, and this procedure offers a considerable speedup over naive methods.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

Our algorithm is inspired by recent work in the area of $\ell_{1}$ minimization, and especially by the work on linearized Bregman iterations for compressed sensing, see for linearized Bregman iterations and for some information about the field of compressed sensing. In this line of work, linearized Bregman iterations are used to find the solution to an underdetermined system of linear equations with minimum $\ell_{1}$ norm. In fact, Theorem 2.1 asserts that the singular value thresholding algorithm can be formulated as a linearized Bregman iteration. Bregman iterations were first introduced in as a convenient tool for solving computational problems in the imaging sciences, and a later paper showed that they were useful for solving $\ell_{1}$-norm minimization problems in the area of compressed sensing. Linearized Bregman iterations were proposed in to improve performance of plain Bregman iterations, see also. Additional details together with a technique for improving the speed of convergence called kicking are described.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

On the practical side, the paper applied Bregman iterations to solve a deblurring problem while on the theoretical side, the references gave a rigorous analysis of the convergence of such iterations. New developments keep on coming out at a rapid pace and recently, introduced a new iteration, the split Bregman iteration, to extend Bregman-type iterations (such as linearized Bregman iterations) to problems involving the minimization of $\ell_{1}$-like functionals such as total-variation norms, Besov norms, and so forth.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

When applied to $\ell_{1}$-minimization problems, linearized Bregman iterations are sequences of soft-thresholding rules operating on vectors. Iterative soft-thresholding algorithms in connection with $\ell_{1}$ or total-variation minimization have quite a bit of history in signal and image processing and we would like to mention the works for total-variation minimization, for $\ell_{1}$ minimization, and for some recent applications in the area of image inpainting and image restoration. Just as iterative soft-thresholding methods are designed to find sparse solutions, our iterative singular value thresholding scheme is designed to find a sparse vector of singular values. In classical problems arising in the areas of compressed sensing, and signal or image processing, the sparsity is expressed in a known transformed domain and soft-thresholding is applied to transformed coefficients. In contrast, the shrinkage operator $\mathcal{D}_{\tau}$ is adaptive. The SVT not only discovers a sparse singular vector but also the bases in which we have a sparse representation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

In this sense, the SVT algorithm is an extension of earlier iterative soft-thresholding schemes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

Finally, we would like to contrast the SVT iteration (2.7) with the popular iterative soft-thresholding algorithm used in many papers in imaging processing and perhaps best known under the name of Proximal Forward-Backward Splitting method (PFBS), see for example. The constrained minimization problem (1.5) may be relaxed into for some $\lambda > 0$. Theorem 2.1 asserts that $\mathcal{D}_{\lambda}$ is the proximity operator of $\lambda{\|{\mathbf{X}}\|}_{\ast}$ and Proposition 3.1(iii) in gives that the solution to this unconstrained problem is characterized by the fixed point equation ${\mathbf{X}} = {\mathcal{D}_{\lambda\delta}{({{\mathbf{X}} + {\deltaP_{\Omega}{({{\mathbf{M}} - {\mathbf{X}}})}}})}}$ for each $\delta > 0$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

One can then apply a simplified version of the PFBS method (see (3.6) in) to obtain iterations of the form Introducing an intermediate matrix ${\mathbf{Y}}^{k}$, this algorithm may be expressed as The difference with (2.7) may seem subtle at first---replacing ${\mathbf{X}}^{k}$ in (2.10) with ${\mathbf{Y}}^{k - 1}$ and setting $\delta_{k} = \delta$ gives (2.7) with $\tau = {\lambda\delta}$---but has enormous consequences as this gives entirely different algorithms. First, they have different limits: while (2.7) converges to the solution of the constrained minimization (2.8), (2.10) converges to the solution of (2.9) provided that the sequence of step sizes is appropriately selected.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Relation with other works", "weight": 1.0} -->

Second, selecting a large $\lambda$ (or a large value of $\tau = {\lambda\delta}$) in (2.10) gives a low-rank sequence of iterates and a limit with small nuclear norm. The limit, however, does not fit the data and this is why one has to choose a small or moderate value of $\lambda$ (or of $\tau = {\lambda\delta}$). However, when $\lambda$ is not sufficiently large, the ${\mathbf{X}}^{k}$ may not have low rank even though the solution has low rank (and one may need to compute many singular vectors), and ${\mathbf{Y}}^{k}$ is not sufficiently sparse to make the algorithm computationally attractive. Moreover, the limit does not necessary have a small nuclear norm. These are reasons why (2.10) is not suitable for matrix completion.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Interpretation as a Lagrange multiplier method", "weight": 1.0} -->

In this section, we recast the SVT algorithm as a type of Lagrange multiplier algorithm known as Uzawa's algorithm. An important consequence is that this will allow us to extend the SVT algorithm to other problems involving the minimization of the nuclear norm under convex constraints, see Section 3. Further, another contribution of this paper is that this framework actually recasts linear Bregman iterations as a very special form of Uzawa's algorithm, hence providing fresh and clear insights about these iterations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Interpretation as a Lagrange multiplier method", "weight": 1.0} -->

From ${\mathbf{Y}}_{0} = \mathbf{0}$, say, inductively define where ${\{\delta_{k}\}}_{k \geq 1}$ is a sequence of positive step sizes. Uzawa's algorithm is, in fact, a subgradient method applied to the dual problem, where each step moves the current iterate in the direction of the gradient or of a subgradient.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Interpretation as a Lagrange multiplier method", "weight": 1.0} -->

Indeed, observe that where $\overset{\sim}{\mathbf{X}}$ is the minimizer of the Lagrangian for that value of $\mathbf{Y}$ so that a gradient descent update for $\mathbf{Y}$ is of the form It remains to compute the minimizer of the Lagrangian (2.12), and note that However, we know that the minimizer is given by $\mathcal{D}_{\tau}{({\mathcal{P}_{\Omega}{({\mathbf{Y}})}})}$ and since ${\mathbf{Y}}^{k} = {\mathcal{P}_{\Omega}{({\mathbf{Y}}^{k})}}$ for all $k \geq 0$, Uzawa's algorithm takes the form which is exactly the update (2.7). This point of view brings to bear many different mathematical tools for proving the convergence of the singular value thresholding iterations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Interpretation as a Lagrange multiplier method", "weight": 1.0} -->

For an early use of Uzawa's algorithm minimizing an $\ell_{1}$-like functional, the total-variation norm, under linear inequality constraints, see.

<!-- chunk {"id": "body-0040", "role": "body", "section": "General Formulation", "weight": 1.0} -->

This section presents a general formulation of the SVT algorithm for approximately minimizing the nuclear norm of a matrix under convex constraints.

<!-- chunk {"id": "body-0041", "role": "body", "section": "General convex constraints", "weight": 1.0} -->

One can also adapt the algorithm to handle general convex constraints. Suppose we wish to minimize $f_{\tau}{({\mathbf{X}})}$ defined as before over a convex set ${\mathbf{X}} \in \mathcal{C}$. To simplify, we will assume that this convex set is given by where the $f_{i}$'s are convex functionals (note that one can handle linear equality constraints by considering pairs of affine functionals). The problem of interest is then of the form Just as before, it is intuitive that as $\tau\rightarrow\infty$, the solution to this problem converges to a minimizer of the nuclear norm under the same constraints (1.7) as shown in Theorem 3.1 at the end of this section.

<!-- chunk {"id": "body-0042", "role": "body", "section": "General convex constraints", "weight": 1.0} -->

Put ${\mathcal{F}{({\mathbf{X}})}}:={({f_{1}{({\mathbf{X}})}},\ldots,{f_{m}{({\mathbf{X}})}})}$ for short. Then the Lagrangian for (3.4) is equal to where ${\mathbf{X}} \in {\mathbb{R}}^{n_{1} \times n_{2}}$ and ${\mathbf{y}} \in {\mathbb{R}}^{m}$ is now a vector with nonnegative components denoted, as usual, by ${\mathbf{y}} \geq \mathbf{0}$. One can apply Uzawa's method just as before with the only modification that we will use a subgradient method with projection to maximize the dual function since we need to make sure that the successive updates ${\mathbf{y}}^{k}$ belong to the nonnegative orthant.

<!-- chunk {"id": "body-0043", "role": "body", "section": "General convex constraints", "weight": 1.0} -->

This gives Above, ${\mathbf{x}}_{+}$ is of course the vector with entries equal to $\max{(x_{i},0)}$. When $\mathcal{F}$ is an affine mapping of the form ${\mathbf{b}} - {\mathcal{A}{({\mathbf{X}})}}$ so that one solves and thus the extension to linear inequality constraints is straightforward.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example", "weight": 1.0} -->

An interesting example concerns the extension of the Dantzig selector to matrix problems. Suppose we have available linear measurements about a matrix $\mathbf{M}$ of interest where ${\mathbf{z}} \in {\mathbb{R}}^{m}$ is a noise vector. Then under these circumstances, one might want to find the matrix which minimizes the nuclear norm among all matrices which are consistent with the data $\mathbf{b}$. Inspired by the work on the Dantzig selector which was originally developed for estimating sparse parameter vectors from noisy data, one could approach this problem by solving where $\mathbf{E}$ is an array of tolerances, which is adjusted to fit the noise statistics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example", "weight": 1.0} -->

Above, ${\text{vec}{({\mathbf{A}})}} \leq {\text{vec}{({\mathbf{B}})}}$, for any two matrices $\mathbf{A}$ and $\mathbf{B}$, means componentwise inequalities; that is, $A_{ij} \leq B_{ij}$ for all indices $i,j$. We use this notation as not to confuse the reader with the positive semidefinite ordering.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example", "weight": 1.0} -->

In the case of the matrix completion problem where $\mathcal{A}$ extracts sampled entries indexed by $\Omega$, one can always see the data vector as the sampled entries of some matrix $\mathbf{B}$ obeying ${\mathcal{P}_{\Omega}{({\mathbf{B}})}} = {\mathcal{A}^{\ast}{({\mathbf{b}})}}$; the constraint is then natural for it may be expressed as If $\mathbf{z}$ is white noise with standard deviation $\sigma$, one may want to use a multiple of $\sigma$ for $E_{ij}$. In words, we are looking for a matrix with minimum nuclear norm under the constraint that all of its sampled entries do not deviate too much from what has been observed.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example", "weight": 1.0} -->

We conclude by noting that in the matrix completion problem where ${\mathcal{A}^{\ast}\mathcal{A}} = \mathcal{P}_{\Omega}$ and one observes $\mathcal{P}_{\Omega}{({\mathbf{B}})}$, one can check that this iteration simplifies to Again, this is easy to implement and whenever the solution has low rank, the iterates ${\mathbf{X}}^{k}$ have low rank as well.

<!-- chunk {"id": "body-0048", "role": "body", "section": "When the proximal problem gets close", "weight": 1.0} -->

We now show that minimizing the proximal objective ${f_{\tau}{({\mathbf{X}})}} = {{\tau{\|{\mathbf{X}}\|}_{\ast}} + {\frac{1}{2}{\|{\mathbf{X}}\|}_{F}^{2}}}$ is the same as minimizing the nuclear norm in the limit of large $\tau$'s. The theorem below is general and covers the special case of linear equality constraints as in (2.8).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

This section establishes the convergence of the SVT iterations. We begin with the simpler proof of the convergence of (2.7) in the special case of the matrix completion problem, and then present the argument for the more general constraints (3.5). We hope that this progression will make the second and more general proof more transparent.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Convergence for matrix completion", "weight": 1.0} -->

We begin by recording a lemma which establishes the strong convexity of the objective $f_{\tau}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "General convergence theorem", "weight": 1.0} -->

Our second result is more general and establishes the convergence of the SVT iterations to the solution of (3.4) under general convex constraints. From now now, we will only assume that the function $\mathcal{F}{({\mathbf{X}})}$ is Lipschitz in the sense that for some nonnegative constant $L{(\mathcal{F})}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "General convergence theorem", "weight": 1.0} -->

We also recall that ${\mathcal{F}{({\mathbf{X}})}} = {({f_{1}{({\mathbf{X}})}},\ldots,{f_{m}{({\mathbf{X}})}})}$ where each $f_{i}$ is convex, and that the Lagrangian for the problem (3.4) is given by We will assume to simplify that strong duality holds which is automatically true if the constraints obey constraint qualifications such as Slater's condition.

<!-- chunk {"id": "body-0053", "role": "body", "section": "General convergence theorem", "weight": 1.0} -->

We first establish the following preparatory lemma.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Implementation and Numerical Results", "weight": 1.0} -->

This section provides implementation details of the SVT algorithm---as to make it practically effective for matrix completion---such as the numerical evaluation of the singular value thresholding operator, the selection of the step size $\delta_{k}$, the selection of a stopping criterion, and so. This section also introduces several numerical simulation results which demonstrate the performance and effectiveness of the SVT algorithm. We show that $30,{000 \times 30},000$ matrices of rank 10 are recovered from just about 0.4% of their sampled entries in a matter of a few minutes on a modest desktop computer with a 1.86 GHz CPU (dual core with Matlab's multithreading option enabled) and 3 GB of memory.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluation of the singular value thresholding operator", "weight": 1.0} -->

To apply the singular value tresholding operator at level $\tau$ to an input matrix, it suffices to know those singular values and corresponding singular vectors above the threshold $\tau$. In the matrix completion problem, the singular value thresholding operator is applied to sparse matrices $\{{\mathbf{Y}}^{k}\}$ since the number of sampled entries is typically much lower than the number of entries in the unknown matrix $\mathbf{M}$, and we are hence interested in numerical methods for computing the dominant singular values and singular vectors of large sparse matrices. The development of such methods is a relatively mature area in scientific computing and numerical linear algebra in particular. In fact, many high-quality packages are readily available. Our implementation uses PROPACK, see for documentation and availability. One reason for this choice is convenience: PROPACK comes in a Matlab and a Fortran version, and we find it convenient to use the well-documented Matlab version. More importantly, PROPACK uses the iterative Lanczos algorithm to compute the singular values and singular vectors directly, by using the Lanczos bidiagonalization algorithm with partial reorthogonalization.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluation of the singular value thresholding operator", "weight": 1.0} -->

In particular, PROPACK does not compute the eigenvalues and eigenvectors of ${({\mathbf{Y}}^{k})}^{\ast}{\mathbf{Y}}^{k}$ and ${\mathbf{Y}}^{k}{({\mathbf{Y}}^{k})}^{\ast}$, or of an augmented matrix as in the Matlab built-in function 'svds' for example. Consequently, PROPACK is an efficient---both in terms of number of flops and storage requirement---and stable package for computing the dominant singular values and singular vectors of a large sparse matrix. For information, the available documentation reports a speedup factor of about ten over Matlab's 'svds'. Furthermore, the Fortran version of PROPACK is about 3--4 times faster than the Matlab version.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluation of the singular value thresholding operator", "weight": 1.0} -->

Despite this significant speedup, we have only used the Matlab version but since the singular value shrinkage operator is by-and-large the dominant cost in the SVT algorithm, we expect that a Fortran implementation would run about 3 to 4 times faster.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation of the singular value thresholding operator", "weight": 1.0} -->

As for most SVD packages, though one can specify the number of singular values to compute, PROPACK can not automatically compute only those singular values exceeding the threshold $\tau$. One must instead specify the number $s$ of singular values ahead of time, and the software will compute the $s$ largest singular values and corresponding singular vectors. To use this package, we must then determine the number $s_{k}$ of singular values of ${\mathbf{Y}}^{k - 1}$ to be computed at the $k$th iteration. We use the following simple method. Let $r_{k - 1} = {{rank}{({\mathbf{X}}^{k - 1})}}$ be the number of nonzero singular values of ${\mathbf{X}}^{k - 1}$ at the previous iteration. Set $s_{k} = {r_{k - 1} + 1}$ and compute the first $s_{k}$ singular values of ${\mathbf{Y}}^{k - 1}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluation of the singular value thresholding operator", "weight": 1.0} -->

If some of the computed singular values are already smaller than $\tau$, then $s_{k}$ is a right choice. Otherwise, increment $s_{k}$ by a predefined integer $\ell$ repeatedly until some of the singular values fall below $\tau$. In the experiments, we choose $\ell = 5$. Another rule might be to repeatedly multiply $s_{k}$ by a positive number---e.g. 2---until our criterion is met. Incrementing $s_{k}$ by a fixed integer works very well in practice; in our experiments, we very rarely need more than one update.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluation of the singular value thresholding operator", "weight": 1.0} -->

We note that it is not necessary to rerun the Lanczos iterations for the first $s_{k}$ vectors since they have been already computed; only a few new singular values ($\ell$ of them) need to be numerically evaluated. This can be done by modifying the PROPACK routines. We have not yet modified PROPACK, however. Had we done so, our run times would be decreased.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Step sizes", "weight": 1.0} -->

There is a large literature on ways of selecting a step size but for simplicity, we shall use step sizes that are independent of the iteration count; that is $\delta_{k} = \delta$ for $k = {1,2,\ldots}$. From Theorem 4.2, convergence for the completion problem is guaranteed (2.7) provided that $0 < \delta < 2$. This choice is, however, too conservative and the convergence is typically slow. In our experiments, we use instead i.e. $1.2$ times the undersampling ratio. We give a heuristic justification below.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Step sizes", "weight": 1.0} -->

Consider a fixed matrix ${\mathbf{A}} \in {\mathbb{R}}^{n_{1} \times n_{2}}$. Under the assumption that the column and row spaces of $\mathbf{A}$ are not well aligned with the vectors taken from the canonical basis of ${\mathbb{R}}^{n_{1}}$ and ${\mathbb{R}}^{n_{2}}$ respectively---the incoherence assumption in ---then with very large probability over the choices of $\Omega$, we have provided that the rank of $\mathbf{A}$ is not too large. The probability model is that $\Omega$ is a set of sampled entries of cardinality $m$ sampled uniformly at random so that all the choices are equally likely.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Step sizes", "weight": 1.0} -->

In (5.2), we want to think of $\epsilon$ as a small constant, e.g. smaller than 1/2. In other words, the 'energy' of $\mathbf{A}$ on $\Omega$ (the set of sampled entries) is just about proportional to the size of $\Omega$. The near isometry (5.2) is a consequence of Theorem 4.1, and we omit the details.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Step sizes", "weight": 1.0} -->

Then we could take $\delta$ inversely proportional to $p$; e.g. with $\epsilon = {1/4}$, we could take $\delta \leq {1.6p^{- 1}}$. Below, we shall use the value $\delta = {1.2p^{- 1}}$ which allows us to take large steps and still provides convergence, at least empirically.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Step sizes", "weight": 1.0} -->

The reason why this is not a rigorous argument is that (5.2) cannot be applied to ${\mathbf{A}} = {{\mathbf{X}}^{\star} - {\mathbf{X}}^{k}}$ even though this matrix difference may obey the incoherence assumption. The issue here is that ${\mathbf{X}}^{\star} - {\mathbf{X}}^{k}$ is not a fixed matrix, but rather depends on $\Omega$ since the iterates $\{{\mathbf{X}}^{k}\}$ are computed with the knowledge of the sampled set.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Initial steps", "weight": 1.0} -->

The SVT algorithm starts with ${\mathbf{Y}}^{0} = \mathbf{0}$, and we want to choose a large $\tau$ to make sure that the solution of (2.8) is close enough to a solution of (1.1). Define $k_{0}$ as that integer obeying Since ${\mathbf{Y}}^{0} = \mathbf{0}$, it is not difficult to see that To save work, we may simply skip the computations of ${\mathbf{X}}^{1},\ldots,{\mathbf{X}}^{k_{0}}$, and start the iteration by computing ${\mathbf{X}}^{k_{0} + 1}$ from ${\mathbf{Y}}^{k_{0}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Initial steps", "weight": 1.0} -->

This strategy is a special case of a kicking device introduced; the main idea of such a kicking scheme is that one can 'jump over' a few steps whenever possible. Just like in the aforementioned reference, we can develop similar kicking strategies here as well. Because in our numerical experiments the kicking is rarely triggered, we forgo the description of such strategies.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

Here, we discuss stopping criteria for the sequence of SVT iterations (2.7), and present two possibilities.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

The first is motivated by the first-order optimality conditions or KKT conditions tailored to the minimization problem (2.8). By (2.14) and letting ${\partial_{\mathbf{Y}}{g_{0}{({\mathbf{Y}})}}} = \mathbf{0}$ in (2.13), we see that the solution ${\mathbf{X}}_{\tau}^{\star}$ to (2.8) must also verify where $\mathbf{Y}$ is a matrix vanishing outside of $\Omega^{c}$. Therefore, to make sure that ${\mathbf{X}}^{k}$ is close to ${\mathbf{X}}_{\tau}^{\star}$, it is sufficient to check how close $({\mathbf{X}}^{k},{\mathbf{Y}}^{k - 1})$ is to obeying (5.4). By definition, the first equation in (5.4) is always true.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

Therefore, it is natural to stop (2.7) when the error in the second equation is below a specified tolerance. We suggest stopping the algorithm when where $\epsilon$ is a fixed tolerance, e.g. $10^{- 4}$. We provide a short heuristic argument justifying this choice below.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

In the matrix completion problem, we know that under suitable assumptions which is just (5.2) applied to the fixed matrix $\mathbf{M}$ (the symbol $\asymp$ here means that there is a constant $\epsilon$ as in (5.2)). Suppose we could also apply (5.2) to the matrix ${\mathbf{X}}^{k} - {\mathbf{M}}$ (which we rigorously cannot since ${\mathbf{X}}^{k}$ depends on $\Omega$), then we would have In words, one would control the relative reconstruction error by controlling the relative error on the set of sampled locations.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

A second stopping criterion comes from duality theory. Firstly, the iterates ${\mathbf{X}}^{k}$ are generally not feasible for (2.8) although they become asymptotically feasible.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

Since ${\overset{\sim}{\mathbf{X}}}^{k}$ is feasible, we have Secondly, using the notations of Section 2.4, duality theory gives that Therefore, $b_{k} - a_{k}$ is an upper bound on the duality gap and one can stop the algorithm when this quantity falls below a given tolerance.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Stopping criteria", "weight": 1.0} -->

For very large problems in which one holds ${\mathbf{X}}^{k}$ in reduced SVD form, one may not want to compute the projection ${\overset{\sim}{\mathbf{X}}}^{k}$ since this matrix would not have low rank and would require significant storage space (presumably, one would not want to spend much time computing this projection either). Hence, the second method only makes practical sense when the dimensions are not prohibitively large, or when the iterates do not have low rank.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We conclude this section by summarizing the implementation details and give the SVT algorithm for matrix completion below (Algorithm 1). Of course, one would obtain a very similar structure for the more general problems of the form (3.1) and (3.4) with linear inequality constraints.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Input: sampled set Ω and sampled entries 𝒫Ω (M), step size δ, tolerance ϵ, parameter τ, increment ℓ, and maximum iteration count kmax Output: Xopt Description: Recover a low-rank matrix M from a subset of sampled entries 1Set Y0 = k0 δ 𝒫Ω (M) (k0 is defined in (5.3)) 2Set r0 = 0 3for k = 1 to kmax 44Set sk = rk − 1 + 1 5repeat 66Compute [Uk − 1, Σk − 1, Vk − 1]sk 7Set sk = sk + ℓ 88until σsk − ℓk − 1 ≤ τ 9Set rk = max {j: σjk − 1 > τ} 10Set ${\mathbf{X}}^{k} = {\sum_{j = 1}^{r_{k}}{{({\sigma_{j}^{k - 1} - \tau})}{\mathbf{u}}_{j}^{k - 1}{\mathbf{v}}_{j}^{k -

<!-- chunk {"id": "body-0077", "role": "body", "section": "Linear equality constraints", "weight": 1.0} -->

Our implementation is in Matlab and all the computational results we are about to report were obtained on a desktop computer with a 1.86 GHz CPU (dual core with Matlab's multithreading option enabled) and 3 GB of memory. In our simulations, we generate $n \times n$ matrices of rank $r$ by sampling two $n \times r$ factors ${\mathbf{M}}_{L}$ and ${\mathbf{M}}_{R}$ independently, each having i.i.d. Gaussian entries, and setting ${\mathbf{M}} = {{\mathbf{M}}_{L}{\mathbf{M}}_{R}^{\ast}}$ as it is suggested. The set of observed entries $\Omega$ is sampled uniformly at random among all sets of cardinality $m$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Linear equality constraints", "weight": 1.0} -->

The recovery is performed via the SVT algorithm (Algorithm 1), and we use as a stopping criterion. As discussed earlier, the step sizes are constant and we set $\delta = {1.2p^{- 1}}$. Throughout this section, we denote the output of the SVT algorithm by ${\mathbf{X}}^{opt}$. The parameter $\tau$ is chosen empirically and set to $\tau = {5n}$. A heuristic argument is as follows. Clearly, we would like the term $\tau{\|{\mathbf{M}}\|}_{\ast}$ to dominate the other, namely, $\frac{1}{2}{\|{\mathbf{M}}\|}_{F}^{2}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Linear equality constraints", "weight": 1.0} -->

For products of Gaussian matrices as above, standard random matrix theory asserts that the Frobenius norm of $\mathbf{M}$ concentrates around $n\sqrt{r}$, and that the nuclear norm concentrates around about $nr$ (this should be clear in the simple case where $r = 1$ and is generally valid). The value $\tau = {5n}$ makes sure that on the average, the value of $\tau{\|{\mathbf{M}}\|}_{\ast}$ is about $10$ times that of $\frac{1}{2}{\|{\mathbf{M}}\|}_{F}^{2}$ as long as the rank is bounded away from the dimension $n$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "iters", "weight": 1.0} -->

Our computational results are displayed in Table 1. There, we report the run time in seconds, the number of iterations it takes to reach convergence (5.7), and the relative error of the reconstruction where $\mathbf{M}$ is the real unknown matrix. All of these quantities are averaged over five runs. The table also gives the percentage of entries that are observed, namely, $m/n^{2}$ together with a quantity that we may want to think as the information oversampling ratio. Recall that an $n \times n$ matrix of rank $r$ depends upon $d_{r}:={r{({{2n} - r})}}$ degrees of freedom. Then $m/d_{r}$ is the ratio between the number of sampled entries and the 'true dimensionality' of an $n \times n$ matrix of rank $r$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "iters", "weight": 1.0} -->

The first observation is that the SVT algorithm performs extremely well in these experiments. In all of our experiments, it takes fewer than 200 SVT iterations to reach convergence. As a consequence, the run times are short. As indicated in the table, we note that one recovers a $1,{000 \times 1},000$ matrix of rank $10$ in less than a minute. The algorithm also recovers $30,{000 \times 30},000$ matrices of rank $10$ from about $0.4\%$ of their sampled entries in just about 17 minutes. In addition, higher-rank matrices are also efficiently completed: for example, it takes between one and two hours to recover $10,{000 \times 10},000$ matrices of rank $100$ and $20,{000 \times 20},000$ matrices of rank $50$. We would like to stress that these numbers were obtained on a modest CPU (1.86GHz). Furthermore, a Fortran implementation is likely to cut down on these numbers by a multiplicative factor typically between three and four.

<!-- chunk {"id": "body-0082", "role": "body", "section": "iters", "weight": 1.0} -->

We also check the validity of the stopping criterion (5.7) by inspecting the relative error defined in (5.8). The table shows that the heuristic and nonrigorous analysis of Section 5.1 holds in practice since the relative reconstruction error is of the same order as ${{\|{\mathcal{P}_{\Omega}{({{\mathbf{X}}^{opt} - {\mathbf{M}}})}}\|}_{F}/{\|{\mathcal{P}_{\Omega}{\mathbf{M}}}\|}_{F}} \sim 10^{- 4}$. Indeed, the overall relative errors reported in Table 1 are all less than $2 \times 10^{- 4}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "iters", "weight": 1.0} -->

We emphasized all along an important feature of the SVT algorithm, which is that the matrices ${\mathbf{X}}^{k}$ have low rank. We demonstrate this fact empirically in Figure 1, which plots the rank of ${\mathbf{X}}^{k}$ versus the iteration count $k$, and does this for unknown matrices of size $5,{000 \times 5},000$ with different ranks. The plots reveal an interesting phenomenon: in our experiments, the rank of ${\mathbf{X}}^{k}$ is nondecreasing so that the maximum rank is reached in the final steps of the algorithm. In fact, the rank of the iterates quickly reaches the value $r$ of the true rank. After these few initial steps, the SVT iterations search for that matrix with rank $r$ minimizing the objective functional. As mentioned earlier, the low-rank property is crucial for making the algorithm run fast.

<!-- chunk {"id": "body-0084", "role": "body", "section": "iters", "weight": 1.0} -->

Finally, we demonstrate the results of the SVT algorithm for matrix completion from noisy sampled entries. Suppose we observe data from the model where $\mathbf{Z}$ is a zero-mean Gaussian white noise with standard deviation $\sigma$. We run the SVT algorithm but stop early, as soon as ${\mathbf{X}}^{k}$ is consistent with the data and obeys where $\epsilon$ is a small parameter. Our reconstruction $\hat{\mathbf{M}}$ is the first ${\mathbf{X}}^{k}$ obeying (5.10). The results are shown in Table 2 (the quantities are averages of 5 runs). Define the noise ratio as and the relative error by (5.8). From Table 2, we see that the SVT algorithm works well as the relative error between the recovered and the true data matrix is just about equal to the noise ratio.

<!-- chunk {"id": "body-0085", "role": "body", "section": "iters", "weight": 1.0} -->

The theory of low-rank matrix recovery from noisy data is nonexistent at the moment, and is obviously beyond the scope of this paper. Having said this, we would like to conclude this section with an intuitive and nonrigorous discussion, which may explain why the observed recovery error is within the noise level. Suppose again that $\hat{\mathbf{M}}$ obeys (5.6), namely, As mentioned earlier, one condition for this to happen is that $\mathbf{M}$ and $\hat{\mathbf{M}}$ have low rank. This is the reason why it is important to stop the algorithm early as we hope to obtain a solution which is both consistent with the data and has low rank (the limit of the SVT iterations, $\lim_{k\rightarrow\infty}{\mathbf{X}}^{k}$, will not generally have low rank since there may be no low-rank matrix matching the noisy data).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Linear inequality constraints", "weight": 1.0} -->

We now examine the speed at which one can solve similar problems with linear inequality constraints instead of linear equality constraints. We assume the model (5.9), where the matrix $\mathbf{M}$ of rank $r$ is sampled as before, and solve the problem (3.8) by using (3.10). We formulate the inequality constraints in (3.8) with $E_{ij} = \sigma$ so that one searches for a solution $\hat{\mathbf{M}}$ with minimum nuclear norm among all those matrices whose sampled entries deviate from the observed ones by at most the noise level $\sigma$.^22^2This may not be conservative enough from a statistical viewpoint but this works well in this case, and our emphasis here is on computational rather than statistical issues.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Linear inequality constraints", "weight": 1.0} -->

In this experiment, we adjust $\sigma$ to be one tenth of a typical absolute entry of $\mathbf{M}$, i.e. $\sigma = {0.1{\sum_{{ij} \in \Omega}{{|M_{ij}|}/m}}}$, and the noise ratio as defined earlier is 0.780. We set $n = {1,000}$, $r = 10$, and the number $m$ of sampled entries is five times the number of degrees of freedom, i.e. $m = {5d_{r}}$. Just as before, we set $\tau = {5n}$, and choose a constant step size $\delta = {1.2p^{- 1}}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Linear inequality constraints", "weight": 1.0} -->

The results, reported in Figure 2, show that the algorithm behaves just as well with linear inequality constraints. To make this point, we compare our results with those obtained from noiseless data (same unknown matrix and sampled locations). In the noiseless case, it takes about 150 iterations to reach the tolerance $\epsilon = 10^{- 4}$ whereas in the noisy case, convergence occurs in about 200 iterations (Figure 2(a)). In addition, just as in the noiseless problem, the rank of the iterates is nondecreasing and quickly reaches the true value $r$ of the rank of the unknown matrix $\mathbf{M}$ we wish to recover (Figure 2(b)). As a consequence the SVT iterations take about the same amount of time as in the noiseless case (Figure 2(c)) so that the total running time of the algorithm does not appear to be substantially different from that in the noiseless case.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Linear inequality constraints", "weight": 1.0} -->

We close by pointing out that from a statistical point of view, the recovery of the matrix $\mathbf{M}$ from undersampled and noisy entries by the matrix equivalent of the Dantzig selector appears to be accurate since the relative error obeys ${{\|{\hat{\mathbf{M}} - {\mathbf{M}}}\|}_{F}/{\|{\mathbf{M}}\|}_{F}} = 0.0769$ (recall that the noise ratio is about $0.08$).

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

This paper introduced a novel algorithm, namely, the singular value thresholding algorithm for matrix completion and related nuclear norm minimization problems. This algorithm is easy to implement and surprisingly effective both in terms of computational cost and storage requirement when the minimum nuclear-norm solution is also the lowest-rank solution. We would like to close this paper by discussing a few open problems and research directions related to this work.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our algorithm exploits the fact that the sequence of iterates $\{{\mathbf{X}}^{k}\}$ have low rank when the minimum nuclear solution has low rank. An interesting question is whether one can prove (or disprove) that in a majority of the cases, this is indeed the case.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion", "weight": 1.5} -->

It would be interesting to explore other ways of computing $\mathcal{D}_{\tau}{({\mathbf{Y}})}$---in words, the action of the singular value shrinkage operator. Our approach uses the Lanczos bidiagonalization algorithm with partial reorthogonalization which takes advantages of sparse inputs but other approaches are possible. We mention two of them.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Discussion", "weight": 1.5} -->

A series of papers have proposed the use of randomized procedures for the approximation of a matrix $\mathbf{Y}$ with a matrix $\mathbf{Z}$ of rank $r$. When this approximation consists of the truncated SVD retaining the part of the expansion corresponding to singular values greater than $\tau$, this can be used to evaluate $\mathcal{D}_{\tau}{({\mathbf{Y}})}$. Some of these algorithms are efficient when the input $\mathbf{Y}$ is sparse, and it would be interesting to know whether these methods are fast and accurate enough to be used in the SVT iteration (2.7).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion", "weight": 1.5} -->

A wide range of iterative methods for computing matrix functions of the general form $f{({\mathbf{Y}})}$ are available today, see for a survey. A valuable research direction is to investigate whether some of these iterative methods, or other to be developed, would provide powerful ways for computing $\mathcal{D}_{\tau}{({\mathbf{Y}})}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion", "weight": 1.5} -->

In practice, one would like to solve (2.8) for large values of $\tau$. However, a larger value of $\tau$ generally means a slower rate of convergence. A good strategy might be to start with a value of $\tau$, which is large enough so that (2.8) admits a low-rank solution, and at the same time for which the algorithm converges rapidly. One could then use a continuation method as in to increase the value of $\tau$ sequentially according to a schedule $\tau_{0},\tau_{1},\ldots$, and use the solution to the previous problem with $\tau = \tau_{i - 1}$ as an initial guess for the solution to the current problem with $\tau = \tau_{i}$ (warm starting). We hope to report on this in a separate paper.
