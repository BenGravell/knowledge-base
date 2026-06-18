## Introduction

Gradient based optimization underlies most of machine learning and it has attracted tremendous research attention over the years. While non-asymptotic complexity analysis of gradient based methods is well-established for convex and *smooth* nonconvex problems, little is known for nonsmooth nonconvex problems. We summarize the known rates (black) in Table 1 based on the references.

$\overset{\sim}{\mathcal{O}}\left( {\epsilon^{- 3}\delta^{- 1}} \right)$

$\overset{\sim}{\mathcal{O}}\left( {\epsilon^{- 4}\delta^{- 1}} \right)$

Table 1: When the problem is nonconvex and nonsmooth, finding a ϵ-stationary point is intractable, see Theorem 11. Thus we introduce a refined notion, (δ,ϵ)-stationarity, and provide non-asymptotic convergence rates for finding (δ,ϵ)-stationary point.

Within the nonsmooth nonconvex setting, recent research results have focused on asymptotic convergence analysis. Despite their advances, these results fail to address finite-time, non-asymptotic convergence rates. Given the widespread use of nonsmooth nonconvex problems in machine learning, a canonical example being deep ReLU neural networks, obtaining a *non-asymptotic* convergence analysis is an important open problem of fundamental interest.

We tackle this problem for nonsmooth functions that are Lipschitz and directionally differentiable. This class is rich enough to cover common machine learning problems, including ReLU neural networks. Surprisingly, even for this seemingly restricted class, finding an $\epsilon$-stationary point, i.e., a point $\overline{x}$ for which ${d{(0,{\partial{f{(\overline{x})}}})}} \leq \epsilon$, is intractable. In other words, no algorithm can guarantee to find an $\epsilon$-stationary point within a *finite* number of iterations.

This intractability suggests that, to obtain meaningful non-asymptotic results, we need to refine the notion of stationarity. We introduce such a notion and base our analysis on it, leading to the following main contributions of the paper:

We show that a traditional $\epsilon$-stationary point cannot be obtained in finite time (Theorem 5).

We study the notion of $(\delta,\epsilon)$-stationary points (see Definition 4). For smooth functions, this notion reduces to usual $\epsilon$-stationarity by setting $\delta = {O{({\epsilon/L})}}$. We provide a $\Omega{(\delta^{- 1})}$ lower bound on the number of calls if algorithms are only allowed access to a generalized gradient oracle.

We propose a normalized "gradient descent" style algorithm that achieves $\overset{\sim}{\mathcal{O}}{({\epsilon^{- 3}\delta^{- 1}})}$ complexity in finding a $(\delta,\epsilon)$-stationary point in the deterministic setting.

We propose a momentum based algorithm that achieves $\overset{\sim}{\mathcal{O}}{({\epsilon^{- 4}\delta^{- 1}})}$ complexity in finding a $(\delta,\epsilon)$-stationary point in the stochastic finite variance setting.

As a proof of concept to validate our theoretical findings, we implement our stochastic algorithm and show that it matches the performance of empirically used SGD with momentum method for training ResNets on the dataset.

Our results attempt to bridge the gap from recent advances in developing a non-asymptotic theory for nonconvex optimization algorithms to settings that apply to training deep neural networks, where, due to non-differentiability of the activations, most existing theory does not directly apply.

### Related Work

Asymptotic convergence for nonsmooth nonconvex functions. Benaïm et al. study the convergence of subgradient methods from a differential inclusion perspective; Majewski et al. extend the result to include proximal and implicit updates. Bolte & Pauwels focus on formally justifying the back propagation rule under nonsmooth conditions. In parallel, Davis et al. proved asymptotic convergence of subgradient methods assuming the objective function to be Whitney stratifiable. The class of Whitney stratifiable functions is broader than regular functions studied in, and it does not assume the regularity inequality (see Lemma 6.3 and in ). Another line of work studies convergence of gradient sampling algorithms. These algorithms assume a deterministic generalized gradient oracle. Our methods draw intuition from these algorithms and their analysis, but are non-asymptotic in contrast.

