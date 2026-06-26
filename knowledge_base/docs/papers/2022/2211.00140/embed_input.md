<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Damped Newton Method Achieves Global O(1/k^2) and Local Quadratic Convergence Rate

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present the first stepsize schedule for Newton method resulting in fast global and local convergence guarantees. In particular, a) we prove an O( frac 1 k^ ) global rate, which matches the state-of-the-art global rate of cubically regularized Newton method of Polyak and Nesterov and of regularized Newton method of Mishchenko and Doikov and Nesterov, b) we prove a local quadratic rate, which matches the best-known local rate of second-order methods, and c) our stepsize formula is simple, explicit, and does not require solving any subproblem. Our convergence proofs hold under affine-invariance assumptions closely related to the notion of self-concordance. Finally, our method has competitive performance when compared to existing baselines, which share the same fast global convergence guarantees.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second-order optimization methods are the backbone of much of industrial and scientific computing. With origins that can be tracked back several centuries to the pioneering works of Newton (Newton, 1687), Raphson (Raphson, 1697) and Simpson (Simpson, 1740), they were extensively studied, generalized, modified, and improved in the last century. For a review of the historical development of the classical Newton-Raphson method, we refer the reader to the work of Ypma. The number of extensions and applications of second-order optimization methods is enormous; for example, the survey of Conn et al. on trust-region and quasi-Newton methods cited over a thousand papers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Second-order methods and modern machine learning", "weight": 1.0} -->

Despite the rich history of the field, research on second-order methods has been flourishing up to this day. Some of the most recent development in the area was motivated by the needs of modern machine learning. Data-oriented machine learning depends on large datasets (both in number of features and number of datapoints), which are often stored in distributed/decentalized fashion. Consequently, there is a need for scalable algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Second-order methods and modern machine learning", "weight": 1.0} -->

To tackle large number of features, Qu et al.; Gower et al.; Doikov and Richtárik and Hanzely et al. proposed variants of Newton method operating in random low-dimensional subspaces. On the other hand, Pilanci and Wainwright; Xu et al. and Kovalev et al. developed subsampled Newton methods for solving empirical risk minimization (ERM) problems with large training datasets. Additionally, Bordes et al.; Mokhtari and Ribeiro; Gower et al.; Byrd et al. and Kovalev et al. proposed stochastic variants of quasi-Newton methods. To tackle non-centralized nature of datasets, Shamir et al.; Reddi et al.; Wang et al. and Crane and Roosta considered distributed variants of Newton method, with improvements under various data/function similarity assumptions. Islamov et al.; Safaryan et al.; Qian et al.; Islamov et al. and Agafonov et al. developed communication-efficient distributed variants of Newton method using the idea of communication compression and error compensation, without the need for any similarity assumptions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Second-order methods and modern machine learning", "weight": 1.0} -->

We highlight two main research directions throughout of history of second-order methods: globally convergent methods under additional second-order smoothness (4 and Local Quadratic Convergence Rate")) and local methods for self-concordant problems (12 and Local Quadratic Convergence Rate")). Former approach lead to various improvements such as acceleration Nesterov; Monteiro and Svaiter, usage of inexact information Ghadimi et al.; Agafonov et al., generalization to tensor methods and their acceleration Nesterov; Gasnikov et al.; Kovalev and Gasnikov, superfast second-order methods under higher smoothness Nesterov; Kamzolov and Gasnikov. Latter approach was a breakthrough in 1990s, it lead to interior-point methods. Summary of the results can be found in books Nesterov and Nemirovski, Nesterov. This direction is still popular up to this day Dvurechensky and Nesterov; Hildebrand; Doikov and Nesterov; Nesterov.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Second-order methods and modern machine learning", "weight": 1.0} -->

