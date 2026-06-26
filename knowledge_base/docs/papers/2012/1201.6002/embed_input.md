<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Matrix Concentration Inequalities via the Method of Exchangeable Pairs

Topics include Matrix concentration, Exchangeable pairs, Stein method, Spectral norm bounds, Random matrices, Tail inequalities, Dependent variables.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends Chatterjee's exchangeable-pairs version of Stein's method from scalar to self-adjoint matrix-valued random variables, producing exponential and moment inequalities for spectral norms. It is useful because it recovers matrix Hoeffding, Bernstein, Khintchine, and Rosenthal bounds in one framework and also handles dependent matrix functions that are awkward for independence-only proofs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper derives exponential concentration inequalities and polynomial moment inequalities for the spectral norm of a random matrix. The analysis requires a matrix extension of the scalar concentration theory developed by Sourav Chatterjee using Stein's method of exchangeable pairs. When applied to a sum of independent random matrices, this approach yields matrix generalizations of the classical inequalities due to Hoeffding, Bernstein, Khintchine and Rosenthal. The same technique delivers bounds for sums of dependent random matrices and more general matrix-valued functions of dependent random variables.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

1. Introduction. Matrix concentration inequalities control the fluctuations of a random matrix about its mean. At present, these results provide an effective method for studying sums of independent random matrices and matrix martingales. They have been used to streamline the analysis of structured random matrices in a range of applications, including statistical estimation, randomized linear algebra, stability of least-squares approximation, combinatorial and robust optimization, matrix completion and random graph theory. These works compose only a small sample of the papers that rely on matrix concentration inequalities. Nevertheless, it remains common to encounter new classes of random matrices that we cannot treat with the available techniques.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

1 Supported in part by the U.S. Army Research Laboratory and the U.S. Army Research Office under Contract/Grant number W911NF-11-1-0391.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

