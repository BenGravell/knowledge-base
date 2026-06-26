<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Shampoo: Preconditioned Stochastic Tensor Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Preconditioned gradient methods are among the most general and powerful tools in optimization. However, preconditioning requires storing and manipulating prohibitively large matrices. We describe and analyze a new structure-aware preconditioning algorithm, called Shampoo, for stochastic optimization over tensor spaces. Shampoo maintains a set of preconditioning matrices, each of which operates on a single dimension, contracting over the remaining dimensions. We establish convergence guarantees in the stochastic convex setting, the proof of which builds upon matrix trace inequalities. Our experiments with state-of-the-art deep learning models show that Shampoo is capable of converging considerably faster than commonly used optimizers. Although it involves a more complex update rule, Shampoo's runtime per step is comparable to that of simple gradient methods such as SGD, AdaGrad, and Adam.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the last decade, stochastic first-order optimization methods have emerged as the canonical tools for training large-scale machine learning models. These methods are particularly appealing due to their wide applicability and their low runtime and memory costs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A potentially more powerful family of algorithms consists of *preconditioned* gradient methods. Preconditioning methods maintain a matrix, termed a preconditioner, which is used to transform (i.e., premultiply) the gradient vector before it is used to take a step. Classic algorithms in this family include Newton's method, which employs the local Hessian as a preconditioner, as well as a plethora of quasi-Newton methods (e.g., ) that can be used whenever second-order information is unavailable or too expensive to compute. Newer additions to this family are preconditioned online algorithms, most notably AdaGrad, that use the covariance matrix of the accumulated gradients to form a preconditioner.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While preconditioned methods often lead to improved convergence properties, the dimensionality of typical problems in machine learning prohibits out-of-the-box use of full-matrix preconditioning. To mitigate this issue, specialized variants have been devised in which the full preconditioner is replaced with a diagonal approximation, a sketched version, or various estimations thereof. While the diagonal methods are heavily used in practice thanks to their favorable scaling with the dimension, the other approaches are seldom practical at large scale as one typically requires a fine approximation (or estimate) of the preconditioner that often demands super-linear memory and computation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we take an alternative approach to preconditioning and describe an efficient and practical apparatus that exploits the structure of the parameter space. Our approach is motivated by the observation that in numerous machine learning applications, the parameter space entertains a more complex structure than a monolithic vector in Euclidean space. In multiclass problems the parameters form a matrix of size $m \times n$ where $m$ is the number of features and $n$ is the number of classes. In neural networks, the parameters of each fully-connected layer form an $m \times n$ matrix with $n$ being the number of input nodes and $m$ is the number of outputs. The space of parameters of convolutional neural networks for images is a collection of $4$ dimensional tensors of the form input-depth $\times$ width $\times$ height $\times$ output-depth. As a matter of fact, machine learning software tools such as Torch and TensorFlow are designed with tensor structure in mind.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our algorithm, which we call Shampoo,^11^1We call it Shampoo because it has to do with preconditioning. retains the tensor structure of the gradient and maintains a separate preconditioner matrix for each of its dimensions. An illustration of Shampoo is provided in Figure 1. The set of preconditioners is updated by the algorithm in an online fashion with the second-order statistics of the accumulated gradients, similarly to AdaGrad. Importantly, however, each individual preconditioner is a full, yet moderately-sized, matrix that can be effectively manipulated in large scale learning problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While our algorithm is motivated by modern machine learning practices, in particular training of deep neural networks, its derivation stems from our analysis in a stochastic convex optimization setting. In fact, we analyze Shampoo in the broader framework of online convex optimization, thus its convergence applies more generally. Our analysis combines well-studied tools in online optimization along with off-the-beaten-path inequalities concerning geometric means of matrices. Moreover, the adaptation to the high-order tensor case is non-trivial and relies on extensions of matrix analysis to the tensor world.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We implemented Shampoo (in its general tensor form) in Python as a new optimizer in the TensorFlow framework. Shampoo is extremely simple to implement, as most of the computations it performs boil down to standard tensor operations supported out-of-the-box in TensorFlow and similar libraries. Using the Shampoo optimizer is also a straightforward process. Whereas recent optimization methods, such as, need to be aware of the structure of the underlying model, Shampoo only needs to be informed of the tensors involved and their sizes. In our experiments with state-of-the-art deep learning models Shampoo is capable of converging considerably faster than commonly used optimizers. Surprisingly, albeit using more complex update rule, Shampoo's runtime per step is comparable to that of simple methods such as vanilla SGD.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Initialize W1 = 0m × n; L0 = ϵ Im; R0 = ϵ In for t = 1, …, T do Receive loss function ft: ℝm × n ↦ ℝ Compute gradient Gt = ∇ft (Wt) {Gt ∈ ℝm × n} Update preconditioners: Lt = Lt − 1 + Gt GtT Rt = Rt − 1 + GtT Gt Update parameters: Wt + 1 = Wt − η Lt−1/4 Gt Rt−1/4 Algorithm 1: Shampoo, matrix case.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Shampoo for matrices", "weight": 1.0} -->

