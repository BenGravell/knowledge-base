<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Topological Properties of the Set of Stabilizing Feedback Gains

Topics include SISO, Continuous time, Discrete-time, LTI, Output feedback.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work presents a fairly complete account on various topological and metrical aspects of feedback stabilization for single-input-single-output (SISO) continuous and discrete time linear-time-invariant (LTI) systems. In particular, we prove that the set of stabilizing output feedback gains for a SISO system with n states has at most lceiln/2rceil connected components. Furthermore, our analysis yields an algorithm for determining intervals of stabilizing gains for general continuous and discrete LIT systems; the proposed algorithm also computes the number of unstable roots in each unstable interval. Along the way, we also make a number of observations on the set of stabilizing state feedback gains for MIMO systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In classical control, topological and metrical properties of stabilizing feedback gains are of paramount importance for the stability analysis and stabilization of LIT systems -. Recently, such properties have received renewed interest in system literature as they have direct implications for adopting learning algorithms for control design. This is particularly the case in the so-called direct policy algorithms, where it is of interest to directly adjust the control gain-without an explicit system identification step-say, using a gradient step. The design objectives in these scenarios are typically functions over direct policies-often desired to be stabilizing feedback gains. For example, in reinforcement learning, the policy gradient updates the feedback iteratively to get desired optimal controller. In this case, the cost functions are defined on the set of stabilizing controllers (assuming +∞ elsewhere). 1 As such, understanding the topological and metrical properties of this set provides valuable insights in designing learning algorithms for dynamic systems. In the meantime, such insights can also reveal fundamental shortcomings in certain optimization algorithms. For example, if the set of stabilizing feedback gains has several path-connected components, the solutions of gradient-type learning algorithms will be highly dependent on the initialization process.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

It is thus surprising that despite the long historical interest in characterizing the set of stabilizing feedback gains, research works on its set-theoretic and topological properties are rather limited. This is potentially due to significantly more interest in characterizing the set of 'certificates" for stabilizing controllers, e.g., in terms of linear matrix inequalities.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The authors are with the University of Washington; Emails: bu+amesbahi+mesbahi@uw.edu 1 In this paper, we will use 'feedback controllers' interchangeably with static feedback gains as 'dynamic' controllers are not considered.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Of particular relevance to our work in directly characterizing stabilizing feedback gains is that of Ohara and colleagues, who examined its differential geometric structure for multipleinput-multiple-output (MIMO) systems. In and, an elegant geometric approach has been adopted to parametrize the set of stabilizing feedback gains; in particular, it has been shown that for continuous and discrete single-input-singleoutput (SISO) and dyadic systems the corresponding sets can be bounded via two and three hyperplanes. Furthermore, the work of Ober has shown that the set of stable SISO systems of order n have n + 1 connected components in the Euclidean topology while the set of stable MIMO systems is connected. The work reported in focuses on the connectedness of this set for both SISO and MIMO systems. We note that both works examine continuous-time systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper discusses the topological, metrical, and geometric properties of the set of stabilizing controllers for both continuous and discrete-time LTI systems. We show that the set of stabilizing state-feedback gains for a continuous SISO system is regular open, unbounded, in general nonconvex, and path-connected in the Euclidean topology. In the meantime, the set of stabilizing output-feedback controllers is shown to be open but not connected in general, and can be bounded or unbounded. It recent works, based on the implicit assumption that stable and unstable intervals of the feedback gain interlace, it has been stated that the set of stabilizing output feedback controllers for SISO systems can have at most n (in) and ⌈ n 2 ⌉ (in) connected components. If this assumption does not hold, however, the line of reasoning reported, lead to the upper bounds of 2 n and n, respectively. 2 In this work, we prove a tight bound of ⌈ n 2 ⌉ for continuous as well as discrete time LTI systems; all of our results are constructive (they lead to algorithms for characterizing these sets) and rely on basic topology and analytic theory of polynomials,.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

3 The separate treatment for continuous and discrete time systems is warranted; in fact, in contrast to the folklore expectation of unified properties for continuous and discrete time systems, there are counterexamples to show that the analogies between the two are far from complete,. The distinct difference between continuous and discrete LTI systems might be due to the fact that the generalized bilinear transform has poles and thus not continuous,. Therefore, generalizing the proposed topological properties of the set of stabilizing feedback gains from continuous LTI systems to discrete ones is not straightforward. Nevertheless, in this paper we show that the set of stabilizing state feedback gains for discrete-time LTI SISO systems enjoys some of the topological properties as its continuous counterpart, i.e., open and pathconnected in Euclidean topology and nonconvexity. But in contrast to the continuous case, the set of stabilizing state feedback gains is bounded. For output feedback SISO systems, the corresponding set of stabilizing gains is open, bounded and in general nonconvex, but is no longer path-connected.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Accordingly, we prove that the set can have at most ⌈ n 2 ⌉ path-connected components, which is a tight bound supported by simulation results. The present work also proposes an algorithm for determining the intervals of stabilizing feedback gains for general continuous and discrete LIT systems. This algorithm also computes the number of unstable roots in each unstable interval.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

2 In discussions with authors of, it has been pointed out that a perturbation type argument can help address this issue; the approach adopted in this work is direct and leads to a constructive algorithm for characterizing the stabilizing and unstabilizing intervals.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