2 Supported by the National Defense Science and Engineering Graduate Fellowship. 3 Supported by ONR awards N00014-08-1-0883 and N00014-11-1002, AFOSR award FA9550-09-1-0643, DARPA award N66001-08-1-2065 and a Sloan Research Fellowship. AMS 2000 subject classifications. Primary 60B20, 60E15; secondary 60G09, 60F10.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Key words and phrases. Concentration inequalities, moment inequalities, Stein's method, exchangeable pairs, random matrix, noncommutative.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This is an electronic reprint of the original article published by the Institute of Mathematical Statistics in The Annals of Probability, 2014, Vol. 42, No. 3, 906-945. This reprint differs from the original in pagination and typographic detail.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The purpose of this paper is to lay the foundations of a new approach for analyzing structured random matrices. Our work is based on Chatterjee's technique for developing scalar concentration inequalities via Stein's method of exchangeable pairs. We extend this argument to the matrix setting, where we use it to establish exponential concentration bounds (Theorems 4.1 and 5.1) and polynomial moment inequalities (Theorem 7.1) for the spectral norm of a random matrix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To illustrate the power of this idea, we show that our general results imply several important concentration bounds for a sum of independent, random, Hermitian matrices. In particular, we obtain a matrix Hoeffding inequality with optimal constants (Corollary 4.2) and a version of the matrix Bernstein inequality (Corollary 5.2). Our techniques also yield concise proofs of the matrix Khintchine inequality (Corollary 7.3) and the matrix Rosenthal inequality (Corollary 7.4).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The method of exchangeable pairs also applies to matrices constructed from dependent random variables. We offer a hint of the prospects by establishing concentration results for several other classes of random matrices. In Section 9, we consider sums of dependent matrices that satisfy a conditional zero-mean property. In Section 10, we treat a broad class of combinatorial matrix statistics. Finally, in Section 11, we analyze general matrix-valued functions that have a self-reproducing property. 1.1. Notation and preliminaries. The symbol ‖·‖ is reserved for the spectral norm, which returns the largest singular value of a general complex matrix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We write M d for the algebra of all d × d complex matrices. The trace and normalized trace of a square matrix are defined as We define the linear space H d of Hermitian d × d matrices. All matrices in this paper are Hermitian unless explicitly stated otherwise. The symbols λ max (A) and λ min (A) refer to the algebraic maximum and minimum eigenvalues of a matrix A ∈ H d. For each interval I ⊂ R, we define the set of Hermitian matrices whose eigenvalues fall in that interval, The set H d + consists of all positive-semidefinite (psd) d × d matrices. Curly inequalities refer to the semidefinite partial order on Hermitian matrices. For example, we write A ≼ B to signify that the matrix B -A is psd.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We require operator convexity properties of the matrix square so often that we state them now: More generally, we have the operator Jensen inequality valid for any random Hermitian matrix, provided that E ‖ X ‖ 2 < ∞. To verify this result, simply expand the inequality E (X -E X) 2 ≽ 0. The operator Jensen inequality also holds for conditional expectation, again provided that E ‖ X ‖ 2 < ∞. 2. Exchangeable pairs of random matrices. Our approach to studying random matrices is based on the method of exchangeable pairs, which originates in the work of Charles Stein on normal approximation for a sum of dependent random variables. In this section, we explain how some central ideas from this theory extend to matrices. 2.1. Matrix Stein pairs. First, we define an exchangeable pair.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 2.1 (Exchangeable pair). Let Z and Z ′ be random variables taking values in a Polish space Z. We say that ( Z,Z ′ ) is an exchangeable pair if it has the same distribution as ( Z ′, Z ). In particular, Z and Z ′ must share the same distribution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We can obtain a lot of information about the fluctuations of a random matrix X if we can construct a good exchangeable pair ( X, X ′ ). With this motivation in mind, let us introduce a special class of exchangeable pairs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 2.2 (Matrix Stein pair). Let (Z,Z ′) be an exchangeable pair of random variables taking values in a Polish space Z, and let Ψ: Z → H d be a measurable function. Define the random Hermitian matrices We say that (X, X ′) is a matrix Stein pair if there is a constant α ∈ (0, 1] for which The constant α is called the scale factor of the pair. When discussing a matrix Stein pair (X, X ′), we always assume that E ‖ X ‖ 2 < ∞.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A matrix Stein pair (X, X ′) has several useful properties. First, (X, X ′) always forms an exchangeable pair. Second, it must be the case that E X = 0. Indeed, because of identity (2.1), the tower property of conditional expectation and the exchangeability of (X, X ′). In Section 2.4, we construct a matrix Stein pair for a sum of centered, independent random matrices. More sophisticated examples appear in Sections 9, 10 and 11.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Remark 2.3 (Approximate matrix Stein pairs). In the scalar setting, it is common to consider exchangeable pairs that satisfy an approximate Stein condition. For matrices, this condition reads E [X -X ′ | Z] = α X + R, where R is an error term. The methods in this paper extend easily to this case. 2.2. The method of exchangeable pairs. A well-chosen matrix Stein pair (X, X ′) provides a surprisingly powerful tool for studying the random matrix X. The technique depends on a fundamental technical lemma.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Lemma 2.4 (Method of exchangeable pairs). Suppose that (X, X ′) ∈ H d × H d is a matrix Stein pair with scale factor α. Let F: H d → H d be a measurable function that satisfies the regularity condition In short, the randomness in the Stein pair furnishes an alternative expression for the expected product of X and the function F. Identity (2.3) is valuable because it allows us to estimate this integral using the smoothness properties of the function F and the discrepancy between X and X ′.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proof of Lemma 2.4. Suppose (X, X ′) is a matrix Stein pair constructed from an auxiliary exchangeable pair (Z,Z ′). The defining property (2.1) implies We have used regularity condition (2.2) to invoke the pull-through property of conditional expectation. Since (X, X ′) is an exchangeable pair, Identity (2.3) follows when we average the two preceding displays. □ 2.3. The conditional variance. To each matrix Stein pair (X, X ′), we may associate a random matrix called the conditional variance of X. The ultimate purpose of this paper is to argue that the spectral norm of X is unlikely to be large when the conditional variance is small.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 2.5 (Conditional variance). Suppose that (X, X ′) is a matrix Stein pair, constructed from an auxiliary exchangeable pair (Z,Z ′). The conditional variance is the random matrix where α is the scale factor of the pair. We may take any version of the conditional expectation in this definition.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The conditional variance ∆ X should be regarded as a stochastic estimate for the variance of the random matrix X. Indeed, This identity follows from Lemma 2.4 with the choice F (X) = X. 2.4. Example: A sum of independent random matrices. To make the definitions in this section more vivid, we describe a simple but important example of a matrix Stein pair. Consider an independent sequence Z:= (Y 1,..., Y n) of random Hermitian matrices that satisfies E Y k = 0 and E ‖ Y k ‖ 2 < ∞ for each k. Introduce the random series Let us explain how to build a good matrix Stein pair (X, X ′). We need the exchangeable counterpart X ′ to have the same distribution as X, but it should also be close to X so that we can control the conditional variance. To achieve these goals, we construct X ′ by picking a summand from X at random and replacing it with a fresh copy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Formally, let Y ′ k be an independent copy of Y k for each index k, and draw a random index K uniformly from { 1,..., n } and independently from everything else. Define the random sequence One can check that (Z,Z ′) forms an exchangeable pair. The random matrix is thus an exchangeable counterpart for X. To verify that (X, X ′) is a Stein pair, calculate that The third identity holds because Y ′ k is a centered random matrix that is independent from Z. Therefore, (X, X ′) is a matrix Stein pair with scale factor α = n -1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, we compute the conditional variance: For the third relation, expand the square and invoke the pull-through property of conditional expectation. We may drop the conditioning because Y ′ k is independent from Z. In the last line, we apply the property that Y ′ k has the same distribution as Y k.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Expression (2.6) shows that we can control the size of the conditional expectation uniformly if we can control the size of the individual summands. This example also teaches us that we may use the symmetries of the distribution of the random matrix to construct a matrix Stein pair. 3. Exponential moments and eigenvalues of a random matrix. Our main goal in this paper is to study the behavior of the extreme eigenvalues of a random Hermitian matrix. In Section 3.2, we describe an approach to this problem that parallels the classical Laplace transform method for scalar random variables. The adaptation to the matrix setting leads us to consider the trace of the moment generating function (m.g.f.) of a random matrix. After presenting this background, we explain how the method of exchangeable pairs can be used to control the growth of the trace m.g.f. This result, which appears in Section 3.5, is the key to our exponential concentration bounds for random matrices. 2. 3.1. Standard matrix functions. Before entering the discussion, recall that a standard matrix function is obtained by applying a real function to the eigenvalues of a Hermitian matrix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Higham provides an excellent treatment of this concept.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 3.1 (Standard matrix function). Let f: I → R be a function on an interval I of the real line. Suppose that A ∈ H d ( I ) has the eigenvalue decomposition A = Q · diag( λ 1,..., λ d ) · Q ∗ where Q is a unitary matrix. Then the matrix extension f ( A ):= Q · diag( f ( λ 1 ),..., f ( λ d )) · Q ∗.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The spectral mapping theorem states that, if λ is an eigenvalue of A, then f ( λ ) is an eigenvalue of f ( A ). This fact follows from Definition 3.1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When we apply a familiar scalar function to a Hermitian matrix, we are always referring to a standard matrix function. For instance, | A | is the matrix absolute value, exp(A) is the matrix exponential, and log(A) is the matrix logarithm. The latter is defined only for positive-definite matrices. 3.2. The matrix Laplace transform method. Let us introduce a matrix variant of the classical moment generating function. We learned this definition from Ahlswede-Winter, Appendix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 3.2 (Trace m.g.f.). Let X be a random Hermitian matrix. The (normalized) trace moment generating function of X is defined as We admit the possibility that the expectation may not exist for all θ.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Ahlswede and Winter, Appendix, had the insight that the classical Laplace transform method could be extended to the matrix setting by replacing the classical m.g.f. with the trace m.g.f. This adaptation allows us to obtain concentration inequalities for the extreme eigenvalues of a random Hermitian matrix using methods from matrix analysis. The following proposition distills results from the papers.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proposition 3.3 (Matrix Laplace transform method). Let X ∈ H d be a random matrix with trace m.g.f. m (θ):= E ¯ tr e θ X. For each t ∈ R, Estimates (3.3) and (3.4) for the expectations are usually sharp up to the logarithm of the dimension. In many situations, tail bounds (3.1) and (3.2) are reasonable for moderate t, but they tend to overestimate the probability of a large deviation. Note that, in general, we cannot dispense with the dimensional factor d. See, Section 4, for a detailed discussion of these issues. Additional inequalities for the interior eigenvalues can be established using the minimax Laplace transform method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proof of Proposition 3.3. To establish (3.1), fix θ > 0. Owing to Markov's inequality, The third relation depends on the spectral mapping theorem and the monotonicity of the exponential. The last inequality holds because the trace of a positive-definite matrix exceeds its maximum eigenvalue. Identify the normalized trace m.g.f., and take the infimum over θ to complete the argument.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The proof of (3.2) parallels the proof of (3.1). For θ < 0, We used the property that -λ min (A) = λ max (-A) for each Hermitian matrix A. The rest of the argument is the same as in the preceding paragraph. For the expectation bound (3.3), fix θ > 0. Jensen's inequality yields The justification is the same as above. Identify the normalized trace m.g.f., and take the infimum over θ > 0. Similar considerations yield (3.4). □ 3.3. Studying the trace m.g.f. with exchangeable pairs. The technical difficulty in the matrix Laplace transform method arises because we need to estimate the trace m.g.f. Previous authors have applied deep results from matrix analysis to accomplish this bound: the Golden-Thompson inequality is central to, while Lieb's result, Theorem 6, animates.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In this paper, we develop a fundamentally different technique for studying the trace m.g.f. The main idea is to control the growth of the trace m.g.f. by bounding its derivative. To see why we have adopted this strategy, consider a random Hermitian matrix X, and observe that the derivative of its trace m.g.f. can be written as under appropriate regularity conditions. This expression has just the form that we need to invoke the method of exchangeable pairs, Lemma 2.4, with F (X) = e θ X. We obtain This formula strongly suggests that we should apply a mean value theorem to control the derivative; we establish the result that we need in Section 3.4 below. Ultimately, this argument leads to a differential inequality for m ′ (θ), which we can integrate to obtain an estimate for m (θ).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The technique of bounding the derivative of an m.g.f. lies at the heart of the log-Sobolev method for studying concentration phenomena, Chapter 5. Recently, Chatterjee demonstrated that the method of exchangeable pairs provides another way to control the derivative of an m.g.f. Our arguments closely follow the pattern set by Chatterjee; the novelty inheres in the extension of these ideas to the matrix setting and the striking applications that this extension permits. 3.4. The mean value trace inequality. To bound expression (3.5) for the derivative of the trace m.g.f., we need a matrix generalization of the mean value theorem for a function with a convex derivative. We state the result in full generality because it plays a role later.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Paper Body", "weight": 1.0} -->

