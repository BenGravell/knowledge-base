<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The End of Optimism? An Asymptotic Analysis of Finite-Armed Linear Bandits

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic linear bandits are a natural and simple generalisation of finite-armed bandits with numerous practical applications. Current approaches focus on generalising existing techniques for finite-armed bandits, notably the optimism principle and Thompson sampling. While prior work has mostly been in the worst-case setting, we analyse the asymptotic instance-dependent regret and show matching upper and lower bounds on what is achievable. Surprisingly, our results show that no algorithm based on optimism or Thompson sampling will ever achieve the optimal rate, and indeed, can be arbitrarily far from optimal, even in very simple cases. This is a disturbing result because these techniques are standard tools that are widely used for sequential optimisation. For example, for generalised linear bandits and reinforcement learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The linear bandit is the simplest generalisation of the finite-armed bandit. Let $\mathcal{A} \subset {\mathbb{R}}^{d}$ be a finite set that spans ${\mathbb{R}}^{d}$ with ${|\mathcal{A}|} = k$ and $\left\| x \right\|_{2} \leq 1$ for all $x \in \mathcal{A}$. A learner interacts with the bandit over $n$ rounds. In each round $t$ the learner chooses an action (arm) $A_{t} \in \mathcal{A}$ and observes a payoff $Y_{t} = {\left\langle A_{t},\theta \right\rangle + \eta_{t}}$ where $\eta_{t} \sim {\mathcal{N}{}}$ is Gaussian noise and $\theta \in {\mathbb{R}}^{d}$ is an unknown parameter.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The optimal action is $x^{\ast} = {\underset{x \in \mathcal{A}}{\arg\max}\left\langle x,\theta \right\rangle}$, which is not known since it depends on $\theta$. The assumption that $\mathcal{A}$ spans ${\mathbb{R}}^{d}$ is non-restrictive, since if ${span}{(\mathcal{A})}$ has rank $r < d$, then one can simply use a different basis for which all but $r$ coordinates are always zero and then drop them from the analysis. The Gaussian assumption can be relaxed to $1$-subgaussian for our upper bound, but is needed for the lower bound. Our performance measure is the expected pseudo-regret (from now on just the regret), which is given by

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

where the expectation is taken with respect to the actions of the strategy and the noise. There are a number of algorithms designed for minimising the regret, all of which use one of two algorithmic designs. The first is the principle of optimism in the face of uncertainty, which was originally applied to finite-armed bandits by Agrawal; Katehakis and Robbins; Auer et al. and many others, and more recently to linear bandits. The second algorithm design is Thompson sampling, which is an old algorithm that has experienced a resurgence in popularity because of its impressive practical performance and theoretical guarantees for finite-armed bandits. Thompson sampling has also recently been applied to linear bandits with good empirical performance and near-minimax theoretical guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

While both approaches lead to practical algorithms (especially Thompson sampling), we will show they are fundamentally flawed in that algorithms based on these ideas cannot be close to asymptotically optimal. Along the way we characterise the optimal achievable asymptotic regret and design a strategy achieving it. This is an important message because optimism and Thompson sampling are widely used beyond the finite-armed case. Examples include generalised linear bandits, spectral bandits, and even learning in Markov decision processes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The disadvantages of these approaches is obscured in the worst-case regime, where both are quite close to optimal. One might question whether or not the asymptotic analysis is relevant in practice. The gold standard would be instance-dependent finite-time guarantees like what is available for finite-armed bandits, but historically the asymptotic analysis has served as a useful guide towards understanding the trade-offs in finite-time. Besides hiding the structure of specific problems, pushing for optimality in the worst-case regime can also lead to sub-optimal instance-dependent guarantees. For example, the MOSS algorithm for finite-armed bandits is minimax optimal, but far from finite-time optimal. For these reasons we believe that understanding the asymptotics of a problem is a useful first step towards optimal finite-time instance-dependent guarantees that are most desirable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

It is worth mentioning that partial monitoring (a more complicated online learning setting) is a well known example of the failure of optimism. Although related, the partial monitoring framework is more general than the bandit setting because the learner may not observe the reward even for the action they take, which means that additional exploration is usually necessary in order to gain information. Basic results in partial monitoring are concerned with characterizing whether an instance is easier or harder than bandit instances. More recently, the question of asymptotic instance optimality was studied in finite stochastic partial monitoring, and the special setting of learning with side information. While the algorithms derived in these works served as inspiration, the analysis and the algorithms do not generalise in a simple direct fashion to the linear setting, which requires a careful study of how information is transferred between actions in a linear setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

We note first that the finite-armed UCB algorithm of Agrawal; Katehakis and Robbins can be used on this problem by disregarding the structure on the arms to achieve an asymptotic regret of

