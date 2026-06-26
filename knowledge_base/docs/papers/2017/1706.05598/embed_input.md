<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Optimization Landscape of Tensor Decompositions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Non-convex optimization with local search heuristics has been widely used in machine learning, achieving many state-of-art results. It becomes increasingly important to understand why they can work for these NP-hard problems on typical data. The landscape of many objective functions in learning has been conjectured to have the geometric property that "all local optima are (approximately) global optima", and thus they can be solved efficiently by local search algorithms. However, establishing such property can be very difficult. In this paper, we analyze the optimization landscape of the random over-complete tensor decomposition problem, which has many applications in unsupervised learning, especially in learning latent variable models. In practice, it can be efficiently solved by gradient ascent on a non-convex objective. We show that for any small constant epsilon > 0, among the set of points with function values (1+epsilon)-factor larger than the expectation of the function, all the local maxima are approximate global maxima. Previously, the best-known result only characterizes the geometry in small neighborhoods around the true components. Our result implies that even with an initialization that is barely better than the random guess, the gradient ascent algorithm is guaranteed to solve this problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our main technique uses Kac-Rice formula and random matrix theory. To our best knowledge, this is the first time when Kac-Rice formula is successfully applied to counting the number of local minima of a highly-structured random polynomial with dependent coefficients.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Non-convex optimization is the dominating algorithmic technique behind many state-of-art results in machine learning, computer vision, natural language processing and reinforcement learning. Local search algorithms through stochastic gradient methods are simple, scalable and easy to implement. Surprisingly, they also return high-quality solutions for practical problems like training deep neural networks, which are NP-hard in the worst case. It has been conjectured \[DPG^+^14, CHM^+^15\] that on typical data, the landscape of the training objectives has the nice geometric property that all local minima are (approximate) global minima. Such property assures the local search algorithms to converge to global minima. However, establishing it for concrete problems can be challenging.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite recent progress on understanding the optimization landscape of various machine learning problems (see and references therein), a comprehensive answer remains elusive. Moreover, all previous techniques fundamentally rely on the spectral structure of the problems. For example, allows us to pin down the set of the critical points (points with vanishing gradients) as approximate eigenvectors of some matrix. Among these eigenvectors we can further identify all the local minima. The heavy dependency on linear algebraic structure limits the generalization to problems with non-linearity (like neural networks).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Towards developing techniques beyond linear algebra, in this work, we investigate the optimization landscape of tensor decomposition problems. This is a clean non-convex optimization problem whose optimization landscape cannot be analyzed by the previous approach. It also connects to the training of neural networks with many shared properties. For example, in comparison with the matrix case where all the global optima reside on a (connected) Grassmannian manifold, for both tensors and neural networks all the global optima are isolated from each other.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides the technical motivations above, tensor decomposition itself is also the key algorithmic tool for learning many latent variable models, mixture of Gaussians, hidden Markov models, dictionary learning \[ AFH^+^12, \], just to name a few. In practice, local search heuristics such as alternating least squares, gradient descent and power method are popular and successful.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Concretely, we consider decomposing a random 4-th order tensor $T$ of the rank $n$ of the following form, We are mainly interested in the over-complete regime where $n \gg d$. This setting is particularly challenging, but it is crucial for unsupervised learning applications where the hidden representations have higher dimension than the data. Previous algorithmic results either require access to high order tensors, or use complicated techniques such as FOOBI or sum-of-squares relaxation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the worst case, most tensor problems are NP-hard \[Hås90, \]. Therefore we work in the average case where vectors $a_{i} \in {\mathbb{R}}^{d}$ are assumed to be drawn i.i.d from Gaussian distribution $\mathcal{N}{(0,I)}$. We call $a_{i}$'s the components of the tensor. We are given the entries of tensor $T$ and our goal is to recover the components $a_{1},\ldots,a_{n}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will analyze the following popular non-convex objective, It is known that for $n \ll d^{2}$, the global maxima of $f$ is close to one of ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$. Previously, Ge et al. show that for the orthogonal case where $n \leq d$ and all the $a_{i}$'s are orthogonal, objective function $f{(\cdot)}$ have only $2n$ local maxima that are approximately ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$. However, the technique heavily uses the orthogonality of the components and is not generalizable to over-complete case.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically, projected gradient ascent and power methods find one of the components $a_{i}$'s even if $n$ is significantly larger than $d$. The local geometry for the over-complete case around the true components is known: in a small neighborhood of each of $\pm {\frac{1}{\sqrt{d}}a_{i}}$'s, there is a unique local maximum. Algebraic geometry techniques can show that $f{( \cdot )}$ has an exponential number of other critical points, while these techniques seem difficult to extend to the characterization of local maxima. It remains a major open question whether there are any other spurious local maxima that gradient ascent can potentially converge to.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Main results", "weight": 1.0} -->