- Lemma 3.4 (Mean value trace inequality). Let I be an interval of the real line. Suppose that g: I → R is a weakly increasing function and that h: I → R is a function whose derivative h ′ is convex. For all matrices A, B ∈ H d (I), it holds that When h ′ is concave, the inequality is reversed. The same results hold for the standard trace.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To prove Lemma 3.4, we require a trace inequality, Proposition 3, that follows from the definition of a matrix function and the spectral theorem for Hermitian matrices.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proposition 3.5 (Generalized Klein inequality). Let u 1,..., u n and v 1,..., v n be real-valued functions on an interval I of the real line. Suppose With the generalized Klein inequality, we can establish Lemma 3.4 by developing the appropriate scalar inequality.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proof of Lemma 3.4. Fix a, b ∈ I. Since g is weakly increasing, (g (a) -g (b)) · (a -b) ≥ 0. The fundamental theorem of calculus and the convexity of h ′ yield the estimate The inequality is reversed when h ′ is concave.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Bound (3.7) can be written in the form (3.6) by expanding the products and collecting terms depending on a into functions u k (a) and terms depending on b into functions v k (b). Proposition 3.5 then delivers a trace inequality, which can be massaged into the desired form using the cyclicity of the trace and the fact that standard functions of the same matrix commute. We omit the algebraic details. □ Remark 3.6. We must warn the reader that the proof of Lemma 3.4 succeeds because the trace contains a product of three terms involving two matrices. The obstacle to proving more general results is that we cannot reorganize expressions like tr(ABAB) and tr(ABC) at will. 3.5. Bounding the derivative of the trace m.g.f. The central result in this section applies the method of exchangeable pairs and the mean value trace inequality to bound the derivative of the trace m.g.f. in terms of the conditional variance. This is the most important step in our theory on the exponential concentration of random matrices.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Lemma 3.7 (The derivative of the trace m.g.f.). Suppose that (X, X ′) ∈ H d × H d is a matrix Stein pair, and assume that X is almost surely bounded in norm. Define the trace m.g.f. m (θ):= E ¯ tr e θ X. Then The conditional variance ∆ X is defined in (2.4).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proof. We begin with the expression for the derivative of the trace m.g.f., We can move the derivative inside the expectation because of the dominated convergence theorem and the boundedness of X.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Apply the method of exchangeable pairs, Lemma 2.4, with the function F (X) = e θ X to reach an alternative representation of the derivative (3.10), We have used the boundedness of X to verify the regularity condition (2.2). Expression (3.11) is perfectly suited for an application of the mean value trace inequality, Lemma 3.4. First, assume that θ ≥ 0, and consider the function h: s ↦→ e θs. The derivative h ′: s ↦→ θ e θs is convex, so Lemma 3.4 implies that The second line follows from the fact that (X, X ′) is an exchangeable pair. In the last line, we have used the boundedness of X and X ′ to invoke the pull-through property of conditional expectation. Identify the conditional variance ∆ X, defined in (2.4), to complete the argument.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The result for θ ≤ 0 follows from an analogous argument. In this case, we simply observe that the derivative of the function h: s ↦→ e θs is now concave, so the mean value trace inequality, Lemma 3.4, produces a lower bound. The remaining steps are identical. □

