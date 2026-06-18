Code Generation for Solving and Differentiating through Convex Optimization Problems

We introduce custom code generation for parametrized convex optimization problems that supports evaluating the derivative of the solution with respect to the parameters, i.e., differentiating through the optimization problem. We extend the open source code generator CVXPYgen, which itself extends CVXPY, a Python-embedded domain-specific language with a natural syntax for specifying convex optimization problems, following their mathematical description. Our extension of CVXPYgen adds a custom C implementation to differentiate the solution of a convex optimization problem with respect to its parameters, together with a Python wrapper for prototyping and desktop (non-embedded) applications. We give three representative application examples: Tuning hyper-parameters in machine learning; choosing the parameters in an approximate dynamic programming (ADP) controller; and adjusting the parameters in an optimization based financial trading engine via back-testing, i.e., simulation on historical data....

## Introduction

A convex optimization problem, parametrized by $\theta \in \Theta \subseteq \text{R}^{d}$, can be written as

where $x \in \text{R}^{n}$ is the optimization variable, $f_{0}$ is the objective function to be minimized, which is convex in $x$, and $f_{1},\ldots,f_{m}$ are inequality constraint functions that are convex in $x$ \[\]. The parameter $\theta$ specifies data that can change, but is constant and given (or chosen) when we solve an instance of the problem. We refer to the parametrized problem as a *problem family*; when we specify a fixed value of $\theta \in \Theta$, we refer to it as a *problem instance*. We let $x^{\star}$ denote an optimal point for problem, assuming it exists....

## Conclusions

We have added new functionality to the code generator CVXPYgen for differentiating through parametrized convex optimization problems. Users can model their problem in CVXPY with instructions close to the math, and create an efficient implementation of the gradient computation in C, by simply setting an additional keyword argument of the CVXPYgen code generation method. Our numerical experiments show that the gradient computations are sped up by around one order of magnitude for typical use cases.

where $\ell:{{\mathcal{D} \times \text{R}^{n} \times \Omega}\rightarrow\text{R}}$ is the training loss function and $r:{{\text{R}^{n} \times \Omega}\rightarrow\text{R}}$ is the regularizer. While the entries of $\beta$ are oftentimes referred to as *model parameters* in the machine learning literature, we call them *weights* to make clear that they enter the above optimization problem as variables (and not as parameters of the optimization problem). Both $\ell$ and $r$ are parametrized by the design $\omega$....

### Low-rank updates to factorization of linear system

We take $m = 100$ data points, $n = 20$ features, and $J = 10$ CV folds. For every fold, we reserve ${m/J} = 10$ data points for validation and use the other $90$ data points for training. We generate the features ${\overline{z}}_{i}$ without outliers by sampling from the Gaussian $\mathcal{N}{}$. Then, we sample $\overline{\beta} \sim {\mathcal{N}{(0,I)}}$ and set noisy labels $y_{i} = {{{\overline{z}}_{i}^{T}\overline{\beta}} + \xi_{i}}$ with $\xi_{i} \sim {\mathcal{N}{(0,0.01)}}$. Afterwards, we simulate feature outliers due to, e.g., data capturing errors....
