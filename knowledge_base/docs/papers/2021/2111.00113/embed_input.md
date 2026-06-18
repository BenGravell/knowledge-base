<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper develops a new class of algorithms for general linear systems and eigenvalue problems. These algorithms apply fast randomized sketching to accelerate subspace projection methods, such as GMRES and Rayleigh-Ritz. This approach offers great flexibility in designing the basis for the approximation subspace, which can improve scalability in many computational environments. The resulting algorithms outperform the classic methods with minimal loss of accuracy. For model problems, numerical experiments show large advantages over MATLAB's optimized routines, including a 100 x speedup over gmres and a 10 x speedup over eigs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Arguably, the most exciting recent development in numerical linear algebra (NLA) is the advent of new randomized algorithms that are fast, scalable, robust, and reliable. For example, many practitioners have adopted the "randomized SVD" and its relatives to compute truncated singular value decompositions of large matrices. Randomized preconditioning allows us to solve highly overdetermined least-squares problems faster than any previous algorithm.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In spite of these successes, our community has made less progress on other core challenges from NLA, especially problems involving nonsymmetric square matrices. This paper exposes a new class of algorithms for solving general linear systems and eigenvalue problems. Our framework combines subspace projection methods, such as GMRES and the Rayleigh--Ritz process, with the modern technique of randomized sketching. This approach allows us to accelerate the existing methods by incorporating approximation subspaces that are easier to construct. The resulting algorithms are faster than their classic counterparts, without much loss of accuracy. In retrospect, the marriage of these ideas appears inevitable.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Sketching a least-squares problem", "weight": 1.0} -->

The sketch-and-solve paradigm is a basic tool for randomized matrix computations. The idea is to decrease the dimension of a large problem by projecting it onto a random subspace and to solve the smaller problem instead. The solution of this "sketched problem" sometimes serves in place of the solution to the original computational problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Sketching a least-squares problem", "weight": 1.0} -->

For a typical example, consider the $n \times d$ overdetermined least-squares problem

<!-- chunk {"id": "body-0007", "role": "body", "section": "Sketching a least-squares problem", "weight": 1.0} -->

where ${\mathbf{M}} \in {\mathbb{C}}^{n \times d}$ is a tall matrix with $n \gg d$. The right-hand side ${\mathbf{f}} \in {\mathbb{C}}^{n}$ and $\parallel \cdot \parallel_{2}$ denotes the $\ell_{2}$ norm. Draw a random sketching matrix ${\mathbf{S}} \in {\mathbb{C}}^{s \times n}$ with embedding dimension $s = {2d}$, say. Then solve the smaller $s \times d$ sketched problem

<!-- chunk {"id": "body-0008", "role": "body", "section": "Sketching a least-squares problem", "weight": 1.0} -->

For a carefully designed, "fast" sketching matrix $\mathbf{S}$, the whole sketch-and-solve process may be significantly faster than solving Eq. 1 directly. See Section 2 for details.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Sketching a least-squares problem", "weight": 1.0} -->

We can compare the residual norms of the solution $\hat{\mathbf{y}}$ to the sketched problem Eq. 2 and the solution ${\mathbf{y}}_{\star}$ to the original problem Eq. 1. The sketching method ensures that

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sketching a least-squares problem", "weight": 1.0} -->

Provided that the original problem has a tiny residual, the solution to the sketched problem also yields a tiny residual!

<!-- chunk {"id": "body-0011", "role": "body", "section": "Solving linear systems by sketched GMRES", "weight": 1.0} -->

Now, suppose that we wish to solve the (nonsymmetric, nonsingular) linear system

<!-- chunk {"id": "body-0012", "role": "body", "section": "Solving linear systems by sketched GMRES", "weight": 1.0} -->

All algorithms in this paper access the matrix via products: ${\mathbf{x}}\mapsto{{\mathbf{A}}{\mathbf{x}}}$. Our approach builds on a standard template, called a subspace projection method, which casts the linear system as a variational problem. We can treat this formulation by sketching. Let us summarize the ideas; a full exposition appears in Sections 3 and 4.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sketched GMRES", "weight": 1.0} -->

For the moment, suppose that we have acquired a tall matrix ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$, called a basis, with the property that ${range}{({\mathbf{B}})}$ contains a good approximate solution to the linear system Eq. 4. That is, ${{\mathbf{A}}{\mathbf{B}}{\mathbf{y}}} \approx {\mathbf{f}}$ for some ${\mathbf{y}} \in {\mathbb{C}}^{d}$. In addition, assume we have the reduced matrix ${{\mathbf{A}}{\mathbf{B}}} \in {\mathbb{C}}^{n \times d}$ at hand. In typical situations, the basis has very low dimension: $d \ll n$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sketched GMRES", "weight": 1.0} -->

At its heart, the GMRES algorithm is a subspace projection method that replaces the linear system Eq. 4 with the overdetermined least-squares problem

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sketched GMRES", "weight": 1.0} -->

The least-squares formulation Eq. 5 is a natural candidate for sketching.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sketched GMRES", "weight": 1.0} -->

The solution $\hat{\mathbf{y}}$ of the sketched problem Eq. 6 induces an approximate solution $\hat{\mathbf{x}} = {{\mathbf{B}}\hat{\mathbf{y}}}$ to the linear system Eq. 4. According to Eq. 3, the residual norm ${\|{{{\mathbf{A}}\hat{\mathbf{x}}} - {\mathbf{f}}}\|}_{2}$ is within a constant factor of the original residual norm ${\|{{{\mathbf{A}}{\mathbf{x}}_{\mathbf{B}}} - {\mathbf{f}}}\|}_{2}$. In summary, the sketched formulation Eq. 6 is effective if and only if the subspace ${range}{({\mathbf{B}})}$ contains an accurate approximate solution of the linear system.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sketched GMRES", "weight": 1.0} -->

We refer to Eq. 6 as the sketched GMRES problem (sGMRES). For an unstructured basis $\mathbf{B}$, the sGMRES approach is faster than solving the original least-squares problem Eq. 5, both in theory and in practice. With careful implementation, sGMRES is reliable and robust, even when the conditioning of the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ is poor. Indeed, it suffices that ${\kappa_{2}{({{\mathbf{A}}{\mathbf{B}}})}} \lesssim u^{- 1}$ where $u$ is the unit roundoff.^11^1In standard IEEE double-precision arithmetic, the unit roundoff $u \approx 10^{- 16}$. As a consequence, we have an enormous amount of flexibility in choosing the basis $\mathbf{B}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

To make sGMRES work well, we must construct a subspace that captures an approximate solution to the linear system Eq. 4. To that end, consider a Krylov subspace of the form

