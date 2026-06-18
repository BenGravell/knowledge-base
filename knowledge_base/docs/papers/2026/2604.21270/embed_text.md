## Introduction

System identification---the task of recovering unknown parameters of a dynamical system from observed system behavior---is a central problem in control. While system identification has a long and rich history in the control theory literature, the rise of machine learning approaches to control has led to a recent surge of results, particularly in establishing non-asymptotic, finite-sample guarantees for parameter recovery \[simchowitz2018learning, sarkar2019near, Faradonbeh2018identification, Ziemann2023\]. Such bounds are valuable both for characterizing the statistical limits of system identification, and for providing principled guidance on the data requirements needed to learn accurate models in practice.

Despite this remarkable progress, we argue that existing state-of-the-art bounds still fail to fully capture the statistical complexity of system identification---surprisingly even in the most basic setting of estimating the dynamics matrix of a discrete-time linear dynamical system (LDS) given one or many trajectories of state observations using ordinary least-squares (OLS) regression, a model known as the ${VAR}{}$ (vector auto-regressive) model which we focus on in this work. At first glance, this statement seems to contradict existing claims of minimax-optimality of OLS for this setting \[simchowitz2018learning, jedra2019lowerbounds, jedra2020lti\]. However, a more careful introspection reveals that minimax-optimal rates are only sharp on a carefully selected set of problem instances; they do *not* guarantee sharp rates on every problem instance.

Concretely, we consider two setups where asymptotic normality can be used to compute the exact instance-specific problem scaling: (i) strictly stable transition dynamics, and (ii) the many trajectories \[tu2024manytraj\] setting, where the number of independent trajectories outnumber the dimension. We remark that (i) and (ii) are not mutually exclusive. Our analysis reveals many problem instances where the sharpest known OLS bounds *overestimate* the squared parameter estimation error, in either Frobenius or operator norm, by a factor of the state-dimension. These instances are characterized by a sufficiently fast decay of the eigenvalues of either the noise covariance matrix or the inverse state covariance matrix, so that trace $\operatorname{\mathsf{t}\mathsf{r}}{(M)}$ of said matrices is significantly smaller than $d{\parallel M\parallel}_{\mathsf{o}\mathsf{p}}$, where $d$ is the state-dimension and ${\parallel M\parallel}_{\mathsf{o}\mathsf{p}}$ is the operator norm. A practical setting where this naturally arises is when disturbances enter the system in a non-uniform way, such as through an approximately low-rank subspace, or due to different physical scaling across state variables.

We then turn to the problem of sharpening the non-asymptotic OLS bounds to match the instance-specific optimal rates from asymptotic normality. We establish sufficient conditions on the trajectory length in the case of stable transition dynamics, and on the number of trajectories in the many trajectories setting, for the squared parameter error of the OLS estimator to match the instance-specific optimal rate up to a constant factor in Frobenius norm, and up to ${polylog}{(d)}$ factors in operator norm. At a high level, the deficiency of existing approaches is rooted in the standard decomposition of the OLS error introduced by \[simchowitz2018learning\], which splits the OLS error into two terms that are analyzed separately: (i) a self-normalized martingale term \[abbasi2011online\], and (ii) the minimum eigenvalue of the empirical state covariance matrix. We propose a novel second-order decomposition where the lowest order term becomes a simpler matrix-valued martingale that captures the CLT scaling. In Frobenius norm analyzing said martingale is immediate thanks to the inner-product structure, but for the operator norm extracting the CLT scaling is non-trivial and relies on the machinery of non-commutative Burkholder inequalities \[randrianantoanina07, junge2008\]. Returning back to our second-order decomposition, the new higher-order term places a stronger requirement on the empirical state covariance---namely a $p$-th moment approximate isometry condition---for which we establish by taking inspiration from the Hanson-Wright approach described in \[jedra2020lti\].

Our paper is organized as follows. In Section 2, we formalize the problem setting, discuss in detail what target rates we should expect from asymptotic normality, and illustrate examples where existing bounds are loose. In Section 3, we state our main non-asymptotic results for both Frobenius and operator norms. Section 4 provides a detailed proof outline, and Section 5 concludes with future directions. All proof details are deferred to Appendices A to C.

### Related Work

We focus our literature discussion on both asymptotic and finite-sample analysis of parameter estimation in discrete-time linear dynamical systems with full state observation; see \[Ziemann2023, hazan2025research\] for a broader overview of recent non-asymptotic results and perspectives, and \[ljung1999system\] for a classical treatment.

The starting point for non-asymptotic error analysis of the OLS estimator is due to \[simchowitz2018learning\], which controls the operator norm of the parameter error via decomposition into a self-normalized process and the minimum eigenvalue of empirical covariance. In the case where the underlying process is stable, \[jedra2020lti\] improves the required sample complexity for $(\varepsilon,\delta)$-PAC, although as $\varepsilon\rightarrow 0$ the leading order term is the same. We will show that, in the case where the noise matrix is non-isotropic, these results can be loose. The work \[ziemann2023noiselevel\] controls the excess risk (squared parameter error in a weighted Frobenius norm by the process covariance) of OLS for the stable setting, and matches the CLT variance order-wise; such a bound immediately yields control of the squared Frobenius norm of the parameter error. However as we will also discuss, this conversion introduces un-necessary conservatism in the bound. Most related to this paper is the work \[tu2024manytraj\], which initiates a study of multi-trajectory estimation for dependent linear regression (in contrast, all aforementioned papers consider the single trajectory setting). Similar to \[ziemann2023noiselevel\], the presented bounds are also for excess risk, and suffer from the same conversion issue. One additional notable digression in \[tu2024manytraj\] compared to the aforementioned papers is in controlling the *expected value* of excess risk, instead of with high probability; this requires several key technical tools, which we build off of in this work.

On the asymptotic side, there is a well-established literature on the strong consistency and asymptotic normality of single trajectory OLS for both autoregressive \[lai1983autoregressive, lai1982leastsquares\] and vector autoregressive \[anderson1992asymptotic\] models. In Section 2.1 we will discuss these results, specifically \[anderson1992asymptotic\], in more detail. However, we limit our discussions to the setting when the transition matrix is strictly stable, as single trajectory asymptotic distributions are significantly more involved in the marginal and explosive cases \[white1958limiting, phillips2013inconsistent\]. On the other hand, for the multi-trajectory setting, when the number of trajectories tends to infinity, we can utilize classical $M$-estimation theory \[Vaart1998\] to study the asymptotics regardless of the stability of the dynamics matrix; we also discuss this in detail in Section 2.1.

## Background and Problem Statement

Consider the linear dynamical system evolving in ${\mathbb{R}}^{d}$:

where ${\{ w_{t}\}}_{t \geqslant 0}$ is a noise process satisfying $w_{t}\overset{i.i.d.}{\sim}\mathcal{W}$. We assume $\mathcal{W}$ is zero-mean and has a finite positive definite covariance, which we denote ${\Sigma_{\mathcal{W}}:={{\mathbb{E}}_{w \sim \mathcal{W}}\left\lbrack {ww^{\mathsf{T}}} \right\rbrack}}.$ We observe $m$ i.i.d. trajectories from (2.1), in the form of $\mathcal{D}_{m,T}:={\{{\{ x_{t}^{(i)}\}}_{t = 1}^{T + 1}\}}_{i = 1}^{m}$. The OLS estimator for $A$ is:

Our goal is to study the squared parameter error under both the Frobenius and operator (spectral) norm. Specifically, denoting a problem instance by a tuple $(A,\mathcal{W})$, we seek optimal instance-specific upper-bounds $\gamma_{F}$ and $\gamma_{\mathsf{o}\mathsf{p}}$:

${\mathbb{E}}\left\| {{\hat{A}}_{m,T} - A} \right\|_{F}^{2}$ ${\leqslant {\gamma_{F}(A,\mathcal{W})}},$ (2.3a)
${\mathbb{E}}\left\| {{\hat{A}}_{m,T} - A} \right\|_{\mathsf{o}\mathsf{p}}^{2}$ ${\leqslant {\gamma_{\mathsf{o}\mathsf{p}}(A,\mathcal{W})}}.$ (2.3b)

where the expectation is taken w.r.t. the training data $\mathcal{D}_{m,T}$.

In this paper, we consider two primary problem regimes. The first is the *strictly stable* regime, where the dynamics matrix $A$ satisifes ${\rho{(A)}} < 1$, with $\rho{( \cdot )}$ denoting the spectral radius. The second is the *many trajectories* regime \[tu2024manytraj\], where no assumptions are made on $A$, but instead we assume that $m \geqslant {Cd}$, where $C$ is a universal constant *independent* of $A$. Note that these two regimes are *not* mutually exclusive; for problem instances that fall into both regimes, both sets of corresponding results apply.

### Asymptotic Normality of OLS

We first discuss the asymptotic normality of the OLS estimator, which is the key tool for us in establishing the correct forms of the bounds $\gamma_{F}$ and $\gamma_{\mathsf{o}\mathsf{p}}$ in (2.3).^11^1Appendix A contains the proofs for all claims in this subsection.

In our formulation, there are two variables, $m$ and $T$, that can either be separately or jointly sent to infinity, depending on the problem instance. We first consider holding $T$ fixed and taking $m$ to infinity, which does not require any assumptions on $A$. Indeed, by classical asymptotic normality of $M$-estimation (see e.g. \[Vaart1998\]), as $m\rightarrow\infty$,

where $\Gamma_{T}:={\frac{1}{T}{\sum_{t = 1}^{T}\Sigma_{t}}}$ and $\Sigma_{t}:={\sum_{k = 0}^{t - 1}{A^{k}\Sigma_{\mathcal{W}}{(A^{k})}^{\mathsf{T}}}}$.

On the flip side, in order to send $T$ to infinity (either while holding $m$ fixed or jointly tending to infinity as well), we need to impose some assumptions on $A$. In general, the OLS estimator is not consistent when $A$ is irregular, i.e., the geometric multiplicity of any unstable eigenvalues of $A$ exceeds one (see e.g., \[phillips2013inconsistent, Faradonbeh2018identification, sarkar2019near\]). Furthermore, when $A$ is regular but not strictly stable, the limiting error distributions are not Gaussian \[white1958limiting, chan1988limiting\] and require functional CLT arguments to study. Hence, for sending $T$ to infinity, we will focus only on strictly stable dynamics. Specifically, when ${\rho{(A)}} < 1$, extending classical results such as \[anderson1992asymptotic, Theorem 1\], we have as $T\rightarrow\infty$,

where $\Sigma_{\infty}:={\sum_{t = 0}^{\infty}{A^{t}\Sigma_{\mathcal{W}}{(A^{t})}^{\mathsf{T}}}}$.

We note that the right-hand-side of both (2.4) and (2.5) can be further unified via a joint limit on $(m,T)$. Let $\phi:{{\mathbb{N}}_{+}\mapsto{\mathbb{N}}_{+}}$ be any function such that ${\phi{(m)}}\rightarrow\infty$ as $m\rightarrow\infty$. Then for the joint limit $(m,T_{m})$ with $T_{m}:={\phi{(m)}}$, as $m\rightarrow\infty$, one can show using the Lindeberg-Feller CLT \[Vaart1998, Proposition 2.27\],

With the asymptotic limits (2.4), (2.5), and (2.6) in place, we now discuss how these limit distributions imply the correct form of both $\gamma_{F}$ and $\gamma_{\mathsf{o}\mathsf{p}}$. The key idea is the following fact. Suppose ${\{\Delta_{n}\}}_{n \geqslant 1}$ is a sequence of random vectors in ${\mathbb{R}}^{k}$ satisfying ${\sqrt{n}\Delta_{n}}\overset{d}{↝}{\mathsf{N}{(0,V)}}$ and $\parallel \cdot \parallel$ is an arbitrary norm on ${\mathbb{R}}^{k}$. If the sequence ${\{{n{\parallel\Delta_{n}\parallel}^{2}}\}}_{n \geqslant 1}$ is uniformly integrable, then ${\lim_{n\rightarrow\infty}{{n \cdot {\mathbb{E}}}{\parallel\Delta_{n}\parallel}^{2}}} = {{\mathbb{E}}_{g \sim {\mathsf{N}{(0,I_{k})}}}{\parallel{V^{1/2}g}\parallel}^{2}}$. Hence we will utilize the expression ${\mathbb{E}}_{g}{\parallel{V^{1/2}g}\parallel}^{2}$ to compute what the optimal form of both $\gamma_{F}$ (with $\parallel \cdot \parallel$ the $\ell_{2}$-norm) and $\gamma_{\mathsf{o}\mathsf{p}}$ (with ${\parallel \cdot \parallel} = {\parallel{{mat}{( \cdot )}}\parallel}_{\mathsf{o}\mathsf{p}}$) should be.

### Asymptotic Analysis in Frobenius Norm

For the Frobenius norm, from the limit distributions in Section 2.1, we immediately identify our target goal for the quantity $\gamma_{F} = {\gamma_{F}(A,\mathcal{W})}$ in (2.3a) as the following:

Note that the goal (2.7) is consistent with both $m\rightarrow\infty$ limits (2.4) as well as $T\rightarrow\infty$ limits (2.5), (2.6), as $\Gamma_{T}\rightarrow\Sigma_{\infty}$ with $T\rightarrow\infty$ whenever $A$ is strictly stable.

