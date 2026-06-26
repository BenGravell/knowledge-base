<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Cantor-Kantorovich Metric between Markov Decision Processes with Application to Transfer Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We extend the notion of Cantor-Kantorovich distance between Markov chains introduced by in the context of Markov Decision Processes (MDPs). The proposed metric is well-defined and can be efficiently approximated given a finite horizon. Then, we provide numerical evidences that the latter metric can lead to interesting applications in the field of reinforcement learning. In particular, we show that it could be used for forecasting the performance of transfer learning algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Research on quantitative notion of behavioural distance between Markov processes by the reinforcement learning community (see and the references therein) mimics the study of distance between dynamical systems conducted by the control community (see, and the references therein). Both communities are interested in computing *how much processes/dynamical systems differ in terms of their behaviour*. Several metrics have been proposed for Markov Chains (MC) (see ), including the recent Cantor-Kantorovich metric by Banse et al. where they applied it for abstraction-based methods. Few metrics like the one in are equipped with the availability of algorithms for fast computation making them deployment-ready.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is typical to train a reinforcement learning algorithm in a simpler world modeled as a Markov Decision Process (MDP) and deploy it in a real world setting corresponding to a different MDP. Several Transfer Learning (TL) algorithms have been developed in this paradigm where one transfers a learned policy from one MDP to another in the hope of improving the performance of the latter (see Lazaric et al., Wang et al., Tao et al., Bou Ammar et al. ). Many works have shown numerical evidences that TL algorithms have better performances when the source and target MDPs are similar to each other (see Song et al., Carroll and Seppi, Zhu et al. and the references therein). This triggered the research community to undertake similar efforts as that of MC for studying the similarity between the MDPs. Interestingly Carroll and Seppi argued that no single task similarity measure is uniformly superior for TL problems. Despite their observation, it would be beneficial to design a metric between MDPs which does not have computational complexity issues so that it can be used to improve the performance of TL problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This manuscript extends the range of application of the Cantor-Kantorovich metric proposed by Banse et al. in the context of TL. Specifically, the main contributions are: The Cantor-Kantorovich metric is formulated in the context of MDPs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The promising potential of the proposed metric is demonstrated on a transfer learning problem where sources having smaller Cantor-Kantorovich distance with the target are shown to guarantee performance using TL techniques.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outline: Following a short summary of notations and preliminaries, we present the proposed metric between MDPs in Section 2. Subsequently, the application to problems in Transfer Learning domain is demonstrated in Section 3. Finally, the paper is summarised in Section 4 along with the discussion of potential future research directions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations The set of real and natural numbers are denoted by $\mathbb{R}$ and $\mathbb{N}$ respectively. For $N \in {\mathbb{N}}$, we denote by ${\lbrack N\rbrack}:={\{ 0,1,\ldots,N\}}$. The cardinality of the set $C$ is denoted by $|C|$. The notation $f:{X\rightarrow Y}$ denotes that $f$ is a mapping from domain $X$ to range $Y$. Given a set $S \subseteq {\mathbb{R}}^{n}$, the Borel set associated with it is denoted by $\mathcal{B}{(S)}$. For a random variable $x$, its expected value is given by the notation ${\mathbb{E}}{\lbrack x\rbrack}$. Let $(\Omega,D)$ be a discrete and finite metric space equipped with metric $D$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given two probability distributions ${\mathbb{P}}:{\Omega\rightarrow{\lbrack 0,1\rbrack}}$ and ${\mathbb{Q}}:{\Omega\rightarrow{\lbrack 0,1\rbrack}}$, the Kantorovich distance between them is defined as where $\Pi{({\mathbb{P}},{\mathbb{Q}})}$ denotes the set of all joint probability distributions on $\Omega \times \Omega$ with $\mathbb{P}$ and $\mathbb{Q}$ being the marginals.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Cantor-Kantorovich metric in the context of MDPs", "weight": 1.0} -->

In this section, we recall the notions introduced in and we show how to use them in the context of MDPs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "A metric between dynamics of two MDPs", "weight": 1.0} -->

We now recall the main recent results in in the context of MDPs. Consider two MDPs $M_{1} = {(\mathcal{S}_{1},\mathcal{U}_{1},\mathcal{T}_{1},R_{1},\mu_{1})}$ and $M_{2} = {(\mathcal{S}_{2},\mathcal{U}_{2},\mathcal{T}_{2},R_{2},\mu_{2})}$. We assume that both MDPs are homogeneous (see Definition 3.2 in ), meaning that there exist one-to-one correspondence between their state-spaces $(\mathcal{S}_{1},\mathcal{S}_{2})$, and also between their control spaces $(\mathcal{U}_{1},\mathcal{U}_{2})$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "A metric between dynamics of two MDPs", "weight": 1.0} -->

