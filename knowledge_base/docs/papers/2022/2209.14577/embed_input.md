<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Rectified Flow: A Marginal Preserving Approach to Optimal Transport

Topics include Regression, Optimal transport, Flow, Ordinary differential equation, Convex function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a flow-based approach to the optimal transport (OT) problem between two continuous distributions pi_0, pi_1 on R^(d), of minimizing a transport cost E[c(X_1-X_0)] in the set of couplings (X_0, X_1) whose marginal distributions on X_0, X_1 equals pi_0, pi_1, respectively, where c is a cost function. Our method iteratively constructs a sequence of neural ordinary differentiable equations (ODE), each learned by solving a simple unconstrained regression problem, which monotonically reduce the transport cost while automatically preserving the marginal constraints. This yields a monotonic interior approach that traverses inside the set of valid couplings to decrease the transport cost, which distinguishes itself from most existing approaches that enforce the coupling constraints from the outside. The main idea of the method draws from rectified flow, a recent approach that simultaneously decreases the whole family of transport costs induced by convex functions c (and is hence multi-objective in nature), but is not tailored to minimize a specific transport cost.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our method is a single-object variant of rectified flow that guarantees to solve the OT problem for a fixed, user-specified convex cost function c.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Monge-Kantorovich (MK) optimal transport (OT) problem concerns finding an optimal coupling between two distributions π 0, π 1: where we seek to find (the law of) an optimal coupling (X 0, X 1) of π 0 and π 1, for which marginal laws of X 0, X 1 equal π 0, π 1, respectively, to minimize E [c (X 1 -X 0)], called the c -transport cost, for a cost function c. Theories, algorithms, and applications of optimal transport have attracted a vast literature; see, for example, the monographs of [PC + 19] for overviews. Notably, OT has been growing into a popular and powerful technique in machine learning, for key tasks such as learning generative models, transfer learning, and approximate inference [e.g., PC + 19].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The OT problem should be treated differently depending on whether π 0, π 1 are discrete or continuous measures. In this work, we focus on the continuous case when π 0, π 1 are high dimensional absolutely continuous measures on R d that are observed through empirical observations, a setting called data-driven OT. A well known result in OT [e.g.,] shows that, if π 0 is continuous, the optimization in can be restricted to the set of deterministic couplings satisfying X 1 = T (X 0) for some continuous transport mapping T: R d → R d, which is often approximated in practice with deep neural networks [e.g. KLG + 21].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, continuous OT remains highly challenging computationally. One major difficulty is to handle the coupling constraints of Law( X 0 ) = π 0 and Law( X 1 ) = π 1, which are infinite dimensional when π 0 and π 1 are continuous. As a result, can not be solved as a 'clean' unconstrained optimization problem. There are essentially two types of approaches to solving in the literature. One uses Lagrange duality to turn into a certain minimax game, and the other one approximates the constraint with an integral (often entropic-like) penalty function. However, the minimax approaches suffer from convergence and instability issues and are difficult to solve in practice, while the regularization approach can not effectively enforce the infinite-dimensional coupling constraints.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work We present a different approach to continuous OT that re-frames into a sequence of simple unconstrained nonlinear least squares optimization problems, which monotonically reduce the transport cost of a coupling while automatically preserving the marginal constraints. Different from the minimax and regularization approaches that enforce the constraints from outside, our method is an interior approach which starts from a valid coupling (typically the naive independent coupling), and traverses inside the constraint set to decrease the transport cost. Such an interior approach is non-trivial and has not been realized before, because there exists no obvious unconstrained parameterization of the set of couplings of π 0 and π 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method is made possible by leveraging rectified flow, a recent approach to constructing (nonoptimal) transport maps for generative modeling and domain transfer. What makes rectified flow special is that it provides a simple procedure that turns a given coupling into a new one that obeys the same marginal laws, while yielding no worse transport cost w.r.t. all convex functions c simultaneously. Despite this attractive property, as pointed out, rectified flow can not be used to optimize any fixed cost c, as it is essentially a special multi-objective optimization procedure that targets no specific cost. Our method is a variant of rectified flow that targets a user-specified cost function c and hence yields a new approach to the OT problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rectified flow We provide a high-level overview of the rectified flow of and the main results of this work. For a given coupling (X 0, X 1) of π 0 and π 1, the rectified flow induced by (X 0, X 1) is the time-differentiable process Z = { Z t: t ∈ } over an artificial notion of time t ∈, that solves the following ordinary differential equation (ODE): where v X: R d × → R d is a time-dependent velocity field defined as the solution of and X t is the linear interpolation between X 0 and X 1. Eq is a least squares regression problem of predicting the line direction of (X 1 -X 0) from every space-time point (X t, t) on the linear interpolation path, yielding a solution of which is the average of direction (X 1 -X 0) for all lines that pass point X t = z at time t. The (conditional) expectations E [·] above are w.r.t. the randomness of (X 0, X 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We assume that the solution of exists and is unique, and hence v X t (z) is assumed to exist at least on the trajectories of the ODE. The start-end pair (Z 0, Z 1) induced by Z is called the rectified coupling of (X 0, X 1), and we denote it by (Z 0, Z 1) = Rectify ((X 0, X 1)).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, the expectation E [ · ] is approximated by empirical observations of ( X 0, X 1 ), and v is approximated by a parametric family, such as deep neural networks. In this case, the optimization in Eq can be solved conveniently with off-the-shelf stochastic optimizers such as stochastic gradient descent (SGD), without resorting to minimax algorithms or expensive inner loops. This makes rectified flow attractive for deep learning applications as these considered.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The importance of (Z 0, Z 1) = Rectify ((X 0, X 1)) is justified by two key properties: 1) (Z 0, Z 1) shares the same marginal laws as (X 0, X 1) and is hence a valid coupling of π 0 and π 1; 2) (Z 0, Z 1) yields no larger convex transport costs than (X 0, X 1), that is, E [c (Z 1 -Z 0)] ≤ E [c (X 1 -X 0)], for every convex function c: R d → R.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, it is natural to recursively apply the Rectify mapping, that is, ( Z k +1 0, Z k +1 1 ) = Rectify (( Z k 0, Z k 1 )) starting from ( Z 0 0, Z 0 1 ) = ( X 0, X 1 ), yielding a sequence of couplings that is monotonically non-increasing in terms of all convex transport costs. The initialization can be taken to be the independent coupling ( Z 0 0, Z 0 1 ) ∼ π 0 × π 1, or any other couplings that can be constructed from marginal (unpaired) observations of π 0 and π 1. In practice, each step of Rectify is empirically approximated by first drawing samples of ( Z k 0, Z k 1 ) from the ODE with drift v k, and then constructing the next flow v k +1 from the optimization. Although this process accumulates errors, it was shown that one or two iterations are sufficient for practical applications.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the Rectify procedure is 'cost-agnostic' in that it does not dependent on any specific cost c. Although the recursive Rectify update is monotonically non-increasing on the transport cost for all convex c, it does not necessarily converge to the optimal coupling for any pre-specified c, as the update would stop whenever two cost functions are conflicting with each other. In, a coupling (X 0, X 1) is called straight if it is a fixed point of Rectify, that is, (X 0, X 1) = Rectify ((X 0, X 1)). It was shown that rectifiable couplings that are optimal w.r.t. a convex c must be straight, but the opposite is not true in general. One exception is the one dimension case (d = 1), for which all convex functions c (whose c -optimal coupling exists) share a common optimal coupling that is also straight. But this does not hold when d ≥ 2. c -Rectified flow In this work, we modify the Rectify procedure so that it can be used to solve given a user-specified cost function c.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that this can be done easily by properly restricting the optimization domain of v and modifying the loss function. The case of quadratic loss c (x) = 1 2 ‖ x ‖ 2 is particularly simple, for which we simply need to restrict the v to be a gradient field v t = ∇ f t in the optimization of. For more general convex c, we need to restrict v to have a form of v t (x) = ∇ c ∗ (∇ f t (x)), with f minimizing the following loss function: where c ∗ denotes the conjugate function of c. Obviously when c (x) = 1 2 ‖ x ‖ 2, reduces to with v = ∇ f. The loss function in is closely related to Bregman divergence [e.g., BMD + 05] and the socalled matching loss [e.g.,].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We call Z = { Z t: t ∈ } that follows d Z t = ∇ c ∗ (∇ f t (Z t))d t with Z 0 = X 0 and f solving the c -rectified flow of (X 0, X 1), and the corresponding (Z 0, Z 1) the c -rectified coupling of (X 0, X 1), denoted as (Z 0, Z 1) = c -Rectify ((X 0, X 1)).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similar to the original rectified coupling, the c -rectified coupling ( Z 0, Z 1 ) also share the same marginal laws as ( X 0, X 1 ) and hence is a coupling of π 0 and π 1. In addition, ( Z 0, Z 1 ) yields no larger transport cost than ( X 0, X 1 ) w.r.t. c, that is, E [ c ( Z 1 -Z 0 )] ≤ E [ c ( X 1 -X 0 )]. But this only holds for the specific c that is used to define the flow, rather than all convex functions like Rectify.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