We now remark on the difference between the stated goal (2.7) and existing results in the literature. We first compare to existing work in the strictly stable regime, which are stated for a single trajectory ($m = 1$). Here, most parameter error bounds in the literature are in terms of the operator norm of the error, which we will also discuss shortly. However, via the norm equivalence inequality ${\parallel{{\hat{A}}_{m,T} - A}\parallel}_{F}^{2} \leqslant {d{\parallel{{\hat{A}}_{m,T} - A}\parallel}_{\mathsf{o}\mathsf{p}}^{2}}$, operator norm bounds also imply Frobenius norm bounds. Furthermore, most bounds work under the simplification $\Sigma_{\mathcal{W}} = {\sigma^{2}I_{d}}$, which we will further assume here for comparison. Let $K:=\max_{i \in {\lbrack d\rbrack}}{\parallel w_{i}\parallel}_{\psi_{2}}$ denote the maximum $\psi_{2}$-norm of each coordinate of $w \sim \mathcal{W}$, and suppose all coordinates are independent. Note that by definition, $K \geqslant \sigma$. A prototypical operator norm bound is from \[jedra2020lti\], which states that for strictly stable $A$, when ${T\lambda_{\min}{(\Gamma_{T})}} \gtrsim {{\max{\{ K^{2},K^{4}\}}}\mathcal{J}{(A)}^{2}{({d + {\log{({1/\delta})}}})}}$ where ${\mathcal{J}{(A)}}:={\sum_{t \geqslant 0}{\parallel A^{t}\parallel}_{\mathsf{o}\mathsf{p}}}$, with probability at least $1 - \delta$,^22^2For this comparison, we ignore the difference between expected value and high probability. However, we note that converting the typical high probability result in the literature to an expected value bound is non-trivial, as typical results require e.g., the trajectory length $T$ to scale as $\log{({1/\delta})}$ where $\delta$ is the failure probability. ${\parallel{{\hat{A}}_{1,T} - A}\parallel}_{\mathsf{o}\mathsf{p}}^{2} \lesssim \frac{K^{2}{({d + {\log{({1/\delta})}}})}}{T\lambda_{\min}{(\Sigma_{\infty})}}$. Using the norm inequality:

We see that this is qualitatively looser than (2.7) in Goal 1, since both $\sigma^{2} \leqslant K^{2}$ and ${\operatorname{\mathsf{t}\mathsf{r}}{(\Sigma_{\infty}^{- 1})}} \leqslant {{d/\lambda_{\min}}{(\Sigma_{\infty})}}$. \[tu2024manytraj, Theorem 5.8\] also states a similar bound as (2.8) in expectation (the bound has extra log-factors due to it being applicable to marginally stable dynamics; these can be removed by specializing the proof to strictly stable $A$).

Let us now compare to existing results in the many trajectories setting. The most relevant result is \[tu2024manytraj, Theorem 5.5\], which states that as long as $m \gtrsim d$, we have that the *excess risk* is optimally controlled as:

While this excess risk bound is optimal, directly converting it to a Frobenius error bound via ${\parallel{{\hat{A}}_{m,T} - A}\parallel}_{\Gamma_{T}}^{2} \geqslant {\lambda_{\min}{(\Gamma_{T})}{\parallel{{\hat{A}}_{m,T} - A}\parallel}_{F}^{2}}$ implies the result:

which again is looser than the stated goal (2.7).

We emphasize the difference between these two bounds. For concreteness we focus on the strictly stable, single trajectory setting with $\Sigma_{\mathcal{W}} = I_{d}$ and $A = {{diag}{({(\sqrt{1 - {1/i^{2}}})}_{i = 1}^{d})}}$. Immediately, we have ${\operatorname{\mathsf{t}\mathsf{r}}{(\Sigma_{\infty}^{- 1})}} = {\sum_{i = 1}^{d}i^{- 2}} = {O{}}$ and ${\lambda_{\min}{(\Sigma_{\infty})}} = 1$. Hence, the bound in (2.8) yields ${\parallel{{\hat{A}}_{1,T} - A}\parallel}_{F}^{2} \lesssim {\overset{\sim}{O}{({{K^{2}d^{2}}/T})}}$, whereas (2.7) has the form $\gamma_{F} \lesssim {d/T}$. Here, we see two sources of gaps. First, the gap between $K$ and one can be arbitrarily large, even for scaled isotropic noise.^33^3Consider the r.v. ${{\mathbb{P}}{({X = {\pm M}})}} = {1/{({2M^{2}})}}$ and ${{\mathbb{P}}{({X = 0})}} = {1 - M^{- 2}}$. Here, ${{{\parallel X\parallel}_{\psi_{2}}^{2}/{\mathbb{E}}}{\lbrack X^{2}\rbrack}} = {M^{2}/{\log{({1 + M^{2}})}}}\rightarrow\infty$ as $M\rightarrow\infty$. Second, for state covariance matrices where the spectrum is highly non-uniform, there can be a non-trivial dimension factor gap between the state-of-the-art current rates and the optimal rate (2.7).^44^4We note that this example essentially illustrates the worst-case gap, as ${\parallel M\parallel}_{\mathsf{o}\mathsf{p}} \leqslant {\operatorname{\mathsf{t}\mathsf{r}}{(M)}} \leqslant {d{\parallel M\parallel}_{\mathsf{o}\mathsf{p}}}$ for any $d \times d$ PSD matrix $M$.

### Asymptotic Analysis in Operator (Spectral) Norm

Computing the correct form of $\gamma_{\mathsf{o}\mathsf{p}}$ for the operator norm is more involved, as the limiting asymptotic risk involves computing the largest singular value of a Gaussian random matrix, which does not typically admit a closed form expression. Concretely, for e.g., (2.4), we have ${\lim_{m\rightarrow\infty}{{m \cdot {\mathbb{E}}}{\parallel{{\hat{A}}_{m,T} - A}\parallel}_{\mathsf{o}\mathsf{p}}^{2}}} = {{\mathbb{E}}_{g \sim {\mathsf{N}{(0,I_{d^{2}})}}}{\parallel{{mat}{({{({{\Gamma_{T}^{- {1/2}}/\sqrt{T}} \otimes \Sigma_{\mathcal{W}}^{1/2}})}g})}}\parallel}_{\mathsf{o}\mathsf{p}}^{2}}$. The RHS expression is equal to ${T^{- 1} \cdot {\mathbb{E}}_{G}}{\parallel{\Sigma_{\mathcal{W}}^{1/2}G\Gamma_{T}^{- {1/2}}}\parallel}_{\mathsf{o}\mathsf{p}}^{2}$, where $G$ is a $d \times d$ matrix with i.i.d. $\mathsf{N}{}$ entries. Fortunately, the correct order of this expression is available via the Gaussian Chevet inequality \[vershynin2018high, Section 8.6\], as summarized below.

