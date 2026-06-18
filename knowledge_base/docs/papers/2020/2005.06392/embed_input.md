<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Global Convergence Rates of Softmax Policy Gradient Methods

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We make three contributions toward better understanding policy gradient methods in the tabular setting. First, we show that with the true gradient, policy gradient with a softmax parametrization converges at a O(1/t) rate, with constants depending on the problem and initialization. This result significantly expands the recent asymptotic convergence results. The analysis relies on two findings: that the softmax policy gradient satisfies a Łojasiewicz inequality, and the minimum probability of an optimal action during optimization can be bounded in terms of its initial value. Second, we analyze entropy regularized policy gradient and show that it enjoys a significantly faster linear convergence rate O(e^-c * t) toward softmax optimal policy (c > 0). This result resolves an open question in the recent literature. Finally, combining the above two results and additional new Omega(1/t) lower bound results, we explain how entropy regularization improves policy optimization, even with the true gradient, from the perspective of convergence rate. The separation of rates is further explained using the notion of non-uniform Łojasiewicz degree. These results provide a theoretical understanding of the impact of entropy and corroborate existing empirical studies.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The *policy gradient* is one of the most foundational concepts in Reinforcement Learning (RL), lying at the core of policy-search and actor-critic methods. This paper is concerned with the analysis of the convergence rate of *policy gradient methods*. As an approach to RL, the appeal of policy gradient methods is that they are conceptually straightforward and under some regularity conditions they guarantee monotonic improvement of the value. A secondary appeal is that policy gradient methods were shown to achieve effective empirical performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the prevalence and importance of policy optimization in RL, the theoretical understanding of policy gradient method has, until recently, been severely limited. A key barrier to understanding is the inherent non-convexity of the value landscape with respect to standard policy parametrizations. As a result, little has been known about the global convergence behavior of policy gradient method. Recently, important new progress in understanding the convergence behavior of policy gradient has been achieved. As in this paper we will restrict ourselves to the tabular setting, we analyze the part of the literature that also deals with this setting. While the tabular setting is clearly limiting, this is the setting where so far the cleanest results have been achieved and understanding this setting is a necessary first step towards the bigger problem of understanding RL algorithms. Returning to the discussion of recent work, Bhandari & Russo showed that, without parametrization, projected gradient ascent on the simplex does not suffer from spurious local optima.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In concurrent work, Agarwal et al. showed that (i) without parametrization, projected gradient ascent converges at rate $O{({1/\sqrt{t}})}$ to a global optimum; and (ii) with softmax parametrization, policy gradient converges asymptotically. Agarwal et al. also analyze other variants of policy gradient, and show that policy gradient with relative entropy regularization converges at rate $O{({1/\sqrt{t}})}$, natural policy gradient (mirror descent) converges at rate $O{({1/t})}$, and given a "compatible" function approximation (thus, going beyond the tabular case) natural policy gradient converges at rate $O{({1/\sqrt{t}})}$. Shani et al. obtains the slower rate $O{({1/\sqrt{t}})}$ for mirror descent. They also proposed a variant that adds entropy regularization and prove a rate of $O{({1/t})}$ for this modified problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these advances, many open questions remain in understanding the behavior of policy gradient methods, even in the tabular setting and even when the true gradient is available in the updates. In this paper, we provide answers to the following three questions left open by previous work in this area: (i) What is the convergence rate of policy gradient methods with softmax parametrization? The best previous result, due to Agarwal et al., established asymptotic convergence but gave no rates. (ii) What is the convergence rate of entropy regularized softmax policy gradient? Figuring out the answer to this question was explicitly stated as an open problem by Agarwal et al.. (iii) Empirical results suggest that entropy helps optimization. Can this empirical observation be turned into a rigorous theoretical result?^11^1While Shani et al. suggest that entropy regularization speeds up mirror descent to achieve the rate of $O{({1/t})}$, in light of the corresponding result of Agarwal et al. who established the same rate for the unregularized version of mirror descent, their conclusion needs further support (e.g., lower bounds).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, we prove that with the true gradient, policy gradient methods with a softmax parametrization converge to the optimal policy at a $O{({1/t})}$ rate, with constants depending on the problem and initialization. This result significantly strengthens the recent asymptotic convergence results of Agarwal et al.. Our analysis relies on two novel findings: (i) that softmax policy gradient satisfies what we call a non-uniform Łojasiewicz-type inequality with the constant in the inequality depending on the optimal action probability under the current policy; (ii) the minimum probability of an optimal action during optimization can be bounded in terms of its initial value. Combining these two findings, with a few other properties we describe, it can be shown that softmax policy gradient method achieves a $O{({1/t})}$ convergence rate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we analyze entropy regularized policy gradient and show that it enjoys a linear convergence rate of $O{(e^{- t})}$ toward the softmax optimal policy, which is significantly faster than that of the unregularized version. This result resolves an open question in Agarwal et al., where the authors analyzed a more aggressive relative entropy regularization rather than the more common entropy regularization. A novel insight is that entropy regularized gradient updates behave similarly to the contraction operator in value learning, with a contraction factor that depends on the current policy.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, we provide a theoretical understanding of entropy regularization in policy gradient methods. (i) We prove a new lower bound of $\Omega{({1/t})}$ for softmax policy gradient, implying that the upper bound of $O{({1/t})}$ that we established, apart from constant factors, is unimprovable. This result also provides a theoretical explanation of the optimization advantage of entropy regularization: even with access to the true gradient, entropy helps policy gradient *converge faster than any achievable rate of softmax policy gradient method without regularization*. (ii) We study the concept of non-uniform Łojasiewicz degree and show that, without regularization, the Łojasiewicz degree of expected reward cannot be positive, which allows $O{({1/t})}$ rates to be established. We then show that with entropy regularization, the Łojasiewicz degree of maximum entropy reward becomes $1/2$, which is sufficient to obtain linear $O{(e^{- t})}$ rates. This change of the relationship between gradient norm and sub-optimality reveals a deeper reason for the improvement in convergence rates.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The theoretical study we provide corroborates existing empirical studies on the impact of entropy in policy optimization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. After introducing notation and defining the setting in Section 2, we present the three main contributions in Sections 3, 4 and 5 as aforementioned. Section 6 gives our conclusions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Notations and Settings", "weight": 1.0} -->

