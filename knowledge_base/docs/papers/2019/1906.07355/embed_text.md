## Introduction

We consider minimizing a non-convex smooth function on a smooth manifold $\mathcal{M}$,

where $\mathcal{M}$ is a $d$-dimensional smooth manifold^11^1Here $d$ is the dimension of the manifold itself; we do not consider $\mathcal{M}$ as a submanifold of a higher dimensional space. For instance, if $\mathcal{M}$ is a 2-dimensional sphere embedded in ${\mathbb{R}}^{3}$, its dimension is $d = 2$., and $f$ is twice differentiable, with a Hessian that is $\rho$-Lipschitz (assumptions are formalized in section 4). This framework includes a wide range of fundamental problems (often non-convex), such as PCA, dictionary learning, low rank matrix completion, and tensor factorization. Finding the global minimum to Eq. is in general NP-hard; our goal is to find an approximate second order stationary point with first order optimization methods. We are interested in first-order methods because they are extremely prevalent in machine learning, partly because computing Hessians is often too costly. It is then important to understand how first-order methods fare when applied to nonconvex problems, and there has been a wave of recent interest on this topic since, as reviewed below.

In the Euclidean space, it is known that with random initialization, gradient descent avoids saddle points asymptotically. Lee et al. (section 5.5) show that this is also true on smooth manifolds, although the result is expressed in terms of nonstandard manifold smoothness measures. Also, importantly, this line of work does not give quantitative rates for the algorithm's behaviour near saddle points.

Du et al. show gradient descent can be *exponentially slow* in the presence of saddle points. To alleviate this phenomenon, it is shown that for a $\beta$-gradient Lipschitz, $\rho$-Hessian Lipschitz function, cubic regularization and perturbed gradient descent converges to $(\epsilon,{- \sqrt{\rho\epsilon}})$ local minimum ^22^2defined as $x$ satisfying ${\|{{\nabla f}{(x)}}\|} \leq \epsilon$, ${\lambda_{\min}{\nabla^{2}f}{(x)}} \geq {- \sqrt{\rho\epsilon}}$ in polynomial time, and momentum based method accelerates. Much less is known about inequality constraints: Nouiehed et al. and Mokhtari et al. discuss second order convergence for general inequality-constrained problems, where they need an NP-hard subproblem (checking the co-positivity of a matrix) to admit a polynomial time approximation algorithm. However such an approximation exists only under very restrictive assumptions.

An orthogonal line of work is optimization on Riemannian manifolds. Absil et al. provide comprehensive background, showing how algorithms such as gradient descent, Newton and trust region methods can be implemented on Riemannian manifolds, together with asymptotic convergence guarantees to first order stationary points. Zhang & Sra provide global convergence guarantees for first order methods when optimizing geodesically convex functions. Bonnabel obtains the first asymptotic convergence result for stochastic gradient descent in this setting, which is further extended by Tripuraneni et al.; Zhang et al.; Khuzani & Li. If the problem is non-convex, or the Riemannian Hessian is not positive definite, one can use second order methods to escape from saddle points. Boumal et al. shows that Riemannian trust region method converges to a second order stationary point in polynomial time. But this method requires a Hessian oracle, whose complexity is $d$ times more than computing gradient. In Euclidean space, trust region subproblem can be sometimes solved via a Hessian-vector product oracle, whose complexity is about the same as computing gradients. Agarwal et al. discuss its implementation on Riemannian manifolds, but not clear about the complexity and sensitivity of Hessian vector product oracle on manifold.

The study of the convergence of gradient descent for non-convex Riemannian problems is previously done only in the Euclidean space by modeling the manifold with equality constraints. Ge et al. prove that stochastic projected gradient descent methods converge to second order stationary points in polynomial time (here the analysis is not geometric, and depends on the algebraic representation of the equality constraints). Sun & Fazel proves perturbed projected gradient descent converges with a comparable rate to the unconstrained setting (polylog in dimension). The paper applies projections from the ambient Euclidean space to the manifold and analyzes the iterations under the Euclidean metric. This approach loses the geometric perspective enabled by Riemannian optimization, and cannot explain convergence rates in terms of inherent quantities such as the sectional curvature of the manifold.