More importantly, recursively performing c -Rectify allows us to find c -optimal couplings that solve the OT problem. Under mild conditions, we have where ℓ ∗ X,c denotes the minimum value of the loss function, which provides a criterion of c -optimality of a given coupling without solving the OT problem. Moreover, when following the recursive update (Z k +1 0, Z k +1 1) = c -Rectify ((Z k 0, Z k 1)), the ℓ ∗ Z k,c is guaranteed to decay to zero with min k ≤ K ℓ ∗ Z k,c = O (1 /K).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation Let C 1 ( R d ) be the set of continuously differentiable functions f: R d → R, and C 1 c ( R d ) the functions in C 1 ( R d ) whose support is compact. For a time-dependent velocity field v: R d × → R, we write v t ( · ) = v ( x, t ) and use ˙ v t ( x ):= ∂v ( x, t ) and ∇ v t ( x ):= ∂ x v ( x, t ) to denote the partial derivative w.r.t. time t and variable x, respectively. We denote by C 2, 1 ( R d × ) the set of functions f: R d × → R that are second-order continuously differentiable w.r.t. x and first-order continuously differentiable w.r.t. t. In this work, an ordinary differential equation (ODE) d z t = v t ( z t )d t should be interpolated as an integral equation z t = z 0 + ∫ t 0 v t ( z t )d t. For x ∈ R d, ‖ x ‖ denotes the Euclidean norm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

