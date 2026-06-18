<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Improved Sample Complexity of Imitation Learning for Barrier Model Predictive Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent work in imitation learning has shown that having an expert controller that is both suitably smooth and stable enables stronger guarantees on the performance of the learned controller. However, constructing such smoothed expert controllers for arbitrary systems remains challenging, especially in the presence of input and state constraints. As our primary contribution, we show how such a smoothed expert can be designed for a general class of systems using a log-barrier-based relaxation of a standard Model Predictive Control (MPC) optimization problem. Improving upon our previous work, we show that barrier MPC achieves theoretically optimal error-to-smoothness tradeoff along some direction. At the core of this theoretical guarantee on smoothness is an improved lower bound we prove on the optimality gap of the analytic center associated with a convex Lipschitz function, which we believe could be of independent interest. We validate our theoretical findings via experiments, demonstrating the merits of our smoothing approach over randomized smoothing.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning has emerged as a powerful tool in machine learning, enabling agents to learn complex behaviors by imitating expert demonstrations acquired either from a human demonstrator or a policy computed offline \[pomerleau1988alvinn, ratliff2009learning, abbeel2010autonomous, ross2011reduction\]. Despite its significant success, imitation learning often suffers from a compounding error problem: Successive evaluations of the approximate policy could accumulate error, resulting in out-of-distribution failures \[pomerleau1988alvinn\]. Recent results in imitation learning \[pfrommer2022tasil, tu2022sample, block2023provable\] have identified *smoothness* (i.e., Lipschitzness of the derivative of the optimal controller with respect to the initial state) and *stability* of the expert as two key properties that circumvent this issue, thereby allowing for end-to-end performance guarantees for the final learned controller.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, our focus is on enabling such guarantees when the expert being imitated is a Model Predictive Controller (MPC), a powerful class of control algorithms based on solving an optimization problem over a receding prediction horizon \[borrelli2017predictive\]. In some cases, the solution to this multiparametric optimization problem, known as the explicit MPC representation \[bemporad2002explicit\], can be pre-computed. For instance, in our setup --- linear systems with polytopic constraints --- the optimal control input is a piecewise affine (and, hence, highly non-smooth) function of the state \[bemporad2002explicit\]. However, the number of these pieces may grow exponentially with the time horizon and the state and input dimension, which makes pre-computing and storing such a representation impractical in high dimensions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the approximation of a linear MPC controller has garnered significant attention \[chen2018approximating, maddalena2020neural, ahn2023model\], these prior works are primarily concerned with approximating the non-smooth explicit MPC using a neural network and then introducing schemes for enforcing the stability of the learned policy. In contrast, in our paper, we first construct a smoothed version of the expert and then apply theoretical results derived from the imitation of a smoothed expert.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we demonstrate --- both theoretically and empirically --- that a log-barrier formulation of the underlying MPC optimization yields smoothness properties similar to its randomized-smoothing-based counterpart, while being faster to compute. Similar to prior works \[wills2004barrier, feller2013barrier, feller2014barrier\], our barrier MPC formulation replaces the constraints in the MPC optimization problem by a log-barrier in the objective (cf. Section 4). We show that, in conjunction with a black-box imitation learning algorithm, this provides end-to-end guarantees on the performance of the learned policy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

