<!-- arxiv-full-text:v1 {"arxiv_id": "1602.04915", "source": "ar5iv"} -->

## Introduction

Saddle points have long been regarded as a tremendous obstacle for continuous optimization. There are many well known examples when worst case initialization of gradient descent provably converge to saddle points \[20, Section 1.2.3\], and hardness results which show that finding even a *local* minimizer of non-convex functions is NP-Hard in the worst case. However, such worst-case analyses have not daunted practitioners, and high quality solutions of continuous optimization problems are readily found by a variety of simple algorithms. Building on tools from the theory of dynamical systems, this paper demonstrates that, under very mild regularity conditions, saddle points are indeed of little concern for the gradient method.

More precisely, let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be twice continuously differentiable, and consider the classic gradient method with constant step size $\alpha$: We call $x$ a critical point of $f$ if ${{\nabla f}{(x)}} = 0$, and say that $f$ satisfies the strict saddle property if each critical point $x$ of $f$ is either a local minimizer, or a "strict saddle", i.e, ${\nabla^{2}f}{(x)}$ has at least one strictly negative eigenvalue. We prove: > If $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is twice continuously differentiable and satisfies the strict saddle property, then gradient descent (Equation 1) with a random initialization and sufficiently small constant step size converges to a local minimizer or negative infinity almost surely.

Here, by sufficiently small, we simply mean less than the inverse of the Lipschitz constant of the gradient. As we discuss below, such step sizes are standard for the gradient method. We remark that the strict saddle assumption is necessary in the worst case, due to hardness results regarding testing the local optimality of functions whose Hessians are highly degenerate at critical points (e.g, quartic polynomials).

### Related work

Prior work has show that first-order descent methods can circumvent strict saddle points, provided that they are augmented with unbiased noise whose variance is sufficiently large along each direction. For example, establishes convergence of the Robbins-Monro stochastic approximation to local minimizers for strict saddle functions. More recently, give quantitative rates on the convergence of noise-added stochastic gradient descent to local minimizers, for strict saddle functions. The condition that the noise have large variance along all directions is often not satisfied by the randomness which arises in sample-wise or coordinate-wise stochastic updates. In fact, it generally requires that additional, near-isotropic noise be added at each iteration, which yields convergence rates that depend heavily on problem parameters like dimension. In contrast, our results hold for the simplest implementation of gradient descent and thus do not suffer from the slow convergence associated with adding high-variance noise to each iterate.

But is this strict saddle property reasonable? Many works have answered in the affirmative by demonstrating that many objectives of interest do in fact satisfy the "strict saddle" property: PCA, a fourth-order tensor factorization, formulations of dictionary learning and phase retrieval.

To obtain provable guarantees, the authors of and adopt trust-region methods which leverage Hessian information in order to circumvent saddle points. This approach joins a long line of related strategies, including: a modified Newton's method with curvilinear line search, the modified Cholesky method, trust-region methods, and the related cubic regularized Newton's method, to name a few. Specialized to deep learning applications, have introduced a saddle-free Newton method.

Unfortunately, such curvature-based optimization algorithms have a per-iteration computational complexity which scales quadratically or even cubically in the dimension $d$, rendering them unsuitable for optimization of high dimensional functions. In contrast, the complexity of an iteration of gradient descent is linear in dimension. We also remark that the authors of empirically observe gradient descent with $100$ random initializations on the phase retrieval problem reliably converges to a local minimizer, and one whose quality matches that of the solution found using more costly trust-region techniques.

More broadly, many recent works have shown that gradient descent plus smart initialization provably converges to the global minimum for a variety of non-convex problems: such settings include matrix factorization, phase retrieval, dictionary learning, and latent-variable models. While our results only guarantee convergence to local minimizers, they eschew the need for complex and often computationally prohibitive initialization procedures.

Finally, some preliminary results have shown that there are settings in which if an algorithm converges to a saddle point it necessarily has a small objective value. For example, studies the loss surface of a particular Gaussian random field as a proxy for understanding the objective landscape of deep neural nets. The results leverage the Kac-Rice Theorem, and establish that that critical points with more positive eigenvalues have lower expected function value, often close to that of the global minimizer. We remark that functions drawn from this Gaussian random field model share the strict saddle property defined above, and so our results apply in this setting. On the other hand, our results are considerably more general, as they do not place stringent generative assumptions on the objective function $f$.

