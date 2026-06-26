<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite Sample Analysis of Open-loop Subspace Identification Methods

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Subspace identification methods (SIMs) are known for their simple parameterization for MIMO systems and robust numerical properties. However, a comprehensive statistical analysis of SIMs remains an open problem. Following a three-step procedure generally used in SIMs, this work presents a finite sample analysis for open-loop SIMs. In Step 1 we begin with a parsimonious SIM. Leveraging a recent analysis of an individual ARX model, we obtain a union error bound for a Hankel-like matrix constructed from a bank of ARX models. Step 2 involves model reduction via weighted singular value decomposition (SVD), where we use robustness results for SVD to obtain error bounds on extended controllability and observability matrices, respectively. The final Step 3 focuses on deriving error bounds for system matrices, where two different realization algorithms, the MOESP type and the CVA type, are studied. Our results not only agree with classical asymptotic results, but also show how much data is needed to guarantee a desired error bound with high probability. The proposed method generalizes related finite sample analyses and applies broadly to many variants of SIMs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Originating from the celebrated Ho-Kalman algorithm, subspace identification methods (SIMs) have proven extremely useful for estimating linear state-space models and became one of the mainstream approaches in system identification. Over the past 50 years, numerous efforts have been made to develop improved algorithms and gain a deeper understanding of them. For a comprehensive overview of SIMs, we refer to. Overall speaking, SIMs can be categorized into two types, namely, the open-loop and closed-loop. Open-loop SIMs were developed first and formed the basis for the development of closed-loop ones. Some representative open-loop SIMs are canonical variate analysis (CVA), numerical algorithms for subspace state-space system identification (N4SID), multivariable output-error state-space (MOESP) algorithms, the observer-Kalman filter method (OKID), and the parsimonious SIM (PARSIM). Despite the significant theoretical and practical success of SIMs, certain limitations remain--most notably, their lower accuracy compared to the prediction error method (PEM) in the case of exogenous inputs being present, and the lack of a comprehensive statistical analysis.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A thorough statistical analysis of SIMs is essential to establish their reliability, assess their performance, and guide the design of more robust and efficient algorithms and the choice of user choices.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

The main contributions of this paper are three-fold: \(1\) We develop a robust and scalable framework for finite sample analysis of a broad class of SIMs. To avoid non-causal models caused by the projection step in classical SIMs, we propose to use PARSIM to enforce a causal model. Such a choice brings convenience to statistical analysis, and the method can be applied to other ARX-based SIMs, such as SSARX and PBSID.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

\(2\) We establish a more general PE condition. Compared with related studies that only include past inputs and past outputs as regressors, our work also includes future inputs as regressors, leading to a more general PE condition. This broader PE condition is instrumental in deriving error bounds and in analyzing the use of data-dependent weighting matrices. Therefore, it serves as a contribution of independent interest.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

\(3\) Compared with related studies that streamline the realization algorithm, we provide the first finite sample upper bounds on system matrices under different weighting matrices and two popular realization algorithms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

A preliminary version of this work was accepted by IEEE, where we provide a finite sample analysis for a simplified PARSIM, i.e., without taking into account the weighting matrices and including the CVA type realization algorithm. In this full version, we include different weighting matrices and two popular realization algorithms. In addition, we also provide complete proofs and a technical framework to approach this problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Structure", "weight": 1.0} -->

The disposition of the paper is as follows: In Section 2, we introduce models and assumptions used in SIMs, and then formulate the problem explicitly. In Section 3, we present a short review of SIMs with a focus on PARSIM, and the roadmap ahead to analyze its finite sample behavior. In Section 4, we first provide a finite sample analysis of an individual ARX model, which we then combine with a union bound to control the performance of a bank of ARX models. In Section 5, we first analyze certain robustness properties of weighted SVD, and then derive error bounds on the system matrices coming from two realization algorithms. In Section 6, we discuss the implications of our main results. Finally, the paper is concluded in Section 7. All proofs and technical lemmas are provided in the Appendix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Notations", "weight": 1.0} -->

\(1\) For a matrix $X$ with appropriate dimensions, $X^{\top}$, $X^{-1}$, $X^{\frac{1}{2}}$, $X^{\dagger}$, $\lVert X\rVert$, $\lVert X\rVert_{F}$, ${\rm{det}}(X)$, ${\rm{rank}}(X)$, ${\rm{trace}}(X)$, $\rho(X)$, $\lambda_{\rm{max}}(X)$, $\lambda_{\rm{min}}(X)$, $\sigma_{\rm{min}}(X)$ and $\sigma_{n}(X)$ denote its transpose, inverse, square root, Moore-Penrose pseudo-inverse, spectral norm, Frobenius norm, determinant, rank, trace, spectral radius, maximum eigenvalue, minimum eigenvalue, minimum singular value and $n$-th largest singular value, respectively.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Notations", "weight": 1.0} -->

