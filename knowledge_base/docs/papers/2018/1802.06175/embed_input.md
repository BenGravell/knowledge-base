An Alternative View: When Does SGD Escape Local Minima?

Topics include Stochastic gradient descent, Local minima, Non-convex optimization, Neural networks, Optimization theory.

Provides a theoretical explanation for why SGD escapes sharp local minima, reframing SGD as optimizing a smoothed (convolved) version of the loss. The one-point convexity condition identified is broad enough to encompass neural network loss surfaces, bridging the gap between theory and practical SGD success.

Stochastic gradient descent (SGD) is widely used in machine learning. Although being commonly viewed as a fast but not accurate version of gradient descent (GD), it always finds better solutions than GD for modern neural networks. In order to understand this phenomenon, we take an alternative view that SGD is working on the convolved (thus smoothed) version of the loss function. We show that, even if the function f has many bad local minima or saddle points, as long as for every point x, the weighted average of the gradients of its neighborhoods is one point convex with respect to the desired solution x*, SGD will get close to, and then stay around x* with constant probability. More specifically, SGD will not get stuck at "sharp" local minima with small diameters, as long as the neighborhoods of these regions contain enough gradient information. The neighborhood size is controlled by step size and gradient noise. Our result identifies a set of functions that SGD provably works, which is much larger than the set of convex functions.

## Introduction

Nowadays, stochastic gradient descent (SGD), as well as its variants (Adam, Momentum, Adagrad, etc.) have become the de facto algorithms for training neural networks. SGD runs iterative updates for the weights $x_{t}$: $x_{t + 1} = {x_{t} - {\etav_{t}}}$, where $\eta$ is the step size^11^1In this paper, we use step size and learning rate interchangeably.. $v_{t}$ is the stochastic gradient that satisfies ${E{\lbrack v_{t}\rbrack}} = {{\nabla f}{(x_{t})}}$, and is usually computed using a mini-batch of the dataset.

In the regime of convex optimization, SGD is proved to be a nice tradeoff between accuracy and efficiency: it requires more iterations to converge, but fewer gradient evaluations per iteration. Therefore, for the standard empirical risk minimizing problems with $n$ points and smoothness $L$, to get to $\epsilon$-close to $x^{\ast}$, GD needs $O{({{Ln}/\epsilon})}$ gradient evaluations, but SGD with reduced variance only needs $O{({{n{\log\frac{1}{\epsilon}}} + \frac{L}{\epsilon}})}$ gradient evaluations. In these scenarios, noise is a by-product of cheap gradient computation, and does not help training.

By contrast, for non-convex optimization problems like training neural networks, noise seems crucial. It is observed that with the help of noisy gradients, SGD does not only converge faster, but also converge to a better solution compared with GD. To formally understand this phenomenon, people have analyzed the role of noise in various settings. For example, it is proved that noise helps to escape saddle points, gives better generalization, and also guarantees polynomial hitting time of good local minima under some assumptions.

## Conclusion

In this paper, we take an alternative view of SGD that it is working on the convolved version of the loss function. Under this view, we could show that when the convolved function is one point convex with respect to the final solution $x^{\ast}$, SGD could escape all the other local minima and stay around $x^{\ast}$ with constant probability.

To show our assumption is reasonable, we look at the loss surface of modern neural networks, and find that SGD trajectory has nice local one point convex properties, therefore the loss surface is very friend to SGD optimization. It remains an interesting open question to prove local one point convex property for deep neural networks.
