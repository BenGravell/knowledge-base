### Introduction

Second-order optimization methods are the backbone of much of industrial and scientific computing. With origins that can be tracked back several centuries to the pioneering works of Newton (Newton, 1687), Raphson (Raphson, 1697) and Simpson (Simpson, 1740), they were extensively studied, generalized, modified, and improved in the last century. For a review of the historical development of the classical Newton-Raphson method, we refer the reader to the work of Ypma. The number of extensions and applications of second-order optimization methods is enormous; for example, the survey of Conn et al. on trust-region and quasi-Newton methods cited over a thousand papers.

### Second-order methods and modern machine learning

Despite the rich history of the field, research on second-order methods has been flourishing up to this day. Some of the most recent development in the area was motivated by the needs of modern machine learning. Data-oriented machine learning depends on large datasets (both in number of features and number of datapoints), which are often stored in distributed/decentalized fashion. Consequently, there is a need for scalable algorithms.

To tackle large number of features, Qu et al.; Gower et al.; Doikov and Richtárik and Hanzely et al. proposed variants of Newton method operating in random low-dimensional subspaces. On the other hand, Pilanci and Wainwright; Xu et al. and Kovalev et al. developed subsampled Newton methods for solving empirical risk minimization (ERM) problems with large training datasets. Additionally, Bordes et al.; Mokhtari and Ribeiro; Gower et al.; Byrd et al. and Kovalev et al. proposed stochastic variants of quasi-Newton methods. To tackle non-centralized nature of datasets, Shamir et al.; Reddi et al.; Wang et al. and Crane and Roosta considered distributed variants of Newton method, with improvements under various data/function similarity assumptions. Islamov et al.; Safaryan et al.; Qian et al.; Islamov et al. and Agafonov et al. developed communication-efficient distributed variants of Newton method using the idea of communication compression and error compensation, without the need for any similarity assumptions.

We highlight two main research directions throughout of history of second-order methods: globally convergent methods under additional second-order smoothness (4 and Local Quadratic Convergence Rate")) and local methods for self-concordant problems (12 and Local Quadratic Convergence Rate")). Former approach lead to various improvements such as acceleration Nesterov; Monteiro and Svaiter, usage of inexact information Ghadimi et al.; Agafonov et al., generalization to tensor methods and their acceleration Nesterov; Gasnikov et al.; Kovalev and Gasnikov, superfast second-order methods under higher smoothness Nesterov; Kamzolov and Gasnikov. Latter approach was a breakthrough in 1990s, it lead to interior-point methods. Summary of the results can be found in books Nesterov and Nemirovski, Nesterov. This direction is still popular up to this day Dvurechensky and Nesterov; Hildebrand; Doikov and Nesterov; Nesterov.

As easy-to-scale alternative to second-order methods, first-order algorithms attracted a lot of attention. Many of their aspects have been explored, including strong results in variance reduction (Roux et al.,Gower et al., Johnson and Zhang; Nguyen et al. ), preconditioning Jahani et al., acceleration (Nesterov, d'Aspremont et al. ) distributed/federated computation (Konečný et al.; Chen et al.; Berahas et al.; Takáč et al.; Richtárik and Takáč, Kairouz et al. ), and decentralized computation. However, the convergence of first-order methods always depends on the conditioning of the underlying problem. Improving conditioning is fundamentally impossible without using higher-order information. Removing this conditioning dependence is possible by incorporating information about the Hessian. This results in second-order methods. Their most compelling advantage is that they can converge extremely quickly, usually in just a few iterations.

### Newton method: benefits and limitations

One of the most famous algorithms in optimization, Newton method, takes iterates of form Its iterates satisfy the recursion $\left\| {{\nabla f}{(x_{k + 1})}} \right\|_{2} \leq {c\left\| {{\nabla f}{(x_{k})}} \right\|_{2}^{2}}$ (for a constant $c > 0$), which means that Newton method converges locally quadratically. However, convergence of Newton method is limited to only to the neighborhood of the solution. It is well-known that when initialized far from optimum, Newton can diverge, both in theory and practice (Jarre and Toint, Mascarenhas). We can explain intuition why this happens. Update rule of Newton (1 and Local Quadratic Convergence Rate")) was chosen to minimize right hand side of Taylor approximation The main problem is that Taylor approximation is not an upper bound, and therefore, global convergence of Newton method is not guaranteed.

### Towards a fast globally convergent Newton method

Even though second-order algorithms with superlinear local convergence rates are very common, global convergence guarantees of any form are surprisingly rare. Many papers proposed globalization strategies, essentially all of them require some combination of the following: line-search, trust regions, damping/truncation, regularization. Some popular globalization strategies show non-increase of functional value during the training. However, this turned out to be insufficient for convergence to the optimum. Jarre and Toint, Mascarenhas designed simple functions (strictly convex with compact level sets) so that Newton method with Armijo stepsizes does not converge to the optimum. To this day, virtually all known global convergence guarantees are for regularized Newton methods, which can be written as where $\lambda_{k} \geq 0$. Parameter $\lambda_{k}$ is also known as Levenberg-Marquardt regularization, which was first introduced for a nonlinear least-squares objective. For simplicity, we disregard differences in the objectives for the literature comparison. Motivation behind update (3 and Local Quadratic Convergence Rate")) is to replace Taylor approximation in (2 and Local Quadratic Convergence Rate")) by an upper bound. The first method with proven global convergence rate $\mathcal{O}\left(k^{- 2} \right)$ is Cubic Newton method for function $f$ with Lipschitz-continuous Hessian, Under this condition, one can upper bound of Taylor approximation eq. 2 and Local Quadratic Convergence Rate") as Next iterate of Cubic Newton can be written as a minimizer of right hand side of (5 and Local Quadratic Convergence Rate"))^11^1Where $\mathbb{E}$ a $d$-dimensional Euclidean space, defined in Section 2.3 and Local Quadratic Convergence Rate").