We always write c ∗ as the convex conjugate of c: R d → R, that is, c ∗ ( x ) = sup y ∈ R d { x ⊤ y -c ( y ) }.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Random variables are capitalized (e.g., X,Y,Z ) to distinguish them with deterministic values (e.g, x, y, z ). Recall that an R d -valued random variable X = X ( ω ) is a measurable function X: Ω → R d, where Ω is an underlying sample space equipped with a σ -algebra F and a probability measure P. The triplet (Ω, F, P ) form the underlying probability space, which is omitted in writing in the most places. We use Law( X ) to denote the probability law of X, which is the probability measure L that satisfies L ( B ) = P ( { ω: X ( ω ) ∈ B } ) for all measurable sets on R d. For a functional F ( X ) of a random variable X, the optimization problem min X F ( X ) technically means to find a measurable function X ( ω ) to minimize F, even though we omit the underlying sample space Ω. When F ( X ) depends on X only through Law( X ), the optimization problem is equivalent to finding the optimal Law( X ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outline The rest of the work is organized as follows. Section 2 introduces the background of optimal transport. Section 3 reviews rectified flow of from an optimization-based view. Section 4 characterizes the if and only if condition for two differentiable stochastic processes to have equal marginal laws. Section 5 introduces the main c -rectified flow method and establishes its theoretical properties.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Weintroduce rectified flow of from an optimization-based perspective: we show that rectified flow can be viewed as the solution of a special constrained dynamic optimization problem, which allows us to gain more understanding of rectified flow and motivates the development of c -rectified flow.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Following, for a time-differentiable stochastic process X = { X t: t ∈ }, its expected velocity field v X is defined as where ˙ X t denotes the time derivative of X t. Obviously, v X is the solution of where the optimization is on the set of all measurable velocity fields v: R d → R d. The importance of v X lies on the fact that it characterizes the time-evolution of the marginal laws ρ t:= Law(X t) of X, through the continuity equation in the distributional sense: Precisely, Equation should be interpreted by its weak and integral form: where ρ t (h):= ∫ h (x)d ρ t (x) and C 1 c (R d) denotes the set of continuously differentiable functions on R d with compact support. Hence, if the solution of Eq - is unique, then the marginal laws { Law(X t) } t of X are uniquely determined by v X and the initial Law(X 0).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

We define the rectified flow of X, denoted by Z = Rectflow (X), as the ODE driven by v X: Moreover, the rectified flow of a coupling (X 0, X 1) is defined as the rectified flow of X when X is the linear interpolation of (X 0, X 1).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Definition 3.1. A stochastic process X is called rectifiable if v X exists and is locally bounded, and Equation has an unique solution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

A coupling ( X 0, X 1 ) is called rectifiable if its linear interpolation process X, following X t = tX 1 +(1 -t ) X 0, is rectifiable. In this case, we call Z = Rectflow ( X ) the rectified flow of ( X 0, X 1 ), and write it (with an abuse of notation) as Z = Rectflow (( X 0, X 1 )). The corresponding ( Z 0, Z 1 ) is called the rectified coupling of ( X 0, X 1 ), denoted as ( Z 0, Z 1 ) = Rectify (( X 0, X 1 )).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

By the definition, we have v Z = v X, and hence the marginal laws Law( Z t ) of Z are governed by the same continuity equation -, which is a well known fact. As shown, Equation has an unique solution iff Equation has an unique solution, which implies that Z and X share the same marginal laws. We also assumed that the solution of is unique; if not, results in the paper hold for all solutions of.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Theorem 3.2 (Theorem 3.3 of). Assume that X is rectifiable. We have Hence, rectified flow turns a rectifiable stochastic process into a flow while preserving the marginal laws.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

A optimization view of rectified flow We show that the rectified flow Z of X achieves the minimum of the path-wise c -transport cost in the set of time-differentiable stochastic processes whose expected velocity field equals v X. This explains that the property of non-increasing convex transport costs of rectified flow/coupling.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Lemma 3.3. The rectified flow Z = Rectflow (X t) in attains the minimum of which holds for any convex functions c: R d → R.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Proof. For any stochastic process Y with v X t (z) = v Y t (z) = E [˙ Y t | Y t = z], we have Lemma 3.3 suggests that the rectified flow decreases the path-wise c -transport cost: F c (Z) ≤ F c (X), for all convex c. Note that E [c (Z 1 -Z 0)] ≤ F c (Z) by Jensen's inequality, and E [c (X 1 -X 0)] = F c (X) if X is the linear interpolation of (X 0, X 1). Hence, in this case, we have which yields a proof of Theorem 3.2 of that the rectified coupling (Z 0, Z 1) yields no larger convex transport costs than (X 0, X 1).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

A primal-dual relation Let us generalize the least squares loss L X (v) in to a a Bregman divergence based loss: where b c (·; ·) is the Bregman divergence w.r.t. c. The least squares loss L X is recovered with c (x) = 1 2 ‖ x ‖ 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Rectified flow can be alternatively implemented by minimizing ˜ L X,c with a differentiable strictly convex c, as in this case the minimum of ˜ L X,c is also attended by v X ( z ) = E [ ˙ X t | X t = z ]. The c -rectified flow is obtained if we minimize ˜ L X,c with v restricted to be a form of v = ∇ c ∗ ◦ ∇ f t. See more in Section 5.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

In the following, we show that the optimization in can be viewed as the dual problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Theorem 3.4. For any differentiable convex function c, and rectifiable process X, we have and the optima above are achieved when v = v X and Y = Rectflow (X).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Proof. Let var c (˙ X t | X t):= E [c (˙ X t) -c (E [˙ X t | X t]) | X t]. For any v, we have The inequality is tight when v = v X, which attains the minimum of ˜ L X,c.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Write R X,c (Y) = F c (X) -F c (Y). We know that Z = Rectify (X) attains the maximum of R X,c (Y) subject to v Y = v X by Lemma 3.3. In addition, This concludes the proof.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Straight couplings The ˜ ℓ ∗ X,c = ∫ 1 0 var c ( ˙ X t | X t )d t above provides a measure of how much the different paths of X intersect with each other. If c is strictly convex and ˜ ℓ ∗ X,c = 0, we have ˙ X t = E [ ˙ X t | X t ] almost surely, meaning that there exist no two paths that go across a point along two different directions. In this case, X is a fixed point of Rectflow ( · ), that is, X = Z = Rectify ( X ), because we have d X t = ˙ X t d t = E [ ˙ X t | X t ]d t = v X ( X t )d t, which is the same Equation that defines Z.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Similarly, if X is the linear interpolation of the coupling ( X 0, X 1 ), then ˜ ℓ ∗ X,c = 0 with strictly convex c if and only if ( X 0, X 1 ) is a fixed point of the Rectify mapping, that is, ( X 0, X 1 ) = Rectify (( X 0, X 1 )), following. Such couplings are called straight, or fully rectified. Obtaining straight couplings is useful for learning fast ODE models because the trajectories of the associated rectified flow Z are straight lines and hence can be calculated in closed form without iterative numerical solvers. See for more discussion.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Moreover, showed that rectifiable c -optimal couplings must be straight. In the one dimensional case ( d = 1 ), the straight coupling, if it exists, is unique and attains the minimum of E [ c ( X 1 -X 0 )] for all convex functions for which c -optimal coupling exists. For higher dimensions ( d ≥ 2 ), however, straight couplings are not unique, and the specific straight coupling obtained at the convergence of the recursive Rectify update (i.e. ( Z k +1 0, Z k +1 1 ) = Rectify (( Z k 0, Z k 1 )) ) is implicitly determined by the initial coupling ( Z 0 0, Z 0 1 ), and is not expected to be optimal w.r.t. any pre-fixed c.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

The following counter example shows a somewhat stronger negative result: there exist straight couplings that are not optimal w.r.t. all second order differentiable convex functions with invertible Hessian matrices.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Example 3.5. Take π 0 = π 1 = N (0, I ). Hence, for c ( x ) = ‖ x ‖ p with p > 0, the c -optimal mapping is the trivial identity coupling ( X 0, X 0 ) with X 0 ∼ π 0.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

However, consider the coupling ( X 0, AX 0 ), where A is a non-identity and non-reflecting rotation matrix (namely A ⊤ A = I, det( A ) = 1, A = I and A does not have λ = -1 as an eigenvalue). Then ( X 0, AX 0 ) is a straight coupling of π 0 and π 1, but it is not c -optimal for all second order differentiable convex function c whose Hessian matrix is invertible everywhere. See Appendix for the proof.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

It is the rotation transform that makes ( X 0, AX 0 ) sub-optimal, which is removed in the proposed c -rectified flow in Section 5 via a Helmholtz like decomposition.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

The marginal preserving property of rectified flow is due to the property of v Z = v X by construction. However, we show in this section that v X = v Z is only a sufficient condition: two differentiable processes X and Z can have the same marginal laws even if r:= v X -v Z = 0. This is because r, as illustrated in Example 3.5, can be a rotation-only vector field (in a generalized sense shown below) that introduces rotation components into the dynamics without modifying the marginal distributions. Therefore, the constraint of v Y = v X in the optimization problem may be too restrictive. A natural relaxation of would be which yields a dynamic OT problem with a continuum of marginal constraints. In Section 5, we show that the solution of yields our c -rectified flow that solve the OT problem at the fixed point. Solving allows us to remove the rotational components of v X, which is what what renders rectified flow non-optimal. In this section, we first characterize the necessary and sufficient condition for having equivalent marginal laws.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

Definition 4.1. A time-dependent vector field r: R d × → R d is said to be X -marginal-preserving if Equation is equivalent to saying that E [∇ h (X t) ⊤ r t (X t)] = 0 holds almost surely assuming that t is a random variable following Uniform (i.e., t -almost surely). Let ρ t = Law(X t) and it yields a density function ϱ t. Using integration by parts, we have which gives ∇ · (r t ϱ t) = 0. This says that r t ϱ t is a rotation-only (or divergence-free) vector field in the classical sense.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

Lemma 4.2. Let X and Y be two stochastic processes with the same initial distributions Law( X 0 ) = Law( Y 0 ). Assume that X is rectifiable, and v Y t ( z ):= E [ ˙ Y t | Y t = z ] exists and is locally bounded.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

Then X and Y share the same marginal laws at all time, that is, Law( X t ) = Law( Y t ), ∀ t ∈, if and only if v X -v Y is Y -marginal-preserving.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

Proof. Taking any h in C 1 c (R d), we have for t ∈ This suggests that the marginal law ρ t:= Law(X t) satisfies where we define ρ t (h) = ∫ h (x)d ρ t (x). Equation is formally written as the continuity equation: Similarly, ˜ ρ t:= Law(Y t) satisfies If v X t -v Y t is Law(Y t) -preserving for ∀ t ∈, we have which suggests that ˜ ρ t:= Law(Y t) solves the same continuity equation, starting from the same initialization as Law(X 0) = Law(Y 0). Hence, we have ρ t = ˜ ρ t if the solution of is unique, which is equivalent to the uniqueness of the solution of d Z t = v X t (Z t) in following Corollary 1.3 of.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

On the other hand, if ρ t = Law(X t) = Law(Y t) = ˜ ρ t, following and, we have for any h ∈ C 1 c (R d), which is the definition of Y -marginal-preserving following.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Rectified Flow", "weight": 1.0} -->

We introduce c -rectified flow, a c -dependent variant of rectified flow that guarantees to minimize the c -transport cost when applied recursively. This section is organized as follows: Section 5.1 defines and discusses the c -rectified flow of a differentiable stochastic process X, which we show yields the solution of the infinite-marginal OT problem. Section 5.2 considers the c -rectified flow of a coupling ( X 0, X 1 ), which we show is non-increasing on the c -transport cost. Section 5.3 proves that the fixed points of c -Rectify are c -optimal. Section 5.4 interprets c -rectified flow as an alternating direction descent method for the dynamic OT problem, and a majorize-minimization (MM) algorithm for the static OT problem. Section 5.5 discusses a key lemma relating c -optimal couplings and its associated displacement interpolation with Hamilton-Jacobi equation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

For a convex cost function c: R d → R and a time-differentiable process X, the c -rectified flow of X, denoted as Z = c -Rectflow (X), is defined as the solution of where c ∗ (x):= sup y { x ⊤ y -c (y) } is the convex conjugate of c, and f X,c: R d × → R is the optimal solution of where m c: R d × R d → [0, + ∞) is a loss function defined as Note that we have m c (x; y) ≥ 0 for ∀ x, y following the definition of the conjugate c ∗ (or the Fenchel-Young inequality). Losses of form m c (x; y) is equivalent to the so called matching loss proposed for learning generalized linear models.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Compared with the original rectified flow, the difference of c -rectified flow is i) restricting the velocity field to a form of g t = ∇ c ∗ ◦ ∇ f t, and ii) replacing the quadratic objective function to the matching loss. These two changes combined yield a Helmholtz like decomposition of v X as we show below, allowing us to remove the 'rotation-only' component of v X and obtain c -optimal couplings at fixed points.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Bregman divergence, Helmholtz decomposition, marginal preserving We can equivalently write using Bergman divergence associated with c, that is, Then it is easy to see that m c (x; y) = b c (x; ∇ c ∗ (y)), by using the fact that ∇ c (∇ c ∗ (y)) = y and c ∗ (y) = y ⊤ ∇ c ∗ (y) -c (∇ c ∗ (y)). Hence, m c and b c are equivalent up to the monotonic transform ∇ c ∗ on y. The minimum b c (x; y) = 0 is achieved when y = x, while m c (x; y) = 0 is achieved when ∇ c ∗ (y) = x.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Moreover, the generalized Pythagorean theorem of Bregman divergence (e.g., [BMD + 05]) gives Because v X (X t) = E [˙ X t | X t] and the last term of is independent with g t, we can further reframe into which can be viewed as projecting the expected velocity v X t to the set of functions of form g t = ∇ c ∗ ◦ ∇ f t, w.r.t. the Bregman divergence. This yields an orthogonal decomposition of v X t: where r X,c t = v X,c t - ∇ c ∗ ◦ ∇ f X,c t is the residual term. The key result below shows that r X,c is X -marginal-preserving, which ensures that the c -rectified flow preserves the marginals of X.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Definition 5.1. We say that X is c -rectifiable if v X exists, the minimum of exists and is attained by a locally bounded function f X,c, and the solution of Equation exists and is unique.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Theorem 5.2. Assume that X is c -rectifiable, and c ∗:= sup y { x ⊤ y -c (y) } and c ∗ ∈ C 1 (R d). We have i) v X -g X,c is X -marginal-preserving. ii) Z = c -Rectify (X) preserves the marginal laws of X, that is, Law(Z t) = Law(X t), ∀ t ∈.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Proof. i) By v X t (z) = E [˙ X t | X t = z], the loss function in is equivalent to By Euler-Lagrange equation, we have Taking g s = h if s < t and g s = 0 if s > t yields that r X,c (x) = ∇ c ∗ (∇ f X,c s (X s)) -v X (X s) is X -marginal-preserving following. ii) Note that Z is rectifiable if X is c -rectifiable. Applying Lemma 4.2 yields the result.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

