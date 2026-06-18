<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

When Is Partially Observable Reinforcement Learning Not Scary?

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Applications of Reinforcement Learning (RL), in which agents learn to make a sequence of decisions despite lacking complete information about the latent states of the controlled system, that is, they act under partial observability of the states, are ubiquitous. Partially observable RL can be notoriously difficult - well-known information-theoretic results show that learning partially observable Markov decision processes (POMDPs) requires an exponential number of samples in the worst case. Yet, this does not rule out the existence of large subclasses of POMDPs over which learning is tractable. In this paper we identify such a subclass, which we call weakly revealing POMDPs. This family rules out the pathological instances of POMDPs where observations are uninformative to a degree that makes learning hard. We prove that for weakly revealing POMDPs, a simple algorithm combining optimism and Maximum Likelihood Estimation (MLE) is sufficient to guarantee polynomial sample complexity. To the best of our knowledge, this is the first provably sample-efficient result for learning from interactions in overcomplete POMDPs, where the number of latent states can be larger than the number of observations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A wide range of modern artificial intelligence challenges can be cast as Reinforcement Learning (RL) problems under *partial observability*, in which agents learn to make a sequence of decisions despite lacking complete information about the underlying state of system. For example, in robotics the agent has to cope with noisy sensors, occlusions, and unknown dynamics, while in imperfect information games the player makes only local observations. Further applications of partially observable RL include autonomous driving, resource allocation, medical diagnostic systems, recommendation, business management, etc. As such, learning and acting under partial observability has been an important topic in operation research, control, and machine learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because of the non-Markovian nature of the observations, learning and planning in partially observable environments requires an agent to maintain *memory* and possibly reason about *beliefs* over the states, all while exploring to collect information about the environment. As such, partial observability can significantly complicate learning and planning under uncertainty. While practical RL systems have succeeded in a set of partially observable problems including Poker, Starcraft and certain robotic tasks, the theoretical understanding of learning to act in partially observable systems remains limited. Most existing results in RL theory focus on fully observable systems or, more generally, learning when the features of states are accessible and can faithfully represent value functions. As such, algorithms developed for this case need not to reason about what the latent state may be and in particular do not need to resort to using the observation histories. Thus, the resulting algorithms can be fundamentally limited and may not work beyond the narrow settings that they are designed. Owning to the ubiquity of partially observable problems, addressing the theoretical challenges of partial observability is vital to closing the gap between the typical applications and the scope of available theoretical works.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper considers Partially Observable Markov Decision Process (POMDPs)---the standard model in reinforcement learning that captures the partial-information structure. Despite the existence of many efficient algorithms for learning MDPs in the fully observable settings, learning POMDPs is notoriously difficult in theory---well-known complexity-theoretic results show that learning and planning in partially observable environments is indeed statistically and computationally *intractable* in general, even if in the favorable setting with a small number of states, actions, and observations. However, these complexity barriers are of a worst case nature, and they do not preclude efficient algorithms for learning rich sub-classes of POMDPs which could potentially cover interesting practical applications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Can we identify a rich sub-class of POMDPs that empowers sample-efficient RL?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior efforts on sample-efficient learning of POMDPs focus either on special cases of POMDPs such as latent MDPs, or on general POMDPs but with restrictive assumptions. In particular, Azizzadenesheli et al.; Guo et al. do not address strategic exploration---a core challenge in RL; Jin et al. considers the exploration setting but only addresses undercomplete POMDPs, where the number of states must be no larger than the number of observations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper answers the highlighted question above affirmatively. We identify a rich family of tractable POMDPs---*weakly revealing* POMDPs (see Section 3), which rule out the pathological instances whose observations contain no information to distinguish latent states. *Weakly revealing* POMDPs are very rich---it contains a majority of existing POMDPs classes which are known to be tractable; it also handles overcomplete POMDPs where the number of latent states can be larger than the number of observations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further propose a new simple algorithm for learning POMDPs---*Optimistic Maximum Likelihood Estimation* (OMLE). As its name suggests, OMLE (read, Oh-Em-El-Eeh) combines optimism with classical maximum likelihood estimation. In contrast to the algorithm of Jin et al. which heavily exploit the undercomplete structure, our algorithm is generic, does not explicitly rely on any special structure, and can be used for any POMDPs. We prove that OMLE learns a near-optimal policy for any weakly revealing POMDP within a polynomial number of samples (Theorem 4. ‣ Theoretical guarantees ‣ 4.1 Undercomplete setting ‣ 4 Main Results ‣ When Is Partially Observable Reinforcement Learning Not Scary?") and 7. ‣ Theoretical guarantees ‣ 4.2 Overcomplete setting ‣ 4 Main Results ‣ When Is Partially Observable Reinforcement Learning Not Scary?")). To the best of our knowledge, this is the first provably sample-efficient result for learning overcomplete POMDPs in settings where exploration is necessary. Our result also reasserts that optimism is a powerful tool to address exploration needs, regardless of whether states are observable.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We complement our positive results with lower bounds showing that certain polynomial dependency on the problem parameters in our sample complexity is necessary.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we remark that our algorithm, as well as all existing algorithms for learning large classes of POMDPs, remains *computationally* inefficient. This is due to the inherent computational hardness of learning POMDPs: planning (i.e., computing the optimal policy *given* model parameters) alone is already PSPACE-complete, not mentioning the additional computation required for model estimation and exploration. We leave the challenge of computationally efficient learning for future work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overview of techniques", "weight": 1.0} -->

