The First Optimal Algorithm for Smooth and Strongly-Convex-Strongly-Concave Minimax Optimization

Topics include Optimization.

In this paper, we revisit the smooth and strongly-convex-strongly-concave minimax optimization problem. Zhang et al. and Ibrahim et al. established the lower bound Omega(sqrt(kappa_xkappa_y) log frac1epsilon) on the number of gradient evaluations required to find an epsilon-accurate solution, where kappa_x and kappa_y are condition numbers for the strong convexity and strong concavity assumptions. However, the existing state-of-the-art methods do not match this lower bound: algorithms of Lin et al. and Wang and Li have gradient evaluation complexity O( sqrt(kappa_xkappa_y)log^frac1epsilon) and O( sqrt(kappa_xkappa_y)log^ (kappa_xkappa_y)logfrac1epsilon), respectively. We fix this fundamental issue by providing the first algorithm with O(sqrt(kappa_xkappa_y)logfrac1epsilon) gradient evaluation complexity. We design our algorithm in three steps: (i) we reformulate the original problem as a minimization problem via the pointwise conjugate function; (ii) we apply a specific variant of the proximal point algorithm to the reformulated problem; (iii) we compute the proximal operator inexactly using the optimal algorithm for operator norm reduction in monotone inclusions.

## Introduction

In this paper, we revisit the smooth and strongly-convex-strongly-concave minimax optimization problem of the form

where ${F{(x,y)}}:{{{\mathbb{R}}^{d_{x}} \times {\mathbb{R}}^{d_{y}}}\rightarrow{\mathbb{R}}}$ is a continuously differentiable function, ${r{(x)}}:{{\mathbb{R}}^{d_{x}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$ and ${g{(y)}}:{{\mathbb{R}}^{d_{y}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$ are proper lower semi-continuous convex functions. Problem has been actively studied in economics, game theory, statistics and computer science.

In our paper, we focus on the case when function $f{(x,y)}$ is strongly convex in $x$ and strongly concave in $y$. There are several reasons to consider this function class. First, this setting is fundamental and studied by most existing works on minimax optimization.^11^1Most existing works on minimax optimization study the convex-concave case. However, this setting can be easily reduced to the strongly-convex-strongly-concave case via the regularization technique. Second, efficient algorithms initially developed for convex optimization often show state-of-the-art performance in non-convex applications.
