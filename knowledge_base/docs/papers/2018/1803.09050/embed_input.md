Learning to Reweight Examples for Robust Deep Learning

Deep neural networks have been shown to be very powerful modeling tools for many supervised learning tasks involving complex input patterns. However, they can also easily overfit to training set biases and label noises. In addition to various regularizers, example reweighting algorithms are popular solutions to these problems, but they require careful tuning of additional hyperparameters, such as example mining schedules and regularization hyperparameters. In contrast to past reweighting methods, which typically consist of functions of the cost value of each example, in this work we propose a novel meta-learning algorithm that learns to assign weights to training examples based on their gradient directions. To determine the example weights, our method performs a meta gradient descent step on the current mini-batch example weights (which are initialized from zero) to minimize the loss on a clean unbiased validation set....

## Introduction

Deep neural networks (DNNs) have been widely used for machine learning applications due to their powerful capacity for modeling complex input patterns. Despite their success, it has been shown that DNNs are prone to training set biases, i.e. the training set is drawn from a joint distribution $p{(x,y)}$ that is different from the distribution $p{(x^{v},y^{v})}$ of the evaluation set. This distribution mismatch could have many different forms. Class imbalance in the training set is a very common example....

Another popular type of training set bias is label noise. To train a reasonable supervised deep model, we ideally need a large dataset with high-quality labels, which require many passes of expensive human quality assurance (QA). Although coarse labels are cheap and of high availability, the presence of noise will hurt the model performance, e.g. Zhang et al. has shown that a standard CNN can fit any ratio of label flipping noise in the training set and eventually leads to poor generalization performance.

## Conclusion

In this work, we propose an online meta-learning algorithm for reweighting training examples and training more robust deep learning models. While various types of training set biases exist and manually designed reweighting objectives have their own bias, our automatic reweighting algorithm shows superior performance dealing with class imbalance, noisy labels, and both. Our method can be directly applied to any deep learning architecture and is expected to train end-to-end without any additional hyperparameter search....

### Theorem 2

Detailed derivations can be found in Appendix A. Eq. 12 suggests that the meta-gradient on $\epsilon$ is composed of the sum of the products of two terms: $z^{\top}z^{v}$ and $g^{\top}g^{v}$. The first dot product computes the similarity between the training and validation inputs to the layer, while the second computes the similarity between the training and validation gradient directions....

MentorNet, proposed by Jiang et al., is an RNN-based meta-learning model that takes in a sequence of loss values and outputs the example weights. We compare numbers reported in their paper with a base model that achieves similar test accuracy under 0% noise.

Training set biases and misspecification can sometimes be addressed with dataset resampling, i.e....
