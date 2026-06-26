<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Convex Geometry of Linear Inverse Problems

Topics include Linear inverse problems, Atomic norms, Convex geometry, Low-dimensional models, Sparse recovery, Low-rank recovery.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a convex-geometric framework for linear inverse problems in which model simplicity is encoded by atomic norms and tangent cones. The paper unifies sparse, low-rank, and other structured recovery results under one geometric recovery theory.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In applications throughout science and engineering one is often faced with the challenge of solving an ill-posed inverse problem, where the number of available measurements is smaller than the dimension of the model to be estimated. However in many practical situations of interest, models are constrained structurally so that they only have a few degrees of freedom relative to their ambient dimension. This paper provides a general framework to convert notions of simplicity into convex penalty functions, resulting in convex optimization solutions to linear, underdetermined inverse problems. The class of simple models considered are those formed as the sum of a few atoms from some (possibly infinite) elementary atomic set; examples include well-studied cases such as sparse vectors and low-rank matrices, as well as several others including sums of a few permutations matrices, low-rank tensors, orthogonal matrices, and atomic measures. The convex programming formulation is based on minimizing the norm induced by the convex hull of the atomic set; this norm is referred to as the atomic norm. The facial structure of the atomic norm ball carries a number of favorable properties that are useful for recovering simple models, and an analysis of the underlying convex geometry provides sharp estimates of the number of generic measurements required for exact and robust recovery of models from partial information.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These estimates are based on computing the Gaussian widths of tangent cones to the atomic norm ball. When the atomic set has algebraic structure the resulting optimization problems can be solved or approximated via semidefinite programming. The quality of these approximations affects the number of measurements required for recovery. Thus this work extends the catalog of simple models that can be recovered from limited linear information via tractable convex programming.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deducing the state or structure of a system from partial, noisy measurements is a fundamental task throughout the sciences and engineering. A commonly encountered difficulty that arises in such inverse problems is the limited availability of data relative to the ambient dimension of the signal to be estimated. However many interesting signals or models in practice contain few degrees of freedom relative to their ambient dimension. For instance a small number of genes may constitute a signature for disease, very few parameters may be required to specify the correlation structure in a time series, or a sparse collection of geometric constraints might completely specify a molecular configuration. Such low-dimensional structure plays an important role in making inverse problems well-posed. In this paper we propose a unified approach to transform notions of simplicity into convex penalty functions, thus obtaining convex optimization formulations for inverse problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We describe a model as simple if it can be written as a nonnegative combination of a few elements from an atomic set. Concretely let $\mathbf{x} \in {\mathbb{R}}^{p}$ be formed as follows: where $\mathcal{A}$ is a set of atoms that constitute simple building blocks of general signals. Here we assume that $\mathbf{x}$ is *simple* so that $k$ is relatively small. For example $\mathcal{A}$ could be the finite set of unit-norm one-sparse vectors in which case $\mathbf{x}$ is a sparse vector, or $\mathcal{A}$ could be the infinite set of unit-norm rank-one matrices in which case $\mathbf{x}$ is a low-rank matrix. These two cases arise in many applications, and have received a tremendous amount of attention recently as several authors have shown that sparse vectors and low-rank matrices can be recovered from highly incomplete information. However a number of other structured mathematical objects also fit the notion of simplicity described.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The set $\mathcal{A}$ could be the collection of unit-norm rank-one tensors, in which case $\mathbf{x}$ is a low-rank tensor and we are faced with the familiar challenge of low-rank tensor decomposition. Such problems arise in numerous applications in computer vision and image processing, and in neuroscience. Alternatively $\mathcal{A}$ could be the set of permutation matrices; sums of a few permutation matrices are objects of interest in ranking and multi-object tracking. As yet another example, $\mathcal{A}$ could consist of measures supported at a single point so that $\mathbf{x}$ is an atomic measure supported at just a few points. This notion of simplicity arises in problems in system identification and statistics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In each of these examples as well as several others, a fundamental problem of interest is to recover $\mathbf{x}$ given limited *linear* measurements. For instance the question of recovering a sparse function over the group of permutations (i.e., the sum of a few permutation matrices) given linear measurements in the form of partial Fourier information was investigated in the context of ranked election problems. Similar linear inverse problems arise with atomic measures in system identification, with orthogonal matrices in machine learning, and with simple models formed from several other atomic sets (see Section 2.2 for more examples). Hence we seek tractable computational tools to solve such problems. When $\mathcal{A}$ is the collection of one-sparse vectors, a method of choice is to use the $\ell_{1}$ norm to induce sparse solutions. This method has seen a surge in interest in the last few years as it provides a tractable convex optimization formulation to exactly recover sparse vectors under various conditions. More recently the nuclear norm has been proposed as an effective convex surrogate for solving rank minimization problems subject to various affine constraints.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the success of these methods we propose a general convex optimization framework in Section 2 in order to recover objects with structure of the form from limited linear measurements. The guiding question behind our framework is: how do we take a concept of simplicity such as sparsity and derive the $\ell_{1}$ norm as a convex heuristic? In other words what is the natural procedure to go from the set of one-sparse vectors $\mathcal{A}$ to the $\ell_{1}$ norm? We observe that the convex hull of (unit-Euclidean-norm) one-sparse vectors is the unit ball of the $\ell_{1}$ norm, or the cross-polytope. Similarly the convex hull of the (unit-Euclidean-norm) rank-one matrices is the nuclear norm ball; see Figure 1 for illustrations. These constructions suggest a natural generalization to other settings. Under suitable conditions the convex hull ${conv}{(\mathcal{A})}$ defines the unit ball of a norm, which is called the *atomic norm* induced by the atomic set $\mathcal{A}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We can then minimize the atomic norm subject to measurement constraints, which results in a convex programming heuristic for recovering simple models given linear measurements. As an example suppose we wish to recover the sum of a few permutation matrices given linear measurements. The convex hull of the set of permutation matrices is the *Birkhoff polytope* of doubly stochastic matrices, and our proposal is to solve a convex program that minimizes the norm induced by this polytope. Similarly if we wish to recover an orthogonal matrix from linear measurements we would solve a *spectral norm* minimization problem, as the spectral norm ball is the convex hull of all orthogonal matrices. As discussed in Section 2.5 the atomic norm minimization problem is, in some sense, the best convex heuristic for recovering simple models with respect to a given atomic set.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We give general conditions for exact and robust recovery using the atomic norm heuristic. In Section 3 we provide concrete bounds on the number of generic linear measurements required for the atomic norm heuristic to succeed. This analysis is based on computing certain *Gaussian widths* of tangent cones with respect to the unit balls of the atomic norm. Arguments based on Gaussian width have been fruitfully applied to obtain bounds on the number of Gaussian measurements for the special case of recovering sparse vectors via $\ell_{1}$ norm minimization, but computing Gaussian widths of general cones is not easy. Therefore it is important to exploit the special structure in atomic norms, while still obtaining sufficiently general results that are broadly applicable. An important theme in this paper is the connection between Gaussian widths and various notions of *symmetry*. Specifically by exploiting symmetry structure in certain atomic norms as well as convex duality properties, we give bounds on the number of measurements required for recovery using very general atomic norm heuristics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example we provide precise estimates of the number of generic measurements required for exact recovery of an orthogonal matrix via spectral norm minimization, and the number of generic measurements required for exact recovery of a permutation matrix by minimizing the norm induced by the Birkhoff polytope. While these results correspond to the recovery of individual atoms from random measurements, our techniques are more generally applicable to the recovery of models formed as sums of a few atoms as well. We also give tighter bounds than those previously obtained on the number of measurements required to robustly recover sparse vectors and low-rank matrices via $\ell_{1}$ norm and nuclear norm minimization. In all of the cases we investigate, we find that the number of measurements required to reconstruct an object is proportional to its intrinsic dimension rather than the ambient dimension, thus confirming prior folklore. See Table 1 for a summary of these results.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Gaussian measurements", "weight": 1.0} -->