3 Thus the emphasis on the SISO case; some of these results have been extended to MIMO case.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The paper is organized as follows. In §II, we introduce the notation and the preliminary background; §III §IV are devoted to set-theoretic properties of Hurwitz and Schur stabilizing feedback gains, respectively, followed by numerical examples. Our results are intermingled with observations and remarks that further provide insights into some of the geometric and topological intricacies of feedback stabilization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROPERTIES OF HURWITZ STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Consider again the continuous LTI SISO system in relation to the sets H and H x. The diffeomorphism between the set of stabilizing feedback gains for a system and its controllable canonical form (Observation II.3) allows us to prove a number of topological and metrical properties for H and H x. In fact, Observation II.3 leads to the following properties through the application of theory of polynomials: (a) H is open in the Euclidean topology for both statefeedback and output-feedback systems, (b) H x is unbounded but H can be either bounded or unbounded, (c) the sets H and H x are both convex when the corresponding system has order two, (d) H x is connected and H can have at most ⌈ n 2 ⌉ connected components. We now provide the proofs for these observations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "PROPERTIES OF HURWITZ STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Lemma III.1. The set H is open in R and H x is open in R n.

<!-- chunk {"id": "body-0015", "role": "body", "section": "PROPERTIES OF HURWITZ STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Proof. By Observation II.3, without loss of generality, we shall assume that the system (A,b,c ⊺) is in the controllable canonical form. Let a = (a 0,..., a n -1) be the last row of A and c = (c 0,..., c n -1) ⊺. For any k ∈ R, the characteristic polynomial of this system is given, We note that for a fixed k ∈ R, the map ˜ υ ∶ C n ∗ / S n → R given by is continuous since υ ∶= max ○ Re ∶ C n ∗ → R is continuous and there is a unique continuous map ˜ υ ∶ C n / S n → R such that υ = ˜ υ ○ π: this follows from the properties of the quotient topology (see Theorem 3.73 in). Thus the map, is continuous as it is a composition of continuous maps. Thus as the pre-image of the open interval (-∞, 0) under the continuous map g, the set H is an open subset of R and as such, H is a union of disjoint open intervals.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROPERTIES OF HURWITZ STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

8 Following a similar argument, the map g x ∶ R n → R defined via the composition, is continuous and hence H x is open in R n.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROPERTIES OF HURWITZ STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

We shall point out another favorable property of H x, namely that it is regular open. In other words, the closure of the set of Hurwitz stabilizing controllers is the set of marginally stabilizing controllers and H x is precisely the interior of the set of marginally stabilizing controllers.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PROPERTIES OF HURWITZ STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

8 That is, it can always be represented as such.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Proof. By Observation II.3, it suffices to assume that the pair (A,b) is in controllable canonical form. For any k = (k 0,..., k n) ⊺ ∈ R n, the characteristic polynomial of the corresponding closed-loop system is, By Pole-shifting theorem, for every n -tuple (-j, -j,..., -j), with j ∈ R, there is some k j ∈ R n such that k j ∈ H x and the zeros of p (λ, A -b (k j) ⊺) are exactly (-j,..., -j). But a 0 -k j 0 = (-j) n by Vieta's formula. 9 Hence H x is not bounded.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

For an output feedback system, the set H can either be bounded or unbounded depending on the properties of the system ( A,b,c ⊺ ); this is demonstrated in the following example.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Example 1. Let the triplet ( A ♭, b ♭, c ⊺ ), in controllable canonical form, be controllable. 10 Let a = ( a 0, a 1,..., a n -1 ) be the last row of A ♭. Then,

<!-- chunk {"id": "body-0022", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

- a) If for some i, j ∈ { 0,..., n -1 }, c i > 0 and c j < 0, then H is bounded. - b) Suppose that n = 4 and the entries of c are positive. If c 3 c 2 c 1 < c 2 3 c 0 then H is unbounded; when c 3 c 2 c 1 > c 2 3 c 0, H is bounded.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

The assertions in this example are consequences of the RouthHurwitz Criterion. If k is stabilizing, then If there exists a k that satisfies the above inequalities, and for some i, j, c i > 0 and c j < 0, then k satisfies, 9 The indexing of k j is with reference to.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

10 Of course, the controllability of the triplet is independent of c.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Hence, H must be bounded. For part (b), the Routh-Hurwitz Criterion states that, We note that for sufficiently negative k, the last inequality holds since c 1 c 2 c 3 > c 2 3 c 0; hence H is not bounded. On the other hand, if c 1 c 2 c 3 < c 2 3 c 0, then k must be bounded from below; thus H is bounded.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

We further make an observation on a necessary condition for the unboundedness of the set H; see also.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Observation III.4. If ( A,b,c ⊺ ) is controllable and observable, a necessary condition for H to be unbounded is that the nonzero entries of c have the same sign. Moreover, if H is unbounded, then H must only include one of the two intervals: (-∞, M ) and ( M ′, ∞) for some M,M ′ ∈ R.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Proof. If a monic polynomial is Hurwitz stable, all of its coefficients are positive (Theorem 2. 4 in ). Hence, we have a j -kc j > 0 for every j. If the nonzero entries of c do not have the same sign, k should be bounded. Since the system is observable, c ≠ 0. Thereby, either k < M or k > M ′, for some M,M ′ ∈ R.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

We now make a few observations on the convexity of the sets H and H x; needless to say, these observations have direct algorithmic implications. It is known that a convex combination of stable polynomials is not necessarily convex. However, a convex combination of stable monic polynomials with degree 2 is convex; this follows from the Routh-Hurwitz criterion.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Observation III.5. For the state feedback system ( A,b ), the set H x is convex if n = 2.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Proof. It suffices to show this for (A ♭, b ♭). Let k = (k 0, k 1) ⊺ and k ′ = (k ′ 0, k ′ 1) ⊺ be two stabilizing feedback gains. Then the characteristic polynomial of the corresponding closed-loop systems are, Note that p 1 and p 2 are stable if and only if the coefficients are positive. 11 Hence, if ˆ k = (1 -δ) k + δk ′, for δ ∈, then p ˆ k (x) = (1 -δ) p 1 (x) + δp 2 (x) and p ˆ k is stable by the positivity of its coefficients.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Observation III.6. For the output feedback system ( A,b,c ⊺ ) with n = 2, the set H is convex.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

Proof. Recall that by Observation II.2, Noting that span (c) ∩ H x is a convex subset of R 2; by Observation III.5, the proof follows.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

