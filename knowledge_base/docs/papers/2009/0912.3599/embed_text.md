## Introduction

### Motivation

Suppose we are given a large data matrix $M$, and know that it may be decomposed as

where $L_{0}$ has low-rank and $S_{0}$ is sparse; here, both components are of arbitrary magnitude. We do not know the low-dimensional column and row space of $L_{0}$, not even their dimension. Similarly, we do not know the locations of the nonzero entries of $S_{0}$, not even how many there are. Can we hope to recover the low-rank and sparse components both accurately (perhaps even exactly) and efficiently?

A provably correct and scalable solution to the above problem would presumably have an impact on today's data-intensive scientific discovery.^11^1Data-intensive computing is advocated by Jim Gray as the fourth paradigm for scientific discovery. The recent explosion of massive amounts of high-dimensional data in science, engineering, and society presents a challenge as well as an opportunity to many areas such as image, video, multimedia processing, web relevancy data analysis, search, biomedical imaging and bioinformatics. In such application domains, data now routinely lie in thousands or even billions of dimensions, with a number of samples sometimes of the same order of magnitude.

To alleviate the curse of dimensionality and scale,^22^2We refer to either the complexity of algorithms that increases drastically as dimension increases, or to their performance that decreases sharply when scale goes up. we must leverage on the fact that such data have low intrinsic dimensionality, e.g. that they lie on some low-dimensional subspace, are sparse in some basis, or lie on some low-dimensional manifold. Perhaps the simplest and most useful assumption is that the data all lie near some low-dimensional subspace. More precisely, this says that if we stack all the data points as column vectors of a matrix $M$, the matrix should have (approximately) low-rank: mathematically,

where $L_{0}$ has low-rank and $N_{0}$ is a small perturbation matrix. Classical Principal Component Analysis (PCA) seeks the best (in an $\ell^{2}$ sense) rank-$k$ estimate of $L_{0}$ by solving

(Throughout the paper, $\| M\|$ denotes the $2$-norm; that is, the largest singular value of $M$.) This problem can be efficiently solved via the singular value decomposition (SVD) and enjoys a number of optimality properties when the noise $N_{0}$ is small and i.i.d. Gaussian.

### Robust PCA

PCA is arguably the most widely used statistical tool for data analysis and dimensionality reduction today. However, its brittleness with respect to grossly corrupted observations often puts its validity in jeopardy -- a single grossly corrupted entry in $M$ could render the estimated $\hat{L}$ arbitrarily far from the true $L_{0}$. Unfortunately, gross errors are now ubiquitous in modern applications such as image processing, web data analysis, and bioinformatics, where some measurements may be arbitrarily corrupted (due to occlusions, malicious tampering, or sensor failures) or simply irrelevant to the low-dimensional structure we seek to identify. A number of natural approaches to robustifying PCA have been explored and proposed in the literature over several decades. The representative approaches include influence function techniques, multivariate trimming, alternating minimization, and random sampling techniques. Unfortunately, none of these existing approaches yields a polynomial-time algorithm with strong performance guarantees under broad conditions^33^3Random sampling approaches guarantee near-optimal estimates, but have complexity exponential in the rank of the matrix $L_{0}$. Trimming algorithms have comparatively lower computational complexity, but guarantee only locally optimal solutions.. The new problem we consider here can be considered as an idealized version of Robust PCA, in which we aim to recover a low-rank matrix $L_{0}$ from highly corrupted measurements $M = {L_{0} + S_{0}}$. Unlike the small noise term $N_{0}$ in classical PCA, the entries in $S_{0}$ can have arbitrarily large magnitude, and their support is assumed to be sparse but unknown^44^4The unknown support of the errors makes the problem more difficult than the matrix completion problem that has been recently much studied..

### Applications

There are many important applications in which the data under study can naturally be modeled as a low-rank plus a sparse contribution. All the statistical applications, in which robust principal components are sought, of course fit our model. Below, we give examples inspired by contemporary challenges in computer science, and note that depending on the applications, either the low-rank component or the sparse component could be the object of interest:

Video Surveillance. Given a sequence of surveillance video frames, we often need to identify activities that stand out from the background. If we stack the video frames as columns of a matrix $M$, then the low-rank component $L_{0}$ naturally corresponds to the stationary background and the sparse component $S_{0}$ captures the moving objects in the foreground. However, each image frame has thousands or tens of thousands of pixels, and each video fragment contains hundreds or thousands of frames. It would be impossible to decompose $M$ in such a way unless we have a truly scalable solution to this problem. In Section 4, we will show the results of our algorithm on video decomposition.

Face Recognition. It is well known that images of a convex, Lambertian surface under varying illuminations span a low-dimensional subspace. This fact has been a main reason why low-dimensional models are mostly effective for imagery data. In particular, images of a human's face can be well-approximated by a low-dimensional subspace. Being able to correctly retrieve this subspace is crucial in many applications such as face recognition and alignment. However, realistic face images often suffer from self-shadowing, specularities, or saturations in brightness, which make this a difficult task and subsequently compromise the recognition performance. In Section 4, we will show how our method is able to effectively remove such defects in face images.

Latent Semantic Indexing. Web search engines often need to analyze and index the content of an enormous corpus of documents. A popular scheme is the Latent Semantic Indexing (LSI). The basic idea is to gather a document-versus-term matrix $M$ whose entries typically encode the relevance of a term (or a word) to a document such as the frequency it appears in the document (e.g. the TF/IDF). PCA (or SVD) has traditionally been used to decompose the matrix as a low-rank part plus a residual, which is not necessarily sparse (as we would like). If we were able to decompose $M$ as a sum of a low-rank component $L_{0}$ and a sparse component $S_{0}$, then $L_{0}$ could capture common words used in all the documents while $S_{0}$ captures the few key words that best distinguish each document from others.

Ranking and Collaborative Filtering. The problem of anticipating user tastes is gaining increasing importance in online commerce and advertisement. Companies now routinely collect user rankings for various products, e.g., movies, books, games, or web tools, among which the Netflix Prize for movie ranking is the best known. The problem is to use incomplete rankings provided by the users on some of the products to predict the preference of any given user on any of the products. This problem is typically cast as a low-rank matrix completion problem. However, as the data collection process often lacks control or is sometimes even ad hoc -- a small portion of the available rankings could be noisy and even tampered with. The problem is more challenging since we need to simultaneously complete the matrix and correct the errors. That is, we need to infer a low-rank matrix $L_{0}$ from a set of incomplete and corrupted entries. In Section 1.6, we will see how our results can be extended to this situation.

Similar problems also arise in many other applications such as graphical model learning, linear system identification, and coherence decomposition in optical systems, as discussed in. All in all, the new applications we have listed above require solving the low-rank and sparse decomposition problem for matrices of extremely high dimension and under much broader conditions, a goal this paper aims to achieve.

### A surprising message

At first sight, the separation problem seems impossible to solve since the number of unknowns to infer for $L_{0}$ and $S_{0}$ is twice as many as the given measurements in $M \in {\mathbb{R}}^{n_{1} \times n_{2}}$. Furthermore, it seems even more daunting that we expect to reliably obtain the low-rank matrix $L_{0}$ with errors in $S_{0}$ of arbitrarily large magnitude.

In this paper, we are going to see that very surprisingly, not only can this problem be solved, it can be solved by tractable convex optimization. Let ${\| M\|}_{\ast}:={\sum_{i}{\sigma_{i}{(M)}}}$ denote the nuclear norm of the matrix $M$, i.e. the sum of the singular values of $M$, and let ${\| M\|}_{1} = {\sum_{ij}{|M_{ij}|}}$ denote the $\ell_{1}$-norm of $M$ seen as a long vector in ${\mathbb{R}}^{n_{1} \times n_{2}}$. Then we will show that under rather weak assumptions, the Principal Component Pursuit (PCP) estimate solving^55^5Although the name naturally suggests an emphasis on the recovery of the low-rank component, we reiterate that in some applications, the sparse component truly is the object of interest.

exactly recovers the low-rank $L_{0}$ and the sparse $S_{0}$. Theoretically, this is guaranteed to work even if the rank of $L_{0}$ grows almost linearly in the dimension of the matrix, and the errors in $S_{0}$ are up to a constant fraction of all entries. Algorithmically, we will see that the above problem can be solved by efficient and scalable algorithms, at a cost not so much higher than the classical PCA. Empirically, our simulations and experiments suggest this works under surprisingly broad conditions for many types of real data. In Section 1.5, we will comment on the similar approach taken in the paper, which was released during the preparation of this manuscript.

### When does separation make sense?

A normal reaction is that the objectives of this paper cannot be met. Indeed, there seems to not be enough information to perfectly disentangle the low-rank and the sparse components. And indeed, there is some truth to this, since there obviously is an identifiability issue. For instance, suppose the matrix $M$ is equal to $e_{1}e_{1}^{\ast}$ (this matrix has a one in the top left corner and zeros everywhere else). Then since $M$ is both sparse and low-rank, how can we decide whether it is low-rank or sparse? To make the problem meaningful, we need to impose that the low-rank component $L_{0}$ is not sparse. In this paper, we will borrow the general notion of incoherence introduced in for the matrix completion problem; this is an assumption concerning the singular vectors of the low-rank component. Write the singular value decomposition of $L_{0} \in {\mathbb{R}}^{n_{1} \times n_{2}}$ as

where $r$ is the rank of the matrix, $\sigma_{1},\ldots,\sigma_{r}$ are the positive singular values, and $U = {\lbrack u_{1},\ldots,u_{r}\rbrack}$, $V = {\lbrack v_{1},\ldots,v_{r}\rbrack}$ are the matrices of left- and right-singular vectors. Then the incoherence condition with parameter $\mu$ states that