It is known from classical optimization theory \[beck2012smoothing\] that any smooth approximation of a nonsmooth function which is $O{(\epsilon)}$ close everywhere must have a smoothness constant (Lipschitzness of the gradient) at least $O{({1/\epsilon})}$. The well-known randomized smoothing technique \[duchi2012randomized\] (convolution with a smoothing kernel) is optimal in this sense; however, it does not preserve the stability properties of the underlying controller and hence is not well-suited for controls applications.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Our main result is that log-barrier-based MPC \[wills2004barrier\] is an optimal smoother along some direction and outperforms randomized smoothing for controls tasks. More formally, for a given MPC, letting $u^{\star}$ be the solution of the explicit MPC and $u^{\eta}$ be the solution of the barrier-MPC formulation, with $\eta$ being the weight on the barrier, our main contributions for barrier MPC are as follows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We provide in Theorem 4.8 an upper bound of $O{(\frac{1}{\sqrt{\eta + d^{2}} - d)})}$ on the spectral norm of the Hessian of $u^{\eta}$ with respect to $x_{0}$, where $d$ is the distance of the unconstrained solution from the polytope boundary under the appropriate metric. Separately, we show that there exists a direction $a$ (independent of $\eta$) along which the error $a^{\top}{({u^{\eta} - u^{\star}})}$ is at most $O{({\sqrt{\eta + d^{2}} - d})}$. These two results together show that the controller smoothness and the error match along this direction $a$, from which we infer that barrier MPC is an optimal smoother along this direction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Along the way, we show (Lemma 4.6) that the Jacobian of the log-barrier solution can be written as a convex combination of the Jacobian of the solution of the explicit MPC. In particular, this shows that the rate of change of $u^{\eta}$ with respect to $x_{0}$ is bounded independent of the weight $\eta$ applied to the log barrier. We also show (Theorem 4.3) that overall, the distance of $u^{\eta}$ from $u^{\star}$ is bounded by $O{(\sqrt{\eta})}$. Finally, we demonstrate through numerical experiments that barrier MPC outperforms randomized smoothing, thus empirically affirming the merits of controls-aware smoothing techniques.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

A crucial technical component in obtaining the aforementioned bound on the controller smoothness is a lower bound on the distance of $u^{\eta}$ from the boundary of the polytope (equivalently, a lower bound on the optimality gap of the analytic center associated with a convex Lipschitz function). Intuitively, the nature of the self-concordant barrier already suggests that the solution to a problem with such a barrier in the objective cannot be too close to the boundary of the constraint set. However, obtaining the desired upper bound on the controller smoothness requires an *explicit quantification* of this distance. We provide (Theorem B.13) such a bound for general convex Lipschitz functions via a novel reduction to the setting of linear objectives and then invoking a result by \\citetzong2023short. Furthermore, our smoothing analysis demonstrates that our lower bound is tight up to constants. We believe this result could be broadly useful to the optimization community.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

We first state our notation and setup that we use throughout. The notation $\parallel \cdot \parallel$ refers to the $\ell_{2}$ norm $\parallel \cdot \parallel_{2}$ for vectors and, by extension, to the spectral norm (largest singular value) for square matrices. For a positive definite matrix $H$, we denote the local inner product ${\| x\|}_{H} = \sqrt{x^{\top}Hx}$. Unless transposed, all vectors are column vectors. We use uppercase letters for matrices and lowercase letters for vectors. For a vector $x$, we use ${Diag}{(x)}$ for the diagonal matrix with the entries of $x$ along its diagonal. We use $\lbrack n\rbrack$ for the set $\{ 1,2,\ldots,n\}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

Given a matrix $M \in {\mathbb{R}}^{n \times n}$ and $\sigma \in {\{ 0,1\}}^{n}$, we denote by ${\lbrack M\rbrack}_{\mathbf{σ}}$ the principal submatrix of $M$ corresponding to the rows and columns $i$ for which $\sigma_{i} = 1$. We use $M_{\mathbf{σ}}^{- 1}$ to denote the matrix obtained by first computing the inverse of the matrix ${\lbrack M\rbrack}_{\mathbf{σ}}$ and then appropriately padding it with zeroes so that the resulting matrix $M_{\mathbf{σ}}^{- 1}$ has the same size as $M$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

Similarly, we define $\operatorname{adj}{(M)}_{\mathbf{σ}}$ to be the matrix obtained by first computing the adjugate (the transpose of the cofactor matrix) of ${\lbrack M\rbrack}_{\mathbf{σ}}$ and then appropriately padding it with zeroes so that $\operatorname{adj}{(M)}_{\mathbf{σ}}$ has the same size as $M$. Lastly, $\mathcal{O}{( \cdot )}$ denotes expressions where numerical constants have been suppressed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

We use the same setup as in our previous work \[pfrommer2024sample\] and consider constrained discrete-time linear dynamical systems of the form,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

We consider deterministic state-feedback control policies of the form $\pi:{\mathcal{X}\rightarrow\mathcal{U}}$ and denote the closed-loop system under $\pi$ by ${f_{cl}^{\pi}{(x)}}:={{Ax} + {B\pi{(x)}}}$. We use ${\mathbf{π}}^{\star}$ to refer to the expert policy and $\hat{\mathbf{π}}$ to refer to its learned approximation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

