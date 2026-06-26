## Introduction

Over the last decade, stochastic first-order optimization methods have emerged as the canonical tools for training large-scale machine learning models. These methods are particularly appealing due to their wide applicability and their low runtime and memory costs.

A potentially more powerful family of algorithms consists of *preconditioned* gradient methods. Preconditioning methods maintain a matrix, termed a preconditioner, which is used to transform (i.e., premultiply) the gradient vector before it is used to take a step. Classic algorithms in this family include Newton's method, which employs the local Hessian as a preconditioner, as well as a plethora of quasi-Newton methods (e.g., ) that can be used whenever second-order information is unavailable or too expensive to compute. Newer additions to this family are preconditioned online algorithms, most notably AdaGrad, that use the covariance matrix of the accumulated gradients to form a preconditioner.

While preconditioned methods often lead to improved convergence properties, the dimensionality of typical problems in machine learning prohibits out-of-the-box use of full-matrix preconditioning. To mitigate this issue, specialized variants have been devised in which the full preconditioner is replaced with a diagonal approximation, a sketched version, or various estimations thereof. While the diagonal methods are heavily used in practice thanks to their favorable scaling with the dimension, the other approaches are seldom practical at large scale as one typically requires a fine approximation (or estimate) of the preconditioner that often demands super-linear memory and computation.

In this paper, we take an alternative approach to preconditioning and describe an efficient and practical apparatus that exploits the structure of the parameter space. Our approach is motivated by the observation that in numerous machine learning applications, the parameter space entertains a more complex structure than a monolithic vector in Euclidean space. In multiclass problems the parameters form a matrix of size $m \times n$ where $m$ is the number of features and $n$ is the number of classes. In neural networks, the parameters of each fully-connected layer form an $m \times n$ matrix with $n$ being the number of input nodes and $m$ is the number of outputs. The space of parameters of convolutional neural networks for images is a collection of $4$ dimensional tensors of the form input-depth $\times$ width $\times$ height $\times$ output-depth. As a matter of fact, machine learning software tools such as Torch and TensorFlow are designed with tensor structure in mind.

Figure 1: Illustration of Shampoo for a 3-dimensional tensor G ∈ ℝ3 × 4 × 5.

Our algorithm, which we call Shampoo,^11^1We call it Shampoo because it has to do with preconditioning. retains the tensor structure of the gradient and maintains a separate preconditioner matrix for each of its dimensions. An illustration of Shampoo is provided in Figure 1. The set of preconditioners is updated by the algorithm in an online fashion with the second-order statistics of the accumulated gradients, similarly to AdaGrad. Importantly, however, each individual preconditioner is a full, yet moderately-sized, matrix that can be effectively manipulated in large scale learning problems.

While our algorithm is motivated by modern machine learning practices, in particular training of deep neural networks, its derivation stems from our analysis in a stochastic convex optimization setting. In fact, we analyze Shampoo in the broader framework of online convex optimization, thus its convergence applies more generally. Our analysis combines well-studied tools in online optimization along with off-the-beaten-path inequalities concerning geometric means of matrices. Moreover, the adaptation to the high-order tensor case is non-trivial and relies on extensions of matrix analysis to the tensor world.

We implemented Shampoo (in its general tensor form) in Python as a new optimizer in the TensorFlow framework. Shampoo is extremely simple to implement, as most of the computations it performs boil down to standard tensor operations supported out-of-the-box in TensorFlow and similar libraries. Using the Shampoo optimizer is also a straightforward process. Whereas recent optimization methods, such as, need to be aware of the structure of the underlying model, Shampoo only needs to be informed of the tensors involved and their sizes. In our experiments with state-of-the-art deep learning models Shampoo is capable of converging considerably faster than commonly used optimizers. Surprisingly, albeit using more complex update rule, Shampoo's runtime per step is comparable to that of simple methods such as vanilla SGD.

Initialize W1 = 0m × n; L0 = ϵ Im; R0 = ϵ In for t = 1, …, T do Receive loss function ft: ℝm × n ↦ ℝ Compute gradient Gt = ∇ft (Wt) {Gt ∈ ℝm × n} Update preconditioners: Lt = Lt − 1 + Gt GtT Rt = Rt − 1 + GtT Gt Update parameters: Wt + 1 = Wt − η Lt−1/4 Gt Rt−1/4 Algorithm 1: Shampoo, matrix case.

### Shampoo for matrices

In order to further motivate our approach we start with a special case of Shampoo and defer a formal exposition of the general algorithm to later sections. In the two dimensional case, the parameters form a matrix $W \in {\mathbb{R}}^{m \times n}$. First-order methods update iterates $W_{t}$ based on the gradient $G_{t} = {{\nabla f_{t}}{(W_{t})}}$, which is also an $m \times n$ matrix. Here, $f_{t}$ is the loss function encountered on iteration $t$ that typically represents the loss incurred over a single data point (or more generally, over a batch of data).

