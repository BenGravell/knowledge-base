A Simplified Approach to Recovery Conditions for Low Rank Matrices

Topics include Low-rank recovery, Matrix recovery, Restricted isometry property, Nullspace conditions, Nuclear norm minimization, Compressed sensing, Singular values.

Provides a cleaner route from sparse-vector recovery theory to low-rank matrix recovery by using a key inequality on singular values. The payoff is simpler proofs and stronger RIP and nullspace recovery conditions for nuclear-norm and related low-rank reconstruction methods.

Recovering sparse vectors and low-rank matrices from noisy linear measurements has been the focus of much recent research. Various reconstruction algorithms have been studied, including l_1 and nuclear norm minimization as well as l_p minimization with p < 1. These algorithms are known to succeed if certain conditions on the measurement map are satisfied. Proofs of robust recovery for matrices have so far been much more involved than in the vector case. In this paper, we show how several robust classes of recovery conditions can be extended from vectors to matrices in a simple and transparent way, leading to the best known restricted isometry and nullspace conditions for matrix recovery. Our results rely on the ability to "vectorize" matrices through the use of a key singular value inequality.

## Introduction

Recovering sparse vectors and low-rank matrices from noisy linear measurements, with applications in compressed sensing and machine learning, has been the focus of much recent research. The Restricted Isometry Property (RIP) was introduced by Candès and Tao in and has played a major role in proving recoverability of sparse signals from compressed measurements. The first recovery algorithm that was analyzed using RIP was $\ell_{1}$ minimization . Since then, many algorithms including GraDes, Reweighed $\ell_{1}$, and CoSaMP have been analyzed using RIP.

In this paper, we show that if a set of conditions are sufficient for the robust recovery of sparse vectors with sparsity at most $k$, then the "extension" (defined later) of the same set of conditions are sufficient for the robust recovery of low rank matrices up to rank $k$.

While the recovery analysis in and (Theorem 2.4) is complicated and lengthy, our results (see "Main Theorem") are easily derived due to the use of a key singular value inequality (Lemma 1). Our results also apply to generic recovery conditions, one of which is RIP. As an example, $\delta_{k} < 0.307$, $\delta_{2k} < 0.472$ are two of the many RIP-based conditions (see also, ) that are known to be sufficient for sparse vector recovery using $\ell_{1}$ minimization.

Our results also apply to another recovery condition known as the Nullspace Spherical Section Property (SSP) and it easily follows from our main theorem that the spherical section constant $\Delta > {4k}$ is sufficient for the recovery of matrices up to rank $k$ as in the vector case. This approach not only simplifies the analysis , but also gives a better condition (as compared to $\Delta > {6k}$ in ). Our final contribution is to give nullspace based conditions for recovery of low-rank matrices using Schatten-$p$ quasi-norm minimization, which is analogous to $\ell_{p}$ minimization with $0 < p < 1$ for vectors.
