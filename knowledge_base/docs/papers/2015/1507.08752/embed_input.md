<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Optimal Algorithm for Bandit and Zero-Order Convex Optimization with Two-Point Feedback

Topics include Convex optimization, Bandits, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the closely related problems of bandit convex optimization with two-point feedback, and zero-order stochastic convex optimization with two function evaluations per round. We provide a simple algorithm and analysis which is optimal for convex Lipschitz functions. This improves , which only provides an optimal result for smooth functions; Moreover, the algorithm and analysis are simpler, and readily extend to non-Euclidean problems. The algorithm is based on a small but surprisingly powerful modification of the gradient estimator.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the problem of bandit convex optimization with two-point feedback. This problem can be defined as a repeated game between a learner and an adversary as follows: At each round $t$, the adversary picks a convex function $f_{t}$ on ${\mathbb{R}}^{d}$, which is not revealed to the learner. The learner then chooses a point $\mathbf{w}_{t}$ from some known and closed convex set $\mathcal{W} \subseteq {\mathbb{R}}^{d}$, and suffers a loss $f_{t}{(\mathbf{w}_{t})}$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As feedback, the learner may choose two points ${\mathbf{w}_{t}',\mathbf{w}_{t}^{\operatorname{\prime\prime}}} \in \mathcal{W}$ and receive^11^1This is slightly different than the model of, where the learner only chooses $\mathbf{w}_{t}',\mathbf{w}_{t}^{\operatorname{\prime\prime}}$ and the loss is $\frac{1}{2}\left({{f_{t}{(\mathbf{w}_{t}')}} + {f_{t}{(\mathbf{w}_{t}^{\operatorname{\prime\prime}})}}} \right)$. However, our results and analysis can be easily translated to their setting, and the model we discuss translates more directly to the zero-order stochastic optimization considered later.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

${f_{t}{(\mathbf{w}_{t}')}},{f_{t}{(\mathbf{w}_{t}^{\operatorname{\prime\prime}})}}$. The learner's goal is to minimize average regret, defined as In this note, we focus on obtaining bounds on the expected average regret (with respect to the learner's randomness).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A closely-related and easier setting is zero-order stochastic convex optimization. In this setting, our goal is to approximately solve ${F{(\mathbf{w})}} = {{\min_{\mathbf{w} \in \mathcal{W}}{\mathbb{E}}_{\xi}}{\lbrack{f{(\mathbf{w};\xi)}}\rbrack}}$, given limited access to ${\{{f{(\cdot;\xi_{t})}}\}}_{t = 1}^{T}$ where $\xi_{t}$ are i.i.d. instantiations. Specifically, we assume that each $f{(\cdot,\xi_{t})}$ is not directly observed, but rather can be queried at two points. This models situations where computing gradients directly is complicated or infeasible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is well-known that given an algorithm with expected average regret $R_{T}$ in the bandit optimization setting above, if we feed it with the functions ${f_{t}{(\mathbf{w})}} = {f{(\mathbf{w};\xi_{t})}}$, then the average ${\overline{\mathbf{w}}}_{T} = {\frac{1}{T}{\sum_{t = 1}^{T}\mathbf{w}_{t}}}$ of the points generated satisfies the following bound on the expected optimization error: Thus, an algorithm for bandit optimization can be converted to an algorithm for zero-order stochastic optimization with similar guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The bandit optimization setting with two-point feedback was proposed and studied. Independently, and considered two-point methods for stochastic optimization. Both papers are based on randomized gradient estimates which are then fed into standard first-order algorithms (e.g. gradient descent, or more generally mirror descent). However, the regret/error guarantees in both papers were suboptimal in terms of the dependence on the dimension. Recently, considered a similar approach for the stochastic optimization setting, attaining an optimal error guarantee when $f{( \cdot;\xi)}$ is a smooth function (differential and with Lipschitz-continuous gradients). Related results in the smooth case were also obtained. However, to tackle the general case, where $f{( \cdot;\xi)}$ may be non-smooth, resorted to a non-trivial smoothing scheme and a significantly more involved analysis. The resulting bounds have additional factors (logarithmic in the dimension) compared to the guarantees in the smooth case.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, an analysis is only provided for Euclidean problems (where the domain $\mathcal{W}$ and Lipschitz parameter of $f_{t}$ scale with the $L_{2}$ norm).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this note, we present and analyze a simple algorithm with the following properties: For Euclidean problems, it is optimal up to constants for both smooth and non-smooth functions. This closes the gap between the smooth and non-smooth Euclidean problems in this setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The algorithm and analysis are readily applicable to non-Euclidean problems. We give an example for the $1$-norm, with the resulting bound optimal up to a $\sqrt{\log{(d)}}$ factor.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The algorithm and analysis are simpler than those proposed. They apply equally to the bandit and zero-order optimization setting, and can be readily extended using standard techniques (e.g. to strongly-convex functions, regret/error bounds holding with high-probability rather than just in expectation, and improved bounds if allowed $k > 2$ observations per round instead of just two).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Like previous algorithms, our algorithm is based on a random gradient estimator, which given a function $f$ and point $\mathbf{w}$, queries $f$ at two random locations close to $\mathbf{w}$, and computes a random vector whose expectation is a gradient of a smoothed version of $f$. The papers essentially use the estimator which queries at $\mathbf{w}$ and $\mathbf{w} + {\delta\mathbf{u}}$ (where $\mathbf{u}$ is a random unit vector and $\delta > 0$ is a small parameter), and returns The intuition is readily seen in the one-dimensional ($d = 1$) case, where the expectation of this expression equals which indeed approximates the derivative of $f$ (assuming $f$ is differentiable) at $w$, if $\delta$ is small enough.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, our algorithm uses a slightly different estimator (also used in), which queries at ${\mathbf{w} - {\delta\mathbf{u}}},{\mathbf{w} + {\delta\mathbf{u}}}$, and returns Again, the intuition is readily seen in the case $d = 1$, where the expectation of this expression also equals Eq..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

When $\delta$ is sufficiently small and $f$ is differentiable at $\mathbf{w}$, both estimators compute a good approximation of the true gradient ${\nabla f}{(\mathbf{w})}$. However, when $f$ is not differentiable, the variance of the estimator in Eq. can be quadratic in the dimension $d$, as pointed out: For example, for ${f{(\mathbf{w})}} = {\|\mathbf{w}\|}_{2}$ and $\mathbf{w} = 0$, the second moment equals Since the performance of the algorithm crucially depends on the second moment of the gradient estimate, this leads to a highly sub-optimal guarantee. In, this was handled by adding an additional random perturbation and using a more involved analysis. Surprisingly, it turns out that the slightly different estimator in Eq. does not suffer from this problem, and its second moment is essentially linear in the dimension $d$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Algorithm and Main Results", "weight": 1.0} -->

We consider the algorithm described in Figure 1, which performs standard mirror descent using a randomized gradient estimator ${\overset{\sim}{\mathbf{g}}}_{t}$ of a (smoothed) version of $f_{t}$ at point $\mathbf{w}_{t}$. We make the assumption that one can indeed query $f_{t}$ at any point $\mathbf{w}_{t} + {\delta_{t}\mathbf{u}_{t}}$ as specified in the algorithm^22^2This may require us to query at a distance $\delta_{t}$ outside $\mathcal{W}$. If we must query within $\mathcal{W}$, then one can simply run the algorithm on a slightly smaller set ${({1 - \delta})}\mathcal{W}$, where $\delta \geq \delta_{t}$ for all $t$, ensuring that we always query at $\mathcal{W}$. Since the formal guarantee in Thm.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Algorithm and Main Results", "weight": 1.0} -->

1 holds for arbitrarily small $\delta_{t}$, and each $f_{t}$ is Lipschitz, we can always take $\delta$ and $\delta_{t}$ small enough so that the additional regret/error incurred is negligible..
