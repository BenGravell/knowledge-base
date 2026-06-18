<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Robust Control for LQR Systems with Multiplicative Noise via Policy Gradient

Topics include Gradient method, Gradient descent, Natural gradients, Reinforcement learning, Policy gradients, Linear systems, Uncertain systems, Optimal control, Stochastic systems, Multiplicative noise, Non-convex, Dynamics, Global convergence, Linear quadratic regulator.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides non-asymptotic finite-sample convergence results for policy gradient algorithms applied to the problem of optimal control of linear systems with multiplicative noise when the dynamics and noise covariances are unknown.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The linear quadratic regulator (LQR) problem has reemerged as an important theoretical benchmark for reinforcement learning-based control of complex dynamical systems with continuous state and action spaces. In contrast with nearly all recent work in this area, we consider multiplicative noise models, which are increasingly relevant because they explicitly incorporate inherent uncertainty and variation in the system dynamics and thereby improve robustness properties of the controller. Robustness is a critical and poorly understood issue in reinforcement learning; existing methods which do not account for uncertainty can converge to fragile policies or fail to converge at all. Additionally, intentional injection of multiplicative noise into learning algorithms can enhance robustness of policies, as observed in ad hoc work on domain randomization. Although policy gradient algorithms require optimization of a non-convex cost function, we show that the multiplicative noise LQR cost has a special property called gradient domination, which is exploited to prove global convergence of policy gradient algorithms to the globally optimum control policy with polynomial dependence on problem parameters. Results are provided both in the model-known and model-unknown settings where samples of system trajectories are used to estimate policy gradients.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning-based control has recently achieved impressive successes in games and simulators. But these successes are significantly more challenging to translate to complex physical systems with continuous state and action spaces, safety constraints, and non-negligible operation and failure costs that demand data efficiency. An intense and growing research effort is creating a large array of models, algorithms, and heuristics for approaching the myriad of challenges arising from these systems. To complement a dominant trend of more computationally focused work, the canonical linear quadratic regulator (LQR) problem in control theory has reemerged as an important theoretical benchmark for learning-based control. Despite its long history, there remain fundamental open questions for LQR with unknown models, and a foundational understanding of learning in LQR problems can give insight into more challenging problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Almost all recent work on learning in LQR problems has utilized either deterministic or additive noise models, but here we consider *multiplicative noise models*. In control theory, multiplicative noise models have been studied almost as long as their deterministic and additive noise counterparts, although this area is somewhat less developed and far less widely known. We believe the study of learning in LQR problems with multiplicative noise is important for three reasons. First, this class of models is much richer than deterministic or additive noise while still allowing exact solutions when models are known, which makes it a compelling additional benchmark. Second, they explicitly incorporate model uncertainty and inherent stochasticity, thereby improving robustness properties of the controller. Robustness is a critical and poorly understood issue in reinforcement learning; existing methods which do not account for uncertainty can converge to fragile policies or fail to converge at all. Additionally, intentional injection of multiplicative noise into learning algorithms is known to enhance robustness of policies from ad hoc work on domain randomization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, in emerging difficult-to-model complex systems where learning-based control approaches are perhaps most promising, multiplicative noise models are increasingly relevant; examples include networked systems with noisy communication channels, modern power networks with large penetration of intermittent renewables, turbulent fluid flow, and neuronal brain networks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Related literature", "weight": 1.0} -->

Multiplicative noise LQR problems have been studied in control theory since the 1960s. Since then a line of research parallel to deterministic and additive noise has developed, including basic stability and stabilizability results, semidefinite programming formulations, robustness properties, and numerical algorithms. This line of research is less widely known perhaps because much of it studies continuous time systems, where the heavy machinery required to formalize stochastic differential equations is a barrier to entry for a broad audience. Multiplicative noise models are well-poised to offer data-driven model uncertainty representations and enhanced robustness in learning-based control algorithms and complex dynamical systems and processes. A related line of research which has seen recent activity is on learning optimal control of Markovian jump linear systems with unknown dynamics and noise distributions, which under certain assumptions form a special case of the multiplicative noise system we analyze in this work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Related literature", "weight": 1.0} -->