Moreover, $X_{1}\succ(\succcurlyeq)$ $0$ and $X_{2}\prec(\preccurlyeq)$ $0$ mean that $X_{1}$ is positive (semi) definite and $X_{2}$ is negative (semi) definite, respectively. ${\rm{diag}}(X_{1},X_{2})$ is a block matrix having $X_{1}$ and $X_{2}$ on its diagonal. The matrices $I$ and $0$ are the identity and zero matrices with compatible dimensions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Notations", "weight": 1.0} -->

\(s\) The multivariate normal distribution with mean $\mu$ and covariance $\Sigma$ is denoted as $\mathcal{N}(\mu,\Sigma)$. The notation $\mathbb{E}\left[x\right]$ is the expectation of a random vector $x$. For an event $\mathcal{E}$, $\mathbb{P}(\mathcal{E})$ is the probability of $\mathcal{E}$, $\mathcal{E}^{c}$ is the complementary event of $\mathcal{E}$, and $\mathcal{E}_{1}\cup\mathcal{E}_{2}$ and $\mathcal{E}_{1}\cap\mathcal{E}_{2}$ are the union and intersection of events $\mathcal{E}_{1}$ and $\mathcal{E}_{2}$, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations", "weight": 1.0} -->

\(3\) The notation $f=\mathcal{O}(g)$ means that functions $f,g\in\mathbb{R}^{d}$ satisfy $\limsup_{x\to x_{0}}{|\frac{f(x)}{g(x)}|}<\infty$, where the limit point $x_{0}$ is typically understood from the context. Moreover, $f\gtrsim g$ means $f$ is greater than or approximately equal to $g$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations", "weight": 1.0} -->

\(4\) The notations $c$, $c_{1}$,... stand for universal constants independent of system parameters, confidence, and accuracy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Models and Assumptions", "weight": 1.0} -->

Consider the following discrete-time linear time-invariant (LTI) system in innovations form: where $x_{k}\in\mathbb{R}^{n_{x}}$, $u_{k}\in\mathbb{R}^{n_{u}}$, $y_{k}\in\mathbb{R}^{n_{y}}$ and $e_{k}\in\mathbb{R}^{n_{y}}$ are the state, input, output and innovations, respectively. For brevity of notation, we assume that the initial time starts at $k=1$, and the terminal time is denoted as $\bar{N}=N+p+f-1$, where $N$ is the number of columns in data Hankel matrices, and $p$ and $f$ stand for past and future horizons, respectively, to be defined later. In addition, the initial state is assumed to be $x_{1}=0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

\(2\) The system is minimal, i.e., $(A,[B,K])$ is controllable and $(A,C)$ is observable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

\(3\) The innovations $\{e_{k}\}$ consists of independent and identically distributed (i.i.d.) Gaussian random variables, i.e., $e_{k}\sim\mathcal{N}(0,I)$.^11^1Similar to, our results can be extended to more general setups, such as sub-Gaussians.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

\(4\) The input sequence $\{u_{k}\}$ consists also of i.i.d. Gaussian random variables, i.e., $u_{k}\sim\mathcal{N}(0,\sigma_{u}^{2}I)$. Moreover, it is assumed independent of $\{e_{k}\}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To illustrate the generality of the innovations model, we consider the following standard state-space model which divides the noise term into contributions from measurement noise $v_{k}$ acting on the outputs and process noise $w_{k}$ acting on the states: The noises $w_{k}$ and $v_{k}$ consist of i.i.d. zero-mean Gaussian random variables, with covariance $\Sigma_{w}$ and $\Sigma_{v}$, respectively. Moreover, they are independent of each other. We assume that $\Sigma_{v}\succ 0$, $(A,C)$ is detectable, and $(A,\Sigma_{w})$ is stabilizable. Then, the Kalman filter of system is well defined, and the Kalman gain is equal to where $P$ is the solution of the following Riccati equation: We further assume that the initial state is a zero-mean Gaussian variable with covariance $P$ and independent of the noises. Then, by the orthogonality principle the innovations sequence also consists of i.i.d.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Gaussian variables with covariance Therefore, under mild conditions the innovations form describes the same input-output trajectories as the standard state-space model, and it is widely used in SIMs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Based on the innovations form, after replacing $\Sigma_{e}^{1/2}e_{k}$ in (1a) with $y_{k}-Cx_{k}$, we obtain the following predictor form: where $A_{K}=A-KC$. Since the innovations form and the predictor form are equivalent and all can represent input and output data exactly, one has the option to use any of these forms for convenience. For instance, MOESP and PARSIM use the innovations form, and SSARX and PBSID use the predictor form.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given a finite number $\bar{N}$ of input-output samples from a single trajectory of system, our goal is to explicitly derive high probability error bounds on the system matrices estimated by some SIMs. To be specific, given a confidence level $0<\delta<1$, we wish to derive error bounds $\epsilon_{A},\epsilon_{B},\epsilon_{C}$, such that hold with probability at least $1-\delta$, where $\hat{A}$, $\hat{B}$ and $\hat{C}$ are estimates of system matrices, and $T$ is a non-singular matrix.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It is only possible to obtain the system matrices up to a similarity transformation due to the non-uniqueness of a realization. Moreover, it should be mentioned that the matrix $T$ here is stochastic, depending on the realization. Alternatively the estimates could be transformed into a canonical form. Furthermore, bounds on the estimation of Markov parameters or other system invariants could also be given.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Problem 1 is one of the long-standing open problems in subspace identification. As noted by Van Overschee and De Moor, "solving these problems would contribute significantly to the maturing of the field of subspace identification." The existing literature already offers some pertinent solutions to Problem 1. According to recent work in the non-asymptotic regime, the error bound $\epsilon_{\theta}$ is typically of the form where $\theta$ denotes the parameter of interest, and SNR denotes the signal-to-noise ratio.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In the asymptotic regime, prior work have shown that the normalized error $\sqrt{\bar{N}}\left(\hat{\theta}-\theta\right)$ converges in law to a normal distribution. Consequently, the results in --where the error decays at rate $\mathcal{O}(1/\sqrt{\bar{N}})$ and the confidence level $\delta$ appears through $\log(1/\delta)$--are consistent with these asymptotic results. Moreover, the LIL suggests that error decays at rate $\mathcal{O}(\sqrt{\frac{\log\log\bar{N}}{\bar{N}}})$ almost surely, which is sharp. However, asymptotic results require that $\bar{N}\to\infty$ and can only be used as a heuristic for a finite $\bar{N}$. Some questions remained unanswered.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

