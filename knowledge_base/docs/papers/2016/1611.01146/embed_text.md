<!-- arxiv-full-text:v1 {"arxiv_id": "1611.01146", "source": "arxiv-pdf"} -->

## Introduction

Finding a global minimizer of a non-convex optimization problem is NP-hard. Thus, the standard goal of efficient non-convex optimization algorithms is instead to find a local minimum. This problem has become increasingly important as the state-of-the-art in machine learning is attained by non-convex models, many of which are variants of deep neural networks. Experiments in suggest that fast convergence to a local minimum is sufficient for training neural nets, while convergence to critical points (points with vanishing gradients) is not. Theoretical works have also affirmed the same phenomenon for other machine learning problems (see and the references therein).

In this paper we give a provable linear-time algorithm for finding an approximate local minimum in smooth non-convex optimization. It applies to a general setting of machine learning optimization, and in particular to the optimization problem of training deep neural networks. Furthermore, the running time bound of our algorithm is the fastest known even for the more lenient task of computing a point with vanishing gradient (called a critical point), for a wide range of parameters.

Formally, the problem of unconstrained mathematical optimization is stated in general terms as that of finding the minimum value that a function attains over Euclidean space, i.e.

If f is convex, the above formulation is convex optimization and is solvable in (randomized) polynomial time even if only a valuation oracle to f is provided. A crucial property of convex functions is that 'local optimality implies global optimality', allowing for greedy algorithms to reach the global optimum efficiently. Unfortunately, this is no longer the case if f is nonconvex; indeed, even a degree four polynomial can be NP-hard to optimize, or even just to check whether a point is not a local minimum. Thus, for non-convex optimization one has to settle for the more modest goal of reaching approximate local optimality efficiently.

Note that a particular interest to machine learning is the optimization of functions f: R d ↦→ R of the finite-sum form Such functions arise when minimizing loss over a training set, where each example i in the set corresponds to one loss function f i in the summation.

We say that the function f is second-order smooth if it has Lipschitz continuous gradient and Lipschitz continuous Hessian. We say that a point x is an ε -approximate local minimum if it satisfies (following the tradition of): where ‖ · ‖ denotes the Euclidean norm of a vector. We say that a point x is an ε -critical point if it satisfies the gradient condition above, but not necessarily the second-order condition. Critical points include saddle points in addition to local minima. We remark that ε -approximate local minima (even with ε = 0) are not necessarily close to any local minimum, neither in domain nor in function value. However, if we assume in addition the function satisfies the (robust) strict-saddle property (see Section 2 for the precise definition), then an ε -approximate local minimum is guaranteed to be close to a local minimum for sufficiently small ε.

Our main theorem below states the time required for the proposed algorithm FastCubic to find an ε -approximate local minimum for second-order smooth functions.

Theorem (informal). Ignoring smoothness parameters, the running time of FastCubic to return an ε -approximate local minimum is Above, T h is the time to compute Hessian-vector product for ∇ 2 f (x) and T h, 1 is that for an arbitrary ∇ 2 f i (x).

The full statement of Theorem 1 can be found in Section 2.

Hessian-vector products can be computed in linear time -meaning T h, 1 = O (d) and T h = O (nd)- for many machine learning problems such as generalized linear models and training neural networks. We explain this more generally in Appendix A. Therefore, Corollary 1.1. Algorithm FastCubic returns an ε -approximate local minimum for the optimization problem of training a neural network in time Another important aspect of our algorithm is that even in terms of just reaching an ε -critical point, i.e. a point that satisfies ‖∇ f (x) ‖ ≤ ε without any second-order guarantee, FastCubic is faster than all previous results (see Table 1 for a comparison).

