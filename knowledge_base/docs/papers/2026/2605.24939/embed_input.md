<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Linear Convergence of Entropy-Regularized Softmax Policy Gradient beyond Tabular MDPs

Topics include Policy gradients, Reinforcement learning, Entropy regularization, Function approximation, Convergence analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proves global linear convergence results for entropy-regularized softmax policy gradient beyond tabular MDPs using log-linear policies and realizability assumptions. The paper extends finite-state policy-gradient theory toward continuous state-action settings while tracking the geometry of the policy class.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the global convergence of policy gradient for infinite-horizon entropy-regularized Markov decision processes (MDPs) with continuous state and action spaces. We consider log-linear softmax policies with linear function approximation, which extend the tabular softmax parameterization while retaining a tractable policy class. Under Q-pi-tau realizability for the regularized state-action value function, we first establish a non-uniform Polyak-Łojasiewicz (PŁ) inequality. The non-uniformity arises through degeneracy of constants associated with the policy geometry, namely the Fisher information matrix or an uncentered feature covariance matrix. We then identify two feature regimes under which this non-uniform constant can be bounded along the gradient flow. For full-affine-span features, we prove radial unboundedness of the KL regularizer and show that the smallest eigenvalue of the Fisher information matrix remains bounded below by an initialization-dependent positive constant.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For simplex-valued features, we prove an analogous radial unboundedness result in the subspace orthogonal to the all-ones vector and obtain a uniform lower bound for the smallest eigenvalue of the uncentered covariance matrix. These results imply global linear convergence of the regularized objective along the gradient flow, i.e. suboptimality decaying as O(exp(-C t)) for some positive constant C. Our analysis extends the global convergence theory of entropy-regularized softmax policy gradient beyond the tabular setting of Agarwal et al.; Bhandari and Russo; Mei et al..

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overview: The policy gradient is a fundamental concept in reinforcement learning (RL), underpinning policy search and actor-critic methods Sutton et al.. However, for parametrized softmax policies, the normalization factor induces non-convexity in the parameters. As a result, despite the prevalence of softmax policies in RL, their theoretical understanding has remained limited until recently, with existing results confined to the tabular setting Agarwal et al.; Bhandari and Russo; Mei et al..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a discounted infinite horizon Markov decision model $(S,A,P,c,\gamma)$, where $S$ and $A$ are general, possibly continuous, state space and action spaces respectively. Let $\mu$ be the fixed finite reference measure, $\rho$ the distribution of initial state, $P \in {\mathcal{P}{(\left. S \middle| {S \times A} \right.)}}$ the transition probability kernel, $c$ a bounded cost function, and $\gamma \in {\lbrack 0,1)}$ the discount factor. For a given stochastic policy $\pi \in {\mathcal{P}{(\left. A \middle| S \right.)}}$, we define the entropy regularized value function $V_{\tau}^{\pi}:{S\rightarrow{\mathbb{R}}}$ by

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\tau > 0$ determines the intensity of the entropy regularization. For full details on our assumptions and notation, we refer to Section 3.1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two implications of having $\tau > 0$. The first is that the optimal policy satisfies

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $V_{\tau}^{\ast}$ and $Q_{\tau}^{\ast}$ denote the (bounded) optimal value and state-action value functions, respectively. This is an immediate consequence of the Bellman principle (see Theorem 16. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") or Ziebart et al.; Haarnoja et al.; Geist et al. ).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, since the entropy term is strictly convex, its addition in is expected to improve the convergence when optimizing $V_{\tau}^{\pi}{(\rho)}$ over $\pi$ using policy gradient. While the latter point may seem intuitive, the analysis is far from being straightforward even in the tabular case when $S$ and $A$ are finite and direct parametrization

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

with $\theta:{{S \times A}\rightarrow{\mathbb{R}}}$ is employed. Two main difficulties arise: first $\theta \in {\mathbb{R}}^{p}\mapsto{V_{\tau}^{\pi_{\theta}}{(\rho)}}$ is non-convex (see, e.g., Proposition 1 in Mei et al. ), even in the bandit case. Moreover, second, ${\mathcal{P}{(\left. A \middle| S \right.)}} \ni \pi\mapsto{V_{\tau}^{\pi}{(\rho)}}$ is in general non-convex Agarwal et al.; Giegrich et al. even when dynamics are linear and costs convex. Nevertheless, convergence with good rates of policy gradient with softmax policies in the tabular setting has been shown in Mei et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, the suboptimality $V_{0}^{\pi_{\theta_{t}}} - V_{0}^{\ast}$ converges sub-linearly, i.e. $\mathcal{O}{({1/t})}$, while with the additional entropy regularization, the the suboptimality $V_{\tau}^{\pi_{\theta_{t}}} - V_{\tau}^{\ast}$ converges converges linearly, i.e. $\mathcal{O}{(e^{- {Ct}})}$. The key insight in Mei et al., is to use non-uniform Polyak--Łojasiewicz (PŁ) inequality.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This approach becomes computationally intractable as the size of the sets $S$ and $A$ grow large or when $S$ or $A$ are continous. To overcome this one parametrizes the log densities. In this paper we assume the following linear function approximation: given basis functions $g:{{S \times A}\rightarrow}$ ${\mathbb{R}}^{p}$, for all $a \in A$ and $s \in S$, let

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\theta \in {\mathbb{R}}^{p}$. The continuous-time policy gradient is

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The expression for the gradient is given by the well known policy gradient theorem, which we restate for convenience later, in Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outline of the argument to obtain linear convergence: First, we wish to obtain gradient dominance property for the objective in the form of a PŁ inequality. To proceed we assume $Q_{\tau}^{\pi}$-realizability i.e. that for any $\pi$ there exists a unique ${\mathbf{θ}}{(\pi)}$ such that ${\langle{{\mathbf{θ}}{(\pi)}},g\rangle} = {- {\frac{1}{\tau}Q_{\tau}^{\pi}}}$. Under this assumption a simple calculation shows that

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the Fisher Information matrix (FIM) of $\pi_{\theta}$ for fixed $s$ is defined as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Separately, using the KL-sandwich inequality (see Lemma 9. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")) and local Lipschitz continuity of KL (see Lemma 17, which is an extension of the tabular case from ) we get that for some $C_{\tau,\gamma,\theta} > 0$

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is stated fully as Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") below with a complete proof given later. Note that the strength of the gradient dominance is parameter dependent i.e. we only have non-uniform PŁ inequality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neverthless with ${\{\theta_{t}\}}_{t \geq 0}$ given by the gradient flow we have

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, from Grönwall's lemma we immediately get that

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

If we can show that non-uniform term can be lower bounded along the flow, i.e. if we can show that ${\inf_{t}{C^{- 1}\left( \theta_{t} \right)}} > 0$ then this is the required linear convergence rate.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

We notice that if ${\{\theta_{t}\}}_{t \geq 0}$ given by the gradient flow produces policies with uniformly bounded log densities i.e. if ${\sup_{t}{|{\log\frac{d\pi_{\theta_{t}}}{d\mu}}|}_{B_{b}{({S \times A})}}} < \infty$ then the smallest eigenvalue of the FIM will remain bounded away from zero and so we will have ${\inf_{t}{C^{- 1}\left( \theta_{t} \right)}} > 0$. Thus it is enough to show that ${\{\theta_{t}\}}_{t \geq 0}$ is contained in a compact subset of ${\mathbb{R}}^{p}$. We will use Lyapunov function techniques to that end.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

With that in mind, we note that a simple calculation using the chain rule yields value improvement along the gradient flow, namely ${{\frac{d}{dt}V_{\tau}^{\pi_{\theta_{t}}}{(\rho)}} = {- {\|{{\nabla_{\theta}V_{\tau}^{\pi_{\theta}}}{(\rho)}}\|}_{2}^{2}} \leq 0}.$ The value function $\theta\mapsto{V_{\tau}^{\pi_{\theta_{t}}}{(\rho)}}$ can then be used as a Lyapunov function as long as it is radially unbounded. Since the cost itself is bounded the radial unboundedness can only come as a consequence of the KL term. Example 3. ‣ Example of a feature basis not providing radial unboundedness ‣ 2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), which uses the hat functions as a basis (P1 finite elements) shows that not every reasonable feature basis leads to a radially unbounded KL term. Howevever we identify conditions on the feature basis which ensure radial unboundedness i.e. that ${{KL}{(\left. \pi_{\theta} \middle| \mu \right.)}}\rightarrow\infty$ whenever ${\|\theta\|}_{2}\rightarrow\infty$. In Example 1. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") we show that the Fourier basis satisfies our Assumption 2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Additionally, in the case of simplex features (see Assumption 4) below we can extend the PŁ inequality by replacing the FIM with a version built using uncentred features which allows us to carry out a similar convergence argument but capturing further types of basis functions, e.g. the Bernstein polynomials, see Example 2. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our setting, with general log-linear policies, their way to formulate the property that the gradient of the value function summed up over $a$ is $0$ along the flow cannot be employed. Even though with simplex features we have ${\sum_{i}{{\nabla_{\theta_{i}}V_{\tau}^{\pi_{\theta_{t}}}}{(\rho)}}} = 0$ for all $t$, weights $\theta$ impact the entire conditional log-density and thus we cannot hope to derive a lower bound for the action density at a given state since this separation is not available. Thus, a fundamentally different approach has to be used. On the other hand, in the tabular setting, one cannot expect radial unboundedness of the KL divergence as this term will be finite any $\mu$ s.t. ${\mu{(a)}} > 0$ for all $a$. Thus the use of the KL divergence as a Lyapunov function is novel and our results complement those of Mei et al..

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

Literature review: There is a tremendous amount of research literature on convergence RL methods, which underscores its importance. Here we focus on the subset of the RL literature that we think is most related to our work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Introduction", "weight": 1.5} -->

Entropy-regularized RL has demonstrated both good algorithmic performance and desirable theoretical properties Haarnoja et al.; Geist et al.; Vieillard et al.; Neu et al.; Fox et al.; Ziebart et al.. It has been shown that the softmax policies are optimal in the entropy regularized setting.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Introduction", "weight": 1.5} -->

For policy gradient in tabular setting, the work of Agarwal et al. initiated a global analysis in discounted MDPs under tabular setting and compatible function approximation parameterizations, making explicit the roles of distribution mismatch, approximation error, and statistical error; in the tabular softmax case this gives a sublinear convergence guarantee for vanilla policy gradient. The work of Mei et al. subsequently gave a sharper analysis of tabular softmax policy gradient with direct parametrization as discussed above. These guarantees are complemented by worse case analysis for the policy gradient methods in Agarwal et al.; Mei et al. and show that standard softmax policy gradient the constants in the convergence rate suffer from exponential dependence on state-space and horizon sizes Li et al.. Moving beyond the realizability assumption Lin et al. derive some ordering conditions in the bandit case (empty state space) which guarantee the convergence of softmax policy gradient using linear function approximation. However as of now it is unclear how this applies to MDPs and also fundamentally depends on the finite cardinality of the action space.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although MDPs with continuous state and action spaces are widely used in practical applications Doya; Van Hasselt; Manna et al., the convergence analysis of policy gradient methods in this setting remains less developed compared to its discrete counterparts. Most existing works have focused on discrete-time linear quadratic regulator (LQR) problems with linear parameterized policies. The linear-quadratic structure leads to the PŁ inequality Polyak and others; Lojasiewicz; Kurdyka with a uniform constant and we've seen above how this then gives linear convergence Fazel et al.; Bu et al.; Hu et al.. These results have been extended to continuous-time LQR systems Sontag; Giegrich et al..

<!-- chunk {"id": "body-0032", "role": "body", "section": "Introduction", "weight": 1.5} -->

One may choose to use the inverse of the integrated FIM as a pre-conditioner in the gradient flow which gives rise to the natural policy gradient (NPG). For NPG under with log-linear policies Cayci et al. prove linear convergence of the NPG in the entropy regularized setting. Moreover for log-linear policies the NPG is in fact identical to mirror descent (MD) (in the sense of producing the same policy updates) and MD is known to converge linearly for entropy regularized MDPs Lan; Ju and Lan; Kerimkulov et al.. It is perhaps interesting to note that unlike policy gradient, MD / NPG automatically ensure that log densities remain bounded along the optimization and thus the FIM is invertible almost regardless of the feature basis (one cannot have linearly dependent features). This is a consequnce of the policy improvement of NPG / MD under exact evaluations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Introduction", "weight": 1.5} -->

A linear convergence rate is proved in Liu et al. under an additional PŁ inequality for the continuous-time Fisher--Rao flow on the space of measures. Continuous-time Fisher--Rao flows in the entropy regularized MDPs has been studied by Kerimkulov et al., where the linear convergence to the optimal policy has been established and the insights into the natural policy gradient flow with linear function approximation was given.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Introduction", "weight": 1.5} -->

Main contributions of this paper: We prove that under suitable conditions on the features and under $Q_{\tau}^{\pi}$-realizability the policy gradient for the KL-regularized MDP on general state and action spaces with exact evaluations converges linearly.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prove a non-uniform PŁ inequality in this setting, see Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Introduction", "weight": 1.5} -->

Establish conditions on the feature basis under which the KL divergence is radially unbounded and hence Lyapunov function techniques can be used to obtain a bound on the non-uniform constant, see Theorems 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). This is of independent interest to anyone analysing algorithms that employ log-linear densities and KL regularization as it opens up Lyapunov function techniques to them.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Introduction", "weight": 1.5} -->

