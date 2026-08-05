<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Enhancing Sparsity by Reweighted L1 Minimization

Topics include Compressed sensing, Sparse recovery, Reweighted L1, Convex optimization, Iterative reweighting, Signal reconstruction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes solving a sequence of weighted L1 problems to better approximate sparsity than a single unweighted relaxation. The simple iterative reweighting rule often recovers sparse signals from fewer measurements and became a standard heuristic in compressed sensing and sparse modeling.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It is now well understood that it is possible to reconstruct sparse signals exactly from what appear to be highly incomplete sets of linear measurements and that this can be done by constrained L1 minimization. In this paper, we study a novel method for sparse signal recovery that in many situations outperforms L1 minimization in the sense that substantially fewer measurements are needed for exact recovery. The algorithm consists of solving a sequence of weighted L1-minimization problems where the weights used for the next iteration are computed from the value of the current solution. We present a series of experiments demonstrating the remarkable performance and broad applicability of this algorithm in the areas of sparse signal recovery, statistical estimation, error correction and image processing. Interestingly, superior gains are also achieved when our method is applied to recover signals with assumed near-sparsity in overcomplete representations - not by reweighting the L1 norm of the coefficient sequence as is common, but by reweighting the L1 norm of the transformed object. An immediate consequence is the possibility of highly efficient data acquisition protocols by improving on a technique known as compressed sensing.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

