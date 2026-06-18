<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

When Should We Prefer Offline Reinforcement Learning over Behavioral Cloning?

Topics include Offline reinforcement learning, Behavior cloning, Imitation learning, Expert demonstrations, Sparse rewards, Long-horizon tasks, Suboptimal data, Robotic manipulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes when offline RL can outperform behavioral cloning even when the dataset resembles expert demonstrations. The paper identifies conditions such as sparse rewards, long horizons, and useful noise or suboptimality where value-based improvement can exploit data better than direct imitation, then validates the story across diagnostic and high-dimensional domains.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Offline reinforcement learning (RL) algorithms can acquire effective policies by utilizing previously collected experience, without any online interaction. It is widely understood that offline RL is able to extract good policies even from highly suboptimal data, a scenario where imitation learning finds suboptimal solutions that do not improve over the demonstrator that generated the dataset. However, another common use case for practitioners is to learn from data that resembles demonstrations. In this case, one can choose to apply offline RL, but can also use behavioral cloning (BC) algorithms, which mimic a subset of the dataset via supervised learning. Therefore, it seems natural to ask: when can an offline RL method outperform BC with an equal amount of expert data, even when BC is a natural choice? To answer this question, we characterize the properties of environments that allow offline RL methods to perform better than BC methods, even when only provided with expert data. Additionally, we show that policies trained on sufficiently noisy suboptimal data can attain better performance than even BC algorithms with expert data, especially on long-horizon problems.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate our theoretical results via extensive experiments on both diagnostic and high-dimensional domains including robotic manipulation, maze navigation, and Atari games, with a variety of data distributions. We observe that, under specific but common conditions such as sparse rewards or noisy data sources, modern offline RL methods can significantly outperform BC.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Offline reinforcement learning (RL) algorithms aim to leverage large existing datasets of previously collected data to produce effective policies that generalize across a wide range of scenarios, without the need for costly active data collection. Many recent offline RL algorithms can work well even when provided with highly suboptimal data, and a number of these approaches have been studied theoretically. While it is clear that offline RL algorithms are a good choice when the available data is either random or highly suboptimal, it is less clear if such methods are useful when the dataset consists of demonstration that come from expert or near-expert demonstrations. In these cases, imitation learning algorithms, such as behavorial cloning (BC), can be used to train policies via supervised learning. It then seems natural to ask: *When should we prefer to use offline RL over imitation learning?*

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To our knowledge, there has not been a rigorous characterization of when offline RL perform better than imitation learning. Existing *empirical* studies comparing offline RL to imitation learning have come to mixed conclusions. Some works show that offline RL methods appear to greatly outperform imitation learning, specifically in environments that require "stitching" parts of suboptimal trajectories. In contrast, a number of recent works have argued that BC performs better than offline RL on both expert and suboptimal demonstration data over a variety of tasks. This makes it confusing for practitioners to understand whether to use offline RL or simply run BC on collected demonstrations. Thus, in this work we aim to understand if there are conditions on the environment or the dataset under which an offline RL algorithm might outperform BC for a given task, even when BC is provided with expert data or is allowed to use rewards as side information. Our findings can inform a practitioner in determining whether offline RL is a good choice in their domain, even when expert or near-expert data is available and BC might appear to be a natural choice.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contribution in this paper is a theoretical and empirical characterization of certain conditions when offline RL outperforms BC. Theoretically, our work presents conditions on the MDP and dataset that are sufficient for offline RL to achieve better worst-case guarantees than even the *best-case lower-bound* for BC using the same amount of *expert demonstrations*. These conditions are grounded in practical problems, and provide guidance to the practitioner as to whether they should use RL or BC. Concretely, we show that in the case of expert data, the error incurred by offline RL algorithms can scale significantly more favorably when the MDP enjoys some structure, which includes horizon-independent returns (*i.e.*, sparse rewards) or a low volume of states where it is "critical" to take the same action as the expert (Section 4.2). Meanwhile, in the case of sufficiently noisy data, we show that offline RL again enjoys better guarantees on long-horizon tasks (Section 4.3).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, since BC methods ignore rewards, we consider generalized BC methods that use the observed rewards to inform learning, and show that it is still preferable to perform offline RL (Section 4.4).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically, we validate our theoretical conclusions on diagnostic gridworld domains and large-scale benchmark problems in robotic manipulation and navigation and Atari games, using human data, scripted data, and data generated from RL policies. We verify that in multiple long-horizon problems where the conditions we propose are likely to be satisfied, practical offline RL methods can outperform BC and generalized BC methods. We show that using careful offline tuning practices, we show that it is possible for offline RL to outperform cloning an expert dataset for the same task, given equal amounts of data. We also highlight open questions for hyperparameter tuning that have the potential to make offline RL methods work better in practice.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup and Preliminaries", "weight": 1.0} -->

