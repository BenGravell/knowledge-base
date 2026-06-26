<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Revisiting the Polyak Step Size

Topics include Convex optimization, Gradient descent, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper revisits the Polyak step size schedule for convex optimization problems, proving that a simple variant of it simultaneously attains near optimal convergence rates for the gradient descent algorithm, for all ranges of strong convexity, smoothness, and Lipschitz parameters, without a-priory knowledge of these parameters.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scaleable optimization for machine learning is based entirely on first order gradient methods. Besides the age-old method of stochastic approximation, three accelerated methods have proved their practical and theoretical significance: Nesterov acceleration, variance reduction and adaptive learning-rate/regularization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Adaptive choices of step sizes allow optimization algorithms to accelerate quickly according to the local curvature and smoothness of the optimization landscape. However, in theory, there are few parameter free algorithms, and, in practice, there are many search heuristics utilized.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let us examine this question of parameter free, adaptive learning rates for one of the most standard algorithms, namely the gradient descent method: Although this class of algorithms is not optimal in all settings (i.e. the aforementioned accelerations can be applied), it is fundamental, and we may ask what are optimal known rates along with the optimal step size choices are for this particular algorithm. Here, Table 1 shows the best known rates for gradient descent in the standard regimes: general convex (non-smooth with bounded sub-gradients); $\beta$-smooth; $\alpha$-strongly-convex; and $\beta$-smooth&$\alpha$-strongly convex (see for more details).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

From a practical perspective these step size settings are unfortunately disparate in various regimes: ranging from rapidly decaying at $\eta_{t} = {O{(\frac{1}{\alphat})}}$ to moderately decaying at $\eta_{t} = {O{(\frac{1}{\sqrt{t}})}}$ to a constant $\eta_{t} = \frac{1}{\beta}$ (see for more details).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work: We show that a single (and simple) choice of a step size schedule gives, simultaneously, the optimal convergence (among the class of gradient descent algorithms) in all these regimes, without knowing these parameters in advance. Perhaps surprisingly, this choice is that prescribed, who argued that this choice was optimal for the non-smooth, convex case (marked as "convex" in Table 1, see also). $e^{- {\frac{\beta}{\alpha}T}}$ Table 1: Standard convergence rates of gradient descent in convex optimization problems. Error denotes f (xt) − f (x⋆) of a first order methods as a function of the number of iterations. Step Size is the standard learning rate schedule used to obtain this rate. Dependence on other parameters, namely the Lipchitz constant and initial distance to the objective, is omitted.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Convexity Preliminaries", "weight": 1.0} -->

The following are basic properties for $\alpha$-strongly-convex functions and/or $\beta$-smooth functions (proved for completeness in Lemma 4): The following standard lemma is at the heart of much of the analysis of first order convex optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Main Results", "weight": 1.0} -->

argued that, in a sense, the optimal step size choice of $\eta_{t}$ should decrease the upper bound on $d_{t + 1}^{2}$ as fast as possible. This choice is: which leads to a decrease of $d_{t}^{2}$: Note that this choice utilizes knowledge of $f{(\mathbf{x}^{\star})}$, since $h_{t} = {{f{(\mathbf{x}_{t})}} - {f{(\mathbf{x}^{\star})}}}$. showed that this choice was optimal for non-smooth convex optimization (i.e. for bounded gradients). Our first result shows that this step size schedule (which knows $f{(\mathbf{x}^{\star})}$) achieves the min of the best known bounds in all the standard parameter regimes (among the class of projected gradient descent algorithms).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Analysis: the adaptive case", "weight": 1.0} -->

The proof of Theorem 2 rests on the following lemma which shows that, given a lower bound on the objective, the subroutine in Algorithm 3 either returns a near-optimal point with desired precision or a tighter lower bound.
