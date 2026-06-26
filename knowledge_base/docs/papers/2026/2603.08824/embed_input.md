<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients

Topics include Benchmarks, Optimization, Optimal transport, SoftJAX & SoftTorch, Automatic differentiation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Automatic differentiation (AD) frameworks such as JAX and PyTorch have enabled gradient-based optimization for a wide range of scientific fields. Yet, many "hard" primitives in these libraries such as thresholding, Boolean logic, discrete indexing, and sorting operations yield zero or undefined gradients that are not useful for optimization. While numerous "soft" relaxations have been proposed that provide informative gradients, the respective implementations are fragmented across projects, making them difficult to combine and compare. This work introduces SoftJAX and SoftTorch, open-source, feature-complete libraries for soft differentiable programming. These libraries provide a variety of soft functions as drop-in replacements for their hard JAX and PyTorch counterparts. This includes (i) elementwise operators such as clip or abs, (ii) utility methods for manipulating Booleans and indices via fuzzy logic, (iii) axiswise operators such as sort or rank - based on optimal transport or permutahedron projections, and (iv) offer full support for straight-through gradient estimation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Overall, SoftJAX and SoftTorch make the toolbox of soft relaxations easily accessible to differentiable programming, as demonstrated through benchmarking and a practical case study. Code is available at github.com/a-paulus/softjax and github.com/a-paulus/softtorch.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automatic differentiation (AD) frameworks have enabled rapid progress in machine learning. They make gradient computation efficient, user-friendly, and composable. Thereby, they become a ubiquitous tool widely adopted beyond machine learning. This includes (i) *differentiable rendering* using Nerfs and Gaussian splatting; (ii) *differentiable simulation*, such as MuJoCo XLA (MJX) and WARP; (iii) *structured prediction* like ranking and matching; (iv) *combinatorial layers* for CEM, MPC, and discrete decisions; (v) *differentiable optimization*; and (vi) *physical simulations*, e. g., for a gravitational wave detector. However, the programs for these and many more applications contain classical operations using comparisons for branching code, ranking elements, and so forth.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, AD does not necessarily result in informative gradients. Here, *informative* means providing a stable local direction leading to improvements in the objective. Uninformative are cases with zero gradients (e. g., rounding, comparisons, indexing, sort/max/top-k/median) and arbitrary subgradients (ReLU at zero, sort with duplicates). Many applications call for replacing such hard operations with soft ones that yield informative gradients. A successful example is addressing the "dying ReLU problem", where ReLU's zero gradients hinder gradient-based optimization of deep neural networks, by replacing the ReLU function with a smooth relaxation such as SiLU or Softplus.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While many relaxation techniques have been proposed, the existing toolbox is fragmented. Proposed techniques include analytic smooth surrogates (e. g., SiLU for ReLU, sigmoid for steps, and softmax for argmax ), optimization-based approaches (e. g., sorting via regularized optimal transport or projections onto the permutahedron, proximal methods ), stochastic relaxations (e. g., Gumbel-softmax, perturbed optimizers ), gradient "hacks" / estimators (straight-through, black-box differentiation ) and more.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To unify soft relaxations and ease their use, we present *SoftJAX* and *SoftTorch*. Our libraries provide soft drop-in replacements for many commonly used hard operations in JAX and Pytorch. In turn, SoftJAX and SoftTorch form easy to use abstraction layers between user code and underlying primitive operations. Our treatment also draws unifying connections, generalizes various techniques, and provides comprehensible "softness" knobs and "mode" families across operations. As an example, see Figure 1 where we plot the soft $\operatorname{rank}$ operator for varying softness parameters $\tau>0$ and softening modes. As for all our relaxations, we recover the original hard operation as $\tau\rightarrow 0^{+}$. By combining the vast toolbox of soft relaxations, our libraries make *soft differentiable programming* accessible.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We next explain the operators implemented in SoftJAX and SoftTorch and how their hard versions are relaxed to soft counterparts. Section 2 reviews the basics of soft surrogates and straight-through estimation. Section 3 then describes the softening of elementwise operators in SoftJAX and SoftTorch, such as $\operatorname{sign}$ or $\operatorname{round}$, via relaxations of the Heaviside step function. Section 4 shows how more involved axiswise operators, such as $\operatorname{sort}$ or $\operatorname{quantile}$, can be softened via optimal transport or projections onto the unit simplex or the permutahedron. An overview of all currently implemented functions in SoftJAX is available in Figure 9. Finally, Section 5 presents runtime and memory comparisons to help end users select suitable methods that balance the trade-offs required by their applications.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Softening and Straight-through estimation", "weight": 1.0} -->

Many functions used in modern ML frameworks are poorly suited for automatic differentiation as they are discontinuous or have large regions with zero derivative. To resolve this, our libraries have one main goal: to provide informative gradients for any program written in the supported frameworks. The underlying mechanism rests on two core concepts: *soft surrogates* and *straight-through estimation*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Soft surrogate", "weight": 1.0} -->

