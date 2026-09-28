<!-- arxiv-full-text:v1 {"arxiv_id": "cs/0408007", "source": "arxiv-html"} -->

## Introduction

Consider three optimization settings where one would like to minimize a convex function (equivalently maximize a concave function). In all three settings, gradient descent is one of the most popular methods.

Offline: Minimize a fixed convex cost function $c\colon\thinspace\mathbb{R}^{d}\rightarrow\mathbb{R}$. In this case, gradient descent is $x_{t+1}=x_{t}-\eta\nabla c(x_{t})$.

Stochastic: Minimize a fixed convex cost function $c$ given only "noisy" access to $c$, for example, we can only get $c_{t}(x)=c(x)+\epsilon_{t}(x)$ for zero-mean error random error $\epsilon_{t}(x)$. Here, stochastic gradient descent is $x_{t+1}=x_{t}-\eta\nabla c_{t}(x_{t})$. (The intuition is that the expected gradient is correct, i.e. $\operatorname{\bf E}[\nabla c_{t}(x)]=\nabla\operatorname{\bf E}[c_{t}(x)]=\nabla c(x)$.) In non-convex cases, the additional randomness may actually help avoid local minima, in a manner similar to Simulated Annealing.

Online: Minimize an unknown sequence of convex functions, $c_{1},c_{2},\ldots,$ i.e. choose a sequence $x_{1},x_{2},\ldots$ where each $x_{t}$ only depends on $x_{1},x_{2},\ldots,x_{t-1}$ and $c_{1},c_{2},\ldots,c_{t-1}$. The goals is to have low regret $\sum c_{t}(x_{t})-\min\sum c_{t}(x)$ for not using the best single point, chosen with the benefit of hindsight. In this setting, Zinkevich analyzes the regret of gradient descent given by $x_{t+1}=x_{t}-\eta\nabla c_{t}(x_{t})$.

We will focus primarily on gradient descent in a "bandit" version of the online setting. As a motivating example, consider a company that has to decide, every week, how much to spend advertising on each of a $d$ different channels, represented as a vector $x_{t}\in\mathbb{R}^{d}$. At the end of each week, they calculate their total profit $p_{t}(x_{t})$. In the offline case, one might assume that each week the function $p_{1},p_{2},\ldots$ are identical. In the stochastic case, one might assume that different weeks will have profit functions, but the $p_{t}(x)$ will be noisy realizations of some true underlying profit function, for example $p_{t}(x)=p(x)+\epsilon_{t}(x)$, where $\epsilon_{t}(x)$ has mean 0. In the online case, *no assumptions* are made about a distribution over convex profit functions and instead they are modeled as the malicious choices of an (oblivious) adversary. This allows, for example, for the possibility of a bad economy which cause the profits to crash.

In this paper, we consider the bandit case where we only have black-box access to the function(s) and thus cannot access the gradient of $c_{t}$ directly for gradient descent. (In the advertising example, the advertisers only find out the total profit of their chosen $x_{t}$, and not how much they would have profited from other values of $x$.) This type of optimization is sometimes referred to as direct or gradient-free.

A natural approach in the black-box case, for all three settings, would be to estimate the gradient by evaluating the function at several places around the point, and from them estimate the gradient (see Finite Difference Stochastic Approximation, e.g. Chapter 6 of ). However, in the online setting, the functions change adversarially over time and we only can evaluate each function once. We use a one-point estimate of the gradient to sidestep these difficulties.

### A one-point estimate to the gradient

Our estimate is based on the observation that for a uniformly random unit vector $u$, The first line looks more like an approximation of the gradient than the second. But because $u$ is uniformly random over the sphere, in expectation the second term in the first line is zero. Thus, it would seem that on average, the vector $(d/\delta)f(x+\delta u)u$ is an estimate of the gradient with low bias, and thus we say loosely that it is an approximation to the gradient.

