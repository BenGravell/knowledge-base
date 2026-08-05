<!-- arxiv-full-text:v1 {"arxiv_id": "1706.05598", "source": "ar5iv"} -->

## Introduction

Non-convex optimization is the dominating algorithmic technique behind many state-of-art results in machine learning, computer vision, natural language processing and reinforcement learning. Local search algorithms through stochastic gradient methods are simple, scalable and easy to implement. Surprisingly, they also return high-quality solutions for practical problems like training deep neural networks, which are NP-hard in the worst case. It has been conjectured \[DPG^+^14, CHM^+^15\] that on typical data, the landscape of the training objectives has the nice geometric property that all local minima are (approximate) global minima. Such property assures the local search algorithms to converge to global minima \[ \]. However, establishing it for concrete problems can be challenging.

Despite recent progress on understanding the optimization landscape of various machine learning problems (see \[ \] and references therein), a comprehensive answer remains elusive. Moreover, all previous techniques fundamentally rely on the spectral structure of the problems. For example, allows us to pin down the set of the critical points (points with vanishing gradients) as approximate eigenvectors of some matrix. Among these eigenvectors we can further identify all the local minima. The heavy dependency on linear algebraic structure limits the generalization to problems with non-linearity (like neural networks).

Towards developing techniques beyond linear algebra, in this work, we investigate the optimization landscape of tensor decomposition problems. This is a clean non-convex optimization problem whose optimization landscape cannot be analyzed by the previous approach. It also connects to the training of neural networks with many shared properties. For example, in comparison with the matrix case where all the global optima reside on a (connected) Grassmannian manifold, for both tensors and neural networks all the global optima are isolated from each other.

Besides the technical motivations above, tensor decomposition itself is also the key algorithmic tool for learning many latent variable models, mixture of Gaussians, hidden Markov models, dictionary learning \[ AFH^+^12, \], just to name a few. In practice, local search heuristics such as alternating least squares, gradient descent and power method are popular and successful.

Concretely, we consider decomposing a random 4-th order tensor $T$ of the rank $n$ of the following form, We are mainly interested in the over-complete regime where $n \gg d$. This setting is particularly challenging, but it is crucial for unsupervised learning applications where the hidden representations have higher dimension than the data \[, \]. Previous algorithmic results either require access to high order tensors \[, \], or use complicated techniques such as FOOBI or sum-of-squares relaxation \[\].

In the worst case, most tensor problems are NP-hard \[Hås90, \]. Therefore we work in the average case where vectors $a_{i} \in {\mathbb{R}}^{d}$ are assumed to be drawn i.i.d from Gaussian distribution $\mathcal{N}{(0,I)}$. We call $a_{i}$'s the components of the tensor. We are given the entries of tensor $T$ and our goal is to recover the components $a_{1},\ldots,a_{n}$.

We will analyze the following popular non-convex objective, It is known that for $n \ll d^{2}$, the global maxima of $f$ is close to one of ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$. Previously, Ge et al. show that for the orthogonal case where $n \leq d$ and all the $a_{i}$'s are orthogonal, objective function $f{(\cdot)}$ have only $2n$ local maxima that are approximately ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$. However, the technique heavily uses the orthogonality of the components and is not generalizable to over-complete case.

Empirically, projected gradient ascent and power methods find one of the components $a_{i}$'s even if $n$ is significantly larger than $d$. The local geometry for the over-complete case around the true components is known: in a small neighborhood of each of $\pm {\frac{1}{\sqrt{d}}a_{i}}$'s, there is a unique local maximum. Algebraic geometry techniques \[, \] can show that $f{( \cdot )}$ has an exponential number of other critical points, while these techniques seem difficult to extend to the characterization of local maxima. It remains a major open question whether there are any other spurious local maxima that gradient ascent can potentially converge to.

### Main results

We show that there are no spurious local maxima in a large superlevel set that contains all the points with function values slightly larger than that of the random initialization.

### Theorem 1.1

Let ${\varepsilon,\zeta} \in {(0,{1/3})}$ be two arbitrary constants and $d$ be sufficiently large. Suppose $d^{1 + \varepsilon} < n < d^{2 - \varepsilon}$. Then, with high probability over the randomness of $a_{i}$'s, we have that in the superlevel set there are exactly $2n$ local maxima with function values ${({1 \pm {o{}}})}d^{2}$, each of which is $\overset{\sim}{O}{(\sqrt{n/d^{3}})}$-close to one of ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$.

Previously, the best known result only characterizes the geometry in small neighborhoods around the true components, that is, there exists one local minima in each of the small constant neighborhoods around each of the true components $a_{i}$'s. (It turns out in such neighborhoods, the objective function is actually convex.) We significantly enlarge this region to the superlevel set $L$, on which the function $f$ is not convex and has an exponential number of saddle points, but still doesn't have any spurious local minima.

Note that a random initialization $z$ on the unit sphere has expected function value ${{\mathbb{E}}{\lbrack{f{(z)}}\rbrack}} = {3n}$. Therefore the superlevel set $L$ contains all points that have function values barely larger than that of the random guess. Hence, Theorem 1.1 implies that with a slightly better initialization than the random guess, gradient ascent and power method^11^1Power method is exactly equivalent to gradient ascent with a properly chosen finite learning rate are guaranteed to find one of the components in polynomial time. (It is known that after finding one component, it can be peeled off from the tensor and the same algorithm can be repeated to find all other components.)

### Corollary 1.2

In the setting of Theorem 1.1, with high probability over the choice of $a_{i}$'s, we have that given any starting point $x^{0}$ that satisfies ${f{(x^{0})}} \geq {3{({1 + \zeta})}n}$, stochastic projected gradient descent^22^2We note that by stochastic gradient descent we meant the algorithm that is analyzed. To get a global minimizer in polynomial time (polynomial in $\log{({1/\varepsilon})}$ to get $\varepsilon$ precision), one also needs to slightly modify stochastic gradient descent in the following way: one can run SGD until $1/d$ accuracy and then switch to gradient descent. Since the problem is locally strongly convex, the local convergence is linear. will find one of the $\pm {\frac{1}{\sqrt{d}}a_{i}}$'s up to $\overset{\sim}{O}{(\sqrt{n/d^{3}})}$ Euclidean error in polynomial time.

We also strengthen Theorem 1.1 and Corollary 1.2 (see Theorem 3.1. ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) slightly -- the same conclusion still holds with $\zeta = {O{(\sqrt{d/n})}}$ that is smaller than a constant. Note that the expected value of a random initialization is $3n$ and we only require an initialization that is slightly better than random guess in function value. We also conjecture that from random initialization, it suffices to use constant number of projected gradient descent (with optimal step size) to achieve the function value $3{({1 + \zeta})}n$ with $\zeta = {O{(\sqrt{d/n})}}$. This conjecture --- an interesting question for future work --- is based on the hypothesis that the first constant number of steps of gradient descent can make similar improvements as the first step does (which is equal to $c\sqrt{dn}$ for a universal constant $c$).

As a comparison, previous works such as require an initialization with function value ${\Theta{(d^{2})}} \gg n$. Anandkumar et al. analyze the dynamics of tensor power method with a delicate initialization that is independent with the randomness of the tensor. Thus it is not suitable for the situation where the initialization comes from the result of another algorithm, and it does not have a direct implication on the landscape of $f{( \cdot )}$.

We note that the local maximum of $f{( \cdot )}$ corresponds to the robust eigenvector of the tensor. Using this language, our theorem says that a robust eigenvector of an over-complete tensor with random components is either one of those true components or has a small correlation with the tensor in the sense that $\langle T,x^{\otimes 4}\rangle$ is small. This improves significantly upon the understanding of robust eigenvectors under an interesting random model.

### Our techniques

