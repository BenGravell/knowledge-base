<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning is a framework for interactive decision-making with incentives sequentially revealed across time without a system dynamics model. Due to its scaling to continuous spaces, we focus on policy search where one iteratively improves a parameterized policy with stochastic policy gradient (PG) updates. In tabular Markov Decision Problems (MDPs), under persistent exploration and suitable parameterization, global optimality may be obtained. By contrast, in continuous space, the non-convexity poses a pathological challenge as evidenced by existing convergence results being mostly limited to stationarity or arbitrary local extrema. To close this gap, we step towards persistent exploration in continuous space through policy parameterizations defined by distributions of heavier tails defined by tail-index parameter alpha, which increases the likelihood of jumping in state space. Doing so invalidates smoothness conditions of the score function common to PG. Thus, we establish how the convergence rate to stationarity depends on the policy's tail index alpha, a Holder continuity parameter, integrability conditions, and an exploration tolerance parameter introduced here for the first time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Further, we characterize the dependence of the set of local maxima on the tail index through an exit and transition time analysis of a suitably defined Markov chain, identifying that policies associated with Levy Processes of a heavier tail converge to wider peaks. This phenomenon yields improved stability to perturbations in supervised learning, which we corroborate also manifests in improved performance of policy search, especially when myopic and farsighted incentives are misaligned.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reinforcement learning (RL), an autonomous agent sequentially interacts with its environment and observes rewards incrementally across time. This framework has gained attention in recent years for its successes in continuous control, web services, personalized medicine, among other contexts. Mathematically, it may be described by a Markov Decision Process (MDP), in which an agent seeks to select actions so as to maximize the long-term accumulation of rewards, known as the value. The key distinguishing point of RL from classical optimal control is its ability to discern control policies without a system dynamics model.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Algorithms for RL either operate by Monte Carlo tree search, approximately solve Bellman's equations, or conduct direct policy search. While the first two approaches may have lower variance and converge faster, they typically require representing a tree or $Q$-function for every state-action pair, which is intractable in continuous space. For this reason, we focus on PG.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy search hinges upon the Policy Gradient Theorem, which expresses the gradient of the value function with respect to policy parameters as the expected value of the product of the score function of the policy and its associated $Q$ function. Its performance has historically been understood only asymptotically via tools from dynamical systems. More recently, the non-asymptotic behavior of policy search has come to the fore. In continuous space, its finite-time performance has been linked to stochastic search over non-convex objectives, whose $\mathcal{O}{({1/\sqrt{k}})}$ convergence rate to stationarity is now clear. However, it is challenging to discern the quality of a given limit point under this paradigm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By contrast, for tabular MDPs, i.e., those with state and action spaces defined by finite discrete sets, stronger results have appeared: linear convergence to *global* optimality for tabular or softmax parameterizations. A critical enabler of these recent innovations in finite MDPs is a persistent exploration condition: the initial distribution over the states is uniformly lower bounded away from null, under which the current policy may be shown to assign strictly positive likelihood to the optimal action over the entire state space \[Lemma 9\]. This concept of exploration is categorically different from notions common to bandits, i.e., optimism in the face of uncertainty, and instead echoes persistence of excitation in systems identification. Under this condition, then, a version of gradient dominance (known also as Polyak-Łojasiewicz inequality ) holds, as derived. This result enables such global improvement bounds. Unfortunately, translating this condition to continuous space is elusive, as many common distributions in continuous space may fail to be integrable if their likelihood is lower bounded away from null over the entire (not necessarily compact) state space.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Can one nearly satisfy persistent exploration in MDPs over continuous spaces through appropriate policy parameterizations, and in doing so, mitigate the pathologies of non-convexity?*

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we step towards an answer by studying policy parameterizations defined by heavy-tailed distributions, which includes the family of Lévy Processes common to fractal geometry, finance, pattern formation in nature, and networked systems. By employing a heavy-tailed policy, the induced transition dynamics will be heavy-tailed, and hence at increased likelihood of jumping to non-adjacent states. That policies or stochastic policy gradient estimates associated with heavy-tailed distributions exhibit improved coverage of continuous space is well-documented experimentally. Here we seek a more rigorous understanding of in what sense this impacts performance may be formalized through *metastability*, the study of how a stochastic process transitions between its equilibria. This marks a step towards persistent exploration in continuous space, but satisfying it precisely remains beyond our grasp.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Historically, heavy-tailed distributions have been recently employed in non-convex optimization to perturb stochastic gradient updates by $\alpha$-stable Lévy noise, inspired by earlier approaches where instead Gaussian noise perturbations are used. Doing so has notably been shown to yield improved stability to perturbations in parameter space since SGD perturbed by heavy-tailed noise can converge to local extrema with more volume, which in supervised learning is experimentally associated with improved generalization, and has given rise to a nascent generalization theory based on the tail index of the parameter estimate's limiting distribution. Rather than perturbing stochastic gradient updates, we directly parameterize policies as heavy-tailed distributions, which induces heavy-tailed gradient noise. Doing so invalidates several aspects of existing analyses of PG in continuous spaces.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a few heavy-tailed policy parameterizations that may be used in lieu of a Gaussian policy for continuous space, which can prioritize selecting actions far from the distribution's center (Sec. 3), and discuss how policy search manifests for this setting (Sec. 4);

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish the attenuation rate of the expected gradient norm of the value function when the score function is Hölder continuous, and may be unbounded but whose moment is integrable with respect to the policy (Theorem 5.2). This statement generalizes previous results that break for non-compact spaces, and further requires introducing an exploration tolerance parameter (Definition 5.1) to quantify the subset of the action space where the score function is absolutely bounded;

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In sec. 5.2, by rewriting the PG under a heavy-tailed policy as a discretization of a Lévy Process, we establish that the time required to exit a (possibly spurious) local extrema decreases polynomially with heavier tails (smaller $\alpha$), and the width of a peak's neighborhood (Theorem 5.5). Further, the proportion of time required to transition from one local extrema to another depends polynomially on its width, which decreases for smaller tail index (Theorem 5.6). By contrast, lighter-tailed policies exhibit transition times depending exponentially on the volume of an extrema's neighborhood;

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Experimentally, we observe that policies associated with heavy-tailed distributions converge more quickly in problems that are afflicted with multiple spurious stationary points, which are especially common when myopic and farsighted incentives are in conflict with one another (Sec. 6).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