For our newly-proposed algorithm AICN (Algorithm 1 and Local Quadratic Convergence Rate")), we are using almost identical step1 and Local Quadratic Convergence Rate") ^22^2Function $f$ is $L_{\text{semi}}$-semi-strongly self-concordant (Definition 3 and Local Quadratic Convergence Rate")). Instead of $L_{\text{semi}}$, we will use its upper bound $L_{\text{est}}$, $L_{\text{est}} \geq L_{\text{semi}}$.

The difference between the update of Cubic Newton and AICN is that we measure the cubic regularization term in the local Hessian norms. This seemingly negligible perturbation turned out to be of a great significance for two reasons a) model in (7 and Local Quadratic Convergence Rate")) is affine-invariant, b) surprisingly, the next iterate of (7 and Local Quadratic Convergence Rate")) lies in the direction of Newton method step and is obtainable without regularizer $\lambda_{k}$ (AICN just needs to set stepsize $\alpha_{k}$). We elaborate on both of these points later in the paper.

Cubic Newton method (6 and Local Quadratic Convergence Rate")) can be equivalently expressed in form (3 and Local Quadratic Convergence Rate")) with $\alpha_{k} = 1$ and $\lambda_{k} = {L_{2}\left\| {x_{k} - x_{k + 1}} \right\|_{2}}$. However, since such $\lambda_{k}$ depends on $x_{k + 1}$, resulting algorithm requires additional subroutine for solving its subproblem each iteration. Next work showing convergence rate of regularized Newton method avoided implicit steps by choosing $\lambda_{k} \propto \left\| {{\nabla f}{(x_{k})}} \right\|_{2}$. However, this came with a trade-off for slower convergence rate, $\mathcal{O}\left( k^{- {1/4}} \right)$. Finally, Mishchenko (see also the work of Doikov and Nesterov ) improved upon both of these works by using explicit regularization $\alpha_{k} = 1$, $\lambda_{k} \propto \sqrt{L_{2}\left\| {{\nabla f}{(x_{k})}} \right\|_{2}}$, and proving global rate $\mathcal{O}\left( k^{- 2} \right)$.

### Contributions

### AICN as a damped Newton method

In this work, we investigate global convergence for most basic globalization strategy, stepsized Newton method without any regularizer ($\lambda_{k} = 0$). This algorithm is also referred as damped (or truncated) Newton method; it can be written as Resulting algorithm was investigated in detail as an interior-point method. Nesterov shows quadratic local convergence for stepsizes ${\alpha_{1}\overset{\text{def}}{=}\frac{1}{1 + G_{1}}},{\alpha_{2}\overset{\text{def}}{=}\frac{1 + G_{1}}{1 + G_{1} + G_{1}^{2}}}$, where^33^3Function $f$ is $L_{\text{sc}}$-self-concordant (Definition 1 and Local Quadratic Convergence Rate")).^44^4Dual norm $\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast} = \left\langle {{\nabla f}{(x_{k})}},{{\nabla^{2}f}{(x_{k})}^{- 1}{\nabla f}{(x_{k})}} \right\rangle$ is defined in Section 2.3 and Local Quadratic Convergence Rate"). $G_{1}\overset{\text{def}}{=}{L_{\text{sc}}\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast}}$. Our algorithm AICN is also damped Newton method with stepsize $\alpha = \frac{{- 1} + \sqrt{1 + {2G}}}{G}$, where2 and Local Quadratic Convergence Rate")4 and Local Quadratic Convergence Rate") $G\overset{\text{def}}{=}{L_{\text{semi}}\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast}}$. Mentioned stepsizes $\alpha_{1},\alpha_{2},\alpha$ share two characteristics. Firstly, all of them depends on gradient computed in the dual norm and scaled by a smoothness constant ($G_{1}$ or $G$). Secondly, all of these stepsizes converge to $1$ from below (for $\hat{\alpha} \in {\{\alpha_{1},\alpha_{2},\alpha\}}$ holds $0 < \hat{\alpha} \leq 1$ and ${\lim_{x\rightarrow x_{\ast}}\hat{\alpha}} = 1$). Our algorithm uses stepsize bigger by orders of magnitude (see Figure 3 and Local Quadratic Convergence Rate") in Appendix A and Local Quadratic Convergence Rate") for detailed comparison). The main difference between already established stepsizes $\alpha_{1},\alpha_{2}$ and our stepsize $\alpha$ are resulting global convergence rates. While stepsize $\alpha_{2}$ does not lead to a global convergence rate, and $\alpha_{1}$ leads to rate $\mathcal{O}\left(k^{- {1/2}} \right)$, our stepsize $\alpha$ leads to a significantly faster, $\mathcal{O}\left(k^{- 2} \right)$ rate. Our rate matches best known global rates for regularized Newton methods. We manage to achieve these results by carefully choosing assumptions. While rates for $\alpha_{1}$ and $\alpha_{2}$ follows from standard self-concordance, our assumptions are a consequence of a slightly stronger version of self-concordance. We will discuss this difference in detail later.