11 For convexity analysis, this is in fact the key property for systems of order 2.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Observation III.3. The set H x is unbounded", "weight": 1.0} -->

We can also use the Routh-Hurwitz stability criteria to show the nonconvexity of the set of stabilizing feedback gains when n > 2. For example, let n = 3 and consider the controllable canonical form (A ♭, b ♭) with the last row of A ♭ set to 0. Then the stabilizing feedback gain is parametrized by three parameters k = (k 1, k 2, k 3) and the characteristic polynomial of A -bk ⊺ is The following example essentially shows that convex combinations of stable polynomials are not necessarily stable.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 2. Consider the system,", "weight": 1.0} -->

For k 1 = (-24, -5, -5 ) ⊺ and k 2 = (-0. 9, -1, -1 ) ⊺, the characteristic polynomials of the corresponding closed-loop systems are given by p 1 ( λ ) = λ 3 + 5 λ 2 + 5 λ + 24 and p 2 ( λ ) = λ 3 + λ 2 + λ + 0. 9. Both polynomials are stable and as such, k 1, k 2 ∈ H x; however, k ′ = 0. 5 k 1 + 0. 5 k 2 yields an unstable characteristic polynomial p ( λ ) = λ 3 + 3 λ 2 + 3 λ + 12. 45.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We will now delve into connectedness of the sets H and H x, requiring more delicate arguments as compared with their boundedness and convexity properties. For the state feedback system, by Corollary II.1.1, H x is connected in R n. We now show that this set is in fact contractible, i.e., it can be continuously deformed to a point.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Lemma III.7. When ( A,b ) is controllable, the set of stabilizing feedback controllers H x ⊆ R n is connected and contractible.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proof. Let { H n -} ∗ denote the set of n -tuples v ∈ H n -invariant under (entry-wise) complex conjugation. We note that { H n -} ∗ / S n is connected in C n / S n by noting that every v ∈ { H n -} ∗ / S n is path-connected. This path in fact defines a homotopy between the identity and the constant map (-1,..., -1). Mind that i.e., an affine translation in R n. By Corollary II.1.1, it now follows that H x is connected and contractible.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Remark III.8. Note that even though the set H x in contractible to a point, it is not necessary star-convex. This is due to nonlinearity of the Vieta's map ˆ σ -1.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Connected Components of H: We now develop bounds on the number of connected components of H as it is not necessary connected. Lemma III.10 provides a bound of n and Lemma III.14 will tighten the bound to ⌈ n 2 ⌉. We have chosen to present the two lemmas in sequence, since the proof of Lemma III.10 is straightforward but tightening the bound to ⌈ n 2 ⌉ requires more delicate analysis.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Let us start our analysis by recalling the smooth dependence of simple roots of a polynomial on its coefficients, subsequently used in Lemma III.14.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Lemma III.9. Let a j ∶ I → R be C ∞ functions for j = { 1,..., n }, where I ⊆ R is an open interval. If t 0 ∈ I and λ 0 is a simple root of the polynomial f (λ) = a n (t 0) λ n + a n -1 (t 0) λ n -1 + ⋅ ⋅ ⋅ + a 0 (t 0) ∈ R [λ] with t 0 ∈ I, then there exists a C ∞ function η ∶ J → C over an open interval J ⊆ I such that t 0 ∈ J, η (t 0) = λ 0 and η (t) is a zero of Proof. This follows from Implicit Function Theorem. First note that f (λ, t) is C ∞ in both λ and t; we note that at (λ 0, t 0), f ′ (λ 0, t 0) ≠ 0 since λ 0 is a simple zero.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We now prove an upper bound of n on the number of connected components of H.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Lemma III.10. If H ≠ ∅, it has at most n connected components.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proof. Note that in the SISO case, H is a subset of R; furthermore, it suffices to show that (A ♭, b ♭, c ⊺) has at most n connected components. Recall that for k ∈ R, the characteristic polynomial of a closed-loop system A ♭ -kb ♭ c ⊺ is given by where a: = (a 0, a 1,..., a n -1) is the last row of A ♭ and c j 's are components of c. Let ζ ∶ R n → P n (λ) denote the natural bijection, assigning coefficients to monic polynomials. We denote, Γ = { a ∈ R n ∶ ζ (a) has at least one zero on imaginary axis }, and ℓ (k) = a -kc, i.e., a parametrized line in R n. Suppose that ℓ (k) intersects Γ for finitely many k 's, listed in an increasing order k 1,..., k q; this fact will be proved subsequently. Let n p (λ,k) (H -) denote the number of roots of p (λ, k) in H -.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Moreover, let γ (r) be a counterclockwise oriented curve in C consisting the line segment [-ir, ir] and the semicircle S (r, θ) = re iθ, with θ ∈ [π / 2, 3 π / 2]. For each k ∈ (k j, k j + 1), we define Note that if p (λ, k) does not vanish on γ (r), by Cauchy's Argument Principle, m r (k) is the number of zeros of p (λ, k) inside the curve γ (r). However, since p (λ, k) has at most n roots, the integral is well-defined except at finitely many r 's. Hence m (k) is well-defined and m (k) = n p (λ,k) (H -). In the meantime, the function m (k) is continuous in k and integer-valued, and thereby, m (k) = n p (λ,k) is constant on each interval (k j, k j + 1).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

