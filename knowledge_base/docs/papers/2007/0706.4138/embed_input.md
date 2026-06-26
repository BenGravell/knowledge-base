<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization

Topics include Rank minimization, Nuclear norm, Compressed sensing, Convex relaxation, Restricted isometry, Matrix recovery.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that nuclear-norm minimization can recover minimum-rank matrices from linear measurements under restricted-isometry conditions. The paper establishes low-rank recovery as the matrix analogue of sparse compressed sensing and ties it to system identification, embedding, and recommendation problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The affine rank minimization problem consists of finding a matrix of minimum rank that satisfies a given system of linear equality constraints. Such problems have appeared in the literature of a diverse set of fields including system identification and control, Euclidean embedding, and collaborative filtering. Although specific instances can often be solved with specialized algorithms, the general affine rank minimization problem is NP-hard. In this paper, we show that if a certain restricted isometry property holds for the linear transformation defining the constraints, the minimum rank solution can be recovered by solving a convex optimization problem, namely the minimization of the nuclear norm over the given affine space. We present several random ensembles of equations where the restricted isometry property holds with overwhelming probability. The techniques used in our analysis have strong parallels in the compressed sensing framework. We discuss how affine rank minimization generalizes this pre-existing concept and outline a dictionary relating concepts from cardinality minimization to those of rank minimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notions such as order, complexity, or dimensionality can often be expressed by means of the rank of an appropriate matrix. For example, a low-rank matrix could correspond to a low-degree statistical model for a random process (e.g., factor analysis), a low-order realization of a linear system, a low-order controller for a plant, or a low-dimensional embedding of data in Euclidean space. If the set of feasible models or designs is affine in the matrix variable, choosing the simplest model can be cast as an *affine rank minimization problem*, where $X \in {\mathbb{R}}^{m \times n}$ is the decision variable, and the linear map $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ and vector $b \in {\mathbb{R}}^{p}$ are given. In certain instances with very special structure, the rank minimization problem can be solved by using the singular value decomposition, or can be exactly reduced to the solution of linear systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, however, problem (1.1) is a challenging nonconvex optimization problem for which all known finite time algorithms have at least doubly exponential running times in both theory and practice. For the general case, a variety of heuristic algorithms based on local optimization, including alternating projections and alternating LMIs, have been proposed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A recent heuristic introduced in minimizes the *nuclear norm*, or the sum of the singular values of the matrix, over the affine subset. The nuclear norm is a convex function, can be optimized efficiently, and is the best convex approximation of the rank function over the unit ball of matrices with norm less than one. When the matrix variable is symmetric and positive semidefinite, this heuristic is equivalent to the trace heuristic often used by the control community (see, e.g., ). The nuclear norm heuristic has been observed to produce very low-rank solutions in practice, but a theoretical characterization of when it produces the minimum rank solution has not been previously available. This paper provides the first such mathematical characterization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work is built upon a large body of literature on a related optimization problem. When the matrix variable is constrained to be diagonal, the affine rank minimization problem reduces to finding the *sparsest vector* in an affine subspace. This problem is commonly referred to as *cardinality minimization*, since we seek the vector whose support has the smallest cardinality, and is known to be NP-hard. For diagonal matrices, the sum of the singular values is equal to the sum of the absolute values (i.e., the $\ell_{1}$ norm) of the diagonal elements. Minimization of the $\ell_{1}$ norm is a well-known heuristic for the cardinality minimization problem, and stunning results pioneered by Candès and Tao and Donoho have characterized a vast set of instances for which the $\ell_{1}$ heuristic can be *a priori* guaranteed to yield the optimal solution. These techniques provide the foundations of the recently developed *compressed sensing* or *compressive sampling* frameworks for measurement, coding, and signal estimation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As has been shown by a number of research groups (e.g., ), the $\ell_{1}$ heuristic for cardinality minimization provably recovers the sparsest solution whenever the sensing matrix has certain "basis incoherence" properties, and in particular, when it is randomly chosen according to certain specific ensembles.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The fact that the $\ell_{1}$ heuristic is a special case of the nuclear norm heuristic suggests that these results from the compressed sensing literature might be extended to provide guarantees about the nuclear norm heuristic for the more general rank minimization problem. In this paper, we show that this is indeed the case, and the parallels are surprisingly strong. Following the program laid out in the work of Candès and Tao, our main contribution is the development of a restricted isometry property (RIP), under which the nuclear norm heuristic can be *guaranteed* to produce the minimum-rank solution. Furthermore, as in the case for the $\ell_{1}$ heuristic, we provide several specific examples of matrix ensembles for which RIP holds with overwhelming probability. Our results considerably extend the compressed sensing machinery in a so far undeveloped direction, by allowing a much more general notion of parsimonious models that rely on low-rank assumptions instead of cardinality restrictions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make the parallels as clear as possible, we begin by establishing a dictionary between the matrix rank and nuclear norm minimization problems and the vector sparsity and $\ell_{1}$ norm problems in Section 2. In the process of this discussion, we present a review of many useful properties of the matrices and matrix norms necessary for the main results. We then generalize the notion of Restricted Isometry to matrices in Section 3 and show that when linear mappings are Restricted Isometries, recovering low-rank solutions of underdetermined systems can be achieved by nuclear norm minimization. In Section 4, we present several families of random linear maps that are restricted isometries with overwhelming probability when the dimensions are sufficiently large. In Section 5, we briefly discuss three different algorithms designed for solving the nuclear norm minimization problem and their relative strengths and weaknesses: interior point methods, gradient projection methods, and a low-rank factorization technique. In Section 6, we demonstrate that in practice nuclear-norm minimization recovers the lowest rank solutions of affine sets with even fewer constraints than those guaranteed by our mathematical analysis. Finally, in Section 7, we list a number of possible directions for future research.

