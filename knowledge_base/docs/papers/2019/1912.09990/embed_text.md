<!-- arxiv-full-text:v1 {"arxiv_id": "1912.09990", "source": "arxiv-pdf"} -->

## Introduction

We will develop controllers for linear systems with time-varying parametric uncertainty, which may cover a wide range of system classes extensively studied in the literature. For example, we obtain Linear Parameter Varying (LPV) systems when the disturbance is observable at each time step, Linear Difference Inclusions (LDIs) when it is unknown but norm-bounded and stochastic systems with multiplicative noise when it varies stochastically.

In many practical applications, however, the distribution of the disturbance is not known. These traditional control approaches either make a boundedness assumption on the disturbance or on its moments, which allows for a fully robust approach. Such approaches, however, disregard any statistical information that may be obtained on the distribution of the disturbances. Our aim, instead, is to design linear controllers which use sampled data to improve performance over fully robust approaches, while inheriting many of the system-theoretical guarantees of a robust control strategy. To this end, we adopt a distributionally robust (DR) approach towards solving the infinite-horizon Linear Quadratic Regulator (LQR) problem, where we minimize the expected cost for the worst-case distribution in a so-called ambiguity set computed based on the available data such that it contains the true distribution with high probability. Such a DR approach addresses most of the difficulties associated with learning automatically, since the ambiguity set directly models the uncertainty in the sample-based estimates against which the controllers will be robust. Similar techniques were recently studied in Schuurmans et al. for stochastic jump linear systems and in Dean et al. for deterministic systems, where the system matrices A and B are learned from data.

The work of Gravell et al. also deals with learning control of linear systems with multiplicative noise, albeit from a different perspective. They employ a policy gradient algorithm, which requires the initial guess for the control gain to be stabilizing. By contrast, obtaining such a controller is the main goal of our approach.

Our main contributions are summarized as follows. Leveraging recent results from high dimensional statistics, we provide practical high-probability confidence bounds for the ambiguity sets, which depend only on known quantities (Section 3). We then extend the solution of the ( nominal ) infinite horizon LQR problem with known distribution to related DR counterparts which account for the ambiguity on the disturbance distribution. Whenever the mean of the disturbance is known, we show that the DR problem is equivalent to a semidefinite program (SDP) which has the same form as the nominal one. Next, we extend the formulation to the setting in which both the mean and the covariance are only known to lie in an ellipsoidal ambiguity set (Section 4.2), for which we can only approximate the optimal controller.

## Notation

Let I R denote the reals, I N the naturals and I N + = I N \ { 0 }. For symmetric matrices P, Q we write P ≻ Q ( P ⪰ Q ) to signify that P -Q is positive (semi)definite and denote by ⊗ the Kronecker product. We assume that all random variables are defined on a probability space (Ω, F, P ), with Ω the sample space, F its associated σ -algebra and P the probability measure. Let y: Ω → I R n be a random vector defined on (Ω, F, P ). With some abuse of notation we will write y ∈ R n to state the dimension of this random vector. Let P y denote the distribution of y, i.e., P y ( A ) = P [ y ∈ A ]. Then, a trajectory { y i } N i =1 of identically and independently distributed ( i.i.d. ) copies of y is defined by the distribution it induces. That is, for any A 0,..., A N ∈ F we define P y 0,...,y N ( A 0 × · · · × A N ):= P [ y 0 ∈ A 0 ∧ · · · ∧ y N ∈ A N ] = ∏ N i =0 P y ( A i ). This definition can be extended to infinite trajectories { y i } i ∈ I N by Kolmogorov's existence theorem Billingsley. We will write the expectation operator as I E. We denote by I E [ y | z ] the conditional expectation with respect to z. Let M denote the set of probability measures defined on (I R n w, B ), with B the Borel σ -algebra of I R n w.

## Problem statement

Consider the stochastic discrete-time system with input- and state-multiplicative noise given :

## Nominal stochastic LQR problem and solution