For the quadratic cost c ( x ) = c ∗ ( x ) = 1 2 ‖ x ‖ 2, the ∇ c ∗ is the identity mapping, and reduces to the Helmholtz decomposition, which represents a velocity field into the sum of a gradient field and a divergencefree field. Hence, yields a generalization of Helmholtz decomposition, in which a monotonic transform ∇ c ∗ is applied on the gradient field component. We call a Bregman Helmholtz decomposition.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Remark: score matching In some special cases, v X may already be a gradient field, and hence the rectified flow and c -rectified flow coincide for c (x) = 1 2 ‖ x ‖ 2. One example of this is when X t = α t X 1 + β t ξ for some time-differentiable functions α t and β t, and ξ ∼ N (0, I), satisfying α 1 = 1, β 1 = 0, and X 0 = α 0 X 1 + β 0 ξ. In this case, one can show that where ϱ t is the density function of X t with ϱ t (z) ∝ ∫ φ (z -α t x 1 β t) d π 1 (x 1) and φ (z) = exp(-‖ z ‖ 2 / 2), and η t = β 2 t (˙ α t /α t -˙ β t /β t) and ζ t = ˙ α t /α t. This case covers the probability flow ODEs [SSDK + 20] and denoising diffusion implicit models (DDIM) with different choices of α t and β t as suggested.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

