## Introduction

Consider the optimization problem arising when training maximum margin structured prediction models:

where each $f^{(i)}$ is the structural hinge loss. Max-margin structured prediction was designed to forecast discrete data structures such as sequences and trees.

Batch non-smooth optimization algorithms such as cutting plane methods are appropriate for problems with small or moderate sample sizes. Stochastic non-smooth optimization algorithms such as stochastic subgradient methods can tackle problems with large sample sizes. However, both families of methods achieve the typical worst-case complexity bounds of non-smooth optimization algorithms and cannot easily leverage a possible hidden smoothness of the objective.

Furthermore, as significant progress is being made on incremental smooth optimization algorithms for training unstructured prediction models, we would like to transfer such advances and design faster optimization algorithms to train structured prediction models. Indeed if each term in the finite-sum were $L$-smooth, incremental optimization algorithms such as MISO, SAG, SAGA, SDCA, and SVRG could leverage the finite-sum structure of the objective and achieve faster convergence than batch algorithms on large-scale problems.

Incremental optimization algorithms can be further accelerated, either on a case-by-case basis or using the Catalyst acceleration scheme, to achieve near-optimal convergence rates. Accelerated incremental optimization algorithms demonstrate stable and fast convergence behavior on a wide range of problems, in particular for ill-conditioned ones.

We introduce a general framework that allows us to bring the power of accelerated incremental optimization algorithms to the realm of structured prediction problems. To illustrate our framework, we focus on the problem of training a structural support vector machine (SSVM), and extend the developed algorithms to deep structured prediction models with nonlinear mappings.

We seek primal optimization algorithms, as opposed to saddle-point or primal-dual optimization algorithms, in order to be able to tackle structured prediction models with affine mappings such as SSVM as well as deep structured prediction models with nonlinear mappings. We show how to shade off the inherent non-smoothness of the objective while still being able to rely on efficient inference algorithms.

Smooth Inference Oracles.

: We introduce a notion of smooth inference oracles that gracefully fits the framework of black-box first-order optimization. While the exp inference oracle reveals the relationship between max-margin and probabilistic structured prediction models, the top-$K$ inference oracle can be efficiently computed using simple modifications of efficient inference algorithms in many cases of interest.

Incremental Optimization Algorithms.

: We present a new algorithm built on top of SVRG, blending an extrapolation scheme for acceleration and an adaptive smoothing scheme. We establish the worst-case complexity bounds of the proposed algorithm and extend it to the case of non-linear mappings. Finally, we demonstrate its effectiveness compared to competing algorithms on two tasks, namely named entity recognition and visual object localization.

The code is publicly available as a software library called Casimir^11^1[https://github.com/krishnap25/casimir](https://github.com/krishnap25/casimir). The outline of the paper is as follows: Sec. 1.1 reviews related work. Sec. 2 discusses smoothing for structured prediction followed by Sec. 3, which defines and studies the properties of inference oracles and Sec. 4, which describes the concrete implementation of these inference oracles in several settings of interest. Then, we switch gears to study accelerated incremental algorithms in convex case (Sec. 5) and their extensions to deep structured prediction (Sec. 6). Finally, we evaluate the proposed algorithms on two tasks, namely named entity recognition and visual object localization in Sec. 7.

### Related Work

Algo. (exp oracle) # Oracle calls Exponentiated gradient* $\frac{\left( {n + {\log|\mathcal{Y}|}} \right)R^{2}}{\lambda\epsilon}$ Excessive gap reduction $nR\sqrt{\frac{\log|\mathcal{Y}|}{\lambda\epsilon}}$ Prop. 29*, entropy smoother $\sqrt{\frac{nR^{2}{\log|\mathcal{Y}|}}{\lambda\epsilon}}$ Prop. 30*, entropy smoother $n + \frac{R^{2}{\log|\mathcal{Y}|}}{\lambda\epsilon}$
Algo. (max oracle) # Oracle calls BMRM $\frac{nR^{2}}{\lambda\epsilon}$ QP 1-slack $\frac{nR^{2}}{\lambda\epsilon}$ Stochastic subgradient* $\frac{R^{2}}{\lambda\epsilon}$ Block-Coordinate Frank-Wolfe* $n + \frac{R^{2}}{\lambda\epsilon}$
Algo. (top-K oracle) # Oracle calls Prop. 29*, ℓ22 smoother $\sqrt{\frac{n{\overset{\sim}{R}}^{2}}{\lambda\epsilon}}$ Prop. 30*, ℓ22 smoother $n + \frac{{\overset{\sim}{R}}^{2}}{\lambda\epsilon}$
Table 1: Convergence rates given in terms of the number of calls to various oracles for different optimization algorithms on the learning problem in case of structural support vector machines. The rates are specified in terms of the target accuracy ϵ, the number of training examples n, the regularization λ, the size of the label space |𝒴|, the max feature norm R = maxi∥Φ (x(i),y) − Φ (x(i),y(i))∥2 and $\overset{\sim}{R} \geq R$ (see Remark 28 for explicit form). The rates are specified up to constants and factors logarithmic in the problem parameters. The dependence on the initial error is ignored. * denotes algorithms that make 𝒪 oracle calls per iteration.

### Optimization for Structural Support Vector Machines

Table 1 gives an overview of different optimization algorithms designed for structural support vector machines. Early works considered batch dual quadratic optimization (QP) algorithms. The stochastic subgradient method operated directly on the non-smooth primal formulation. More recently, Lacoste-Julien et al. proposed a block coordinate Frank-Wolfe (BCFW) algorithm to optimize the dual formulation of structural support vector machines; see also Osokin et al. for variants and extensions. Saddle-point or primal-dual approaches include the mirror-prox algorithm. Palaniappan and Bach propose an incremental optimization algorithm for saddle-point problems. However, it is unclear how to extend it to the structured prediction problems considered here. Incremental optimization algorithms for conditional random fields were proposed by Schmidt et al.. We focus here on primal optimization algorithms in order to be able to train structured prediction models with affine or nonlinear mappings with a unified approach, and on incremental optimization algorithms which can scale to large datasets.

### Inference

The ideas of dynamic programming inference in tree structured graphical models have been around since the pioneering works of Pearl and Dawid. Other techniques emerged based on graph cuts, bipartite matchings and search algorithms. For graphical models that admit no such a discrete structure, techniques based on loopy belief propagation, linear programming (LP), dual decomposition and variational inference gained popularity.

### Top-$K$ Inference

Smooth inference oracles with $\ell_{2}^{2}$ smoothing echo older heuristics in speech and language processing. Combinatorial algorithms for top-$K$ inference have been studied extensively by the graphical models community under the name "$M$-best MAP". Seroussi and Golmard and Nilsson first considered the problem of finding the $K$ most probable configurations in a tree structured graphical model. Later, Yanover and Weiss presented the Best Max-Marginal First algorithm which solves this problem with access only to an oracle that computes max-marginals. We also use this algorithm in Sec. 4.2. Fromer and Globerson study top-$K$ inference for LP relaxation, while Batra considers the dual problem to exploit graph structure. Flerova et al. study top-$K$ extensions of the popular $\text{A}^{\star}$ and branch and bound search algorithms in the context of graphical models. Other related approaches include diverse $K$-best solutions and finding $K$-most probable modes.

### Smoothing Inference

Smoothing for inference was used to speed up iterative algorithms for continuous relaxations. Johnson considered smoothing dual decomposition inference using the entropy smoother, followed by Jojic et al. and Savchynskyy et al. who studied its theoretical properties. Meshi et al. expand on this study to include $\ell_{2}^{2}$ smoothing. Explicitly smoothing discrete inference algorithms in order to smooth the learning problem was considered by Zhang et al. and Song et al. using the entropy and $\ell_{2}^{2}$ smoothers respectively. The $\ell_{2}^{2}$ smoother was also used by Martins and Astudillo. Hazan et al. consider the approach of blending learning and inference, instead of using inference algorithms as black-box procedures.

Related ideas to ours appear in the independent works. These works partially overlap with ours, but the papers choose different perspectives, making them complementary to each other. Mensch and Blondel proceed differently when, e.g., smoothing inference based on dynamic programming. Moreover, they do not establish complexity bounds for optimization algorithms making calls to the resulting smooth inference oracles. We define smooth inference oracles in the context of black-box first-order optimization and establish worst-case complexity bounds for incremental optimization algorithms making calls to these oracles. Indeed we relate the amount of smoothing controlled by $\mu$ to the resulting complexity of the optimization algorithms relying on smooth inference oracles.

### End-to-end Training of Structured Prediction

The general framework for global training of structured prediction models was introduced by Bottou and Gallinari and applied to handwriting recognition by Bengio et al. and to document processing by Bottou et al.. This approach, now called "deep structured prediction", was used, e.g., by Collobert et al. and Belanger and McCallum.

### Notation

Vectors are denoted by bold lowercase characters as ${\mathbf{w}} \in {\mathbb{R}}^{d}$ while matrices are denoted by bold uppercase characters as ${\mathbf{A}} \in {\mathbb{R}}^{d \times n}$. For a matrix ${\mathbf{A}} \in {\mathbb{R}}^{m \times n}$, define the norm for ${\alpha,\beta} \in {\{ 1,2,\infty\}}$,

For any function $f:{{\mathbb{R}}^{d}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$, its convex conjugate $f^{\ast}:{{\mathbb{R}}^{d}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$ is defined as

A function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is said to be $L$-smooth with respect to an arbitrary norm $\parallel \cdot \parallel$ if it is continuously differentiable and its gradient $\nabla f$ is $L$-Lipschitz with respect to $\parallel \cdot \parallel$. When left unspecified, $\parallel \cdot \parallel$ refers to $\parallel \cdot \parallel_{2}$. Given a continuously differentiable map ${\mathbf{g}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{m}}$, its Jacobian ${{\nabla{\mathbf{g}}}{({\mathbf{w}})}} \in {\mathbb{R}}^{m \times d}$ at ${\mathbf{w}} \in {\mathbb{R}}^{d}$ is defined so that its $ij$th entry is ${\lbrack{{\nabla{\mathbf{g}}}{({\mathbf{w}})}}\rbrack}_{ij} = {\partial{{g_{i}{({\mathbf{w}})}}/w_{j}}}$ where $g_{i}$ is the $i$th element of $\mathbf{g}$ and $w_{j}$ is the $j$th element of $\mathbf{w}$. The vector valued function ${\mathbf{g}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{m}}$ is said to be $L$-smooth with respect to $\parallel \cdot \parallel$ if it is continuously differentiable and its Jacobian $\nabla{\mathbf{g}}$ is $L$-Lipschitz with respect to $\parallel \cdot \parallel$.

For a vector ${\mathbf{z}} \in {\mathbb{R}}^{m}$, $z_{} \geq \cdots \geq z_{(m)}$ refer to its components enumerated in non-increasing order where ties are broken arbitrarily. Further, we let ${\mathbf{z}}_{\lbrack k\rbrack} = {(z_{},\cdots,z_{(k)})} \in {\mathbb{R}}^{k}$ denote the vector of the $k$ largest components of $\mathbf{z}$. We denote by $\Delta^{m - 1}$ the standard probability simplex in ${\mathbb{R}}^{m}$. When the dimension is clear from the context, we shall simply denote it by $\Delta$. Moreover, for a positive integer $p$, $\lbrack p\rbrack$ refers to the set $\{ 1,\ldots,p\}$. Lastly, $\overset{\sim}{\mathcal{O}}$ in the big-$\mathcal{O}$ notation hides factors logarithmic in problem parameters.

## Smooth Structured Prediction

Structured prediction aims to search for score functions $\phi$ parameterized by ${\mathbf{w}} \in {\mathbb{R}}^{d}$ that model the compatibility of input ${\mathbf{x}} \in \mathcal{X}$ and output ${\mathbf{y}} \in \mathcal{Y}$ as $\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}$ through a graphical model. Given a score function $\phi{( \cdot, \cdot;{\mathbf{w}})}$, predictions are made using an inference procedure which, when given an input $\mathbf{x}$, produces the best output

We shall return to the score functions and the inference procedures in Sec. 3. First, given such a score function $\phi$, we define the structural hinge loss and describe how it can be smoothed.

### Structural Hinge Loss

On a given input-output pair $({\mathbf{x}},{\mathbf{y}})$, the error of prediction of $\mathbf{y}$ by the inference procedure with a score function $\phi{( \cdot, \cdot;{\mathbf{w}})}$, is measured by a task loss $\ell\left( {\mathbf{y}},{{\mathbf{y}}^{\ast}{({\mathbf{x}};{\mathbf{w}})}} \right)$ such as the Hamming loss. The learning procedure would then aim to find the best parameter $\mathbf{w}$ that minimizes the loss on a given dataset of input-output training examples. However, the resulting problem is piecewise constant and hard to optimize. Instead, Altun et al.; Taskar et al.; Tsochantaridis et al. propose to minimize a majorizing surrogate of the task loss, called the structural hinge loss defined on an input-output pair $({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)})$ as

where ${\psi^{(i)}{({\mathbf{y}};{\mathbf{w}})}} = {{{\phi{({\mathbf{x}}^{(i)},{\mathbf{y}};{\mathbf{w}})}} + {\ell{({\mathbf{y}}^{(i)},{\mathbf{y}})}}} - {\phi{({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)};{\mathbf{w}})}}}$ is the augmented score function.

This approach, known as max-margin structured prediction, builds upon binary and multi-class support vector machines, where the term $\ell{({\mathbf{y}}^{(i)},{\mathbf{y}})}$ inside the maximization in generalizes the notion of margin. The task loss $\ell$ is assumed to possess appropriate structure so that the maximization inside, known as loss augmented inference, is no harder than the inference problem in. When considering a fixed input-output pair $({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)}$), we drop the index with respect to the sample $i$ and consider the structural hinge loss as

When the map ${\mathbf{w}}\mapsto{\psi{({\mathbf{y}};{\mathbf{w}})}}$ is affine, the structural hinge loss $f$ and the objective $F$ from are both convex - we refer to this case as the structural support vector machine. When ${\mathbf{w}}\mapsto{\psi{({\mathbf{y}};{\mathbf{w}})}}$ is a nonlinear but smooth map, then the structural hinge loss $f$ and the objective $F$ are nonconvex.

### Smoothing Strategy

A convex, non-smooth function $h$ can be smoothed by taking its infimal convolution with a smooth function. We now recall its dual representation, which Nesterov first used to relate the amount of smoothing to optimal complexity bounds.

### Definition 1

For a given convex function $h:{{\mathbb{R}}^{m}\rightarrow{\mathbb{R}}}$, a smoothing function $\omega:{{\operatorname{dom}h^{\ast}}\rightarrow{\mathbb{R}}}$ which is 1-strongly convex with respect to $\parallel \cdot \parallel_{\alpha}$ (for $\alpha \in {\{ 1,2\}}$), and a parameter $\mu > 0$, define

as the smoothing of $h$ by $\mu\omega$.

We now state a classical result showing how the parameter $\mu$ controls both the approximation error and the level of the smoothing. For a proof, see Beck and Teboulle or Prop. 39 of Appendix A.

### Proposition 2

Consider the setting of Def. 1. The smoothing $h_{\mu\omega}$ is continuously differentiable and its gradient, given by

