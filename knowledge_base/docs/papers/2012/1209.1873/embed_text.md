## Introduction

We consider the following generic optimization problem associated with regularized loss minimization of linear predictors: Let $x_{1},\ldots,x_{n}$ be vectors in ${\mathbb{R}}^{d}$, let $\phi_{1},\ldots,\phi_{n}$ be a sequence of scalar convex functions, and let $\lambda > 0$ be a regularization parameter. Our goal is to solve ${\min_{w \in {\mathbb{R}}^{d}}P}{(w)}$ where^11^1Throughout this paper, we only consider the $\ell_{2}$-norm.

For example, given labels $y_{1},\ldots,y_{n}$ in $\{{\pm 1}\}$, the SVM problem (with linear kernels and no bias term) is obtained by setting ${\phi_{i}{(a)}} = {\max{\{ 0,{1 - {y_{i}a}}\}}}$. Regularized logistic regression is obtained by setting ${\phi_{i}{(a)}} = {\log{({1 + {\exp{({- {y_{i}a}})}}})}}$. Regression problems also fall into the above. For example, ridge regression is obtained by setting ${\phi_{i}{(a)}} = {({a - y_{i}})}^{2}$, regression with the absolute-value is obtained by setting ${\phi_{i}{(a)}} = {|{a - y_{i}}|}$, and support vector regression is obtained by setting ${\phi_{i}{(a)}} = {\max{\{ 0,{{|{a - y_{i}}|} - \nu}\}}}$, for some predefined insensitivity parameter $\nu > 0$.

Let $w^{\ast}$ be the optimum of. We say that a solution $w$ is $\epsilon_{P}$-sub-optimal if ${{P{(w)}} - {P{(w^{\ast})}}} \leq \epsilon_{P}$. We analyze the runtime of optimization procedures as a function of the time required to find an $\epsilon_{P}$-sub-optimal solution.

A simple approach for solving SVM is stochastic gradient descent (SGD). SGD finds an $\epsilon_{P}$-sub-optimal solution in time $\overset{\sim}{O}{({1/{({\lambda\epsilon_{P}})}})}$. This runtime does not depend on $n$ and therefore is favorable when $n$ is very large. However, the SGD approach has several disadvantages. It does not have a clear stopping criterion; it tends to be too aggressive at the beginning of the optimization process, especially when $\lambda$ is very small; while SGD reaches a moderate accuracy quite fast, its convergence becomes rather slow when we are interested in more accurate solutions.

An alternative approach is dual coordinate ascent (DCA), which solves a *dual* problem of. Specifically, for each $i$ let $\phi_{i}^{\ast}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ be the convex conjugate of $\phi_{i}$, namely, ${\phi_{i}^{\ast}{(u)}} = {\max_{z}{({{zu} - {\phi_{i}{(z)}}})}}$. The dual problem is The dual objective in has a different dual variable associated with each example in the training set. At each iteration of DCA, the dual objective is optimized with respect to a single dual variable, while the rest of the dual variables are kept in tact. then it is known that ${w{(\alpha^{\ast})}} = w^{\ast}$, where $\alpha^{\ast}$ is an optimal solution of. It is also known that ${P{(w^{\ast})}} = {D{(\alpha^{\ast})}}$ which immediately implies that for all $w$ and $\alpha$, we have ${P{(w)}} \geq {D{(\alpha)}}$, and hence the duality gap defined as can be regarded as an upper bound of the primal sub-optimality ${P{({w{(\alpha)}})}} - {P{(w^{\ast})}}$.

We focus on a *stochastic* version of DCA, abbreviated by SDCA, in which at each round we choose which dual coordinate to optimize uniformly at random. The purpose of this paper is to develop theoretical understanding of the convergence of the duality gap for SDCA.

We analyze SDCA either for $L$-Lipschitz loss functions or for $({1/\gamma})$-smooth loss functions, which are defined as follows. Throughout the paper, we will use $\phi'{(a)}$ to denote a sub-gradient of a convex function $\phi{( \cdot )}$, and use $\partial{\phi{(a)}}$ to denote its sub-differential.

### Definition 1

A function $\phi_{i}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is $L$-Lipschitz if for all ${a,b} \in {\mathbb{R}}$, we have A function $\phi_{i}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is $({1/\gamma})$-smooth if it is differentiable and its derivative is $({1/\gamma})$-Lipschitz. An equivalent condition is that for all ${a,b} \in {\mathbb{R}}$, we have where $\phi_{i}'$ is the derivative of $\phi_{i}$.

It is well-known that if $\phi_{i}{(a)}$ is $({1/\gamma})$-smooth, then $\phi_{i}^{\ast}{(u)}$ is $\gamma$ strongly convex: for all ${u,v} \in {\mathbb{R}}$ and $s \in {\lbrack 0,1\rbrack}$: Our main findings are: in order to achieve a duality gap of $\epsilon$, For $L$-Lipschitz loss functions, we obtain the rate of $\overset{\sim}{O}{({n + {L^{2}/{({\lambda\epsilon})}}})}$.

For $({1/\gamma})$-smooth loss functions, we obtain the rate of $\overset{\sim}{O}{({{({n + {1/{({\lambda\gamma})}}})}{\log{({1/\epsilon})}}})}$.

For loss functions which are almost everywhere smooth (such as the hinge-loss), we can obtain rate better than the above rate for Lipschitz loss. See Section 5 for a precise statement.

## Related Work

DCA methods are related to decomposition methods. While several experiments have shown that decomposition methods are inferior to SGD for large scale SVM, recently argued that SDCA outperform the SGD approach in some regimes. For example, this occurs when we need relatively high solution accuracy so that either SGD or SDCA has to be run for more than a few passes over the data.

However, our theoretical understanding of SDCA is not satisfying. Several authors (e.g. ) proved a linear convergence rate for solving SVM with DCA (not necessarily stochastic). The basic technique is to adapt the linear convergence of coordinate ascent that was established . The linear convergence means that it achieves a rate of ${({1 - \nu})}^{k}$ after $k$ passes over the data, where $\nu > 0$. This convergence result tells us that after an unspecified number of iterations, the algorithm converges faster to the optimal solution than SGD.

However, there are two problems with this analysis. First, the linear convergence parameter, $\nu$, may be very close to zero and the initial unspecified number of iterations might be very large. In fact, while the result of does not explicitly specify $\nu$, an examine of their proof shows that $\nu$ is proportional to the smallest nonzero eigenvalue of $X^{\top}X$, where $X$ is the $n \times d$ data matrix with its $i$-th row be the $i$-th data point $x_{i}$. For example if two data points $x_{i} \neq x_{j}$ becomes closer and closer, then $\nu\rightarrow 0$. This dependency is problematic in the data laden domain, and we note that such a dependency does not occur in the analysis of SGD.

