Distributionally Robust Logistic Regression

This paper proposes a distributionally robust approach to logistic regression. We use the Wasserstein distance to construct a ball in the space of probability distributions centered at the uniform distribution on the training samples. If the radius of this ball is chosen judiciously, we can guarantee that it contains the unknown data-generating distribution with high confidence. We then formulate a distributionally robust logistic regression model that minimizes a worst-case expected logloss function, where the worst case is taken over all distributions in the Wasserstein ball. We prove that this optimization problem admits a tractable reformulation and encapsulates the classical as well as the popular regularized logistic regression problems as special cases. We further propose a distributionally robust approach based on Wasserstein balls to compute upper and lower confidence bounds on the misclassification probability of the resulting classifier. These bounds are given by the optimal values of two highly tractable linear programs. We validate our theoretical out-of-sample guarantees through simulated and empirical experiments.

## Introduction

Logistic regression is one of the most frequently used classification methods applied. Its objective is to establish a probabilistic relationship between a continuous feature vector and a binary explanatory variable. However, in spite of its overwhelming success in machine learning, data analytics and medicine etc., logistic regression models can display a poor out-of-sample performance if training data is sparse. In this case modelers often resort to ad hoc regularization techniques in order to combat overfitting effects.

## Logistic Regression

Let $x \in {\mathbb{R}}^{n}$ denote a feature vector and $y \in {\{{- 1},{+ 1}\}}$ the associated binary label to be predicted. In logistic regression, the conditional distribution of $y$ given $x$ is modeled as

where the weight vector $\beta \in {\mathbb{R}}^{n}$ constitutes an unknown regression parameter. Suppose that $N$ training samples ${\{{({\hat{x}}_{i},{\hat{y}}_{i})}\}}_{i = 1}^{N}$ have been observed. Then, the maximum likelihood estimator of classical logistic regression is found by solving the geometric program

whose objective function is given by the sample average of the *logloss function* ${{l_{\beta}{(x,y)}} = {\log{({1 + {\exp{({- {y{\langle\beta,x\rangle}}})}}})}}}.$ It has been observed, however, that the resulting maximum likelihood estimator may display a poor out-of-sample performance. Indeed, it is well documented that minimizing the average logloss function leads to overfitting and weak classification performance feng2014robust; plan2013robust. In order to overcome this deficiency, it has been proposed to modify the objective function of problem ding2013t; liu2004robit; rousseeuw2003robustness.