<!-- chunk {"id": "body-0046", "role": "body", "section": "Paper Body", "weight": 1.0} -->

- Remark 3.8 (Regularity conditions). To simplify the presentation, we have instated a boundedness assumption in Lemma 3.7. All the examples we discuss satisfy this requirement. When X is unbounded, Lemma 3.7 still holds provided that X meets an integrability condition. 4. Exponential concentration for bounded random matrices. Weare now prepared to establish exponential concentration inequalities. Our first major result demonstrates that an almost-sure bound for the conditional variance yields exponential tail bounds for the extreme eigenvalues of a random Hermitian matrix. We can also obtain estimates for the expectation of the extreme eigenvalues.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Theorem 4.1 (Concentration for bounded random matrices). Consider a matrix Stein pair (X, X ′) ∈ H d × H d. Suppose there exist nonnegative constants c, v for which the conditional variance (2.4) of the pair satisfies Then, for all t ≥ 0, This result may be viewed as a matrix analogue of Chatterjee's concentration inequality for scalar random variables, Theorem 1.5(ii). The proof of Theorem 4.1 appears below in Section 4.2. Before we present the argument, let us explain how the result provides a short proof of a Hoeffding-type inequality for matrices. 4.1. Application: Matrix Hoeffding inequality. Theorem 4.1 yields an extension of Hoeffding's inequality that holds for an independent sum of bounded random matrices.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 4.2 (Matrix Hoeffding). Consider a finite sequence (Y k) k ≥ 1 of independent random matrices in H d and a finite sequence (A k) k ≥ 1 of deterministic matrices in H d. Assume that E Y k = 0 and Y 2 k ≼ A 2 k almost surely for each index k. Then, for all t ≥ 0, P { λ max (∑ k Y k) ≥ t } ≤ d · e -t 2 / 2 σ 2 for σ 2:= 1 2 ∥ ∥ ∥ ∥ ∑ k (A 2 k + E Y 2 k) ∥ ∥ ∥ ∥. Furthermore, Proof. Let X = ∑ k Y k. Since X is a sum of centered, independent random matrices, we can use the matrix Stein pair constructed in Section 2.4. According to (2.6), the conditional variance satisfies because Y 2 k ≼ A 2 k. Invoke Theorem 4.1 with c =0 and v = σ 2 to complete the bound.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Paper Body", "weight": 1.0} -->

□ In the scalar setting d =1, Corollary 4.2 reproduces an inequality of Chatterjee, Section 1.5, which itself is an improvement over the classical scalar Hoeffding bound. In turn, Corollary 4.2 improves upon the matrix Hoeffding inequality of, Theorem 1.3, in two ways. First, we have improved the constant in the exponent to its optimal value 1 / 2. Second, we have decreased the size of the variance measure because σ 2 ≤ ‖ ∑ k A 2 k ‖. Finally, let us remark that a similar result holds under the weaker assumption that k Y 2 k ≼ A 2 almost surely.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Paper Body", "weight": 1.0} -->

∑ Corollary 4.2 admits a plethora of applications. For example, in theoretical computer science, Widgerson and Xiao employ a suboptimal matrix Hoeffding inequality, Theorem 2.6, to derive efficient, derandomized algorithms for homomorphism testing and semidefinite covering problems. Under the improvements of Corollary 4.2, their results improve accordingly. 4.2. Proof of Theorem 4.1: Exponential concentration. Suppose that (X, X ′) is a matrix Stein pair constructed from an auxiliary exchangeable pair (Z,Z ′). Our aim is to bound the normalized trace m.g.f.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The basic strategy is to develop a differential inequality, which we integrate to control m ( θ ) itself. Once these estimates are in place, the matrix Laplace transform method, Proposition 3.3, furnishes probability inequalities for the extreme eigenvalues of X.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following result summarizes our bounds for the trace m.g.f. m ( θ ).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Lemma 4.3 (Trace m.g.f. estimates for bounded random matrices). Let (X, X ′) be a matrix Stein pair, and suppose there exist nonnegative constants c, v for which Then the normalized trace m.g.f. m (θ):= E ¯ tr e θ X satisfies the bounds We establish Lemma 4.3 in Section 4.2.1 et seq. In Section 4.2.4, we finish the proof of Theorem 4.1 by combining these bounds with the matrix Laplace transform method. 4.2.1. Boundedness of the random matrix. First, we confirm that the random matrix X is almost surely bounded under hypothesis (4.3) on the conditional variance ∆ X. Recall definition (2.4) of the conditional variance, and compute that The semidefinite bound is the operator Jensen inequality (1.2), applied conditionally. The third relation follows from definition (2.1) of a matrix Stein pair.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Owing to assumption (4.3), we reach the quadratic inequality 1 2 α X 2 ≼ c X + v I. The scale factor α is positive, so we may conclude that the eigenvalues of X are almost surely restricted to a bounded interval.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Paper Body", "weight": 1.0} -->

