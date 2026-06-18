## Introduction

Nowadays, stochastic gradient descent (SGD), as well as its variants (Adam, Momentum, Adagrad, etc.) have become the de facto algorithms for training neural networks. SGD runs iterative updates for the weights $x_{t}$: $x_{t + 1} = {x_{t} - {\etav_{t}}}$, where $\eta$ is the step size^11^1In this paper, we use step size and learning rate interchangeably.. $v_{t}$ is the stochastic gradient that satisfies ${E{\lbrack v_{t}\rbrack}} = {{\nabla f}{(x_{t})}}$, and is usually computed using a mini-batch of the dataset.

In the regime of convex optimization, SGD is proved to be a nice tradeoff between accuracy and efficiency: it requires more iterations to converge, but fewer gradient evaluations per iteration. Therefore, for the standard empirical risk minimizing problems with $n$ points and smoothness $L$, to get to $\epsilon$-close to $x^{\ast}$, GD needs $O{({{Ln}/\epsilon})}$ gradient evaluations, but SGD with reduced variance only needs $O{({{n{\log\frac{1}{\epsilon}}} + \frac{L}{\epsilon}})}$ gradient evaluations. In these scenarios, noise is a by-product of cheap gradient computation, and does not help training.

By contrast, for non-convex optimization problems like training neural networks, noise seems crucial. It is observed that with the help of noisy gradients, SGD does not only converge faster, but also converge to a better solution compared with GD. To formally understand this phenomenon, people have analyzed the role of noise in various settings. For example, it is proved that noise helps to escape saddle points, gives better generalization, and also guarantees polynomial hitting time of good local minima under some assumptions.

However, it is still unclear why SGD could converge to better local minima than GD. Empirically, in additional to the gradient noise, the step size is observed to be a key factor in optimization. More specifically, small step size helps refine the network and converge to a local minimum, while large step size helps escape the current local minimum and go towards a better one. Thus, standard training schedule for modern networks uses large step size first, and shrinks it later. While using large step sizes to escape local minima matches with intuition, the existing analysis on SGD for non-convex objectives always considers the small-step-size settings.

Figure 1: SGD path xt → xt + 1 can be decomposed into xt → yt → xt + 1. If the local minimum basin has small diameter, the gradient at xt + 1 will point away from the basin.

Figure 2: 3D version of Figure 2: SGD could escape a local minimum within one step.

See Figure 2 for an illustration. Consider the scenario that for some $x_{t}$, instead of pointing to the solution $x^{\ast}$ (not shown), its negative gradient points to a bad local minimum $x_{\circ}$, so following the full gradient we will arrive $y_{t} \triangleq {x_{t} - {\eta{\nabla f}{(x_{t})}}}$. Fortunately, since we are running SGD, the actual direction we take is ${- {\etav_{t}}} = {- {\eta{({{{\nabla f}{(x_{t})}} + \omega_{t}})}}}$, where $\omega_{t}$ is the noise with ${{{\mathbb{E}}{\lbrack\omega_{t}\rbrack}} = 0},{\omega_{t} \sim {W{(x_{t})}}}$^22^2$W{(x_{t})}$ is data dependent.. As we show in Figure 2, if we take a large $\eta$, we may get out of the basin region with the help of noise, i.e., from $y_{t}$ to $x_{t + 1}$. Here, getting out of the basin means the negative gradient at $x_{t + 1}$ no longer points to $x_{\circ}$ (See also Figure 2).

To formalize this intuition, instead of analyzing the sequence $x_{t}\rightarrow x_{t + 1}$, let us look at the sequence $y_{t}\rightarrow y_{t + 1}$, where $y_{t}$ is defined to be $x_{t} - {\eta{\nabla f}{(x_{t})}}$, as in the preceding paragraph. The SGD algorithm never computes these vectors $y_{t}$, but we are only using them as an analysis tool. From the equation $x_{t + 1} = {y_{t} - {\eta\omega_{t}}}$ we obtain the following update rule relating $y_{t + 1}$ to $y_{t}$.