We summarize important properties of regularized Newton methods with fast global convergence guarantees and damped Newton methods in Table 1 and Local Quadratic Convergence Rate").

Affine invariant? (alg., ass., rate) Avoids line search? Global convergence rate Local convergence exponent Nesterov and Nemirovski $\mathcal{O}\left(k^{- \frac{1}{2}} \right)$ Nesterov and Polyak, Griewank, Doikov and Nesterov Locally Reg. Newton Globally Reg. Newton $\frac{\mu + \left\| {{\nabla f}\left(x_{k} \right)} \right\|_{2}}{L_{1}}$ $\mathcal{O}\left(k^{- \frac{1}{4}} \right)$ Globally Reg. Newton $\sqrt{L_{2}\left\| {{\nabla f}\left(x_{k} \right)} \right\|_{2}}$ Mishchenko Doikov and Nesterov AIC Newton (Algorithm 1) In triplets, we report whether algorithm, used assumptions, convergence rate are affine-invariant, respectively.

For a Lyapunov function Φk and a constant c, we report exponent β of Φ (xk + 1) ≤ c Φ (xk)β. f has L1-Lipschitz continuous gradient.

For simplicity, we denote $G_{1}\overset{\text{def}}{=}{L_{\text{sc}}\left\| {{\nabla f}\left( x_{k} \right)} \right\|_{x_{k}}^{\ast}}$ and $G\overset{\text{def}}{=}{L_{\text{semi}}\left\| {{\nabla f}\left( x_{k} \right)} \right\|_{x_{k}}^{\ast}}$ (for Lest ← Lsemi).

Table 1: A summary of regularized Newton methods with global convergence guarantees. We consider algorithms with updates of form xk + 1 = xk − αk (∇2f (xk) + λk I)−1 ∇f (xk). For simplicity of comparison, we disregard differences in objectives and assumptions. We assume L2-smoothness of Hessian, Lsemi-semi-strong self-concordance, convexity (Definition 3), μ-strong convexity locally and bounded level sets. For regularization parameter holds λk ≥ 0 and stepsize satisfy 0 < αk ≤ 1. We highlight the best know rates in blue.

### Summary of contributions

To summarize novelty in our work, we present a novel algorithm AICN. Our algorithm can be interpreted in two viewpoints a) as a regularized Newton method (version of Cubic Newton method), b) as a damped Newton method. AICN enjoys the best properties of these two worlds: Fast global convergence: AICN converges globally with rate $\mathcal{O}\left(k^{- 2} \right)$ (Theorem 2 and Local Quadratic Convergence Rate"), 4. ‣ Appendix C Global Convergence with weaker assumptions on Self-Concordance ‣ Appendix ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate")), which matches state-of-the-art global rate for all regularized Newton methods. Furthermore, it is the first such rate for Damped Newton method.

