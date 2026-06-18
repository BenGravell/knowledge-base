<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Linear Quadratic Control Using Model-Free Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this article, we consider linear quadratic (LQ) control problem with process and measurement noises. We analyze the LQ problem in terms of the average cost and the structure of the value function. We assume that the dynamics of the linear system is unknown and only noisy measurements of the state variable are available. Using noisy measurements of the state variable, we propose two model-free iterative algorithms to solve the LQ problem. The proposed algorithms are variants of policy iteration routine where the policy is greedy with respect to the average of all previous iterations. We rigorously analyze the properties of the proposed algorithms, including stability of the generated controllers and convergence. We analyze the effect of measurement noise on the performance of the proposed algorithms, the classical off-policy, and the classical Q -learning routines. We also investigate a model-building approach, inspired by adaptive control, where a model of the dynamical system is estimated and the optimal control problem is solved assuming that the estimated model is the true model. We use a benchmark to evaluate and compare our proposed algorithms with the classical off-policy, the classical Q -learning, and the policy gradient.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that our model-building approach performs nearly identical to the analytical solution and our proposed policy iteration-based algorithms outperform the classical off-policy and the classical Q -learning algorithms on this benchmark but do not outperform the model-building approach.
