<!-- arxiv-full-text:v1 {"arxiv_id": "2605.24939", "source": "arxiv-html"} -->

## Introduction

Overview: The policy gradient is a fundamental concept in reinforcement learning (RL), underpinning policy search and actor-critic methods Sutton et al.. However, for parametrized softmax policies, the normalization factor induces non-convexity in the parameters. As a result, despite the prevalence of softmax policies in RL, their theoretical understanding has remained limited until recently, with existing results confined to the tabular setting Agarwal et al.; Bhandari and Russo; Mei et al..

We consider a discounted infinite horizon Markov decision model $(S,A,P,c,\gamma)$, where $S$ and $A$ are general, possibly continuous, state space and action spaces respectively. Let $\mu$ be the fixed finite reference measure, $\rho$ the distribution of initial state, $P\in\mathcal{P}(S|S\times A)$ the transition probability kernel, $c$ a bounded cost function, and $\gamma\in[0,1)$ the discount factor. For a given stochastic policy $\pi\in\mathcal{P}(A|S)$, we define the entropy regularized value function $V^{\pi}_{\tau}:S\rightarrow\mathbb{R}$ by where $\tau>0$ determines the intensity of the entropy regularization. For full details on our assumptions and notation, we refer to Section 3.1.

There are two implications of having $\tau>0$. The first is that the optimal policy satisfies where $V_{\tau}^{*}$ and $Q_{\tau}^{*}$ denote the (bounded) optimal value and state-action value functions, respectively. This is an immediate consequence of the Bellman principle (see Theorem 16. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") or Ziebart et al.; Haarnoja et al.; Geist et al.).

Second, since the entropy term is strictly convex, its addition in is expected to improve the convergence when optimizing $V_{\tau}^{\pi}(\rho)$ over $\pi$ using policy gradient. While the latter point may seem intuitive, the analysis is far from being straightforward even in the tabular case when $S$ and $A$ are finite and direct parametrization with $\theta:S\times A\rightarrow\mathbb{R}$ is employed. Two main difficulties arise: first $\theta\in\mathbb{R}^{p}\mapsto V^{\pi_{\theta}}_{\tau}(\rho)$ is non-convex (see, e.g., Proposition 1 in Mei et al.), even in the bandit case. Moreover, second, $\mathcal{P}(A|S)\ni\pi\mapsto V_{\tau}^{\pi}(\rho)$ is in general non-convex Agarwal et al.; Giegrich et al. even when dynamics are linear and costs convex. Nevertheless, convergence with good rates of policy gradient with softmax policies in the tabular setting has been shown in Mei et al.. In general, the suboptimality $V^{\pi_{\theta_{t}}}_{0}-V^{\ast}_{0}$ converges sub-linearly, i.e. $\mathcal{O}(1/t)$, while with the additional entropy regularization, the the suboptimality $V^{\pi_{\theta_{t}}}_{\tau}-V^{\ast}_{\tau}$ converges converges linearly, i.e. $\mathcal{O}(e^{-Ct})$. The key insight in Mei et al., is to use non-uniform Polyak--Łojasiewicz (PŁ) inequality.

This approach becomes computationally intractable as the size of the sets $S$ and $A$ grow large or when $S$ or $A$ are continous. To overcome this one parametrizes the log densities. In this paper we assume the following linear function approximation: given basis functions $g:S\times A\rightarrow$ $\mathbb{R}^{p}$, for all $a\in A$ and $s\in S$, let where $\theta\in\mathbb{R}^{p}$. The continuous-time policy gradient is The expression for the gradient is given by the well known policy gradient theorem, which we restate for convenience later, in Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

Outline of the argument to obtain linear convergence: First, we wish to obtain gradient dominance property for the objective in the form of a PŁ inequality. To proceed we assume $Q^{\pi}_{\tau}$-realizability i.e. that for any $\pi$ there exists a unique $\boldsymbol{{\theta}}(\pi)$ such that $\langle\boldsymbol{{\theta}}(\pi),g\rangle=-\tfrac{1}{\tau}Q^{\pi}_{\tau}$. Under this assumption a simple calculation shows that where the Fisher Information matrix (FIM) of $\pi_{\theta}$ for fixed $s$ is defined as Left multiplying by $(\theta-\boldsymbol{\theta}(\pi_{\theta}))^{\top}$, using that the FIM is positive semi-definite, using the Cauchy--Schwartz inequalty and finally dividing by $\|\theta-\boldsymbol{\theta}(\pi_{\theta})\|_{2}$ we have Separately, using the KL-sandwich inequality (see Lemma 9. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")) and local Lipschitz continuity of KL (see Lemma 17, which is an extension of the tabular case from) we get that for some $C_{\tau,\gamma,\theta}>0$ This, together with show that there is $C:\mathbb{R}^{p}\to(0,\infty)$ s.t. for all $\theta\in\mathbb{R}^{p}$ This is stated fully as Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") below with a complete proof given later. Note that the strength of the gradient dominance is parameter dependent i.e. we only have non-uniform PŁ inequality.

Neverthless with $\{\theta_{t}\}_{t\geq 0}$ given by the gradient flow we have Hence, from Grönwall's lemma we immediately get that If we can show that non-uniform term can be lower bounded along the flow, i.e. if we can show that $\inf_{t}C^{-1}\left(\theta_{t}\right)>0$ then this is the required linear convergence rate.

We notice that if $\{\theta_{t}\}_{t\geq 0}$ given by the gradient flow produces policies with uniformly bounded log densities i.e. if $\sup_{t}|\log\frac{\mathrm{d}\pi_{\theta_{t}}}{\mathrm{d}\mu}|_{B_{b}(S\times A)}<\infty$ then the smallest eigenvalue of the FIM will remain bounded away from zero and so we will have $\inf_{t}C^{-1}\left(\theta_{t}\right)>0$. Thus it is enough to show that $\{\theta_{t}\}_{t\geq 0}$ is contained in a compact subset of $\mathbb{R}^{p}$. We will use Lyapunov function techniques to that end.

With that in mind, we note that a simple calculation using the chain rule yields value improvement along the gradient flow, namely $\frac{d}{dt}V^{\pi_{\theta_{t}}}_{\tau}(\rho)=-\|\nabla_{\theta}V^{\pi_{\theta}}_{\tau}(\rho)\|_{2}^{2}\leq 0\,.$ The value function $\theta\mapsto V^{\pi_{\theta_{t}}}_{\tau}(\rho)$ can then be used as a Lyapunov function as long as it is radially unbounded. Since the cost itself is bounded the radial unboundedness can only come as a consequence of the KL term. Example 3. ‣ Example of a feature basis not providing radial unboundedness ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), which uses the hat functions as a basis (P1 finite elements) shows that not every reasonable feature basis leads to a radially unbounded KL term. Howevever we identify conditions on the feature basis which ensure radial unboundedness i.e. that $\operatorname{KL}(\pi_{\theta}|\mu)\to\infty$ whenever $\|\theta\|_{2}\to\infty$. In Example 1. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") we show that the Fourier basis satisfies our Assumption 2.

Additionally, in the case of simplex features (see Assumption 4) below we can extend the PŁ inequality by replacing the FIM with a version built using uncentred features which allows us to carry out a similar convergence argument but capturing further types of basis functions, e.g. the Bernstein polynomials, see Example 2. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

Key differences with the tabular case: In the tabular case when $\tau>0$ Mei et al. prove PŁ inequality with $C(\theta)=C\min_{s,a}\pi_{\theta_{t}}(a|s)$ with $C$ independent of $\theta$. Their methods then can be used to show that along the flow it holds that $\sum_{a}\tfrac{\partial V^{\pi_{\theta_{t}}}_{\tau}(\rho)}{\partial\theta_{t}(s,a)}=0$ for all $t$. From this they then derive $\inf_{t}\min_{a}\pi_{\theta_{t}}(a)>0$ which, as we've seen, leads to linear convergence.

In our setting, with general log-linear policies, their way to formulate the property that the gradient of the value function summed up over $a$ is $0$ along the flow cannot be employed. Even though with simplex features we have $\sum_{i}\nabla_{\theta_{i}}V^{\pi_{\theta_{t}}}_{\tau}(\rho)=0$ for all $t$, weights $\theta$ impact the entire conditional log-density and thus we cannot hope to derive a lower bound for the action density at a given state since this separation is not available. Thus, a fundamentally different approach has to be used. On the other hand, in the tabular setting, one cannot expect radial unboundedness of the KL divergence as this term will be finite any $\mu$ s.t. $\mu(a)>0$ for all $a$. Thus the use of the KL divergence as a Lyapunov function is novel and our results complement those of Mei et al..

Literature review: There is a tremendous amount of research literature on convergence RL methods, which underscores its importance. Here we focus on the subset of the RL literature that we think is most related to our work.

Entropy-regularized RL has demonstrated both good algorithmic performance and desirable theoretical properties Haarnoja et al.; Geist et al.; Vieillard et al.; Neu et al.; Fox et al.; Ziebart et al.. It has been shown that the softmax policies are optimal in the entropy regularized setting.

For policy gradient in tabular setting, the work of Agarwal et al. initiated a global analysis in discounted MDPs under tabular setting and compatible function approximation parameterizations, making explicit the roles of distribution mismatch, approximation error, and statistical error; in the tabular softmax case this gives a sublinear convergence guarantee for vanilla policy gradient. The work of Mei et al. subsequently gave a sharper analysis of tabular softmax policy gradient with direct parametrization as discussed above. These guarantees are complemented by worse case analysis for the policy gradient methods in Agarwal et al.; Mei et al. and show that standard softmax policy gradient the constants in the convergence rate suffer from exponential dependence on state-space and horizon sizes Li et al.. Moving beyond the realizability assumption Lin et al. derive some ordering conditions in the bandit case (empty state space) which guarantee the convergence of softmax policy gradient using linear function approximation. However as of now it is unclear how this applies to MDPs and also fundamentally depends on the finite cardinality of the action space.