Efforts to circumvent the necessity of persistent exploration and obtain rates to global optimality have been considered in both finite and continuous space. In tabular settings, one may incorporate proximal-style updates in order to leverage a performance-difference lemma, which has given rise to recent analyses of natural policy gradient. Translating these results to the continuum remains an open problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

Alternatively, in continuous space, one may hypothesize the policy parameterization is a neural network whose size grows unbounded with the number of samples processed. Doing so belies the fact that typically a parameterization has fixed dimension during training. Alternatively, one may impose a "transferred compatible function approximation error" condition that mandates the ability to sample from the occupancy measure of the optimal policy to ensure sufficient state space coverage, which is difficult to perform in practice.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

Two additional lines of effort are pertinent to the objective of this work. The first is state aggregation, in which one hypothesizes a large but finite space admits a representation in terms of low-dimensional features, such as tile coding or interpolators. A long history of works seeks to discern such state aggregations adaptively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

Such representations can be used, e.g., policy search or value iteration to obtain refined convergence behavior that depends only on the properties of the representation rather than the underlying state or action spaces. Finding this representation is itself not necessarily easier than solving the original MDP, however. See, for instance where a variety of structural assumptions and representations are discussed. In this work, we assume such a feature map is fixed at the outset of training as part of one's specification of a policy parameterization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

The other research thrust broadly related to this work is information-theoretic exploration that seeks comprehensive state-space coverage. The simplest way to achieve this goal is to simply replace the cumulative return with an objective that prioritizes state-space coverage, such as the entropy of the occupancy measure induced by a policy. This goal does not necessarily result in good performance with respect to the cumulative return, however. Alternatively, exploration bonuses in the form of upper-confidence bound, Thompson sampling, information-directed sampling, among other strategies (see for a thorough review), have percolated into RL in various forms.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