The fastest methods to find critical points for a smooth non-convex function are gradient descent and its extensions, jointly known as first-order methods. These methods are extremely efficient in terms of per-iteration complexity; however, they necessarily suffer from a 1 /ε 2 convergence rate, to the best of our knowledge, in previous results only higher-order methods seem capable of breaking this 1 /ε 2 bottleneck. For certain ranges of parameters, our FastCubic fi nds local minima even faster than first-order methods, even though they only find critical points. This is depicted in Table 1.

Table 1: Comparison of known methods.

| Paper | Total Time Achieving ‖∇ f (x) ‖ | Second-Order Guarantee | a Here C 1, C 2 are two constants that are not explicitly written. We believe C 1 ≥ 4.

## Related work

Methods that Provably Reach Critical Points. Recall that only a gradient oracle is needed to reach a critical point. The most commonly used algorithm in practice for training non-convex learning machines such as deep neural networks is stochastic gradient descent (SGD), also known as stochastic approximation and its derivatives. Some practical enhancements widely used in practice are based on Nesterov's acceleration and adaptive regularization. The variance reduction technique, introduced , was extremely successful in convex optimization, but only recently there was a non-convex counterpart with theoretical benefits introduced.

Methods that Provably Reach Local Minima. The recent work of Ge et al. showed that a noise-injected version of SGD in fact converges to local minima instead of critical points, as long as the underlying non-convex function is strict-saddle. Their theoretical running time is a large polynomial in the dimension and not competitive with our method (see Table 1).

The work of Lee et al. shows that gradient descent, starting from a random point, almost surely converges to a local minimum of a strict-saddle function. The rates of convergence and precise step-sizes that are required are, however, yet unknown.

If second-order information (i.e., the Hessian oracle) is provided, the cubic-regularization method of Nesterov and Polyak converges in O ( 1 ε 3 / 2 ) iterations. However, each iteration of NesterovPolyak requires solving a cubic function which, in general, takes time super-linear in the input representation.

One natural direction is to apply an approximate trust region solver, such as the linear-time solver of, to approximately solve the cubic regularization subroutine of Nesterov-Polyak. However, the approximation needed by a naive calculation makes this approach even slower than vanilla gradient descent. Our main challenge is to obtain approximate second-order local-minima and simultaneously improve upon gradient descent.

Independently of this paper and concurrently 1, Carmon et al. develop an accelerated gradient descent method that achieves the same running time for finding an approximate local minimum as in our paper. Remarkably, the same running time is obtained via a very different technique.

## Our Techniques

Our algorithm is based on the cubic regularization method of Nesterov and Polyak. At a high level, cubic regularization states that if we can minimize a cubic function m ( h ) ≜ g ⊤ h + 1 2 h ⊤ H h + L 6 ‖ h ‖ 3 exactly, where g = ∇ f ( x ), H = ∇ 2 f ( x ), and L is the second-order smoothness of the function f, then we can iteratively perform updates x ′ ← x + h, and this algorithm converges to an ε -approximate local minimum in O (1 /ε 3 / 2 ) iterations. Unfortunately, solving this cubic minimization problem exactly, to the best of our knowledge, requires a running time of O ( d ω ) where ω is the matrix multiplication constant. Getting around this requires five observations.

The fi rst observation is that, minimizing m ( h ) up to a constant multiplicative approximation (plus a few other constraints) is sufficient for showing an iteration complexity of O (1 /ε 3 / 2 ). 2 The proof techniques to show this observation are based on extending Nesterov and Polyak.

The second observation is that the minimizer h ∗ of m ( h ) must be of the form h ∗ = ( H + λ ∗ I ) + g + v, where λ ∗ ≥ 0 is some constant satisfying H + λ ∗ I ⪰ 0, and v is the smallest eigenvector of H and + denotes the pseudo-inverse of a matrix. This can be viewed as moving in a mixture direction between choosing h ← v, and choosing h to follow a shifted Newton's direction h ← ( H + λ ∗ I ) + g. Intuitively, we wish to reduce both the computation of ( H + λ ∗ I ) + g and v to Hessian-vector products.