For a finite set $\mathcal{X}$, we use $\Delta{(\mathcal{X})}$ to denote the set of probability distributions over $\mathcal{X}$. A finite Markov decision process (MDP) $\mathcal{M} = {(\mathcal{S},\mathcal{A},\mathcal{P},r,\gamma)}$ is determined by a finite state space $\mathcal{S}$, a finite action space $\mathcal{A}$, transition function $\mathcal{P}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$, reward function $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, and discount factor $\gamma \in {\lbrack 0,1)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations and Settings", "weight": 1.0} -->

Given a policy $\pi:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$, the value of state $s$ under $\pi$ is defined as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Bounded reward)", "weight": 1.0} -->

The softmax transform of a vector exponentiates the components of the vector and normalizes it so that the result lies in the simplex.

<!-- chunk {"id": "body-0015", "role": "body", "section": "H matrix", "weight": 1.0} -->

Here, we are using the standard convention that derivatives give row-vectors.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Gradient", "weight": 1.0} -->

Policy gradient is a special policy search method. In policy search, one considers a family of policies parametrized by finite-dimensional parameter vectors, reducing the search for a good policy to searching in the space of parameters. This search is usually accomplished by making incremental changes (additive updates) to the parameters. Representative policy-based RL methods include REINFORCE, natural policy gradient, deterministic policy gradient, and trust region policy optimization. In policy gradient methods, the parameters are updated by following the gradient of the map that maps policy parameters to values.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Vanilla Softmax Policy Gradient", "weight": 1.0} -->

We focus on the policy gradient method that uses the softmax parametrization. Since we consider the tabular case, the policy is then parametrized using the logit $\theta:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ function and $\pi_{\theta}{( \cdot |s)} = {softmax}{(\theta{(s, \cdot )})}$. The vanilla form of policy gradient for this case is shown in Algorithm 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Vanilla Softmax Policy Gradient", "weight": 1.0} -->

