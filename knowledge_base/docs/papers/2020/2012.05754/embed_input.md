<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Thompson Sampling Strategies for Support-aware CVaR Bandits

Topics include Bandits, Regret bounds, Sampling, Conditional value at risk, Thompson sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we study a multi-arm bandit problem in which the quality of each arm is measured by the Conditional Value at Risk (CVaR) at some level alpha of the reward distribution. While existing works in this setting mainly focus on Upper Confidence Bound algorithms, we introduce a new Thompson Sampling approach for CVaR bandits on bounded rewards that is flexible enough to solve a variety of problems grounded on physical resources. Building on a recent work by Riou & Honda, we introduce B-CVTS for continuous bounded rewards and M-CVTS for multinomial distributions. On the theoretical side, we provide a non-trivial extension of their analysis that enables to theoretically bound their CVaR regret minimization performance. Strikingly, our results show that these strategies are the first to provably achieve asymptotic optimality in CVaR bandits, matching the corresponding asymptotic lower bounds for this setting. Further, we illustrate empirically the benefit of Thompson Sampling approaches both in a realistic environment simulating a use-case in agriculture and on various synthetic examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the past few years, a number of works have focused on adapting multi-armed bandit strategies (see e.g. Lattimore and Szepesvari ) to optimize an other criterion than the expected cumulative reward. Sani et al., Vakili and Zhao, Vakili and Zhao, Zimin et al. consider a mean-variance criterion, studies a quantile (Value-at-Risk) criterion, focuses on Entropic-value-at-risk. The Conditional Value at Risk (CVaR) as well as more generic coherent spectral risk measures have received specific attention from the bandit community (Galichet et al.; Galichet; Cassel et al.; Zhu and Tan; Tamkin et al.; Prashanth et al. to cite a few). Indeed, in a large number of application domains (healthcare, agriculture, marketing,...), one needs to take into account personalized preferences of the practitioner that are not captured by the expected reward. We consider an illustrative use-case in agriculture in section 4, where an algorithm recommends planting dates to farmers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Conditional Value at Risk (CVaR) at level $\alpha \in {\lbrack 0,1\rbrack}$ (see Mandelbrot, Artzner et al.) is easily interpretable as the expected reward in the worst $\alpha$-fraction of the outcomes, and hence captures different preferences, from being neutral to the shape of the distribution ($\alpha = 1$, mean criterion) to trying to maximize the reward in the worst-case scenarios ($\alpha$ close to 0, typically in finance or insurance). It is further a coherent spectral measure in the sense of Rockafellar et al., see Acerbi and Tasche). Several definitions of the CVaR exist in the literature, depending on whether the samples are considered as losses or as rewards. Brown, Thomas and Learned-Miller and Agrawal et al. consider the loss version of CVaR. We here follow Galichet et al. and Tamkin et al. who use the reward version, defined for arm $k$ with distribution $\nu_{k}$ as This implies that the best arm is the one with the largest CVaR.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other notions of regret have been studied for risk-averse bandits, e.g. computing the risk metric of the full trajectory of observed rewards (Sani et al.; Cassel et al.; Maillard), but are less interpretable.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In finance CVaR is often associated to heavy-tail distributions. Other variants of bandits have been considered to deal with possibly heavy-tail distributions, or weak moment conditions: In, the authors study regret minimization for extreme statistics (the maximum), for Weibull of Frechet-like distributions. In, a median-of-mean estimator is studied to minimize regret for distributions with bounded kurtosis. A CVaR strategy has been proposed for the different pure exploration setting, under weak moment conditions. These works consider a different setup and objective.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we purposely focus on minimizing the CVaR regret considering either distributions with discrete, finite support, or with continuous and bounded support, as we believe this has great practical relevance and is still a relatively unexplored topic in the literature. More precisely, we target first-order asymptotic optimality for these (sometimes called "non-parametric\") families and first derive in Theorem 1. ‣ 3.1 Asymptotic Optimality in CVaR bandits ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") a lower-bound on the CVaR regret, adapting that of to the CVaR criterion. This simple result highlights the right complexity term that should appear when deriving regret upper bounds. We then introduce in Section 2 B-CVTS for CVaR bandits with bounded support, and M-CVTS for CVaR bandits with multinomial arms, adapting the strategies proposed by Riou and Honda for the CVaR. We provide in Theorem 2. ‣ 3.2 Regret Guarantees for M-CVTS and B-CVTS ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") and Theorem 3.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