For instance, incorporating randomized perturbations/exploration bonuses into value iteration, Q-learning, or augmenting a policy's variance hyper-parameters in policy search in a manner reminiscent of line-search for step-size selection. Alternative approaches based on Thompson sampling and various Bayesian models of the value function have been considered, as well as approaches which subsume exploration goals into the choice of the aforementioned state aggregator. Our approach contrasts with approaches that inject suitably scaled randomness into an RL update, by searching over a policy class that is itself more inherently random.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Additional Context and Related Work", "weight": 1.0} -->

Notations: All the norms $\parallel \cdot \parallel$ are Euclidean norm unless otherwise stated.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Markov Decision Problems", "weight": 1.0} -->

In RL, an agent evolves through states $s \in \mathcal{S}$ selecting actions $a \in \mathcal{A}$, which causes transitions to another state $s^{\prime}$ to occur according to a Markov transition density ${\mathbb{P}}{(\left. s^{\prime} \middle| {s,a} \right.)}$ and a reward $r{(s,a)}$ is revealed by the environment to inform its merit. Formally, an MDP consists of the tuple $(\mathcal{S},\mathcal{A},{\mathbb{P}},r,\gamma)$, where continuous state $\mathcal{S} \subseteq {\mathbb{R}}^{q}$ and action spaces may be unbounded, i.e., Euclidean space in the appropriate dimension.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Markov Decision Problems", "weight": 1.0} -->

We hypothesize that actions $a_{t} \sim \pi{( \cdot |s_{t})}$ are selected according to a time-invariant distribution ${\pi{(\left. a \middle| s \right.)}}:={{\mathbb{P}}{({a_{t} = \left. a \middle| s_{t} \right. = s})}}$ called a policy determining the probability of action $a$ when in state $s$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Markov Decision Problems", "weight": 1.0} -->

One difficulty in RL is that (3.2) is non-convex in parameters $\mathbf{θ}$. Thus, finding a global optimizer is challenging even if the problem were deterministic. However, in the present context, the search procedure also interacts with the transition dynamics ${\mathbb{P}}{(\left. s^{\prime} \middle| {s,a} \right.)}$. Before delving into how one may iteratively and approximately solve (3.2), we present a few representative policy parameterizations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 3.2 (Moderate-tailed policy)", "weight": 1.0} -->

We next introduce heavy-tailed policies, specifically, Lévy processes called $\alpha$-stable distributions, which are historically associated with fractal geometry, finance, and network science.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3.3 (Lévy Process Policy)", "weight": 1.0} -->

Symmetric $\alpha$ stable, $\mathcal{S}\alpha\mathcal{S}$ distributions generalize Gaussians with $\alpha \in {(0,2\rbrack}$ as the tail index determining the decay rate of the distribution's tail. Denote random variable $\text{X} \sim {\mathcal{S}\alpha\mathcal{S}{(\sigma)}}$ with associated characteristic function ${{\mathbb{E}}\left\lbrack e^{i\omega\text{X}} \right\rbrack} = e^{- {\sigma{|\omega|}^{\alpha}}}$ and scale parameter $\sigma \in {(0,\infty)}$. For non-integer (fractional) value of $\alpha$, there is no closed form expression but the density decays at a rate $1/{|a|}^{1 + \alpha}$, and is referred to as fractal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 3.3 (Lévy Process Policy)", "weight": 1.0} -->

With a few policy choices of detailed, we delve into their relative merits and drawbacks. Intuitively, policies that select actions far from a learned mean parameter over actions may better explore the space, which exhibits outsize importance when near and long-term incentives of the MDP are misaligned. More formally, persistent exploration has been identified in *tabular* MDPs as key to the ability to converge to the optimal policy using first-order methods and avoid spurious behavior. Persistent exploration formally ensures that under any initial distribution over $s_{0}$ in (3.1), the current policy assigns strictly positive likelihood to the optimal action over the entire state space \[Lemma 9\], under which a version of gradient dominance (akin to strong convexity) holds (Lemma 8). Interestingly, these results echo classical persistence of excitation in systems identification. The stumbling block in translating these conditions from finite to continuous spaces is that many common distributions over unbounded continuous space may fail to be integrable if their likelihood is lower bounded away from null.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 3.3 (Lévy Process Policy)", "weight": 1.0} -->

As a step towards satisfying this condition, we seek to ensure that the induced transition dynamics under a policy are heavy-tailed, which increases the likelihood of jumping to cover more of the state space. Doing so may be accomplished by specifying a heavy-tailed policy (Example 3.2. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control") - 3.3. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control")), whose likelihood approaches null slowly while still defining a valid distribution. That continuous space necessitates exploration to eventuate in suitable behavior may be illuminated through the Pathological Mountain Car (PMC) (cf. Fig. 1) introduced next, where a car is between two mountains.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 3.3 (Lévy Process Policy)", "weight": 1.0} -->