The proof of Theorem 1.1 uses Kac-Rice formula (see, e.g., ), which is based on a counting argument. To build up the intuition, we tentatively view the unit sphere as a collection of discrete points, then for each point $x$ one can compute the probability (with respect to the randomness of the function) that $x$ is a local maximum. Adding up all these probabilities will give us the expected number of local maxima. In continuous space, such counting argument has to be more delicate since the local geometry needs to be taken into account. This is formalized by Kac-Rice formula (see Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")).

However, Kac-Rice formula only gives a closed form expression that involves the integration of the expectation of some complicated random variable. It's often very challenging to simplify the expression to obtain interpretable results. Before our work, Auffinger et al. \[AAČ13, AA^+^13\] have successfully applied Kac-Rice formula to characterize the landscape of polynomials with random Gaussian coefficients. The exact expectation of the number of local minima can be computed there, because the Hessian of a random polynomial is a Gaussian orthogonal ensemble, whose eigenvalue distribution is well-understood with closed form expression.

Our technical contribution here is successfully applying Kac-Rice formula to structured random non-convex functions where the formula cannot be exactly evaluated. The Hessian and gradients of $f{( \cdot )}$ have much more complicated distributions compared to the Gaussian orthogonal ensemble. As a result, the Kac-Rice formula is impossible to be evaluated exactly. We instead cut the space ${\mathbb{R}}^{d}$ into regions and use different techniques to estimate the number of local maxima. See a proof overview in Section 3. We believe our techniques can be extended to 3rd order tensors and can shed light on the analysis of other non-convex problems with structured randomness.

### Organization

In Section 2 we introduce preliminaries regarding manifold optimization and Kac-Rice formula. We give a detailed explanation of our proof strategy in Section 3. We fill in the technical details in the later sections: in Section 4 we show that there is no local maximum that is uncorrelated with any of the true components. We compliment that by a local analysis in Section 5 that shows there are exactly $2n$ local optima around the true components.

## Notations and Preliminaries

We use $\text{Id}_{d}$ to denote the identity matrix of dimension $d \times d$, and for a subspace $K$, let $\text{Id}_{K}$ denote the projection matrix to the subspace $K$. For unit vector $x$, let $P_{x} = {\text{Id} - {xx^{\top}}}$ denote the projection matrix to the subspace orthogonal to $x$. Let $S^{d - 1}$ be the $d - 1$-dimensional sphere $S^{d - 1}:={\{{x \in {\mathbb{R}}^{d}}:{{\| x\|}^{2} = 1}\}}$.

Let $u \odot v$ denote the Hadamard product between vectors $u$ and $v$. Let $u^{\odot s}$ denote $u \odot \cdots \odot u$ where $u$ appears $k$ times. Let $A \otimes B$ denote the Kronecker product of $A$ and $B$. Let $\parallel \cdot \parallel$ denote the spectral norm of a matrix or the Euclidean norm of a vector. Let ${\parallel \cdot \parallel}_{F}$ denote the Frobenius norm of a matrix or a tensor.

We write $A \lesssim B$ if there exists a universal constant $C$ such that $A \leq {CB}$. We define $\gtrsim$ similarly. Unless explicitly stated otherwise, $O{( \cdot )}$-notation hides absolute multiplicative constants. Concretely, every occurrence of the notation $O{(x)}$ is a placeholder for some function $f{(x)}$ that satisfies ${{\forall x} \in {\mathbb{R}}},{{|{f{(x)}}|} \leq {C{|x|}}}$ for some absolute constant $C > 0$.

### Gradient, Hessian, and local maxima on manifold

We have a constrained optimization problem over the unit sphere $S^{d - 1}$, which is a smooth manifold. Thus we define the local maxima with respect to the manifold. It's known that projected gradient descent for $S^{d - 1}$ behaves pretty much the same on the manifold as in the usual unconstrained setting. In Section A we give a brief introduction to manifold optimization, and the definition of gradient and Hessian. We refer the readers to the book for more backgrounds. Here we use $\text{grad~}f$ and $\text{Hess~}f$ to denote the gradient and the Hessian of $f$ on the manifold $S^{d - 1}$. We compute them in the following claim.

### Claim 2.1

Let $f:{S^{d - 1}\rightarrow{\mathbb{R}}}$ be ${f{(x)}}:={\frac{1}{4}{\sum_{i = 1}^{n}{\langle a_{i},x\rangle}^{4}}}$. Then the gradient and Hessian of $f$ on the sphere can be written as, where $P_{x} = {\text{Id}_{d} - {xx^{\top}}}$.

A local maximum of a function $f$ on the manifold $S^{d - 1}$ satisfies ${\text{grad~}f{(x)}} = 0$, and ${\text{Hess~}f{(x)}} \preceq 0$. Let $\mathcal{M}_{f}$ be the set of all local maxima,

### Kac-Rice formula

Kac-Rice formula is a general tool for computing the expected number of special points on a manifold. Suppose there are two random functions ${P{( \cdot )}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ and ${Q{( \cdot )}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{k}}$, and an open set $\mathcal{B}$ in ${\mathbb{R}}^{k}$. The formula counts the expected number of point $x \in {\mathbb{R}}^{d}$ that satisfies both ${P{(x)}} = 0$ and ${Q{(x)}} \in \mathcal{B}$.

Suppose we take $P = {\nabla f}$ and $Q = {\nabla^{2}f}$, and let $\mathcal{B}$ be the set of negative semidefinite matrices, then the set of points that satisfies ${P{(x)}} = 0$ and $Q \in \mathcal{B}$ is the set of all local maxima $\mathcal{M}_{f}$. Moreover, for any set $Z \subset S^{d - 1}$, we can also augment $Q$ by $Q = {\lbrack{\nabla^{2}f},x\rbrack}$ and choose $\mathcal{B} = {{\{ A:{A \preceq 0}\}} \otimes Z}$. With this choice of $P,Q$, Kac-Rice formula can count the number of local maxima inside the region $Z$. For simplicity, we will only introduce Kac-Rice formula for this setting. We refer the readers to \[, Chapter 11&12\] for more backgrounds.

### Lemma 2.2 (Informally stated)

Let $f$ be a random function defined on the unit sphere $S^{d - 1}$ and let $Z \subset S^{d - 1}$. Under certain regularity conditions^33^3We omit the long list of regularity conditions here for simplicity. See more details at \[, Theorem 12.1.1\] on $f$ and $Z$, we have where $dx$ is the usual surface measure on $S^{d - 1}$ and $p_{\text{grad~}f{(x)}}{}$ is the density of $\text{grad~}f{(x)}$ at 0.

### Formula for the number of local maxima

In this subsection, we give a concrete formula for the number of local maxima of our objective function (1.1) inside the superlevel set $L$ (defined in equation (1.2)). Taking $Z = L$ in Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions"), it boils down to estimating the quantity on the right hand side of (2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")). We remark that for the particular function $f$ as defined in (1.1) and $Z = L$, the integrand in (2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")) doesn't depend on the choice of $x$. This is because for any $x \in S^{d - 1}$, $({\text{Hess~}f},{\text{grad~}f},{\mathbf{1}{({x \in L})}})$ has the same joint distribution, as characterized below:

### Lemma 2.3

Let $f$ be the random function defined in (1.1). Let ${\alpha_{1},\ldots,\alpha_{n}} \in {\mathcal{N}{}}$, and ${b_{1},\ldots,b_{n}} \sim {\mathcal{N}{(0,\text{Id}_{d - 1})}}$ be independent Gaussian random variables. Let Then, we have that for any $x \in S^{d - 1}$, $({\text{Hess~}f},{\text{grad~}f},f)$ has the same joint distribution as $({- M},g,\left. \parallel\alpha\parallel \right._{4}^{4})$.

### Proof

We use Claim 2.1. We fix $x \in S^{d - 1}$ and let $\alpha_{i} = {\langle a_{i},x\rangle}$ and $b_{i} = {P_{x}a_{i}}$. We have $\alpha_{i}$ and $b_{i}$ are independent, and $b_{i}$ is spherical Gaussian random vector in the tangent space at $x$ (which is isomorphic to ${\mathbb{R}}^{d - 1}$). We can verify that ${\text{grad~}f{(x)}} = {\sum_{i \in {\lbrack n\rbrack}}{\alpha_{i}^{3}b_{i}}} = g$ and ${\text{Hess~}f{(x)}} = {- M}$, and this complete the proof. ∎ Using Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions") (with $Z = L$) and Lemma 2.3, we derive the following formula for the expectation of our random variable $\mathbb{E}\left\lbrack {|{\mathcal{M}_{f} \cap L}|} \right\rbrack$. Later we will later use Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions") slightly differently with another choice of $Z$.

### Lemma 2.4

Using the notation of Lemma 2.3, let $p_{g}{( \cdot )}$ denote the density of $g$. Then,

## Proof Overview

In this section, we give a high-level overview of the proof of the main Theorem. We will prove a slightly stronger version of Theorem 1.1.

Let $\gamma$ be a universal constant that is to be determined later. Define the set $L_{1} \subset S^{d - 1}$ as, Indeed we see that $L$ (defined in (1.2)) is a subset of $L_{1}$ when $n \gg d$. We prove that in $L_{1}$ there are exactly $2n$ local maxima.

### Theorem 3.1 (main)

There exists universal constants $\gamma,\beta$ such that the following holds: suppose ${d^{2}/\log^{O{}}} \geq n \geq {\betad{\log^{2}d}}$ and $L_{1}$ be defined as in (3.1), then with high probability over the choice of $a_{1},\ldots,a_{n}$, we have that the number of local maxima in $L_{1}$ is exactly $2n$: Moreover, each of the local maximum in $L_{1}$ is $\overset{\sim}{O}{(\sqrt{n/d^{3}})}$-close to one of ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$.

In order to count the number of local maxima in $L_{1}$, we use the Kac-Rice formula (Lemma 2.4). Recall that what Kac-Rice formula gives an expression that involves the complicated expectation $\mathbb{E}\left\lbrack {{{\left| {\det{(M)}} \right|\mathbf{1}{({M \succeq 0})}\mathbf{1}{({\left. \parallel\alpha\parallel \right._{4}^{4} \geq {3{({1 + \zeta})}n}})}} \mid g} = 0} \right\rbrack$. Here the difficulty is to deal with the determinant of a random matrix $M$ (defined in Lemma 2.3), whose eigenvalue distribution does not admit an analytical form. Moreover, due to the existence of the conditioning and the indicator functions, it's almost impossible to compute the RHS of the Kac-Rice formula (equation (2.4)) exactly.

### Local vs. global analysis

The key idea to proceed is to divide the superlevel set $L_{1}$ into two subsets Here $\delta$ is a sufficiently small universal constant that is to be chosen later. We also note that $L_{2}^{c} \subset L_{1}$ and hence $L_{1} = {{({L_{1} \cap L_{2}})} \cup L_{2}^{c}}$.

Intuitively, the set $L_{1} \cap L_{2}$ contains those points that do not have large correlation with any of the $a_{i}$'s; the compliment $L_{2}^{c}$ is the union of the neighborhoods around each of the desired vector ${\frac{1}{\sqrt{d}}a_{1}},\ldots,{\frac{1}{\sqrt{d}}a_{n}}$. We will refer to the first subset $L_{1} \cap L_{2}$ as the global region, and refer to the $L_{2}^{c}$ as the local region.

We will compute the number of local maxima in sets $L_{1} \cap L_{2}$ and $L_{2}^{c}$ separately using different techniques. We will show that with high probability $L_{1} \cap L_{2}$ contains zero local maxima using Kac-Rice formula (see Theorem 3.2). Then, we show that $L_{2}^{c}$ contains exactly $2n$ local maxima (see Theorem 3.3) using a different and more direct approach.

### Global analysis

The key benefit of have such division to local and global regions is that for the global region, we can avoid evaluating the value of the RHS of the Kac-Rice formula. Instead, we only need to have an estimate: Note that the number of local optima in $L_{1} \cap L_{2}$, namely $|{\mathcal{M}_{f} \cap L_{1} \cap L_{2}}|$, is an integer nonnegative random variable. Thus, if we can show its expectation $\mathbb{E}\left\lbrack {|{\mathcal{M}_{f} \cap L_{1} \cap L_{2}}|} \right\rbrack$ is much smaller than $1$, then Markov's inequality implies that with high probability, the number of local maxima will be exactly zero. Concretely, we will use Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions") with $Z = {L_{1} \cap L_{2}}$, and then estimate the resulting integral using various techniques in random matrix theory. It remains quite challenging even if we are only shooting for an estimate. see Theorem 3.2 for the exact statement and Section 3.1 for an overview of the analysis.

### Local analysis

