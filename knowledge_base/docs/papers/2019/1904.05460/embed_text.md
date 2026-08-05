<!-- arxiv-full-text:v1 {"arxiv_id": "1904.05460", "source": "ar5iv"} -->

## Introduction

Since its introduction over 200 years ago by Legendre and Gauss, the method of least squares \[, \] has been one of the most widely employed computational techniques in many fields, including machine learning and statistics, signal processing, control, robotics, and finance. Its wide application primarily comes from the fact that it has a simple analytical solution, it is easy to understand, and very efficient and stable algorithms for computing its solution have been developed \[, \].

In essentially all applications, the least squares objective is not the true objective; rather it is a surrogate for the real goal. For example, in least squares data fitting, the objective is not to solve a least squares problem involving the training data set, but rather to find a model or predictor that generalizes, i.e., achieves small error on new unseen data. In control, the least squares objective is only a surrogate for keeping the state near some target or desired value, while keeping the control or actuator input small.

To account for the discrepancy between the least squares objective and the true objective, it is common practice to modify (or tune) the least squares problem that is solved to obtain a good solution in terms of the true objective. Typical tricks here include modifying the data, adding additional (regularization) terms to the cost function, or varying hyper-parameters or weights in the least squares problem to be solved.

The art of using least squares in applications is generally in how to carry out these modifications or choose these additional terms, and how to choose the hyper-parameters. The choice of hyper-parameters is often done in an ad hoc way, by varying them, solving the least squares problem, and then evaluating the result using the true objective or objectives. In data fitting, for example, regularization scaled by a hyper-parameter is added to the least squares problem, which is solved for many values of the hyper-parameter to obtain a family of data models; among these, the one that gives the best predictions on a test set of data is the one that is ultimately used. We refer to this general design approach, of modifying the least squares problem to be solved, varying some hyper-parameters, and evaluating the result using the true objective, as *least squares tuning*. It is very widely used, and can be extremely effective in practice.

Our focus in this paper is on automating the process of least squares tuning, for a variety of data fitting applications. We parametrize the least squares problem to be solved by hyper-parameters, and then automatically adjust these hyper-parameters using a gradient-based optimization algorithm, to obtain the best (or at least better) true performance. This lets us automatically search the hyper-parameter design space, which can lead us to better designs than could be found manually, or help us find good values of the hyper-parameters more quickly than if the adjustments were done manually. We refer to the method as *least squares auto-tuning*.

One of our main contributions in this paper is the observation that least squares auto-tuning is very effective for a wide variety of data fitting problems that are usually handled using more complex and advanced methods, such as non-quadratic loss functions or regularizers in regression, or special loss functions for classification problems. In addition, it can simultaneously adjust hyper-parameters in the feature generation chain. Through several examples, we show that ordinary least squares, used for over 200 years, coupled with automated hyper-parameter tuning, can be very effective as a method for data fitting.

The method we describe for least squares auto-tuning is easy to understand and just as easy to implement. Moreover, it is an exercise in calculus to find the derivative of the least squares solution, and an exercise in numerical linear algebra to compute it efficiently. We describe an implementation that utilizes new and powerful software frameworks that were originally designed to optimize the parameters in deep neural networks, making it very efficient on modern hardware and allowing it to scale to (extremely) large least squares tuning problems.

### Our contributions

We claim three main contributions. The first contribution is the observation that the least squares solution map can be efficiently differentiated, including when the problem data is sparse; we mirror our description with an open-source implementation for both of these cases. The second contribution is the method of least squares auto-tuning, which can automatically tune hyper-parameters in least squares problems. The final contribution is our unique application of least squares auto-tuning to data fitting.

## Background and related work

Our work mainly falls at the intersection of two fields: automatic differentiation and hyper-parameter optimization. In this section we review related work.

### Automatic differentiation

The general idea of automatic differentiation (AD) is to automatically compute the derivatives of a function given a program that evaluates the function \[, \]. In general, the cost of computing the derivative or gradient of a function can be made about the same (usually within a factor of 5) as computing the function \[, \]. This means that an optimization algorithm can obtain derivatives of the function it is optimizing as fast as computing the function itself, and explains the proliferation of gradient-based minimization methods \[, \]. There are many popular implementations of AD, and they generally fall into two categories. The first category is are trace-based AD systems, which trace computations at runtime, as they are executed; popular ones include PyTorch \[PGC^+^17\], Tensorflow eager \[AMP^+^19\], and autograd. The second category are based on source transformation, which transform the (native) source code that implements the function into source code that implements the derivative operation. Popular implementations here include Tensorflow \[ABC^+^16\], Tangent \[vMMW18\], and (more recently) Zygote.

### Argmin differentiation

