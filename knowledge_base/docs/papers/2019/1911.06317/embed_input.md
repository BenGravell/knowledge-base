<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradientless Descent: High-Dimensional Zeroth-Order Optimization

Topics include Benchmarks, Optimization, GLD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Zeroth-order optimization is the process of minimizing an objective f(x), given oracle access to evaluations at adaptively chosen inputs x. In this paper, we present two simple yet powerful GradientLess Descent (GLD) algorithms that do not rely on an underlying gradient estimate and are numerically stable. We analyze our algorithm from a novel geometric perspective and present a novel analysis that shows convergence within an epsilon-ball of the optimum in O(kQlog(n)log(R/epsilon)) evaluations, for any monotone transform of a smooth and strongly convex objective with latent dimension k < n, where the input dimension is n, R is the diameter of the input space and Q is the condition number. Our rates are the first of its kind to be both 1) poly-logarithmically dependent on dimensionality and 2) invariant under monotone transformations. We further leverage our geometric perspective to show that our analysis is optimal. Both monotone invariance and its ability to utilize a low latent dimensionality are key to the empirical success of our algorithms, as demonstrated on BBOB and MuJoCo benchmarks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the problem of zeroth-order optimization (also known as gradient-free optimization, or bandit optimization), where our goal is to minimize an objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ with as few evaluations of $f{(x)}$ as possible. For many practical and interesting objective functions, gradients are difficult to compute and there is still a need for zeroth-order optimization in applications such as reinforcement learning \[, SHC^+^17, CRS^+^18\], attacking neural networks \[CZS^+^17, PMG^+^17\], hyperparameter tuning of deep networks, and network control.\The standard approach to zeroth-order optimization is, ironically, to estimate the gradients from function values and apply a first-order optimization algorithm.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