We show that there are no spurious local maxima in a large superlevel set that contains all the points with function values slightly larger than that of the random initialization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our techniques", "weight": 1.0} -->

The proof of Theorem 1.1 uses Kac-Rice formula (see, e.g., ), which is based on a counting argument. To build up the intuition, we tentatively view the unit sphere as a collection of discrete points, then for each point $x$ one can compute the probability (with respect to the randomness of the function) that $x$ is a local maximum. Adding up all these probabilities will give us the expected number of local maxima. In continuous space, such counting argument has to be more delicate since the local geometry needs to be taken into account. This is formalized by Kac-Rice formula (see Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our techniques", "weight": 1.0} -->

However, Kac-Rice formula only gives a closed form expression that involves the integration of the expectation of some complicated random variable. It's often very challenging to simplify the expression to obtain interpretable results. Before our work, Auffinger et al. \[AAČ13, AA^+^13\] have successfully applied Kac-Rice formula to characterize the landscape of polynomials with random Gaussian coefficients. The exact expectation of the number of local minima can be computed there, because the Hessian of a random polynomial is a Gaussian orthogonal ensemble, whose eigenvalue distribution is well-understood with closed form expression.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our techniques", "weight": 1.0} -->

Our technical contribution here is successfully applying Kac-Rice formula to structured random non-convex functions where the formula cannot be exactly evaluated. The Hessian and gradients of $f{( \cdot )}$ have much more complicated distributions compared to the Gaussian orthogonal ensemble. As a result, the Kac-Rice formula is impossible to be evaluated exactly. We instead cut the space ${\mathbb{R}}^{d}$ into regions and use different techniques to estimate the number of local maxima. See a proof overview in Section 3. We believe our techniques can be extended to 3rd order tensors and can shed light on the analysis of other non-convex problems with structured randomness.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Organization", "weight": 1.0} -->

In Section 2 we introduce preliminaries regarding manifold optimization and Kac-Rice formula. We give a detailed explanation of our proof strategy in Section 3. We fill in the technical details in the later sections: in Section 4 we show that there is no local maximum that is uncorrelated with any of the true components. We compliment that by a local analysis in Section 5 that shows there are exactly $2n$ local optima around the true components.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations and Preliminaries", "weight": 1.0} -->

Let $u \odot v$ denote the Hadamard product between vectors $u$ and $v$. Let $u^{\odot s}$ denote $u \odot \cdots \odot u$ where $u$ appears $k$ times. Let $A \otimes B$ denote the Kronecker product of $A$ and $B$. Let $\parallel \cdot \parallel$ denote the spectral norm of a matrix or the Euclidean norm of a vector. Let ${\parallel \cdot \parallel}_{F}$ denote the Frobenius norm of a matrix or a tensor.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations and Preliminaries", "weight": 1.0} -->

We write $A \lesssim B$ if there exists a universal constant $C$ such that $A \leq {CB}$. We define $\gtrsim$ similarly. Unless explicitly stated otherwise, $O{( \cdot )}$-notation hides absolute multiplicative constants. Concretely, every occurrence of the notation $O{(x)}$ is a placeholder for some function $f{(x)}$ that satisfies ${{\forall x} \in {\mathbb{R}}},{{|{f{(x)}}|} \leq {C{|x|}}}$ for some absolute constant $C > 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gradient, Hessian, and local maxima on manifold", "weight": 1.0} -->

We have a constrained optimization problem over the unit sphere $S^{d - 1}$, which is a smooth manifold. Thus we define the local maxima with respect to the manifold. It's known that projected gradient descent for $S^{d - 1}$ behaves pretty much the same on the manifold as in the usual unconstrained setting. In Section A we give a brief introduction to manifold optimization, and the definition of gradient and Hessian. We refer the readers to the book for more backgrounds. Here we use $\text{grad~}f$ and $\text{Hess~}f$ to denote the gradient and the Hessian of $f$ on the manifold $S^{d - 1}$. We compute them in the following claim.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Claim 2.1", "weight": 1.0} -->

A local maximum of a function $f$ on the manifold $S^{d - 1}$ satisfies ${\text{grad~}f{(x)}} = 0$, and ${\text{Hess~}f{(x)}} \preceq 0$. Let $\mathcal{M}_{f}$ be the set of all local maxima,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Kac-Rice formula", "weight": 1.0} -->

Suppose we take $P = {\nabla f}$ and $Q = {\nabla^{2}f}$, and let $\mathcal{B}$ be the set of negative semidefinite matrices, then the set of points that satisfies ${P{(x)}} = 0$ and $Q \in \mathcal{B}$ is the set of all local maxima $\mathcal{M}_{f}$. Moreover, for any set $Z \subset S^{d - 1}$, we can also augment $Q$ by $Q = {\lbrack{\nabla^{2}f},x\rbrack}$ and choose $\mathcal{B} = {{\{ A:{A \preceq 0}\}} \otimes Z}$. With this choice of $P,Q$, Kac-Rice formula can count the number of local maxima inside the region $Z$. For simplicity, we will only introduce Kac-Rice formula for this setting.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Kac-Rice formula", "weight": 1.0} -->

We refer the readers to \[, Chapter 11&12\] for more backgrounds.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Formula for the number of local maxima", "weight": 1.0} -->

In this subsection, we give a concrete formula for the number of local maxima of our objective function (1.1) inside the superlevel set $L$ (defined in equation (1.2)). Taking $Z = L$ in Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions"), it boils down to estimating the quantity on the right hand side of (2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")). We remark that for the particular function $f$ as defined in (1.1) and $Z = L$, the integrand in (2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")) doesn't depend on the choice of $x$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Local vs. global analysis", "weight": 1.0} -->

