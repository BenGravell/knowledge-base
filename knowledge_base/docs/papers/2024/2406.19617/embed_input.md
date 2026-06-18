<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Zeroth-Order Optimization under Strongly Convexity and Lipschitz Hessian: Minimax Sample Complexity

Topics include Regret bounds, Online algorithms, Sample complexity, Optimization, Learning, Sampling, Hessian.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Optimization of convex functions under stochastic zeroth-order feedback has been a major and challenging question in online learning. In this work, we consider the problem of optimizing second-order smooth and strongly convex functions where the algorithm is only accessible to noisy evaluations of the objective function it queries. We provide the first tight characterization for the rate of the minimax simple regret by developing matching upper and lower bounds. We propose an algorithm that features a combination of a bootstrapping stage and a mirror-descent stage. Our main technical innovation consists of a sharp characterization for the spherical-sampling gradient estimator under higher-order smoothness conditions, which allows the algorithm to optimally balance the bias-variance tradeoff, and a new iterative method for the bootstrapping stage, which maintains the performance for unbounded Hessian.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic optimization of an unknown function with access to only noisy function evaluations is a fundamental problem in operations research, optimization, simulation and bandit optimization research, commonly known as *zeroth-order optimization*, *derivative-free optimization* (Conn et al. Rios & Sahinidis, ) or *bandit optimization*. In this problem, an optimization algorithm interacts sequentially with an oracle and obtains noisy function evaluations at queried points every time. The algorithm produces an approximately optimal solution after $T$ such evaluations, with its performance evaluated by the expected difference between the function values at the approximate optimal solution produced and the optimal solution. A more rigorous formulation of the problem is given in Sec. below.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convex functions. In the first thread of research, the unknown objective function to be optimized is assumed to be *concave* (for maximization problems) or *convex* (for minimization problems). For these problems, with minimal smoothness (e.g. objective function being Lipschitz continuous) it is possible to achieve a sample complexity of $\overset{\sim}{O}{(\varepsilon^{- 2})}$ for an expected optimization error or $\varepsilon$, which is also a polynomial function of domain dimension $d$; see for example the works of Agarwal et al.; Lattimore & Gyorgy; Bubeck et al.;

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Smooth functions. In the second thread of research, the unknown objective function to be optimized is assumed to be highly *smooth*, but not necessary concave/convex. Typical results assume the objective function is Hölder smooth of order $k \geq 1$, meaning that the $({k - 1})$-th derivative of the objective function is Lipschitz continuous. Without additional conditions, the optimal sample complexity with such smoothness assumptions is $\overset{\sim}{O}{(\varepsilon^{- {({2 + {d/k}})}})}$, which scales exponentially with the domain dimension $d$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the optimal sample complexity of stochastic zeroth-order optimization when the objective function exhibits both (strong) convexity and a high degree of smoothness. As we have remarked in the first bullet point above, with convexity and Hölder smoothness of order $k = 1$ (equivalent to the objective function being Lipschitz continuous), the works of Agarwal et al.; Lattimore & Gyorgy; Bubeck et al. established an $\overset{\sim}{O}{(\varepsilon^{- 2})}$ upper bound. With higher order of Hölder smoothness, i.e., $k = 2$ (equivalent to the gradient of the objective being Lipschitz continuous), it is shown that simpler algorithms exist but the sample complexity remains $\overset{\sim}{O}{(\varepsilon^{- 2})}$ (Besbes et al. Agarwal et al. Hazan & Levy, ), which seemingly suggests the relatively smaller role smoothness plays in the presence of convexity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we show that with even higher order of Hölder smoothness, i.e., $k = 3$ (specifically, the Hessian of the objective being Lipschitz continuous), the optimal sample complexity is improved to $O{(\varepsilon^{- 1.5})}$, which is significantly smaller than the sample complexity of the convex-without-smoothness setting $\overset{\sim}{O}{(\varepsilon^{- 2})}$, or the smooth-without-convexity setting $\overset{\sim}{O}{(\varepsilon^{- {({2 + {d/3}})}})}$. More importantly, when the Lipschitzness of Hessian is defined in Frobenius norm (see condition A1), we propose an algorithm that also achieves the optimal dimension dependency, which fully characterizes the optimal sample complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Summary of technical contributions", "weight": 1.0} -->