For instance, there often is a minimal requirement on $\bar{N}$, namely the burn-in time $\bar{N}_{\text{pe}}$, which is necessary for a bound of the form to hold. Such requirements are typically of the form The above $\bar{N}_{\text{pe}}$ cannot be obtained by applying only asymptotic tools. Moreover, as shown in and Lemma 1 in this work, non-asymptotic analysis can even achieve an error bound for marginally stable systems, whereas asymptotic results are often limited to asymptotically stable systems.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Existing non-asymptotic results for Problem 1 mainly focus on the classical Ho--Kalman algorithm or similar variants. However, this realization algorithm is outdated, as more powerful SIMs have later been proposed in the literature. Whether the structure in also holds for modern SIMs has therefore remained unclear. This work proves that modern SIMs also obey the same structure. Moreover, it is different in the following key respects.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2", "weight": 1.0} -->

First, a standard step of SIMs is to estimate a Hankel (or Hankel-like) matrix of Markov parameters, denoted by $\mathcal{H}_{fp}$. A key feature of modern SIMs is that $\mathcal{H}_{fp}$ is estimated directly using a projection method. However, this projection step couples future data with past data, resulting in an error without a standard martingale structure, which is difficult to upper bound. We believe that this is one of the main barriers preventing a finite sample analysis for SIMs. Previous analyses either revert to the Ho--Kalman algorithm or avoid inputs, where the projection step is not involved, thereby sidestepping the problem. The way we solve it is to absorb the projection matrix into an enlarged regressor, so that the error restores a standard martingale structure. The price to pay is that this format requires a more complex yet tractable PE condition.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Second, in the model reduction step, due to the fact that $\mathcal{H}_{fp}$ is low-rank, some data-dependent weighting matrices $W_{1}$ and $W_{2}$ are pre-multiplied and post-multiplied to the estimate of ${\mathcal{H}}_{fp}$ before performing an SVD to improve the numerical and statistical properties. Several asymptotic properties of such algorithmic variations have been studied. However, it is an open problem to study the impact of weighting matrices and compare their performance in a finite sample setting. Prior work considered the trivial weighting $W_{1}=W_{2}=I$. This work delivers the first finite sample analysis for general weighting matrices through a novel analysis leveraging the Schur complement.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Third, unlike the Ho-Kalman algorithm, many SIMs typically estimate system matrices by first recovering the state sequences and then applying least-squares regression in the output and state equations. To the best of our knowledge, this realization algorithm has not been analyzed in the non-asymptotic regime. Our work shows that the error of this realization algorithm also obeys the structure of.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In summary, our work extends finite sample results from simplified prototypes to the algorithms actually deployed, offering new insights and systematic performance guarantees.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Recap of Subspace Identification Methods", "weight": 1.0} -->

In this section we provide a short overview of open-loop SIMs, with the focus on PARSIM. For convenience, we define which stack past inputs and future inputs, respectively. Similar definitions apply to $y_{p}(k)$, $e_{f}(k)$, $u_{i}(k)$ and $e_{i}(k)$. Moreover, after lining up $u_{p}(k)$ and $u_{f}(k)$ from $k=1$ to $k=N$, we obtain Hankel matrices Similar definitions apply to data matrices $Y_{p}$, $Y_{f}$, $E_{p}$ and $E_{f}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Recap of Subspace Identification Methods", "weight": 1.0} -->