The major technical challenge of this paper is to establish the sample efficiency guarantee of OMLE for learning any weakly revealing POMDPs despite the simplicity of the algorithm. Our results rely on the following three key ideas. To the best of our knowledge, the second and the third ideas are novel in the context of learning POMDPs, while the first technique was used by Jin et al..

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview of techniques", "weight": 1.0} -->

Observable Operator Model (OOM): OOM provides an alternative parameterization of the POMDP model, by representing the probability of a trajectory over observations and actions as the product of a series of linear operators, which is known as *observable operators*. For more details, see Section 5.1. Such linear structure facilitates us to use existing tools from matrix analysis to analyze POMDPs. Although OMLE algorithm does not explicitly utilize the OOM representation, the observable operators serve as important intermediate quantities in our analysis. They help us to bound the suboptimality of the learned policy as a function of the size of our confidence set.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview of techniques", "weight": 1.0} -->

MLE-based Confidence Set: In contrast to the current mainstream approaches of learning POMDPs which use *spectral methods* to directly estimate either the model parameters or the observable operators, we use the *maximum likelihood estimation* (MLE) approach, which provides implicit guarantees on learning observable operators. We achieve this by adapting the classic techniques for analyzing MLE. An appealing feature of the MLE approach is its generality and that the confidence set construction does not need to rely on the specific structure of the problem. The strength of this unified approach is that it allows OMLE to be used with almost no changes in both undercomplete and overcomplete POMDPs. In constrast, spectral-based algorithms require more careful designs that are adjusted to specific problems (such as undercomplete vs. overcomplete settings). These adjustments, if not done optimally, easily lead to requirement of unnecessary, artificial assumptions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview of techniques", "weight": 1.0} -->

$\ell_{1}$-norm eluder Dimension: To prove the sample efficiency of optimistic algorithms, one needs to argue that, after a sufficient number of iterations, the size of the maintained confidence set is small enough to guarantee near-optimality of the learned policy. In the tabular setting, this is typically achieved by resorting to the pigeon-hole principle, while in the linear setting, one typically uses the so-called elliptical potential lemma. To generalize these argument, Russo and Van Roy introduced the notion of eluder dimension for sets of real-valued functions with a common domain. The use of MLE-based confidence set requires us to develop a new result which is stronger than the standard elliptical potential arguments: While we have linear structures, the $\ell_{2}$-norms typically used are not suitable for our purposes. As such, the standard eluder dimension (which is tied to the $\ell_{2}$-norm) is also unsuitable. To address these challenges, we introduce a variation of the eluder dimension, which is called $\ell_{1}$-norm eluder dimension, and which might be of independent interest.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related works", "weight": 1.0} -->