The key idea to proceed is to divide the superlevel set $L_{1}$ into two subsets Here $\delta$ is a sufficiently small universal constant that is to be chosen later. We also note that $L_{2}^{c} \subset L_{1}$ and hence $L_{1} = {{({L_{1} \cap L_{2}})} \cup L_{2}^{c}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Local vs. global analysis", "weight": 1.0} -->

Intuitively, the set $L_{1} \cap L_{2}$ contains those points that do not have large correlation with any of the $a_{i}$'s; the compliment $L_{2}^{c}$ is the union of the neighborhoods around each of the desired vector ${\frac{1}{\sqrt{d}}a_{1}},\ldots,{\frac{1}{\sqrt{d}}a_{n}}$. We will refer to the first subset $L_{1} \cap L_{2}$ as the global region, and refer to the $L_{2}^{c}$ as the local region.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Local vs. global analysis", "weight": 1.0} -->

We will compute the number of local maxima in sets $L_{1} \cap L_{2}$ and $L_{2}^{c}$ separately using different techniques. We will show that with high probability $L_{1} \cap L_{2}$ contains zero local maxima using Kac-Rice formula (see Theorem 3.2). Then, we show that $L_{2}^{c}$ contains exactly $2n$ local maxima (see Theorem 3.3) using a different and more direct approach.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Global analysis", "weight": 1.0} -->

The key benefit of have such division to local and global regions is that for the global region, we can avoid evaluating the value of the RHS of the Kac-Rice formula. Instead, we only need to have an estimate: Note that the number of local optima in $L_{1} \cap L_{2}$, namely $|{\mathcal{M}_{f} \cap L_{1} \cap L_{2}}|$, is an integer nonnegative random variable. Thus, if we can show its expectation $\mathbb{E}\left\lbrack {|{\mathcal{M}_{f} \cap L_{1} \cap L_{2}}|} \right\rbrack$ is much smaller than $1$, then Markov's inequality implies that with high probability, the number of local maxima will be exactly zero. Concretely, we will use Lemma 2.2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Global analysis", "weight": 1.0} -->

‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions") with $Z = {L_{1} \cap L_{2}}$, and then estimate the resulting integral using various techniques in random matrix theory. It remains quite challenging even if we are only shooting for an estimate. see Theorem 3.2 for the exact statement and Section 3.1 for an overview of the analysis.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Local analysis", "weight": 1.0} -->

In the local region $L_{2}^{c}$, that is, the neighborhoods of $a_{1},\ldots,a_{n}$, we will show there are exactly $2n$ local maxima. As argued above, it's almost impossible to get exact numbers out of the Kac-Rice formula since it's often hard to compute the complicated integral. Moreover, Kac-Rice formula only gives the expected number but not high probability bounds. However, here the observation is that the local maxima (and critical points) in the local region are well-structured. Thus, instead, we show that in these local regions, the gradient and Hessian of a point $x$ are dominated by the terms corresponding to components $\{ a_{i}\}$'s that are highly correlated with $x$. The number of such terms cannot be very large (by restricted isometry property, see Section B.5).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Local analysis", "weight": 1.0} -->

