<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Solutions to Non-Convex Functional Constrained Problems with Hidden Convexity

Topics include Convex optimization, Reinforcement learning, Safety, Online algorithms, Optimization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Constrained non-convex optimization is fundamentally challenging, as global solutions are generally intractable and constraint qualifications may not hold. However, in many applications, including safe policy optimization in control and reinforcement learning, such problems possess hidden convexity, meaning they can be reformulated as convex programs via a nonlinear invertible transformation. Typically such transformations are implicit or unknown, making the direct link with the convex program impossible. On the other hand, (sub-)gradients with respect to the original variables are often accessible or can be easily estimated, which motivates algorithms that operate directly in the original (non-convex) problem space using standard (sub-)gradient oracles. In this work, we develop the first algorithms to provably solve such non-convex problems to global minima. First, using a modified inexact proximal point method, we establish global last-iterate convergence guarantees with O~(epsilon^(-3)) oracle complexity in non-smooth setting. For smooth problems, we propose a new bundle-level type method based on linearly constrained quadratic subproblems, improving the oracle complexity to O~(epsilon^(-1)).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Surprisingly, despite non-convexity, our methodology does not require any constraint qualifications, can handle hidden convex equality constraints, and achieves complexities matching those for solving unconstrained hidden convex optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Non-convex constrained optimization problems (with possibly non-smooth objectives and constraints) arise frequently in many modern applications. In this work, we study a sub-class of non-convex problems of the form where X ⊂ R d is a closed convex set, and F 1, F 2 are possibly non-convex with respect to variable x. 1 A central running assumption in this work is that problem admits a convex reformulation via variable change: u = c (x), where H 1, H 2 are convex functions defined over a closed convex set U ⊂ R d, and c: X → U is an invertible map (with c -1 denoting its inverse). 2 This property, often referred to as hidden convexity, appears in diverse applications, including policy optimization in optimal control [; ADL+19] and reinforcement learning [ZKB+20 YGL+24], variational inference, generative models, supply chain and revenue management [; CHH+25], geometric programming, neural network training, and non-monotone games [; MSG+22; SVM+23; DVL+25], to name just a few.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Figure 1 provides illustrative examples of constrained hidden convex problems, which we will cover in more detail in Section 5.1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ilyas Fatkhullin: ilyas.fatkhullin@ai.ethz.ch, Niao He: niao.he@inf.ethz.ch, Guanghui Lan: george.lan@isye.gatech.edu, Florian Wolf: fwolf@caltech.edu Although the reformulation in is convex, in practice, the transformation c ( · ) is often either difficult to compute or entirely unknown [; YGL+24]. Consequently, solving the convex reformulation and recovering the solution to is generally impossible. On the other hand, directly solving the non-convex problem using the standard (sub-)gradient methods is a well-established practice, which may already lead to approximate global solutions. A recent work justifies the use of (sub-)gradient methods applied to the hidden convex problem in the special case without functional constraint ( F 2 ( · ) ≡ 0 ). They establish global convergence of (sub-)gradient methods in the function value, i.e., F 1 ( x ( N ) ) -F ∗ 1 ≤ ε, in smooth and non-smooth setups.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

1 Department of Computer Science, ETH Zurich, Switzerland 2 ETH AI Center, ETH Zurich, Switzerland. 3 Department of Industrial and Systems Engineering, Georgia Institute of Technology, Atlanta, GA. 4 The Computing & Mathematical Sciences Department, California Institute of Technology, Pasadena, CA.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

1 We assume F 2 is scalar-valued, but our results are extendable to the vector-valued case.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

2 We show how the invertibility assumption can be relaxed in Section 2.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: Illustrative examples of non-smooth (top) and smooth (bottom) hidden convex problems: (a) and (b) Constrained Non-Linear Least Squares; (c) and (d) Constrained Geometric Programming, see (Ex-CNLS) and (Ex-CGP) in Section 5.1 for details. The plots illustrate in color the level sets of the non-convex formulation (left) and the convex formulation (right). The feasible sets are shown as gray regions: { F 2 ≤ 0 } in the X -domain, and { H 2 ≤ 0 } in the U -domain. We use the notation x ∗ uncon to denote the optimum of min x F 1 ( x ) without constraints and x ∗ the minimizer under constraints; analogously, u ∗ uncon and u ∗ denote their counterparts in U.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the presence of functional constraints significantly complicates the analysis. First, extending the standard schemes from convex optimization (such as primal-dual, switching (sub-)gradient, bundle level) seems challenging, and we are not aware of satisfactory analysis under hidden convexity in the literature. Second, the direct application of convergence guarantees for general non-convex (or weakly convex) constrained optimization to our problem yields rather weak guarantees of reaching merely an approximate Karush-Kuhn-Tucker (KKT) point under strong constraint qualification (CQ) assumptions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. To address these challenges, we explore two distinct approaches based on (i) the proximal point framework and (ii) a bundle-level idea. In both cases, we design algorithms suitable for our hidden convex problems using only the oracle access to (sub-)gradients and function values of F 1, F 2, which allows us to establish the first guarantees to find an ( ε, ε ) -approximate global minima of, i.e., F 1 ( x ( N ) ) -F ∗ 1 ≤ ε and F 2 ( x ( N ) ) ≤ ε.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

- (C1) Constrained Proximal Point Approach. We propose a modified Inexact Proximal Point Method (IPPM) with shifted constraints under hidden convexity. The key technical novelty of our convergence analysis lies in showing that our IPPM subproblems always satisfy Slater's condition without imposing any CQs on the original problem. In our analysis, a Slater point is explicitly constructed using the variable transformation c (x). Using this key insight, we apply existing algorithms for strongly convex constrained optimization to approximate each IPPM subproblem using the standard (sub-)gradient oracle access. In particular, in the non-smooth setting, we use the Switching Sub-Gradient (SwSG) method as an inner solver to derive ˜ O (ε -3) oracle complexity without any CQs. In the smooth setting, we use the Accelerated Constrained Gradient Descent (ACGD) method, achieving ˜ O (ε -2) (or ˜ O (θ -1 ε -1)) oracle complexity without any CQs (or with θ -Slater's condition). We refer to Tables 1 and 2 for a summary. - (C2) Bundle-level Approach.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To improve the complexity in the smooth case when Slater's condition may not hold, we propose a new Shifted Bundle-level method. The main algorithmic novelty is a carefully selected shift of the linear constraints at each subproblem, which allows convergence of the algorithm even without convexity in the X space. When the optimal value of the constrained problem F ∗ 1 is available, we design a Shifted Star Bundle-level algorithm (S-StarBL), which attains ˜ O (ε -1) oracle complexity without any CQs. In the setting when F ∗ 1 is unknown, we invent an adaptive line-search procedure involving an exact penalty as the convergence criterion. The resulting scheme (referred to as S-BL+AdaLS) achieves the ˜ O (λ ∗ ε -1) complexity under strong duality, where λ ∗ is the optimal dual variable. We refer to Table 2 for a summary.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both approaches modify classical convex optimization methods to handle hidden convexity using shifts in the constraints, and both are the first to achieve global optimality guarantees for such problems. Our IPPM approach relies on regularization, ensuring feasibility through an explicit Slater point construction and achieving reliable convergence under minimal assumptions. In contrast, the Bundle-level method adopts a cutting-plane strategy with shifted constraints, attaining a faster ˜ O (ε -1) complexity for smooth problems without Slater's condition, requiring only the weaker strong duality assumption. We also validate our methods on a non-smooth constrained non-linear least squares, and on a smooth geometric programming problem in Section 5. 3 Table 1: Summary of total sub-gradient and function evaluation complexities for sub-gradient methods under hidden convexity in the non-smooth setup. The 'Setting' column distinguishes between unconstrained (F 2 (·) ≡ 0) and constrained (F 2 (·) ̸≡ 0) problems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The third column reports the number of sub-gradient (and function, when F 2 (·) ̸≡ 0) evaluations in ˜ O (·) notation to find a point x (N) such that F 1 (x (N)) -F ∗ 1 ≤ ε, F 2 (x (N)) ≤ ε. The complexity of SM is stated in terms of the Moreau envelope and suffers a loss in complexity when translated to the original objective in the non-smooth setting, see the discussion after Corollary 1 therein. 'IPPM' stands for Inexact Proximal Point Method, and 'SwSG' for Switching Sub-Gradient.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

| Setting | Method | Complexity | 3 The source code for the numerical experiments and illustrations is publicly available under.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations and Standard Assumptions", "weight": 1.0} -->