Although MDPs with continuous state and action spaces are widely used in practical applications Doya; Van Hasselt; Manna et al., the convergence analysis of policy gradient methods in this setting remains less developed compared to its discrete counterparts. Most existing works have focused on discrete-time linear quadratic regulator (LQR) problems with linear parameterized policies. The linear-quadratic structure leads to the PŁ inequality Polyak and others; Lojasiewicz; Kurdyka with a uniform constant and we've seen above how this then gives linear convergence Fazel et al.; Bu et al.; Hu et al.. These results have been extended to continuous-time LQR systems Sontag; Giegrich et al..

One may choose to use the inverse of the integrated FIM as a pre-conditioner in the gradient flow which gives rise to the natural policy gradient (NPG). For NPG under with log-linear policies Cayci et al. prove linear convergence of the NPG in the entropy regularized setting. Moreover for log-linear policies the NPG is in fact identical to mirror descent (MD) (in the sense of producing the same policy updates) and MD is known to converge linearly for entropy regularized MDPs Lan; Ju and Lan; Kerimkulov et al.. It is perhaps interesting to note that unlike policy gradient, MD / NPG automatically ensure that log densities remain bounded along the optimization and thus the FIM is invertible almost regardless of the feature basis (one cannot have linearly dependent features). This is a consequnce of the policy improvement of NPG / MD under exact evaluations.

A linear convergence rate is proved in Liu et al. under an additional PŁ inequality for the continuous-time Fisher--Rao flow on the space of measures. Continuous-time Fisher--Rao flows in the entropy regularized MDPs has been studied by Kerimkulov et al., where the linear convergence to the optimal policy has been established and the insights into the natural policy gradient flow with linear function approximation was given.

Main contributions of this paper: We prove that under suitable conditions on the features and under $Q^{\pi}_{\tau}$-realizability the policy gradient for the KL-regularized MDP on general state and action spaces with exact evaluations converges linearly. In particular we: Prove a non-uniform PŁ inequality in this setting, see Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

Establish conditions on the feature basis under which the KL divergence is radially unbounded and hence Lyapunov function techniques can be used to obtain a bound on the non-uniform constant, see Theorems 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). This is of independent interest to anyone analysing algorithms that employ log-linear densities and KL regularization as it opens up Lyapunov function techniques to them.

Obtain the desired linear convergence, see Theorems 4. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and 7. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

Provide examples of basis functions which satisfy the conditions, see Examples 1. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and 2. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs").

## Formulation and the statement of the main results

Let $S$ and $A$ be Polish spaces with $A$ compact. Let $P\in\mathcal{P}(S|S\times A)$. Let $\gamma\in[0,1)$ be the discount factor. Let $c\in B_{b}(S\times A)$ be the cost function and we will assume, without loss of generality, that $|c|_{B_{b}(S\times A)}\leq 1$. Let $\tau>0$. Let $\mu\in\mathcal{P}(A)$ have full support on $A$ and be absolutely continuous w.r.t. the Lebesgue measure. The seven-tuple $(S,A,P,c,\gamma,\tau,\mu)$ determines a $\gamma$-discounted infinite horizon $\tau$-entropy regularized Markov decision process model.

For a given randomized Markov policy $\pi\in P(A|S)$, we define the $\tau$-entropy regularized value function $V^{\pi}_{\tau}:S\rightarrow\mathbb{R}\cup\{+\infty\}$ by The aim is to minimize $P(A|S)\ni\pi\mapsto V^{\pi}_{\tau}(\rho)$. Due to the Bellman principle, Theorem 16. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") for convenience in Section 3.5 or Ziebart et al.; Haarnoja et al.; Geist et al., we know that the optimal policy is of the form and the optimal value (and state value) functions are bounded. Hence, without loss of generality we may restrict our minimization problem to softmax policies from the class For a given policy $\pi\in\Pi_{\mu}$, we define the regularized state-action value function $Q^{\pi}_{\tau}\in B_{b}(S\times A)$ by The occupancy kernel $d^{\pi}\in\mathcal{P}(S|S)$ is defined by $d^{\pi}(ds^{\prime}|s)=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}P^{t}_{\pi}(ds^{\prime}|s)\ d^{\pi}_{\rho}(ds)=\int_{S}d^{\pi}(ds|s^{\prime})\rho(ds^{\prime})$ where $P^{0}_{\pi}(ds^{\prime}|s):=\delta_{s}(ds^{\prime})$, $P^{t}_{\pi}$ is understood as a product of kernels, and convergence is understood in $b\mathcal{K}(S|S)$. It is well known that the on policy Bellman equation holds, see e.g., that is Moreover one can see that this has the stochastic representation For a given fixed initial distribution $\rho\in\mathcal{P}(S)$, we define When $S$ or $A$ are not of finite cardinality the minimization over the class 9 is intractable. Thus, instead of looking for the optimal policy in 9, we parametrize the softmax policies using linear function approximation. To that end let $g:A\times S\rightarrow$ $\mathbb{R}^{p}$ be our basis functions (or features). We will take $g$ to be measurable and such that $\sum_{i=1}^{p}|g_{i}|_{B_{b}(S\times A)}^{2}\leq 1$. Now given parameters $\theta\in\mathbb{R}^{p}$ consider parametrized policies of the form Thus we wish to solve the minimization problem We will work under the $Q^{\pi}_{\tau}$-realizability assumption.

### Assumption 1 ($Q^{\pi}_{\tau}$-realizability)

For any $\pi\in\Pi_{\mu}$, there exists a unique $\boldsymbol{\theta}(\pi)$ such that $\langle\boldsymbol{\theta}(\pi),g(s,a)\rangle=-\frac{1}{\tau}Q^{\pi}_{\tau}(s,a)$ for all $s\in S,a\in A$.

An example of when this holds besides the tabular case is linear MDPs (see, e.g., Yang and Wang; Zanette et al.; Li et al.). An MDP is linear if there exists exists $w\in\mathbb{R}^{p}$ and a sequence $\{\psi_{i}\}_{i=1}^{p}$ with $\psi_{i}\in\mathcal{M}(S)$ such that for all $(s,a)\in S\times A$, $c(s,a)=\langle w,g(s,a)\rangle,P(ds^{\prime}\mid s,a)=\sum_{i=1}^{p}g_{i}(s,a)\psi_{i}(ds^{\prime})$. In this case, given $\pi\in\mathcal{P}(A|S)$ we can take $\mathbb{\theta}(\pi)_{i}=-\tfrac{1}{\tau}\big(w_{i}+\gamma\int_{S}V^{\pi}(s^{\prime})\psi_{i}(ds^{\prime})\big)$ so that Recall that due to the Bellman principle the optimal state-action value function $Q^{\ast}_{\tau}=Q^{\pi_{\tau}^{\ast}}_{\tau}\in B_{b}(S\times A)$ with $\pi^{\ast}\in\Pi_{\mu}$. Let $\theta^{*}$ such that $\langle\theta^{*},g\rangle=-\frac{1}{\tau}Q^{*}_{\tau}$ which exists and is unique due to Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). Since the optimal $\pi^{*}\in\Pi_{\mu}$ is of the form, we have In other words, the $Q^{\pi}_{\tau}$-realizability assumption for the KL regularized MDP means that our minimization problem is solvable: $\min_{\theta\in\mathbb{R}^{p}}V_{\tau}^{\pi_{\theta}}(\rho)=V^{*}_{\tau}(\rho)$.

The remainder of the paper is devoted to the argument that under suitable assumptions on the features the gradient flow converges linearly in the sense that $0\leq V_{\tau}^{\pi_{\theta}}(\rho)-V_{\tau}^{\pi_{\theta}^{\ast}}(\rho)\leq\mathcal{O}(e^{-Ct})$. Recall that we will do this by first obtaining a non-uniform PŁ inequality and then demonstrating that along the gradient flow we in fact can bound the constant uniformly, using radial unboundedness of $\theta\mapsto\operatorname{KL}(\pi_{\theta}|\mu)$ which holds for suitable feature basis.

### Theorem 1 (Non-uniform PŁ inequality)

Let Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") hold. Let $R\geq|\log\tfrac{d\pi_{\theta^{\ast}}}{d\mu}|_{B_{b}(S\times A)}$. Let Then for any $\theta\in\Theta_{R}$ there exists $C_{R}(\theta)>0$ such that Depending on the assumptions on the feature basis, this will be proved in Section 3.3.1, where the exact form of the constant $C_{R}(\theta)$ will be given. We now need to work with specific assumptions on the basis functions. Below, we will define "full affine span features" and "simplex features" and discuss how they allow us to prove the linear convergence.

### Full affine span features

We will say that the feature basis $g:S\times A\to\mathbb{R}^{p}$ has full affine dimension if $\operatorname{span}\{g(s,a)-g(s,a^{\prime}):a,a^{\prime}\in A\}=\mathbb{R}^{p}$. Recall that $u\in\mathbb{S}^{p-1}$ if $u\in\mathbb{R}^{p}$ and $\|u\|_{2}=1$.

### Assumption 2

For each fixed $s\in S$, assume that $a\mapsto g(s,a)\in\mathbb{R}^{p}$ is continuous and that, for every $u\in\mathbb{S}^{p-1}$, We see that Assumption 2 implies 1. in Lemma 15. ‣ 3.3.2. Proof of Theorem 2 ‣ 3.3. Proof of the main results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). Thus $g(s,A)$ has full affine dimension. We will work under Assumption 2 as it will be needed later to get the radial unboundedness of $\theta\mapsto\operatorname{KL}(\pi_{\theta}|\mu)$.

### Theorem 2 (Radial unboundedness of KL divergence)

Let Assumption 2 hold. Fix $s\in S$. Then The proof of Theorem 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") can be found in Section 3.3.2.

Theorem 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") combined with classical arguments for constructing ODE solutions with Lyapunov functions will give existence of the solution to the gradient flow.