The state sequence is given by By iterating model using the above notations, an extended state-space model can be derived as where $\Gamma_{f}$ is the extended observability matrix, defined by Moreover, the transmission matrices $G_{f}$ is a lower-triangular Toeplitz matrix of Markov parameters, and $H_{f}$ is similarly defined by replacing $0$ on the diagonal of $G_{f}$ with $\Sigma_{e}^{\frac{1}{2}}$, and by replacing $B$ with $K\Sigma_{e}^{\frac{1}{2}}$. Similar definitions apply to matrices $\Gamma_{p}$, $G_{p}$ and $H_{p}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Recap of Subspace Identification Methods", "weight": 1.0} -->

Furthermore, by iterating equation (3a), we obtain where $Z_{p}=\begin{bmatrix}Y_{p}^{\top}&U_{p}^{\top}\end{bmatrix}^{\top}$ and $L_{p}$ is the extended controllability matrix in a reverse order, defined by After substituting into (8a), we have where $\mathcal{H}_{fp}:=\Gamma_{f}L_{p}$ is the Hankel-like matrix. Most variants of SIMs can be integrated into a unified framework which generally consists of three steps. We now introduce them based.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Step 1: Linear Regression or Projection", "weight": 1.0} -->

Most open-loop SIMs use to first estimate the Hankel-like matrix $\mathcal{H}_{fp}$, and then proceed to obtain the system matrices. A basic approach in classical SIMs is one-step regression, which takes $Z_{p}$ and $U_{f}$ as regressors and obtains $\mathcal{H}_{fp}$ and $G_{f}$ simultaneously using Since $\mathcal{H}_{fp}$ is our main interest, using the inverse of a block matrix (see Lemma 13.10), $\hat{\mathcal{H}}_{fp}$ can be extracted from as where $\Pi_{U_{f}}^{\perp}=I-U_{f}^{\top}(U_{f}U_{f}^{\top})^{-1}U_{f}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Step 1: Linear Regression or Projection", "weight": 1.0} -->

Although the estimate $\hat{\mathcal{H}}_{fp}$ is consistent, the one-step regression method cannot preserve the lower-triangular Toeplitz structure of the transmission matrix $G_{f}$, which is responsible for recording the impact of future input $U_{f}$ on future output $Y_{f}$. Due to the loss of this structure in $\hat{G}_{f}$, the model format is not causal anymore, which poses a challenge in statistical analysis.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In some literature of SIMs, the above one-step regression is called the projection method, in the sense that the future input $U_{f}$ is first projected out using For a sufficiently large $p$, since $A_{K}^{p}\approx 0$, the rightmost term $\Gamma_{f}A_{K}^{p}X_{k-p}\Pi_{U_{f}}^{\perp}$ becomes negligible. Moreover, as $U_{f}$ is uncorrelated with $E_{f}$, we have $E_{f}\Pi_{U_{f}}^{\perp}\approx E_{f}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3", "weight": 1.0} -->

After multiplying $Z_{p}^{\top}$ on both sides of, we have Since $E_{f}$ is uncorrelated with $Z_{p}$, implying $\frac{1}{N}E_{f}Z_{p}^{\top}\approx 0$, $\Gamma_{f}L_{p}$ can then be estimated using least-squares. It is clear that the estimate of $\Gamma_{f}L_{p}$ in is identical to.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3", "weight": 1.0} -->

To enforce causal models, a parallel and parsimonious SIM, PARSIM, is proposed. Instead of using the one-step regression, PARSIM zooms into each row of and performs $f$ least-squares to estimate a bank of ARX models. To illustrate this, equation can be partitioned row-wise as where for $i=1,2,...f$, $\Gamma_{fi}=CA^{i-1}\in\mathbb{R}^{n_{y}\times n_{x}}$, where similar definitions apply to $E_{fi}$ and $E_{i}$. PARSIM then minimizes a bank of $i$-steps ahead prediction errors from model using ordinary least-squares (OLS), At last, the whole estimate of ${\mathcal{H}}_{fp}$ is obtained by stacking the $f$ estimates together as It has been shown in that the estimate in admits a smaller variance than.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Step 3: Realization of System Matrices", "weight": 1.0} -->

Given estimates of $\Gamma_{f}$ and $L_{p}$, there are two paths to obtain the system matrices. It should be mentioned that currently there is no solid conclusion on which realization leads to a better model. To be specific, one is the CVA type which uses the following linear regressions in the output and state equations to estimate the system matrices: where $X_{k}^{+}$ stacks the states for the next time instant compared to $X_{k}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Step 3: Realization of System Matrices", "weight": 1.0} -->

By replacing $X_{k}$ and $X_{k}^{+}$ with their estimates where $Z_{p}^{+}$ is similarly defined as $X_{k}^{+}$, we have Another realization method is the MOESP type, which directly extracts system matrices based on the shift invariance property of $\hat{\Gamma}_{f}$ and $\hat{L}_{p}$, i.e., where $\hat{\Gamma}_{f}^{+}$ and $\hat{\Gamma}_{f}^{-}$ are the last and first $f-1$ row blocks of $\hat{\Gamma}_{f}$, and the indexing of matrices follows MATLAB syntax.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 4", "weight": 1.0} -->

