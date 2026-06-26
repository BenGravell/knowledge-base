<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimum Volume Conformal Sets for Multivariate Regression

Topics include Conformal prediction, Multivariate regression, Prediction sets, Minimum-volume sets, Nonconformity scores, Norm balls, Distribution-free inference, Uncertainty quantification.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes an optimization-driven way to learn conformal prediction sets for multivariate regression while directly targeting small set volume. The method turns minimum-volume coverage into a learned nonconformity score over norm-ball prediction sets, making conformal multivariate uncertainty more adaptive than fixed-shape constructions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Conformal prediction provides a principled framework for constructing predictive sets with finite-sample validity. While much of the focus has been on univariate response variables, existing multivariate methods either impose rigid geometric assumptions or rely on flexible but computationally expensive approaches that do not explicitly optimize prediction set volume. We propose an optimization-driven framework based on a novel loss function that directly learns minimum-volume covering sets while ensuring valid coverage. This formulation naturally induces a new nonconformity score for conformal prediction, which adapts to the residual distribution and covariates. Our approach optimizes over prediction sets defined by arbitrary norm balls, including single and multi-norm formulations. Additionally, by jointly optimizing both the predictive model and predictive uncertainty, we obtain prediction sets that are tight, informative, and computationally efficient, as demonstrated in our experiments on real-world datasets.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In predictive modeling, quantifying uncertainty is often as crucial as making accurate predictions. Traditional point estimates provide limited insight into predictive accuracy, whereas prediction sets offer a more robust alternative by identifying regions that contain the true outcome with high probability. Conformal prediction Vovk et al.; Shafer and Vovk; Angelopoulos et al. provides a model-agnostic framework for constructing such sets with finite-sample validity, ensuring that the true response is captured at least $1-\alpha$ fraction of the time without requiring strong distributional assumptions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the setting of univariate regression, conformal prediction can produce prediction intervals that adapt to heteroskedasticity in the data. Quantile regression, optimized using the pinball loss, is a common approach for learning such intervals Romano et al.. Extending these ideas to multivariate regression, however, where the response is vector-valued, introduces significant challenges. A straightforward extension---constructing Cartesian products of marginal intervals Neeven and Smirnov ---fails to account for dependencies across dimensions, resulting in overly conservative and inefficient prediction sets. Instead, prediction sets must be structured to adapt to the joint distribution of the residuals, balancing validity, efficiency, and flexibility.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

More structured alternatives, such as ellipsoidal prediction sets shaped by empirical residual dependencies Johnstone and Cox; Messoudi et al., incorporate covariance information but assume elliptical symmetry, limiting their adaptability to more complex distributions. More flexible approaches attempt to model joint dependencies explicitly. Copula-based methods Messoudi et al.; Sun and Yu and density estimators Izbicki et al.; Wang et al. relax geometric constraints but often require accurate joint distribution estimation, which is computationally expensive in high dimensions, and typically leads to high estimation variance. Other methods, including optimal transport Klein et al.; Thurin et al. and quantile region estimation Feldman et al., allow for nonconvex and multimodal structures, improving adaptability. However, these approaches typically lack an explicit volume minimization criterion, leading to unnecessarily large sets, and often involve computationally expensive procedures that scale poorly in high dimensions. These methods, along with other approaches, will be reviewed in more detail in Section 1.1 on related work.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these limitations, we introduce a framework for constructing multivariate conformal prediction sets that minimize volume while maintaining valid coverage. Rather than imposing a fixed structure, our approach learns the optimal shape of the prediction set by optimizing over flexible geometric representations, including adaptive norm-based formulations. This optimization extends beyond the prediction set itself, as we jointly learn the predictive model together with the prediction set, ensuring that the predictor is aligned with the minimum-volume criterion. By jointly optimizing over both the predictor and the uncertainty model, we obtain tighter prediction sets that better adapt to the underlying data distribution. Finally, we conformalize the learned sets to achieve finite-sample coverage guarantees. These methodological innovations result in a scalable, data-driven approach that improves efficiency and adaptivity while preserving coverage guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Specifically, our contributions can be summarized as follows: Minimum-volume covering sets (MVCS). We introduce a general optimization-based framework for constructing minimum-volume sets that contain a prescribed fraction of a given dataset in $\mathbb{R}^{k}$. This extends beyond standard approaches by allowing arbitrary norm balls, including data-driven norms that adapt to the geometry of the data. We reformulate the problem as a structured nonconvex optimization, providing both a difference-of-convex (DC) formulation and a convex relaxation for efficient computation. By restricting to $p$-norms, with $p\in(0,\infty)$, we further enable automatic selection of the optimal norm, and we extend this framework to multi-norm formulations, yielding highly flexible and adaptive prediction sets. We illustrate this in Figure 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

Supervised learning with adaptive prediction sets. We extend our MVCS framework to supervised learning, where prediction sets are constructed for a learned predictor $f_{\theta}$ with parameter $\theta\in\Theta$ rather than solely from residuals. Unlike standard conformal methods, which construct prediction sets post hoc, we propose an integrated optimization scheme that jointly learns the predictor, the norm structure, and the transformation function that scales the uncertainty set. This is achieved by introducing a *novel loss function* that learns minimum-volume covering sets (MVCSs) while ensuring valid coverage. Since the problem is nonconvex, we develop an iterative optimization scheme to jointly optimize over all parameters.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Conformalized minimum-volume prediction sets. To ensure valid finite-sample coverage, we integrate our framework with conformal prediction, leveraging a separate calibration set to rescale the learned minimum-volume sets. This approach preserves the adaptive shape of the sets while ensuring rigorous coverage guarantees. The conformalization procedure is computationally efficient and applies seamlessly to any of our formulations---fixed norm, single learned $p$-norm, or multiple norms---making the method broadly applicable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

By bridging conformal prediction and volume optimization, our method provides a principled, data-driven framework for constructing valid, adaptive, and minimal-volume prediction sets in multivariate regression.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Minimum-Volume Covering Set", "weight": 1.0} -->