Second, the analysis only deals with the sub-optimality of the *dual* objective, while our real goal is to bound the sub-optimality of the *primal* objective. Given a dual solution $\alpha \in {\mathbb{R}}^{n}$ its corresponding primal solution is $w{(\alpha)}$ (see ). The problem is that even if $\alpha$ is $\epsilon_{D}$-sub-optimal in the dual, for some small $\epsilon_{D}$, the primal solution $w{(\alpha)}$ might be far from being optimal. For SVM, \[4, Theorem 2\] showed that in order to obtain a primal $\epsilon_{P}$-sub-optimal solution, we need a dual $\epsilon_{D}$-sub-optimal solution with $\epsilon_{D} = {O{({\lambda\epsilon_{P}^{2}})}}$; therefore a convergence result for dual solution can only translate into a primal convergence result with worse convergence rate. Such a treatment is unsatisfactory, and this is what we will avoid in the current paper.

Some analyses of stochastic coordinate ascent provide solutions to the first problem mentioned above. For example, analyzed an exponentiated gradient dual coordinate ascent algorithm. The algorithm analyzed there (exponentiated gradient) is different from the standard DCA algorithm which we consider here, and the proof techniques are quite different. Consequently their results are not directly comparable to results we obtain in this paper. Nevertheless we note that for SVM, their analysis shows a convergence rate of $O{({n/\epsilon_{D}})}$ in order to achieve $\epsilon_{D}$-sub-optimality (on the dual) while our analysis shows a convergence of $O{({{n{\log{\log n}}} + {{1/\lambda}\epsilon}})}$ to achieve $\epsilon$ duality gap; for logistic regression, their analysis shows a convergence rate of $O{({{({n + {1/\lambda}})}{\log{({1/\epsilon_{D}})}}})}$ in order to achieve $\epsilon_{D}$-sub-optimality on the dual while our analysis shows a convergence of $O{({{({n + {1/\lambda}})}{\log{({1/\epsilon})}}})}$ to achieve $\epsilon$ duality gap.

In addition and later have analyzed randomized versions of coordinate descent for unconstrained and constrained minimization of smooth convex functions. \[3, Theorem 4\] applied these results to the dual SVM formulation. However, the resulting convergence rate is $O{({n/\epsilon_{D}})}$ which is, as mentioned before, inferior to the results we obtain here. Furthermore, neither of these analyses can be applied to logistic regression due to their reliance on the smoothness of the dual objective function which is not satisfied for the dual formulation of logistic regression. We shall also point out again that all of these bounds are for the dual sub-optimality, while as mentioned before, we are interested in the primal sub-optimality.

In this paper we derive new bounds on the duality gap (hence, they also imply bounds on the primal sub-optimality) of SDCA. These bounds are superior to earlier results, and our analysis only holds for randomized (stochastic) dual coordinate ascent. As we will see from our experiments, randomization is important in practice. In fact, the practical convergence behavior of (non-stochastic) cyclic dual coordinate ascent (even with a random ordering of the data) can be slower than our theoretical bounds for SDCA, and thus cyclic DCA is inferior to SDCA. In this regard, we note that some of the earlier analysis such as can be applied both to stochastic and to cyclic dual coordinate ascent methods with similar results. This means that their analysis, which can be no better than the behavior of cyclic dual coordinate ascent, is inferior to our analysis.

Recently, derived a stochastic coordinate ascent for structural SVM based on the Frank-Wolfe algorithm. Specifying one variant of their algorithm to binary classification with the hinge loss, yields the SDCA algorithm for the hinge-loss. The rate of convergence derived for their algorithm is the same as the rate we derive for SDCA with a Lipschitz loss function.

Another relevant approach is the Stochastic Average Gradient (SAG), that has recently been analyzed . There, a convergence rate of $\overset{\sim}{O}{({n{\log{({1/\epsilon})}}})}$ rate is shown, for the case of smooth losses, assuming that $n \geq \frac{8}{\lambda\gamma}$. This matches our guarantee in the regime $n \geq \frac{8}{\lambda\gamma}$.

The following table summarizes our results in comparison to previous analyses. Note that for SDCA with Lipschitz loss, we observe a faster practical convergence rate, which is explained with our refined analysis in Section 5.

| Algorithm | type of convergence | rate | | SGD | primal | $\overset{\sim}{O}{(\frac{1}{\lambda\epsilon})}$ | | online EG (for SVM) | dual | $\overset{\sim}{O}{(\frac{n}{\epsilon})}$ | | Stochastic Frank-Wolfe | prima-dual | $\overset{\sim}{O}{({n + \frac{1}{\lambda\epsilon}})}$ | | SDCA | primal-dual | $\overset{\sim}{O}{({n + \frac{1}{\lambda\epsilon}})}$ or faster | | Algorithm | type of convergence | rate | | SGD | primal | $\overset{\sim}{O}{(\frac{1}{\lambda\epsilon})}$ | | online EG (for logistic regression) | dual | $\overset{\sim}{O}{({{({n + \frac{1}{\lambda}})}{\log\frac{1}{\epsilon}}})}$ | | SAG (assuming $n \geq \frac{8}{\lambda\gamma}$) | primal | $\overset{\sim}{O}{({{({n + \frac{1}{\lambda}})}{\log\frac{1}{\epsilon}}})}$ | | SDCA | primal-dual | $\overset{\sim}{O}{({{({n + \frac{1}{\lambda}})}{\log\frac{1}{\epsilon}}})}$ |

## Basic Results

The generic algorithm we analyze is described below. In the pseudo-code, the parameter $T$ indicates the number of iterations while the parameter $T_{0}$ can be chosen to be a number between $1$ to $T$. Based on our analysis, a good choice of $T_{0}$ is to be $T/2$. In practice, however, the parameters $T$ and $T_{0}$ are not required as one can evaluate the duality gap and terminate when it is sufficiently small.

Procedure SDCA$(\alpha^{})$ Let $w^{} = {w{(\alpha^{})}}$ Iterate: for $t = {1,2,\ldots,T}$: Randomly pick $i$ Find $\Delta\alpha_{i}$ to maximize ${- {\phi_{i}^{\ast}{({- {({\alpha_{i}^{({t - 1})} + {\Delta\alpha_{i}}})}})}}} - {\frac{\lambdan}{2}{\|{w^{({t - 1})} + {{({\lambdan})}^{- 1}\Delta\alpha_{i}x_{i}}}\|}^{2}}$. $\alpha^{(t)}\leftarrow{\alpha^{({t - 1})} + {\Delta\alpha_{i}e_{i}}}$ $w^{(t)}\leftarrow{w^{({t - 1})} + {{({\lambdan})}^{- 1}\Delta\alpha_{i}x_{i}}}$ Output (Averaging option): Let $\overline{\alpha} = {\frac{1}{T - T_{0}}{\sum_{i = {T_{0} + 1}}^{T}\alpha^{({t - 1})}}}$ Let $\overline{w} = {w{(\overline{\alpha})}} = {\frac{1}{T - T_{0}}{\sum_{i = {T_{0} + 1}}^{T}w^{({t - 1})}}}$ return $\overline{w}$ Output (Random option): Let $\overline{\alpha} = \alpha^{(t)}$ and $\overline{w} = w^{(t)}$ for some random $t \in {{T_{0} + 1},\ldots,T}$ return $\overline{w}$ We analyze the algorithm based on different assumptions on the loss functions. To simplify the statements of our theorems, we always assume the following: For all $i$, ${\| x_{i}\|} \leq 1$ For all $i$ and $a$, ${\phi_{i}{(a)}} \geq 0$ For all $i$, ${\phi_{i}{}} \leq 1$