<!-- chunk {"id": "body-0019", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

The Krylov subspace often contains an excellent approximate solution to the linear system, even when the depth $p \ll n$. See \[41, Chaps. 6 and 7\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

For computations, we need an explicit basis $\mathbf{B}$ whose columns span the Krylov subspace. Although it is straightforward to form the monomial basis visible in Eq. 7, the condition number may grow exponentially, rendering the basis useless for numerical purposes. Instead, we will consider other procedures that quickly construct Krylov subspace bases with smaller condition number. Section 4 outlines several possible approaches.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

We have written ^∗^ for the (conjugate) transpose. Note that we obtain the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ as a by-product of this computation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

We have found that $k$-truncated Arnoldi is often effective, even with $k = 2$ or $k = 4$. Nevertheless, we are not aware of any fast, universal procedure for constructing a Krylov subspace basis with full numerical rank, short of strategies that perform costly full orthogonalization. This is a matter for further research.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

1:Matrix A ∈ ℂn × n, right-hand side f ∈ ℂn, initial guess x ∈ ℂn, basis dimension d, number k of vectors for truncated orthogonalization, stability tolerance tol = O (u−1).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

2:Approximate solution $\hat{\mathbf{x}} \in {\mathbb{C}}^{n}$ to linear system Eq. 4 and estimated residual norm r̂est 4: Draw subspace embedding S ∈ ℂs × n with s = 2 (d+1) ⊳ See Section 2.3 5: Form residual and sketch: r = f − A x and g = S r 6: Normalize basis vector b1 = r/∥r∥2 and apply matrix m1 = A b1 8: Truncated Arnoldi: wj = (I−bj − 1 bj − 1*−⋯−bj − k bj − k*) mj − 1 ⊳ b−i = 0 for i ≥ 0 9: Normalize basis vector bj = wj/∥wj∥2 and apply matrix mj = A bj 10: Sketch reduced matrix: C = S [m1,…,md] 12: if condition number κ2 (T) &gt; tol then warning… 13: Either whiten B ← B T−1 or form new residual and restart ⊳ See Section 5.3 14: Solve least-squares problem: $\hat{\mathbf{y}} =

<!-- chunk {"id": "body-0025", "role": "body", "section": "Krylov subspaces", "weight": 1.0} -->

{{\mathbf{T}}^{- 1}\left( {{\mathbf{U}}^{\ast}{\mathbf{g}}} \right)}$ ⊳ See Eq. 27 15: Residual estimate: r̂est = ∥(I−U U*) g∥2 ⊳ See Eq. 28 16: Construct solution: $\hat{\mathbf{x}} = {{\mathbf{x}} + {\left\lbrack {\mathbf{m}}_{1},\ldots,{\mathbf{m}}_{j} \right\rbrack\hat{\mathbf{y}}}}$ \ImplementationIn line 6, use double Gram–Schmidt for stability. In line 9, the QR factorization may require pivoting. In lines 11–12, apply T−1 via triangular substitution. Algorithm 1 sGMRES + k-truncated Arnoldi

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison with GMRES", "weight": 1.0} -->

The standard version of GMRES applies the expensive Arnoldi process (with full orthogonalization; see Section 4.2) to build an orthonormal basis for the Krylov subspace, and it exploits the structure of this basis to solve the least-squares problem Eq. 5 efficiently.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison with GMRES", "weight": 1.0} -->

In contrast, we propose to use a quick-and-dirty construction, such as the $k$-truncated Arnoldi process, to obtain a basis for the Krylov subspace. Then we solve the sGMRES least-squares problem Eq. 6 to produce an approximate solution of the linear system.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparison with GMRES", "weight": 1.0} -->

This expression assumes that sGMRES uses $k$-truncated Arnoldi for $k$ constant, as well as a fast sketching matrix (Section 2.3). See Algorithm 1 for pseudocode.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Comparison with GMRES", "weight": 1.0} -->

As evidence for the benefits of using sGMRES, Figure 1 depicts an over 100$\times$ speedup for a sparse nonsymmetric linear system with dimension $n = {921,632}$. In this case, sGMRES with $4$-truncated Arnoldi attains the same accuracy as GMRES with full orthogonalization. sGMRES is comparable in speed to restarted GMRES with restarting frequency $10$, whose convergence is significantly impaired. Section 8 provides more details on the experimental setup, as well as further illustrations. For example, when applied to a sparse positive-definite linear system, sGMRES can produce $\ell_{2}$ residual norms about $5 \times$ smaller than the conjugate gradient (CG) method after the same running time. Thus, it can be argued that sGMRES combines the speed of CG with the generality and robustness of GMRES.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Solving eigenvalue problems by sketched Rayleigh--Ritz", "weight": 1.0} -->

Similar ideas apply to spectral computations. We pose the nonsymmetric eigenvalue problem

<!-- chunk {"id": "body-0031", "role": "body", "section": "Solving eigenvalue problems by sketched Rayleigh--Ritz", "weight": 1.0} -->

As before, we access the matrix via products: ${\mathbf{x}}\mapsto{{\mathbf{A}}{\mathbf{x}}}$. Typically, we seek a family of eigenvectors associated with a particular class of eigenvalues (e.g., largest real part, closest to zero). Let us outline a sketched subspace projection method for the eigenvalue problem. Full details appear in Sections 6 and 7.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

As in Section 1.2.1, suppose that we have procured a basis ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$ and the reduced matrix ${{\mathbf{A}}{\mathbf{B}}} \in {\mathbb{C}}^{n \times d}$. The range of the basis should contain approximate eigenpairs $({\mathbf{x}},\lambda)$ for which ${{\mathbf{A}}{\mathbf{x}}} \approx {\lambda{\mathbf{x}}}$. In this setting, the most commonly employed strategy is the Rayleigh--Ritz (RR) method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

We begin with the classic variational formulation \[37, Thm. 11.4.2\]

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

Evidently, the least-squares problem Eq. 10 is ripe for sketching.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

For each solution $(\hat{\mathbf{y}},\hat{\theta})$, we obtain an approximate eigenpair $({{\mathbf{B}}\hat{\mathbf{y}}},\hat{\theta})$ of the original matrix $\mathbf{A}$. We will show---both theoretically and empirically---that the computed eigenpairs of Eq. 12 are competitive with the eigenpairs obtained from RR.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

We refer to Eq. 11 as the sketched Rayleigh--Ritz (sRR) formulation. Although it demands a careful implementation, sRR is faster than the original least-squares method Eq. 10 for an unstructured basis $\mathbf{B}$. Moreover, sRR is robust, even when the basis $\mathbf{B}$ has poor conditioning. Indeed, it suffices that ${\kappa_{2}{({\mathbf{B}})}} \lesssim u^{- 1}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

1:Matrix A ∈ ℂn × n, initial vector b ∈ ℂn, basis dimension d, number k of vector for partial orthogonalization, stability tolerance tol = O (u−1), convergence tolerance τ. 2:Approximate eigenpairs (xi,λi) such that A xi ≈ λi xi and estimated residual norms r̂est, i.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

4: Draw subspace embedding S ∈ ℂs × n with s = 4 d ⊳ See Section 2.3 5: Starting vector: w1 = randn (n,1) 6: Normalize basis vector b1 = w1/∥w1∥2 and apply matrix m1 = A b1 8: Truncated Arnoldi: wj = (I−bj − 1 bj − 1*−⋯−bj − k bj − k*) mj − 1 ⊳ b−i = 0 for i ≥ 0 9: Normalize bj = wj/∥wj∥2 and apply matrix mj = A bj 10: Sketch basis C = S [b1,…,bdmax] and reduced matrix D = S [m1,…,mdmax] 12: if κ2 (T) &gt; tol then warning: 13: Either whiten B ← B T−1 or stabilize and solve Eq. 46 ⊳ See Section 6.5 14: Solve eigenvalue problem: T−1 U* D yi = λi yi for i = 1, …, d ⊳ See Eq. 45 15: Form residual estimates ∥D yi−λi C yi∥2/∥C yi∥2 ⊳ See Eq. 43, Section 6.4 16: Identify

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sketched Rayleigh--Ritz", "weight": 1.0} -->

set ℐ of indices i where residual is at most τ 17: Compute xi = B yi and normalize xi:= xi/∥xi∥2 for i ∈ ℐ, and output (xi,λi) \ImplementationIn line 6, use double Gram–Schmidt for stability. In line 9, the QR factorization may require pivoting. In lines 11–12, apply T−1 via triangular substitution. Algorithm 2 sRR + k-truncated Arnoldi

<!-- chunk {"id": "body-0040", "role": "body", "section": "Comparison with Arnoldi + Rayleigh--Ritz", "weight": 1.0} -->

As before, we can deploy the Krylov subspace Eq. 7 for eigenvalue computations. In this case, we typically use a random starting vector ${\mathbf{ω}} \in {\mathbb{C}}^{n}$ to generate the subspace $\mathsf{K}_{p}{({\mathbf{A}};{\mathbf{ω}})}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison with Arnoldi + Rayleigh--Ritz", "weight": 1.0} -->

To solve a large nonsymmetric eigenvalue problem, one standard algorithm \[42, Sec. 6.2\] applies the Arnoldi process (with full orthogonalization; see Section 4.2) to form an orthonormal basis for the Krylov subspace, and it uses the structure of the basis to solve the RR eigenvalue problem efficiently.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison with Arnoldi + Rayleigh--Ritz", "weight": 1.0} -->

Instead, we propose to combine a fast construction of a Krylov subspace basis, such as $k$-truncated Arnoldi Eq. 8, with the sRR eigenvalue problem Eq. 12.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison with Arnoldi + Rayleigh--Ritz", "weight": 1.0} -->

This expression includes basis generation via $k$-truncated Arnoldi for $k$ constant, and sRR uses a fast sketching matrix (Section 2.3). See Algorithm 2 for pseudocode.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison with Arnoldi + Rayleigh--Ritz", "weight": 1.0} -->

As evidence, Figure 2 highlights an eigenvalue problem arising in numerical optimization for which sRR runs over 10$\times$ faster than the MATLAB eigs command. Even so, both methods compute the desired eigenpair to the same accuracy. Section 8 describes the experimental setup and provides further illustrations. For example, when applied to a sparse symmetric eigenvalue problem, sRR can outperform standard implementations of the Lanczos method in both speed and reliability.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

For eigenvalue problems, there is also a compelling opportunity to explore alternative subspace constructions. For example, consider the block Krylov subspace

<!-- chunk {"id": "body-0046", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

We commonly generate the Krylov subspace from a random matrix $\mathbf{\Omega}$. The standard prescription recommends a small block size $b$ and a large depth $p$, but recent research \[30, Sec. 11\] has shown the value of a large block size $b$ and a small depth $p$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

We must take care in constructing the block Krylov subspace. Truncated Arnoldi is only competitive when the block size $b$ is a small constant.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

We obtain the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ as a by-product. In practice, the Chebyshev polynomials must be shifted and scaled to adapt to the spectrum of $\mathbf{A}$. See Section 7 for details and alternative methods for fast basis construction.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our idea to combine subspace projection methods with sketching offers compelling advantages over the classic algorithms, especially in modern computing environments. Nevertheless, it must be acknowledged that this approach suffers from some of the same weaknesses as GMRES and RR. For example, when the basis $\mathbf{B}$ is a Krylov subspace, these methods are limited by the approximation power of Krylov subspaces. Furthermore, we are not aware of a universal method for quickly computing a full-rank basis for the Krylov subspace, short of expensive strategies based on full orthogonalization. Both of these points merit further attention.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

With hindsight, our framework appears as an obvious application of the sketch-and-solve paradigm for overdetermined least-squares problems. A critical reader may even wonder whether this idea is actually novel. Let us respond to this concern.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

We believe that we are the first authors to identify the natural connection between sketching and subspace projection methods for linear algebra problems. Indeed, we are not aware of any prior work where authors sketch the minimum-residual formulations Eqs. 6 and 11 of general linear systems and eigenvalue problems.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

Second, to obtain algorithms that are asymptotically faster than classic methods, we must also employ efficient constructions of Krylov subspace bases. In the past, researchers have regarded these techniques as a way to postpone expensive orthogonalization steps in parallel computing environments. In contrast, sketching sometimes allows us to eliminate the orthogonalization steps. Thus, we can finally take full advantage of the potential of fast computational bases.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

In particular, there is a remarkable opportunity to design a new class of preconditioners for iterative solution of large-scale linear algebra problems. Indeed, since our approach allows for more flexible bases and mitigates orthogonalization costs, we can still derive benefits from a mediocre preconditioner that only reduces the iteration complexity to 100s or 1000s of iterations. We are excited about this prospect.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Roadmap", "weight": 1.0} -->

In Section 2, we give a rigorous treatment of sketching for least-squares problems. Sections 3, 4, and 5 develop and analyze the sGMRES method and associated basis constructions. Sections 6 and 7 contain the analogous developments for sRR. Computational experiments in Section 8 confirm that these algorithms are fast, robust, and reliable. Sections 9 and 10 describe extensions and prospects.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Sketching for least-squares problems", "weight": 1.0} -->

As discussed in Section 1.1, we can use a subspace embedding to reduce the dimension of an overdetermined least-squares problem. This idea is also due to Sarlós; it serves as the foundation for a collection of methods called the sketch-and-solve paradigm.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Fact 1 (Sketching for least-squares)", "weight": 1.0} -->

In particular, the solution $\mathbf{y}_{\star}$ to the least-squares problem Eq. 1 and the solution $\hat{\mathbf{y}}$ to the sketched least-squares problem Eq. 2 satisfy residual norm bounds

<!-- chunk {"id": "body-0057", "role": "body", "section": "Fact 1 (Sketching for least-squares)", "weight": 1.0} -->

Equation Eq. 16. ‣ 2.1 Sketching for least-squares problems ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777.") justifies the claim Eq. 3 with $\varepsilon = {1/\sqrt{2}}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Whitening the basis", "weight": 1.0} -->

Rokhlin & Tygert observed that a subspace embedding yields an inexpensive way to precondition an iterative algorithm for the overdetermined least-squares problem. We can invoke the same idea to approximately orthogonalize, or whiten, a given basis.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Fact 2 (Whitening)", "weight": 1.0} -->

Furthermore, we have the condition number diagnostic

<!-- chunk {"id": "body-0060", "role": "body", "section": "Constructing a subspace embedding", "weight": 1.0} -->

There are many performant constructions of fast randomized subspace embeddings that work for an unknown subspace of bounded dimension \[30, Sec. 9\]. Let us summarize two that are most relevant for our purposes. In each case, for a subspace with dimension $d$, to obtain empirical distortion $\varepsilon \in {}$, we set the embedding dimension $s = {d/\varepsilon^{2}}$. We focus on the complex field; modifications for the real field are straightforward.

<!-- chunk {"id": "body-0061", "role": "body", "section": "SRFTs", "weight": 1.0} -->

First, we introduce the subsampled random Fourier transform (SRFT). This subspace embedding^22^2For worst-case problems, a more elaborate SRFT construction may be needed \[30, Sec. 9\]. takes the form

<!-- chunk {"id": "body-0062", "role": "body", "section": "SRFTs", "weight": 1.0} -->

In this expression, ${\mathbf{D}} \in {\mathbb{C}}^{s \times n}$ is a diagonal projector onto $s$ coordinates, chosen independently at random, ${\mathbf{F}} \in {\mathbb{C}}^{n \times n}$ is the unitary discrete Fourier transform (DFT), and ${\mathbf{E}} \in {\mathbb{C}}^{n \times n}$ is a diagonal matrix whose entries are independent Steinhaus^33^3A Steinhaus random variable is uniform on the complex unit circle $\{{z \in {\mathbb{C}}}:{{|z|} = 1}\}$. random variables. The cost of applying the matrix $\mathbf{S}$ to an $n \times d$ matrix is $O{({nd{\log d}})}$ operations using the subsampled FFT algorithm.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sparse maps", "weight": 1.0} -->

Next, we describe the sparse dimension reduction map, which is useful for sparse data and may require less data movement. It takes the form

<!-- chunk {"id": "body-0064", "role": "body", "section": "Sparse maps", "weight": 1.0} -->

The columns of $\mathbf{S}$ are statistically independent. Each column ${\mathbf{s}}_{i}$ has exactly $\zeta$ nonzero entries, drawn from the Steinhaus distribution, placed in uniformly random coordinates. For reliability, we choose the sparsity level $\zeta = {\lceil{2{\log{({1 + d})}}}\rceil}$. We can apply $\mathbf{S}$ to a matrix $\mathbf{M}$ with $O{({{\zeta \cdot \text{nnz}}{({\mathbf{M}})}})}$ operations, but it may require a sparse arithmetic library to achieve the best performance.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Solving linear systems with sGMRES", "weight": 1.0} -->

This section elaborates on the sGMRES method outlined in Section 1.2. Section 4 discusses methods for constructing the basis required by sGMRES. Section 5 combines these ideas to obtain complete sGMRES algorithms.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Derivation of GMRES", "weight": 1.0} -->

With some imprecision, we refer to Eq. 22 as the GMRES problem. By calculus, the least-squares problem Eq.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Derivation of GMRES", "weight": 1.0} -->

The formulation Eq. 23 is also called a Petrov--Galerkin method \[41, Chap. 5\] with approximation space ${\mathbf{x}}_{0} + {{range}{({\mathbf{B}})}}$ and orthogonality space ${range}{({{\mathbf{A}}{\mathbf{B}}})}$. The GMRES algorithm is a particular instance where $\mathbf{B}$ is an orthonormal basis for a Krylov subspace generated by ${\mathbf{r}}_{0}$. GMRES forms the basis $\mathbf{B}$ via the Arnoldi process (Section 4.2), which involves $d$ matvecs with $\mathbf{A}$ plus $O{({nd^{2}})}$ arithmetic. This reduces Eq. 22 to a structured least-squares problem that can be solved in $O{(d^{2})}$ operations.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Derivation and analysis of sGMRES", "weight": 1.0} -->

To develop the sGMRES method, we just sketch the GMRES problem Eq. 22. Construct a subspace embedding ${\mathbf{S}} \in {\mathbb{C}}^{s \times n}$ for ${range}{({\lbrack{{\mathbf{A}}{\mathbf{B}}},{\mathbf{r}}_{0}\rbrack})}$ with distortion $\varepsilon \in {}$. The sketched GMRES problem is

<!-- chunk {"id": "body-0069", "role": "body", "section": "Derivation and analysis of sGMRES", "weight": 1.0} -->

We have an a priori comparison of the GMRES Eq. 22 and sGMRES Eq. 24 residual norms because of the relation Eq. 16. ‣ 2.1 Sketching for least-squares problems ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777."):

<!-- chunk {"id": "body-0070", "role": "body", "section": "Derivation and analysis of sGMRES", "weight": 1.0} -->

Thus, sGMRES produces approximate solutions to Eq. 21 with small $\ell_{2}$ residuals precisely when GMRES does.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Derivation and analysis of sGMRES", "weight": 1.0} -->

The last display is a consequence of Eq. 15. ‣ 2.1 Sketching for least-squares problems ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777.").

<!-- chunk {"id": "body-0072", "role": "body", "section": "Derivation and analysis of sGMRES", "weight": 1.0} -->

For both GMRES Eq. 22 and sGMRES Eq. 24, the fundamental challenge is to produce a basis $\mathbf{B}$ that captures an approximate solution to the linear system Eq. 21. We return to this matter in Section 4.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Implementation", "weight": 1.0} -->

Let us outline a numerically robust implementation of sGMRES and describe some of the issues that arise.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Implementation", "weight": 1.0} -->

The algorithm operates with either an SRFT Eq. 19 or a sparse embedding Eq. 20, depending on which is more appropriate to the computational environment. We recommend the embedding dimension $s = {2{({d + 1})}}$, which typically yields distortion $\varepsilon = {1/\sqrt{2}}$. In view of Eq. 25, the sGMRES residual norm is less than $6 \times$ the GMRES residual norm, although the discrepancy is often smaller in practice.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Implementation", "weight": 1.0} -->

Of course, we apply the inverse by triangular substitution. The sketched residual norm Eq. 26 admits the simple expression

<!-- chunk {"id": "body-0076", "role": "body", "section": "Implementation", "weight": 1.0} -->

In summary, given the basis $\mathbf{B}$, the cost of forming and solving the sGMRES problem Eq. 24 is $O{({d^{3} + {nd{\log d}}})}$ arithmetic. In contrast, for an unstructured basis, the cost of solving the GMRES problem Eq. 22 is $O{({nd^{2}})}$ arithmetic. Section 5 provides an accounting of the costs of forming the basis and solving the least-squares problem.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Stability", "weight": 1.0} -->

The classical stability result \[24, Thm. 20.3\] shows that standard numerical methods for the least-squares problem Eq. 24 produce a solution with essentially optimal residual as long as ${\kappa_{2}{({{\mathbf{S}}{\mathbf{A}}{\mathbf{B}}})}} \lesssim u^{- 1}$. According to Eq. 18. ‣ 2.2 Whitening the basis ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777."), this condition is equivalent to ${\kappa_{2}{({{\mathbf{A}}{\mathbf{B}}})}} \lesssim u^{- 1}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Stability", "weight": 1.0} -->

Our computational work (Section 8) confirms that sGMRES is reliable unless the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ is very badly conditioned. In our experience, it suffices that ${\kappa_{2}{({{\mathbf{A}}{\mathbf{B}}})}} \leq 10^{14}$ in double-precision arithmetic. Therefore, we have wide latitude to design bases that we can construct quickly; see Section 4. We will provide evidence that sGMRES with a fast basis construction is more efficient than GMRES with a structured basis.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Restarting", "weight": 1.0} -->

Standard implementations of GMRES periodically restart \[41, Sec. 6.5.5\]. That is, they use a basis $\mathbf{B}$ to compute an approximate solution ${\mathbf{x}}_{\mathbf{B}}$ to the linear system Eq. 21 with the residual vector ${\mathbf{r}}_{\mathbf{B}} = {{\mathbf{r}}_{0} - {{\mathbf{A}}{\mathbf{x}}_{\mathbf{B}}}}$. If the residual norm ${\|{\mathbf{r}}_{\mathbf{B}}\|}_{2}$ exceeds an error tolerance, the residual vector ${\mathbf{r}}_{\mathbf{B}}$ is used to generate a new basis, which is fed back to GMRES to construct another approximate solution. This process is repeated until a solution of desired quality is obtained.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Restarting", "weight": 1.0} -->

Restarting has a number of benefits for the process of basis construction. It allows us to work with bases that have fewer columns, which limits the cost of storing the basis. For orthogonal basis constructions, restarting reduces the cost of orthogonalization. For non-orthogonal basis constructions, the restarting process helps control the conditioning of the basis. On the other hand, restarted GMRES may not converge if the bases are not rich enough (see Fig. 1), and we pay for the convergence delay with every restart. As we will discuss in Section 5, sGMRES can help us manage all of these issues.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

For difficult linear systems, we may need a preconditioner ${\mathbf{P}} \in {\mathbb{C}}^{n \times n}$ to solve it successfully with either GMRES or sGMRES. The preconditioned system has the form

<!-- chunk {"id": "body-0082", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

A good preconditioner has two features \[41, Chaps. 9 and 10\]. First, the matrix ${\mathbf{P}}^{- 1}{\mathbf{A}}$ has a more "favorable" structure than $\mathbf{A}$. Second, we can solve ${{\mathbf{P}}{\mathbf{z}}} = {\mathbf{g}}$ efficiently. (Let us emphasize that we only interact with ${\mathbf{P}}^{- 1}$ by solving linear systems!) Although preconditioning is critical in practice, it is heavily problem dependent, so we will not delve into examples.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Preconditioning", "weight": 1.0} -->

We may derive sGMRES for the preconditioned system Eq. 29, following the same pattern as before. Note that we employ the preconditioned matrix ${\mathbf{P}}^{- 1}{\mathbf{A}}$ when we construct the basis $\mathbf{B}$ and the reduced matrix ${\mathbf{P}}^{- 1}{({{\mathbf{A}}{\mathbf{B}}})}$. The details are routine. We believe that sGMRES opens up new opportunities for designing preconditioners because it is faster and more flexible than GMRES.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Constructing a basis for sGMRES", "weight": 1.0} -->

As we have seen, the success of both GMRES Eq. 22 and sGMRES Eq. 24 hinges on the approximation power of the basis. Krylov subspaces are, perhaps, the most natural way to capture solutions to a linear system when we access the matrix via products \[41, Chaps. 6 and 7\]. In this section, we describe a number of ways to compute non-orthogonal bases for Krylov subspaces. Although these strategies are decades old, they warrant a fresh look because sGMRES has a fundamentally different computational profile from GMRES.

<!-- chunk {"id": "body-0085", "role": "body", "section": "The single-vector Krylov subspace", "weight": 1.0} -->

Many iterative methods for solving the linear system Eq. 21 implicitly search for solutions in the Krylov subspace

<!-- chunk {"id": "body-0086", "role": "body", "section": "The single-vector Krylov subspace", "weight": 1.0} -->

A basis ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$ for the Krylov subspace $\mathsf{K}_{p}{({\mathbf{A}};{\mathbf{r}})}$ comprises a system of vectors that spans the subspace. We can write

<!-- chunk {"id": "body-0087", "role": "body", "section": "The single-vector Krylov subspace", "weight": 1.0} -->

The filter polynomials $({\varphi_{j}:{j = {1,\ldots,d}}})$ have degree at most $p - 1$, and they are usually linearly independent (so $d = p$). In most cases, the polynomials are also graded $({{\deg{(\varphi_{j})}} = {j - 1}})$, and they are constructed sequentially by a recurrence. This process delivers the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ without any extra work.

<!-- chunk {"id": "body-0088", "role": "body", "section": "The single-vector Krylov subspace", "weight": 1.0} -->

We will consider other constructions of Krylov subspace bases that are more suitable in practice. Our aim is to control the resources used to obtain the basis, including arithmetic, (working) storage, communication, synchronization, etc. We can advance these goals by relaxing the requirement that the basis be well-conditioned.

<!-- chunk {"id": "body-0089", "role": "body", "section": "The single-vector Krylov subspace", "weight": 1.0} -->

For theoretical analysis of the approximation power of Krylov subspaces in the context of linear system solvers, see \[41, Sec. 6.11\].

<!-- chunk {"id": "body-0090", "role": "body", "section": "The Arnoldi process", "weight": 1.0} -->

As a consequence, we can solve the least-squares problem Eq. 22 with ${\mathbf{B}} = {\mathbf{Q}}_{p}$ in $O{(p^{2})}$ time and produce the approximate solution ${\mathbf{x}}_{\mathbf{B}}$ in $O{({np})}$ operations. This is roughly how the standard implementation of the GMRES algorithm operates.

<!-- chunk {"id": "body-0091", "role": "body", "section": "The Arnoldi process", "weight": 1.0} -->

The orthogonalization steps in the Arnoldi process are expensive. For $p$ iterations, they expend $O{({np^{2}})}$ arithmetic, and they may also involve burdensome inner-products, communication, and synchronization. Robust implementations usually incorporate modified or double Gram--Schmidt or else use Householder reflectors.

<!-- chunk {"id": "body-0092", "role": "body", "section": "The Arnoldi process", "weight": 1.0} -->

The literature contains many strategies for controlling the orthogonalization costs in the Arnoldi process \[41, Chap. 6\]. sGMRES motivates us to reevaluate techniques for building a nonorthogonal basis. For example, we can use $k$-truncated Arnoldi, as in Eq. 8, which reduces the cost of basis generation to $O{({nk^{2}})}$. Provided the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ is reasonably conditioned, we can still obtain accurate solutions to the linear system via sGMRES Eq. 24.

<!-- chunk {"id": "body-0093", "role": "body", "section": "The Arnoldi process", "weight": 1.0} -->

Relatedly, Balabanov & Grigori have proposed to use a low-dimensional sketch of the basis vectors to implement an approximate orthogonalization strategy. Their approach has the same asymptotic cost as full orthogonalization, but similar ideas might be invoked to accelerate partial or selective orthogonalization.

<!-- chunk {"id": "body-0094", "role": "body", "section": "The Lanczos recurrence", "weight": 1.0} -->

For this subsection, assume $\mathbf{A}$ is Hermitian. In this case, the Arnoldi process simplifies to a three-term recurrence \[41, Sec. 6.6\]:

<!-- chunk {"id": "body-0095", "role": "body", "section": "The Lanczos recurrence", "weight": 1.0} -->

This allows us to solve the least-squares problem Eq. 22 with ${\mathbf{B}} = {\mathbf{Q}}_{p}$ in $O{(p)}$ time, and we construct the approximate solution ${\mathbf{x}}_{\mathbf{B}}$ with $O{({np})}$ arithmetic. This is roughly how the MINRES algorithm operates.

<!-- chunk {"id": "body-0096", "role": "body", "section": "The Lanczos recurrence", "weight": 1.0} -->

For $p$ iterations, the Lanczos recurrence costs just $O{({np})}$ operations, but it has complicated behavior in finite-precision arithmetic. This issue is not devastating when Lanczos is used to solve linear systems \[28, Chap. 5\], but it can present a more serious challenge when solving eigenvalue problems \[37, Chap. 13\].

<!-- chunk {"id": "body-0097", "role": "body", "section": "The Lanczos recurrence", "weight": 1.0} -->

Although it is very efficient to solve the least-squares problem Eq. 22 by passing to the tridiagonal matrix ${\mathbf{J}}_{p}$, it is more reliable to sketch ${\mathbf{S}}{({{\mathbf{A}}{\mathbf{Q}}_{p}})}$ and to solve the sketched problem Eq. 24 instead. The approach based on sketching is competitive with MINRES when $p \ll n$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "The Lanczos recurrence", "weight": 1.0} -->

The literature describes many approaches for maintaining the orthogonality of the Lanczos basis, such as selective orthogonalization \[37, Chap. 13\]. When using the basis for sGMRES, we might simply omit the extra orthogonalization steps. Alternatively, we may adopt the approximate orthogonalization strategies sketched in Section 4.2.

<!-- chunk {"id": "body-0099", "role": "body", "section": "The Chebyshev recurrence", "weight": 1.0} -->

In some settings, we may wish to avoid the orthogonalization steps entirely because they involve operations on high-dimensional basis vectors. We can achieve this goal by using other polynomial recurrences to construct a Krylov subspace basis. This idea is attributed to Joubert & Carey.

<!-- chunk {"id": "body-0100", "role": "body", "section": "The Chebyshev recurrence", "weight": 1.0} -->

In practice, we also rescale each basis vector ${\mathbf{b}}_{j}$ to have unit $\ell_{2}$ norm after it has played its role in the recurrence. The key theoretical fact is that the Chebyshev basis tends to have a condition number that grows polynomially in $p$, rather than exponentially. This claim depends on assumptions that the eigenvalues of the matrix are equidistributed over an ellipse.

<!-- chunk {"id": "body-0101", "role": "body", "section": "The Chebyshev recurrence", "weight": 1.0} -->

To implement this procedure, we may first apply a few iterations of the Arnoldi method (Section 6.2) to estimate the spectrum of $\mathbf{A}$. More generally, we find a (transformed) ellipse that contains the spectrum. Then we adapt the Chebyshev polynomials to this ellipse. The overall cost of constructing a Chebyshev basis for $\mathsf{K}_{p}{({\mathbf{A}};{\mathbf{r}})}$ is $O{({np})}$, and it involves no orthogonalization whatsoever.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Newton polynomials", "weight": 1.0} -->

The Newton polynomials provide another standard construction of a nonorthogonal basis for the Krylov subspace. Suppose that ${\theta_{1},\ldots,\theta_{p}} \in {\mathbb{C}}$ are complex-valued shift parameters. Then we can build a basis ${\mathbf{B}} \in {\mathbb{C}}^{n \times p}$ for $\mathsf{K}_{p}{(\mathsf{A};{\mathbf{r}})}$ via the recurrence

<!-- chunk {"id": "body-0103", "role": "body", "section": "Newton polynomials", "weight": 1.0} -->

The shifts $\theta_{i}$ are often chosen to be estimated eigenvalues of $\mathbf{A}$, obtained from an invocation of the Arnoldi method (Section 6.2). The overall computational profile of constructing the Newton basis is similar to constructing a Chebyshev basis.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Local orthogonalization", "weight": 1.0} -->

We can improve the conditioning of a computed basis ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$ by local orthogonalization. Indeed, it is generally helpful to orthogonalize subcollections of basis vectors, even if it proves too expensive to orthogonalize all of the basis vectors. In particular, scaling each column to have unit $\ell_{2}$ norm is always appropriate. See for an analysis.

<!-- chunk {"id": "body-0105", "role": "body", "section": "sGMRES algorithms", "weight": 1.0} -->

This section presents complete algorithms for solving the linear system Eq. 21 via sGMRES, including options for adaptive basis generation.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Basic implementation", "weight": 1.0} -->

Algorithm 1 contains pseudocode for a basic implementation of sGMRES using the $k$-truncated Arnoldi basis Eq. 8. We recommend this version of the algorithm when the user lacks information about the spectrum of $\mathbf{A}$. Given bounds on the spectrum, one may replace the truncated Arnoldi basis with a Chebyshev basis (Section 4.4). Table 1 summarizes the arithmetic costs.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Iterative sGMRES", "weight": 1.0} -->

As noted, most methods for producing the Krylov subspace basis are recursive. They generate the columns of $\mathbf{B}$ and the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ in sequence. This observation suggests an iterative implementation of sGMRES. We sketch the columns of the reduced matrix as they arrive, incrementally solving the sGMRES problem Eq. 24 at each step.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Iterative sGMRES", "weight": 1.0} -->

Let $d_{\max}$ be a user-specified parameter that bounds the maximum depth allowed for the Krylov subspace. Draw and fix a randomized subspace embedding ${\mathbf{S}} \in {\mathbb{C}}^{s \times n}$ with embedding dimension $s = {2{({d_{\max} + 1})}}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Iterative sGMRES", "weight": 1.0} -->

Repeat this process until the estimated residual norm ${\hat{r}}_{{est},j}$ is sufficiently small or we breach the threshold $d_{\max}$ for the size of the Krylov space. After $d$ iterations, the arithmetic costs of Eqs. 32 and 33 match the non-sequential implementation (Section 3.3) with a basis of size $d$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Adaptive restarting", "weight": 1.0} -->

There is a further opportunity to design an adaptive strategy for restarting. According to Eq. 18. ‣ 2.2 Whitening the basis ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777."), the condition number $\kappa_{2}{({\mathbf{T}}_{j})}$ is comparable with $\kappa_{2}{({{\mathbf{A}}{\mathbf{B}}_{j}})}$. When first ${\kappa_{2}{({\mathbf{T}}_{j})}} > \text{tol}$, we recognize that it is time to restart.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Adaptive restarting", "weight": 1.0} -->