What makes some scientific or engineering problems at once interesting and challenging is that often, one has fewer equations than unknowns. When the equations are linear, one would like to determine an object x 0 ∈ R n from data y = Φ x 0, where Φ is an m × n matrix with fewer rows than columns; i.e., m<n. The problem is of course that a system with fewer equations than unknowns usually has infinitely many solutions and thus, it is apparently impossible to identify which of these candidate solutions is indeed the 'correct' one without some additional information.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many instances, however, the object we wish to recover is known to be structured in the sense that it is sparse or compressible. This means that the unknown object depends upon a smaller number of unknown parameters. In a biological experiment, one could measure changes of expression in 30,000 genes and expect at most a couple hundred genes with a different expression level. In signal processing, one could sample or sense signals which are known to be sparse (or approximately so) when expressed in the correct basis. This premise radically changes the problem, making the search for solutions feasible since the simplest solution now tends to be the right one.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mathematically speaking and under sparsity assumptions, one would want to recover a signal x 0 ∈ R n, e.g., the coefficient sequence of the signal in the appropriate basis, by solving the combinatorial optimization problem where ‖ x ‖ ℓ 0 = |{ i: x i = 0 }|. This is a common sense approach which simply seeks the simplest explanation fitting the data. In fact, this method can recover sparse solutions even in situations in which m ≪ n. Suppose for example that all sets of m columns of Φ are in general position. Then the program (P 0) perfectly recovers all sparse signals x 0 obeying ‖ x 0 ‖ ℓ 0 ≤ m/ 2. This is of little practical use, however, since the optimization problem is nonconvex and generally impossible to solve as its solution usually requires an intractable combinatorial search.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common alternative is to consider the convex problem where ‖ x ‖ ℓ 1 = ∑ n i =1 | x i |. Unlike (P 0), this problem is convex-it can actually be recast as a linear program-and is solved efficiently. The programs (P 0) and (P 1) differ only in the choice of objective function, with the latter using an ℓ 1 norm as a proxy for the literal ℓ 0 sparsity count. As summarized below, a recent body of work has shown that perhaps surprisingly, there are conditions guaranteeing a formal equivalence between the combinatorial problem (P 0) and its relaxation (P 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The use of the ℓ 1 norm as a sparsity-promoting functional traces back several decades. A leading early application was reflection seismology, in which a sparse reflection function (indicating meaningful changes between subsurface layers) was sought from bandlimited data. In 1973, Claerbout and Muir first proposed the use of ℓ 1 to deconvolve seismic traces. Over the next decade this idea was refined to better handle observation noise, and the sparsity-promoting nature of ℓ 1 minimization was empirically confirmed. Rigorous results began to appear in the late-1980's, with Donoho and Stark and Donoho and Logan quantifying the ability to recover sparse reflectivity functions. The application areas for ℓ 1 minimization began to broaden in the mid-1990's, as the LASSO algorithm was proposed as a method in statistics for sparse model selection, Basis Pursuit was proposed in computational harmonic analysis for extracting a sparse signal representation from highly overcomplete dictionaries, and a related technique known as total variation minimization was proposed in image processing.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some examples of ℓ 1 type methods for sparse design in engineering include Vandenberghe et al. for designing sparse interconnect wiring, and Hassibi et al. for designing sparse control system feedback gains. In, Dahleh and Diaz-Bobillo solve controller synthesis problems with an ℓ 1 criterion, and observe that the optimal closed-loop responses are sparse. Lobo et al. used ℓ 1 techniques to find sparse trades in portfolio optimization with fixed transaction costs. In, Ghosh and Boyd used ℓ 1 methods to design well connected sparse graphs Sun et al. observe that optimizing the rates of a Markov process on a graph leads to sparsity. In [1, § 6.5.4, § 11.4.1], Boyd and Vandenberghe describe several problems involving ℓ 1 methods for sparse solutions, including finding small subsets of mutually infeasible inequalities, and points that violate few constraints. In a recent paper, Koh et al. used these ideas to carry out piecewise-linear trend analysis.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the last decade, the applications and understanding of ℓ 1 minimization have continued to increase dramatically. Donoho and Huo provided a more rigorous analysis of Basis Pursuit, and this work was extended and refined in subsequent years, see. Much of the recent focus on ℓ 1 minimization, however, has come in the emerging field of Compressive Sensing. This is a setting where one wishes to recover a signal x 0 from a small number of compressive measurements y = Φ x 0. It has been shown that ℓ 1 minimization allows recovery of sparse signals from remarkably few measurements: supposing Φ is chosen randomly from a suitable distribution, then with very high probability, all sparse signals x 0 for which ‖ x 0 ‖ ℓ 0 ≤ m/α with α = O (log( n/m )) can be perfectly recovered by using (P 1 ). Moreover, it has been established that Compressive Sensing is robust in the sense that ℓ 1 minimization can deal very effectively (a) with only approximately sparse signals and (b) with measurement noise.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The implications of these facts are quite farreaching, with potential applications in data compression, digital photography, medical imaging, error correction, analog-to-digital conversion, sensor networks, and so. (We will touch on some more concrete examples in Section 3.)

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The use of ℓ 1 regularization has become so widespread that it could arguably be considered the 'modern least squares'. This raises the question of whether we can improve upon ℓ 1 minimization? It is natural to ask, for example, whether a different (but perhaps again convex) alternative to ℓ 0 minimization might also find the correct solution, but with a lower measurement requirement than ℓ 1 minimization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we consider one such alternative, which aims to help rectify a key difference between the ℓ 1 and ℓ 0 norms, namely, the dependence on magnitude: larger coefficients are penalized more heavily in the ℓ 1 norm than smaller coefficients, unlike the more democratic penalization of the ℓ 0 norm. To address this imbalance, we propose a weighted formulation of ℓ 1 minimization designed to more democratically penalize nonzero coefficients. In Section 2, we discuss an iterative algorithm for constructing the appropriate weights, in which each iteration of the algorithm solves a convex optimization problem, whereas the overall algorithm does not. Instead, this iterative algorithm attempts to find a local minimum of a concave penalty function that more closely resembles the ℓ 0 norm. Finally, we would like to draw attention to the fact that each iteration of this algorithm simply requires solving one ℓ 1 minimization problem, and so the method can be implemented readily using existing software.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 3, we present a series of experiments demonstrating the superior performance and broad applicability of this algorithm, not only for recovery of sparse signals, but also pertaining to compressible signals, noisy measurements, error correction, and image processing. This section doubles as a brief tour of the applications of Compressive Sensing. In Section 4, we demonstrate the promise of this method for efficient data acquisition. Finally, we conclude in Section 5 with a final discussion of related work and future directions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Weighted ℓ 1 minimization", "weight": 1.0} -->

Consider the 'weighted' ℓ 1 minimization problem where w 1, w 2,..., w n are positive weights. Just like its 'unweighted' counterpart (P 1), this convex problem can be recast as a linear program. In the sequel, it will be convenient to denote the objective functional by ‖ Wx ‖ ℓ 1 where W is the diagonal matrix with w 1,..., w n on the diagonal and zeros elsewhere.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Weighted ℓ 1 minimization", "weight": 1.0} -->

The weighted ℓ 1 minimization (WP 1) can be viewed as a relaxation of a weighted ℓ 0 minimization problem Whenever the solution to (P 0) is unique, it is also the unique solution to (WP 0) provided that the weights do not vanish. However, the corresponding ℓ 1 relaxations (P 1) and (WP 1) will have different solutions in general. Hence, one may think of the weights (w i) as free parameters in the convex relaxation, whose values-if set wisely-could improve the signal reconstruction.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Weighted ℓ 1 minimization", "weight": 1.0} -->

This raises the immediate question: what values for the weights will improve signal reconstruction? One possible use for the weights could be to counteract the influence of the signal magnitude on the ℓ 1 penalty function. Suppose, for example, that the weights were inversely proportional to the true signal magnitude, i.e., that If the true signal x 0 is k -sparse, i.e., obeys ‖ x 0 ‖ ℓ 0 ≤ k, then (WP 1) is guaranteed to find the correct solution with this choice of weights, assuming only that m ≥ k and that just as before, the columns of Φ are in general position. The large (actually infinite) entries in w i force the solution x to concentrate on the indices where w i is small (actually finite), and by construction these correspond precisely to the indices where x 0 is nonzero. It is of course impossible to construct the precise weights without knowing the signal x 0 itself, but this suggests more generally that large weights could be used to discourage nonzero entries in the recovered signal, while small weights could be used to encourage nonzero entries.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Weighted ℓ 1 minimization", "weight": 1.0} -->

For the sake of illustration, consider the simple 3-D example in Figure 1, where x 0 = T and We wish to recover x 0 from y = Φ x 0 = T. Figure 1(a) shows the original signal x 0, the set of points x ∈ R 3 obeying Φ x = Φ x 0 = y, and the ℓ 1 ball of radius 1 centered at the origin. The interior of the ℓ 1 ball intersects the feasible set Φ x = y, and thus (P 1) finds an incorrect solution, namely, x ⋆ = [1 / 3 0 1 / 3] T = x 0 (see Figure 1(b)).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Weighted ℓ 1 minimization", "weight": 1.0} -->

Consider now a hypothetical weighting matrix W = diag(T). Figure 1(c) shows the 'weighted ℓ 1 ball' of radius ‖ Wx ‖ ℓ 1 = 1 centered at the origin. Compared to the unweighted ℓ 1 Figure 1: Weighting ℓ 1 minimization to improve sparse signal recovery. (a) Sparse signal x 0, feasible set Φ x = y, and ℓ 1 ball of radius ‖ x 0 ‖ ℓ 1. (b) There exists an x = x 0 for which ‖ x ‖ ℓ 1 < ‖ x 0 ‖ ℓ 1. (c) Weighted ℓ 1 ball. There exists no x = x 0 for which ‖ Wx ‖ ℓ 1 ≤ ‖ Wx 0 ‖ ℓ 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Weighted ℓ 1 minimization", "weight": 1.0} -->

ball (Figure 1(a)), this ball has been sharply pinched at x 0. As a result, the interior of the weighted ℓ 1 ball does not intersect the feasible set, and consequently, (WP 1) will find the correct solution x ⋆ = x 0. Indeed, it is not difficult to show that the same statements would hold true for any positive weighting matrix for which w 2 < (w 1 + w 3) / 3. Hence there is a range of valid weights for which (WP 1) will find the correct solution. As a rough rule of thumb, the weights should relate inversely to the true signal magnitudes.

<!-- chunk {"id": "body-0021", "role": "body", "section": "An iterative algorithm", "weight": 1.0} -->

The question remains of how a valid set of weights may be obtained without first knowing x 0. As Figure 1 shows, there may exist a range of favorable weighting matrices W for each fixed x 0, which suggests the possibility of constructing a favorable set of weights based solely on an approximation x to x 0 or on other side information about the vector magnitudes.

<!-- chunk {"id": "body-0022", "role": "body", "section": "An iterative algorithm", "weight": 1.0} -->

We propose a simple iterative algorithm that alternates between estimating x 0 and redefining the weights. The algorithm is as follows: 1. Set the iteration count ℓ to zero and w i = 1, i = 1,..., n. 2. Solve the weighted ℓ 1 minimization problem 3. Update the weights: for each i = 1,..., n, 4. Terminate on convergence or when ℓ attains a specified maximum number of iterations ℓ max. Otherwise, increment ℓ and go to step 2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "An iterative algorithm", "weight": 1.0} -->

