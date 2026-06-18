<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Q-learning

Topics include Reinforcement learning, Q-learning, Temporal difference learning, Markov decision process, Dynamic programming, Convergence proof.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents the canonical convergence proof for Watkins's Q-learning algorithm in controlled Markov domains with discrete action values and repeated exploration. The paper established Q-learning as a simple off-policy temporal-difference method for learning optimal action values without a model of the environment.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Q -learning is a simple way for agents to learn how to act optimally in controlled Markovian domains. It amounts to an incremental method for dynamic programming which imposes limited computational demands. It works by successively improving its evaluations of the quality of particular actions at particular states. This paper presents and proves in detail a convergence theorem for Q -learning based on that outlined in Watkins. We show that Q -learning converges to the optimum action-values with probability 1 so long as all actions are repeatedly sampled in all states and the action-values are represented discretely. We also sketch extensions to the cases of non-discounted, but absorbing, Markov environments, and where many Q values can be changed each iteration, rather than just one.