We generate the new Krylov subspace using the previous residual ${\hat{\mathbf{r}}}_{j - 1} = {{\mathbf{r}}_{0} - {{\mathbf{A}}{\mathbf{B}}_{j - 1}{\hat{\mathbf{y}}}_{j - 1}}}$. Alternatively, instead of restarting, we could approximately orthogonalize $\mathbf{B}$ by replacing it with ${\mathbf{B}}{\mathbf{T}}^{- 1}$, whose condition number is constant, and continue generating basis vectors.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Storage-efficient versions", "weight": 1.0} -->

In situations where storage is at a premium, we can even avoid storing the reduced matrix ${\mathbf{A}}{\mathbf{B}}_{j}$ by sketching its columns sequentially and discarding them immediately after sketching. Once the estimated residual norm ${\hat{r}}_{{est},j}$ is sufficiently small, we can construct the approximate solution

<!-- chunk {"id": "body-0113", "role": "body", "section": "Storage-efficient versions", "weight": 1.0} -->

by iteratively regenerating the columns of the reduced matrix ${\mathbf{A}}{\mathbf{B}}_{j}$ and linearly combining them on the fly. For some basis constructions (e.g., truncated Arnoldi or Chebyshev), we only need to maintain a few columns of $\mathbf{B}$ and the $j$ columns of ${\mathbf{S}}{({{\mathbf{A}}{\mathbf{B}}_{j}})}$. This modification doubles the arithmetic cost associated with basis generation (matvecs plus orthogonalization). A similar technique was used.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Obtaining a solution with full accuracy", "weight": 1.0} -->