*Soft surrogates* replace the original function with another function that has more informative gradients for optimization. Specifically, we call the function $f_{\tau}$ with softening parameter $\tau>0$ a *soft surrogate* of $f$ if (i) $f_{\tau}$ is continuous and differentiable almost everywhere, (ii) $f_{\tau}$ yields informative gradients over the relevant domain, i. e., avoids extended regions of zero derivative, and (iii) $f_{\tau}$ recovers $f$ in the limit $\tau\to 0^{+}$. The softening parameter $\tau$ controls the trade-off between faithfulness to $f$ and gradient informativeness: larger $\tau$ benefits differentiability, while $\tau\to 0^{+}$ causes $f_{\tau}$ to approach the original function. See Figure 2 for an example of a soft relu surrogate. Note that softening a function may involve significantly altering the output domain, e.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Soft surrogate", "weight": 1.0} -->

g., a soft surrogate for boolean operations outputs a probability instead of a Boolean value, likewise a soft surrogate for an argmax operation outputs a probability distribution over indices instead of an index.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Straight-through estimation", "weight": 1.0} -->

Unfortunately, blindly replacing a function with a soft surrogate may introduce undesired effects in the forward pass, e. g., resulting in unphysical rollout trajectories of a simulator. Fortunately, these problems can be addressed effectively through *straight-through estimation (STE)*.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Straight-through estimation", "weight": 1.0} -->

Historically, STE dates back to early work on single-layer perceptrons, where the derivative of binary activations was replaced with the derivative of the identity map. Following Bengio et al., STE keeps the original function in the forward pass during automatic differentiation, but uses the gradient of a soft surrogate in the backward pass. In our framework, STE is implemented via the straight-through trick, writing where $\operatorname{sg}$ denotes the stop-gradient operator of an automatic differentiation library. Therefore, we obtain $f_{\text{STE}}=f$ on the forward pass, but $\nabla f_{\text{STE}}=\nabla f_{\tau}$ on the backward pass. In practice, using a soft surrogate for differentiation amounts to wrapping a soft function like sj.relu in the sj.st function decorator, which implements the straight-through trick, i. e., y_soft_st = sj.st(sj.relu). Figure 2 illustrates straight-through wrapping a soft relu surrogate.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The straight-through pitfall", "weight": 1.0} -->

A subtle issue arises when STE-wrapped functions interact multiplicatively. Automatic differentiation computes the gradient between the product of functions $f_{\text{STE}}(x)$ and $g_{\text{STE}}(y)$ via the product rule as where the original functions $f$ and $g$ appear as multiplicative gates in the backward pass. This defeats the purpose of softening, as the gradient can still vanish when scaled by $f$ or $g$. As illustrated in Figure 3 for the case of $f(x,y)\coloneqq\operatorname{relu}(x)$ and $g(x,y)=\operatorname{relu}(y)$, $\nabla(f_{\text{STE}}\cdot g_{\text{STE}})$ is zero when $x,y<0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The straight-through pitfall", "weight": 1.0} -->

To avoid gradient multiplication by zero, STE should be applied to the *composite function* such that In code, this reads: (notice the decorator) [⬇](data:text/plain;base64,QHNqLnN0CmRlZiByZWx1X3Byb2QoeCwgeSwgKiprd2FyZ3MpOgogICAgcmVsdV94ID0gc2oucmVsdSh4LCAqKmt3YXJncykKICAgIHJlbHVfeSA9IHNqLnJlbHUoeSwgKiprd2FyZ3MpCiAgICByZXR1cm4gcmVsdV94ICogcmVsdV95){download=""} def relu_prod(x, y, \*\*kwargs): relu_x = sj.relu(x, \*\*kwargs) relu_y = sj.relu(y, \*\*kwargs) return relu_x \* relu_y To our knowledge, this "STE pitfall" and its remedy have not been explicitly discussed before.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Elementwise Operators", "weight": 1.0} -->

Conceptually, all our elementwise soft operators, some of which are illustrated in Figure 4, are rooted in the relaxation of the *Heaviside step function,* defined as Its derivative is zero everywhere except at the origin, where it is not defined. Following many previous works, we soften the Heaviside function with a sigmoidal function that traces a characteristic S-shape. Some examples include the standard exponential-based sigmoid (referred to as smooth mode) or the piece-wise polynomial-based sigmoidals^11^1We overload the notation here.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Elementwise Operators", "weight": 1.0} -->

The piecewise modes transition on $[-\tau,\tau]$; in the library, their input is rescaled by $1/5$ so that all modes share an effective transition width of approximately $10\tau$, matching the smooth mode ($\sigma(\pm 5)\approx 0.007/0.993$). These piece-wise Heaviside relaxations are either continuous (linear, also referred to as c0 mode), differentiable (c1), or twice differentiable (c2).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sign, abs, and round", "weight": 1.0} -->

A soft surrogate for the $\operatorname{sign}$ function is obtained by the Heaviside function and subtracting a constant.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sign, abs, and round", "weight": 1.0} -->

