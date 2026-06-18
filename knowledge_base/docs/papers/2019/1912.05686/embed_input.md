<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bayesian Hyperparameter Optimization with BoTorch, GPyTorch and Ax

Topics include Gaussian processes, Deep learning, Autoencoders, Bayesian methods, Graphs, Optimization, Learning, Bayesian hyperparameter optimization, Bayesian optimization, Hyperparameter optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep learning models are full of hyperparameters, which are set manually before the learning process can start. To find the best configuration for these hyperparameters in such a high dimensional space, with time-consuming and expensive model training / validation, is not a trivial challenge. Bayesian optimization is a powerful tool for the joint optimization of hyperparameters, efficiently trading off exploration and exploitation of the hyperparameter space. In this paper, we discuss Bayesian hyperparameter optimization, including hyperparameter optimization, Bayesian optimization, and Gaussian processes. We also review BoTorch, GPyTorch and Ax, the new open-source frameworks that we use for Bayesian optimization, Gaussian process inference and adaptive experimentation, respectively. For experimentation, we apply Bayesian hyperparameter optimization, for optimizing group weights, to weighted group pooling, which couples unsupervised tiered graph autoencoders learning and supervised graph prediction learning for molecular graphs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We find that Ax, BoTorch and GPyTorch together provide a simple-to-use but powerful framework for Bayesian hyperparameter optimization, using Ax's high-level API that constructs and runs a full optimization loop and returns the best hyperparameter configuration.
