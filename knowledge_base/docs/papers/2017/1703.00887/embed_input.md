<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How to Escape Saddle Points Efficiently

Topics include Matrix factorization, Convex optimization, Gradient descent, Deep learning, Optimization, Learning, Saddle point, Stationary point.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper shows that a perturbed form of gradient descent converges to a second-order stationary point in a number iterations which depends only poly-logarithmically on dimension (i.e., it is almost "dimension-free"). The convergence rate of this procedure matches the well-known convergence rate of gradient descent to first-order stationary points, up to log factors. When all saddle points are non-degenerate, all second-order stationary points are local minima, and our result thus shows that perturbed gradient descent can escape saddle points almost for free. Our results can be directly applied to many machine learning applications, including deep learning. As a particular concrete example of such an application, we show that our results can be used directly to establish sharp global convergence rates for matrix factorization. Our results rely on a novel characterization of the geometry around saddle points, which may be of independent interest to the non-convex optimization community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, gradient descent aims to minimize the function via the following iteration: where $\eta > 0$ is a step size. Gradient descent and its variants (e.g., stochastic gradient) are widely used in machine learning applications due to their favorable computational properties. This is notably true in the deep learning setting, where gradients can be computed efficiently via back-propagation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient descent is especially useful in high-dimensional settings because the number of iterations required to reach a point with small gradient is independent of the dimension ("dimension-free"). More precisely, for a function that is $\ell$-gradient Lipschitz (see Definition 1), it is well known that gradient descent finds an $\epsilon$-first-order stationary point (i.e., a point $\mathbf{x}$ with ${\|{{\nabla f}{(\mathbf{x})}}\|} \leq \epsilon$) within ${\ell{({{f{(\mathbf{x}_{0})}} - f^{\star}})}}/\epsilon^{2}$ iterations, where $\mathbf{x}_{0}$ is the initial point and $f^{\star}$ is the optimal value of $f$. This bound does not depend on the dimension of $\mathbf{x}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In convex optimization, finding an $\epsilon$-first-order stationary point is equivalent to finding an approximate global optimum.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In non-convex settings, however, convergence to first-order stationary points is not satisfactory. For non-convex functions, first-order stationary points can be global minima, local minima, saddle points or even local maxima. Finding a global minimum can be hard, but fortunately, for many non-convex problems, it is sufficient to find a local minimum. Indeed, a line of recent results show that, in many problems of interest, either all local minima are global minima (e.g., in tensor decomposition, dictionary learning, phase retrieval, matrix sensing, matrix completion, and certain classes of deep neural networks ). Moreover, there are suggestions that in more general deep newtorks most of the local minima are as good as global minima.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, saddle points (and local maxima) can correspond to highly suboptimal solutions in many problems. Furthermore, Dauphin et al. argue that saddle points are ubiquitous in high-dimensional, non-convex optimization problems, and are thus the main bottleneck in training neural networks. Standard analysis of gradient descent cannot distinguish between saddle points and local minima, leaving open the possibility that gradient descent may get stuck at saddle points, either asymptotically or for a sufficiently long time so as to make training times for arriving at a local minimum infeasible. Ge et al. showed that by adding noise at each step, gradient descent can escape all saddle points in a polynomial number of iterations, provided that the objective function satisfies the strict saddle property (see Assumption A2). Lee et al. proved that under similar conditions, gradient descent with random initialization avoids saddle points even without adding noise. However, this result does not bound the number of steps needed to reach a local minimum.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though these results establish that gradient descent can find local minima in a polynomial number of iterations, they are still far from being efficient. For instance, the number of iterations required in Ge et al. is at least $\Omega{(d^{4})}$, where $d$ is the underlying dimension. This is significantly suboptimal compared to rates of convergence to first-order stationary points, where the iteration complexity is dimension-free. This motivates the following question: Can gradient descent escape saddle points and converge to local minima in a number of iterations that is (almost) dimension-free?

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to answer this question formally, this paper investigates the complexity of finding $\epsilon$-second-order stationary points. For $\rho$-Hessian Lipschitz functions (see Definition 5), these points are defined as: Under the assumption that all saddle points are strict (i.e., for any saddle point $\mathbf{x}_{s}$, ${\lambda_{\min}{({{\nabla^{2}f}{(\mathbf{x}_{s})}})}} < 0$), all second-order stationary points ($\epsilon = 0$) are local minima. Therefore, convergence to second-order stationary points is equivalent to convergence to local minima. if perturbation condition holds then Algorithm 1 Perturbed Gradient Descent (Meta-algorithm) This paper studies gradient descent with phasic perturbations (see Algorithm 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For $\ell$-smooth functions that are also Hessian Lipschitz, we show that perturbed gradient descent will converge to an $\epsilon$-second-order stationary point in $\overset{\sim}{O}{({{\ell{({{f{(\mathbf{x}_{0})}} - f^{\star}})}}/\epsilon^{2}})}$, where $\overset{\sim}{O}{(\cdot)}$ hides polylog factors. This guarantee is almost dimension free (up to $\text{polylog}{(d)}$ factors), answering the above highlighted question affirmatively. Note that this rate is exactly the same as the well-known convergence rate of gradient descent to first-order stationary points, up to log factors. Furthermore, our analysis admits a maximal step size of up to $\Omega{({1/\ell})}$, which is the same as that in analyses for first-order stationary points.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

As many real learning problems present strong *local* geometric properties, similar to strong convexity in the global setting, it is important to note that our analysis naturally takes advantage of such local structure. We show that when local strong convexity is present, the $\epsilon$-dependence goes from a polynomial rate, $1/\epsilon^{2}$, to linear convergence, $\log{({1/\epsilon})}$. As an example, we show that sharp global convergence rates can be obtained for matrix factorization as a direct consequence of our analysis.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

This paper presents the first sharp analysis that shows that (perturbed) gradient descent finds an approximate second-order stationary point in at most $polylog{(d)}$ iterations, thus escaping all saddle points efficiently. Our main technical contributions are as follows: For $\ell$-gradient Lipschitz, $\rho$-Hessian Lipschitz functions (possibly non-convex), gradient descent with appropriate perturbations finds an $\epsilon$-second-order stationary point in $\overset{\sim}{O}{({{\ell{({{f{(\mathbf{x}_{0})}} - f^{\star}})}}/\epsilon^{2}})}$ iterations. This rate matches the well-known convergence rate of gradient descent to first-order stationary points up to log factors.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Under a strict-saddle condition (see Assumption A2), this convergence result directly applies for finding local minima. This means that gradient descent can escape all saddle points with only logarithmic overhead in runtime.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

When the function has local structure, such as local strong convexity (see Assumption A3.a), the above results can be further improved to linear convergence. We give sharp rates that are comparable to previous problem-specific local analysis of gradient descent with smart initialization (see Section 1.2).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

All the above results rely on a new characterization of the geometry around saddle points: points from where gradient descent gets stuck at a saddle point constitute a thin "band." We develop novel techniques to bound the volume of this band. As a result, we can show that after a random perturbation the current point is very unlikely to be in the "band"; hence, efficient escape from the saddle point is possible (see Section 5).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Result", "weight": 1.0} -->

In this section we show that it possible to modify gradient descent in a simple way so that the resulting algorithm will provably converge quickly to a second-order stationary point.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main Result", "weight": 1.0} -->

The algorithm that we analyze is a perturbed form of gradient descent (see Algorithm 2). The algorithm is based on gradient descent with step size $\eta$. When the norm of the current gradient is small ($\leq g_{\text{thres}}$) (which indicates that the current iterate ${\overset{\sim}{\mathbf{x}}}_{t}$ is potentially near a saddle point), the algorithm adds a small random perturbation to the gradient. The perturbation is added at most only once every $t_{\text{thres}}$ iterations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption A1", "weight": 1.0} -->

Function $f{( \cdot )}$ is both $\ell$-smooth and $\rho$-Hessian Lipschitz.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption A1", "weight": 1.0} -->

The Hessian Lipschitz condition ensures that the function is well-behaved near a saddle point, and the small perturbation we add will suffice to allow the subsequent gradient updates to escape from the saddle point.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Functions with Strict Saddle Property", "weight": 1.0} -->

In many real applications, objective functions further admit the property that all saddle points are strict. In this case, all second-order stationary points are local minima and hence convergence to second-order stationary points (Theorem 3) is equivalent to convergence to local minima.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption A2", "weight": 1.0} -->

Intuitively, the strict saddle assumption states that the ${\mathbb{R}}^{d}$ space can be divided into three regions: 1) a region where the gradient is large; 2) a region where the Hessian has a significant negative eigenvalue (around saddle point); and 3) the region close to a local minimum.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Functions with Strong Local Structure", "weight": 1.0} -->