1 To be precise, their manuscript appeared online approximately 24 hours before ours.

2 More specifically, we need m t ( h ) ≤ 1 C min h { m t ( h ) } for some constant C. In addition, we need to have good bounds on ‖ h ‖ and ‖∇ m ( h ) ‖.

The first task of computing ( H + λ ∗ I ) + g can be slow, and even if H + λ ∗ I is strictly positivedefinite, computing it has a complexity depending on the (possibly huge) condition number of H + λ ∗ I. The third observation is that it suffices to pick some λ ′ > λ ∗ so both the condition number of H + λ ′ I is small and the vectors ( H + λ ∗ I ) -1 g and ( H + λ ′ I ) -1 g are close. This relies on the structure of m ( h ).

The second task of computing v has a complexity depending on 1 / √ δ where δ is the target additive error. The fourth observation is that the choice δ = √ ε suffices for the outer loop of cubic regularization to make sufficient progress. This reduces the complexity to compute v.

Finally, finding the correct value λ ∗ itself is as hard as minimizing m t ( h ). The fi fth step is to design an iterative scheme that makes only logarithmic number of guesses on λ ∗. This procedure either finds the correct one (via binary search), or finds an approximate one, λ ′, but satisfying ( H + λ ∗ I ) -1 g and ( H + λ ′ I ) -1 g being sufficiently close.

Putting all the observations together, and balancing all the parameters, we can obtain a cubic minimization subroutine (see FastCubicMin in Algorithm 2) that runs in time O ( nd + n 3 / 4 d/ε 1 / 4 ).

## Preliminaries and Main Theorem

We use ‖ · ‖ to denote the Euclidean norm of a vector and the spectral norm of a matrix. For a symmetric matrix M we denote by λ max ( M ) and λ min ( M ) respectively the maximum and minimum eigenvalues of M. We denote by A ⪰ B that A -B is positive semidefinite (PSD). For a PSD matrix M, we denote by M + its pseudo-inverse if M is not strictly positive definite.

We make the following Lipschitz continuity assumptions for the gradient and Hessian of the target function f. Namely, there exist L 2, L > 0 such that Definition 2.1. We assume the following complexity parameters on the access to f (x):

- Let T g ∈ R ∗ be the time complexity to compute ∇ f ( x ) for any x ∈ R d.

· Let T h ∈ R ∗ be the time complexity to compute ( ∇ 2 f ( x ) ) v for any x, v ∈ R d. Definition 2.2. We say that f is of finite-sum form if f = 1 n ∑ n i =1 f i ( x ) and ‖∇ 2 f i ( x ) ‖ ≤ L 2 for each i ∈ [ n ]. In this case, we define T h, 1 to be the time complexity to compute ( ∇ 2 f i ( x ) ) v for arbitrary x, v ∈ R d and i ∈ [ n ].

Next we define the strict-saddle function for which an ε -approximate local minimum is almost equivalent to a local minimum.

Definition 2.3 (strict saddle). Suppose f (·): R d → R is twice differentiable. For α, β, γ ≥ 0, we say f is (α, β, γ) -strict saddle if every x ∈ R d satisfies at least one of the following three conditions:. 3. There exists a local minimum x ⋆ that is γ -close to x in Euclidean distance.

We see that if a function is ( α, β, γ )-strict saddle, then for ε < min { α, β 2 } an ε -approximate local minimum is γ -close to some local minimum.

## Algorithm 1 FastCubic ( f, x 0, ε, L, L 2 )

Input: f ( x ) that satisfies (2.1) with L 2 and L; a starting vector x 0; a target accuracy ε. 1: κ ← ( 900 εL ) 1 / 2.

- 5: h ′ ← either v or λv min 2 L whichever gives smaller value for m t ( h );

## Main Results