Structured nonsmooth nonconvex problems. Another line of research in nonconvex optimization is to exploit structure: Duchi & Ruan; Drusvyatskiy & Paquette; Davis & Drusvyatskiy consider the composition structure $f \circ g$ of convex and smooth functions; Bolte et al.; Zhang & He; Beck & Hallak study composite objectives of the form $f + g$ where one function is differentiable or convex/concave. With such structure, one can apply proximal gradient algorithms if the proximal mapping can be efficiently evaluated. However, this usually requires weak convexity, i.e., adding a quadratic function makes the function convex, which is not satisfied by several simple functions, e.g., $- {|x|}$.

Stationary points under smoothness. When the objective function is smooth, SGD finds an $\epsilon$-stationary point in $O{(\epsilon^{- 4})}$ gradient calls, which improves to $O{(\epsilon^{- 2})}$ for convex problems. Fast upper bounds under a variety of settings (deterministic, finite-sum, stochastic) are studied in. More recently, lower bounds have also been developed. When the function enjoys high-order smoothness, a stronger goal is to find an approximate second-order stationary point and could thus escape saddle points too. Many methods focus on this goal.

## Preliminaries

In this section, we set up the notion of generalized directional derivatives that will play a central role in our analysis. Throughout the paper, we assume that the nonsmooth function $f$ is $L$-Lipschitz continuous (more precise assumptions on the function class are outlined in §2.3).

### Generalized gradients

We start with the definition of generalized gradients, following, for which we first need:

### Definition 1

Given a point $x \in {\mathbb{R}}^{d}$, and direction $d$, the *generalized directional derivative* of $f$ is defined as

### Definition 2

The *generalized gradient* of $f$ is defined as

We recall below the following basic properties of the generalized gradient, see e.g., for details.

### Proposition 1 (Properties of generalized gradients)

$\partial{f{(x)}}$ is a nonempty, convex compact set. For all vectors $g \in {\partial{f{(x)}}}$, we have ${\| g\|} \leq L$.

${f^{\circ}{(x;d)}} = {\max{\{{{{\langle g,d\rangle} \mid g} \in {\partial{f{(x)}}}}\}}}$.

$\partial{f{(x)}}$ is an upper-semicontinuous set valued map.

$f$ is differentiable almost everywhere (as it is $L$-Lipschitz); let ${conv}{( \cdot )}$ denote the convex hull, then

Let $B$ denote the unit Euclidean ball. Then,

For any $y,z$, there exists $\lambda \in {}$ and $g \in {\partial{f{({{\lambday} + {{({1 - \lambda})}z}})}}}$ such that ${{f{(y)}} - {f{(z)}}} = {\langle g,{y - z}\rangle}$.

### Directional derivatives

Since general nonsmooth functions can have arbitrarily large variations in their "gradients," we must restrict the function class to be able to develop a meaningful complexity theory. We show below that directionally differentiable functions match this purpose well.

### Definition 3

A function $f$ is called *directionally differentiable in the sense of Hadamard* (*cf.* ) if for any mapping $\varphi:{{\mathbb{R}}_{+}\rightarrow X}$ for which ${\varphi{}} = x$ and ${\lim_{t\rightarrow 0^{+}}\frac{{\varphi{(t)}} - {\varphi{}}}{t}} = d$, the following limit exists:

In the rest of the paper, we will say a function $f$ is directionally differentiable if it is directionally differentiable in the sense of Hadamard at all $x$.

This directional differentiabilility is also referred to as Hadamard semidifferentiability in. Notably, such directional differentiability is satisfied by most problems of interest in machine learning. It includes functions such as ${f{(x)}} = {- {|x|}}$ that *do not* satisfy the so-called regularity inequality (equation in ). Moreover, it covers the class of semialgebraic functions, as well as o-minimally definable functions (see Lemma 6.1 in ) discussed in. Currently, we are unaware whether the notion of Whitney stratifiability (studied in some recent works on nonsmooth optimization) implies directional differentiability.

A very important property of directional differentiability is that it is preserved under composition.

### Lemma 2 (Chain rule)

Let $\phi$ be Hadamard directionally differentiable at $x$, and $\psi$ be Hadamard directionally differentiable at $\phi{(x)}$. Then the composite mapping $\psi \circ \phi$ is Hadamard directionally differentiable at $x$ and

A proof of this lemma can be found in. As a consequence, any neural network function composed of directionally differentiable functions, including ReLU/LeakyReLU, is directionally differentiable.

Directional differentiability also implies key properties useful in the analysis of nonsmooth problems. In particular, it enables the use of (Lebesgue) path integrals as follows.

### Lemma 3

