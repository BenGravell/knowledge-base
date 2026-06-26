<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite Sample Analysis for a Class of Subspace Identification Methods

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While subspace identification methods (SIMs) are appealing due to their simple parameterization for MIMO systems and robust numerical realizations, a comprehensive statistical analysis of SIMs remains an open problem, especially in the non-asymptotic regime. In this work, we provide a finite sample analysis for a class of SIMs, which reveals that the convergence rates for estimating Markov parameters and system matrices are O(1/sqrt(N)), in line with classical asymptotic results. Based on the observation that the model format in classical SIMs becomes non-causal because of a projection step, we choose a parsimonious SIM that bypasses the projection step and strictly enforces a causal model to facilitate the analysis, where a bank of ARX models are estimated in parallel. Leveraging recent results from finite sample analysis of an individual ARX model, we obtain an overall error bound of an array of ARX models and proceed to derive error bounds for system matrices via robustness results for the singular value decomposition.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Originating from the celebrated Ho-Kalman algorithm, subspace identification methods (SIMs) have proven extremely useful for estimating linear state-space models. Over the past 50 years, numerous efforts have been made to develop improved algorithms and gain a deeper understanding of the family of SIMs, exemplified by the successful narrative of closed-loop identification. For a comprehensive overview of SIMs, we refer to. Despite their tremendous success both in theory and practice, several drawbacks have been recognized, including a lower accuracy compared to prediction error methods (PEMs) and an incomplete statistical analysis. There are some significant contributions to statistical properties of SIMs in the asymptotic regime. The consistency of open-loop and closed-loop SIMs is analyzed in and, respectively, where the former suggests that persistence of excitation (PE) of the input signals is not sufficient for consistency, and stronger conditions are required in some cases. The asymptotic variance of SIMs is discussed. Furthermore, the asymptotic equivalence of some SIMs is discussed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regarding the optimality, although the canonical variate analysis (CVA) method is stated to be optimal when measured inputs are white, simulation studies indicate that it is not asymptotically efficient, as it does not reach Cramér-Rao lower bound (CRLB). In short, SIMs are generally consistent, however, the question of whether there are SIMs that are asymptotically efficient remains unresolved. Besides, although some of the methods are asymptotically equivalent, their performance differs in finite sample setups. Meanwhile, it is difficult to capture their transient behaviors using the asymptotic theory. Therefore, a complete statistical analysis and comparison among various SIMs, as well as the pursuit of an efficient SIM are still open problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has been a recent resurgence of interest in identifying state-space models for dynamic systems, where the focus is on the non-asymptotic regime. Finite sample analysis in the field of system identification was pioneered, where the performance of PEMs were analyzed. Over the last few years, a series of papers have revisited this topic and introduced many promising developments on fully observed systems and partially observed systems. For a broader overview of these results, we refer to. As pointed out, finite sample analysis has been a standard tool for comparing algorithms in the non-asymptotic regime. It is expected that such analysis of SIMs will not only provide a detailed qualitative characterization of learning complexity and error bounds, but also bring more insights into the comparison of different SIMs regarding optimality, the selection of past and future horizons, and the design of controllers. Broadly speaking, an analysis in the non-asymptotic regime brings a wider understanding of SIMs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the auspicious future, the path of finite sample analysis for SIMs proves to be challenging. Usually, multi-step statistical operations are involved in SIMs, including pre-estimation, projection, weighted singular value decomposition (SVD) and maximum likelihood (ML) estimation. While these steps enhance performance, they simultaneously complicate the model and pose challenges for statistical analysis. To the best of our knowledge, except for a finite sample analysis of the Ho-Kalman algorithm, a stochastic SIM in the absence of input signals and an individual ARX model, a finite sample analysis of classical SIMs in the presence of inputs is still unavailable. Compared with SIMs without taking account of measured inputs, the inclusion of inputs results in a higher complexity due to the presence of an unknown block matrix with a lower-triangular Toeplitz structure. This matrix is responsible for recording the impact of 'future' input on 'future' output. To manage this complexity, classical SIMs choose to remove this matrix via a projection step. Although this method is computationally efficient, it makes the model format non-causal anymore and poses challenges for statistical analysis.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, we propose to use a parallel and parsimonious SIM, namely PARSIM, which bypasses the projection step and strictly enforces a causal model to facilitate the analysis. Except the projection step, PARSIM aligns with the unified framework of the family of SIMs in all other aspects, opting for PARSIM will not constrain our comprehension of the full panorama of SIMs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this paper are: We leverage recent results from finite sample analysis of an individual ARX model to obtain an error bound for the bank of ARX models featured in PARSIM. Our analysis reveals that the convergence rates for estimating Markov parameters and system matrices are $\mathcal{O}{({1/\sqrt{N}})}$ even in the presence of inputs, which is in line with classical asymptotics.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method can be extended to the class of SIMs that estimate an array of ARX models, for instance, the included PARSIM and SIMs based on predictor identification (PBSID). Therefore, it paves the way for comprehensively understanding the broader landscape of SIMs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The disposition of the paper is as follows: A short review of SIMs with the focus on PARSIM is given in Section II, and the problem as well as the roadmap ahead to analyze its finite sample behavior are described at the end of Section II. The finite sample analysis of an individual ARX model is summarized in Section III. An overall error bound for a bank of ARX models and the resulting error bounds of the system matrices are given in Section IV. Finally, some discussions and future work are provided in Section V.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations: For a matrix $X$ with appropriate dimensions, $X^{\top}$, $X^{- 1}$, $X^{1/2}$, $X^{\dagger}$, $\parallel X\parallel$, $\det{(X)}$, $\rho{(X)}$, $\lambda_{\max}{(X)}$, $\lambda_{\min}{(X)}$ and $\sigma_{n}{(X)}$ denote its transpose, inverse, square root, Moore-Penrose pseudo-inverse, spectral norm, determinant, spectral radius, maximum eigenvalue, minimum eigenvalue and $n -$th largest singular value, respectively. $X \succ {( \succcurlyeq )}$ $0$ means that $X$ is positive (semi) definite. The matrices $I$ and $0$ are the identity and zero matrices with compatible dimensions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The multivariate normal distribution with mean $\mu$ and covariance $\Sigma$ is denoted as $\mathcal{N}{(\mu,\Sigma)}$. The notation ${\mathbb{E}}x$ is the expectation of a random vector $x$, and ${\mathbb{P}}{(\mathcal{E})}$ is the probability of the event $\mathcal{E}$. $\mathcal{E}^{c}$ is the complementary event of $\mathcal{E}$, and $\mathcal{E}_{1} \cup \mathcal{E}_{2}$ and $\mathcal{E}_{1} \cap \mathcal{E}_{2}$ are the union and intersection of events $\mathcal{E}_{1}$ and $\mathcal{E}_{2}$, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Model and Assumptions", "weight": 1.0} -->

