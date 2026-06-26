<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-driven Distributionally Robust MPC for Constrained Stochastic Systems

Topics include Optimal control, Robustness, Online algorithms, Optimization, Control, Learning, Robust optimization, Robust control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we introduce a novel approach to distributionally robust optimal control that supports online learning of the ambiguity set, while guaranteeing recursive feasibility. We introduce conic representable risk, which is useful to derive tractable reformulations of distributionally robust optimization problems. Specifically, to illustrate the techniques introduced, we utilize risk measures constructed based on data-driven ambiguity sets, constraining the second moment of the random disturbance. In the optimal control setting, such moment-based risk measures lead to tractable optimal controllers when combined with affine disturbance feedback. Assumptions on the constraints are given that guarantee recursive feasibility. The resulting control scheme acts as a robust controller when little data is available and converges to the certainty equivalent controller when a large sample count implies high confidence in the estimated second moment. This is illustrated in a numerical experiment.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

D ISTRIBUTIONALLY robust optimization (DRO) has gained traction recently as a technique that balances robustness with performance in an intuitive fashion. From a theoretical point of view such techniques act as regularizers and in a data-driven setting, DRO acts at the interface between stochastic and robust optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In the control community the potential of such techniques has not gone unnoticed,. Here one would ideally solve stochastic optimal control problems like where x t ∈ I R n x denotes the state. Parametrized, causal policies π ∈ Π map disturbances to inputs. That is, an element π t of the sequence π = { π t } N -1 t =0, maps { w i } t -1 i =0 to inputs in I R n u for t ≥ 1 and π 0 ∈ I R n u. Here, the disturbances w t ∈ I R n w are i.i.d. random vectors, the distribution of which is unknown, usually introducing the need for robust approaches. DRO then improves upon classical robust control by using available data to infer properties of the distribution, while retaining guarantees.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

† P. Coppens and P. Patrinos are with the Department of Electrical Engineering (ESAT-STADIUS), KU Leuven, Kasteelpark Arenberg 10, 3001 Leuven, Belgium. Email: peter.coppens@kuleuven.be, panos.patrinos@kuleuven.be This work was supported: the Research Foundation Flanders (FWO) PhD grant 11E5520N and research projects G0A0920N, G086518N and G086318N; Research Council KU Leuven C1 project No. C14/18/068; Fonds de la Recherche Scientifique - FNRS and the FWO - Vlaanderen under EOS project no 30468160 (SeLMA); EU's Horizon 2020 research and innovation programme: Marie Skłodowska-Curie grant No. 953348.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The core construct in DRO is the ambiguity set, a set of distributions against which one should robustify. Several ambiguity sets have been examined with varying success. The most common are moment-based, φ -divergence and Wasserstein ambiguity sets. Such ambiguity sets are connected to so-called risk measures by duality. Hence this approach is directly related to risk-averse optimization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Throughout the paper we rely on conic representable ambiguity and risk to derive tractable problems, similar to the methodology presented,. The main contributions are then as follows: (i) we derive tight, data-driven, moment-based ambiguity sets that are conic representable and shrink when more data becomes available; (ii) we extend conic risks to the multi-stage setting and use them to model average value-at-risk constraints; (iii) we synthesize the controller such that it is recursive feasible when it is applied in a receding horizon fashion; (iv) we illustrate how our framework leads to tractable controllers based on affine disturbance feedback policies, which are evaluated in numerical experiments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Similar results were achieved in for a tube-based approach with Wasserstein ambiguity, the radius of which is not data-driven; in for relaxed, robust constraints; in for moment-based ambiguity which is not data-driven and does not guarantee recursive feasibility; and, for discrete distributions. DR control of Markov decision processes with finite state-spaces was also considered. Our framework supports online learning of truly data-driven ambiguity sets and risk constraints within a continuous state-space, while guaranteeing recursive feasibility.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This section continues with notation and preliminaries. Next §II introduces conic and data-driven ambiguity in a single-stage setting and §III introduces multi-stage extensions as well as the optimal control problem that we want to solve. Then §IV shows how to construct a controller such that recursive feasibility is guaranteed. Finally §V illustrates how our techniques lead to tractable controllers and contains numerical experiments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "SINGLE-STAGE PROBLEMS", "weight": 1.0} -->