In particular, our principal choice of ${\mathbf{π}}^{\star}$ in this paper is an MPC with quadratic cost and linear constraints.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

where $Q_{t}$ and $R_{t - 1}$ are positive definite for all $t \in {\lbrack T\rbrack}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

where the minimization is over the feasible set defined in Section 2. For ${\mathbf{π}}_{mpc}$ to be well-defined, we assume that $V{(x_{0},u)}$ has a unique global minimum in $u$ for all feasible $x_{0}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Explicit Solution to MPC", "weight": 1.0} -->

As first noted by \\citetbemporad2002explicit, explicit MPC rewrites Equation 2.4 as a multi-parametric quadratic program with linear inequality constraints and solves it for every possible combination of active constraints, building an analytical solution to the control problem. Following this known derivation (see \\citep\[Section 4\]bemporad2002explicit and \\citep\[Chapter 11\]borrelli2017predictive), we rewrite Equation 2.4

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

We assume that the constraint polytope in Section 2.1 contains a ball of radius $r$ and is contained inside an origin-centered ball of radius $R$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

We now state the solution to Section 2.1 and later (in Lemma 4.6) show how it appears in the smoothness of the barrier MPC solution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motivating Smoothness: Imitation Learning Frameworks", "weight": 1.0} -->

In this section, we instantiate the imitation learning framework to motivate our approach of barrier MPC. We use the Taylor series based imitation learning framework introduced by \\citetpfrommer2022tasil, which gives high-probability guarantees on the quality of an approximation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Taylor Series Imitation Learning", "weight": 1.0} -->

We first introduce the setting for imitation learning. Suppose we are given an expert controller ${\mathbf{π}}^{\star}$, a policy class $\Pi$, a distribution of initial conditions $\mathcal{D}$, and $N$ sample trajectories ${\{ x_{0:{K - 1}}^{(i)}\}}_{i = 1}^{N}$ of length $K$, with ${\{ x_{0}^{(i)}\}}_{i = 1}^{N}$ sampled i.i.d from $\mathcal{D}$. As formalized in Fact 3.6. ‣ 3.1 Taylor Series Imitation Learning ‣ 3 Motivating Smoothness: Imitation Learning Frameworks ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Taylor Series Imitation Learning", "weight": 1.0} -->

An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis]."), our goal is to find an approximate policy $\hat{\mathbf{π}} \in \Pi$ such that given a suitably small accuracy parameter $\epsilon$, the closed-loop states ${\hat{x}}_{t}$ and $x_{t}^{\star}$ induced by $\hat{\mathbf{π}}$ and ${\mathbf{π}}^{\star}$, respectively, satisfy, with high probability over $x_{0} \sim \mathcal{D}$,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Taylor Series Imitation Learning", "weight": 1.0} -->

To understand the sufficient conditions for such a guarantee, we now introduce a few definitions. We first assume through 3.1 that $\hat{\mathbf{π}}$ has been chosen by a black-box supervised imitation learning algorithm which, given the input data, produces a $\hat{\mathbf{π}} \in \Pi$ such that, with high probability over the distribution induced by $\mathcal{D}$, the policy and its Jacobian are close to the expert.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

As shown in \[pfrommer2022tasil\], an example in which 3.1 holds is when $\hat{\mathbf{π}}$ is chosen as an empirical risk minimizer from a class of twice differentiable parametric functions with $\ell_{2}$-bounded parameters, e.g., dense neural networks with smooth activation functions and trained with $\ell_{2}$ weight regularization. We refer the reader to \[pfrommer2022tasil, tu2022sample\] for other valid examples of $\Pi$. Further, note that the above definition requires generalization on only the state distribution induced by the expert, rather than on the distribution induced by the learned policy, as is the case in \[chen2018approximating, ahn2023model\].

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Next, we define a weaker variant of the standard *incremental input-to-state stability* ($\delta$ISS) \[vosswinkel2020determining\] and assume, in 3.3, that this property holds for the expert policy.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

The expert policy ${\mathbf{π}}^{\star}$ is ($\kappa,\gamma$)-locally incrementally input-to-state stable.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

