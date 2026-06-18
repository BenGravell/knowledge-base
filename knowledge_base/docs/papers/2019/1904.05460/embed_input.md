<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Least Squares Auto-Tuning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Least squares is by far the simplest and most commonly applied computational method in many fields. In almost all applications, the least squares objective is rarely the true objective. We account for this discrepancy by parametrizing the least squares problem and automatically adjusting these parameters using an optimization algorithm. We apply our method, which we call least squares auto-tuning, to data fitting.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since its introduction over 200 years ago by Legendre and Gauss, the method of least squares has been one of the most widely employed computational techniques in many fields, including machine learning and statistics, signal processing, control, robotics, and finance. Its wide application primarily comes from the fact that it has a simple analytical solution, it is easy to understand, and very efficient and stable algorithms for computing its solution have been developed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In essentially all applications, the least squares objective is not the true objective; rather it is a surrogate for the real goal. For example, in least squares data fitting, the objective is not to solve a least squares problem involving the training data set, but rather to find a model or predictor that generalizes, i.e., achieves small error on new unseen data. In control, the least squares objective is only a surrogate for keeping the state near some target or desired value, while keeping the control or actuator input small.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To account for the discrepancy between the least squares objective and the true objective, it is common practice to modify (or tune) the least squares problem that is solved to obtain a good solution in terms of the true objective. Typical tricks here include modifying the data, adding additional (regularization) terms to the cost function, or varying hyper-parameters or weights in the least squares problem to be solved.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The art of using least squares in applications is generally in how to carry out these modifications or choose these additional terms, and how to choose the hyper-parameters. The choice of hyper-parameters is often done in an ad hoc way, by varying them, solving the least squares problem, and then evaluating the result using the true objective or objectives. In data fitting, for example, regularization scaled by a hyper-parameter is added to the least squares problem, which is solved for many values of the hyper-parameter to obtain a family of data models; among these, the one that gives the best predictions on a test set of data is the one that is ultimately used. We refer to this general design approach, of modifying the least squares problem to be solved, varying some hyper-parameters, and evaluating the result using the true objective, as *least squares tuning*. It is very widely used, and can be extremely effective in practice.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our focus in this paper is on automating the process of least squares tuning, for a variety of data fitting applications. We parametrize the least squares problem to be solved by hyper-parameters, and then automatically adjust these hyper-parameters using a gradient-based optimization algorithm, to obtain the best (or at least better) true performance. This lets us automatically search the hyper-parameter design space, which can lead us to better designs than could be found manually, or help us find good values of the hyper-parameters more quickly than if the adjustments were done manually. We refer to the method as *least squares auto-tuning*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of our main contributions in this paper is the observation that least squares auto-tuning is very effective for a wide variety of data fitting problems that are usually handled using more complex and advanced methods, such as non-quadratic loss functions or regularizers in regression, or special loss functions for classification problems. In addition, it can simultaneously adjust hyper-parameters in the feature generation chain. Through several examples, we show that ordinary least squares, used for over 200 years, coupled with automated hyper-parameter tuning, can be very effective as a method for data fitting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The method we describe for least squares auto-tuning is easy to understand and just as easy to implement. Moreover, it is an exercise in calculus to find the derivative of the least squares solution, and an exercise in numerical linear algebra to compute it efficiently. We describe an implementation that utilizes new and powerful software frameworks that were originally designed to optimize the parameters in deep neural networks, making it very efficient on modern hardware and allowing it to scale to (extremely) large least squares tuning problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We claim three main contributions. The first contribution is the observation that the least squares solution map can be efficiently differentiated, including when the problem data is sparse; we mirror our description with an open-source implementation for both of these cases. The second contribution is the method of least squares auto-tuning, which can automatically tune hyper-parameters in least squares problems. The final contribution is our unique application of least squares auto-tuning to data fitting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

The general idea of automatic differentiation (AD) is to automatically compute the derivatives of a function given a program that evaluates the function. In general, the cost of computing the derivative or gradient of a function can be made about the same (usually within a factor of 5) as computing the function. This means that an optimization algorithm can obtain derivatives of the function it is optimizing as fast as computing the function itself, and explains the proliferation of gradient-based minimization methods. There are many popular implementations of AD, and they generally fall into two categories. The first category is are trace-based AD systems, which trace computations at runtime, as they are executed; popular ones include PyTorch \[PGC^+^17\], Tensorflow eager \[AMP^+^19\], and autograd. The second category are based on source transformation, which transform the (native) source code that implements the function into source code that implements the derivative operation. Popular implementations here include Tensorflow \[ABC^+^16\], Tangent \[vMMW18\], and (more recently) Zygote.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Argmin differentiation", "weight": 1.0} -->

Given an optimization problem parametrized by some parameters, the solution map is a set-valued map from those parameters to a set of solutions. If the solution map is differentiable (and in turn unique), then we can differentiate the solution map. For convex optimization problems that satisfy strong duality, the solution map is given by the set of solutions to the KKT conditions, which can in some cases be differentiated using the implicit function theorem. This idea has been applied to convex quadratic programs, stochastic optimization, games, physical systems \[dABPSA^+^18\], control \[AJS^+^18\], and structured inference. In machine learning, these techniques were originally applied to neural networks and ridge regression, and more recently to lasso, support vector machines, and log-linear models A notable AD implementation of these methods is the PyTorch implementation `qpth`, which can compute derivatives of the solution map of quadratic programs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Unrolled optimization", "weight": 1.0} -->