As easy-to-scale alternative to second-order methods, first-order algorithms attracted a lot of attention. Many of their aspects have been explored, including strong results in variance reduction (Roux et al.,Gower et al., Johnson and Zhang; Nguyen et al. ), preconditioning Jahani et al., acceleration (Nesterov, d'Aspremont et al. ) distributed/federated computation (Konečný et al.; Chen et al.; Berahas et al.; Takáč et al.; Richtárik and Takáč, Kairouz et al. ), and decentralized computation. However, the convergence of first-order methods always depends on the conditioning of the underlying problem. Improving conditioning is fundamentally impossible without using higher-order information. Removing this conditioning dependence is possible by incorporating information about the Hessian. This results in second-order methods. Their most compelling advantage is that they can converge extremely quickly, usually in just a few iterations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Newton method: benefits and limitations", "weight": 1.0} -->

One of the most famous algorithms in optimization, Newton method, takes iterates of form Its iterates satisfy the recursion $\left\| {{\nabla f}{(x_{k + 1})}} \right\|_{2} \leq {c\left\| {{\nabla f}{(x_{k})}} \right\|_{2}^{2}}$ (for a constant $c > 0$), which means that Newton method converges locally quadratically. However, convergence of Newton method is limited to only to the neighborhood of the solution. It is well-known that when initialized far from optimum, Newton can diverge, both in theory and practice (Jarre and Toint, Mascarenhas). We can explain intuition why this happens. Update rule of Newton (1 and Local Quadratic Convergence Rate")) was chosen to minimize right hand side of Taylor approximation The main problem is that Taylor approximation is not an upper bound, and therefore, global convergence of Newton method is not guaranteed.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Towards a fast globally convergent Newton method", "weight": 1.0} -->

Even though second-order algorithms with superlinear local convergence rates are very common, global convergence guarantees of any form are surprisingly rare. Many papers proposed globalization strategies, essentially all of them require some combination of the following: line-search, trust regions, damping/truncation, regularization. Some popular globalization strategies show non-increase of functional value during the training. However, this turned out to be insufficient for convergence to the optimum. Jarre and Toint, Mascarenhas designed simple functions (strictly convex with compact level sets) so that Newton method with Armijo stepsizes does not converge to the optimum. To this day, virtually all known global convergence guarantees are for regularized Newton methods, which can be written as where $\lambda_{k} \geq 0$. Parameter $\lambda_{k}$ is also known as Levenberg-Marquardt regularization, which was first introduced for a nonlinear least-squares objective. For simplicity, we disregard differences in the objectives for the literature comparison. Motivation behind update (3 and Local Quadratic Convergence Rate")) is to replace Taylor approximation in (2 and Local Quadratic Convergence Rate")) by an upper bound.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Towards a fast globally convergent Newton method", "weight": 1.0} -->

The first method with proven global convergence rate $\mathcal{O}\left(k^{- 2} \right)$ is Cubic Newton method for function $f$ with Lipschitz-continuous Hessian, Under this condition, one can upper bound of Taylor approximation eq. 2 and Local Quadratic Convergence Rate") as Next iterate of Cubic Newton can be written as a minimizer of right hand side of (5 and Local Quadratic Convergence Rate"))^11^1Where $\mathbb{E}$ a $d$-dimensional Euclidean space, defined in Section 2.3 and Local Quadratic Convergence Rate").

<!-- chunk {"id": "body-0011", "role": "body", "section": "Towards a fast globally convergent Newton method", "weight": 1.0} -->

For our newly-proposed algorithm AICN (Algorithm 1 and Local Quadratic Convergence Rate")), we are using almost identical step1 and Local Quadratic Convergence Rate") ^22^2Function $f$ is $L_{\text{semi}}$-semi-strongly self-concordant (Definition 3 and Local Quadratic Convergence Rate")). Instead of $L_{\text{semi}}$, we will use its upper bound $L_{\text{est}}$, $L_{\text{est}} \geq L_{\text{semi}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Towards a fast globally convergent Newton method", "weight": 1.0} -->