In this section, we consider the general problem of finding the minimum-volume set that contains a fraction $1-\alpha$ of a given set of points $\{y_{1},\dots,y_{n}\}$ in $\mathbb{R}^{k}$, for some $\alpha\in$. In Section 2.3, we show how this formulation extends naturally to regression, where we observe pairs $\{(x_{i},y_{i})\}_{i=1}^{n}$ and construct adaptive prediction regions that account for multivariate uncertainty. To define these sets, we consider arbitrary norms $\|\cdot\|$ on $\mathbb{R}^{k}$. Formally, given $\|\cdot\|$, we define: Here, $\mu\in\mathbb{R}^{k}$ specifies the center, while $M\in\mathbb{R}^{k\times k}$, with $M\succcurlyeq 0$, determines its shape.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Minimum-Volume Covering Set", "weight": 1.0} -->

These sets serve as our fundamental prediction regions, and we aim to optimize $M$ and $\mu$ to minimize their volume.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Minimum-Volume Covering Set", "weight": 1.0} -->

A notable case arises when $\|\cdot\|$ is the $p$-norm, denoted $\|\cdot\|_{p}$, for some $p\in(0,\infty)$. In this setting, we use the notation $\mathbb{B}(p,M,\mu)$. Beyond optimizing $M$ and $\mu$, we also learn $p$, allowing the norm structure to be selected adaptively based on the data. More generally, combining multiple $p$-norms allows for asymmetric prediction sets, overcoming the symmetry constraints of individual norms. This enables better adaptation to the geometry of the data while ensuring the required $1-\alpha$ coverage. A formal definition of this multi-norm formulation is presented in Section 2.2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Minimum-Volume Covering Set", "weight": 1.0} -->

In the rest of this section, we first establish a general framework for computing the minimum-volume covering set by optimizing $M$ and $\mu$ for a given norm, as introduced in Section 2.1. Since this problem is inherently nonconvex, we propose a difference-of-convex (DC) reformulation and a convex relaxation to enable efficient computation. We then focus on $p$-norms in Section 2.2, jointly optimizing over $M$, $\mu$, and $p\in(0,\infty)$, allowing the optimization process to automatically select the most suitable $p$, leveraging gradient-based methods for nonconvex optimization. Moreover, within the same section, we extend this framework to multiple norms, enabling the construction of more flexible, asymmetric prediction sets. Finally, in Section 2.3 we employ this framework in the context of supervised learning.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Arbitrary norm-based sets", "weight": 1.0} -->

Given a norm $\|\cdot\|$ on $\mathbb{R}^{k}$, our objective is to find the minimum-volume norm-based set that satisfies a prescribed coverage constraint.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Arbitrary norm-based sets", "weight": 1.0} -->

This leads to the optimization problem: | | $\displaystyle\begin{split}\min\quad&\textrm{Vol}(\mathbb{B}(\|\cdot\|,M,\mu))\\ | | \(3\) | | | \mathrm{s.t.}\quad&M\succcurlyeq 0,\;\mu\in\mathbb{R}^{k},\\ | | | | | &\mathrm{Card}\left\{i\in[n]\mid\|M(y_{i}-\mu)\|\leq 1\right\}\geq n-r+1.\end{split}$ | | | Here, the constraint ensures that the set contains at least $n-r+1$ of the given points $\{y_{1},\dots,y_{n}\}$. The quantity $r$ is chosen such that this corresponds to a fraction $1-\alpha$ of the total points.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Arbitrary norm-based sets", "weight": 1.0} -->

The volume of a norm-based set is given by where $\mathbb{B}_{\|\cdot\|}=\{y\in\mathbb{R}^{k}\mid\|y\|\leq 1\}$ is the unit ball under $\|\cdot\|$, and $\lambda$ denotes the Lebesgue measure in $\mathbb{R}^{k}$. Since we do not optimize over the norm $\|\cdot\|$ in this section, the term $\lambda(B_{\|\cdot\|})$ remains fixed, and we can simplify the objective function by minimizing $-\log\det(M)$. This reformulation preserves the essential structure of the problem while removing unnecessary constants. We will return to the full volume formulation in Section 2.2, where we optimize over the norm, making the dependence on $\lambda(B_{\|\cdot\|})$ relevant.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Arbitrary norm-based sets", "weight": 1.0} -->

Under these considerations, the problem reduces to | | $\displaystyle\begin{split}\min\quad&-\log\det(M)\\ | | \(5\) | | | \mathrm{s.t.}\quad&M\succcurlyeq 0,\;\mu\in\mathbb{R}^{k},\\ | | | | | &\mathrm{Card}\left\{i\in[n]\mid\|M(y_{i}-\mu)\|\leq 1\right\}\geq n-r+1.\end{split}$ | | | Throughout this section, we refer to problem as a *minimum-volume covering set* (MVCS) problem. While the objective function $-\log\det(M)$ is convex for $M\succcurlyeq 0$, the problem remains nonconvex due to the cardinality constraint, which introduces a combinatorial structure to the feasible set. This problem is known to be NP hard.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Arbitrary norm-based sets", "weight": 1.0} -->

The following proposition, based on a homogeneity argument, provides an exact reformulation that enables both convex relaxations and exact reformulations via difference-of-convex (DC) programming. In Section 2.2 we also formulate this loss in a way that allows the use of first-order optimization strategies.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Difference-of-convex algorithm (DCA)", "weight": 1.0} -->

DCA begins with an initial point $(\Lambda_{0},\eta_{0})\in\mathrm{dom}\,\partial g$ and iteratively refines the solution by linearizing the concave part of the objective function. At each iteration, the function $g(\Lambda,\eta)$ is linearized at the current iterate $(\Lambda_{t},\eta_{t})$, yielding a convex majorization of $f(\Lambda,\eta)-g(\Lambda,\eta)$. The next iterate $(\Lambda_{t+1},\eta_{t+1})$ is then obtained by solving the resulting convex subproblem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Difference-of-convex algorithm (DCA)", "weight": 1.0} -->

Mathematically, given a subgradient $(G_{\Lambda_{t}},G_{\eta_{t}})\in\partial g(\Lambda_{t},\eta_{t})$, the update rule is where the matrix subgradient $G_{\Lambda_{t}}$ and the vector subgradient $G_{\eta_{t}}$ are defined by and where the vectors $g_{i}$ belong to the subdifferential of the norm function: with $\|\cdot\|_{*}$ being the dual norm of $\|\cdot\|$. This definition ensures that $g_{i}$ acts as a supporting hyperplane at the point $\Lambda_{t}y_{i}+\eta_{t}$ with respect to the given norm structure.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Difference-of-convex algorithm (DCA)", "weight": 1.0} -->