### Organization

The rest of the paper is organized as follows. Section 2 introduces the notation and definitions used throughout the paper. Section 3 provides an intuitive explanation for why it is unlikely that gradient descent converges to a saddle point, by studying a non-convex quadratic and emphasizing the analogy with power iteration. Section 4 states our main results which guarantee gradient descent converges to only local minimizers, and also establish rates of convergence depending on the local geometry of the minimizer. The primary tool we use is the local stable manifold theorem, accompanied by inversion of gradient descent via the proximal point algorithm. Finally, we conclude in Section 5 by suggesting several directions of future work.

## Preliminaries

Throughout the paper, we will use $f$ to denote a real-valued function in $C^{2}$, the space of twice-continuously differentiable functions, and $g$ to denote the corresponding gradient map with step size $\alpha$, The Jacobian of $g$ is given by ${Dg{(x)}_{ij}} = {\frac{\partial g_{i}}{\partial x_{j}}{(x)}}$, or ${Dg{(x)}} = {I - {\alpha{\nabla^{2}f}{(x)}}}$. In addition to being $C^{2}$, our main regularity assumption on $f$ is that it has a Lipschitz gradient: The $k$-fold composition of the gradient map $g^{k}{(x)}$ corresponds to performing $k$ steps of gradient descent initialized at $x$. The iterates of gradient descent will be denoted $x_{k}:={g^{k}{(x_{0})}}$. All the probability statements are with respect to $\nu$, the distribution of $x_{0}$, which we assume is absolutely continuous with respect to Lebesgue measure.

A fixed point of the gradient map $g$ is a critical point of the function $f$. Critical points can be saddle points, local minima, or local maxima. In this paper, we will study the critical points of $f$ via the fixed points of $g$, and then apply dynamical systems theory to $g$.

### Definition 2.1

A point $x^{\ast}$ is a critical point of $f$ if it is a fixed point of the gradient map ${g{(x^{\ast})}} = x^{\ast}$, or equivalently ${{\nabla f}{(x^{\ast})}} = 0$.

A critical point $x^{\ast}$ is isolated if there is a neighborhood $U$ around $x^{\ast}$, and $x^{\ast}$ is the only critical point in $U$.

A critical point is a local minimum if there is a neighborhood $U$ around $x^{\ast}$ such that ${f{(x^{\ast})}} \leq {f{(x)}}$ for all $x \in U$, and a local maximum if ${f{(x^{\ast})}} \geq {f{(x)}}$.

A critical point is a saddle point if for all neighborhoods $U$ around $x^{\ast}$, there are ${x,y} \in U$ such that ${f{(x)}} \leq {f{(x^{\ast})}} \leq {f{(y)}}$.

As mentioned in the introduction, we will be focused on saddle points that have directions of strictly negative curvature. This notion is made precise by the following definition.

### Definition 2.2 (Strict Saddle)

A critical point $x^{\ast}$ of $f$ is a strict saddle if ${\lambda_{\min}{({{\nabla^{2}f}{(x^{\ast})}})}} < 0$.

Since we are interested in the attraction region of a critical point, we define the stable set.

### Definition 2.3 (Global Stable Set)

The global stable set $W^{s}{(x^{\ast})}$ of a critical point $x^{\ast}$ is the set of initial conditions of gradient descent that converge to $x^{\ast}$:

## Intuition

To illustrate why gradient descent does not converge to saddle points, consider the case of a non-convex quadratic, ${f{(x)}} = {\frac{1}{2}x^{T}Hx}$. Without loss of generality, assume $H = {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(\lambda_{1},\ldots,\lambda_{n})}}$ with ${\lambda_{1},\ldots,\lambda_{k}} > 0$ and ${\lambda_{k + 1},\ldots,\lambda_{n}} < 0$. $x^{\ast} = 0$ is the unique critical point of this function and the Hessian at $x^{\ast}$ is $H$. Note that gradient descent initialized from $x_{0}$ has iterates where $e_{i}$ denote the standard basis vectors. This iteration resembles power iteration with the matrix $I - {\alphaH}$.