We developed several important techniques in this paper to achieve the optimal sample complexity when the objective function is strongly convex and has Lipschitz Hessian. First, we show that when estimating the gradient under a stochastic environment, even with an unbounded action space, it could be beneficial to sample with non-isotropic distributions (as opposed to conventional standard Gaussian, or uniform distributions on hyperspheres). Second, we present a new approach to analyze the bias and variance of the hyperellipsoid-sampling-based gradient estimators, which enables obtaining sharp bounds with tight constants and strengthens the best-known results in the higher-order smoothness case. Third, we present a two-stage bootstrap-type framework for the algorithmic design, which extends the perturbative analysis in the final stage to the full regime. This extension relies on a non-trivial modification of Newton's method, and we proved its robustness under stochastic observation. We complete the characterization of the minimax regret by deriving a lower bound using the KL-divergence-based approach.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

\mathbf{1}}})}$ Recent years have seen increasing attention on exploiting higher order smoothness in bandit optimization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Remarkably, it was shown that when the Hölder smoothness condition holds simultaneously for both k = 2 and k = 3, the optimal sample complexity can be improved to O(ε−1.5).. We list our results together with the most relevant work in Table 1. While this line of work also demonstrates the benefit of higher-order smoothness in improving the sample complexity, their setting is related but slightly different from what we considered in this work. (See reference therein: Bach &amp; Perchet; Akhavan et al.; Novitskii &amp; Gasnikov ). On one hand, the prior work concentrates on projected gradient-descent-like algorithms, which require a Lipschitz gradient (i.e., the k = 2 requirement, and we do not).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

This additional requirement can not be removed by simply replacing the gradient steps with Newton’s methods, which can lead to unbounded expectation in simple regret in the stochastic case.111We note that even in the classical analysis of Newton’s method, which assumes zero-error observations, the additional k = 2 smoothness condition was adopted to obtain non-trivial complexity bounds (e.g., see Boyd &amp; Vandenberghe, Section 9.5.3), implying the non-trivialness of removing the k = 2 smoothness condition. In this work, we provided an analysis for our proposed bootstrapping algorithm, which ensures the achievability of bounded expected regret even with unbounded hessian. On the other hand, their results are based on the generalized Hölder condition, which is different from our assumption that the Hessian is Lipschitz in Frobenius norm. Therefore we only emphasize the dependence of d, T and M in Table 1 and omit other parameters. We provide a detailed comparison on the implication of these results in Appendix A.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Our results are also related to a special case discussed, which shows that for quadratic functions it is possible to achieve a sample complexity of $\overset{\sim}{O}{(\varepsilon^{- 1})}$. As quadratic functions are infinitely differentiable with bounded derivatives on orders, they are Hölder smooth of any arbitrary order k → ∞, which could be regarded as an extreme of the results established in this paper which only require k = 3. Related works on gradient estimators. Gradient estimation serves as a key building block for stochastic zeroth-order optimization algorithms. For instance, a classical one-point estimator was proposed as early as in Flaxman et al.; Blair, where the gradient ∇f(x) is estimated based on empirical measures of f(x+ru) for some fixed r and i.i.d. uniformly random u on the unit hypersphere. This was later refined to be two-point estimators, and the sampling distribution of u was generalized to isotropic distributions such as standard Gaussian (e.g., see Agarwal et al.; Bach &amp; Perchet; Zhang et al. ).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