If the norm is differentiable (which holds for $p>1$ and $x\neq 0$), the subgradient simplifies to: In the special case of $p=2$, this reduces to $g_{i}={\Lambda_{t}y_{i}+\eta_{t}}/{\|\Lambda_{t}y_{i}+\eta_{t}\|_{2}}$. In practice, problem (10. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")) can be solved efficiently using cvxpy Diamond and Boyd with the Mosek solver ApS.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Difference-of-convex algorithm (DCA)", "weight": 1.0} -->

A key property of the DCA is that the sequence of objective values $f(\Lambda_{t},\eta_{t})-g(\Lambda_{t},\eta_{t})$ is *nonincreasing and convergent*. However, since problem (6. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")) is nonconvex, DCA does not guarantee global optimality. The algorithm may converge to a local minimum, meaning that the resulting prediction set may not have the smallest possible volume.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convex relaxation", "weight": 1.0} -->

Instead of solving the nonconvex DC formulation via the DCA algorithm (10. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")), an alternative approach is to consider a convex relaxation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convex relaxation", "weight": 1.0} -->

problem (see Appendix A for details).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convex relaxation", "weight": 1.0} -->

This formulation can be efficiently solved using standard off-the-shelf solvers. However, since the term $\overline{\sigma}_{r-1}$ played a crucial role in balancing coverage constraints with volume minimization, the relaxed formulation may lead to larger prediction sets than the exact DC formulation. Nevertheless, in scenarios where computational efficiency is prioritized, this convex relaxation provides a scalable alternative.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2.2 (MVCS for the DCA and convex relaxation problem)", "weight": 1.0} -->

Let $(\Lambda^{\star},\eta^{\star})$ denote the final iterate of the DCA method (10. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")) or the global solution of the convex relaxation. The corresponding MVCS set, which contains $n-r+1$ points, is given by $\{y\in\mathbb{R}^{k}\mid\|\Lambda^{\star}y+\eta^{\star}\|\leq\sigma_{r}\left\{\|\Lambda^{\star}y_{i}+\eta^{\star}\|\right\}\}$. We illustrate in Figure 2. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression") the solutions obtained by both methods for different distributions. In the Gaussian case (left), the solutions are nearly identical, with both approaches aligning with the empirical covariance structure.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2.2 (MVCS for the DCA and convex relaxation problem)", "weight": 1.0} -->

However, for an asymmetric distribution (right), the convex relaxation method is more influenced by the tails, stretching the prediction set outward, whereas the DCA solution remains concentrated around the high-density region near the origin. These observations suggest that in elliptical distributions, the convex relaxation method performs well, but for non-elliptical distributions, the DCA method provides tighter, more representative sets.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2.3 (Connection to pinball loss)", "weight": 1.0} -->

A key insight emerges when taking the derivative of the objective function in with respect to $\nu$: at optimality, $\nu^{\star}$ is the $(n-r+1)$-th order statistic of the nonconformity scores, enforcing the required coverage constraint. This mechanism closely parallels the structure of quantile regression Koenker, where the pinball loss implicitly selects a quantile level by balancing over- and under-estimation errors. A similar argument appears in \Roth, [2022, Lemma 2.2.1\], which establishes that minimizing the pinball loss aligns with quantile estimation through a first-order optimality condition.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning $p$-norm prediction sets", "weight": 1.0} -->

Thus far, we have considered the problem of finding the minimum-volume norm-based set while assuming that the norm structure is fixed. We now extend this approach by allowing the norm itself to be optimized. To accomplish this, we restrict our attention to the family of $p$-norms, parameterized by $p\in(0,\infty)$. This introduces an additional degree of flexibility, enabling the prediction set to better conform to the geometry of the data.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Learning $p$-norm prediction sets", "weight": 1.0} -->

Its explicit formula is given by Dirichlet, where $\Gamma(\cdot)$ denotes the gamma function Artin. For brevity, we will retain the notation $\lambda(B_{\|\cdot\|_{p}})$ throughout the remainder of the paper. Building on the reasoning in Proposition 2.1. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression"), we derive the following corollary, which provides a more structured and tractable reformulation of the MVCS problem.

<!-- chunk {"id": "body-0033", "role": "body", "section": "First-order optimization strategy", "weight": 1.0} -->

While the optimization problem (14. ‣ 2.2 Learning 𝑝-norm prediction sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")) is already nonconvex due to the function $\sigma_{r}$, the additional optimization over $p$ further complicates the landscape, breaking the difference-of-convex (DC) structure that allowed for efficient iterative optimization in the fixed-norm case. Consequently, direct application of the DCA is no longer possible, and solving for $p$ requires alternative strategies. We thus turn to first-order optimization methods, as explained next.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 2.5 (Unconstrained single-norm MVCS)", "weight": 1.0} -->

The primary challenge in designing such an algorithm is handling the constraint $\Lambda\succcurlyeq 0$. To eliminate this constraint, we parameterize $\Lambda$ as $\Lambda:=AA^{\top}$, where $A\in\mathbb{R}^{k\times k}$. This parameterization ensures positive semidefiniteness without imposing additional assumptions on $A$. Additionally, to allow for unconstrained optimization over $p$, we reparameterize it as $|p|$, enabling updates without restrictions on its sign. With these transformations, the optimization problem reduces to minimizing the following *unconstrained* loss function, over $A\in\mathbb{R}^{k\times k}$, $\mu\in\mathbb{R}^{k}$, and $p\in\mathbb{R}$. For this objective, standard first-order optimization algorithms, such as gradient descent, can be applied.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2.5 (Unconstrained single-norm MVCS)", "weight": 1.0} -->

For our experiments, we update gradients using the Adam optimizer Kingma and Ba in PyTorch, with a learning rate scheduler (see Appendix E). After optimization, the final transformation is recovered as $\Lambda^{*}=A^{*}A^{*\top}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2.5 (Unconstrained single-norm MVCS)", "weight": 1.0} -->