The primary goal is to solve the following LQR problem: where we assume that Q ≻ 0 and R ≻ 0. The solution of will yield a controller that renders the closed-loop system exponentially stable in the mean square sense, which is defined as follows.

Definition 1 ((Exponential) Mean Square Stability) We say that an autonomous system x k +1 = A ( w k ) x k is mean square stable ( m.s.s. ) iff I E [ x ⊤ k x k ] → 0 as k → ∞. It is exponentially mean square stable ( e.m.s.s. ) iff there exists a pair of positive constants γ ∈ and c such that I E [ x ⊤ k x k ] ≤ cγ k ‖ x 0 ‖ for all k ∈ I N and for each x 0 ∈ I R n x.

This property can be verified using the classical Lyapunov operator: Theorem 2 (Lyapunov stability) For the autonomous system x k +1 = A (w k) x k the following statements are then equivalent: (i) it is m.s.s., (ii) it is e.m.s.s., (iii) ∃ P ≻ 0: Proof See Appendix A.1.

The LQR problem has been studied for many variations of. The following proposition is then similar to many classical results in literature: Proposition 3 Consider a system with dynamics and the associated LQR problem. Assuming that is mean square stabilizable, i.e., there exists a K and P ≻ 0 such that holds for the closed-loop system x k +1 = (A (w k) + B (w k) K) x k, then the following statements hold.

I The optimal solution of is given by K ∞ = -(R + G (P ∞)) -1 H (P ∞), with P ∞ the solution of the following Riccati equation: III The solution of the Riccati equation is found by solving the following SDP: II The controller K ∞ stabilizes in the mean square sense.

Proof See Appendix A.2.

Notice that the optimal solution to the LQR problem depends solely on the first and second moment of the random disturbance. This motivates our choice for the parametric form of the ambiguity set used in the data-driven LQR problem, which we state in the next section.

## Data-driven stochastic LQR problem

Consider now the case where P w is not known a priori and only a finite set of offline i.i.d. samples { ˆ w } M -1 i =0 is available. For clarity, we add a hat to imply that a random variable depends on these samples. It is apparent that under such circumstances, it is only possible to solve approximately. For most applications, however, it is crucial that the approximate solution remains stabilizing, which is not trivial. For instance, the empirical approach, where is solved using ˆ µ:= 1 M ∑ M -1 i =0 ˆ w i and ˆ Σ:= 1 M ∑ M -1 i =0 ( ˆ w i -ˆ µ )( ˆ w i -ˆ µ ) ⊤, does not guarantee stability. We will illustrate this with an example, which motivates the methodology presented in this paper.

## Example 1 (Motivating example) Consider the following scalar system,

where x k ∈ I R, u k ∈ I R and w k ∈ I R are defined as before, but now w is assumed Gaussian with I E[w] = 0 and I E[w 2] = σ 2 = 0. 5. The empirical variance is ˆ σ 2 = 1 M ∑ M -1 i =0 ˆ w 2 i, using i.i.d. samples { ˆ w i } M -1 i =0. We will develop an optimal LQR controller with a stage cost given by qx 2 k + ru 2 k = x 2 k +10 4 u 2 k. Using the results from Proposition 3 to derive the Riccati equation, we obtain Note that this is a quadratic equation in p with the following positive solution: where we used r ≫ q and assumed that ˆ σ 2 > 0. 4375 and ˆ σ 2 < 1. If the lower bound is not satisfied it turns out that the optimal feedback gain is given by ˆ K ∗ ≈ 0. The optimal linear controller associated with this solution is given: The closed-loop system given this controller is mean square stable iff (0. 75+ ˆ K ∗) 2 +0. 5(ˆ K ∗) 2 < 1, which follows from the recursive expression for the variance of the state in closed-loop: Solving this stability condition for ˆ K ∗ leads to the conclusion that the system is mean square stable iff -1. 4571 < ˆ K ∗ < -0. 0429. Filling in results in a condition on ˆ σ 2: 0. 4697 < ˆ σ 2 < 1. 5303. Note that ˆ σ 2 > 1 implies that the system is not stabilizable (this is related to the uncertainty threshold principle of Athans et al.), so we only consider the lower bound on ˆ σ 2 (which is larger than 0. 4375 from our earlier assumption). In fact, we can now evaluate the probability that the empirical approach provides an unstable closed-loop controller as with ˆ ξ i = ˆ w i / σ ∼ N and which corresponds to the cumulative distribution function of a χ 2 -distributed random variable with M degrees of freedom, since we assumed that w is Gaussian. Evaluating this probability numerically, we find that with M = 500, there is a probability of 0. 1693 that the empirical approach provides an unstable closed-loop controller.