- 4.2.2. Differential inequalities for the trace m.g.f. Since the matrix X is almost surely bounded, the derivative of the trace m.g.f. has the form To control the derivative, we combine Lemma 3.7 with the assumed inequality (4.3) for the conditional variance. For θ ≥ 0, we obtain In the last line, we have identified the trace m.g.f. (4.2) and its derivative (4.7). The second relation holds because the matrix e θ X is positive definite. Indeed, when P is psd, A ≼ B implies that tr(AP) ≤ tr(BP).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For θ ≤ 0, the same argument yields a lower bound Rearrange these inequalities to isolate the log-derivative m ′ (θ) /m (θ) of the trace m.g.f. We reach 4.2.3. Solving the differential inequalities. Observe that Therefore, we may integrate the differential inequalities (4.8) and (4.9), starting at zero, to obtain bounds on log m (θ) elsewhere.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Paper Body", "weight": 1.0} -->

First, assume that 0 ≤ θ < 1 /c. In view of (4.10), the fundamental theorem of calculus and the differential inequality (4.8) imply that We can develop a weaker inequality by making a further approximation within the integral, These inequalities are the trace m.g.f. estimates (4.5) and (4.6) appearing in Lemma 4.3.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, assume that θ ≤ 0. In this case, the differential inequality (4.9) yields This calculation delivers the trace m.g.f. bound (4.4). The proof of Lemma 4.3 is complete.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Paper Body", "weight": 1.0} -->

