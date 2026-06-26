<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimizing Neural Networks with Kronecker-factored Approximate Curvature

Topics include Low-rank models, Stochastic optimization, Gradient descent, Stochastic gradients, Natural gradients, Neural networks, Optimization, K-FAC, Stochastic gradient descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose an efficient method for approximating natural gradient descent in neural networks which we call Kronecker-Factored Approximate Curvature (K-FAC). K-FAC is based on an efficiently invertible approximation of a neural network's Fisher information matrix which is neither diagonal nor low-rank, and in some cases is completely non-sparse. It is derived by approximating various large blocks of the Fisher (corresponding to entire layers) as being the Kronecker product of two much smaller matrices. While only several times more expensive to compute than the plain stochastic gradient, the updates produced by K-FAC make much more progress optimizing the objective, which results in an algorithm that can be much faster than stochastic gradient descent with momentum in practice. And unlike some previously proposed approximate natural-gradient/Newton methods which use high-quality non-diagonal curvature matrices (such as Hessian-free optimization), K-FAC works very well in highly stochastic optimization regimes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This is because the cost of storing and inverting K-FAC's approximation to the curvature matrix does not depend on the amount of data used to estimate it, which is a feature typically associated only with diagonal or low-rank approximations to the curvature matrix.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of training neural networks is one of the most important and highly investigated ones in machine learning. Despite work on layer-wise pretraining schemes, and various sophisticated optimization methods which try to approximate Newton-Raphson updates or natural gradient updates, stochastic gradient descent (SGD), possibly augmented with momentum, remains the method of choice for large-scale neural network training.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

From the work on Hessian-free optimization (HF) and related methods we know that updates computed using local curvature information can make much more progress per iteration than the scaled gradient. The reason that HF sees fewer practical applications than SGD are twofold. Firstly, its updates are much more expensive to compute, as they involve running linear conjugate gradient (CG) for potentially hundreds of iterations, each of which requires a matrix-vector product with the curvature matrix (which are as expensive to compute as the stochastic gradient on the current mini-batch). Secondly, HF's estimate of the curvature matrix must remain fixed while CG iterates, and thus the method is able to go through much less data than SGD can in a comparable amount of time, making it less well suited to stochastic optimizations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As discussed in Martens and Sutskever and Sutskever et al., CG has the potential to be much faster at local optimization than gradient descent, when applied to quadratic objective functions. Thus, insofar as the objective can be locally approximated by a quadratic, each step of CG could potentially be doing a lot more work than each iteration of SGD, which would result in HF being much faster overall than SGD. However, there are examples of quadratic functions, characterized by curvature matrices with highly spread-out eigenvalue distributions, where CG will have no distinct advantage over well-tuned gradient descent with momentum. Thus, insofar as the quadratic functions being optimized by CG within HF are of this character, HF shouldn't in principle be faster than well-tuned SGD with momentum. The extent to which neural network objective functions give rise to such quadratics is unclear, although Sutskever et al. provides some preliminary evidence that they do.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

CG falls victim to this worst-case analysis because it is a first-order method. This motivates us to consider methods which don't rely on first-order methods like CG as their primary engines of optimization. One such class of methods which have been widely studied are those which work by directly inverting a diagonal, block-diagonal, or low-rank approximation to the curvature matrix. In fact, a diagonal approximation of the Fisher information matrix is used within HF as a preconditioner for CG. However, these methods provide only a limited performance improvement in practice, especially compared to SGD with momentum, and many practitioners tend to forgo them in favor of SGD or SGD with momentum.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We know that the curvature associated with neural network objective functions is highly non-diagonal, and that updates which properly respect and account for this non-diagonal curvature, such as those generated by HF, can make much more progress minimizing the objective than the plain gradient or updates computed from diagonal approximations of the curvature (usually $\sim 10^{2}$ HF updates are required to adequately minimize most objectives, compared to the $\sim {10^{4} - 10^{5}}$ required by methods that use diagonal approximations). Thus, if we had an efficient and direct way to compute the inverse of a high-quality non-diagonal approximation to the curvature matrix (i.e. without relying on first-order methods like CG) this could potentially yield an optimization method whose updates would be large and powerful like HF's, while being (almost) as cheap to compute as the stochastic gradient.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we develop such a method, which we call Kronecker-factored Approximate Curvature (K-FAC). We show that our method can be much faster in practice than even highly tuned implementations of SGD with momentum on certain standard neural network optimization benchmarks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main ingredient in K-FAC is a sophisticated approximation to the Fisher information matrix, which despite being neither diagonal nor low-rank, nor even block-diagonal with small blocks, can be inverted very efficiently, and can be estimated in an online fashion using arbitrarily large subsets of the training data (without increasing the cost of inversion).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

This approximation is built in two stages. In the first, the rows and columns of the Fisher are divided into groups, each of which corresponds to *all the weights in a given layer*, and this gives rise to a block-partitioning of the matrix (where the blocks are *much* larger than those used by Le Roux et al. or Ollivier ). These blocks are then approximated as Kronecker products between much smaller matrices, which we show is equivalent to making certain approximating assumptions regarding the statistics of the network's gradients.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the second stage, this matrix is further approximated as having an *inverse* which is either block-diagonal or block-tridiagonal. We justify this approximation through a careful examination of the relationships between inverse covariances, tree-structured graphical models, and linear regression. Notably, this justification doesn't apply to the Fisher itself, and our experiments confirm that while the inverse Fisher does indeed possess this structure (approximately), the Fisher itself does not.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

In this section we will define the basic notation for feed-forward neural networks which we will use throughout this paper. Note that this presentation closely follows the one from Martens.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

A neural network transforms its input $a_{0} = x$ to an output ${f{(x,\theta)}} = a_{\ell}$ through a series of $\ell$ layers, each of which consists of a bank of units/neurons. The units each receive as input a weighted sum of the outputs of units from the previous layer and compute their output via a nonlinear "activation" function. We denote by $s_{i}$ the vector of these weighted sums for the $i$-th layer, and by $a_{i}$ the vector of unit outputs (aka "activities").

