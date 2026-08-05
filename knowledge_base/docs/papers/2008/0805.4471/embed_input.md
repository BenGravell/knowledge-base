<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Exact Matrix Completion via Convex Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider a problem of considerable practical interest: the recovery of a data matrix from a sampling of its entries. Suppose that we observe m entries selected uniformly at random from a matrix M. Can we complete the matrix and recover the entries that we have not seen? We show that one can perfectly recover most low-rank matrices from what appears to be an incomplete set of entries. We prove that if the number m of sampled entries obeys m >= C n^{1.2} r log n for some positive numerical constant C, then with very high probability, most n by n matrices of rank r can be perfectly recovered by solving a simple convex optimization program. This program finds the matrix with minimum nuclear norm that fits the data. The condition above assumes that the rank is not too large. However, if one replaces the 1.2 exponent with 1.25, then the result holds for all values of the rank. Similar results hold for arbitrary rectangular matrices as well. Our results are connected with the recent literature on compressed sensing, and show that objects other than signals and images can be perfectly reconstructed from very limited information.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many practical problems of interest, one would like to recover a matrix from a sampling of its entries. As a motivating example, consider the task of inferring answers in a partially filled out survey. That is, suppose that questions are being asked to a collection of individuals. Then we can form a matrix where the rows index each individual and the columns index the questions. We collect data to fill out this table but unfortunately, many questions are left unanswered. Is it possible to make an educated guess about what the missing answers should be? How can one make such a guess? Formally, we may view this problem as follows. We are interested in recovering a data matrix $\mathbf{M}$ with $n_{1}$ rows and $n_{2}$ columns but only get to observe a number $m$ of its entries which is comparably much smaller than $n_{1}n_{2}$, the total number of entries. Can one recover the matrix $\mathbf{M}$ from $m$ of its entries? In general, everyone would agree that this is impossible without some additional information.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many instances, however, the matrix we wish to recover is known to be structured in the sense that it is low-rank or approximately low-rank. (We recall for completeness that a matrix with $n_{1}$ rows and $n_{2}$ columns has rank $r$ if its rows or columns span an $r$-dimensional space.) Below are two examples of practical scenarios where one would like to be able to recover a low-rank matrix from a sampling of its entries.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Netflix problem. In the area of recommender systems, users submit ratings on a subset of entries in a database, and the vendor provides recommendations based on the user's preferences. Because users only rate a few items, one would like to infer their preference for unrated items.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A special instance of this problem is the now famous Netflix problem. Users (rows of the data matrix) are given the opportunity to rate movies (columns of the data matrix) but users typically rate only very few movies so that there are very few scattered observed entries of this data matrix. Yet one would like to complete this matrix so that the vendor (here Netflix) might recommend titles that any particular user is likely to be willing to order. In this case, the data matrix of all user-ratings may be approximately low-rank because it is commonly believed that only a few factors contribute to an individual's tastes or preferences.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Triangulation from incomplete data. Suppose we are given partial information about the distances between objects and would like to reconstruct the low-dimensional geometry describing their locations. For example, we may have a network of low-power wirelessly networked sensors scattered randomly across a region. Suppose each sensor only has the ability to construct distance estimates based on signal strength readings from its nearest fellow sensors. From these noisy distance estimates, we can form a partially observed distance matrix. We can then estimate the true distance matrix whose rank will be equal to two if the sensors are located in a plane or three if they are located in three dimensional space. In this case, we only need to observe a few distances per node to have enough information to reconstruct the positions of the objects.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

These examples are of course far from exhaustive and there are many other problems which fall in this general category. For instance, we may have some very limited information about a covariance matrix of interest. Yet, this covariance matrix may be low-rank or approximately low-rank because the variables only depend upon a comparably smaller number of factors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Impediments and solutions", "weight": 1.0} -->

Suppose for simplicity that we wish to recover a square $n \times n$ matrix $\mathbf{M}$ of rank $r$.^11^1We emphasize that there is nothing special about $\mathbf{M}$ being square and all of our discussion would apply to arbitrary rectangular matrices as well. The advantage of focusing on square matrices is a simplified exposition and reduction in the number of parameters of which we need to keep track. Such a matrix $\mathbf{M}$ can be represented by $n^{2}$ numbers, but it only has ${({{2n} - r})}r$ degrees of freedom. This fact can be revealed by counting parameters in the singular value decomposition (the number of degrees of freedom associated with the description of the singular values and of the left and right singular vectors). When the rank is small, this is considerably smaller than $n^{2}$. For instance, when $\mathbf{M}$ encodes a 10-dimensional phenomenon, then the number of degrees of freedom is about $20n$ offering a reduction in dimensionality by a factor about equal to $n/20$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Impediments and solutions", "weight": 1.0} -->

When $n$ is large (e.g. in the thousands or millions), the data matrix carries much less information than its ambient dimension suggests. The problem is now whether it is possible to recover this matrix from a sampling of its entries without having to probe all the $n^{2}$ entries, or more generally collect $n^{2}$ or more measurements about $\mathbf{M}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Which matrices?", "weight": 1.0} -->

In general, one cannot hope to be able to recover a low-rank matrix from a sample of its entries. Consider the rank-1 matrix $\mathbf{M}$ equal to where here and throughout, ${\mathbf{e}}_{i}$ is the $i$th canonical basis vector in Euclidean space (the vector with all entries equal to 0 but the $i$th equal to 1). This matrix has a 1 in the top-right corner and all the other entries are 0. Clearly this matrix cannot be recovered from a sampling of its entries unless we pretty much see all the entries. The reason is that for most sampling sets, we would only get to see zeros so that we would have no way of guessing that the matrix is not zero. For instance, if we were to see 90% of the entries selected at random, then 10% of the time we would only get to see zeroes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Which matrices?", "weight": 1.0} -->

It is therefore impossible to recover all low-rank matrices from a set of sampled entries but can one recover most of them? To investigate this issue, we introduce a simple model of low-rank matrices. Consider the singular value decomposition (SVD) of a matrix $\mathbf{M}$ where the ${\mathbf{u}}_{k}$'s and ${\mathbf{v}}_{k}$'s are the left and right singular vectors, and the $\sigma_{k}$'s are the singular values (the roots of the eigenvalues of ${\mathbf{M}}^{\ast}{\mathbf{M}}$).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Which matrices?", "weight": 1.0} -->