Another approach to argmin differentiation is unrolled optimization. In unrolled optimization, one fixes the number of iterations in an iterative minimization method, and differentiates the steps taken by the method itself. The idea of unrolled optimization was originally applied to optimizing hyper-parameters in deep neural networks, and has been extended in several ways to adjust learning rates, regularization parameters, and even to learn weights on individual data points. It is still unclear whether argmin differentiation should be performed via implicit differentiation or unrolled optimization. However, when the optimization problem is nonconvex, differentiation by unrolled optimization seems to be the only practical one.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Hyper-parameter optimization", "weight": 1.0} -->

The idea of adjusting hyper-parameters to obtain better true performance in the context of data fitting is hardly new, and routinely employed in settings more sophisticated than least squares. For example, in data fitting, it is standard practice to vary one or more hyper-parameters to generate a set of models, and choose the model that attains the best true objective, which is usually error on an unseen test set. The most commonly employed methods here include grid search, random search, Bayesian optimization \[Moč75 \], and covariance matrix adaptation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Least squares auto-tuning", "weight": 1.0} -->

In this section we describe the idea of least squares tuning, our method for least squares auto-tuning, and our implementation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Least squares problem", "weight": 1.0} -->

The *matrix least squares problem* that depends on a *hyper-parameter vector* $\omega \in \Omega \subseteq \text{R}^{p}$ has the form

<!-- chunk {"id": "body-0017", "role": "body", "section": "Least squares problem", "weight": 1.0} -->

where the variable is $\theta \in \text{R}^{n \times m}$, the *least squares optimization variable* or *parameter matrix*, and $A:{\Omega\rightarrow\text{R}^{k \times n}}$ and $B:{\Omega\rightarrow\text{R}^{k \times m}}$ map the hyper-parameter vector to the least squares *problem data*. The norm $\parallel \cdot \parallel_{F}$ denotes the Frobenius norm, i.e., the squareroot of the sum of squares of the entries of a matrix. We assume throughout this paper that $A{(\omega)}$ has linearly independent columns, which implies that it is tall, i.e., $k \geq n$. Under these assumptions, the *least squares solution* is unique, given by

<!-- chunk {"id": "body-0018", "role": "body", "section": "Least squares problem", "weight": 1.0} -->

where $A{(\omega)}^{\dagger}$ denotes the (Moore-Penrose) pseudo-inverse. Solving a least squares problem for a given hyper-parameter vector corresponds to computing $\theta^{ls}{(\omega)}$. We will think of the least squares solution $\theta^{ls}$ as a function mapping the hyper-parameter $\omega \in \Omega$ to a parameter ${\theta^{ls}{(\omega)}} \in \text{R}^{n \times m}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Multi-objective least squares", "weight": 1.0} -->

In many applications we have multiple least squares objectives. These are typically scalarized by forming a positive weighted sum, which leads to

<!-- chunk {"id": "body-0020", "role": "body", "section": "Multi-objective least squares", "weight": 1.0} -->

where $\lambda_{1},\ldots,\lambda_{r}$ are the positive objective weights. This problem is readily expressed as the standard least squares problem by stacking the objectives, with

<!-- chunk {"id": "body-0021", "role": "body", "section": "Multi-objective least squares", "weight": 1.0} -->

We will often write least squares problems in the form, and assume that the reader understands that the problem data can easily be transformed into. The objective weights $\lambda_{1},\ldots,\lambda_{r}$ can also be considered hyper-parameters themselves, or to depend on hyper-parameters; to keep the notation light we do not show this dependence.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Solving the least squares problem", "weight": 1.0} -->

For a given value of $\omega$, there are many ways to solve the least squares problem, including dense or sparse QR or other factorizations, iterative methods such as CG or LSQR, and many others. Very efficient libraries for computing the least squares solution that target multiple CPUs or one or more GPUs have also been developed \[, ABB^+^99 \]. We note that the problem is separable across the columns of $\theta$, i.e., the problem splits into $m$ independent least squares problems with vector variables and a common coefficient matrix.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Solving the least squares problem", "weight": 1.0} -->

We give a few more details here for two of these methods. First we consider the case where $A{(\omega)}$ and $B{(\omega)}$ are stored and manipulated as dense matrices. One attractive option (for GPU implementation) is to form the Gram matrix $G = {A^{T}A}$, along with $H = {A^{T}B}$. This requires around (order) $kn^{2}$ and $knm$ flops, respectively, but these matrix-matrix multiplies are BLAS level 3 operations, which can be carried out very efficiently. To compute $\theta^{ls}$, we can use a Cholesky factorization of $G$, $G = {LL^{T}}$, which costs order $n^{3}$ flops, solve the triangular equation ${LY} = H$, which costs order $n^{2}m$ flops, and then solve the triangular equation ${L^{T}\theta^{ls}} = Y$, which costs order $n^{2}m$ flops.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Solving the least squares problem", "weight": 1.0} -->

