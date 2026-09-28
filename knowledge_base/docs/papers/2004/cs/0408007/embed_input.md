<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Online Convex Optimization in the Bandit Setting: Gradient Descent without a Gradient

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider a the general online convex optimization framework introduced by Zinkevich. In this setting, there is a sequence of convex functions. Each period, we must choose a signle point (from some feasible set) and pay a cost equal to the value of the next function on our chosen point. Zinkevich shows that, if the each function is revealed after the choice is made, then one can achieve vanishingly small regret relative the best single decision chosen in hindsight. We extend this to the bandit setting where we do not find out the entire functions but rather just their value at our chosen point. We show how to get vanishingly small regret in this setting. Our approach uses a simple approximation of the gradient that is computed from evaluating a function at a single (random) point. We show that this estimate is sufficient to mimic Zinkevich's gradient descent online analysis, with access to the gradient (only being able to evaluate the function at a single point).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider three optimization settings where one would like to minimize a convex function (equivalently maximize a concave function). In all three settings, gradient descent is one of the most popular methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Offline: Minimize a fixed convex cost function $c\colon\thinspace\mathbb{R}^{d}\rightarrow\mathbb{R}$. In this case, gradient descent is $x_{t+1}=x_{t}-\eta\nabla c(x_{t})$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic: Minimize a fixed convex cost function $c$ given only "noisy" access to $c$, for example, we can only get $c_{t}(x)=c(x)+\epsilon_{t}(x)$ for zero-mean error random error $\epsilon_{t}(x)$. Here, stochastic gradient descent is $x_{t+1}=x_{t}-\eta\nabla c_{t}(x_{t})$. (The intuition is that the expected gradient is correct, i.e. $\operatorname{\bf E}[\nabla c_{t}(x)]=\nabla\operatorname{\bf E}[c_{t}(x)]=\nabla c(x)$.) In non-convex cases, the additional randomness may actually help avoid local minima, in a manner similar to Simulated Annealing.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Online: Minimize an unknown sequence of convex functions, $c_{1},c_{2},\ldots,$ i.e. choose a sequence $x_{1},x_{2},\ldots$ where each $x_{t}$ only depends on $x_{1},x_{2},\ldots,x_{t-1}$ and $c_{1},c_{2},\ldots,c_{t-1}$. The goals is to have low regret $\sum c_{t}(x_{t})-\min\sum c_{t}(x)$ for not using the best single point, chosen with the benefit of hindsight. In this setting, Zinkevich analyzes the regret of gradient descent given by $x_{t+1}=x_{t}-\eta\nabla c_{t}(x_{t})$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will focus primarily on gradient descent in a "bandit" version of the online setting. As a motivating example, consider a company that has to decide, every week, how much to spend advertising on each of a $d$ different channels, represented as a vector $x_{t}\in\mathbb{R}^{d}$. At the end of each week, they calculate their total profit $p_{t}(x_{t})$. In the offline case, one might assume that each week the function $p_{1},p_{2},\ldots$ are identical.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the stochastic case, one might assume that different weeks will have profit functions, but the $p_{t}(x)$ will be noisy realizations of some true underlying profit function, for example $p_{t}(x)=p(x)+\epsilon_{t}(x)$, where $\epsilon_{t}(x)$ has mean 0. In the online case, *no assumptions* are made about a distribution over convex profit functions and instead they are modeled as the malicious choices of an (oblivious) adversary. This allows, for example, for the possibility of a bad economy which cause the profits to crash.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we consider the bandit case where we only have black-box access to the function(s) and thus cannot access the gradient of $c_{t}$ directly for gradient descent. (In the advertising example, the advertisers only find out the total profit of their chosen $x_{t}$, and not how much they would have profited from other values of $x$.) This type of optimization is sometimes referred to as direct or gradient-free.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural approach in the black-box case, for all three settings, would be to estimate the gradient by evaluating the function at several places around the point, and from them estimate the gradient (see Finite Difference Stochastic Approximation, e.g. Chapter 6 of ). However, in the online setting, the functions change adversarially over time and we only can evaluate each function once. We use a one-point estimate of the gradient to sidestep these difficulties.

<!-- chunk {"id": "body-0011", "role": "body", "section": "A one-point estimate to the gradient", "weight": 1.0} -->

Our estimate is based on the observation that for a uniformly random unit vector $u$, The first line looks more like an approximation of the gradient than the second. But because $u$ is uniformly random over the sphere, in expectation the second term in the first line is zero. Thus, it would seem that on average, the vector $(d/\delta)f(x+\delta u)u$ is an estimate of the gradient with low bias, and thus we say loosely that it is an approximation to the gradient.

