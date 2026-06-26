<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Computational Optimal Transport: Complexity by Accelerated Gradient Descent Is Better than by Sinkhorn's Algorithm

Topics include Gradient descent, Accuracy, Optimal transport, Transport, APDAGD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We analyze two algorithms for approximating the general optimal transport (OT) distance between two discrete distributions of size n, up to accuracy epsilon. For the first algorithm, which is based on the celebrated Sinkhorn's algorithm, we prove the complexity bound O~(n^/epsilon^) arithmetic operations. For the second one, which is based on our novel Adaptive Primal-Dual Accelerated Gradient Descent (APDAGD) algorithm, we prove the complexity bound O~(min{n^(9/4)/epsilon, n^/epsilon^ }) arithmetic operations. Both bounds have better dependence on epsilon than the state-of-the-art result given by O~(n^/epsilon^). Our second algorithm not only has better dependence on epsilon in the complexity bound, but also is not specific to entropic regularization and can solve the OT problem with different regularizers.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimal transport (OT) distances between probability measures or histograms, including the earth mover's distance and MongeKantorovich or Wasserstein distance, play an increasing role in different machine learning tasks, such as unsupervised learning, semi-supervised learning, clustering, text classification, as well as in image retrieval, clustering and clas- 1 Weierstrass Institute for Applied Analysis and Stochastics, Berlin, Germany 2 National Research University Higher School of Economics, Moscow, Russian Federation 3 Moscow Institute of Physics and Technology, Dolgoprudny, Moscow Region, Russia 4 Institute for Information Transmission Problems RAS, Moscow, Russia. Correspondence to: Pavel Dvurechensky < pavel.dvurechensky@wias-berlin.de >.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Proceedings of the 35 th International Conference on Machine Learning, Stockholm, Sweden, PMLR 80, 2018. Copyright 2018 by the author(s).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

1 ˜ O hides polylogarithmic factors (ln n) c, c > 0. sification, statistics, and other applications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our focus in this paper is on the computational aspects of OT distances for the case of two discrete probability measures with support of equal 2 size n. The state-of-the-art approach for this setting is to apply Sinkhorn's algorithm to the entropy-regularized OT optimization problem. As it was recently shown, this approach allows to find an ε -approximation for an OT distance in ˜ O ( n 2 ε 3 ) arithmetic operations. In terms of the dependence on n, this result improves on the complexity ˜ O ( n 3 ) achieved by the network simplex method or interior point methods, applied directly to the OT optimization problem, which is a linear program. Nevertheless, the cubic dependence on ε prevents approximating OT distances with good accuracy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, in image color transfer or domain adaptation not only the OT distance, but also the optimal transportation plan is of interest. Recent works observe that entropic regularization of the OT problem leads to a dense transportation plan, which is in contrast to the sparse transportation plan obtained by solving the unregularized OT problem. Motivated by this observation, they study general regularization by a strongly convex function, e.g. squared euclidean norm, and show that this leads to a sparse transportation plan. In this situation, Sinkhorn's algorithm becomes inapplicable since it is specific to entropic regularization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal in this paper is, first, to obtain better than stateof-the-art complexity bounds for approximating the OT distance and, second, propose a flexible algorithm for solving the OT problem with different types of regularization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Approximating the OT distance amounts to solving the OT 2 This is done for simplicity and all the results easily generalize to the case of measures with different support size. where X is transportation plan, C ∈ R n × n + is a given ground cost matrix, r, c ∈ R n are given vectors from the probability simplex ∆ n, 1 is the vector of all ones. The regularized OT problem is where γ > 0 is the regularization parameter and R (X) is a strongly convex regularizer, e.g. negative entropy or squared Euclidean norm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal is to find X ∈ U (r, c) such that In this case, 〈 C, ̂ X 〉 is an ε -approximation for the OT distance and X is an approximation for the transportation plan.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

