<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Role of Baselines in Policy Gradient Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the effect of baselines in on-policy stochastic policy gradient optimization, and close the gap between the theory and practice of policy optimization methods. Our first contribution is to show that the state value baseline allows on-policy stochastic natural policy gradient (NPG) to converge to a globally optimal policy at an O(1/t) rate, which was not previously known. The analysis relies on two novel findings: the expected progress of the NPG update satisfies a stochastic version of the non-uniform Łojasiewicz (NŁ) inequality, and with probability 1 the state value baseline prevents the optimal action's probability from vanishing, thus ensuring sufficient exploration. Importantly, these results provide a new understanding of the role of baselines in stochastic policy gradient: by showing that the variance of natural policy gradient estimates remains unbounded with or without a baseline, we find that variance reduction cannot explain their utility in this setting. Instead, the analysis reveals that the primary effect of the value baseline is to \textbf{reduce the aggressiveness of the updates} rather than their variance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

That is, we demonstrate that a finite variance is not necessary for almost sure convergence of stochastic NPG, while controlling update aggressiveness is both necessary and sufficient. Additional experimental results verify these theoretical findings.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The policy gradient (PG) is a key concept in reinforcement learning (RL), lying at the foundation of policy-based and actor-critic methods, and responsible for some of the most prominent practical achievements in RL. However, progress in the theoretical understanding of PG methods is recent, and a number of the techniques used in practice still lack rigorous support, particularly in the online stochastic regime where an action is sampled from the current policy at each iteration. We study stochastic policy optimization in more detail to close this gap between theory and practice.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In stochastic policy optimization, the two most common techniques for improving the basic algorithm are to include on-policy importance sampling (IS) and subtract a baseline. Including on-policy IS provides unbiased gradient estimates, but introduces high variance when an action's sampling probability is close to $0$. Meanwhile, subtracting a baseline remains a heuristic that has strong empirical but limited theoretical support. One possible benefit of a baseline is that it provides variance reduction, which has motivated work on designing alternative baselines that further reduce variance. However, other work has shown that variance reduction is not necessarily aligned with policy learning quality. To date, it has remained unclear how a baseline impacts the quality of the ultimate solution found by policy gradient optimization. We resolve this question in this work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress in the theory of deterministic PG has shown that, given exact gradients, softmax policy gradient is able to converge to a globally optimal policy at a $O{({1/t})}$ rate. Unfortunately, despite this guarantee, the constants in this rate can be extremely large due to initialization sensitivity and poor performance at escaping sub-optimal plateaus. Therefore, in the exact gradient setting, several techniques have been considered for mitigating the weaknesses of softmax PG, leading to better constants or even exponentially faster rates of $O{(e^{- {c \cdot t}})}$ for $c > 0$. Such improvements include adding entropy regularization, normalizing the gradients, or applying natural policy gradient (NPG).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, in the on-policy stochastic optimization case, recent studies show that naively applying the above techniques, such as normalization or NPG, leads to unexpectedly *worse* performance than stochastic PG. That is, techniques that accelerate convergence in the exact policy gradient setting become *unsound* in the stochastic gradient setting, by inducing a non-zero probability of failure (i.e., failing to converge to a globally optimal solution). Such failures occur even when stochastic PG can still converge to a global optimum in probability. Previous work has indicated that one key reason behind the failure of these acceleration strategies arises from their "over-committal behaviour" in the stochastic setting, which occurs independently of the variance of the gradient estimates. That is, baseline techniques with higher variance can still better avoid over-committal behaviour (i.e., premature convergence) and ultimately achieve better policy optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To resolve this issue, we develop a deeper understanding of the role of baselines in stochastic policy optimization based on the following contributions. First, we establish a new result that combining on-policy IS with a value function baseline and natural policy gradient (NPG) can achieve almost sure convergence to a globally optimal policy at a $O{({1/t})}$ rate. This result is based on two novel findings: (i) At any iteration $t$, the conditional expected progress of the algorithm's next iterate obeys a stochastic non-uniform Łojasiewicz (NŁ) inequality. (ii) The use of the state value baseline (with appropriate learning rate control) almost surely prevents the probability of the optimal action from vanishing. These findings show that a key role of the value baseline is to automatically ensure "sufficient exploration" during on-policy stochastic optimization. Next, we provide a detailed understanding of how baselines modulate the circular interaction between stochastic action sampling and updating. Although a baseline has no effect on exact gradients, it can play a major role in stochastic gradients.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this respect, we first show that the PG estimator variance is unbounded with or without a baseline, hence variance reduction cannot be the primary effect. Instead, our analysis reveals that the key role the baseline plays in ensuring global convergence is to reduce the aggressiveness of updates. That is, finite variance of the gradient estimates is not necessary for ensuring global convergence, while properly controlling update aggressiveness is both necessary and sufficient.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. Section 2 provides the main results that establish the almost sure $O{({1/t})}$ convergence rate of stochastic NPG with on-policy IS and state value baseline to a globally optimal policy. Section 3 then develops the new understanding of the role of the baseline by going beyond standard variance reduction arguments. Section 4 provides some simulations to verify the results, and Section 5 concludes the paper with a brief discussion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "On-policy Stochastic Natural Policy Gradient", "weight": 1.0} -->