In this paper, our main interest is to estimate the system matrices $\left\{A,B,C\right\}$, and derive error bounds for them. In principle, the Kalman gain $K$ can also be obtained from the above algorithms with minor modifications. Meanwhile, there are also other methods to obtain $K$, such as solving a Riccati equation in N4SID and using QR factorization in PARSIM. To keep our results relatively compact, the estimate of $K$ and its error bound are not considered in this work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Roadmap Ahead", "weight": 1.0} -->

Now we sketch the path ahead to the solution for Problem 1. In the first step that estimates the Hankel-like matrix ${\mathcal{H}}_{fp}$, we opt for PARSIM to facilitate the analysis. Parallel to the three steps in SIMs, we solve Problem 1 by a three-step procedure: \(1\) Step 1: We first derive an error bound on $\hat{\Theta}_{i}$ in for every ARX model. In other words, we define the following events for $i=1,2,...,f$: and require that $\mathbb{P}(\mathcal{E}_{i,\Theta}^{c})\leq\frac{\delta}{f}$. We then utilize a norm inequality (see Lemma 13.9.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Roadmap Ahead", "weight": 1.0} -->

‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) between the block matrix $\widehat{\Gamma_{f}L_{p}}-{\Gamma_{f}L_{p}}$ and its sub-blocks $\widehat{\Gamma_{fi}L_{p}}-{\Gamma_{fi}L_{p}}$ to obtain the total bound on $\hat{\mathcal{H}}_{fp}-{\mathcal{H}}_{fp}$. This essentially requires that the intersection of $f$ events has probability $\mathbb{P}(\bigcap_{i=1}^{f}\mathcal{E}_{i,\Theta})\geq 1-\delta$, which is guaranteed due to the union bound $\mathbb{P}(\bigcup_{i=1}^{f}\mathcal{E}_{i,\Theta}^{c})\leq\delta$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Roadmap Ahead", "weight": 1.0} -->

\(2\) Step 2: We use recent results from SVD robustness to provide error bounds on the extended observability matrix $\Gamma_{f}$ and controllability matrix $L_{p}$, where the impact of different weighting matrices in Table 1 is also discussed.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Roadmap Ahead", "weight": 1.0} -->

\(3\) Step 3: We derive error bounds $\epsilon_{A}$, $\epsilon_{B}$, and $\epsilon_{C}$ on the system matrices $\left\{A,B,C\right\}$ coming from the Larimore and MOESP realization algorithms.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Finite Sample Analysis of ARX Models", "weight": 1.0} -->

Following our roadmap, we formalize Step 1 above in this section. We emphasize that the results presented in this section apply to each ARX model in for $i=1,...,f$, where the subscript $i$ shows the model-specific dependence. For convenience, we define two covariates where $d_{p,i}=p(n_{u}+n_{y})+in_{u}$ is the problem dimension of each ARX model, and $\Lambda_{e,u}={\rm{diag}}(\sigma_{u},\cdots,\sigma_{u},1,\cdots,1)$ normalizes $w_{p,i}(k)$, such that it has unite variance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Finite Sample Analysis of ARX Models", "weight": 1.0} -->

We further partition the following matrices column-wise: Moreover, we have the following definitions regarding the covariance and empirical covariance of $\phi_{p,i}(k)$ and $x_{k}$: Note that the regressor in can be rewritten as Then, the error of the OLS estimate can be written as There are two types of errors, namely, the cross-term error ${\tilde{\Theta}}_{i}^{E}$ and the truncation bias ${\tilde{\Theta}}_{i}^{B}$. A key observation is that the future innovations $e_{i}(k)$ are independent of the covariate $\phi_{p,i}(l)$ for all $l<k$. This provides a martingale structure, which is convenient to analyze. To bound the above two errors, we first use results from the smallest eigenvalue of the empirical covariance of causal Gaussian processes to lower bound ${\hat{\Sigma}}_{p,i,N}$, which simultaneously establish the PE condition.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Persistence of Excitation", "weight": 1.0} -->

To achieve PE, the number of samples $N$ should exceed a certain threshold, which we call the burn-in time $N_{pe}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 5", "weight": 1.0} -->

As shown in Appendix 8, for any given $p$, $i$ and $\delta$, the $N$-dependent factors $N_{W}\left(\delta,p,i\right)$ and $N_{\Phi}\left(\delta,p,i\right)$ grow at most logarithmically with $N$. Therefore, for a sufficiently large $N$, the existence of $N_{pe}(\delta,p,i)$ is guaranteed.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Some relevant PE conditions appear in and, where past outputs and inputs are included in regressors. Our analysis extends this by additionally incorporating future inputs, thus establishing a more general PE condition. This broader result is also useful for analyzing data-dependent weighting matrices, as detailed in Section 5. Furthermore, this PE condition also holds for marginally stable systems.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Bound on Truncation Bias", "weight": 1.0} -->