### Theorem 1

Consider Procedure SDCA with $\alpha^{} = 0$. Assume that $\phi_{i}$ is $L$-Lipschitz for all $i$. To obtain a duality gap of ${\mathbb{E}{\lbrack{{P{(\overline{w})}} - {D{(\overline{\alpha})}}}\rbrack}} \leq \epsilon_{P}$, it suffices to have a total number of iterations of Moreover, when $t \geq T_{0}$, we have dual sub-optimality bound of ${\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{(t)})}}}\rbrack}} \leq {\epsilon_{P}/2}$.

### Remark 1

If we choose the average version, we may simply take $T = {2T_{0}}$. Moreover, we note that Theorem 1 holds for both averaging or for choosing $w$ at random from $\{{T_{0} + 1},\ldots,T\}$. This means that calculating the duality gap at few random points would lead to the same type of guarantee with high probability. This approach has the advantage over averaging, since it is easier to implement the stopping condition (we simply check the duality gap at some random stopping points. This is in contrast to averaging in which we need to know $T,T_{0}$ in advance).

### Remark 2

The above theorem applies to the hinge-loss function, ${\phi_{i}{(u)}} = {\max{\{ 0,{1 - {y_{i}a}}\}}}$. However, for the hinge-loss, the constant $4$ in the first inequality can be replaced by $1$ (this is because the domain of the dual variables is positive, hence the constant $4$ in Lemma 4 can be replaced by $1$). We therefore obtain the bound:

### Theorem 2

Consider Procedure SDCA with $\alpha^{} = 0$. Assume that $\phi_{i}$ is $({1/\gamma})$-smooth for all $i$. To obtain an expected duality gap of ${\mathbb{E}{\lbrack{{P{(w^{(T)})}} - {D{(\alpha^{(T)})}}}\rbrack}} \leq \epsilon_{P}$, it suffices to have a total number of iterations of Moreover, to obtain an expected duality gap of ${\mathbb{E}{\lbrack{{P{(\overline{w})}} - {D{(\overline{\alpha})}}}\rbrack}} \leq \epsilon_{P}$, it suffices to have a total number of iterations of $T > T_{0}$ where

### Remark 3

If we choose $T = {2T_{0}}$, and assume that $T_{0} \geq {n + {1/{({\lambda\gamma})}}}$, then the second part of Theorem 2 implies a requirement of which is slightly weaker than the first part of Theorem 2 when $\epsilon_{P}$ is relatively large.

### Remark 4

analyzed the runtime of SGD and other algorithms from the perspective of the time required to achieve a certain level of error on the test set. To perform such analysis, we also need to take into account the *estimation error*, namely, the additional error we suffer due to the fact that the training examples defining the regularized loss minimization problem are only a finite sample from the underlying distribution. The estimation error of the primal objective behaves like $\Theta\left( \frac{1}{\lambdan} \right)$ (see ). Therefore, an interesting regime is when $\frac{1}{\lambdan} = {\Theta{(\epsilon)}}$. In that case, the bound for both Lipschitz and smooth functions would be $\overset{\sim}{O}{(n)}$. However, this bound on the estimation error is for the worst-case distribution over examples. Therefore, another interesting regime is when we would like $\epsilon \ll \frac{1}{\lambdan}$, but still $\frac{1}{\lambdan} = {O{}}$ (following the practical observation that $\lambda = {\Theta{({1/n})}}$ often performs well). In that case, smooth functions still yield the bound $\overset{\sim}{O}{(n)}$, but the dominating term for Lipschitz functions will be $\frac{1}{\lambda\epsilon}$.

### Remark 5

The runtime of SGD is $\overset{\sim}{O}{(\frac{1}{\lambda\epsilon})}$. This can be better than SDCA if $n \gg \frac{1}{\lambda\epsilon}$. However, in that case, SGD in fact only looks at $n' = {\overset{\sim}{O}{(\frac{1}{\lambda\epsilon})}}$ examples, so we can run SDCA on these $n'$ examples and obtain basically the same rate. For smooth functions, SGD can be much worse than SDCA if $\epsilon \ll \frac{1}{\lambdan}$.

## Using SGD at the first epoch

From the convergence analysis, SDCA may not perform as well as SGD for the first few epochs (each epoch means one pass over the data). The main reason is that SGD takes a larger step size than SDCA earlier , which helps its performance. It is thus natural to combine SGD and SDCA, where the first epoch is performed using a modified stochastic gradient descent rule. We show that the expected dual sub-optimality at the end of the first epoch is $\overset{\sim}{O}{({1/{({\lambdan})}})}$. This result can be combined with SDCA to obtain a faster convergence when $\lambda \gg {\log{n/n}}$.

We first introduce convenient notation. Let $P_{t}$ denote the primal objective for the first $t$ examples in the training set, The corresponding dual objective is Note that $P_{n}{(w)}$ is the primal objective given in and that $D_{n}{(\alpha)}$ is the dual objective given.

The following algorithm is a modification of SGD. The idea is to greedily decrease the dual sub-optimality for problem $D_{t}{( \cdot )}$ at each step $t$. This is different from DCA which works with $D_{n}{( \cdot )}$ at each step $t$.

Procedure Modified-SGD Initialize: $w^{} = 0$ Iterate: for $t = {1,2,\ldots,n}$: Find $\alpha_{t}$ to maximize ${- {\phi_{t}^{\ast}{({- \alpha_{t}})}}} - {\frac{\lambdat}{2}{\|{w^{({t - 1})} + {{({\lambdat})}^{- 1}\alpha_{t}x_{t}}}\|}^{2}}$. Let $w^{(t)} = {\frac{1}{\lambdat}{\sum_{i = 1}^{t}{\alpha_{i}x_{i}}}}$ return $\alpha$ We have the following result for the convergence of dual objective:

### Theorem 3

Assume that $\phi_{i}$ is $L$-Lipschitz for all $i$. In addition, assume that $(\phi_{i},x_{i})$ are iid samples from the same distribution for all $i = {1,\ldots,n}$. At the end of Procedure Modified-SGD, we have Here the expectation is with respect to the random sampling of $\{{(\phi_{i},x_{i})}:{i = {1,\ldots,n}}\}$.

### Remark 6