Obtain the desired linear convergence, see Theorems 4. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and 7. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

<!-- chunk {"id": "body-0038", "role": "body", "section": "Introduction", "weight": 1.5} -->

Provide examples of basis functions which satisfy the conditions, see Examples 1. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and 2. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

Let $S$ and $A$ be Polish spaces with $A$ compact. Let $P \in {\mathcal{P}{(\left. S \middle| {S \times A} \right.)}}$. Let $\gamma \in {\lbrack 0,1)}$ be the discount factor. Let $c \in {B_{b}{({S \times A})}}$ be the cost function and we will assume, without loss of generality, that ${|c|}_{B_{b}{({S \times A})}} \leq 1$. Let $\tau > 0$. Let $\mu \in {\mathcal{P}{(A)}}$ have full support on $A$ and be absolutely continuous w.r.t. the Lebesgue measure. The seven-tuple $(S,A,P,c,\gamma,\tau,\mu)$ determines a $\gamma$-discounted infinite horizon $\tau$-entropy regularized Markov decision process model.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

The aim is to minimize ${P{(\left. A \middle| S \right.)}} \ni \pi\mapsto{V_{\tau}^{\pi}{(\rho)}}$. Due to the Bellman principle, Theorem 16. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") for convenience in Section 3.5 or Ziebart et al.; Haarnoja et al.; Geist et al., we know that the optimal policy is of the form and the optimal value (and state value) functions are bounded. Hence, without loss of generality we may restrict our minimization problem to softmax policies from the class

