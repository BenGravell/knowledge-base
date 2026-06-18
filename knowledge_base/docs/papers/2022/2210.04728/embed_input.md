PyHopper - A Plug-and-Play Hyperparameter Optimization Engine

Topics include PyHopper, Hyperparameter optimization, Black-box optimization, Markov chain Monte Carlo, Optimization software, High-dimensional optimization, Machine learning tooling, Open-source software.

Introduces PyHopper, a lightweight Python platform for hyperparameter optimization centered on a single robust Markov-chain Monte Carlo search algorithm. The paper emphasizes ease of integration, scalability to very high-dimensional hyperparameter spaces, and practical utilities that reduce the setup burden for ML experiments.

Hyperparameter tuning is a fundamental aspect of machine learning research. Setting up the infrastructure for systematic optimization of hyperparameters can take a significant amount of time. Here, we present PyHopper, a black-box optimization platform designed to streamline the hyperparameter tuning workflow of machine learning researchers. PyHopper's goal is to integrate with existing code with minimal effort and run the optimization process with minimal necessary manual oversight. With simplicity as the primary theme, PyHopper is powered by a single robust Markov-chain Monte-Carlo optimization algorithm that scales to millions of dimensions. Compared to existing tuning packages, focusing on a single algorithm frees the user from having to decide between several algorithms and makes PyHopper easily customizable. PyHopper is publicly available under the Apache-2.0 license at

## Introduction

Modern machine learning (ML) research involves a considerable amount of hyperparameter tuning. A hyperparameter is a value that is required to be set for training a machine learning model before the optimization process begins. For instance, the learning rate, i.e., the step size with which an optimization algorithm performs the next iteration towards minimizing a loss function, is a typical hyperparameter. Other examples of hyperparameters include the choice of the optimization algorithm, weight regularization factors, or simply the width and depth of a neural network.

For instance, an HPO algorithm that performs well in low-dimensional problems may struggle to outperform simple baselines in higher-dimensional setups. Similarly, the smoothness and curvature of the objective surface can change drastically between two problem instances, making a one-fits-all solution impossible. Moreover, the design of hyperparameter tuning packages often encounters contradictory specifications. For instance, an ideal package should be extensible, customizable, and rich in features, which, however, may steepen the learning curve and contradict our requirement that the package should be simple and easy to use.

In this work, we introduce Pyopper, a hyperparameter tuning platform tailored to the optimization frameworks we encounterin machine learning research (e.g., training neural networks). In particular, our HPO platform allows us to streamline the hyperparameter tuning procedures and scale to hundreds of tuning tasks with minimal effort.

## Limitations

There cannot be a perfect hyperparameter tuning package, as some features of what makes a good HP tuner might be contradictory. For instance, implementing several different optimization algorithms might be both an advantage and a disadvantage. Instead, each hyperparameter tuning package comes with tradeoffs that were made for specific application areas in mind. The main tradeoff for PyHopper is the focus on a single optimization algorithm.

## Conclusion

PyHopper is a customizable, open-source, and plug-and-play hyperparameter optimization engine, that can be integrated with advanced training jobs with minimal effort and low cost, generating competitive models compared to existing well-established packages.