In contrast to classical work on system identification and adaptive control, which has a strong focus on asymptotic results, more recent work has focused on non-asymptotic analysis using newly developed mathematical tools from statistics and machine learning. There remain fundamental open problems for learning in LQR problems, with several addressed only recently, including non-asymptotic sample complexity, regret bounds, and algorithmic convergence. Alternatives to reinforcement learning include other data-driven model-free optimal control schemes and those leveraging the behavioral framework. Subspace identification methods offer a model-based generalization to the output feedback setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In §2 we establish the multiplicative noise LQR problem and motivate its study via a connection to robust stability. We then give several fundamental results for policy gradient algorithms on linear quadratic problems with multiplicative noise. Our main contributions are as follows, which can be viewed as a generalization of the recent results of Fazel et al.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In §3 we show that although the multiplicative noise LQR cost is generally non-convex, it has a special property called *gradient domination*, which facilitates its optimization (Lemmas 3.1. ‣ 3.1. Multiplicative Noise LQR Cost is Gradient Dominated ‣ 3. Gradient Domination and Other Properties of the Multiplicative Noise LQR Cost ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient") and 3.3. ‣ 3.1. Multiplicative Noise LQR Cost is Gradient Dominated ‣ 3. Gradient Domination and Other Properties of the Multiplicative Noise LQR Cost ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient")).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In particular, in §4 the gradient domination property is exploited to prove global convergence of three policy gradient algorithm variants (namely, exact gradient descent, "natural" gradient descent, and Gauss-Newton/policy iteration) to the globally optimum control policy with a rate that depends polynomially on problem parameters (Theorems 4.1. ‣ 4.2. Gauss-Newton Descent ‣ 4. Global Convergence of Policy Gradient in the Model-Based Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient"), 4.2. ‣ 4.3. Natural Policy Gradient Descent ‣ 4. Global Convergence of Policy Gradient in the Model-Based Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient"), and 4.3. ‣ 4.4. Policy Gradient Descent ‣ 4. Global Convergence of Policy Gradient in the Model-Based Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient")).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Furthermore, in §5 we show that a model-free policy gradient algorithm, where the gradient is estimated from trajectory data ("rollouts") rather than computed from model parameters, also converges globally (with high probability) with an appropriate exploration scheme and sufficiently many samples (polynomial in problem data) (Theorem 5.1. ‣ 5. Global Convergence of Policy Gradient in the Model-Free Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient")).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We quantify the increase in computational burden of policy gradient methods due to the presence of multiplicative noise, which is evident from the bounds developed in Appendices B and C. The noise acts to reduce the step size and thus convergence rate, and increases the required number of samples and rollout length in the model-free setting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our contributions", "weight": 1.0} -->

A covariance dynamics operator $\mathcal{F}_{K}$ is established for multiplicative noise systems with a more complicated form than the deterministic case. This necessitated a more careful treatment and novel proof by induction and term matching argument in the proof of Lemma B.4. ‣ Appendix B Model-based policy gradient descent ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient").

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Several restrictions on the algorithmic parameters (step size, number of rollouts, rollout length, exploration radius) which are necessary for convergence are established and treated.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our contributions", "weight": 1.0} -->

An important restriction on the support of the multiplicative noise distribution, which is naturally absent, is established in the model-free setting.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our contributions", "weight": 1.0} -->

A matrix Bernstein concentration inequality is stated explicitly and used to give explicit bounds on the algorithmic parameters in the model-free setting in terms of problem data.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Discussion and numerical results on the use of backtracking line search is included.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Our contributions", "weight": 1.0} -->

When the multiplicative variances $\alpha_{i}$, $\beta_{j}$ are all zero, the assertions of Theorems 4.1. ‣ 4.2. Gauss-Newton Descent ‣ 4. Global Convergence of Policy Gradient in the Model-Based Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient"), 4.2. ‣ 4.3. Natural Policy Gradient Descent ‣ 4. Global Convergence of Policy Gradient in the Model-Based Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient"), 4.3. ‣ 4.4. Policy Gradient Descent ‣ 4. Global Convergence of Policy Gradient in the Model-Based Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient"), 5.1. ‣ 5. Global Convergence of Policy Gradient in the Model-Free Setting ‣ Learning Robust Controllers for Linear Quadratic Systems with Multiplicative Noise via Policy Gradient") recover the same step sizes and convergence rates of the deterministic setting reported.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Thus, policy gradient algorithms for the multiplicative noise LQR problem enjoy the same global convergence properties as deterministic LQR, while significantly enhancing the resulting controller's robustness to variations and inherent stochasticity in the system dynamics, as demonstrated by our numerical experiments in §6.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Our contributions", "weight": 1.0} -->

