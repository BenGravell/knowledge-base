## Introduction

Despite its many successes, deep learning remains poorly understood. In contrast, kernel machines are based on a well-developed mathematical theory, but their empirical performance generally lags behind that of deep networks. The standard algorithm for learning deep networks, and many other models, is gradient descent. Here we show that every model learned by this method, regardless of architecture, is approximately equivalent to a kernel machine with a particular type of kernel. This kernel measures the similarity of the model at two data points in the neighborhood of the path taken by the model parameters during learning. Kernel machines store a subset of the training data points and match them to the query using the kernel. Deep network weights can thus be seen as a superposition of the training data points in the kernel's feature space, enabling their efficient storage and matching. This contrasts with the standard view of deep learning as a method for discovering representations from data, with the attendant lack of interpretability. Our result also has significant implications for boosting algorithms, probabilistic graphical models, and convex optimization.

## Path Kernels

A kernel machine is a model of the form

where $x$ is the query data point, the sum is over training data points $x_{i}$, $g$ is an optional nonlinearity, the $a_{i}$'s and $b$ are learned parameters, and the kernel $K$ measures the similarity of its arguments. In supervised learning, $a_{i}$ is typically a linear function of $y_{i}^{\ast}$, the known output for $x_{i}$. Kernels may be predefined or learned. Kernel machines, also known as support vector machines, are one of the most developed and widely used machine learning methods. In the last decade, however, they have been eclipsed by deep networks, also known as neural networks and multilayer perceptrons, which are composed of multiple layers of nonlinear functions. Kernel machines can be viewed as neural networks with one hidden layer, with the kernel as the nonlinearity. For example, a Gaussian kernel machine is a radial basis function network. But a deep network would seem to be irreducible to a kernel machine, since it can represent some functions exponentially more compactly than a shallow one.

Whether a representable function is actually learned, however, depends on the learning algorithm. Most deep networks, and indeed most machine learning models, are trained using variants of gradient descent. Given an initial parameter vector $w_{0}$ and a loss function $L = {\sum_{i}{L{(y_{i}^{\ast},y_{i})}}}$, gradient descent repeatedly modifies the model's parameters $w$ by subtracting the loss's gradient from them, scaled by the learning rate $\epsilon$:

The process terminates when the gradient is zero and the loss is therefore at an optimum (or saddle point). Remarkably, we have found that learning by gradient descent is a strong enough constraint that the end result is guaranteed to be approximately a kernel machine, regardless of the number of layers or other architectural features of the model.

Specifically, the kernel machines that result from gradient descent use what we term a path kernel. If we take the learning rate to be infinitesimally small, the path kernel between two data points is simply the integral of the dot product of the model's gradients at the two points over the path taken by the parameters during gradient descent:

where $c{(t)}$ is the path. Intuitively, the path kernel measures how similarly the model at the two data points varies during learning. The more similar the variation for $x$ and $x^{\prime}$, the higher the weight of $x^{\prime}$ in predicting $y$. Fig. 1 illustrates this graphically.

Figure 1: How the path kernel measures similarity between examples. In this two-dimensional illustration, as the weights follow a path on the plane during training, the model’s gradients (vectors on the weight plane) for x, x1 and x2 vary along it. The kernel K (x,x1) is the integral of the dot product of the gradients ∇wy (x) and ∇wy (x1) over the path, and similarly for K (x,x2). Because on average over the weight path ∇wy (x) ⋅ ∇wy (x1) is greater than ∇wy (x) ⋅ ∇wy (x2), y1 has more influence than y2 in predicting y, all else being equal.

Our result builds on the concept of neural tangent kernel, recently introduced to analyze the behavior of deep networks. The neural tangent kernel is the integrand of the path kernel when the model is a multilayer perceptron. Because of this, and since a sum of positive definite kernels is also a positive definite kernel, the known conditions for positive definiteness of neural tangent kernels extend to path kernels. A positive definite kernel is equivalent to a dot product in a derived feature space, which greatly simplifies its analysis.

We now present our main result. For simplicity, in the derivations below we assume that $y$ is a (real-valued) scalar, but it can be made a vector with only minor changes. The data points $x_{i}$ can be arbitrary structures.

### Definition 1

The tangent kernel associated with function $f_{w}{(x)}$ and parameter vector $v$ is\
${K_{f,v}^{g}{(x,x^{\prime})}} = {{{{\nabla_{w}f_{w}}{(x)}} \cdot {\nabla_{w}f_{w}}}{(x^{\prime})}}$, with the gradients taken at $v$.

### Definition 2

The path kernel associated with function $f_{w}{(x)}$ and curve $c{(t)}$ in parameter space is ${K_{f,c}^{p}{(x,x^{\prime})}} = {\int_{c{(t)}}{K_{f,{w{(t)}}}^{g}{(x,x^{\prime})}{dt}}}$.

### Theorem 1