Let $n{(\mathbf{s},\mathbf{a})}$ be the number of times $(\mathbf{s},\mathbf{a})$ appear in $\mathcal{D}$, and $\hat{P}{( \cdot |\mathbf{s},\mathbf{a})}$ and $\hat{r}{(\mathbf{s},\mathbf{a})}$ denote the empirical dynamics and reward distributions in $\mathcal{D}$, which may be different from $P$ and $r$ due to stochasticity. Following Rashidinejad et al.,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup and Preliminaries", "weight": 1.0} -->

We will now define some conditions on the offline dataset and MDP structure that we will use in our analysis. The first characterizes the distribution shift between the data distribution $\mu{(\mathbf{s},\mathbf{a})}$ and the normalized state-action marginal of $\pi^{\ast}$, given by ${d^{\ast}{(\mathbf{s},\mathbf{a})}} = {{({1 - \gamma})}{\sum_{t = 0}^{\infty}{\gamma^{t}{\mathbb{P}}\left( {{\mathbf{s}_{t} = s},{\mathbf{a}_{t} = {a;\pi^{\ast}}}} \right)}}}$, via a *concentrability coefficient* $C^{\ast}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Condition 3.1 (Rashidinejad et al., Concentrability of the data distribution)", "weight": 1.0} -->

Intuitively, the coefficient $C^{\ast}$ formalizes how well the data distribution $\mu{(\mathbf{s},\mathbf{a})}$ covers the state-action pairs visited under the optimal $\pi^{\ast}$, where $C^{\ast} = 1$ corresponds to data from $\pi^{\ast}$. If $\mu{(\mathbf{s},\mathbf{a})}$ primarily covers state-action pairs that are not visited by $\pi^{\ast}$, $C^{\ast}$ would be large. The next condition is that the return for any trajectory in the MDP is bounded by a constant, which w.l.o.g., we assume to be 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Condition 3.2 (Ren et al., the value of any trajectory is bounded by 1)", "weight": 1.0} -->

This condition holds in sparse-reward tasks, particularly those where an agent succeeds or fails at its task once per episode. This is common in domains such as robotics and games, where the agent receives a signal upon succeeding a task or winning. This condition also appears in prior work deriving suboptimality bounds for RL algorithms.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Theoretical Comparison of BC and Offline RL", "weight": 1.0} -->

In this section, we present performance guarantees for BC and offline RL, and characterize scenarios where offline RL algorithms will outperform BC. We first present general upper bounds for both algorithms in Section 4.1, by extending prior work to account for the conditions discussed in Section 3. Then, we compare the performance of BC and RL when provided with the same data generated by an expert in Section 4.2 and when RL is given noisy, suboptimal data in Section 4.3. Our goal is to characterize the conditions on the environment and offline dataset where RL can outperform BC. Furthermore, we provide intuition for when they are likely to hold in Appendix D.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Improved Performance Guarantees of BC and Offline RL", "weight": 1.0} -->