Here and below, ${\| M\|}_{\infty} = {\max_{i,j}{|M_{ij}|}}$, i.e. is the $\ell_{\infty}$ norm of $M$ seen as a long vector. Note that since the orthogonal projection $P_{U}$ onto the column space of $U$ is given by $P_{U} = {UU^{\ast}}$, (1.2) is equivalent to ${\max_{i}{\|{P_{U}e_{i}}\|}^{2}} \leq {{\mur}/n_{1}}$, and similarly for $P_{V}$. As discussed in earlier references, the incoherence condition asserts that for small values of $\mu$, the singular vectors are reasonably spread out -- in other words, not sparse.

Another identifiability issue arises if the sparse matrix has low-rank. This will occur if, say, all the nonzero entries of $S$ occur in a column or in a few columns. Suppose for instance, that the first column of $S_{0}$ is the opposite of that of $L_{0}$, and that all the other columns of $S_{0}$ vanish. Then it is clear that we would not be able to recover $L_{0}$ and $S_{0}$ by any method whatsoever since $M = {L_{0} + S_{0}}$ would have a column space equal to, or included in that of $L_{0}$. To avoid such meaningless situations, we will assume that the sparsity pattern of the sparse component is selected uniformly at random.

### Main result

The surprise is that under these minimal assumptions, the simple PCP solution perfectly recovers the low-rank and the sparse components, provided of course that the rank of the low-rank component is not too large, and that the sparse component is reasonably sparse. Below, $n_{} = {\text{max}{(n_{1},n_{2})}}$ and $n_{} = {\text{min}{(n_{1},n_{2})}}$.

### Theorem 1.1

Suppose $L_{0}$ is $n \times n$, obeys (1.2)--(1.3), and that the support set of $S_{0}$ is uniformly distributed among all sets of cardinality $m$. Then there is a numerical constant $c$ such that with probability at least $1 - {cn^{- 10}}$ (over the choice of support of $S_{0}$), Principal Component Pursuit (1.1) with $\lambda = {1/\sqrt{n}}$ is exact, i.e. $\hat{L} = L_{0}$ and $\hat{S} = S_{0}$, provided that

Above, $\rho_{r}$ and $\rho_{s}$ are positive numerical constants. In the general rectangular case where $L_{0}$ is $n_{1} \times n_{2}$, PCP with $\lambda = {1/\sqrt{n_{}}}$ succeeds with probability at least $1 - {cn_{}^{- 10}}$, provided that ${{rank}{(L_{0})}} \leq {\rho_{r}n_{}\mu^{- 1}{({\log n_{}})}^{- 2}}$ and $m \leq {\rho_{s}n_{1}n_{2}}$.

In other words, matrices $L_{0}$ whose singular vectors---or principal components---are reasonably spread can be recovered with probability nearly one from arbitrary and completely unknown corruption patterns (as long as these are randomly distributed). In fact, this works for large values of the rank, i.e. on the order of $n/{({\log n})}^{2}$ when $\mu$ is not too large. We would like to emphasize that the only 'piece of randomness' in our assumptions concerns the locations of the nonzero entries of $S_{0}$; everything else is deterministic. In particular, all we require about $L_{0}$ is that its singular vectors are not spiky. Also, we make no assumption about the magnitudes or signs of the nonzero entries of $S_{0}$. To avoid any ambiguity, our model for $S_{0}$ is this: take an arbitrary matrix $S$ and set to zero its entries on the random set $\Omega^{c}$; this gives $S_{0}$.

A rather remarkable fact is that there is no tuning parameter in our algorithm. Under the assumption of the theorem, minimizing

always returns the correct answer. This is surprising because one might have expected that one would have to choose the right scalar $\lambda$ to balance the two terms in ${\| L\|}_{\ast} + {\lambda{\| S\|}_{1}}$ appropriately (perhaps depending on their relative size). This is, however, clearly not the case. In this sense, the choice $\lambda = {1/\sqrt{n_{}}}$ is universal. Further, it is not a priori very clear why $\lambda = {1/\sqrt{n_{}}}$ is a correct choice no matter what $L_{0}$ and $S_{0}$ are. It is the mathematical analysis which reveals the correctness of this value. In fact, the proof of the theorem gives a whole range of correct values, and we have selected a sufficiently simple value in that range.

Another comment is that one can obtain results with larger probabilities of success, i.e. of the form $1 - {O{(n^{- \beta})}}$ (or $1 - {O{(n_{}^{- \beta})}}$) for $\beta > 0$ at the expense of reducing the value of $\rho_{r}$.

### Connections with prior work and innovations

The last year or two have seen the rapid development of a scientific literature concerned with the matrix completion problem introduced in, see also and the references therein. In a nutshell, the matrix completion problem is that of recovering a low-rank matrix from only a small fraction of its entries, and by extension, from a small number of linear functionals. Although other methods have been proposed, the method of choice is to use convex optimization: among all the matrices consistent with the data, simply find that with minimum nuclear norm. The papers cited above all prove the mathematical validity of this approach, and our mathematical analysis borrows ideas from this literature, and especially from those pioneered in. Our methods also much rely on the powerful ideas and elegant techniques introduced by David Gross in the context of quantum-state tomography. In particular, the clever golfing scheme plays a crucial role in our analysis, and we introduce two novel modifications to this scheme.

Despite these similarities, our ideas depart from the literature on matrix completion on several fronts. First, our results obviously are of a different nature. Second, we could think of our separation problem, and the recovery of the low-rank component, as a matrix completion problem. Indeed, instead of having a fraction of observed entries available and the other missing, we have a fraction available, but do not know which one, while the other is not missing but entirely corrupted altogether. Although, this is a harder problem, one way to think of our algorithm is that it simultaneously detects the corrupted entries, and perfectly fits the low-rank component to the remaining entries that are deemed reliable. In this sense, our methodology and results go beyond matrix completion. Third, we introduce a novel de-randomization argument that allows us to fix the signs of the nonzero entries of the sparse component. We believe that this technique will have many applications. One such application is in the area of compressive sensing, where assumptions about the randomness of the signs of a signal are common, and merely made out of convenience rather than necessity; this is important because assuming independent signal signs may not make much sense for many practical applications when the involved signals can all be non-negative (such as images).

We mentioned earlier the related work, which also considers the problem of decomposing a given data matrix into sparse and low-rank components, and gives sufficient conditions for convex programming to succeed. These conditions are phrased in terms of two quantities. The first is the maximum ratio between the $\ell_{\infty}$ norm and the operator norm, restricted to the subspace generated by matrices whose row or column spaces agree with those of $L_{0}$. The second is the maximum ratio between the operator norm and the $\ell_{\infty}$ norm, restricted to the subspace of matrices that vanish off the support of $S_{0}$. Chandrasekaran et. al. show that when the product of these two quantities is small, then the recovery is exact for a certain interval of the regularization parameter.

One very appealing aspect of this condition is that it is completely deterministic: it does not depend on any random model for $L_{0}$ or $S_{0}$. It yields a corollary that can be easily compared to our result: suppose $n_{1} = n_{2} = n$ for simplicity, and let $\mu_{0}$ be the smallest quantity satisfying (1.2), then correct recovery occurs whenever

The left-hand side is at least as large as $\rho_{s}\sqrt{\mu_{0}nr}$, where $\rho_{s}$ is the fraction of entries of $S_{0}$ that are nonzero. Since $\mu_{0} \geq 1$ always, this statement only guarantees recovery if $\rho_{s} = {O{({({nr})}^{- {1/2}})}}$; i.e., even when ${{rank}{(L_{0})}} = {O{}}$, only vanishing fractions of the entries in $S_{0}$ can be nonzero.

In contrast, our result shows that for incoherent $L_{0}$, correct recovery occurs with high probability for ${rank}{(L_{0})}$ on the order of $n/{\lbrack{\mu{\log^{2}n}}\rbrack}$ and a number of nonzero entries in $S_{0}$ on the order of $n^{2}$. That is, matrices of large rank can be recovered from non-vanishing fractions of sparse errors. This improvement comes at the expense of introducing one piece of randomness: a uniform model on the error support.^66^6Notice that the bound of depends only on the support of $S_{0}$, and hence can be interpreted as a worst case result with respect to the signs of $S_{0}$. In contrast, our result does not randomize over the signs, but does assume that they are sampled from a fixed sign pattern. Although we do not pursue it here due to space limitations, our analysis also yields a result which holds for worst case sign patterns, and guarantees correct recovery with ${{rank}{(L_{0})}} = {O{}}$, and a sparsity pattern of cardinality $\rhon_{1}n_{2}$ for some $\rho > 0$.

Our analysis has one additional advantage, which is of significant practical importance: it identifies a simple, non-adaptive choice of the regularization parameter $\lambda$. In contrast, the conditions on the regularization parameter given by Chandrasekaran et al. depend on quantities which in practice are not known a-priori. The experimental section of suggests searching for the correct $\lambda$ by solving many convex programs. Our result, on the other hand, demonstrates that the simple choice $\lambda = {1/\sqrt{n}}$ works with high probability for recovering any square incoherent matrix.

### Implications for matrix completion from grossly corrupted data

We have seen that our main result asserts that it is possible to recover a low-rank matrix even though a significant fraction of its entries are corrupted. In some applications, however, some of the entries may be missing as well, and this section addresses this situation. Let $\mathcal{P}_{\Omega}$ be the orthogonal projection onto the linear space of matrices supported on $\Omega \subset {{\lbrack n_{1}\rbrack} \times {\lbrack n_{2}\rbrack}}$,

Then imagine we only have available a few entries of $L_{0} + S_{0}$, which we conveniently write as

that is, we see only those entries ${(i,j)} \in \Omega_{\text{obs}} \subset {{\lbrack n_{1}\rbrack} \times {\lbrack n_{2}\rbrack}}$. This models the following problem: we wish to recover $L_{0}$ but only see a few entries about $L_{0}$, and among those a fraction happens to be corrupted, and we of course do not know which one. As is easily seen, this is a significant extension of the matrix completion problem, which seeks to recover $L_{0}$ from undersampled but otherwise perfect data $\mathcal{P}_{\Omega_{\text{obs}}}L_{0}$.