A majority of prior work focused on the analysis for such estimators under the Lipschitz gradient assumption, where the best guaranteed bound for the bias is at the order of Θ(r), with a polynomial factor dependent on d. The line of works by Bach &amp; Perchet; Akhavan et al.; Novitskii &amp; Gasnikov also adopted isotropic sampling, and it was shown that with higher-order smoothness of k = 3, this bound can be improved to Θ(r2). The improvement of sample complexity in our work is mainly due to the tight characterization of our gradient estimator, which covers the special case of isotropic sampling and provides a bound of $\frac{r^{2}\rho\sqrt{d}}{2{({d + 2})}}$ in the estimation bias. This strengthens or improves the bounds presented in prior works, and a detailed comparison can be found in Appendix A. On the other hand, non-isotropic sampling was used as early as in Abernethy et al., then extended in Saha &amp; Tewari; Hazan &amp; Levy.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Primarily, they were used to ensure that the sampling points are contained within a bounded action set. showed the necessity of non-isotropic sampling over quadratic loss function in the adversarial setting. In this work, we essentially demonstrated that non-isotropic sampling can be used to refine a preliminary algorithm by adding a mirror-descent-like final stage. More recently, non-isotropic sampling was also adopted in Lattimore &amp; György to optimize convex and global Lipschitz functions. We follow the convention of machine learning theory where ∇2f(x) denotes the Hessian of f at point x, while the trace of Hessian is denoted by Tr(∇2f(x)). This should not be confused with the notation in classical field theory, where ∇2f(x) instead denotes the trace of the Hessian. We use ∥ ⋅ ∥2 to denote vector ℓ2 norms, and ∥ ⋅ ∥F to denote matrix Frobenius norms. We use Id to denote the identity matrix, and Sd − 1 to denote the unit hypersphere centered at the origin, both for the d-dimensional Euclidean space ℝd.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

We adopt the conventional notations (i.e., O, Ω, o, and ω) to describe regret bounds in the asymptotic sense with respect to the total number of samples (denoted by T). We consider the stochastic optimization problem under the class of functions that are strongly convex and have Lipschitz Hessian. The goal in this setting is to design learning algorithms to achieve approximately the global minimum of an unknown objective function f: ℝd → ℝ. A learning algorithm 𝒜 can interact with the function by adaptively sampling their value for T times, and receive noisy observations. At each time t ∈ [T], the algorithm selects xt ∈ ℝd, and receives the following observation,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where {wt}t = 1T are independent random variables with zero mean and bounded variance. Formally, the algorithm can be described by a list of conditional distributions where each xt is selected based on all historical data {xτ, yτ}τ &lt; t and the corresponding distribution. Then for any t, we assume that 𝔼[wt|{xτ, yτ}τ &lt; t,xt] = 0 and Var[wt|{xτ, yτ}τ &lt; t,xt] ≤ 1 for any t.222If the variances of wt’s are bounded by a different constant, all our results can be reproduced by normalizing the values of f. For simplicity, we also adopt a common assumption that the additive noises are subgaussian, particularly, ℙ[|wt| &gt; s|{xτ, yτ}τ &lt; t,xt] ≤ 2e−s2 for all s &gt; 0 and t ∈ [T].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

However, the subgaussian assumption can be removed by adopting more sophisticated mean-estimation methods (e.g., see Nemirovskii &amp; Yuom; Jerrum et al.; Alon et al.; Lee &amp; Valiant; Yu et al. ). We assume that the objective function f is second-order differentiable. Furthermore, we impose the following conditions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

(Lipschitz Hessian). There exist a constant ρ ∈ (0,+∞) such that for all x, x′ ∈ ℝd, it holds that ∥∇2f(x) − ∇2f(x′)∥F ≤ ρ∥x′ − x∥2, where ∥ ⋅ ∥F denotes the Frobenius norm;
(Strong Convexity). There exists a constant M ∈ (0,+∞) such that for any x ∈ ℝd, the minimum eigenvalue of the Hessian ∇2f(x) is greater than M.
(Bounded Distance from Initialization to Optimum Point). There exists a constant R ∈ (0,+∞) such that the infimum of f(x) within the hyperball ∥x∥2 ≤ R is identical to the infimum of f(x) over the entire ℝd.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

In the rest of this paper, we let ℱ(ρ,M,R) denote the set of all second-order differentiable functions that satisfy the above conditions, with corresponding constants given by ρ, M, and R. We aim to find algorithms to achieve asymptotically the following minimax simple regret, which measures the expected difference of the objective function on xT and the optimum.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where x* denotes the global minimum point of f. For any dimension d and constants ρ, M, R, the minimax simple regrets are upper bounded by ${\operatorname{lim\ sup}_{T\rightarrow\infty}{{\Re{(T;\rho,M,R)}} \cdot T^{\frac{2}{3}}}} \leq {C \cdot \left( {\frac{\rho^{\frac{2}{3}}}{M}d} \right)}$, where C is a universal constant.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