Given the dual formulation of a risk measure, it is clear that the choice of A is a critical design decision. In this section we introduce how ambiguity sets, using moment information, are derived from data. We also introduce conic representable risk, used to derive tractable problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Data-driven risk", "weight": 1.0} -->

In DRO the reasoning is usually as follows. Consider a probability space (Ω, F, I P) and the optimization problem with u ∈ I R n u some decision variable, f some loss function and w: Ω → W a random variable with W ⊂ I R n w the (compact) support of w. The main difficulty in solving the stochastic optimization problem is that the distribution (or push-forward measure), µ ⋆ ∈ P (W) defined on the sample space (W, B) as µ ⋆ (O) = I P[w -1 (O)] for all O ∈ B and with w -1 (O) the pre-image of O, is unknown.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Data-driven risk", "weight": 1.0} -->

Hence, instead one introduces an ambiguity set A ⊆ P (W), which contains µ ⋆ with some confidence. To do so one can estimate some statistic θ based on data. In the case of φ -divergence and Wasserstein ambiguity, this θ is the empirical distribution, while for moment-based ambiguity, θ encapsulates moment information. We will consider this final case in §II-B. To summarize: Definition II.1. Consider random variable w: Ω → W with distribution µ ⋆ and i.i.d. samples w 0: M -1: Ω → W M. Let θ: W M → Θ denote a statistic for a set Θ and let β ∈ I R be some radius 1. Then a data-driven ambiguity A: Θ × I R ⇒ P (W) with confidence δ ∈ maps (θ (w), β) to an ambiguity set A β (θ (w)) ⊆ P (W) such that In this is referred to as a learning system.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Data-driven risk", "weight": 1.0} -->

Based on we minimize ρ A β ( ˆ θ ) [ f ( u, w )] instead of. The result upper bounds with probability at least 1 -δ.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Moment-based ambiguity", "weight": 1.0} -->

As mentioned before, we focus on the case where θ encapsulates moment information. Such ambiguity sets have the advantage that (i) they can contain measures with support not limited to the observed samples (unlike most φ -divergence based sets); (ii) the radius is estimated with reasonable accuracy based on known information of the distribution (unlike for Wasserstein-based sets); and (iii) problem complexity does not grow with the sample count.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Moment-based ambiguity", "weight": 1.0} -->

To ensure that an ambiguity set satisfying can be derived, we assume that W is bounded, which is often the case in control applications and is therefore the usual assumption in robust control. Other common choices are that w is multivariate Gaussian or that it satisfies some concentration properties (e.g., sub-Gaussian). We have: Lemma II.2. Let W = { w ∈ I R n w: ‖ w ‖ 2 ≤ r } and R w = diag(I n w, cr) with c ∈ I R. Assume we have a set of i.i.d. samples w 0: M -1 of w ∼ µ ⋆ and let ˆ C:= ∑ M -1 i =0 w i w ⊤ i /M. Then, Proof. We use a matrix Hoeffding bound [20, Thm. 1.3] with improved constants. See App. A for the full proof.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Moment-based ambiguity", "weight": 1.0} -->

Remark II.3. In the numerical experiments towards the end of the paper we select c = 1 / 4. This choice results in a relatively simple expression for the radius and performed well in experiments.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Moment-based ambiguity", "weight": 1.0} -->

1 Some moment-based ambiguity set can have multiple radii (cf. ).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

We introduce conic representable ambiguity (similar to the framework, ) below and show how such risk is related to robust optimization through conic duality.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

Definition II.4. Consider a compact sample space W ⊂ I R n w and Z = C (W). An ambiguity set A is conic representable if, for some E,F: M (W) → I R n b and b ∈ I R n b, with ν some auxiliary measure and K a closed, convex cone. Usually we assume F = 0. When F = 0 we refer to the ambiguity as ν -conic representable. Similarly we refer to ρ A, as, as (ν -)conic representable risk (conic for short).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