We first consider a one-state Markov Decision Process (MDP) defined by a finite action space ${\lbrack K\rbrack} ≔ {\{ 1,2,\ldots,K\}}$ where the true mean reward vector is $r \in {\lbrack 0,1\rbrack}^{K}$. The policy optimization problem is to maximize the expected reward,

<!-- chunk {"id": "body-0012", "role": "body", "section": "On-policy Stochastic Natural Policy Gradient", "weight": 1.0} -->

where the policy $\pi_{\theta}$ is parameterized by $\theta$ using the standard softmax parameterization,

<!-- chunk {"id": "body-0013", "role": "body", "section": "On-policy Stochastic Natural Policy Gradient", "weight": 1.0} -->

Our focus in this paper is on on-policy optimization, where at each iteration $t \geq 1$ the current policy $\pi_{\theta_{t}}$ is used to sample one action and perform one update.

<!-- chunk {"id": "body-0014", "role": "body", "section": "On-policy Stochastic Natural Policy Gradient", "weight": 1.0} -->

For the sampled action $a_{t}$, a noisy reward observation ${x_{t}{(a_{t})}} \in {\mathbb{R}}$ is drawn from an unknown distribution with expected value $r{(a_{t})}$. We make the following assumption that the observed reward $x_{t}{(a)}$ is sampled from a bounded distribution: ${x_{t}{(a)}} \in {\lbrack{- R_{\max}},R_{\max}\rbrack}$ with probability one.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1 (Bounded sampled reward)", "weight": 1.0} -->

For each action $a \in {\lbrack K\rbrack}$, the true mean reward $r{(a)}$ is the expectation of a bounded reward distribution, i.e.,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1 (Bounded sampled reward)", "weight": 1.0} -->

where $\mu$ is a finite measure over $\lbrack{- R_{\max}},R_{\max}\rbrack$, and ${P_{a}{(x)}} \geq 0$ is the probability density function with respect to $\mu$, and $R_{\max} > 0$ is the reward range. We let $R_{a}$ denote the reward distribution for action $a$ defined by the density $P_{a}$ and base measure $\mu$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1 (Bounded sampled reward)", "weight": 1.0} -->

Then, given a sampled reward observation ${x_{t}{(a)}} \sim R_{a}$, an unbiased estimate of the expected reward vector $r$ can be formed by on-policy importance sampling (IS).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Failure Without a Baseline", "weight": 1.0} -->

First, to establish context, we review an existing negative result for the representative algorithm, natural policy gradient (NPG), which for the softmax parameterization is defined as follows.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Update 1 (NPG with on-policy stochastic gradient)", "weight": 1.0} -->

It is known that NPG behaves problematically with on-policy IS, even if the true mean reward $r{(a_{t})}$ is observed. In particular, NPG converges to a sub-optimal deterministic policy with a constant positive probability in this case, as shown.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Global Convergence with a Value Baseline", "weight": 1.0} -->

Despite the above failure, we now prove that subtracting a value baseline rectifies the problem for NPG. Consider the modified update that includes a baseline.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Update 2 (NPG, on-policy stochastic gradient with value baseline)", "weight": 1.0} -->