We propose recovering $L_{0}$ by solving the following problem:

In words, among all decompositions matching the available data, Principal Component Pursuit finds the one that minimizes the weighted combination of the nuclear norm, and of the $\ell_{1}$ norm. Our observation is that under some conditions, this simple approach recovers the low-rank component exactly. In fact, the techniques developed in this paper establish this result:

### Theorem 1.2

Suppose $L_{0}$ is $n \times n$, obeys the conditions (1.2)--(1.3), and that $\Omega_{\text{obs}}$ is uniformly distributed among all sets of cardinality $m$ obeying $m = {0.1n^{2}}$. Suppose for simplicity, that each observed entry is corrupted with probability $\tau$ independently of the others. Then there is a numerical constant $c$ such that with probability at least $1 - {cn^{- 10}}$, Principal Component Pursuit (1.5) with $\lambda = {1/\sqrt{0.1n}}$ is exact, i.e. $\hat{L} = L_{0}$, provided that

Above, $\rho_{r}$ and $\tau_{s}$ are positive numerical constants. For general $n_{1} \times n_{2}$ rectangular matrices, PCP with $\lambda = {1/\sqrt{0.1n_{}}}$ succeeds from $m = {0.1n_{1}n_{2}}$ corrupted entries with probability at least $1 - {cn_{}^{- 10}}$, provided that ${{rank}{(L_{0})}} \leq {\rho_{r}n_{}\mu^{- 1}{({\log n_{}})}^{- 2}}$.

In short, perfect recovery from incomplete and corrupted entries is possible by convex optimization.

On the one hand, this result extends our previous result in the following way. If all the entries are available, i.e. $m = {n_{1}n_{2}}$, then this is Theorem 1.1. On the other hand, it extends matrix completion results. Indeed, if $\tau = 0$, we have a pure matrix completion problem from about a fraction of the total number of entries, and our theorem guarantees perfect recovery as long as $r$ obeys (1.6), which for large values of $r$, matches the strongest results available. We remark that the recovery is exact, however, via a different algorithm. To be sure, in matrix completion one typically minimizes the nuclear norm ${\| L\|}_{\ast}$ subject to the constraint ${\mathcal{P}_{\Omega_{\text{obs}}}L} = {\mathcal{P}_{\Omega_{\text{obs}}}L_{0}}$. Here, our program would solve

and return $\hat{L} = L_{0}$, $\hat{S} = 0$! In this context, Theorem 1.2 proves that matrix completion is stable vis a vis gross errors.

### Remark

We have stated Theorem 1.2 merely to explain how our ideas can easily be adapted to deal with low-rank matrix recovery problems from undersampled and possibly grossly corrupted data. In our statement, we have chosen to see 10% of the entries but, naturally, similar results hold for all other positive fractions provided that they are large enough. We would like to make it clear that a more careful study is likely to lead to a stronger version of Theorem 1.2. In particular, for very low rank matrices, we expect to see similar results holding with far fewer observations; that is, in the limit of large matrices, from a decreasing fraction of entries. In fact, our techniques would already establish such sharper results but we prefer not to dwell on such refinements at the moment, and leave this up for future work.

### Notation

We provide a brief summary of the notations used throughout the paper. We shall use five norms of a matrix. The first three are functions of the singular values and they are: 1) the operator norm or $2$-norm denoted by $\| X\|$; 2) the Frobenius norm denoted by ${\| X\|}_{F}$; and 3) the nuclear norm denoted by ${\| X\|}_{\ast}$. The last two are the $\ell_{1}$ and $\ell_{\infty}$ norms of a matrix seen as a long vector, and are denoted by ${\| X\|}_{1}$ and ${\| X\|}_{\infty}$ respectively. The Euclidean inner product between two matrices is defined by the formula ${\langle X,Y\rangle}:={{trace}{({X^{\ast}Y})}}$, so that ${\| X\|}_{F}^{2} = {\langle X,X\rangle}$.

Further, we will also manipulate linear transformations which act on the space of matrices, and we will use calligraphic letters for these operators as in $\mathcal{P}_{\Omega}X$. We shall also abuse notation by also letting $\Omega$ be the linear space of matrices supported on $\Omega$. Then $\mathcal{P}_{\Omega^{\perp}}$ denotes the projection onto the space of matrices supported on $\Omega^{c}$ so that $\mathcal{I} = {\mathcal{P}_{\Omega} + \mathcal{P}_{\Omega^{\perp}}}$, where $\mathcal{I}$ is the identity operator. We will consider a single norm for these, namely, the operator norm (the top singular value) denoted by $\|\mathcal{A}\|$, which we may want to think of as ${\|\mathcal{A}\|} = {\sup_{\{{{\| X\|}_{F} = 1}\}}{\|{\mathcal{A}X}\|}_{F}}$; for instance, ${\|\mathcal{P}_{\Omega}\|} = 1$ whenever $\Omega \neq \varnothing$.

### Organization of the paper

The paper is organized as follows. In Section 2, we provide the key steps in the proof of Theorem 1.1. This proof depends upon on two critical properties of dual certificates, which are established in the separate Section 3. The reason why this is separate is that in a first reading, the reader might want to jump to Section 4, which presents applications to video surveillance, and computer vision. Section 5 introduces algorithmic ideas to find the Principal Component Pursuit solution when $M$ is of very large scale. We conclude the paper with a discussion about future research directions in Section 6. Finally, the proof of Theorem 1.2 is in the Appendix, Section 7, together with those of intermediate results.

## Architecture of the Proof

This section introduces the key steps underlying the proof of our main result, Theorem 1.1. We will prove the result for square matrices for simplicity, and write $n = n_{1} = n_{2}$. Of course, we shall indicate where the argument needs to be modified to handle the general case. Before we start, it is helpful to review some basic concepts and introduce additional notation that shall be used throughout. For a given scalar $x$, we denote by $\text{sgn}{(x)}$ the sign of $x$, which we take to be zero if $x = 0$. By extension, $\text{sgn}{(S)}$ is the matrix whose entries are the signs of those of $S$. We recall that any subgradient of the $\ell_{1}$ norm at $S_{0}$ supported on $\Omega$, is of the form

where $F$ vanishes on $\Omega$, i.e. ${\mathcal{P}_{\Omega}F} = 0$, and obeys ${\| F\|}_{\infty} \leq 1$.

We will also manipulate the set of subgradients of the nuclear norm. From now on, we will assume that $L_{0}$ of rank $r$ has the singular value decomposition $U\SigmaV^{\ast}$, where ${U,V} \in {\mathbb{R}}^{n \times r}$ just as in Section 1.3. Then any subgradient of the nuclear norm at $L_{0}$ is of the form

where ${U^{\ast}W} = 0$, ${WV} = 0$ and ${\| W\|} \leq 1$. Denote by $T$ the linear space of matrices

and by $T^{\perp}$ its orthogonal complement. It is not hard to see that taken together, ${U^{\ast}W} = 0$ and ${WV} = 0$ are equivalent to ${\mathcal{P}_{T}W} = 0$, where $\mathcal{P}_{T}$ is the orthogonal projection onto $T$. Another way to put this is ${\mathcal{P}_{T^{\perp}}W} = W$. In passing, note that for any matrix $M$, ${\mathcal{P}_{T^{\perp}}M} = {{({I - {UU^{\ast}}})}M{({I - {VV^{\ast}}})}}$, where we recognize that $I - {UU^{\ast}}$ is the projection onto the orthogonal complement of the linear space spanned by the columns of $U$ and likewise for $({I - {VV^{\ast}}})$. A consequence of this simple observation is that for any matrix $M$, ${\|{\mathcal{P}_{T^{\perp}}M}\|} \leq {\| M\|}$, a fact that we will use several times in the sequel. Another consequence is that for any matrix of the form $e_{i}e_{j}^{\ast}$,

where we have assumed ${{\mur}/n} \leq 1$. Since ${{\|{\mathcal{P}_{T}e_{i}e_{j}^{\ast}}\|}_{F}^{2} + {\|{\mathcal{P}_{T^{\perp}}e_{i}e_{j}^{\ast}}\|}_{F}^{2}} = 1$, this gives

For rectangular matrices, the estimate is ${\|{\mathcal{P}_{T}e_{i}e_{j}^{\ast}}\|}_{F} \leq \sqrt{\frac{2\mur}{\min{(n_{1},n_{2})}}}$.

Finally, in the sequel we will write that an event holds with high or large probability whenever it holds with probability at least $1 - {O{(n^{- 10})}}$ (with $n_{}$ in place of $n$ for rectangular matrices).

### An elimination theorem

We begin with a useful definition and an elementary result we shall use a few times.

### Definition 2.1

We will say that $S^{\prime}$ is a trimmed version of $S$ if ${\text{supp}{(S^{\prime})}} \subset {\text{supp}{(S)}}$ and $S_{ij}^{\prime} = S_{ij}$ whenever $S_{ij}^{\prime} \neq 0$.

In words, a trimmed version of $S$ is obtained by setting some of the entries of $S$ to zero. Having said this, the following intuitive theorem asserts that if Principal Component Pursuit correctly recovers the low-rank and sparse components of $M_{0} = {L_{0} + S_{0}}$, it also correctly recovers the components of a matrix $M_{0}^{\prime} = {L_{0} + S_{0}^{\prime}}$ where $S_{0}^{\prime}$ is a trimmed version of $S_{0}$. This is intuitive since the problem is somehow easier as there are fewer things to recover.

### Theorem 2.2