norm induced by Birkhoff polytope Table 1: A summary of the recovery bounds obtained using Gaussian width arguments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Gaussian measurements", "weight": 1.0} -->

Although our conditions for recovery and bounds on the number of measurements hold generally, we note that it may not be possible to obtain a computable representation for the convex hull ${conv}{(\mathcal{A})}$ of an arbitrary set of atoms $\mathcal{A}$. This leads us to another important theme of this paper, which we discuss in Section 4, on the connection between algebraic structure in $\mathcal{A}$ and the semidefinite representability of the convex hull ${conv}{(\mathcal{A})}$. In particular when $\mathcal{A}$ is an algebraic variety the convex hull ${conv}{(\mathcal{A})}$ can be approximated as (the projection of) a set defined by linear matrix inequalities. Thus the resulting atomic norm minimization heuristic can be solved via semidefinite programming.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gaussian measurements", "weight": 1.0} -->

A second issue that arises in practice is that even with algebraic structure in $\mathcal{A}$ the semidefinite representation of ${conv}{(\mathcal{A})}$ may not be computable in polynomial time, which makes the atomic norm minimization problem intractable to solve. A prominent example here is the tensor nuclear norm ball, obtained by taking the convex hull of the rank-one tensors. In order to address this problem we give a hierarchy of semidefinite relaxations using *theta bodies* that approximate the original (intractable) atomic norm minimization problem. We also highlight that while these semidefinite relaxations are more tractable to solve, we require more measurements for exact recovery of the underlying model than if we solve the original intractable atomic norm minimization problem. Hence there is a tradeoff between the complexity of the recovery algorithm and the number of measurements required for recovery. We illustrate this tradeoff with the cut polytope and its relaxations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gaussian measurements", "weight": 1.0} -->

Outline Section 2 describes the construction of the atomic norm, gives several examples of applications in which these norms may be useful to recover simple models, and provides general conditions for recovery by minimizing the atomic norm. In Section 3 we investigate the number of generic measurements for exact or robust recovery using atomic norm minimization, and give estimates in a number of settings by analyzing the Gaussian width of certain tangent cones. We address the problem of semidefinite representability and tractable relaxations of the atomic norm in Section 4. Section 5 describes some algorithmic issues as well as a few simulation results, and we conclude with a discussion and open questions in Section 6.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Atomic Norms and Convex Geometry", "weight": 1.0} -->

In this section we describe the construction of an atomic norm from a collection of simple atoms. In addition we give several examples of atomic norms, and discuss their properties in the context of solving ill-posed linear inverse problems. We denote the Euclidean norm by $\parallel \cdot \parallel$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Examples", "weight": 1.0} -->

Next we provide several examples of atomic norms that can be viewed as special cases of the construction above. These norms are obtained by convexifying atomic sets that are of interest in various applications.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Examples", "weight": 1.0} -->

Sparse vectors. The problem of recovering sparse vectors from limited measurements has received a great deal of attention, with applications in many problem domains. In this case the atomic set $\mathcal{A} \subset {\mathbb{R}}^{p}$ can be viewed as the set of unit-norm one-sparse vectors ${\{{\pm \mathbf{e}_{i}}\}}_{i = 1}^{p}$, and $k$-sparse vectors in ${\mathbb{R}}^{p}$ can be constructed using a linear combination of $k$ elements of the atomic set. In this case it is easily seen that the convex hull ${conv}{(\mathcal{A})}$ is given by the *cross-polytope* (i.e., the unit ball of the $\ell_{1}$ norm), and the atomic norm $\parallel \cdot \parallel_{\mathcal{A}}$ corresponds to the $\ell_{1}$ norm in ${\mathbb{R}}^{p}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Examples", "weight": 1.0} -->

