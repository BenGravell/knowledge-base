<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Complexity of Best-Arm Identification in Non-Stationary Linear Bandits

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the fixed-budget best-arm identification (BAI) problem in non-stationary linear bandits. Concretely, given a fixed time budget Tin N, finite arm set X subset R^(d), and a potentially adversarial sequence of unknown parameters lbrace theta_trbrace_t = 1^(T) (hence non-stationary), a learner aims to identify the arm with the largest cumulative reward x_* = argmax_x in X x^(top)sum_t = 1^(T) theta_t with high probability. In this setting, it is well-known that uniformly sampling arms from the G-optimal design yields a minimax-optimal error probability of exp(-Theta(T / H_G)), where H_G scales proportionally with the dimension d. However, this notion of complexity is overly pessimistic, as it is derived from a lower bound in which the arm set consists only of the standard basis vectors, thus masking any potential advantages arising from arm sets with richer geometric structure. To address this, we establish an arm-set-dependent lower bound that, in contrast, holds for any arm set.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motivated by the ideas underlying our lower bound, we propose the Adjacent-optimal design, a specialization of the well-known XY-optimal design, and develop the textsfAdjacent-BAI algorithm. We prove that the error probability of textsfAdjacent-BAI matches our lower bound up to constants, verifying the tightness of our lower bound, and establishing the arm-set-dependent complexity of this setting.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on quantifying the difficulty of fixed-budget best-arm identification (BAI) problem in non-stationary linear bandits. The linear bandit framework generalizes the classical multi-armed bandit problem by associating each arm with a feature vector and modeling rewards as linear in an unknown parameter. Algorithms such as UCB and Thompson Sampling are known to perform optimally in the well-studied regret-minimization setting. However, in the best-arm identification setting, where exploration is more important than cumulative reward, these algorithms are suboptimal, thus requiring specialized attention. In the standard BAI setting, a stationary environment is assumed where the rewards of arms are sampled i.i.d. However, algorithms designed for these environments can completely fail as soon as this assumption is lifted, for example, in settings where the value of an arm can change at any time step. An interesting question is *exactly how the difficulty of this setting changes once this stationary assumption is lifted*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent work, Xiong et al. partially answered this question by showing that when the arm set is restricted to the standard basis, the difficulty of non-stationary BAI scales proportionally with the dimension. While informative, this result is ultimately unsatisfying as it collapses the linear bandit model back into a multi-armed bandit. Basis arm sets erase correlations between arms, precisely the geometric structure that linear bandits are meant to exploit. With this in mind, we aim to uncover precisely which relationship between arms truly governs the difficulty of non-stationary BAI. Inspired by Soare et al., a natural conjecture is that the pairwise relationships between every arm should be considered when measuring difficulty. However, such a characterization implies that any arm set containing a basis is no easier than the basis itself, and thus no progress is made. To refine this view, we introduce adjacency, a geometric notion that captures which pairs of arms can compete for optimality. Accordingly, we find that the pairwise relationships between adjacent arms are necessary and sufficient to measure the difficulty of non-stationary BAI.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Formally, by leveraging the adjacent structure of the arm set, we refine the previous notion of difficulty in non-stationary BAI by establishing a measure of complexity that adapts to the geometry of any arm set, which we term as arm-set-dependent.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Adjacency and Non-Stationary BAI. The main novelty of our paper stems from our characterization of non-stationary BAI as a problem of differentiating only between adjacent arms, a notion we formalize in later sections. The intuition for this restriction stems from our central Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), which implies that if an arm is better than its adjacent arms, then it is the optimal arm. Accordingly, we introduce a new arm-set-dependent complexity measure $H_{Adjacent}{(\mathcal{X})}$ and show it strictly refines the minimax-optimal complexity $H_{G}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Arm-set-dependent lower bound. We show in Theorem 1 that for fixed arm set $\mathcal{X}$, the error probability of any algorithm must be at least $\exp\left( {- {O\left( {{T/H_{Adjacent}}{(\mathcal{X})}} \right)}} \right)$. Our lower bound builds off of previous works concerning lower bounds in best-arm identification for the multi-armed bandit setting. However, these methods alone are not sufficient for the linear setting, which we address by characterizing the lower bound as an optimization problem in Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), and which we solve in Lemma 4 by exploiting the adjacent geometry of the arm set.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Matching upper bound. We introduce the Adjacent-optimal design, a specialization of the well-known $\mathcal{X}\mathcal{Y}$-optimal design, that instead reduces variance only between adjacent arms. Using the Adjacent-optimal design, we introduce the algorithm Adjacent-BAI. Utilizing Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), we obtain Theorem 2.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") showing that for fixed arm set $\mathcal{X}$, the error probability of Adjacent-BAI is at most $\exp\left( {- {\Omega\left( {{T/H_{Adjacent}}{(\mathcal{X})}} \right)}} \right)$, verifying the tightness of our lower bound, and establishing $H_{Adjacent}{(\mathcal{X})}$ as the arm-set-dependent complexity measure of this setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Best-arm identification with fixed confidence", "weight": 1.0} -->