That is, either n p (λ,k) = n or n p (λ,k) < n, corresponding to either stabilizing or nonstabilizing gains, respectively. So by inspecting the number of intersections between ℓ (k) and Γ, one can derive an upper bound on the number of connected components of H. Let Consider an intersection of ℓ (k) and Γ that is, when for some k ∈ R, there exists λ = iβ, β ∈ R, for which p (iβ, k) = 0. We first observe that r (iβ) ≠ 0 since otherwise iβ would be a root for every k ∈ R. This on the other hand, implies that H is empty.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Hence p (iβ, k) = 0 implies that, Since k ∈ R, β must be a root of, We note that φ (β) ∈ R [β] has degree at most 2 n -1. Thus it can be written as, for some set of real coefficients { d 2 n -3, d 2 n -5,..., d 1 } ⊆ R, noting that all exponentials of i are either 1 or -1. Now let us set τ (β) = i 2 n -2 β 2 n -2 + i 2 n -4 d 2 n -3 β 2 n -4 +⋅⋅⋅ + i 2 d 3 β 2 + d 1 ∈ R [β]; hence, φ (β) = βτ (β). Now we note that τ (β) is an even polynomial in β (having only even degrees). Letting we have τ (β) = υ (β 2). Thereby, the roots of τ are the square roots of those of υ. This implies that τ has two real roots if υ has a positive real root.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We further observe that if β 0 is a positive real root of υ (β), then √ β 0 and - √ β 0 are the real roots of τ.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Let us now consider the scenario that leads to greatest upper bound on the number of connected components of H. This scenario corresponds to the situation where φ ( β ) has 2 n -1 real roots; let these roots be { 0, β 1, -β 1,..., β n -1, -β n -1 }, where β j ∈ R + for each j. These roots can be mapped to feedback gains via relation; in fact, β j and -β j are mapped to the same k. Thus adding the k that corresponds to the 0 root via relation, we will have at most n values for k. These values on the other hand, divide the real line into n + 1 intervals. But only one of the two unbounded intervals can be stabilizing by Observation III.4; the upper bound of n on the number of connected components of H now follows.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Remark III.11. Note that having n connected components for H implies that we can have a situation where { k 1,..., k n } are marginally stabilizing gains and the open intervals (k j, k j + 1) are stabilizing. Figure 1 demonstrates this phenomena for two adjacent intervals: there is a gain k 0 such that the closed-loop system is marginally stable but (k ′, k 0) and (k 0, k ′′) are both stabilizing for some k ′, k ′′ ∈ R. 12 The system parameters 13 are Fig. 1: An example where the feedback gain k 0 leads to a marginally stable closed-loop system yet both intervals (k ′, k 0) and (k 0, k ′′) are stabilizing for some k ′, k ′′ ∈ R.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We now proceed to show that the bound on the number of connected components of H can be tightened to ⌈ n 2 ⌉. The proof of this tighter bound follows a distinct line of reasoning, as necessitated by examples such as that shown in Figure 1. The result contains several technical details. Let us outline the idea behind the proof first: we denote by { 0, β 1, -β 1,..., β n, -β n } as the real roots of φ ( β ) and { k 1,..., k n } in an increasing order as the feedback gains acquired via relation in Lemma III.10:

<!-- chunk {"id": "body-0054", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

- a) We will first show that when two adjacent intervals (k j -1, k j) and (k j, k j + 1) are stabilizing, then p (λ, k j) = λ n +(a n -1 -k j c n -1) λ n -1 +⋅⋅⋅ + (a 0 -k j c 0) would have the non-stable mode λ 0 = iβ, i.e., the mode with zero real part, as a simple root of p (λ, k j) ∈ R [λ]. By Lemma III.9, this would imply that we can find some C ∞ function η ∶ I → C (with I ⊂ R and k i ∈ I) such that η (t) tracks the zero of p (λ, k) locally with η (k j) = r. Indeed, what we really need is that the curve of the root iβ is differentiable at iβ.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

- b) If two adjacent intervals are both stabilizing, the curve η (t) is tangent to the imaginary axis at t 0. We show that this observation leads to having -β j and β j as multiple zeros of φ (β). Mind the subtlety here: λ 0 is the simple root of the polynomial p (λ, k j) ∈ R [λ] in λ whereas ± β j are multiple zeros of the polynomial φ (β) ∈ R [β] in β (recall the expression for φ (β) in the proof of 12 Note that Theorem 1 in uses the same line of reasoning as the proof of Lemma III.10 to arrive at the improved bound of ⌈ n 2 ⌉ for the number of connected components in H, assuming that the intervals constructed above are stabilizing/non-stabilizing interlacing intervals. However, as Figure 1 depicts, this assumption is not valid in general. The ⌈ n 2 ⌉ bound is still valid, however, and can be obtained by utilizing the structure of the polynomial φ (β) and the relation between the feedback gain k and parameter β.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

13 These parameters are actually chosen carefully according to the analysis of Lemma III.14.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Lemma III.10.). See Figure 2 for a demonstration of the relations.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

- c) Using the multiplicities of λ j ′ s as roots of φ ( β ) and a careful counting of the stabilizing/non-stabilizing intervals lead to the final result.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We shall developing several propositions before we prove the main result. First we provide an asymptotic expansion of the zeros of p ( λ, k ) with respect to k. Note that this is not simply a Taylor expansion around k, as a multiple root is not differentiable with respect to k. Recall the definitions of the polynomials r ( λ ) and s ( λ ) used in the proof of Lemma III.10.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proposition III.12. Suppose for k 0 ∈ R, λ 0 is a root of p (λ, k 0) ∈ R [λ] with multiplicity m ∈ N and r (λ 0) ≠ 0. Then for k that is sufficiently close to k 0, p (λ, k) will have m roots given, for j = 1,..., m, where ω j 's are the m th roots of unity, 14 h (λ) ∈ R [λ] is such that p (λ, k 0) = (λ -λ 0) m h (λ), and o (∣ k -k j ∣ 1 / m) signifies a function f (k) for which lim k → k j ∣ f (k)∣/∣ k -k j ∣ 1 / m = 0.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

