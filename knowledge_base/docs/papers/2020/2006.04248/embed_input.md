Learning Convex Optimization Models

A convex optimization model predicts an output from an input by solving a convex optimization problem. The class of convex optimization models is large, and includes as special cases many well-known models like linear and logistic regression. We propose a heuristic for learning the parameters in a convex optimization model given a dataset of input-output pairs, using recently developed methods for differentiating the solution of a convex optimization problem with respect to its parameters. We describe three general classes of convex optimization models, maximum a posteriori (MAP) models, utility maximization models, and agent models, and present a numerical experiment for each.

## Introduction

### Convex optimization models

We consider the problem of learning to predict outputs $y \in \mathcal{Y}$ from inputs $x \in \mathcal{X}$, given a set of input-output pairs $(x^{i},y^{i})$, $i = {1,\ldots,N}$, with ${(x^{i},y^{i})} \in {\mathcal{X} \times \mathcal{Y}}$. We assume that $\mathcal{Y} \subseteq \text{R}^{m}$ is a convex set, but make no assumptions on $\mathcal{X}$. In this paper, we specifically consider models $\phi:{\mathcal{X}\rightarrow\mathcal{Y}}$ that predict the output $y$ by solving a convex optimization problem that depends on the input $x$. We call such models *convex optimization models*....

for $i = {1,\ldots,1000}$. We generate $1000$ validation points in the same way.

We use the mean-squared loss for the loss function $L$, and train for 20 iterations. As a baseline, we compare against a two-layer feedforward ReLU network with hidden layer dimension $n$, and with output clamped to have absolute value no greater than $0.5$. The results are displayed in figure 4. The ReLU network achieves a validation loss of 0.071. The trained convex optimization model achieves a validation loss of 0.066, which is close to the validation loss of the underlying model. Additionally, the convex optimization model nearly recovers the true weights.

A Markov random field (MRF) is an undirected graphical model that describes the joint distribution of a set of random variables, which are represented by the nodes in the graph. An MRF associates parametrized potential functions to cliques of nodes, and the joint distribution it describes is proportional to the product of these potential functions. MRFs are commonly used for structured prediction, but learning their parameters is in general difficult \[24, §8.3\]. When the potential functions are log-concave, however, we can fit the parameters using the methods described in this paper.

These very basic examples can be made more interesting by constraining the outputs $y$ to lie in a convex subset $C$ of $\mathcal{Y}$, using a density of the form

where $U_{i}{(y_{i};\theta)}$ is the utility of allocating $y_{i}$ of the resource to the $i$th agent or task. In this case the entries of the decision $y$ are coupled by budget constraints. A simple example for separable utility is exponential utility ${U_{i}{(y_{i};\theta)}} = {- {{\exp{({\theta_{i}y_{i}})}}/\theta_{i}}}$.