analyze this class of algorithms as gradient descent on a Gaussian smoothing of the objective and gives an accelerated $O{({n\sqrt{Q}{\log{({{({{LR^{2}} + F})}/\epsilon})}}})}$ iteration complexity for an $L$-Lipschitz convex function with condition number $Q$ and $R = {\|{x_{0} - x^{\ast}}\|}$ and $F = {{f{(x_{0})}} - {f{(x^{\ast})}}}$. They propose a two-point evaluation scheme that constructs gradient estimates from the difference between function values at two points that are close to each other. This scheme was extended for stochastic settings, for nonconvex settings, and for non-smooth and non-Euclidean norm settings. Since then, first-order techniques such as variance reduction \[LKC^+^18\], conditional gradients, and diagonal preconditioning have been successfully adopted in this setting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This class of algorithms are also known as stochastic search, random search, or (natural) evolutionary strategies and have been augmented with a variety of heuristics, such as the popular CMA-ES.\These algorithms, however, suffer from high variance due to non-robust local minima or highly non-smooth objectives, which are common in the fields of deep learning and reinforcement learning. notes that gradient variance increases as training progresses due to higher variance in the objective functions, since often parameters must be tuned precisely to achieve reasonable models. Therefore, some attention has shifted into direct search algorithms that usually finds a descent direction $u$ and moves to $x + {\deltau}$, where the step size is not scaled by the function difference.\The first approaches for direct search were based on deterministic approaches with a positive spanning set and date back to the 1950s. Only recently have theoretical bounds surfaced, giving an iteration complexity that is a large polynomial of $n$ and giving an improved $O{({{n^{2}L^{2}}/\epsilon})}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic approaches tend to have better complexities: uses line search to give a $O{({nQ{\log{({F/\epsilon})}}})}$ iteration complexity for convex functions with condition number $Q$ and most recently, \[GBS^+^19\] uses importance sampling to give a $O{({n\overline{Q}{\log{({F/\epsilon})}}})}$ complexity for convex functions with average condition number $\overline{Q}$, assuming access to sampling probabilities. notes that direct search algorithms are invariant under monotone transforms of the objective, a property that might explain their robustness in high-variance settings.\In general, zeroth order optimization suffers an at least linear dependence on input dimension $n$ and recent works have tried to address this limitation when $n$ is large but $f{(x)}$ admits a low-dimensional structure.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some papers assume that $f{(x)}$ depends only on $k$ coordinates and applies Lasso to find the important set of coordinates, whereas simply change the step size to achieve an $O{({k{({{\log{(n)}}/\epsilon})}^{2}})}$ iteration complexity. Other papers assume more generally that ${f{(x)}} = {g{({\mathbf{P}_{\mathbf{A}}x})}}$ only depends on a $k$-dimensional subspace given by the range of $\mathbf{P}_{\mathbf{A}}$ and apply low-rank approximation to find the low-dimensional subspace while \[WZH^+^13\] use random embeddings. assume that $f{(x)}$ is a sparse collection of $k$-degree monomials on the Boolean hypercube and apply sparse recovery to achieve a $O{(n^{k})}$ runtime bound.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will show that under the case that ${f{(x)}} = {g{({\mathbf{P}_{\mathbf{A}}x})}}$, our algorithm will inherently pick up any low-dimensional structure in $f{(x)}$ and achieve a convergence rate that depends on $k{\log{(n)}}$. This initial convergence rate survives, even if we perturb ${f{(x)}} = {{g{({\mathbf{P}_{\mathbf{A}}x})}} + {h{(x)}}}$, so long as $h{(x)}$ is sufficiently small.\We will not cover the whole variety of black-box optimization methods, such as Bayesian optimization or genetic algorithms.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, these methods attempt to solve a broader problem (e.g. multiple optima), have weaker theoretical guarantees and may require substantial computation at each step: e.g. Bayesian optimization generally has theoretical iteration complexities that grow exponentially in dimension, and CMA-ES lacks provable complexity bounds beyond convex quadratic functions. In addition to the slow runtime and weaker guarantees, Bayesian optimization assumes the success of an inner optimization loop of the acquisition function. This inner optimization is often implemented with many iterations of a simpler zeroth-order methods, justifying the need to understand gradient-less descent algorithms within its own context.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In this paper, we present GradientLess Descent (GLD), a class of truly gradient-free algorithms (also known as direct search algorithms) that are parameter free and provably fast. Our algorithms are based on a simple intuition: for well-conditioned functions, if we start from a point and take a small step in a randomly chosen direction, there is a significant probability that we will reduce the objective function value. We present a novel analysis that relies on facts in high dimensional geometry and can thus be viewed as a geometric analysis of gradient-free algorithms, recovering the standard convergence rates and step sizes. Specifically, we show that if the step size is on the order of $O{(\frac{1}{\sqrt{n}})}$, we can guarantee an expected decrease of $1 - {\Omega{(\frac{1}{n})}}$ in the optimality gap, based on geometric properties of the sublevel sets of a smooth and strongly convex function.\Our results are invariant under monotone transformations of the objective function, thus our convergence results also hold for a large class of non-convex functions that are a subclass of quasi-convex functions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Specifically, note that monotone transformations of convex functions are not necessarily convex. However, a monotone transformation of a convex function is always *quasi-convex*. The maximization of *quasi-concave* utility functions, which is equivalent to the minimization of quasi-convex functions, is an important topic of study in economics (e.g.).\Intuition suggests that the step-size dependence on dimensionality can be improved when $f{(x)}$ admits a low-dimensional structure. With a careful choice of sampling distribution we can show that if ${f{(x)}} = {g{({\mathbf{P}_{\mathbf{A}}x})}}$, where $\mathbf{P}_{\mathbf{A}}$ is a rank $k$ matrix, then our step size can be on the order of $O{(\frac{1}{\sqrt{k}})}$ as our optimization behavior is preserved under projections. We call this property affine-invariance and show that the number of function evaluations needed for convergence depends logarithmically on $n$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Unlike most previous algorithms in the high-dimensional setting, no expensive sparse recovery or subspace finding methods are needed. Furthermore, by novel perturbation arguments, we show that our fast convergence rates are robust and holds even under the more realistic assumption when ${f{(x)}} = {{g{({\mathbf{P}_{\mathbf{A}}x})}} + {h{(x)}}}$ with $h{(x)}$ being sufficiently small.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Analysis of Descent Steps", "weight": 1.0} -->