After finishing this work, we found the recent and independent paper Criscitiello & Boumal which gives a similar convergence analysis result for a related perturbed Riemannian gradient method. We point out a few differences: In Criscitiello & Boumal Lipschitz assumptions are made on the pullback map $f \circ {Retr}$. While this makes the analysis simpler, it lumps the properties of the function and the manifold together, and the role of the manifold's curvature is not explicit. In contrast, our rates are expressed in terms of the function's smoothness parameters and the sectional curvature of the manifold separately, capturing the geometry more clearly. The algorithm in Criscitiello & Boumal uses two types of iterates (some on the manifold but some taken on a tangent space), whereas all our algorithm steps are directly on the manifold, which is more natural. To connect our iterations with intrinsic parameters of the manifold, we use the exponential map instead of the more general retraction used in Criscitiello & Boumal.

Contributions. We provide convergence guarantees for perturbed first order Riemannian optimization methods to second-order stationary points (local minimum). We prove that as long as the function is appropriately smooth and the manifold has bounded sectional curvature, a perturbed Riemannian gradient descent algorithm escapes (an approximate) saddle points with a rate of $1/\epsilon^{2}$, a polylog dependence on the dimension of the manifold (hence almost dimension-free), and a polynomial dependence on the smoothness and curvature parameters. This is the first result showing such a rate for Riemannian optimization, and the first to relate the rate to geometric parameters of the manifold.

Despite analogies with the unconstrained (Euclidean) analysis and with the Riemannian optimization literature, the technical challenge in our proof goes beyond combining two lines of work: we need to analyze the interaction between the first-order method and the second order structure of the manifold to obtain second-order convergence guarantees that depend on the manifold curvature. Unlike in Euclidean space, the curvature affects the Taylor approximation of gradient steps. On the other hand, unlike in the local rate analysis in first-order Riemannian optimization, our second-order analysis requires more refined properties of the manifold structure (whereas in prior work, first order oracle makes enough progress for a local convergence rate proof, see Lemma 1), and second order algorithms such as use second order oracles (Hessian evaluation). See section 4 for further discussion.

## Notation and Background

We consider a complete^33^3Since our results are local, completeness is not necessary and our results can be easily generalized, with extra assumptions on the injectivity radius., smooth, $d$ dimensional Riemannian manifold $(\mathcal{M},{\mathfrak{g}})$, equipped with a Riemannian metric $\mathfrak{g}$, and we denote by $\mathcal{T}_{x}\mathcal{M}$ its tangent space at $x \in \mathcal{M}$ (which is a vector space of dimension $d$). We also denote by ${{\mathbb{B}}_{x}{(r)}} = {\{{{v \in {\mathcal{T}_{x}\mathcal{M}}},{{\| v\|} \leq r}}\}}$ the ball of radius $r$ in $\mathcal{T}_{x}\mathcal{M}$ centered at $0$. At any point $x \in \mathcal{M}$, the metric $\mathfrak{g}$ induces a natural inner product on the tangent space denoted by ${\langle \cdot, \cdot \rangle}:{{{{\mathcal{T}_{x}\mathcal{M}} \times \mathcal{T}_{x}}\mathcal{M}}\rightarrow{\mathbb{R}}}$. We also consider the Levi-Civita connection $\nabla$. The Riemannian curvature tensor is denoted by $R{(x)}{\lbrack u,v\rbrack}$ where $x \in \mathcal{M}$, ${u,v} \in {\mathcal{T}_{x}\mathcal{M}}$ and is defined in terms of the connection $\nabla$. The sectional curvature $K{(x)}{\lbrack u,v\rbrack}$ for $x \in \mathcal{M}$ and ${u,v} \in {\mathcal{T}_{x}\mathcal{M}}$ is then defined in Lee.