We introduce the parameter ϵ > 0 in step 3 in order to provide stability and to ensure that a zero-valued component in x ( ℓ ) does not strictly prohibit a nonzero estimate at the next step. As empirically demonstrated in Section 3, ϵ should be set slightly smaller than the expected nonzero magnitudes of x 0. In general, the recovery process tends to be reasonably robust to the choice of ϵ.

<!-- chunk {"id": "body-0024", "role": "body", "section": "An iterative algorithm", "weight": 1.0} -->

Using an iterative algorithm to construct the weights ( w i ) tends to allow for successively better estimation of the nonzero coefficient locations. Even though the early iterations may find inaccurate signal estimates, the largest signal coefficients are most likely to be identified as nonzero. Once these locations are identified, their influence is downweighted in order to allow more sensitivity for identifying the remaining small but nonzero signal coefficients.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Analytical justification", "weight": 1.0} -->

The iterative reweighted algorithm falls in the general class of MM algorithms, see and references therein. In a nutshell, MM algorithms are more general than EM algorithms, and work by iteratively minimizing a simple surrogate function majorizing a given objective function. To establish this connection, consider the problem The equivalence means that if x ⋆ is a solution to, then (x ⋆, | x ⋆ |) is a solution to. And conversely, if (x ⋆, u ⋆) is a solution to, then x ⋆ is a solution to.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Analytical justification", "weight": 1.0} -->

Problem is of the general form where C is a convex set. In, the function g is concave and, therefore, below its tangent. Thus, one can improve on a guess v at the solution by minimizing a linearization of g around v. This simple observation yields the following MM algorithm: starting with v ∈ C, inductively define Figure 2: Sparse signal recovery through reweighted ℓ 1 iterations. (a) Original length n = 512 signal x 0 with 130 spikes. (b) Scatter plot, coefficient-by-coefficient, of x 0 versus its reconstruction x using unweighted ℓ 1 minimization. (c) Reconstruction x after the first reweighted iteration. (d) Reconstruction x after the second reweighted iteration.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Analytical justification", "weight": 1.0} -->

Each iterate is now the solution to a convex optimization problem. In the case of interest, this gives which is of course equivalent to One now recognizes our iterative algorithm.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analytical justification", "weight": 1.0} -->

In two papers, Fazel et al. have considered the same reweighted ℓ 1 minimization algorithm as in Section 2.2, first as a heuristic algorithm for applications in portfolio optimization, and second as a special case of an iterative algorithm for minimizing the rank of a matrix subject to convex constraints. Using general theory, they argue that ∑ n i =1 log( | x ( ℓ ) i | + ϵ ) converges to a local minimum of g ( x ) = ∑ n i =1 log( | x i | + ϵ ) (note that this not saying that the sequence ( x ( ℓ ) ) converges). Because the log-sum penalty function is concave, one cannot expect this algorithm to always find a global minimum. As a result, it is important to choose a suitable starting point for the algorithm. Like, we have suggested initializing with the solution to (P 1 ), the unweighted ℓ 1 minimization. In practice we have found this to be an effective strategy. Further connections between our work and FOCUSS strategies are discussed at the end of the paper.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Analytical justification", "weight": 1.0} -->

The connection with the log-sum penalty function provides a basis for understanding why reweighted ℓ 1 minimization can improve the recovery of sparse signals. In particular, the logsum penalty function has the potential to be much more sparsity-encouraging than the ℓ 1 norm. Consider, for example, three potential penalty functions for scalar magnitudes t: where the constant of proportionality is set such that f log,ϵ = 1 = f 0 = f 1, see Figure 3. The first (ℓ 0 -like) penalty function f 0 has infinite slope at t = 0, while its convex (ℓ 1 -like) relaxation f 1 has unit slope at the origin. The concave penalty function f log,ϵ, however, has slope at the origin that grows roughly as 1 /ϵ when ϵ → 0. Like the ℓ 0 norm, this allows a relatively large penalty to be placed on small nonzero coefficients and more strongly encourages them to be set to zero.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Analytical justification", "weight": 1.0} -->

