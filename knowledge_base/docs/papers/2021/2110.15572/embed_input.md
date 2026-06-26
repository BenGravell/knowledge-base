<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Understanding the Effect of Stochasticity in Policy Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the effect of stochasticity in on-policy policy optimization, and make the following four contributions. First, we show that the preferability of optimization methods depends critically on whether stochastic versus exact gradients are used. In particular, unlike the true gradient setting, geometric information cannot be easily exploited in the stochastic case for accelerating policy optimization without detrimental consequences or impractical assumptions. Second, to explain these findings we introduce the concept of committal rate for stochastic policy optimization, and show that this can serve as a criterion for determining almost sure convergence to global optimality. Third, we show that in the absence of external oracle information, which allows an algorithm to determine the difference between optimal and sub-optimal actions given only on-policy samples, there is an inherent trade-off between exploiting geometry to accelerate convergence versus achieving optimality almost surely. That is, an uninformed algorithm either converges to a globally optimal policy with probability 1 but at a rate no better than O(1/t), or it achieves faster than O(1/t) convergence but then must fail to converge to the globally optimal policy with some positive probability.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we use the committal rate theory to explain why practical policy optimization methods are sensitive to random initialization, then develop an ensemble method that can be guaranteed to achieve near-optimal solutions with high probability.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy optimization is a central problem in reinforcement learning (RL) that provides a foundation for both policy-based and actor-critic RL methods. Until recently it had generally been assumed that methods based on following the policy gradient (PG) could not be guaranteed to converge to globally optimal solutions, given that the policy value function is not concave. However, this assumption has been contradicted by recent findings that policy gradient methods can indeed prove to converge to global optima, at least in the tabular setting. In particular, the standard softmax PG method with a constant learning rate has been shown to converge to a globally optimal policy at a $\Theta{({1/t})}$ rate for finite MDPs, albeit with challenging problem and initialization dependent constants. Several techniques have been developed to further improve standard PG and achieve better rates and constants. For example, adding entropy regularization has been shown to produce faster $O{(e^{- {c \cdot t}})}$ convergence ($c > 0$) to the optimal regularized policy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

By exploiting natural geometries based on Bregman divergences, natural PG (NPG) or mirror descent (MD) have been shown to achieve better constants than standard PG and faster $O{(e^{- {c \cdot t}})}$ rates, with and without regularization. Alternative policy parameterizations, such as the escort parameterization, have been shown to improve the constants achieved by softmax and yield faster plateau escaping. More recently, a geometry-aware normalized PG (GNPG) approach has been proposed to exploit the non-uniformity of the value function, achieving faster $O{(e^{- {c \cdot t}})}$ rates with improved constants.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key observation is that each of these four techniques---(i) entropy regularization, (ii) NPG (or MD), (iii) alternative policy parameterization, and (iv) GNPG---accelerates the convergence of standard softmax PG by better exploiting the geometry of the optimization landscape. In particular, entropy regularization makes the regularized objective behave more like a quadratic, which significantly improves the near-linear character of the softmax policy value. Natural PG (or MD) performs non-Euclidean updates in the parameter space, which is quite different from the Euclidean geometry characterizing standard softmax PG updates. The escort policy parameterization induces an alternative policy-parameter relation. GNPG exploits the non-uniform smoothness in the optimization landscape via a simple gradient normalization operation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, these advantages have only been established for the true gradient setting. A natural question therefore is whether geometry can also be exploited to accelerate convergence to global optimality in *stochastic* gradient settings. In this paper, we show that in a certain fundamental sense, the answer is *no*. That is, there exists a fundamental trade-off between leveraging geometry to accelerate convergence and overcoming the noise introduced by stochastic gradients (possibly infinite); in particular, no uninformed algorithm can improve the $O{({1/t})}$ convergence rate without incurring a positive probability of failure (i.e. diverging or converging to a sub-optimal stationary point).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The conditions used in vanilla stochastic gradient convergence analysis, *i.e.*, unbiased and variance-bounded gradient estimator, has been exploited to attempt to explain such a trade-off in policy gradients. However, the bounded variance requires the sample policy to be bounded away from zero everywhere, which is impractical. Meanwhile, a variant of NPG can converge even with unbounded variance. These gaps raise the question that if not the bounded variance, then what is the key factor to ensure the convergence of stochastic policy optimization algorithms? Motivated by this question, we introduce the concept committal rate to characterize the update behaviors, which significantly affect whether convergence to a correct solution can be guaranteed in the stochastic on-policy setting. In particular, we make the following contributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*First*, we illustrate the anomaly that the preferability of policy optimization algorithms (softmax PG vs. NPG and GNPG) changes dramatically depending on whether true versus on-policy stochastic gradients are considered, and reveal the impracticality and unnecessity of a bounded variance requirement in Section 2; *Second*, we introduce the concept of the committal rate in Section 3 to characterize the aggressiveness of an update, which provide us tools for analyzing the stochasticity effect in convergences; *Third*, we use the committal rate to study general stochastic policy optimization behaviors rigorously and reveal the inherent geometry-convergence trade-off in Section 4; *Finally*, we explain the sensitivity to random initialization in practical policy optimization algorithms. From these results, we then develop an ensemble method that can achieve fast convergence to global optima with high probability in Section 5.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Understanding Algorithm Preferability in On-line Policy Optimization", "weight": 1.0} -->