The convergence rate in Theorem 3 is polynomial in $\epsilon$, which is similar to that of Theorem 2). ‣ 2.2 Gradient Descent ‣ 2 Preliminaries ‣ How to Escape Saddle Points Efficiently"), but is worse than the rate of Theorem 1 because of the lack of strong convexity. Although global strong convexity does not hold in the non-convex setting that is our focus, in many machine learning problems the objective function may have a favorable local structure in the neighborhood of local minima. Exploiting this property can lead to much faster convergence (linear convergence) to local minima.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption A3.a", "weight": 1.0} -->

In a $\zeta$-neighborhood of the set of local minima $\mathcal{X}^{\star}$, the function $f{( \cdot )}$ is $\alpha$-strongly convex, and $\beta$-smooth.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption A3.a", "weight": 1.0} -->

Here we use different letter $\beta$ to denote the local smoothness parameter (in contrast to the global smoothness parameter $\ell$). Note that we always have $\beta \leq \ell$. However, often even local $\alpha$-strong convexity does not hold.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption A3.b", "weight": 1.0} -->

In a $\zeta$-neighborhood of the set of local minima $\mathcal{X}^{\star}$, the function $f{(\cdot)}$ satisfies a $(\alpha,\beta)$-regularity condition if for any $\mathbf{x}$ in this neighborhood: Here $\mathcal{P}_{\mathcal{X}^{\star}}{(\cdot)}$ is the projection on to the set $\mathcal{X}^{\star}$. Note $(\alpha,\beta)$-regularity condition is more general and is directly implied by standard $\beta$-smooth and $\alpha$-strongly convex conditions. This regularity condition commonly appears in low-rank problems such as matrix sensing and matrix completion, and has been used in Bhojanapalli et al.; Zheng and Lafferty, where local minima form a connected set, and where the Hessian is strictly positive only with respect to directions pointing outside the set of local minima.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption A3.b", "weight": 1.0} -->

