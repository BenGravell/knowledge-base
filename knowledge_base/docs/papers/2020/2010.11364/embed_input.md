<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Efficient Reinforcement Learning with REINFORCE

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy gradient methods are among the most effective methods for large-scale reinforcement learning, and their empirical success has prompted several works that develop the foundation of their global convergence theory. However, prior works have either required exact gradients or state-action visitation measure based mini-batch stochastic gradients with a diverging batch size, which limit their applicability in practical scenarios. In this paper, we consider classical policy gradient methods that compute an approximate gradient with a single trajectory or a fixed size mini-batch of trajectories under soft-max parametrization and log-barrier regularization, along with the widely-used REINFORCE gradient estimation procedure. By controlling the number of "bad" episodes and resorting to the classical doubling trick, we establish an anytime sub-linear high probability regret bound as well as almost sure global convergence of the average regret with an asymptotically sub-linear rate. These provide the first set of global convergence and sample efficiency results for the well-known REINFORCE algorithm and contribute to a better understanding of its performance in practice.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the global convergence rates of the REINFORCE algorithm for episodic reinforcement learning. REINFORCE is a vanilla policy gradient method that computes a stochastic approximate gradient with a single trajectory or a fixed size mini-batch of trajectories with particular choice of gradient estimator, where we use 'vanilla' here to disambiguate the method from more exotic variants such as natural policy gradient methods. REINFORCE and its variants are among the most widely used policy gradient methods in practice due to their good empirical performance and implementation simplicity. Related methods include the actor-critic family and deterministic and trust-region based variants.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The theoretical results for policy gradient methods have, up to recently, been restricted to convergence to local stationary points. Lately, a series of works have established *global* convergence results. These recent developments cover a broad range of issues including global optimality characterization, convergence rates, the use of function approximation, and efficient exploration (for more details, see the related work section, which we defer to Appendix E due to space limits). Nevertheless, prior work on vanilla policy gradient methods either requires exact and deterministic policy gradients or only guarantees convergence up to $\Theta{({1/M^{p}})}$ with a fixed mini-batch size $M > 0$ of trajectories collected when performing a single update (where $p > 0$ is $1/2$ in most cases), while global convergence is only achieved when the batch size $M$ goes to infinity. By contrast, practical implementations of policy gradient methods typically use either a single or a fixed number of sample trajectories, which tends to perform well.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, prior theoretical results (for general MDPs) have used the state-action visitation measure based gradient estimation (see e.g., (Wang et al. 2019, (3.10))), which are typically not used in practice.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main purpose of this paper is to bridge this gap between theory and practice. We do this in two major ways. First, we derive performance bounds for the case of a fixed mini-batch size, rather than requiring diverging size. Second, we remove the need for the state-action visitation measure based gradient, instead using the REINFORCE gradient estimator. It is nontrivial to go from a diverging mini-batch size to a fixed one. In fact, by allowing for an arbitrarily large batch size, existing works in the literature were able to make use of IID samples to decouple the analysis into deterministic gradient descent/ascent and error control of stochastic gradient estimations. In contrast, with a single trajectory or a fixed batch size, such a decoupling is no longer feasible. In addition, the state-action visitation measure based gradient estimations are unbiased and unbounded, while REINFORCE gradient estimations are biased and bounded. Hence a key to the analysis is to deal with the bias while making better use of the boundedness.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our analysis not only addresses these challenges, but also leads to convergence results in almost sure and high probability senses, which are stronger than the expected convergence results that dominate the literature (for vanilla policy gradient methods). We also emphasize that the goal of this work is to provide a deeper understanding of a widely used algorithm, REINFORCE, with little or no modifications, rather than tweaking it to achieve near-optimal performance bounds. Lastly, our analysis is not the complete picture and several open questions about the performance of policy gradient methods remain. We discuss these issues in the conclusion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contribution", "weight": 1.0} -->

Our major contribution can be summarized as follows. We establish the first set of global convergence results for the REINFORCE algorithm. In particular, we establish an anytime sub-linear high probability regret bound as well as almost sure global convergence of the average regret with an asymptotically sub-linear rate for REINFORCE, showing that the algorithm is sample efficient (i.e., with polynomial/non-exponential complexity). To our knowledge, these (almost sure and high probability) results are stronger than existing global convergence results for (vanilla) policy gradient methods in the literature. Moreover, our convergence results remove the non-vanishing $\Theta{({1/M^{p}})}$ term (with $M > 0$ being the mini-batch size of the trajectories and $p > 0$ being some constant exponent) and hence show for the first time that policy gradient estimations with a single or finite number of trajectories also enjoy global convergence properties. Finally, the widely-used REINFORCE gradient estimation procedure is studied, as opposed to the state-action visitation measure based estimators typically studied in the literature but rarely used in practice.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem setting and preliminaries", "weight": 1.0} -->