### Lemma 3 (Existence of solution to the gradient flow using full affine span features)

Let Assumption 2 hold. Then there exists solution $\{\theta_{t}\}_{t\geq 0}$ to. Moreover $\sup_{t\geq 0}\big|\log\tfrac{d\pi_{\theta_{t}}}{d\mu}\big|_{B_{b}(S\times A)}<\infty$.

The proof of Lemma 3. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") can be found in Section 3.3.3.

### Assumption 3

For all $s\in S$, the FIM $G^{\pi_{\theta_{0}}}(s)$ given by is positive definite.

### Theorem 4 (Linear convergence with full affine span features)

Let Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), 2 and 3 hold. Let $\{\theta_{t}\}_{t\geq 0}$ be the solution to gradient flow. Then there exists $C_{\theta_{0}}>0$ such that for $C_{R}(\theta_{t})$ from Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") we have $\sup_{t\geq 0}C_{R}(\theta_{t})\leq C_{\theta_{0}}$ and The the exact form of $C_{\theta_{0}}$ can be found in Section 3.3.4.

To conclude this part, we introduce an example of full affine span features that satisfy Assumption 2.

### Example 1 (Trigonometric features)

Let $S\subset\mathbb{R}^{d_{1}}$ be a compact state set and let $A\subset\mathbb{R}^{d_{2}}$ be a compact action set. Let $\mu$ denote the $d_{2}$-dimensional Lebesgue measure on the action space. Choose a finite set $\mathcal{K}\subset\mathbb{Z}^{d_{2}}\setminus\{\mathbf{0}\}$ of nonzero action frequencies, with no redundant action modes, for example with only one representative from each pair $\{k,-k\}$. For each $k\in\mathcal{K}$, choose a state-frequency vector $\ell_{k}\in\mathbb{R}^{d_{1}}$ and define the trigonometric feature $g(s,a)$ by using the coordinates $\cos(k^{\top}a+\ell_{k}^{\top}s)$ and $\sin(k^{\top}a+\ell_{k}^{\top}s)$ for $k\in\mathcal{K}$. Thus, for $\theta=(\alpha_{k},\beta_{k})_{k\in\mathcal{K}}$, define $f_{\theta}(s,a)=\theta^{\top}g(s,a)=\sum_{k\in\mathcal{K}}\{\alpha_{k}\cos(k^{\top}a+\ell_{k}^{\top}s)+\beta_{k}\sin(k^{\top}a+\ell_{k}^{\top}s)\}$.

The features have no action-constant Fourier mode. We assume that the action-frequency has been chosen without redundant modes, so that for every fixed $s\in S$, $\theta\neq 0$ implies that the map $a\mapsto f_{\theta}(s,a)$ is not identically zero.

For fixed $s$, one has $f_{\theta}(s,a)=\sum_{k\in\mathcal{K}}\{\widetilde{\alpha}_{k}(s)\cos(k^{\top}a)+\widetilde{\beta}_{k}(s)\sin(k^{\top}a)\}$, where $\widetilde{\alpha}_{k}(s)=\alpha_{k}\cos(\ell_{k}^{\top}s)+\beta_{k}\sin(\ell_{k}^{\top}s)$ and $\widetilde{\beta}_{k}(s)=-\alpha_{k}\sin(\ell_{k}^{\top}s)+\beta_{k}\cos(\ell_{k}^{\top}s)$. Moreover, $\widetilde{\alpha}_{k}(s)^{2}+\widetilde{\beta}_{k}(s)^{2}=\alpha_{k}^{2}+\beta_{k}^{2}$. Hence, if $\theta\neq\mathbf{0}$, then for every fixed $s\in S$ at least one pair $(\widetilde{\alpha}_{k}(s),\widetilde{\beta}_{k}(s))$ is nonzero. Since all $k\in\mathcal{K}$ are nonzero action frequencies and there is no redundant action mode, the fixed-state function $a\mapsto f_{\theta}(s,a)$ is a non-constant real-analytic function of $a$.

For fixed $s\in S$, define $M_{\theta}(s):=\max_{a\in A}f_{\theta}(s,a)$ and $\mathcal{A}_{\theta}(s):=\operatorname*{arg\,max}_{a\in A}f_{\theta}(s,a)$. The maximum exists because $A$ is compact and $a\mapsto f_{\theta}(s,a)$ is continuous. Since $a\mapsto f_{\theta}(s,a)-M_{\theta}(s)$ is a nontrivial real-analytic function on an open neighborhood of $A$, the standard zero-set theorem for real-analytic functions implies that its zero set has $d_{2}$-dimensional Lebesgue measure zero. Because $\mathcal{A}_{\theta}(s)=\{a\in A:f_{\theta}(s,a)-M_{\theta}(s)=0\}$, we obtain $\mu(\mathcal{A}_{\theta}(s))=0$ for every fixed $s\in S$ and every nonzero $\theta$.

### Simplex features

Assumption 4 explains what we mean by simplex features and adds an additional property which allow us to get unboundedness of $\theta\mapsto\operatorname{KL}(\pi_{\theta}|\mu)$ in the direction orthogonal to the $\mathbf{1}$-vector. Recall that for any $v\in\mathbb{R}^{p}$ we write $v_{\perp}:=v-p^{-1}\langle v,\mathbf{1}\rangle\mathbf{1}$.

### Assumption 4

The feature basis $g:S\times A\to\mathbb{R}^{p}$ fall in the probability simplex $\Delta_{p-1}$ for every $s$ and $a$, i.e. $\sum_{i=1}^{p}g_{i}(s,a)=1$ and for all $s\in S,a\in A$, $g(s,a)\geq 0$. Moreover, for each fixed $s\in S$, assume that $a\mapsto g(s,a)\in\mathbb{R}^{p}$ is continuous and that, for every $u\in\mathbb{R}^{p}$ such that $u\neq 0$ and $u\perp\mathbf{1}$, Note the assumption on the measure of the maximizer set of $u^{\top}g(s,a)$ is a little different between Assumption 4 and Assumption 2 in that we consider different vectors $u$ in each.

### Theorem 5 (Radial unboundedness of KL divergence in direction orthogonal to $\mathbf{1}$)

Let Assumption 4 hold. Fix $s\in S$. Then The proof of Theorem 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") can be found in Section 3.3.5.

Theorem 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") combined with classical arguments for constructing ODE solutions with Lyapunov functions will give existence of the solution to the gradient flow.

### Lemma 6 (Existence of solution to the gradient flow using simplex features)

Let Assumption 4 hold. Then there exists solution $\{\theta_{t}\}_{t\geq 0}$ to. Moreover, $\sup_{t\geq 0}\big|\log\frac{d\pi_{\theta_{t}}}{d\mu}\big|_{B_{b}(S\times A)}<\infty$.

The proof of Lemma 6. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") can be found in Section 3.3.6.

### Assumption 5

For all $s\in S$, $\int g(s,a)g^{\top}(s,a)\pi_{\theta_{0}}(da|s)$ is positive definite.

### Theorem 7 (Linear convergence rate using simplex features)

Let Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), 4 and 5 hold. Let $\{\theta_{t}\}_{t\geq 0}$ be the solution to gradient flow. Then there exists $C_{\theta_{0}}>0$ such that for $C_{R}(\theta_{t})$ from Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") we have $\sup_{t\geq 0}C_{R}(\theta_{t})\leq C_{\theta_{0}}$ and The the exact form of $C_{\theta_{0}}$ can be found in Section 3.3.7.

To conclude discussing simplex features we provide an example that satisfies Assumption 4.

### Example 2 (Bernstein polynomial features)

Let $S\subset\mathbb{R}^{d_{1}}$ be nonempty and compact, and let $A\subset\mathbb{R}^{d_{2}}$ be compact with nonempty interior. Here, nonempty interior means that there exist $a_{0}\in A$ and $r>0$ such that the open ball $B(a_{0},r)\subset A$. Fix $u\in\mathbb{R}^{d_{2}}\setminus\{\mathbf{0}\}$ and let $q:S\to\mathbb{R}$ be continuous. Define $\widetilde{h}(s,a):=q(s)+u^{\top}a$.

Let $m_{h}:=\min_{(s,a)\in S\times A}\widetilde{h}(s,a)$ and $M_{h}:=\max_{(s,a)\in S\times A}\widetilde{h}(s,a)$. These extrema exist because $S\times A$ is compact and $\widetilde{h}$ is continuous. Moreover, $M_{h}>m_{h}$. Indeed, since $A$ has nonempty interior, there exist $a_{0}\in A$ and $r>0$ such that $B(a_{0},r)\subset A$. Let $v:=u/\|u\|$, and define $a_{+}:=a_{0}+(r/2)v$ and $a_{-}:=a_{0}-(r/2)v$. Then $a_{+},a_{-}\in A$, and for any fixed $s_{0}\in S$, we have $\widetilde{h}(s_{0},a_{+})-\widetilde{h}(s_{0},a_{-})=u^{\top}(a_{+}-a_{-})=r\|u\|>0$. Hence $\widetilde{h}$ is not constant on $S\times A$, so its maximum and minimum are distinct. Define $h:S\times A\to$ by $h(s,a):=(\widetilde{h}(s,a)-m_{h})/(M_{h}-m_{h})$.

Fix $k\geq 1$. For $\ell=0,\dots,k$, define the one-dimensional Bernstein basis function $b_{\ell,k}(w):=\binom{k}{\ell}w^{\ell}(1-w)^{k-\ell}$ for $w\in$. Define the feature $g:S\times A\to\mathbb{R}^{k+1}$ by $g(s,a):=(b_{0,k}(h(s,a)),\dots,b_{k,k}(h(s,a)))^{\top}$. Then $g_{\ell}(s,a)\geq 0$ for every $\ell$, and $\sum_{\ell=0}^{k}g_{\ell}(s,a)=1$ for every $(s,a)\in S\times A$.