In fact, f log,ϵ (t) tends to f 0 (t) as ϵ → 0. Following this argument, it would appear that ϵ should be set arbitrarily small, to most closely make the log-sum penalty resemble the ℓ 0 norm. Unfortunately, as ϵ → 0, it becomes more likely that the iterative reweighted ℓ 1 algorithm will get stuck in an undesirable local minimum. As shown in Section 3, a cautious choice of ϵ (slightly smaller than the expected nonzero magnitudes of x) provides the stability necessary to correct for inaccurate coefficient estimates while still improving upon the unweighted ℓ 1 algorithm for sparse recovery.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Variations", "weight": 1.0} -->

One could imagine a variety of possible reweighting functions in place of. We have experimented with alternatives, including a binary (large/small) setting of w i depending on the current guess. Though such alternatives occasionally provide superior reconstruction of sparse signals, we have found the rule to perform well in a variety of experiments and applications.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Variations", "weight": 1.0} -->

Alternatively, one can attempt to minimize a concave function other than the log-sum penalty. For instance, we may consider in lieu of ∑ n i =1 log(1 + | x i | /ϵ). The function atan is bounded above and ℓ 0 -like. If x is the current guess, this proposal updates the sequence of weights as w i = 1 / (x 2 i + ϵ 2). There are of course many possibilities of this nature and they tend to work well (sometimes better than the log-sum penalty). Because of space limitations, however, we will limit ourselves to empirical studies of the performance of the log-sum penalty, and leave the choice of other penalties for further research.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Historical progression", "weight": 1.0} -->

The development of the reweighted ℓ 1 algorithm has an interesting historical parallel with the use of Iteratively Reweighted Least Squares (IRLS) for robust statistical estimation. Consider a regression problem Ax = b where the observation matrix A is overdetermined. It was noticed that standard least squares regression, in which one minimizes ‖ r ‖ 2 where r = Ax -b is the residual vector, lacked robustness vis a vis outliers. To defend against this, IRLS was proposed as an iterative method to minimize instead the objective where ρ (·) is a penalty function such as the ℓ 1 norm. This minimization can be accomplished by solving a sequence of weighted least-squares problems where the weights { w i } depend on the previous residual w i = ρ ′ (r i) /r i. For typical choices of ρ this dependence is in fact inversely proportional-large residuals will be penalized less in the subsequent iteration and vice versaas is the case with our reweighted ℓ 1 algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Historical progression", "weight": 1.0} -->

Interestingly, just as IRLS involved iteratively reweighting the ℓ 2 -norm in order to better approximate an ℓ 1 -like criterion, our algorithm involves iteratively reweighting the ℓ 1 -norm in order to better approximate an ℓ 0 -like criterion.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We present a series of experiments demonstrating the benefits of reweighting the ℓ 1 penalty. We will see that the requisite number of measurements to recover or approximate a signal is typically reduced, in some cases by a substantial amount. We also demonstrate that the reweighting approach is robust and broadly applicable, providing examples of sparse and compressible signal recovery, noise-aware recovery, model selection, error correction, and 2-dimensional total-variation minimization. Meanwhile, we address important issues such as how one can choose ϵ wisely and how robust is the algorithm to this choice, and how many reweighting iterations are needed for convergence.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sparse signal recovery", "weight": 1.0} -->

The purpose of this first experiment is to demonstrate that reweighting reduces the necessary sampling rate for sparse signals that this recovery is robust with respect to the choice of ϵ and that few reweighting iterations are typically needed in practice. The setup for each trial is as follows. We select a sparse signal x 0 of length n = 256 with ‖ x 0 ‖ ℓ 0 = k. The k nonzero spike positions are chosen randomly, and the nonzero values are chosen randomly from a zero-mean unit-variance Gaussian distribution. We set m = 100 and sample a random m × n matrix Φ with i.i.d. Gaussian entries, giving the data y = Φ x 0. To recover the signal, we run several reweighting iterations with equality constraints (see Section 2.2). The parameter ϵ remains fixed during these iterations. Finally, we run 500 trials for various fixed combinations of k and ϵ.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sparse and compressible signal recovery with adaptive choice of ϵ", "weight": 1.0} -->

We would like to confirm the benefits of reweighted ℓ 1 minimization for compressible signal recovery and consider the situation when the parameter ϵ is not provided in advance and must be estimated during reconstruction. We propose an experiment in which each trial is designed as follows. We sample a signal of length n = 256 from one of three types of distribution: k -sparse with i.i.d. Gaussian entries, k -sparse with i.i.d. symmetric Bernoulli ± 1 entries, or compressible, constructed by randomly permuting the sequence { i -1 /p } n i =1 for a fixed p, applying random sign flips, and normalizing so that ‖ x 0 ‖ ℓ ∞ = 1. We set m = 128 and sample a random m × n matrix Φ with i.i.d. Gaussian entries. To recover the signal, we again solve a reweighted ℓ 1 minimization with equality constraints y = Φ x 0 = Φ x.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sparse and compressible signal recovery with adaptive choice of ϵ", "weight": 1.0} -->