For multi-armed bandits, Even-Dar et al. established the first sample-complexity upper bound, with a nearly matching lower bound later given by Mannor and Tsitsiklis. These bounds were subsequently tightened by Karnin et al. and Kaufmann et al.. Notably, Kaufmann et al. derived a general information-theoretic lower bound that underpins many linear-bandit lower bounds. In linear bandits, Soare et al. proposed the seminal $\mathcal{X}\mathcal{Y}$-allocation strategy, which has been refined and generalized in follow-up work. Nearly matching lower bounds were also established by Fiez et al. and Jedra and Proutiere.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Best-arm identification with fixed budget", "weight": 1.0} -->

For multi-armed bandits, Audibert and Bubeck provided nearly matching upper and lower bounds, with improvements due to Karnin et al. and Kaufmann et al.. In contrast, comparatively little is known for linear bandits in this setting. Among existing results, Katz-Samuels et al. ---via a Gaussian-width analysis---gave the only arm-set-dependent upper bound. Methods based on G-optimal design yield arm-set-*independent* guarantees, as does the Bayesian-style approach of Hoffman et al.; similarly, a method based on the $\mathcal{X}\mathcal{Y}$-design in Alieva et al. remains arm-set-independent. On the lower-bound side, Yang and Tan proved a minimax bound, but to date, there is no arm-set-dependent lower bound for stationary linear bandits in the fixed-budget setting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Best-arm identification in non-stationary environments", "weight": 1.0} -->

Compared with regret minimization, non-stationarity has received less attention in BAI. In the fixed-confidence regime, non-stationary multi-armed bandits under models different from ours were studied by Jamieson and Talwalkar and Li et al.. In the fixed-budget regime, Abbasi-Yadkori et al. analyzed multi-armed bandits from a best-of-both-worlds perspective and established matching upper and lower bounds in a non-stationary setting; Xiong et al. extended the upper bounds to linear bandits. However, Xiong et al. does not provide lower bounds, and its non-stationary guarantees are arm-set-independent. Our work adopts a non-stationary model similar to Abbasi-Yadkori et al. and Xiong et al. and, to the best of our knowledge, presents the first arm-set-dependent lower bound for the fixed-budget setting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "BAI in Non-Stationary Linear Bandits", "weight": 1.0} -->

A central measure of difficulty in bandit problems is the reward gap between the first and second best arm. Here, we deviate slightly from the standard definition by defining this gap only in terms of extreme points $\mathcal{V}$. This restriction is natural since by definition, non-extreme point arms can never be the best arm, and thus do not affect problem difficulty.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Minimax-Optimal Complexity in Non-Stationary BAI", "weight": 1.0} -->

In prior work in the non-stationary setting, Xiong et al. showed that uniform sampling from the well-known G-optimal design

<!-- chunk {"id": "body-0016", "role": "body", "section": "Minimax-Optimal Complexity in Non-Stationary BAI", "weight": 1.0} -->

The relationship between $H_{G}$ and the G-optimal design stems from the Kiefer--Wolfowitz Theorem, which states that