is $1/\mu$-Lipschitz with respect to $\parallel \cdot \parallel_{\alpha}^{\ast}$. Moreover, letting $h_{\mu\omega} \equiv h$ for $\mu = 0$, the smoothing satisfies, for all $\mu_{1} \geq \mu_{2} \geq 0$,

### Smoothing the Structural Hinge Loss

We rewrite the structural hinge loss as a composition

where $m = {|\mathcal{Y}|}$ so that the structural hinge loss reads

We smooth the structural hinge loss by simply smoothing the non-smooth max function $h$ as

When $\mathbf{g}$ is smooth and Lipschitz continuous, $f_{\mu\omega}$ is a smooth approximation of the structural hinge loss, whose gradient is readily given by the chain-rule. In particular, when $\mathbf{g}$ is an affine map ${{\mathbf{g}}{({\mathbf{w}})}} = {{{\mathbf{A}}{\mathbf{w}}} + {\mathbf{b}}}$, if follows that $f_{\mu\omega}$ is $({{\|{\mathbf{A}}\|}_{\beta,\alpha}^{2}/\mu})$-smooth with respect to $\parallel \cdot \parallel_{\beta}$ (cf. Lemma 40 in Appendix A). Furthermore, for $\mu_{1} \geq \mu_{2} \geq 0$, we have,

### Smoothing Variants

In the context of smoothing the max function, we now describe two popular choices for the smoothing function $\omega$, followed by computational considerations.

### Entropy and $\ell_{2}^{2}$ smoothing

When $h$ is the max function, the smoothing operation can be computed analytically for the *entropy* smoother and the $\ell_{2}^{2}$ smoother, denoted respectively as

These lead respectively to the log-sum-exp function

and an orthogonal projection onto the simplex,

Furthermore, the following holds for all $\mu_{1} \geq \mu_{2} \geq 0$ from Prop. 2:

### Top-$K$ Strategy

Though the gradient of the composition $f_{\mu\omega} = {h_{\mu\omega} \circ {\mathbf{g}}}$ can be written using the chain rule, its actual computation for structured prediction problems involves computing $\nabla{\mathbf{g}}$ over all $m = {|\mathcal{Y}|}$ of its components, which may be intractable. However, in the case of $\ell_{2}^{2}$ smoothing, projections onto the simplex are sparse, as pointed out by the following proposition.

### Proposition 3

Consider the Euclidean projection $\mathbf{u}^{\ast} = {\underset{\mathbf{u} \in \Delta^{m - 1}}{\arg\min}{\|{\mathbf{u} - {\mathbf{z}/\mu}}\|}_{2}^{2}}$ of ${\mathbf{z}/\mu} \in {\mathbb{R}}^{m}$ onto the simplex, where $\mu > 0$. The projection $\mathbf{u}^{\ast}$ has exactly $k \in {\lbrack m\rbrack}$ non-zeros if and only if

where $z_{} \geq \cdots \geq z_{(m)}$ are the components of $\mathbf{z}$ in non-decreasing order and $z_{({m + 1})}:={- \infty}$. In this case, $\mathbf{u}^{\ast}$ is given by

### Proof

The projection ${\mathbf{u}}^{\ast}$ satisfies $u_{i}^{\ast} = {({{z_{i}/\mu} + \rho^{\ast}})}_{+}$, where $\rho^{\ast}$ is the unique solution of $\rho$ in the equation

where $\alpha_{+} = {\max{\{ 0,\alpha\}}}$. See, e.g., Held et al. for a proof of this fact. Note that ${{z_{(i)}/\mu} + \rho^{\ast}} \leq 0$ implies that ${{z_{(j)}/\mu} + \rho^{\ast}} \leq 0$ for all $j \geq i$. Therefore ${\mathbf{u}}^{\ast}$ has $k$ non-zeros if and only if ${{z_{(k)}/\mu} + \rho^{\ast}} > 0$ and ${{z_{({k + 1})}/\mu} + \rho^{\ast}} \leq 0$.

Now suppose that ${\mathbf{u}}^{\ast}$ has exactly $k$ non-zeros, we can then solve to obtain $\rho^{\ast} = {\varphi_{k}{({{\mathbf{z}}/\mu})}}$, which is defined as

Plugging in the value of $\rho^{\ast}$ in ${{z_{(k)}/\mu} + \rho^{\ast}} > 0$ gives $\mu > {\sum_{i = 1}^{k}\left( {z_{(i)} - z_{(k)}} \right)}$. Likewise, ${{z_{({k + 1})}/\mu} + \rho^{\ast}} \leq 0$ gives $\mu \leq {\sum_{i = 1}^{k}\left( {z_{(i)} - z_{({k + 1})}} \right)}$.

Conversely assume and let $\hat{\rho} = {\varphi_{k}{({{\mathbf{z}}/\mu})}}$. Eq. can be written as ${{z_{(k)}/\mu} + \hat{\rho}} > 0$ and ${{z_{({k + 1})}/\mu} + \hat{\rho}} \leq 0$. Furthermore, we verify that $\hat{\rho}$ satisfies Eq., and so $\hat{\rho} = \rho^{\ast}$ is its unique root. It follows, therefore, that the sparsity of ${\mathbf{u}}^{\ast}$ is $k$. ∎

Thus, the projection of ${\mathbf{z}}/\mu$ onto the simplex picks out some number $K_{{\mathbf{z}}/\mu}$ of the largest entries of ${\mathbf{z}}/\mu$ - we refer to this as the sparsity of ${proj}_{\Delta^{m - 1}}{({{\mathbf{z}}/\mu})}$. This fact motivates the top-$K$ strategy: given $\mu > 0$, fix an integer $K$ a priori and consider as surrogates for $h_{\mu\ell_{2}^{2}}$ and $\nabla h_{\mu\ell_{2}^{2}}$ respectively

where ${\mathbf{z}}_{\lbrack K\rbrack}$ denotes the vector composed of the $K$ largest entries of $\mathbf{z}$ and $\Omega_{K}:{{\mathbb{R}}^{m}\rightarrow{\{ 0,1\}}^{K \times m}}$ defines their extraction, i.e., ${\Omega_{K}{({\mathbf{z}})}} = {({\mathbf{e}}_{j_{1}}^{\top},\ldots,{\mathbf{e}}_{j_{K}}^{\top})}^{\top} \in {\{ 0,1\}}^{K \times m}$ where $j_{1},\cdots,j_{K}$ satisfy $z_{j_{1}} \geq \cdots \geq z_{j_{K}}$ such that ${\mathbf{z}}_{\lbrack K\rbrack} = {\Omega_{K}{({\mathbf{z}})}{\mathbf{z}}}$. A surrogate of the $\ell_{2}^{2}$ smoothing is then given by

### Exactness of Top-$K$ Strategy

We say that the top-$K$ strategy is exact at $\mathbf{z}$ for $\mu > 0$ when it recovers the first order information of $h_{\mu\ell_{2}^{2}}$, i.e. when ${h_{\mu\ell_{2}^{2}}{({\mathbf{z}})}} = {h_{\mu,K}{({\mathbf{z}})}}$ and ${{\nabla h_{\mu\ell_{2}^{2}}}{({\mathbf{z}})}} = {\overset{\sim}{\nabla}h_{\mu,K}{({\mathbf{z}})}}$. The next proposition outlines when this is the case. Note that if the top-$K$ strategy is exact at $\mathbf{z}$ for a smoothing parameter $\mu > 0$ then it will be exact at $\mathbf{z}$ for any $\mu^{\prime} < \mu$.

### Proposition 4

The top-$K$ strategy is exact at $\mathbf{z}$ for $\mu > 0$ if

Moreover, for any fixed $\mathbf{z} \in {\mathbb{R}}^{m}$ such that the vector $\mathbf{z}_{\lbrack{K + 1}\rbrack} = {\Omega_{K + 1}{(\mathbf{z})}\mathbf{z}}$ has at least two unique elements, the top-$K$ strategy is exact at $\mathbf{z}$ for all $\mu$ satisfying $0 < \mu \leq {z_{} - z_{({K + 1})}}$.

### Proof

First, we note that the top-$K$ strategy is exact when the sparsity $K_{{\mathbf{z}}/\mu}$ of the projection ${proj}_{\Delta^{m - 1}}{({{\mathbf{z}}/\mu})}$ satisfies $K_{{\mathbf{z}}/\mu} \leq K$. From Prop. 3, the condition that $K_{{\mathbf{z}}/\mu} \in {\{ 1,2,\cdots,K\}}$ happens when

since the intervals in the union are contiguous. This establishes.

The only case when cannot hold for any value of $\mu > 0$ is when the right hand size of is zero. In the opposite case when ${\mathbf{z}}_{\lbrack{K + 1}\rbrack}$ has at least two unique components, or equivalently, ${z_{} - z_{({K + 1})}} > 0$, the condition $0 < \mu \leq {z_{} - z_{({K + 1})}}$ implies. ∎

If the top-$K$ strategy is exact at ${\mathbf{g}}{({\mathbf{w}})}$ for $\mu$, then

where the latter follows from the chain rule. When used instead of $\ell_{2}^{2}$ smoothing in the algorithms presented in Sec. 5, the top-$K$ strategy provides a computationally efficient heuristic to smooth the structural hinge loss. Though we do not have theoretical guarantees using this surrogate, experiments presented in Sec. 7 show its efficiency and its robustness to the choice of $K$.

## Inference Oracles

This section studies first order oracles used in standard and smoothed structured prediction. We first describe the parameterization of the score functions through graphical models.

### Score Functions

Structured prediction is defined by the structure of the output $\mathbf{y}$, while input ${\mathbf{x}} \in \mathcal{X}$ can be arbitrary. Each output ${\mathbf{y}} \in \mathcal{Y}$ is composed of $p$ components $y_{1},\ldots,y_{p}$ that are linked through a graphical model $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$ - the nodes $\mathcal{V} = {\{ 1,\cdots,p\}}$ represent the components of the output $\mathbf{y}$ while the edges $\mathcal{E}$ define the dependencies between various components. The value of each component $y_{v}$ for $v \in \mathcal{V}$ represents the state of the node $v$ and takes values from a finite set $\mathcal{Y}_{v}$. The set of all output structures $\mathcal{Y} = {\mathcal{Y}_{1} \times \cdots \times \mathcal{Y}_{p}}$ is then finite yet potentially intractably large.

The structure of the graph (i.e., its edge structure) depends on the task. For the task of sequence labeling, the graph is a chain, while for the task of parsing, the graph is a tree. On the other hand, the graph used in image segmentation is a grid.

For a given input $\mathbf{x}$ and a score function $\phi{( \cdot, \cdot;{\mathbf{w}})}$, the value $\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}$ measures the compatibility of the output $\mathbf{y}$ for the input $\mathbf{x}$. The essential characteristic of the score function is that it decomposes over the nodes and edges of the graph as

For a fixed $\mathbf{w}$, each input $\mathbf{x}$ defines a specific compatibility function $\phi{({\mathbf{x}}, \cdot;{\mathbf{w}})}$. The nature of the problem and the optimization algorithms we consider hinge upon whether $\phi$ is an affine function of $\mathbf{w}$ or not. The two settings studied here are the following:

: Pre-defined Feature Map. In this structured prediction framework, a pre-specified feature map $\Phi:{{\mathcal{X} \times \mathcal{Y}}\rightarrow{\mathbb{R}}^{d}}$ is employed and the score $\phi$ is then defined as the linear function

: Learning the Feature Map. We also consider the setting where the feature map $\Phi$ is parameterized by ${\mathbf{w}}_{0}$, for example, using a neural network, and is learned from the data. The score function can then be written as

where ${\mathbf{w}} = {({\mathbf{w}}_{0},{\mathbf{w}}_{1})}$ and the scalar product decomposes into nodes and edges as above.

Note that we only need the decomposition of the score function over nodes and edges of the $\mathcal{G}$ as in Eq.. In particular, while Eq. is helpful to understand the use of neural networks in structured prediction, the optimization algorithms developed in Sec. 6 apply to general nonlinear but smooth score functions.

This framework captures both generative probabilistic models such as Hidden Markov Models (HMMs) that model the joint distribution between $\mathbf{x}$ and $\mathbf{y}$ as well as discriminative probabilistic models, such as conditional random fields where dependencies among the input variables $\mathbf{x}$ do not need to be explicitly represented. In these cases, the log joint and conditional probabilities respectively play the role of the score $\phi$.

### Example 5 (Sequence Tagging)

Consider the task of sequence tagging in natural language processing where each $\mathbf{x} = {(x_{1},\cdots,x_{p})} \in \mathcal{X}$ is a sequence of words and $\mathbf{y} = {(y_{1},\cdots,y_{p})} \in \mathcal{Y}$ is a sequence of labels, both of length $p$. Common examples include part of speech tagging and named entity recognition. Each word $x_{v}$ in the sequence $\mathbf{x}$ comes from a finite dictionary $\mathcal{D}$, and each tag $y_{v}$ in $\mathbf{y}$ takes values from a finite set $\mathcal{Y}_{v} = \mathcal{Y}_{tag}$. The corresponding graph is simply a linear chain.

The score function measures the compatibility of a sequence $\mathbf{y} \in \mathcal{Y}$ for the input $\mathbf{x} \in \mathcal{X}$ using parameters $\mathbf{w} = {(\mathbf{w}_{unary},\mathbf{w}_{pair})}$ as, for instance,

where, using $\mathbf{w}_{unary} \in {\mathbb{R}}^{{|\mathcal{D}|}{|\mathcal{Y}_{tag}|}}$ and $\mathbf{w}_{pair} \in {\mathbb{R}}^{{|\mathcal{Y}_{tag}|}^{2}}$ as node and edge weights respectively, we define for each $v \in {\lbrack p\rbrack}$,

The pairwise term $\langle{\Phi_{pair}{(y_{v},y_{v + 1})}},\mathbf{w}_{pair}\rangle$ is analogously defined. Here, $y_{0},y_{p + 1}$ are special "start" and "stop" symbols respectively. This can be written as a dot product of $\mathbf{w}$ with a pre-specified feature map as in, by defining

where $\mathbf{e}_{x_{v}}$ is the unit vector ${({\mathbb{I}{({x = x_{v}})}})}_{x \in \mathcal{D}} \in {\mathbb{R}}^{|\mathcal{D}|}$, $\mathbf{e}_{y_{v}}$ is the unit vector ${({\mathbb{I}{({j = y_{v}})}})}_{j \in \mathcal{Y}_{tag}} \in {\mathbb{R}}^{|\mathcal{Y}_{tag}|}$, $\otimes$ denotes the Kronecker product between vectors and $\oplus$ denotes vector concatenation.

### Inference Oracles

We define now inference oracles as first order oracles in structured prediction. These are used later to understand the information-based complexity of optimization algorithms.

### First Order Oracles in Structured Prediction

A first order oracle for a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is a routine which, given a point ${\mathbf{w}} \in {\mathbb{R}}^{d}$, returns on output a value $f{({\mathbf{w}})}$ and a (sub)gradient ${\mathbf{v}} \in {\partial{f{({\mathbf{w}})}}}$, where $\partial f$ is the Fréchet (or regular) subdifferential. We now define inference oracles as first order oracles for the structural hinge loss $f$ and its smoothed variants $f_{\mu\omega}$. Note that these definitions are independent of the graphical structure. However, as we shall see, the graphical structure plays a crucial role in the implementation of the inference oracles.