Denote the distance (induced by the Riemannian metric) between two points in $\mathcal{M}$ by $d{(x,y)}$. A geodesic $\gamma:{{\mathbb{R}}\rightarrow\mathcal{M}}$ is a constant speed curve whose length is equal to $d{(x,y)}$, so it is the shortest path on manifold linking $x$ and $y$. $\gamma_{x\rightarrow y}$ denotes the geodesic from $x$ to $y$ (thus ${\gamma_{x\rightarrow y}{}} = x$ and ${\gamma_{x\rightarrow y}{}} = y$).

The exponential map ${Exp}_{x}{(v)}$ maps $v \in {\mathcal{T}_{x}\mathcal{M}}$ to $y \in \mathcal{M}$ such that there exists a geodesic $\gamma$ with ${\gamma{}} = x$, ${\gamma{}} = y$ and ${\frac{d}{dt}\gamma{}} = v$. The injectivity radius at point $x \in \mathcal{M}$ is the maximal radius $r$ for which the exponential map is a diffeomorphism on ${{\mathbb{B}}_{x}{(r)}} \subset {\mathcal{T}_{x}\mathcal{M}}$. The injectivity radius of the manifold, denoted by $\Im$, is the infimum of the injectivity radii at all points. Since the manifold is complete, we have $\Im > 0$. When ${x,y} \in \mathcal{M}$ satisfies ${d{(x,y)}} \leq \Im$, the exponential map admits an inverse ${Exp}_{x}^{- 1}{(y)}$, which satisfies ${d{(x,y)}} = {\|{{Exp}_{x}^{- 1}{(y)}}\|}$. Parallel translation $\Gamma_{x}^{y}$ denotes a the map which transports $v \in {\mathcal{T}_{x}\mathcal{M}}$ to ${\Gamma_{x}^{y}v} \in {\mathcal{T}_{y}\mathcal{M}}$ along $\gamma_{x\rightarrow y}$ such that the vector stays constant by satisfying a zero-acceleration condition (Lee, 1997, equation (4.13)).

For a smooth function $f:{\mathcal{M}\rightarrow{\mathbb{R}}}$, ${{grad}f{(x)}} \in {\mathcal{T}_{x}\mathcal{M}}$ denotes the Riemannian gradient of $f$ at $x \in \mathcal{M}$ which satisfies ${\frac{d}{dt}f{({\gamma{(t)}})}} = {\langle{\gamma^{\prime}{(t)}},{{grad}f{(x)}}\rangle}$ (see Absil et al., 2009, Sec 3.5.1 and (3.31)). The Hessian of $f$ is defined jointly with the Riemannian structure of the manifold. The (directional) Hessian is ${{H{(x)}{\lbrack\xi_{x}\rbrack}}:={\nabla_{\xi_{x}}{{grad}f}}},$ and we use ${H{(x)}{\lbrack u,v\rbrack}}:={\langle u,{H{(x)}{\lbrack v\rbrack}}\rangle}$ as a shorthand. We call $x \in \mathcal{M}$ an $(\epsilon,{- \sqrt{\rho\epsilon}})$ saddle point when ${\|{{\nabla f}{(x)}}\|} \leq \epsilon$ and ${\lambda_{\min}{({H{(x)}})}} \leq {- \sqrt{\rho\epsilon}}$. We refer the interested reader to Do Carmo and Lee which provide a thorough review on these important concepts of Riemannian geometry.

## Perturbed Riemannian gradient algorithm

Our main Algorithm 1 runs as follows:

Check the norm of the gradient: If it is large, do one step of Riemannian gradient descent, consequently the function value decreases.

If the norm of gradient is small, it's either an approximate saddle point or a local minimum. Perturb the variable by adding an appropriate level of noise in its tangent space, map it back to the manifold and run a few iterations.

If the function value decreases, iterates are escaping from the approximate saddle point (and the algorithm continues)

If the function value does not decrease, then it is an approximate local minimum (the algorithm terminates).