Then we could think of a generic low-rank matrix as follows: the family ${\{{\mathbf{u}}_{k}\}}_{1 \leq k \leq r}$ is selected uniformly at random among all families of $r$ orthonormal vectors, and similarly for the the family ${\{{\mathbf{v}}_{k}\}}_{1 \leq k \leq r}$. The two families may or may not be independent of each other. We make no assumptions about the singular values $\sigma_{k}$. In the sequel, we will refer to this model as the random orthogonal model. This model is convenient in the sense that it is both very concrete and simple, and useful in the sense that it will help us fix the main ideas. In the sequel, however, we will consider far more general models. The question for now is whether or not one can recover such a generic matrix from a sampling of its entries.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Which sampling sets?", "weight": 1.0} -->

Clearly, one cannot hope to reconstruct any low-rank matrix $\mathbf{M}$---even of rank $1$---if the sampling set avoids any column or row of $\mathbf{M}$. Suppose that $\mathbf{M}$ is of rank 1 and of the form ${\mathbf{x}}{\mathbf{y}}^{\ast}$, ${{\mathbf{x}},{\mathbf{y}}} \in {\mathbb{R}}^{n}$ so that the $(i,j)$th entry is given by Then if we do not have samples from the first row for example, one could never guess the value of the first component $x_{1}$, by any method whatsoever; no information about $x_{1}$ is observed. There is of course nothing special about the first row and this argument extends to any row or column. To have any hope of recovering an unknown matrix, one needs at least one observation per row and one observation per column.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Which sampling sets?", "weight": 1.0} -->

We have just seen that if the sampling is adversarial, e.g. one observes all of the entries of $\mathbf{M}$ but those in the first row, then one would not even be able to recover matrices of rank $1$. But what happens for most sampling sets? Can one recover a low-rank matrix from almost all sampling sets of cardinality $m$? Formally, suppose that the set $\Omega$ of locations corresponding to the observed entries (${(i,j)} \in \Omega$ if $M_{ij}$ is observed) is a set of cardinality $m$ sampled uniformly at random. Then can one recover a generic low-rank matrix $M$, perhaps with very large probability, from the knowledge of the value of its entries in the set $\Omega$?

<!-- chunk {"id": "body-0016", "role": "body", "section": "Which algorithm?", "weight": 1.0} -->

If the number of measurements is sufficiently large, and if the entries are sufficiently uniformly distributed as above, one might hope that there is only one low-rank matrix with these entries. If this were true, one would want to recover the data matrix by solving the optimization problem where $\mathbf{X}$ is the decision variable and ${rank}{({\mathbf{X}})}$ is equal to the rank of the matrix $\mathbf{X}$. The program (1.3) is a common sense approach which simply seeks the simplest explanation fitting the observed data. If there were only one low-rank object fitting the data, this would recover $\mathbf{M}$. This is unfortunately of little practical use because this optimization problem is not only NP-hard, but all known algorithms which provide exact solutions require time doubly exponential in the dimension $n$ of the matrix in both theory and practice.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Which algorithm?", "weight": 1.0} -->

If a matrix has rank $r$, then it has exactly $r$ nonzero singular values so that the rank function in (1.3) is simply the number of nonvanishing singular values. In this paper, we consider an alternative which minimizes the sum of the singular values over the constraint set. This sum is called the *nuclear norm*, where, here and below, $\sigma_{k}{({\mathbf{X}})}$ denotes the $k$th largest singular value of $\mathbf{X}$. The heuristic optimization is then given by Whereas the rank function counts the number of nonvanishing singular values, the nuclear norm sums their amplitude and in some sense, is to the rank functional what the convex $\ell_{1}$ norm is to the counting $\ell_{0}$ norm in the area of sparse signal recovery. The main point here is that the nuclear norm is a convex function and, as we will discuss in Section 1.4 can be optimized efficiently via semidefinite programming.

<!-- chunk {"id": "body-0018", "role": "body", "section": "A first typical result", "weight": 1.0} -->

Our first result shows that, perhaps unexpectedly, this heuristic optimization recovers a generic $\mathbf{M}$ when the number of randomly sampled entries is large enough.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main results", "weight": 1.0} -->

As seen in our first example (1.1), it is impossible to recover a matrix which is equal to zero in nearly all of its entries unless we see all the entries of the matrix. To recover a low-rank matrix, this matrix cannot be in the null space of the sampling operator giving the values of a subset of the entries. Now it is easy to see that if the singular vectors of a matrix $\mathbf{M}$ are highly concentrated, then $\mathbf{M}$ could very well be in the null-space of the sampling operator. For instance consider the rank-2 symmetric matrix $\mathbf{M}$ given by where the singular values are arbitrary. Then this matrix vanishes everywhere except in the top-left $2 \times 2$ corner and one would basically need to see all the entries of $\mathbf{M}$ to be able to recover this matrix exactly by any method whatsoever. There is an endless list of examples of this sort.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main results", "weight": 1.0} -->

Hence, we arrive at the notion that, somehow, the singular vectors need to be sufficiently spread---that is, uncorrelated with the standard basis---in order to minimize the number of observations needed to recover a low-rank matrix.^22^2Both the left and right singular vectors need to be uncorrelated with the standard basis. Indeed, the matrix ${\mathbf{e}}_{1}{\mathbf{v}}^{\ast}$ has its first row equal to $\mathbf{v}$ and all the others equal to zero. Clearly, this rank-1 matrix cannot be recovered unless we basically see all of its entries. This motivates the following definition.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Extensions", "weight": 1.0} -->

Our main result (Theorem 1.3) extends to a variety of other low-rank matrix completion problems beyond the sampling of entries. Indeed, suppose we have two orthonormal bases ${\mathbf{f}}_{1},\ldots,{\mathbf{f}}_{n}$ and ${\mathbf{g}}_{1},\ldots,{\mathbf{g}}_{n}$ of ${\mathbb{R}}^{n}$, and that we are interested in solving the rank minimization problem This comes up in a number of applications. As a motivating example, there has been a great deal of interest in the machine learning community in developing specialized algorithms for the *multiclass* and *multitask* learning problems (see, e.g.,). In multiclass learning, the goal is to build multiple classifiers with the same training data to distinguish between more than two categories. For example, in face recognition, one might want to classify whether an image patch corresponds to an eye, nose, or mouth.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Extensions", "weight": 1.0} -->

