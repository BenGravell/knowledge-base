## Introduction

Deep networks have achieved remarkable performance in several application domains such as computer vision, natural language processing and genomics. The input-output mapping implemented by a deep neural network is a chain of compositions of modules, where each module is typically a composition of a non-linear mapping, called an activation function, and an affine mapping. The last module in the chain is usually task-specific in that it relates to a performance accuracy for a specific task. This module can be expressed either explicitly in analytical form as in supervised classification or implicitly as a solution of an optimization problem as in dimension reduction or unsupervised clustering.

The optimization problem arising when training a deep network is often framed as a non-convex optimization problem, dismissing the structure of the objective yet central to the software implementation. Indeed optimization algorithms used to train deep networks proceed by making calls to first-order (or second-order) oracles relying on dynamic programming such as gradient back-propagation. Gradient back-propagation is now part of modern machine learning software. We highlight here the elementary yet important fact that the chain-compositional structure of the objective naturally emerges through the smoothness constants governing the convergence guarantee of a gradient-based optimization algorithm. This provides a reference frame to relate the network architecture and the convergence rate through the smoothness constants. This also brings to light the benefit of specific modules popular among practitioners to improve the convergence.

In Sec. 2, we define the parameterized input-output map implemented by a deep network as a chain-composition of modules and write the corresponding optimization objective consisting in learning the parameters of this map. In Sec. 3, we detail the implementation of first-order and second-order oracles by dynamic programming; the classical gradient back-propagation algorithm is recovered as a canonical example. Gauss-Newton steps can also be simply stated in terms of calls to an automatic-differentiation oracle implemented in modern machine learning software libraries. In Sec. 4, we present the computation of the smoothness constants of a chain of computations given its components and the resulting convergence guarantees for gradient descent. Finally, in Sec. 5, we present the application of the approach to derive the smoothness constants for the VGG architecture and illustrate how our approach can be used to identify the benefits of batch-normalization. In the Appendix, we estimate the smoothness constants related to the VGG architecture and we investigate batch-normalization in the light of our approach. All the proofs and the notations are also provided in the Appendix.

## Problem formulation

### Deep network architecture

A feed-forward deep network of depth $\tau$ can be described as a transformation of an input $x$ into an output $x_{\tau}$ through the composition of $\tau$ blocks, called layers, illustrated in Fig. 1. Each layer is defined by a set of parameters. In general, (see Sec. 2.3 for a detailed decomposition), these parameters act on the input of the layer through an affine operation followed by a non-linear operation. Formally, the $t$^th^ layer can be described as a function of its parameters $u_{t}$ and a given input $x_{t - 1}$ that outputs $x_{t}$ as

where $b_{t}$ is generally linear in $u_{t}$ and affine in $x_{t - 1}$ and $a_{t}$ is non-linear.

Learning a deep network consists in minimizing w.r.t. its parameters an objective involving $n$ inputs ${{\overline{x}}^{},\ldots,{\overline{x}}^{(n)}} \in {\mathbb{R}}^{\delta}$. Formally, the problem is written

where $u_{t} \in {\mathbb{R}}^{p_{t}}$ is the set of parameters at layer $t$ whose dimension $p_{t}$ can vary among layers and $r$ is a regularization on the parameters of the network.

We are interested in the influence of the architecture on the optimization complexity of the problem. The architecture translates into a structure of the chain of computations involved in the optimization problem.

### Definition 2.1

A chain of $\tau$ computations $\phi_{t}:{{{\mathbb{R}}^{d_{t - 1}} \times {\mathbb{R}}^{p_{t}}}\rightarrow{\mathbb{R}}^{d_{t}}}$ is defined as $f:{{{\mathbb{R}}^{d_{0}} \times {\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}}}\rightarrow{\mathbb{R}}^{\sum_{t = 1}^{\tau}d_{t}}}$ such that for $x_{0} \in {\mathbb{R}}^{d_{0}}$ and $u = {(u_{1};\ldots;u_{\tau})} \in {\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}}$ we have ${f{(x_{0},u)}} = {({f_{1}{(x_{0},u)}};\ldots;{f_{\tau}{(x_{0},u)}})}$ with

Denote then $f^{0}$ the chain of computations associated to the layers of a deep network and consider the concatenation of the transformations of each input as a single transformation, i.e., ${f_{t}{(\overline{x},u)}} = {({f_{t}^{0}{({\overline{x}}^{},u)}};\ldots;{f_{t}^{0}{({\overline{x}}^{(n)},u)}})}$ for $t \in {\{ 1,\ldots,\tau\}}$, and $\overline{x} = {({\overline{x}}^{};\ldots;{\overline{x}}^{(n)})}$, the objective in can be written as

where $f_{\tau}:{{{\mathbb{R}}^{nd_{0}} \times {\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}}}\rightarrow{\mathbb{R}}^{nd_{\tau}}}$ is the output of a chain of $\tau$ computations with $d_{0} = \delta$, $r:{{\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}}\rightarrow{\mathbb{R}}}$ is typically a decomposable differentiable function such as ${r{(u)}} = {\lambda{\sum_{t = 1}^{\tau}{\| u_{t}\|}_{2}^{2}}}$ for $\lambda \geq 0$, and we present examples of learning objectives $f:{{\mathbb{R}}^{nd_{\tau}}\rightarrow{\mathbb{R}}}$ below. Assumptions on differentiability and smoothness of the objective are detailed in Sec. 4.

Figure 1: Deep network architecture.

### Objectives