0: Initial point x0 ∈ ℳ, parameters β, ρ, K, ℑ, accuracy ϵ, probability of success δ (parameters defined in Assumptions 1, 2, 3 and assumption of Theorem 1). Set constants: ĉ ≥ 4, C:= C (K,β,ρ) (defined in Lemma 2 and proof of Lemma 8) and $\sqrt{c_{\max}} \leq \frac{1}{56{\hat{c}}^{2}}$, $r = {\frac{\sqrt{c_{\max}}}{\chi^{2}}\epsilon}$, $\chi = {3{\max{\{{\log{(\frac{d\beta{({{f{(x_{0})}} - f^{\ast}})}}{\hat{c}\epsilon^{2}\delta})}},4\}}}}$.Set threshold values: $f_{thres} = {\frac{c_{\max}}{\chi^{3}}\sqrt{\frac{\epsilon^{3}}{\rho}}}$, $g_{thres} = {\frac{\sqrt{c_{\max}}}{\chi^{2}}\epsilon}$, $t_{thres} = {\frac{\chi}{c_{\max}}\frac{\beta}{\sqrt{\rho\epsilon}}}$, tnoise = −tthres − 1.Set stepsize: $\eta = \frac{c_{\max}}{\beta}$.
if ∥grad f (xt)∥ ≤ gthres and t − tnoise &gt; tthres then
tnoise ← t, ${\overset{\sim}{x}}_{t}\leftarrow x_{t}$, xt ← Expxt (ξt), ξt uniformly sampled from 𝔹xt (r) ⊂ 𝒯x ℳ.
if t − tnoise = tthres and ${{f{(x_{t})}} - {f{({\overset{\sim}{x}}_{t_{noise}})}}} &gt; {- f_{thres}}$ then
output ${\overset{\sim}{x}}_{t_{noise}}$
${{x_{t + 1} +}\leftarrow{{Exp}_{x_{t}}{({- {{\min{\{\eta,\frac{\Im}{\|{{grad}f{(x_{t})}}\|}\}}}{grad}f{(x_{t})}}})}}}.$
Algorithm 1 Perturbed Riemannian gradient algorithm

Algorithm 1 relies on the manifold's exponential map, and is useful for cases where this map is easy to compute (true for many common manifolds). We refer readers to Lee for the exponential map of sphere and hyperbolic manifolds, and Absil et al. for the Stiefel and Grassmann manifolds. If the exponential map is not computable, the algorithm can use a retraction^44^4A retraction is a first-order approximation of the exponential map which is often easier to compute. instead, however our current analysis only covers the case of the exponential map. In Figure 1, we illustrate a function with saddle point on sphere, and plot the trajectory of Algorithm 1 when it is initialized at a saddle point.

Figure 1: Function f with saddle point on a sphere. f (x) = x12 − x22 + 4 x32. We plot the contour of this function on unit sphere. Algorithm 1 initializes at x0 = (a saddle point), perturbs it towards x1 and runs Riemannian gradient descent, and terminates at x* = [0, −1, 0] (a local minimum). We amplify the first iteration to make saddle perturbation visible.

## Main theorem: escape rate for perturbed Riemannian gradient descent

We now turn to our main results, beginning with our assumptions and a statement of our main theorem. We then develop a brief proof sketch.

Our main result involves two conditions on function $f$ and one on the curvature of the manifold $\mathcal{M}$.

### Assumption 1 (Lipschitz gradient)

There is a finite constant $\beta$ such that

### Assumption 2 (Lipschitz Hessian)

There is a finite constant $\rho$ such that

### Assumption 3 (Bounded sectional curvature)

There is a finite constant $K$ such that

$K$ is an intrinsic parameter of the manifold capturing the curvature. We list a few examples here: (i) A sphere of radius $R$ has a constant sectional curvature $K = {1/R^{2}}$. If the radius is bigger, $K$ is smaller which means the sphere is less curved; (ii) A hyper-bolic space $H_{R}^{n}$ of radius $R$ has $K = {- {1/R^{2}}}$; (iii) For sectional curvature of the Stiefel and the Grasmann manifolds, we refer readers to Rapcsák and Wong, respectively.