Input: Learning rate η &gt; 0.
Initialize logit θ1 (s,a) for all (s,a).
$\theta_{t + 1}\leftarrow{\theta_{t} + {\eta \cdot \frac{\partial{V^{\pi_{\theta_{t}}}{(\mu)}}}{\partial\theta_{t}}}}$.
Algorithm 1 Policy Gradient Method

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Instructive Case of Bandits", "weight": 1.0} -->

As promised, in this section we consider "bandit case": In particular, assume that the MDP has a single state and the discount factor $\gamma$ is zero: $\gamma = 0$. In this case, Eq. 1 reduces to maximizing the expected reward,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Update 1 (Softmax policy gradient, expected reward)", "weight": 1.0} -->

As is well known, if a function is smooth, then a small gradient update will be guaranteed to improve the objective value.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The value of $\pi_{\theta_{t}}{(a^{\ast})}$, while it is nonzero (and so is $c_{t}$) can be small (e.g., because of the choice of $\theta_{1}$). Consequently, its minimum $c_{t}$ can be quite small and the upper bound in Lemma 4. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") can be large, or even vacuous. The dependence of the previous result on $\pi_{\theta_{t}}{(a^{\ast})}$ comes from Lemma 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods").

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

As it turns out, it is not possible to eliminate or improve the dependence on $\pi_{\theta}{(a^{\ast})}$ in Lemma 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). To see this consider $r = {}^{\top}$, $\pi_{\theta} = {({2\epsilon},{{1/2} - {2\epsilon}},{1/2})}$ where $\epsilon > 0$ is small number.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

which means for any Łojasiewicz-type inequality, $C$ necessarily depends on $\epsilon$ and hence on ${\pi_{\theta}{(a^{\ast})}} = {2\epsilon}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The necessary dependence on $\pi_{\theta_{t}}{(a^{\ast})}$ makes it clear that Lemma 4. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") is insufficient to conclude a $O{({1/t})}$ rate. since $c_{t}$ may vanish faster than $O{({1/t})}$ as $t$ increases. Our next result eliminates this possibility. In particular, the result follows from the asymptotic convergence result of Agarwal et al. which states that ${\pi_{\theta_{t}}{(a^{\ast})}}\rightarrow 1$ as $t\rightarrow\infty$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In Section 5, we prove a lower bound $\Omega{({1/t})}$ for the same update rule, showing that the upper bound $O{({1/t})}$ of Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), apart from constant factors, is unimprovable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In general it is difficult to characterize how the constant $C$ in Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") depends on the problem and initialization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Visualization", "weight": 1.0} -->

Subfigure (b) shows the behavior of the gradient updates with "good" ($\pi_{\theta_{1}} = {(0.05,0.01,0.94)}^{\top}$) and "bad" ($\pi_{\theta_{1}} = {(0.01,0.05,0.94)}^{\top}$) initial policies. While these are close to each other, the iterates behave quite differently (in both cases $\eta = {2/5}$). From the good initialization, the iterates converge quickly: after $100$ iterations the distance to the optimal policy is already quite small. At the same time, starting from a "bad" initial value, the iterates are first attracted toward a sub-optimal action. It takes more than $7000$ iterations for the algorithm to escape this sub-optimal corner!

<!-- chunk {"id": "body-0028", "role": "body", "section": "Visualization", "weight": 1.0} -->

In subfigure (c), we see that $\pi_{\theta_{t}}{(a^{\ast})}$ increases for the good initialization, while in subfigure (d), for the bad initialization, we see that it initially decreases. These experiments confirm that the dependence of the error bound in Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") on the initial values cannot be removed.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Non-unique optimal actions", "weight": 1.0} -->

When the optimal action is non-unique, the arguments need to be slightly modified. Instead of using a single $\pi_{\theta}{(a^{\ast})}$, we need to consider $\sum_{a^{\ast} \in \mathcal{A}^{\ast}}{\pi_{\theta}{(a^{\ast})}}$, i.e., the sum of probabilities of all optimal actions. Details are given in the appendix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "General MDPs", "weight": 1.0} -->