<!-- chunk {"id": "body-0017", "role": "body", "section": "Minimax-Optimal Complexity in Non-Stationary BAI", "weight": 1.0} -->

$H_{G}$ is minimax-optimal since if the arm set is restricted to the standard basis vectors, $H_{G}$ matches the optimal complexity for the multi-armed bandit setting of $H_{UNIF} = \frac{K}{\Delta_{}^{2}}$. However, this notion of complexity is overly pessimistic in the linear bandit setting as it ignores potential advantages arising from arm sets with more complex structure. In contrast, we refine this notion of complexity by establishing an arm-set-dependent complexity that adapts to the geometry of any given arm set.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Adjacency and Non-Stationary BAI", "weight": 1.0} -->

The main results of our paper are motivated by the following central lemma.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Lower Bound of BAI in Non-Stationary Linear Bandits", "weight": 1.0} -->

We present, to the best of our knowledge, the first arm-set-dependent lower bound for BAI in the non-stationary linear bandit setting.

<!-- chunk {"id": "body-0020", "role": "body", "section": "First step", "weight": 1.0} -->

We use Lemma 2 to obtain Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") which states the following.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Second step", "weight": 1.0} -->

We bound the previous optimization problem by solving the following relaxed version of the optimization problem introduced in Lemma 3. ‣ First step. ‣ 5.1

<!-- chunk {"id": "body-0022", "role": "body", "section": "Second step", "weight": 1.0} -->

This is a relaxation because $\hat{f}\left( \mathcal{X},\Delta_{} \right)$ minimizes only over adjacent pairs ${(x,x^{\prime})} \in \mathcal{I}$ rather than all extreme point pairs ${(x,x^{\prime})} \in \mathcal{Y}$. Since, $\mathcal{I} \subseteq \mathcal{Y}$, and hence ${\hat{f}\left( \mathcal{X},\Delta_{} \right)} \geq {f\left( \mathcal{X},\Delta_{} \right)}$, we can substitute $f$ by $\hat{f}$ in the bound corresponding to Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

<!-- chunk {"id": "body-0023", "role": "body", "section": "Second step", "weight": 1.0} -->

Requiring $(x,x^{\prime})$ to be adjacent is crucial: it enables a closed-form solution of the inner $(\theta,v)$ problem, described by the following lemma.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Matching Upper Bound", "weight": 1.0} -->

In this section, we first introduce the Adjacent-optimal design, which is a modified version of the well-known $\mathcal{X}\mathcal{Y}$-optimal design. Based on this new design, we then develop the algorithm Adjacent-BAI, and show that it achieves an error probability guarantee that matches the lower bound presented in Section 5, verifying the tightness of our lower bound, and establishing the arm-set-dependent complexity of this setting.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Adjacent-Optimal Design", "weight": 1.0} -->

A central quantity in BAI problems is the $\mathcal{X}\mathcal{Y}$-optimal design, which aims to uniformly minimize the variance of predictions in directions defined by the pairwise differences between all arms. Formally, the $\mathcal{X}\mathcal{Y}$-optimal design is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Adjacent-Optimal Design", "weight": 1.0} -->

The relevance of the $\mathcal{X}\mathcal{Y}$-optimal design stems from the ranking nature of BAI; identifying the best arm only requires accurate estimates of the relative ordering between arms. Motivated by Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), we refine this idea by introducing the Adjacent-optimal design, which uniformly minimizes the variance over differences only between adjacent arms. Formally, it is defined as

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Adjacent-Optimal Design", "weight": 1.0} -->

Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") implies that if an arm is better than all its adjacent arms, then it must be the optimal arm. Thus, when identifying the best arm, only accurate comparisons between adjacent arms are needed. The Adjacent-optimal design embodies this principle: reducing the variance of estimation of the relative ordering between adjacent arms is sufficient for identifying the best arm. Focusing on fewer, more informative directions leads to stronger estimation, which we make use of in the algorithm presented in the next section.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Adjacent-Optimal Best-Arm Identification (Adjacent-BAI)", "weight": 1.0} -->