̂ Related work. We focus on the general case with C being a non-negative dense matrix. In this case, is a linear programming problem with best theoretical complexity ˜ O ( n 5 / 2 ) and best practical complexity ˜ O ( n 3 ), which is problematic when n is larger than 10 3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural alternative is to approximate by with a small γ. Starting with the work, the widely used practical implementation of this idea is to use entropy regularization, i.e. solve, where R ( X ) is negative entropy of a matrix X. The special structure of this problem allows to use the balancing algorithm also known as Sinkhorn's algorithm and RAS. The best known complexity bound in the literature for this approach is ˜ O ( n 2 ε 3 ) to obtain, Theorem 1. They also show that the regularization parameter should be chosen proportional to ε, which necessitates working with the matrix exp( -C/ε ) and leads to problems with numerical stability of the algorithm. Several ways to overcome this instability issue were proposed, but with limited theoretical analysis. While the entropy-regularized OT problem allows to use other matrix-scaling algorithms such as with theoretical guarantees, the authors do not provide any experimental results, so the practical implementability of these algorithms is questionable. In, stochastic gradient descent is applied to solve the entropy-regularized OT problem, but the complexity for approximating OT distance in the sense of is not studied.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In any case, Sinkhorn's and other mentioned algorithms are very specific to entropic regularization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

| ALGORITHM | RATES | LS | ENTR. | A flexible alternative can be to use some general purpose optimization method to solve, which is a particular case of a minimization problem with linear constraints. When n is large, the natural choice is the class of first-order methods, e.g. Conjugate Gradients (CG), quasi-Newton methods like L-BFGS or Nesterov's accelerated gradient descent (AGD). Due to the presence of linear constraints, the most common approach involves the construction of the Lagrange dual problem, which is an unconstrained problem. Based on the latter fact, L-BFGS was used in for the dual problem. Since our focus is on complexity analysis, it is crucial to estimate the rate of convergence for the norm of the dual problem objective gradient as this norm is exactly the equality constraints feasibility in the primal problem. This can be complicated if CG or LBFGS is used for the dual problem, so we choose AGD-type methods with primal-dual updates. The tricky part of this approach is to prove accelerated convergence rates separately for the primal objective residual and linear constraints feasibility.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, first-order methods use the Lipschitz constant of the objective's gradient to define the stepsize. The theoretical value for this constant is usually an overestimation and leads to small stepsize and slow convergence in practice. Thus, an algorithm should use a line-search strategy to adapt to the local value of this constant and converge faster. Finally, entropy regularization in is an important particular case and an algorithm should be able to deal with this non-Lipschitz-smooth regularizer. We analyzed a bunch of algorithms in the literature (see Table 1) and none of them combine all three described features, namely, a) accelerated convergence rates separately for the primal objective and constraints feasibility, b) line-search, c) entropy friendliness.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

3 Their algorithm uses Lipschitz constant in the stopping crite- Our contributions can be summarized as follows.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Improved analysis of the Sinkhorn's algorithm and complexity ˜ O (n 2 ε 2) arithmetic operations for approximating the OT distance in the sense of. - Improved complexity ˜ O (min { n 9 / 4 ε, n 2 ε 2 }) arithmetic operations for approximating the OT distance in the sense of, based on our APDAGD method. - An Adaptive Primal-Dual Accelerated Gradient Descent (APDAGD) algorithm, which incorporates a linesearch strategy and has accelerated convergence rates separately for the primal objective and constraints 4 feasibility in with a general strongly convex regularizer. - Numerical illustration of the practical performance of these algorithms for approximating the OT distance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

For a matrix A and a vector a, we denote e A, e a, ln A, ln a their entrywise exponents and natural logarithms respectively. For a vector a ∈ R n, we denote by ‖ a ‖ 1 the sum of absolute values of its elements, and by ‖ a ‖ 2 its Euclidean norm, and by ‖ a ‖ ∞ the maximum absolute value of its elements. Given a matrix A ∈ R n × n, we denote by vec(A) the vector in R n 2, which is obtained from A by writing its columns one below another. For a matrix A ∈ R n × n, we denote ‖ A ‖ 1 = ‖ vec(A) ‖ 1 and ‖ A ‖ ∞ = ‖ vec(A) ‖ ∞. Further, we define the entropy of a matrix X ∈ R n × n + by For two matrices A,B, we denote their Frobenius inner product by 〈 A,B 〉. We denote by ∆ n:= { a ∈ R n +: a T 1 = 1 } the probability simplex in R n.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