In the following, we briefly revisit some basic notation. Throughout this work, we define [ N ]:= { 0,..., N } for N ∈ N. We denote with ⟨ ·, · ⟩, the inner product in R d along with its induced Euclidean norm ∥ · ∥ = ∥ · ∥ 2, where d ∈ N indicates the ambient dimension. We call the map c: X → U invertible if there exists a map c -1: U → X, called inverse, with c -1 ( c ( x )) = x and c ( c -1 ( u )) = u for all x ∈ X and u ∈ U respectively. The set U ⊂ R d is called convex if for all u, v ∈ U, and α ∈ we have (1 -α ) u + αv ∈ U, and with D U:= sup u,v ∈U ∥ u -v ∥ we denote its diameter. To deal with properties of the objective and the constraints simultaneously, we use i = 1, 2 to simplify notation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Notations and Standard Assumptions", "weight": 1.0} -->

If for a function H i: U → R there exists µ H i ≥ 0 such that for all u, v ∈ U and α ∈ it holds H i ((1 -α ) u + αv ) ≤ (1 -α ) H i ( u ) + αH i ( v ) -(1 -α ) αµ Hi 2 ∥ u -v ∥ 2 we call H i strongly convex if µ H i > 0 and convex if µ H i = 0 on U respectively. With R d > 0 we denote the set { x ∈ R d | x i > 0, i = 1,..., d }. For a convex set X ⊂ R d and a point y ∈ R d we denote with Π X ( y ):= min x ∈X ∥ y -x ∥ its projection onto X; by δ X we denote the indicator function, i.e., δ X ( x ) = 0 if x ∈ X and δ X ( x ) = ∞ otherwise. The relative interior of X is denoted by relint ( X ).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Notations and Standard Assumptions", "weight": 1.0} -->

A function F: X → R is called ρ -weakly convex ( ρ -WC) if for any fixed y ∈ X, the function F ρ ( x, y ):= F ( x ) + ρ 2 ∥ x -y ∥ 2 is convex in x ∈ X. The (Fréchet) sub-differential of F in x ∈ X is ∂F ( x ):= { g ∈ R d | F ( y ) ≥ F ( x ) + ⟨ g, y -x ⟩ + o ( ∥ y -x ∥ ), ∀ y ∈ R d }, with its elements g ∈ ∂F ( x ) being called sub-gradients of F at x ∈ X. We refer to for equivalent definitions of the subdifferential set of ρ -WC functions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Notations and Standard Assumptions", "weight": 1.0} -->

A differentiable function F: X → R is L -smooth on X ⊂ R d if its gradient is L -Lipschitz continuous on the set X, i.e., it holds ∥∇ F ( x ) - ∇ F ( y ) ∥ ≤ L ∥ x -y ∥ for all x, y ∈ X. For a constraint F 2: X → R and a budget b ∈ R, we use the following short notation { F 2 ≤ b }:= { x ∈ X | F 2 ( x ) ≤ b } to denote the corresponding feasible set, usually b = 0. We use O ( · ) notation to hide all dependencies except for the final accuracy ε and ˜ O ( · ) to hide additional logarithmic terms in 1 /ε.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Notations and Standard Assumptions", "weight": 1.0} -->

The following standard assumptions will be used throughout the paper. More specific assumptions related to the problem structure will be introduced in the subsequent section.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1 We assume", "weight": 1.0} -->

1. The functions F 1, F 2 are ρ -weakly convex. 2. The functions F 1, F 2 are continuous and satisfy for all x ∈ X that ∂F 1 (x) = ∅, ∂F 2 (x) = ∅ on X, and the norms of the sub-gradients are uniformly bounded by ∥ g 1 ∥ ≤ G F 1, ∥ g 2 ∥ ≤ G F 2 for all x ∈ X, g 1 ∈ ∂F 1 (x) and g 2 ∈ ∂F 2 (x) respectively. We define G:= max { G F 1, G F 2 }. 3. The domain U has bounded diameter D U > 0.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

The existence of a convex reformulation for the problem motivates its representation as a compositional optimization problem in the form: under a consistent transformation function, c (·), for both the objective and the constraint. Now we introduce the central definition of this work, which postulates the existence of an (unknown) transformation c (·) and its properties.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

Definition 1 (Hidden Convexity 4) The above problem (HC) is called hidden convex with modulus µ c > 0, if its components satisfy the following underlying conditions. 1. The domain U = c (X) is convex, the functions H 1, H 2: U → R are convex, i.e. satisfy for i = 1, 2 and for all u, v ∈ U and any λ ∈ Additionally, we assume (HC) admits a solution u ∗ ∈ U with its corresponding objective function value F ∗ 1:= H 1 (u ∗) = F 1 (c -1 (u ∗)). 2. The map c: X → U is invertible and there exists a µ c > 0 such that for all x, y ∈ X it holds Note that the condition (HC-2) along with Assumption 1 (Item 3) imply that the domain X has bounded diameter D X ≤ 1 µ c D U. We refer to for necessary and sufficient conditions for (HC-2).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

In particular, for continuously differentiable transformations (HC-2) is equivalent to a uniformly bounded operator norm of the Jacobian of c -1 (·), i.e., ∥ J c -1 (u) ∥ op ≤ 1 /µ c for all u ∈ U. We must highlight the importance of the consistent transformation function c (·) for both the objective F 1 and the constraint F 2. If the transformations are inconsistent, the problem becomes intractable due to multiple isolated feasible points (cf. Section 2.3).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

Relaxing invertibility condition. Assuming the existence of an invertible map c ( · ) may sound limiting. Here we comment on possible relaxations of the invertibility of the transformation c ( · ).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

- Local Invertibility. The invertibility of c (·) can be relaxed to a local neighborhood V x around each x ∈ X, where c (·) is a bijection between V x and W c (x):= c (V x). This allows us to relax the Item 2 of Definition 1 as invertibility is only required locally. By carefully examining the proofs of Theorems 2 to 4, we find that we only require an ¯ α such that for all α ∈ [0, ¯ α], the combination (1 -α) c (x) + αc (x ∗) ∈ W c (x) for all x ∈ X. An example of this relaxation appears in the context of (CCMDP) problem, cf. [ZNY+21, Ass. 5.11], [YGL+24, Ass. 2]. - Generalized Inverse of Non-linear Transformations. Another possible relaxation is to use the generalized inverse of a non-linear mapping introduced by Gofer and Gilboa, which generalizes the well-known notion of pseudoinverse of a linear map due to Penrose.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

Following their Definition 3, the non-linear generalized inverse c †: U → X of the map c (·) is defined as: 4 Definition 1 can be extended to hidden strong convexity, cf. Definition 4 in the Appendix, for which we will show additional results in Section B.1, but for the sake of clarity, we focus on hidden convexity throughout this work.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

Our Item 2 in Definition 1 can be relaxed by requiring the existence of c † (·) and replacing the condition (HC-2) with for all u, v ∈ U. By examining the proof of Proposition 3, it becomes clear that the above relaxation is sufficient for our analysis. We provide an educational example for a transformation satisfying (Gen-HC-2). With d = dim(X) and m:= dim(U), we consider a piece-wise linear map c (·) of the form for x ∈ R d, with an arbitrary partition { R i } k i =1 of R d, indicator functions ✶ R i (x) = 1 if x ∈ R i and ✶ R i (x) = 0 otherwise, and and arbitrary matrices { A i } k i =1 ⊂ R m × d satisfying the boundary conditions, for all i, j = 1,..., k with i = j, to ensure the continuity of c (·).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

- Case d < m (underdetermined case): Each A i has full column rank, and its Moore-Penrose pseudoinverse is given by

<!-- chunk {"id": "body-0032", "role": "body", "section": "Hidden Convex Problem Class", "weight": 1.0} -->

- Case d > m (overdetermined case): Each A i has full row rank, and its Moore-Penrose pseudoinverse is given by Then c (·) satisfies (NLGI-1) and (NLGI-2) with for u ∈ R m. Such c (·) satisfies (Gen-HC-2) with i.e. the reciprocal of the minimal non-zero singular value. The special instance of the case where dim(U) ≫ dim(X) is particularly interesting, e.g. in the context of controller synthesis in optimal control [BEF+94; ADL+19;], where the original problem, despite being non-convex, is still favorable, due to its lower dimensionality.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Globally Optimal Solutions and KKT Points", "weight": 1.0} -->

We start our analysis by proving elementary properties of constrained optimization under the structural assumption of hidden convexity.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Globally Optimal Solutions and KKT Points", "weight": 1.0} -->