Suppose the solution to (1.1) with input data $M_{0} = {L_{0} + S_{0}}$ is unique and exact, and consider $M_{0}^{\prime} = {L_{0} + S_{0}^{\prime}}$, where $S_{0}^{\prime}$ is a trimmed version of $S_{0}$. Then the solution to (1.1) with input $M_{0}^{\prime}$ is exact as well.

Proof Write $S_{0}^{\prime} = {\mathcal{P}_{\Omega_{0}}S_{0}}$ for some $\Omega_{0} \subset {{\lbrack n\rbrack} \times {\lbrack n\rbrack}}$ and let $(\hat{L},\hat{S})$ be the solution of (1.1) with input $L_{0} + S_{0}^{\prime}$. Then

Note that $(\hat{L},{\hat{S} + {\mathcal{P}_{\Omega_{0}^{\perp}}S_{0}}})$ is feasible for the problem with input data $L_{0} + S_{0}$, and since ${\|{\hat{S} + {\mathcal{P}_{\Omega_{0}^{\perp}}S_{0}}}\|}_{1} \leq {{\|\hat{S}\|}_{1} + {\|{\mathcal{P}_{\Omega_{0}^{\perp}}S_{0}}\|}_{1}}$, we have

The right-hand side, however, is the optimal value, and by unicity of the optimal solution, we must have $\hat{L} = L_{0}$, and ${\hat{S} + {\mathcal{P}_{\Omega_{0}^{\perp}}S_{0}}} = S_{0}$ or $\hat{S} = {\mathcal{P}_{\Omega_{0}}S_{0}} = S_{0}^{\prime}$. This proves the claim.

### The Bernoulli model

In Theorem 1.1, probability is taken with respect to the uniformly random subset $\Omega = {\{{(i,j)}:{S_{ij} \neq 0}\}}$ of cardinality $m$. In practice, it is a little more convenient to work with the Bernoulli model $\Omega = {\{{(i,j)}:{\delta_{ij} = 1}\}}$, where the $\delta_{ij}$'s are i.i.d. variables Bernoulli taking value one with probability $\rho$ and zero with probability $1 - \rho$, so that the expected cardinality of $\Omega$ is $\rhon^{2}$. From now on, we will write $\Omega \sim {\text{Ber}{(\rho)}}$ as a shorthand for $\Omega$ is sampled from the Bernoulli model with parameter $\rho$.

Since by Theorem 2.2, the success of the algorithm is monotone in $|\Omega|$, any guarantee proved for the Bernoulli model holds for the uniform model as well, and vice versa, if we allow for a vanishing shift in $\rho$ around $m/n^{2}$. The arguments underlying this equivalence are standard, see, and may be found in the Appendix for completeness.

### Derandomization

In Theorem 1.1, the values of the nonzero entries of $S_{0}$ are fixed. It turns out that it is easier to prove the theorem under a stronger assumption, which assumes that the signs of the nonzero entries are independent symmetric Bernoulli variables, i.e. take the value $\pm 1$ with probability $1/2$ (independently of the choice of the support set). The convenient theorem below shows that establishing the result for random signs is sufficient to claim a similar result for fixed signs.

### Theorem 2.3

Suppose $L_{0}$ obeys the conditions of Theorem 1.1 and that the locations of the nonzero entries of $S_{0}$ follow the Bernoulli model with parameter $2\rho_{s}$, and the signs of $S_{0}$ are i.i.d. $\pm 1$ as above (and independent from the locations). Then if the PCP solution is exact with high probability, then it is also exact with at least the same probability for the model in which the signs are fixed and the locations are sampled from the Bernoulli model with parameter $\rho_{s}$.

This theorem is convenient because to prove our main result, we only need to show that it is true in the case where the signs of the sparse component are random.

Proof Consider the model in which the signs are fixed. In this model, it is convenient to think of $S_{0}$ as $\mathcal{P}_{\Omega}S$, for some fixed matrix $S$, where $\Omega$ is sampled from the Bernoulli model with parameter $\rho_{s}$. Therefore, $S_{0}$ has independent components distributed as

Consider now a random sign matrix with i.i.d. entries distributed as

and an "elimination" matrix $\Delta$ with entries defined by

Note that the entries of $\Delta$ are independent since they are functions of independent variables.

Consider now $S_{0}^{\prime} = {\Delta \circ {({{|S|} \circ E})}}$, where $\circ$ denotes the Hadamard or componentwise product so that, ${\lbrack S_{0}^{\prime}\rbrack}_{ij} = {\Delta_{ij}{({{|S_{ij}|}E_{ij}})}}$. Then we claim that $S_{0}^{\prime}$ and $S_{0}$ have the same distribution. To see why this is true, it suffices by independence to check that the marginals match. For $S_{ij} \neq 0$, we have

which establishes the claim.

This construction allows to prove the theorem. Indeed, ${|S|} \circ E$ now obeys the random sign model, and by assumption, PCP recovers ${|S|} \circ E$ with high probability. By the elimination theorem, this program also recovers $S_{0}^{\prime} = {\Delta \circ {({{|S|} \circ E})}}$. Since $S_{0}^{\prime}$ and $S_{0}$ have the same distribution, the theorem follows.

### Dual certificates

We introduce a simple condition for the pair $(L_{0},S_{0})$ to be the unique optimal solution to Principal Component Pursuit. These conditions are stated in terms of a dual vector, the existence of which certifies optimality. (Recall that $\Omega$ is the space of matrices with the same support as the sparse component $S_{0}$, and that $T$ is the space defined via the the column and row spaces of the low-rank component $L_{0}$ (2.1).)

### Lemma 2.4

Assume that ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} < 1$. With the standard notations, $(L_{0},S_{0})$ is the unique solution if there is a pair $(W,F)$ obeying

with ${\mathcal{P}_{T}W} = 0$, ${\| W\|} < 1$, ${\mathcal{P}_{\Omega}F} = 0$ and ${\| F\|}_{\infty} < 1$.

Note that the condition ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} < 1$ is equivalent to saying that ${\Omega \cap T} = {\{ 0\}}$.

Proof We consider a feasible perturbation $({L_{0} + H},{S_{0} - H})$ and show that the objective increases whenever $H \neq 0$, hence proving that $(L_{0},S_{0})$ is the unique solution. To do this, let ${UV^{\ast}} + W_{0}$ be an arbitrary subgradient of the nuclear norm at $L_{0}$, and ${\text{sgn}{(S_{0})}} + F_{0}$ be an arbitrary subgradient of the $\ell_{1}$-norm at $S_{0}$. By definition of subgradients,

Now pick $W_{0}$ such that ${\langle W_{0},H\rangle} = {\|{\mathcal{P}_{T^{\perp}}H}\|}_{\ast}$ and $F_{0}$ such that ${\langle F_{0},H\rangle} = {- {\|{\mathcal{P}_{\Omega^{\perp}}H}\|}_{1}}$.^77^7For instance, $F_{0} = {- {\text{sgn}{({\mathcal{P}_{\Omega^{\perp}}H})}}}$ is such a matrix. Also, by duality between the nuclear and the operator norm, there is a matrix obeying ${\| W\|} = 1$ such that ${\langle W,{\mathcal{P}_{T^{\perp}}H}\rangle} = {\|{\mathcal{P}_{T^{\perp}}H}\|}_{\ast}$, and we just take $W_{0} = {\mathcal{P}_{T^{\perp}}{(W)}}$. We have

for $\beta = {\text{max}{({\| W\|},{\| F\|}_{\infty})}} < 1$ and, thus,

Since by assumption, ${\Omega \cap T} = {\{ 0\}}$, we have ${{\|{\mathcal{P}_{T^{\perp}}H}\|}_{\ast} + {\lambda{\|{\mathcal{P}_{\Omega^{\perp}}H}\|}_{1}}} > 0$ unless $H = 0$.

Hence, we see that to prove exact recovery, it is sufficient to produce a 'dual certificate' $W$ obeying

Our method, however, will produce with high probability a slightly different certificate. The idea is to slightly relax the constraint ${\mathcal{P}_{\Omega}{({{UV^{\ast}} + W})}} = {\lambda\text{sgn}{(S_{0})}}$, a relaxation that has been introduced by David Gross in in a different context. We prove the following lemma.

### Lemma 2.5

Assume ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} \leq {1/2}$ and $\lambda < 1$. Then with the same notation, $(L_{0},S_{0})$ is the unique solution if there is a pair $(W,F)$ obeying

with ${\mathcal{P}_{T}W} = 0$ and ${\| W\|} \leq \frac{1}{2}$, ${\mathcal{P}_{\Omega}F} = 0$ and ${\| F\|}_{\infty} \leq \frac{1}{2}$, and ${\|{\mathcal{P}_{\Omega}D}\|}_{F} \leq \frac{1}{4}$.

Proof Following the proof of Lemma 2.4, we have

Observe now that

and the term between parenthesis is strictly positive when $H \neq 0$.

As a consequence of Lemma 2.5, it now suffices to produce a dual certificate $W$ obeying

Further, we would like to note that the existing literature on matrix completion gives good bounds on $\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|$, see Theorem 2.6 in Section 2.5.

### Dual certification via the golfing scheme

In the papers, Gross introduces a new scheme, termed the golfing scheme, to construct a dual certificate for the matrix completion problem, i.e. the problem of reconstructing a low-rank matrix from a subset of its entries. In this section, we will adapt this clever golfing scheme, with two important modifications, to our separation problem.

Before we introduce our construction, our model assumes that $\Omega \sim {\text{Ber}{(\rho)}}$, or equivalently that $\Omega^{c} \sim {\text{Ber}{({1 - \rho})}}$. Now the distribution of $\Omega^{c}$ is the same as that of $\Omega^{c} = {\Omega_{1} \cup \Omega_{2} \cup \ldots \cup \Omega_{j_{0}}}$, where each $\Omega_{j}$ follows the Bernoulli model with parameter $q$, which has an explicit expression. To see this, observe that by independence, we just need to make sure that any entry $(i,j)$ is selected with the right probability. We have