The gradient method is guaranteed to converge with a constant step size provided $0 < \alpha < \frac{2}{L}$. For this quadratic $f$, $L$ is equal to $\max{|\lambda_{i}|}$. Suppose $\alpha < {1/L}$, a slightly stronger condition. Then we will have ${({1 - {\alpha\lambda_{i}}})} < 1$ for $i \leq k$ and ${({1 - {\alpha\lambda_{i}}})} > 1$ for $i > k$. If $x_{0} \in E_{s}:={{span}{(e_{1},\ldots,e_{k})}}$, then $x_{k}$ converges to the saddle point at $0$ since ${({1 - {\alpha\lambda_{i}}})}^{k + 1}\rightarrow 0$. However, if $x_{0}$ has a component outside $E_{s}$ then gradient descent diverges to $\infty$. For this simple quadratic function, we see that the global stable set (attractive set) of $0$ is the subspace $E_{s}$. Now, if we choose our initial point at random, the probability of that point landing in $E_{s}$ is zero.

As an example of this phenomena for a non-quadratic function, consider the following example from \[20, Section 1.2.3\]. Letting ${f{(x,y)}} = {{{\frac{1}{2}x^{2}} + {\frac{1}{4}y^{4}}} - {\frac{1}{2}y^{2}}}$, the corresponding gradient mapping is The critical points are The points $z_{2}$ and $z_{3}$ are isolated local minima, and $z_{1}$ is a saddle point.

Gradient descent initialized from any point of the form $\begin{bmatrix} \end{bmatrix}$ converges to the saddle point $z_{1}$. Any other initial point either diverges, or converges to a local minimum, so the stable set of $z_{1}$ is the $x$-axis, which is a zero measure set in $\mathbf{R}^{2}$. By computing the Hessian, we find that ${\nabla^{2}f}{(z_{1})}$ has one positive eigenvalue with eigenvector that spans the $x$-axis, thus agreeing with our above characterization of the stable set. If the initial point is chosen randomly, there is zero probability of initializing on the $x$-axis and thus zero probability of converging to the saddle point $z_{1}$.

In the general case, the local stable set $W_{loc}^{s}{(x^{\ast})}$ of a critical point $x^{\ast}$ is well-approximated by the span of the eigenvectors corresponding to positive eigenvalues. By an application of Taylor's theorem, one can see that if the initial point $x_{0}$ is uniformly random in a small neighborhood around $x^{\ast}$, then the probability of initializing in the span of these eigenvectors is zero whenever there is a negative eigenvalue. Thus, gradient descent initialized at $x_{0}$ will leave the neighborhood. The primary difficulty is that $x_{0}$ is randomly distributed over the entire domain, not a small neighborhood around $x^{\ast}$, and Taylor's theorem does not provide any global guarantees.

However, the global stable set can be found by inverting the gradient map via $g^{- 1}$. Indeed, the global stable set is precisely $\cup_{k = 0}^{\infty}{g^{- k}{({W_{loc}^{s}{(x^{\ast})}})}}$. This follows because if a point $x$ converges to $x^{\ast}$, then for some sufficiently large $k$ it must enter the local stable set. That is, $x$ converges to $x^{\ast}$ if and only if ${g^{k}{(x)}} \in W_{loc}^{s}$ for sufficiently large $k$. If $W_{loc}^{s}{(x^{\ast})}$ is of measure zero, then $g^{- k}{({W_{loc}^{s}{(x^{\ast})}})}$ is also of measure zero, and hence the global stable set is of measure zero. Thus, gradient descent will never converge to $x^{\ast}$ from a random initialization.

In Section 4, we formalize the above arguments by showing the existence of an inverse gradient map. The case of degenerate critical points, critical points with zero eigenvalues, is more delicate; the geometry of the global stable set is no longer characterized by only the number of positive eigenvectors. However in Section 4, we show that if a critical point has at least one negative eigenvalue, then the global stable set is of measure zero.

## Main Results

We now state and prove our main theorem, making our intuition rigorous.

### Theorem 4.1

Let $f$ be a $C^{2}$ function and $x^{\ast}$ be a strict saddle. Assume that $0 < \alpha < \frac{1}{L}$, then That is, the gradient method never converges to saddle points, provided the step size is not chosen aggressively. Greedy methods that use precise line search may still get stuck at stationary points. However, a short-step gradient method will only converge to minimizers.

### Remark 4.2