In order to ensure that the truncation bias term ${\tilde{\Theta}}_{i}^{B}$ decays much faster than the cross-term error ${\tilde{\Theta}}_{i}^{E}$, we make the following assumption regarding the past horizon $p$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The past horizon is chosen as $p=\beta\text{log}N$, where $\beta$ is large enough such that

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

To ensure that the model closely approximates an ARX model, the truncation bias $\Gamma_{fi}A_{K}^{p}x_{k}$ should be small enough, which requires that the exponentially decaying term $A_{K}^{p}$ counteracts the magnitude of the state $x_{k}$. To illustrate this, we have that As a consequence of Lemma 13.14. ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), the state norm $\left\lVert{\Sigma}_{x,N}\right\rVert$ grows at most polynomially with $N$. Meanwhile, since $\rho(A_{K})<1$, we have $\left\lVert A_{K}^{p}\right\rVert=\mathcal{O}({\bar{\rho}}^{p})$ for some ${\bar{\rho}}>\rho(A_{K})$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Overall Bound", "weight": 1.0} -->

Lemma 4.3 suggests that the cross-term error ${\tilde{\Theta}}_{i}^{E}$ decays as $\mathcal{O}(1/\sqrt{N})$, and Lemma 4.6 suggests that the truncation bias ${\tilde{\Theta}}_{i}^{B}$ decays as $\mathcal{O}(1/N)$. This implies that ${\tilde{\Theta}}_{i}^{B}$ is dominated by ${\tilde{\Theta}}_{i}^{E}$ and it can be considered negligible. After absorbing higher order terms into the dominant term by inflating the constants accordingly, we obtain the following theorem controlling the whole error ${\tilde{\Theta}}_{i}$ of each ARX model in our collection.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Robustness of Balanced Realization", "weight": 1.0} -->

Following our roadmap, having obtained an overall error bound on $\hat{\mathcal{H}}_{fp}-{\mathcal{H}}_{fp}$ in Step 1, we now move to Step 2 to derive error bounds on the extended controllability and observability matrices, and Step 3 to obtain error bounds on the system matrices.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Weighted Singular Value Decomposition", "weight": 1.0} -->

Weighted SVD is crucial for improving the performance of SIMs. As summarized in Table 1, different choices of weighting matrices lead to different variants of SIMs. Since those data-dependent weighting matrices share a similar structure, we choose the pair used in MOESP and PARSIM to illustrate their characteristics, where The focus is on the data-dependent $W_{2}$, whose finite-sample properties are summarized as follows: ^33^3Similarly, conditions for other weighting matrices in Table 1 can be obtained.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 5.5", "weight": 1.0} -->

Compared to a stochastic non-singular matrix $T$ in Problem 1, matrix $T$ is constrained to be an orthogonal matrix in Theorem 5.3. This is mainly due to Lemma 13.12. ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). Furthermore, according to the eigenvalue decomposition, every non-singular matrix has an associated orthogonal matrix. Therefore, such a constraint will not affect the generality of our results.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Bounds on System Matrices", "weight": 1.0} -->

Having obtained upper bounds on the extended observability matrix $\bar{\Gamma}_{f}$ and controllability matrix $\bar{L}_{p}$ in Step 2, we now move to the final Step 3 to derive error bounds on the system matrices, where two realization algorithms are studied.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussions", "weight": 1.0} -->

We now discuss the implications of our main results. Specifically, we will answer two key questions: how to extend our method to other variants of SIMs, and what does the finite sample analysis bring.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Extensions to Other Methods", "weight": 1.0} -->

It is clear that our results in Steps 2 and 3 cover a large class of SIMs. In Step 1, to strictly enforce a causal model, we opt for the multi-regression method used in PARSIM--one of the most appealing SIMs, to estimate the Hankel-like matrix ${\mathcal{H}}_{fp}$. The following observations suggest that the technique used in the analysis of PARSIM can be extended to other SIMs.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Extensions to Other Methods", "weight": 1.0} -->

First, our analysis for PARSIM can be extended to the one-step regression method. If we study the estimation error of ${\mathcal{H}}_{fp}$ in separately, the cross-term error will be $E_{f}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}(Z_{p}\Pi_{U_{f}}^{\perp}Z_{p}^{\top})^{-1}$. Due to the data-dependent projection matrix $\Pi_{U_{f}}^{\perp}$, the columns of $E_{f}$ and $Z_{p}$ are mixed together, bringing challenges to statistical analysis. However, this problem can be avoided if we study the total error of $\Theta$, which is equivalent to setting $i=f$ in PARSIM.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Extensions to Other Methods", "weight": 1.0} -->

Second, our analysis can be extended to other SIMs that estimate high order ARX models using least-squares in their first step, such as SSARX and PBSID. To be specific, for SSARX, it first estimates the predictor Markov parameters $\left\{{C{A_{K}^{i}}B,C{A_{K}^{i}}K}\right\}_{i=0}^{f-1}$ from a high-order ARX model, and then replaces the true Markov parameters in the transmission matrices with their estimates, and proceeds to estimate a Hankel-like matrix. PBSID, also known as the whitening filter approach, starts from the predictor form. Similar to PARSIM, it utilizes the structure of the transmission matrices to carry out multiple regressions parallelly. It is clear that our methods can be applied to the first step of SSARX, and to every step of PBSID in the ope-loop setting.