- 4.2.4. The matrix Laplace transform argument. With Lemma 4.3 at hand, we quickly finish the proof of Theorem 4.1. First, let us establish probability inequalities for the maximum eigenvalue. The Laplace transform bound (3.1) and the trace m.g.f. estimate (4.5) together yield The second relation follows when we choose θ = t/ (v + ct). Similarly, the trace m.g.f. bound (4.6) delivers because the infimum occurs at θ =(1 -1 / √ 1 + 2 ct/v) /c. The final inequality depends on the numerical fact To control the expectation of the maximum eigenvalue, we combine the Laplace transform bound (3.3) and the trace m.g.f. bound (4.6) to see that The second relation can be verified using a computer algebra system.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, we turn to results for the minimum eigenvalue. Combine the matrix Laplace transform bound (3.2) with the trace m.g.f. bound (4.4) to reach The infimum is attained at θ = -t/v. To compute the expectation of the minimum eigenvalue, we apply the Laplace transform bound (3.4) and the trace m.g.f. bound (4.4), whence 5. Refined exponential concentration for random matrices. Although Theorem 4.1 is a strong result, the hypothesis ∆ X ≼ c X + v I on the conditional variance is too stringent for many situations of interest. Our second major result shows that we can use the typical behavior of the conditional variance to obtain tail bounds for the maximum eigenvalue of a random Hermitian matrix.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Theorem 5.1 (Refined concentration for random matrices). Suppose that (X, X ′) ∈ H d × H d is a matrix Stein pair, and assume that X is almost surely bounded in norm. Define the function where ∆ X is the conditional variance (2.4). Then, for all t ≥ 0 and all ψ > 0, Furthermore, for all ψ > 0, This theorem is essentially a matrix version of a result from Chatterjee's thesis, Theorem 3.13. The proof of Theorem 5.1 is similar in spirit to the proof of Theorem 4.1, so we postpone the demonstration until Appendix A.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let us offer some remarks to clarify the meaning of this result. Recall that ∆ X is a stochastic approximation for the variance of the random matrix X. We can interpret the function r (ψ) as a measure of the typical magnitude of the conditional variance. Indeed, the matrix Laplace transform result, Proposition 3.3, ensures that The import of this inequality is that we can often identify a value of ψ to make r (ψ) ≈ E λ max (∆ X). Ideally, we also want to choose r (ψ) ≫ ψ -1 / 2 so that the term r (ψ) drives the tail bound (5.2) when the parameter t is small. In the next subsection, we show that these heuristics yield a matrix Bernstein inequality. 5.1. Application: The matrix Bernstein inequality. As an illustration of Theorem 5.1, we establish a tail bound for a sum of centered, independent random matrices that are subject to a uniform norm bound.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 5.2 (Matrix Bernstein). Consider an independent sequence (Y k) k ≥ 1 of random matrices in H d that satisfy Then, for all t ≥ 0, Corollary 5.2 is directly comparable with other matrix Bernstein inequalities in the literature. The constants are slightly worse than, Theorem 1.4 and slightly better than, Theorem 1.2. The hypotheses in the current result are somewhat stricter than those in the prior works. Nevertheless, the proof provides a template for studying more complicated random matrices that involve dependent random variables.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proof of Corollary 5.2. Consider the matrix Stein pair (X, X ′) described in Section 2.4. Calculation (2.6) shows that the conditional variance of X satisfies The function r (ψ) measures the typical size of ∆ X. To control r (ψ), we center the conditional variance and reduce the expression as follows: The inequality depends on the monotonicity of the trace exponential, Section 2. Afterward, we have applied the identity ‖ E ∆ X ‖ = ‖ E X 2 ‖ = σ 2, which follows from (2.5) and the independence of the sequence (Y k) k ≥ 1.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Introduce the centered random matrix Observe that W consists of a sum of centered, independent random matrices, so we can study it using the matrix Stein pair discussed in Section 2.4. Adapt the conditional variance calculation (2.6) to obtain To reach the second line, we apply the operator convexity (1.1) of the matrix square to the first parenthesis, and we compute the second expectation explicitly. The third line follows from the operator Jensen inequality (1.2). To continue, make the estimate Y 4 k ≼ R 2 Y 2 k in both terms. Thus, The trace m.g.f. bound, Lemma 4.3, delivers To complete the proof, combine the bounds (5.4) and (5.6) to reach In particular, it holds that r (R -2) ≤ 1. 5 σ 2. The result now follows from Theorem 5.1. □ 6. Polynomial moments and the spectral norm of a random matrix. We can also study the spectral norm of a random matrix by bounding its polynomial moments. To present these results, we must introduce the family of Schatten norms.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 6.1 (Schatten norm). For each p ≥ 1, the Schatten p -norm is defined as In this setting, | B |:= (B ∗ B) 1 / 2. Bhatia's book, Chapter IV, contains a detailed discussion of these norms and their properties.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following proposition is a matrix analog of the Chebyshev bound from classical probability. As in the scalar case, Exercise 1, this bound is at least as tight as the analogous matrix Laplace transform bound (3.1).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proposition 6.2 (Matrix Chebyshev method). Let X be a random matrix. For all t > 0, Proof. To prove (6.1), we use Markov's inequality. For p ≥ 1, since the trace of a positive matrix dominates the maximum eigenvalue. To verify (6.2), select p ≥ 1. Jensen's inequality implies that Identify the Schatten p -norm and take infima to complete the bounds. □ 7. Polynomial moment inequalities for random matrices. Our last major result demonstrates that the polynomial moments of a random Hermitian matrix are controlled by the moments of the conditional variance. By combining this result with the matrix Chebyshev method, Proposition 6.2, we can obtain probability inequalities for the spectral norm of a random Hermitian matrix.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Theorem 7.1 (Matrix BDG inequality). Let p =1 or p ≥ 1. 5. Suppose that (X, X ′) is a matrix Stein pair where E ‖ X ‖ 2 p 2 p < ∞. Then The conditional variance ∆ X is defined in (2.4).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Remark 7.2 (Missing values). Theorem 7.1 also holds when 1 <p< 1. 5. In this range, our bound for the constant is √ 4 p -2. The proof requires a variant of the mean value trace inequality for a convex function h.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Theorem 7.1 extends a scalar result of Chatterjee, Theorem 1.5(iii), to the matrix setting. Chatterjee's bound can be viewed as an exchangeable pairs version of the Burkholder-Davis-Gundy (BDG) inequality from classical martingale theory. Other matrix extensions of the BDG inequality appear in the work of Pisier-Xu and the work of Junge-Xu. The proof of Theorem 7.1, which applies equally to infinite dimensional operators X, appears below in Section 7.3. 7.1. Application: Matrix Khintchine inequality. First, we demonstrate that the matrix BDG inequality contains an improvement of the noncommutative Khintchine inequality in the matrix setting. This result has been a dominant tool in several application areas over the last few years, largely because of the articles.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 7.3 (Matrix Khintchine). Suppose that p = 1 or p ≥ 1. 5. Consider a finite sequence (Y k) k ≥ 1 of independent, random, Hermitian matrices and a deterministic sequence (A k) k ≥ 1 for which E Y k = 0 and Y 2 k ≼ A 2 k almost surely for each index k. (7.1) Then ∥ ∥ ∥ In particular, when (ε k) k ≥ 1 is an independent sequence of Rademacher random variables, Proof. Consider the random matrix X = ∑ k Y k. We use the matrix Stein pair constructed in Section 2.4. According to (2.6), the conditional variance ∆ X satisfies An application of Theorem 7.1 completes the argument. □ For each positive integer p, the optimal constant C 2 p on the right-hand side of (7.2) satisfies as shown by Buchholz, Theorem 5. Since (2 p -1) p / (2 p -1)!! < e p -1 / 2 for each positive integer p, the constant in (7.2) lies within a factor √ e of optimal.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Previous methods for establishing the matrix Khintchine inequality are rather involved, so it is remarkable that the simple argument based on exchangeable pairs leads to a result that is so accurate. The same argument even yields a result under the weaker assumption that ∑ k Y 2 k ≼ A 2 almost surely. 7.2. Application: Matrix Rosenthal inequality. As a second example, we can develop a more sophisticated set of moment inequalities that are roughly the polynomial equivalent of the exponential moment bound underlying the matrix Bernstein inequality.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 7.4 (Matrix Rosenthal inequality). Suppose that p =1 or p ≥ 1. 5. Consider a finite sequence (P k) k ≥ 1 of independent, random psd matrices that satisfy E ‖ P k ‖ 2 p 2 p < ∞. Then ∥ Now, consider a finite sequence (Y k) k ≥ 1 of centered, independent, random Hermitian matrices, and assume that E ‖ Y k ‖ 4 p 4 p < ∞. Then Turn to Appendix B for the proof of Corollary 7.4. This result extends a moment inequality due to Nagaev and Pinelis, which refines the constants in Rosenthal's inequality, Lemma 1. See the historical discussion, Section 5, for details. An interesting application of Corollary 7.4 is to establish improved sample complexity bounds for masked sample covariance estimation when the dimension of a covariance matrix exceeds the number of samples. As we were finishing this paper, we learned that Junge and Zheng have recently established a noncommutative moment inequality, Theorem 0.4, that is quite similar to Corollary 7.4. 7.3. Proof of the matrix BDG inequality.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In many respects, the proof of the matrix BDG inequality is similar to the proof of the exponential concentration result, Theorem 4.1. Both are based on moment comparison arguments that ultimately depend on the method of exchangeable pairs and the mean value trace inequality.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Suppose that (X, X ′) is a matrix Stein pair with scale factor α. First, observe that the result for p =1 already follows from (2.5). Therefore, we may assume that p ≥ 1. 5. Introduce notation for the quantity of interest, Rewrite the expression for E by peeling off a copy of | X |. This move yields Apply the method of exchangeable pairs, Lemma 2.4, with F (X) = sgn(X) · | X | 2 p -1 to reach To verify the regularity condition (2.2) in Lemma 2.4, compute that We have used the fact that sgn (X) is a unitary matrix, the exchangeability of (X, X ′), H¨ older's inequality for expectation and the fact that the Schatten 2 p -norm dominates the spectral norm.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We intend to apply the mean value trace inequality to obtain an estimate for the quantity E. Consider the function h: s ↦→ sgn(s) · | s | 2 p -1. Its derivative h ′ (s) = (2 p -1) · | s | 2 p -2 is convex because p ≥ 1. 5. Lemma 3.4 delivers the bound The second line follows from the exchangeability of X and X ′. In the last line, we identify the conditional variance ∆ X, defined in (2.4). As before, the moment bound E ‖ X ‖ 2 p 2 p < ∞ is strong enough to justify using the pullthrough property in this step.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To continue, we must find a copy of E within the latter expression. We can accomplish this goal using one of the basic results from the theory of Schatten norms, Corollary IV.2.6.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proposition 7.5 (H¨ older inequality for trace). Let p and q be H¨ older conjugate indices, that is, positive numbers with the relationship q = p/ (p -1). Then To complete the argument, apply the H¨ older inequality for the trace followed by the H¨ older inequality for the expectation. Thus Solve this algebraic inequality for the positive number E to conclude that Extract the (2 p)th root to establish the matrix BDG inequality. 8. Extension to general complex matrices. Although, at first sight, it may seem that our theory is limited to random Hermitian matrices, results for general random matrices follow as a formal corollary. The approach is based on a device from operator theory.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Definition 8.1 (Hermitian dilation). Let B be a matrix in C d 1 × d 2, and set d = d 1 + d 2. The Hermitian dilation of B is the matrix The dilation has two valuable properties. First, it preserves spectral information, Second, the square of the dilation satisfies We can study a random matrix-not necessarily Hermitian-by applying our matrix concentration inequalities to the Hermitian dilation of the random matrix. As an illustration, let us prove a Bernstein inequality for general random matrices.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 8.2 (Bernstein inequality for general matrices). Consider a finite sequence (Z k) k ≥ 1 of independent random matrices in C d 1 × d 2 that satisfy Define d:= d 1 + d 2, and introduce the variance measure Then, for all t ≥ 0, ∥ Proof. Consider the random series ∑ k D (Z k). The summands are independent, random Hermitian matrices that satisfy The second identity depends on the spectral property (8.1). Therefore, the matrix Bernstein inequality, Corollary 5.2, applies. To state the outcome, we first note that λ max (∑ k D (Z k)) = ‖ ∑ k Z k ‖, again because of the spectral property (8.1). Next, use the formula (8.2) to compute that ∥ This observation completes the proof. □ Corollary 8.2 has important implications for the problem of estimating a matrix from noisy measurements. Indeed, bound (8.4) leads to a sample complexity analysis for matrix completion. Moreover, a variety of authors have used tail bounds of the form (8.3) to control the error of convex optimization methods for matrix estimation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Paper Body", "weight": 1.0} -->