To illustrate the key aspects of policy optimization methods and their comparative preferability, it suffices to consider deterministic, single-state, finite-action Markov decision processes (MDPs). The main results extend to general finite MDPs, but for clarity of exposition we restrict attention to one-state MDPs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Understanding Algorithm Preferability in On-line Policy Optimization", "weight": 1.0} -->

A deterministic, single-state, finite-action MDP can be simply be specified by an action space is ${\lbrack K\rbrack} ≔ \left\{ 1,2,{\ldotsK} \right\}$ and a $K$-dimensional reward vector $r \in {\mathbb{R}}^{K}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Understanding Algorithm Preferability in On-line Policy Optimization", "weight": 1.0} -->

The problem is to maximize the expected reward of a parametric policy $\pi_{\theta}$, where $\pi_{\theta}$ is parameterized by $\theta$ using the standard softmax transform, Without loss of generality, we assume there exists a unique optimal action $a^{\ast} = {{{\arg\max}_{a \in {\lbrack K\rbrack}}r}{(a)}}$, hence there exists a unique optimal deterministic policy $\pi^{\ast}$ such that ${\pi_{}^{\ast \top}r} = {\sup_{\theta \in {\mathbb{R}}^{K}}{\pi_{\theta}^{\top}r}} = {r{(a^{\ast})}}$. We make the following assumption on the reward.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Exact Gradient Setting", "weight": 1.0} -->

It is known that Eq. 1 is a non-concave maximization over the policy parameter $\theta$. Nevertheless, it has recently become better understood how policy gradient (PG) methods still converge to global optima for Eq. 1 when exact gradients are used. To illustrate the main considerations, we focus on the following three representative algorithms that have recently been proved to achieve convergence to global optima but at different rates: softmax policy gradient (PG), natural PG (NPG), and geometry-aware normalized PG (GNPG), while similar conclusions can be drawn for other variants.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Softmax PG", "weight": 1.0} -->

The standard softmax PG method is specified by the following update.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Update 1 (Softmax PG, true gradient)", "weight": 1.0} -->

As shown in Mei et al., the convergence of this update to a globally optimal policy, given exact gradients, can be established by considering the following non-uniform Łojasiewicz (NŁ) inequality,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The constant dependence of PG follows a $\Omega{({1/c})}$ lower bound for one-state MDPs, while $c$ can be exponentially small in terms of the number of states for general finite MDPs.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To summarize, using $\eta \in {O{}}$, softmax PG achieves convergence to a global optima, but with a $\Theta{({1/t})}$ rate that exhibits poor constant dependence.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Natural PG (NPG)", "weight": 1.0} -->