As noted in \[pfrommer2022tasil\], local incremental input-to-state stability (local $\delta$ISS) is a much weaker criterion than regular incremental input-to-state stability. We will later show in Lemma 4.10 that under mild assumptions even input-to-state stabilizing (ISS) policies (defined in (Definition 4.9. ‣ 4.4 Learning Guarantees for Barrier MPC ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis]."))) are locally $\delta$ISS.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

There is considerable prior work (see, e.g., \[zamani2011lyapunov, pouilly2020stability\]) demonstrating that ISS holds under mild conditions for both the explicit MPC and the barrier-based MPC under consideration in this paper. Putting these facts together then implies local $\delta$ISS of barrier MPC. Having established some preliminaries for stability, we now move on to the smoothness property we consider.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.5", "weight": 1.0} -->

At a high level, assuming smoothness of the expert and the learned policy helps implicitly ensure that the learned policy captures the stability of the expert in a neighborhood around the data distribution. If the expert or learned policy were to be only piecewise smooth (as is the case, e.g., with standard MPC-based solution of LQR), a transition from one piece to another in the expert not replicated by the learned policy could result in unstable closed-loop behavior.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 3.5", "weight": 1.0} -->

Having stated all the necessary assumptions, we are now ready to state below the main export of this section, given by \[pfrommer2022tasil\], guaranteeing closeness of the learned and expert policies.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Fact 3.6 (\\[pfrommer2022tasil\\], Corollary A.1)", "weight": 1.0} -->

The upshot of this result is that provided the MPC policy ${\mathbf{π}}^{\star}$ is $(L_{0},L_{1})$-smooth, to match the trajectory of ${\mathbf{π}}^{\star}$ with high probability, we need to match the Jacobian and value of ${\mathbf{π}}^{\star}$ on *only* $NK$ pieces. This is in contrast to prior work such as \[maddalena2020neural, karg2020efficient, chen2018approximating\] on approximating explicit MPC, which require sampling new control inputs during training (in a reinforcement learning-like fashion) or post-training verification of the stability properties of the network.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Fact 3.6 (\\[pfrommer2022tasil\\], Corollary A.1)", "weight": 1.0} -->

However, as we noted in Section 1, these strong guarantees crucially require a smooth expert controller. We investigate two approaches for smoothing ${\mathbf{π}}_{mpc}$: randomized smoothing and barrier MPC. Before doing so, we first consider what constitutes an "optimal" smoothing approach in terms of the smallest possible Hessian norm for a given level of approximation error.

<!-- chunk {"id": "body-0036", "role": "body", "section": "An Overview of Optimal Smoothing", "weight": 1.0} -->

We begin by considering the properties of a general smoothing algorithm. For simplicity, in this section, we consider smoothing functions of the form $f:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$, although we note that this analysis can easily be extended to $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ by considering arbitrary paths ${\mathbb{R}}\rightarrow{\mathbb{R}}^{n}$ and projection ${\mathbb{R}}^{m}\rightarrow{\mathbb{R}}$. This motivates the following definition of a smoothing algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "First Approach: Randomized Smoothing", "weight": 1.0} -->

We first consider randomized smoothing (see, e.g., \[duchi2012randomized\]) as a baseline approach for smoothing the expert policy ${\mathbf{π}}^{\star}$. Here, the imitator is learned with a loss function that randomly samples with noise drawn from a chosen probability distribution in order to smooth the policy, effectively convolving the controller with a smoothing kernel. This approach corresponds to the following controller.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Fact 3.13 (\\\\citet\\[Appendix E\\]duchi2012randomized)", "weight": 1.0} -->

This implies that randomized smoothing is an optimal smoother for the given choices of $\mathcal{P}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Fact 3.13 (\\\\citet\\[Appendix E\\]duchi2012randomized)", "weight": 1.0} -->

However, using randomized smoothing to obtain a smoothed policy has three key disadvantages. First, ${\mathbb{E}}_{w \sim \mathcal{P}}{\lbrack{{\mathbf{π}}_{mpc}{({x + {\epsilon w}})}}\rbrack}$ is evaluated via sampling, which means the expert policy must be continuously re-evaluated during training in order to guarantee convergence to the smoothed policy. Secondly, smoothing in this manner may cause ${\mathbf{π}}^{rs}$ to violate state constraints. Finally, simply smoothing the policy may not preserve the stability of ${\mathbf{π}}_{mpc}$. The first two stated problems arise due to randomized smoothing *oversmoothing* the underlying controller. Consider the following example.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 3.14", "weight": 1.0} -->