Low-rank matrices. Recovering low-rank matrices from limited information is also a problem that has received considerable attention as it finds applications in problems in statistics, control, and machine learning. The atomic set $\mathcal{A}$ here can be viewed as the set of rank-one matrices of unit-Euclidean-norm. The convex hull ${conv}{(\mathcal{A})}$ is the *nuclear norm ball* of matrices in which the sum of the singular values is less than or equal to one.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Examples", "weight": 1.0} -->

Sparse and low-rank matrices. The problem of recovering a sparse matrix and a low-rank matrix given information about their sum arises in a number of model selection and system identification settings. The corresponding atomic norm is constructed by taking the convex hull of an atomic set obtained via the union of rank-one matrices and (suitably scaled) one-sparse matrices. This norm can also be viewed as the *infimal convolution* of the $\ell_{1}$ norm and the nuclear norm, and its properties have been explored.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Examples", "weight": 1.0} -->

Permutation matrices. A problem of interest in a ranking context or an object tracking context is that of recovering permutation matrices from partial information. Suppose that a small number $k$ of rankings of $m$ candidates is preferred by a population. Such preferences can be modeled as the sum of a few $m \times m$ permutation matrices, with each permutation corresponding to a particular ranking. By conducting surveys of the population one can obtain partial linear information of these preferred rankings. The set $\mathcal{A}$ here is the collection of permutation matrices (consisting of $m!$ elements), and the convex hull ${conv}{(\mathcal{A})}$ is the *Birkhoff polytope* or the set of doubly stochastic matrices. The centroid of the Birkhoff polytope is the matrix $\mathbf{1}\mathbf{1}^{T}/m$, so it needs to be recentered appropriately.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Examples", "weight": 1.0} -->

We mention here recent work by Jagabathula and Shah on recovering a sparse function over the symmetric group (i.e., the sum of a few permutation matrices) given partial Fourier information; although the algorithm proposed in is tractable it is not based on convex optimization.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Examples", "weight": 1.0} -->

Binary vectors. In integer programming one is often interested in recovering vectors in which the entries take on values of $\pm 1$. Suppose that there exists such a sign-vector, and we wish to recover this vector given linear measurements. This corresponds to a version of the multi-knapsack problem. In this case $\mathcal{A}$ is the set of all sign-vectors, and the convex hull ${conv}{(\mathcal{A})}$ is the *hypercube* or the unit ball of the $\ell_{\infty}$ norm. The image of this hypercube under a linear map is also referred to as a zonotope.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Examples", "weight": 1.0} -->

Vectors from lists. Suppose there is an unknown vector $\mathbf{x} \in {\mathbb{R}}^{p}$, and that we are given the entries of this vector without any information about the locations of these entries. For example if $\mathbf{x} = {\lbrack{31224}\rbrack}'$, then we are only given the list of numbers $\{ 1,2,2,3,4\}$ without their positions in $\mathbf{x}$. Further suppose that we have access to a few linear measurements of $\mathbf{x}$. Can we recover $\mathbf{x}$ by solving a convex program? Such a problem is of interest in recovering partial rankings of elements of a set. An extreme case is one in which we only have two preferences for rankings, i.e., a vector in ${\{ 1,2\}}^{p}$ composed only of one's and two's, which reduces to a special case of the problem above of recovering binary vectors (in which the number of entries of each sign is fixed).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Examples", "weight": 1.0} -->

For this problem the set $\mathcal{A}$ is the set of all permutations of $\mathbf{x}$ (which we know since we have the list of numbers that compose $\mathbf{x}$), and the convex hull ${conv}{(\mathcal{A})}$ is the *permutahedron*. As with the Birkhoff polytope, the permutahedron also needs to be recentered about the point ${\mathbf{1}^{T}\mathbf{x}}/p$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Examples", "weight": 1.0} -->

Matrices constrained by eigenvalues. This problem is in a sense the non-commutative analog of the one above. Suppose that we are given the eigenvalues $\lambda$ of a symmetric matrix, but no information about the eigenvectors. Can we recover such a matrix given some additional linear measurements? In this case the set $\mathcal{A}$ is the set of all symmetric matrices with eigenvalues $\lambda$, and the convex hull ${conv}{(\mathcal{A})}$ is given by the *Schur-Horn orbitope*.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Examples", "weight": 1.0} -->

Orthogonal matrices. In many applications matrix variables are constrained to be orthogonal, which is a non-convex constraint and may lead to computational difficulties. We consider one such simple setting in which we wish to recover an orthogonal matrix given limited information in the form of linear measurements. In this example the set $\mathcal{A}$ is the set of $m \times m$ orthogonal matrices, and ${conv}{(\mathcal{A})}$ is the *spectral norm ball*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Examples", "weight": 1.0} -->

Measures. Recovering a measure given its moments is another question of interest that arises in system identification and statistics. Suppose one is given access to a linear combination of moments of an atomically supported measure. How can we reconstruct the support of the measure? The set $\mathcal{A}$ here is the moment curve, and its convex hull ${conv}{(\mathcal{A})}$ goes by several names including the *Caratheodory orbitope*. Discretized versions of this problem correspond to the set $\mathcal{A}$ being a finite number of points on the moment curve; the convex hull ${conv}{(\mathcal{A})}$ is then a *cyclic polytope*.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Examples", "weight": 1.0} -->

Cut matrices. In some problems one may wish to recover low-rank matrices in which the entries are constrained to take on values of $\pm 1$. Such matrices can be used to model basic user preferences, and are of interest in problems such as collaborative filtering. The set of atoms $\mathcal{A}$ could be the set of rank-one signed matrices, i.e., matrices of the form ${\mathbf{z}\mathbf{z}}^{T}$ with the entries of $\mathbf{z}$ being $\pm 1$. The convex hull ${conv}{(\mathcal{A})}$ of such matrices is the *cut polytope*. An interesting issue that arises here is that the cut polytope is in general intractable to characterize. However there exist several well-known tractable semidefinite relaxations to this polytope, and one can employ these in constructing efficient convex programs for recovering cut matrices. We discuss this point in greater detail in Section 4.3.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Examples", "weight": 1.0} -->

