<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Robust Control for LQR Systems with Multiplicative Noise via Policy Gradient

Topics include Gradient method, Gradient descent, Natural gradients, Reinforcement learning, Policy gradients, Linear systems, Uncertain systems, Optimal control, Stochastic systems, Multiplicative noise, Non-convex, Dynamics, Global convergence, Linear quadratic regulator.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides non-asymptotic finite-sample convergence results for policy gradient algorithms applied to the problem of optimal control of linear systems with multiplicative noise when the dynamics and noise covariances are unknown.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The linear quadratic regulator (LQR) problem has reemerged as an important theoretical benchmark for reinforcement learning-based control of complex dynamical systems with continuous state and action spaces. In contrast with nearly all recent work in this area, we consider multiplicative noise models, which are increasingly relevant because they explicitly incorporate inherent uncertainty and variation in the system dynamics and thereby improve robustness properties of the controller. Robustness is a critical and poorly understood issue in reinforcement learning; existing methods which do not account for uncertainty can converge to fragile policies or fail to converge at all. Additionally, intentional injection of multiplicative noise into learning algorithms can enhance robustness of policies, as observed in ad hoc work on domain randomization. Although policy gradient algorithms require optimization of a non-convex cost function, we show that the multiplicative noise LQR cost has a special property called gradient domination, which is exploited to prove global convergence of policy gradient algorithms to the globally optimum control policy with polynomial dependence on problem parameters. Results are provided both in the model-known and model-unknown settings where samples of system trajectories are used to estimate policy gradients.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning-based control has recently achieved impressive successes in games [silver2016mastering,silver2018general] and simulators [mnih2015human]. But these successes are significantly more challenging to translate to complex physical systems with continuous state and action spaces, safety constraints, and non-negligible operation and failure costs that demand data efficiency. An intense and growing research effort is creating a large array of models, algorithms, and heuristics for approaching the myriad of challenges arising from these systems. To complement a dominant trend of more computationally focused work, the canonical linear quadratic regulator (LQR) problem in control theory has reemerged as an important theoretical benchmark for learning-based control [recht2018tour,dean2017sample]. Despite its long history, there remain fundamental open questions for LQR with unknown models, and a foundational understanding of learning in LQR problems can give insight into more challenging problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Almost all recent work on learning in LQR problems has utilized either deterministic or additive noise models [recht2018tour,dean2017sample,Fazel2018,Bradtke1994,fiechter1997pac,abbasi2011regret,lewis2012reinforcement,tu2017least,abeille2018improved,umenberger2018learning,mania2019certainty,venkataraman2018recovering], but here we consider multiplicative noise models. In control theory, multiplicative noise models have been studied almost as long as their deterministic and additive noise counterparts [Wonham1967,Damm2004], although this area is somewhat less developed and far less widely known. We believe the study of learning in LQR problems with multiplicative noise is important for three reasons.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, this class of models is much richer than deterministic or additive noise while still allowing exact solutions when models are known, which makes it a compelling additional benchmark [willems1976feedback,athans1977uncertainty,bernstein1987robust]. Second, they explicitly incorporate model uncertainty and inherent stochasticity, thereby improving robustness properties of the controller. Robustness is a critical and poorly understood issue in reinforcement learning; existing methods which do not account for uncertainty can converge to fragile policies or fail to converge at all [athans1977uncertainty,ku1977further,bertsekas1995dynamic]. Additionally, intentional injection of multiplicative noise into learning algorithms is known to enhance robustness of policies from ad hoc work on domain randomization [tobin2017domain].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, in emerging difficult-to-model complex systems where learning-based control approaches are perhaps most promising, multiplicative noise models are increasingly relevant; examples include networked systems with noisy communication channels [antsaklis2007special,hespanha2007survey], modern power networks with large penetration of intermittent renewables [carrasco2006power,milano2018foundations], turbulent fluid flow [lumley2007stochastic], and neuronal brain networks [breakspear2017dynamic].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Related literature", "weight": 1.0} -->

Multiplicative noise LQR problems have been studied in control theory since the 1960s [Wonham1967]. Since then a line of research parallel to deterministic and additive noise has developed, including basic stability and stabilizability results [willems1976feedback], semidefinite programming formulations [el1995state, boyd1994linear,li2005estimation], robustness properties [Damm2004,bernstein1987robust,hinrichsen1998stochastic,bamieh2018input,gravell2020ifac], and numerical algorithms [benner2011lyapunov]. This line of research is less widely known perhaps because much of it studies continuous time systems, where the heavy machinery required to formalize stochastic differential equations is a barrier to entry for a broad audience. Multiplicative noise models are well-poised to offer data-driven model uncertainty representations and enhanced robustness in learning-based control algorithms and complex dynamical systems and processes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related literature", "weight": 1.0} -->

A related line of research which has seen recent activity is on learning optimal control of Markovian jump linear systems with unknown dynamics and noise distributions [schuurmans2019,jansch2020convergence], which under certain assumptions form a special case of the multiplicative noise system we analyze in this work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related literature", "weight": 1.0} -->

In contrast to classical work on system identification and adaptive control, which has a strong focus on asymptotic results, more recent work has focused on non-asymptotic analysis using newly developed mathematical tools from statistics and machine learning. There remain fundamental open problems for learning in LQR problems, with several addressed only recently, including non-asymptotic sample complexity [dean2017sample,tu2017least], regret bounds [abbasi2011regret,abeille2018improved,mania2019certainty], and algorithmic convergence [Fazel2018]. Alternatives to reinforcement learning include other data-driven model-free optimal control schemes [goncalves2019,baggio2019] and those leveraging the behavioral framework [maupong2017,persis2019]. Subspace identification methods offer a model-based generalization to the output feedback setting [juang1985].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In [sec:model] we establish the multiplicative noise LQR problem and motivate its study via a connection to robust stability. We then give several fundamental results for policy gradient algorithms on linear quadratic problems with multiplicative noise. Our main contributions are as follows, which can be viewed as a generalization of the recent results of Fazel et al.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

- In [sec:graddom] we show that although the multiplicative noise LQR cost is generally non-convex, it has a special property called gradient domination, which facilitates its optimization (Lemmas [lemma:policy\_grad\_exp] and [lemma:gradient\_dominated]). - In particular, in [sec:conv] the gradient domination property is exploited to prove global convergence of three policy gradient algorithm variants (namely, exact gradient descent, natural’’ gradient descent, and Gauss-Newton/policy iteration) to the globally optimum control policy with a rate that depends polynomially on problem parameters (Theorems [thm:gauss\_newton\_exact], [thm:nat\_grad\_exact\_convergence], and [thm:grad\_exact\_convergence]).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our contributions", "weight": 1.0} -->

- Furthermore, in [sec:modelfree] we show that a model-free policy gradient algorithm, where the gradient is estimated from trajectory data (rollouts) rather than computed from model parameters, also converges globally (with high probability) with an appropriate exploration scheme and sufficiently many samples (polynomial in problem data) (Theorem [thm:model-free]).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our contributions", "weight": 1.0} -->

- We quantify the increase in computational burden of policy gradient methods due to the presence of multiplicative noise, which is evident from the bounds developed in Appendices [appendix:model\_based\_gd] and [appendix:model\_free\_gd]. The noise acts to reduce the step size and thus convergence rate, and increases the required number of samples and rollout length in the model-free setting. - A covariance dynamics operator $\mathcal{F}_K$ is established for multiplicative noise systems with a more complicated form than the deterministic case. This necessitated a more careful treatment and novel proof by induction and term matching argument in the proof of Lemma [lemma:S\_K\_trace\_bound]. - Several restrictions on the algorithmic parameters (step size, number of rollouts, rollout length, exploration radius) which are necessary for convergence are established and treated. - An important restriction on the support of the multiplicative noise distribution, which is naturally absent in [Fazel2018], is established in the model-free setting.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our contributions", "weight": 1.0} -->

- A matrix Bernstein concentration inequality is stated explicitly and used to give explicit bounds on the algorithmic parameters in the model-free setting in terms of problem data. - Discussion and numerical results on the use of backtracking line search is included. - When the multiplicative variances $\alpha_i$, $\beta_j$ are all zero, the assertions of Theorems [thm:gauss\_newton\_exact], [thm:nat\_grad\_exact\_convergence], [thm:grad\_exact\_convergence], [thm:model-free] recover the same step sizes and convergence rates of the deterministic setting reported by [Fazel2018].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Thus, policy gradient algorithms for the multiplicative noise LQR problem enjoy the same global convergence properties as deterministic LQR, while significantly enhancing the resulting controller’s robustness to variations and inherent stochasticity in the system dynamics, as demonstrated by our numerical experiments in [sec:numexp].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our contributions", "weight": 1.0} -->