The random vector $\eta\omega_{t}$ in has expectation $0$, so if we take the expectation of both sides of, we get ${{\mathbb{E}}_{\omega_{t}}{\lbrack y_{t + 1}\rbrack}} = {y_{t} - {\eta{\nabla{\mathbb{E}}_{\omega_{t}}}{\lbrack{f{({y_{t} - {\eta\omega_{t}}})}}\rbrack}}}$. Therefore, if we define $g_{t}$ to be the function ${g_{t}{(y)}} = {{\mathbb{E}}_{\omega_{t}}{\lbrack{f{({y - {\eta\omega_{t}}})}}\rbrack}}$, which is simply the original function $f$ convolved with the $\eta$-scaled gradient noise, then the sequence $y_{t}$ is approximately doing gradient descent on the sequence of functions $(g_{t})$.

This alternative view helps to explain why SGD converges to a good local minimum, even when $f$ has many other sharp local minima. Intuitively, sharp local minima are eliminated by the convolution operator that transforms $f$ to $g_{t}$, since convolution has the effect of smoothing out short-range fluctuations. This reasoning ensures that SGD converges to a good local minimum under much weaker conditions, because instead of imposing convexity or one-point convexity requirements on $f$ itself, we only require those properties to hold for the smoothed functions obtained from $f$ by convolution. We can formalize the foregoing argument using the following assumption.

### Assumption 1 (Main Assumption)

For a fixed point $x^{\ast}$^33^3Notice that $x^{\ast}$ is not necessarily the global optimal in the original function $f$ due to the convolution operator., noise distribution $W{(x)}$, step size $\eta$, the function $f$ is $c$-one point strongly convex with respect to $x^{\ast}$ after convolved with noise. That is, for any $x,y$ in domain $\mathbb{D}$ s.t. $y = {x - {\eta{\nabla f}{(x)}}}$,

For point $y$, since the direction $x^{\ast} - y$ points to $x^{\ast}$, by having positive inner product with $x^{\ast} - y$, we know the direction $- {\eta{\nabla f}{({y_{t} - {\eta\omega_{t}}})}}$ in approximately points to $x^{\ast}$ in expectation (See more discussion on one point convexity in Appendix). Therefore, $y_{t}$ will converge to $x^{\ast}$ with decent probability:

### Theorem 1 (Main Theorem, Informal)

Assume $f$ is smooth, for every $x \in {\mathbb{D}}$, $W{(x)}$ s.t., ${\max_{\omega \sim {W{(x)}}}{\|\omega\|}_{2}} \leq r$. Also assume $\eta$ is bounded by a constant, and Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") holds with $x^{\ast},\eta$, and $c$. For $T_{1} \geq {\overset{\sim}{O}{(\frac{1}{\etac})}}$^44^4We use $\overset{\sim}{O}$ to hide $\log$ terms here., and any $T_{2} > 0$, with probability at least $1/2$, we have ${\|{y_{t} - x^{\ast}}\|}_{2}^{2} \leq {O{({{\log{(T_{2})}}\frac{\etar^{2}}{c}})}}$ for any $t$ s.t., ${T_{1} + T_{2}} \geq t \geq T_{1}$.

Notice that our main theorem not only says SGD will get close to $x^{\ast}$, but also says with constant probability, SGD will stay close to $x^{\ast}$ for the future $T_{2}$ steps. As we will see in Section 5, we observe that Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") holds along the SGD trajectory for the modern neural networks when the noise comes from real data mini-batches. Moreover, the SGD trajectory matches with our theory prediction in practice.

Our main theorem can also help explain why SGD could escape "sharp" local minima and converge to "flat" local minima in practice. Indeed, the sharp local minima have small loss value and small diameter, so after convolved with the noise kernel, they easily disappear, which means Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") holds. However, flat local minima have large diameter, so they still exists after convolution. In that case, our main theorem says, it is more likely that SGD will converge to flat local minima, instead of sharp local minima.

