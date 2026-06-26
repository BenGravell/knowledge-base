<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an approach to obtain convergence guarantees of optimization algorithms for deep networks based on elementary arguments and computations. The convergence analysis revolves around the analytical and computational structures of optimization oracles central to the implementation of deep networks in machine learning software. We provide a systematic way to compute estimates of the smoothness constants that govern the convergence behavior of first-order optimization algorithms used to train deep networks. A diverse set of example components and architectures arising in modern deep networks intersperse the exposition to illustrate the approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep networks have achieved remarkable performance in several application domains such as computer vision, natural language processing and genomics. The input-output mapping implemented by a deep neural network is a chain of compositions of modules, where each module is typically a composition of a non-linear mapping, called an activation function, and an affine mapping. The last module in the chain is usually task-specific in that it relates to a performance accuracy for a specific task. This module can be expressed either explicitly in analytical form as in supervised classification or implicitly as a solution of an optimization problem as in dimension reduction or unsupervised clustering.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimization problem arising when training a deep network is often framed as a non-convex optimization problem, dismissing the structure of the objective yet central to the software implementation. Indeed optimization algorithms used to train deep networks proceed by making calls to first-order (or second-order) oracles relying on dynamic programming such as gradient back-propagation. Gradient back-propagation is now part of modern machine learning software. We highlight here the elementary yet important fact that the chain-compositional structure of the objective naturally emerges through the smoothness constants governing the convergence guarantee of a gradient-based optimization algorithm. This provides a reference frame to relate the network architecture and the convergence rate through the smoothness constants. This also brings to light the benefit of specific modules popular among practitioners to improve the convergence.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Sec. 2, we define the parameterized input-output map implemented by a deep network as a chain-composition of modules and write the corresponding optimization objective consisting in learning the parameters of this map. In Sec. 3, we detail the implementation of first-order and second-order oracles by dynamic programming; the classical gradient back-propagation algorithm is recovered as a canonical example. Gauss-Newton steps can also be simply stated in terms of calls to an automatic-differentiation oracle implemented in modern machine learning software libraries. In Sec. 4, we present the computation of the smoothness constants of a chain of computations given its components and the resulting convergence guarantees for gradient descent. Finally, in Sec. 5, we present the application of the approach to derive the smoothness constants for the VGG architecture and illustrate how our approach can be used to identify the benefits of batch-normalization. In the Appendix, we estimate the smoothness constants related to the VGG architecture and we investigate batch-normalization in the light of our approach. All the proofs and the notations are also provided in the Appendix.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Deep network architecture", "weight": 1.0} -->

A feed-forward deep network of depth $\tau$ can be described as a transformation of an input $x$ into an output $x_{\tau}$ through the composition of $\tau$ blocks, called layers, illustrated in Fig. 1. Each layer is defined by a set of parameters. In general, (see Sec. 2.3 for a detailed decomposition), these parameters act on the input of the layer through an affine operation followed by a non-linear operation. Formally, the $t$^th^ layer can be described as a function of its parameters $u_{t}$ and a given input $x_{t - 1}$ that outputs $x_{t}$ as where $b_{t}$ is generally linear in $u_{t}$ and affine in $x_{t - 1}$ and $a_{t}$ is non-linear.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Deep network architecture", "weight": 1.0} -->

Learning a deep network consists in minimizing w.r.t. its parameters an objective involving $n$ inputs ${{\overline{x}}^{},\ldots,{\overline{x}}^{(n)}} \in {\mathbb{R}}^{\delta}$. Formally, the problem is written where $u_{t} \in {\mathbb{R}}^{p_{t}}$ is the set of parameters at layer $t$ whose dimension $p_{t}$ can vary among layers and $r$ is a regularization on the parameters of the network.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Deep network architecture", "weight": 1.0} -->

We are interested in the influence of the architecture on the optimization complexity of the problem. The architecture translates into a structure of the chain of computations involved in the optimization problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Supervised learning", "weight": 1.0} -->