When $\lambda$ is relatively large, the convergence rate in Theorem 3 for modified-SGD is better than what we can prove for SDCA. This is because Modified-SGD employs a larger step size at each step $t$ for $D_{t}{(\alpha)}$ than the corresponding step size in SDCA for $D{(\alpha)}$. However, the proof requires us to assume that $(\phi_{i},x_{i})$ are randomly drawn from a certain distribution, while this extra randomness assumption is not needed for the convergence of SDCA.

Procedure SDCA with SGD Initialization Stage 1: call Procedure Modified-SGD and obtain $\alpha$ Stage 2: call Procedure SDCA with parameter $\alpha^{} = \alpha$

### Theorem 4

Assume that $\phi_{i}$ is $L$-Lipschitz for all $i$. In addition, assume that $(\phi_{i},x_{i})$ are iid samples from the same distribution for all $i = {1,\ldots,n}$. Consider Procedure SDCA with SGD Initialization. To obtain a duality gap of ${\mathbb{E}{\lbrack{{P{(\overline{w})}} - {D{(\overline{\alpha})}}}\rbrack}} \leq \epsilon_{P}$ at Stage 2, it suffices to have a total number of SDCA iterations of Moreover, when $t \geq T_{0}$, we have duality sub-optimality bound of ${\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{(t)})}}}\rbrack}} \leq {\epsilon_{P}/2}$.

### Remark 7

For Lipschitz loss, ideally we would like to have a computational complexity of $O{({n + {L^{2}/{({\lambda\epsilon_{P}})}}})}$. Theorem 4 shows that SDCA with SGD at first epoch can achieve no worst than $O{({{n{\log{({\log n})}}} + {L^{2}/{({\lambda\epsilon_{P}})}}})}$, which is very close to the ideal bound. The result is better than that of vanilla SDCA in Theorem 1 when $\lambda$ is relatively large, which shows a complexity of $O{({{n{\log{(n)}}} + {L^{2}/{({\lambda\epsilon_{P}})}}})}$. The difference is caused by small step-sizes in the vanilla SDCA, and its negative effect can be observed in practice. That is, the vanilla SDCA tends to have a slower convergence rate than SGD in the first few iterations when $\lambda$ is relatively large.

### Remark 8

Similar to Remark 2, for the hinge-loss, the constant $4$ in Theorem 4 can be reduced to 1, and the constant $20$ can be reduced to $5$.

## Refined Analysis for Almost Smooth Loss

Our analysis shows that for smooth loss, SDCA converges faster than SGD (linear versus sub-linear convergence). For non-smooth loss, the analysis does not show any advantage of SDCA over SGD. This does not explain the practical observation that SDCA converges faster than SGD asymptotically even for SVM. This section tries to refine the analysis for Lipschitz loss and shows potential advantage of SDCA over SGD asymptotically. Note that the refined analysis of this section relies on quantities that depend on the underlying data distribution, and thus the results are more complicated than those presented earlier. Although precise interpretations of these results will be complex, we will discuss them qualitatively after the theorem statements, and use them to explain the advantage of SDCA over SGD for non-smooth losses.

Although we note that for SVM, Luo and Tseng's analysis shows linear convergence of the form ${({1 - \nu})}^{k}$ for dual sub-optimality after $k$ passes over the data, as we mentioned, $\nu$ is proportional to the smallest nonzero eigenvalue of the data Gram matrix $X^{\top}X$, and hence can be arbitrarily bad when two data points $x_{i} \neq x_{j}$ becomes very close to each other. Our analysis uses a completely different argument that avoids this dependency on the data Gram matrix.

The main intuition behind our analysis is that many non-smooth loss functions are nearly smooth everywhere. For example, the hinge loss $\max{(0,{1 - {uy_{i}}})}$ is smooth at any point $u$ such that $uy_{i}$ is not close to $1$. Since a smooth loss has a strongly convex dual (and the strong convexity of the dual is directly used in our proof to obtain fast rate for smooth loss), the refined analysis in this section relies on the following refined dual strong convexity condition that holds for nearly everywhere smooth loss functions.

### Definition 2

For each $i$, we define ${\gamma_{i}{(\cdot)}} \geq 0$ so that for all dual variables $a$ and $b$, and $u \in {\partial{\phi_{i}^{\ast}{({- b})}}}$, we have For the SVM loss, we have ${\phi_{i}{(u)}} = {\max{(0,{1 - {uy_{i}}})}}$, and ${\phi_{i}^{\ast}{({- a})}} = {- {ay_{i}}}$, with ${ay_{i}} \in {\lbrack 0,1\rbrack}$ and $y_{i} \in {\{{\pm 1}\}}$. It follows that Therefore we may take ${\gamma_{i}{(u)}} = {|{{uy_{i}} - 1}|}$.

For the absolute deviation loss, we have ${\phi_{i}{(u)}} = {|{u - y_{i}}|}$, and ${\phi^{\ast}{({- a})}} = {- {ay_{i}}}$ with $a \in {\lbrack{- 1},1\rbrack}$. It follows that ${\gamma_{i}{(u)}} = {|{u - y_{i}}|}$.

### Proposition 1

Under the assumption of. Let $\gamma_{i} = {\gamma_{i}{({w^{\ast \top}x_{i}})}}$, we have the following dual strong convexity inequality: Moreover, given $w \in {\mathbb{R}}^{d}$ and ${- a_{i}} \in {\partial{\phi_{i}{({w^{\top}x_{i}})}}}$, we have For SVM, we can take $\gamma_{i} = {|{{w^{\ast \top}x_{i}y_{i}} - 1}|}$, and for the absolute deviation loss, we may take $\gamma_{i} = {|{{w^{\ast \top}x_{i}} - y_{i}}|}$. Although some of $\gamma_{i}$ can be close to zero, in practice, most $\gamma_{i}$ will be away from zero, which means $D{(\alpha)}$ is strongly convex at nearly all points. Under this assumption, we may establish a convergence result for the dual sub-optimality.

### Theorem 5