### Definition 6

Consider an augmented score function $\psi$, a level of smoothing $\mu > 0$ and the structural hinge loss ${f{(\mathbf{w})}} = {{\max_{\mathbf{y} \in \mathcal{Y}}\psi}{(\mathbf{y};\mathbf{w})}}$. For a given $\mathbf{w} \in {\mathbb{R}}^{d}$,

the max oracle returns $f{({\mathbf{w}})}$ and ${\mathbf{v}} \in {\partial{f{({\mathbf{w}})}}}$.

the exp oracle returns $f_{- {\muH}}{({\mathbf{w}})}$ and ${\nabla f_{- {\muH}}}{({\mathbf{w}})}$.

the top-$K$ oracle returns $f_{\mu,K}{({\mathbf{w}})}$ and $\overset{\sim}{\nabla}f_{\mu,K}{({\mathbf{w}})}$ as surrogates for $f_{\mu\ell_{2}^{2}}{({\mathbf{w}})}$ and ${\nabla f_{\mu\ell_{2}^{2}}}{({\mathbf{w}})}$ respectively.

Note that the exp oracle gets its name since it can be written as an expectation over all $\mathbf{y}$, as revealed by the next lemma, which gives analytical expressions for the gradients returned by the oracles.

### Lemma 7

Consider the setting of Def. 6. We have the following:

For any ${\mathbf{y}}^{\ast} \in {{\underset{{\mathbf{y}} \in \mathcal{Y}}{\arg\max}\psi}{({\mathbf{y}};{\mathbf{w}})}}$, we have that ${{\nabla_{\mathbf{w}}\psi}{({\mathbf{y}}^{\ast};{\mathbf{w}})}} \in {\partial{f{({\mathbf{w}})}}}$. That is, the max oracle can be implemented by inference.

The output of the exp oracle satisfies ${{\nabla f_{- {\muH}}}{({\mathbf{w}})}} = {\sum_{{\mathbf{y}} \in \mathcal{Y}}{P_{\psi,\mu}{({\mathbf{y}};{\mathbf{w}})}{\nabla\psi}{({\mathbf{y}};{\mathbf{w}})}}}$, where

The output of the top-$K$ oracle satisfies ${{\overset{\sim}{\nabla}f_{\mu,K}{({\mathbf{w}})}} = {\sum_{i = 1}^{K}{u_{\psi,\mu,i}^{\ast}{({\mathbf{w}})}{\nabla\psi}{({\mathbf{y}}_{(i)};{\mathbf{w}})}}}},$ where $Y_{K} = \left\{ {\mathbf{y}}_{},\cdots,{\mathbf{y}}_{(K)} \right\}$ is the set of $K$ largest scoring outputs satisfying

and ${\mathbf{u}}_{\psi,\mu}^{\ast} = {{proj}_{\Delta^{K - 1}}\left( \left\lbrack {\psi{({\mathbf{y}}_{};{\mathbf{w}})}},\cdots,{\psi{({\mathbf{y}}_{(K)};{\mathbf{w}})}} \right\rbrack^{\top} \right)}$.

### Proof

Part (ii) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models") deals with the composition of differentiable functions, and follows from the chain rule. Part (iii) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models") follows from the definition in Eq.. The proof of Part (i) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models") follows from the chain rule for Fréchet subdifferentials of compositions together with the fact that by convexity and Danskin's theorem, the subdifferential of the max function is given by ${\partial{h{({\mathbf{z}})}}} = {\operatorname{conv}{\{{\left. {\mathbf{e}}_{i} \middle| i \right. \in {{\lbrack m\rbrack}\text{~such that~}z_{i}} = {h{({\mathbf{z}})}}}\}}}$. ∎

Figure 1: Viterbi trellis for a chain graph with p = 4 nodes and 3 labels.

### Example 8

Consider the task of sequence tagging from Example 5. ‣ 3.1 Score Functions ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"). The inference problem is a search over all ${|\mathcal{Y}|} = {|\mathcal{Y}_{tag}|}^{p}$ label sequences. For chain graphs, this is equivalent to searching for the shortest path in the associated trellis, shown in Fig. 1. An efficient dynamic programming approach called the Viterbi algorithm can solve this problem in space and time polynomial in $p$ and $|\mathcal{Y}_{tag}|$. The structural hinge loss is non-smooth because a small change in $\mathbf{w}$ might lead to a radical change in the best scoring path shown in Fig. 1.

When smoothing $f$ with $\omega = \ell_{2}^{2}$, the smoothed function $f_{\mu\ell_{2}^{2}}$ is given by a projection onto the simplex, which picks out some number $K_{\psi/\mu}$ of the highest scoring outputs $\mathbf{y} \in \mathcal{Y}$ or equivalently, $K_{\psi/\mu}$ shortest paths in the Viterbi trellis (Fig. 1(b)). The top-$K$ oracle then uses the top-$K$ strategy to approximate $f_{\mu\ell_{2}^{2}}$ with $f_{\mu,K}$.

On the other hand, with entropy smoothing $\omega = {- H}$, we get the log-sum-exp function and its gradient is obtained by averaging over paths with weights such that shorter paths have a larger weight (cf. Lemma 7(ii) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models")). This is visualized in Fig. 1(c).

### Exp Oracles and Conditional Random Fields

Recall that a Conditional Random Field (CRF) with augmented score function $\psi$ and parameters ${\mathbf{w}} \in {\mathbb{R}}^{d}$ is a probabilistic model that assigns to output ${\mathbf{y}} \in \mathcal{Y}$ the probability

where $A_{\psi}{({\mathbf{w}})}$ is known as the log-partition function, a normalizer so that the probabilities sum to one. Gradient-based maximum likelihood learning algorithms for CRFs require computation of the log-partition function $A_{\psi}{({\mathbf{w}})}$ and its gradient ${\nabla A_{\psi}}{({\mathbf{w}})}$. Next proposition relates the computational costs of the exp oracle and the log-partition function.

### Proposition 9

The exp oracle for an augmented score function $\psi$ with parameters $\mathbf{w} \in {\mathbb{R}}^{d}$ is equivalent in hardness to computing the log-partition function $A_{\psi}{(\mathbf{w})}$ and its gradient ${\nabla A_{\psi}}{(\mathbf{w})}$ for a conditional random field with augmented score function $\psi$.

### Proof

Fix a smoothing parameter $\mu > 0$. Consider a CRF with augmented score function ${\psi^{\prime}{({\mathbf{y}};{\mathbf{w}})}} = {\mu^{- 1}\psi{({\mathbf{y}};{\mathbf{w}})}}$. Its log-partition function $A_{\psi^{\prime}}{({\mathbf{w}})}$ satisfies ${\exp{({A_{\psi^{\prime}}{({\mathbf{w}})}})}} = {\sum_{{\mathbf{y}} \in \mathcal{Y}}{\exp\left( {\mu^{- 1}\psi{({\mathbf{y}};{\mathbf{w}})}} \right)}}$. The claim now follows from the bijection ${f_{- {\muH}}{({\mathbf{w}})}} = {\muA_{\psi^{\prime}}{({\mathbf{w}})}}$ between $f_{- {\muH}}$ and $A_{\psi^{\prime}}$. ∎

## Implementation of Inference Oracles

We now turn to the concrete implementation of the inference oracles. This depends crucially on the structure of the graph $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$. If the graph $\mathcal{G}$ is a tree, then the inference oracles can be computed exactly with efficient procedures, as we shall see in in the Sec. 4.1. When the graph $\mathcal{G}$ is not a tree, we study special cases when specific discrete structure can be exploited to efficiently implement some of the inference oracles in Sec. 4.2. The results of this section are summarized in Table 2.

Table 2: Smooth inference oracles, algorithms and complexity. Here, p is the size of each y ∈ 𝒴. The time complexity is phrased in terms of the time complexity 𝒯 of the max oracle.

Throughout this section, we fix an input-output pair $({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)})$ and consider the augmented score function ${\psi{({\mathbf{y}};{\mathbf{w}})}} = {{{\phi{({\mathbf{x}}^{(i)},{\mathbf{y}};{\mathbf{w}})}} + {\ell{({\mathbf{y}}^{(i)},{\mathbf{y}})}}} - {\phi{({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)};{\mathbf{w}})}}}$ it defines, where the index of the sample is dropped by convenience. From and the decomposability of the loss, we get that $\psi$ decomposes along nodes $\mathcal{V}$ and edges $\mathcal{E}$ of $\mathcal{G}$ as:

When $\mathbf{w}$ is clear from the context, we denote $\psi{( \cdot;{\mathbf{w}})}$ by $\psi$. Likewise for $\psi_{v}$ and $\psi_{v,v^{\prime}}$.

### Inference Oracles in Trees

We first consider algorithms implementing the inference algorithms in trees and examine their computational complexity.

### Implementation of Inference Oracles

### Max Oracle

