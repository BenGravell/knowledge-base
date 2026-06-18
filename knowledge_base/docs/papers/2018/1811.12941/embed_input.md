On the Computational Inefficiency of Large Batch Sizes for Stochastic Gradient Descent

Topics include Stochastic gradient descent, Machine learning systems, Machine learning efficiency, Parallel computing, Optimization, Generalization, Neural networks.

Analyzes why increasing the batch size in stochastic gradient training can stop producing proportional wall-clock gains. The paper separates hardware utilization from optimization progress, giving a practical lens for deciding when large-batch training becomes computationally wasteful.

Increasing the mini-batch size for stochastic gradient descent offers significant opportunities to reduce wall-clock training time, but there are a variety of theoretical and systems challenges that impede the widespread success of this technique. We investigate these issues, with an emphasis on time to convergence and total computational cost, through an extensive empirical analysis of network training across several architectures and problem domains, including image classification, image segmentation, and language modeling. Although it is common practice to increase the batch size in order to fully exploit available computational resources, we find a substantially more nuanced picture. Our main finding is that across a wide range of network architectures and problem domains, increasing the batch size beyond a certain point yields no decrease in wall-clock time to convergence for either train or test loss. This batch size is usually substantially below the capacity of current systems....

## Introduction

Mini-batch stochastic gradient descent (SGD) is the dominant optimization method for training deep neural networks (DNNs). In the face of unprecedented growth in dataset size, a large body of work has attempted to scale SGD to train DNN models on increasingly large datasets, while keeping *wall-clock time* manageable. The most common approach to train large models at scale is distributed synchronous mini-batch SGD, which exploits additional computational resources through data parallelism....

Increasing the batch size improves the scaling performance of SGD per epoch, but there are significant challenges in building efficient distributed systems that are able to exploit additional computational resources to use large batch sizes. However, even if we were able to address these systems challenges, there are still more fundamental limitations to this approach. Large batch sizes often negatively impact important performance metrics of interest, including total computational cost (which usually determines monetary cost) and prediction quality.

Recent works also suggest heuristics to decrease the generalization gap, but we find that these heuristics cannot be used to solve the underlying issue of training convergence speed. Moreover, we find that they usually only help decrease the generalization error in a small-to-medium batch size regime. There does not seem to be a simple training heuristic to improve large batch performance in general.

These results suggest that we should not assume that increasing the batch size for larger datasets will keep training times manageable for all problems. Even though it is a natural form of data parallelism for large-scale optimization, alternative forms of parallelism should be explored to utilize all of our data more efficiently.

## Critical Batch Sizes and Diminishing Returns

A mini-batch $\mathcal{B}_{m}$ of size $m < n$ is a collection of $m$ indices randomly drawn from the set $\{ 1,\ldots,n\}$, and we can use it to form an unbiased estimate of the gradient at iteration $k$, as well as the corresponding SGD update:

In Figure 1, we show contour plots of training loss as a function of both the batch size and the number of training iterations of on CIFAR-10, an LSTM on WikiText-2, and DRN-D-22 on Cityscapes. Consider, for example, the contour plot for trained on CIFAR-10....