Consider the system ${f{(x_{t},u_{t})}} = {{2x_{t}} + u_{t}}$ and controller ${\pi^{\star}{(x)}} = {\min{({\max{({- {2x}},{- 1})}},1)}}$. We can see that as $\sigma\rightarrow\infty$ (where $\sigma$ is the smoothing parameter from Definition 3.12. ‣ 3.3 First Approach: Randomized Smoothing ‣ 3 Motivating Smoothness: Imitation Learning Frameworks ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 3.14", "weight": 1.0} -->

An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].")), we have ${\pi^{rs}{(x)}}\rightarrow 0$ for all $x$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 3.14", "weight": 1.0} -->

The above example shows that $\pi^{rs}$ is not stable for high $\sigma$. Ideally, we would like to aggressively smooth only the discontinuities that do not affect stability or constraint guarantees. This requires a smoothing technique that is aware of when more aggressive control inputs are being taken in order to more quickly stabilize versus preserve some constraint guarantees. As we shall show, barrier MPC is precisely one such method that also preserves state guarantees. We now define barrier MPC and bound the approximation error and smoothness of the resulting controller.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Our Approach to Smoothing: Barrier MPC", "weight": 1.0} -->

Having described the guarantees obtained via randomized smoothing, we now consider smoothing via self-concordant barrier functions, a notion introduced by \\citetnesterov1994interior.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problem 4.2 (Barrier MPC)", "weight": 1.0} -->

Given an MPC as in Section 2.1 and weight $\eta > 0$, the barrier MPC is defined by minimizing, over the input sequence $u \in {\mathbb{R}}^{T \cdot d_{u}}$, the cost

<!-- chunk {"id": "body-0045", "role": "body", "section": "Problem 4.2 (Barrier MPC)", "weight": 1.0} -->

where ${\phi{(x_{0},u)}} = {{{Px_{0}} + w} - {Gu}} \in {\mathbb{R}}^{m}$ is the (vector) residual of constraints for $x_{0}$ and $u$, and the vector $d$ is set to $d:={{\nabla_{u}{\sum_{i = 1}^{m}{\log{({\phi_{i}{(0,u)}})}}}}|}_{u = 0}$. We denote by $u^{\eta}{(x_{0})}$ the minimizer of 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Problem 4.2 (Barrier MPC)", "weight": 1.0} -->

Some remarks are in order. First, the choice of $d$ in 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problem 4.2 (Barrier MPC)", "weight": 1.0} -->

An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].") is made so as to ensure that ${{{\arg\min}_{u^{\eta}}\mathcal{V}^{\eta}}{(0,u^{\eta})}} = 0$, i.e. that ${\mathbf{π}}_{mpc}^{\eta}$ satisfies ${{\mathbf{π}}_{mpc}^{\eta}{}} = {{\mathbf{π}}_{mpc}{}} = 0$, which is a necessary condition for the controller to be stabilizing at the origin. Further, note that ${\| d\|}^{2}$ is a constant by construction, a fact that turns out to be useful in Theorem 4.8.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Problem 4.2 (Barrier MPC)", "weight": 1.0} -->

Secondly, the technical assumptions about the constraint polytope in Section 2.1 containing a full-dimensional ball of radius $r$ and being contained inside an origin-centered ball of radius $R$ are both inherited by 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].").

<!-- chunk {"id": "body-0049", "role": "body", "section": "Error Bound for Barrier MPC", "weight": 1.0} -->

To kick off our analysis of the barrier MPC, we first give the following upper bound on the distance between the optimal solution of 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].") and that of explicit MPC in Section 2.1. Our result is based on standard techniques to analyze the sub-optimality gap in interior-point methods and crucially uses the strong convexity of our quadratic cost in 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Error Bound for Barrier MPC", "weight": 1.0} -->

An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].").

<!-- chunk {"id": "body-0051", "role": "body", "section": "First-Derivative Bound for the Barrier MPC", "weight": 1.0} -->

