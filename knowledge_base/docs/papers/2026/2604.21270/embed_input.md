<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CLT-Optimal Parameter Error Bounds for Linear System Identification

Topics include System identification, Regression, Linear dynamical system, Via ordinary least-squares regression, Ordinary least squares, Linear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

There has been remarkable progress over the past decade in establishing finite-sample, non-asymptotic bounds on recovering unknown system parameters from observed system behavior. Surprisingly, however, we show that the current state-of-the-art bounds do not accurately capture the statistical complexity of system identification, even in the most fundamental setting of estimating a discrete-time linear dynamical system (LDS) via ordinary least-squares regression (OLS). Specifically, we utilize asymptotic normality to identify classes of problem instances for which current bounds overstate the squared parameter error, in both spectral and Frobenius norm, by a factor of the state-dimension of the system. Informed by this discrepancy, we then sharpen the OLS parameter error bounds via a novel second-order decomposition of the parameter error, where crucially the lower-order term is a matrix-valued martingale that we show correctly captures the CLT scaling.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

From our analysis we obtain finite-sample bounds for both (i) stable systems and (ii) the many-trajectories setting that match the instance-specific optimal rates up to constant factors in Frobenius norm, and polylogarithmic state-dimension factors in spectral norm.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification---the task of recovering unknown parameters of a dynamical system from observed system behavior---is a central problem in control. While system identification has a long and rich history in the control theory literature, the rise of machine learning approaches to control has led to a recent surge of results, particularly in establishing non-asymptotic, finite-sample guarantees for parameter recovery \[simchowitz2018learning, sarkar2019near, Faradonbeh2018identification, Ziemann2023\]. Such bounds are valuable both for characterizing the statistical limits of system identification, and for providing principled guidance on the data requirements needed to learn accurate models in practice.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite this remarkable progress, we argue that existing state-of-the-art bounds still fail to fully capture the statistical complexity of system identification---surprisingly even in the most basic setting of estimating the dynamics matrix of a discrete-time linear dynamical system (LDS) given one or many trajectories of state observations using ordinary least-squares (OLS) regression, a model known as the $\mathrm{VAR}$ (vector auto-regressive) model which we focus on in this work. At first glance, this statement seems to contradict existing claims of minimax-optimality of OLS for this setting \[simchowitz2018learning, jedra2019lowerbounds, jedra2020lti\]. However, a more careful introspection reveals that minimax-optimal rates are only sharp on a carefully selected set of problem instances; they do *not* guarantee sharp rates on every problem instance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Concretely, we consider two setups where asymptotic normality can be used to compute the exact instance-specific problem scaling: (i) strictly stable transition dynamics, and (ii) the many trajectories \[tu2024manytraj\] setting, where the number of independent trajectories outnumber the dimension. We remark that (i) and (ii) are not mutually exclusive. Our analysis reveals many problem instances where the sharpest known OLS bounds *overestimate* the squared parameter estimation error, in either Frobenius or operator norm, by a factor of the state-dimension. These instances are characterized by a sufficiently fast decay of the eigenvalues of either the noise covariance matrix or the inverse state covariance matrix, so that trace $\operatorname*{\mathsf{tr}}(M)$ of said matrices is significantly smaller than $d\lVert M\rVert_{\mathsf{op}}$, where $d$ is the state-dimension and $\lVert M\rVert_{\mathsf{op}}$ is the operator norm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A practical setting where this naturally arises is when disturbances enter the system in a non-uniform way, such as through an approximately low-rank subspace, or due to different physical scaling across state variables.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then turn to the problem of sharpening the non-asymptotic OLS bounds to match the instance-specific optimal rates from asymptotic normality. We establish sufficient conditions on the trajectory length in the case of stable transition dynamics, and on the number of trajectories in the many trajectories setting, for the squared parameter error of the OLS estimator to match the instance-specific optimal rate up to a constant factor in Frobenius norm, and up to $\mathrm{polylog}(d)$ factors in operator norm. At a high level, the deficiency of existing approaches is rooted in the standard decomposition of the OLS error introduced by \[simchowitz2018learning\], which splits the OLS error into two terms that are analyzed separately: (i) a self-normalized martingale term \[abbasi2011online\], and (ii) the minimum eigenvalue of the empirical state covariance matrix. We propose a novel second-order decomposition where the lowest order term becomes a simpler matrix-valued martingale that captures the CLT scaling.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Frobenius norm analyzing said martingale is immediate thanks to the inner-product structure, but for the operator norm extracting the CLT scaling is non-trivial and relies on the machinery of non-commutative Burkholder inequalities \[randrianantoanina07, junge2008\]. Returning back to our second-order decomposition, the new higher-order term places a stronger requirement on the empirical state covariance---namely a $p$-th moment approximate isometry condition---for which we establish by taking inspiration from the Hanson-Wright approach described in \[jedra2020lti\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our paper is organized as follows. In Section 2, we formalize the problem setting, discuss in detail what target rates we should expect from asymptotic normality, and illustrate examples where existing bounds are loose. In Section 3, we state our main non-asymptotic results for both Frobenius and operator norms. Section 4 provides a detailed proof outline, and Section 5 concludes with future directions. All proof details are deferred to Appendices A to C.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Asymptotic Normality of OLS", "weight": 1.0} -->

We first discuss the asymptotic normality of the OLS estimator, which is the key tool for us in establishing the correct forms of the bounds $\gamma_{F}$ and $\gamma_{\mathsf{op}}$ in (2.3).^11^1Appendix A contains the proofs for all claims in this subsection.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Asymptotic Normality of OLS", "weight": 1.0} -->

In our formulation, there are two variables, $m$ and $T$, that can either be separately or jointly sent to infinity, depending on the problem instance. We first consider holding $T$ fixed and taking $m$ to infinity, which does not require any assumptions on $A$. Indeed, by classical asymptotic normality of $M$-estimation (see e.g. \[Vaart1998\]), as $m\to\infty$, where $\Gamma_{T}:=\frac{1}{T}\sum_{t=1}^{T}\Sigma_{t}$ and $\Sigma_{t}:=\sum_{k=0}^{t-1}A^{k}\Sigma_{\mathcal{W}}(A^{k})^{\mathsf{T}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Asymptotic Normality of OLS", "weight": 1.0} -->

On the flip side, in order to send $T$ to infinity (either while holding $m$ fixed or jointly tending to infinity as well), we need to impose some assumptions on $A$. In general, the OLS estimator is not consistent when $A$ is irregular, i.e., the geometric multiplicity of any unstable eigenvalues of $A$ exceeds one (see e.g., \[phillips2013inconsistent, Faradonbeh2018identification, sarkar2019near\]). Furthermore, when $A$ is regular but not strictly stable, the limiting error distributions are not Gaussian \[white1958limiting, chan1988limiting\] and require functional CLT arguments to study. Hence, for sending $T$ to infinity, we will focus only on strictly stable dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Asymptotic Normality of OLS", "weight": 1.0} -->

We note that the right-hand-side of both (2.4) and (2.5) can be further unified via a joint limit on $(m,T)$. Let $\phi:\mathbb{N}_{+}\mapsto\mathbb{N}_{+}$ be any function such that $\phi(m)\to\infty$ as $m\to\infty$. Then for the joint limit $(m,T_{m})$ with $T_{m}:=\phi(m)$, as $m\to\infty$, one can show using the Lindeberg-Feller CLT \[Vaart1998, Proposition 2.27\], With the asymptotic limits (2.4), (2.5), and (2.6) in place, we now discuss how these limit distributions imply the correct form of both $\gamma_{F}$ and $\gamma_{\mathsf{op}}$. The key idea is the following fact.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

For the Frobenius norm, from the limit distributions in Section 2.1, we immediately identify our target goal for the quantity $\gamma_{F}=\gamma_{F}\left(A,\mathcal{W}\right)$ in (2.3a) as the following: Note that the goal (2.7) is consistent with both $m\to\infty$ limits (2.4) as well as $T\to\infty$ limits (2.5), (2.6), as $\Gamma_{T}\to\Sigma_{\infty}$ with $T\to\infty$ whenever $A$ is strictly stable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

We now remark on the difference between the stated goal (2.7) and existing results in the literature. We first compare to existing work in the strictly stable regime, which are stated for a single trajectory ($m=1$). Here, most parameter error bounds in the literature are in terms of the operator norm of the error, which we will also discuss shortly. However, via the norm equivalence inequality $\lVert\hat{A}_{m,T}-A\rVert_{F}^{2}\leqslant d\lVert\hat{A}_{m,T}-A\rVert_{\mathsf{op}}^{2}$, operator norm bounds also imply Frobenius norm bounds. Furthermore, most bounds work under the simplification $\Sigma_{\mathcal{W}}=\sigma^{2}I_{d}$, which we will further assume here for comparison.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

Let $K:=\max_{i\in[d]}\lVert w_{i}\rVert_{\psi_{2}}$ denote the maximum $\psi_{2}$-norm of each coordinate of $w\sim\mathcal{W}$, and suppose all coordinates are independent. Note that by definition, $K\geqslant\sigma$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

A prototypical operator norm bound is from \[jedra2020lti\], which states that for strictly stable $A$, when $T\lambda_{\min}(\Gamma_{T})\gtrsim\max\{K^{2},K^{4}\}\mathcal{J}(A)^{2}(d+\log(1/\delta))$ where $\mathcal{J}(A):=\sum_{t\geqslant 0}\lVert A^{t}\rVert_{\mathsf{op}}$, with probability at least $1-\delta$,^22^2For this comparison, we ignore the difference between expected value and high probability. However, we note that converting the typical high probability result in the literature to an expected value bound is non-trivial, as typical results require e.g., the trajectory length $T$ to scale as $\log(1/\delta)$ where $\delta$ is the failure probability.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

$\lVert\hat{A}_{1,T}-A\rVert_{\mathsf{op}}^{2}\lesssim\frac{K^{2}(d+\log(1/\delta))}{T\lambda_{\min}(\Sigma_{\infty})}$. Using the norm inequality: We see that this is qualitatively looser than (2.7) in Goal 1, since both $\sigma^{2}\leqslant K^{2}$ and $\operatorname*{\mathsf{tr}}(\Sigma_{\infty}^{-1})\leqslant d/\lambda_{\min}(\Sigma_{\infty})$. \[tu2024manytraj, Theorem 5.8\] also states a similar bound as (2.8) in expectation (the bound has extra log-factors due to it being applicable to marginally stable dynamics; these can be removed by specializing the proof to strictly stable $A$).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

Let us now compare to existing results in the many trajectories setting. The most relevant result is \[tu2024manytraj, Theorem 5.5\], which states that as long as $m\gtrsim d$, we have that the *excess risk* is optimally controlled as: While this excess risk bound is optimal, directly converting it to a Frobenius error bound via $\lVert\hat{A}_{m,T}-A\rVert^{2}_{\Gamma_{T}}\geqslant\lambda_{\min}(\Gamma_{T})\lVert\hat{A}_{m,T}-A\rVert_{F}^{2}$ implies the result: which again is looser than the stated goal (2.7).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

Here, we see two sources of gaps. First, the gap between $K$ and one can be arbitrarily large, even for scaled isotropic noise.^33^3Consider the r.v. $\mathbb{P}(X=\pm M)=1/(2M^{2})$ and $\mathbb{P}(X=0)=1-M^{-2}$. Here, $\lVert X\rVert_{\psi_{2}}^{2}/\mathbb{E}[X^{2}]=M^{2}/\log(1+M^{2})\to\infty$ as $M\to\infty$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Asymptotic Analysis in Frobenius Norm", "weight": 1.0} -->

Second, for state covariance matrices where the spectrum is highly non-uniform, there can be a non-trivial dimension factor gap between the state-of-the-art current rates and the optimal rate (2.7).^44^4We note that this example essentially illustrates the worst-case gap, as $\lVert M\rVert_{\mathsf{op}}\leqslant\operatorname*{\mathsf{tr}}(M)\leqslant d\lVert M\rVert_{\mathsf{op}}$ for any $d\times d$ PSD matrix $M$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Asymptotic Analysis in Operator (Spectral) Norm", "weight": 1.0} -->

Computing the correct form of $\gamma_{\mathsf{op}}$ for the operator norm is more involved, as the limiting asymptotic risk involves computing the largest singular value of a Gaussian random matrix, which does not typically admit a closed form expression. Concretely, for e.g., (2.4), we have $\lim_{m\to\infty}m\cdot\mathbb{E}\lVert\hat{A}_{m,T}-A\rVert_{\mathsf{op}}^{2}=\mathbb{E}_{g\sim\mathsf{N}(0,I_{d^{2}})}\lVert\mathrm{mat}((\Gamma_{T}^{-1/2}/\sqrt{T}\otimes\Sigma_{\mathcal{W}}^{1/2})g)\rVert_{\mathsf{op}}^{2}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Asymptotic Analysis in Operator (Spectral) Norm", "weight": 1.0} -->

The RHS expression is equal to $T^{-1}\cdot\mathbb{E}_{G}\lVert\Sigma_{\mathcal{W}}^{1/2}G\Gamma_{T}^{-1/2}\rVert_{\mathsf{op}}^{2}$, where $G$ is a $d\times d$ matrix with i.i.d. $\mathsf{N}$ entries. Fortunately, the correct order of this expression is available via the Gaussian Chevet inequality \[vershynin2018high, Section 8.6\], as summarized below.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumptions for Non-Asymptotic Analysis", "weight": 1.0} -->

Towards setting up and presenting our main non-asymtotic results, we first collect and discuss the various assumptions on the noise process $\{w_{t}\}_{t\geqslant 0}$ that we utilize in our analysis. Throughout the article, we utilize the following notation: with the understanding that $\mathcal{F}_{0}$ is the trivial $\sigma$-algebra. It is clear that $\{w_{t}\}_{t\geqslant 0}$ is $\mathcal{F}_{t+1}$-adapted and $\{x_{t}\}_{t\geqslant 0}$ is $\mathcal{F}_{t}$-adapted. We begin by formalizing our aforementioned problem setting with an additional sub-Gaussianity condition.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

For $w\sim\mathcal{W}$, $\bar{w}:=\Sigma^{-1/2}_{\mathcal{W}}w$ is directionally $\nu$-sub-Gaussian: for any $\lambda\in\mathbb{R}$, Assumption 2.2 is fairly standard in the non-asymptotic LDS identification literature \[simchowitz2018learning, sarkar2019near, tu2024manytraj\], as it provides access to sub-Gaussian self-normalized martingale tail bounds \[abbasi2011online\]. This assumption alone, however, is insufficient for our purposes, as we also need to control the behaviour of the empirical covariance $\Sigma_{m,T}:=(mT)^{-1}X_{m,T}^{\mathsf{T}}X_{m,T}$ as part of the OLS error. We now introduce two additional assumptions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

The first provides, in the two regimes we consider, high probability control on empirical covariance error $\lVert\Sigma_{m,T}-\Gamma_{T}\rVert_{\mathsf{op}}$. To state the assumption, we denote the entropy functional of a nonnegative integrable function $f$ with respect to a probability distribution $\mu$ as: We also denote the whitened noise process $\{\bar{w}_{t}\}_{t\geqslant 0}:=\left\{\Sigma_{\mathcal{W}}^{-1/2}w_{t}\right\}_{t\geqslant 0}$, and the whitened distribution of $\mathcal{W}$ as $\bar{\mathcal{W}}$, such that $\bar{w}_{t}\stackrel{{\scriptstyle\mathrm{i.i.d.}}}{{\sim}}\bar{\mathcal{W}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

We assume that $\bar{\mathcal{W}}$ satisfies *either* of the following: $\bar{\mathcal{W}}=\otimes_{i=1}^{d}\bar{\mathcal{W}}_{i}$ for one-dimensional distributions $\bar{\mathcal{W}}_{i}$, i.e., $\bar{w}_{t}$ has independent coordinates. $\bar{\mathcal{W}}$ satisfies the log-Sobolev inequality $\mathrm{LS}(\nu^{2})$: for any continuously differentiable $f\in L^{2}(\bar{\mathcal{W}})$ such that $\nabla f\in L^{2}(\bar{\mathcal{W}})$, Assumption 2.3 $(i)$ is fairly standard, having appeared in several prior works on LTI identification \[sarkar2019near, jedra2020lti\].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

On the other hand, Assumption 2.3 $(ii)$ is non-standard, and we will discuss verifying it in a moment. The role of Assumption 2.3 is to allow us to obtain concentration of $\lVert\Sigma_{m,T}-\Gamma_{T}\rVert_{\mathsf{op}}$ via different Hanson-Wright inequalities \[RudelsonVershynin2013, adamczak15\]. Specifically, Assumption 2.3 $(i)$ gives access to the classical Hanson-Wright inequality \[RudelsonVershynin2013\] requiring independence, here across time $t$ and across the coordinates of $\bar{w}_{t}$. On the other hand, Assumption 2.3 $(ii)$ enables the use of a Hanson-Wright inequality under the convex concentration property \[adamczak15\], where the whitened noise distribution $\bar{\mathcal{W}}$ is allowed to have dependencies between coordinates, but must instead satisfy a geometric restriction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

We note that for Assumption 2.3 $(ii)$, requiring the constant for log-Sobolev inequality to coincide with the sub-Gaussian constant in Assumption 2.2 $(ii)$ is without loss of generality, as $\bar{\mathcal{W}}$ satisfying $\mathrm{LS}(C)$ implies $\bar{\mathcal{W}}$ is directionally $\sqrt{C}$-sub-Gaussian (cf. Lemma D.4).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

Now off the typical events where we have concentration of $\lVert\Sigma_{m,T}-\Gamma_{T}\rVert_{\mathsf{op}}$, we still require control on how degenerate $\Sigma_{m,T}$ can become. Hence, our next assumption, from \[tu2024manytraj, Definition 4.1\], yields control on the *lower tail* of $\lambda_{\min}(\Sigma_{m,T})$, and generalizes small-ball conditions in the i.i.d. setting \[mourtada2022exact\].

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 2.4 (Trajectory small-ball (Traj-SB))", "weight": 1.0} -->

Assume the state trajectory $\{x_{t}\}_{t\geqslant 0}$ from (2.1) defined by $(A,\mathcal{W})$ satisfies the trajectory small-ball condition: for any trajectory length $T$, there exists constants $c\geqslant 1$ and $\alpha\in(0,1]$ such that for any excitation window size $k\in[T]$, window index $j\in\{1,\dots,\lfloor T/k\rfloor\}$, $v\in\mathbb{R}^{d}\setminus\{0\}$, and $\varepsilon>0$: We now discuss verifying Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification").

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 2.4 (Trajectory small-ball (Traj-SB))", "weight": 1.0} -->

It turns out that a very broad family of distributions $\bar{\mathcal{W}}$ can be readily shown to simultaneously satisfy these assumptions, namely the class of log-concave distributions. $\bar{\mathcal{W}}$ is said to be log-concave if it is (a) absolutely continuous w.r.t. the Lebesgue measure on $\mathbb{R}^{d}$ (denoted $\lambda_{d}$), (b) supported on a convex set $S$, and (c) the negative log density $\psi_{\bar{\mathcal{W}}}:=-\log\frac{\mathrm{d}\bar{\mathcal{W}}}{\mathrm{d}\lambda_{d}}$ is convex on $S$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2.4 (Trajectory small-ball (Traj-SB))", "weight": 1.0} -->

By Carbery and Wright's classical work on anti-concentration for polynomials of log-concave distributions (see \[carbery2001distributional, Theorem 8\] and \[tu2024manytraj, Example 4.6\]), a log-concave $\bar{\mathcal{W}}$ implies Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). Next, it turns out that there are two cases where additionally we have that Assumption 2.3 $(ii)$ holds (which then implies Assumption 2.2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2.4 (Trajectory small-ball (Traj-SB))", "weight": 1.0} -->

The first case (*strongly log-concave*, or SLC for short), is when $\psi_{\bar{\mathcal{W}}}$ is twice-differentiable and $\nu^{-2}$-strongly-convex (i.e., $\nabla^{2}\psi_{\bar{\mathcal{W}}}\succcurlyeq\nu^{-2}I_{d}$ everywhere on $S$); this follows from the classic Bakry-Émery criteria \[Bakry2014\]. The second case (*bounded log-concave*, or BLC for short), is when the support $S$ has diameter bounded as $O(\nu^{2})$, which is the result of recent work on stochastic localization \[leekls2024\]. This discussion is formalized in the following lemma.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Main Results", "weight": 1.0} -->

We now state our main results in light of Goal 1 and Goal 2 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). For what follows, we denote the parameter error $\hat{\Delta}_{m,T}:=\hat{A}_{m,T}-A$. We start with the Frobenius norm case.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis of Term $T_{1}$ for Frobenius Norm", "weight": 1.0} -->

For the Frobenius norm, we have: Furthermore, $\mathbb{E}[\hat{Q}_{m,T}^{\mathsf{T}}\hat{Q}_{m,T}]$ admits a simple closed form: where $(a)$ follows from independence across trajectories, and $(b)$ follows from applying iterated expection with respect to smaller time indices. Hence,

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis of Term $T_{1}$ for Operator Norm", "weight": 1.0} -->

Unlike the Frobenius norm analysis in Section 4.1, the operator norm analysis for $T_{1}$ is more challenging, as there is no inherent inner-product structure. Instead, we will exploit that $T_{1}$ is the second moment of the Schatten-$\infty$ norm of a matrix-valued martingale $\hat{Q}_{m,T}\Gamma_{T}^{-1}$. Such types of moment bounds in their full generality are known as noncommutative Burkholder inequalities \[randrianantoanina07, junge2008\]. The following lemma is a direct implication of \[randrianantoanina07, Theorem 4.1\] tailored to bounding $T_{1}$ under the operator norm.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analysis of Term $T_{2}$", "weight": 1.0} -->

We now turn to our analysis of term $T_{2}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Analysis of Term $T_{2}$", "weight": 1.0} -->

We denote the whitened version of $\hat{Q}_{m,T}$ and $\hat{\Sigma}_{m,T}$ as follows: Via elementary operations, we write $\hat{Q}_{m,T}(\hat{\Sigma}_{m,T}^{-1}-\Gamma_{T}^{-1})$ as: We now introduce an arbitrary positive definite normalization matrix $N\in\mathbb{R}^{d\times d}$, whose purpose will be explained soon in Section 4.3.2. We can upper bound $\left\lVert\hat{Q}_{m,T}(\hat{\Sigma}_{m,T}^{-1}-\Gamma_{T}^{-1})\right\rVert_{S_{p}}^{2}$ as follows: where $(a)$ applies the inequality $\lVert MN\rVert_{S_{p}}\leqslant\lVert M\rVert_{S_{p}}\lVert

<!-- chunk {"id": "body-0041", "role": "body", "section": "Analysis of Term $T_{2}$", "weight": 1.0} -->

Now using the Cauchy-Schwarz inequality and the inequality $\lVert M\rVert_{S_{p}}\leqslant\min\{d_{1},d_{2}\}^{1/p}\lVert M\rVert_{\mathsf{op}}$ for $M\in\mathbb{R}^{d_{1}\times d_{2}}$, we have: As suggested by the notation, $T_{2}^{\text{AIP}}$ measures the approximate isometry property (AIP) of the whitened empirical covariance $\bar{\Sigma}_{m,T}$, whereas $T_{2}^{\text{OLS}}$ measures the typical bound on OLS error (cf. Equation 4.1), specifically the norm of a self-normalized martingale divided by the minimum eigenvalue of an empirical covariance matrix.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Upper bounding $T_{2}^{\\textnormal{AIP}}$", "weight": 1.0} -->

Taking inspiration from the work of \[jedra2020lti\], we utilize the Hanson-Wright inequality \[RudelsonVershynin2013, adamczak15\] to control the $r$-th moments of the approximate isometry error. For what follows, we let $\phi(\tau):=\max\{\tau,\tau^{2}\}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

(4.8) cannot generally be improved to $o_{T}$ whenever $\rho(A)\geqslant 1$. This can be seen from considering a random walk with a scaled identity noise covariance, i.e., $A=I_{d}$ and $\Sigma_{\mathcal{W}}=\sigma^{2}I_{d}$. Therefore, $\Sigma_{t}=t\sigma^{2}I_{d}$, and $\Gamma_{T}=\frac{T+1}{2}\sigma^{2}I_{d}$. We can further compute Therefore, fixing $m=1$ and taking $T\to\infty$: where $\left(x_{t}^{(i)}\right)_{1}$ denotes the first coordinate of $x_{t}^{(i)}$, and $W(\cdot)$ denotes the standard Wiener process.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

The second step holds by that $\left(x_{t}^{(i)}\right)_{1}$ is a 1D random walk, and therefore one can apply the 1D Donsker's theorem \[Billingsley1999, Theorem 8.2\] combined with the continuous mapping theorem \[Vaart1998, Theorem 2.3\]. Now, by the portmanteau lemma \[Vaart1998, Lemma 2.2\], Hence, this shows that $(\mathbb{E}\lVert I_{d}-\bar{\Sigma}_{m,T}\rVert_{\mathsf{op}}^{r})^{1/r}$ cannot be $o_{T}$ in general when $\rho(A)\geqslant 1$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Upper bounding $T_{2}^{\\textnormal{OLS}}$", "weight": 1.0} -->

Our analysis of $T_{2}^{\text{OLS}}$ builds on the arguments given in \[tu2024manytraj, Lemma 5.1\]. In order to utilize this result, we need to choose the correct normalization factor $N$ depending on if we are in the (i) many trajectories setting or (ii) the strictly stable setting. We remark it is the analysis of $T_{2}^{\text{OLS}}$ which crucially relies on the trajectory small-ball assumption (Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Upper bounding $T_{2}^{\\textnormal{OLS}}$", "weight": 1.0} -->

We first start with the many trajectories ($m\gtrsim d$) setting. Here, we pick $N=\Gamma_{T}$, in which case $T_{2}^{\text{OLS}}$ reduces to This is precisely the quantity studied in \[tu2024manytraj, Lemma 5.1\].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Upper bounding $T_{2}^{\\textnormal{OLS}}$", "weight": 1.0} -->

Next, we turn to the strictly stable ($\rho(A)<1$) setting. Here, after the burn-in time $\kappa=\kappa(A)$, where $\kappa(A)$ is defined in (2.13), both $\Gamma_{\kappa}$ and $\Gamma_{T}$ are approximately isometric with respect to each other, independent of the relative scale between $\kappa$ and $T$. This approximate isometry is formalized by the following result.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We derived non-asymptotic parameter error bounds for linear system identification with general non-isotropic sub-Gaussian noise that nearly matches the rate predicted by asymptotic normality, for error measured in both the Frobenius norm and operator norm.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

These results open up several further research directions. One immediate direction is in studying to what extent that the "burn-in" requirements prescribed by (3.1 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) and (3.2 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) (resp. (3.4 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) and (3.5 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"))) to get within a $(1+\varepsilon)$-factor (resp. $O$) of the asymptotic error for Frobenius norm (resp. for operator norm) are sharp. Another technical extension would be eliminating the extra $\log^{2}(d)$ in the operator norm bound, so that it matches the CLT-predicted rate exactly. This would require a sharper analysis of the operator norm of a matrix-valued martingale.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

More broadly, our results remain valid when the error metric is the general Schatten-$p$ norm. However, the central limit behaviour of OLS error under general Schatten-$p$ norms is unexplored, and it is of interest to establish both asymptotic and non-asymptotic bounds in this setting. Finally, deriving optimal non-asymptotic results in the $m=o(d)$ setting when $\rho(A)\geqslant 1$ and $A$ is regular (so that OLS is consistent) remains a challenging open question.