For $\theta=(\theta_{0},\dots,\theta_{k})\in\mathbb{R}^{k+1}$, define $f_{\theta}(s,a):=\theta^{\top}g(s,a)=\sum_{\ell=0}^{k}\theta_{\ell}b_{\ell,k}(h(s,a))$. Equivalently, $f_{\theta}(s,a)=P_{\theta}(h(s,a))$, where $P_{\theta}(w):=\sum_{\ell=0}^{k}\theta_{\ell}b_{\ell,k}(w)$.

Assume that $\theta\neq\mathbf{0}$ and $\theta^{\top}\mathbf{1}=\sum_{\ell=0}^{k}\theta_{\ell}=0$. Then $P_{\theta}:\mathbb{[}0,1]\to\mathbb{R}$ is non-constant. To see this, suppose that $P_{\theta}\equiv c$ on $$. Since $\sum_{\ell=0}^{k}b_{\ell,k}(w)=1$, the constant polynomial $c$ satisfies $c=\sum_{\ell=0}^{k}c\,b_{\ell,k}(w)$. By uniqueness of expansion of the Bernstein polynomials, $\theta_{\ell}=c$ for every $\ell=0,\dots,k$. The condition $\theta^{\top}\mathbf{1}=0$ gives $0=\sum_{\ell=0}^{k}\theta_{\ell}=(k+1)c$, so $c=0$, and hence $\theta=\mathbf{0}$, contradicting $\theta\neq\mathbf{0}$. Therefore $P_{\theta}:\mathbb{[}0,1]\to\mathbb{R}$ is non-constant.

For each fixed state $s\in S$, define $M_{\theta}(s):=\max_{a\in A}f_{\theta}(s,a)$ and $\mathcal{A}_{\theta}(s):=\operatorname*{arg\,max}_{a\in A}f_{\theta}(s,a)$. The maximum exists because $A$ is compact and $a\mapsto f_{\theta}(s,a)$ is continuous. Since $P_{\theta}:\mathbb{[}0,1]\to\mathbb{R}$ is a non-constant uni-variate polynomial, $P_{\theta}(w)-M_{\theta}(s)$ is not the zero polynomial. Hence the set $H_{\theta}(s):=\{w\in\mathbb{R}:P_{\theta}(w)=M_{\theta}(s)\}$ is finite.

Now, if $a\in\mathcal{A}_{\theta}(s)$, then $P_{\theta}(h(s,a))=M_{\theta}(s)$, so $h(s,a)\in H_{\theta}(s)$. Therefore $\mathcal{A}_{\theta}(s)\subseteq\bigcup_{w\in H_{\theta}(s)}\{a\in A:h(s,a)=w\}$. For fixed $s$ and $w$, the level set $\{a\in A:h(s,a)=w\}$ is contained in the affine hyperplane $\{a\in\mathbb{R}^{d_{2}}:u^{\top}a=m_{h}+(M_{h}-m_{h})w-q(s)\}$. Since $u\neq\mathbf{0}$, this hyperplane has $d_{2}$-dimensional Lebesgue measure zero. Thus $\mathcal{A}_{\theta}(s)$ is contained in a finite union of measure-zero sets, and hence $\mu(\mathcal{A}_{\theta}(s))=0$.

### Example of a feature basis not providing radial unboundedness

In bandit setting, where the MDP has a single state, we have the following example using simplex features that do not give radial unboundedness of $\operatorname{KL}$ term in the subspace orthogonal to $\mathbf{1}$.

### Example 3 (Hat-functions do not give radial unboundedness in the subspace )

Choose the concrete grid $x_{0}=0,\ x_{1}=\frac{1}{3},\ x_{2}=\frac{2}{3},\ x_{3}=1$, and let $g_{0},g_{1},g_{2},g_{3}$ be the standard one-dimensional finite-element hat functions on the grid $[0,\frac{1}{3}),[\frac{1}{3},\frac{2}{3}),[\frac{2}{3},1]$. Set $g(a):=(g_{0}(a),g_{1}(a),g_{2}(a),g_{3}(a))^{\top}$ and $\theta=(-1,1,1,-1)^{\top}$. Then $\theta^{\top}\mathbf{1}=0$, and the induced function $f_{\theta}(a):=\theta^{\top}g(a)$ is Thus $f_{\theta}$ attains its maximum value $1$ on the whole interval $[\frac{1}{3},\frac{2}{3}]$. Writing $\mathcal{A}_{\theta}:=\operatorname*{arg\,max}_{a\in}f_{\theta}(a)$, we have $\mathcal{A}_{\theta}=[\frac{1}{3},\frac{2}{3}]$ and $\mu(\mathcal{A}_{\theta})=\frac{1}{3}>0$. Hence Assumption 4 fails for this choice of $\theta$.

This also shows that radial unboundedness of the entropy may fail without the zero-measure maximizer assumption. Let $\mu$ be Lebesgue measure restricted to $$. For $\beta>0$, let $\pi_{\beta}$ be the probability measure whose density with respect to $\mu$ is $p_{\beta}(a):=\frac{d\pi_{\beta}}{d\mu}(a)=e^{\beta f_{\theta}(a)}/Z_{\beta}$, where $Z_{\beta}:=\int_{0}^{1}e^{\beta f_{\theta}(a)}\,da$. Since $f_{\theta}$ is linear on the two exterior intervals and equals $1$ on $[\frac{1}{3},\frac{2}{3}]$, the change of variables $y=f_{\theta}(a)$ gives Moreover, we have $\mathbb{E}_{\pi_{\beta}}[f_{\theta}(a)]=\partial_{\beta}\log Z_{\beta}$, and therefore From the exact expression for $Z_{\beta}$, we have $\log Z_{\beta}=\beta-\log 3+\log(1+(1-e^{-2\beta})/\beta)$. Hence, as $\beta\to\infty$, Consequently, $\operatorname{KL}(\pi_{\beta}\mid\mu)=\log 3-\frac{2}{\beta}+\mathcal{O}(\beta^{-2})$, and in particular $\lim_{\beta\to\infty}\operatorname{KL}(\pi_{\beta}\mid\mu)=\log 3$, which is finite.

The detailed calculation can be found in Section 3.4.

## Proofs

### Basic notations and definitions

For matrix $G\in\mathbb{R}^{p\times p}$, denote $\lambda_{\min}(G)$ the smallest eigenvalue value of $G$. Let $\mathbb{S}^{p-1}:=\left\{u\in\mathbb{R}^{p}:\|u\|_{2}=1\right\}.$ Let $\mathbf{1}=(1,1,\dots,1)\in\mathbb{R}^{p}$. For vectors $\mathbf{a},\mathbf{b}\in\mathbb{R}^{p}$, the inner product $\langle\mathbf{a},\mathbf{b}\rangle$ of $\mathbf{a}\ \text{and}\ \mathbf{b}$ is $\mathbf{a}^{\top}\mathbf{b}$. And we use both notations throughout the paper.

Let $(E,d)$ denote a complete separable metric space (i.e. a Polish space). For a given measure $\rho$ in $E$, denote by $L^{p}(E,\rho)$, $p\in[1,\infty]$, for Lebesgue spaces of integrable functions. We always equip a Polish space with its Borel sigma-field $\mathcal{B}(E).$ Denote by $B_{b}(E)$ the space of bounded strongly measurable functions $f:E\rightarrow\mathbb{R}$ endowed with the supremum norm $|f|_{B_{b}(E)}=\sup_{x\in E}|f(x)|$. Denote by $\mathcal{M}(E)$ the Banach space of signed measures (finite) $\mu$ on $E$ endowed with the total variation norm $|\mu|_{\mathcal{M}(A)}=|\mu|(E)$, where $|\mu|$ is the total-variation measure. We note that if $\mu=fd\rho$, where $\rho\in\mathcal{M}_{+}(E)$ is a non-negative measure and $f\in L^{1}(E,\rho)$, then $|\mu|_{\mathcal{M}(E)}=|f|_{L^{1}(E,\rho)}$. We denote by $\mathcal{P}(E)\subset\mathcal{M}(E)$ the convex subset of probability measures on $E$. For $\mu,\mu^{\prime}\in\mathcal{P}(E)$ such that $\mu$ is absolutely continuous with respect to $\mu^{\prime}$, the relative entropy of $\mu$ with respect to $\mu^{\prime}$ (or KL divergence of $\mu$ relative to $\mu^{\prime}$) is defined by It is convenient to have notation for measurable functions $k:E_{1}\rightarrow\mathcal{M}(E_{2})$ for given Polish spaces $(E_{1},d_{1})$ and $(E_{2},d_{2})$. For example, $P:S\rightarrow\mathcal{P}(S\times A)$ will denote a controlled transition probability and $\pi:S\rightarrow\mathcal{P}(A)$ a stochastic policy. Denote by $b\mathcal{K}(E_{1}|E_{2})$ the Banach space of bounded signed kernels $k:E_{2}\rightarrow\mathcal{M}(E_{1})$ endowed with the norm $|k|_{b\mathcal{K}(E_{1}|E_{2})}=\sup_{x\in E_{2}}|k(x)|_{\mathcal{M}(E_{1})}$; that is, $k(U|\cdot):E_{2}\rightarrow\mathbb{R}$ is measurable for all $U\in\mathcal{M}(E_{1})$ and $k(\cdot|x)\in\mathcal{M}(E_{1})$ for all $x\in E_{2}$. For a fixed positive reference measure $\mu\in\mathcal{M}(E_{1})$, we denote by $b\mathcal{K}_{\mu}(E_{1}|E_{2})$ the space of bounded kernels that are absolutely continuous with respect to $\mu$.

