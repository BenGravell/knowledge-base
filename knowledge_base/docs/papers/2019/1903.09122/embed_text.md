## Introduction

Identifying predictive models from data has been a fundamental problem across several fields, from classical control theory to economics and modern machine learning. System identification, in particular, has a long history of studying this problem from a control theoretic perspective. Identifying linear state-space models:

from input-output data has been the focus of time-domain identification. In fact, some identification algorithms can not only learn the system matrices in but also the Kalman filter required for state estimation.

Most identification methods for linear systems either follow the prediction error approach or the subspace method. The prediction error approach is usually non-convex and directly searches over the system parameters $A,B,C,D$ by minimizing a prediction error cost. The subspace approach is a convex one; first, Hankel matrices of the system are estimated, then, the parameters are realized via steps involving singular value decomposition (SVD). Methods inspired by machine learning have also also been employed. In this paper, we focus on the subspace identification approach--see for an overview. The convergence properties of subspace algorithms have been studied before in; the analysis relies on the assumption of asymptotic stability (spectral radius ${\rho{(A)}} < 1$) and is limited to asymptotic results. In it is shown that the identification error can decrease as fast as $\mathcal{O}\left( {1/\sqrt{N}} \right)$ up to logarithmic factors, as the number of output data $N$ grows to infinity. While asymptotic results have been established, a finite sample analysis of subspace algorithms remains an open problem. Another open question is whether the asymptotic stability condition ${\rho{(A)}} < 1$ can be relaxed to marginal stability ${\rho{(A)}} \leq 1$.

From a machine learning perspective, finite sample analysis has been a standard tool for comparing algorithms in the non-asymptotic regime. Early work in finite sample analysis of system identification can be found in. A series of recent papers studied the finite sample properties of system identification from a single trajectory, when the system state is fully observed ($C = I$). Finite sample results for partially observed systems ($C \neq I$), which is a more challenging problem, appeared recently in. These papers provide a non-asymptotic convergence rate of $1/\sqrt{N}$ for the recovery of matrices $A,B,C,D$ up to a similarity transformation. The results rely on the assumption that that the system can be driven by external inputs, i.e. ${B,D} \neq 0$. In, the analysis of the classical Ho-Kalman realization algorithm was explored. In, it was shown that with a prefiltering step, consistency can be achieved even for marginally stable systems where ${\rho(A)} \leq 1$. In, identification of a system of unknown order is considered. Finite sample properties of system identification algorithms have also been used to design controllers. The dual problem of Kalman filtering has not been studied yet in this context.

In this paper, we perform the first finite sample analysis of system in the case ${B,D} = 0$, when we have no inputs, also known as stochastic system identification (SSI). This problem is more challenging than the case ${B,D} \neq 0$, since the system can only be driven through noise and establishing persistence of excitation is harder. We provide the first non-asymptotic guarantees for the estimation of matrices $A,C$ as well as the Kalman filter gain of. Similar to, the analysis is based on new tools from machine learning and statistics. In summary the main contributions of this paper are:

To the best of our knowledge, our paper provides the first finite sample upper bounds in the case of stochastic system identification, where we have no inputs and the system is only driven by noise. We also provide the first finite sample guarantees for the estimation error of the Kalman filter gain.

We prove that the outputs of the system satisfy persistence of excitation in finite time with high probability. This result is fundamental for the analysis of most subspace identification algorithms, which use outputs as regressors.

We show that we can achieve a learning rate of $\mathcal{O}{(\sqrt{1/N})}$ up to logarithmic factors for marginally stable systems. To the best of our knowledge, the classical subspace identification results do not offer guarantees in the case of marginal stability where ${\rho{(A)}} \leq 1$. For stable systems (${\rho{(A)}} < 1$), this rate is consistent with classical asymptotic results.

All proofs are included in the Appendix.

## Problem formulation