Consider Procedure SDCA with $\alpha^{} = 0$. Assume that $\phi_{i}$ is $L$-Lipschitz for all $i$ and it satisfies. Define ${N{(u)}} = {\#{\{ i:{\gamma_{i} < u}\}}}$. To obtain a dual-suboptimality of ${\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{t})}}}\rbrack}} \leq \epsilon_{D}$, it suffices to have a total number of iterations of where $s \in {\lbrack 0,1\rbrack}$ satisfies $\epsilon_{D} \geq {{8L^{2}{({{s/\lambda}n})}N{({{s/\lambda}n})}}/n}$.

### Remark 9

if ${N{({{s/\lambda}n})}}/n$ is small, then Theorem 5 is superior to Theorem 1 for the convergence of the dual objective function. We consider three scenarios. The first scenario is when $s = 1$. If ${N{({{1/\lambda}n})}}/n$ is small, and $\epsilon_{D} \geq {{8L^{2}{({{1/\lambda}n})}N{({{1/\lambda}n})}}/n}$, then the convergence is linear. The second scenario is when there exists $s_{0}$ so that ${N{({{s_{0}/\lambda}n})}} = 0$ (for SVM, it means that ${\lambdan{|{{w^{\ast \top}x_{i}y_{i}} - 1}|}} \geq s_{0}$ for all $i$), and since $\epsilon_{D} \geq {{8L^{2}{({{s_{0}/\lambda}n})}N{({{s_{0}/\lambda}n})}}/n}$, we again have a linear convergence of ${({{2n}/s_{0}})}{\log{({2/\epsilon_{D}})}}$. In the third scenario, we assume that ${{N{({{s/\lambda}n})}}/n} = {O{\lbrack{({{s/\lambda}n})}^{\nu}\rbrack}}$ for some $\nu > 0$, we can take $\epsilon_{D} = {O{({({{s/\lambda}n})}^{1 + \nu})}}$ and obtain The $\log{({1/\epsilon_{D}})}$ factor can be removed in this case with a slightly more complex analysis. This result is again superior to Theorem 1 for dual convergence.

The following result shows fast convergence of duality gap using Theorem 5.

### Theorem 6

Consider Procedure SDCA with $\alpha^{} = 0$. Assume that $\phi_{i}$ is $L$-Lipschitz for all $i$ and it satisfies. Let $\rho \leq 1$ be the largest eigenvalue of the matrix $n^{- 1}{\sum_{i = 1}{x_{i}x_{i}^{\top}}}$. Define ${N{(u)}} = {\#{\{ i:{\gamma_{i} < u}\}}}$. Assume that at time $T_{0} \geq n$, we have dual suboptimality of ${\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{(T_{0})})}}}\rbrack}} \leq \epsilon_{D}$, and define then at time $T = {2T_{0}}$, we have If for some $\gamma$, ${N{(\gamma)}}/n$ is small, then Theorem 6 is superior to Theorem 1. Although the general dependency may be complex, the improvement over Theorem 1 can be more easily seen in the special case that ${N{(\gamma)}} = 0$ for some $\gamma > 0$. In fact, in this case we have ${\overset{\sim}{\epsilon}}_{P} = {O{(\epsilon_{D})}}$, and thus This means that the convergence rate for duality gap in Theorem 6 is linear as implied by the linear convergence of $\epsilon_{D}$ in Theorem 5.

## Examples

We will specify the SDCA algorithms for a few common loss functions. For simplicity, we only specify the algorithms without SGD initialization. In practice, instead of complete randomization, we may also run in epochs, and each epoch employs a random permutation of the data. We call this variant SDCA-Perm.

Procedure SDCA-Perm$(\alpha^{})$ Let $w^{} = {w{(\alpha^{})}}$ Let $t = 0$ Iterate: for epoch $k = {1,2,\ldots}$ Let $\{ i_{1},\ldots,i_{n}\}$ be a random permutation of $\{ 1,\ldots,n\}$ Iterate: for $j = {1,2,\ldots,n}$: $t\leftarrow{t + 1}$ $i = i_{j}$ Find $\Delta\alpha_{i}$ to increase dual (\*) $\alpha^{(t)}\leftarrow{\alpha^{({t - 1})} + {\Delta\alpha_{i}e_{i}}}$ $w^{(t)}\leftarrow{w^{({t - 1})} + {{({\lambdan})}^{- 1}\Delta\alpha_{i}x_{i}}}$ Output (Averaging option): Let $\overline{\alpha} = {\frac{1}{T - T_{0}}{\sum_{i = {T_{0} + 1}}^{T}\alpha^{({t - 1})}}}$ Let $\overline{w} = {w{(\overline{\alpha})}} = {\frac{1}{T - T_{0}}{\sum_{i = {T_{0} + 1}}^{T}w^{({t - 1})}}}$ return $\overline{w}$ Output (Random option): Let $\overline{\alpha} = \alpha^{(t)}$ and $\overline{w} = w^{(t)}$ for some random $t \in {{T_{0} + 1},\ldots,T}$ return $\overline{w}$

### Lipschitz loss

Hinge loss is used in SVM. We have ${\phi_{i}{(u)}} = {\max{\{ 0,{1 - {y_{i}u}}\}}}$ and ${\phi_{i}^{\ast}{({- a})}} = {- {ay_{i}}}$ with ${ay_{i}} \in {\lbrack 0,1\rbrack}$. Absolute deviation loss is used in quantile regression. We have ${\phi_{i}{(u)}} = {|{u - y_{i}}|}$ and ${\phi_{i}^{\ast}{({- a})}} = {- {ay_{i}}}$ with $a \in {\lbrack{- 1},1\rbrack}$.

For the hinge loss, step (\*) in Procedure SDCA-Perm has a closed form solution as For absolute deviation loss, step (\*) in Procedure SDCA-Perm has a closed form solution as Both hinge loss and absolute deviation loss are $1$-Lipschitz. Therefore, we expect a convergence behavior of no worse than without SGD initialization based on Theorem 1. The refined analysis in Section 5 suggests a rate that can be significantly better, and this is confirmed with our empirical experiments.

### Smooth loss

Squared loss is used in ridge regression. We have ${\phi_{i}{(u)}} = {({u - y_{i}})}^{2}$, and ${\phi_{i}^{\ast}{({- a})}} = {{- {ay_{i}}} + {a^{2}/4}}$. Log loss is used in logistic regression. We have ${\phi_{i}{(u)}} = {\log{({1 + {\exp{({- {y_{i}u}})}}})}}$, and ${\phi_{i}^{\ast}{({- a})}} = {{ay_{i}{\log{({ay_{i}})}}} + {{({1 - {ay_{i}}})}{\log{({1 - {ay_{i}}})}}}}$ with ${ay_{i}} \in {\lbrack 0,1\rbrack}$.

For squared loss, step (\*) in Procedure SDCA-Perm has a closed form solution as For log loss, step (\*) in Procedure SDCA-Perm does not have a closed form solution. However, one may start with the approximate solution, and further use several steps of Newton's update to get a more accurate solution.

Finally, we present a smooth variant of the hinge-loss, as defined below. Recall that the hinge loss function (for positive labels) is ${\phi{(u)}} = {\max{\{ 0,{1 - u}\}}}$ and we have ${\phi^{\ast}{({- a})}} = {- a}$ with $a \in {\lbrack 0,1\rbrack}$. Consider adding to $\phi^{\ast}$ the term $\frac{\gamma}{2}a^{2}$ which yields the $\gamma$-strongly convex function Then, its conjugate, which is defined below, is $({1/\gamma})$-smooth. We refer to it as the *smoothed hinge-loss* (for positive labels): For the smoothed hinge loss, step (\*) in Procedure SDCA-Perm has a closed form solution as Both log loss and squared loss are $1$-smooth. The smoothed-hinge loss is $1/\gamma$ smooth. Therefore we expect a convergence behavior of no worse than This is confirmed in our empirical experiments.

## Proofs

We denote by $\partial{\phi_{i}{(a)}}$ the set of sub-gradients of $\phi_{i}$ at $a$. We use the notation $\phi_{i}'{(a)}$ to denote some sub-gradient of $\phi_{i}$ at $a$. For convenience, we list the following simple facts about primal and dual formulations, which will used in the proofs. For each $i$, we have The proof of our basic results stated in Theorem 2 and Theorem 1 relies on the fact that for SDCA, it is possible to lower bound the expected increase in dual objective by the duality gap. This key observation is stated in Lemma 1. Note that the duality gap can be further lower bounded using dual suboptimality. Therefore Lemma 1 implies a recursion for dual suboptimality which can be solved to obtain the convergence of dual objective. We can then apply Lemma 1 again, and the convergence of dual objective implies an upper bound of the duality gap, which leads to the basic theorems. The more refined results in Section 4 and Section 5 use similar strategies but with Lemma 1 replaced by its variants.

### Proof of Theorem 2

The key lemma, which estimates the expected increase in dual objective in terms of the duality gap, can be stated as follows.

### Lemma 1

Assume that $\phi_{i}^{\ast}$ is $\gamma$-strongly-convex (where $\gamma$ can be zero). Then, for any iteration $t$ and any $s \in {\lbrack 0,1\rbrack}$ we have Proof Since only the $i$'th element of $\alpha$ is updated, the improvement in the dual objective can be written as By the definition of the update we have for all $s \in {\lbrack 0,1\rbrack}$ that From now, we omit the superscripts and subscripts. Since $\phi^{\ast}$ is $\gamma$-strongly convex, we have that Combining this with and rearranging terms we obtain that where we used ${- u} \in {\partial{\phi{({w^{\top}x})}}}$ which yields ${\phi^{\ast}{({- u})}} = {{- {uw^{\top}x}} - {\phi{({w^{\top}x})}}}$. Therefore Next note that Therefore, if we take expectation of w.r.t. the choice of $i$ we obtain that We have obtained that Multiplying both sides by $s/n$ concludes the proof of the lemma. \We also use the following simple lemma:

### Lemma 2

For all $\alpha$, ${D{(\alpha)}} \leq {P{(w^{\ast})}} \leq {P{}} \leq 1$. In addition, ${D{}} \geq 0$.

Proof The first inequality is by weak duality, the second is by the optimality of $w^{\ast}$, and the third by the assumption that ${\phi_{i}{}} \leq 1$. For the last inequality we use ${- {\phi_{i}^{\ast}{}}} = {- {\max_{z}{({0 - {\phi_{i}{(z)}}})}}} = {{\min_{z}\phi_{i}}{(z)}} \geq 0$, which yields ${D{}} \geq 0$. \Equipped with the above lemmas we are ready to prove Theorem 2.

Proof \Proof of Theorem The assumption that $\phi_{i}$ is $({1/\gamma})$-smooth implies that $\phi_{i}^{\ast}$ is $\gamma$-strongly-convex. We will apply Lemma 1 with $s = \frac{\lambdan\gamma}{1 + {\lambdan\gamma}} \in {\lbrack 0,1\rbrack}$. Recall that ${\| x_{i}\|} \leq 1$. Therefore, the choice of $s$ implies that ${{\| x_{i}\|}^{2} - \frac{\gamma{({1 - s})}\lambdan}{s}} \leq 0$, and hence $G^{(t)} \leq 0$ for all $t$. This yields, This would be smaller than $\epsilon_{D}$ if So, requiring $\epsilon_{D}^{(t)} \leq {\frac{s}{n}\epsilon_{P}}$ we obtain a duality gap of at most $\epsilon_{P}$. This means that we should require which proves the first part of Theorem 2.

Next, we sum over $t = {T_{0},\ldots,{T - 1}}$ to obtain Now, if we choose $\overline{w},\overline{\alpha}$ to be either the average vectors or a randomly chosen vector over $t \in {\{{T_{0} + 1},\ldots,T\}}$, then the above implies It follows that in order to obtain a result of ${\mathbb{E}{\lbrack{{P{(\overline{w})}} - {D{(\overline{\alpha})}}}\rbrack}} \leq \epsilon_{P}$, we only need to have This implies the second part of Theorem 2, and concludes the proof. \

### Proof of Theorem 1

Next, we turn to the case of Lipschitz loss function. We rely on the following lemma.

### Lemma 3

Let $\phi:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ be an $L$-Lipschitz function. Then, for any $\alpha$ s.t. ${|\alpha|} > L$ we have that ${\phi^{\ast}{(\alpha)}} = \infty$.

Proof Fix some $\alpha > L$. By definition of the conjugate we have Similar argument holds for $\alpha < {- L}$. \A direct corollary of the above lemma is:

### Lemma 4

Suppose that for all $i$, $\phi_{i}$ is $L$-Lipschitz. Let $G^{(t)}$ be as defined in Lemma 1 (with $\gamma = 0$). Then, $G^{(t)} \leq {4L^{2}}$.

Proof Using Lemma 3 we know that ${|\alpha_{i}^{({t - 1})}|} \leq L$, and in addition by the relation of Lipschitz and sub-gradients we have ${|u_{i}^{({t - 1})}|} \leq L$. Thus, ${({u_{i}^{({t - 1})} - \alpha_{i}^{({t - 1})}})}^{2} \leq {4L^{2}}$, and the proof follows. \We are now ready to prove Theorem 1.

Proof \Proof of Theorem Let $G = {\max_{t}G^{(t)}}$ and note that by Lemma 4 we have $G \leq {4L^{2}}$. Lemma 1, with $\gamma = 0$, tells us that which implies that We next show that the above yields for all $t \geq t_{0} = {\max{(0,{\lceil{n{\log{({{2\lambdan\epsilon_{D}^{}}/G})}}}\rceil})}}$. Indeed, let us choose $s = 1$, then at $t = t_{0}$, we have This implies that holds at $t = t_{0}$. For $t > t_{0}$ we use an inductive argument. Suppose the claim holds for $t - 1$, therefore Choosing $s = {{2n}/{({{{{2n} - t_{0}} + t} - 1})}} \in {\lbrack 0,1\rbrack}$ yields This provides a bound on the dual sub-optimality. We next turn to bound the duality gap. Summing over $t = {{T_{0} + 1},\ldots,T}$ and rearranging terms we obtain that Now, if we choose $\overline{w},\overline{\alpha}$ to be either the average vectors or a randomly chosen vector over $t \in {\{{T_{0} + 1},\ldots,T\}}$, then the above implies If $T \geq {n + T_{0}}$ and $T_{0} \geq t_{0}$, we can set $s = {n/{({T - T_{0}})}}$ and combining with we obtain A sufficient condition for the above to be smaller than $\epsilon_{P}$ is that $T_{0} \geq {{\frac{4G}{\lambda\epsilon_{P}} - {2n}} + t_{0}}$ and $T \geq {T_{0} + \frac{G}{\lambda\epsilon_{P}}}$. It also implies that ${\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{(T_{0})})}}}\rbrack}} \leq {\epsilon_{P}/2}$. Since we also need $T_{0} \geq t_{0}$ and ${T - T_{0}} \geq n$, the overall number of required iterations can be We conclude the proof by noticing that $\epsilon_{D}^{} \leq 1$ using Lemma 2, which implies that $t_{0} \leq {\max{(0,{\lceil{n{\log{({{2\lambdan}/G})}}}\rceil})}}$. \