### Proposition 2.1

Let $G \in {\mathbb{R}}^{n \times p}$ have i.i.d. $\mathsf{N}{}$ entries, and ${A \in {\mathbb{R}}^{m \times n}},{B \in {\mathbb{R}}^{p \times q}}$ be fixed matrices. We have:

By 2.1 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), we have that ${\mathbb{E}}_{G}{\parallel\Sigma_{\mathcal{W}}^{1/2}G\Gamma_{T}^{- {1/2}}\parallel}_{\mathsf{o}\mathsf{p}}^{2} \asymp {\parallel\Sigma_{\mathcal{W}}\parallel}_{\mathsf{o}\mathsf{p}}\operatorname{\mathsf{t}\mathsf{r}}{(\Gamma_{T}^{- 1})} + \operatorname{\mathsf{t}\mathsf{r}}{(\Sigma_{\mathcal{W}})}{\parallel\Gamma_{T}^{- 1}\parallel}_{\mathsf{o}\mathsf{p}}$. Similar then to the Frobenius norm case, this yields the following target goal for the quantity $\gamma_{\mathsf{o}\mathsf{p}} = {\gamma_{\mathsf{o}\mathsf{p}}(A,\mathcal{W})}$ in (2.3b).

As in the Frobenius norm case, (2.10 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) is consistent with both $m\rightarrow\infty$ limits (2.4) as well as $T\rightarrow\infty$ limits (2.5), (2.6), as $\Gamma_{T}\rightarrow\Sigma_{\infty}$ with $T\rightarrow\infty$ whenever $A$ is strictly stable.

We again compare to the operator norm bound from \[jedra2020lti\], in the case when $\Sigma_{\mathcal{W}} = {\sigma^{2}I_{d}}$, $m = 1$, and $A$ is strictly stable. In this case, the target rate in (2.10 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) simplifies to $\frac{\sigma^{2}d}{T\lambda_{\min}{(\Sigma_{\infty})}}$, which shows that while the dependence on ${d/\lambda_{\min}}{(\Sigma_{\infty})}$ is correct in the rate from \[jedra2020lti\], the $\sigma^{2}$ vs. $K^{2}$ gap persists in operator norm as well. Modifications to the proof of \[tu2024manytraj, Theorem 5.5\] also show the same gap for many trajectories.

The issue is further exacerbated when $\Sigma_{\mathcal{W}}$ is no longer a scaled identity matrix, a setting that has received a lot less attention in the literature. To the best of our knowledge, the only explicit result in the literature covering non scaled-isotropic process noise is \[Faradonbeh2018identification\]. While their result handles general sub-Weibull process noise, we will instantiate their result for $\mathcal{W} = {\mathsf{N}{(0,\Sigma_{\mathcal{W}})}}$, i.e., sub-Weibull with $\alpha = 2$. From \[Faradonbeh2018identification, Corollary 1\], when $A$ is strictly stable, with probability at least $1 - \delta$,

where $\nu_{\mathcal{W}}:=\max_{i \in {\lbrack d\rbrack}}{(\Sigma_{\mathcal{W}})}_{ii}$, $\Psi{(A)}$ is an expression that depends on various properties of $A$'s Jordan decomposition, and $\overset{\sim}{O}{( \cdot )}$ hides log factors. Note that when $\Sigma_{\mathcal{W}} = {\sigma^{2}I_{d}}$, (2.11 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) does not reduce to (2.8). A sharper result in the non-isotropic sub-Gaussian $\mathcal{W}$ case can be derived for both the strictly stable and many trajectory setting by extending \[tu2024manytraj\]. For the strictly stable case for example,

where $K_{vec}^{2}:={\sup_{v \in {\mathbb{S}}^{d - 1}}{\parallel{\langle v,w\rangle}\parallel}_{\psi_{2}}^{2}}$, and similarly for the many trajectory setting.

Let us compare these bounds in the case where $\Sigma_{\mathcal{W}} = {\operatorname{diag}{({(i^{- 2})}_{i = 1}^{d})}}$ and $A = {\operatorname{diag}{({(\sqrt{1 - {1/i^{4}}})}_{i = 1}^{d})}}$, in which case $\Sigma_{\infty} = {\operatorname{diag}{({(i^{2})}_{i = 1}^{d})}}$. Here, (2.12 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) yields ${{\mathbb{E}}{\parallel{{\hat{A}}_{1,T} - A}\parallel}_{\mathsf{o}\mathsf{p}}^{2}} \lesssim {{K_{vec}^{2}d}/T}$, whereas (2.10 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) states $\gamma_{\mathsf{o}\mathsf{p}} \lesssim {1/T}$. We again see the two sources of gaps as we did in the Frobenius norm case; both in the gap between $K_{vec}$ and one, and due to non-isotropic state covariance matrices.

### Assumptions for Non-Asymptotic Analysis

Towards setting up and presenting our main non-asymtotic results, we first collect and discuss the various assumptions on the noise process ${\{ w_{t}\}}_{t \geqslant 0}$ that we utilize in our analysis. Throughout the article, we utilize the following notation:

with the understanding that $\mathcal{F}_{0}$ is the trivial $\sigma$-algebra. It is clear that ${\{ w_{t}\}}_{t \geqslant 0}$ is $\mathcal{F}_{t + 1}$-adapted and ${\{ x_{t}\}}_{t \geqslant 0}$ is $\mathcal{F}_{t}$-adapted. We begin by formalizing our aforementioned problem setting with an additional sub-Gaussianity condition.

### Assumption 2.2

We assume that ${\{ w_{t}\}}_{t \geqslant 0}$ satisfies:

$w_{t}\overset{i.i.d.}{\sim}\mathcal{W}$, ${{\mathbb{E}}_{w \sim \mathcal{W}}{\lbrack w\rbrack}} = 0$, $\Sigma_{\mathcal{W}} = {{\mathbb{E}}_{w \sim \mathcal{W}}{\lbrack{ww^{\mathsf{T}}}\rbrack}} \succ 0$.

For $w \sim \mathcal{W}$, $\overline{w}:={\Sigma_{\mathcal{W}}^{- {1/2}}w}$ is directionally $\nu$-sub-Gaussian: for any $\lambda \in {\mathbb{R}}$,