A structure-oblivious full-matrix preconditioning scheme would flatten the parameter space into an $mn$-dimensional vector and employ preconditioning matrices $H_{t}$ of size ${{mn} \times m}n$. In contrast, Shampoo maintains smaller left $L_{t} \in {\mathbb{R}}^{m \times m}$ and right $R_{t} \in {\mathbb{R}}^{n \times n}$ matrices containing second-moment information of the accumulated gradients. On each iteration, two preconditioning matrices are formed from $L_{t}$ and $R_{t}$ and multiply the gradient matrix from the left and right respectively. The amount of space Shampoo uses in the matrix case is $m^{2} + n^{2}$ instead of $m^{2}n^{2}$. Moreover, as the preconditioning involves matrix inversion (and often spectral decomposition), the amount of computation required to construct the left and right preconditioners is $O{({m^{3} + n^{3}})}$, substantially lower than full-matrix methods which require $O{({m^{3}n^{3}})}$.

The pseudocode of Shampoo for the matrix case is given in Algorithm 1. To recap more formally, Shampoo maintains two different matrices: an $m \times m$ matrix $L_{t}^{1/4}$ to precondition the rows of $G_{t}$ and $R_{t}^{1/4}$ for its columns. The $1/4$ exponent arises from our analysis; intuitively, it is a sensible choice as it induces an overall step-size decay rate of $O{({1/\sqrt{t}})}$, which is common in stochastic optimization methods. The motivation for the algorithm comes from the observation that its update rule is equivalent, after flattening $W_{t}$ and $G_{t}$, to a gradient step preconditioned using the Kronecker product of $L_{t}^{1/4}$ and $R_{t}^{1/4}$. The latter is shown to be tightly connected to a full unstructured preconditioner matrix used by algorithms such as AdaGrad. Thus, the algorithm can be thought of as maintaining a "structured" matrix which is implicitly used to precondition the flattened gradient, without either forming a full matrix or explicitly performing a product with the flattened gradient vector.

### Related work

As noted above, Shampoo is closely related to AdaGrad. The diagonal (i.e., element-wise) version of AdaGrad is extremely popular in practice and frequently applied to tasks ranging from learning linear models over sparse features to training of large deep-learning models. In contrast, the full-matrix version of AdaGrad analyzed in is rarely used in practice due to the prohibitive memory and runtime requirements associated with maintaining a full preconditioner. Shampoo can be viewed as an efficient, practical and provable apparatus for approximately and implicitly using the full AdaGrad preconditioner, without falling back to diagonal matrices.

Another recent optimization method that uses factored preconditioning is K-FAC, which was specifically designed to optimize the parameters of neural networks. K-FAC employs a preconditioning scheme that approximates the Fisher-information matrix of a generative model represented by a neural network. The Fisher matrix of each layer in the network is approximated by a Kronecker product of two smaller matrices, relying on certain independence assumptions regarding the statistics of the gradients. K-FAC differs from Shampoo in several important ways. While K-FAC is used for training generative models and needs to sample from the model's predictive distribution, Shampoo applies in a general stochastic (more generally, online) optimization setting and comes with convergence guarantees in the convex case. K-FAC relies heavily on the structure of the backpropagated gradients in a feed-forward neural network. In contrast, Shampoo is virtually oblivious to the particular model structures and only depends on standard gradient information. As a result, Shampoo is also much easier to implement and use in practice as it need not be tailored to the particular model or architecture.

## Background and technical tools

We use lowercase letters to denote scalars and vectors and uppercase letters to denote matrices and tensors. Throughout, the notation $A \succeq 0$ (resp. $A \succ 0$) for a matrix $A$ means that $A$ is *symmetric* and positive semidefinite (resp. definite), or PSD (resp. PD) in short. Similarly, the notations $A \succeq B$ and $A \succ B$ mean that ${A - B} \succeq 0$ and ${A - B} \succ 0$ respectively, and both tacitly assume that $A$ and $B$ are symmetric. Given $A \succeq 0$ and $\alpha \in {\mathbb{R}}$, the matrix $A^{\alpha}$ is defined as the PSD matrix obtained by applying $x\mapsto x^{\alpha}$ to the eigenvalues of $A$; formally, if we rewrite $A$ using its spectral decomposition $\sum_{i}{\lambda_{i}u_{i}u_{i}^{\mathsf{T}}}$ in which $(\lambda_{i},u_{i})$ is $A$'s $i$'th eigenpair, then $A^{\alpha} = {\sum_{i}{\lambda_{i}^{\alpha}u_{i}u_{i}^{\mathsf{T}}}}$. We denote by ${\| x\|}_{A} = \sqrt{x^{\mathsf{T}}Ax}$ the Mahalanobis norm of $x \in {\mathbb{R}}^{d}$ as induced by a positive definite matrix $A \succ 0$. The dual norm of $\parallel \cdot \parallel_{A}$ is denoted $\parallel \cdot \parallel_{A}^{\ast}$ and equals $\sqrt{x^{\mathsf{T}}A^{- 1}x}$. The inner product of two matrices $A$ and $B$ is denoted as ${A \bullet B} = {\operatorname{Tr}{({A^{\mathsf{T}}B})}}$. The spectral norm of a matrix $A$ is denoted ${\| A\|}_{2} = {\max_{x \neq 0}{{\|{Ax}\|}/{\| x\|}}}$ and the Frobenius norm is ${\| A\|}_{\mathsf{F}} = \sqrt{A \bullet A}$. We denote by $e_{i}$ the unit vector with $1$ in its $i$'th position and $0$ elsewhere.