Note that the constant $K$ is not directly related to the RLICQ parameter $R$ defined by Ge et al. which first requires describing the manifold by equality constraints. Different representations of the same manifold could lead to different curvature bounds, while sectional curvature is an intrinsic property of manifold. If the manifold is a sphere ${\sum_{i = 1}^{d + 1}x_{i}^{2}} = R^{2}$, then $K = {1/R^{2}}$, but more generally there is no simple connection. The smoothness parameters we assume are natural compared to some quantity from complicated compositions or pullback. With these assumptions, the main result of this paper is the following:

### Theorem 1

Under Assumptions 1. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"),2. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"),3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), let $C{(K,\beta,\rho)}$ be a function defined in Lemma 2, $\hat{\rho} = {\max{\{\rho,{C{(K,\beta,\rho)}}\}}}$, if $\epsilon$ satisfies that

where $c_{2}{(K)}$, $c_{3}{(K)}$ are defined in Lemma 4, then with probability $1 - \delta$, perturbed Riemannian gradient descent with step size $c_{\max}/\beta$ converges to a $(\epsilon,{- \sqrt{\hat{\rho}\epsilon}})$-stationary point of $f$ in

Proof roadmap. For a function satisfying smoothness condition (Assumption 1. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds") and 2. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds")), we use a local upper bound of the objective based on the third-order Taylor expansion (see supplementary material Section A for a review),

When the norm of the gradient is large (not near a saddle), the following lemma guarantees the decrease of the objective function in one iteration.

### Lemma 1

Under Assumption 1. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), by choosing $\overline{\eta} = {\min{\{\eta,\frac{\Im}{\|{{grad}f{(u)}}\|}\}}} = {O{({1/\beta})}}$, the Riemannian gradient descent algorithm is monotonically descending, ${f{(u^{+})}} \leq {{f{(u)}} - {\frac{1}{2}\overline{\eta}{\|{{grad}f{(u)}}\|}^{2}}}$.

Thus our main challenge in proving the main theorem is the Riemannian gradient behaviour at an approximate saddle point:

1\. Similar to the Euclidean case studied by Jin et al., we need to bound the "thickness" of the "stuck region" where the perturbation fails. We still use a pair of hypothetical auxiliary sequences and study the "coupling" sequences. When two perturbations couple in the thinnest direction of the stuck region, their distance grows and one of them escapes from saddle point.

2\. However our iterates are evolving on a manifold rather than a Euclidean space, so our strategy is to map the iterates back to an appropriate fixed tangent space where we can use the Euclidean analysis. This is done using the inverse of the exponential map and various parallel transports.

3\. Several key challenges arise in doing this. Unlike Jin et al., the structure of the manifold interacts with the local approximation of the objective function in a complicated way. On the other hand, unlike recent work on Riemannian optimization by Boumal et al., we do not have access to a second order oracle and we need to understand how the sectional curvature and the injectivity radius (which both capture intrinsic manifold properties) affect the behavior of the first order iterates.

4\. Our main contribution is to carefully investigate how the various approximation errors arising from (a) the linearization of the iteration couplings and (b) their mappings to a common tangent space can be handled on manifolds with bounded sectional curvature. We address these challenges in a sequence of lemmas (Lemmas 3 through 6) we combine to linearize the coupling iterations in a common tangent space and precisely control the approximation error. This result is formally stated in the following lemma.

### Lemma 2

Define $\gamma = \sqrt{\hat{\rho}\epsilon}$, $\kappa = \frac{\beta}{\gamma}$, and $\mathcal{S} = {\sqrt{\eta\beta}\frac{\gamma}{\hat{\rho}}{\log^{- 1}{(\frac{d\kappa}{\delta})}}}$. Let us consider $x$ be a $(\epsilon,{- \sqrt{\hat{\rho}\epsilon}})$ saddle point, and define $u^{+} = {{Exp}_{u}{({- {\eta{grad}f{(u)}}})}}$ and $w^{+} = {{Exp}_{w}{({- {\eta{grad}f{(w)}}})}}$. Under Assumptions 1. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), 2. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), if all pairwise distances between $u,w,u^{+},w^{+},x$ are less than $12\mathcal{S}$, then for some explicit constant $C{(K,\rho,\beta)}$ depending only on $K,\rho,\beta$, there is