Suppose the model $y = {f_{w}{(x)}}$, with $f$ a differentiable function of $w$, is learned from a training set ${\{{(x_{i},y_{i}^{\ast})}\}}_{i = 1}^{m}$ by gradient descent with differentiable loss function $L = {\sum_{i}{L{(y_{i}^{\ast},y_{i})}}}$ and learning rate $\epsilon$. Then

where $K{(x,x_{i})}$ is the path kernel associated with $f_{w}{(x)}$ and the path taken by the parameters during gradient descent, $a_{i}$ is the average $- {\partial{L/{\partial y_{i}}}}$ along the path weighted by the corresponding tangent kernel, and $b$ is the initial model.

Proof In the $\epsilon\rightarrow 0$ limit, the gradient descent equation, which can also be written as

where $L$ is the loss function, becomes the differential equation

(This is known as a gradient flow.) Then for any differentiable function of the weights $y$,

where $d$ is the number of parameters. Replacing ${{dw_{j}}/d}t$ by its gradient descent expression:

Applying the additivity of the loss and the chain rule of differentiation:

Let ${L^{\prime}{(y_{i}^{\ast},y_{i})}} = {\partial{L/{\partial y_{i}}}}$, the loss derivative for the $i$th output. Applying this and Definition 1:

Let $y_{0}$ be the initial model, prior to gradient descent. Then for the final model $y$:

where $c{(t)}$ is the path taken by the parameters during gradient descent. Multiplying and dividing by $\int_{c{(t)}}{K_{f,{w{(t)}}}^{g}{(x,x_{i})}{dt}}$:

Let ${\overline{L^{\prime}}{(y_{i}^{\ast},y_{i})}} = {\int_{c{(t)}}{{K_{f,{w{(t)}}}^{g}{(x,x_{i})}L^{\prime}{(y_{i}^{\ast},y_{i})}{dt}}/{\int_{c{(t)}}{K_{f,{w{(t)}}}^{g}{(x,x_{i})}{dt}}}}}$, the average loss derivative weighted by similarity to $x$. Applying this and Definition 2:

### Remark 1

This differs from typical kernel machines in that the $a_{i}$'s and $b$ depend on $x$. Nevertheless, the $a_{i}$'s play a role similar to the example weights in ordinary SVMs and the perceptron algorithm: examples that the loss is more sensitive to during learning have a higher weight. $b$ is simply the prior model, and the final model is thus the sum of the prior model and the model learned by gradient descent, with the query point entering the latter only through kernels. Since Theorem 1 applies to every $y_{i}$ as a query throughout gradient descent, the training data points also enter the model only through kernels (initial model aside).

### Remark 2

Theorem 1 can equally well be proved using the loss-weighted path kernel $K_{f,c,L}^{lp} = {\int_{c{(t)}}{L^{\prime}{(y_{i}^{\ast},y_{i})}K_{f,{w{(t)}}}^{g}{(x,x_{i})}{dt}}}$, in which case $a_{i} = {- 1}$ for all $i$.

### Remark 3

In least-squares regression, ${L^{\prime}{(y_{i}^{\ast},y_{i})}} = {y_{i} - y_{i}^{\ast}}$. When learning a classifier by minimizing cross-entropy, the standard practice in deep learning, the function to be estimated is the conditional probability of the class, $p_{i}$, the loss is $- {\sum_{i = 1}^{m}{\ln p_{i}}}$, and the loss derivative for the $i$th output is $- {1/p_{i}}$. Similar expressions hold for modeling a joint distribution by minimizing negative log likelihood, with $p_{i}$ as the probability of the data point.

### Remark 4

Adding a regularization term $R{(w)}$ to the loss function simply adds\
$- {\int_{c{(t)}}{\sum_{j = 1}^{d}{{({\partial{y/{\partial w_{j}}}})}{({\partial{R/{\partial w_{j}}}})}}}}$ to $b$.

### Remark 5

The proof above is for batch gradient descent, which uses all training data points at each step. To extend it to stochastic gradient descent, which uses a subsample, it suffices to multiply each term in the summation over data points by an indicator function $I_{i}{(t)}$ that is 1 if the $i$th data point is included in the subsample at time $t$ and 0 otherwise. The only change this causes in the result is that the path kernel and average loss derivative for a data point are now stochastic integrals. Based on previous results, Theorem 1 or a similar result seems likely to also apply to further variants of gradient descent, but proving this remains an open problem.

For linear models, the path kernel reduces to the dot product of the data points. It is well known that a single-layer perceptron is a kernel machine, with the dot product as the kernel. Our result can be viewed as a generalization of this to multilayer perceptrons and other models. It is also related to Lippmann et al.'s proof that Hopfield networks, a predecessor of many current deep architectures, are equivalent to the nearest-neighbor algorithm, a predecessor of kernel machines, with Hamming distance as the comparison function.

The result assumes that the learning rate is sufficiently small for the trajectory of the weights during gradient descent to be well approximated by a smooth curve. This is standard in the analysis of gradient descent, and is also generally a good approximation in practice, since the learning rate has to be quite small in order to avoid divergence (e.g., $\epsilon = 10^{- 3}$). Nevertheless, it remains an open question to what extent models learned by gradient descent can still be approximated by kernel machines outside of this regime.

