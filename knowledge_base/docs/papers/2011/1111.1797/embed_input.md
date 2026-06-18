<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Analysis of Thompson Sampling for the Multi-armed Bandit Problem

Topics include Thompson sampling, Multi-armed bandits, Bayesian algorithms, Regret analysis, Exploration exploitation, Stochastic bandits, Sequential decision making.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides one of the first logarithmic expected-regret analyses for Thompson sampling in stochastic multi-armed bandits. The paper helped move Thompson sampling from an empirically attractive Bayesian heuristic toward a theoretically grounded bandit algorithm, though with gap-dependent constants that later work refined.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The multi-armed bandit problem is a popular model for studying exploration/exploitation trade-off in sequential decision problems. Many algorithms are now available for this well-studied problem. One of the earliest algorithms, given by W. R. Thompson, dates back to 1933. This algorithm, referred to as Thompson Sampling, is a natural Bayesian algorithm. The basic idea is to choose an arm to play according to its probability of being the best arm. Thompson Sampling algorithm has experimentally been shown to be close to optimal. In addition, it is efficient to implement and exhibits several desirable properties such as small regret for delayed feedback. However, theoretical understanding of this algorithm was quite limited. In this paper, for the first time, we show that Thompson Sampling algorithm achieves logarithmic expected regret for the multi-armed bandit problem. More precisely, for the two-armed bandit problem, the expected regret in time T is O(fracln TDelta + 1/Delta^). And, for the N-armed bandit problem, the expected regret in time T is O([(sum_i = 2^(N) 1/Delta_i^)^] ln T).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our bounds are optimal but for the dependence on Delta_i and the constant factors in big-Oh.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-armed bandit (MAB) problem models the exploration/exploitation trade-off inherent in sequential decision problems. Many versions and generalizations of the multi-armed bandit problem have been studied in the literature; in this paper we will consider a basic and well-studied version of this problem: the stochastic multi-armed bandit problem. Among many algorithms available for the stochastic bandit problem, some popular ones include Upper Confidence Bound (UCB) family of algorithms, (e.g. and more recently ), which have good theoretical guarantees, and the algorithm, which gives optimal strategy under Bayesian setting with known priors and geometric time-discounted rewards. In one of the earliest works on stochastic bandit problems, proposed a natural randomized Bayesian algorithm to minimize regret. The basic idea is to assume a simple prior distribution on the parameters of the reward distribution of every arm, and at any time step, play an arm according to its posterior probability of being the best arm. This algorithm is known as *Thompson Sampling* (TS), and it is a member of the family of *randomized probability matching* algorithms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We emphasize that although TS algorithm is a Bayesian approach, the description of the algorithm and our analysis apply to the prior-free stochastic multi-armed bandit model where parameters of the reward distribution of every arm are fixed, though unknown (refer to Section 1.1). One could think of the "assumed" Bayesian priors as a tool employed by the TS algorithm to encode the current knowledge about the arms. Thus, our regret bounds for Thompson Sampling are directly comparable to the regret bounds for UCB family of algorithms which are a frequentist approach to the same problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, TS has attracted considerable attention. Several studies (e.g., ) have empirically demonstrated the efficacy of Thompson Sampling: provides a detailed discussion of probability matching techniques in many general settings along with favorable empirical comparisons with other techniques. demonstrate that empirically TS achieves regret comparable to the lower bound of; and in applications like display advertising and news article recommendation, it is competitive to or better than popular methods such as UCB. In their experiments, TS is also more robust to delayed or batched feedback (delayed feedback means that the result of a play of an arm may become available only after some time delay, but we are required to make immediate decisions for which arm to play next) than the other methods. A possible explanation may be that TS is a randomized algorithm and so it is unlikely to get trapped in an early bad decision during the delay. Microsoft's adPredictor for CTR prediction of search ads on Bing uses the idea of Thompson Sampling.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

It has been suggested that despite being easy to implement and being competitive to the state of the art methods, the reason TS is not very popular in literature could be its lack of strong theoretical analysis. Existing theoretical analyses in provide weak guarantees, namely, a bound of $o{(T)}$ on expected regret in time $T$. In this paper, for the first time, we provide a logarithmic bound on expected regret of TS algorithm in time $T$ that is close to the lower bound of. Before stating our results, we describe the MAB problem and the TS algorithm formally.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The multi-armed bandit problem", "weight": 1.0} -->