‣ 3.2 Regret Guarantees for M-CVTS and B-CVTS ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") the regret bound of each algorithm, proving asymptotic optimality of these strategies. Up to our knowledge, these are the first results showing asymptotic optimality of a Thompson Sampling based CVaR regret minimization strategy. As expected, adapting the regret analysis from Riou and Honda is non-trivial; we highlight the main challenges of this adaption in section 3.3. For instance, one of the key challenge was to handle boundary crossing probability for the CVaR, and another difficulty comes in the analysis of the non-parametric B-CVTS due to regularity properties of the Kulback-Leibler projection. In Section 4, we provide a case study in agriculture, making the well-established DSSAT agriculture simulator available to the bandit community, and highlight the benefits of using strategies based on Thompson Sampling in this CVaR bandit setting against state-of-the-art baselines: We compare to U-UCB and CVaR-UCB^22^2MaRaB is similar to U-UCB but enjoys weaker guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

as they showcase two fundamentally different approaches to build a UCB strategy for a non-linear utility function. The first one is closely related to UCB, the second one exploits properties of the underlying CDF, which may generalize to different risk metrics. As claimed in Tamkin et al., our experiments confirm that CVaR-UCB generally performs better than U-UCB. However, both TS strategies outperform UCB algorithms that tend to suffer from non-optimized confidence bounds. We complete this study with more classical experiments on synthetic data that also confirm the benefit of TS.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Thompson Sampling Algorithms", "weight": 1.0} -->

We present two novel algorithms based on Thompson Sampling and targeting the lower bound of Theorem 1. ‣ 3.1 Asymptotic Optimality in CVaR bandits ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") on the CVaR-regret, for any specified value of $\alpha \in {(0,1\rbrack}$. These algorithms are inspired by the first algorithms based on Thompson Sampling matching the Burnetas and Katehakis lower bound for bounded distributions in the expectation setting, recently proposed by Riou and Honda.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Notations", "weight": 1.0} -->

We introduce the notation $C_{\alpha}{(\mathcal{X},p)}$ for the CVaR of the distribution of support $\mathcal{X}$ and probability $p \in \mathcal{P}^{|\mathcal{X}|}$, where $\mathcal{P}^{n}$ denotes the probability simplex of size $n$. For a multinomial arm $k$ we denote its known support $\mathcal{X}_{k} = {(x_{k}^{1},\ldots,x_{k}^{M_{k}})}$ for some $M_{k} \in {\mathbb{N}}$, and its true probability vector $p_{k}$. We also define $N_{k}^{i}{(t)}$ as the number of times the algorithm has observed $x_{k}^{i}$ for arm $k$ before the time $t$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Notations", "weight": 1.0} -->

For general bounded distributions we denote $\nu_{k}$ the distribution of arm $k$ and introduce $\mathcal{X}_{k,t}$ the set of its observed rewards before time $t$, augmented with a known upper bound $B_{k}$ for the support of $\nu_{k}$. We further introduce $\mathcal{D}_{n}$ as the uniform distribution on the simplex $\mathcal{P}^{n}$, corresponding to the Dirichlet distribution ${Dir}{({(1,\ldots,1)}}$).

<!-- chunk {"id": "body-0013", "role": "body", "section": "M-CVTS", "weight": 1.0} -->

Thompson Sampling (or posterior sampling) is a general Bayesian principle that can be traced back to the work of Thompson, and that is now investigated for many sequential decision making problems (see Russo et al. for a survey). Given a prior distribution on the bandit model, Thompson Sampling is a randomized algorithm that selects each arm according to its posterior probability of being optimal. This can be implemented by drawing a possible model from the posterior distribution, and acting optimally in the sampled model. For multinomial distribution M-CVTS (Multinomial-CVaR-Thompson-Sampling), described in Algorithm 1, follows this principle. For each arm $k$, $p_{k}$ is assumed to be drawn from $\mathcal{D}_{M_{k}}$, the uniform prior on $\mathcal{P}^{M_{k}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "M-CVTS", "weight": 1.0} -->

Input: Level α, horizon T, K, supports 𝒳1, …, 𝒳K Init.: t ← 1, ∀k ∈ {1, …, K}, $\beta_{k} = \underset{M_{k}}{\underbrace{(1,\ldots,1)}}$ Pull arm At = argmaxk ∈ {1, …, K} ck, t. Update βAt (j) = βAt (j) + 1, for j as rt, At = xkj

<!-- chunk {"id": "body-0015", "role": "body", "section": "B-CVTS", "weight": 1.0} -->

