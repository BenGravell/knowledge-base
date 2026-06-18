<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Alternative View: When Does SGD Escape Local Minima?

Topics include Stochastic gradient descent, Local minima, Non-convex optimization, Neural networks, Optimization theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides a theoretical explanation for why SGD escapes sharp local minima, reframing SGD as optimizing a smoothed (convolved) version of the loss. The one-point convexity condition identified is broad enough to encompass neural network loss surfaces, bridging the gap between theory and practical SGD success.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic gradient descent (SGD) is widely used in machine learning. Although being commonly viewed as a fast but not accurate version of gradient descent (GD), it always finds better solutions than GD for modern neural networks. In order to understand this phenomenon, we take an alternative view that SGD is working on the convolved (thus smoothed) version of the loss function. We show that, even if the function f has many bad local minima or saddle points, as long as for every point x, the weighted average of the gradients of its neighborhoods is one point convex with respect to the desired solution x*, SGD will get close to, and then stay around x* with constant probability. More specifically, SGD will not get stuck at "sharp" local minima with small diameters, as long as the neighborhoods of these regions contain enough gradient information. The neighborhood size is controlled by step size and gradient noise. Our result identifies a set of functions that SGD provably works, which is much larger than the set of convex functions.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Empirically, we observe that the loss surface of neural networks enjoys nice one point convexity properties locally, therefore our theorem helps explain why SGD works so well for neural networks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nowadays, stochastic gradient descent (SGD), as well as its variants (Adam, Momentum, Adagrad, etc.) have become the de facto algorithms for training neural networks. SGD runs iterative updates for the weights $x_{t}$: $x_{t + 1} = {x_{t} - {\etav_{t}}}$, where $\eta$ is the step size^11^1In this paper, we use step size and learning rate interchangeably.. $v_{t}$ is the stochastic gradient that satisfies ${E{\lbrack v_{t}\rbrack}} = {{\nabla f}{(x_{t})}}$, and is usually computed using a mini-batch of the dataset.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the regime of convex optimization, SGD is proved to be a nice tradeoff between accuracy and efficiency: it requires more iterations to converge, but fewer gradient evaluations per iteration. Therefore, for the standard empirical risk minimizing problems with $n$ points and smoothness $L$, to get to $\epsilon$-close to $x^{\ast}$, GD needs $O{({{Ln}/\epsilon})}$ gradient evaluations, but SGD with reduced variance only needs $O{({{n{\log\frac{1}{\epsilon}}} + \frac{L}{\epsilon}})}$ gradient evaluations. In these scenarios, noise is a by-product of cheap gradient computation, and does not help training.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By contrast, for non-convex optimization problems like training neural networks, noise seems crucial. It is observed that with the help of noisy gradients, SGD does not only converge faster, but also converge to a better solution compared with GD. To formally understand this phenomenon, people have analyzed the role of noise in various settings. For example, it is proved that noise helps to escape saddle points, gives better generalization, and also guarantees polynomial hitting time of good local minima under some assumptions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, it is still unclear why SGD could converge to better local minima than GD. Empirically, in additional to the gradient noise, the step size is observed to be a key factor in optimization. More specifically, small step size helps refine the network and converge to a local minimum, while large step size helps escape the current local minimum and go towards a better one. Thus, standard training schedule for modern networks uses large step size first, and shrinks it later. While using large step sizes to escape local minima matches with intuition, the existing analysis on SGD for non-convex objectives always considers the small-step-size settings.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