In this case, however, we adapt ϵ at each iteration as a function of the current guess x (ℓ); step 3 of the algorithm is modified as follows: Figure 4: Sparse signal recovery from m = 100 random measurements of a length n = 256 signal. The probability of successful recovery depends on the sparsity level k. The dashed curves represent a reweighted ℓ 1 algorithm that outperforms the traditional unweighted ℓ 1 approach (solid curve). (a) Performance after 4 reweighting iterations as a function of ϵ. (b) Performance with fixed ϵ = 0. 1 as a function of the number of reweighting iterations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Let ( | x | ( i ) ) denote a reordering of ( | x i | ) in decreasing order of magnitude. Set", "weight": 1.0} -->

Our motivation for choosing this value for ϵ is based on the anticipated accuracy of ℓ 1 minimization for arbitrary signal recovery. In general, the reconstruction quality afforded by ℓ 1 minimization is comparable (approximately) to the best i 0 -term approximation to x 0, and so we expect approximately this many signal components to be approximately correct. Choosing the smallest of these gives us a rule of thumb for choosing ϵ.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Let ( | x | ( i ) ) denote a reordering of ( | x i | ) in decreasing order of magnitude. Set", "weight": 1.0} -->

We run 100 trials of the above experiment for each signal type. The results for the k -sparse experiments are shown in Figure 5(a). The solid black line indicates the performance of unweighted ℓ 1 recovery (success is declared when ‖ x 0 -x ‖ ℓ ∞ ≤ 10 -3 ). This curve is the same for both the Gaussian and Bernoulli coefficients, as the success or failure of unweighted ℓ 1 minimization depends only on the support and sign pattern of the original sparse signal. The dashed curves indicate the performance of reweighted ℓ 1 minimization for Gaussian coefficients (blue curve) and Bernoulli coefficients (red curve) with ℓ max = 4. We see a substantial improvement for recovering sparse signals with Gaussian coefficients, yet we see only very slight improvement for recovering sparse signals with Bernoulli coefficients. This discrepancy likely occurs because the decay in the sparse Gaussian coefficients allows large coefficients to be easily identified and significantly downweighted early in the reweighting algorithm. With Bernoulli coefficients there is no such 'low-hanging fruit'.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Let ( | x | ( i ) ) denote a reordering of ( | x i | ) in decreasing order of magnitude. Set", "weight": 1.0} -->

The results for compressible signals are shown in Figure 5(b),(c). Each plot represents a histogram, over 100 trials, of the ℓ 2 reconstruction error improvement afforded by reweighting, namely, ‖ x 0 -x ‖ ℓ 2 / ‖ x 0 -x ‖ ℓ 2. We see the greatest improvements for smaller p corresponding to sparser signals, with reductions in ℓ 2 reconstruction error up to 50% or more. As p → 1, the improvements diminish.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Recovery from noisy measurements", "weight": 1.0} -->

Reweighting can be applied to a noise-aware version of ℓ 1 minimization, further improving the recovery of signals from noisy data. We observe y = Φ x 0 + z, where z is a noise term which is either stochastic or deterministic. To recover x 0, we adapt quadratically-constrained ℓ 1 minimization, and modify step 2 of the reweighted ℓ 1 algorithm with equality constraints (see Section 2.2) as The parameter δ is adjusted so that the true vector x 0 be feasible (resp. feasible with high probability) for in the case where z is deterministic (resp. stochastic).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Recovery from noisy measurements", "weight": 1.0} -->

To demonstrate how this proposal improves on plain ℓ 1 minimization, we sample a vector of length n = 256 from one of three types of distribution: k -sparse with k = 38 and i.i.d. Gaussian entries, k -sparse with k = 38 and i.i.d. symmetric Bernoulli ± 1 entries, or compressible, constructed by randomly permuting the sequence { i -1 /p } n i =1 for a fixed p, applying random sign flips, and normalizing so that ‖ x 0 ‖ ℓ ∞ = 1. The matrix Φ is 128 × 256 with i.i.d. Gaussian entries whose columns are subsequently normalized, and the noise vector z is drawn from an i.i.d. Gaussian zero-mean distribution properly rescaled so that ‖ z ‖ ℓ 2 = β ‖ Φ x ‖ ℓ 2 with β = 0.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Recovery from noisy measurements", "weight": 1.0} -->

2; i.e., z = σz 0 where z 0 is standard white noise and σ = β ‖ Φ x ‖ ℓ 2 / ‖ z 0 ‖ ℓ 2. The parameter δ is set to δ 2 = σ 2 ( m +2 √ 2 m ) as this provides a likely upper bound on ‖ z ‖ ℓ 2. We set ϵ to be the empirical maximum value of ‖ Φ ∗ ξ ‖ ℓ ∞ over several realizations of a random vector ξ ∼ N (0, σ 2 I m ). (This gives a rough estimate for the noise amplitude in the signal domain, and hence, a baseline above which significant signal components could be identified.)

<!-- chunk {"id": "body-0045", "role": "body", "section": "Recovery from noisy measurements", "weight": 1.0} -->

We run 100 trials for each signal type. Figure 6 shows histograms of the ℓ 2 reconstruction error improvement afforded by 9 iterations, i.e., each histogram documents ‖ x 0 -x ‖ ℓ 2 / ‖ x 0 -x ‖ ℓ 2 Figure 6: Sparse and compressible signal reconstruction from noisy measurements. Histograms indicate the ℓ 2 reconstruction error improvements afforded by the reweighted quadratically-constrained ℓ 1 minimization for various signal types. over 100 trials. We see in these experiments that the reweighted quadratically-constrained ℓ 1 minimization typically offers improvements ‖ x 0 -x ‖ ℓ 2 / ‖ x 0 -x ‖ ℓ 2 in the range 0. 5 -1 in many examples. The results for sparse Gaussian spikes are slightly better than for sparse Bernoulli spikes, though both are generally favorable. Similar behavior holds for compressible signals, and we have observed that smaller values of p (sparser signals) allow the most improvement.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Statistical estimation", "weight": 1.0} -->