Moreover, a soft surrogate for the $\operatorname{abs}$ function is obtained by gating the soft $\operatorname{sign}$ function with $x$, reading Following Semenov, the $\operatorname{round}$ function is implemented as the difference between shifted sigmoidals | | $\displaystyle\footnotesize\begin{split}\operatorname{round}_{\tau}(x)\coloneqq\hskip-6.88889pt\sum_{k=\lfloor x\rfloor-K}^{\lfloor x\rfloor+K}\hskip-3.44444ptk\bigl[\operatorname{H}_{\tau}\bigl(x-k+\tfrac{1}{2}\bigr)-\operatorname{H}_{\tau}\bigl(x-k-\tfrac{1}{2}\bigr)\bigr],\end{split}$ | | where $K$ controls the number of neighbouring sigmoidals that are

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sign, abs, and round", "weight": 1.0} -->

taken into account. Larger temperatures $\tau$ require a higher $K$, as each sigmoidal is softened over a larger region, thereby increasing its region of influence.

<!-- chunk {"id": "body-0021", "role": "body", "section": "ReLU and clip", "weight": 1.0} -->

Due to its widespread use in ML, the rectified linear unit (ReLU) deserves extra attention. The function $\operatorname{relu}(x)\coloneqq\max\{0,x\}$ has zero gradient for $x<0$, and at $x=0$ it is only sub-differentiable. To get a soft surrogate, we can transform the sigmoidal via Integration or via a gating mechanism Therefore, for each of the Heaviside relaxations, we define two ReLU relaxations, some of which are well known. For instance, integrating the sigmoid yields the Softplus $\tau\log(1+e^{x/\tau}).$ On the other hand, gating the sigmoid recovers the SiLU activation $x\cdot\sigma(x/\tau)$. From the soft ReLU, we can now derive a soft surrogate for the $\operatorname{clip}$ function as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Comparison operators and differentiable logic", "weight": 1.0} -->

Next, we turn to soft surrogates of comparison operators, such as $\operatorname{greater}$ or $\operatorname{equal}$. The hard operators output a Boolean variable $b\in\{\text{True},\text{False}\}$, whereas our soft surrogates output a value in the interval $$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Comparison operators and differentiable logic", "weight": 1.0} -->

\operatorname{equal}_{\tau}(x,y)&=2\cdot\operatorname{less_equal}_{\tau}(\operatorname{abs}_{\tau}(x-y),0),\\ | | | | | \operatorname{isclose}_{\tau}(x,y)&=2\cdot\operatorname{less_equal}_{\tau}(\operatorname{abs}_{\tau}(x-y),\text{tol}).\end{split}\hskip-20.00003pt$ | | | Here, $\epsilon$ denotes the machine precision to ensure that the surrogates converge to the correct hard function as $\tau\to 0^{+}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison operators and differentiable logic", "weight": 1.0} -->

In the definition of $\operatorname{isclose}_{\tau}$, we use a standard tolerance $\text{tol}=\text{atol}+\text{rtol}\cdot\operatorname{abs}_{\tau}(y)$ with $\text{atol}>0$ and $\text{rtol}>0$ denoting the relative and absolute tolerance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison operators and differentiable logic", "weight": 1.0} -->

The output of our soft surrogates can be interpreted as the probability of the hard comparison being True. For the sake of simplicity, we refer to such a probability as a soft Boolean or, in short, a "SoftBool". This perspective has been studied extensively in the field of fuzzy logic. Given multiple SoftBools $p_{1},\ldots,p_{n}$, differentiable logic operators reduce to the manipulation of probabilities. By default, our framework implements the logical $\operatorname{all}$ operator as denoting the joint probability that independent Boolean events $p_{1},\ldots,p_{n}$ equate to True. Alternatively, we allow using the geometric mean providing advantageous numerical scaling for gradient computation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison operators and differentiable logic", "weight": 1.0} -->

Similarly, the $\operatorname{not}$ operator yields the probability that a Boolean event is False Other fuzzy logical operators are derived using the $\operatorname{all}$ and $\operatorname{not}$ operators | | $\displaystyle\begin{split}\operatorname{any}(p_{1},\ldots,p_{n})&\coloneqq\neg\operatorname{all}(\neg p_{1},\ldots,\neg p_{n}),\\ | | \(15\) | | | \operatorname{and}(p,q)&\coloneqq\operatorname{all}(p,q),\\ | | | | | \operatorname{or}(p,q)&\coloneqq\operatorname{any}(p,q),\\ | | | | | \operatorname{xor}(p,q)&\coloneqq\operatorname{or}\bigl(\operatorname{and}(p,\neg

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison operators and differentiable logic", "weight": 1.0} -->

q),\operatorname{and}(\neg p,q)\bigr).\end{split}$ | | | Similar to how normal Boolean variables can be used to select elements among two arrays, we can use a SoftBool variable $p_{i}$ to do a soft selection via the expectation In code, this is abstracted from the user via [⬇](data:text/plain;base64,c29mdF9jb25kID0gc2ouZ3JlYXRlcih4LCB5KSAjIFswLjA1IDAuNzMgMC45OF0KeiA9IHNqLndoZXJlKHNvZnRfY29uZCwgeCwgeSkgIyBbMC4zOSAwLjI3IDAuNjld){download=""} soft_cond = sj.greater(x, y) \# \[0.05 0.73 0.98\] z = sj.where(soft_cond, x, y) \# \[0.39 0.27 0.69\]