Fast local convergence: In addition to the fast global rate, AICN decreases gradient norms locally in quadratic rate (Theorem 3. ‣ 4.2 Local convergence ‣ 4 Convergence Results ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate")). This result matches the best-known rates for both regularized Newton algorithms and damped Newton algorithms.

Simplicity: Previous works on Newton regularizations can be viewed as a popular global-convergence fix for the Newton method. We propose an even simpler fix in the form of a stepsize schedule (Section 3 and Local Quadratic Convergence Rate")).

Implementability: Step of AICN depends on a smoothness constant $L_{\text{semi}}$ (Definition 3 and Local Quadratic Convergence Rate")). Given this constant, next iterate of AICN can be computed directly.

This is improvement over Cubic Newton, which for a given constant $L_{2}$ needs to run line-search subroutine each iteration to solve its subproblem.

Improvement: Avoiding latter subroutine yields theoretical improvements. If we compute matrix inverses naively, iteration cost of AICN is $\mathcal{O}{(d^{3})}$ (where $d$ is a dimension of the problem), which is improvement over $\mathcal{O}{({d^{3}{\log\varepsilon^{- 1}}})}$ iteration cost of Cubic Newton.

Practical performance: We show that in practice, AICN outperforms all algorithms sharing same convergence guarantees: Cubic Newton and Globally Regularized Newton and Doikov and Nesterov, and fixed stepsize Damped Newton method (Section 5 and Local Quadratic Convergence Rate")).

Geometric properties: We analyze AICN under more geometrically natural assumptions. Instead of smoothness, we use a version of self-concordance (Section 3.1 and Local Quadratic Convergence Rate")), which is invariant to affine transformations and hence also to a choice of a basis. AICN preserves affine-invariance obtained from assumptions throughout the convergence. In contrast, Cubic Newton uses base-dependent $l_{2}$ norm and hence depends on a choice of a basis. This represents an extra layer of complexity.

Alternative analysis: We also provide alternative analysis under weaker assumptions (Appendix C and Local Quadratic Convergence Rate")).

The rest of the paper is structured as follows. In Section 2.3 and Local Quadratic Convergence Rate") we introduce our notation. In Section 3 and Local Quadratic Convergence Rate"), we discuss algorithm AICN, affine-invariant properties and self-concordance. In Sections 4.1 and Local Quadratic Convergence Rate") and 4.2 and Local Quadratic Convergence Rate") we show global and local convergence guarantees, respectively. In Section 5 and Local Quadratic Convergence Rate") we present an empirical comparison of AICN with other algorithms sharing fast global convergence.

### Minimization problem & notation

In the paper, we consider a $d$-dimensional Euclidean space $\mathbb{E}$. Its dual space, ${\mathbb{E}}^{\ast}$, is composed of all linear functionals on $\mathbb{E}$. For a functional $g \in {\mathbb{E}}^{\ast}$, we denote by $\left\langle g,x \right\rangle$ its value at $x \in {\mathbb{E}}$.

We consider the following convex optimization problem: where ${f{(x)}} \in C^{2}$ is a convex function with continuous first and second derivatives and positive definite Hessian. We assume that the problem has a unique minimizer $x_{\ast} \in {{\operatorname{argmin}\limits_{x \in {\mathbb{E}}}f}{(x)}}$. Note, that ${{{{\nabla f}{(x)}} \in {\mathbb{E}}^{\ast}},{{{\nabla^{2}f}{(x)}h} \in {\mathbb{E}}^{\ast}}}.$ Now, we introduce different norms for spaces $\mathbb{E}$ and ${\mathbb{E}}^{\ast}$. Denote ${{x,h} \in {\mathbb{E}}},{g \in {\mathbb{E}}^{\ast}}$. For a self-adjoint positive-definite operator $\mathbf{H}:{{\mathbb{E}}\rightarrow{\mathbb{E}}^{\ast}}$, we can endow these spaces with conjugate Euclidean norms: For identity $\mathbf{H} = \mathbf{I}$, we get classical Eucledian norm ${\| x\|}_{\mathbf{I}} = \left\langle x,x \right\rangle^{1/2}$. For local Hessian norm $\mathbf{H} = {{\nabla^{2}f}{(x)}}$, we use shortened notation Operator norm is defined by for $\mathbf{H}:{{\mathbb{E}}\rightarrow{\mathbb{E}}^{\ast}}$ and a fixed $x \in {\mathbb{E}}$. If we consider a specific case ${\mathbb{E}}\leftarrow{\mathbb{R}}^{d}$, then $\mathbf{H}$ is a symmetric positive definite matrix.

### New Algorithm: Affine-Invariant Cubic Newton

Finally, we are ready to present algorithm AICN. It is damped Newton method with updates as summarized in Algorithm 1 and Local Quadratic Convergence Rate"). Stepsize satisfy $\alpha_{k} \leq 1$ (from AG inequality, (45. ‣ B.4 Technical lemmas ‣ Appendix B Proofs of Results Appearing in the Paper ‣ Appendix ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate"))). Also ${\lim_{x_{k}\rightarrow x_{\ast}}\alpha_{k}} = 1$, hence (11 and Local Quadratic Convergence Rate")) converges to Newton method. Next, we are going to discuss geometric properties of our algorithm.

1:Requires: Initial point x0 ∈ 𝔼, constant Lest s.t. Lest ≥ Lsemi > 0 4: xk + 1 = xk − αk [∇2f (xk)]−1 ∇f (xk) ⊳ Note that $x_{k + 1}\overset{}{=}{S_{f,L_{\text{est}}}{(x_{k})}}$. Algorithm 1 AICN: Affine-Invariant Cubic Newton

### Geometric properties: affine invariance

One of the main geometric properties of the Newton method is affine invariance, invariance to affine transformations of variables. Let $\mathbf{A}:{{\mathbb{E}}\rightarrow{\mathbb{E}}^{\ast}}$ be a non-degenerate linear transformation. Consider function ${\phi{(y)}} = {f{({\mathbf{A}y})}}$. By affine transformation, we denote ${{f{(x)}}\rightarrow{\phi{(y)}} = {f{({\mathbf{A}y})}}},{x\rightarrow{\mathbf{A}^{- 1}y}}$.

### Significance of norms

Note that local Hessian norm ${\| h\|}_{{\nabla f}{(x)}}$ is affine-invariant because where $h = {\mathbf{A}z}$. On the other hand, induced norm ${\| h\|}_{\mathbf{I}}$ is not affine-invariant because With respect to geometry, the most natural norm is local Hessian norm, ${\| h\|}_{{\nabla f}{(x)}}$. From affine invariance follows that for this norm, the level sets $\left\{ {y \in {\mathbb{E}}} \middle| {{\|{y - x}\|}_{x}^{2} \leq c} \right\}$ are balls centered around $x$ (all directions have the same scaling). In comparison, scaling of the $l_{2}$ norm is dependent on eigenvalues of the Hessian. In terms of convergence, one direction in $l_{2}$ can significantly dominate others and slow down an algorithm.

### Significance for algorithms

Algorithms that are not affine-invariant can suffer from chosen coordinate system. This is the case for Cubic Newton, as its model (4 and Local Quadratic Convergence Rate")) is bound to base-dependent $l_{2}$ norm. Same is true for any other method regularized with an induced norm ${\| h\|}_{\mathbf{I}}$. On the other hand, (damped) Newton methods have affine-invariant models, and hence as algorithms independent of the chosen coordinate system. We prove this claim in following lemma (note: $\alpha_{k} = 1$ and $\alpha_{k}$ from (11 and Local Quadratic Convergence Rate")) are affine-invariant).

