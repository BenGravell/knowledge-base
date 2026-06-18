<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Certificates: Towards Accountable Reinforcement Learning

Topics include Reinforcement learning, Regret bounds, Learning, Certificates.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The performance of a reinforcement learning algorithm can vary drastically during learning because of exploration. Existing algorithms provide little information about the quality of their current policy before executing it, and thus have limited use in high-stakes applications like healthcare. We address this lack of accountability by proposing that algorithms output policy certificates. These certificates bound the sub-optimality and return of the policy in the next episode, allowing humans to intervene when the certified quality is not satisfactory. We further introduce two new algorithms with certificates and present a new framework for theoretical analysis that guarantees the quality of their policies and certificates. For tabular MDPs, we show that computing certificates can even improve the sample-efficiency of optimism-based exploration. As a result, one of our algorithms is the first to achieve minimax-optimal PAC bounds up to lower-order terms, and this algorithm also matches (and in some settings slightly improves upon) existing minimax regret bounds.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is increasing excitement around applications of machine learning, but also growing awareness and concerns about fairness, accountability and transparency. Recent research aims to address these concerns but most work focuses on supervised learning and only few results exist on reinforcement learning (RL).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

One challenge when applying RL in practice is that, unlike in supervised learning, the performance of an RL algorithm is typically not monotonically increasing with more data due to the trial-and-error nature of RL that necessitates exploration. Even sharp drops in policy performance during learning are common, e.g., when the agent starts to explore a new part of the state space. Such unpredictable performance fluctuation has limited the use of RL in high-stakes applications like healthcare, and calls for more *accountable* algorithms that can quantify and reveal their performance online during learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this lack of accountability, we propose that RL algorithms output *policy certificates* in episodic RL. Policy certificates consist of a confidence interval of the algorithm's expected sum of rewards (return) in the next episode (policy return certificates) and a bound on how far from the optimal return the performance can be (policy optimality certificates). Certificates make the policy's performance more transparent and accountable, and allow designers to intervene if necessary. For example, in medical applications, one would need to intervene unless the policy achieves a certain minimum treatment outcome; in financial applications, policy optimality certificates can be used to assess the potential loss when learning a trading strategy. In addition to accountability, we also want RL algorithms to be sample-efficient and quickly achieve good performance. To formally quantify accountability and sample-efficiency of an algorithm, we introduce a new framework for theoretical analysis called IPOC. IPOC bounds guarantee that certificates indeed bound the algorithm's expected performance in an episode, and prescribe the rate at which the algorithm's policy and certificates improve with more data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

IPOC is stronger than other frameworks like regret, PAC and Uniform-PAC, that only guarantee the cumulative performance of the algorithm, but do not provide bounds for *individual* episodes during learning. IPOC also provides stronger bounds and more nuanced guarantees on per episode performance than KWIK.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural way to create accountable and sample-efficient RL algorithms is to combine existing sample-efficient algorithms with off-policy policy evaluation approaches to estimate the return (expected sum of rewards) of the algorithm's policy before each episode. Existing policy evaluation approaches estimate the return of a fixed policy from a batch of data. They provide little to no guarantees when the policy is not fixed but computed from that same batch of data, as is here the case. They also do not reason about the return of the unknown optimal policy which is necessary for providing policy optimality certificates. We found that by focusing on optimism-in-the-face-of-uncertainty (OFU) based RL algorithms for updating the policy and model-based policy evaluation techniques for estimating the policy returns, we can create sample-efficient algorithms that compute policy certificates on both the current policy's return and its difference to the optimal return. The main insight is that OFU algorithms compute an upper confidence bound on the optimal return from an empirical model when updating the policy. Model-based policy evaluation can leverage the same empirical model to compute a confidence interval on the policy return, even when the policy depends on the data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We illustrate this approach with new algorithms for two different episodic settings.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Perhaps surprisingly, we show that in tabular Markov decision processes (MDPs) it can be beneficial to explicitly leverage the combination of OFU-based policy optimization and model-based policy evaluation to improve either component. Specifically, computing the certificates can directly improve the underlying OFU approach and knowing that the policy converges to the optimal policy at a certain rate improves the accuracy of policy return certificates. As a result, the guarantees for our new algorithm improve state-of-the-art regret and PAC bounds in problems with large horizons and are minimax-optimal up to lower-order terms.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second setting we consider are finite MDPs with linear side information (context), which is of particular interest in practice. For example, in a drug treatment optimization task where each patient is one episode, context is the background information of the patient which influences the treatment outcome. While one expects the algorithm to learn a good policy quickly for frequent contexts, the performance for unusual patients may be significantly more variable due to the limited prior experience of the algorithm. Policy certificates allow humans to detect when the current policy is good for the current patient and intervene if a certified performance is deemed inadequate. For example, for this health monitoring application, a human expert could intervene to either directly specify the policy for that episode, or in the context of automated customer service, the service could be provided at reduced cost to the customer.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce policy certificates and the IPOC framework for evaluating RL algorithms with certificates. Similar to existing frameworks like PAC, it provides formal requirements to be satisfied by the algorithm, here requiring the algorithm to be an efficient learner and to quantify its performance online through policy certificates.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a new RL algorithm for finite, episodic MDPs that satisfies this definition, and show that it has stronger, minimax regret and PAC guarantees than prior work. Formally, our sample complexity bound is $\overset{\sim}{O}{({{{SAH^{2}}/\epsilon^{2}} + {{S^{2}AH^{3}}/\epsilon}})}$ vs. prior $\overset{\sim}{O}{({{{SAH^{4}}/\epsilon^{2}} + {{S^{2}AH^{3}}/\epsilon}})}$, and our regret bound $\overset{\sim}{O}{({\sqrt{SAH^{2}T} + {S^{2}AH^{3}}})}$ improves prior work since it has minimax rate up to log-terms in the dominant term even for long horizons $H > {SA}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a new RL algorithm for finite, episodic MDPs with linear side information that has a cumulative IPOC bound, which is tighter than past results by a factor of $\sqrt{SAH}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Setting and Notation", "weight": 1.0} -->