## Discussion

A notable disadvantage of deep networks is their lack of interpretability. Knowing that they are effectively path kernel machines greatly ameliorates this. In particular, the weights of a deep network have a straightforward interpretation as a superposition of the training examples in gradient space, where each example is represented by the corresponding gradient of the model. Fig. 2 illustrates this. One well-studied approach to interpreting the output of deep networks involves looking for training instances that are close to the query in Euclidean or some other simple space. Path kernels tell us what the exact space for these comparisons should be, and how it relates to the model's predictions.

Figure 2: Deep network weights as superpositions of training examples. Applying the learned model to a query example is equivalent to simultaneously matching the query with each stored example using the path kernel and outputting a weighted sum of the results.

Experimentally, deep networks and kernel machines often perform more similarly than would be expected based on their mathematical formulation. Even when they generalize well, deep networks often appear to memorize and replay whole training instances. The fact that deep networks are in fact kernel machines helps explain both of these observations. It also sheds light on the surprising brittleness of deep models, whose performance can degrade rapidly as the query point moves away from the nearest training instance, since this is what is expected of kernel estimators in high-dimensional spaces.

Perhaps the most significant implication of our result for deep learning is that it casts doubt on the common view that it works by automatically discovering new representations of the data, in contrast with other machine learning methods, which rely on predefined features. As it turns out, deep learning also relies on such features, namely the gradients of a predefined function, and uses them for prediction via dot products in feature space, like other kernel machines. All that gradient descent does is select features from this space for use in the kernel. If gradient descent is limited in its ability to learn representations, better methods for this purpose are a key research direction. Current nonlinear alternatives include predicate invention and latent variable discovery in graphical models. Techniques like structure mapping, crossover and predictive coding may also be relevant. Ultimately, however, we may need entirely new approaches to solve this crucial but extremely difficult problem.

Our result also has significant consequences on the kernel machine side. Path kernels provide a new and very flexible way to incorporate knowledge of the target function into the kernel. Previously, it was only possible to do so in a weak sense, via generic notions of what makes two data points similar. The extensive knowledge that has been encoded into deep architectures by applied researchers, and is crucial to the success of deep learning, can now be ported directly to kernel machines. For example, kernels with translation invariance or selective attention are directly obtainable from the architecture of, respectively, convolutional neural networks or transformers.

A key property of path kernels is that they combat the curse of dimensionality by incorporating derivatives into the kernel: two data points are similar if the candidate function's derivatives at them are similar, rather than if they are close in the input space. This can greatly improve kernel machines' ability to approximate highly variable functions. It also means that points that are far in Euclidean space can be close in gradient space, potentially improving the ability to model complex functions. (For example, the maxima of a sine wave are all close in gradient space, even though they can be arbitrarily far apart in the input space.)

Most significantly, however, learning path kernel machines via gradient descent largely overcomes the scalability bottlenecks that have long limited the applicability of kernel methods to large data sets. Computing and storing the Gram matrix at learning time, with its quadratic cost in the number of examples, is no longer required. (The Gram matrix is the matrix of applications of the kernel to all pairs of training examples.) Separately storing and matching (a subset of) the training examples at query time is also no longer necessary, since they are effectively all stored and matched simultaneously via their superposition in the model parameters. The storage space and matching time are independent of the number of examples. (Interestingly, superposition has been hypothesized to play a key role in combatting the combinatorial explosion in visual cognition, and is also essential to the efficiency of quantum computing and radio communication.) Further, the same specialized hardware that has given deep learning a decisive edge in scaling up to large data can now be used for kernel machines as well.

The significance of our result extends beyond deep networks and kernel machines. In its light, gradient descent can be viewed as a boosting algorithm, with tangent kernel machines as the weak learner and path kernel machines as the strong learner obtained by boosting it. In each round of boosting, the examples are weighted by the corresponding loss derivatives. It is easily seen that each round (gradient descent step) decreases the loss, as required. The weight of the model at a given round is the learning rate for that step, which can be constant or the result of a line search. In the latter case gradient descent is similar to gradient boosting.

Another consequence of our result is that every probabilistic model learned by gradient descent, including Bayesian networks, is a form of kernel density estimation. The result also implies that the solution of every convex learning problem is a kernel machine, irrespective of the optimization method used, since, being unique, it is necessarily the solution obtained by gradient descent. It is an open question whether the result can be extended to nonconvex models learned by non-gradient-based techniques, including constrained and combinatorial optimization.

The results in this paper suggest a number of research directions. For example, viewing gradient descent as a method for learning path kernel machines may provide new paths for improving it. Conversely, gradient descent is not necessarily the only way to form superpositions of examples that are useful for prediction. The key question is how to optimize the tradeoff between accurately capturing the target function and minimizing the computational cost of storing and matching the examples in the superposition.