<!-- chunk {"id": "body-0041", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

Moreover one can see that this has the stochastic representation

<!-- chunk {"id": "body-0042", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

For a given fixed initial distribution $\rho \in {\mathcal{P}{(S)}}$, we define

<!-- chunk {"id": "body-0043", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

When $S$ or $A$ are not of finite cardinality the minimization over the class 9 is intractable. Thus, instead of looking for the optimal policy in 9, we parametrize the softmax policies using linear function approximation. To that end let $g:{{A \times S}\rightarrow}$ ${\mathbb{R}}^{p}$ be our basis functions (or features). We will take $g$ to be measurable and such that ${\sum_{i = 1}^{p}{|g_{i}|}_{B_{b}{({S \times A})}}^{2}} \leq 1$. Now given parameters $\theta \in {\mathbb{R}}^{p}$ consider parametrized policies of the form

<!-- chunk {"id": "body-0044", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

Thus we wish to solve the minimization problem

<!-- chunk {"id": "body-0045", "role": "body", "section": "Formulation and the statement of the main results", "weight": 1.0} -->

We will work under the $Q_{\tau}^{\pi}$-realizability assumption.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 1 ($Q_{\\tau}^{\\pi}$-realizability)", "weight": 1.0} -->

Recall that due to the Bellman principle the optimal state-action value function $Q_{\tau}^{\ast} = Q_{\tau}^{\pi_{\tau}^{\ast}} \in {B_{b}{({S \times A})}}$ with $\pi^{\ast} \in \Pi_{\mu}$. Let $\theta^{\ast}$ such that ${\langle\theta^{\ast},g\rangle} = {- {\frac{1}{\tau}Q_{\tau}^{\ast}}}$ which exists and is unique due to Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). Since the optimal $\pi^{\ast} \in \Pi_{\mu}$ is of the form, we have

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 1 ($Q_{\\tau}^{\\pi}$-realizability)", "weight": 1.0} -->

The remainder of the paper is devoted to the argument that under suitable assumptions on the features the gradient flow converges linearly in the sense that $0 \leq {{V_{\tau}^{\pi_{\theta}}{(\rho)}} - {V_{\tau}^{\pi_{\theta}^{\ast}}{(\rho)}}} \leq {\mathcal{O}{(e^{- {Ct}})}}$. Recall that we will do this by first obtaining a non-uniform PŁ inequality and then demonstrating that along the gradient flow we in fact can bound the constant uniformly, using radial unboundedness of $\theta\mapsto{{KL}{(\left. \pi_{\theta} \middle| \mu \right.)}}$ which holds for suitable feature basis.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We see that Assumption 2 implies 1. in Lemma 15. ‣ 3.3.2. Proof of Theorem 2 ‣ 3.3. Proof of the main results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). Thus $g{(s,A)}$ has full affine dimension. We will work under Assumption 2 as it will be needed later to get the radial unboundedness of $\theta\mapsto{{KL}{(\left. \pi_{\theta} \middle| \mu \right.)}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 1 (Trigonometric features)", "weight": 1.0} -->

The features have no action-constant Fourier mode. We assume that the action-frequency has been chosen without redundant modes, so that for every fixed $s \in S$, $\theta \neq 0$ implies that the map $a\mapsto{f_{\theta}{(s,a)}}$ is not identically zero.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simplex features", "weight": 1.0} -->

Assumption 4 explains what we mean by simplex features and adds an additional property which allow us to get unboundedness of $\theta\mapsto{{KL}{(\left. \pi_{\theta} \middle| \mu \right.)}}$ in the direction orthogonal to the $\mathbf{1}$-vector. Recall that for any $v \in {\mathbb{R}}^{p}$ we write $v_{\perp}:={v - {p^{- 1}{\langle v,\mathbf{1}\rangle}\mathbf{1}}}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Note the assumption on the measure of the maximizer set of $u^{\top}g{(s,a)}$ is a little different between Assumption 4 and Assumption 2 in that we consider different vectors $u$ in each.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example of a feature basis not providing radial unboundedness", "weight": 1.0} -->

In bandit setting, where the MDP has a single state, we have the following example using simplex features that do not give radial unboundedness of $KL$ term in the subspace orthogonal to $\mathbf{1}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 3 (Hat-functions do not give radial unboundedness in the subspace )", "weight": 1.0} -->

The detailed calculation can be found in Section 3.4.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Basic notations and definitions", "weight": 1.0} -->

Let $(E,d)$ denote a complete separable metric space (i.e. a Polish space). For a given measure $\rho$ in $E$, denote by $L^{p}{(E,\rho)}$, $p \in {\lbrack 1,\infty\rbrack}$, for Lebesgue spaces of integrable functions. We always equip a Polish space with its Borel sigma-field ${\mathcal{B}{(E)}}.$ Denote by $B_{b}{(E)}$ the space of bounded strongly measurable functions $f:{E\rightarrow{\mathbb{R}}}$ endowed with the supremum norm ${|f|}_{B_{b}{(E)}} = {\sup_{x \in E}{|{f{(x)}}|}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Basic notations and definitions", "weight": 1.0} -->

For ${\mu,\mu^{\prime}} \in {\mathcal{P}{(E)}}$ such that $\mu$ is absolutely continuous with respect to $\mu^{\prime}$, the relative entropy of $\mu$ with respect to $\mu^{\prime}$ (or KL divergence of $\mu$ relative to $\mu^{\prime}$) is defined by

<!-- chunk {"id": "body-0056", "role": "body", "section": "Basic notations and definitions", "weight": 1.0} -->

respectively. Moreover, by Exercise 2.3 and Proposition 3.1 in Kunze, we have

<!-- chunk {"id": "body-0057", "role": "body", "section": "Basic notations and definitions", "weight": 1.0} -->

where the latter are operator norms. Thus, $b\mathcal{K}{(\left. E \middle| E \right.)}$ is a Banach algebra with the product defined via composition of the corresponding linear operators; in particular, for a given $k \in {b\mathcal{K}{(\left. E \middle| E \right.)}}$,

<!-- chunk {"id": "body-0058", "role": "body", "section": "Basic results on entropy regularized MDPs", "weight": 1.0} -->

The following lemma (see e.g., Lemma 2.3 Kerimkulov et al. ) is crucial for addressing this non-convexity issue.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Proofs of Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs\")", "weight": 1.0} -->

Let us restate Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") in its full version.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Proofs of Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs\")", "weight": 1.0} -->

Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). Let Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") hold. Let $R \geq {|{\log\frac{d\pi_{\theta^{\ast}}}{d\mu}}|}_{B_{b}{({S \times A})}}$. Let

<!-- chunk {"id": "body-0061", "role": "body", "section": "Example 4 (Hat function features)", "weight": 1.0} -->

Let $x_{0} < x_{1} < \cdots < x_{N}$, and consider the standard one-dimensional finite-element hat functions

<!-- chunk {"id": "body-0062", "role": "body", "section": "Example 4 (Hat function features)", "weight": 1.0} -->

together with the boundary functions

<!-- chunk {"id": "body-0063", "role": "body", "section": "Example 4 (Hat function features)", "weight": 1.0} -->

Dividing the exact formula for $N_{\beta}$ by the exact formula for $Z_{\beta}$, we find

<!-- chunk {"id": "body-0064", "role": "body", "section": "Example 4 (Hat function features)", "weight": 1.0} -->

Since $e^{- {2\beta}}$ is exponentially small, it may be absorbed into any algebraic remainder. Therefore

<!-- chunk {"id": "body-0065", "role": "body", "section": "Example 4 (Hat function features)", "weight": 1.0} -->

Therefore, ${\lim_{\beta\rightarrow\infty}{{KL}{(\left. \pi_{\beta} \middle| \mu \right.)}}} = {\log 3}$. Hence, in this concrete example, the relative entropy remains bounded as $\beta\rightarrow\infty$. Therefore, without Assumption 4, one cannot in general expect radial unboundedness of the KL divergence.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Additional useful results", "weight": 1.0} -->

We introduce the following dynamic programming principle (see Theorem B.1 in Kerimkulov et al. ).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We prove linear convergence of policy gradient for entropy regularized MDPs with log-linear policies on general state and action spaces under $Q_{\tau}^{\pi}$-realizability and when suitable basis functions are employed. This complements existing results for softmax policy gradient methods in the tabular setting Mei et al.. To obtain our results we have established a non-uniform PŁ inequality for general state and action spaces and carried out novel Lyapunov function-based analysis allowing control of the non-uniform term.
