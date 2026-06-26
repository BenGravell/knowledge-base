<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The First Optimal Algorithm for Smooth and Strongly-Convex-Strongly-Concave Minimax Optimization

Topics include Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we revisit the smooth and strongly-convex-strongly-concave minimax optimization problem. Zhang et al. and Ibrahim et al. established the lower bound Omega(sqrt(kappa_xkappa_y) log frac1epsilon) on the number of gradient evaluations required to find an epsilon-accurate solution, where kappa_x and kappa_y are condition numbers for the strong convexity and strong concavity assumptions. However, the existing state-of-the-art methods do not match this lower bound: algorithms of Lin et al. and Wang and Li have gradient evaluation complexity O( sqrt(kappa_xkappa_y)log^frac1epsilon) and O( sqrt(kappa_xkappa_y)log^ (kappa_xkappa_y)logfrac1epsilon), respectively. We fix this fundamental issue by providing the first algorithm with O(sqrt(kappa_xkappa_y)logfrac1epsilon) gradient evaluation complexity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We design our algorithm in three steps: (i) we reformulate the original problem as a minimization problem via the pointwise conjugate function; (ii) we apply a specific variant of the proximal point algorithm to the reformulated problem; (iii) we compute the proximal operator inexactly using the optimal algorithm for operator norm reduction in monotone inclusions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, many applications of this problem appeared in machine learning, including adversarial training, prediction and regression problems, reinforcement learning and generative adversarial networks Arjovsky et al. Goodfellow et al.,.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our paper, we focus on the case when function $f{(x,y)}$ is strongly convex in $x$ and strongly concave in $y$. There are several reasons to consider this function class. First, this setting is fundamental and studied by most existing works on minimax optimization.^11^1Most existing works on minimax optimization study the convex-concave case. However, this setting can be easily reduced to the strongly-convex-strongly-concave case via the regularization technique. Second, efficient algorithms initially developed for convex optimization often show state-of-the-art performance in non-convex applications. Finally, we will further see that this fundamental setting is utterly understudied and lacks answers to even the most basic questions such as "What is the best possible algorithm for solving a problem in this setting?"^22^2In contrast to smooth convex-concave minimax optimization, the answer to this question for smooth convex minimization was given by Nesterov, several decades ago.