### Lemma 1 (Lemma 5.1.1 Nesterov )

Let the sequence $\left\{ x_{k} \right\}$ be generated by a damped Newton method with affine-invariant stepsize $\alpha_{k}$, applied to the function $f$: ${x_{k + 1} = {x_{k} - {\alpha_{k}\left\lbrack {{\nabla^{2}f}{(x_{k})}} \right\rbrack^{- 1}{\nabla f}{(x_{k})}}}}.$ For function $\phi{(y)}$, damped Newton method generates $\left\{ y_{k} \right\}$: ${y_{k + 1} = {y_{k} - {\alpha_{k}\left\lbrack {{\nabla^{2}\phi}{(y_{k})}} \right\rbrack^{- 1}{\nabla\phi}{(y_{k})}}}},$ with $y_{0} = {\mathbf{A}^{- 1}x_{0}}$. Then $y_{k} = {\mathbf{A}^{- 1}x_{k}}$.

### Significance in assumptions: self-concordance

We showed that damped Newton methods preserve affine-invariance through iterations. Hence it is more fitting to analyze them under affine-invariant assumptions. Affine-invariant version of smoothness, *self-concordance*, was introduced in Nesterov and Nemirovski.

### Definition 1

Convex function $f \in C^{3}$ is called self-concordant if $${{{|{D^{3}f{(x)}{\lbrack h\rbrack}^{3}}|} \leq {{L_{\text{sc}}{\| h\|}_{x}^{3}},{\forall x}}},{h \in {\mathbb{E}}}},$$ where for any integer $p \geq 1$, by ${D^{p}f{(x)}{\lbrack h\rbrack}^{p}}\overset{\text{def}}{=}{D^{p}f{(x)}{\lbrack h,\ldots,h\rbrack}}$ we denote the $p$-th order directional derivative^55^5For example, ${D^{1}f{(x)}{\lbrack h\rbrack}} = {\langle{{\nabla f}{(x)}},h\rangle}$ and ${D^{2}f{(x)}{\lbrack h\rbrack}^{2}} = \left\langle {{\nabla^{2}f}{(x)}h},h \right\rangle$. of $f$ at $x \in {\mathbb{E}}$ along direction $h \in {\mathbb{E}}$.

Both sides of inequality are affine-invariant. This assumption corresponds to a big class of optimization methods called interior-point methods. Self-concordance implies uniqueness of the solution, as stated in following proposition.

### Proposition 1 (Theorem 5.1.16, Nesterov )

Let a self-concordant function $f$ be bounded below. Then it attains its minimum at a single point.