See Figure 2 for an illustration. Consider the scenario that for some $x_{t}$, instead of pointing to the solution $x^{\ast}$ (not shown), its negative gradient points to a bad local minimum $x_{\circ}$, so following the full gradient we will arrive $y_{t} \triangleq {x_{t} - {\eta{\nabla f}{(x_{t})}}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fortunately, since we are running SGD, the actual direction we take is ${- {\etav_{t}}} = {- {\eta{({{{\nabla f}{(x_{t})}} + \omega_{t}})}}}$, where $\omega_{t}$ is the noise with ${{{\mathbb{E}}{\lbrack\omega_{t}\rbrack}} = 0},{\omega_{t} \sim {W{(x_{t})}}}$^22^2$W{(x_{t})}$ is data dependent.. As we show in Figure 2, if we take a large $\eta$, we may get out of the basin region with the help of noise, i.e., from $y_{t}$ to $x_{t + 1}$. Here, getting out of the basin means the negative gradient at $x_{t + 1}$ no longer points to $x_{\circ}$ (See also Figure 2).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To formalize this intuition, instead of analyzing the sequence $x_{t}\rightarrow x_{t + 1}$, let us look at the sequence $y_{t}\rightarrow y_{t + 1}$, where $y_{t}$ is defined to be $x_{t} - {\eta{\nabla f}{(x_{t})}}$, as in the preceding paragraph. The SGD algorithm never computes these vectors $y_{t}$, but we are only using them as an analysis tool. From the equation $x_{t + 1} = {y_{t} - {\eta\omega_{t}}}$ we obtain the following update rule relating $y_{t + 1}$ to $y_{t}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This alternative view helps to explain why SGD converges to a good local minimum, even when $f$ has many other sharp local minima. Intuitively, sharp local minima are eliminated by the convolution operator that transforms $f$ to $g_{t}$, since convolution has the effect of smoothing out short-range fluctuations. This reasoning ensures that SGD converges to a good local minimum under much weaker conditions, because instead of imposing convexity or one-point convexity requirements on $f$ itself, we only require those properties to hold for the smoothed functions obtained from $f$ by convolution. We can formalize the foregoing argument using the following assumption.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

For a fixed point $x^{\ast}$^33^3Notice that $x^{\ast}$ is not necessarily the global optimal in the original function $f$ due to the convolution operator., noise distribution $W{(x)}$, step size $\eta$, the function $f$ is $c$-one point strongly convex with respect to $x^{\ast}$ after convolved with noise. That is, for any $x,y$ in domain $\mathbb{D}$ s.t. $y = {x - {\eta{\nabla f}{(x)}}}$,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

For point $y$, since the direction $x^{\ast} - y$ points to $x^{\ast}$, by having positive inner product with $x^{\ast} - y$, we know the direction $- {\eta{\nabla f}{({y_{t} - {\eta\omega_{t}}})}}$ in approximately points to $x^{\ast}$ in expectation (See more discussion on one point convexity in Appendix).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

Let us first see a simple example in Figure 3. We use $F_{r,c}$ to denote the sub-figure at row $r$ and column $c$. The function $f$ at $F_{1,1}$ is a approximately convex function, but very spiky. Therefore, GD easily gets stuck at various local minima, see $F_{2,1}$. However, we want to get rid of those spurious local minima, and get a point near $x^{\ast} = 0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

If we take the alternative view that SGD works on the convolved version of $f$ ($F_{1,2}$, $F_{1,3}$, $F_{1,4}$), we find that those functions are much smoother and contain few local minima. However, the gradient noise here is a double-edged sword. On one hand, if the noise is small, the convolved $f$ is still somewhat non-convex, then SGD may find a few bad local minima as shown in $F_{2,2}$. On the other hand, if the noise is too large, the noise dominates the gradient, and SGD will act like random walk, see $F_{2,4}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

$F_{2,3}$ seems like a nice tradeoff, as all trials converges to a local region near $0$, but the region is too big (most points are in $\lbrack{- 1.5},1.5\rbrack$). In order to get closer to $0$, we may "restart" SGD with a point in $\lbrack{- 1.5},1.5\rbrack$, using smaller noise level $0.15$. Recall in $F_{2,2}$, SGD fails because the convolved $f$ has a few non-convex regions ($F_{1,2}$), so SGD may find spurious local minima. However, those local minima are outside $\lbrack{- 1.5},1.5\rbrack$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

The convolved $f$ in $F_{1,2}$ restricted in $\lbrack{- 1.5},1.5\rbrack$ is pretty convex, so if we start a point in this region, SGD converges to a smaller local region centered at $0$, see $F_{3,2}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivating Example", "weight": 1.0} -->

We may do this iteratively, with even smaller noise levels and smaller initialization regions, and finally we will get pretty close to $0$ with decent probability, see $F_{3,3}$ and $F_{3,4}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Empirical Observations", "weight": 1.0} -->

(a) SGD trajectory is locally one point convex.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Empirical Observations", "weight": 1.0} -->

(b) The neighborhood of SGD trajectory is one point convex.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Empirical Observations", "weight": 1.0} -->

In this section, we explore the loss surfaces of modern neural networks, and show that they enjoy many nice one point convex properties. Therefore, our main theorem could be used for explaining why SGD works so well in practice.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The SGD trajectory is one point convex", "weight": 1.0} -->

It is well known that the loss surface of neural network is highly non-convex, with numerous local minima. However, we observe that the loss surface is consisted of many one point convex basin region, while each time SGD traverses one of such regions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The SGD trajectory is one point convex", "weight": 1.0} -->

See Figure 5(a) for details. We ran experiments on Resnet ($34$ layers, $\approx 1.2$M parameters), Densenet ($100$ layers, $\approx 0.8$M parameters) on cifar10 and cifar100, each for 5 trials with $300$ epochs and different initializations. For the start of every epoch $x_{t}$ in each trial, we compute the inner product between the negative gradient $- {{\nabla f}{(x_{t})}}$ and the direction $x_{300} - x_{t}$. In Figure 5(a), we plot the minimum value for every epoch among $5$ trials for each setting. Notice that except for the starting period of densenet on Cifar-10, all the other networks in all trials have positive inner products, which shows that the trajectory of SGD (except the starting period) is one point convex with respect to the final solution^55^5Similar observations were implicitly observed previously..

<!-- chunk {"id": "body-0025", "role": "body", "section": "The SGD trajectory is one point convex", "weight": 1.0} -->

In these experiments, we have used the standard step size schedule ($0.1$ initially, $0.01$ after epoch $150$, and $0.001$ after epoch $225$). However, we got the same observation when using smoothly decreasing step sizes (shrink by $0.99$ per epoch).

<!-- chunk {"id": "body-0026", "role": "body", "section": "The neighborhood of the trajectory is one point convex", "weight": 1.0} -->

Having a one point convex trajectory for $5$ trials does not suffice to show SGD always has a simple and easy trajectory, due to the randomness of the stochastic gradient. Indeed, by a slight random perturbation, SGD might be in a completely different trajectory that is far from being one point convex to the final solution. However, in this subsection, we show that it is not the case, as the SGD trajectory is one point convex after convolving with uniform ball with radius $0.5$. That means, the whole neighborhood of the SGD trajectory is one point convex with respect to the final solution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The neighborhood of the trajectory is one point convex", "weight": 1.0} -->

In this experiment, we tried Resnet ($34$ layers, $\approx 1.2$M parameters), Densenet ($100$ layers, $\approx 0.8$M parameters) on cifar10 and cifar100^66^6We also tried VGG with $\approx 1$M parameters, but does not have similar observations. This might be why Resnet and Densenet are slightly easier to optimize.. For every epoch in each setting, we take one point and look at its neighborhood with radius $0.5$ (upper bound of the length of one SGD step, as we will show below). We take $100$ random points inside each neighborhood to verify Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?")^77^7We also tried to sample points that are one SGD step away to represent the neighborhood, and got similar observations..

<!-- chunk {"id": "body-0028", "role": "body", "section": "The neighborhood of the trajectory is one point convex", "weight": 1.0} -->

More specifically, for every random point $w$ in the neighborhood of $x_{t}$, we computer $\langle{- {{\nabla f}{(w)}}},{x_{300} - x_{t}}\rangle$. Figure 5(b) shows the mean value (solid line), as well as upper and lower bound of the inner product (shaded area). As we can see, the inner products for all epochs in every setting have small variances, and are always positive. Although we could not verify Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") by computing the exact expectation due to limited computational resources, from Figure 5(b) and Hoeffding bound (Lemma 6. ‣ 5.2 The neighborhood of the trajectory is one point convex ‣ 5 Empirical Observations ‣ An Alternative View: When Does SGD Escape Local Minima?")), we conclude that Assumption 2. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") should hold with high probability.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Loss surface is locally a \"slope\"", "weight": 1.0} -->