Consider the standard state space representation with ${B,D} = 0$, where $x_{k} \in {\mathbb{R}}^{n}$ is the system state, $y_{k} \in {\mathbb{R}}^{m}$ is the output, $A \in {\mathbb{R}}^{n \times n}$ is the system matrix, $C \in {\mathbb{R}}^{m \times n}$ is the output matrix, $w_{k} \in {\mathbb{R}}^{n}$ is the process noise and $v_{k} \in {\mathbb{R}}^{m}$ is the measurement noise. The noises $w_{k},v_{k}$ are assumed to be i.i.d. zero mean Gaussian, with covariance matrices $Q$ and $R$ respectively, and independent of each other. The initial state $x_{0}$ is also assumed to be zero mean Gaussian, independent of the noises, with covariance $\Sigma_{0}$. Matrices $A$, $C$, $Q$, $R$, $\Sigma_{0}$ are initially unknown. However, the following assumption holds throughout the paper.

### Assumption 1

The order of the system $n$ is known. System $A$ is marginally stable: ${\rho(A)} \leq 1$, where $\rho$ denotes the spectral radius. The pair $(A,C)$ is observable, $(A,Q^{1/2})$ is controllable and $R$ is strictly positive definite. $\diamond$

We leave the case of unknown $n$ for future work ^11^1The results of Section 4 do not depend on the order $n$ being known.. The assumption ${\rho{(A)}} \leq 1$ is more general than the stricter condition ${\rho{(A)}} < 1$ found in previous works, see. The remaining conditions in Assumption 1 are standard for the stochastic system identification problem to be well posed and the Kalman filter to converge.

The steady-state Kalman filter of system is:

where $K \in {\mathbb{R}}^{n \times m}$ is the steady-state Kalman gain

and $P$ is the positive definite solution of the Riccati equation:

A byproduct of Assumption 1 is that the closed-loop matrix $A - {KC}$ has all the eigenvalues strictly inside the unit circle. The state of the Kalman filter is the minimum mean square error prediction:

We denote its covariance matrix by:

The innovation error sequence $e_{k}$ has covariance

Since the original errors are Gaussian i.i.d., by the orthogonality principle the innovation error sequence $e_{k}$ is also Gaussian and i.i.d. The later property is true since we also assumed that the Kalman filter is in steady-state.

### Assumption 2

We assume that $\Sigma_{0} = P$, so that the Kalman filter has converged to its steady-state. $\diamond$

Since the Kalman filter converges exponentially fast to the steady-state gain, this assumption is reasonable in many situations; it is also standard. Nonetheless, we leave the case of general $\Sigma_{0}$ for future work.

In the classical stochastic subspace identification problem, the main goal is to identify the Kalman filter parameters $A,C,K$ from output samples ${y_{0}\ldots},y_{N}$--see for example Chapter 3 of. The problem is ill-posed in general since the outputs are invariant under any similarity transformation $\overline{A} = {S^{- 1}AS}$, $\overline{C} = {CS}$, $\overline{K} = {S^{- 1}K}$. Thus, we can only estimate $A,C,K$ up to a similarity transformation.

In this paper, we will analyze the finite sample properties of a subspace identification algorithm, which is based on least squares.

### Problem 1 (Finite Sample Analysis of SSI)

Consider a finite number $N$ of output samples $y_{0},\ldots,y_{N - 1}$, which follow model with ${B,D} = 0$, and an algorithm $\mathcal{A}$, which returns estimates $\hat{A},\hat{C},\hat{K}$ of the true parameters. Given a confidence level $\delta$ provide upper bounds $\epsilon_{A}(\delta,N)$, $\epsilon_{C}(\delta,N)$, $\epsilon_{K}(\delta,N)$ and an invertible matrix $S$ such that with probability at least $1 - \delta$:

where $\left. \parallel \cdot \parallel{}_{2} \right.$ denotes the spectral norm. The bounds $\epsilon$ can also depend on the model parameters $n,A,C,R,Q$ as well as the identification algorithm used. $\diamond$

## Subspace Identification Algorithm

The procedure of estimating the parameters $A,C,K$ is based on a least square approach, see for example. It involves two stages. First, we regress future outputs to past outputs to obtain a Hankel-like matrix, which is a product of an observability and a controllability matrix. Second, we perform a balanced realization step, similar to the Ho-Kalman algorithm, to obtain estimates for $A,C,K$.

Before describing the algorithm, we need some definitions. Let $p,f$, with ${p,f} \geq n$ be two design parameters that define the horizons of the past and the future respectively. Assume that the total number of output samples is $\overline{N} = {{N + p + f} - 1}$. Then, the future outputs $Y_{k}^{+} \in {\mathbb{R}}^{mf}$ and past outputs $Y_{k}^{-} \in {\mathbb{R}}^{mp}$ at time $k \geq p$ are defined as follows:

By stacking the outputs for all sample sequences, over all times $p \leq k \leq {{N + p} - 1}$, we form the batch outputs:

The past and future noises $E_{k}^{+},E_{k}^{-},E_{+},E_{-}$ are defined similarly. Finally, define the batch states:

The (extended) observability matrix $\mathcal{O}_{k} \in {\mathbb{R}}^{{mk} \times n}$ and the reversed (extended) controllability matrix $\mathcal{K}_{k} \in {\mathbb{R}}^{{n \times m}k}$ associated to system are defined as:

respectively. We denote the Hankel(-like) matrix $\mathcal{O}_{f}\mathcal{K}_{p}$ by:

Finally, for any $s \geq 2$, define block-Toeplitz matrix:

### Regression for Hankel Matrix Estimation

First, we establish a linear regression between the future and past outputs. This step is common in most (stochastic) subspace identification algorithms. From, for every $k$:

Meanwhile, from, the state prediction ${\hat{x}}_{k}$ can be expressed in terms of the past outputs:

After some algebra, we derive the linear regression:

where the regressors $Y_{-}$ and the residuals $E_{+}$ are independent column-wise. The term $\mathcal{O}_{k}{({A - {KC}})}^{p}\hat{X}$ introduces a bias due to the Kalman filter truncation, where we use only $p$ past outputs instead of all of them. Based on, we compute the least squares estimate

The Hankel matrix $G$ can be interpreted as a (truncated) Kalman filter which predicts future outputs directly from past outputs, independently of the internal state-space representation. In this sense, the estimate $\hat{G}$ is a "data-driven\" Kalman filter. Notice that persistence of excitation of the outputs (invertibility of $Y_{-}Y_{-}^{\ast}$) is required in order to compute the least squares estimate $\hat{G}$.

### Balanced Realization

This step determines a balanced realization of the state-space, which is only one of the possibly infinite state-space representations--see Section 6 for comparison with other subspace methods. First, we compute a rank-$n$ factorization of the full rank matrix $\hat{G}$. Let the SVD of $\hat{G}$ be:

where ${\hat{\Sigma}}_{1} \in {\mathbb{R}}^{n \times n}$ contains the $n -$largest singular values. Then, a standard realization of $\mathcal{O}_{f}$, $\mathcal{K}_{p}$ is:

This step assumed knowing the order $n$ of the system, see Assumption 1. In addition, matrix $\mathcal{K}_{p}$ should have full rank $n$. This is equivalent to the pair $(A,K)$ being controllable. Otherwise, $\mathcal{O}_{f}\mathcal{K}_{p}$ will have rank less than $n$ making it impossible to accurately estimate $\mathcal{O}_{f}$.

### Assumption 3

The pair $(A,K)$ is controllable. $\diamond$

The above assumption is standard--see for example.

Based on the estimated observability/controllability matrices, we can approximate the system parameters as follows:

where the notation ${\hat{\mathcal{O}}}_{f}(1:m,:)$ means we pick the first $m$ rows and all columns. The notation for ${\hat{\mathcal{K}}}_{p}$ has similar interpretation. For simplicity, define

which includes the $m{({f - 1})}$ "upper\" rows of matrix ${\hat{\mathcal{O}}}_{f}$. Similarly, we define the lower part ${\hat{\mathcal{O}}}_{f}^{l}$. For matrix $A$ we exploit the structure of the extended observability matrix and solve ${{\hat{\mathcal{O}}}_{f}^{u}\hat{A}} = {\hat{\mathcal{O}}}_{p}^{l}$ in the least squares sense by computing

where $\dagger$ denotes the pseudoinverse.

Now that we have a stochastic system identification algorithm, our goal is to perform finite sample analysis, which is divided in two parts. First, in Section 4, we provide high probability upper bounds for the error ${\|{G - \hat{G}}\|}_{2}$ in the regression step. Then, in Section 5, we analyze the robustness of the balanced realization step.

## Finite Sample Analysis of Regression