To make this precise, we show in Section 2 that $(d/\delta)f(x+\delta u)u$ is an unbiased estimator the gradient of a smoothed version of $f$, where the value of at $x$ is replaced by the average over a ball of radius $\delta$ around $x$. For a vector $v$ selected uniformly at random from the unit ball, let Interestingly, this does not require that $f$ be differentiable.

Our method of obtaining a one-point estimate of the gradient is similar to a one-point estimates proposed independently by by Granichin and Spall. Spall's estimate uses a perturbation vector $p$, in which each entry is a zero-mean independent random variable, to produce an estimate of the gradient $\hat{g}(x)=\frac{f(x+\delta p)}{\delta}\left[\frac{1}{p_{1}},\frac{1}{p_{2}},\ldots,\frac{1}{p_{d}}\right]^{T}.$ This estimate is more of a direct attempt to estimate the gradient coordinatewise and is not rotationally invariant. Spall's analysis focuses on the stochastic setting and requires that the function is three-times differentiable. In, Granichin shows that a similar approximation is sufficient to perform gradient descent in a very general stochastic model.

Unlike, we work in an adversarial model, where instead of trying to make the restrictions on the randomness of nature as weak as possible, we pessimistically assume that nature is conspiring against us. Even in the (oblivious) adversarial setting a one-point estimate of the gradient is sufficient to make gradient descent work.

### Guarantees and analysis outline

We use the following online bandit version of Zinkevich's model. There is a fixed unknown sequence of convex functions $c_{1},c_{2},\ldots,c_{n}\colon\thinspace S\rightarrow[-C,C]$, where $C>0$ and $S\subseteq\mathbb{R}^{d}$ is a convex feasible set. The decision-maker sequentially chooses points $x_{1},x_{2},\ldots,x_{n}\in S$. After $x_{t}$ is chosen, the value $c_{t}(x_{t})$ is revealed, and $x_{t+1}$ must be chosen only based on $x_{1},x_{2},\ldots,x_{t}$ and $c_{1}(x_{1}),c_{2}(x_{2}),\ldots,c_{t}(x_{t})$ (and private randomness).

Zinkevich shows that, when the gradient $\nabla c_{t}(x_{t})$ is given to the decision-maker after each round, an online gradient descent algorithm guarantees, Here $D$ is the diameter of the feasible set, and $G$ is an upper bound on the magnitudes of the gradients.

By elaborating on his technique, we present update rules for computing a sequence of $x_{t+1}$ in the absence of $\nabla c_{t}(x_{t})$, that give the following guarantee on expected regret: Notice we have replaced the differentiability and bounded gradient assumptions by bounded function assumptions. As expected, our guarantees in the bandit setting are worse than those of the full-information setting: $O(n^{5/6})$ instead of $O(n^{1/2})$. If we make an additional assumption that the functions satisfy an $L$-Lipschitz condition (which is less restrictive than a bounded gradient assumption), then we can reduce expected regret to $O(n^{3/4})$: To prove these bounds, we have several pieces to put together. First of all, we show that Zinkevich's guarantee holds unmodified for vectors that are unbiased estimates of the gradients. Here $G$ becomes an upper bound on the magnitude of the estimates.

Now, the updates should roughly be of the form $x_{t+1}=x_{t}-\eta(d/\delta)\operatorname{\bf E}[c_{t}(x_{t}+\delta u_{t})u_{t}]$. Since we can only evaluate each function at one point, that point should be $x_{t}+\delta u_{t}$. However, our analysis applies to bound $\sum c_{t}(x_{t})$ and not $\sum c_{t}(x_{t}+\delta u_{t})$. Fortunately, these points are close together and thus these values should not be too different.

Another problem that arises is that the perturbations may move points outside the feasible set. To deal with these issues, we stay on a subset of the set such that the ball of radius $\delta$ around each point in the subset is contained in $S$. In order to do this, it is helpful to have bounds on the radii $r,R$ of balls that are contained in $S$ and that contain $S$, respectively. Then guarantees can be given in terms of $R/r$. Finally, we can use existing algorithms to reshape the body so $R/r\leq d$ to get the final results.

### Related work