Our goal is to understand if there exist offline RL methods that can outperform BC for a given task. As our aim is to provide a proof of existence, we analyze representative offline RL and BC algorithms that achieve optimal suboptimality guarantees. For brevity, we only consider a conservative offline RL algorithm (as defined in Section 2) in the main paper and defer analysis of a representative policy-constraint method to Appendix C. Both algorithms are described in Algorithms 1 and 2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Improved Performance Guarantees of BC and Offline RL", "weight": 1.0} -->

Guarantees for BC. For analysis purposes, we consider a BC algorithm that matches the empirical behavior policy on states in the offline dataset, and takes uniform random actions outside the support of the dataset. This BC algorithm was also analyzed in prior work, and is no worse than other schemes for acting at out-of-support states in general. Denoting the learned BC policy as ${\hat{\pi}}_{\beta}$, we have ${{\forall\mathbf{s}} \in \mathcal{D}},{{{\hat{\pi}}_{\beta}{(\left. \mathbf{a} \middle| \mathbf{s} \right.)}}\leftarrow{{{n{(\mathbf{s},\mathbf{a})}}/n}{(\mathbf{s})}}}$, and ${{\forall\mathbf{s}} \notin \mathcal{D}},{{{\hat{\pi}}_{\beta}{(\left.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Improved Performance Guarantees of BC and Offline RL", "weight": 1.0} -->

\mathbf{a} \middle| \mathbf{s} \right.)}}\leftarrow{1/{|\mathcal{A}|}}}$. We adapt the results presented by Rajaraman et al. to the setting with Conditions 3.1. ‣ 3 Problem Setup and Preliminaries ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?") and 3.2. ‣ 3 Problem Setup and Preliminaries ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"). BC can only incur a non-zero asymptotic suboptimality (*i.e.*, does not decrease to $0$ as $N\rightarrow\infty$) in scenarios where $C^{\ast} = 1$, as it aims to match the data distribution $\mu{(\mathbf{s},\mathbf{a})}$, and a non-expert dataset will inhibit the cloned policy from matching the expert $\pi^{\ast}$. The performance for BC is bounded in Theorem 4.1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Improved Performance Guarantees of BC and Offline RL", "weight": 1.0} -->

‣ 4.1 Improved Performance Guarantees of BC and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Comparison Under Expert Data", "weight": 1.0} -->

We first compare the performance bounds from Section 4.1 when the offline dataset is generated from the expert. In relation to Condition 3.1. ‣ 3 Problem Setup and Preliminaries ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"), this corresponds to small $C^{\ast}$. Specifically, we consider $C^{\ast} \in {\lbrack 1,{1 + {\overset{\sim}{\mathcal{O}}{({1/N})}}}\rbrack}$ and in this case, the suboptimality of BC in Theorem 4.1. ‣ 4.1 Improved Performance Guarantees of BC and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?") scales as $\overset{\sim}{\mathcal{O}}{({{{|\mathcal{S}|}H}/N})}$. In this regime, we perform a nuanced comparison by analyzing specific scenarios where RL may outperform BC.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Comparison Under Expert Data", "weight": 1.0} -->

What happens when $C^{\ast} = 1$? In this case, we derive a lower-bound of ${{|\mathcal{S}|}H}/N$ for any offline algorithm, by utilizing the analysis of Rajaraman et al. and factoring in Condition 3.2. ‣ 3 Problem Setup and Preliminaries ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?").

<!-- chunk {"id": "body-0021", "role": "body", "section": "Condition 4.1 (Occupancy of critical states is small)", "weight": 1.0} -->

We can show that, if the MDP satisfies the above condition with a small enough $p_{c}$ and and the number of good actions $|{\mathcal{G}{(\mathbf{s})}}|$ are large enough, then by controlling the gap $\Delta{(\mathbf{s})}$ between suboptimality of good and bad actions some offline RL algorithms can outperform BC. We perform this analysis under a simplified setting where the state-marginal distribution in the dataset matches that of the optimal policy and find that a policy constraint offline RL algorithm can outperform BC. We describe the informal statement below and discuss the details and a proof in Appendix B.3.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Comparison Under Noisy Data", "weight": 1.0} -->

