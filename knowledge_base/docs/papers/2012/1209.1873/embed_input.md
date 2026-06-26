<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Dual Coordinate Ascent Methods for Regularized Loss Minimization

Topics include Stochastic dual coordinate ascent, Variance reduction, Empirical risk minimization, Convex optimization, Coordinate ascent, Support vector machine, Regularized loss minimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Reanalyzes stochastic dual coordinate ascent for regularized empirical-risk objectives and establishes strong convergence guarantees comparable to or better than stochastic gradient descent. The paper helped make SDCA a canonical variance-reduced finite-sum method, especially for linear supervised-learning problems with convex losses and explicit regularization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic Gradient Descent (SGD) has become popular for solving large scale supervised machine learning optimization problems such as SVM, due to their strong theoretical guarantees. While the closely related Dual Coordinate Ascent (DCA) method has been implemented in various software packages, it has so far lacked good convergence analysis. This paper presents a new analysis of Stochastic Dual Coordinate Ascent (SDCA) showing that this class of methods enjoy strong theoretical guarantees that are comparable or better than SGD. This analysis justifies the effectiveness of SDCA for practical applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the following generic optimization problem associated with regularized loss minimization of linear predictors: Let $x_{1},\ldots,x_{n}$ be vectors in ${\mathbb{R}}^{d}$, let $\phi_{1},\ldots,\phi_{n}$ be a sequence of scalar convex functions, and let $\lambda > 0$ be a regularization parameter. Our goal is to solve ${\min_{w \in {\mathbb{R}}^{d}}P}{(w)}$ where^11^1Throughout this paper, we only consider the $\ell_{2}$-norm.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $w^{\ast}$ be the optimum of. We say that a solution $w$ is $\epsilon_{P}$-sub-optimal if ${{P{(w)}} - {P{(w^{\ast})}}} \leq \epsilon_{P}$. We analyze the runtime of optimization procedures as a function of the time required to find an $\epsilon_{P}$-sub-optimal solution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A simple approach for solving SVM is stochastic gradient descent (SGD). SGD finds an $\epsilon_{P}$-sub-optimal solution in time $\overset{\sim}{O}{({1/{({\lambda\epsilon_{P}})}})}$. This runtime does not depend on $n$ and therefore is favorable when $n$ is very large. However, the SGD approach has several disadvantages. It does not have a clear stopping criterion; it tends to be too aggressive at the beginning of the optimization process, especially when $\lambda$ is very small; while SGD reaches a moderate accuracy quite fast, its convergence becomes rather slow when we are interested in more accurate solutions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative approach is dual coordinate ascent (DCA), which solves a *dual* problem of. Specifically, for each $i$ let $\phi_{i}^{\ast}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ be the convex conjugate of $\phi_{i}$, namely, ${\phi_{i}^{\ast}{(u)}} = {\max_{z}{({{zu} - {\phi_{i}{(z)}}})}}$. The dual problem is The dual objective in has a different dual variable associated with each example in the training set. At each iteration of DCA, the dual objective is optimized with respect to a single dual variable, while the rest of the dual variables are kept in tact. then it is known that ${w{(\alpha^{\ast})}} = w^{\ast}$, where $\alpha^{\ast}$ is an optimal solution of.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is also known that ${P{(w^{\ast})}} = {D{(\alpha^{\ast})}}$ which immediately implies that for all $w$ and $\alpha$, we have ${P{(w)}} \geq {D{(\alpha)}}$, and hence the duality gap defined as can be regarded as an upper bound of the primal sub-optimality ${P{({w{(\alpha)}})}} - {P{(w^{\ast})}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on a *stochastic* version of DCA, abbreviated by SDCA, in which at each round we choose which dual coordinate to optimize uniformly at random. The purpose of this paper is to develop theoretical understanding of the convergence of the duality gap for SDCA.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We analyze SDCA either for $L$-Lipschitz loss functions or for $({1/\gamma})$-smooth loss functions, which are defined as follows. Throughout the paper, we will use $\phi'{(a)}$ to denote a sub-gradient of a convex function $\phi{( \cdot )}$, and use $\partial{\phi{(a)}}$ to denote its sub-differential.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Basic Results", "weight": 1.0} -->

The generic algorithm we analyze is described below. In the pseudo-code, the parameter $T$ indicates the number of iterations while the parameter $T_{0}$ can be chosen to be a number between $1$ to $T$. Based on our analysis, a good choice of $T_{0}$ is to be $T/2$. In practice, however, the parameters $T$ and $T_{0}$ are not required as one can evaluate the duality gap and terminate when it is sufficiently small.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Remark 1", "weight": 1.0} -->

If we choose the average version, we may simply take $T = {2T_{0}}$. Moreover, we note that Theorem 1 holds for both averaging or for choosing $w$ at random from $\{{T_{0} + 1},\ldots,T\}$. This means that calculating the duality gap at few random points would lead to the same type of guarantee with high probability. This approach has the advantage over averaging, since it is easier to implement the stopping condition (we simply check the duality gap at some random stopping points. This is in contrast to averaging in which we need to know $T,T_{0}$ in advance).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The above theorem applies to the hinge-loss function, ${\phi_{i}{(u)}} = {\max{\{ 0,{1 - {y_{i}a}}\}}}$. However, for the hinge-loss, the constant $4$ in the first inequality can be replaced by $1$ (this is because the domain of the dual variables is positive, hence the constant $4$ in Lemma 4 can be replaced by $1$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 3", "weight": 1.0} -->

If we choose $T = {2T_{0}}$, and assume that $T_{0} \geq {n + {1/{({\lambda\gamma})}}}$, then the second part of Theorem 2 implies a requirement of which is slightly weaker than the first part of Theorem 2 when $\epsilon_{P}$ is relatively large.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 4", "weight": 1.0} -->

analyzed the runtime of SGD and other algorithms from the perspective of the time required to achieve a certain level of error on the test set. To perform such analysis, we also need to take into account the *estimation error*, namely, the additional error we suffer due to the fact that the training examples defining the regularized loss minimization problem are only a finite sample from the underlying distribution. The estimation error of the primal objective behaves like $\Theta\left( \frac{1}{\lambdan} \right)$ (see ). Therefore, an interesting regime is when $\frac{1}{\lambdan} = {\Theta{(\epsilon)}}$. In that case, the bound for both Lipschitz and smooth functions would be $\overset{\sim}{O}{(n)}$. However, this bound on the estimation error is for the worst-case distribution over examples.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Therefore, another interesting regime is when we would like $\epsilon \ll \frac{1}{\lambdan}$, but still $\frac{1}{\lambdan} = {O{}}$ (following the practical observation that $\lambda = {\Theta{({1/n})}}$ often performs well). In that case, smooth functions still yield the bound $\overset{\sim}{O}{(n)}$, but the dominating term for Lipschitz functions will be $\frac{1}{\lambda\epsilon}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The runtime of SGD is $\overset{\sim}{O}{(\frac{1}{\lambda\epsilon})}$. This can be better than SDCA if $n \gg \frac{1}{\lambda\epsilon}$. However, in that case, SGD in fact only looks at $n' = {\overset{\sim}{O}{(\frac{1}{\lambda\epsilon})}}$ examples, so we can run SDCA on these $n'$ examples and obtain basically the same rate. For smooth functions, SGD can be much worse than SDCA if $\epsilon \ll \frac{1}{\lambdan}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Using SGD at the first epoch", "weight": 1.0} -->

From the convergence analysis, SDCA may not perform as well as SGD for the first few epochs (each epoch means one pass over the data). The main reason is that SGD takes a larger step size than SDCA earlier, which helps its performance. It is thus natural to combine SGD and SDCA, where the first epoch is performed using a modified stochastic gradient descent rule. We show that the expected dual sub-optimality at the end of the first epoch is $\overset{\sim}{O}{({1/{({\lambdan})}})}$. This result can be combined with SDCA to obtain a faster convergence when $\lambda \gg {\log{n/n}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Using SGD at the first epoch", "weight": 1.0} -->

We first introduce convenient notation. Let $P_{t}$ denote the primal objective for the first $t$ examples in the training set, The corresponding dual objective is Note that $P_{n}{(w)}$ is the primal objective given in and that $D_{n}{(\alpha)}$ is the dual objective given.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Using SGD at the first epoch", "weight": 1.0} -->

The following algorithm is a modification of SGD. The idea is to greedily decrease the dual sub-optimality for problem $D_{t}{( \cdot )}$ at each step $t$. This is different from DCA which works with $D_{n}{( \cdot )}$ at each step $t$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 6", "weight": 1.0} -->

When $\lambda$ is relatively large, the convergence rate in Theorem 3 for modified-SGD is better than what we can prove for SDCA. This is because Modified-SGD employs a larger step size at each step $t$ for $D_{t}{(\alpha)}$ than the corresponding step size in SDCA for $D{(\alpha)}$. However, the proof requires us to assume that $(\phi_{i},x_{i})$ are randomly drawn from a certain distribution, while this extra randomness assumption is not needed for the convergence of SDCA.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Procedure SDCA with SGD Initialization Stage 1: call Procedure Modified-SGD and obtain $\alpha$ Stage 2: call Procedure SDCA with parameter $\alpha^{} = \alpha$

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 7", "weight": 1.0} -->

For Lipschitz loss, ideally we would like to have a computational complexity of $O{({n + {L^{2}/{({\lambda\epsilon_{P}})}}})}$. Theorem 4 shows that SDCA with SGD at first epoch can achieve no worst than $O{({{n{\log{({\log n})}}} + {L^{2}/{({\lambda\epsilon_{P}})}}})}$, which is very close to the ideal bound. The result is better than that of vanilla SDCA in Theorem 1 when $\lambda$ is relatively large, which shows a complexity of $O{({{n{\log{(n)}}} + {L^{2}/{({\lambda\epsilon_{P}})}}})}$. The difference is caused by small step-sizes in the vanilla SDCA, and its negative effect can be observed in practice. That is, the vanilla SDCA tends to have a slower convergence rate than SGD in the first few iterations when $\lambda$ is relatively large.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 8", "weight": 1.0} -->

Similar to Remark 2, for the hinge-loss, the constant $4$ in Theorem 4 can be reduced to 1, and the constant $20$ can be reduced to $5$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Refined Analysis for Almost Smooth Loss", "weight": 1.0} -->

Our analysis shows that for smooth loss, SDCA converges faster than SGD (linear versus sub-linear convergence). For non-smooth loss, the analysis does not show any advantage of SDCA over SGD. This does not explain the practical observation that SDCA converges faster than SGD asymptotically even for SVM. This section tries to refine the analysis for Lipschitz loss and shows potential advantage of SDCA over SGD asymptotically. Note that the refined analysis of this section relies on quantities that depend on the underlying data distribution, and thus the results are more complicated than those presented earlier. Although precise interpretations of these results will be complex, we will discuss them qualitatively after the theorem statements, and use them to explain the advantage of SDCA over SGD for non-smooth losses.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Refined Analysis for Almost Smooth Loss", "weight": 1.0} -->

Although we note that for SVM, Luo and Tseng's analysis shows linear convergence of the form ${({1 - \nu})}^{k}$ for dual sub-optimality after $k$ passes over the data, as we mentioned, $\nu$ is proportional to the smallest nonzero eigenvalue of the data Gram matrix $X^{\top}X$, and hence can be arbitrarily bad when two data points $x_{i} \neq x_{j}$ becomes very close to each other. Our analysis uses a completely different argument that avoids this dependency on the data Gram matrix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Refined Analysis for Almost Smooth Loss", "weight": 1.0} -->

The main intuition behind our analysis is that many non-smooth loss functions are nearly smooth everywhere. For example, the hinge loss $\max{(0,{1 - {uy_{i}}})}$ is smooth at any point $u$ such that $uy_{i}$ is not close to $1$. Since a smooth loss has a strongly convex dual (and the strong convexity of the dual is directly used in our proof to obtain fast rate for smooth loss), the refined analysis in this section relies on the following refined dual strong convexity condition that holds for nearly everywhere smooth loss functions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 9", "weight": 1.0} -->

The following result shows fast convergence of duality gap using Theorem 5.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Examples", "weight": 1.0} -->

We will specify the SDCA algorithms for a few common loss functions. For simplicity, we only specify the algorithms without SGD initialization. In practice, instead of complete randomization, we may also run in epochs, and each epoch employs a random permutation of the data. We call this variant SDCA-Perm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Lipschitz loss", "weight": 1.0} -->

For the hinge loss, step (\*) in Procedure SDCA-Perm has a closed form solution as For absolute deviation loss, step (\*) in Procedure SDCA-Perm has a closed form solution as Both hinge loss and absolute deviation loss are $1$-Lipschitz. Therefore, we expect a convergence behavior of no worse than without SGD initialization based on Theorem 1. The refined analysis in Section 5 suggests a rate that can be significantly better, and this is confirmed with our empirical experiments.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Smooth loss", "weight": 1.0} -->

For squared loss, step (\*) in Procedure SDCA-Perm has a closed form solution as For log loss, step (\*) in Procedure SDCA-Perm does not have a closed form solution. However, one may start with the approximate solution, and further use several steps of Newton's update to get a more accurate solution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Smooth loss", "weight": 1.0} -->

Finally, we present a smooth variant of the hinge-loss, as defined below. Recall that the hinge loss function (for positive labels) is ${\phi{(u)}} = {\max{\{ 0,{1 - u}\}}}$ and we have ${\phi^{\ast}{({- a})}} = {- a}$ with $a \in {\lbrack 0,1\rbrack}$. Consider adding to $\phi^{\ast}$ the term $\frac{\gamma}{2}a^{2}$ which yields the $\gamma$-strongly convex function Then, its conjugate, which is defined below, is $({1/\gamma})$-smooth. We refer to it as the *smoothed hinge-loss* (for positive labels): For the smoothed hinge loss, step (\*) in Procedure SDCA-Perm has a closed form solution as Both log loss and squared loss are $1$-smooth. The smoothed-hinge loss is $1/\gamma$ smooth.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Smooth loss", "weight": 1.0} -->

Therefore we expect a convergence behavior of no worse than This is confirmed in our empirical experiments.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Proofs", "weight": 1.0} -->

We denote by $\partial{\phi_{i}{(a)}}$ the set of sub-gradients of $\phi_{i}$ at $a$. We use the notation $\phi_{i}'{(a)}$ to denote some sub-gradient of $\phi_{i}$ at $a$. For convenience, we list the following simple facts about primal and dual formulations, which will used in the proofs. For each $i$, we have The proof of our basic results stated in Theorem 2 and Theorem 1 relies on the fact that for SDCA, it is possible to lower bound the expected increase in dual objective by the duality gap. This key observation is stated in Lemma 1. Note that the duality gap can be further lower bounded using dual suboptimality. Therefore Lemma 1 implies a recursion for dual suboptimality which can be solved to obtain the convergence of dual objective. We can then apply Lemma 1 again, and the convergence of dual objective implies an upper bound of the duality gap, which leads to the basic theorems.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Proofs", "weight": 1.0} -->

The more refined results in Section 4 and Section 5 use similar strategies but with Lemma 1 replaced by its variants.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section we demonstrate the tightness of our theory. All our experiments are performed with the smooth variant of the hinge-loss defined, where the value of $\gamma$ is taken from the set $\{ 0,0.01,0.1,1\}$. Note that for $\gamma = 0$ we obtain the vanilla non-smooth hinge-loss.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In the experiments, we use $\epsilon_{D}$ to denote the dual sub-optimality, and $\epsilon_{P}$ to denote the primal sub-optimality (note that this is different than the notation in our analysis which uses $\epsilon_{P}$ to denote the duality gap). It follows that $\epsilon_{D} + \epsilon_{P}$ is the duality gap.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data", "weight": 1.0} -->

The experiments were performed on three large datasets with very different feature counts and sparsity, which were kindly provided by Thorsten Joachims. The astro-ph dataset classifies abstracts of papers from the physics ArXiv according to whether they belong in the astro-physics section; CCAT is a classification task taken from the Reuters RCV1 collection; and cov1 is class 1 of the covertype dataset of Blackard, Jock & Dean. The following table provides details of the dataset characteristics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data", "weight": 1.0} -->

Dataset Training Size Testing Size Features Sparsity

<!-- chunk {"id": "body-0040", "role": "body", "section": "Linear convergence for Smooth Hinge-loss", "weight": 1.0} -->

Our first experiments are with $\phi_{\gamma}$ where we set $\gamma = 1$. The goal of the experiment is to show that the convergence is indeed linear. We ran the SDCA algorithm for solving the regularized loss minimization problem with different values of regularization parameter $\lambda$. Figure 1 shows the results. Note that a logarithmic scale is used for the vertical axis. Therefore, a straight line corresponds to linear convergence. We indeed observe linear convergence for the duality gap.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convergence for non-smooth Hinge-loss", "weight": 1.0} -->

Next we experiment with the original hinge loss, which is $1$-Lipschitz but is not smooth. We again ran the SDCA algorithm for solving the regularized loss minimization problem with different values of regularization parameter $\lambda$. Figure 2 shows the results. As expected, the overall convergence rate is slower than the case of a smoothed hinge-loss. However, it is also apparent that for large values of $\lambda$ a linear convergence is still exhibited, as expected according to our refined analysis. The bounds plotted are based on Theorem 1, which are slower than what we observe, as expected from the refined analysis in Section 5.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Effect of smoothness parameter", "weight": 1.0} -->

We next show the effect of the smoothness parameter. Figure 3 shows the effect of the smoothness parameter on the rate of convergence. As can be seen, the convergence becomes faster as the loss function becomes smoother. However, the difference is more dominant when $\lambda$ decreases.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Cyclic vs. Stochastic vs. Random Permutation", "weight": 1.0} -->

In Figure 5 we compare choosing dual variables at random with repetitions (as done in SDCA) vs. choosing dual variables using a random permutation at each epoch (as done in SDCA-Perm) vs. choosing dual variables in a fixed cyclic order (that was chosen once at random). As can be seen, a cyclic order does not lead to linear convergence and yields actual convergence rate much slower than the other methods and even worse than our bound. As mentioned before, some of the earlier analyses such as can be applied both to stochastic and to cyclic dual coordinate ascent methods with similar results. This means that their analysis, which can be no better than the behavior of cyclic dual coordinate ascent, is inferior to our analysis. Finally, we also observe that SDCA-Perm is sometimes faster than SDCA.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison to SGD", "weight": 1.0} -->

We next compare SDCA to Stochastic Gradient Descent (SGD). In particular, we implemented SGD with the update rule $w^{({t + 1})} = {{{({1 - {1/t}})}w^{(t)}} - {\frac{1}{\lambdat}\phi_{i}'{({w^{{(t)}\top}x_{i}})}x_{i}}}$, where $i$ is chosen uniformly at random and $\phi_{i}'$ denotes a sub-gradient of $\phi_{i}$. One clear advantage of SDCA is the availability of a clear stopping condition (by calculating the duality gap). In Figure 6 and Figure 7 we present the primal sub-optimality of SDCA, SDCA-Perm, and SGD. As can be seen, SDCA converges faster than SGD in most regimes. SGD can be better if both $\lambda$ is high and one performs a very small number of epochs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison to SGD", "weight": 1.0} -->

This is in line with our theory of Section 4. However, SDCA quickly catches up.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison to SGD", "weight": 1.0} -->

In Figure 8 we compare the zero-one test error of SDCA, when working with the smooth hinge-loss ($\gamma = 1$) to the zero-one test error of SGD, when working with the non-smooth hinge-loss. As can be seen, SDCA with the smooth hinge-loss achieves the smallest zero-one test error faster than SGD.
