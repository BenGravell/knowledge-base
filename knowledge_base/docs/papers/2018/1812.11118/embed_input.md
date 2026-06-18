Reconciling Modern Machine Learning Practice and the Bias-variance Trade-off

Topics include Neural networks, Datasets, Accuracy, Learning, Machine learning.

Breakthroughs in machine learning are rapidly changing science and society, yet our fundamental understanding of this technology has lagged far behind. Indeed, one of the central tenets of the field, the bias-variance trade-off, appears to be at odds with the observed behavior of methods used in the modern machine learning practice. The bias-variance trade-off implies that a model should balance under-fitting and over-fitting: rich enough to express underlying structure in data, simple enough to avoid fitting spurious patterns. However, in the modern practice, very rich models such as neural networks are trained to exactly fit (i.e., interpolate) the data. Classically, such models would be considered over-fit, and yet they often obtain high accuracy on test data. This apparent contradiction has raised questions about the mathematical foundations of machine learning and their relevance to practitioners. In this paper, we reconcile the classical understanding and the modern practice within a unified performance curve....

## Introduction

Machine learning has become key to important applications in science, technology and commerce. The focus of machine learning is on the problem of prediction: given a sample of training examples ${(x_{1},y_{1})},\ldots,{(x_{n},y_{n})}$ from ${\mathbb{R}}^{d} \times {\mathbb{R}}$, we learn a predictor $h_{n}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ that is used to predict the label $y$ of a new point $x$, unseen in training.

The predictor $h_{n}$ is commonly chosen from some function class $\mathcal{H}$, such as neural networks with a certain architecture, using *empirical risk minimization (ERM)* and its variants. In ERM, the predictor is taken to be a function $h \in \mathcal{H}$ that minimizes the *empirical (or training) risk* $\frac{1}{n}{\sum_{i = 1}^{n}{\ell{({h{(x_{i})}},y_{i})}}}$, where $\ell$ is a loss function, such as the squared loss ${\ell{(y^{\prime},y)}} = {({y^{\prime} - y})}^{2}$ for regression or zero-one loss ${\ell{(y^{\prime},y)}} = \mathbb{1}_{\{{y^{\prime} \neq y}\}}$ for classification.

### Outlook

The classical U-shaped bias-variance trade-off curve has shaped our view of model selection and directed applications of learning algorithms in practice. The understanding of model performance developed in this work delineates the limits of classical analyses and opens new lines of enquiry to study and compare computational, statistical, and mathematical properties of the classical and modern regimes in machine learning. We hope that this perspective, in turn, will help practitioners choose models and algorithms for optimal performance.

Finally, in Appendix C.4, we also describe a simple synthetic model, which can be regarded as a one-dimensional version of the RFF model, where we observe the same double descent behavior.

We first consider a popular class of non-linear parametric models called *Random Fourier Features* (*RFF*), which can be viewed as a class of two-layer neural networks with fixed weights in the first layer. The RFF model family $\mathcal{H}_{N}$ with $N$ (complex-valued) parameters consists of functions $h:{{\mathbb{R}}^{d}\rightarrow{\mathbb{C}}}$ of the form

Does the double descent risk curve manifest with other prediction methods besides neural networks? We give empirical evidence that the families of functions explored by boosting with decision trees and Random Forests also show similar...
