The First Optimal Algorithm for Smooth and Strongly-Convex-Strongly-Concave Minimax Optimization

Topics include Optimization.

In this paper, we revisit the smooth and strongly-convex-strongly-concave minimax optimization problem. Zhang et al. and Ibrahim et al. established the lower bound Omega(sqrt(kappa_xkappa_y) log frac1epsilon) on the number of gradient evaluations required to find an epsilon-accurate solution, where kappa_x and kappa_y are condition numbers for the strong convexity and strong concavity assumptions. However, the existing state-of-the-art methods do not match this lower bound: algorithms of Lin et al. and Wang and Li have gradient evaluation complexity O( sqrt(kappa_xkappa_y)log^frac1epsilon) and O( sqrt(kappa_xkappa_y)log^ (kappa_xkappa_y)logfrac1epsilon), respectively. We fix this fundamental issue by providing the first algorithm with O(sqrt(kappa_xkappa_y)logfrac1epsilon) gradient evaluation complexity. We design our algorithm in three steps: (i) we reformulate the original problem as a minimization problem via the pointwise conjugate function; (ii) we apply a specific variant of the proximal point algorithm to the reformulated problem; (iii) we compute the proximal operator inexactly using the optimal algorithm for operator norm reduction in monotone inclusions.

### Introduction

In this paper, we revisit the smooth and strongly-convex-strongly-concave minimax optimization problem of the form

where ${F{(x,y)}}:{{{\mathbb{R}}^{d_{x}} \times {\mathbb{R}}^{d_{y}}}\rightarrow{\mathbb{R}}}$ is a continuously differentiable function, ${r{(x)}}:{{\mathbb{R}}^{d_{x}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$ and ${g{(y)}}:{{\mathbb{R}}^{d_{y}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$ are proper lower semi-continuous convex functions. Problem has been actively studied in economics, game theory, statistics and computer science....

Now, we are ready to provide the final gradient complexity of Algorithm 4. It is done by the following theorem.
Let parameters of Algorithm 4 be defined as follows: $\alpha = {\min\left\{ 1,\sqrt{\theta_{y}\mu_{y}} \right\}}$, θy = 8 μx−1, $\lambda = \left( {2\sqrt{5}{({1 + {{8L}/\mu_{x}}})}} \right)^{- 1}$, stepsizes ηz and ηy are defined by, parameters γx and γy are defined by, parameters {βt}t = 0∞ are defined by. Then, to find an ϵ-accurate solution of problem, Algorithm 4 requires the following number of gradient evaluations:

Without loss of generality we can assume μx ≥ μy, otherwise we just swap variables x and y in problem. Hence, Algorithm 4 has the following gradient evaluation complexity:

where (zfk + 1,yfk + 1) ∈ ℝdx × ℝdy is computed via the following auxiliary minimization problem:

One can observe that for fixed y ∈ ℝdy, function G (⋅,y) is nothing else but the Fenchel conjugate333Recall that for a convex function h (x), Fenchel conjugate is defined as h* (z) = supx[⟨z, x⟩ − h (x)]. of function r (⋅) + F̂ (⋅,y) − g (y). Moreover, function G (z,y) is defined as a pointwise supremum of a family of convex and lower semi-continuous functions {φx (z,y) = ⟨x, z⟩ − r (x) − F (x,y) + g (y)∣x ∈ ℝdx}. Hence, G (z,y) is also convex and lower semi-continuous function....

Algorithm 3 Extra Anchored Gradient for Monotone Inclusions

In our paper, we focus on the case when function $f{(x,y)}$ is strongly convex in $x$ and strongly concave in $y$. There are several reasons to consider this function class. First, this setting is fundamental and studied by most existing works on minimax optimization.^11^1Most existing works on minimax optimization study the convex-concave case....
