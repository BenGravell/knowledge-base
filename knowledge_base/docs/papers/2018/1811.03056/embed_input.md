Policy Certificates: Towards Accountable Reinforcement Learning

Topics include Reinforcement learning, Regret bounds, Learning, Certificates.

The performance of a reinforcement learning algorithm can vary drastically during learning because of exploration. Existing algorithms provide little information about the quality of their current policy before executing it, and thus have limited use in high-stakes applications like healthcare. We address this lack of accountability by proposing that algorithms output policy certificates. These certificates bound the sub-optimality and return of the policy in the next episode, allowing humans to intervene when the certified quality is not satisfactory. We further introduce two new algorithms with certificates and present a new framework for theoretical analysis that guarantees the quality of their policies and certificates. For tabular MDPs, we show that computing certificates can even improve the sample-efficiency of optimism-based exploration. As a result, one of our algorithms is the first to achieve minimax-optimal PAC bounds up to lower-order terms, and this algorithm also matches (and in some settings slightly improves upon) existing minimax regret bounds.

## Introduction

There is increasing excitement around applications of machine learning, but also growing awareness and concerns about fairness, accountability and transparency. Recent research aims to address these concerns but most work focuses on supervised learning and only few results exist on reinforcement learning (RL).

To address this lack of accountability, we propose that RL algorithms output *policy certificates* in episodic RL. Policy certificates consist of a confidence interval of the algorithm's expected sum of rewards (return) in the next episode (policy return certificates) and a bound on how far from the optimal return the performance can be (policy optimality certificates). Certificates make the policy's performance more transparent and accountable, and allow designers to intervene if necessary.

Perhaps surprisingly, we show that in tabular Markov decision processes (MDPs) it can be beneficial to explicitly leverage the combination of OFU-based policy optimization and model-based policy evaluation to improve either component. Specifically, computing the certificates can directly improve the underlying OFU approach and knowing that the policy converges to the optimal policy at a certain rate improves the accuracy of policy return certificates. As a result, the guarantees for our new algorithm improve state-of-the-art regret and PAC bounds in problems with large horizons and are minimax-optimal up to lower-order terms.

## Conclusion and Future Work

We introduced policy certificates to improve accountability in RL by enabling users to intervene if the guaranteed performance is deemed inadequate. Bounds in our new theoretical framework IPOC ensure that certificates indeed bound the return and suboptimality in each episode and prescribe the rate at which certificates and policy improve. By combining optimism-based exploration with model-based policy evaluation, we have created two algorithms for RL with policy certificates, including for tabular MDPs with side information. For tabular MDPs, we demonstrated that policy certificates help optimism-based policy learning and vice versa.

Future areas of interest include scaling up these ideas to continuous state spaces, extending them to model-free RL, and to provide per-episode risk-sensitive guarantees on the reward obtained.