When ζ t = 0, as the case of, v X t is proportional to ∇ log ρ t, the score function of ϱ t, and the least squares loss L X (v) in reduces to a time-integrated score matching loss.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

However, v X t is generally not a score function or gradient function, especially in complicate cases when the coupling (X 0, X 1) is induced from the previous rectified flow as we iteratively apply the rectification procedure. In these cases, it is necessary to impose the gradient form as we do in c -rectified flow. c -Rectified flow solves Problem Weare ready to show that the c -rectified flow solves the optimization problem. Further, forms a dual problem of.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Theorem 5.3. Under the conditions in Theorem 5.2, we have i) Z = c -Rectify (X) attains the minimum of. ii) Problem and has a strong duality: As the optima above are achieved by f X,c and Z, we have L X,c (f X,c) = F c (X) -F c (Z).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Rectified Flow of Time-Differentiable Processes X", "weight": 1.0} -->

Proof. Write R X,c (Y) = F c (X) -F c (Y). First, we show that L X,c (f) ≥ R X,c (Y) for any f and Y that satisfies Law(Y t) = Law(X t), ∀ t: Moreover, if we take Y = Z and f = f X,c, then the inequality in ≤ is tight because ˙ Z t = ∇ c ∗ (∇ f t (Y t)) holds t -almost surely. Therefore, R X,c (Z) = L X,c (f X,c) ≥ R X,c (Y), which suggests that Z attains the maximum of R X,c (under the marginal constraints) and the strong duality holds.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Rectified Flow of Coupling ( X 0, X 1 )", "weight": 1.0} -->

