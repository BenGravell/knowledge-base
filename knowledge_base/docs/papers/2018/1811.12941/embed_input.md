On the Computational Inefficiency of Large Batch Sizes for Stochastic Gradient Descent

Topics include Stochastic gradient descent, Machine learning systems, Machine learning efficiency, Parallel computing, Optimization, Generalization, Neural networks.

Analyzes why increasing the batch size in stochastic gradient training can stop producing proportional wall-clock gains. The paper separates hardware utilization from optimization progress, giving a practical lens for deciding when large-batch training becomes computationally wasteful.

Increasing the mini-batch size for stochastic gradient descent offers significant opportunities to reduce wall-clock training time, but there are a variety of theoretical and systems challenges that impede the widespread success of this technique. We investigate these issues, with an emphasis on time to convergence and total computational cost, through an extensive empirical analysis of network training across several architectures and problem domains, including image classification, image segmentation, and language modeling. Although it is common practice to increase the batch size in order to fully exploit available computational resources, we find a substantially more nuanced picture. Our main finding is that across a wide range of network architectures and problem domains, increasing the batch size beyond a certain point yields no decrease in wall-clock time to convergence for either train or test loss. This batch size is usually substantially below the capacity of current systems.

## Introduction

Mini-batch stochastic gradient descent (SGD) is the dominant optimization method for training deep neural networks (DNNs). In the face of unprecedented growth in dataset size, a large body of work has attempted to scale SGD to train DNN models on increasingly large datasets, while keeping *wall-clock time* manageable. The most common approach to train large models at scale is distributed synchronous mini-batch SGD, which exploits additional computational resources through data parallelism.

In this paper, we will measure the total computational cost as the number of training iterations times the work done per iteration---in order to simplify measurements, we use the number of training iterations as a proxy for the wall-clock time. We do this because the implementation of parallel algorithms depends on software and hardware choices, and our goal is to draw more general conclusions about the performance of SGD-based methods.

Diminishing returns: there is a larger regime of batch sizes that results in sublinear gains in convergence speed---in this regime, increasing the batch size can improve wall-clock training time at the expense of greater total computational cost;

## Conclusion

By experimenting across a wide range of network architectures and problem domains, we find that, after a certain point, increasing the batch size fails to decrease wall-clock time to convergence and results in low computational efficiency, even assuming perfect parallelism. The critical batch size after which these returns diminish tends to be small relative to existing system capabilities. These trends present impediments to progress in developing effective machine learning systems that are capable of handling growing data demands.

Recent works also suggest heuristics to decrease the generalization gap, but we find that these heuristics cannot be used to solve the underlying issue of training convergence speed. Moreover, we find that they usually only help decrease the generalization error in a small-to-medium batch size regime. There does not seem to be a simple training heuristic to improve large batch performance in general.
