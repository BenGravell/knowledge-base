Minimal Variance Sampling in Stochastic Gradient Boosting

Topics include Stochastic gradients, Accuracy, Generalization, Optimization, Learning, Sampling, MVS, SGB, Minimal variance sampling, Gradient boosting, Decision trees, Machine learning.

Stochastic Gradient Boosting (SGB) is a widely used approach to regularization of boosting models based on decision trees. It was shown that, in many cases, random sampling at each iteration can lead to better generalization performance of the model and can also decrease the learning time. Different sampling approaches were proposed, where probabilities are not uniform, and it is not currently clear which approach is the most effective. In this paper, we formulate the problem of randomization in SGB in terms of optimization of sampling probabilities to maximize the estimation accuracy of split scoring used to train decision trees. This optimization problem has a closed-form nearly optimal solution, and it leads to a new sampling technique, which we call Minimal Variance Sampling (MVS). The method both decreases the number of examples needed for each iteration of boosting and increases the quality of the model significantly as compared to the state-of-the art sampling methods....

## Introduction

Gradient boosted decision trees (GBDT) is one of the most popular machine learning algorithms as it provides high-quality models in a large number of machine learning problems containing heterogeneous features, noisy data, and complex dependencies. There are many fields where gradient boosting achieves state-of-the-art results, e.g., search engines, recommendation systems, and other applications.

One problem of GBDT is the computational cost of the learning process. GBDT may be described as an iterative process of constructing decision tree models, each of which estimates negative gradients of examples' errors. At each step, GBDT greedily builds a tree. GBDT scores every possible feature split and chooses the best one, which requires computational time proportional to the number of data instances. Since most GBDT models consist of an ensemble of many trees, as the number of examples grows, more learning time is required, what imposes restrictions on using GBDT models for large industry datasets.

## Conclusion

In this paper, we addressed a surprisingly understudied problem of weighted sampling in GBDT. We proposed a novel technique, which directly maximizes the accuracy of split scoring, a core step of the tree construction procedure. We rigorously formulated this goal as an optimization problem and derived a near-optimal closed-form solution. This solution led to a novel sampling technique MVS. We provided our work with necessary theoretical statements and empirical observations that show the superiority of MVS over the well-known state-of-the-art approaches to data sampling in SGB....

Note that we do not have the values of $c_{l}$ for all possible leaves of all possible candidate splits in advance, when we perform sampling procedure. A possible approach to Problem 8 is to substitute all $c_{l}^{2}$ by a universal constant value, which is a parameter of sampling algorithm. Also, note that $Var{(x_{l})}$ is $\sum\limits_{i \in l}{\frac{1}{p_{i}}g_{i}^{2}}$ and $Var{(y_{l})}$ is $\sum\limits_{i \in l}{\frac{1}{p_{i}}h_{i}^{2}}$ up to constants that do not depend on the sampling procedure. In this way, we come to the following form of Problem 8:

## Minimal Variance Sampling

Now we are ready to derive the MVS algorithm from Theorem 2, which can be directly applied to general scheme of Stochastic Gradient Boosting....