The finite-sum setting captures much of supervised learning, including Neural Networks and Generalized Linear Models. The main theorem which we show in our paper is as follows: Theorem 1. FastCubic (Algorithm 1) starts from a point x 0 and outputs a point x such that in total time (denoting by D ≜ f (x 0) -f (x ∗)) Here ˜ O hides logarithmic factors in L, L 2, 1 /ε, d, and in max x { ‖∇ f (x) ‖ }.

- ˜ O ( D √ L ε 3 / 2 · ( T g + n T h, 1 ) + Dn 3 / 4 L 1 / 4 √ L 2 ε 7 / 4 · T h, 1 ) in the finite-sum setting (see Definition 2.2).

Two Known Subroutines. Our running time of FastCubic relies on the following recent results for approximate matrix inverse and approximate PCA: Theorem 2.4 (Approximate Matrix Inverse). Suppose matrix M ∈ R d × d satisfies ‖ M ‖ ≤ L 2 and λ I + M ⪰ δ I for constants λ, δ, L 2 > 0. Let κ ≜ λ + L 2 δ. Then, we can compute vector x satisfying Moreover, suppose M = 1 n ∑ n i =1 M i where each M i is symmetric and satisfies ‖ M i ‖ ≤ L 2. If M i b can be computed in time O (d ′) for each i and vector b, then accelerated SVRG computes a vector x that satisfies equation (2.2) in time O (max { n, n 3 / 4 κ 1 / 2 } · d ′ · log 2 (κ/ε)).

∥ ∥ x -( λ I + M ) -1 b ∥ ∥ ≤ ε ‖ b ‖, (2.2) using Accelerated gradient descent (AGD) in O ( κ 1 / 2 log( κ/ε ) ) iterations, each requiring O ( d ) time plus the time needed to multiply M with a vector.

We refer to the running time for this computation as T inverse ( κ, ε ) and the algorithm as A.

Above, the SVRG based running time shall be used only towards our finite-sum case in Definition 2.2.

Theorem 2.5 (AppxPCA ). Let M ∈ R d × d be a symmetric matrix with eigenvalues 1 ≥ λ 1 ≥ · · · ≥ λ d ≥ 0. With probability at least 1 -p, AppxPCA produces a unit vector w satisfying w ⊤ Mw ≥ (1 -δ × )(1 -ε ) λ max ( M ). The total running time is ˜ O ( T inverse (1 /δ ×, εδ × )).

## Our Fast Cubic Regularization Algorithm

Recall that the cubic regularization method of Nesterov and Polyak studies the following upper bound on the change in objective value as we move from a point x t to x t + h: (it follows simply ⋄ c is a constant; we proved c = 2. 4 ∗ 10 6 works from the Taylor series truncated to the third order) Denote by h ∗ an arbitrary minimizer of m t (h). Wepropose in this paper a subroutine FastCubicMin to minimizes m t (h) approximately. Note that FastCubicMin returns two vectors v and v min. We then choose h ′ to be either v or λv min 2 L, whichever gives a smaller value for m t (h).

Before discussing the details of FastCubicMin, let us first state a main theorem for FastCubicMin: 3 Theorem 2 (Guarantees of FastCubicMin). The algorithm FastCubicMin fi nds a vector h ′ that satisfies (a) It produces a vector h ′ satisfying m t (h ′) ≤ 0 and

- (c) FastCubicMin runs in time: (using ˜ O to hide logarithmic factors in L, L 2, 1 /ε, d, ‖∇ f (x t) ‖) - ˜ O (max { n, n 3 / 4 √ L 2 (εL) 1 / 4 } · T h, 1) where T h, 1 is the time to multiply ∇ 2 f i (x t) with a vector. - ˜ O (√ L 2 (εL) 1 / 4 · T h) where T h is the time to multiply ∇ 2 f (x t) to a vector; Above, the first guarantee promises that we are either done (because m t (h ∗) is close to zero), or we obtain a 1 / 3000 multiplicative approximation to m t (h ∗). Our second guarantee in Theorem 2 promises that when we are done (because m t (h ∗) is close to zero), the output vector h ′ and h ∗ are roughly similar in Euclidean norm and have a small gradient ‖∇ m t (h ′) ‖. Our third guarantee gives the time complexity of FastCubicMin.