Rodomanov and Nesterov introduced stronger version of self-concordance assumption.

### Definition 2

Convex function $f \in C^{2}$ is called strongly self-concordant if $${{{{{\nabla^{2}f}{(y)}} - {{\nabla^{2}f}{(x)}}} \preceq {{L_{\text{str}}{\|{y - x}\|}_{z}{\nabla^{2}f}{(w)}},{\forall y},x,z}},{w \in {\mathbb{E}}}}.$$ For our analysis, we introduce definition for functions between self-concordant and strongly self-concordant.

### Definition 3

Convex function $f \in C^{2}$ is called semi-strongly self-concordant if $${{\left\| {{{\nabla^{2}f}{(y)}} - {{\nabla^{2}f}{(x)}}} \right\|_{op} \leq {{L_{\text{semi}}{\|{y - x}\|}_{x}},{\forall y}}},{x \in {\mathbb{E}}}}.$$ Note that all of the Definitions 1 and Local Quadratic Convergence Rate") - 3 and Local Quadratic Convergence Rate") are affine-invariant, their respective classes satisfy Also, for a fixed strongly self-concordant function $f$ and smallest such $L_{\text{sc}},L_{\text{semi}},L_{\text{str}}$ holds ${L_{\text{sc}} \leq L_{\text{semi}} \leq L_{\text{str}}}.$ These notions are related to the convexity and smoothness; strong concordance follows from function $L_{2}$-Lipschitz continuous Hessian and strong convexity.

### Proposition 2 (Example 4.1 from )

Let $\mathbf{H}:{{\mathbb{E}}\rightarrow{\mathbb{E}}^{\ast}}$ be a self-adjoint positive definite operator. Suppose there exist $\mu > 0$ and $L_{2} \geq 0$ such that the function $f$ is $\mu$-strongly convex and its Hessian is $L_{2}$-Lipschitz continuous (4 and Local Quadratic Convergence Rate")) with respect to the norm $\parallel \cdot \parallel_{\mathbf{H}}$. Then $f$ is strongly self-concordant with constant $L_{\text{str}} = \frac{L_{2}}{\mu^{3/2}}$.

### From assumptions to algorithm

From semi-strong self-concordance we can get a second-order bounds on the function and model.

### Lemma 2

If $f$ is semi-strongly self-concordant, then Consequently, we have upper bound for function value in form One can show that (16 and Local Quadratic Convergence Rate")) is not valid for just self-concordant functions. For example, there is no such upper bound for $- {\log{(x)}}$. Hence, the semi-strongly self-concordance is significant as an assumption.

We can define iterates of optimization algorithm to be minimizers of the right hand side of (16 and Local Quadratic Convergence Rate")), $${{S_{f,L_{\text{est}}}{(x)}}\overset{\text{def}}{=}{x + {\operatorname{argmin}\limits_{h \in {\mathbb{E}}}\left\{ {{f{(x)}} + \left\langle {{\nabla f}{(x)}},h \right\rangle + {\frac{1}{2}\left\langle {{\nabla^{2}f}{(x)}h},h \right\rangle} + {\frac{L_{\text{est}}}{6}{\| h\|}_{x}^{3}}} \right\}}}},$$ $${x_{k + 1} = {S_{f,L_{\text{est}}}{(x_{k})}}},$$ for an estimate constant $L_{\text{est}} \geq L_{\text{semi}}$. It turns out that subproblem (17 and Local Quadratic Convergence Rate")) is easy to solve. To get an explicit solution, we compute its gradient w.r.t. $h$. For solution $h^{\ast}$, it should be equal to zero, We get that step (18 and Local Quadratic Convergence Rate")) has the same direction as a Newton method and is scaled by ${\alpha_{k} = \left({{\frac{L_{\text{est}}}{2}{\| h^{\ast}\|}_{x}} + 1} \right)^{- 1}}.$ Now, we substitute $h^{\ast}$ from (20 and Local Quadratic Convergence Rate")) to (19 and Local Quadratic Convergence Rate")) We solve the quadratic equation (21 and Local Quadratic Convergence Rate")) for $\alpha_{k}$, and obtain explicit formula for stepsizes of AICN, as (11 and Local Quadratic Convergence Rate")). We formalize this connection in theorem, for further explanation see proof in Appendix B and Local Quadratic Convergence Rate").

### Theorem 1

For $L_{\text{est}} \geq L_{\text{semi}}$, update of AICN (11 and Local Quadratic Convergence Rate")), $${{x_{k + 1} = {{x_{k} - {\alpha_{k}{\nabla^{2}f}{(x_{k})}^{- 1}{\nabla f}{(x_{k})}}},\text{where}}}\qquad{\alpha_{k} = \frac{{- 1} + \sqrt{1 + {2L_{\text{est}}\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast}}}}{L_{\text{est}}\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast}}}},$$ is a minimizer of upper bound (17 and Local Quadratic Convergence Rate")), $x_{k + 1} = {S_{f,L_{\text{est}}}{(x_{k})}}$.

