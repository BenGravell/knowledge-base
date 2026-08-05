<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Power of Convex Relaxation: Near-Optimal Matrix Completion

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is concerned with the problem of recovering an unknown matrix from a small fraction of its entries. This is known as the matrix completion problem, and comes up in a great number of applications, including the famous Netflix Prize and other similar questions in collaborative filtering. In general, accurate recovery of a matrix from a small number of entries is impossible; but the knowledge that the unknown matrix has low rank radically changes this premise, making the search for solutions meaningful. This paper presents optimality results quantifying the minimum number of entries needed to recover a matrix of rank r exactly by any method whatsoever (the information theoretic limit). More importantly, the paper shows that, under certain incoherence assumptions on the singular vectors of the matrix, recovery is possible by solving a convenient convex program as soon as the number of entries is on the order of the information theoretic limit (up to logarithmic factors). This convex program simply finds, among all matrices consistent with the observed entries, that with minimum nuclear norm.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As an example, we show that on the order of nr log(n) samples are needed to recover a random n x n matrix of rank r by any method, and to be sure, nuclear norm minimization succeeds as soon as the number of entries is of the form nr polylog(n).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Motivation", "weight": 1.0} -->

Imagine we have an $n_{1} \times n_{2}$ array of real^11^1Much of the discussion below, as well as our main results, apply also to the case of complex matrix completion, with some minor adjustments in the absolute constants; but for simplicity we restrict attention to the real case. numbers and that we are interested in knowing the value of each of the $n_{1}n_{2}$ entries in this array. Suppose, however, that we only get to see a small number of the entries so that most of the elements about which we wish information are simply missing. Is it possible from the available entries to guess the many entries that we have not seen? This problem is now known as the matrix completion problem, and comes up in a great number of applications, including the famous Netflix Prize and other similar questions in collaborative filtering. In a nutshell, collaborative filtering is the task of making automatic predictions about the interests of a user by collecting taste information from many users. Netflix is a commercial company implementing collaborative filtering, and seeks to predict users' movie preferences from just a few ratings per user.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

There are many other such recommendation systems proposed by Amazon, Barnes and Noble, and Apple Inc. to name just a few. In each instance, we have a partial list about a user's preferences for a few rated items, and would like to predict his/her preferences for all items from this and other information gleaned from many other users.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

In mathematical terms, the problem may be posed as follows: we have a data matrix $M \in {\mathbb{R}}^{n_{1} \times n_{2}}$ which we would like to know as precisely as possible. Unfortunately, the only information available about $M$ is a sampled set of entries $M_{ij}$, ${(i,j)} \in \Omega$, where $\Omega$ is a subset of the complete set of entries ${\lbrack n_{1}\rbrack} \times {\lbrack n_{2}\rbrack}$. (Here and in the sequel, $\lbrack n\rbrack$ denotes the list $\{ 1,\ldots,n\}$.) Clearly, this problem is ill-posed for there is no way to guess the missing entries without making any assumption about the matrix $M$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

An increasingly common assumption in the field is to suppose that the unknown matrix $M$ has low rank or has approximately low rank. In a recommendation system, this makes sense because often times, only a few factors contribute to an individual's taste. In, the authors showed that this premise radically changes the problem, making the search for solutions meaningful. Before reviewing these results, we would like to emphasize that the problem of recovering a low-rank matrix from a sample of its entries, and by extension from fewer linear functionals about the matrix, comes up in many application areas other than collaborative filtering. For instance, the completion problem also arises in computer vision. There, many pixels may be missing in digital images because of occlusion or tracking failures in a video sequence. Recovering a scene and inferring camera motion from a sequence of images is a matrix completion problem known as the structure-from-motion problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

Other examples include system identification in control, multi-class learning in data analysis, global positioning---e.g. of sensors in a network---from partial distance information, remote sensing applications in signal processing where we would like to infer a full covariance matrix from partially observed correlations, and many statistical problems involving succinct factor models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Minimal sampling", "weight": 1.0} -->

This paper is concerned with the theoretical underpinnings of matrix completion and more specifically in quantifying the minimum number of entries needed to recover a matrix of rank $r$ exactly. This number generally depends on the matrix we wish to recover. For simplicity, assume that the unknown rank-$r$ matrix $M$ is $n \times n$. Then it is not hard to see that matrix completion is impossible unless the number of samples $m$ is at least ${2nr} - r^{2}$, as a matrix of rank $r$ depends on this many degrees of freedom.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Minimal sampling", "weight": 1.0} -->

Informally, the singular values $\sigma_{1} \geq \ldots \geq \sigma_{r}$ depend on $r$ degrees of freedom, the left singular vectors $u_{k}$ on ${{({n - 1})} + {({n - 2})} + \ldots + {({n - r})}} = {{nr} - {{r{({r + 1})}}/2}}$ degrees of freedom, and similarly for the right singular vectors $v_{k}$. If $m < {{2nr} - r^{2}}$, no matter which entries are available, there can be an infinite number of matrices of rank at most $r$ with exactly the same entries, and so exact matrix completion is impossible. In fact, if the observed locations are sampled at random, we will see later that the minimum number of samples is better thought of as being on the order of $nr{\log n}$ rather than $nr$ because of a coupon collector's effect.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Minimal sampling", "weight": 1.0} -->

In this paper, we are interested in identifying large classes of matrices which can provably be recovered by a tractable algorithm from a number of samples approaching the above limit, i.e. from about $nr{\log n}$ samples. Before continuing, it is convenient to introduce some notations that will be used throughout: let $\mathcal{P}_{\Omega}:{{\mathbb{R}}^{n \times n}\rightarrow{\mathbb{R}}^{n \times n}}$ be the orthogonal projection onto the subspace of matrices which vanish outside of $\Omega$ (${(i,j)} \in \Omega$ if and only if $M_{ij}$ is observed); that is, $Y = {\mathcal{P}_{\Omega}{(X)}}$ is defined as so that the information about $M$ is given by $\mathcal{P}_{\Omega}{(M)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Minimal sampling", "weight": 1.0} -->

The matrix $M$ can be, in principle, recovered from $\mathcal{P}_{\Omega}{(M)}$ if it is the unique matrix of rank less or equal to $r$ consistent with the data. In other words, if $M$ is the unique solution to Knowing when this happens is a delicate question which shall be addressed later. For the moment, note that attempting recovery via (1.2) is not practical as rank minimization is in general an NP-hard problem for which there are no known algorithms capable of solving problems in practical time once, say, $n \geq 10$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Minimal sampling", "weight": 1.0} -->

In, it was proved 1) that matrix completion is not as ill-posed as previously thought and 2) that exact matrix completion is possible by convex programming. The authors of proposed recovering the unknown matrix by solving the nuclear norm minimization problem where the *nuclear norm* ${\| X\|}_{\ast}$ of a matrix $X$ is defined as the sum of its singular values, (The problem (1.3) is a semidefinite program.) They proved that if $\Omega$ is sampled uniformly at random among all subset of cardinality $m$ and $M$ obeys a low coherence condition which we will review later, then with large probability, the unique solution to (1.3) is exactly $M$, provided that the number of samples obeys (to be completely exact, there is a restriction on the range of values that $r$ can take on).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Minimal sampling", "weight": 1.0} -->