Overall, the complexity of solving a dense least squares problem is order $kn{({n + m})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Solving the least squares problem", "weight": 1.0} -->

The other case for which we give more detail is when $A{(\omega)}$ is represented as an abstract linear operator, and not as a matrix. This is a natural representation when $A{(\omega)}$ is large and sparse, or represented as a product of small (or sparse) matrices. That is, we can evaluate $A{(\omega)}u$ for any $u \in \text{R}^{n}$, and $A{(\omega)}^{T}v$ for any $v \in \text{R}^{k}$. (This is the so-called *matrix-free* representation.) We can use CG or LSQR to solve the least squares problem, in parallel for each column of $\theta$. The complexity of CG or LSQR depends on the problem, and can vary considerably based on the data, size, sparsity, choice of pre-conditioner, and required accuracy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Least squares tuning problem", "weight": 1.0} -->

In a *least squares tuning problem*, our goal is to choose the hyper-parameters to achieve some goal. We formalize this as the problem

<!-- chunk {"id": "body-0027", "role": "body", "section": "Least squares tuning problem", "weight": 1.0} -->

with variable $\omega \in \Omega$ and objective $F:{\Omega\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$, where $\psi:{\text{R}^{n \times m}\rightarrow\text{R}}$ is the *true objective function*, and $r:{\Omega\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ is the *hyper-parameter regularization function*. We use infinite values of $r$ (and therefore $F$) to encode constraints on the hyper-parameter $\omega$, and will assume that $r{(\omega)}$ is defined as $\infty$ for $\omega \notin \Omega$. A least squares tuning problem is specified by the functions $A$, $B$, $\psi$, and $r$. We will make some additional assumptions about these functions below.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Least squares tuning problem", "weight": 1.0} -->

The hyper-parameter regularization function $r$ can itself contain a few parameters that can be varied, which of course affects the hyper-parameters chosen in the least squares auto-tuning problem, which in turn affects the parameters selected by least squares. We refer to parameters that may appear in the hyper-parameter regularization function as *hyper-hyper-parameters*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Least squares tuning problem", "weight": 1.0} -->

The least squares tuning problem can be formulated in several alternative ways, for example as the constrained problem with variables $\theta \in \text{R}^{n \times m}$ and $\omega \in \Omega$

<!-- chunk {"id": "body-0030", "role": "body", "section": "Least squares tuning problem", "weight": 1.0} -->

In this formulation, $\theta$ and $\omega$ are independent variables, coupled by the constraint, which is the optimality condition for the least squares problem. Eliminating the constraint in this problem yields our formulation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Solving the least squares tuning problem", "weight": 1.0} -->

The least squares tuning problem is in general nonconvex, and difficult or impossible as a practical matter to solve exactly. (One important exception is when $\omega$ is a scalar and $\Omega$ is an interval, in which case we can simply evaluate $F{(\omega)}$ on a grid of values over $\Omega$.) This means that we will need to resort to a local optimization or heuristic method in order to (approximately) solve it.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Solving the least squares tuning problem", "weight": 1.0} -->

We will assume that $A$ and $B$ are differentiable in $\omega$, which implies that $\theta^{ls}$ is differentiable in $\omega$, since the mapping from $\omega$ to $\theta^{ls}$ is differentiable. We will also assume that $\psi$ is differentiable, which implies that the true objective $\psi{({\theta^{ls}{(\omega)}})}$ is differentiable in the hyper-parameters $\omega$. This means that the first term (the true objective) in the least squares tuning problem is differentiable, while the second one (the hyper-parameter regularizer) need not be. There are many methods that can be used to (approximately) solve such a composite problem \[ BPC^+^11 \].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Solving the least squares tuning problem", "weight": 1.0} -->

For completeness, we describe one of the simplest methods, the proximal gradient method (which stems from the proximal point method; for a modern reference see ), given by the iteration

<!-- chunk {"id": "body-0034", "role": "body", "section": "Solving the least squares tuning problem", "weight": 1.0} -->

where $k$ denotes the iteration number, $t^{k} > 0$ is a step size, and the proximal operator ${\mathbf{p}\mathbf{r}\mathbf{o}\mathbf{x}}_{tr}:{\text{R}^{p}\rightarrow\Omega}$ is given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Solving the least squares tuning problem", "weight": 1.0} -->

We assume here that the argmin exists; when it is not unique, we choose any minimizer. In order to use the proximal gradient method, we need the proximal operator of $tr$ to be relatively easy to evaluate.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Solving the least squares tuning problem", "weight": 1.0} -->

The proximal gradient method reduces to the ordinary gradient method when $r = 0$ and $\Omega = \text{R}^{p}$. Another special case is when $\Omega \subset \text{R}^{p}$, and ${r{(\omega)}} = 0$ for $\omega \in \Omega$. In this case $r$ is the indicator function of the set $\Omega$, the proximal operator of $tr$ is Euclidean projection onto $\Omega$, and the proximal gradient method coincides with the projected gradient method.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Choosing the step size", "weight": 1.0} -->

There are many ways to choose the step size. We adopt the following simple adaptive scheme, borrowed. The method begins with an initial step size $t^{1}$. If the function value decreases or stays the same from iteration $k$ to $k + 1$, or ${F{(\omega^{k + 1})}} \leq {F{(\omega^{k})}}$, then we increase the step size a bit and accept the update. If, on the other hand, the function value increases from iteration $k$ to $k + 1$, or ${F{(\omega^{k + 1})}} > {F{(\omega^{k})}}$, we decrease the step size substantially and reject the update, i.e., $\omega^{k + 1} = \omega^{k}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Choosing the step size", "weight": 1.0} -->

A simple rule for increasing the step size is $t^{k + 1} = {{(1.2)}t^{k}}$, and a simple rule for decreasing it is $t^{k + 1} = {{({1/2})}t^{k}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Choosing the step size", "weight": 1.0} -->

We note that more sophisticated step size selection methods exist (see, e.g., the line search methods for the Goldstein or Armijo conditions ).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Stopping criterion", "weight": 1.0} -->

By default, we run the method for a fixed maximum number of iterations. If ${F{(\omega^{k + 1})}} \leq {F{(\omega^{k})}}$, then a reasonable stopping criterion at iteration $k + 1$ is

<!-- chunk {"id": "body-0041", "role": "body", "section": "Stopping criterion", "weight": 1.0} -->

where $g^{k} = {{\nabla_{\omega^{k}}\psi}{({\theta^{ls}{(\omega^{k})}})}}$, for some small tolerance $\epsilon > 0$. (For more justification of this stopping criterion, see Appendix B.) When $r = 0$ and $\Omega = \text{R}^{p}$ (i.e., the proximal gradient method coincides with the ordinary gradient method), this stopping criterion reduces to

<!-- chunk {"id": "body-0042", "role": "body", "section": "Stopping criterion", "weight": 1.0} -->

which is the standard stopping criterion in the ordinary gradient method. The full algorithm for least squares auto-tuning via the proximal gradient method is summarized in Algorithm 3.2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stopping criterion", "weight": 1.0} -->

Algorithm 3.1 *Least squares auto-tuning via proximal gradient.*

<!-- chunk {"id": "body-0044", "role": "body", "section": "Stopping criterion", "weight": 1.0} -->

We emphasize that many other methods can be used to (approximately) solve the least squares tuning problem; we have described the proximal gradient method here only for completeness.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

*Note.* In principle, one could calculate the gradient by directly differentiating the linear algebra routines used to solve the least squares problem. We, however, work out formulas for computing the gradient analytically, that work in the case of sparse $A$ and allow for a more efficient implementation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

(Here we have dropped the dependence on $\omega$, i.e., $A = {A{(\omega)}}$.) If $A$ is stored as a dense matrix, we observe that $G = {A^{T}A}$ and its factorization have already been computed (to evaluate $\theta$), so this step involves a back-solve. If $A$ is represented as an abstract operator, we can evaluate each column of $C$ (in parallel) using an iterative method.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

It can be shown (see Appendix A) that the gradients of $\psi$ with respect to $A$ and $B$ are given by

<!-- chunk {"id": "body-0048", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

(Again, the dependence on $\omega$ has been dropped.)

<!-- chunk {"id": "body-0049", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

In the case of $A$ dense, we can explicitly form $\nabla_{A}\psi$ and $\nabla_{B}\psi$, since they are the same size as $A$ and $B$, which we already have stored. The overall complexity of computing $\nabla_{A}\psi$ and $\nabla_{B}\psi$ is $kn{({n + m})}$ in the dense case, which is the same cost as solving the least squares problem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

In the case of $A$ sparse, we can explicitly form the matrix $\nabla_{B}\psi$, but we can not form $\nabla_{A}\psi$, since it is the size of $A$, which by assumption is too large to store. Instead, we assume that $\omega$ only affects $A$ at a subset of its entries, $\Gamma$, i.e., ${A_{ij}{(\omega)}} = 0$ for all ${i,j} \notin \Gamma$, and for all $\omega \in \Omega$. By doing this, we have restricted $\nabla_{A}\psi$ to have the same sparsity pattern as $A$, meaning we only need to compute ${({\nabla_{A}\psi})}_{ij}$ for ${i,j} \in \Gamma$. That is, we compute

<!-- chunk {"id": "body-0051", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

The next step is to compute $g = {\nabla_{\omega}\psi}$ given $\nabla_{A}\psi$ and $\nabla_{B}\psi$. We first describe how $g$ can be computed in the case of dense $A$, and then in the case of sparse $A$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Dense $A$", "weight": 1.0} -->

We first evaluate ${\nabla_{\omega}A_{ij}} \in \text{R}^{p}$ and ${\nabla_{\omega}B_{ij}} \in \text{R}^{p}$, the gradients of the problem data entries with respect to $\omega$. If these gradients are all dense, we need to store $k{({n + m})}$ vectors in $\text{R}^{p}$; but generally, they are quite sparse. (We explain how to take advantage of the sparsity in §3.4.) Finally, we have

<!-- chunk {"id": "body-0053", "role": "body", "section": "Dense $A$", "weight": 1.0} -->

Assuming these are all dense, this requires order ${{knp} + {kmp}} = {kp{({n + m})}}$ flops. The overall complexity of evaluating the gradient $g$ is order $k{({n + m})}{({n + p})}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sparse $A$", "weight": 1.0} -->

When $A$ is large and sparse, we only need to compute the inner product at the entries of $A$ that are affected by $\omega$, i.e., we compute

<!-- chunk {"id": "body-0055", "role": "body", "section": "Sparse $A$", "weight": 1.0} -->

If ${|\Gamma|} \ll {kn}$, then this can be much faster than treating $A$ as dense.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Implementation", "weight": 1.0} -->

The equations in §3.3 for computing $g$ do not directly lend themselves to an implementation. For example, we need to compute $\nabla_{\theta}\psi$, $\nabla_{\omega}A_{ij}$ and $\nabla_{\omega}B_{ij}$, which depend on the form of $\psi$, $A$, and $B$. Also, we would like to take advantage of the (potential) sparsity of these gradients. We can use libraries for automatic differentiation, e.g., PyTorch \[PGC^+^17\] and Tensorflow \[ABC^+^16\], to automatically (and efficiently) compute $g$ given $\psi$, $A$, and $B$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Implementation", "weight": 1.0} -->

These libraries generally work by representing functions as differentiable computation graphs, allowing one to evaluate the function as well as its gradient. In our case, we represent $\psi$ as a function of $\omega$, defined by a differentiable computation graph, and use these libraries to automatically compute $g = {\nabla_{\omega}\psi}$. In order to use these libraries to compute $g$, we need to implement an operation that solves the least squares problem and computes its gradients. We have implemented an operation `lstsq(A,B)` that does exactly this, in both PyTorch and Tensorflow, in both the dense and sparse case. (The code can be found in the Appendix.)

<!-- chunk {"id": "body-0058", "role": "body", "section": "Implementation", "weight": 1.0} -->

There are several advantages of using these libraries. First, they automatically exploit parallelism and gradient sparsity. Second, they utilize BLAS level 3 operations, which are very efficient on modern hardware. Third, they make it easy to represent the functions $\psi$, $A$, and $B$, since they can be represented as compositions of (the many) pre-defined operations in these libraries.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Implementation", "weight": 1.0} -->

We also provide a generic PyTorch implementation of the adaptive proximal gradient algorithm that we used in this paper.

<!-- chunk {"id": "body-0060", "role": "body", "section": "GPU timings", "weight": 1.0} -->

Table 1 gives timings of computing ${\psi{({\theta^{ls}{(\omega)}})}} = {\operatorname{\mathbf{t}\mathbf{r}}{({\mathbf{1}\mathbf{1}^{T}\theta^{ls}{(\omega)}})}}$ and its gradient $g$ for a random problem (where $\omega$ simply scales the rows of a fixed $A$ and $B$) and various problem dimensions, where $A$ is dense. The timings given are for the PyTorch implementation, on an unloaded GeForce GTX 1080 Ti Nvidia GPU using 32-bit floating point numbers (floats). The timings are about ten times longer using 64-bit floating point numbers (doubles). (For most applications, including data fitting, we only need floats.) We also give the percentage of time spent on the Cholesky factorization of the Gram matrix.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

One can easily extend the ideas described in this paper to the equality-constrained least squares problem

<!-- chunk {"id": "body-0062", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

with variable $\theta \in \text{R}^{n \times m}$, where $C:{\Omega\rightarrow\text{R}^{d \times n}}$ and $D:{\Omega\rightarrow\text{R}^{d \times m}}$. The pair of primal and dual variables ${(\theta,\nu)} \in {\text{R}^{n \times m} \times \text{R}^{d \times m}}$ are optimal if and only if they satisfy the KKT conditions \[, Chapter 16\]

<!-- chunk {"id": "body-0063", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

When $A$ and $C$ are dense, one can factorize $M$ directly, using an $LDL^{T}$ factorization. When $A$ and $C$ are sparse matrices, one can solve this system iteratively (i.e., without forming the matrix $M$) using, e.g., MINRES.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

Our true objective function becomes a function of both $\eta = {(\theta,\nu)}$. Suppose we have the gradient $\nabla_{\eta}\psi$. We first compute

<!-- chunk {"id": "body-0065", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

Then the gradients of $\psi$ with respect to $A$ and $B$ are given by

<!-- chunk {"id": "body-0066", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

and with respect to $C$ and $D$ are given by

<!-- chunk {"id": "body-0067", "role": "body", "section": "Equality constrained extension", "weight": 1.0} -->

Computing the gradients of the solution map requires the solution of two linear systems, and thus has roughly double the complexity of computing the solution itself (and much less in the dense case when a factorization is cached). When $A$ and $C$ are sparse, we can compute their gradients at only the nonzero elements, in a similar fashion to the procedure described in §3.3.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Least squares data fitting", "weight": 1.0} -->

In the previous section we described the general idea of least squares auto-tuning. In this section, and for the remainder of the paper, we apply least squares auto-tuning to data fitting.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Least squares data fitting", "weight": 1.0} -->

In a data fitting problem, we have *training data* consisting of *inputs* ${u_{1},\ldots,u_{N}} \in \mathcal{U}$ and *outputs* ${y_{1},\ldots,y_{N}} \in \text{R}^{m}$. In *least squares data fitting*, we fit the parameters of a predictor

<!-- chunk {"id": "body-0070", "role": "body", "section": "Least squares data fitting", "weight": 1.0} -->

where $\theta \in \text{R}^{n \times m}$ is the model variable, $\omega^{feat} \in \Omega^{feat} \subseteq \text{R}^{p^{feat}}$ are feature engineering hyper-parameters, and $\phi:{{\mathcal{U} \times \Omega^{feat}}\rightarrow\text{R}^{n}}$ is a featurizer (assumed to be differentiable in its second argument). We note that this predictor is linear in the output of the featurizer.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Least squares data fitting", "weight": 1.0} -->

To select the model parameters, we solve a least squares problem with data given by

<!-- chunk {"id": "body-0072", "role": "body", "section": "Least squares data fitting", "weight": 1.0} -->

where $\omega^{data} \in \Omega^{data} \subseteq \text{R}^{N}$ are data weighting hyper-parameters, $R_{1},\ldots,R_{d}$ are regularization matrices with appropriate sizes, and $\omega^{reg} \in \Omega^{reg} \subseteq \text{R}^{d}$ are regularization hyper-parameters.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Least squares data fitting", "weight": 1.0} -->

We will describe the roles of each hyper-parameter in more detail below; but here we note that $\omega^{data}$ scales the individual training data examples, $\omega^{feat}$ are hyper-parameters in our featurizer, and $\omega^{reg}$ are hyper-parameters that scale each of our regularizers. We assume that the hyper-parameter regularization function is separable, meaning it has the form

<!-- chunk {"id": "body-0074", "role": "body", "section": "True objective function", "weight": 1.0} -->

where the featurizer is fixed, or ${\phi{(u)}} = {\phi{(u,\omega^{data})}}$. The true objective $\psi$ in least squares data fitting corresponds to the average loss of our predictions of the validation outputs, which has the form

<!-- chunk {"id": "body-0075", "role": "body", "section": "True objective function", "weight": 1.0} -->

where $l:{{\text{R}^{m} \times \text{R}^{m}}\rightarrow\text{R}}$ is a penalty function (assumed to be differentiable in its first argument).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Regression and classification", "weight": 1.0} -->

The setting that we have described encompasses many problems in data fitting, including both regression and classification. In regression, the output is a scalar, i.e., $y \in \text{R}$. In multi-task regression, the output is a vector, i.e., $y \in \text{R}^{m}$. In boolean classification, $y \in {\{ e_{1},e_{2}\}}$ ($e_{i}$ is the $i$th unit vector in $\text{R}^{2}$), and the output represents a boolean class. In multi-class classification, $y \in {\{ e_{i}\mid{i = {1,\ldots,m}}\}}$ ($e_{i}$ is the $i$th unit vector in $\text{R}^{m}$), and the output represents a class label.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Regression penalty function", "weight": 1.0} -->

The penalty function in regression (and multi-task regression) problems often has the form

<!-- chunk {"id": "body-0078", "role": "body", "section": "Regression penalty function", "weight": 1.0} -->

where $r = {\hat{y} - y}$ is the residual and $\pi:{\text{R}^{m}\rightarrow\text{R}}$ is a penalty function applied to the residual. Some common forms for $\pi$ are listed below.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Classification penalty function", "weight": 1.0} -->

For classification, we associate with our prediction $\hat{y} \in \text{R}^{m}$ the probability distribution on the $m$ label values given by

<!-- chunk {"id": "body-0080", "role": "body", "section": "Classification penalty function", "weight": 1.0} -->

We interpret our prediction $\hat{y}$ as giving us a distribution on the labels of $y$, given $x$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Classification penalty function", "weight": 1.0} -->

We will use the *cross-entropy loss* as the penalty function in classification. It has the form

<!-- chunk {"id": "body-0082", "role": "body", "section": "Classification penalty function", "weight": 1.0} -->

The true loss is then average negative log probability of $y$ under the predicted distribution, over the test set.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Classification penalty function", "weight": 1.0} -->

We now describe the role of each of the three (vector) components of our hyper-parameter vector.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Data weighting", "weight": 1.0} -->

We first describe the role of the data weighting hyper-parameter $\omega^{data}$. The $i$th entry $\omega_{i}^{data}$ *weights* the squared error of the $(u_{i},y_{i})$ data point in the loss by $e^{2\omega_{i}^{data}}$ (a positive number). If $\omega_{i}$ is small, then the $i$th data point has little effect on the model parameter, and vice versa.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Data weighting", "weight": 1.0} -->

By separately weighting the loss values of each data point, we can get the same effect as using a non-quadratic loss function. However, instead of having to decide on which loss function to use, we can automatically select the weights in a weighted square loss.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Data weighting", "weight": 1.0} -->

We let $\Omega^{data} = {\{ x\mid{{\mathbf{1}^{T}x} = 0}\}}$, meaning we constrain the geometric mean of $\exp{(\omega^{data})}$ to be one. We describe some forms for the hyper-parameter regularization function $r^{data}$. We can regularize the hyper-parameter towards each data point being weighted equally ($\omega^{data} = 0$), e.g., by using ${r^{data}{(\omega)}} = {\lambda{\|\omega\|}_{2}^{2}}$ or ${r^{data}{(\omega)}} = {\lambda{\|\omega\|}_{1}}$, where $\lambda > 0$. (Here $\lambda$ is a hyper-hyper-parameter, since it scales a regularizer on the hyper-parameters.)

<!-- chunk {"id": "body-0087", "role": "body", "section": "Proximal operator", "weight": 1.0} -->

We give details on a particular proximal operator that is needed later in the paper. Evaluating the proximal operator of ${r^{data}{(\omega)}} = {\lambda{\|\omega\|}_{2}^{2}}$ with $\Omega = \Omega^{data}$ at $\nu$ with step size $t$ corresponds to solving the optimization problem

<!-- chunk {"id": "body-0088", "role": "body", "section": "Proximal operator", "weight": 1.0} -->

with variable $\omega$. The (linear) KKT system for this optimization problem is

<!-- chunk {"id": "body-0089", "role": "body", "section": "Proximal operator", "weight": 1.0} -->

with dual variable $y$. This linear system can be solved efficiently using block elimination \[, Appendix C\].

<!-- chunk {"id": "body-0090", "role": "body", "section": "Regularization", "weight": 1.0} -->

The next hyper-parameter subvector that we consider is the regularization hyper-parameter $\omega^{reg}$. The regularization hyper-parameter affects the

<!-- chunk {"id": "body-0091", "role": "body", "section": "Regularization", "weight": 1.0} -->

term in the least squares objective. Each ${\|{R_{i}\theta}\|}_{F}^{2}$ term is meant to correspond to a measure of the complexity of $\theta$. For example, if $R_{i} = I$, then the $i$th term is the sum of the squares of the singular values of $\theta$. The entries of the regularization hyper-parameter correspond to the log of the weight on each regularization term. The regularization matrices can have many forms; here we give two examples.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Diagonal regularization", "weight": 1.0} -->

Separate diagonal regularization has the form

<!-- chunk {"id": "body-0093", "role": "body", "section": "Diagonal regularization", "weight": 1.0} -->

where $e_{i}$ is the $i$th unit vector in $\text{R}^{n}$. The $i$th regularization term corresponds to the sum of squares of the $i$th row of $\theta$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Graph regularization", "weight": 1.0} -->

The $R_{i}$ can correspond to incidence matrices of graphs between the elements in each column of $\theta$. Here the regularization hyper-parameter determines the relative importance of the regularization graphs.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Feature engineering", "weight": 1.0} -->

The final hyper-parameter is the feature engineering hyper-parameter $\omega^{feat}$, which parametrizes the featurizer. The goal is to select a $\omega^{feat}$ which makes the output $y$ roughly linear in $\phi{(u,\omega^{feat})}$. We assume that the input set $\mathcal{U}$ is a vector space in these examples.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Composition", "weight": 1.0} -->

Often $\phi$ is constructed as a feature generation chain, meaning it can be expressed as the composition of individual feature engineering functions $\phi_{1},\ldots,\phi_{l}$, or

<!-- chunk {"id": "body-0097", "role": "body", "section": "Composition", "weight": 1.0} -->

Often the last feature engineering function adds a constant, or ${\phi_{l}{(x)}} = {(x,1)}$, so that the resulting predictor is affine.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Scalar feature engineering functions", "weight": 1.0} -->

We describe some scalar feature engineering functions $\phi:{\text{R}\rightarrow\text{R}}$, with the assumption that we could apply them elementwise (with different hyper-parameters) to vector inputs.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Scaling", "weight": 1.0} -->

One of the simplest feature engineering functions is affine scaling, given by

<!-- chunk {"id": "body-0100", "role": "body", "section": "Scaling", "weight": 1.0} -->

It is common practice in data fitting to standardize or whiten the data, by scaling each dimension with $a = {{1/{\mathbf{s}\mathbf{t}\mathbf{d}}}{(x)}}$ and $b = {- {\mathbf{E}{{{\lbrack x\rbrack}/{\mathbf{s}\mathbf{t}\mathbf{d}}}{(x)}}}}$. Instead, with least squares auto tuning, we can select $a$ and $b$ based on the data.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Power transform", "weight": 1.0} -->

where ${\mathbf{s}\mathbf{g}\mathbf{n}}{(x)}$ is $1$ if $x > 0$, $- 1$ if $x < 0$ and $0$ if $x = 0$, the center $c \in \text{R}$, and the scale $\gamma \in \text{R}$. Here the hyper-parameters are $\gamma \in \text{R}$ and the center $c \in \text{R}$. For various values of $\gamma$ and $c$, this function defines different transformations. For example, if $\gamma = 1$ and $c = 0$, this transform is the identity. If $\gamma = 0$, this transform determines whether $x$ is to the right or left of the center, $c$. If $\gamma = {1/2}$ and $c = 0$, this transform performs a symmetric square root. This transform is differentiable everywhere except when $\gamma = 0$. See figure 1 for some examples.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Polynomial splines", "weight": 1.0} -->

A spline is a piecewise polynomial function. Given a monotonically increasing knot vector $z \in \text{R}^{k + 1}$, a degree $d$, and polynomial coefficients ${f_{0},\ldots,f_{k + 1}} \in \text{R}^{d + 1}$, a spline is given by

<!-- chunk {"id": "body-0103", "role": "body", "section": "Polynomial splines", "weight": 1.0} -->

Here $r^{feat}$ and $\Omega^{feat}$ can be used to enforce continuity (and differentiability) at $z_{1},\ldots,z_{k + 1}$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Multi-dimensional feature engineering functions", "weight": 1.0} -->

Next we describe some multidimensional feature engineering functions.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Low rank", "weight": 1.0} -->

Can be a low rank transformation, given by

<!-- chunk {"id": "body-0106", "role": "body", "section": "Low rank", "weight": 1.0} -->

where $T \in \text{R}^{r \times n}$, and $r < n$. In practice, a common choice for $T$ is the first few eigenvectors of the singular value decomposition of the data matrix. With least squares auto tuning, we can select $T$ directly.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Neural networks", "weight": 1.0} -->

The featurizer $\phi$ can be a neural network; in this case $\omega^{feat}$ corresponds to the neural network's parameters.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Feature selection", "weight": 1.0} -->

We can select a fraction $f$ of the features with

<!-- chunk {"id": "body-0109", "role": "body", "section": "Test set and early stopping", "weight": 1.0} -->

There is a risk of overfitting to the validation set when there are a large number of hyper-parameters, since we are (almost) directly minimizing the validation loss. To detect this, we introduce a third dataset, the *test dataset*, and evaluate the fitted model on it *once* at the end of the algorithm. In particular, the validation loss throughout the algorithm need not be an accurate measure of the model's performance on new unseen data, especially when there are many hyper-parameters.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Early stopping", "weight": 1.0} -->

As a slight variation, to combat overfitting, we can calculate the loss of the fitted model on the test at each iteration, and halt the algorithm when the test loss begins to increase. This technique is sometimes referred to as early stopping. When performing early stopping, it is important to have a fourth dataset, the *final test dataset*, and evaluate on this set one time when the algorithm terminates. We have observed that this technique works very well in practice. However, we do not use early stopping in our numerical example, and instead run the algorithm until convergence.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In this section we apply our method of automatic least squares data fitting to the well-studied MNIST handwritten digit classification dataset. We note that in the machine learning community, this task is considered "solved", e.g., deep convolutional neural networks (i.e., one can achieve arbitrarily low test error). We apply the ideas described in this paper to a large and small version of MNIST in order to show that standard least squares coupled with automatic tuning of additional hyper-parameters can achieve relatively high test accuracy, and can drastically improve the performance of standard least squares. In this example, it is also worth nothing that we do not perform any hyper-hyper-parameter optimization.

<!-- chunk {"id": "body-0112", "role": "body", "section": "MNIST", "weight": 1.0} -->

The MNIST dataset is composed of 50,000 training data points, where each data point is a 784-vector (a $28 \times 28$ grayscale image flattened in row-order). There are $m = 10$ classes, corresponding to the digits 0--9. MNIST also comes with a test set, composed of 10,000 training points and labels. Since the task here is classification, we use the cross-entropy loss as the true objective function. The code used to produce these results has been made freely available at [www.github.com/sbarratt/lsat](www.github.com/sbarratt/lsat). All experiments were performed on an unloaded Nvidia 1080 TI GPU using floats.

<!-- chunk {"id": "body-0113", "role": "body", "section": "MNIST", "weight": 1.0} -->

We create two MNIST datasets by randomly selecting data points. The *small dataset* has 3,500 training data points and 1,500 validation data points. The *full dataset* has 35,000 training data points and 15,000 validation data points. We evaluate four methods by tuning their hyper-parameters and then calculating the final validation loss and test error. The results are summarized in table 3 and table 2. We describe each method below, in order.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Base model", "weight": 1.0} -->

The simplest model is standard least squares, using the $n = 784$ image pixels as the feature vector. That is, we solve the optimization problem

<!-- chunk {"id": "body-0115", "role": "body", "section": "Base model", "weight": 1.0} -->

Here we do no hyper-parameter tuning. We refer to this model as *LS* in the tables.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Regularization", "weight": 1.0} -->

To this simple model, we add a graph regularization term, and optimize the two regularization hyper-parameters. We define a graph on the length 784 feature vector, connecting two nodes if the pixels they correspond to are adjacent to each other in the original image. We then compute the incidence matrix of this graph, as described in §4.4, and denote it by $A \in \text{R}^{1512 \times 784}$ (it has 1512 edges).

<!-- chunk {"id": "body-0117", "role": "body", "section": "Regularization", "weight": 1.0} -->

The matrix $R_{1}$ corresponds to standard ridge regularization, and $R_{2}$ measures the smoothness of the feature vector according to the graph we defined. This introduces $2$ hyper-parameters, which separately weight $R_{1}$ and $R_{2}$. We do not use a hyper-parameter regularization function, and initialize $\omega^{reg} = {({- 2},{- 2})}$. We optimize these two regularization hyper-parameters to minimize validation loss. We refer to this model as *LS + reg $\times$ 2* in the tables.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Feature engineering", "weight": 1.0} -->

For each label, we run the $k$-means algorithm with $k = 5$ on the training data points that have that label. From this, we get ${km} = 50$ centers, which we call *archetypes* and denote by ${a_{1},\ldots,a_{50}} \in \text{R}^{784}$. Define the function $d$ such that it calculates how far $x$ is from each of the archetypes, or

<!-- chunk {"id": "body-0119", "role": "body", "section": "Feature engineering", "weight": 1.0} -->

We use the feature engineering function

<!-- chunk {"id": "body-0120", "role": "body", "section": "Feature engineering", "weight": 1.0} -->

where $\sigma$ is a feature engineering hyper-parameter, and $s$ is the softmax function, which transforms a vector $z \in \text{R}^{n}$ to a vector in the probability simplex, defined as

<!-- chunk {"id": "body-0121", "role": "body", "section": "Feature engineering", "weight": 1.0} -->

We introduce separate ridge regularization for the pixel features and the $k$-means features, i.e., and still use the graph regularization on the pixel features; the regularization matrices are

<!-- chunk {"id": "body-0122", "role": "body", "section": "Feature engineering", "weight": 1.0} -->

We do not use a hyper-parameter regularization function for $\omega^{feat}$. We initialize $\sigma$ to $3$ and $\omega^{reg}$ to $$, and optimize these four hyper-parameters. We refer to this model as *LS + reg $\times$ 3 + feat*.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Data weighting", "weight": 1.0} -->

To LS + reg $\times$ 3 + feat, we add data weighting, as described in §4.3. We use $\Omega^{reg} = {\{\omega\mid{{\mathbf{1}^{T}\omega} = 0}\}}$ and ${r^{reg}{(\omega^{reg})}} = {{(0.01)}{\|\omega^{reg}\|}_{2}^{2}}$. This introduces 3,500 hyper-parameters in the case of the small dataset, and 35,000 hyper-parameters for the large dataset. We use the initialization $\omega = 0$. We refer to this model as *LS + reg $\times$ 3 + feat + weighting*. This method performs the best on the small dataset, in terms of test error.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Data weighting", "weight": 1.0} -->

On the full dataset, it performs slightly worse than the model without data weighting, likely because of the overfitting phenomenon discussed in §4.6. We show the training examples with the lowest data weights and the training examples with the highest weights in figure 2 and figure 3 respectively, on the small dataset. The training data points with low weights seem harder to classify (for example, (b) and (c) in figure 2 could be interpreted as nines).

<!-- chunk {"id": "body-0125", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The authors are currently writing a second paper, *Least Squares Auto-Tuning Examples*, which will detail many more applications of the methods described in this paper to data fitting, control, and estimation.