In the local region $L_{2}^{c}$, that is, the neighborhoods of $a_{1},\ldots,a_{n}$, we will show there are exactly $2n$ local maxima. As argued above, it's almost impossible to get exact numbers out of the Kac-Rice formula since it's often hard to compute the complicated integral. Moreover, Kac-Rice formula only gives the expected number but not high probability bounds. However, here the observation is that the local maxima (and critical points) in the local region are well-structured. Thus, instead, we show that in these local regions, the gradient and Hessian of a point $x$ are dominated by the terms corresponding to components $\{ a_{i}\}$'s that are highly correlated with $x$. The number of such terms cannot be very large (by restricted isometry property, see Section B.5). As a result, we can characterize the possible local maxima explicitly, and eventually show there is exactly one local maximum in each of the local neighborhoods around $\{{\pm {\frac{1}{\sqrt{d}}a_{i}}}\}$'s.

### Concentration properties of $a_{i}$'s

Before stating the formal results regarding the local and global analysis, we have the following technical preparation. Since $a_{i}$'s are chosen at random, with small probability the tensor $T$ will behave very differently from the average instances. The optimization problem for such irregular tensors may have much more local maxima. To avoid these we will restrict our attention to the following event $G_{0}$, which occurs with high probability (over the randomness of $a_{i}$'s): Here $\delta$ is a small enough universal constant. Event $G_{0}$ summarizes common properties of the vectors $a_{i}$'s that we frequently use in the technical sections. Equation (3.4) is the restricted isometry property (see Section B.5) that ensures the $a_{i}$'s are not adversarially correlated with each other. Equation (3.5) lowerbounds the high order moments of $a_{i}$'s. Equation (3.6) bounds the singular values of the matrix $\sum_{i = 1}^{n}{a_{i}a_{i}^{\top}}$. These conditions will be useful in the later technical sections.

Next, we formalize the intuition above as the two theorems below. Theorem 3.2 states there is no local maximum in $L_{1} \cap L_{2}$, whereas Theorem 3.3 concludes that there are exactly $2n$ local maxima in $L_{1} \cap L_{2}^{c}$.

### Theorem 3.2

There exists universal small constant $\delta \in {}$ and universal constants $\gamma,\beta$ such that for sets $L_{1},L_{2}$ defined in equation (3.3) and $n \geq {\betad{\log^{2}d}}$, we have that the expected number of local maxima in $L_{1} \cap L_{2}$ is exponentially small:

### Theorem 3.3

Suppose ${{{1/\delta^{2}} \cdot d}{\log d}} \leq n \leq {d^{2}/{\log^{O{}}d}}$. Then, with high probability over the choice $a_{1},\ldots,a_{n}$, we have, Moreover, each of the point in $L \cap L_{2}^{c}$ is $\overset{\sim}{O}{(\sqrt{n/d^{3}})}$-close to one of ${\pm {\frac{1}{\sqrt{d}}a_{1}}},\ldots,{\pm {\frac{1}{\sqrt{d}}a_{n}}}$.

### Proof of the main theorem

The following Lemma shows that event $G_{0}$ that we conditioned on is indeed a high probability event. The proof follows from simple concentration inequalities and is deferred to Section C.

### Lemma 3.4

Suppose ${{{1/\delta^{2}} \cdot d}{\log^{2}d}} \leq n \leq {d^{2}/{\log^{O{}}d}}$. Then, Combining Theorem 3.2, Theorem 3.3 and Lemma 3.4, we obtain Theorem 3.1. ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions") straightforwardly.

### Proof of Theorem 3.1. ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")

By Theorem 3.2 and Markov inequality, we obtain that ${\Pr\left\lbrack {{{|{L \cap L_{1} \cap L_{2}}|}\mathbf{1}{(G_{0})}} < {1/2}} \right\rbrack} \leq 2^{{- {d/2}} + 1}$. Since ${|{L \cap L_{1} \cap L_{2}}|}\mathbf{1}{(G_{0})}$ is an integer value random variable, therefore, we get ${\Pr\left\lbrack {{{|{L \cap L_{1} \cap L_{2}}|}\mathbf{1}{(G_{0})}} = 0} \right\rbrack} \leq 2^{{- {d/2}} + 1}$. Thus, using Lemma 3.4, Theorem 3.3 and union bound, with high probability, we have that $G_{0}$, ${{|{L \cap L_{1} \cap L_{2}}|}\mathbf{1}{(G_{0})}} = 0$ and equation (3.7) happen. Then, using Theorem 3.3 and union bound, we concluded that ${|{L \cap L_{1}}|} = {{|{L \cap L_{1} \cap L_{2}^{c}}|} + {|{L \cap L_{1} \cap L_{2}}|}} = {2n}$. ∎ In the next subsections we sketch the basic ideas behind the proof of of Theorem 3.2 and Theorem 3.3. Theorem 3.2 is the crux of this technical part of the paper.

### Estimating the Kac-Rice formula for the global region

The general plan to prove Theorem 3.2 is to use random matrix theory to estimate the RHS of the Kac-Rice formula. We begin by applying Kac-Rice formula to our situation.

We first note that by definition of $G_{0}$, where $L_{G} = {\{{x \in S^{d - 1}}:{x{\text{satisfies equation ~(}\text{),~(}\text{) and~(}\text{)}}}\}}$. Indeed, when $G_{0}$ happens, then $L_{G} = S^{d - 1}$, and therefore equation (3.8) holds.