In tree structured graphical models, the inference problem, and thus the max oracle (cf. Lemma 7(i) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models")) can always be solved exactly in polynomial time by the max-product algorithm, which uses the technique of dynamic programming. The Viterbi algorithm (Algo. 1) for chain graphs from Example 8 is a special case. See Algo. 7 in Appendix B for the max-product algorithm in full generality.

### Top-$K$ Oracle

The top-$K$ oracle uses a generalization of the max-product algorithm that we name top-$K$ max-product algorithm. Following the work of Seroussi and Golmard, it keeps track of the $K$-best intermediate structures while the max-product algorithm just tracks the single best intermediate structure. Formally, the $k$th largest element from a discrete set $S$ is defined as

We present the algorithm in the simple case of chain structured graphical models in Algo. 2. The top-$K$ max-product algorithm for general trees is given in Algo. 8 in Appendix B. Note that it requires $\overset{\sim}{\mathcal{O}}{(K)}$ times the time and space of the max oracle.

### Exp oracle

The relationship of the exp oracle with CRFs (Prop. 9) leads directly to Algo. 3, which is based on marginal computations from the sum-product algorithm.

1: Input: Augmented score function ψ (⋅,⋅;w) defined on a chain graph 𝒢.
2: Set π1 (y1) ← ψ1 (y1) for all y1 ∈ 𝒴1.
4: For all yv ∈ 𝒴v, set

5: Assign to δv (yv) the yv − 1 that attains the max above for each yv ∈ 𝒴v.
7: Set ψ* ← maxyp ∈ 𝒴pπp (yp) and store the maximizing assignments of yp in yp*.

Algorithm 1 Max-product (Viterbi) algorithm for chain graphs

1: Input: Augmented score function ψ (⋅,⋅;w) defined on chain graph 𝒢, integer K &gt; 0.
2: For k = 1, ⋯, K, set π1(k) (y1) ← ψ1 (y1) if k = 1 and − ∞ otherwise for all y1 ∈ 𝒴1.
4: For all yv ∈ 𝒴v, set

${{\pi_{v}^{(k)}{(y_{v})}}\leftarrow{{\psi_{v}{(y_{v})}} + {\underset{{{y_{v - 1} \in \mathcal{Y}_{v - 1}},{\ell \in {\lbrack K\rbrack}}}\phantom{(k)}}{\max^{(k)}}\left\{ {{\pi_{v - 1}^{(\ell)}{(y_{v - 1})}} + {\psi_{v,{v - 1}}{(y_{v},y_{v - 1})}}} \right\}}}}.$

5: Assign to δv(k) (yv), κv(k) (yv) the yv − 1, ℓ that attain the max(k) above for each yv ∈ 𝒴v.
7: For k = 1, ⋯, K, set $\psi^{(k)}\leftarrow{{\max_{{y_{p} \in \mathcal{Y}_{p}},{k \in {\lbrack K\rbrack}}}^{(k)}\pi_{p}^{(k)}}{(y_{p})}}$ and store in yp(k), ℓ(k) respectively the maximizing assignments of yp, k.
Algorithm 2 Top-K max-product (top-K Viterbi) algorithm for chain graphs

1: Input: Augmented score function ψ (⋅,⋅;w) defined on tree structured graph 𝒢, μ &gt; 0.
2: Compute the log-partition function and marginals using the sum-product algorithm (Algo. 9 in Appendix B)

$${{A_{\psi/\mu},{\{{{P_{v}\text{~for~}v} \in \mathcal{V}}\}},{\{{{P_{v,v^{\prime}}\text{~for~}{(v,v^{\prime})}} \in \mathcal{E}}\}}}\leftarrow{\text{SumProduct}\left( {\frac{1}{\mu}\psi{( \cdot;{\mathbf{w}})}},\mathcal{G} \right)}}.$$

$${{{\nabla f_{- {\muH}}}{({\mathbf{w}})}}\leftarrow{{\sum\limits_{v \in \mathcal{V}}{\sum\limits_{y_{v} \in \mathcal{Y}_{v}}{P_{v}{(y_{v})}{\nabla\psi_{v}}{(y_{v};{\mathbf{w}})}}}} + {\sum\limits_{{(v,v^{\prime})} \in \mathcal{E}}{\sum\limits_{y_{v} \in \mathcal{Y}_{v}}{\sum\limits_{y_{v^{\prime}} \in \mathcal{Y}_{v^{\prime}}}{P_{v,v^{\prime}}{(y_{v},y_{v^{\prime}})}{\nabla\psi_{v,v^{\prime}}}{(y_{v};{\mathbf{w}})}}}}}}}.$$

Algorithm 3 Entropy smoothed max-product algorithm

### Remark 10

We note that clique trees allow the generalization of the algorithms of this section to general graphs with cycles. However, the construction of a clique tree requires time and space exponential in the treewidth of the graph.

### Example 11

Consider the task of sequence tagging from Example 5. ‣ 3.1 Score Functions ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"). The Viterbi algorithm (Algo. 1) maintains a table $\pi_{v}{(y_{v})}$, which stores the best length-$v$ prefix ending in label $y_{v}$. One the other hand, the top-$K$ Viterbi algorithm (Algo. 2) must store in $\pi_{v}^{(k)}{(y_{v})}$ the score of $k$th best length-$v$ prefix that ends in $y_{v}$ for each $k \in {\lbrack K\rbrack}$. In the vanilla Viterbi algorithm, the entry $\pi_{v}{(y_{v})}$ is updated by looking the previous column $\pi_{v - 1}$ following. Compare this to update of the top-$K$ Viterbi algorithm. In this case, the exp oracle is implemented by the forward-backward algorithm, a specialization of the sum-product algorithm to chain graphs.

### Complexity of Inference Oracles

The next proposition presents the correctness guarantee and complexity of each of the aforementioned algorithms. Its proof has been placed in Appendix B.

### Proposition 12

Consider as inputs an augmented score function $\psi{( \cdot, \cdot;\mathbf{w})}$ defined on a tree structured graph $\mathcal{G}$, an integer $K > 0$ and a smoothing parameter $\mu > 0$.

The output $(\psi^{\ast},{\mathbf{y}}^{\ast})$ of the max-product algorithm (Algo. 1 for the special case when $\mathcal{G}$ is chain structured Algo. 7 from Appendix B in general) satisfies $\psi^{\ast} = {\psi{({\mathbf{y}}^{\ast};{\mathbf{w}})}} = {{\max_{{\mathbf{y}} \in \mathcal{Y}}\psi}{({\mathbf{y}};{\mathbf{w}})}}$. Thus, the pair $\left( \psi^{\ast},{{\nabla\psi}{({\mathbf{y}}^{\ast};{\mathbf{w}})}} \right)$ is a correct implementation of the max oracle. It requires time $\mathcal{O}{(p\max_{v \in \mathcal{V}}{|\mathcal{Y}_{v}|}^{2})}$ and space $\mathcal{O}{({p{\max_{v \in \mathcal{V}}{|\mathcal{Y}_{v}|}}})}$.

The output ${\{\psi^{(k)},{\mathbf{y}}^{(k)}\}}_{k = 1}^{K}$ of the top-$K$ max-product algorithm (Algo. 2 for the special case when $\mathcal{G}$ is chain structured or Algo. 8 from Appendix B in general) satisfies $\psi^{(k)} = {\psi{({\mathbf{y}}^{(k)})}} = {{\max_{{\mathbf{y}} \in \mathcal{Y}}^{(k)}\psi}{({\mathbf{y}})}}$. Thus, the top-$K$ max-product algorithm followed by a projection onto the simplex (Algo. 6 in Appendix A) is a correct implementation of the top-$K$ oracle. It requires time $\mathcal{O}{(pK\log K\max_{v \in \mathcal{V}}{|\mathcal{Y}_{v}|}^{2})}$ and space $\mathcal{O}{({pK{\max_{v \in \mathcal{V}}{|\mathcal{Y}_{v}|}}})}$.

Algo. 3 returns $\left( {f_{- {\muH}}{({\mathbf{w}})}},{{\nabla f_{- {\muH}}}{({\mathbf{w}})}} \right)$. Thus, Algo. 3 is a correct implementation of the exp oracle. It requires time $\mathcal{O}{(p\max_{v \in \mathcal{V}}{|\mathcal{Y}_{v}|}^{2})}$ and space $\mathcal{O}{({p{\max_{v \in \mathcal{V}}{|\mathcal{Y}_{v}|}}})}$.

### Inference Oracles in Loopy Graphs

For general loopy graphs with high tree-width, the inference problem is NP-hard. In particular cases, graph cut, matching or search algorithms can be used for exact inference in dense loopy graphs, and therefore, to implement the max oracle as well (cf. Lemma 7(i) ‣ Lemma 7. ‣ 3.2.1 First Order Oracles in Structured Prediction ‣ 3.2 Inference Oracles ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models")). In each of these cases, we find that the top-$K$ oracle can be implemented, but the exp oracle is intractable. Appendix C contains a review of the algorithms and guarantees referenced in this section.

### Inference Oracles using Max-Marginals

We now define a max-marginal, which is a constrained maximum of the augmented score $\psi$.

### Definition 13

The max-marginal of $\psi$ relative to a variable $y_{v}$ is defined, for $j \in \mathcal{Y}_{v}$ as

In cases where exact inference is tractable using graph cut or matching algorithms, it is possible to extract max-marginals as well. This, as we shall see next, allows the implementation of the max and top-$K$ oracles.

When the augmented score function $\psi$ is unambiguous, i.e., no two distinct ${{\mathbf{y}}_{1},{\mathbf{y}}_{2}} \in \mathcal{Y}$ have the same augmented score, the output ${\mathbf{y}}^{\ast}{({\mathbf{w}})}$ is unique can be decoded from the max-marginals as (see Pearl; Dawid or Thm. 45 in Appendix C)

If one has access to an algorithm $\mathcal{M}$ that can compute max-marginals, the top-$K$ oracle is also easily implemented via the Best Max-Marginal First (BMMF) algorithm of Yanover and Weiss. This algorithm requires computations of $2K$ sets of max-marginals, where a set of max-marginals refers to max-marginals for all $y_{v}$ in $\mathbf{y}$. Therefore, the BMMF algorithm followed by a projection onto the simplex (Algo. 6 in Appendix A) is a correct implementation of the top-$K$ oracle at a computational cost of $2K$ sets of max-marginals. The BMMF algorithm and its guarantee are recalled in Appendix C.1 for completeness.

### Graph Cut and Matching Inference

Kolmogorov and Zabin showed that submodular energy functions over binary variables can be efficiently minimized exactly via a minimum cut algorithm. For a class of alignment problems, e.g., Taskar et al., inference amounts to finding the best bipartite matching. In both these cases, max-marginals can be computed exactly and efficiently by combinatorial algorithms. This gives us a way to implement the max and top-$K$ oracles. However, in both settings, computing the log-partition function $A_{\psi}{({\mathbf{w}})}$ of a CRF with score $\psi$ is known to be #P-complete. Prop. 9 immediately extends this result to the exp oracle. This discussion is summarized by the following proposition, whose proof is provided in Appendix C.4.

### Proposition 14

Consider as inputs an augmented score function $\psi{( \cdot, \cdot;\mathbf{w})}$, an integer $K > 0$ and a smoothing parameter $\mu > 0$. Further, suppose that $\psi$ is unambiguous, that is, ${\psi{(\mathbf{y}^{\prime};\mathbf{w})}} \neq {\psi{(\mathbf{y}^{\operatorname{\prime\prime}};\mathbf{w})}}$ for all distinct ${\mathbf{y}^{\prime},\mathbf{y}^{\operatorname{\prime\prime}}} \in \mathcal{Y}$. Consider one of the two settings:

the output space $\mathcal{Y}_{v} = {\{ 0,1\}}$ for each $v \in \mathcal{V}$, and the function $- \psi$ is submodular (see Appendix C.2 and, in particular, for the precise definition), or,

the augmented score corresponds to an alignment task where the inference problem corresponds to a maximum weight bipartite matching (see Appendix C.3 for a precise definition).

In these cases, we have the following:

The max oracle can be implemented at a computational complexity of $\mathcal{O}{(p)}$ minimum cut computations in Case (A) ‣ Proposition 14. ‣ Graph Cut and Matching Inference ‣ 4.2.1 Inference Oracles using Max-Marginals ‣ 4.2 Inference Oracles in Loopy Graphs ‣ 4 Implementation of Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"), and in time $\mathcal{O}{(p^{3})}$ in Case (B) ‣ Proposition 14. ‣ Graph Cut and Matching Inference ‣ 4.2.1 Inference Oracles using Max-Marginals ‣ 4.2 Inference Oracles in Loopy Graphs ‣ 4 Implementation of Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models").

The top-$K$ oracle can be implemented at a computational complexity of $\mathcal{O}{({pK})}$ minimum cut computations in Case (A) ‣ Proposition 14. ‣ Graph Cut and Matching Inference ‣ 4.2.1 Inference Oracles using Max-Marginals ‣ 4.2 Inference Oracles in Loopy Graphs ‣ 4 Implementation of Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"), and in time $\mathcal{O}{({p^{3}K})}$ in Case (B) ‣ Proposition 14. ‣ Graph Cut and Matching Inference ‣ 4.2.1 Inference Oracles using Max-Marginals ‣ 4.2 Inference Oracles in Loopy Graphs ‣ 4 Implementation of Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models").

The exp oracle is #P-complete in both cases.

Prop. 14 is loose in that the max oracle can be implemented with just one minimum cut computation instead of $p$ in in Case (A) ‣ Proposition 14. ‣ Graph Cut and Matching Inference ‣ 4.2.1 Inference Oracles using Max-Marginals ‣ 4.2 Inference Oracles in Loopy Graphs ‣ 4 Implementation of Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models").

### Branch and Bound Search

Max oracles implemented via search algorithms can often be extended to implement the top-$K$ oracle. We restrict our attention to best-first branch and bound search such as the celebrated Efficient Subwindow Search.

Branch and bound methods partition the search space into disjoint subsets, while keeping an upper bound $\hat{\psi}:{{\mathcal{X} \times 2^{\mathcal{Y}}}\rightarrow{\mathbb{R}}}$, on the maximal augmented score for each of the subsets $\hat{\mathcal{Y}} \subseteq \mathcal{Y}$. Using a best-first strategy, promising parts of the search space are explored first. Parts of the search space whose upper bound indicates that they cannot contain the maximum do not have to be examined further.

The top-$K$ oracle is implemented by simply continuing the search procedure until $K$ outputs have been produced - see Algo. 13 in Appendix C.5. Both the max oracle and the top-$K$ oracle can degenerate to an exhaustive search in the worst case, so we do not have sharp running time guarantees. However, we have the following correctness guarantee.

### Proposition 15

Consider an augmented score function $\psi{( \cdot, \cdot;\mathbf{w})}$, an integer $K > 0$ and a smoothing parameter $\mu > 0$. Suppose the upper bound function ${\hat{\psi}{( \cdot, \cdot;\mathbf{w})}}:{{\mathcal{X} \times 2^{\mathcal{Y}}}\rightarrow{\mathbb{R}}}$ satisfies the following properties:

$\hat{\psi}{(\hat{\mathcal{Y}};{\mathbf{w}})}$ is finite for every $\hat{\mathcal{Y}} \subseteq \mathcal{Y}$,

${\hat{\psi}{(\hat{\mathcal{Y}};{\mathbf{w}})}} \geq {{\max_{{\mathbf{y}} \in \hat{\mathcal{Y}}}\psi}{({\mathbf{y}};{\mathbf{w}})}}$ for all $\hat{\mathcal{Y}} \subseteq \mathcal{Y}$, and,

${\hat{\psi}{({\{{\mathbf{y}}\}};{\mathbf{w}})}} = {\psi{({\mathbf{y}};{\mathbf{w}})}}$ for every ${\mathbf{y}} \in \mathcal{Y}$.

Then, we have the following:

Algo. 13 with $K = 1$ is a correct implementation of the max oracle.

Algo. 13 followed by a projection onto the simplex (Algo. 6 in Appendix A) is a correct implementation of the top-$K$ oracle.

See Appendix C.5 for a proof. The discrete structure that allows inference via branch and bound search cannot be leveraged to implement the exp oracle.

## The Casimir Algorithm

We come back to the optimization problem with $f^{(i)}$ defined in. We assume in this section that the mappings ${\mathbf{g}}^{(i)}$ defined in are affine. Problem now reads

For a single input ($n = 1$), the problem reads

where $h$ is a simple non-smooth convex function and $\lambda \geq 0$. Nesterov first analyzed such setting: while the problem suffers from its non-smoothness, fast methods can be developed by considering smooth approximations of the objectives. We combine this idea with the Catalyst acceleration scheme to accelerate a linearly convergent smooth optimization algorithm resulting in a scheme called Casimir.

### Casimir: Catalyst with Smoothing

The Catalyst approach minimizes regularized objectives centered around the current iterate. The algorithm proceeds by computing approximate proximal point steps instead of the classical (sub)-gradient steps. A proximal point step from a point $\mathbf{w}$ with step-size $\kappa^{- 1}$ is defined as the minimizer of

which can also be seen as a gradient step on the Moreau envelope of $F$ - see Lin et al. for a detailed discussion. While solving the subproblem might be as hard as the original problem we only require an approximate solution returned by a given optimization method $\mathcal{M}$. The Catalyst approach is then an inexact accelerated proximal point algorithm that carefully mixes approximate proximal point steps with the extrapolation scheme of Nesterov. The Casimir scheme extends this approach to non-smooth optimization.

For the overall method to be efficient, subproblems must have a low complexity. That is, there must exist an optimization algorithm $\mathcal{M}$ that solves them linearly. For the Casimir approach to be able to handle non-smooth objectives, it means that we need not only to regularize the objective but also to smooth it. To this end we define

as a smooth approximation of the objective $F$, and,

a smooth and regularized approximation of the objective centered around a given point ${\mathbf{z}} \in {\mathbb{R}}^{d}$. While the original Catalyst algorithm considered a fixed regularization term $\kappa$, we vary $\kappa$ and $\mu$ along the iterations. This enables us to get adaptive smoothing strategies.

The overall method is presented in Algo. 4. We first analyze in Sec. 5.2 its complexity for a generic linearly convergent algorithm $\mathcal{M}$. Thereafter, in Sec. 5.3, we compute the total complexity with SVRG as $\mathcal{M}$. Before that, we specify two practical aspects of the implementation: a proper stopping criterion and a good initialization of subproblems (Line 4).

### Stopping Criterion

Following Lin et al., we solve subproblem $k$ in Line 4 to a degree of relative accuracy specified by $\delta_{k} \in {\lbrack 0,1)}$. In view of the $({\lambda + \kappa_{k}})$-strong convexity of $F_{{\mu_{k}\omega},\kappa_{k}}{( \cdot;{\mathbf{z}}_{k - 1})}$, the functional gap can be controlled by the norm of the gradient, precisely it can be seen that ${\|{{\nabla F_{{\mu_{k}\omega},\kappa_{k}}}{(\hat{\mathbf{w}};{\mathbf{z}}_{k - 1})}}\|}_{2}^{2} \leq {{({\lambda + \kappa_{k}})}\delta_{k}\kappa_{k}{\|{\hat{\mathbf{w}} - {\mathbf{z}}_{k - 1}}\|}_{2}^{2}}$ is a sufficient condition for the stopping criterion.

A practical alternate stopping criterion proposed by Lin et al. is to fix an iteration budget $T_{budget}$ and run the inner solver $\mathcal{M}$ for exactly $T_{budget}$ steps. We do not have a theoretical analysis for this scheme but find that it works well in experiments.

### Warm Start of Subproblems

Rate of convergence of first order optimization algorithms depends on the initialization and we must warm start $\mathcal{M}$ at an appropriate initial point in order to obtain the best convergence of subproblem in Line 4 of Algo. 4. We advocate the use of the prox center ${\mathbf{z}}_{k - 1}$ in iteration $k$ as the warm start strategy. We also experiment with other warm start strategies in Section 7.

1: Input: Smoothable objective F of the form with h simple, smoothing function ω, linearly convergent algorithm ℳ, non-negative and non-increasing sequence of smoothing parameters (μk)k ≥ 1, positive and non-decreasing sequence of regularization parameters (κk)k ≥ 1, non-negative sequence of relative target accuracies (δk)k ≥ 1 and, initial point w0, α0 ∈, time horizon K.
4: Using ℳ with zk − 1 as the starting point, find ${\mathbf{w}}_{k} \approx {{\underset{{\mathbf{w}} \in {\mathbb{R}}^{d}}{\arg\min}F_{{\mu_{k}\omega},\kappa_{k}}}{({\mathbf{w}};{\mathbf{z}}_{k - 1})}}$ where

$${F_{{\mu_{k}\omega},\kappa_{k}}{({\mathbf{w}};{\mathbf{z}}_{k - 1})}}:={{\frac{1}{n}{\sum\limits_{i = 1}^{n}{h_{\mu_{k}\omega}{({{{\mathbf{A}}^{(i)}{\mathbf{w}}} + {\mathbf{b}}^{(i)}})}}}} + {\frac{\lambda}{2}{\|{\mathbf{w}}\|}_{2}^{2}} + {\frac{\kappa_{k}}{2}{\|{{\mathbf{w}} - {\mathbf{z}}_{k - 1}}\|}_{2}^{2}}}$$