While the constant-factor loss Eq. 25 in sGMRES is unlikely to be an issue, we can obtain a solution with the same quality as GMRES by using $\mathbf{T}$ as a preconditioner to solve Eq. 22 via an iterative method as. This method still requires ${\kappa_{2}{({{\mathbf{A}}{\mathbf{B}}})}} \lesssim u^{- 1}$ to operate reliably.

<!-- chunk {"id": "body-0115", "role": "body", "section": "The sketched Rayleigh--Ritz method", "weight": 1.0} -->

Let us turn to the nonsymmetric eigenvalue problem

<!-- chunk {"id": "body-0116", "role": "body", "section": "The sketched Rayleigh--Ritz method", "weight": 1.0} -->

We will provide an implementation and analysis of the sRR method outlined in Section 1.3.1. Section 6.8 describes modifications for the symmetric eigenvalue problem. Section 7 covers techniques for constructing the basis for sRR.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Perspectives on Rayleigh--Ritz", "weight": 1.0} -->

Recall that eigenvalue problems are invariant under similarity transforms. In the present context, the computed eigenpairs only depend on the range of $\mathbf{B}$, so they are invariant under the map ${\mathbf{B}}\leftarrow{{\mathbf{B}}{\mathbf{T}}}$ for a nonsingular ${\mathbf{T}} \in {\mathbb{C}}^{d \times d}$. Therefore, if ${\mathbf{Q}} \in {\mathbb{C}}^{n \times d}$ is an orthonormal basis for ${range}{({\mathbf{B}})}$, then we may pass to

