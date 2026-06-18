Every Model Learned by Gradient Descent Is Approximately a Kernel Machine

Topics include Gradient descent, Deep learning, Learning.

Deep learning's successes are often attributed to its ability to automatically discover new representations of the data, rather than relying on handcrafted features like other learning methods. We show, however, that deep networks learned by the standard gradient descent algorithm are in fact mathematically approximately equivalent to kernel machines, a learning method that simply memorizes the data and uses it directly for prediction via a similarity function (the kernel). This greatly enhances the interpretability of deep network weights, by elucidating that they are effectively a superposition of the training examples. The network architecture incorporates knowledge of the target function into the kernel. This improved understanding should lead to better learning algorithms.

## Introduction

Despite its many successes, deep learning remains poorly understood. In contrast, kernel machines are based on a well-developed mathematical theory, but their empirical performance generally lags behind that of deep networks. The standard algorithm for learning deep networks, and many other models, is gradient descent. Here we show that every model learned by this method, regardless of architecture, is approximately equivalent to a kernel machine with a particular type of kernel. This kernel measures the similarity of the model at two data points in the neighborhood of the path taken by the model parameters during learning....

## Path Kernels

Another consequence of our result is that every probabilistic model learned by gradient descent, including Bayesian networks, is a form of kernel density estimation. The result also implies that the solution of every convex learning problem is a kernel machine, irrespective of the optimization method used, since, being unique, it is necessarily the solution obtained by gradient descent. It is an open question whether the result can be extended to nonconvex models learned by non-gradient-based techniques, including constrained and combinatorial optimization.

The results in this paper suggest a number of research directions. For example, viewing gradient descent as a method for learning path kernel machines may provide new paths for improving it. Conversely, gradient descent is not necessarily the only way to form superpositions of examples that are useful for prediction. The key question is how to optimize the tradeoff between accurately capturing the target function and minimizing the computational cost of storing and matching the examples in the superposition.

where $c{(t)}$ is the path taken by the parameters during gradient descent. Multiplying and dividing by $\int_{c{(t)}}{K_{f,{w{(t)}}}^{g}{(x,x_{i})}{dt}}$:

### Theorem 1

### Remark 5

A kernel machine is a model of the form

where $x$ is the query data point, the sum is over training data points $x_{i}$, $g$ is an optional nonlinearity, the $a_{i}$'s and $b$ are learned parameters, and the kernel $K$ measures the similarity of its arguments. In supervised learning, $a_{i}$ is typically a linear function of $y_{i}^{\ast}$, the known output for $x_{i}$. Kernels may be predefined or learned....