Despite the challenges induced by the nonconvexity Lee et al., we observe empirically that the joint optimization over $(A,\mu,p)$ with nonconvex gradient descent performs remarkably well in practice. In particular, our numerical experiments demonstrate that the learned values of $p$ often yield well-calibrated prediction sets that align with the intrinsic geometric properties of the data. We illustrate this in Figure 3, where the left panel compares the MVCS obtained via problem (14. ‣ 2.2 Learning 𝑝-norm prediction sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")) to the DCA approach with fixed $p=2$. While both maintain the prescribed coverage level, optimizing $p$ yields a more flexible shape that better fits the data distribution. The right panel further demonstrates this effect in an anisotropic setting, where the learned $p=0.58$ results in an elongated prediction set, adapting to the underlying structure.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2.5 (Unconstrained single-norm MVCS)", "weight": 1.0} -->

Further illustrating the flexibility of our approach, Figure 4 presents two three-dimensional examples where the learned values of $p$ adapt to the underlying data distribution. The left panel shows an elongated prediction set with $p=0.56$, learned from data uniformly distributed in an $\ell_{0.5}$-ball, capturing its directional spread. In contrast, the right panel corresponds to an exponential distribution, where the learned $p=8.19$ results in an axis-aligned prediction region, similar to the patterns observed in the right panel of Figure 2. ‣ 2.1 Arbitrary norm-based sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression").

<!-- chunk {"id": "body-0038", "role": "body", "section": "Learning multi-norm prediction sets", "weight": 1.0} -->

Thus far, we have optimized prediction sets using a single global norm. While this provides flexibility, it fails to adapt to local variations in uncertainty. In many applications, uncertainty behaves asymmetrically---certain directions require tighter coverage, while others necessitate broader regions. To address this, we extend our framework to allow for region-dependent norms by partitioning the space into $m$ disjoint regions $\{\mathcal{A}_{j}\}_{j=1}^{m}$, each with its own norm $p_{j}$. A natural way to define these partitions is through axis-aligned decomposition, where the space is split along coordinate axes. This approach ensures computational tractability and facilitates structured volume computations, allowing for at most $m=2^{k}$ regions in dimension $k$. For example, when $k=2$, the space can be split into four quadrants, and when $k=3$, it can be divided into eight octants.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning multi-norm prediction sets", "weight": 1.0} -->

To construct these prediction sets, we introduce a global rotation matrix $R$ that aligns the space, followed by region-specific *diagonal* scaling matrices $D_{j}$, for $j\in[m]$. The role of $R$ is to standardize the representation of data by aligning principal directions of variation with coordinate axes. Within each partition, the diagonal matrix $D_{j}$ then scales the axes independently, capturing anisotropic structure while preserving computational efficiency.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning multi-norm prediction sets", "weight": 1.0} -->

&\mathrm{Card}\left\{i\in[n]\mid d(y_{i},\mu;{R,\{D_{j}\}_{j=1}^{m}})\leq 1\right\}\geq n-r+1.\end{split}$ | | | Here, the total volume of the multi-norm prediction set is given by the average of the region-specific volumes, where $\lambda(B_{\|\cdot\|_{p_{j}}})$ represents Lebesgue measure of the unit $p_{j}$-norm ball, given explicitly.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Learning multi-norm prediction sets", "weight": 1.0} -->

The global rotation matrix $R$ does not affect the volume since it is an orthogonal transformation with $\det(R)=1$, leaving the determinant term unchanged. Moreover, the uniform weighting of $1/m$ arises because the matrices $D_{j}$ are diagonal, so the total volume is taken as the average contribution across all regions. The following proposition provides a reformulation of that is amenable to iterative optimization algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2.7 (Unconstrained multi-norm MVCS)", "weight": 1.0} -->

Similarly to the single-norm approach, we can express the objective function in an unconstrained form as: To enable unconstrained optimization over the rotation matrix $R$, we introduce a parameterization based on the QR decomposition. Specifically, we optimize over a full matrix $Q\in\mathbb{R}^{k\times k}$ and extract the rotation matrix via the decomposition $Q=R_{1}R_{2}$, where $R_{1}$ is an orthogonal matrix and $R_{2}$ is upper triangular. Since $R_{1}$ may have determinant $-1$, we ensure that $R$ remains a proper rotation matrix in $\mathrm{SO}(k)$ by setting $R=R_{1}$ if $\det R_{1}=1$, and $R=I_{-}R_{1}$ if $\det R_{1}=-1$, where $I_{-}$ is a diagonal matrix with all ones except for a $-1$ in the first diagonal entry.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2.7 (Unconstrained multi-norm MVCS)", "weight": 1.0} -->

Problem (17. ‣ Learning multi-norm prediction sets. ‣ 2.2 Learning 𝑝-norm prediction sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")) provides a principled framework for learning adaptive multi-norm prediction sets, but it is nonconvex. Nonetheless, its structured formulation again allows for effective optimization using iterative approaches to obtain locally optimal solutions. Empirical results demonstrate that the learned multi-norm prediction sets significantly enhance flexibility and adaptivity, effectively capturing complex uncertainty structures across different regions of space. We illustrate this in Figure 5, where we compare MVCS sets obtained via the iterative procedure described in Section 5.1 for solving problem (17. ‣ Learning multi-norm prediction sets. ‣ 2.2 Learning 𝑝-norm prediction sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression")). The left panel contrasts the single-norm MVCS, learned with $p=1.21$, against a multi-norm formulation that assigns distinct norms to different regions of the space.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 2.7 (Unconstrained multi-norm MVCS)", "weight": 1.0} -->

The multi-norm MVCS successfully adapts to the anisotropic data structure by varying $p$ across regions, yielding a more expressive and data-conforming prediction set. In the right panel, we further observe that learning multiple norms refines the predictive set shape, adjusting its geometry based on local uncertainty.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Application to multivariate regression", "weight": 1.0} -->