$\mathbf{x}_{t + 1}\leftarrow{\mathbf{x}_{t} - {\frac{1}{\beta}{\nabla f}{(\mathbf{x}_{t})}}}$ Algorithm 3 Perturbed Gradient Descent with Local Improvement: PGDli (x0, ℓ, ρ, ϵ, c, δ, Δf, β) Gradient descent naturally exploits local structure very well. In Algorithm 3, we first run Algorithm 2 to output a point within the neighborhood of a local minimum, and then perform standard gradient descent with step size $\frac{1}{\beta}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example --- Matrix Factorization", "weight": 1.0} -->

As a simple example to illustrate how to apply our general theorems to specific non-convex optimization problems, we consider a symmetric low-rank matrix factorization problem, based on the following objective function: where $\mathbf{M}^{\star} \in {\mathbb{R}}^{d \times d}$. For simplicity, we assume ${\text{rank}{(\mathbf{M}^{\star})}} = r$, and denote $\sigma_{1}^{\star}: = \sigma_{1}{(\mathbf{M}^{\star})}$, $\sigma_{r}^{\star}: = \sigma_{r}{(\mathbf{M}^{\star})}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example --- Matrix Factorization", "weight": 1.0} -->

Clearly, in this case the global minimum of function value is zero, which is achieved at $\mathbf{V}^{\star} = {\mathbf{T}\mathbf{D}}^{1/2}$ where ${\mathbf{T}\mathbf{D}\mathbf{T}}^{\top}$ is the SVD of the symmetric real matrix $\mathbf{M}^{\star}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example --- Matrix Factorization", "weight": 1.0} -->

