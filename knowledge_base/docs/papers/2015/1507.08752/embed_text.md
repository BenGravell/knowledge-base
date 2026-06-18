## Introduction

We consider the problem of bandit convex optimization with two-point feedback. This problem can be defined as a repeated game between a learner and an adversary as follows: At each round $t$, the adversary picks a convex function $f_{t}$ on ${\mathbb{R}}^{d}$, which is not revealed to the learner. The learner then chooses a point $\mathbf{w}_{t}$ from some known and closed convex set $\mathcal{W} \subseteq {\mathbb{R}}^{d}$, and suffers a loss $f_{t}{(\mathbf{w}_{t})}$. As feedback, the learner may choose two points ${\mathbf{w}_{t}^{\prime},\mathbf{w}_{t}^{\operatorname{\prime\prime}}} \in \mathcal{W}$ and receive^11^1This is slightly different than the model of, where the learner only chooses $\mathbf{w}_{t}^{\prime},\mathbf{w}_{t}^{\operatorname{\prime\prime}}$ and the loss is $\frac{1}{2}\left( {{f_{t}{(\mathbf{w}_{t}^{\prime})}} + {f_{t}{(\mathbf{w}_{t}^{\operatorname{\prime\prime}})}}} \right)$. However, our results and analysis can be easily translated to their setting, and the model we discuss translates more directly to the zero-order stochastic optimization considered later. ${f_{t}{(\mathbf{w}_{t}^{\prime})}},{f_{t}{(\mathbf{w}_{t}^{\operatorname{\prime\prime}})}}$. The learner's goal is to minimize average regret, defined as