In (1.5), the number of samples per degree of freedom is not logarithmic or polylogarithmic in the dimension, and one would like to know whether better results approaching the $nr{\log n}$ limit are possible. This paper provides a positive answer. In details, this work develops many useful matrix models for which nuclear norm minimization is guaranteed to succeed as soon as the number of entries is of the form $nr\text{polylog}{(n)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Main results", "weight": 1.0} -->

A contribution of this paper is to develop simple hypotheses about the matrix $M$ which makes it recoverable by semidefinite programming from nearly minimally sampled entries. To state our assumptions, we recall the SVD of $M$ (1.1) and denote by $P_{U}$ (resp. $P_{V}$) the orthogonal projections onto the column (resp. row) space of $M$; i.e. the span of the left (resp. right) singular vectors. Note that Next, define the matrix $E$ as We observe that $E$ interacts well with $P_{U}$ and $P_{V}$, in particular obeying the identities One can view $E$ as a sort of matrix-valued "sign pattern" for $M$ (compare (1.7) with (1.1)), and is also closely related to the subgradient $\partial{\| M\|}_{\ast}$ of the nuclear norm at $M$ (see (3.2)).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main results", "weight": 1.0} -->

It is clear that some assumptions on the singular vectors $u_{i},v_{i}$ (or on the spaces $U,V$) is needed in order to have a hope of efficient matrix completion. For instance, if $u_{1}$ and $v_{1}$ are Kronecker delta functions at positions $i,j$ respectively, then the singular value $\sigma_{1}$ can only be recovered if one actually samples the $(i,j)$ coordinate, which is only likely if one is sampling a significant fraction of the entire matrix. Thus we need the vectors $u_{i},v_{i}$ to be "spread out" or "incoherent" in some sense. In our arguments, it will be convenient to phrase this incoherence assumptions using the projection matrices $P_{U},P_{V}$ and the sign pattern matrix $E$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main results", "weight": 1.0} -->

More precisely, our assumptions are as follows.: There exists $\mu_{1} > 0$ such that for all pairs ${(a,a')} \in {{\lbrack n_{1}\rbrack} \times {\lbrack n_{1}\rbrack}}$ and ${(b,b')} \in {{\lbrack n_{2}\rbrack} \times {\lbrack n_{2}\rbrack}}$,: There exists $\mu_{2} > 0$ such that for all ${(a,b)} \in {{\lbrack n_{1}\rbrack} \times {\lbrack n_{2}\rbrack}}$, We will say that the matrix $M$ obey the strong incoherence property with parameter $\mu$ if one can take $\mu_{1}$ and $\mu_{2}$ both less than equal to $\mu$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main results", "weight": 1.0} -->

(This property is related to, but slightly different, the *incoherence property*, which will be discussed in Section 1.6.1.)

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main results", "weight": 1.0} -->

*Remark.* Our assumptions only involve the singular vectors $u_{1},\ldots,u_{r},v_{1},\ldots,v_{r}$ of $M$; the singular *values* $\sigma_{1},\ldots,\sigma_{r}$ are completely unconstrained. This lack of dependence on the singular values is a consequence of the geometry of the nuclear norm (and in particular, the fact that the subgradient $\partial{\| X\|}_{\ast}$ of this norm is independent of the singular values, see (3.2)).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main results", "weight": 1.0} -->

It is not hard to see that $\mu$ must be greater than 1. For instance, (1.9) implies which forces $\mu_{2} \geq 1$. The Frobenius norm identities and (1.8a), (1.8b) also place a similar lower bound on $\mu_{1}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main results", "weight": 1.0} -->

We will show that 1) matrices obeying the strong incoherence property with a small value of the parameter $\mu$ can be recovered from fewer entries and that 2) many matrices of interest obey the strong incoherence property with a small $\mu$. We will shortly develop three models, the uniformly bounded orthogonal model, the low-rank low-coherence model, and the random orthogonal model which all illustrate the point that if the singular vectors of $M$ are "spread out" in the sense that their amplitudes all have about the same size, then the parameter $\mu$ is low. In some sense, "most" low-rank matrices obey the strong incoherence property with $\mu = {O{(\sqrt{\log n})}}$, where $n = {\max{(n_{1},n_{2})}}$. Here, $O{( \cdot )}$ is the standard asymptotic notation, which is reviewed in Section 1.8.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Main results", "weight": 1.0} -->

Our first matrix completion result is as follows.

<!-- chunk {"id": "body-0023", "role": "body", "section": "A surprise", "weight": 1.0} -->

We find it unexpected that nuclear norm-minimization works so well, for reasons we now pause to discuss. For simplicity, consider matrices with a strong incoherence parameter $\mu$ polylogarithmic in the dimension. We know that for the rank minimization program (1.2) to succeed, or equivalently for the problem to be well posed, the number of samples must exceed a constant times $nr{\log n}$. However, Theorem 1.2 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion") proves that the convex relaxation is rigorously exact nearly as soon as our problem has a unique low-rank solution. The surprise here is that admittedly, there is a priori no good reason to suspect that convex relaxation might work so well. There is a priori no good reason to suspect that the gap between what combinatorial and convex optimization can do is this small. In this sense, we find these findings a little unexpected.

<!-- chunk {"id": "body-0024", "role": "body", "section": "A surprise", "weight": 1.0} -->

The reader will note an analogy with the recent literature on compressed sensing, which shows that under some conditions, the sparsest solution to an underdetermined system of linear equations is that with minimum $\ell_{1}$ norm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Model matrices", "weight": 1.0} -->

We now discuss model matrices which obey the conditions (1.8) and (1.9) for small values of the strong incoherence parameter $\mu$. For simplicity we restrict attention to the square matrix case $n_{1} = n_{2} = n$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Uniformly bounded model", "weight": 1.0} -->

In this section we shall show, roughly speaking, that almost all $n \times n$ matrices $M$ with singular vectors obeying the size property with $\mu_{B} = {O{}}$ also satisfy the assumptions A1 and A2 with ${\mu_{1},\mu_{2}} = {O{(\sqrt{\log n})}}$. This justifies our earlier claim that when the singular vectors are spread out, then the strong incoherence property holds for a small value of $\mu$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Uniformly bounded model", "weight": 1.0} -->

We define a random model obeying (1.13) as follows: take two arbitrary families of $n$ orthonormal vectors $\lbrack u_{1},\ldots,u_{n}\rbrack$ and $\lbrack v_{1},\ldots,v_{n}\rbrack$ obeying (1.13). We allow the $u_{i}$ and $v_{i}$ to be deterministic; for instance one could have $u_{i} = v_{i}$ for all $i \in {\lbrack n\rbrack}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Uniformly bounded model", "weight": 1.0} -->

Select $r$ left singular vectors $u_{\alpha{}},\ldots,u_{\alpha{(r)}}$ at random with replacement from the first family, and $r$ right singular vectors $v_{\beta{}},\ldots,v_{\beta{(r)}}$ from the second family, also at random. We do *not* require that the $\beta$ are chosen independently from the $\alpha$; for instance one could have ${\beta{(k)}} = {\alpha{(k)}}$ for all $k \in {\lbrack r\rbrack}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Uniformly bounded model", "weight": 1.0} -->

Set $M:={\sum_{k \in {\lbrack r\rbrack}}{\epsilon_{k}\sigma_{k}u_{\alpha{(k)}}v_{\beta{(k)}}^{\ast}}}$, where the signs ${\epsilon_{1},\ldots,\epsilon_{r}} \in {\{{- 1},{+ 1}\}}$ are chosen independently at random (with probability $1/2$ of each choice of sign), and ${\sigma_{1},\ldots,\sigma_{r}} > 0$ are arbitrary distinct positive numbers (which are allowed to depend on the previous random choices).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Uniformly bounded model", "weight": 1.0} -->

We emphasize that the only assumptions about the families $\lbrack u_{1},\ldots,u_{n}\rbrack$ and $\lbrack v_{1},\ldots,v_{n}\rbrack$ is that they have small components. For example, they may be the same. Also note that this model allows for any kind of dependence between the left and right singular selected vectors. For instance, we may select the same columns as to obtain a symmetric matrix as in the case where the two families are the same. Thus, one can think of our model as producing a generic matrix with uniformly bounded singular vectors.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Uniformly bounded model", "weight": 1.0} -->

For (1.8), we will use a beautiful concentration-of-measure result of McDiarmid.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Low-rank low-coherence model", "weight": 1.0} -->

When the rank is small, the assumption that the singular vectors are spread is sufficient to show that the parameter $\mu$ is small. To see this, suppose that the singular vectors obey (1.13). Then The first inequality follows from the Cauchy-Schwarz inequality for $a \neq a'$ and from the Frobenius norm bound This gives $\mu_{1} \leq {\mu_{B}\sqrt{r}}$. Also, by another application of Cauchy-Schwarz we have so that we also have $\mu_{2} \leq {\mu_{B}\sqrt{r}}$. In short, $\mu \leq {\mu_{B}\sqrt{r}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Low-rank low-coherence model", "weight": 1.0} -->

