<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods

Topics include Policy gradients, Sample complexity, Natural policy gradient, NPG, Variance reduction.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we revisit and improve the convergence of policy gradient (PG), natural PG (NPG) methods, and their variance-reduced variants, under general smooth policy parametrizations. More specifically, with the Fisher information matrix of the policy being positive definite: i) we show that a state-of-the-art variance-reduced PG method, which has only been shown to converge to stationary points, converges to the globally optimal value up to some inherent function approximation error due to policy parametrization; ii) we show that NPG enjoys a lower sample complexity; iii) we propose SRVR-NPG, which incorporates variance-reduction into the NPG update. Our improvements follow from an observation that the convergence of (variance-reduced) PG and NPG methods can improve each other: the stationary convergence analysis of PG can be applied to NPG as well, and the global convergence analysis of NPG can help to establish the global convergence of (variance-reduced) PG methods. Our analysis carefully integrates the advantages of these two lines of works. Thanks to this improvement, we have also made variance-reduction for NPG possible, with both global convergence and an efficient finite-sample complexity.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient (PG) methods, or more generally direct policy search methods, have long been recognized as one of the foundations of reinforcement learning (RL). Specifically, PG methods directly search for the optimal policy parameter that maximizes the long-term return in Markov decision processes (MDPs), following the policy gradient ascent direction. This search direction can be more efficient using a preconditioning matrix, e.g., using the natural PG direction. These methods have achieved tremendous empirical successes recently, especially boosted by the power of (deep) neural networks for policy parametrization. These successes are primarily attributed to the fact that PG methods naturally incorporate *function approximation* for policy parametrization, in order to handle massive and even continuous state-action spaces.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, the policy gradients are usually estimated via samples using Monte-Carlo rollouts and bootstrapping. Such stochastic PG methods notoriously suffer from very high variances, which not only destabilize but also slow down the convergence. Several conventional approaches have been advocated to reduce the variance of PG methods, e.g., by adding a baseline, or by using function approximation for estimating the value function, namely, developing actor-critic algorithms. More recently, motivated by the advances of variance-reduction techniques in stochastic optimization, there have been surging interests in developing *variance-reduced* PG methods, which are shown to be faster.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to the empirical successes of PG methods, their theoretical convergence guarantees, especially *non-asymptotic global* convergence guarantees, have not been addressed satisfactorily until very recently. By *non-asymptotic global* convergence, here we mean the convergence behavior of PG methods from any initialization, and the quality of the point they converge to (usually enjoys global optimality up to some compatible function approximation error due to policy parametrization), after a finite number of iterations/samples. These recent prominent guarantees are normally beyond the folklore *first-order* stationary-point convergence^11^1That is, finding a parameter $\theta$ such that ${\|{{\nabla J}{(\theta)}}\|}^{2} \leq \varepsilon$, where $J$ is the expected return., as expected from a *stochastic nonconvex optimization* perspective of solving RL with PG methods. Special landscapes of the RL objective, though nonconvex, have enabled the convergence to even globally optimal values.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, none of the aforementioned variance-reduced PG methods have been shown to enjoy these desired global convergence properties. It remains unclear whether these methods can converge to beyond first-order stationary policies.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by these advances and the questions that remain to be answered, we aim in this paper to improve the convergence of PG and natural PG (NPG) methods, and their variance-reduced variants, under general smooth policy parametrizations. Our contributions are summarized as follows.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. With a focus on the conventional Monte-Carlo-based PG methods, we propose a general framework for analyzing their *global convergence*. Our contribution is three-fold: first, we establish the global convergence up to compatible function approximation errors due to policy parametrization, for a variance-reduced PG method SRVR-PG; second, we improve the global convergence of NPG methods established, from $\mathcal{O}\left( \varepsilon^{- 4} \right)$ to $\mathcal{O}\left( \varepsilon^{- 3} \right)$; third, we propose a new variance-reduced algorithm based on NPG, and establish its global convergence with an efficient sample-complexity. These improvements are based on a framework that integrates the advantages of previous analyses on (variance reduced) PG and NPG, and rely on a (mild) assumption that the Fisher information matrix induced by the policy parametrization is positive definite (see Assumption 2.1 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A comparison of previous results and our improvements is laid out in Table 1 Policy Gradient and Natural Policy Gradient Methods").

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Global Convergence of (Natural) PG. Recently, there has been a surging research interest in investigating the global convergence of PG and NPG methods, which is beyond the folklore convergence to first-order stationary policies. In the special case with linear dynamics and quadratic reward, shows that PG methods with random search converge to the globally optimal policy with linear rates. In, with a simple reward-reshaping, PG methods have been shown to converge to the second-order stationary-point policies. shows that for finite-MDPs and several control tasks, the nonconvex RL objective has no suboptimal local minima. prove that (natural) PG methods converge to the globally optimal value when overparametrized neural networks are used for function approximation. provides a fairly general characterization of global convergence for these methods, and a basic sample complexity result for sample-based NPG updates. It is also worth noting that trust-region policy optimization (TRPO), as a variant of NPG, also enjoys global convergence with overparametrized neural networks, and for regularized MDPs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Very recently, for actor-critic algorithms, a series of non-asymptotic convergence results have also been established, with global convergence guarantees when natural PG/PPO are used in the actor step.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Variance-Reduction (VR) for PG. Conventional approaches to reduce the high variance in PG methods include using (natural) actor-critic algorithms, and adding baselines. The idea of variance reduction (VR) is first proposed to accelerate stochastic minimization. VR algorithms such as SVRG, SAGA, SARAH, and Spider achieve acceleration over SGD in both convex and nonconvex settings. SVRG is also accelerated by applying a positive definite preconditioner that captures the curvature of the objective. Inspired by these successes in stochastic optimization, VR is also incorporated into PG methods, with empirical validations for acceleration, and analyzed rigorously. Then, improves the sample complexity of SVRPG, and proposes a new SRVR-PG method that uses recursively updated semi-stochastic policy gradient, which leads to an improved sample complexity of $\mathcal{O}{(\varepsilon^{- 1.5})}$ over previous works. More recently, proposes a new STORM-PG method, which blends momentum in the update and matches the sample complexity of, and applies the idea of SARAH and considers a more general setting with regularization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, heavy-ball type of momentum has also been applied to PG methods. We highlight that all these sample complexity results are for first-order stationary-point convergence (which might have arbitrarily bad performance: see (2.2 Policy Gradient and Natural Policy Gradient Methods"))), in contrast to the more desired global convergence guarantees (up to some function approximation errors that can be small) that we are interested.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

𝒪 (TT D ε−2) 111In, TT D iterations of temporal difference updates are needed at each iteration, TT D can be large for wide neural networks. See App. A for details.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

Consider a discounted Markov decision process defined by a tuple $(\mathcal{S},\mathcal{A},{\mathbb{P}},R,\gamma)$, where $\mathcal{S}$ and $\mathcal{A}$ denote the state and action spaces of the agent, ${{\mathbb{P}}{(\left. s^{\prime} \middle| {s,a} \right.)}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{P}{(\mathcal{S})}}}$ is the Markov kernel that determines the transition probability from $(s,a)$ to state $s^{\prime}$, $\gamma \in {}$ is the discount factor, and $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack{- R},R\rbrack}}$ is the reward function of $s$ and $a$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