The parameters of A should be selected such that it is an ambiguity set (i.e., a nonempty, closed and convex subset of P ( W ) ). Since we usually want an A satisfying, it will be non-empty as it should at least contain the true distribution. The random variables used to construct E and F, are all continuous. Therefore [21, Thm. 15.5] E and F are continuous mappings. Thus A is the intersection between the closed set P ( W ) and the pre-image of a closed set under a continuous mapping, which is also closed. Hence A is a closed subset of P ( W ). Convexity of A then follows, since E and F are linear and K is convex.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

In it was shown that both the average and entropic value-at-risk are conic whenever W is finite. Many more risks fall under this framework,.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

Direct application of conic linear duality gives: Lemma II.5. A risk ρ A [z] as in Def. II.4 is equal to the optimal value of where the functional inequalities should hold pointwise for all w ∈ W, E ∗ and F ∗ denote the adjoint operators (cf. §I-A), and K ∗ the dual cone.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

Proof. By the primal problem is with val(P) = ρ [z] (where we omit the subscript for convenience). We refer to the minimization problem (D) as the dual problem. Let τ ∈ I R and λ ∈ I R n b. Then the Lagrangian is where we can use to construct the adjoints. We have Hence max ν ∈ M + (W) min λ ∈ K ∗,τ { (b -Eµ -Fν) · λ } = -χ [µ], where χ is the indicator of A. Therefore Similarly note that [17, Eq. 3.7] which follows from a similar argument as. As such since λ gives a finite cost iff τ + E ∗ λ -z ∈ M ∗ + (W) and F ∗ λ ∈ M ∗ + (W) (i.e. τ + E ∗ λ -z ≽ 0 and F ∗ λ ≽ 0).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

All that is left is to show strong duality (i.e. val( D ) = val( P ) = ρ [ z ] ). This follows directly from coherence of ρ (specifically ρ being proper, implying consistency of ( P )), compactness of W and [17, Cor. 3.1].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

Note that constraints in the dual are robust constraints, since they hold for all w ∈ W. Hence, techniques from robust optimization enable finding tractable reformulations.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

Moreover, letting λ = (Λ, V) with Λ, V ∈ S n w +1 and τ ∈ I R while using Lem. II.5, means where the adjoint E ∗: I R n b → Z, is (cf.)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

If the constraint τ + E ∗ λ ≽ z is LMI representable, then ρ A β (ˆ C) [z] can be evaluated by solving a SDP. For example if z = w ⊤ Pw. Then, since w ⊤ w ≤ r 2, we can apply the S-Lemma [23, Thm. B.2.1.] to show that τ + E ∗ λ ≽ z iff., We also consider ambiguity with only support constraints.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conic-representable ambiguity", "weight": 1.0} -->

Example II.7. Ambiguity P ( W ) is conic representable with n b = 0. Hence, ρ P ( W ) [ z ] = min τ { τ: τ ≽ z }, corresponds to ρ P ( W ) [ z ] = max w ∈ W z ( w ) and only considers the support as is common in robust optimization.

<!-- chunk {"id": "body-0029", "role": "body", "section": "MULTI-STAGE PROBLEMS", "weight": 1.0} -->

In this section we show how conic single-stage risk can be extended to a multi-stage setting, which is required to develop distributionally robust MPC controllers. Specifically, we will consider risk measures operating on the dynamics with x t ∈ I R n x (u t ∈ I R n u) the state (input) and w t ∈ I R n w the disturbance, which follows a random process. For t ∈ I N 0: N -1 we consider ℓ t: I R n x × I R n u → I R + a stage cost function, and ℓ N: I R n x → I R + the terminal cost.

<!-- chunk {"id": "body-0030", "role": "body", "section": "MULTI-STAGE PROBLEMS", "weight": 1.0} -->

We can then consider multistage ambiguity sets A t, which are nonempty, closed and convex subsets of P t. These in turn define a multistage analog to risk measures 2, multistage risk measures [6, §4.2], ρ A t: Z t → I R. Since this is simply a usual risk measure, but defined on Z t, the properties of Lem. I.1 generalize. We specifically consider coherent multistage risk For each stage t, the trajectory up to that time w 0: t -1 is an element of W t. For each W t, B t is the accompanying Borel sigma-algebra, (M t) M t + the set of (signed) measures and P t the set of probability measures on (W t, B t). For brevity we henceforth omit the explicit dependency on W t. Also consider the paired spaces of continuous functions Z t = C (W t).