Assumption 2.2 is fairly standard in the non-asymptotic LDS identification literature \[simchowitz2018learning, sarkar2019near, tu2024manytraj\], as it provides access to sub-Gaussian self-normalized martingale tail bounds \[abbasi2011online\]. This assumption alone, however, is insufficient for our purposes, as we also need to control the behaviour of the empirical covariance $\Sigma_{m,T}:={{({mT})}^{- 1}X_{m,T}^{\mathsf{T}}X_{m,T}}$ as part of the OLS error. We now introduce two additional assumptions. The first provides, in the two regimes we consider, high probability control on empirical covariance error ${\parallel{\Sigma_{m,T} - \Gamma_{T}}\parallel}_{\mathsf{o}\mathsf{p}}$. To state the assumption, we denote the entropy functional of a nonnegative integrable function $f$ with respect to a probability distribution $\mu$ as:

We also denote the whitened noise process ${\{{\overline{w}}_{t}\}}_{t \geqslant 0}:=\left\{ {\Sigma_{\mathcal{W}}^{- {1/2}}w_{t}} \right\}_{t \geqslant 0}$, and the whitened distribution of $\mathcal{W}$ as $\overline{\mathcal{W}}$, such that ${\overline{w}}_{t}\overset{i.i.d.}{\sim}\overline{\mathcal{W}}$.

### Assumption 2.3

We assume that $\overline{\mathcal{W}}$ satisfies *either* of the following:

$\overline{\mathcal{W}} = \otimes_{i = 1}^{d}{\overline{\mathcal{W}}}_{i}$ for one-dimensional distributions ${\overline{\mathcal{W}}}_{i}$, i.e., ${\overline{w}}_{t}$ has independent coordinates.

$\overline{\mathcal{W}}$ satisfies the log-Sobolev inequality ${LS}{(\nu^{2})}$: for any continuously differentiable $f \in {L^{2}{(\overline{\mathcal{W}})}}$ such that ${\nabla f} \in {L^{2}{(\overline{\mathcal{W}})}}$,

Assumption 2.3 $(i)$ is fairly standard, having appeared in several prior works on LTI identification \[sarkar2019near, jedra2020lti\]. On the other hand, Assumption 2.3 $({ii})$ is non-standard, and we will discuss verifying it in a moment. The role of Assumption 2.3 is to allow us to obtain concentration of ${\parallel{\Sigma_{m,T} - \Gamma_{T}}\parallel}_{\mathsf{o}\mathsf{p}}$ via different Hanson-Wright inequalities \[RudelsonVershynin2013, adamczak15\]. Specifically, Assumption 2.3 $(i)$ gives access to the classical Hanson-Wright inequality \[RudelsonVershynin2013\] requiring independence, here across time $t$ and across the coordinates of ${\overline{w}}_{t}$. On the other hand, Assumption 2.3 $({ii})$ enables the use of a Hanson-Wright inequality under the convex concentration property \[adamczak15\], where the whitened noise distribution $\overline{\mathcal{W}}$ is allowed to have dependencies between coordinates, but must instead satisfy a geometric restriction. We note that for Assumption 2.3 $({ii})$, requiring the constant for log-Sobolev inequality to coincide with the sub-Gaussian constant in Assumption 2.2 $({ii})$ is without loss of generality, as $\overline{\mathcal{W}}$ satisfying ${LS}{(C)}$ implies $\overline{\mathcal{W}}$ is directionally $\sqrt{C}$-sub-Gaussian (cf. Lemma D.4).

Now off the typical events where we have concentration of ${\parallel{\Sigma_{m,T} - \Gamma_{T}}\parallel}_{\mathsf{o}\mathsf{p}}$, we still require control on how degenerate $\Sigma_{m,T}$ can become. Hence, our next assumption, from \[tu2024manytraj, Definition 4.1\], yields control on the *lower tail* of $\lambda_{\min}{(\Sigma_{m,T})}$, and generalizes small-ball conditions in the i.i.d. setting \[mourtada2022exact\].

### Assumption 2.4 (Trajectory small-ball (Traj-SB))

Assume the state trajectory ${\{ x_{t}\}}_{t \geqslant 0}$ from (2.1) defined by $(A,\mathcal{W})$ satisfies the trajectory small-ball condition: for any trajectory length $T$, there exists constants $c \geqslant 1$ and $\alpha \in {(0,1\rbrack}$ such that for any excitation window size $k \in {\lbrack T\rbrack}$, window index $j \in {\{ 1,\ldots,{\lfloor{T/k}\rfloor}\}}$, $v \in {{\mathbb{R}}^{d} \smallsetminus {\{ 0\}}}$, and $\varepsilon > 0$:

We now discuss verifying Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). It turns out that a very broad family of distributions $\overline{\mathcal{W}}$ can be readily shown to simultaneously satisfy these assumptions, namely the class of log-concave distributions. $\overline{\mathcal{W}}$ is said to be log-concave if it is (a) absolutely continuous w.r.t. the Lebesgue measure on ${\mathbb{R}}^{d}$ (denoted $\lambda_{d}$), (b) supported on a convex set $S$, and (c) the negative log density $\psi_{\overline{\mathcal{W}}}:={- {\log\frac{d\overline{\mathcal{W}}}{d\lambda_{d}}}}$ is convex on $S$. By Carbery and Wright's classical work on anti-concentration for polynomials of log-concave distributions (see \[carbery2001distributional, Theorem 8\] and \[tu2024manytraj, Example 4.6\]), a log-concave $\overline{\mathcal{W}}$ implies Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). Next, it turns out that there are two cases where additionally we have that Assumption 2.3 $({ii})$ holds (which then implies Assumption 2.2). The first case (*strongly log-concave*, or SLC for short), is when $\psi_{\overline{\mathcal{W}}}$ is twice-differentiable and $\nu^{- 2}$-strongly-convex (i.e., ${\nabla^{2}\psi_{\overline{\mathcal{W}}}} \succcurlyeq {\nu^{- 2}I_{d}}$ everywhere on $S$); this follows from the classic Bakry-Émery criteria \[Bakry2014\]. The second case (*bounded log-concave*, or BLC for short), is when the support $S$ has diameter bounded as $O{(\nu^{2})}$, which is the result of recent work on stochastic localization \[leekls2024\]. This discussion is formalized in the following lemma.

### Lemma 2.5

Given a problem instance $(A,\mathcal{W})$, suppose that $\mathcal{W}$ satisfies Assumption 2.2 $(i)$, and $\overline{\mathcal{W}}$ satisfies *either* of the following (let $S$ denote the support of $\overline{\mathcal{W}}$, which we assume is convex):

$\psi_{\overline{\mathcal{W}}}$ is twice-differentiable and $\nu^{- 2}$-strongly-convex on $S$.

$\psi_{\overline{\mathcal{W}}}$ is convex and $S$ has a bounded diameter $O{(\nu^{2})}$.

Then Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") are satisfied.