For general MDPs, the optimization problem takes the form

<!-- chunk {"id": "body-0031", "role": "body", "section": "General MDPs", "weight": 1.0} -->

Here, as before, $\pi_{\theta}{( \cdot |s)} = {softmax}{(\theta{(s, \cdot )})}$, $s \in \mathcal{S}$. Following Agarwal et al., the values here are defined with respect to an initial state distribution $\rho$ which may not be the same as the initial state distribution $\mu$ used in the gradient updates (cf. Algorithm 1), allowing for greater flexibility in our analysis. While the initial state distributions do not play any role in the bandit case, here, in the multi-state case, they have a strong influence.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 2 (Sufficient exploration)", "weight": 1.0} -->

2. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") was also adapted by Agarwal et al., which ensures "sufficient exploration" in the sense that the occupancy measure $d_{\mu}^{\pi}$ of any policy $\pi$ when started from $\mu$ will be guaranteed to be positive over the whole state space. Agarwal et al. asked whether this assumption is necessary for convergence to global optimality.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The improved dependence on $\epsilon$ (or $t$) in our result follows from Lemmas 8. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") and 9 and a different proof technique utilized to prove Theorem 4, while we pay a price because our bound depends on $c$, which adds an extra dependence on the MDP as well as on the initialization of the algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Entropy Regularized Policy Gradient", "weight": 1.0} -->

Agarwal et al. considered relative-entropy regularization in policy gradient to get an $O{({1/\sqrt{t}})}$ convergence rate. As they note, relative-entropy is more "agressive" in penalizing small probabilities than the more "common" entropy regularizer (cf. Remark 5.5 in their paper) and it remains unclear whether this latter regularizer leads to an algorithm with the same rate. In this section, we answer this positively and in fact prove a much better rate. In particular, we show that entropy regularized policy gradient with the softmax parametrization enjoys a linear rate of $O{(e^{- t})}$. In retrospect, perhaps this is unsurprising as entropy regularization bears a strong similarity to introducing a strongly convex regularizer in convex optimization, where this change is known to significantly improve the rate of convergence of first-order methods.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Maximum Entropy RL", "weight": 1.0} -->

In entropy regularized RL, or sometimes called maximum entropy RL, near-deterministic policies are penalized, which is achieved by modifying the value of a policy $\pi$ to

<!-- chunk {"id": "body-0036", "role": "body", "section": "Maximum Entropy RL", "weight": 1.0} -->

where ${\mathbb{H}}{(\rho,\pi)}$ is the "discounted entropy", defined as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Maximum Entropy RL", "weight": 1.0} -->

and $\tau \geq 0$, the "temperature", determines the strength of the penalty.^33^3 To better align with naming conventions in information-theory, discounted entropy should be rather called the discounted action-entropy rate as entropy itself in the literature on Markov chain information theory would normally refer to the entropy of the stationary distribution of the chain, while entropy rate refers to what is being used here. Clearly, the value of any policy can be obtained by adding an entropy penalty to the rewards (as proposed originally by Williams & Peng ).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Convergence Rates", "weight": 1.0} -->

As in the non-regularized case, to gain insight, we first consider MDPs with a single state and $\gamma = 0$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Bandit Case", "weight": 1.0} -->

In the one-state case with $\gamma = 0$, Eq. 15 reduces to maximizing the entropy-regularized reward,

<!-- chunk {"id": "body-0040", "role": "body", "section": "Bandit Case", "weight": 1.0} -->

Again, Eq. 20 is a non-concave function of $\theta$. In this case, regularized policy gradient reduces to

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 4", "weight": 1.0} -->

At this stage, we could use arguments similar to those of Section 3 to show the $O{({1/t})}$ convergence of $\pi_{\theta_{t}}$ to $\pi_{\tau}^{\ast}$. However, we can use an alternative idea to show that entropy-regularized policy gradient converges significantly faster. The issue of bias will be discussed later.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Our alternative idea is to show that Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2