Every kernel $k\in b\mathcal{K}(E_{1}|E_{2})$ induces bounded linear operators $T_{k}\in\mathcal{L}(\mathcal{M}(E_{2}),\mathcal{M}(E_{1}))$ and $S_{k}\in\mathcal{L}(B_{b}(E_{1}),B_{b}(E_{2}))$ defined by respectively. Moreover, by Exercise 2.3 and Proposition 3.1 in Kunze, we have where the latter are operator norms. Thus, $b\mathcal{K}(E|E)$ is a Banach algebra with the product defined via composition of the corresponding linear operators; in particular, for a given $k\in b\mathcal{K}(E|E)$, Notice that if $f\in L^{\infty}(E_{1},\mu)$ and $k\in b\mathcal{K}_{\mu}(E_{1}|E_{2})$, then for all $x\in E_{2}$, We denote by $\mathcal{P}(E_{1}|E_{2})$ the convex subspace of $P\in b\mathcal{K}(E_{1}|E_{2})$ such that $P(\cdot|x)\in\mathcal{P}(E_{1})$ for all $x\in E_{2}$; such kernels are referred to as stochastic kernels. A stochastic kernel $P\in\mathcal{P}(E_{1}|E_{2})$ is said to be strongly Feller if $\int_{E_{1}}P(dy|x)f(y)$ is continuous in $x\in E_{2}$ for all $f\in B_{b}(E_{1})$. For a fixed positive reference measure $\mu\in\mathcal{M}(E_{1})$, we denote by $\mathcal{P}_{\mu}(E_{1}|E_{2})$ the space of kernels that are absolutely continuous with respect to $\mu$. A bounded kernel $k\in b\mathcal{K}(E_{1}|E_{2})$ is thus strongly Feller if the range of $S_{k}$ lies in the space of continuous functions on $E_{2}$.

### Basic results on entropy regularized MDPs

The following lemma (see e.g., Lemma 2.3 Kerimkulov et al. ) is crucial for addressing this non-convexity issue.

### Lemma 8 (Performance difference)

For all $\rho\in\mathcal{P}(S)$ and $\pi,\pi^{\prime}\in\Pi_{\mu}$, Define the proximal policy where $Z_{\pi^{\prime}}(s):=\int_{A}\exp\left(-\frac{1}{\tau}\left(Q^{\pi^{\prime}}_{\tau}\left(s,a^{\prime}\right)-V^{\pi^{\prime}}_{\tau}(s)\right)\right)\mu\left(da^{\prime}\right)$. Then we have the following sandwich inequality of sub-optimal gap in terms of KL divergence:

### Lemma 9 (Sandwich Inequality)

Let $\pi_{\bar{\pi}}$ denote the proximal policy step associated with a policy $\bar{\pi}$. Then, for any policies $\pi,\pi^{\prime}$ and any initial distribution $\rho$, Moreover, if $\pi^{*}$ is an optimal policy, then for any policy $\pi^{\prime}$ and any initial distribution $\rho$,

### Proof

The flat derivative of the objective can be written in terms of the proximal policy as By the regularized performance-difference Lemma 8. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), for any $\pi,\pi^{\prime}\in\Pi_{\mu}$ and any $\rho$, Using the expression of the flat derivative, we obtain Minimizing the term inside the integral over $\pi$ for every $s\in S$ and recalling the proximal policy step gives From, for any $\pi,\pi^{\prime}$, Combining and, we get which proves (17. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")).

Finally, the optimality condition for $\pi^{*}$ gives, for all $s\in S,a\in A$, Using this in the regularized performance-difference identity yields Taking $\pi=\pi^{*}$ in and combining with gives (18. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")). ∎

### Lemma 10 (Gradient of log policy)

For any $\theta\in\mathbb{R}^{p}$, $s\in S$, $a\in A$

### Proof

then taking gradient concludes the proof. ∎ In the remainder of the paper, $\nabla$ means $\nabla_{\theta}$ unless stated otherwise.

### Definition 1

For fixed $s$ and for $\theta\in\mathbb{R}^{p}$, the Fisher information matrix (FIM) $G^{\pi_{\theta}}(s)$ is defined as and for $\rho\in\mathcal{P}(S)$,$G^{\pi_{\theta}}(\rho)=\int G^{\pi_{\theta}}(s)d_{\rho}^{\pi_{\theta}}(ds)$.

### Lemma 11

For any $\theta\in\mathbb{R}^{p}$ and any $s\in S$ and $a\in A$,

### Lemma 12 (Smoothness of $\theta\mapsto\nabla\log\frac{d\pi_{\theta}}{d\mu}(a|s)$)

For any $\theta,\theta^{\prime}\in\mathbb{R}^{p}$, then for any $s\in S$ and $a\in A$,

### Proof

where we use Lemma 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") in the third equality. Hence by the bound of $g$, which concludes the proof. ∎

### Lemma 13

For any $\theta\in\mathbb{R}^{p}$, we have

### Proof

By the bound on cost function and Eq., we obtain | \(31\) | | $\displaystyle|V^{\pi_{\theta}}_{\tau}(s)|$ | $\displaystyle=\frac{1}{1-\gamma}\left|\int_{S}\int_{A}\left(c(s^{\prime},a)+\tau\log\frac{d\pi_{\theta}}{d\mu}(a|s)\right)\pi_{\theta}(da|s^{\prime})d^{\pi_{\theta}}(ds^{\prime}|s)\right|$ | | | | | | $\displaystyle\leq\frac{1}{1-\gamma}\left(1+\tau\bigg|\log\frac{d\pi_{\theta}}{d\mu}\bigg|_{B_{b}(S\times A)}\right)\,.$ | | To estimate the state-action value function, by Eq., we have Next we introduce the following Lipschitz continuity of the occupancy kernel (See Lemma A.4 in Leahy et al.).

### Lemma 14

For given $\pi,\pi^{\prime}\in\mathcal{P}(A|S)$, we have

### Corollary 1 (Lipschitz continuity of the occupancy measure in the parameter)

For given $\theta,\theta^{\prime}\in\mathbb{R}^{p}$, we have

### Proof

By Lemma 14, it is enough to show that Let $\theta^{\varepsilon}=\varepsilon\theta^{\prime}+(1-\varepsilon)\theta$, $\varepsilon\in$. Let $s\in S$ and $h\in B_{b}(A)$ be arbitrarily given. Using Lemma 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we find that which results into by Lemma 11 and concludes the proof. ∎ The proof of Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") follows Lemma 2.3 in Leahy et al. and can be found in Section 3.5.1. It verifies that chain rule holds for $\pi\mapsto V^{\pi}_{\tau}$ and $\theta\mapsto\pi_{\theta}$.

### Proposition 1 (Gradient of the Objective)

For any $\theta\in\mathbb{R}^{p}$,

### Proposition 2 (Local Lipschitz Continuity of $\theta\mapsto\nabla V_{\tau}^{\pi_{\theta}}(\rho)$)

Let $R>0$. For any $\theta\in\mathbb{R}^{p}$ such that $\left|\log\frac{d\pi_{\theta}}{d\mu}\right|_{B_{b}(S\times A)}\leq R$, $\theta\mapsto\nabla V_{\tau}^{\pi_{\theta}}(\rho)$ is Lipschitz continuous: where $C_{\gamma,\tau,R}=\left(\frac{1}{1-\gamma}\left(\frac{\gamma(5+\tau R)}{1-\gamma}+6\right)\left(\frac{1+\gamma\tau R}{1-\gamma}+\tau R\right)+\frac{2\tau}{1-\gamma}\right)$.

The proof of Proposition 2). ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") can be found in Section 3.5.2

### Proof of the main results

### Proofs of Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

Let us restate Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") in its full version.

Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"). Let Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") hold. Let $R\geq|\log\frac{d\pi_{\theta^{\ast}}}{d\mu}|_{B_{b}(S\times A)}$. Let Then for any $\theta\in\Theta_{R}$ there exists $C_{R}(\theta)>0$ such that and $\lambda^{\theta}=\bigg[\int_{S}\lambda_{\min}(G^{\pi_{\theta}}(s))d_{\rho}^{\pi_{\theta^{*}}}(ds)\bigg]^{-2}.$ Moreover, if the feature basis $g:S\times A\to\mathbb{R}^{p}$ fall in the probability simplex $\Delta_{p-1}$ for every $s$ and $a$, i.e. $\sum_{i=1}^{p}g_{i}(s,a)=1$ and for all $s\in S,a\in A$, $g(s,a)\geq 0$, then we may replace $\lambda^{\theta}$ in with $\lambda^{\theta}=\left[\int_{S}\lambda_{\min}\left(\int_{A}g(s,a)g^{\top}(s,a)\pi_{\theta}(da|s)\right)d^{\pi_{\theta}}_{\rho}(ds)\right]^{-2}$.

### Proof

Define proximal policy $\bar{\pi}_{\theta}(da|s)\propto\exp\left(-\frac{1}{\tau}Q^{\pi_{\theta}}_{\tau}(s,a)\right)\mu(da)$ as where by Lemma 13, we have Also, from Assumption 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we know there exists $\boldsymbol{\theta}(\pi_{\theta})$ such that $\langle\boldsymbol{\theta}(\pi_{\theta}),g(s,a)\rangle=-\frac{1}{\tau}Q^{\pi_{\theta}}_{\tau}(s,a)$.

Hence by Lemma 9. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and Lemma 17, we have where $\hat{R}=\max\left(\frac{2}{(1-\gamma)\tau}\left(1+\gamma\tau R\right),R\right)$. On the other hand, by Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), where the second and third equality above is due to Lemma 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and the fact that $\int_{A}(g(s,a)-\int_{A}g(s,a^{\prime})\pi_{\theta}(da^{\prime}))\pi_{\theta}(da)=\mathbf{0}$. Left multiplying the above identity by $(\theta-\boldsymbol{\theta}(\pi_{\theta}))^{\top}$, using that the FIM is positive semi-definite, using the Cauchy--Schwartz inequality and finally dividing by $\|\theta-\boldsymbol{\theta}(\pi_{\theta})\|_{2}$ we have Due to and this we get Moreover, note that for any $E\in\mathcal{B}(S)$ and $\pi\in\mathcal{P}(A|S)$, we have Thus we have shown that holds.