In practice, it is often much more tractable to obtain suboptimal demonstrations rather than expert ones. For example, suboptimal demonstrations can be obtained by running a scripted policy. From Theorem 4.1. ‣ 4.1 Improved Performance Guarantees of BC and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"), we see that for $C^{\ast} = {1 + {\Omega{({1/\sqrt{N}})}}}$, BC will incur suboptimality that is worse asymptotically than offline RL. In contrast, from Theorem 4.2. ‣ 4.1 Improved Performance Guarantees of BC and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"), we note that offline RL does not scale nearly as poorly with increasing $C^{\ast}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Comparison Under Noisy Data", "weight": 1.0} -->

Since offline RL is not as reliant on the performance of the behavior policy, we hypothesize that RL can actually benefit from suboptimal data when this improves coverage. In this section, we aim to answer the following question: *Can offline RL with suboptimal data outperform BC with an equal amount of expert data?*

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison Under Noisy Data", "weight": 1.0} -->

We show in Corollary 4.2. ‣ 4.3 Comparison Under Noisy Data ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?") that, if the suboptimal dataset $\mathcal{D}$ satisfies an additional coverage condition, then running conservative offline RL can attain $\overset{\sim}{\mathcal{O}}{(\sqrt{H})}$ suboptimality in the horizon. This implies, perhaps surprisingly, that offline RL with suboptimal data can actually outperform BC, *even when the latter is provided expert data*.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Condition 4.2 (Coverage of the optimal policy)", "weight": 1.0} -->

Intuitively, this means that the data distribution puts sufficient mass on states that have non-negligible density in the optimal policy distribution. Note that this is a weaker condition than prior works that require full coverage of the state-action space, and enforce a constraint on the empirical state-action visitations $\hat{\mu}{(\mathbf{s},\mathbf{a})}$ instead of $\mu{(\mathbf{s},\mathbf{a})}$. This condition is reasonable when the dataset is collected by $\epsilon$-greedy or a maximum-entropy expert, which is a standard assumption in MaxEnt IRL. Even if the expert is not noisy, we argue that in several real-world applications, creating noisy-expert data is feasible. In many robotics applications, it is practical to augment expert demonstrations with counterfactual data by using scripted exploration policies. Existing work has also simulated trajectories to increase coverage, as was done in self-driving by perturbing the vehicle location, or in robotics using learned simulators.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Condition 4.2 (Coverage of the optimal policy)", "weight": 1.0} -->

For intuition, we provide an illustrative example of the noisy data that can help offline RL in Figure 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison of Generalized BC Methods and Offline RL", "weight": 1.0} -->

So far we have studied scenarios where offline RL can outperform naïve BC. One might now wonder how offline RL methods perform relative to generalized BC methods that additionally use reward information to inform learning. We study two such approaches: filtered BC, which only fits to the top $k$-percentage of trajectories in $\mathcal{D}$, measured by the total reward, and BC with one-step policy improvement, which fits a Q-function for the behavior policy, then uses the values to perform one-step of policy improvement over the behavior policy. In this section, we aim to answer how these methods perform relative to RL.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparison of Generalized BC Methods and Offline RL", "weight": 1.0} -->

Filtered BC. In expectation, this algorithm uses $\alphaN$ samples of the offline dataset $\mathcal{D}$ for $\alpha \in {\lbrack 0,1\rbrack}$ to perform BC. This means that the upper bound (Theorem 4.1. ‣ 4.1 Improved Performance Guarantees of BC and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?")) will have worse scaling in $N$. For $C^{\ast} = 1$, this leads to a strictly worse bound than regular BC. However, for suboptimal data, the filtering step could decrease $C^{\ast}$ by filtering out suboptimal trajectories, allowing filtered BC to outperform traditional BC.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Comparison of Generalized BC Methods and Offline RL", "weight": 1.0} -->