15 Before we prove the proposition, let us remark that in the case that (k -k j) r (λ 0)/ h (λ 0) is negative, there would be m choices for ((k -k j) r (λ 0)/ h (λ 0)) 1 / m, namely (-(k -k j) r (λ 0)/ h (λ 0)) 1 / m e i (π + 2 πl)/ m for l = { 0, 1,..., m -1 }. Note that these numbers differ multiplicatively from each other by e i 2 πν / m, with ν ∈ { 0,..., m -1 }; the expression above would not be affected by selecting any of these numbers. Moreover, this statement should be interpreted separately for k ↑ k j and k ↓ k j. The difference amounts to a rotation of λ j 's.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proof. Since λ 0 is a root of multiplicity m, p (λ, k 0) = (λ -λ 0) m h (λ), where h (λ) ∈ R [λ] with h (λ 0) ≠ 0. Hence, for k ∈ R, we can write p (λ, k) as Now suppose that (λ -λ 0) m h (λ) - (k -k j) r (λ) = 0. Putting ˆ λ = λ -λ 0, ˆ h (ˆ λ) = h (ˆ λ + λ 0)/ h (λ 0), ˆ r (ˆ λ) = r (ˆ λ + λ 0)/ h (λ 0) and t = k -k j, it suffices to show that the zeros of ˆ λ m ˆ h (ˆ λ) -t ˆ r (ˆ λ) are exactly, as t → 0. Note that ˆ h = 1 and ˆ h (ˆ λ) ∈ R [ˆ λ]. Let t > 0 and observe that if z is a zero of 14 That is, there are the zeros of z m -1.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

15 Recall root locus rules! then t 1 / m z would be a zero of λ m h (λ)-t r (λ). On a compact set [0, T] (T ∈ R +), ψ t (λ) → ψ 0 (λ) = λ M -r uniformly. Let us denote the zeros of ψ 0 (λ) = λ m -r by where ω j 's are the m th roots of unity. Choose a sufficiently small ε > 0 such that the disks B z j (ε) are disjoint. Since ∂B z j (ε) is compact and ψ 0 (λ) does not vanish on ∂B z j (ε), there is some l > 0 such that ∣ ψ 0 (λ)∣ > l. Since ψ t (λ) → ψ 0 (λ) uniformly on any compact subset of C, there is some t ∗ > 0, such that ∣ ψ t (λ) -ψ 0 (λ)∣ < l for t ∈ (-t ∗, t ∗) and λ ∈ ¯ B z j (ε).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

By Rouché's Theorem, there is exactly one zero for ψ t (λ) in each B z j (ε) for t ∈ (-t ∗, t ∗). As such, the zeros of ψ t (λ) are given, It then follows that, the case where t < 0 can be treated similarly by considering t h (λ) = (-t)(-h (λ)). Hence, Before we proceed to the proof of the main result of this section, let us make an observation pertaining to the derivative of f (β) ∈ R [β] evaluated on the imaginary axis.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proposition III.13. Consider f (λ) = α m λ m +⋅⋅ ⋅ + α 1 λ + α 0 ∈ R [λ] and let ϕ (β) = Im (f (λ)∣ λ = iβ) ∈ R [β]. Then we have, Proof. When m is odd we have, But we also note that, The case when m is even follows analogously.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We are now ready to prove the bound ⌈ n 2 ⌉ on the number of connected components of H.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Fig. 2: The relation between roots of φ ( β ) and p ( λ, k ), as the root locus intersects the imaginary axis for continuous time systems.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Lemma III.14. Let H≠∅; then it has at most ⌈ n 2 ⌉ connected components.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proof. Consider two adjacent intervals (k j -1, k j) and (k j, k j + 1) that are both stabilizing. Note that by assumption p (λ 0, k j) = 0 for some pure imaginary λ 0. First, let us examine whether λ 0 can have multiplicity m ≥ 2. By Proposition III.12 for k sufficiently close to k 0, p (λ, k) will have m roots given, for j = 1,..., m, where ω j 's are the m th roots of unity. When m ≥ 3, as k → k j, m roots, from m equally spaced directions in the complex plane (see Figure 3), would tend to λ 0. In Fig. 3: Roots coming from m = 3 equally spaced directions in the complex plane tend to λ 0 this case, at least one direction would be in the right half plane, contradicting the assumption that both (k j -1, k j) and (k j, k j + 1) are stabilizing. If m = 2, the roots would traverse a horizontal line passing through λ 0, 16 with on of the intervals as nonstabilizing.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

This is again a contradiction. Hence λ 0 must be simple. This on the other hand would imply the differentiability of the root with respect to k. By the asymptotic formula above (with m = 1), the derivative of η ′ (k j) = r (λ 0)/ h (λ 0); 16 Note that in this case either k ↑ k j or k ↓ k j would yield the quantity (k -k j) r (λ 0)/ h (λ 0) in Proposition III.12 positive, and the resulting expression would be a scalar multiple of the primitive 2 nd roots of unity, i.e., ± α for some α ∈ R. note that in this scenario h (λ 0) = p ′ (λ 0, k j).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