${{F_{{\mu_{k}\omega},\kappa_{k}}{({\mathbf{w}}_{k};{\mathbf{z}}_{k - 1})}} - {{\min\limits_{\mathbf{w}}F_{{\mu_{k}\omega},\kappa_{k}}}{({\mathbf{w}};{\mathbf{z}}_{k - 1})}}} \leq {\frac{\delta_{k}\kappa_{k}}{2}{\|{{\mathbf{w}}_{k} - {\mathbf{z}}_{k - 1}}\|}_{2}^{2}}$

${\beta_{k} = \frac{\alpha_{k - 1}{({1 - \alpha_{k - 1}})}{({\kappa_{k} + \lambda})}}{{\alpha_{k - 1}^{2}{({\kappa_{k} + \lambda})}} + {\alpha_{k}{({\kappa_{k + 1} + \lambda})}}}}.$

Algorithm 4 The Casimir algorithm

### Convergence Analysis of Casimir

We first state the outer loop complexity results of Algo. 4 for any generic linearly convergent algorithm $\mathcal{M}$ in Sec. 5.2.1, prove it in Sec. 5.2.2. Then, we consider the complexity of each inner optimization problem in Sec. 5.2.3 based on properties of $\mathcal{M}$.

### Outer Loop Complexity Results

The following theorem states the convergence of the algorithm for general choice of parameters, where we denote ${\mathbf{w}}^{\ast} \in {{\underset{{\mathbf{w}} \in {\mathbb{R}}^{d}}{\arg\min}F}{({\mathbf{w}})}}$ and $F^{\ast} = {F{({\mathbf{w}}^{\ast})}}$.

### Theorem 16

Consider Problem. Suppose $\delta_{k} \in {\lbrack 0,1)}$ for all $k \geq 1$, the sequence ${(\mu_{k})}_{k \geq 1}$ is non-negative and non-increasing, and the sequence ${(\kappa_{k})}_{k \geq 1}$ is strictly positive and non-decreasing. Further, suppose the smoothing function $\omega:{{\operatorname{dom}h^{\ast}}\rightarrow{\mathbb{R}}}$ satisfies ${- D_{\omega}} \leq {\omega{(\mathbf{u})}} \leq 0$ for all $\mathbf{u} \in {\operatorname{dom}h^{\ast}}$ and that $\alpha_{0}^{2} \geq {\lambda/{({\lambda + \kappa_{1}})}}$. Then, the sequence ${(\alpha_{k})}_{k \geq 0}$ generated by Algo. 4 satisfies $0 < \alpha_{k} \leq \alpha_{k - 1} < 1$ for all $k \geq 1$. Furthermore, the sequence ${(\mathbf{w}_{k})}_{k \geq 0}$ of iterates generated by Algo. 4 satisfies

where $\mathcal{A}_{i}^{j}:={\prod_{r = i}^{j}{({1 - \alpha_{r}})}}$, $\mathcal{B}_{i}^{j}:={\prod_{r = i}^{j}{({1 - \delta_{r}})}}$, $\Delta_{0}:={{{F{(\mathbf{w}_{0})}} - F^{\ast}} + {\frac{{{({\kappa_{1} + \lambda})}\alpha_{0}^{2}} - {\lambda\alpha_{0}}}{2{({1 - \alpha_{0}})}}{\|{\mathbf{w}_{0} - \mathbf{w}^{\ast}}\|}_{2}^{2}}}$ and $\mu_{0}:={2\mu_{1}}$.

Before giving its proof, we present various parameters strategies as corollaries. Table 3 summarizes the parameter settings and the rates obtained for each setting. Overall, the target accuracies $\delta_{k}$ are chosen such that $\mathcal{B}_{j}^{k}$ is a constant and the parameters $\mu_{k}$ and $\kappa_{k}$ are then carefully chosen for an almost parameter-free algorithm with the right rate of convergence. Proofs of these corollaries are provided in Appendix D.2.

The first corollary considers the strongly convex case ($\lambda > 0$) with constant smoothing $\mu_{k} = \mu$, assuming that $\epsilon$ is known a priori. We note that this is, up to constants, the same complexity obtained by the original Catalyst scheme on a fixed smooth approximation $F_{\mu\omega}$ with $\mu = {\mathcal{O}{({\epsilonD_{\omega}})}}$.

### Corollary 17

Consider the setting of Thm. 16. Let $q = {\lambda/{({\lambda + \kappa})}}$. Suppose $\lambda > 0$ and $\mu_{k} = \mu$, $\kappa_{k} = \kappa$, for all $k \geq 1$. Choose $\alpha_{0} = \sqrt{q}$ and, ${\delta_{k} = {\sqrt{q}/{({2 - \sqrt{q}})}}}.$ Then, we have,

Next, we consider the strongly convex case where the target accuracy $\epsilon$ is not known in advance. We let smoothing parameters ${(\mu_{k})}_{k \geq 0}$ decrease over time to obtain an adaptive smoothing scheme that gives progressively better surrogates of the original objective.

### Corollary 18

Consider the setting of Thm. 16. Let $q = {\lambda/{({\lambda + \kappa})}}$ and $\eta = {1 - {\sqrt{q}/2}}$. Suppose $\lambda > 0$ and $\kappa_{k} = \kappa$, for all $k \geq 1$. Choose $\alpha_{0} = \sqrt{q}$ and, the sequences ${(\mu_{k})}_{k \geq 1}$ and ${(\delta_{k})}_{k \geq 1}$ as

where $\mu > 0$ is any constant. Then, we have,

The next two corollaries consider the unregularized problem, i.e., $\lambda = 0$ with constant and adaptive smoothing respectively.

### Corollary 19

Consider the setting of Thm. 16. Suppose $\mu_{k} = \mu$, $\kappa_{k} = \kappa$, for all $k \geq 1$ and $\lambda = 0$. Choose $\alpha_{0} = {{({\sqrt{5} - 1})}/2}$ and ${\delta_{k} = {({k + 1})}^{- 2}}.$ Then, we have,

### Corollary 20

Consider the setting of Thm. 16 with $\lambda = 0$. Choose $\alpha_{0} = {{({\sqrt{5} - 1})}/2}$, and for some non-negative constants $\kappa,\mu$, define sequences ${(\kappa_{k})}_{k \geq 1},{(\mu_{k})}_{k \geq 1},{(\delta_{k})}_{k \geq 1}$ as

Then, for $k \geq 2$, we have,

For the first iteration (i.e., $k = 1$), this bound is off by a constant factor $1/{\log 2}$.

Cor. λ &gt; 0 κk μk δk α0 F (wk) − F* Remark 17 Yes κ μ $\frac{\sqrt{q}}{2 - \sqrt{q}}$ $\sqrt{q}$ ${\left( {1 - \frac{\sqrt{q}}{2}} \right)^{k}\DeltaF_{0}} + \frac{\muD}{1 - \sqrt{q}}$ $q = \frac{\lambda}{\lambda + \kappa}$ 18 Yes κ $\mu\left( {1 - \frac{\sqrt{q}}{2}} \right)^{k/2}$ $\frac{\sqrt{q}}{2 - \sqrt{q}}$ $\sqrt{q}$ $\left( {1 - \frac{\sqrt{q}}{2}} \right)^{k/2}\left( {{\DeltaF_{0}} + \frac{\muD}{1 - \sqrt{q}}} \right)$ $q = \frac{\lambda}{\lambda + \kappa}$ 19 No κ μ k−2 c ${\frac{1}{k^{2}}\left( {{\DeltaF_{0}} + {\kappa\Delta_{0}^{2}}} \right)} + {\muD}$ $c = {{({\sqrt{5} - 1})}/2}$ 20 No κ k μ/k k−2 c $\frac{\log k}{k}{({{\DeltaF_{0}} + {\kappa\Delta_{0}^{2}} + {\muD}})}$ $c = {{({\sqrt{5} - 1})}/2}$
Table 3: Summary of outer iteration complexity for Algorithm 4 for different parameter settings. We use shorthand Δ F0:= F (w0) − F* and Δ0 = ∥w0 − w*∥2. Absolute constants are omitted from the rates.

### Outer Loop Convergence Analysis

We now prove Thm. 16. The proof technique largely follows that of Lin et al., with the added challenges of accounting for smoothing and varying Moreau-Yosida regularization. We first analyze the sequence ${(\alpha_{k})}_{k \geq 0}$. The proof follows from the algebra of Eq. and has been given in Appendix D.1_{𝑘≥0} ‣ Appendix D The Casimir Algorithm and Non-Convex Extensions: Missing Proofs ‣ A Smoother Way to Train Structured Prediction Models").

### Lemma 21

Given a positive, non-decreasing sequence ${(\kappa_{k})}_{k \geq 1}$ and $\lambda \geq 0$, consider the sequence ${(\alpha_{k})}_{k \geq 0}$ defined by, where $\alpha_{0} \in {}$ such that $\alpha_{0}^{2} \geq {\lambda/{({\lambda + \kappa_{1}})}}$. Then, we have for every $k \geq 1$ that $0 < \alpha_{k} \leq \alpha_{k - 1}$ and, ${\alpha_{k}^{2} \geq {\lambda/{({\lambda + \kappa_{k + 1}})}}}.$

We now characterize the effect of an approximate proximal point step on $F_{\mu\omega}$.

### Lemma 22

Suppose $\hat{\mathbf{w}} \in {\mathbb{R}}^{d}$ satisfies ${{F_{{\mu\omega},\kappa}{(\hat{\mathbf{w}};\mathbf{z})}} - {{\min_{\mathbf{w} \in {\mathbb{R}}^{d}}F_{{\mu\omega},\kappa}}{(\mathbf{w};\mathbf{z})}}} \leq \hat{\epsilon}$ for some $\hat{\epsilon} > 0$. Then, for all $0 < \theta < 1$ and all $\mathbf{w} \in {\mathbb{R}}^{d}$, we have,

### Proof

Let ${\hat{F}}^{\ast} = {{\min_{{\mathbf{w}} \in {\mathbb{R}}^{d}}F_{{\mu\omega},\kappa}}{({\mathbf{w}};{\mathbf{z}})}}$. Let ${\hat{\mathbf{w}}}^{\ast}$ be the unique minimizer of $F_{{\mu\omega},\kappa}{( \cdot;{\mathbf{z}})}$. We have, from $({\kappa + \lambda})$-strong convexity of $F_{{\mu\omega},\kappa}{( \cdot;{\mathbf{z}})}$,

where we used that $\hat{\epsilon}$ was sub-optimality of $\hat{\mathbf{w}}$ and Lemma 51 from Appendix D.7. From $({\kappa + \lambda})$-strong convexity of $F_{{\mu\omega},\kappa}{( \cdot;{\mathbf{z}})}$, we have,

Since $({{1/\theta} - 1})$ is non-negative, we can plug this into the previous statement to get,

Substituting the definition of $F_{{\mu\omega},\kappa}{( \cdot;{\mathbf{z}})}$ from completes the proof. ∎

We now define a few auxiliary sequences integral to the proof. Define sequences ${({\mathbf{v}}_{k})}_{k \geq 0}$, ${(\gamma_{k})}_{k \geq 0}$, ${(\eta_{k})}_{k \geq 0}$, and ${({\mathbf{r}}_{k})}_{k \geq 1}$ as

One might recognize $\gamma_{k}$ and ${\mathbf{v}}_{k}$ from their resemblance to counterparts from the proof of Nesterov. Now, we claim some properties of these sequences.

### Claim 23

For the sequences defined in -, we have,

### Proof

Eq. follows from plugging in in for $k \geq 1$, while for $k = 0$, it is true by definition. Eq. follows from plugging in. Eq. follows from and. Lastly, to show, we shall show instead that is equivalent to the update for ${\mathbf{z}}_{k}$. We have,

completing the proof. ∎

### Claim 24

The sequence ${(\mathbf{r}_{k})}_{k \geq 1}$ from satisfies

### Proof

Notice that $\eta_{k}\overset{()}{=}{\alpha_{k} \cdot \frac{\gamma_{k}}{\gamma_{k} + {\alpha_{k}\lambda}}} \leq \alpha_{k}$. Hence, using convexity of the squared Euclidean norm, we get,

For all $\mu \geq \mu^{\prime} \geq 0$, we know from Prop. 2 that

We now define the sequence ${(S_{k})}_{k \geq 0}$ to play the role of a potential function here.

We are now ready to analyze the effect of one outer loop. This lemma is the crux of the analysis.

### Lemma 25

Suppose ${{F_{{\mu_{k}\omega},\kappa_{k}}{(\mathbf{w}_{k};\mathbf{z})}} - {{\min_{\mathbf{w} \in {\mathbb{R}}^{d}}F_{{\mu_{k}\omega},\kappa_{k}}}{(\mathbf{w};\mathbf{z})}}} \leq \epsilon_{k}$ for some $\epsilon_{k} > 0$. The following statement holds for all $0 < \theta_{k} < 1$:

### Proof

For ease of notation, let $F_{k}:=F_{\mu_{k}\omega}$, and $D:=D_{\omega}$. By $\lambda$-strong convexity of $F_{\mu_{k}\omega}$, we have,

We now invoke Lemma 22 on the function $F_{{\mu_{k}\omega},\kappa_{k}}{( \cdot;{\mathbf{z}}_{k - 1})}$ with $\hat{\epsilon} = \epsilon_{k}$ and ${\mathbf{w}} = {\mathbf{r}}_{k}$ to get,

We shall separately manipulate the left and right hand sides of, starting with the right hand side, which we call $\mathcal{R}$. We have, using and,

We notice now that

and hence the terms containing ${\|{{\mathbf{w}}_{k - 1} - {\mathbf{w}}^{\ast}}\|}_{2}^{2}$ cancel out. Therefore, we get,

To move on to the left hand side, we note that

Using ${{\mathbf{r}}_{k} - {\mathbf{w}}_{k}}\overset{()}{=}{\alpha_{k - 1}{({{\mathbf{w}}^{\ast} - {\mathbf{v}}_{k}})}}$, we simplify the left hand side of, which we call $\mathcal{L}$, as

In view of and (5.2.2), we can simplify as

We make a distinction for $k \geq 2$ and $k = 1$ here. For $k \geq 2$, the condition that $\mu_{k - 1} \geq \mu_{k}$ gives us,

The right hand side of can now be upper bounded by

and noting that ${1 - \alpha_{k - 1}} \leq 1$ yields for $k \geq 2$.

For $k = 1$, we note that $S_{k - 1}\mspace{7mu}{({= S_{0}})}$ is defined in terms of $F{({\mathbf{w}})}$. So we have,

because we used $\mu_{0} = {2\mu_{1}}$. This is of the same form as. Therefore, holds for $k = 1$ as well. ∎

We now prove Thm. 16.

### Proof of Thm. 16

We continue to use shorthand $F_{k}:=F_{\mu_{k}\omega}$, and $D:=D_{\omega}$. We now apply Lemma 25. In order to satisfy the supposition of Lemma 25 that ${\mathbf{w}}_{k}$ is $\epsilon_{k}$-suboptimal, we make the choice $\epsilon_{k} = {\frac{\delta_{k}\kappa_{k}}{2}{\|{{\mathbf{w}}_{k} - {\mathbf{z}}_{k - 1}}\|}_{2}^{2}}$ (cf. ). Plugging this in and setting $\theta_{k} = \delta_{k} < 1$, we get from,