In the following, we consider the output of the chain of computations on $n$ sample to be given as $\hat{y} = {({\hat{y}}^{};\ldots;{\hat{y}}^{(n)})} = {({f_{\tau}^{0}{({\overline{x}}^{},u)}};\ldots;{f_{\tau}^{0}{({\overline{x}}^{(n)},u)}})} = {f_{\tau}{(\overline{x},u)}}$ for $\overline{x} = {({\overline{x}}^{};\ldots;{\overline{x}}^{(n)})}$.

### Supervised learning

For supervised learning, the objective can be decomposed as a finite sum

where $h^{(i)}$ are losses on the labels predicted by the chain of computations, i.e., ${h^{(i)}{({\hat{y}}^{(i)})}} = {\mathcal{L}{({\hat{y}}^{(i)},y^{(i)})}}$ with $y^{(i)}$ the label of ${\overline{x}}_{i}$, and $\mathcal{L}$ is a given loss such as the squared loss or the logistic loss (see Appendix D.1).

### Unsupervised learning

In unsupervised learning tasks the labels are unknown. The objective itself is defined through a minimization problem rather than through an explicit loss function. For example, a convex clustering objective is written

We consider in Appendix D.2 different clustering objectives. Note that classical ones, such as the one of $k$-means or spectral clustering, are inherently non-smooth, i.e., non-continuously differentiable.

### Layer decomposition

The $t$^th^ layer of a deep network can be described by the following components:

a bi-affine operation such as a matrix multiplication or a convolution, denoted $b_{t}:{{{\mathbb{R}}^{d_{t - 1}} \times {\mathbb{R}}^{p_{t}}}\rightarrow{\mathbb{R}}^{\eta_{t}}}$ and decomposed as

where $\beta_{t}$ is bilinear, $\beta_{t}^{u}$ and $\beta_{t}^{x}$ are linear and $\beta_{t}^{0}$ is a constant vector,

an activation function, such as the element-wise application of a non-linear function, denoted $\alpha_{t}:{{\mathbb{R}}^{\eta_{t}}\rightarrow{\mathbb{R}}^{\eta_{t}}}$,

a reduction of dimension, such as a pooling operation, denoted $\pi_{t}:{{\mathbb{R}}^{\eta_{t}}\rightarrow{\mathbb{R}}^{d_{t}}}$,

a normalization of the output, such as batch-normalization, denoted $\nu_{t}:{{\mathbb{R}}^{d_{t}}\rightarrow{\mathbb{R}}^{d_{t}}}$.

By concatenating the non-affine operations, i.e., defining $a_{t} = {\nu_{t} \circ \pi_{t} \circ \alpha_{t}}$, a layer can be written as

Note that some components may not be included, for example some layers do not include normalization. In the following, we consider the non-linear operation $a_{t}$ to be an arbitrary composition of functions, i.e., $a_{t} = {a_{t,k_{t}} \circ \ldots \circ a_{t,1}}$. We present common examples of the components of a deep network.

### Linear operations

In the following, we drop the dependency w.r.t. the layer $t$ and denote by a tilde $\overset{\sim}{\cdot}$ the quantities characterizing the output. We denote by semi-columns the concatenations of matrices by rows, i.e., for ${A \in {\mathbb{R}}^{d \times n}},{B \in {\mathbb{R}}^{q \times n}}$, ${(A;B)} = {(A^{\top},B^{\top})}^{\top}$.

### Fully connected layer

A *fully connected* layer taking an input of dimension $\delta$ is written

where $z \in {\mathbb{R}}^{\delta}$ is the input, $W \in {\mathbb{R}}^{\delta \times \overset{\sim}{\delta}}$ are the weights of the layer and $w^{0} \in {\mathbb{R}}^{\overset{\sim}{\delta}}$ define the intercepts. By vectorizing the parameters and the inputs, a fully connected layer can be written as

### Convolutional layer

A *convolutional* layer convolves an input (images or signals) of dimension $\delta$ denoted $z \in {\mathbb{R}}^{\delta}$ with $n^{f}$ affine filters of size $s^{f}$ defined by weights $W = {(w_{1},\ldots,w_{n^{f}})} \in {\mathbb{R}}^{s^{f} \times n^{f}}$ and intercepts $w^{0} = {(w_{1}^{0},\ldots,w_{n^{f}}^{0})} \in {\mathbb{R}}^{n^{f}}$ through $n^{p}$ patches. The $k$^th^ output of the convolution of the input by the $j$^th^ filter reads

where $\Pi_{k} \in {\mathbb{R}}^{s^{f} \times \delta}$ extracts a patch of size $s^{f}$ at a given position of the input $z$. The output $\overset{\sim}{z}$ is then given by the concatenation ${\overset{\sim}{z}}_{k + {n^{p}{({j - 1})}}} = \Xi_{j,k}$. By vectorizing the inputs and the outputs, the convolution operation is defined by a set of matrices ${(\Pi_{k})}_{k = 1}^{n^{p}}$ such that

### Activation functions

We consider element-wise activation functions $\alpha:{{\mathbb{R}}^{\eta}\rightarrow{\mathbb{R}}^{\eta}}$ such that for a given $x = {(x_{1},\ldots,x_{\eta})} \in {\mathbb{R}}^{\eta}$,

for a given scalar function $\overline{\alpha}$ such as ${\overline{\alpha}{(x)}} = {\max{(x,0)}}$ for the Rectified Linear Unit (ReLU) or ${\overline{\alpha}{(x)}} = {({1 + {\exp{({- x})}}})}^{- 1}$ for the sigmoid function.

### Pooling functions