Given an optimization problem parametrized by some parameters, the solution map is a set-valued map from those parameters to a set of solutions. If the solution map is differentiable (and in turn unique), then we can differentiate the solution map. For convex optimization problems that satisfy strong duality, the solution map is given by the set of solutions to the KKT conditions, which can in some cases be differentiated using the implicit function theorem. This idea has been applied to convex quadratic programs, stochastic optimization, games \[, \], physical systems \[dABPSA^+^18\], control \[AJS^+^18\], and structured inference \[, \]. In machine learning, these techniques were originally applied to neural networks \[, \] and ridge regression, and more recently to lasso, support vector machines, and log-linear models \[, \] A notable AD implementation of these methods is the PyTorch implementation `qpth`, which can compute derivatives of the solution map of quadratic programs.

### Unrolled optimization

Another approach to argmin differentiation is unrolled optimization. In unrolled optimization, one fixes the number of iterations in an iterative minimization method, and differentiates the steps taken by the method itself \[, \]. The idea of unrolled optimization was originally applied to optimizing hyper-parameters in deep neural networks, and has been extended in several ways to adjust learning rates, regularization parameters \[ \], and even to learn weights on individual data points. It is still unclear whether argmin differentiation should be performed via implicit differentiation or unrolled optimization. However, when the optimization problem is nonconvex, differentiation by unrolled optimization seems to be the only practical one.

### Hyper-parameter optimization

The idea of adjusting hyper-parameters to obtain better true performance in the context of data fitting is hardly new, and routinely employed in settings more sophisticated than least squares. For example, in data fitting, it is standard practice to vary one or more hyper-parameters to generate a set of models, and choose the model that attains the best true objective, which is usually error on an unseen test set. The most commonly employed methods here include grid search, random search, Bayesian optimization \[Moč75 \], and covariance matrix adaptation.

## Least squares auto-tuning

In this section we describe the idea of least squares tuning, our method for least squares auto-tuning, and our implementation.

### Least squares problem

The *matrix least squares problem* that depends on a *hyper-parameter vector* $\omega \in \Omega \subseteq \text{R}^{p}$ has the form where the variable is $\theta \in \text{R}^{n \times m}$, the *least squares optimization variable* or *parameter matrix*, and $A:{\Omega\rightarrow\text{R}^{k \times n}}$ and $B:{\Omega\rightarrow\text{R}^{k \times m}}$ map the hyper-parameter vector to the least squares *problem data*. The norm $\parallel \cdot \parallel_{F}$ denotes the Frobenius norm, i.e., the squareroot of the sum of squares of the entries of a matrix. We assume throughout this paper that $A{(\omega)}$ has linearly independent columns, which implies that it is tall, i.e., $k \geq n$. Under these assumptions, the *least squares solution* is unique, given by where $A{(\omega)}^{\dagger}$ denotes the (Moore-Penrose) pseudo-inverse. Solving a least squares problem for a given hyper-parameter vector corresponds to computing $\theta^{ls}{(\omega)}$. We will think of the least squares solution $\theta^{ls}$ as a function mapping the hyper-parameter $\omega \in \Omega$ to a parameter ${\theta^{ls}{(\omega)}} \in \text{R}^{n \times m}$.

### Multi-objective least squares

In many applications we have multiple least squares objectives. These are typically scalarized by forming a positive weighted sum, which leads to where $\lambda_{1},\ldots,\lambda_{r}$ are the positive objective weights. This problem is readily expressed as the standard least squares problem by stacking the objectives, with We will often write least squares problems in the form, and assume that the reader understands that the problem data can easily be transformed into. The objective weights $\lambda_{1},\ldots,\lambda_{r}$ can also be considered hyper-parameters themselves, or to depend on hyper-parameters; to keep the notation light we do not show this dependence.

### Solving the least squares problem

For a given value of $\omega$, there are many ways to solve the least squares problem, including dense or sparse QR or other factorizations \[, \], iterative methods such as CG or LSQR \[, \], and many others \[, \]. Very efficient libraries for computing the least squares solution that target multiple CPUs or one or more GPUs have also been developed \[, ABB^+^99 \]. We note that the problem is separable across the columns of $\theta$, i.e., the problem splits into $m$ independent least squares problems with vector variables and a common coefficient matrix.

We give a few more details here for two of these methods. First we consider the case where $A{(\omega)}$ and $B{(\omega)}$ are stored and manipulated as dense matrices. One attractive option (for GPU implementation) is to form the Gram matrix $G = {A^{T}A}$, along with $H = {A^{T}B}$. This requires around (order) $kn^{2}$ and $knm$ flops, respectively, but these matrix-matrix multiplies are BLAS level 3 operations, which can be carried out very efficiently. To compute $\theta^{ls}$, we can use a Cholesky factorization of $G$, $G = {LL^{T}}$, which costs order $n^{3}$ flops, solve the triangular equation ${LY} = H$, which costs order $n^{2}m$ flops, and then solve the triangular equation ${L^{T}\theta^{ls}} = Y$, which costs order $n^{2}m$ flops. Overall, the complexity of solving a dense least squares problem is order $kn{({n + m})}$.