Even with the observation that the whole neighborhood along the SGD trajectory is one point convex with respect to the final solution, there exists a chicken-and-egg concern, as the final target is generated using the SGD trajectory.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Loss surface is locally a \"slope\"", "weight": 1.0} -->

In this subsection, we show that the one point convexity is a pretty "global" property. We were running Resnet and Densenet, but with smaller networks (each with about $10K$ parameters). For each network, if we fix the first $10$ epochs, and generate $50$ SGD trajectories with different random seeds for $140$ epochs and $0.1$ learning rate, we get $50$ different final solutions (they are pretty far away from each other, with minimum pairwise distance $40$). For each network, if we look at the inner product between the negative gradient of any epoch of any trajectories, and the vector pointing to any final solutions, we find that the inner products are almost always positive. (only $0.1\%$ of the inner products are not positive for Densenet, and only $2$ out of $343,000$ inner products are not positive for Resnet).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Loss surface is locally a \"slope\"", "weight": 1.0} -->

This indicates that the loss surface is "skewed" to the similar direction, and our observation that the whole SGD trajectory is one point convex w.r. to the last point is not a coincidence. Based on our Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?"), such loss surface is very friendly to SGD optimization, even with a few exceptional points that are not one point convex with respect to the final solution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Loss surface is locally a \"slope\"", "weight": 1.0} -->