Given any $x,y$, let ${\gamma{(t)}} = {x + {t{({y - x})}}}$, $t \in {\lbrack 0,1\rbrack}$. If $f$ is directionally differentiable and Lipschitz, then

The following important lemma further connects directional derivatives with generalized gradients.

### Lemma 4

Assume that the directional derivative exists. For any $x,d$, there exists $g \in {\partial{f{(x)}}}$ s.t. ${\langle g,d\rangle} = {f^{\prime}{(x;d)}}$.

### Nonsmooth function class of interest

Throughout the paper, we focus on the set of Lipschitz, directionally differentiable and bounded (below) functions:

where a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $L -$Lipschitz if

As indicated previously, ReLU neural networks with bounded weight norms are included in this function class.

## Stationary points and oracles

We now formally define our notion of stationarity and discuss the intractability of the standard notion. Afterwards, we formalize the optimization oracles and define measures of complexity for algorithms that use these oracles.

### Stationary points

With the generalized gradient in hand, commonly a point is called stationary if $0 \in {\partial{f{(x)}}}$. A natural question is, what is the necessary complexity to obtain an *$\epsilon$-stationary point*, i.e., a point $x$ for which

It turns out that attaining such a point is intractable. In particular, there is no finite time algorithm that can guarantee $\epsilon$-stationarity in the nonconvex nonsmooth setting. We make this claim precise in our first main result.

### Theorem 5

Given any algorithm $\mathcal{A}$ that accesses function value and generalized gradient of $f$ in each iteration, for any $\epsilon \in {\lbrack 0,1)}$ and for any finite iteration $T$, there exists $f \in {\mathcal{F}{(\Delta,L)}}$ such that the sequence ${\{ x_{t}\}}_{t \in {\lbrack 1,T\rbrack}}$ generated by $\mathcal{A}$ on the objective $f$ does not contain any $\epsilon$-stationary point with probability more than $\frac{1}{2}$.

A key ingredient of the proof is that an algorithm $\mathcal{A}$ is uniquely determined by ${\{{f{(x_{t})}},{\partial{f{(x_{t})}}}\}}_{t \in {\lbrack 1,T\rbrack}}$, the function values and gradients at the query points. For any two functions $f_{1}$ and $f_{2}$ that have the same function values and gradients at the same set of queried points $\{ x_{1},\ldots,x_{t}\}$, the distribution of the iterate $x_{t + 1}$ generated by $\mathcal{A}$ is identical for $f_{1}$ and $f_{2}$. However, due to the richness of the class of nonsmooth functions, we can find $f_{1}$ and $f_{2}$ such that the set of $\epsilon$-stationary points of $f_{1}$ and $f_{2}$ are disjoint. Therefore, the algorithm cannot find a stationary point with probability more than $\frac{1}{2}$ for both $f_{1}$ and $f_{2}$ simultaneously. Intuitively, such functions exist because a nonsmooth function could vary arbitrarily---e.g., a nonsmooth nonconvex function could have constant gradient norms except at the (local) extrema, as happens for a piecewise linear zigzag function. Moreover, the set of extrema could be of measure zero. Therefore, unless the algorithm lands exactly in this measure-zero set, it cannot find any $\epsilon$-stationary point.

Theorem 5 suggests the need for rethinking the definition of stationary points. Intuitively, even though we are unable to find an $\epsilon$-stationary point, one could hope to find a point that is close to an $\epsilon$-stationary point. This motivates us to adopt the following more refined notion:

### Definition 4

A point $x$ is called *$(\delta,\epsilon)$-stationary* if

where ${\partial{f{({x + {\deltaB}})}}}:={\text{conv}{({\cup_{y \in {x + {\deltaB}}}{\partial{f{(y)}}}})}}$ is the Goldstein $\delta$-subdifferential, introduced in.

Note that if we can find a point $y$ at most distance $\delta$ away from $x$ such that $y$ is $\epsilon$-stationary, then we know $x$ is $(\delta,\epsilon)$-stationary. However, the contrary is not true. In fact, shows that finding a point that is $\delta$ close to an $\epsilon -$stationary point requires exponential dependence on the dimension of the problem.

At first glance, Definition 4 appears to be a weaker notion since if $x$ is $\epsilon$-stationary, then it is also a $(\delta,\epsilon)$-stationary point for any $\delta \geq 0$, but not vice versa. We show that the converse implication indeed holds, assuming smoothness.