Pathological Mountain Car. The environment consists of two goal posts, a less-rewarding goal at $s = 2.667$ with a reward of $10$ and a bonanza at $s = {- 4.0}$ of $500$ units of reward.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 3.3 (Lévy Process Policy)", "weight": 1.0} -->

In Fig. 1, it is possible to get stuck at the lower peak and never reach the jackpot without sufficient exploration. Its potential pitfalls are illuminated experimentally in Sec. 6.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 3.3 (Lévy Process Policy)", "weight": 1.0} -->

With the motivation clarified, we shift to illuminating that heavy-tailed policies, while encouraging actions far from the mean, may cause policy search directions to possibly be unbounded and non-smooth. These issues are the focus of Section 4.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

Policy gradient (PG) is an RL algorithm in which policy parameters in ${\mathbb{R}}^{d}$ are iteratively updated as approximate gradient ascent with respect to the value function (3.1).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption 2 is weaker than the standard almost-sure boundedness of the score function assumed in prior work, which is restrictive, and not valid even for Gaussians (Example 3.1. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control")). To see this, write the norm of its score function as ${\|{{{\nabla_{\mathbf{θ}}\log}\pi_{\mathbf{θ}}}{(s,a)}}\|} \leq {\mathcal{O}\left( {{\| a\|} + {\| a\|}^{2}} \right)}$, which grows unbounded when the support of the action space is infinite. The score function also is unbounded in Example 3.2. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control"). These subtleties motivate the relaxed condition in Assumption 2 which is valid regardless of a policy's tail index (Examples 3.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control") - 3.3. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control")).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Next, we shift towards detailing PG. Under Assumptions 1 - 2, we establish that the integral in (4.1) is finite (Lemma 4 ‣ A Technical Details of Policy Search ‣ Part I Appendix ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control") in Appendix A.1 ‣ A Technical Details of Policy Search ‣ Part I Appendix ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control")). Thus, we employ it to compute search directions, which requires unbiased estimates of (4.1).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

where the parameter update for ${\mathbf{θ}}_{k}$ is defined according to stochastic gradient ascent with step-size $\eta > 0$. The procedure for policy search along a trajectory is summarized as Algorithm 1, where in the pseudo-code, we permit mini-batching with batch-size $B_{k}$, but subsequently assume $B_{k} = 1$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

1: Initialize: policy parameters θ0, discount γ, step-size η, gradient g0 = 0, starting point (s0,a0) Repeat for k = 1, …
2: Starting from (s0,a0), generate Bk trajectories τk, i = (s0,a0,s1,a1,… sTk, i,aTk, i) of length Tk, i ∼ Geom (1−γ1/2) with actions au ∼ πθk(.|su)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Algorithm 1 Heavy-tailed Policy Gradient (HPG)

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Next, we establish that the stochastic gradient ${\hat{\nabla}}_{\mathbf{θ}}J{({\mathbf{θ}})}$ is an unbiased estimate of the true gradient ${\nabla_{\mathbf{θ}}J}{({\mathbf{θ}})}$ for a given $\mathbf{θ}$. As previously mentioned, almost sure boundedness of the score function ${{\nabla_{\mathbf{θ}}\log}\pi_{\mathbf{θ}}}{(\left. a \middle| s \right.)}$ does not even hold for the Gaussian (Example 3.1. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control")), which motivates the moment condition in Assumption 2. This alternate condition is employed to establish unbiasedness of (4.2) formalized next (see Appendix A.2 for proof).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Observe that the policy parameterization in Example 3.2. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control") is not Lipschitz but Hölder continuous. In the next section, we formalize the convergence of (4.2), discerning the convergence rate to stationarity and metastability characteristics: the proportion of time the algorithm's limit points spent at wider versus narrower local extrema as a function of the tail index.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