For supervised learning, the objective can be decomposed as a finite sum where $h^{(i)}$ are losses on the labels predicted by the chain of computations, i.e., ${h^{(i)}{({\hat{y}}^{(i)})}} = {\mathcal{L}{({\hat{y}}^{(i)},y^{(i)})}}$ with $y^{(i)}$ the label of ${\overline{x}}_{i}$, and $\mathcal{L}$ is a given loss such as the squared loss or the logistic loss (see Appendix D.1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Unsupervised learning", "weight": 1.0} -->

In unsupervised learning tasks the labels are unknown. The objective itself is defined through a minimization problem rather than through an explicit loss function. For example, a convex clustering objective is written We consider in Appendix D.2 different clustering objectives. Note that classical ones, such as the one of $k$-means or spectral clustering, are inherently non-smooth, i.e., non-continuously differentiable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Layer decomposition", "weight": 1.0} -->

By concatenating the non-affine operations, i.e., defining $a_{t} = {\nu_{t} \circ \pi_{t} \circ \alpha_{t}}$, a layer can be written as Note that some components may not be included, for example some layers do not include normalization. In the following, we consider the non-linear operation $a_{t}$ to be an arbitrary composition of functions, i.e., $a_{t} = {a_{t,k_{t}} \circ \ldots \circ a_{t,1}}$. We present common examples of the components of a deep network.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Linear operations", "weight": 1.0} -->

In the following, we drop the dependency w.r.t. the layer $t$ and denote by a tilde $\overset{\sim}{\cdot}$ the quantities characterizing the output. We denote by semi-columns the concatenations of matrices by rows, i.e., for ${A \in {\mathbb{R}}^{d \times n}},{B \in {\mathbb{R}}^{q \times n}}$, ${(A;B)} = {(A^{\top},B^{\top})}^{\top}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Fully connected layer", "weight": 1.0} -->

A *fully connected* layer taking an input of dimension $\delta$ is written where $z \in {\mathbb{R}}^{\delta}$ is the input, $W \in {\mathbb{R}}^{\delta \times \overset{\sim}{\delta}}$ are the weights of the layer and $w^{0} \in {\mathbb{R}}^{\overset{\sim}{\delta}}$ define the intercepts. By vectorizing the parameters and the inputs, a fully connected layer can be written as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Pooling functions", "weight": 1.0} -->

A pooling layer reduces the dimension of the output. For example, an average pooling convolves an input image with a mean filter. Formally, for an input $z \in {\mathbb{R}}^{\delta}$, the average pooling with a patch size $s^{f}$ for inputs with $n^{f}$ channels and $n^{p}$ coordinates such that $\delta = {n^{f}n^{p}}$ convolves the input with a filter $P = {\mathbf{1}_{s^{f}}{\mathbf{1}_{n^{f}}^{\top}/s^{f}}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Normalization functions", "weight": 1.0} -->

Given a batch of input $Z \in {\mathbb{R}}^{\delta \times m}$ the batch-normalization outputs $\overset{\sim}{Z}$ defined by with $\epsilon > 0$, such that the vectorized formulation of the batch-normalization reads ${\nu{(x)}} = {{Vec}{(\overset{\sim}{Z})}}$ for $x = {{Vec}{(Z)}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dense, highway or residual networks", "weight": 1.0} -->

Dense networks use not only the last input but all previous ones. The output of such networks can be described as where $v_{t} = {(u_{t,0};{\ldotsu_{t,{t - 1}}})}$ are the parameters of the layer dispatched with one set of parameters per previous state and $v = {(v_{1};\ldots;v_{\tau})}$. The dynamics can be described as previously as ${\phi_{t}{(x_{0:{t - 1}},v_{t})}} = {a_{t}{({b_{t}{(x_{0:{t - 1}},v_{t})}})}}$. The bilinear operation $b_{t}$ is still a matrix multiplication or a convolution as previously presented except that it incorporates more variables. The non-linear operation $a_{t}$ is also the same, i.e., it incorporates an activation function and, potentially, a pooling operation and a normalization operation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dense, highway or residual networks", "weight": 1.0} -->

Dense networks can naturally be translated as a single input-output transformation by defining layers of the form and ${f_{\tau}{(x_{0},v)}} = {E_{\tau}x_{0:\tau}} = x_{\tau}$ where $E_{\tau}$ is a linear projector that extracts $x_{\tau}$ from $x_{0:\tau}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dense, highway or residual networks", "weight": 1.0} -->

Highway networks are dense networks that consider only the last input and the penultimate one, i.e., they are of the form except that they propagate only $x_{{t - 1}:t} = {(x_{t - 1},x_{t})}$. Namely they are defined by with $v_{t} = {(u_{t,{t - 2}};u_{t,{t - 1}})}$. Finally, residual networks are highway networks with fixed parameters acting on the penultimate input. In the simple case where the current and penultimate inputs have the same dimension, they read with $x_{- 1} = 0$, where $b_{t}$ and $a_{t}$ are of the forms described above.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Implicit functions", "weight": 1.0} -->

We consider implicit functions that take the form where $\zeta$ is twice differentiable and $\zeta{(\alpha, \cdot)}$ is strongly convex for any $\alpha$ such that $g{(\alpha)}$ is uniquely defined. These can be used either in the objective as seen before with clustering tasks, in that case $\alpha = x_{\tau}$. These can also be used in the layers such that $\alpha = {(x,u)}$ and ${\phi{(x,u)}} = {{{\arg\min}_{\beta \in {\mathbb{R}}^{b}}\zeta}{(x,u,\beta)}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Implicit functions", "weight": 1.0} -->

If the minimizer is computed exactly, we can compute the gradient by invoking the implicit function theorem. Formally, denoting ${\xi{(\alpha,\beta)}} = {{\nabla_{\beta}\zeta}{(\alpha,\beta)}}$, the function $g{(\alpha)}$ is defined by the implicit equation ${\xi{(\alpha,{g{(\alpha)}})}} = 0$ and its gradient is given by The smoothness constants of this layer for exact minimizations are provided in Appendix D.9.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Implicit functions", "weight": 1.0} -->

If the minimizer is computed approximately through an algorithm, its derivative can be computed by using automatic differentiation through the chain of computations defining the algorithm (see Subsection 3.2 for a detailed explanation of automatic differentiation). Alternatively, an approximate gradient can be computed by using the above formula. The resulting approximation error of the gradient is given by the following lemma.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Oracle arithmetic complexity", "weight": 1.0} -->

For each class of optimization algorithm considered (gradient descent, Gauss-Newton, Newton), we define the appropriate optimization oracle called at each step of the optimization algorithm which can be efficiently computed through a dynamic programming procedure. For a gradient step, we retrieve the gradient back-propagation algorithm. The gradient back-propagation algorithm forms then the basis of automatic-differentiation procedures.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Oracle reformulations", "weight": 1.0} -->

We consider optimization oracles as procedures that compute either the next step of an optimization method or a decent direction along which the next step of an optimization method is taken. Formally, the optimization oracles for an objective $f$ are defined by a model $m_{f}^{u}$ that approximates the objective around the current point $u$ as ${f{({u + v})}} \approx {{f{(u)}} + {m_{f}^{u}{(v)}}}$. The models can be minimized with an additional proximal term that ensures that the minimizer lies in a region where the model approximates well the objective as The parameter $\gamma$ acts as a stepsize that controls how large should be the step (the smaller the $\gamma$, the smaller the $v_{\gamma}^{\ast}$). Alternatively the model can be minimized directly providing a descent direction along which the next iterate is taken as where $\gamma$ is found by a line-search using e.g. an Armijo condition.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Oracle reformulations", "weight": 1.0} -->

On a point $u \in {\mathbb{R}}^{p}$, given a regularization $\kappa$, for an objective of the form ${{h \circ \psi} + r}:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}}$, a *gradient* oracle is defined as a (regularized) *Gauss-Newton* oracle is defined as a (regularized) *Newton* oracle is defined as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm", "weight": 1.0} -->

As explained in last subsection and shown in Appendix B, a gradient step can naturally be derived as a dynamic programming procedure applied to the subproblem. However, the implementation of the gradient step provides itself a different kind of oracle on the chain of computations as defined below.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Complexity", "weight": 1.0} -->

Without additional information on the structure of the layers, the space and time complexities of the forward-backward algorithm is of the order of respectively, where $\mathcal{T}{(\phi_{t},{\nabla\phi_{t}})}$ is the time complexity of computing $\phi_{t},{\nabla\phi_{t}}$ during the backward pass. The units chosen are for the space complexity the cost of storing one digit and for the time complexity the cost of performing an addition or a multiplication.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Complexity", "weight": 1.0} -->

Provided that for all $t \in {\{ 1,{\ldots\tau}\}}$, where $\mathcal{T}{(\phi_{t})}$ is the time complexity of computing $\phi_{t}$ and $Q \geq 0$ is a constant, we get that where $\mathcal{T}{(f)}$ is the complexity of computing the chain of computations. We retrieve Baur-Strassen's theorem which states that the complexity of computing the derivative of a function formulated as a chain of computations is of the order of the complexity of computing the function itself.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Complexity", "weight": 1.0} -->

For chain of computations of the form, this cost can be refined as shown in Appendix B. Specifically, for a chain of fully-connected layers with element-wise activation function, no normalization or pooling, the cost of the backward pass is then of the order of $\mathcal{O}\left( {\sum_{t = 1}^{\tau}{2m\delta_{t}{({\delta_{t - 1} + 1})}}} \right)$ elementary operations. For a chain of convolutional layers with element-wise activation function, no normalization or pooling, the cost of the backward pass is of the order of $\mathcal{O}\left( {\sum_{t = 1}^{\tau}{{({{2n_{t}^{p}n_{t}^{f}s_{t}^{f}} + {n_{t}^{p}n_{t}^{f}} + \delta_{t}})}m}} \right)$ elementary operations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Gauss-Newton by automatic differentiation", "weight": 1.0} -->

The Gauss-Newton step can also be solved by making calls to an automatic differentiation oracle.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimization complexity", "weight": 1.0} -->

We present smoothness properties with respect to the Euclidean norm $\parallel \cdot \parallel_{2}$, whose operator norm is denoted $\parallel \cdot \parallel_{2,2}$. In the following, for a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{n}}$ and a set $C \subset {{dom}f} \subset {\mathbb{R}}^{d}$, we denote by a bound of $h$ on $C$, the Lipschitz-continuity parameter of $h$ on $C$, and the smoothness parameter of $h$ on $C$ (i.e., the Lipschitz-continuity parameter of its gradient if it exists), all with respect to $\parallel \cdot \parallel_{2}$. Note that if $x = {{Vec}{(X)}}$ for a given matrix $X$, ${\| x\|}_{2} = {\| X\|}_{F}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimization complexity", "weight": 1.0} -->

We denote by $m_{f},\ell_{f},L_{f}$ the same quantities defined on the domain of $f$, e.g., $m_{f} = m_{f}^{{dom}f}$. We denote by $\mathcal{C}_{m,\ell,L}$ the class of functions $f$ such that ${m_{f} = m},{{\ell_{f} = \ell},{L_{f} = L}}$. In the following, we allow the quantities $m_{f},\ell_{f},L_{f}$ to be infinite if for example the function is unbounded or the smoothness constant is not defined. The procedures presented below output infinite estimates if the combinations of the smoothness properties do not allow for finite estimates. On the other hand, they provide finite estimates automatically if they are available.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergence rate to a stationary point", "weight": 1.0} -->

We recall the convergence rate to a stationary point of a gradient descent and a stochastic gradient descent on constrained problems.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remarks", "weight": 1.0} -->

Since a gradient descent is monotonically decreasing, a gradient descent applied to the unconstrained problem converges to an $\varepsilon$-stationary point in at most iterations, where $S_{0} = {\{{u \in {\mathbb{R}}^{p}}:{{F{(u)}} \leq {F{(u_{0})}}}\}}$ is the initial sub-level set.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remarks", "weight": 1.0} -->

Tighter rates of convergence can be obtained for the finite-sum problem (ii) by using variance reduction methods and by varying mini-batch sizes. They would then depend on the smoothness constants of the objective or the maximal smoothness of the components on $C$, i.e., $\max_{i = {1,\ldots,n}}L_{{h_{i} \circ \psi_{i}} + r}^{C}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remarks", "weight": 1.0} -->

The smoothness of the objectives $F$ defined in Theorem 4.1. ‣ 4.1 Convergence rate to a stationary point ‣ 4 Optimization complexity ‣ An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks") can be derived from the smoothness properties of their components.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Smoothness estimates", "weight": 1.0} -->