From this example, it is clear that underestimation of the variance of the disturbance is directly related to the probability of failure of the controller. In order to take this into account, we introduce an arbitrarily-chosen confidence level β ∈ and a corresponding ambiguity set ˆ A: Ω ⇒ M, which represents the uncertainty of estimators ˆ µ and ˆ Σ. The size of A is then determined such that P (P w ∈ ˆ A) ≥ 1 -β. In particular, we parametrize A as first suggested by Delage and Ye: ∣ The values of r µ (β) and r Σ (β) such that P (P w ∈ ˆ A) ≥ 1 -β are derived in Section 3. In Section 4, the following DR counterpart of is solved where { v k } k ∈ I N is a trajectory of i.i.d. copies of v. In doing so, we can finally establish m.s.s. of the data-driven controller with high probability, by virtue of the following generalization of Theorem 2 to the DR case.

Theorem 4 (DR Lyapunov stability) Consider the matrices { ˆ A i } n w i =0, the set { w k } k ∈ I N consisting of i.i.d. copies of a square integrable random vector w and the autonomous system x k +1 = ˆ A (w k) x k, with ˆ A (w) = ∑ M i =1 ˆ A i w (i). Say that we have an ambiguity set with P (P w ∈ ˆ A) ≥ 1 -β, with P w the true distribution of w. Then if there exists a P ≻ 0 such that: the autonomous system is e.m.s.s. with probability at least 1 -β.

Proof See Appendix B.1.

## Data-driven ambiguity set estimation

Wenow turn to the problem of estimating the parameters r Σ ( β ) and r µ ( β ) involved in the definition of the ambiguity set, given that we have M i.i.d. draws from the true distribution. These parameters will be estimated under the following assumption on the disturbances.

Definition 5 (Sub-Gaussianity) A random variable y is sub-Gaussian with variance proxy σ 2 if I E[y] = 0 and its moment generating function satisfies We denote this by y ∼ subG (σ 2). We say that a random vector ξ ∈ I R n w is sub-Gaussian, or ξ ∼ subG n w (σ 2), if z ⊤ ξ ∼ subG (σ 2), ∀ z ∈ I R n w with ‖ z ‖ 2 = 1.

Assumption 1 We assume that (i) w is square integrable; (ii) { w k } k ∈ I N are i.i.d. copies of w; (iii) Σ ≻ 0; and (iv) Σ -1 / 2 ( w k -µ ) ∼ subG n w ( σ 2 ) for some σ ≥ 1.

Note that in the specific case of Gaussian disturbances, Assumption 1(iv) holds with σ 2 = 1, so no further prior knowledge on the distribution is required. Moreover, in this case the bound on the covariance obtained in Theorem 6 can be slightly improved. In the case of bounded disturbances, σ 2 can be estimated in a data-driven fashion.

For the moment, we restrict our attention to obtaining concentration inequalities for moment estimators of random vectors with zero mean and unit variance - hereafter referred to as isotropic random vectors. We will then convert these results into ambiguity sets of the form using arguments from Delage and Ye; So. We begin by specializing the isotropic covariance bound, derived with constants in based on a result by Litvak et al. and the isotropic mean bound .

Theorem 6 (Isotropic covariance bound) Let ξ ∼ subG n w (σ 2) be a random vector, with I E[ξ] = 0, I E[ξξ ⊤] = I n w. Let { ˆ ξ i } M -1 i =0 be M independent copies of ξ and ˆ I:= 1 M ∑ M -1 i =0 ˆ ξ i ˆ ξ ⊤ i. Then where ϵ ∈ (0, 1 / 2) is chosen freely and q (β, ϵ, n w):= n w log (1 + 1 / ϵ) + log (2 / β).