Figure 3: Running SGD on a spiky function f. Row 1: f gets smoother after convolving with uniform random noise. Row 2: Run SGD with different noise levels. Every figure is obtained with 100 trials with different random initializations. Red dots represent the last iterates of these trials, while blue bars represent the cumulative counts. GD without noise easily gets stuck at various local minima, while SGD with appropriate noise level converges to a local region. Row 3: In order to get closer to x*, one may run SGD in multiple stages with shrinking learning rates.

### Related Work

Previously, people already realized that the noise in the gradient could help SGD to escape saddle points or achieve better generalization. With the help of noise, SGD can also be viewed as doing approximate Bayesian inference or variational inference. Besides, it is proved that SGD with extra noise could "hit" a local minimum with small loss value in polynomial time under some assumptions. However, the extra noise is too big to guarantee convergence, and that model cannot deal with escaping sharp local minima.

Escaping sharp local minima for neural network is important, because it is conjectured (although controversial ) that flat local minima may lead to better generalization. It is also observed that the correct learning rate schedule (small or large) is crucial for escaping bad local minima. Furthermore, solutions that are farther away from the initialization may lead to wider local minima and better generalization. Under a Bayesian perspective, it is shown that the noise in stochastic gradient could drive SGD away from sharp minima, which decides the optimal batch size. There are also explanations for why small batch methods prefers flat minima while large batch methods are not, by investigating the canonical quadratic sums problem.

To visualize the loss surface of neural network, a common practice is projecting it onto a one dimensional line, which was observed to be convex. For the simple two layer neural network, a local one point strongly convexity property provably holds under Gaussian input assumption.

## Motivating Example

Let us first see a simple example in Figure 3. We use $F_{r,c}$ to denote the sub-figure at row $r$ and column $c$. The function $f$ at $F_{1,1}$ is a approximately convex function, but very spiky. Therefore, GD easily gets stuck at various local minima, see $F_{2,1}$. However, we want to get rid of those spurious local minima, and get a point near $x^{\ast} = 0$.

If we take the alternative view that SGD works on the convolved version of $f$ ($F_{1,2}$, $F_{1,3}$, $F_{1,4}$), we find that those functions are much smoother and contain few local minima. However, the gradient noise here is a double-edged sword. On one hand, if the noise is small, the convolved $f$ is still somewhat non-convex, then SGD may find a few bad local minima as shown in $F_{2,2}$. On the other hand, if the noise is too large, the noise dominates the gradient, and SGD will act like random walk, see $F_{2,4}$.

$F_{2,3}$ seems like a nice tradeoff, as all trials converges to a local region near $0$, but the region is too big (most points are in $\lbrack{- 1.5},1.5\rbrack$). In order to get closer to $0$, we may "restart" SGD with a point in $\lbrack{- 1.5},1.5\rbrack$, using smaller noise level $0.15$. Recall in $F_{2,2}$, SGD fails because the convolved $f$ has a few non-convex regions ($F_{1,2}$), so SGD may find spurious local minima. However, those local minima are outside $\lbrack{- 1.5},1.5\rbrack$. The convolved $f$ in $F_{1,2}$ restricted in $\lbrack{- 1.5},1.5\rbrack$ is pretty convex, so if we start a point in this region, SGD converges to a smaller local region centered at $0$, see $F_{3,2}$.

We may do this iteratively, with even smaller noise levels and smaller initialization regions, and finally we will get pretty close to $0$ with decent probability, see $F_{3,3}$ and $F_{3,4}$.

## Main Theorem

### Definition 1 (Smoothness)

Function $f \in {\mathbb{R}}^{d}\rightarrow{\mathbb{R}}$ is $L$-smooth, if for any ${x,y} \in {\mathbb{R}}^{d}$,