For any fixed dimension d and constants ρ, M, R, the minimax simple regrets are lower bounded by ${\operatorname{lim\ inf}_{T\rightarrow\infty}{{\Re{(T;\rho,M,R)}} \cdot T^{\frac{2}{3}}}} \geq {C \cdot \left( {\frac{\rho^{\frac{2}{3}}}{M}d} \right)}$ when the additive noises w1, …, wT are standard Gaussian, where C is a universal constant. 4 Proof Ideas for Theorem 3.1
The proposed algorithm operates in two stages (see Algorithm 4). In the first stage, the algorithm uses a small fraction of samples to obtain a rough estimation of the global minimum point. We ensure that the estimation in the first stage is sufficiently accurate with high probability, so that in the following final stage, the objective function can be approximated by a quadratic function and the resulting approximation error can be bounded using tensor analysis.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

4.1 Key Techniques and The Final Stage
We first present the key steps of our algorithm, which relies on the subroutines presented in Algorithm 1-3, i.e., GradientEst, BootstrappingEst, and HessianEst. These subroutines estimate the (linearly transformed) gradients and Hessian functions of f at any given point by sampling the values of f on hyperellipsoids. The key ingredient of our proof is the sharp characterizations for the biases and variances of the GradientEst estimator, stated in Theorem 4.1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Input: x, Z, n ⊳ Z is a d × d matrix, return $\hat{\mathbf{g}}$ as an estimator of Z∇f(x)
Let uk be a point sampled uniformly randomly from the standard hypersphere Sd − 1
Let let y+, y− be samples of f at x + Zuk and x − Zuk, respectively, let ${\mathbf{g}}_{k} = {\frac{d}{2}{({y_{+} - y_{-}})}{\mathbf{u}}_{k}}$
Return $\hat{\mathbf{g}} = {\frac{1}{n}{\sum_{k = 1}^{n}{\mathbf{g}}_{k}}}$