<!-- chunk {"id": "body-0031", "role": "body", "section": "MULTI-STAGE PROBLEMS", "weight": 1.0} -->

Given such risks, the goal is to solve, for a given x 0, where Π denotes a set of parametrized, continuous, causal policies. The risk constraints (9c) involve the multistage risk measures r t A and are discussed in detail in §IV. We illustrate how interpolates between the robust setting and in §V.

<!-- chunk {"id": "body-0032", "role": "body", "section": "MULTI-STAGE PROBLEMS", "weight": 1.0} -->

Remark III.1. Problem is not exact as we optimize over parametrized policies (cf. §V), for tractability. As such, time-consistency cannot be guaranteed (i.e. a policy computed at t = 0 may not be optimal at t = 1 after realization of w 0 ). Hence a receding horizon scheme is used.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Product ambiguity", "weight": 1.0} -->

To enforce independence of the disturbances w t we introduce product ambiguity [6, §4.2]. For a sequence of single-stage ambiguity factors A i for i ∈ I N 0: t -1, consider 2 Multistage risk is often constructed using nested conditional risk measures. We avoid such a construction for conciseness and tractability. The consequences of this are discussed in [6, §4]. where some µ t ∈ A 0 × · · · × A t -1 if it is constructed as a product measure of some µ i ∈ A i, for i ∈ I N 0: t -1 (denoted by µ t = µ 0 ×··· × µ t -1). We show that in certain cases such ambiguities are conic representable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Product ambiguity", "weight": 1.0} -->

Before doing so we need to extend linear operators E i: M → I R n b to take arguments in M t in a natural way. To do so, note that for any E i: M → I R n b and µ ∈ M we have E i µ = ∫ w ∈ W e i (w)d µ (w) for some e i: W → I R n b, by definition. Measures µ t ∈ M t take arguments w: t -1 = (w 0,..., w t -1), so we introduce E | i: M t → I R n b such that With these new operators we have Lemma III.2. Let A i be conic representable with parameters E i, b i, K i for i ∈ I N 0: t -1. Then × t -1 i =0 A i is also conic representable with parameters Proof. Let µ t = µ 0 ×··· × µ t -1, with µ i ∈ P i. Then, following the notation, where (i) follows from µ t = µ 0 × · · · × µ t -1 and µ t ∈ P t.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Product ambiguity", "weight": 1.0} -->

Hence E | i µ ≼ K i b i iff E i µ i ≼ K i b i. Repeating the same argument for each i proves that A t:= × t -1 i =0 A i is conic representable. Since A i are all non-empty, A t is also nonempty. Convexity and closedness follow from the arguments below Def. II.4. The dual then follows from applying Lem. II.5.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Risk constraints", "weight": 1.0} -->

Ideally constraints like (9c) would require the state to lie within some set almost surely. Since such a constraint in a stochastic setting can be very conservative, we will instead implement average value-at-risk constraints, for α ∈, Such constraints (i) act as a convex relaxation of chance constraints; (ii) penalize the expected violation in the α quantile where violations do occur. In control applications is natural, since it penalizes large violations more.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Risk constraints", "weight": 1.0} -->

To evaluate the expectation, true knowledge about the distribution is needed. Hence, we will operate on the distributionally robust AV@R constraint instead: with A the core ambiguity. If A satisfies, then implies the chance constraint I P[z t ≤ 0] ≥ 1 -ε holds with 1 -ε ≤ (1 -δ)(1 -α). Moreover, whenever A is conic, then robust AV@R is ν -conic.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Risk constraints", "weight": 1.0} -->