<!-- chunk {"id": "body-0064", "role": "body", "section": "What Does Finite Sample Analysis Bring", "weight": 1.0} -->

Under the umbrella of this question, we analyze the implications of our results and validate them with simulations on a benchmark SISO system used in SIM studies. It should be mentioned that the results in this paper directly extend to MIMO systems. The SISO system is given by where $a=-0.7$, $b=1$ and $c=0.5$. The innovations $e_{k}\sim\mathcal{N}$. Two types of inputs are considered, one is a white input given by $u_{k}\sim\mathcal{N}$, and the other is a colored input^44^4It is important to note that due to Assumption 2.1, our theoretical results do not apply to scenarios with colored inputs yet.

<!-- chunk {"id": "body-0065", "role": "body", "section": "What Does Finite Sample Analysis Bring", "weight": 1.0} -->

However, using colored inputs in our simulations helps in demonstrating the behavior of SIMs., generated by a white noise $r_{k}\sim\mathcal{N}$ passing through a filter $H_{u}(q^{-1})=\frac{0.318}{1-0.5q^{-1}+0.9q^{-2}}$, where $q^{-1}$ is the backward shift operator.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Statistical Rates", "weight": 1.0} -->

According to Theorems 4.9, 5.3, 5.6 and 5.8, the error bounds on the Hankel-like matrix ${\mathcal{H}}_{fp}$, the extended observability matrix $\Gamma_{f}$, controllability matrix ${L}_{p}$, and system matrices $C$, $B$ and $A$ decay as $\mathcal{O}(1/\sqrt{N})$ up to logarithmic terms. Classical asymptotic results, such as the LIL, can tighten the log factor to $\mathcal{O}(\text{log}\text{log}N/\sqrt{N})$. This suggests that our bounds are not tight, which is one of the downsides of the non-asymptotic analysis. It is possible to optimize our results in the future.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Persistence of Excitation", "weight": 1.0} -->

Similar to the PE condition for consistency analysis in the asymptotic regime, Lemma 1 provides a non-asymptotic PE condition. Specifically, it guarantees the invertibility of the empirical covariance matrix ${\hat{\Sigma}}_{p,i,N}$ defined in by establishing a lower bound on its smallest eigenvalue. In practice, once data is available, one can directly verify PE by computing the smallest eigenvalue of ${\hat{\Sigma}}_{p,i,N}$. Nonetheless, Lemma 1 provides a theoretical threshold, denoted by the burn-in time $N_{pe}$, indicating the minimum sample size required to ensure invertibility of ${\hat{\Sigma}}_{p,i,N}$. Such a non-asymptotic result is valuable for designing experiments (e.g., determining excitation duration), and implementing stopping rules in adaptive control.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Dimensional Dependence", "weight": 1.0} -->

As shown in and Theorem 4.9, the burn-in time $N_{pe}$ and error bounds scale with the problem dimension $d_{p,i}$ and the state dimension $n_{x}$. Such a dimensional dependence still holds when $n_{x}$ increases to the same order as $N$, whereas the results in the asymptotic regime are less meaningful in this case.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Sweet Spot for the Past Horizon $p$", "weight": 1.0} -->

Assumption 4.1 implies that to make the truncation bias ${\tilde{\Theta}}_{i}^{B}$ decay much faster than the cross-term error ${\tilde{\Theta}}_{i}^{E}$, the past horizon $p$ should increase at a proper rate with $N$, i.e., $p=\beta\text{log}N$, where $\beta$ is sufficiently large. Meanwhile, a larger $p$ means that there are more parameters to be estimated, thus implying a larger error bound. This highlights that, for a fixed $N$, there is a sweet spot for the choice of $p$. Similar conclusions are found in asymptotic analysis, suggesting that $p$ should grow moderately with $N$, neither too slow nor too fast. In practice though, $p$ can be selected using information criteria or a two-step procedure--either by minimizing the prediction error of the estimated state-space model or by directly minimizing the error bounds. We use the numerical example to demonstrate the existence of the sweet spot.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Sweet Spot for the Past Horizon $p$", "weight": 1.0} -->

We fix the future horizon at $f=7$, and vary the number of samples $\bar{N}=500:1000:2500$ and the past horizon $p=2:4:30$. The input is white, and the weighting matrices are chosen as $W_{1}=I$ and $W_{2}=I$. We run 100 Monte Carlo trials. The performance is evaluated by the average normalized error of the poles $\left\lVert\hat{a}-a\right\rVert/\left\lVert a\right\rVert$, where $\hat{a}$ is obtained using two realization algorithms. As shown in Figure 1, for both two realization methods, when the number of samples is fixed, there is a sweet spot for $p$ that minimizes the errors. In addition, when the number of samples increases, the sweet spot for $p$ tends to increase as well.