9. A sum of conditionally independent, zero-mean matrices. A chief advantage of the method of exchangeable pairs is its ability to handle random matrices constructed from dependent random variables. In this section, we briefly describe a way to relax the independence requirement when studying a sum of random matrices. In Sections 10 and 11, we develop more elaborate examples. 2. 9.1. Formulation. Let us consider a finite sequence (Y 1,..., Y n) of random Hermitian matrices that are conditionally independent given an auxiliary random element Z. Suppose moreover that We are interested in the sum of these conditionally independent, zero-mean random matrices This type of series includes many examples that arise in practice.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Example 9.1 (Rademacher series with random matrix coefficients). Consider a finite sequence (W k) k ≥ 1 of random Hermitian matrices. Suppose the sequence (ε k) k ≥ 1 consists of independent Rademacher random variables that are independent from the random matrices. Consider the random series The summands may be strongly dependent on each other, but the independence of the Rademacher variables ensures that the summands are conditionally independent and of zero mean (9.1) given Z:= (W k) k ≥ 1.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Paper Body", "weight": 1.0} -->

- 9.2. A matrix Stein pair. Let us describe how to build a matrix Stein pair (X, X ′) for the sum (9.2) of conditionally independent, zero-mean random matrices. The approach is similar to the case of an independent sum, which appears in Section 2.4. For each k, we draw a random matrix Y ′ k so that Y ′ k and Y k are conditionally i.i.d. given (Y j) j = k. Then, independently, we draw an index K uniformly at random from { 1,..., n }. As in Section 2.4, the random matrix is an exchangeable counterpart to X. The conditional independence and conditional zero-mean (9.1) assumptions imply that, almost surely, Therefore, (X, X ′) is a matrix Stein pair with scale factor α = n -1.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We can determine the conditional variance after a short argument that parallels computation (2.6) in the independent setting, Expression (9.3) shows that, even in the presence of some dependence, we can control the size of the conditional expectation uniformly if we control the size of the individual summands.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Using the Stein pair (X, X ′) and expression (9.3), we may develop a variety of concentration inequalities for conditionally independent, zero-mean sums that are analogous to our results for independent sums. We omit detailed examples. 10. Combinatorial sums of matrices. The method of exchangeable pairs can also be applied to many types of highly symmetric distributions. In this section, we study a class of combinatorial matrix statistics, which generalize the scalar statistics studied by Hoeffding. 2. 10.1. Formulation. Consider a deterministic array (A jk) n j,k =1 of Hermitian matrices, and let π be a uniformly random permutation on { 1,..., n }. Define the random matrix The combinatorial sum Y is a natural candidate for an exchangeable pair analysis. Before we describe how to construct a matrix Stein pair, let us mention a few problems that lead to a random matrix of the form Y.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Example 10.1 (Sampling without replacement). Consider a finite collection B:= { B 1,..., B n } of deterministic Hermitian matrices. Suppose that we want to study a sum of s matrices sampled randomly from B without replacement. We can express this type of series in the form where π is a random permutation on { 1,..., n }. The matrix W is therefore an example of a combinatorial sum.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Example 10.2 (A randomized 'inner product'). Consider two fixed sequences of complex matrices We may form a permuted matrix 'inner product' by arranging one sequence in random order, multiplying the elements of the two sequences together, and summing the terms. That is, we are interested in the random matrix This random matrix D (Z) is a combinatorial sum of Hermitian matrices. 10.2. A matrix Stein pair. To study the combinatorial sum (10.1) of matrices using the method of exchangeable pairs, we first introduce the zero-mean random matrix To construct a matrix Stein pair (X, X ′), we draw a pair (J, K) of indices independently of π and uniformly at random from { 1,..., n } 2. Define a second random permutation π ′:= π ◦ (J, K) by composing π with the transposition of the random indices J and K. The pair (π,π ′) is exchangeable, so To verify that (X, X ′) is a matrix Stein pair, we calculate that The first identity holds because the sums X and X ′ differ for only four choices of indices.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Thus (X, X ′) is a Stein pair with scale factor α =2 /n.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Turning to the conditional variance, we find that The structure of the conditional variance differs from previous examples, but we recognize that ∆ X is controlled when the matrices A jk are bounded.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Paper Body", "weight": 1.0} -->