In order to further motivate our approach we start with a special case of Shampoo and defer a formal exposition of the general algorithm to later sections. In the two dimensional case, the parameters form a matrix $W \in {\mathbb{R}}^{m \times n}$. First-order methods update iterates $W_{t}$ based on the gradient $G_{t} = {{\nabla f_{t}}{(W_{t})}}$, which is also an $m \times n$ matrix. Here, $f_{t}$ is the loss function encountered on iteration $t$ that typically represents the loss incurred over a single data point (or more generally, over a batch of data).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Shampoo for matrices", "weight": 1.0} -->

A structure-oblivious full-matrix preconditioning scheme would flatten the parameter space into an $mn$-dimensional vector and employ preconditioning matrices $H_{t}$ of size ${{mn} \times m}n$. In contrast, Shampoo maintains smaller left $L_{t} \in {\mathbb{R}}^{m \times m}$ and right $R_{t} \in {\mathbb{R}}^{n \times n}$ matrices containing second-moment information of the accumulated gradients. On each iteration, two preconditioning matrices are formed from $L_{t}$ and $R_{t}$ and multiply the gradient matrix from the left and right respectively. The amount of space Shampoo uses in the matrix case is $m^{2} + n^{2}$ instead of $m^{2}n^{2}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Shampoo for matrices", "weight": 1.0} -->

Moreover, as the preconditioning involves matrix inversion (and often spectral decomposition), the amount of computation required to construct the left and right preconditioners is $O{({m^{3} + n^{3}})}$, substantially lower than full-matrix methods which require $O{({m^{3}n^{3}})}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Shampoo for matrices", "weight": 1.0} -->

The pseudocode of Shampoo for the matrix case is given in Algorithm 1. To recap more formally, Shampoo maintains two different matrices: an $m \times m$ matrix $L_{t}^{1/4}$ to precondition the rows of $G_{t}$ and $R_{t}^{1/4}$ for its columns. The $1/4$ exponent arises from our analysis; intuitively, it is a sensible choice as it induces an overall step-size decay rate of $O{({1/\sqrt{t}})}$, which is common in stochastic optimization methods. The motivation for the algorithm comes from the observation that its update rule is equivalent, after flattening $W_{t}$ and $G_{t}$, to a gradient step preconditioned using the Kronecker product of $L_{t}^{1/4}$ and $R_{t}^{1/4}$. The latter is shown to be tightly connected to a full unstructured preconditioner matrix used by algorithms such as AdaGrad.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Shampoo for matrices", "weight": 1.0} -->

Thus, the algorithm can be thought of as maintaining a "structured" matrix which is implicitly used to precondition the flattened gradient, without either forming a full matrix or explicitly performing a product with the flattened gradient vector.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Online convex optimization", "weight": 1.0} -->

We use Online Convex Optimization (OCO) as our analysis framework. OCO can be seen as a generalization of stochastic (convex) optimization. In OCO a learner makes predictions in the form of a vector belonging to a convex domain $\mathcal{W} \subseteq {\mathbb{R}}^{d}$ for $T$ rounds. After predicting $w_{t} \in \mathcal{W}$ on round $t$, a convex function $f_{t}:{\mathcal{W}\mapsto{\mathbb{R}}}$ is chosen, potentially in an adversarial or adaptive way based on the learner's past predictions. The learner then suffers a loss $f_{t}{(w_{t})}$ and observes the function $f_{t}$ as feedback. The goal of the learner is to achieve low cumulative loss compared to any fixed vector in the $\mathcal{W}$. Formally, the learner attempts to minimize its *regret*, defined as the quantity Online convex optimization includes stochastic convex optimization as a special case.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Online convex optimization", "weight": 1.0} -->