Reinforcement learning has been extensively studied in the fully observable setting. For the purpose of this paper, we focus our attention on reviewing the theoretical results for partially observable reinforcement learning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Hardness of learning POMDPs", "weight": 1.0} -->

There is a line of well-known computational hardness results for planning and learning in POMDPs. Firstly, even when the parameters of a POMDP are known, computing the optimal policy (i.e., planning) is PSPACE-complete. Moreover, even if one only wants to find the optimal memoryless policy, the problem is still NP-hard. In addition, the model estimation of POMDPs is also computationally hard---Mossel and Roch proved an average-case computational result showing that estimating the model parameters for a subclass of Hidden Markov Models (HMMs) is at least as hard as learning parity with noise^22^2Learning parity with noise is conjectured to be NP-hard in the theory of computational complexity.. Since HMMs can be viewed as special cases of POMDPs without action control, their result directly implies estimating the model parameters of POMDPs is hard.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Hardness of learning POMDPs", "weight": 1.0} -->

Learning POMDPs is also known to be statistically hard: Krishnamurthy et al. proved that finding a near-optimal policy of a POMDP in the worst case requires a number of samples that is exponential in the episode length. The hard instances are those pathological POMDPs where the observations contain no useful information for identifying the system dynamics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Positive results for learning POMDPs", "weight": 1.0} -->

Despite the worst-case hardness results, there is a long history of learning sub-classes of POMDPs. Even-Dar et al. studied POMDPs without resets, where the proposed algorithm has sample complexity scaling exponentially with a certain horizon time. Poupart and Vlassis; Ross et al. developed Bayesian methods to learn POMDPs, while Azizzadenesheli et al. considered learning the optimal memoryless policies with policy gradient methods. PAC or regret bounds are not known for these approaches.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Positive results for learning POMDPs", "weight": 1.0} -->

In the category of polynomial sample results, a sequence of recent works applied spectral methods to learning POMDPs and obtained polynomial sample complexity results. Among them, Guo et al.; Azizzadenesheli et al.; Xiong et al. made strong reachability assumptions and did not address the exploration problem. Furthermore, these results assume that both the transition and emission matrices are full rank, which are stronger than the weakly revealing conditions considered in this paper. Jafarnia-Jahromi et al. proposed a posterior sampling-based algorithm, and provided sample-efficient guarantees *assuming* either sufficient separability between different models, or the success of belief state and transition kernel estimation. These assumptions significantly reduce the difficulty of estimating model dynamics---a core challenge in learning POMDPs, and thus reduce the generality of the results.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Positive results for learning POMDPs", "weight": 1.0} -->

The most related work to us is Jin et al., which addressed the exploration problem in learning undercomplete POMDPs, where the number of latent states must be no greater than the number of observations. Their algorithm is specially designed to exploit the undercomplete structure of POMDPs. It remains unclear if their techniques can be extended to the overcomplete setting. In contrast, this paper presents a new generic algorithm based on MLE, which enjoys provable sample-efficiency in the exploration settings of both undercomplete and overcomplete POMDPs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Positive results for learning POMDPs", "weight": 1.0} -->

Very recently, Golowich et al. developed the first quasi-polynomial time planning algorithm for a subclass of POMDPs. Their result holds under the $\gamma$-observability condition, which is very similar to the weakly-revealing condition presented in this paper.^33^3$\gamma$-observability condition requires that ${\min_{h}{\|{{\mathbb{O}}_{h}{({b - b^{\prime}})}}\|}_{1}} \geq {\gamma{\|{b - b^{\prime}}\|}_{1}}$ for any ${b,b} \in \Delta_{S}$, while $\alpha$-weakly-revealing condition (Assumption 1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Positive results for learning POMDPs", "weight": 1.0} -->

‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?")) assumes ${\min_{h}{\|{{\mathbb{O}}_{h}x}\|}_{2}} \geq {\alpha{\| x\|}_{2}}$ for any $x \in {\mathbb{R}}^{O}$. In Lemma 35 and the weakly revealing conditions ‣ Appendix H Proofs for Weakly Revealing Conditions ‣ When Is Partially Observable Reinforcement Learning Not Scary?"), we prove that $\frac{\alpha}{\sqrt{S}} \leq \gamma \leq {4\sqrt{O}\alpha}$. As a result, these two conditions are "equivalent" up to a factor of at most $\mathcal{O}{(\sqrt{O})}$. Compared to this paper, the result in Golowich et al. purely focuses on the computational efficiency.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Positive results for learning POMDPs", "weight": 1.0} -->