<!-- chunk {"id": "body-0028", "role": "body", "section": "Axiswise Operators", "weight": 1.0} -->

After discussing elementwise operators in the previous section, this section discusses and derives soft surrogates for axis-wise operators such as $\operatorname{argmax}$, $\operatorname{sort}$ or $\operatorname{argtopk}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Axiswise Operators", "weight": 1.0} -->

The simplest example of an axiswise operation is the $\operatorname{(arg)max}$ operator. The standard $\operatorname{argmax}$ operator returns an index $j\in\{0,\ldots,n-1\}$, and the $\operatorname{max}$ operator simply selects the corresponding element $x_{j}$. Another way to write this is as an inner product $x_{j}=\mathbf{e}_{j}\cdot\mathbf{x}$, where $\mathbf{e}_{j}$ is one at index $j$ and zero everywhere else. We can now relax the notion of an index as an indicator vector to a "SoftIndex" on the unit simplex In the case of the $\operatorname{argmax}$ operator, a simple relaxation that produces a SoftIndex is the softmax function (more accurately referred to as *softargmax*).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Axiswise Operators", "weight": 1.0} -->

The previous dot-product index-selection can now be interpreted as an expectation In code, our drop-in replacements read as: [⬇](data:text/plain;base64,eCA9IGpucC5hcnJheShbMC4xLCAwLjQsIDAuOF0pCgppZHggPSBqbnAuYXJnbWF4KHgpICMgMgp5ID0gamF4LmxheC5keW5hbWljX2luZGV4X2luX2RpbSh4LCBpZHgpICMgWzAuOF0KCnNvZnRfaWR4ID0gc2ouYXJnbWF4KHgpICMgWzAuMDA0IDAuMDQyIDAuOTUzXQp5ID0gc2ouZHluYW1pY19pbmRleF9pbl9kaW0oeCwgc29mdF9pZHgpICMgWzAuNzhd){download=""} idx = jnp.argmax(x) \# 2 y = jax.lax.dynamic_index_in_dim(x, idx) \# \[0.8\] soft_idx = sj.argmax(x) \# \[0.004 0.042 0.953\] y = sj.dynamic_index_in_dim(x, soft_idx) \# \[0.78\] We can further generalize this technique of using SoftIndices to sorting and ranking. To see this, we first note that sorting an array $\mathbf{x}\in\mathbb{R}^{n}$ can be viewed as multiplying it with the sorting permutation matrix Throughout, $\operatorname{sort}$ is in ascending order.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Axiswise Operators", "weight": 1.0} -->

The rows of $P^{\star}$ are indicator vectors, and the matrix multiplication can be interpreted as doing index selection in parallel. In this sense, the permutation matrix $P^{\star}$ can be interpreted as the generalized $\operatorname{argsort}$ operator, i. e., Similarly, the same matrix can be used for ranking, where rank 1 is assigned to the largest element, We can now relax the notion of a permutation matrix into a bistochastic matrix, the set of which is also called the Birkhoff polytope Note that in practice, for sorting or ranking, we only need $P_{\tau}$ to be a row- or column-stochastic matrix, respectively. The following two sections discuss how we can compute soft permutation matrices $P_{\tau}$ from $\mathbf{x}$, either resorting to regularized optimal transport (OT) or unit simplex projections. Finally, we will discuss an approach that directly relaxes the $\operatorname{sort}$ operator via projection onto the permutahedron without relaxing permutation matrices.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Axiswise Operators", "weight": 1.0} -->

In this version of the library, we deliberately choose to focus on deterministic approaches, and do not consider stochastic ones such as. Table 2 provides an overview on the various available methods and regularizations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimal Transport-based", "weight": 1.0} -->

The first family of algorithms is based on optimal transport. In general, optimal transport describes optimally moving probability mass from one distribution to another distribution while paying minimal cost. As described by Cuturi et al., regularized OT can be used to define soft (arg)sort operators. The general idea is to mimic a sorting-like behavior by defining two uniform distribution, one on the to-be-sorted input vector $\mathbf{x}\in\mathbb{R}^{n}$ and one on a set of increasing "anchor" points $\mathbf{y}\in\mathbb{R}^{n}$. The optimal transport cost matrix is then defined as the squared distance between input and anchor points, which means that probability mass from large values of $\mathbf{x}$ will be moved to large anchor points. As the anchor points are sorted, this creates a sorting behavior, which is illustrated in Figure 5.

<!-- chunk {"id": "body-0034", "role": "body", "section": "OT problem", "weight": 1.0} -->