We further introduce the B-CVTS algorithm (for Bounded-CVaR-Thompson-Sampling) for general bounded distributions. B-CVTS, stated as Algorithm 2, bears some similarity with a Thompson Sampling algorithm, although it does not explicitly use a prior distribution. The algorithm retains the idea of using a noisy version of $\nu_{k}$, obtained by a random re-weighting of the previous observations. Hence, at a time $t$ the index used by the algorithm for an arm $k$ is simply $c_{k,t} = {C_{\alpha}{(\mathcal{X}_{k,t},w_{k,t})}}$, where $w_{k,t} \sim \mathcal{D}_{N_{k}{(t)}}$ is drawn uniformly at random in the simplex $\mathcal{P}^{|\mathcal{X}_{k,t}|}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "B-CVTS", "weight": 1.0} -->

B-CVTS then selects the arm $A_{t} = {\text{argmax}_{k}c_{k,t}}$. For $\alpha = 1$, this algorithm coincides with the Non Parametric Thompson Sampling of Riou and Honda (NPTS). NPTS can be seen as an algorithm that computes for each arm a random average of the past observations. Our extension to CVAR-bandits required to interpret this operation as the computation of the *expectation* of a random perturbation of the empirical distribution, which can be replaced by the computation of the CVaR of this new distribution. Note that this idea generalizes beyond using the CVaR, that can be replaced with any criterion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "B-CVTS", "weight": 1.0} -->

Input: Level α, horizon T, K, upper bounds B1, …, BK Pull arm At = argmaxk ∈ {1, …, K} ck, t. Update 𝒳At = 𝒳At ∪ {rt, At}, NAt = NAt + 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Interestingly, B-CVTS also applies to multinomial distributions (that are bounded). The resulting strategy differs from M-CVTS due to the initialization step using the knowledge of the support in M-CVTS.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

In this section we prove, after defining this notion, that M-CVTS and B-CVTS are asymptotically optimal in terms of the CVaR regret for the distributions they cover.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Asymptotic Optimality in CVaR bandits", "weight": 1.0} -->

Lai and Robbins first gave an asymptotic lower bound on the regret for parameteric distribution, that was later extended by Burnetas and Katehakis to more general classes of distributions. We present below an intuitive generalization of this result for CVaR bandits.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Regret Guarantees for M-CVTS and B-CVTS", "weight": 1.0} -->

Our main result is the following regret bound for M-CVTS, showing that it is matching the lower bound of Theorem 1. ‣ 3.1 Asymptotic Optimality in CVaR bandits ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") for multinomial distributions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Technical challenges and tools", "weight": 1.0} -->

The proofs of, and follow the outline of Riou and Honda, respectively for Multinomial Thompson Sampling and Non Parametric Thompson Sampling. However, replacing the linear expectation by the CVaR that is non-linear, causes several technical challenges that make the adaptation non-trivial. This is particularly true for the boundary crossing probabilities for Dirichlet random variables, that we define and analyze in this section. Our results aim at replacing the Lemma 13, 14, 15 and 17 of Riou and Honda in the proofs of Theorem 2. ‣ 3.2 Regret Guarantees for M-CVTS and B-CVTS ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") and Theorem 3. ‣ 3.2 Regret Guarantees for M-CVTS and B-CVTS ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits").

<!-- chunk {"id": "body-0023", "role": "body", "section": "Boundary crossing probabilities", "weight": 1.0} -->

In this paragraph we highlight the construction of boundary crossing probabilities for Dirichlet random variables, which consists in providing upper and lower bounds of some terms of the form for some known support $\mathcal{X} = {(x_{1},\ldots,x_{n})}$, parameter $\beta \in {\mathbb{R}}_{+}^{n}$ of the Dirichlet distribution, and some real value $c$ that will be defined in context. We introduce the set following the notations of Section 2 for $C_{\alpha}{(\mathcal{X},p)}$. Thanks to the expression of the CVaR in Equation we have where we defined for all $m \in {\{ 1,\ldots,n\}}$ the sets This set is closed and convex, hence $\mathcal{S}_{\mathcal{X}}^{\alpha}{(c)}$ is closed, and is the finite union of convex sets (but is not convex). These properties are crucial to prove the results of this section.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Bounded support size", "weight": 1.0} -->