<!-- chunk {"id": "body-0011", "role": "body", "section": "When are random constraints interesting for rank minimization?", "weight": 1.0} -->

As in the case of compressed sensing, the conditions we derive to guarantee properties about the nuclear norm heuristic are deterministic, but they are at least as difficult to check as solving the rank minimization problem itself. We are only able to guarantee that the nuclear norm heuristic recovers the minimum rank solution of ${\mathcal{A}{(X)}} = b$ when $\mathcal{A}$ is sampled from specific ensembles of random maps. The constraints appearing in many of the applications mentioned above, such as low-order control system design, are typically not random at all and have structured demands according to the specifics of the design problem. It thus behooves us to present several examples where random constraints manifest themselves in practical scenarios for which no practical solution procedure is known.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Minimum order linear system realization", "weight": 1.0} -->

Rank minimization forms the basis of many model reduction and low-order system identification problems for linear time-invariant (LTI) systems. The following example illustrates how random constraints might arise in this context. Consider the problem of finding the minimum order discrete-time LTI system that is consistent with a set of time-domain observations. In particular, suppose our observations are the system output sampled at a fixed time $N$, after a random Gaussian input signal is applied from $t = 0$ to $t = N$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Minimum order linear system realization", "weight": 1.0} -->

Suppose we make such measurements for $p$ different input signals, that is, we observe ${y_{i}{(N)}} = {\sum_{t = 0}^{N}{a_{i}{({N - t})}h{(t)}}}$ for $i = {1,\ldots,p}$, where $a_{i}$, the $i$th input signal, is a zero-mean Gaussian random variable with the same variance for $t = {0,{\ldotsN}}$, and $h{(t)}$ denotes the impulse response. We can write this compactly as $y = {Ah}$, where $h = {\lbrack{h{}},\ldots,{h{(N)}}\rbrack}'$, and $A_{ij} = {a_{i}{({N - j})}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Minimum order linear system realization", "weight": 1.0} -->

From linear system theory, the order of the minimal realization for such a system is given by the rank of the following Hankel matrix (see, e.g.,) Therefore the problem can be expressed as where the optimization variables are ${h{}},\ldots,{h{({2N})}}$, and the matrix $A$ consists of i.i.d. zero-mean Gaussian entries.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Low-Rank Matrix Completion", "weight": 1.0} -->

In the matrix completion problem where we are given random subset of entries of a matrix, we would like to fill in the missing entries such that the resulting matrix has the lowest possible rank. This problem arises in machine learning scenarios where we are given partially observed examples of a process with a low-rank covariance matrix and would like to estimate the missing data. A typical situation where the hidden matrix is low-rank is when the columns are i.i.d. samples of a random process with low-rank covariance. Such models are ubiquitous in Factor Analysis, Collaborative Filtering, and Latent Semantic Indexing. In many of these settings, some prior probability distribution (such as a Bernoulli model or uniform distribution on subsets) is assumed to generate the set of available entries.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Low-Rank Matrix Completion", "weight": 1.0} -->

Suppose we are presented with a set of triples $({I{(i)}},{J{(i)}},{S{(i)}})$ for $i = {1,\ldots,p}$ and wish to find the matrix with $S{(i)}$ in the entry corresponding to row $I{(i)}$ and column $J{(i)}$ for all $i$. The matrix completion problem seeks to solve which is a special case of the affine rank minimization problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Low-dimensional Euclidean embedding problems", "weight": 1.0} -->

A problem that arises in a variety of fields is the determination of configurations of points in low-dimensional Euclidean spaces, subject to some given distance information. In Multi-Dimensional Scaling (MDS), such problems occur in extracting the underlying geometric structure of distance data. In psychometrics, the information about inter-point distances is usually gathered through a set of experiments where subjects are asked to make quantitative (in metric MDS) or qualitative (in non-metric MDS) comparisons of objects. In computational chemistry, they come up in inferring the three-dimensional structure of a molecule (molecular conformation) from information about interatomic distances.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Low-dimensional Euclidean embedding problems", "weight": 1.0} -->

A classical result by Schoenberg states that $D$ is a Euclidean distance matrix of $n$ points in ${\mathbb{R}}^{d}$ if and only if $D_{ii} = 0$, the matrix $VDV$ is negative semidefinite, and ${rank}{({VDV})}$ is less than or equal to $d$. If the matrix $D$ is known exactly, the corresponding configuration of points (up to a unitary transform) is obtained by simply taking a matrix square root of $- {\frac{1}{2}VDV}$. However, in many cases, only a random sampling collection of the distances are available. The problem of finding a valid EDM consistent with the known inter-point distances and with the smallest embedding dimension can be expressed as the rank optimization problem where $\mathcal{A}:{\mathcal{S}^{n}\rightarrow{\mathbb{R}}^{p}}$ is a random sampling operator as discussed in the matrix completion problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Low-dimensional Euclidean embedding problems", "weight": 1.0} -->

