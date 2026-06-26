<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient Descent Converges to Minimizers

Topics include Gradient descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that gradient descent converges to a local minimizer, almost surely with random initialization. This is proved by applying the Stable Manifold Theorem from dynamical systems theory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Saddle points have long been regarded as a tremendous obstacle for continuous optimization. There are many well known examples when worst case initialization of gradient descent provably converge to saddle points \[20, Section 1.2.3\], and hardness results which show that finding even a *local* minimizer of non-convex functions is NP-Hard in the worst case. However, such worst-case analyses have not daunted practitioners, and high quality solutions of continuous optimization problems are readily found by a variety of simple algorithms. Building on tools from the theory of dynamical systems, this paper demonstrates that, under very mild regularity conditions, saddle points are indeed of little concern for the gradient method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

More precisely, let $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be twice continuously differentiable, and consider the classic gradient method with constant step size $\alpha$: We call $x$ a critical point of $f$ if ${{\nabla f}{(x)}} = 0$, and say that $f$ satisfies the strict saddle property if each critical point $x$ of $f$ is either a local minimizer, or a "strict saddle", i.e, ${\nabla^{2}f}{(x)}$ has at least one strictly negative eigenvalue. We prove: > If $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is twice continuously differentiable and satisfies the strict saddle property, then gradient descent (Equation 1) with a random initialization and sufficiently small constant step size converges to a local minimizer or negative infinity almost surely.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, by sufficiently small, we simply mean less than the inverse of the Lipschitz constant of the gradient. As we discuss below, such step sizes are standard for the gradient method. We remark that the strict saddle assumption is necessary in the worst case, due to hardness results regarding testing the local optimality of functions whose Hessians are highly degenerate at critical points (e.g, quartic polynomials).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Organization", "weight": 1.0} -->

The rest of the paper is organized as follows. Section 2 introduces the notation and definitions used throughout the paper. Section 3 provides an intuitive explanation for why it is unlikely that gradient descent converges to a saddle point, by studying a non-convex quadratic and emphasizing the analogy with power iteration. Section 4 states our main results which guarantee gradient descent converges to only local minimizers, and also establish rates of convergence depending on the local geometry of the minimizer. The primary tool we use is the local stable manifold theorem, accompanied by inversion of gradient descent via the proximal point algorithm. Finally, we conclude in Section 5 by suggesting several directions of future work.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Intuition", "weight": 1.0} -->

To illustrate why gradient descent does not converge to saddle points, consider the case of a non-convex quadratic, ${f{(x)}} = {\frac{1}{2}x^{T}Hx}$. Without loss of generality, assume $H = {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(\lambda_{1},\ldots,\lambda_{n})}}$ with ${\lambda_{1},\ldots,\lambda_{k}} > 0$ and ${\lambda_{k + 1},\ldots,\lambda_{n}} < 0$. $x^{\ast} = 0$ is the unique critical point of this function and the Hessian at $x^{\ast}$ is $H$. Note that gradient descent initialized from $x_{0}$ has iterates where $e_{i}$ denote the standard basis vectors.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Intuition", "weight": 1.0} -->

This iteration resembles power iteration with the matrix $I - {\alphaH}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Intuition", "weight": 1.0} -->

However, if $x_{0}$ has a component outside $E_{s}$ then gradient descent diverges to $\infty$. For this simple quadratic function, we see that the global stable set (attractive set) of $0$ is the subspace $E_{s}$. Now, if we choose our initial point at random, the probability of that point landing in $E_{s}$ is zero.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Intuition", "weight": 1.0} -->

As an example of this phenomena for a non-quadratic function, consider the following example from \[20, Section 1.2.3\]. Letting ${f{(x,y)}} = {{{\frac{1}{2}x^{2}} + {\frac{1}{4}y^{4}}} - {\frac{1}{2}y^{2}}}$, the corresponding gradient mapping is The critical points are The points $z_{2}$ and $z_{3}$ are isolated local minima, and $z_{1}$ is a saddle point.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Intuition", "weight": 1.0} -->

Gradient descent initialized from any point of the form $\begin{bmatrix} \end{bmatrix}$ converges to the saddle point $z_{1}$. Any other initial point either diverges, or converges to a local minimum, so the stable set of $z_{1}$ is the $x$-axis, which is a zero measure set in $\mathbf{R}^{2}$. By computing the Hessian, we find that ${\nabla^{2}f}{(z_{1})}$ has one positive eigenvalue with eigenvector that spans the $x$-axis, thus agreeing with our above characterization of the stable set. If the initial point is chosen randomly, there is zero probability of initializing on the $x$-axis and thus zero probability of converging to the saddle point $z_{1}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Intuition", "weight": 1.0} -->

In the general case, the local stable set $W_{loc}^{s}{(x^{\ast})}$ of a critical point $x^{\ast}$ is well-approximated by the span of the eigenvectors corresponding to positive eigenvalues. By an application of Taylor's theorem, one can see that if the initial point $x_{0}$ is uniformly random in a small neighborhood around $x^{\ast}$, then the probability of initializing in the span of these eigenvectors is zero whenever there is a negative eigenvalue. Thus, gradient descent initialized at $x_{0}$ will leave the neighborhood. The primary difficulty is that $x_{0}$ is randomly distributed over the entire domain, not a small neighborhood around $x^{\ast}$, and Taylor's theorem does not provide any global guarantees.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Intuition", "weight": 1.0} -->