- 10.3. Exponential concentration for a combinatorial sum. We can apply our matrix concentration results to study the behavior of a combinatorial sum of matrices. As an example, let us present a Bernstein-type inequality. The argument is similar to the proof of Corollary 5.2, so we leave the details to Appendix C.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 10.3 (Bernstein inequality for a combinatorial matrix sum). Consider an array (A jk) n j,k =1 of deterministic matrices in H d that satisfy Define the random matrix X:= ∑ n j =1 A jπ (j), where π is a uniformly random permutation on { 1,..., n }. Then, for all t ≥ 0, 11. Self-reproducing matrix functions. The method of exchangeable pairs can also be used to analyze nonlinear matrix-valued functions of random variables. In this section, we explain how to analyze matrix functions that satisfy a self-reproducing property. 2. 11.1. Example: Matrix second-order Rademacher chaos. We begin with an example that shows how the self-reproducing property might arise. Consider a quadratic form that takes on random matrix values In this expression, ε is a finite vector of independent Rademacher random variables. The array (A jk) j,k ≥ 1 consists of deterministic Hermitian matrices, and we assume that A jk = A kj.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Observe that the summands in H (ε) are dependent, and they do not satisfy the conditional zero-mean property (9.1) in general. Nevertheless, H (ε) does satisfy a fruitful self-reproducing property We have applied the pull-through property of conditional expectation, the assumption that the Rademacher variables are independent and the fact that A jk = A kj. As we will see, this type of self-reproducing condition can be used to construct a matrix Stein pair.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A random matrix of the form (11.1) is called a second-order Rademacher chaos. This class of random matrices arises in a variety of situations, including randomized linear algebra, compressed sensing, Section 9, and chance-constrained optimization. Indeed, concentration inequalities for the matrix-valued Rademacher chaos have many potential applications. 11.2. Formulation and matrix Stein pair. In this section, we describe a more general version of the self-reproducing property. Suppose that z:= (Z 1,..., Z n) is a random vector taking values in a Polish space Z. First, we construct an exchangeable counterpart Next, let H: Z → H d be a bounded measurable function. Assume that H (z) satisfies an abstract self-reproducing property: for a parameter s > 0, where Z k and Z ′ k are conditionally i.i.d. given (Z j) j = k, and K is an independent coordinate drawn uniformly at random from { 1,..., n }.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Under this assumption, we can easily check that the random matrices form a matrix Stein pair. Indeed, We see that (X, X ′) is a matrix Stein pair with scaling factor α = s/n.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Finally, we compute the conditional variance We discover that the conditional variance is small when H has controlled coordinate differences. In this case, the method of exchangeable pairs provides good concentration inequalities for the random matrix X. 11.3. Matrix bounded differences inequality. As an example, we can develop a bounded differences inequality for random matrices by appealing to Theorem 4.1.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary 11.1 (Matrix bounded differences). Let z:= (Z 1,..., Z n) be a random vector taking values in a Polish space Z, and, for each index k, let Z ′ k and Z k be conditionally i.i.d. given (Z j) j = k. Suppose that H: Z → H d is a function that satisfies the self-reproducing property for a parameter s > 0 as well as the bounded differences condition E [(H (z) -H (Z 1,..., Z ′ k,..., Z n)) 2 | z] ≼ A 2 k for each index k (11.4) almost surely, where A k is a deterministic matrix in H d. Then, for all t ≥ 0, In the scalar setting, Corollary 11.1 reduces to a version of McDiarmid's bounded difference inequality. The result also complements the matrix bounded difference inequality of, Corollary 7.5, which requires independent input variables but makes no self-reproducing assumption.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proof of Corollary 11.1. Since H (z) is self-reproducing, we may construct a matrix Stein pair (X, X ′) with scale factor α = s/n as in Section 11. According to (11.3), the conditional variance of the pair satisfies We have used the bounded differences condition (11.4) and the definition of the bound L. To complete the proof, we apply the concentration result, Theorem 4.1, with the parameters c =0 and v = L/ 2 s. □