Definition 2 We say ˆ x ∈ X is a Karush-Kuhn-Tucker (KKT) point of if F 2 (ˆ x) ≤ 0 and there exists a Lagrangian Multiplier ̂ λ ≥ 0 such that Definition 3 (Slater's Condition) We say that a θ -Slater's (or simply Slater's) condition holds if there exists a point x ∈ relint (X) with F 2 (x) ≤ -θ for some θ > 0. Such x is called a θ -Slater point.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Globally Optimal Solutions and KKT Points", "weight": 1.0} -->

Similar to Proposition 1 in the unconstrained case, we relate the KKT points of with the global minima.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Globally Optimal Solutions and KKT Points", "weight": 1.0} -->

Proposition 1 Let F i (·) be weakly convex on X for i = 1, 2 and problem (HC) be hidden convex. Assume c (·) is differentiable for some ˆ x ∈ X. Then the following implications hold: 1. If ˆ x is a KKT point of, then ˆ x is a global minimum. 2. If ˆ x is a global minimum of and Slater's condition holds, i.e. also ˆ x ∈ relint(X), then ˆ x is a KKT point.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Globally Optimal Solutions and KKT Points", "weight": 1.0} -->

Proof First, we show that ˆ x ∈ X being a KKT point of is equivalent to ˆ u = c (ˆ x) ∈ U being a KKT point of. Indeed, conditions H 2 (ˆ u) ≤ 0 and ̂ λH 2 (ˆ u) = 0 follow immediately from the reformulation, and by the chain rule we have As the map c (·) is invertible with a Lipschitz continuous inverse by (HC-2), then its Jacobian J c (ˆ x) is invertible at ˆ x (see e.g., Corollary 3.3.). Therefore, is equivalent to 0 ∈ ∂H 1 (ˆ u) + ̂ λ∂H 2 (ˆ u) + ∂ u δ U (ˆ u) and the promised equivalence holds. Since problem is convex and ˆ u is a KKT point, by the sufficient optimality condition, ˆ u is a globally optimal solution, i.e., H 1 (ˆ u) ≤ H 1 (u) for any u ∈ { v ∈ U | H 2 (v) ≤ 0 }.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Globally Optimal Solutions and KKT Points", "weight": 1.0} -->

As a result, we have To prove the second claim, we notice that if ˆ x ∈ X is a global minimum of implies that ˆ u = c (ˆ x) is a global minimum of the convex problem. Moreover, Slater's condition also holds for the convex reformulated problem. Then by [, Thm. 3.1.26] ˆ u is a KKT point of. It remains to use the equivalence of KKT points of problems and to conclude the proof. □

<!-- chunk {"id": "body-0039", "role": "body", "section": "Non-convex Equality Constraints", "weight": 1.0} -->

Throughout the paper, our main focus is hidden convex inequality constraints. However, many applications involve non-convex equality type constraints, which are known to be more challenging to handle than inequality constraints. We show that our results can be extended to hidden linear equality type constraints. In particular, for a given matrix A ∈ R n × d, consider the problem The equality constraint of this type can be written in the form of inequality constraint by increasing the number of constraints, i.e., Here, F 2, eq is vector valued when n > 1, and the equality and inequality constraints should be understood component-wise, i.e., F i 2, eq (x) = 0 for all i ∈ [n]. Moreover, one can combine these constraints into a single one and directly reduce the problem to our original form with a single constraint: It is important to note that in this formulation, Slater's condition typically fails and the max operators introduce non-smoothness even when the map c (·) is sufficiently smooth.

<!-- chunk {"id": "body-0040", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

Anatural question is whether the assumption about the common transformation c ( · ) in (HC) is essential. Suppose the objective and constraint are each hidden convex but under different transformations, c 1 ( · ) and c 2 ( · ). Does such a relaxation still admit efficient algorithms?

<!-- chunk {"id": "body-0041", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

We call this the setting of inconsistent transformations, where for convex functions H 1, H 2 and invertible maps c 1, c 2: X → U. We establish the following hardness result for such problems.

<!-- chunk {"id": "body-0042", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

Proposition 2 Hidden convex optimization under inconsistent transformations (HC-ICT) is NP-hard: there is no polynomial-time global solution method, unless P = NP.

<!-- chunk {"id": "body-0043", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

Proof We reduce from 0 -1 Integer Linear Programming. Given an integer matrix A ∈ Z n × d and vectors b, c ∈ Z n, consider the problem Step 1: Hidden convex structure. Define the maps Then F 1 (x) is trivially hidden convex as it is convex. Observe that the constraint can be written as F 2 (x) = H 2 (c 2 (x)) with H 2 (u):= ∥ w ∥ ∞, u:= (v, w), where v = y. The map c 2 (·) is invertible with a well-conditioned Jacobian of c -1 2 (operator norm bounded by 1 + 2 π), so F 2 is hidden convex under the transformation c 2 (·).

<!-- chunk {"id": "body-0044", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

Step 2: Constraint interpretation and hardness. The constraint F 2 ( x ) ≤ 0, together with z = 1, forces each y i to be an integer (since cos(2 πy i ) = 1 iff y i ∈ Z ). Thus the feasible region encodes the Boolean cube, and the problem simulates a 0 -1 Integer Linear Program of the form min y ∈ Z ⟨ c, y ⟩, s.t. Ay ≤ b.

<!-- chunk {"id": "body-0045", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

Proposition 2 shows that inconsistent transformations make hidden convex optimization intractable. Moreover, this result can be extended to show that such problems cannot even be well-approximated in polynomial time, unless P = NP. We refer to for the complexity of approximation algorithms and related canonical hard problems such as Independent Set, MAX-3SAT, and MAX-CUT.

<!-- chunk {"id": "body-0046", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

Proposition 2 has an additional consequence: it highlights the strength of hidden convexity compared to related structural assumptions such as gradient-domination. Indeed, using Proposition 2, one can verify that in the inconsistent-transformation setting (HC-ICT), both F 1 and F 2 satisfy a gradient-domination condition of the form where F ∗ i:= min x ∈X F i (x), D U i:= sup x,y ∈X ∥ c i (x) -c i (y) ∥. Nevertheless, Proposition 2 shows that such condition is insufficient to guarantee tractability: gradient domination (at least in this form) does not guarantee the tractability of global solutions. Figure 2 illustrates this phenomenon on a simpler instance. There, the transformation, c (x):= (x 1 -1, 2 | x 1 | -x 2 -1) ⊤, convexifies the feasible set, { F 2 ≤ 0 }:= { x ∈ X | ∥ c (x) + (0. 5, 0. 6) ⊤ ∥ 1 -0.

<!-- chunk {"id": "body-0047", "role": "body", "section": "NP-Hardness under Inconsistent Transformation", "weight": 1.0} -->

8 ≤ 0 }, but simultaneously destroys the convexity of the objective F 1 (x):= ∥ x - ⊤ ∥ 2, turning it into a nonconvex function. This contrast underscores the necessity of a consistent transformation applied jointly to the objective and constraints in hidden convex optimization.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Now we describe three motivating practical examples for hidden convex problems under functional constraints with consistent transformations. For additional examples, we refer, for example, to.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

(a) Non-convex Constraint. Level sets of F 1 and the feasible set { F 2 ≤ 0 } in the X -domain.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

(b) Convex Constraint after Reformulation. Level sets of transformed objective and the feasible set { H 2 ≤ 0 } in the U -domain.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Fig. 2: An illustrative example of a hidden convex problem with inconsistent transformations (HC-ICT).The grey regions illustrate the feasible set, and the objective value is shown in color. This problem has two local minima: the sub-optimal leftmost point x local = ( -0. 3, 0. 2) ⊤, and the optimal rightmost point x ∗ = (0. 5, 1. 5); x ∗ uncon denotes the global optimum without constraints. A local search method may terminate at the sub-optimal local minima x local.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Geometric Programming [; BKV+07;]. In the context of power control and communication systems, as well as optimal doping profile, the problems often involve so-called posinomial functions F j: R d > 0 → R with j = 1,..., p of the form with coefficients b k j > 0, K j ∈ N + and a i,k j ∈ R for all j = 1,..., p, k j = 1,..., K j, i = 1,..., d. Constrained Geometric Programming problem in the standard form [BKV+07, Eq. 3] is given by which is non-convex in x ∈ X:= R d > 0 but admits a convex reformulation via the variable change u:= c (x):= (log(x 1),..., log(x d)) ⊤. The resulting convex reformulation is where H j (·), j = 1,..., p are convex.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

One can easily see that (CGP) is hidden convex and satisfies (HC-2) with µ c:= (max x ∈X ∥ x ∥ ∞) -1, since log x i is (max x ∈X x i) -1 -strongly monotone.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Convex Constrained Markov Decision Process (CCMPD) [ZKB+20]. Convex reinforcement learning (RL) under convex constraints generalizes the classical (constrained) RL setting. Based on a discounted constrained Markov Decision Process (CMDP) of the form M (S, A, P, µ 0, γ, r, c), where S and A denote the (finite) state and action spaces respectively, P: S × A → ∆ (S) represents the state-action transition probability kernel, ∆ (S) is the probability simplex over S, µ 0 is the initial state distribution and γ ∈ is the discount factor. Based on the reward r: S ×A → R and the penalty cost c: S ×A → R, the classical RL problem is formulated in finding an optimal stationary policy π: ∆ (A) |S| → ∆ (A) by maximizing the reward function while satisfying the constraint on the cost function.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

With the notation of X ∼ ρ for a random variable X following a probability distribution ρ, as well as E [·] and P (·) for the expectation and probability, respectively, we formally define where Π:= ∆ (A) |S| is the set of all stationary policies. This set is the product of simplices, which admits an efficient projection. Note that, for consistency with our formulation, we minimize the negative expected reward, which is equivalent to maximizing the expected reward in standard RL formulations.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Given a policy π, at each time h ∈ N, the agent is in a state s h and chooses an action a h ∼ π (· | s h), resulting in a transition s h +1 ∼ P (· | s h, a h). With P µ 0,π we denote the induced probability distribution of the Markov chain (s h, a h) h ∈ N with an initial state distribution µ 0. Under a transformation via the state-action occupancy measure, defined by the classical constrained RL problem becomes linear in the objective and the constraint, i.e. (CMDP) is equivalent to max λ ∈U ⟨ r, λ π ⟩ s.t. ⟨ c, λ π ⟩ ≤ 0, where U:= { λ π | π ∈ Π }. Convex constrained RL generalizes this optimization problem to where the utility functions H 1, H 2: U → R are convex functions in λ π, but the resulting optimization problem over the policy space Π is non-convex.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Beyond the standard (CMDP), popular examples of (CCMDP) encompass safe exploration, i.e. H 1 is the negative entropy, under safety constraints, e.g. staying close to an experts trajectory H 2 (λ π):= ∥ λ π -λ π exp ∥. Other instances include safe apprenticeship learning and safe learning, see e.g., [GPL+21; ZOD+21; MDD+22] for details.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

The problem (CCMDP) is hidden convex by construction with X = Π and c ( x ):= λ π, (with x = π ). As shown in [ZKB+20, Proposition H.1], the constant µ c can be estimated under mild assumptions on the initial distribution µ 0. Note that in convex RL, we can control λ π only implicitly by changing the policy π, i.e. via the policy gradient theorem, and thus, the exact computation of the transformation map and its inverse would require the knowledge of the state-action transition probability kernel and can be either computationally expensive or even intractable.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Controller Synthesis in Optimal Control. Given a continuous-time linear time-invariant (LTI) system where x (t) ∈ R n is a state vector, u (t) ∈ R m a control input vector, and x 0 ∈ R n is an initial state generated as a random variable with covariance matrix W = E [x 0 x ⊤ 0] ∈ S n +, where S n + denotes the set of symmetric positive semidefinite n × n matrices. With static state feedback u (t) = Kx (t), K ∈ R m × n, the classical linear quadratic regulator (LQR) problem reads [Kal+60;]: where Q ⪰ 0, R ≻ 0, and Hurwitz stable means that all real parts of eigenvalues of A + BK are negative. It is known that (LQR) admits an optimal solution K ∗ (that is unique when W ≻ 0), which is also optimal for any square integrable control laws u (t) under mild assumptions.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

A direct gradient-based optimization of J LQR ( K ) over K is possible, but it requires initialization with a stabilizing K such that A + BK is Hurwitz. Finding such an initialization is often nontrivial, particularly in large-scale or poorly conditioned systems. To circumvent this difficulty, one can instead reformulate the problem with equality-type constraints that implicitly enforce stability and allow the user an arbitrary initialization of K.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Specifically, consider the nonlinear equality-constrained problem Above formulation is equivalent to (LQR), but (NL-Eq-LQR) implicitly enforces stability via the Lyapunov equation F 2, eq (x) = 0 and P ≻ 0, avoiding the need for stabilizing initialization. Although the strong duality holds under mild assumptions [, Thm. 1], the presence of the equality constraint implies that Slater's condition does not hold for this problem.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

Nevertheless, a convex reformulation of (NL-Eq-LQR) can be obtained by the variable change where K ∗ is the optimal controller.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

The inverse of c (·) is given by which admits a Jacobian of the form defined in perturbation notation in order to avoid tensors. For the paired spectral norm of the Jacobian we have Let us assume that the variable P is bounded away from zero with a sufficiently small constant, i.e., P ⪰ δI, and the variable Y is bounded. Then we can bound the operator norm by showing that c -1 is Lipschitz, which verifies (HC-2).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Motivating Applications", "weight": 1.0} -->

We define A ∗:= A + BK ∗, Q ∗:= Q +(K ∗) ⊤ RK ∗, then (NL-Eq-LQR) is reformulated as Notice that the objective is convex and the constraint is linear in the new variables. Although such reformulation exists, the change of variables u = c (x) depends on the unknown optimal controller K ∗, thus we need to solve the problem in the original variable x = (P, K). We note that (L-Eq-LQR) involves linear equality constraints; refer to Section 2.2, where we show how multiple scalar equality type constraints can be reformulated into a single inequality constraint using the max-operator, matching our problem formulation (HC).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Observations for Convergence Analysis", "weight": 1.0} -->

We state the following basic proposition, which is a useful observation for convergence analysis of gradient methods under hidden convexity.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Observations for Convergence Analysis", "weight": 1.0} -->

Proposition 3 (Prop. 3) Let (HC) be hidden convex with µ c > 0. For any α ∈ and x, y ∈ X, define x α:= c -1 ((1 -α) c (x) + αc (y)), then, for i = 1, 2, the following functional inequality and the norm inequality These two inequalities will be used multiple times in the subsequent sections. The proof is included in Section A for completeness.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Proximal Point Method (PPM)", "weight": 1.0} -->

We begin the algorithmic part by analyzing the Proximal Point Method under hidden convexity. This approach seems promising in light of the prior work, which used PPM framework for non-asymptotic analysis, cf. Section 1.1. Specifically, we focus on an inexact variant (IPPM) using a feasible inner solver A; see Algorithm 1. Such feasible inner solver will be crucial to avoid constraint qualification (CQ) assumptions. The main challenge is to prove convergence of IPPM to a global optimum under hidden convexity when A is only approximate. Our key observation is that, even if the original problem fails Slater's condition, each IPPM subproblem can be made to satisfy Slater's condition via a constraint shift. In Section 3.2 we instantiate the inner solver A and derive total (sub-)gradient oracle complexities for (HC) problems, depending on the smoothness levels of F 1 and F 2.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Proximal Point Method (PPM)", "weight": 1.0} -->

The central device enabling our IPPM analysis is a two-level shift of the constraint that enlarges the feasible set of each subproblem: (i) an outer shift by a budget τ (chosen on the order of the target accuracy ε ), and (ii) an inner shift used by the inner solver A that depends on the Slater gap of the current IPPM subproblem (typically smaller), cf. Algorithms 2 and 3.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Algorithm 1 IPPM( F 1, F 2, x, ε, τ, N, ˆ ρ ) Inexact Proximal Point Method for (HC)", "weight": 1.0} -->

- 1: Input: Objective F 1, constraint F 2, initial point x ∈ X ∩ { F 2 ( · ) ≤ τ }, accuracy ε, constraint violation budget τ, outer loops N, inner (feasible) algorithm A, regularization parameter ˆ ρ > ρ

<!-- chunk {"id": "body-0070", "role": "body", "section": "Algorithm 1 IPPM( F 1, F 2, x, ε, τ, N, ˆ ρ ) Inexact Proximal Point Method for (HC)", "weight": 1.0} -->

- 4: Compute an approximate feasible solution to (Shifted-IPPM) via 5: end for 6: Return: x (N)

<!-- chunk {"id": "body-0071", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

IPPM solves at each iteration k ∈ N the (strongly convex) shifted subproblem Here, ˆ x (k +1) is the exact subproblem minimizer and x (k +1) is an approximate solution.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

- -Initialization. Assume x is τ -feasible for (HC), i.e., F 2 (x) ≤ τ. If not, a simple (sub-)gradient method on F 2 finds such a point in ˜ O (1 /τ) gradient evaluations in the smooth case or ˜ O (1 /τ 3) in the non-smooth case; this does not change the overall complexity. - -Feasibility preservation. If x (k) is τ -feasible for (HC), it is (trivially) feasible for (Shifted-IPPM). Running a feasible inner method on (Shifted-IPPM) from x (k) yields φ (k) 2 (x (k)) ≤ τ and hence F 2 (x (k)) ≤ τ. Thus all outer iterates remain τ -feasible for (HC). - -Slater points for subproblems. Define x (k) α:= c -1 ((1 -α) c (x (k)) + αc (x ⋆)). For sufficiently small α (relative to τ), the point x (k) α is strictly feasible for (Shifted-IPPM).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

This proves Slater's condition for (Shifted-IPPM) at each iteration k ≥ 0 and allows us to apply a feasible method to solve this subproblem. - -Optimality Improvement. It remains to build a PPM recursion similar to analysis to guarantee the improvement in F 1, up to errors from inexact inner solvers.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Now we formalize our key 'HC-Slater's Lemma', which verifies the subproblems (Shifted-IPPM) satisfy Slater's condition under a suitable reference point x ( k ).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Lemma 1 (HC-Slater's Lemma) Assume that (HC) is hidden convex, Assumption 1.3 holds and x (k) is τ -feasible for (HC). Then 1. (Shifted-IPPM) satisfies ατ 2 -Slater's condition with α ≤ min { 1, µ 2 c τ ˆ ρ D 2 U }. 2. If, additionally, (HC) satisfies θ -Slater's condition, then (Shifted-IPPM) satisfies βθ 2 -Slater's condition with β ≤ min { 1, µ 2 c θ ˆ ρ D 2 U }.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Proof Part 1. Fix an iteration index k ∈ [N], and for any α ∈ define We will show that x (k) α is a Slater point for subproblem (Shifted-IPPM). Indeed, where we used (HC-FI) for F 2 in (i), τ -feasibility of x (k) in (ii), (HC-NI) in (iii), as well as the boundedness of U domain in (iv). The last inequality follows by the choice of α.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Part 2. Let ¯ y ∈ X be a θ -Slater point of (HC), and for any k ∈ [N], β ∈ define We will show that ¯ y (k) β is a Slater point for subproblem (Shifted-IPPM). Indeed, where we used (HC-FI) for F 2 in (i), θ -Slater point in (ii), (1 -β) τ ≤ τ since β ≤ 1 in (iii), (HC-NI) in (iv), as well as the boundedness of U domain in (v). The last inequality follows by the choice of β. □ Lemma 1 says that regardless whether (HC) satisfies Slater's condition, a Slater point for PPM sub-problem (Shifted-IPPM) always exists. This allows us to apply a feasible method to solve such subproblems, i.e., we suppose the algorithm A ε in solves (Shifted-IPPM) to (ε, 0) -optimality for any target precision ε in > 0, i.e.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

We will see in Section 3.2 that such algorithms are readily available in the literature (with a slight modification of shifting the constraint φ ( k ) 2 with a value less than ατ 2 or αθ 2 ), e.g., switching sub-gradient or fast primal-dual methods.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Now we are set to show the main result, i.e. the convergence of IPPM.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Theorem 2 (Inexact PPM) Assume that (HC) is hidden convex and Assumption 1 holds. Let x be τ -feasible for (HC) and algorithm A ε in initialized with a feasible point x (k) outputs a point x (k +1) satisfying (IPPM-Feas) after T in = T in (ε in) (sub-)gradient and function evaluations. Given a lifting parameter ˆ ρ > ρ (here ρ > 0 is the weak convexity parameter) and a desired tolerance ε > 0 for the optimality gap, assume ε ≤ 3ˆ ρ D 2 U 2 µ 2 c and τ ≤ ˆ ρ D 2 U 2 µ 2 c hold. Then setting ˆ ρ:= 2 ρ and ε in ≤ ε 3 min { 2 µ 2 c ε 3ˆ ρ D 2 U, µ 2 c τ ˆ ρ D 2 U }, the last iterate of Algorithm 1 satisfies iterations, where ∆ 0:= F 1 (x) -F ∗ 1. The total oracle complexity is given by In Section 3.2, we will compute the bounds for the oracle complexity T tot as a function of ε, specifying T, but first we prove the above central theorem.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

Proof By the HC-Slater's Lemma 1.1, we have the point after with α ≤ µ 2 c τ ˆ ρ D 2 U is feasible for (Shifted-IPPM) at iteration k, i.e., x (k) α ∈ X ∩{ F 2 (·)+ ˆ ρ 2 ∥ · -x (k) ∥ 2 -τ ≤ 0 }. Since A ε in satisfies φ (k) 1 (x (k +1)) ≤ φ (k) 1 (ˆ x (k +1)) + ε in and using the optimality condition for ˆ x (k +1), we derive where the second inequality holds by the property of A ε, the third is by optimality of ˆ x (k +1) and feasibility of x (k) α.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Convergence Analysis of Inexact PPM", "weight": 1.0} -->

The last step is due to (HC-FI), (HC-NI), and the bound on the diameter of U. By unrolling the above recursion from k = 1,..., N -1 and using that the partial sum of the geometric series is bounded by 1 / α, we derive where the last step holds by the choice of ε, N as in the Theorem statement, and α ≤ min { 2 µ 2 c ε 3ˆ ρ D 2 U, µ 2 c τ ˆ ρ D 2 U } ∈. □ Remark 1 It is possible to improve the above oracle complexity in the case of µ H -hidden strong convexity, cf. Theorem 5 in Section B.1.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Oracle Complexity Analysis for IPPM", "weight": 1.0} -->

In this section, we specify algorithms for solving the sub-problem in Algorithm 1 and compute the upper bounds on the oracle complexity of the resulting methods. We distinguish between two important cases. First, we consider the problem without any CQ in the non-smooth and smooth settings. Second, we establish faster convergence assuming a Slater point exists for problem (HC).

<!-- chunk {"id": "body-0084", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

To compute the total oracle ((sub-)gradient and function evaluation) complexity of IPPM in the nonsmooth setting without any constraint qualification (CQ), we use a slight modification of the SwSG method in place of A ε, see Algorithm 2. We use SwSG since it is optimal for nonsmooth convex (and strongly convex) constrained optimization and does not require CQ assumptions.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Switching Sub-Gradient Method [, Algo 1] for solving (Shifted-IPPM) 1: Input: Regularized objective φ (k) 1 and constraint φ (k) 2, current IPPM-iterate x (k) ∈ X, number of steps T in ∈ N, constraint violation budget τ 2: Define precision ε in > 0, parameter α > 0, and stepsizes (η t) t as in Corollary 1 3: Initialize z ← x (k) ∈ X 4: Define F ← ∅, I ← ∅ 5: Shift constraint φ (k) 2, sh (x):= φ (k) 2 (x) -τ + ατ 3, x ∈ X 6: for t = 1, 2, 3,...,

<!-- chunk {"id": "body-0086", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

z (t +1) ← proj X (z (t) -η t ζ (t) 2), with ζ (t) 2 ∈ ∂φ (k) 2 (z (t)), I ← I ∪ { t } 11: end if 12: end for 13: return x (k +1) ← ∑ t ∈F (t +1) z (t) / (∑ t ∈F (t +1)) Corollary 1 (IPPM+SwSG, Non-smooth, No CQ) Under the assumptions of Theorem 2, when using the SwSG (Algorithm 2) method as the inner solver, the total number of sub-gradient calls and function evaluations required to achieve (IPPM-Opt) is given: Proof The proof is deferred to Section B.3.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Remarkably, the above result matches (in terms of ε ) the sub-gradient complexity for solving hidden convex unconstrained problems (see also Corollary 4 in Section B.2 for discussion about the optimality criterion). Importantly, in the constrained setting, F 2 ( · ) ̸≡ 0 requires no constraint qualification (CQ) conditions. This is consistent with similar results in convex case, where the oracle complexity of SwSG method matches the one of (sub-)gradient method, i.e., O ( ε -2 ).

<!-- chunk {"id": "body-0088", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Next, we consider the smooth setting, where the oracle complexity can be further improved from ˜ O ( ε -3 ) to ˜ O ( ε -2 ) under hidden convexity. To achieve this, we do not require CQs, but we need to use a faster inner solver to reduce the inner solver complexity, T in ( ε in ). We use a suitably modified (shifted) version of ACGD algorithm, see Algorithm 3. ACGD achieves the optimal oracle complexities in (strongly) convex smooth constrained optimization (improving, e.g., SwSG), which translates to improvements of the total oracle complexities for our problem.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Accelerated Constrained Gradient Descent Method [, Algo 1] for solving (Shifted-IPPM) 1: Input: Regularized objective φ (k) 1 and constraint φ (k) 2, current PPM-iterate x (k) ∈ X, constraint violation budget τ, 2: Define stepsizes { θ t }, { η t }, { τ t }, and weights { ω t } according to Corollary 2 or Corollary 3 if Slater's condition holds 3: Counter t ← 0 and initialize z (t -1) ← x (k), z (t) ← x (k), z (t) ← x (k) ∈ X 4: Set π ←∇ φ (k) 1 (z), ν ←∇ φ (k) 2 (z) 5: if Slater's condition holds then 6: b ←-τ + βθ 3 according to Corollary 3 7: else 8: b ←-τ + ατ 3 according to Corollary 2 9: end if 10: Shift constraint φ (k) 2, sh (x):= φ (k) 2 (x) -b, x ∈ X 11: for t = 1,

<!-- chunk {"id": "body-0090", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

ν (t) · (x -z (t)) + φ (k) 2, sh (z (t)) ≤ 0 } 15: end for 16: return x (k +1) ← ∑ T in t =1 ω t z (t) / (∑ T in t =1 ω t) Corollary 2 (IPPM+ACGD, Smooth, No CQ) Under the assumptions of Theorem 2 and assuming that F 1, F 2 are L -smooth, when using the ACGD (Algorithm 3) method as the inner solver, the total number of gradient calls and function evaluations required to achieve (IPPM-Opt) is given: Proof The proof idea of the above result is to upper bound the Lagrange multiplier of the sub-problem (Shifted-IPPM), and use it to calculate the oracle complexity bound of ACGD, see Section B.3 for details.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

□ 3.2.2 Oracle complexity with Slater's assumption Unfortunately, the oracle complexity in Corollary 2 does not recover the oracle complexity of unconstrained hidden convex problems in the smooth case [ZKB+20;], which is ˜ O (ε -1). The loss in the complexity happens since the oracle complexity of the ACGD depends on the bound of the optimal dual variable λ ∗, which in our case happens to be large - of order ˜ O (ε -2) (assuming ε = τ), see the proof details in Section B.3. The following Corollary improves this complexity in the setting when Slater's condition holds.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Corollary 3 (IPPM+ACGD, Smooth, Slater's Condition) Let the assumptions of Theorem 2 hold and that F 1, F 2 are L -smooth. Assume additionally that (HC) satisfies θ -Slater's condition with µ 2 c θ ˆ ρ D 2 U ≤ 1. Then when using ACGD (Algorithm 3) method as the inner solver, the total number of gradient calls and function evaluations required to achieve (IPPM-Opt) is given: where F UB 1:= max x ∈X F 1 (x), F LB 1:= min x ∈X F 1 (x).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Proof The proof is analogous to the proof of Corollary 2 and the details are deferred to Section B.3. □ This result implies that if our original problem (HC) satisfies the θ -Slater's condition, the oracle complexity of Algorithm 1 can be further improved to ˜ O (θ -1 ε -1), up to logarithmic factors, matching the complexity for solving unconstrained hidden convex problems when θ = ˜ O.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Oracle complexity without Slater's assumption", "weight": 1.0} -->

Remark 2 The results of Corollaries 2 and 3 only focus on the oracle complexity and do not take into account the computational complexity for solving quadratic sub-problems with linear constraints in ACGD method. However, the computational complexity (number of arithmetic operations and matrixvector products) is mild and can be estimated based on Corollary 4.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

As established in the previous section, the inexact proximal point approach (IPPM) yields oracle complexities matching those for unconstrained hidden convex optimization. In the smooth setting, however, our approach either relies on Slater's condition (and results in ˜ O ( θ -1 ε -1 ) complexity) or incurs a suboptimal ˜ O ( ε -2 ) oracle complexity in terms of accuracy ε. The former bound is not satisfactory since it scales with the inverse of the Slater gap θ, a quantity that may be arbitrarily close to zero in practice. This limitation appears inherent to the IPPM approach, as our proof technique requires each subproblem to satisfy Slater's condition. Obtaining the ˜ O ( ε -1 ) rate (matching the unconstrained setting) without Slater's condition would require an algorithm for smooth, strongly convex, constrained optimization with ˜ O ( √ κ ) complexity independent of dual variable bounds. Such an algorithm is not known, and to the best of our knowledge, its existence remains an open problem.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

In this section, we aim to achieve fast ˜ O ( ε -1 ) gradient complexity for hidden convex problems without Slater's condition. To do so, we take a different approach based on the cutting plane/bundle-level idea. First, we want to highlight that the existing theory of bundle-level type methods is predominantly limited to the convex setting. This is because the core idea of this approach is to build a global lower model of the objective using linear or piece-wise linear approximations. While such philosophy is powerful for convex programming, it fails even on simple non-convex problems.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

- (a) Illustration of the linearized objective without shifting, ℓ F 1 (x, x (t)), over the set X = [-0. 95, 0. 95]. Starting at x (t) = 0. 891, the lack of shifting causes (StarBL) to diverge; the next iterate x (t +1) = -0. 95 is maximum on X. - (b) Illustration of the shifted linearized constraint, ℓ F 2 (x, x (t)), at x (t) = (1. 34, 0. 74) ⊤. The point x (t) α is feasible for (S-StarBL) subproblem when α, τ are chosen according to Lemma 2 and Theorem 3 respectively. - (c) Illustration of the shift of the linearized objective ℓ F 1 (x, x (t)). By introducing the shift, (S-StarBL) makes a more careful step than (StarBL) and improves the next iterate to x (t +1) = -0. 24.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

Fig. 3: (a) and (c): To illustrate the need for the shift, we use the hidden convex function F 1 ( x ):= 1 -cos( π · x ) without constraints. (b): We illustrate the shifted constraint on the constrained geometric programming example F 1 ( x ):= x 1 · x 2 + 4 x 1 + 1 x 2 constrained to { F 2 ≤ 0 }, where F 2 ( x ):= x 1 · x 2 -1, cf. (Ex-CGP) in Section 5.1.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

This algorithm finds the next point x ( t +1) as the projection of the current iterate x ( t ) to the intersection of two linear constraints. We refer to this algorithm (StarBL) as it uses the optimal value F ∗ 1. While this method converges for convex problems (see ), it may fail for non-convex problems.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

Example 1 Consider minimizing F 1 ( x ) = 1 -cos( πx ) with F 2 ( · ) ≡ 0 over the set X = [ -0. 95, 0. 95]. This problems is hidden convex with c ( x ) = sin( π 2 x ), H ( u ) = 2 u 2, µ c ≥ π 2 cos( π 2 · 0. 95) > 0. However, starting from a point x ( t ) ≥ 0. 891 the method jumps to x ( t +1) = -0. 95. In subsequent iterations the algorithm infinitely oscillates between x = ± 0. 95, which correspond to the global maxima of this problem, see Figure 3a for an illustration of this failure example.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

The failures as in the above example are common and occur due to the negative curvature of the objective, which makes the linear approximation an invalid global lower model of F 1, see Figure 3b. This motivates our key algorithmic modification involving a carefully chosen shift of the linearized objective and constraints. The introduced shifts relax the linearized constraints allowing the bundle-level method to approach the optimum as illustrated in Figure 3c.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

Before we proceed with the formal algorithm description, we introduce some useful notation for this section. We define the optimal value function as Notice that when the argument η = F ∗ 1 = min x ∈X { F 1 (x), s.t. F 2 (x) ≤ 0 }, then V (F ∗ 1) = 0. Define a linear minorant of a differentiable function F: X → R as Now we are ready to introduce the proposed algorithm. First, we consider the case when the optimal value F ∗ 1 is known. 5 Let α ∈, τ > 0 are some parameters, then our Shifted Star Bundle-level (S-StarBL) algorithm has the update rule: This algorithm shifts the feasible set of Bundle-level subproblem allowing us to search for x (t +1) in the larger set, see Figures 3b and 3c for illustrations of the update rule.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

Next, we consider the setting when F ∗ 1 is unknown, which is arguably much more challenging. In this setting, we design a double-loop procedure, which dynamically searches for the optimal value F ∗ 1 using the exact penalty, F 1 ( x ( t ) ) + λ [ F 2 ( x ( t ) )] +, as a convergence criterion. The method is described in Algorithms 4 and 5. The outer loop Algorithm 5 repeatedly calls the Shifted Bundle-level Algorithm 4 and updates the current lower bound estimate η k of the optimal value F ∗ 1.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

Remark 3 In Algorithm 5, we assume that the input lower bound value satisfies η 0 ≤ F ∗ 1. This is not limiting as we can use the following simple initialization protocol. We first run the (projected) gradient descent on the unconstrained problem, min x ∈X F 1 ( x ), for N init = ˜ O ( ( ρ + L ) D 2 U µ 2 c ε ) iterations to find a point z ( N init ) with F 1 ( z ( N init ) ) -ε ≤ min x ∈X F 1 ( x ) ≤ F ∗ 1. If we have F 2 ( z ( N init ) ) ≤ ε, we return the point z ( N init ) as the solution, otherwise we initialize η 0 = F 1 ( z ( N init ) ) -ε, which is a valid lower bound for F ∗ 1.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Bundle-level Approach", "weight": 1.0} -->

Remark 4 We assume that in Algorithm 5 the input estimate of the Lagrange multiplier λ is lower bounded by the optimal multiplier λ ∗. Such upper bound of λ ∗ can be obtained if Slater's gap is known, e.g. using λ ∗ ≤ ( F 1 ( y ) -F ∗ 1 ) /θ [, Lem. 3.1.21], where y is a θ -Slater point. However, oftentimes, although Slater's condition fails, the strong duality can be verified with an estimate of λ ∗, see, e.g., the controller synthesis example with equality constraints in Section 2.4.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Algorithm 5 Ada-LS ( x, η 0, N, τ, α, β, λ )", "weight": 1.0} -->

Adaptive Line Search for Shifted Bundle-level (S-BL) Method

<!-- chunk {"id": "body-0107", "role": "body", "section": "Algorithm 5 Ada-LS ( x, η 0, N, τ, α, β, λ )", "weight": 1.0} -->

- 1: Input: Initial point x ∈ X, lower bound of the optimal value η 0 ≤ F ∗ 1 of (HC), number of epochs T, maximum minorant violation budget τ, contraction factors α and β, estimate of Lagrange multiplier λ 5 In practice, the optimal value can be obtained by solving the Lagrange dual problem if strong duality holds provided that the dual problem is easy to solve.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Algorithm 4 S-BL ( x, η, T, τ, α, β, λ )", "weight": 1.0} -->

- 1: Input: Initial point x ∈ X, lower bound of the optimal value η ≤ F ∗ 1 of (HC), number of iterations T, maximum minorant violation budget τ, contraction factors α and β, estimate of Lagrange multiplier λ The following lemma is central to establish convergence of both above proposed algorithms. Since (S-StarBL) is a special case of Algorithm 4 with η = F ∗ 1, β = 1 and arbitrary λ ∈ R, the following unified lemma applies to both schemes.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Algorithm 4 S-BL ( x, η, T, τ, α, β, λ )", "weight": 1.0} -->

Lemma 2 Let Assumption 1 hold and let x ∗ ∈ X be an optimal solution to the hidden convex problem (HC). For any t ≥ 1 and α ∈, define the point x (t) α:= c -1 ((1 -α) c (x (t)) + αc (x ∗)). Then we can distinguish between two cases: for all t ∈ [T]. By setting τ ≥ ρα 2 D 2 U 2 µ 2 c, the point x (k) α is feasible for subproblem (SBL-QP). Moreover, for any t = 0,..., T -1: Alternatively, there exists ¯ t ∈ [T] such that Then we have η k +1 < F ∗ 1. If, additionally, strong duality holds with a Lagrange multiplier λ ∗, then Proof Assume we are in the ' Good case ', then using weak convexity and hidden convexity of F 1, we have where the second and third inequalities follow from Proposition 3, and the last two are due to our choice of τ, and the fact that we are in the ' Good case '.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Algorithm 4 S-BL ( x, η, T, τ, α, β, λ )", "weight": 1.0} -->

Similarly for F 2, we have where in the last step we used the assumption on τ and the feasibility of x ∗. The above two inequalities imply that x (t) α is feasible for sub-problem (SBL-QP). Using the optimality of x (t +1), and above established feasibility of x (t) α, we obtain Now assume we are in the ' Bad case ', then by construction of η t +1 we have where the inequality holds since ¯ x (k) satisfies F 1 (¯ x (k))+ λ [F 2 (¯ x (k))] + ≤ F 1 (x (¯ t))+ λ [F 2 (x (¯ t))] + due to the output criterion of Algorithm 4. By strong duality, we have for any x ∈ X, that F 1 (x) ≥ F ∗ 1 -λ ∗ [F 2 (x)] +. Therefore, concluding the proof.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Algorithm 4 S-BL ( x, η, T, τ, α, β, λ )", "weight": 1.0} -->

Now we are ready to formulate the main results of this section, i.e. the convergence of Algorithms 4 and 5. We distinguish between two most interesting cases: when we know the optimal value F ∗ 1 and when we do not know it.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Convergence with Known F ∗ 1", "weight": 1.0} -->

In this case we can set η = F ∗ 1, β = 1, arbitrary λ ∈ R, and we do not need the outer loop 'line-search' procedure Algorithm 5, since our algorithm simplifies to (S-StarBL). Under this choice of parameters, we always fall in the ' Good case ' of Lemma 2, and we have the following convergence result.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Convergence with Known F ∗ 1", "weight": 1.0} -->

Theorem 3 (S-StarBL, Known F ∗ 1, No CQ) Assume that (HC) is hidden convex, Assumption 1 holds and that F 1, F 2 are L -smooth. Set τ = ρα 2 D 2 U 2 µ 2 c, α = εµ 2 c (ρ + L) D 2 U, then the last iterate of (S-StarBL) satisfies Proof The choice of η, β and λ implies that for any t ≥ 0 Therefore, by smoothness of F 1 we obtain where the last inequality follows from the update rule of Algorithm 4 due to feasibility of x (t +1) for (SBL-QP). Subtracting F ∗ 1 from both sides and noticing that the choice of η, β and λ imply that we are in the ' Good case ' of Lemma 2, we obtain for any τ ≥ ρα 2 D 2 U 2 µ 2 c the recursion after An analogous derivation for F 2 results in Combining the above two inequalities, we can establish a recursion for the value function where in the last step we used the definition of the value function and set τ = ρα 2 D 2 U 2 µ 2 c.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Convergence with Known F ∗ 1", "weight": 1.0} -->

Then by unrolling the recursion for t = 0,..., T -1, we have for any α ∈ Setting α = εµ 2 c (ρ + L) D 2 U, we obtain the desired result.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

In this subsection, we will deal with the situation when the exact value of F ∗ 1 is unknown. Assume for simplicity that we have a valid lower bound for the optimal value F ∗ 1 to initialize our Algorithm 5, i.e., η 0 ≤ F ∗ 1. Such lower bound can be straightforwardly obtained as we explain in Remark 3. We also assume that the initial point x is nearly feasible, i.e., [ F 2 ( x )] + ≤ ε/ (2 λ ). Such point can be easily found by solving min x ∈X F 2 ( x ) to this accuracy in ˜ O ( λ ( ρ + L ) D 2 U µ 2 c ε ) iterations of projected gradient descent applied to F 2 ( · ). Now we are ready to prove the main convergence result of Algorithm 5 which calls Algorithm 4 at each iteration.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

Theorem 4 (S-BL+AdaLS, Unknown F ∗ 1, Strong Duality) Assume that (HC) is hidden convex, Assumption 1 holds, and that F 1, F 2 are L -smooth. Let the strong duality hold for (HC) and the optimal Lagrange muliplier is at most λ ∗. Set η 0 ≤ F ∗ 1, β = 1 / 2, λ ≥ λ ∗, and [F 2 (x)] + ≤ ε / (2 λ). Then Algorithm 5 has the oracle complexity Proof Assume, for the sake of contradiction, that for the first k ≤ N iterations F 1 (¯ x (k)) -F ∗ 1 + λ [F 2 (¯ x (k))] + > ε. Our proof strategy is to show that we always fall into the ' Good case ' of Lemma 2 at least once before k ≤ N.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

First, if for some k ≤ N, the lower bound η k is a good approximation of the optimal value η k, i.e., F ∗ 1 -η k ≤ ε, then the choice β = 1 / 2 implies that for all t in iteration k and we automatically fall into the ' Good case ' of Lemma 2.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

Otherwise, if F ∗ 1 -η k > ε, we are going to estimate the number of outer loop iterations N (of Algorithm 5) to achieve F ∗ 1 -η N ≤ ε. Since λ ≥ λ ∗, the ' Bad case ' of Lemma 2 implies F ∗ 1 -η N ≤ ( F ∗ 1 -η 0 ) / 2 N. Thus, after at most N ≥ log 2 ( F ∗ 1 -η 0 ε ) iterations, we have F ∗ 1 -η N ≤ ε, and we end up in the ' Good case ' of Lemma 2.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

Therefore, there exists at least one k = k ∗ ≤ N when we fall into the ' Good case '.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

By Lemma 2, x (t) α is feasible for each subproblem (SBL-QP), and ∥ x (t +1) -x (t) ∥ ≤ ∥ x (t) α -x (t) ∥ ≤ α D U µ c for all t = 0,..., T -1. By L -smoothness, following similar steps as in the proof of Theorem 3, we obtain Defining A:= (ρ + L) D 2 U 2 µ 2 c, using η k ∗ ≤ F ∗ 1 (guaranteed by Lemma 2) and setting τ = ρα 2 D 2 U 2 µ 2 c where the [·] + appears by considering the cases when F 2 (x (t +1)) ≥ 0 and F 2 (x (t +1)) < 0. Summing up, we have Unrolling and using the above average feasibility bound, we have Now it remains to set which implies F 1 (x (T)) -F ∗ 1 ≤ ε/ 2 and λ [F 2 (x (T))] + ≤ ε/ 2 and, therefore, their sum is at most ε.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Convergence with Unknown F ∗ 1 under Strong Duality", "weight": 1.0} -->

We arrive at the contradiction with the initial assumption F 1 (¯ x (k)) -F ∗ 1 + λ [F 2 (¯ x (k))] + > ε, there must be some k ∗ ≤ N such that This concludes the proof.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Numerical Simulations", "weight": 1.0} -->

This section presents numerical simulations that illustrate and verify the proposed algorithms. The examples are small or medium scale, and primarily serve to demonstrate the concepts and theoretical properties in a transparent manner.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

Non-smooth Non-linear Least Squares. First, we focus on the IPPM+SwSG algorithm and test it on a toy non-smooth problem. In the two-dimensional case X = U = R 2, we use an invertible map which is non-smooth and has a Lipschitz inverse on X = [-1, 2. 5] 2. Our goal is to minimize the following non-smooth non-convex constrained non-linear least-squares (CNLS) problem of the form: (c) Objective value and constraint violation for IPPM+SwSG method (outer loop iterates, (x (k)) k), oracle calls in logscale.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

Fig. 4: Solving the non-smooth (Ex-CNLS) using the Inexact Proximal Point Method with Switching Sub-Gradient (IPPM+SwSG), cf. Section 3.2.1. with b 1:= ⊤, b 2:= (-0. 5, -0. 6) ⊤. Note that the problem above is non-smooth and non-convex (in variable x ∈ X), in particular, we cannot use a projection onto a non-convex set { F 2 ≤ 0 }, cf. feasible region in Figure 4a.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

It can be verified that (Ex-CNLS) is hidden convex with µ c = 4 and satisfies Assumption 1 with ρ = 2, and G = 2, e.g., using [, Thm. 4.2], [, Cor. 16.72]. The solution to this problem is x ∗ = (0. 85, 0. 85) ⊤ with F 1 ( x ∗ ) = 0. 15, u ∗ = ( -0. 15, -0. 15) ⊤, and λ ∗ = 0. 5. 6 We also verify that Slater's condition (Definition 3) holds, noting that F 2 ((0. 5, 0. 5) ⊤ ) = -0. 7 < 0. The optimization trajectory of IPPM+SwSG is presented in Figures 4a and 4b. The proximal point iterates approach the constrained solution and remain in the constrained (gray) region; the induced trajectory in the convex space has a 'z' shape due to non-linearity of the transformation c ( · ). Convergence and constraint violation plots in Figure 4c show that the proposed algorithm successfully reduces the objective value and ensures the constraint satisfaction.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

6 In this toy example, the optimizer can be obtained by solving the problem in the convex space U, projecting the global optima onto the feasible set, and mapping the point back to X.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

(c) Objective value and constraint violation for ( x ( k ) ) k, oracle calls in log-scale.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

Fig. 5: Solving the smooth (Ex-CGP) problem. Comparison of the Inexact Proximal Point Method with Accelerated Constrained Gradient Descent (IPPM+ACGD), cf. Section 3.2.2, the Shifted Star Bundlelevel (S-StarBL) with known F ∗ 1, cf. Section 4.1, and the and Shifted Bundle-level with Adaptive Line Search (S-BL+AdaLS) with unknown F ∗ 1 and η 0 = 0, cf. Section 4.2. For both Bundle-level variants we only plot every 50th iterate to simplify the visualization.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

Smooth Geometric Programming. Now we test our more advanced algorithms IPPM+ACGD, S-StarBL, and S-StarBL+AdaLS designed for smooth optimization. We use the previous instance of (CGP) problem from Figure 1: where X:= [0. 4, 3] 2 ⊂ R 2 +. As shown in Section 1, (Ex-CGP) is non-convex in x ∈ X but hidden convex under the transformation function c (x):= (log x 1, log x 2) ⊤, and satisfies our assumptions with µ c = 1 3, ρ = 1, G = 25. 286. This problem has the minimizer x ∗ = (2, 0. 5) ⊤ with F 1 (x ∗) = 5, and u ∗ = (log 2, -log 2) ⊤. Slater's condition holds with F 2 ((0. 5, 0. 5)) = -0. 75 < 0.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

The results are shown in Figure 5. We observe that all three proposed algorithms successfully converge to the global minima of this problem and respect the constraint satisfaction during optimization process. IPPM+ACGD progresses slowly at the initial phase due to the conflicting (non-convex) objective and constraint. The S-StarBL method converges the fastest among the three, efficiently leveraging the knowledge of the optimal value F ∗ 1. In the absence of F ∗ 1, our adaptive line-search (AdaLS) procedure converges slower than the star version of the algorithm due to an underestimation of the linearized objective caused by the misspecification of the optimal value estimate η 0, cf. Figure 3.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Visualization of Convergence and Optimization Trajectories (2D Case)", "weight": 1.0} -->

Fig. 6: Solving a high dimensional instance of (CGP) using our IPPM+SwSG, IPPM+ACGD, S-StarBL and S-BL+AdaLS algorithms. We report the objective value and constraint violation vs. the cumulative oracle calls.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Scalablility to High Dimensions", "weight": 1.0} -->

Finally, we compare both proposed algorithms (with two variations each) on a high dimensional constrained geometric programming problem (CGP). We evaluate them on randomly generated instances where both the objective and constraint are posynomials F j ( x ) = ∑ k j b k j ∏ i x a i,k j i, j ∈ { 1, 2 }. We fix the dimension d = 100 and the number of components K 1 = 10 and K 2 = 8. Exponent rows ( a ·,k j ) are drawn uniformly from [ -0. 5, 0. 5], and coefficients b k j are sampled from a log-normal distribution (normalized for the constraint so that ∑ K 2 k 2 =1 b k 2 = 1, making it nearly tight at x = 1 ). Iterates are projected component-wise onto the box [0. 5, 2] d, starting from x = 1, which is feasible. Before running our algorithms, we use CVX solver to solve our problem in log-variables, which provides the reference value F ⋆ 1 ≈ 0.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Scalablility to High Dimensions", "weight": 1.0} -->

07114. Our proximal point algorithms use identical outer-loop settings: ten proximal epochs, proximal weight ˆ ρ = 0. 02, tolerance τ = 10 -3, oracle tolerance 10 -4, and inner budgets chosen so that each method performs exactly 1,210 first-order oracle calls. IPPM+SwSG runs 121 switching subgradient steps per epoch with step sizes 0. 05 / ( t + 1) and relaxation α = 0. 1; IPPM+ACGD keeps T in = 60, the same α = 0. 1, and no additional constraint shift; S-StarBL performs 605 bundle-level projections with α = 0. 3, β = 1; and S-BL+AdaLS executes five adaptive epochs of 121 bundle steps using α = 0. 3, β = 0. 5, λ = 0. 25, and starting bound η 0 = 0. 5 F ⋆ 1.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Scalablility to High Dimensions", "weight": 1.0} -->

The convergence and constraint satisfaction are illustrated in Figure 6. We observe that all four algorithms eventually satisfy the constraint up to a small tolerance of order 10 -3. Three algorithms, IPPM+ACGD, S-StarBL and S-BL+AdaLS, converge to the global optimal value F ∗ 1, precomputed by the CVX solver. As expected from theory, the convergence of IPPM+SwSG is relatively slow; although it improves the objective value and respects the constraint, it does not reach the optimum within the fixed number of oracle calls. Using faster ACGD inner solver shows a clear benefit compared to SwSG and solves the problem to high accuracy.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Scalablility to High Dimensions", "weight": 1.0} -->

The fastest algorithm is S-StarBL, which converges using less than 100 oracle calls, which is explained by its access to the optimal value F ∗ 1. S-BL+AdaLS also converges, but slightly slower due to its online adaptive estimation of optimal value F ∗ 1. We can also notice that SBL+AdaLS initially violates the constraint after the first outer loop iteration, however it quickly recovers afterwards and its final iterate results in a small constraint violation ≈ 3 · 10 -3. All above observations are in line with our theoretical upper complexity bounds in Sections 3.2 and 4.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we study a class of non-convex constrained problems under hidden convexity, proposing the first efficient algorithmic solutions under minimal assumptions.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Conclusion", "weight": 1.5} -->

- -While we established a strong baseline for hidden convex constrained optimization in terms of oracle complexity, our algorithms are fairly complicated. It would be interesting to develop simple singleloop methods without additional quadratic linearly constrained subproblems, e.g., similar to. - -Our oracle complexities match the best-known complexity in unconstrained setting; however, we still do not know what are the minimax optimal gradient complexities of hidden convex optimization. - -While we follow a common strategy of quadratic regularization in our PPM framework, an exploration of other natural choices is an interesting direction for future work. For example, it is conceptually possible to regularize the iterates in the U -space and leverage hidden convexity. While in general such approaches require knowledge of transformation c (·), this direction might be potentially useful in specific applications, e.g. convex reinforcement learning (CCMDP), where an approximation of c (·) can be used to improve regularization and/or act as a precondition.