Thus it suffice to control $\mathbb{E}\left\lbrack \left| {\mathcal{M}_{f} \cap L_{1} \cap L_{2} \cap L_{G}} \right| \right\rbrack$. We will use the Kac-Rice formula (Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions")) with the set $Z = {\mathcal{M}_{f} \cap L_{1} \cap L_{2} \cap L_{G}}$.

### Applying Kac-Rice formula

The first step to apply Kac-Rice formula is to characterize the joint distribution of the gradient and the Hessian. We use the notation of Lemma 2.3 for expressing the joint distribution of $({\text{Hess~}f},{\text{grad~}f},{\mathbf{1}{({x \in Z})}})$. For any fix $x \in S^{d - 1}$, let $\alpha_{i} = {\langle a_{i},x\rangle}$ and $b_{i} = {P_{x}a_{i}}$ (where $P_{x} = {\text{Id} - {xx^{\top}}}$) and $M = {{{\parallel\alpha\parallel}_{4}^{4} \cdot \text{Id}_{d - 1}} - {3{\sum_{i = 1}^{n}{\alpha_{i}^{2}b_{i}b_{i}^{\top}\text{and}g}}}} = {\sum_{i = 1}^{n}{\alpha_{i}^{3}b_{i}}}$ as defined in (2.3). In order to apply Kac-Rice formula, we'd like to compute the joint distribution of the gradient and the Hessian. We have that where $E_{0},E_{1},E_{2},E_{2}'$ are defined as follows (though these details here will only be important later).

We see that the equations above correspond to equation (3.4), (3.5) and (3.6) and event $\mathbf{1}{(E_{0})}$ corresponds to the event $x \in L_{G}$. Similarly, the following event $E_{1}$ corresponds to $x \in L_{1}$.

Events $E_{2}$ and $E_{2}'$ correspond to the events that $x \in L_{2}$. We separate them out to reflect that $E_{2}$ and $E_{2}'$ depends the randomness of $\alpha_{i}$'s and $b_{i}$'s respectively.

Using Kac-Rice formula (Lemma 2.2. ‣ 2.2 Kac-Rice formula ‣ 2 Notations and Preliminaries ‣ On the Optimization Landscape of Tensor Decompositions") with $Z = {L_{1} \cap L_{2} \cap L_{G}}$), we conclude that Next, towards proving Theorem 3.2 we will estimate the RHS of the equation (3.10) using various techniques.

### Conditioning on $\alpha$

We observe that the distributions of the gradient $g$ and Hessian $M$ are fairly complicated. In particular, we need to deal with the interactions of $\alpha_{i}$'s (the components along $x$) and $b_{i}$'s (the components in the orthogonal subspace of $x$). Therefore, we use the law of total expectation to first condition on $\alpha$ and take expectation over the randomness of $b_{i}$'s, and then take expectation over $\alpha_{i}$'s. Here below the inner expectation of RHS of (3.11) is with respect to the randomness of $b_{i}$'s and the outer one is with respect to $\alpha_{i}$'s.

### Lemma 3.5

Using the notation of Lemma 2.3, let $E$ denotes an event and let $p_{g \mid \alpha}$ denotes the density of $g \mid \alpha$. Then, For notional convenience we define ${h{(\cdot)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ as Using equation (3.8), the Kac-Rice formula (equation (3.10)), and law of total expectation (Lemma 3.5), we obtain straightforwardly the following Lemma which gives an explicit formula for the number of local maxima in $L_{1} \cap L_{2}$. We provide a rigorous proof in Section C that verifies the regularity condition of Kac-Rice formula.

### Lemma 3.6

Let $h{(\cdot)}$ be defined as above. In the setting of this section, we have We note that $p_{g \mid \alpha}{}$ has an explicit expression since $g \mid \alpha$ is Gaussian. For the ease of exposition, we separate out the hard-to-estimate part from $h{(\alpha)}$, which we call $W{(\alpha)}$: Therefore by definition, we have that Now, since we have conditioned on $\alpha$, the distributions of the Hessian, namely $M \mid \alpha$, is a generalized Wishart matrix which is slightly easier than before. However there are still several challenges that we need to address in order to estimate $W{(\alpha)}$.

### Question I: how to control $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$?

Recall that $M = {\left. \parallel\alpha\parallel \right._{4}^{4} - {3{\sum{\alpha_{i}^{2}b_{i}b_{i}^{\top}}}}}$, which is a generalized Wishart matrix whose eigenvalue distribution has no (known) analytical expression. The determinant itself by definition is a high-degree polynomial over the entries, and in our case, a complicated polynomial over the random variables $\alpha_{i}$'s and vectors $b_{i}$'s. We also need to properly exploit the presence of the indicator function $\mathbf{1}{({M \succeq 0})}$, since otherwise, the desired statement will not be true -- the function $f$ has an exponential number of critical points.

Fortunately, in most of the cases, we can use the following simple claim that bounds the determinant from above by the trace. The inequality is close to being tight when all the eigenvalues of $M$ are similar to each other. More importantly, it uses naturally the indicator function $\mathbf{1}{({M \succeq 0})}$! Later we will see how to strengthen it when it's far from tight.

### Claim 3.7

For any $p \times p$ symmetric matrix $V$, we have, The claim is a direct consequence of AM-GM inequality.

### Proof

We can assume $V$ is positive semidefinite since otherwise both sides of the inequality vanish. Then, suppose ${\lambda_{1},\ldots,\lambda_{p}} \geq 0$ are the eigenvalues of $V$. We have ${\det{(V)}} = {\lambda_{1}\ldots\lambda_{p}}$ and ${|{\text{tr}{(V)}}|} = {\text{tr}{(V)}} = {\lambda_{1} + \cdots + \lambda_{p}}$. Then by AM-GM inequality we complete the proof. ∎ Applying the Lemma above with $V = M$, we have Here we dropped the indicators for events $E_{2}$ and $E_{2}'$ since they are not important for the discussion below. It turns out that $|{\text{tr}{(M)}}|$ is a random variable that concentrates very well, and thus we have ${\mathbb{E}\left\lbrack {|{\text{tr}{(M)}}|}^{d - 1} \right\rbrack} \approx {|{\mathbb{E}\left\lbrack {\text{tr}{(M)}} \right\rbrack}|}^{d - 1}$. It can be shown that (see Proposition 4.3 for the detailed calculation), Therefore using equation (3.14⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) and equation above, ignoring $\mathbf{1}{(E_{2}')}$, we have that Note that since $g \mid \alpha$ has Gaussian distribution, we have, Thus using two equations above, we can bound $\mathbb{E}\left\lbrack {h{(\alpha)}} \right\rbrack$ by Therefore, it suffices to control the RHS of (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")), which is much easier than the original Kac-Rice formula. However, we still need to be careful here, as it turns out that RHS of (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) is roughly $c^{d}$ for some constant $c > 1$! Roughly speaking, this is because the high powers of a random variables is very sensitive to its tail.

### Easy case when all $\alpha_{i}$'s are small

To find a tight bound for the RHS of (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")), intuitively we can consider two events: the event $F_{0}$ when all of the $\alpha_{i}$'s are close to constant (defined rigorously later in equation (3.19)) and the complementary event $F_{0}^{c}$.

We claim that $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{0})}} \right\rbrack$ can be bounded by $2^{- {d/2}}$. Then we will argue that it's difficult to get an upperbound for $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{0}^{c})}} \right\rbrack$ that is smaller than 1 using the RHS of equation (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")).

It turns out in most of the calculations below, we can safely ignore the contribution of the term ${3{\parallel\alpha\parallel}_{8}^{8}}/{\|\alpha\|}_{6}^{6}$. For notation convenience, let ${Q{(\cdot)}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be defined as: When conditioned on the event $F_{0}$, roughly speaking, random variable ${Q{(\alpha)}} = {{\|\alpha\|}_{4}^{4} - {3{\|\alpha\|}^{2}}}$ behaves like a Gaussian distribution with variance $\Theta{(n)}$, since $Q{(\alpha)}$ is a sum of independent random variables with constant variances. Note that $\mathbf{1}{(E_{1})}$ and $\mathbf{1}{(E_{0})}$ imply that ${Q{(\alpha)}} = {{\parallel\alpha\parallel}_{4}^{4} - {3{\parallel\alpha\parallel}_{2}^{2}}} \geq {{({\gamma - 3})}\sqrt{nd}}$. Therefore, $Q{(\alpha)}\mathbf{1}{(E_{0})}\mathbf{1}{(E_{1})}$ behaves roughly like a truncated Gaussian distribution, that is, ${X \cdot \mathbf{1}}{({X \geq {{({\gamma - 3})}\sqrt{nd}}})}$ where $X \sim {\mathcal{N}{(0,{\Theta{(\sqrt{n})}})}}$. Then for sufficiently large constant $\gamma$, Moreover, recall that when the event $E_{0}$ happens, we have that $\left. \parallel\alpha\parallel \right._{6}^{6} \geq {15{({1 - \delta})}n}$. Therefore putting all these bounds together into equation (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) with the indicator $\mathbf{1}{(F_{0})}$, and using the fact that ${\text{Vol}{(S^{d - 1})}} = \frac{\pi^{d/2}}{\Gamma{({{d/2} + 1})}}$, we can obtain the target bound,

### The heavy tail problem

Next we explain why it's difficult to achieve a good bound from using RHS (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")). The critical issue is that the random variable $Q{(\alpha)}$ has very heavy tail, and exponentially small probability cannot be ignored. To see this, we first claim that $Q{(\alpha)}$ has a tail distribution that roughly behaves like Taking $t = d^{2}$, then the contribution of the tail to the expectation of $Q{(\alpha)}^{d}$ is at least ${{\Pr\left\lbrack {{Q{(\alpha)}} \geq t} \right\rbrack} \cdot t^{d}} \approx d^{2d}$, which is much larger than what we obtained (equation (3.18)) in the case when all $\alpha_{i}$'s are small.

The obvious fix is to consider $Q{(\alpha)}^{d}{({\parallel\alpha\parallel}_{6}^{6})}^{- {d/2}}$ together (instead of separately). For example, we will use Cauchy-Schwarz inequality to obtain that ${Q{(\alpha)}^{d}{({\parallel\alpha\parallel}_{6}^{6})}^{- {d/2}}} \leq {\parallel\alpha\parallel}^{d}$. However, this alone is still not enough to get an upper bound of RHS of (3.16⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) that is smaller than 1. In the next paragraph, we will tighten the analysis by strengthening the estimates of $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$.

### Question II: how to tighten the estimate of $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$?

It turns out that the AM-GM inequality is not always tight for controlling the quantity $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$. In particular, it gives pessimistic bound when $M \succeq 0$ is not true. As a matter of fact, whenever $F_{0}^{c}$ happens, $M$ is unlikely to be positive semidefinite! (The contribution of $\det{{(M)}\mathbf{1}{({M \succeq 0})}}$ will not be negligible since there is still tiny chance that $M$ is PSD. As we argued before, even exponential probability event cannot be safely ignored.) We will show that formally the event $\mathbf{1}{({M \succeq 0})}\mathbf{1}{(F_{0}^{c})}$ have small enough probability that can kill the contribution of $Q{(\alpha)}^{d}$ when it happens (see Lemma 4.6 formally).

### Summary with formal statements

Below, we formally setup the notation and state two Propositions that summarize the intuitions above. Let $\tau = {{Kn}/d}$ where $K$ is a universal constant that will be determined later. Let $F_{k}$ be the event that We note that $1 \leq {{\mathbf{1}{(F_{0})}} + {\mathbf{1}{(F_{1})}} + \cdots + {\mathbf{1}{(F_{k})}}}$, and therefore we have Therefore towards controlling $\mathbb{E}\left\lbrack {h{(\alpha)}} \right\rbrack$, it suffices to have good upper bounds on $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{k})}} \right\rbrack$ for each $k$, which are summarized in the following two propositions.

### Proposition 3.8

Let $K \geq {2 \cdot 10^{3}}$ be a universal constant. Let $\tau = {{Kn}/d}$ and let $\gamma,\beta$ be sufficiently large constants (depending on $K$). Then for any $n \geq {\betad{\log^{2}d}}$, we have that for any $k \in {\{ 1,\ldots,n\}}$

### Proposition 3.9

In the setting of Proposition 3.8, we have, We see that Theorem 3.2 can be obtained as a direct consequence of Proposition 3.9, Proposition 3.8 and Lemma 3.6.

### Proof of Theorem 3.2

Using equation (3.21) and Lemma 3.6, we have that

### Local analysis

For a point $x$ in the local region $L_{2}^{c}$, the gradient and the Hessian are dominated by the contributions from the components that have a large correlation with $x$. Therefore it is easier to analyze the first and second order optimality condition directly.

Note that although this region is small, there are still exponentially many critical points (as an example, there is a critical point near $\frac{a_{1} + a_{2}}{\|{a_{1} + a_{2}}\|}$). Therefore our proof still needs to consider the second order conditions and is more complicated than Anandkumar et al..

We first show that all local maxima in this region must have very high correlation with one of the components:

### Lemma 3.10

In the setting of Theorem 3.3, for any local maximum $x \in L_{2}$, there exists a component $a \in {\{{\pm {a_{i}/{\| a_{i}\|}}}\}}$ such that ${\langle x,a\rangle} \geq 0.99$.

Intuitively, if there is a unique component $a_{i}$ that is highly correlated with $x$, then the gradient ${\text{grad~}f{(x)}} = {\sum_{j = 1}^{n}{{\langle a_{j},x\rangle}^{3}a_{j}}}$ will be even more correlated with $a_{i}$. On the other hand, if $x$ has similar correlation with two components (e.g., $x = \frac{a_{1} + a_{2}}{\|{a_{1} + a_{2}}\|}$), then $x$ is close to a saddle point, and the Hessian will have a positive direction that makes $x$ more correlated with one of the two components.

Once $x$ has really high correlation with one component (${|{\langle x,a_{i}\rangle}|} \geq {0.99{\| a_{i}\|}}$), we can prove that the gradient of $x$ is also in the same local region. Therefore by fixed point theorem, there must be a point where ${\text{grad~}f{(x)}} = x$, and it is a critical point. We also show the function is strongly concave in the whole region where ${|{\langle x,a_{i}\rangle}|} \geq {0.99{\| a_{i}\|}}$. Therefore we know the critical point is actually a local maximum.

## Bounding the number of local minima using Kac-Rice Formula

In this section we give the proof of Proposition 3.9 and Proposition 3.8, using the intuition described in Section 3.

### Proof of Proposition 3.9

Following the plan in Section 3, we start with using AM-GM inequality for the determinant.

### Lemma 4.1

Under the setting of Proposition 3.9, we have, The next thing that we need to bound is $\mathbb{E}\left\lbrack {{|{\text{tr}{(M)}}|}^{d - 1} \mid {g,\alpha}} \right\rbrack$. Here the basic intuition is that since ${\text{tr}{(M)}} \mid {g,\alpha}$ is quite concentrated around its mean and therefore we can switch the $({d - 1})$-th power with the expectation without losing much. Proving such a result would require the understanding of the distribution of $M \mid {g,\alpha}$. We have the following generic Claim that computes this distribution in a more general setting.

### Claim 4.2