<!-- chunk {"id": "body-0010", "role": "body", "section": "LOWER BOUND", "weight": 1.0} -->

This quantity depends *linearly* on the number of suboptimal arms, which may be very large (much larger than the dimension) and is very undesirable. Nevertheless we immediately observe that the asymptotic regret should be logarithmic. The following theorem and its corollary characterises the optimal asymptotic regret.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example 3 (Finite armed bandits)", "weight": 1.0} -->

which recovers the lower bound by Lai and Robbins.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 4", "weight": 1.0} -->

The reason is that $x_{1}$ and $x_{3}$ are pointing in nearly the same direction, so learning the difference is very challenging. But determining which of $x_{1}$ and $x_{3}$ is optimal is easy by playing $x_{2}$. So we see that in linear bandits there is a complicated trade-off between information and regret that makes the structure of the optimal strategy more interesting than in the finite setting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 4", "weight": 1.0} -->

The closest prior work to our lower bound is by Komiyama et al. and Agrawal et al.. The latter consider stochastic partial monitoring when the reward is part of the observation. In this setting in each round, the learner selects one of finitely many actions and receives an observation from a distribution that depends on the action chosen and an unknown parameter, but is otherwise known. While this model could cover our setting, the results in the paper are developed only for the case when the unknown parameter belongs to a finite set, an assumption that all the results of the paper heavily depend. Komiyama et al. on the other hand restricts partial monitoring to the case when the observations belong to a finite set, while the parameter belongs to the unit simplex. While this problem also has a linear structure, their results do not generalize beyond the discrete observation setting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 7", "weight": 1.0} -->

The uniqueness assumption of the theorem can be lifted at the price of more work and by slightly changing the theorem statement. In particular, the theorem statement must be restricted to those suboptimal actions $x \in \mathcal{A}^{-}$ that can be made optimal by changing $\theta$ to $\theta^{\prime}$, while none of the optimal actions ${\mathcal{A}^{\ast}{(\theta)}} = {\{{x \in \mathcal{A}}:{{\langle x,\theta\rangle} = {\max_{y \in \mathcal{A}}{\langle y,\theta\rangle}}}\}}$ are optimal.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 7", "weight": 1.0} -->

size=,color=blue!20!white,\]Csaba: This last step I have not verified.. If time permits.. Otherwise we can shorten this remark to basically say that we think an extension is possible.

<!-- chunk {"id": "body-0016", "role": "body", "section": "OPTIMAL STRATEGY", "weight": 1.0} -->

A barycentric spanner of the action space is a set $B = \left\{ x_{1},\ldots,x_{d} \right\} \subseteq A$ such that for any $x \in \mathcal{A}$ there exists an $\alpha \in {\lbrack{- 1},1\rbrack}^{d}$ with $x = {\sum_{i = 1}^{d}{\alpha_{i}x_{i}}}$. The existence of a barycentric spanner is guaranteed because $\mathcal{A}$ is finite and spans ${\mathbb{R}}^{d}$. We propose a simple strategy that operates in three phases called the warm-up phase, the success phase and the recovery phase. In the warm-up the algorithm deterministically chooses its actions from a barycentric spanner to obtain a rough estimate of the sub-optimality gaps. The algorithm then uses the estimated gaps as a substitute for the true gaps to determine the optimal pull counts for each action, and starts implementing this strategy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "OPTIMAL STRATEGY", "weight": 1.0} -->

Finally, if an anomaly is detected that indicates the inaccuracy of the estimated gaps then the algorithm switches to the recovery phase where it simply plays UCB.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

We now argue that algorithms based on optimism or Thompson sampling cannot be close to asymptotically optimal. In each round $t$ an optimistic algorithm constructs a confidence set $\mathcal{C}_{t} \subseteq {\mathbb{R}}^{d}$ and chooses $A_{t}$ according to $A_{t} = {{\underset{x \in \mathcal{A}}{\arg\max}\max_{\overset{\sim}{\theta} \in \mathcal{C}_{t}}}{\langle x,\overset{\sim}{\theta}\rangle}}$. In order to proceed we need to make some assumptions on $\mathcal{C}_{t}$, otherwise one can define a "confidence set" to ensure any behaviour at all.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

First of all, we will assume that ${\mathbb{P}}\left( \exists t \leq n:\theta \notin \mathcal{C}_{t} \right) = O{(1/n)}$. That is, that the probability that the true parameter is ever outside the confidence set is not too large. Second, we assume that $\mathcal{C}_{t} \subseteq \mathcal{E}_{t}$ where $\mathcal{E}_{t}$ is the ellipsoid about the least squares estimator given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