Lemma III.3. Let A be conic with parameters E c, b c, K c. Then r -AV@R A α in is ν -conic with Proof. This proof generalizes the methodology of to arbitrary conic representable risk. First note that by [27, Thm. 2.1]. Specifically let φ (τ, w) = τ + α -1 [z (w) -τ] +. Then we have (i) φ (τ, ·) ∈ Z, implying that it is µ integrable and measurable; (ii) φ (·, w) is convex for any w ∈ W; (iii) ρ A [z -τ] + is finite (Lem. I.1); (iv) the set A ⊆ P (W) is compact (Lem. I.1); (v) φ (τ, ·) is continuous and hence bounded for any τ ∈ I R on W. Under these properties as well as A being convex, [27, Thm. 2.1] states that strong duality holds, allowing us to exchange the inf and the max.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Risk constraints", "weight": 1.0} -->

Applying Lem. II.5 to ρ A on the r.h.s., results in (where [ · ] + produces two separate constraints and τ c, λ c act as the Lagrangian multipliers for the constraint µ c ∈ A c ). Again applying Lem. II.5 gives the original ν -conic representation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Risk constraints", "weight": 1.0} -->

The second application of Lem. II.5 requires the resulting set of measures (denoted A α below) to be a nonempty, closed and convex subset of P (W). By construction we already have A α ⊆ P (W). Next, we show that A α is larger than A. After all, for any µ c ∈ A, take µ = µ c and ν = α -1 (1 -α) µ c ≽ 0, since α ∈. Moreover, since K c is a cone, with αµ + αν = αµ c +(1 -α) µ c = µ c. For the same reason we have 〈 1, µ 〉 + 〈 1, ν 〉 = α -1 〈 1, µ c 〉 = α -1. Therefore µ c ∈ A α for each µ c ∈ A. Hence, since A is nonempty, so is A α. Closedness and convexity then follow by the arguments below Def. II.4. So using Lem. II.5 is justified.