A pooling layer reduces the dimension of the output. For example, an average pooling convolves an input image with a mean filter. Formally, for an input $z \in {\mathbb{R}}^{\delta}$, the average pooling with a patch size $s^{f}$ for inputs with $n^{f}$ channels and $n^{p}$ coordinates such that $\delta = {n^{f}n^{p}}$ convolves the input with a filter $P = {\mathbf{1}_{s^{f}}{\mathbf{1}_{n^{f}}^{\top}/s^{f}}}$. The output dimension for each input is $\overset{\sim}{\delta} = {n^{f}{\overset{\sim}{n}}^{p}}$ and the patches, represented by some ${(\Pi_{k})}_{k = 1}^{\overset{\sim}{n^{p}}}$ acting in Eq., are chosen such that it induces a reduction of dimension, i.e., $\overset{\sim}{n^{p}} \leq n^{p}$.

### Normalization functions

Given a batch of input $Z \in {\mathbb{R}}^{\delta \times m}$ the batch-normalization outputs $\overset{\sim}{Z}$ defined by

with $\epsilon > 0$, such that the vectorized formulation of the batch-normalization reads ${\nu{(x)}} = {{Vec}{(\overset{\sim}{Z})}}$ for $x = {{Vec}{(Z)}}$.

### Specific structures

### Auto-encoders

An auto-encoder seeks to learn a compact representation of some data $\overline{x} \in {\mathbb{R}}^{d}$ by passing it through an encoder network with output dimension $\hat{d} \ll d$ then a decoder network with output dimension $d$ with the objective that the final output is close to the original input. Each network can be represented by a chain of computations. Given $n$ data points $\overline{x} = {({\overline{x}}^{}:\ldots;{\overline{x}}^{(n)})}$, denoting $f^{e}$ the encoder with parameters $u_{e}$ such that $f_{u_{e}}^{e}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{\hat{d}}}$ and $f^{d}$ the decoder with parameters $u_{d}$ such that $f_{u_{d}}^{d}:{{\mathbb{R}}^{\hat{d}}\rightarrow{\mathbb{R}}^{d}}$, the objective is

The composition of the encoder and the decoder form a chain of computations such that the overall objective can be written as in as detailed in Appendix 2.3. Formally, denoting $f^{0}:{{x_{0},u}\rightarrow{f^{d}{({f^{e}{(x_{0},u_{e})}},u_{d})}}}$ for $u = {(u_{d};u_{e})}$ the resulting chain of computations on a single input and $f{(\overline{x},u)} = {(f^{0}{({\overline{x}}^{},u)};\ldots;f^{0}{({\overline{x}}^{(n)},u)}}$ the concatenation of the outputs applied to the set of inputs, the objective of an auto-encoder has the form $h{({f{(\overline{x},u)}})}$ with ${h{(\hat{x})}} = {\frac{1}{n}{\sum_{i = 1}^{n}{\|{{\overline{x}}_{i} - {\hat{x}}_{i}}\|}_{2}^{2}}}$.

### Dense, highway or residual networks

Dense networks use not only the last input but all previous ones. The output of such networks can be described as

where $v_{t} = {(u_{t,0};{\ldotsu_{t,{t - 1}}})}$ are the parameters of the layer dispatched with one set of parameters per previous state and $v = {(v_{1};\ldots;v_{\tau})}$. The dynamics can be described as previously as ${\phi_{t}{(x_{0:{t - 1}},v_{t})}} = {a_{t}{({b_{t}{(x_{0:{t - 1}},v_{t})}})}}$. The bilinear operation $b_{t}$ is still a matrix multiplication or a convolution as previously presented except that it incorporates more variables. The non-linear operation $a_{t}$ is also the same, i.e., it incorporates an activation function and, potentially, a pooling operation and a normalization operation.

Dense networks can naturally be translated as a single input-output transformation by defining layers of the form

and ${f_{\tau}{(x_{0},v)}} = {E_{\tau}x_{0:\tau}} = x_{\tau}$ where $E_{\tau}$ is a linear projector that extracts $x_{\tau}$ from $x_{0:\tau}$.

Highway networks are dense networks that consider only the last input and the penultimate one, i.e., they are of the form except that they propagate only $x_{{t - 1}:t} = {(x_{t - 1},x_{t})}$. Namely they are defined by

with $v_{t} = {(u_{t,{t - 2}};u_{t,{t - 1}})}$. Finally, residual networks are highway networks with fixed parameters acting on the penultimate input. In the simple case where the current and penultimate inputs have the same dimension, they read

with $x_{- 1} = 0$, where $b_{t}$ and $a_{t}$ are of the forms described above. This amounts to define layers $\psi_{t}$ on $x_{{t - 2}:{t - 1}}$ whose bi-affine operation ${\overset{\sim}{b}}_{t}{(x_{{t - 2}:{t - 1}},u_{t})}$ has a non-zero affine term ${\overset{\sim}{\beta}}_{t}^{x}$ on $x_{{t - 2}:{t - 1}} = {(x_{t - 2};x_{t - 1})}$, see Appendix D.8.

### Implicit functions

We consider implicit functions that take the form

where $\zeta$ is twice differentiable and $\zeta{(\alpha, \cdot )}$ is strongly convex for any $\alpha$ such that $g{(\alpha)}$ is uniquely defined. These can be used either in the objective as seen before with clustering tasks, in that case $\alpha = x_{\tau}$. These can also be used in the layers such that $\alpha = {(x,u)}$ and ${\phi{(x,u)}} = {{{\arg\min}_{\beta \in {\mathbb{R}}^{b}}\zeta}{(x,u,\beta)}}$.

If the minimizer is computed exactly, we can compute the gradient by invoking the implicit function theorem. Formally, denoting ${\xi{(\alpha,\beta)}} = {{\nabla_{\beta}\zeta}{(\alpha,\beta)}}$, the function $g{(\alpha)}$ is defined by the implicit equation ${\xi{(\alpha,{g{(\alpha)}})}} = 0$ and its gradient is given by

The smoothness constants of this layer for exact minimizations are provided in Appendix D.9.

If the minimizer is computed approximately through an algorithm, its derivative can be computed by using automatic differentiation through the chain of computations defining the algorithm (see Subsection 3.2 for a detailed explanation of automatic differentiation). Alternatively, an approximate gradient can be computed by using the above formula. The resulting approximation error of the gradient is given by the following lemma.

### Lemma 2.2

Let $\zeta:{{(\alpha,\beta)}\rightarrow{\zeta{(\alpha,\beta)}} \in {\mathbb{R}}}$ for ${\alpha \in {\mathbb{R}}^{a}},{\beta \in {\mathbb{R}}^{b}}$ be s.t. $\zeta{(\alpha, \cdot )}$ is $\mu_{\zeta}$-strongly convex for any $\alpha$ and denote ${\xi{(\alpha,\beta)}} = {{\nabla_{\beta}\zeta}{(\alpha,\beta)}}$. Denote ${g{(\alpha)}} = {{{\arg\min}_{\beta \in {\mathbb{R}}^{b}}\zeta}{(\alpha,\beta)}}$ and ${\hat{g}{(\alpha)}} \approx {{{\arg\min}_{\beta \in {\mathbb{R}}^{b}}\zeta}{(\alpha,\beta)}}$ be an approximate minimizer. Provided that $\zeta$ has a $L_{\zeta}$-Lipschitz gradient and a $H_{\zeta}$-Lipschitz Hessian, the approximation error of using

instead of ${\nabla g}{(\alpha)}$ is bounded as

## Oracle arithmetic complexity

For each class of optimization algorithm considered (gradient descent, Gauss-Newton, Newton), we define the appropriate optimization oracle called at each step of the optimization algorithm which can be efficiently computed through a dynamic programming procedure. For a gradient step, we retrieve the gradient back-propagation algorithm. The gradient back-propagation algorithm forms then the basis of automatic-differentiation procedures.

### Oracle reformulations

In the following, we use the notations presented in Sec. A for gradients, Hessians and tensors. Briefly, ${\nabla f}{(x)}$ is used to denote the gradient of a function $f$ at $x$, which, if $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{d}}$ is multivariate, is the transpose of the Jacobian, i.e., ${{\nabla f}{(x)}} \in {\mathbb{R}}^{p \times d}$. For a multivariate function $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{d}}$, its second order information at $x$ is represented by a tensor ${{\nabla^{2}f}{(x)}} \in {\mathbb{R}}^{p \times p \times d}$, and we denote for example $\nabla^{2}f{(x)}{\lbrack y,y, \cdot \rbrack} = {(y^{\top}\nabla^{2}f^{}{(x)})}y;\ldots;y^{\top}\nabla^{2}f^{(n)}{(x)}y) \in {\mathbb{R}}^{d}$. For a function $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{d}}$, we define, provided that ${\nabla f}{(x)}$, ${\nabla f^{2}}{(x)}$ are defined,