We present the smoothness computations for a deep network. Generic estimations of the smoothness properties of a chain of computation are presented in Appendix C. The propositions below give *upper bounds* on the smoothness constants of the function achieved through chain-composition. For a trivial composition such as $f \circ f^{- 1}$, the upper bound is clearly loose. The upper bounds we present here are informative for non-trivial architectures.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Smoothness estimates", "weight": 1.0} -->

The estimation is done by a forward pass on the network, as illustrated in Fig. 3. The reasoning is based on the following lemma.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Application", "weight": 1.0} -->

We apply our framework to assess the smoothness properties of the Visual Geometry Group (VGG) deep network used for image classification.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VGG network", "weight": 1.0} -->

The VGG Network is a benchmark network for image classification with deep networks. The objective is to classify images among $1000$ classes. Its architecture is composed of 16 layers described in Appendix F. We consider in the following smoothness properties for mini-batches with size $m = 128$, i.e., by concatenating $m$ chains of computations $f^{(i)}$ each defined by a different input. This highlights the impact of the size of the mini-batch for batch-normalization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Smoothness computations", "weight": 1.0} -->

To compute the Lipschitz-continuity and smoothness parameters, we recall the list of Lipschitz continuity and smoothness constants of each layer of interest. For the bilinear and linear operations we denote by $L$ the smoothness of the bilinear operation $\beta$ and by $\ell$ the Lipschitz-continuity of the linear operation $\beta^{u}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Smoothness computations", "weight": 1.0} -->

