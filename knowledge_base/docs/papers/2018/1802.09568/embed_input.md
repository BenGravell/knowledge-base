Shampoo: Preconditioned Stochastic Tensor Optimization

Preconditioned gradient methods are among the most general and powerful tools in optimization. However, preconditioning requires storing and manipulating prohibitively large matrices. We describe and analyze a new structure-aware preconditioning algorithm, called Shampoo, for stochastic optimization over tensor spaces. Shampoo maintains a set of preconditioning matrices, each of which operates on a single dimension, contracting over the remaining dimensions. We establish convergence guarantees in the stochastic convex setting, the proof of which builds upon matrix trace inequalities. Our experiments with state-of-the-art deep learning models show that Shampoo is capable of converging considerably faster than commonly used optimizers. Although it involves a more complex update rule, Shampoo's runtime per step is comparable to that of simple gradient methods such as SGD, AdaGrad, and Adam.

## Introduction

Over the last decade, stochastic first-order optimization methods have emerged as the canonical tools for training large-scale machine learning models. These methods are particularly appealing due to their wide applicability and their low runtime and memory costs.

A potentially more powerful family of algorithms consists of *preconditioned* gradient methods. Preconditioning methods maintain a matrix, termed a preconditioner, which is used to transform (i.e., premultiply) the gradient vector before it is used to take a step. Classic algorithms in this family include Newton's method, which employs the local Hessian as a preconditioner, as well as a plethora of quasi-Newton methods (e.g., ) that can be used whenever second-order information is unavailable or too expensive to compute....

Our next experiment was on the LM1B benchmark for statistical language modeling. We used an Attention model with 9.8M trainable parameters from. This model has a succession of fully connected-layers, with corresponding tensors of order at most $2$, the largest of which is of dimension $$. In this experiment, we simply used the default learning rate of $\eta = 1.0$ for Shampoo. For the other algorithms we explored various different settings of the learning rate. The graph for the test perplexity is shown in Fig. 4.

Figure 4: Test log-perplexity of an Attention model of Vaswani et al..

which holds since given a vector $x$ we can write $\alpha_{i} = {x^{\mathsf{T}}w_{i}}$, and use the convexity of $\alpha\mapsto\alpha^{2}$ to obtain

### Matrix inequalities

The following definitions are used throughout the section.

While preconditioned methods often lead to improved convergence properties, the dimensionality of typical problems in machine learning prohibits out-of-the-box use of full-matrix preconditioning. To mitigate this issue, specialized variants have been devised in which the full preconditioner is replaced with a diagonal approximation, a sketched version, or various estimations thereof....

In this paper, we take an alternative approach to preconditioning and describe an efficient and practical apparatus that exploits the structure of the parameter space. Our approach is motivated by the observation that in numerous machine learning applications, the parameter space entertains a more complex structure than a monolithic vector in Euclidean space....
