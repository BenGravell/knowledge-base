<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Complexity of Finding Stationary Points of Nonsmooth Nonconvex Functions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide the first non-asymptotic analysis for finding stationary points of nonsmooth, nonconvex functions. In particular, we study the class of Hadamard semi-differentiable functions, perhaps the largest class of nonsmooth functions for which the chain rule of calculus holds. This class contains examples such as ReLU neural networks and others with non-differentiable activation functions. We first show that finding an epsilon-stationary point with first-order methods is impossible in finite time. We then introduce the notion of (delta, epsilon)-stationarity, which allows for an epsilon-approximate gradient to be the convex combination of generalized gradients evaluated at points within distance delta to the solution. We propose a series of randomized first-order methods and analyze their complexity of finding a (delta, epsilon)-stationary point. Furthermore, we provide a lower bound and show that our stochastic algorithm has min-max optimal dependence on delta. Empirically, our methods perform well for training ReLU neural networks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient based optimization underlies most of machine learning and it has attracted tremendous research attention over the years. While non-asymptotic complexity analysis of gradient based methods is well-established for convex and *smooth* nonconvex problems, little is known for nonsmooth nonconvex problems. We summarize the known rates (black) in Table 1 based on the references. $\overset{\sim}{\mathcal{O}}\left({\epsilon^{- 3}\delta^{- 1}} \right)$ $\overset{\sim}{\mathcal{O}}\left({\epsilon^{- 4}\delta^{- 1}} \right)$ Table 1: When the problem is nonconvex and nonsmooth, finding a ϵ-stationary point is intractable, see Theorem 11. Thus we introduce a refined notion, (δ, ϵ)-stationarity, and provide non-asymptotic convergence rates for finding (δ, ϵ)-stationary point.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Within the nonsmooth nonconvex setting, recent research results have focused on asymptotic convergence analysis. Despite their advances, these results fail to address finite-time, non-asymptotic convergence rates. Given the widespread use of nonsmooth nonconvex problems in machine learning, a canonical example being deep ReLU neural networks, obtaining a *non-asymptotic* convergence analysis is an important open problem of fundamental interest.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We tackle this problem for nonsmooth functions that are Lipschitz and directionally differentiable. This class is rich enough to cover common machine learning problems, including ReLU neural networks. Surprisingly, even for this seemingly restricted class, finding an $\epsilon$-stationary point, i.e., a point $\overline{x}$ for which ${d{(0,{\partial{f{(\overline{x})}}})}} \leq \epsilon$, is intractable. In other words, no algorithm can guarantee to find an $\epsilon$-stationary point within a *finite* number of iterations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This intractability suggests that, to obtain meaningful non-asymptotic results, we need to refine the notion of stationarity. We introduce such a notion and base our analysis on it, leading to the following main contributions of the paper: We show that a traditional $\epsilon$-stationary point cannot be obtained in finite time (Theorem 5).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the notion of $(\delta,\epsilon)$-stationary points (see Definition 4). For smooth functions, this notion reduces to usual $\epsilon$-stationarity by setting $\delta = {O{({\epsilon/L})}}$. We provide a $\Omega{(\delta^{- 1})}$ lower bound on the number of calls if algorithms are only allowed access to a generalized gradient oracle.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a normalized "gradient descent" style algorithm that achieves $\overset{\sim}{\mathcal{O}}{({\epsilon^{- 3}\delta^{- 1}})}$ complexity in finding a $(\delta,\epsilon)$-stationary point in the deterministic setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a momentum based algorithm that achieves $\overset{\sim}{\mathcal{O}}{({\epsilon^{- 4}\delta^{- 1}})}$ complexity in finding a $(\delta,\epsilon)$-stationary point in the stochastic finite variance setting.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a proof of concept to validate our theoretical findings, we implement our stochastic algorithm and show that it matches the performance of empirically used SGD with momentum method for training ResNets on the dataset.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our results attempt to bridge the gap from recent advances in developing a non-asymptotic theory for nonconvex optimization algorithms to settings that apply to training deep neural networks, where, due to non-differentiability of the activations, most existing theory does not directly apply.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Directional derivatives", "weight": 1.0} -->

Since general nonsmooth functions can have arbitrarily large variations in their "gradients," we must restrict the function class to be able to develop a meaningful complexity theory. We show below that directionally differentiable functions match this purpose well.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Nonsmooth function class of interest", "weight": 1.0} -->