### Proposition 6

The following statements hold:

$\epsilon$-stationarity implies $(\delta,\epsilon)$-stationarity for any $\delta \geq 0$.

If $f$ is smooth with an $L$-Lipschitz gradient and if $x$ is ($\frac{\epsilon}{3L}$, $\frac{\epsilon}{3}$)-stationary, then $x$ is also $\epsilon$-stationary, i.e.

Consequently, the two notions of stationarity are equivalent for differentiable functions. It is then natural to ask: *does $(\delta,\epsilon)$-stationarity permit a finite time analysis?*

The answer is positive, as we will show later, revealing an intrinsic difference between the two notions of stationarity. Besides providing algorithms, in Theorem 11. ‣ 5 Stochastic Setting ‣ Complexity of Finding Stationary Points of Nonsmooth Nonconvex Functions") we also prove an $\Omega{(\delta^{- 1})}$ lower bound on the dependency of $\delta$ for algorithms that can only access a generalized gradient oracle.

We also note that $(\delta,\epsilon)$-stationarity behaves well as $\delta \downarrow 0$.

### Lemma 7

The set $\partial{f{({x + {\deltaB}})}}$ converges as $\delta \downarrow 0$ as

Lemma 7 enables a straightforward routine for transforming non-asymptotic analyses for finding $(\delta,\epsilon)$-stationary points to asymptotic results for finding $\epsilon$-stationary points. Indeed, assume that a finite time algorithm for finding $(\delta,\epsilon)$-stationary points is provided. Then, by repeating the algorithm with decreasing $\delta_{k}$, (e.g., $\delta_{k} = {1/k}$), any accumulation points of the repeated algorithm is an $\epsilon$-stationary point with high probability.

### Gradient Oracles

We assume that our algorithm has access to a generalized gradient oracle in the following manner:

### Assumption 1

Given $x,d$, the oracle ${\mathbb{O}}{(x,d)}$ returns a function value $f_{x}$, and a generalized gradient $g_{x}$,

In the deterministic setting, the oracle returns

In the stochastic finite-variance setting, the oracle only returns a stochastic gradient $g$ with ${{\mathbb{E}}{\lbrack g\rbrack}} = g_{x}$, where $g_{x} \in {\partial{f{(x)}}}$ satisfies ${\langle g_{x},d\rangle} = {f^{\prime}{(x,d)}}$. Moreover, the variance ${{\mathbb{E}}{\lbrack{\|{g - g_{x}}\|}^{2}\rbrack}} \leq \sigma^{2}$ is bounded. In particular, no function value is accessible.

We remark that one cannot generally evaluate the generalized gradient $\partial f$ in practice at any point where $f$ is not differentiable. When the function $f$ is not directionally differentiable, one needs to incorporate gradient sampling to estimate $\partial f$. Our oracle queries only an element of the generalized gradient and is thus weaker than querying the entire set $\partial f$. Still, finding a vector $g_{x}$ such that $\langle g_{x},d\rangle$ equals the directional derivative $f^{\prime}{(x,d)}$ is non-trivial in general. Yet, when the objective function is a composition of directionally differentiable functions, such as ReLU neural networks, and if a closed form directional derivative is available for each function in the composition, then we can find the desired $g_{x}$ by appealing to the chain rule in Lemma 2. ‣ 2.2 Directional derivatives ‣ 2 Preliminaries ‣ Complexity of Finding Stationary Points of Nonsmooth Nonconvex Functions"). This property justifies our choice of oracles.

### Algorithm class and complexity measures

An algorithm $A$ maps a function $f \in {\mathcal{F}{(\Delta,L)}}$ to a sequence of points ${\{ x_{k}\}}_{k \geq 0}$ in ${\mathbb{R}}^{n}$. We denote $A^{(k)}$ to be the mapping from previous $k$ iterations to $x_{k + 1}$. Each $x_{k}$ can potentially be a random variable, due to the stochastic oracles or algorithm design. Let ${\{\mathcal{F}_{k}\}}_{k \geq 0}$ be the filtration generated by $\{ x_{k}\}$ such that $x_{k}$ is adapted to $\mathcal{F}_{k}$. Based on the definition of the oracle, we assume that the iterates follow the structure