Now, our final algorithm FastCubic for finding the ε -approximate local minimum of f ( x ) is included in Algorithm 1. It simply iteratively calls FastCubicMin to find an approximate minimizer, and it then stops whenever m t ( h ′ ) > -ε 3 / 2 c √ L for some large constant c.

Roadmap. In Section 4 we show why Theorem 2 implies Theorem 1. All the remaining sections are for the purpose of proving Theorem 2. Because our FastCubicMin is very technical, instead of stating what the algorithm is right away, we decide to take a different path. In Section 5, we first state a lemma characterizing 'what h ∗ looks like'. In Section 6, we provide a set of sufficient conditions which 'look similar' to the characterization of h ∗, and show that as long as these conditions are met, Theorem 2-a and 2-b follow easily. Finally, in Section 7, we state FastCubicMin and explain why it satisfies these sufficient conditions and why it runs in the aforementioned time.

## Theorem 2 implies Theorem 1

In this section, we show that Theorem 2 implies Theorem 1. It relies on the following lemma (proved in Appendix B) regarding the sufficient condition for us to reach an ε -approximate local minimum.

3 To present the simplest result, we have not tried to improve the constant dependency in this paper.

Lemma 4.1. If m t (h ∗) ≥ -ε 3 / 2 800 √ L and h ′ is an approximate minimizer of m t (h) satisfying then we have that ‖∇ f (x t + h ′) ‖ ≤ ε and λ min (∇ 2 f (x t + h ′)) ≥ -√ Lε.

Proof of Theorem 1 from Theorem 2. When FastCubic terminates, we have m t ( h ′ ) > -ε 3 / 2 c √ L; therefore, it satisfies m t ( h ∗ ) ≥ -ε 3 / 2 800 √ L according to Theorem 2-a. Combining this with Theorem 2-b and Corollary 4.1, we conclude that in the last iteration of FastCubic, our output satisfies ‖∇ f ( x t + h ′ ) ‖ ≤ ε and λ ( 2 f ( x + h )) √ Lε. This finishes the proof with respect to the accuracy conditions.

As for the running time, in every iteration except for the last one, FastCubic satisfies m t ( h ) ≤ -Ω ( -ε 3 / 2 √ L ). Therefore by (3.1), we must have decreased the objective by at least Ω ( -ε 3 / 2 √ L ) in this round, and this cannot happen for more than O ( ( f ( x 0 ) -f ∗ ) √ L ε 3 / 2 ) iterations. The final running time of FastCubic follows from this bound together with Theorem 2-c.

Therefore, in the rest of the paper it suffices to study FastCubicMin and prove Theorem 2.

## Characterization Lemma of the Minimizer h ∗

For notational simplicity in this and the subsequent sections we focus on the following problem: where H is a symmetric matrix with ‖ H ‖ 2 ≤ L 2.

Recall from the previous section that we have denoted by h ∗ an arbitrary minimizer of m (h). We have the following lemma which characterizes h ∗: (a variant of this lemma has appeared, and we prove it in the appendix for the sake of completeness) Lemma 5.1. We have h ∗ is a minimizer of m (h) if and only if there exists λ ∗ ≥ 0 such that The objective value in this case is given by The following corollary comes from Lemma 5.1 and its proof: Corollary 5.2. The value λ ∗ in Lemma 5.1 is unique, and for every λ satisfying H + λ I ≻ 0, we have In the above characterization, we have a crude upper bound on λ ∗: Proof. We have L ‖ (H + B I) -1 g ‖ ≤ L ‖ g ‖ λ min (H + B I) ≤ L ‖ g ‖ B -L 2 < 2 B and therefore λ ∗ ≤ B due to Corollary 5.2.

