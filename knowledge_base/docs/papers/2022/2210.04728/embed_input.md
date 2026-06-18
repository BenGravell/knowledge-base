PyHopper - A Plug-and-Play Hyperparameter Optimization Engine

Topics include PyHopper, Hyperparameter optimization, Black-box optimization, Markov chain Monte Carlo, Optimization software, High-dimensional optimization, Machine learning tooling, Open-source software.

Introduces PyHopper, a lightweight Python platform for hyperparameter optimization centered on a single robust Markov-chain Monte Carlo search algorithm. The paper emphasizes ease of integration, scalability to very high-dimensional hyperparameter spaces, and practical utilities that reduce the setup burden for ML experiments.

Hyperparameter tuning is a fundamental aspect of machine learning research. Setting up the infrastructure for systematic optimization of hyperparameters can take a significant amount of time. Here, we present PyHopper, a black-box optimization platform designed to streamline the hyperparameter tuning workflow of machine learning researchers. PyHopper's goal is to integrate with existing code with minimal effort and run the optimization process with minimal necessary manual oversight. With simplicity as the primary theme, PyHopper is powered by a single robust Markov-chain Monte-Carlo optimization algorithm that scales to millions of dimensions. Compared to existing tuning packages, focusing on a single algorithm frees the user from having to decide between several algorithms and makes PyHopper easily customizable. PyHopper is publicly available under the Apache-2.0 license at

## Introduction

Modern machine learning (ML) research involves a considerable amount of hyperparameter tuning. A hyperparameter is a value that is required to be set for training a machine learning model before the optimization process begins. For instance, the learning rate, i.e., the step size with which an optimization algorithm performs the next iteration towards minimizing a loss function, is a typical hyperparameter. Other examples of hyperparameters include the choice of the optimization algorithm, weight regularization factors, or simply the width and depth of a neural network....

Changes in the hyperparameters drastically affect the performance of a trained ML model. For instance, a learning rate set too high or too low can make the difference between failing or solving a task. Moreover, the relation of the optimization process with respect to the hyperparameters is non-convex and non-differentiable. Consequently, the problem of finding the optimal hyperparameters could be formulated as a black-box optimization problem.

## Conclusion

PyHopper is a customizable, open-source, and plug-and-play hyperparameter optimization engine, that can be integrated with advanced training jobs with minimal effort and low cost, generating competitive models compared to existing well-established packages.

PyHopper's algorithm is flexible and customizable. For example, we can skip phase 1 and directly let the local sampling algorithm improve on a set of hyperparameters the user provides. Such scenarios often occur when the user finds some decently working hyperparameter through a manual search. Moreover, PyHopper allows integrating custom sampling and local perturbation (i.e., mutation) strategies for special types of problems. For instance, the Travelling salesman problem (TSP) is an NP-complete combinatorial optimization problem that concerns finding the shortest roundtrip over a set of cities....

PyHopper helps us maximize resource usage via two key features: First, PyHopper expects the user to set the target runtime of the hyperparameter tuning process. For instance, this allows PyHopper to run overnight (or over the weekend) and finish the next day in the morning, thus fully utilizing our hardware during non-working hours.

### Pruning algorithms