We consider the stochastic multi-armed bandit (MAB) problem: We are given a slot machine with $N$ arms; at each time step $t = {1,2,3,\ldots}$, one of the $N$ arms must be chosen to be played. Each arm $i$, when played, yields a random real-valued reward according to some fixed (unknown) distribution with support in $\lbrack 0,1\rbrack$. The random reward obtained from playing an arm repeatedly are i.i.d. and independent of the plays of the other arms. The reward is observed immediately after playing the arm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The multi-armed bandit problem", "weight": 1.0} -->

An algorithm for the MAB problem must decide which arm to play at each time step $t$, based on the outcomes of the previous $t - 1$ plays. Let $\mu_{i}$ denote the (unknown) expected reward for arm $i$. A popular goal is to maximize the expected total reward in time $T$, i.e., ${\mathbb{E}}{\lbrack{\sum_{t = 1}^{T}\mu_{i{(t)}}}\rbrack}$, where $i{(t)}$ is the arm played in step $t$, and the expectation is over the random choices of $i{(t)}$ made by the algorithm. It is more convenient to work with the equivalent measure of expected total *regret*: the amount we lose because of not playing optimal arm in each step. To formally define regret, let us introduce some notation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The multi-armed bandit problem", "weight": 1.0} -->

Other performance measures include PAC-style guarantees; we do not consider those measures here.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

The algorithm for Bernoulli bandits maintains Bayesian priors on the Bernoulli means $\mu_{i}$'s. Beta distribution turns out to be a very convenient choice of priors for Bernoulli rewards. Let us briefly recall that beta distributions form a family of continuous probability distributions on the interval $$. The pdf of $\text{Beta}{(\alpha,\beta)}$, the beta distribution with parameters $\alpha > 0$, $\beta > 0$, is given by ${f{(x;\alpha,\beta)}} = {\frac{\Gamma{({\alpha + \beta})}}{\Gamma{(\alpha)}\Gamma{(\beta)}}x^{\alpha - 1}{({1 - x})}^{\beta - 1}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

The mean of $\text{Beta}{(\alpha,\beta)}$ is $\alpha/{({\alpha + \beta})}$; and as is apparent from the pdf, higher the $\alpha,\beta$, tighter is the concentration of $\text{Beta}{(\alpha,\beta)}$ around the mean. Beta distribution is useful for Bernoulli rewards because if the prior is a $\text{Beta}{(\alpha,\beta)}$ distribution, then after observing a Bernoulli trial, the posterior distribution is simply $\text{Beta}{({\alpha + 1},\beta)}$ or $\text{Beta}{(\alpha,{\beta + 1})}$, depending on whether the trial resulted in a success or failure, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

The Thompson Sampling algorithm initially assumes arm $i$ to have prior $\text{Beta}{}$ on $\mu_{i}$, which is natural because $\text{Beta}{}$ is the uniform distribution on $$. At time $t$, having observed $S_{i}{(t)}$ successes (reward = $1$) and $F_{i}{(t)}$ failures (reward = $0$) in ${k_{i}{(t)}} = {{S_{i}{(t)}} + {F_{i}{(t)}}}$ plays of arm $i$, the algorithm updates the distribution on $\mu_{i}$ as $\text{Beta}{({{S_{i}{(t)}} + 1},{{F_{i}{(t)}} + 1})}$. The algorithm then samples from these posterior distributions of the $\mu_{i}$'s, and plays an arm according to the probability of its mean being the largest.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

We summarize the Thompson Sampling algorithm below.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

For each arm i = 1, …, N, sample θi (t) from the Beta (Si + 1,Fi + 1) distribution.
Play arm i (t):= arg maxiθi (t) and observe reward rt.
Algorithm 1 Thompson Sampling for Bernoulli bandits