The GLD template can be summarized as follows: given a sampling distribution $\mathcal{D}$, we start at $x_{0}$ and in iteration $t$, we choose a scalar radii $r_{t}$ and we sample $y_{t}$ from a distribution $r_{t}\mathcal{D}$ centered around $x_{t}$, where $r_{t}$ provides the scaling of $\mathcal{D}$. Then, if ${f{(x_{t + 1})}} < x_{t}$, we update $x_{t + 1} = y_{t}$; otherwise, we set $x_{t + 1} = x_{t}$. The analysis of GLD follows from the main observation that the sub-level set of a monotone transformation of a strongly convex and strongly smooth function contains a ball of sufficiently large radius tangent to the level set (Lemma 15).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Analysis of Descent Steps", "weight": 1.0} -->

In this section, we show that this property, combined with facts of high-dimensional geometry, implies that moving in a random direction from any point has a good chance of significantly improving the objective.\As we mentioned before, the key to fast convergence is the careful choice of step sizes, which we describe in Theorem 7. The intuition here is that we would like to take as large steps as possible while keeping the probability of improving the objective function reasonably high, so by insights in high-dimensional geometry, we choose a step size of $\Theta{({1/\sqrt{n}})}$. Also, we show that if $f{(x)}$ admits a latent rank-$k$ structure, then this step size can be increased to $\Theta{({1/\sqrt{k}})}$ and is therefore only dependent on the latent dimensionality of $f{(x)}$, allowing for fast high-dimensional optimization. Lastly, our geometric understanding allows us to show that our convergence rates are optimal with a matching lower bound.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Analysis of Descent Steps", "weight": 1.0} -->

Without loss of generality, this section assumes that $f{(x)}$ is strongly convex and smooth with condition number $Q$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gaussian Sampling and Low Rank Structure", "weight": 1.0} -->

A direct application of Lemma 8 seems to imply that uniform sampling of a high-dimensional ball is necessary. Upon further inspection, this can be easily replaced with a much simpler Gaussian sampling procedure that concentrates the mass close to the surface to the ball. This procedure lends itself to better analysis when $f{(x)}$ admits a latent low-dimensional structure since any affine projection of a Gaussian is still Gaussian.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

We show that our upper bounds given in the previous section are tight up to logarithmic factors for any symmetric sampling distribution $\mathcal{D}$. These lower bounds are easily derived from our geometric perspective as we show that a sampling distribution with a large radius gives an extremely low probability of intersection with the desired sub-level set. Therefore, while gradient-approximation algorithms can be accelerated to achieve a runtime that depends on the square-root of the condition number $Q$, gradient-less methods that rely on random sampling are likely unable to be accelerated according to our lower bound. However, we emphasize that monotone invariance allows these results to apply to a broader class of objective functions, beyond smooth and convex, so the results can be useful in practice despite the seemingly worse theoretical bounds.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Gradientless Algorithms", "weight": 1.0} -->

In this section, we present two algorithms that follow the same Gradientless Descent (GLD) template: GLD-Search and GLD-Fast, with the latter being an optimized version of the former when an upper bound on the condition number of a function is known. For both algorithms, since they are monotone-invariant, we appeal to the previous section to derive fast convergence rates for any monotone transform of convex $f{(x)}$ with good condition number. We show the efficacy of both algorithms experimentally in the Experiments section.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gradientless Descent with Binary Search", "weight": 1.0} -->

Although the sampling distribution $\mathcal{D}$ is fixed, we have a choice of radii for each iteration of the algorithm. We can apply a binary search procedure to ensure progress. The most straightforward version of our algorithm is thus with a naive binary sweep across an interval in $\lbrack r,R\rbrack$ that is unchanged throughout the algorithm. This allows us to give convergence guarantees without previous knowledge of the condition number at a cost of an extra factor of $\log{({n/\epsilon})}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gradientless Descent with Binary Search", "weight": 1.0} -->

Input: function: f: ℝn → ℝ, T ∈ ℤ+: number of iterations, x0: starting point, 𝒟: sampling distribution, R: maximum search radius, r: minimum search radius 3 Ball Sampling Trial: 9 Update: $x_{t + 1} = {{\arg\min\limits_{k}}\left\{ {f{(y)}} \middle| {{y = x_{t}},{y = {x_{t} + v_{k}}}} \right\}}$ Algorithm 1 Gradientless Descent with Binary Search (GLD-Search)

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gradientless Descent with Fast Binary Search", "weight": 1.0} -->