At each time $t$, the agent executes an action $a_{t} \in \mathcal{A}$ given the current state $s_{t} \in \mathcal{S}$, following a possibly stochastic policy $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$, i.e., $a_{t} \sim \pi{( \cdot |s_{t})}$. Then, given the state-action pair $(s_{t},a_{t})$, the agent observes a reward $r_{t} = {r{(s_{t},a_{t})}}$. Thus, under any policy $\pi$, one can define the *state-action value* function $Q^{\pi}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

In practice, both the state and action spaces $\mathcal{S}$ and $\mathcal{A}$ can be very large. Thus, the policy $\pi$ is usually parametrized as $\pi_{\theta}$ for some parameter $\theta \in {\mathbb{R}}^{d}$, using, for example, deep neural networks. As such, the goal of the agent is to maximize $J{(\pi_{\theta})}$ in the space of the parameter $\theta$, which naturally induces an optimization problem. Such a problem is in general nonconvex, making it challenging to find the globally optimal policy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

For notational convenience, let us denote $J{(\pi_{\theta})}$ by $J{(\theta)}$. Many of the previous works focus on establishing stationary convergence of policy gradient methods. That is, finding a $\theta$ that satisfies

<!-- chunk {"id": "body-0019", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

Obviously, such a $\theta$ may not lead to a large $J{(\theta)}$. Instead, we are interested in finding a $\theta$ such that

<!-- chunk {"id": "body-0020", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

where $J^{\star} = {{\max_{\pi}J}{(\pi)}}$, and the $\mathcal{O}{(\sqrt{\varepsilon_{\text{bias}}})}$ term reflects the inherent error related to the possibly limited expressive power of the policy parametrization $\pi_{\theta}$ (see Assumption 4.4 Policy Gradient and Natural Policy Gradient Methods") for the definition).

<!-- chunk {"id": "body-0021", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

To solve the optimization problem (2.1 Policy Gradient and Natural Policy Gradient Methods")), one standard way is via the policy gradient (PG) method. Specifically, let $\tau_{i} = {\{ s_{0}^{i},a_{0}^{i},s_{1}^{i},\cdots\}}$ denote the data of a sampled trajectory under policy $\pi_{\theta}$. Then, a stochastic PG ascent update is given as

<!-- chunk {"id": "body-0022", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

where $\eta > 0$ is a stepsize, $N$ is the number of trajectories, and $g{(\left. \tau_{i} \middle| \theta^{k} \right.)}$ estimates ${\nabla J}{(\theta^{k})}$ using the trajectory $\tau_{i}$. Common unbiased estimators of PG include REINFORCE, using the policy gradient theorem, and GPOMDP. The commonly used GPOMDP estimator will be given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

where ${{\nabla_{\theta}\log}\pi_{\theta}}{(\left. a_{t}^{i} \middle| s_{t}^{i} \right.)}$ is the *score function*. If the expectation of this infinite sum exits, then (2.5 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")) becomes an unbiased estimate of the policy gradient of the objective $J{(\theta)}$ defined in (2.1 Policy Gradient and Natural Policy Gradient Methods")). This unbiasedness is established in App. B Policy Gradient and Natural Policy Gradient Methods") for completeness.

<!-- chunk {"id": "body-0024", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

In practice, a *truncated* version of GPOMDP is used to approximate the infinite sum in (2.5 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")), as

<!-- chunk {"id": "body-0025", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

where $\tau_{i}^{H} = {\{ s_{0}^{i},a_{0}^{i},s_{1}^{i},\cdots,s_{H - 1}^{i},a_{H - 1}^{i},s_{H}^{i}\}}$ is a truncation of the full trajectory $\tau_{i}$ of length $H$. (2.6 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")) is thus a biased stochastic estimate of ${\nabla J}{(\theta)}$, with the bias being negligible for a large enough $H$. For notational simplicity, we denote the $H$-horizon trajectory distribution induced by the initial state distribution $\rho$ and policy $\pi_{\theta}$ as $p_{\rho}^{H}{( \cdot |\theta)}$, that is,

<!-- chunk {"id": "body-0026", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

Hereafter, unless otherwise stated, we refer to this *$H$-horizon trajectory* simply as *trajectory*, drawn from $p_{\rho}^{H}{( \cdot |\theta)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

As a significant variant of PG, NPG also incorporates a preconditioning matrix $F_{\rho}{(\theta)}$, leading to the following update

<!-- chunk {"id": "body-0028", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

The NPG update (2.7 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")) can also be written as

<!-- chunk {"id": "body-0029", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

where $L_{\nu_{\rho}^{\pi_{\theta}}}{(w;\theta)}$ is the compatible function approximation error defined by

<!-- chunk {"id": "body-0030", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

For convenience, we will denote $\nu_{\rho}^{\pi_{\theta}}$ by $\nu^{\pi_{\theta}}$ hereafter. In other words, the NPG update direction $w^{k}$ is given by the minimizer of a stochastic optimization problem. In practice, one obtains an approximate NPG update direction $w^{k}$ by SGD (see Procedure 1 Policy Gradient and Natural Policy Gradient Methods")).

<!-- chunk {"id": "body-0031", "role": "body", "section": "(Natural) Policy Gradient Methods", "weight": 1.0} -->

Regarding the NPG update (2.8 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")), we make the following standing assumption on the Fisher information matrix induced by $\pi_{\theta}$ and $\rho$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

For all $\theta \in {\mathbb{R}}^{d}$, the Fisher information matrix induced by policy $\pi_{\theta}$ and initial state distribution $\rho$ satisfies

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

Assumption 2.1 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods") essentially states that $F_{\rho}{(\theta)}$ behaves well as a preconditioner in the NPG update (2.8 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")). This is a common (and minimal) requirement for the convergence of preconditioned algorithms in both convex and nonconvex settings in the optimization realm, for example, the quasi-Newton algorithms, and their stochastic variants.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

In the RL realm, one common example of policy parametrizations that can satisfy this assumption is the Gaussian policy, where $\pi_{\theta}{( \cdot |s)} = \mathcal{N}{(\mu_{\theta}{(s)},\Sigma)}$ with mean parametrized linearly as ${\mu_{\theta}{(s)}} = {\phi{(s)}^{\top}\theta}$, where $\phi{(s)}$ denotes some feature matrix of proper dimensions, $\theta$ is the coefficient vector, and $\Sigma \succ 0$ is some fixed covariance matrix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

In this case, the Fisher information matrix at each $s$ becomes $\phi{(s)}\Sigma^{- 1}\phi{(s)}^{\top}$, independent of $\theta$, and is uniformly lower bounded (positive definite sense) if $\phi{(s)}$ is full-row-rank, namely, the features expanded by $\theta$ are linearly independent, which is a common requirement for linear function approximation settings. See App. B.2 ‣ Appendix B Helper Lemmas ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods") for more detailed justifications, as well as discussions on more general policy parametrizations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

In the pioneering NPG work, $F{(\theta)}$ is directly assumed to be positive definite. So is in the follow-up works on natural actor-critic algorithms. In fact, this way, $F{(\theta)}$ will define a valid Riemannian metric on the parameter space, which has been used for interpreting the desired convergence properties of natural gradient methods. In a recent version of, a relevant assumption (specifically, Assumption 6.5, item 3) is made to establish the global convergence of NPG, in which it is assumed that $\lambda_{\text{min}}{({F_{\rho}{(\theta)}})}$ is not too small compared with the Fisher information matrix induced by a fixed comparator policy. this can be implied by our Assumption 2.1 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods"). To sum up, the positive definiteness on the Fisher preconditioning matrix is common and not very restrictive.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

In Sec. 4 Policy Gradient and Natural Policy Gradient Methods"), we shall see that under Assumption 2.1 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods"), the stationary convergence of NPG can be analyzed, and NPG enjoys a better sample complexity of $\mathcal{O}{(\varepsilon^{- 3})}$ in terms of its global convergence, compared with the existing sample complexity of $\mathcal{O}{(\varepsilon^{- 4})}$. In addition, interestingly, PG and its variance-reduced version SRVR-PG also enjoy global convergence, although the Fisher information matrix does not appear explicitly in their updates.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Variance-Reduced Policy Gradient Methods", "weight": 1.0} -->

Recently, proposes an algorithm called Stochastic Recursive Variance Reduced Policy Gradient (SRVR-PG, see Algorithm 2 Policy Gradient and Natural Policy Gradient Methods")), which applies variance-reduction on PG. It achieves a sample complexity of $\mathcal{O}{(\varepsilon^{- 1.5})}$ to find an $\varepsilon -$stationary point, compared with the $\mathcal{O}{(\varepsilon^{- 2})}$ sample complexity of stochastic PG. However, it remains unclear whether SRVR-PG converges globally. In this work, we provide an affirmative answer to this question by showing that SRVR-PG has a sample complexity of $\mathcal{O}{(\varepsilon^{- 3})}$ to find an $\varepsilon -$optimal policy, up to some compatible function approximation error due to policy parametrization.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Variance-Reduced Policy Gradient Methods", "weight": 1.0} -->

We also propose a new algorithm called SRVR-NPG to incorporate variance reduction into NPG, which is described in Algorithm 1 Policy Gradient and Natural Policy Gradient Methods"). In Sec. 4 Policy Gradient and Natural Policy Gradient Methods"), we provide a sample complexity for its global convergence, which is comparable to our improved NPG result.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Variance-Reduced Policy Gradient Methods", "weight": 1.0} -->

\tau_{j}^{H} \middle| \theta_{t}^{j + 1} \right.)}} - {g_{w}{(\left. \tau_{j}^{H} \middle| \theta_{t - 1}^{j + 1} \right.)}}} \right)}}}$;
9: wtj + 1 = SRVR-NPG-SGD (νπθtj + 1,πθtj + 1,utj + 1); ⊳ wtj + 1 ≈ wt, ⋆j + 1 = Fρ−1 (θtj + 1) utj + 1;
13:return θout chosen uniformly from {θ}j = 1, …, S; t = 0, …, m − 1. Algorithm 1 Stochastic Recursive Variance Reduced Natural Policy Gradient (SRVR-NPG)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Variance-Reduced Policy Gradient Methods", "weight": 1.0} -->

In line 8 of Algorithm 1 Policy Gradient and Natural Policy Gradient Methods"), $g_{w}{(\left. \tau_{j}^{H} \middle| \theta_{t - 1}^{j + 1} \right.)}$ is a weighted gradient estimator given by

<!-- chunk {"id": "body-0042", "role": "body", "section": "Variance-Reduced Policy Gradient Methods", "weight": 1.0} -->

In lines 4 and 8 of Algorithm 1 Policy Gradient and Natural Policy Gradient Methods"), $w_{t}^{j + 1}$ is produced by SRVR-NPG-SGD (see Procedure 2 Policy Gradient and Natural Policy Gradient Methods")), which applies SGD^11^1Following, we apply SGD to make a fair comparison. One can also apply the SA algorithm and AC-SA algorithm.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Variance-Reduced Policy Gradient Methods", "weight": 1.0} -->

where $\nu_{t}^{j + 1}$ is the state-action visitation measure induced by $\pi_{\theta_{t}^{j + 1}}$. The exact update direction given by (3.3 Policy Gradient and Natural Policy Gradient Methods")) is $F_{\rho}^{- 1}{(\theta_{t}^{j + 1})}u_{t}^{j + 1}$, and as in NPG, $F_{\rho}{(\theta_{t}^{j + 1})}$ also serves as a preconditioner.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

Before presenting the global convergence results, we first introduce some standard assumptions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The truncated GPOMDP estimator $g{(\left. \tau^{H} \middle| \theta \right.)}$ defined in (2.6 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")) satisfies $\text{Var}\left( g{(\tau^{H}|\theta)} \right) ≔ \mathbb{E}{\lbrack \parallel g{(\tau^{H}|\theta)} - \mathbb{E}{\lbrack g{(\tau^{H}|\theta)}\rbrack} \parallel^{2}\rbrack} \leq \sigma^{2}$ for any $\theta$ and $\tau^{H} \sim p_{\rho}^{H}{( \cdot |\theta)}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 4.3", "weight": 1.0} -->

For the importance weight $w_{0:h}{(\left. \tau^{H} \middle| {\theta_{1},\theta_{2}} \right.)}$ (3.2 Policy Gradient and Natural Policy Gradient Methods")), there exists $W > 0$ such that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 4.3", "weight": 1.0} -->

Assumptions 4.1 Policy Gradient and Natural Policy Gradient Methods"), 4.2 Policy Gradient and Natural Policy Gradient Methods") and 4.3 Policy Gradient and Natural Policy Gradient Methods") are standard in the analysis of PG methods and their variance reduced variants. They can be verified for simple policy parametrizations such as Gaussian policies; see for more justifications.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 4.3", "weight": 1.0} -->

Following the Assumption 6.5 of, we assume that the policy parametrization $\pi_{\theta}$ achieves a good function approximation, as measured by the transferred compatible function approximation error.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 4.4", "weight": 1.0} -->

For any $\theta \in {\mathbb{R}}^{d}$, the transferred compatible function approximation error satisfies

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 4.4", "weight": 1.0} -->

$\varepsilon_{\text{bias}}$ reflects the error when approximating the advantage function from the score function, it measures the capacity of the parametrization $\pi_{\theta}$. When $\pi_{\theta}$ is the softmax parametrization, we have $\varepsilon_{\text{bias}} = 0$. When $\pi_{\theta}$ is a restricted parametrization, $\varepsilon_{\text{bias}}$ is often positive as $\pi_{\theta}$ may not contain all stochastic policies. For rich neural parametrizations, $\varepsilon_{\text{bias}}$ is very small.

<!-- chunk {"id": "body-0051", "role": "body", "section": "General Framework for Global Convergence", "weight": 1.0} -->

Inspired by the global convergence analysis of NPG, we present a general framework that relates the global convergence rates of these algorithms to i) their stationary convergence rate on $J{(\theta)}$, and ii) the difference between their update directions and exact NPG update directions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Global Convergence Results", "weight": 1.0} -->