Since ${{softmax}{(\theta)}} = {{softmax}{({\theta + {c \cdot \mathbf{1}}})}}$ for all $c \in {\mathbb{R}}$, Update 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") is equivalent to the following update if ${\hat{r}}_{t}$ is by Definition 1). ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"). Given the same $\pi_{\theta_{t}}$, Updates 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") and 3 produce the same next policy $\pi_{\theta_{t + 1}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Update 3", "weight": 1.0} -->

Unfortunately, the variance of this update is not uniformly bounded whenever $\pi_{\theta_{t}}{(a)}$ is close to $0$ for at least one action $a \in {\lbrack K\rbrack}$ (Proposition 3. ‣ 3.1 Baselines Do Not Control Update Variance in NPG ‣ 3 Understanding Baselines in On-policy Stochastic Policy Optimization ‣ The Role of Baselines in Policy Gradient Optimization")), therefore standard stochastic gradient analysis for bounded variance estimators cannot be applied. Instead, we develop two new techniques to establish global convergence results, both of which rely heavily on using baselines.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Update 3", "weight": 1.0} -->

Lemma 1). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") provides the first key technique, which we refer to as the stochastic NŁ inequality.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We have $\eta \in {O{({1/t})}}$ in Eq. 6 ‣ Lemma 1 (Stochastic non-uniform Łojasiewciz (NŁ)). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") after knowing the convergence rate later.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We refer to $\pi_{\theta_{t}}{(a^{\ast})}^{2}$ in Eq. 8 ‣ Lemma 1 (Stochastic non-uniform Łojasiewciz (NŁ)). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") the stochastic NŁ coefficient. Lemma 1). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") is a stochastic generalization of the NŁ inequality, which has been widely used in proving global convergence of softmax PG variants. It is stochastic since Eq. 7 ‣ Lemma 1 (Stochastic non-uniform Łojasiewciz (NŁ)). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") contains an expectation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1", "weight": 1.0} -->

It is non-uniform because Eq. 8 ‣ Lemma 1 (Stochastic non-uniform Łojasiewciz (NŁ)). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") depends on $\theta_{t}$, which cannot be uniformly lower bounded away from $0$ across the entire domain of $\theta \in {\mathbb{R}}^{K}$ (that is, one can always find $\theta$ such that $\pi_{\theta}{(a^{\ast})}$ is arbitrarily close to $0$).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The key idea of Lemma 1). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") is as follows. If ${\hat{r}}_{t}$ is from Definition 2). ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), then by algebra we have,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Since ${\left( {e^{c \cdot y} - 1} \right) \cdot y} \geq 0$ for all $y \in {\mathbb{R}}$ and $c > 0$, Eq. 9 is non-negative (letting $y ≔ {{r{(i)}} - {\pi_{\theta_{t}}^{\top}r}}$ and $c ≔ {\eta/{\pi_{\theta_{t}}(i)}}$). However, this is not true if ${\hat{r}}_{t}$ is from Definition 1). ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), where we have,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Similar things happen for a "bad" action (${{r{(i)}} - {\pi_{\theta_{t}}^{\top}r}} < 0$) with "good" sampled reward (${x - {\pi_{\theta_{t}}^{\top}r}} > 0$). It is then necessary to use $\eta$ like Eq. 6 ‣ Lemma 1 (Stochastic non-uniform Łojasiewciz (NŁ)). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), to control the non-linear sigmoid-like functions in the progress by piecewise linear functions (Lemma 15. ‣ Appendix E Miscellaneous Extra Supporting Results ‣ The Role of Baselines in Policy Gradient Optimization")) to get non-negative expected progresses. According to Eq. 8 ‣ Lemma 1 (Stochastic non-uniform Łojasiewciz (NŁ)).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), we have

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

which implies that LABEL:{update_rule:softmax_natural_pg_special_on_policy_stochastic_gradient_value_baseline} achieves non-negative progress in expectation. Combining Lemma 1). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") with Doob's supermartingale convergence theorem then leads to the following result.

<!-- chunk {"id": "body-0032", "role": "body", "section": "General MDPs", "weight": 1.0} -->

Next, we generalize these results to finite Markov decision processes (MDPs). Given a finite set $\mathcal{X}$, let $\Delta{(\mathcal{X})}$ denote the set of all probability distributions on $\mathcal{X}$. A finite MDP is defined as a tuple $\mathcal{M} ≔ {(\mathcal{S},\mathcal{A},r,\mathcal{P},\gamma)}$, where $\mathcal{S}$ and $\mathcal{A}$ are finite state and action spaces, respectively. $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is the expected reward function, $\mathcal{P}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$ is the probability transition function, and $\gamma \in {\lbrack 0,1)}$ is the discount factor.