Similar to the case of rectified flow, the c -rectified flow/coupling of a coupling ( X 0, X 1 ) is defined as the c -rectified flow/coupling of its linear interpolation process. In the following, we show that the c -rectified coupling of a coupling yields no larger c -transport cost.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Rectified Flow of Coupling ( X 0, X 1 )", "weight": 1.0} -->

Definition 5.4. Let X be the linear interpolation of coupling ( X 0, X 1 ) in that X t = tX 1 +(1 -t ) X 0, ∀ t ∈. We say that ( X 0, X 1 ) is c -rectifiable if X is c -rectifiable, and call Z = c -Rectflow ( X ) the c -rectified flow of ( X 0, X 1 ). We call the induced ( Z 0, Z 1 ) the c -rectified coupling of ( X 0, X 1 ), denoted as ( Z 0, Z 1 ) = c -Rectify (( X 0, X 1 )).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Rectified Flow of Coupling ( X 0, X 1 )", "weight": 1.0} -->

Note that the c -transport cost E [c (X 1 -X 0)] is related to the path-wise c -transport cost F c (X) via where S c (X) is a non-negative measurement of how close X is to be geodesic: We have S c (X) ≥ 0 following Jensen's inequality ∫ 1 0 c (˙ X t)d t ≥ c (∫ 1 0 ˙ X t d t) = c (X 1 -X 0), and S c (X) = 0 if X t = tX 1 + (1 -t) X 0.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Rectified Flow of Coupling ( X 0, X 1 )", "weight": 1.0} -->

Hence, when X is the linear interpolation of (X 0, X 1), we have from Theorem 5.3 that which establishes that (Z 0, Z 1) yields no larger transport cost than (X 0, X 1).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Rectified Flow of Coupling ( X 0, X 1 )", "weight": 1.0} -->

Theorem 5.5. Assume that c is convex with conjugate c ∗ ∈ C 1 ( R d ), and the conditions in Definition 5.4 holds. Then Equation holds and E [ c ( Z 1 -Z 0 )] ≤ E [ c ( X 1 -X 0 )].

<!-- chunk {"id": "body-0071", "role": "body", "section": "Rectified Flow of Coupling ( X 0, X 1 )", "weight": 1.0} -->

Compared with the regular Rectify mapping, the key difference here is that the monotonicity of c -Rectify only holds for the specific c that it employees, rather than all convex cost functions. More importantly, as we show below, recursively applying c -Rectify yields optimal couplings w.r.t. c, a key property that the regular rectified flow misses.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Fixed Points of c -Rectify are c -Optimal", "weight": 1.0} -->

- 1) A coupling (X 0, X 1) is a fixed point of c -Rectify, that is, (X 0, X 1) = c -Rectify ((X 0, X 1)), if and only if it is c -optimal; - 2) Define ℓ ∗ X,c = inf f L X,c (f) where X is the linear interpolation of (X 0, X 1). Then ℓ ∗ X,c yields an indication of c -optimality of (X 0, X 1), that is, L ∗ X,c = 0, iff (X 0, X 1) is c -optimal. - 3) The minimum ℓ ∗ X,c in the first k iterations of c -Rectify steps decreases with an O (1 /k) rate.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Fixed Points of c -Rectify are c -Optimal", "weight": 1.0} -->

Theorem 5.6. Assume that c is convex with conjugate c ∗, and c, c ∗ ∈ C 1 (R d) and X is the linear interpolation process of (X 0, X 1). Assume that (X 0, X 1) is a c -rectifiable coupling, and f X,c ∈ C 2, 1 (R d ×). Then the following statements are equivalent: i) (X 0, X 1) is a fixed point of c -Rectify, that is, (X 0, X 1) = c -Rectify (X 0, X 1). iii) (X 0, X 1) is a c -optimal coupling.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Fixed Points of c -Rectify are c -Optimal", "weight": 1.0} -->

Proof. i) → ii). If (Z 0, Z 1) = (X 0, X 1), we have S c (Z) = 0 and L X,c (f X,c) = 0 following. iii) → ii). If (X 0, X 1) is c -optimal, we have E [c (X 1 -X 0)] ≤ E [c (Z 1 -Z 0)], which again implies that L X,c (f X,c) = 0 following.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Fixed Points of c -Rectify are c -Optimal", "weight": 1.0} -->