Throughout the paper, we focus on the set of Lipschitz, directionally differentiable and bounded (below) functions: where a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $L -$Lipschitz if As indicated previously, ReLU neural networks with bounded weight norms are included in this function class.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stationary points and oracles", "weight": 1.0} -->

We now formally define our notion of stationarity and discuss the intractability of the standard notion. Afterwards, we formalize the optimization oracles and define measures of complexity for algorithms that use these oracles.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stationary points", "weight": 1.0} -->

With the generalized gradient in hand, commonly a point is called stationary if $0 \in {\partial{f{(x)}}}$. A natural question is, what is the necessary complexity to obtain an *$\epsilon$-stationary point*, i.e., a point $x$ for which It turns out that attaining such a point is intractable. In particular, there is no finite time algorithm that can guarantee $\epsilon$-stationarity in the nonconvex nonsmooth setting. We make this claim precise in our first main result.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Given $x,d$, the oracle ${\mathbb{O}}{(x,d)}$ returns a function value $f_{x}$, and a generalized gradient $g_{x}$, In the deterministic setting, the oracle returns In the stochastic finite-variance setting, the oracle only returns a stochastic gradient $g$ with ${{\mathbb{E}}{\lbrack g\rbrack}} = g_{x}$, where $g_{x} \in {\partial{f{(x)}}}$ satisfies ${\langle g_{x},d\rangle} = {f'{(x,d)}}$. Moreover, the variance ${{\mathbb{E}}{\lbrack{\|{g - g_{x}}\|}^{2}\rbrack}} \leq \sigma^{2}$ is bounded. In particular, no function value is accessible.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We remark that one cannot generally evaluate the generalized gradient $\partial f$ in practice at any point where $f$ is not differentiable. When the function $f$ is not directionally differentiable, one needs to incorporate gradient sampling to estimate $\partial f$. Our oracle queries only an element of the generalized gradient and is thus weaker than querying the entire set $\partial f$. Still, finding a vector $g_{x}$ such that $\langle g_{x},d\rangle$ equals the directional derivative $f'{(x,d)}$ is non-trivial in general. Yet, when the objective function is a composition of directionally differentiable functions, such as ReLU neural networks, and if a closed form directional derivative is available for each function in the composition, then we can find the desired $g_{x}$ by appealing to the chain rule in Lemma 2. ‣ 2.2 Directional derivatives ‣ 2 Preliminaries ‣ Complexity of Finding Stationary Points of Nonsmooth Nonconvex Functions"). This property justifies our choice of oracles.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm class and complexity measures", "weight": 1.0} -->

Based on the definition of the oracle, we assume that the iterates follow the structure where ${(f_{k},g_{k})} = {{\mathbb{O}}{(y_{k},d_{k})}}$, and the point $y_{k}$ and direction $d_{k}$ are (stochastic) functions of the iterates $x_{1},\ldots,x_{k}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm class and complexity measures", "weight": 1.0} -->

For a random process ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$, we define the complexity of ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$ for a function $f$ as the value Let $A{\lbrack f,x_{0}\rbrack}$ denote the sequence of points generated by algorithm $A$ for function $f$. Then, we define the iteration complexity of an algorithm class $\mathcal{A}$ on a function class $\mathcal{F}$ as At a high level, is the minimum number of oracle calls required for a fixed algorithm to find a $(\delta,\epsilon)$-stationary point with probability at least $2/3$ for all functions is class $\mathcal{F}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Deterministic Setting", "weight": 1.0} -->

For optimizing $L$-smooth functions, a crucial inequality is In other words, either the gradient is small or the function value decreases sufficiently along the negative gradient. However, when the objective function is nonsmooth, this descent property is no longer satisfied. Thus, defining an appropriate descent direction is non-trivial. Our key innovation is to solve this problem via randomization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Deterministic Setting", "weight": 1.0} -->

More specifically, in our algorithm, Interpolated Normalized Gradient Descent (Ingd), we derive a local search strategy to find the descent direction at an iterate $x_{t}$. The vector $m_{t,k}$ plays the role of descent direction and we sequentially update it until the condition is satisfied. To connect with the descent property, observe that when $f$ is smooth, with $m_{t,k} = {{\nabla f}{(x_{t})}}$ and $\delta = {{\| m_{t,k}\|}/L}$, (descent condition) is the same as up to a factor $2$. This connection motivates our choice of descent condition.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Deterministic Setting", "weight": 1.0} -->