Consider the following discrete-time linear time-invariant (LTI) system on innovations form: where $x_{t} \in {\mathbb{R}}^{n_{x}}$, $u_{t} \in {\mathbb{R}}^{n_{u}}$, $y_{t} \in {\mathbb{R}}^{n_{y}}$ and $e_{t} \in {\mathbb{R}}^{n_{y}}$ are the state, input, output and innovations, respectively. For brevity of notation, we assume that the initial time starts at $k = 1$, and the initial state is $x_{1} = 0$. It has been widely recognized that under mild conditions, the above innovations model describes the same input-output trajectories with identical statistics as a standard state-space model. Thus, without loss of generality, we study the innovations model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption II.1", "weight": 1.0} -->

The system is minimal, i.e., $(A,{\lbrack B,K\rbrack})$ is controllable and $(A,C)$ is observable, and the system order $n_{x}$ is known to the user.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption II.1", "weight": 1.0} -->

The innovations $\{ e_{k}\}$ consists of independent and identically distributed (i.i.d.) Gaussian random variables, i.e., $e_{k} \sim {\mathcal{N}{(0,{\sigma_{e}^{2}I})}}$.^11^1We believe that our results can be extended to more general setups, for instance, sub-Gaussians.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

Here we provide a short review of SIMs, with a focus on PARSIM. An extended state-space model for can be derived as where $f$ and $p$ denote future and past horizons chosen by the user, respectively. The extended observability matrix is and $G_{f}$ with $H_{f}$ are lower-triangular Toeplitz matrices of Markov parameters with respect to the input and innovations, Past and future inputs are collected in the Hankel matrices Similar definitions are given for matrices $\Gamma_{p}$, $G_{p}$, $H_{p}$, $Y_{p}$, $Y_{f}$, $E_{p}$ and $E_{f}$. Usually, we take $k = {p + 1}$, and then the total number of samples is denoted as $\overline{N} = {{p + f + N} - 1}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

