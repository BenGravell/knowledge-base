<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Sample Complexity of Imitation Learning for Smoothed Model Predictive Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent work in imitation learning has shown that having an expert controller that is both suitably smooth and stable enables stronger guarantees on the performance of the learned controller. However, constructing such smoothed expert controllers for arbitrary systems remains challenging, especially in the presence of input and state constraints. As our primary contribution, we show how such a smoothed expert can be designed for a general class of systems using a log-barrier-based relaxation of a standard Model Predictive Control (MPC) optimization problem. At the crux of this theoretical guarantee on smoothness is a new lower bound we prove on the optimality gap of the analytic center associated with a convex Lipschitz function, which we hope could be of independent interest. We validate our theoretical findings via experiments, demonstrating the merits of our smoothing approach over randomized smoothing.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imitation learning has emerged as a powerful tool in machine learning, enabling agents to learn complex behaviors by imitating expert demonstrations acquired either from a human demonstrator or a policy computed offline \[pomerleau1988alvinn, ratliff2009learning, abbeel2010autonomous, ross2011reduction\]. Despite its significant success, imitation learning often suffers from a compounding error problem: Successive evaluations of the approximate policy can accumulate error, resulting in out-of-distribution failures \[pomerleau1988alvinn\]. Recent results \[pfrommer2022tasil, tu2022sample, block2023provable\] have identified *smoothness* (i.e. the derivative, with respect to the state, of the control policy being Lipschitz) and *stability* of the expert as two key properties that enable circumventing this issue, thereby allowing for end-to-end performance guarantees for the final learned controller.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, our focus is on enabling such guarantees when the expert being imitated is a Model Predictive Controller (MPC), a powerful class of control algorithms based on solving an optimization problem over a receding prediction horizon \[allgower2012nonlinear\]. In some cases, the solution to this multiparametric optimization problem, known as the explicit MPC representation \[bemporad2002explicit\], can be pre-computed. For our setup --- linear systems with polytopic constraints --- the optimal control input is known to be a piecewise affine function of the state. However, the number of these pieces may grow exponentially with the time horizon and the state and input dimension, which could render pre-computing and storing such a representation impractical in high dimensions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the approximation of a linear MPC controller has garnered significant attention \[maddalena2020neural, chen2018approximating, ahn2023model\], prior works typically approximate the (non-smooth) explicit MPC with a neural network and introduce schemes to enforce the stability of the learned policy. In contrast, we construct a smoothed version of the expert and apply stronger theoretical results for the imitation of a smoothed expert.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we demonstrate --- both theoretically and empirically --- that a log-barrier formulation of the underlying MPC optimization yields the same desired smoothness properties as its randomized-smoothing-based counterpart, while being faster to compute. Our barrier MPC formulation replaces the constraints in the MPC optimization problem with "soft constraints" using the log-barrier (cf. Section 4). We show that, when used in conjunction with a black-box imitation learning algorithm, this enables end-to-end guarantees on the performance of the learned policy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

We first state our notation and setup. The notation $\parallel \cdot \parallel$ refers to the $\ell_{2}$ norm $\parallel \cdot \parallel_{2}$. Unless transposed, all vectors are column vectors. For a vector $x$, we use ${Diag}{(x)}$ for the diagonal matrix with the entries of $x$ along its diagonal. We use $\lbrack n\rbrack$ for the set $\{ 1,2,\ldots,n\}$. Given $M \in {\mathbb{R}}^{n \times n}$ and $\sigma \in {\{ 0,1\}}^{n}$, we denote by ${\lbrack M\rbrack}_{\sigma}$ the principal submatrix, of $M$, with rows and columns $i$ for which $\sigma_{i} = 1$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

We additionally use $M_{\sigma}^{- 1}$ and $\operatorname{adj}{(M)}_{\sigma}$ to denote, respectively, the inverse and adjugate (the transpose of the cofactor matrix) of ${\lbrack M\rbrack}_{\sigma}$, appropriately padded with zeros back to the size of $M$, at same location.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