so that the two models are the same if

hence justifying our assertion. Note that because of overlaps between the $\Omega_{j}$'s, $q \geq {{({1 - \rho})}/j_{0}}$.

We now propose constructing a dual certificate

where each component is as follows:

Construction of $W^{L}$ via the golfing scheme. Fix an integer $j_{0} \geq 1$ whose value shall be discussed later, and let $\Omega_{j}$, $1 \leq j \leq j_{0}$, be defined as above so that $\Omega^{c} = {\cup_{1 \leq j \leq j_{0}}\Omega_{j}}$. Then starting with $Y_{0} = 0$, inductively define

This is a variation on the golfing scheme discussed in, which assumes that the $\Omega_{j}$'s are sampled with replacement, and does not use the projector $\mathcal{P}_{\Omega_{j}}$ but something more complicated taking into account the number of times a specific entry has been sampled.

Construction of $W^{S}$ via the method of least squares. Assume that ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} < {1/2}$. Then ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}}\|} < {1/4}$ and, thus, the operator $\mathcal{P}_{\Omega} - {\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}}$ mapping $\Omega$ onto itself is invertible; we denote its inverse by ${({\mathcal{P}_{\Omega} - {\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}}})}^{- 1}$. We then set

Clearly, an equivalent definition is via the convergent Neumann series

Note that ${\mathcal{P}_{\Omega}W^{S}} = {\lambda\mathcal{P}_{\Omega}{({I - \mathcal{P}_{T}})}{({\mathcal{P}_{\Omega} - {\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}}})}^{- 1}\text{sgn}{(S_{0})}} = {\lambda\text{sgn}{(S_{0})}}$. With this, the construction has a natural interpretation: one can verify that among all matrices $W \in T^{\perp}$ obeying ${\mathcal{P}_{\Omega}W} = {\lambda\text{sgn}{(S_{0})}}$, $W^{S}$ is that with minimum Frobenius norm.

Since both $W^{L}$ and $W^{S}$ belong to $T^{\perp}$ and ${\mathcal{P}_{\Omega}W^{S}} = {\lambda\text{sgn}{(S_{0})}}$, we will establish that $W^{L} + W^{S}$ is a valid dual certificate if it obeys

### Key lemmas

We now state three lemmas, which taken collectively, establish our main theorem. The first may be found in.

### Theorem 2.6

\[8, Theorem 4.1\] Suppose $\Omega_{0}$ is sampled from the Bernoulli model with parameter $\rho_{0}$. Then with high probability,

provided that $\rho_{0} \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n}}{n}}$ for some numerical constant $C_{0} > 0$ ($\mu$ is the incoherence parameter). For rectangular matrices, we need $\rho_{0} \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n_{}}}{n_{}}}$.

Among other things, this lemma is important because it shows that ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} \leq {1/2}$, provided $|\Omega|$ is not too large. Indeed, if $\Omega \sim {\text{Ber}{(\rho)}}$, we have

with the proviso that ${1 - \rho} \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n}}{n}}$. Note, however, that since $\mathcal{I} = {\mathcal{P}_{\Omega} + \mathcal{P}_{\Omega^{\perp}}}$,

and, therefore, by the triangular inequality

Since ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|}^{2} = {\|{\mathcal{P}_{T}\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|}$, we have established the following:

### Corollary 2.7

Assume that $\Omega \sim {\text{Ber}{(\rho)}}$, then ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|}^{2} \leq {\rho + \epsilon}$, provided that ${1 - \rho} \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n}}{n}}$, where $C_{0}$ is as in Theorem 2.6. For rectangular matrices, the modification is as in Theorem 2.6.

The lemma below is proved is Section 3.

### Lemma 2.8

Assume that $\Omega \sim {\text{Ber}{(\rho)}}$ with parameter $\rho \leq \rho_{s}$ for some $\rho_{s} > 0$. Set $j_{0} = {2{\lceil{\log n}\rceil}}$ (use $\log n_{}$ for rectangular matrices). Then under the other assumptions of Theorem 1.1, the matrix $W^{L}$ (2.5) obeys

${\|{\mathcal{P}_{\Omega}{({{UV^{\ast}} + W^{L}})}}\|}_{F} < {\lambda/4}$,

${\|{\mathcal{P}_{\Omega^{\perp}}{({{UV^{\ast}} + W^{L}})}}\|}_{\infty} < {\lambda/4}$.

Since ${\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} < 1$ with large probability, $W^{S}$ is well defined and the following holds.

### Lemma 2.9

Assume that $S_{0}$ is supported on a set $\Omega$ sampled as in Lemma 2.8, and that the signs of $S_{0}$ are i.i.d. symmetric (and independent of $\Omega$). Then under the other assumptions of Theorem 1.1, the matrix $W^{S}$ (2.6) obeys

${\|{\mathcal{P}_{\Omega^{\perp}}W^{S}}\|}_{\infty} < {\lambda/4}$.

The proof is also in Section 3. Clearly, $W^{L}$ and $W^{S}$ obey (2.8), hence certifying that Principal Component Pursuit correctly recovers the low-rank and sparse components with high probability when the signs of $S_{0}$ are random. The earlier "derandomization" argument then establishes Theorem 1.1.

## Proofs of Dual Certification

This section proves the two crucial estimates, namely, Lemma 2.8 and Lemma 2.9.

### Preliminaries

We begin by recording two results which shall be useful in proving Lemma 2.8. While Theorem 2.6 asserts that with large probability,

for all $Z \in T$, the next lemma shows that for a fixed $Z$, the sup-norm of $Z - {\rho_{0}^{- 1}\mathcal{P}_{T}\mathcal{P}_{\Omega_{0}}{(Z)}}$ also does not increase (also with large probability).

### Lemma 3.1

Suppose $Z \in T$ is a fixed matrix, and $\Omega_{0} \sim {\text{Ber}{(\rho_{0})}}$. Then with high probability,

provided that $\rho_{0} \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n}}{n}}$ (for rectangular matrices, $\rho_{0} \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n_{}}}{n_{}}}$) for some numerical constant $C_{0} > 0$.

The proof is an application of Bernstein's inequality and may be found in the Appendix. A similar but somewhat different version of (3.1) appears in.

The second result was proved in.

### Lemma 3.2

\[8, Theorem 6.3\] Suppose $Z$ is fixed, and $\Omega_{0} \sim {\text{Ber}{(\rho_{0})}}$. Then with high probability,

for some small numerical constant $C_{0}^{\prime} > 0$ provided that $\rho_{0} \geq {C_{0}\frac{\mu{\log n}}{n}}$ (or $\rho_{0} \geq {C_{0}^{\prime}\frac{\mu{\log n_{}}}{n_{}}}$ for rectangular matrices in which case $n_{}{\log n_{}}$ replaces $n{\log n}$ in (3.2)).

As a remark, Lemmas 3.1 and 3.2, and Theorem 2.6 all hold with probability at least $1 - {O{(n^{- \beta})}}$, $\beta > 2$, if $C_{0}$ is replaced by $C\beta$ for some numerical constant $C > 0$.

### Proof of Lemma 2.8

We begin by introducing a piece of notation and set $Z_{j} = {{UV^{\ast}} - {\mathcal{P}_{T}Y_{j}}}$ obeying

Obviously $Z_{j} \in T$ for all $j \geq 0$. First, note that when

(for rectangular matrices, take $q \geq {C_{0}\epsilon^{- 2}\frac{\mur{\log n_{}}}{n_{}}}$), we have

by Lemma 3.1. (This holds with high probability because $\Omega_{j}$ and $Z_{j - 1}$ are independent, and this is why the golfing scheme is easy to use.) In particular, this gives that with high probability

When $q$ obeys the same estimate,

by Theorem 2.6. In particular, this gives that with high probability

Below, we will assume $\epsilon \leq e^{- 1}$.

### Proof of (a)

We prove the first part of the lemma and the argument parallels that in, see also. From

The fourth step follows from Lemma 3.2 and the fifth from (3.5). Since ${\|{UV^{\ast}}\|} \leq {\sqrt{\mur}/n}$, this gives

for some numerical constant $C^{\prime}$ whenever $q$ obeys (3.3).

### Proof of (b)

Since ${\mathcal{P}_{\Omega}Y_{j_{0}}} = 0$,

and it follows from (3.6) that

Since $\epsilon \leq e^{- 1}$ and $j_{0} \geq {2{\log n}}$, $\epsilon^{j_{0}} \leq {1/n^{2}}$ and this proves the claim.

### Proof of (c)

We have ${{UV^{\ast}} + W^{L}} = {Z_{j_{0}} + Y_{j_{0}}}$ and know that $Y_{j_{0}}$ is supported on $\Omega^{c}$. Therefore, since ${\| Z_{j_{0}}\|}_{F} \leq {\lambda/8}$, it suffices to show that ${\| Y_{j_{0}}\|}_{\infty} \leq {\lambda/8}$. We have

Since ${\|{UV^{\ast}}\|}_{\infty} \leq {\sqrt{\mur}/n}$, this gives

for some numerical constant $C^{\prime}$ whenever $q$ obeys (3.3). Since $\lambda = {1/\sqrt{n}}$, ${\| Y_{j_{0}}\|}_{\infty} \leq {\lambda/8}$ if

### Summary

We have seen that (a) and (b) are satisfied if $\epsilon$ is sufficiently small and $j_{0} \geq {2{\log n}}$. For (c), we can take $\epsilon$ on the order of ${({{\mur{({\log n})}^{2}}/n})}^{1/4}$, which will be sufficiently small as well provided that $\rho_{r}$ in (1.4) is sufficiently small. Note that everything is consistent since ${C_{0}\epsilon^{- 2}\frac{\mur{\log n}}{n}} < 1$. This concludes the proof of Lemma 2.8.