where ${(f_{k},g_{k})} = {{\mathbb{O}}{(y_{k},d_{k})}}$, and the point $y_{k}$ and direction $d_{k}$ are (stochastic) functions of the iterates $x_{1},\ldots,x_{k}$.

For a random process ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$, we define the complexity of ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$ for a function $f$ as the value

Let $A{\lbrack f,x_{0}\rbrack}$ denote the sequence of points generated by algorithm $A$ for function $f$. Then, we define the iteration complexity of an algorithm class $\mathcal{A}$ on a function class $\mathcal{F}$ as

At a high level, is the minimum number of oracle calls required for a fixed algorithm to find a $(\delta,\epsilon)$-stationary point with probability at least $2/3$ for all functions is class $\mathcal{F}$.

## Deterministic Setting

For optimizing $L$-smooth functions, a crucial inequality is

In other words, either the gradient is small or the function value decreases sufficiently along the negative gradient. However, when the objective function is nonsmooth, this descent property is no longer satisfied. Thus, defining an appropriate descent direction is non-trivial. Our key innovation is to solve this problem via randomization.

More specifically, in our algorithm, Interpolated Normalized Gradient Descent (Ingd), we derive a local search strategy to find the descent direction at an iterate $x_{t}$. The vector $m_{t,k}$ plays the role of descent direction and we sequentially update it until the condition

is satisfied. To connect with the descent property, observe that when $f$ is smooth, with $m_{t,k} = {{\nabla f}{(x_{t})}}$ and $\delta = {{\| m_{t,k}\|}/L}$, (descent condition) is the same as up to a factor $2$. This connection motivates our choice of descent condition.

When the descent condition is satisfied, the next iterate $x_{t + 1}$ is obtained by taking a normalized step from $x_{t}$ along the direction $m_{t,k}$. Otherwise, we stay at $x_{t}$ and continue the search for a descent direction. We raise special attention to the fact that inside the $k$-loop, the iterates $x_{t,k}$ are always obtained by taking a normalized step from $x_{t}$. Thus, all the inner iterates $x_{t,k}$ have distance exactly $\delta$ from $x_{t}$.

To update the descent direction, we incorporate a randomized strategy. We randomly sample an interpolation point $y_{t,{k + 1}}$ on the segment $\lbrack x_{t},x_{t,k}\rbrack$ and evaluate the generalized gradient $g_{t,{k + 1}}$ at this random point $y_{t,{k + 1}}$. Then, we update the descent direction as a convex combination of $g_{t,{k + 1}}$ and the previous direction $m_{t,k}$. Due to lack of smoothness, the violation of the descent condition does not directly imply that $g_{t,{k + 1}}$ is small. Instead, the projection of the generalized gradient is small along the direction $m_{t,k}$ on average. Hence, with a proper linear combination, the random interpolation allows us to guarantee the decrease of $\| m_{t,k}\|$ in expectation. This reasoning allows us to derive the non-asymptotic convergence rate in high probability.

4: Call oracle ${\sim,m_{t,1}} = {{\mathbb{O}}{(x_{t},\overset{\rightarrow}{0})}}$
8: Terminate the algorithm and return xt
13: Sample yt, k + 1 uniformly from [xt, xt, k]
20: Return xt such that ∥mt, K∥ ≤ ϵ
Algorithm 1 Interpolated Normalized Gradient Descent

### Theorem 8

In the deterministic setting and with Assumption 1(a), the Ingd algorithm with parameters $K = \frac{48L^{2}}{\epsilon^{2}}$ and $T = \frac{4\Delta}{\epsilon\delta}$ finds a $(\delta,\epsilon)$-stationary point for function class $\mathcal{F}{(\Delta,L)}$ with probability $1 - \gamma$ using at most

Since we introduce random sampling for choosing the interpolation point, even in the deterministic setting we can only guarantee a high probability result. The detailed proof is deferred to Appendix C.

A sketch of the proof is as follows. Since ${\|{x_{t,k} - x_{t}}\|} = \delta$ for any $k$, the interpolation point $y_{t,k}$ is inside the ball $x_{t} + {\deltaB}$. Hence $m_{t,k} \in {\partial{f{({x_{t} + {\deltaB}})}}}$ for any $k$. In other words, as soon as ${\| m_{t,k}\|} \leq \epsilon$ (line 7), the reference point $x_{t}$ is $(\delta,\epsilon)$-stationary. If this is not true, i.e., ${\| m_{t,k}\|} > \epsilon$, then we check whether (descent condition) holds, in which case