Below we begin with our problem setting and some preliminaries on MDPs and policy optimization. For brevity we restrict ourselves to the stationary infinite-horizon discounted setting. We briefly discuss potential extensions beyond this setting in §6.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem setting", "weight": 1.0} -->

We consider a finite MDP $\mathcal{M}$, which is characterized by a finite state space $\mathcal{S} = {\{ 1,\ldots,S\}}$, a finite action space $\mathcal{A} = {\{ 1,\ldots,A\}}$, a transition probability $p$ (with $p{(\left. s^{\prime} \middle| {s,a} \right.)}$ being the probability of transitioning to state $s^{\prime}$ given the current state $s$ and action $a$), a reward function $r$ (with $r{(s,a)}$ being the instantaneous reward when taking action $a$ at state $s$), a discount factor $\gamma \in {\lbrack 0,1)}$ and an initial state distribution $\rho \in {\Delta{(\mathcal{S})}}$. Here $\Delta{(\mathcal{X})}$ denotes the probability simplex over a finite set $\mathcal{X}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem setting", "weight": 1.0} -->

A (stationary, stochastic) policy $\pi$ is a mapping from $\mathcal{S}$ to $\Delta{(\mathcal{A})}$. We will use $\pi{(\left. a \middle| s \right.)}$, $\pi{(s,a)}$ or $\pi_{s,a}$ alternatively to denote the probability of taking action $a$ at state $s$ following policy $\pi$. The policy $\pi$ can also be viewed as an $SA$ dimensional vector in

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem setting", "weight": 1.0} -->

Notice that here we use the double indices $s$ and $a$ for notational convenience. We use ${\pi{(s, \cdot )}} \in \text{R}^{A}$ to denote the sub-vector $({\pi{(s,1)}},\ldots,{\pi{(s,A)}})$. We also assume that $r{(s,a)}$ is deterministic for any $s \in \mathcal{S}$ and $a \in \mathcal{A}$ for simplicity, although our results hold for any $r$ with an almost sure uniform bound. Here $r$ can be similarly viewed as an $SA$-dimensional vector. Without loss of generality, we assume that ${r{(s,a)}} \in {\lbrack 0,1\rbrack}$ for all $s \in \mathcal{S}$ and $a \in \mathcal{A}$, which is a common assumption. We also assume that $\rho$ is component-wise positive, as is assumed.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem setting", "weight": 1.0} -->

Given a policy $\pi \in \Pi$, the expected cumulative reward of the MDP is defined as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem setting", "weight": 1.0} -->

Any policy $\pi^{\star} \in {\operatorname{argmax}_{\pi \in \Pi}{F{(\pi)}}}$ is said to be optimal, and the corresponding optimal objective value is denoted as $F^{\star} = {F{(\pi^{\star})}}$. Note that in the literature, $F{(\pi)}$ is also commonly written as $V_{\rho}^{\pi}$ and referred to as the value function. Here we hide the dependency on $\rho$ as it is fixed throughout the paper.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Vanilla policy gradient method and REINFORCE algorithm", "weight": 1.0} -->

When the transition probability $p$ and reward $r$ are fully known, problem reduces to solving an MDP, in which case various classical algorithms are available, including value iteration and policy iteration. In this paper, we consider the episodic reinforcement learning setting in which the agent accesses $p$ and $r$ by interacting with the environment over successive episodes, i.e., the agent accesses the environment in the form of a $\rho$-restart model, which is commonly adopted in the policy gradient literature. In addition, we focus on the REINFORCE algorithm, a representative policy gradient method.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy parametrization and surrogate objectives", "weight": 1.0} -->

Here we consider parametrizing the policy with parameter $\theta \in \Theta$, i.e.,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy parametrization and surrogate objectives", "weight": 1.0} -->

where $\lambda \geq 0$ and $R:{\Theta\rightarrow\text{R}}$ is a differentiable regularization term that improves convergence, to be specified later. Although our ultimate goal is still to solve the original problem this regularized optimization problem is a useful surrogate and our approach will be to tackle problem with progressively smaller $\lambda$ regularization penalties, thereby converging to solving the actual problem we care about.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy gradient method", "weight": 1.0} -->