It is restricted to the undercomplete setting, and addresses only planning but not estimation or exploration, all of which are important components for learning POMDPs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Latent MDPs", "weight": 1.0} -->

Latent MDPs ---where an MDP is randomly drawn from a set of $M$ possible MDPs at the beginning of the interaction---can be considered as a special class of overcomplete POMDPs. Kwon et al. proved that learning latent MDPs remains statistically hard in the worst case. They also provided several positive results for learning latent MDPs with additional assumptions, such as revealing the latent contexts at the end of each episode. Kwon et al. provided positive results for latent MDPs without these additional assumptions, but the results only apply to the setting of $M = 2$ with a shared transition. Latent MDPs and weakly revealing POMDPs do not contain each other.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Decodable POMDPs", "weight": 1.0} -->

Block MDPs are POMDPs whose current latent state can be uniquely determined by the current observation. By simple algebra, one can verify that block MPDs are special cases of single-step weakly revealing POMDPs that satisfy Assumption 1. ‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") with $\alpha \geq {1/\sqrt{O}}$. The recently proposed $m$-step decodable POMDPs are generalizations of block MDPs, in which the latent state can be uniquely decoded from the most recent history (of observations and actions) of a short length $m$. This multistep decodability assumption can also be viewed as a special case of general "weakly revealing"-type of conditions. However, Efroni et al. assume that $m$-step history decodes (weakly reveals) the current state, while this paper assumes that $m$-step future weakly reveals the current state.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Decodable POMDPs", "weight": 1.0} -->

Finally, we remark that most existing results for block MDPs or $m$-step decodable POMDPs further involve decoder class or value function approximation, which is beyond the scope of this paper.

<!-- chunk {"id": "body-0028", "role": "body", "section": "RL with function approximation", "weight": 1.0} -->

There is a recent line of research on reinforcement learning with general function approximation. This line of results proposed certain complexity measure for sequential decision making problems, and developed generic algorithms which have sample-efficient guarantees as long as the complexity measure of RL problems is small. These frameworks are known to cover a special subclass of POMDPs---reactive POMDPs, where the optimal value only depends on the current-step observation-action pair. It remains highly unclear whether weakly revealing POMDPs identified in this paper can be covered by those general frameworks. We remark that investigating this problem requires us to compute those complexity measures for POMDPs, which is highly non-trivial and may require techniques developed in this paper.

<!-- chunk {"id": "body-0029", "role": "body", "section": "MLE approaches in bandit and RL", "weight": 1.0} -->

The idea of using the MLE principle in the confidence set construction can be traced back to Lai, which considers the problem of Bernoulli bandits. MLE-based approaches are also used in the framework of reward-biased MLE, which balances the reward with the likelihood value, for learning tabular MDPs. Recently, the MLE-based approaches are also used in the setting of representation learning in RL.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning objective", "weight": 1.0} -->

Our goal is to learn an $\varepsilon$-optimal policy $\pi$ in the sense that $V^{\pi} \geq {V^{\star} - \varepsilon}$, using a number of samples polynomial in all relevant parameters. We also consider the problem of learning with low regret. Suppose the agent interacts with POMDPs for $K$ episodes, and plays a policy $\pi_{k}$ in the $k^{\text{th}}$ iteration for any $k \in {\lbrack K\rbrack}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning objective", "weight": 1.0} -->

The question then is whether a learner can keep the regret small.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Weakly Revealing POMDPs", "weight": 1.0} -->