Our low-rank low-coherence model assumes that $r = {O{}}$ and that the singular vectors obey (1.13). When $\mu_{B} = {O{}}$, this model obeys the strong incoherence property with $\mu = {O{}}$. In this case, Theorem 1.1 ‣ 1.3

<!-- chunk {"id": "body-0034", "role": "body", "section": "Random orthogonal model", "weight": 1.0} -->

Our last model is borrowed from and assumes that the column matrices $\lbrack u_{1},\ldots,u_{r}\rbrack$ and $\lbrack v_{1},\ldots,v_{r}\rbrack$ are independent random orthogonal matrices, with no assumptions whatsoever on the singular values $\sigma_{1},\ldots,\sigma_{r}$. Note that this is a special case of the uniformly bounded model since this is equivalent to selecting two $n \times n$ random orthonormal bases, and then selecting the singular vectors as in Section 1.5.1. Since we know that the maximum entry of an $n \times n$ random orthogonal matrix is bounded by a constant times $\sqrt{\frac{\log n}{n}}$ with large probability, then Section 1.5.1 shows that this model obeys the strong incoherence property with $\mu = {O{({\log n})}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Random orthogonal model", "weight": 1.0} -->

Theorems 1.1 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"), 1.2 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion") then give

<!-- chunk {"id": "body-0036", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

The mathematical study of matrix completion began, which made slightly different incoherence assumptions than in this paper. Namely, let us say that the matrix $M$ obeys the *incoherence property* with a parameter $\mu_{0} > 0$ if for all $a \in {\lbrack n_{1}\rbrack}$, $b \in {\lbrack n_{2}\rbrack}$. Again, this implies $\mu_{0} \geq 1$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

In it was shown that if a fixed matrix $M$ obeys the incoherence property with parameter $\mu_{0}$, then nuclear minimization succeeds with large probability if provided that ${\mu_{0}r} \leq n^{1/5}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

Now consider a matrix $M$ obeying the strong incoherence property with $\mu = {O{}}$. Then since $\mu_{0} \geq 1$, (1.19) guarantees exact reconstruction only if $m \geq {Cn^{6/5}r{\log n}}$ (and $r = {O{(n^{1/5})}}$) while our results only need $nr\text{polylog}{(n)}$ samples. Hence, our results provide a substantial improvement over (1.19) at least in the regime which permits minimal sampling.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

We would like to note that there are obvious relationships between the best incoherence parameter $\mu_{0}$ and the best strong incoherence parameters $\mu_{1}$, $\mu_{2}$ for a given matrix $M$, which we take to be square for simplicity. On the one hand, (1.8) implies that so that one can take $\mu_{0} \leq {1 + {\mu_{1}/\sqrt{r}}}$. This shows that one can apply results from the incoherence model (in which we only know (1.18)) to our model (in which we assume strong incoherence). On the other hand, so that $\mu_{1} \leq {\mu_{0}\sqrt{r}}$. Similarly, $\mu_{2} \leq {\mu_{0}\sqrt{r}}$ so that one can transfer results in the other direction as well.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Nuclear norm minimization", "weight": 1.0} -->

We would like to mention another important paper inspired by compressed sensing, and which also recovers low-rank matrices from partial information. The model, however, assumes some sort of Gaussian measurements and is completely different from the completion problem discussed in this paper.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Spectral methods", "weight": 1.0} -->

An interesting new approach to the matrix completion problem has been recently introduced. This algorithm starts by trimming each row and column with too few entries; i.e. one replaces the entries in those rows and columns by zero. Then one computes the SVD of the trimmed matrix and truncate it as to only keep the top $r$ singular values (note that one would need to know $r$ *a priori*). Then under some conditions (including the incoherence property (1.18) with $\mu = {O{}}$), this work shows that accurate recovery is possible from a minimal number of samples, namely, on the order of $nr{\log n}$ samples. Having said this, this work is not directly comparable to ours because it operates in a different regime. Firstly, the results are asymptotic and are valid in a regime when the dimensions of the matrix tend to infinity in a fixed ratio while ours are not. Secondly, there is a strong assumption about the range of the singular values the unknown matrix can take on while we make no such assumption; they must be clustered so that no singular value can be too large or too small compared to the others.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Spectral methods", "weight": 1.0} -->

Finally, this work only shows approximate recovery---not exact recovery as we do here---although exact recovery results have been announced. This work is of course very interesting because it may show that methods---other than convex optimization---can also achieve minimal sampling bounds.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

We would like to conclude the tour of the results introduced in this paper with a simple lower bound, which highlights the fundamental role played by the coherence in controlling what is information-theoretically possible.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

This section proves Theorem 1.7 ‣ 1.7 Lower bounds ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"), which asserts that no method can recover an arbitrary $n \times n$ matrix of rank $r$ and coherence at most $\mu_{0}$ unless the number of random samples obeys (1.20 ‣ 1.7 Lower bounds ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")). As stated in the theorem, we establish lower bounds for the Bernoulli model, which then apply to the model where exactly $m$ entries are selected uniformly at random, see the Appendix for details.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

It may be best to consider a simple example first to understand the main idea behind the proof of Theorem 1.7 ‣ 1.7 Lower bounds ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"). Suppose that $r = 1$, $\mu_{0} > 1$ in which case $M = {xy^{\ast}}$. For simplicity, suppose that $y$ is fixed, say $y = {(1,\ldots,1)}$, and $x$ is chosen arbitrarily from the cube ${\lbrack 1,\sqrt{\mu_{0}}\rbrack}^{n}$ of ${\mathbb{R}}^{n}$. One easily verifies that $M$ obeys the coherence property with parameter $\mu_{0}$ (and in fact also obeys the strong incoherence property with a comparable parameter). Then to recover $M$, we need to see at least one entry per row.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

For instance, if the first row is unsampled, one has no information about the first coordinate $x_{1}$ of $x$ other than that it lies in $\lbrack 1,\sqrt{\mu_{0}}\rbrack$, and so the claim follows in this case by varying $x_{1}$ along the infinite set $\lbrack 1,\sqrt{\mu_{0}}\rbrack$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

