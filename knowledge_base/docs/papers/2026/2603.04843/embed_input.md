<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization of Mixed H2/H-infinity Control: Benign Nonconvexity and Global Optimality

Topics include Convex optimization, Nonconvex optimization, Policy iteration, Robustness, Optimization, Control, Policy optimization, Mixed H2/H-infinity control, ECL.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Mixed H2/H-infinity control balances performance and robustness by minimizing an H2 cost bound subject to an H-infinity constraint. However, classical Riccati/LMI solutions offer limited insight into the nonconvex optimization landscape and do not readily scale to large-scale or data-driven settings. In this paper, we revisit mixed H2/H-infinity control from a modern policy optimization viewpoint, including the general two-channel and single-channel cases. One central result is that both cases enjoy a benign nonconvex structure: every stationary point is globally optimal. We characterize the H-infinity-constrained feasible set, which is open, path-connected, with boundary given exactly by policies saturating the H-infinity constraint. We also show that the mixed objective is real analytic in the interior with explicit gradient formulas. Our key analysis builds on an Extended Convex Lifting (ECL) framework that bridges nonconvex policy optimization and convex reformulations. The ECL constructions rely on non-strict Riccati inequalities that allow us to characterize global optimality.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These insights reveal hidden convexity in mixed H2/H-infinity control and facilitate the design of scalable policy iteration methods in large-scale settings.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Performance and robustness are two central objectives in control design: H 2 control optimizes average performance, whereas H ∞ control guarantees safety against worstcase scenarios. Mixed H 2 / H ∞ control provides a principled framework to balance the two, leading to a variety of formulations studied across decades. A particularly influential formulation designs a stabilizing controller that minimizes an H 2 cost bound subject to an H ∞ constraint. Classical solutions based on coupled Riccati equations or linear matrix inequalities (LMIs) are well established, but they provide little understanding of the underlying optimization landscape. Moreover, these methods are inherently model-based and scale poorly with system dimension, limiting their applicability in large-scale or datadriven settings.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, policy optimization has emerged as a promising alternative for controller design, inspired by the success of reinforcement learning in sequential decisionmaking and continuous control tasks. Despite the nonconvexity of policy spaces, recent studies have revealed benign landscapes in various control problems such as stabilization, linear quadratic regulation (LQR), linear quadratic Gaussian (LQG), and dynamic fil- tering. For these control problems, stationary points can be globally optimal, and gradient-based methods can achieve global convergence under mild assumptions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

⋆ The work of Chih-Fan Pai, Yuto Watanabe, and Yang Zheng is supported by NSF CMMI 2320697 and NSF CAREER 2340713.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Email addresses: cpai@ucsd.edu (Chih-Fan Pai), y1watanabe@ucsd.edu (Yuto Watanabe), yujietang@pku.edu.cn (Yujie Tang), zhengy@ucsd.edu (Yang Zheng).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key insight behind these benign landscape results is that many nonconvex control problems can be reformulated as convex ones via appropriate changes of variables. In particular, LMI-based synthesis methods, despite involving auxiliary Lyapunov variables, provide a lens for analyzing the geometry of policy optimization. This perspective has been formalized in the Extended Convex Lifting ( ECL ) framework, which systematically bridges classical convex reformulations and modern nonconvex policy optimization. The ECL framework is broadly applicable, encompassing state-feedback and output-feedback H 2 and H ∞ control as well as distributed control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we revisit the classical mixed H 2 / H ∞ control design from a modern policy optimization perspective. Building on the classical formulations of, we analyze both the general two-channel case and its single-channel specialization, and provide a systematic study of the associated nonconvex optimization landscapes. Our results reveal hidden convexity and establish the absence of spurious stationary points. Beyond new theoretical insights into nonconvex optimization in modern control, these results will facilitate the mixed H 2 / H ∞ design in large-scale and/or model-free data-driven settings.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

This paper presents a systematic study of mixed H 2 / H ∞ state-feedback control through the lens of modern nonconvex optimization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