By applying Proposition 4.5 Policy Gradient and Natural Policy Gradient Methods") on the PG, NPG, SRVR-PG, and SRVR-NPG updates and analyzing their stationary convergence, we obtain their global convergence rates. In the following, we only keep the dependences on $\sigma^{2}$ (the variance of the gradient estimator), $W$ (variance of importance weight), $\frac{1}{1 - \gamma}$ (the effective horizon) and $\varepsilon$ (target accuracy). The specific choice of the parameters and sample complexities, as well as the proof, can be found in the appendix.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4.7", "weight": 1.0} -->

$L_{J} = \frac{MR}{{({1 - \gamma})}^{2}}$ is the Lipschitz constant of $\nabla J$, see Lemma B.1 Policy Gradient and Natural Policy Gradient Methods") for details.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

Theorem 4.6 Policy Gradient and Natural Policy Gradient Methods") improves the result of \[1, Thm. 6.11\] from (impractical) full gradients to sample-based stochastic gradients.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 4.10", "weight": 1.0} -->

Compared with \[1, Coro. 6.10\], Theorem 4.9 Policy Gradient and Natural Policy Gradient Methods") improves the sample complexity of NPG by $\mathcal{O}{(\varepsilon^{- 1})}$. This is because our stationary convergence analysis on NPG allows for a constant stepsize $\eta$, while \[1, Coro. 6.10\] applies a stepsize of $\eta = {\mathcal{O}{({1/\sqrt{K}})}}$. It is worth noting that the $\mathcal{O}{(\sqrt{\varepsilon_{\text{bias}}})}$ term is the same as, and we also apply the average SGD to solve the NPG subproblem (2.8 Policy Gradient Methods ‣ 2 Preliminaries ‣ An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods")).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 4.12", "weight": 1.0} -->