We consider the case of an entropic regularizer $R(\Gamma)=\sum_{i,j}\Gamma_{ij}(\log\Gamma_{ij}-1)$, Euclidean regularizer $R(\Gamma)=\frac{1}{2}\sum_{i,j}\Gamma_{ij}^{2}$ and p-norm regularizer $R(\Gamma)=\frac{1}{p}\sum_{i,j}|\Gamma_{ij}|^{p}$. It is well known that the Euclidean regularizer has a sparsity-inducing effect on the gradients; see, e. g., SparseMax. As discussed by Sander et al. in the context of projections onto the permutahedron, the p-norm regularizer shares this property, but additionally allows for everywhere differentiable relaxations (Theorem 1. ‣ D.4 Smoothness of 𝑝-norm Regularized Projections ‣ Appendix D Extended Axiswise Operators ‣ SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients")).

<!-- chunk {"id": "body-0035", "role": "body", "section": "OT problem", "weight": 1.0} -->

Interestingly, for univariate inputs, the closed-form solutions of the entropic and Euclidean OT problem reduce to the corresponding sigmoidal functions used in our soft Heaviside relaxation, as shown in Section D.3.

<!-- chunk {"id": "body-0036", "role": "body", "section": "OT based operators", "weight": 1.0} -->

We set the source marginal to a uniform distribution $\mathbf{a}=\mathbf{1_{n}}/n$, and specifically for sorting and ranking, we follow Cuturi et al. by setting uniform $\mathbf{b}=\mathbf{1_{n}}/n$ and grid-like $\mathbf{y}=\tfrac{1}{n-1}[0,\ldots,n-1]^{\top}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "OT based operators", "weight": 1.0} -->

Moreover, we first standardize and then squash $\mathbf{x}$ with a sigmoid to the range $$. Although this is not strictly necessary, the use of $\mathbf{x}$ and $\mathbf{y}$ in the range $$ improves numerical stability and makes the softening parameter independent of the scale of $\mathbf{x}$. Then we have^22^2Note, that the multiplication of the soft permutation matrix with $\mathbf{x}$ has close ties to the gating-style definition of the soft $\operatorname{relu}$ function in Equation 10, see Section D.5 for details.

<!-- chunk {"id": "body-0038", "role": "body", "section": "OT based operators", "weight": 1.0} -->

To abstract the soft indices away from the user, we offer several replacements of utility functions for index selection that mirror the behavior of standard hard JAX and PyTorch index selection, e. g., [⬇](data:text/plain;base64,eCA9IGpucC5hcnJheShbMC4zLCAxLjAsIC0wLjVdKQoKaW5kID0gam5wLmFyZ3NvcnQoeCkgIyBbMiAwIDFdCnZhbCA9IGpucC50YWtlX2Fsb25nX2F4aXMoeCwgaW5kKSAjIFstMC41ICAwLjMgIDEuMF0KCnNvZnRfaW5kID0gc2ouYXJnc29ydCh4KQogICAgIyBbWzAuMDcgIDAuICAgIDAuOTMgXSwgWy4uLl0sIFsuLi5dXQp2YWwgPSBzai50YWtlX2Fsb25nX2F4aXMoeCwgc29mdF9pbmQpCiAgICAjIFstMC40NDQgIDAuMzEgICAwLjkzNl0=){download=""} ind = jnp.argsort(x) \# val = jnp.take_along_axis(x, ind) \# \[-0.5 0.3 1.0\] soft_ind = sj.argsort(x) val = sj.take_along_axis(x, soft_ind) In principle sorting is enough to define many other operators like $\operatorname{max}$, $\operatorname{median}$ and $\operatorname{top-k}$, via appropriate selection and combination of the soft-sorted values. However, the dimensionality of the cost matrix for an $n$-dimensional vector $\mathbf{x}$ is $n\times n$, which can lead to large memory requirements.

<!-- chunk {"id": "body-0039", "role": "body", "section": "OT based operators", "weight": 1.0} -->

Fortunately, it is possible to strongly reduce the dimensionality, by transporting multiple elements of $\mathbf{x}$ which we are not interested in (e. g., the bottom $n-k$ elements in $\operatorname{top-k}$) to a shared dummy anchor point, thereby reducing the number of anchors.

<!-- chunk {"id": "body-0040", "role": "body", "section": "OT based operators", "weight": 1.0} -->

For q-quantiles we slightly vary the approach of Cuturi et al. by setting $k=\lfloor q(n-1)\rfloor$, $\mathbf{b}=[\tfrac{k}{n},\tfrac{1}{n},\tfrac{1}{n},\tfrac{n-k-2}{n}]^{\top},\mathbf{y}=\tfrac{1}{3}^{\top}$, then we can compute the lower $\downarrow$ and upper $\uparrow$ q-quantiles via the second and third entry of $P_{\tau}^{\star}$, i. e., Various quantile definitions can be recovered by appropriately combining the upper and lower quantiles (e. g., interpolating or using midpoint). We also trivially get the median by evaluating the quantile function with $q=0.5$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Approximate OT: Unit simplex projection-based", "weight": 1.0} -->