However, the global stable set can be found by inverting the gradient map via $g^{- 1}$. Indeed, the global stable set is precisely $\cup_{k = 0}^{\infty}{g^{- k}{({W_{loc}^{s}{(x^{\ast})}})}}$. This follows because if a point $x$ converges to $x^{\ast}$, then for some sufficiently large $k$ it must enter the local stable set. That is, $x$ converges to $x^{\ast}$ if and only if ${g^{k}{(x)}} \in W_{loc}^{s}$ for sufficiently large $k$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Intuition", "weight": 1.0} -->

If $W_{loc}^{s}{(x^{\ast})}$ is of measure zero, then $g^{- k}{({W_{loc}^{s}{(x^{\ast})}})}$ is also of measure zero, and hence the global stable set is of measure zero. Thus, gradient descent will never converge to $x^{\ast}$ from a random initialization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Intuition", "weight": 1.0} -->

In Section 4, we formalize the above arguments by showing the existence of an inverse gradient map. The case of degenerate critical points, critical points with zero eigenvalues, is more delicate; the geometry of the global stable set is no longer characterized by only the number of positive eigenvectors. However in Section 4, we show that if a critical point has at least one negative eigenvalue, then the global stable set is of measure zero.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Results", "weight": 1.0} -->

We now state and prove our main theorem, making our intuition rigorous.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Note that even for the convex functions method, a constant step size slightly less than $1/L$ is a nearly optimal choice. Indeed, for $\theta < 1$, if one runs the gradient method with step size of $\theta/L$ on a convex function a convergence rate of $O{(\frac{1}{\thetaT})}$ is attained.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 4.3", "weight": 1.0} -->

When $\lim_{k}x_{k}$ does not exist, the above theorem is trivially true.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 4.3", "weight": 1.0} -->

To prove Theorem 4.1, our primary tool will be the theory of Invariant Manifolds. Specifically, we will use Stable-Center Manifold theorem developed, which allows for a local characterization of the stable set. Recall that a map $g:{X\rightarrow Y}$ is a diffeomorphism if $g$ is a bijection, and $g$ and $g^{- 1}$ are continuously differentiable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 4.7", "weight": 1.0} -->

If the saddle points are isolated points, then the set of saddle points is at most countably infinite.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have shown that gradient descent with random initialization and appropriate constant step size does not converge to a saddle point. Our analysis relies on a characterization of the local stable set from the theory of invariant manifolds. The geometric characterization is not specific to the gradient descent algorithm. To use Theorem 4.1, we simply need the update step of the algorithm to be a diffeomorphism. For example if $g$ is the mapping induced by the proximal point algorithm, then $g$ is a diffeomorphism with inverse given by gradient ascent on $- f$. Thus the results in Section 4 also apply to the proximal point algorithm. That is, *the proximal point algorithm does not converge to saddles*. We expect that similar arguments can be used to show ADMM, mirror descent and coordinate descent do not converge to saddle points under appropriate choices of step size. Indeed, convergence to minimizers has been empirically observed for the ADMM algorithm.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Conclusion", "weight": 1.5} -->

It is not clear if the step size restriction ($\alpha < {1/L}$) is necessary to avoid saddle points. Most of the constructions where the gradient method converges to saddle points require fragile initial conditions as discussed in Section 3. It remains a possibility that methods that choose step sizes greedily, by Wolfe Line Search or backtracking, may still avoid saddle points provided the initial point is chosen at random. We leave such investigations for future work.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Another important piece of future work would be relaxing the conditions on isolated saddle points. It is possible that for the structured problems that arise in machine learning, whether in matrix factorization or convolutional neural networks, that saddle points are isolated after taking a quotient with respect to the associated symmetry group of the problem. Techniques from dynamical systems on manifolds may be applicable to understand the behavior of optimization algorithms on problems with a high degree of symmetry.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conclusion", "weight": 1.5} -->

It is also important to understand how stringent the strict saddle assumption is. Will a perturbation of a function always satisfy the strict saddle property? provide very general sufficient conditions for a random function to be Morse, meaning the eigenvalues at critical points are non-zero, which implies the strict saddle condition. These conditions rely on checking the density of ${\nabla^{2}f}{(x)}$ has full support conditioned on the event that ${{\nabla f}{(x)}} = 0$. This can be explicitly verified for functions $f$ that arise from learning problems.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conclusion", "weight": 1.5} -->

However, we note that there are very difficult unconstrained optimization problems where the strict saddle condition fails. Perhaps the simplest is optimization of quartic polynomials. Indeed, checking if $0$ is a local minimizer of the quartic is equivalent to checking whether the matrix $Q = {\lbrack q_{ij}\rbrack}$ is co-positive, a co-NP complete problem. For this $f$, the Hessian at $x = 0$ is zero. Interestingly, the strict saddle property failing is analogous in dynamical systems to the existence of a *slow manifold* where complex dynamics may emerge. Slow manifolds give rise to metastability, bifurcation, and other chaotic dynamics, and it would be intriguing to see how the analysis of chaotic systems could be applied to understand the behavior of optimization algorithms around these difficult critical points.