We consider episodic RL problems where the agent interacts with the environment in episodes of a certain length. While the framework for policy certificates applies more breadly, we focus on finite MDPs with linear side information for concreteness. This setting includes tabular MDPs as a special case but is more general and can model variations in the environment across episodes, e.g., because different episodes correspond to treating different patients in a healthcare application. Unlike the tabular special case, function approximation is necessary for efficient learning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tabular MDPs", "weight": 1.0} -->

The agent interacts with the MDP in episodes indexed by $k$. Each episode is a sequence $(s_{k,1},a_{k,1},r_{k,1},\ldots,s_{k,H},a_{k,H},r_{k,H})$ of $H$ states $s_{k,h} \in \mathcal{S}$, actions $a_{k,h} \in \mathcal{A}$ and scalar rewards $r_{k,h} \in {\lbrack 0,1\rbrack}$. For notational simplicity, we assume that the initial state $s_{k,1}$ is deterministic.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Tabular MDPs", "weight": 1.0} -->

The actions are taken as prescribed by the agent's policy $\pi_{k}$ and we here focus on deterministic time-dependent policies, i.e., $a_{k,h} = {\pi_{k}{(s_{k,h},h)}}$ for all time steps $h \in {\lbrack H\rbrack}:={\{ 1,2,{\ldotsH}\}}$. The successor states and rewards are sampled from the MDP as $s_{k,{h + 1}} \sim {P{(s_{k,h},a_{k,h})}}$ and $r_{k,h} \sim {P_{R}{(s_{k,h},a_{k,h})}}$. In tabular MDPs the size of the state space $S = {|\mathcal{S}|}$ and action space $A = {|\mathcal{A}|}$ are finite.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Return and optimality gap", "weight": 1.0} -->

The quality of a policy $\pi$ in any episode $k$ is evaluated by the *total expected reward* or *return*: ${\rho_{k}{(\pi)}}:={{\mathbb{E}}\left\lbrack {\left. {\sum_{h = 1}^{H}r_{k,h}} \middle| a_{{k,1}:H} \right. \sim \pi} \right\rbrack}$, where this notation means that all actions in the episode are taken as prescribed by a policy $\pi$. Optimal policy and return $\rho_{k}^{\star} = {{\max_{\pi}\rho_{k}}{(\pi)}}$ may depend on the episode's contexts.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Return and optimality gap", "weight": 1.0} -->

The difference of achieved and optimal return is called *optimality gap* $\Delta_{k} = {\rho_{k}^{\star} - {\rho_{k}{(\pi_{k})}}}$ for each episode $k$ where $\pi_{k}$ is the algorithm's policy in that episode.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The IPOC Framework", "weight": 1.0} -->

During execution, the optimality gaps $\Delta_{k}$ are hidden and the algorithm only observes the sum of rewards which is a sample of $\rho_{k}{(\pi_{k})}$. This causes risk as one does not know whether the algorithm is playing a good or potentially bad policy. We introduce a new learning framework that mitigates this limitation. This framework forces the algorithm to output its current policy $\pi_{k}$ as well as certificates $\epsilon_{k} \in {\mathbb{R}}_{+}$ and $\mathcal{I}_{k} \subseteq {\mathbb{R}}$ before each episode $k$. The *return certificate* $\mathcal{I}_{k}$ is a confidence interval on the return of the policy, while the *optimality certificate* $\epsilon_{k}$ informs the user how sub-optimal the policy can be for the current context, i.e., $\epsilon_{k} \geq \Delta_{k}$. Certificates allow one to intervene if needed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The IPOC Framework", "weight": 1.0} -->