This problem involves a Linear Matrix Inequality (LMI) and appears to be more general than the equality constrained rank minimization problem. However, general LMIs can equivalently be expressed as rank constraints on an appropriately defined block matrix. The rank of a block symmetric matrix is equal to the rank of a diagonal block plus the rank of its Schur complement (see, e.g., \[33, §2.2\]). Given a function $f$ that maps matrices into $q \times q$ symmetric matrices, that $f{(X)}$ is positive semidefinite can be equivalently expressed through a rank constraint as That is, if there exists a matrix $B$ satisfying the inequality above, then ${f{(X)}} = {B'B} \succeq 0$. Using this equivalent representation allows us to rewrite (1.1) as an affine rank minimization problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Image Compression", "weight": 1.0} -->

A simple and well-known method to compress two-dimensional images can be obtained by using the singular value decomposition (e.g.,). The basic idea is to associate to the given grayscale image a rectangular matrix $M$, with the entries $M_{ij}$ corresponding to the gray level of the $(i,j)$ pixel. The best rank-$k$ approximation of $M$ is given by where $|| \cdot ||$ is any unitarily invariant norm. By the classical Eckart-Young-Mirsky theorem, the optimal approximant is given by a truncated singular value decomposition of $M$, i.e., if $M = {U\SigmaV^{T}}$, then $X^{\ast} = {U\Sigma_{k}V^{T}}$, where the first $k$ diagonal entries of $\Sigma_{k}$ are the largest $k$ singular values, and the rest of the entries are zero.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Image Compression", "weight": 1.0} -->

If for a given rank $k$, the approximation error $\|{M - X^{\ast}}\|$ is small enough, then the amount of data needed to encode the information about the image is $k{({{m + n} - k})}$ real numbers, which can be much smaller than the $mn$ required to transmit the values of all the entries.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Image Compression", "weight": 1.0} -->

Consider a given image, whose associated matrix $M$ has low-rank, or can be well-approximated by a low-rank matrix. As proposed by Wakin *et al.*, a single-pixel camera would ideally produce measurements that are random linear combinations of all the pixels of the given image. Under this situation, the image reconstruction problem boils down exactly to affine rank minimization, where the constraints are given by the random linear functionals.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Image Compression", "weight": 1.0} -->

It should be remarked that the simple SVD image compression scheme described has certain deficiencies that more sophisticated techniques do not share (in particular, the lack of invariance of the description length under rotations). Nevertheless, due to its simplicity and relatively good practical performance, this method is particularly popular in introductory treatments and numerical linear algebra textbooks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "From Compressed Sensing to Rank Minimization", "weight": 1.0} -->

As discussed above, when the matrix variable is constrained to be diagonal, the affine rank minimization problem (1.1) reduces to the cardinality minimization problem of finding the element in the affine space with the fewest number of nonzero components. In this section we will establish a dictionary between the concepts of rank and cardinality minimization. The main elements of this correspondence are outlined in Table 1. With these elements in place, the existing proofs of sparsity recovery provide a template for the more general case of low-rank recovery.

<!-- chunk {"id": "body-0025", "role": "body", "section": "From Compressed Sensing to Rank Minimization", "weight": 1.0} -->

In establishing our dictionary, we will provide a review of useful facts regarding matrix norms and their characterization as convex optimization problems. We will show how computing both the operator norm and the nuclear norm of a matrix can be cast as semidefinite programming problems. We also establish the suitable optimality conditions for the minimization of the nuclear norm under affine equality constraints, the main convex optimization problem studied in this article. Our discussion of matrix norms will mostly follow the discussion in where extensive lists of references are provided.

<!-- chunk {"id": "body-0026", "role": "body", "section": "From Compressed Sensing to Rank Minimization", "weight": 1.0} -->

Hilbert Space norm sparsity inducing norm orthogonal row and column spaces Table 1: A dictionary relating the concepts of cardinality and rank minimization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Matrix vs. Vector Norms", "weight": 1.0} -->

The three vector norms that play significant roles in the compressed sensing framework are the $\ell_{1}$, $\ell_{2}$, and $\ell_{\infty}$ norms, denoted by ${\| x\|}_{1}$, $\| x\|$ and ${\| x\|}_{\infty}$ respectively. These norms have natural generalizations to matrices, inheriting many appealing properties from the vector case. In particular, there is a parallel duality structure.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Matrix vs. Vector Norms", "weight": 1.0} -->

For a rectangular matrix $X \in {\mathbb{R}}^{m \times n}$, $\sigma_{i}{(X)}$ denotes the $i$-th largest singular value of $X$ and is equal to the square-root of the $i$-th largest eigenvalue of $XX'$. The rank of $X$ will usually be denoted by $r$, and is equal to the number of nonzero singular values. For matrices $X$ and $Y$ of the same dimensions, we define the inner product in ${\mathbb{R}}^{m \times n}$ as ${\langle X,Y\rangle}:={{Tr}{({X'Y})}} = {\sum_{i = 1}^{m}{\sum_{j = 1}^{n}{X_{ij}Y_{ij}}}}$. The norm associated with this inner product is called the Frobenius (or Hilbert-Schmidt) norm $|| \cdot ||_{F}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Matrix vs. Vector Norms", "weight": 1.0} -->

The Frobenius norm is also equal to the Euclidean, or $\ell_{2}$, norm of the vector of singular values, i.e., The operator norm (or induced 2-norm) of a matrix is equal to its largest singular value (i.e., the $\ell_{\infty}$ norm of the singular values): The nuclear norm of a matrix is equal to the sum of its singular values, i.e., and is alternatively known by several other names including the Schatten $1$-norm, the Ky Fan $r$-norm, and the trace class norm. Since the singular values are all positive, the nuclear norm is equal to the $\ell_{1}$ norm of the vector of singular values.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dual norms", "weight": 1.0} -->

For any given norm $\parallel \cdot \parallel$ in an inner product space, there exists a dual norm $\parallel \cdot \parallel_{d}$ defined as Furthermore, the norm dual to the norm $|| \cdot ||_{d}$ is again the original norm $|| \cdot ||$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dual norms", "weight": 1.0} -->