In each episode $n$, the policy gradient method directly performs an online stochastic gradient ascent update on a surrogate objective $L_{\lambda^{n}}{(\theta)}$, i.e.,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy gradient method", "weight": 1.0} -->

where $\alpha^{n}$ is the step-size and $\lambda^{n}$ is the regularization parameter. Here the stochastic gradient ${\hat{\nabla}}_{\theta}L_{\lambda^{n}}{(\theta^{n})}$ is computed by sampling a single trajectory $\tau^{n}$ following policy $\pi_{\theta^{n}}$ from $\mathcal{M}$ with the initial state distribution $\rho$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy gradient method", "weight": 1.0} -->

We summarize the generic policy gradient method (with single trajectory gradient estimates) in Algorithm 1. An extension to mini-batch scenarios will be discussed in §5. As is always (implicitly) assumed in the literature of episodic reinforcement learning (e.g., cf. ), given the current policy, we assume that the sampled trajectory is conditionally independent of all previous policies and trajectories.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy gradient method", "weight": 1.0} -->

1: Input: initial parameter θ0, step-sizes αn and regularization parameters λn (n ≥ 0).
3: Choose Hn, sample trajectory τn from ℳ following policy πθn, and compute an approximate gradient ${\hat{\nabla}}_{\theta}L_{\lambda^{n}}{(\theta^{n})}$ of Lλn using trajectory τn.
4: Update $\theta^{n + 1} = {\theta^{n} + {\alpha^{n}{\hat{\nabla}}_{\theta}L_{\lambda^{n}}{(\theta^{n})}}}$.
Algorithm 1 Policy Gradient Method with Single Trajectory Estimates

<!-- chunk {"id": "body-0022", "role": "body", "section": "REINFORCE algorithm", "weight": 1.0} -->

There are several ways of choosing the stochastic gradient operator ${\hat{\nabla}}_{\theta}$ in the policy gradient method, and the well-known REINFORCE algorithm corresponds to a specific family of estimators based on the policy gradient theorem (cf. §3). Other common alternatives include zeroth order/random search and actor-critic approximations. One may also choose to parametrize the policy as a mapping from the parameter space to a specific action, which would then result in deterministic policy gradient approximations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "REINFORCE algorithm", "weight": 1.0} -->

Although our main goal is to study the REINFORCE algorithm, our analysis indeed holds for rather generic stochastic gradient estimates. In the next section, we introduce the (mild) assumptions needed for our convergence analysis and the detailed gradient estimation procedures in the REINFORCE algorithm, and then verify that the assumptions do hold for these gradient estimations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Phased learning", "weight": 1.0} -->

To facilitate the exposition below, we divide the optimization in Algorithm 1 into successive phases $l = {0,1,\ldots}$, each with length $T_{l} > 0$. We then fix the regularization coefficient $\lambda_{l}$ within each phase $l \geq 0$. In addition, a post-processing step is enforced at the end of each phase to produce the initialization of the next phase. The resulting algorithm is described in Algorithm 2. Here the trajectory is denoted as $\tau^{l,k} = {(s_{0}^{l,k},a_{0}^{l,k},r_{0}^{l,k},\ldots,s_{H^{l,k}}^{l,k},a_{H^{k,l}}^{l,k},r_{H^{l,k}}^{l,k})}$, and we will refer to $\theta^{l,k}$ as the $(l,k)$-th iterate hereafter.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Phased learning", "weight": 1.0} -->