Now under the Bernoulli model, the number of observed entries in the first row---and in any fixed row or column---is a binomial random variable with a number of trials equal to $n$ and a probability of success equal to $p$. Therefore, the probability $\pi_{0}$ that any row is unsampled is equal to $\pi_{0} = {({1 - p})}^{n}$. By independence, the probability that all rows are sampled at least once is ${({1 - \pi_{0}})}^{n}$, and any method succeeding with probability greater $1 - \delta$ would need or ${- {n\pi_{0}}} \geq {n{\log{({1 - \pi_{0}})}}} \geq {\log{({1 - \delta})}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

This type of simple analysis easily extends to general values of the rank $r$ and of the coherence. Without loss of generality, assume that $\ell:=\frac{n}{\mu_{0}r}$ is an integer, and consider a (self-adjoint) $n \times n$ matrix $M$ of rank $r$ of the form where the $\sigma_{k}$ are drawn arbitrarily from $\lbrack 0,1\rbrack$ (say), and the singular vectors $u_{1},\ldots,u_{r}$ are defined as follows: that is to say, $u_{k}$ vanishes everywhere except on a support of $\ell$ consecutive indices. Clearly, this matrix is incoherent with parameter $\mu_{0}$. Because the supports of the singular vectors are disjoint, $M$ is a block-diagonal matrix with diagonal blocks of size $\ell \times \ell$. We now argue as before.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

Recovery with positive probability is impossible unless we have sampled at least one entry per row of each diagonal block, since otherwise we would be forced to guess at least one of the $\sigma_{k}$ based on no information (other than that $\sigma_{k}$ lies in $\lbrack 0,1\rbrack$), and the theorem will follow by varying this singular value. Now the probability $\pi_{0}$ that the first row of the first block---and any fixed row of any fixed block---is unsampled is equal to ${({1 - p})}^{\ell}$. Therefore, any method succeeding with probability greater $1 - \delta$ would need which implies $\pi_{1} \leq {{2\delta}/n}$ just as before. With $\pi_{1} = {({1 - p})}^{\ell}$, this gives (1.20 ‣ 1.7 Lower bounds ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")) under the Bernoulli model.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

The second part of the theorem, namely, (1.21) follows from the equivalent characterization together with ${1 - e^{- x}} > {x - {x^{2}/2}}$ whenever $x \geq 0$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Strategy and Novelty", "weight": 1.0} -->

This section outlines the strategy for proving our main results, Theorems 1.1 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion") and 1.2 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"). The proofs of these theorems are the same up to a point where the arguments to estimate the moments of a certain random matrix differ. In this section, we present the common part of the proof, leading to two key moment estimates, while the proofs of these crucial estimates are the object of later sections.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Strategy and Novelty", "weight": 1.0} -->

One can of course prove our claims for the Bernoulli model with $p = {m/n^{2}}$ and transfer the results to the uniform model, by using the arguments in the appendix. For example, the probability that the recovery via (1.3) is not exact is at most twice that under the Bernoulli model.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Duality", "weight": 1.0} -->

We begin by recalling some calculations from \[7, Section 3\]. From standard duality theory, we know that the correct matrix $M \in {\mathbb{R}}^{n \times n}$ is a solution to (1.3) if and only if there exists a dual certificate $Y \in {\mathbb{R}}^{n_{1} \times n_{2}}$ with the property that $\mathcal{P}_{\Omega}{(Y)}$ is a subgradient of the nuclear norm at $M$, which we write as We recall the projection matrices $P_{U},P_{V}$ and the companion matrix $E$ defined by (1.6), (1.7). It is known that There is a more compact way to write (3.2).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Duality", "weight": 1.0} -->

Let $T \subset {\mathbb{R}}^{n \times n}$ be the span of matrices of the form $u_{k}y^{\ast}$ and $xv_{k}^{\ast}$ and let $T^{\perp}$ be its orthogonal complement. Let $\mathcal{P}_{T}:{{\mathbb{R}}^{n \times n}\rightarrow T}$ be the orthogonal projection onto $T$; one easily verifies the explicit formula and note that the complementary projection $\mathcal{P}_{T^{\perp}}:={\mathcal{I} - \mathcal{P}_{T}}$ is given by the formula In particular, $\mathcal{P}_{T^{\perp}}$ is a contraction: Then $Z \in {\partial{\| X\|}_{\ast}}$ if and only if With these preliminaries in place, establishes the following result.

<!-- chunk {"id": "body-0055", "role": "body", "section": "The dual certificate", "weight": 1.0} -->

Introduce the dual matrix $Y \in {\mathcal{P}_{\Omega}{({\mathbb{R}}^{n \times n})}} \subset {\mathbb{R}}^{n \times n}$ defined via By construction, ${\mathcal{P}_{\Omega}{(Y)}} = Y$, ${\mathcal{P}_{T}{(Y)}} = E$ and, therefore, we will establish that $M$ is the unique minimizer if one can show that The dual matrix $Y$ would then certify that $M$ is the unique solution, and this is the reason why we will refer to $Y$ as a *candidate certificate*. This certificate was also used.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The dual certificate", "weight": 1.0} -->

Before continuing, we would like to offer a little motivation for the choice of the dual matrix $Y$. It is not difficult to check that (3.10) is actually the solution to the following problem: Note that by the Pythagorean identity, $Y$ obeys The interpretation is now clear: among all matrices obeying ${\mathcal{P}_{\Omega}{(Z)}} = Z$ and ${\mathcal{P}_{T}{(Z)}} = E$, $Y$ is that element which minimizes ${\|{\mathcal{P}_{T^{\perp}}{(Z)}}\|}_{F}$. By forcing the Frobenius norm of $\mathcal{P}_{T^{\perp}}{(Y)}$ to be small, it is reasonable to expect that its spectral norm will be sufficiently small as well. In that sense, $Y$ defined via (3.10) is a very suitable candidate.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The dual certificate", "weight": 1.0} -->

Even though this is a different problem, our candidate certificate resembles---and is inspired by---that constructed in to show that $\ell_{1}$ minimization recovers sparse vectors from minimally sampled data.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Neumann series", "weight": 1.0} -->

We now develop a useful formula for the candidate certificate, and begin by introducing a normalized version $\mathcal{Q}_{\Omega}:{{\mathbb{R}}^{n \times n}\rightarrow{\mathbb{R}}^{n \times n}}$ of $\mathcal{P}_{\Omega}$, defined by the formula where $\mathcal{I}:{{\mathbb{R}}^{n \times n}\rightarrow{\mathbb{R}}^{n \times n}}$ is the identity operator on matrices (*not* the identity matrix $I \in {\mathbb{R}}^{n \times n}$!). Note that with the Bernoulli model for selecting $\Omega$, that $\mathcal{Q}_{\Omega}$ has expectation zero.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Neumann series", "weight": 1.0} -->

It is not hard to bound the tail of the series thanks to Theorem 3.2 ‣ 3.1 Duality ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"). First, this theorem bounds the spectral norm of $\mathcal{P}_{T}\mathcal{Q}_{\Omega}\mathcal{P}_{T}$ by the quantity $a$ in (3.7 ‣ 3.1 Duality ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")).

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Neumann series", "weight": 1.0} -->

For each $k_{0} \geq 0$, this gives provided that $a < {1/2}$. With $p = {m/n^{2}}$ and $a$ defined by (3.7 ‣ 3.1 Duality ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")) with $\beta = 4$, we have with probability at least $1 - n^{- 4}$. When ${k_{0} + 1} \geq {\log n}$, $n^{\frac{1}{k_{0} + 1}} \leq n^{\frac{1}{\log n}} = e$ and thus for each such a $k_{0}$, with the same probability.

<!-- chunk {"id": "body-0061", "role": "body", "section": "The Neumann series", "weight": 1.0} -->

To summarize this section, we conclude that since both our results assume that $m \geq {c_{0}\mu_{0}nr{\log n}}$ for some sufficiently large numerical constant $c_{0}$ (see the discussion at the end of Section 3.1), it now suffices to show that (say) with probability at least $1 - {n^{- 3}/4}$ (say).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Centering", "weight": 1.0} -->

We have already normalised $\mathcal{P}_{\Omega}$ to have "mean zero" in some sense by replacing it with $\mathcal{Q}_{\Omega}$. Now we perform a similar operation for the projection $\mathcal{P}_{T}:{X\mapsto{{{P_{U}X} + {XP_{V}}} - {P_{U}XP_{V}}}}$. The eigenvalues of $\mathcal{P}_{T}$ are centered around as this follows from the fact that $\mathcal{P}_{T}$ is a an orthogonal projection onto a space of dimension ${2nr} - r^{2}$. Therefore, we simply split $\mathcal{P}_{T}$ as so that the eigenvalues of $\mathcal{Q}_{T}$ are centered around zero. From now, $\rho$ and $\rho'$ will always be the numbers defined above.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Key estimates", "weight": 1.0} -->

To summarize the previous discussion, and in particular the bounds (3.20) and (3.14), we see everything reduces to bounding the spectral norm of ${({\mathcal{Q}_{\Omega}\mathcal{Q}_{T}})}^{k}\mathcal{Q}_{\Omega}{(E)}$ for $k = {0,1,\ldots,{\lfloor{\log n}\rfloor}}$. Providing good upper bounds on these quantities is the crux of the argument. We use the moment method, controlling a spectral norm a matrix by the trace of a high power of that matrix. We will prove two moment estimates which ultimately imply our two main results (Theorems 1.1 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion") and 1.2 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")) respectively.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Novelty", "weight": 1.0} -->

As explained earlier, this paper derives near-optimal sampling results which are stronger than those. One of the reasons underlying this improvement is that we use completely different techniques. In details, constructs the dual certificate (3.10) and proceeds by showing that ${\|{\mathcal{P}_{T^{\perp}}{(Y)}}\|} < 1$ by bounding each term in the series ${\sum_{k \geq 0}{\|{{({\mathcal{Q}_{\Omega}\mathcal{P}_{T}})}^{k}\mathcal{Q}_{\Omega}{(E)}}\|}} < 1$. Further, to prove that the early terms (small values of $k$) are appropriately small, the authors employ a sophisticated array of tools from asymptotic geometric analysis, including noncommutative Khintchine inequalities, decoupling techniques of Bourgain and Tzafiri and of de la Peña, and large deviations inequalities.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Novelty", "weight": 1.0} -->