An alternative method, natural PG (NPG), provides the prototype for many practical policy optimization methods, such as TRPO and PPO. NPG is based on the following update.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Update 2 (Natural PG (NPG), true gradient)", "weight": 1.0} -->

For softmax policies, it turns out that Update 2, true gradient). ‣ 2.1.2 Natural PG (NPG) ‣ 2.1 Exact Gradient Setting ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") is identical to mirror descent (MD) with a Kullback-Leibler (KL) divergence. Therefore a standard MD analysis shows that Update 2, true gradient). ‣ 2.1.2 Natural PG (NPG) ‣ 2.1 Exact Gradient Setting ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") achieves convergence to a global optimum at a rate of $O{({1/t})}$. Very recently, work concurrent to this submission has shown that Update 2, true gradient).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Update 2 (Natural PG (NPG), true gradient)", "weight": 1.0} -->

‣ 2.1.2 Natural PG (NPG) ‣ 2.1 Exact Gradient Setting ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") actually enjoys a much faster $O{(e^{- {c \cdot t}})}$ rate. In fact, here too we can establish the same $O{(e^{- {c \cdot t}})}$ rate, but using a simpler argument based on the following variant of the NŁ inequality for natural gradients. These results are new to this paper. Due to space limitation, we postpone all the proofs to the appendix.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Geometry-aware Normalized PG (GNPG)", "weight": 1.0} -->

The Geometry-aware Normalized PG (GNPG) update is investigated in to accelerate the convergence of PG by exploiting local smoothness properties of the optimization landscape.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Update 3 (Geometry-aware Normalized PG (GNPG), true gradient)", "weight": 1.0} -->

The analysis in focuses on exploiting non-uniform smoothness (NS) rather than improving the NŁ inequality as for NPG above.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Anomalous Behaviour of Some On-policy Stochastic Gradient Updates", "weight": 1.0} -->

Although the above results show that exploiting geometric information can allow linear convergence to an optimal solution given true gradients---obviously $O{(e^{- {c \cdot t}})}$ represents an exponential speedup over the $\Omega{({1/t})}$ lower bound for standard PG---it is critical to understand whether such advantages can also be obtained in the more natural stochastic gradient setting. Given the previous results, it would seem natural to prefer accelerated algorithms over PG in practice, and there is some evidence that such thinking has become mainstream based on the popularity of TRPO and PPO over PG. Indeed, TRPO and PPO are often interpreted as instances of NPG and the faster convergence of NPG is used to explain their empirical success. However, by more closely examining the behavior of these algorithms when true gradients are replaced by on-policy stochastic estimates, serious shortcomings begin to emerge, as empirically observed in Chung et al., and it is far from obvious that similar advantages from the true gradient case might be recoverable in the more practical stochastic scenario.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Anomalous Behaviour of Some On-policy Stochastic Gradient Updates", "weight": 1.0} -->

We begin by examining the behavior of the previous algorithms in the context of on-policy stochastic gradients. To enable this analysis, first note that each of the above PG methods, Updates 1. ‣ 2.1.1 Softmax PG ‣ 2.1 Exact Gradient Setting ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization"), 2, true gradient). ‣ 2.1.2 Natural PG (NPG) ‣ 2.1 Exact Gradient Setting ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") and 3, true gradient). ‣ 2.1.3 Geometry-aware Normalized PG (GNPG) ‣ 2.1 Exact Gradient Setting ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization"), can be adapted to the stochastic setting by using on-policy importance sampling (IS) to provide an unbiased estimate of the true reward.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Anomalous Behaviour of Some On-policy Stochastic Gradient Updates", "weight": 1.0} -->