In this section, we provide the finite sample analysis of the linear regression step of the identification algorithm. We provide high-probability upper bounds for estimation error ${\|{G - \hat{G}}\|}_{2}$ of the Hankel-like matrix $G$. Before we state the main result, let us introduce some notation. Recall the definition of the innovation covariance matrix $\overline{R}$ in. We denote the past noises' weighted covariance by:

The least singular value of the above matrix is denoted by:

In Lemma B.2 in the Appendix, we show that $\sigma_{E} \geq {\sigma_{\min}(R)} > 0$.

### Theorem 1 (Regression Step Analysis)

Consider system under the Assumptions 1, 2, 3. Let $\hat{G}$ be the estimate of the subspace identification algorithm given an output trajectory $y_{0},\ldots,y_{{N + p + f} - 1}$ and let $G$ be as in. Fix a confidence $\delta > 0$ and define:

There exist $N_{0},N_{1},N_{2}$ such that if $N \geq {N_{0},N_{1},N_{2}}$, (see definitions (B.1), (B.5), (C.3) in the Appendix), then with probability at least $1 - \delta_{N} - {6\delta}$:

over-approximates the condition number of ${\mathbb{E}}\left\lbrack {Y_{-}Y_{-}^{\ast}} \right\rbrack$ and

are system-dependent constants. $\diamond$

The final result in (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) has been simplified for compactness--see (C.4) for the full expression in the Appendix.

### Remark 1 (Result interpretation)

From, the estimation error consists of two terms:

The first term in (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) corresponds to the cross-term error, while the second term corresponds to the Kalman filter truncation bias term. To obtain consistency for $\hat{G}$, we have to let the term $\left\| {({A - {KC}})}^{p} \right\|_{2}$ go to zero with $N$. Recall that the matrix $A - {KC}$ has spectral radius less than one, thus, the second term decreases exponentially with $p$. By selecting $p = {c{\log N}}$, for some $c$, we can force the Kalman truncation error term to decrease at least as fast as the first one, see for example. In this sense, the dominant term is the first one, i.e. the cross-term. Notice, that $f$ can be kept bounded as long as it is larger than $n$. Notice that the norm $\left\| \mathcal{O}_{p}^{\dagger} \right\|$ remains bounded by $\left\| \mathcal{O}_{n}^{\dagger} \right\|$ as $p$ increases--see Lemma E.3. ‣ Appendix E Bounds for system matrices ‣ Finite Sample Analysis of Stochastic System Identification") in Appendix. $\diamond$

### Remark 2 (Statistical rates)

For marginally stable systems (${\rho{(A)}} \leq 1$) and $p = {c{\log N}}$, we have ${\log\kappa_{N}} = {\mathcal{O}\left( {\log N} \right)}$, since $\left\| \mathcal{O}_{p} \right\|_{2},{{tr}\Gamma_{N}}$ depend at most polynomially on $p,N$--see Corollary E.1 in the Appendix. In this case, (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) results in a rate of:

To the best of our knowledge, there have not been any bounds for the performance of subspace algorithms in the case of marginally stable systems.

In the case of asymptotically stable systems (${\rho{(A)}} < 1$), we have $\kappa_{N} = {\mathcal{O}(p)}$, since $\left\| \mathcal{O}_{p} \right\|_{2},{{tr}\Gamma_{N}},\left\| \mathcal{T}_{p} \right\|_{2}$ are now $\mathcal{O}{}$--see Corollary E.1 in the Appendix. Hence, if $p = {c{\log N}}$, we obtain a rate of:

As a result, our finite sample bound (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) is consistent with the asymptotic bound in equation of as $N$ grows to infinity. $\diamond$

In the absence of inputs (${B,D} = 0$), the noise both helps and obstructs identification. Larger noise leads to better excitation of the outputs, but also worsens the convergence of the least squares estimator. To see how our finite sample bounds capture that, observe that larger noise leads to bigger $\sigma_{E}$ but also bigger $\left\| \overline{R} \right\|_{2}$. This trade-off is captured by $\mathcal{C}_{1}$.

If $N$ is sufficiently large (condition $N \geq {N_{0},N_{1}}$), the outputs are guaranteed to be persistently exciting in finite time; more details can be found in Section 4.1 and the Appendix. Meanwhile, condition $N \geq N_{2}$ is not necessary; it just leads to a simplified expression for the bound of the Kalman filter truncation error--see Section 4.3 and Appendix. The definitions of $N_{0},N_{1},N_{2}$ can be found in (B.1), (B.5), (C.3). Their existence is guaranteed even if $p$ varies slowly with $N$, i.e. logarithmically.