As a result, we can characterize the possible local maxima explicitly, and eventually show there is exactly one local maximum in each of the local neighborhoods around $\{{\pm {\frac{1}{\sqrt{d}}a_{i}}}\}$'s.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Concentration properties of $a_{i}$'s", "weight": 1.0} -->

Before stating the formal results regarding the local and global analysis, we have the following technical preparation. Since $a_{i}$'s are chosen at random, with small probability the tensor $T$ will behave very differently from the average instances. The optimization problem for such irregular tensors may have much more local maxima. To avoid these we will restrict our attention to the following event $G_{0}$, which occurs with high probability (over the randomness of $a_{i}$'s): Here $\delta$ is a small enough universal constant. Event $G_{0}$ summarizes common properties of the vectors $a_{i}$'s that we frequently use in the technical sections. Equation (3.4) is the restricted isometry property (see Section B.5) that ensures the $a_{i}$'s are not adversarially correlated with each other. Equation (3.5) lowerbounds the high order moments of $a_{i}$'s.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Concentration properties of $a_{i}$'s", "weight": 1.0} -->

Equation (3.6) bounds the singular values of the matrix $\sum_{i = 1}^{n}{a_{i}a_{i}^{\top}}$. These conditions will be useful in the later technical sections.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Concentration properties of $a_{i}$'s", "weight": 1.0} -->

Next, we formalize the intuition above as the two theorems below. Theorem 3.2 states there is no local maximum in $L_{1} \cap L_{2}$, whereas Theorem 3.3 concludes that there are exactly $2n$ local maxima in $L_{1} \cap L_{2}^{c}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Estimating the Kac-Rice formula for the global region", "weight": 1.0} -->

The general plan to prove Theorem 3.2 is to use random matrix theory to estimate the RHS of the Kac-Rice formula. We begin by applying Kac-Rice formula to our situation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Estimating the Kac-Rice formula for the global region", "weight": 1.0} -->

Thus it suffice to control $\mathbb{E}\left\lbrack \left| {\mathcal{M}_{f} \cap L_{1} \cap L_{2} \cap L_{G}} \right| \right\rbrack$. We will use the Kac-Rice formula (Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")) with the set $Z = {\mathcal{M}_{f} \cap L_{1} \cap L_{2} \cap L_{G}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Applying Kac-Rice formula", "weight": 1.0} -->

We see that the equations above correspond to equation (3.4), (3.5) and (3.6) and event $\mathbf{1}{(E_{0})}$ corresponds to the event $x \in L_{G}$. Similarly, the following event $E_{1}$ corresponds to $x \in L_{1}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Applying Kac-Rice formula", "weight": 1.0} -->

Events $E_{2}$ and $E_{2}'$ correspond to the events that $x \in L_{2}$. We separate them out to reflect that $E_{2}$ and $E_{2}'$ depends the randomness of $\alpha_{i}$'s and $b_{i}$'s respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Applying Kac-Rice formula", "weight": 1.0} -->

Using Kac-Rice formula (Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions") with $Z = {L_{1} \cap L_{2} \cap L_{G}}$), we conclude that Next, towards proving Theorem 3.2 we will estimate the RHS of the equation (3.10) using various techniques.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conditioning on $\\alpha$", "weight": 1.0} -->

We observe that the distributions of the gradient $g$ and Hessian $M$ are fairly complicated. In particular, we need to deal with the interactions of $\alpha_{i}$'s (the components along $x$) and $b_{i}$'s (the components in the orthogonal subspace of $x$). Therefore, we use the law of total expectation to first condition on $\alpha$ and take expectation over the randomness of $b_{i}$'s, and then take expectation over $\alpha_{i}$'s. Here below the inner expectation of RHS of (3.11) is with respect to the randomness of $b_{i}$'s and the outer one is with respect to $\alpha_{i}$'s.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Question I: how to control $\\det{{(M)}\\mathbf{1}{({M \\succeq 0})}}$?", "weight": 1.0} -->