<!-- chunk {"id": "body-0017", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

We adapt the Bernoulli Thompson sampling algorithm to the general stochastic bandits case, i.e. when the rewards for arm $i$ are generated from an arbitrary unknown distribution with support $\lbrack 0,1\rbrack$ and mean $\mu_{i}$, in a way that allows us to reuse our analysis of the Bernoulli case. To our knowledge, this adaptation is new. We modify TS so that after observing the reward ${\overset{\sim}{r}}_{t} \in {\lbrack 0,1\rbrack}$ at time $t$, it performs a Bernoulli trial with success probability $\overset{\sim}{r_{t}}$. Let random variable $r_{t}$ denote the outcome of this Bernoulli trial, and let $\{{S_{i}{(t)}},{F_{i}{(t)}}\}$ denote the number of successes and failures in the Bernoulli trials until time $t$. The remaining algorithm is the same as for Bernoulli bandits.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

Algorithm 2 gives the precise description of this algorithm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

We observe that the probability of observing a success (i.e., $r_{t} = 1$) in the Bernoulli trial after playing an arm $i$ in the new generalized algorithm is equal to the mean reward $\mu_{i}$. Let $f_{i}$ denote the (unknown) pdf of reward distribution for arm $i$. Then, on playing arm $i$,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

Thus, the probability of observing $r_{t} = 1$ is same and ${S_{i}{(t)}},{F_{i}{(t)}}$ evolve exactly in the same way as in the case of Bernoulli bandits with mean $\mu_{i}$. Therefore, the analysis of TS for Bernoulli setting is applicable to this modified TS for the general setting. This allows us to replace, for the purpose of analysis, the problem with general stochastic bandits with Bernoulli bandits with the same means. We use this observation to confine the proofs in this paper to the case of Bernoulli bandits only.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Thompson Sampling", "weight": 1.0} -->

For each arm i = 1, …, N, sample θi (t) from the Beta (Si + 1,Fi + 1) distribution.
Play arm i (t):= arg maxiθi (t) and observe reward ${\overset{\sim}{r}}_{t}$.
Perform a Bernoulli trial with success probability ${\overset{\sim}{r}}_{t}$ and observe output rt.
Algorithm 2 Thompson Sampling for general stochastic bandits

<!-- chunk {"id": "body-0022", "role": "body", "section": "Our results", "weight": 1.0} -->

In this article, we bound the *finite time* expected regret of Thompson Sampling. From now on we will assume that the first arm is the unique optimal arm, i.e., $\mu^{\ast} = \mu_{1} > {\arg{\max_{i \neq 1}\mu_{i}}}$. Assuming that the first arm is an optimal arm is a matter of convenience for stating the results and for the analysis. The assumption of *unique* optimal arm is also without loss of generality, since adding more arms with $\mu_{i} = \mu^{\ast}$ can only decrease the expected regret; details of this argument are provided in Appendix A.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

For the $N$-armed bandit problem, we can obtain an alternate bound of

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

by slight modification to the proof. The above bound has a better dependence on $N$ than in Theorem 2, but worse dependence on $\Delta_{i}s$. Here $\Delta_{min} = {\min_{i \neq 1}\Delta_{i}}$,$\Delta_{max} = {\max_{i \neq 1}\Delta_{i}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In interest of readability, we used big-Oh notation ^11^1For any two functions ${f{(n)}},{g{(n)}}$, ${f{(n)}} = {O{({g{(n)}})}}$ if there exist two constants $n_{0}$ and $c$ such that for all $n \geq n_{0}$, ${f{(n)}} \leq {cg{(n)}}$. to state our results. The exact constants are provided in the proofs of the above theorems. Let us contrast our bounds with the previous work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1", "weight": 1.0} -->

where $D$ denotes the KL divergence. They also gave algorithms asymptotically achieving this guarantee, though unfortunately their algorithms are not efficient.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1", "weight": 1.0} -->

For many settings of the parameters, the bound of Auer et al. is not far from the lower bound of Lai and Robbins. Our bounds are optimal in terms of dependence on $T$, but inferior in terms of the constant factors and dependence on $\Delta$. We note that for the two-armed case our bound closely matches the bound of. For the $N$-armed setting, the exponent of $\Delta$'s in our bound is basically $4$ compared to the exponent $1$ for UCB1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1", "weight": 1.0} -->

More recently, gave Bayes-UCB algorithm which achieves regret bounds close to the lower bound of for Bernoulli rewards. Bayes-UCB is a UCB like algorithm, where the upper confidence bounds are based on the quantiles of Beta posterior distributions. Interestingly, these upper confidence bounds turn out to be similar to those used by algorithms in and. Bayes-UCB can be seen as an hybrid of TS and UCB. However, the general structure of the arguments used in is similar to; for the analysis of Thompson Sampling we need to deal with additional difficulties, as discussed in the next section.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Main technical difficulties", "weight": 1.0} -->

Thompson Sampling is a randomized algorithm which achieves exploration by choosing to play the arm with best sampled mean, among those generated from beta distributions around the respective empirical means. The beta distribution becomes more and more concentrated around the empirical mean as the number of plays of an arm increases. This randomized setting is unlike the algorithms in UCB family, which achieve exploration by adding a *deterministic, non-negative* bias inversely proportional to the number of plays, to the observed empirical means. Analysis of TS poses difficulties that seem to require new ideas.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Main technical difficulties", "weight": 1.0} -->

For example, following general line of reasoning is used to analyze regret of UCB like algorithms in two-arms setting (for example, in ): once the second arm has been played sufficient number of times, its empirical mean is tightly concentrated around its actual mean. If the first arm has been played sufficiently large number of times by then, it will have an empirical mean close to its actual mean and larger than that of the second arm. Otherwise, if it has been played small number of times, its non-negative bias term will be large. Consequently, once the second arm has been played sufficient number of times, it will be played with very small probability (inverse polynomial of time) *regardless of the number of times the first arm has been played so far*.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Main technical difficulties", "weight": 1.0} -->

However, for Thompson Sampling, if the number of previous plays of the first arm is small, then the probability of playing the second arm could be as large as a constant even if it has already been played large number of times. For instance, if the first arm has not been played at all, then $\theta_{1}{(t)}$ is a uniform random variable, and thus ${\theta_{1}{(t)}} < {\theta_{2}{(t)}}$ with probability ${\theta_{2}{(t)}} \approx \mu_{2}$. As a result, in our analysis we need to carefully consider the distribution of the number of previous plays of the first arm, in order to bound the probability of playing the second arm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main technical difficulties", "weight": 1.0} -->

The observation just mentioned also points to a challenge in extending the analysis of TS for two-armed bandit to the general $N$-armed bandit setting. One might consider analyzing the regret in the $N$-armed case by considering only two arms at a time---the first arm and one of the suboptimal arms. We could use the observation that the probability of playing a suboptimal arm is bounded by the probability of it exceeding the first arm. However, this probability also depends on the number of previous plays of the two arms, which in turn depend on the plays of the other arms. Again in their analysis of UCB algorithm, overcome this difficulty by bounding this probability for *all possible numbers of previous plays* of the first arm, and large enough plays of the suboptimal arm. For Thompson Sampling, due to the observation made earlier, the (distribution of the) number of previous plays of the first arm needs to be carefully accounted, which in turn requires considering all the arms at the same time, thereby leading to a more involved analysis.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Regret bound for the two-armed bandit problem", "weight": 1.0} -->

In this section, we present a proof of Theorem 1, our result for the two-armed bandit problem. Recall our assumption that all arms have Bernoulli distribution on rewards, and that the first arm is the unique optimal arm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Regret bound for the two-armed bandit problem", "weight": 1.0} -->

Let random variable $j_{0}$ denote the number of plays of the first arm until $L = {{24{({\ln T})}}/\Delta^{2}}$ plays of the second arm. Let random variable $t_{j}$ denote the time step at which the $j^{th}$ play of the first arm happens (we define $t_{0} = 0$). Also, let random variable $Y_{j} = {t_{j + 1} - t_{j} - 1}$ measure the number of time steps between the $j^{th}$ and ${({j + 1})}^{th}$ plays of the first arm (not counting the steps in which the $j^{th}$ and ${({j + 1})}^{th}$ plays happened), and let $s{(j)}$ denote the number of successes in the first $j$ plays of the first arm. Then the expected number of plays of the second arm in time $T$ is bounded by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Regret bound for the two-armed bandit problem", "weight": 1.0} -->

To understand the expectation of $Y_{j}$, it will be useful to define another random variable $X{(j,s,y)}$ as follows. We perform the following experiment until it succeeds: check if a $\text{Beta}{({s + 1},{{j - s} + 1})}$ distributed random variable exceeds a threshold $y$. For each experiment, we generate the beta-distributed r.v. independently of the previous ones. Now define $X{(j,s,y)}$ to be the number of trials *before* the experiment succeeds. Thus, $X{(j,s,y)}$ takes non-negative integer values, and is a geometric random variable with parameter (success probability) $1 - {F_{{s + 1},{{j - s} + 1}}^{beta}{(y)}}$. Here $F_{\alpha,\beta}^{beta}$ denotes the cdf of the beta distribution with parameters $\alpha,\beta$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Regret bound for the two-armed bandit problem", "weight": 1.0} -->

Also, let $F_{n,p}^{B}$ denote the cdf of the *binomial* distribution with parameters $(n,p)$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regret bound for the two-armed bandit problem", "weight": 1.0} -->

We will relate $Y$ and $X$ shortly. The following lemma provides a handle on the expectation of $X$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

In this section, we prove Theorem 2, our result for the $N$-armed bandit problem. Again, we assume that all arms have Bernoulli distribution on rewards, and that the first arm is the unique optimal arm.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

At every time step $t$, we divide the set of suboptimal arms into saturated and unsaturated arms. We say that an arm $i \neq 1$ is in the saturated set $C{(t)}$ at time $t$, if it has been played at least $L_{i}:=\frac{24{\ln T}}{\Delta_{i}^{2}}$ times before time $t$. We bound the regret due to playing unsaturated and saturated suboptimal arms separately. The former is easily bounded as we will see; most of the work is in bounding the latter. For this, we bound the number of plays of saturated arms between two consecutive plays of the first arm.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

In the following, by an interval of time we mean a set of contiguous time steps. Let r.v. $I_{j}$ denote the interval between (and excluding) the $j^{th}$ and ${({j + 1})}^{th}$ plays of the first arm. We say that event $M{(t)}$ holds at time $t$, if $\theta_{1}{(t)}$ exceeds $\mu_{i} + \frac{\Delta_{i}}{2}$ of all the saturated arms, i.e.,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

For $t$ such that $C{(t)}$ is empty, we define $M{(t)}$ to hold trivially.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

Then, the number of plays of saturated arms in interval $I_{j}$ is at most

<!-- chunk {"id": "body-0043", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

In words, $E{(t)}$ denotes the event that all saturated arms have $\theta_{i}{(t)}$ tightly concentrated around their means. Intuitively, from the definition of saturated arms, $E{(t)}$ should hold with high probability; we prove this in Lemma 4.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

We are interested in bounding regret due to playing saturated arms, which depends not only on the number of plays, but also on *which* saturated arm is played at each time step. Let $V_{j}^{\ell,a}$ denote the number of steps in $I_{j}{(\ell)}$, for which $a$ is the best saturated arm, i.e.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

(resolve the ties for best saturated arm using an arbitrary, but fixed, ordering on arms). In Figure 1, we illustrate this notation by showing steps $\{ V_{j}^{4,a}\}$ for interval $I_{j}{}$. In the example shown, we assume that $\mu_{1} > \mu_{2} > \cdots > \mu_{6}$, and that the suboptimal arms got added to the saturated set $C{(t)}$ in order $5,3,4,2,6$, so that initially $5$ is the best saturated arm, then $3$ is the best saturated arm, and finally $2$ is the best saturated arm.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

Recall that $M{(t)}$ holds trivially for all $t$ such that $C{(t)}$ is empty. Therefore, there is at least one saturated arm at all $t \in {I_{j}{(\ell)}}$, and hence ${{V_{j}^{\ell,a},a} = 2},{\ldots,N}$ are well defined and cover the interval $I_{j}{(\ell)}$,

<!-- chunk {"id": "body-0047", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

Next, we will show that the regret due to playing a saturated arm at a time step $t$ in one of the $V_{j}^{\ell,a}$ steps is at most ${3\Delta_{a}} + {I{(\overline{E{(t)}})}}$. The idea is that if all saturated arms have their $\theta_{i}{(t)}$ tightly concentrated around their means $\mu_{i}$, then either the arm with the highest mean (i.e., the best saturated arm $a$) or an arm with mean very close to $\mu_{a}$ will be chosen to be played during these $V_{j}^{\ell,a}$ steps.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

That is, if a saturated arm $i$ is played at a time $t$ among one of the $V_{j}^{\ell,a}$ steps, then, either $E{(t)}$ is violated, i.e. $\theta_{i^{\prime}}{(t)}$ for some saturated arm $i^{\prime}$ is not close to its mean, or

<!-- chunk {"id": "body-0049", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

Therefore, regret due to play of a saturated arm at a time $t$ in one of the $V_{j}^{\ell,a}$ steps is at most ${3\Delta_{a}} + {I{(\overline{E{(t)}})}}$. With slight abuse of notation let us use $t \in V_{j}^{\ell,a}$ to indicate that $t$ is one of the $V_{j}^{\ell,a}$ steps in $I_{j}{(\ell)}$. Then, the expected regret *due to playing saturated arms* in interval $I_{j}$ is bounded as

<!-- chunk {"id": "body-0050", "role": "body", "section": "Regret bound for the $N$-armed bandit problem", "weight": 1.0} -->

The following lemma will be useful for bounding the second term on the right hand side in the above equation (as shown in the complete proof in Appendix D).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we showed theoretical guarantees for Thompson Sampling close to other state of the art methods, like UCB. Our result is a first step in theoretical understanding of TS and there are several avenues to explore for the future work: There is a gap between our upper bounds and the lower bound of. While it may be easy to improve the constant factors in our upper bounds by making the analysis more careful (but more complicated), it seems harder to improve the dependence on the $\Delta$'s. With further work, we hope that our techniques in this paper will be useful in providing several extensions, including analysis of TS for delayed and batched feedbacks, contextual bandits, prior mismatch and posterior reshaping discussed. As mentioned before, empirically TS has been shown to have superior performance than other methods, especially for handling delayed feedback. A theoretical justification of this observation would require a tighter analysis of TS than what we have achieved here, and in addition, it would require lower bound on the regret of the other algorithms. TS has also been used for problems such as regularized logistic regression (see ). These multi-parameter settings lack theoretical analysis.