<!-- chunk {"id": "body-0118", "role": "body", "section": "Perspectives on Rayleigh--Ritz", "weight": 1.0} -->

Given a solution $({\mathbf{z}},\theta)$ to Eq. 37, we obtain an approximate eigenpair $({{\mathbf{Q}}{\mathbf{z}}},\theta)$ of the matrix $\mathbf{A}$. This is the most typical presentation of RR.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Perspectives on Rayleigh--Ritz", "weight": 1.0} -->

This formulation is sometimes called a rectangular eigenvalue problem. Let us emphasize that the RR method Eq. 36 does not solve the rectangular eigenvalue problem. Nevertheless, for any eigenpair $({\mathbf{y}}_{\star},\theta_{\star})$ of the matrix ${\mathbf{M}}_{\star}$, it holds that

<!-- chunk {"id": "body-0120", "role": "body", "section": "Perspectives on Rayleigh--Ritz", "weight": 1.0} -->

The matrix ${\mathbf{M}}_{\star}$ from Eq. 36 does solve a related variational problem \[37, Thm. 11.4.2\]:

<!-- chunk {"id": "body-0121", "role": "body", "section": "Perspectives on Rayleigh--Ritz", "weight": 1.0} -->

These connections support the design and analysis of a sketched version of RR.

<!-- chunk {"id": "body-0122", "role": "body", "section": "The Arnoldi method", "weight": 1.0} -->

The Arnoldi method is a classic algorithm \[42, Sec. 6.2\] for eigenvalue problems based on RR. First, it invokes the Arnoldi process (Section 4.2) to build an orthonormal basis ${\mathbf{Q}} \in {\mathbb{C}}^{n \times d}$ for a Krylov subspace (generated by a random vector) at a cost of $O{({nd^{2}})}$ operations. This construction ensures that ${\mathbf{Q}}^{\ast}{\mathbf{A}}{\mathbf{Q}}$ has upper Hessenberg form, so we can solve the eigenvalue problem Eq. 36 with $O{(d^{2})}$ operations by means of the QR algorithm \[42, Chap. 7\].

<!-- chunk {"id": "body-0123", "role": "body", "section": "The Arnoldi method", "weight": 1.0} -->

Each eigenpair $({\mathbf{y}},\theta)$ of Eq. 36 induces an approximate eigenpair $({{\mathbf{B}}{\mathbf{y}}},\theta)$ of $\mathbf{A}$, which we can form with $O{({nd})}$ operations.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Derivation of sRR", "weight": 1.0} -->

We can view the sRR method as a sketched version of the matrix optimization problem Eq. 40. Consider a subspace embedding ${\mathbf{S}} \in {\mathbb{C}}^{s \times n}$ for ${range}{({\lbrack{{\mathbf{A}}{\mathbf{B}}},{\mathbf{B}}\rbrack})}$ with distortion $\varepsilon \in {}$. The sketched problem is

<!-- chunk {"id": "body-0125", "role": "body", "section": "Derivation of sRR", "weight": 1.0} -->

The sRR method finds a solution $\hat{\mathbf{M}} \in {\mathbb{C}}^{d \times d}$ to this optimization problem. Then it poses the ordinary eigenvalue problem

<!-- chunk {"id": "body-0126", "role": "body", "section": "Derivation of sRR", "weight": 1.0} -->

Sketching allows us to obtain inexpensive a posteriori error bounds.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Derivation of sRR", "weight": 1.0} -->

By definition, the subspace embedding $\mathbf{S}$ ensures that the true residual satisfies

<!-- chunk {"id": "body-0128", "role": "body", "section": "Derivation of sRR", "weight": 1.0} -->

In other words, we can diagnose when the sRR method has (or has not) produced a high-quality approximate eigenpair $({{\mathbf{B}}\hat{\mathbf{y}}},\hat{\theta})$ of the original matrix $\mathbf{A}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Implementation of sRR", "weight": 1.0} -->

To implement sRR, we may use either an SRFT embedding Eq. 19 or a sparse embedding Eq. 20. We recommend the embedding dimension $s = {4d}$, which typically results in distortion $\varepsilon = {1/\sqrt{2}}$ for the range of $\lbrack{{\mathbf{A}}{\mathbf{B}}},{\mathbf{B}}\rbrack$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Implementation of sRR", "weight": 1.0} -->

We apply the inverse by triangular substitution. Then invoke the QR algorithm to solve the eigenvalue problem Eq. 42. Each of the last three steps costs $O{(d^{3})}$ operations.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Implementation of sRR", "weight": 1.0} -->

Given a computed eigenpair $(\hat{\mathbf{y}},\hat{\theta})$, we can obtain the sketched residual value ${\hat{r}}_{est}{(\hat{\mathbf{y}},\hat{\theta})}$ from Eq. 43 at a cost of $O{(d^{2})}$ operations. If the residual estimate is sufficiently small, we declare that $({{\mathbf{B}}\hat{\mathbf{y}}},\hat{\theta})$ is an approximate eigenpair of $\mathbf{A}$. For maximum efficiency, we present the approximate eigenvector $\hat{\mathbf{x}} = {{\mathbf{B}}\hat{\mathbf{y}}} \in {\mathbb{C}}^{n}$ in factored form. If we need the full vector $\hat{\mathbf{x}}$, it costs $O{({nd})}$ operations.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Implementation of sRR", "weight": 1.0} -->

Ironically, if we extract a large number of explicit eigenvectors, this last step dominates the cost of the computation. Usually, the number of high-quality approximate eigenpairs is moderate.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Implementation of sRR", "weight": 1.0} -->

In summary, given the basis $\mathbf{B}$, if we use sRR to solve Eq. 34, the cost of reporting the factored form of $d$ approximate eigenpairs is $O{({d^{3} + {nd{\log d}}})}$ operations. In contrast, RR requires $O{({nd^{2}})}$ arithmetic with an unstructured basis. Our numerical experience indicates that sRR is a robust alternative to RR so long as the condition number of the basis ${\kappa_{2}{({\mathbf{B}})}} \leq 10^{14}$. This fact allows us to exploit fast non-orthogonal basis constructions; see Section 7. See Algorithm 2 for a simple implementation of sRR with a partial Arnoldi basis.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Stabilization", "weight": 1.0} -->

The output of sRR is almost identical to RR provided that ${\kappa_{2}{({\mathbf{B}})}} \lesssim u^{- 1}$. This condition is very generous. In contrast, recall that the standard stability analysis \[37, Chap. 13\] for the Lanczos algorithm asks that ${\kappa_{2}{({\mathbf{B}})}} < {1 + \sqrt{u}}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Stabilization", "weight": 1.0} -->