Therefore, L X,c (f X,c) = 0 implies that ˙ X t = g X,c t (X t) t -almost surely. Because Z t satisfies the same equation, whose solution is assumed to be unique, we have Z = X and hence (Z 0, Z 1) = (X 0, X 1). ii) → iii) Because X is the linear interpolation, we have X t = tX 1 + (1 -t) X 0, and it simultaneously satisfies the ODE d X t = g X,c t (X t)d t. Using Lemma 5.9 shows that (X 0, X 1) is c -optimal.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Fixed Points of c -Rectify are c -Optimal", "weight": 1.0} -->

Knowing that L X,c ( f X,c ) is an indication of c -optimality, we show below that it is guaranteed to converge to zero with recursive Rectify updates.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Fixed Points of c -Rectify are c -Optimal", "weight": 1.0} -->

Corollary 5.7. Let Z k be the k -th c -rectified flow of (X 0, X 1), satisfying Z k +1 = c -Rectflow ((Z k 0, Z k 1)) and (Z 0 0, Z 0 1) = (X 0, X 1). Assume each (Z k 0, Z k 1) is c -rectifiable for k = 0,..., K. Then Therefore, if E [c (X 1 -X 0)] < + ∞, we have min k ≤ K L Z k,c (f Z k,c) + S c (Z k +1) = O (1 /K).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

In this section, we draw more understanding on how iterative c -rectified flowing solves the static and dynamic OT problems. We first show that c -rectified flow can be viewed as an alternative direction descent on the dynamic OT problem, and then that c -rectified coupling as a majorize-minimization (MM) algorithm on the statistic OT problem. The results in this section are framed in terms of a general path-wise loss function F c (Y), and hence provide a useful starting point for deriving c -rectified flow like approaches to more general optimization problems with coupling constraints. c -Rectified flow as alternative direction descent on The mapping Z k +1 = c -Rectflow (Z k) can be interpreted as an alternative direction descent procedure for the dynamic OT problem: Here, we minimize F c (Y) in the set of processes whose start-end pair (Y 0, Y 1) equals the coupling (Z k 0, Z k 1) from Z k, which simply yields the linear interpolation X k t = tZ k 1 +(1 -t) Z k 0 by Jensen's inequality.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

In, we minimize F c (Y) given the path-wise marginal constraint of Law(Y t) = Law(X k t) for all time t ∈, which yields the c -rectified flow following Theorem 5.3. Note that the updates in both and keep the start-end marginal laws Law(Y 0) and Law(Y 1) unchanged, and hence the algorithm stays inside the feasible set { Y: Law(Y 0) = π 0, Law(Y 1) = π 1 } in once it is initialized to be so.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

The updates in - highlight a key difference between our method and the Benamou-Brenier approach -: the key idea of Benamou-Brenier is to restrict the optimization domain to the set of deterministic, ODE-induced processes (a.k.a. flows), but our updates alternate between the deterministic c -rectified flow Z k and the linear interpolation process X k, which is not deterministic or ODE-inducable unless the fixed point is achieved. c -Rectified flow as an MM algorithm The majorize-minimization (MM) algorithm is a general optimization recipe that works by finding a surrogate function that majorizes the objective function. Let F (X) be the objective concave function to be minimize.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

An MM algorithm consists of iterative update of form X k +1 ∈ arg min Y F + (Y | X k), where F + is a majorization function of F that satsifies In this case, the MM update guarantees that F (X k) is monotonically non-increasing: One can also view MM as conducting coordinate descent on (X,Y) for solving min X,Y F + (Y | X).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

In the following, we show that (Z k +1 0, Z k +1 1) = c -Rectify ((Z k 0, Z k 1)) can be interpreted as an MM algorithm for the static OT problem for minimizing E [c (X 1 -X 1)] in the set of couplings of π 0 and π 1. The majorization function corresponding to c -Rectify can be shown to be where F + c ((Y 0, Y 1) | (X 0, X 1)) denotes the minimum value of F c (˜ Y) for ˜ Y whose start-end points equal (Y 0, Y 1), and yields the same marginal laws as that of the linear interpolation process of (X 0, X 1).

<!-- chunk {"id": "body-0083", "role": "body", "section": "Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

Proposition 5.8. i) F + c yields a majorization function of the c -transport cost E [c (Y 1 -Y 0)] in the sense that and the minimum is attained by (X 0, X 1) = (Y 0, Y 1), where Π 0, 1 denotes the set of couplings of π 0 and π 1. ii) c -Rectify yields the MM update related F + in that Proof. i) For any coupling (X 0, X 1) and (Y 0, Y 1), we have where the inequality holds because remove the constraint Y ∈ M X. In addition, it is obvious that the inequality above becomes equality when (X 0, X 1) = (Y 0, Y 1).

<!-- chunk {"id": "body-0084", "role": "body", "section": "Note that", "weight": 1.0} -->

whose minimum of the right side is attained by Y = c -Rectflow (( X 0, X 1 )) following Theorem 5.3. Hence, the minimum of the left side is attained by ( Y 0, Y 1 ) = c -Rectify (( X 0, X 1 )).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

