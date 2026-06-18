Efficient Shapley Performance Attribution for Least-Squares Regression

We consider the performance of a least-squares regression model, as judged by out-of-sample R^. Shapley values give a fair attribution of the performance of a model to its input features, taking into account interdependencies between features. Evaluating the Shapley values exactly requires solving a number of regression problems that is exponential in the number of features, so a Monte Carlo-type approximation is typically used. We focus on the special case of least-squares regression models, where several tricks can be used to compute and evaluate regression models efficiently. These tricks give a substantial speed up, allowing many more Monte Carlo samples to be evaluated, achieving better accuracy. We refer to our method as least-squares Shapley performance attribution (LS-SPA), and describe our open-source implementation.

## Introduction

We consider classic least-squares regression, with $p$ features, judged by an out-of-sample $R^{2}$ metric. A natural question is how much each of the $p$ features contributes to our $R^{2}$ metric; roughly speaking, how valuable is each feature to our least-squares predictor? Except for a special case described below in §2.4, this question seems difficult to answer, since the value of a feature depends on the other features.

Our interest is in attributing the *overall performance* of a least-squares model to the features. A related task is attributing a *specific prediction* of a least-squares model to the features, which is a popular method for so-called explainable AI called SHAP, an acronym for Shapley additive explanations. That is a very different task, discussed in more detail below. In this paper, we consider only performance attribution, and not explaining a specific prediction from a model. We refer to this task as Shapley performance attribution to features.

We used argsort QMC to sample $2^{4}$ batches each with $2^{9}$ permutations. We use the Cholesky reduction presented in §4.4. The correlation matrix $C$ has condition number $4.3 \times 10^{5}$.

The algorithm took 3.5 seconds to complete the initial reduction. LS-SPA ran for 14.6 seconds to reach an error estimate of $8.4 \times 10^{- 3}$, and ran for 113.3 seconds to complete all $2^{13}$ permutations, for a total time of 116.8 seconds to complete, reaching an error estimate of $2.0 \times 10^{- 3}$.

which is negligible compared to the cost of solving the least-squares problems.

For $p$ more than 10 or so, it is impractical to evaluate the lift vector for all $p!$ permutations. Instead, we estimate it as

We can efficiently compute a batched version of the risk estimate on the fly for use as a stopping criterion. For any subset $\Pi$ of permutations, define the sample mean

This performance attribution problem was essentially solved in Lloyd Shapley's 1953 paper "A Value for $n$-person Games" \[\]. He proposed a method to allocate the payoff in a cooperative game to the players, which came to be known as the Shapley values. The Shapley values provide a fair distribution of the total payoff in a game, taking into account the contributions of each player to the coalition....