The state sequences are defined as Furthermore, by replacing $e_{k}$ with $y_{k} - {Cx_{k}}$ in (1a) and iterating the equation, we obtain the relation where $A_{c} = {A - {KC}}$, $Z_{p} = \begin{bmatrix} \end{bmatrix}^{\top}$, and $L_{p}$ is the extended controllability matrix defined as After substituting into (2a), we have Most SIMs use to first estimate either the extended observability matrix $\Gamma_{f}$ or system state $X_{k}$, and then obtain a realization of the system matrices up to a similarity transformation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

To illustrate, since $G_{f}$ is a lower-triangular Toeplitz matrix recording the effect of $U_{f}$ on $Y_{f}$, and it is difficult to preserve such structure with least-squares, what classical SIMs do is to eliminate this term by projecting out $U_{f}$ as where $\Pi_{U_{f}}^{\perp} = {I - {U_{f}^{\top}{({U_{f}U_{f}^{\top}})}^{- 1}U_{f}}}$. Then the above equation is simplified based on the following observations: When $p$ is sufficiently large, we have ${\overline{A}}^{p} \approx 0$. Also, as $U_{f}$ is uncorrelated with $E_{f}$, we have ${E_{f}\Pi_{U_{f}}^{\perp}} \approx E_{f}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

Furthermore, $E_{f}$ is uncorrelated with $Z_{p}$, i.e., ${\frac{1}{N}E_{f}Z_{p}^{\top}} \approx 0$. By multiplying $Z_{p}^{\top}$ on both sides of we have Then the range space of the extended observability matrix $\Gamma_{f}$ can be estimated using To recover the extended observability matrix $\Gamma_{f}$ or the state $X_{k}$, weighted SVD is often used, i.e., where ${\hat{\Lambda}}_{1}$ contains the $n_{x}$ largest singular values.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

In this way, a balanced realization of ${\hat{\Gamma}}_{f}$ or ${\hat{L}}_{p}$ is Different choices of weighting matrices $W_{1}$ and $W_{2}$ lead to distinct classical SIMs. As pointed out, one of the main issues of those classical SIMs is that the model is not causal anymore due to the absence of $G_{f}$. As a result, the estimated parameters have inflated variance due to the existence of unnecessary and extra terms. Furthermore, this poses a challenge in analyzing statistical properties, which we will see later in detail.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

To enforce causal models, a parallel and parsimonious SIM, PARSIM, is proposed. Instead of doing the projection step in once, PARSIM zooms into each row of and equivalently performs $f$ ordinary least-squares (OLS) to estimate a bank of ARX models. To illustrate this, the extended state-space model can be partitioned row-wise as where $i = {1,2,{\ldots f}}$, and Then PARSIM uses OLS to estimate each $\Gamma_{fi}L_{p}$ and $G_{fi}$ simultaneously from the causal model: At last, the whole estimate of $\Gamma_{f}L_{p}$ is obtained by stacking the $f$ estimates together as Comparing with classical SIMs that only estimate $\Gamma_{f}L_{p}$, PARSIM estimates $\Gamma_{f}L_{p}$ and Markov parameters $G_{fi}$ simultaneously. In this way, the lower-triangular Toeplitz structure of $G_{f}$ is preserved and the causality is strictly enforced.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

Furthermore, it has been shown that the above algorithm gives a smaller variance of $\hat{\Gamma_{f}⁢L_{p}}$ than classical SIMs in the asymptotic regime. For the subsequent realization step, PARSIM goes back to the weighted SVD step.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B A Recap of PARSIM", "weight": 1.0} -->

In this paper, we consider a simplified implementation of the original PARSIM, i.e., we choose the weighting matrices $W_{1} = I$ and $W_{2} = I$, and the system matrices are obtained in the following way: where $\underset{¯}{I} = \begin{bmatrix} \end{bmatrix}$, $\overline{I} = \begin{bmatrix} \end{bmatrix}$ and the indexing of matrices follows MATLAB syntax.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Problem and Roadmap Ahead", "weight": 1.0} -->

Now we define the problem explicitly and sketch the path ahead to its solution. Under Assumption II.1, given a finite number $\overline{N}$ of input-output samples and horizons $f$ and $p$, we aim to provide error bounds with high probability for the realization. To be specific, with probability at least $1 - \delta$, we wish to establish the following error bounds explicitly: where $T$ is a non-singular matrix.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1", "weight": 1.0} -->