The difference between the update of Cubic Newton and AICN is that we measure the cubic regularization term in the local Hessian norms. This seemingly negligible perturbation turned out to be of a great significance for two reasons a) model in (7 and Local Quadratic Convergence Rate")) is affine-invariant, b) surprisingly, the next iterate of (7 and Local Quadratic Convergence Rate")) lies in the direction of Newton method step and is obtainable without regularizer $\lambda_{k}$ (AICN just needs to set stepsize $\alpha_{k}$). We elaborate on both of these points later in the paper.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Towards a fast globally convergent Newton method", "weight": 1.0} -->

Cubic Newton method (6 and Local Quadratic Convergence Rate")) can be equivalently expressed in form (3 and Local Quadratic Convergence Rate")) with $\alpha_{k} = 1$ and $\lambda_{k} = {L_{2}\left\| {x_{k} - x_{k + 1}} \right\|_{2}}$. However, since such $\lambda_{k}$ depends on $x_{k + 1}$, resulting algorithm requires additional subroutine for solving its subproblem each iteration. Next work showing convergence rate of regularized Newton method avoided implicit steps by choosing $\lambda_{k} \propto \left\| {{\nabla f}{(x_{k})}} \right\|_{2}$. However, this came with a trade-off for slower convergence rate, $\mathcal{O}\left( k^{- {1/4}} \right)$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Towards a fast globally convergent Newton method", "weight": 1.0} -->

Finally, Mishchenko (see also the work of Doikov and Nesterov ) improved upon both of these works by using explicit regularization $\alpha_{k} = 1$, $\lambda_{k} \propto \sqrt{L_{2}\left\| {{\nabla f}{(x_{k})}} \right\|_{2}}$, and proving global rate $\mathcal{O}\left( k^{- 2} \right)$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

In this work, we investigate global convergence for most basic globalization strategy, stepsized Newton method without any regularizer ($\lambda_{k} = 0$). This algorithm is also referred as damped (or truncated) Newton method; it can be written as Resulting algorithm was investigated in detail as an interior-point method.

<!-- chunk {"id": "body-0016", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

f}{(x_{k})}} \right\rangle$ is defined in Section 2.3 and Local Quadratic Convergence Rate").

<!-- chunk {"id": "body-0017", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

Firstly, all of them depends on gradient computed in the dual norm and scaled by a smoothness constant ($G_{1}$ or $G$). Secondly, all of these stepsizes converge to $1$ from below (for $\hat{\alpha} \in {\{\alpha_{1},\alpha_{2},\alpha\}}$ holds $0 < \hat{\alpha} \leq 1$ and ${\lim_{x\rightarrow x_{\ast}}\hat{\alpha}} = 1$). Our algorithm uses stepsize bigger by orders of magnitude (see Figure 3 and Local Quadratic Convergence Rate") in Appendix A and Local Quadratic Convergence Rate") for detailed comparison). The main difference between already established stepsizes $\alpha_{1},\alpha_{2}$ and our stepsize $\alpha$ are resulting global convergence rates.