Low-rank tensors. Low-rank tensor decompositions play an important role in numerous applications throughout signal processing and machine learning. Developing computational tools to recover low-rank tensors is therefore of great interest. In principle we could solve a tensor nuclear norm minimization problem, in which the tensor nuclear norm ball is obtained by taking the convex hull of rank-one tensors. A computational challenge here is that the tensor nuclear norm is in general intractable to compute; in order to address this problem we discuss further convex relaxations to the tensor nuclear norm using theta bodies in Section 4. A number of additional technical issues also arise with low-rank tensors including the non-existence in general of a singular value decomposition analogous to that for matrices, and the difference between the rank of a tensor and its border rank.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Examples", "weight": 1.0} -->

Nonorthogonal factor analysis. Suppose that a data matrix admits a factorization $X = {AB}$. The matrix nuclear norm heuristic will find a factorization into *orthogonal* factors in which the columns of $A$ and rows of $B$ are mutually orthogonal. However if *a priori* information is available about the factors, precision and recall could be improved by enforcing such priors. These priors may sacrifice orthogonality, but the factors might better conform with assumptions about how the data are generated. For instance in some applications one might know in advance that the factors should only take on a discrete set of values. In this case, we might try to fit a sum of rank-one matrices that are bounded in $\ell_{\infty}$ norm rather than in $\ell_{2}$ norm. Another prior that commonly arises in practice is that the factors are non-negative (i.e., in non-negative matrix factorization). These and other priors on the basic rank-one summands induce different norms on low-rank models than the standard nuclear norm, and may be better suited to specific applications.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Recovery Condition", "weight": 1.0} -->

The following result gives a characterization of the favorable underlying geometry required for exact recovery. Let ${null}{(\Phi)}$ denote the nullspace of the operator $\Phi$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Why Atomic Norm?", "weight": 1.0} -->

The atomic norm induced by a set $\mathcal{A}$ possesses a number of favorable properties that are useful for recovering "simple" models from limited linear measurements. The key point to note from Section 2.4 is that the smaller the tangent cone at a point $\mathbf{x}^{\star}$ with respect to ${conv}{(\mathcal{A})}$, the easier it is to satisfy the empty-intersection condition of Proposition 2.1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Why Atomic Norm?", "weight": 1.0} -->

Based on this observation it is desirable that points in ${conv}{(\mathcal{A})}$ with smaller tangent cones correspond to simpler models, while points in ${conv}{(\mathcal{A})}$ with larger tangent cones generally correspond to more complicated models. The construction of ${conv}{(\mathcal{A})}$ by taking the convex hull of $\mathcal{A}$ ensures that this is the case. The extreme points of ${conv}{(\mathcal{A})}$ correspond to the simplest models, i.e., those models formed from a single element of $\mathcal{A}$. Further the low-dimensional faces of ${conv}{(\mathcal{A})}$ consist of those elements that are obtained by taking linear combinations of a few basic atoms from $\mathcal{A}$. These are precisely the properties desired as points lying in these low-dimensional faces of ${conv}{(\mathcal{A})}$ have smaller tangent cones than those lying on larger faces.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Why Atomic Norm?", "weight": 1.0} -->

We also note that the atomic norm is, in some sense, the best possible convex heuristic for recovering simple models. Any reasonable heuristic penalty function should be constant on the set of atoms $\mathcal{A}$. This ensures that no atom is preferred over any other. Under this assumption, we must have that for any $\mathbf{a} \in \mathcal{A}$, $\mathbf{a}' - \mathbf{a}$ must be a descent direction for all $\mathbf{a}' \in \mathcal{A}$. The best convex penalty function is one in which the cones of descent directions at $\mathbf{a} \in \mathcal{A}$ are as small as possible. This is because, as described above, smaller cones are more likely to satisfy the empty intersection condition required for exact recovery.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Why Atomic Norm?", "weight": 1.0} -->

Since the tangent cone at $\mathbf{a} \in \mathcal{A}$ with respect to ${conv}{(\mathcal{A})}$ is precisely the conic hull of $\mathbf{a}' - \mathbf{a}$ for $\mathbf{a}' \in \mathcal{A}$, the atomic norm is the best convex heuristic for recovering models where simplicity is dictated by the set $\mathcal{A}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Why Atomic Norm?", "weight": 1.0} -->

Our reasons for proposing the atomic norm as a useful convex heuristic are quite different from previous justifications of the $\ell_{1}$ norm and the nuclear norm. In particular let $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}}$ denote the cardinality function that counts the number of nonzero entries of a vector. Then the $\ell_{1}$ norm is the *convex envelope* of $f$ restricted to the unit ball of the $\ell_{\infty}$ norm, i.e., the best convex underestimator of $f$ restricted to vectors in the $\ell_{\infty}$-norm ball. This view of the $\ell_{1}$ norm in relation to the function $f$ is often given as a justification for its effectiveness in recovering sparse vectors. However if we consider the convex envelope of $f$ restricted to the Euclidean norm ball, then we obtain a very different convex function than the $\ell_{1}$ norm!

<!-- chunk {"id": "body-0039", "role": "body", "section": "Why Atomic Norm?", "weight": 1.0} -->

With more general atomic sets, it may not be clear *a priori* what the bounding set should be in deriving the convex envelope. In contrast the viewpoint adopted in this paper leads to a natural, unambiguous construction of the $\ell_{1}$ norm and other general atomic norms. Further as explained above it is the favorable *facial structure* of the atomic norm ball that makes the atomic norm a suitable convex heuristic to recover simple models, and this connection is transparent in the definition of the atomic norm.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Recovery from Generic Measurements", "weight": 1.0} -->