The left hand side simplifies to ${{S_{k}{({1 - \delta_{k}})}}/{({1 - \alpha_{k}})}} + {\delta_{k}{({{F_{k}{({\mathbf{w}}_{k})}} - {F_{k}{({\mathbf{w}}^{\ast})}}})}}$. Note that ${{F_{k}{({\mathbf{w}}_{k})}} - {F_{k}{({\mathbf{w}}^{\ast})}}}\overset{()}{\geq}{{F{({\mathbf{w}}_{k})}} - {F{({\mathbf{w}}^{\ast})}} - {\mu_{k}D}} \geq {- {\mu_{k}D}}$. From this, noting that $\alpha_{k} \in {}$ for all $k$, we get,

Unrolling the recursion for $S_{k}$, we now have,

Now, we need to reason about $S_{0}$ and $S_{k}$ to complete the proof. To this end, consider $\eta_{0}$:

With this, we can expand out $S_{0}$ to get

Lastly, we reason about $S_{k}$ for $k \geq 1$ as,

Plugging this into the left hand side of completes the proof. ∎

### Inner Loop Complexity

Consider a class $\mathcal{F}_{L,\lambda}$ of functions defined as

We now formally define a linearly convergent algorithm on this class of functions.

### Definition 26

A first order algorithm $\mathcal{M}$ is said to be linearly convergent with parameters $C:{{{\mathbb{R}}_{+} \times {\mathbb{R}}_{+}}\rightarrow{\mathbb{R}}_{+}}$ and $\tau:{{{\mathbb{R}}_{+} \times {\mathbb{R}}_{+}}\rightarrow{}}$ if the following holds: for all $L \geq \lambda > 0$, and every $f \in \mathcal{F}_{L,\lambda}$ and $\mathbf{w}_{0} \in {\mathbb{R}}^{d}$, $\mathcal{M}$ started at $\mathbf{w}_{0}$ generates a sequence ${(\mathbf{w}_{k})}_{k \geq 0}$ that satisfies:

where $f^{\ast}:={{\min_{\mathbf{w} \in {\mathbb{R}}^{d}}f}{(\mathbf{w})}}$ and the expectation is over the randomness of $\mathcal{M}$.

The parameter $\tau$ determines the rate of convergence of the algorithm. For instance, batch gradient descent is a deterministic linearly convergent algorithm with ${\tau{(L,\lambda)}^{- 1}} = {L/\lambda}$ and incremental algorithms such as SVRG and SAGA satisfy requirement with ${\tau{(L,\lambda)}^{- 1}} = {c{({n + {L/\lambda}})}}$ for some universal constant $c$.

The warm start strategy in step $k$ of Algo. 4 is to initialize $\mathcal{M}$ at the prox center ${\mathbf{z}}_{k - 1}$. The next proposition, due to Lin et al. bounds the expected number of iterations of $\mathcal{M}$ required to ensure that ${\mathbf{w}}_{k}$ satisfies. Its proof has been given in Appendix D.3 for completeness.

### Proposition 27

Consider $F_{{\mu\omega},\kappa}{( \cdot;\mathbf{z})}$ defined in Eq., and a linearly convergent algorithm $\mathcal{M}$ with parameters $C$, $\tau$. Let $\delta \in {\lbrack 0,1)}$. Suppose $F_{\mu\omega}$ is $L_{\mu\omega}$-smooth and $\lambda$-strongly convex. Then the expected number of iterations ${\mathbb{E}}{\lbrack\hat{T}\rbrack}$ of $\mathcal{M}$ when started at $\mathbf{z}$ in order to obtain $\hat{\mathbf{w}} \in {\mathbb{R}}^{d}$ that satisfies

Prop. λ &gt; 0 μk κk δk 𝔼 [N] Remark 29 Yes ϵ/D A D/ϵ n − λ $\sqrt{\frac{\lambda\epsilonn}{AD}}$ $n + \sqrt{\frac{ADn}{\lambda\epsilon}}$ fix ϵ in advance 30 Yes μ ck λ c′ $n + {\frac{A}{\lambda\epsilon}\frac{{\DeltaF_{0}} + {\muD}}{\mu}}$ c, c′ &lt; 1 are universal constants 31 No ϵ/D A D/ϵ n 1/k2 ${n\sqrt{\frac{\DeltaF_{0}}{\epsilon}}} + \frac{\sqrt{ADn}\Delta_{0}}{\epsilon}$ fix ϵ in advance 32 No μ/k κ0 k 1/k2 $\frac{{\hat{\Delta}}_{0}}{\epsilon}\left( {n + \frac{A}{\mu\kappa_{0}}} \right)$ ${\hat{\Delta}}_{0} = {{\DeltaF_{0}} + {\frac{\kappa_{0}}{2}\Delta_{0}^{2}} + {\muD}}$
Table 4: Summary of global complexity of Casimir-SVRG, i.e., Algorithm 4 with SVRG as the inner solver for various parameter settings. We show 𝔼 [N], the expected total number of SVRG iterations required to obtain an accuracy ϵ, up to constants and factors logarithmic in problem parameters. We denote Δ F0:= F (w0) − F* and Δ0 = ∥w0 − w*∥2. Constants D, A are short for Dω, Aω (see ).

### Casimir with SVRG

We now choose SVRG to be the linearly convergent algorithm $\mathcal{M}$, resulting in an algorithm called Casimir-SVRG. The rest of this section analyzes the total iteration complexity of Casimir-SVRG to solve Problem. The proofs of the results from this section are calculations stemming from combining the outer loop complexity from Cor. 17 to 20 with the inner loop complexity from Prop. 27, and are relegated to Appendix D.4. Table 4 summarizes the results of this section.

Recall that if $\omega$ is 1-strongly convex with respect to $\parallel \cdot \parallel_{\alpha}$, then $h_{\mu\omega}{({{{\mathbf{A}}{\mathbf{w}}} + {\mathbf{b}}})}$ is $L_{\mu\omega}$-smooth with respect to $\parallel \cdot \parallel_{2}$, where $L_{\mu\omega} = {{\|{\mathbf{A}}\|}_{2,\alpha}^{2}/\mu}$. Therefore, the complexity of solving problem will depend on

### Remark 28

We have that ${\|\mathbf{A}\|}_{2,2} = {\|\mathbf{A}\|}_{2}$ is the spectral norm of $\mathbf{A}$ and ${\|\mathbf{A}\|}_{2,1} = {\max_{j}{\|\mathbf{a}_{j}\|}_{2}}$ is the largest row norm, where $\mathbf{a}_{j}$ is the $j$th row of $\mathbf{A}$. Moreover, we have that ${\|\mathbf{A}\|}_{2,2} \geq {\|\mathbf{A}\|}_{2,1}$.

We start with the strongly convex case with constant smoothing.

### Proposition 29

Consider the setting of Thm. 16 and fix $\epsilon > 0$. If we run Algo. 4 with SVRG as the inner solver with parameters: $\mu_{k} = \mu = {{\epsilon/10}D_{\omega}}$, $\kappa_{k} = k$ chosen as

$q = {\lambda/{({\lambda + \kappa})}}$, $\alpha_{0} = \sqrt{q}$, and $\delta = {\sqrt{q}/{({2 - \sqrt{q}})}}$. Then, the number of iterations $N$ to obtain $\mathbf{w}$ such that ${{F{(\mathbf{w})}} - {F{(\mathbf{w}^{\ast})}}} \leq \epsilon$ is bounded in expectation as

Here, we note that $\kappa$ was chosen to minimize the total complexity (cf. Lin et al. ). This bound is known to be tight, up to logarithmic factors. Next, we turn to the strongly convex case with decreasing smoothing.

### Proposition 30

Consider the setting of Thm. 16. Suppose $\lambda > 0$ and $\kappa_{k} = \kappa$, for all $k \geq 1$ and that $\alpha_{0}$, ${(\mu_{k})}_{k \geq 1}$ and ${(\delta_{k})}_{k \geq 1}$ are chosen as in Cor. 18, with $q = {\lambda/{({\lambda + \kappa})}}$ and $\eta = {1 - {\sqrt{q}/2}}$. If we run Algo. 4 with SVRG as the inner solver with these parameters, the number of iterations $N$ of SVRG required to obtain $\mathbf{w}$ such that ${{F{(\mathbf{w})}} - F^{\ast}} \leq \epsilon$ is bounded in expectation as

Unlike the previous case, there is no obvious choice of $\kappa$, such as to minimize the global complexity. Notice that we do not get the accelerated rate of Prop. 29. We now turn to the case when $\lambda = 0$ and $\mu_{k} = \mu$ for all $k$.

### Proposition 31

Consider the setting of Thm. 16 and fix $\epsilon > 0$. If we run Algo. 4 with SVRG as the inner solver with parameters: $\mu_{k} = \mu = {{\epsilon/20}D_{\omega}}$, $\alpha_{0} = {{({\sqrt{5} - 1})}/2}$, $\delta_{k} = {1/{({k + 1})}^{2}}$, and $\kappa_{k} = \kappa = {{A_{\omega}/\mu}{({n + 1})}}$. Then, the number of iterations $N$ to get a point $\mathbf{w}$ such that ${{F{(\mathbf{w})}} - F^{\ast}} \leq \epsilon$ is bounded in expectation as

This rate is tight up to log factors. Lastly, we consider the non-strongly convex case ($\lambda = 0$) together with decreasing smoothing. As with Prop. 30, we do not obtain an accelerated rate here.

### Proposition 32

Consider the setting of Thm. 16. Suppose $\lambda = 0$ and that $\alpha_{0}$, ${(\mu_{k})}_{k \geq 1}$,${(\kappa_{k})}_{k \geq 1}$ and ${(\delta_{k})}_{k \geq 1}$ are chosen as in Cor. 20. If we run Algo. 4 with SVRG as the inner solver with these parameters, the number of iterations $N$ of SVRG required to obtain $\mathbf{w}$ such that ${{F{(\mathbf{w})}} - F^{\ast}} \leq \epsilon$ is bounded in expectation as

## Extension to Non-Convex Optimization

Let us now turn to the optimization problem in full generality where the mappings ${\mathbf{g}}^{(i)}$ defined in are not constrained to be affine:

where $h$ is a simple, non-smooth, convex function, and each ${\mathbf{g}}^{(i)}$ is a continuously differentiable nonlinear map and $\lambda \geq 0$.

We describe the prox-linear algorithm in Sec. 6.1, followed by the convergence guarantee in Sec. 6.2 and the total complexity of using Casimir-SVRG together with the prox-linear algorithm in Sec. 6.3.

### The Prox-Linear Algorithm

The exact prox-linear algorithm of Burke generalizes the proximal gradient algorithm (see e.g., Nesterov ) to compositions of convex functions with smooth mappings such as. When given a function $f = {h \circ {\mathbf{g}}}$, the prox-linear algorithm defines a local convex approximation $f{( \cdot;{\mathbf{w}}_{k})}$ about some point ${\mathbf{w}} \in {\mathbb{R}}^{d}$ by linearizing the smooth map $\mathbf{g}$ as ${{f{({\mathbf{w}};{\mathbf{w}}_{k})}}:={h{({{{\mathbf{g}}{({\mathbf{w}}_{k})}} + {{\nabla{\mathbf{g}}}{({\mathbf{w}}_{k})}{({{\mathbf{w}} - {\mathbf{w}}_{k}})}}})}}}.$ With this, it builds a convex model $F{( \cdot;{\mathbf{w}}_{k})}$ of $F$ about ${\mathbf{w}}_{k}$ as

Given a step length $\eta > 0$, each iteration of the exact prox-linear algorithm then minimizes the local convex model plus a proximal term as

1: Input: Smoothable objective F of the form with h simple, step length η, tolerances (ϵk)k ≥ 1, initial point w0, non-smooth convex optimization algorithm, ℳ, time horizon K
3: Using ℳ with wk − 1 as the starting point, find

${\hat{\mathbf{w}}}_{k} \approx \underset{\mathbf{w}}{\arg\min}\left\lbrack F_{\eta}{({\mathbf{w}};{\mathbf{w}}_{k - 1})}:=\frac{1}{n}\sum\limits_{i = 1}^{n} \right.$

$\left. + \frac{\lambda}{2} \parallel {\mathbf{w}} \parallel_{2}^{2} + \frac{1}{2\eta} \parallel {\mathbf{w}} - {\mathbf{w}}_{k - 1} \parallel_{2}^{2}, \right\rbrack$

${{{F_{\eta}{({\hat{\mathbf{w}}}_{k};{\mathbf{w}}_{k - 1})}} - {{\min\limits_{{\mathbf{w}} \in {\mathbb{R}}^{d}}F_{\eta}}{({\mathbf{w}};{\mathbf{w}}_{k - 1})}}} \leq \epsilon_{k}}.$

4: Set ${\mathbf{w}}_{k} = {\hat{\mathbf{w}}}_{k}$ if ${F{({\hat{\mathbf{w}}}_{k})}} \leq {F{({\mathbf{w}}_{k - 1})}}$, else set wk = wk − 1.
Algorithm 5 (Inexact) Prox-linear algorithm: outer loop

Following Drusvyatskiy and Paquette, we consider an inexact prox-linear algorithm, which approximately solves using an iterative algorithm. In particular, since the function to be minimized in is precisely of the form, we employ the fast convex solvers developed in the previous section as subroutines. Concretely, the prox-linear outer loop is displayed in Algo. 5. We now delve into details about the algorithm and convergence guarantees.

### Inexactness Criterion

As in Section 5, we must be prudent in choosing when to terminate the inner optimization (Line 3 of Algo. 5). Function value suboptimality is used as the inexactness criterion here. In particular, for some specified tolerance $\epsilon_{k} > 0$, iteration $k$ of the prox-linear algorithm accepts a solution $\hat{\mathbf{w}}$ that satisfies ${{F_{\eta}{({\hat{\mathbf{w}}}_{k};{\mathbf{w}}_{k - 1})}} - {{\min_{\mathbf{w}}F_{\eta}}{({\mathbf{w}};{\mathbf{w}}_{k - 1})}}} \leq \epsilon_{k}$.

### Implementation

In view of the $({\lambda + \eta^{- 1}})$-strong convexity of $F_{\eta}{( \cdot;{\mathbf{w}}_{k - 1})}$, it suffices to ensure that ${{({\lambda + \eta^{- 1}})}{\|{\mathbf{v}}\|}_{2}^{2}} \leq \epsilon_{k}$ for a subgradient ${\mathbf{v}} \in {\partial{F_{\eta}{({\hat{\mathbf{w}}}_{k};{\mathbf{w}}_{k - 1})}}}$.

### Fixed Iteration Budget

As in the convex case, we consider as a practical alternative a fixed iteration budget $T_{budget}$ and optimize $F_{\eta}{( \cdot;{\mathbf{w}}_{k})}$ for exactly $T_{budget}$ iterations of $\mathcal{M}$. Again, we do not have a theoretical analysis for this scheme but find it to be effective in practice.