For p, q ∈ ∆ n, we define the Kullback-Leibler divergence between p and q to be 4 Amore general adaptive primal-dual method, which can solve problems both with linear equality and inequality constraints can be found. rion and, hence, is not completely adaptive.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sinkhorn's Algorithm", "weight": 1.0} -->

In this section, our goal is to refine the complexity analysis of the Sinkhorn's algorithm, then, based on this analysis, improve the existing complexity bound O ( n 2 ‖ C ‖ 3 ∞ log n ε 3 ) for approximating the OT distance in the sense of and obtain new complexity O ( n 2 ‖ C ‖ 2 ∞ log n ε 2 ).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

We consider the Sinkhorn-Knopp algorithm listed as Algorithm 1, which solves, Lemma 2, the minimization problem To improve the complexity of the Sinkhorn's algorithm, first, we obtain some bounds for the iterates u k, v k and an optimal solution (u ∗, v ∗). Then, using these bounds, for each iteration of the algorithm, we upper bound the objective value ψ (u k, v k) by ‖ B (u k, v k) 1 -r ‖ 1 + ‖ B (u k, v k) T 1 -c ‖ 1. Finally, the latter bound is used, to prove the main theorem of this subsection with new complexity result for the Sinkhorn's algorithm. where K:= e -C/γ and B (u, v):= diag (e u) K diag (e v), diag(a) being the diagonal matrix with the vector a on the diagonal. Problem is equivalent to the dual to with a particular choice R (X) = -H (X), see the derivation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

The following lemma provides the bounds for u k, v k, u ∗ and v ∗.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

Lemma 1. Let k ≥ 0 and u k, v k be generated by Algorithm 1 and (u ∗, v ∗) be a solution of. Then Proof. First, we prove the bound for u k. Obviously, the stated inequality holds for k = 0. Let k -1 be even. Then the variable u is updated on the iteration k -1 and B (u k, v k) 1 = r by the algorithm construction. Hence, for each i ∈ [1, n], we have On the other hand, since K ij ≤ 1, for each i ∈ [1, n], and min i u i k ≥ min i ln (r i 〈 1, e v k 〉) = ln (min i r i 〈 1, e v k 〉).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

The latter inequality and give Since the next iteration k, which is odd, updates the variable v and leaves the variable u unchanged, the obtained bound for u k holds for any k ≥ 0. The bound in for v k is proved in the same way. Finally, since (u ∗, v ∗) is an optimal solution of, the gradient of the objective in vanishes at this point. Hence, B (u ∗, v ∗) 1 = r and B (u ∗, v ∗) T 1 = c. Using these equalities and repeating the same arguments as in the proof of bounds for u k and v k, we prove the bounds for u ∗ and v ∗.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

The following lemma, for each iteration of Algorithm 1, relates the objective ψ (u k, v k) in and ‖ B (u k, v k) 1 -r ‖ 1 + ‖ B (u k, v k) T 1 -c ‖ 1. To simplify derivations, we define Lemma 2. Let k ≥ 1 and u k, v k be generated by Algorithm 1. Then, denoting B k:= B (u k, v k), we have Proof. Let us fix k ≥ 1 and consider the convex function of (ˆ u, ˆ v) Since its gradient vanishes at (ˆ u, ˆ v) = (u k, v k), the point (u k, v k) is its minimizer. Hence, Next, we bound the r.h.s. of this inequality.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

Since, on each iteration of the Sinkhorn's algorithm, either B k 1 = r, or B T k 1 = c, we have that 〈 1, B k 1 〉 = 1 and 〈 1, B k 1 -r 〉 = 0. Taking a = max i u i k +min i u i k 2, by H¨ older's inequality and Lemma 1, we obtain Using the same arguments, we bound 〈-u ∗, B k 1 -r 〉, 〈 v k, B T k 1 -c 〉 and 〈-v ∗, B T k 1 -c 〉 in and finish the proof of the lemma.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