In the case of vector norms in ${\mathbb{R}}^{n}$, it is well-known that the dual norm of the $\ell_{p}$ norm (with $1 < p < \infty$) is the $\ell_{q}$ norm, where ${\frac{1}{p} + \frac{1}{q}} = 1$. This fact is essentially equivalent to Hölder's inequality. Similarly, the dual norm of the $\ell_{\infty}$ norm of a vector is the $\ell_{1}$ norm. These facts also extend to the matrix norms we have defined. For instance, the dual norm of the Frobenius norm is the Frobenius norm. This can be verified by simple calculus (or Cauchy-Schwarz), since is equal to ${\| X\|}_{F}$, with the maximizing $Y$ being equal to $X/{\| X\|}_{F}$. Similarly, as shown below, the dual norm of the operator norm is the nuclear norm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dual norms", "weight": 1.0} -->

The proof of this fact will also allow us to present variational characterizations of each of these norms as semidefinite programs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Convex envelopes of rank and cardinality functions", "weight": 1.0} -->

Let $\mathcal{C}$ be a given convex set. The *convex envelope* of a (possibly nonconvex) function $f:{\mathcal{C}\rightarrow{\mathbb{R}}}$ is defined as the largest convex function $g$ such that ${g{(x)}} \leq {f{(x)}}$ for all $x \in \mathcal{C}$ (see, e.g., ). This means that among all convex functions, $g$ is the best pointwise approximation to $f$. In particular, if the optimal $g$ can be conveniently described, it can serve as an approximation to $f$ that can be minimized efficiently.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Convex envelopes of rank and cardinality functions", "weight": 1.0} -->

By the chain of inequalities in (2.1), we have that ${{rank}{(X)}} \geq {{\| X\|}_{\ast}/{\| X\|}}$ for all $X$. For all matrices with ${\| X\|} \leq 1$, we must have that ${{rank}{(X)}} \geq {\| X\|}_{\ast}$, so the nuclear norm is a convex lower bound of the rank function on the unit ball in the operator norm. In fact, it can be shown that this is the tightest convex lower bound.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Additivity of rank and nuclear norm", "weight": 1.0} -->

A function $f$ mapping a linear space $\mathcal{S}$ to $\mathbb{R}$ is called *subadditive* if ${f{({x + y})}} \leq {{f{(x)}} + {f{(y)}}}$. It is *additive* if ${f{({x + y})}} = {{f{(x)}} + {f{(y)}}}$. In the case of vectors, both the cardinality function and the $\ell_{1}$ norm are subadditive.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Additivity of rank and nuclear norm", "weight": 1.0} -->

That is, if $x$ and $y$ are sparse vectors, then it always holds that the number of non-zeros in $x + y$ is less than or equal to the number of non-zeros in $x$ plus the number of non-zeros of $y$; furthermore (by the triangle inequality) ${\|{x + y}\|}_{1} \leq {{\| x\|}_{1} + {\| y\|}_{1}}$. In particular, the cardinality function is additive exactly when the vectors $x$ and $y$ have disjoint support. In this case, the $\ell_{1}$ norm is also additive, in the sense that ${\|{x + y}\|}_{1} = {{\| x\|}_{1} + {\| y\|}_{1}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Additivity of rank and nuclear norm", "weight": 1.0} -->

For matrices, the rank function is subadditive. For the rank to be additive, it is necessary and sufficient that the row and column spaces of the two matrices intersect only at the origin, since in this case they operate in essentially disjoint spaces (see, e.g., ). As we will show below, a related condition that ensures that the nuclear norm is additive, is that the matrices $A$ and $B$ have row and column spaces that are *orthogonal*. In fact, a compact sufficient condition for the additivity of the nuclear norm will be that ${AB'} = 0$ and ${A'B} = 0$. This is a stronger requirement than the aforementioned condition for rank additivity, as orthogonal subspaces only intersect at the origin. The disparity arises because the nuclear norm of a linear map depends on the choice of the inner products on the spaces ${\mathbb{R}}^{m}$ and ${\mathbb{R}}^{n}$ on which the matrix acts, whereas the rank is independent of such a choice.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

Let us turn now to the study of equality-constrained norm minimization problems where we are searching for a matrix $X \in {\mathbb{R}}^{m \times n}$ of minimum nuclear norm belonging to a given affine subspace. In our applications, the subspace is usually described by linear equations of the form ${\mathcal{A}{(X)}} = b$, where $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ is a linear mapping. This problem admits the primal-dual convex formulation where $\mathcal{A}^{\ast}:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{m \times n}}$ is the adjoint of $\mathcal{A}$. The formulation (2.7) is valid for any norm minimization problem, by replacing the norms appearing above by any dual pair of norms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

In particular, if we replace the nuclear norm with the $\ell_{1}$ norm and the operator norm with the $\ell_{\infty}$ norm, we obtain a primal-dual pair of optimization problems, that can be reformulated in terms of linear programming.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

Using the SDP characterizations of the nuclear and operator norms given in (2.5)-(2.6) above allows us to rewrite (2.7) as the primal-dual pair of semidefinite programs | | s.t. | | $\begin{bmatrix} | $\succeq 0$ | s.t. | ${\begin{bmatrix} | | | | | | | \end{bmatrix}$ | | | \end{bmatrix} \succeq 0}.$ | | |