We consider the question of using the convex program to recover "simple" models formed according to from a *generic* measurement operator or map $\Phi:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{n}}$. Specifically, we wish to compute estimates on the number of measurements $n$ so that we have exact recovery using for *most* operators comprising of $n$ measurements. That is, the measure of $n$-measurement operators for which recovery fails using must be exponentially small. In order to conduct such an analysis we study random *Gaussian* maps whose entries are independent and identically distributed Gaussians. These measurement operators have a nullspace that is uniformly distributed among the set of all $({p - n})$-dimensional subspaces in ${\mathbb{R}}^{p}$. In particular we analyze when such operators satisfy the conditions of Proposition 2.1 and Proposition 2.2 for exact recovery.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Recovery Conditions based on Gaussian Width", "weight": 1.0} -->

Proposition 2.1 requires that the nullspace of the measurement operator $\Phi$ must miss the tangent cone $T_{\mathcal{A}}{(\mathbf{x}^{\star})}$. Gordon gave a solution to the problem of characterizing the probability that a random subspace (of some fixed dimension) distributed uniformly misses a cone. We begin by defining the Gaussian width of a set, which plays a key role in Gordon's analysis.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Properties of Gaussian Width", "weight": 1.0} -->

The Gaussian width has deep connections to convex geometry. Since the length and direction of a Gaussian random vector are independent, one can verify that for $S \subset {\mathbb{R}}^{p}$ where the integral is with respect to Haar measure on ${\mathbb{S}}^{p - 1}$ and $b{(S)}$ is known as the *mean width* of $S$. The mean width measures the average length of $S$ along unit directions in ${\mathbb{R}}^{p}$ and is one of the fundamental *intrinsic volumes* of a body studied in combinatorial geometry. Any continuous valuation that is invariant under rigid motions and homogeneous of degree 1 is a multiple of the mean width and hence a multiple of the Gaussian width. We can use this connection with convex geometry to underscore several properties of the Gaussian width that are useful for computation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Properties of Gaussian Width", "weight": 1.0} -->

The Gaussian width of a body is invariant under translations and unitary transformations. Moreover, it is homogeneous in the sense that $w{({tK})}$ = $tw{(K)}$ for $t > 0$. The width is also monotonic. If $S_{1} \subseteq S_{2} \subseteq {\mathbb{R}}^{p}$, then it is clear from the definition of the Gaussian width that Less obvious, the width is modular in the sense that if $S_{1}$ and $S_{2}$ are convex bodies with $S_{1} \cup S_{2}$ convex, we also have This equality follows from the fact that $w$ is a valuation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Properties of Gaussian Width", "weight": 1.0} -->

Also note that if we have a set $S \subseteq {\mathbb{R}}^{p}$, then the Gaussian width of $S$ is equal to the Gaussian width of the convex hull of $S$: This result follows from the basic fact in convex analysis that the maximum of a convex function over a convex set is achieved at an extreme point of the convex set.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Properties of Gaussian Width", "weight": 1.0} -->

If $V \subset {\mathbb{R}}^{p}$ is a subspace in ${\mathbb{R}}^{p}$, then we have that which follows from standard results on random Gaussians. This result also agrees with the intuition that a random Gaussian map $\Phi$ misses a $k$-dimensional subspace with high probability as long as ${\dim{({{null}{(\Phi)}})}} \geq {k + 1}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Properties of Gaussian Width", "weight": 1.0} -->

Finally, if a cone $S \subset {\mathbb{R}}^{p}$ is such that $S = {S_{1} \oplus S_{2}}$, where $S_{1} \subset {\mathbb{R}}^{p}$ is a $k$-dimensional cone, $S_{2} \subset {\mathbb{R}}^{p}$ is a $({p - k})$-dimensional cone that is orthogonal to $S_{1}$, and $\oplus$ denotes the direct sum operation, then the width can be decomposed as follows: These observations are useful in a variety of situations. For example a width computation that frequently arises is one in which $S = {S_{1} \oplus S_{2}}$ as described above, with $S_{1}$ being a $k$-dimensional subspace.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Properties of Gaussian Width", "weight": 1.0} -->

It follows that the width of $S \cap {\mathbb{S}}^{p - 1}$ is bounded as Another tool for computing Gaussian widths is based on Dudley's inequality, which bounds the width of a set in terms of the covering number of the set at all scales.

<!-- chunk {"id": "body-0048", "role": "body", "section": "New Results on Gaussian Width", "weight": 1.0} -->

We now present a framework for computing Gaussian widths by bounding the Gaussian width of a cone via the distance to the dual cone. To be fully general let $\mathcal{C}$ be a non-empty convex cone in ${\mathbb{R}}^{p}$, and let $\mathcal{C}^{\ast}$ denote the polar of $\mathcal{C}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "New Recovery Bounds", "weight": 1.0} -->

We use the bounds derived in the last section to obtain new recovery results. First using the dual characterization of the Gaussian width in Proposition 3.6, we are able to obtain sharp bounds on the number of measurements required for recovering sparse vectors and low-rank matrices from random Gaussian measurements using convex optimization (i.e., $\ell_{1}$-norm and nuclear norm minimization).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Representability and Algebraic Geometry of Atomic Norms", "weight": 1.0} -->

All of our discussion thus far has focussed on arbitrary atomic sets $\mathcal{A}$. As seen in Section 2 the geometry of the convex hull ${conv}{(\mathcal{A})}$ completely determines conditions under which exact recovery is possible using the convex program. In this section we address the question of computing atomic norms for general sets of atoms. These issues are critical in order to be able to solve the convex optimization problem. Although the convex hull ${conv}{(\mathcal{A})}$ is always a mathematically well-defined object, testing membership in this set is in general undecidable (for example, if $\mathcal{A}$ is a fractal). Further, even if these convex hulls are computable they may not admit efficient representations. For example if $\mathcal{A}$ is the set of rank-one signed matrices (see Section 2.2), the corresponding convex hull ${conv}{(\mathcal{A})}$ is the cut polytope for which there is no known tractable characterization.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Representability and Algebraic Geometry of Atomic Norms", "weight": 1.0} -->