such that the linear and quadratic approximations of $f$ around $x$ are ${f{({x + y})}} \approx {{f{(x)}} + {\ell_{f}^{x}{(y)}}}$ and ${f{({x + y})}} \approx {{f{(x)}} + {q_{f}^{x}{(y)}}}$ respectively.

We consider optimization oracles as procedures that compute either the next step of an optimization method or a decent direction along which the next step of an optimization method is taken. Formally, the optimization oracles for an objective $f$ are defined by a model $m_{f}^{u}$ that approximates the objective around the current point $u$ as ${f{({u + v})}} \approx {{f{(u)}} + {m_{f}^{u}{(v)}}}$. The models can be minimized with an additional proximal term that ensures that the minimizer lies in a region where the model approximates well the objective as

The parameter $\gamma$ acts as a stepsize that controls how large should be the step (the smaller the $\gamma$, the smaller the $v_{\gamma}^{\ast}$). Alternatively the model can be minimized directly providing a descent direction along which the next iterate is taken as

where $\gamma$ is found by a line-search using e.g. an Armijo condition.

On a point $u \in {\mathbb{R}}^{p}$, given a regularization $\kappa$, for an objective of the form ${{h \circ \psi} + r}:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}}$,

a *gradient* oracle is defined as

a (regularized) *Gauss-Newton* oracle is defined as

a (regularized) *Newton* oracle is defined as

### Proposition 3.1

Let $f$ be a chain of $\tau$ computations $\phi_{t}:{{{\mathbb{R}}^{d_{t - 1}} \times {\mathbb{R}}^{p_{t}}}\rightarrow{\mathbb{R}}^{d_{t}}}$, $u = {(u_{1};\ldots;u_{\tau})}$ and $x_{0} \in {\mathbb{R}}^{d_{0}}$. Denote $\psi = f_{x_{0},\tau}$ and ${f{(x_{0},u)}} = {(x_{1};\ldots;x_{\tau})}$. Assume $r$ to be decomposable as ${r{(u)}} = {\sum_{t = 1}^{\tau}{r_{t}{(u_{t})}}}$. Gradient (15 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")), Gauss-Newton (16 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")) and Newton oracles on ${h \circ \psi} + r$ are the solutions $v^{\ast} = {(v_{1}^{\ast};\ldots;v_{\tau}^{\ast})}$ of problems of the form