Theorem 4.11 Policy Gradient and Natural Policy Gradient Methods") establishes the global convergence of SRVR-PG proposed, where only stationary convergence is shown. Also, compared with stochastic PG, SRVR-PG enjoys a better sample complexity thanks to its faster stationary convergence.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 4.14", "weight": 1.0} -->

Compared with SRVR-PG, our SRVR-NPG has a better dependence on $W$ and $\sigma^{2}$, which could be large in practice (especially $W$). The current sample complexity of SRVR-NPG is not better than our (improved) result of NPG since, in our analysis, the advantage of variance reduction is offset by the cost of solving the subproblems.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we compare the numerical performances of stochastic PG, NPG, SRVR-PG, and SRVR-NPG. Specifically, we test on benchmark reinforcement learning environments Cartpole and Mountain Car. Our implementation is based on the implementation of SRVPG^11^1 and SRVR-PG^22^2 and can be found in the supplementary material.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

For the Cartpole problem, we apply a neural network of size $32 \times 1$ and a horizon of $H = 100$. In addition, each training algorithm uses $5000$ trajectories in total. For the Mountain Car problem, we apply a neural network of size $64 \times 1$ and take $H = 1000$. $3000$ trajectories are allowed for each algorithm. The numerical performance comparison, as well as the settings of algorithm-specific parameters, can be found in Figures 2 Policy Gradient and Natural Policy Gradient Methods") and 2 Policy Gradient and Natural Policy Gradient Methods"). In App. O Policy Gradient and Natural Policy Gradient Methods"), we provide more implementation details.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this work, we have introduced a framework for analyzing the global convergence of (natural) PG methods and their variance-reduced variants, under the assumption that the Fisher information matrix is positive definite. We have established the sample complexity for the global convergence of stochastic PG and its variance-reduced variant SRVR-PG, and improved the sample complexity of NPG. In addition, we have introduced SRVR-NPG, which incorporates variance-reduction into NPG, and enjoys both global convergence guarantee and an efficient sample complexity. Our improved analysis hinges on exploiting the advantages of previous analyses on (variance reduced) PG and NPG methods, which may be of independent interest, and can be used to design faster variance-reduced NPG methods in the future.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

The results of this paper improves the performance of policy-gradient methods for reinforcement learning, as well as our understanding to the existing methods. Through reinforcement learning, our study will also benefit several research communities such as machine learning and robotics. We do not believe that the results in this work will cause any ethical issue, or put anyone at a disadvantage in our society.