For direct offline optimization, i.e. from an oracle that evaluates the function, in theory one can use the ellipsoid or more recent random-walk based approaches. In black-box optimization, practitioners often use Simulated Annealing or finite difference/simulated perturbation stochastic approximation methods (see, for example, ). In the case that the functions may change dramatically over time, a single-point approximation to the gradient may be necessary. Granichin and Spall propose a different single-point estimate of the gradient.

In addition to the appeal of an online model of convex optimization, Zinkevich's gradient descent analysis can be applied to several other online problems for which gradient descent and other special-purpose algorithms have been carefully analyzed, such as Universal Portfolios, online linear regression, and online shortest paths (one convexifies to get an online shortest flow problem).

A similar line of research has developed for the problem of online linear optimization. Here, one wants to solve the related but incomparable problem of optimizing a sequence of linear functions, over a possibly non-convex feasible set, modeling problems such as online shortest paths and online binary search trees (which are difficult to convexify). Kalai and Vempala show that, for such linear optimization problems in general, if the offline optimization problem is solvable efficiently, then regret can be bounded by $O(\sqrt{n})$ also by an efficient online algorithm, in the full-information model. Awerbuch and Kleinberg generalize this to the bandit setting against an oblivious adversary (like ours). Blum and McMahan give a simpler algorithm that applies to adaptive adversaries, that may choose their functions $c_{t}$ depending on the previous points.

A few comparisons are interesting to make with the online linear optimization problem. First of all, for the bandit versions of the linear problems, there was a distinction between exploration phases and exploitation phases. During exploration phases, one action from a barycentric spanner basis of $d$ actions was chosen, for the sole purpose of estimating the linear objective function. In contrast, our algorithm does a little bit of exploration each time. Secondly, Blum and McMahan were able to compete against an adaptive adversary, using a careful Martingale analysis. It is not clear if that can be done in our setting.

### Notation

Let $\mathbb{B}$ and $\mathbb{S}$ be the unit ball and sphere centered around the origin in $d$ dimensions, respectively, The ball and sphere of radius $a$ are $a\mathbb{B}$ and $a\mathbb{S}$, correspondingly.

The sequence of functions $c_{1},c_{2},\ldots c_{n}\colon\thinspace S\rightarrow\mathbb{R}$ are fixed in advance (we only handle such an oblivious adversary, not an adaptive one). The sequence of points we pick is $x_{1},x_{2},\ldots,x_{n}$. For bandit algorithms, we need to be randomized, so we consider our expected regret: Zinkevich assumes the existence of a projection oracle $\operatorname{\bf P}_{S}(x)$, projecting the point $x$ onto the nearest point in the convex set $S$, Projecting onto the set is an elegant way to handle the situation that the gradient takes one outside of the set, and is a common trick in the optimization literature. Note that computing $\operatorname{\bf P}_{S}$ is "only" an offline convex optimization problem. While for arbitrary feasible sets, this may seem difficult, for standard shapes, such as cube, ball, simplex, etc., the calculation is quite straightforward. for all $x,y$ in the domain of $f$.

We assume $S$ contains the ball of radius $r$ centered at the origin and is contained in the ball of radius $R$, i.e.,

## Approximating the gradient with a single sample

The main observation of this section is that we can estimate the gradient of a function $f$ by taking a random unit vector $u$ and scaling it by $f(x+\delta u)$, i.e. $\hat{g}=f(x+\delta u)u$. The approximation is correct in the sense that $\operatorname{\bf E}[\hat{g}]$ is proportional to the gradient of a smoothed version of $f$. For any function $f$, for $v$ random from the unit ball, define

### Lemma 1

Fix $\delta>0$, over random unit vectors $u$,

### Proof

If $d=1$, then the fundamental theorem of calculus implies, The $d$-dimensional generalization, following from Stoke's theorem, is, Combining Eq.'s and, and the fact that ratio of volume to surface area of a $d$-dimensional ball of radius $\delta$ is $\delta/d$ gives the lemma. ∎ Notice that the function $\hat{f}$ is differentiable even when $f$ is not.

