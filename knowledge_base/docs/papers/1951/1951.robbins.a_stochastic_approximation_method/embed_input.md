<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Stochastic Approximation Method

Topics include Stochastic approximation, Robbins-Monro algorithm, Stochastic root finding, Sequential experiments, Recursive estimation, Noisy observations, Convergence in probability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Robbins and Monro introduce the stochastic approximation procedure for solving a root-finding problem when the function can only be observed through noisy experiments. The paper is a foundation for recursive estimation and stochastic optimization because it shows how carefully chosen diminishing step sizes can drive sequential experimental levels toward the target in probability.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Let M(x) denote the expected value at level x of the response to a certain experiment. M(x) is assumed to be a monotone function of x but is unknown to the experimenter, and it is desired to find the solution x = theta of the equation M(x) = alpha, where alpha is a given constant. We give a method for making successive experiments at levels x_1, x_2,... in such a way that x_n will tend to theta in probability.