We first study the case when the size of the support is ${|\mathcal{X}|} = M$, for some known $M \in {\mathbb{N}}$ and when the considered distributions are the frequency of each observation in $\mathcal{X}$ out of $n \in {\mathbb{N}}$ many observations, which we represent by the set We then express bounds for boundary crossing probabilities on this set, in terms of $n$ and $M$, where $n$ should be considered much larger than $M$. Lemma 1. ‣ Bounded support size ‣ 3.3 Technical challenges and tools ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") and 2. ‣ Bounded support size ‣ 3.3 Technical challenges and tools ‣ 3 Regret Analysis ‣ Optimal Thompson Sampling strategies for support-aware CVaR bandits") respectively provide an upper and lower bound on such probabilities.

<!-- chunk {"id": "body-0025", "role": "body", "section": "General support size", "weight": 1.0} -->

We now detail some results that are specifically designed for the regret analysis of B-CVTS. For this reason, we consider a support $\mathcal{X} = {(x_{1},\ldots,x_{n})}$ and the Dirichlet distribution $\mathcal{D}_{n}$ defined in Section 2. Here we focus on the Dirichlet sample, hence the support $\mathcal{X}$ is known. We further denote $u_{\mathcal{X}}$ the uniform distribution on $\mathcal{X}$, and $C_{\alpha}{(\mathcal{X})}$ its CVaR. We first establish an upper bound.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The results presented in this section contains most of the difficulty induced by the replacement of the expectation by the CVaR in the proofs. Extending these results to other criterion is an interesting future work and may help generalize the Non Parametric Thompson Sampling algorithms to broader settings.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we report the results of experiments on the algorithms presented in the previous sections, first on synthetic examples, and then on a use-case study in agriculture based on the DSSAT agriculture simulator.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Preliminary Experiments", "weight": 1.0} -->

We first performed various experiments on synthetic data in order to check the good practical performance of M-CVTS and B-CVTS on settings that are simple to implement and are good illustrative examples of the performance of the algorithms. Due to space limitation, we report a complete description of the experiments and and an analysis of the results in Appendix G. We tested the TS algorithms on specified difficult instances and on randomly generated problems, against U-UCB and CVaR-UCB.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Preliminary Experiments", "weight": 1.0} -->

As an example of experiment with multinomial arms, we report in Table 1 the results of an experiment with $10^{3}$ randomly generated problems with $5$ arms drawn uniformly at random in $\mathcal{P}^{|\mathcal{X}|}$, where $\mathcal{X} = {\lbrack 0,0.1,0.2,\ldots,1\rbrack}$, for $\alpha \in {\{{10\%},{50\%},{90\%}\}}$ and an horizon $10^{4}$. These experiments confirm the benefits of TS over UCB approaches, as M-CVTS significantly outperforms its competitors for all levels of the parameter $\alpha$. We also tested the algorithms with fixed instances (see Tables 8-8), with the same results, and further illustrated the asymptotic optimality of M-CVTS in Figures 7 and 8 by representing the lower bound presented in Section 3 along with the regret of the algorithm in logarithmic scale.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Preliminary Experiments", "weight": 1.0} -->

We also tested B-CVTS on different problems, using truncated gaussian mixtures (TGM). The results are presented in Tables 9-12, and again show the merits of the TS approach. We also performed an experiment with a small level $\alpha = {1\%}$ (Table 13) and show that B-CVTS keeps the same level of performance in this case, while the other algorithm stay in the linear regime for the horizon we consider. Finally, we also experimented more arms ($K = 30$) and randomly generated TGM problems and report the results in Table 2. The means and variance of each arm satisfy ${(\mu_{k},\sigma_{k})} \sim {\mathcal{U}{({{{{\lbrack 0.25,1\rbrack}^{1}0} \times {\lbrack 0,0.1\rbrack}^{1}}0})}}$, and the probabilities of each mode are drawn uniformly, $p_{k} \sim \mathcal{D}_{19}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Preliminary Experiments", "weight": 1.0} -->

These very good results with synthetic data and its theoretical guarantees motivate using the B-CVTS algorithm in the real-world application we introduce in the next section.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Motivation", "weight": 1.0} -->

Let us consider a farmer who must decide on a planting date (action) for a rainfed crop. Farmers have been reported to primarily seek advice that reduces uncertainty in highly uncertain decision making. Planting date is an example of such a decision as it will influence the probabilities of favorable meteorologic events during crop cultivation. These events are highly uncertain due to the length of crop growing cycles (e.g. 3 to 6 months for grain maize). For instance, because of the stochastic nature of the rainfalls and temperatures, a farmer will observe a range of different crop yields from year to year for the same planting date, all other technical choices being equal. Thus, assuming that the environment is stationary, each planting date corresponds to an underlying, unknown yield distribution, which can be modeled as an arm in a bandit problem. Depending on her profile, a farmer may be more or less risk averse, and the Conditional Value at Risk can be used to personalize her level of risk-aversion.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Motivation", "weight": 1.0} -->