<!-- chunk {"id": "body-0071", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

In the asymptotic regime, the impact of weighting matrices is discussed. At a high level, $W_{1}$ is related to a maximum likelihood or CVA objective, while $W_{2}$ is related to an orthogonal projection. In addition, $W_{1}$ has little impact on the asymptotic accuracy of $\Gamma_{f}$, and $W_{2}$ has little impact on the asymptotic accuracy of $L_{p}$. As shown in Theorem 5.3, our work provides a new perspective on the impact of weighting matrices. To be specific, for the robustness of SVD, the condition should be satisfied, which guarantees that the singular vectors related to small singular values of $W_{1}{\mathcal{H}}_{fp}W_{2}$ can be separated from the singular vectors coming from the noise $W_{1}\left(\hat{\mathcal{H}}_{fp}-{\mathcal{H}}_{fp}\right)W_{2}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

Because $W_{1}$ and $W_{2}$ reshape these singular values, they can either relax or tighten the condition. To see this clearly, we use the numerical example to show the impact of different weighting matrices in Table 1. The simulation settings are the same as before, and the past horizon is fixed at $p=f=7$. Both white input and colored input are considered. The performance is evaluated by the ratio We determine whether the condition is satisfied or not by comparing $\kappa$ with $1/4$. The results are shown in Figure 2^55^5Note that N4SID gives almost identical results as MOESP, and IVM gives almost identical results as CVA, so only results for MOESP, CVA and OKID are presented..

<!-- chunk {"id": "body-0073", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

First, Figure 2 suggests that different weighting matrices result in different number of samples required for the condition to be satisfied. Since $\left\lVert\hat{\mathcal{H}}_{fp}-{\mathcal{H}}_{fp}\right\rVert$ decays as $\mathcal{O}(1/\sqrt{N})$, no matter what pair of weighting matrices we choose, $\kappa\leq 1/4$ will be eventually satisfied as $N\to\infty$. However, a good choice of weighting matrices makes it easier to satisfy this condition, such as the MOESP weighting.

<!-- chunk {"id": "body-0074", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

Second, both weighting matrices $W_{1}$ and $W_{2}$ affect the robustness condition. As shown in Figure 2, MOESP and CVA employ different $W_{1}$ and the same $W_{2}$, which result in different robustness conditions. Meanwhile, MOESP and OKID employ different $W_{2}$ and the same $W_{1}$, which also result in different robustness conditions.

<!-- chunk {"id": "body-0075", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

Third, the impact of weighting matrices is input-dependent. As shown in Figure 2, it is easier for the MOESP weighting to satisfy the condition when the input is white than colored.

<!-- chunk {"id": "body-0076", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

Fourth, besides their impact on the robustness condition, the weighting matrices also influence the estimation accuracy. It should be emphasized that a pair of weighting matrices making the robustness condition easier to achieve does not mean that they also imply a smaller estimation error. To illustrate this, we choose the estimate of poles coming from two realization algorithms to demonstrate the impact of the weighting matrices. The simulation settings are same as before, and only the white input is considered. The performance is evaluated by the normalized error of the poles $\left\lVert\hat{a}-a\right\rVert/\left\lVert a\right\rVert$. The results are shown in Figure 7. Based on the right subplots of Figures 2 and 7, we see that compared to the CVA weighting, although the MOESP weighting makes the robustness condition easier to achieve, it increases the estimation error of the poles.

<!-- chunk {"id": "body-0077", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

In addition, as shown in Figure 7, $W_{1}$ has minor influence on the estimate of the poles for the MOESP type realization, and $W_{2}$ has minor influence on the estimate of the poles for the Larimore type realization. This is consistent with an analysis in the asymptotic regime. However, this conclusion cannot be obtained through our finite sample analysis. This comparison underscores the view that both asymptotic and non-asymptotic methods are valuable in uncovering the statistical properties of SIMs, and they complement each other.

<!-- chunk {"id": "body-0078", "role": "body", "section": "On the Impact of Weighting Matrices", "weight": 1.0} -->

Finally, we remark that the robustness condition is a sufficient condition, and our results are upper bounds. It is not sufficient to determine the best choice of weighting matrices solely based on the criteria of facilitating the achievement of robustness conditions and minimizing the upper bounds. To fully grasp the influence of the weighting matrices and develop an optimal choice, further study is needed.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents a finite sample analysis for a large class of open-loop SIMs. Compared with the-state-of-art that mainly analyzes the performance of the Ho-Kalman algorithm or similar variants, we investigate one of the most representative SIMs, PARSIM. Our analysis establishes a more general PE condition, and takes the different weighting matrices and two realization algorithms into account. It not only confirms that the convergence rates for estimating the Markov parameters and system matrices are $\mathcal{O}(1/\sqrt{N})$ even in the presence of inputs, in line with classical asymptotic results, but it also provides high-probability upper bounds for these estimates. Our findings complement the existing asymptotic results, and methodologies can be similarly applied to many variants of SIMS, such as classical SIMs, SSARX and PBSID.
