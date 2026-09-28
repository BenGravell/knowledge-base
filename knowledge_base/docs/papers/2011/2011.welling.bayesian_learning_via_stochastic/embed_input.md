<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bayesian Learning via Stochastic Gradient Langevin Dynamics

Topics include Bayesian inference, Stochastic gradient langevin dynamics, Posterior sampling, Markov chain Monte Carlo, Mini-batch learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces stochastic gradient Langevin dynamics, adding calibrated noise to mini-batch gradient updates so an annealed optimization trajectory becomes a posterior sampler. It also proposes a threshold for collecting samples and demonstrates the method on three models.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we propose a new framework for learning from large scale datasets based on iterative learning from small mini-batches. By adding the right amount of noise to a standard stochastic gradient optimization algorithm we show that the iterates will converge to samples from the true posterior distribution as we anneal the stepsize. This seamless transition between optimization and Bayesian posterior sampling provides an in-built protection against overfitting. We also propose a practical method for Monte Carlo estimates of posterior statistics which monitors a ``sampling threshold'' and collects samples after it has been surpassed. We apply the method to three models: a mixture of Gaussians, logistic regression and ICA with natural gradients.