### Warm Start of Subproblems

As in the convex case, we advocate the use of the prox center ${\mathbf{w}}_{k - 1}$ to warm start the inner optimization problem in iteration $k$ (Line 3 of Algo. 5).

### Convergence analysis of the prox-linear algorithm

We now state the assumptions and the convergence guarantee of the prox-linear algorithm.

### Assumptions

For the prox-linear algorithm to work, the only requirement is that we minimize an upper model. The assumption below makes this concrete.

### Assumption 33

The map $\mathbf{g}^{(i)}$ is continuously differentiable everywhere for each $i \in {\lbrack n\rbrack}$. Moreover, there exists a constant $L > 0$ such that for all ${\mathbf{w},\mathbf{w}^{\prime}} \in {\mathbb{R}}^{d}$ and $i \in {\lbrack n\rbrack}$, it holds that

When $h$ is $G$-Lipschitz and each ${\mathbf{g}}^{(i)}$ is $\overset{\sim}{L}$-smooth, both with respect to $\parallel \cdot \parallel_{2}$, then Assumption 33 holds with $L = {G\overset{\sim}{L}}$. In the case of structured prediction, Assumption 33 holds when the augmented score $\psi$ as a function of $\mathbf{w}$ is $L$-smooth. The next lemma makes this precise and its proof is in Appendix D.5.

### Lemma 34

Consider the structural hinge loss ${f{(\mathbf{w})}} = {{\max_{\mathbf{y} \in \mathcal{Y}}\psi}{(\mathbf{y};\mathbf{w})}} = {{h \circ \mathbf{g}}{(\mathbf{w})}}$ where $h,\mathbf{g}$ are as defined in. If the mapping $\mathbf{w}\mapsto{\psi{(\mathbf{y};\mathbf{w})}}$ is $L$-smooth with respect to $\parallel \cdot \parallel_{2}$ for all $\mathbf{y} \in \mathcal{Y}$, then it holds for all ${\mathbf{w},\mathbf{z}} \in {\mathbb{R}}^{d}$ that

### Convergence Guarantee

Convergence is measured via the norm of the prox-gradient $\mathbf{\varrho}_{\eta}{( \cdot )}$, also known as the gradient mapping, defined as

The measure of stationarity $\|{\mathbf{\varrho}_{\eta}{({\mathbf{w}})}}\|$ turns out to be related to the norm of the gradient of the Moreau envelope of $F$ under certain conditions - see Drusvyatskiy and Paquette for a discussion. In particular, a point $\mathbf{w}$ with small $\|{\mathbf{\varrho}_{\eta}{({\mathbf{w}})}}\|$ means that $\mathbf{w}$ is close to ${\mathbf{w}}^{\prime} = {{\underset{{\mathbf{z}} \in {\mathbb{R}}^{d}}{\arg\min}F_{\eta}}{({\mathbf{z}};{\mathbf{w}})}}$, which is nearly stationary for $F$.

The prox-linear outer loop shown in Algo. 5 has the following convergence guarantee.

### Theorem 35

Consider $F$ of the form that satisfies Assumption 33, a step length $0 < \eta \leq {1/L}$ and a non-negative sequence ${(\epsilon_{k})}_{k \geq 1}$. With these inputs, Algo. 5 produces a sequence ${(\mathbf{w}_{k})}_{k \geq 0}$ that satisfies

where $F^{\ast} = {\inf_{\mathbf{w} \in {\mathbb{R}}^{d}}{F{(\mathbf{w})}}}$. In addition, we have that the sequence ${({F{(\mathbf{w}_{k})}})}_{k \geq 0}$ is non-increasing.

### Remark 36

Algo. 5 accepts an update only if it improves the function value (Line 4). A variant of Algo. 5 which always accepts the update has a guarantee identical to that of Thm. 35, but the sequence ${({F{(\mathbf{w}_{k})}})}_{k \geq 0}$ would not guaranteed to be non-increasing.

### Prox-Linear with Casimir-SVRG

We now analyze the total complexity of minimizing the finite sum problem with Casimir-SVRG to approximately solve the subproblems of Algo. 5.

For the algorithm to converge, the map ${\mathbf{w}}\mapsto{{{\mathbf{g}}^{(i)}{({\mathbf{w}}_{k})}} + {{\nabla{\mathbf{g}}^{(i)}}{({\mathbf{w}}_{k})}{({{\mathbf{w}} - {\mathbf{w}}_{k}})}}}$ must be Lipschitz for each $i$ and each iterate ${\mathbf{w}}_{k}$. To be precise, we assume that

is finite, where $\omega$, the smoothing function, is 1-strongly convex with respect to $\parallel \cdot \parallel_{\alpha}$. When ${\mathbf{g}}^{(i)}$ is the linear map ${\mathbf{w}}\mapsto{{\mathbf{A}}^{(i)}{\mathbf{w}}}$, this reduces to.

We choose the tolerance $\epsilon_{k}$ to decrease as $1/k$. When using the Casimir-SVRG algorithm with constant smoothing (Prop. 29) as the inner solver, this method effectively smooths the $k$th prox-linear subproblem as $1/k$. We have the following rate of convergence for this method, which is proved in Appendix D.6.

### Proposition 37

Consider the setting of Thm. 35. Suppose the sequence ${(\epsilon_{k})}_{k \geq 1}$ satisfies $\epsilon_{k} = {\epsilon_{0}/k}$ for some $\epsilon_{0} > 0$ and that the subproblem of Line 3 of Algo. 5 is solved using Casimir-SVRG with the settings of Prop. 29. Then, total number of SVRG iterations $N$ required to produce a $\mathbf{w}$ such that ${\|{\mathbf{\varrho}_{\eta}{(\mathbf{w})}}\|}_{2} \leq \epsilon$ is bounded as

### Remark 38

When an estimate or an upper bound $B$ on ${F{(\mathbf{w}_{0})}} - F^{\ast}$, one could set $\epsilon_{0} = {\mathcal{O}{(B)}}$. This is true, for instance, in the structured prediction task where $F^{\ast} \geq 0$ whenever the task loss $\ell$ is non-negative (cf. ).

## Experiments

In this section, we study the experimental behavior of the proposed algorithms on two structured prediction tasks, namely named entity recognition and visual object localization. Recall that given training examples ${\{{({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)})}\}}_{i = 1}^{n}$, we wish to solve the problem:

Note that we now allow the output space $\mathcal{Y}{({\mathbf{x}})}$ to depend on the instance $\mathbf{x}$ - the analysis from the previous sections applies to this setting as well. In all the plots, the shaded region represents one standard deviation over ten random runs.

We compare the performance of various optimization algorithms based on the number of calls to a smooth inference oracle. Moreover, following literature for algorithms based on SVRG, we exclude the cost of computing the full gradients.

The results must be interpreted keeping in mind that the running time of all inference oracles is not the same. These choices were motivated by the following reasons, which may not be appropriate in all contexts. The ultimate yardstick to benchmark the performance of optimization algorithms is wall clock time. However, this depends heavily on implementation, system and ambient system conditions. With regards to the differing running times of different oracles, we find that a small value of $K$, e.g., 5 suffices, so that our highly optimized implementations of the top-$K$ oracle incurs negligible running time penalties over the max oracle. Moreover, the computations of the batch gradient have been neglected as they are embarrassingly parallel.

The outline of the rest of this section is as follows. First, we describe the datasets and task description in Sec. 7.1, followed by methods compared in Sec. 7.2 and their hyperparameter settings in Sec. 7.3. Lastly, Sec. 7.4 presents the experimental studies.

### Dataset and Task Description

For each of the tasks, we specify below the following: (a) the dataset ${\{{({\mathbf{x}}^{(i)},{\mathbf{y}}^{(i)})}\}}_{i = 1}^{n}$, (b) the output structure $\mathcal{Y}$, (c) the loss function $\ell$, (d) the score function $\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}$, (e) implementation of inference oracles, and lastly, (f) the evaluation metric used to assess the quality of predictions.

### CoNLL 2003: Named Entity Recognition

Named entities are phrases that contain the names of persons, organization, locations, etc, and the task is to predict the label (tag) of each entity. Named entity recognition can be formulated as a sequence tagging problem where the set $\mathcal{Y}_{tag}$ of individual tags is of size 7.

Each datapoint $\mathbf{x}$ is a sequence of words ${\mathbf{x}} = {(x_{1},\cdots,x_{p})}$, and the label ${\mathbf{y}} = {(y_{1},\cdots,y_{p})} \in {\mathcal{Y}{({\mathbf{x}})}}$ is a sequence of the same length, where each $y_{i} \in \mathcal{Y}_{tag}$ is a tag.

### Loss Function

The loss function is the Hamming Loss ${\ell{({\mathbf{y}},{\mathbf{y}}^{\prime})}} = {\sum_{i}{\mathbb{I}{({y_{i} \neq y_{i}^{\prime}})}}}$.

### Score Function

We use a chain graph to represent this task. In other words, the observation-label dependencies are encoded as a Markov chain of order 1 to enable efficient inference using the Viterbi algorithm. We only consider the case of linear score ${\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}} = {\langle{\mathbf{w}},{\Phi{({\mathbf{x}},{\mathbf{y}})}}\rangle}$ for this task. The feature map $\Phi$ here is very similar to that given in Example 5. ‣ 3.1 Score Functions ‣ 3 Inference Oracles ‣ A Smoother Way to Train Structured Prediction Models"). Following Tkachenko and Simanovsky, we use local context $\Psi_{i}{({\mathbf{x}})}$ around $i$^th^ word $x_{i}$ of $\mathbf{x}$. In particular, define ${\Psi_{i}{({\mathbf{x}})}} = {{\mathbf{e}}_{x_{i - 2}} \otimes \cdots \otimes {\mathbf{e}}_{x_{i + 2}}}$, where $\otimes$ denotes the Kronecker product between column vectors, and ${\mathbf{e}}_{x_{i}}$ denotes a one hot encoding of word $x_{i}$, concatenated with the one hot encoding of its the part of speech tag and syntactic chunk tag which are provided with the input. Now, we can define the feature map $\Phi$ as

where ${\mathbf{e}}_{y} \in {\mathbb{R}}^{|\mathcal{Y}_{tag}|}$ is a one hot-encoding of $y \in \mathcal{Y}_{tag}$, and $\oplus$ denotes vector concatenation.

### Inference

We use the Viterbi algorithm as the max oracle (Algo. 1) and top-$K$ Viterbi algorithm (Algo. 2) for the top-$K$ oracle.

### Dataset

The dataset used was CoNLL 2003, which contains about $\sim {20K}$ sentences.

### Evaluation Metric

We follow the official CoNLL metric: the $F_{1}$ measure excluding the 'O' tags. In addition, we report the objective function value measured on the training set ("train loss").

### Other Implementation Details

The sparse feature vectors obtained above are hashed onto $2^{16} - 1$ dimensions for efficiency.

### PASCAL VOC 2007: Visual Object Localization

Given an image and an object of interest, the task is to localize the object in the given image, i.e., determine the best bounding box around the object. A related, but harder task is object detection, which requires identifying and localizing any number of objects of interest, if any, in the image. Here, we restrict ourselves to pure localization with a single instance of each object. Given an image ${\mathbf{x}} \in \mathcal{X}$ of size $n_{1} \times n_{2}$, the label ${\mathbf{y}} \in {\mathcal{Y}{({\mathbf{x}})}}$ is a bounding box, where $\mathcal{Y}{({\mathbf{x}})}$ is the set of all bounding boxes in an image of size $n_{1} \times n_{2}$. Note that ${|{\mathcal{Y}{({\mathbf{x}})}}|} = {\mathcal{O}{({n_{1}^{2}n_{2}^{2}})}}$.

### Loss Function

The PASCAL IoU metric is used to measure the quality of localization. Given bounding boxes ${\mathbf{y}},{\mathbf{y}}^{\prime}$, the IoU is defined as the ratio of the intersection of the bounding boxes to the union:

We then use the $1 - {IoU}$ loss defined as ${\ell{({\mathbf{y}},{\mathbf{y}}^{\prime})}} = {1 - {{IoU}{({\mathbf{y}},{\mathbf{y}}^{\prime})}}}$.

### Score Function

The formulation we use is based on the popular R-CNN approach. We consider two cases: linear score and non-linear score $\phi$, both of which are based on the following definition of the feature map $\Phi{({\mathbf{x}},{\mathbf{y}})}$.

Consider a patch ${{\mathbf{x}}|}_{\mathbf{y}}$ of image $\mathbf{x}$ cropped to box $\mathbf{y}$, and rescale it to $64 \times 64$. Call this $\Pi{({{\mathbf{x}}|}_{\mathbf{y}})}$.

Consider a convolutional neural network known as AlexNet pre-trained on ImageNet and pass $\Pi{({{\mathbf{x}}|}_{\mathbf{y}})}$ through it. Take the output of conv4, the penultimate convolutional layer as the feature map $\Phi{({\mathbf{x}},{\mathbf{y}})}$. It is of size $3 \times 3 \times 256$.

In the case of linear score functions, we take ${\phi{({\mathbf{x}},{\mathbf{y}};{\mathbf{w}})}} = {\langle{\mathbf{w}},{\Phi{({\mathbf{x}},{\mathbf{y}})}}\rangle}$. In the case of non-linear score functions, we define the score $\phi$ as the the result of a convolution composed with a non-linearity and followed by a linear map. Concretely, for ${\mathbf{θ}} \in {\mathbb{R}}^{H \times W \times C_{1}}$ and ${\mathbf{w}} \in {\mathbb{R}}^{C_{1} \times C_{2}}$ let the map ${\mathbf{θ}}\mapsto{{\mathbf{θ}} \star {\mathbf{w}}} \in {\mathbb{R}}^{H \times W \times C_{2}}$ denote a two dimensional convolution with stride $1$ and kernel size $1$, and $\sigma:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ denote the exponential linear unit, defined respectively as

where ${\lbrack{\mathbf{θ}}\rbrack}_{ij} \in {\mathbb{R}}^{C_{1}}$ is such that its $l$th entry is ${\mathbf{θ}}_{ijl}$ and likewise for ${\lbrack{{\mathbf{θ}} \star {\mathbf{w}}}\rbrack}_{ij}$. We overload notation to let $\sigma:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ denote the exponential linear unit applied element-wise. Notice that $\sigma$ is smooth. The non-linear score function $\phi$ is now defined, with ${{\mathbf{w}}_{1} \in {\mathbb{R}}^{256 \times 16}},{{\mathbf{w}}_{2} \in {\mathbb{R}}^{16 \times 3 \times 3}}$ and ${\mathbf{w}} = {({\mathbf{w}}_{1},{\mathbf{w}}_{2})}$, as,

### Inference

For a given input image $\mathbf{x}$, we follow the R-CNN approach and use selective search to prune the search space. In particular, for an image $\mathbf{x}$, we use the selective search implementation provided by OpenCV and take the top 1000 candidates returned to be the set $\hat{\mathcal{Y}}{({\mathbf{x}})}$, which we use as a proxy for $\mathcal{Y}{({\mathbf{x}})}$. The max oracle and the top-$K$ oracle are then implemented as exhaustive searches over this reduced set $\hat{\mathcal{Y}}{({\mathbf{x}})}$.

