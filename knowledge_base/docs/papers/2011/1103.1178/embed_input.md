A Simplified Approach to Recovery Conditions for Low Rank Matrices

Topics include Low-rank recovery, Matrix recovery, Restricted isometry property, Nullspace conditions, Nuclear norm minimization, Compressed sensing, Singular values.

Provides a cleaner route from sparse-vector recovery theory to low-rank matrix recovery by using a key inequality on singular values. The payoff is simpler proofs and stronger RIP and nullspace recovery conditions for nuclear-norm and related low-rank reconstruction methods.

Recovering sparse vectors and low-rank matrices from noisy linear measurements has been the focus of much recent research. Various reconstruction algorithms have been studied, including l_1 and nuclear norm minimization as well as l_p minimization with p < 1. These algorithms are known to succeed if certain conditions on the measurement map are satisfied. Proofs of robust recovery for matrices have so far been much more involved than in the vector case. In this paper, we show how several robust classes of recovery conditions can be extended from vectors to matrices in a simple and transparent way, leading to the best known restricted isometry and nullspace conditions for matrix recovery. Our results rely on the ability to "vectorize" matrices through the use of a key singular value inequality.

## Introduction

Recovering sparse vectors and low-rank matrices from noisy linear measurements, with applications in compressed sensing and machine learning, has been the focus of much recent research. The Restricted Isometry Property (RIP) was introduced by Candès and Tao in and has played a major role in proving recoverability of sparse signals from compressed measurements. The first recovery algorithm that was analyzed using RIP was $\ell_{1}$ minimization in. Since then, many algorithms including GraDes, Reweighed $\ell_{1}$, and CoSaMP have been analyzed using RIP....

In this paper, we show that if a set of conditions are sufficient for the robust recovery of sparse vectors with sparsity at most $k$, then the "extension" (defined later) of the same set of conditions are sufficient for the robust recovery of low rank matrices up to rank $k$.

We presented a general result stating that the extension of any sufficient condition for the recovery of sparse vectors using $\ell_{1}$ minimization is also sufficient for the recovery of low-rank matrices using nuclear norm minimization. Consequently, we have that the best known RIP-based recovery conditions of $\delta_{k} < 0.307$ (and $\delta_{2k} < 0.472$) for sparse vector recovery are also sufficient for low-rank matrix recovery....

We showed that a Null-space based sufficient condition (Spherical Section Property) given in easily extends to the matrix case, tightening the existing conditions for low-rank matrix recovery. Finally, we gave null-space based conditions for recovery using Schatten-$p$ quasi-norm minimization and showed that RIP based conditions for $\ell_{p}$ minimization extend to the matrix case. We note that all of these results rely on the ability to "vectorize" matrices through the use of key singular value inequalities including Lemma 1, 11....

### Lemma 5

The use of the above condition has a long history; it was stated in (see also ) for matrices made from concatenation of two bases, and studied in in a general setting.

We show that various robustness conditions are equivalent to simple conditions on the measurement operator. The case of noiseless and perfectly sparse signals, is already given in Lemmas 3 and 4. Such simple conditions might be useful for analysis of nuclear norm minimization in later works....