In multitask learning, we have a large set of data, but have a variety of different classification tasks, and, for each task, only partial subsets of the data are relevant. For instance, in activity recognition, we may have acquired sets of observations of multiple subjects and want to determine if each observed person is walking or running. However, a different classifier is to be learned for each individual, and it is not clear how having access to the full collection of observations can improve classification performance. Multitask learning aims precisely to take advantage of the access to the full database to improve performance on the individual tasks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Extensions", "weight": 1.0} -->

In the abstract formulation of this problem for linear classifiers, we have $K$ classes to distinguish and are given training examples ${\mathbf{f}}_{1},\ldots,{\mathbf{f}}_{n}$. For each example, we are given partial labeling information about which classes it belongs or does not belong to. That is, for each example ${\mathbf{f}}_{j}$ and class $k$, we may either be told that ${\mathbf{f}}_{j}$ belongs to class $k$, be told ${\mathbf{f}}_{j}$ does not belong to class $k$, or provided no information about the membership of ${\mathbf{f}}_{j}$ to class $k$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Extensions", "weight": 1.0} -->

Formally, we can search for the vector ${\mathbf{w}}_{k}$ that satisfies the equality constraints ${{\mathbf{w}}_{k}^{\ast}{\mathbf{f}}_{i}} = y_{ik}$ where $y_{ik} = 1$ if we are told that ${\mathbf{f}}_{i}$ belongs to class $k$, $y_{ik} = {- 1}$ if we are told that ${\mathbf{f}}_{i}$ does not belong to class $k$, and $y_{ik}$ unconstrained if we are not provided information. A common hypothesis in the multitask setting is that the ${\mathbf{w}}_{k}$ corresponding to each of the classes together span a very low dimensional subspace with dimension significantly smaller than $K$. That is, the basic assumption is that is low-rank.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Extensions", "weight": 1.0} -->

Hence, the multiclass learning problem can be cast as (1.13) with observations of the form ${\mathbf{f}}_{i}^{\ast}{\mathbf{W}}{\mathbf{e}}_{j}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Extensions", "weight": 1.0} -->

Hence, Then if the conditions of Theorem 1.3 hold for the matrix ${\mathbf{F}}{\mathbf{X}}{\mathbf{G}}^{\ast}$, it is immediate that nuclear norm minimization finds the unique optimal solution of (1.13) when we are provided a large enough random collection of the inner products ${\mathbf{f}}_{i}^{\ast}{\mathbf{M}}{\mathbf{g}}_{j}$. In other words, all that is needed is that the column and row spaces of $\mathbf{M}$ be respectively incoherent with the basis $({\mathbf{f}}_{i})$ and $({\mathbf{g}}_{i})$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Extensions", "weight": 1.0} -->

From this perspective, we additionally remark that our results likely extend to the case where one observes a small number of arbitrary linear functionals of a hidden matrix $\mathbf{M}$. Set $N = n^{2}$ and ${\mathbf{A}}_{1},\ldots,{\mathbf{A}}_{N}$ be an orthonormal basis for the linear space of $n \times n$ matrices with the usual inner product ${\langle{\mathbf{X}},{\mathbf{Y}}\rangle} = {{trace}{({{\mathbf{X}}^{\ast}{\mathbf{Y}}})}}$. Then we expect our results should also apply to the rank minimization problem where $\Omega \subset {\{ 1,\ldots,N\}}$ is selected uniformly at random.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Extensions", "weight": 1.0} -->

In fact, (1.14) is (1.3) when the orthobasis is the canonical basis ${({{\mathbf{e}}_{i}{\mathbf{e}}_{j}^{\ast}})}_{{1 \leq i},{j \leq n}}$. Here, those low-rank matrices which have small inner product with all the basis elements ${\mathbf{A}}_{k}$ may be recoverable by nuclear norm minimization. To avoid unnecessary confusion and notational clutter, we leave this general low-rank recovery problem for future work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

Nuclear norm minimization is a recent heuristic introduced by Fazel, and is an extension of the trace heuristic often used by the control community, see e.g.. Indeed, when the matrix variable is symmetric and positive semidefinite, the nuclear norm of $\mathbf{X}$ is the sum of the (nonnegative) eigenvalues and thus equal to the trace of $\mathbf{X}$. Hence, for positive semidefinite unknowns, (1.5) would simply minimize the trace over the constraint set: This is a semidefinite program. Even for the general matrix $\mathbf{M}$ which may not be positive definite or even symmetric, the nuclear norm heuristic can be formulated in terms of semidefinite programming as, for instance, the program (1.5) is equivalent to with optimization variables $\mathbf{X}$, ${\mathbf{W}}_{1}$ and ${\mathbf{W}}_{2}$, (see, e.g.,).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

There are many efficient algorithms and high-quality software available for solving these types of problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

Our work is inspired by results in the emerging field of compressive sampling or compressed sensing, a new paradigm for acquiring information about objects of interest from what appears to be a highly incomplete set of measurements. In practice, this means for example that high-resolution imaging is possible with fewer sensors, or that one can speed up signal acquisition time in biomedical applications by orders of magnitude, simply by taking far fewer specially coded samples. Mathematically speaking, we wish to reconstruct a signal ${\mathbf{x}} \in {\mathbb{R}}^{n}$ from a small number measurements ${\mathbf{y}} = {\Phi{\mathbf{x}}}$, ${\mathbf{y}} \in {\mathbb{R}}^{m}$, and $m$ is much smaller than $n$; i.e. we have far fewer equations than unknowns. In general, one cannot hope to reconstruct $\mathbf{x}$ but assume now that the object we wish to recover is known to be structured in the sense that it is sparse (or approximately sparse).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