Consequently, one may have to resort to efficiently computable approximations of ${conv}{(\mathcal{A})}$. The tradeoff in using such approximations in our atomic norm minimization framework is that we require more measurements for robust recovery. This section is devoted to providing a better understanding of these issues.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Role of Algebraic Structure", "weight": 1.0} -->

In order to obtain exact or approximate representations (analogous to the cases of the $\ell_{1}$ norm and the nuclear norm) it is important to identify properties of the atomic set $\mathcal{A}$ that can be exploited computationally. We focus on cases in which the set $\mathcal{A}$ has algebraic structure. Specifically let the ring of multivariate polynomials in $p$ variables be denoted by ${{\mathbb{R}}{\lbrack\mathbf{x}\rbrack}} = {{\mathbb{R}}{\lbrack\mathbf{x}_{1},\ldots,\mathbf{x}_{p}\rbrack}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Semidefinite Relaxations using Theta Bodies", "weight": 1.0} -->

In this section we give a family of semidefinite relaxations to the atomic norm minimization problem whenever the atomic set has algebraic structure. To begin with if we approximate the atomic norm $\parallel \cdot \parallel_{\mathcal{A}}$ by another atomic norm $\parallel \cdot \parallel_{\overset{\sim}{\mathcal{A}}}$ defined using a *larger* collection of atoms $\mathcal{A} \subseteq \overset{\sim}{\mathcal{A}}$, it is clear that Consequently outer approximations of the atomic set give rise to approximate norms that provide lower bounds on the optimal value of the problem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Semidefinite Relaxations using Theta Bodies", "weight": 1.0} -->

In order to provide such lower bounds on the optimal value of, we discuss semidefinite relaxations of the convex hull ${conv}{(\mathcal{A})}$. All our discussion here is based on results described in for semidefinite relaxations of convex hulls of algebraic varieties using theta bodies. We only give a brief review of the relevant constructions, and refer the reader to the vast literature on this subject for more details (see and the references therein).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Tradeoff between Relaxation and Number of Measurements", "weight": 1.0} -->

As discussed in Section 2.5 the atomic norm is the best convex heuristic for solving ill-posed linear inverse problems of the type considered in this paper. However we may wish to approximate the atomic norm in cases when it is intractable to compute exactly, and the discussion in the preceding section provides one approach to constructing a family of relaxations. As one might expect the tradeoff for using such approximations, i.e., a *weaker* convex heuristic than the atomic norm, is an increase in the number of measurements required for exact or robust recovery. The reason for this is that the approximate norms have *larger* tangent cones at their extreme points, which makes it harder to satisfy the empty intersection condition of Proposition 2.1. We highlight this tradeoff here with an illustrative example involving the cut polytope.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Tradeoff between Relaxation and Number of Measurements", "weight": 1.0} -->

The cut polytope is defined as the convex hull of all cut matrices: As described in Section 2.2 low-rank matrices that are composed of $\pm 1$'s as entries are of interest in collaborative filtering, and the norm induced by the cut polytope is a potential convex heuristic for recovering such matrices from limited measurements. However it is well-known that the cut polytope is intractable to characterize, and therefore we need to use tractable relaxations instead. We consider the following two relaxations of the cut polytope. The first is the popular relaxation that is used in semidefinite approximations of the MAXCUT problem: This is the well-studied elliptope, and can be interpreted as the second theta body relaxation (see Section 4.2) of the cut polytope $\mathcal{P}$. We also investigate the performance of a second, weaker relaxation: This polytope is simply the convex hull of symmetric matrices with $\pm 1$'s in the off-diagonal entries, and $1$'s on the diagonal.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Tradeoff between Relaxation and Number of Measurements", "weight": 1.0} -->

We note that $\mathcal{P}_{2}$ is an extremely weak relaxation of $\mathcal{P}$, but we use it here only for illustrative purposes. It is easily seen that with all the inclusions being strict. Figure 3 gives a toy sketch that highlights all the main geometric aspects of these relaxations. In particular $\mathcal{P}_{1}$ has many more extreme points that $\mathcal{P}$, although the set of vertices of $\mathcal{P}_{1}$, i.e., points that have full-dimensional normal cones, are precisely the cut matrices (which are the vertices of $\mathcal{P}$). The convex polytope $\mathcal{P}_{2}$ contains many more vertices compared to $\mathcal{P}$ as shown in Figure 3. As expected the tangent cones at vertices of $\mathcal{P}$ become increasingly larger as we use successively weaker relaxations.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Tradeoff between Relaxation and Number of Measurements", "weight": 1.0} -->

The following result summarizes the number of random measurements required for recovering a cut matrix, i.e., a rank-one sign matrix, using the norms induced by each of these convex bodies.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Terracini's Lemma and Lower Bounds on Recovery", "weight": 1.0} -->

Algebraic structure in the atomic set $\mathcal{A}$ also provides a means for computing *lower bounds* on the number of measurements required for exact recovery. The recovery condition of Proposition 2.1 states that the nullspace ${null}{(\Phi)}$ of the measurement operator $\Phi:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{n}}$ must miss the tangent cone $T_{\mathcal{A}}{(\mathbf{x}^{\star})}$ at the point of interest $\mathbf{x}^{\star}$. Suppose that this tangent cone contains a $q$-dimensional subspace. It is then clear from straightforward linear algebra arguments that the number of measurements $n$ must exceed $q$. Indeed this bound must hold for *any* linear measurement scheme. Thus the dimension of the subspace contained inside the tangent cone (i.e., the dimension of the lineality space) provides a simple lower bound on the number of linear measurements.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Terracini's Lemma and Lower Bounds on Recovery", "weight": 1.0} -->