We do not make assumptions like each action is sufficiently explored, since $\pi_{\theta_{t}}$ is the behaviour policy as well as the policy to be optimized. It is possible that $\pi_{\theta_{t}}$ approaches a near deterministic policy, ruling out positive results based on such assumptions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We consider sampling one action in each iteration, but the results continue to hold for sampling a constant $B > 0$ mini-batch of actions. A significant limitation of our results is that the reward is observed without noise, which is an idealized case. It remains to be seen which conclusions of this work can be extended to the more general case when the rewards are observed in noise.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In the next subsections we consider the mentioned three on-policy update rules. As we shall see, only the first update rule, vanilla policy gradient with softmax parameterization is sound.

<!-- chunk {"id": "body-0028", "role": "body", "section": "NPG", "weight": 1.0} -->

Similarly, we can use on-policy IS estimation to adapt NPG to the stochastic setting.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Update 5 (NPG, on-policy stochastic gradient)", "weight": 1.0} -->

Although the NPG is unbiased, its variance can be possibly unbounded in the on-policy setting.

<!-- chunk {"id": "body-0030", "role": "body", "section": "GNPG", "weight": 1.0} -->

Finally, we consider the stochastic version of GNPG.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Update 6 (GNPG, on-policy stochastic gradient)", "weight": 1.0} -->

Unfortunately, this estimator involves a ratio of random variables, and its bias can be large. As for NPG we can show that stochastic GNPG fails with positive probability in the stochastic case.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Why Consider the On-policy Stochastic Setting?", "weight": 1.0} -->

The findings of the previous sections are summarized in Table 1. The two methods that converge faster when the exact gradient is available are exactly those that fail in the worse possible way in the on-policy setting. This raises the question of should one even consider the on-policy setting?

<!-- chunk {"id": "body-0033", "role": "body", "section": "Why Consider the On-policy Stochastic Setting?", "weight": 1.0} -->

One possible reason to consider this setting is because on-policy sampling is the simplest and most straightforward approach to extend algorithms developed for the "exact gradient" setting and with a minor twist, Occam's razor dictates that one should consider simple solutions before considering more complex ones. Indeed, off-policy algorithms are more complex with many more choices to be made and while having the extra freedom may ultimately be useful (and even perhaps necessary), it is worthwhile to first thoroughly examine whether this complexity can be avoided. Indeed, there is some empirical evidence that the simple, on-policy approach may sometimes be a reasonable one: The method PPO uses on-policy sampling and yet, remarkably, it achieved outstanding results on challenging tasks, a good example of which is to learn dexterous in-hand manipulation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Why Consider the On-policy Stochastic Setting?", "weight": 1.0} -->

A second reason is that the on-policy setting presents unique challenges and as such is interesting on its own for learning about how to design and reason about stochastic methods. Indeed, the standard approach in analyzing stochastic update rules, such as SGD, is to start with the assumption that the gradient estimates are unbiased and have a uniformly bounded variance. This has been used both in the analysis of SGD, and later adopted to policy gradient methods. However, such conditions are only *sufficient* and not necessary as the numerous results in the literature of the analysis and design of stochastic approximation methods also show. In fact, the bounded variance assumption can be difficult to satisfy. For example, in the problems studied here this assumption requires that the probabilities induced by a behaviour policy are bounded away from $0$ everywhere, which is impractical for large state and action spaces and impossible when they are infinite.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Why Consider the On-policy Stochastic Setting?", "weight": 1.0} -->

Another observation that suggests that it is worthwhile to consider methods which potentially unbounded variance is made by Chung et al. who explored the role of baselines in policy optimization. They show that variance reduction techniques are not able to overcome unbounded variance, while NPG can still achieve global convergence almost surely with a judicious choice of baseline even though its variance remains *unbounded* (see Update 7. ‣ 3 Committal Rate of Stochastic Policy Optimization Algorithms ‣ Understanding the Effect of Stochasticity in Policy Optimization") for details). This is another example that shows that bounded variance is not necessary for convergence, and some other factors rather than variance account for the convergence behaviour of stochastic policy optimization algorithms.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Why Consider the On-policy Stochastic Setting?", "weight": 1.0} -->

