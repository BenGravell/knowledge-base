<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Soft Projections for Robust Data-driven Control

Topics include Predictive control, Robustness, Generalization, Control, Learning, Soft projections.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider data-based predictive control based on behavioral systems theory. In the linear setting this means that a system is described as a subspace of trajectories, and predictive control can be formulated using a projection onto the intersection of this behavior and a constraint set. Instead of learning the model, or subspace, we focus on determining this projection from data. Motivated by the use of regularization in data-enabled predictive control (DeePC), we introduce the use of soft projections, which approximate the true projector onto the behavior from noisy data. In the simplest case, these are equivalent to known regularized DeePC schemes, but they exhibit a number of benefits. First, we provide a bound on the approximation error consisting of a bias and a variance term that can be traded-off by the regularization weight. The derived bound is independent of the true system order, highlighting the benefit of soft projections compared to low-dimensional subspace estimates. Moreover, soft projections allow for intuitive generalizations, one of which we show has superior performance on a case study. Finally, we provide update formulas for soft projectors enabling the efficient adaptation of the proposed data-driven control methods in the case of streaming data.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Direct data-driven predictive control methods have recently gained significant attention in the control community. These formulations are fundamentally rooted in behavioral systems theory, which takes a representation-free perspective and treats dynamical systems simply as sets of trajectories. For linear time-invariant (LTI) systems, this means that the system behavior can be described as a linear subspace containing all possible trajectories. This viewpoint enables one to use raw data directly to represent the underlying system. This approach is often referred to as direct to emphasize the contrast with traditional indirect approaches, which require the intermediate step of first identifying a parametric model before performing controller design based on that estimate. To ensure that these direct control formulations remain robust to measurement noise and nonlinearities, regularization is typically added to the optimization problem. As demonstrated by numerous empirical case studies, regularized data-driven control methods often perform remarkably well in practical application domains.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Initially, regularization was introduced into direct data-driven control formulations heuristically, lacking clear theoretical interpretability. Subsequent research has largely focused on addressing this gap to develop more interpretable formulations. While some of these studies successfully explain the implicit effects of regularization within existing frameworks, they do not propose novel control algorithms. Conversely, other approaches have modified the seminal formulation to derive new, theoretically grounded regularization terms. Beyond interpretability, a second major challenge is the efficient integration of online data updates into these control schemes, as highlighted in the surveys. Although recent methods allow for the online adaptation of behavioral subspace models, they rely on explicitly estimating the underlying subspace. This explicit approach has notable drawbacks: representing the behavior as a low-dimensional subspace generally yields inferior performance compared to regularized schemes, and the accuracy of these estimates is highly sensitive to system order selection.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address current challenges, we take a ground-up perspective rather than adapting the seminal formulation. Based on behavioral systems theory, we view predictive control for linear systems as a projection onto the behavior. Inspired by the principle behind the direct approach to data-driven control, we learn the solution map directly instead of explicitly learning the system model or its subspace representation. More specifically, we introduce the use of soft projections to approximate the true projector from noisy data, which is conceptually similarly to regularization in existing methods. Crucially, we provide rigorous bounds on the approximation error of these soft projections. The derived error bound reveals a clear trade-off between bias and variance, which can be tuned via a parameter similar to a regularization weight. Furthermore, this bound is completely independent of the true system order, thereby avoiding the sensitivity issues that come with explicit subspace estimates. The proposed perspective leads to conceptually novel control formulations, offering a new alternative to approaches that focus on designing interpretable regularization terms. Specifically, we propose two novel formulations: the first is a generalization of regularized data-enabled predictive control (DeePC), while the second is a more interpretable formulation that exhibits superior robust performance in a case study.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we provide efficient rank-one update formulas for soft projectors, allowing the control methods to seamlessly adapt new data online.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. Section II contains preliminaries on behavioral systems theory, orthogonal projections, and direct data-driven control. Soft projectors are analyzed in detail in Section III. We provide novel data-driven control formulations in Section IV, and describe the online updates of soft projectors in Section V. Finally, Section VI contains a case study.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Behavioral systems theory", "weight": 1.0} -->