Any regret minimizing algorithm can be converted to a stochastic optimization algorithm with convergence rate $O{({\mathcal{R}_{T}/T})}$ using an online-to-batch conversion technique.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Adaptive regularization in online optimization", "weight": 1.0} -->

We next introduce tools from online optimization that our algorithms rely upon. First, we describe an adaptive version of Online Mirror Descent (OMD) in the OCO setting which employs time-dependent regularization. The algorithm proceeds as follows: on each round $t = {1,2,\ldots,T}$, it receives the loss function $f_{t}$ and computes the gradient $g_{t} = {{\nabla f_{t}}{(w_{t})}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Adaptive regularization in online optimization", "weight": 1.0} -->

Then, given a positive definite matrix $H_{t} \succ 0$ it performs an update according to When $\mathcal{W} = {\mathbb{R}}^{d}$, Eq. 1 is equivalent to a preconditioned gradient step, ${w_{t + 1} = {w_{t} - {\etaH_{t}^{- 1}g_{t}}}}.$ More generally, the update rule can be rewritten as a projected gradient step, where ${\Pi_{\mathcal{W}}{\lbrack z;H\rbrack}} = {{\arg\min}_{w \in \mathcal{W}}{\|{w - z}\|}_{H}}$ is the projection onto the convex set $\mathcal{W}$ with respect to the norm $\parallel \cdot \parallel_{H}$. The following lemma provides a regret bound for Online Mirror Descent, see for instance.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Kronecker products", "weight": 1.0} -->

We recall the definition of the Kronecker product, the vectorization operation and their calculus. Let $A$ be an $m \times n$ matrix and $B$ be an $m' \times n'$ matrix. The Kronecker product, denoted $A \otimes B$, is an ${{mm'} \times n}n'$ block matrix defined as, For an $m \times n$ matrix $A$ with rows $a_{1},\ldots,a_{m}$, the *vectorization* (or flattening) of $A$ is the ${mn} \times 1$ column vector^22^2This definition is slightly non-standard and differs from the more typical column-major operator ${vec}{}$; the notation $\overline{vec}{}$ is used to distinguish it from the latter.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Kronecker products", "weight": 1.0} -->

The next lemma collects several properties of the Kronecker product and the $\overline{vec}{( \cdot )}$ operator, that will be used throughout the paper. For proofs and further details, we refer to.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Matrix inequalities", "weight": 1.0} -->

Our analysis requires the following result concerning the geometric means of matrices. Recall that by writing $X \succeq 0$ we mean, in particular, that $X$ is a symmetric matrix.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Analysis of Shampoo for matrices", "weight": 1.0} -->

In this section we analyze Shampoo in the matrix case. The analysis conveys the core ideas while avoiding numerous the technical details imposed by the general tensor case. The main result of this section is stated in the following theorem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Shampoo for tensors", "weight": 1.0} -->

In this section we introduce the Shampoo algorithm in its general form, which is applicable to tensors of arbitrary dimension. Before we can present the algorithm, we review further definitions and operations involving tensors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

A tensor is a multidimensional array. The *order* of a tensor is the number of dimensions (also called modes). For an order-$k$ tensor $A$ of dimension $n_{1} \times \cdots \times n_{k}$, we use the notation $A_{j_{1},\ldots,j_{k}}$ to refer to the single element at position $j_{i}$ on the $i$'th dimension for all $i$ where $1 \leq j_{i} \leq n_{i}$. We also denote The following definitions are used throughout the section.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

A *slice* of an order-$k$ tensor along its $i$'th dimension is a tensor of order $k - 1$ which consists of entries with the same index on the $i$'th dimension. A slice generalizes the notion of rows and columns of a matrix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

An $n_{1} \times \cdots \times n_{k}$ tensor $A$ is of *rank one* if it can be written as an outer product of $k$ vectors of appropriate dimensions. Formally, let $\circ$ denote the vector outer product and and set $A = {u^{1} \circ u^{2} \circ \cdots \circ u^{k}}$ where $u^{i} \in {\mathbb{R}}^{n_{i}}$ for all $i$. Then $A$ is an order-$k$ tensor defined through The *vectorization* operator flattens a tensor to a column vector in ${\mathbb{R}}^{n}$, generalizing the matrix $\overline{vec}$ operator.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

For an $n_{1} \times \cdots \times n_{k}$ tensor $A$ with slices $A_{1}^{1},\ldots,A_{n_{1}}^{1}$ along its first dimension, this operation can be defined recursively as follows: where for the base case ($k = 1$), we define ${\overline{vec}{(u)}} = u$ for any column vector $u$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

The *matricization* operator ${mat}_{i}{(A)}$ reshapes a tensor $A$ to a matrix by vectorizing the slices of $A$ along the $i$'th dimension and stacking them as rows of a matrix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

Explicitly, we define $A \times_{i}M$ element-wise as A useful fact, that follows directly from this definition, is that the tensor-matrix product is commutative, in the sense that ${{A \times_{i}M} \times_{i'}M'} = {{A \times_{i'}M'} \times_{i}M}$ for any $i \neq i'$ and matrices $M \in {\mathbb{R}}^{n_{i} \times n_{i}}$, $M' \in {\mathbb{R}}^{n_{i'} \times n_{i'}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Tensors: notation and definitions", "weight": 1.0} -->

The *contraction* of an $n_{1} \times \cdots \times n_{k}$ tensor $A$ with itself along all but the $i$'th dimension is an $n_{i} \times n_{i}$ matrix defined as $A^{(i)} = {{mat}_{i}{(A)}{mat}_{i}{(A)}^{\mathsf{T}}}$, or more explicitly as where the sum ranges over all possible indexings $\alpha_{- i}$ of all dimensions $\neq i$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The algorithm", "weight": 1.0} -->

We can now describe the Shampoo algorithm in the general, order-$k$ tensor case, using the definitions established above. Here we assume that the optimization domain is $\mathcal{W} = {\mathbb{R}}^{n_{1} \times \cdots \times n_{k}}$, that is, the vector space of order-$k$ tensors, and the functions $f_{1},\ldots,f_{T}$ are convex over this domain. In particular, the gradient $\nabla f_{t}$ is also an $n_{1} \times \cdots \times n_{k}$ tensor.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The algorithm", "weight": 1.0} -->

The Shampoo algorithm in its general form, presented in Algorithm 2, is analogous to Algorithm 1. It maintains a separate preconditioning matrix $H_{t}^{i}$ (of size $n_{i} \times n_{i}$) corresponding to for each dimension $i \in {\lbrack k\rbrack}$ of the gradient. On step $t$, the $i$'th mode of the gradient $G_{t}$ is then multiplied by the matrix ${(H_{t}^{i})}^{- {1/{2k}}}$ through the tensor-matrix product operator $\times_{i}$. (Recall that the order in which the multiplications are carried out does not affect the end result and can be arbitrary.) After all dimensions have been processed and the preconditioned gradient ${\overset{\sim}{G}}_{t}$ has been obtained, a gradient step is taken.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The algorithm", "weight": 1.0} -->

The tensor operations $A^{(i)}$ and $M \times_{i}A$ can be implemented using tensor contraction, which is a standard library function in scientific computing libraries such as Python's NumPy, and is fully supported by modern machine learning frameworks such as TensorFlow. See Section 5 for further details on our implementation of the algorithm in the TensorFlow environment.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The algorithm", "weight": 1.0} -->

We now state the main result of this section.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis", "weight": 1.0} -->

We turn to proving Theorem 10. For the proof, we require the following generalizations of Lemmas 8 and 4 to tensors of arbitrary order.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We implemented Shampoo in its general tensor form in Python as a new TensorFlow optimizer. Our implementation follows almost verbatim the pseudocode shown in Algorithm 2. We used the built-in tensordot operation to implement tensor contractions and tensor-matrix products. Matrix powers were computed simply by constructing a singular value decomposition (SVD) and then taking the powers of the singular values. These operations are fully supported in TensorFlow. We plan to implement Shampoo in PyTorch in the near future.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation details", "weight": 1.0} -->

Our optimizer treats each tensor in the input model as a separate optimization variable and applies the Shampoo update to each of these tensors independently. This has the advantage of making the optimizer entirely oblivious to the specifics of the architecture, and it only has to be aware of the tensors involved and their dimensions. In terms of preconditioning, this approach amounts to employing a block-diagonal preconditioner, with blocks corresponding to the different tensors in the model. In particular, only intra-tensor correlations are captured and correlations between parameters in different tensors are ignored entirely.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation details", "weight": 1.0} -->

Our optimizer also implements a diagonal variant of Shampoo which is automatically activated for a dimension of a tensor whenever it is considered too large for the associated preconditioner to be stored in memory or to compute its SVD. Other dimensions of the same tensor are not affected and can still use non-diagonal preconditioning (unless they are too large themselves). See Appendix A for a detailed description of this variant and its analysis. In our experiments, we used a threshold of around 1200 for each dimension to trigger the diagonal version with no apparent sacrifice in performance. This option gives the benefit of working with full preconditioners whenever possible, while still being able to train models where some of the tensors are prohibitively large, and without having to modify either the architecture or the code used for training.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental results", "weight": 1.0} -->

We performed experiments with Shampoo on several datasets, using standard deep neural-network models. We focused on two domains: image classification on CIFAR-10/100, and statistical language modeling on LM1B. In each experiment, we relied on existing code for training the models, and merely replaced the TensorFlow optimizer without making any other changes to the code.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental results", "weight": 1.0} -->

In all of our experiments, we worked with a mini-batch of size 128. In Shampoo, this simply means that the gradient $G_{t}$ used in each iteration of the algorithm is the average of the gradient over 128 examples, but otherwise has no effect on the algorithm. Notice that, in particular, the preconditioners are also updated once per batch using the averaged gradient rather than with gradients over individual examples.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental results", "weight": 1.0} -->

We made two minor heuristic adjustments to Shampoo to improve performance. First, we employed a delayed update for the preconditioners, and recomputed the roots of the matrices $H_{t}^{i}$ once in every 20--100 steps. This had almost no impact on accuracy, but helped to improve the amortized runtime per step. Second, we incorporated momentum into the gradient step, essentially computing the running average of the gradients ${\overline{G}}_{t} = {{\alpha{\overline{G}}_{t - 1}} + {{({1 - \alpha})}G_{t}}}$ with a fixed setting of $\alpha = 0.9$. This slightly improved the convergence of the algorithm, as is the case with many other first-order stochastic methods.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental results", "weight": 1.0} -->

Quite surprisingly, while the Shampoo algorithm performs significantly more computation per step than algorithms like SGD, AdaGrad, and Adam, its actual runtime in practice is not much worse. Table 1 shows the average number of steps (i.e., batches of size 128) per second on a Tesla K40 GPU, for each of the algorithms we tested. As can be seen from the results, each step of Shampoo is typically slower than that of the other algorithms by a small margin, and in some cases (ResNet-55) it is actually faster.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Image Classification", "weight": 1.0} -->

We ran the CIFAR-10 benchmark with several different architectures. For each optimization algorithm, we explored 10 different learning rates between 0.01 and 10.0 (scaling the entire range for Adam), and chose the one with the best loss and error. We show in Fig. 2 the training loss for a 32-layer residual network with 2.4M parameters. This network is capable of reaching an error rate of 5% on the test set. We also ran on the 20-layer small inception network described in Zhang et al., with 1.65M trainable parameters, capable of reaching an error rate of 7.5% on test data.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Image Classification", "weight": 1.0} -->

For CIFAR-100 (Fig. 3), we used a 55-layer residual network with 13.5M trainable parameters. In this model, the trainable variables are all tensors of order $4$ (all layers are convolutional), where the largest layer is of dimension $$. This architecture does not employ batch-norm, dropout, etc., and was able to reach an error rate of 24% on the test set.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Language Models", "weight": 1.0} -->

Our next experiment was on the LM1B benchmark for statistical language modeling. We used an Attention model with 9.8M trainable parameters. This model has a succession of fully connected-layers, with corresponding tensors of order at most $2$, the largest of which is of dimension $$. In this experiment, we simply used the default learning rate of $\eta = 1.0$ for Shampoo. For the other algorithms we explored various different settings of the learning rate. The graph for the test perplexity is shown in Fig. 4.