Nevertheless, from our analysis in Section 4.3, offline RL is still preferred to filtered BC because RL can leverage the noisy data and potentially achieve $O{(\sqrt{H})}$ suboptimality, whereas even filtered BC would always incur a worse $O{(H)}$ suboptimality.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Comparison of Generalized BC Methods and Offline RL", "weight": 1.0} -->

*When would this algorithm perform poorly compared to offline RL?* Intutively, this would happen when multiple steps of policy improvement are needed to effectively discover high-advantage actions under the behavior policy. This is the case when the the behavior policy puts low density on high-advantage transitions. In Theorem 4.4. ‣ 4.4 Comparison of Generalized BC Methods and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"), we show that more than one step of policy improvement can improve the policy under Condition 4.2. ‣ 4.3 Comparison Under Noisy Data ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"), for the special case of the softmax policy parameterization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Having characterized scenarios where offline RL methods can outperform BC in theory, we now validate our results empirically. Concretely, we aim to answer the following questions: Does an existing offline RL method trained on expert data outperform BC on expert data in MDPs with few critical points?, Can offline RL trained on noisy data outperform BC on expert data?, and How does full offline RL compare to the reward-aware BC methods studied in Section 4.4? We first validate our findings on a tabular gridworld domain, and then study high-dimensional domains.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Diagnostic experiments on a gridworld. We first evaluate tabular versions of the BC and offline RL methods analyzed in Section 4.1 on sparse-reward $10 \times 10$ gridworlds environments. Complete details about the setup can be found in Appendix E.1. On a high-level, we consider three different environments, each with varying number of critical states, from "Single Critical" with exactly one, to "Cliffwalk" where every state is critical and veering off yields zero reward.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

In the left plot of Figure 3, we show the return (normalized by return of the optimal policy) across all the different environments for optimal data ($C^{\ast} = 1$) and data generated from the optimal policy but with a different initial state distribution ($C^{\ast} > 1$ but $\pi_{\beta}{( \cdot |\mathbf{s})} = \pi^{\ast}{( \cdot |\mathbf{s})}$).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

As expected from our discussion in Section 4.2, BC performs best under $C^{\ast} = 1$, but ${\mathtt{R}\mathtt{L}}\text{-}\mathtt{C}$ and ${\mathtt{R}\mathtt{L}}\text{-}{\mathtt{P}\mathtt{C}}$ performs much better when $C^{\ast} > 1$; also BC with one-step policy improvement outperforms naive BC for $C^{\ast} > 1$, but does not beat full offline RL. In Figure 3 (right), we vary $C^{\ast}$ by interpolating the dataset with one generated by a random policy, where $\alpha$ is the proportion of random data. RL performs much better over all BC methods, when the data supporting our analysis in Section 4.3. Finally, BC with multiple policy improvement steps performs better than one step when the data is noisy, which validates Theorem 4.4.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

‣ 4.4 Comparison of Generalized BC Methods and Offline RL ‣ 4 Theoretical Comparison of BC and Offline RL ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Evaluation in high-dimensional tasks. Next, we turn to high-dimensional problems. We consider a diverse set of domains (shown on the right) and behavior policies that are representative of practical scenarios: multi-stage robotic manipulation tasks from state (Adroit domains from Fu et al. ) and image observations, antmaze navigation, and 7 Atari games. We use the scripted