For instance, a small-holder farmer looking for food security may seek to avoid very poor yields compromising auto-consumption (e.g $\alpha \leq {20\%}$), while a market-oriented farmer may be more prone to risky choices in order to increase her profit but still not risk neutral (e.g $\alpha = {80\%}$). Yield distributions are supposed to be bounded. Indeed, a finite yield potential can be defined under non-stressing conditions for a given crop and environment. Observed yields can be modeled as following Von Liebig's law of minimum: limiting factors will determine how much of the yield potential can be expressed.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Setting", "weight": 1.0} -->

Planting date decision-making support requires extensive testing prior to any real-life application, due the potential impact of wrong action-making, particularly in subsistence farming. For this reason, we consider the problem of facing many times the decision of a planting date in the DSSAT^33^3DSSAT is an Open-Source project maintained by the DSSAT Foundation, see simulator, to make an in silico decision. DSSAT, standing for *Decision Support System for Agrotechnology Transfer*, is a world-wide crop simulator, supporting 42 different crops, with more than 30 years of development. We specifically address maize planting date decision, as maize is a crucial crop for global food security. Each simulation is assumed to be realistic, and starts from the same field initial conditions as ground measured. The simulator takes as input historical weather data, field soil measures, crop specific genetic parameters and a given crop management plan. Modeling is based on simulations of atmospheric, soil and plants compartments and their interactions. In the considered experiments, after a decision is made on planting date in the simulator, daily stochastic meteorologic features are generated according to historical data and injected in the complex crop model.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Setting", "weight": 1.0} -->

At the end of crop cycle, a maize grain yield is measured to evaluate decision-making. We parameterized the crop-model under challenging rainfed conditions on shallow sandy soils, i.e. with poor water retention and fertility. Such experiment intends to be representative of realistic conditions faced by small-holder farmers under heavy environmental constraints, such as in Sub-Saharan Africa. Thus, this setting can help picturing how CVaR bandits may perform in real-world conditions. For the sake of the experiments, we built a bandit-oriented Python wrapper to DSSAT that we made available^44^4 to the bandit community for reproducibility.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We test bandit performances on the 4 armed DSSAT environment described in Table 3. To illustrate the non-parametric nature of these distributions, we report in Figure 1 estimations of their density obtained with Monte-Carlo simulations, as well as of their CVaRs. The resulting distributions are typically *multi-modal*, with one of their mode very close to zero (years of bad harvest), and with upper tails that cannot be properly characterized. However the practitioner can realistically assume that the distributions are upper-bounded, due to the physical constraints of crop-farming. The yield upper-bound is set to 10 t/ha thanks to expert knowledge for the considered conditions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Further experiments are reported in Appendix G. In particular we increase the number of arms, and empirically study the effect of over-estimating the support upper-bound: our results show that a \"prudent\" bound has little effect of the performance of the algorithms in the settings we consider. This property is of particular interest for the practitioner, as a proper tuning of the support upper bound is the main limitation of the use of B-CVTS (and all bandit algorithms available for this problem). In most applications grounded on physical reality, the availability of such prudent upper-bound estimate is likely, and sufficient to ensure the practical performance of the B-CVTS algorithm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Perspectives", "weight": 1.0} -->

This first set of experiments using a challenging realistic crop simulator is promising, and motivates to further investigate the use of B-CVTS algorithm for crop-management support and other problems that can be modeled as CVaR bandits. B-CVTS enjoys appealing theoretical guarantees, and thanks to its simplicity and competitive empirical performances may be a good candidate for practitioners. In order to address real-world crop-management challenges, many questions remain to be considered, e.g. how to optimally generate mini-batches of recommendations to an ensemble of farmers in a semi-sequential procedure (in order to account for the long feedback time), how to incorporate distribution priors on crop-management options that could be pre-learnt in silico and refining them adaptively in the real world (thus, minimizing random exploration in the real world), how to include contextual information such as soil characteristics and local weather forecasts, or how handle non-stationarity, incorporating climate change progressive impact on an optimal planting date.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Perspectives", "weight": 1.0} -->

Furthermore, the simplicity of the Non-Parametric Thompson Sampling algorithms make them appealing for generalization to other risk-aware settings, e.g risk-constrained (maximizing the mean under a condition on the CVaR) or with other risk metrics (mean-variance, entropic risk, etc). All of these open questions make interesting challenges for future works.