For LTI systems, the restricted behavior, $\mathcal{B}_{L}$ is defined as and it is a shift-invariant subspace of the set of all possible trajectories. Let $n$ be the order of a minimal system realization. Then, for LTI systems and for large enough $L$, the restricted behavior $\mathcal{B}_{L}\subseteq\mathbb{R}^{qL}$ is a subspace of dimension $d=mL+n$. A basis for $\mathcal{B}_{L}$ can be constructed from a state-space representation or directly from sufficiently rich and noise free data for LTI behaviors. The restricted behavior fully specifies the behavior in case $L$ is larger than the lag of the system. We focus on the restricted behavior $\mathcal{B}_{L}$ and refer to it simply as the behavior in the remainder of the manuscript.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Orthogonal projections", "weight": 1.0} -->

Let $U\in\mathbb{R}^{qL\times d}$ be a matrix with full column rank. The orthogonal projector to the column space $\mathrm{col}(U)$ is The projector to the orthogonal complement of $\mathrm{col}(U)$ is $I-P_{U}$. Furthermore, $P_{U}=P_{U}^{\top}$ and $P_{U}^{2}=P_{U}$ hold. For two subspaces $\mathrm{col}(U_{1})$ and $\mathrm{col}(U_{2})$, the gap metric is defined as and it measures the largest principal angle between the subspaces. With other words, the gap metric quantifies the worst case error between the projection of a unit vector onto $\mathrm{col}(U_{1})$ and $\mathrm{col}(U_{2})$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-C Behavioral predictive control", "weight": 1.0} -->

We can use the behavioral framework to formulate a predictive control scheme as follows. At time $t$, consider $T_{\mathrm{ini}}$ greater than the lag and define $w_{\mathrm{ini}}=w_{t-T_{\mathrm{ini}}-1,t-1}$. We are interested in finding a finite input sequence, such that the future trajectory $w_{\mathrm{f}}=w_{t,t+T_{\mathrm{f}}-1}$ minimizes the control cost where $Q$ and $R$ are symmetric positive definite matrices, and $\|\cdot\|_{Q}$ denotes the 2-norm weighted by $Q$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-C Behavioral predictive control", "weight": 1.0} -->