where $\alpha$ is some constant and $\hat{\theta}{(t)}$ is the empirical estimate of $\theta$ based on the observations so far. Existing algorithms based on confidence all use such confidence sets. Standard wisdom when designing optimistic algorithms is to use the smallest confidence set possible, so an alternative algorithm that used a different form of confidence set would normally be advised to use the intersection $\mathcal{C}_{t} \cap \mathcal{E}_{t}$, which remains valid with high probability by a union bound. If the optimistic algorithm is not consistent, then its regret is not logarithmic on some problem and so diverges relative to the optimal strategy. Suppose now that the algorithm is consistent. Then we design a bandit on which its asymptotic regret is worse than optimal by an arbitrarily large constant factor.

<!-- chunk {"id": "body-0021", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

But because $\theta \in C_{t}$, the optimistic value of the optimal action is at least ${\langle e_{1},\theta\rangle} = 1$, which means that $A_{t} \neq e_{2}$. We conclude that if $\theta \in C_{t}$ for all rounds, then the optimistic algorithm satisfies ${T_{e_{2}}{({t - 1})}} \leq {1 + {4\alpha{\log{(n)}}}}$. By the assumption that $\theta \in C_{t}$ with probability at least $1 - {1/n}$ we bound ${{\mathbb{E}}{\lbrack{T_{e_{2}}{(n)}}\rbrack}} \leq {2 + {4\alpha{\log{(n)}}}}$. By consistency of the optimistic algorithm and our lower bound (Theorem 1) we have

<!-- chunk {"id": "body-0022", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

Therefore by choosing $\varepsilon$ sufficiently small we conclude that ${\operatorname{lim\ sup}_{n\rightarrow\infty}{{{\mathbb{E}}{\lbrack{T_{x}{(n)}}\rbrack}}/{\log{(n)}}}} = {\Omega{({1/\varepsilon^{2}})}}$ and so the asymptotic regret of the optimistic algorithm is at least

<!-- chunk {"id": "body-0023", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

However, for small $\varepsilon$ the optimal regret for this problem is ${c{(\mathcal{A},\theta)}} = {128\alpha^{2}}$ and so by choosing $\varepsilon \ll \alpha$ we can see that the optimistic approach is sub-optimal by an arbitrarily large constant factor. The intuition is that the optimistic algorithms very quickly learn that $e_{2}$ is a sub-optimal arm and stop playing it. But as it turns out, the information gained by choosing $e_{2}$ is sufficiently valuable that an optimal algorithm should use it for exploration.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

Thompson sampling has also been proposed for the linear bandit problem. The standard approach uses a nearly flat Gaussian prior (and so posterior), which means that essentially the algorithm operates by sampling $\theta_{t}$ from $\mathcal{N}{({\hat{\mu}{(t)}},{\alphaG_{t}^{- 1}})}$ and choosing the arm $A_{t} = {\underset{x \in \mathcal{A}}{\arg\max}{\langle x,\theta_{t}\rangle}}$. Why does this approach fail? By the assumption of consistency we expect that the optimal arm will be played all but logarithmically often, which means that the posterior will concentrate quickly about the value of the optimal action so that ${\langle x^{\ast},\theta_{t}\rangle} \approx \mu^{\ast}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SUB-OPTIMALITY OF OPTIMISM AND THOMPSON SAMPLING", "weight": 1.0} -->

Then using the same counter-example as for the optimistic algorithm we see that the likelihood that ${\langle{e_{2} - e_{1}},\theta_{t}\rangle} \geq 0$ is vanishingly small once ${T_{e_{2}}{({t - 1})}} = {\Omega{({\alpha{\log{(n)}}})}}$ and so Thompson sampling will also fail to sample action $e_{2}$ sufficiently often.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SUMMARY", "weight": 1.0} -->

We characterised the optimal asymptotic regret for linear bandits with Gaussian noise and finitely many actions in the sense of Lai and Robbins. The results highlight a surprising fact that all reasonable algorithms based on optimism can be arbitrarily worse than optimal. While this behaviour has been observed before in more complicated settings (notably, partial monitoring), our results are the first to illustrate this issue in a setting only barely more complicated than finite-armed bandits. Besides this we improve the self-normalised concentration guarantees by Abbasi-Yadkori et al. by a factor of $d$ asymptotically.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SUMMARY", "weight": 1.0} -->

As usual, we open more questions than we answer. While the proposed strategy is asymptotically optimal, it is also extraordinarily naive and the analysis is far from showing finite-time optimality. For this reason we think the most pressing task is to develop efficient and practical algorithms that exploit the available information in a way that Thompson sampling and optimism do not. There are two natural research directions towards this goal. The first is to push the optimisation approach used here and also by Wu et al., but applied more "smoothly" without discarding data or long phases. The second is to generalise information-theoretic ideas used (for instance) by Russo and Van Roy or Reddy et al..