Knowing that the function value is lower bounded, this can happen at most $T = \frac{4\Delta}{\epsilon\delta}$ times. Thus, for at least one $x_{t}$, the local search inside the while loop is not broken by the descent condition. Finally, given that ${\| m_{t,k}\|} > \epsilon$ and the descent condition is not satisfied, we show that

This implies that ${\mathbb{E}}{\lbrack{\| m_{t,k}\|}^{2}\rbrack}$ follows a decrease of order $O{({1/k})}$. Hence with $K = {O{({1/\epsilon^{2}})}}$, we are guaranteed to find ${\| m_{t,k}\|} \leq \epsilon$ with high probability.

### Remark 9

If the problem is smooth, the descent condition is always satisfied in one iteration. Hence the global complexity of our algorithm reduces to $T = {O{({{1/\epsilon}\delta})}}$. Due to the equivalence of the notions of stationarity (Prop. 6), with $\delta = {O{({\epsilon/L})}}$, our algorithm recovers the standard $O{({1/\epsilon^{2}})}$ convergence rate for finding an $\epsilon$-stationary point. In other words, our algorithm can adapt to the smoothness condition.

## Stochastic Setting

In the deterministic setting one of the key ingredients used Ingd is to check whether the function value decreases sufficiently. However, evaluating the function value can be computationally expensive, or even infeasible in the stochastic setting. For example, when training neural networks, evaluating the entire loss function requires going through all the data, which is impractical. As a result, we do not assume access to function value in the stochastic setting and instead propose a variant of Ingd that only relies on gradient information.

2: Call oracle ${g{(x_{1})}} = {{\mathbb{O}}{(x_{1},\overset{\rightarrow}{0})}}$ and set m1 = g (x1).
4: Update xt + 1 = xt − ηt mt with $\eta_{t} = \frac{1}{{p{\| m_{t}\|}} + q}$.
5: Sample yt + 1 uniformly from [xt, xt + 1]
9: Randomly sample i uniformly from {1, …, T}.
Algorithm 2 Stochastic Ingd (x1, p, q, β, T, K)

One of the challenges of using stochastic gradients is the noisiness of the gradient evaluation. To control the variance of the associated updates, we introduce a parameter $q$ into the normalized step size:

A similar strategy is used in adaptive methods like to prevent instability. Here, we show that the constant $q$ allows us to control the variance of $x_{t + 1} - x_{t}$. In particular, it implies the bound

where $G^{2}:={L^{2} + \sigma^{2}}$ is a trivial upper-bound on the expected norm of any sampled gradient $g$.

Another substantial change (relative to Ingd) is the removal of the explicit local search, since the stopping criterion can now no longer be tested without access to the function value. Instead, one may view $x_{{t - K} + 1},\ldots,x_{t - 1},x_{t}$ as an implicit local search with respect to the reference point $x_{t - K}$. In particular, we show that when the direction $m_{t}$ has a small norm, then $x_{t - K}$ is a $(\delta,\epsilon)$-stationary point, but not $x_{t}$. This discrepancy explains why we output $x_{t - K}$ instead of $x_{t}$.

In the deterministic setting, the direction $m_{t,k}$ inside each local search is guaranteed to belong to $\partial{f{({x_{t} + {\deltaB}})}}$. Hence, controlling the norm of $m_{t,k}$ implies the $(\delta,\epsilon)$-stationarity of $x_{t}$. In the stochastic case, however, we have two complications. First, only the expectation of the gradient evaluation satisfies the membership ${{\mathbb{E}}{\lbrack{g{(y_{k})}}\rbrack}} \in {\partial{f{(y_{k})}}}$. Second, the direction $m_{t}$ is a convex combination of all the previous gradients ${g{(y_{1})}},\ldots,{g{(y_{t})}}$, with all coefficients being nonzero. In contrast, we use a re-initialization in the deterministic setting. We overcome these difficulties and their ensuing subtleties to finally obtain the following complexity result:

### Theorem 10