The purpose of this section is to define the class of weakly revealing POMDPs. We first motivate our definition by revisiting the pathological instances which prevent sample-efficient learning of POMDPs in general. We then introduce the formal definition of weakly revealing POMDPs in the *undercomplete* setting when $S \leq O$ and finally extend it to the *overcomplete* setting when $S > O$. All the proofs for this section are deferred to Appendix H.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Hard instances of POMDPs", "weight": 1.0} -->

Here we revisit the hardness results and the pathological instances constructed by Krishnamurthy et al. and Jin et al.. As it turns out, learning POMDPs is statistically hard in the worst-case due to the existence of POMDPs with uninformative observations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Weakly revealing condition in the undercomplete setting", "weight": 1.0} -->

Based on the hard instances constructed above, we conclude that if the observations do not contain information to distinguish two different latent states, then learning these POMDPs is statistically hard. For POMDPs with more than two states, the hardness result above can be easily extended to the case where there exist two mixtures of latent states with disjoint support such that the observations do not contain any information to distinguish these two mixtures. Concretely, by a mild abuse of language, a mixture of states is identified by a probability vector $\nu \in \Delta_{S}$; $\nu_{1}$ and $\nu_{2}$ are said to have disjoint support if ${{\text{supp}{(\nu_{1})}} \cap {\text{supp}{(\nu_{2})}}} = \varnothing$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Weakly revealing condition in the undercomplete setting", "weight": 1.0} -->

A direct approach to rule out the above-described pathological instances is to just assume that any two latent state mixtures $\nu_{1},\nu_{2}$ that have disjoint support induce distinct distributions over observations, that is, ${{\mathbb{O}}_{h}\nu_{1}} \neq {{\mathbb{O}}_{h}\nu_{2}}$ for all $h \in {\lbrack H\rbrack}$ where ${\mathbb{O}}_{h}$ is the $O \times S$ emission matrix at step $h$. A linear algebraic argument then shows that this condition is equivalent to that the rank of the emission matrix ${\mathbb{O}}_{h}$ is $S$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 1 ($\\alpha$-weakly revealing condition)", "weight": 1.0} -->

This condition ensures that the observations contain enough information to distinguish any two mixtures of states given a sufficiently large number of samples.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 1 ($\\alpha$-weakly revealing condition)", "weight": 1.0} -->

We call Assumption 1. ‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") the "*weakly*" revealing condition to distinguish it from the setup known as rich observation or block MDP in the literature. The latter setup considers the problem where the latent state can be directly recovered from any single observation and the stage $h$ in the episode. That is, the latent state is completely revealed by the observation. Therefore, technically speaking, block MDPs are fully observable, which is in a way "diagonally opposite" to the setting we consider.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 1 ($\\alpha$-weakly revealing condition)", "weight": 1.0} -->

Finally, we note that since ${\mathbb{O}}_{h}$ is a matrix of size $O \times S$, Assumption 1. ‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") implicitly requires $S \leq O$. That is, it only holds in the undercomplete setting.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Weakly revealing condition in the overcomplete setting", "weight": 1.0} -->

In the overcomplete setting, we have $S > O$. It is information-theoretically impossible to distinguish any two mixtures of latent states by inspecting observations only in a single step. The key observation here is that we should instead inspect the distribution of observations for *$m$ consecutive steps*. We note that the number of all possible observable sequence $(o_{1},a_{1},\ldots,a_{m - 1},o_{m})$ of length $m$ is $O^{m}A^{m - 1}$, which is larger than $S$ when $m \geq {\Omega{({\log S})}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Weakly revealing condition in the overcomplete setting", "weight": 1.0} -->

To state our assumption, we define the $m$-step emission-action matrices

<!-- chunk {"id": "body-0041", "role": "body", "section": "Weakly revealing condition in the overcomplete setting", "weight": 1.0} -->

Similar to the undercomplete case, the weakly revealing condition in the overcomplete setting assumes that the $S^{\text{th}}$ singular value of the $m$-step emission matrix ${\mathbb{M}}_{h}$ is lower bounded.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 2 ($m$-step $\\alpha$-weakly revealing condition)", "weight": 1.0} -->

Assumption 2. ‣ 3.3 Weakly revealing condition in the overcomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") ensures that the observable sequence in the next $m$ consecutive steps contain enough information to distinguish any two mixtures of states given a sufficiently large number of observations. Assumption 1. ‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") is a special case of Assumption 2. ‣ 3.3 Weakly revealing condition in the overcomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") with $m = 1$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 2 ($m$-step $\\alpha$-weakly revealing condition)", "weight": 1.0} -->