<!-- chunk {"id": "body-0018", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

While stepsize $\alpha_{2}$ does not lead to a global convergence rate, and $\alpha_{1}$ leads to rate $\mathcal{O}\left(k^{- {1/2}} \right)$, our stepsize $\alpha$ leads to a significantly faster, $\mathcal{O}\left(k^{- 2} \right)$ rate. Our rate matches best known global rates for regularized Newton methods. We manage to achieve these results by carefully choosing assumptions. While rates for $\alpha_{1}$ and $\alpha_{2}$ follows from standard self-concordance, our assumptions are a consequence of a slightly stronger version of self-concordance. We will discuss this difference in detail later.

<!-- chunk {"id": "body-0019", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

We summarize important properties of regularized Newton methods with fast global convergence guarantees and damped Newton methods in Table 1 and Local Quadratic Convergence Rate").

<!-- chunk {"id": "body-0020", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

Affine invariant? (alg., ass., rate) Avoids line search? Global convergence rate Local convergence exponent Nesterov and Nemirovski $\mathcal{O}\left(k^{- \frac{1}{2}} \right)$ Nesterov and Polyak, Griewank, Doikov and Nesterov Locally Reg. Newton Globally Reg. Newton $\frac{\mu + \left\| {{\nabla f}\left(x_{k} \right)} \right\|_{2}}{L_{1}}$ $\mathcal{O}\left(k^{- \frac{1}{4}} \right)$ Globally Reg. Newton $\sqrt{L_{2}\left\| {{\nabla f}\left(x_{k} \right)} \right\|_{2}}$ Mishchenko Doikov and Nesterov AIC Newton (Algorithm 1) In triplets, we report whether algorithm, used assumptions, convergence rate are affine-invariant, respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "AICN as a damped Newton method", "weight": 1.0} -->

For a Lyapunov function Φk and a constant c, we report exponent β of Φ (xk + 1) ≤ c Φ (xk)β. f has L1-Lipschitz continuous gradient.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

To summarize novelty in our work, we present a novel algorithm AICN. Our algorithm can be interpreted in two viewpoints a) as a regularized Newton method (version of Cubic Newton method), b) as a damped Newton method. AICN enjoys the best properties of these two worlds: Fast global convergence: AICN converges globally with rate $\mathcal{O}\left(k^{- 2} \right)$ (Theorem 2 and Local Quadratic Convergence Rate"), 4. ‣ Appendix C Global Convergence with weaker assumptions on Self-Concordance ‣ Appendix ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate")), which matches state-of-the-art global rate for all regularized Newton methods. Furthermore, it is the first such rate for Damped Newton method.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Fast local convergence: In addition to the fast global rate, AICN decreases gradient norms locally in quadratic rate (Theorem 3. ‣ 4.2 Local convergence ‣ 4 Convergence Results ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate")). This result matches the best-known rates for both regularized Newton algorithms and damped Newton algorithms.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Simplicity: Previous works on Newton regularizations can be viewed as a popular global-convergence fix for the Newton method. We propose an even simpler fix in the form of a stepsize schedule (Section 3 and Local Quadratic Convergence Rate")).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Implementability: Step of AICN depends on a smoothness constant $L_{\text{semi}}$ (Definition 3 and Local Quadratic Convergence Rate")). Given this constant, next iterate of AICN can be computed directly.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

This is improvement over Cubic Newton, which for a given constant $L_{2}$ needs to run line-search subroutine each iteration to solve its subproblem.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Improvement: Avoiding latter subroutine yields theoretical improvements. If we compute matrix inverses naively, iteration cost of AICN is $\mathcal{O}{(d^{3})}$ (where $d$ is a dimension of the problem), which is improvement over $\mathcal{O}{({d^{3}{\log\varepsilon^{- 1}}})}$ iteration cost of Cubic Newton.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Practical performance: We show that in practice, AICN outperforms all algorithms sharing same convergence guarantees: Cubic Newton and Globally Regularized Newton and Doikov and Nesterov, and fixed stepsize Damped Newton method (Section 5 and Local Quadratic Convergence Rate")).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Geometric properties: We analyze AICN under more geometrically natural assumptions. Instead of smoothness, we use a version of self-concordance (Section 3.1 and Local Quadratic Convergence Rate")), which is invariant to affine transformations and hence also to a choice of a basis. AICN preserves affine-invariance obtained from assumptions throughout the convergence. In contrast, Cubic Newton uses base-dependent $l_{2}$ norm and hence depends on a choice of a basis. This represents an extra layer of complexity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

Alternative analysis: We also provide alternative analysis under weaker assumptions (Appendix C and Local Quadratic Convergence Rate")).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Summary of contributions", "weight": 1.0} -->

The rest of the paper is structured as follows. In Section 2.3 and Local Quadratic Convergence Rate") we introduce our notation. In Section 3 and Local Quadratic Convergence Rate"), we discuss algorithm AICN, affine-invariant properties and self-concordance. In Sections 4.1 and Local Quadratic Convergence Rate") and 4.2 and Local Quadratic Convergence Rate") we show global and local convergence guarantees, respectively. In Section 5 and Local Quadratic Convergence Rate") we present an empirical comparison of AICN with other algorithms sharing fast global convergence.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Minimization problem & notation", "weight": 1.0} -->