This means that the unknown object depends upon a smaller number of unknown parameters. Then it has been shown that $\ell_{1}$ minimization allows recovery of sparse signals from remarkably few measurements: supposing $\Phi$ is chosen randomly from a suitable distribution, then with very high probability, all sparse signals with about $k$ nonzero entries can be recovered from on the order of $k{\log n}$ measurements. For instance, if $\mathbf{x}$ is $k$-sparse in the Fourier domain, i.e. $\mathbf{x}$ is a superposition of $k$ sinusoids, then it can be perfectly recovered with high probability---by $\ell_{1}$ minimization---from the knowledge of about $k{\log n}$ of its entries sampled uniformly at random.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

From this viewpoint, the results in this paper greatly extend the theory of compressed sensing by showing that other types of interesting objects or structures, beyond sparse signals and images, can be recovered from a limited set of measurements. Moreover, the techniques for proving our main results build upon ideas from the compressed sensing literature together with probabilistic tools such as the powerful techniques of Bourgain and of Rudelson for bounding norms of operators between Banach spaces.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

Our notion of incoherence generalizes the concept of the same name in compressive sampling. Notably the authors introduce the notion of the incoherence of a unitary transformation. Letting $\mathbf{U}$ be an $n \times n$ unitary matrix, the *coherence* of $\mathbf{U}$ is given by This quantity ranges in values from $1$ for a unitary transformation whose entries all have the same magnitude to $n$ for the identity matrix. Using this notion, showed that with high probability, a $k$-sparse signal could be recovered via linear programming from the observation of the inner product of the signal with $m = {\Omega{({\mu{({\mathbf{U}})}k{\log n}})}}$ randomly selected columns of the matrix $\mathbf{U}$. This result provided a generalization of the celebrated results about partial Fourier observations described, a special case where ${\mu{({\mathbf{U}})}} = 1$. This paper generalizes the notion of incoherence to problems beyond the setting of sparse signal recovery.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

In, the authors studied the nuclear norm heuristic applied to a related problem where partial information about a matrix $\mathbf{M}$ is available from $m$ equations of the form where for each $k$, ${\{ A_{ij}^{(k)}\}}_{ij}$ is an i.i.d. sequence of Gaussian or Bernoulli random variables and the sequences $\{{\mathbf{A}}^{(k)}\}$ are also independent from each other (the sequences $\{{\mathbf{A}}^{(k)}\}$ and $\{ b_{k}\}$ are available to the analyst). Building on the concept of restricted isometry introduced in in the context of sparse signal recovery, establishes the first sufficient conditions for which the nuclear norm heuristic returns the minimum rank element in the constraint set. They prove that the heuristic succeeds with large probability whenever the number $m$ of available measurements is greater than a constant times $2nr{\log n}$ for $n \times n$ matrices.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

Although this is an interesting result, a serious impediment to this approach is that one needs to essentially measure random projections of the unknown data matrix---a situation which unfortunately does not commonly arise in practice. Further, the measurements in (1.15) give some information about all the entries of $\mathbf{M}$ whereas in our problem, information about most of the entries is simply not available. In particular, the results and techniques introduced in do not begin to address the matrix completion problem of interest to us in this paper. As a consequence, our methods are completely different; for example, they do not rely on any notions of restricted isometry. Instead, as we discuss below, we prove the existence of a Lagrange multiplier for the optimization (1.5) that certifies the unique optimal solution is precisely the matrix that we wish to recover.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

Finally, we would like to briefly discuss the possibility of other recovery algorithms when the sampling happens to be chosen in a very special fashion. For example, suppose that $\mathbf{M}$ is generic and that we precisely observe every entry in the first $r$ rows and columns of the matrix. Write $\mathbf{M}$ in block form as with ${\mathbf{M}}_{11}$ an $r \times r$ matrix. In the special case that ${\mathbf{M}}_{11}$ is invertible and $\mathbf{M}$ has rank $r$, then it is easy to verify that ${\mathbf{M}}_{22} = {{\mathbf{M}}_{21}{\mathbf{M}}_{11}^{- 1}{\mathbf{M}}_{12}}$. One can prove this identity by forming the SVD of $\mathbf{M}$, for example.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Connections, alternatives and prior art", "weight": 1.0} -->

That is, if $\mathbf{M}$ is generic, and the upper $r \times r$ block is invertible, and we observe *every* entry in the first $r$ rows and columns, we can recover $\mathbf{M}$. This result immediately generalizes to the case where one observes precisely $r$ rows and $r$ columns and the $r \times r$ matrix at the intersection of the observed rows and columns is invertible. However, this scheme has many practical drawbacks that stand in the way of a generalization to a completion algorithm from a general set of entries. First, if we miss *any* entry in these rows or columns, we cannot recover $\mathbf{M}$, nor can we leverage any information provided by entries of ${\mathbf{M}}_{22}$. Second, if the matrix has rank less than $r$, and we observe $r$ rows and columns, a combinatorial search to find the collection that has an invertible square sub-block is required. Moreover, because of the matrix inversion, the algorithm is rather fragile to noise in the entries.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Notations and organization of the paper", "weight": 1.0} -->

The paper is organized as follows. We first argue in Section 2 that the random orthogonal model and, more generally, matrices with incoherent column and row spaces obey the assumptions of the general Theorem 1.3. To prove Theorem 1.3, we first establish sufficient conditions which guarantee that the true low-rank matrix $\mathbf{M}$ is the unique solution to (1.5) in Section 3. One of these conditions is the existence of a dual vector obeying two crucial properties. Section 4 constructs such a dual vector and provides the overall architecture of the proof which shows that, indeed, this vector obeys the desired properties provided that the number of measurements is sufficiently large. Surprisingly, as explored in Section 5, the existence of a dual vector certifying that $\mathbf{M}$ is unique is related to some problems in random graph theory including "the coupon collector's problem." Following this discussion, we prove our main result via several intermediate results which are all proven in Section 6. Section 7 introduces numerical experiments showing that matrix completion based on nuclear norm minimization works well in practice. Section 8 closes the paper with a short summary of our findings, a discussion of important extensions and improvements.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Notations and organization of the paper", "weight": 1.0} -->

In particular, we will discuss possible ways of improving the 1.2 exponent in (1.10) so that it gets closer to 1. Finally, the Appendix provides proofs of auxiliary lemmas supporting our main argument.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Notations and organization of the paper", "weight": 1.0} -->