To our best knowledge, the present paper is the first work to consider and obtain global convergence results using reinforcement learning algorithms for the multiplicative noise LQR problem. Our approach allows the explicit incorporation of a model uncertainty representation that significantly improves the robustness of the controller compared to deterministic and additive noise approaches.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

the initial state $x_0$ is distributed according to $\mathcal{P}_0$ with covariance $\Sigma_0 \coloneqq {\mathbb{E}}_{x_0} [x_0 x_0^\intercal]$, $\Sigma_0 \succ 0$, and $Q \succ 0$ and $R \succ 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

The dynamics are described by a dynamics matrix $A \in \mathbb{R}^{n \times n}$ and input matrix $B \in \mathds{}{R}^{n \times m}$ and incorporate multiplicative noise terms modeled by the i.i.d. (across time), zero-mean, mutually independent scalar random variables $\delta_{ti}$ and $\gamma_{tj}$, which have variances $\alpha_i$ and $\beta_j$, respectively. The matrices $A_i \in \mathbb{R}^{n \times n}$ and $B_i \in \mathbb{R}^{n \times m}$ specify how each scalar noise term affects the system dynamics and input matrices. Alternatively, suppose $\bar A$ and $\bar B$ are zero-mean random matrices with a joint covariance structure We assume $\bar A$ and $\bar B$ are independent for simplicity, but it is straightforward to include correlations between the entries of $\bar A$ and $\bar B$ into the model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

over their entries governed by the covariance matrices $\Sigma_A \coloneqq \mathbb{E} [\mathbf{vec}(\bar A)\mathbf{vec}(\bar A)^\intercal] \in \mathbb{R}^{n^2 \times n^2}$ and $\Sigma_B \coloneqq \mathbb{E} [\mathbf{vec}(\bar B)\mathbf{vec}(\bar B)^\intercal] \in \mathbb{R}^{nm \times nm}$. Then it suffices to take the variances $\alpha_i$ and $\beta_{j}$ and matrices $A_i$ and $B_j$ as the eigenvalues and (reshaped) eigenvectors of $\Sigma_A$ and $\Sigma_B$, respectively, after a projection onto a set of orthogonal real-valued vectors [gravell2020acc].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

The goal is to determine a closed-loop state feedback policy $\pi^*$ with $u_t = \pi^*(x_t)$ from a set $\Pi$ of admissible policies which solves the optimization in [eq:LQRm].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

We assume that the problem data $A$, $B$, $\alpha_i$, $A_i$, $\beta_j$, and $B_j$ permit existence and finiteness of the optimal value of the problem, in which case the system is called mean-square stabilizable and requires mean-square stability of the closed-loop system [kozin1969survey,willems1976feedback]. The system in [eq:LQRm] is called mean-square stable if $\lim_{t \to \infty}\mathbb{E}_{x_0, \delta, \gamma}[x_t x_t^\intercal] = 0$ for any given initial covariance $\Sigma_0$, where for brevity we notate expectation with respect to the noises $\mathbb{E}_{\{\delta_{ti}\},\{\gamma_{tj}\}}$ as $\mathbb{E}_{\delta, \gamma}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

Mean-square stability is a form of robust stability, implying stability of the mean (i.e. $\lim_{t \to \infty}\mathbb{E} x_t = 0 \ \forall \ x_0$) as well as almost-sure stability (i.e. $\lim_{t \to \infty} x_t = 0$ almost surely) [willems1976feedback]. Mean-square stability requires stricter and more complicated conditions than stabilizability of the nominal system $(A,B)$ [willems1976feedback], which are discussed in the sequel. This essentially can limit the size of the multiplicative noise covariance [athans1977uncertainty], which can be viewed as a representation of uncertainty in the nominal system model or as inherent variation in the system dynamics.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

Dynamic programming can be used to show that the optimal policy $\pi^*$ is linear state feedback $u_t = \pi^*(x_t) = K^* x_t$, where $K^* \in \mathbb{R}^{m \times n}$ denotes the optimal gain matrix.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

When the control policy is linear state feedback ${u_t = \pi(x_t) = K x_t}$, with a very slight abuse of notation the cost becomes C(K) = \mathbb{E}_{x_0,\{\delta_{ti}\}, \{\gamma_{tj}\}} \sum_{t=0}^\infty x_t^\intercal (Q + K^\intercal R K) x_t Dynamic programming further shows that the resulting optimal cost is quadratic in the initial state, i.e. ${C(K^*) = \mathbb{E}_{x_0} x_0^\intercal P x_0 = \Tr(P \Sigma_0)}$, where $P \in \mathbb{R}^{n \times n}$ is a symmetric positive definite matrix [bertsekas1995dynamic]. Note that the optimal controller does not need to directly observe the noise variables $\delta_{ti}$, $\gamma_{tj}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

When the model parameters are known, there are several ways to compute the optimal feedback gains and corresponding optimal cost. The optimal cost is given by the solution of the generalized algebraic Riccati equation (GARE) P & = Q + A^\intercal P A + \sum_{i=1}^p \alpha_i A_i^\intercal P A_i - A^\intercal P B (R + B^\intercal P B + \sum_{j=1}^q \beta_j B_j^\intercal P B_j)^{-1} B^\intercal P A.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

This is a special case of the GARE for optimal static output feedback given in [bernstein1987robust] and can be solved via the value iteration P_{k+1} & = Q + A^\intercal P_k A + \sum_{i=1}^p \alpha_i A_i^\intercal P_k A_i % - A^\intercal P_k B (R + B^\intercal P_k B + \sum_{j=1}^q \beta_j B_j^\intercal P_k B_j)^{-1} B^\intercal P_k A, with $P_0 = Q$, or via semidefinite programming formulations [boyd1994linear,el1995state,li2005estimation], or via more exotic iterations based on the Smith method and Krylov subspaces [freiling2003,ivanov2007].