In the paper, we consider a $d$-dimensional Euclidean space $\mathbb{E}$. Its dual space, ${\mathbb{E}}^{\ast}$, is composed of all linear functionals on $\mathbb{E}$. For a functional $g \in {\mathbb{E}}^{\ast}$, we denote by $\left\langle g,x \right\rangle$ its value at $x \in {\mathbb{E}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "New Algorithm: Affine-Invariant Cubic Newton", "weight": 1.0} -->

Finally, we are ready to present algorithm AICN. It is damped Newton method with updates as summarized in Algorithm 1 and Local Quadratic Convergence Rate"). Stepsize satisfy $\alpha_{k} \leq 1$ (from AG inequality, (45. ‣ B.4 Technical lemmas ‣ Appendix B Proofs of Results Appearing in the Paper ‣ Appendix ‣ A Damped Newton Method Achieves Global 𝒪⁢(1/𝑘²) and Local Quadratic Convergence Rate"))). Also ${\lim_{x_{k}\rightarrow x_{\ast}}\alpha_{k}} = 1$, hence (11 and Local Quadratic Convergence Rate")) converges to Newton method. Next, we are going to discuss geometric properties of our algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "New Algorithm: Affine-Invariant Cubic Newton", "weight": 1.0} -->

1:Requires: Initial point x0 ∈ 𝔼, constant Lest s.t. Lest ≥ Lsemi > 0 4: xk + 1 = xk − αk [∇2f (xk)]−1 ∇f (xk) ⊳ Note that $x_{k + 1}\overset{}{=}{S_{f,L_{\text{est}}}{(x_{k})}}$. Algorithm 1 AICN: Affine-Invariant Cubic Newton

<!-- chunk {"id": "body-0035", "role": "body", "section": "Geometric properties: affine invariance", "weight": 1.0} -->

One of the main geometric properties of the Newton method is affine invariance, invariance to affine transformations of variables. Let $\mathbf{A}:{{\mathbb{E}}\rightarrow{\mathbb{E}}^{\ast}}$ be a non-degenerate linear transformation. Consider function ${\phi{(y)}} = {f{({\mathbf{A}y})}}$. By affine transformation, we denote ${{f{(x)}}\rightarrow{\phi{(y)}} = {f{({\mathbf{A}y})}}},{x\rightarrow{\mathbf{A}^{- 1}y}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Significance of norms", "weight": 1.0} -->

Note that local Hessian norm ${\| h\|}_{{\nabla f}{(x)}}$ is affine-invariant because where $h = {\mathbf{A}z}$. On the other hand, induced norm ${\| h\|}_{\mathbf{I}}$ is not affine-invariant because With respect to geometry, the most natural norm is local Hessian norm, ${\| h\|}_{{\nabla f}{(x)}}$. From affine invariance follows that for this norm, the level sets $\left\{ {y \in {\mathbb{E}}} \middle| {{\|{y - x}\|}_{x}^{2} \leq c} \right\}$ are balls centered around $x$ (all directions have the same scaling). In comparison, scaling of the $l_{2}$ norm is dependent on eigenvalues of the Hessian. In terms of convergence, one direction in $l_{2}$ can significantly dominate others and slow down an algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Significance for algorithms", "weight": 1.0} -->

Algorithms that are not affine-invariant can suffer from chosen coordinate system. This is the case for Cubic Newton, as its model (4 and Local Quadratic Convergence Rate")) is bound to base-dependent $l_{2}$ norm. Same is true for any other method regularized with an induced norm ${\| h\|}_{\mathbf{I}}$. On the other hand, (damped) Newton methods have affine-invariant models, and hence as algorithms independent of the chosen coordinate system. We prove this claim in following lemma (note: $\alpha_{k} = 1$ and $\alpha_{k}$ from (11 and Local Quadratic Convergence Rate")) are affine-invariant).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Significance in assumptions: self-concordance", "weight": 1.0} -->