<!-- chunk {"id": "body-0041", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

We show how one can configure the constraints of such that recursive feasibility is ensured. To do so we assume We introduce the terminal set X N:= { x: ψ (x) ≤ 0 }. Let V A N (x 0) denote the minimum of for some x 0 and let D N (A) denote its domain. Then consider the set of feasible policies Π N (x 0, A):= { π ∈ Π: (9b), (9c), (9d) }.

<!-- chunk {"id": "body-0042", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

(A2) A is updated based on measurements as g ( A, w ) (e.g., following Lem. II.2) and A +:= g ( A, w ) ⊆ A a.s.

<!-- chunk {"id": "body-0043", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

We begin with the following definition.

<!-- chunk {"id": "body-0044", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

Definition IV.1 (Recursive Feasibility). Let x 0 ∈ D N ( A ) and π ∈ Π N ( x 0, A ). If, f ( x 0, π 0, w 0 ) ∈ D N ( g ( A, w 0 )) a.s., then is recursive feasible (RF).

<!-- chunk {"id": "body-0045", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

We can then prove the following theorem: Theorem IV.2. Assume (A1), (A2) and that we are given some terminal policy π f (x N) such that (A5) ∀ π 0: N -1 ∈ Π, let π N = π f (x N), depending on w: N through x N. Then the shifted policy π + 0: N -1 = π 1: N (w 0, ·) for any fixed w 0 ∈ W, lies in Π. Then, is recursive feasible.

<!-- chunk {"id": "body-0046", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

- (A4) X N is robust positive invariant (RPI) for π f (i.e., f (x, π f (x), w) ∈ X N for each (x, w) ∈ X N × W); Proof. We will consider any fixed w 0 ∈ W and show that, given that is feasible for some x 0, it will also be feasible for the next time step starting from x + 0 = f (x 0, π 0, w 0) (cf. Def. IV.1). Here, we consider the feasible policy π 0: N -1 ∈ Π N (x 0, A), to which we append π N = π f (x N). Propagating the dynamics with this policy gives the sequence of states x 0: N +1, depending on w: N through (9b).

<!-- chunk {"id": "body-0047", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

We then define the shifted sequence of states as where w 0 is considered fixed and w 1: N is left variable. We can analogously define the shifted policy π + 0: N -1 as By construction, these shifted sequences satisfy (9b) and we can consider risk measures over (continuous) functions of these, where integration is performed over w 1: N.

<!-- chunk {"id": "body-0048", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

Using this coupling between the feasible problem and the shifted problem we show π + ∈ Π N ( x 0, A + ). That is, the candidate policy π + is feasible for the shifted problem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

- II: We show that (9c) at t implies (9c) in the shifted problem at t -1. That is, r t A [φ (x t)] ≥ r t -1 A [φ (x + t -1)] for any w 0 ∈ W. So, letting z = φ (x t) with z τ = [z -τ] +. For z +:= φ (x + t -1) = z (w 0, w 1: t -1) (z + τ = [z + -τ] +), we replace ρ P t -1 × A [z τ] with ρ P t -2 × A [z + τ] for r t -1 A [z +]. Writing out ρ P t -1 × A gives Noting that µ t = µ t -1 × µ t -1 with µ t -1 ∈ P t -1 and µ t -1 ∈ A, before splitting up the max and the integrals, gives (i).

<!-- chunk {"id": "body-0050", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

The inner integral (i.e. h (w: t -2)) then acts as a continuous random variable W t -1 → I R for any fixed µ t -1 (cf. App. B). Hence we can apply the reasoning within Ex. II.7 to maximize over w: t -2 ∈ W t -1 instead of over measures resulting in (ii). It is clear that, fixing the value of w 0 results in the inequality (iii). Reverting the steps (i) and (ii) to get a maximization over µ t -1 ∈ P t -2 × A shows that the final expression after (iii) equals ρ + A t -1 [z + -τ] +. Hence ρ P t -1 × A [z -τ] + ≥ ρ P t -2 × A [z + -τ] + for all τ ∈ I R, z ∈ Z t and w 0 ∈ W. Therefore r t A [φ (x t)] ≥ r t -1 A [φ (x + t -1)].

<!-- chunk {"id": "body-0051", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

Since A + ⊆ A by (A2), r t A [φ (x t)] ≥ r t -1 A + [φ (x + t -1)]. Hence (9c) holds for all t ∈ I N 1: N -2 in the shifted problem. For t = N -1 we rely on (A3) and (A4).

<!-- chunk {"id": "body-0052", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

III: The terminal constraint (9d) follows directly from (A4).

<!-- chunk {"id": "body-0053", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

We have thus shown that π + is a feasible policy.

<!-- chunk {"id": "body-0054", "role": "body", "section": "RECURSIVE FEASIBILITY", "weight": 1.0} -->

Remark IV.3. Note that (A1) is essential since RF is a robust property, holding a.s. It acts as a convex relaxation of chance constraints conditioned on previous time steps (i.e., I P[ φ ( x t ) ≤ 0 | x t -1 ] ≤ ε which holds a.s., hence ∀ µ t -1 ∈ P t -1 by Ex. II.7). Due to the reduction of the policy space Π (cf. Rem. III.1) it is harder to satisfy such constraints for larger t. Other (less conservative) reformulations exist in the stochastic MPC literature, which impose all constraints at the first time step using a (maximal) RPI set (cf. ).

<!-- chunk {"id": "body-0055", "role": "body", "section": "AFFINE DISTURBANCE FEEDBACK", "weight": 1.0} -->

To make the reformulations above more concrete, we show how is solved. In general this is intractable, since we need to optimize over infinite dimensional policies π, under robust constraints associated with the risks (cf. Rem. III.1). Hence, we use affine disturbance feedback. The resulting optimization problem is a SDP. Different ambiguity sets and policies would give other reformulations (e.g. ).

<!-- chunk {"id": "body-0056", "role": "body", "section": "AFFINE DISTURBANCE FEEDBACK", "weight": 1.0} -->

Consider linear dynamics, quadratic losses and constraints: with Q ⪰ 0, R ⪰ 0, Q f ⪰ 0, G ⪰ 0, G f ⪰ 0. We could include (hard) input constraints as well or multiple state constraints (cf. discussion in [4, §1] on modeling joint chance constraints), but abstain from doing so for conciseness.

<!-- chunk {"id": "body-0057", "role": "body", "section": "AFFINE DISTURBANCE FEEDBACK", "weight": 1.0} -->

In this setting affine disturbance feedback has been applied to solve many robust optimal control problems (and even some DRO problems). The idea is to let where F: I R (N +1) n w → I R (N +1) n x (defined in App. C), has a structure that enforces causality of π. Note x: N ∈ I R (N +1) n x, w: N -1 ∈ I R Nn w and u: N -1 ∈ I R Nn u.

<!-- chunk {"id": "body-0058", "role": "body", "section": "AFFINE DISTURBANCE FEEDBACK", "weight": 1.0} -->

The state trajectory then depends on the disturbance as with A, B, E defined in App. C, F = [F, f] and H = [H, h] = [BF + E, A x 0 + Bf]. Here the linear part, H, can be interpreted as the sensitivity of the state to the disturbance, while h = (h 0,..., h N) is the deterministic part of the state (i.e., the state trajectory when w = 0).

<!-- chunk {"id": "body-0059", "role": "body", "section": "AFFINE DISTURBANCE FEEDBACK", "weight": 1.0} -->

We first show how the cost (9a) is implemented, before doing the same for the risk constraints (9c) and the terminal constraint (9d).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Reformulation of the cost", "weight": 1.0} -->

We will assume the risk in (9a) has a product ambiguity, A N = A β (ˆ C) ×···× A β (ˆ C) with A β (ˆ C) as in Lem. II.2. Letting z:= x ⊤ Qx + u ⊤ Ru, (9a) is Note, by Ex. II.6, that the factors A i = A β (ˆ C) for i ∈ I N 0: N -1 are conic with where Q and R are defined in App. C.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Reformulation of the cost", "weight": 1.0} -->

Therefore, by Lem. III.2, A N = × N -1 i =0 A i is conic with and K ρ = K ρ 0 × · · · × K ρ N -1. Let Λ ρ i, V ρ i ⪰ 0, τ ∈ I R, λ ρ i = (Λ ρ i, V ρ i) and b = (R w ˆ CR ⊤ w ± βI) for all i ∈ I N 0: N -1. Then, by Lem. III.2, Our goal is now to find a tight, conservative LMI reformulation of (18b) as an LMI. We use, for any matrix ∆ ∈ S n w +1, the partitioning with [∆] m ∈ S n w, [∆] v ∈ I R n w and [∆] c ∈ I R. We also introduce ∆ ρ i:= R ⊤ w (Λ ρ i -V ρ i) R w for all i ∈ I N 0: N -1. Then, which is quadratic in w. Note that the argument of ρ A N is also quadratic in w. Therefore (cf. z in), (18b) is quadratic in w.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Reformulation of the cost", "weight": 1.0} -->

It should hold for all w in the set of quadratic inequalities W N = { w: w ⊤ i w i ≤ r 2, ∀ i ∈ I N 0: N -1 }. This is conservatively approximated by a LMI, with the approximate S-Lemma [23, Thm. B.3.1.]. Its effect here is conservatively quantified as increasing the radius r by a factor 9. 19 √ ln(N -1), before solving the problem exactly. Specifically (18b) holds if there exists a P ρ ∈ S N w +1 + and s ρ ∈ I R N -1 + such that (remembering ∆ ρ i:= R ⊤ w (Λ ρ i -V ρ i) R w) Here implies w ⊤ P ρ w ≥ z (w) for all w ∈ I R N w by a Schur complement argument. The cost (18a) meanwhile is given as

<!-- chunk {"id": "body-0063", "role": "body", "section": "Reformulation of risk constraints", "weight": 1.0} -->

We consider constraints, r t A with ambiguity A = A β (ˆ C), satisfying (A1). The random variable φ (x t) in (9c) equals and is thus quadratic in w: t -1. By construction, (9c) is of type with core ambiguity P t -1 × A. Both ambiguity factors are conic by Ex. II.7 and Ex. II.6. We now use µ t = µ t -1 × µ t -1. Then, similarly to before, by Lem. III.2, P t -1 × A is conic for Using the duality result of Lem. III.3 shows that (9c) holds if there exists a τ r t, τ r c,t ∈ I R, Λ r t, V r t ⪰ 0 and λ r t = (Λ r t, V r t) such that We applied Ex. II.7 for P t -1 and Ex. II.6 for A. Note that (23a) is a linear constraint.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Reformulation of risk constraints", "weight": 1.0} -->

Since E r | ∗ t -1 λ r t = w ⊤ t -1 R ⊤ w (Λ r t -V r t) R w w t -1, (23b) and (23c) are of similar structure to (18b). That is, a quadratic inequality that should hold for all w: t -1 ∈ W t -1. Hence we can once again apply the approximate S-Lemma followed by a Schur complement, resulting in a LMI.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Reformulation of risk constraints", "weight": 1.0} -->

Specifically, let ∆ r t:= R ⊤ w (Λ r t -V r t) R w. Then, Following a similar procedure to before, we apply the approximate S-Lemma for both (23b) and (23c). Specifically, (23b) holds if there exists some s r 1,t ∈ I R N -1 + such that Meanwhile, (23c) holds if there exists some P r t ∈ S tn w +1 + and s r 2,t ∈ I R N -1 + such that We then apply a Schur complement to find an equivalent LMI: We conclude by reformulating the terminal constraint (9d), which is equivalent to for all w ∈ W N. We apply the approximate S-Lemma, followed by a Schur complement. Specifically holds, if there exists some s f ∈ I R N -1 + such that To summarize, we minimize subject to and (replacing the cumulative stage cost (9a)). Then add constraints for each t ∈ I N 1: N -1 (replacing the chance constraints (9c)). The terminal constraint (9d) is then replaced. The resulting minimization problem is a SDP.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Reformulation of risk constraints", "weight": 1.0} -->

Fig. 1. (left) Range of closed-loop costs when using the matrix-hoeffding bound to construct the ambiguity set for T = 15; (right) state trajectories for M = 10, 10 6 offline samples.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We consider two experiments: one where data is gathered offline and one where data is gathered online. In both settings the controller acts more optimally when more data is available without affecting recursive feasibility.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Offline learning: Consider the linear system with w t distributed as a truncated Gaussian with covariance Σ = 0. 01 2 I and ‖ w t ‖ 2 ≤ 0. 15 and N = 8. For the cost, we take Q = diag, R = 10 and Q f and K f and the solution to the discrete algebraic Riccati equation and the corresponding optimal controller respectively. For the state constraints we have α = 0. 2 and φ (x) = [x] 1 -1. 5 ≤ 0, where [x] 1 denotes the first element of x. For the terminal constraint we have ψ (x) = x ⊤ Q f x -9. 524 ≤ 0, which is RPI for π f (x) = K f x and x 0 = (1. 75, 2).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We investigate sample counts M between 10 and 10 6. For each sample count we gather an offline data set and compute A from Lem. II.2 for δ = 0. 05. Then we propagate the dynamics, with the receding horizon controller for T = 15 time steps, cumulating the stage cost for each step. This experiment is repeated 25 times. The range of resulting costs is shown in Fig. 1. For M = 10 and M = 10 6, closed-loop state trajectories are depicted. The cost initially remains approximately constant, since the moment constraint is inactive due to insufficient samples. Afterwards, the controller gains confidence, moving closer to the state constraint when more data is available, resulting in a lower cost.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Online learning: We illustrate how our framework can be used to construct controllers that learn online, guaranteeing recursive feasibility. Consider the scalar linear system with w t distributed as a truncated Gaussian with variance σ 2 = 0. 05 2, expectation I E[w t] = 0. 05 and | w t | ≤ 1. 0. Let Q = 1, R = 0. 1, N = 5, α = 0. 2 and φ (x) = 1 -x ≤ 0. We use π f (x) = -0. 9 x +2. 375, ψ (x) = (x -2. 375) 2 -1. 375 2 ≤ 0 and Q f the solution to the discrete algebraic Riccati equation. To implement learning, the ambiguity update scheme described in App. D is used (which constructs ambiguity from data based on Lem. II.2 for δ = 0. 05 and rejects an ambiguity set if it is not a subset of the previously accepted ambiguity).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We consider three cases: (i) robust, with A = P and no learning; (ii) online, starting from M = 10 samples and then updating the ambiguity online while running the controller; and (iii) offline, where M = 10000 initial samples and no updates. Fig. 2 depicts the state trajectory, which approaches the constraint for larger M.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Fig. 2. State trajectories for robust; online-; and offline learning.