Proposition 5.3. We have λ ∗ ≤ B ≜ max { 2 L 2 + √ L ‖ g ‖, 1 } with λ ∗ defined in Lemma 5.1.

## Sufficient Conditions for Theorem 2-a and 2-b

Without worrying about the design of FastCubicMin at this moment, let us first state a set of sufficient conditions under which the assumptions in Theorem 2-a can be satisfied.

Main Lemma 1. Consider an algorithm that outputs a real λ ∈ [0, 2 B], a vector v ∈ R d, and a unit vector v min ∈ R d. Additionally, suppose numbers κ, ˜ ε ≥ 0 satisfying the following conditions: Moreover, suppose that the outputs (λ, v, v min) satisfy one of the following two cases: Case 2: The following conditions are satisfied: Then, at least one of the two choices h ′ ∈ v, λv min 2 L satisfy Let us compare such sufficient conditions to the characterization Lemma 5.1.

- In Case 1, up to a very small error ˜ ε, we have essentially found a vector v that satisfies v ≈ -(H + λ I) -1 g and ‖ v ‖ ≈ 2 λ L. Therefore, this v should be close to h ∗ for obvious reason. (This is the simple case.) - In Case 2, we have only found a vector v that satisfies v ≈ -(H + λ I) -1 g and ‖ v ‖ ≲ 2 λ L. In this case, we also compute an approximate lowest eigenvector v min of λ min (H) up to an additive 1 / 10 κ accuracy (see case 2-c). We will make sure that, as long as the conditions in 2-a hold, then either v or λv min 2 L will be an approximate minimizer for m t (h).

(This is the hard case.)

Proof of Main Lemma 1. We first consider Case 1. According to Corollary 5.2, if ˜ ε = 0 then v is a minimizer of m (h). The following claim extends this argument to the setting when ˜ ε > 0: From the above lemma it follows that either m (h ∗) ≥ -8 κ 3 L 2 otherwise m (h ∗) ≥ 1. 1 m (v) which satisfies the conditions of the theorem.

We now consider Case 2, and in this case we make the following two claims: Lemma 1 now follows from the two claims because we can output the vector h ′ which has the lowest value of m (h ′) amongst the two choices h ′ ∈ { v, λ v min 2 d }. This satisfies either m (h ∗) ≥ 3000 m (h ′) or m (h ∗) ≥ -32 κ 3 L 2.

The missing proofs of the three claims are deferred to Appendix D.

The next main lemma shows that, under the same sufficient conditions as Main Lemma 1, we also have that Theorem 2-b holds. (Its proof is contained in Appendix E.)

Main Lemma 2. In the same setting as Main Lemma 1, suppose m ( h ∗ ) ≥ -ε 3 / 2 300 √ L. Then the output vector v satisfies the following conditions:

## Main Algorithms for Theorem 2

We are now ready to state our main algorithm FastCubicMin and sketch why it satisfies the sufficient conditions in Main Lemma 1. As described in Algorithm 2, our algorithm starts with a very large choice λ 0 ← 2 B and decreases it gradually. At each iteration i, it computes an approximate inverse v satisfying ‖ v + ( H + λ i I ) -1 g ‖ ≤ ˜ ε with respect to the current λ i. Then there are three cases, depending on whether L ‖ v ‖ is approximately equal to, larger than, or smaller than 2 λ i. At a high level, if it is 'equal', then we have met Case 1 in Main Lemma 1; if it is 'larger', then we can binary search the correct value of λ ∗ in the interval [ λ i, λ i -1 ]; and if it is 'smaller', then we need to compute an approximate eigenvector and carefully choose the next point λ i +1.

We state our main lemma below regarding the correctness and running time of FastCubicMin.

Main Lemma 3. FastCubicMin in Algorithm 2 outputs a real λ ∈ [0, 2 B ], a vector v ∈ R d, and a unit vector v min ∈ R d satisfying one of the two sufficient conditions in Main Lemma 1. We also have that the procedure can be implemented in a total running time of