In many practical scenarios, we aim to construct prediction sets for a multivariate response variable $Y\in\mathbb{R}^{k}$ given a covariate vector $X\in\mathbb{R}^{d}$. The MVCS framework naturally extends to this setting by modeling uncertainty through residuals relative to a predictive model. Let $f_{\theta}:\mathbb{R}^{d}\to\mathbb{R}^{k}$ be a parametric model with parameters $\theta$. If $f_{\theta}$ is fixed (i.e., fit on a separate dataset), we can apply the MVCS methodology to the residuals $\{y_{i}-f_{\theta}(x_{i})\}_{i=1}^{n}$ to construct the prediction region where $\mathbb{B}(p,M,\mu)$ is learned using Corollary 2.4.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Application to multivariate regression", "weight": 1.0} -->

‣ 2.2 Learning 𝑝-norm prediction sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression"). The role of the correction term $\mu$ is to optimally position the covering set within the residual space. Unlike a shift meant to correct predictive bias in $f_{\theta}(x)$, $\mu$ aligns the set to minimize its volume while still maintaining coverage. This approach yields feature-dependent prediction regions by centering the set at $f_{\theta}(x)+\mu$. However, the estimated set remains *globally constrained*, as the same structure is applied uniformly across all values of $x$. In Section 3, we introduce *local adaptivity*, allowing the prediction set to adjust to variations in $x$ and better capture heteroskedastic uncertainty.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Optimizing over $\\theta$", "weight": 1.0} -->

Rather than fixing $f_{\theta}$, a natural extension is to jointly optimize over $\theta$ together with the MVCS parameters. This formulation seeks the predictive model that minimizes the volume of the covering set, effectively balancing predictive accuracy and uncertainty quantification. By directly learning $\theta$ to align with the minimum-volume criterion, the model adapts to the data in a way that tightens the overall uncertainty region.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Optimizing over $\\theta$", "weight": 1.0} -->

A key consequence of this joint optimization is that the correction term $\mu$ becomes unnecessary. When $f_{\theta}$ is fixed, $\mu$ is used to optimally reposition the prediction set. However, when optimizing $f_{\theta}$, the model itself can absorb any systematic shift. As a result, the optimization problem becomes | | $\displaystyle\begin{split}\min\quad&-\log\det(\Lambda)+k\log\sigma_{r}\left\{\|\Lambda(y_{i}-f_{\theta}(x_{i}))\|_{p}\right\}+\log\lambda(B_{\|\cdot\|_{p}})\\ | | \(19\) | | | \mathrm{s.t.}\quad&\Lambda\succcurlyeq 0,\;p>0,\;\theta\in\Theta,\end{split}$ | | | where $\Theta$ represents the space of permissible model parameters.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Optimizing over $\\theta$", "weight": 1.0} -->

This formulation has several advantages: *Unified learning.* The prediction function $f_{\theta}$ is no longer a separate entity; it is learned jointly with the uncertainty quantification model.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Optimizing over $\\theta$", "weight": 1.0} -->

*Implicit set alignment.* Any shift that would have been captured by $\mu$ is now directly absorbed by the optimization over $f_{\theta}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Optimizing over $\\theta$", "weight": 1.0} -->

*Tighter prediction sets.* The predictive model is adjusted not just for accuracy, but to yield the minimum-volume uncertainty set.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Optimizing over $\\theta$", "weight": 1.0} -->

The joint optimization introduces additional computational complexity, but empirical results indicate that the method performs well in practice, effectively balancing predictive accuracy and uncertainty quantification while adapting to the structure of the data. We illustrate this in Figure 6, which presents the MVCSs constructed for different feature values $X_{i}$ in a setting where the noise distribution varies with $X$ (see Section 5 for details). The learned norms adapt to the residual structure, leading to different prediction set geometries. In the left panel, where the residuals are Gaussian, the optimization selects $p=1.93$, while in the right panel, corresponding to an exponential residual distribution, the learned $p=2.24$. Notably, the same prediction set is applied uniformly across all $X$, as the transformation $M$ is learned globally rather than varying with $X$. In Section 3, we extend this framework to introduce local adaptivity, allowing the prediction sets to adjust to different feature values (see Figure 7 for a direct comparison).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Local Adaptivity in Multivariate Regression", "weight": 1.0} -->

In the previous section, we established a general framework for constructing minimum-volume covering sets and applied it to regression by modeling uncertainty through residuals. While this approach enables feature-dependent prediction by centering the region at $f_{\theta}(x)+\mu$, it assumes a globally shared uncertainty structure, applying the same prediction set across all feature values. However, residual distributions often exhibit heteroskedasticity, meaning that uncertainty varies significantly with $x$. A single global region may be overly conservative in some areas while too narrow in others. To address this, we now introduce *local adaptivity*, where the prediction set varies with $x$ by learning an covariate-dependent transformation matrix $M(x)$ that adjusts the shape and size of the prediction set. Additionally, we jointly optimize the predictive model $f_{\theta}$ to minimize uncertainty while maintaining coverage.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Local Adaptivity in Multivariate Regression", "weight": 1.0} -->

Given a dataset $\{(x_{i},y_{i})\}_{i=1}^{n}$, we define the residuals $\{y_{i}-f_{\theta}(x_{i})\}_{i=1}^{n}$, which quantify the discrepancy between predictions and observed responses. To account for feature-dependent variations in uncertainty, we introduce a local transformation $M(\cdot)$ and learn it from the residuals. The resulting prediction region is given by where $\mathbb{B}(p,M(x),0)$ is a locally adaptive minimum-volume norm-based set, learned from the residuals to ensure the required coverage. As discussed in Section 2.3, centering the prediction set at zero is justified when additionally optimizing over $\theta$ since any systematic shift can be absorbed within $f_{\theta}(x)$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Local Adaptivity in Multivariate Regression", "weight": 1.0} -->

To formalize the objective of learning locally adaptive prediction sets, we consider the following population-level optimization problem: | | $\displaystyle\begin{split}\min\quad&\mathbb{E}\left[\text{Vol}(C(X))\right]\\ | | \(20\) | | | \mathrm{s.t.}\quad&\mathrm{Prob}\left\{Y\in C(X)\right\}\geq 1-\alpha.\end{split}$ | | | Since the true distribution of $(X,Y)$ is unknown, we approximate this objective using the observed dataset $\{(x_{i},y_{i})\}_{i=1}^{n}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Local Adaptivity in Multivariate Regression", "weight": 1.0} -->