This leave us an important question to be answered to bridge the gap between theory and practice, *What are the key factors determining the convergence of stochastic policy optimization?* As an answer to this question we propose a new notion, the *committal rate* of policy optimization methods and will demonstrate that small committal rates are necessary to ensure the convergent behavior of policy optimization methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Committal Rate of Stochastic Policy Optimization Algorithms", "weight": 1.0} -->

Although the baseline study only focuses on two- and three-action bandits primarily, it develops a useful intuition that stochastic policy optimization in practical settings consists of separate "sampling" and "updating" steps that become coupled in the on-policy setting. Building from this observation, and seeking to explain the outcomes in Section 2, we formalize the following "committal rate" function of a policy optimization algorithm. The main idea is to decouple the "sampling" and "updating" by fixing sampling one action and characterizing the aggressiveness of an update in a deterministic way. Thus, in what follows, by a policy optimization algorithm $\mathcal{A}$ we mean a mapping from all sequences of pairs of action-reward pairs to the set of parameter vectors.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Geometry-Convergence Trade-off in Stochastic Policy Optimization", "weight": 1.0} -->

Theorem 7 raises the question of whether ${\kappa{(\mathcal{A},a)}} \leq 1$ for all sub-optimal actions $a \in {\lbrack K\rbrack}$ is sufficient to ensure an algorithm $\mathcal{A}$ converges to an optimal policy almost surely. Unfortunately, this is not the case, and the complete picture of global optimality in stochastic policy optimization is more complex and requires detailed study of different iteration behaviors.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The condition that ${\kappa{(\mathcal{A},a)}} \leq 1$ for all sub-optimal actions $a \in {\lbrack K\rbrack}$ is not sufficient for ensuring almost sure convergence to global optimality. In addition to "convergence to a sub-optimal policy with positive probability" and "convergence to a globally optimal policy with probability $1$" there exist other possible optimization behaviours, such as "not converging to any policy".

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In particular, consider the following update behaviors.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Staying", "weight": 1.0} -->

For the stationary update $\mathcal{A}:{\theta_{t + 1}\leftarrow\theta_{t}}$ we obtain ${\kappa{(\mathcal{A},a)}} = 0 \leq 1$ for all $a \in {\lbrack K\rbrack}$, yet $\pi_{\theta_{t}} = \pi_{\theta_{1}}$ does not converge to the optimal policy nor any sub-optimal deterministic policy.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Wandering", "weight": 1.0} -->

The above examples show that not converging to a sub-optimal policy does not necessarily imply converging to an optimal policy almost surely, and a stronger condition is needed to eliminate unreasonable behaviors like $\theta_{t + 1}\leftarrow\theta_{t}$. We leave it as an open question to identify necessary and sufficient conditions for almost sure convergence to a global optimum.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Geometry-Convergence Trade-off", "weight": 1.0} -->

In Section 2 we see that NPG and GNGP can use true gradients to significantly accelerate PG by better exploiting geometry. However, in the stochastic setting, any estimated geometry might be inaccurate, and intuitively, accelerated methods risk leveraging inaccurate information too aggressively. On the one hand, if progress is sufficiently fast (i.e., with a large committal rate), then an algorithm might never recover from aggressive yet inaccurate updates (Theorem 5. ‣ 3 Committal Rate of Stochastic Policy Optimization Algorithms ‣ Understanding the Effect of Stochasticity in Policy Optimization")). On the other hand, large progress is necessary for fast convergence. The tension between these observations suggest that there might be an inherent trade-off between exploiting geometry and avoiding premature convergence in stochastic policy optimization. We formalize this intuition with the following results.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Geometry-Convergence Trade-off", "weight": 1.0} -->