Note that even for the convex functions method, a constant step size slightly less than $1/L$ is a nearly optimal choice. Indeed, for $\theta < 1$, if one runs the gradient method with step size of $\theta/L$ on a convex function a convergence rate of $O{(\frac{1}{\thetaT})}$ is attained.

### Remark 4.3

When $\lim_{k}x_{k}$ does not exist, the above theorem is trivially true.

To prove Theorem 4.1, our primary tool will be the theory of Invariant Manifolds. Specifically, we will use Stable-Center Manifold theorem developed , which allows for a local characterization of the stable set. Recall that a map $g:{X\rightarrow Y}$ is a diffeomorphism if $g$ is a bijection, and $g$ and $g^{- 1}$ are continuously differentiable.

### Theorem 4.4 (Theorem III.7, )

Let $0$ be a fixed point for the $C^{r}$ local diffeomorphism $\phi:{U\rightarrow E}$, where $U$ is a neighborhood of $0$ in the Banach space $E$. Suppose that $E = {E_{s} \oplus E_{u}}$, where $E_{s}$ is the span of the eigenvectors corresponding to eigenvalues less than or equal to $1$ of $D\phi{}$, and $E_{u}$ is the span of the eigenvectors corresponding to eigenvalues greater than $1$ of $D\phi{}$. Then there exists a $C^{r}$ embedded disk $W_{loc}^{cs}$ that is tangent to $E_{s}$ at $0$ called the *local stable center manifold*. Moreover, there exists a neighborhood $B$ of $0$, such that ${{\phi{(W_{loc}^{cs})}} \cap B} \subset W_{loc}^{cs}$, and ${\cap_{k = 0}^{\infty}{\phi^{- k}{(B)}}} \subset W_{loc}^{cs}$.

To unpack all of this terminology, what the stable manifold theorem says is that if there is a map that diffeomorphically deforms a neighborhood of a critical point, then this implies the existence of a local stable center manifold $W_{loc}^{cs}$ containing the critical point. This manifold has dimension equal to the number of eigenvalues of the Jacobian of the critical point that are less than $1$. $W_{loc}^{sc}$ contains all points that are locally forward non-escaping meaning, in a smaller neighborhood $B$, a point converges to $x^{\ast}$ after iterating $\phi$ only if it is in $W_{loc}^{cs} \cap B$.

Relating this back to the gradient method, replace $\phi$ with our gradient map $g$ and let $x^{\ast}$ be a strict saddle point. We first record a very useful fact:

### Proposition 4.5

The gradient mapping $g$ with step size $\alpha < \frac{1}{L}$ is a diffeomorphism.

We will prove this proposition below. But let us first continue to apply the stable manifold theorem. Note that ${Dg{(x)}} = {I - {\alpha{\nabla^{2}f}{(x)}}}$. Thus, the set $W_{loc}^{cs}$ is a manifold of dimension equal to the number of non-negative eigenvalues of the ${\nabla^{2}f}{(x)}$. Note that by the strict saddle assumption, this manifold has strictly positive codimension and hence has measure zero.

Let $B$ be the neighborhood of $x^{\ast}$ promised by the Stable Manifold Theorem. If $x$ converges to $x^{\ast}$ under the gradient map, then there exists a $T$ such that ${g^{t}{(x)}} \in B$ for all $t \geq T$. This means that ${g^{t}{(x)}} \in {\cap_{k = 0}^{\infty}{g^{- k}{(B)}}}$, and hence, ${g^{t}{(x)}} \in W_{loc}^{cs}$. That is, we have shown that Since diffeomorphisms map sets of measure zero to sets of measure zero, and countable unions of measure zero sets have measure zero, we conclude that $W^{s}$ has measure zero. That is, we have proven Theorem 4.1.

### Proof of Proposition 4.5

We first check that $g$ is injective from $\mathbf{R}^{n}\rightarrow\mathbf{R}^{n}$ for $\alpha < \frac{1}{L}$. Suppose that there exist $x$ and $y$ such that ${g{(x)}} = {g{(y)}}$. Then we would have ${x - y} = {\alpha{({{{\nabla f}{(x)}} - {{\nabla f}{(y)}}})}}$ and hence Since ${\alphaL} < 1$, this means $x = y$.