### Dataset

We use the PASCAL VOC 2007 dataset, which contains $\sim {5K}$ annotated consumer (real world) images shared on the photo-sharing site Flickr from 20 different object categories. For each class, we consider all images with only a single occurrence of the object, and train an independent model for each class.

### Evaluation Metric

We keep track of two metrics. The first is the localization accuracy, also known as CorLoc (for correct localization), following Deselaers et al.. A bounding box with IoU $> 0.5$ with the ground truth is considered correct and the localization accuracy is the fraction of images labeled correctly. The second metric is average precision (AP), which requires a confidence score for each prediction. We use $\phi{({\mathbf{x}},{\mathbf{y}}^{\prime};{\mathbf{w}})}$ as the confidence score of ${\mathbf{y}}^{\prime}$. As previously, we also plot the objective function value measured on the training examples.

### Other Implementation Details

For a given input-output pair $({\mathbf{x}},{\mathbf{y}})$ in the dataset, we instead use $({\mathbf{x}},\hat{\mathbf{y}})$ as a training example, where $\hat{\mathbf{y}} = {{\underset{{\mathbf{y}}^{\prime} \in {\hat{\mathcal{Y}}{({\mathbf{x}})}}}{\arg\max}{IoU}}{({\mathbf{y}},{\mathbf{y}}^{\prime})}}$ is the element of $\hat{\mathcal{Y}}{({\mathbf{x}})}$ which overlaps the most with the true output $\mathbf{y}$.

### Methods Compared

The experiments compare various convex stochastic and incremental optimization methods for structured prediction.

SGD: Stochastic subgradient method with a learning rate $\gamma_{t} = {\gamma_{0}/{({1 + {\lfloor{t/t_{0}}\rfloor}})}}$, where $\eta_{0},t_{0}$ are tuning parameters. Note that this scheme of learning rates does not have a theoretical analysis. However, the averaged iterate ${\overline{\mathbf{w}}}_{t} = {{2/{({t^{2} + t})}}{\sum_{\tau = 1}^{t}{\tau{\mathbf{w}}_{\tau}}}}$ obtained from the related scheme $\gamma_{t} = {1/{({\lambdat})}}$ was shown to have a convergence rate of $\mathcal{O}{({({\lambda\epsilon})}^{- 1})}$. It works on the non-smooth formulation directly.

BCFW: The block coordinate Frank-Wolfe algorithm of Lacoste-Julien et al.. We use the version that was found to work best in practice, namely, one that uses the weighted averaged iterate ${\overline{\mathbf{w}}}_{t} = {{2/{({t^{2} + t})}}{\sum_{\tau = 1}^{t}{\tau{\mathbf{w}}_{\tau}}}}$ (called bcfw-wavg by the authors) with optimal tuning of learning rates. This algorithm also works on the non-smooth formulation and does not require any tuning.

SVRG: The SVRG algorithm proposed by Johnson and Zhang, with each epoch making one pass through the dataset and using the averaged iterate to compute the full gradient and restart the next epoch. This algorithm requires smoothing.

Casimir-SVRG-const: Algo. 4 with SVRG as the inner optimization algorithm. The parameters $\mu_{k}$ and $\kappa_{k}$ as chosen in Prop. 29, where $\mu$ and $\kappa$ are hyperparameters. This algorithm requires smoothing.

Casimir-SVRG-adapt: Algo. 4 with SVRG as the inner optimization algorithm. The parameters $\mu_{k}$ and $\kappa_{k}$ as chosen in Prop. 30, where $\mu$ and $\kappa$ are hyperparameters. This algorithm requires smoothing.

On the other hand, for non-convex structured prediction, we only have two methods:

SGD: The stochastic subgradient method, which we call as SGD. This algorithm works directly on the non-smooth formulation. We try learning rates $\gamma_{t} = \gamma_{0}$, $\gamma_{t} = {\gamma_{0}/\sqrt{t}}$ and $\gamma_{t} = {\gamma_{0}/t}$, where $\gamma_{0}$ is found by grid search in each of these cases. We use the names SGD-const, SGD-$t^{- {1/2}}$ and SGD-$t^{- 1}$ respectively for these variants. We note that SGD-$t^{- 1}$ does not have any theoretical analysis in the non-convex case.

PL-Casimir-SVRG: Algo. 5 with Casimir-SVRG-const as the inner solver using the settings of Prop. 37. This algorithm requires smoothing the inner subproblem.

### Hyperparameters and Variants

### Smoothing

In light of the discussion of Sec. 4, we use the $\ell_{2}^{2}$ smoother ${\omega{({\mathbf{u}})}} = {{\|{\mathbf{u}}\|}_{2}^{2}/2}$ and use the top-$K$ strategy for efficient computation. We then have $D_{\omega} = {1/2}$.

### Regularization

The regularization coefficient $\lambda$ is chosen as $c/n$, where $c$ is varied in $\{ 0.01,0.1,1,10\}$.

### Choice of $K$

The experiments use $K = 5$ for named entity recognition where the performance of the top-$K$ oracle is $K$ times slower, and $K = 10$ for visual object localization, where the running time of the top-$K$ oracle is independent of $K$. We also present results for other values of $K$ in Fig. 5(d) and find that the performance of the tested algorithms is robust to the value of $K$.

### Tuning Criteria

Some algorithms require tuning one or more hyperparameters such as the learning rate. We use grid search to find the best choice of the hyperparameters using the following criteria: For the named entity recognition experiments, the train function value and the validation $F_{1}$ metric were only weakly correlated. For instance, the 3 best learning rates in the grid in terms of $F_{1}$ score, the best $F_{1}$ score attained the worst train function value and vice versa. Therefore, we choose the value of the tuning parameter that attained the best objective function value within 1% of the best validation $F_{1}$ score in order to measure the optimization performance while still remaining relevant to the named entity recognition task. For the visual object localization task, a wide range of hyperparameter values achieved nearly equal performance in terms of the best CorLoc over the given time horizon, so we choose the value of the hyperparameter that achieves the best objective function value within a given iteration budget.

### Hyperparameters for Convex Optimization

This corresponds to the setting of Section 5.

### Learning Rate

The algorithms SVRG and Casimir-SVRG-adapt require tuning of a learning rate, while SGD requires $\eta_{0},t_{0}$ and Casimir-SVRG-const requires tuning of the Lipschitz constant $L$ of $\nabla F_{\mu\omega}$, which determines the learning rate $\gamma = {1/{({L + \lambda + \kappa})}}$. Therefore, tuning the Lipschitz parameter is similar to tuning the learning rate. For both the learning rate and Lipschitz parameter, we use grid search on a logarithmic grid, with consecutive entries chosen a factor of two apart.

### Choice of $\kappa$

For Casimir-SVRG-const, with the Lipschitz constant in hand, the parameter $\kappa$ is chosen to minimize the overall complexity as in Prop. 29. For Casimir-SVRG-adapt, we use $\kappa = \lambda$.

### Stopping Criteria

Following the discussion of Sec. 5, we use an iteration budget of $T_{budget} = n$.

### Warm Start

The warm start criterion determines the starting iterate of an epoch of the inner optimization algorithm. Recall that we solve the following subproblem using SVRG for the $k$th iterate (cf. ):

Here, we consider the following warm start strategy to choose the initial iterate ${\hat{\mathbf{w}}}_{0}$ for this subproblem:

Prox-center: ${\hat{\mathbf{w}}}_{0} = {\mathbf{z}}_{k - 1}$.

In addition, we also try out the following warm start strategies of Lin et al.:

Extrapolation: ${\hat{\mathbf{w}}}_{0} = {{\mathbf{w}}_{k - 1} + {c{({{\mathbf{z}}_{k - 1} - {\mathbf{z}}_{k - 2}})}}}$ where $c = \frac{\kappa}{\kappa + \lambda}$.

Prev-iterate: ${\hat{\mathbf{w}}}_{0} = {\mathbf{w}}_{k - 1}$.

We use the Prox-center strategy unless mentioned otherwise.

### Level of Smoothing and Decay Strategy

For SVRG and Casimir-SVRG-const with constant smoothing, we try various values of the smoothing parameter in a logarithmic grid. On the other hand, Casimir-SVRG-adapt is more robust to the choice of the smoothing parameter (Fig. 5(a)). We use the defaults of $\mu = 2$ for named entity recognition and $\mu = 10$ for visual object localization.

### Hyperparameters for Non-Convex Optimization

This corresponds to the setting of Section 6.

### Prox-Linear Learning Rate $\eta$

We perform grid search in powers of 10 to find the best prox-linear learning rate $\eta$. We find that the performance of the algorithm is robust to the choice of $\eta$ (Fig. 7(a)).

### Stopping Criteria

We used a fixed budget of 5 iterations of Casimir-SVRG-const. In Fig. 7(b), we experiment with different iteration budgets.

### Level of Smoothing and Decay Strategy

In order to solve the $k$th prox-linear subproblem with Casimir-SVRG-const, we must specify the level of smoothing $\mu_{k}$. We experiment with two schemes, (a) constant smoothing $\mu_{k} = \mu$, and (b) adaptive smoothing $\mu_{k} = {\mu/k}$. Here, $\mu$ is a tuning parameters, and the adaptive smoothing scheme is designed based on Prop. 37 and Remark 38. We use the adaptive smoothing strategy as a default, but compare the two in Fig. 6.

### Gradient Lipschitz Parameter for Inner Optimization

The inner optimization algorithm Casimir-SVRG-const still requires a hyperparameter $L_{k}$ to serve as an estimate to the Lipschitz parameter of the gradient ${\nabla F_{\eta,{\mu_{k}\omega}}}{( \cdot;{\mathbf{w}}_{k})}$. We set this parameter as follows, based on the smoothing strategy: (a) $L_{k} = L_{0}$ with the constant smoothing strategy, and (b) $L_{k} = {kL_{0}}$ with the adaptive smoothing strategy (cf. Prop. 2). We note that the latter choice has the effect of decaying the learning rate as $1/k$ in the $k$th outer iteration.

Figure 2: Comparison of convex optimization algorithms for the task of Named Entity Recognition on CoNLL 2003.

Figure 3: Comparison of convex optimization algorithms for the task of visual object localization on PASCAL VOC 2007 for λ = 10/n. Plots for all other classes are in Appendix E.

Figure 4: Comparison of non-convex optimization algorithms for the task of visual object localization on PASCAL VOC 2007 for λ = 1/n. Plots for all other classes are in Appendix E.

### Experimental study of different methods

### Convex Optimization

For the named entity recognition task, Fig. 2 plots the performance of various methods on CoNLL 2003. On the other hand, Fig. 3 presents plots for various classes of PASCAL VOC 2007 for visual object localization.

The plots reveal that smoothing-based methods converge faster in terms of training error while achieving a competitive performance in terms of the performance metric on a held-out set. Furthermore, BCFW and SGD make twice as many actual passes as SVRG based algorithms.

### Non-Convex Optimization

Fig. 4 plots the performance of various algorithms on the task of visual object localization on PASCAL VOC.

### Experimental Study of Effect of Hyperparameters: Convex Optimization

We now study the effects of various hyperparameter choices.

### Effect of Smoothing

Fig. 5(a) plots the effect of the level of smoothing for Casimir-SVRG-const and Casimir-SVRG-adapt. The plots reveal that, in general, small values of the smoothing parameter lead to better optimization performance for Casimir-SVRG-const. Casimir-SVRG-adapt is robust to the choice of $\mu$. Fig. 5(b) shows how the smooth optimization algorithms work when used heuristically on the non-smooth problem.

(a) Effect of level of smoothing.

(b) Effect of smoothing: use of smooth optimization with smoothing (labeled “smooth”) versus the heuristic use of these algorithms without smoothing (labeled “non-smooth”) for λ = 0.01/n.

(c) Effect of warm start strategies for λ = 0.01/n (first row) and λ = 1/n (second row).

(d) Effect of K in the top-K oracle (λ = 0.01/n).

Figure 5: Effect of hyperparameters for the task of Named Entity Recognition on CoNLL 2003. C-SVRG stands for Casimir-SVRG in these plots.

### Effect of Warm Start Strategies

Fig. 5(c) plots different warm start strategies for Casimir-SVRG-const and Casimir-SVRG-adapt. We find that Casimir-SVRG-adapt is robust to the choice of the warm start strategy while Casimir-SVRG-const is not. For the latter, we observe that Extrapolation is less stable (i.e., tends to diverge more) than Prox-center, which is in turn less stable than Prev-iterate, which always works (cf. Fig. 5(c)). However, when they do work, Extrapolation and Prox-center provide greater acceleration than Prev-iterate. We use Prox-center as the default choice to trade-off between acceleration and applicability.

### Effect of $K$

Fig. 5(d) illustrates the robustness of the method to choice of $K$: we observe that the results are all within one standard deviation of each other.

### Experimental Study of Effect of Hyperparameters: Non-Convex Optimization

We now study the effect of various hyperparameters for the non-convex optimization algorithms. All of these comparisons have been made for $\lambda = {1/n}$.

### Effect of Smoothing

Fig. 6(a) compares the adaptive and constant smoothing strategies. Fig. 6(b) and Fig. 6(c) compare the effect of the level of smoothing on the the both of these. As previously, the adaptive smoothing strategy is more robust to the choice of the smoothing parameter.

(a) Comparison of adaptive and constant smoothing strategies.

(b) Effect of μ of the adaptive smoothing strategy.

(c) Effect of μ of the constant smoothing strategy.

Figure 6: Effect of smoothing on PL-Casimir-SVRG for the task of visual object localization on PASCAL VOC 2007.

(a) Effect of the hyperparameter η.

(b) Effect of the iteration budget of the inner solver.

(c) Effect of the warm start strategy of the inner Casimir-SVRG-const algorithm.

Figure 7: Effect of hyperparameters on PL-Casimir-SVRG for the task of visual object localization on PASCAL VOC 2007.

### Effect of Prox-Linear Learning Rate $\eta$

Fig. 7(a) shows the robustness of the proposed method to the choice of $\eta$.

### Effect of Iteration Budget

Fig. 7(b) also shows the robustness of the proposed method to the choice of iteration budget of the inner solver, Casimir-SVRG-const.

### Effect of Warm Start of the Inner Solver

Fig. 7(c) studies the effect of the warm start strategy used within the inner solver Casimir-SVRG-const in each inner prox-linear iteration. The results are similar to those obtained in the convex case, with Prox-center choice being the best compromise between acceleration and compatibility.

## Future Directions

We introduced a general notion of smooth inference oracles in the context of black-box first-order optimization. This allows us to set the scene to extend the scope of fast incremental optimization algorithms to structured prediction problems owing to a careful blend of a smoothing strategy and an acceleration scheme. We illustrated the potential of our framework by proposing a new incremental optimization algorithm to train structural support vector machines both enjoying worst-case complexity bounds and demonstrating competitive performance on two real-world problems. This work paves also the way to faster incremental primal optimization algorithms for deep structured prediction models.

There are several potential venues for future work. When there is no discrete structure that admits efficient inference algorithms, it could be beneficial to not treat inference as a black-box numerical procedure. Instance-level improved algorithms along the lines of Hazan et al. could also be interesting to explore.