The relaxations based on OT have many desirable properties such as smoothness in the case of an entropic regularizer. However, solving the OT problem can be memory- and compute-intensive in practice. We now describe different soft surrogates based on unit-simplex projections, which have a closed-form solution. The downside is that these relaxations typically still allow for some non-differentiabilities, e. g., when ties occur. However, in practice they often perform well and are therefore selected as the default method of choice.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Unit simplex projection", "weight": 1.0} -->

The regularized linear program over the simplex, see Equation 17, is defined as We consider Euclidean regularization $R(\mathbf{p})=\tfrac{1}{2}\|\mathbf{p}\|_{2}^{2}$, which leads to a Euclidean projection onto the unit simplex and entropic regularization $R(\mathbf{p})=\sum_{j}p_{j}\log p_{j}$, leading to a closed-form solution via the softmax ${\exp(\mathbf{x}/\tau)}/{\sum_{j}\exp(x_{j}/\tau)}$. Finally, we consider p-norm regularization $R(\mathbf{p})=\tfrac{1}{p}\sum_{j}|p_{j}|^{p}$, which leads to a Bregman projection onto the unit simplex.

<!-- chunk {"id": "body-0043", "role": "body", "section": "SoftSort", "weight": 1.0} -->

Entropy-regularized OT can be solved efficiently via the Sinkhorn algorithm. In the case of OT for sorting in Equation 26, where both marginals $\mathbf{a}$ and $\mathbf{b}$ are uniform, the Sinkhorn algorithm boils down to alternating row and column softmax-normalization of the cost matrix. SoftSort can be seen as approximating this algorithm by reducing it to a single row-wise softmax normalization via a clever initialization of the anchors. This corresponds to the entropic regularizer in Equation 33, which we generalize to other regularizers, leading to new variants of SoftSort.

<!-- chunk {"id": "body-0044", "role": "body", "section": "SoftSort", "weight": 1.0} -->

To define the anchors, instead of using a uniform grid over the interval $$ as in Equation 26, the anchors are constructed by first applying the hard operator to $x$, e. g., $\mathbf{y}=\operatorname{sort}(\mathbf{x})$. The cost matrix is the absolute difference between elements of $\mathbf{x}$ and $\mathbf{y}$, which will intuitively assign a low transportation cost between elements of $\operatorname{sort}(\mathbf{x})$ that are close to $\mathbf{x}$. For the $\operatorname{sort}$ operator, this leads to The projection is applied row-wise. The computation is illustrated in Figure 6. We showcase the output and partial derivatives of the soft sort operation for two different regularizers over a range of $\tau$ in Figure 7.

<!-- chunk {"id": "body-0045", "role": "body", "section": "SoftSort", "weight": 1.0} -->

Note that the computation is independent over rows, we can therefore independently get soft operators for each of the sorted elements, which trivially gives us a soft ($\operatorname{arg}$)$\operatorname{topk}$/ $\operatorname{quantile}$/$\operatorname{max}$ operator, by replacing the $\operatorname{sort}$ function in Equation 34 with the corresponding operator. Interestingly, the $\operatorname{argmax}$ operator reduces to $P_{\tau}(\mathbf{x})$, which for entropic regularization is simply softmax, thereby recovering the example used in the beginning of the chapter. For Euclidean regularization, it recovers the SparseMax operator.

<!-- chunk {"id": "body-0046", "role": "body", "section": "SoftSort", "weight": 1.0} -->

Finally, we can also define a novel SoftSort-style $\operatorname{rank}$ operator. For this we observe that $\Pi_{\tau}$ is applied independently to each row of the cost matrix, so the resulting matrix is only row-stochastic and the corresponding argsort operator cannot be transposed to define a soft ranking as we did in the OT case. Instead, we transpose the cost matrix before applying the unit-simplex projection, which gives distributions over rank indices as Note, that all SoftSort-based surrogates are not fully smooth, as the computation involves the hard $\operatorname{sort}$ operator (non-smooth at ties) and the absolute value function (non-smooth at zero). For this reason, the NeuralSort-based surrogates (which are fully smooth when combined with our soft $\operatorname{abs}$) are selected as the default method for $\operatorname{sort}$, $\operatorname{rank}$, $\operatorname{quantile}$, and $\operatorname{median}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "SoftSort", "weight": 1.0} -->

However, for $\operatorname{argmax}$, $\operatorname{argmin}$, $\operatorname{max}$, and $\operatorname{min}$, the SoftSort-based method is the default, since it requires only a single simplex projection, giving $O(n)$ complexity compared to NeuralSort's $O(n^{2})$, and in smooth mode it reduces to the standard softmax, the canonical soft argmax.

<!-- chunk {"id": "body-0048", "role": "body", "section": "NeuralSort", "weight": 1.0} -->