Assume that we are running SGD on the sequence $\{ x_{t}\}$. Recall the update rule for $y_{t}$. Our main theorem says that $\{ y_{t}\}$ is converging to $x^{\ast}$ and will stay around $x^{\ast}$ afterwards.

### Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") (Main Theorem)

Assume $f$ is $L$-smooth, for every $x \in {\mathbb{D}}$, $W{(x)}$ s.t., ${\max_{\omega \sim {W{(x)}}}{\|\omega\|}_{2}} \leq r$. For a fixed target solution $x^{\ast}$, if there exists constant ${c,\eta} > 0$, such that Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") holds with $x^{\ast},\eta,c$, and $\eta < {\min{\{\frac{1}{2L},\frac{c}{L^{2}},\frac{1}{2c}\}}}$, $\lambda \triangleq {{2\etac} - {\eta^{2}L^{2}}}$, $b \triangleq {\eta^{2}r^{2}{({1 + {\etaL}})}^{2}}$. Then for any fixed $T_{1} \geq \frac{\log{({{\lambda{\|{y_{0} - x^{\ast}}\|}_{2}^{2}}/b})}}{\lambda}$ and $T_{2} > 0$, with probability at least $1/2$, we have ${\|{y_{T} - x^{\ast}}\|}_{2}^{2} \leq \frac{20b}{\lambda}$ and ${\|{y_{t} - x^{\ast}}\|}_{2}^{2} \leq {O\left( \frac{{\log{(T_{2})}}b}{\lambda} \right)}$ for all $t$ s.t., ${T_{1} + T_{2}} \geq t \geq T_{1}$.

We defer the proof to Section 4.

Remark. For fixed $c$, there exists a lower bound on $\eta$ to satisfy Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?"), so $\eta$ cannot be arbitrarily small. However, the main theorem says within $T_{1} + T_{2}$ steps, SGD will stay in a local region centered at $x^{\ast}$ with diameter $O\left( \frac{{\log{(T_{2})}}b}{\lambda} \right)$, which is essentially $\overset{\sim}{O}{({{\etar^{2}}/c})}$ that scales with $\eta$. In order to get closer to $x^{\ast}$, a common trick in practice is to restart SGD with smaller step size $\eta^{\prime}$ within the local region. If $f$ inside this region has better geometric properties (which is usually true), one gets better convergence guarantee:

### Corollary 2 (Shrinking Learning Rate)

If the assumptions in Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") holds, and $f$ restricted in the local region ${\mathbb{D}}^{\prime} \triangleq \left. \{ x \middle| {{\|{x - x^{\ast}}\|} \leq \frac{20b}{\lambda}}\} \right.$ satisfy the same assumption with ${c^{\prime} > c},{\eta^{\prime} < \eta}$, then if we run SGD with $\eta$ for the first $T_{1} \geq \frac{\log{(\frac{\lambdad}{b})}}{\lambda}$ steps, and with $\eta^{\prime}$ for the next $T_{2} \geq \frac{\log{(\frac{\lambda\frac{20b^{\prime}}{\lambda}}{b^{\prime}})}}{\lambda^{\prime}}$ steps, with probability at least $1/4$, we have ${\|{y_{T_{1} + T_{2}} - x^{\ast}}\|}_{2}^{2} \leq \frac{20b^{\prime}}{\lambda^{\prime}} < \frac{20b}{\lambda}$.

This corollary can be easily generalized to shrink the learning rate multiple times.

