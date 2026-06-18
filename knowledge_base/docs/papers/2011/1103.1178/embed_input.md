<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Simplified Approach to Recovery Conditions for Low Rank Matrices

Topics include Low-rank recovery, Matrix recovery, Restricted isometry property, Nullspace conditions, Nuclear norm minimization, Compressed sensing, Singular values.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides a cleaner route from sparse-vector recovery theory to low-rank matrix recovery by using a key inequality on singular values. The payoff is simpler proofs and stronger RIP and nullspace recovery conditions for nuclear-norm and related low-rank reconstruction methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recovering sparse vectors and low-rank matrices from noisy linear measurements has been the focus of much recent research. Various reconstruction algorithms have been studied, including l_1 and nuclear norm minimization as well as l_p minimization with p < 1. These algorithms are known to succeed if certain conditions on the measurement map are satisfied. Proofs of robust recovery for matrices have so far been much more involved than in the vector case. In this paper, we show how several robust classes of recovery conditions can be extended from vectors to matrices in a simple and transparent way, leading to the best known restricted isometry and nullspace conditions for matrix recovery. Our results rely on the ability to "vectorize" matrices through the use of a key singular value inequality.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recovering sparse vectors and low-rank matrices from noisy linear measurements, with applications in compressed sensing and machine learning, has been the focus of much recent research. The Restricted Isometry Property (RIP) was introduced by Candès and Tao in and has played a major role in proving recoverability of sparse signals from compressed measurements. The first recovery algorithm that was analyzed using RIP was $\ell_{1}$ minimization. Since then, many algorithms including GraDes, Reweighed $\ell_{1}$, and CoSaMP have been analyzed using RIP. Analogous to the vector case, RIP has also been used in the analysis of algorithms for *low rank matrix recovery*, for example Nuclear Norm Minimization, SVP, Reweighted Trace Minimization and AdMiRA. Other recovery conditions have also been proposed for recovery of both sparse vectors and low-rank matrices including the Null Space Property and the Spherical Section Property (also known as the 'almost Euclidean' property) for the nullspace. The first matrix RIP result was given in where it was shown that the RIP is sufficient for low rank recovery using nuclear norm minimization, and that it holds with high probability as long as number of measurements are sufficiently large.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This analysis was improved in to require a minimal order of measurements. Recently, improved the RIP constants with a stronger analysis similar to.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we show that if a set of conditions are sufficient for the robust recovery of sparse vectors with sparsity at most $k$, then the "extension" (defined later) of the same set of conditions are sufficient for the robust recovery of low rank matrices up to rank $k$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the recovery analysis in and (Theorem 2.4) is complicated and lengthy, our results (see "Main Theorem") are easily derived due to the use of a key singular value inequality (Lemma 1). Our results also apply to generic recovery conditions, one of which is RIP. As an example, $\delta_{k} < 0.307$, $\delta_{2k} < 0.472$ are two of the many RIP-based conditions (see also, ) that are known to be sufficient for sparse vector recovery using $\ell_{1}$ minimization. A simple consequence of this paper is the following: The RIP conditions ${\delta_{k} < 0.307},{\delta_{2k} < 0.472}$ (and all other RIP conditions that are sufficient for sparse vector recovery) are *also* sufficient for robust recovery of matrices with rank at most $k$ improving the previous best condition of $\delta_{2k} < 0.307$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Improving the RIP conditions is a direct consequence of our observation but is not the focus of this paper, although such improvements have been of independent interest (e.g., ).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our results also apply to another recovery condition known as the Nullspace Spherical Section Property (SSP) and it easily follows from our main theorem that the spherical section constant $\Delta > {4k}$ is sufficient for the recovery of matrices up to rank $k$ as in the vector case. This approach not only simplifies the analysis, but also gives a better condition (as compared to $\Delta > {6k}$ in ). Our final contribution is to give nullspace based conditions for recovery of low-rank matrices using Schatten-$p$ quasi-norm minimization, which is analogous to $\ell_{p}$ minimization with $0 < p < 1$ for vectors. These nonconvex surrogate functions have motivated algorithms such as IRLS that are empirically observed to improve on the recovery performance of $\ell_{1}$ and nuclear norm minimization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Basic Definitions and Notation", "weight": 1.0} -->

Consider the problem of recovering the desired vector $\mathbf{x}_{0} \in {\mathbb{R}}^{n}$ with ${\|\mathbf{x}_{0}\|}_{1} = k$ from corrupted measurements $\mathbf{y} = {{A\mathbf{x}_{0}} + \mathbf{z}}$, with ${\|\mathbf{z}\|}_{2} \leq \epsilon$ where $\epsilon$ denotes the noise level, and $A \in {\mathbb{R}}^{m \times n}$ denotes the measurement matrix. Under certain conditions, $\mathbf{x}_{0}$ can be found under certain conditions by solving the following convex problem,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Basic Definitions and Notation", "weight": 1.0} -->

Similar to the vector case, we say that $X^{\ast}$ is *as good as* $X_{0}$ w.r.t $\mathbf{y}$ if ${\|{{\mathcal{A}{(X^{\ast})}} - \mathbf{y}}\|}_{2} \leq \epsilon$ and ${\| X^{\ast}\|}_{\star} \leq {\| X_{0}\|}_{\star}$. In particular the optimal solution to *problem* 4 is as good as $X_{0}$. We now give the definitions for certain recovery conditions on the measurement map, the Restricted Isometry Property and the Spherical Section Property.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Key Observations", "weight": 1.0} -->