- ˜ O ( √ κL 2 · T h ) if Accelerated Gradient Descent is used in Theorem 2.4 to invert matrices. · ˜ O ( max { n, n 3 / 4 √ κL 2 }· T h, 1 ) if we use accelerated SVRG as the subprocedure A in Theorem 2.4. Here ˜ O hides logarithmic factors in L, L 2, κ, d, B.

Weprove the correctness half of Main Lemma 3, and defer its running time analysis to Appendix G.

## Correctness Half of Main Lemma 3

We will now establish the correctness of our algorithm. We first observe that the BinarySearch subroutine returns ( λ, v, ∅ ) that satisfies Case 1 of Main Lemma 1.

Fact 7.1. BinarySearch outputs a pair λ and v such that Proof. The latter is guaranteed by line 3 in BinarySearch, and the former is implied by the latter because We also establish the following invariants regarding the values λ i. (Proof in Appendix F.)

Lemma 7.2. The following statements hold for all i until FastCubicMin terminates

- (c) λ i +1 + λ min (H) ≤ 3 4 (λ i + λ min (H)) unless λ i +1 = 0 Moreover when FastCubicMin terminates at Line 20 we have λ i + λ min (H) ≤ 1 κ.

Wenow prove the output ( λ, v, v min ) of FastCubicMin satisfies the sufficient conditions of Main Lemma 1.

## Algorithm 2 FastCubicMin ( g, H, L, L 2, κ ) (main algorithm for cubic minimization)

Input: g a vector, H a symmetric matrix, parameters κ, L and L 2 which satisfies -L 2 I ⪯ H ⪯ L 2 I. Output: ( λ, v, v min ) 1: B ← L 2 + √ L ‖ g ‖ + 1 κ. 2: ˜ ε ← 1 / ( 10000 ( max { L, ‖ g ‖, 3 κ 10, B, 1 }) 20 ) 3: λ 0 ← 2 B. 4: for i = 0 to ∞ do 5: Compute v such that ‖ v +( H + λ i I ) -1 g ‖ ≤ ˜ ε. 6: if L ‖ v ‖ ∈ [2 λ i -L ˜ ε, 2 λ i + L ˜ ε ] then 7: return ( λ i, v, ∅ ). 8: else if L ‖ v ‖ > 2 λ i + L ˜ ε then 9: return BinarySearch ( λ 1 = λ i -1, λ 2 = λ i, ˜ ε ). 10: else if L ‖ v ‖ < 2 λ i -L ˜ ε then 11: Let Power Method find vector w that is 9 / 10-appx leading eigenvector of ( H + λ i I ) -1: 9 10 λ max (( H + λ i I ) -1 ) ≤ w ⊤ ( H + λ i I ) -1 w ≤ λ max (( H + λ i I ) -1 ). 12: Compute a vector ˜ w such that ‖ ˜ w -( H + λ i I ) -1 w ‖ ≤ ˆ ε ≜ 1 60 B. 13: ∆ ← 1 2 1 ˜ w ⊤ w -ˆ ε. 14: if ∆ > 1 2 κ then 15: ˜ λ i +1 ← λ i -∆ 2. 16: if ˜ λ i +1 > 0 then λ i +1 ← ˜ λ i +1 else λ i +1 ← 0 17: else 18: Use AppxPCA to find any unit vector v min such that v ⊤ min H v min ≤ λ min ( H ) + 1 10 κ. 19: Flip the sign of v min so that g ⊤ v min ≤ 0. 20: return ( λ i, v, v min ). 21: end if 22: end if 23: end for

## Algorithm 3 BinarySearch ( λ 1, λ 2, ˜ ε ) (binary search subroutine)