### Convergence Results

### Global convergence

Next, we focus on global convergence guarantees. We will utilize the following assumption:

### Assumption 1 (Bounded level sets)

The objective function $f$ has a unique minimizer $x_{\ast}$. Also, the diameter of the level set ${\mathcal{L}{(x_{0})}}\overset{\text{def}}{=}\left\{ {x \in {\mathbb{E}}}:{{f{(x)}} \leq {f{(x_{0})}}} \right\}$ is bounded by a constant $D_{2}$ as^66^6We state it in $l_{2}$ norm for easier verification. In proofs, we use its variant $D$ in Hessian norms, (23 and Local Quadratic Convergence Rate"))., ${\max\limits_{x \in {\mathcal{L}{(x_{0})}}}\left\| {x - x_{\ast}} \right\|_{2}} \leq D_{2} < {+ \infty}$.

Our analysis proceeds as follows. Firstly, we show that one step of the algorithm decreases function value, and secondly, we use the technique from to show that multiple steps lead to $\mathcal{O}\left( k^{- 2} \right)$ global convergence. We start with following lemma.

### Lemma 3 (One step globally)

Let function $f$ be $L_{\text{semi}}$-semi-strongly self-concordant, convex with positive-definite Hessian and $L_{\text{est}} \geq L_{\text{semi}}$. Then for any $x \in {\mathbb{E}}$, we have This lemma implies that step (17 and Local Quadratic Convergence Rate")) decreases function value (take $y\leftarrow x$). Using notation of 1. ‣ 4.1 Global convergence ‣ 4 Convergence Results ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate"), $x_{k} \in {\mathcal{L}{(x_{0})}}$ for any $k \geq 0$. Also, setting $y\leftarrow x$ and $x\leftarrow x_{\ast}$ in (14 and Local Quadratic Convergence Rate")) yields ${{\|{x - x_{\ast}}\|}_{x} \leq \left({{\|{x - x_{\ast}}\|}_{x_{\ast}}^{2} + {L_{\text{est}}{\|{x - x_{\ast}}\|}_{x_{\ast}}^{3}}} \right)^{\frac{1}{2}}}.$ We denote those distances $D$ and $R$, They are both affine-invariant and $R$ upper bounds $D$. While $R$ depends only on the level set $\mathcal{L}{(x_{0})}$, $D$ can be used to obtain more tight inequalities. We avoid using common distance $D_{2}$, as $l_{2}$ norm would ruin affine-invariant properties.

### Theorem 2

Let $f{(x)}$ be a $L_{\text{semi}}$-semi-strongly self-concordant convex function with positive-definite Hessian, constant $L_{\text{est}}$ satisfy $L_{\text{est}} \geq L_{\text{semi}}$ and 1. ‣ 4.1 Global convergence ‣ 4 Convergence Results ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate") holds. Then, after $k + 1$ iterations of Algorithm 1 and Local Quadratic Convergence Rate"), we have the following convergence rate: $${{{f{(x_{k + 1})}} - {f{(x_{\ast})}}} \leq {O\left(\frac{L_{\text{est}}D^{3}}{k^{2}} \right)} \leq {O\left(\frac{L_{\text{est}}R^{3}}{k^{2}} \right)}}.$$ Consequently, AICN converges globally with a fast rate $\mathcal{O}\left(k^{- 2} \right)$. We can now present local analysis.

### Local convergence

For local quadratic convergence are going to utilise following lemmas.

### Lemma 4

For convex $L_{\text{semi}}$-semi-strongly self-concordant function $f$ and for any $0 < c < 1$ in the neighborhood of solution Lemma 4 and Local Quadratic Convergence Rate") formalizes that a inverse hessians of a self-concordant function around the solution is non-degenerate. With this result, we can show one-step gradient norm decrease.

### Lemma 5 (One step decrease locally)

Let function $f$ be $L_{\text{semi}}$-semi-strongly self-concordant and $L_{\text{est}} \geq L_{\text{semi}}$. If $x_{k}$ such that (25 and Local Quadratic Convergence Rate")) holds, then for next iterate $x_{k + 1}$ of AICN holds Using Lemma 4 and Local Quadratic Convergence Rate"), we shift the gradient bound to respective norms, Gradient norm decreases $\left\| {{\nabla f}{(x_{k + 1})}} \right\|_{x_{k + 1}}^{\ast} \leq \left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast}$ for $\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast} \leq \frac{{({2 - c})}^{2} - 1}{2L_{\text{est}}}$.