### Proof of Theorem 3

We assume that $(\phi_{t},x_{t})$ are randomly drawn from a distribution $D$, and define the population optimizer By definition, we have ${P{(w^{\ast})}} \leq {P{(w_{D}^{\ast})}}$ for any specific realization of $\{{(\phi_{t},x_{t})}:{t = {1,\ldots,n}}\}$. Therefore where the expectation is with respect to the choice of examples, and note that both $P{(\cdot)}$ and $w^{\ast}$ are sample dependent.

After each step $t$, we let $\alpha^{(t)} = {\lbrack\alpha_{1},\ldots,\alpha_{t}\rbrack}$, and let ${- u} \in {\partial{\phi_{t + 1}{({x_{t + 1}^{\top}w^{(t)}})}}}$. We have, for all $t$, The inequality above can be obtained by noticing that the choice of $- \alpha_{t + 1}^{({t + 1})}$ maximizes the dual objective. In the derivation of the equalities we have used basic algebra as well as the equation ${{- {\phi_{t + 1}^{\ast}{({- u})}}} - {x_{t + 1}^{\top}w^{(t)}u}} = {\phi_{t + 1}{({x_{t + 1}^{\top}w^{(t)}})}}$ which follows from ${- u} \in {\partial{\phi_{t + 1}{({x_{t + 1}^{\top}w^{(t)}})}}}$. Next we note that ${\|{{\lambdaw^{(t)}} - {ux_{t + 1}}}\|} \leq {2L}$ (where we used the triangle inequality, the definition of $w^{(t)}$, and Lemma 3). Therefore, Taking expectation *with respect to the choice of the examples*, and note that the $({t + 1})$'th example does not depend on $w^{(t)}$ we obtain that Using Lemma 2 we know that ${D_{t}{(\alpha^{(t)})}} \geq 0$ for all $t$. Therefore, by summing the above over $t$ we obtain that