To prove our main result (Theorem 4.8) on the spectral norm of the Hessian, we first establish the following technical result bounding the first derivative of $u^{\eta}$ with respect to $x_{0}$. This result may be of independent interest, since it formulates the Jacobian of the log-barrier smoothed solution as a convex combination of derivatives associated with sets of active constraints from the original MPC problem. Our proof starts with the first-order optimality condition for $u^{\eta}$ and obtains the desired simplification by applying the Sherman-Morrison-Woodbury identity (Fact A.3. ‣ Appendix A Technical Results from Matrix Analysis ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].")).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Main Result: Smoothness Bound for the Barrier MPC", "weight": 1.0} -->

We are now ready to state our main result, which effectively shows that $u^{\eta}$ (and hence ${\mathbf{π}}_{mpc}^{\eta}$) satisfies the conditions of 3.5. Our proof of Theorem 4.8 starts with Lemma 4.5 and computes another derivative. To get an upper bound on the operator norm of the Hessian so obtained, our proof then crucially hinges on Lemma B.11 and Theorem B.13, which provide explicit lower bounds on residuals when minimizing a quadratic cost plus a self-concordant barrier over a polytope, a result we believe to be of independent interest to the optimization community.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Learning Guarantees for Barrier MPC", "weight": 1.0} -->

We now revisit the learning guarantees discussed in Section 3, adapted specifically to a log-barrier MPC expert. We begin by considering the stability properties of barrier MPC. Since we are interested in establishing ${\|{{\hat{x}}_{t} - x_{t}^{\star}}\|} \leq \epsilon$, where $\hat{x}$ is the state under the learned policy and $x^{\star}$ is the state under the expert, and since we consider MPC controllers which stabilize to the origin, we can relax our local incremental input-to-state stability requirements to simply input-to-state stability (ISS) with minimal assumptions. Definition 4.9. ‣ 4.4 Learning Guarantees for Barrier MPC ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Learning Guarantees for Barrier MPC", "weight": 1.0} -->

An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].") introduces this weaker input-to-state stability property, and Lemma 4.10 shows that ISS policies are locally $\delta$ISS. We then observe that there is considerable prior work showing that ISS holds under minimal assumptions for barrier MPC, meaning 3.3 is satisfied for barrier MPC.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 4.11", "weight": 1.0} -->

The parameters of the barrier MPC controller ${\mathbf{π}}_{mpc}^{\eta}$ in 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].") are chosen such that the system is input-to-state stabilizing. Consequently, by Lemma 4.10 and Corollary 4.7, it is incrementally input-to-state stabilizing over $t \leq K$ for some with linear gain function $\gamma$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 4.11", "weight": 1.0} -->

This shows that ${\mathbf{π}}_{mpc}^{\eta}$ satisfies the even weaker notion of locally $\delta$ISS as required in 3.3. We now state our end-to-end learning guarantee, an extension of Fact 3.6. ‣ 3.1 Taylor Series Imitation Learning ‣ 3 Motivating Smoothness: Imitation Learning Frameworks ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].").

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

The experiments presented below first appeared in our previous work \[pfrommer2024sample\]. We include these here for completeness.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

We demonstrate the advantage of barrier MPC over randomized smoothing for the double integrator system visualized in Figure 1. The matrices describing the dynamics are $A = \begin{bmatrix}
\end{bmatrix}$ and $B = \begin{bmatrix}
\end{bmatrix}$, and the cost matrices are given by $Q_{t} = I$, $R_{t} = {0.01I}$, with horizon length $T = 10$. Our constraints for 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].") are ${\| x\|}_{\infty} \leq 10$ and ${\| u\|}_{\infty} \leq 1$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiments", "weight": 1.0} -->

This is the same setup as in \[ahn2023model\], which we note asymptotically stabilizes the system to the origin.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Experiments", "weight": 1.0} -->

We sample $N \in {\{ 20,50\}}$ trajectories of length $K = 20$ using ${\mathbf{π}}_{mpc}^{\eta}$ and ${\mathbf{π}}^{rs}$ and smoothing parameters $\eta$ (4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024. An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].")) and $\sigma$ (Definition 3.12. ‣ 3.3 First Approach: Randomized Smoothing ‣ 3 Motivating Smoothness: Imitation Learning Frameworks ‣ Improved Sample Complexity of Imitation Learning for Barrier Model Predictive ControlThe first two authors contributed equally. This work extends our previous result in [pfrommer2024sample], which has been accepted for publication in CDC 2024.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experiments", "weight": 1.0} -->