We analyze the ability of PG \cf. ([4.2)\] to maximize the value function (3.2). As $J{({\mathbf{θ}})}$ is non-convex in the policy parameter $\mathbf{θ}$, the best pathwise result one may hope for is convergence to stationarity unless additional structure is present. Thus, we first study sample complexity in terms of the rate of decrease of the expected gradient norm ${\mathbb{E}}{\lbrack{\|{{\nabla J}{({\mathbf{θ}}_{k})}}\|}\rbrack}$, which we pursue under Assumptions 2-3 regarding the integrability of the norm of the score function with respect to the policy and Hölder continuity. This generality is necessitated by heavy-tailed policy parameterizations as previously mentioned, and has not been considered in prior works such as.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Assumptions 2-3 present unique confounders to the RL setting that do not manifest in vanilla stochastic programming under relaxed smoothness conditions. Specifically, they cause integrability and smoothness complications with respect to the occupancy measure $\rho_{\mathbf{θ}}{(s,a)}$ induced by the MDP, which upends conditions on the objective and policy gradient in existing analyses. These complications are overcome in Lemmas 2 - 3, which first require partitioning the action space into sets where the score function is and is not almost surely bounded according to an exploration tolerance parameter (Definition 5.1), which is unique to this work. Next, we make precise this discussion, establishing the convergence rate to stationarity of (4.2). Later in this section, we formalize that iterates escape narrow extrema, and tend to jump towards wider peaks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Attenuation Rate of the Expected Gradient Norm", "weight": 1.0} -->

We first focus on convergence rates to stationarity. To do so, we begin by establishing that Assumption 3 regarding the Hölder continuity of the score function implies approximate Hölder continuity on the overall policy gradient. First, we partition the action space according to when the score function is almost surely bounded and where it is integrable according via a constant $\lambda > 0$ defined next.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

In the previous subsection, we established that the attenuation rate of the expected gradient norm for heavy-tailed policies is actually *slower* than the rate associated smoother policies. This fact seemingly contradicts prior experimental results which demonstrate that they tend towards policies that achieve higher reward more quickly. The nature of this confounder has to do with the fact that expected gradient norm may only characterize how close a policy is to stationarity, but not how quickly a policy moves from one stationary point to another.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

To make sense of this quandary, we turn to characterizing (i) the time that Algorithm 1 takes to escape a (possibly spurious) local extremum, and (ii) how the proportion of time spent at a local maxima depends on its width and the policy's tail index. These results hinge upon introducing into RL for the first time of *metastability* of dynamical systems under the influence of weak random perturbations. Similar results have been employed for SGD in the context of training neural networks in supervised learning; however, it is unclear how one neural parameterization induces gradient noise whose distribution has a heavier from another. By contrast, here, this aspect is directly determined by the policy parameterization's tail index, which *we choose* in Algorithm 1. Moreover, in the aforementioned works, the analysis is only for the scalar-dimensional case, whereas here we consider dimension $d > 1$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

We begin then by rewriting (4.2) in terms of the true policy gradient and the stochastic error ${\hat{\nabla}J{({\mathbf{θ}}_{k})}} - {{\nabla J}{({\mathbf{θ}}_{k})}}$, with the noise process hypothesized as an $\alpha$-tailed distribution, given by