For notational convenience, we overload $\phi$ to compactly denote the vector of constraint residuals for a state $x$ and input $u$ as well as for the sequences $x_{1:T}$ and $u_{0:{T - 1}}$: We consider deterministic state-feedback control policies of the form $\pi:{X\rightarrow U}$ and denote the closed-loop system under $\pi$ by ${f_{cl}^{\pi}{(x)}}:={{Ax} + {B\pi{(x)}}}$. We use $\pi^{\star}$ to refer to the expert policy and $\hat{\pi}$ for its learned approximation. In particular, our choice of $\pi^{\star}$ in this paper is an MPC with quadratic cost and linear constraints.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup and Background", "weight": 1.0} -->

The MPC policy is obtained by solving the following minimization problem over future actions $u:=u_{0:{T - 1}}$ with quadratic cost in $u$ and states $x:=x_{1:T}$: where $Q_{t}$ and $R_{t - 1}$ are positive definite for all $t \in {\lbrack T\rbrack}$. For a given state $x$, the corresponding input ${\mathbf{π}}_{mpc}$ of the MPC is: where the minimization is over the feasible set defined in Section 2. For ${\mathbf{π}}_{mpc}$ to be well-defined, we assume that $V{(x_{0},u)}$ has a unique global minimum in $u$ for all feasible $x_{0}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Explicit Solution to MPC", "weight": 1.0} -->

Explicit MPC \[bemporad2002explicit\] rewrites Equation 2.4 as a multi-parametric quadratic program with linear inequality constraints and solves it for every possible combination of active constraints, building an analytical solution to the control problem.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Explicit Solution to MPC", "weight": 1.0} -->

We assume that the constraint polytope in Section 2.1 contains a full-dimensional ball of radius $r$ and is contained inside an origin-centered ball of radius $R$. Consequently, its objective is $L_{V}$-Lipschitz for some constant $L_{V}$. We now state the solution of Section 2.1 \[alessio2009survey\] and later (in Lemma 4.5) show how it appears in the smoothness of the barrier MPC solution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Fact 2.1 (\\[bemporad2002explicit\\])", "weight": 1.0} -->

Let $\sigma \in {\{ 0,1\}}^{m}$ denote a set of active constraints for Section 2.1, with $\sigma_{i} = 1$ iff the $i$th constraint is active. We overload this notation so that $\sigma{(x_{0})}$ represents active constraints of the solution of Section 2.1 for a particular $x_{0}$. Let $P_{\sigma} = \left. \{ x \middle| {{\sigma{(x)}} = \sigma}\} \right.$ be the the set of $x_{0}$ for which the solution has active constraints $\sigma$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Fact 2.1 (\\[bemporad2002explicit\\])", "weight": 1.0} -->

Then for $x_{0} \in P_{\sigma}$, the solution $u$ of Section 2.1 may be expressed as $u = {{K_{\sigma}x_{0}} + k_{\sigma}}$, where $K_{\sigma}$ and $k_{\sigma}$ are defined as: Based on this fact, one may pre-compute an efficient lookup structure mapping $x \in P_{\sigma}$ to $K_{\sigma},k_{\sigma}$. However, since every combination of active constraints may potentially yield a unique feedback law, the number of pieces to be computed may grow exponentially in the problem dimension or time horizon. For instance, even the simple two-dimensional toy system in Figure 1 has $261$ pieces. In high dimensions or over long time horizons, merely enumerating all pieces of the explicit MPC may be computationally intractable.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Fact 2.1 (\\[bemporad2002explicit\\])", "weight": 1.0} -->

This observation motivates us to consider approximating explicit MPC using a polynomial number of sample trajectories, collected offline. We introduce this framework next.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Motivating Smoothness: Imitation Learning Frameworks", "weight": 1.0} -->

In this section, we motivate barrier MPC by specializing to the setting of Section 2 the framework from \[pfrommer2022tasil\], which enables high-probability guarantees on the quality of an approximation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivating Smoothness: Imitation Learning Frameworks", "weight": 1.0} -->