If, additionally, we know that the feature basis $g:S\times A\to\mathbb{R}^{p}$ satisfies $\sum_{i=1}^{p}g_{i}(s,a)=1$ and for all $s\in S,a\in A$, $g(s,a)\geq 0$ then we return to to proceed. By Lemma 18, we have where $\hat{R}=\max\left(\frac{2}{(1-\gamma)\tau}\left(1+\gamma\tau R\right),R\right)$. On the other hand,, where the last equality is due to Proposition 4. Hence by Corollary 2, we have where the last inequality is due to.This concludes the second situation. ∎

### Proof of Theorem 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Lemma 15 (Full affine span at a fixed state)

For any fixed $s\in S$, the following statements are equivalent: For any $v\in\mathbb{R}^{p}$ such that $\|v\|_{2}=1$ the map $A\ni a\mapsto v^{\top}g(s,a)$ is not a constant. $g(s,A)$ has full affine dimension i.e. $\operatorname{span}\{g(s,a)-g(s,a^{\prime}):a,a^{\prime}\in A\}=\mathbb{R}^{p}$.

### Proof

To see this, let us first show that 1. implies 2. We proceed by contradiction. If the span in 2. was a proper subspace $V_{s}\subset\mathbb{R}^{p}$, then $V_{s}^{\perp}$ is not empty. Hence we can choose some $m\in V_{s}^{\perp}\setminus\{\mathbf{0}\}$ such that But then $a\mapsto(m/\|m\|_{2})^{\top}g(s,a)=(m/\|m\|_{2})^{\top}g(s,a^{\prime})$ which is a constant thus contradicting 1.

Now we show 2. implies 1. Again we proceed by contradiction. From 2. we know that $u\in V_{s}^{\perp}=\{\mathbf{0}\}$. If $u^{\top}g(s,\cdot)$ is constant for some $u\in\mathbb{R}^{p}$ such that $\|u\|_{2}=1$ then $u^{\top}(g(s,a)-g(s,a^{\prime}))=0$ for all $a,a^{\prime}\in A$. So $u\in V_{s}^{\perp}=\{\mathbf{0}\}$, a contradiction. ∎ See 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

Consider $\theta=ru$ with $r=\|\theta\|_{2}$ and $u\in\mathbb{S}^{p-1}$. We analyze along $\theta=ru$ with $r\to+\infty$: Define for fixed $s\in S$, For any fixed margin $\varepsilon>0$, define the $\varepsilon$-optimal super-level set: First, we establish that the Gibbs measure strictly concentrates on $A_{\varepsilon}$. The probability of sampling outside this set under $\pi_{\theta}$ is bounded by evaluating the worst-case numerator and restricting the denominator's domain to $A_{\varepsilon/2}$: $\mu(A_{\varepsilon/2})>0$ is a strictly positive constant independent of $r$ And we have $e^{-r\varepsilon/2}\to 0$ as $r\to\infty$. Thus, $\pi_{ru}(A_{\varepsilon}^{c}|s)\to 0$, which implies $\pi_{ru}(A_{\varepsilon}|s)\to 1$.

Next, we apply partition property of the KL divergence (Lemma 1.4.3 in Dupuis and Ellis). By splitting the action space into the binary partition $\{A_{\varepsilon},A_{\varepsilon}^{c}\}$, the KL divergence is bounded below by the divergence between the Bernoulli distributions induced by this partition: Taking the limit inferior as $r\to\infty$, and substituting $\pi_{ru}(A_{\varepsilon}|s)\to 1$ and $\pi_{ru}(A_{\varepsilon}^{c}|s)\to 0$, we obtain: This lower bound holds for any $\varepsilon>0$. By the continuity of $g(s,\cdot)$, the intersection of these sets as $\varepsilon\downarrow 0$ is exactly the maximizer set $\operatorname{Argmax}(\phi^{s}_{u})$ i.e.

Moreover, the family $\{A_{\varepsilon}\}_{\varepsilon>0}$ is decreasing as $\varepsilon\downarrow 0$. By continuity from above of the probability measure $\mu$, By Assumption 2, $\mu(\operatorname{Argmax}(\phi^{s}_{u}))=0$. Therefore, taking the limit as $\varepsilon\downarrow 0$ yields: Consequently, since $u\in\mathbb{S}^{p-1}$ is arbitrary and $\mathbb{S}^{p-1}$ is compact, $\lim_{\|\theta\|_{2}\to\infty}\mathrm{KL}\bigl(\pi_{\theta}(\cdot\mid s)\,|\,\mu\bigr)=\infty$, which completes the proof. ∎

### Proof of Lemma 3. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

See 3. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

Since the gradient flow satisfying local Lipschitz condition by Proposition 2). ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), with Lyapunov function $V_{\tau}^{\pi_{\cdot}}(\rho):\mathbb{R}^{p}\rightarrow\mathbb{R}$ that has radial unboundedness by Theorem 2. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), and we know the existence of solutions to the gradient flow for any $t\geq 0$ and there exists a constant $C_{\tau}$ such that $\sup_{t}\|\theta_{t}\|\leq C_{\tau}$ by classical arguments for constructing ODE solutions with Lyapunov functions.

For all $s\in S,a\in A$, any $t\geq 0$

### Proof of Theorem 4. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

See 3 See 4. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

From Lemma 3. ‣ Full affine span features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), there exists $R>0$ which is sufficiently large, such that for $t\geq 0$, which means that $\min_{s,a}\frac{d\pi_{\theta_{t}}}{d\mu}(a|s)\geq e^{-R}$. From Lemma 20, we know that there exists From Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we know Then from Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), and Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") again, then using Grönwall's inequality concludes the proof. ∎

### Proof of Theorem 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

Recall that for any $v\in\mathbb{R}^{p}$ we will write $v_{\perp}:=v-p^{-1}\langle v,\mathbf{1}\rangle\mathbf{1}$.

See 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

Consider $\theta_{\perp}=ru$ with $r=\|\theta\|_{2}$ and $u\perp\mathbf{1},u\in\mathbb{S}^{p-1}$. We analyze along $\theta_{\perp}=ru$ with $r\to+\infty$: Define for fixed $s\in S$, For any fixed margin $\varepsilon>0$, define the $\varepsilon$-optimal super-level set: First, we establish that the Gibbs measure strictly concentrates on $A_{\varepsilon}$. The probability of sampling outside this set under $\pi_{\theta}$ is bounded by evaluating the worst-case numerator and restricting the denominator's domain to $A_{\varepsilon/2}$: $\mu(A_{\varepsilon/2})>0$ is a strictly positive constant independent of $r$ And we have $e^{-r\varepsilon/2}\to 0$ as $r\to\infty$. Thus, $\pi_{ru}(A_{\varepsilon}^{c}|s)\to 0$, which implies $\pi_{ru}(A_{\varepsilon}|s)\to 1$.

Next, we apply partition property of the KL divergence (Lemma 1.4.3 in Dupuis and Ellis). By splitting the action space into the binary partition $\{A_{\varepsilon},A_{\varepsilon}^{c}\}$, the KL divergence is bounded below by the divergence between the Bernoulli distributions induced by this partition: Taking the limit inferior as $r\to\infty$, and substituting $\pi_{ru}(A_{\varepsilon}|s)\to 1$ and $\pi_{ru}(A_{\varepsilon}^{c}|s)\to 0$, we obtain: This lower bound holds for any $\varepsilon>0$. By the continuity of $g(s,\cdot)$, the intersection of these sets as $\varepsilon\downarrow 0$ is exactly the maximizer set $\operatorname{Argmax}(\phi^{s}_{u})$ i.e.

Moreover, the family $\{A_{\varepsilon}\}_{\varepsilon>0}$ is decreasing as $\varepsilon\downarrow 0$. By continuity from above of the probability measure $\mu$, By Assumption 2, $\mu(\operatorname{Argmax}(\phi^{s}_{u}))=0$. Therefore, taking the limit as $\varepsilon\downarrow 0$ yields: Consequently, since $u\in\mathbb{S}^{p-1}\cap\{v\in\mathbb{R}^{p}:v\perp\mathbf{1}\}$ is arbitrary and $\mathbb{S}^{p-1}\cap\{v\in\mathbb{R}^{p}:v\perp\mathbf{1}\}$ is compact, $\lim_{\theta\in\mathbb{R}^{p}:\|\theta_{\perp}\|_{2}\to\infty}\mathrm{KL}\bigl(\pi_{\theta}(\cdot\mid s)\,|\,\mu\bigr)=\infty$, which completes the proof. ∎

### Proof of Lemma 6. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

See 6. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

By Proposition 2). ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we know the solution to exists for $t\in0,T_{\max})$ for some $T_{\max}<\infty$, denoted by $\{\theta_{t}\}_{t\in[0,T_{\max})}$. Firstly, we show that the solution to the gradient flow would not explode in finite time $t\in[0,T_{\max})$. Note that for all $s\in S$ and $a\in A$, Calculation in Lemma [13 shows that By Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we have where in the first inequality we use that $G^{\pi_{\theta_{t}}}(\rho)$ is positive semi-definite, in the second inequality we use Young's Inequality, bounds and Lemma 11, in the last inequality we use. From the previous estimates, define Then we obtain the differential inequality for constants $C_{1},C_{2}>0$. By Grönwall's inequality, As a result, there is no finite time blow up of $\theta_{t}$.

Under Assumption 4, by Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and Lemma 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we know that implying that $\mathbf{1}^{\top}\theta_{t}=\mathbf{1}^{\top}\theta_{0}$ for any $t\geq 0$.

Consider $\theta_{t}=(\theta_{t})_{\perp}+\frac{\theta_{t}^{\top}\mathbf{1}}{p}\mathbf{1}$, where $\theta_{t,\perp}\perp\mathbf{1}$. By Theorem 5. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), and the fact we know $S=\Omega_{c}\cap\left\{\theta|\mathbf{1}^{T}\theta=\mathbf{1}^{T}\theta_{0}\right\}$, where $\Omega_{c}=\left\{\theta|V_{\tau}^{\pi_{\theta}}(\rho)\leq V_{\tau}^{\pi_{\theta_{0}}}(\rho)\right\}$, is compact positive invariant. Hence classical arguments for constructing ODE solutions with Lyapunov functions, we know the existence of solutions to the gradient flow for any $t\geq 0$ and there exists a constant $C_{\tau}$ such that $\sup_{t}\|\theta_{t}\|\leq C_{\tau}$.