For example, in automated customer services, one might reduce the service price in episode $k$ if certificate $\epsilon_{k}$ is above a certain threshold, since the quality of the provided service cannot be guaranteed. When there is no context, an optimality certificate upper bounds the sub-optimality of the current policy in any episode which makes algorithms anytime interruptable: one is guaranteed to always know a policy with improving performance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Relation to Existing Frameworks", "weight": 1.0} -->

Unlike IPOC, existing frameworks for RL only guarantee sample-efficiency of the algorithm over multiple episodes and do not provide performance bounds for single episodes during learning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Relation to Existing Frameworks", "weight": 1.0} -->

*Mistake-style PAC bounds* bound the number of $\epsilon$-mistakes, that is, the size of the set $\{{k \in {\mathbb{N}}}:{\Delta_{k} > \epsilon}\}$ with high probability, but do not tell us when mistakes happen. The same is true for the stronger Uniform-PAC bounds which hold for all $\epsilon$ jointly.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Relation to Existing Frameworks", "weight": 1.0} -->

*Supervised-learning style PAC bounds* ensure that the algorithm outputs an $\epsilon$-optimal policy for a given $\epsilon$, i.e., they ensure $\Delta_{k} \leq \epsilon$ for $k$ greater than the bound. Yet, they need to know $\epsilon$ ahead of time and tell us nothing about $\Delta_{k}$ during learning (for $k$ smaller than the bound).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Relation to Existing Frameworks", "weight": 1.0} -->

*Regret bounds* control the cumulative sum of optimality gaps $\sum_{k = 1}^{T}\Delta_{k}$ (regret) which does not yield any nontrivial guarantee for individual $\Delta_{k}$ because it does not reveal which optimality gaps are small.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Relation to Existing Frameworks", "weight": 1.0} -->

We show that mistake IPOC bounds are stronger than any of the above guarantees, i.e., they imply Uniform PAC, PAC, and regret bounds. Cumulative IPOC bounds are slightly weaker but still imply regret bounds. Both versions of IPOC also ensure that the algorithm is anytime interruptable, i.e., it can be used to find better and better policies that have small $\Delta_{k}$ with high probability $1 - \delta$. That means IPOC bounds imply supervised-learning style PAC bounds for all $\epsilon$ jointly.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithms with Policy Certificates", "weight": 1.0} -->

A natural path to obtain RL algorithms with IPOC bounds is to combine existing provably efficient online RL algorithms with an off-policy policy evaluation method to compute a confidence interval on the online RL algorithm's policy for the current episode. This yields policy return certificates, but not necessarily policy optimality certificates -- bounds on the difference of the optimal and current policy's return. Estimating the optimal return using off-policy evaluation algorithms in order to compute optimality certificates would require a significant computational burden, e.g. evaluating all (exponentially many) policies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithms with Policy Certificates", "weight": 1.0} -->

However optimism in the face of uncertainty (OFU) algorithms can be modified to provide both policy return certificates and optimality certificates without the need for a separate off-policy policy optimization step. Specifically, we here consider OFU algorithms that maintain an upper confidence bound (for a potentially changing confidence level) on the optimal value function $Q_{k,h}^{\star}$ and therefore optimal return $\rho_{k}^{\star}$. This bound is also an upper bound on the return of the current policy which is chosen to maximize this bound. Many OFU methods explicitly maintain a confidence set of the MDP model to compute the upper confidence bound on $Q_{k,h}^{\star}$. These same confidence sets of the model can be used to compute a lower bound on the value function of the current policy. In doing so, OFU algorithms can be modified with little computational overhead to provide policy return and optimality certificates.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithms with Policy Certificates", "weight": 1.0} -->

For these reasons, we focus on OFU methods, introducing two new algorithms with policy certificates, one for tabular MDPs and and one for the more general MDPs with linear side information setting. Both approaches have a similar structure, but leverage different confidence sets and model estimators. In the first case, we show that maintaining lower bounds on the current policy's value has significant benefits beyond enabling policy certificates: lower bounds help us to derive a tighter bound on our uncertainty over the range of future values. Thus we are able to provide the strongest, to our knowledge, PAC and regret bounds for tabular MDPs. It remains an intriguing but non-trivial question if we can create confidence sets that leverage explicit upper and lower bounds for the linear side information setting.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Tabular MDPs", "weight": 1.0} -->