Obtaining the bound on the error ${\|{G - \hat{G}}\|}_{2}$ in (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) of Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") requires the following three steps:

Proving persistence of excitation (PE) for the past outputs, i.e. invertibility of $Y_{-}Y_{-}^{\ast}$.

Establishing bounds for the cross-term error in (29. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")).

Establishing bounds for the the Kalman truncation error in (29. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")).

In the following subsections, we sketch the proof steps.

### Persistence of Excitation in Finite Time

The next theorem shows that with high probability the past outputs and noises are persistently exciting in finite time. The result is of independent interest and is fundamental since most subspace algorithms use past outputs as regressors.

### Theorem 2 (Persistence of Excitation)

Consider the conditions of Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") and $N_{0}$, $N_{1}$ as in (B.1), (B.5). If $N \geq {N_{0},N_{1}}$, then with probability at least $1 - \delta_{N} - {2\delta}$ both of the following events occur:

where $\succeq$ denotes comparison in the positive semidefinite cone. Hence, with probability at least $1 - \delta_{N} - {2\delta}$ the outputs satisfy the PE condition:

where $\sigma_{E} > 0$ is defined in. $\diamond$

The above result implies that if the past noises satisfy a PE condition, then PE for the outputs is also guaranteed; the noises are the only way to excite the system in the absence of control inputs. The prove PE, from, the past outputs satisfy:

Thus, their correlations are

We can first show PE for the noise correlations $\mathcal{T}_{p}E_{-}E_{-}^{\ast}\mathcal{T}_{p}^{\ast}$, i.e. show that the event $\mathcal{E}_{E}$ occurs with high probability when $N$ is sufficiently large (condition $N \geq N_{0}$). This behavior is due to the fact that ${{\mathbb{E}}\left\lbrack {\mathcal{T}_{p}E_{-}E_{-}^{\ast}\mathcal{T}_{p}^{\ast}} \right\rbrack} = {N\Sigma_{E}}$ and the sequence $E_{k}^{-}$ is component-wise i.i.d. To prove this step, we use Lemma C.2 from --see Lemma B.1. ‣ Appendix B Persistence of Excitation ‣ Finite Sample Analysis of Stochastic System Identification") in the Appendix.

Meanwhile, the cross terms $\hat{X}E^{\ast}$ are much smaller and their norm increases with a rate of at most $\mathcal{O}{(\sqrt{N})}$ up to logarithmic terms. This is since ${{\mathbb{E}}\left\lbrack {\hat{X}E^{\ast}} \right\rbrack} = 0$ and the product $\hat{X}E^{\ast}$ has martingale structure (see Appendix and Theorem 3. ‣ 4.2 Cross-term error ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") below). Eventually, if the number of samples $N$ is large enough (condition $N \geq N_{1}$), the cross-terms will be dominated by the noise and state correlations with high probability, which establishes output PE.

### Cross-term error

To bound the cross-term error, we express it as a product of $E_{+}Y_{-}^{\ast}\left( {Y_{-}Y_{-}^{\ast}} \right)^{- {1/2}}$ and ${({Y_{-}Y_{-}^{\ast}})}^{- {1/2}}$, as in. The second term of the product can be bounded by applying Theorem 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification"). The first term is self-normalized and has martingale structure component-wise. In particular, the product $Y_{-}E_{+}^{\ast}$ is equal to:

where every sum above is a martingale. To bound it, we apply the next theorem, which generalizes Theorem 1 in and Proposition 8.2 in.

### Theorem 3 (Cross terms)

Let $\left\{ \mathcal{F}_{t} \right\}_{t = 0}^{\infty}$ be a filtration. Let $\eta_{t} \in {\mathbb{R}}^{m}$, $t \geq 0$ be $\mathcal{F}_{t}$-measurable, independent of $\mathcal{F}_{t - 1}$. Suppose also that $\eta_{t}$ has independent components $\eta_{t,i}$ $i = {1,\ldots,m}$, which are $1 -$sub-Gaussian:

Let $X_{t} \in {\mathbb{R}}^{d}$, $t \geq 0$ be $\mathcal{F}_{t - 1} -$measurable. Assume that $V$ is a $d \times d$ positive definite matrix. For any $t \geq 0$, define:

for some integer $r$. Then, for any $\delta > 0$, with probability at least $1 - \delta$, for all $t \geq 0$

The above theorem along with a Markov upper bound on $Y_{-}Y_{-}^{\ast}$ (see Lemma B.3. ‣ Appendix B Persistence of Excitation ‣ Finite Sample Analysis of Stochastic System Identification") in the Appendix) are used to bound $E_{+}Y_{-}^{\ast}\left( {Y_{-}Y_{-}^{\ast}} \right)^{- {1/2}}$.

### Kalman truncation error

For the Kalman truncation error term, we need to bound the term $\hat{X}Y_{-}^{\ast}{({Y_{-}Y_{-}^{\ast}})}^{- 1}$, which is $\mathcal{O}$. Using the identities ${\mathcal{O}_{p}^{\dagger}\mathcal{O}_{p}\hat{X}} = \hat{X}$, and $Y_{-} = {{\mathcal{O}_{p}\hat{X}} + {\mathcal{T}_{p}E_{-}}}$, we derive the following equality:

From Theorem 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification"), we obtain $\left\| {\mathcal{T}_{p}E_{-}E_{-}^{\ast}\mathcal{T}_{p}^{\ast}{({Y_{-}Y_{-}^{\ast}})}^{- 1}} \right\|_{2} \leq 2$. The last term in can be treated like the cross-term in Section 4.2, by applying Theorems 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification"), 3. ‣ 4.2 Cross-term error ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") and Lemma B.3. ‣ Appendix B Persistence of Excitation ‣ Finite Sample Analysis of Stochastic System Identification"). It decreases with a rate of $\mathcal{O}\left( {1/\sqrt{N}} \right)$ up to logarithmic terms, so it is much smaller than the other terms in. To keep the final bound simple, we select $N_{2}$ such that

with high probability--see also (C.3) for the definition of $N_{2}$.

## Robustness of Balanced Realization

In this section, we analyze the robustness of the balanced realization. In particular, we upper bound the estimation errors of matrices $A,C,K$ in terms of the estimation error ${\|{G - \hat{G}}\|}_{2}$ obtained by Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification").

Assume that we knew $G$ exactly. Then, the SVD of the true $G$, would be:

for some $\Sigma_{1} \in {\mathbb{R}}^{n \times n}$. Hence, if we knew $G$ exactly, the output of the balanced realization would be:

The respective matrices $\overline{C},\overline{K},\overline{A}$ are defined similarly, based on ${\overline{\mathcal{O}}}_{f},{\overline{\mathcal{K}}}_{p}$, as described in Section 3. The system matrices $\overline{C},\overline{K},\overline{A}$ are equivalent to the original matrices $C,K,A$ up to a similarity transformation $\overline{C} = {CS}$, $\overline{K} = {S^{- 1}K}$, $\overline{A} = {S^{- 1}AS}$ for some invertible $S$. For simplicity, we will quantify the estimation errors in terms of the similar $\overline{A},\overline{C},\overline{K}$ instead of the original $A,C,K$.

The next result follows the steps of and relies on Lemma 5.14 of and Theorem 4.1 of. Let $\sigma_{n}( \cdot )$ denote the $n -$th largest singular value.

### Theorem 4 (Realization robustness)

Consider the true Hankel-like matrix $G$ defined in and the noisy estimate $\hat{G}$ defined in. Let $\hat{A},\hat{C},\hat{K},{\hat{\mathcal{O}}}_{f}$, ${\hat{\mathcal{K}}}_{p}$ be the output of the balanced realization algorithm based on $\hat{G}$. Let $\overline{A},\overline{C},\overline{K},{\overline{\mathcal{O}}}_{f}$, ${\overline{\mathcal{K}}}_{p}$ be the output of the balanced realization algorithm based on the true $G$. If $G$ has rank $n$ and the following robustness condition is satisfied:

there exists an orthonormal matrix $T \in {\mathbb{R}}^{n \times n}$ such that:

The notation ${{\hat{\mathcal{O}}}_{f}^{u},{\overline{\mathcal{O}}}_{f}^{u}},$ refers to the upper part of the respective matrix (first ${({f - 1})}m$ rows)--see Section 3.2. $\diamond$

### Remark 3

The result states that if the error of the regression step is small enough, then the realization is robust. The singular value $\sigma_{n}(G)$ can be quite small. Hence, the robustness condition (36. ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Stochastic System Identification")) can be quite restrictive in practice. However, such a condition is a fundamental limitation of the SVD procedure. The gap between the singular values of $G$ and the singular values coming from the noise $G - \hat{G}$ should be large enough; this guarantees that the singular vectors related to small singular values of $G$ are separated from the singular vectors coming from the noise $G - \hat{G}$, which can be arbitrary. See also Wedin's theorem. Such robustness conditions have also appeared in model reduction theory. $\diamond$

The term $\frac{\sqrt{\left\| G \right\|_{2}} + \sigma_{o}}{\sigma_{o}^{2}}$ which appears in the bound of $A$ is $\mathcal{O}$. The value of $\sigma_{o}^{- 1}$ is random since it depends on ${\hat{\mathcal{O}}}_{f}^{h}$. However, we could replace it by a deterministic bound. From:

$\sigma_{o}$ will eventually be lower bounded by ${\sigma_{n}\left( {\overline{\mathcal{O}}}_{f}^{h} \right)}/2$ if the error $\left\| {{\hat{\mathcal{O}}}_{f} - {{\overline{\mathcal{O}}}_{f}T}} \right\|_{2} \leq {{\sigma_{n}\left( {\overline{\mathcal{O}}}_{f}^{h} \right)}/2}$ is small enough. The norm ${\| G\|}_{2} \leq {\left\| \mathcal{O}_{f} \right\|_{2}\left\| \mathcal{K}_{p} \right\|_{2}}$ is bounded as $p$ increases, since $A - {KC}$ is asymptotically stable and $f$ is finite.

### Remark 4 (Total bounds)

The final upper bounds for the estimation of the system parameters $A,C,K$, as stated in Problem 1. ‣ 2 Problem formulation ‣ Finite Sample Analysis of Stochastic System Identification"), can be found by combining the finite sample guarantees of the regression step (Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) with the robustness analysis of the realization step (Theorem 4. ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Stochastic System Identification")). All matrix estimation errors depend linearly on the Hankel matrix estimation error ${\|{G - \hat{G}}\|}_{2}$. As a result, all matrix errors have the same statistical rate as the error of $G$, i.e. their estimation error decreases at least as fast as $\mathcal{O}\left( {1/\sqrt{N}} \right)$ up to logarithmic factors. $\diamond$

## Discussion and Future Work

One of the main differences between the subspace algorithm considered in this paper and other stochastic subspace identification algorithms is the SVD step. The other algorithms perform SVD on $W_{1}GW_{2}$ instead of $G$, where $W_{1},W_{2}$ are full rank weighting matrices, possibly data dependent. From this point of view, the results of Section 4 (upper bound for $\|{G - \hat{G}}\|$ in Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") and persistence of excitation in Theorem 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) are fundamental for understanding the finite sample properties of other subspace identification algorithms. Here, we studied the case ${W_{1} = I},{W_{2} = I}$, which is not the standard choice. It is subject of future work to explore how the choice of $W_{1},W_{2}$ affects the realization step, especially the robustness condition of the SVD step.

We could also provide finite sample bounds for the estimation of the closed-loop matrix $A_{c} \triangleq {A - {KC}}$. This can be done in two ways. One option is to form matrix $\hat{A} - {\hat{K}\hat{C}}$ from the estimates $\hat{A},\hat{C},\hat{K}$. Alternatively, we could estimate $\hat{A_{c}}$ directly from ${\hat{\mathcal{K}}}_{p}$ in the same way that we estimated $\hat{A}$. However, we do not have finite sample guarantees for the stability of the closed-loop estimates $\hat{A} - {\hat{K}\hat{C}}$, $\hat{A_{c}}$. It would be interesting to address this in future work.

Another direction for future work is repeating the analysis when the Kalman filter has not reached steady-state, i.e. relax Assumption 2. Finally, in this work, we only considered upper bounds. It would be interesting to study lower bounds as well to evaluate the tightness of our upper bounds. In any case, from lower bounds for fully observed systems, the factor of $1/\sqrt{N}$ is tight.