In this note, we focus on obtaining bounds on the expected average regret (with respect to the learner's randomness).

A closely-related and easier setting is zero-order stochastic convex optimization. In this setting, our goal is to approximately solve ${F{(\mathbf{w})}} = {{\min_{\mathbf{w} \in \mathcal{W}}{\mathbb{E}}_{\xi}}{\lbrack{f{(\mathbf{w};\xi)}}\rbrack}}$, given limited access to ${\{{f{( \cdot;\xi_{t})}}\}}_{t = 1}^{T}$ where $\xi_{t}$ are i.i.d. instantiations. Specifically, we assume that each $f{( \cdot,\xi_{t})}$ is not directly observed, but rather can be queried at two points. This models situations where computing gradients directly is complicated or infeasible. It is well-known that given an algorithm with expected average regret $R_{T}$ in the bandit optimization setting above, if we feed it with the functions ${f_{t}{(\mathbf{w})}} = {f{(\mathbf{w};\xi_{t})}}$, then the average ${\overline{\mathbf{w}}}_{T} = {\frac{1}{T}{\sum_{t = 1}^{T}\mathbf{w}_{t}}}$ of the points generated satisfies the following bound on the expected optimization error:

Thus, an algorithm for bandit optimization can be converted to an algorithm for zero-order stochastic optimization with similar guarantees.

The bandit optimization setting with two-point feedback was proposed and studied in. Independently, and considered two-point methods for stochastic optimization. Both papers are based on randomized gradient estimates which are then fed into standard first-order algorithms (e.g. gradient descent, or more generally mirror descent). However, the regret/error guarantees in both papers were suboptimal in terms of the dependence on the dimension. Recently, considered a similar approach for the stochastic optimization setting, attaining an optimal error guarantee when $f{( \cdot;\xi)}$ is a smooth function (differential and with Lipschitz-continuous gradients). Related results in the smooth case were also obtained by. However, to tackle the general case, where $f{( \cdot;\xi)}$ may be non-smooth, resorted to a non-trivial smoothing scheme and a significantly more involved analysis. The resulting bounds have additional factors (logarithmic in the dimension) compared to the guarantees in the smooth case. Moreover, an analysis is only provided for Euclidean problems (where the domain $\mathcal{W}$ and Lipschitz parameter of $f_{t}$ scale with the $L_{2}$ norm).

In this note, we present and analyze a simple algorithm with the following properties:

For Euclidean problems, it is optimal up to constants for both smooth and non-smooth functions. This closes the gap between the smooth and non-smooth Euclidean problems in this setting.

The algorithm and analysis are readily applicable to non-Euclidean problems. We give an example for the $1$-norm, with the resulting bound optimal up to a $\sqrt{\log{(d)}}$ factor.

The algorithm and analysis are simpler than those proposed in. They apply equally to the bandit and zero-order optimization setting, and can be readily extended using standard techniques (e.g. to strongly-convex functions, regret/error bounds holding with high-probability rather than just in expectation, and improved bounds if allowed $k > 2$ observations per round instead of just two).

Like previous algorithms, our algorithm is based on a random gradient estimator, which given a function $f$ and point $\mathbf{w}$, queries $f$ at two random locations close to $\mathbf{w}$, and computes a random vector whose expectation is a gradient of a smoothed version of $f$. The papers essentially use the estimator which queries at $\mathbf{w}$ and $\mathbf{w} + {\delta\mathbf{u}}$ (where $\mathbf{u}$ is a random unit vector and $\delta > 0$ is a small parameter), and returns

The intuition is readily seen in the one-dimensional ($d = 1$) case, where the expectation of this expression equals

which indeed approximates the derivative of $f$ (assuming $f$ is differentiable) at $w$, if $\delta$ is small enough.

In contrast, our algorithm uses a slightly different estimator (also used in ), which queries at ${\mathbf{w} - {\delta\mathbf{u}}},{\mathbf{w} + {\delta\mathbf{u}}}$, and returns

Again, the intuition is readily seen in the case $d = 1$, where the expectation of this expression also equals Eq..

When $\delta$ is sufficiently small and $f$ is differentiable at $\mathbf{w}$, both estimators compute a good approximation of the true gradient ${\nabla f}{(\mathbf{w})}$. However, when $f$ is not differentiable, the variance of the estimator in Eq. can be quadratic in the dimension $d$, as pointed out by: For example, for ${f{(\mathbf{w})}} = {\|\mathbf{w}\|}_{2}$ and $\mathbf{w} = 0$, the second moment equals

Since the performance of the algorithm crucially depends on the second moment of the gradient estimate, this leads to a highly sub-optimal guarantee. In, this was handled by adding an additional random perturbation and using a more involved analysis. Surprisingly, it turns out that the slightly different estimator in Eq. does not suffer from this problem, and its second moment is essentially linear in the dimension $d$.

## Algorithm and Main Results

We consider the algorithm described in Figure 1, which performs standard mirror descent using a randomized gradient estimator ${\overset{\sim}{\mathbf{g}}}_{t}$ of a (smoothed) version of $f_{t}$ at point $\mathbf{w}_{t}$. We make the assumption that one can indeed query $f_{t}$ at any point $\mathbf{w}_{t} + {\delta_{t}\mathbf{u}_{t}}$ as specified in the algorithm^22^2This may require us to query at a distance $\delta_{t}$ outside $\mathcal{W}$. If we must query within $\mathcal{W}$, then one can simply run the algorithm on a slightly smaller set ${({1 - \delta})}\mathcal{W}$, where $\delta \geq \delta_{t}$ for all $t$, ensuring that we always query at $\mathcal{W}$. Since the formal guarantee in Thm. 1 holds for arbitrarily small $\delta_{t}$, and each $f_{t}$ is Lipschitz, we can always take $\delta$ and $\delta_{t}$ small enough so that the additional regret/error incurred is negligible..

Input: Step size η, function r: 𝒲 ↦ ℝ, exploration parameters δt &gt; 0
Predict wt = arg maxw ∈ 𝒲⟨θt, w⟩ − r (w)
Sample ut uniformly from the Euclidean unit sphere {w: ∥w∥2 = 1}
Set ${\overset{\sim}{\mathbf{g}}}_{t} = {\frac{d}{2\delta_{t}}\left( {{f_{t}{({\mathbf{w}_{t} + {\delta_{t}\mathbf{u}_{t}}})}} - {f_{t}{({\mathbf{w}_{t} - {\delta_{t}\mathbf{u}_{t}}})}}} \right)\mathbf{u}_{t}}$
Update ${\mathbf{θ}}_{t + 1} = {{\mathbf{θ}}_{t} - {\eta\overset{\sim}{\mathbf{g}_{t}}}}$
Algorithm 1 Two-Point Bandit Convex Optimization Algorithm

The analysis of the algorithm is presented in the following theorem:

### Theorem 1

Assume the following conditions hold:

$r$ is $1$-strongly convex with respect to a norm $\parallel \cdot \parallel$, and ${\sup_{\mathbf{w} \in \mathcal{W}}{r{(\mathbf{w})}}} \leq R^{2}$ for some $R < \infty$.

$f_{t}$ is convex and $G_{2}$-Lipschitz with respect to the $2$-norm $\parallel \cdot \parallel_{2}$.

The dual norm $\parallel \cdot \parallel_{\ast}$ of $\parallel \cdot \parallel$ is such that $\sqrt{{\mathbb{E}}_{\mathbf{u}_{t}}{\|\mathbf{u}_{t}\|}_{\ast}^{4}} \leq p_{\ast}$ for some $p_{\ast} < \infty$.

If $\eta = \frac{R}{p_{\ast}G_{2}\sqrt{dT}}$, and $\delta_{t}$ chosen such that $\delta_{t} \leq {p_{\ast}R\sqrt{\frac{d}{T}}}$, then the sequence $\mathbf{w}_{1},\ldots,\mathbf{w}_{T}$ generated by the algorithm satisfies the following for any $T$ and $\mathbf{w}^{\ast} \in \mathcal{W}$:

where $c$ is some numerical constant.

We note that conditions 1 is standard in the analysis of the mirror-descent method (see the specific corollaries below), whereas conditions 2 and 3 are needed to ensure that the variance of our gradient estimator is controlled.

As mentioned earlier, the bound on the average regret which appears in Thm. 1 immediately implies a similar bound on the error in a stochastic optimization setting, for the average point ${\overline{\mathbf{w}}}_{T} = {\frac{1}{T}{\sum_{t = 1}^{T}\mathbf{w}_{t}}}$. We note that the result is robust to the choice of $\eta$, and is the same up to constants as long as $\eta = {\Theta{({{R/p_{\ast}}G_{2}\sqrt{dT}})}}$. Also, the constant $c$, while always bounded above zero, shrinks as $\delta_{t}\rightarrow 0$ (see the proof for details).

As a first application, let us consider the case where $\parallel \cdot \parallel$ is the Euclidean norm $\parallel \cdot \parallel_{2}$. In this case, we can take ${s{(\mathbf{w})}} = {\frac{1}{2}{\|\mathbf{w}\|}_{2}^{2}}$, and the algorithm reduces to a standard variant of online gradient descent, defined as ${\mathbf{θ}}_{t + 1} = {{\mathbf{θ}}_{t} - {\overset{\sim}{\mathbf{g}}}_{t}}$ and $\mathbf{w}_{t} = {\arg{\min_{\mathbf{w} \in \mathcal{W}}{\|{w - {\mathbf{θ}}_{t}}\|}_{2}}}$. In this case, we get the following corollary:

### Corollary 1

Suppose $f_{t}$ for all $t$ is $G_{2}$-Lipschitz with respect to the Euclidean norm, and $\mathcal{W} \subseteq {\{\mathbf{w}:{{\|\mathbf{w}\|}_{2} \leq R}\}}$. Then using $\parallel \cdot \parallel = \parallel \cdot \parallel_{2}$ and ${r{(\mathbf{w})}} = {\frac{1}{2}{\|\mathbf{w}\|}_{2}^{2}}$, it holds for some constant $c$ and any $\mathbf{w}^{\ast} \in \mathcal{W}$ that

The proof is immediately obtained from Thm. 1, noting that $p_{\ast} = 1$ in our case. This bound matches (up to constants) the lower bound in, hence closing the gap between upper and lower bounds in this setting.

As a second application, let us consider the case where $\parallel \cdot \parallel$ is the $1$-norm, $\parallel \cdot \parallel_{1}$, the domain $\mathcal{W}$ is the simplex in ${\mathbb{R}}^{d}$, $d > 1$ (although our result easily extends to any subset of the $1$-norm unit ball), and we use a standard entropic regularizer:

### Corollary 2

Suppose $f_{t}$ for all $t$ is $G_{1}$-Lipschitz with respect to the $L_{1}$ norm. Then using $\parallel \cdot \parallel = \parallel \cdot \parallel_{1}$ and ${r{(\mathbf{w})}} = {\sum_{i = 1}^{d}{w_{i}{\log{({dw_{i}})}}}}$, it holds for some constant $c$ and any $\mathbf{w}^{\ast} \in \mathcal{W}$ that

This bound matches (this time up to a logarithmic factor) the lower bound in for this setting.

### Proof

The function $r$ is $1$-strongly convex with respect to the $1$-norm (see for instance, Example 2.5), and has value at most $\log{(d)}$ on the simplex. Also, if $f_{t}$ is $G_{1}$-Lipschitz with respect to the $1$-norm, then it must be $\sqrt{d}G_{1}$-Lipschitz with respect to the Euclidean norm. Finally, to satisfy condition 3 in Thm. 1, we upper bound $\sqrt{{\mathbb{E}}{\lbrack{\|\mathbf{u}_{t}\|}_{\infty}^{4}\rbrack}}$ using the following lemma, whose proof is given in the appendix:

### Lemma 1

If $\mathbf{u}$ is uniformly distributed on the unit sphere in ${\mathbb{R}}^{d}$, $d > 1$, then $\sqrt{{\mathbb{E}}{\lbrack{\|\mathbf{u}\|}_{\infty}^{4}\rbrack}} \leq {c\sqrt{\frac{\log{(d)}}{d}}}$ where $c$ is a positive numerical constant independent of $d$.

Plugging these observations into Thm. 1 leads to the desired result. ∎

## Proof of Theorem 1

As discussed in the introduction, the key to getting improved results compared to previous papers is the use of a slightly different random gradient estimator, which turns out to have significantly less variance. The formal proof relies on a few simple lemmas listed below. The key lemma is Lemma 5, which establishes the improved variance behavior.

### Lemma 2

For any $\mathbf{w}^{\ast} \in \mathcal{W}$, it holds that

This lemma is the canonical result on the convergence of online mirror descent, and the proof is standard (see e.g. ).

### Lemma 3

Define the function

over $\mathcal{W}$, where $\mathbf{u}_{t}$ is a vector picked uniformly at random from the Euclidean unit sphere. Then the function is convex, Lipschitz with constant $G_{2}$, satisfies

and is differentiable with the following gradient:

### Proof

The fact that the function is convex and Lipschitz is immediate from its definition and the assumptions in the theorem. The inequality follows from $\mathbf{u}_{t}$ being a unit vector and that $f_{t}$ is assumed to be $G_{2}$-Lipschitz with respect to the $2$-norm. The differentiability property follows from Lemma 2.1 in. ∎

### Lemma 4

For any function $g$ which is $L$-Lipschitz with respect to the $2$-norm, it holds that if $\mathbf{u}$ is uniformly distributed on the Euclidean unit sphere, then

for some numerical constant $c$.

### Proof

A standard result on the concentration of Lipschitz functions on the Euclidean unit sphere implies that

for some numerical constant $c^{\prime} > 0$ (see the proof of Proposition 2.10 and Corollary 2.6 in ). Therefore,

which equals ${cL^{2}}/d$ for some numerical constant $c$. ∎

### Lemma 5

It holds that ${{\mathbb{E}}{\lbrack\left. {\overset{\sim}{\mathbf{g}}}_{t} \middle| \mathbf{w}_{t} \right.\rbrack}} = {{\nabla{\hat{f}}_{t}}{(\mathbf{w}_{t})}}$ (where ${\hat{f}}_{t}{( \cdot )}$ is as defined in Lemma 3), and ${{\mathbb{E}}{\lbrack\left. {\|{\overset{\sim}{\mathbf{g}}}_{t}\|}^{2} \middle| \mathbf{w}_{t} \right.\rbrack}} \leq {cdp_{\ast}^{2}G_{2}^{2}}$ for some numerical constant $c$.

### Proof

For simplicity of notation, we drop the $t$ subscript. Since $\mathbf{u}$ has a symmetric distribution around the origin,

which equals ${\nabla\hat{f}}{(\mathbf{w})}$ by Lemma 3.

As to the second part of the lemma, we have the following, where $\alpha$ is an arbitrary parameter and where we use the elementary inequality ${({a - b})}^{2} \leq {2{({a^{2} + b^{2}})}}$.

Again using the symmetrical distribution of $\mathbf{u}$, this equals

Applying Cauchy-Schwartz and using the condition $\sqrt{{\mathbb{E}}_{\mathbf{u}}{\|\mathbf{u}\|}_{\ast}^{4}} \leq p_{\ast}$ stated in the theorem, we get the upper bound

In particular, taking $\alpha = {{\mathbb{E}}_{\mathbf{u}}{\lbrack{f{({\mathbf{w} + {\delta\mathbf{u}}})}}\rbrack}}$ and using Lemma 4 (noting that $f{({\mathbf{w} + {\delta\mathbf{u}}})}$ is $G_{2}\delta$-Lipschitz w.r.t. $\mathbf{u}$ in terms of the $2$-norm), this is at most ${\frac{p_{\ast}^{2}d^{2}}{\delta^{2}}c\frac{{({G_{2}\delta})}^{2}}{d}} = {cdp_{\ast}^{2}G_{2}^{2}}$ as required. ∎

We are now ready to prove the theorem. Taking expectations on both sides of the inequality in Lemma 2, we have

Using Lemma 5, the right hand side is at most

The left hand side of Eq., by Lemma 5 and convexity of ${\hat{f}}_{t}$, equals

By Lemma 3, this is at least

Combining these inequalities and plugging back into Eq., we get

Choosing $\eta = {R/{({p_{\ast}G_{2}\sqrt{dT}})}}$, and any $\delta_{t} \leq {p_{\ast}R\sqrt{d/T}}$, we get

Dividing both sides by $T$, the result follows.