Now we are ready to improve the iteration complexity bound for the Sinkhorn's algorithm.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

Theorem 1. Algorithm 1 outputs a matrix B (u k, v k) satisfying ‖ B (u k, v k) 1 -r ‖ 1 + ‖ B (u k, v k) T 1 -c ‖ 1 ≤ ε ′ in the number of iterations k satisfying Proof. Assume that k ≥ 1 is even. As before, we denote B k = B (u k, v k). Since 〈 1, B k 1 〉 = 〈 1, B k +1 1 〉 = 1 and v k +1 = v k, we have By Pinsker's inequality and Lemma 2, since B T k 1 = c, we obtain where we also used that, as soon as the stopping criterion is not yet fulfilled and B T k 1 = c, ‖ B k 1 -r ‖ 2 1 ≥ (ε ′) 2. The same inequality can be proved for the case of odd k.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

Therefore, §2.1.5, for any k ≥ 1, To combine the two estimates and, we consider a switching strategy, parametrized by number s ∈ (0, ˜ ψ (u 1, v 1)]. First, using, we estimate the number of iterations to reduce ˜ ψ (u, v) from ˜ ψ (u 1, v 1) to s. Then, using, we estimate the number of iterations to reduce ˜ ψ (u, v) from s to zero, keeping in mind that ˜ ψ (u, v) ≥ 0 by its definition. Minimizing the sum of these two estimates in s ∈ (0, ˜ ψ (u 1, v 1)], we conclude that the total number of iterations k satisfies In both cases, we have 4 R.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Improved Complexity of the Sinkhorn's Algorithm", "weight": 1.0} -->

The main innovation of our proof is the first component in the max in r.h.s. of, which follows from Lemma 2. On the contrary, (see also ) prove only the bound with the second component and, thus, obtain worse estimate for the number of Sinkhorn's iterations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Complexity of OT Distance by Sinkhorn", "weight": 1.0} -->

Now we apply the result of the previous subsection to derive a complexity estimate for finding ̂ X ∈ U ( r, c ) satisfying. The procedure for approximating the OT distance by the Sinkhorn's algorithm is listed as Algorithm 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Complexity of OT Distance by Sinkhorn", "weight": 1.0} -->

Theorem 2. Algorithm 2 outputs ̂ X ∈ U (r, c) satisfying in Before we prove the theorem, we compare our result with the best known in the literature, which is given, Theorem 1: O (n 2 ‖ C ‖ 3 ∞ ln n ε 3). As we see, our result has better dependence on ε and ‖ C ‖ ∞.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm 2 Approximate OT by Sinkhorn", "weight": 1.0} -->

- 3: Calculate B by Algorithm 1 with marginals ˜ r, ˜ c and accuracy ε ′ / 2. - 4: Find ̂ X as the projection of B on U (r, c) by Algorithm 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm 2 Approximate OT by Sinkhorn", "weight": 1.0} -->

Proof of Theorem 2. Following the same steps as in the proof of Theorem 1, we obtain

<!-- chunk {"id": "body-0035", "role": "body", "section": "Output: ̂ X", "weight": 1.0} -->

where ̂ X is the output of Algorithm 2, X ∗ is a solution to the OT problem, and B is the matrix obtained in step 3 of this Algorithm 2. At the same time, we have Setting γ = ε 4 ln n and ε ′ = ε 8 ‖ C ‖ ∞, we obtain from the above inequality and that X satisfies inequality.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Output: ̂ X", "weight": 1.0} -->

̂ It remains to estimate the complexity of Algorithm 2. By Theorem 1, when ε ′ is sufficiently small, the number of iterations of the Sinkhorn's algorithm in step 3 of Algorithm 2 is O (R ε ′), where, according to and, Since γ = ε 4 ln n and ε ′ = ε 8 ‖ C ‖ ∞, we obtain that R = O (‖ C ‖ ∞ ln n ε). Inserting this into the estimate k = O (R ε ′), we obtain that the total number of Sinkhorn's algorithm iterations is bounded by O (‖ C ‖ 2 ∞ ln n ε 2). Obviously, ˜ r and ˜ c in step 2 of Algorithm 2 can be found in O (n) time. Since each iteration of the Sinkhorn's algorithm requires O (n 2) arithmetic operations, the total complexity of Algorithm 2 is O (n 2 ‖ C ‖ 2 ∞ ln n ε 2).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Output: ̂ X", "weight": 1.0} -->