Our main theorem is based on the important assumption that the step size is bounded. If the step size is too big, even if the whole function $f$ is one point convex (a stronger assumption than Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?")), and we run full gradient descent, we may not keep getting closer to $x^{\ast}$, as we show below.

### Theorem 3

For function $f$, if ${{\forall x},{\langle{- {{\nabla f}{(x)}}},{x^{\ast} - x}\rangle}} \leq {c^{\prime}{\|{x^{\ast} - x}\|}_{2}^{2}}$, and we are at the point $x_{t}$. If we run full gradient descent with step size $\eta > \frac{2c^{\prime}{\|{x_{t} - x^{\ast}}\|}_{2}^{2}}{{\|{{\nabla f}{(x_{t})}}\|}_{2}^{2}}$, we have ${\|{x_{t + 1} - x^{\ast}}\|}_{2}^{2} \geq {\|{x_{t} - x^{\ast}}\|}_{2}^{2}$.

### Proof

The proof is straightforward and we defer it to Appendix C. ∎

Figure 4: When step size is too big, even the gradient is one point convex, we may still go farther away from x*.

This theorem can be best illustrated with Figure 4. If $\eta$ is too big, although the gradient (the arrow) is pointing to the approximately correct direction, $x_{t + 1}$ will be farther away from $x^{\ast}$ (going outside of the $x^{\ast}$-centered ball).

Although this theorem analyzes the simple full gradient case, SGD is similar. In the high dimensional case, it is natural to assume that most of the noise will be orthogonal to the direction of $x_{t} - x^{\ast}$, therefore with additional noise inside the stochastic gradient, a large step size will drive $x_{t + 1}$ away from $x^{\ast}$ more easily.

Therefore, our paper provides a theoretical explanation for why picking step size is so important (too big or too small will not work). We hope it could lead to more practical guidelines in the future.

## Proof for Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?")

In the proof, we will use the following lemma.

### Theorem 4 (Azuma)

Let $X_{1},X_{2},\cdots,X_{n}$ be independent random variables satisfying ${{|{X_{i} - {E{(X_{i})}}}|} \leq c_{i}},{{{for}1} \leq i \leq n}$. We have the following bound for the sum $X = {\sum_{i = 1}^{n}X_{i}}$:

Our proof has four steps.

Step 1. Since Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") holds, we show that SGD always makes progress towards $x^{\ast}$ in expectation, plus some noise.

Let filtration $\mathcal{F}_{t} = {\sigma{\{\omega_{0},\cdots,\omega_{t - 1}\}}}$, where $\sigma{\{ \cdot \}}$ denotes the sigma field. Notice that for any $\omega_{t} \sim {W{(x_{t})}}$, we have ${{\mathbb{E}}{\lbrack\left. \omega_{t} \middle| \mathcal{F}_{t} \right.\rbrack}} = 0$.

Step 2. Since SGD makes progress in every step, after many steps, SGD gets very close to $x^{\ast}$ in expectation. By Markov inequality, this event holds with large probability.

Notice that since $\eta < \frac{c}{L^{2}}$, we have $\lambda = {{2\etac} - {\eta^{2}L^{2}}} > {\etac} > 0$. Recall $b \triangleq {\eta^{2}r^{2}{({1 + {\etaL}})}^{2}}$, we get:

That means, $G_{t}$ is a supermartingale. We have

Since $T_{1} \geq \frac{\log\left( \frac{\lambda{\|{y_{0} - x^{\ast}}\|}_{2}^{2}}{b} \right)}{\lambda}$, we get:

By Markov inequality, we know with probability at least $0.9$,

For notational simplicity, for the analysis below we relabel the point $y_{T_{1}}$ as $y_{0}$. Therefore, at time $0$ we already have ${\|{y_{0} - x^{\ast}}\|}_{2}^{2} \leq \frac{20b}{\lambda}$.

Step 3. Conditioned on the event that we are close to $x^{\ast}$, below we show that if for $t_{0} > t \geq 0$, $y_{t}$ is close to $x^{\ast}$, then $y_{t_{0}}$ is also close to $x^{\ast}$ with high probability.

Let $\zeta = \frac{9T_{2}}{4}$. Let event ${\mathfrak{E}}_{t} = {\{{{{\forall\tau} \leq t},{{\|{y_{\tau} - x^{\ast}}\|} \leq {\mu\sqrt{\frac{b}{\lambda}}} = \delta}}\}}$, where $\mu$ is a parameter satisfies $\mu \geq {\max{\{ 8,{42{\log^{\frac{1}{2}}{(\zeta)}}}\}}}$. If with probability $\frac{5}{9}$, ${\mathfrak{E}}_{t}$ holds for every $t \leq T_{2}$, we are done.

By the previous calculation, we know that ($\mathbb{1}_{{\mathfrak{E}}_{t}}$ is the indicator function for ${\mathfrak{E}}_{t}$)

So $G_{t}\mathbb{1}_{{\mathfrak{E}}_{t - 1}}$ is a supermartingale, with the initial value $G_{0}$. In order to apply Azuma inequality, we first bound the following term (notice that we use ${{\mathbb{E}}{\lbrack\omega_{t}\rbrack}} = 0$ multiple times):

Where the last inequality uses the fact that ${\etaL} \leq \frac{1}{2}$ and ${\|{y_{t} - x^{\ast}}\|}_{2} \leq \delta$ (as $\mathbb{1}_{{\mathfrak{E}}_{t}}$ holds). Let $M \triangleq {{3.5\eta^{2}r^{2}} + {7\etar\delta}}$. Let $d_{\tau} = |G_{\tau}\mathbb{1}_{{\mathfrak{E}}_{\tau - 1}} - {\mathbb{E}}{\lbrack G_{\tau}\mathbb{1}_{{\mathfrak{E}}_{\tau - 1}}|\mathcal{F}_{t}\rbrack}|$, we have

Apply Azuma inequality (Theorem 4. ‣ 4 Proof for Theorem 4 ‣ An Alternative View: When Does SGD Escape Local Minima?")), for any $\zeta > 0$, we know

Therefore, with probability $1 - \frac{1}{\zeta}$,

Step 4. The inequality above says, if ${\mathfrak{E}}_{t - 1}$ holds, i.e., for all ${\tau \leq {t - 1}},{{\|{y_{\tau} - x^{\ast}}\|} \leq \delta}$, then with probability $1 - \frac{1}{\zeta}$, $G_{t}$ is bounded. If we can show from the upper bound of $G_{t}$ that ${\|{y_{t} - x^{\ast}}\|} \leq \delta$ is also true, we automatically get ${\mathfrak{E}}_{t}$ holds. In other words, that means if ${\mathfrak{E}}_{t - 1}$ holds, then ${\mathfrak{E}}_{t}$ holds with probability $1 - \frac{1}{\zeta}$. Therefore, by applying this claim $T_{2}$ times, we get ${\mathfrak{E}}_{T_{2}}$ holds with probability ${1 - \frac{T_{2}}{\zeta}} = \frac{5}{9}$. Combining with inequality, we know with probability at least $1/2$, the theorem statement holds. Thus, it remains to show that ${\|{y_{t} - x^{\ast}}\|} \leq \delta$.

If ${G_{t}\mathbb{1}_{{\mathfrak{E}}_{t - 1}}} \leq {G_{0} + {\sqrt{2}r_{t}{\log^{\frac{1}{2}}{(\zeta)}}}}$, we know

The second last inequality holds because we know $\frac{1}{1 - {({1 - \lambda})}^{2}} = \frac{1}{{2\lambda} - \lambda^{2}} \leq \frac{1}{\lambda} \leq \frac{1}{\etac}$, since $\lambda = {{2\etac} - {\eta^{2}L^{2}}} \leq {2\etac} < 1$, and $\lambda > {\etac}$.

It remains to prove the following lemma, which we defer to Appendix B.

### Lemma 5

Therefore, ${\|{y_{t} - x^{\ast}}\|} \leq \delta$. Combining the 4 steps together, we have proved the theorem.

## Empirical Observations

(a) SGD trajectory is locally one point convex.

(b) The neighborhood of SGD trajectory is one point convex.

(c) The norm of stochastic gradient

Figure 5: (a). The inner product between the negative gradient and x300 − xt for each epoch t ≥ 5 is always positive. Every data point is the minimum value among 5 trials. (b). Neighborhood of SGD trajectory is also one point convex with respect to x300. (c). Norm of stochastic gradient

In this section, we explore the loss surfaces of modern neural networks, and show that they enjoy many nice one point convex properties. Therefore, our main theorem could be used for explaining why SGD works so well in practice.

### The SGD trajectory is one point convex

It is well known that the loss surface of neural network is highly non-convex, with numerous local minima. However, we observe that the loss surface is consisted of many one point convex basin region, while each time SGD traverses one of such regions.

See Figure 5(a) for details. We ran experiments on Resnet ($34$ layers, $\approx 1.2$M parameters), Densenet ($100$ layers, $\approx 0.8$M parameters) on cifar10 and cifar100, each for 5 trials with $300$ epochs and different initializations. For the start of every epoch $x_{t}$ in each trial, we compute the inner product between the negative gradient $- {{\nabla f}{(x_{t})}}$ and the direction $x_{300} - x_{t}$. In Figure 5(a), we plot the minimum value for every epoch among $5$ trials for each setting. Notice that except for the starting period of densenet on Cifar-10, all the other networks in all trials have positive inner products, which shows that the trajectory of SGD (except the starting period) is one point convex with respect to the final solution^55^5Similar observations were implicitly observed previously.. In these experiments, we have used the standard step size schedule ($0.1$ initially, $0.01$ after epoch $150$, and $0.001$ after epoch $225$). However, we got the same observation when using smoothly decreasing step sizes (shrink by $0.99$ per epoch).

### The neighborhood of the trajectory is one point convex

Having a one point convex trajectory for $5$ trials does not suffice to show SGD always has a simple and easy trajectory, due to the randomness of the stochastic gradient. Indeed, by a slight random perturbation, SGD might be in a completely different trajectory that is far from being one point convex to the final solution. However, in this subsection, we show that it is not the case, as the SGD trajectory is one point convex after convolving with uniform ball with radius $0.5$. That means, the whole neighborhood of the SGD trajectory is one point convex with respect to the final solution.

In this experiment, we tried Resnet ($34$ layers, $\approx 1.2$M parameters), Densenet ($100$ layers, $\approx 0.8$M parameters) on cifar10 and cifar100^66^6We also tried VGG with $\approx 1$M parameters, but does not have similar observations. This might be why Resnet and Densenet are slightly easier to optimize.. For every epoch in each setting, we take one point and look at its neighborhood with radius $0.5$ (upper bound of the length of one SGD step, as we will show below). We take $100$ random points inside each neighborhood to verify Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?")^77^7We also tried to sample points that are one SGD step away to represent the neighborhood, and got similar observations.. More specifically, for every random point $w$ in the neighborhood of $x_{t}$, we computer $\langle{- {{\nabla f}{(w)}}},{x_{300} - x_{t}}\rangle$. Figure 5(b) shows the mean value (solid line), as well as upper and lower bound of the inner product (shaded area). As we can see, the inner products for all epochs in every setting have small variances, and are always positive. Although we could not verify Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") by computing the exact expectation due to limited computational resources, from Figure 5(b) and Hoeffding bound (Lemma 6. ‣ 5.2 The neighborhood of the trajectory is one point convex ‣ 5 Empirical Observations ‣ An Alternative View: When Does SGD Escape Local Minima?")), we conclude that Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") should hold with high probability.

### Lemma 6 (Hoeffding bound \[12\])

Let $X_{1},\ldots,X_{n}$ be i.i.d. random variables bounded by the interval $\lbrack a,b\rbrack$. Then ${\Pr\left( {{{\frac{1}{n}{\sum_{i}X_{i}}} - {{\mathbb{E}}{\lbrack X_{1}\rbrack}}} \geq t} \right)} \leq {\exp\left( {- \frac{2nt^{2}}{{({b - a})}^{2}}} \right)}$.

Figure 5(c) shows the norm of the stochastic gradients, including both the mean value (solid lines), as well as upper and lower bounds (shaped area). For all settings, the stochastic gradients are always less than $5$ before epoch $150$ with learning rate $0.1$, and less than $15$ afterwards with learning rate $0.01$. Therefore, multiplying step size with gradient norm, we know SGD step length is always bounded by $0.5$.

Notice that the gradient norm gets bigger when we get closer to the final solution (after epoch $150$). This further explains why shrinking step size is important.

(a) Loss value of different local minima on

(b) Loss value of different local minima on Cifar100

(c) Distance from the local minima to the initialization

Figure 6: Spectrum of local minima on the loss surface on modern neural networks.

### Loss surface is locally a "slope"

Even with the observation that the whole neighborhood along the SGD trajectory is one point convex with respect to the final solution, there exists a chicken-and-egg concern, as the final target is generated using the SGD trajectory.

In this subsection, we show that the one point convexity is a pretty "global" property. We were running Resnet and Densenet on, but with smaller networks (each with about $10K$ parameters). For each network, if we fix the first $10$ epochs, and generate $50$ SGD trajectories with different random seeds for $140$ epochs and $0.1$ learning rate, we get $50$ different final solutions (they are pretty far away from each other, with minimum pairwise distance $40$). For each network, if we look at the inner product between the negative gradient of any epoch of any trajectories, and the vector pointing to any final solutions, we find that the inner products are almost always positive. (only $0.1\%$ of the inner products are not positive for Densenet, and only $2$ out of $343,000$ inner products are not positive for Resnet).

This indicates that the loss surface is "skewed" to the similar direction, and our observation that the whole SGD trajectory is one point convex w.r. to the last point is not a coincidence. Based on our Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?"), such loss surface is very friendly to SGD optimization, even with a few exceptional points that are not one point convex with respect to the final solution.

Notice that in general, it is not possible that all the negative gradients of all points are one point convex with respect to multiple target points. For example, if we take $1D$ interpolation between any two target points, we could easily find points that have negative gradients only pointing to one target point. However, based on our simulation, empirically SGD almost never traverse those regions.

### Spectrum of the local minima

From the previous subsections, we know that the loss surface of neural network has great one point convex properties. It seems that by our Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?"), SGD will almost always converge to a few target points (or regions). However, empirically SGD converges to very different target points. In this subsection, we argue that this is because of the learning rate is too big for SGD to converge (Theorem 3). On the other hand, whenever we shrink the learning rate to $0.01$, Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") immediately applies and SGD converges to a local minimum.