### Proof of Lemma 2.9

It is convenient to introduce the sign matrix $E = {\text{sgn}{(S_{0})}}$ distributed as

We shall be interested in the event $\{{{\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} \leq \sigma}\}$ which holds with large probability when $\sigma = {\sqrt{\rho} + \epsilon}$, see Corollary 2.7. In particular, for any $\sigma > 0$, $\{{{\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} \leq \sigma}\}$ holds with high probability provided $\rho$ is sufficiently small.

### Proof of (a)

For the first term, we have ${\|{\mathcal{P}_{T^{\perp}}W_{0}^{S}}\|} \leq {\| W_{0}^{S}\|} = {\lambda{\| E\|}}$. Then standard arguments about the norm of a matrix with i.i.d. entries give

with large probability. Since $\lambda = {1/\sqrt{n}}$, this gives ${\| W_{0}^{S}\|} \leq {4\sqrt{\rho}}$. When the matrix is rectangular, we have

with high probability. Since $\lambda = {1/\sqrt{n_{}}}$ in this case, ${\| W_{0}^{S}\|} \leq {4\sqrt{\rho}}$ as well.

Set $\mathcal{R} = {\sum_{k \geq 1}{({\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}})}^{k}}$ and observe that $\mathcal{R}$ is self-adjoint. For the second term, ${\|{\mathcal{P}_{T^{\perp}}W_{1}^{S}}\|} \leq {\| W_{1}^{S}\|}$, where $W_{1}^{S} = {\lambda\mathcal{R}{(E)}}$. We need to bound the operator norm of the matrix $\mathcal{R}{(E)}$, and use a standard covering argument to do this. Throughout, $N$ denotes an $1/2$-net for ${\mathbb{S}}^{n - 1}$ of size at most $6^{n}$ (such a net exists, see \[30, Theorem 4.16\]). Then a standard argument shows that

For a fixed pair $(x,y)$ of unit-normed vectors in $N \times N$, define the random variable

Conditional on $\Omega = {\text{supp}{(E)}}$, the signs of $E$ are i.i.d. symmetric and Hoeffding's inequality gives

Now since ${\|{yx^{\ast}}\|}_{F} = 1$, the matrix $\mathcal{R}{({yx^{\ast}})}$ obeys ${\|{\mathcal{R}{({yx^{\ast}})}}\|}_{F} \leq {\|\mathcal{R}\|}$ and, therefore,

On the event $\{{{\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} \leq \sigma}\}$,

and, therefore, unconditionally,

With $\lambda = {1/\sqrt{n}}$,

with large probability, provided that $\sigma$, or equivalently $\rho$, is small enough.

### Proof of (b)

Now for ${(i,j)} \in \Omega^{c}$, $W_{ij}^{S} = {\langle e_{i},{W^{S}e_{j}}\rangle} = {\langle{e_{i}e_{j}^{\ast}},W^{S}\rangle}$, and we have

where $X{(i,j)}$ is the matrix $- {{({\mathcal{P}_{\Omega} - {\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}}})}^{- 1}\mathcal{P}_{\Omega}\mathcal{P}_{T}{({e_{i}e_{j}^{\ast}})}}$. Conditional on $\Omega = {\text{supp}{(E)}}$, the signs of $E$ are i.i.d. symmetric, and Hoeffding's inequality gives

Since (2.2) holds, we have

on the event $\{{{\|{\mathcal{P}_{\Omega}\mathcal{P}_{T}}\|} \leq \sigma}\}$. On the same event, ${\|{({\mathcal{P}_{\Omega} - {\mathcal{P}_{\Omega}\mathcal{P}_{T}\mathcal{P}_{\Omega}}})}^{- 1}\|} \leq {({1 - \sigma^{2}})}^{- 1}$ and, therefore,

This proves the claim when ${\mur} < {\rho_{r}^{\prime}n{({\log n})}^{- 1}}$ and $\rho_{r}^{\prime}$ is sufficiently small.

## Numerical Experiments and Applications

In this section, we perform numerical experiments corroborating our main results and suggesting their many applications in image and video analysis. We first investigate Principal Component Pursuit's ability to correctly recover matrices of various rank from errors of various density. We then sketch applications in background modeling from video and removing shadows and specularities from face images.

While the exact recovery guarantee provided by Theorem 1.1 is independent of the particular algorithm used to solve Principal Component Pursuit, its applicability to large scale problems depends on the availability of scalable algorithms for nonsmooth convex optimization. For the experiments in this section, we use the an augmented Lagrange multiplier algorithm introduced in.^88^8Both have posted a version of their code online. In Section 5, we describe this algorithm in more detail, and explain why it is our algorithm of choice for sparse and low-rank separation.

One important implementation detail in our approach is the choice of $\lambda$. Our analysis identifies one choice, $\lambda = {1/\sqrt{\text{max}{(n_{1},n_{2})}}}$, which works well for incoherent matrices. In order to illustrate the theory, throughout this section we will always choose $\lambda = {1/\sqrt{\text{max}{(n_{1},n_{2})}}}$. For practical problems, however, it is often possible to improve performance by choosing $\lambda$ according to prior knowledge about the solution. For example, if we know that $S$ is very sparse, increasing $\lambda$ will allow us to recover matrices $L$ of larger rank. For practical problems, we recommend $\lambda = {1/\sqrt{\text{max}{(n_{1},n_{2})}}}$ as a good rule of thumb, which can then be adjusted slightly to obtain the best possible result.

### Exact recovery from varying fractions of error

We first verify the correct recovery phenomenon of Theorem 1.1 on randomly generated problems. We consider square matrices of varying dimension $n = {500,\ldots,3000}$. We generate a rank-$r$ matrix $L_{0}$ as a product $L_{0} = {XY^{\ast}}$ where $X$ and $Y$ are $n \times r$ matrices with entries independently sampled from a $\mathcal{N}{(0,{1/n})}$ distribution. $S_{0}$ is generated by choosing a support set $\Omega$ of size $k$ uniformly at random, and setting $S_{0} = {\mathcal{P}_{\Omega}E}$, where $E$ is a matrix with independent Bernoulli $\pm 1$ entries.

Table 1 (top) reports the results with $r = {{rank}{(L_{0})}} = {0.05 \times n}$ and $k = {\| S_{0}\|}_{0} = {0.05 \times n^{2}}$. Table 1 (bottom) reports the results for a more challenging scenario, ${{rank}{(L_{0})}} = {0.05 \times n}$ and $k = {0.10 \times n^{2}}$. In all cases, we set $\lambda = {1/\sqrt{n}}$. Notice that in all cases, solving the convex PCP gives a result $(L,S)$ with the correct rank and sparsity. Moreover, the relative error ${\|{L - L_{0}}\|}_{F}/{\| L_{0}\|}_{F}$ is small, less than $10^{- 5}$ in all examples considered.^99^9We measure relative error in terms of $L$ only, since in this paper we view the sparse and low-rank decomposition as recovering a low-rank matrix $L_{0}$ from gross errors. $S_{0}$ is of course also well-recovered: in this example, the relative error in $S$ is actually smaller than that in $L$.