<!-- chunk {"id": "body-0037", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

expert provided by Fu et al. for antmaze and those provided by Singh et al. for manipulation, an RL-trained expert for Atari, and human expert for Adroit. We obtain suboptimal data using failed attempts from a noisy expert policy (*i.e.*, previous policies in the replay buffer for Atari, and noisy scripted experts for antmaze and manipulation). All these tasks utilize sparse rewards such that the return of any trajectory is bounded by a constant much smaller than the horizon. We use CQL as a representative offline RL method, and utilize Brandfonbrener et al. as a representative BC-PI method.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Tuning offline RL and BC. Naïvely running offline RL can lead to poor performance, as noted by prior works. This is also true for BC, but, some solutions such as early stopping based on validation losses, can help improve performance. We claim that an offline tuning strategy is also crucial for offline RL. In our experiments we utilize the offline workflow proposed by Kumar et al. to perform policy selection, and address overfitting and underfitting, purely offline. While this workflow does not fully address all the tuning issues, we find that it is sufficient to improve performance. When the Q-values learned by CQL are extremely negative (typically on the Adroit domains), we utilize a capacity-decreasing dropout regularization with probability $0.4$ on the layers of the Q-function to combat overfitting. On the other hand, when the Q-values exhibit a relatively stable trend (*e.g.*, in Antmaze or Atari), we utilize the DR3 regularizer to increase capacity.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Consistent with prior work, we find that naïve offline RL generally performs worse than BC without offline tuning, but we find that *tuned* offline RL can work well. For tuning BC and BC-PI, we applied regularizers such as dropout on the policy to prevent overfitting in Adroit, and utilized a larger ResNet architecture for the robotic manipulation tasks and Atari domains. For BC, we report the performance of the *best* checkpoint found during training, giving BC an unfair advantage, but we still find that *offline-tuned* offline RL can do better better. More details about tuning each algorithm can be found in Appendix F.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Domain / Behavior Policy
Task/Data Quality

<!-- chunk {"id": "body-0041", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Answers to questions to. For, we run CQL and BC on expert data in each task, and present the comparison in Table 1 and Figure 4. While naïve CQL performs comparable or worse than BC in this case, after offline tuning, CQL outperforms BC. This tuning does not require any additional online rollouts. Note that while BC performs better or comparable to RL for antmaze (large) with expert data, it performs worse than RL when the data admits a more diverse initial state distribution such that $C^{\ast} \neq 1$, even though the behavior policy matches the expert.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

For, we compare offline RL trained on noisy-expert data with BC trained on on an equal amount of expert data, on domains where noisy-expert data is easy to generate: (a) manipulation domains (Table 2) and (b) Atari games (Figure 4). Observe that CQL outperforms BC and also improves over only using expert data. The performance gap also increases with $H$, *i.e.*, open-grasp ($H = 40$) vs pick-place-open-grasp ($H = 80$) vs Atari domains ($H = 27000$). This validates that some form of offline RL with noisy-expert data can outperform BC with expert data, particularly on long-horizon tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Empirical Evaluation of BC and Offline RL", "weight": 1.0} -->

Finally we compare CQL to a representative BC-PI method trained using noisy-expert data on Atari domains, which present multiple stitching opportunities. The BC-PI method estimates the Q-function of the behavior policy using SARSA and then performs one-step of policy improvement. The results in Figure 4 support what is predicted by our theoretical results, *i.e.*, BC-PI still performs significantly worse than CQL with noisy-expert data, even though we utilized online rollouts for tuning BC-PI and report the best hyperparameters found.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion", "weight": 1.5} -->

We sought to understand if offline RL is at all preferable over running BC, even provided with expert or near-expert data. While in the worst case, both approaches attain similar performance on expert data, additional assumptions on the environment can provide certain offline RL methods with an advantage. We also show that running RL on noisy-expert, suboptimal data attains more favorable guarantees compared to running BC on expert data for the same task, using equal amounts of data. Empirically, we observe that offline-tuned offline RL can outperform BC on various practical problem domains, with different kinds of expert policies. While our work is an initial step towards understanding when RL presents a favorable approach, there is still plenty of room for further investigation. Our theoretical analysis can be improved to handle function approximation. Understanding if offline RL is preferred over BC for other real-world data distributions is also important. Finally, our work focuses on analyzing cases where we might expect offline RL to outperform BC. An interesting direction is to understand cases where the opposite holds; such analysis would further contribute to this discussion.