<!-- chunk {"id": "body-0033", "role": "body", "section": "General MDPs", "weight": 1.0} -->

We also extend 1. ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") to every ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$ and assume there is a reward distribution $R_{s,a}$ with expectation $r{(s,a)}$, uniformly bounded within $\lbrack{- R_{\max}},R_{\max}\rbrack$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "General MDPs", "weight": 1.0} -->

The policy optimization problem for a general MDP is to maximize the expected value of the policy,

<!-- chunk {"id": "body-0035", "role": "body", "section": "General MDPs", "weight": 1.0} -->

For a general MDP, we assume the initial state distribution $\mu$ is "sufficiently exploratory".

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2 (Sufficient exploration)", "weight": 1.0} -->

At iteration $t$, the NPG method uses the current state distribution to sample one state $s_{t} \sim {d_{\mu}^{\pi_{\theta_{t}}}{( \cdot )}}$, then uses on-policy sampling to sample one action $a_{t} \sim \pi_{\theta_{t}}{( \cdot |s)}$. For the sampled state action pair ${(s_{t},a_{t})} \in {\mathcal{S} \times \mathcal{A}}$, the state-action value $Q^{\pi_{\theta_{t}}}{(s_{t},a_{t})}$ is then used to perform update. The current state value function $V^{\pi_{\theta_{t}}}{(s_{t})}$ is used as the baseline, as shown in Algorithm 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 2 (Sufficient exploration)", "weight": 1.0} -->

Algorithm 1 NPG, on-policy stochastic natural gradient

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2 (Sufficient exploration)", "weight": 1.0} -->

According to the performance difference lemma, we have,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2 (Sufficient exploration)", "weight": 1.0} -->

where the inner summation over actions is similar to $\left( {\pi_{\theta_{t + 1}} - \pi_{\theta_{t}}} \right)^{\top}r$ in one-state MDPs. This connection allows us to generalize Lemma 1). ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") to the following result.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Understanding Baselines in On-policy Stochastic Policy Optimization", "weight": 1.0} -->

Section 2 shows that using a value function baseline in on-policy stochastic NPG can ensure convergence to a globally optimal policy. However, the mechanism behind this finding requires further elucidation. Preliminary studies have observed that subtracting a baseline can reduce the committal behavior of PG-based estimators, suggesting that this effect might be more important than variance reduction. A mathematical characterization of "committal behavior" is from using the following concept of "committal rate".

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baselines Do Not Control Update Variance in NPG", "weight": 1.0} -->

We begin from the well known result that value baselines have no effect on exact policy gradients.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Coupled Sampling and Updating", "weight": 1.0} -->

In on-policy stochastic policy optimization, sampling and updating are coupled as shown in Figure 1. At iteration $t$, the data collected depends on the current policy, since on-policy sampling is used $a_{t} \sim {\pi_{\theta_{t}}{( \cdot )}}$, while the policy is updated from the observations collected based on $a_{t}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Coupled Sampling and Updating", "weight": 1.0} -->

This coupling introduces complexity in the optimization process as well as in the analysis. However, this coupling is also fundamental to understanding the circular interaction created by any on-policy stochastic optimization method. That is, on-policy stochastic optimization faces an exploration-exploitation dilemma: a learning algorithm can improve the policy and increase the probability of choosing actions that yield higher rewards (exploitation), but it must not do so too aggressively lest it fail to identify possibly higher-reward actions (exploration). Striking a proper balance between exploration and exploitation is key to achieving good convergence properties. Different levels of update aggression create different circular effects between sampling and updating, which is central to determining almost sure convergence to a global optimum.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The \"Vicious Circle\" of Being Too Aggressive", "weight": 1.0} -->

First we illustrate a negative effect, the "vicious circle" of being too aggressive.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The \"Virtuous Circle\" of Not Being Too Aggressive", "weight": 1.0} -->

Next, we demonstrate a positive effect, the "virtuous circle" of not being too aggressive.