Suppose we are given an expert controller $\pi^{\star}$, a policy class $\Pi$, a distribution of initial conditions $\mathcal{D}$, and $N$ sample trajectories ${\{ x_{0:{K - 1}}^{(i)}\}}_{i = 1}^{N}$ of length $K$, with ${\{ x_{0}^{(i)}\}}_{i = 1}^{N}$ sampled i.i.d from $\mathcal{D}$. Our goal is to find an approximate policy $\hat{\pi} \in \Pi$ such that, given an accuracy parameter $\epsilon$, the closed-loop states ${\hat{x}}_{t}$ and $x_{t}^{\star}$ induced by $\hat{\pi}$ and $\pi^{\star}$, respectively, satisfy, with high probability over $x_{0} \sim \mathcal{D}$, This is formalized in 3.6.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivating Smoothness: Imitation Learning Frameworks", "weight": 1.0} -->

‣ 3 Motivating Smoothness: Imitation Learning Frameworks ‣ On the Sample Complexity of Imitation Learning for Smoothed Model Predictive ControlThe first two authors contributed equally. A preliminary version of this manuscript is published in CDC 2024."). To understand this statement, we first establish some assumptions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivating Smoothness: Imitation Learning Frameworks", "weight": 1.0} -->

We first assume through 3.1 that $\hat{\pi}$ has been chosen by a black-box supervised imitation learning algorithm which, given the input data, produces a $\hat{\pi} \in \Pi$ such that, with high probability over the distribution induced by $\mathcal{D}$, the policy and its Jacobian are close to the expert.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

For some ${\delta \in {}},{{\epsilon_{0} > 0},{\epsilon_{1} > 0}}$ and given $N$ trajectories ${\{ x_{0:{K - 1}}^{(i)}\}}_{i = 1}^{(N)}$ of length $K$ sampled i.i.d. from $\mathcal{D}$ and rolled out under $\pi^{\star}$, the approximating policy $\hat{\pi}$ satisfies: For instance, as shown in \[pfrommer2022tasil\], 3.1 holds for $\hat{\pi}$ chosen as an empirical risk minimizer from a class of twice differentiable parametric functions with $\ell_{2}$-bounded parameters, e.g., dense neural networks with smooth activation functions and trained with $\ell_{2}$ weight regularization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