The proof of this lemma includes novel contributions by strengthen known result (Lemmas 3) and also combining known inequalities in novel ways (Lemmas 4 to 6) that allow us to control all the approximation errors and arrive at the tight rate of escape for the algorithm.

## Proof of Lemma 2

Lemma 2 controls the error of the linear approximation of the iterates when mapped in $T_{x}\mathcal{M}$. In this section, we assume that all points are within a region of diameter $R:={12\mathcal{S}} \leq \Im$ (inequality follows from Eq. ), i.e., the distance of any two points in the following lemmas are less than $R$. The proof of Lemma 2 is based on the sequence of following lemmas.

### Lemma 3

Let $x \in \mathcal{M}$ and ${y,a} \in {T_{x}\mathcal{M}}$. Let us denote by $z = {{Exp}_{x}{(a)}}$ then under Assumption 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds")

This lemma tightens the result of Karcher, which only shows an upper-bound $O{({{\| a\|}{({{\| a\|} + {\| y\|}})}^{2}})}$. We prove the upper-bound $O{({{\| y\|}{({{\| a\|} + {\| y\|}})}^{2}})}$ in the supplement.

Figure 2: (a) Eq.. First map w and w+ to 𝒯u ℳ and 𝒯u+ ℳ, and transport the two vectors to 𝒯x ℳ, and get their relation. (b) Lemma 3 bounds the difference of two steps starting from x: take y + a step in 𝒯x ℳ and map it to manifold, and take a step in 𝒯x ℳ, map to manifold, call it z, and take Γxz y step in 𝒯x ℳ, and map to manifold. Expz (Γxz y) is close to Expx (y+a).

We also need the following lemma showing that both the exponential map and its inverse are Lipschitz.

### Lemma 4

Let ${x,y,z} \in M$, and the distance of each two points is no bigger than $R$. Then under assumption 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds")

Intuitively this lemma relates the norm of the difference of two vectors of $\mathcal{T}_{x}\mathcal{M}$ to the distance between the corresponding points on the manifold $\mathcal{M}$ and follows from bounds on the Hessian of the square-distance function. The upper-bound is directly proven by Karcher, and we prove the lower-bound via Lemma 3 in the supplement.

The following contraction result is fairly classical and is proven using the Rauch comparison theorem from differential geometry.

### Lemma 5

Under Assumption 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), for ${x,y} \in \mathcal{M}$ and $w \in {T_{x}\mathcal{M}}$,

Finally we need the following corollary of the Ambrose-Singer theorem.

### Lemma 6

Under Assumption 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), for ${x,y,z} \in \mathcal{M}$ and $w \in {T_{x}\mathcal{M}}$,

Lemma 3 through 6 are mainly proven in the literature, and we make up the missing part in Supplementary material Section B. Then we prove Lemma 2 in Supplementary material Section B.

The spirit of the proof is to linearize the manifold using the exponential map and its inverse, and to carefully bounds the various error terms caused by the approximation. Let us denote by $\theta = {{d{(u,w)}} + {d{(u,x)}} + {d{(w,x)}}}$.

1\. We first show using twice Lemma 3 and Lemma 5 that

2\. We use Lemma 4 to linearize this iteration in $\mathcal{T}_{u}\mathcal{M}$ as

3\. Using the Hessian Lipschitzness

3\. We use Lemma 6 to map to $T_{x}\mathcal{M}$ and the Hessian Lipschitzness to compare $H{(u)}$ to $H{(x)}$. This is an important intermediate result (see Lemma 1 in Supplementary material Section B).

4\. We use Lemma 3 and 4 to approximate two iteration updates in $\mathcal{T}_{x}\mathcal{M}$.

And same for the $u_{+},w_{+}$ pair replacing $u,w$.

5\. Combining Eq. and Eq. together, we obtain

Now note that, the iterations $u,u_{+},w,w_{+}$ of the algorithm are both on the manifold. We use ${Exp}_{x}^{- 1}{( \cdot )}$ to map them to the same tangent space at $x$.