<!-- chunk {"id": "body-0047", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

where, $S_{k} \in {\mathbb{R}}^{d}$ is $\mathcal{S}\alpha\mathcal{S}$ distributed random vector. Subsequently, we impose that the score function \cf. ([4.1)\] is dissipative (Assumption 6).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

Hereafter, we rewrite discrete-time process ${\mathbf{θ}}_{k}$ as ${\mathbf{θ}}^{k}$ with superscript to disambiguate between continuous and discrete time. (5.6) holds under a hypothesis that the stochastic errors associated with policy gradient steps are heavy-tailed, which is observed experimentally. In Sec. 6, we experimentally corroborate that policies induce gradient noise with a proportionate tail index (Fig. 2).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

Exit time (Def. 5.3)
Trans. time (Def. 5.4)

<!-- chunk {"id": "body-0050", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

The continuous-time analogue of (5.6), i.e., ${({{\mathbf{θ}}_{k + 1} - {\mathbf{θ}}_{k}})}/\eta$ as $\eta\rightarrow 0$, defines Stochastic Differential Equation (SDE) driven by an $\alpha -$stable Lévy process as

<!-- chunk {"id": "body-0051", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

where, $\epsilon:=\eta^{\frac{\alpha - 1}{\alpha}}$ is a coefficient of the jump process (similar to diffusion coefficient in Brownian motion), and $\mathbf{L}_{t}^{\alpha}$ denotes the multi-dimensional $\alpha$-stable Lévy motion in ${\mathbb{R}}^{d}$. With these details in place, we impose some additional structure (Assumption 4) on the non-convex landscape of the objective $J{({\mathbf{θ}})}$ in (3.1), namely, within the region of the objective's assumed finitely many local maxima, each one is separated by only a local minimum and no saddle points.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

where, ${a,\xi} > 0$ are scalar radius parameters, and $\partial\mathcal{G}_{i}$ denotes the boundary of this neighborhood.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Metastability and Convergence to Wide Peaks", "weight": 1.0} -->

Exit Time and Transition Time. We next define the metastability quantities of exit and transition time in both continuous and discrete-time, assuming that (5.7) and (5.6) are initialized at ${\mathbf{θ}}_{0} \in \mathcal{G}_{i}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

We also first present an additional condition we require on the score function.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

We impose the following structural assumption on $\mathcal{G}_{i}$ \cf. ([5.8)\] such that desired properties for a domain perturbed by a Lévy noise in multi-dimensional space holds Imkeller et al..

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 7", "weight": 1.0} -->

Local extrema, ${\overline{\mathbf{θ}}}_{i}$ is an attractor of the domain, i.e. for every starting value ${\mathbf{θ}} \in \mathcal{G}_{i}$, the deterministic solution vanishes asymptotically.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Assumption 7", "weight": 1.0} -->

Assumption 4 is regarding the level sets of the value function within the vicinity of stationary points versus local extrema. Assumption 4.1 ensures that there is positive volume separating distinct extrema, which imposes that the value function, and hence reward, cannot be extremely similar for policies whose relative merits are different. Observe that the strict saddle property (Assumption 4.2) has been studied before in the context of policy gradient method, as it is a sufficient condition for the correlated negative curvature condition Zhang et al., which holds whenever the policy parameterization is associated with a positive definite Fischer information matrix, and the reward function is strictly positive or strictly negative. Assumption 4.3 is easy to satisfy for any policy that does not threshold large values of the derivative, such as the Gaussian or Cauchy -- direct calculation reveals that it holds for these cases, but it does not hold for a *truncated* Gaussian.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Assumption 7", "weight": 1.0} -->

Assumption 5 imposes conditions on the Lévy processes that drive the heavy-tailed noise. Theoretically they are difficult to verify, but we note that they are strictly more general than standard assumptions in the ODE analysis of stochastic approximation that underlies the stability analysis of reinforcement learning -- see Borkar and Meyn. Moreover, we empirically verify that the noise satisfies the conditions required to be jump process with index $\alpha$ in Figure 2, due to the fact that if the gradient is heavy tailed, then the noise associated with the stochastic errors is heavy-tailed.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Assumption 7", "weight": 1.0} -->

Assumption 6 holds for any policy parameterization which is an increasing function of the norm. Observe that it holds for the policy in Example 3.2. ‣ 3 Markov Decision Problems ‣ On the Sample Complexity and Metastability of Heavy-tailed Policy Search in Continuous Control") directly when the policy parameter $\theta$ lies in compact space. Assumption 7 imposes structure on the landscape of the value function. Assumption 7.2 imposes that the gradient is negatively correlated with the normal vector pointing away from a neighborhood of a stationary point, which usually holds. Assumption 7.3 ensures that the gradient is null near a local extrema, i.e., the policy gradient becomes null at a local extrema. Assumption 7.4 imposes that there is some intersection between the neighborhoods of extrema, which means that one locally optimal policy may have similar cumulative return to another of comparable quality. Assumption 7.5 imposes that the transition time between the neighborhoods of local extrema is governed by choice of learning rate up to a constant factor, which typically holds in practice.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Assumption 7", "weight": 1.0} -->

The following theorems present the first exit time and transition time probabilities of the proposed heavy-tailed policy gradient setting, (4.2) when initialized within $\mathcal{G}_{i} \subset {\mathbb{R}}^{d}$ such that (5.8) holds.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate the proposed HPG (Algorithm 1) as compared to some common approaches for policy search. Before doing so, we demonstrate experimentally evidence that the heavy-tailed policies results in heavy tailed policy gradients. Then, we provide experiments for the Pathological Mountain Car (PMC) (Sec. 3) and 1D Mario environment Matheron et al.. For PMC, we consider an incentive structure in which the amount of energy expenditure, i.e., the action squared, at each time-step is negatively penalized and the reward structure is given by

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experiments", "weight": 1.0} -->

Here, $s$ denotes the state space, and the action $a_{t}$ is a one-dimensional scalar representing the speed of the vehicle ${\overset{˙}{s}}_{t}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experiments", "weight": 1.0} -->

In 1D Mario environments, state $s \in {\lbrack{- 4.0},\, 3.709\rbrack}$ and the actions are confined to $\lbrack{- 20},\, 20\rbrack$. On the other hand, as the name suggests, the 1D Mario environment is one-dimensional with continuous state and action spaces with incentive structure and state transition defined as ${r{(s_{t},a_{t})}} = \mathbb{1}_{\{{{s_{t} + a_{t}} < 0}\}}$, and $s_{t + 1} = {\min{\{ 1,{\max{\{ 0,{s_{t} + a_{t}}\}}}\}}}$ where, state, $s \in {\lbrack 0,1\rbrack}$ and action $a \in {\lbrack{- 0.1},0.1\rbrack}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experiments", "weight": 1.0} -->

Before presenting the experiments, first in Fig. 2, we depict the estimation of tail index $\alpha$ (using method in Mohammadi et al. ) for gradient estimates \cf. ([4.2)\] with a Cauchy and Gaussian policy. The lower the value of $\alpha$ the heavier the tail is of the policy gradient. In Fig. 2(a), we observe that the average estimate for the Gaussian policy settles to a value of one, while the corresponding value for Cauchy values settles around $0.2$ for 1D Mario environment. A similar plot for PMC is in Fig. 2(b): note that the tail-index estimate of Cauchy settles around unity and the corresponding value for Gaussian exhibits volatility since the policy has yet to converge. For the tail index estimation, we utilized the logic presented in Mohammadi et al. for the $\alpha$ estimation reiterated here in the form of Theorem 6.1 for quick reference.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We focused on PG method in infinite-horizon RL problems. Inspired by persistent exploration that mitigates the tendency of policies to become mired at spurious behavior, we sought to nearly satisfy it in continuous settings through heavy-tailed policies. Doing so invalidated several aspects of existing analyses, which motivated studying the sample complexity of policy search when the score function is Hölder continuous and its norm is integrable with respect to the policy, and introducing an exploration tolerance parameter to quantify the degree to which the score function may be unbounded.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Moreover, we established that heavy-tailed policies induce heavy-tailed transition dynamics, which jump away from local extrema as formally quantified by the metastability characteristics of its Lévy process representation. We discerned that policies a heavier tail induce transitions away from a local extrema more quickly than one with a lighter tail, and tend towards extrema with more volume, which we empirically associated with more stable policies for a few RL problems in practice. The characterization of jumps defined by metastability provides a lens through which approximate persistent exploration may be satisfied in continuous space.