### Online convex optimization

We use Online Convex Optimization (OCO) as our analysis framework. OCO can be seen as a generalization of stochastic (convex) optimization. In OCO a learner makes predictions in the form of a vector belonging to a convex domain $\mathcal{W} \subseteq {\mathbb{R}}^{d}$ for $T$ rounds. After predicting $w_{t} \in \mathcal{W}$ on round $t$, a convex function $f_{t}:{\mathcal{W}\mapsto{\mathbb{R}}}$ is chosen, potentially in an adversarial or adaptive way based on the learner's past predictions. The learner then suffers a loss $f_{t}{(w_{t})}$ and observes the function $f_{t}$ as feedback. The goal of the learner is to achieve low cumulative loss compared to any fixed vector in the $\mathcal{W}$. Formally, the learner attempts to minimize its *regret*, defined as the quantity Online convex optimization includes stochastic convex optimization as a special case. Any regret minimizing algorithm can be converted to a stochastic optimization algorithm with convergence rate $O{({\mathcal{R}_{T}/T})}$ using an online-to-batch conversion technique.

### Adaptive regularization in online optimization

We next introduce tools from online optimization that our algorithms rely upon. First, we describe an adaptive version of Online Mirror Descent (OMD) in the OCO setting which employs time-dependent regularization. The algorithm proceeds as follows: on each round $t = {1,2,\ldots,T}$, it receives the loss function $f_{t}$ and computes the gradient $g_{t} = {{\nabla f_{t}}{(w_{t})}}$. Then, given a positive definite matrix $H_{t} \succ 0$ it performs an update according to When $\mathcal{W} = {\mathbb{R}}^{d}$, Eq. 1 is equivalent to a preconditioned gradient step, ${w_{t + 1} = {w_{t} - {\etaH_{t}^{- 1}g_{t}}}}.$ More generally, the update rule can be rewritten as a projected gradient step, where ${\Pi_{\mathcal{W}}{\lbrack z;H\rbrack}} = {{\arg\min}_{w \in \mathcal{W}}{\|{w - z}\|}_{H}}$ is the projection onto the convex set $\mathcal{W}$ with respect to the norm $\parallel \cdot \parallel_{H}$. The following lemma provides a regret bound for Online Mirror Descent, see for instance.

### Lemma 1

For any sequence of matrices ${H_{1},\ldots,H_{T}} \succ 0$, the regret of online mirror descent is bounded above, In order to analyze particular regularization schemes, namely specific strategies for choosing the matrices $H_{1},\ldots,H_{T}$, we need the following lemma, adopted; for completeness, we provide a short proof in Appendix C.

### Lemma 2 (Gupta et al. )

Let $g_{1},\ldots,g_{T}$ be a sequence of vectors, and let $M_{t} = {\sum_{s = 1}^{t}{g_{s}g_{s}^{\mathsf{T}}}}$ for $t \geq 1$. Given a function $\Phi$ over PSD matrices, define (and assume that a minimum is attained for all $t$). Then

### Kronecker products