We conclude our discussion on the noise assumptions by noting that although the natural intersection of Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") are log-concave distributions (as presented in Lemma 2.5), we present Assumption 2.3 $(i)$ as there readily exist product measures of one-dimensional sub-Gaussian distributions that violate the log-Sobolev inequality; see \[adamczak2005logarithmic, Section 2\]. However, we leave a general distributional characterization that implies Assumption 2.2, Assumption 2.3 $(i)$ and Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") as an open question.

Beside conditions on noise process, another important concept for the analysis of LDS identification is stability of $A$. Here we utilize a quantified definition of stability equivalent to the typical spectral radius definition.

### Definition 2.6 (Strict stability)

$A$ is $(M,\rho)$-*strictly-stable* if there exists $M > 0$ and $\rho < 1$ such that ${\parallel A^{k}\parallel}_{\mathsf{o}\mathsf{p}} \leqslant {M\rho^{k}}$ for all $k \in {\mathbb{N}}$.

For $A$ that is $(M,\rho)$-strictly-stable, we define the following quantity:

$\kappa{(A)}$ is intuitively a "burn-in" time for stable systems, in a sense that for any $T \geqslant {\kappa{(A)}}$, $\Gamma_{T}$ and $\Sigma_{\infty}$ are sufficiently approximately isometric for analysis purposes. Such a "burn-in" property plays an important role in obtaining sharp results for stable systems. We will revisit in detail the above discussions in Section 4.3.

## Main Results

We now state our main results in light of Goal 1 and Goal 2 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). For what follows, we denote the parameter error ${\hat{\Delta}}_{m,T}:={{\hat{A}}_{m,T} - A}$. We start with the Frobenius norm case.

### Theorem 3.1 (Frobenius norm case)

Suppose the problem instance $(A,\mathcal{W})$ satisfies Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). Then we have for any $q > 0$,

Many trajectories: If $m \gtrsim d$, then

Stable dynamics: If $A$ is $(M,\rho)$-strictly-stable (cf. 2.6. ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")), $T \geqslant {\kappa{(A)}}$, and ${mT} \gtrsim {{\max\left\{ {\kappa{(A)}},{\frac{M}{1 - \rho}\sqrt{\frac{{\parallel\Sigma_{\mathcal{W}}\parallel}_{\mathsf{o}\mathsf{p}}}{\lambda_{\min}{(\Gamma_{\infty})}}}} \right\}}d}$, then

Recall that $\kappa{(A)}$ is defined (2.13).

Here, $c_{1},c_{2}$ are universal constants.

With the tuning parameter $q$, 3.1. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") allows us to match Goal 1 arbitrarily closely. Fix a $q \in {}$, and in addition to the relevant hypothesis in 3.1. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), assume:

*Many trajectories:* suppose further that

*Stable dynamics:* suppose further that

Therefore, by letting $q\rightarrow 0$, we can drive the bound (3.3) arbitrarily close to Goal 1. We can also derive sufficient conditions for (3.1 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) and (3.2 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) using the inequalities ${\lambda_{\min}{(\Gamma_{T})}{\operatorname{\mathsf{t}\mathsf{r}}{(\Gamma_{T}^{- 1})}}} \geqslant 1$ and ${\operatorname{\mathsf{t}\mathsf{r}}{(\Sigma_{\mathcal{W}})}} \geqslant {\parallel\Sigma_{\mathcal{W}}\parallel}_{\mathsf{o}\mathsf{p}}$. Specifically, (3.1 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) holds whenever $m \gtrsim {{\nu^{6}d^{3}}/q^{2}}$, and also (3.2 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) holds whenever ${mT} \gtrsim {\frac{\nu^{6}d^{3}M}{q^{2}{({1 - \rho})}}\sqrt{\frac{{\parallel\Sigma_{\mathcal{W}}\parallel}_{\mathsf{o}\mathsf{p}}}{\lambda_{\min}{(\Sigma_{\infty})}}}}$. We leave the necessity of the conditions (3.1 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) and (3.2 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) for the error bound (3.3) to hold for future work.

We now turn to the operator norm case. For simplicity of notations, let us define for a PSD matrix $M \in {\mathbb{R}}^{d \times d}$, the operator ${\overline{\mathsf{t}\mathsf{r}}{(M)}}:={\max{\{{\operatorname{\mathsf{t}\mathsf{r}}{(M)}},{{\log{(d)}}{\parallel M\parallel}_{\mathsf{o}\mathsf{p}}}\}}}$. We also define the shorthand $\varphi_{T}:={{{\parallel\Sigma_{\mathcal{W}}\parallel}_{\mathsf{o}\mathsf{p}}/\lambda_{\min}}{(\Gamma_{T})}}$.

### Theorem 3.2 (Operator norm case)

Suppose the problem instance $(A,\mathcal{W})$ satisfies Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), and that $d \geqslant 8$. Then:

Many trajectories: If $m \gtrsim {{\max{\{ 1,\nu^{4}\}}}d}$, then

Stable dynamics: If $A$ is $(M,\rho)$-strictly-stable (cf. 2.6. ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")), $T \geqslant {\kappa{(A)}}$, and ${mT} \gtrsim {{\max\left\{ {\kappa{(A)}},{\frac{{\max{\{ 1,\nu^{4}\}}}M}{1 - \rho}\sqrt{\frac{{\parallel\Sigma_{\mathcal{W}}\parallel}_{\mathsf{o}\mathsf{p}}}{\lambda_{\min}{(\Gamma_{\infty})}}}} \right\}}d}$, then

Recall that $\kappa{(A)}$ is defined (2.13).

Unlike 3.1. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), 3.2. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") does not allow us to match Goal 2 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") exactly, due to the extra dimensionality factor $\log^{2}{(d)}$ in the leading term. Nonetheless, we can absorb the higher order terms into the leading term as follows. In addition to the relevent hypothesis in 3.2. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), suppose that the following holds:

*Many trajectories:* suppose further that

*Stable dynamics:* suppose further that

Unlike the Frobenius norm case, in the many trajectories setting, (3.4 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) requires that $m$ actually grows with $T$, specifically $m \geqslant {\Omega{(T^{2/{({{\log d} - 2})}})}}$, for the higher-order terms in 3.2. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") to be dominated by the lower-order $1/{({mT})}$ term. We believe this to be an artifact of our proof strategy, specifically the noncommutative Burkholder inequality we utilize (cf. Section 4.2). Resolving this is of future interest.

## Proof Ideas: Key Decompositions and Technical Tools

We first derive a new second-order error decomposition that is shared between the paths to both 3.1. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification") and 3.2. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). We start with the standard decomposition of the OLS error:

Note that under Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), ${\hat{\Sigma}}_{m,T}$ is invertible a.s. by \[tu2024manytraj, Corollary B.14\] given our requirements on $m$ (resp. $mT$) in the many trajectories setting (resp. stable dynamics setting), and therefore the above decomposition is well defined. The typical route for analyzing the OLS error proceeds by first decomposing the product above as:

where the first term is analyzed using concentration inequalities for self-normalized martingales, and the second term is controlled using small-ball techniques to lower bound the minimum eigenvalue. We take a departure from this route and instead write:

By triangle inequality and the AM-GM inequality, we have for any $q > 0$ the following *basic error inequality*:

where for a matrix $M$, ${\parallel \cdot \parallel}_{S_{p}}$ denotes the Schatten-$p$ norm ${\parallel M\parallel}_{S_{p}}:=\left( {\operatorname{\mathsf{t}\mathsf{r}}{({({M^{\mathsf{T}}M})}^{p/2})}} \right)^{1/p}$; note that $p = 2$ yields the Frobenius norm, and $p = \infty$ yields the operator norm.

Outline: We will show that $T_{1}$ matches the corresponding rates in Goal 1 or Goal 2 Norm ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), whereas $T_{2}$ is of higher order. The analysis of $T_{1}$ differs depending on the norm: it is simple to analyze under Frobenius norm due to inner product structure (cf. Section 4.1), but requires a noncommutative Burkholder inequality \[randrianantoanina07\] for the operator norm (cf. Section 4.2). On the other hand, the analysis of term $T_{2}$ is independent of the norm, and builds on the Hanson-Wright inequality \[vershynin2018high, adamczak15\] in addition to existing OLS analysis under the trajectory small-ball condition \[tu2024manytraj\] (cf. Section 4.3).

### Analysis of Term $T_{1}$ for Frobenius Norm

For the Frobenius norm, we have:

Furthermore, ${\mathbb{E}}{\lbrack{{\hat{Q}}_{m,T}^{\mathsf{T}}{\hat{Q}}_{m,T}}\rbrack}$ admits a simple closed form:

where $(a)$ follows from independence across trajectories, and $(b)$ follows from applying iterated expection with respect to smaller time indices. Hence,

### Analysis of Term $T_{1}$ for Operator Norm

Unlike the Frobenius norm analysis in Section 4.1, the operator norm analysis for $T_{1}$ is more challenging, as there is no inherent inner-product structure. Instead, we will exploit that $T_{1}$ is the second moment of the Schatten-$\infty$ norm of a matrix-valued martingale ${\hat{Q}}_{m,T}\Gamma_{T}^{- 1}$. Such types of moment bounds in their full generality are known as noncommutative Burkholder inequalities \[randrianantoanina07, junge2008\]. The following lemma is a direct implication of \[randrianantoanina07, Theorem 4.1\] tailored to bounding $T_{1}$ under the operator norm.

### Proposition 4.1

Fix a filtration ${\{\mathcal{G}_{i}\}}_{i \geqslant 0}$. Let ${\{ D_{i}\}}_{i \geqslant 1}$ be a matrix-valued martingale difference sequence where $D_{i}$ takes values in ${\mathbb{R}}^{d \times d}$ and is $\mathcal{G}_{i}$-measurable, and let $M_{t}:={\sum_{i = 1}^{t}D_{i}}$. Then if $d \geqslant 8$, for any $t \in {\mathbb{N}}_{+}$ and $r \geqslant {\log d}$,

Some remarks are in order. First, the requirement that $d \geqslant 8$ and $r \geqslant {\log d}$ results from converting the Haagerup $L^{r}$-norm, under which the original result is stated, to operator norm. Eliminating such a requirement is of future interest. Second, aside from the Burkholder inequality, one can also use the matrix Freedman inequality \[Tropp2011\] to establish control on ${\mathbb{E}}{\parallel M_{t}\parallel}_{\mathsf{o}\mathsf{p}}^{2}$. However, due to the boundedness assumption in \[Tropp2011, Theorem 1.1\], this approach will introduce a $\log{({mT})}$ factor in the final bound due to a truncation argument.

To apply 4.1 for analyzing $T_{1}$, we denote $M_{mT}:={{\hat{Q}}_{m,T}\Gamma_{T}^{- 1}} = {\sum_{j = 1}^{mT}D_{j}}$, where

and where the ordering is $i_{j}:={{\lfloor{{({j - 1})}/T}\rfloor} + 1}$ and $t_{j}:={{({{({j - 1})}\operatorname{mod}T})} + 1}$; this corresponds to flattening the time index $t$ first. Focusing on the first two terms of the bound in 4.1 (the main terms that generalize quadratic variation), for any $r \geqslant 1$,

A key tool for bounding these two terms is an approximate isometry condition on the empirical covariance ${\hat{\Sigma}}_{m,T}$. This approximate isometry also plays a key role in the analysis of term $T_{2}$, which we will turn to shortly in Section 4.3. Bounding the last term in 4.1 involves controlling moments of the form ${\mathbb{E}}{\lbrack{{\parallel w_{t}\parallel}^{r}{\parallel{\Gamma_{T}^{- 1}x_{t}}\parallel}^{r}}\rbrack}$, which we handle using standard concentration inequalities for sub-Gaussian random vectors. We remark that it is precisely this third term that gives rise to the $T^{2/{\log d}}$ dependence in (3.4 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) in the context of 3.2. ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). We conclude this section with the result obtained from the above analysis.

### Lemma 4.2

Given a problem instance $(A,\mathcal{W})$, suppose that ${\{ w_{t}\}}_{t \geqslant 0}$ satisfies Assumptions 2.2 to 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"), and furthermore $d \geqslant 8$. We have the following:

If $m \gtrsim {{\max{\{\nu^{2},\nu^{4}\}}}d}$, then

If $A$ is $(M,\rho)$-strictly stable, ${mT} \gtrsim \frac{{\max{\{\nu^{2},\nu^{4}\}}}{\parallel\Sigma_{\mathcal{W}}^{1/2}\parallel}_{\mathsf{o}\mathsf{p}}Md}{\lambda_{\min}{(\Gamma_{T}^{1/2})}{({1 - \rho})}}$ and $T \geqslant {\kappa{(A)}}$, then

### Analysis of Term $T_{2}$

We now turn to our analysis of term $T_{2}$. We denote the whitened version of ${\hat{Q}}_{m,T}$ and ${\hat{\Sigma}}_{m,T}$ as follows:

Via elementary operations, we write ${\hat{Q}}_{m,T}{({{\hat{\Sigma}}_{m,T}^{- 1} - \Gamma_{T}^{- 1}})}$ as:

We now introduce an arbitrary positive definite normalization matrix $N \in {\mathbb{R}}^{d \times d}$, whose purpose will be explained soon in Section 4.3.2. We can upper bound $\left\| {{\hat{Q}}_{m,T}{({{\hat{\Sigma}}_{m,T}^{- 1} - \Gamma_{T}^{- 1}})}} \right\|_{S_{p}}^{2}$ as follows:

where $(a)$ applies the inequality ${\parallel{MN}\parallel}_{S_{p}} \leqslant {{\parallel M\parallel}_{S_{p}}{\parallel M\parallel}_{\mathsf{o}\mathsf{p}}}$. Now using the Cauchy-Schwarz inequality and the inequality ${\parallel M\parallel}_{S_{p}} \leqslant \min{\{ d_{1},d_{2}\}}^{1/p}{\parallel M\parallel}_{\mathsf{o}\mathsf{p}}$ for $M \in {\mathbb{R}}^{d_{1} \times d_{2}}$, we have:

As suggested by the notation, $T_{2}^{\text{AIP}}$ measures the approximate isometry property (AIP) of the whitened empirical covariance ${\overline{\Sigma}}_{m,T}$, whereas $T_{2}^{\text{OLS}}$ measures the typical bound on OLS error (cf. Equation 4.1), specifically the norm of a self-normalized martingale divided by the minimum eigenvalue of an empirical covariance matrix.

### Upper bounding $T_{2}^{\text{AIP}}$

Taking inspiration from the work of \[jedra2020lti\], we utilize the Hanson-Wright inequality \[RudelsonVershynin2013, adamczak15\] to control the $r$-th moments of the approximate isometry error. For what follows, we let ${\phi{(\tau)}}:={\max{\{\tau,\tau^{2}\}}}$.

### Lemma 4.3

Let $(A,\mathcal{W})$ denote a problem instance satisfying Assumption 2.2 and Assumption 2.3. For any $r \geqslant 1$,

If in addition $A$ is $(M,\rho)$-strictly-stable, then for any $r \geqslant 1$,

### Remark 4.4

(4.8) cannot generally be improved to $o_{T}{}$ whenever ${\rho{(A)}} \geqslant 1$. This can be seen from considering a random walk with a scaled identity noise covariance, i.e., $A = I_{d}$ and $\Sigma_{\mathcal{W}} = {\sigma^{2}I_{d}}$. Therefore, $\Sigma_{t} = {t\sigma^{2}I_{d}}$, and $\Gamma_{T} = {\frac{T + 1}{2}\sigma^{2}I_{d}}$. We can further compute

Therefore, fixing $m = 1$ and taking $T\rightarrow\infty$:

where $\left( x_{t}^{(i)} \right)_{1}$ denotes the first coordinate of $x_{t}^{(i)}$, and $W{( \cdot )}$ denotes the standard Wiener process. The second step holds by that $\left( x_{t}^{(i)} \right)_{1}$ is a 1D random walk, and therefore one can apply the 1D Donsker's theorem \[Billingsley1999, Theorem 8.2\] combined with the continuous mapping theorem \[Vaart1998, Theorem 2.3\]. Now, by the portmanteau lemma \[Vaart1998, Lemma 2.2\],

Hence, this shows that ${({{\mathbb{E}}{\parallel{I_{d} - {\overline{\Sigma}}_{m,T}}\parallel}_{\mathsf{o}\mathsf{p}}^{r}})}^{1/r}$ cannot be $o_{T}{}$ in general when ${\rho{(A)}} \geqslant 1$.

### Upper bounding $T_{2}^{\text{OLS}}$

Our analysis of $T_{2}^{\text{OLS}}$ builds on the arguments given in \[tu2024manytraj, Lemma 5.1\]. In order to utilize this result, we need to choose the correct normalization factor $N$ depending on if we are in the (i) many trajectories setting or (ii) the strictly stable setting. We remark it is the analysis of $T_{2}^{\text{OLS}}$ which crucially relies on the trajectory small-ball assumption (Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")).

We first start with the many trajectories ($m \gtrsim d$) setting. Here, we pick $N = \Gamma_{T}$, in which case $T_{2}^{\text{OLS}}$ reduces to

This is precisely the quantity studied in \[tu2024manytraj, Lemma 5.1\].

Next, we turn to the strictly stable (${\rho{(A)}} < 1$) setting. Here, after the burn-in time $\kappa = {\kappa{(A)}}$, where $\kappa{(A)}$ is defined in (2.13), both $\Gamma_{\kappa}$ and $\Gamma_{T}$ are approximately isometric with respect to each other, independent of the relative scale between $\kappa$ and $T$. This approximate isometry is formalized by the following result.

### Proposition 4.5

Suppose that $A$ is $(M,\rho)$-strictly-stable, and that $T \geqslant {\kappa{(A)}}$. Then,

With 4.5 in place, we use the normalizer $N = \Gamma_{\kappa{(A)}}$, for which $T_{2}^{\text{OLS}}$ reduces to

Similar to $T_{\text{many}}^{\text{OLS}}$, the quantity $T_{\text{stable}}^{\text{OLS}}$ can also be controlled via similar arguments as in \[tu2024manytraj, Lemma 5.1\]. The following result collects the resulting bounds for both cases.

### Lemma 4.6

Let $(A,\mathcal{W})$ denote a problem instance with $\mathcal{W}$ satisfying Assumption 2.2 and Assumption 2.4). ‣ 2.4. Assumptions for Non-Asymptotic Analysis ‣ 2. Background and Problem Statement ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"). Let $r \geqslant 1$ be arbitrary. We have:

If $A$ is $(M,\rho)$-strictly stable, and we further assume that both $T \gtrsim \kappa$ and ${mT} \gtrsim {r\kappad}$, then

## Conclusion and Future Work

We derived non-asymptotic parameter error bounds for linear system identification with general non-isotropic sub-Gaussian noise that nearly matches the rate predicted by asymptotic normality, for error measured in both the Frobenius norm and operator norm.

These results open up several further research directions. One immediate direction is in studying to what extent that the "burn-in" requirements prescribed by (3.1 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) and (3.2 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) (resp. (3.4 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification")) and (3.5 ‣ 3. Main Results ‣ CLT-Optimal Parameter Error Bounds for Linear System Identification"))) to get within a $({1 + \varepsilon})$-factor (resp. $O{}$) of the asymptotic error for Frobenius norm (resp. for operator norm) are sharp. Another technical extension would be eliminating the extra $\log^{2}{(d)}$ in the operator norm bound, so that it matches the CLT-predicted rate exactly. This would require a sharper analysis of the operator norm of a matrix-valued martingale. More broadly, our results remain valid when the error metric is the general Schatten-$p$ norm. However, the central limit behaviour of OLS error under general Schatten-$p$ norms is unexplored, and it is of interest to establish both asymptotic and non-asymptotic bounds in this setting. Finally, deriving optimal non-asymptotic results in the $m = {o{(d)}}$ setting when ${\rho{(A)}} \geqslant 1$ and $A$ is regular (so that OLS is consistent) remains a challenging open question.