<!-- chunk {"id": "body-0046", "role": "body", "section": "How a State Value Baseline Reduces Update Aggressiveness", "weight": 1.0} -->

Based on Lemmas 5. ‣ 3.3 The “Vicious Circle” of Being Too Aggressive ‣ 3 Understanding Baselines in On-policy Stochastic Policy Optimization ‣ The Role of Baselines in Policy Gradient Optimization") and 7. ‣ 3.4 The “Virtuous Circle” of Not Being Too Aggressive ‣ 3 Understanding Baselines in On-policy Stochastic Policy Optimization ‣ The Role of Baselines in Policy Gradient Optimization"), the boundary between "too aggressive" and "not too aggressive" is precisely $\Theta{({1/t})}$. We now explain how a state value baseline in NPG will control update aggressiveness. First, without a baseline, sampling a sub-optimal action $a \in {\lbrack K\rbrack}$ for $t$ times makes its parameter behave as ${\theta_{t}{(a)}} \in {\Theta{(t)}}$, since ${r{(a)}} \in {\Theta{}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "How a State Value Baseline Reduces Update Aggressiveness", "weight": 1.0} -->

On the other hand, other action parameters will behave as ${\theta_{t}{(a^{\prime})}} \in {\Theta{}}$ if they are only sampled a constant number of times. Under the softmax parameterization Eq. 2, this will imply that ${1 - {\pi_{\theta_{t}}{(a)}}} \in {O{(e^{- {c \cdot t}})}}$, which is far too aggressive. Second, using a state value baseline, under repeated sampling the parameter increase for a sub-optimal action $a \in {\lbrack K\rbrack}$ will be damped. In particular, whenever the policy is close to deterministic, say ${\pi_{\theta_{t}}{(a)}} \approx 1$, we also have ${\pi_{\theta_{t}}^{\top}r} \approx {r{(a)}}$. Therefore, since

<!-- chunk {"id": "body-0048", "role": "body", "section": "How a State Value Baseline Reduces Update Aggressiveness", "weight": 1.0} -->

the closer $1 - {\pi_{\theta_{t}}{(a)}}$ is to $0$, the smaller ${r{(a)}} - {\pi_{\theta_{t}}^{\top}r}$ will be. This means even if $a$ is sampled repeatedly for $t$ times, we obtain ${\theta_{t}{(a)}} \in {O{({\log t})}}$ and ${1 - {\pi_{\theta_{t}}{(a)}}} \in {\Omega{({1/t})}}$ (LABEL:{lem:npg_aggressiveness_value_baseline}). Thus, the effect of baseline is to modify the sampling to lie exactly on the boundary of being good enough. From this argument the key role of the value baseline is to reduce update aggressiveness to achieve a particular effect on long-term sampling, rather than simply reduce variance. It also shows how using an appropriately un-aggressive update is both necessary (Lemma 5.

<!-- chunk {"id": "body-0049", "role": "body", "section": "How a State Value Baseline Reduces Update Aggressiveness", "weight": 1.0} -->

‣ 3.3 The “Vicious Circle” of Being Too Aggressive ‣ 3 Understanding Baselines in On-policy Stochastic Policy Optimization ‣ The Role of Baselines in Policy Gradient Optimization")) and sufficient (Lemma 7. ‣ 3.4 The “Virtuous Circle” of Not Being Too Aggressive ‣ 3 Understanding Baselines in On-policy Stochastic Policy Optimization ‣ The Role of Baselines in Policy Gradient Optimization")) to achieve almost sure convergence to a global optimum in on-policy stochastic policy optimization.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulations", "weight": 1.0} -->

We conducted simulations to verify the two main results above: asymptotic convergence toward globally optimal policy $\pi^{\ast}$ in Lemma 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), and the $O{({1/t})}$ convergence rate in Theorem 1. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization").

<!-- chunk {"id": "body-0051", "role": "body", "section": "Asymptotic Convergence", "weight": 1.0} -->

We first consider a one-state MDP with $K = 20$ actions and true mean reward vector $r \in {}^{K}$, where the optimal action is $a^{\ast} = 1$ with true mean reward ${r{}} \approx 0.97$ and best sub-optimal action's true mean reward ${r{}} \approx 0.95$. The sampled reward is observed with a large noise, e.g., $x \approx {- 2.03}$ and $x \approx 3.97$ with both $0.5$ probability for the optimal action, such that ${r{}} \approx {{0.5 \cdot {({- 2.03})}} + {0.5 \cdot 3.97}}$. Details about $r$ and the reward distributions can be found in the appendix.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Asymptotic Convergence", "weight": 1.0} -->

