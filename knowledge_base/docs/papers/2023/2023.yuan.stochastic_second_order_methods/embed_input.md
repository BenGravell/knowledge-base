<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Second Order Methods and Finite Time Analysis of Policy Gradient Methods

Topics include Research paper.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To solve large scale machine learning problems, first-order methods such as stochastic gradient descent and ADAM are the methods of choice because of their low cost per iteration. The issue with first order methods is that they can require extensive parameter tuning, and/or knowledge of the parameters of the problem. There is now a concerted effort to develop efficient stochastic second order methods to solve large scale machine learning problems. The motivation is that they require less parameter tuning and converge for wider variety of models and datasets. In the first part of the thesis, we presented a principled approach for designing stochastic Newton methods for solving both nonlinear equations and optimization problems in an efficient manner. Our approach has two steps. First, we can re-write the nonlinear equations or the optimization problem as desired nonlinear equations. Second, we apply new stochastic second order methods to solve this system of nonlinear equations. Through our general approach, we showcase many specific new second-order algorithms that can solve the large machine learning problems efficiently without requiring knowledge of the problem nor parameter tuning. In the second part of the thesis, we then focus on optimization algorithms applied in a specific domain: reinforcement learning (RL).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This part is independent to the first part of the thesis. To achieve such high performance of RL problems, policy gradient (PG) and its variant, natural policy gradient (NPG), are the foundations of the several state of the art algorithms (e.g., TRPO and PPO) used in deep RL. In spite of the empirical success of RL and PG methods, a solid theoretical understanding of even the “vanilla” PG has long been elusive. By leveraging the RL structure of the problem together with modern optimization proof techniques, we derive new finite time analysis of both PG and NPG. Through our analysis, we also bring new insights to the methods with better hyperparameter choices.