To show the gradient map is surjective, we will construct an explicit inverse function. The inverse of the gradient mapping is given by performing the proximal point algorithm on the function $- f$. The proximal point mapping of $- f$ centered at $y$ is given by For $\alpha < \frac{1}{L}$, the function above is strongly convex with respect to $x$, so there is a unique minimizer. Let $x_{y}$ be the unique minimizer, then by KKT conditions, Hence, $x_{y}$ is mapped to $y$ by the gradient map.

We have already shown that $g$ is a bijection, and continuously differentiable. Since ${Dg{(x)}} = {I - {\alpha{\nabla^{2}f}{(x)}}}$ is invertible for $\alpha < \frac{1}{L}$, the inverse function theorem guarantees $g^{- 1}$ is continuously differentiable, completing the proof that $g$ is a diffeomorphism.

### Further consequences of Theorem 4.1

### Corollary 4.6

Let $C$ be the set of saddle points and assume they are all strict. If $C$ has at most countably infinite cardinality, then

### Proof

By applying Corollary 4.1 to each point $x^{\ast} \in C$, we have that ${\Pr{({{\lim_{k}x_{k}} = x^{\ast}})}} = 0$. Since the critical points are countable, the conclusion follows since countable union of null sets is a null set. ∎

### Remark 4.7

If the saddle points are isolated points, then the set of saddle points is at most countably infinite.

### Theorem 4.8

Assume the same conditions as Theorem 4.6 and $\lim_{k}x_{k}$ exists, thien ${\Pr{({{\lim_{k}x_{k}} = x^{\star}})}} = 1$, where $x^{\star}$ is a local minimizer.

### Proof

Using the previous theorem, ${\Pr{({{\lim_{k}x_{k}} \in C})}} = 0$. Since $\lim_{k}x_{k}$ exists and there is zero probability of converging to a saddle, then ${\Pr{({{\lim_{k}x_{k}} = x^{\ast}})}} = 1$, where $x^{\ast}$ is a local minimizer. ∎ We now discuss two sufficient conditions for $\lim_{k}x_{k}$ to exist. The following proposition prevents $x_{k}$ from escaping to $\infty$, by enforcing that $f$ has compact sublevel sets, $\{ x:{{f{(x)}} \leq c}\}$. This is true for any coercive function, ${\lim_{{\| x\|}\rightarrow\infty}{f{(x)}}} = \infty$, which holds in most machine learning applications since $f$ is usually a loss function.

### Proposition 4.9 (Proposition 12.4.4 of )

Assume that $f$ is continuously differentiable, has isolated critical points, and compact sublevel sets, then $\lim_{k}x_{k}$ exists and that limit is a critical point of $f$.

The second sufficient condition for $\lim_{k}x_{k}$ to exist is based on the Lojasiewicz gradient inequality, which characterizes the steepness of the gradient near a critical point. The Lojasiewicz inequality ensures that the length traveled by the iterates of gradient descent is finite. This will also allow us to derive rates of convergence to a local minimum.

### Definition 4.10 (Lojasiewicz Gradient Inequality)

A critical point $x^{\ast}$ is satisfies the Lojasiewicz gradient inequality if there exists a neighborhood $U$, ${m,\epsilon} > 0$, and $0 \leq a < 1$ such that for all x in $\{{x \in U}:{{f{(x^{\ast})}} < {f{(x)}} < {{f{(x^{\ast})}} + \epsilon}}\}$.

The Lojasiewicz inequality is very general as discussed . In fact every analytic function satisfies the Lojasiewicz inequality. Also if the solution is $\mu$-strongly convex in a neighborhood, then the Lojasiewicz inequality is satisfied with parameters $a = \frac{1}{2}$, and $m = \sqrt{2\mu}$.

### Proposition 4.11

Assume the same conditions as Theorem 4.6, and the iterates do not escape to $\infty$, meaning $\{ x_{k}\}$ is a bounded sequence. Then $\lim_{k}x_{k}$ exists and ${\lim_{k}x_{k}} = x^{\ast}$ for a local minimum $x^{\ast}$.

Furthermore if $x^{\ast}$ satisfies the Lojasiewicz gradient inequality for $0 < a \leq \frac{1}{2}$, then for some $C$ and $b < 1$ independent of $k$,

### Proof