Finally, we remark that in case that $O^{m} \geq S$, a sufficient condition to make Assumption 2. ‣ 3.3 Weakly revealing condition in the overcomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?") hold is that: for any stage $h$, there exists a $({m - 1})$-step action sequence such that the $m$-step observation sequences under this action sequence is $\alpha$-weakly revealing the hidden state. Formally, for any $h \in {\lbrack H\rbrack}$ and $\mathbf{a} \in \mathcal{A}^{m - 1}$ let ${\mathbb{M}}_{h,\mathbf{a}}$ stands for the $O^{m} \times S$ matrix obtained from ${\mathbb{M}}_{h}$ by selecting the rows of ${\mathbb{M}}_{h}$ where the row-index corresponds to $\mathbf{a}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we present our algorithm---*Optimistic Maximum Likelihood Estimation* (OMLE) and its theoretical guarantees for learning weakly revealing POMDPs in both the undercomplete and the overcomplete settings.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Undercomplete setting", "weight": 1.0} -->

For clarity, we first present the algorithm and results for learning undercomplete POMDPs under Assumption 1. ‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?"). As we will see in the later section, with a minor modification this algorithm also generalizes to learning overcomplete POMDPs under Assumption 2. ‣ 3.3 Weakly revealing condition in the overcomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?").

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

To condense notations, we use $\theta = {({\mathbb{T}},{\mathbb{O}},\mu_{1})}$ to denote the model parameters of a POMDP and use $\Theta$ to denote the collections of all possible model parameters $\theta$ that correspond to POMDPs with $S$ states, $A$ actions, and $O$ observations. To make the dependence on $\theta$ explicit, we will use $V^{\pi}{(\theta)}$ to denote the value of a policy $\pi$, while we use ${\mathbb{P}}_{\theta}^{\pi}{(\tau)}$ to denote the probability of observing a trajectory $\tau$ under policy $\pi$, when the underlying POMDP is given by $\theta$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

We also use ${\mathbb{O}}_{h}{(\theta)}$ (${\mathbb{M}}_{h}{(\theta)}$) to denote the emission matrix of $\theta$ (respectively, the multistep emission matrix of $\theta$).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Algorithm 1 gives the pseudocode of OMLE.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Optimistic planning (Lines 3-4): find the POMDP model $\theta^{k}$ with the highest optimal value in the confidence set $\mathcal{B}^{k}$ and follow the associated optimal policy $\pi^{k}$ in the episode to collect a trajectory $\tau^{k}$. ^55^5Our algorithm, as well as all existing algorithms for learning large classes of POMDPs, is computationally inefficient. In particular, a naive implementation of optimistic planning (Line 3) is to enumerate all POMDP models in an $\varepsilon$-cover of the confidence set and compute their optimal policies, which requires $e^{\Omega{({{HS^{2}A} + {HSO}})}}$ time in the worst case.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Confidence set update (Line 3): add the newly collected policy-trajectory pair into the dataset, and then update the confidence set to include those models that assign a total log-likelihood to the data that is "close" to the maximum possible such total log-likelihood. In particular, the form of the confidence set is

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

where $\mathcal{B}^{1}$ is the initial confidence set that contains all $\alpha$-weakly revealing models of a given size.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Compared to the standard maximum likelihood estimation (MLE) approach, all $\alpha$-weakly revealing models with a sufficiently high likelihood are allowed and the size of this set is controlled by $\beta \geq 0$. In particular, if $\beta = 0$, the confidence set collapses to the solutions of MLE.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

In our algorithm, the choice of $\beta$ is governed by the magnitude of the "statistical noise" introduced by various random events. By analyzing this noise, one can choose the value of $\beta$ to guarantee that the true POMDP model is always contained in the resulting confidence set with a prescribed probability (see Proposition 13 for a rigorous statement).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