A Lipschitz-continuity estimate of this architecture can then be computed using Prop. 4.5 on a Cartesian product of balls $C = {\{{w = {(u_{1};\ldots;u_{16})}}:{{\| u_{t}\|}_{2} \leq R}\}}$ for $R = 1$ for example.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Smooth VGG", "weight": 1.0} -->

First, the VGG architecture can be made continuously differentiable by considering the soft-plus activation instead of the ReLU activation and average pooling instead of the max-pooling operation. As shown in Appendix D, we have $\ell_{avgpool} = 1$, $L_{avgpool} = 0$, $\ell_{softplus} = 1$, $L_{softplus} = {1/4}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Batch-normalization effect", "weight": 1.0} -->

We can also compare the smoothness properties of the smoothed network with the same network modified by adding the batch-normalization layer for $m$ inputs and $\epsilon$ normalization parameter at each convolutional layer. As shown in Appendix D, the batch-normalization satisfies $m_{batch} = {\deltam}$, $\ell_{batch} = {2\epsilon^{- {1/2}}}$, $L_{batch} = {2m^{- {1/2}}\epsilon^{- 1}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Batch-normalization effect", "weight": 1.0} -->

Denoting $\ell_{{VGG} - {smooth}}$, $L_{{VGG} - {smooth}}$ and $\ell_{{VGG} - {batch}}$, $L_{{VGG} - {batch}}$ the Lipschitz-continuity and smoothness estimates of the smoothed VGG network with and without batch-normalization respectively on a Cartesian product of balls $C = {\{{u = {(u_{1};\ldots;u_{16})}}:{{\| u_{t}\|}_{2} \leq 1}\}}$ with ${\| x\|}_{2} = 1$, we get using Prop. 4.5, Intuitively, the batch-norm bounds the output of each layer, mitigating the increase of $m_{t}$ in the computations of the estimates of the smoothness in lines 8 and 9 of Algo.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Batch-normalization effect", "weight": 1.0} -->

4. Yet, for a small $\epsilon$, this effect is balanced by the non-smoothness of the batch-norm layer (which for $\epsilon\rightarrow 0$ tends to have an infinite slope around 0).