Reweighting also enhances statistical estimation as well. Suppose we observe y = Φ x 0 + z, where Φ is m × n with m ≤ n, and z is a noise vector z ∼ N (0, σ 2 I m) drawn from an i.i.d. Gaussian zero-mean distribution, say. To estimate x 0, we adapt the Dantzig selector and modify step 2 of the reweighted ℓ 1 algorithm as Again δ is a parameter making sure that the true unknown vector is feasible with high probability. To judge this proposal, we consider a sequence of experiments in which x 0 is of length n = 256 with k = 8 nonzero entries in random positions. The nonzero entries of x 0 have i.i.d. entries according to the model x i = s i (1+ | a i |) where the sign s i = ± 1 with probability 1 / 2 and a i ∼ N. The matrix Φ is 72 × 256 with i.i.d. Gaussian entries whose columns are subsequently normalized just as before. The noise vector (z i) has i.i.d.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Statistical estimation", "weight": 1.0} -->

N (0, σ 2) components with σ = 1 / 3 √ k/m ≈ 0. 11. The parameter δ is set to be the empirical maximum value of ‖ Φ ∗ z ‖ ℓ ∞ over several realizations of a random vector z ∼ N (0, σ 2 I m). We set ϵ = 0. 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Statistical estimation", "weight": 1.0} -->

After each iteration of the reweighted Dantzig selector, we also refine our estimate x (ℓ) using the Gauss-Dantzig technique to correct for a systematic bias. Let I = { i: | x (ℓ) i | > α · σ } with α = 1 / 4. Then one substitutes x (ℓ) with the least squares estimate which solves that is, by regressing y onto the subset of columns indexed by I.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Statistical estimation", "weight": 1.0} -->

We first report on one trial with ℓ max = 4. Figure 7(a) shows the original signal x 0 along with the recovery x using the first (unweighted) Dantzig selector iteration; the error is ‖ x 0 -x ‖ ℓ 2 = 1. 46.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Statistical estimation", "weight": 1.0} -->

| | Unweighted Gauss-Dantzig | Reweighted Gauss-Dantzig | Figure 7(b) shows the Dantzig selector recovery after 4 iterations; the error has decreased to ‖ x 0 -x ‖ ℓ 2 = 1. 25. Figure 7(c) shows the Gauss-Dantzig estimate x obtained from the first (unweighted) Dantzig selector iteration; this decreases the error to ‖ x 0 -x ‖ ℓ 2 = 0. 57. The estimator correctly includes all 8 positions at which x 0 is nonzero, but also incorrectly includes 4 positions at which x 0 should be zero. In Figure 7(d) we see, however, that all of these mistakes are rectified in the Gauss-Dantzig estimate x obtained from the reweighted Dantzig selector; the total error also decreases to ‖ x 0 -x ‖ ℓ 2 = 0. 29.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Statistical estimation", "weight": 1.0} -->

We repeat the above experiment across 5000 trials. Figure 8 shows a histogram of the ratio ρ 2 between the squared error loss of some estimate x and the ideal squared error for both the unweighted and reweighted Gauss-Dantzig estimators. (The results are also summarized in Table 1.) For an interpretation of the denominator, the ideal squared error ∑ min(x 2 0,i, σ 2) is roughly the mean-squared error one could achieve if one had available an oracle supplying perfect information about which coordinates of x 0 are nonzero, and which are actually worth estimating. We see again a significant reduction in reconstruction error; the median value of ρ 2 decreases from 2.43 to 1.21. As pointed out, a primary reason for this improvement comes from a more accurate identification of significant coefficients: on average the unweighted Gauss-Dantzig estimator includes 3.2 'false positives,' while the reweighted Gauss-Dantzig estimator includes only 0.5. Both algorithms correctly include all 8 nonzero positions in a large majority of trials.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Error correction", "weight": 1.0} -->

Suppose we wish to transmit a real-valued signal x 0 ∈ R n, a block of n pieces of information, to a remote receiver. The vector x 0 is arbitrary and in particular, nonsparse. The difficulty is that errors occur upon transmission so that a fraction of the transmitted codeword may be corrupted in a completely arbitrary and unknown fashion. In this setup, the authors in showed that one could transmit n pieces of information reliably by encoding the information as Φ x 0 where Φ ∈ R m × n, m ≥ n, is a suitable coding matrix, and by solving upon receiving the corrupted codeword y = Φ x 0 + e; here, e is the unknown but sparse corruption pattern. The conclusion of is then that the solution to this program recovers x 0 exactly provided that the fraction of errors is not too large. Continuing on our theme, one can also enhance the performance of this error-correction strategy, further increasing the number of corrupted entries that can be overcome.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Error correction", "weight": 1.0} -->

Select a vector of length n = 128 with elements drawn from a zero-mean unit-variance Gaussian distribution, and sample an m × n coding matrix Φ with i.i.d. Gaussian entries yielding the codeword Φ x. For this experiment, m = 4 n = 512, and k random entries of the codeword are corrupted with a sign flip. For the recovery, we simply use a reweighted version of. Our algorithm is as follows: 1. Set ℓ = 0 and w i = 1 for i = 1, 2,..., m. 2. Solve the weighted ℓ 1 minimization problem Figure 9: Unweighted (solid curve) and reweighted (dashed curve) ℓ 1 signal recovery from corrupted measurements y = Φ x 0 + e. The signal x 0 has length n = 128, the codeword y has size m = 4 n = 512, and the number of corrupted entries ‖ e ‖ ℓ 0 = k.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Error correction", "weight": 1.0} -->

