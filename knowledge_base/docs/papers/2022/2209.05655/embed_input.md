<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Gaussian Variational Inference Approach to Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a Gaussian variational inference framework for the motion planning problem. In this framework, motion planning is formulated as an optimization over the distribution of the trajectories to approximate the desired trajectory distribution by a tractable Gaussian distribution. Equivalently, the proposed framework can be viewed as a standard motion planning with an entropy regularization. Thus, the solution obtained is a transition from an optimal deterministic solution to a stochastic one, and the proposed framework can recover the deterministic solution by controlling the level of stochasticity. To solve this optimization, we adopt the natural gradient descent scheme. The sparsity structure of the proposed formulation induced by factorized objective functions is further leveraged to improve the scalability of the algorithm. We evaluate our method on several robot systems in simulated environments, and show that it achieves collision avoidance with smooth trajectories, and meanwhile brings robustness to the deterministic baseline results, especially in challenging environments and tasks.