To our best knowledge, the present paper is the first work to consider and obtain global convergence results using reinforcement learning algorithms for the multiplicative noise LQR problem. Our approach allows the explicit incorporation of a model uncertainty representation that significantly improves the robustness of the controller compared to deterministic and additive noise approaches.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

We consider the infinite-horizon linear quadratic regulator problem with multiplicative noise (LQRm)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

(across time), zero-mean, mutually independent scalar random variables $\delta_{ti}$ and $\gamma_{tj}$, which have variances $\alpha_{i}$ and $\beta_{j}$, respectively. The matrices $A_{i} \in {\mathbb{R}}^{n \times n}$ and $B_{i} \in {\mathbb{R}}^{n \times m}$ specify how each scalar noise term affects the system dynamics and input matrices. Alternatively, suppose ${bar}A$ and ${bar}B$ are zero-mean random matrices with a joint covariance structure^11^1We assume ${bar}A$ and ${bar}B$ are independent for simplicity, but it is straightforward to include correlations between the entries of ${bar}A$ and ${bar}B$ into the model.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

Then it suffices to take the variances $\alpha_{i}$ and $\beta_{j}$ and matrices $A_{i}$ and $B_{j}$ as the eigenvalues and (reshaped) eigenvectors of $\Sigma_{A}$ and $\Sigma_{B}$, respectively, after a projection onto a set of orthogonal real-valued vectors. The goal is to determine a closed-loop state feedback policy $\pi^{\ast}$ with $u_{t} = {\pi^{\ast}{(x_{t})}}$ from a set $\Pi$ of admissible policies which solves the optimization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

We assume that the problem data $A$, $B$, $\alpha_{i}$, $A_{i}$, $\beta_{j}$, and $B_{j}$ permit existence and finiteness of the optimal value of the problem, in which case the system is called *mean-square stabilizable* and requires *mean-square stability* of the closed-loop system.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimal Control of Linear Systems with Multiplicative Noise and Quadratic Costs", "weight": 1.0} -->

Mean-square stability is a form of robust stability, implying stability of the mean (i.e. ${\lim_{t\rightarrow\infty}{{\mathbb{E}}x_{t}}} = {0{\forall x_{0}}}$) as well as almost-sure stability (i.e. ${\lim_{t\rightarrow\infty}x_{t}} = 0$ almost surely). Mean-square stability requires stricter and more complicated conditions than stabilizability of the nominal system $(A,B)$, which are discussed in the sequel. This essentially can limit the size of the multiplicative noise covariance, which can be viewed as a representation of uncertainty in the nominal system model or as inherent variation in the system dynamics.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

Dynamic programming can be used to show that the optimal policy $\pi^{\ast}$ is linear state feedback $u_{t} = {\pi^{\ast}{(x_{t})}} = {K^{\ast}x_{t}}$, where $K^{\ast} \in {\mathbb{R}}^{m \times n}$ denotes the optimal gain matrix. When the control policy is linear state feedback $u_{t} = {\pi{(x_{t})}} = {Kx_{t}}$, with a very slight abuse of notation the cost becomes