The other case for which we give more detail is when $A{(\omega)}$ is represented as an abstract linear operator, and not as a matrix. This is a natural representation when $A{(\omega)}$ is large and sparse, or represented as a product of small (or sparse) matrices. That is, we can evaluate $A{(\omega)}u$ for any $u \in \text{R}^{n}$, and $A{(\omega)}^{T}v$ for any $v \in \text{R}^{k}$. (This is the so-called *matrix-free* representation.) We can use CG or LSQR to solve the least squares problem, in parallel for each column of $\theta$. The complexity of CG or LSQR depends on the problem, and can vary considerably based on the data, size, sparsity, choice of pre-conditioner, and required accuracy \[, \].

### Least squares tuning problem

In a *least squares tuning problem*, our goal is to choose the hyper-parameters to achieve some goal. We formalize this as the problem with variable $\omega \in \Omega$ and objective $F:{\Omega\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$, where $\psi:{\text{R}^{n \times m}\rightarrow\text{R}}$ is the *true objective function*, and $r:{\Omega\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ is the *hyper-parameter regularization function*. We use infinite values of $r$ (and therefore $F$) to encode constraints on the hyper-parameter $\omega$, and will assume that $r{(\omega)}$ is defined as $\infty$ for $\omega \notin \Omega$. A least squares tuning problem is specified by the functions $A$, $B$, $\psi$, and $r$. We will make some additional assumptions about these functions below.

The hyper-parameter regularization function $r$ can itself contain a few parameters that can be varied, which of course affects the hyper-parameters chosen in the least squares auto-tuning problem, which in turn affects the parameters selected by least squares. We refer to parameters that may appear in the hyper-parameter regularization function as *hyper-hyper-parameters*.

The least squares tuning problem can be formulated in several alternative ways, for example as the constrained problem with variables $\theta \in \text{R}^{n \times m}$ and $\omega \in \Omega$ In this formulation, $\theta$ and $\omega$ are independent variables, coupled by the constraint, which is the optimality condition for the least squares problem. Eliminating the constraint in this problem yields our formulation.

### Solving the least squares tuning problem

The least squares tuning problem is in general nonconvex, and difficult or impossible as a practical matter to solve exactly \[, \]. (One important exception is when $\omega$ is a scalar and $\Omega$ is an interval, in which case we can simply evaluate $F{(\omega)}$ on a grid of values over $\Omega$.) This means that we will need to resort to a local optimization or heuristic method in order to (approximately) solve it.

We will assume that $A$ and $B$ are differentiable in $\omega$, which implies that $\theta^{ls}$ is differentiable in $\omega$, since the mapping from $\omega$ to $\theta^{ls}$ is differentiable. We will also assume that $\psi$ is differentiable, which implies that the true objective $\psi{({\theta^{ls}{(\omega)}})}$ is differentiable in the hyper-parameters $\omega$. This means that the first term (the true objective) in the least squares tuning problem is differentiable, while the second one (the hyper-parameter regularizer) need not be. There are many methods that can be used to (approximately) solve such a composite problem \[ BPC^+^11 \].

For completeness, we describe one of the simplest methods, the proximal gradient method (which stems from the proximal point method; for a modern reference see), given by the iteration where $k$ denotes the iteration number, $t^{k} > 0$ is a step size, and the proximal operator ${\mathbf{p}\mathbf{r}\mathbf{o}\mathbf{x}}_{tr}:{\text{R}^{p}\rightarrow\Omega}$ is given by We assume here that the argmin exists; when it is not unique, we choose any minimizer. In order to use the proximal gradient method, we need the proximal operator of $tr$ to be relatively easy to evaluate.

The proximal gradient method reduces to the ordinary gradient method when $r = 0$ and $\Omega = \text{R}^{p}$. Another special case is when $\Omega \subset \text{R}^{p}$, and ${r{(\omega)}} = 0$ for $\omega \in \Omega$. In this case $r$ is the indicator function of the set $\Omega$, the proximal operator of $tr$ is Euclidean projection onto $\Omega$, and the proximal gradient method coincides with the projected gradient method.

### Choosing the step size

There are many ways to choose the step size. We adopt the following simple adaptive scheme, borrowed. The method begins with an initial step size $t^{1}$. If the function value decreases or stays the same from iteration $k$ to $k + 1$, or ${F{(\omega^{k + 1})}} \leq {F{(\omega^{k})}}$, then we increase the step size a bit and accept the update. If, on the other hand, the function value increases from iteration $k$ to $k + 1$, or ${F{(\omega^{k + 1})}} > {F{(\omega^{k})}}$, we decrease the step size substantially and reject the update, i.e., $\omega^{k + 1} = \omega^{k}$. A simple rule for increasing the step size is $t^{k + 1} = {{(1.2)}t^{k}}$, and a simple rule for decreasing it is $t^{k + 1} = {{({1/2})}t^{k}}$.

We note that more sophisticated step size selection methods exist (see, e.g., the line search methods for the Goldstein or Armijo conditions ).

### Stopping criterion

By default, we run the method for a fixed maximum number of iterations. If ${F{(\omega^{k + 1})}} \leq {F{(\omega^{k})}}$, then a reasonable stopping criterion at iteration $k + 1$ is where $g^{k} = {{\nabla_{\omega^{k}}\psi}{({\theta^{ls}{(\omega^{k})}})}}$, for some small tolerance $\epsilon > 0$. (For more justification of this stopping criterion, see Appendix B.) When $r = 0$ and $\Omega = \text{R}^{p}$ (i.e., the proximal gradient method coincides with the ordinary gradient method), this stopping criterion reduces to which is the standard stopping criterion in the ordinary gradient method. The full algorithm for least squares auto-tuning via the proximal gradient method is summarized in Algorithm 3.2.

Algorithm 3.1 *Least squares auto-tuning via proximal gradient.* We emphasize that many other methods can be used to (approximately) solve the least squares tuning problem; we have described the proximal gradient method here only for completeness.

### Computing the gradient

*Note.* In principle, one could calculate the gradient by directly differentiating the linear algebra routines used to solve the least squares problem. We, however, work out formulas for computing the gradient analytically, that work in the case of sparse $A$ and allow for a more efficient implementation.

To compute $g = {{\nabla_{\omega}\psi}{({\theta^{ls}{(\omega)}})}} \in \text{R}^{p}$ we can make use of the chain rule for the composition $f = {\psi \circ \theta^{ls}}$. We assume that $\theta = {\theta^{ls}{(\omega)}}$ has been computed. We first compute ${{\nabla_{\theta}\psi}{(\theta)}} \in \text{R}^{n \times m}$, and then form (Here we have dropped the dependence on $\omega$, i.e., $A = {A{(\omega)}}$.) If $A$ is stored as a dense matrix, we observe that $G = {A^{T}A}$ and its factorization have already been computed (to evaluate $\theta$), so this step involves a back-solve. If $A$ is represented as an abstract operator, we can evaluate each column of $C$ (in parallel) using an iterative method.

It can be shown (see Appendix A) that the gradients of $\psi$ with respect to $A$ and $B$ are given by (Again, the dependence on $\omega$ has been dropped.)

In the case of $A$ dense, we can explicitly form $\nabla_{A}\psi$ and $\nabla_{B}\psi$, since they are the same size as $A$ and $B$, which we already have stored. The overall complexity of computing $\nabla_{A}\psi$ and $\nabla_{B}\psi$ is $kn{({n + m})}$ in the dense case, which is the same cost as solving the least squares problem.

In the case of $A$ sparse, we can explicitly form the matrix $\nabla_{B}\psi$, but we can not form $\nabla_{A}\psi$, since it is the size of $A$, which by assumption is too large to store. Instead, we assume that $\omega$ only affects $A$ at a subset of its entries, $\Gamma$, i.e., ${A_{ij}{(\omega)}} = 0$ for all ${i,j} \notin \Gamma$, and for all $\omega \in \Omega$. By doing this, we have restricted $\nabla_{A}\psi$ to have the same sparsity pattern as $A$, meaning we only need to compute ${({\nabla_{A}\psi})}_{ij}$ for ${i,j} \in \Gamma$. That is, we compute where $b_{i}$ is the $i$th row of $B$, $a_{i}$ is the $i$th row of $A$, $c_{j}$ is the $j$th column of $C$, and ${({C\theta^{T}})}_{j}$ is the $j$th column of $C\theta^{T}$. (This computation can be done in parallel.)

The next step is to compute $g = {\nabla_{\omega}\psi}$ given $\nabla_{A}\psi$ and $\nabla_{B}\psi$. We first describe how $g$ can be computed in the case of dense $A$, and then in the case of sparse $A$.

### Dense $A$

We first evaluate ${\nabla_{\omega}A_{ij}} \in \text{R}^{p}$ and ${\nabla_{\omega}B_{ij}} \in \text{R}^{p}$, the gradients of the problem data entries with respect to $\omega$. If these gradients are all dense, we need to store $k{({n + m})}$ vectors in $\text{R}^{p}$; but generally, they are quite sparse. (We explain how to take advantage of the sparsity in §3.4.) Finally, we have Assuming these are all dense, this requires order ${{knp} + {kmp}} = {kp{({n + m})}}$ flops. The overall complexity of evaluating the gradient $g$ is order $k{({n + m})}{({n + p})}$.

### Sparse $A$

When $A$ is large and sparse, we only need to compute the inner product at the entries of $A$ that are affected by $\omega$, i.e., we compute If ${|\Gamma|} \ll {kn}$, then this can be much faster than treating $A$ as dense.

### Implementation

The equations in §3.3 for computing $g$ do not directly lend themselves to an implementation. For example, we need to compute $\nabla_{\theta}\psi$, $\nabla_{\omega}A_{ij}$ and $\nabla_{\omega}B_{ij}$, which depend on the form of $\psi$, $A$, and $B$. Also, we would like to take advantage of the (potential) sparsity of these gradients. We can use libraries for automatic differentiation, e.g., PyTorch \[PGC^+^17\] and Tensorflow \[ABC^+^16\], to automatically (and efficiently) compute $g$ given $\psi$, $A$, and $B$.

These libraries generally work by representing functions as differentiable computation graphs, allowing one to evaluate the function as well as its gradient. In our case, we represent $\psi$ as a function of $\omega$, defined by a differentiable computation graph, and use these libraries to automatically compute $g = {\nabla_{\omega}\psi}$. In order to use these libraries to compute $g$, we need to implement an operation that solves the least squares problem and computes its gradients. We have implemented an operation `lstsq(A,B)` that does exactly this, in both PyTorch and Tensorflow, in both the dense and sparse case. (The code can be found in the Appendix.)

There are several advantages of using these libraries. First, they automatically exploit parallelism and gradient sparsity. Second, they utilize BLAS level 3 operations, which are very efficient on modern hardware. Third, they make it easy to represent the functions $\psi$, $A$, and $B$, since they can be represented as compositions of (the many) pre-defined operations in these libraries.

We also provide a generic PyTorch implementation of the adaptive proximal gradient algorithm that we used in this paper.

### GPU timings

Table 1 gives timings of computing ${\psi{({\theta^{ls}{(\omega)}})}} = {\operatorname{\mathbf{t}\mathbf{r}}{({\mathbf{1}\mathbf{1}^{T}\theta^{ls}{(\omega)}})}}$ and its gradient $g$ for a random problem (where $\omega$ simply scales the rows of a fixed $A$ and $B$) and various problem dimensions, where $A$ is dense. The timings given are for the PyTorch implementation, on an unloaded GeForce GTX 1080 Ti Nvidia GPU using 32-bit floating point numbers (floats). The timings are about ten times longer using 64-bit floating point numbers (doubles). (For most applications, including data fitting, we only need floats.) We also give the percentage of time spent on the Cholesky factorization of the Gram matrix.

Table 1: GPU timings.

### Equality constrained extension

One can easily extend the ideas described in this paper to the equality-constrained least squares problem with variable $\theta \in \text{R}^{n \times m}$, where $C:{\Omega\rightarrow\text{R}^{d \times n}}$ and $D:{\Omega\rightarrow\text{R}^{d \times m}}$. The pair of primal and dual variables ${(\theta,\nu)} \in {\text{R}^{n \times m} \times \text{R}^{d \times m}}$ are optimal if and only if they satisfy the KKT conditions \[, Chapter 16\] From here, we let When $A$ and $C$ are dense, one can factorize $M$ directly, using an $LDL^{T}$ factorization. When $A$ and $C$ are sparse matrices, one can solve this system iteratively (i.e., without forming the matrix $M$) using, e.g., MINRES.

Our true objective function becomes a function of both $\eta = {(\theta,\nu)}$. Suppose we have the gradient $\nabla_{\eta}\psi$. We first compute Then the gradients of $\psi$ with respect to $A$ and $B$ are given by and with respect to $C$ and $D$ are given by Computing the gradients of the solution map requires the solution of two linear systems, and thus has roughly double the complexity of computing the solution itself (and much less in the dense case when a factorization is cached). When $A$ and $C$ are sparse, we can compute their gradients at only the nonzero elements, in a similar fashion to the procedure described in §3.3.

## Least squares data fitting

In the previous section we described the general idea of least squares auto-tuning. In this section, and for the remainder of the paper, we apply least squares auto-tuning to data fitting.

### Least squares data fitting

In a data fitting problem, we have *training data* consisting of *inputs* ${u_{1},\ldots,u_{N}} \in \mathcal{U}$ and *outputs* ${y_{1},\ldots,y_{N}} \in \text{R}^{m}$. In *least squares data fitting*, we fit the parameters of a predictor where $\theta \in \text{R}^{n \times m}$ is the model variable, $\omega^{feat} \in \Omega^{feat} \subseteq \text{R}^{p^{feat}}$ are feature engineering hyper-parameters, and $\phi:{{\mathcal{U} \times \Omega^{feat}}\rightarrow\text{R}^{n}}$ is a featurizer (assumed to be differentiable in its second argument). We note that this predictor is linear in the output of the featurizer.

To select the model parameters, we solve a least squares problem with data given by where $\omega^{data} \in \Omega^{data} \subseteq \text{R}^{N}$ are data weighting hyper-parameters, $R_{1},\ldots,R_{d}$ are regularization matrices with appropriate sizes, and $\omega^{reg} \in \Omega^{reg} \subseteq \text{R}^{d}$ are regularization hyper-parameters.

The overall hyper-parameter is denoted We will describe the roles of each hyper-parameter in more detail below; but here we note that $\omega^{data}$ scales the individual training data examples, $\omega^{feat}$ are hyper-parameters in our featurizer, and $\omega^{reg}$ are hyper-parameters that scale each of our regularizers. We assume that the hyper-parameter regularization function is separable, meaning it has the form leading to a separable proximal operator.

### True objective function

We also have *validation data* composed of inputs ${u_{1}^{val},\ldots,u_{N_{val}}^{val}} \in \mathcal{U}$ and outputs ${y_{1}^{val},\ldots,y_{N_{val}}^{val}} \in \text{R}^{m}$. We form predictions where the featurizer is fixed, or ${\phi{(u)}} = {\phi{(u,\omega^{data})}}$. The true objective $\psi$ in least squares data fitting corresponds to the average loss of our predictions of the validation outputs, which has the form where $l:{{\text{R}^{m} \times \text{R}^{m}}\rightarrow\text{R}}$ is a penalty function (assumed to be differentiable in its first argument).

### Regression and classification

The setting that we have described encompasses many problems in data fitting, including both regression and classification. In regression, the output is a scalar, i.e., $y \in \text{R}$. In multi-task regression, the output is a vector, i.e., $y \in \text{R}^{m}$. In boolean classification, $y \in {\{ e_{1},e_{2}\}}$ ($e_{i}$ is the $i$th unit vector in $\text{R}^{2}$), and the output represents a boolean class. In multi-class classification, $y \in {\{ e_{i}\mid{i = {1,\ldots,m}}\}}$ ($e_{i}$ is the $i$th unit vector in $\text{R}^{m}$), and the output represents a class label.

### Regression penalty function

The penalty function in regression (and multi-task regression) problems often has the form where $r = {\hat{y} - y}$ is the residual and $\pi:{\text{R}^{m}\rightarrow\text{R}}$ is a penalty function applied to the residual. Some common forms for $\pi$ are listed below.

*Square*. The square penalty is given by ${\pi{(r)}} = {\| r\|}_{2}^{2}$.

*Huber*. The Huber penalty is a robust penalty that has the form of the square penalty for small residuals, and the 2-norm penalty for large residuals: We can consider $M$ as a hyper-hyper-parameter.

*Bisquare*. The bisquare penalty is a robust penalty that is constant for large residuals: We can consider $M$ as a hyper-hyper-parameter.

### Classification penalty function

For classification, we associate with our prediction $\hat{y} \in \text{R}^{m}$ the probability distribution on the $m$ label values given by We interpret our prediction $\hat{y}$ as giving us a distribution on the labels of $y$, given $x$.

We will use the *cross-entropy loss* as the penalty function in classification. It has the form The true loss is then average negative log probability of $y$ under the predicted distribution, over the test set.

We now describe the role of each of the three (vector) components of our hyper-parameter vector.

### Data weighting

We first describe the role of the data weighting hyper-parameter $\omega^{data}$. The $i$th entry $\omega_{i}^{data}$ *weights* the squared error of the $(u_{i},y_{i})$ data point in the loss by $e^{2\omega_{i}^{data}}$ (a positive number). If $\omega_{i}$ is small, then the $i$th data point has little effect on the model parameter, and vice versa.

By separately weighting the loss values of each data point, we can get the same effect as using a non-quadratic loss function. However, instead of having to decide on which loss function to use, we can automatically select the weights in a weighted square loss.

We let $\Omega^{data} = {\{ x\mid{{\mathbf{1}^{T}x} = 0}\}}$, meaning we constrain the geometric mean of $\exp{(\omega^{data})}$ to be one. We describe some forms for the hyper-parameter regularization function $r^{data}$. We can regularize the hyper-parameter towards each data point being weighted equally ($\omega^{data} = 0$), e.g., by using ${r^{data}{(\omega)}} = {\lambda{\|\omega\|}_{2}^{2}}$ or ${r^{data}{(\omega)}} = {\lambda{\|\omega\|}_{1}}$, where $\lambda > 0$. (Here $\lambda$ is a hyper-hyper-parameter, since it scales a regularizer on the hyper-parameters.)

### Proximal operator

We give details on a particular proximal operator that is needed later in the paper. Evaluating the proximal operator of ${r^{data}{(\omega)}} = {\lambda{\|\omega\|}_{2}^{2}}$ with $\Omega = \Omega^{data}$ at $\nu$ with step size $t$ corresponds to solving the optimization problem with variable $\omega$. The (linear) KKT system for this optimization problem is with dual variable $y$. This linear system can be solved efficiently using block elimination \[, Appendix C\].

### Regularization

The next hyper-parameter subvector that we consider is the regularization hyper-parameter $\omega^{reg}$. The regularization hyper-parameter affects the term in the least squares objective. Each ${\|{R_{i}\theta}\|}_{F}^{2}$ term is meant to correspond to a measure of the complexity of $\theta$. For example, if $R_{i} = I$, then the $i$th term is the sum of the squares of the singular values of $\theta$. The entries of the regularization hyper-parameter correspond to the log of the weight on each regularization term. The regularization matrices can have many forms; here we give two examples.

### Diagonal regularization

Separate diagonal regularization has the form where $e_{i}$ is the $i$th unit vector in $\text{R}^{n}$. The $i$th regularization term corresponds to the sum of squares of the $i$th row of $\theta$.

### Graph regularization

The $R_{i}$ can correspond to incidence matrices of graphs between the elements in each column of $\theta$. Here the regularization hyper-parameter determines the relative importance of the regularization graphs.

### Feature engineering

The final hyper-parameter is the feature engineering hyper-parameter $\omega^{feat}$, which parametrizes the featurizer. The goal is to select a $\omega^{feat}$ which makes the output $y$ roughly linear in $\phi{(u,\omega^{feat})}$. We assume that the input set $\mathcal{U}$ is a vector space in these examples.

### Composition

Often $\phi$ is constructed as a feature generation chain, meaning it can be expressed as the composition of individual feature engineering functions $\phi_{1},\ldots,\phi_{l}$, or Often the last feature engineering function adds a constant, or ${\phi_{l}{(x)}} = {(x,1)}$, so that the resulting predictor is affine.

### Scalar feature engineering functions

We describe some scalar feature engineering functions $\phi:{\text{R}\rightarrow\text{R}}$, with the assumption that we could apply them elementwise (with different hyper-parameters) to vector inputs.

### Scaling

One of the simplest feature engineering functions is affine scaling, given by It is common practice in data fitting to standardize or whiten the data, by scaling each dimension with $a = {{1/{\mathbf{s}\mathbf{t}\mathbf{d}}}{(x)}}$ and $b = {- {\mathbf{E}{{{\lbrack x\rbrack}/{\mathbf{s}\mathbf{t}\mathbf{d}}}{(x)}}}}$. Instead, with least squares auto tuning, we can select $a$ and $b$ based on the data.

### Power transform

The *power transform* is given by where ${\mathbf{s}\mathbf{g}\mathbf{n}}{(x)}$ is $1$ if $x > 0$, $- 1$ if $x < 0$ and $0$ if $x = 0$, the center $c \in \text{R}$, and the scale $\gamma \in \text{R}$. Here the hyper-parameters are $\gamma \in \text{R}$ and the center $c \in \text{R}$. For various values of $\gamma$ and $c$, this function defines different transformations. For example, if $\gamma = 1$ and $c = 0$, this transform is the identity. If $\gamma = 0$, this transform determines whether $x$ is to the right or left of the center, $c$. If $\gamma = {1/2}$ and $c = 0$, this transform performs a symmetric square root. This transform is differentiable everywhere except when $\gamma = 0$. See figure 1 for some examples.

Figure 1: Examples of the power transform. Here the center c = 0.

### Polynomial splines

A spline is a piecewise polynomial function. Given a monotonically increasing knot vector $z \in \text{R}^{k + 1}$, a degree $d$, and polynomial coefficients ${f_{0},\ldots,f_{k + 1}} \in \text{R}^{d + 1}$, a spline is given by Here $r^{feat}$ and $\Omega^{feat}$ can be used to enforce continuity (and differentiability) at $z_{1},\ldots,z_{k + 1}$.

### Multi-dimensional feature engineering functions

Next we describe some multidimensional feature engineering functions.

### Low rank

Can be a low rank transformation, given by where $T \in \text{R}^{r \times n}$, and $r < n$. In practice, a common choice for $T$ is the first few eigenvectors of the singular value decomposition of the data matrix. With least squares auto tuning, we can select $T$ directly.

### Neural networks

The featurizer $\phi$ can be a neural network; in this case $\omega^{feat}$ corresponds to the neural network's parameters.

### Feature selection

We can select a fraction $f$ of the features with where $\Omega^{feat} = {\{ a\mid{{a \in {\{ 0,1\}}^{n_{1}}},{{\mathbf{1}^{T}a} = {\lfloor{fn_{1}}\rfloor}}}\}}$. Here $f$ is a hyper-hyper-parameter.

### Test set and early stopping

There is a risk of overfitting to the validation set when there are a large number of hyper-parameters, since we are (almost) directly minimizing the validation loss. To detect this, we introduce a third dataset, the *test dataset*, and evaluate the fitted model on it *once* at the end of the algorithm. In particular, the validation loss throughout the algorithm need not be an accurate measure of the model's performance on new unseen data, especially when there are many hyper-parameters.

### Early stopping

As a slight variation, to combat overfitting, we can calculate the loss of the fitted model on the test at each iteration, and halt the algorithm when the test loss begins to increase. This technique is sometimes referred to as early stopping. When performing early stopping, it is important to have a fourth dataset, the *final test dataset*, and evaluate on this set one time when the algorithm terminates. We have observed that this technique works very well in practice. However, we do not use early stopping in our numerical example, and instead run the algorithm until convergence.

## Numerical example

In this section we apply our method of automatic least squares data fitting to the well-studied MNIST handwritten digit classification dataset. We note that in the machine learning community, this task is considered "solved" , e.g., deep convolutional neural networks (i.e., one can achieve arbitrarily low test error). We apply the ideas described in this paper to a large and small version of MNIST in order to show that standard least squares coupled with automatic tuning of additional hyper-parameters can achieve relatively high test accuracy, and can drastically improve the performance of standard least squares. In this example, it is also worth nothing that we do not perform any hyper-hyper-parameter optimization.

### MNIST

The MNIST dataset is composed of 50,000 training data points, where each data point is a 784-vector (a $28 \times 28$ grayscale image flattened in row-order). There are $m = 10$ classes, corresponding to the digits 0--9. MNIST also comes with a test set, composed of 10,000 training points and labels. Since the task here is classification, we use the cross-entropy loss as the true objective function. The code used to produce these results has been made freely available at [www.github.com/sbarratt/lsat](www.github.com/sbarratt/lsat). All experiments were performed on an unloaded Nvidia 1080 TI GPU using floats.

We create two MNIST datasets by randomly selecting data points. The *small dataset* has 3,500 training data points and 1,500 validation data points. The *full dataset* has 35,000 training data points and 15,000 validation data points. We evaluate four methods by tuning their hyper-parameters and then calculating the final validation loss and test error. The results are summarized in table 3 and table 2. We describe each method below, in order.

LS + reg × 3 + feat + weighting Table 2: Small dataset.

LS + reg × 3 + feat + weighting Table 3: Full dataset.

### Base model

The simplest model is standard least squares, using the $n = 784$ image pixels as the feature vector. That is, we solve the optimization problem Here we do no hyper-parameter tuning. We refer to this model as *LS* in the tables.

### Regularization

To this simple model, we add a graph regularization term, and optimize the two regularization hyper-parameters. We define a graph on the length 784 feature vector, connecting two nodes if the pixels they correspond to are adjacent to each other in the original image. We then compute the incidence matrix of this graph, as described in §4.4, and denote it by $A \in \text{R}^{1512 \times 784}$ (it has 1512 edges). We then use the two regularization matrices: The matrix $R_{1}$ corresponds to standard ridge regularization, and $R_{2}$ measures the smoothness of the feature vector according to the graph we defined. This introduces $2$ hyper-parameters, which separately weight $R_{1}$ and $R_{2}$. We do not use a hyper-parameter regularization function, and initialize $\omega^{reg} = {({- 2},{- 2})}$. We optimize these two regularization hyper-parameters to minimize validation loss. We refer to this model as *LS + reg $\times$ 2* in the tables.

### Feature engineering

For each label, we run the $k$-means algorithm with $k = 5$ on the training data points that have that label. From this, we get ${km} = 50$ centers, which we call *archetypes* and denote by ${a_{1},\ldots,a_{50}} \in \text{R}^{784}$. Define the function $d$ such that it calculates how far $x$ is from each of the archetypes, or We use the feature engineering function where $\sigma$ is a feature engineering hyper-parameter, and $s$ is the softmax function, which transforms a vector $z \in \text{R}^{n}$ to a vector in the probability simplex, defined as We introduce separate ridge regularization for the pixel features and the $k$-means features, i.e., and still use the graph regularization on the pixel features; the regularization matrices are We do not use a hyper-parameter regularization function for $\omega^{feat}$. We initialize $\sigma$ to $3$ and $\omega^{reg}$ to $$, and optimize these four hyper-parameters. We refer to this model as *LS + reg $\times$ 3 + feat*.

### Data weighting

To LS + reg $\times$ 3 + feat, we add data weighting, as described in §4.3. We use $\Omega^{reg} = {\{\omega\mid{{\mathbf{1}^{T}\omega} = 0}\}}$ and ${r^{reg}{(\omega^{reg})}} = {{(0.01)}{\|\omega^{reg}\|}_{2}^{2}}$. This introduces 3,500 hyper-parameters in the case of the small dataset, and 35,000 hyper-parameters for the large dataset. We use the initialization $\omega = 0$. We refer to this model as *LS + reg $\times$ 3 + feat + weighting*. This method performs the best on the small dataset, in terms of test error. On the full dataset, it performs slightly worse than the model without data weighting, likely because of the overfitting phenomenon discussed in §4.6. We show the training examples with the lowest data weights and the training examples with the highest weights in figure 2 and figure 3 respectively, on the small dataset. The training data points with low weights seem harder to classify (for example, (b) and (c) in figure 2 could be interpreted as nines).

Figure 2: Training data with the lowest weights. Captions correspond to labels.

Figure 3: Training data with the highest weights. Captions correspond to labels.

## Conclusion

The authors are currently writing a second paper, *Least Squares Auto-Tuning Examples*, which will detail many more applications of the methods described in this paper to data fitting, control, and estimation.
