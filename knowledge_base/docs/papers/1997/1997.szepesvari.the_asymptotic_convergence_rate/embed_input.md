<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Asymptotic Convergence-Rate of Q-learning

Topics include Reinforcement learning, Q-learning, Convergence rate, Markov decision process, Stochastic approximation, Temporal difference learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives asymptotic convergence-rate bounds for Q-learning under fixed or stationary state-action sampling distributions. The paper refines the theoretical understanding of how discounting and visitation-frequency imbalance affect stochastic-approximation speed in tabular reinforcement learning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we show that for discounted MDPs with discount factor greater than 1/2 the asymptotic rate of convergence of Q-learning is O(1/t^R(1-gamma)) if R(1 - gamma) < 1/2 and O(sqrt(log log t / t)) otherwise provided that the state-action pairs are sampled from a fixed probability distribution. Here R = p_min / p_max is the ratio of the minimum and maximum state-action occupation frequencies. The results extend to convergent on-line learning provided that p_min > 0, where p_min and p_max now become the minimum and maximum state-action occupation frequencies corresponding to the stationary distribution.