When the descent condition is satisfied, the next iterate $x_{t + 1}$ is obtained by taking a normalized step from $x_{t}$ along the direction $m_{t,k}$. Otherwise, we stay at $x_{t}$ and continue the search for a descent direction. We raise special attention to the fact that inside the $k$-loop, the iterates $x_{t,k}$ are always obtained by taking a normalized step from $x_{t}$. Thus, all the inner iterates $x_{t,k}$ have distance exactly $\delta$ from $x_{t}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Deterministic Setting", "weight": 1.0} -->

To update the descent direction, we incorporate a randomized strategy. We randomly sample an interpolation point $y_{t,{k + 1}}$ on the segment $\lbrack x_{t},x_{t,k}\rbrack$ and evaluate the generalized gradient $g_{t,{k + 1}}$ at this random point $y_{t,{k + 1}}$. Then, we update the descent direction as a convex combination of $g_{t,{k + 1}}$ and the previous direction $m_{t,k}$. Due to lack of smoothness, the violation of the descent condition does not directly imply that $g_{t,{k + 1}}$ is small. Instead, the projection of the generalized gradient is small along the direction $m_{t,k}$ on average. Hence, with a proper linear combination, the random interpolation allows us to guarantee the decrease of $\| m_{t,k}\|$ in expectation. This reasoning allows us to derive the non-asymptotic convergence rate in high probability.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Deterministic Setting", "weight": 1.0} -->

4: Call oracle ${\sim,m_{t,1}} = {{\mathbb{O}}{(x_{t},\overset{\rightarrow}{0})}}$ 8: Terminate the algorithm and return xt 13: Sample yt, k + 1 uniformly from [xt, xt, k] 20: Return xt such that ∥mt, K∥ ≤ ϵ Algorithm 1 Interpolated Normalized Gradient Descent

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 9", "weight": 1.0} -->

If the problem is smooth, the descent condition is always satisfied in one iteration. Hence the global complexity of our algorithm reduces to $T = {O{({{1/\epsilon}\delta})}}$. Due to the equivalence of the notions of stationarity (Prop. 6), with $\delta = {O{({\epsilon/L})}}$, our algorithm recovers the standard $O{({1/\epsilon^{2}})}$ convergence rate for finding an $\epsilon$-stationary point. In other words, our algorithm can adapt to the smoothness condition.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stochastic Setting", "weight": 1.0} -->

In the deterministic setting one of the key ingredients used Ingd is to check whether the function value decreases sufficiently. However, evaluating the function value can be computationally expensive, or even infeasible in the stochastic setting. For example, when training neural networks, evaluating the entire loss function requires going through all the data, which is impractical. As a result, we do not assume access to function value in the stochastic setting and instead propose a variant of Ingd that only relies on gradient information.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stochastic Setting", "weight": 1.0} -->

2: Call oracle ${g{(x_{1})}} = {{\mathbb{O}}{(x_{1},\overset{\rightarrow}{0})}}$ and set m1 = g (x1). 4: Update xt + 1 = xt − ηt mt with $\eta_{t} = \frac{1}{{p{\| m_{t}\|}} + q}$. 5: Sample yt + 1 uniformly from [xt, xt + 1] 9: Randomly sample i uniformly from {1, …, T}. Algorithm 2 Stochastic Ingd (x1, p, q, β, T, K) One of the challenges of using stochastic gradients is the noisiness of the gradient evaluation. To control the variance of the associated updates, we introduce a parameter $q$ into the normalized step size: A similar strategy is used in adaptive methods like to prevent instability. Here, we show that the constant $q$ allows us to control the variance of $x_{t + 1} - x_{t}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Stochastic Setting", "weight": 1.0} -->

In particular, it implies the bound where $G^{2}:={L^{2} + \sigma^{2}}$ is a trivial upper-bound on the expected norm of any sampled gradient $g$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stochastic Setting", "weight": 1.0} -->

Another substantial change (relative to Ingd) is the removal of the explicit local search, since the stopping criterion can now no longer be tested without access to the function value. Instead, one may view $x_{{t - K} + 1},\ldots,x_{t - 1},x_{t}$ as an implicit local search with respect to the reference point $x_{t - K}$. In particular, we show that when the direction $m_{t}$ has a small norm, then $x_{t - K}$ is a $(\delta,\epsilon)$-stationary point, but not $x_{t}$. This discrepancy explains why we output $x_{t - K}$ instead of $x_{t}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Stochastic Setting", "weight": 1.0} -->