As a result, neighbourhood of the local convergence is $\left\{ x:{\left\| {{\nabla f}{(x)}} \right\|_{x}^{\ast} \leq {\min\left\lbrack \frac{{({2 - c})}^{2} - 1}{2L_{\text{est}}};\frac{{({{2c} + 1})}^{2} - 1}{2L_{\text{est}}} \right\rbrack}} \right\}.$ Maximizing by $c$, we get $c = {1/3}$ and neighrbourhood $\left\{ x:{\left\| {{\nabla f}{(x)}} \right\|_{x}^{\ast} \leq \frac{8}{9L_{\text{est}}}} \right\}.$ One step of AICN decreases gradient norm quadratically, multiple steps leads to following decrease.

### Theorem 3 (Local convergence rate)

Let function $f$ be $L_{\text{semi}}$-semi-strongly self-concordant, $L_{\text{est}} \geq L_{\text{semi}}$ and starting point $x_{0}$ be in the neighborhood of the solution such that $\left\| {{\nabla f}{(x_{0})}} \right\|_{x_{0}}^{\ast} \leq \frac{8}{9L_{\text{est}}}$. For $k \geq 0$, we have quadratic decrease of the gradient norms, $\left\| {{\nabla f}{(x_{k})}} \right\|_{x_{k}}^{\ast}$ ${\leq {\left( {\frac{3}{2}L_{\text{est}}} \right)^{k}\left( \left\| {{\nabla f}{(x_{0})}} \right\|_{x_{0}}^{\ast} \right)^{2^{k}}}}.$

### Numerical Experiments

In this section, we evaluate proposed AICN (Algorithm 1 and Local Quadratic Convergence Rate")) algorithm on the logistic regression task and second-order lower bound function. We compare it with regularized Newton methods sharing fast global convergence guarantees: Cubic Newton method, and Globally Regularized Newton method with $L_{2}$-constant. Because AICN has a form of a damped Newton method, we also compare it with Damped Newton with fixed (tuned) stepsize $\alpha_{k} = \alpha$. We report decrease in function value $f{(x_{k})}$, function value suboptimality ${f{(x_{k})}} - {f{(x_{\ast})}}$ with respect to iteration and time. The methods are implemented as PyTorch optimizers. The code is available at

### Logistic regression

For first part, we solve the following empirical risk minimization problem: where ${\{{(a_{i},b_{i})}\}}_{i = 1}^{m}$ are given data samples described by features $a_{i}$ and class $b_{i} \in {\{{- 1},1\}}$.

In Figure 1 and Local Quadratic Convergence Rate"), we consider task of classification images on dataset *a9a*. Number of features for every data sample is $d = 123$, $m = 20000$. We take staring point $x_{0}\overset{\text{def}}{=}{10{\lbrack 1,1,\ldots,1\rbrack}^{\top}}$ and $\mu = 10^{- 3}$. Our choice is differ from $x_{0} = 0$ (equal to all zeroes) to show globalisation properties of methods ($x_{0} = 0$ is very close to the solution, as Newton method converges in 4 iterations). Parameters of all methods are fine-tuned, we choose parameters $L_{\text{est}},L_{2},\alpha$ (of AICN, Cubic Newton, Damped Newton, resp.) to largest values having monotone decrease in reported metrics. Fine-tuned values are $L_{\text{est}} = 0.97$ $L_{2} = 0.000215$, $\alpha = 0.285$. Figure 1 and Local Quadratic Convergence Rate") demonstrates that AICN converges slightly faster than Cubic Newton method by iteration, notably faster than Globally Regularized Newton and significantly faster than Damped Newton. AICN outperforms every method by time.

Figure 1: Comparison of regularized Newton methods and Damped Newton method for logistic regression task on a9a dataset.

Figure 2: Comparison of regularized Newton methods and Damped Newton method for second-order lower bound function.

### Second-order lower bound function

For second part we solve the following minimization problem: This function is a lower bound for a class of functions with Lipschitz continuous Hessian (4 and Local Quadratic Convergence Rate")) with additional regularization. In Figure 2 and Local Quadratic Convergence Rate"), we take $d = 20$, $x_{0} = 0$ (equal to all zeroes). Parameters $L_{\text{est}},L_{2},\alpha$ are fine-tuned to largest values having monotone decrease in reported metrics: $L_{\text{est}} = 662$ $L_{2} = 0.662$, $\alpha = 0.0172$. Figure 2 and Local Quadratic Convergence Rate") demonstrates that AICN converges slightly slower than Cubic Newton method, slightly faster than Globally Regularized Newton, and significantly faster than Damped Newton. ain outperforms every method by time. More experiments are presented in Appendix A and Local Quadratic Convergence Rate"). Note, that the iteration of the Cubic Newton method needs an additional line-search, so one iteration of Cubic Newton is computationally harder than one iteration of AICN. More experiments are presented in Appendix A and Local Quadratic Convergence Rate").