The following two lemmas show that the objective function in Eq. satisfies the geometric assumptions A1, A2,and A3.b. Moreover, all local minima are global minima.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Exploiting Large Gradient or Negative Curvature", "weight": 1.0} -->

Recall that an $\epsilon$-second-order stationary point is a point with a small gradient, and where the Hessian does not have a significant negative eigenvalue. Suppose we are currently at an iterate $\mathbf{x}_{t}$ that is not an $\epsilon$-second-order stationary point; i.e., it does not satisfy the above properties. There are two possibilities: Gradient is large: ${\|{{\nabla f}{(\mathbf{x}_{t})}}\|} \geq g_{\text{thres}}$, or Around saddle point: ${\|{{\nabla f}{(\mathbf{x}_{t})}}\|} \leq g_{\text{thres}}$ and ${\lambda_{\min}{({{\nabla^{2}f}{(\mathbf{x}_{t})}})}} \leq {- \sqrt{\rho\epsilon}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Exploiting Large Gradient or Negative Curvature", "weight": 1.0} -->

The following two lemmas address these two cases respectively. They guarantee that perturbed gradient descent will decrease the function value in both scenarios.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main Lemma: Escaping from Saddle Points Quickly", "weight": 1.0} -->

The proof of Lemma 9. ‣ 5.1 Exploiting Large Gradient or Negative Curvature ‣ 5 Proof Sketch for Theorem 3 ‣ How to Escape Saddle Points Efficiently") is straightforward and follows from traditional analysis. The key technical contribution of this paper is the proof of Lemma 10. ‣ 5.1 Exploiting Large Gradient or Negative Curvature ‣ 5 Proof Sketch for Theorem 3 ‣ How to Escape Saddle Points Efficiently"), which gives a new characterization of the geometry around saddle points.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Lemma: Escaping from Saddle Points Quickly", "weight": 1.0} -->

Consider a point $\overset{\sim}{\mathbf{x}}$ that satisfies the the preconditions of Lemma 10. ‣ 5.1 Exploiting Large Gradient or Negative Curvature ‣ 5 Proof Sketch for Theorem 3 ‣ How to Escape Saddle Points Efficiently") (${\|{{\nabla f}{(\overset{\sim}{\mathbf{x}})}}\|} \leq g_{\text{thres}}$ and ${\lambda_{\min}{({{\nabla^{2}f}{(\overset{\sim}{\mathbf{x}})}})}} \leq {- \sqrt{\rho\epsilon}}$).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Lemma: Escaping from Saddle Points Quickly", "weight": 1.0} -->

Our general proof strategy is to show that $\mathcal{X}_{\text{stuck}}$ consists of a very small proportion of the volume of perturbation ball. After adding a perturbation to $\overset{\sim}{\mathbf{x}}$, point $\mathbf{x}_{0}$ has a very small chance of falling in $\mathcal{X}_{\text{stuck}}$, and hence will escape from the saddle point efficiently.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Lemma: Escaping from Saddle Points Quickly", "weight": 1.0} -->

The major challenge here is to bound the volume of this high-dimensional non-flat "pancake" shaped region $\mathcal{X}_{\text{stuck}}$. A crude approximation of this "pancake" by a flat "disk" loses polynomial factors in the dimensionalilty, which gives a suboptimal rate. Our proof relies on the following crucial observation: Although we do not know the explicit form of the stuck region, we know it must be very "thin," therefore it cannot have a large volume.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents the first (nearly) dimension-free result for gradient descent in a general non-convex setting. We present a general convergence result and show how it can be further strengthened when combined with further structure such as strict saddle conditions and/or local regularity/convexity.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are still many related open problems. First, in the presence of constraints, it is worthwhile to study whether gradient descent still admits similar sharp convergence results. Another important question is whether similar techniques can be applied to accelerated gradient descent. We hope that this result could serve as a first step towards a more general theory with strong, almost dimension free guarantees for non-convex optimization.