The post-processing function is required to guarantee that the resulting policy $\pi_{\theta}$ is lower bounded by a pre-specified tolerance $\epsilon_{pp} \in {(0,{1/A}\rbrack}$ to ensure that the regularization is bounded (cf. Algorithm 3 for a formal description and §3.1 for an example realization).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Phased learning", "weight": 1.0} -->

1: Input: initial parameter ${\overset{\sim}{\theta}}^{0,0}$, step-sizes αl, k, regularization parameters λl, phase lengths Tl (l, k ≥ 0) and post-processing tolerance ϵpp ∈ (0, 1/A]. 2: Set $\theta^{0,0} = {\text{PostProcess}{({\overset{\sim}{\theta}}^{0,0},\epsilon_{pp})}}$. 5: Choose Hl, k, sample trajectory τl, k from ℳ following policy πθl, k, and compute an approximate gradient ${\hat{\nabla}}_{\theta}L_{\lambda^{l}}{(\theta^{l,k})}$ of Lλl using trajectory τl, k.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Phased learning", "weight": 1.0} -->

Return θ′ (near θ) such that πθ′ (s,a) ≥ ϵpp for each s, a ∈ 𝒮 × 𝒜.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Performance criteria", "weight": 1.0} -->

The criterion we adopt to evaluate the performance of Algorithm 2 is *regret*. For any $N \geq 0$, the regret up to episode $N$ is defined as the cumulative sub-optimality of the policy over the $N$ episodes. Formally, we define

<!-- chunk {"id": "body-0029", "role": "body", "section": "Performance criteria", "weight": 1.0} -->

${\forall t} \geq 0$, and $\mathbf{E}_{l,k}$ denotes the conditional expectation given the $(l,k)$-th iteration $\theta^{l,k}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Performance criteria", "weight": 1.0} -->

Notice that the regret defined above takes into account the fact that the trajectories are stopped/truncated to have finite horizons $H^{l,k}$, which characterizes the actual loss caused by sampling the trajectories in line 5 of Algorithm 2. A similar regret definition for the episodic (discounted) reinforcement learning setting considered here is adopted. We remark that all our regret bounds remain correct up to lower order terms when we replace ${\hat{F}}^{l,k}$ with $F$ or an expectation-free version.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Performance criteria", "weight": 1.0} -->

Similarly, we also define the single phase version of regret as follows. The regret up to episode $K \in {\{ 0,\ldots,{T_{l} - 1}\}}$ in phase $l$ is defined as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Performance criteria", "weight": 1.0} -->

Notice that and are connected via

<!-- chunk {"id": "body-0033", "role": "body", "section": "Performance criteria", "weight": 1.0} -->

We provide high probability regret bounds in §4. We remark that a regret bound of the form ${{{\mathbf{r}\mathbf{e}\mathbf{g}\mathbf{r}\mathbf{e}\mathbf{t}}{(N)}}/{({N + 1})}} \leq R$ (for some $R > 0$) immediately implies that ${{\min_{{l,k}:{{B_{\mathcal{T}}{(l,k)}} \leq N}}F^{\star}} - {F{(\pi_{\theta^{l,k}})}}} \leq R$, where the latter is also a commonly adopted performance criteria in the literature.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumptions", "weight": 1.0} -->

Here we list a few fundamental assumptions that we require for our analysis.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 1 (Setting)", "weight": 1.0} -->

The first assumption concerns the form of the policy parameterization and the regularization. Notice that the regularization term here can also be seen as a relative entropy/KL regularization (with a uniform distribution policy reference). Such kind of regularization terms are also widely adopted in practice (although typically with variations).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 1 (Setting)", "weight": 1.0} -->

With Assumption 1. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE"), the post-processing function in Algorithm 3 can be for example realized by first calculating $\hat{\pi} = {{\epsilon_{pp}\mathbf{1}} + {{({1 - {A\epsilon_{pp}}})}\pi_{\theta}}}$, and then return $\theta^{\prime}$ with $\theta_{s,a}^{\prime} = {{\log{\hat{\pi}}_{s,a}} + c_{s}}$. Here $\mathbf{1}$ is an all-one vector and $c_{s} \in \text{R}$ ($s = {1,\ldots,S}$) are arbitrary real numbers.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 2 (Policy gradient estimator)", "weight": 1.0} -->

The second assumption requires that the gradient estimates are almost surely bounded, nearly unbiased and satisfy a bounded second-order moment growth condition. This is a slight generalization of standard assumptions in the stochastic gradient descent literature. Additionally, we also require that the trajectory lengths $H^{l,k}$ are at least logarithmically growing in $k$ to control the loss of rewards due to truncation. For notational simplicity, hereafter we omit to mention the trajectory sampling (i.e., $s_{0} \sim \rho,a_{t}^{l,k} \sim \pi_{\theta^{l,k}}{( \cdot |s_{t}^{l,k})},s_{t + 1}^{l,k} \sim p{( \cdot |s_{t}^{l,k},a_{t}^{l,k})},\forall t \geq 0$) when we write down $\mathbf{E}_{l,k}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2 (Policy gradient estimator)", "weight": 1.0} -->

Notice that Assumption 2. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE") immediately holds if ${\hat{\nabla}}_{\theta}L_{\lambda^{l}}{(\theta^{l,k})}$ is unbiased and has a bounded second-order moment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "REINFORCE gradient estimations", "weight": 1.0} -->