However, for the ease of exposition, we will proceed ahead with a simpler setting where $\mathcal{S}_{1} = \mathcal{S}_{2} = \mathcal{S}$ and $\mathcal{U}_{1} = \mathcal{U}_{2} = \mathcal{U}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "A metric between dynamics of two MDPs", "weight": 1.0} -->

We are interested in the asymptotic difference between the dynamics of both MDPs under two policies $p$ and $q$. Given a horizon length $N$, consider the metric space $(\mathcal{S}^{N},C)$, equipped with the Cantor metric $C$. Given two trajectory sequences ${\mathbf{a}^{N},\mathbf{b}^{N}} \in \mathcal{S}^{N}$, the Cantor metric between $\mathbf{a}^{N}$ and $\mathbf{b}^{N}$ is defined as Given a horizon $N$ and two policies $p$ and $q$, let ${\mathbb{P}}_{p}^{N}$ and ${\mathbb{Q}}_{q}^{N}$ be the two probability distributions respectively induced by MDPs $M_{1}$ and $M_{2}$ at time $N$ according to.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Application to Transfer Learning", "weight": 1.0} -->

In this section, we showcase the possible application of our Cantor-Kantorovich distance to transfer learning with a numerical experiment. We consider a grid-world target MDP which is illustrated in Figure 1. The size of the grid-world is $10 \times 10$; the possible control actions are $\mathcal{U} = {\{\text{left},\text{right},\text{up},\text{down}\}}$; the goal is in position $$, and corresponds to a reward of 10; when choosing a direction $u$, the probability to go in that direction is $\delta = {1/2}$, and the other probabilities are ${{({1 - \delta})}/3} = {1/6}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Application to Transfer Learning", "weight": 1.0} -->

The transfer learning experiment goes as follows. We generate 100 other grid-worlds $M_{S,i}$, where the only difference with the target is the probability $\delta$, uniformly sampled between 0 and 1. For each source MDP $M_{S,i}$: We compute an optimal policy $p_{S,i}^{\ast}$ with Q-learning and we save the optimal Q-table $Q_{S,i}^{\ast}$. Specifically, we used an $\varepsilon$-greedy exploration strategy with $\varepsilon = 0.5$, and we learned the optimal policy with 4000 episodes of length 100, and with a learning rate of 0.01. We approximated the rewards with 10000 samples, and the discount factor is $\gamma = 0.95$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Application to Transfer Learning", "weight": 1.0} -->

We compute the Cantor-Kantorovich distance with the target, that is $\mathbf{d}{(M_{T},M_{S,i})}$ using $N = 8$. We fix the policies $p$ and $q$ as We solve the target with Q-learning by initializing Q-values with $Q_{S,i}^{\ast}$, and we compute the jump-start reward (which describes the increase in the initial performance achievable in the target using the transferred knowledge, before any further learning), that is the difference of reward at the start of the learning process with and without transfer learning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Application to Transfer Learning", "weight": 1.0} -->

The results of this experiment can be found in Figure 2 and they can be reproduced with the code provided in Figure 2: Results of the transfer learning experiment. The x-axis is the Cantor-Kantorovich distance between the target and the sources. The y-axis is the jumpstart metric, i.e. the metric used to asses the performance of the transfer. Green and red dots correspond to sources with δ < 1/2, and δ ≥ 1/2 respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Application to Transfer Learning", "weight": 1.0} -->

First we can observe that, in the red case (i.e. when the source has a greater chance to take the right direction than the target), the TL technique used here always improves performance as the jumpstart reward is always larger than 1. This is due to the fact that the policy found by the source is always optimal for the target as well. In the second case though, the green dots show that there is a strong correlation between the Cantor-Kantorovich distance and the performance of the transfer.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Application to Transfer Learning", "weight": 1.0} -->

This experiment therefore provides a numerical evidence that sources with a non-optimal policy but with a small Cantor-Kantorovich distance with the target guarantee performance using transfer learning. Although the example discussed here is simple, it is rich enough to demonstrate the effectiveness of our proposed metric. We leave the option of exploring a more involved numerical example with different reward setting, studying other TL algorithms and other nuances to the future study.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

In this work, a novel Cantor-Kantorovich metric with reasonable computational complexity was introduced in the context of MDPs. Its applicability to problems in the TL domain was also demonstrated using a simple numerical simulation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

There are several promising and potential research directions for the future. For instance, one could aim for improving the upper bound for accuracy of the proposed Cantor-Kantorovich metric with a finite horizon $N$. Similarly, one could investigate a distance of the form where $\mathbf{d}_{r}$ is a distance between the rewards of $M_{1}$ and $M_{2}$. The choice of $\mathbf{d}_{r},\alpha$ and $\beta$ would therefore depend on the application context. For example, one could investigate the distances described. In the same fashion as Carroll and Seppi, one could apply such distances to the same grid-world example as above, but where the goal is moving. Finally, it would be interesting to investigate other performance measures than the jumpstart reward to evaluate the performance of the proposed metric in the transfer learning setting.