Recall that $M = {\left. \parallel\alpha\parallel \right._{4}^{4} - {3{\sum{\alpha_{i}^{2}b_{i}b_{i}^{\top}}}}}$, which is a generalized Wishart matrix whose eigenvalue distribution has no (known) analytical expression. The determinant itself by definition is a high-degree polynomial over the entries, and in our case, a complicated polynomial over the random variables $\alpha_{i}$'s and vectors $b_{i}$'s. We also need to properly exploit the presence of the indicator function $\mathbf{1}{({M \succeq 0})}$, since otherwise, the desired statement will not be true -- the function $f$ has an exponential number of critical points.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Question I: how to control $\\det{{(M)}\\mathbf{1}{({M \\succeq 0})}}$?", "weight": 1.0} -->

Fortunately, in most of the cases, we can use the following simple claim that bounds the determinant from above by the trace. The inequality is close to being tight when all the eigenvalues of $M$ are similar to each other. More importantly, it uses naturally the indicator function $\mathbf{1}{({M \succeq 0})}$! Later we will see how to strengthen it when it's far from tight.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Claim 3.7", "weight": 1.0} -->

For any $p \times p$ symmetric matrix $V$, we have, The claim is a direct consequence of AM-GM inequality.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Easy case when all $\\alpha_{i}$'s are small", "weight": 1.0} -->

To find a tight bound for the RHS of (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")), intuitively we can consider two events: the event $F_{0}$ when all of the $\alpha_{i}$'s are close to constant (defined rigorously later in equation (3.19)) and the complementary event $F_{0}^{c}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Easy case when all $\\alpha_{i}$'s are small", "weight": 1.0} -->

We claim that $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{0})}} \right\rbrack$ can be bounded by $2^{- {d/2}}$. Then we will argue that it's difficult to get an upperbound for $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{0}^{c})}} \right\rbrack$ that is smaller than 1 using the RHS of equation (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Easy case when all $\\alpha_{i}$'s are small", "weight": 1.0} -->

It turns out in most of the calculations below, we can safely ignore the contribution of the term ${3{\parallel\alpha\parallel}_{8}^{8}}/{\|\alpha\|}_{6}^{6}$. For notation convenience, let ${Q{(\cdot)}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be defined as: When conditioned on the event $F_{0}$, roughly speaking, random variable ${Q{(\alpha)}} = {{\|\alpha\|}_{4}^{4} - {3{\|\alpha\|}^{2}}}$ behaves like a Gaussian distribution with variance $\Theta{(n)}$, since $Q{(\alpha)}$ is a sum of independent random variables with constant variances.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Easy case when all $\\alpha_{i}$'s are small", "weight": 1.0} -->

Then for sufficiently large constant $\gamma$, Moreover, recall that when the event $E_{0}$ happens, we have that $\left. \parallel\alpha\parallel \right._{6}^{6} \geq {15{({1 - \delta})}n}$. Therefore putting all these bounds together into equation (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) with the indicator $\mathbf{1}{(F_{0})}$, and using the fact that ${\text{Vol}{(S^{d - 1})}} = \frac{\pi^{d/2}}{\Gamma{({{d/2} + 1})}}$, we can obtain the target bound,

<!-- chunk {"id": "body-0047", "role": "body", "section": "The heavy tail problem", "weight": 1.0} -->

Next we explain why it's difficult to achieve a good bound from using RHS (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")). The critical issue is that the random variable $Q{(\alpha)}$ has very heavy tail, and exponentially small probability cannot be ignored. To see this, we first claim that $Q{(\alpha)}$ has a tail distribution that roughly behaves like Taking $t = d^{2}$, then the contribution of the tail to the expectation of $Q{(\alpha)}^{d}$ is at least ${{\Pr\left\lbrack {{Q{(\alpha)}} \geq t} \right\rbrack} \cdot t^{d}} \approx d^{2d}$, which is much larger than what we obtained (equation (3.18)) in the case when all $\alpha_{i}$'s are small.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The heavy tail problem", "weight": 1.0} -->

The obvious fix is to consider $Q{(\alpha)}^{d}{({\parallel\alpha\parallel}_{6}^{6})}^{- {d/2}}$ together (instead of separately). For example, we will use Cauchy-Schwarz inequality to obtain that ${Q{(\alpha)}^{d}{({\parallel\alpha\parallel}_{6}^{6})}^{- {d/2}}} \leq {\parallel\alpha\parallel}^{d}$. However, this alone is still not enough to get an upper bound of RHS of (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) that is smaller than 1. In the next paragraph, we will tighten the analysis by strengthening the estimates of $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Question II: how to tighten the estimate of $\\det{{(M)}\\mathbf{1}{({M \\succeq 0})}}$?", "weight": 1.0} -->

It turns out that the AM-GM inequality is not always tight for controlling the quantity $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$. In particular, it gives pessimistic bound when $M \succeq 0$ is not true. As a matter of fact, whenever $F_{0}^{c}$ happens, $M$ is unlikely to be positive semidefinite! (The contribution of $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$ will not be negligible since there is still tiny chance that $M$ is PSD.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Question II: how to tighten the estimate of $\\det{{(M)}\\mathbf{1}{({M \\succeq 0})}}$?", "weight": 1.0} -->

As we argued before, even exponential probability event cannot be safely ignored.) We will show that formally the event $\mathbf{1}{({M \succeq 0})}\mathbf{1}{(F_{0}^{c})}$ have small enough probability that can kill the contribution of $Q{(\alpha)}^{d}$ when it happens (see Lemma 4.6 formally).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Summary with formal statements", "weight": 1.0} -->

Below, we formally setup the notation and state two Propositions that summarize the intuitions above. Let $\tau = {{Kn}/d}$ where $K$ is a universal constant that will be determined later. Let $F_{k}$ be the event that We note that $1 \leq {{\mathbf{1}{(F_{0})}} + {\mathbf{1}{(F_{1})}} + \cdots + {\mathbf{1}{(F_{k})}}}$, and therefore we have Therefore towards controlling $\mathbb{E}\left\lbrack {h{(\alpha)}} \right\rbrack$, it suffices to have good upper bounds on $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{k})}} \right\rbrack$ for each $k$, which are summarized in the following two propositions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Local analysis", "weight": 1.0} -->