For the first result, we need to restrict to the class of policy optimization methods that do not decrease the probability of the optimal action whenever that action is chosen: In particular, a policy optimization method is said to be *optimality-smart* if for any $t \geq 1$, ${\pi_{{\overset{\sim}{\theta}}_{t}}{(a^{\ast})}} \geq {\pi_{\theta_{t}}{(a^{\ast})}}$ holds where ${\overset{\sim}{\theta}}_{t}$ is the parameter vector obtained when $a^{\ast}$ is chosen in every time step, starting at $\theta_{1}$, while $\theta_{t}$ is *any* parameter vector that can be obtained with $t$ updates (regardless of the action sequence chosen), but also starting from $\theta_{1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Theorem 10. ‣ 4.2 Geometry-Convergence Trade-off ‣ 4 The Geometry-Convergence Trade-off in Stochastic Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") implies that an algorithm can achieve at most one of the mentioned two results. It is possible that an algorithm achieves neither (e.g., staying or wandering).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Exploiting External Information", "weight": 1.0} -->

In Theorem 10. ‣ 4.2 Geometry-Convergence Trade-off ‣ 4 The Geometry-Convergence Trade-off in Stochastic Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization"), the condition of ${\kappa{(\mathcal{A},a^{\ast})}} = {\kappa{(\mathcal{A},a)}}$ for at least one sub-optimal action $a \in {\lbrack K\rbrack}$ is necessary for the trade-off to hold. If this condition can somehow be bypassed, then it is possible to simultaneously achieve faster rates and almost sure convergence to a global optimum. For example, consider Update 7. ‣ 3 Committal Rate of Stochastic Policy Optimization Algorithms ‣ Understanding the Effect of Stochasticity in Policy Optimization").

<!-- chunk {"id": "body-0047", "role": "body", "section": "Exploiting External Information", "weight": 1.0} -->

As mentioned before, we have ${\kappa{(\mathcal{A},a^{\ast})}} = \infty$ and ${\kappa{(\mathcal{A},a)}} = 0$ for all $a \neq a^{\ast}$, breaking the mentioned condition, which allows $\mathcal{A}$ to enjoy almost sure global convergence as well as a $O{(e^{- {c \cdot t}})}$ rate. Of course, such a fortuitous outcome required a very specific baseline that is aware of both the optimal reward and the reward gap. Without introducing external mechanisms that inform an on-policy algorithm it appears that such information cannot be recovered sufficiently quickly from sample data alone. Nevertheless, it remains an open question to prove that this is not possible, or whether some other strategy might allow an on-policy stochastic policy optimization algorithm to avoid the condition of Theorem 10.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Exploiting External Information", "weight": 1.0} -->

‣ 4.2 Geometry-Convergence Trade-off ‣ 4 The Geometry-Convergence Trade-off in Stochastic Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") and achieve both fast rates and almost sure global convergence.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Initialization Sensitivity and Ensemble Methods", "weight": 1.0} -->

We use the committal rate to further reveal mystery observed in practice about the initialization sensitivity. With the understanding of this unavoidable phenomenon, we introduce ensemble method and quantitatively characterize the successful rate in terms of number of trials.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Initialization Sensitivity", "weight": 1.0} -->

It has been observed empirically that RL algorithms are sensitive to initialization in practice: the same algorithm can produce remarkably different performance given different random seeds. Some existing work has attempted to explain initialization sensitivity due to the softmax transform, but such results only hold for true gradients and apply to standard PG methods.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Initialization Sensitivity", "weight": 1.0} -->

Using the committal rate theory developed above, we can provide a new explanation and additional understanding of the initialization sensitivity of practical policy optimization algorithms. Most well-performing policy optimization algorithms in practice, such as TRPO and PPO, are based on NPG, which exploits geometry to accelerate PG in true gradient settings. However, according to Theorem 10. ‣ 4.2 Geometry-Convergence Trade-off ‣ 4 The Geometry-Convergence Trade-off in Stochastic Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization"), such fast convergence must incur a positive probability of failing to reach a global optimum, even in bandit settings. Therefore, the need to attempt multiple random seeds to achieve success is an unavoidable consequence of using these algorithms according to this theory.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ensemble Methods", "weight": 1.0} -->