Now we introduce REINFORCE gradient estimation with baselines, and specify the hyper-parameters under which the technical Assumption 2. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE") holds, when operating under the setting Assumption 1. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE").

<!-- chunk {"id": "body-0040", "role": "body", "section": "REINFORCE gradient estimations", "weight": 1.0} -->

Here $b:{\mathcal{S}\rightarrow\text{R}}$ is called the baseline, and is required to be independent of the trajectory $\tau^{l,k}$. The purpose of subtracting $b$ from the approximate $Q$-values is to (potentially) reduce the variance of the "plain" REINFORCE gradient estimation, which corresponds to the case when $b = 0$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "REINFORCE gradient estimations", "weight": 1.0} -->

With this we have the following result, the proof of which can be found in the Appendix.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Preliminary tools", "weight": 1.0} -->

We first present some preliminary tools for our analysis.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Non-convexity and control of \"bad\" episodes", "weight": 1.0} -->

One of the key difficulties in applying policy gradient methods to solve an MDP problem towards global optimality is that problem is in general non-convex. Fortunately, we have the following result, which connects the gradient of the surrogate objective $L_{\lambda}$ with the global optimality gap of the original optimization problem.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Doubling trick", "weight": 1.0} -->

The second tool is a classical doubling trick that is commonly adopted in the design of online learning algorithms, which can be used to stitch together the regret over multiple learning phases in Algorithm 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Doubling trick", "weight": 1.0} -->

Notice that Proposition 3). ‣ Non-convexity and control of “bad” episodes. ‣ 4.1 Preliminary tools ‣ 4 Main convergence results ‣ Sample Efficient Reinforcement Learning with REINFORCE") suggests that for any pre-specified tolerance $\epsilon$, one can select $\lambda$ proportional to $\epsilon$ and then run (stochastic) gradient ascent to drive $F^{\star} - {F{(\pi_{\theta})}}$ below the tolerance. To obtain the eventual convergence and regret bound in the long run we apply the doubling trick, which specifies a growing phase length sequence with $T_{l + 1} \approx {2T_{l}}$ in Algorithm 2 and a suitably decaying sequence of regularization parameters ${\{\lambda^{l}\}}_{l = 0}^{\infty}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "From high probability to almost sure convergence", "weight": 1.0} -->

The last tool is an observation that an arbitrary anytime sub-linear high probability regret bound with logarithmic dependency on $1/\delta$ immediately leads to almost sure convergence of the average regret with a corresponding asymptotic rate. Although such an observation seems to be informally well-known in the theoretical computer science community, we provide a compact formal discussion below for self-contained-ness.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Regret analysis", "weight": 1.0} -->

In this section, we establish the regret bound of Algorithm 2, when used with the REINFORCE gradient estimator from §3.2. We begin by bounding the regret of a single phase and then use the doubling trick to combine these into the overall regret bound.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Single phase analysis", "weight": 1.0} -->

We begin by bounding the regret defined in of each phase in Algorithm 2. Note that a single phase in Algorithm 2 is exactly Algorithm 1 terminated in episode $T_{l}$, with $\lambda^{n} = \lambda^{l}$ for all $n \geq 0$ and $\theta^{0} = \theta^{l,0}$. Also notice that for a given phase $l \geq 0$, in order for Theorem 5 below to hold, we actually only need the conditions in Assumption 2. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE") to be satisfied for this specific $l$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Overall regret bound", "weight": 1.0} -->

Now we stitch together the single phase regret bounds established above to obtain the overall regret bound of Algorithm 2, with the help of the doubling trick. This leads to the following theorem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Extension to mini-batch updates", "weight": 1.0} -->

We now consider extending our previous results to mini-batch settings, by modifying Algorithm 2 as follows. Firstly, in each inner iteration, instead of sampling only one trajectory in line 5, we sample $M \geq 1$ independent trajectories $\tau_{1}^{l,k},\ldots,\tau_{M}^{l,k}$ from $\mathcal{M}$ following policy $\pi_{\theta^{l,k}}$ and then compute an approximate gradient ${\hat{\nabla}}_{\theta}^{(i)}L_{\lambda^{l}}{(\theta^{l,k})}$ ($i = {1,\ldots,M}$) using each of these $M$ trajectories. We then modify the update in line 6 as

<!-- chunk {"id": "body-0051", "role": "body", "section": "Extension to mini-batch updates", "weight": 1.0} -->