But the condition that both intervals are stabilizing implies that η ′ (λ 0) is pure imaginary (the tangent of the curve should be the imaginary axis, see Figure 1); that is for some γ ∈ R. This implies that if λ 0 = iβ (β ∈ R) is a zero of φ (β); since η ′ (λ 0) is pure imaginary, we would also have, where s (λ) = a n -1 λ n -1 +⋅ ⋅ ⋅+ a 0. Putting r (λ) = r o (λ)+ r e (λ), where r o (λ) consists of the terms with odd degrees and r e (λ) consists terms of even degrees, we observe that r (¯ λ)∣ λ = iβ = r (-iβ) = r e (iβ) -r o (iβ) = (r e (λ) -r o (λ))∣ z = iβ.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Now by Proposition III.13, we have Noting that (λ n + s (λ) -k r (λ))∣ λ = λ 0 = 0, we have Now r ′ e (λ) consists of terms with odd degrees and r ′ o (λ) of those with even degrees; this implies that, minding that r ′ (¯ λ) refers to the derivative of r ′ (λ) evaluated at ¯ λ.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Furthermore, Combining all these observations, we conclude that φ ′ (β) = 0. Now let { 0, u 1, -u 1,..., u µ, -u µ, v 1, -v 1,..., v ν, -v ν } denote the roots of the polynomials φ (β), where u i 's and v j 's are nonnegative real numbers, and v 1, -v 1,..., v ν, -v ν are roots with multiplicity greater than 1. We must then have 2 µ + 2 (2 ν) ≤ 2 n -2. These roots will be mapped to the gains k via the relation, Now let Λ = { k 1,..., k µ ′ } be the set of distinct real gains corresponding to { u 1, -u 1,..., u µ, -u µ } and Π = { k 1,..., k ν ′ } be the set of distinct real gains corresponding to { v 1, -v 1,..., v ν, -v ν }.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Note that µ ′ ≤ µ and ν ′ ≤ ν since it is possible that multiple roots are mapped to the same k; append k corresponding to 0 via. We must then have µ ′ + 2 ν ′ ≤ n. Now if k j ∈ Λ, then one of the intervals (k j -1, k j) and (k j, k j + 1) is not stabilizing. Let Υ be the collection of intervals that are not stabilizing. It follows then that if k ∈ Λ, k must be the end point of an interval in Υ. Note that only one of the unbounded intervals could be stabilizing; thereby, Now, Lemma III.10 implies that the set of feedback (real) gains k is divided into ν ′ + µ ′ + 1 intervals. As such, ν ′ + µ ′ + 1 -∣ Υ ∣ is the number of stabilizing intervals, obtained by subtracting the number of non-stabilizing intervals from the total number of intervals. Hence, Remark III.15. We note that ⌈ n 2 ⌉ is a tight upper bound.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Indeed, Figure 1 already indicates that there are two disjoint stabilizing intervals for a SISO system with n = 3. Figure 4 provides a more transparent view of this; the system parameters are, We mention that although stabilizing and non-stabilizing intervals do not necessary interlace for all controllable and observable triplets (A,b,c ⊺), this property is indeed generic. 17 To this end, we first observe that the set CO of all controllable and observable triplets (A,b,c ⊺) is open in M n × n (R) × R n × R n.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proposition III.16. The set CO is (Zariski) open.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

17 Aproperty is generic when it holds except on an algebraic (Zariski closed) set.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Root path of the largest real part as k varies Fig. 4: The figure depicts how the root with the largest real part varies with respect to the feedback gain k. The blue and yellow segments correspond to two stabilizing intervals.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proof. Putting C to denote the controllability matrix and O to denote the observability matrix. We observe (CO) c = C c ∪ O c ∪C c O c, where C c denotes the collection of non-controllable but observable systems, O c denotes the collection of nonobservable but controllable systems, and C c O c denotes the collection of non-controllable and non-observable systems. 18 We note that C c is the set where all the n × n minors of C vanish. Similarly for O c and C c O c. Hence, (CO) c is an algebraic set. Consequently, CO is open.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

We now observe the interlacing property is generic.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Lemma III.17. For a controllable and observable system ( A,b,c ⊺ ), the property that the stabilizing and non-stabilizing intervals in H interlace is generic.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

Proof. Denote U ⊆ CO the subset such that the corresponding Hurwitz stabilizing set H has the interlacing property. As we have shown, for any (A,b,c ⊺) ∈ CO, if we have two adjacent stabilizing (or non-stabilizing) intervals, then the corresponding polynomial φ (β) must have a root with multiplicity greater than one. This means the discriminant of φ (β) must vanish. This in turn is a polynomial in the entries of A,b,c ⊺. That is, This suggests that U is Zariski open and nonempty (see for example, Figure 4). 19 An algorithm for characterizing the connected components of H: Our analysis for deriving the bound ⌈ n 2 ⌉ for the number of connected components of H has direct algorithmic implications. We summarize the corresponding algorithm as follows.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

18 For a set A, A c denotes its complement.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Connectedness properties of H x and H", "weight": 1.0} -->

19 Note that M n ( R )× R n × R n is identified by the affine space A n 2 + 2 n [ R ] and the subset CO is equipped with the Zariski subspace topology.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Algorithm 1: Identifying stabilizing intervals of H", "weight": 1.0} -->

- 1: Find the real roots { λ 1,..., λ l } of the real polynomial. Appending { 0 } to this list if necessary, we get L = { 0, λ 1,..., λ l }. Map L to { k 1,..., k l ′ } (order this list in an increasing manner). - 2: Identify whether (-∞, k 1) and (k l ′, +∞) are stabilizing (Observation III.4). - 3: If (-∞, k 1) is stabilizing, check the multiplicity of λ 1 ′ that maps to k 1. If λ 1 ′ is simple, then (k 1, k 2) is not stabilizing. If λ 1 ′ is not simple, check whether is satisfied; if not, i.e., the corresponding derivative is not pure imaginary, then (k 1, k 2) is not stabilizing. If this derivative is pure imaginary, then (k 1, k 2) is stabilizing. Continue the process.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Algorithm 1: Identifying stabilizing intervals of H", "weight": 1.0} -->

The main computational cost of Algorithm 1 is finding the roots of a real polynomial. The specifics are beyond the scope of this paper; see, and references therein for the recent algorithmic developments in this direction.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Algorithm 1: Identifying stabilizing intervals of H", "weight": 1.0} -->

Let us demonstrate the progression of Algorithm 1 for the example in Remark III.11. The characteristic polynomial of the closed-loop system for this example is then with nonnegative roots 0, √ 6018 40, where √ 6018 40 has multiplicity 2. The root β 1 = 0 is mapped to k 1 = -625919 6 × 10 7, and β 2 = √ 6018 40 to k 2 = 2041 6000. We start from the unbounded interval (k 2, ∞): pick k and test the stability of the closed loop system; n this case, we conclude that (k 2, ∞) is stabilizing. Since k 2 is acquired from a multiple root of φ (β), we examine the derivative p ′ (λ, k 2); since it is pure imaginary, we conclude that the interval (k 1, k 2) is stabilizing. As such (-∞, k 1) is not stabilizing by Observation III.4.