### Proof of Theorem 4

The proof is identical to the proof of Theorem 1. We just need to notice that at the end of the first stage, we have ${{\mathbb{E}}\epsilon_{D}^{}} \leq {{2L^{2}{\log{({en})}}}/{({\lambdan})}}$. It implies that $t_{0} \leq {\max{(0,{\lceil{n{\log{({{{{2\lambdan} \cdot 2}L^{2}{\log{({en})}}}/{({\lambdanG})}})}}}\rceil})}}$.

### Proof of Proposition 1

Consider any feasible dual variable $\alpha$ and the corresponding $w = {w{(\alpha)}}$. Since Since ${w^{\ast \top}x_{i}} \in {\partial{\phi_{i}^{\ast}{({- \alpha_{i}^{\ast}})}}}$, we have By combining the previous two displayed inequalities, we obtain the first desired bound.

Next, we let $u = {w^{\ast \top}x_{i}}$, $v = {w^{\top}x_{i}}$. Since ${- a_{i}} \in {\partial{\phi_{i}{(v)}}}$ and ${- \alpha_{i}^{\ast}} \in {\partial{\phi_{i}{(u)}}}$, it follows that $u \in {\partial{\phi_{i}^{\ast}{({- \alpha_{i}^{\ast}})}}}$ and $v \in {\partial{\phi_{i}^{\ast}{({- a_{i}})}}}$. Therefore This implies the second bound.

### Proof of Theorem 5

The following lemma is very similar to Lemma 1 with nearly identical proof, but it focuses only on the convergence of dual objective function using.

### Lemma 5

Assume that is valid. Then for any iteration $t$ and any $s \in {\lbrack 0,1\rbrack}$ we have Proof Since only the $i$'th element of $\alpha$ is updated, the improvement in the dual objective can be written as By the definition of the update we have for all $s \in {\lbrack 0,1\rbrack}$ that We can now apply the Jensen's inequality to obtain By summing over $i = {1,\ldots,n}$, we obtain where the equality follows from ${\sum_{i = 1}^{n}{{({\alpha_{i}^{\ast} - \alpha_{i}^{({t - 1})}})}x_{i}}} = {\lambdan{({w^{\ast} - w^{({t - 1})}})}}$. By rearranging the terms on the right hand side using ${{({w^{\ast} - w^{({t - 1})}})}^{\top}w^{({t - 1})}} = {{{\| w^{\ast}\|}^{2}/2} - {{\| w^{({t - 1})}\|}^{2}/2} - {{\|{w^{\ast} - w^{({t - 1})}}\|}^{2}/2}}$, we obtain We can now apply to obtain This implies the desired result. \

### Lemma 6

Suppose that for all $i$, $\phi_{i}$ is $L$-Lipschitz. Let $G_{\ast}^{(t)}$ be as defined in Lemma 5. Then Proof Similarly to the proof of Lemma 4, we know that ${({\alpha_{i}^{\ast} - \alpha_{i}^{({t - 1})}})}^{2} \leq {4L^{2}}$. Moreover, ${\| x_{i}\|}^{2} \leq 1$, and ${{\| x_{i}\|}^{2} - \frac{\gamma_{i}\lambdan}{s}} \leq 0$ when $\gamma_{i} \geq {s/{({\lambdan})}}$. Therefore there are no more than $N{({s/{({\lambdan})}})}$ data points $i$ such that ${\| x_{i}\|}^{2} - \frac{\gamma_{i}\lambdan}{s}$ is positive. The desired result follows from these facts. \Proof \Proof of Theorem Let $\epsilon_{D}^{(t)} = {\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{(t)})}}}\rbrack}}$, and ${G_{\ast}{(s)}} = {{4L^{2}N{({{s/\lambda}n})}}/n}$. We obtain from Lemma 5 and Lemma 6 that It follows that for all $t > 0$ we have It follows that when we have $\epsilon_{D}^{(t)} \leq \epsilon_{D}$. \

### Proof of Theorem 6

Let $\epsilon_{D}^{(t)} = {\mathbb{E}{\lbrack{{D{(\alpha^{\ast})}} - {D{(\alpha^{(t)})}}}\rbrack}}$. From Proposition 1, we know that for all $t \geq T_{0}$: where ${- u_{i}^{({t - 1})}} \in {\partial{\phi_{i}{({x_{i}^{\top}w^{(t)}})}}}$. It follows that given any $\gamma > 0$, we have where Lemma 4 is used for the last inequality. Since $\gamma$ is arbitrary and $\epsilon_{D}^{(t)} \leq \epsilon_{D}$, it follows that Now plug into Lemma 1, we obtain for all $t \geq {T_{0} + 1}$: By taking $s = {n/T_{0}}$, and summing over ${t = {{T_{0} + 1},\ldots}},{{2T_{0}} = T}$, we obtain This proves the desired bound.