- Basic landscape properties. We analyze the geometry of the nonconvex feasible set. It is known that this set is open and path-connected (Lemma 2). We further precisely characterize its boundary as the set of policies that exactly saturate the H ∞ constraint (Theorem 1 and Corollary 1). We also examine the landscape of the mixed cost function. This cost function is real analytic in the interior, and continuous on the closure of its domain (Theorem 2 and Lemma 3). Thus, the mixed cost function is smooth, and we provide its explicit gradient formulas (Lemmas 4 and 5). These results underpin our analysis of stationarity, global optimality, and solvability of mixed H 2 / H ∞ control. - Global optimality of stationary points. We investigate the global optimality of the two-channel mixed control. This includes the single-channel setting in as a special case. Despite its nonconvexity, we establish that no spurious stationary points exist (Theorem 3). This property, along with the gradient expressions, recovers the classical optimality conditions (Corollaries 2 and 3).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We further analyze existence and uniqueness, showing that the single-channel case always admits a unique stationary point (Theorem 5), whereas the twochannel case may not (Fact 1). Nevertheless, we prove that a stationary point exists when the robustness constraint is sufficiently relaxed (Theorem 4). - Analysis techniques via ECL. We explicitly construct an extended convex lifting (ECL) for the twochannel mixed control (Theorem 6). While relying on classical LMI techniques, our convex lifting construction is non-trivial since we need to employ non-strict Riccati inequalities and LMIs, in contrast to classical suboptimal controller synthesis based on strict inequalities. This key distinction enables the ECL framework to certify the global optimality of stationary points over the entire feasible set. Moreover, the resulting convex reformulation (Theorem 7) not only preserves the optimal value of the original nonconvex problem, but also guarantees solvability when incorporating boundary policies (Proposition 1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper outline", "weight": 1.0} -->

Notations. We denote the set of k × k real symmetric matrices by S k. For M 1, M 2 ∈ S k, we write M 1 ≺ ( ⪯ ) M 2 and M 2 ≻ ( ⪰ ) M 1 if M 2 -M 1 is positive (semi)definite. The Frobenius norm for matrices is denoted by ‖ · ‖. We use I n and 0 m × n for the n × n identity and m × n zero matrices, respectively, omitting their subscripts when clear. For a subset S of a topological space, int( S ) denote its interior and cl( S ) its closure.

<!-- chunk {"id": "body-0014", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

Consider the continuous-time linear dynamical system where x (t) ∈ R n is the state, u (t) ∈ R m is the control input, w (t) ∈ R n is the disturbance. We focus on static state feedback policies of the form u (t) = Kx (t), where K ∈ R m × n. The set of stabilizing policies is defined as We henceforth denote A K:= A + BK and W:= B w B T w.

<!-- chunk {"id": "body-0015", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

In standard LQR, the disturbance w (t) is modeled as zero-mean white Gaussian noise with identity covariance, i.e., E[w (t) w (τ)] = δ (t -τ) I n. The objective is to find a stabilizing policy K ∈ K that minimizes the averaged cost lim T →∞ E [1 T ∫ T 0 x (t) T Q 2 x (t)+ u (t) T R 2 u (t) dt], where Q 2 ⪰ 0 and R 2 ≻ 0 are performance weight matrices. It is known that LQR can be equivalently cast as H 2 optimal control: min K ∈K ‖ T 2 (K) ‖ 2 H 2, where z 2 defines the H 2 performance output and T 2 (K) denotes the transfer function from w to z 2 as follows On the other hand, H ∞ robust control treats the disturbance w (t) as an adversarial input with bounded energy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

The aim is to design a stabilizing policy K ∈ K that minimizes the worst-case cost sup ∫ ∞ 0 x (t) T Q ∞ x (t)+ u (t) T R ∞ u (t) dt subject to ‖ w ‖ 2 ℓ 2 = ∫ ∞ 0 w T (t) w (t) dt ≤ 1 and x =0, where Q ∞ ≻ 0 and R ∞ ≻ 0. This problem is equivalent to H ∞ optimal control: inf K ∈K ‖ T ∞ (K) ‖ H ∞, where z ∞ defines the H ∞ performance output and T ∞ (K) denotes the transfer function from w to z ∞ as follows One may also consider a mixed H 2 / H ∞ design where β is a prescribed bound. Here, the H 2 channel captures nominal performance, while the H ∞ channel enforces system robustness. It is worth noting that these two channels may be distinct or identical. We define the feasible set of H ∞ -constrained stabilizing policies as Note that a strict H ∞ bound is commonly used to ensure a well-defined stabilizing Riccati solution.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

Recall that the H 2 cost for any stabilizing policy K ∈ K is ‖ T 2 (K) ‖ 2 H 2 = tr((Q 2 + K T R 2 K) ˆ X K), where ˆ X K is the unique solution to the Lyapunov equation Despite simple formulation, problem is challenging to solve. A classical approach from is to minimize an upper bound on the H 2 cost over the feasible set K β.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

To enforce the H ∞ constraint, we instead consider the stabilizing solution X K to the Riccati equation where S K:= Q ∞ + K T R ∞ K. By the bounded real lemma (see Lemma 1), a policy K ∈ K β if and only if admits a unique stabilizing solution X K ⪰ 0 such that the matrix A K + β -2 X K S K is Hurwitz. Subtracting from gives Since A K is Hurwitz and the last term is positive semidefinite, it follows that X K -ˆ X K ⪰ 0, and hence the H 2 cost admits an upper bound ‖ T 2 (K) ‖ 2 H 2 ≤ tr((Q 2 + K T R 2 K) X K) for all K ∈ K β. Therefore, we define the mixed cost where X K is the unique stabilizing solution to.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

In sum, we consider the following mixed design Unlike the H 2 cost, J mix is evaluated using the Riccati solution X K from rather than the Lyapunov solution ˆ X K. Since the cost and constraint in are in general defined by distinct signals z 2 and z ∞, we refer to this formulation as the two-channel mixed H 2 / H ∞ design.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

We make the following standard assumption throughout.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

Assumption 1 ( A,B ) is stabilizable and ( Q 1 / 2 2, A ) is detectable. In addition, the robustness parameter satisfies β > β ∗:= inf K ∈K ‖ T ∞ ( K ) ‖ H ∞.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

We make another assumption for analysis.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

Assumption 2 The matrix Q 2 is positive semidefinite. The matrices W, Q ∞, R 2, and R ∞ are positive definite.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Policy optimization for mixed H 2 / H ∞ design", "weight": 1.0} -->

Remark 1 (Single-channel case) Whenthe H 2 and H ∞ channels share the same performance output, J mix in simplifies. Specifically, let Q:= Q 2 = Q ∞ and R:= R 2 = R ∞ in and, so that z 2 = z ∞. Under Assumption 1, where P K is the stabilizing solution to the Riccati equation with A K + β -2 WP K Hurwitz. We give further details in Appendix A.1. As we will see, this reformulation yields a simpler gradient formula and a closed-form optimum. ✷

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Classical solutions to mixed H 2 / H ∞ design primarily rely on Riccati equations or LMIs. While effective for smallto medium-scale systems, these techniques offer limited insight into the optimization landscape, and may face challenges in high-dimensional or data-driven settings.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem statement", "weight": 1.0} -->

In this work, we revisit the mixed H 2 / H ∞ control in from a nonconvex optimization perspective.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem statement", "weight": 1.0} -->

- Geometry of the optimization landscape. We study the geometry of the H ∞ -constrained feasible domain K β, and analyze key properties of the mixed cost function, including continuity, analyticity, and gradient expressions. - Global optimality of stationary points. We investigate whether problem admits spurious stationary points. We further derive the optimality conditions, and analyze the existence and uniqueness of stationary points. - Analysis via the ECL framework. We explore if the hidden convexity in problem can be revealed via an appropriate convex lifting. In particular, we ask if an extended convex lifting (ECL) can be constructed to certify the global optimality of stationary points.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Collectively, our results provide a renewed understanding of mixed H 2 / H ∞ control through nonconvex optimization and convex lifting, and offer guidance for the design of principled policy optimization algorithms in large-scale or model-free settings.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Basic Landscape Properties", "weight": 1.0} -->

In this section, we investigate the optimization landscape of, i.e., the geometry of the feasible set K β and structural properties of the mixed cost function J mix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Geometry of the H ∞ constrained domain", "weight": 1.0} -->

We start with a version of the Bounded Real Lemma, which connects a Riccati equation (or inequality) to an upper bound on the H ∞ norm. Here, we slightly abuse the notation for the matrices A, B, and C, but this should cause no confusion in the context.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Theorem 2 Under Assumption 1, the mixed H 2 / H ∞ cost function J mix in is real analytic on K β.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

We now examine some properties of the cost function. It is clear from Lemma 2 that J mix is nonconvex. Our next result shows that it is real analytic (and hence infinitely differentiable) on the feasible set K β.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Note that J mix is defined through the stabilizing solution X K of, which admits no closed form. Instead, we use the Implicit Function Theorem [43, Theorem 2.3.5] to show that X K depends analytically on K ∈ K β. Thus, the cost J mix is real analytic. Proof details are provided in Appendix A.4.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Since K β is open, the optimal value of problem may not be attained but only approached at the boundary ∂ K β. To capture this limiting behavior, we extend J mix to ∂ K β. By Corollary 1, any K ∈ ∂ K β satisfies ‖ T ∞ (K) ‖ H ∞ = β, so Lemma 1 no longer applies and does not admit stabilizing solution. Nonetheless, it is known that still admits a unique minimal solution X K with eigenvalues of A K + β -2 X K S K in the closed left half-plane [39, Corollary 13.13, Lemma 13.17]. We thus define the boundary cost as where X K is the minimal solution to.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

The above extension is continuous: as K ∈K β approaches a boundary point K 0 ∈ ∂ K β, the cost converges to ˜ J mix ( K 0 ).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Lemma 3 Suppose Assumptions 1 and 2 hold. Given any boundary point K 0 ∈ ∂ K β, we have The proof relies on a nontrivial continuity result for Riccati minimal solutions [44, Theorem 11.2.1], with details deferred to Appendix A.3. As a direct consequence of Lemma 3, the cost J mix is non-coercive, remaining finite as K with ‖ K ‖ < ∞ approaches the boundary of K β. Nevertheless, since J mix serves as a pointwise upper bound on the coercive LQR cost, it exhibits partial coercivity: J mix (K) →∞ as ‖ K ‖ → ∞.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Example 2 (Non-coercivity) Consider the problem instance from Example 1. We set β = 3. 5 and Q 2 = R 2 = I 2 to define J mix. For comparison, we also consider the limiting case β = ∞, which reduces to the LQR cost J LQR. The global optima are K ∗ = -0. 4193 I 2 for J mix and K ∗ LQR = (1 -√ 2) I 2 for J LQR. Fig. 1(b) depicts J mix for K = K ∗ + [0 k 12 k 21 0], while Fig. 1(c) plots J LQR for K = K ∗ LQR + [0 k 12 k 21 0]. As shown in Fig. 1(b), the cost J mix stays bounded as K with ‖ K ‖ < ∞ approaches the boundary ∂ K β, unlike J LQR which diverges in Fig. 1(c). ✷ Theorem 2 ensures that J mix is infinitely differentiable. In particular, we have the following gradient formulas.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Lemma 4 Suppose Assumption 1 holds. For any K ∈ K β, the policy gradient of J mix is given by where X K is the stabilizing solution to the Riccati equation, and Γ K is the unique solution to the Lyapunov equation with ˜ A K:= A K + β -2 X K S K being stable.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Lemma 4 applies to the general two-channel case. In the single-channel case where z 2 = z ∞, an alternative gradient expression can be derived using.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Lemma 5 Suppose Assumption 1 holds. If z 2 = z ∞ in and, the policy gradient of J mix can be evaluated as where P K is the stabilizing solution to the Riccati equation (11b), and Λ K is the solution to the Lyapunov equation with ˆ A K:= A K + β -2 WP K being stable.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

The formula in also applies to the single-channel case by setting Q 2 = Q ∞ and R 2 = R ∞. While mathematically equivalent, the alternative expression in is more useful for analysis. Our proofs of Lemmas 4 and 5 build on the strategy of [16, Appendix B.4], adapting sensitivity analysis of Lyapunov equations to the Riccati settings. Details are provided in Appendices A.5.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Analyticity of the mixed H 2 / H ∞ cost function", "weight": 1.0} -->

Remark 2 (Comparison with LQR) Lemmas 4 and 5 show that computing ∇ J mix requires solving one Riccati and one Lyapunov equation, slightly more involved than the LQR case, which only needs two Lyapunov equations [45, Section IV]. Note that as β →∞, J mix in and reduces to J LQR, and both gradient formulas simplify to ∇ J LQR. In particular, we have ∇ J LQR (K) = 2(R 2 K + B T Γ K) X K, where X K and Γ K are the solutions to the Lyapunov equations This is expected as reduces to LQR as β →∞. ✷

<!-- chunk {"id": "body-0043", "role": "body", "section": "No Spurious Stationary Points", "weight": 1.0} -->

In this section, we characterize the global optimality of the mixed H 2 / H ∞ design.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Since K β is open, any local minimizer of J mix must lie in its interior and thus must be a stationary point. Despite nonconvexity, we establish a key result that every stationary point (when it exists) of is globally optimal.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Theorem 3 Suppose Assumptions 1 and 2 hold. For any policy K ∈ K β, if K is a stationary point, i.e., ∇ J mix ( K ) = 0, then K is a global minimizer of.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Owing to the absence of spurious stationary points, the mixed H 2 / H ∞ design exhibits hidden convexity: every local minimum is globally optimal. This parallels recent results on benign nonconvexity in state-feedback problems such as LQR and H ∞ control.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Theorem3is most closely related to [24, Proposition A.5], which establishes the global optimality of all stationary points in the single-channel case. Its proof relies on a gametheoretic formulation, whose extension to the two-channel case remains unclear. In contrast, our approach builds on convex reformulations via the recently developed ECL framework, which provides greater transparency and directly deals with the general two-channel problem. In this sense, [24, Proposition A.5] appears as a special case of Theorem 3. Our proof involves an explicit ECL construction, which requires careful analysis of (non)strict Riccati inequalities. We provide the details in Section 5.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Building on Lemma 4 and Theorem 3, we further derive stationarity conditions that characterize global optima of problem. To simplify the expression, we assume R ∞ = α 2 R 2 with α ≥ 0 as a design parameter.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Corollary 2 Suppose Assumptions 1 and 2 hold, and assume R ∞ = α 2 R 2 for some α ≥ 0. Then a policy K ∈ K β is global optimal for if and only if there exist matrices Γ ⪰ 0 and X ≻ 0 satisfying the following conditions: where ˜ A K:= A K + β -2 XS K is further Hurwitz.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Proof: We prove the equivalence in two directions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

⇒. Suppose K ∈ K β is globally optimal. Since K β is open, we must have ∇ J mix (K) = 0. Using the gradient formula and setting ∇ J mix (K) = 0 yields where X K is the unique stabilizing solution to the Riccati equation and Γ K solves the Lyapunov equation (17b). Since W ≻ 0, the bounded real lemma ensures that X K ≻ 0. In addition, (17b) implies that Γ K ⪰ 0. Thus, the matrix I + β -2 α 2 X K Γ K is invertible. Let Γ:= Γ K and X:= X K. Then using R ∞ = α 2 R 2, we can rearrange to obtain (20a). It is clear that and (17b) corresponds to (20b) and (20c), respectively. Thus, all three optimality conditions are satisfied.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

⇐. Suppose that there exist X ≻ 0 and Γ ⪰ 0 satisfying (20a) to (20c). From (20b) and the stability of ˜ A K, Lemma 1 implies that K ∈ K β. Substituting the expression for K in (20a) into the gradient formula confirms that ∇ J mix (K) = 0. We then conclude by Theorem 3 that K is a global minimizer of. ✷ Corollary 2 provides necessary and sufficient conditions for a policy K ∈ K β to be globally optimal. Similar conditions were derived in [4, Theorem 4.1] via Lagrange multipliers, but were only shown to be necessary.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Clearly, Corollary 2 also applies to the single-channel case. However, the alternative formulation in leads to a simpler gradient expression, further offering additional insight into global optimality. To see this, with W ≻ 0, the solution Λ K to the Lyapunov equation (18b) is positive definite, and therefore, the stationarity condition ∇ J mix ( K ) = 0 implies K = -R -1 B T P K. Substituting this into the Riccati equation (11b) results in a single Riccati equation, as summarized below.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Corollary 3 Under Assumptions 1 and 2, if z 2 = z ∞ in and, a policy K ∈ K β is globally optimal for if and only if there exists a matrix P ⪰ 0 such that: where A +(β -2 W -BR -1 B T) P is further Hurwitz.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

The proof is similar to that of Corollary 2. We give some details in Appendix B.1. Compared with the coupled con- ditions, the conditions in are much simpler, requiring solving only a single Riccati equation independent of K.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Remark 3 (Connection to LQR) As β →∞, both optimality conditions in the single- and two-channel cases, and, reduce to the classical LQR Riccati equation with the optimal policy K = -R -1 B T P, where P is the stabilizing solution. ✷ Remark 4 (Connection to H ∞ suboptimal control) The Riccati equation (22b) is closely tied to state-feedback H ∞ suboptimal control. By [39, Theorem 17.6] and [44, Theorem 20.2.1], it admits a unique stabilizing solution P if and only if there exists a policy K ∈K β. One suboptimal policy is given by K = -R -1 B T P. As shown in Corollary 3, this K also solves problem with z 2 = z ∞. This highlights the close connection of to several classical formulations, including maximum entropy H ∞ control, risk-sensitive control, and zero-sum dynamic games. ✷

<!-- chunk {"id": "body-0057", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Theorem3andCorollaries2-3 do not ensure the existence of stationary points. In particular, the optimality conditions may be infeasible. We summarize this fact below.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Fact 1 Under Assumptions 1 and 2, the mixed H 2 / H ∞ control may admit no stationary points in K β, and its optimal value may not be attained within K β.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

In fact, the infeasibility of stems from an overly stringent robustness requirement. Relaxing the constraint by increasing β ensures the existence of a stationary point.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Theorem 4 Under Assumption 1, there exists a threshold ¯ β > 0 such that for all β > ¯ β, problem admits a stationary point K ∈ K β. Equivalently, there exists ( K,X, Γ) satisfying where X is the stabilizing solution to (20b).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Note that this existence result does not rely on the assumption R ∞ = α 2 R 2. The proof uses a perturbation argument around the LQR case. The key insight is that as β →∞, the optimality conditions converge to those of LQR (Remark 3), where a stationary point always exists. The details are technically involved, and we present them in Appendix B.2.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

In contrast, the single-channel case always admits a sta- tionary point attaining the optimal value, thanks to its connection to H ∞ suboptimal control (Remark 4).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Theorem 5 Under Assumptions 1 and 2, the singlechannel problem with z 2 = z ∞ admits a unique stationary point K ∈ K β, given by K = -R -1 B T P, where P is the stabilizing solution to the Riccati equation (22b).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Proof: By [39, Theorem 17.6] and [44, Theorem 20.2.1], (22b) admits a stabilizing solution if and only if K β is nonempty, satisfied by Assumption 1. Then, under Assumption 2, the stationary point is given by (22a), and its uniqueness follows from that of the stabilizing solution. ✷ We provide a simple example illustrating Theorems 4 and 5, showing that the existence of stationary points depends on β.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Example 3 Consider a scalar instance of with A = -1, B = B w = 1, Q 2 = 0, Q ∞ = 1, R 2 = R ∞ = 1. The stabilizing set is K = { k ∈ R: k < 1 }. The H ∞ norm can be computed in closed form as J ∞ (k):= ‖ T ∞ (k) ‖ H ∞ = √ 1 + k 2 / (1 -k) for all k < 1, which yields the feasible set With J mix (k) = k 2 X k and X k the stabilizing solution to β -2 (k 2 +1) X 2 k +2(k -1) X k +1 = 0, problem reads Case 1: β = 1. We have K 1 = { k: k < 0 }. The infimum J ∗ 1 = 0 is not attained in K 1 but approached as k → 0 -and X k → 1 + (see Figure 2(a)).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Case 3 (single-channel): β = 1. We consider Q =0 and R =1, which preserves the LQR cost but alters the H ∞ constraint (blue curve in Figure 2(c)). Here, J mix always admits a stationary point, showing that problem structure beyond β also affects the existence of optimal policies.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Case 2: β = 2. We have K 2 = { k: k< (4 -√ 7) / 3 }. The infimum J ∗ 2 = 0 is attained by the optimal policy k ∗ = 0 (see Figure 2(b)). One can verify by Lemma 4 ∇ J mix ( k ∗ ) = 0.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Analysis via Extended Convex Lifting", "weight": 1.0} -->

This section exploits the recent ECL framework to prove the global optimality result in Theorem 3, details the ECL construction for problem, and discusses the solvability of the associated convex reformulation.

<!-- chunk {"id": "body-0069", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

The ECL framework studies a class of nonconvex optimization problems using convex tools. The key idea is simple and based on a change of variables. Let f: R n → R be smooth and nonconvex. Suppose there exists a smooth bijection y = φ ( x ) such that g ( y ):= f ( φ -1 ( y )) becomes convex. It is then clear that min f ( x ) = min g ( y ) and every stationary point of f is globally optimal. Here, the mapping y = φ ( x ) acts as direct convexification.

<!-- chunk {"id": "body-0070", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

The ECL generalizes this idea to a broader class of constrained nonconvex problems that may not admit direct convexification. Indeed, such problems frequently arise in control, including. We first review the definitions and key results of ECL, presenting a simplified version tailored for clarity and relevance to our setting.

<!-- chunk {"id": "body-0071", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

For a function f: D → R with an open domain D ⊆ R d, we define its strict and non-strict epigraphs by Definition 1 (Extended Convex Lifting) Let f: D → R be continuous, where D ⊆ R d is open.

<!-- chunk {"id": "body-0072", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

- L lft ⊆ R d × R × R d ξ is a lifted set with an extra variable ξ ∈ R d ξ, such that its canonical projection onto the first d +1 coordinates, given by π x,γ ( L lft ) = { ( x, γ ): ∃ ξ ∈ R d ξ s.t. ( x, γ, ξ ) ∈L lft }, satisfies

<!-- chunk {"id": "body-0073", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

- F cvx ⊆ R × R d + d ϵ is a convex set and Φ is a C 2 diffeomorphism from L lft to F cvx. - For any (x, γ, ξ) ∈ L lft, we have Φ(x, γ, ξ) = (γ, ζ 1) ∈ F cvx for some ζ 1 ∈ R d + d ϵ. In other words, the mapping Φ directly outputs γ in the first component.

<!-- chunk {"id": "body-0074", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

This procedure generalizes direct convexification by introducing epigraphs and a lifting variable ξ. The set inclusion also adds flexibility. Similar to direct convexification, the existence of an ECL enables the minimization of f over D to be reformulated as a convex problem. Specifically, we have the following equivalence where the right-hand side is convex by the ECL construction. We here define non-degenerate points of f.

<!-- chunk {"id": "body-0075", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

Definition 2 (Non-degenerate points ) Given an ECL ( L lft, F cvx, Φ) for f, a point x ∈ D is called nondegenerate if ( x, f ( x )) ∈ π x,γ ( L lft ).

<!-- chunk {"id": "body-0076", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

Lastly, the existence of an ECL certifies the global optimality of non-degenerate stationary points of f.

<!-- chunk {"id": "body-0077", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

Lemma 6 ([23, Theorem 3.2]) Let f: D → R be differentiable, where D ⊆ R d is open. Suppose f admits an ECL ( L lft, F cvx, Φ). Then, any non-degenerate stationary point x ∗ satisfying ∇ f ( x ∗ )=0 is a global minimizer of f over D.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

The ECL construction also leads to a convex reformulation, which offers further insight into problem.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

Theorem 7 Consider problem and the convex set F cvx in (25b). Under Assumptions 1 and 2, we have We use 'min' in to indicate that the optimum is always attained (see Proposition 1). Unlike optimizing K over the policy space K β, the convex reformulation in optimizes (γ, X, Y) over the higher-dimensional set F cvx.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

The result most relevant to Theorem 7 is [5, Theorem 4.3], which gives a similar reformulation via strict LMIs (equations - therein). While the strict formulation yields the same optimal value, it does not capture the global optimality of all stationary points (Theorem 3).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

We now address the solvability of the reformulation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

Proposition 1 Let γ ∗ be the (finite) optimal value of. Under Assumptions 1 and 2, the following statements hold.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

- The reformulation, i.e. min ( γ,X,Y ) ∈F cvx γ, admits a solution. That is, there exists ( γ ∗, X ∗, Y ∗ ) ∈ F cvx attaining the minimum γ ∗.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

Proof: By Theorem 7, γ ∗ = min ( γ,X,Y ) ∈F cvx γ. We first note that γ ∗ cannot be attained as ‖ K ‖ → ∞ since the corresponding cost diverges. Now consider the case where γ ∗ is attained in K β, i.e., there exists K ∗ ∈ K β with J mix ( K ∗ ) = γ ∗. That is, ( K ∗, γ ∗ ) ∈ epi ≥ ( J mix ). By the inclusion epi ≥ ( J mix ) ⊆ π K,γ ( L lft ), there exists X ∗ such that ( K ∗, γ ∗, X ∗ ) ∈ L lft. Applying the diffeomorphism Φ( K ∗, γ ∗, X ∗ ) = ( γ ∗, X ∗, Y ∗ ) ∈ F cvx then establishes solvability in this case.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

- The corresponding policy K ∗:= Y ∗ ( X ∗ ) -1 lies in cl( K β ) with its extended cost value ˜ J mix ( K ∗ ) = γ ∗.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

Next, consider the case where γ ∗ is not attained in K β. By the continuity in Lemma 3, there exists a boundary policy K ∗ ∈ ∂ K β with ˜ J mix ( K ∗ ) = γ ∗. Crucially, the pair ( K ∗, γ ∗ ) still admits a valid lifting to L lft. This follows from Corollary 4, where epi ≥ ( ˜ J mix ) = π K,γ ( L lft ) guarantees the existence of X ∗ such that ( K ∗, γ ∗, X ∗ ) ∈ L lft. Applying the diffeomorphism Φ( K ∗, γ ∗, X ∗ ) = ( γ ∗, X ∗, Y ∗ ) ∈ F cvx then shows solvability.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

Combining both cases and noting that K ∗ = Y ∗ (X ∗) -1 since Y ∗ = K ∗ X ∗, we conclude that there exists (γ ∗, X ∗, Y ∗) ∈ F cvx with K ∗ ∈ cl(K β). ✷ Proposition 1 guarantees solvability of the convex reformulation in as well as recovery of an optimal policy, even when the optimal value is not attained in K β, in which case the policy lies on the boundary ∂ K β.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present numerical experiments evaluating the performance of different methods for solving the mixed H 2 / H ∞ control and in both small and largescale cases.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

- Analytical solution: For the single-channel case, we solve the Riccati equation (22b) and obtain the optimal policy from (22a). - Policy iteration: Inspired by the optimality conditions in Corollaries 2 and 3, we apply iterative policy updates to solve and its single-channel case. The details are given below. - LMI-based convex optimization: Solve the convex reformulation in with the conic solver MOSEK. - HIFOO: A sophisticated nonsmooth optimization package (v3.501 with Hanso 2.01) for fixed-order H 2 / H ∞ controller synthesis.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

Policy iteration. The method starts from a feasible policy and alternates between policy evaluation (solving a Riccati equation) and policy improvement. It can be viewed as a fixed-point iteration for solving a stationary point ∇ J mix (·) = 0. In the single-channel case with z 2 = z ∞, using, the update simplifies to: which is equivalent to the Gauss-Newton update: K ′ = K -ηR -1 ∇ J mix (K)Λ -1 K with η = 1 / 2. This update preserves feasibility, and its convergence is established. For the general two-channel setting, we adopt an analogous fixedpoint iteration based: While a formal convergence analysis remains open, we conjecture that the method converges for sufficiently large β, and leave this as future work.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

Setup. All experiments are conducted in MATLAB R2024b. The stabilizing Riccati solution is computed using MATLAB's icare. Policy iteration is run until convergence ‖ K ′ -K ‖ < 10 -5. For LMI-based methods, we use MOSEK with its default high-accuracy stopping criteria.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

We compare these methods in terms of 1) the runtime complexity; 2) the square root of J mix of the converged policy; 3) the resulting H 2 and H ∞ norms.

<!-- chunk {"id": "body-0093", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

We begin with a low-dimensional example (instance 0) with a 3 × 3 policy matrix. The problem parameters are The performance matrices for the H 2 and H ∞ channels are For the special case z 2 = z ∞, we set Q = R = I 3. The minimal achievable robustness level (i.e., the optimal H ∞ norm) is β ∗ ≈ 5. 24. We evaluate all methods with β = 6, 14, and 18. One can verify that Assumptions 1 and 2 are satisfied. For reference, in the single-channel case, the optimal LQR policy achieves an H ∞ norm ≈ 9. 26 (with the optimal LQR cost ≈ 9. 92); in the two-channel case, the corresponding values are around 19. 15 and 4. 65, respectively. Therefore, our chosen β values are small enough so that problem cannot be solved analytically for the two-channel case.

<!-- chunk {"id": "body-0094", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

Table 1 summarizes the performance of all four approaches. The ARE row shows that solving (22b) is the most efficient and serves as the benchmark when z 2 = z ∞. From the PI row, we observe that the single-channel update in (28a) performs reliably, requiring only about 10 times the runtime of solving (22b). In the two-channel setting, the policy iteration in (28b) converges for β = 18, maintaining feasibility throughout and achieving the optimal policy of, consistent with the LMI-based solution. However, for smaller values of β, (28b) fails to converge, an observation consistent with our conjecture. For β = 6, the iterates leave the feasible set K β and the procedure terminates (e.g., at some iteration t, the H ∞ norm of K t exceeds 6). For β = 14, the iterates remain feasible in K β but fail to converge, instead exhibiting a periodic behavior suggesting of a limit cycle.

<!-- chunk {"id": "body-0095", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

From the LMI row, we see that the global minimum of J mix is attained by solving the convex reformulation, with the gradient ∇ J mix of the resulting policy nearly zero. Overall, when successful, all three methods ( ARE, PI, LMI ) yield almost identical solutions. Finally, the HIFOO solver is less reliable for smaller β, often triggering warnings or failing to return feasible solutions. Even at β = 18, its performance (especially the H ∞ norm) deviates noticeably from the other methods. This is expected as HIFOO relies on nonsmooth local optimization and does not guarantee global optimality. In contrast, our result in Theorem 3 ensures that stationary points found via gradient-based methods are globally optimal.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

We next consider three higher-dimensional examples, with policy matrices of sizes 15 × 15, 60 × 60, and 90 × 90, referred to as instances 1, 2, and 3, respectively. The problem data for the single-channel formulations are adapted from [24, Sec. 7.3]. For the two-channel formulations, we retain the same H ∞ performance signals but specify the H 2 performance with Q 2 = I and R 2 = 1 4 R ∞.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

Table 1 Comparison of different methods on Instance 0. Results for the two- and single-channel cases are shown under 2-ch and 1-ch subcolumns, respectively. A dash (-) indicates unavailable results. Bold values mark the best runtime among all methods.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

The minimum robustness level β ∗ for instances 1-3 are ≈ 0. 067, 0. 098, and 0. 096, respectively. Unlike the lowdimensional example (instance 0), our focus here is on assessing the scalability of different methods. Accordingly, we test larger robustness levels, setting β = 10, 15, and 20. One can verify that all assumptions are satisfied.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

Table 2 summarizes the results on the higher-dimensional examples. As shown in the ARE row, solving the Riccati equation remains highly efficient for the single-channel case, even at larger scales. The PI row demonstrates that the updates in remain effective as the problem size increases. Notably, the two-channel update (28b) converges across all instances, with the resulting policies exhibiting nearly vanishing gradients, which empirically supports our conjecture. This behavior suggests that (28b) enjoys an implicit regularization property, maintaining feasibility and achieving convergence when β is sufficiently large.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

The LMI row shows that the global minimum of J mix can be achieved by solving a convex reformulation. However, despite yielding policies with nearly zero gradients, the LMI method scales poorly: its runtimes for instance 2 and 3 are significantly longer than those of the analytical and policy iteration approaches. Overall, compared with the classical LMI-based methods, these results show that policy iteration can scale more favorably to large-scale problems.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we examine the nonconvex optimization landscape of mixed H 2 / H ∞ control. We characterize the feasible set and cost function, showing that despite nonconvexity, every stationary point is globally optimal. Our analysis, grounded in the ECL framework, further clarifies the role of strict versus non-strict Riccati inequalities in certifying global optimality and ensuring solvability of the convex reformulation. Several open questions are worth further investigation. An important one is to establish convergence guarantees for policy iteration in the general two-channel case, particularly for large β. Another is to design principled, scalable policy optimization algorithms for mixed H 2 / H ∞ design with provable performance guarantees.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Table 2 Comparison of different methods on Instance 1-3 (denoted I 1 -3 ). Results for two- and single-channel cases are shown under 2-ch and 1-ch subcolumns, respectively. A dash (-) indicates unavailable results. Bold values mark the best runtime.