For a point $x$ in the local region $L_{2}^{c}$, the gradient and the Hessian are dominated by the contributions from the components that have a large correlation with $x$. Therefore it is easier to analyze the first and second order optimality condition directly.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Local analysis", "weight": 1.0} -->

Note that although this region is small, there are still exponentially many critical points (as an example, there is a critical point near $\frac{a_{1} + a_{2}}{\|{a_{1} + a_{2}}\|}$). Therefore our proof still needs to consider the second order conditions and is more complicated than Anandkumar et al..

<!-- chunk {"id": "body-0054", "role": "body", "section": "Bounding the number of local minima using Kac-Rice Formula", "weight": 1.0} -->

In this section we give the proof of Proposition 3.9 and Proposition 3.8, using the intuition described in Section 3.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Claim 4.2", "weight": 1.0} -->

Then, we have that $B \mid {({g_{y} = 0})}$ has the same distribution as $Z$, and consequently ${M_{w} \mid g_{y}} = 0$ has the same distribution as One can see that the setting that we are mostly interested in corresponds to $w = y = \alpha$ in Claim 4.2.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Local Maxima Near True Components", "weight": 1.0} -->

In this section we show that in the neighborhoods of the $2n$ true components, there are exactly $2n$ local maxima. Recall the set $L_{2}$ was defined to be the set of points $x$ that do not have large correlation with any of the components: We will show that the objective function (1.1) has exactly $2n$ local maxima in the set $L_{2}^{c}$, and they are close to the normalized version of $\pm a_{i}$'s.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Local Maxima Near True Components", "weight": 1.0} -->

Let ${\overline{a}}_{i} = \frac{a_{i}}{\| a_{i}\|}$ be the normalized version of $a_{i}$ on the unit sphere. We prove the following slightly stronger version of Theorem 3.3. (Note that Theorem 3.3 is a straightforward corollary of the Theorem below, since w.h.p, for every $i$, ${\| a_{i}\|} = {\sqrt{d} \pm {\overset{\sim}{O}{}}}$. )

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We analyze the optimization landscape of the random over-complete tensor decomposition problem using the Kac-Rice formula and random matrix theory. We show that in the superlevel set $L$ that contains all the points with function values barely larger than the random guess, there are exactly $2n$ local maxima that correspond to the true components. This implies that with an initialization slight better than the random guess, local search algorithms converge to the desired solutions. We believe our techniques can be extended to 3rd order tensors, or other non-convex problems with structured randomness.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The immediate open question is whether there is any other spurious local maximum outside this superlevel set. Answering it seems to involve solving difficult questions in random matrix theory. Another potential approach to unravel the mystery behind the success of the non-convex methods is to analyze the early stage of local search algorithms and show that they will enter the superlevel set $L$ quickly.