We showed that damped Newton methods preserve affine-invariance through iterations. Hence it is more fitting to analyze them under affine-invariant assumptions. Affine-invariant version of smoothness, *self-concordance*, was introduced in Nesterov and Nemirovski.

<!-- chunk {"id": "body-0039", "role": "body", "section": "From assumptions to algorithm", "weight": 1.0} -->

From semi-strong self-concordance we can get a second-order bounds on the function and model.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Global convergence", "weight": 1.0} -->

Next, we focus on global convergence guarantees.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 1 (Bounded level sets)", "weight": 1.0} -->

Our analysis proceeds as follows. Firstly, we show that one step of the algorithm decreases function value, and secondly, we use the technique from to show that multiple steps lead to $\mathcal{O}\left( k^{- 2} \right)$ global convergence. We start with following lemma.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Local convergence", "weight": 1.0} -->

For local quadratic convergence are going to utilise following lemmas.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we evaluate proposed AICN (Algorithm 1 and Local Quadratic Convergence Rate")) algorithm on the logistic regression task and second-order lower bound function. We compare it with regularized Newton methods sharing fast global convergence guarantees: Cubic Newton method, and Globally Regularized Newton method with $L_{2}$-constant. Because AICN has a form of a damped Newton method, we also compare it with Damped Newton with fixed (tuned) stepsize $\alpha_{k} = \alpha$. We report decrease in function value $f{(x_{k})}$, function value suboptimality ${f{(x_{k})}} - {f{(x_{\ast})}}$ with respect to iteration and time. The methods are implemented as PyTorch optimizers. The code is available at

<!-- chunk {"id": "body-0044", "role": "body", "section": "Logistic regression", "weight": 1.0} -->

In Figure 1 and Local Quadratic Convergence Rate"), we consider task of classification images on dataset *a9a*. Number of features for every data sample is $d = 123$, $m = 20000$. We take staring point $x_{0}\overset{\text{def}}{=}{10{\lbrack 1,1,\ldots,1\rbrack}^{\top}}$ and $\mu = 10^{- 3}$. Our choice is differ from $x_{0} = 0$ (equal to all zeroes) to show globalisation properties of methods ($x_{0} = 0$ is very close to the solution, as Newton method converges in 4 iterations). Parameters of all methods are fine-tuned, we choose parameters $L_{\text{est}},L_{2},\alpha$ (of AICN, Cubic Newton, Damped Newton, resp.) to largest values having monotone decrease in reported metrics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Logistic regression", "weight": 1.0} -->

Fine-tuned values are $L_{\text{est}} = 0.97$ $L_{2} = 0.000215$, $\alpha = 0.285$. Figure 1 and Local Quadratic Convergence Rate") demonstrates that AICN converges slightly faster than Cubic Newton method by iteration, notably faster than Globally Regularized Newton and significantly faster than Damped Newton. AICN outperforms every method by time.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Second-order lower bound function", "weight": 1.0} -->

For second part we solve the following minimization problem: This function is a lower bound for a class of functions with Lipschitz continuous Hessian (4 and Local Quadratic Convergence Rate")) with additional regularization. In Figure 2 and Local Quadratic Convergence Rate"), we take $d = 20$, $x_{0} = 0$ (equal to all zeroes). Parameters $L_{\text{est}},L_{2},\alpha$ are fine-tuned to largest values having monotone decrease in reported metrics: $L_{\text{est}} = 662$ $L_{2} = 0.662$, $\alpha = 0.0172$. Figure 2 and Local Quadratic Convergence Rate") demonstrates that AICN converges slightly slower than Cubic Newton method, slightly faster than Globally Regularized Newton, and significantly faster than Damped Newton. ain outperforms every method by time. More experiments are presented in Appendix A and Local Quadratic Convergence Rate").

<!-- chunk {"id": "body-0047", "role": "body", "section": "Second-order lower bound function", "weight": 1.0} -->

Note, that the iteration of the Cubic Newton method needs an additional line-search, so one iteration of Cubic Newton is computationally harder than one iteration of AICN. More experiments are presented in Appendix A and Local Quadratic Convergence Rate").