We present the ORLC (optimistic RL with certificates) Algorithm shown in Algorithm 1 (see the appendix for a version with empirically tighter confidence bounds but same theoretical guarantees). It shares similar structure with recent OFU algorithms like UBEV and UCBVI-BF but has some significant differences highlighted in red. Before each episode $k$, Algorithm 1 computes an optimistic estimate ${\overset{\sim}{Q}}_{k,h}$ of $Q_{h}^{\star}$ in Line 1 by dynamic programming on the empirical model $({\hat{P}}_{k},{\hat{r}}_{k})$ with confidence intervals $\psi_{k,h}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Tabular MDPs", "weight": 1.0} -->

Importantly, it also computes ${\underset{\sim}{Q}}_{k,h}$, a pessimistic estimate of $Q_{h}^{\pi_{k}}$ in similar fashion in Line 1. The optimistic and pessimistic estimates ${\underset{\sim}{Q}}_{k,h},{\overset{\sim}{Q}}_{k,h}$ (resp. ${\underset{\sim}{V}}_{k,h},{\overset{\sim}{V}}_{k,h}$) allow us to compute the certificates $\epsilon_{k}$ and $\mathcal{I}_{k}$ and enables more sample-efficient learning. Specifically, Algorithm 1 uses a novel form of confidence intervals $\psi$ that explicitly depends on this difference.

<!-- chunk {"id": "body-0031", "role": "body", "section": "MDPs With Linear Side Information", "weight": 1.0} -->

We now present an algorithm for the more general setting with side information, which, for example, allows us to take background information about a customer into account and generalize across different customers. Algorithm 2 gives an extension, called ORLC-SI, of the OFU algorithm by Abbasi-Yadkori & Neu. Its overall structure is the same as the tabular Algorithm 1 but here the empirical model are least-squares estimates of the model parameters evaluated at the current contexts. Specifically, the empirical transition probability ${\hat{P}}_{k}{(\left. s^{\prime} \middle| {s,a} \right.)}$ is ${(x_{k}^{(p)})}^{\top}{\hat{\theta}}_{s^{\prime},s,a}$ where ${\hat{\theta}}_{s^{\prime},s,a}$ is the least squares estimate of model parameter $\theta_{s^{\prime},s,a}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "MDPs With Linear Side Information", "weight": 1.0} -->

Since transition probabilities are normalized, this estimate is then clipped to $\lbrack 0,1\rbrack$. This model is estimated separately for each $(s^{\prime},s,a)$-triple, but generalizes across different contexts. The confidence widths $\psi_{k,h}$ are derived using ellipsoid confidence sets on model parameters.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

One important use case for certificates is to detect sudden performance drops when the distribution of contexts changes. For example, in a call center dialogue system, there can be a sudden increase of customers calling due to a certain regional outage. We demonstrate that certificates can identify such performance drops caused by context shifts. We consider a simulated MDP with $10$ states, $40$ actions and horizon $5$ where rewards depend on a $10$-dimensional context and let the distribution of contexts change after $2$M episodes. As seen in Figure 1, this causes a spike in optimality gap as well as in the optimality certificates. While our certificates need to upper bound the optimality gap / contain the return in each episode up to a small failure probability, even for the worst case, our algorithm reliably can detect this sudden decrease of performance. In fact, the optimality certificates have a very high correlation of $0.94$ with the unobserved optimality gaps.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Experiment", "weight": 1.0} -->

One also may wonder if our algorithms leads to improvements over prior approaches in practice or only in the theoretical bounds. To help answer this, we present results in Appendix E at both on analyzing the policy certificates provided, and examining ORLC's performance in tabular MDPs versus other recent papers with similar regret or PAC bounds. Encouragingly in the small simulation MDPs considered, we find that our algorithms lead to faster learning and better performance. Therefore while our primary contribution is theoretical results, these simulations suggest the potential benefits of the ideas underlying our proposed framework and algorithms.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We introduced policy certificates to improve accountability in RL by enabling users to intervene if the guaranteed performance is deemed inadequate. Bounds in our new theoretical framework IPOC ensure that certificates indeed bound the return and suboptimality in each episode and prescribe the rate at which certificates and policy improve. By combining optimism-based exploration with model-based policy evaluation, we have created two algorithms for RL with policy certificates, including for tabular MDPs with side information. For tabular MDPs, we demonstrated that policy certificates help optimism-based policy learning and vice versa. As a result, our new algorithm is the first to achieve minimax-optimal PAC bounds up to lower-order terms for tabular episodic MDPs, and, also the first to have both, minimax PAC and regret bounds, for this setting.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Future areas of interest include scaling up these ideas to continuous state spaces, extending them to model-free RL, and to provide per-episode risk-sensitive guarantees on the reward obtained.