In this experiment, we were running smaller version of Resnet and Densenet (each with about $10K$ parameters) on and Cifar100. For each setting, we first train the network with step size $0.1$ for $300$ epochs, then we pick different epochs as the new starting points for finding nearby local minima using smaller learning rates with additional $150$ epochs.

See Figure 6(a) and Figure 6(b). Starting from different epochs, we got local minima with decreasing validation loss and training loss.

To show that these local minima are not from the same region, we also plot the distance of the local minima to the (unique) initialized point. As we can see, as we pick later epochs as the starting points, we get local minima that are farther away from the initialization with better quality (also observed in ).

Furthermore, we observe that for every local minimum, the whole trajectory is always one point convex to that local minimum. Therefore, the time for shrinking learning rate decides the quality of the final local minimum. That is, using large step size initially avoids being trapped into a bad local minimum, and whenever we are distant enough from the initialization, we can shrink the step size and converge to a good local minimum (due to one point convexity by Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?")).

## Conclusion

In this paper, we take an alternative view of SGD that it is working on the convolved version of the loss function. Under this view, we could show that when the convolved function is one point convex with respect to the final solution $x^{\ast}$, SGD could escape all the other local minima and stay around $x^{\ast}$ with constant probability.

To show our assumption is reasonable, we look at the loss surface of modern neural networks, and find that SGD trajectory has nice local one point convex properties, therefore the loss surface is very friend to SGD optimization. It remains an interesting open question to prove local one point convex property for deep neural networks.