NeuralSort also utilizes unit-simplex projections but originates in a soft relaxation of the $\operatorname{median}$ operator. Defining the matrix of soft absolute differences $A_{\mathbf{x}}^{\tau}\in\mathbb{R}^{n\times n}$ using our soft $\operatorname{abs}$ from Equation 8 as we have that $A_{\mathbf{x}}^{\tau}\mathbf{1}_{n}$ is the vector of sums of soft absolute differences between each element and all other elements.^33^3The original NeuralSort paper uses the hard $|x_{i}-x_{j}|$, which introduces gradient discontinuities at ties. By using our soft $\operatorname{abs}$, we obtain fully smooth NeuralSort surrogates.

<!-- chunk {"id": "body-0049", "role": "body", "section": "NeuralSort", "weight": 1.0} -->

It is well-known that the median minimizes this sum for $\tau\rightarrow 0^{+}$, therefore we have By adding a regularizer similar to SoftSort Equation 33, we get a soft surrogate NeuralSort generalizes this idea to the sorting operator, by setting For $\tau\rightarrow 0^{+}$ this recovers the true argsort operator. Intuitively, the vector that is projected is a linear combination of the original vector $\mathbf{x}$ and the vector of sums of soft absolute differences, which, when projected onto the unit simplex individually, give an $\operatorname{argmax}$ and an $\operatorname{argmedian}$ relaxation, respectively.

<!-- chunk {"id": "body-0050", "role": "body", "section": "NeuralSort", "weight": 1.0} -->

This also directly provides relaxations for the $\operatorname{argmax}$, $\operatorname{argmin}$, $\operatorname{argquantile}$^↑^ and $\operatorname{argquantile}$^↓^ operators by computing only the corresponding elements of the soft sorted array, i. e., with $c^{\uparrow}=n\!-\!1-2\lceil q(n\!-\!1)\rceil$ and $c^{\downarrow}=n\!-\!1-2\lfloor q(n\!-\!1)\rfloor$, Note that the original paper only treats the smooth (entropic) projection; we extend it to c0, c1, and c2 regularizers. As with SoftSort, the NeuralSort argsort matrix is only row-stochastic.

<!-- chunk {"id": "body-0051", "role": "body", "section": "NeuralSort", "weight": 1.0} -->

To obtain soft ranks, we normalize each column to sum to one and compute $\operatorname{rank}_{\tau}(\mathbf{x})=\widetilde{P}^{\top}[n,\ldots,1]^{\top}$, mirroring Equation 26.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Permutahedron projection-based", "weight": 1.0} -->

For sorting and ranking, both OT-based and unit-simplex-projection-based approaches involve computations with the $n\times n$ cost matrix. In SoftJAX, we avoid materializing this matrix by processing rows in chunks via lax.scan, reducing memory from $O(n^{2})$ to $O(n)$ while also yielding $O$ XLA compilation time. Nevertheless, for large $n$, the $O(n^{2})$ time complexity remains a bottleneck. Blondel et al.; Sander et al. resolve this issue by directly softening the value-space operators, e. g., $\operatorname{sort}$ instead of $\operatorname{argsort}$. This is achieved by interpreting these operators as projections onto the permutahedron, the convex hull of permutations of $\mathbf{z}$, i.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Permutahedron projection-based", "weight": 1.0} -->

e., Here, $\Sigma$ is the set of permutation matrices, see Equation 19. The Euclidean projection of a vector $\mathbf{y}\in\mathbb{R}^{n}$ onto the permutahedron of another vector $\mathbf{z}\in\mathbb{R}^{n}$ is given by Blondel et al. also propose a variant that uses an entropic regularizer by optimizing over exponentiated inputs and taking the log, i. e.,

<!-- chunk {"id": "body-0054", "role": "body", "section": "FastSoftSort", "weight": 1.0} -->

Intuitively, FastSoftSort now projects the sorted ranks onto the permutahedron of the input $\mathbf{x}$, which will select the permutation of $\mathbf{x}$ that is closest to being sorted. In the same way, projecting the (negative) $\mathbf{x}$ onto the permutahedron of the possible ranks selects the ranks that follow the ordering of $\mathbf{x}$. This gives the surrogate operators Other operators like top-k, quantile, median or max can be computed by first running soft sorting, and then selecting the appropriate values.

<!-- chunk {"id": "body-0055", "role": "body", "section": "FastSoftSort", "weight": 1.0} -->

Crucially, Blondel et al. derive an algorithm based on isotonic optimization which solves the projection onto the permutahedron in $O(n\log n)$. This is much faster than the runtime of Sinkhorn which is $O(Tn^{2})$, where $T$ is the number of Sinkhorn iterations. However, note that this approach does not allow for an $\operatorname{argsort}$ or $\operatorname{argrank}$ operator.

<!-- chunk {"id": "body-0056", "role": "body", "section": "SmoothSort", "weight": 1.0} -->