## Expected Gradient Descent

First we consider a version of gradient descent where each step $t$ we get a random vector $g_{t}$ with expectation equal to the gradient. Then we can still use Zinkevich's online analysis of gradient descent. For lack of a better choice, we use the starting point $x_{1}=0$, the center of a containing ball of radius $R\leq D$ and $x_{t+1}=\operatorname{\bf P}_{S}(x_{t}-\eta g_{t})$.

### Lemma 2

Let $c_{1},c_{2},\ldots,c_{n}\colon\thinspace S\rightarrow\mathbb{R}$ be a sequence of convex, differentiable functions. Let $x_{1},x_{2},\ldots,x_{n}\in S$ be defined by $x_{1}=0$ and $x_{t+1}=\operatorname{\bf P}_{S}(x_{t}-\eta g_{t})$, where $\eta>0$ and $g_{1},\dots,g_{n}$ are vector-valued random variables with $\operatorname{\bf E}[g_{t}\thinspace\big|\thinspace x_{t}]=\nabla c_{t}(x_{t})$ and $\|g_{t}\|\leq G$, for some $G>0$ (this also implies $\|\nabla c_{t}(x)\|\leq G$). Then, for $\eta=\frac{R}{G\sqrt{n}}$,

### Proof

Let $x_{\star}$ be a point in $S$ minimizing $\sum_{t=1}^{n}c_{t}(x)$.

Since $c_{t}$ is convex and differentiable, we can bound the difference between $c_{t}(x_{t})$ and $c_{t}(x_{\star})$ in terms of the gradient.

Taking the expectation on both sides of this inequality yields Following Zinkevich's analysis, we use $\|x_{t}-x_{\star}\|^{2}$ as a potential function. Since $S$ is convex, for any $x\in\mathbb{R}^{d}$ we have $\|\operatorname{\bf P}_{S}(x)-x_{\star}\|\leq\|x-x_{\star}\|$. So After rearranging terms, we have By putting Eq. and Eq. together we see that The last step follows because we chose $x_{1}=0$ and $S\subseteq R\mathbb{B}$. Plugging in $\eta=R/G\sqrt{n}$ gives the lemma. ∎

### Algorithm and analysis

In this section, we analyze the algorithm given in Figure 1. select unit vector ut uniformly at random Figure 1: Bandit gradient descent algorithm We begin with a few observations.

### Observation 1

The optimum in $(1-\alpha)S$ is near the optimum in $S$,

### Proof

Clearly $(1-\alpha)S\subseteq S$. Also, And since each $c_{t}$ is convex and $0\in S$, we have Finally, since for any $y\in S$ and $t\in\{1,\dots,n\}$ we have $|c_{t}(y)|\leq C$, we may conclude that

### Observation 2

For any point $x$ in $(1-\alpha)S$ the ball of radius $\alpha r$ centered at $x$ is contained in $S$.

### Proof

Since $r\mathbb{B}\subseteq S$ and $S$ is convex, we have The next observation establishes a bound on the maximum the function can change in $(1-\alpha)S$, an effective Lipschitz condition.

### Observation 3

For any $x$ in $(1-\alpha)S$ and any $y$ in $S$

### Proof

Let $y=x+\Delta$. If $|\Delta|>\alpha r$, the observation follows from $|c_{t}|<C$. Otherwise, let $z=x+\alpha r\frac{\Delta}{|\Delta|}$, the point at distance $\alpha r$ from $x$ in the direction $\Delta$. By the previous observation, we know $z\in S$. Also, $y=\frac{|\Delta|}{\alpha r}z+\left(1-\frac{|\Delta|}{\alpha r}\right)x$, so, Now we are ready to select the parameters.

### Theorem 1

For any $n\geq\left(\frac{3Rd}{2r}\right)^{2}$ and $\nu=\frac{R}{C\sqrt{n}}$, $\delta=\sqrt{\frac{rR^{2}d^{2}}{12n}}$, and $\alpha=\sqrt{\frac{3Rd}{2r\sqrt{n}}}$, the expected regret of $\mathrm{BGD}(\nu,\delta,\alpha)$ is upper bounded by