If we see that the sketched basis ${\mathbf{S}}{\mathbf{B}}$ is very badly conditioned (${\kappa_{2}{({{\mathbf{S}}{\mathbf{B}}})}} \gtrsim u^{- 1}$), then the condition number diagnostic Eq. 18. ‣ 2.2 Whitening the basis ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777.") implies that the basis $\mathbf{B}$ is also very badly conditioned. In this case, we can stabilize sRR by regularizing the basis.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Stabilization", "weight": 1.0} -->

Then we use the QZ algorithm \[21, §7.7\] to solve the generalized eigenvalue problem^44^4When ${\kappa_{2}{({\mathbf{B}})}} \gtrsim u^{- 1}$, numerical experiments suggest this approach is more stable than reducing to a standard eigenvalue problem as in Eq. 45.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Stabilization", "weight": 1.0} -->

Each solution yields an sRR eigenpair $({{\mathbf{V}}{\mathbf{z}}},\theta)$ and an associated approximate eigenpair $({{\mathbf{B}}{\mathbf{V}}{\mathbf{z}}},\theta)$ of $\mathbf{A}$. The asymptotic cost is the same as the basic implementation.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

We will argue that RR and sRR solve eigenvalue problems that are similar to a pair of nearby eigenvalue problems.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

First, recall that ${{\mathbf{S}}{\mathbf{B}}} = {{\mathbf{U}}{\mathbf{T}}}$ is the QR decomposition of the sketched basis. Per Eq. 17. ‣ 2.2 Whitening the basis ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777."), the whitened basis $\overline{\mathbf{B}}:={{\mathbf{B}}{\mathbf{T}}^{- 1}}$ has conditioning ${\kappa_{2}{(\overline{\mathbf{B}})}} \leq {{({1 + \varepsilon})}/{({1 - \varepsilon})}}$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

Now, consider the variational problem Eq.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

Eigenvalue problems are invariant under similarity, so it suffices to show $\overline{\mathbf{M}} \approx {\overline{\mathbf{M}}}_{\star}$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

To that end, we invoke Eq. 16. ‣ 2.1 Sketching for least-squares problems ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777.") columnwise to obtain the comparison