They bound each term individually up to $k = 4$ and use the same argument as that in Section 3.3 to bound the rest of the series. Since the tail starts at $k_{0} = 5$, this gives that a sufficient condition is that the number of samples exceeds a constant times $\mu_{0}n^{6/5}nr{\log n}$. Bounding each term ${\|{{({\mathcal{Q}_{\Omega}\mathcal{P}_{T}})}^{k}\mathcal{Q}_{\Omega}{(E)}}\|}^{k}$ with the tools put forth in for larger values of $k$ becomes increasingly delicate because of the coupling between the indicator variables defining the random set $\Omega$. In addition, the noncommutative Khintchine inequality seems less effective in higher dimensions; that is, for large values of $k$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Novelty", "weight": 1.0} -->

Informally speaking, the reason for this seems to be that the types of random sums that appear in the moments ${({\mathcal{Q}_{\Omega}\mathcal{P}_{T}})}^{k}\mathcal{Q}_{\Omega}{(E)}$ for large $k$ involve complicated combinations of the coefficients of $\mathcal{P}_{T}$ that are not simply components of some product matrix, and which do not simplify substantially after a direct application of the Khintchine inequality.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Novelty", "weight": 1.0} -->

In this paper, we use a very different strategy to estimate the spectral norm of ${({\mathcal{Q}_{\Omega}\mathcal{Q}_{T}})}^{k}\mathcal{Q}_{\Omega}{(E)}$, and employ moment methods, which have a long history in random matrix theory, dating back at least to the classical work of Wigner. We raise the matrix $A:={{({\mathcal{Q}_{\Omega}\mathcal{Q}_{T}})}^{k}\mathcal{Q}_{\Omega}{(E)}}$ to a large power $j$ so that (the largest element dominates the sum). We then need to compute the expectation of the right-hand side, and reduce matters to a purely combinatorial question involving the statistics of various types of paths in a plane. It is rather remarkable that carrying out these combinatorial calculations nearly give the quantitatively correct answer; the moment method seems to come close to giving the ultimate limit of performance one can expect from nuclear-norm minimization.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Novelty", "weight": 1.0} -->

As we shall shortly see, the expression ${trace}{(A^{\ast}A)}^{j}$ expands as a sum over "paths" of products of various coefficients of the operators $\mathcal{Q}_{\Omega},\mathcal{Q}_{T}$ and the matrix $E$. These paths can be viewed as complicated variants of Dyck paths. However, it does not seem that one can simply invoke standard moment method calculations in the literature to compute this sum, as in order to obtain efficient bounds, we will need to take full advantage of identities such as ${\mathcal{P}_{T}\mathcal{P}_{T}} = \mathcal{P}_{T}$ (which capture certain cancellation properties of the coefficients of $\mathcal{P}_{T}$ or $\mathcal{Q}_{T}$) to simplify various components of this sum. It is only after performing such simplifications that one can afford to estimate all the coefficients by absolute values and count paths to conclude the argument.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Moments", "weight": 1.0} -->

Let $j \geq 0$ be a fixed integer. The goal of this section is to develop a formula for This will clearly be of use in the proofs of the moment bounds (Theorems 3.4 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"), 3.6 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")).

