<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Escaping from Saddle Points on Riemannian Manifolds

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider minimizing a nonconvex, smooth function f on a Riemannian manifold M. We show that a perturbed version of Riemannian gradient descent algorithm converges to a second-order stationary point (and hence is able to escape saddle points on the manifold). The rate of convergence depends as 1/epsilon^ on the accuracy epsilon, which matches a rate known only for unconstrained smooth minimization. The convergence rate depends polylogarithmically on the manifold dimension d, hence is almost dimension-free. The rate also has a polynomial dependence on the parameters describing the curvature of the manifold and the smoothness of the function. While the unconstrained problem (Euclidean setting) is well-studied, our result is the first to prove such a rate for nonconvex, manifold-constrained problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider minimizing a non-convex smooth function on a smooth manifold $\mathcal{M}$, where $\mathcal{M}$ is a $d$-dimensional smooth manifold^11^1Here $d$ is the dimension of the manifold itself; we do not consider $\mathcal{M}$ as a submanifold of a higher dimensional space. For instance, if $\mathcal{M}$ is a 2-dimensional sphere embedded in ${\mathbb{R}}^{3}$, its dimension is $d = 2$., and $f$ is twice differentiable, with a Hessian that is $\rho$-Lipschitz (assumptions are formalized in section 4). This framework includes a wide range of fundamental problems (often non-convex), such as PCA, dictionary learning, low rank matrix completion, and tensor factorization. Finding the global minimum to Eq. is in general NP-hard; our goal is to find an approximate second order stationary point with first order optimization methods. We are interested in first-order methods because they are extremely prevalent in machine learning, partly because computing Hessians is often too costly.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is then important to understand how first-order methods fare when applied to nonconvex problems, and there has been a wave of recent interest on this topic since, as reviewed below.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the Euclidean space, it is known that with random initialization, gradient descent avoids saddle points asymptotically. Lee et al. (section 5.5) show that this is also true on smooth manifolds, although the result is expressed in terms of nonstandard manifold smoothness measures. Also, importantly, this line of work does not give quantitative rates for the algorithm's behaviour near saddle points.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Du et al. show gradient descent can be *exponentially slow* in the presence of saddle points. To alleviate this phenomenon, it is shown that for a $\beta$-gradient Lipschitz, $\rho$-Hessian Lipschitz function, cubic regularization and perturbed gradient descent converges to $(\epsilon,{- \sqrt{\rho\epsilon}})$ local minimum ^22^2defined as $x$ satisfying ${\|{{\nabla f}{(x)}}\|} \leq \epsilon$, ${\lambda_{\min}{\nabla^{2}f}{(x)}} \geq {- \sqrt{\rho\epsilon}}$ in polynomial time, and momentum based method accelerates. Much less is known about inequality constraints: Nouiehed et al. and Mokhtari et al. discuss second order convergence for general inequality-constrained problems, where they need an NP-hard subproblem (checking the co-positivity of a matrix) to admit a polynomial time approximation algorithm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However such an approximation exists only under very restrictive assumptions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An orthogonal line of work is optimization on Riemannian manifolds. Absil et al. provide comprehensive background, showing how algorithms such as gradient descent, Newton and trust region methods can be implemented on Riemannian manifolds, together with asymptotic convergence guarantees to first order stationary points. Zhang & Sra provide global convergence guarantees for first order methods when optimizing geodesically convex functions. Bonnabel obtains the first asymptotic convergence result for stochastic gradient descent in this setting, which is further extended by Tripuraneni et al.; Zhang et al.; Khuzani & Li. If the problem is non-convex, or the Riemannian Hessian is not positive definite, one can use second order methods to escape from saddle points. Boumal et al. shows that Riemannian trust region method converges to a second order stationary point in polynomial time. But this method requires a Hessian oracle, whose complexity is $d$ times more than computing gradient. In Euclidean space, trust region subproblem can be sometimes solved via a Hessian-vector product oracle, whose complexity is about the same as computing gradients.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Agarwal et al. discuss its implementation on Riemannian manifolds, but not clear about the complexity and sensitivity of Hessian vector product oracle on manifold.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The study of the convergence of gradient descent for non-convex Riemannian problems is previously done only in the Euclidean space by modeling the manifold with equality constraints. Ge et al. prove that stochastic projected gradient descent methods converge to second order stationary points in polynomial time (here the analysis is not geometric, and depends on the algebraic representation of the equality constraints). Sun & Fazel proves perturbed projected gradient descent converges with a comparable rate to the unconstrained setting (polylog in dimension). The paper applies projections from the ambient Euclidean space to the manifold and analyzes the iterations under the Euclidean metric. This approach loses the geometric perspective enabled by Riemannian optimization, and cannot explain convergence rates in terms of inherent quantities such as the sectional curvature of the manifold.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

