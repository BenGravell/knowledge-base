Optuna: A Next-generation Hyperparameter Optimization Framework

Topics include Optuna, Hyperparameter optimization, Black-box optimization, Define-by-run, Pruning, Distributed optimization, Machine learning systems.

Introduces Optuna as a define-by-run hyperparameter optimization framework that lets users construct dynamic search spaces in ordinary Python code. The paper emphasizes practical system design: search and pruning algorithms, simple single-machine use, and scalable distributed execution.

The purpose of this study is to introduce new design-criteria for next-generation hyperparameter optimization software. The criteria we propose include define-by-run API that allows users to construct the parameter search space dynamically, efficient implementation of both searching and pruning strategies, and easy-to-setup, versatile architecture that can be deployed for various purposes, ranging from scalable distributed computing to light-weight experiment conducted via interactive interface. In order to prove our point, we will introduce Optuna, an optimization software which is a culmination of our effort in the development of a next generation optimization software. As an optimization software designed with define-by-run principle, Optuna is particularly the first of its kind. We will present the design-techniques that became necessary in the development of the software that meets the above criteria, and demonstrate the power of our new design through experimental results and real world applications. Our software is available under the MIT license.

## Introduction

Hyperparameter search is one of the most cumbersome tasks in machine learning projects. The complexity of deep learning method is growing with its popularity, and the framework of efficient automatic hyperparameter tuning is in higher demand than ever. Hyperparameter optimization softwares such as *Hyperopt*, *Spearmint*, *SMAC*, *Autotune*, and *Vizier* were all developed in order to meet this need.

The choice of the parameter-sampling algorithms varies across frameworks. *Spearmint* and *GPyOpt* use Gaussian Processes, and *Hyperopt* employs *tree-structured Parzen estimator* (TPE). Hutter et al. proposed *SMAC* that uses random forests. Recent frameworks such as *Google Vizier*, *Katib* and *Tune* also support *pruning* algorithms, which monitor the intermediate result of each trial and kills the unpromising trials prematurely in order to speed up the exploration. There is an active research field for the pruning algorithm in hyperparameter optimization. Domhan et al....

## Conclusions

The efficacy of *Optuna* strongly supports our claim that our new design criteria for next generation optimization frameworks are worth adopting in the development of future frameworks. The *define-by-run* principle enables the user to dynamically construct the search space in the way that has never been possible with previous hyperparameter tuning frameworks. Combination of efficient searching and pruning algorithm greatly improves the cost effectiveness of optimization. Finally, scalable and versatile design allows users of various types to deploy the frameworks for a wide variety of purposes....

### Efficient Pruning Algorithm

Figure 4: Another example of Optuna’s objective function. This code simultaneously optimizes neural network architecture (the create_model method) and the hyperparameters for stochastic gradient descent (the create_optimizer method).

*Optuna*'s new design thus significantly reduces the effort required for storage deployment. This new design can be easily incorporated into a container-orchestration system like *Kubernetes* as well. As we verify in the experiment section, the distributed computations conducted with our flexible system-design scales linearly with the number of workers. *Optuna* is also an open source software that can be installed to user's system with one command.