GLD-Search (Algorithm 1) uses a naive lower and upper bound for the search radius $\|{x_{t} - x^{\ast}}\|$, which incurs an extra factor of $\log{({1/\epsilon})}$ in the runtime bound. In GLD-Fast, we remove this extra factor dependence on $\log{({1/\epsilon})}$ by drastically reducing the range of the binary search. This is done by exploiting the assumption that $f$ has a good condition number upper bound $\hat{Q}$ and by slowly halfing the diameter of the search space every few iterations since we expect $x_{t}\rightarrow x^{\ast}$ as $t\rightarrow\infty$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gradientless Descent with Fast Binary Search", "weight": 1.0} -->

Input: function f: ℝn → ℝ, T ∈ ℤ+: number of iterations, x0: starting point, 𝒟: sampling distribution, R: diameter of search space, Q: condition number bound 1 Set $K = {\log{({4\sqrt{Q}})}}$, H = n Q log (Q) 3 Set R = R/2 when t ≡ 0mod H (every H iterations). 4 Ball Sampling Trial: 10 Update: $x_{t + 1} = {{\arg\min\limits_{k}}\left\{ {f{(y)}} \middle| {{y = x_{t}},{y = {x_{t} + v_{k}}}} \right\}}$ Algorithm 2 Gradientless Descent with Fast Binary Search (GLD-Fast)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

We tested GLD algorithms on a simple class of objective functions and compare it to Accelerated Random Search (ARS), which has linear convergence guarantees on strongly convex and strongly smooth functions. To our knowledge, ARS makes the weakest assumption among the zeroth-order algorithms that have linear convergence guarantees and perform only a constant order of operations per iteration. Our main conclusion is that GLD-Fast is comparable to ARS and tends to achieve a reasonably low error much faster than ARS in high dimensions ($\geq 50$). In low dimensions, GLD-Search is competitive with GLD-Fast and ARS though it requires no information about the function.\We let $H_{\alpha,\beta,n} \in {\mathbb{R}}^{n \times n}$ be a diagonal matrix with its $i$-th diagonal equal to $\alpha + {{({\beta - \alpha})}\frac{i - 1}{n - 1}}$. In simple words, its diagonal elements form an evenly space sequence of numbers from $\alpha$ to $\beta$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our objective function is then $f_{\alpha,\beta,n}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ as ${f_{\alpha,\beta,n}{(x)}} = {\frac{1}{2}x^{\top}H_{\alpha,\beta,n}x}$, which is $\alpha$-strongly convex and $\beta$-strongly smooth. We always use the same starting point $x = {\frac{1}{\sqrt{n}}{(1,\ldots,1)}}$, which requires $\left\| X \right\| = \sqrt{Q}$ for our algorithms. We plot the optimality gap ${f{(b_{t})}} - {f{(x^{\ast})}}$ against the number of function evaluations, where $b_{t}$ is the best point observed so far after $t$ evaluations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

Although all tested algorithms are stochastic, they have a low variance on the objective functions that we use; hence we average the results over 10 runs and omit the error bars in the plots.\We ran experiments on $f_{1,8,n}$ with imperfect curvature information $\hat{\alpha}$ and $\hat{\beta}$ (see Figure 3 in appendix). GLD-Search is independent of the condition number. GLD-Fast takes only one parameter, which is the upper bound on the condition number; if approximation factor is $z$, then we pass $8z$ as the upper bound. ARS requires both strong convexity and smoothness parameters. We test three different distributions of the approximation error; when the approximation factor is $z$, then ARS-alpha gets $({\alpha/z},\beta)$, ARS-beta gets ($\alpha,{z\beta}$), and ARS-even gets $({\alpha/\sqrt{z}},{\sqrt{z}\beta})$ as input.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

GLD-Fast is more robust and faster than ARS when the condition number is over-approximated. When the condition number is underestimated, GLD-Fast still steadily converges.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Monotone Transformations", "weight": 1.0} -->

In Figure 1, we ran experiments on $f_{1,8,n}$ for different settings of dimensionality $n$, and its monotone transformation with ${g{(y)}} = {- {\exp{({- \sqrt{y}})}}}$. For this experiment, we assume a perfect oracle for the strong convexity and smoothness parameters of $f$. The convergence of GLD is totally unaffected by the monotone transformation. For the low-dimension cases of a transformed function (bottom half of the figure), we note that there are inflection points in the convergence curve of ARS. This means that ARS initially struggles to gain momentum and then struggles to stop the momentum when it gets close to the optimum. Another observation is that unlike ARS that needs to build up momentum, GLD-Fast starts from a large radius and therefore achieves a reasonably low error much faster than ARS, especially in higher dimensions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "BBOB Benchmarks", "weight": 1.0} -->