<!-- chunk {"id": "body-0070", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

We first write the matrix $A$ in components as for some scalars $A_{ab}$, where $e_{ab}$ is the standard basis for the $n \times n$ matrices and $A_{ab}$ is the ${(a,b)}^{th}$ entry of $A$. Then where we adopt the cyclic convention $a_{j + 1} = a_{1}$. Equivalently, we can write where the sum is over all ${a_{i,\mu},b_{i,\mu}} \in {\lbrack n\rbrack}$ for ${i \in {\lbrack j\rbrack}},{\mu \in {\{ 0,1\}}}$ obeying the compatibility conditions with the cyclic convention $a_{{j + 1},0} = a_{1,0}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

*Example.* If $j = 2$, then we can write ${trace}{(A^{\ast}A)}^{j}$ as where the sum is over all ${a_{1,0},a_{1,1},a_{2,0},a_{2,1},b_{1,0},b_{1,1},b_{2,0},b_{2,1}} \in {\lbrack n\rbrack}$ obeying the compatibility conditions *Remark.* The sum in (4.2) can be viewed as over all closed paths of length $2j$ in ${\lbrack n\rbrack} \times {\lbrack n\rbrack}$, where the edges of the paths alternate between "horizontal rook moves" and "vertical rook moves" respectively; see Figure 1.

<!-- chunk {"id": "body-0072", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

Second, write $\mathcal{Q}_{T}$ and $\mathcal{Q}_{\Omega}$ in coefficients as where $c_{{ab},{a'b'}}$ is given by (3.23), and where $\xi_{ab}$ are the iid, zero-expectation random variables With this, we have for any ${a_{0},b_{0}} \in {\lbrack n\rbrack}$. Note that this formula is even valid in the base case $k = 0$, where it simplifies to just $A_{a_{0}b_{0}} = {\xi_{a_{0}b_{0}}E_{a_{0}b_{0}}}$ due to our conventions on trivial sums and empty products.

<!-- chunk {"id": "body-0073", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

*Remark.* One can view the right-hand side of (4.3) as the sum over paths of length $k + 1$ in ${\lbrack n\rbrack} \times {\lbrack n\rbrack}$ starting at the designated point $(a_{0},b_{0})$ and ending at some arbitrary point $(a_{k},b_{k})$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

Each edge (from $(a_{i},b_{i})$ to $(a_{i + 1},b_{i + 1})$) may be a horizontal or vertical "rook move" (in that at least one of the $a$ or $b$ coordinates does not change^22^2Unlike the ordinary rules of chess, we will consider the trivial move when $a_{i + 1} = a_{i}$ *and* $b_{i + 1} = b_{i}$ to also qualify as a "rook move", which is simultaneously a horizontal and a vertical rook move.), or a "non-rook move" in which both the $a$ and $b$ coordinates change. It will be important later on to keep track of which edges are rook moves and which ones are not, basically because of the presence of the delta functions $1_{a = a'},1_{b = b'}$ in (3.23).

<!-- chunk {"id": "body-0075", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

Each edge in this path is weighted by a $c$ factor, and each vertex in the path is weighted by a $\xi$ factor, with the final vertex also weighted by an additional $E$ factor. It is important to note that the path is allowed to cross itself, in which case weights such as $\xi^{2}$, $\xi^{3}$, etc. may appear, see Figure 2.

<!-- chunk {"id": "body-0076", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

Inserting (4.3) into (4.2), we see that $X$ can thus be expanded as where the sum $\sum_{\ast}$ is over all combinations of ${a_{i,\mu,l},b_{i,\mu,l}} \in {\lbrack n\rbrack}$ for $i \in {\lbrack j\rbrack}$, $\mu \in {\{ 0,1\}}$ and $0 \leq l \leq k$ obeying the compatibility conditions with the cyclic convention $a_{{j + 1},0,0} = a_{1,0,0}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

*Example.* Continuing our running example $j = k = 2$, we have where $a_{i,\mu,l}$ for $i = {1,2}$, $\mu = {0,1}$, $l = {0,1,2}$ obey the compatibility conditions Note that despite the small values of $j$ and $k$, this is already a rather complicated sum, ranging over $n^{2j{({{2k} + 1})}} = n^{20}$ summands, each of which is the product of ${4j{({k + 1})}} = 24$ terms.

<!-- chunk {"id": "body-0078", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

*Remark.* The expansion (4.4) is the sum over a sort of combinatorial "spider", whose "body" is a closed path of length $2j$ in ${\lbrack n\rbrack} \times {\lbrack n\rbrack}$ of alternating horizontal and vertical rook moves, and whose $2j$ "legs" are paths of length $k$, emanating out of each vertex of the body. The various "segments" of the legs (which can be either rook or non-rook moves) acquire a weight of $c$, and the "joints" of the legs acquire a weight of $\xi$, with an additional weight of $E$ at the tip of each leg. To complicate things further, it is certainly possible for a vertex of one leg to overlap with another vertex from either the same leg or a different leg, introducing weights such as $\xi^{2}$, $\xi^{3}$, etc.; see Figure 3.

<!-- chunk {"id": "body-0079", "role": "body", "section": "First step: expansion", "weight": 1.0} -->

As one can see, the set of possible configurations that this "spider" can be in is rather large and complicated.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Second step: collecting rows and columns", "weight": 1.0} -->

We now group the terms in the expansion (4.4) into a bounded number of components, depending on how the various horizontal coordinates $a_{i,\mu,l}$ and vertical coordinates $b_{i,\mu,l}$ overlap.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Second step: collecting rows and columns", "weight": 1.0} -->

{(i,\mu,l)}$ otherwise. Define $t_{i,\mu,l}$ using $b_{i,\mu,l}$ similarly. We observe the *cyclic condition* with the cyclic convention $s_{{j + 1},0,0} = s_{1,0,0}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Second step: collecting rows and columns", "weight": 1.0} -->

*Example.* Suppose that $j = 2$, $k = 1$, and $n \geq 30$, with the $(a_{i,\mu,l},b_{i,\mu,l})$ given in lexicographical ordering as Then we would have Observe that the conditions (4.5) hold for this example, which then forces (4.6) to hold also.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Second step: collecting rows and columns", "weight": 1.0} -->

In addition to the property (4.6), we see from construction of $(s,t)$ that for any ${(i,\mu,l)} \in {{\lbrack j\rbrack} \times {\{ 0,1\}} \times {\{ 0,\ldots,k\}}}$, the sets are initial segments, i.e. of the form $\lbrack m\rbrack$ for some integer $m$. Let us call pairs $(s,t)$ of sequences with this property, as well as the property (4.6), *admissible*; thus for instance the sequences in the above example are admissible. Given an admissible pair $(s,t)$, if we define the sets $J$, $K$ by then we observe that ${J = {\lbrack{|J|}\rbrack}},{K = {\lbrack{|K|}\rbrack}}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Second step: collecting rows and columns", "weight": 1.0} -->

*Example.* Continuing the previous example, we have $J = {\lbrack 3\rbrack}$, $K = {\lbrack 4\rbrack}$, with the injections $\alpha:{{\lbrack 3\rbrack}\rightarrow{\lbrack n\rbrack}}$ and $\beta:{{\lbrack 4\rbrack}\rightarrow{\lbrack n\rbrack}}$ defined by Conversely, any admissible pair $(s,t)$ and injections $\alpha,\beta$ determine $a_{i,\mu,l}$ and $b_{i,\mu,l}$. Because of this, we can thus expand $X$ as where the outer sum is over all admissible pairs $(s,t)$, and the inner sum is over all injections.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Second step: collecting rows and columns", "weight": 1.0} -->

*Remark.* As with preceding identities, the above formula is also valid when $k = 0$ (with our conventions on trivial sums and empty products), in which case it simplifies to *Remark.* One can think of $(s,t)$ as describing the combinatorial "configuration" of the "spider" ${({(a_{i,\mu,l},b_{i,\mu,l})})}_{{(i,\mu,l)} \in {{\lbrack j\rbrack} \times {\{ 0,1\}} \times {\{ 0,\ldots,k\}}}}$ - it determines which vertices of the spider are equal to, or on the same row or column as, other vertices of the spider. The injections $\alpha,\beta$ then enumerate the ways in which such a configuration can be "represented" inside the grid ${\lbrack n\rbrack} \times {\lbrack n\rbrack}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Third step: computing the expectation", "weight": 1.0} -->

The expansion we have for $X$ looks quite complicated. However, the fact that the $\xi_{ab}$ are independent and have mean zero allows us to simplify this expansion to a significant degree. Indeed, observe that the random variable $\Xi:={\prod_{i \in {\lbrack j\rbrack}}{\prod_{\mu = 0}^{1}{\prod_{l = 0}^{L}\xi_{\alpha{(s_{i,\mu,l})}\beta{(t_{i,\mu,l})}}}}}$ has zero expectation if there is any pair in $J \times K$ which can be expressed exactly once in the form $(s_{i,\mu,l},t_{i,\mu,l})$. Thus we may assume that no pair can be expressed exactly once in this manner.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Third step: computing the expectation", "weight": 1.0} -->

If $\delta$ is a Bernoulli variable with ${{\mathbb{P}}{({\delta = 1})}} = p = {1 - {{\mathbb{P}}{({\delta = 0})}}}$, then for each $s \geq 0$, one easily computes The value of the expectation of ${\mathbb{E}}\Xi$ does not depend on the choice of $\alpha$ or $\beta$, and the calculation above shows that $\Xi$ obeys Applying this estimate and the triangle inequality, we can thus bound $X$ by where the sum is over those admissible $(s,t)$ such that each element of $\Omega$ is visited at least twice by the sequence $(s_{i,\mu,l},t_{i,\mu,l})$; we shall call such $(s,t)$ *strongly admissible*.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Third step: computing the expectation", "weight": 1.0} -->

We will use the bound (4.10) as a starting point for proving the moment estimates (3.25 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")) and (3.27 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Third step: computing the expectation", "weight": 1.0} -->

*Example.* The pair $(s,t)$ in the Example in Section 4.2 is admissible but not strongly admissible, because not every element of the set $\Omega$ (which, in this example, is $\{{},{},{},$ ${{},{}},$ ${},{}\}$) is visited twice by the $(s,t)$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Third step: computing the expectation", "weight": 1.0} -->

*Remark.* Once again, the formula (4.10) is valid when $k = 0$, with the usual conventions on empty products (in particular, the factor involving the $c$ coefficients can be deleted in this case).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

This section establishes (3.25 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")) under the assumptions of Theorem 1.1 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"), which is the easier of the two moment estimates. Here we shall just take the absolute values in (4.10) inside the summation and use the estimates on the coefficients given to us by hypothesis.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

Indeed, starting with (4.10) and the triangle inequality and applying (1.9) together with (3.23) gives where we recall that $r_{\mu} = {\mu^{2}r}$, and $Q$ is the set of all ${(i,\mu,l)} \in {{\lbrack j\rbrack} \times {\{ 0,1\}} \times {\lbrack k\rbrack}}$ such that $s_{i,\mu,{l - 1}} \neq s_{i,\mu,l}$ and $t_{i,\mu,{l - 1}} \neq t_{i,\mu,l}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

Thinking of the sequence $\{{(s_{i,\mu,l},t_{i,\mu,l})}\}$ as a path in $J \times K$, we have that ${(i,\mu,l)} \in Q$ if and only if the move from $(s_{i,\mu,{l - 1}},t_{i,\mu,{l - 1}})$ to $(s_{i,\mu,l},t_{i,\mu,l})$ is neither horizontal nor vertical; per our earlier discussion, this is a "non-rook" move.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

*Example.* The example in Section 4.2 is admissible, but not strongly admissible. Nevertheless, the above definitions can still be applied, and we see that $Q = {\{{},{},{},{}\}}$ in this case, because all of the four associated moves are non-rook moves.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

As the number of injections $\alpha,\beta$ is at most $n^{|J|},n^{|K|}$ respectively, we thus have which we rearrange slightly as Since $(s,t)$ is strongly admissible and every point in $\Omega$ needs to be visited at least twice, we see that Also, since $Q \subset {{\lbrack j\rbrack} \times {\{ 0,1\}} \times {\lbrack k\rbrack}}$, we have the trivial bound This ensures that From the hypotheses of Theorem 1.1 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion") we have ${np} \geq r_{\mu}^{2}$, and thus *Remark.* In the case where $k = 0$ in which $Q = \varnothing$, one can easily obtain a better estimate, namely, (if ${np} \geq r_{\mu}$) Call a triple $(i,\mu,l)$ *recycled*

<!-- chunk {"id": "body-0096", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

*Example.* The example in Section 4.2 is admissible, but not strongly admissible. Nevertheless, the above definitions can still be applied, and we see that the triples are all recycled (because they either reuse an existing value of $s$ or $t$ or both), while the triple $$ is totally recycled (it visits the same location as the earlier triple $$). Thus in this case, we have $Q' = {\{{},{},{}\}}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Quadratic bound in the rank", "weight": 1.0} -->

We observe that if ${(i,\mu,l)} \in {{\lbrack j\rbrack} \times {\{ 0,1\}} \times {\lbrack k\rbrack}}$ is not recycled, then it must have been reached from $(i,\mu,{l - 1})$ by a non-rook move, and thus $(i,\mu,l)$ lies in $Q$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Linear bound in the rank", "weight": 1.0} -->

We now prove the more sophisticated moment estimate (3.27 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")) under the hypotheses of Theorem 1.2 ‣ 1.3 Main results ‣ 1 Introduction ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion"). Here, we cannot afford to take absolute values immediately, as in the proof of (3.25 ‣ 3.5 Key estimates ‣ 3 Strategy and Novelty ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion")), but first must exploit some algebraic cancellation properties in the coefficients $c_{{ab},{a'b'}}$, $E_{ab}$ appearing in (4.10) to simplify the sum.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Cancellation identities", "weight": 1.0} -->

Recall from (3.23) that the coefficients $c_{{ab},{a'b'}}$ are defined in terms of the coefficients $U_{a,a'}$, $V_{b,b'}$ introduced in (3.22). We recall the symmetries ${U_{a,a'} = U_{a',a}},{V_{b,b'} = V_{b',b}}$ and the projection identities the first identity follows from the matrix identity after one writes the projection identity $P_{U}^{2} = P_{U}$ in terms of $Q_{U}$ using (3.21), and similarly for the second identity.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Reduction to a summand bound", "weight": 1.0} -->

Just as before, our goal is to estimate We recall the bound (4.10), and expand out each of the $c$ coefficients using (3.23) into three terms. To describe the resulting expansion of the sum we need more notation.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Reduction to a summand bound", "weight": 1.0} -->

The sets $\mathcal{L}_{U}\backslash\mathcal{L}_{V}$, $\mathcal{L}_{V}\backslash\mathcal{L}_{U}$, $\mathcal{L}_{U} \cap \mathcal{L}_{V}$ will correspond to the three terms $1_{b = b'}U_{a,a'}$, $1_{a = a'}V_{b,b'}$, $U_{a,a'}V_{b,b'}$ appearing in (3.23). With this notation, we expand the product where the sum is over all partitions as above, and which we can rearrange as From this and the triangle inequality, we observe the bound where the sum ranges over all strongly admissible quadruplets, and *Remark.* A strongly admissible quadruplet can be viewed as the configuration of a "spider" with several additional constraints. Firstly, the spider must visit each of its vertices at least twice (strong admissibility).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Reduction to a summand bound", "weight": 1.0} -->

When ${(i,\mu,l)} \in {{\lbrack j\rbrack} \times {\{ 0,1\}} \times {\lbrack k\rbrack}}$ lies out of $\mathcal{L}_{U}$, then only horizontal rook moves are allowed when reaching $(i,\mu,l)$ from $(i,\mu,{l - 1})$; similarly, when $(i,\mu,l)$ lies out of $\mathcal{L}_{V}$, then only vertical rook moves are allowed from $(i,\mu,{l - 1})$ to $(i,\mu,l)$. In particular, non-rook moves are only allowed inside $\mathcal{L}_{U} \cap \mathcal{L}_{V}$; in the notation of the previous section, we have $Q \subset {\mathcal{L}_{U} \cap \mathcal{L}_{V}}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Reduction to a summand bound", "weight": 1.0} -->

Note though that while one has the *right* to execute a non-rook move to $\mathcal{L}_{U} \cap \mathcal{L}_{V}$, it is not mandatory; it could still be that $(s_{i,\mu,{l - 1}},t_{i,\mu,{l - 1}})$ shares a common row or column (or even both) with $(s_{i,\mu,l},t_{i,\mu,l})$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "First case: an unguarded non-rook move", "weight": 1.0} -->

When we have such an unguarded non-rook move, we can "erase" the element $(i_{0},\mu_{0},l_{0})$ from $\mathcal{L}_{U} \cap \mathcal{L}_{V}$ by replacing $\mathcal{C} = {(j,k,J,K,s,t,\mathcal{L}_{U},\mathcal{L}_{V})}$ by the "stretched" variant $\mathcal{C}' = {(j',k',J',K',s',}$ $t',\mathcal{L}_{U}',\mathcal{L}_{V}')$, defined as follows: All of this is illustrated in Figure 5.

<!-- chunk {"id": "body-0105", "role": "body", "section": "First case: an unguarded non-rook move", "weight": 1.0} -->

One can check that $\mathcal{C}'$ is still a configuration, and $X_{\mathcal{C}'}$ is exactly equal to $X_{\mathcal{C}}$; informally what has happened here is that a single "non-rook" move (which contributed both a $U_{a,a'}$ factor and a $V_{b,b'}$ factor to the summand in $X_{\mathcal{C}}$) has been replaced with an equivalent pair of two rook moves (one of which contributes the $U_{a,a'}$ factor, and the other contributes the $V_{b,b'}$ factor).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

Next, given any $x \in J$, define the *row multiplicity* $\tau_{x}$ to be and similarly for any $y \in K$, define the *column multiplicity* $\tau^{y}$ to be *Remark.* Informally, $\tau_{x}$ measures the number of times $\alpha{(x)}$ appears in (6.5), and similarly for $\tau^{y}$ and $\beta{(y)}$. Alternatively, one can think of $\tau_{x}$ as counting the number of times the spider has the opportunity to "enter" and "exit" the row $s = x$, and similarly $\tau^{y}$ measures the number of opportunities to enter or exit the column $t = y$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

By surjectivity we know that $\tau_{x},\tau^{y}$ are strictly positive for each $x \in J$, $y \in K$. We also observe that $\tau_{x},\tau^{y}$ must be even. To see this, write Now observe that if ${(i,\mu,l)} \in {\Gamma_{+}\backslash\mathcal{L}_{U}}$, then $1_{{s{(i,\mu,l)}} = x} = 1_{{s{(i,\mu,{l - 1})}} = x}$. Thus we have But we can telescope this to and the right-hand side vanishes by (4.6), showing that $\tau_{x}$ is even, and similarly $\tau^{y}$ is even.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

In this subsection, we dispose of the case of a low-multiplicity row, or more precisely when $\tau_{x} = 2$ for some $x \in J$. By symmetry, the argument will also dispose of the case of a low-multiplicity column, when $\tau^{y} = 2$ for some $y \in K$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

Now let us look at the terms in (6.5) which involve $\alpha{(x)}$. Since $\tau_{x} = 2$, there are only two such terms, and each of the terms are either of the form $U_{{\alpha{(x)}},{\alpha{(x')}}}$ or $E_{{\alpha{(x)}},{\beta{(y)}}}$ for some $y \in K$ or $x' \in {J\backslash{\{ x\}}}$. We now have to divide into three subcases.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

Subcase 1: (6.5) contains two terms $U_{{\alpha{(x)}},{\alpha{(x')}}}$, $U_{{\alpha{(x)}},{\alpha{(x^{\operatorname{\prime\prime}})}}}$. Figure 6(a) for a typical configuration in which this is the case.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

The idea is to use the identity (6.1) to "delete" the row $x$, thus reducing ${|J|} + {|K|}$ and allowing us to use an induction hypothesis. Accordingly, let us define $\overset{\sim}{J}:={J\backslash{\{ j\}}}$, and let $\overset{\sim}{\alpha}:{\overset{\sim}{J}\rightarrow{\lbrack n\rbrack}}$ be the restriction of $\alpha$ to $\overset{\sim}{J}$. We also write $a:={\alpha{(x)}}$ for the deleted row $a$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

This deals with the case when there are two $U$ terms involving $\alpha{(x)}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

A typical case here is depicted in Figure 10.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

The strategy here is similar to Subcase 1, except that one uses (6.3) instead of (6.1). Letting $\overset{\sim}{J},\overset{\sim}{\alpha},a$ be as before, we can express (6.5) as where the $\ldots$ denotes the product of all the terms in (6.5) other than $U_{{\alpha{(x)}},{\alpha{(x')}}}$ and $E_{{\alpha{(x)}},{\beta{(y)}}}$, but with $\alpha$ replaced by $\overset{\sim}{\alpha}$, and $\overset{\sim}{\alpha},\beta$ ranging over injections from $\overset{\sim}{J}$ and $K$ to $\lbrack n\rbrack$ respectively.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

The contribution of the final terms in (6.11) are treated in exactly the same way as the final terms in (6.10), and the main term $E_{{\overset{\sim}{\alpha}{(x')}},{\beta{(y)}}}$ is treated in exactly the same way as the term $U_{{\overset{\sim}{\alpha}{(x')}},{\overset{\sim}{\alpha}{(x^{\operatorname{\prime\prime}})}}}$ in (6.10). This concludes the treatment of the case when there is one $U$ term and one $E$ term involving $\alpha{(x)}$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

A typical case here is depicted in 11. The strategy here is similar to that in the previous two subcases, but now one uses (6.4) rather than (6.1). The combinatorics of the situation are, however, slightly different.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

By considering the path from $E_{{\alpha{(x)}},{\beta{(y)}}}$ to $E_{{\alpha{(x)}},{\beta{(y')}}}$ along the spider, we see (from the hypothesis $\tau_{x} = 2$) that this path must be completely horizontal (with no elements of $\mathcal{L}_{U}$ present), and the two legs of the spider that give rise to $E_{{\alpha{(x)}},{\beta{(y)}}}$, $E_{{\alpha{(x)}},{\beta{(y')}}}$ at their tips must be adjacent, with their bases connected by a horizontal line segment.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

In other words, up to interchange of $y$ and $y'$, and cyclic permutation of the $\lbrack j\rbrack$ indices, we may assume that for all $0 \leq l \leq {k{}}$ and $0 \leq l' \leq {k{}}$, where the index $2$ is understood to be identified with $1$ in the degenerate case $j = 1$. Also, $\mathcal{L}_{U}$ cannot contain any triple of the form $(1,1,l)$ for $l \in {\lbrack{k{}}\rbrack}$ or $(2,0,l')$ for $l' \in {\lbrack{k{}}\rbrack}$ (and so all these triples lie in $\mathcal{L}_{V}$ instead).

<!-- chunk {"id": "body-0119", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

For technical reasons we need to deal with the degenerate case $j = 1$ separately. In this case, $s$ is identically equal to $x$, and so (6.5) simplifies to In the extreme degenerate case when ${k{}} = {k{}} = 0$, the sum is just ${\sum_{{a,b} \in {\lbrack n\rbrack}}E_{ab}^{2}} = r$, which is acceptable, so we may assume that ${{k{}} + {k{}}} > 0$. We may assume that the column multiplicity $\tau^{\overset{\sim}{y}} \geq 4$ for every $\overset{\sim}{y} \in K$, since otherwise we could use (the reflected form of) one of the previous two subcases to conclude (6.6) from the induction hypothesis.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

Using (6.4) followed by (1.8a) we have and so by (1.8b) we can bound The number of possible $\beta$ is at most $n^{|K|}$, so to establish (6.6) in this case it suffices to show that Observe that in this degenerate case $j = 1$, we have ${|\Omega|} = {|K|}$ and ${|\Gamma|} = {{k{}} + {k{}} + 2}$. One then checks that the claim is true when $r_{\mu} = 1$, so it suffices to check that the other extreme case $r_{\mu} = n$, i.e.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

But as $\tau^{y} \geq 4$ for all $k$, every element in $K$ must be visited at least twice, and the claim follows.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

Now we deal with the non-degenerate case $j > 1$. Letting $\overset{\sim}{J},\overset{\sim}{\alpha},a$ be as in previous subcases, we can express (6.5) as where the $\ldots$ denotes the product of all the terms in (6.5) other than $E_{{\alpha{(x)}},{\beta{(y)}}}$ and $E_{{\alpha{(x)}},{\beta{(y')}}}$, but with $\alpha$ replaced by $\overset{\sim}{\alpha}$, and $\overset{\sim}{\alpha},\beta$ ranging over injections from $\overset{\sim}{J}$ and $K$ to $\lbrack n\rbrack$ respectively.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

The final terms are treated here in exactly the same way as the final terms in (6.10) or (6.11). Now we consider the main term $V_{{\beta{(y)}},{\beta{(y')}}}$. The contribution of this term will be of the form $X_{\mathcal{C}'}$, where the configuration $\mathcal{C}'$ is formed from $\mathcal{C}$ by "detaching" the two legs ${(i,\mu)} = {{},{}}$ from the spider, "gluing them together" at the tips using the $V_{{\beta{(y)}},{\beta{(y')}}}$ term, and then "inserting" those two legs into the base of the ${(i,\mu)} = {}$ leg.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

To explain this procedure more formally, observe that the $\ldots$ term in (6.12) can be expanded further (isolating out the terms coming from ${(i,\mu)} = {{},{}}$) as where the $\ldots$ now denote all the terms that do not come from ${(i,\mu)} = {}$ or ${(i,\mu)} = {}$, and we have reversed the order of the second product for reasons that will be clearer later.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

Recalling that $y = {t{(1,1,{k{}})}}$ and $y' = {t{(2,0,{k{}})}}$, we see that the contribution of the first term of (6.13) to (6.12) is now of the form But this expression is simply $X_{\mathcal{C}'}$, where the configuration of $\mathcal{C}'$ is formed from $\mathcal{C}$ in the following fashion: $j'$ is equal to $j - 1$, $J'$ is equal to $\overset{\sim}{J}$, and $K'$ is equal to $K$.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Second case: a low multiplicity row or column, no unguarded non-rook moves", "weight": 1.0} -->

This handles the contribution of the $V_{{\beta{(y)}},{\beta{(y')}}}$ term. The $\rho1_{y = y'}$ term is treated similarly, except that there is no edge between the points $({s{}},{t{(2,0,{k{}})}})$ and $({s{}},{t{(1,1,{k{}})}})$ (which are now equal, since $y = y'$). This reduces the analogue of $|\Gamma'|$ to ${|\Gamma|} - 2$, but the additional factor of $\rho$ (which is at most $r_{\mu}/n$) compensates for this. We omit the details. This concludes the treatment of the third subcase.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Third case: High multiplicity rows and columns", "weight": 1.0} -->

After eliminating all of the previous cases, we may now may assume (since $\tau_{x}$ is even) that and similarly we may assume that We have now made the maximum use we can of the cancellation identities (6.1), (6.3), (6.4), and have no further use for them. Instead, we shall now place absolute values everywhere and estimate $X_{\mathcal{C}}$ using (1.9), (1.8a), (1.8b), obtaining the bound Comparing this with (6.6), we see that it will suffice (by taking $C_{0}$ large enough) to show that Using the extreme cases $r_{\mu} = 1$ and $r_{\mu} = n$ as test cases, we see that our task is to show that The first inequality (6.16) is proven by Lemma 5.1 ‣ 5 Quadratic bound in the rank ‣ The Power of Convex Relaxation: Near-Optimal Matrix Completion").

<!-- chunk {"id": "body-0128", "role": "body", "section": "Third case: High multiplicity rows and columns", "weight": 1.0} -->

The second is a consequence of the double counting identity where the inequality follows from (6.14)--(6.15) (and we don't even need the $+ 1$ in this case).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Discussion", "weight": 1.5} -->

Interestingly, there is an emerging literature on the development of efficient algorithms for solving the nuclear-norm minimization problem (1.3). For instance the authors show that the singular-value thresholding algorithm can solve certain problem instances in which the matrix has close to a billion unknown entries in a matter of minutes on a personal computer. Hence, the near-optimal sampling results introduced in this paper are practical and, therefore, should be of consequence to practitioners interested in recovering low-rank matrices from just a few entries.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Discussion", "weight": 1.5} -->

To be broadly applicable, however, the matrix completion problem needs to be robust vis a vis noise. That is, if one is given a few entries of a low-rank matrix contaminated with a small amount of noise, one would like to be able to guess the missing entries, perhaps not exactly, but accurately. We actually believe that the methods and results developed in this paper are amenable to the study of "the noisy matrix completion problem" and hope to report on our progress in a later paper.