<!-- chunk {"id": "body-0028", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

Dynamic programming further shows that the resulting optimal cost is quadratic in the initial state, i.e. ${C{(K^{\ast})}} = {{\mathbb{E}}_{x_{0}}x_{0}^{\intercal}Px_{0}} = {{Tr}{({P\Sigma_{0}})}}$, where $P \in {\mathbb{R}}^{n \times n}$ is a symmetric positive definite matrix. Note that the optimal controller does not need to directly observe the noise variables $\delta_{ti}$, $\gamma_{tj}$. When the model parameters are known, there are several ways to compute the optimal feedback gains and corresponding optimal cost. The optimal cost is given by the solution of the *generalized* algebraic Riccati equation (GARE)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

This is a special case of the GARE for optimal static output feedback given in and can be solved via the value iteration

<!-- chunk {"id": "body-0030", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

with $P_{0} = Q$, or via semidefinite programming formulations, or via more exotic iterations based on the Smith method and Krylov subspaces. The associated optimal gain matrix is

<!-- chunk {"id": "body-0031", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

It was verified in that existence of a positive definite solution to the GARE is equivalent to mean-square stabilizability of the system, which depends on the problem data $A$, $B$, $\alpha_{i}$, $A_{i}$, $\beta_{j}$, and $B_{j}$; in particular, mean-square stability generally imposes upper bounds on the variances $\alpha_{i}$ and $\beta_{j}$, but may be infinite depending on the structure of $A$, $B$, $A_{i}$, and $B_{j}$. At a minimum, uniqueness and existence of a solution to the GARE requires the standard conditions for uniqueness and existence of a solution to the standard ARE, namely of $(A,B)$ stabilizable and $(A,Q^{1/2})$ detectable.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Control Design with Known Models: Value Iteration", "weight": 1.0} -->

Although (approximate) value iteration can be implemented using sample trajectory data, policy gradient methods have been shown to be more effective for approximately optimal control of high-dimensional stochastic nonlinear systems e.g. those arising in robotics. This motivates our following analysis of the simpler case of stochastic linear systems wherein we show that policy gradient indeed facilitates a data-driven approach for learning optimal and robust policies.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Consider a fixed linear state feedback policy $u_{t} = {Kx_{t}}$. Defining the stochastic system matrices

<!-- chunk {"id": "body-0034", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

the deterministic nominal and stochastic closed-loop system matrices

<!-- chunk {"id": "body-0035", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

and the closed-loop state-cost matrix

<!-- chunk {"id": "body-0036", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

A gain $K$ is mean-square stabilizing if the closed-loop system is mean-square stable. Denote the set of mean-square stabilizing $K$ as $\mathcal{K}$. If $K \in \mathcal{K}$, then the cost can be written as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

where $P_{K}$ is the unique positive semidefinite solution to the *generalized* Lyapunov equation

<!-- chunk {"id": "body-0038", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

We define the state covariance matrices and the infinite-horizon aggregate state covariance matrix as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

If $K \in \mathcal{K}$ then $\Sigma_{K}$ also satisfies a *dual* generalized Lyapunov equation

<!-- chunk {"id": "body-0040", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Vectorization and Kronecker products can be used to convert and into systems of linear equations. Alternatively, iterative methods have been suggested for their solution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

Thus $\mathcal{F}_{K}$ (without an argument) is a linear operator whose matrix representation is

<!-- chunk {"id": "body-0042", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

The $\Sigma_{t}$ evolve according to the dynamics

<!-- chunk {"id": "body-0043", "role": "body", "section": "Control Design with Known Models: Policy Gradient", "weight": 1.0} -->

which gives the natural characterization

<!-- chunk {"id": "body-0044", "role": "body", "section": "From Stochastic to Robust Stability", "weight": 1.0} -->

Additional motivation for designing controllers which stabilize a stochastic system in mean-square is to ensure robustness of stability of a nominal deterministic system to model parameter perturbations. Here we state a condition which guarantees robust deterministic stability for a perturbed deterministic system given mean-square stability of a stochastic single-state system with multiplicative noise where the noise variance and parameter perturbation size are related.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 2.2 (Robust stability)", "weight": 1.0} -->

Suppose the stochastic closed-loop system

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 2.2 (Robust stability)", "weight": 1.0} -->

where $a,x_{t},\delta_{t}$ are scalars with ${{\mathbb{E}}{\lbrack\delta_{t}^{2}\rbrack}} = \alpha$ is mean-square stable. Then, the perturbed deterministic system

<!-- chunk {"id": "body-0047", "role": "body", "section": "Gradient Domination and Other Properties of the Multiplicative Noise LQR Cost", "weight": 1.0} -->

In this section, we demonstrate that the multiplicative noise LQR cost function is *gradient dominated*, which facilitates optimization by gradient descent. Gradient dominated functions have been studied for many years in the optimization literature and have recently been discovered in deterministic LQR problems.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Multiplicative Noise LQR Cost is Gradient Dominated", "weight": 1.0} -->

First, we give the expression for the policy gradient of the multiplicative noise LQR cost.^22^2We include a factor of 2 on the gradient expression that was erroneously dropped. This affects the step size restrictions by a corresponding factor of 2. Define

<!-- chunk {"id": "body-0049", "role": "body", "section": "Additional Setup Lemmas", "weight": 1.0} -->

Following we refer to Lipschitz continuity of the gradient as ($\mathcal{C}^{1}$-)smoothness, and so this section deals with showing that the LQR cost satisfies an expression that is almost of the exact form of a Lipschitz continuous gradient.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

For small deviations $K^{\prime} - K$ the equation in the almost-smoothness lemma exactly describes a Lipschitz continuous gradient. The naming should not be taken to imply that the LQRm cost is not smooth, but rather that the equation as stated does not immediately yield a Lipschitz constant; indeed the Lipschitz constant is what much of the later proofs go towards bounding (implicitly) i.e. by bounding higher-order terms which must be accounted for when $K^{\prime} \neq K$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

To be specific, a Lipschitz continuous gradient to $C{(K)}$ implies there exists a Lipschitz constant $L$ such that

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

for all $K^{\prime}$, $K$. This is the quadratic upper bound which is used e.g. in Thm. 1 of to prove convergence of gradient descent on a gradient dominated objective function. The "almost"-smoothness condition is that

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

which is exactly of the form of the Lipschitz gradient condition with Lipschitz constant $2{\|\Sigma_{K}\|}{\| R_{K}\|}$. Note this is not a global Lipschitz condition since $2{\|\Sigma_{K}\|}{\| R_{K}\|}$ becomes unbounded as $K$ becomes mean-square destabilizing, but rather a local Lipschitz condition since $2{\|\Sigma_{K}\|}{\| R_{K}\|}$ is bounded on any sublevel set of $C{(K)}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Global Convergence of Policy Gradient in the Model-Based Setting", "weight": 1.0} -->

In this section we show that the policy gradient algorithm and two important variants for multiplicative noise LQR converge globally to the optimal policy. In contrast, the policies we obtain are robust to uncertainties and inherent stochastic variations in the system dynamics.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Global Convergence of Policy Gradient in the Model-Based Setting", "weight": 1.0} -->

The more elaborate natural gradient and Gauss-Newton variants provide superior convergence rates and simpler proofs. A development of the natural policy gradient is given in building on ideas. The Gauss-Newton step with step size $\frac{1}{2}$ is in fact identical to the policy improvement step in policy iteration (a short derivation is given shortly) and was first studied for deterministic LQR. This was extended to a model-free setting using policy iteration and Q-learning, proving asymptotic convergence of the gain matrix to the optimal gain matrix. For multiplicative noise LQR, we have the following results.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Stationary points occur when the gradient is zero, so differentiating with respect to $u$ we obtain

<!-- chunk {"id": "body-0057", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Setting to zero and solving for $u$ gives

<!-- chunk {"id": "body-0058", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

confirming that the stationary point is indeed a global minimum.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Thus the policy iteration gain matrix update is

<!-- chunk {"id": "body-0060", "role": "body", "section": "Derivation of the Gauss-Newton step from policy iteration", "weight": 1.0} -->

Parameterizing with a step size gives the Gauss-Newton step

<!-- chunk {"id": "body-0061", "role": "body", "section": "Global Convergence of Policy Gradient in the Model-Free Setting", "weight": 1.0} -->

The results in the previous section are model-based; the policy gradient steps are computed exactly based on knowledge of the model parameters. In the model-free setting, the policy gradient is estimated to arbitrary accuracy from sample trajectories with a sufficient number of sample trajectories $n_{\text{sample}}$ of sufficiently long horizon length $\ell$ using gain matrices randomly selected from a Frobenius-norm ball around the current gain of sufficiently small exploration radius $r$. We show for multiplicative noise LQR that with a finite number of samples polynomial in the problem data, the model-free policy gradient algorithm still converges to the globally optimal policy, despite small perturbations on the gradient.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Global Convergence of Policy Gradient in the Model-Free Setting", "weight": 1.0} -->

In the model-free setting, the policy gradient method proceeds as before except that at each iteration Algorithm 1 is called to generate an estimate of the gradient via the zeroth-order optimization procedure described by Fazel et al..

<!-- chunk {"id": "body-0063", "role": "body", "section": "Global Convergence of Policy Gradient in the Model-Free Setting", "weight": 1.0} -->

0: Gain matrix K, number of samples nsample, rollout length ℓ, exploration radius r 2: Generate a sample gain matrix K̂i = K + Ui, where Ui is drawn uniformly at random over matrices with Frobenius norm r 3: Generate a sample initial state x0(i) ∼ 𝒫0 4: Simulate the closed-loop system for ℓ steps according to the stochastic dynamics in starting from x0(i) with ut(i) = K̂i xt(i), yielding the state sequence {xt(i)}t = 0t = ℓ 5: Collect the empirical finite-horizon cost estimate ${\hat{C}}_{i} ≔ {\sum_{t = 0}^{\ell}{{}_{}^{(i)}{({Q + {{\hat{K}}_{i}^{\intercal}R{\hat{K}}_{i}}})}x_{t}^{(i)}}}$ 6: Gradient estimate ${\hat{\nabla}C{(K)}} ≔

<!-- chunk {"id": "body-0064", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Shows that "optimal" control that ignores actual multiplicative noise can lead to loss of mean-square stability,

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Shows the efficacy of the policy gradient algorithms on a networked system,

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Shows the increased difficulty of estimating the gradient from sample data in the presence of multiplicative noise.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All systems considered permitted a solution to the GARE. The bounds on the step size, number of rollouts, and rollout length given by the theoretical analysis can be rather conservative. For practicality, we selected the constant step size, number of rollouts, rollout length, and exploration radius according to a grid search over reasonable values. Additionally, we investigated the use of backtracking line search to adaptively select the step size; see e.g.. Throughout the simulations, we computed the baseline optimal cost $C{(K^{\ast})}$ by solving the GARE to high precision via value iteration. Python code which implements the algorithms and generates the figures reported in this work can be found in the GitHub repository at The code was run on a desktop PC with a quad-core Intel i7 6700K 4.0GHz CPU, 16GB RAM; no GPU computing was utilized.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Importance of Accounting for Multiplicative Noise", "weight": 1.0} -->

We performed model-based policy gradient descent; at each iteration gradients were calculated by solving generalized Lyapunov equations and using the problem data. The gains $K_{m}$ and $K_{\ell}$ represent iterates during optimization of ("training" on) the LQRm and LQR cost (with the multiplicative noise variances set to zero), respectively. We performed the optimization starting from the same feasible initial gain, which was generated by perturbing the exact solution of the generalized algebraic Riccati equation such that the LQRm cost under the initial control was approximately 10 times that of the optimal control. The step size was chosen via backtracking line search. The optimization stopped once the Frobenius norm of the gradient fell below a small threshold. The plot in Fig. 1 shows the "testing" cost of the gains at each iteration evaluated on the LQRm cost (with multiplicative noise). From this figure, it is clear that $K_{m}$ minimized the LQRm as desired.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Importance of Accounting for Multiplicative Noise", "weight": 1.0} -->

When there was high multiplicative noise, the noise-ignorant controller $K_{\ell}$ actually destabilized the system in the mean-square sense; this can be seen as the LQRm cost exploded upwards to infinity after iteration 10. In this sense, the multiplicative noise-aware optimization is generally safer and more robust than noise-ignorant optimization, and in examples like this is actually necessary for mean-square stabilization.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

Many practical networked systems can be approximated by diffusion dynamics with losses and stochastic diffusion constants (edge weights) between nodes; examples include heat flow through uninsulated pipes, hydraulic flow through leaky pipes, information flow between processors with packet loss, electrical power flow between generators with resistant electrical power lines, etc. A derivation of the discrete-time dynamics of this system is given.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

This system is open-loop mean-square stable, so we initialized the gains to all zeros for each trial. We performed policy optimization using the model-free gradient, and the model-based gradient, model-based natural gradient, and model-based Gauss-Newton step directions on 20 unique problem instances using two step size schemes:\
Backtracking line search: Step sizes $\eta$ were chosen adaptively at each iteration by backtracking line search with parameters $\alpha = 0.01$, $\beta = 0.5$ (see for a description), except for Gauss-Newton which used the optimal constant step-size of $1/2$. Model-free gradients and costs were estimated with 100,000 rollouts per iteration.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

We ran a fixed number, 20, of iterations chosen such that the final cost using model-free gradient descent was no more than $5\%$ worse than optimal.\
Constant step size: Step sizes were set to constants chosen as large as possible without observing infeasibility or divergence, which on this problem instance was $\eta = {5 \times 10^{- 5}}$ for gradient, $\eta = {2 \times 10^{- 4}}$ for natural gradient, and $\eta = {1/2}$ for Gauss-Newton step directions. Model-free gradients were estimated with 1,000 rollouts per iteration. We ran a fixed number, 20,000, of iterations chosen such that convergence was achieved with all step directions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

In both cases sample gains were chosen for model-free gradient estimation with exploration radius $r = 0.1$ and the rollout length was set to $\ell = 20$. The plots in Fig. 2 show the relative cost over the iterations; for the model-free gradient descent, the bold centerline is the mean of all trials and the shaded region is between the 10^th^ and 90^th^ percentile of all trials. Using backtracking line search, it is evident that in terms of convergence the Gauss-Newton step was extremely fast, and both the natural gradient and model-based gradient were slightly slower, but still quite fast. The model-free policy gradient converged to a reasonable neighborhood of the minimum cost quickly, but stagnated with further iterations; this is a consequence of the inherent gradient and cost estimation errors that arise due to random sampling and the multiplicative noise. Using constant stepsizes, we were forced to take small steps due to the steepness of the cost function near the initial gains, slowing overall convergence using the gradient and natural gradient methods. Here we observed that Gauss-Newton again converged most quickly, followed by natural gradient and lastly the gradient methods.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Policy Gradient Methods Applied to a Network", "weight": 1.0} -->

The smaller step size also allowed us to use far fewer samples in the model-free setting, where we observed somewhat faster initial cost decrease with eventual stagnation around $10^{- 2}$, or 1%, relative error, which represents excellent control performance. All algorithms exhibited convergence to the optimum, confirming the asserted theoretical claims.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Gradient Estimation", "weight": 1.0} -->

Multiplicative noise can significantly increase the variance and sample complexity of cost gradient estimates relative to the noiseless case, which is novelly reflected in the theoretical analysis for the number of rollouts and rollout length. To demonstrate this empirically, we evaluated the relative gradient estimation error vs. number of rollouts for the system

<!-- chunk {"id": "body-0076", "role": "body", "section": "Gradient Estimation", "weight": 1.0} -->

with ${{K = 0},{Q = \Sigma_{0} = I_{2}}},{R = 1}$, $\delta_{t} \sim {\mathcal{N}{(0,0.1)}}$, rollout length $l = 40$, exploration radius $r = 0.2$, averaged over 10 gradient estimates. The results are plotted in Figure 3. To achieve the same gradient estimate error of $10\%$, the system with multiplicative noise required $200 \times$ the number of rollout samples ($10^{8}$) as when there was no noise ($5 \times 10^{5}$).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have shown that policy gradient methods in both model-based and model-free settings give global convergence to the globally optimal policy for LQR systems with multiplicative noise. These techniques are directly applicable for the design of robust controllers of uncertain systems and serve as a benchmark for data-driven control design. Our ongoing work is exploring ways of mitigating the relative sample inefficiency of model-free policy gradient methods by leveraging the special structure of LQR models and Nesterov-type acceleration, and exploring alternative system identification and adaptive control approaches. We are also investigating other methods of building robustness through $\mathcal{H}_{\infty}$ and dynamic game approaches. Another extension relevant to networked control systems is enforcing sparse structure constraints on the gain matrix via projected policy gradient as suggested.