<!-- chunk {"id": "body-0088", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

In this section, we study the properties of the set of static feedback gains for discrete-time linear systems. Here is our first observation.

<!-- chunk {"id": "body-0089", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Proof. Without loss of generality, as we have done throughout this paper, we assume that the pair (A,b) is in the controllable canonical form. Recall that the bilinear transform, is a diffeomorphism between the unit disk D and the open left-half plane H -in C. Clearly G: = (g,..., g) ∶ D n → H n -defines a diffeomorphism between D n → H n -. Passing to the quotient space (modulo the action of the symmetric group), we have a diffeomorphism ˜ G ∶ D n / S n → H n -/ S n given by ˜ G ○ π = G, where π is the canonical projection.

<!-- chunk {"id": "body-0090", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Let ζ be the bijection between R n and the set of monic n th degree polynomials, i.e., if α = (α 0,..., α n -1) ∈ R n, then ζ (α) = λ n + α n -1 λ n -1 +⋅⋅⋅ + α 0. Denote the sets, By Corollary II.1.1, we have following commuting diagram: where { D n } ∗ / S n ⊆ C n / S n denotes the n -dimensional vector invariant under conjugation with entries inside the unit disk of C; similarly for { H n -} ∗ / S n (recall the notation in § II).

<!-- chunk {"id": "body-0091", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Now, the map defines a homeomorphism between E and F. However, note that S x = a - E and H x = a - F, where a is the last row of A. This completes the proof since a translation in R n is a diffeomorphism.

<!-- chunk {"id": "body-0092", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

Remark IV.2. The above result immediately implies that S x is open, connected and contractible since H x is. In our subsequent discussion, we will also outline more direct proofs for the above facts since they provide additional insights into the structure of the set of stabilizing feedback gains for discrete-time linear systems.

<!-- chunk {"id": "body-0093", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

In view of Lemma IV.1, one might be inclined to construct a similar homeomorphism between the sets S and H. However, as it turns out, the technique adopted in Lemma IV.1 can not be generalized for this purpose. For example, when k 0 ∈ S, it does follow that k 0 c ∈ S x. However, under the homeomorphism constructed in Lemma IV.1, the image of k 0 c is not necessarily a scalar multiple of c. For a concrete example, one may consider the triplet (A,b,c ⊺) given by We note 0 ∈ S and Z p (λ,A -0 bc ⊺) = { 0,..., 0 }. Under the bilinear transform, the zeros will be mapped to {-1,..., -1 }, which corresponds to characteristic polynomial p (λ) = λ 4 -4 λ 3 + 6 λ 2 -4 λ + 1. However, no k ∈ H can yield a closed-loop system A -kbc ⊺ with this characteristic polynomial.

<!-- chunk {"id": "body-0094", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

- a) S and S x are both open in the Euclidean topology. - b) S and S x are both bounded. - c) S and S x are convex if the system has two states.

<!-- chunk {"id": "body-0095", "role": "body", "section": "PROPERTIES OF SCHUR STABILIZING FEEDBACK GAINS", "weight": 1.0} -->

20 Note that we are not claiming that such homeomorphism does not exist. The non-existence of such a homeomorphism requires a deeper understanding of these two topological subspaces. To the best of our knowledge such a homeomorphism has not been reported in the literature.

<!-- chunk {"id": "body-0096", "role": "body", "section": "S x is connected and S has at most ⌈ n 2 ⌉ connected components", "weight": 1.0} -->

Most of the proofs for the discrete time case have a similar flavor as their continuous counterparts. However, the proof for the upper bound on the number of connected components of S has a few distinct steps.

<!-- chunk {"id": "body-0097", "role": "body", "section": "S x is connected and S has at most ⌈ n 2 ⌉ connected components", "weight": 1.0} -->

Lemma IV.3. The set S is open in R and S x is open in R n.

<!-- chunk {"id": "body-0098", "role": "body", "section": "S x is connected and S has at most ⌈ n 2 ⌉ connected components", "weight": 1.0} -->

Proof. The proof proceeds similar to the proof of Lemma III.1. We only need to observe that the composition map, is continuous, even when adopted on the quotient space. That is, there is a unique continuous map ˜ υ ∶ C n ∗ / S n →[0, ∞) such that υ = ˜ υ ○ π. Hence the map, is continuous. The interval [0, 1) is open in the subspace topology of [0, ∞) and S is the preimage of [0, 1) under the above map; thereby, S is open.

<!-- chunk {"id": "body-0099", "role": "body", "section": "S x is connected and S has at most ⌈ n 2 ⌉ connected components", "weight": 1.0} -->

In order to show that S x is open in R n, we only need to observe that the map F ∶ R n →[0, ∞), given by We now note that contrary to the continuous time case, the sets S and S x are bounded.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Observation IV.5. The set S x is convex when n = 2", "weight": 1.0} -->

Proof. Without loss of generality, we assume that the pair (A,b) is in the controllable canonical form. Suppose that k = (k 0, k 1) ⊺ and e = (k ′ 0, k ′ 1) ⊺ are two stabilizing controllers. The characteristic polynomials of the corresponding closedloop systems are then, 21 The entries of k are consistent with the way the are indexed in the characteristic polynomial.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Observation IV.5. The set S x is convex when n = 2", "weight": 1.0} -->

Note that by Vieta's formula, k 0 < 1 and k ′ 0 < 1 since the zeros are inside the unit disk. For ˆ k = ( 1 -δ ) k + δk ′ with δ ∈, consider the corresponding characteristic equation p ˆ k ( λ ) = ( 1 -δ ) p k ( λ )+ δp k ′ ( λ ).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Observation IV.5. The set S x is convex when n = 2", "weight": 1.0} -->

If p ˆ k has two conjugate zeros z 1, ¯ z 1, then ∣ z 1 ∣ = ∣ ¯ z 1 ∣ < 1 by Vieta's formula since ∣ z 1 ∣ 2 = ( 1 -δ ) k 0 + δk ′ 0 < 1. On the other hand, if p ˆ k has two real zeros, suppose that one of them is 1 or -1 (note that by Vieta's formula, the product of two zeros is strictly less than 1; hence the other zero is inside the open unit disk), i.e., p ˆ k = 0 or p ˆ k (-1 ) = 0. Note that p k, p k (-1 ), p ˆ k, p ˆ k (-1 ) are all positive since if p k has two conjugate zeros, then p k ( λ ) is positive on the real line; if p k has two real zeros, by the assumption that the zeros are in (-1, 1 ), p k, p k (-1 ) are positive.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Observation IV.5. The set S x is convex when n = 2", "weight": 1.0} -->

This is a contradiction to the assumption that p ˆ k = 0 or p ˆ k (-1 ) = 0 (as p ˆ k ( λ ) is the convex combination of p k ( λ ) and p k ′ ( λ ) ). Hence the zeros of p ˆ k must be in the open unit disk for every δ ∈.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Connectedness properties of S x and S", "weight": 1.0} -->

The following topological property of the set S x has immediate algorithmic implications.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Connectedness properties of S x and S", "weight": 1.0} -->

Lemma IV.6. For the state feedback system, the set S x is connected and contractible in R n.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Connectedness properties of S x and S", "weight": 1.0} -->

Proof. The proof proceeds similar to the proof of Lemma III.7. Putting Γ = { λ ∈ C ∶ ∣ λ ∣ < 1 } n, it suffices to show that Γ ∗ / S n is connected and contractible. 22 But this is immediate since any v ∈ Γ ∗ / S n is connected to ( 0,..., 0 ) by the convex line segment ( 1 -δ ) v + δ 0 ( δ ∈ ) in Γ ∗.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Connectedness properties of S x and S", "weight": 1.0} -->

For the output feedback case, the set S is not connected in general. Following is an example of a SISO system with more than one path-connected component. 23 Example 3. Consider the LTI system (A,b,c ⊺), The feedback controllers are then parametrized by intervals in R. Figure 5 depicts that the roots of the closed loop system are inside the unit disk for some interval, then become unstable, and subsequently reenter the unit disk as k varies; as such, S has two connected components.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Connectedness properties of S x and S", "weight": 1.0} -->

Connected Components of S for SISO Systems: We now show that there is at most ⌈ n 2 ⌉ connected components in S. We will follow a similar line of reasoning as for the continuous systems presented in § III-A. We shall demonstrate the upper bound n fi rst, followed by the upper bound of ⌈ n 2 ⌉. The essential ideas for proving the two results are similar to the strategy we followed in Lemmas III.10 and III.14, with some subtle differences.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Algorithm 2: Identifying stabilizing intervals of S", "weight": 1.0} -->

- 1: Find real zeros { λ 1,..., λ l } of the real polynomial. Note that these zeros correspond to cos (θ). Mapping these zeros to the corresponding values of λ, we get { λ 1, ¯ λ 1,..., λ l, ¯ λ l }. Appending {-1, 1 } to this list if necessary, we get a new list L = { 1, -1, λ 1, ¯ λ 1,..., λ l, ¯ λ l }. Mapping L to { k 1,..., k l ′ } (order this list in an increasing manner). - 2: Start from the interval (-∞, k 1). It is not stabilizing by Proposition IV.4. Check the multiplicity of λ 1 ′ that maps to k 1. If λ 1 ′ is simple, then (k 1, k 2) is not stabilizing; if λ 1 ′ is not simple, check whether is satisfied; if not, i.e., the corresponding derivative is not pure imaginary, then (k 1, k 2) is not stabilizing.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Algorithm 2: Identifying stabilizing intervals of S", "weight": 1.0} -->

On the other hand, if this derivative is pure imaginary, then (k 1, k 2) is stabilizing. Continue the process.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Algorithm 2: Identifying stabilizing intervals of S", "weight": 1.0} -->

We demonstrate the progression of Algorithm 2 on the example in Remark IV.8. The characteristic polynomial of the closed-loop system is given by 24 In particular, when n = 2, the set S corresponding to the triplet (A,b,c ⊺), if nonempty, is connected. has a root 6018 40 with multiplicity 2. Then sin (θ 1) = 0 is mapped to k 1 = 0. 06065638 and k 3 = 20. 09687366; cos (θ 2) = √ 6018 40 on the other hand maps to k 2 = 0. 6198635016. By Corollary IV.4.1, the two unbounded intervals (-∞, k 1) and (k 3, ∞) are both non-stabilizing. We note that k 1 corresponds to sin (θ) = 0 and thereby (k 1, k 2) is stabilizing. Since k 2 is obtained from a multiple root of g (cos (θ)), we need to check condition. In this case, we conclude that the interval (k 2, k 3) is stabilizing. 25

<!-- chunk {"id": "body-0112", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

The motivation for this work stems from recent interest in devising learning type algorithms for control synthesis, that evolve over the set of stabilizing feedback gains. This in turn, has inspired the need to further examine the topological properties of these sets. We envisage that some of these properties might been observed in the earlier literature in system theory and known to experts; 26 however, this work is an attempt to gather and prove these properties in a concise and rigorous manner using basic topology and the theory of polynomials. In this work, we have focused on topological and metrical properties of stabilizing state feedback gains and SISO output feedback gains for continuous and discrete time linear systems; some of these results have MIMO counterparts that are discussed. In this latter case, topological arguments turn out to be even more dominant for characterizing the set of stabilizing feedback gains, with less reliance on the geometry of polynomials.