Before continuing, we provide here a brief summary of the notations used throughout the paper. Matrices are bold capital, vectors are bold lowercase and scalars or entries are not bold. For instance, $\mathbf{X}$ is a matrix and $X_{ij}$ its $(i,j)$th entry. Likewise $\mathbf{x}$ is a vector and $x_{i}$ its $i$th component. When we have a collection of vectors ${\mathbf{u}}_{k} \in {\mathbb{R}}^{n}$ for $1 \leq k \leq d$, we will denote by $u_{ik}$ the $i$th component of the vector ${\mathbf{u}}_{k}$ and $\lbrack{\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{d}\rbrack$ will denote the $n \times d$ matrix whose $k$th column is ${\mathbf{u}}_{k}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Notations and organization of the paper", "weight": 1.0} -->

Further, we will also manipulate linear transformation which acts on matrices and will use caligraphic letters for these operators as in $\mathcal{A}{({\mathbf{X}})}$. In particular, the identity operator will be denoted by $\mathcal{I}$. The only norm we will consider for these operators is their spectral norm (the top singular value) denoted by ${\|\mathcal{A}\|} = {\sup_{{\mathbf{X}}:{{\|{\mathbf{X}}\|}_{F} \leq 1}}{\|{\mathcal{A}{({\mathbf{X}})}}\|}_{F}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Notations and organization of the paper", "weight": 1.0} -->

Finally, we adopt the convention that $C$ denotes a numerical constant independent of the matrix dimensions, rank, and number of measurements, whose value may change from line to line. Certain special constants with precise numerical values will be ornamented with subscripts (e.g., $C_{R}$). Any exceptions to this notational scheme will be noted in the text.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Which matrices are incoherent?", "weight": 1.0} -->

In this section we restrict our attention to square $n \times n$ matrices, but the extension to rectangular $n_{1} \times n_{2}$ matrices immediately follows by setting $n = {\max{(n_{1},n_{2})}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Incoherent bases span incoherent subspaces", "weight": 1.0} -->

As mentioned above, A0 holds automatically, but, observe that A1 would not hold with a small value of $\mu_{1}$ if two rows of the matrices $\lbrack{\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{r}\rbrack$ and $\lbrack{\mathbf{v}}_{1},\ldots,{\mathbf{v}}_{r}\rbrack$ are identical with all entries of magnitude $\sqrt{\mu_{B}/n}$ since it is not hard to see that in this case Certainly, this example is constructed in a very special way, and should occur infrequently. We now show that it is generically unlikely.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Incoherent bases span incoherent subspaces", "weight": 1.0} -->

Consider the matrix where ${\{\epsilon_{k}\}}_{1 \leq k \leq r}$ is an arbitrary sign sequence. For almost all choices of sign sequences, A1 is satisfied with $\mu_{1} = {O{({\mu_{B}\sqrt{\log n}})}}$. Indeed, if one selects the signs uniformly at random, then for each $\beta > 0$, This is of interest because suppose the low-rank matrix we wish to recover is of the form with scalars $\lambda_{k}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Incoherent bases span incoherent subspaces", "weight": 1.0} -->

Since the vectors $\{{\mathbf{u}}_{k}\}$ and $\{{\mathbf{v}}_{k}\}$ are orthogonal, the singular values of $\mathbf{M}$ are given by $|\lambda_{k}|$ and the singular vectors are given by $\text{sgn}{(\lambda_{k})}{\mathbf{u}}_{k}$ and ${\mathbf{v}}_{k}$ for $k = {1,\ldots,r}$. Hence, in this model A1 concerns the maximum entry of the matrix given by (2.1) with $\epsilon_{k} = {\text{sgn}{(\lambda_{k})}}$. That is to say, for most sign patterns, the matrix of interest obeys an appropriate size condition.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Incoherent bases span incoherent subspaces", "weight": 1.0} -->

We emphasize here that the only thing that we assumed about the ${\mathbf{u}}_{k}$'s and ${\mathbf{v}}_{k}$'s was that they had small entries. In particular, they could be equal to each other as would be the case for a symmetric matrix.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Incoherent bases span incoherent subspaces", "weight": 1.0} -->

The claim (2.2) is a simple application of Hoeffding's inequality. The $(i,j)$th entry of (2.1) is given by and is a sum of $r$ zero-mean independent random variables, each bounded by $\mu_{B}/n$. Therefore, Setting $\lambda$ proportional to $\sqrt{\log n}$ and applying the union bound gives the claim.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Random subspaces span incoherent subspaces", "weight": 1.0} -->

In this section, we prove that the random orthogonal model obeys the two assumptions A0 and A1 (with appropriate values for the $\mu$'s) with large probability.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Duality", "weight": 1.0} -->

Suppose ${\mathbf{X}}_{0} \in {\mathbb{R}}^{n_{1} \times n_{2}}$ has rank $r$ with a singular value decomposition given by With these notations, $\mathbf{Y}$ is a subgradient of the nuclear norm at ${\mathbf{X}}_{0}$ if and only if it is of the form where $\mathbf{W}$ obeys the following two properties: the column space of $\mathbf{W}$ is orthogonal to $U \equiv {{span}{({\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{r})}}$, and the row space of $\mathbf{W}$ is orthogonal to $V \equiv {{span}{({\mathbf{v}}_{1},\ldots,{\mathbf{v}}_{r})}}$; the spectral norm of $\mathbf{W}$ is less than or equal

<!-- chunk {"id": "body-0052", "role": "body", "section": "Duality", "weight": 1.0} -->

(see, e.g., ). To express these properties concisely, it is convenient to introduce the orthogonal decomposition ${\mathbb{R}}^{n_{1} \times n_{2}} = {T \oplus T^{\perp}}$ where $T$ is the linear space spanned by elements of the form ${\mathbf{u}}_{k}{\mathbf{x}}^{\ast}$ and ${\mathbf{y}}{\mathbf{v}}_{k}^{\ast}$, $1 \leq k \leq r$, where $\mathbf{x}$ and $\mathbf{y}$ are arbitrary, and $T^{\perp}$ is its orthogonal complement.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Duality", "weight": 1.0} -->

Now that we have characterized the subgradient of the nuclear norm, the lemma below gives sufficient conditions for the uniqueness of the minimizer to (1.5).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Architecture of the proof", "weight": 1.0} -->

Our strategy to prove that ${\mathbf{M}} = {\sum_{1 \leq k \leq r}{\sigma_{k}{\mathbf{u}}_{k}{\mathbf{v}}_{k}^{\ast}}}$ is the unique minimizer to (1.5) is to construct a matrix $\mathbf{Y}$ which vanishes on $\Omega^{c}$ and obeys the conditions of Lemma 3.1 (and show the injectivity of the sampling operator restricted to matrices in $T$ along the way). Set $\mathcal{P}_{\Omega}$ to be the orthogonal projector onto the indices in $\Omega$ so that the $(i,j)$th component of $\mathcal{P}_{\Omega}{({\mathbf{X}})}$ is equal to $X_{ij}$ if ${(i,j)} \in \Omega$ and zero otherwise.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Architecture of the proof", "weight": 1.0} -->

Since the Pythagoras formula gives minimizing the Frobenius norm of $\mathbf{X}$ amounts to minimizing the Frobenius norm of $\mathcal{P}_{T^{\perp}}{({\mathbf{X}})}$ under the constraint ${\mathcal{P}_{T}{({\mathbf{X}})}} = {\sum_{k = 1}^{r}{{\mathbf{u}}_{k}{\mathbf{v}}_{k}^{\ast}}}$. Our motivation is twofold. First, the solution to the least-squares problem (4.1) has a closed form that is amenable to analysis.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Architecture of the proof", "weight": 1.0} -->

Second, by forcing $\mathcal{P}_{T^{\perp}}{({\mathbf{Y}})}$ to be small in the Frobenius norm, we hope that it will be small in the spectral norm as well, and establishing that ${\|{\mathcal{P}_{T^{\perp}}{({\mathbf{Y}})}}\|} < 1$ would prove that $\mathbf{M}$ is the unique solution to (1.5).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Architecture of the proof", "weight": 1.0} -->

To summarize the aims of our proof strategy, We must first show that ${\mathcal{A}_{\OmegaT}^{\ast}\mathcal{A}_{\OmegaT}} = {\mathcal{P}_{T}\mathcal{P}_{\Omega}\mathcal{P}_{T}}$ is a one-to-one linear mapping from $T$ onto itself. In this case, $\mathcal{A}_{\OmegaT} = {\mathcal{P}_{\Omega}\mathcal{P}_{T}}$---as a mapping from $T$ to ${\mathbb{R}}^{n_{1} \times n_{2}}$---is injective. This is the second sufficient condition of Lemma 3.1. Moreover, our ansatz for $\mathbf{Y}$ given by (4.2) is well-defined.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Architecture of the proof", "weight": 1.0} -->

Having established that $\mathbf{Y}$ is well-defined, we will show that thus proving the first sufficient condition.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Bernoulli model", "weight": 1.0} -->

Instead of showing that the theorem holds when $\Omega$ is a set of size $m$ sampled uniformly at random, we prove the theorem for a subset $\Omega'$ sampled according to the Bernoulli model. Here and below, ${\{\delta_{ij}\}}_{{1 \leq i \leq n_{1}},{1 \leq j \leq n_{2}}}$ is a sequence of independent identically distributed $0/1$ Bernoulli random variables with Note that ${{\mathbb{E}}{|\Omega'|}} = m$, so that the average cardinality of $\Omega'$ is that of $\Omega$. Then following the same reasoning as the argument developed in Section II.C of shows that the probability of 'failure' under the uniform model is bounded by 2 times the probability of failure under the Bernoulli model; the failure event is the event on which the solution to (1.5) is not exact.

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Bernoulli model", "weight": 1.0} -->

Hence, we can restrict our attention to the Bernoulli model and from now, we will assume that $\Omega$ is given by (4.4). This is advantageous because the Bernoulli model admits a simpler analysis than uniform sampling thanks to the independence between the $\delta_{ij}$'s.

<!-- chunk {"id": "body-0061", "role": "body", "section": "The injectivity property and the coupon collector's problem", "weight": 1.0} -->

We argued in the Introduction that to have any hope of recovering an unknown matrix of rank 1 by any method whatsoever, one needs at least one observation per row and one observation per column. Sample $m$ entries uniformly at random. Viewing the row indices as bins, assign the $k$th sampled entry to the bin corresponding to its row index. Then to have any hope of recovering our matrix, all the bins need to be occupied. Quantifying how many samples are required to fill all of the bins is the famous *coupon collector's problem*.

<!-- chunk {"id": "body-0062", "role": "body", "section": "The injectivity property and the coupon collector's problem", "weight": 1.0} -->

When the entries are sampled uniformly at random, it is well known that one needs on the order of $n{\log n}$ samples to sample all the rows. What is interesting is that Theorem 4.1 implies that $\mathcal{P}_{T}\mathcal{P}_{\Omega}\mathcal{P}_{T}$ is invertible---a stronger property---when the number of samples is also on the order of $n{\log n}$. A particular implication of this discussion is that the logarithmic factors in Theorem 4.1 are unavoidable.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The injectivity property and the connectivity problem", "weight": 1.0} -->

To recover a matrix of rank 1, one needs much more than at least one observation per row and column. Let $R$ be the set of row indices, $1 \leq i \leq n$, and $C$ be the set of column indices, $1 \leq j \leq n$, and consider the bipartite graph connecting vertices $i \in R$ to vertices $j \in C$ if and only if ${(i,j)} \in \Omega$, i.e. the $(i,j)$th entry is observed. We claim that if this graph is not fully connected, then one cannot hope to recover a matrix of rank 1.

<!-- chunk {"id": "body-0064", "role": "body", "section": "The injectivity property and the connectivity problem", "weight": 1.0} -->

To see this, we let $I$ be the set of row indices and $J$ be the set of column indices in any connected component. We will assume that $I$ and $J$ are nonempty as otherwise, one is in the previously discussed situation where some rows or columns are not sampled. Consider a rank 1 matrix equal to ${\mathbf{x}}{\mathbf{y}}^{\ast}$ as before with singular vectors ${\mathbf{u}} = {{\mathbf{x}}/{\|{\mathbf{x}}\|}}$ and ${\mathbf{v}} = {{\mathbf{y}}/{\|{\mathbf{y}}\|}}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "The injectivity property and the connectivity problem", "weight": 1.0} -->

Then all the information about the values of the $x_{i}$'s with $i \in I$ and of the $y_{j}$'s with $j \in J$ are given by the sampled entries connecting $I$ to $J$ since all the other observed entries connect vertices in $I^{c}$ to those in $J^{c}$. Now even if one observes all the entries $x_{i}y_{j}$ with $i \in I$ and $j \in J$, then at least the signs of $x_{i}$, $i \in I$, and of $y_{j}$, $j \in J$, would remain undetermined.

<!-- chunk {"id": "body-0066", "role": "body", "section": "The injectivity property and the connectivity problem", "weight": 1.0} -->

Indeed, if the values ${(x_{i})}_{i \in I}$, ${(y_{j})}_{j \in J}$ are consistent with the observed entries, so are the values ${({- x_{i}})}_{i \in I}$, ${({- y_{j}})}_{j \in J}$. However, since the same analysis holds for the sets $I^{c}$ and $J^{c}$, there are at least two matrices consistent with the observed entries and exact matrix completion is impossible.

<!-- chunk {"id": "body-0067", "role": "body", "section": "The injectivity property and the connectivity problem", "weight": 1.0} -->

When the entries are sampled uniformly at random, it is well known that one needs on the order of $n{\log n}$ samples to obtain a fully connected graph with large probability (see, e.g., ). Remarkably, Theorem 4.1 implies that $\mathcal{P}_{T}\mathcal{P}_{\Omega}\mathcal{P}_{T}$ is invertible---a stronger property---when the number of samples is also on the order of $n{\log n}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Proofs of the Critical Lemmas", "weight": 1.0} -->

Suppose that $b = b'$ and $a \neq a'$, then We have a similar bound when $a = a'$ and $b \neq b'$ whereas when $a \neq a'$ and $b \neq b'$, In short, it follows from this analysis (and from (4.8) for the case where ${(a,b)} = {(a',b')}$) that A consequence of (4.8) is the estimate: which we will apply several times. A related estimate is this: and the same is true by exchanging the role of $a$ and $b$. To see this, write and the conclusion follows from the coherence property.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Proofs of the Critical Lemmas", "weight": 1.0} -->

We will prove the lemmas in the case where $n_{1} = n_{2} = n$ for simplicity, i.e. in the case of square matrices of dimension $n$. The general case is treated in exactly the same way. In fact, the argument only makes use of the bounds (6.2), (6.3) (and sometimes (6.4)), and the general case is obtained by replacing $n$ with $\min{(n_{1},n_{2})}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Proofs of the Critical Lemmas", "weight": 1.0} -->

Each of the following subsections computes the operator norm of some random variable. In each section, we denote $\mathbf{S}$ as the quantity whose norm we wish to analyze. We will also frequently use the notation $\mathbf{H}$ for some auxiliary matrix variable whose norm we will need to bound. Hence, we will reuse the same notation many times rather than introducing a dozens new names---just like in computer programming where one uses the same variable name in distinct routines.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To demonstrate the practical applicability of the nuclear norm heuristic for recovering low-rank matrices from their entries, we conducted a series of numerical experiments for a variety of the matrix sizes $n$, ranks $r$, and numbers of entries $m$. For each $(n,m,r)$ triple, we repeated the following procedure $50$ times. We generated $\mathbf{M}$, an $n \times n$ matrix of rank $r$, by sampling two $n \times r$ factors ${\mathbf{M}}_{L}$ and ${\mathbf{M}}_{R}$ with i.i.d. Gaussian entries and setting ${\mathbf{M}} = {{\mathbf{M}}_{L}{\mathbf{M}}_{R}^{\ast}}$. We sampled a subset $\Omega$ of $m$ entries uniformly at random. Then the nuclear norm minimization was solved using the SDP solver SDPT3.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We declared $\mathbf{M}$ to be recovered if the solution returned by the SDP, ${\mathbf{X}}_{\mathbf{o}\mathbf{p}\mathbf{t}}$, satisfied ${{\|{{\mathbf{X}}_{\mathbf{o}\mathbf{p}\mathbf{t}} - {\mathbf{M}}}\|}_{F}/{\|{\mathbf{M}}\|}_{F}} < 10^{- 3}$. Figure 1 shows the results of these experiments for $n = 40$ and $50$. The $x$-axis corresponds to the fraction of the entries of the matrix that are revealed to the SDP solver. The $y$-axis corresponds to the ratio between the dimension of the set of rank $r$ matrices, $d_{r} = {r{({{2n} - r})}}$, and the number of measurements $m$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Note that both of these axes range from zero to one as a value greater than one on the $x$-axis corresponds to an overdetermined linear system where the semidefinite program always succeeds, and a value of greater than one on the $y$-axis corresponds to a situation where there is always an infinite number of matrices with rank $r$ with the given entries. The color of each cell in the figures reflects the empirical recovery rate of the $50$ runs (scaled between $0$ and $1$). White denotes perfect recovery in all experiments, and black denotes failure for all experiments. Interestingly, the experiments reveal very similar plots for different $n$, suggesting that our asymptotic conditions for recovery may be rather conservative.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

For a second experiment, we generated random *positive semidefinite* matrices and tried to recover them from their entries using the nuclear norm heuristic. As above, we repeated the same procedure $50$ times for each $(n,m,r)$ triple. We generated $\mathbf{M}$, an $n \times n$ positive semidefinite matrix of rank $r$, by sampling an $n \times r$ factor ${\mathbf{M}}_{F}$ with i.i.d. Gaussian entries and setting ${\mathbf{M}} = {{\mathbf{M}}_{F}{\mathbf{M}}_{F}^{\ast}}$. We sampled a subset $\Omega$ of $m$ entries uniformly at random.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Then we solved the nuclear norm minimization problem As above, we declared $\mathbf{M}$ to be recovered if ${{\|{{\mathbf{X}}_{\mathbf{o}\mathbf{p}\mathbf{t}} - {\mathbf{M}}}\|}_{F}/{\|{\mathbf{M}}\|}_{F}} < 10^{- 3}$. Figure 2 shows the results of these experiments for $n = 40$ and $50$. The $x$-axis again corresponds to the fraction of the entries of the matrix that are revealed to the SDP solver, but, in this case, the number of measurements is divided by $D_{n} = {{n{({n + 1})}}/2}$, the number of unique entries in a positive-semidefinite matrix and the dimension of the rank $r$ matrices is $d_{r} = {{nr} - {{r{({r - 1})}}/2}}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The color of each cell is chosen in the same fashion as in the experiment with full matrices. Interestingly, the recovery region is much larger for positive semidefinite matrices, and future work is needed to investigate if the theoretical scaling is also more favorable in this scenario of low-rank matrix completion.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Finally, in Figure 3, we plot the performance of the nuclear norm heuristic when recovering low-rank matrices from Gaussian projections of these matrices. In these cases, $\mathbf{M}$ was generated in the same fashion as above, but, in place of sampling entries, we generated $m$ random Gaussian projections of the data (see the discussion in Section 1.4). Then we solved the optimization with the additional constraint that ${\mathbf{X}} \succeq 0$ in the positive semidefinite case. Here $\mathcal{A}{({\mathbf{X}})}$ denotes a linear map of the form (1.15) where the entries are sampled i.i.d. from a zero-mean unit variance Gaussian distribution. In these experiments, the recovery regime is far larger than in the case of that of sampling entries, but this is not particularly surprising as each Gaussian observation measures a contribution from every entry in the matrix $\mathbf{M}$. These Gaussian models were studied extensively.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Improvements", "weight": 1.0} -->

In this paper, we have shown that under suitable conditions, one can reconstruct an $n \times n$ matrix of rank $r$ from a small number of its sampled entries provided that this number is on the order of $n^{1.2}r{\log n}$, at least for moderate values of the rank. One would like to know whether better results hold in the sense that exact matrix recovery would be guaranteed with a reduced number of measurements. In particular, recall that an $n \times n$ matrix of rank $r$ depends on ${({{2n} - r})}r$ degrees of freedom; is it true then that it is possible to recover most low-rank matrices from on the order of $nr$---up to logarithmic multiplicative factors---randomly selected entries? Can the sample size be merely proportional to the true complexity of the low-rank object we wish to recover?

<!-- chunk {"id": "body-0079", "role": "body", "section": "Improvements", "weight": 1.0} -->

In this direction, we would like to emphasize that there is nothing in our approach that apparently prevents us from getting stronger results. Indeed, we developed a bound on the spectral norm of each of the first four terms ${({\mathcal{P}_{T^{\perp}}\mathcal{P}_{\Omega}\mathcal{P}_{T}})}\mathcal{H}^{k}{(E)}$ in the series (4.13) (corresponding to values of $k$ equal to $0,1,2,3$) and used a general argument to bound the remainder of the series. Presumably, one could bound higher order terms by the same techniques. Getting an appropriate bound on $\|{{({\mathcal{P}_{T^{\perp}}\mathcal{P}_{\Omega}\mathcal{P}_{T}})}\mathcal{H}^{4}{(E)}}\|$ would lower the exponent of $n$ from $6/5$ to $7/6$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Improvements", "weight": 1.0} -->

The appropriate bound on $\|{{({\mathcal{P}_{T^{\perp}}\mathcal{P}_{\Omega}\mathcal{P}_{T}})}\mathcal{H}^{5}{(E)}}\|$ would further lower the exponent to $8/7$, and so. To obtain an optimal result, one would need to reach $k$ of size about $\log n$. In doing so, however, one would have to pay special attention to the size of the decoupling constants (the constant $C_{D}$ for two variables in Lemma 6.5) which depend on $k$---the number of decoupled variables. These constants grow with $k$ and upper bounds are known.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Further directions", "weight": 1.0} -->

It would be of interest to extend our results to the case where the unknown matrix is approximately low-rank. Suppose we write the SVD of a matrix $\mathbf{M}$ as where $\sigma_{1} \geq \sigma_{2} \geq \ldots \geq \sigma_{n} \geq 0$ and assume for simplicity that none of the $\sigma_{k}$'s vanish. In general, it is impossible to complete such a matrix exactly from a partial subset of its entries. However, one might hope to be able to recover a good approximation if, for example, most of the singular values are small or negligible. For instance, consider the truncated SVD of the matrix $\mathbf{M}$, where the sum extends over the $r$ largest singular values and let ${\mathbf{M}}_{\star}$ be the solution to (1.5).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Further directions", "weight": 1.0} -->

Then one would not expect to have ${\mathbf{M}}_{\star} = {\mathbf{M}}$ but it would be of great interest to determine whether the size of ${\mathbf{M}}_{\star} - {\mathbf{M}}$ is comparable to that of ${\mathbf{M}} - {\mathbf{M}}_{r}$ provided that the number of sampled entries is sufficiently large. For example, one would like to know whether it is reasonable to expect that ${\|{{\mathbf{M}}_{\star} - {\mathbf{M}}}\|}_{\ast}$ is on the same order as ${\|{{\mathbf{M}} - {\mathbf{M}}_{r}}\|}_{\ast}$ (one could ask for a similar comparison with a different norm). If the answer is positive, then this would say that approximately low-rank matrices can be accurately recovered from a small set of sampled entries.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Further directions", "weight": 1.0} -->

Another important direction is to determine whether the reconstruction is robust to noise as in some applications, one would presumably observe where $z$ is a deterministic or stochastic perturbation. In this setup, one would perhaps want to minimize the nuclear norm subject to ${\|{\mathcal{P}_{\Omega}{({{\mathbf{X}} - {\mathbf{Y}}})}}\|}_{F} \leq \epsilon$ where $\epsilon$ is an upper bound on the noise level instead of enforcing the equality constraint ${\mathcal{P}_{\Omega}{({\mathbf{X}})}} = {\mathcal{P}_{\Omega}{({\mathbf{Y}})}}$. Can one expect that this algorithm or a variation thereof provides accurate answers? That is, can one expect that the error between the recovered and the true data matrix be proportional to the noise level?