We now present the algorithm Adjacent-BAI. In the first step, we compute the adjacent set $\mathcal{I}$, for which we provide a polynomial-time procedure in Appendix C. We then compute the Adjacent-optimal design $\lambda^{\ast}$; however, we do not proceed by sampling directly from it. In order to obtain an optimal error rate using random sampling we would require an estimator that (i) admits sub-Gaussian, variance-only error and (ii) does not require a prespecified confidence level^22^2This requirement is unnecessary in the fixed-confidence setting, hence the use of Catoni's estimator in Camilleri et al... According to Devroye et al., this is impossible without stronger distributional assumptions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Adjacent-Optimal Best-Arm Identification (Adjacent-BAI)", "weight": 1.0} -->

Instead, we employ the classical rounding procedure of Pukelsheim to obtain a static allocation $\left\{ x_{t} \right\}_{t = 1}^{T}$ such that the empirical design matrix $\frac{1}{T}{\sum_{t = 1}^{T}{x_{t}x_{t}^{\top}}}$ approximates the optimal design matrix ${A{(\lambda^{\ast})}} = {\sum_{x \in \mathcal{X}}{\lambda_{x}^{\ast}xx^{\top}}}$. Specifically, the rounding procedure guarantees that if $T \geq d^{2}$,^33^3We note the existence of a rounding procedure requiring only $T \geq {\Omega{(d)}}$ at the cost of significantly looser constants. An insightful discussion on both rounding procedures is provided in Appendix B of Fiez et al..

<!-- chunk {"id": "body-0030", "role": "body", "section": "Adjacent-Optimal Best-Arm Identification (Adjacent-BAI)", "weight": 1.0} -->

Then, to ensure our estimator is unbiased, we inject the necessary randomness by playing the allocation in a uniformly random order. Finally, we compute the least-squares estimator ${\hat{\theta}}_{T}$ and output its corresponding best arm. The complete procedure is summarized in Algorithm 1 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

<!-- chunk {"id": "body-0031", "role": "body", "section": "Adjacent-Optimal Best-Arm Identification (Adjacent-BAI)", "weight": 1.0} -->

We characterize the error probability of Algorithm 1 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") in the following theorem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "First step", "weight": 1.0} -->

The statistical analysis of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") relies primarily on the following lemma.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Second step", "weight": 1.0} -->

Finally, we combine Lemmas 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") and 5. ‣ First step. ‣ 6.3 Proof Sketch of Theorem 2 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") to obtain the final bound in Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"). We aim to bound the error probability

<!-- chunk {"id": "body-0034", "role": "body", "section": "Second step", "weight": 1.0} -->

However, critically, by Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), we have

<!-- chunk {"id": "body-0035", "role": "body", "section": "Second step", "weight": 1.0} -->

Applying the union bound, we have

<!-- chunk {"id": "body-0036", "role": "body", "section": "Second step", "weight": 1.0} -->

Fix some $x \in \mathcal{I}^{x_{\ast}}$. Combining Lemma 5. ‣ First step. ‣ 6.3 Proof Sketch of Theorem 2 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") and Hoeffding's inequality we have

<!-- chunk {"id": "body-0037", "role": "body", "section": "Second step", "weight": 1.0} -->

Using that ${(x,x_{\ast})} \in \mathcal{I}$, and incorporating the rounding error from Eq. (36 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits")), we have

<!-- chunk {"id": "body-0038", "role": "body", "section": "Second step", "weight": 1.0} -->

Observing that, by definition of $\lambda^{\ast}$

<!-- chunk {"id": "body-0039", "role": "body", "section": "Second step", "weight": 1.0} -->

completes the proof of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

<!-- chunk {"id": "body-0040", "role": "body", "section": "Future Work", "weight": 1.5} -->

The most promising future direction is investigating whether adjacency can be leveraged to establish a stronger notion of complexity for the stationary fixed-budget setting. In the stationary fixed-budget setting, currently, no lower bound exists outside of a pessimistic minimax-optimal lower bound derived from a multi-armed bandit reduction. However, in the stationary fixed-confidence setting, it is well-known that for arm set $\mathcal{X}$, and parameter vector $\theta$, the instance-optimal sample complexity is of order