<!-- chunk {"id": "body-0043", "role": "body", "section": "General MDPs", "weight": 1.0} -->

Using a somewhat lengthy calculation, we show that the discounted entropy in Eq.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Controlling the Bias", "weight": 1.0} -->

As noted in Remark 4, $\pi_{\tau}^{\ast}$ is biased, i.e., $\pi_{\tau}^{\ast} \neq \pi^{\ast}$ for fixed $\tau > 0$. We discuss two possible approaches to deal with the bias, but much remains to be done to properly address the bias. For simplicity, we consider the bandit case.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Decreasing the penalty", "weight": 1.0} -->

Another simple idea is to decrease the strength of regularization, e.g., set $\tau_{t} \in {O{({1/{\log t}})}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Update 3", "weight": 1.0} -->

The rationale for the scaling factor is that it allows one to prove a variant of Lemma 11. ‣ Softmax optimal policy. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). While this is promising, the proof cannot be finished as before. The difficulty is that $\pi_{\theta_{t}}\rightarrow\pi^{\ast}$ (which is what we want to achieve) implies that ${{\min_{a}\pi_{\theta_{t}}}{(a)}}\rightarrow 0$, which prevents the use of our previous proof technique. We show the following partial results.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Does Entropy Regularization Really Help?", "weight": 1.0} -->

The previous section indicated that entropy regularization may speed up convergence. In addition, ample empirical evidence suggest that this may be the case. In this section, we aim to provide new insights into why entropy may help policy optimization, taking an optimization perspective.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Does Entropy Regularization Really Help?", "weight": 1.0} -->

We start by establishing a lower bound that shows that the $O{({1/t})}$ rate we established earlier for softmax policy gradient without entropy regularization cannot be improved. Next, we introduce the notion of Łojasiewicz degree, which we show to increase in the presence of entropy regularization. We then connect a higher degree to faster convergence rates. Note that our proposal to view entropy regularization as an optimization aid is somewhat conflicting with the more common explanation that entropy regularization helps by encouraging exploration. While it is definitely true that entropy regularization encourages exploration, the form of exploration it encourages is not sensitive to epistemic uncertainty and as such it fails to provide a satisfactory solution to the exploration problem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

The purpose of this section is to establish that the $O{({1/t})}$ rates established earlier for unpenalized policy gradient is tight. To get lower bounds, we need to show that progress in every iteration cannot be too large. This holds when we can reverse the inequality in the Łojasiewicz inequality.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Our convergence rates in Section 3 match the lower bounds up to constant. However, the constant gap is large, e.g., $K^{2}$ in Theorem 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), and $\Delta^{2}$ in Theorem 9. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). The gap is because the reversed Łojasiewicz inequality of Lemma 17. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") uses $\Delta$, which is unavoidable when $\pi_{\theta}$ is close to $\pi^{\ast}$. We leave it as an open problem to close this gap.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 5", "weight": 1.0} -->

With the lower bounds established, we confirm that entropy regularization helps policy optimization by speeding up convergence, though the question remains as to the mechanism by which the improved convergence rate manifests itself.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We set out to study the convergence speed of softmax policy gradient methods with and without entropy regularization in the tabular setting. Here, the error is measured in terms of the sub-optimality of the policy obtained after some number of updates. Our main findings is that without entropy regularization, the rate is $\Theta{({1/t})}$, which is faster than rates previously obtained. Our analysis also uncovered an unpleasant dependence on the initial parameter values. With entropy regularization, the rate becomes linear, where now the constant in the exponent is influenced by the initial choice of parameters. Thus, our analysis shows that entropy regularization substantially changes the rate at which gradient methods converge. Our main technical innovation is the introduction of a non-uniform variant of the Łojasiewicz inequality. Our work leaves open a number of interesting questions: While we have some lower bounds, there remains some gaps to be filled between the lower and upper bounds. Other interesting directions are extending the results for alternative (e.g., restricted) policy parametrizations or studying policy gradient when the gradient must be estimated from data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

One also expects that non-uniform Łojasiewicz inequalities and the Łojasiewicz degree could also be put to good use in other areas of non-convex optimization.