Let ${w,y} \in {\mathbb{R}}^{n}$ be two fixed vectors, and let $\overline{q} = {y^{\odot 3}/{\parallel y^{\odot 3}\parallel}}$. Let $B = {\lbrack b_{1},\ldots,b_{n}\rbrack} \in {\mathbb{R}}^{{({d - 1})} \times n}$ be a matrix with independent standard Gaussians as entries. Let $M_{w} = {{{\| w\|}_{4}^{4} \cdot \text{Id}_{d - 1}} - {3{\sum_{i = 1}^{n}{w_{i}^{2}b_{i}b_{i}^{\top}}}}}$ and $g_{y} = {\sum_{i = 1}^{n}{y_{i}^{3}b_{i}}}$. Let $Z \in {\mathbb{R}}^{{({d - 1})} \times n}$ be a random matrix with rows independent drawn from $\mathcal{N}{(0,{\text{Id}_{n} - {\overline{q}{\overline{q}}^{\top}}})}$.

Then, we have that $B \mid {({g_{y} = 0})}$ has the same distribution as $Z$, and consequently ${M_{w} \mid g_{y}} = 0$ has the same distribution as One can see that the setting that we are mostly interested in corresponds to $w = y = \alpha$ in Claim 4.2.

### Proof

Let $c_{1}^{\top},\ldots,c_{d - 1}^{\top}$ be the rows of $B$. We write $c_{i} = {{\beta_{i}\overline{q}} + z_{i}}$ where $\beta_{i} = {\langle c_{i},\overline{q}\rangle}$ and $z_{i} = {{({\text{Id}_{n} - {\overline{q}{\overline{q}}^{\top}}})}c_{i}}$. Let $Z$ denote the matrix with $z_{i}^{\top}$ as rows. Therefore we have $B = {Z + {\beta{\overline{q}}^{\top}}}$. Recall that $b_{i}$ are independent Gaussians with covariance $\mathcal{N}{(0,\text{Id}_{d - 1})}$. Thus we have that $c_{i}$'s are independent Gaussians with covariance $\mathcal{N}{(0,\text{Id}_{n})}$, and consequently $\beta_{i}$ and $z_{i}$ are independent random variables with $\mathcal{N}{}$ and $\mathcal{N}{(0,{\text{Id}_{n} - {\overline{q}{\overline{q}}^{\top}}})}$ respectively. Moreover, note that $g = 0$ is equivalent to that ${{\forall i} \in {\lbrack{d - 1}\rbrack}},{{\langle c_{i},q\rangle} = 0}$, which in turn is equivalent to that ${{\forall i} \in {\lbrack{d - 1}\rbrack}},{\beta_{i} = 0}$. Hence, $B \mid {({g_{y} = 0})}$ has the same distribution as $Z$, and consequently $M_{w} \mid {({g_{y} = 0})}$ has the same distribution as ${{\| w\|}_{4}^{4}\text{Id}_{d - 1}} - {3Z{{diag}{(w^{\odot 2})}}Z^{\top}}$. ∎ Using Claim 4.2, we can compute the the expectation of the trace and its $p$-th moments. Again we state the following proposition in a more general setting for future re-usability.

### Proposition 4.3

In the setting of Claim 4.2, we have Moreover, for any $\varepsilon \in {}$,

### Proof of Proposition 4.3

We use the same notations as in the proof of Claim 4.2. By Claim 4.2, we have $B = {{\lbrack b_{1},\ldots,b_{n}\rbrack} \mid {({g_{y} = 0})}}$ has the same distribution as $Z$, and consequently $M_{w} \mid {({g_{y} = 0})}$ has the same distribution as ${{\| w\|}_{4}^{4}\text{Id}_{d - 1}} - {3Z{{diag}{(w^{\odot 2})}}Z^{\top}}$. Furthermore, this implies that $\text{tr}{({M_{w} \mid {({g_{y} = 0})}})}$ has the same distribution as the random variable (denoted by $\Gamma$ below) Since $z_{k} \odot w$ is Gaussian random variable, we have that ${\|{z_{k} \odot w}\|}^{2}$ is a sub-exponential random variable with parameter $(\nu,\rho)$ satisfying $\nu \lesssim {\| w\|}_{4}^{2}$ and $\rho \lesssim {\| w\|}_{\infty}^{2}$ (see Definition B.1. ‣ B.1 Sub-exponential random variables ‣ Appendix B Toolbox ‣ On the Optimization Landscape of Tensor Decompositions") for the definition of sub-exponential random variable and see Lemma B.15 for the exact calculation of the parameters for this case). It is well known that when one takes sum of independent sub-exponential random variable, the $\rho$ parameter will be preserved and $\nu^{2}$ (which should be thought of as variance) will added up (see Lemma B.4. ‣ B.1 Sub-exponential random variables ‣ Appendix B Toolbox ‣ On the Optimization Landscape of Tensor Decompositions") for details). Therefore, we have that $\Gamma$ is a sub-exponential random variable with parameter $(\nu^{\ast},\rho^{\ast})$ satisfying $\nu^{\ast} \lesssim {\sqrt{d - 1}{\| w\|}_{4}^{2}}$ and $\rho^{\ast} \lesssim {\| w\|}_{\infty}^{2}$. Moreover, by Lemma B.15 again and the linearity of expectation, we can compute the expectation of $\Gamma$, Next the basic intuition is if $\nu^{\ast}$ and $\rho^{\ast}$ are small enough compared to the mean of $\Gamma$, then $\Gamma$ is extremely concentrated around its mean, and thus $\mathbb{E}\left\lbrack {|\Gamma|}^{p} \right\rbrack$ is close to $\mathbb{E}\lbrack\Gamma\rbrack^{p}$. Otherwise, the mean is more or less negligible compared to $\max{\{{p{\parallel w\parallel}_{\infty}},{2\sqrt{pd}{\parallel w\parallel}_{4}^{2}}\}}$, then the moment of $\Gamma$ behaves like the moments of an sub-exponential random variable with mean 0. Indeed, using basic integration, we can show (see Lemma B.10) that a sub-exponential random variable with mean $\mu$ and parameter $(\nu,b)$ satisfies that for any $\varepsilon \in {}$, Applying the equation above to $\Gamma$ completes the proof. ∎ Using Proposition 4.3 with $w = y = \alpha$. we obtain the following bounds for the moments of the trace of $M$.

### Corollary 4.4

For any fixed $\alpha$, we have

### Proof

We fix the choice of $\alpha$ and assume it satisfies event $F_{0}$. We will apply Proposition 4.3 with $w = \alpha$ and $y = \alpha$. We can verify that when $E_{0}$ and $E_{2}$ both happen, we have Therefore, taking $\varepsilon = {O{(\delta)}}$ in Proposition 4.3, we have that where $\mu = \left| {\mathbb{E}\left\lbrack {\text{tr}{(M)}} \right\rbrack} \right| = {{({d - 1})}{({{{\|\alpha\|}^{4} - {3{\|\alpha\|}^{2}}} + \frac{3{\|\alpha\|}_{8}^{8}}{{\|\alpha\|}_{6}^{6}}})}}$. When $E_{0}$ happens, we have $\mu \leq {{({d - 1})}{({{\left. \parallel\alpha\parallel \right._{4}^{4} - {3\left. \parallel\alpha\parallel \right.^{2}}} + {3\left. \parallel\alpha\parallel \right._{\infty}^{2}}})}} \leq {{({d - 1})}{({{\left. \parallel\alpha\parallel \right._{4}^{4} - {3\left. \parallel\alpha\parallel \right.^{2}}} + {O{({\deltad})}}})}}$. It follows that Putting Corollary 4.4 and Lemma 4.1 together, we can prove Proposition 3.9.

### Proof of Proposition 3.9

Moreover, when $E_{0}$ happens, we have, For simplicity, Let $Z_{i} = {{({\alpha_{i}^{4} - {3\alpha_{i}^{2}}})}\mathbf{1}{({{|\alpha_{i}|} \leq \tau^{1/4}})}}$, and $Z = {\sum_{i}Z_{i}}$. We observe that $E_{1}$ and $E_{0}$ implies that $Z \geq {{({\gamma - 3})}\sqrt{nd}}$. Let $\gamma' = {\gamma - 3}$. Thus, ${Z^{d}\mathbf{1}{({Z \geq {\gamma'\sqrt{nd}}})}} \leq {{({\sum_{i \in {\lbrack n\rbrack}}{{({\alpha_{i}^{4} - {3\alpha_{i}^{2}}})}\mathbf{1}{({{|\alpha_{i}|} \leq \tau^{1/4}})}}})}^{d}\mathbf{1}{(E_{1})}}$. Then, We have that $Z_{i}$ is a sub-exponential variable with parameter $(\sqrt{41},{{({4 + {o_{\tau}{}}})}\tau^{1/2}})$ (by Lemma B.5). Then by Lemma B.4. ‣ B.1 Sub-exponential random variables ‣ Appendix B Toolbox ‣ On the Optimization Landscape of Tensor Decompositions"), we have that $\sum_{i}Z_{i}$ is sub-exponential with parameters $(\sqrt{41n},{{({4 + {o_{\tau}{}}})}\tau^{1/2}})$. Moreover, we have $Z$ has mean $o_{d}{(n)}$ since $n \geq {d{\log d}}$.