Theorem 7 (Isotropic mean bound) Let { ˆ ξ i } M -1 i =0 be as defined in Theorem 6, and ˆ ζ:= 1 M ∑ M -1 i =0 ˆ ξ i. Then P [ ‖ ˆ ζ ‖ 2 2 ≤ t µ ( β )] ≥ 1 -β.

By combining the bounds in Theorems 6 and 7, we readily obtain the following result.

Theorem 8 (Ambiguity set) Let w ∈ I R n w be a sub-Gaussian random vector, with I E[w] = µ, I E[(w -µ)(w -µ) ⊤] = Σ and ξ = Σ -1 / 2 (w -µ) ∼ subG n w (σ 2). Let { ˆ w i } M -1 i =0 be independent copies of w. Let ˆ µ:= 1 M ∑ M -1 i =0 ˆ w i and ˆ Σ:= 1 M ∑ M -1 i =0 (ˆ w i -ˆ µ)(ˆ w i -ˆ µ) ⊤ denote the empirical estimators for the mean and the covariance matrix, respectively. Let ϵ, p (β, n w), q (β, ϵ, n w), t Σ (β / 2) and t µ (β / 2) be as defined in Theorems 6 and 7. Provided that then with probability at least 1 -β, Proof Let us define ξ = Σ -1 / 2 (w -µ) ∼ subG n w (σ 2) so that Let ˆ ζ = 1 M ∑ M -1 i =0 ˆ ξ i and ˆ I = 1 M ∑ M -1 i =0 ˆ ξ i ˆ ξ ⊤ i. By Theorems 6 and 7, we then have with probability 1 -β that, Let us define the covariance estimator with respect to the true mean by ˜ Σ:= 1 M ∑ M -1 i =0 (ˆ w i -µ)(ˆ w i -µ) ⊤ = 1 M ∑ M -1 i =0 (Σ 1 / 2 ξ i)(Σ 1 / 2 ξ i) ⊤ = Σ 1 / 2 ˆ I Σ 1 / 2. Therefore, we can rewrite (13a) in terms of the anisotropic random variable w as where we have used and the fact that condition implies t Σ (β / 2) < 1. As shown, (13b) implies that for any x ∈ I R n w, I nw Using this fact, we can bound ˜ Σ with respect to ˆ Σ and Σ as where we used in the final step. Combining this, we have that (1 -t Σ)Σ ⪯ ˆ Σ+ t µ Σ, thus Condition 12 then follows from assuming 1 -t µ -t Σ > 0, which is a quadratic inequality in √ M.

## Distributionally Robust LQR

We will tackle the solution of for the ambiguity set given in in two stages. Firstly, we extend the result of Proposition 3 to the case where µ is known and Σ is estimated, i.e., r µ ( β ) = 0 and r Σ ( β ) > 0. Secondly, we present the result where both the mean and the covariance are estimated.

## Uncertain covariance

The case where the mean is known is interesting since we can still formulate an exact solution to. This will no longer be true for the full-uncertainty case (Section 4.2).

Proposition 9 Consider that v ∈ I R n w is distributed according to an element of the set where P (P w ∈ ˆ A Σ) ≥ 1 -β. Then applying Proposition 3 with Σ = r Σ (β) ˆ Σ results in the optimal linear controller, assuming that is DR mean square stabilizable, i.e., there exists a K such that the DR Lyapunov decrease holds for the closed-loop system x k +1 = (A (w k)+ B (w k) K) x k. The optimal controller is also mean square stabilizing for with probability at least 1 -β.

Proof See Appendix B.2.

## Full uncertainty

