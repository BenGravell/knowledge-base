Policy Certificates: Towards Accountable Reinforcement Learning

Topics include Reinforcement learning, Regret bounds, Learning, Certificates.

The performance of a reinforcement learning algorithm can vary drastically during learning because of exploration. Existing algorithms provide little information about the quality of their current policy before executing it, and thus have limited use in high-stakes applications like healthcare. We address this lack of accountability by proposing that algorithms output policy certificates. These certificates bound the sub-optimality and return of the policy in the next episode, allowing humans to intervene when the certified quality is not satisfactory. We further introduce two new algorithms with certificates and present a new framework for theoretical analysis that guarantees the quality of their policies and certificates. For tabular MDPs, we show that computing certificates can even improve the sample-efficiency of optimism-based exploration. As a result, one of our algorithms is the first to achieve minimax-optimal PAC bounds up to lower-order terms, and this algorithm also matches (and in some settings slightly improves upon) existing minimax regret bounds.

## Introduction

There is increasing excitement around applications of machine learning, but also growing awareness and concerns about fairness, accountability and transparency. Recent research aims to address these concerns but most work focuses on supervised learning and only few results exist on reinforcement learning (RL).

One challenge when applying RL in practice is that, unlike in supervised learning, the performance of an RL algorithm is typically not monotonically increasing with more data due to the trial-and-error nature of RL that necessitates exploration. Even sharp drops in policy performance during learning are common, e.g., when the agent starts to explore a new part of the state space. Such unpredictable performance fluctuation has limited the use of RL in high-stakes applications like healthcare, and calls for more *accountable* algorithms that can quantify and reveal their performance online during learning.

We introduced policy certificates to improve accountability in RL by enabling users to intervene if the guaranteed performance is deemed inadequate. Bounds in our new theoretical framework IPOC ensure that certificates indeed bound the return and suboptimality in each episode and prescribe the rate at which certificates and policy improve. By combining optimism-based exploration with model-based policy evaluation, we have created two algorithms for RL with policy certificates, including for tabular MDPs with side information. For tabular MDPs, we demonstrated that policy certificates help optimism-based policy learning and vice versa....

Future areas of interest include scaling up these ideas to continuous state spaces, extending them to model-free RL, and to provide per-episode risk-sensitive guarantees on the reward obtained.

episodes. Hence, for settings without context, the algorithm outputs an $\epsilon$-optimal policy within that number of episodes (supervised learning-style PAC bound).

for any threshold $\epsilon$, the number of times certificates can exceed the threshold is bounded as ${\sum_{k = 1}^{\infty}{\mathbf{1}{\{{\epsilon_{k} > \epsilon}\}}}} \leq {F{(W,\epsilon,\delta)}}$ (Mistake Version).

Table 1: Comparison of the state of the art and our bounds for episodic RL in tabular MDPs. A dash means that the algorithm does not satisfy a non-trivial bound without modifications....