<!-- chunk {"id": "body-0012", "role": "body", "section": "A one-point estimate to the gradient", "weight": 1.0} -->

To make this precise, we show in Section 2 that $(d/\delta)f(x+\delta u)u$ is an unbiased estimator the gradient of a smoothed version of $f$, where the value of at $x$ is replaced by the average over a ball of radius $\delta$ around $x$. For a vector $v$ selected uniformly at random from the unit ball, let Interestingly, this does not require that $f$ be differentiable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "A one-point estimate to the gradient", "weight": 1.0} -->

Our method of obtaining a one-point estimate of the gradient is similar to a one-point estimates proposed independently by by Granichin and Spall. Spall's estimate uses a perturbation vector $p$, in which each entry is a zero-mean independent random variable, to produce an estimate of the gradient $\hat{g}(x)=\frac{f(x+\delta p)}{\delta}\left[\frac{1}{p_{1}},\frac{1}{p_{2}},\ldots,\frac{1}{p_{d}}\right]^{T}.$ This estimate is more of a direct attempt to estimate the gradient coordinatewise and is not rotationally invariant. Spall's analysis focuses on the stochastic setting and requires that the function is three-times differentiable. In, Granichin shows that a similar approximation is sufficient to perform gradient descent in a very general stochastic model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "A one-point estimate to the gradient", "weight": 1.0} -->

Unlike, we work in an adversarial model, where instead of trying to make the restrictions on the randomness of nature as weak as possible, we pessimistically assume that nature is conspiring against us. Even in the (oblivious) adversarial setting a one-point estimate of the gradient is sufficient to make gradient descent work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Guarantees and analysis outline", "weight": 1.0} -->

We use the following online bandit version of Zinkevich's model. There is a fixed unknown sequence of convex functions $c_{1},c_{2},\ldots,c_{n}\colon\thinspace S\rightarrow[-C,C]$, where $C>0$ and $S\subseteq\mathbb{R}^{d}$ is a convex feasible set. The decision-maker sequentially chooses points $x_{1},x_{2},\ldots,x_{n}\in S$. After $x_{t}$ is chosen, the value $c_{t}(x_{t})$ is revealed, and $x_{t+1}$ must be chosen only based on $x_{1},x_{2},\ldots,x_{t}$ and $c_{1}(x_{1}),c_{2}(x_{2}),\ldots,c_{t}(x_{t})$ (and private randomness).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Guarantees and analysis outline", "weight": 1.0} -->

Zinkevich shows that, when the gradient $\nabla c_{t}(x_{t})$ is given to the decision-maker after each round, an online gradient descent algorithm guarantees, Here $D$ is the diameter of the feasible set, and $G$ is an upper bound on the magnitudes of the gradients.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Guarantees and analysis outline", "weight": 1.0} -->

By elaborating on his technique, we present update rules for computing a sequence of $x_{t+1}$ in the absence of $\nabla c_{t}(x_{t})$, that give the following guarantee on expected regret: Notice we have replaced the differentiability and bounded gradient assumptions by bounded function assumptions. As expected, our guarantees in the bandit setting are worse than those of the full-information setting: $O(n^{5/6})$ instead of $O(n^{1/2})$. If we make an additional assumption that the functions satisfy an $L$-Lipschitz condition (which is less restrictive than a bounded gradient assumption), then we can reduce expected regret to $O(n^{3/4})$: To prove these bounds, we have several pieces to put together. First of all, we show that Zinkevich's guarantee holds unmodified for vectors that are unbiased estimates of the gradients. Here $G$ becomes an upper bound on the magnitude of the estimates.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Guarantees and analysis outline", "weight": 1.0} -->

Now, the updates should roughly be of the form $x_{t+1}=x_{t}-\eta(d/\delta)\operatorname{\bf E}[c_{t}(x_{t}+\delta u_{t})u_{t}]$. Since we can only evaluate each function at one point, that point should be $x_{t}+\delta u_{t}$. However, our analysis applies to bound $\sum c_{t}(x_{t})$ and not $\sum c_{t}(x_{t}+\delta u_{t})$. Fortunately, these points are close together and thus these values should not be too different.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Guarantees and analysis outline", "weight": 1.0} -->