We refer the reader to \[pfrommer2022tasil, tu2022sample\] for other such examples of $\Pi$. Note the above definition requires generalization on only the state distribution induced by the expert, rather than the distribution induced by the learned policy, as in \[ahn2023model, chen2018approximating\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Next, we define a weaker variant of the standard *incremental input-to-state stability* ($\delta$ISS) \[vosswinkel2020determining\] and assume, in 3.3, that this property holds for the expert policy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

The expert policy $\pi^{\star}$ is ($\eta,\gamma$)-locally incrementally stable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

As noted in \[pfrommer2022tasil\], local $\delta$ISS is a much weaker criterion than even just regular incremental input-to-state stability. There is considerable prior work demonstrating that ISS (and $\delta$ISS) holds under mild conditions for both the explicit MPC and the barrier-based MPC under consideration in this paper \[pouilly2020stability\]. We refer the reader to \[zamani2011lyapunov\] for more details. Having established some preliminaries for stability, we now move on to the smoothness property we consider.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3.5", "weight": 1.0} -->

At a high level, by assuming smoothness of the expert and the learned policy, we can implicitly ensure that the learned policy captures the stability of the expert in a neighborhood around the data distribution. If the expert or learned policy were to be only piecewise smooth, a transition from one piece to another in the expert, which is not replicated by the learned policy, could lead to unstable closed-loop behavior.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3.5", "weight": 1.0} -->

Having stated all the necessary assumptions, we are now ready to state below the main export of this section, guaranteeing closeness of the learned and expert policies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Fact 3.6 (cf. \\[pfrommer2022tasil\\], Corollary A.1)", "weight": 1.0} -->

This is in contrast to prior work such as \[maddalena2020neural, karg2020efficient, chen2018approximating\] on approximating explicit MPC, which require sampling new control inputs during training (in a reinforcement learning-like fashion) or post-training verification of the stability properties of the network.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Fact 3.6 (cf. \\[pfrommer2022tasil\\], Corollary A.1)", "weight": 1.0} -->

However, as we noted in 3.5, these strong guarantees crucially require a smooth expert controller. In the following sections, we investigate two approaches for smoothing ${\mathbf{π}}_{mpc}$: randomized smoothing and barrier MPC.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Randomized Smoothing", "weight": 1.0} -->

We first consider randomized smoothing \[duchi2012randomized\] as a baseline approach for smoothing $\pi^{\star}$. Here, the imitator $\pi^{rs}$ is learned with a loss function that randomly samples noise drawn from a probability distribution chosen to smooth the policy. This approach corresponds to the following controller.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Fact 3.8 (c.f. \\[duchi2012randomized\\], Appendix E, Lemma 7-9)", "weight": 1.0} -->

For $\mathcal{P} \in {\{{{Unif}{({B_{\ell_{2}}{}})}},{{Unif}{({B_{\ell_{\infty}}{}})}},{\mathcal{N}{(0,I)}}\}}$, there exist $L_{0},L_{1}$ that depend on $d_{x}$ and the Lipschitz constant of ${\mathbf{π}}_{mpc}$ such that Using randomized smoothing to obtain a smoothed policy has the following key disadvantages: Firstly the expectation ${\mathbb{E}}_{w \sim \mathcal{P}}{\lbrack{{\mathbf{π}}_{mpc}{({x + {\epsilon w}})}}\rbrack}$ is evaluated via sampling, which means the policy must be continuously re-evaluated during training in order to guarantee a smooth learned policy.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Fact 3.8 (c.f. \\[duchi2012randomized\\], Appendix E, Lemma 7-9)", "weight": 1.0} -->

Secondly, smoothing in this manner may cause $\pi^{rs}$ to violate state constraints. Finally, simply smoothing the policy may not preserve the stability of ${\mathbf{π}}_{mpc}$. As we shall show, using barrier MPC as a smoothed policy overcomes all these drawbacks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Our Approach to Smoothing: Barrier MPC", "weight": 1.0} -->

Having described the guarantees obtained via randomized smoothing, we now consider smoothing via barrier functions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem 4.2 (Barrier MPC)", "weight": 1.0} -->

The following result, based on standard techniques to analyze the sub-optimality gap in interior-point methods, bounds the distance between the optimal solution of 4.2. ‣ 4 Our Approach to Smoothing: Barrier MPC ‣ On the Sample Complexity of Imitation Learning for Smoothed Model Predictive ControlThe first two authors contributed equally. A preliminary version of this manuscript is published in CDC 2024.") and that of explicit MPC in Section 2.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We demonstrate the advantage of barrier MPC over randomized smoothing for the toy double integrator system visualized in Figure 1. We sample $N \in {\lbrack 20,50\rbrack}$ trajectories of length $K = 20$ using ${\mathbf{π}}_{mpc}^{\eta}$ and $\pi^{rs}$ with a horizon length $T = 10$ and smoothing parameters $\eta$ and $\epsilon$ ranging from $10^{- 4}$ to $10^{3}$ and $10^{- 4}$ to $20$, respectively. We use $\mathcal{P} = {\mathcal{N}{(0,I)}}$ for the randomized smoothing distribution. For each parameter set, we trained a 4-layer multi-layer perceptron (MLP) using GELU activations \[hendrycks2016gaussian\] to ensure smoothness of $\Pi$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Figure 3, we visualize the smoothness properties of the chosen $\pi^{\ast}$ for each method across the choices of $\eta,\epsilon$. We also show the imitation error $\max_{t}{\|{x^{\star} - \hat{x}}\|}$ for the learned MLP as a function of the expert smoothness. For more smooth experts, we observe that barrier MPC outperforms randomized smoothing, even in the lower-data setting. These experiments confirm our hypothesis: barrier MPC is an effective smoothing technique (preserving both stability and constraints) that outperforms randomized smoothing.