Throughout this note, many of the proofs involving matrices apply the following useful Lemma which enables us to "vectorize" matrices when dealing with matrix norm inequalities.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Main Result", "weight": 1.0} -->

In this section, we state our main result which enables us to seamlessly translate results for vector recovery to matrix recovery. Our main theorem assumes that operator $\mathcal{A}$ satisfies an extension property, defined below.

<!-- chunk {"id": "body-0014", "role": "body", "section": "RIP implications for $k$-sparse recovery", "weight": 1.0} -->

Now, using Lemma 5 and Theorem 1, we have the following implications for matrix recovery.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Simplified Robustness Conditions", "weight": 1.0} -->

We show that various robustness conditions are equivalent to simple conditions on the measurement operator. The case of noiseless and perfectly sparse signals, is already given in Lemmas 3 and 4. Such simple conditions might be useful for analysis of nuclear norm minimization in later works. We state the conditions for matrices only; however, vector and matrix conditions will be identical (similar to Lemmas 3, 4) as one can expect from Theorem 1. The proofs follow from simple algebraic manipulations with the help of Lemma 1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Null space based recovery result for Schatten-$p$ quasi-norm minimization", "weight": 1.0} -->

In the previous sections, we stated the main theorem and considered its applications on RIP and SSP based conditions to show that results for recovery of sparse vectors can be analogously extended to recovery of low-rank matrices without making the recovery conditions stronger. In this section, we consider extending results from vectors to matrices using an algorithm different from $\ell_{1}$ minimization or nuclear norm minimization.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Null space based recovery result for Schatten-$p$ quasi-norm minimization", "weight": 1.0} -->

The $\ell_{p}$ quasi-norm (with $0 < p < 1$) is given by ${\| x\|}_{p}^{p} = {\sum_{i = 1}^{n}{|x|}_{i}^{p}}$. Note that for $p = 0$, this is nothing but the cardinality function. Thus it is natural to consider the minimization of the $\ell_{p}$ quasi-norm (as a surrogate for minimizing the cardinality function). Indeed, $\ell_{p}$ minimization has been a starting point for algorithms including Iterative Reweighted Least Squares and Iterative Reweighted $\ell_{1}$ minimization. Note that although $\ell_{1}$ minimization is convex, $\ell_{p}$ minimization with $0 < p < 1$ is *non-convex*.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Null space based recovery result for Schatten-$p$ quasi-norm minimization", "weight": 1.0} -->

However empirically, $\ell_{p}$ minimization based algorithms with $0 < p < 1$ have a better recovery performance as compared to $\ell_{1}$ minimization (see e.g.,). The recovery analysis of these algorithms has mostly been based on RIP. However Null space based recovery conditions analogous to those for $\ell_{1}$ minimization have been given for $\ell_{p}$ minimization (see e.g. ).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Null space based recovery result for Schatten-$p$ quasi-norm minimization", "weight": 1.0} -->

Let ${Tr}|A|^{p} = {Tr}{(A^{T}A)}^{\frac{p}{2}} = \sum_{i = 1}^{n}\sigma_{i}^{p}{(A)}$ denote the *Schatten-$p$ quasi norm* with $0 < p < 1$. Analogous to the vector case, one can consider the minimization of the Schatten-$p$ quasi-norm for the recovery of low-rank matrices,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Null space based recovery result for Schatten-$p$ quasi-norm minimization", "weight": 1.0} -->

where $y = {\mathcal{A}{(X_{0})}}$ with $X_{0}$ being the low-rank solution we wish to recover. IRLS-$p$ has been proposed as an algorithm to find a local minimum to. However no null-space based recovery condition has been given for the recovery analysis of Schatten-$p$ quasi norm minimization. We give such a condition below, after mentioning a few useful inequalities.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented a general result stating that the extension of any sufficient condition for the recovery of sparse vectors using $\ell_{1}$ minimization is also sufficient for the recovery of low-rank matrices using nuclear norm minimization. Consequently, we have that the best known RIP-based recovery conditions of $\delta_{k} < 0.307$ (and $\delta_{2k} < 0.472$) for sparse vector recovery are also sufficient for low-rank matrix recovery. Note that our result shows there is no "gap" between the recovery conditions for vectors and matrices, and we do not lose a factor of 2 in the rank of matrices that can be recovered, as might be suggested by existing analysis (e.g. ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We showed that a Null-space based sufficient condition (Spherical Section Property) given in easily extends to the matrix case, tightening the existing conditions for low-rank matrix recovery. Finally, we gave null-space based conditions for recovery using Schatten-$p$ quasi-norm minimization and showed that RIP based conditions for $\ell_{p}$ minimization extend to the matrix case. We note that all of these results rely on the ability to "vectorize" matrices through the use of key singular value inequalities including Lemma 1, 11. ‣ VI Null space based recovery result for Schatten-𝑝 quasi-norm minimization ‣ A Simplified Approach to Recovery Conditions for Low Rank Matrices").