For all $s\in S,a\in A$, any $t\geq 0$,

### Proof of Theorem 7. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

See 5 See 7. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

From Lemma 6. ‣ Simplex features ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), there exists $R>0$ which is sufficiently large, such that for $t\geq 0$, which means that $\min_{s,a}\frac{d\pi_{\theta_{t}}}{d\mu}(a|s)\geq e^{-R}$. From Lemma 21, we know that there exists From Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we know Then from Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), and Theorem 1. ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") again, then using Grönwall's inequality concludes the proof. ∎

### More discussions about Example 3. ‣ Example of a feature basis not providing radial unboundedness ‣ 2. Formulation and the statement of the main results ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Example 4 (Hat function features)

Let $x_{0}<x_{1}<\cdots<x_{N}$, and consider the standard one-dimensional finite-element hat functions together with the boundary functions Set $g(a):=(g_{0}(a),g_{1}(a),\dots,g_{N}(a))^{\top}$. We now take $N=3$ and choose the concrete grid $x_{0}=0,\ x_{1}=\frac{1}{3},\ x_{2}=\frac{2}{3},\ x_{3}=1$.

Let $\theta=(-1,1,1,-1)^{\top}$. Then $\theta^{\top}\mathbf{1}=-1+1+1-1=0$. Define $f_{\theta}(a):=\theta^{\top}g(a)$. Therefore Thus $f_{\theta}(a)\leq 1$ for every $a\in$, and the maximizer set is $\operatorname*{arg\,max}_{a\in}f_{\theta}(a)=\left[\frac{1}{3},\frac{2}{3}\right]$, which has positive Lebesgue measure $\mu([\frac{1}{3},\frac{2}{3}])=\frac{1}{3}$. Consequently, Assumption 4 is not satisfied in this example.

Let $\mu$ be Lebesgue measure restricted to $$. For $\beta>0$, define the probability measure $\pi_{\beta}$ by $p_{\beta}(a):=\frac{d\pi_{\beta}}{d\mu}(a)=e^{\beta f_{\theta}(a)}/Z_{\beta}$, where $Z_{\beta}:=\int_{0}^{1}e^{\beta f_{\theta}(a)}\,da$. Since $p_{\beta}$ integrates to one, the relative entropy of $\pi_{\beta}$ with respect to $\mu$ is $\operatorname{KL}(\pi_{\beta}|\mu):=\int_{0}^{1}p_{\beta}(a)\log p_{\beta}(a)\,da$. Moreover, since $\log p_{\beta}(a)=\beta f_{\theta}(a)-\log Z_{\beta}$, we have We first compute $Z_{\beta}$. On $[0,\frac{1}{3}]$, set $y=f_{\theta}(a)=6a-1$. Then $\int_{0}^{1/3}e^{\beta f_{\theta}(a)}\,da=\frac{1}{6}\int_{-1}^{1}e^{\beta y}\,dy$. On the middle interval $[\frac{1}{3},\frac{2}{3}]$, one has $f_{\theta}(a)=1$, so $\int_{1/3}^{2/3}e^{\beta f_{\theta}(a)}\,da=\frac{1}{3}e^{\beta}$. On $[\frac{2}{3},1]$, set $y=f_{\theta}(a)=5-6a$. Then $dy=-6\,da$, $\int_{2/3}^{1}e^{\beta f_{\theta}(a)}\,da=\frac{1}{6}\int_{-1}^{1}e^{\beta y}\,dy$. Combining the three pieces gives Since $\int_{-1}^{1}e^{\beta y}\,dy=(e^{\beta}-e^{-\beta})/\beta$, we obtain Therefore $\log Z_{\beta}=\beta-\log 3+\log(1+(1-e^{-2\beta})/\beta)$. Since $e^{-2\beta}$ is exponentially small as $\beta\to\infty$, and since $\log(1+u)=u-\frac{u^{2}}{2}+\mathcal{O}(u^{3})$ as $u\to 0$, we get Next define $N_{\beta}:=\int_{0}^{1}f_{\theta}(a)e^{\beta f_{\theta}(a)}\,da$. Then $\mathbb{E}_{\pi_{\beta}}[f_{\theta}(a)]=N_{\beta}/Z_{\beta}$. We compute $N_{\beta}$ using the same changes of variables. On the two exterior intervals, the variable $y=f_{\theta}(a)$ runs linearly from $-1$ to $1$, while on the middle interval $f_{\theta}(a)=1$. Hence Dividing the exact formula for $N_{\beta}$ by the exact formula for $Z_{\beta}$, we find Since $e^{-2\beta}$ is exponentially small, it may be absorbed into any algebraic remainder. Therefore The rational term equals $1-\frac{1/\beta^{2}}{1+1/\beta}$. Using $1/(1+1/\beta)=1-1/\beta+\mathcal{O}(1/\beta^{2})$, we obtain Substituting the expansions of $\beta\,\mathbb{E}_{\pi_{\beta}}[f_{\theta}(a)]$ and $\log Z_{\beta}$ into the entropy identity gives Therefore, $\lim_{\beta\to\infty}\operatorname{KL}(\pi_{\beta}|\mu)=\log 3$. Hence, in this concrete example, the relative entropy remains bounded as $\beta\to\infty$. Therefore, without Assumption 4, one cannot in general expect radial unboundedness of the KL divergence.

### Additional useful results

We introduce the following dynamic programming principle (see Theorem B.1 in Kerimkulov et al. ).

### Theorem 16 (Dynamic programming principle)

Let $\tau>0$. The optimal value function $V_{\tau}^{*}$ is the unique bounded solution of the following Bellman equation: Consequently, for all $s\in S$, where $Q^{*}\in B_{b}(S\times A)$ is defined by Moreover, there is an optimal policy $\pi_{\tau}^{*}\in\mathcal{P}_{\mu}(a|s)$ given by

### Definition 2

A functional $F:\mathcal{C}\mapsto\mathbb{R}^{d}$ is said to admit a linear derivative if there is a continuous map $\frac{\delta F}{\delta m}:\mathcal{C}\times\mathbb{R}^{p}\mapsto\mathbb{R}^{d}$, such that for all $m,m^{\prime}\in\mathcal{C}$, it holds that $\int\left\|\frac{\delta F}{\delta m}(m)(a)\right\|_{2}m^{\prime}(a)d(a)<\infty$, and

### Proposition 3 (Strong convexity of negative entropy)

Let $W>0$ and define Define $F:\mathcal{P}_{W}^{A}\to\mathbb{R}$ by with the convention $0\log 0=0$. Then $F$ is $W$--strongly convex on $\mathcal{P}_{W}^{A}$ with respect to the $L^{2}(A,\mu)$ distance between densities. In particular, for all $\pi,\pi^{\prime}\in\mathcal{P}_{W}^{A}$ such that $\frac{d\pi}{d\mu}>0$ $\mu$-a.e. and the first variation is well defined, is the first variation in the sense of Definition 2.

### Proof

By definition of $\mathcal{P}_{W}^{A}$, we have Consider $\varphi(x)=x\log x$ on $[0,W^{-1}]$, with the convention $\varphi=0$. Since the function $\varphi$ is $W$--strongly convex on $[0,W^{-1}]$. Hence, for $x,y\in[0,W^{-1}]$ with $x>0$, and integrating over $A$ gives Moreover, since both $\pi$ and $\pi^{\prime}$ are probability measures, so the linear term may also be written as This proves the claimed strong convexity inequality. ∎ Next, let us introduce the KL-logit inequality (for discrete case, refer to Lemma 27 Mei et al.).

### Lemma 17

Fix $s\in S$. If $\theta,\theta^{\prime}\in\mathbb{R}^{p}$ satisfy for some $W>0$, then

### Proof

For simplicity, write By definition, both densities are strictly positive $\mu$-a.e. Moreover, by assumption, Define the negative entropy functional By Proposition 3. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), $F$ is $W$--strongly convex on the set of densities bounded by $W^{-1}$. Hence, Since both $f_{\theta}$ and $f_{\theta^{\prime}}$ are probability densities, Using the identity The normalizing constants vanish after integration because Using the elementary inequality Finally, by the bound on $g$,

### Lemma 18

Let Assumptions 4 hold. Fix $s\in S$. If $\theta,\theta^{\prime}\in\mathbb{R}^{p}$ satisfy for some $W>0$, then for every $c\in\mathbb{R}$,

### Proof

By the logit parametrization, both densities are strictly positive $\mu$-a.e. Moreover, by assumption, be the negative entropy functional. By Proposition 3. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), $F$ is $W$--strongly convex on densities bounded by $W^{-1}$. Hence, to remove the constant term in the first variation.

By the logit parametrization, Thus, for any $c\in\mathbb{R}$, Since both $f_{\theta}(\cdot|s)$ and $f_{\theta^{\prime}}(\cdot|s)$ are probability densities, Hence the constant term vanishes after integration against $f_{\theta}(\cdot|s)-f_{\theta^{\prime}}(\cdot|s)$. Therefore, Finally, by the bound on $g$,

### Lemma 19 (Concavity of variance)

Let $P=qP_{1}+(1-q)P_{2}$ with $q\in$, where $P_{1}$ and $P_{2}$ are probability measures. If $X\in L^{2}(P_{1})\cap L^{2}(P_{2})$, then

### Proof