such that at least $1-\alpha$ of the training points are contained within their respective prediction sets. This formulation minimizes the average volume of the prediction sets while ensuring empirical coverage.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Local Adaptivity in Multivariate Regression", "weight": 1.0} -->

We now derive an equivalent reformulation that facilitates efficient optimization. The following proposition formalizes the extension of the MVCS framework from formulation to locally adaptive transformations, allowing the prediction set to vary with $x$. While we present the result for a single norm $p$, this formulation can be immediately extended to multiple norms in the spirit of Proposition 2.6. ‣ Learning multi-norm prediction sets. ‣ 2.2 Learning 𝑝-norm prediction sets ‣ 2 Minimum-Volume Covering Set ‣ Minimum Volume Conformal Sets for Multivariate Regression"). However, our numerical experiments indicate that extending the multi-norm MVCS framework to locally adaptive transformations in regression often leads to overfitting. While multi-norm MVCS effectively captures complex uncertainty structures in Section 2, applying it in a regression setting requires learning feature-dependent transformations, which substantially increases the complexity of the optimization landscape. As a result, the learned prediction sets may fit well for certain feature values $x_{i}$ but fail to generalize across the input space, leading to inconsistent adaptivity. This suggests that while multi-norm formulations offer greater flexibility, their practical success in regression depends on having sufficient training data and appropriate regularization to mitigate overfitting.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 3.2 (Unconstrained locally adaptive MVCS)", "weight": 1.0} -->

Extending the single-norm formulation from Section 2, we express the objective function in an unconstrained form as: where $A(\cdot)$ is a function mapping features $x\in\mathbb{R}^{d}$ to a transformation matrix in $\mathbb{R}^{k\times k}$, ensuring that the learned transformation remains positive semidefinite via the parameterization $\Lambda(x)=A(x)A(x)^{\top}$. Moreover, the reparameterization $|p|$ allows for unconstrained optimization over the norm parameter, enabling updates without restrictions on its sign. This formulation facilitates efficient first-order gradient-based optimization without requiring explicit constraints on $\Lambda(\cdot)$ or $p$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 3.2 (Unconstrained locally adaptive MVCS)", "weight": 1.0} -->

While optimizing over $A(\cdot)$ introduces additional computational complexity, it provides a significant advantage: the resulting prediction sets are tighter and better calibrated to local uncertainty. Empirical results confirm that this adaptivity leads to meaningful improvements, particularly in settings where uncertainty varies across feature space. We illustrate this in Figure 7, where MVCSs are constructed in a locally adaptive manner. Compared to Figure 6, where a single transformation was applied globally, the prediction sets here adjust to the residual distribution at each feature value $x_{i}$. The left panel, corresponding to Gaussian residuals, yields $p=2.08$, while the right panel, with exponential residuals, results in $p=2.52$. By allowing the prediction sets to vary with $X$, this approach more effectively captures heteroskedasticity, improving both calibration and efficiency.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conformalized Minimum-Volume Prediction Sets", "weight": 1.0} -->

Thus far, we have developed a framework for constructing minimum-volume prediction sets by leveraging geometric structure in residuals. These sets are designed to provide high coverage within the training data, and we need to ensure that the coverage properties extend to unseen test samples. We do this by integrating the methods discussed thus far with conformal prediction.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conformalized Minimum-Volume Prediction Sets", "weight": 1.0} -->

The conformalization procedure we adopt follows the standard split conformal prediction framework Vovk et al.; Papadopoulos et al., with the key difference being our choice of nonconformity scores, which are derived from the locally adaptive MVCS sets presented in Section 3. We consider a setting where we are given a dataset of $n$ i.i.d. samples $(X_{i},Y_{i})\sim\mathbb{P}$, where $\mathbb{P}$ is the unknown joint distribution of covariates $X_{i}\in\mathbb{R}^{d}$ and responses $Y_{i}\in\mathbb{R}^{k}$. Our goal is to construct covariate-dependent prediction sets $C(x)$ that satisfy the coverage guarantee for a prescribed confidence level $1-\alpha$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conformalized Minimum-Volume Prediction Sets", "weight": 1.0} -->

In line with the split conformal prediction framework, we partition the dataset into *independent* sets: $\mathcal{D}_{1}$, the *proper training set*, with ${\rm Card}(\mathcal{D}_{1})=n_{1}$; $\mathcal{D}_{2}$, the *calibration set*, with ${\rm Card}(\mathcal{D}_{2})=n_{2}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conformalized Minimum-Volume Prediction Sets", "weight": 1.0} -->

Using $\mathcal{D}_{1}$, we fit a predictive model $f_{\theta}$ and estimate a minimum-volume transformation function $M(x)$ using the optimization formulation presented in Proposition 3.1. ‣ 3 Local Adaptivity in Multivariate Regression ‣ Minimum Volume Conformal Sets for Multivariate Regression"). The choice of structure---whether to use a fixed norm, a single learned $p$-norm, or a multiple-norm extension---determines the learned transformation and the associated prediction set shape. For simplicity, we present a version of the conformalization procedure in which the prediction sets are derived using a single learned $p$-norm, though the same approach extends to arbitrary norm choices and multi-norm formulations. Thus, while the conformalization step follows the standard framework, our methodology is distinguished by the use of locally adaptive MVCS-based scores.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conformalized Minimum-Volume Prediction Sets", "weight": 1.0} -->

In this setting, we define the nonconformity scores as To simplify notation, we denote the scores computed on the calibration set as $S_{i}=s(X_{i},Y_{i})$, for $i\in[n_{2}]$. These scores are then used to determine a conformalized threshold that ensures the required coverage. Specifically, we compute an empirical quantile of the calibration scores, incorporating a finite-sample correction. The threshold is given by The quantity $\widehat{q}_{\alpha}$ defines the conformalized radius that determines the final prediction region. By leveraging the independent calibration dataset, this approach guarantees that the constructed prediction sets satisfy the marginal coverage requirement in a finite-sample sense. For a new test point $X_{n+1}$, we define the conformalized prediction set as This formulation maintains the same geometric structure as the minimum-volume prediction sets derived in Section 3, but now scales their size using $\widehat{q}_{\alpha}$ to guarantee marginal coverage.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conformalized Minimum-Volume Prediction Sets", "weight": 1.0} -->