In this section we discuss a method to obtain estimates of the dimension of a subspace component of the tangent cone. We focus again on the setting in which $\mathcal{A}$ is an algebraic variety. Indeed in all of the examples of Section 2.2, the atomic set $\mathcal{A}$ is an algebraic variety. In such cases simple models $\mathbf{x}^{\star}$ formed according to can be viewed as elements of *secant varieties*.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

While a variety of atomic norms can be represented or approximated by linear matrix inequalities, these representations do not necessarily translate into practical implementations. Semidefinite programming can be technically solved in polynomial time, but general interior point solvers typically only scale to problems with a few hundred variables. For larger scale problems, it is often preferable to exploit structure in the atomic set $\mathcal{A}$ to develop fast, first-order algorithms.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

A starting point for first-order algorithm design lies in determining the structure of the proximity operator (or Moreau envelope) associated with the atomic norm, Here $\mu$ is some positive parameter. Proximity operators have already been harnessed for fast algorithms involving the $\ell_{1}$ norm and the nuclear norm where these maps can be quickly computed in closed form. For the $\ell_{1}$ norm, the $i$th component of $\Pi_{\mathcal{A}}{(\mathbf{x};\mu)}$ is given by This is the so-called *soft thresholding* operator. For the nuclear norm, $\Pi_{\mathcal{A}}$ soft thresholds the singular values. In either case, the only structure necessary for the cited algorithms to converge is the convexity of the norm. Indeed, essentially any algorithm developed for $\ell_{1}$ or nuclear norm minimization can in principle be adapted for atomic norm minimization. One simply needs to apply the operator $\Pi_{\mathcal{A}}$ wherever a shrinkage operation was previously applied.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

For a concrete example, suppose $f$ is a smooth function, and consider the optimization problem The classical projected gradient method for this problem alternates between taking steps along the gradient of $f$ and then applying the proximity operator associated with the atomic norm. Explicitly, the algorithm consists of the iterative procedure where $\{\alpha_{k}\}$ is a sequence of positive stepsizes. Under very mild assumptions, this iteration can be shown to converge to a stationary point of. When $f$ is convex, the returned stationary point is a globally optimal solution. Recently, Nesterov has described a particular variant of this algorithm that is guaranteed to converge at a rate no worse than $O{(k^{- 1})}$, where $k$ is the iteration counter. Moreover, he proposes simple enhancements of the standard iteration to achieve an $O{(k^{- 2})}$ convergence rate for convex $f$ and a linear rate of convergence for strongly convex $f$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

If we apply the projected gradient method to the regularized inverse problem then the algorithm reduces to the straightforward iteration Here is equivalent to for an appropriately chosen $\lambda > 0$ and is useful for estimation from noisy measurements.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

The basic (noiseless) atomic norm minimization problem can be solved by minimizing a sequence of instances of with monotonically decreasing values of $\lambda$. Each subsequent minimization is initialized from the point returned by the previous step. Such an approach corresponds to the classic Method of Multipliers and has proven effective for solving problems regularized by the $\ell_{1}$ norm and for total variation denoising.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