Let $\bar{\mu}_{i}=\mathbb{E}_{P_{i}}[X]$ for $i=1,2$. Since $P=qP_{1}+(1-q)P_{2}$, For any $\pi\in\Pi_{\mu}$, define

### Lemma 20

Let $\theta^{\prime}\in\mathbb{R}^{p}$. If there exists a constant $R>0$ such that $\left|\log\frac{d\pi}{d\mu}(a|s)\right|_{B_{b}({S\times A})}\leq R$, then there exists such that $\int_{S}\lambda_{\min}(G^{\pi}(s))d_{\rho}^{\pi^{*}}(ds)\geq\lambda$.

### Proof

so $\left|\frac{d\pi_{\theta^{\prime}}}{d\mu}\right|_{B_{b}(S\times A)}\leq e^{2\|\theta^{\prime}\|_{2}}$. Since $\min_{s\in S,a\in A}\frac{d\pi}{d\pi_{\theta^{\prime}}}(a|s)=\min_{s\in S,a\in A}\frac{d\pi}{d\mu}\frac{d\mu}{d\pi_{\theta^{\prime}}}(a|s)\geq e^{-R-2\|\theta^{\prime}\|_{2}}>0$, then we know $e^{-R-2\|\theta^{\prime}\|_{2}}\leq\int_{A}\frac{d\pi}{d\pi_{\theta^{\prime}}}(a|s)\pi_{\theta^{\prime}}(da)=1$, and where $\bar{\pi}(da|s)=\frac{\pi(da|s)-e^{-R-2\|\theta^{\prime}\|_{2}}\pi_{\theta^{\prime}}(da)}{1-e^{-R-2\|\theta^{\prime}\|_{2}}}$ determines a valid probability measure for fixed $s$.

Hence by Lemma 19. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), where in the first equality we use the Definition 1 of FIM, which implies that, then there exists such that $\int_{A}\lambda_{\min}(G^{\pi}(s))d_{\rho}^{\pi^{*}}(ds)\geq\lambda$. ∎

### Lemma 21

Let $\theta^{\prime}\in\mathbb{R}^{p}$. If there exists a constant $R>0$ such that $\left|\log\frac{d\pi}{d\mu}(a|s)\right|_{B_{b}({S\times A})}\leq R$, then there exists such that $\int\lambda_{\min}\left(\int g(s,a)g^{\top}(s,a)\pi(da|s)\right))d_{\rho}^{\pi_{\theta^{*}}}(ds)\geq\lambda$.

### Proof

Also for all $s\in S,a\in A$, so $\left|\frac{d\pi_{\theta^{\prime}}}{d\mu}\right|_{B_{b}(S\times A)}\leq e^{2\|\theta^{\prime}\|_{2}}$.

Since $\min_{s\in S,a\in A}\frac{d\pi}{d\pi_{\theta^{\prime}}}(a|s)=\min_{s\in S,a\in A}\frac{d\pi}{d\mu}\frac{d\mu}{d\pi_{\theta^{\prime}}}(a|s)\geq e^{-R-2\|\theta^{\prime}\|_{2}}>0$, then we know $e^{-R-2\|\theta^{\prime}\|_{2}}\leq\int_{A}\frac{d\pi}{d\pi_{\theta^{\prime}}}(a|s)\pi_{\theta^{\prime}}(da)=1$, and where $\bar{\pi}(da|s)=\frac{\pi(da|s)-e^{-R-2\|\theta^{\prime}\|_{2}}\pi_{\theta^{\prime}}(da)}{1-e^{-R-2\|\theta^{\prime}\|_{2}}}$ determines a valid probability measure for fixed $s$.

Hence by Lemma 19. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"),

### Proposition 4

Let Assumption 2 hold. For all $\theta\in\mathbb{R}^{p}$, $\lambda_{\min}(G^{\pi_{\theta}}(s))=0$ with eigenvector $\textbf{1}\in\mathbb{R}^{p}$.

### Proof

Define $\bar{g}_{\theta}(s):=\int_{A}g(s,a)\pi_{\theta}(da|s)$, and note that $\bar{g}_{\theta}^{\top}(s)\textbf{1}=\int g(s,a)^{\top}\textbf{1}\pi_{\theta}(da|s)=1$, then we have Next, we introduce the following interlacing theorem of eigenvalues of a real symmetric matrix perturbed by a rank 1 matrix (see Section 5 in Golub).

### Theorem 22 (Eigenvalue Interlacing Theorem)

Let B be a real symmetric matrix. Define: If the n eigenvalues of A are $\eta_{1}\geq\dots\geq\eta_{n}$, and the n eigenvalues of B are $\lambda_{1}\geq\dots\geq\lambda_{n}$, then these are interlaced as: $\eta_{1}\geq\lambda_{1}\geq\dots\geq\eta_{i}\geq\lambda_{i}\geq\eta_{i+1}\dots\eta_{n}\geq\lambda_{n}$.

The following Corollary 2 is similar to Lemma 23 in Mei et al..

### Corollary 2

Let Assumption 2 hold. Then for fixed $s\in\mathcal{S}$, for any vector $y,\theta\in\mathbb{R}^{p}$, then

### Proof

Let $\eta_{i},i=2,3,\ldots,p$ be the eigenvalue of matrix $\int_{A}g(s,a)g^{\top}(s,a)\pi_{\theta}(da|s)$ in the following order and denote the eigenvalues of $G^{\pi_{\theta}}(s)$ as Then Theorem 22. ‣ 3.5. Additional useful results ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") indicates that, Since $G^{\pi_{\theta}}(s)$ is real symmetric, its eigenvectors $\left\{\frac{\mathbf{1}}{\sqrt{p}},v_{p-1},\ldots,v_{1}\right\}$ are orthonormal. For any vector $y$, $y$ can be written as linear combination of eigenvectors of $G^{\pi_{\theta}}(s)$, The last equation is because the representation is unique, and Therefore because of $\lambda_{p-1}\geq\eta_{p}=\lambda_{\min}\left(\int_{A}g(s,a)g^{\top}(s,a)\pi_{\theta}(da|s)\right)$,

### Proof of Proposition 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

Let $\theta,\theta^{\prime}\in\mathbb{R}^{p}$ and define $\theta^{\varepsilon}=\theta+\varepsilon(\theta^{\prime}-\theta)$ for $\varepsilon\in$. we first study the difference quotient $H^{\varepsilon}(s)=\frac{V^{\pi_{\theta^{\varepsilon}}}_{\tau}(s)-V^{\pi_{\theta}}_{\tau}(s)}{\varepsilon}\,.$ By, we have For convenience, we introduce the unnormalized policy $\tilde{\pi}:\mathcal{P}(\mathbb{R}^{d})\rightarrow b\mathcal{K}_{\mu}(A|S)$ given by For all $(s,a)\in S\times A$, we have Simple manipulation yields Taylor expanding the exponential function, we find | \(46\) | | $\displaystyle\varepsilon^{-1}\frac{\frac{d\tilde{\pi}_{\theta^{\varepsilon}}}{d\mu}(a|s)-\frac{d\tilde{\pi}_{\theta}}{d\mu}(a|s)}{\tilde{\pi}_{\theta}(A|s)}$ | $\displaystyle=\frac{d\pi_{\theta}}{d\mu}(a|s)\langle\theta^{\prime}-\theta,g(s,a)\rangle$ | | | | | | $\displaystyle\quad+\varepsilon\frac{d\pi_{\theta}}{d\mu}(a|s)\sum_{n=2}^{\infty}\varepsilon^{n-2}\frac{\varepsilon\langle\theta^{\prime}-\theta,g(s,a)\rangle^{n}}{n!}\,.$ | | Thus, using $\pi_{\theta}(A|s)=1$, we obtain The dominated convergence theorem implies that Step 2: We now will pass to the limit as $\varepsilon\rightarrow 0$ in Eq.. Let us begin with the $I_{4}^{\varepsilon}$-term. Recalling, we have Since $\pi_{\theta}\in\Pi_{\mu}$, there exists a constant $\tilde{R}_{\theta}>0$ such that $\left|\frac{d\pi_{\theta}}{d\mu}\right|_{B_{b}(S\times A)}\leq\tilde{R}_{\theta}$ there is an $\varepsilon_{0}\in(0,1]$ such that for all $\varepsilon<\varepsilon_{0}$, $s\in S$, and $\mu-a.e.\,a\in A$, Taylor expanding the logarithm, we get Using, we find that Thus, by Lemma 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), we have and that there exists a constant $C>0$ such that for all $\varepsilon<\varepsilon_{0}$, $s\in S$, and $\mu-a.e.\,a\in A$, Therefore, owing to and, we find We now turn our attention to $I_{3}^{\varepsilon}$. Recalling, we have It follows from Corollary 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), Eq. (also Eq.), Lemma 13, and the bound on cost function, that Thus, by Lemmas 13 and 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), by dominated convergence theorem we obtain Using Lemmas 13 and 10. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs") and bound on cost function, by dominated convergence theorem we get Putting it all together and using the definition of $Q^{\pi}_{\tau}$, we arrive at Since $(I_{j})_{1\leq j\leq 5}$ are bounded uniformly in $\varepsilon$, we may apply the bounded convergence theorem to pass to the limit in to obtain (33. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")). ∎

### Proof of Proposition 2). ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs")

### Proof

Using Lemma 11, Lemma 13, Lemma 12). ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), Corollary 1. ‣ 3.2. Basic results on entropy regularized MDPs ‣ 3. Proofs ‣ Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs"), putting Eq. back to Eq., we have

## Conclusion

We prove linear convergence of policy gradient for entropy regularized MDPs with log-linear policies on general state and action spaces under $Q^{\pi}_{\tau}$-realizability and when suitable basis functions are employed. This complements existing results for softmax policy gradient methods in the tabular setting Mei et al.. To obtain our results we have established a non-uniform PŁ inequality for general state and action spaces and carried out novel Lyapunov function-based analysis allowing control of the non-uniform term.