Input: λ 1 ≥ λ 2, L ‖ (H + λ 1 I) -1 g ‖ ≤ 2 λ 1, L ‖ (H + λ 2 I) -1 g ‖ ≥ 2 λ 2, λ 2 + λ min (H) > 0 Output: (λ, v, ∅) 1: for t = 1 to ∞ do 2: λ mid ← λ 1 + λ 2 2 3: Compute vector v such that ‖ v +(H + λ mid I) -1 g ‖ ≤ ˜ ε/ 2 4: if L ‖ v ‖ ∈ [2 λ mid -L ˜ ε, 2 λ mid + L ˜ ε] then 5: return (λ mid, v, ∅) 6: else if L ‖ v ‖ + L ˜ ε ≤ 2 λ mid then 7: λ 1 ← λ mid 8: else if L ‖ v ‖ -L ˜ ε ≥ 2 λ mid then 9: λ 2 ← λ mid 10: end if 11: end for Correctness Proof of Main Lemma 3. We carefully verify these sufficient conditions:

- λ i + λ min (H) ≥ 3 10 κ from Lemma 7.2 implies ‖ (H + λ i I) -1 ‖ ≤ 4 κ. It is now immediate that the choice of ˜ ε on Line 2 satisfies the Condition (6.1) in the assumption of Main Lemma 1. - Since ˜ ε ≤ 1 10 κL and λ i + λ min (H) ≥ 3 10 κ it follows that (H +(λ i -L ˜ ε) I) -1 ≻ 0 which proves Condition (6.2) in Main Lemma 1. - We now verify Case 1 and 2 in the assumption of Main Lemma 1. At the beginning of the algorithm, our choice λ 0 = 2 B ensures (using Proposition 5.3) that L ‖ (H + λ 0 I) -1 g ‖ < 2 λ 0. Let us now consider the various places where the algorithm outputs: - -If FastCubicMin terminates at Line 7, then we have ‖ v +(H + λ i I) -1 g ‖ ≤ ˜ ε and additionally L ‖ (H + λ i I) -1 g ‖ ∈ [L ‖ v ‖ -L ˜ ε, L ‖ v ‖ + L ˜ ε] ⊆ [2 λ i -2 L ˜ ε, 2 λ i +2 L ˜ ε]. Therefore, the output meets Case 1 requirement of Main Lemma 1 with λ = λ i. - -If FastCubicMin terminates at Line 9, then L ‖ (H + λ i I) -1 g ‖ > L ‖ v ‖ -L ˜ ε ≥ 2 λ i. Obviously, we must have i ≥ 1 in this case because L ‖ (H + λ 0 I) -1 g ‖ < 2 λ 0. Therefore, Line 10 must have been reached at the previous iteration, so it implies L ‖ (H + λ i -1 I) -1 g ‖ < 2 λ i -1. Together, these two imply that we can call BinarySearch with (λ i -1, λ i). Owing to Fact 7.1, the subroutine outputs a pair (λ, v) satisfying the Case 1 requirement of Main Lemma 1. - -If FastCubicMin terminates on Line 20, we verify that Case 2 of Main Lemma 1 with λ = λ i holds. We first have In sum, we have verified that all the assumptions of Main Lemma 1 hold.

By Corollary 5.2, we also have that λ i ≥ λ ∗. Lemma 7.2 tells us λ i satisfies λ i + λ min ( H ) ≤ 1 κ. Vector v satisfies ‖ v +( H + λ i I ) -1 g ‖ ≤ ˜ ε. Vector v min satisfies v ⊤ min H v min ≤ λ min ( H ) + 1 10 κ.

Final Proof of Theorem 2. Theorem 2 is a direct corollary of our main lemmas. Main Lemma 3 ensures that the assumptions of Main Lemma 1 and Main Lemma 2 both hold. Now, using the special choice of κ in FastCubic, Theorem 2-a immediately comes from Main Lemma 1; Theorem 2-b immediately comes from Main Lemma 2; and Theorem 2-c immediately comes from Main Lemma 3. This finishes the proof of Theorem 2.