This discussion demonstrates that when the proximity operator associated with some atomic set $\mathcal{A}$ can be easily computed, then efficient first-order algorithms are immediate. For novel atomic norm applications, one can thus focus on algorithms and techniques to compute the associated proximity operators. We note that, from a computational perspective, it may be easier to compute the proximity operator via dual atomic norm. Associated to each proximity operator is the dual operator By an appropriate change of variables, $\Lambda_{\mathcal{A}}$ is nothing more than the projection of $\mu^{- 1}\mathbf{x}$ onto the unit ball in the dual atomic norm: From convex programming duality, we have $\mathbf{x} = {{\Pi_{\mathcal{A}}{(\mathbf{x};\mu)}} + {\Lambda_{\mathcal{A}}{(\mathbf{x};\mu)}}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

This can be seen by observing In particular, $\Pi_{\mathcal{A}}{(\mathbf{x};\mu)}$ and $\Lambda_{\mathcal{A}}{(\mathbf{x};\mu)}$ form a complementary primal-dual pair for this optimization problem. Hence, we only need to able to efficiently compute the Euclidean projection onto the dual norm ball to compute the proximity operator associated with the atomic norm.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

Finally, though the proximity operator provides an elegant framework for algorithm generation, there are many other possible algorithmic approaches that may be employed to take advantage of the particular structure of an atomic set $\mathcal{A}$. For instance, we can rewrite as Suppose we have access to a procedure that, given $\mathbf{z} \in {\mathbb{R}}^{n}$, can decide whether ${\langle\mathbf{z},\mathbf{a}\rangle} \leq 1$ for all $\mathbf{a} \in \mathcal{A}$, or can find a violated constraint where ${\langle\mathbf{z},\hat{\mathbf{a}}\rangle} > 1$. In this case, we can apply a cutting plane method or ellipsoid method to solve or. Similarly, if it is simpler to compute a subgradient of the atomic norm than it is to compute a proximity operator, then the standard subgradient method can be applied to solve problems of the form.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Algorithmic Considerations", "weight": 1.0} -->

Each computational scheme will have different advantages and drawbacks for specific atomic sets, and relative effectiveness needs to be evaluated on a case-by-case basis.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We describe the results of numerical experiments in recovering orthogonal matrices, permutation matrices, and rank-one sign matrices (i.e., cut matrices) from random linear measurements by solving convex optimization problems. All the atomic norm minimization problems in these experiments are solved using a combination of the SDPT3 package and the YALMIP parser.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Orthogonal matrices. We consider the recovery of $20 \times 20$ orthogonal matrices from random Gaussian measurements via *spectral norm minimization*. Specifically we solve the convex program, with the atomic norm being the spectral norm. Figure 4 gives a plot of the probability of exact recovery (computed over $50$ random trials) versus the number of measurements required.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Permutation matrices. We consider the recovery of $20 \times 20$ permutation matrices from random Gaussian measurements. We solve the convex program, with the atomic norm being the norm induced by the Birkhoff polytope of $20 \times 20$ doubly stochastic matrices. Figure 4 gives a plot of the probability of exact recovery (computed over $50$ random trials) versus the number of measurements required.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Cut matrices. We consider the recovery of $20 \times 20$ cut matrices from random Gaussian measurements. As the cut polytope is intractable to characterize, we solve the convex program with the atomic norm being approximated by the norm induced by the semidefinite relaxation $\mathcal{P}_{1}$ described in Section 4.3. Recall that this is the second theta body associated with the convex hull of cut matrices, and so this experiment verifies that objects can be recovered from theta-body approximations. Figure 4 gives a plot of the probability of exact recovery (computed over $50$ random trials) versus the number of measurements required.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In each of these experiments we see agreement between the observed phase transitions, and the theoretical predictions (Propositions 3.13, 3.15, and 4.3) of the number of measurements required for exact recovery. In particular note that the phase transition in Figure 4 for the number of measurements required for recovering an orthogonal matrix is very close to the prediction $n \approx \frac{{3m^{2}} - m}{4} = 295$ of Proposition 3.13. We refer the reader to for similar phase transition plots for recovering sparse vectors, low-rank matrices, and signed vectors from random measurements via convex optimization.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

This manuscript has illustrated that for a fixed set of base atoms, the atomic norm is the best choice of a convex regularizer for solving ill-posed inverse problems with the prescribed priors. With this in mind, our results in Section 3 and Section 4 outline methods for computing hard limits on the number of measurements required for recovery from *any* convex heuristic. Using the calculus of Gaussian widths, such bounds can be computed in a relatively straightforward fashion, especially if one can appeal to notions of convex duality and symmetry. This computational machinery of widths and dimension counting is surprisingly powerful: near-optimal bounds on estimating sparse vectors and low-rank matrices from partial information follow from elementary integration. Thus we expect that our new bounds concerning symmetric, vertex-transitive polytopes are also nearly tight. Moreover, algebraic reasoning allowed us to explore the inherent trade-offs between computational efficiency and measurement demands. More complicated algorithms for atomic norm regularization might extract structure from less information, but approximation algorithms are often sufficient for near optimal reconstructions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Width calculations for more atomic sets", "weight": 1.0} -->

The calculus of Gaussian widths described in Section 3 provides the building blocks for computing the Gaussian widths for the application examples discussed in Section 2. We have not yet exhaustively estimated the widths in all of these examples, and a thorough cataloging of the measurement demands associated with different prior information would provide a more complete understanding of the fundamental limits of solving underdetermined inverse problems. Moreover, our list of examples is by no means exhaustive. The framework developed in this paper provides a compact and efficient methodology for constructing regularizers from very general prior information, and new regularizers can be easily created by translating grounded expert knowledge into new atomic norms.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Recovery bounds for structured measurements", "weight": 1.0} -->

Our recovery results focus on generic measurements because, for a general set $\mathcal{A}$, it does not make sense to delve into specific measurement ensembles. Particular structures of the measurement matrix $\Phi$ will depend on the application and the atomic set $\mathcal{A}$. For instance, in compressed sensing, much work focuses on randomly sampled Fourier coefficients and random Toeplitz and circulant matrices. With low-rank matrices, several authors have investigated reconstruction from a small collection of entries. In all of these cases, some notion of *incoherence* plays a crucial role, quantifying the amount of information garnered from each row of $\Phi$. It would be interesting to explore how to appropriately generalize notions of incoherence to new applications. Is there a particular definition that is general enough to encompass most applications? Or do we need a specialized concept to match the specifics of each atomic norm?

<!-- chunk {"id": "body-0078", "role": "body", "section": "Quantifying the loss due to relaxation", "weight": 1.0} -->

Section 4.3 illustrates how the choice of approximation of a particular atomic norm can dramatically alter the number of measurements required for recovery. However, as was the case for vertices of the cut polytope, some relaxations incur only a very modest increase in measurement demands. Using techniques similar to those employed in the study of semidefinite relaxations of hard combinatorial problems, is it possible to provide a more systematic method to estimate the number of measurements required to recover points from polynomial-time computable norms?

<!-- chunk {"id": "body-0079", "role": "body", "section": "Atomic norm decompositions", "weight": 1.0} -->

While the techniques of Section 3 and Section 4 provide bounds on the estimation of points in low-dimensional secant varieties of atomic sets, they do not provide a procedure for actually constructing decompositions. That is, we have provided bounds on the number of measurements required to recover points $\mathbf{x}$ of the form when the coefficient sequence $\{ c_{\mathbf{a}}\}$ is sparse, but we do not provide any methods for actually recovering $c$ itself. These decompositions are useful, for instance, in actually computing the rank-one binary vectors optimized in semidefinite relaxations of combinatorial algorithms, or in the computation of tensor decompositions from incomplete data. Is it possible to use algebraic structure to generate deterministic or randomized algorithms for reconstructing the atoms that underlie a vector $\mathbf{x}$, especially when approximate norms are used?

<!-- chunk {"id": "body-0080", "role": "body", "section": "Large-scale algorithms", "weight": 1.0} -->

Finally, we think that the most fruitful extensions of this work lie in a thorough exploration of the empirical performance and efficacy of atomic norms on large-scale inverse problems. The proposed algorithms in Section 5 require only the knowledge of the proximity operator of an atomic norm, or a Euclidean projection operator onto the dual norm ball. Using these design principles and the geometry of particular atomic norms should enable the scaling of atomic norm techniques to massive data sets.