We emphasize that the algorithm design of MLE is considerably simpler than that of prior provably sample-efficient algorithms for learning POMDPs, which rely on spectral methods.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

4: execute policy πk to collect a trajectory τk:= (o1k,a1k,…,ohk,ahk)
5: add (πk,τk) into 𝒟 and update

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Algorithm 1 Optimistic Maximum Likelihood Estimation (OMLE)

<!-- chunk {"id": "body-0057", "role": "body", "section": "Theoretical guarantees", "weight": 1.0} -->

Our main result, which shows that OMLE will achieve small regret in any *weakly revealing POMDPs* (Assumption 1. ‣ 3.2 Weakly revealing condition in the undercomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?")),

<!-- chunk {"id": "body-0058", "role": "body", "section": "Overcomplete setting", "weight": 1.0} -->

We now turn to the more challenging setting of learning in overcomplete POMDPs, where the number of hidden states can be larger than the number of observations. We show that a simple variant of OMLE is able to learn weakly-revealing overcomplete POMDPs in a polynomial number of samples. As we shall see, we pay a nontrivial price for the increased generality: while we can still achieve rate-optimal PAC-results, we compromise on the regret of the algorithm.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Algorithm 2 shows the pseudo-code of OMLE suitable for $m$-step $\alpha$-weakly revealing overcomplete POMDPs.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Instead of merely following the optimistic policy, Algorithm 2 adopts a more active strategy for exploration. Specifically, for each optimistic policy $\pi^{k}$, the learner will one by one experiments with $({{H - m} + 1})$ policies that are obtained by picking a within-episode time index $h \in {\{ 0,\ldots,{H - m}\}}$ and then following policy $\pi^{k}$ for the first $h$ steps, and then picking actions uniformly at random in the remaining steps of the episode. We denote the resulting policy by ${\pi_{1:h}^{k} \circ \text{uniform}}{(\mathcal{A})}$, which abuses notation, but should improve readability.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

When constructing the confidence set, Algorithm 2 requires the minimum singular value of the $m$-step emission-action matrix (defined in equation ) to be lower bounded by $\alpha$, which enforces the multi-step *$\alpha$-weakly revealing* condition in Assumption 2. ‣ 3.3 Weakly revealing condition in the overcomplete setting ‣ 3 Weakly Revealing POMDPs ‣ When Is Partially Observable Reinforcement Learning Not Scary?").

<!-- chunk {"id": "body-0062", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

By trying random action sequences after executing $\pi^{k}$ for the initial $h$ steps, the learner can gather more information about the hidden states reachable by $\pi^{k}$ at step $h$ and therefore can better learn the system dynamics under $\pi^{k}$. The price of trying random actions is that the algorithm as described here will in general have linear regret. Nevertheless, with an online-to-batch conversion, Algorithm 2 serves as a suitable approach to learning a good policy with low sample complexity.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

5: execute policy π1: hk ∘ uniform (𝒜) to collect a trajectory τk, h then add (π1: hk ∘ uniform (𝒜),τk, h) into 𝒟

<!-- chunk {"id": "body-0064", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Algorithm 2 Multi-step Optimistic Maximum Likelihood Estimation

<!-- chunk {"id": "body-0065", "role": "body", "section": "Theoretical guarantees", "weight": 1.0} -->

Our main result in this section bounds the total suboptimality of the policies $\pi^{1},\ldots,\pi^{k}$ chosen by OMLE. Note that since OMLE is not following these policies, the regret of OMLE is different (in general, higher) than the total suboptimality.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Observable operator models", "weight": 1.0} -->

To begin, we introduce the observable operators that provide an alternate parameterization of POMDPs. These operators will serve as intermediate quantities in our analysis: They will allow us to bound the suboptimality of the learned policies as a function of the "width" of the MLE confidence set.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Observable operator models", "weight": 1.0} -->

where ${{\mathbb{O}}_{h}{({o \mid \cdot})}} \in {\mathbb{R}}^{S}$ denotes the $o^{th}$ row of ${\mathbb{O}}_{h}$. It is known that the these operators give an equivalent parameterization of the POMDPs: For any policy, the distribution induced by a POMDP over the possible trajectories of observation-action pairs can be described solely using these operators. In particular, the probability of observing trajectory $\tau_{h} = {(o_{1},a_{1},\ldots,o_{h},a_{h})}$ under policy $\pi$ in POMDP model $\theta$ is given by

<!-- chunk {"id": "body-0068", "role": "body", "section": "Observable operator models", "weight": 1.0} -->

where ${\pi{(\tau_{h})}}:={\prod_{h^{\prime} = 1}^{h}{\pi{({a_{h} \mid {o_{h},\tau_{h - 1}}})}}}$ represents the part of the probability of $\tau_{h}$ that can be attributed to the randomness of the policy and we used $\mathbf{B}_{j}{( \cdot;\theta)}$ to denote the observable operators underlying $\theta$. One important advantage of adopting this operator representation of POMDPs is that the linear structure facilitates us to use existing tools from matrix analysis to analyze the error of operator estimates.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Step 1: bound the regret by the error of operator estimates", "weight": 1.0} -->

where $\tau_{H} = {(o_{1},a_{1},\ldots,o_{H},a_{H})}$ denotes a whole trajectory and the second inequality uses the fact that the cumulative reward of each trajectory is bounded by $H$. Therefore, to prove Theorem 1, it suffices to bound the total cumulated error in estimating the probability of the individual trajectories, cf. the RHS of.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Step 2: derive constraints for the operator estimates from OMLE", "weight": 1.0} -->

Now let us make a detour to see what guarantees OMLE can provide for our operator estimates. As a result of the classic MLE analysis, we can show under the same choice of $\beta$ as Theorem 4. ‣ Theoretical guarantees ‣ 4.1 Undercomplete setting ‣ 4 Main Results ‣ When Is Partially Observable Reinforcement Learning Not Scary?"), with high probability

<!-- chunk {"id": "body-0071", "role": "body", "section": "Step 2: derive constraints for the operator estimates from OMLE", "weight": 1.0} -->

(Proposition 14 in Appendix A gives the precise result.) In brief, this means the model estimate in the $k^{th}$ iteration, that is $\theta^{k}$, can be used to predict the behavior of the policies followed *before* the $k^{th}$ iteration to a certain accuracy. To proceed, we represent the probabilities in equation by products of operators using equation and perform further algebraic transformations, which eventually leads to the following lemma for our operator estimates. The proof of this lemma is given in Appendix E.2.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Step 3: bridge Step $1$ and $2$ via $\\ell_{1}$-norm eluder dimension", "weight": 1.0} -->

To prove the sample efficiency of optimistic algorithms, one needs to argue that, after a sufficient number of iterations, the size of the maintained confidence set is small enough to guarantee near-optimality of the learned policy. This is typically achieved by resorting to the pigeon-hole principle in the tabular setting, or to the elliptical potential lemma in the linear setting.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Step 3: bridge Step $1$ and $2$ via $\\ell_{1}$-norm eluder dimension", "weight": 1.0} -->

In the context of this paper, by further algebraic transformations, we reduce the problem of bounding by to proving the following algebraic inequality, which plays a similar role as the elliptical potential lemma. The full inequality is more involved (see Proposition 22 in Appendix C); here we present a simplified version for the sake of simplicity.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we identified a new rich class of POMDPs, which we call *weakly revealing* POMDPs. *Weakly revealing* POMDPs subsume a majority of existing POMDPs that are known to be sample-efficiently learnable, and include both undercomplete and overcomplete POMDPs. We further propose a new simple algorithm, OMLE, which combines optimism with maximum likelihood estimation. We prove that OMLE can learn a near-optimal policy for any weakly revealing POMDP using polynomial samples. We complement our positive results with two lower bounds to justify the necessity of the appearance of certain problem-dependent quantities in our upper bounds. Finally, while our work shows that sample-efficient learning is possible in large classes of POMDPs, computationally efficient learning of POMDPs remains challenging, which we leave for future work.