Note that, as a byproduct, we obtained a theoretical justification of a commonly used in practice heuristic trick of changing zero values of measures r, c to some small positive values.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Accelerated Gradient Descent", "weight": 1.0} -->

In this section, our goal is to propose a flexible algorithm for solving the regularized OT problem with a general strongly convex regularizer and, based on this algorithm, obtain a complexity bound ˜ O ( min { n 9 / 4 ε, n 2 ε 2 }) for approximating the OT distance in the sense of. To achieve this goal, we consider a general optimization problem, of which is a particular case, and provide an Adaptive Primal-Dual Accelerated Gradient Descent (APDAGD) method for this problem together with its convergence rate. Finally, we apply this algorithm to the entropy-regularized OT problem and obtain the desired complexity.

<!-- chunk {"id": "body-0039", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

In this subsection, we consider the optimization problem where E is a finite-dimensional real vector space, Q is a simple closed convex set, A is a given linear operator from E to some finite-dimensional real vector space H, b ∈ H is given, f (x) is a γ -strongly convex function on Q with respect to some chosen norm ‖ · ‖ E on E.

<!-- chunk {"id": "body-0040", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

The Lagrange dual problem, written as a minimization problem, is Note that ∇ ϕ (λ) = b -Ax (λ) is Lipschitz-continuous where x (λ):= arg min x ∈ Q (-f (x) -〈 A T λ, x 〉) and L ≤ ‖ A ‖ 2 E → H γ. This estimate can be pessimistic and our algorithm does not use it and adapts automatically to the local value of the Lipschitz constant.

<!-- chunk {"id": "body-0041", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

We assume that the dual problem has a solution and there exists some R > 0 such that ‖ λ ∗ ‖ 2 ≤ R < + ∞, where λ ∗ is the solution to with minimum value of ‖ λ ∗ ‖ 2. Note that the algorithm does not need any estimate of R and the value R is used only in the convergence analysis.

<!-- chunk {"id": "body-0042", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

This algorithm can be considered as a primal-dual extension of accelerated mirror descent. The difference to the literature consists in incorporating linesearch and an online stopping criterion based only on the duality gap and constraints infeasibility. We provide a more detailed discussion in the supplementary material. Gradient methods for non-convex problems with line-search can be found.

<!-- chunk {"id": "body-0043", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

Algorithm 3 Adaptive Primal-Dual Accelerated Gradient Descent (APDAGD) Input: Accuracy ε f, ε eq > 0, initial estimate L 0 s.t. 0 < L 0 < 2 L.

<!-- chunk {"id": "body-0044", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

- 2: repeat { Main iterate } Theorem 3. Assume that the objective in the primal problem is γ -strongly convex and that the dual solution λ ∗ satisfies ‖ λ ∗ ‖ 2 ≤ R. Then, for k ≥ 1, the points ˆ x k, η k in Algorithm 3 satisfy where x ∗ and f ∗ are respectively an optimal solution and the optimal value. Moreover, the stopping criterion in step 11 is correctly defined.

<!-- chunk {"id": "body-0045", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

A stronger statement of the theorem and its proof can be found in the supplementary material.

<!-- chunk {"id": "body-0046", "role": "body", "section": "General Problem and Algorithm", "weight": 1.0} -->

Note that APDAGD is indeed flexible. For the case of entropy regularization, we set f ( X ) = 〈 C, X 〉 -γH ( X ) and immediately get an algorithm to solve since -H ( X ) is strongly convex w.r.t. ‖ · ‖ 1. For the case of Euclidean norm regularization, we set f ( X ) = 〈 C, X 〉 + γ ‖ X ‖ 2 2 and obtain strong convexity w.r.t. the Euclidean norm. Other strongly convex regularizes are also suitable.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Complexity of OT Distance by APDAGD", "weight": 1.0} -->

Now we apply the result of the previous subsection to derive a complexity estimate for finding ̂ X ∈ U ( r, c ) satisfying

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

| Input: Accuracy ε. | Input: Accuracy ε. |. We use entropic regularization of problem and consider the regularized problem with the regularizer R (X) = -H (X), where H (X) is given. We define E = R n 2, ‖ · ‖ E = ‖ · ‖ 1, and variable x = vec(X) ∈ R n 2 to be the vector obtained from a matrix X by writing each column of X below the previous column. Also we set f (x) = 〈 C, X 〉 -γH (X), Q = R n 2 +, b T = (r T, c T) and A: R n 2 → R 2 n defined by the identity (A vec(X)) T = ((X 1) T, (X T 1) T). With this setting, we solve problem by our APDAGD. Let ̂ X k be defined by identity vec(̂ X k) = ˆ x k, where ˆ x k is generated by APDAGD.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

We also define ̂ X ∈ U (r, c) to be the projection of ̂ X k onto U (r, c) constructed by Algorithm 2. The pseudocode of our procedure for approximating the OT distance is listed as Algorithm 4.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

Theorem 4. Algorithm 4 outputs ̂ X ∈ U (r, c) satisfying in Before we prove the theorem, we compare our result with the best known in the literature, which is given, Theorem 1: O (n 2 ‖ C ‖ 3 ∞ ln n ε 3). As we see, our result in has much better dependence on ε and ‖ C ‖ ∞, which comes for a reasonable price of n 1 / 4. We also underline that the complexity obtained with the accelerated gradient descent Algorithm 4 has better dependence on ε and ‖ C ‖ ∞ than our improved bound for the Sinkhorn's algorithm given in Theorem 2: O (n 2 ‖ C ‖ 2 ∞ ln n ε 2).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

Importantly, similarly to the Sinkhorn's algorithm, our APDAGD algorithm can be parallelized, and efficiently implemented when the Sinkhorn kernel matrix exp( -C/γ ) is easy to apply, e.g. the measures are supported on regular grids and C is given by squared Euclidean distance. See the supplementary material for the details.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

Proof of Theorem 4. Let X ∗ be the solution of the OT problem and X ∗ γ be the solution of the regularized problem. Then, we have Now we estimate the second and third term in the r.h.s. Since, for any X ∈ U (r, c), -H (X) ∈ [-2 ln n, 0], we have Further, since APDAGD solves problem with f (x) = 〈 C, X 〉 -γH (X) and X ∗ γ is the solution, we have where we used again that -H (X) ∈ [-2 ln n, 0] for X ∈ U (r, c). Combining, and, we obtain We immediately see that, when the stopping criterion in step 5 of Algorithm 4 is fulfilled, the output ̂ X ∈ U (r, c) satisfies.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

It remains to obtain the complexity bound. First, we estimate the number of iterations in Algorithm 4 to guarantee 〈 C, ̂ X -̂ X k 〉 ≤ ε 6 and, after that, estimate the number of iterations to guarantee f (ˆ x k) + ϕ (η k) ≤ ε 6. By H¨ older's inequality, we have 〈 C, ̂ X -̂ X k 〉 ≤ ‖ C ‖ ∞ ‖ ̂ X -̂ X k ‖ 1. By Lemma 7, Next, we obtain two estimates for the r.h.s of this inequality. First, by the definition of the operator A and vector b, Here we used the choice of the norm ‖ · ‖ 1 in E = R n 2 and the norm ‖ · ‖ 2 in H = R 2 n. Indeed, in this setting ‖ A ‖ E → H = ‖ A ‖ 1 → 2 and this norm is equal to the maximum Euclidean norm of a column of A. By definition, each column of A contains only two non-zero elements, which are equal to one. Hence, ‖ A ‖ 1 → 2 = √ 2.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

Second, since X ∗ γ ∈ U (r, c), we have and a similar estimate for ‖ ̂ X T k 1 -c ‖ 1. Combining these estimates with and an estimate for ‖ A ‖ E → H, we obtain Combining, and, we obtain Setting γ = ε 3 ln n, we have that, to obtain 〈 C, X -X k 〉 ≤ ε 6, it is sufficient to choose At the same time, since ‖ A ‖ E → H = √ 2, Since we set γ = ε 3 ln n, we conclude that in order to obtain f (ˆ x k) + ϕ (η k) ≤ ε 6, it is sufficient to choose To estimate the total number of iterations, we should take maximum of and. Normalizing the cost matrix C, we can set ‖ C ‖ ∞ = 1. At the same time, as one can see, the change of the dual variables u → u + t 1, v → v -t 1, for any t ∈ R does not change the value of the dual objective. Thus, without loss of generality, we can set R ≤ 1. Hence, the maximum of and is attained.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm 4 Approximate OT by APDAGD", "weight": 1.0} -->

Since each iteration of APDAGD uses only operations with matrices of the size n × n and vectors of the size 2 n, each iteration requires O ( n 2 ) arithmetic operations. At the same time, according to Lemma 7, the complexity of projecting ̂ X k on U ( r, c ) by their Algorithm 2 is O ( n 2 ). Thus, to obtain the total complexity of Algorithm 4 as in the Theorem statement, we just multiply by n 2.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we provide an empirical illustration of the work of Algorithm 2 and Algorithm 4. We run experiments on randomly chosen real images from the MNIST dataset. By default, this dataset contains images of handwritten digits of the size 28 by 28 pixels. To understand the dependence on the number of pixels n, we resize MNIST images to be images of 28 · s by 28 · s pixels, where s is an integer. We change all the zero elements in the measures, representing these images, to 10 -6 and, then, normalize them, so that they sum up to one. As we show in the proof of Theorem 2, small perturbations of the vectors r and c (see step 2 of Alg. 2) do not influence much the theoretical guarantees for the Sinkhorn's algorithm approach. By similar arguments, these changes do not influence much the APDAGD approach. We run Algorithm 2 until the stopping criterion ‖ B 1 -r ‖ 1 + ‖ B T 1 -c ‖ 1 ≤ ε 8 ‖ C ‖ ∞ is fulfilled.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

As we can see from the proof of Theorem 4, the inequality f (ˆ x k )+ ϕ ( η k ) ≤ ε 6 is fulfilled faster than 〈 C, ̂ X -̂ X k 〉 ≤ ε 6. Thus, we run Algorithm 4 until the latter inequality is fulfilled. To understand the dependence on ε, we choose several values of accuracy ε ∈ [0. 025, 0. 12] and s = 1. For each value, we randomly choose 10 pairs of images, run Algorithm 2 and Algorithm 4, and average the results. It is worth noting that, in practice, the working time of Algorithm 2 is approximately proportional to 1 ε. The reason could be in a pessimistic theoretical bound R in Lemma 1. Figure 1 (left) illustrates the working time of two algorithms for different ε. To understand the dependence on n, we choose accuracy ε = 0. 1 and several values of s ∈. For each value, we randomly choose 5 pairs of images, run Algorithm 2 and Algorithm 4, and average the results. Figure 1 (right) illustrates the working time of two algorithms for different n.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We analyze two algorithms for approximating the general OT distances between two discrete distributions. Our first algorithm is based on the entropic regularization of the OT problem and Sinkhorn's algorithm. We prove the complexity bound ˜ O ( n 2 ε 2 ) arithmetic operations. The second algorithm is based on the entropic regularization of the OT problem and our novel Adaptive Primal-Dual Accelerated Gradient method. We obtain the complexity ˜ O ( min { n 9 / 4 ε, n 2 ε 2 }) arithmetic operations for this algorithm. Both complexity bounds are better than the state-of-the-art result given by ˜ O ( n 2 ε 3 ). Our APDAGD can be of a separate interest for solving strongly convex problems with linear constraints, since it is not specific to the entropic regularization, incorporates a line-search strategy and has an accelerated rate of convergence.