See Algorithm 4 in Appendix D for a formal description of the modified algorithm.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Regret with mini-batches", "weight": 1.0} -->

where ${(l_{N,M},k_{N,M})} = {G_{\mathcal{T}}{({\lfloor{N/M}\rfloor})}}$ and ${\hat{F}}^{l,k}{(\pi_{\theta^{l,k}})}$ is the same as. The above definition accounts for the fact that each of the $M$ episodes in an inner iteration/step $(l,k)$ corresponds to the same iterate $\theta^{l,k}$ and hence has the same contribution to the regret. The second term on the right-hand side accounts for the contribution of the (remaining) $N - {M{\lfloor{N/M}\rfloor}}$ episodes (among a total of $M$ episodes) in inner iteration/step $(l_{N,M},k_{N,M})$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Regret with mini-batches", "weight": 1.0} -->

Then the following regret bound can be established.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and open problems", "weight": 1.5} -->

In this work, we establish the global convergence rates of practical policy gradient algorithms with a fixed size mini-batch of trajectories combined with REINFORCE gradient estimation.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and open problems", "weight": 1.5} -->

Although in §4 and §5, we only instantiate the bounds for the REINFORCE gradient estimators, we note that our general results (in particular, Theorem 10. ‣ B.3 Overall regret bound for general policy gradient estimators ‣ Appendix B Proofs for convergence analysis ‣ Sample Efficient Reinforcement Learning with REINFORCE") in Appendix B.3) can be easily applied to other gradient estimators (e.g., actor-critic and state-action visitation measure based estimators) as well, as long as one can verify the existence of the constants in Assumption 2. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE") in a similar way to Lemma 2. In addition, one can also easily derive sample complexity results as by-products of our analysis.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion and open problems", "weight": 1.5} -->

In fact, our proof of Theorem 5 immediately implies a $\overset{\sim}{O}{({1/\epsilon^{4}})}$ sample complexity bound (for Algorithm 1 with REINFORCE gradient estimators and a constant regularization parameter) for any pre-specified tolerance $\epsilon > 0$, where we use $\overset{\sim}{O}$ to indicate the big-$O$ notation with logarithmic terms suppressed. We have focused only on regret in this paper mainly for clarity purposes.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and open problems", "weight": 1.5} -->

It is also relatively straightforward to extend our results to finite horizon non-stationary settings, in which the soft-max policy parametrization will have a dimension of $SAH$ and different policy gradient estimators can be adopted (without trajectory truncation), with $H$ being the horizon of each episode. In this case, it's also easy to rewrite the regret bound as a function of the total number of time steps $T \leq {HN}$, where $N$ is the total number of episodes. Other straightforward extensions include refined convergence to stationary points (in both almost sure and high probability senses and with no requirement on large batch sizes), and inexact convergence results when $\delta^{l,k}$ (cf. Assumption 2. ‣ 3.1 Assumptions ‣ 3 Assumptions and REINFORCE gradients ‣ Sample Efficient Reinforcement Learning with REINFORCE")) is not square summable (e.g., when $H^{l,k}$ is fixed or not growing sufficiently fast).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion and open problems", "weight": 1.5} -->

There are also several open problems that may be resolved by combining the techniques introduced in this paper with existing results in the literature. Firstly, it would be desirable to remove the "exploration" assumption that the initial distribution $\rho$ is component-wise positive. This may be achieved by combining our results with the policy cover technique in or the optimistic bonus tricks. Secondly, the bounds in our paper are likely far from optimal (i.e., sharp). Hence it would be desirable to either refine our analysis or apply our techniques to accelerated policy gradient methods (e.g., IS-MBPG ) to obtain better global convergence rates and/or last-iterate convergence. Thirdly, it would be very interesting to see if global convergence results still hold for REINFORCE when the relative entropy regularization term used in this paper is replaced with the practically adopted entropy regularization term in the literature. The answer is affirmative when exact gradient estimations are available, but it remains unknown how these results might be generalized to the stochastic settings in our paper. We conjecture that entropy regularization leads to better global convergence rates and can help us remove the necessity of the PostProcess steps in Algorithm 2 as they are uniformly bounded.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion and open problems", "weight": 1.5} -->

Finally, one may also consider relaxing the uniform bound assumption on the rewards $r$ to instead being sub-Gaussian, introducing function approximation, and extending our results to natural policy gradient and actor-critic methods as well as more modern policy gradient methods like DPG, PPO and TRPO.
