User-friendly Tail Bounds for Sums of Random Matrices

Topics include Matrix concentration, Random matrices, Tail bounds, Probability inequalities, Martingales, Spectral norm.

Presents accessible matrix concentration inequalities for sums of independent random self-adjoint matrices, including matrix analogues of classical scalar bounds. The paper became a standard reference because it packages powerful noncommutative tail tools in user-friendly forms.

This paper presents new probability inequalities for sums of independent, random, self-adjoint matrices. These results place simple and easily verifiable hypotheses on the summands, and they deliver strong conclusions about the large-deviation behavior of the maximum eigenvalue of the sum. Tail bounds for the norm of a sum of random rectangular matrices follow as an immediate corollary. The proof techniques also yield some information about matrix-valued martingales. In other words, this paper provides noncommutative generalizations of the classical bounds associated with the names Azuma, Bennett, Bernstein, Chernoff, Hoeffding, and McDiarmid. The matrix inequalities promise the same diversity of application, ease of use, and strength of conclusion that have made the scalar inequalities so valuable.

## Introduction

Random matrices have come to play a significant role in computational mathematics. This line of research has advanced by using established methods from random matrix theory, but it has also generated difficult questions that cannot be addressed without new tools. Let us summarize some of the challenges that arise in numerical applications.

Research has extended well beyond the classical ensembles (e.g., Wishart matrices and Wigner matrices) to encompass many other classes of random matrices. For instance, it is now common to study the properties of a sparse matrix sampled from a fixed matrix or a random submatrix drawn from a fixed matrix.

by definition of the bound ${\mathbf{A}}_{k}^{2}$. Finally, the semidefinite Jensen inequality (2.14) for the matrix square yields

To complete the proof, we apply (7.3) to the martingale $\{{\mathbf{Y}}_{k}\}$. ∎

It may not be immediately clear why abstract probability inequalities, such as Theorem 4.1. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices") and Corollary 4.2. ‣ 4.1. Main Results ‣ 4. Case Study: Matrix Gaussian Series ‣ User-Friendly Tail Bounds for Sums of Random Matrices"), deliver information about interesting random matrices that arise in practice. Let us describe a simple application that speaks to this concern.

### Proof

If $\{{\mathbf{X}}_{k}\}$ is a sequence of independent random matrices with the same distribution as $\mathbf{X}$, then

We also encounter highly structured matrices that involve a limited amount of randomness. One important example is the randomized DFT, which consists of a diagonal matrix of random signs multiplied by a discrete Fourier transform matrix.

Questions about the spectral properties of random matrices remain fundamental, but modern problems can also involve other considerations. For example, we might need to estimate the cut norm of a random adjacency matrix. Or we might want to study the action of a random operator on a class of vectors or matrices.

Most problems in numerical mathematics concern matrices of finite order. Asymptotic theory is less relevant in practice.

We often require explicit large-deviation theorems for statistics of random matrices so that we can study rates of convergence.