The first part of the theorem follows , which shows that $\lim_{k}x_{k}$ exists. By Theorem 4.8, $\lim_{k}x_{k}$ is a local minimizer $x^{\ast}$. Without loss of generality, we may assume that ${f{(x^{\ast})}} = 0$ by shifting the function.

Define $e_{k} = {\sum_{j = k}^{\infty}\left\| {x_{j + 1} - x_{j}} \right\|}$, and since $e_{k} \geq \left\| {x_{k} - x^{\ast}} \right\|$ it suffices to upper bound $e_{k}$.

Since we have established that $x_{k}$ converges, for $k$ large enough we can use the gradient inequality and ${{\nabla f}{(x_{k})}} = \frac{x_{k} - x_{k + 1}}{\alpha}$: Define $\beta = \frac{2}{{({m\alpha})}^{1/a}{({1 - a})}}$ and $d = \frac{a}{1 - a}$. First consider the case $0 \leq a \leq \frac{1}{2}$, then $d \leq 1$. Thus, where the last inequality uses $e_{k} < 1$ and $d \leq 1$.

For $\frac{1}{2} < a < 1$, we have established $e_{k + 1} \leq {e_{k} - {\frac{1}{\beta^{d}}e_{k}^{d}}}$. We show by induction that $e_{k + 1} \leq \frac{C}{{({k + 1})}^{{({1 - a})}/{({{2a} - 1})}}}$. The inductive hypothesis guarantees us $e_{k} \leq \frac{C}{k^{{({1 - a})}/{({{2a} - 1})}}}$, so

## Conclusion

We have shown that gradient descent with random initialization and appropriate constant step size does not converge to a saddle point. Our analysis relies on a characterization of the local stable set from the theory of invariant manifolds. The geometric characterization is not specific to the gradient descent algorithm. To use Theorem 4.1, we simply need the update step of the algorithm to be a diffeomorphism. For example if $g$ is the mapping induced by the proximal point algorithm, then $g$ is a diffeomorphism with inverse given by gradient ascent on $- f$. Thus the results in Section 4 also apply to the proximal point algorithm. That is, *the proximal point algorithm does not converge to saddles*. We expect that similar arguments can be used to show ADMM, mirror descent and coordinate descent do not converge to saddle points under appropriate choices of step size. Indeed, convergence to minimizers has been empirically observed for the ADMM algorithm.

It is not clear if the step size restriction ($\alpha < {1/L}$) is necessary to avoid saddle points. Most of the constructions where the gradient method converges to saddle points require fragile initial conditions as discussed in Section 3. It remains a possibility that methods that choose step sizes greedily, by Wolfe Line Search or backtracking, may still avoid saddle points provided the initial point is chosen at random. We leave such investigations for future work.

Another important piece of future work would be relaxing the conditions on isolated saddle points. It is possible that for the structured problems that arise in machine learning, whether in matrix factorization or convolutional neural networks, that saddle points are isolated after taking a quotient with respect to the associated symmetry group of the problem. Techniques from dynamical systems on manifolds may be applicable to understand the behavior of optimization algorithms on problems with a high degree of symmetry.

It is also important to understand how stringent the strict saddle assumption is. Will a perturbation of a function always satisfy the strict saddle property? provide very general sufficient conditions for a random function to be Morse, meaning the eigenvalues at critical points are non-zero, which implies the strict saddle condition. These conditions rely on checking the density of ${\nabla^{2}f}{(x)}$ has full support conditioned on the event that ${{\nabla f}{(x)}} = 0$. This can be explicitly verified for functions $f$ that arise from learning problems.

However, we note that there are very difficult unconstrained optimization problems where the strict saddle condition fails. Perhaps the simplest is optimization of quartic polynomials. Indeed, checking if $0$ is a local minimizer of the quartic is equivalent to checking whether the matrix $Q = {\lbrack q_{ij}\rbrack}$ is co-positive, a co-NP complete problem. For this $f$, the Hessian at $x = 0$ is zero. Interestingly, the strict saddle property failing is analogous in dynamical systems to the existence of a *slow manifold* where complex dynamics may emerge. Slow manifolds give rise to metastability, bifurcation, and other chaotic dynamics, and it would be intriguing to see how the analysis of chaotic systems could be applied to understand the behavior of optimization algorithms around these difficult critical points.
