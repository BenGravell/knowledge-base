The Asymptotic Convergence-Rate of Q-learning

Topics include Reinforcement learning, Q-learning, Convergence rate, Markov decision process, Stochastic approximation, Temporal difference learning.

Derives asymptotic convergence-rate bounds for Q-learning under fixed or stationary state-action sampling distributions. The paper refines the theoretical understanding of how discounting and visitation-frequency imbalance affect stochastic-approximation speed in tabular reinforcement learning.

In this paper we show that for discounted MDPs with discount factor greater than 1/2 the asymptotic rate of convergence of Q-learning is O(1/t^R(1-gamma)) if R(1 - gamma) < 1/2 and O(sqrt(log log t / t)) otherwise provided that the state-action pairs are sampled from a fixed probability distribution. Here R = p_min / p_max is the ratio of the minimum and maximum state-action occupation frequencies. The results extend to convergent on-line learning provided that p_min > 0, where p_min and p_max now become the minimum and maximum state-action occupation frequencies corresponding to the stationary distribution.