After finishing this work, we found the recent and independent paper Criscitiello & Boumal which gives a similar convergence analysis result for a related perturbed Riemannian gradient method. We point out a few differences: In Criscitiello & Boumal Lipschitz assumptions are made on the pullback map $f \circ {Retr}$. While this makes the analysis simpler, it lumps the properties of the function and the manifold together, and the role of the manifold's curvature is not explicit. In contrast, our rates are expressed in terms of the function's smoothness parameters and the sectional curvature of the manifold separately, capturing the geometry more clearly. The algorithm in Criscitiello & Boumal uses two types of iterates (some on the manifold but some taken on a tangent space), whereas all our algorithm steps are directly on the manifold, which is more natural. To connect our iterations with intrinsic parameters of the manifold, we use the exponential map instead of the more general retraction used in Criscitiello & Boumal.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We provide convergence guarantees for perturbed first order Riemannian optimization methods to second-order stationary points (local minimum). We prove that as long as the function is appropriately smooth and the manifold has bounded sectional curvature, a perturbed Riemannian gradient descent algorithm escapes (an approximate) saddle points with a rate of $1/\epsilon^{2}$, a polylog dependence on the dimension of the manifold (hence almost dimension-free), and a polynomial dependence on the smoothness and curvature parameters. This is the first result showing such a rate for Riemannian optimization, and the first to relate the rate to geometric parameters of the manifold.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite analogies with the unconstrained (Euclidean) analysis and with the Riemannian optimization literature, the technical challenge in our proof goes beyond combining two lines of work: we need to analyze the interaction between the first-order method and the second order structure of the manifold to obtain second-order convergence guarantees that depend on the manifold curvature. Unlike in Euclidean space, the curvature affects the Taylor approximation of gradient steps. On the other hand, unlike in the local rate analysis in first-order Riemannian optimization, our second-order analysis requires more refined properties of the manifold structure (whereas in prior work, first order oracle makes enough progress for a local convergence rate proof, see Lemma 1), and second order algorithms such as use second order oracles (Hessian evaluation). See section 4 for further discussion.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Perturbed Riemannian gradient algorithm", "weight": 1.0} -->

Our main Algorithm 1 runs as follows: Check the norm of the gradient: If it is large, do one step of Riemannian gradient descent, consequently the function value decreases.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Perturbed Riemannian gradient algorithm", "weight": 1.0} -->

If the norm of gradient is small, it's either an approximate saddle point or a local minimum. Perturb the variable by adding an appropriate level of noise in its tangent space, map it back to the manifold and run a few iterations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Perturbed Riemannian gradient algorithm", "weight": 1.0} -->

If the function value decreases, iterates are escaping from the approximate saddle point (and the algorithm continues) If the function value does not decrease, then it is an approximate local minimum (the algorithm terminates).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Perturbed Riemannian gradient algorithm", "weight": 1.0} -->

0: Initial point x0 ∈ ℳ, parameters β, ρ, K, ℑ, accuracy ϵ, probability of success δ (parameters defined in Assumptions 1, 2, 3 and assumption of Theorem 1).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Perturbed Riemannian gradient algorithm", "weight": 1.0} -->

if ∥grad f (xt)∥ ≤ gthres and t − tnoise > tthres then tnoise ← t, ${\overset{\sim}{x}}_{t}\leftarrow x_{t}$, xt ← Expxt (ξt), ξt uniformly sampled from 𝔹xt (r) ⊂ 𝒯x ℳ.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Perturbed Riemannian gradient algorithm", "weight": 1.0} -->

We refer readers to Lee for the exponential map of sphere and hyperbolic manifolds, and Absil et al. for the Stiefel and Grassmann manifolds. If the exponential map is not computable, the algorithm can use a retraction^44^4A retraction is a first-order approximation of the exponential map which is often easier to compute. instead, however our current analysis only covers the case of the exponential map. In Figure 1, we illustrate a function with saddle point on sphere, and plot the trajectory of Algorithm 1 when it is initialized at a saddle point.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main theorem: escape rate for perturbed Riemannian gradient descent", "weight": 1.0} -->

We now turn to our main results, beginning with our assumptions and a statement of our main theorem. We then develop a brief proof sketch.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main theorem: escape rate for perturbed Riemannian gradient descent", "weight": 1.0} -->

Our main result involves two conditions on function $f$ and one on the curvature of the manifold $\mathcal{M}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1 (Lipschitz gradient)", "weight": 1.0} -->

There is a finite constant $\beta$ such that

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2 (Lipschitz Hessian)", "weight": 1.0} -->

There is a finite constant $\rho$ such that

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3 (Bounded sectional curvature)", "weight": 1.0} -->

There is a finite constant $K$ such that $K$ is an intrinsic parameter of the manifold capturing the curvature. We list a few examples here: (i) A sphere of radius $R$ has a constant sectional curvature $K = {1/R^{2}}$. If the radius is bigger, $K$ is smaller which means the sphere is less curved; (ii) A hyper-bolic space $H_{R}^{n}$ of radius $R$ has $K = {- {1/R^{2}}}$; (iii) For sectional curvature of the Stiefel and the Grasmann manifolds, we refer readers to Rapcsák and Wong, respectively.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3 (Bounded sectional curvature)", "weight": 1.0} -->