In OT and unit simplex projection-based approaches, entropic regularization typically leads to dense Jacobians, whereas Euclidean regularization promotes sparsity, see e. g.,. However, in FastSoftSort this is not the case: While Euclidean regularization behaves as usual by promoting sparsity, the entropic regularization behaves very similarly to the Euclidean case by promoting sparsity, as also discussed by Blondel et al..

<!-- chunk {"id": "body-0057", "role": "body", "section": "SmoothSort", "weight": 1.0} -->

Therefore, we propose a new variant of this surrogate family by adding entropic regularization to a dual formulation of the permutahedron projection; see Section D.6 for details. This leads to a surrogate that behaves more like the entropic regularizer in the OT setting, which yields dense Jacobians. Moreover, by replacing the hard order-statistic bounds in the permutahedron LP with smooth log-sum-exp relaxations (Section D.6), this variant is $\mathcal{C}^{\infty}$ differentiable, unlike the other FastSoftSort variants which are at most $\mathcal{C}^{2}$. Unfortunately, we cannot use the same fast PAV algorithm in this case, because the smooth bounds require $O(n^{2})$ preprocessing and the LP is solved via L-BFGS. However, compared to entropy-regularized OT, the $O(n^{2})$ cost is paid only once (for the bounds), not per iteration, and we do not need to materialize an $n\times n$ matrix.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Sorting network-based", "weight": 1.0} -->

An alternative approach that avoids both the $O(n^{2})$ pairwise cost matrix and iterative optimization is to use a differentiable sorting network. Following Petersen et al., who propose replacing the hard compare-and-swap operations in a bitonic sorting network with soft comparisons based on a logistic sigmoid, we implement a bitonic sorting network using our soft Heaviside function $\operatorname{H}_{\tau}$ (Equations 5 and 6) for soft swapping, i. e., In smooth mode, $\operatorname{H}_{\tau}$ is the logistic sigmoid, directly recovering the method of Petersen et al., while c0, c1, and c2 modes yield new sorting network variants with the corresponding smoothness guarantees. Following Petersen et al., we obtain soft permutation matrices by tracking an $n\times n$ matrix $P$ (initialized to the identity) through the network.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Sorting network-based", "weight": 1.0} -->

At each compare-and-swap step, the rows of $P$ corresponding to the two compared positions are mixed using the weights $\sigma$ and $1-\sigma$, hence $\operatorname{sort}(\mathbf{x})=P\mathbf{x}$. Unlike FastSoftSort, sorting networks can therefore produce both sorted values and soft permutation matrices, enabling $\operatorname{argsort}$ and $\operatorname{argmax}$ in addition to $\operatorname{sort}$, $\operatorname{max}$, $\operatorname{min}$, $\operatorname{quantile}$, $\operatorname{median}$, and $\operatorname{top_k}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Benchmarks & Case Study", "weight": 1.0} -->

In order to be useful for machine learning practitioners, softened functions and their gradients must be both fast to compute and memory efficient. SoftJAX allows us to easily compare these aspects across different methods within a unified framework. Figure 8 shows the computation time and peak memory of sj.sort for different input sizes and methods (smooth mode) on an Nvidia RTX 3060 GPU. The sorting network is the fastest soft method at \\qty1.0\\milli for $n=4096$ (only ${\sim}3.8\times$ the hard baseline), followed by SoftSort (\\qty16\\milli) and NeuralSort (\\qty37\\milli). FastSoftSort is the most memory-efficient method, scaling roughly linearly (\\qty420\\kilo at $n=4096$) since it avoids materializing a permutation matrix. Our novel method SmoothSort and the OT-based surrogate are the slowest out of the testsed methods. Extensive benchmarking results on all methods and modes for a variety of axis-wise functions are included in Appendix E.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Benchmarks & Case Study", "weight": 1.0} -->

Additionally, we include a case study which demonstrates the ease of using SoftJAX for softening a subroutine which is commonly used in collision detection, see Appendix B for details.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Standard tensor libraries with GPU acceleration and automatic differentiation have enabled differentiable optimization at scale in ML research. For many problems in ML and other fields, discrete primitives are needed, but result in uninformative gradients. Differentiable alternatives are scattered across papers, slowing progress and adoption. This work introduces SoftJAX and SoftTorch: feature-complete, unified and extensible libraries for soft relaxations of hard operators with principled straight-through estimation (STE).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We systematically derive differentiable surrogates for elementwise discrete operators from smooth relaxation of the Heaviside step function. Our framework also provides a broad set of axiswise differentiable discrete operators including $\operatorname{argsort}$, $\operatorname{argquantile}$, and $\operatorname{argtop_k}$ -- implemented via state-of-the-art algorithms based on optimal transport and simplex/permutahedron projections and derive index-selection primitives (e.g., $\operatorname{take_along_axis}$, $\operatorname{choose}$) for end-to-end use. Through this standardization, this work derives a broad range of differentiable operators for which an implementation is currently not easily available (see Table 2).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Overall, the framework consolidates core components for *soft differentiable programming* into a single, well-tested, feature-complete library, improving reproducibility and lowering the barrier to widespread use of soft differentiable programming in practice.