3. Update the weights; let r (ℓ) = y -Φ x (ℓ) and for each i = 1,..., m, define 4. Terminate on convergence or when ℓ attains a specified maximum number of iterations ℓ max. Otherwise, increment ℓ and go to step 2.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Error correction", "weight": 1.0} -->

We set ϵ to be some factor β times the standard deviation of the corrupted codeword y. We run 100 trials for several values of β and of the size k of the corruption pattern.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Total variation minimization for sparse image gradients", "weight": 1.0} -->

In a different direction, reweighting can also boost the performance of total-variation (TV) minimization for recovering images with sparse gradients. Recall the total-variation norm of a 2dimensional array (x i,j), 1 ≤ i, j ≤ n, defined as the ℓ 1 norm of the magnitudes of the discrete gradient, where (Dx) i,j is the 2-dimensional vector of forward differences (Dx) i,j = (x i +1,j -x i,j, x i,j +1 -x i,j). Because many natural images have a sparse or nearly sparse gradient, it makes sense to search for the reconstruction with minimal TV norm, i.e., see, for example. It turns out that this problem can be recast as a second-order cone program, and thus solved efficiently.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Total variation minimization for sparse image gradients", "weight": 1.0} -->

We adapt by minimizing a sequence of weighted TV norms as follows: 2. Solve the weighted TV minimization problem 3. Update the weights; for each (i, j), 1 ≤ i, j ≤ n -1, 4. Terminate on convergence or when ℓ attains a specified maximum number of iterations ℓ max. Otherwise, increment ℓ and go to step 2.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Total variation minimization for sparse image gradients", "weight": 1.0} -->

Naturally, this iterative algorithm corresponds to minimizing a sequence of linearizations of the log-sum function 1 ≤ i,j ≤ n -1 log( ‖ ( Dx ) i,j ‖ + ϵ ) around the previous signal estimate.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Total variation minimization for sparse image gradients", "weight": 1.0} -->

∑ To show how this can enhance the performance of the recovery, consider the following experiment. Our test image is the Shepp-Logan phantom of size n = 256 × 256 (see Figure 10(a)). The pixels take values between 0 and 1, and the image has a nonzero gradient at 2184 pixels. We measure y by sampling the discrete Fourier transform of the phantom along 10 pseudo-radial lines (see Figure 10(b)). That is, y = Φ x 0, where Φ represents a subset of the Fourier coefficients of x 0. In total, we take m = 2521 real-valued measurements.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Total variation minimization for sparse image gradients", "weight": 1.0} -->

For point of comparison it takes approximately 17 radial lines ( m = 4257 real-valued measurements) to perfectly recover the phantom using unweighted TV minimization. Hence, with respect to the sparsity of the image gradient, we have reduced the requisite oversampling factor significantly, from 4257 2184 ≈ 1. 95 down to 2521 2184 ≈ 1. 15. It is worth noting that comparable reconstruction performance on the phantom image has also been recently achieved by directly minimizing a nonconvex ℓ p norm, p < 1, of the image gradient; we discuss this approach further in Section 5.1.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Reweighted ℓ 1 analysis", "weight": 1.0} -->

In many problems, a signal may assume sparsity in a possibly overcomplete representation. To make things concrete, suppose we are given a dictionary Ψ of waveforms ( ψ j ) j ∈ J (the columns of Ψ) which allows representing any signal as x = Ψ α. The representation α is deemed sparse when the vector of coefficients α has comparably few significant terms. In some applications, it may be natural to choose Ψ as an orthonormal basis but in others, a sparse representation of the signal x may only become possible when Ψ is a redundant dictionary; that is, it has more columns than rows. A good example is provided by an audio signal which often is sparsely represented as a superposition of waveforms of the general shape σ -1 / 2 g (( t -t 0 ) /σ ) e iωt, where t 0, ω, and σ are discrete shift, modulation and scale parameters.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Reweighted ℓ 1 analysis", "weight": 1.0} -->

In this setting, the common approach for sparsity-based recovery from linear measurements goes by the name of Basis Pursuit and is of the form that is, we seek a sparse set of coefficients α that synthesize the signal x = Ψ α. We call this synthesis-based ℓ 1 recovery. Afar less common approach, however, seeks a signal x whose coefficients α = Ψ ∗ x (when x is analyzed in the dictionary Ψ) are sparse We call this analysis-based ℓ 1 recovery. When Ψ is an orthonormal basis, these two programs are identical, but in general they find different solutions. When Ψ is redundant, involves fewer unknowns than and may be computationally simpler to solve. Moreover, in some cases the analysis-based reconstruction may in fact be superior, a phenomenon which is not very well understood; see for some insights.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Reweighted ℓ 1 analysis", "weight": 1.0} -->

Both programs are amenable to reweighting but what is interesting is the combination of analysis-based ℓ 1 recovery and iterative reweighting which seems especially powerful. This section provides two typical examples. For completeness, the iterative reweighted ℓ 1 -analysis algorithm is as follows: 1. Set ℓ = 0 and w (ℓ) j = 1, j ∈ J (J indexes the dictionary). 2. Solve the weighted ℓ 1 minimization problem 3. Put α (ℓ) = Ψ ∗ x (ℓ) and define 4. Terminate on convergence or when ℓ attains a specified maximum number of iterations ℓ max. Otherwise, increment ℓ and go to step 2.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Incoherent sampling of radar pulses", "weight": 1.0} -->