<!-- chunk {"id": "body-0028", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

The associated optimal gain matrix is K^* = - \bigg(R + B^\intercal P B + \sum_{j=1}^q \beta_j B_j^\intercal P B_j \bigg)^{-1} B^\intercal P A.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

It was verified in [willems1976feedback] that existence of a positive definite solution to the GARE [eq:genriccati] is equivalent to mean-square stabilizability of the system, which depends on the problem data $A$, $B$, $\alpha_i$, $A_i$, $\beta_j$, and $B_j$; in particular, mean-square stability generally imposes upper bounds on the variances $\alpha_i$ and $\beta_j$ [athans1977uncertainty], but may be infinite depending on the structure of $A$, $B$, $A_i$, and $B_j$ [willems1976feedback]. At a minimum, uniqueness and existence of a solution to the GARE [eq:genriccati] requires the standard conditions for uniqueness and existence of a solution to the standard ARE, namely of $(A,B)$ stabilizable and $(A, Q^{1/2})$detectable.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

Although (approximate) value iteration can be implemented using sample trajectory data, policy gradient methods have been shown to be more effective for approximately optimal control of high-dimensional stochastic nonlinear systems e.g. those arising in robotics [peters2006]. This motivates our following analysis of the simpler case of stochastic linear systems wherein we show that policy gradient indeed facilitates a data-driven approach for learning optimal and robust policies.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Consider a fixed linear state feedback policy ${u_t = Kx_t}$. Defining the stochastic system matrices \widetilde{A} &= A + \sum_{i=1}^p \delta_{ti} A_i, \\\widetilde{B} &= B + \sum_{j=1}^q \gamma_{tj} B_j, the deterministic nominal and stochastic closed-loop system matrices \widetilde{A}_K = \widetilde{A} + \widetilde{B} K, and the closed-loop state-cost matrix the closed-loop dynamics become x_{t+1} = \widetilde{A}_K x_t = \bigg((A + \sum_{i=1}^p \delta_{ti} A_i) + (B + \sum_{j=1}^q \gamma_{tj} B_j)K\bigg) x_t.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

A gain $K$ is mean-square stabilizing if the closed-loop system is mean-square stable. Denote the set of mean-square stabilizing $K$ as $\mathcal{K}$. If $K \in \mathcal{K}$, then the cost can be written as C(K) = \mathbb{E}_{x_0} x_0^\intercal P_K x_0 = \Tr(P_K \Sigma_0), where $P_K$ is the unique positive semidefinite solution to the generalized Lyapunov equation

<!-- chunk {"id": "body-0033", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

We define the state covariance matrices and the infinite-horizon aggregate state covariance matrix as \Sigma_{t} \coloneqq {\mathbb{E}}_{x_0,\delta, \gamma } [x_t x_t^\intercal], \qquad \Sigma_{K} \coloneqq \sum_{t=0}^\infty \Sigma_t.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Vectorization and Kronecker products can be used to convert [eq:glyap1] and [eq:glyap2] into systems of linear equations. Alternatively, iterative methods have been suggested for their solution [freiling2003, ivanov2007].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

The state covariance dynamics are captured by two closed-loop finite-dimensional linear operators which operate on a symmetric matrix $X$: \mathcal{T}_K(X) & \coloneqq \underset{\delta, \gamma}{\mathbb{E}} \sum_{t=0}^\infty \widetilde{A}_K^t X \widetilde{A}_K^{\intercal^t}, \\\mathcal{F}_K(X) & \coloneqq \underset{\delta, \gamma}{\mathbb{E}} \widetilde{A}_K X \widetilde{A}_K^\intercal = A_K X A_K^\intercal + \sum_{i=1}^p \alpha_i A_i X A_i^\intercal + \sum_{j=1}^q \beta_j B_j K X (B_j K)^\intercal.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Thus $\mathcal{F}_K$ (without an argument) is a linear operator whose matrix representation is \mathcal{F}_K & \coloneqq A_K \otimes A_K + \! \sum_{i=1}^p \alpha_i A_i \otimes A_i + \! \sum_{j=1}^q \beta_j (B_j K) \otimes (B_j K).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

We then have the following lemma: A gain $K$ is mean-square stabilizing if and only if the spectral radius $\rho(\mathcal{F}_{K}) < 1$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Mean-square stability implies ${\underset{t \to \infty}{\lim} \mathbb{E} [x_t x_t^\intercal] = 0}$, which for linear systems occurs only when $\Sigma_K$ is finite, which by [eq:TK\_char] is equivalent to $\rho(\mathcal{F}_{K})<1$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Recalling the definition of $C(K)$ and [eq:glyap2], along with the basic observation that $K \notin \mathcal{K}$ induces infinite cost, gives the following characterization of the cost: \Tr(Q_K \Sigma_K) = \Tr(P_K \Sigma_0) \quad &\text{if } K \in \mathcal{K} \\\infty \quad &\text{otherwise.} The evident fact that $C(K)$ is expressed as a closed-form function, up to a Lyapunov equation, of $K$ leads to the idea of performing gradient descent on $C(K)$ (i.e., policy gradient) via the update $K \leftarrow K - \eta \nabla C(K)$ to find the optimal gain matrix. However, two properties of the LQR cost function $C(K)$ complicate a convergence analysis of gradient descent.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

First, $C(K)$ is extended valued since not all gain matrices provide closed-loop mean-square stability, so it does not have (global) Lipschitz gradients. Second, and even more concerning, $C(K)$ is generally non-convex in $K$ (even for deterministic LQR problems, as observed by Fazel et al. [Fazel2018]), so it is unclear if and when gradient descent converges to the global optimum, or if it even converges at all. Fortunately, as in the deterministic case, we show that the multiplicative LQR cost possesses further key properties that enable proof of global convergence despite the lack of Lipschitz gradients and non-convexity.

<!-- chunk {"id": "body-0041", "role": "body", "section": "From Stochastic to Robust Stability", "weight": 1.0} -->

Additional motivation for designing controllers which stabilize a stochastic system in mean-square is to ensure robustness of stability of a nominal deterministic system to model parameter perturbations. Here we state a condition which guarantees robust deterministic stability for a perturbed deterministic system given mean-square stability of a stochastic single-state system with multiplicative noise where the noise variance and parameter perturbation size are related.

<!-- chunk {"id": "body-0042", "role": "body", "section": "From Stochastic to Robust Stability", "weight": 1.0} -->

Suppose the stochastic closed-loop system where $a, x_t, \delta_t $ are scalars with $\mathbb{E} [\delta_{t}^2] = \alpha $ is mean-square stable. Then, the perturbed deterministic system is stable for any constant perturbation $|\phi| \leq \sqrt{a^2 + \alpha} - | a |$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "From Stochastic to Robust Stability", "weight": 1.0} -->

By the bound on $\phi$ and triangle inequality we have \rho(a + \phi) = |a + \phi | \leq |a| + | \phi | \leq \sqrt{a^2 + \alpha}. From Lemma [lemma:mss\_char], mean-square stability of [eq:scalar\_stochastic\_sys] implies \sqrt{\rho(\mathcal{F})} = \sqrt{a^2 + \alpha} < 1 and thus $\rho(a + \phi) < 1$, proving stability of [eq:perturbed\_det\_sys].

<!-- chunk {"id": "body-0044", "role": "body", "section": "From Stochastic to Robust Stability", "weight": 1.0} -->

Although this is a simple example, it demonstrates that the robustness margin increases monotonically with the multiplicative noise variance. We also see that when $\alpha = 0$ the bound collapses so that no robustness is guaranteed, i.e., when $|a| \rightarrow 1$. This result can be extended to multiple states, inputs, and noise directions, but the resulting conditions become considerably more complex [bernstein1987robust, gravell2020ifac]. We now proceed with developing methods for optimal control.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Gradient Domination and Other Properties oftheMultiplicativeNoiseLQRCost", "weight": 1.0} -->

In this section, we demonstrate that the multiplicative noise LQR cost function is gradient dominated, which facilitates optimization by gradient descent. Gradient dominated functions have been studied for many years in the optimization literature [Polyak1963] and have recently been discovered in deterministic LQR problems by [Fazel2018].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

First, we give the expression for the policy gradient of the multiplicative noise LQR cost.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

We include a factor of 2 on the gradient expression that was erroneously dropped. This affects the step size restrictions by a corresponding factor of 2.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

For brevity the gradient is implied to be with respect to the gains $K$ in the rest of this work, i.e., $\nabla_K$ denoted by $\nabla$. Now we must develop some auxiliary results before demonstrating gradient domination. Throughout $\| Z \|$ and $\|Z\|_F$ are the spectral and Frobenius norms respectively of a matrix $Z$, and $\underline{\sigma}(Z)$ and $\overline{\sigma}(Z)$ are the minimum and maximum singular values of a matrix $Z$. The value function of $V_K(x)$ for $x=x_0$ is defined as V_K(x) \coloneqq \mathbb{E}_{\delta,\gamma} \sum_{t=0}^\infty x_t^\intercal Q_K x_t. which relates to the cost as $C(K) = \mathbb{E}_{x_0} V_K(x_0)$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

The advantage function is defined as \mathcal{A}_K(x,u) & \coloneqq x^\intercal Q x + u^\intercal R u + \underset{\delta,\gamma}{\mathbb{E}} V_K(\widetilde{A}x+\widetilde{B}u) - V_K(x), where the expectation is with respect to $\widetilde{A}$ and $\widetilde{B}$ inside the parentheses of $V_{K}(\widetilde{A} x+\widetilde{B} u)$. The advantage function can be thought of as the difference in cost (advantage) when starting in state $x$ of taking an action $u$ for one step instead of the action generated by policy $K$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

We also define the state, input, and cost sequences \{x_t\}_{K,x} & \coloneqq \{x, \widetilde{A}_K x,\widetilde{A}_K^2 x,..., \widetilde{A}_K^t x,... \} \\Throughout the proofs we will consider pairs of gains $K$ and $K{^\prime}$ and their difference $\Delta \coloneqq K{^\prime} - K$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

The proof follows the cost-difference lemma in [Fazel2018] exactly substituting versions of value and cost functions, etc. which take expectation over the multiplicative noise.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

For the second part of the proof regarding the advantage expression, we expand and substitute in definitions: \mathcal{A}_{K}(x,K{^\prime} x) &= \mathcal{Q}_{K}(x,K{^\prime}x) - V_{K}(x) \\&= x^\intercal Q x + x^\intercal K{^\prime}^\intercal R K{^\prime} x +\underset{\delta,\gamma}{\mathbb{E}} V_{K}(A_{K{^\prime}} x) - V_{K}(x).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

We also have the following expression from the recursive relationship for $P_{K}$ V_{K}(x) &= x^\intercal P_{K} x = x^\intercal \bigg[Q + K^\intercal RK + (A+BK)^\intercal P_{K} (A+BK) + \sum_{i=1}^p \alpha_i A_i^\intercal P_{K} A_i + \sum_{j=1}^q \beta_j K^\intercal B_j^\intercal P_{K} B_j K \bigg] x.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

Next, we see that the multiplicative noise LQR cost is gradient dominated.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

The LQR-with-multiplicative-noise cost $C(K)$ satisfies the gradient domination condition C(K) - C(K^*) &\leq \frac{\|\Sigma_{K^*}\|}{4\underline{\sigma}(R) {\underline{\sigma} (\Sigma_0)}^2 } \|\nabla C(K)\|_F^2.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

We start with the advantage expression \mathcal{A}_{K}(x,K{^\prime} x) &= 2x^\intercal \Delta^\intercal E_{K} x + x^\intercal \Delta^\intercal R_{K} \Delta x \\&= 2 \Tr[xx^\intercal\Delta^\intercal E_{K}] +\Tr [xx^\intercal \Delta^\intercal R_{K} \Delta].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

Let the state and control sequences associated with the optimal gain $K^*$ be $\{x_t\}_{K^*,x}$ and $\{u_t\}_{K^*,x}$ respectively. We now obtain an upper bound for the cost difference by writing the cost difference in terms of the value function as C(K) - C(K^*) = \underset{x_0}{\mathbb{E}} \big[V(K,x_0) \big] - \underset{x_0}{\mathbb{E}} \big[V(K^*,x_0) \big] = \underset{x_0}{\mathbb{E}} \big[V(K,x_0)-V(K^*,x_0) \big].

<!-- chunk {"id": "body-0058", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

The gradient domination property gives the following stationary point characterization.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

In other words, so long as $\Sigma_K$ is full rank, stationarity is both necessary and sufficient for global optimality, as for convex functions. Note that it is not sufficient to just have multiplicative noise in the dynamics with a deterministic initial state $x_0$ to ensure that $\Sigma_K$ is full rank. To see this, observe that if $x_0=0$ and $\Sigma_0 = 0$ then $\Sigma_K=0$, which is clearly rank deficient. By contrast, additive noise is sufficient to ensure that $\Sigma_K$ is full rank with a deterministic initial state $x_0$, although we will not consider this setting. Using a random initial state with $\Sigma_0 \succ 0$ ensures rank$(\Sigma_K)=n$ and thus $\nabla C(K)=0$ implies $K=K^*$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

Although the gradient of the multiplicative noise LQR cost is not globally Lipschitz continuous, it is locally Lipschitz continuous over any subset of its domain (i.e., over any set of mean-square stabilizing gain matrices). The gradient domination is then sufficient to show that policy gradient descent will converge to the optimal gains at a linear rate (a short proof of this fact for globally Lipschitz functions is given in [Karimi2016]). We prove this convergence of policy gradient to the optimum feedback gain by bounding the local Lipschitz constant in terms of the problem data, which bounds the maximum step size and the convergence rate.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

Following [Fazel2018] we refer to Lipschitz continuity of the gradient as ($\mathcal{C}^1$-)smoothness, and so this section deals with showing that the LQR cost satisfies an expression that is almost of the exact form of a Lipschitz continuous gradient.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

The LQR-with-multiplicative-noise cost $C(K)$ satisfies the almost-smoothness expression C(K{^\prime}) - C(K) &= 2\Tr\big[\Sigma_{K{^\prime}} \Delta^\intercal E_{K} \big] + \Tr\big[\Sigma_{K{^\prime}} \Delta^\intercal R_{K}\Delta \big].

<!-- chunk {"id": "body-0063", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

As in the gradient domination proof, we express the cost difference in terms of the advantage by taking expectation over the initial states to obtain C(K{^\prime}) - C(K) &= \underset{x_0}{\mathbb{E}} \bigg[\sum_{t=0}^\infty \mathcal{A}_{K}\big(\{x_t\}_{K{^\prime},x} \, \ \{u_t\}_{K{^\prime},x}\big)\bigg].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

From the value difference lemma for the advantage we have \mathcal{A}_{K}(x,K{^\prime} x) &= 2x^\intercal\Delta^\intercal E_{K} x + x^\intercal \Delta^\intercal R_{K} \Delta x.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

Using the definition of $\Sigma_{K^\prime}$ completes the proof.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

For small deviations $K^\prime - K$ the equation in the almost-smoothness lemma exactly describes a Lipschitz continuous gradient. The naming should not be taken to imply that the LQRm cost is not smooth, but rather that the equation as stated does not immediately yield a Lipschitz constant; indeed the Lipschitz constant is what much of the later proofs go towards bounding (implicitly) i.e. by bounding higher-order terms which must be accounted for when $K^\prime \neq K$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

To be specific, a Lipschitz continuous gradient to $C(K)$ implies there exists a Lipschitz constant $L$ such that C(K^\prime) - C(K) \leq \Tr(\nabla C(K)^\intercal \Delta) + \frac{L}{2} \Tr (\Delta^\intercal \Delta) for all $K^\prime$, $K$. This is the quadratic upper bound which is used e.g. in Thm. 1 of [Karimi2016] to prove convergence of gradient descent on a gradient dominated objective function. The almost-smoothness condition is that C(K{^\prime}) - C(K) &= 2\Tr\big[\Sigma_{K{^\prime}} \Delta^\intercal E_{K} \big] + \Tr\big[\Sigma_{K{^\prime}} \Delta^\intercal R_{K}\Delta \big].

<!-- chunk {"id": "body-0068", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

The proof follows that in [Fazel2018] exactly. The cost is lower bounded as C(K) &= \Tr\left[P_K \Sigma_0 \right] \geq \|P_K\| \Tr(\Sigma_0) \geq \|P_K\| \underline{\sigma}(\Sigma_0), which gives the first inequality. The cost is also lower bounded as C(K) &= \Tr\left[Q_K \Sigma_K \right] \geq \|\Sigma_K\| \Tr(Q_K) \geq \|\Sigma_K\| \underline{\sigma}(Q_K) \geq \|\Sigma_K\| \underline{\sigma}(Q), which gives the second inequality.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-BasedSetting", "weight": 1.0} -->

In this section we show that the policy gradient algorithm and two important variants for multiplicative noise LQR converge globally to the optimal policy. In contrast with [Fazel2018], the policies we obtain are robust to uncertainties and inherent stochastic variations in the system dynamics.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-BasedSetting", "weight": 1.0} -->

- 25mm $K_{s+1} = K_s - \eta \nabla C(K_s) \Sigma_{K_s}^{-1}$ - 25mm $K_{s+1} = K_s - \eta R_{K_s}^{-1} \nabla C(K_s) \Sigma_{K_s}^{-1}$ The more elaborate natural gradient and Gauss-Newton variants provide superior convergence rates and simpler proofs. A development of the natural policy gradient is given in [Fazel2018] building on ideas from [Kakade2002]. The Gauss-Newton step with step size $\frac{1}{2}$ is in fact identical to the policy improvement step in policy iteration (a short derivation is given shortly) and was first studied for deterministic LQR in [Hewer1971]. This was extended to a model-free setting using policy iteration and Q-learning in [Bradtke1994], proving asymptotic convergence of the gain matrix to the optimal gain matrix.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-BasedSetting", "weight": 1.0} -->

For multiplicative noise LQR, we have the following results.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

We start with the policy improvement expression for the LQR problem: u_{s+1} &= \underset{u}{\text{argmin}}\bigg[x^\intercal Q x + u^\intercal R u + \underset{\delta,\gamma}{\mathbb{E}} V_{K_s}(\widetilde{A}x+\widetilde{B}u) \bigg] = \underset{u}{\text{argmin}}\bigg[\mathcal{Q}_{K_s}(x,u) \bigg].

<!-- chunk {"id": "body-0073", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Stationary points occur when the gradient is zero, so differentiating with respect to $u$ we obtain \frac{\partial}{\partial u} \mathcal{Q}_{K_s}(x,u) = 2\bigg[(B^\intercal P_{K_s} A)x + (R+B^\intercal P_{K_s} B + \sum_{j=1}^q \beta_j B_j^\intercal P_{K_s} B_j)u \bigg].

<!-- chunk {"id": "body-0074", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Differentiating [eq:grad\_u] with respect to $u$ we obtain \frac{\partial^2}{{\partial u}^2} \mathcal{Q}_{K_s}(x,u) = 2\bigg[R+B^\intercal P_{K_s} B + \sum_{j=1}^q \beta_j B_j^\intercal P_{K_s} B_j \bigg] \succeq 0 \ \forall \ u, confirming that the stationary point is indeed a global minimum.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Parameterizing with a step size gives the Gauss-Newton step K_{s+1} &= K_s - \eta R_{K_s}^{-1}\nabla C(K_s) \Sigma_{K_s}^{-1}.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Gauss-Newton Descent", "weight": 1.0} -->

Adding $C(K_s) - C(K^*)$ to both sides and rearranging completes the proof.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Natural Policy Gradient Descent", "weight": 1.0} -->

First we bound the one-step progress, where the step size depends explicitly on the current gain $K_s$. Using the update [eq:nat\_grad\_update], the next-step gain matrix difference is \Delta = K_{s+1} - K_s &= -\eta \nabla C(K_s) \Sigma_{K_s}^{-1} = -2\eta E_{K_s}.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Natural Policy Gradient Descent", "weight": 1.0} -->

Adding $C(K_s) - C(K^*)$ to both sides and rearranging gives the one step progress bound \frac{ C(K_{s+1}) - C(K^*)}{C(K_{s}) - C(K^*)} \leq 1 - 2 \eta \frac{\underline{\sigma}(R) {\underline{\sigma} (\Sigma_0)}}{\|\Sigma_{K^*}\|}.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Policy Gradient Descent", "weight": 1.0} -->

[Policy gradient convergence] Using the policy gradient step with step size $0 < \eta \leq c_{pg}$ gives global convergence to the optimal gain matrix $K^*$ at a linear rate described by 1 - 2 \eta \frac{ \underline{\sigma}(R){\underline{\sigma} (\Sigma_0)}^2}{\|\Sigma_{K^*}\|} where $c_{\text{pg}}$ is a polynomial in the problem data $A$, $B$, $\alpha_i$, $\beta_j$, $A_i$, $B_j$, $Q$, $R$, $\Sigma_0$, $K_0$ given in the proof in Appendix [appendix:model\_based\_gd].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Policy Gradient Descent", "weight": 1.0} -->

The proof is developed in Appendix [appendix:model\_based\_gd].

<!-- chunk {"id": "body-0081", "role": "body", "section": "Policy Gradient Descent", "weight": 1.0} -->

The proofs for these results explicitly incorporate the effects of the multiplicative noise terms $\delta_{ti}$ and $\gamma_{tj}$ in the dynamics. For the policy gradient and natural policy gradient algorithms, we show explicitly how the maximum allowable step size depends on problem data and in particular on the multiplicative noise terms. Compared to deterministic LQR, the multiplicative noise terms decrease the allowable step size and thereby decrease the convergence rate; specifically, the state-multiplicative noise increases the initial cost $C(K_0)$ and the norms of the covariance $\Sigma_{K^*}$ and cost $P_K$, and the input-multiplicative noise also increases the denominator term $\|B\|^2+\sum_{j=1}^q \beta_j \|B_j\|^2$. This means that the algorithm parameters for deterministic LQR in [Fazel2018] may cause failure to converge on problems with multiplicative noise.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Policy Gradient Descent", "weight": 1.0} -->

Moreover, even the optimal policies for deterministic LQR may actually destabilize systems in the presence of small amounts of multiplicative noise uncertainty, indicating the possibility for a catastrophic lack of robustness; observe the results of the example in Section [sec:numexp\_A]. The results and proofs also differ from that of [Fazel2018] because the more complicated mean-square stability must be accounted, and because generalizedLyapunov equations must be solved to compute the gradient steps, which requires specialized solvers.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

The results in the previous section are model-based; the policy gradient steps are computed exactly based on knowledge of the model parameters. In the model-free setting, the policy gradient is estimated to arbitrary accuracy from sample trajectories with a sufficient number of sample trajectories $n_{\text{sample}}$ of sufficiently long horizon length $\ell$ using gain matrices randomly selected from a Frobenius-norm ball around the current gain of sufficiently small exploration radius $r$. We show for multiplicative noise LQR that with a finite number of samples polynomial in the problem data, the model-free policy gradient algorithm still converges to the globally optimal policy, despite small perturbations on the gradient.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

In the model-free setting, the policy gradient method proceeds as before except that at each iteration Algorithm [algorithm:algo1] is called to generate an estimate of the gradient via the zeroth-order optimization procedure described by Fazel et al. [Fazel2018].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

Model-Free policy gradient estimation Gain matrix $K$, number of samples $n_{\text{sample}}$, rollout length $\ell$, exploration radius $r$ $i=1,\ldots,n_{\text{sample}}$ Generate a sample gain matrix $\widehat{K}_{i}=K+U_{i},$ where $U_{i}$ is drawn uniformly at random over matrices with Frobenius norm $r$ Generate a sample initial state $x_0^{(i)} \sim \mathcal{P}_0$ Simulate the closed-loop system for $\ell$ steps according to the stochastic dynamics in [eq:LQRm] starting from $x_0^{(i)}$ with $u_t^{(i)} = \widehat{K}_{i} x_t^{(i)}$, yielding the state sequence $\{ x_t^{(i)} \}_{t=0}^{t=\ell}$ Collect the empirical finite-horizon cost estimate

<!-- chunk {"id": "body-0086", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

Suppose that the distribution of the initial states is bounded such that $x_0 \sim \mathcal{P}_0$ implies $\|x_0^i\| \leq L_0$ almost surely for any given realization $x_0^i$ of $x_0$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

Suppose additionally that the distribution of the multiplicative noises is bounded such that the following inequality is satisfied almost surely for any given realized sequence $x_t^i$ of $x_t$ with a positive scalar $z \geq 1$: \sum_{t=0}^{\ell-1} \Big({x_{t}^{i}}^\intercal Q x_{t}^{i}+{u_{t}^{i}}^\intercal R u_{t}^{i} \Big) \leq z \underset{\delta, \gamma}{\mathbb{E}} \left[\sum_{t=0}^{\ell-1} \Big(x_t^\intercal Q x_t + u_t^\intercal R u_t \Big) \right] under the closed-loop dynamics with any gain such that $C(K) \leq 2 C(K_0)$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

Suppose the step size $\eta$ is chosen according to the restriction in Theorem [thm:grad\_exact\_convergence] and at every iteration the gradient is estimated according to the finite-horizon procedure in Algorithm [algorithm:algo1] where the number of samples $n_{\text{sample}}$, rollout length $\ell$, and exploration radius $r$ are chosen according to the fixed polynomials of the problem data $A$, $B$, $\alpha_i$, $\beta_j$, $A_i$, $B_j$, $Q$, $R$, $\Sigma_0$, $K_0$, $L_0$ and $z$ which are all defined in the proofs in Appendix [appendix:model\_free\_gd].

<!-- chunk {"id": "body-0089", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

Then, with high probability of at least $1 - \mu$, performing gradient descent results in convergence to the global optimum over all $N$ steps: at each step, either progress is made at the linear rate \frac{C(K_{s+1})-C(K^*)}{C(K_s)-C\left(K^{*}\right)} \leq 1 - \eta \frac{\underline{\sigma}(R)\underline{\sigma}(\Sigma_0)^{2}}{\left\|\Sigma_{K^{*}}\right\|}. or convergence has been attained with $C(K_s) - C(K^*) \leq \epsilon$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

The proof is developed in Appendix [appendix:model\_free\_gd].

<!-- chunk {"id": "body-0091", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

From a sample complexity standpoint, it is notable that the number of samples $n_{\text{sample}}$, rollout length $\ell$, and exploration radius $r$ in Theorem [thm:model-free] are polynomial in the problem data $A$, $B$, $\alpha_i$, $\beta_j$, $A_i$, $B_j$, $Q$, $R$, $\Sigma_0$, $C(K_0)$. The constant $z$ imposes a bound on the multiplicative noise, which is naturally absent in [Fazel2018]. Note that $z \geq 1$ since any upper bound of a scalar distribution with finite support must be equal to or greater than the mean. In general, this implicitly requires the noises to have bounded support. Such an assumption is qualitatively the same as the condition imposed on the initial states. These assumptions are reasonable; in a practical setting with a physical system the initial state and noise distributions will have finite support. There is no restriction on how large the support is, only that it not be unbounded.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Global Convergence of Policy Gradient in theModel-FreeSetting", "weight": 1.0} -->

Also note that the rate is halved compared with the model-based case of Theorem [thm:grad\_exact\_convergence]; this is because the other halfis consumed by the error between the estimated and true gradient.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

- Shows that optimal control that ignores actual multiplicative noise can lead to loss of mean-square stability, - Shows the efficacy of the policy gradient algorithms on a networked system, - Shows the increased difficulty of estimating the gradient from sample data in the presence of multiplicative noise.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All systems considered permitted a solution to the GARE [eq:genriccati]. The bounds on the step size, number of rollouts, and rollout length given by the theoretical analysis can be rather conservative. For practicality, we selected the constant step size, number of rollouts, rollout length, and exploration radius according to a grid search over reasonable values. Additionally, we investigated the use of backtracking line search to adaptively select the step size; see e.g. [boyd2004convex]. Throughout the simulations, we computed the baseline optimal cost $C(K^*)$ by solving the GARE [eq:genriccati] to high precision via value iteration. Python code which implements the algorithms and generates the figures reported in this work can be found in the GitHub repository at The code was run on a desktop PC with a quad-core Intel i7 6700K 4.0GHz CPU, 16GB RAM; no GPU computing was utilized.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Importance of Accounting for Multiplicative Noise", "weight": 1.0} -->

We first considered an open-loop mean-square unstable system with four states and one input representing an active two-mass suspension converted from continuous to discrete time using a standard bilinear transformation, with parameters: \end{bmatrix}, \quad \end{bmatrix}, \quad B_1 = \mathbf{1}_{4 \times 1}, \quad We performed model-based policy gradient descent; at each iteration gradients were calculated by solving generalized Lyapunov equations [eq:glyap1] and [eq:glyap2] using the problem data. The gains $K_m$ and $K_\ell$ represent iterates during optimization of (training on) the LQRm and LQR cost (with the multiplicative noise variances set to zero), respectively. We performed the optimization starting from the same feasible initial gain, which was generated by perturbing the exact solution of the generalized algebraic Riccati equation such that the LQRm cost under the initial control was approximately 10 times that of the optimal control. The step size was chosen via backtracking line search.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Importance of Accounting for Multiplicative Noise", "weight": 1.0} -->

The optimization stopped once the Frobenius norm of the gradient fell below a small threshold. The plot in Fig. [fig:plot\_cost\_vs\_iteration\_suspension\_both] shows the testing cost of the gains at each iteration evaluated on the LQRm cost (with multiplicative noise). From this figure, it is clear that $K_m$ minimized the LQRm as desired. When there was high multiplicative noise, the noise-ignorant controller $K_\ell$ actually destabilized the system in the mean-square sense; this can be seen as the LQRm cost exploded upwards to infinity after iteration 10. In this sense, the multiplicative noise-aware optimization is generally safer and more robust than noise-ignorant optimization, and in examples like this is actually necessaryfor mean-square stabilization.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Importance of Accounting for Multiplicative Noise", "weight": 1.0} -->

Relative cost error $\frac{C(K)-C(K^*)}{C(K^*)}$ vs. iteration during policy gradient descent on the 4-state, 1-input suspension example system.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

Many practical networked systems can be approximated by diffusion dynamics with losses and stochastic diffusion constants (edge weights) between nodes; examples include heat flow through uninsulated pipes, hydraulic flow through leaky pipes, information flow between processors with packet loss, electrical power flow between generators with resistant electrical power lines, etc. A derivation of the discrete-time dynamics of this system is given in [gravell2020acc]. We considered a particular 4-state, 4-input system and open-loop mean-square stable with the following parameters: \end{bmatrix}, \quad \end{cases} \quad This system is open-loop mean-square stable, so we initialized the gains to all zeros for each trial.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

We performed policy optimization using the model-free gradient, and the model-based gradient, model-based natural gradient, and model-based Gauss-Newton step directions on 20 unique problem instances using two step size schemes: Backtracking line search: Step sizes $\eta$ were chosen adaptively at each iteration by backtracking line search with parameters $\alpha = 0.01$, $\beta = 0.5$ (see [boyd2004convex] for a description), except for Gauss-Newton which used the optimal constant step-size of $1/2$. Model-free gradients and costs were estimated with 100,000 rollouts per iteration. We ran a fixed number, 20, of iterations chosen such that the final cost using model-free gradient descent was no more than $5\%$ worse than optimal.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

Constant step size: Step sizes were set to constants chosen as large as possible without observing infeasibility or divergence, which on this problem instance was $\eta = 5 \times 10^{-5}$ for gradient, $\eta = 2 \times 10^{-4}$ for natural gradient, and $\eta = 1/2$for Gauss-Newton step directions. Model-free gradients were estimated with 1,000 rollouts per iteration. We ran a fixed number, 20,000, of iterations chosen such that convergence was achieved with all step directions.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

In both cases sample gains were chosen for model-free gradient estimation with exploration radius $r \! = \! 0.1$ and the rollout length was set to $\ell \! = \! 20$. The plots in Fig. [fig:plot\_costnorm\_vs\_iteration\_random] show the relative cost over the iterations; for the model-free gradient descent, the bold centerline is the mean of all trials and the shaded region is between the 10th and 90th percentile of all trials. Using backtracking line search, it is evident that in terms of convergence the Gauss-Newton step was extremely fast, and both the natural gradient and model-based gradient were slightly slower, but still quite fast. The model-free policy gradient converged to a reasonable neighborhood of the minimum cost quickly, but stagnated with further iterations; this is a consequence of the inherent gradient and cost estimation errors that arise due to random sampling and the multiplicative noise. Using constant stepsizes, we were forced to take small steps due to the steepness of the cost function near the initial gains, slowing overall convergence using the gradient and natural gradient methods.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

Here we observed that Gauss-Newton again converged most quickly, followed by natural gradient and lastly the gradient methods. The smaller step size also allowed us to use far fewer samples in the model-free setting, where we observed somewhat faster initial cost decrease with eventual stagnation around $10^{-2}$, or 1%, relative error, which represents excellent control performance. All algorithms exhibited convergence to the optimum, confirming the asserted theoretical claims.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

Relative cost error $\frac{C(K)-C(K^*)}{C(K^*)}$ vs. iteration during policy gradient methods on a 4-state, 4-input lossy diffusion network with multiplicative noise using a) backtracking line search and b) constant step sizes.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Gradient Estimation", "weight": 1.0} -->

Multiplicative noise can significantly increase the variance and sample complexity of cost gradient estimates relative to the noiseless case, which is novelly reflected in the theoretical analysis for the number of rollouts and rollout length. To demonstrate this empirically, we evaluated the relative gradient estimation error vs. number of rollouts for the system {x_{t+1}=\left(\begin{bmatrix} 0.8 & 0.1 \\ 0.1 & 0.8 \end{bmatrix} + \delta_t \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} + \begin{bmatrix} 1 \\ 0 \end{bmatrix} K \right) x_t} with $K = 0, Q = \Sigma_0 = I_2, R = 1$, $\delta_t \sim \mathcal{N}(0,0.1)$, rollout length $l=40$, exploration radius $r = 0.2$, averaged over 10 gradient estimates. The results are plotted in Figure [fig:gradient\_estimation].

<!-- chunk {"id": "body-0105", "role": "body", "section": "Gradient Estimation", "weight": 1.0} -->

To achieve the same gradient estimate error of $10\%$, the system with multiplicative noise required $200 \times$ the number of rollout samples ($10^8$) as when there was no noise ($5 \times 10^5$).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Gradient Estimation", "weight": 1.0} -->

Relative gradient estimation error vs. number of rollouts for eq:gradient\_estimation\_example.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have shown that policy gradient methods in both model-based and model-free settings give global convergence to the globally optimal policy for LQR systems with multiplicative noise. These techniques are directly applicable for the design of robust controllers of uncertain systems and serve as a benchmark for data-driven control design. Our ongoing work is exploring ways of mitigating the relative sample inefficiency of model-free policy gradient methods by leveraging the special structure of LQR models and Nesterov-type acceleration, and exploring alternative system identification and adaptive control approaches. We are also investigating other methods of building robustness through $\mathcal{H}_\infty$ and dynamic game approaches. Another extension relevant to networked control systems is enforcing sparse structure constraints on the gain matrix via projected policy gradient as suggested in [bu2019lqr].

<!-- chunk {"id": "body-0108", "role": "body", "section": "Standard matrix expressions", "weight": 1.0} -->

Before proceeding with the proof of the main results of this study, we first review several basic expressions that will be used later throughout the section. In this section we let $A$, $B$, $C$, $M_i$ be generic matrices $\in \mathds{R}^{n \times m}$, $a$, $b$ be generic vectors, and $s$ be a generic scalar.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

The proof of convergence using gradient descent proceeds by establishing several technical lemmas, bounding the infinite-horizon covariance $\Sigma_K$, then using that bound to limit the step size, and finally obtaining a one-step bound on gradient descent progress and applying it inductively at each successive step. We begin with a bound on the induced operator norm of $\mathcal{T}_K$: ($\mathcal{T}_K$ norm bound) The following bound holds for any mean-square stabilizing $K$: \|\mathcal{T}_K\| \coloneqq \underset{X}{\text{sup}} \frac{\|\mathcal{T}_K(X)\|}{\|X\|} \leq \frac{C(K)}{{\underline{\sigma} (\Sigma_0)} \underline{\sigma}(Q)}.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

The proof follows that given in [Fazel2018] using our definition of $\mathcal{T}_K$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

The proof follows [Fazel2018] using our modified definitions of $\mathcal{T}_K$ and $\mathcal{F}_K$. [$\Sigma_K$ trace bound] If $\rho(\mathcal{F}_K) < 1$ then \Tr \left(\Sigma_{K}\right) \geq \frac{{\underline{\sigma} (\Sigma_0)}}{1-\rho(\mathcal{F}_K)}.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

We have a generic inequality for a sum of $n$ matrices $M_i$: \Tr \left[\sum_i^n M_i M_i^\intercal \right] = \sum_i^n \Tr \left[M_i M_i^\intercal \right] = \sum_i^n \left\| M_i \right\|_F^2 = \sum_i^n \left\| M_i \otimes M_i \right\|_F \geq \left\| \sum_i^n M_i \otimes M_i \right\|_F \nonumber where the last step is due to the triangle inequality.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

Recalling the definitions of $\mathcal{F}^t_K(I)$ and $\mathcal{F}^t_K$ we see they are of the form of the LHS and RHS in [eq:sum\_kron\_fro] with all terms matched between $\mathcal{F}^t_K(I)$ and $\mathcal{F}^t_K$ so that the inequality in [eq:sum\_kron\_fro] holds; this can be seen by starting with $t=1$ and incrementing $t$ up by $1$ which will give $(1+p+q)^t$ terms which are all matched.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

By hypothesis $\rho(\mathcal{F}_K) < 1$, and taking the sum of the geometric series completes the proof.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

First we show that $K$ is mean-square stabilizing and $ \|\Delta\| \leq h_\Delta(K) $ then $K{^\prime}$ is also mean-square stabilizing. This follows from an analogous argument in [Fazel2018] by characterizing mean-square stability in terms of $\rho(\mathcal{F}_K)$ rather than $\rho(A_K)$ and using Lemma [lemma:S\_K\_trace\_bound]. Let $K^{\prime\prime}$ be distinct from $K$ with $\rho(\mathcal{F}_{K^{\prime\prime}}) < 1$ and $ \|K^{\prime\prime}- K\| \leq h_\Delta $.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

Since spectral radius is a continuous function (see [Tyrtyshnikov2012]) there must be a point $K^{\prime\prime\prime}$ on the path between $K$ and $K^\prime$ such that $\rho(\mathcal{F}_{K^{\prime\prime\prime}}) = 1-\epsilon < 1$. Since $K$ and $K^{\prime\prime\prime}$ are mean-square stabilizing Lemma [lemma:Sigma\_K\_perturbation] holds so we have |\Tr(\Sigma_{K^{\prime\prime\prime}} - \Sigma_{K})| \leq n \frac{C(K)}{\sigma_{\min}(Q)}, \Tr(\Sigma_{K^{\prime\prime\prime}}) \leq \Tr(\Sigma_{K}) + n \frac{C(K)}{\sigma_{\min}(Q)} = \Gamma.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

However since $K^{\prime\prime\prime}$ is mean-square stabilizing Lemma [lemma:S\_K\_trace\_bound] holds so we have \Tr \left(\Sigma_{K^{\prime\prime\prime}}\right) \geq \frac{{\sigma_{\min} (\Sigma_0)}}{1-\rho(\mathcal{F}_{K^{\prime\prime\prime}})} = \frac{{2 \epsilon \Gamma}}{1-(1-\epsilon)} = 2 \Gamma which is a contradiction. Therefore no such mean-square unstable $K^\prime$ satisfying the hypothesized perturbation restriction can exist, completing the first part of the proof.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

Using Lemma [lemma:cost\_bounds] completes the proof.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

Now we bound the one step progress of policy gradient where we allow the step size to depend explicitly on the current gain matrix iterate [Gradient descent, one-step] Using the policy gradient step update with step size 0 < \eta \leq \frac{1}{16}\min \Bigg\{ \frac{ \left(\frac{\underline{\sigma}(Q) {\underline{\sigma} (\Sigma_0)}}{C(K)} \right)^2 }{ h_B \|\nabla C(K)\| (\|A_K\|+1)}, \frac{\underline{\sigma}(Q)}{C(K) \|R_K\|} \Bigg\} gives the one step progress bound \frac{ C(K_{s+1}) - C(K^*)}{ C(K_{s}) - C(K^*)} \leq 1 - 2 \eta \frac{ \underline{\sigma}(R) {\underline{\sigma}

<!-- chunk {"id": "body-0120", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

Adding 1 to both sides completes the proof. [Cost difference lower bound] The following cost difference inequality holds: C(K)-C(K^*) \geq \frac{{\underline{\sigma} (\Sigma_0)}}{\|R_K\|} \Tr(E_K^\intercal E_K).

<!-- chunk {"id": "body-0121", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

The proof follows that for an analogous condition located in the gradient domination lemma in [Fazel2018]. Let $K$ and $K{^\prime}$ generate the (stochastic) state and action sequences By definition of the optimal gains we have $C(K^*) \leq C(K{^\prime})$. Then by Lemma [lemma:value\_difference] we have &= -\underset{x_0}{\mathbb{E}} \bigg[\sum_{t=0}^\infty \mathcal{A}_{K}\big(\{x_t\}_{K{^\prime},x}, \{u_t\}_{K{^\prime},x}\big)\bigg].

<!-- chunk {"id": "body-0122", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

The proof follows [Fazel2018] with $R_K$ defined here. From the policy gradient expression we have \|\nabla C(K)\|_F^2 = \|2 E_K \Sigma_K\|_F^2 & = 4\Tr(\Sigma_K^\intercal E_K^\intercal E_K \Sigma_K) \\& \leq 4 \|\Sigma_K\|^2 \Tr(E_K^\intercal E_K).

<!-- chunk {"id": "body-0123", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

Then the claim of Theorem [thm:grad\_exact\_convergence] holds.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

We have by Weyl's inequality for singular values [eq:weyl1], submultiplicativity of spectral norm, and Lemma [lemma:gradient\_gain\_bounds] that Thus by choosing $0 < \eta \leq c_{pg}$ we satisfy the requirements for Lemma [lemma:grad\_exact\_one\_step] at $s=1$, which implies that progress is made at $s=1$, i.e., that $C(K_1)\leq C(K_0)$ according to the rate in Lemma [lemma:grad\_exact\_one\_step]. Proceeding inductively and applying Lemma [lemma:grad\_exact\_one\_step] at each step completes the proof.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Model-based policy gradient descent", "weight": 1.0} -->

The quantities $\overline{h_{1}}$, $\overline{h_{2}}$, and $\overline{\|R_{K}\|}$ may be upper bounded by quantities that depend only on problem data and $C(K_0)$ e.g. using the cost bounds in Lemma [lemma:cost\_bounds], which we omit for brevity, so a conservative minimum step size $\eta$ may be computed exactly.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

The overall proof technique of showing high probability convergence of model-free policy gradient proceeds by showing that the difference between estimated gradient and true gradient is bounded by a sufficiently small value that the iterative descent progress remains sufficiently large to maintain a linear rate. We use a matrix Bernstein inequality to ensure that enough sample trajectories are collected to estimate the gradient to high enough accuracy.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

We begin with a lemma shows that $C(K)$ and $\Sigma_K$ can be estimated with arbitrarily high accuracy as the rollout length $\ell$ increases. [Approximating $C(K)$ CK and $\Sigma_K$ SK with infinitely many finite horizon rollouts] Let $\epsilon$ be an arbitrary small constant. Suppose $K$ gives finite $C(K)$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

The proof follows [Fazel2018] exactly using suitably modified definitions of $C(K)$, $\mathcal{T}_K$, $\mathcal{F}_K$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Next we bound cost and gradient perturbations in terms of gain matrix perturbations and problem data. Using the same restriction as in Lemma [lemma:Sigma\_K\_perturbation] we have Lemmas [lemma:C\_K\_perturbation] and [lemma:nabla\_K\_C\_K\_perturbation].

<!-- chunk {"id": "body-0130", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

$C(K)$, $\mathcal{T}_K$, $\mathcal{F}_K$, however compared with [Fazel2018] we terminate the proof bound earlier so as to avoid a degenerate bound in the case of $K = 0$, and we also correct typographical errors. Note that $\|\Delta\|$ has a more restrictive upper bound due to the multiplicative noise.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

First we bound the second term of [eq:int2]. By Lemma [lemma:cost\_difference\_lower\_bound] \|E_K\| \leq \|E_K\|_F = \sqrt{\Tr(E_K^\intercal E_K)} \leq h_0(K).

<!-- chunk {"id": "body-0132", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

We now discuss smoothing of the cost in the context of model-free gradient descent. As in [Fazel2018], in the model-free setting we apply Frobenius-norm ball smoothing to the cost. Let $\mathbb{S}_r$ be the uniform distribution over all matrices with Frobenius norm $r$ (the boundary of the ball), and $\mathbb{B}_r$ be the uniform distribution over all matrices with Frobenius norm at most $r$ (the entire ball). The smoothed cost is C_{r}(K)=\mathbb{E}_{U \sim \mathbb{B}_r}[C(K+U)] where $U$ is a random matrix with the same dimensions as $K$ and Frobenius norm $r$. The following lemma shows that the gradient of the smoothed function can be estimated just with an oracle of the function value.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

[Zeroth-order gradient estimation] The gradient of the smoothed cost is related to the unsmoothed cost by \nabla C_{r}(K)=\frac{mn}{r^{2}} \mathbb{E}_{U \sim \mathbb{S}_r}[C(K+U) U].

<!-- chunk {"id": "body-0134", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

The result is proved in Lemma 2.1 in [Flaxman2005]. For completeness, we prove it here. By Stokes' Theorem we have \nabla \int_{\mathbb{B}_r} C(K+U) dU = \int_{\mathbb{S}_r} C(K+U) \left(\frac{U}{\|U\|_{F}}\right) dU=\int_{\mathbb{S}_r} C(K+U) \left(\frac{U}{r}\right) dU.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Lemma [lemma:zeroth\_order\_optimization] shows that the gradient of the smoothed cost can be found exactly with infinitely many infinite-horizon rollouts. Much of the remaining proofs goes towards showing that the error between the gradient of the smoothed cost and the unsmoothed cost, the error due to using finite-horizon rollouts, and the error due to using finitely many rollouts can all be bounded by polynomials of the problem data. As noted by [Fazel2018] the reason for smoothing in a Frobenius norm ball rather than over a Gaussian distribution is to ensure stability and finiteness of the cost of every gain within the smoothing domain, although now in the multiplicative noise case we must be even more restrictive about our choice of perturbation on $K$ because we require not only mean stability, but also mean-square stability.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

We now give a Bernstein inequality for random matrices and some simple variants; this allows us to bound the difference between the sample average of a random matrix and its expectation. [Matrix Bernstein inequality [Tropp2012]] Let $\{ Z_i \}_{i=1}^N$ be a set of $N$ independent random matrices of dimension $d_1 \times d_2$ with $d_+ = d_1 + d_2$, $\mathbb{E} [Z_i] = 0$, $\| Z_i \| \leq R$ almost surely, and maximum variance $\sigma^2:= \max \left(\left\| \sum_{i=1}^N \mathbb{E} (Z_i Z_i^\intercal) \right\|, \left\| \sum_{i=1}^N \mathbb{E} (Z_i^\intercal Z_i) \right\| \right)$.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Then for all $\epsilon \geq 0$ \mathbb{P} \left[\left\| \sum_{i=1}^N Z_i \right\| \geq \epsilon \right] \leq d_+ \exp \left(-\frac{3}{2} \cdot \frac{\epsilon^2}{3 \sigma^2 + R \epsilon} \right) The lemma and proof follow [Tropp2012] exactly.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Then for all $\epsilon \geq 0$ \mathbb{P} \left[\left\| \widehat{Z} - Z \right\| \geq \epsilon \right] \leq d_+ \exp \left(-\frac{3}{2} \cdot \frac{\epsilon^2 N}{3 \sigma^2 + R \epsilon} \right) The lemma follows readily from the matrix Bernstein inequality in Lemma [eq:matrix\_bernstein\_original] by variable substitutions. Notice that the bound in the RHS of this variant depends on the number of samples $N$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Let a small tolerance ${\epsilon \geq 0}$ and small probability ${ 0 \leq \mu \leq 1 }$ be given.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

First note that $\|K^\prime - K\|_F=\|\Delta\|_F=\|U\|_F=r$. We break the difference between estimated and true gradient $\hat{\nabla} C(K) - \nabla C(K)$ into two terms as \big(\nabla C_{r}(K)-\nabla C(K)\big)+\big(\hat{\nabla} C(K) -\nabla C_{r}(K)\big).

<!-- chunk {"id": "body-0141", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Since $r \leq h_\Delta(K)$ we see that Lemmas [lemma:C\_K\_perturbation] and [lemma:nabla\_K\_C\_K\_perturbation] hold. By enforcing the bound $r \leq \frac{1}{h_{\text{cost}}(K)}$, by Lemma [lemma:C\_K\_perturbation] and noting that $\|\Delta\| \leq \|\Delta\|_F$ we have |C(K \! +\! U)-C(K)| \leq C(K) \rightarrow C(K \! +\! U) \leq 2C(K). \phantom{} This ensures stability of the system under the perturbed gains so that $C(K+U)$ is well-defined.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Since $\nabla C_{r}(K)$ is the expectation of $\nabla C({K+U})$, by the triangle inequality we have \|\nabla C_{r}(K)-\nabla C({K})\|_F \leq \frac{\epsilon}{2}.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

For the second term $\hat{\nabla} C(K) - \nabla C_{r}(K)$, we work towards using the matrix Bernstein inequality and adopt the notation of the associated lemma. First note that by Lemma [lemma:zeroth\_order\_optimization] we have $Z:= \nabla C_{r}(K) = \mathbb{E}[\hat{\nabla} C(K)]$.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Next, from [eq:est\_grad\_inf\_first\_term] and Lemma [lemma:gradient\_gain\_bounds] we have & \leq \frac{\epsilon}{2} + \|\nabla C({K})\|_F \\& \leq \frac{\epsilon}{2} + h_1(K) so by the triangle inequality each sample difference has the bounded Frobenius norm & \leq \frac{2mn C(K)}{r} + \frac{\epsilon}{2} + h_1(K).

<!-- chunk {"id": "body-0145", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Adding the bounds on the two terms in [eq:int3] and using the triangle inequality completes the proof.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Suppose that the distribution of the initial states is such that $x_0 \sim \mathcal{P}_0$ implies $\|x_0^i\| \leq L_0$ almost surely for any given realization $x_0^i$ of $x_0$.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Suppose additionally that the multiplicative noises are distributed such that the following bound is satisfied almost surely under the closed-loop dynamics with any gain $K+U_i$ where $\|U_i\| \leq r$ for any given realized sequence $x_t^i$ of $x_t$ with a positive scalar $z \geq 1$ \sum_{t=0}^{\ell-1} \Big({x_{t}^{i}}^\intercal Q x_{t}^{i}+{u_{t}^{i}}^\intercal R u_{t}^{i} \Big) \leq z \underset{\delta, \gamma}{\mathbb{E}} \left[\sum_{t=0}^{\ell-1} \Big(x_t^\intercal Q x_t + u_t^\intercal R u_t \Big) \right].

<!-- chunk {"id": "body-0148", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Thus the choice of $r$ and $n_{\text{sample}}$ satisfy the conditions of Lemma [lemma:est\_grad\_inf], so with high probability of at least $1-\mu$ \|\hat{\nabla} C(K)-\nabla C(K)\|_F \leq \frac{\epsilon}{4}.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

For the second term, by using the choices $\ell \geq h_{\ell}\left(\frac{ r \epsilon }{ 4 m n }\right)$ and $C(K+U_i) \leq 2C(K)$, Lemma [lemma:finite\_horizon] holds and implies that \left\|C^{(\ell)}\left(K+U_i \right)-C\left(K+U_i \right)\right\|_F \leq \frac{r \epsilon}{4 mn}.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

$\sigma_{\widetilde{\nabla}}^2$ given in the assumption.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

Thus the polynomial $h_{\text{sample,trunc}}$ is large enough so the matrix Bernstein inequality implies \|\widetilde{\nabla} C(K) - \nabla^{\prime}_K C(K)\|_F \leq \frac{\epsilon}{4} with high probability $1-\mu$. Adding the three terms together and using the triangle inequality completes the proof.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

We now give the parameters and proof of high-probability global convergence in Theorem [thm:model-free].

<!-- chunk {"id": "body-0153", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

[Model-free policy gradient convergence] Consider the assumptions and notations of Theorem [thm:model-free] where the number of samples $n_{\text{sample}}$, rollout length $\ell$, and exploration radius $r$ are chosen according to the fixed quantities r \geq h_{r,\text{GD}} & \coloneqq h_{r} \left(\frac{\epsilon^\prime}{4} \right), \\\ell \geq h_{\ell,\text{GD}} & \coloneqq h_{\ell}\left(\frac{ r \epsilon^\prime }{ 4 m n }\right), \\n_{\text{sample}} \geq h_{\text{sample,GD}} & \coloneqq h_{\text{sample,trunc}} \left(\frac{\epsilon^\prime}{4}, \frac{\mu}{N},

<!-- chunk {"id": "body-0154", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

C(K) \leq 2 C(K_0) Then the claim of Theorem [thm:model-free] holds.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

The proof follows [Fazel2018] using the polynomials defined in our theorem. The last part of the proof is the same as in Theorem [thm:grad\_exact\_convergence]. As noted by [Fazel2018], the monotonic decrease in the function value during gradient descent and the choice of exploration radius $r$ are sufficient to ensure that all cost values encountered throughout the entire algorithm are bounded by $2 C(K_0)$, ensuring that all polynomial quantities used are bounded as well. We also require $\epsilon^\prime \leq \frac{ \overline{h_\Delta} }{\eta}$ in order for $ \| \Delta \| = \eta \| \widetilde{\nabla} C(K) - \nabla_K C(K)) \|$ to satisfy the condition of Lemma [lemma:C\_K\_perturbation].

<!-- chunk {"id": "body-0156", "role": "body", "section": "Model-free policy gradient descent", "weight": 1.0} -->

As in Remark [rem:param\_bounds], the quantities $\overline{h_{\text{cost}}}$ and $\overline{h_\Delta}$ may be upper (lower) bounded by quantities that depend on problem data and $C(K_0)$, so a conservative minimum exploration radius $r$, number of rollouts $n_{\text{sample}}$, and rollout length $\ell$ can be computed exactly in terms of problem data. Looking back across the terms that feed into the step size, number of rollouts, rollout length, and exploration radius, we see $C(K)$, $\|\Sigma_K\|$, $\|P_K\|$, and $\|B\|^2 + \sum_{j=1}^q \beta_j \|B_j\|^2$ are necessarily greater with state- and/or input-dependent multiplicative noise, and thus the algorithmic parameters are worsened by the noise.
