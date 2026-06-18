Decoupled Weight Decay Regularization

Topics include Gradient descent, Stochastic gradients, Classification, Datasets, Generalization, Optimization, Learning, AdamW.

L_2 regularization and weight decay regularization are equivalent for standard stochastic gradient descent (when rescaled by the learning rate), but as we demonstrate this is not the case for adaptive gradient algorithms, such as Adam. While common implementations of these algorithms employ L_2 regularization (often calling it "weight decay" in what may be misleading due to the inequivalence we expose), we propose a simple modification to recover the original formulation of weight decay regularization by decoupling the weight decay from the optimization steps taken w.r.t. the loss function. We provide empirical evidence that our proposed modification (i) decouples the optimal choice of weight decay factor from the setting of the learning rate for both standard SGD and Adam and (ii) substantially improves Adam's generalization performance, allowing it to compete with SGD with momentum on image classification datasets (on which it was previously typically outperformed by the latter).

## Introduction

Adaptive gradient methods, such as AdaGrad, RMSProp, Adam and most recently AMSGrad have become a default method of choice for training feed-forward and recurrent neural networks. Nevertheless, state-of-the-art results for popular image classification datasets, such as CIFAR-10 and CIFAR-100 Krizhevsky, are still obtained by applying SGD with momentum. Furthermore, Wilson et al. suggested that adaptive gradient methods do not generalize as well as SGD with momentum when tested on a diverse set of deep learning tasks, such as image classification, character-level language modeling and constituency parsing.

: Weight decay is equally effective in both SGD and Adam. For SGD, it is equivalent to L~2~ regularization, while for Adam it is not.

: Adam can substantially benefit from a scheduled learning rate multiplier. The fact that Adam is an adaptive gradient algorithm and as such adapts the learning rate for each parameter does *not* rule out the possibility to substantially improve its performance by using a global learning rate multiplier, scheduled, e.g., by cosine annealing.

The main contribution of this paper is to *improve regularization in Adam by decoupling the weight decay from the gradient-based update*. In a comprehensive analysis, we show that Adam generalizes substantially better with decoupled weight decay than with L~2~ regularization, achieving 15% relative improvement in test error (see Figures 2 and 3); this holds true for various image recognition datasets (CIFAR-10 and ImageNet32x32), training budgets (ranging from 100 to 1800 epochs), and learning rate schedules (fixed, drop-step, and cosine annealing; see Figure 1).

## Conclusion and Future Work

Following suggestions that adaptive gradient methods such as Adam might lead to worse generalization than SGD with momentum, we identified and exposed the inequivalence of L~2~ regularization and weight decay for Adam. We empirically showed that our version of Adam with decoupled weight decay yields substantially better generalization performance than the common implementation of Adam with L~2~ regularization. We also proposed to use warm restarts for Adam to improve its anytime performance.