Note that the constant $K$ is not directly related to the RLICQ parameter $R$ defined by Ge et al. which first requires describing the manifold by equality constraints. Different representations of the same manifold could lead to different curvature bounds, while sectional curvature is an intrinsic property of manifold. If the manifold is a sphere ${\sum_{i = 1}^{d + 1}x_{i}^{2}} = R^{2}$, then $K = {1/R^{2}}$, but more generally there is no simple connection. The smoothness parameters we assume are natural compared to some quantity from complicated compositions or pullback.

<!-- chunk {"id": "body-0026", "role": "body", "section": "kPCA", "weight": 1.0} -->

We consider the kPCA problem, where we want to find the $k \leq n$ principal eigenvectors of a symmetric matrix $H \in {\mathbb{R}}^{n \times n}$, as an example. This corresponds to which is an optimization problem on the Grassmann manifold defined by the constraint ${X^{T}X} = I$. If the eigenvalues of $H$ are distinct, we denote by $v_{1}$,...,$v_{n}$ the eigenvectors of $H$, corresponding to eigenvalues with decreasing order. Let $V^{\ast} = {\lbrack v_{1},\ldots,v_{k}\rbrack}$ be the matrix with columns composed of the top $k$ eigenvectors of $H$, then the local minimizers of the objective function are $V^{\ast}G$ for all unitary matrices $G \in {\mathbb{R}}^{k \times k}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "kPCA", "weight": 1.0} -->

Denote also by $V = {\lbrack v_{i_{1}},\ldots,v_{i_{k}}\rbrack}$ the matrix with columns composed of $k$ distinct eigenvectors, then the first order stationary points of the objective function (with Riemannian gradient being $0$) are $VG$ for all unitary matrices $G \in {\mathbb{R}}^{k \times k}$. In our numerical experiment, we choose $H$ to be a diagonal matrix $H = {{diag}{}}$ and let $k = 3$. The Euclidean basis $(e_{i})$ are an eigenbasis of $H$ and the first order stationary points of the objective function are ${\lbrack e_{i_{1}},e_{i_{2}},e_{i_{3}}\rbrack}G$ with distinct basis and $G$ being unitary.

<!-- chunk {"id": "body-0028", "role": "body", "section": "kPCA", "weight": 1.0} -->

The local minimizers are ${\lbrack e_{3},e_{4},e_{5}\rbrack}G$. We start the iteration at $X_{0} = {\lbrack e_{2},e_{3},e_{4}\rbrack}$ and see in Fig. 3 the algorithm converges to a local minimum.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Burer-Monteiro approach for certain low rank problems", "weight": 1.0} -->

Following Boumal et al., we consider, for $A \in {\mathbb{S}}^{d \times d}$ and ${{r{({r + 1})}}/2} \leq d$, the problem We factorize $X$ by $YY^{T}$ with an overparametrized $Y \in {\mathbb{R}}^{d \times p}$ and ${{p{({p + 1})}}/2} \geq d$. Then any local minimum of is a global minimum where ${YY^{T}} = X^{\ast}$. Let ${f{(Y)}} = {\frac{1}{2}{trace}{({AYY^{T}})}}$. In the experiment, we take $A \in {\mathbb{R}}^{100 \times 20}$ being a sparse matrix that only the upper left $5 \times 5$ block is random and other entries are $0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Burer-Monteiro approach for certain low rank problems", "weight": 1.0} -->

Let the initial point $Y_{0} \in {\mathbb{R}}^{100 \times 20}$, such that ${(Y_{0})}_{i,j} = 1$ for ${{5j} - 4} \leq i \leq {5j}$ and ${(Y_{0})}_{i,j} = 0$ otherwise. Then $Y_{0}$ is a saddle point. We see in Fig. 3 the algorithm converges to the global optimum.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Summary", "weight": 1.0} -->

We have shown that for the constrained optimization problem of minimizing $f{(x)}$ subject to a manifold constraint as long as the function and the manifold are appropriately smooth, a perturbed Riemannian gradient descent algorithm will escape saddle points with a rate of order $1/\epsilon^{2}$ in the accuracy $\epsilon$, polylog in manifold dimension $d$, and depends polynomially on the curvature and smoothness parameters.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Summary", "weight": 1.0} -->

A natural extension of our result is to consider other variants of gradient descent, such as the heavy ball method, Nesterov's acceleration, and the stochastic setting. The question is whether these algorithms with appropriate modification (with manifold constraints) would have a fast convergence to second-order stationary point (not just first-order stationary as studied in recent literature), and whether it is possible to show the relationship between convergence rate and smoothness of manifold.