Therefore we have linearized the two coupled trajectories ${Exp}_{x}^{- 1}{(u_{t})}$ and ${Exp}_{x}^{- 1}{(w_{t})}$ in a common tangent space, and we can modify the Euclidean escaping saddle analysis thanks to the error bound we proved in Lemma 2.

## Proof of main theorem

In this section we suppose all assumptions in Section 4 hold. The proof strategy is to show with high probability that the function value decreases of $\mathcal{F}$ in $\mathcal{T}$ iterations at an approximate saddle point. Lemma 7 suggests that, if after a perturbation and $\mathcal{T}$ steps, the iterate is $\Omega{(\mathcal{S})}$ far from the approximate saddle point, then the function value decreases. If the iterates do not move far, the perturbation falls in a stuck region. Lemma 8 uses a coupling strategy, and suggests that the width of the stuck region is small in the negative eigenvector direction of the Riemannian Hessian.

At an approximate saddle point $\overset{\sim}{x}$, let $y$ be in the neighborhood of $\overset{\sim}{x}$ where ${d{(y,\overset{\sim}{x})}} \leq \Im$, denote

Let ${\|{{grad}f{(\overset{\sim}{x})}}\|} \leq \mathcal{G}$ and ${\lambda_{\min}{({H{(\overset{\sim}{x})}})}} \leq {- \gamma}$. We consider two iterate sequences, $u_{0},u_{1},\ldots$ and $w_{0},w_{1},\ldots$ where $u_{0},w_{0}$ are two perturbations at $\overset{\sim}{x}$.

### Lemma 7

Assume Assumptions 1. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), 2. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds") and Eq. hold. There exists a constant $c_{\max}$, ${{\forall\hat{c}} > 3},{\delta \in {(0,\frac{d\kappa}{e}\rbrack}}$, for any $u_{0}$ with ${d{(\overset{\sim}{x},u_{0})}} \leq {{2\mathcal{S}}/{({\kappa{\log{(\frac{d\kappa}{\delta})}}})}}$, $\kappa = {\beta/\gamma}$.

then ${\forall\eta} \leq {c_{\max}/\beta}$, we have ${\forall 0} < t < T$, ${d{(u_{0},u_{t})}} \leq {3{({\hat{c}\mathcal{S}})}}$.

### Lemma 8

Assume Assumptions 1. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), 2. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds"), 3. ‣ 4 Main theorem: escape rate for perturbed Riemannian gradient descent ‣ Escaping from saddle points on Riemannian manifolds") and Eq. hold. Take two points $u_{0}$ and $w_{0}$ which are perturbed from an approximate saddle point, where ${d{(\overset{\sim}{x},u_{0})}} \leq {{2\mathcal{S}}/{({\kappa{\log{(\frac{d\kappa}{\delta})}}})}}$, ${{{Exp}_{\overset{\sim}{x}}^{- 1}{(w_{0})}} - {{Exp}_{\overset{\sim}{x}}^{- 1}{(u_{0})}}} = {\mure_{1}}$, $e_{1}$ is the smallest eigenvector^55^5"smallest eigenvector" means the eigenvector corresponding to the smallest eigenvalue. of $H{(\overset{\sim}{x})}$, $\mu \in {\lbrack{\delta/{({2\sqrt{d}})}},1\rbrack}$, and the algorithm runs two sequences $\{ u_{t}\}$ and $\{ w_{t}\}$ starting from $u_{0}$ and $w_{0}$. Denote

then ${\forall\eta} \leq {c_{\max}/l}$, if ${\forall 0} < t < T$, ${d{(\overset{\sim}{x},u_{t})}} \leq {3{({\hat{c}\mathcal{S}})}}$, we have $T < {\hat{c}\mathcal{T}}$.

We prove Lemma 7 and 8 in supplementary material Section C. We also prove, in the same section, the main theorem using the coupling strategy of Jin et al.. but with the additional difficulty of taking into consideration the effect of the Riemannian geometry (Lemma 2) and the injectivity radius.