<!-- chunk {"id": "body-0143", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

From the last two displays, a short argument using the triangle inequality and the conditioning of the whitened basis produces

<!-- chunk {"id": "body-0144", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

Here is an interpretation. If ${{range}{({\mathbf{Q}})}} = {{range}{({\mathbf{B}})}}$ is close to an invariant subspace of $\mathbf{A}$, then ${{({\mathbf{I} - {{\mathbf{Q}}{\mathbf{Q}}^{\ast}}})}{\mathbf{A}}{\mathbf{Q}}} \approx \mathbf{0}$. In this case, $\overline{\mathbf{M}} \approx {\overline{\mathbf{M}}}_{\star}$. Therefore, sRR and RR solve nearby eigenvalue problems, and we deduce that sRR is a backward stable approximation to RR in exact arithmetic.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Why does sRR work?", "weight": 1.0} -->

More generally, as long as ${range}{({\mathbf{B}})}$ contains an approximate eigenvector of $\mathbf{A}$ with small residual, Eq. 44 shows that the same vector yields a comparably small residual for the sketched eigenproblem Eq. 42. Unfortunately, even in this case, there is no guarantee that sRR will find an approximate eigenpair with a small residual. Indeed, the behavior of classic RR is already complicated, with pathological examples \[49, p. 282\]. Nevertheless, RR is known to provide excellent outputs in the vast majority of cases; see for the analysis.

<!-- chunk {"id": "body-0146", "role": "body", "section": "sRR with a Krylov subspace basis", "weight": 1.0} -->

When $\mathbf{B}$ is a (graded) basis for a Krylov subspace, the analysis of sRR simplifies further. In this case, the solutions ${\mathbf{M}}_{\star}$ and $\hat{\mathbf{M}}$ to Eq. 40 and Eq. 41 differ only in the final column! To verify this point, observe that Eq.

<!-- chunk {"id": "body-0147", "role": "body", "section": "sRR with a Krylov subspace basis", "weight": 1.0} -->

By construction, the vector ${\mathbf{A}}{\mathbf{b}}_{i}$ lies in the span of $\mathbf{B}$ for $i = {1,\ldots,{d - 1}}$. Each of these problems has a unique solution with zero residual. Thus, the sketched problem Eq. 41 correctly identifies the exact solution.

<!-- chunk {"id": "body-0148", "role": "body", "section": "The symmetric case", "weight": 1.0} -->

Consider the symmetric eigenvalue problem

<!-- chunk {"id": "body-0149", "role": "body", "section": "The symmetric case", "weight": 1.0} -->

We can apply sRR directly to Eq. 48. Unfortunately, sRR is not guaranteed to (and in fact does not always) return real eigenvalue estimates. At root, the sketched eigenvalue problem Eq. 42 is not (similar to) a symmetric problem. Accordingly, the computed eigenvectors need not be orthogonal. This is an inherent drawback.

<!-- chunk {"id": "body-0150", "role": "body", "section": "The symmetric case", "weight": 1.0} -->

Fortunately, for Eq. 48, sRR often computes eigenvalue estimates that are real (or nearly real), and the associated eigenvectors tend to be nearly orthogonal. We can anticipate this outcome when the whitened matrices satisfy $\overline{\mathbf{M}} \approx {\overline{\mathbf{M}}}_{\star}$. Indeed, the eigenvalues of a symmetric matrix are well-conditioned under nonsymmetric perturbations.

<!-- chunk {"id": "body-0151", "role": "body", "section": "The symmetric case", "weight": 1.0} -->

For a real symmetric matrix $\mathbf{A}$, our implementation of sRR simply extracts the real part of the computed eigenvalues and eigenvectors. When $\mathbf{A}$ is complex Hermitian, we force the eigenvalues to be real (but not eigenvectors). The design of a fast algorithm that respects symmetry remains an open problem.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Constructing a basis for sRR", "weight": 1.0} -->

The performance of RR and sRR depends on the quality of the basis construction. For these problems, it is natural to consider block Krylov bases generated by random vectors. As before, we can consider nonorthogonal basis constructions. Owing to the overlap with the discussion of single-vector Krylov spaces, our presentation here is more telegraphic.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

For the eigenvalue problem Eq. 34, we can search for solutions using sRR with a block Krylov subspace. Let $\mathbf{\Omega} \in {\mathbb{C}}^{n \times b}$ be an initial matrix; the dimension $b$ is called the block size. Define

<!-- chunk {"id": "body-0154", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

Setting $d = {bp}$, we can express a basis ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$ for this subspace in the form

<!-- chunk {"id": "body-0155", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

Here, $\{\varphi_{i}:{i = {1,\ldots,d}}\}$ is a linearly independent family of filter polynomials. For eigenvalue problems, the generating matrix $\mathbf{\Omega} \in {\mathbb{C}}^{n \times b}$ may be drawn at random from a standard normal distribution.^55^5In this context, we do not derive much computational benefit from fancier nonadaptive distributions, such as SRFTs or sparse embeddings.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Block Krylov subspaces", "weight": 1.0} -->

Historically, the NLA literature has prescribed a small block size, say $b \leq 4$, and a large depth $p$. More recent research \[30, Sec. 11\] has identified an opportunity to use a large block size $b$, say 10s or 100s, with a much smaller depth, say $p \leq 10$. This shift in perspective has already transformed the computational profile of block Krylov methods for low-rank approximation. For instance, we can parallelize the computation over the columns of $\mathbf{\Omega}$ (or over the filter polynomials $\varphi_{i}$). In combination with sRR, nonorthogonal basis constructions promise further benefits. See for theoretical analysis of block Krylov subspaces for low-rank matrix approximation and symmetric eigenvalue problems.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Remark 7.1 (Other kinds of bases)", "weight": 1.0} -->

There are other subspace projection methods for solving eigenvalue problems that use bases other than Krylov subspaces. For example, the Jacobi--Davidson method and the LOBPCG algorithm uses alternative ideas to build a search space. These methods may also be combined with sRR.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Basis diagnostics and restarting", "weight": 1.0} -->

As with single-vector Krylov subspaces, we can sketch basis vectors as they are generated to collect summary information about the quality of the basis. Indeed, if ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$ is a basis, then the condition number of the sketched basis $\kappa_{2}{({{\mathbf{S}}{\mathbf{B}}})}$ serves as a proxy for $\kappa_{2}{({\mathbf{B}})}$; see Eq. 18. ‣ 2.2 Whitening the basis ‣ 2 Background: Subspace embeddings ‣ Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue ProblemsDate: 29 October 2021. Revised: 4 February 2022. \funding JAT acknowledges ONR BRC N00014-1-18-2363 and NSF FRG 1952777."). When the basis is poor, it can be important to use stabilized sRR (Section 6.5).

<!-- chunk {"id": "body-0159", "role": "body", "section": "Basis diagnostics and restarting", "weight": 1.0} -->

It can also be effective to restart production of the Krylov subspace when the quality of the basis starts to decline. For example, we may compute a basis for the Krylov subspace $\mathsf{K}_{p}{({\mathbf{A}};\mathbf{\Omega})}$, and we can feed this basis to sRR to extract a matrix $\mathbf{X}$ whose columns approximately span the desired invariant subspace of $\mathbf{A}$. Then we pass to the Krylov subspace $\mathsf{K}_{p}{({\mathbf{A}};{\mathbf{X}})}$, and so forth. Randomized subspace iteration is a simple version of this technique.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Basis diagnostics and restarting", "weight": 1.0} -->

Another possibility for restarting is to deflate converged eigenpairs by working in their orthogonal complement. Convergence of Ritz pairs and loss of orthogonality are known to be tightly linked \[37, Ch. 11\]. Felicitously, sRR is able to identify such eigenpairs cheaply. Optimizing the sRR restarting strategy is left as future work.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Block monomial basis with orthogonalization", "weight": 1.0} -->

Although the monomial basis is anathema for large-degree polynomials, we can still use it for shallow Krylov subspaces (say, when $p < 5$). In this case, we can assemble a basis ${\mathbf{B}} = {\lbrack{\mathbf{B}}_{1},\ldots,{\mathbf{B}}_{p}\rbrack}$ for $\mathsf{K}_{p}{({\mathbf{A}};\mathbf{\Omega})}$ as follows. Set ${\mathbf{B}}_{1} = {\text{orth}{(\mathbf{\Omega})}}$, and iterate

<!-- chunk {"id": "body-0162", "role": "body", "section": "Block monomial basis with orthogonalization", "weight": 1.0} -->

We acquire the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ as a by-product of this computation.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Block monomial basis with orthogonalization", "weight": 1.0} -->

The block monomial basis has been used in the "blanczos" method for low-rank matrix approximation, but it requires an expensive full orthogonalization of $\mathbf{B}$ in the final step. When used as an input to sRR, it may not be necessary to reorthogonalize the block monomial basis $\mathbf{B}$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Block Arnoldi with truncation", "weight": 1.0} -->

We can mitigate the rapid condition number growth of the block monomial basis by adding extra orthogonalization steps. For recurrence length $k \in {\mathbb{N}}$, we set ${\mathbf{B}}_{1} = {\text{orth}{(\mathbf{\Omega})}}$ and iterate

<!-- chunk {"id": "body-0165", "role": "body", "section": "Block Arnoldi with truncation", "weight": 1.0} -->

The resulting basis ${\mathbf{B}} = {\lbrack{\mathbf{B}}_{1},\ldots,{\mathbf{B}}_{p}\rbrack}$ serves as an input to sRR. The choice $k = 1$ or $k = 2$ already improves substantially over the block monomial basis.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Block Arnoldi with truncation", "weight": 1.0} -->

When $\mathbf{A}$ is Hermitian, the choice $k = 2$ corresponds to the block Lanczos method without reorthogonalization \[37, Chap. 13\]. Historically, the reorthogonalization step has been regarded as important for achieving robustness. If we use block Lanczos with sRR, then we can often dispense with reorthogonalization.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Block Arnoldi with truncation", "weight": 1.0} -->

As with sGMRES, in the unblocked case ($b = 1$), we recommend $k$-truncated Arnoldi with a modest $k$ as shown in Algorithm 2. However, for eigenvalue computations, there is compelling reason to take the block size $b \gg 1$. As the block size $b$ increases, the cost of orthogonalization quickly becomes devastating.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Block Chebyshev recurrence", "weight": 1.0} -->

By employing other polynomial recurrences, we can potentially eliminate all expensive computations that involve high-dimensional basis vectors. In particular, the shifted-and-scaled Chebyshev recurrence emerges as an appealing option.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Block Chebyshev recurrence", "weight": 1.0} -->

To implement this procedure, we typically need to perform a coarse initial eigenvalue computation (using sRR + block Arnoldi) to obtain a rough estimate for the spectrum of $\mathbf{A}$. For this purpose, a small block size $b$ and depth $p$ usually suffice. We may also consider Chebyshev polynomials based on rotated ellipses, as.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Block Chebyshev recurrence", "weight": 1.0} -->

A remarkable feature of this approach is that we can compute the block Chebyshev basis for $\mathsf{K}_{p}{({\mathbf{A}};\mathbf{\Omega})}$ with $b{({p - 1})}$ matvecs plus $O{({nbp})}$ operations. In contrast, it requires $O{({n{({bp})}^{2}})}$ extra operations to produce an (approximately) orthogonal basis. Beyond that, the Chebyshev recurrence can be implemented efficiently in parallel or with SIMD processors, and the lack of inner products and orthogonalization steps allows us to evade communication and synchronization costs.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Computational experiments", "weight": 1.0} -->

This section presents numerics that showcase the potential of sGMRES and sRR for solving large linear systems and eigenvalue problems. All examples involve real-valued matrices, with appropriate modifications to the methodology. All computations were performed in MATLAB version 2020a on a workstation with 256GB memory and 96 cores, each clocked at 3.3 GHz.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Solving linear systems with sGMRES", "weight": 1.0} -->

This subsection applies the sGMRES method to solve symmetric and nonsymmetric linear systems.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Algorithm details", "weight": 1.0} -->

Our implementation of sGMRES follows the pseudocode in Algorithm 1. We construct a basis using $k$-truncated Arnoldi with small values $k \in {\{ 2,4\}}$, unless otherwise noted. In one example, we consider a Chebyshev basis, as described in Section 4.4. We do not whiten the basis or restart sGMRES. The subspace embedding is based on an SRFT matrix Eq. 19 where $\mathbf{E}$ has independent Rademacher^66^6A Rademacher random variable takes values $\pm 1$ with equal probability. entries and $\mathbf{F}$ is a discrete cosine transform (DCT2). This sketch is easy to implement, but it uses $O{({nd{\log n}})}$ operations rather than $O{({nd{\log d}})}$.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Algorithm details", "weight": 1.0} -->

We do not report tests involving the more elaborate algorithms discussed in Section 5, because fine-tuning for optimal performance is outside the scope of this exploratory research.

<!-- chunk {"id": "body-0175", "role": "body", "section": "A nonsymmetric linear system", "weight": 1.0} -->

This subsection offers details about solving the nonsymmetric linear system, documented in Figure 1 of the introduction. The matrix $\mathbf{A}$ is the sparse instance t2em with dimension $n = {921,632}$ from the SuiteSparse Matrix Collection. The right-hand side $\mathbf{f}$ is generated via ${\mathbf{f}} = {{\mathbf{A}}{\mathbf{x}}}$, where $\mathbf{x}$ is a random vector drawn from the standard normal distribution. We compare sGMRES with the MATLAB command gmres without restarting and with restarting frequencies $\{ 10,30,100\}$. Observe that the $k$-truncated Arnoldi basis leads to a reduced matrix ${\mathbf{A}}{\mathbf{B}}$ whose condition number grows quickly, but the condition number remains below the tolerance $u^{- 1}$ throughout the computation. This property ensures that sGMRES is effective.

<!-- chunk {"id": "body-0176", "role": "body", "section": "A symmetric linear system", "weight": 1.0} -->

We consider a symmetric test matrix $\mathbf{A}$ with dimension $n = 10^{6}$, obtained by discretizing the 2D Laplacian.^77^7To generate the matrix we used the code in The matrix is positive semidefinite with kernel $\mathbf{e} = {\lbrack 1,1,\ldots,1\rbrack}^{\ast}$. We solve the Poisson problem ${{\mathbf{A}}{\mathbf{x}}} = {\mathbf{f}}$ where the right-hand side ${\mathbf{f}} = {{\mathbf{A}}{\mathbf{x}}}$ is generated as above, which forces ${{\mathbf{e}}^{\ast}{\mathbf{f}}} = 0$. For this problem, CG would be more appropriate than GMRES. In fact, specialized algorithms (e.g., multigrid) are available, but this example still offers an inspiring illustration of our methodology.

<!-- chunk {"id": "body-0177", "role": "body", "section": "A symmetric linear system", "weight": 1.0} -->

For both versions of sGMRES, the cost of $d$ iterations is about 50$\%$ slower than $d$ iterations of CG. Nevertheless, for the same number $d$ of iterations, sGMRES achieves $\ell_{2}$ residual norms that are about $5 \times$ smaller than CG. According to this metric, the sGMRES method is more efficient than CG. As we saw for the nonsymmetric problem, sGMRES is up to $6 \times$ faster than the restarted versions of GMRES, which do not converge to high accuracy. Meanwhile, sGMRES achieves the same accuracy as GMRES, but the sketched version is up to $100 \times$ faster after $3000$ iterations.

<!-- chunk {"id": "body-0178", "role": "body", "section": "A symmetric linear system", "weight": 1.0} -->

The Laplacian matrix is a natural candidate for testing the Chebyshev basis because we have prior knowledge about the spectrum. We use the fact that the eigenvalues are real numbers in the interval $\lbrack 0,8\rbrack$ to select the parameters for the Chebyshev recurrence (Section 4.4). The Chebyshev basis construction is slightly faster than the $k$-truncated Arnoldi construction because it requires no inner products or orthogonalization steps. Even so, the quality of the Chebyshev basis is decent; after $3000$ iterations, the reduced matrix has condition number ${\kappa_{2}{({{\mathbf{A}}{\mathbf{B}}})}} \approx 10^{8}$, which is good enough for sGMRES to succeed. The $k$-truncated Arnoldi basis is still better conditioned (see Figure 5), but we do not need this improvement. This experiment is intriguing because the Chebyshev basis can offer dramatic benefits in parallel computing environments.

<!-- chunk {"id": "body-0179", "role": "body", "section": "sGMRES: Hard examples", "weight": 1.0} -->

It is important to acknowledge that the sGMRES method is not always an effective tool for solving linear systems. In some cases, sGMRES inherits its weaknesses from GMRES, but there are also new phenomena that arise.

<!-- chunk {"id": "body-0180", "role": "body", "section": "sGMRES: Hard examples", "weight": 1.0} -->

First, there are linear systems where classic GMRES cannot produce a small residual because the Krylov subspace does not have sufficient approximation power. sGMRES cannot cure this debility. In these cases, preconditioning is critical.

<!-- chunk {"id": "body-0181", "role": "body", "section": "sGMRES: Hard examples", "weight": 1.0} -->

Second, sGMRES is not especially useful for problems where the matrix--vector multiply ${\mathbf{x}}\mapsto{{\mathbf{A}}{\mathbf{x}}}$ is costly relative to the other arithmetic. For example, when $\mathbf{A}$ is dense, over 99% of the runtime of GMRES or sGMRES may be devoted to matvecs.

<!-- chunk {"id": "body-0182", "role": "body", "section": "sGMRES: Hard examples", "weight": 1.0} -->

Third, and most seriously, there are linear systems where it is very difficult to construct a numerically full-rank basis for the Krylov subspace without meticulous orthogonalization. The rest of this subsection documents one such problem instance.

<!-- chunk {"id": "body-0183", "role": "body", "section": "sGMRES: Hard examples", "weight": 1.0} -->

Consider the matrix FS 680 1 from Matrix Market, which is known to instigate Krylov bases with bad behavior \[38, Table 2\]. In this case, the basis $\mathbf{B}$ and the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ and their sketches ${\mathbf{S}}{\mathbf{B}}$ and ${\mathbf{S}}{\mathbf{A}}{\mathbf{B}}$ have rapidly increasing condition number. Once ${\kappa_{2}{({{\mathbf{S}}{\mathbf{A}}{\mathbf{B}}})}} > u^{- 1}$, numerical errors can cause sGMRES to fail, even when GMRES is successful. See Figure 4 for an illustration, which shows that increasing the extent $k$ of the truncation does not help.

<!-- chunk {"id": "body-0184", "role": "body", "section": "sGMRES: Hard examples", "weight": 1.0} -->

We can always monitor the conditioning of the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ inexpensively by means of its sketch ${\mathbf{S}}{\mathbf{A}}{\mathbf{B}}$. Unfortunately, we are not aware of a reliable mechanism for controlling the conditioning, short of full orthogonalization. Indeed, $k$-truncated Arnoldi does not even guarantee monotone decrease of the condition number as $k$ increases. This issue remains a challenge for sGMRES. The ideas from may be useful here.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Solving eigenvalue problems with sRR", "weight": 1.0} -->

This subsection studies the performance of sRR for solving nonsymmetric and symmetric eigenvalue problems.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Algorithm details", "weight": 1.0} -->

Our implementation of sRR follows the pseudocode in Algorithm 2 with minor changes to facilitate comparison with the MATLAB eigs command. In particular, we focus on a single-vector Krylov subspace ($b = 1$), and we use $k$-truncated Arnoldi to form the basis. In one example, we consider a block Krylov subspace with a Chebyshev basis, as described in Section 7.5. We do not use restarting or stabilization, except as noted. The subspace embedding is based on an SRFT matrix Eq. 19 where $\mathbf{E}$ is diagonal Rademacher and $\mathbf{F}$ is a DCT2.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Algorithm details", "weight": 1.0} -->

When using eigs, we set the option opts.p=r; opts.maxit=1; to suppress restart. We set the flag opts.issym to reflect whether the problem is symmetric.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Algorithm details", "weight": 1.0} -->

For eigenvalue computations, we anticipate that block Krylov subspaces can yield significant advantages over single-vector Krylov subspaces. Some of these improvements derive from higher-order BLAS. We can also take advantage of SIMD architectures, and we can reduce costs of communication and synchronization in parallel computing environments.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Nonsymmetric eigenvalue problems", "weight": 1.0} -->

This section describes the nonsymmetric eigenvalue problem that forms the basis for Figure 2.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Nonsymmetric eigenvalue problems", "weight": 1.0} -->

To obtain a solution to Eq. 49, we extract a (scaled) eigenvector of Eq. 50 corresponding to the right-most eigenvalue (which must be real).

<!-- chunk {"id": "body-0191", "role": "body", "section": "Nonsymmetric eigenvalue problems", "weight": 1.0} -->

We consider an instance of Eq. 50 where $\mathbf{A}$ is an $n \times n$ tridiagonal matrix with equispaced values in $\lbrack{- 1},1\rbrack$ on the main diagonal and with $1$s on the off-diagonals. In this case, the block matrix admits a fast matrix--vector multiplication operation. The vector ${\mathbf{g}} \in {\mathbb{R}}^{n}$ is drawn from the standard normal distribution and scaled so that ${\|{\mathbf{g}}\|}_{2} = 0.01$. The constraint value $\Delta = 1$.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Nonsymmetric eigenvalue problems", "weight": 1.0} -->

We solved Eq. 50 using sRR, as described in Section 8.3.1, taking $k = 2$. The Krylov subspace was generated from the initial vector $\mathbf{0} \oplus {\mathbf{g}}$. The results appear in Fig. 2. The modest loss of accuracy in sRR after $1500$ iterations can be remedied by using the stabilization process (Section 6.5), which approximately doubles the runtime.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Symmetric eigenvalue problems", "weight": 1.0} -->

Next, we present an example of a symmetric eigenvalue problem. The matrix $\mathbf{A}$ is the 2D Laplacian matrix with dimension $n = 10^{6}$ that was introduced in Section 8.1.3. The initial vector for the Krylov subspace is drawn from the standard normal distribution, and it is shared between sRR and eigs. We use the basic Lanczos recurrence (i.e., $2$-truncation without extra orthogonalization) to construct the subspace basis. For sRR, we report the real parts of the eigenvalues and eigenvectors, as discussed in Section 6.8.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Symmetric eigenvalue problems", "weight": 1.0} -->

When the Lanczos method is used to reduce the matrix to (partial) tridiagonal form, it is critical that the Lanczos basis remain almost perfectly orthogonal. Loss of orthogonality of the basis leads to ghost eigenvalues, which are repeated estimates of a single eigenvalue \[17, Ch. 7\]. (Selective) orthogonalization is a traditional remedy, but it can be costly. In our experience, sRR rarely produces ghost eigenvalues because it does not need the basis to reduce the matrix to tridiagonal form.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Poorly conditioned bases and stabilization", "weight": 1.0} -->

When the computed basis $\mathbf{B}$ is ill-conditioned, sRR may not produce reliable eigenvalues estimates. We can partially stanch this loss by stabilization, as discussed in Section 6.5.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Poorly conditioned bases and stabilization", "weight": 1.0} -->

Without loss of generality, we consider a diagonal matrix $\mathbf{A}$. The dimension $n = 2^{19}$, and the eigenvalues are ten equispaced spaced numbers in $\lbrack{- 1},{- 0.1}\rbrack$, along with $2^{19} - 10$ equispaced numbers in $\lbrack 0,1\rbrack$. Via the block Chebyshev recurrence (Section 7.5), we construct a (nonorthogonal) basis ${\mathbf{B}} \in {\mathbb{R}}^{n \times {({bp})}}$ for the block Krylov subspace with block size $b = 100$ and increasing depth $p$. We then use classic RR, sRR, and sRRstab (the stabilized version) to compute eigenpairs of $\mathbf{A}$.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Variations and extensions", "weight": 1.0} -->

The ideas underlying sGMRES and sRR can be adapted to address a wide variety of eigenvalue and singular value computations.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Generalized eigenvalue problems", "weight": 1.0} -->

Suppose that ${\mathbf{B}} \in {\mathbb{C}}^{n \times d}$ is a basis that captures approximate solutions to Eq. 51. Following the development in Section 6.1,

<!-- chunk {"id": "body-0199", "role": "body", "section": "Generalized eigenvalue problems", "weight": 1.0} -->

Excluding basis generation, we can solve the generalized eigenvalue problem via sketching with $O{({d^{3} + {nd{\log d}}})}$ operations. In contrast, the classic RR approach typically requires $O{({nd^{2}})}$ operations.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Low-rank matrix approximation", "weight": 1.0} -->

The most successful application of randomized matrix computation has been to approximate truncated singular value decompositions efficiently. Using the new insights from our paper, we can accelerate these algorithms by sketching. The resulting techniques share some genes with sketch-based algorithms for low-rank matrix approximation, but they are different in spirit.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Low-rank matrix approximation", "weight": 1.0} -->

where ${\mathbf{Q}} \in {\mathbb{C}}^{n \times d}$ is an orthonormal basis for the range of ${\mathbf{A}}{\mathbf{B}}$. If we choose $\mathbf{B}$ at random, we obtain the Halko et al. randomized SVD algorithm. If we form an adapted basis $\mathbf{B}$ by means of subspace iteration or block Krylov methods, we obtain much better approximations, as described in the cited work.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Low-rank matrix approximation", "weight": 1.0} -->

Let ${\mathbf{S}} \in {\mathbb{C}}^{s \times n}$ be an "affine space" embedding with $s = {2d}$. (The SRFT Eq. 19 and sparse map Eq. 20 both qualify.) We pose the sketched problem

<!-- chunk {"id": "body-0203", "role": "body", "section": "Low-rank matrix approximation", "weight": 1.0} -->

The formula Eq. 56 is wholly unsuitable for practical computation, but it can be replaced with a stable and efficient variant. If we choose $\mathbf{B}$ to be a second sketching map, we obtain the (low-accuracy) sketched SVD algorithms.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Low-rank matrix approximation", "weight": 1.0} -->

Our work delivers the novel insight that using an adapted basis $\mathbf{B}$ in Eq. 56 leads to a fast and accurate algorithm for low-rank matrix approximation. Excluding the cost of basis generation, we can stably form the approximation in $O{({d^{3} + {{({m + n})}d{\log d}}})}$ operations. In contrast with sketched SVD algorithms, we attain errors similar to randomized subspace iteration or randomized block Krylov methods.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Prospects", "weight": 1.0} -->

We believe that our framework for combining sketching with subspace projection methods presents many exciting opportunities and challenges. Let us close by highlighting some of the prospects.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Prospects", "weight": 1.0} -->

First, our work suggests that traditional strategies for building high-dimensional Krylov subspace bases merit a fresh look. For example, our experiments indicate that we can easily run thousands of iterations of sGMRES, whereas orthogonalization dominates the cost of classic GMRES after, say, a few dozen iterations. One consequence is that it would suffice to find a "mediocre" preconditioner for linear systems that reduces the iteration complexity of sGMRES to 1000s of iterations, rather than the historical goal of 10s of iterations. Other aspects of basis generation that deserve further attention include restarting, deflation, and pruning.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Prospects", "weight": 1.0} -->

Second, we believe that the performance advantages of sGMRES and sRR algorithms would be maximized in modern computing environments where communication and synchronization costs dominate computation. For example, we can trivially parallelize the computation of block Krylov subspaces. Likewise, sketching allows us to perform approximate orthogonalization of distributed vectors by means of short messages. While our experiments focused on a serial computing environment, there are clear opportunities for efficient implementations on GPUs, multicore and parallel processors, distributed and cloud computing systems, and so forth.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Prospects", "weight": 1.0} -->

Third, aside from GMRES and RR, there are many subspace projection methods that might benefit from sketching. For instance, there is an important class of algorithms (BiCG, BiCGstab, CGS, QMR, etc.) for solving linear systems by means of Lanczos biorthogonalization. These methods form Krylov subspaces with respect to both $\mathbf{A}$ and ${\mathbf{A}}^{\ast}$ using three-term recurrences, but they have complicated stability properties. Perhaps, with sketching, we can improve the profile of these methods.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Prospects", "weight": 1.0} -->

Finally, let us mention one remaining difficulty. At present, we lack a reliable mechanism for guaranteeing that the condition number of basis $\mathbf{B}$ and the reduced matrix ${\mathbf{A}}{\mathbf{B}}$ do not explode. Truncated orthogonalization is a practical approach that often works well, but it can fail. It would be valuable to identify strategies for inexpensively producing computational bases that are numerically full rank.
