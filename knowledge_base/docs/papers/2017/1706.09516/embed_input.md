CatBoost: Unbiased Boosting with Categorical Features

Topics include Datasets, CatBoost, Gradient boosting.

This paper presents the key algorithmic techniques behind CatBoost, a new gradient boosting toolkit. Their combination leads to CatBoost outperforming other publicly available boosting implementations in terms of quality on a variety of datasets. Two critical algorithmic advances introduced in CatBoost are the implementation of ordered boosting, a permutation-driven alternative to the classic algorithm, and an innovative algorithm for processing categorical features. Both techniques were created to fight a prediction shift caused by a special kind of target leakage present in all currently existing implementations of gradient boosting algorithms. In this paper, we provide a detailed analysis of this problem and demonstrate that proposed algorithms solve it effectively, leading to excellent empirical results.

## Introduction

Gradient boosting is a powerful machine-learning technique that achieves state-of-the-art results in a variety of practical tasks. For many years, it has remained the primary method for learning problems with heterogeneous features, noisy data, and complex dependencies: web search, recommendation systems, weather forecasting, and many others. Gradient boosting is essentially a process of constructing an ensemble predictor by performing gradient descent in a functional space. It is backed by solid theoretical results that explain how strong predictors can be built by iteratively combining weaker models (base predictors) in a greedy manner.

We show in this paper that all existing implementations of gradient boosting face the following statistical issue. A prediction model $F$ obtained after several steps of boosting relies on the targets of all training examples. We demonstrate that this actually leads to a shift of the distribution of ${F{(\mathbf{x}_{k})}} \mid \mathbf{x}_{k}$ for a training example $\mathbf{x}_{k}$ from the distribution of ${F{(\mathbf{x})}} \mid \mathbf{x}$ for a test example $\mathbf{x}$. This finally leads to a prediction shift of the learned model. We identify this problem as a special kind of target leakage in Section 4....

## Conclusion

In this paper, we identify and analyze the problem of prediction shifts present in all existing implementations of gradient boosting. We propose a general solution, ordered boosting with ordered TS, which solves the problem. This idea is implemented in CatBoost, which is a new gradient boosting library. Empirical results demonstrate that CatBoost outperforms leading GBDT packages and leads to new state-of-the-art results on common benchmarks.

Here we propose a boosting algorithm which does not suffer from the prediction shift problem described in Section 4.1. Assuming access to an unlimited amount of training data, we can easily construct such an algorithm. At each step of boosting, we sample a new dataset $\mathcal{D}_{t}$ independently and obtain unshifted residuals by applying the current model to new training examples. In practice, however, labeled data is limited. Assume that we learn a model with $I$ trees. To make the residual $r^{I - 1}{(\mathbf{x}_{k},y_{k})}$ unshifted, we need to have $F^{I - 1}$ trained without the example $\mathbf{x}_{k}$....

### Prediction shift