Another problem that arises is that the perturbations may move points outside the feasible set. To deal with these issues, we stay on a subset of the set such that the ball of radius $\delta$ around each point in the subset is contained in $S$. In order to do this, it is helpful to have bounds on the radii $r,R$ of balls that are contained in $S$ and that contain $S$, respectively. Then guarantees can be given in terms of $R/r$. Finally, we can use existing algorithms to reshape the body so $R/r\leq d$ to get the final results.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Approximating the gradient with a single sample", "weight": 1.0} -->

The main observation of this section is that we can estimate the gradient of a function $f$ by taking a random unit vector $u$ and scaling it by $f(x+\delta u)$, i.e. $\hat{g}=f(x+\delta u)u$. The approximation is correct in the sense that $\operatorname{\bf E}[\hat{g}]$ is proportional to the gradient of a smoothed version of $f$. For any function $f$, for $v$ random from the unit ball, define

<!-- chunk {"id": "body-0021", "role": "body", "section": "Expected Gradient Descent", "weight": 1.0} -->

First we consider a version of gradient descent where each step $t$ we get a random vector $g_{t}$ with expectation equal to the gradient. Then we can still use Zinkevich's online analysis of gradient descent. For lack of a better choice, we use the starting point $x_{1}=0$, the center of a containing ball of radius $R\leq D$ and $x_{t+1}=\operatorname{\bf P}_{S}(x_{t}-\eta g_{t})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm and analysis", "weight": 1.0} -->

In this section, we analyze the algorithm given in Figure 1. select unit vector ut uniformly at random Figure 1: Bandit gradient descent algorithm We begin with a few observations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Observation 1", "weight": 1.0} -->

The optimum in $(1-\alpha)S$ is near the optimum in $S$,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Observation 2", "weight": 1.0} -->

For any point $x$ in $(1-\alpha)S$ the ball of radius $\alpha r$ centered at $x$ is contained in $S$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Observation 3", "weight": 1.0} -->

For any $x$ in $(1-\alpha)S$ and any $y$ in $S$

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reshaping", "weight": 1.0} -->

The above regret bound depends on $R/r$, which can be very large. To remove this dependence (or at least the dependence on $1/r$), we can reshape the body to make it more "round."

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reshaping", "weight": 1.0} -->

The set $S$, with $r\mathbb{B}\subseteq S\subseteq R\mathbb{B}$ can be put in isotropic position. Essentially, this amounts to estimating the covariance of random samples from the body and applying an affine transformation $T$ so that the new covariance matrix is the identity matrix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reshaping", "weight": 1.0} -->

A body $T(S)\subseteq\mathbb{R}^{d}$ in isotropic position has several nice properties, including $\mathbb{B}\subseteq T(S)\subseteq d\mathbb{B}$. So, we first apply the preprocessing step to find $T$ which puts the body in isotropic position. This gives us a new $R^{\prime}=d$ and $r^{\prime}=1$. The following observation shows that we can use $L^{\prime}=LR$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have given algorithms for bandit online optimization of convex functions. Our approach is to extend Zinkevich's gradient descent analysis to a situation where we do not have access to the gradient. We give a simple trick for approximating the gradient of a function by a single sample, and we give a simple understanding of this approximation as being the gradient of a smoothed function. This is similar to a similar approximation proposed. The simplicity of our approximation make it straightforward to analyze this algorithm in an online setting, with few assumptions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Zinkevich presents a few nice variations on the model and algorithms. He shows that an adaptive step size $\eta_{t}=O(1/\sqrt{t})$ can be used with similar guarantees. It is likely that a similar adaptive step size could be used here.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusions", "weight": 1.0} -->

He also proves that gradient descent can be compared, to an extent, with a non-stationary adversary. He shows that relative to any sequence $z_{1},z_{2},\ldots,z_{n}$, it achieves, Thus, compared to an adversary that moves a total distance $o(n)$, he has regret $o(n)$. These types of guarantees may be extended to the bandit setting.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusions", "weight": 1.0} -->

It would also be interesting to analyze the algorithm in an unconstrained setting, where issues of the shape of the convex set wouldn't come into play. The difficulty is that in the unconstrained setting we cannot assume the convex functions are bounded. However, since $E[c_{t}(x_{t}+\delta u_{t})u_{t}]=E[\bigl(c_{t}(x_{t}+\delta u_{t})-c_{t-1}(x_{t-1}+\delta u_{t-1})\bigr)u_{t}]$, if the functions do not change too much from period to period, one may be able to use the evaluation of the previous period as a baseline to prevent the random gradient estimate from being too large.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Acknowledgements. We would like to thank David McAllester and Rakesh Vohra for helpful discussions. We are particularly grateful to Rakesh Vohra for pointing us to the work of James Spall.