To verify asymptotic convergence to a globally optimal policy in Lemma 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), we consider the iteration behaviors of Update 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") under an adversarial initialization, where ${\pi_{\theta_{1}}{}} \approx 0.88$, i.e., a sub-optimal action starts with a dominating probability. This is the worst case scenario for Lemma 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), where the optimal action only has a small chance to be sampled, while the sampled reward noise is very large.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Asymptotic Convergence", "weight": 1.0} -->

As shown in Figure 2(a), the expected reward $\pi_{\theta_{t}}^{\top}r$ quickly approaches and remains stuck around ${r{}} \approx 0.95$ initially, as expected. However, after about $8 \times 10^{6}$ iterations, the policy $\pi_{\theta_{t}}$ finally escapes the sub-optimal plateau and approaches the optimal reward ${r{}} \approx 0.97$. This simulation result is consistent with Lemma 2.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Asymptotic Convergence", "weight": 1.0} -->

‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), i.e., for an arbitrary initialization, the introduction of a value baseline eventually makes $\pi_{\theta_{t}}$ approach a globally optimal policy within finite time, while additionally the optimal action's probability never vanishes, ${\inf_{t \geq 1}{\pi_{\theta_{t}}{(a^{\ast})}}} > 0$, as shown in Figure 2(b).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Convergence Rate", "weight": 1.0} -->

We run Update 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization") with a uniform initialization, i.e., ${\pi_{\theta_{1}}{(a)}} = {1/K}$ for all $a \in {\lbrack K\rbrack}$, and calculate averaged sub-optimality gap $\left( {\pi^{\ast} - \pi_{\theta_{t}}} \right)^{\top}r$ across $20$ independent runs, using deterministic reward settings where ${\hat{r}}_{t}$ is from Definition 2). ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Convergence Rate", "weight": 1.0} -->

As shown in Figure 2(c), where both axes are in $\log$ scale, the slope is approximately $- 1$, indicating that $\log\left( \pi^{\ast} - \pi_{\theta_{t}} \right)^{\top}r = - \log t + C$, or equivalently ${\left( {\pi^{\ast} - \pi_{\theta_{t}}} \right)^{\top}r} = {C^{\prime}/t}$, which is consistent with Theorem 1. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization").

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work clarifies some of the longstanding mysteries those have separated the theory and practice of policy gradient optimization. The major finding is a state value baseline reduces the aggressiveness of the on-policy stochastic NPG update, which turns out to be necessary and sufficient for achieving almost sure convergence to a global optimum. The deeper understanding of the circular dependence between on-policy sampling and updating also dispels a common misconception about variance reduction, showing that bounded variance estimators are not necessary for achieving global convergence. The main technical innovation is the stochastic NŁ inequality, and the subsequent arguments that establish global convergence, both of which depend critically on the value baseline.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work leaves open a number of interesting questions. First, the $O{({1/t})}$ convergence rate contains an initialization dependent constant in Lemma 2. ‣ 2.2 Global Convergence with a Value Baseline ‣ 2 On-policy Stochastic Natural Policy Gradient ‣ The Role of Baselines in Policy Gradient Optimization"), resulting from plateaus as observed in Figure 2(a), which does not appear in results that use the direct parameterization. Thus the difficulty appears due to the non-linear softmax transform. Removing or improving this constant would impact practical performance, so investigating other techniques, such as regularization, optimism or momentum might be helpful. Second, the results in this paper use the true state values as the baselines. It would be interesting to consider the effect of estimating the value baseline or using alternative baselines in policy optimization. Finally, the $O{({1/t})}$ last iteration convergence rate implies an optimal $O{({\log T})}$ regret in stochastic bandit problems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The explanation of the circular dependence between sampling and updating is specific to on-policy PG optimization, but it is also consistent with the exploration exploitation dilemma in RL. In other words, this work suggests a completely new approach to the exploration-exploitation trade-off, achieving provable bounds with ever requiring explicit uncertainty estimates, nor any concrete instantiation of the principle of optimism under uncertainty.