Then, we use Lemma B.13 to control the moments the sub-exponential random variable ${Z \cdot \mathbf{1}}{({{|Z|} \geq {\gamma'\sqrt{nd}}})}$. Taking $s = {\gamma'\sqrt{nd}}$ and $\nu = \sqrt{41n}$ and $b = {{({4 + {o_{\tau}{}}})}\tau^{1/2}}$ in Lemma B.13, we obtain that when when $\gamma' \geq {\max{\{\sqrt{41},{{({1 + \eta})}{({8 + {o_{\tau}{}}})}\sqrt{{\taud}/n}}\}}} = {\max{\{\sqrt{41},{{({1 + \eta})}{({8 + {o_{\tau}{}}})}\sqrt{K}}\}}}$ Take $\varepsilon = {1/{\log d}}$ and $\eta = {1/{\log d}}$, we obtain that Hence, combing equation (4.7), (4.8) and (4.9), we have,

### Proof of Proposition 3.8

In the proof of Proposition 3.8, we will have another division of the the coordinates of $\alpha$ into two subsets $S$ and $L$ according to the magnitude of $\alpha_{i}$'s. Throughout this subsection, let $C$ be a sufficiently large constant that depends on $\delta$. Let $S = {\{ i:{{|\alpha_{i}|} \leq \sqrt{C{\log d}}}\}}$ and $L = {{\lbrack n\rbrack}\backslash S}$. Thus by definition, since $n \geq {d{\log^{2}d}}$, we have that event $F_{k}$ implies that $k \in L$. But we note the threshold $\sqrt{C{\log d}}$ here is smaller than the threshold $\tau = {{Kn}/d}$ for defining event $F_{k}$'s. The key property that we use here is that the set $L$ have cardinality at most $d$ as long as $E_{0}$ happens. This will allows us to bound the contribution of the coordinates in $L$ in a more informative way.

### Claim 4.5

Let $S,L$ are defined as above with $C \geq {2/\delta}$. Suppose $E_{0}$ happens, then we have ${|L|} \leq {{\deltan}/{\log d}}$.

### Proof

Assume for the sake of contradiction that ${|L|} > {{\deltan}/{\log d}}$, then we can pick a subset $L' \subset L$ of size ${\deltan}/{\log d}$ and obtain that ${\parallel\alpha_{L'}\parallel}^{2} \geq {{|L'|}C{\log d}} = {\deltadC} \geq {2d}$ which violates (3.9). ∎ For notational convenience, let $P = {{({2 - {O{(\delta)}}})}\tau^{1/2}d} = {{({2 - {O{(\delta)}}})}\sqrt{Knd}}$. Recall $\alpha_{S}$ is the restriction of vector $\alpha$ to the coordinate set $S$, and ${Q{(\cdot)}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is defined as: Define ${T_{1}{(\alpha)}},{T_{2}{(\alpha)}}$ as Therefore, since ${Q{(\alpha_{S})}} = {{\parallel\alpha_{S}\parallel}_{4}^{4} - {3{\parallel\alpha_{S}\parallel}^{2}}}$ is roughly a random variable with standard deviation $\Theta{(\sqrt{n})}$, for large enough constant $K$, we should think of $T_{1}{(\alpha)}$ and $T_{2}{(\alpha)}$ as exponentially small random variable. The following Lemma is the key of this section, which says that when $F_{0}$ happens, the chance of $M$ being PSD is very small.

### Lemma 4.6

In the setting of Proposition 3.8, let ${T_{1}{(\alpha)}},{T_{2}{(\alpha)}}$ be defined as in (4.10). Then,

### Proof

We assume throughout this proof that $\alpha$ is a fixed vector and that $\alpha$ satisfies $F_{k}$ and $E_{0}$. For simplicity, define $\hat{\tau} = \sqrt{C{\log d}}$.

Let $q = {(\alpha_{1}^{3},\ldots,\alpha_{n}^{3})}^{\top} \in {\mathbb{R}}^{n}$, and $\overline{q} = {q/{\| q\|}}$. Let $z_{1},{\ldotsz_{d - 1}}$ be i.i.d Gaussian random variables in ${\mathbb{R}}^{d}$ with covriance $\mathcal{N}{(0,{\text{Id}_{n} - {\overline{q}{\overline{q}}^{\top}}})}$. Let $Z$ denote the matrix with $z_{i}^{\top}$ as rows and let $v_{j}{({j \in {\lbrack n\rbrack}})}$ denotes the $j$-th column of $Z$. Then, by Claim 4.2, random variable ${(M,\mathbf{1}{(E_{2}')})} \mid g = 0,\alpha)$ has the same joint distribution as $(M',{\mathbf{1}{(E_{2}^{\operatorname{\prime\prime}})}})$ defined below, Then, it suffices to bound from above the quantity ${\Pr\left\lbrack {M' \succeq {0 \land E_{2}^{\operatorname{\prime\prime}}}} \right\rbrack}.$ A technical complication here is that $v_{1},\ldots,v_{n}$ are not independent random variables. We get around this issue by the following "coupling" technique which introduces some additional randomness. Let $\beta \in {\mathcal{N}{(0,\text{Id}_{d - 1})}}$ be a random variable that is independent with all the $v_{i}$'s and define $\overset{\sim}{B} = {{\beta{\overline{q}}^{\top}} + Z}$. We can verify that $\overset{\sim}{B}$ contains independent entries with distribution $\mathcal{N}{}$. Let ${\overset{\sim}{b}}_{1},\ldots,{\overset{\sim}{b}}_{n}$ be the columns of $\overset{\sim}{B}$. Let ${\overline{v}}_{k} = {v_{k}/{\parallel v_{k}\parallel}}$. We have that $M' \succeq 0$ implies that We bound from above ${\overline{v}}_{k}^{\top}M'{\overline{v}}_{k}$ by decomposing it according to the subset $S,L$.

Here $A_{S},A_{L}$ are defined above in equation (4.12). By Claim 4.5, we have ${|L|} \leq {{\deltan}/{\log d}}$. By (3.9) again, we have that $E_{0}$ implies that ${\parallel\alpha_{L}\parallel}^{2} \leq {{({1 + \delta})}d}$. Then, we have ${\parallel\alpha_{L}\parallel}_{4}^{4} \leq {{\max_{i}\alpha_{i}^{2}} \cdot {\parallel\alpha_{L}\parallel}^{2}} \leq {{({1 + \delta})}d{\max_{i}\alpha_{i}^{2}}} = {{({1 + \delta})}d\alpha_{k}^{2}}$. Moreover, when $E_{2}^{\operatorname{\prime\prime}}$ happens, we have that ${\alpha_{k}^{2}{\langle v_{k},{\overline{v}}_{k}\rangle}^{2}} = {\alpha_{k}^{2}{\parallel{\overline{v}}_{k}\parallel}^{2}} \geq {\alpha_{k}^{2}{({1 - \delta})}d}$. Thus, Then combining equation (4.11), (4.12) and (4.13), we have that when $M' \succeq 0$ and $E_{2}^{\operatorname{\prime\prime}}$ both happen, it holds that $A_{S} \geq {{({2 - {O{(d)}}})}\tau^{1/2}d}$.

Next we consider in more detail the random variable $A_{S}$. Define random variable $Y = {{\overline{v}}_{k}^{\top}{\overset{\sim}{B}}_{- k}{{diag}{({(\alpha_{S})}_{- k})}}}$, where ${\overset{\sim}{B}}_{- k}$ is the ${({d - 1})} \times {({n - 1})}$ sub-matrix of $\overset{\sim}{B}$ that excludes the $k$-th column of $\overset{\sim}{B}$, and ${(\alpha_{S})}_{- k}$ is the $n - 1$-dimensional vector that is obtained from removing the $k$-th entry of $\alpha_{S}$. Note that since $k \notin S$, we have that ${\parallel Y\parallel}^{2} = {\sum_{i \in S}{\alpha_{i}^{2}{\langle v_{i},{\overline{v}}_{i}\rangle}^{2}}}$, and $A_{S} = {{\parallel\alpha_{S}\parallel}_{4}^{4} - {3{\parallel Y\parallel}^{2}}}$. Thus our goal next is to understand the distribution of $Y$.

We observe that $Y \mid v_{k}$ is a Gaussian random variable since ${\overset{\sim}{B}}_{k} \mid v_{k}$ is a Gaussian random variable. Let $\ell_{i} \in {\mathbb{R}}^{n - 1}$ denote the $i$-th row of the matrix $\overset{\sim}{B}$. Then $\ell_{1},\ldots,\ell_{d - 1}$ are i.i.d Gaussian random variable with distribution $\mathcal{N}{(0,\text{Id}_{n})}$. Now we consider $\ell_{i} \mid v_{k,i}$, where $v_{k,i}$ is the $i$-th coordinates of vector $v_{k}$. Note that $v_{k,i} = z_{i,k} = {({{({\text{Id} - {\overline{q}{\overline{q}}^{\top}}})}\ell_{i}})}_{k} = {\langle{e_{k} - {{\overline{q}}_{k}\overline{q}}},\ell_{i}\rangle}$ (here $z_{i,k}$ denotes the $k$-th coordinate of $z_{i}$ and $e_{k}$ is the $k$-th natural basis vector in ${\mathbb{R}}^{n}$). Thus, conditioning on $v_{k,i}$ imposes linear constraints on $\ell_{i}$. Let $s_{k} = {e_{k} - {{\overline{q}}_{k}\overline{q}}} \in {\mathbb{R}}^{n}$ and ${\overline{s}}_{k} = {s_{k}/{\parallel s_{k}\parallel}}$. Then $\ell_{i} \mid v_{k,i}$ has covariance $\text{Id}_{n} - {{\overline{s}}_{k}{\overline{s}}_{k}^{\top}}$. Computing the mean of $\ell_{i} \mid v_{k,i}$ will be tedious but fortunately our bound will not be sensitive to it. Now we consider random variable $\ell_{i}' = {{{(\ell_{i})}_{- k}{{diag}{({(\alpha_{S})}_{- k})}}} \mid v_{k,i}}$ in ${\mathbb{R}}^{n - 1}$ where ${(\ell_{i})}_{- k}$ denotes the restriction of $\ell_{i}$ to the subset ${\lbrack n\rbrack}\backslash{\{ k\}}$. Note that $\ell_{i}'$ is precisely a row of ${\overset{\sim}{B}}_{- k}{{diag}{({(\alpha_{S})}_{- k})}}$. We have $\ell_{i}'$ is again a Gaussian random variable and its covariance matrix is $\Sigma = {{{diag}{({(\alpha_{S})}_{- k})}}\left( {\text{Id}_{n} - {{\overline{s}}_{k}{\overline{s}}_{k}^{\top}}} \right)_{{- k},{- k}}{{diag}{({(\alpha_{S})}_{- k})}}}$, where $\left( {\text{Id}_{n} - {{\overline{s}}_{k}{\overline{s}}_{k}^{\top}}} \right)_{{- k},{- k}}$ is the restriction of $\text{Id}_{n} - {{\overline{s}}_{k}{\overline{s}}_{k}^{\top}}$ to the subsets ${({{\lbrack n\rbrack}\backslash{\{ k\}}})} \times {({{\lbrack n\rbrack}\backslash{\{ k\}}})}$. Since $\ell_{i}$'s are independent with each other, we have ${Y^{\top} \mid {\overline{v}}_{k}} = {{\lbrack\ell_{1}',\ldots,\ell_{d - 1}'\rbrack} \cdot {\overline{v}}_{k}}$ is Gaussian random variable with covariance ${{\|{\overline{v}}_{k}\|}^{2}\Sigma} = \Sigma$.

Next we apply Lemma B.7 on random variable $Y^{\top}$ and obtain that $Y^{\top}$ has concentrated norm in the sense that for any choice of $v_{k}$, Recall that $\Sigma = {{{diag}{({(\alpha_{S})}_{- k})}}\left({\text{Id}_{n} - {{\overline{s}}_{k}{\overline{s}}_{k}^{\top}}} \right)_{{- k},{- k}}{{diag}{({(\alpha_{S})}_{- k})}}}$. Therefore, we have ${\text{tr}{(\Sigma)}} = {{\sum_{i \in S}\alpha_{i}^{2}} - {\parallel{{\overline{s}}_{k} \odot {(\alpha_{S})}_{- k}}\parallel}^{2}} \geq {{\sum_{i \in S}\alpha_{i}^{2}} - {\parallel\alpha_{S}\parallel}_{\infty}^{2}} \geq {{\sum_{i \in S}\alpha_{i}^{2}} - {\hat{\tau}}^{1/2}}$. Moreover, we have that ${\parallel\Sigma\parallel} \leq {\parallel\alpha_{S}\parallel}^{2} \leq {\hat{\tau}}^{1/2}$ and ${\text{tr}{(\Sigma^{2})}} \leq {\parallel\alpha_{S}\parallel}_{4}^{4}$. Plugging these into equation (4.14), and using the fact that $A_{S} = {{\parallel\alpha_{S}\parallel}_{4}^{4} - {3{\parallel Y\parallel}^{2}}}$, we have that for any $t \geq 0$, For simplicity, let $P = {{{({2 - {O{(\delta)}}})}\tau^{1/2}d} - {6{\hat{\tau}}^{1/2}}} = {{({2 - {O{(\delta)}} - {o{}}})}\tau^{1/2}d}$ and ${Q{(\alpha)}} = {{\|\alpha_{S}\|}_{4}^{4} - {3{\|\alpha_{S}\|}^{2}}}$. Then we have that suppose $P > {Q{(\alpha)}}$, by taking $t = \frac{{({P - {Q{(\alpha)}}})}^{2}}{36{\parallel\alpha_{S}\parallel}^{2}}$ in equation (4.15), For notational convenience, again we define $T_{3}{(\alpha)}$ and $T_{4}{(\alpha)}$ as, Intuitively, $T_{3}$ and $T_{4}$ are the contribution of the small coordinates and large coordinates to the quantity ${\mathbb{E}{{\lbrack{\text{tr}{(M)}}\rbrack}^{d}p_{g \mid \alpha}{}}} \propto {Q{(\alpha)}{({\parallel\alpha\parallel}_{6}^{6})}^{- {d/2}}}$, which is the central object that we are controlling.

Using Lemma 4.6, we show that bounding $\mathbb{E}\left\lbrack {h{(\alpha)}\mathbf{1}{(F_{k})}} \right\rbrack$ reduces to bounding the second moments of ${T_{1}{(\alpha)}},\ldots,{T_{4}{(\alpha)}}$.

### Lemma 4.7

Let ${T_{1}{(\alpha)}},{T_{2}{(\alpha)}},{T_{3}{(\alpha)}},{T_{4}{(\alpha)}}$ be defined as above. In the setting of Proposition 3.8, we have,

### Proof of Lemma 4.7

By AM-GM inequality (Claim 3.7⁢𝟏⁢(𝑀⪰0)}? ‣ 3.1 Estimating the Kac-Rice formula for the global region ‣ 3 Proof Overview ‣ On the Optimization Landscape of Tensor Decompositions")) we obtain that Here in the last step we used Cauchy-Schwarz inequality. Let $T_{5}{(\alpha)}$ be defined as in equation (4.22), by Corollary 4.4 Then, combining equation (4.23) and (4.5), we obtain that Here the last inequality uses Cauchy-Schwarz inequality and Holder inequality (technically, Lemma B.19 with $\eta = {1/2}$). Using Lemma 4.6, we obtain that Now we have that our final target can be bounded by The next few Lemmas are devoted to controlling the second moments of ${T_{1}{(\alpha)}},\ldots,{T_{4}{(\alpha)}}$. We start off with $T_{3}{(\alpha)}$.

### Lemma 4.8

In the setting of Lemma 4.7, we have,

### Proof

Let $Z = {\left. \parallel\alpha_{S}\parallel \right._{4}^{4} - \left. \parallel\alpha_{S}\parallel \right.^{2}} = {\sum_{i = 1}^{n}{{({\alpha_{i}^{4} - {3\alpha_{i}^{2}}})}\mathbf{1}{({{|\alpha_{i}|} \leq \sqrt{C{\log d}}})}}}$. Then $Z$ is a sub-exponential random variable with parameters $(\sqrt{41n},{4C{\log d}})$ (by Lemma B.5). Moreover, for sufficiently large $C$ (depending on the choice of $\delta$) we have ${|{\mathbb{E}\lbrack Z\rbrack}|} \leq \delta$. Therefore, by Lemma B.10, choosing $\varepsilon = {O{(\delta)}}$, we have Moreover, when $E_{0}$ happens, we have $\left. \parallel\alpha_{S}\parallel \right._{6}^{6} \geq {15{({1 - \delta})}n}$. Hence, Next we control the second moments of $T_{4}{(\alpha)}$.

### Lemma 4.9

In the setting of Lemma 4.7, we have As a direct consequence, we have

### Proof

The next two Lemmas control the second moments of $T_{1}{(\alpha)}$ and $T_{2}{(\alpha)}$.

### Lemma 4.10

In the setting of Lemma 4.7, we have

### Proof

Since $Q{(\alpha_{S})}$ is a sub-exponential random variable with parameters $(\sqrt{41n},{4C{\log d}})$ (by Lemma B.5), we have that (by Lemma B.3. ‣ B.1 Sub-exponential random variables ‣ Appendix B Toolbox ‣ On the Optimization Landscape of Tensor Decompositions"))

### Lemma 4.11

In the setting of Lemma 4.7, we have

### Proof

Similarly to the proof of Lemma 4.10, we have that for $K \geq 400$, it holds that ${\Pr\left\lbrack {{Q{(\alpha)}} \geq {P/2}} \right\rbrack} \leq {(0.1)}^{d}$. Then it follows that Finally using the four Lemmas above and Lemma 4.7, we can prove Proposition 3.8.

### Proof of Proposition 3.8

Using Lemma 4.7, Lemma 4.8, 4.9, 4.10,4.11, we have that

## Local Maxima Near True Components

In this section we show that in the neighborhoods of the $2n$ true components, there are exactly $2n$ local maxima. Recall the set $L_{2}$ was defined to be the set of points $x$ that do not have large correlation with any of the components: We will show that the objective function (1.1) has exactly $2n$ local maxima in the set $L_{2}^{c}$, and they are close to the normalized version of $\pm a_{i}$'s.

Let ${\overline{a}}_{i} = \frac{a_{i}}{\| a_{i}\|}$ be the normalized version of $a_{i}$ on the unit sphere. We prove the following slightly stronger version of Theorem 3.3. (Note that Theorem 3.3 is a straightforward corollary of the Theorem below, since w.h.p, for every $i$, ${\| a_{i}\|} = {\sqrt{d} \pm {\overset{\sim}{O}{}}}$. )

### Theorem 5.1

Suppose ${{({d{\log d}})}/\delta^{2}} \leq n \leq {d^{2}/{\log^{O{}}d}}$. Then, with high probability over the choice $a_{1},\ldots,a_{n}$, Moreover, each of the point in $\mathcal{M}_{f} \cap L \cap L_{2}^{c}$ is $\overset{\sim}{O}{(\sqrt{n/d^{3}})}$-close to one of ${\pm {\overline{a}}_{1}},{\cdots \pm {\overline{a}}_{n}}$.

Towards proving the Theorem, we first show that all the local minima in the set $L_{2}^{c}$ must have at least $0.99$ correlation with one of $\pm {\overline{a}}_{i}$ (see Lemma 5.2). Next we show in each of the regions ${\langle x,{\overline{a}}_{i}\rangle} \geq 0.99$, the objective function is strongly convex with a unique local maximum (see Lemma 5.5).

### Lemma 5.2

In the setting of Theorem 3.3, for any local maximum $x \in L_{2}$, there exists a component $a \in {\{{\pm {\overline{a}}_{i}}\}}$ such that ${\langle x,a\rangle} \geq 0.99$.

We can partition points in $L_{2}$ according to their correlations with the components. We say its largest correlation is the maximum of $|{\langle{\overline{a}}_{i},x\rangle}|$, and second largest correlation is the second largest among $|{\langle{\overline{a}}_{i},x\rangle}|$. For any point $x$ in $L_{2}$, it is in one of the three types 1) the largest correlation is at least $0.99$; 2) the largest correlation is at least $\sqrt{2}$ larger than the second largest correlation; 3) the largest and second largest correlations are within a factor of $\sqrt{2}$. Intuitively, points in case 1 are what we want for the Lemma, points in case 2 will have a nonzero gradient, points in case 3 will not have a negative semidefinite Hessian (hence points in cases 2 and 3 cannot be local maxima). We formalize this intuition in the following proof:

### Proof of Lemma 5.2

Let $c_{i} = {\langle x,{\overline{a}}_{i}\rangle}$, without loss of generality, we can rearrange the $a_{i}$'s so that Let $k$ be the index such that ${|c_{k}|} \geq \frac{\log d}{\sqrt{d}}$ and ${|c_{k + 1}|} < \frac{\log d}{\sqrt{d}}$. We will call components $1,2,\ldots,k$ the large components, and the rest the small components. We assume the following events happen simultaneously (note that, with high probability, all of them are true): $\{ a_{i}\}$'s satisfy the $({{d/\Delta}{\log n}},0.01)$-RIP property for some universal constant $\Delta$. As a direct consequence, $k \ll {d/{\log d}}$ and ${\sum_{i = 1}^{k}c_{i}^{2}} \leq {(1.01)}^{2}$.). (See Definition B.20) For all $i$, we have ${\| a_{i}\|} = {\sqrt{d}{({1 \pm {o{}}})}}$.

For all $i \neq j$, ${|{\langle a_{i},a_{j}\rangle}|} \leq {\sqrt{d}{\log d}}$. As a consequence, we have ${|{\langle{\overline{a}}_{i},{\overline{a}}_{j}\rangle}|} \leq {{({1 + {o{}}})}\frac{\log d}{\sqrt{d}}}$.

Concentration Lemmas B.22, B.23 and B.24 hold.

We aim to show ${|c_{1}|} \geq 0.99$. First, if $0.99 > {|c_{1}|} > {\sqrt{2}{|c_{2}|}}$, we will show the point has nonzero $\text{grad~}f{(x)}$, and hence cannot be a local maximum.

### Claim 5.3

If $0.99 > {|c_{1}|} > {\sqrt{2}{|c_{2}|}}$, then $\frac{| \parallel P_{{\overline{a}}_{1}^{\perp}}\nabla f{(x)} \parallel}{|{\langle{{\nabla f}{(x)}},{\overline{a}}_{1}\rangle}|} < {{\frac{3}{4} \cdot \frac{\|{\Pi_{{\overline{a}}_{1}^{\perp}}x}\|}{|{\langle x,{\overline{a}}_{1}\rangle}|}} + \frac{O{({\sqrt{nd}{\log^{4}d}})}}{{|c_{1}|}^{3}d^{2}}}$, in particular when ${|c_{1}|} \leq 0.99$ we know ${\text{grad~}f{(x)}} \neq 0$.

### Proof

Let $x' = {{\nabla f}{(x)}}$, we know the gradient ${\text{grad~}f{(x)}} = 0$ if and only if $x'$ is a multiple of $x$. Therefore we shall show $x'$ is not a multiple of $x$ by showing $\frac{| \parallel \Pi_{{\overline{a}}_{1}^{\perp}}x' \parallel}{|{\langle x',{\overline{a}}_{1}\rangle}|} > \frac{\|{\Pi_{{\overline{a}}_{1}^{\perp}}x}\|}{|{\langle x,{\overline{a}}_{1}\rangle}|}$. Intuitively, after one step of gradient ascent/power iterations, the point should become more correlated with $\pm a_{1}$.

Since $x' = {\sum_{i = 1}^{n}{4{\langle x,a_{i}\rangle}^{3}a_{i}}}$, we can write $x' = {{4{\langle a_{1},x\rangle}^{3}a_{1}} + x_{L}' + x_{S}'}$, where $x_{L}' = {\sum_{i = 2}^{k}{4{\langle x,a_{i}\rangle}^{3}a_{i}}}$ and $x_{S}' = {\sum_{i = {k + 1}}^{n}{4{\langle x,a_{i}\rangle}^{3}a_{i}}}$. The first term has norm ${(c_{1}^{3})}{({1 \pm {o{}}})}d^{2}$ and is purely in the direction ${\overline{a}}_{1}$. We just need to show the other terms are small. First, we bound $\| x_{S}'\|$ by concentration inequality Lemma B.23: for any vector $x$ we know On the other hand, we have | | $\langle x_{L}',{\overline{a}}_{1}\rangle$ | $= {\sum\limits_{i = 2}^{k}{4{\langle x,a_{i}\rangle}^{3}{\langle a_{i},{\overline{a}}_{1}\rangle}}}$ | | | Therefore $x_{L}'$ does not have large correlation with ${\overline{a}}_{1}$. We can also bound the norm of $\Pi_{{\overline{a}}_{1}^{\perp}}x_{L}'$: by RIP condition we know ${\overline{a}}_{1},\ldots,\overline{a_{k}}$ form an almost orthonormal basis, therefore We know $c_{i} = {{\langle{c_{1}{\overline{a}}_{1}},{\overline{a}}_{i}\rangle} + {\langle{\Pi_{{\overline{a}}_{1}^{\perp}}x},{\overline{a}}_{i}\rangle}}$, by Claim B.18 we know that ${\|{a + b}\|}_{6}^{6} \leq {{1.01{\| a\|}_{6}^{6}} + {O{({\| b\|}_{6}^{6})}}}$, therefore where the last inequality follows from RIP condition as it implies ${\sum_{i = 2}^{k}{\langle{\Pi_{{\overline{a}}_{1}^{\perp}}x},{\overline{a}}_{i}\rangle}^{2}} \leq {1.01{\|{\Pi_{{\overline{a}}_{1}^{\perp}}x}\|}^{2}}$.

Combining these we know Next we show if ${|c_{1}|} \leq {\sqrt{2}{|c_{2}|}}$, then the Hessian $\text{Hess~}f{(x)}$ is not negative semidefinite, hence again $x$ cannot be a local maximum

### Claim 5.4

If ${|c_{1}|} \leq {\sqrt{2}{|c_{2}|}}$, we have ${\sigma_{max}{({\text{Hess~}f{(x)}})}} > 0$.

### Proof

Consider the space spanned by ${\overline{a}}_{1}$ and $\overline{a_{2}}$, this is a two dimensional subspace so there is at least one direction that is orthogonal to $x$. Let $u$ such a direction (${u \in {\text{span}{({\overline{a}}_{1},\overline{a_{2}})}}},{{{\langle u,x\rangle} = 0},{{\| u\|} = 1}}$). By Claim 2.1, we know the Hessian is equal to Clearly, the first term is PSD and the second term is negative. We will consider $u^{\top}\text{Hess~}f{(x)}u$, and break both terms in the Hessian into the sum of large and small components. For the large components, we know $({{c_{1}^{2}{\| a_{1}\|}^{2}a_{1}a_{1}^{\top}} + {c_{2}^{2}{\| a_{2}\|}^{2}a_{2}a_{2}^{\top}}})$ is a matrix that has smallest singular value at least $c_{2}^{2}d^{2}{({1 - {o{}}})}$ in subspace $\text{span}{({\overline{a}}_{1},\overline{a_{2}})}$ because $a_{1}$ and $a_{2}$ are almost orthogonal. Also, $u$ is orthogonal to $x$ so ${P_{x}u} = u$, therefore for large components On the other hand, for the second term, the contribution from large components is smaller For the small components, we only count their contributions to the second term (because the first term is positive anyways), by concentration inequality Lemma B.22, we know with high probability for all $u$ The last inequality is because $c_{2}^{2} \geq {c_{1}^{2}/2} \geq {{\delta^{2}{({1 - {o{}}})}}/2}$ and $n \ll {d^{2}\delta^{2}}$. Therefore, combining all these terms we know Therefore the Hessian is not negative semidefinite, and the point $x$ could not have been a local maximum. ∎ The Lemma follows immediately from the two claims.

### Lemma 5.5

Under the same condition as Theorem 3.3, for all vector $z$ in $\{{\pm {\overline{a}}_{i}}\}$, in the set $\{ x:{{\langle x,z\rangle} \geq 0.99}\}$there is a unique local maximum that is $\overset{\sim}{O}{(\sqrt{n/d^{3}})}$-close to $z$.

The fact that power method converges to a local maximum in this region is proven by Anandkumar et al.. We give the proof for completeness.

### Proof

Without loss of generality we assume ${\langle x,{\overline{a}}_{1}\rangle} \geq 0.99$.

By Claim 5.3, we know for any $x$ in the set $\{ x:{{\langle x,{\overline{a}}_{1}\rangle} \geq 0.99}\}$, $\frac{{\nabla f}{(x)}}{\|{{\nabla f}{(x)}}\|}$ is in the same set. Therefore by Schauder fixed point theorem there is at least a critical point in this set. Again by Claim 5.3 we know every critical point must satisfy $\frac{| \parallel \Pi_{{\overline{a}}_{1}^{\perp}}\nabla f{(x)} \parallel}{|{\langle{{\nabla f}{(x)}},{\overline{a}}_{1}\rangle}|} \leq \frac{O{({\sqrt{nd}{\log^{4}d}})}}{{|c_{1}|}^{3}d^{2}}$. Therefore we only need to prove there is a unique critical point and it is also a local maximum. We do this by showing the Hessian $\text{Hess~}f{(x)}$ is always negative semidefinite in this set.

Again let $c_{i} = {\langle x,{\overline{a}}_{i}\rangle}$ and rearrange the $a_{i}$'s so that Let $k$ be the index such that ${|c_{k}|} \geq \frac{\log d}{\sqrt{d}}$ and ${|c_{k + 1}|} < \frac{\log d}{\sqrt{d}}$. With high probability, we know $\{ a_{i}\}$ satisfy the $({d/4},0.01)$-RIP property. Under RIP condition we know $k \ll {d/{\log d}}$ and ${\sum_{i = 1}^{k}c_{i}^{2}} \leq {({1 + \zeta})}^{2}$. We also condition on event that for all $i$ ${\| a_{i}\|} = {\sqrt{d}{({1 \pm {o{}}})}}$ and for all $i,j$ ${|{\langle a_{i},a_{j}\rangle}|} \leq {\sqrt{d}{\log d}}$ which happens with high probability when $n \geq {d{\log d}}$.

Now consider the Hessian The second term is obviously larger than ${c_{1}^{4}{({1 - {o{}}})}d^{2}} = {{({1 - {o{}}})}d^{2}}$. Therefore we only need to show the spectral norm of the first term is much smaller. We can break the first term into 3 parts: the first component, components 2 to $k$, and components $k + 1$ to $n$. For the first component, we know in the set ${\|{P_{x}a_{1}}\|} \leq {{({1 + {o{}}})}\sqrt{0.02d}}$, so For the second component, Here the last inequality used the fact that $A$ is RIP and therefore $\sum_{i = 2}^{k}{{\overline{a}}_{i}{\overline{a}}_{i}^{\top}}$ cannot have large eigenvalue. Finally for the third component we can bound it directly by concentration inequality Lemma B.24, Taking the sum of these three equations (5.4-5.6), we know $\text{Hess~}f{(x)}$ is always negative semidefinite in the set. Therefore the set can only have a unique critical point which is also a local maximum. ∎

## Conclusion

We analyze the optimization landscape of the random over-complete tensor decomposition problem using the Kac-Rice formula and random matrix theory. We show that in the superlevel set $L$ that contains all the points with function values barely larger than the random guess, there are exactly $2n$ local maxima that correspond to the true components. This implies that with an initialization slight better than the random guess, local search algorithms converge to the desired solutions. We believe our techniques can be extended to 3rd order tensors, or other non-convex problems with structured randomness.

The immediate open question is whether there is any other spurious local maximum outside this superlevel set. Answering it seems to involve solving difficult questions in random matrix theory. Another potential approach to unravel the mystery behind the success of the non-convex methods is to analyze the early stage of local search algorithms and show that they will enter the superlevel set $L$ quickly.