We recall the definition of the Kronecker product, the vectorization operation and their calculus. Let $A$ be an $m \times n$ matrix and $B$ be an $m' \times n'$ matrix. The Kronecker product, denoted $A \otimes B$, is an ${{mm'} \times n}n'$ block matrix defined as, For an $m \times n$ matrix $A$ with rows $a_{1},\ldots,a_{m}$, the *vectorization* (or flattening) of $A$ is the ${mn} \times 1$ column vector^22^2This definition is slightly non-standard and differs from the more typical column-major operator ${vec}{}$; the notation $\overline{vec}{}$ is used to distinguish it from the latter.

The next lemma collects several properties of the Kronecker product and the $\overline{vec}{( \cdot )}$ operator, that will be used throughout the paper. For proofs and further details, we refer to.

### Lemma 3

Let $A,A',B,B'$ be matrices of appropriate dimensions. The following properties hold: ${{({A \otimes B})}{({A' \otimes B'})}} = {{({AA'})} \otimes {({BB'})}}$; ${({A \otimes B})}^{\mathsf{T}} = {A^{\mathsf{T}} \otimes B^{\mathsf{T}}}$; If ${A,B} \succeq 0$, then for any $s \in {\mathbb{R}}$ it holds that ${({A \otimes B})}^{s} = {A^{s} \otimes B^{s}}$, and in particular, if ${A,B} \succ 0$ then ${({A \otimes B})}^{- 1} = {A^{- 1} \otimes B^{- 1}}$; If $A \succeq A'$ and $B \succeq B'$ then ${A \otimes B} \succeq {A' \otimes B'}$, and in particular, if ${A,B} \succeq 0$ then ${A \otimes B} \succeq 0$; ${\operatorname{Tr}{({A \otimes B})}} = {{\operatorname{Tr}{(A)}}{\operatorname{Tr}{(B)}}}$; ${\overline{vec}{({uv^{\mathsf{T}}})}} = {u \otimes v}$ for any two column vectors $u,v$.

The following identity connects the Kronecker product and the $\overline{vec}$ operator. It facilitates an efficient computation of a matrix-vector product where the matrix is a Kronecker product of two smaller matrices. We provide its proof for completeness; see Appendix C.

### Lemma 4

Let $G \in {\mathbb{R}}^{m \times n}$, $L \in {\mathbb{R}}^{m \times m}$ and $R \in {\mathbb{R}}^{n \times n}$. Then, one has

### Matrix inequalities

Our analysis requires the following result concerning the geometric means of matrices. Recall that by writing $X \succeq 0$ we mean, in particular, that $X$ is a symmetric matrix.

### Lemma 5 (Ando et al. )

Assume that $0 \preceq X_{i} \preceq Y_{i}$ for all $i = {1,\ldots,n}$. Assume further that all $X_{i}$ commute with each other and all $Y_{i}$ commute with each other. Let ${\alpha_{1},\ldots,\alpha_{n}} \geq 0$ such that ${\sum_{i = 1}^{n}\alpha_{i}} = 1$, then In words, the (weighted) geometric mean of commuting PSD matrices is operator monotone.

Ando et al. proved a stronger result which does not require the PSD matrices to commute with each other, relying on a generalized notion of geometric mean, but for our purposes the simpler commuting case suffices. We also use the following classic result from matrix theory, attributed to Löwner, which is an immediate consequence of Lemma 5. ‣ 2.4 Matrix inequalities ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization").

### Lemma 6

The function $x\mapsto x^{\alpha}$ is operator-monotone for $\alpha \in {\lbrack 0,1\rbrack}$, that is, if $0 \preceq X \preceq Y$ then $X^{\alpha} \preceq Y^{\alpha}$.

## Analysis of Shampoo for matrices

In this section we analyze Shampoo in the matrix case. The analysis conveys the core ideas while avoiding numerous the technical details imposed by the general tensor case. The main result of this section is stated in the following theorem.

### Theorem 7

Assume that the gradients $G_{1},\ldots,G_{T}$ are matrices of rank at most $r$. Then the regret of Algorithm 1 compared to any $W^{\star} \in {\mathbb{R}}^{m \times n}$ is bounded as follows, Let us make a few comments regarding the bound. First, under mild conditions, each of the trace terms on the right-hand side of the bound scales as $O{(T^{1/4})}$. Thus, the overall scaling of the bound with respect to the number of iterations $T$ is $O{(\sqrt{T})}$, which is the best possible in the context of online (or stochastic) optimization. For example, assume that the functions $f_{t}$ are $1$-Lipschitz with respect to the spectral norm, that is, ${\| G_{t}\|}_{2} \leq 1$ for all $t$. Let us also fix $\epsilon = 0$ for simplicity. Then, ${G_{t}G_{t}^{\mathsf{T}}} \preceq I_{m}$ and ${G_{t}^{\mathsf{T}}G_{t}} \preceq I_{n}$ for all $t$, and so we have ${\operatorname{Tr}{(L_{T}^{1/4})}} \leq {mT^{1/4}}$ and ${\operatorname{Tr}{(R_{T}^{1/4})}} \leq {nT^{1/4}}$. That is, in the worst case, while only assuming convex and Lipschitz losses, the regret of the algorithm is $O{(\sqrt{T})}$.

Second, we note that $D$ in the above bound could in principle grow with the number of iterations $T$ and is not necessarily bounded by a constant. This issue can be easily addressed, for instance, by adding an additional step to the algorithm in which $W_{t}$ is projected $W_{t}$ onto the convex set of matrices whose Frobenius norm is bounded by $D/2$. Concretely, the projection at step $t$ needs to be computed with respect to the norm induced by the pair of matrices $(L_{t},R_{t})$, defined as ${\| A\|}_{t}^{2} = {\operatorname{Tr}{({A^{\mathsf{T}}L_{t}^{1/4}AR_{t}^{1/4}})}}$; it is not hard to verify that the latter indeed defines a norm over ${\mathbb{R}}^{m \times n}$, for any ${L_{t},R_{t}} \succ 0$. Alas, the projection becomes computationally expensive in large scale problems and is rarely performed in practice. We therefore omitted the projection step from Algorithm 1 in favor of a slightly looser bound.

The main step in the proof of the theorem is established in the following lemma. The lemma implies that the Kronecker product of the two preconditioners used by the algorithm is lower bounded by a full ${{mn} \times m}n$ matrix often employed in full-matrix preconditioning methods.

### Lemma 8

Assume that ${G_{1},\ldots,G_{T}} \in {\mathbb{R}}^{m \times n}$ are matrices of rank at most $r$. Let $g_{t} = {\overline{vec}{(G_{t})}}$ denote the vectorization of $G_{t}$ for all $t$. Then, for any $\epsilon \geq 0$, In particular, the lemma shows that the small eigenvalues of the full-matrix preconditioner on the left, which are the most important for effective preconditioning, do not vanish as a result of the implicit approximation. In order to prove Lemma 8 we need the following technical result.

### Lemma 9

Let $G$ be an $m \times n$ matrix of rank at most $r$ and denote $g = {\overline{vec}{(G)}}$. Then,

### Proof

Write the singular value decomposition $G = {\sum_{i = 1}^{r}{\sigma_{i}u_{i}v_{i}^{\mathsf{T}}}}$, where $\sigma_{i} \geq 0$ for all $i$, and ${u_{1},\ldots,u_{r}} \in {\mathbb{R}}^{m}$ and ${v_{1},\ldots,v_{r}} \in {\mathbb{R}}^{n}$ are orthonormal sets of vectors. Then, $g = {\sum_{i = 1}^{r}{\sigma_{i}{({u_{i} \otimes v_{i}})}}}$ and hence, Next, we use the fact that for any set of vectors $w_{1},\ldots,w_{r}$, which holds since given a vector $x$ we can write $\alpha_{i} = {x^{\mathsf{T}}w_{i}}$, and use the convexity of $\alpha\mapsto\alpha^{2}$ to obtain Using this fact and Lemma 3(i) ‣ Lemma 3. ‣ 2.3 Kronecker products ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization") we can rewrite, Now, since ${GG^{\mathsf{T}}} = {\sum_{i = 1}^{r}{\sigma_{i}^{2}u_{i}u_{i}^{\mathsf{T}}}}$ and ${v_{i}v_{i}^{\mathsf{T}}} \preceq I_{n}$ for all $i$, we have Similarly, using ${G^{\mathsf{T}}G} = {\sum_{i = 1}^{r}{\sigma_{i}^{2}v_{i}v_{i}^{\mathsf{T}}}}$ and ${u_{i}u_{i}^{\mathsf{T}}} \preceq I_{m}$ for all $i$, we obtain the second matrix inequality. ∎

### Proof of Lemma 8

Let us introduce the following notations to simplify our derivation, From Lemma 9 we know that, Now, observe that $I_{m} \otimes B_{n}$ and $A_{m} \otimes I_{n}$ commute with each other. Using Lemma 5. ‣ 2.4 Matrix inequalities ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization") followed by Lemma 3(iii) ‣ Lemma 3. ‣ 2.3 Kronecker products ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization") and Lemma 3(i) ‣ Lemma 3. ‣ 2.3 Kronecker products ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization") yields which completes the proof. ∎ We can now prove the main result of the section.

### Proof of Theorem 7

Recall the update performed in Algorithm 1, Note that the pair of left and right preconditioning matrices, $L_{t}^{1/4}$ and $R_{t}^{1/4}$, is equivalent due to Lemma 4 to a single preconditioning matrix $H_{t} = {L_{t}^{1/4} \otimes R_{t}^{1/4}} \in {\mathbb{R}}^{{{mn} \times m}n}$. This matrix is applied to flattened version of the gradient $g_{t} = {\overline{vec}{(G_{t})}}$. More formally, letting $w_{t} = {\overline{vec}{(W_{t})}}$ we have that the update rule of the algorithm is equivalent to, Hence, we can invoke Lemma 1 in conjuction the fact that $0 \prec H_{1} \preceq \ldots \preceq H_{T}$. The latter follows from Lemma 3(iv) ‣ Lemma 3. ‣ 2.3 Kronecker products ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization"), as $0 \prec L_{1} \preceq \ldots \preceq L_{T}$ and $0 \prec R_{1} \preceq \ldots \preceq R_{T}$. We thus further bound the first term of Lemma 1, for $D = {\max_{t \in {\lbrack T\rbrack}}{\|{w_{t} - w^{\star}}\|}} = {\max_{t \in {\lbrack T\rbrack}}{\|{W_{t} - W^{\star}}\|}_{\mathsf{F}}}$ where $w^{\star} = {\overline{vec}{(W^{\star})}}$ and $H_{0} = 0$. We obtain the regret bound Let us next bound the sum on the right-hand side of Eq. 4. First, according to Lemma 8 and the monotonicity (in the operator sense) of the square root function $x\mapsto x^{1/2}$ (recall Lemma 6), for the preconditioner $H_{t}$ we have that On the other hand, invoking Lemma 2. ‣ 2.2 Adaptive regularization in online optimization ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization") with the choice of potential and $M_{t} = {\sum_{s = 1}^{t}{g_{t}g_{t}^{\mathsf{T}}}}$, we get, To see the last equality, observe that for any symmetric $A \succeq 0$, the function $\operatorname{Tr}{({{AX} + X^{- 1}})}$ is minimized at $X = A^{- {1/2}}$, since ${\nabla_{X}{\operatorname{Tr}{({{AX} + X^{- 1}})}}} = {A - X^{- 2}}$. Hence, Lemma 2. ‣ 2.2 Adaptive regularization in online optimization ‣ 2 Background and technical tools ‣ Shampoo: Preconditioned Stochastic Tensor Optimization") implies Using Eq. 5 twice along with Section 3, we obtain Finally, using the above upper bound in Eq. 4 and choosing $\eta = {D/\sqrt{2r}}$ gives the desired regret bound:

## Shampoo for tensors

In this section we introduce the Shampoo algorithm in its general form, which is applicable to tensors of arbitrary dimension. Before we can present the algorithm, we review further definitions and operations involving tensors.

### Tensors: notation and definitions

A tensor is a multidimensional array. The *order* of a tensor is the number of dimensions (also called modes). For an order-$k$ tensor $A$ of dimension $n_{1} \times \cdots \times n_{k}$, we use the notation $A_{j_{1},\ldots,j_{k}}$ to refer to the single element at position $j_{i}$ on the $i$'th dimension for all $i$ where $1 \leq j_{i} \leq n_{i}$. We also denote The following definitions are used throughout the section.

A *slice* of an order-$k$ tensor along its $i$'th dimension is a tensor of order $k - 1$ which consists of entries with the same index on the $i$'th dimension. A slice generalizes the notion of rows and columns of a matrix.

An $n_{1} \times \cdots \times n_{k}$ tensor $A$ is of *rank one* if it can be written as an outer product of $k$ vectors of appropriate dimensions. Formally, let $\circ$ denote the vector outer product and and set $A = {u^{1} \circ u^{2} \circ \cdots \circ u^{k}}$ where $u^{i} \in {\mathbb{R}}^{n_{i}}$ for all $i$. Then $A$ is an order-$k$ tensor defined through The *vectorization* operator flattens a tensor to a column vector in ${\mathbb{R}}^{n}$, generalizing the matrix $\overline{vec}$ operator. For an $n_{1} \times \cdots \times n_{k}$ tensor $A$ with slices $A_{1}^{1},\ldots,A_{n_{1}}^{1}$ along its first dimension, this operation can be defined recursively as follows: where for the base case ($k = 1$), we define ${\overline{vec}{(u)}} = u$ for any column vector $u$.