### Proof

We begin by showing that the points $x_{t}\in S$. Since $y_{t}\in(1-\alpha)S$, Observation 2 implies this fact as long as $\frac{\delta}{r}\leq\alpha<1$, which is the case for $n\geq(3Rd/2r)^{2}$.

Suppose we wanted to run the gradient descent algorithm on the functions $\hat{c}_{t}$ defined, and the set $(1-\alpha)S$. If we let then (since $u_{t}$ is selected uniformly at random from $\mathbb{S}$) Lemma 1 says $\operatorname{\bf E}[g_{t}\thinspace\big|\thinspace x_{t}]=\nabla\hat{c}_{t}(x_{t})$. So Lemma 2 applies with the update rule: which is exactly the update rule we are using to obtain $y_{t}$, with $\eta=\nu\delta/d$. Since we can apply Lemma 2 with $G=dC/\delta$. By our choice of $\nu$, we have $\eta=R/G\sqrt{n}$, and so the expected regret is upper bounded by Let $L=\frac{2C}{\alpha r}$, which will act an "effective Lipschitz constant". Notice that for $x\in(1-\alpha)S$ Observation 3 shows that $|\hat{c}_{t}(x)-c_{t}(x)|\leq\delta L$ since $\hat{c}_{t}$ is an average over inputs within $\delta$ of $x$. Since $|y_{t}-x_{t}|=\delta$, Observation 3 also shows that These with the above imply, so rearranging terms and using Observation 1 gives Plugging in $L=\frac{2C}{\alpha r}$ gives, This expression is of the form $\frac{a}{\delta}+b\frac{\delta}{\alpha}+c\alpha$. Setting $\delta=\sqrt{\frac{a^{2}}{bc}}$ and $\alpha=\sqrt{\frac{ab}{c^{2}}}$ gives a value of $3\sqrt{abc}$. The lemma is achieved for $a=RdC\sqrt{n}$, $b=6Cn/r$ and $c=2Cn$. ∎

### Theorem 2

If each $c_{t}$ is $L$-Lipschitz, then for $n$ sufficiently large and $\nu=\frac{R}{C\sqrt{n}}$, $\alpha=\frac{\delta}{r}$, and $\delta=n^{-.25}\sqrt{\frac{RdCr}{3(Lr+C)}},$

### Proof

The proof is quite similar to the proof of Theorem 1. Again we check that the points $x_{t}\in S$, which it is for $n$ is sufficiently large. We now have a direct Lipschitz constant, so we can use it directly in Eq.. Plugging this in with chosen values of $\alpha$ and $\delta$ gives the lemma. ∎

### Reshaping

The above regret bound depends on $R/r$, which can be very large. To remove this dependence (or at least the dependence on $1/r$), we can reshape the body to make it more "round."

The set $S$, with $r\mathbb{B}\subseteq S\subseteq R\mathbb{B}$ can be put in isotropic position. Essentially, this amounts to estimating the covariance of random samples from the body and applying an affine transformation $T$ so that the new covariance matrix is the identity matrix.

A body $T(S)\subseteq\mathbb{R}^{d}$ in isotropic position has several nice properties, including $\mathbb{B}\subseteq T(S)\subseteq d\mathbb{B}$. So, we first apply the preprocessing step to find $T$ which puts the body in isotropic position. This gives us a new $R^{\prime}=d$ and $r^{\prime}=1$. The following observation shows that we can use $L^{\prime}=LR$.

### Observation 4

Let $c_{t}^{\prime}(u)=c_{t}(T^{-1}(u))$. Then $c_{t}^{\prime}$ is $LR$-Lipschitz.

### Proof