We now formally state the finite-sample coverage property of the conformalized MVCS.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

All the results presented in this section are fully reproducible and available in the associated GitHub repository.^22^2

<!-- chunk {"id": "body-0067", "role": "body", "section": "Training procedure", "weight": 1.0} -->

Optimizing the training objective (22. ‣ 3 Local Adaptivity in Multivariate Regression ‣ Minimum Volume Conformal Sets for Multivariate Regression")) is challenging due to its nonconvexity. To enable efficient minimization using first-order optimization techniques, we introduce a structured parameterization. Specifically, both the predictive function for the center $f_{\theta}$ and the transformation matrix $\Lambda_{\phi}$ are modeled using neural networks. To ensure positive semi-definiteness of the learned transformation, we define a mapping $A_{\phi}:\mathbb{R}^{d}\to\mathbb{R}^{k\times k}$ that outputs a $k\times k$ matrix and set $\Lambda_{\phi}(x)=A_{\phi}(x)A_{\phi}(x)^{T}$. This guarantees that $\Lambda_{\phi}(x)$ satisfies the constraints of the optimization problem while allowing for flexible, data-driven adaptation. This parameterization enables direct (unconstrained) minimization of the loss in (24.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Training procedure", "weight": 1.0} -->

‣ 3 Local Adaptivity in Multivariate Regression ‣ Minimum Volume Conformal Sets for Multivariate Regression")). Our training procedure consists of three sequential stages: *Pretraining the predictive model.* We first train the predictive model $f_{\theta}$, which determines the center of the prediction set, using a mean squared error objective. This pretraining step stabilizes the learning process and improves convergence.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Training procedure", "weight": 1.0} -->

*Optimizing the transformation matrix.* Keeping $f_{\theta}$ fixed, we then optimize the matrix model by adjusting $\Lambda_{\phi}(x)$ based on the residuals. This sequential approach is motivated by empirical observations: when $f_{\theta}$ overfits, the residual structure deteriorates, making it difficult for the matrix model to generalize effectively.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Training procedure", "weight": 1.0} -->

*Joint optimization.* Finally, we jointly optimize both $\theta$ and $\phi$, refining the predictive model and the uncertainty quantification simultaneously. To approximate the coverage constraint efficiently in mini-batch training, we compute the $r$-th largest nonconformity score within each batch, where $r=\lfloor\alpha B\rfloor$ and $B$ denotes the batch size.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Training procedure", "weight": 1.0} -->

This structured approach ensures a balance between expressivity and stability, preventing overfitting while effectively capturing the heteroskedastic structure of the data. The resulting prediction sets are both adaptive and well-calibrated, as demonstrated in our empirical evaluations.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Comparative baselines", "weight": 1.0} -->

We compare our method (single-norm MVCS) against three established baselines: Naïve Quantile Regression Dheur et al. (naïve QR), the empirical covariance matrix Johnstone and Cox (emp. cov.), and the local empirical covariance method Messoudi et al. (loc. emp. cov.). Below, we summarize these approaches.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Comparative baselines", "weight": 1.0} -->

*Naïve quantile regression.* This strategy involves performing quantile regression using the pinball loss Steinwart and Christmann for the quantiles ${\tilde{\alpha}}/{2}$ and $1-{\tilde{\alpha}}/{2}$ along all axes on a training dataset. To avoid overcovering, we select $\tilde{\alpha}=2(1-(1-\alpha)^{1/k})$, as suggested by previous work Dheur et al. to fit the quantile networks $q$. The prediction regions are then conformalized on a calibration dataset using the score obtaining the calibration quantile $\hat{q}^{p}_{\alpha}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Comparative baselines", "weight": 1.0} -->

At test time, the coverage and average volume of the region are computed on a test dataset, with the volume for each test point $x$ given by $\prod_{i}(q_{1-{\tilde{\alpha}}/{2}}(x)_{i}-q_{{\tilde{\alpha}}/{2}}(x)_{i}+2\hat{q}^{p}_{\alpha})$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Comparative baselines", "weight": 1.0} -->

*Empirical covariance matrix.* A widely used alternative constructs ellipsoidal prediction regions by leveraging the empirical covariance structure of the residuals Johnstone and Cox. The estimated covariance matrix $\hat{\Sigma}$ is computed from the training residuals, and the prediction region is shaped using the Mahalanobis norm. The nonconformity score is given by We compute the calibration quantile $\hat{q}^{e}_{\alpha}$ with the calibration dataset and the volume of the ellipsoid is $\lambda(B_{\|\cdot\|_{2}})\cdot(\det((\hat{q}^{e}_{\alpha})^{2}\cdot\hat{\Sigma}))^{1/2}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Comparative baselines", "weight": 1.0} -->

*Local empirical covariance matrix.* While the global covariance structure captures overall variability, it fails to adapt to local heteroskedasticity. To address this limitation, a local empirical covariance approach Messoudi et al. estimates $\hat{\Sigma}_{x}$ using only the $m$ nearest neighbors of $x$ in the training dataset. The nonconformity score is then computed as We compute the calibration quantile $\hat{q}^{l}_{\alpha}$ with the calibration dataset and the corresponding volume for a test point $x$ is $\lambda(B_{\|\cdot\|_{2}})\cdot(\det((\hat{q}^{l}_{\alpha})^{2}\cdot\hat{\Sigma}_{x}))^{1/2}$. By locally adapting the covariance structure, this method yields more flexible prediction sets that better reflect data-dependent uncertainty.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Comparative baselines", "weight": 1.0} -->

These competing strategies serve as baselines for evaluating our proposed approach, demonstrating its advantages in both adaptivity and efficiency.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Synthetic dataset", "weight": 1.0} -->

Throughout our experiments, we utilize four datasets: a training dataset, a validation dataset for model selection, a calibration dataset for conformalization, and a test dataset for evaluating final coverage and volume. This setup follows standard practice in the literature.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conditional coverage", "weight": 1.0} -->