<!-- chunk {"id": "body-0015", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

The precise computation performed at each layer $i \in {\{ 1,\ldots,\ell\}}$ is given as follows: where $\phi_{i}$ is an element-wise nonlinear function, $W_{i}$ is a weight matrix, and ${\overline{a}}_{i}$ is defined as the vector formed by appending to $a_{i}$ an additional homogeneous coordinate with value 1. Note that we do not include explicit bias parameters here as these are captured implicitly through our use of homogeneous coordinates. In particular, the last column of each weight matrix $W_{i}$ corresponds to what is usually thought of as the "bias vector". Figure 1 illustrates our definition for $\ell = 2$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

We will define $\theta = {\lbrack{vec}{(W_{1})}^{\top}{vec}{(W_{2})}^{\top}\ldots{vec}{(W_{\ell})}^{\top}\rbrack}^{\top}$, which is the vector consisting of all of the network's parameters concatenated together, where $vec$ is the operator which vectorizes matrices by stacking their columns together.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

We let $L{(y,z)}$ denote the loss function which measures the disagreement between a prediction $z$ made by the network, and a target $y$. The training objective function $h{(\theta)}$ is the average (or expectation) of losses $L{(y,{f{(x,\theta)}})}$ with respect to a training distribution ${\hat{Q}}_{x,y}$ over input-target pairs $(x,y)$. $h{(\theta)}$ is a proxy for the objective which we actually care about but don't have access to, which is the expectation of the loss taken with respect to the true data distribution $Q_{x,y}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

We will assume that the loss is given by the negative log probability associated with a simple predictive distribution $R_{y|z}$ for $y$ parameterized by $z$, i.e. that we have where $r$ is $R_{y|z}$'s density function. This is the case for both the standard least-squares and cross-entropy objective functions, where the predictive distributions are multivariate normal and multinomial, respectively.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

We will let ${P_{y|x}{(\theta)}} = R_{y|{f{(x,\theta)}}}$ denote the conditional distribution defined by the neural network, as parameterized by $\theta$, and ${p{(\left. y \middle| {x,\theta} \right.)}} = {r{(\left. y \middle| {f{(x,\theta)}} \right.)}}$ its density function. Note that minimizing the objective function $h{(\theta)}$ can be seen as maximum likelihood learning of the model $P_{y|x}{(\theta)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Neural Networks", "weight": 1.0} -->

For convenience we will define the following additional notation: Algorithm 1 shows how to compute the gradient $\mathcal{D}\theta$ of the loss function of a neural network using standard backpropagation. for all i from 1 to ℓ do /* Loss derivative computation */${\mathcal{D}a_{\ell}}\leftarrow\left. \frac{\partial{L{(y,z)}}}{\partial z} \right|_{z = a_{\ell}}$ for all i from ℓ downto 1 do ${\mathcal{D}W_{i}}\leftarrow{g_{i}{\overline{a}}_{i - 1}^{\top}}$ output: 𝒟θ = [vec(𝒟W1)⊤vec(𝒟W2)⊤…vec(𝒟Wℓ)⊤]⊤ Algorithm 1 An algorithm for computing the gradient of the loss L (y, f (x, θ)) for a given (x, y). Note that we are assuming here for simplicity that the ϕi are defined as coordinate-wise functions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Natural Gradient", "weight": 1.0} -->

Because our network defines a conditional model $P_{y|x}{(\theta)}$, it has an associated Fisher information matrix (which we will simply call "the Fisher") which is given by Here, the expectation is taken with respect to the data distribution $Q_{x}$ over inputs $x$, and the model's predictive distribution $P_{y|x}{(\theta)}$ over $y$. Since we usually don't have access to $Q_{x}$, and the above expectation would likely be intractable even if we did, we will instead compute $F$ using the training distribution ${\hat{Q}}_{x}$ over inputs $x$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Natural Gradient", "weight": 1.0} -->

The well-known natural gradient is defined as $F^{- 1}{\nabla h}{(\theta)}$. Motivated from the perspective of information geometry, the natural gradient defines the direction in parameter space which gives the largest change in the objective per unit of change in the model, as measured by the KL-divergence. This is to be contrasted with the standard gradient, which can be defined as the direction in parameter space which gives the largest change in the objective per unit of change in the parameters, as measured by the standard Euclidean metric.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Natural Gradient", "weight": 1.0} -->

The natural gradient also has links to several classical ideas from optimization. It can be shown that the Fisher is equivalent to the Generalized Gauss-Newton matrix (GGN) in certain important cases, which is a well-known positive semi-definite approximation to the Hessian of the objective function. In particular, showed that when the GGN is defined so that the network is linearized up to the loss function, and the loss function corresponds to the negative log probability of observations under an exponential family model $R_{y|z}$ with $z$ representing the *natural parameters*, then the Fisher corresponds exactly to the GGN.^11^1Note that the condition that $z$ represents the natural parameters might require one to formally include the nonlinear transformation usually performed by the final nonlinearity $\phi_{\ell}$ of the network (such as the logistic-sigmoid transform before a cross-entropy error) as part of the loss function $L$ instead. Equivalently, one could linearize the network only up to the input $s_{\ell}$ to $\phi_{\ell}$ when computing the GGN (see Martens and Sutskever ).

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Natural Gradient", "weight": 1.0} -->

The GGN has served as the curvature matrix of choice in HF and related methods, and so in light of its equivalence to the Fisher, these 2nd-order methods can be seen as approximate natural gradient methods. And perhaps more importantly from a practical perspective, natural gradient-based optimization methods can conversely be viewed as 2nd-order optimization methods, which as pointed out by Martens ), brings to bare the vast wisdom that has accumulated about how to make such methods work well in both theory and practice. In Section 6 we productively make use of these connections in order to design a robust and highly effective optimization method using our approximation to the natural gradient/Fisher (which is developed in Sections 3 and 4).

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Natural Gradient", "weight": 1.0} -->

For some good recent discussion and analysis of the natural gradient, see Arnold et al.; Martens; Pascanu and Bengio.

<!-- chunk {"id": "body-0026", "role": "body", "section": "A block-wise Kronecker-factored Fisher approximation", "weight": 1.0} -->

The main computational challenge associated with using the natural gradient is computing $F^{- 1}$ (or its product with $\nabla h$). For large networks, with potentially millions of parameters, computing this inverse naively is computationally impractical. In this section we develop an initial approximation of $F$ which will be a key ingredient in deriving our efficiently computable approximation to $F^{- 1}$ and the natural gradient.

<!-- chunk {"id": "body-0027", "role": "body", "section": "A block-wise Kronecker-factored Fisher approximation", "weight": 1.0} -->

Our initial approximation $\overset{\sim}{F}$ to $F$ will be defined by the following block-wise approximation: where ${\overline{A}}_{i,j} = {E\left\lbrack {{\overline{a}}_{i}{\overline{a}}_{j}^{\top}} \right\rbrack}$ and $G_{i,j} = {E\left\lbrack {g_{i}g_{j}^{\top}} \right\rbrack}$. which has the form of what is known as a Khatri-Rao product in multivariate statistics.

<!-- chunk {"id": "body-0028", "role": "body", "section": "A block-wise Kronecker-factored Fisher approximation", "weight": 1.0} -->

The expectation of a Kronecker product is, in general, not equal to the Kronecker product of expectations, and so this is indeed a major approximation to make, and one which likely won't become exact under any realistic set of assumptions, or as a limiting case in some kind of asymptotic analysis. Nevertheless, it seems to be fairly accurate in practice, and is able to successfully capture the "coarse structure" of the Fisher, as demonstrated in Figure 2 for an example network.

<!-- chunk {"id": "body-0029", "role": "body", "section": "A block-wise Kronecker-factored Fisher approximation", "weight": 1.0} -->

As we will see in later sections, this approximation leads to significant computational savings in terms of storage and inversion, which we will be able to leverage in order to design an efficient algorithm for computing an approximation to the natural gradient.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Interpretations of this approximation", "weight": 1.0} -->

The approximation given by eqn. 1 is equivalent to making the following approximation for each pair of weights: And thus one way to interpret the approximation in eqn. 1 is that we are assuming statistical independence between products ${\overline{a}}^{}{\overline{a}}^{}$ of unit activities and products $g^{}g^{}$ of unit input derivatives.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Interpretations of this approximation", "weight": 1.0} -->

Another more detailed interpretation of the approximation emerges by considering the following expression for the approximation error ${E\left\lbrack {{\overline{a}}^{}{\overline{a}}^{}g^{}g^{}} \right\rbrack} - {{E\left\lbrack {{\overline{a}}^{}{\overline{a}}^{}} \right\rbrack}{E\left\lbrack {g^{}g^{}} \right\rbrack}}$ (which is derived in the appendix): Here $\kappa{(\cdot)}$ denotes the cumulant of its arguments. Cumulants are a natural generalization of the concept of mean and variance to higher orders, and indeed 1st-order cumulants are means and 2nd-order cumulants are covariances. Intuitively, cumulants of order $k$ measure the degree to which the interaction between variables is intrinsically of order $k$, as opposed to arising from many lower-order interactions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Interpretations of this approximation", "weight": 1.0} -->

A basic upper bound for the approximation error is which will be small if all of the higher-order cumulants are small (i.e. those of order 3 or higher). Note that in principle this upper bound may be loose due to possible cancellations between the terms in eqn. 3.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Interpretations of this approximation", "weight": 1.0} -->

Because higher-order cumulants are zero for variables jointly distributed according to a multivariate Gaussian, it follows that this upper bound on the approximation error will be small insofar as the joint distribution over ${\overline{a}}^{}$, ${\overline{a}}^{}$, $g^{}$, and $g^{}$ is well approximated by a multivariate Gaussian. And while we are not aware of an argument for why this should be the case in practice, it does seem to be the case that for the example network from Figure 2, the size of the error is well predicted by the size of the higher-order cumulants. In particular, the total approximation error, summed over all pairs of weights in the middle 4 layers, is $2894.4$, and is of roughly the same size as the corresponding upper bound ($4134.6$), whose size is tied to that of the higher order cumulants (due to the impossibility of cancellations in eqn. 4).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Additional approximations to $\\overset{\\sim}{F}$ and inverse computations", "weight": 1.0} -->

To the best of our knowledge there is no efficient general method for inverting a Khatri-Rao product like $\overset{\sim}{F}$. Thus, we must make further approximations if we hope to obtain an efficiently computable approximation of the inverse Fisher.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Additional approximations to $\\overset{\\sim}{F}$ and inverse computations", "weight": 1.0} -->

In the following subsections we argue that the inverse of $\overset{\sim}{F}$ can be reasonably approximated as having one of two special structures, either of which make it efficiently computable. The second of these will be slightly less restrictive than the first (and hence a better approximation) at the cost of some additional complexity. We will then show how matrix-vector products with these approximate inverses can be efficiently computed, which will thus give an efficient algorithm for computing an approximation to the natural gradient.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Suppose we are given a multivariate distribution whose associated covariance matrix is $\Sigma$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Define the matrix $B$ so that for $i \neq j$, ${\lbrack B\rbrack}_{i,j}$ is the coefficient on the $j$-th variable in the optimal linear predictor of the $i$-th variable from all the other variables, and for $i = j$, ${\lbrack B\rbrack}_{i,j} = 0$. Then define the matrix $D$ to be the diagonal matrix where ${\lbrack D\rbrack}_{i,i}$ is the variance of the error associated with such a predictor of the $i$-th variable.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Pourahmadi showed that $B$ and $D$ can be obtained from the inverse covariance $\Sigma^{- 1}$ by the formulas from which it follows that the inverse covariance matrix can be expressed as Intuitively, this result says that each row of the inverse covariance $\Sigma^{- 1}$ is given by the coefficients of the optimal linear predictor of the $i$-th variable from the others, up to a scaling factor. So if the $j$-th variable is much less "useful" than the other variables for predicting the $i$-th variable, we can expect that the $(i,j)$-th entry of the inverse covariance will be relatively small.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Note that "usefulness" is a subtle property as we have informally defined it. In particular, it is not equivalent to the degree of correlation between the $j$-th and $i$-th variables, or any such simple measure. As a simple example, consider the case where the $j$-th variable is equal to the $k$-th variable plus independent Gaussian noise. Since any linear predictor can achieve a lower variance simply by shifting weight from the $j$-th variable to the $k$-th variable, we have that the $j$-th variable is not useful (and its coefficient will thus be zero) in the task of predicting the $i$-th variable for any setting of $i$ other than $i = j$ or $i = k$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Noting that the Fisher $F$ is a covariance matrix over $\mathcal{D}\theta$ w.r.t. the model's distribution (because ${E{\lbrack{\mathcal{D}\theta}\rbrack}} = 0$ by Lemma 4), we can thus apply the above analysis to the distribution over $\mathcal{D}\theta$ to gain insight into the approximate structure of $F^{- 1}$, and by extension its approximation ${\overset{\sim}{F}}^{- 1}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Consider the derivative $\mathcal{D}W_{i}$ of the loss with respect to the weights $W_{i}$ of layer $i$. Intuitively, if we are trying to predict one of the entries of $\mathcal{D}W_{i}$ from the other entries of $\mathcal{D}\theta$, those entries also in $\mathcal{D}W_{i}$ will likely be the most useful in this regard. Thus, it stands to reason that the largest entries of ${\overset{\sim}{F}}^{- 1}$ will be those on the diagonal blocks, so that ${\overset{\sim}{F}}^{- 1}$ will be well approximated as block-diagonal, with each block corresponding to a different $\mathcal{D}W_{i}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Beyond the other entries of $\mathcal{D}W_{i}$, it is the entries of $\mathcal{D}W_{i + 1}$ and $\mathcal{D}W_{i - 1}$ (i.e. those associated with adjacent layers) that will arguably be the most useful in predicting a given entry of $\mathcal{D}W_{i}$. This is because the true process for computing the loss gradient only uses information from the layer below (during the forward pass) and from the layer above (during the backwards pass). Thus, approximating ${\overset{\sim}{F}}^{- 1}$ as block-tridiagonal seems like a reasonable and milder alternative than taking it to be block-diagonal.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Indeed, this approximation would be exact if the distribution over $\mathcal{D}\theta$ were given by a directed graphical model which generated each of the $\mathcal{D}W_{i}$'s, one layer at a time, from either $\mathcal{D}W_{i + 1}$ or $\mathcal{D}W_{i - 1}$. Or equivalently, if $\mathcal{D}W_{i}$ were distributed according to an undirected Gaussian graphical model with binary potentials only between entries in the same or adjacent layers. Both of these models are depicted in Figure 4.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

Now while in reality the $\mathcal{D}W_{i}$'s are generated using information from adjacent layers according to a process that is *neither linear nor Gaussian*, it nonetheless stands to reason that their joint statistics might be reasonably approximated by such a model. In fact, the idea of approximating the distribution over loss gradients with a directed graphical model forms the basis of the recent FANG method of Grosse and Salakhutdinov.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Structured inverses and the connection to linear regression", "weight": 1.0} -->

In the following two subsections we show how both the block-diagonal and block-tridiagonal approximations to ${\overset{\sim}{F}}^{- 1}$ give rise to computationally efficient methods for computing matrix-vector products with it. And at the end of Section 4 we present two figures (Figures 5 and 6) which examine the quality of these approximations for an example network.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-diagonal", "weight": 1.0} -->

Approximating ${\overset{\sim}{F}}^{- 1}$ as block-diagonal is equivalent to approximating $\overset{\sim}{F}$ as block-diagonal. A natural choice for such an approximation $\breve{F}$ of $\overset{\sim}{F}$, is to take the block-diagonal of $\breve{F}$ to be that of $\overset{\sim}{F}$. This gives the matrix Using the identity ${({A \otimes B})}^{- 1} = {A^{- 1} \otimes B^{- 1}}$ we can easily compute the inverse of $\breve{F}$ as Thus, computing ${\breve{F}}^{- 1}$ amounts to computing the inverses of $2\ell$ smaller matrices.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-diagonal", "weight": 1.0} -->

Note that block-diagonal approximations to the Fisher information have been proposed before in TONGA, where each block corresponds to the weights associated with a particular unit. In our block-diagonal approximation, the blocks correspond to all the parameters in a given layer, and are thus *much* larger. In fact, they are so large that they would be impractical to invert as general matrices.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

Note that unlike in the above block-diagonal case, approximating ${\overset{\sim}{F}}^{- 1}$ as block-tridiagonal is *not* equivalent to approximating $\overset{\sim}{F}$ as block-tridiagonal. Thus we require a more sophisticated approach to deal with such an approximation. We develop such an approach in this subsection.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

To start, we will define $\hat{F}$ to be the matrix which agrees with $\overset{\sim}{F}$ on the tridiagonal blocks, and which satisfies the property that ${\hat{F}}^{- 1}$ is block-tridiagonal. Note that this definition implies certain values for the off-tridiagonal blocks of $\hat{F}$ which will differ from those of $\overset{\sim}{F}$ insofar as ${\overset{\sim}{F}}^{- 1}$ is not actually block-tridiagonal.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

To establish that such a matrix $\hat{F}$ is well defined and can be inverted efficiently, we first observe that assuming that ${\hat{F}}^{- 1}$ is block-tridiagonal is equivalent to assuming that it is the precision matrix of an undirected Gaussian graphical model (UGGM) over $\mathcal{D}\theta$ (as depicted in Figure 4), whose density function is proportional to $\exp{({- {\mathcal{D}\theta^{\top}{\hat{F}}^{- 1}\mathcal{D}\theta}})}$. As this graphical model has a tree structure, there is an equivalent *directed* graphical model with the same distribution and the same (undirected) graphical structure, where the directionality of the edges is given by a directed acyclic graph (DAG). Moreover, this equivalent directed model will also be linear/Gaussian, and hence a directed Gaussian Graphical model (DGGM).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

Next we will show how the parameters of such a DGGM corresponding to $\hat{F}$ can be efficiently recovered from the tridiagonal blocks of $\hat{F}$, so that $\hat{F}$ is uniquely determined by these blocks (and hence well-defined). We will assume here that the direction of the edges is from the higher layers to the lower ones. Note that a different choice for these directions would yield a superficially different algorithm for computing the inverse of $\hat{F}$ that would nonetheless yield the same output.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

For each $i$, we will denote the conditional covariance matrix of ${vec}{({\mathcal{D}W_{i}})}$ on ${vec}{({\mathcal{D}W_{i + 1}})}$ by $\Sigma_{i|{i + 1}}$ and the linear coefficients from ${vec}{({\mathcal{D}W_{i + 1}})}$ to ${vec}{({\mathcal{D}W_{i}})}$ by the matrix $\Psi_{i,{i + 1}}$, so that the conditional distributions defining the model are Figure 4: A diagram depicting the UGGM corresponding to F̂−1 and its equivalent DGGM. The UGGM’s edges are labeled with the corresponding weights of the model (these are distinct from the network’s weights).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

Here, (F̂−1)i, j denotes the (i, j)-th block of F̂−1. The DGGM’s edges are labeled with the matrices that specify the linear mapping from the source node to the conditional mean of the destination node (whose conditional covariance is given by its label).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

Since $\Sigma_{\ell}$ is just the covariance of ${vec}{({\mathcal{D}W_{\ell}})}$, it is given simply by ${\hat{F}}_{\ell,\ell} = {\overset{\sim}{F}}_{\ell,\ell}$. And for $i \leq {\ell - 1}$, we can see that $\Psi_{i,{i + 1}}$ is given by The conditional covariance $\Sigma_{i|{i + 1}}$ is thus given by Following the work of Grosse and Salakhutdinov, we use the block generalization of well-known "Cholesky" decomposition of the precision matrix of DGGMs, which gives Thus, matrix-vector multiplication with ${\hat{F}}^{- 1}$ amounts to performing matrix-vector multiplication by $\Xi$, followed by $\Lambda$, and then by $\Xi^{\top}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

As in the block-diagonal case considered in the previous subsection, matrix-vector products with $\Xi$ (and $\Xi^{\top}$) can be efficiently computed using the well-known identity ${({A \otimes B})}^{- 1} = {A^{- 1} \otimes B^{- 1}}$. In particular, $u = {\Xi^{\top}v}$ can be computed as and similarly $u = {\Xiv}$ can be computed as where the $U_{i}$'s and $V_{i}$'s are defined in terms of $u$ and $v$ as in the previous subsection.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Approximating ${\\overset{\\sim}{F}}^{- 1}$ as block-tridiagonal", "weight": 1.0} -->

Multiplying a vector $v$ by $\Lambda$ amounts to multiplying each ${vec}{(V_{i})}$ by the corresponding $\Sigma_{i|{i + 1}}^{- 1}$. This is slightly tricky because $\Sigma_{i|{i + 1}}$ is the difference of Kronecker products, so we cannot use the straightforward identity ${({A \otimes B})}^{- 1} = {A^{- 1} \otimes B^{- 1}}$. Fortunately, there are efficient techniques for inverting such matrices which we discuss in detail in Appendix B.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Examining the approximation quality", "weight": 1.0} -->

Figures 5 and 6 examine the quality of the approximations $\breve{F}$ and $\hat{F}$ of $\overset{\sim}{F}$, which are derived by approximating ${\overset{\sim}{F}}^{- 1}$ as block-diagonal and block-tridiagonal (resp.), for an example network.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Examining the approximation quality", "weight": 1.0} -->

From Figure 5, which compares $\breve{F}$ and $\hat{F}$ directly to $\overset{\sim}{F}$, we can see that while $\breve{F}$ and $\hat{F}$ exactly capture the diagonal and tridiagonal blocks (resp.) of $\overset{\sim}{F}$, as they must by definition, $\hat{F}$ ends up approximating the off-tridiagonal blocks of $\overset{\sim}{F}$ very well too. This is likely owed to the fact that the approximating assumption used to derive $\hat{F}$, that ${\overset{\sim}{F}}^{- 1}$ is block-tridiagonal, is a very reasonable one in practice (judging by Figure 3).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

Since the ${\overline{a}}_{i}$'s don't depend on $y$, we can take the expectation $E\left\lbrack {{\overline{a}}_{i}{\overline{a}}_{j}^{\top}} \right\rbrack$ with respect to just the training distribution ${\hat{Q}}_{x}$ over the inputs $x$. On the other hand, the $g_{i}$'s do depend on $y$, and so the expectation^33^3It is important to note this expectation should *not* be taken with respect to the training/data distribution over $y$ (i.e. ${\hat{Q}}_{y|x}$ or $Q_{y|x}$).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

Using the training/data distribution for $y$ would perhaps give an approximation to a quantity known as the "empirical Fisher information matrix", which lacks the previously discussed equivalence to the Generalized Gauss-Newton matrix, and would not be compatible with the theoretical analysis performed in Section 3.1 (in particular, Lemma 4 would break down). Moreover, such a choice would not give rise to what is usually thought of as the natural gradient, and based on the findings of Martens, would likely perform worse in practice as part of an optimization algorithm. See Martens for a more detailed discussion of the empirical Fisher and reasons why it may be a poor choice for a curvature matrix compared to the standard Fisher. $E\left\lbrack {g_{i}g_{j}^{\top}} \right\rbrack$ must be taken with respect to *both* ${\hat{Q}}_{x}$ and the network's predictive distribution $P_{y|x}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

While computing matrix-vector products with the $G_{i,j}$ could be done exactly and efficiently for a given input $x$ (or small mini-batch of $x$'s) by adapting the methods of Schraudolph, there doesn't seem to be a sufficiently efficient method for computing the entire matrix itself. Indeed, the hardness results of Martens et al. suggest that this would require, for each example $x$ in the mini-batch, work that is asymptotically equivalent to matrix-matrix multiplication involving matrices the same size as $G_{i,j}$. While a small constant number of such multiplications is arguably an acceptable cost (see Section 8), a number which grows with the size of the mini-batch would not be.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

Instead, we will approximate the expectation over $y$ by a standard Monte-Carlo estimate obtained by sampling $y$'s from the network's predictive distribution and then rerunning the backwards phase of backpropagation (see Algorithm 1) as if these were the training targets.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

Note that computing/estimating the required ${\overline{A}}_{i,j}$/$G_{i,j}$'s involves computing averages over outer products of various ${\overline{a}}_{i}$'s from network's usual forward pass, and $g_{i}$'s from the modified backwards pass (with targets sampled as above). Thus we can compute/estimate these quantities on the same input data used to compute the gradient $\nabla h$, at the cost of one or more additional backwards passes, and a few additional outer-product averages. Fortunately, this turns out to be quite inexpensive, as we have found that just one modified backwards pass is sufficient to obtain a good quality estimate in practice, and the required outer-product averages are similar to those already used to compute the gradient in the usual backpropagation algorithm.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

In the case of online/stochastic optimization we have found that the best strategy is to maintain running estimates of the required ${\overline{A}}_{i,j}$'s and $G_{i,j}$'s using a simple exponentially decaying averaging scheme. In particular, we take the new running estimate to be the old one weighted by $\epsilon$, plus the estimate on the new mini-batch weighted by $1 - \epsilon$, for some $0 \leq \epsilon < 1$. In our experiments we used $\epsilon = {\min{\{{1 - {1/k}},0.95\}}}$, where $k$ is the iteration number.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

Note that the more naive averaging scheme where the estimates from each iteration are given equal weight would be inappropriate here. This is because the ${\overline{A}}_{i,j}$'s and $G_{i,j}$'s depend on the network's parameters $\theta$, and these will slowly change over time as optimization proceeds, so that estimates computed many iterations ago will become stale.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

This kind of exponentially decaying averaging scheme is commonly used in methods involving diagonal or block-diagonal approximations (with much smaller blocks than ours) to the curvature matrix. Such schemes have the desirable property that they allow the curvature estimate to depend on much more data than can be reasonably processed in a single mini-batch.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Estimating the required statistics", "weight": 1.0} -->

Notably, for methods like HF which deal with the exact Fisher indirectly via matrix-vector products, such a scheme would be impossible to implement efficiently, as the exact Fisher matrix (or GGN) seemingly cannot be summarized using a compact data structure whose size is independent of the amount of data used to estimate it. Indeed, it seems that the only representation of the exact Fisher which would be independent of the amount of data used to estimate it would be an explicit $n \times n$ matrix (which is far too big to be practical). Because of this, HF and related methods must base their curvature estimates only on subsets of data that can be reasonably processed all at once, which limits their effectiveness in the stochastic optimization regime.

<!-- chunk {"id": "body-0068", "role": "body", "section": "A highly effective damping scheme for K-FAC", "weight": 1.0} -->

Methods like HF which use the exact Fisher seem to work reasonably well with an adaptive Tikhonov regularization technique where $\lambdaI$ is added to $F + {\etaI}$, and where $\lambda$ is adapted according to Levenberg-Marquardt style adjustment rule. This common and well-studied method can be shown to be equivalent to imposing an adaptive spherical region (known as a "trust region") which constrains the optimization of the quadratic model. However, we found that this simple technique is insufficient when used with our approximate natural gradient update proposals. In particular, we have found that there never seems to be a "good" choice for $\lambda$ that gives rise to updates which are of a quality comparable to those produced by methods that use the exact Fisher, such as HF.

<!-- chunk {"id": "body-0069", "role": "body", "section": "A highly effective damping scheme for K-FAC", "weight": 1.0} -->

One possible explanation for this finding is that, unlike quadratic models based on the exact Fisher (or equivalently, the GGN), the one underlying K-FAC has no guarantee of being accurate up to 2nd-order. Thus, $\lambda$ must remain large in order to compensate for this intrinsic 2nd-order inaccuracy of the model, which has the side effect of "washing out" the small eigenvalues (which represent important low-curvature directions).

<!-- chunk {"id": "body-0070", "role": "body", "section": "A highly effective damping scheme for K-FAC", "weight": 1.0} -->

Fortunately, through trial and error, we were able to find a relatively simple and highly effective damping scheme, which combines several different techniques, and which works well within K-FAC. Our scheme works by computing an initial update proposal using a version of the above described adaptive Tikhonov damping/regularization method, and then re-scaling this according to quadratic model computed using the exact Fisher. This second step is made practical by the fact that it only requires a single matrix-vector product with the exact Fisher, and this can be computed efficiently using standard methods. We discuss the details of this scheme in the following subsections.

<!-- chunk {"id": "body-0071", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

In the first stage of our damping scheme we generate a candidate update proposal $\Delta$ by applying a slightly modified form of Tikhononv damping to our approximate Fisher, before multiplying $- {\nabla h}$ by its inverse.

<!-- chunk {"id": "body-0072", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

In the usual Tikhonov regularization/damping technique, one adds ${({\lambda + \eta})}I$ to the curvature matrix (where $\eta$ accounts for the $\ell_{2}$ regularization), which is equivalent to adding a term of the form $\frac{\lambda + \eta}{2}{\|\delta\|}_{2}^{2}$ to the corresponding quadratic model (given by $M{(\delta)}$ with $F$ replaced by our approximation).

<!-- chunk {"id": "body-0073", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

For the block-diagonal approximation $\breve{F}$ of $\overset{\sim}{F}$ (from Section 4.2) this amounts to adding ${({\lambda + \eta})}I$ (for a lower dimensional $I$) to each of the individual diagonal blocks, which gives modified diagonal blocks of the form Because this is the sum of two Kronecker products we cannot use the simple identity ${({A \otimes B})}^{- 1} = {A^{- 1} \otimes B^{- 1}}$ anymore. Fortunately however, there are efficient techniques for inverting such matrices, which we discuss in detail in Appendix B.

<!-- chunk {"id": "body-0074", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

If we try to apply this same Tikhonov technique to our more sophisticated approximation $\hat{F}$ of $\overset{\sim}{F}$ (from Section 4.3) by adding ${({\lambda + \eta})}I$ to each of the diagonal blocks of $\hat{F}$, it is no longer clear how to efficiently invert $\hat{F}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

Instead, a solution which we have found works very well in practice (and which we also use for the block-diagonal approximation $\breve{F}$), is to add $\pi_{i}{(\sqrt{\lambda + \eta})}I$ and $\frac{1}{\pi_{i}}{(\sqrt{\lambda + \eta})}I$ for a scalar constant $\pi_{i}$ to the individual Kronecker factors ${\overline{A}}_{{i - 1},{i - 1}}$ and $G_{i,i}$ (resp.) of each diagonal block, giving As this is a single Kronecker product, all of the computations described in Sections 4.2 and 4.3 can still be used here too, simply by replacing each ${\overline{A}}_{{i - 1},{i - 1}}$ and $G_{i,i}$ with their modified versions ${\overline{A}}_{{i - 1},{i -

<!-- chunk {"id": "body-0076", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

To see why the expression in eqn. 7 is a reasonable approximation to eqn. 6, note that expanding it gives which differs from eqn. 6 by the residual error expression While the choice of $\pi_{i} = 1$ is simple and can sometimes work well in practice, a slightly more principled choice can be found by minimizing the obvious upper bound (following from the triangle inequality) on the matrix norm of this residual expression, for some matrix norm $\parallel \cdot \parallel_{\upsilon}$. This gives Evaluating this expression can be done efficiently for various common choices of the matrix norm $\parallel \cdot \parallel_{\upsilon}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

In our experience, one of the best and must robust choices for the norm $\parallel \cdot \parallel_{\upsilon}$ is the trace-norm, which for PSD matrices is given by the trace. With this choice, the formula for $\pi_{i}$ has the following simple form: where $d_{i}$ is the dimension (number of units) in layer $i$. Intuitively, the inner fraction is just the average eigenvalue of ${\overline{A}}_{{i - 1},{i - 1}}$ divided by the average eigenvalue of $G_{i,i}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "A factored Tikhonov regularization technique", "weight": 1.0} -->

Interestingly, we have found that this factored approximate Tikhonov approach, which was originally motivated by computational concerns, often works better than the exact version (eqn. 6) in practice. The reasons for this are still somewhat mysterious to us, but it may have to do with the fact that the inverse of the product of two quantities is often most robustly estimated as the inverse of the product of their individually regularized estimates.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Re-scaling according to the exact $F$", "weight": 1.0} -->

Given an update proposal $\Delta$ produced by multiplying the negative gradient $- {\nabla h}$ by our approximate Fisher inverse (subject to the Tikhonov technique described in the previous subsection), the second stage of our proposed damping scheme re-scales $\Delta$ according to the quadratic model $M$ as computed with the exact $F$, to produce a final update $\delta = {\alpha\Delta}$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Re-scaling according to the exact $F$", "weight": 1.0} -->

More precisely, we optimize $\alpha$ according to the value of the quadratic model as computed using an estimate of the exact Fisher $F$ (to which we add the $\ell_{2}$ regularization + Tikhonov term ${({\lambda + \eta})}I$). Because this is a 1-dimensional quadratic minimization problem, the formula for the optimal $\alpha$ can be computed very efficiently as To evaluate this formula we use the current stochastic gradient $\nabla h$ (i.e. the same one used to produce $\Delta$), and compute matrix-vector products with $F$ using the input data from the same mini-batch. While using a mini-batch to compute $F$ gets away from the idea of basing our estimate of the curvature on a long history of data (as we do with our *approximate* Fisher), it is made slightly less objectionable by the fact that we are only using it to estimate a single scalar quantity ($\Delta^{\top}F\Delta$).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Re-scaling according to the exact $F$", "weight": 1.0} -->

This is to be contrasted with methods like HF which perform a long and careful optimization of $M{(\delta)}$ using such an estimate of $F$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Re-scaling according to the exact $F$", "weight": 1.0} -->

Because the matrix-vector products with $F$ are only used to compute scalar quantities in K-FAC, we can reduce their computational cost by roughly one half (versus standard matrix-vector products with $F$) using a simple trick which is discussed in Appendix C.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Re-scaling according to the exact $F$", "weight": 1.0} -->

Intuitively, this second stage of our damping scheme effectively compensates for the intrinsic inaccuracy of the approximate quadratic model (based on our approximate Fisher) used to generate the initial update proposal $\Delta$, by essentially falling back on a more accurate quadratic model based on the exact Fisher.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Re-scaling according to the exact $F$", "weight": 1.0} -->

Interestingly, by re-scaling $\Delta$ according to $M{(\delta)}$, K-FAC can be viewed as a version of HF which uses our approximate Fisher as a preconditioning matrix (instead of the traditional diagonal preconditioner), and runs CG for only 1 step, initializing it from 0. This observation suggests running CG for longer, thus obtaining an algorithm which is even closer to HF (although using a much better preconditioner for CG). Indeed, this approach works reasonably well in our experience, but suffers from some of the same problems that HF has in the stochastic setting, due its much stronger use of the mini-batch--estimated exact $F$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Adapting $\\lambda$", "weight": 1.0} -->

Tikhonov damping can be interpreted as implementing a trust-region constraint on the update $\delta$, so that in particular the constraint ${\|\delta\|} \leq r$ is imposed for some $r$, where $r$ depends on $\lambda$ and the curvature matrix. While some approaches adjust $r$ and then seek to find the matching $\lambda$, it is often simpler just to adjust $\lambda$ directly, as the precise relationship between $\lambda$ and $r$ is complicated, and the curvature matrix is constantly evolving as optimization takes place.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Adapting $\\lambda$", "weight": 1.0} -->

The theoretically well-founded Levenberg-Marquardt style rule used by HF for doing this, which we will adopt for K-FAC, is given by if $\rho > {3/4}$ then $\lambda\leftarrow{\omega_{1}\lambda}$ if $\rho < {1/4}$ then $\lambda\leftarrow{\frac{1}{\omega_{1}}\lambda}$ where $\rho \equiv \frac{{h{({\theta + \delta})}} - {h{(\theta)}}}{{M{(\delta)}} - {M{}}}$ is the "reduction ratio" and $0 < \omega_{1} < 1$ is some decay constant, and all quantities are computed on the current mini-batch (and $M$ uses the exact $F$).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Adapting $\\lambda$", "weight": 1.0} -->

Intuitively, this rule tries to make $\lambda$ as small as possible (and hence the implicit trust-region as large as possible) while maintaining the property that the quadratic model $M{(\delta)}$ remains a good *local* approximation to $h$ (in the sense that it accurately predicts the value of $h{({\theta + \delta})}$ for the $\delta$ which gets chosen at each iteration). It has the desirable property that as the optimization enters the final convergence stage where $M$ becomes an almost exact approximation in a sufficiently large neighborhood of the local minimum, the value of $\lambda$ will go rapidly enough towards $0$ that it doesn't interfere with the asymptotic local convergence theory enjoyed by 2nd-order methods.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Adapting $\\lambda$", "weight": 1.0} -->

In our experiments we applied this rule every $T_{1}$ iterations of K-FAC, with $\omega_{1} = {({19/20})}^{T_{1}}$ and $T_{1} = 5$, from a starting value of $\lambda = 150$. Note that the optimal value of $\omega_{1}$ and the starting value of $\lambda$ may be application dependent, and setting them inappropriately could significantly slow down K-FAC in practice.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Adapting $\\lambda$", "weight": 1.0} -->

Computing $\rho$ can be done quite efficiently. Note that for the optimal $\delta$, ${{M{(\delta)}} - {M{}}} = {\frac{1}{2}{\nabla{h^{\top}\delta}}}$, and $h{(\theta)}$ is available from the usual forward pass. The only remaining quantity which is needed to evaluate $\rho$ is thus $h{({\theta + \delta})}$, which will require an additional forward pass. But fortunately, we only need to perform this once every $T_{1}$ iterations.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Maintaining a separate damping strength for the approximate Fisher", "weight": 1.0} -->

While the scheme described in the previous sections works reasonably well in most situations, we have found that in order to avoid certain failure cases and to be truly robust in a large variety of situations, the Tikhonov damping strength parameter for the factored Tikhonov technique described in Section 6.3 should be maintained and adjusted independently of $\lambda$. To this end we replace the expression $\sqrt{\lambda + \eta}$ in Section 6.3 with a separate constant $\gamma$, which we initialize to $\sqrt{\lambda + \eta}$ but which is then adjusted using a different rule, which is described at the end of this section.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Maintaining a separate damping strength for the approximate Fisher", "weight": 1.0} -->

The reasoning behind this modification is as follows. The role of $\lambda$, according to the Levenberg Marquardt theory, is to be as small as possible while maintaining the property that the quadratic model $M$ remains a trust-worthy approximation of the true objective. Meanwhile, $\gamma$'s role is to ensure that the initial update proposal $\Delta$ is as good an approximation as possible to the true optimum of $M$ (as computed using a mini-batch estimate of the exact $F$), so that in particular the re-scaling performed in Section 6.4 is as benign as possible. While one might hope that adding the same multiple of the identity to our approximate Fisher as we do to the exact $F$ (as it appears in $M$) would produce the best $\Delta$ in this regard, this isn't obviously the case. In particular, using a larger multiple may help compensate for the approximation we are making to the Fisher when computing $\Delta$, and thus help produce a more "conservative" but ultimately more useful initial update proposal $\Delta$, which is what we observe happens in practice.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Maintaining a separate damping strength for the approximate Fisher", "weight": 1.0} -->

A simple measure of the quality of our choice of $\gamma$ is the (negative) value of the quadratic model ${M{(\delta)}} = {M{({\alpha\Delta})}}$ for the optimally chosen $\alpha$. To adjust $\gamma$ based on this measure (or others like it) we use a simple greedy adjustment rule. In particular, every $T_{2}$ iterations during the optimization we try 3 different values of $\gamma$ ($\gamma_{0}$, $\omega_{2}\gamma_{0}$, and ${({1/\omega_{2}})}\gamma_{0}$, where $\gamma_{0}$ is the current value) and choose the new $\gamma$ to be the best of these, as measured by our quality metric.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Maintaining a separate damping strength for the approximate Fisher", "weight": 1.0} -->

In our experiments we used $T_{2} = 20$ (which must be a multiple of the constant $T_{3}$ as defined in Section 8), and $\omega_{2} = {(\sqrt{19/20})}^{T_{2}}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Maintaining a separate damping strength for the approximate Fisher", "weight": 1.0} -->

We have found that $M{(\delta)}$ works well in practice as a measure of the quality of $\gamma$, and has the added bonus that it can be computed at essentially no additional cost from the incidental quantities already computed when solving for the optimal $\alpha$. In our initial experiments we found that using it gave similar results to those obtained by using other obvious measures for the quality of $\gamma$, such as $h{({\theta + \delta})}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Momentum", "weight": 1.0} -->

Sutskever et al. found that momentum was very helpful in the context of stochastic gradient descent optimization of deep neural networks. A version of momentum is also present in the original HF method, and it plays an arguably even more important role in more "stochastic" versions of HF.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Momentum", "weight": 1.0} -->

A natural way of adding momentum to K-FAC, and one which we have found works well in practice, is to take the update to be $\delta = {{\alpha\Delta} + {\mu\delta_{0}}}$, where $\delta_{0}$ is the final update computed at the previous iteration, and where $\alpha$ and $\mu$ are chosen to minimize $M{(\delta)}$. This allows K-FAC to effectively build up a better solution to the local quadratic optimization problem ${\min_{\delta}M}{(\delta)}$ (where $M$ uses the *exact* $F$) over many iterations, somewhat similarly to how Matrix Momentum and HF do this.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Momentum", "weight": 1.0} -->

The optimal solution for $\alpha$ and $\mu$ can be computed as The main cost in evaluating this formula is computing the two matrix-vector products $F\Delta$ and $F\delta_{0}$. Fortunately, the technique discussed in Appendix C can be applied here to compute the 4 required scalars at the cost of only two forwards passes (equivalent to the cost of only one matrix-vector product with $F$).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Momentum", "weight": 1.0} -->

Empirically we have found that this type of momentum provides substantial acceleration in regimes where the gradient signal has a low noise to signal ratio, which is usually the case in the early to mid stages of stochastic optimization, but can also be the case in later stages if the mini-batch size is made sufficiently large. These findings are consistent with predictions made by convex optimization theory, and with older empirical work done on neural network optimization.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Momentum", "weight": 1.0} -->

Notably, because the implicit "momentum decay constant" $\mu$ in our method is being computed on the fly, one doesn't have to worry about setting schedules for it, or adjusting it via heuristics, as one often does in the context of SGD.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Momentum", "weight": 1.0} -->

Interestingly, if $h$ is a quadratic function (so the definition of $M{(\delta)}$ remains fixed at each iteration) and all quantities are computed deterministically (i.e. without noise), then using this type of momentum makes K-FAC equivalent to performing preconditioned linear CG on $M{(\delta)}$, with the preconditioner given by our approximate Fisher. This follows from the fact that linear CG can be interpreted as a momentum method where the learning rate $\alpha$ and momentum decay coefficient $\mu$ are chosen to jointly minimize $M{(\delta)}$ at the current iteration.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Let $d$ be the typical number of units in each layer and $m$ the mini-batch size.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

The significant computational tasks required to compute a single update/iteration of K-FAC, and rough estimates of their associated computational costs, are as follows: standard forwards and backwards pass: $2C_{1}\elld^{2}m$ computation of the gradient $\nabla h$ on the current mini-batch using quantities computed in backwards pass: $C_{2}\elld^{2}m$ additional backwards pass with random targets (as described in Section 5): $C_{1}\elld^{2}m$ updating the estimates of the required ${\overline{A}}_{i,j}$'s and $G_{i,j}$'s from quantities computed in the forwards pass and the additional randomized backwards pass: $2C_{2}\elld^{2}m$ matrix inverses (or SVDs for the block-tridiagonal inverse, as described in Appendix B) required to compute the inverse of the approximate Fisher: $C_{3}\elld^{3}$ for the block-diagonal inverse,

<!-- chunk {"id": "body-0103", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

$C_{4}\elld^{3}$ for the block-tridiagonal inverse various matrix-matrix products required to compute the matrix-vector product of the approximate inverse with the stochastic gradient: $C_{5}\elld^{3}$ for the block-diagonal inverse, $C_{6}\elld^{3}$ for the block-tridiagonal inverse matrix-vector products with the exact $F$ on the current mini-batch using the approach in Appendix C: $4C_{1}\elld^{2}m$ with momentum, $2C_{1}\elld^{2}m$ without momentum additional forward pass required to evaluate the reduction ratio $\rho$ needed to apply the $\lambda$ adjustment rule described in Section 6.5: $C_{1}\elld^{2}m$ every $T_{1}$ iterations Here the $C_{i}$ are various constants that account for implementation details, and we are assuming the use of the naive cubic matrix-matrix multiplication and inversion algorithms when producing the cost estimates.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Note that it it is hard to assign precise values to the constants, as they very much depend on how these various tasks are implemented.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Note that most of the computations required for these tasks will be sped up greatly by performing them in parallel across units, layers, training cases, or all of these. The above cost estimates however measure sequential operations, and thus may not accurately reflect the true computation times enjoyed by a parallel implementation. In our experiments we used a vectorized implementation that performed the computations in parallel over units and training cases, although not over layers (which is possible for computations that don't involve a sequential forwards or backwards "pass" over the layers).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Tasks 1 and 2 represent the standard stochastic gradient computation.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

The costs of tasks 3 and 4 are similar and slightly smaller than those of tasks 1 and 2. One way to significantly reduce them is to use a random subset of the current mini-batch of size $\tau_{1}m$ to update the estimates of the required ${\overline{A}}_{i,j}$'s and $G_{i,j}$'s. One can similarly reduce the cost of task 7 by computing the (factored) matrix-vector product with $F$ using such a subset of size $\tau_{2}m$, although we recommend proceeding with caution when doing this, as using inconsistent sets of data for the quadratic and linear terms in $M{(\delta)}$ can hypothetically cause instability problems which are avoided by using consistent data (see Martens and Sutskever, Section 13.1). In our experiments in Section 13 we used $\tau_{1} = {1/8}$ and $\tau_{2} = {1/4}$, which seemed to have a negligible effect on the quality of the resultant updates, while significantly reducing per-iteration computation time.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

In a separate set of unreported experiments we found that in certain situations, such as when $\ell_{2}$ regularization isn't used and the network starts heavily overfitting the data, or when smaller mini-batches were used, we had to revert to using $\tau_{2} = 1$ to prevent significant deterioration in the quality of the updates.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

The cost of task 8 can be made relatively insignificant by making the adjustment period $T_{1}$ for $\lambda$ large enough. We used $T_{1} = 5$ in our experiments.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

The costs of tasks 5 and 6 are hard to compare directly with the costs associated with computing the gradient, as their relative sizes will depend on factors such as the architecture of the neural network being trained, as well as the particulars of the implementation. However, one quick observation we can make is that both tasks 5 and 6 involve computations that be performed in parallel across the different layers, which is to be contrasted with many of the other tasks which require *sequential* passes over the layers of the network.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Clearly, if $m \gg d$, then the cost of tasks 5 and 6 becomes negligible in comparison to the others. However, it is more often the case that $m$ is comparable or perhaps smaller than $d$. Moreover, while algorithms for inverses and SVDs tend to have the same asymptotic cost as matrix-matrix multiplication, they are at least several times more expensive in practice, in addition to being harder to parallelize on modern GPU architectures (indeed, CPU implementations are often faster in our experience). Thus, $C_{3}$ and $C_{4}$ will typically be (much) larger than $C_{5}$ and $C_{6}$, and so in a basic/naive implementation of K-FAC, task 5 can dominate the overall per-iteration cost.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Fortunately, there are several possible ways to mitigate the cost of task 5. As mentioned above, one way is to perform the computations for each layer in parallel, and even simultaneously with the gradient computation and other tasks. In the case of our block-tridiagonal approximation to the inverse, one can avoid computing any SVDs or matrix square roots by using an iterative Stein-equation solver (see Appendix B). And there are also ways of reducing matrix-inversion (and even matrix square-root) to a short sequence of matrix-matrix multiplications using iterative methods. Furthermore, because the matrices in question only change slowly over time, one can consider hot-starting these iterative inversion methods from previous solutions. In the extreme case where $d$ is very large, one can also consider using low-rank + diagonal approximations of the ${\overline{A}}_{i,j}$ and $G_{i,j}$ matrices maintained online (e.g. using a similar strategy as Le Roux et al. ) from which inverses and/or SVDs can be more easily computed.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Although based on our experience such approximations can, in some cases, lead to a substantial degradation in the quality of the updates.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

While these ideas work reasonably well in practice, perhaps the simplest method, and the one we ended up settling on for our experiments, is to simply recompute the approximate Fisher inverse only every $T_{3}$ iterations (we used $T_{3} = 20$ in our experiments). As it turns out, the curvature of the objective stays relatively stable during optimization, especially in the later stages, and so in our experience this strategy results in only a modest decrease in the quality of the updates.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

If $m$ is much smaller than $d$, the costs associated with task 6 can begin to dominate (provided $T_{3}$ is sufficiently large so that the cost of task 5 is relatively small). And unlike task 5, task 6 must be performed at every iteration. While the simplest solution is to increase $m$ (while reaping the benefits of a less noisy gradient), in the case of the block-diagonal inverse it turns out that we can change the cost of task 6 from $C_{5}\elld^{3}$ to $C_{5}\elld^{2}m$ by taking advantage of the low-rank structure of the stochastic gradient. The method for doing this is described below.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

From Section 4.2, computing the ${\breve{F}}^{- 1}{\nabla h}$ amounts to computing $U_{i} = {G_{i,i}^{- 1}{({\nabla_{W_{i}}h})}{\overline{A}}_{{i - 1},{i - 1}}^{- 1}}$. Substituting in our mini-batch estimate of $\nabla_{W_{i}}h$ gives Direct evaluation of the expression on the right-hand side involves only matrix-matrix multiplications between matrices of size $m \times d$ and $d \times m$ (or between those of size $d \times d$ and $d \times m$), and thus we can reduce the cost of task 6 to $C_{5}\elld^{2}m$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Note that the use of standard $\ell_{2}$ weight-decay is not compatible with this trick. This is because the contribution of the weight-decay term to each $\nabla_{W_{i}}h$ is $\etaW_{i}$, which will typically not be low-rank. Some possible ways around this issue include computing the weight-decay contribution $\eta{\breve{F}}^{- 1}\theta$ separately and refreshing it only occasionally, or using a different regularization method, such as drop-out or weight-magnitude constraints.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Note that the adjustment technique for $\gamma$ described in Section 6.6 requires that, at every $T_{2}$ iterations, we compute 3 different versions of the update for each of 3 candidate values of $\gamma$. In an ideal implementation these could be computed in parallel with each other, although in the summary analysis below we will assume they are computed serially.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Summarizing, we have that with all of the various efficiency improvements discussed in this section, the average per-iteration computational cost of K-FAC, in terms of *serial* arithmetic operations, is where ${\chi_{mom},\chi_{tri}} \in {\{ 0,1\}}$ are flag variables indicating whether momentum and the block-tridiagonal inverse approximation (resp.) are used.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Computational Costs and Efficiency Improvements", "weight": 1.0} -->

Plugging in the values of these various constants that we used in our experiments, for the block-diagonal inverse approximation ($\chi_{tri} = 0$) this becomes and for the block-tridiagonal inverse approximation ($\chi_{tri} = 1$) which is to be compared to the per-iteration cost of SGD, as given by

<!-- chunk {"id": "body-0121", "role": "body", "section": "Pseudocode for K-FAC", "weight": 1.0} -->

Algorithm 2 gives high-level pseudocode for the K-FAC method, with the details of how to perform the computations required for each major step left to their respective sections.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Pseudocode for K-FAC", "weight": 1.0} -->

• Initialize θ1 (e.g. using a good method such as the ones described in Martens or Glorot and Bengio) • Choose initial values of λ (err on the side of making it too large) • $\gamma\leftarrow\sqrt{\lambda + \eta}$ while θk is not satisfactory do • Choose a mini-batch size m (e.g. using a fixed value, an adaptive rule, or some predefined schedule) • Select a random mini-batch S′ ⊂ S of training cases of size m • Select a random subset S1 ⊂ S′ of size τ1 |S′| • Select a random subset S2 ⊂ S′ of size τ2 |S′| • Perform a forward and backward pass on S′ to estimate the gradient ∇h (θk) (see Algorithm 1) • Perform an additional backwards pass on S1 using random targets generated from the model’s predictive distribution (as described in Section 5) • Update the estimates of the required ${\overline{A}}_{i,j}$’s and Gi, j’s using the ai’s computed in forward pass for S1,

<!-- chunk {"id": "body-0123", "role": "body", "section": "Pseudocode for K-FAC", "weight": 1.0} -->

and the gi’s computed in the additional backwards pass for S1 (as described Section 5) • Choose a set Γ of new candidate γ’s as described in Section 6.6 (setting Γ = {γ} if not adjusting γ at this iteration, i.e. if k ≢ 0 (mod T2)) if recomputing the approximate Fisher inverse this iteration (i.e. if k ≡ 0 (mod T3) or k ≤ 3) then • Compute the approximate Fisher inverse (using the formulas derived in Section 4.2 or Section 4.3) from versions of the current ${\overline{A}}_{i,j}$’s and Gi, j’s which are modified as per the factored Tikhonov damping technique described in Section 6.3 (but using γ as described in Section 6.6) • Compute the update proposal Δ by multiplying current estimate of approximate Fisher inverse by the estimate of ∇h (using the formulas derived in Section 4.2 or Section 4.3).

<!-- chunk {"id": "body-0124", "role": "body", "section": "Pseudocode for K-FAC", "weight": 1.0} -->

For layers with size d < m consider using trick described at the end of Section 8 for increased efficiency. • Compute the final update δ from Δ as described in Section 6.4 (or Section 7 if using momentum) where the matrix-vector products with F are estimated on S2 using the ai’s computed in the forward pass • Select the δ and the new γ computing in the above loop that correspond to the lowest value of M (δ) (see Section 6.6) if updating λ this iteration (i.e. if k ≡ 0 (mod T1)) then • Update λ with the Levenberg-Marquardt style rule described in Section 6.5 Algorithm 2 High-level pseudocode for K-FAC

<!-- chunk {"id": "body-0125", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

When computed with the exact Fisher, the natural gradient specifies a direction in the space of predictive distributions which is invariant to the specific way that the model is parameterized. This invariance means that the smooth path through distribution space produced by following the natural gradient with infinitesimally small steps will be similarly invariant.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

For a practical natural gradient based optimization method which takes large discrete steps in the direction of the natural gradient, this invariance of the optimization path will only hold approximately. As shown by Martens, the approximation error will go to zero as the effects of damping diminish and the reparameterizing function $\zeta$ tends to a locally linear function. Note that the latter will happen as $\zeta$ becomes smoother, or the local region containing the update shrinks to zero.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

Because K-FAC uses an approximation of the natural gradient, these invariance results are not applicable in our case. Fortunately, as was shown by Martens, one can establish invariance of an update direction with respect to a given reparameterization of the model by verifying certain simple properties of the curvature matrix $C$ used to compute the update. We will use this result to show that, under the assumption that damping is absent (or negligible in its affect), K-FAC is invariant to a broad and natural class of transformations of the network.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

This class of transformations is given by the following modified network definition (c.f. the definition in Section 2.1): where ${\overline{\phi}}_{i}$ is the function that computes $\phi_{i}$ and then appends a homogeneous coordinate (with value 1), $\Omega_{i}$ and $\Phi_{i}$ are arbitrary invertible matrices of the appropriate sizes (except that we assume $\Omega_{\ell} = I$), ${\overline{a}}_{0}^{\dagger} = {\Omega_{0}{\overline{a}}_{0}}$, and where the network's output is given by ${f^{\dagger}{(x,\theta)}} = a_{\ell}^{\dagger}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

Note that because $\Omega_{i}$ multiplies ${\overline{\phi}}_{i}{({\Phi_{i}s_{i}^{\dagger}})}$, it can implement arbitrary translations of the unit activities $\phi_{i}{({\Phi_{i}s_{i}^{\dagger}})}$ in addition to arbitrary linear transformations. Figure 8 illustrates our modified network definition for $\ell = 2$ (c.f. Figure 1).

<!-- chunk {"id": "body-0130", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

Here, and going forward, we will add a "$\dagger$" superscript to any network-dependent quantity in order to denote the analogous version of it computed by the transformed network. Note that under this identification, the loss derivative formulas for the transformed network are analogous to those of the original network, and so our various Fisher approximations are still well defined.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Invariance Properties and the Relationship to Whitening and Centering", "weight": 1.0} -->

The following theorem describes the main technical result of this section.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Heskes' interpretation of the block-diagonal approximation", "weight": 1.0} -->

Heskes discussed an alternative interpretation of the block-diagonal approximation which yields some useful insight to complement our own theoretical analysis. In particular, he observed that the block-diagonal Fisher approximation $\breve{F}$ is the curvature matrix corresponding to the following quadratic function which measures the difference between the new parameter value $\theta'$ and the current value $\theta$: Here, $s_{i}' = {W_{i}'{\overline{a}}_{i - 1}}$, and the $s_{i}$'s and ${\overline{a}}_{i}$'s are determined by $\theta$ and are independent of $\theta'$ (which determines the $W_{i}'$'s). $D{(\theta',\theta)}$ can be interpreted as a reweighted sum of squared changes of each of the $s_{i}$'s.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Heskes' interpretation of the block-diagonal approximation", "weight": 1.0} -->

The reweighing matrix $G_{i,i}$ is given by where $P_{y|s_{i}}^{(i)}$ is the network's predictive distribution as parameterized by $s_{i}$, and $F_{P_{y|s_{i}}^{(i)}}$ is its Fisher information matrix, and where the expectation is taken w.r.t. the distribution on $s_{i}$ (as induced by the distribution on the network's input $x$).

<!-- chunk {"id": "body-0134", "role": "body", "section": "Heskes' interpretation of the block-diagonal approximation", "weight": 1.0} -->

Thus, the effect of reweighing by the $G_{i,i}$'s is to (approximately) translate changes in $s_{i}$ into changes in the predictive distribution over $y$, although using the expected/average Fisher $G_{i,i} = {E{\lbrack F_{P_{y|s_{i}}^{(i)}}\rbrack}}$ instead of the more specific Fisher $F_{P_{y|s_{i}}^{(i)}}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Heskes' interpretation of the block-diagonal approximation", "weight": 1.0} -->

Interestingly, if one used $F_{P_{y|s_{i}}^{(i)}}$ instead of $G_{i,i}$ in the expression for $D{(\theta',\theta)}$, then $D{(\theta',\theta)}$ would correspond to a basic layer-wise block-diagonal approximation of $F$ where the blocks are computed exactly (i.e. without the Kronecker-factorizing approximation introduced in Section 3). Such an approximate Fisher would have the interpretation of being the Hessian w.r.t. $\theta'$ of either of the measures Note that each term in either of these sums is a function measuring an intrinsic quantity (i.e. changes in the output distribution), and so overall these are intrinsic measures except insofar as they assume that $\theta$ is divided into $\ell$ independent groups that each parameterize one of the $\ell$ different predictive distributions (which are each conditioned on their respective $a_{i - 1}$'s).

<!-- chunk {"id": "body-0136", "role": "body", "section": "Heskes' interpretation of the block-diagonal approximation", "weight": 1.0} -->

It is not clear whether $\breve{F}$, with its Kronecker-factorizing structure can similarly be interpreted as the Hessian of such a self-evidently intrinsic measure. If it could be, then this would considerably simplify the proof of our Theorem 1 (e.g. using the techniques of Arnold et al. ). Note that $D{(\theta',\theta)}$ itself doesn't work, as it isn't obviously intrinsic. Despite this, as shown in Section 10, both $\breve{F}$ and our more advanced approximation $\hat{F}$ produce updates which have strong invariance properties.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Experiments", "weight": 1.0} -->

To investigate the practical performance of K-FAC we applied it to the 3 deep autoencoder optimization problems from Hinton and Salakhutdinov, which use the "MNIST", "CURVES", and "FACES" datasets respectively (see Hinton and Salakhutdinov for a complete description of the network architectures and datasets). Due to their high difficulty, performance on these problems has become a standard benchmark for neural network optimization methods. We included $\ell_{2}$ regularization with a coefficient of $\eta = 10^{- 5}$ in each of these three optimization problems (i.e. so that $\frac{\eta}{2}{\|\theta\|}_{2}^{2}$ was added to the objective), which is lower than what was used by Martens, but higher than what was used by Sutskever et al..

<!-- chunk {"id": "body-0138", "role": "body", "section": "Experiments", "weight": 1.0} -->

As our baseline we used the version of SGD with momentum based on Nesterov's Accelerated Gradient described in Sutskever et al., which was calibrated to work well on these particular deep autoencoder problems. For each problem we followed the prescription given by Sutskever et al. for determining the learning rate, and the increasing schedule for the decay parameter $\mu$. We did not compare to methods based on diagonal approximations of the curvature matrix, as in our experience such methods tend not perform as well on these kinds of optimization problems as the baseline does (an observation which is consistent with the findings of Schraudolph; Zeiler ).

<!-- chunk {"id": "body-0139", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our implementation of K-FAC used most of the efficiency improvements described in Section 8, except that all "tasks" were computed serially (and thus with better engineering and more hardware, a faster implementation could likely be obtained). Because the mini-batch size $m$ tended to be comparable to or larger than the typical/average layer size $d$, we did not use the technique described at the end of Section 8 for accelerating the computation of the approximate inverse, as this only improves efficiency in the case where $m < d$, and will otherwise decrease efficiency.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Experiments", "weight": 1.0} -->

Both K-FAC and the baseline were implemented using vectorized MATLAB code accelerated with the GPU package Jacket. The code for K-FAC is available for download^44^4 All tests were performed on a single computer with a 4.4 Ghz 6 core Intel CPU and an NVidia GTX 580 GPU with 3GB of memory. Each method used the same initial parameter setting, which was generated using the "sparse initialization" technique from Martens (which was also used by Sutskever et al. ).

<!-- chunk {"id": "body-0141", "role": "body", "section": "Experiments", "weight": 1.0} -->

To help mitigate the detrimental effect that the noise in the stochastic gradient has on the convergence of the baseline (and to a lesser extent K-FAC as well) we used a exponentially decayed iterate averaging approach based loosely on Polyak averaging. In particular, at each iteration we took the "averaged" parameter estimate to be the previous such estimate, multiplied by $\xi$, plus the new iterate produced by the optimizer, multiplied by $1 - \xi$, for $\xi = 0.99$. Since the training error associated with the optimizer's current iterate may sometimes be lower than the training error associated with the averaged estimate (which will often be the case when the mini-batch size $m$ is very large), we report the minimum of these two quantities.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Experiments", "weight": 1.0} -->

To be consistent with the numbers given in previous papers we report the reconstruction error instead of the actual objective function value (although these are almost perfectly correlated in our experience). And we report the error on the training set as opposed to the test set, as we are chiefly interested in optimization speed and not the generalization capabilities of the networks themselves.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Experiments", "weight": 1.0} -->

In our first experiment we examined the relationship between the mini-batch size $m$ and the per-iteration rate of progress made by K-FAC and the baseline on the MNIST problem. The results from this experiment are plotted in Figure 9. They strongly suggest that the per-iteration rate of progress of K-FAC tends to a superlinear function of $m$ (which can be most clearly seen by examining the plots of training error vs training cases processed), which is to be contrasted with the baseline, where increasing $m$ has a much smaller effect on the per-iteration rate of progress, and with K-FAC without momentum, where the per-iteration rate of progress seems to be a linear or slightly sublinear function of $m$. It thus appears that the main limiting factor in the convergence of K-FAC (with momentum applied) is the noise in the gradient, at least in later stages of optimization, and that this is not true of the baseline to nearly the same extent. This would seem to suggest that K-FAC, much more than SGD, would benefit from a massively parallel distributed implementation which makes use of more computational resources than a single GPU.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Experiments", "weight": 1.0} -->

But even in the single CPU/GPU setting, the fact that the per-iteration rate of progress tends to a *superlinear* function of $m$, while the per-iteration computational cost of K-FAC is a roughly linear function of $m$, suggests that in order to obtain the best per-second rate of progress with K-FAC, we should use a rapidly increasing schedule for $m$. To this end we designed an exponentially increasing schedule for $m$, given by $m_{k} = {\min{({m_{1}{\exp{({{({k - 1})}/b})}}},{|S|})}}$, where $k$ is the current iteration, $m_{1} = 1000$, and where $b$ is chosen so that $m_{500} = {|S|}$. The approach of increasing the mini-batch size in this way is analyzed by Friedlander and Schmidt.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Experiments", "weight": 1.0} -->

Note that for other neural network optimization problems, such as ones involving larger training datasets than these autoencoder problems, a more slowly increasing schedule, or one that stops increasing well before $m$ reaches $|S|$, may be more appropriate. One may also consider using an approach similar to that of Byrd et al. for adaptively determining a suitable mini-batch size.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Experiments", "weight": 1.0} -->

In our second experiment we evaluated the performance of our implementation of K-FAC versus the baseline on all 3 deep autoencoder problems, where we used the above described exponentially increasing schedule for $m$ for K-FAC, and a fixed setting of $m$ for the baseline and momentum-less K-FAC (which was chosen from a small range of candidates to give the best overall per-second rate of progress). The relatively high values of $m$ chosen for the baseline ($m = 250$ for CURVES, and $m = 500$ for MNIST and FACES, compared to the $m = 200$ which was used by Sutskever et al. ) reflect the fact that our implementation of the baseline uses a high-performance GPU and a highly optimized linear algebra package, which allows for many training cases to be efficiently processed in parallel. Indeed, after a certain point, making $m$ much smaller didn't result in a significant reduction in the baseline's per-iteration computation time.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Experiments", "weight": 1.0} -->

Note that in order to process the very large mini-batches required for the exponentially increasing schedule without overwhelming the memory of the GPU, we partitioned the mini-batches into smaller "chunks" and performed all computations involving the mini-batches, or subsets thereof, one chunk at a time.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Experiments", "weight": 1.0} -->

The results from this second experiment are plotted in Figures 10 and 11. For each problem K-FAC had a *per-iteration* rate of progress which was orders of magnitude higher than that of the baseline's (Figure 11), provided that momentum was used, which translated into an overall much higher *per-second* rate of progress (Figure 10), despite the higher cost of K-FAC's iterations (due mostly to the much larger mini-batch sizes used). Note that Polyak averaging didn't produce a significant increase in convergence rate of K-FAC in this second experiment (actually, it hurt a bit) as the increasing schedule for $m$ provided a much more effective (although expensive) solution to the problem of noise in the gradient.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Experiments", "weight": 1.0} -->

The importance of using some form of momentum on these problems is emphasized in these experiments by the fact that without the momentum technique developed in Section 7, K-FAC wasn't significantly faster than the baseline (which itself used a strong form of momentum). These results echo those of Sutskever et al., who found that without momentum, SGD was orders of magnitude slower on these particular problems. Indeed, if we had included results for the baseline without momentum they wouldn't even have appeared in the axes boundaries of the plots in Figure 10.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Experiments", "weight": 1.0} -->

Recall that the type of momentum used by K-FAC compensates for the inexactness of our approximation to the Fisher by allowing K-FAC to build up a better solution to the exact quadratic model minimization problem (defined using the exact Fisher) across many iterations. Thus, if we were to use a much stronger approximation to the Fisher when computing our update proposals $\Delta$, the benefit of using this type of momentum would have likely been much smaller than what we observed. One might hypothesize that it is the particular type of momentum used by K-FAC that is mostly responsible for its advantages over the SGD baseline. However in our testing we found that for SGD the more conventional type of momentum used by Sutskever et al. performs significantly better.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Experiments", "weight": 1.0} -->

From Figure 11 we can see that the block-tridiagonal version of K-FAC has a per-iteration rate of progress which is typically 25% to 40% larger than the simpler block-diagonal version. This observation provides empirical support for the idea that the block-tridiagonal approximate inverse Fisher ${\hat{F}}^{- 1}$ is a more accurate approximation of $F^{- 1}$ than the block-diagonal approximation ${\breve{F}}^{- 1}$. However, due to the higher cost of the iterations in the block-tridiagonal version, its overall per-second rate of progress seems to be only moderately higher than the block-diagonal version's, depending on the problem.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Experiments", "weight": 1.0} -->

Note that while matrix-matrix multiplication, matrix inverse, and SVD computation all have the same computational complexity, in practice their costs differ significantly (in increasing order as listed). Computation of the approximate Fisher inverse, which is performed in our experiments once every 20 iterations (and for the first 3 iterations), requires matrix inverses for the block-diagonal version, and SVDs for the block-tridiagonal version. For the FACES problem, where the layers can have as many as 2000 units, this accounted for a significant portion of the difference in the average per-iteration computational cost of the two versions.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Experiments", "weight": 1.0} -->

While our results suggest that the block-diagonal version is probably the better option overall due to its greater simplicity (and comparable per-second progress rate), the situation may be different given a more efficient implementation of K-FAC where the more expensive SVDs required by the tri-diagonal version are computed approximately and/or in parallel with the other tasks, or perhaps even while the network is being optimized.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our results also suggest that K-FAC may be much better suited than the SGD baseline for a massively distributed implementation, since it would require far fewer synchronization steps (by virtue of the fact that it requires far fewer iterations).

<!-- chunk {"id": "body-0155", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

In this paper we developed K-FAC, an approximate natural gradient-based optimization method. We started by developing an efficiently invertible approximation to a neural network's Fisher information matrix, which we justified via a theoretical and empirical examination of the statistics of the gradient of a neural network. Then, by exploiting the interpretation of the Fisher as an approximation of the Hessian, we designed a developed a complete optimization algorithm using quadratic model-based damping/regularization techniques, which yielded a highly effective and robust method virtually free from the need for hyper-parameter tuning. We showed the K-FAC preserves many of natural gradient descent's appealing theoretical properties, such as invariance to certain reparameterizations of the network. Finally, we showed that K-FAC, when combined with a form of momentum and an increasing schedule for the mini-batch size $m$, far surpasses the performance of a well-tuned version of SGD with momentum on difficult deep auto-encoder optimization benchmarks (in the setting of a single GPU machine).

<!-- chunk {"id": "body-0156", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

Moreover, our results demonstrated that K-FAC requires orders of magnitude fewer total updates/iterations than SGD with momentum, making it ideally suited for a massively distributed implementation where synchronization is the main bottleneck.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Conclusions and future directions", "weight": 1.0} -->

Some potential directions for future development of K-FAC include: a better/more-principled handling of the issue of gradient stochasticity than a pre-determined increasing schedule for $m$ extensions of K-FAC to recurrent or convolutional architectures, which may require specialized approximations of their associated Fisher matrices an implementation that better exploits opportunities for parallelism described in Section 8 exploitation of massively distributed computation in order to compute high-quality estimates of the gradient