The committal rate theory also explains why ensemble methods, *i.e.*, running a policy optimization algorithm in multiple parallel threads and picking the best performing one, can provably work well. This is because a fast algorithm for the true gradient setting can have a positive probability of success or failure across different initializations while always converging quickly. In which case, multiple independent runs can then be used to reduce the failure probability to any desired positive value, while retaining efficiency (if full parallelism can be maintained).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sufficient and Necessary Conditions for Almost Sure Global Convergence", "weight": 1.0} -->

We make the following conjecture with some intuitions for the sufficient and necessary condition for global convergence, a question left open in Section 4.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conjecture 1", "weight": 1.0} -->

Given a stochastic policy optimization algorithm $\mathcal{A}$, if ${\kappa{(\mathcal{A},a^{\ast})}} = {\kappa{(\mathcal{A},a)}}$ for at least one sub-optimal action $a$, then ${\kappa{(\mathcal{A},a^{\ast})}} \in {(0,1\rbrack}$ is a sufficient and necessary condition for global convergence to $\pi^{\ast}$ with polynomial convergence rate of $O{({1/t^{\alpha}})}$, where $\alpha > 0$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conjecture 1", "weight": 1.0} -->

The necessary condition is from Theorem 5. ‣ 3 Committal Rate of Stochastic Policy Optimization Algorithms ‣ Understanding the Effect of Stochasticity in Policy Optimization"). For the sufficient condition, Theorem 9 can potentially be strengthened to ${\kappa{(\mathcal{A},a^{\ast})}} \geq \alpha$ is a sufficient and necessary condition for global convergence rate $O{({1/t^{\alpha}})}$ ($\alpha > 0$). The observation here is that 1. ‣ 2 Understanding Algorithm Preferability in On-line Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") leads to ${\left( {\pi^{\ast} - \pi_{\theta_{t}}} \right)^{\top}r} \leq {1 - {\pi_{\theta_{t}}{(a^{\ast})}}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Lower Bounds in Bandit Literature", "weight": 1.0} -->

In the bandit literature, the $\Omega{({\log T})}$ result implies that the convergence speed in terms of sub-optimality ("average regret") cannot be faster than $O{({1/t})}$. However, the lower bound construction there holds for stochastic reward settings. Theorem 10. ‣ 4.2 Geometry-Convergence Trade-off ‣ 4 The Geometry-Convergence Trade-off in Stochastic Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") holds for a simpler optimization setting: the reward is fixed and deterministic, but the policy gradient is estimated by on-policy sampling. Therefore, the difficulty and trade-off are from the restriction on the action-selection scheme (balancing the aggressiveness and the stability), not from estimating or tracking the reward signal.

<!-- chunk {"id": "body-0057", "role": "body", "section": "General MDPs", "weight": 1.0} -->

The one-state MDP results already show the main findings, since a large portion is about constructing counterexamples showing that the stochastic policy optimization algorithms do not perform well as in the true gradient setting. A counterexample for one-state MDPs is also a counterexample for general MDPs. Therefore, there is no loss of generality by establishing negative results using one-state MDPs. We include extensions to general finite MDPs in Appendix E for completeness.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

This paper introduces the committal rate theory, which not only explains why faster policy optimization algorithms in the true gradient setting become dominated by slower counterparts in the on-policy stochastic setting, but also reveals an inherent geometry-convergence trade-off in stochastic policy optimization. The theory also explains empirical observations of sensitivity to random initialization for practical policy optimization algorithms as well as the effectiveness of ensemble methods.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

One interesting future direction is to study necessary and sufficient conditions for almost sure global convergence, which could be weaker than the bounded variance assumption. Another important direction is to investigate whether other techniques might be used in on-policy settings to break the condition of Theorem 10. ‣ 4.2 Geometry-Convergence Trade-off ‣ 4 The Geometry-Convergence Trade-off in Stochastic Policy Optimization ‣ Understanding the Effect of Stochasticity in Policy Optimization") to achieve almost sure global convergence with a fast rate. One also expects that some generalized versions of committal rate would be meaningful in stochastic reward settings.