## Experimental Results

In this section we demonstrate the tightness of our theory. All our experiments are performed with the smooth variant of the hinge-loss defined , where the value of $\gamma$ is taken from the set $\{ 0,0.01,0.1,1\}$. Note that for $\gamma = 0$ we obtain the vanilla non-smooth hinge-loss.

In the experiments, we use $\epsilon_{D}$ to denote the dual sub-optimality, and $\epsilon_{P}$ to denote the primal sub-optimality (note that this is different than the notation in our analysis which uses $\epsilon_{P}$ to denote the duality gap). It follows that $\epsilon_{D} + \epsilon_{P}$ is the duality gap.

### Data

The experiments were performed on three large datasets with very different feature counts and sparsity, which were kindly provided by Thorsten Joachims. The astro-ph dataset classifies abstracts of papers from the physics ArXiv according to whether they belong in the astro-physics section; CCAT is a classification task taken from the Reuters RCV1 collection; and cov1 is class 1 of the covertype dataset of Blackard, Jock & Dean. The following table provides details of the dataset characteristics.

Dataset Training Size Testing Size Features Sparsity

### Linear convergence for Smooth Hinge-loss

Our first experiments are with $\phi_{\gamma}$ where we set $\gamma = 1$. The goal of the experiment is to show that the convergence is indeed linear. We ran the SDCA algorithm for solving the regularized loss minimization problem with different values of regularization parameter $\lambda$. Figure 1 shows the results. Note that a logarithmic scale is used for the vertical axis. Therefore, a straight line corresponds to linear convergence. We indeed observe linear convergence for the duality gap.

### Convergence for non-smooth Hinge-loss

Next we experiment with the original hinge loss, which is $1$-Lipschitz but is not smooth. We again ran the SDCA algorithm for solving the regularized loss minimization problem with different values of regularization parameter $\lambda$. Figure 2 shows the results. As expected, the overall convergence rate is slower than the case of a smoothed hinge-loss. However, it is also apparent that for large values of $\lambda$ a linear convergence is still exhibited, as expected according to our refined analysis. The bounds plotted are based on Theorem 1, which are slower than what we observe, as expected from the refined analysis in Section 5.

### Effect of smoothness parameter

We next show the effect of the smoothness parameter. Figure 3 shows the effect of the smoothness parameter on the rate of convergence. As can be seen, the convergence becomes faster as the loss function becomes smoother. However, the difference is more dominant when $\lambda$ decreases.

Figure 4 shows the effect of the smoothness parameter on the zero-one test error. It is noticeable that even though the non-smooth hinge-loss is considered a tighter approximation of the zero-one error, in most cases, the smoothed hinge-loss actually provides a lower test error than the non-smooth hinge-loss. In any case, it is apparent that the smooth hinge-loss decreases the zero-one test error faster than the non-smooth hinge-loss.

### Cyclic vs. Stochastic vs. Random Permutation

In Figure 5 we compare choosing dual variables at random with repetitions (as done in SDCA) vs. choosing dual variables using a random permutation at each epoch (as done in SDCA-Perm) vs. choosing dual variables in a fixed cyclic order (that was chosen once at random). As can be seen, a cyclic order does not lead to linear convergence and yields actual convergence rate much slower than the other methods and even worse than our bound. As mentioned before, some of the earlier analyses such as can be applied both to stochastic and to cyclic dual coordinate ascent methods with similar results. This means that their analysis, which can be no better than the behavior of cyclic dual coordinate ascent, is inferior to our analysis. Finally, we also observe that SDCA-Perm is sometimes faster than SDCA.

### Comparison to SGD

We next compare SDCA to Stochastic Gradient Descent (SGD). In particular, we implemented SGD with the update rule $w^{({t + 1})} = {{{({1 - {1/t}})}w^{(t)}} - {\frac{1}{\lambdat}\phi_{i}'{({w^{{(t)}\top}x_{i}})}x_{i}}}$, where $i$ is chosen uniformly at random and $\phi_{i}'$ denotes a sub-gradient of $\phi_{i}$. One clear advantage of SDCA is the availability of a clear stopping condition (by calculating the duality gap). In Figure 6 and Figure 7 we present the primal sub-optimality of SDCA, SDCA-Perm, and SGD. As can be seen, SDCA converges faster than SGD in most regimes. SGD can be better if both $\lambda$ is high and one performs a very small number of epochs. This is in line with our theory of Section 4. However, SDCA quickly catches up.

Figure 1: Experiments with the smoothed hinge-loss (γ = 1). The primal and dual sub-optimality, the duality gap, and our bound are depicted as a function of the number of epochs, on the astro-ph (left), CCAT (center) and cov1 (right) datasets. In all plots the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data).

Figure 2: Experiments with the hinge-loss (non-smooth). The primal and dual sub-optimality, the duality gap, and our bound are depicted as a function of the number of epochs, on the astro-ph (left), CCAT (center) and cov1 (right) datasets. In all plots the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data).

Figure 3: Duality gap as a function of the number of rounds for different values of γ.

Figure 4: Comparing the test zero-one error of SDCA for smoothed hinge-loss (γ = 1) and non-smooth hinge-loss (γ = 0). In all plots the vertical axis is the zero-one error on the test set and the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data). We terminated each method when the duality gap was smaller than 10−5.

Figure 5: Comparing the duality gap achieved by choosing dual variables at random with repetitions (SDCA), choosing dual variables at random without repetitions (SDCA-Perm), or using a fixed cyclic order. In all cases, the duality gap is depicted as a function of the number of epochs for different values of λ. The loss function is the smooth hinge loss with γ = 1.

Figure 6: Comparing the primal sub-optimality of SDCA and SGD for the smoothed hinge-loss (γ = 1). In all plots the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data).

Figure 7: Comparing the primal sub-optimality of SDCA and SGD for the non-smooth hinge-loss (γ = 0). In all plots the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data).

In Figure 8 we compare the zero-one test error of SDCA, when working with the smooth hinge-loss ($\gamma = 1$) to the zero-one test error of SGD, when working with the non-smooth hinge-loss. As can be seen, SDCA with the smooth hinge-loss achieves the smallest zero-one test error faster than SGD.

Figure 8: Comparing the test error of SDCA with the smoothed hinge-loss (γ = 1) to the test error of SGD with the non-smoothed hinge-loss. In all plots the vertical axis is the zero-one error on the test set and the horizontal axis is the number of iterations divided by training set size (corresponding to the number of epochs through the data). We terminated SDCA when the duality gap was smaller than 10−5.