The last two columns of Table 1 give the number of partial singular value decompositions computed in the course of the optimization ($\#$ SVD) as well as the total computation time. This experiment was performed in Matlab on a Mac Pro with dual quad-core 2.66 GHz Intel Xenon processors and 16 GB RAM. As we will discuss in Section 5 the dominant cost in solving the convex program comes from computing one partial SVD per iteration. Strikingly, in Table 1, the number of SVD computations is nearly constant regardless of dimension, and in all cases less than 17.^1010^10One might reasonably ask whether this near constant number of iterations is due to the fact that random problems are in some sense well-conditioned. There is some validity to this concern, as we will see in our real data examples. suggests a continuation strategy (there termed "Inexact ALM") that produces qualitatively similar solutions with a similarly small number of iterations. However, to the best of our knowledge its convergence is not guaranteed. This suggests that in addition to being theoretically well-founded, the recovery procedure advocated in this paper is also reasonably practical.

## SVD

Table 1: Correct recovery for random problems of varying size. Here, L0 = X Y* ∈ ℝn × n with X, Y ∈ ℝn × r; X, Y have entries i.i.d. 𝒩 (0,1/n). S0 ∈ {−1, 0, 1}n × n has support chosen uniformly at random and independent random signs; ∥S0∥0 is the number of nonzero entries in S0. Top: recovering matrices of rank 0.05 × n from 5% gross errors. Bottom: recovering matrices of rank 0.05 × n from 10% gross errors. In all cases, the rank of L0 and ℓ0-norm of S0 are correctly estimated. Moreover, the number of partial singular value decompositions (# SVD) required to solve PCP is almost constant.

### Phase transition in rank and sparsity

Theorem 1.1 shows that convex programming correctly recovers an incoherent low-rank matrix from a constant fraction $\rho_{s}$ of errors. We next empirically investigate the algorithm's ability to recover matrices of varying rank from errors of varying sparsity. We consider square matrices of dimension $n_{1} = n_{2} = 400$. We generate low-rank matrices $L_{0} = {XY^{\ast}}$ with $X$ and $Y$ independently chosen $n \times r$ matrices with i.i.d. Gaussian entries of mean zero and variance $1/n$. For our first experiment, we assume a Bernoulli model for the support of the sparse term $S_{0}$, with random signs: each entry of $S_{0}$ takes on value $0$ with probability $1 - \rho$, and values $\pm 1$ each with probability $\rho/2$. For each $(r,\rho)$ pair, we generate $10$ random problems, each of which is solved via the algorithm of Section 5. We declare a trial to be successful if the recovered $\hat{L}$ satisfies ${{\|{L - L_{0}}\|}_{F}/{\| L_{0}\|}_{F}} \leq 10^{- 3}$. Figure 1 (left) plots the fraction of correct recoveries for each pair $(r,\rho)$. Notice that there is a large region in which the recovery is exact. This highlights an interesting aspect of our result: the recovery is correct even though in some cases ${\| S_{0}\|}_{F} \gg {\| L_{0}\|}_{F}$ (e.g., for ${r/n} = \rho$, ${\| S_{0}\|}_{F}$ is $\sqrt{n} = 20$ times larger!). This is to be expected from Lemma 2.4: the existence (or non-existence) of a dual certificate depends only on the signs and support of $S_{0}$ and the orientation of the singular spaces of $L_{0}$.

However, for incoherent $L_{0}$, our main result goes one step further and asserts that the signs of $S_{0}$ are also not important: recovery can be guaranteed as long as its support is chosen uniformly at random. We verify this by again sampling $L_{0}$ as a product of Gaussian matrices and choosing the support $\Omega$ according to the Bernoulli model, but this time setting $S_{0} = {\mathcal{P}_{\Omega}{sgn}{(L_{0})}}$. One might expect such $S_{0}$ to be more difficult to distinguish from $L_{0}$. Nevertheless, our analysis showed that the number of errors that can be corrected drops by at most $1/2$ when moving to this more difficult model. Figure 1 (middle) plots the fraction of correct recoveries over $10$ trials, again varying $r$ and $\rho$. Interestingly, the region of correct recovery in Figure 1 (middle) actually appears to be broader than that in Figure 1 (left). Admittedly, the shape of the region in the upper-left corner is puzzling, but has been 'confirmed' by several distinct simulation experiments (using different solvers).

Finally, inspired by the connection between matrix completion and robust PCA, we compare the breakdown point for the low-rank and sparse separation problem to the breakdown behavior of the nuclear-norm heuristic for matrix completion. By comparing the two heuristics, we can begin to answer the question how much is gained by knowing the location $\Omega$ of the corrupted entries? Here, we again generate $L_{0}$ as a product of Gaussian matrices. However, we now provide the algorithm with only an incomplete subset $M = {\mathcal{P}_{\Omega^{\perp}}L_{0}}$ of its entries. Each $(i,j)$ is included in $\Omega$ independently with probability $1 - \rho$, so rather than a probability of error, here, $\rho$ stands for the probability that an entry is omitted. We solve the nuclear norm minimization problem

using an augmented Lagrange multiplier algorithm very similar to the one discussed in Section 5. We again declare $L_{0}$ to be successfully recovered if ${{\|{L - L_{0}}\|}_{F}/{\| L_{0}\|}_{F}} < 10^{- 3}$. Figure 1 (right) plots the fraction of correct recoveries for varying $r,\rho$. Notice that nuclear norm minimization successfully recovers $L_{0}$ over a much wider range of $(r,\rho)$. This is interesting because in the regime of large $k$, $k = {\Omega{(n^{2})}}$, the best performance guarantees for each heuristic agree in their order of growth -- both guarantee correct recovery for ${{rank}{(L_{0})}} = {O{({n/{\log^{2}n}})}}$. Fully explaining the difference in performance between the two problems may require a sharper analysis of the breakdown behavior of each.

(a) Robust PCA, Random Signs

(b) Robust PCA, Coherent Signs

Figure 1: Correct recovery for varying rank and sparsity. Fraction of correct recoveries across 10 trials, as a function of rank (L0) (x-axis) and sparsity of S0 (y-axis). Here, n1 = n2 = 400. In all cases, L0 = X Y* is a product of independent n × r i.i.d. 𝒩 (0,1/n) matrices. Trials are considered successful if ∥L̂ − L0∥F/∥L0∥F &lt; 10−3. Left: low-rank and sparse decomposition, sgn (S0) random. Middle: low-rank and sparse decomposition, S0 = 𝒫Ω sgn (L0). Right: matrix completion. For matrix completion, ρs is the probability that an entry is omitted from the observation.

### Application sketch: background modeling from surveillance video

Video is a natural candidate for low-rank modeling, due to the correlation between frames. One of the most basic algorithmic tasks in video surveillance is to estimate a good model for the background variations in a scene. This task is complicated by the presence of foreground objects: in busy scenes, every frame may contain some anomaly. Moreover, the background model needs to be flexible enough to accommodate changes in the scene, for example due to varying illumination. In such situations, it is natural to model the background variations as approximately low rank. Foreground objects, such as cars or pedestrians, generally occupy only a fraction of the image pixels and hence can be treated as sparse errors.

We investigate whether convex optimization can separate these sparse errors from the low-rank background. Here, it is important to note that the error support may not be well-modeled as Bernoulli: errors tend to be spatially coherent, and more complicated models such as Markov random fields may be more appropriate. Hence, our theorems do not necessarily guarantee the algorithm will succeed with high probability. Nevertheless, as we will see, Principal Component Pursuit still gives visually appealing solutions to this practical low-rank and sparse separation problem, without using any additional information about the spatial structure of the error.

We consider two example videos introduced in. The first is a sequence of $200$ grayscale frames taken in an airport. This video has a relatively static background, but significant foreground variations. The frames have resolution $176 \times 144$; we stack each frame as a column of our matrix $M \in {\mathbb{R}}^{25,{344 \times 200}}$. We decompose $M$ into a low-rank term and a sparse term by solving the convex PCP problem (1.1) with $\lambda = {1/\sqrt{n_{1}}}$. On a desktop PC with a 2.33 GHz Core2 Duo processor and 2 GB RAM, our Matlab implementation requires 806 iterations, and roughly 43 minutes to converge.^1111^11The paper suggests a variant of ALM optimization procedure, there termed the "Inexact ALM" that finds a visually similar decomposition in far fewer iterations (less than 50). However, since the convergence guarantee for that variant is weak, we choose to present the slower, exact result here. Figure 2(a) shows three frames from the video; (b) and (c) show the corresponding columns of the low rank matrix $\hat{L}$ and sparse matrix $\hat{S}$ (its absolute value is shown here). Notice that $\hat{L}$ correctly recovers the background, while $\hat{S}$ correctly identifies the moving pedestrians. The person appearing in the images in $\hat{L}$ does not move throughout the video.

Convex optimization (this work) Alternating minimization
Figure 2: Background modeling from video. Three frames from a 200 frame video sequence taken in an airport. (a) Frames of original video M. (b)-(c) Low-rank L̂ and sparse components Ŝ obtained by PCP, (d)-(e) competing approach based on alternating minimization of an m-estimator. PCP yields a much more appealing result despite using less prior knowledge.

Convex optimization (this work) Alternating minimization
Figure 3: Background modeling from video. Three frames from a 250 frame sequence taken in a lobby, with varying illumination. (a) Original video M. (b)-(c) Low-rank L̂ and sparse Ŝ obtained by PCP. (d)-(e) Low-rank and sparse components obtained by a competing approach based on alternating minimization of an m-estimator. Again, convex programming yields a more appealing result despite using less prior information.

Figure 2 (d) and (e) compares the result obtained by Principal Component Pursuit to a state-of-the-art technique from the computer vision literature,.^1212^12We use the code package downloaded from http://www.salleurl.edu/\~ftorre/papers/rpca/rpca.zip, modified to choose the rank of the approximation as suggested in. That approach also aims at robustly recovering a good low-rank approximation, but uses a more complicated, nonconvex $m$-estimator, which incorporates a local scale estimate that implicitly exploits the spatial characteristics of natural images. This leads to a highly nonconvex optimization, which is solved locally via alternating minimization. Interestingly, despite using more prior information about the signal to be recovered, this approach does not perform as well as the convex programming heuristic: notice the large artifacts in the top and bottom rows of Figure 2 (d).

In Figure 3, we consider $250$ frames of a sequence with several drastic illumination changes. Here, the resolution is $168 \times 120$, and so $M$ is a $20,{160 \times 250}$ matrix. For simplicity, and to illustrate the theoretical results obtained above, we again choose $\lambda = {1/\sqrt{n_{1}}}$.^1313^13For this example, slightly more appealing results can actually be obtained by choosing larger $\lambda$ (say, $2/\sqrt{n_{1}}$). For this example, on the same 2.66 GHz Core 2 Duo machine, the algorithm requires a total of 561 iterations and 36 minutes to converge.

Figure 3 (a) shows three frames taken from the original video, while (b) and (c) show the recovered low-rank and sparse components, respectively. Notice that the low-rank component correctly identifies the main illuminations as background, while the sparse part corresponds to the motion in the scene. On the other hand, the result produced by the algorithm of treats some of the first illumination as foreground. PCP again outperforms the competing approach, despite using less prior information. These results suggest the potential power for convex programming as a tool for video analysis.

Notice that the number of iterations for the real data is typically higher than that of the simulations with random matrices given in Table 1. The reason for this discrepancy might be that the structures of real data could slightly deviate from the idealistic low-rank and sparse model. Nevertheless, it is important to realize that practical applications such as video surveillance often provide additional information about the signals of interest, e.g. the support of the sparse foreground is spatially piecewise contiguous, or even impose additional requirements, e.g. the recovered background needs to be non-negative etc. We note that the simplicity of our objective and solution suggests that one can easily incorporate additional constraints and more accurate models of the signals so as to obtain much more efficient and accurate solutions in the future.

### Application sketch: removing shadows and specularities from face images

Face recognition is another problem domain in computer vision where low-dimensional linear models have received a great deal of attention. This is mostly due to the work of Basri and Jacobs, who showed that for convex, Lambertian objects, images taken under distant illumination lie near an approximately nine-dimensional linear subspace known as the harmonic plane. However, since faces are neither perfectly convex nor Lambertian, real face images often violate this low-rank model, due to cast shadows and specularities. These errors are large in magnitude, but sparse in the spatial domain. It is reasonable to believe that if we have enough images of the same face, Principal Component Pursuit will be able to remove these errors. As with the previous example, some caveats apply: the theoretical result suggests the performance should be good, but does not guarantee it, since again the error support does not follow a Bernoulli model. Nevertheless, as we will see, the results are visually striking.

Figure 4: Removing shadows, specularities, and saturations from face images. (a) Cropped and aligned images of a person’s face under different illuminations from the Extended Yale B database. The size of each image is 192 × 168 pixels, a total of 58 different illuminations were used for each person. (b) Low-rank approximation L̂ recovered by convex programming. (c) Sparse error Ŝ corresponding to specularities in the eyes, shadows around the nose region, or brightness saturations on the face. Notice in the bottom left that the sparse term also compensates for errors in image acquisition.

Figure 4 shows two examples with face images taken from the Yale B face database. Here, each image has resolution $192 \times 168$; there are a total of $58$ illuminations per subject, which we stack as the columns of our matrix $M \in {\mathbb{R}}^{32,{256 \times 58}}$. We again solve PCP with $\lambda = {1/\sqrt{n_{1}}}$. In this case, the algorithm requires 642 iterations to converge, and the total computation time on the same Core 2 Duo machine is $685$ seconds.

Figure 4 plots the low rank term $\hat{L}$ and the magnitude of the sparse term $\hat{S}$ obtained as the solution to the convex program. The sparse term $\hat{S}$ compensates for cast shadows and specular regions. In one example (bottom row of Figure 4 left), this term also compensates for errors in image acquisition. These results may be useful for conditioning the training data for face recognition, as well as face alignment and tracking under illumination variations.

## Algorithms

Theorem 1.1 shows that incoherent low-rank matrices can be recovered from nonvanishing fractions of gross errors in polynomial time. Moreover, as the experiments in the previous section attest, the low computation cost is guaranteed not only in theory, the efficiency is becoming practical for real imaging problems. This practicality is mainly due to the rapid recent progress in scalable algorithms for nonsmooth convex optimization, in particular for minimizing the $\ell_{1}$ and nuclear norms. In this section, we briefly review this progress, and discuss our algorithm of choice for this problem.

For small problem sizes, Principal Component Pursuit

can be performed using off-the-shelf tools such as interior point methods. This was suggested for rank minimization in and for low-rank and sparse decomposition (see also ). However, despite their superior convergence rates, interior point methods are typically limited to small problems, say $n < 100$, due to the $O{(n^{6})}$ complexity of computing a step direction.

The limited scalability of interior point methods has inspired a recent flurry of work on first-order methods. Exploiting an analogy with iterative thresholding algorithms for $\ell_{1}$-minimization, Cai et. al. developed an algorithm that performs nuclear-norm minimization by repeatedly shrinking the singular values of an appropriate matrix, essentially reducing the complexity of each iteration to the cost of an SVD. However, for our low-rank and sparse decomposition problem, this form of iterative thresholding converges slowly, requiring up to $10^{4}$ iterations. Ma et. al. suggest improving convergence using continuation techniques, and also demonstrate how Bregman iterations can be applied to nuclear norm minimization.

The convergence of iterative thresholding has also been greatly improved using ideas from Nesterov's optimal first-order algorithm for smooth minimization, which was extended to non-smooth optimization in, and applied to $\ell_{1}$-minimization in. Based on, Toh et. al. developed a proximal gradient algorithm for matrix completion which they termed Accelerated Proximal Gradient (APG). A very similar APG algorithm was suggested for low-rank and sparse decomposition in. That algorithm inherits the optimal $O{({1/k^{2}})}$ convergence rate for this class of problems. Empirical evidence suggests that these algorithms can solve the convex PCP problem at least 50 times faster than straightforward iterative thresholding (for more details and comparisons, see ).

However, despite its good convergence guarantees, the practical performance of APG depends strongly on the design of good continuation schemes. Generic continuation does not guarantee good accuracy and convergence across a wide range of problem settings.^1414^14In our experience, the optimal choice may depend on the relative magnitudes of the $L$ and $S$ terms and the sparsity of the corruption. In this paper, we have chosen to instead solve the convex PCP problem (1.1) using an augmented Lagrange multiplier (ALM) algorithm introduced in. In our experience, ALM achieves much higher accuracy than APG, in fewer iterations. It works stably across a wide range of problem settings with no tuning of parameters. Moreover we observe an appealing (empirical) property: the rank of the iterates often remains bounded by ${rank}{(L_{0})}$ throughout the optimization, allowing them to be computed especially efficiently. APG, on the other hand, does not have this property.

The ALM method operates on the augmented Lagrangian

A generic Lagrange multiplier algorithm would solve PCP by repeatedly setting ${(L_{k},S_{k})} = {{\arg{\min_{L,S}l}}{(L,S,Y_{k})}}$, and then updating the Lagrange multiplier matrix via $Y_{k + 1} = {Y_{k} + {\mu{({M - L_{k} - S_{k}})}}}$.

For our low-rank and sparse decomposition problem, we can avoid having to solve a sequence of convex programs by recognizing that ${\min_{L}l}{(L,S,Y)}$ and ${\min_{S}l}{(L,S,Y)}$ both have very simple and efficient solutions. Let $\mathcal{S}_{\tau}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ denote the shrinkage operator ${\mathcal{S}_{\tau}{\lbrack x\rbrack}} = {\text{sgn}{(x)}{\max{({{|x|} - \tau},0)}}}$, and extend it to matrices by applying it to each element. It is easy to show that

Similarly, for matrices $X$, let $\mathcal{D}_{\tau}{(X)}$ denote the singular value thresholding operator given by ${\mathcal{D}_{\tau}{(X)}} = {U\mathcal{S}_{\tau}{(\Sigma)}V^{\ast}}$, where $X = {U\SigmaV^{\ast}}$ is any singular value decomposition. It is not difficult to show that

Thus, a more practical strategy is to first minimize $l$ with respect to $L$ (fixing $S$), then minimize $l$ with respect to $S$ (fixing $L$), and then finally update the Lagrange multiplier matrix $Y$ based on the residual $M - L - S$, a strategy that is summarized as Algorithm 1 below.

2: while not converged do
Algorithm 1 (Principal Component Pursuit by Alternating Directions )

Algorithm 1 is a special case of a more general class of augmented Lagrange multiplier algorithms known as alternating directions methods. The convergence of these algorithms has been well-studied (see e.g. and the many references therein, as well as discussion in ). Algorithm 1 performs excellently on a wide range of problems: as we saw in Section 3, relatively small numbers of iterations suffice to achieve good relative accuracy. The dominant cost of each iteration is computing $L_{k + 1}$ via singular value thresholding. This requires us to compute those singular vectors of $M - S_{k} - {\mu^{- 1}Y_{k}}$ whose corresponding singular values exceed the threshold $\mu$. Empirically, we have observed that the number of such large singular values is often bounded by ${rank}{(L_{0})}$, allowing the next iterate to be computed efficiently via a partial SVD.^1515^15Further performance gains might be possible by replacing this partial SVD with an approximate SVD, as suggested in for nuclear norm minimization. The most important implementation details for this algorithm are the choice of $\mu$ and the stopping criterion. In this work, we simply choose $\mu = {{{n_{1}n_{2}}/4}{\| M\|}_{1}}$, as suggested in. We terminate the algorithm when ${\|{M - L - S}\|}_{F} \leq {\delta{\| M\|}_{F}}$, with $\delta = 10^{- 7}$.

Very similar ideas can be used to develop simple and effective augmented Lagrange multiplier algorithms for matrix completion, and for the robust matrix completion problem (1.5) discussed in Section 1.6, with similarly good performance. In the preceding section, all simulations and experiments are therefore conducted using ALM-based algorithms. For a more thorough discussion, implementation details and comparisons with other algorithms, please see.

## Discussion

This paper delivers some rather surprising news: one can disentangle the low-rank and sparse components exactly by convex programming, and this provably works under very broad conditions that are much broader than those provided by the best known results. Further, our analysis has revealed rather close relationships between matrix completion and matrix recovery (from sparse errors) and our results even generalize to the case when there are both incomplete and corrupted entries (i.e. Theorem 1.2). In addition, Principal Component Pursuit does not have any free parameter and can be solved by simple optimization algorithms with remarkable efficiency and accuracy. More importantly, our results may point to a very wide spectrum of new theoretical and algorithmic issues together with new practical applications that can now be studied systematically.

Our study so far is limited to the low-rank component being exactly low-rank, and the sparse component being exactly sparse. It would be interesting to investigate when either or both these assumptions are relaxed. One way to think of this is via the new observation model $M = {L_{0} + S_{0} + N_{0}}$, where $N_{0}$ is a dense, small perturbation accounting for the fact that the low-rank component is only approximately low-rank and that small errors can be added to all the entries (in some sense, this model unifies the classical PCA and the robust PCA by combining both sparse gross errors and dense small noise). The ideas developed in in connection with the stability of matrix completion under small perturbations may be useful here. Even more generally, the problems of sparse signal recovery, low-rank matrix completion, classical PCA, and robust PCA can all be considered as special cases of a general measurement model of the form

where $\mathcal{A},\mathcal{B},\mathcal{C}$ are known linear maps. An ambitious goal might be to understand exactly under what conditions, one can effectively retrieve or decompose $L_{0}$ and $S_{0}$ from such noisy linear measurements via convex programming.

The remarkable ability of convex optimizations in recovering low-rank matrices and sparse signals in high-dimensional spaces suggest that they will be a powerful tool for processing massive data sets that arise in image/video processing, web data analysis, and bioinformatics. Such data are often of millions or even billions of dimensions so the computational and memory cost can be far beyond that of a typical PC. Thus, one important direction for future investigation is to develop algorithms that have even better scalability, and can be easily implemented on the emerging parallel and distributed computing infrastructures.