An earlier version of this manuscript was submitted as part of DP’s Master’s thesis [pfrommer2024samplethesis].")) ranging from $10^{- 4}$ to $10^{3}$ and $10^{- 4}$ to $20$, respectively. We use $\mathcal{P} = {\mathcal{N}{(0,I)}}$ for the randomized smoothing distribution. For each parameter set, we trained a 4-layer multi-layer perceptron (MLP) using GELU activations \[hendrycks2016gaussian\] to ensure smoothness of $\Pi$. We used AdamW \[loshchilov2018decoupled\] with a learning rate of $3 \cdot 10^{- 4}$ and weight decay of $10^{- 3}$ in order to ensure boundedness of the weights (see \[pfrommer2022tasil\]).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experiments", "weight": 1.0} -->

We visualize the smoothness properties of the chosen expert ${\mathbf{π}}^{\star}$ of each method (either ${\mathbf{π}}_{mpc}^{\eta}$ or ${\mathbf{π}}^{rs}$) across the choices of $\eta,\sigma$ in Figure 3. For small Hessian norms (i.e. the large $\eta,\sigma$ regime), barrier MPC has larger gradient norm $\|{\nabla{\mathbf{π}}^{\star}}\|$ than randomized smoothing. This shows that ${\mathbf{π}}_{mpc}^{\eta}$ prevents oversmoothing in comparison to ${\mathbf{π}}^{rs}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experiments", "weight": 1.0} -->

While randomized smoothing reduces $\|{\nabla^{2}{\mathbf{π}}^{\star}}\|$ by essentially flattening the function, ${\mathbf{π}}_{mpc}^{\eta}$ achieves equally smooth functions while still maintaining control of the system. This effect is also seen in Figure 2, where we visualize the barrier MPC controller for different $\eta$ and see that, even for large $\eta$, we successfully stabilize to the origin.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experiments", "weight": 1.0} -->

One interesting phenomenon is that the maximum gradient of ${\mathbf{π}}_{mpc}^{\eta}$ begins decreasing much earlier than ${\mathbf{π}}^{rs}$. This is due to the fact that ${\mathbf{π}}^{rs}$ smooths only locally, meaning that if the smoothing radius is sufficiently small, the gradient will not be affected. Meanwhile, ${\mathbf{π}}_{mpc}^{\eta}$ always performs a *global* form of smoothing, so even for small $\eta$, the controller is smoothed everywhere.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Figure 3, we also compare the trajectory error when imitating trajectories from ${\mathbf{π}}^{rs},{\mathbf{π}}_{mpc}^{\eta}$ for equivalent levels of smoothness. We can see that for $N = 20$ and $N = 50$, ${\mathbf{π}}_{mpc}^{\eta}$ significantly outperforms ${\mathbf{π}}^{rs}$ across all smoothness levels. This effect is particularly pronounced in the very smooth regime, where imitating ${\mathbf{π}}^{rs}$ proves unstable due to the inherit instability of $(A,B)$, leading to extremely large imitation errors. Meanwhile, ${\mathbf{π}}_{mpc}^{\eta}$ is strictly easier to imitate the more smoothing that is applied. Overall, these experiments confirm our hypothesis that not all smoothing techniques perform equally and that barrier MPC is an effective smoothing technique that outperforms randomized smoothing for the purposes of imitation learning.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion", "weight": 1.5} -->

We consider two methods for smoothing MPC policies for constrained linear systems: randomized smoothing and barrier MPC. While the former is known to have the theoretically optimal ratio of approximation error to Hessian norm, it may not preserve the stability or constraint satisfaction properties of the underlying controller and hence is not always well-suited for controls applications. We show that the log-barrier-based MPC yields a smooth control with optimal error to smoothness ratio along some direction. Additionally, it better ensures constraint satisfaction while also retaining the stability properties of the original policy. We show how these properties enable theoretical guarantees when learning barrier MPC and demonstrate experimentally its better performance compared to a randomized smoothing baseline.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our key technical contribution towards proving the smoothness of barrier MPC is a lower bound on the optimality gap of the analytic center associated with a convex Lipschitz function, which we hope could be of independent interest to the broader optimization community. Extending our results to smoothing nonlinear MPC policies would be a fruitful direction for future work.