The proof of Theorem 5.6 relies on a key lemma shows that if the trajectories of an ODE of form d X t = ∇ c ∗ ( ∇ f t ( X t ))d t are geodesic in that X t = tX 1 +(1 -t ) X 0, then the induced coupling ( X 0, X 1 ) is an c -optimal coupling of its marginals. The proof of this lemma relies on Hamilton-Jacobi (HJ) equation, which provides a characterization of f for an ODE d X t = ∇ c ∗ ( ∇ f t ( X t ))d t whose trajectories are geodesic. The connection between HJ equation and optimal transport has been a classic result and can be found, for example,.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

Lemma5.9. Let v t (x) = ∇ c ∗ (∇ f t (x)) where c ∗ ∈ C 1 (R d) is a convex function c, and f ∈ C 2, 1 (R d ×) and ∇ c ∗ is an injective mapping. Assume all trajectories of d x t = v t (x t)d t are geodesic paths in that x t = tx 1 +(1 -t) x 0. Then we have: i) There exists ˜ f t such that ∇ ˜ f t = ∇ f t (and hence we can replace f with ˜ f in the assumption), such that the following Hamilton-Jacobi (HJ) equation holds where the minimum is attained if { y t } follows the ODE d y t = v t (y t)d t. iii) Assume a coupling (X 0, X 1) of π 0, π 1 satisfies d X t = v t (X t)d t. Then (X 0, X 1) is a c -optimal coupling.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

Proof. i) Starting from any point x t = x ∈ R d at time t, because the trajectories of d x t = v t (x t)d t are geodesic, we have ˙ x t = v t (x t) = const following the trajectory. Because v t (x) = ∇ c ∗ (∇ f t (x)) and ∇ c ∗ is injective, we have ∇ f t (x t) = const as well. Hence, we have On the other hand, define h t (x) = ∂ t f t (x) + c ∗ (∇ f t (x)). Then we have This suggests that ∇ x h t (x) = 0 everywhere and hence h t (x) does not depend on x. Define ˜ f t (x) = f t (x) -∫ t 0 h t (x 0)d t, where x 0 is any fixed point in R d. Then ii) Take any y 0, y 1 in R d, let y t = ty 1 +(1 -t) y 0 be their linear interpolation.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

We have The equality in ≤ is attained if y t follows the geodesic ODE d y t = v t (y t)d t as we have y 1 -y 0 = ∇ c ∗ (∇ f t (y t)), ∀ t in this case. A similar derivation holds for f t. iii) Note that i) gives that c (y 1 -y 0) ≥ f 1 (y 1) -f 0 (y 0). For any coupling (Y 0, Y 1) of π 0, π 1, we have Hence, (X 0, X 1) is a c -optimal coupling.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

Connection to Benamou-Brenier Formula The results in Lemma 5.9 can also formally derived from Benamou-Brenier problem, as shown in the seminal work of. By introducing a Lagrangian multiplier λ: R d × → R for the constraint of ˙ ϱ t + ∇· (v t ϱ t) = 0, the problem in can be framed into a minimax problem: where L (v, ϱ, λ) is the Lagrangian function, and Γ 0, 1 denotes the set of density functions { ϱ t } t satisfying ϱ 0 = d π 0 / d x, ϱ 1 = d π 1 / d x. Note that the following integration by parts formulas: where we assume that λ t v r ρ t decays to zero sufficiently fast at infinity. We have At the saddle points, the functional derivations of L equal zero, yielding Assume ϱ t is positive everywhere and note that ∇ c ∗ (∇ c (x)) = x, we have v t = ∇ c ∗ (∇ λ t), and hence ∇ λ ⊤ t v t -c (v t) = c ∗ (∇ λ t).

<!-- chunk {"id": "body-0090", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

Plugging it back to δ L δρ t = 0 yields that ˙ λ t + c ∗ (∇ λ t) = 0. Overall, the (formal) KKT condition of is This matches the result in Lemma 5.9 with λ t = ˜ f t.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

1. Corollary 5.7 only bounds the surrogate measure ℓ ∗ Z k,c. Can we directly bound the optimality gap on the c -transport cost e ∗ k = E [c (Z k 1 -Z k 0)] -inf (Z 0,Z 1) E [c (Z 1 -Z 0)] ? Can we find a certain type of strong convexity like condition, under which e ∗ k decays exponentially with k ? 2. For machine learning (ML) tasks such as generative models and domain transfer, the transport cost is not necessarily the direct object of interest. In these cases, as suggested, rectified flow might be preferred because it is simpler and does not require to specify a particular cost c. Question: for such ML tasks, when would it be preferred to use OT with a specific c, and how to choose c optimally? 3. In practice, recursively applying the (c -)rectification accumulates errors because the training optimization for the drift field and the simulation of the ODE can not be conducted perfectly. How to avoid the error accumulation at each step?

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

Assume { x 1,i } i ∼ π 1, and { z k 0,i, z k 1,i } i is obtained by solving the ODE of the k -th c -rectified flow starting from z k 0,i ∼ π 0. As we increase k, { z k 0,i } i may yield increasingly bad approximation of π 1 due to the error accumulation. One way to fix this is to adjust { z k 1,i } to make it closer to { x k 1,i } i at each step. This can be done by reweighting/transporting { z k 1,i } i towards { x k 1,i } i by minimizing certain discrepancy measure, or replacing each z k 1,i with x k σ (i) where σ is a permutation that yields a one-to-one matching between { z (i) 1 } and { x (i) 1 } i. The key and challenging part is to do the adjustment in a good and fast way, ideally with a (near) linear time complexity. 4. With or without the adjustment step, build a complete theoretical analysis on the statistical error of the method.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

5. In what precise sense is rectified flow solving a multi-objective variant of optimal transport?