Notice that in general, it is not possible that all the negative gradients of all points are one point convex with respect to multiple target points. For example, if we take $1D$ interpolation between any two target points, we could easily find points that have negative gradients only pointing to one target point. However, based on our simulation, empirically SGD almost never traverse those regions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Spectrum of the local minima", "weight": 1.0} -->

From the previous subsections, we know that the loss surface of neural network has great one point convex properties. It seems that by our Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?"), SGD will almost always converge to a few target points (or regions). However, empirically SGD converges to very different target points. In this subsection, we argue that this is because of the learning rate is too big for SGD to converge (Theorem 3). On the other hand, whenever we shrink the learning rate to $0.01$, Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?") immediately applies and SGD converges to a local minimum.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Spectrum of the local minima", "weight": 1.0} -->

In this experiment, we were running smaller version of Resnet and Densenet (each with about $10K$ parameters) on and Cifar100. For each setting, we first train the network with step size $0.1$ for $300$ epochs, then we pick different epochs as the new starting points for finding nearby local minima using smaller learning rates with additional $150$ epochs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Spectrum of the local minima", "weight": 1.0} -->

See Figure 6(a) and Figure 6(b). Starting from different epochs, we got local minima with decreasing validation loss and training loss.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Spectrum of the local minima", "weight": 1.0} -->

To show that these local minima are not from the same region, we also plot the distance of the local minima to the (unique) initialized point. As we can see, as we pick later epochs as the starting points, we get local minima that are farther away from the initialization with better quality (also observed in ).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Spectrum of the local minima", "weight": 1.0} -->

Furthermore, we observe that for every local minimum, the whole trajectory is always one point convex to that local minimum. Therefore, the time for shrinking learning rate decides the quality of the final local minimum. That is, using large step size initially avoids being trapped into a bad local minimum, and whenever we are distant enough from the initialization, we can shrink the step size and converge to a good local minimum (due to one point convexity by Theorem 4. ‣ 1 Introduction ‣ An Alternative View: When Does SGD Escape Local Minima?")).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we take an alternative view of SGD that it is working on the convolved version of the loss function. Under this view, we could show that when the convolved function is one point convex with respect to the final solution $x^{\ast}$, SGD could escape all the other local minima and stay around $x^{\ast}$ with constant probability.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

To show our assumption is reasonable, we look at the loss surface of modern neural networks, and find that SGD trajectory has nice local one point convex properties, therefore the loss surface is very friend to SGD optimization. It remains an interesting open question to prove local one point convex property for deep neural networks.