In the stochastic setting, with Assumption 1(b), the Stochastic-Ingd algorithm (Algorithm 2) with parameters $G = \sqrt{L^{2} + \sigma^{2}}$, $\beta = {1 - \frac{\epsilon^{2}}{64G^{2}}}$, $p = \frac{64G^{2}{\ln{({{16G}/\epsilon})}}}{\delta\epsilon^{2}}$, $q = {4Gp}$, $K = {p\delta}$, $T = {\frac{2^{16}G^{3}\Delta\text{ln}{({{16G}/\epsilon})}}{\epsilon^{4}\delta}{\max{\{ 1,\frac{G\delta}{8\Delta}\}}}}$ ensures

In other words, the number of gradient calls to achieve a ${(\delta,\epsilon)} -$stationary point is upper bounded by ${\overset{\sim}{\mathcal{O}}\left( \frac{G^{3}\Delta}{\epsilon^{4}\delta} \right)}.$

For readability, the constants in Theorem 10 have not been optimized. The high level idea of the proof is to relate ${\mathbb{E}}{\lbrack{\eta_{t}{\| m_{t}\|}^{2}}\rbrack}$ to the function value decrease ${f{(x_{t})}} - {f{(x_{t + 1})}}$, and then to perform a telescopic sum.

We would like to emphasize the use of the adaptive step size $\eta_{t}$ and the momentum term $m_{t + 1}$. These techniques arise naturally from our goal to find a $(\delta,\epsilon)$-stationary point. The step size $\eta_{t}$ helps us ensure that the distance moved is at most $\frac{1}{p}$, and hence we are certain that adjacent iterates are close to each other. The momentum term $m_{t}$ serves as a convex combination of generalized gradients, as postulated by Definition 4.

Further, even though the parameter $K$ does not directly influence the updates of our algorithm, it plays an important role in understanding our algorithm. Indeed, we show that

In other words, the conditional expectation ${\mathbb{E}}{\lbrack\left. m_{t} \middle| x_{t - K} \right.\rbrack}$ is approximately in the $\delta$-subdifferential $\partial{f{({x_{t - K} + {\deltaB}})}}$ at $x_{t - K}$. This relationship is non-trivial.

On one hand, by imposing $K \leq {\deltap}$, we ensure that $x_{{t - K} + 1},\ldots,x_{t}$ are inside the $\delta$-ball of center $x_{t - K}$. On the other hand, we guarantee that the contribution of $m_{t - K}$ to $m_{t}$ is small, providing an appropriate upper bound on the coefficient $\beta^{K}$. These two requirements help balance the different parameters in our final choice. Details of the proof may be found in Appendix D.

Recall that we do not access the function value in this stochastic setting, which is a strength of the algorithm. In fact, we can show that our $\delta^{- 1}$ dependence is tight, when the oracle has only access to generalized gradients.

### Theorem 11 (Lower bound on $\delta$ dependence)

Let $\mathcal{A}$ denote the class of algorithms defined in Section 3.2 and $\mathcal{F}{(\Delta,L)}$ denote the class of functions defined in Equation (2.3). Assume $\epsilon \in {}$ and $L = 1$. Then the iteration complexity is lower bounded by $\frac{\Delta}{8\delta}$ if the algorithm only has access to generalized gradients.

The proof is inspired by Theorem 1.1.2 in. We show that unless more than $\frac{\Delta}{8\delta}$ different points are queried, we can construct two different functions in the function class that have gradient norm $1$ at all the queried points, and the stationary points of both functions are $\Omega{(\delta)}$ away. For more details, see Appendix E.

This theorem also implies the negative result for finite time analyses that we showed in Theorem 5. Indeed, when an algorithm finds an $\epsilon$-stationary point, the point is also a $(\delta,\epsilon)$-stationary for any $\delta > 0$. Thus, the iteration complexity must be at least ${\lim_{\delta\rightarrow 0}\frac{\Delta}{8\delta}} = {+ \infty}$, i.e., no finite time algorithm can guarantee to find an $\epsilon$-stationary point.

Before moving on to the experimental section, we would like to make several comments related to different settings. First, since the stochastic setting is strictly stronger than the deterministic setting, the stochastic variant Stochastic-INGD is applicable to the deterministic setting too. Moreover, the analysis can be extended to $q = 0$, which leads to a complexity of $\mathcal{O}{({{1/\epsilon^{3}}\delta})}$. This is the same as the deterministic algorithm. However, the stochastic variant does not adapt to the smoothness condition. In other words, even if the function is differentiable, we will not obtain a faster convergence rate. In particular, if the function is smooth, by using the equivalence of the types of stationary points, Stochastic-INGD finds an $\epsilon$-stationary point in $\mathcal{O}{({1/\epsilon^{5}})}$ while standard SGD enjoys a $\mathcal{O}{({1/\epsilon^{4}})}$ convergence rate. We do not know whether a better convergence result is achievable, as our lower bound does not provide an explicit dependency on $\epsilon$; we leave this as a future research direction.