<!-- chunk {"id": "body-0024", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Input: x, r, n⊳ Goal: estimate ∇f(x) coordinate wise with O(nd) samples
Let e1, …, ed be any orthonormal basis of ℝd
Let y+,k, y−,k each be the average of n samples of f at x + rek and x − rek respectively
Let mk = (y+−y−)/2r ⊳ Estimate the kth entry
Return $\hat{\mathbf{m}} = {\{ m_{k}\}}_{k \in {\lbrack d\rbrack}}$

<!-- chunk {"id": "body-0025", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Input: x, r, n⊳ Goal: estimate ∇2f(x) coordinate wise with O(nd2) samples
Let e1, …, ed be any orthonormal basis of ℝd
Let y be the average of n samples of f at x
Let y+,k, y−,k each be the average of n samples of f at x + rek and x − rek respectively
Let Hkk = (y+ + y−−2y)/r2 ⊳ Diagonal entries
Let Hkℓ = Hℓk be the average of n samples of (f(x+rek+reℓ) + f(x−rek−reℓ)−
f(x+rek−reℓ) − f(x−rek+reℓ))/4r2 ⊳ Off-diagonal entries
Let Ĥ0 = {Hjk}(i,j) ∈ [d]2, and Ĥ be the matrix with same eigenvectors but with each eigenvalue λ replaced by max {λ, M} ⊳ Projecting to the set where Ĥ − MId is positive semidefinite

<!-- chunk {"id": "body-0026", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

For any fixed inputs x, Z, n, and any function f satisfying the Lipschitz Hessian condition with parameter ρ, the output $\hat{\mathbf{g}}$ returned by the GradientEst subroutine satisfies the following properties

<!-- chunk {"id": "body-0027", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where λZ is the largest singular value of Z.
Inequality provides a sharp characterization for the bias of the gradient estimator, as it can be matched for any λZ and d with a cubic polynomial f. Inequality is sharp in the asymptotic regime when both ∇f and λZ approaches zero.
We also provide rough estimates on the high-probability bounds for the BootstrappingEst and the HessianEst functions. Specifically, we show that their errors have sub-Gaussain tails in distribution, as stated in the following theorem.
For any fixed inputs x, r, n, any function f satisfying the Lipschitz Hessian condition with parameter ρ, and any variable K &gt; 0, the outputs $\hat{\mathbf{m}}$ and Ĥ returned by the BootstrappingEst and the HessianEst subroutine satisfy the following conditions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

We postpone the proof of the above theorems to Section 4.2 and Appendix C and proceed to describe how these results are used in the algorithm.
For brevity, let $\epsilon \triangleq {\frac{\rho^{\frac{2}{3}}}{M}dT^{- \frac{2}{3}}}$ be the minimax regret we aim to achieve, and let xB denote the estimator x stored at the end of the first stage. The role of the final stage is to ensure that if f(xB) − f(x*) is sufficiently small with high probability, the final result of the proposed algorithm achieves the stated simple regret guarantees. Formally, we require that

<!-- chunk {"id": "body-0029", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Note that the above condition implies that f(xB) − f(x*) concentrates below $o\left( \epsilon^{\frac{2}{3}} \right)$, which is weaker than the O(ϵ) rates stated in our main theorems.333With more sophisticated analysis, this concentration requirement can be improved to only requiring a similar upper bound of $o\left( \epsilon^{\frac{1}{2}} \right)$. However, we choose equation to provide a simpler proof, as it does not affect the asymptotic sample complexity. The bottleneck of the overall algorithm is on the final stage, and one can achieve equation using any suboptimal algorithm with an expected simple regret of $o{(T^{- \frac{4}{9}})}$. For example, one can run the suboptimal algorithm twice, estimate their achieved function values by averaging over o(T) samples, and then choose the outcome with the smaller estimated function value as xB. In the rest of this section, we prove Theorem 3.1 assuming the correctness of equation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

A self-contained proof for equation is provided in Appendix E.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Before proceeding with the proof, we provide a high-level description of the algorithm in the final stage. At the beginning, we perform a Hessian estimation near xB using the HessianEst subroutine with O(T) samples. From Theorem 4.3, our choice of parameters results in an expected estimation error of o for sufficiently large T. The algorithm proceeds to find a real matrix ZH, which essentially serves as a linear transformation on the action domain such that the Hessian of the transformed function is approximately the identity matrix. Note that the projection step in the HessianEst function ensures the eigenvalues of the estimator are no less than M. There is always a valid solution of ZH. Then, we estimate the gradient at xB using the GradientEst subroutine, which samples on a hyperellipsoid with a shape characterized by ZH. We chose the hyperellipsoid sampling in the final stage due to its superior performance in the small-gradient regime compared to coordinate-wise sampling.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

In contrast, the coordinate-wise estimator is used in the bootstrapping stage to eliminate the dependency of the local gradient on its bias-variance tradeoff, which is beneficial for the non-asymptotic analysis. Particularly, we scale the hyperellipsoid with a carefully designed factor (see the definition of variable rg) to minimize the estimation error. Then, the remaining steps can be interpreted as a modified Newton step, which essentially approximates the global minimum point with a quadratic approximation. The analysis in our proof relies on the following proposition, which is proved in Appendix D.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Furthermore, if x is generated by the final stage of Algorithm 4 with any parameter values that satisfy ng ≥ d3, $n_{\text{H}} \geq \frac{64\rho^{4}d^{6}}{M^{6}}$ and the first-stage output is set to xB, then

<!-- chunk {"id": "body-0034", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Now, we use Proposition 4.4 to prove the achievability result.
Proof of Theorem 3.1 given inequality..
First, recall our construction ensures that ${\|{{\mathbf{x}}_{T} - {\mathbf{x}}_{\text{B}}}\|}_{2} \leq \frac{M}{\rho}$. Inequality can always be applied and we have

<!-- chunk {"id": "body-0035", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Then, when T is sufficiently large, the conditions of holds and we have

<!-- chunk {"id": "body-0036", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

To prove inequality, we investigate the following function

<!-- chunk {"id": "body-0037", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where Unif(Sd − 1) denotes the uniform distribution on Sd − 1. Recall that in our algorithm we have ${{\mathbb{E}}{\lbrack\hat{\mathbf{g}}\rbrack}} = {r{\mathbf{G}}{(r;{\mathbf{x}})}}$ if Z = rId for some r ∈ ⟬0, + ∞), and by differentiability we have ∇f(x) = limz → 0+G(z;x). Under this condition, we can bound ${\|{{{\mathbb{E}}{\lbrack\hat{\mathbf{g}}\rbrack}} - {r{\nabla f}{({\mathbf{x}})}}}\|}_{2}$ by integration, i.e.,

<!-- chunk {"id": "body-0038", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Note that G(z;x) can be written into the following equivalent form.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where the integration is with respect to u over the surface Sd − 1, and dA is the vector surface element, i.e., with the magnitude being the infinitesimally small surface area and the direction perpendicular to the surface (pointing outward). The differential of G(z;x) over z can be written as

<!-- chunk {"id": "body-0040", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

The gist of this proof is to note that for any u ∈ S we have u and dA are parallel (i.e., u is parallel to the normal vector of the hypersphere at the same point), so the second term in the integral above on the numerator can be written as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where Bd denotes the standard hyperball.
Now consider any unit vector e. Let ue denote the reflection of u with respect to the hyperplane orthogonal to e, i.e., ue ≜ u − 2(u⋅e)e. Because the hyperball B is invariant under the reflection u → ue, equation (4.2) can also be written as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Hence, by averaging equation (4.2) and, we have

<!-- chunk {"id": "body-0043", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

By the Lipschitz Hessian condition and Cauchy’s inequality, the difference between the differential terms above can be bounded as follows.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

Note that e can be any unit vector. We have essentially bounded the ℓ2 norm of $\frac{d}{dz}{\mathbf{G}}{(z;{\mathbf{x}})}$, i.e.,

<!-- chunk {"id": "body-0045", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

As mentioned earlier, when Z = rId inequality is obtained by applying this gradient-norm bound to inequality.
For general input matrix Z, we can view GradientEst as a subroutine that operates on the same function f but with a linear transformation applied to the input domain. Formally, let ${f^{\prime}{({\mathbf{y}})}} \triangleq {f{({{\mathbf{x}} + {\frac{Z}{\lambda_{Z}}{({{\mathbf{y}} - {\mathbf{x}}})}}})}}$. We have that f′ satisfies the Lipschitz Hessian condition with parameter ρ as well. Therefore, inequality can be obtained following the same analysis by replacing f with f′ and Z with λZId.
Now we present the proof for inequality. Formally, let w+, w− be two independent samples of additive noises. Then the trace of covariance matrix of $\hat{\mathbf{g}}$ can upper bounded using the second moments of single measurements.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

The identity above uses the fact that additive noises are unbiased and have bounded variances.
Note that from the Lipschitz Hessian condition, we have that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where f2 is the Taylor polynomial of f expanded at x up to the quadratic terms. Consequently, inequality (4.2) implies

<!-- chunk {"id": "body-0048", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

where the expectations are taken of u ∼ Unif(Sd − 1), and the last equality is due to the well-known fact that ${{\mathbb{E}}\left\lbrack {{\mathbf{u}}{\mathbf{u}}^{\intercal}} \right\rbrack} = {\frac{1}{d}I_{d}}$. 5 Conclusion and Future Work
In this work, we achieve the first minimax simple regret for bandit optimization of second-order smooth and strongly convex functions. We derived the matching upper and lower bounds and proposed an algorithm that integrates a bootstrapping stage with a mirror-descent stage. Our key technical innovations include a sharp characterization of the spherical-sampling gradient estimator under higher-order smoothness conditions and a novel iterative method for the bootstrapping stage that remains effective with unbounded Hessians. While these advancements settle the fundamental problem of optimizing second-order smooth and strongly convex functions with zeroth-order feedback, the techniques and insights presented in this paper also pave the way for further research in this domain.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Additional related works on higher-order smoothness", "weight": 1.0} -->

One interesting follow-up direction is to generalize our analysis to the online setting for the average regret metric. Additionally, investigating the fundamental tradeoff between simple regret and average regret could yield valuable insights for task-specific algorithmic designs.