Our first example is motivated by our own research focused on advancing devices for analogto-digital conversion of high-bandwidth signals. To cut a long story short, standard analog-todigital converter (ADC) technology implements the usual quantized Shannon representation; that is, the signal is uniformly sampled at or above the Nyquist rate. The hardware brick wall is that conventional analog-to-digital conversion technology is currently limited to sample rates on the order of 1GHz, and hardware implementations of high precision Shannon-based conversion at substantially higher rates seem out of sight for decades to come. This is where the theory of compressive sensing becomes relevant.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Incoherent sampling of radar pulses", "weight": 1.0} -->

Whereas it may not be possible to digitize an analog signal at a very high rate rate, it may be quite possible to change its polarity at a high rate. The idea is then to multiply the signal by a pseudo-random sequence of plus and minus ones, integrate the product over time windows, and digitize the integral at the end of each time interval. This is a parallel architecture and one has several of these random multiplier-integrator pairs running in parallel using distinct or event nearly independent pseudo-random sign sequences.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Incoherent sampling of radar pulses", "weight": 1.0} -->

To show the promise of this approach, we take x 0 to be a 1-D signal of length n = 512 which is a superposition of two modulated pulses (see Figure 11(a)). From this signal, we collect m = 30 measurements using an m × n matrix Φ populated with i.i.d. Bernoulli ± 1 entries. This is an unreasonably small amount of data corresponding to an undersampling factor exceeding 17. For reconstruction we consider a time-frequency Gabor dictionary that consists of a variety of sine waves modulated by Gaussian windows, with different locations and scales. Overall the dictionary is approximately 43 × overcomplete and does not contain the two pulses that comprise x 0.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Frequency sampling of biomedical images", "weight": 1.0} -->

Compressed sensing can help reduce the scan time in Magnetic Resonance Imaging (MRI) and offer sharper images of living tissues. This is especially important because time consuming MRI scans have traditionally limited the use of this sensing modality in important applications. Simply put, faster imaging here means novel applications. In MR, one collects information about an object by measuring its Fourier coefficients and faster acquisition here means fewer measurements.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Frequency sampling of biomedical images", "weight": 1.0} -->

We mimic an MR experiment by taking our unknown image x 0 to be the n = 256 × 256 = 65536 Figure 11: (a) Original two-pulse signal (blue) and reconstructions (red) via (b) ℓ 1 synthesis, (c) ℓ 1 analysis, (d) reweighted ℓ 1 analysis. (e) Relative ℓ 2 reconstruction error as a function of reweighting iteration. pixel MR angiogram image shown in Figure 12(a). We sample the image along 80 lines in the Fourier domain (see Figure 12(b)), effectively taking m = 18737 real-valued measurements y = Φ x 0. In plain terms, we undersample by a factor of about 3.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Frequency sampling of biomedical images", "weight": 1.0} -->

We can reinterpret these results by comparing the reconstruction quality to the best k -term approximation to the image x 0 in a nonredundant wavelet dictionary. For example, an ℓ 2 reconstruction error equivalent to the ℓ 2 reconstruction of Figure 12(c) would require keeping the k = 1905 ≈ m/ 9. 84 largest wavelet coefficients from the orthogonal wavelet transform of our test image. In this sense, the requisite oversampling factor can be thought of as being 9. 84. Of course this can be substantially improved by encouraging sparsity, and the factor is reduced to 3. 33 using TV minimization, to 3. 25 using ℓ 1 analysis, and to 3. 01 using reweighted ℓ 1 analysis.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Frequency sampling of biomedical images", "weight": 1.0} -->

We would like to be clear about what this means. Consider the image in Figure 12(a) and its best k -term wavelet approximation with k = 6225; that is, the approximation obtained by computing all the D4 wavelet coefficients and retaining the k largest in the expansion of the object (and throwing out the others). Then we have shown that the image obtained by measuring 3 k real-valued Fourier measurements and solving the iterative reweighted ℓ 1 analysis has just about the same accuracy. That is, the oversampling factor needed to obtain an image of the same quality as if one knew ahead of time the locations of the k most significant pieces of information and their value, is just 3.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Discussion", "weight": 1.5} -->

In summary, reweighted ℓ 1 minimization outperforms plain ℓ 1 minimization in a variety of setups. Therefore, this technique might be of interest to researchers in the field of compressed sensing and/or statistical estimation as it might help to improve the quality of reconstructions and/or estimations. Further, this technique is easy to deploy as it can be built on top of existing ℓ 1 solvers and the number of iterations is typically very low so that the additional computational cost is not prohibitive. We conclude this paper by discussing related work and possible future directions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Future directions", "weight": 1.0} -->

In light of the promise of reweighted ℓ 1 minimization, it seems desirable to further investigate the properties of this algorithm.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Future directions", "weight": 1.0} -->

- Under what conditions does the algorithm converge? That is, when do the successive iterates x (ℓ) have a limit x (∞) ? - As shown in Section 2, when there is a sparse solution and the reweighted algorithm finds it, convergence may occur in just very few steps. It would be of interest to understand this phenomenon more precisely. - What are smart and robust rules for selecting the parameter ϵ ? That is, rules that would automatically adapt to the dynamic range and the sparsity of the object under study as to ensure reliable performance across a broad array of signals. Of interest are ways of updating ϵ as the algorithm progresses towards a solution. Of course, ϵ does not need to be uniform across all coordinates. - We mentioned the use of other functionals and reweighting rules. How do they compare? - Finally, any result quantifying the improvement of the reweighted algorithm for special classes of sparse or nearly sparse signals would be significant.