for gradient oracles (15 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")),

for Gauss-Newton oracles (16 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")),

for Newton oracles, defining

Problems of the form

can be decomposed into nested subproblems defined as the cost-to-go from ${\hat{x}}_{t}$ at time $t$ by

such that they follow the recursive relation

This principle cannot be used directly on the original problem, since Eq. cannot be solved analytically for generic problems of the form. However, for quadratic problems with linear compositions of the form, this principle can be used to solve problems by dynamic programming. Therefore as a corollary of Prop. 3.1, the complexity of all optimization steps given in (15 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")), (16 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")), is linear w.r.t. to the length $\tau$ of the chain. Precisely, Prop. 3.1 shows that each optimization step amounts to reducing the complexity of the recursive relation to an analytic problem.

In particular, while the Hessian of the objective scales as $\sum_{t = 1}^{\tau}p_{t}$, a Newton step has a linear and not cubic complexity with respect to $\tau$. We present in Appendix B the detailed computation of a Newton step, alternative derivations were first proposed in the control literature. This involves the inversion of intermediate quadratic costs at each layer. Gauss-Newton steps can also be solved by dynamic programming and can be more efficiently implemented using an automatic-differentiation oracles as we explain below.

### Automatic differentiation

### Algorithm

As explained in last subsection and shown in Appendix B, a gradient step can naturally be derived as a dynamic programming procedure applied to the subproblem. However, the implementation of the gradient step provides itself a different kind of oracle on the chain of computations as defined below.

### Definition 3.2

Given a chain of computations $f:{{{\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}} \times {\mathbb{R}}^{d_{0}}}\rightarrow{\mathbb{R}}^{\sum_{t = 1}^{\tau}d_{t}}}$ as defined in Def. 2.1, $u \in {\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}}$ and $x_{0} \in {\mathbb{R}}^{d_{0}}$, an *automatic differentiation oracle* is a procedure that gives access to

The subtle difference is that *we have access to ${\nabla f_{x_{0},\tau}}{(u)}$ not as a matrix but as a linear operator*. The matrix ${\nabla f_{x_{0},\tau}}{(u)}$ can also be computed and stored to perform gradient vector products. Yet, this requires a surplus of storage and of computations that are generally not necessary for our purposes. The only quantities that need to be stored are given by the forward pass. Then, these quantities can be used to compute any gradient vector product directly.

The definition of an automatic differentiation oracle is composed of two steps:

a *forward* pass that computes $f_{x_{0},\tau}{(u)}$ and stores the information necessary to compute gradient-vector products.

the compilation of a *backward* pass that computes $\mu\rightarrow{{\nabla f_{x_{0},\tau}}{(u)}\mu}$ for any $\mu \in {\mathbb{R}}^{d_{\tau}}$ given the information collected in the forward pass.

Note that the two aforementioned passes are decorrelated in the sense that the forward pass does not require the knowledge of the slope $\mu$ for which ${\nabla f_{x_{0},\tau}}{(u)}\mu$ is computed.

We present in Algo. 1 and Algo. 2 the classical forward-backward passes used in modern automatic-differentiation libraries. The implementation of the automatic differentiation oracle as a procedure that computes both the value of the chain $f_{x_{0},\tau}{(u)}$ and the linear operator $\mu\rightarrow{f_{x_{0},\tau}{(u)}\mu}$ is then presented in Algo. 3 and illustrated in Fig. 2.

Computing the gradient $g = {{\nabla{({h \circ f_{x_{0},\tau}})}}{(u)}}$ on $u \in {\mathbb{R}}^{p}$ amounts then to

computing with Algo. 3, ${{f_{x_{0},\tau}{(u)}},\mu}\rightarrow{{\nabla f_{x_{0},\tau}}{(u)}\mu} = {{Autodiff}{(f,u)}}$,

computing $\mu = {{\nabla h}{({f_{x_{0},\tau}{(u)}})}}$ then $g = {{\nabla f_{x_{0},\tau}}{(u)}\mu}$.

1:Inputs: Chain of computations f defined by (ϕt)t = 1, …, τ, input x as in Def. 2.1, variable u = (u1;…;uτ)
Algorithm 1 Forward pass

1:Inputs: Slope μ, intermediate gradients ∇ϕt (xt − 1,ut) for t ∈ {1, …, τ}
Algorithm 2 Backward pass