To show that practicality of GLD on practical and non-convex settings, we also test GLD algorithms on a variety of BlackBox Optimization Benchmarking (BBOB) functions. For each function, the optima is known and we use the log optimality gap as a measure of competance. Because each function can exhibit varying forms of non-smoothness and convexity, all algorithms are ran with a smoothness constant of 10 and a strong convexity constant of 0.1. All other setup details are same as before, such as using a fixed starting point.\The plots, given in Appendix C, underscore the superior performance of GLD algorithms on various BBOB functions, demonstrating that GLD can successfully optimize a diverse set of functions even without explicit knowledge of condition number. We note that BBOB functions are far from convex and smooth, many exhibiting high conditioning, multi-modal valleys, and weak global structure. Due to our radius search produce, our algorithm appears more robust to non-ideal settings with non-convexity and ill conditioning. As expected, we note that GLD-Fast tend to outperform GLD-Search, especially as the dimension increases, matching our theoretical understanding of GLD.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mujoco Control Benchmarks and Affine Transformations", "weight": 1.0} -->

We also ran experiments on the Mujoco benchmarks with varying architectures, both linear and nonlinear. This demonstrates the viability of our approach even in the non-convex, high dimensional setting. We note that however, unlike e.g. ES which uses all queries to form a gradient direction, our algorithm removes queries which produce less reward than using the current arg-max, which can be an information handicap. Nevertheless, we see that our algorithm still achieves competitive performance on the maximum reward. We used a horizon of $1000$ for all experiments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mujoco Control Benchmarks and Affine Transformations", "weight": 1.0} -->

Rew. at (104, 105, Max) Queries Table 2: Final rewards by GLD with linear (L) and deep (H41) policies on Mujoco Benchmarks show that GLD is competitive. We apply an affine projection on HalfCheetah to test affine invariance. We use the reward threshold found with Reacher’s threshold [SWD+17] for a reasonable baseline.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Mujoco Control Benchmarks and Affine Transformations", "weight": 1.0} -->

We further tested the affine invariance of GLD on the policy parameters from using Gaussian ball sampling, under the HalfCheetah benchmark by projecting the state $s$ of the MDP with linear policy to a higher dimensional state $Ws$, using a matrix multiplication with an orthonormal $W$. Specifically, in this setting, for a linear policy parametrized by matrix $K$, the objective function is thus $J{({KW})}$ where ${\pi_{K}{({Ws})}} = {KWs}$. Note that when projecting into a high dimension, there is a slowdown factor of $\log\frac{d_{new}}{d_{old}}$ where $d_{new},d_{old}$ are the new high dimension and previous base dimension, respectively, due to the binary search in our algorithm on a higher dimensional space.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Mujoco Control Benchmarks and Affine Transformations", "weight": 1.0} -->

For our HalfCheetah case, we projected the 17 base dimension to a 200-length dimension, which suggests that the slowdown factor is a factor ${\log\frac{200}{17}} \approx 3.5$. This can be shown in our plots in the appendix (Figure 15).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced GLD, a robust zeroth-order optimization algorithm that is simple, efficient, and we show strong theoretical convergence bounds via our novel geometric analysis. As demonstrated by our experiments on BBOB and MuJoCo benchmarks, GLD performs very robustly even in the non-convex setting and its monotone and affine invariance properties give theoretical insight on its practical efficiency.\GLD is very flexible and allows easy modifications. For example, it could use momentum terms to keep moving in the same direction that improved the objective, or sample from adaptively chosen ellipsoids similarly to adaptive gradient methods.. Just as one may decay or adaptively vary learning rates for gradient descent, one might use a similar change the distribution from which the ball-sampling radii are chosen, perhaps shrinking the minimum radius as the algorithm progresses, or concentrating more probability mass on smaller radii.\Likewise, GLD could be combined with random restarts or other restart policies developed for gradient descent. Analogously to adaptive per--coordinate learning rates, one could adaptively change the shape of the balls being sampled into ellipsoids with various length-scale factors. Arbitrary combinations of the above variants are also possible.