## Experiments

Figure 1: Learning curve of SGD, ADAM and Ingd on training ResNet 20 on.

In this section, we evaluate the performance of our proposed algorithm Stochastic Ingd on image classification tasks.

We train the model on the classification dataset. The dataset contains 50k training images and 10k test images in 10 classes.

We implement Stochastic Ingd in PyTorch with the inbuilt auto differentiation algorithm. We remark that except on the kink points, the auto differentiation matches the generalized gradient oracle, which justifies our choice. We benchmark the experiments with two popular machine learning optimizers, SGD with momentum and ADAM. We train the model for 100 epochs with the standard hyper-parameters from the Github repository^11^1https://github.com/kuangliu/pytorch-cifar:

For SGD with momentum, we initialize the learning rate as $0.1$, momentum as $0.9$ and reduce the learning rate by 10 at epoch 50 and 75. The weight decay parameter is set to $5 \cdot 10^{- 4}$.

For ADAM, we use constant the learning rate $10^{- 3}$, betas in $(0.9,0.999)$, and weight decay parameter $10^{- 6}$ and $\epsilon = 10^{- 3}$ for the best performance.

For Stochastic-Ingd, we use $\beta = 0.9$, $p = 1$, $q = 10$, and weight decay parameter $5 \times 10^{- 4}$.

The training and test accuracy for all three algorithms are plotted in Figure 1. We observe that Stochastic-Ingd matches the SGD baseline and outperforms the ADAM algorithm in terms of test accuracy. The above results suggests that the experimental implications of our algorithm could be interesting, but we leave a more systematic study as future direction.

## Conclusions and Future Directions

In this paper, we investigate the complexity of finding first order stationary points of nonconvex nondifferentiable functions. We focus in particular on Hadamard semi-differentiable functions, which we suspect is perhaps the most general class of functions for which the chain rule of calculus holds---see the monograph. We further extend the standard definition of $\epsilon$-stationary points for smooth functions into a new notion of $(\delta,\epsilon)$-stationary points. We justify our definition by showing that no algorithm can find a $(0,\epsilon)$ stationary point for any $\epsilon < 1$ in a finite number of iterations and conclude that a positive $\delta$ is necessary for a finite time analysis. Using the above definition and a more refined gradient oracle, we prove that the proposed algorithms find stationary points within $\mathcal{O}{({\epsilon^{- 3}\delta^{- 1}})}$ iterations in the deterministic setting and with $\mathcal{O}{({\epsilon^{- 4}\delta^{- 1}})}$ iterations in the stochastic setting.

Our results provide the first non-asymptotic analysis of nonconvex optimization algorithms in the general Lipschitz continuous setting. Yet, they also open further questions. The first question is whether the current dependence on $\epsilon$ in our complexity bound is optimal. A future research direction is to try to find provably faster algorithms or construct adversarial examples that close the gap between upper and lower bounds on $\epsilon$. Second, the rate we obtain in the deterministic case requires function evaluations and is randomized, leading to high probability bounds. Can similar rates be obtained by an algorithm oblivious to the function value? Another possible direction would be to obtain a deterministic convergence result. More specialized questions include whether one can remove the logarithmic factors from our bounds. Aside from the above questions on the rate, we can take a step back and ask high-level questions. Are there better alternatives to the current definition of $(\delta,\epsilon)$-stationary points? One should also investigate whether everywhere directional differentiability is necessary.

In addition to the open problems listed above, our work uncovers another very interesting observation. In the standard stochastic, nonconvex, and smooth setting, stochastic gradient descent is known to be theoretically optimal, while widely used practical techniques such as momentum-based and adaptive step size methods usually lead to worse theoretical convergence rates. In our proposed setting, momentum and adaptivity naturally show up in algorithm design, and become necessary for the convergence analysis. Hence we believe that studying optimization under more relaxed assumptions may lead to theorems that can better bridge the widening theory-practice divide in optimization for training deep neural networks, and ultimately lead to better insights for practitioners.