Let $x_{1},x_{2}\in S$ and $u_{1}=T(x_{1})$, $u_{2}=T(x_{2})$. Observe that, To make this a $LR$-Lipschitz condition on $c^{\prime}_{t}$, it suffices to show that $\|x_{1}-x_{2}\|\leq R\|u_{1}-u_{2}\|.$ Suppose not, i.e. $\|x_{1}-x_{2}\|>R\|u_{1}-u_{2}\|$. Define $v_{1}=\frac{u_{1}-u_{2}}{\|u_{1}-u_{2}\|}$ and $v_{2}=-v_{1}$. Observe that $\|v_{2}-v_{1}\|=2$, and since $T(S)$ contains the ball of radius $1$, $v_{1},v_{2}\in T(S)$. Thus, $y_{1}=T^{-1}(v_{1})$ and $y_{2}=T^{-1}(v_{2})$ are in $S$. Then, since $T$ is affine, where the last line uses the assumption $\|x_{1}-x_{2}\|>R\|u_{1}-u_{2}\|$. The inequality $\|y_{1}-y_{2}\|>2R$ contradicts the assumption that $S$ is contained in a sphere of radius $R$. ∎ Many common shapes such as balls, cubes, etc., are already nicely shaped, but there exist MCMC algorithms for putting any body into isotropic position from a membership oracle. (Note that the projection oracle we assume is a stronger oracle than a membership oracle.) The latest (and greatest) algorithm for putting a body into isotropic position, due to Lovasz and Vempala, runs in time $O(d^{4})\mbox{poly-log}(d,\frac{R}{r})$. This algorithm puts the body into nearly isotropic position, which means that $\mathbb{B}\subseteq T(S)\subseteq 1.01d\mathbb{B}$. After such preprocessing we would have $r^{\prime}=1,R^{\prime}=1.01d,L^{\prime}=LR,$ and $C^{\prime}=C$. This gives,

### Corollary 1

For a set $S$ of diameter $D$, and $c_{t}$ $L$-Lipschitz, after putting $S$ into near- isotropic position, the BGD algorithm has expected regret, Without the $L$-Lipschitz condition,

### Proof

Using $r^{\prime}=1,R^{\prime}=1.01d,L^{\prime}=LR,$ and $C^{\prime}=C$, In the first case, we get an expected regret of at most $2n^{3/4}\sqrt{6(1.01d)dC(LR+C)}$. In the second case, we get an expected regret of at most $3Cn^{5/6}\sqrt{2(1.01d)d}$. ∎

### Conclusions

We have given algorithms for bandit online optimization of convex functions. Our approach is to extend Zinkevich's gradient descent analysis to a situation where we do not have access to the gradient. We give a simple trick for approximating the gradient of a function by a single sample, and we give a simple understanding of this approximation as being the gradient of a smoothed function. This is similar to a similar approximation proposed . The simplicity of our approximation make it straightforward to analyze this algorithm in an online setting, with few assumptions.

Zinkevich presents a few nice variations on the model and algorithms. He shows that an adaptive step size $\eta_{t}=O(1/\sqrt{t})$ can be used with similar guarantees. It is likely that a similar adaptive step size could be used here.

He also proves that gradient descent can be compared, to an extent, with a non-stationary adversary. He shows that relative to any sequence $z_{1},z_{2},\ldots,z_{n}$, it achieves, Thus, compared to an adversary that moves a total distance $o(n)$, he has regret $o(n)$. These types of guarantees may be extended to the bandit setting.

It would also be interesting to analyze the algorithm in an unconstrained setting, where issues of the shape of the convex set wouldn't come into play. The difficulty is that in the unconstrained setting we cannot assume the convex functions are bounded. However, since $E[c_{t}(x_{t}+\delta u_{t})u_{t}]=E[\bigl(c_{t}(x_{t}+\delta u_{t})-c_{t-1}(x_{t-1}+\delta u_{t-1})\bigr)u_{t}]$, if the functions do not change too much from period to period, one may be able to use the evaluation of the previous period as a baseline to prevent the random gradient estimate from being too large.

Acknowledgements. We would like to thank David McAllester and Rakesh Vohra for helpful discussions. We are particularly grateful to Rakesh Vohra for pointing us to the work of James Spall.