A key consideration in conformal prediction is whether a given strategy maintains conditional coverage. While marginal coverage guarantees ensure that $\mathrm{Prob}\left\{Y\in C(X)\right\}\geq 1-\alpha$, conditional validity (i.e., requiring $\mathrm{Prob}\{Y\in C(X)\mid X\}=1-\alpha$) is generally unattainable without strong assumptions on the data distribution Foygel Barber et al.. Aggressively minimizing volume can degrade conditional validity Huang et al., as our optimization objective (22. ‣ 3 Local Adaptivity in Multivariate Regression ‣ Minimum Volume Conformal Sets for Multivariate Regression")) does not explicitly enforce constraints on the $r$-largest values. However, the neural network parameterization promotes generalization, leading to empirically favorable results despite the lack of theoretical convergence guarantees due to nonconvexity.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conditional coverage", "weight": 1.0} -->

To assess conditional coverage empirically, we conduct a 1D regression experiment with $Y=f(X)+t(X)B$, where $(X,Y)\in\mathbb{R}^{2}$ and $B\sim\mathcal{E}$ follows an asymmetric exponential distribution scaled by $t(X)=0.5+2X$. We compare our method against the naïve quantile regression strategy. Figure 8 reports results for a target coverage of $0.99$ (additional results for $0.90$ are in Appendix Figure 9). We observe that our adaptive framework effectively adjusts to the data, showing no clear signs of degraded conditional coverage.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Robustness to outliers", "weight": 1.0} -->

Our loss function is inherently robust to outliers, up to a fraction of $\alpha$. To illustrate this, we replicate the previous experiment while introducing extreme values for a fraction $3\alpha/4$ of the data points.^33^3These extreme values are fixed at 10. We compare our approach with the pinball loss and the standard nonconformity score, using the same evaluation framework. The pinball loss is trained on the quantiles $\alpha/2$ and $1-\alpha/2$, but under contamination, its optimal quantiles shift, leading to unreliable prediction sets. In particular, when the proportion of outliers in the upper quantile exceeds $\alpha/2$, the estimated $(1-\alpha)$-quantile is dominated by extreme values, compromising the validity of the prediction sets. This highlights the limitations of quantile-based methods in the presence of outliers, whereas our approach remains robust, maintaining stable and reliable uncertainty quantification.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Multivariate regression", "weight": 1.0} -->

We evaluate our method's performance in multivariate regression by comparing the average volume and achieved coverage of the prediction sets on a test dataset against baseline approaches. The data is generated as $Y=f(X)+t(X)B$, where $X\sim\mathcal{N}(0,I_{4})$ and $Y\in\mathbb{R}^{4}$. The noise term $B$ follows a fixed distribution and is modulated by the transformation $t(X)$, with further details provided in Appendix B.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Multivariate regression", "weight": 1.0} -->

We assess performance across four synthetic settings: (i) fixed exponential noise ($t$ constant), (ii) exponential noise with a variable transformation $t(X)$, (iii) fixed Gaussian noise, and (iv) Gaussian noise with a transformation. The volume of each prediction set is computed as the mean volume across test points. To account for the effect of dimensionality, we normalize each volume by taking its $1/k$ power. Coverage is measured as the proportion of test samples contained within their respective sets. The empirical covariance baseline corresponds to the predictor with the lowest Mean Squared Error (MSE), selected before fine-tuning with our proposed loss. Results are reported for a target coverage of $0.90$, averaged over 10 runs, excluding the highest and lowest volumes. In all cases, our method achieves the smallest average volume (Table 1) while maintaining valid marginal coverage (Table 2). Additional results for a coverage level of $0.99$ are provided in Appendix C.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Real datasets", "weight": 1.0} -->

We evaluate our approach on nine benchmark datasets commonly used in multivariate regression studies Dheur et al.; Feldman et al.; Wang et al.. Details regarding these datasets, including the response dimensionality and hyperparameter choices, are provided in Appendix D. We compare different strategies for both $\alpha=0.1$ and $\alpha=0.01$. Each dataset is split into four subsets---training, validation, calibration, and test---using respective proportions of 70%, 10%, 10%, and 10%.^44^4Except for the energy dataset, for which the data splitting is 55%, 15%, 15%, 15% due to the smaller amount of samples. To ensure robust evaluation, results are averaged over 10 independent runs, discarding the highest and lowest volume values. Additionally, each volume is scaled by taking its $1/k$-th power to normalize for dimensionality.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Real datasets", "weight": 1.0} -->

To preprocess the data, we apply a quantile transformation to both the covariates ($X$) and responses ($Y$) using scikit-learn Pedregosa et al., ensuring normalization across datasets. Our approach consistently minimizes the volume of prediction sets while maintaining valid marginal coverage. Specifically, we achieve the best average volume in sixteen out of eighteen experiments while preserving the desired coverage level (Tables 4 and 6).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion", "weight": 1.5} -->

While our approach provides a principled framework for learning minimum-volume prediction sets with finite-sample validity, several challenges remain. First, our reliance on first-order optimization methods does not guarantee avoidance of poor local minima, particularly given the inherent nonconvexity of our loss function. While our empirical results demonstrate stable performance, exploring alternative optimization strategies---such as second-order methods or tailored regularization techniques---could enhance robustness to nonconvexity.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

Second, hyperparameter selection remains a critical factor. The learning rate of the matrix model, for instance, strongly influences convergence behavior, and we observed that optimal settings vary across datasets. Developing more adaptive or automated tuning strategies could improve generalization and reduce the need for manual adjustment.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion", "weight": 1.5} -->

Additionally, while our framework effectively minimizes volume, aggressive volume reduction may come at the expense of conditional coverage. Although our empirical results indicate strong generalization, the formulation does not explicitly regulate coverage at the level of individual feature values. Ensuring robust performance in regions with limited training data remains an open challenge, particularly in highly heteroskedastic settings. Future work could explore strategies to balance volume minimization with improved conditional reliability.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, our model is designed for a fixed confidence level $\alpha$, similar to quantile regression approaches. However, one advantage of our framework is that it allows for post-hoc adjustments, enabling adaptation to different coverage levels after training. Investigating how to efficiently recalibrate prediction sets for varying confidence levels could further enhance flexibility.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

Despite these challenges, our approach demonstrates strong empirical performance across both synthetic and real datasets, offering a scalable and adaptive solution to multivariate uncertainty quantification. Future research could build upon this foundation to improve theoretical guarantees, explore alternative optimization techniques, and extend the method to further application areas.