## Examples

### kPCA

We consider the kPCA problem, where we want to find the $k \leq n$ principal eigenvectors of a symmetric matrix $H \in {\mathbb{R}}^{n \times n}$, as an example. This corresponds to

which is an optimization problem on the Grassmann manifold defined by the constraint ${X^{T}X} = I$. If the eigenvalues of $H$ are distinct, we denote by $v_{1}$,...,$v_{n}$ the eigenvectors of $H$, corresponding to eigenvalues with decreasing order. Let $V^{\ast} = {\lbrack v_{1},\ldots,v_{k}\rbrack}$ be the matrix with columns composed of the top $k$ eigenvectors of $H$, then the local minimizers of the objective function are $V^{\ast}G$ for all unitary matrices $G \in {\mathbb{R}}^{k \times k}$. Denote also by $V = {\lbrack v_{i_{1}},\ldots,v_{i_{k}}\rbrack}$ the matrix with columns composed of $k$ distinct eigenvectors, then the first order stationary points of the objective function (with Riemannian gradient being $0$) are $VG$ for all unitary matrices $G \in {\mathbb{R}}^{k \times k}$. In our numerical experiment, we choose $H$ to be a diagonal matrix $H = {{diag}{}}$ and let $k = 3$. The Euclidean basis $(e_{i})$ are an eigenbasis of $H$ and the first order stationary points of the objective function are ${\lbrack e_{i_{1}},e_{i_{2}},e_{i_{3}}\rbrack}G$ with distinct basis and $G$ being unitary. The local minimizers are ${\lbrack e_{3},e_{4},e_{5}\rbrack}G$. We start the iteration at $X_{0} = {\lbrack e_{2},e_{3},e_{4}\rbrack}$ and see in Fig. 3 the algorithm converges to a local minimum.

### Burer-Monteiro approach for certain low rank problems

Following Boumal et al., we consider, for $A \in {\mathbb{S}}^{d \times d}$ and ${{r{({r + 1})}}/2} \leq d$, the problem

We factorize $X$ by $YY^{T}$ with an overparametrized $Y \in {\mathbb{R}}^{d \times p}$ and ${{p{({p + 1})}}/2} \geq d$. Then any local minimum of

is a global minimum where ${YY^{T}} = X^{\ast}$. Let ${f{(Y)}} = {\frac{1}{2}{trace}{({AYY^{T}})}}$. In the experiment, we take $A \in {\mathbb{R}}^{100 \times 20}$ being a sparse matrix that only the upper left $5 \times 5$ block is random and other entries are $0$. Let the initial point $Y_{0} \in {\mathbb{R}}^{100 \times 20}$, such that ${(Y_{0})}_{i,j} = 1$ for ${{5j} - 4} \leq i \leq {5j}$ and ${(Y_{0})}_{i,j} = 0$ otherwise. Then $Y_{0}$ is a saddle point. We see in Fig. 3 the algorithm converges to the global optimum.

Figure 3: (a) kPCA problem. We start from an approximate saddle point, and it converges to a local minimum (which is also global minimum). (b) Burer-Monteiro approach Plot ${f{(Y)}} = {\frac{1}{2}{trace}{({AYY^{T}})}}$ versus iterations. We start from the saddle point, and it converges to a local minimum (which is also global minimum).

### Summary

We have shown that for the constrained optimization problem of minimizing $f{(x)}$ subject to a manifold constraint as long as the function and the manifold are appropriately smooth, a perturbed Riemannian gradient descent algorithm will escape saddle points with a rate of order $1/\epsilon^{2}$ in the accuracy $\epsilon$, polylog in manifold dimension $d$, and depends polynomially on the curvature and smoothness parameters.

A natural extension of our result is to consider other variants of gradient descent, such as the heavy ball method, Nesterov's acceleration, and the stochastic setting. The question is whether these algorithms with appropriate modification (with manifold constraints) would have a fast convergence to second-order stationary point (not just first-order stationary as studied in recent literature), and whether it is possible to show the relationship between convergence rate and smoothness of manifold.
