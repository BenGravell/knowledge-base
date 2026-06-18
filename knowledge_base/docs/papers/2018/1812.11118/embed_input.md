Reconciling Modern Machine Learning Practice and the Bias-variance Trade-off

Topics include Neural networks, Datasets, Accuracy, Learning, Machine learning.

Breakthroughs in machine learning are rapidly changing science and society, yet our fundamental understanding of this technology has lagged far behind. Indeed, one of the central tenets of the field, the bias-variance trade-off, appears to be at odds with the observed behavior of methods used in the modern machine learning practice. The bias-variance trade-off implies that a model should balance under-fitting and over-fitting: rich enough to express underlying structure in data, simple enough to avoid fitting spurious patterns. However, in the modern practice, very rich models such as neural networks are trained to exactly fit (i.e., interpolate) the data. Classically, such models would be considered over-fit, and yet they often obtain high accuracy on test data. This apparent contradiction has raised questions about the mathematical foundations of machine learning and their relevance to practitioners. In this paper, we reconcile the classical understanding and the modern practice within a unified performance curve.

## Introduction

Machine learning has become key to important applications in science, technology and commerce. The focus of machine learning is on the problem of prediction: given a sample of training examples ${(x_{1},y_{1})},\ldots,{(x_{n},y_{n})}$ from ${\mathbb{R}}^{d} \times {\mathbb{R}}$, we learn a predictor $h_{n}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ that is used to predict the label $y$ of a new point $x$, unseen in training.

The predictor $h_{n}$ is commonly chosen from some function class $\mathcal{H}$, such as neural networks with a certain architecture, using *empirical risk minimization (ERM)* and its variants. In ERM, the predictor is taken to be a function $h \in \mathcal{H}$ that minimizes the *empirical (or training) risk* $\frac{1}{n}{\sum_{i = 1}^{n}{\ell{({h{(x_{i})}},y_{i})}}}$, where $\ell$ is a loss function, such as the squared loss ${\ell{(y^{\prime},y)}} = {({y^{\prime} - y})}^{2}$ for regression or zero-one loss ${\ell{(y^{\prime},y)}} = \mathbb{1}_{\{{y^{\prime} \neq y}\}}$ for classification.

The goal of machine learning is to find $h_{n}$ that performs well on new data, unseen in training. To study performance on new data (known as generalization) we typically assume the training examples are sampled randomly from a probability distribution $P$ over ${\mathbb{R}}^{d} \times {\mathbb{R}}$, and evaluate $h_{n}$ on a new test example $(x,y)$ drawn independently from $P$.

Conventional wisdom in machine learning suggests controlling the capacity of the function class $\mathcal{H}$ based on the bias-variance trade-off by balancing *under-fitting* and *over-fitting* (cf.,

When function class capacity is below the "interpolation threshold", learned predictors exhibit the classical U-shaped curve from Figure 1(a). (In this paper, function class capacity is identified with the number of parameters needed to specify a function within the class.) The bottom of the U is achieved at the sweet spot which balances the fit to the training data and the susceptibility to over-fitting: to the left of the sweet spot, predictors are under-fit, and immediately to the right, predictors are over-fit.