The overall trajectory $w=\begin{bmatrix}w_{\mathrm{ini}}^{\top}&w_{\mathrm{f}}^{\top}\end{bmatrix}^{\top}\in\mathbb{R}^{qL}$ with $L=T_{\mathrm{ini}}+T_{\mathrm{f}}$ has to be consistent with the system behavior, which we write as $w\in\mathcal{B}_{L}$, with a slight abuse of notation. In practice, measurements are often corrupted by noise, and therefore, only a noisy estimate $\hat{w}_{\mathrm{ini}}$ of $w_{\mathrm{ini}}$ is available. To mitigate this, one can add $w_{\mathrm{ini}}$ to the problem as an optimization variable that has to be close (but not necessarily equal) to the measurement $\hat{w}_{\mathrm{ini}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-C Behavioral predictive control", "weight": 1.0} -->

Moreover, the trajectory must be in some convex set of constraints $\mathcal{C}$. Formalizing these requirements leads to the predictive control problem | | $\displaystyle\begin{split}\min_{w\in\mathcal{B}_{L}\cap\mathcal{C}}&\quad J(w_{\mathrm{f}})+\lambda_{\sigma}\|\sigma\|_{2}^{2},\\ | | \(1\) | | | \mathrm{s.t.}&\quad w_{\mathrm{ini}}=\hat{w}_{\mathrm{ini}}+\sigma.\end{split}$ | | | The controller is applied in receding horizon, i.e., once the problem is solved, we apply the first input $u_{t}$, and restart the process.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Behavioral predictive control", "weight": 1.0} -->

To highlight the connection between problem and projections, we substitute the constraint in the cost yielding where $w_{\mathrm{ref}}$ is the reference for $w_{\mathrm{f}}$ constructed from $u_{\mathrm{ref}}$ and $y_{\mathrm{ref}}$, and $W$ is a block diagonal symmetric positive definite weighting matrix with blocks built from $\lambda_{\sigma}I$, $Q$, and $R$. Problem is equivalent to the (weighted) projection of $\begin{bmatrix}\hat{w}_{\mathrm{ini}}^{\top}&w_{\mathrm{ref}}^{\top}\end{bmatrix}^{\top}$ onto the set $\mathcal{B}_{L}\cap\mathcal{C}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Behavioral predictive control", "weight": 1.0} -->

In case there are no constraints, i.e., $\mathcal{C}=\mathbb{R}^{qL}$, the solution can be simply expressed as where $B$ is a basis for the subspace $\mathcal{B}_{L}$, and $P_{B}^{W}:=B(B^{\top}WB)^{-1}B^{\top}$ is the projector onto $\mathcal{B}_{L}$ weighted by $W$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-D Data-driven predictive control", "weight": 1.0} -->

The control formulation requires the exact knowledge of the system behavior $\mathcal{B}_{L}$, which is often not available. In the remainder of the paper, we assume that the behavior is unknown, but $D\gg qL$ noisy trajectories $w^{\mathrm{d}}$ from $\mathcal{B}_{L}$ are available. We can arrange the measurements in a data matrix as The data matrix $H$ is a concatenation of two Hankel matrices, one for the inputs, and one for the outputs. With a slight abuse of notation, we permute the rows of $H$ in the subsequent control problems, so that the first $qT_{\mathrm{ini}}$ rows correspond to $w_{\mathrm{ini}}$, and the rest corresponds to $w_{\mathrm{f}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-D Data-driven predictive control", "weight": 1.0} -->

In the absence of constraints, the solution to can be expressed in closed form as a "softened" projection onto $\mathrm{col}(H)$, as shown below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Soft projections", "weight": 1.0} -->

Let us analyze the soft projector with $\delta>0$, defined as The unweighted soft projector with $W=I$ was introduced, and it is closely related to diagonal loading, which is a widely used technique in the signal processing literature. We denote the unweighted soft projector by $\tilde{P}_{H}:=\tilde{P}_{H}^{I}$ throughout the paper. We derive the results for $\tilde{P}_{H}^{W}$ for completeness, but often focus on $\tilde{P}_{H}$ to build intuition.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Soft projections", "weight": 1.0} -->

Computing $\tilde{P}_{H}^{W}$ as in involves inverting a $D$-by-$D$ matrix, which can be computationally restrictive. Using the matrix inversion lemma, $\tilde{P}_{H}^{W}$ can also be expressed as (cf.) This formulation only requires inverting an $qL$-by-$qL$ matrix, and thus, the computation does not scale with the data size.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Soft projections", "weight": 1.0} -->

As the constant $\delta\to 0$, the soft projector $\tilde{P}_{H}$ reduces to the orthogonal projector onto $\mathrm{col}(H)$, i.e., $\tilde{P}_{H}\to HH^{\dagger}=P_{H}$, where $\dagger$ denotes the Moore-Penrose inverse. In the noise-free case ($E=0$) we have that $\mathrm{col}(H)=\mathrm{col}(B)$, and thus, the soft projector recovers the true projection $P_{B}$ as $\delta\to 0$. Recall that the eigenvalues of an orthogonal projector are either 1 or 0. For $\delta>0$, however, the soft projector $\tilde{P}_{H}$ scales the singular values of $H$, denoted by $\sigma_{i}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Soft projections", "weight": 1.0} -->

The eigenvalues of $\tilde{P}_{H}$ are $0\leq\dfrac{\sigma_{i}^{2}}{\sigma_{i}^{2}+\delta}<1$, while the eigenvectors are the same as those of $HH^{\top}$. As $\delta$ increases, the larger $\sigma_{i}$ start to dominate in $\tilde{P}_{H}$, and the smaller $\sigma_{i}$ are suppressed. Thus, the soft projector "denoises" the data matrix $H$. Since all eigenvalues of $\tilde{P}_{H}$ are less than one, the soft projections are biased towards zero compared to the true projection $P_{B}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Introducing the soft projector $\tilde{P}_{H}$ was motivated by the solution to the DeePC problem with 2-norm regularization in Section II-D. In fact, the solution to DeePC in Lemma 1 can be expressed as $w^{\star}_{\mathrm{DeePC}}=\tilde{P}^{W}_{H}W\begin{bmatrix}\hat{w}_{\mathrm{ini}}^{\top}&w_{\mathrm{ref}}^{\top}\end{bmatrix}^{\top}$ with $\delta=\lambda_{g}$. In case the projected 2-norm regularizer is used, the soft projector becomes where the inverse exists, since $\mathrm{col}([Z_{p}^{\top}~U_{f}^{\top}]^{\top})\subseteq\mathrm{col}(H^{\top})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The projector $\hat{P}_{H}$ does not shrink vectors in the subspace $\mathrm{col}([Z_{p}^{\top}~U_{f}^{\top}])$, only in its orthogonal complement. In the following, we focus on the soft projector $\tilde{P}_{H}$, but similar arguments hold for $\hat{P}_{H}$. ∎

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Approximation error bounds", "weight": 1.0} -->

We now analyze the estimation error of the weighted soft projector. Motivated by the gap metric, we quantify the approximation error of the weighted soft projection by providing an upper bound on $\|\tilde{P}_{H}^{W}-P_{B}^{W}\|_{2}$ below. For the analysis, let us decompose the data matrix as $H=BS+E$, where $B\in\mathbb{R}^{qL\times d}$, $BB^{\top}=I$ is an orthonormal basis for the subspace $\mathcal{B}_{L}$. We interpret the term $BS$ as the nominal part of the data that is in the behavior, and $E$ is noise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

For unweighted soft projectors, the bound in Theorem 1 simplifies to Clearly, soft projectors are consistent in the sense that $\|\tilde{P}_{H}-P_{B}\|_{2}\to 0$ as $\|E\|_{2}\to 0$ and $\delta\to 0$, and the error bound changes smoothly with $\delta$. Importantly, the approximation error does not depend on the true dimension of $\mathcal{B}_{L}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2", "weight": 1.0} -->

This is in contrast with the approach to data-driven control in the behavioral setting that explicitly estimates $\mathcal{B}_{L}$ as a low-dimensional subspace from data. If the estimated subspace and $\mathcal{B}_{L}$ and are of different dimensions, the gap metric is 1, meaning that the estimate can be arbitrarily bad. Hence, this approach is sensitive to order selection, which is a major limitation. ∎

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data-driven control using soft projections", "weight": 1.0} -->

The solution of can only be interpreted through a soft projection in the unconstrained case, i.e., when $\mathcal{C}=\mathbb{R}^{qL}$. In this section, we propose a novel approach to approximately enforce the constraint $w\in\mathcal{B}_{L}$ in the behavioral control problem. If a basis $B$ for the behavior is known, the constraint $w\in\mathcal{B}_{L}$ can be written as $(I-P_{B})w=0$. However, this constraint for the soft projector only holds if $w=0$ in general. To address this issue in the data-driven case, we lift the approximated constraint into the cost, leading to the following convex problem In the above formulation, $\alpha$ is a tuning parameter that controls how strong the approximation of the constraint $w\in\mathcal{B}_{L}$ is enforced. Furthermore, $\delta$ in $\tilde{P}_{H}$ controls how much the data is "denoised" by softening the projection.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data-driven control using soft projections", "weight": 1.0} -->

Note that if the data is noise-free and persistently exciting, $\tilde{P}_{H}\to P_{B}$ as $\delta\to 0$, and thus, reduces to as $\alpha\to\infty$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Data-driven control using soft projections", "weight": 1.0} -->

For orthogonal projectors, it holds that $(I-P_{B})^{2}=I-P_{B}$, leading to $\|(I-P_{B})w\|^{2}=w^{\top}(I-P_{B})w$. However, this is not true for the soft projector $\tilde{P}_{H}$. Thus, approximating the constraint $w\in\mathcal{B}_{L}$ by penalizing $w^{\top}(I-\tilde{P}_{H})w$ gives rise to the alternative control problem We scaled the tuning parameter $\hat{\alpha}$ by $\delta$ to highlight the connection between problem and DeePC in the unconstrained case, as formalized below.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Comparison of the proposed control formulations", "weight": 1.0} -->

Recall that the solution to in the unconstrained case is $w^{\star}_{\mathcal{B}}=P_{B}^{W}W\begin{bmatrix}\hat{w}_{\mathrm{ini}}^{\top}&w_{\mathrm{ref}}^{\top}\end{bmatrix}^{\top}$. The matrix $P_{B}^{W}W$ mapping the desired trajectory to the solution is low rank, reflecting that any feasible trajectory lies in the low-dimensional subspace $\mathcal{B}_{L}$. When the solution is estimated from noisy data through soft projections, the low rank structure is destroyed. Yet, the separation of the eigenvalues is desired to approximate the solution to well. As we established in Section III, the eigenvalues of the soft projector can be filtered by tuning the parameter $\delta$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Comparison of the proposed control formulations", "weight": 1.0} -->

Intuitively speaking, the term $(I-\tilde{P}_{H})^{2}$ in acts as a higher order filter that can separate the signal from noise in $H$ better than $(I-\tilde{P}_{H})$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Comparison of the proposed control formulations", "weight": 1.0} -->

We illustrate this difference by analyzing the simple case when $\mathcal{C}=\mathbb{R}^{qL}$ and $W=I$. The proposed formulations and boil down to regularized least-squares problems, whose solution can be expressed in closed-from as $M_{eq:indicator_approx_squared}\begin{bmatrix}\hat{w}_{\mathrm{ini}}^{\top}&w_{\mathrm{ref}}^{\top}\end{bmatrix}^{\top}$ and $M_{eq:indicator_approx}\begin{bmatrix}\hat{w}_{\mathrm{ini}}^{\top}&w_{\mathrm{ref}}^{\top}\end{bmatrix}^{\top}$, respectively, where The eigenvalues of the maps are where $\sigma_{i}$ are the singular values of $H$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Comparison of the proposed control formulations", "weight": 1.0} -->

Figure 1 displays the eigenvalues for $\sigma_{i}=\{1000,100,50,30,20\}$ and $\alpha=\hat{\alpha}/\delta=10^{6}$ as a function of $\delta$. Interpreting $(I-\tilde{P}_{H})^{2}$ as a second order filter, we see that the eigenvalues of $M_{eq:indicator_approx_squared}$ are separated more clearly. This provides the intuition that formulation is more robust to noise than formulation. In Section VI, we present a case study empirically confirming that this is indeed the case. A comprehensive analysis of the differences between and is subject of future work.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Online data-driven control", "weight": 1.0} -->

A major benefit of using soft projections is the ease of incorporating online (new) data into data-driven control methods that are usually formulated with offline data. The continuous adaptation of these methods is essential in many application domains, as real-world dynamical systems often change over time. Furthermore, adapting the estimated projection onto the linear behavior $\mathcal{B}_{L}$ is particularly important because nonlinear systems can be effectively over-approximated as linear time-varying systems.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Online data-driven control", "weight": 1.0} -->

Consider the scenario where the data matrix in includes all trajectories observed up to the current time $t$, denoted as While this time-varying matrix can be directly incorporated into the data-driven control problems or, such a naive implementation presents two primary challenges. First, it is computationally inefficient because the problem size in scales with the number of columns in $H_{t}$, or the soft projector $\tilde{P}_{H_{t}}^{W}$ in formulations and would need to be recomputed at every time step. Second, the appropriate selection of parameters $\lambda_{g}$ or $\delta$ depends directly on the current data matrix $H_{t}$ to achieve a favorable bias-variance trade-off (cf. Theorem 1). Since $H_{t}$ evolves as new data is collected, it is necessary to re-tune the parameter to maintain good performance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Online data-driven control", "weight": 1.0} -->

To address these challenges, we develop efficient update formulas for both the soft projector $\tilde{P}^{W}_{H_{t}}$ and the tuning parameter $\delta_{t}$. This enables direct tracking of the unconstrained DeePC solution and allows the novel formulations from Section IV to be adapted online. Inspired, we present an efficient rank-one update for the weighted soft projector below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Case study", "weight": 1.0} -->

We consider the double spring-mass-damper system from consisting of two rotating discs. The MATLAB code reproducing the results is available online^11^1 The angle and angular velocity of the two disks are the states, and the outputs are the two angles. The input is the torque on the first disk. Disturbance acts on the system in the form of torques on both disks, which are modeled as zero mean white noise. The length of the initial and future trajectories are chosen as $T_{\mathrm{ini}}=2$ and $T_{\mathrm{f}}=12$. The objective is to track the reference at $\begin{bmatrix}0.8&0.8\end{bmatrix}^{\top}$, starting from zero initial state.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Case study", "weight": 1.0} -->

The constraints are $\begin{bmatrix}-1&-1\end{bmatrix}^{\top}\leq y_{k}\leq\begin{bmatrix}1&1\end{bmatrix}^{\top}$ and $-2\leq u_{k}\leq 2$ for all $k=t,\dots,t+T_{\mathrm{f}}-1$. We build the data matrix $H$ by simulating the system for $1000$ steps starting from zero initial state and applying zero mean white noise as input. The weights in the cost are $Q=I,~R=0.01\cdot I,\lambda_{\sigma}=10^{6}$, and $\alpha=10^{6}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Case study", "weight": 1.0} -->

We compare the open-loop predictions obtained by solving DeePC and. The performance of problem was similar to that of DeePC, and therefore, we do not include it here. The parameters $\lambda_{g}$ and $\delta$ are tuned through validation from the intervals $[10,10^{7}]$ and $[10^{-3},10^{3}]$, respectively. The open-loop prediction error and realized cost during validation are plotted in Figure 2 as the function of $\lambda_{g}$ (or $\delta$ for ). We choose $\lambda_{g}=54.29$ and $\delta=0.091$, as these values achieve the lowest open-loop cost on the validation set. With the validated parameter values, the predicted trajectories are tested for both methods. Both the validation and the testing was performed under a 100 noise realizations. The whole experiment was repeated for signal-to-noise ratios (SNR) 10, 5, and 3. Table I shows the mean realized open-loop cost and the prediction error statistics for different SNR levels.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Case study", "weight": 1.0} -->

It can be seen in Figure 2 that the parameter $\lambda_{g}$ trades off prediction accuracy versus realized cost for DeePC. On the other hand, both the prediction error and the realized cost are minimized roughly on the same interval around $[10^{-2},1]$ for the proposed method. Both the validation curves in Figure 2 and the results in Table I show that the proposed method achieves superior performance compared to DeePC. As the signal-to-noise ratio shrinks, the difference between the mean realized costs grows, suggesting that overperforms DeePC due to its increased robustness. mean pred. err. pred. err. variance TABLE I: Realized open-loop cost and prediction error statistics for DeePC and the proposed method.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced the use of soft projectors to approximate the true behavioral projector directly from noisy data, providing an alternative to regularization in direct data-driven predictive control. We established a rigorous bound on the approximation error that highlights a clear bias-variance trade-off and, importantly, remains independent of the underlying system order. Building upon these theoretical insights, we developed intuitive generalizations of regularized DeePC schemes that demonstrated superior performance in our simulated case study. Finally, we derived efficient update formulas for the soft projectors, providing a computationally practical approach for adapting these control methods online with streaming data. Future work includes investigating further approaches to approximate the behavioral projection and their interpretation in the stochastic setting.
