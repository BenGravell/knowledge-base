## Introduction

Originating from the celebrated Ho-Kalman algorithm \[(https://arxiv.org/html/2501.16639v2#bib.bib1)\], subspace identification methods (SIMs) have proven extremely useful for estimating linear state-space models and became one of the mainstream approaches in system identification. Over the past 50 years, numerous efforts have been made to develop improved algorithms and gain a deeper understanding of them. For a comprehensive overview of SIMs, we refer to \[(https://arxiv.org/html/2501.16639v2#bib.bib2), (https://arxiv.org/html/2501.16639v2#bib.bib3)\]. Overall speaking, SIMs can be categorized into two types, namely, the open-loop and closed-loop. Open-loop SIMs were developed first and formed the basis for the development of closed-loop ones. Some representative open-loop SIMs are canonical variate analysis (CVA) \[(https://arxiv.org/html/2501.16639v2#bib.bib4)\], numerical algorithms for subspace state-space system identification (N4SID) \[(https://arxiv.org/html/2501.16639v2#bib.bib5)\], multivariable output-error state-space (MOESP) algorithms \[(https://arxiv.org/html/2501.16639v2#bib.bib6)\], the observer-Kalman filter method (OKID) \[(https://arxiv.org/html/2501.16639v2#bib.bib7)\], and the parsimonious SIM (PARSIM) \[(https://arxiv.org/html/2501.16639v2#bib.bib8), (https://arxiv.org/html/2501.16639v2#bib.bib9)\]. Despite the significant theoretical and practical success of SIMs, certain limitations remain--most notably, their lower accuracy compared to the prediction error method (PEM) in the case of exogenous inputs being present, and the lack of a comprehensive statistical analysis. A thorough statistical analysis of SIMs is essential to establish their reliability, assess their performance, and guide the design of more robust and efficient algorithms and the choice of user choices.

### Related Work

There are some significant contributions to statistical properties of SIMs in the asymptotic regime \[(https://arxiv.org/html/2501.16639v2#bib.bib10), (https://arxiv.org/html/2501.16639v2#bib.bib11), (https://arxiv.org/html/2501.16639v2#bib.bib12), (https://arxiv.org/html/2501.16639v2#bib.bib13), (https://arxiv.org/html/2501.16639v2#bib.bib14), (https://arxiv.org/html/2501.16639v2#bib.bib15), (https://arxiv.org/html/2501.16639v2#bib.bib16), (https://arxiv.org/html/2501.16639v2#bib.bib17), (https://arxiv.org/html/2501.16639v2#bib.bib18), (https://arxiv.org/html/2501.16639v2#bib.bib19), (https://arxiv.org/html/2501.16639v2#bib.bib20), (https://arxiv.org/html/2501.16639v2#bib.bib21), (https://arxiv.org/html/2501.16639v2#bib.bib22), (https://arxiv.org/html/2501.16639v2#bib.bib23)\]. The consistency and asymptotic variance of SIMs are analyzed in \[(https://arxiv.org/html/2501.16639v2#bib.bib13), (https://arxiv.org/html/2501.16639v2#bib.bib21)\] and \[(https://arxiv.org/html/2501.16639v2#bib.bib16), (https://arxiv.org/html/2501.16639v2#bib.bib17), (https://arxiv.org/html/2501.16639v2#bib.bib18), (https://arxiv.org/html/2501.16639v2#bib.bib19), (https://arxiv.org/html/2501.16639v2#bib.bib20)\], respectively. In particular, it was pointed out in \[(https://arxiv.org/html/2501.16639v2#bib.bib13)\] that the persistence of excitation (PE) of inputs is not sufficient for consistency, and stronger conditions are required in some cases. In addition, the impact of some weighting matrices in the SVD step was discussed in \[(https://arxiv.org/html/2501.16639v2#bib.bib24), (https://arxiv.org/html/2501.16639v2#bib.bib25)\], which claim that the choices of weighting matrices mainly influence the asymptotic distribution of the estimates. Although the CVA method gives the lowest variance among available weighting choices when the measured inputs are white \[(https://arxiv.org/html/2501.16639v2#bib.bib11)\], there is no formal proof to show that it is asymptotically efficient \[(https://arxiv.org/html/2501.16639v2#bib.bib23)\]. In the asymptotic regime, convergence rates can be derived using the central limit theorem (CLT) or the law of the iterated logarithm (LIL) \[(https://arxiv.org/html/2501.16639v2#bib.bib26)\]. However, such results only hold as the number of samples tends to infinity. In reality, all data is finite. Asymptotic results serve primarily as heuristics and often fall short in capturing transient behaviors, explaining performance differences among SIM variants in finite sample settings, or determining how much data is needed to get a model with which we are satisfied.

There has been a recent resurgence of interest in identifying state-space models, where the focus is on the non-asymptotic regime. Finite sample analysis in the field of system identification was pioneered by \[(https://arxiv.org/html/2501.16639v2#bib.bib27), (https://arxiv.org/html/2501.16639v2#bib.bib28)\], where the performance of PEMs was analyzed. Over the last few years, a series of papers have revisited this topic and introduced many promising developments on fully observed systems \[(https://arxiv.org/html/2501.16639v2#bib.bib29), (https://arxiv.org/html/2501.16639v2#bib.bib30), (https://arxiv.org/html/2501.16639v2#bib.bib31)\] and partially observed systems \[(https://arxiv.org/html/2501.16639v2#bib.bib32), (https://arxiv.org/html/2501.16639v2#bib.bib33), (https://arxiv.org/html/2501.16639v2#bib.bib34), (https://arxiv.org/html/2501.16639v2#bib.bib35), (https://arxiv.org/html/2501.16639v2#bib.bib36), (https://arxiv.org/html/2501.16639v2#bib.bib37)\]. For a broader overview of these results, we refer to \[(https://arxiv.org/html/2501.16639v2#bib.bib38)\]. As stated in \[(https://arxiv.org/html/2501.16639v2#bib.bib32)\], finite sample analysis has been a standard tool for comparing algorithms. Such an analysis of SIMs can provide a qualitative characterization of learning complexity and elucidate data-accuracy trade-offs. Moreover, it can guide the choice of user choices, such as the horizons and weighting matrices, which may lead to an improvement of the estimator in a two-step approach. However, the path of finite sample analysis for SIMs proves to be challenging due to the involvement of multi-step statistical operations \[(https://arxiv.org/html/2501.16639v2#bib.bib19)\], such as regression, projection, weighted SVD and maximum likelihood (ML) estimation. While these steps enhance performance, they simultaneously pose challenges for any subsequent statistical analysis. Putting the studies on fully observed systems aside, the most relevant studies on partially observed systems are \[(https://arxiv.org/html/2501.16639v2#bib.bib33), (https://arxiv.org/html/2501.16639v2#bib.bib39), (https://arxiv.org/html/2501.16639v2#bib.bib32), (https://arxiv.org/html/2501.16639v2#bib.bib36)\]. However, they mainly analyze the performance of the Ho-Kalman algorithm or similar variants which are rarely used in practice, their results therefore are not sufficient to completely reveal statistical properties of SIMs actually deployed. To the best of our knowledge, a complete finite sample analysis of SIMs under general conditions is still an open problem.

### Contributions

The main contributions of this paper are three-fold:

\(1\) We develop a robust and scalable framework for finite sample analysis of a broad class of SIMs. To avoid non-causal models caused by the projection step in classical SIMs, we propose to use PARSIM to enforce a causal model. Such a choice brings convenience to statistical analysis, and the method can be applied to other ARX-based SIMs, such as SSARX \[(https://arxiv.org/html/2501.16639v2#bib.bib40)\] and PBSID \[(https://arxiv.org/html/2501.16639v2#bib.bib21)\].

\(2\) We establish a more general PE condition. Compared with related studies that only include past inputs and past outputs as regressors, our work also includes future inputs as regressors, leading to a more general PE condition. This broader PE condition is instrumental in deriving error bounds and in analyzing the use of data-dependent weighting matrices. Therefore, it serves as a contribution of independent interest.

\(3\) Compared with related studies that streamline the realization algorithm, we provide the first finite sample upper bounds on system matrices under different weighting matrices and two popular realization algorithms.

A preliminary version \[(https://arxiv.org/html/2501.16639v2#bib.bib41)\] of this work was accepted by IEEE, where we provide a finite sample analysis for a simplified PARSIM, i.e., without taking into account the weighting matrices and including the CVA type realization algorithm. In this full version, we include different weighting matrices and two popular realization algorithms. In addition, we also provide complete proofs and a technical framework to approach this problem.

### Structure

The disposition of the paper is as follows: In Section (https://arxiv.org/html/2501.16639v2#S2 "2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we introduce models and assumptions used in SIMs, and then formulate the problem explicitly. In Section (https://arxiv.org/html/2501.16639v2#S3 "3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we present a short review of SIMs with a focus on PARSIM, and the roadmap ahead to analyze its finite sample behavior. In Section (https://arxiv.org/html/2501.16639v2#S4 "4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we first provide a finite sample analysis of an individual ARX model, which we then combine with a union bound to control the performance of a bank of ARX models. In Section (https://arxiv.org/html/2501.16639v2#S5 "5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we first analyze certain robustness properties of weighted SVD, and then derive error bounds on the system matrices coming from two realization algorithms. In Section (https://arxiv.org/html/2501.16639v2#S6 "6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we discuss the implications of our main results. Finally, the paper is concluded in Section (https://arxiv.org/html/2501.16639v2#S7 "7 Conclusion ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). All proofs and technical lemmas are provided in the Appendix.

### Notations

\(1\) For a matrix $X$ with appropriate dimensions, $X^{\top}$, $X^{- 1}$, $X^{\frac{1}{2}}$, $X^{\dagger}$, $\parallel X\parallel$, ${\parallel X\parallel}_{F}$, $\det{(X)}$, ${rank}{(X)}$, ${trace}{(X)}$, $\rho{(X)}$, $\lambda_{\max}{(X)}$, $\lambda_{\min}{(X)}$, $\sigma_{\min}{(X)}$ and $\sigma_{n}{(X)}$ denote its transpose, inverse, square root, Moore-Penrose pseudo-inverse, spectral norm, Frobenius norm, determinant, rank, trace, spectral radius, maximum eigenvalue, minimum eigenvalue, minimum singular value and $n$-th largest singular value, respectively. Moreover, $X_{1} \succ {( \succcurlyeq )}$ $0$ and $X_{2} \prec {( \preccurlyeq )}$ $0$ mean that $X_{1}$ is positive (semi) definite and $X_{2}$ is negative (semi) definite, respectively. ${diag}{(X_{1},X_{2})}$ is a block matrix having $X_{1}$ and $X_{2}$ on its diagonal. The matrices $I$ and $0$ are the identity and zero matrices with compatible dimensions.

\(s\) The multivariate normal distribution with mean $\mu$ and covariance $\Sigma$ is denoted as $\mathcal{N}{(\mu,\Sigma)}$. The notation ${\mathbb{E}}\lbrack x\rbrack$ is the expectation of a random vector $x$. For an event $\mathcal{E}$, ${\mathbb{P}}{(\mathcal{E})}$ is the probability of $\mathcal{E}$, $\mathcal{E}^{c}$ is the complementary event of $\mathcal{E}$, and $\mathcal{E}_{1} \cup \mathcal{E}_{2}$ and $\mathcal{E}_{1} \cap \mathcal{E}_{2}$ are the union and intersection of events $\mathcal{E}_{1}$ and $\mathcal{E}_{2}$, respectively. We use ${\mathbb{I}}_{\{\mathcal{E}\}}$ to denote the indicator function of $\mathcal{E}$.

\(3\) The notation $f = {\mathcal{O}{(g)}}$ means that functions ${f,g} \in {\mathbb{R}}^{d}$ satisfy ${\operatorname{lim\ sup}_{x\rightarrow x_{0}}{|\frac{f{(x)}}{g{(x)}}|}} < \infty$, where the limit point $x_{0}$ is typically understood from the context. Moreover, $f \gtrsim g$ means $f$ is greater than or approximately equal to $g$.

\(4\) The notations $c$, $c_{1}$,... stand for universal constants independent of system parameters, confidence, and accuracy.

## Problem Formulation

### Models and Assumptions

Consider the following discrete-time linear time-invariant (LTI) system in innovations form:

where $x_{k} \in {\mathbb{R}}^{n_{x}}$, $u_{k} \in {\mathbb{R}}^{n_{u}}$, $y_{k} \in {\mathbb{R}}^{n_{y}}$ and $e_{k} \in {\mathbb{R}}^{n_{y}}$ are the state, input, output and innovations, respectively. For brevity of notation, we assume that the initial time starts at $k = 1$, and the terminal time is denoted as $\overline{N} = {{N + p + f} - 1}$, where $N$ is the number of columns in data Hankel matrices, and $p$ and $f$ stand for past and future horizons, respectively, to be defined later. In addition, the initial state is assumed to be $x_{1} = 0$. We make the following standard assumptions:

### Assumption 2.1

\(1\) The spectral radius of $A$ and $A_{K}$ satisfy ${\rho{(A)}} < 1$ and ${\rho{(A_{K})}} < 1$.

\(2\) The system is minimal, i.e., $(A,{\lbrack B,K\rbrack})$ is controllable and $(A,C)$ is observable.

\(3\) The innovations $\{ e_{k}\}$ consists of independent and identically distributed (i.i.d.) Gaussian random variables, i.e., $e_{k} \sim {\mathcal{N}{(0,I)}}$.^11^1Similar to \[(https://arxiv.org/html/2501.16639v2#bib.bib42)\], our results can be extended to more general setups, such as sub-Gaussians.

\(4\) The input sequence $\{ u_{k}\}$ consists also of i.i.d. Gaussian random variables, i.e., $u_{k} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$. Moreover, it is assumed independent of $\{ e_{k}\}$.

### Remark 1

To illustrate the generality of the innovations model ((https://arxiv.org/html/2501.16639v2#S2.E1 "In 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), we consider the following standard state-space model which divides the noise term into contributions from measurement noise $v_{k}$ acting on the outputs and process noise $w_{k}$ acting on the states \[(https://arxiv.org/html/2501.16639v2#bib.bib43)\]:

The noises $w_{k}$ and $v_{k}$ consist of i.i.d. zero-mean Gaussian random variables, with covariance $\Sigma_{w}$ and $\Sigma_{v}$, respectively. Moreover, they are independent of each other. We assume that $\Sigma_{v} \succ 0$, $(A,C)$ is detectable, and $(A,\Sigma_{w})$ is stabilizable. Then, the Kalman filter of system ((https://arxiv.org/html/2501.16639v2#S2.E2 "In Remark 1 ‣ 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is well defined, and the Kalman gain is equal to

where $P$ is the solution of the following Riccati equation:

We further assume that the initial state is a zero-mean Gaussian variable with covariance $P$ and independent of the noises. Then, by the orthogonality principle the innovations sequence also consists of i.i.d. Gaussian variables with covariance

Therefore, under mild conditions the innovations form ((https://arxiv.org/html/2501.16639v2#S2.E1 "In 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) describes the same input-output trajectories as the standard state-space model ((https://arxiv.org/html/2501.16639v2#S2.E2 "In Remark 1 ‣ 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), and it is widely used in SIMs \[(https://arxiv.org/html/2501.16639v2#bib.bib2)\].

Based on the innovations form, after replacing $\Sigma_{e}^{1/2}e_{k}$ in ([1a](https://arxiv.org/html/2501.16639v2#S2.E1.1 "In 1 ‣ 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) with $y_{k} - {Cx_{k}}$, we obtain the following predictor form:

where $A_{K} = {A - {KC}}$. Since the innovations form and the predictor form are equivalent and all can represent input and output data exactly, one has the option to use any of these forms for convenience. For instance, MOESP \[(https://arxiv.org/html/2501.16639v2#bib.bib6)\] and PARSIM \[(https://arxiv.org/html/2501.16639v2#bib.bib8)\] use the innovations form, and SSARX \[(https://arxiv.org/html/2501.16639v2#bib.bib40)\] and PBSID \[(https://arxiv.org/html/2501.16639v2#bib.bib23)\] use the predictor form.

### Problem Formulation

In this paper we tackle the following problem:

### Problem 1

Given a finite number $\overline{N}$ of input-output samples from a single trajectory of system ((https://arxiv.org/html/2501.16639v2#S2.E1 "In 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), our goal is to explicitly derive high probability error bounds on the system matrices estimated by some SIMs. To be specific, given a confidence level $0 < \delta < 1$, we wish to derive error bounds $\epsilon_{A},\epsilon_{B},\epsilon_{C}$, such that

hold with probability at least $1 - \delta$, where $\hat{A}$, $\hat{B}$ and $\hat{C}$ are estimates of system matrices, and $T$ is a non-singular matrix.

### Remark 2

It is only possible to obtain the system matrices up to a similarity transformation due to the non-uniqueness of a realization\[(https://arxiv.org/html/2501.16639v2#bib.bib33)\]. Moreover, it should be mentioned that the matrix $T$ here is stochastic, depending on the realization. Alternatively the estimates could be transformed into a canonical form. Furthermore, bounds on the estimation of Markov parameters or other system invariants could also be given.

Problem (https://arxiv.org/html/2501.16639v2#Thmproblem1 "Problem 1 ‣ 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") is one of the long-standing open problems in subspace identification. As noted by Van Overschee and De Moor \[(https://arxiv.org/html/2501.16639v2#bib.bib44)\], "solving these problems would contribute significantly to the maturing of the field of subspace identification." The existing literature already offers some pertinent solutions to Problem (https://arxiv.org/html/2501.16639v2#Thmproblem1 "Problem 1 ‣ 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). According to recent work \[(https://arxiv.org/html/2501.16639v2#bib.bib32), (https://arxiv.org/html/2501.16639v2#bib.bib42)\] in the non-asymptotic regime, the error bound $\epsilon_{\theta}$ is typically of the form

where $\theta$ denotes the parameter of interest, and SNR denotes the signal-to-noise ratio.

In the asymptotic regime, prior work \[(https://arxiv.org/html/2501.16639v2#bib.bib16), (https://arxiv.org/html/2501.16639v2#bib.bib17), (https://arxiv.org/html/2501.16639v2#bib.bib18), (https://arxiv.org/html/2501.16639v2#bib.bib19), (https://arxiv.org/html/2501.16639v2#bib.bib20)\] have shown that the normalized error $\sqrt{\overline{N}}\left( {\hat{\theta} - \theta} \right)$ converges in law to a normal distribution. Consequently, the results in ((https://arxiv.org/html/2501.16639v2#S2.E4 "In 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"))--where the error decays at rate $\mathcal{O}{({1/\sqrt{\overline{N}}})}$ and the confidence level $\delta$ appears through $\log{({1/\delta})}$--are consistent with these asymptotic results. Moreover, the LIL suggests that error decays at rate $\mathcal{O}{(\sqrt{\frac{\log{\log\overline{N}}}{\overline{N}}})}$ almost surely \[(https://arxiv.org/html/2501.16639v2#bib.bib10)\], which is sharp. However, asymptotic results require that $\overline{N}\rightarrow\infty$ and can only be used as a heuristic for a finite $\overline{N}$. Some questions remained unanswered. For instance, there often is a minimal requirement on $\overline{N}$, namely the burn-in time ${\overline{N}}_{\text{pe}}$, which is necessary for a bound of the form ((https://arxiv.org/html/2501.16639v2#S2.E4 "In 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) to hold. Such requirements are typically of the form

The above ${\overline{N}}_{\text{pe}}$ cannot be obtained by applying only asymptotic tools \[(https://arxiv.org/html/2501.16639v2#bib.bib38)\]. Moreover, as shown in \[(https://arxiv.org/html/2501.16639v2#bib.bib32)\] and Lemma (https://arxiv.org/html/2501.16639v2#Thmlemma1 "Lemma 1 ‣ 4.1 Persistence of Excitation ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") in this work, non-asymptotic analysis can even achieve an error bound for marginally stable systems, whereas asymptotic results are often limited to asymptotically stable systems.

Existing non-asymptotic results for Problem (https://arxiv.org/html/2501.16639v2#Thmproblem1 "Problem 1 ‣ 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") mainly focus on the classical Ho--Kalman algorithm or similar variants \[(https://arxiv.org/html/2501.16639v2#bib.bib33), (https://arxiv.org/html/2501.16639v2#bib.bib32), (https://arxiv.org/html/2501.16639v2#bib.bib36), (https://arxiv.org/html/2501.16639v2#bib.bib35)\]. However, this realization algorithm is outdated, as more powerful SIMs have later been proposed in the literature. Whether the structure in ((https://arxiv.org/html/2501.16639v2#S2.E4 "In 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) also holds for modern SIMs has therefore remained unclear. This work proves that modern SIMs also obey the same structure. Moreover, it is different in the following key respects.

First, a standard step of SIMs is to estimate a Hankel (or Hankel-like) matrix of Markov parameters, denoted by $\mathcal{H}_{fp}$. A key feature of modern SIMs is that $\mathcal{H}_{fp}$ is estimated directly using a projection method. However, this projection step couples future data with past data, resulting in an error without a standard martingale structure, which is difficult to upper bound. We believe that this is one of the main barriers preventing a finite sample analysis for SIMs. Previous analyses either revert to the Ho--Kalman algorithm \[(https://arxiv.org/html/2501.16639v2#bib.bib45)\] or avoid inputs \[(https://arxiv.org/html/2501.16639v2#bib.bib32)\], where the projection step is not involved, thereby sidestepping the problem. The way we solve it is to absorb the projection matrix into an enlarged regressor, so that the error restores a standard martingale structure. The price to pay is that this format requires a more complex yet tractable PE condition.

Second, in the model reduction step, due to the fact that $\mathcal{H}_{fp}$ is low-rank, some data-dependent weighting matrices $W_{1}$ and $W_{2}$ are pre-multiplied and post-multiplied to the estimate of $\mathcal{H}_{fp}$ before performing an SVD to improve the numerical and statistical properties. Several asymptotic properties of such algorithmic variations have been studied in \[(https://arxiv.org/html/2501.16639v2#bib.bib19)\]. However, it is an open problem to study the impact of weighting matrices and compare their performance in a finite sample setting \[(https://arxiv.org/html/2501.16639v2#bib.bib38), (https://arxiv.org/html/2501.16639v2#bib.bib44)\]. Prior work \[(https://arxiv.org/html/2501.16639v2#bib.bib32), (https://arxiv.org/html/2501.16639v2#bib.bib45), (https://arxiv.org/html/2501.16639v2#bib.bib35), (https://arxiv.org/html/2501.16639v2#bib.bib36)\] considered the trivial weighting $W_{1} = W_{2} = I$. This work delivers the first finite sample analysis for general weighting matrices through a novel analysis leveraging the Schur complement.

Third, unlike the Ho-Kalman algorithm, many SIMs typically estimate system matrices by first recovering the state sequences and then applying least-squares regression in the output and state equations. To the best of our knowledge, this realization algorithm has not been analyzed in the non-asymptotic regime. Our work shows that the error of this realization algorithm also obeys the structure of ((https://arxiv.org/html/2501.16639v2#S2.E4 "In 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")).

In summary, our work extends finite sample results from simplified prototypes to the algorithms actually deployed, offering new insights and systematic performance guarantees.

## Recap of Subspace Identification Methods

In this section we provide a short overview of open-loop SIMs, with the focus on PARSIM. For convenience, we define

which stack past inputs and future inputs, respectively. Similar definitions apply to $y_{p}{(k)}$, $e_{f}{(k)}$, $u_{i}{(k)}$ and $e_{i}{(k)}$. Moreover, after lining up $u_{p}{(k)}$ and $u_{f}{(k)}$ from $k = 1$ to $k = N$, we obtain Hankel matrices

Similar definitions apply to data matrices $Y_{p}$, $Y_{f}$, $E_{p}$ and $E_{f}$ \[(https://arxiv.org/html/2501.16639v2#bib.bib8)\]. The state sequence is given by

By iterating model ((https://arxiv.org/html/2501.16639v2#S2.E1 "In 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) using the above notations, an extended state-space model \[(https://arxiv.org/html/2501.16639v2#bib.bib8)\] can be derived as

where $\Gamma_{f}$ is the extended observability matrix, defined by

Moreover, the transmission matrices $G_{f}$ is a lower-triangular Toeplitz matrix of Markov parameters,

and $H_{f}$ is similarly defined by replacing $0$ on the diagonal of $G_{f}$ with $\Sigma_{e}^{\frac{1}{2}}$, and by replacing $B$ with $K\Sigma_{e}^{\frac{1}{2}}$. Similar definitions apply to matrices $\Gamma_{p}$, $G_{p}$ and $H_{p}$. Furthermore, by iterating equation ([3a](https://arxiv.org/html/2501.16639v2#S2.E3.1 "In 3 ‣ 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), we obtain

where $Z_{p} = \begin{bmatrix}
\end{bmatrix}^{\top}$ and $L_{p}$ is the extended controllability matrix in a reverse order, defined by

After substituting ((https://arxiv.org/html/2501.16639v2#S3.E11 "In 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) into ([8a](https://arxiv.org/html/2501.16639v2#S3.E8.1 "In 8 ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), we have

where $\mathcal{H}_{fp}:={\Gamma_{f}L_{p}}$ is the Hankel-like matrix. Most variants of SIMs can be integrated into a unified framework \[(https://arxiv.org/html/2501.16639v2#bib.bib46), (https://arxiv.org/html/2501.16639v2#bib.bib2)\] which generally consists of three steps. We now introduce them based on ((https://arxiv.org/html/2501.16639v2#S3.E13 "In 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")).

### Step 1: Linear Regression or Projection

Most open-loop SIMs use ((https://arxiv.org/html/2501.16639v2#S3.E13 "In 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) to first estimate the Hankel-like matrix $\mathcal{H}_{fp}$, and then proceed to obtain the system matrices. A basic approach in classical SIMs is one-step regression \[(https://arxiv.org/html/2501.16639v2#bib.bib6), (https://arxiv.org/html/2501.16639v2#bib.bib5), (https://arxiv.org/html/2501.16639v2#bib.bib13), (https://arxiv.org/html/2501.16639v2#bib.bib15)\], which takes $Z_{p}$ and $U_{f}$ as regressors and obtains $\mathcal{H}_{fp}$ and $G_{f}$ simultaneously using

Since $\mathcal{H}_{fp}$ is our main interest, using the inverse of a block matrix (see Lemma [13.10](https://arxiv.org/html/2501.16639v2#S13. "Lemma 13.10. ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), ${\hat{\mathcal{H}}}_{fp}$ can be extracted from ((https://arxiv.org/html/2501.16639v2#S3.E14 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) as

where $\Pi_{U_{f}}^{\perp} = {I - {U_{f}^{\top}{({U_{f}U_{f}^{\top}})}^{- 1}U_{f}}}$. Although the estimate ${\hat{\mathcal{H}}}_{fp}$ is consistent \[(https://arxiv.org/html/2501.16639v2#bib.bib15)\], the one-step regression method cannot preserve the lower-triangular Toeplitz structure of the transmission matrix $G_{f}$, which is responsible for recording the impact of future input $U_{f}$ on future output $Y_{f}$. Due to the loss of this structure in ${\hat{G}}_{f}$, the model format is not causal anymore, which poses a challenge in statistical analysis.

### Remark 3

In some literature of SIMs, the above one-step regression is called the projection method, in the sense that the future input $U_{f}$ is first projected out using

For a sufficiently large $p$, since $A_{K}^{p} \approx 0$, the rightmost term $\Gamma_{f}A_{K}^{p}X_{k - p}\Pi_{U_{f}}^{\perp}$ becomes negligible. Moreover, as $U_{f}$ is uncorrelated with $E_{f}$, we have ${E_{f}\Pi_{U_{f}}^{\perp}} \approx E_{f}$. After multiplying $Z_{p}^{\top}$ on both sides of ((https://arxiv.org/html/2501.16639v2#S3.E16 "In Remark 3 ‣ 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), we have

Since $E_{f}$ is uncorrelated with $Z_{p}$, implying ${\frac{1}{N}E_{f}Z_{p}^{\top}} \approx 0$, $\Gamma_{f}L_{p}$ can then be estimated using least-squares. It is clear that the estimate of $\Gamma_{f}L_{p}$ in ((https://arxiv.org/html/2501.16639v2#S3.E17 "In Remark 3 ‣ 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is identical to ((https://arxiv.org/html/2501.16639v2#S3.E15 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")).

To enforce causal models, a parallel and parsimonious SIM, PARSIM, is proposed in \[(https://arxiv.org/html/2501.16639v2#bib.bib8)\]. Instead of using the one-step regression, PARSIM zooms into each row of ((https://arxiv.org/html/2501.16639v2#S3.E13 "In 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) and performs $f$ least-squares to estimate a bank of ARX models. To illustrate this, equation ((https://arxiv.org/html/2501.16639v2#S3.E13 "In 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) can be partitioned row-wise as

where for $i = {1,2,{\ldotsf}}$, $\Gamma_{fi} = {CA^{i - 1}} \in {\mathbb{R}}^{n_{y} \times n_{x}}$,

where similar definitions apply to $E_{fi}$ and $E_{i}$. PARSIM then minimizes a bank of $i$-steps ahead prediction errors from model ((https://arxiv.org/html/2501.16639v2#S3.E18 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) using ordinary least-squares (OLS),

At last, the whole estimate of $\mathcal{H}_{fp}$ is obtained by stacking the $f$ estimates together as

It has been shown in \[(https://arxiv.org/html/2501.16639v2#bib.bib8)\] that the estimate in ((https://arxiv.org/html/2501.16639v2#S3.E20 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) admits a smaller variance than ((https://arxiv.org/html/2501.16639v2#S3.E15 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")).

### Step 2: Weighted SVD

Since $\mathcal{H}_{fp}$ has rank equal to $n_{x}$, to recover the extended observability matrix $\Gamma_{f}$ and controllability matrix $L_{p}$ from the estimate of $\mathcal{H}_{fp}$, weighted SVD is often used, i.e.,

where ${\hat{\Lambda}}_{1}$ contains the $n_{x}$ largest singular values. In this way, a balanced realization of ${\hat{\Gamma}}_{f}$ and ${\hat{L}}_{p}$ is

Different choices of weighting matrices $W_{1}$ and $W_{2}$ lead to different variants of SIMs \[(https://arxiv.org/html/2501.16639v2#bib.bib46), (https://arxiv.org/html/2501.16639v2#bib.bib2)\]. Popular candidates of weighting matrices are summarized in Table (https://arxiv.org/html/2501.16639v2#S3.T1 "Table 1 ‣ 3.2 Step 2: Weighted SVD ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). ^22^2Notice that those weightings are normalized and may not be the same as they appear in the referred papers. These weightings, however, give estimates of $\Gamma_{f}$ and $L_{p}$ identical to those obtained using the original choice of weighting \[(https://arxiv.org/html/2501.16639v2#bib.bib13)\].

${({\frac{1}{N}Z_{p}Z_{p}^{\top}})}^{\frac{1}{2}}$

${({\frac{1}{N}Z_{p}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}})}^{\frac{1}{2}}$

${({\frac{1}{N}Y_{f}\Pi_{U_{f}}^{\perp}Y_{f}^{\top}})}^{- \frac{1}{2}}$

${({\frac{1}{N}Y_{f}\Pi_{U_{f}}^{\perp}Y_{f}^{\top}})}^{- \frac{1}{2}}$
${({\frac{1}{N}Z_{p}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}})}^{\frac{1}{2}}$

Table 1: Candidates of weighting matrices

### Step 3: Realization of System Matrices

Given estimates of $\Gamma_{f}$ and $L_{p}$, there are two paths to obtain the system matrices. It should be mentioned that currently there is no solid conclusion on which realization leads to a better model. To be specific, one is the CVA type which uses the following linear regressions in the output and state equations to estimate the system matrices:

where $X_{k}^{+}$ stacks the states for the next time instant compared to $X_{k}$. By replacing $X_{k}$ and $X_{k}^{+}$ with their estimates

where $Z_{p}^{+}$ is similarly defined as $X_{k}^{+}$, we have

$\hat{C}$ ${= {Y_{f1}{\hat{X}}_{k}^{\dagger}}},$ (25a)
$\begin{bmatrix} ${= {{\hat{X}}_{k}^{+}\begin{bmatrix} (25b)
\hat{A} & \hat{B} {\hat{X}}_{k} \\
\end{bmatrix}^{\dagger}}}.$

Another realization method is the MOESP type, which directly extracts system matrices based on the shift invariance property of ${\hat{\Gamma}}_{f}$ and ${\hat{L}}_{p}$, i.e.,

$\hat{C}$ $= {\hat{\Gamma}}_{f}{(1:n_{y},:)},$ (26a)

where ${\hat{\Gamma}}_{f}^{+}$ and ${\hat{\Gamma}}_{f}^{-}$ are the last and first $f - 1$ row blocks of ${\hat{\Gamma}}_{f}$, and the indexing of matrices follows MATLAB syntax.

### Remark 4

In this paper, our main interest is to estimate the system matrices $\left\{ A,B,C \right\}$, and derive error bounds for them. In principle, the Kalman gain $K$ can also be obtained from the above algorithms with minor modifications. Meanwhile, there are also other methods to obtain $K$, such as solving a Riccati equation in N4SID and using QR factorization in PARSIM. To keep our results relatively compact, the estimate of $K$ and its error bound are not considered in this work.

### Roadmap Ahead

Now we sketch the path ahead to the solution for Problem (https://arxiv.org/html/2501.16639v2#Thmproblem1 "Problem 1 ‣ 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). In the first step that estimates the Hankel-like matrix $\mathcal{H}_{fp}$, we opt for PARSIM to facilitate the analysis. Parallel to the three steps in SIMs, we solve Problem (https://arxiv.org/html/2501.16639v2#Thmproblem1 "Problem 1 ‣ 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") by a three-step procedure:

\(1\) Step 1: We first derive an error bound on ${\hat{\Theta}}_{i}$ in ((https://arxiv.org/html/2501.16639v2#S3.E19 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) for every ARX model ((https://arxiv.org/html/2501.16639v2#S3.E18 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")). In other words, we define the following events for $i = {1,2,\ldots,f}$:

and require that ${{\mathbb{P}}{(\mathcal{E}_{i,\Theta}^{c})}} \leq \frac{\delta}{f}$. We then utilize a norm inequality (see Lemma [13.9](https://arxiv.org/html/2501.16639v2#S13.Thmtheorem9 "Lemma 13.9 (Lemma A.1 in ). ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) between the block matrix $\hat{\Gamma_{f}L_{p}} - {\Gamma_{f}L_{p}}$ and its sub-blocks $\hat{\Gamma_{fi}L_{p}} - {\Gamma_{fi}L_{p}}$ to obtain the total bound on ${\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}$. This essentially requires that the intersection of $f$ events has probability ${{\mathbb{P}}{({\bigcap_{i = 1}^{f}\mathcal{E}_{i,\Theta}})}} \geq {1 - \delta}$, which is guaranteed due to the union bound ${{\mathbb{P}}{({\bigcup_{i = 1}^{f}\mathcal{E}_{i,\Theta}^{c}})}} \leq \delta$.

\(2\) Step 2: We use recent results from SVD robustness \[(https://arxiv.org/html/2501.16639v2#bib.bib49), (https://arxiv.org/html/2501.16639v2#bib.bib33)\] to provide error bounds on the extended observability matrix $\Gamma_{f}$ and controllability matrix $L_{p}$, where the impact of different weighting matrices in Table (https://arxiv.org/html/2501.16639v2#S3.T1 "Table 1 ‣ 3.2 Step 2: Weighted SVD ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") is also discussed.

\(3\) Step 3: We derive error bounds $\epsilon_{A}$, $\epsilon_{B}$, and $\epsilon_{C}$ on the system matrices $\left\{ A,B,C \right\}$ coming from the Larimore and MOESP realization algorithms.

## Finite Sample Analysis of ARX Models

Following our roadmap, we formalize Step 1 above in this section. We emphasize that the results presented in this section apply to each ARX model in ((https://arxiv.org/html/2501.16639v2#S3.E18 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) for $i = {1,\ldots,f}$, where the subscript $i$ shows the model-specific dependence. For convenience, we define two covariates

$\phi_{p,i}{(k)}$ ${= \begin{bmatrix} (28a)
{y_{p}^{\top}{(k)}} & {u_{p}^{\top}{(k)}} & {u_{i}^{\top}{(k)}}
\end{bmatrix}^{\top} \in {\mathbb{R}}^{d_{p,i}}},$
$w_{p,i}{(k)}$ ${= {\Lambda_{u,e}^{- 1}\begin{bmatrix} (28b)
{u_{p}^{\top}{(k)}} & {u_{i}^{\top}{(k)}} & {e_{p}^{\top}{(k)}}
\end{bmatrix}^{\top}} \in {\mathbb{R}}^{d_{p,i}}},$

where $d_{p,i} = {{p{({n_{u} + n_{y}})}} + {in_{u}}}$ is the problem dimension of each ARX model, and $\Lambda_{e,u} = {{diag}{(\sigma_{u},\cdots,\sigma_{u},1,\cdots,1)}}$ normalizes $w_{p,i}{(k)}$, such that it has unite variance. We further partition the following matrices column-wise:

$\Phi_{p,i} =$ $\begin{bmatrix} (29a)
{\phi_{p,i}{}} & {\phi_{p,i}{}} & \cdots & {\phi_{p,i}{(N)}}

Moreover, we have the following definitions regarding the covariance and empirical covariance of $\phi_{p,i}{(k)}$ and $x_{k}$:

$\Sigma_{p,i,k}$ ${:={{\mathbb{E}}\left\lbrack {\phi_{p,i}{(k)}\phi_{p,i}^{\top}{(k)}} \right\rbrack}},$ (30a)
${\hat{\Sigma}}_{p,i,N}$ ${:={\frac{1}{N}{\sum\limits_{k = 1}^{N}{\phi_{p,i}{(k)}\phi_{p,i}^{\top}{(k)}}}}},$ (30b)
$\Sigma_{x,k}$ ${:={{\mathbb{E}}\left\lbrack {x_{k}x_{k}^{\top}} \right\rbrack}}.$ (30c)

Note that the regressor in ((https://arxiv.org/html/2501.16639v2#S3.E19 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) can be rewritten as

Then, the error of the OLS estimate ((https://arxiv.org/html/2501.16639v2#S3.E19 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) can be written as

There are two types of errors, namely, the cross-term error ${\overset{\sim}{\Theta}}_{i}^{E}$ and the truncation bias ${\overset{\sim}{\Theta}}_{i}^{B}$. A key observation is that the future innovations $e_{i}{(k)}$ are independent of the covariate $\phi_{p,i}{(l)}$ for all $l < k$. This provides a martingale structure, which is convenient to analyze. To bound the above two errors, we first use results from the smallest eigenvalue of the empirical covariance of causal Gaussian processes to lower bound ${\hat{\Sigma}}_{p,i,N}$ \[(https://arxiv.org/html/2501.16639v2#bib.bib50), (https://arxiv.org/html/2501.16639v2#bib.bib42), (https://arxiv.org/html/2501.16639v2#bib.bib36)\], which simultaneously establish the PE condition.

### Persistence of Excitation

To achieve PE, the number of samples $N$ should exceed a certain threshold, which we call the burn-in time $N_{pe}$.

### Definition 4.1

Given a failure probability $0 < \delta < 1$, a past horizon $p$, and a future horizon $i$ in each ARX model, the burn-in time $N_{pe}$ is defined as

where $N_{W}(\delta,p,i)$ and $N_{\Phi}(\delta,p,i)$ are defined in ([8.11](https://arxiv.org/html/2501.16639v2#S8.E11 "In 8.1 Proof of Lemma 1 ‣ 8 Burn-in Time and Persistence of Excitation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) and ([8.18](https://arxiv.org/html/2501.16639v2#S8.E18 "In 8.1 Proof of Lemma 1 ‣ 8 Burn-in Time and Persistence of Excitation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), respectively.

### Remark 5

As shown in Appendix (https://arxiv.org/html/2501.16639v2#S8 "8 Burn-in Time and Persistence of Excitation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), for any given $p$, $i$ and $\delta$, the $N$-dependent factors $N_{W}(\delta,p,i)$ and $N_{\Phi}(\delta,p,i)$ grow at most logarithmically with $N$. Therefore, for a sufficiently large $N$, the existence of $N_{pe}{(\delta,p,i)}$ is guaranteed.

A condition on PE is given the following lemma:

### Lemma 1

Fix a failure probability $0 < \delta < 1$. If $N \geq {N_{pe}{(\frac{\delta}{3},p,i)}}$, then, we have that with probability at least $1 - \delta$,

where ${\overline{\sigma}}_{p,i}:=\frac{\left\| \mathcal{T}_{p,i} \right\|\left\| \Lambda_{u,e} \right\|}{2} > 0$.

### Proof 4.1

See Appendix (https://arxiv.org/html/2501.16639v2#S8 "8 Burn-in Time and Persistence of Excitation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

### Remark 4.2

Some relevant PE conditions appear in \[(https://arxiv.org/html/2501.16639v2#bib.bib32)\] and \[(https://arxiv.org/html/2501.16639v2#bib.bib36)\], where past outputs and inputs are included in regressors. Our analysis extends this by additionally incorporating future inputs, thus establishing a more general PE condition. This broader result is also useful for analyzing data-dependent weighting matrices, as detailed in Section (https://arxiv.org/html/2501.16639v2#S5 "5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). Furthermore, this PE condition also holds for marginally stable systems.

### Bound on Cross-term Error

Based on Lemma (https://arxiv.org/html/2501.16639v2#Thmlemma1 "Lemma 1 ‣ 4.1 Persistence of Excitation ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), a upper bound on the cross-term error ${\overset{\sim}{\Theta}}_{i}^{E}$ in ((https://arxiv.org/html/2501.16639v2#S4.E32 "In 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is provided in the following lemma:

### Lemma 4.3

Fix a failure probability $0 < \delta < 1$. If $N \geq {N_{pe}{(\frac{\delta}{9},p,i)}}$, then with probability at least $1 - \delta$, we have

where $\epsilon_{i,E}^{2} = {\frac{\left\| H_{fi} \right\|^{2}}{{\overline{\sigma}}_{p,i}^{2}}\left( {{d_{p,i}\log\frac{d_{p,i}}{\delta}} + {\log\left( {\det\left( \frac{\Sigma_{p,i,N}}{{\overline{\sigma}}_{p,i}^{2}} \right)} \right)}} \right)}$.

### Proof 4.4

See Appendix (https://arxiv.org/html/2501.16639v2#S9 "9 Bound on Cross-term Error ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

### Bound on Truncation Bias

In order to ensure that the truncation bias term ${\overset{\sim}{\Theta}}_{i}^{B}$ decays much faster than the cross-term error ${\overset{\sim}{\Theta}}_{i}^{E}$, we make the following assumption regarding the past horizon $p$.

### Assumption 4.1

The past horizon is chosen as $p = {\beta\text{log}N}$, where $\beta$ is large enough such that

### Remark 4.5

To ensure that the model ((https://arxiv.org/html/2501.16639v2#S3.E18 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) closely approximates an ARX model, the truncation bias $\Gamma_{fi}A_{K}^{p}x_{k}$ should be small enough, which requires that the exponentially decaying term $A_{K}^{p}$ counteracts the magnitude of the state $x_{k}$. To illustrate this, we have that

As a consequence of Lemma [13.14](https://arxiv.org/html/2501.16639v2#S13. "Lemma 13.14 ([32, Lemma E.2 ]). ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), the state norm $\left\| \Sigma_{x,N} \right\|$ grows at most polynomially with $N$. Meanwhile, since ${\rho{(A_{K})}} < 1$, we have $\left\| A_{K}^{p} \right\| = {\mathcal{O}{({\overline{\rho}}^{p})}}$ for some $\overline{\rho} > {\rho{(A_{K})}}$. Taking $p = {\beta\text{log}N}$, we have $\left\| A_{K}^{p} \right\| = {\mathcal{O}{(N^{- {{\beta/\log}{({1/\overline{\rho}})}}})}}$, which implies that the condition ((https://arxiv.org/html/2501.16639v2#S4.E36 "In Assumption 4.1 ‣ 4.3 Bound on Truncation Bias ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is guaranteed for a large enough $\beta$.

Under Assumption [4.1](https://arxiv.org/html/2501.16639v2#S4.Thmassumption1 "Assumption 4.1 ‣ 4.3 Bound on Truncation Bias ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), a bound on the bias term ${\overset{\sim}{\Theta}}_{i}^{B}$ in ((https://arxiv.org/html/2501.16639v2#S4.E32 "In 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is provided in the following lemma:

### Lemma 4.6

Fix a failure probability $0 < \delta < 1$. If $N \geq {N_{pe}{(\frac{\delta}{9},{\beta\text{log}N},i)}}$, then with probability at least $1 - \delta$, we have

where $\epsilon_{i,B}^{2} = {\frac{n_{x}}{{\overline{\sigma}}_{p,i}^{2}}\log\frac{1}{\delta}}$.

### Proof 4.7

See Appendix (https://arxiv.org/html/2501.16639v2#S10 "10 Bound on Truncation Bias ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

### Overall Bound

Lemma [4.3](https://arxiv.org/html/2501.16639v2#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Bound on Cross-term Error ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") suggests that the cross-term error ${\overset{\sim}{\Theta}}_{i}^{E}$ decays as $\mathcal{O}{({1/\sqrt{N}})}$, and Lemma [4.6](https://arxiv.org/html/2501.16639v2#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.3 Bound on Truncation Bias ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") suggests that the truncation bias ${\overset{\sim}{\Theta}}_{i}^{B}$ decays as $\mathcal{O}{({1/N})}$. This implies that ${\overset{\sim}{\Theta}}_{i}^{B}$ is dominated by ${\overset{\sim}{\Theta}}_{i}^{E}$ and it can be considered negligible. After absorbing higher order terms into the dominant term by inflating the constants accordingly, we obtain the following theorem controlling the whole error ${\overset{\sim}{\Theta}}_{i}$ of each ARX model in our collection.

### Theorem 4.8

Fix a failure probability $0 < \delta < 1$. If $N \geq {N_{pe}{(\frac{\delta}{9},{\beta\text{log}N},i)}}$, then with probability at least $1 - {2\delta}$, we have

After obtaining an error bound on ${\overset{\sim}{\Theta}}_{i}$ in each ARX model, we proceed to bound the total error of $\mathcal{H}_{fp}$, which is crucial for our subsequent analysis. Based on the norm relation between a block matrix and its blocks in Lemma [13.9](https://arxiv.org/html/2501.16639v2#S13.Thmtheorem9 "Lemma 13.9 (Lemma A.1 in ). ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), it is straightforward to obtain a total bound on ${\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}$ from each bound $\left\| {\overset{\sim}{\Theta}}_{i} \right\|$.

### Theorem 4.9

Fix a failure probability $0 < \delta < 1$. If $N \geq {\max\limits_{1 \leq i \leq f}\left\{ {N_{pe}\left( \frac{\delta}{9f},{\beta\text{log}N},i \right)} \right\}}$, then with probability at least $1 - {2\delta}$, we have

where $\epsilon_{i}^{2} = {\frac{\left\| H_{fi} \right\|^{2}}{{\overline{\sigma}}_{p,i}^{2}}\left( {{d_{p,i}\log\frac{d_{p,i}f}{\delta}} + {\log\left( {\det\left( \frac{\Sigma_{p,i,N}}{{\overline{\sigma}}_{p,i}^{2}} \right)} \right)}} \right)}$.

## Robustness of Balanced Realization

Following our roadmap, having obtained an overall error bound on ${\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}$ in Step 1, we now move to Step 2 to derive error bounds on the extended controllability and observability matrices, and Step 3 to obtain error bounds on the system matrices.

### Weighted Singular Value Decomposition

Weighted SVD is crucial for improving the performance of SIMs. As summarized in Table (https://arxiv.org/html/2501.16639v2#S3.T1 "Table 1 ‣ 3.2 Step 2: Weighted SVD ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), different choices of weighting matrices lead to different variants of SIMs. Since those data-dependent weighting matrices share a similar structure, we choose the pair used in MOESP and PARSIM to illustrate their characteristics, where

The focus is on the data-dependent $W_{2}$, whose finite-sample properties are summarized as follows: ^33^3Similarly, conditions for other weighting matrices in Table (https://arxiv.org/html/2501.16639v2#S3.T1 "Table 1 ‣ 3.2 Step 2: Weighted SVD ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") can be obtained.

### Lemma 5.1

Fix a failure probability $0 < \delta < 1$. If $N \geq {N_{pe}{(\delta,p,f)}}$, then with probability at least $1 - {{3\delta}/2} - \delta_{u}$, where $\delta_{u} = {({2{({{N + f} - 1})}n_{u}})}^{- {\log^{2}{({2fn_{u}})}\log{({2{({{N + f} - 1})}n_{u}})}}}$, the weighting matrix $W_{2}$ in ((https://arxiv.org/html/2501.16639v2#S5.E40 "In 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) satisfies:

\(2\) $\left\| W_{2} \right\|$ grows at most logarithmically with $N$.

\(3\) $\left\| W_{2}^{- 1} \right\|$ is bounded.

### Proof 5.2

See Appendix (https://arxiv.org/html/2501.16639v2#S11 "11 Weighted Singular Value Decomposition ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

Now we study the robustness of SVD. Since other weighting matrices in Table (https://arxiv.org/html/2501.16639v2#S3.T1 "Table 1 ‣ 3.2 Step 2: Weighted SVD ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") have the same properties as in Lemma [5.1](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem1 "Lemma 5.1. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we will henceforth not specify a pair but use $W_{1}$ and $W_{2}$ to represent them universally. For simplicity, we further assume that $W_{1}$ and $W_{2}$ satisfy the conditions in Lemma [5.1](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem1 "Lemma 5.1. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") almost surely. The weighted SVD of the true value of $\mathcal{H}_{fp}$ is

where $\Lambda_{1} \succ 0$ contains the $n_{x}$ largest singular values. A balanced realization for $\Gamma_{f}$ and $L_{p}$ is

Then, we obtain the following robustness results regarding the estimates of $\Gamma_{f}$ and $L_{p}$.

### Theorem 5.3

If the following condition is satisfied:

then there exists an orthogonal matrix $T$, such that for a failure probability $0 < \delta < 1$, if $N \geq {\max\limits_{1 \leq i \leq f}\left\{ {N_{pe}{(\frac{\delta}{9f},{\beta\logN},i)}} \right\}}$, then with probability at least $1 - {2\delta}$, we have

$\left\| {{\hat{\Gamma}}_{f} - {{\overline{\Gamma}}_{f}T}} \right\|$ ${\leq {\sqrt{\frac{40n_{x}}{\sigma_{n_{x}}{(\mathcal{H}_{fp})}}}\left\| {{\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}} \right\|W_{\Gamma}}},$ (44a)
$\left\| {{\hat{L}}_{p} - {T^{\top}{\overline{L}}_{p}}} \right\|$ ${\leq {\sqrt{\frac{40n_{x}}{\sigma_{n_{x}}{(\mathcal{H}_{fp})}}}\left\| {{\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}} \right\|W_{L}}},$ (44b)

where $W_{\Gamma} = {\left\| W_{1} \right\|\left\| W_{2} \right\|\left\| W_{1}^{- 1} \right\|^{\frac{3}{2}}\left\| W_{2}^{- 1} \right\|^{\frac{1}{2}}}$ and $W_{L} = {\left\| W_{1} \right\|\left\| W_{2} \right\|\left\| W_{2}^{- 1} \right\|^{\frac{3}{2}}\left\| W_{1}^{- 1} \right\|^{\frac{1}{2}}}$.

### Proof 5.4

See Appendix (https://arxiv.org/html/2501.16639v2#S11 "11 Weighted Singular Value Decomposition ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

### Remark 5.5

Compared to a stochastic non-singular matrix $T$ in Problem (https://arxiv.org/html/2501.16639v2#Thmproblem1 "Problem 1 ‣ 2.2 Problem Formulation ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), matrix $T$ is constrained to be an orthogonal matrix in Theorem [5.3](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem3 "Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). This is mainly due to Lemma [13.12](https://arxiv.org/html/2501.16639v2#S13. "Lemma 13.12 ([32, Th. 4]). ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). Furthermore, according to the eigenvalue decomposition, every non-singular matrix has an associated orthogonal matrix. Therefore, such a constraint will not affect the generality of our results.

### Bounds on System Matrices

Having obtained upper bounds on the extended observability matrix ${\overline{\Gamma}}_{f}$ and controllability matrix ${\overline{L}}_{p}$ in Step 2, we now move to the final Step 3 to derive error bounds on the system matrices, where two realization algorithms are studied.

### CVA Type Realization

The error bounds on system matrices from the realization algorithm ((https://arxiv.org/html/2501.16639v2#S3.E25 "In 3.3 Step 3: Realization of System Matrices ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) are follows:

### Theorem 5.6

If the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is satisfied, then there exists an orthogonal matrix $T$, such that for a failure probability $0 < \delta < 1$, if $N \geq {\max\limits_{1 \leq i \leq f}\left\{ {N_{pe}{(\frac{\delta}{9f},{\beta\logN},i)}} \right\}}$, then with probability at least $1 - {2\delta}$, we have

${\left\| {\hat{C} - {\overline{C}T}} \right\| \leq {{c_{4}\left\| {{\hat{L}}_{p} - {T^{\top}{\overline{L}}_{p}}} \right\|} + {c_{5}\frac{\epsilon_{0,B}}{N}} + {c_{6}\frac{\epsilon_{0,E}}{\sqrt{N}}}}},$ (45a)
${\max\left\{ \left\| {\hat{A} - {T^{\top}\overline{A}T}} \right\|,\left\| {\hat{B} - {T^{\top}\overline{B}}} \right\| \right\}} \leq$
${{c_{7}\left\| {{\hat{L}}_{p} - {T^{\top}{\overline{L}}_{p}}} \right\|} + {c_{8}\frac{\epsilon_{1,B}}{N}} + {c_{9}\frac{\epsilon_{1,E}}{\sqrt{N}}}},$ (45b)

where detailed expressions of $c_{4},\ldots,c_{9}$, $\epsilon_{0,B}$, $\epsilon_{0,E}$, $\epsilon_{1,B}$ and $\epsilon_{1,E}$ are given in Appendix (https://arxiv.org/html/2501.16639v2#S12 "12 Bounds on System matrices ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

### Proof 5.7

See Appendix (https://arxiv.org/html/2501.16639v2#S12 "12 Bounds on System matrices ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

### MOESP Type Realization

The error bounds on system matrices from the realization algorithm ((https://arxiv.org/html/2501.16639v2#S3.E26 "In 3.3 Step 3: Realization of System Matrices ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) are follows:

### Theorem 5.8

If the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is satisfied, then there exists an orthogonal matrix $T$, such that for a failure probability $0 < \delta < 1$, if $N \geq {\max\limits_{1 \leq i \leq f}\left\{ {N_{pe}{({\delta/{({9f})}},{\beta\logN},i)}} \right\}}$, then with probability at least $1 - {2\delta}$, we have

$\left\| {\hat{C} - {\overline{C}T}} \right\|$ ${\leq \left\| {{\hat{\Gamma}}_{f} - {{\overline{\Gamma}}_{f}T}} \right\|},$ (46a)
$\left\| {\hat{B} - {T^{\top}\overline{B}}} \right\|$ ${\leq \left\| {{\hat{L}}_{p} - {T^{\top}{\overline{L}}_{p}}} \right\|},$ (46b)
$\left\| {\hat{A} - {T^{\top}\overline{A}T}} \right\|$ ${\leq {\frac{\sqrt{\left\| {\Gamma_{f}L_{p}} \right\|} + \sigma_{o}}{\sigma_{o}^{2}}\left\| {{\hat{\Gamma}}_{f} - {{\overline{\Gamma}}_{f}T}} \right\|}},$ (46c)

where $\sigma_{o} = {\min\left( {\sigma_{n_{x}}{({\hat{\Gamma}}_{f}^{-})}},{\sigma_{n_{x}}{({\overline{\Gamma}}_{f}^{-})}} \right)}$.

### Proof 5.9

See Appendix (https://arxiv.org/html/2501.16639v2#S12 "12 Bounds on System matrices ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods").

## Discussions

We now discuss the implications of our main results. Specifically, we will answer two key questions: how to extend our method to other variants of SIMs, and what does the finite sample analysis bring.

### Extensions to Other Methods

It is clear that our results in Steps 2 and 3 cover a large class of SIMs. In Step 1, to strictly enforce a causal model, we opt for the multi-regression method used in PARSIM--one of the most appealing SIMs, to estimate the Hankel-like matrix $\mathcal{H}_{fp}$. The following observations suggest that the technique used in the analysis of PARSIM can be extended to other SIMs.

First, our analysis for PARSIM can be extended to the one-step regression method in ((https://arxiv.org/html/2501.16639v2#S3.E15 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")). If we study the estimation error of $\mathcal{H}_{fp}$ in ((https://arxiv.org/html/2501.16639v2#S3.E15 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) separately, the cross-term error will be $E_{f}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}{({Z_{p}\Pi_{U_{f}}^{\perp}Z_{p}^{\top}})}^{- 1}$. Due to the data-dependent projection matrix $\Pi_{U_{f}}^{\perp}$, the columns of $E_{f}$ and $Z_{p}$ are mixed together, bringing challenges to statistical analysis. However, this problem can be avoided if we study the total error of $\Theta$ in ((https://arxiv.org/html/2501.16639v2#S3.E14 "In 3.1 Step 1: Linear Regression or Projection ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), which is equivalent to setting $i = f$ in PARSIM.

Second, our analysis can be extended to other SIMs that estimate high order ARX models using least-squares in their first step, such as SSARX\[(https://arxiv.org/html/2501.16639v2#bib.bib40)\] and PBSID \[(https://arxiv.org/html/2501.16639v2#bib.bib21)\]. To be specific, for SSARX, it first estimates the predictor Markov parameters $\left\{ {CA_{K}^{i}B},{CA_{K}^{i}K} \right\}_{i = 0}^{f - 1}$ from a high-order ARX model, and then replaces the true Markov parameters in the transmission matrices with their estimates, and proceeds to estimate a Hankel-like matrix. PBSID, also known as the whitening filter approach \[(https://arxiv.org/html/2501.16639v2#bib.bib21)\], starts from the predictor form ((https://arxiv.org/html/2501.16639v2#S2.E3 "In 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")). Similar to PARSIM, it utilizes the structure of the transmission matrices to carry out multiple regressions parallelly. It is clear that our methods can be applied to the first step of SSARX, and to every step of PBSID in the ope-loop setting.

### What Does Finite Sample Analysis Bring

Under the umbrella of this question, we analyze the implications of our results and validate them with simulations on a benchmark SISO system used in SIM studies \[(https://arxiv.org/html/2501.16639v2#bib.bib23)\]. It should be mentioned that the results in this paper directly extend to MIMO systems. The SISO system is given by

where $a = {- 0.7}$, $b = 1$ and $c = 0.5$. The innovations $e_{k} \sim {\mathcal{N}{}}$. Two types of inputs are considered, one is a white input given by $u_{k} \sim {\mathcal{N}{}}$, and the other is a colored input^44^4It is important to note that due to Assumption [2.1](https://arxiv.org/html/2501.16639v2#S2.Thmassumption1 "Assumption 2.1 ‣ 2.1 Models and Assumptions ‣ 2 Problem Formulation ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), our theoretical results do not apply to scenarios with colored inputs yet. However, using colored inputs in our simulations helps in demonstrating the behavior of SIMs., generated by a white noise $r_{k} \sim {\mathcal{N}{}}$ passing through a filter ${H_{u}{(q^{- 1})}} = \frac{0.318}{{1 - {0.5q^{- 1}}} + {0.9q^{- 2}}}$, where $q^{- 1}$ is the backward shift operator.

### Statistical Rates

According to Theorems [4.9](https://arxiv.org/html/2501.16639v2#S4.Thmtheorem9 "Theorem 4.9. ‣ 4.4 Overall Bound ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), [5.3](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem3 "Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), [5.6](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem6 "Theorem 5.6. ‣ 5.2.1 CVA Type Realization ‣ 5.2 Bounds on System Matrices ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") and [5.8](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem8 "Theorem 5.8. ‣ 5.2.2 MOESP Type Realization ‣ 5.2 Bounds on System Matrices ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), the error bounds on the Hankel-like matrix $\mathcal{H}_{fp}$, the extended observability matrix $\Gamma_{f}$, controllability matrix $L_{p}$, and system matrices $C$, $B$ and $A$ decay as $\mathcal{O}{({1/\sqrt{N}})}$ up to logarithmic terms. Classical asymptotic results, such as the LIL, can tighten the log factor to $\mathcal{O}{({{{\text{log}\text{log}}N}/\sqrt{N}})}$ \[(https://arxiv.org/html/2501.16639v2#bib.bib10)\]. This suggests that our bounds are not tight, which is one of the downsides of the non-asymptotic analysis. It is possible to optimize our results in the future.

### Persistence of Excitation

Similar to the PE condition for consistency analysis in the asymptotic regime \[(https://arxiv.org/html/2501.16639v2#bib.bib13)\], Lemma (https://arxiv.org/html/2501.16639v2#Thmlemma1 "Lemma 1 ‣ 4.1 Persistence of Excitation ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") provides a non-asymptotic PE condition. Specifically, it guarantees the invertibility of the empirical covariance matrix ${\hat{\Sigma}}_{p,i,N}$ defined in ((https://arxiv.org/html/2501.16639v2#S4.E30 "In 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) by establishing a lower bound on its smallest eigenvalue. In practice, once data is available, one can directly verify PE by computing the smallest eigenvalue of ${\hat{\Sigma}}_{p,i,N}$. Nonetheless, Lemma (https://arxiv.org/html/2501.16639v2#Thmlemma1 "Lemma 1 ‣ 4.1 Persistence of Excitation ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") provides a theoretical threshold, denoted by the burn-in time $N_{pe}$ in ((https://arxiv.org/html/2501.16639v2#S4.E33 "In Definition 4.1 ‣ 4.1 Persistence of Excitation ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")), indicating the minimum sample size required to ensure invertibility of ${\hat{\Sigma}}_{p,i,N}$. Such a non-asymptotic result is valuable for designing experiments (e.g., determining excitation duration), and implementing stopping rules in adaptive control \[(https://arxiv.org/html/2501.16639v2#bib.bib31)\].

### Dimensional Dependence

As shown in ((https://arxiv.org/html/2501.16639v2#S4.E33 "In Definition 4.1 ‣ 4.1 Persistence of Excitation ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) and Theorem [4.9](https://arxiv.org/html/2501.16639v2#S4.Thmtheorem9 "Theorem 4.9. ‣ 4.4 Overall Bound ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), the burn-in time $N_{pe}$ and error bounds scale with the problem dimension $d_{p,i}$ and the state dimension $n_{x}$. Such a dimensional dependence still holds when $n_{x}$ increases to the same order as $N$, whereas the results in the asymptotic regime are less meaningful in this case \[(https://arxiv.org/html/2501.16639v2#bib.bib38)\].

### Sweet Spot for the Past Horizon $p$

Assumption [4.1](https://arxiv.org/html/2501.16639v2#S4.Thmassumption1 "Assumption 4.1 ‣ 4.3 Bound on Truncation Bias ‣ 4 Finite Sample Analysis of ARX Models ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") implies that to make the truncation bias ${\overset{\sim}{\Theta}}_{i}^{B}$ decay much faster than the cross-term error ${\overset{\sim}{\Theta}}_{i}^{E}$, the past horizon $p$ should increase at a proper rate with $N$, i.e., $p = {\beta\text{log}N}$, where $\beta$ is sufficiently large. Meanwhile, a larger $p$ means that there are more parameters to be estimated, thus implying a larger error bound. This highlights that, for a fixed $N$, there is a sweet spot for the choice of $p$. Similar conclusions are found in asymptotic analysis \[(https://arxiv.org/html/2501.16639v2#bib.bib23), (https://arxiv.org/html/2501.16639v2#bib.bib51)\], suggesting that $p$ should grow moderately with $N$, neither too slow nor too fast. In practice though, $p$ can be selected using information criteria or a two-step procedure--either by minimizing the prediction error of the estimated state-space model or by directly minimizing the error bounds. We use the numerical example ((https://arxiv.org/html/2501.16639v2#S6.E47 "In 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) to demonstrate the existence of the sweet spot. We fix the future horizon at $f = 7$, and vary the number of samples ${\overline{N} = 500}:1000:2500$ and the past horizon ${p = 2}:4:30$. The input is white, and the weighting matrices are chosen as $W_{1} = I$ and $W_{2} = I$. We run 100 Monte Carlo trials. The performance is evaluated by the average normalized error of the poles $\left\| {\hat{a} - a} \right\|/\left\| a \right\|$, where $\hat{a}$ is obtained using two realization algorithms. As shown in Figure (https://arxiv.org/html/2501.16639v2#S6.F1 "Figure 1 ‣ 6.2.4 A Sweet Spot for the Past Horizon 𝑝 ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), for both two realization methods, when the number of samples is fixed, there is a sweet spot for $p$ that minimizes the errors. In addition, when the number of samples increases, the sweet spot for $p$ tends to increase as well.

Figure 1: A sweet spot for past horizon: MOESP (left) and CVA (right) realizations.

### On the Impact of Weighting Matrices

In the asymptotic regime, the impact of weighting matrices is discussed in \[(https://arxiv.org/html/2501.16639v2#bib.bib24), (https://arxiv.org/html/2501.16639v2#bib.bib25), (https://arxiv.org/html/2501.16639v2#bib.bib19), (https://arxiv.org/html/2501.16639v2#bib.bib18)\]. At a high level, $W_{1}$ is related to a maximum likelihood or CVA objective, while $W_{2}$ is related to an orthogonal projection. In addition, $W_{1}$ has little impact on the asymptotic accuracy of $\Gamma_{f}$, and $W_{2}$ has little impact on the asymptotic accuracy of $L_{p}$. As shown in Theorem [5.3](https://arxiv.org/html/2501.16639v2#S5.Thmtheorem3 "Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), our work provides a new perspective on the impact of weighting matrices. To be specific, for the robustness of SVD, the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) should be satisfied, which guarantees that the singular vectors related to small singular values of $W_{1}\mathcal{H}_{fp}W_{2}$ can be separated from the singular vectors coming from the noise $W_{1}\left( {{\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}} \right)W_{2}$. Because $W_{1}$ and $W_{2}$ reshape these singular values, they can either relax or tighten the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")). To see this clearly, we use the numerical example ((https://arxiv.org/html/2501.16639v2#S6.E47 "In 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) to show the impact of different weighting matrices in Table (https://arxiv.org/html/2501.16639v2#S3.T1 "Table 1 ‣ 3.2 Step 2: Weighted SVD ‣ 3 A Recap of Subspace Identification Methods ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). The simulation settings are the same as before, and the past horizon is fixed at $p = f = 7$. Both white input and colored input are considered. The performance is evaluated by the ratio

We determine whether the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is satisfied or not by comparing $\kappa$ with $1/4$. The results are shown in Figure (https://arxiv.org/html/2501.16639v2#S6.F2 "Figure 2 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")^55^5Note that N4SID gives almost identical results as MOESP, and IVM gives almost identical results as CVA, so only results for MOESP, CVA and OKID are presented..

Figure 2: Robustness condition: white input (left) and colored input (right), where the three curves are from three types of weighting matrices.

First, Figure (https://arxiv.org/html/2501.16639v2#S6.F2 "Figure 2 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") suggests that different weighting matrices result in different number of samples required for the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) to be satisfied. Since $\left\| {{\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}} \right\|$ decays as $\mathcal{O}{({1/\sqrt{N}})}$, no matter what pair of weighting matrices we choose, $\kappa \leq {1/4}$ will be eventually satisfied as $N\rightarrow\infty$. However, a good choice of weighting matrices makes it easier to satisfy this condition, such as the MOESP weighting.

Second, both weighting matrices $W_{1}$ and $W_{2}$ affect the robustness condition. As shown in Figure (https://arxiv.org/html/2501.16639v2#S6.F2 "Figure 2 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), MOESP and CVA employ different $W_{1}$ and the same $W_{2}$, which result in different robustness conditions. Meanwhile, MOESP and OKID employ different $W_{2}$ and the same $W_{1}$, which also result in different robustness conditions.

Third, the impact of weighting matrices is input-dependent. As shown in Figure (https://arxiv.org/html/2501.16639v2#S6.F2 "Figure 2 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), it is easier for the MOESP weighting to satisfy the condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) when the input is white than colored.

Fourth, besides their impact on the robustness condition, the weighting matrices also influence the estimation accuracy. It should be emphasized that a pair of weighting matrices making the robustness condition easier to achieve does not mean that they also imply a smaller estimation error. To illustrate this, we choose the estimate of poles coming from two realization algorithms to demonstrate the impact of the weighting matrices. The simulation settings are same as before, and only the white input is considered. The performance is evaluated by the normalized error of the poles $\left\| {\hat{a} - a} \right\|/\left\| a \right\|$. The results are shown in Figure (https://arxiv.org/html/2501.16639v2#footnote7 "footnote 7 ‣ Figure 3 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"). Based on the right subplots of Figures (https://arxiv.org/html/2501.16639v2#S6.F2 "Figure 2 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods") and (https://arxiv.org/html/2501.16639v2#footnote7 "footnote 7 ‣ Figure 3 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), we see that compared to the CVA weighting, although the MOESP weighting makes the robustness condition easier to achieve, it increases the estimation error of the poles.

Figure 3: Normalized error of poles: MOESP (left) and Larimore (right), where the three curves are from three types of weighting matrices777Although the OKID weighting performs better for the MOESP type of realization when N becomes larger in this simple example, it generally does not outperform other methods in most cases. Additionally, since we estimate ℋf, p using PARSIM, the best results of OKID is primarily attributable to PARSIM rather than the original OKID approach which estimates ℋf, p in a different way..

In addition, as shown in Figure (https://arxiv.org/html/2501.16639v2#footnote7 "footnote 7 ‣ Figure 3 ‣ 6.2.5 On the Impact of Weighting Matrices ‣ 6.2 What Does Finite Sample Analysis Bring ‣ 6 Discussions ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), $W_{1}$ has minor influence on the estimate of the poles for the MOESP type realization, and $W_{2}$ has minor influence on the estimate of the poles for the Larimore type realization. This is consistent with an analysis in the asymptotic regime \[(https://arxiv.org/html/2501.16639v2#bib.bib24), (https://arxiv.org/html/2501.16639v2#bib.bib25), (https://arxiv.org/html/2501.16639v2#bib.bib19), (https://arxiv.org/html/2501.16639v2#bib.bib18)\]. However, this conclusion cannot be obtained through our finite sample analysis. This comparison underscores the view that both asymptotic and non-asymptotic methods are valuable in uncovering the statistical properties of SIMs, and they complement each other.

Finally, we remark that the robustness condition ((https://arxiv.org/html/2501.16639v2#S5.E43 "In Theorem 5.3. ‣ 5.1 Weighted Singular Value Decomposition ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods")) is a sufficient condition, and our results are upper bounds. It is not sufficient to determine the best choice of weighting matrices solely based on the criteria of facilitating the achievement of robustness conditions and minimizing the upper bounds. To fully grasp the influence of the weighting matrices and develop an optimal choice, further study is needed.

## Conclusion

This paper presents a finite sample analysis for a large class of open-loop SIMs. Compared with the-state-of-art that mainly analyzes the performance of the Ho-Kalman algorithm or similar variants, we investigate one of the most representative SIMs, PARSIM. Our analysis establishes a more general PE condition, and takes the different weighting matrices and two realization algorithms into account. It not only confirms that the convergence rates for estimating the Markov parameters and system matrices are $\mathcal{O}{({1/\sqrt{N}})}$ even in the presence of inputs, in line with classical asymptotic results, but it also provides high-probability upper bounds for these estimates. Our findings complement the existing asymptotic results, and methodologies can be similarly applied to many variants of SIMS, such as classical SIMs, SSARX and PBSID.