In the deterministic setting, the direction $m_{t,k}$ inside each local search is guaranteed to belong to $\partial{f{({x_{t} + {\deltaB}})}}$. Hence, controlling the norm of $m_{t,k}$ implies the $(\delta,\epsilon)$-stationarity of $x_{t}$. In the stochastic case, however, we have two complications. First, only the expectation of the gradient evaluation satisfies the membership ${{\mathbb{E}}{\lbrack{g{(y_{k})}}\rbrack}} \in {\partial{f{(y_{k})}}}$. Second, the direction $m_{t}$ is a convex combination of all the previous gradients ${g{(y_{1})}},\ldots,{g{(y_{t})}}$, with all coefficients being nonzero. In contrast, we use a re-initialization in the deterministic setting.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate the performance of our proposed algorithm Stochastic Ingd on image classification tasks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We train the model on the classification dataset. The dataset contains 50k training images and 10k test images in 10 classes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We implement Stochastic Ingd in PyTorch with the inbuilt auto differentiation algorithm. We remark that except on the kink points, the auto differentiation matches the generalized gradient oracle, which justifies our choice. We benchmark the experiments with two popular machine learning optimizers, SGD with momentum and ADAM. We train the model for 100 epochs with the standard hyper-parameters from the Github repository^11^1 For SGD with momentum, we initialize the learning rate as $0.1$, momentum as $0.9$ and reduce the learning rate by 10 at epoch 50 and 75. The weight decay parameter is set to $5 \cdot 10^{- 4}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

For ADAM, we use constant the learning rate $10^{- 3}$, betas in $(0.9,0.999)$, and weight decay parameter $10^{- 6}$ and $\epsilon = 10^{- 3}$ for the best performance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

For Stochastic-Ingd, we use $\beta = 0.9$, $p = 1$, $q = 10$, and weight decay parameter $5 \times 10^{- 4}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

The training and test accuracy for all three algorithms are plotted in Figure 1. We observe that Stochastic-Ingd matches the SGD baseline and outperforms the ADAM algorithm in terms of test accuracy. The above results suggests that the experimental implications of our algorithm could be interesting, but we leave a more systematic study as future direction.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

In this paper, we investigate the complexity of finding first order stationary points of nonconvex nondifferentiable functions. We focus in particular on Hadamard semi-differentiable functions, which we suspect is perhaps the most general class of functions for which the chain rule of calculus holds---see the monograph. We further extend the standard definition of $\epsilon$-stationary points for smooth functions into a new notion of $(\delta,\epsilon)$-stationary points. We justify our definition by showing that no algorithm can find a $(0,\epsilon)$ stationary point for any $\epsilon < 1$ in a finite number of iterations and conclude that a positive $\delta$ is necessary for a finite time analysis. Using the above definition and a more refined gradient oracle, we prove that the proposed algorithms find stationary points within $\mathcal{O}{({\epsilon^{- 3}\delta^{- 1}})}$ iterations in the deterministic setting and with $\mathcal{O}{({\epsilon^{- 4}\delta^{- 1}})}$ iterations in the stochastic setting.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

Our results provide the first non-asymptotic analysis of nonconvex optimization algorithms in the general Lipschitz continuous setting. Yet, they also open further questions. The first question is whether the current dependence on $\epsilon$ in our complexity bound is optimal. A future research direction is to try to find provably faster algorithms or construct adversarial examples that close the gap between upper and lower bounds on $\epsilon$. Second, the rate we obtain in the deterministic case requires function evaluations and is randomized, leading to high probability bounds. Can similar rates be obtained by an algorithm oblivious to the function value? Another possible direction would be to obtain a deterministic convergence result. More specialized questions include whether one can remove the logarithmic factors from our bounds. Aside from the above questions on the rate, we can take a step back and ask high-level questions. Are there better alternatives to the current definition of $(\delta,\epsilon)$-stationary points? One should also investigate whether everywhere directional differentiability is necessary.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusions and Future Directions", "weight": 1.0} -->

In addition to the open problems listed above, our work uncovers another very interesting observation. In the standard stochastic, nonconvex, and smooth setting, stochastic gradient descent is known to be theoretically optimal, while widely used practical techniques such as momentum-based and adaptive step size methods usually lead to worse theoretical convergence rates. In our proposed setting, momentum and adaptivity naturally show up in algorithm design, and become necessary for the convergence analysis. Hence we believe that studying optimization under more relaxed assumptions may lead to theorems that can better bridge the widening theory-practice divide in optimization for training deep neural networks, and ultimately lead to better insights for practitioners.