1:Inputs: Chain of computations f defined by (ϕt)t = 1, …, τ, input x as in Def. 2.1, variable u = (u1;…;uτ)
2:Compute using Algo. 1 (xτ,(∇ϕt(xt − 1,ut)t = 1τ)=Forward(f,u) which gives fx0, τ (u) = xτ
3:Define μ → ∇fx0, τ (u) μ as μ → Backward(μ,(∇ϕt (xt − 1,ut))t = 1τ) according to Algo. 2.
Algorithm 3 Chain of computations with automatic-differentiation oracle (Autodiff)

Figure 2: Automatic differentiation of a chain of computations.

### Complexity

Without additional information on the structure of the layers, the space and time complexities of the forward-backward algorithm is of the order of

respectively, where $\mathcal{T}{(\phi_{t},{\nabla\phi_{t}})}$ is the time complexity of computing $\phi_{t},{\nabla\phi_{t}}$ during the backward pass. The units chosen are for the space complexity the cost of storing one digit and for the time complexity the cost of performing an addition or a multiplication.

Provided that for all $t \in {\{ 1,{\ldots\tau}\}}$,

where $\mathcal{T}{(\phi_{t})}$ is the time complexity of computing $\phi_{t}$ and $Q \geq 0$ is a constant, we get that

where $\mathcal{T}{(f)}$ is the complexity of computing the chain of computations. We retrieve Baur-Strassen's theorem which states that the complexity of computing the derivative of a function formulated as a chain of computations is of the order of the complexity of computing the function itself.

For chain of computations of the form, this cost can be refined as shown in Appendix B. Specifically, for a chain of fully-connected layers with element-wise activation function, no normalization or pooling, the cost of the backward pass is then of the order of $\mathcal{O}\left( {\sum_{t = 1}^{\tau}{2m\delta_{t}{({\delta_{t - 1} + 1})}}} \right)$ elementary operations. For a chain of convolutional layers with element-wise activation function, no normalization or pooling, the cost of the backward pass is of the order of $\mathcal{O}\left( {\sum_{t = 1}^{\tau}{{({{2n_{t}^{p}n_{t}^{f}s_{t}^{f}} + {n_{t}^{p}n_{t}^{f}} + \delta_{t}})}m}} \right)$ elementary operations.

### Gauss-Newton by automatic differentiation

The Gauss-Newton step can also be solved by making calls to an automatic differentiation oracle.

### Proposition 3.3

Consider the Gauss-Newton oracle (16 ‣ 3.1 Oracle reformulations ‣ 3 Oracle arithmetic complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks")) on $u = {(u_{1};\ldots;u_{\tau})}$ for a convex objective $h$, a convex decomposable regularization ${r{(u)}} = {\sum_{t = 1}^{\tau}{r_{t}{(u_{t})}}}$ and a differentiable chain of computations $f$ with output $\psi = f_{x_{0},\tau}$ on some input $x_{0}$. We have that

the Gauss-Newton oracle amounts to solving

where for a function $f$ we denote by $f^{\star}$ its convex conjugate,

the Gauss-Newton oracle is $v^{\ast} = \nabla\left( q_{r}^{u} + \kappa \parallel \cdot \parallel_{2}^{2}/2 \right)^{\star}{( - \nabla\psi{(u)}\mu^{\ast})}$ where $\mu^{\ast}$ is the solution of,

the dual problem can be solved by ${2d_{\tau}} + 1$ calls to an automatic differentiation procedure.

Proposition 3.3 shows that a Gauss-Newton step is only ${2d_{\tau}} + 1$ times more expansive than a gradient-step. Precisely, for a deep network with a supervised objective, we have $d_{\tau} = {nk}$ where $n$ is the number of samples and $k$ is the number of classes. A gradient step makes then one call to an automatic differentiation procedure to get the gradient of the batch and the Gauss-Newton method will then make ${2nk} + 1$ more calls. If mini-batch Gauss-Newton steps are considered then the cost reduces to ${2mk} + 1$ calls to an automatic differentiation oracle, where $m$ is the size of the mini-batch.

## Optimization complexity

We present smoothness properties with respect to the Euclidean norm $\parallel \cdot \parallel_{2}$, whose operator norm is denoted $\parallel \cdot \parallel_{2,2}$. In the following, for a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{n}}$ and a set $C \subset {{dom}f} \subset {\mathbb{R}}^{d}$, we denote by

a bound of $h$ on $C$, the Lipschitz-continuity parameter of $h$ on $C$, and the smoothness parameter of $h$ on $C$ (i.e., the Lipschitz-continuity parameter of its gradient if it exists), all with respect to $\parallel \cdot \parallel_{2}$. Note that if $x = {{Vec}{(X)}}$ for a given matrix $X$, ${\| x\|}_{2} = {\| X\|}_{F}$. We denote by $m_{f},\ell_{f},L_{f}$ the same quantities defined on the domain of $f$, e.g., $m_{f} = m_{f}^{{dom}f}$. We denote by $\mathcal{C}_{m,\ell,L}$ the class of functions $f$ such that ${m_{f} = m},{{\ell_{f} = \ell},{L_{f} = L}}$. In the following, we allow the quantities $m_{f},\ell_{f},L_{f}$ to be infinite if for example the function is unbounded or the smoothness constant is not defined. The procedures presented below output infinite estimates if the combinations of the smoothness properties do not allow for finite estimates. On the other hand, they provide finite estimates automatically if they are available. In the following we denote ${\bigotimes_{t = 1}^{\tau}{B_{R_{t}}{({\mathbb{R}}^{p_{t}})}}} = {\{{u = {(u_{1};\ldots;u_{\tau})} \in {\mathbb{R}}^{\sum_{t = 1}^{\tau}p_{t}}}:{{u_{t} \in {\mathbb{R}}^{p_{t}}},{{\| u_{t}\|}_{2} \leq R_{t}}}\}}$.

### Convergence rate to a stationary point

We recall the convergence rate to a stationary point of a gradient descent and a stochastic gradient descent on constrained problems.

### Theorem 4.1 (8, Theorems 1 and 2)

Consider problems of the form

where $C$ is a closed convex set and $F$ is $L_{F}^{C}$ smooth on $C$. For problem (ii), consider that we have access to an unbiased estimate $\hat{\nabla}F{(u)}$ of ${\nabla F}{(u)}$ with a variance bounded as ${{\mathbb{E}}{({\|{{\hat{\nabla}F{(u)}} - {{\nabla F}{(u)}}}\|}_{2}^{2})}} \leq \sigma^{2}$.

A projected gradient descent applied on problem (i) with step-size $\gamma = {(L_{F}^{C})}^{- 1}$ converges to an $\varepsilon$-stationary point in at most

iterations, where $u_{0}$ is the initial point and $F^{\ast} = {{\min_{u \in C}F}{(u)}}$.

A stochastic projected gradient descent applied on problem $({ii})$ with step-size $\gamma = {({2L_{F}^{C}})}^{- 1}$ converges in expectation to an $({\varepsilon + \sigma})$-stationary point in at most

iterations, where $u_{0}$ is the initial point and $F^{\ast} = {{\min_{u \in C}F}{(u)}}$.

### Remarks

Since a gradient descent is monotonically decreasing, a gradient descent applied to the unconstrained problem converges to an $\varepsilon$-stationary point in at most

iterations, where $S_{0} = {\{{u \in {\mathbb{R}}^{p}}:{{F{(u)}} \leq {F{(u_{0})}}}\}}$ is the initial sub-level set.

Tighter rates of convergence can be obtained for the finite-sum problem (ii) by using variance reduction methods and by varying mini-batch sizes. They would then depend on the smoothness constants of the objective or the maximal smoothness of the components on $C$, i.e., $\max_{i = {1,\ldots,n}}L_{{h_{i} \circ \psi_{i}} + r}^{C}$.

The smoothness of the objectives $F$ defined in Theorem 4.1. ‣ 4.1 Convergence rate to a stationary point ‣ 4 Optimization complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks") can be derived from the smoothness properties of their components.

### Proposition 4.2

Consider a closed convex set $C \subset {\mathbb{R}}^{p}$, $\psi \in \mathcal{C}_{m_{\psi}^{C},\ell_{\psi}^{C},L_{\psi}^{C}}^{C}$, $r \in \mathcal{C}_{L_{r}}$ and $h \in \mathcal{C}_{\ell_{h},L_{h}}$ with $\ell_{h} = {+ \infty}$ if $h$ is not Lipschitz-continuous. The smoothness of $F = {{h \circ \psi} + r}$ on $C$ is bounded as

where ${\overset{\sim}{\ell}}_{h}^{C} = {\min{\{\ell_{h},{{\min_{z \in {\psi{(C)}}}{\|{{\nabla h}{(z)}}\|}_{2}} + {L_{h}\ell_{\psi}^{C}D^{C}}}\}}}$, where $D^{C} = {\sup_{{x,y} \in C}{\|{x - y}\|}_{2}}$.

What remain to characterize are the smoothness properties of a chain of computations.

### Smoothness estimates

We present the smoothness computations for a deep network. Generic estimations of the smoothness properties of a chain of computation are presented in Appendix C. The propositions below give *upper bounds* on the smoothness constants of the function achieved through chain-composition. For a trivial composition such as $f \circ f^{- 1}$, the upper bound is clearly loose. The upper bounds we present here are informative for non-trivial architectures.

The estimation is done by a forward pass on the network, as illustrated in Fig. 3. The reasoning is based on the following lemma.

### Lemma 4.3

Consider a chain $f$ of $\tau$ computations $\phi_{t} \in \mathcal{C}_{\ell_{\phi_{t}},L_{\phi_{t}}}$ initialized at some $x_{0} \in {\mathbb{R}}^{d_{0}}$.

We have $\ell_{f_{\tau,x_{0}}} \leq \ell_{\tau}$, where

We have $L_{f_{\tau,x_{0}}} \leq L_{\tau}$, where

In the case of deep networks, the computations are not Lipschitz continuous due to the presence of bi-affine functions. Yet, provided that inputs of computations are bounded and that we have access to the smoothness of the computations, we can have an estimate of the Lipschitz-continuity of the computations restricted to these bounded sets.

### Corollary 4.4

Consider a chain $f$ of $\tau$ of computations $\phi_{t} \in \mathcal{C}_{m_{\phi_{t}},\ell_{\phi_{t}},L_{\phi_{t}}}$ initialized at some $x_{0} \in {\mathbb{R}}^{d_{0}}$ and consider $C = {\bigotimes_{t = 1}^{\tau}{B_{R_{t}}{({\mathbb{R}}^{p_{t}})}}}$. Then the smoothness of the output of the chain $f_{\tau,x_{0}}$ on $C$, can be estimated as in Lemma 4.3 by replacing $\ell_{\phi_{t}}$ with ${\overset{\sim}{\ell}}_{\phi_{t}}$ defined by

for $t \in {\{ 1,\ldots,\tau\}}$, with $m_{0} = {\| x_{0}\|}_{2}$.

Chain of computations f defined by ϕt = at ∘ bt for t ∈ {1, …, τ} with at = at, kt ∘ … ∘ at, 1
Smoothness properties Lbt, lbtu, lbtx of the biaffine function bt ∈ ℬLbt, lbtu, lbtx
Smoothness properties mat, i, ℓat, i, Lat, i of the nonlinear functions at, i ∈ 𝒞mat, i, ℓat, i, Lat, i
Bounds Rt on the parameters

4: ℓt, 0x = Lbt Rt + lbtx, ℓt, 0u = Lbt mt − 1 + lbtu, ℓt, 00 = 1
10: $\ell_{t,j}^{0} = {{\overset{\sim}{\ell}}_{a_{t,j}}\ell_{t,{j - 1}}^{0}}$
15: Lt = Lt − 1 ℓt, 0x ℓt, kt0 + (Lbt Rt+lbt)2 Lt, kt ℓt − 12 + 2 ((Lbt mt − 1+lbtu) (Lbt Rt+lbtx) Lt, kt+Lbt ℓt, kt0) ℓt − 1 + (Lbt mt − 1+lbtu)2 Lt, kt
Algorithm 4 Automatic smoothness computations

Figure 3: Smoothness estimates computations.

We specialize the result to deep networks. We denote by $\mathcal{B}_{L,l^{u},l^{x}}$ the set of $L$-smooth bi-affine functions $b$ such that ${\|{{\nabla_{u}b}{}}\|}_{2,2} = l^{u}$, ${\|{{\nabla_{x}b}{}}\|}_{2,2} = l^{x}$, i.e., functions of the form

with $\beta$ bilinear and $L$-smooth, $\beta^{u}$, $\beta^{x}$ linear and $l^{u}$, $l^{x}$ Lipschitz continuous respectively and $\beta^{0}$ a constant vector.

### Proposition 4.5

Consider a chain $f$ of $\tau$ computations whose layers $\phi_{t}$ are defined by

for $t \in {\{ 1,\ldots,\tau\}}$, where $b_{t} \in \mathcal{B}_{L_{b_{t}},l_{b_{t}}^{u},l_{b_{t}}^{x}}$, and $a_{t}$ is decomposed as

with $a_{t,i} \in \mathcal{C}_{m_{a_{t,i}},\ell_{a_{t,i}},L_{a_{t,i}}}$. Consider $C = {\bigotimes_{t = 1}^{\tau}{B_{R_{t}}{({\mathbb{R}}^{p_{t}})}}}$. The outputs $m_{\tau}$, $\ell_{\tau}$ and $L_{\tau}$ of Algo. 4 satisfy $m_{f_{\tau,x_{0}}}^{C} \leq m_{\tau}$, $\ell_{f_{\tau,x_{0}}}^{C} \leq \ell_{\tau}$, $L_{f_{\tau,x_{0}}}^{C} \leq L_{\tau}$.

The proof of the above lemma is the consequence of simple technical lemmas provided in Appendix C. Note that the smoothness of the chain with respect to its input given a fixed set of parameters can also easily be estimated by a similar method; see Corollary C.5 in Appendix C.

The smoothness properties of a chain of composition around a given point follows then directly as stated in the following corollary.

### Corollary 4.6

Consider a chain $f$ of $\tau$ computations as defined in Prop. 4.5 and $u^{\ast} = {(u_{1}^{\ast};\ldots,u_{\tau}^{\ast})} \in {\mathbb{R}}^{p}$. The smoothness properties of $f$ on $C^{\prime} = {\{{u = {(u_{1};\ldots;u_{\tau})} \in {\mathbb{R}}^{p}}:{{{\forall t} \in {\{ 1,\ldots,\tau\}}},{{\|{u_{t} - u_{t}^{\ast}}\|} \leq R_{t}^{\prime}}}\}}$ are given as in Prop. 4.5 by considering

## Application

We apply our framework to assess the smoothness properties of the Visual Geometry Group (VGG) deep network used for image classification.

### VGG network

The VGG Network is a benchmark network for image classification with deep networks. The objective is to classify images among $1000$ classes. Its architecture is composed of 16 layers described in Appendix F. We consider in the following smoothness properties for mini-batches with size $m = 128$, i.e., by concatenating $m$ chains of computations $f^{(i)}$ each defined by a different input. This highlights the impact of the size of the mini-batch for batch-normalization.

### Smoothness computations

To compute the Lipschitz-continuity and smoothness parameters, we recall the list of Lipschitz continuity and smoothness constants of each layer of interest. For the bilinear and linear operations we denote by $L$ the smoothness of the bilinear operation $\beta$ and by $\ell$ the Lipschitz-continuity of the linear operation $\beta^{u}$. The smoothness constants of interest are

$\ell_{conv} = {\sqrt{m}\left\lceil \frac{k}{s} \right\rceil}$, $L_{conv} = \left\lceil \frac{k}{s} \right\rceil$, where the patch is of size $k \times k$ and the stride is $s$,

$\ell_{full} = \sqrt{m}$, $L_{full} = 1$,

$\ell_{ReLu} = 1$, $L_{ReLu}$ not defined,

$\ell_{softmax} = 2$, $L_{softmax} = 4$,

$\ell_{maxpool} = 1$, $L_{maxpool}$ not defined,

$\ell_{\log} = 2$, $L_{\log} = 2$.

A Lipschitz-continuity estimate of this architecture can then be computed using Prop. 4.5 on a Cartesian product of balls $C = {\{{w = {(u_{1};\ldots;u_{16})}}:{{\| u_{t}\|}_{2} \leq R}\}}$ for $R = 1$ for example.

### Variations of VGG

### Smooth VGG

First, the VGG architecture can be made continuously differentiable by considering the soft-plus activation instead of the ReLU activation and average pooling instead of the max-pooling operation. As shown in Appendix D, we have

$\ell_{avgpool} = 1$, $L_{avgpool} = 0$,

$\ell_{softplus} = 1$, $L_{softplus} = {1/4}$.

Denoting $\ell_{VGG}$ and $\ell_{{VGG} - {smooth}}$ the Lipschitz-continuity estimates of the original VGG network and the modified original network on a Cartesian product of balls $C = {\{{u = {(u_{1};\ldots;u_{16})}}:{{\| u_{t}\|}_{2} \leq 1}\}}$ with ${\| x\|}_{2} = 1$, we get using Prop. 4.5, ${\frac{|{\ell_{VGG} - \ell_{{VGG} - {smooth}}}|}{\ell_{VGG}} \leq 10^{- 4}}.$

### Batch-normalization effect

We can also compare the smoothness properties of the smoothed network with the same network modified by adding the batch-normalization layer for $m$ inputs and $\epsilon$ normalization parameter at each convolutional layer. As shown in Appendix D, the batch-normalization satisfies

$m_{batch} = {\deltam}$, $\ell_{batch} = {2\epsilon^{- {1/2}}}$, $L_{batch} = {2m^{- {1/2}}\epsilon^{- 1}}$.

Denoting $\ell_{{VGG} - {smooth}}$, $L_{{VGG} - {smooth}}$ and $\ell_{{VGG} - {batch}}$, $L_{{VGG} - {batch}}$ the Lipschitz-continuity and smoothness estimates of the smoothed VGG network with and without batch-normalization respectively on a Cartesian product of balls $C = {\{{u = {(u_{1};\ldots;u_{16})}}:{{\| u_{t}\|}_{2} \leq 1}\}}$ with ${\| x\|}_{2} = 1$, we get using Prop. 4.5,

Intuitively, the batch-norm bounds the output of each layer, mitigating the increase of $m_{t}$ in the computations of the estimates of the smoothness in lines 8 and 9 of Algo. 4. Yet, for a small $\epsilon$, this effect is balanced by the non-smoothness of the batch-norm layer (which for $\epsilon\rightarrow 0$ tends to have an infinite slope around 0).