It is only possible to obtain the system matrices up to a similarity transformation due to the non-uniqueness of the realization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We arrive at this result by a two-step procedure. In Step 1, we derive an error bound for ${\hat{\theta}}_{i}$ in for every ARX model. In other words, we define the event and require that ${{\mathbb{P}}{(\mathcal{E}_{i}^{c})}} \leq {\delta/f}$ for $i = {1,2,\ldots,f}$. In Step 2, we first utilize a norm inequality between the block matrix $\hat{\Gamma_{f}⁢L_{p}}$ and its sub-matrices $\hat{\Gamma_{f⁢i}⁢L_{p}}$ to obtain the total error bound of $\hat{\Gamma_{f}⁢L_{p}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Finite Sample Analysis of each ARX Model", "weight": 1.0} -->

Following our roadmap, we formalize Step 1 above in this section. We emphasize that the results presented in this section apply to $i = {1,2,\ldots,f}$, with the acknowledgment of their reliance on the specific value of $i$. This dependency is underscored through the use of the subscript $i$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Finite Sample Analysis of each ARX Model", "weight": 1.0} -->

For brevity, we define a covariate so the error of the OLS estimate can be written as There are two types of errors, namely, the stochastic error ${\overset{\sim}{\theta}}_{i}^{S}$ and truncation bias ${\overset{\sim}{\theta}}_{i}^{B}$. The key observation is that the future innovations $e_{i}{(k)}$ are independent of the covariate $z_{p,i}{(l)}$ for all $l < k$, due to the fact that $z_{p,i}{(l)}$ consists of the past output, past input and future input. This provides a martingale structure, which is convenient to analyze.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Finite Sample Analysis of each ARX Model", "weight": 1.0} -->

By contrast, if we revisit the classical SIMs, the stochastic error for the estimate will be $E_{f}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}{({Z_{p}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}})}^{- 1}$. Due to the projection matrix $\Pi_{U_{f}}^{\perp}$, the columns of $E_{f}$ and $Z_{p}$ are mixed together, making the above term non-causal, resulting in the loss of the martingale structure. We believe that this is one of the main barriers preventing a finite sample analysis for classical SIMs, which is also the reason why we choose PARSIM that bypasses the projection step.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Finite Sample Analysis of each ARX Model", "weight": 1.0} -->

Before proceeding further, we have the following definitions regarding the covariance and empirical covariance of the covariant $z_{p,i}{(k)}$: For simplicity, with a slight abuse of notation, we use $\Sigma_{i,k} = {\Sigma_{p,i}{(k)}}$ and ${\hat{\Sigma}}_{i,N} = {{\hat{\Sigma}}_{p,i}{(N)}}$, where the dependency of covariance on the past horizon $p$ is concealed. Also, the covariance of the state $x_{k}$ is defined similarly as In this way, the stochastic error ${\overset{\sim}{\theta}}_{i}^{S}$ can be rewritten as To bound the above term, we use a self-normalized martingale to deal with the leftmost term in the bracket.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Finite Sample Analysis of each ARX Model", "weight": 1.0} -->

As for ${\hat{\Sigma}}_{i,N}^{- {1/2}}$, we use recent results from the smallest eigenvalue of the empirical covariance of causal Gaussian processes to bound it, which establish the condition of PE.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Persistence of Excitation", "weight": 1.0} -->

First, we make the following assumption regarding the selection of the past horizon $p$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption III.1", "weight": 1.0} -->

The past horizon is chosen as $p = {\beta\text{log}N}$, where $\beta$ is large enough such that

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The above assumption ensures that the truncation bias $\Gamma_{fi}A_{c}^{p}x_{k}$ is small enough, allowing the model to closely approximate an ARX model. To achieve this goal, the exponentially decaying term $A_{c}^{p}$ should counteract the magnitude of the state $x_{k}$. Since $A$ is marginally stable, $x_{k}$ scales at most polynomially with $k$. Hence, the state norm $\left. \parallel\Sigma_{x,N}\parallel \right.$ grows at most polynomially with $N$. Since ${\rho{(A_{c})}} < 1$, we have $\left. \parallel A_{c}^{p}\parallel \right. = {\mathcal{O}{(\rho^{p})}}$ for some $\rho > {\rho{(A_{c})}}$. Taking $p = {\beta\text{log}N}$, we have $\left.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