We finally consider the more general case using the full ambiguity set ˆ A given. The general min-max problem for such sets is computationally intractable, which is why an upper bound on the quadratic cost is minimized instead by employing results from robust control. A common approach is to assume that the value function can be written in the quadratic form V (x) = x ⊤ Px for some P ≻ 0 and to solve the optimization problem where we introduced the random initial state ˜ x ∈ I R n x. The optimal cost of then upper bounds the true LQR cost of for a given value of ¯ x as proven in Kothare et al. for a similar setup. We can then write as an SDP using the following theorem.

Theorem 10 Let ˆ A be an ambiguity set of the form. Then we can find an approximate solution of for the system, assuming that the initial state is given by the random vector ˜ x ∈ I R n x with I E [˜ x] = 0 and I E [˜ x ˜ x ⊤] = I n x, by solving the following SDP. where H i = ∑ n w j =1 [ˆ Σ 1 / 2] ji (A j W + B j V), ˆ A = A (ˆ µ), ˆ B = B (ˆ µ), ˆ Σ dr = r Σ (β) ˆ Σ. Let ˆ W and ˆ V denote the minimizers of. The corresponding linear controller u = ˆ Kx with ˆ K = ˆ V ˆ W -1 then achieves an upper bound of the cost, given by I E[˜ x ⊤ ˆ P ˜ x], where ˆ P = ˆ W -1. Moreover, ˆ K is mean-square stabilizing for with probability at least 1 -β.

Proof See Appendix B.3.

Remark 11 Two approximations are made in Theorem 10. First, leveraging, introducing an approximation error quantified by an increase of r µ (β) by a factor of at most √ n w. Secondly, we minimize an upper-bound of the LQR cost instead of the cost itself. We can further decrease the closed-loop cost by instead using a receding horizon controller for a given ¯ x, which too can be formulated as an SDP. Then is reformulated as: where (20a) can be replaced by a linear matrix inequality using Schur's complement. The assumption used in Theorem 10 ensures that the solution converges to the optimal one as r µ (β) and r Σ (β) go to zero.

Remark 12 Invertibility of r Σ ( β ) ˆ Σ can be guaranteed by using r Σ ( β ) ˆ Σ+ λI instead of r Σ ( β ) ˆ Σ for some small λ, which increasing the size of the ambiguity set, introducing additional conservatism.

## Numerical Experiment

We experimentally quantify the sample complexity of our approach, i.e., how many samples are needed before the controller becomes equivalent to the nominal one based on the true Σ and µ instead of their data-driven estimates. Consider the double integrator model with matrices: where we chose T s = 0. 02. The dynamics are then given by with w k an independent random sequence of Gaussian random vectors with covariance Σ = and mean µ =.

The simulation setup is as follows. We compare the nominal controller, the uncertain covariance controller (Proposition 9) and the full uncertainty controller (Theorem 10). We evaluate the expected closed-loop cost for ¯ x = ⊤ by solving the Lyapunov equation. We start with M = 1000 to satisfy. For each value of M we produce 30 realisations of both DR controllers. Figure 1 depicts confidence intervals for relative difference between closed-loop cost of the DR controllers and the nominal controller ( i.e., the relative suboptimality). The figure shows that both converge with a rate O (1 /M ) to the nominal cost even though Theorem 10 only solves approximately.

To estimate the sample complexity, we determine controllers satisfying for Q = and R = 0. 01. The parameters of the ambiguity set are determined using Theorem 8 with β = 0. 05 and ϵ = 1 / 30. Since w k are Gaussian, ξ k = Σ -1 / 2 ( w k -µ ) are sub-Gaussian with σ 2 = 1.

## Conclusion and future work

We studied the infinite horizon LQR problem for systems with multiplicative uncertainty on both the states and the inputs. We operate in the setting where the distributions are estimated from data. We show that using results from high-dimensional statistics, high-confidence ambiguity sets can be constructed, which allow us to formulate a DR counterpart to the stochastic optimal control problem as an SDP. As a result, stability of the closed-loop system can be guaranteed with high probability.

In future work, we aim to perform an in-depth analysis of the conservatism introduced by the proposed formulations. Furthermore, we plan to study extensions towards DR Kalman filtering.