<!-- chunk {"id": "body-0041", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

In order to describe the optimality conditions for the norm minimization problem (2.7), we must first characterize the subdifferential of the nuclear norm. Recall that for a convex function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, the subdifferential of $f$ at $x \in {\mathbb{R}}^{n}$ is the compact convex set Let $X$ be an $m \times n$ matrix with rank $r$ and let $X = {U\SigmaV'}$ be a singular value decomposition where $U \in {\mathbb{R}}^{m \times r}$, $V \in {\mathbb{R}}^{n \times r}$ and $\Sigma$ is an $r \times r$ diagonal matrix.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

The subdifferential of the nuclear norm at $X$ is then given by (see, e.g.,) For comparison, recall the case of the $\ell_{1}$ norm, where $T$ denotes the support of the $n$-vector $x$, $T^{c}$ is the complement of $T$ in the set $\{ 1,\ldots,n\}$, and The similarity between (2.9) and (2.10) is particularly transparent if we recall the *polar decomposition* of a matrix into a product of orthogonal and positive semidefinite matrices (see, e.g.,). The "angular" component of the matrix $X$ is exactly given by $UV'$. Thus, these subgradients always have the form of an "angle" (or sign), plus possibly a contraction in an orthogonal direction if the norm is not differentiable at the current point.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

We can now write concise optimality conditions for the optimization problem (2.7). A matrix $X$ is optimal for (2.7) if there exists a vector $z \in {\mathbb{R}}^{p}$ such that The first condition in (2.11) requires feasibility of the linear equations, and the second one guarantees that there is no feasible direction of improvement. Indeed, since $\mathcal{A}^{\ast}{(z)}$ is in the subdifferential at $X$, for any $Y$ in the primal feasible set of (2.7) we have where the last step follows from the feasibility of $X$ and $Y$. As we can see, the optimality conditions (2.11) for the nuclear norm minimization problem exactly parallel those of the $\ell_{1}$ optimization case.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

These optimality conditions can be used to check and certify whether a given candidate $X$ is indeed the minimum nuclear norm solution. For this, it is sufficient (and necessary) to find a vector $z \in {\mathbb{R}}^{p}$ in the subdifferential of the norm, i.e., such that the left- and right-singular spaces of $\mathcal{A}^{\ast}{(z)}$ are aligned with those of $X$, and is a contraction in the orthogonal complement.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Restricted Isometry and Recovery of Low-Rank Matrices", "weight": 1.0} -->

Let us now turn to the central problem analyzed in this paper. Let $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ be a linear map and let $X_{0}$ be a matrix of rank $r$. Set $b:={\mathcal{A}{(X_{0})}}$, and define the convex optimization problem In this section, we will characterize specific cases when we can *a priori* guarantee that $X^{\ast} = X_{0}$. The key conditions will be determined by the values of a sequence of parameters $\delta_{r}$ that quantify the behavior of the linear map $\mathcal{A}$ when restricted to the subvariety of matrices of rank $r$. The following definition is the natural generalization of the Restricted Isometry Property from vectors to matrices.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nearly Isometric Families", "weight": 1.0} -->

In this section, we will demonstrate that when we sample linear maps from a class of probability distributions obeying certain tail bounds, then they will obey the Restricted Isometry Property (3.2) as $p$, $m$, and $n$ tend to infinity at appropriate rates. The following definition characterizes this family of random linear transformation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithms for nuclear norm minimization", "weight": 1.0} -->

A variety of methods can be developed for the effective minimization of the nuclear norm over an affine subspace of matrices, and we do not have room for a comprehensive treatment here. Instead, we focus on three methods highlighting the trade-offs between computational speed and guarantees on accuracy of the resulting solution. Directly solving the semidefinite characterization of the nuclear norm problem using primal-dual interior point methods is a numerically efficient method for small problems and can be used to yield accuracy up to floating-point precision.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithms for nuclear norm minimization", "weight": 1.0} -->

Since interior point methods use second order information, the memory requirements for computing descent directions quickly becomes too large as the problem size increases. Moreover, for larger problem sizes it is preferable to use methods that exploit, at least partially, the structure of the problem. This can be done at several levels, either by taking into account further information that may be available about the linear map $\mathcal{A}$ (e.g., the case of partially observed Fourier measurements) or by formulating algorithms that are specific to the nuclear norm problem. For the latter, we show how to apply subgradient methods to minimize the nuclear norm over an affine set. Such first-order methods cannot yield as high numerical precision as interior point methods, but much larger problems can be solved because no second-order information needs to be stored. For even larger problems, we discuss a low-rank semidefinite programming that explicitly works with a factorization of the decision variable. This method can be applied even when the matrix decision variable cannot fit into memory, but convergence guarantees are much less satisfactory than in the other two cases.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Interior Point Methods for Semidefinite programming", "weight": 1.0} -->

For small problems where a high-degree of numerical precision is required, interior point methods for semidefinite programming can be directly applied to solve affine nuclear minimization problems. As we have seen in earlier sections, the nuclear norm minimization problem can be directly posed as a semidefinite programming problem via the standard form primal-dual pair (2.8). As written, the primal problem has one ${({n + m})} \times {({n + m})}$ semidefinite constraint and $p$ affine constraints. Conversely, the dual problem has one ${({n + m})} \times {({n + m})}$ semidefinite constraint and $p$ scalar decision variables. Thus, the total number of decision variables (primal and dual) is equal to $\binom{n + m + 1}{2} + p$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Interior Point Methods for Semidefinite programming", "weight": 1.0} -->

Modern interior point solvers for semidefinite programming generally use primal-dual methods, and compute an update direction for the current solution by solving a suitable Newton system. Depending on the structure of the linear mapping $\mathcal{A}$, this may entail solving a potentially large, dense linear system.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Interior Point Methods for Semidefinite programming", "weight": 1.0} -->

If the matrix dimensions $n$ and $m$ are not too large, then any good interior point SDP solver, such as SeDuMi or SDPT3, will quickly produce accurate solutions. In fact, as we will see in the next section, problems with $n$ and $m$ around $50$ can be solved to machine precision in minutes on a desktop computer to machine precision. However, solving such a primal-dual pair of programs with traditional interior point methods can prove to be quite challenging when the dimensions of the matrix $X$ are much bigger than $100 \times 100$, since in this case the corresponding Newton systems become quite large. In the absence of any specific additional structure, the memory requirements of such dense systems quickly limit the size of problems that can be solved.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Interior Point Methods for Semidefinite programming", "weight": 1.0} -->

Perhaps the most important drawback of the direct SDP approach is that it completely ignores the possibility of efficiently computing the nuclear norm via a singular value decomposition, instead of the less efficient eigenvalue decomposition of a bigger matrix. The method we discuss next will circumvent this obstacle, by directly working with subgradients of the nuclear norm.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

The nuclear norm minimization (3.1) is a linearly constrained nondifferentiable convex problem. There are numerous techniques to approach this kind of problems, depending on the specific nature of the constraints (e.g., dense vs. sparse), and the possibility of using first- or second-order information.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

In this section we describe a simple, easy to implement, subgradient projection approach to the solution of (3.1). This first-order method will proceed by computing a sequence of feasible points $\{ X_{k}\}$, with iterates satisfying the update rule where $\Pi$ is the orthogonal projection onto the affine subspace defined by the linear constraints ${\mathcal{A}{(X)}} = b$, and $s_{k} > 0$ is a stepsize parameter. In other words, the method updates the current iterate $X_{k}$ by taking a step along the direction of a subgradient at the current point and then projecting back onto the feasible set. Alternatively, since $X_{k}$ is feasible, we can rewrite this as where $\Pi_{\mathcal{A}}$ is the orthogonal projection onto the kernel of $\mathcal{A}$. Since the feasible set is an affine subspace, there are several options for the projection $\Pi_{\mathcal{A}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

For small problems, one can precompute it using, for example, a QR decomposition of the matrix representation of $\mathcal{A}$ and store it. Alternatively, one can solve a least squares problem at each step by iterative methods such as conjugate gradients.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

The subgradient-based method described above is extremely simple to implement, since only a subgradient evaluation is required at every step. The computation of the subgradient can be done using the formula given in (2.9) earlier, thus requiring only a singular value decomposition of the current point $X_{k}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

A possible alternative here to the use of the SVD for the subgradient computation is to directly focus on the "angular" factor of the polar decomposition of $X_{k}$, using for instance the Newton-like methods developed by Gander. Specifically, for a given matrix $X_{k}$, the Halley-like iteration converges globally and quadratically to the polar factor of $X$, and thus yields an element of the subdifferential of the nuclear norm. This iteration method (suitable scaled) can be faster than a direct SVD computation, particularly if the singular values of the initial matrix are close to 1. This could be appealing since presumably only a very small number of iterations would be needed to update the polar factor of $X_{k}$, although the nonsmoothness of the subdifferential is bound to cause some additional difficulties.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

Regarding convergence, for general nonsmooth problems, subgradient methods do not guarantee a decrease of the cost function at every iteration, even for arbitrarily small step sizes (see, e.g., \[7, §6.3.1\]), unless the minimum-norm subgradient is used. Instead, convergence is usually shown through the decrease (for small stepsize) of the distance from the iterates $X_{k}$ to any optimal point. There are several possibilities for the choice of stepsize $s_{k}$. The simplest choice that can guarantee convergence is to use a diminishing stepsize with an infinite travel condition (i.e., such that ${\lim_{k\rightarrow\infty}s_{k}} = 0$ and $\sum_{k > 0}s_{k}$ diverging).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Projected subgradient methods", "weight": 1.0} -->

Often times, even the computation of a singular value decomposition or Halley-like iteration can be too computationally expensive. The next section proposes a reduction of the size of the search space to alleviate such demands. We must give up guarantees of convergence for this convenience, but this may be an acceptable trade-off for very large-scale problems.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Low-rank parametrization", "weight": 1.0} -->

We now turn to a method that works with an explicit low-rank factorization of $X$. This algorithm not only requires less storage capacity and computational overhead than the previous methods, but for many problems does not even require one to be able to store the decision variable $X$ in memory. This is the case, for example, in the matrix completion problem where $\mathcal{A}{(X)}$ is a subset of the entries of $X$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Low-rank parametrization", "weight": 1.0} -->

Given observations of the form ${\mathcal{A}{(X)}} = b$ of an $m \times n$ matrix $X$ of rank $r$, a possible search algorithm to find a suitable $X$ would be to find a factorization $X = {LR'}$, where $L$ is an $m \times r$ matrix and $R$ an $n \times r$ matrix, such that the equality constraints are satisfied. Since there are many possible such factorizations, we could search for one where the matrices $L$ and $R$ have Frobenius norm as small as possible, i.e., the solution of the optimization problem Even though the cost function is convex, the constraint is not. Such a problem is a nonconvex quadratic program, and it is not evidently easy to optimize. We show below that the minimization of the nuclear norm subject to equality constraints is in fact equivalent to this rather natural heuristic optimization, as long as $r$ is chosen to be sufficiently larger than the rank of the optimum of the nuclear norm problem.

<!-- chunk {"id": "body-0062", "role": "body", "section": "SDPLR and the method of multipliers", "weight": 1.0} -->

For general semidefinite programming problems, Burer and Monteiro have developed in a nonlinear programming approach that relies on a low-rank factorization of the matrix decision variable. We will adapt this idea to our problem, to provide a first-order Lagrangian minimization algorithm that efficiently finds a local minima of (5.1). As a consequence of the work, it will follow that for values of $r$ larger than the rank of the true optimal solution, the local minima of (5.1) can be transformed into global minima of (2.8) under the identification $W_{1} = {LL'}$, $W_{2} = {RR'}$ and $Y = {LR'}$. We summarize below the details of this approach.

<!-- chunk {"id": "body-0063", "role": "body", "section": "SDPLR and the method of multipliers", "weight": 1.0} -->

The algorithm employed is called the *method of multipliers*, a standard approach for solving equality constrained optimization problems. The method of multipliers works with an augmented Lagrangian for (5.1) where the $y_{i}$ are arbitrarily signed Lagrange multipliers and $\sigma$ is a positive constant. A somewhat similar algorithm was proposed by Rennie et al in in the collaborative filtering. In this work, the authors minimize $\mathcal{L}_{a}$ with $\sigma$ fixed and $y = 0$ to serve as a regularized algorithm for matrix completion. Remarkably, by deterministically varying $\sigma$ and $y$, this method can be adapted into an algorithm for solving linearly constrained nuclear-norm minimization.

<!-- chunk {"id": "body-0064", "role": "body", "section": "SDPLR and the method of multipliers", "weight": 1.0} -->

In the method of multipliers, one alternately minimizes the augmented Lagrangian with respect to the decision variables $L$ and $R$, and then increases the value of the penalty coefficient $\sigma$ and updates $y$. The augmented Lagrangian can be minimized using any local search technique, and the partial derivatives are particularly simple to compute. Let $\hat{y}:={y - {\sigma{({{\mathcal{A}{({LR'})}} - b})}}}$. Then we have To calculate the gradients, we first compute the constraint violations ${\mathcal{A}{({LR'})}} - b$, then form $\hat{y}$, and finally use the above equations to compute the gradients.

<!-- chunk {"id": "body-0065", "role": "body", "section": "SDPLR and the method of multipliers", "weight": 1.0} -->

As the number of iterations tends to infinity, only feasible points will have finite values of $\mathcal{L}_{a}$, and for any feasible point, $\mathcal{L}_{a}{(L,R)}$ is equal to the original cost function ${({{\| L\|}_{F}^{2} + {\| R\|}_{F}^{2}})}/2$. The method terminates when $L$ and $R$ are feasible, as in this case the Lagrangian is stationary and we are at a local minima of (5.1). Including the $y$ multipliers improves the conditioning of each subproblem where $\mathcal{L}_{a}$ is minimized and enhances the rate of convergence. The following theorem shows that when the method of multipliers converges, it converges to a local minimum of (5.1).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To illustrate the scaling of low-rank recovery for a particular matrix $M$, consider the MIT logo presented in Figure 1. The image has a total of $46$ rows and $81$ columns (total 3726 elements), and 3 distinct non-zero numerical values corresponding to the colors white, red, and grey. Since the logo only has $5$ distinct rows, it has rank $5$. For each of the ensembles discussed in Section 4, we sampled measurement matrices with $p$ ranging between $700$ and $1500$, and solved the semidefinite program (2.6) using the freely available software SeDuMi. On a 2.0 GHz Laptop, each semidefinite program could be solved in less than four minutes. We chose to use this interior point method because it yielded the highest accuracy in the shortest amount of time, and we were interested in characterizing precisely when the nuclear norm heuristic succeeded and failed.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To demonstrate the average behavior of low-rank recovery, we conducted a series of experiments for a variety of the matrix sizes $n$, ranks $r$, and numbers of measurements $p$. For a fixed $n$, we constructed random recovery scenarios for low-rank $n \times n$ matrices. For each $n$, we varied $p$ between $0$ and $n^{2}$ where the matrix is completely discovered. For a fixed $n$ and $p$, we generated all possible ranks such that ${r{({{2n} - r})}} \leq p$. This cutoff was chosen because beyond that point there would be an infinite set of matrices of rank $r$ satisfying the $p$ equations.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

For each $(n,p,r)$ triple, we repeated the following procedure $10$ times. A matrix of rank $r$ was generated by choosing two random $n \times r$ factors $Y_{L}$ and $Y_{R}$ with i.i.d. random entries and setting $Y_{0} = {Y_{L}Y_{R}'}$. A matrix $\mathbf{A}$ was sampled from the Gaussian ensemble with $p$ rows and $n^{2}$ columns. Then the nuclear norm minimization was solved using the SDP solver SeDuMi on the formulation (2.6). Again, we chose to use SeDuMi because we wanted to precisely distinguish between success and failure of the heuristic. We declared $Y_{0}$ to be recovered if ${{\|{X - Y_{0}}\|}_{F}/{\| Y_{0}\|}_{F}} < 10^{- 3}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Figure 4 shows the results of these experiments for $n = 30$ and $40$. The color of the cell in the figures reflects the empirical recovery rate of the $10$ runs (scaled between $0$ and $1$). White denotes perfect recovery in all experiments, and black denotes failure for all experiments.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

These experiments demonstrate that the logarithmic factors and constants present in our scaling results are somewhat conservative. For example, as one might expect, low-rank matrices are perfectly recovered by nuclear norm minimization when $p = n^{2}$ as the matrix is uniquely determined. Moreover, as $p$ is reduced slightly away from this value, low-rank matrices are still recovered $100$ percent of the time for most values of $r$. Finally, we note that despite the asymptotic nature of our analysis, our experiments demonstrate excellent performance with low-rank matrices of size $30 \times 30$ and $40 \times 40$ matrices, showing that the heuristic is practical even in low-dimensional settings.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Intriguingly, Figure 4 also demonstrates a "phase transition" between perfect recovery and failure. As observed in several recent papers by Donoho and his collaborators (See e.g. ), the random sparsity recovery problem has two distinct connected regions of parameter space: one where the sparsity pattern is perfectly recovered, and one where no sparse solution is found. Not surprisingly, Figure 4 illustrates an analogous phenomenon in rank recovery. Computing explicit formulas for the transition between perfect recovery and failure is left for future work.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Discussion and future developments", "weight": 1.5} -->

Having illustrated the natural connections between affine rank minimization and affine cardinality minimization, we were able to draw on these parallels to determine scenarios where the nuclear norm heuristic was able to exactly solve the rank minimization problem. These scenarios directly generalized conditions for which the $\ell_{1}$ heuristic succeeded and ensembles of linear maps for which these conditions hold. Furthermore, our experimental results display similar recovery properties to those demonstrated in the empirical studies of $\ell_{1}$ minimization. Inspired by the success of this program, we close this report by briefly discussing several exciting directions that are natural continuations of this work building on more analogies from the compressed sensing literature. We also describe possible extensions to more general notions of parsimony.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Factored measurements and alternative ensembles", "weight": 1.0} -->

All of the measurement ensembles require the storage of $O{({mnp})}$ numbers. For large problems this is wholly impractical. There are many promising alternative measurement ensembles that seem to obey the same scaling laws as those presented in Section 4. For example, "factored" measurements, of the form $A_{i}:{X\mapsto{u_{i}^{T}Xv_{i}}}$, where $u_{i},v_{i}$ are Gaussian random vectors empirically yield the same performance as the Gaussian ensemble. This factored ensemble only requires storage of $O{({{({m + n})}p})}$ numbers, which is a rather significant savings for very large problems. The proof in Section 4 does not seem to extend to this ensemble, thus new machinery must be developed to guarantee properties about such low-rank measurements.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Noisy Measurements and Low-rank approximation", "weight": 1.0} -->

Our results in this paper address only the case of exact (noiseless) measurements. It is of natural interest to understand the behavior of the nuclear norm heuristic in the case of noisy data. Based on the existing results for the sparse case (e.g., ), it would be natural to expect similar stability properties of the recovered solution, for instance in terms of the $\ell_{2}$ norm of the computed solution. Such an analysis could also be used to study the nuclear norm heuristic as an approximation technique where a matrix has rapidly decaying singular values and a low-rank approximation is desired.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Incoherent Ensembles and Partially Observed Transforms", "weight": 1.0} -->

Again, taking our lead from the compressed sensing literature, it would be of great interest to extend the results of to low-rank recovery. In this work, the authors show that partially observed unitary transformations of sparse vectors can be used to recover the sparse vector using $\ell_{1}$ minimization. There are many practical applications where low-rank processes are partially observed. For instance, the matrix completion problem can be thought of as partial observations under the identity transformations. As another example, there are many examples in two-dimensional Fourier spectroscopy where only partial information can be observed due to experimental constraints.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Alternative numerical methods", "weight": 1.0} -->

Besides the techniques described in Section 5, there are a number of interesting additional possibilities to solve the nuclear norm minimization problem. An appealing suggestion is to combine the strength of second-order methods (as in the SDP approach) with the known geometry of the nuclear norm (as in the subgradient approach), and develop a customized interior point method, possibly yielding faster convergence rates, while still being relatively memory-efficient.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Alternative numerical methods", "weight": 1.0} -->

It is also of much interest to investigate the possible adaptation of some of the successful path-following approaches in traditional $\ell_{1}$/cardinality minimization, such as the Homotopy or LARS (least angle regression). This may be not be completely straightforward, since the efficiency of many of these methods often relies explicitly on the polyhedral structure of the feasible set of the $\ell_{1}$ norm problem.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Geometric interpretations", "weight": 1.0} -->

For the case of cardinality/$\ell_{1}$ minimization, a beautiful geometric interpretation has been set forth by Donoho and Tanner. Key to their results is the notion of *central $k$-neighborliness* of a centrosymmetric polytope, namely the property that every subset of $k + 1$ vertices not including an antipodal pair spans a $k$-face. In particular, they show that the $\ell_{1}$ heuristic always succeeds whenever the image of the $\ell_{1}$ unit ball (the cross-polytope) under the linear mapping $\mathcal{A}$ is a centrally $k$-neighborly polytope.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Geometric interpretations", "weight": 1.0} -->

In the case of rank minimization, the direct application of these concepts fails, since the unit ball of the nuclear norm is not a polyhedral set. Nevertheless, it seems likely that a similar explanation could be developed, where the key feature would be the preservation under a linear map of the extremality of the components of the boundary of the nuclear norm unit ball defined by low-rank conditions.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Jordan algebras", "weight": 1.0} -->

As we have seen, our results for the rank minimization problem closely parallel the earlier developments in cardinality minimization. A convenient mathematical framework that allows the simultaneous consideration of these cases as well as a few new ones, is that of *Jordan algebras* and the related symmetric cones. In the Jordan-algebraic setting, there is an intrinsic notion of rank that agrees with the cardinality of the support in the case of the nonnegative orthant or the rank of a matrix in the case of the positive semidefinite cone. Besides mathematical elegance, a direct Jordan-algebraic approach would transparently yield similar results for the case of second-order (or Lorentz) cone constraints.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Jordan algebras", "weight": 1.0} -->

As specific examples of the power and elegance of this approach, we mention the work of Faybusovich and Schmieta and Alizadeh that provide a unified development of interior point methods for symmetric cones, as well as Faybusovich's work on convexity theorems for quadratic mappings.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Parsimonious models and optimization", "weight": 1.0} -->

Sparsity and low-rank are two specific classes of parsimonious (or low-complexity) descriptions. Are there other kinds of easy-to-describe parametric models that are amenable to exact solutions via convex optimizations techniques? Given the intimate connections between linear and semidefinite programming and the Jordan algebraic approaches described earlier, it is likely that this will require alternative tractable convex optimization formulations.