PE is equivalent to requiring that the empirical covariance ${\hat{\Sigma}}_{i,N}$ is positive definite. For this purpose, the number of samples $N$ should exceed a certain threshold, namely, burn-in time $N_{pe}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3", "weight": 1.0} -->

To show that the above definition is not vacuous, we need to demonstrate that the condition $N \geq {N_{0}{(N,\delta,\beta,i)}}$ is feasible. For any given $\beta$, $\tau_{i}$ increases logarithmically with $N$. Also, $\left. \parallel\Sigma_{i,N}\parallel \right.^{2}$ grows polynomially with $N$, hence, the system theoretic term $\text{log}C_{\text{sys}}{(N,\tau_{i})}$ increases at most logarithmically with $N$. As a result, $N_{0}{(N,\delta,\beta,i)}$ grows polynomially with $N$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 4", "weight": 1.0} -->

According to the Schur complement, this is equivalent to which is essentially same as PE in Lemma 1 by taking $i = f$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Stochastic Error", "weight": 1.0} -->

The bound of the stochastic error ${\overset{\sim}{\theta}}_{i}^{S}$ is based on the following three events: where ${{\mathbb{P}}{(\mathcal{E}_{i,j}^{c})}} \leq {\delta/3}$ for $j = {1,2,3}$. The event $\mathcal{E}_{i,1}$ is due to PE in Lemma 1, the event $\mathcal{E}_{i,2}$ is derived from the matrix Markov inequality, and the event $\mathcal{E}_{i,3}$ is based on the result of self-normalized martingales. The signal-to-noise ratio (SNR) is defined as and is assumed to be uniformly lower bounded for all possible $p$, which has been proven to be a quite general assumption.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Truncation Bias Term", "weight": 1.0} -->

As for the bias term ${\overset{\sim}{\theta}}_{i}^{B}$, we will see that it is dominated by the stochastic error ${\overset{\sim}{\theta}}_{i}^{S}$, given a proper selection of $p$ and the fact that the system is stable.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robustness of Balanced Realization", "weight": 1.0} -->

Following our roadmap, having obtained error bounds for each ARX model in Step 1, now we move to Step 2 and provide the overall bound for and error bounds for the balanced realization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Bounds on System Matrices", "weight": 1.0} -->

Assume that we know the true value of $\Gamma_{f}L_{p}$, and the SVD of $\Gamma_{f}L_{p}$ is so a balanced realization for $\Gamma_{f}$ and $L_{p}$ is Moreover, the system matrices with respect to a similarity transform are obtained according to, which are denoted as $\left\{ \overline{A},\overline{B},\overline{C},\overline{K} \right\}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

This paper presents a finite sample analysis of a parsimonious SIM that estimates a bank of ARX models using OLS in parallel. It reveals that the convergence rates for estimating Markov parameters and system matrices are $\mathcal{O}{({1/\sqrt{N}})}$, consistent with classical asymptotic results. Besides, PE and the role of past horizon are also discussed. Although the algorithm studied in this paper streamlines the weighted SVD and realization steps, we believe that the findings herein pave the way for comprehensively grasping the broader landscape of the family of SIMs. Here are a few aspects we would like to discuss: Our bound is not tight: Just like the existing bounds for partially observed systems, our bound is not tight, either. In this paper, PE in the $f$ ARX models are dealt with separately, which is convenient but somewhat conservative, given that the past output and input $Z_{p}$ is reused for every estimation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Our bound can be further optimized; however, akin to the challenge of finding an efficient SIM in the asymptotic regime, the pursuit of a lower bound in the non-saymptotic regime for partially observed systems is more challenging.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Selection of past and future horizons: A similar suggestion as other work is given on the selection of the past horizon $p$, however, the guidance for the future horizon $f$ is not given. While it is evident that $f$ influences the error bound, a comprehensive analysis of its impact is not given. Using asymptotic theory, it has been shown that the variance of the estimates of the CVA method improves as $f$ increases, thus, it is interesting to study the impact of $f$ in the non-asymptotic regime.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Comparison between different weighting matrices: We consider a simplified SIM, i.e., taking the weighting matrices $W_{1} = W_{2} = I$. It is generally believed that the optimal choices usually depend on specific data sets, like the CVA method. In the future, we will analyze the influence of different weighting matrices on the realization step. As we remark in the persistence of excitation, our work provides some preliminary insights on the validity of existing weighting matrices.