The *matricization* operator ${mat}_{i}{(A)}$ reshapes a tensor $A$ to a matrix by vectorizing the slices of $A$ along the $i$'th dimension and stacking them as rows of a matrix. More formally, for an $n_{1} \times \cdots \times n_{k}$ tensor $A$ with slices $A_{1}^{i},\ldots,A_{n_{i}}^{i}$ along the $i$'th dimension, matricization is defined as the $n_{i} \times n_{- i}$ matrix, The matrix product of an $n_{1} \times \cdots \times n_{k}$ tensor $A$ with an $m \times n_{i}$ matrix $M$ is defined as the $n_{1} \times \cdots \times n_{i - 1} \times m \times n_{i + 1} \times \cdots \times n_{k}$ tensor, denoted $A \times_{i}M$, for which the identity ${{mat}_{i}{({A \times_{i}M})}} = {M{mat}_{i}{(A)}}$ holds. Explicitly, we define $A \times_{i}M$ element-wise as A useful fact, that follows directly from this definition, is that the tensor-matrix product is commutative, in the sense that ${{A \times_{i}M} \times_{i'}M'} = {{A \times_{i'}M'} \times_{i}M}$ for any $i \neq i'$ and matrices $M \in {\mathbb{R}}^{n_{i} \times n_{i}}$, $M' \in {\mathbb{R}}^{n_{i'} \times n_{i'}}$.

The *contraction* of an $n_{1} \times \cdots \times n_{k}$ tensor $A$ with itself along all but the $i$'th dimension is an $n_{i} \times n_{i}$ matrix defined as $A^{(i)} = {{mat}_{i}{(A)}{mat}_{i}{(A)}^{\mathsf{T}}}$, or more explicitly as where the sum ranges over all possible indexings $\alpha_{- i}$ of all dimensions $\neq i$.

### The algorithm

We can now describe the Shampoo algorithm in the general, order-$k$ tensor case, using the definitions established above. Here we assume that the optimization domain is $\mathcal{W} = {\mathbb{R}}^{n_{1} \times \cdots \times n_{k}}$, that is, the vector space of order-$k$ tensors, and the functions $f_{1},\ldots,f_{T}$ are convex over this domain. In particular, the gradient $\nabla f_{t}$ is also an $n_{1} \times \cdots \times n_{k}$ tensor.

The Shampoo algorithm in its general form, presented in Algorithm 2, is analogous to Algorithm 1. It maintains a separate preconditioning matrix $H_{t}^{i}$ (of size $n_{i} \times n_{i}$) corresponding to for each dimension $i \in {\lbrack k\rbrack}$ of the gradient. On step $t$, the $i$'th mode of the gradient $G_{t}$ is then multiplied by the matrix ${(H_{t}^{i})}^{- {1/{2k}}}$ through the tensor-matrix product operator $\times_{i}$. (Recall that the order in which the multiplications are carried out does not affect the end result and can be arbitrary.) After all dimensions have been processed and the preconditioned gradient ${\overset{\sim}{G}}_{t}$ has been obtained, a gradient step is taken.

Initialize: W1 = 0n1 × ⋯ × nk; ∀i ∈ [k]: H0i = ϵ Ini for t = 1, …, T do Receive loss function ft: ℝn1 × ⋯ × nk ↦ ℝ Compute gradient Gt = ∇ft (Wt) {Gt ∈ ℝn1 × ⋯ × nk} ${\overset{\sim}{G}}_{t}\leftarrow G_{t}$ {${\overset{\sim}{G}}_{t}$ is preconditioned gradient} for i = 1, …, k do Hti = Ht − 1i + Gt(i) ${\overset{\sim}{G}}_{t}\leftarrow{{\overset{\sim}{G}}_{t} \times_{i}{(H_{t}^{i})}^{- {1/{2k}}}}$ Update: $W_{t + 1} = {W_{t} - {\eta{\overset{\sim}{G}}_{t}}}$ Algorithm 2: Shampoo, general tensor case.

The tensor operations $A^{(i)}$ and $M \times_{i}A$ can be implemented using tensor contraction, which is a standard library function in scientific computing libraries such as Python's NumPy, and is fully supported by modern machine learning frameworks such as TensorFlow. See Section 5 for further details on our implementation of the algorithm in the TensorFlow environment.

We now state the main result of this section.

### Theorem 10

Assume that for all $i \in {\lbrack k\rbrack}$ and $t = {1,\ldots,T}$ it holds that ${{rank}{({{mat}_{i}{(G_{t})}})}} \leq r_{i}$, and let $r = {({\prod_{i = 1}^{k}r_{i}})}^{1/k}$. Then the regret of Algorithm 2 compared to any $W^{\star} \in {\mathbb{R}}^{n_{1} \times \cdots \times n_{k}}$ is where $H_{T}^{i} = {{\epsilonI_{n_{i}}} + {\sum_{t = 1}^{T}G_{t}^{(i)}}}$ for all $i \in {\lbrack k\rbrack}$ and $D = {\max_{t \in {\lbrack T\rbrack}}{\|{W_{t} - W^{\star}}\|}_{\mathsf{F}}}$.

The comments following Theorem 7 regarding the parameter $D$ in the above bound and the lack of projections in the algorithm are also applicable in the general tensor version. Furthermore, as in the matrix case, under standard assumptions each of the trace terms on the right-hand side of the above bound is bounded by $O{(T^{1/{2k}})}$. Therefore, their product, and thereby the overall regret bound, is $O{(\sqrt{T})}$.

### Analysis

We turn to proving Theorem 10. For the proof, we require the following generalizations of Lemmas 8 and 4 to tensors of arbitrary order.

### Lemma 11

Assume that $G_{1},\ldots,G_{T}$ are all order $k$ tensors of dimension $n_{1} \times \cdots \times n_{k}$, and let $n = {n_{1}\cdotsn_{k}}$ and $g_{t} = {\overline{vec}{(G_{t})}}$ for all $t$. Let $r_{i}$ denote the bound on the rank of the $i^{\text{th}}$ matricization of $G_{1},\ldots,G_{T}$, namely, ${{rank}{({{mat}_{i}{(G_{t})}})}} \leq r_{i}$ for all $t$ and $i \in {\lbrack k\rbrack}$. Denote $r = {({\prod_{i = 1}^{k}r_{i}})}^{1/k}$. Then, for any $\epsilon \geq 0$ it holds that

### Lemma 12

Let $G$ be an $n_{1} \times \ldots \times n_{k}$ dimensional tensor and $M_{i}$ be an $n_{i} \times n_{i}$ for $i \in {\lbrack k\rbrack}$, then We defer proofs to Appendix B. The proof of our main theorem now readily follows.

### Proof of Theorem 10

The proof is analogous to that of Theorem 7. For all $t$, let Similarly to the order-two (matrix) case, and in light of Lemma 12, the update rule of the algorithm is equivalent to ${w_{t + 1} = {w_{t} - {\etaH_{t}^{- 1}g_{t}}}}.$ The rest of the proof is identical to that of the matrix case, using Lemma 11 in place of Lemma 8. ∎

## Implementation details

We implemented Shampoo in its general tensor form in Python as a new TensorFlow optimizer. Our implementation follows almost verbatim the pseudocode shown in Algorithm 2. We used the built-in tensordot operation to implement tensor contractions and tensor-matrix products. Matrix powers were computed simply by constructing a singular value decomposition (SVD) and then taking the powers of the singular values. These operations are fully supported in TensorFlow. We plan to implement Shampoo in PyTorch in the near future.

Our optimizer treats each tensor in the input model as a separate optimization variable and applies the Shampoo update to each of these tensors independently. This has the advantage of making the optimizer entirely oblivious to the specifics of the architecture, and it only has to be aware of the tensors involved and their dimensions. In terms of preconditioning, this approach amounts to employing a block-diagonal preconditioner, with blocks corresponding to the different tensors in the model. In particular, only intra-tensor correlations are captured and correlations between parameters in different tensors are ignored entirely.

Our optimizer also implements a diagonal variant of Shampoo which is automatically activated for a dimension of a tensor whenever it is considered too large for the associated preconditioner to be stored in memory or to compute its SVD. Other dimensions of the same tensor are not affected and can still use non-diagonal preconditioning (unless they are too large themselves). See Appendix A for a detailed description of this variant and its analysis. In our experiments, we used a threshold of around 1200 for each dimension to trigger the diagonal version with no apparent sacrifice in performance. This option gives the benefit of working with full preconditioners whenever possible, while still being able to train models where some of the tensors are prohibitively large, and without having to modify either the architecture or the code used for training.

## Experimental results

We performed experiments with Shampoo on several datasets, using standard deep neural-network models. We focused on two domains: image classification on CIFAR-10/100, and statistical language modeling on LM1B. In each experiment, we relied on existing code for training the models, and merely replaced the TensorFlow optimizer without making any other changes to the code.

In all of our experiments, we worked with a mini-batch of size 128. In Shampoo, this simply means that the gradient $G_{t}$ used in each iteration of the algorithm is the average of the gradient over 128 examples, but otherwise has no effect on the algorithm. Notice that, in particular, the preconditioners are also updated once per batch using the averaged gradient rather than with gradients over individual examples.

We made two minor heuristic adjustments to Shampoo to improve performance. First, we employed a delayed update for the preconditioners, and recomputed the roots of the matrices $H_{t}^{i}$ once in every 20--100 steps. This had almost no impact on accuracy, but helped to improve the amortized runtime per step. Second, we incorporated momentum into the gradient step, essentially computing the running average of the gradients ${\overline{G}}_{t} = {{\alpha{\overline{G}}_{t - 1}} + {{({1 - \alpha})}G_{t}}}$ with a fixed setting of $\alpha = 0.9$. This slightly improved the convergence of the algorithm, as is the case with many other first-order stochastic methods.

Quite surprisingly, while the Shampoo algorithm performs significantly more computation per step than algorithms like SGD, AdaGrad, and Adam, its actual runtime in practice is not much worse. Table 1 shows the average number of steps (i.e., batches of size 128) per second on a Tesla K40 GPU, for each of the algorithms we tested. As can be seen from the results, each step of Shampoo is typically slower than that of the other algorithms by a small margin, and in some cases (ResNet-55) it is actually faster.

Table 1: Average number of steps per second (with batch size of 128) in each experiment, for each of the algorithms we tested.

### Image Classification

Figure 2: Training loss for a residual network and an inception network on CIFAR-10.

We ran the CIFAR-10 benchmark with several different architectures. For each optimization algorithm, we explored 10 different learning rates between 0.01 and 10.0 (scaling the entire range for Adam), and chose the one with the best loss and error. We show in Fig. 2 the training loss for a 32-layer residual network with 2.4M parameters. This network is capable of reaching an error rate of 5% on the test set. We also ran on the 20-layer small inception network described in Zhang et al., with 1.65M trainable parameters, capable of reaching an error rate of 7.5% on test data.

For CIFAR-100 (Fig. 3), we used a 55-layer residual network with 13.5M trainable parameters. In this model, the trainable variables are all tensors of order $4$ (all layers are convolutional), where the largest layer is of dimension $$. This architecture does not employ batch-norm, dropout, etc., and was able to reach an error rate of 24% on the test set.

Figure 3: Training loss for a residual network on CIFAR-100 (without batchnorm).

### Language Models

Our next experiment was on the LM1B benchmark for statistical language modeling. We used an Attention model with 9.8M trainable parameters . This model has a succession of fully connected-layers, with corresponding tensors of order at most $2$, the largest of which is of dimension $$. In this experiment, we simply used the default learning rate of $\eta = 1.0$ for Shampoo. For the other algorithms we explored various different settings of the learning rate. The graph for the test perplexity is shown in Fig. 4.

Figure 4: Test log-perplexity of an Attention model of Vaswani et al..
