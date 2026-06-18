<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite Sample Analysis of Stochastic System Identification

Topics include Robustness, Kalman filtering, System identification, Sample complexity, Learning, Kalman filter.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we analyze the finite sample complexity of stochastic system identification using modern tools from machine learning and statistics. An unknown discrete-time linear system evolves over time under Gaussian noise without external inputs. The objective is to recover the system parameters as well as the Kalman filter gain, given a single trajectory of output measurements over a finite horizon of length N. Based on a subspace identification algorithm and a finite number of N output samples, we provide non-asymptotic high-probability upper bounds for the system parameter estimation errors. Our analysis uses recent results from random matrix theory, self-normalized martingales and SVD robustness, in order to show that with high probability the estimation errors decrease with a rate of 1/sqrt(N). Our non-asymptotic bounds not only agree with classical asymptotic results, but are also valid even when the system is marginally stable.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Identifying predictive models from data has been a fundamental problem across several fields, from classical control theory to economics and modern machine learning. System identification, in particular, has a long history of studying this problem from a control theoretic perspective.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

from input-output data has been the focus of time-domain identification. In fact, some identification algorithms can not only learn the system matrices in but also the Kalman filter required for state estimation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most identification methods for linear systems either follow the prediction error approach or the subspace method. The prediction error approach is usually non-convex and directly searches over the system parameters $A,B,C,D$ by minimizing a prediction error cost. The subspace approach is a convex one; first, Hankel matrices of the system are estimated, then, the parameters are realized via steps involving singular value decomposition (SVD). Methods inspired by machine learning have also also been employed. In this paper, we focus on the subspace identification approach--see for an overview. The convergence properties of subspace algorithms have been studied before; the analysis relies on the assumption of asymptotic stability (spectral radius ${\rho{(A)}} < 1$) and is limited to asymptotic results. In it is shown that the identification error can decrease as fast as $\mathcal{O}\left( {1/\sqrt{N}} \right)$ up to logarithmic factors, as the number of output data $N$ grows to infinity. While asymptotic results have been established, a finite sample analysis of subspace algorithms remains an open problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another open question is whether the asymptotic stability condition ${\rho{(A)}} < 1$ can be relaxed to marginal stability ${\rho{(A)}} \leq 1$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

From a machine learning perspective, finite sample analysis has been a standard tool for comparing algorithms in the non-asymptotic regime. Early work in finite sample analysis of system identification can be found. A series of recent papers studied the finite sample properties of system identification from a single trajectory, when the system state is fully observed ($C = I$). Finite sample results for partially observed systems ($C \neq I$), which is a more challenging problem, appeared recently. These papers provide a non-asymptotic convergence rate of $1/\sqrt{N}$ for the recovery of matrices $A,B,C,D$ up to a similarity transformation. The results rely on the assumption that that the system can be driven by external inputs, i.e. ${B,D} \neq 0$. In, the analysis of the classical Ho-Kalman realization algorithm was explored. In, it was shown that with a prefiltering step, consistency can be achieved even for marginally stable systems where ${\rho(A)} \leq 1$. In, identification of a system of unknown order is considered.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite sample properties of system identification algorithms have also been used to design controllers. The dual problem of Kalman filtering has not been studied yet in this context.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we perform the first finite sample analysis of system in the case ${B,D} = 0$, when we have no inputs, also known as stochastic system identification (SSI). This problem is more challenging than the case ${B,D} \neq 0$, since the system can only be driven through noise and establishing persistence of excitation is harder. We provide the first non-asymptotic guarantees for the estimation of matrices $A,C$ as well as the Kalman filter gain of. Similar to, the analysis is based on new tools from machine learning and statistics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, our paper provides the first finite sample upper bounds in the case of stochastic system identification, where we have no inputs and the system is only driven by noise. We also provide the first finite sample guarantees for the estimation error of the Kalman filter gain.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove that the outputs of the system satisfy persistence of excitation in finite time with high probability. This result is fundamental for the analysis of most subspace identification algorithms, which use outputs as regressors.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that we can achieve a learning rate of $\mathcal{O}{(\sqrt{1/N})}$ up to logarithmic factors for marginally stable systems. To the best of our knowledge, the classical subspace identification results do not offer guarantees in the case of marginal stability where ${\rho{(A)}} \leq 1$. For stable systems (${\rho{(A)}} < 1$), this rate is consistent with classical asymptotic results.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

All proofs are included in the Appendix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider the standard state space representation with ${B,D} = 0$, where $x_{k} \in {\mathbb{R}}^{n}$ is the system state, $y_{k} \in {\mathbb{R}}^{m}$ is the output, $A \in {\mathbb{R}}^{n \times n}$ is the system matrix, $C \in {\mathbb{R}}^{m \times n}$ is the output matrix, $w_{k} \in {\mathbb{R}}^{n}$ is the process noise and $v_{k} \in {\mathbb{R}}^{m}$ is the measurement noise. The noises $w_{k},v_{k}$ are assumed to be i.i.d. zero mean Gaussian, with covariance matrices $Q$ and $R$ respectively, and independent of each other.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The initial state $x_{0}$ is also assumed to be zero mean Gaussian, independent of the noises, with covariance $\Sigma_{0}$. Matrices $A$, $C$, $Q$, $R$, $\Sigma_{0}$ are initially unknown. However, the following assumption holds throughout the paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The order of the system $n$ is known. System $A$ is marginally stable: ${\rho(A)} \leq 1$, where $\rho$ denotes the spectral radius. The pair $(A,C)$ is observable, $(A,Q^{1/2})$ is controllable and $R$ is strictly positive definite. $\diamond$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We leave the case of unknown $n$ for future work ^11^1The results of Section 4 do not depend on the order $n$ being known.. The assumption ${\rho{(A)}} \leq 1$ is more general than the stricter condition ${\rho{(A)}} < 1$ found in previous works, see. The remaining conditions in Assumption 1 are standard for the stochastic system identification problem to be well posed and the Kalman filter to converge.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $K \in {\mathbb{R}}^{n \times m}$ is the steady-state Kalman gain

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

A byproduct of Assumption 1 is that the closed-loop matrix $A - {KC}$ has all the eigenvalues strictly inside the unit circle.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The innovation error sequence $e_{k}$ has covariance

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Since the original errors are Gaussian i.i.d., by the orthogonality principle the innovation error sequence $e_{k}$ is also Gaussian and i.i.d. The later property is true since we also assumed that the Kalman filter is in steady-state.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We assume that $\Sigma_{0} = P$, so that the Kalman filter has converged to its steady-state. $\diamond$

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Since the Kalman filter converges exponentially fast to the steady-state gain, this assumption is reasonable in many situations; it is also standard. Nonetheless, we leave the case of general $\Sigma_{0}$ for future work.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

In the classical stochastic subspace identification problem, the main goal is to identify the Kalman filter parameters $A,C,K$ from output samples ${y_{0}\ldots},y_{N}$--see for example Chapter 3 of. The problem is ill-posed in general since the outputs are invariant under any similarity transformation $\overline{A} = {S^{- 1}AS}$, $\overline{C} = {CS}$, $\overline{K} = {S^{- 1}K}$. Thus, we can only estimate $A,C,K$ up to a similarity transformation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

In this paper, we will analyze the finite sample properties of a subspace identification algorithm, which is based on least squares.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem 1 (Finite Sample Analysis of SSI)", "weight": 1.0} -->

Consider a finite number $N$ of output samples $y_{0},\ldots,y_{N - 1}$, which follow model with ${B,D} = 0$, and an algorithm $\mathcal{A}$, which returns estimates $\hat{A},\hat{C},\hat{K}$ of the true parameters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1 (Finite Sample Analysis of SSI)", "weight": 1.0} -->

where $\left. \parallel \cdot \parallel{}_{2} \right.$ denotes the spectral norm. The bounds $\epsilon$ can also depend on the model parameters $n,A,C,R,Q$ as well as the identification algorithm used. $\diamond$

<!-- chunk {"id": "body-0028", "role": "body", "section": "Subspace Identification Algorithm", "weight": 1.0} -->

The procedure of estimating the parameters $A,C,K$ is based on a least square approach, see for example. It involves two stages. First, we regress future outputs to past outputs to obtain a Hankel-like matrix, which is a product of an observability and a controllability matrix. Second, we perform a balanced realization step, similar to the Ho-Kalman algorithm, to obtain estimates for $A,C,K$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Subspace Identification Algorithm", "weight": 1.0} -->

Before describing the algorithm, we need some definitions. Let $p,f$, with ${p,f} \geq n$ be two design parameters that define the horizons of the past and the future respectively. Assume that the total number of output samples is $\overline{N} = {{N + p + f} - 1}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Regression for Hankel Matrix Estimation", "weight": 1.0} -->

First, we establish a linear regression between the future and past outputs. This step is common in most (stochastic) subspace identification algorithms.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Regression for Hankel Matrix Estimation", "weight": 1.0} -->

where the regressors $Y_{-}$ and the residuals $E_{+}$ are independent column-wise. The term $\mathcal{O}_{k}{({A - {KC}})}^{p}\hat{X}$ introduces a bias due to the Kalman filter truncation, where we use only $p$ past outputs instead of all of them. Based, we compute the least squares estimate

<!-- chunk {"id": "body-0032", "role": "body", "section": "Regression for Hankel Matrix Estimation", "weight": 1.0} -->

The Hankel matrix $G$ can be interpreted as a (truncated) Kalman filter which predicts future outputs directly from past outputs, independently of the internal state-space representation. In this sense, the estimate $\hat{G}$ is a "data-driven\" Kalman filter. Notice that persistence of excitation of the outputs (invertibility of $Y_{-}Y_{-}^{\ast}$) is required in order to compute the least squares estimate $\hat{G}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Balanced Realization", "weight": 1.0} -->

This step determines a balanced realization of the state-space, which is only one of the possibly infinite state-space representations--see Section 6 for comparison with other subspace methods. First, we compute a rank-$n$ factorization of the full rank matrix $\hat{G}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Balanced Realization", "weight": 1.0} -->

This step assumed knowing the order $n$ of the system, see Assumption 1. In addition, matrix $\mathcal{K}_{p}$ should have full rank $n$. This is equivalent to the pair $(A,K)$ being controllable. Otherwise, $\mathcal{O}_{f}\mathcal{K}_{p}$ will have rank less than $n$ making it impossible to accurately estimate $\mathcal{O}_{f}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The above assumption is standard--see for example.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

where the notation ${\hat{\mathcal{O}}}_{f}(1:m,:)$ means we pick the first $m$ rows and all columns. The notation for ${\hat{\mathcal{K}}}_{p}$ has similar interpretation. For simplicity, define

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

where $\dagger$ denotes the pseudoinverse.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Now that we have a stochastic system identification algorithm, our goal is to perform finite sample analysis, which is divided in two parts. First, in Section 4, we provide high probability upper bounds for the error ${\|{G - \hat{G}}\|}_{2}$ in the regression step. Then, in Section 5, we analyze the robustness of the balanced realization step.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Finite Sample Analysis of Regression", "weight": 1.0} -->

In this section, we provide the finite sample analysis of the linear regression step of the identification algorithm. We provide high-probability upper bounds for estimation error ${\|{G - \hat{G}}\|}_{2}$ of the Hankel-like matrix $G$. Before we state the main result, let us introduce some notation. Recall the definition of the innovation covariance matrix $\overline{R}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Finite Sample Analysis of Regression", "weight": 1.0} -->

In Lemma B.2 in the Appendix, we show that $\sigma_{E} \geq {\sigma_{\min}(R)} > 0$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1 (Result interpretation)", "weight": 1.0} -->

The first term in (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) corresponds to the cross-term error, while the second term corresponds to the Kalman filter truncation bias term. To obtain consistency for $\hat{G}$, we have to let the term $\left\| {({A - {KC}})}^{p} \right\|_{2}$ go to zero with $N$. Recall that the matrix $A - {KC}$ has spectral radius less than one, thus, the second term decreases exponentially with $p$. By selecting $p = {c{\log N}}$, for some $c$, we can force the Kalman truncation error term to decrease at least as fast as the first one, see for example. In this sense, the dominant term is the first one, i.e. the cross-term. Notice, that $f$ can be kept bounded as long as it is larger than $n$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 1 (Result interpretation)", "weight": 1.0} -->

Notice that the norm $\left\| \mathcal{O}_{p}^{\dagger} \right\|$ remains bounded by $\left\| \mathcal{O}_{n}^{\dagger} \right\|$ as $p$ increases--see Lemma E.3. ‣ Appendix E Bounds for system matrices ‣ Finite Sample Analysis of Stochastic System Identification") in Appendix. $\diamond$

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

To the best of our knowledge, there have not been any bounds for the performance of subspace algorithms in the case of marginally stable systems.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

As a result, our finite sample bound (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) is consistent with the asymptotic bound in equation of as $N$ grows to infinity. $\diamond$

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

In the absence of inputs (${B,D} = 0$), the noise both helps and obstructs identification. Larger noise leads to better excitation of the outputs, but also worsens the convergence of the least squares estimator. To see how our finite sample bounds capture that, observe that larger noise leads to bigger $\sigma_{E}$ but also bigger $\left\| \overline{R} \right\|_{2}$. This trade-off is captured by $\mathcal{C}_{1}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

If $N$ is sufficiently large (condition $N \geq {N_{0},N_{1}}$), the outputs are guaranteed to be persistently exciting in finite time; more details can be found in Section 4.1 and the Appendix. Meanwhile, condition $N \geq N_{2}$ is not necessary; it just leads to a simplified expression for the bound of the Kalman filter truncation error--see Section 4.3 and Appendix. The definitions of $N_{0},N_{1},N_{2}$ can be found in (B.1), (B.5), (C.3). Their existence is guaranteed even if $p$ varies slowly with $N$, i.e. logarithmically.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

Obtaining the bound on the error ${\|{G - \hat{G}}\|}_{2}$ in (26. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) of Theorem 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

Proving persistence of excitation (PE) for the past outputs, i.e. invertibility of $Y_{-}Y_{-}^{\ast}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

Establishing bounds for the cross-term error in (29. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

Establishing bounds for the the Kalman truncation error in (29. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 2 (Statistical rates)", "weight": 1.0} -->

In the following subsections, we sketch the proof steps.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Persistence of Excitation in Finite Time", "weight": 1.0} -->

The next theorem shows that with high probability the past outputs and noises are persistently exciting in finite time. The result is of independent interest and is fundamental since most subspace algorithms use past outputs as regressors.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Cross-term error", "weight": 1.0} -->

To bound the cross-term error, we express it as a product of $E_{+}Y_{-}^{\ast}\left( {Y_{-}Y_{-}^{\ast}} \right)^{- {1/2}}$ and ${({Y_{-}Y_{-}^{\ast}})}^{- {1/2}}$, as. The second term of the product can be bounded by applying Theorem 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification"). The first term is self-normalized and has martingale structure component-wise.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Cross-term error", "weight": 1.0} -->

where every sum above is a martingale. To bound it, we apply the next theorem, which generalizes Theorem 1 in and Proposition 8.2.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Kalman truncation error", "weight": 1.0} -->

From Theorem 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification"), we obtain $\left\| {\mathcal{T}_{p}E_{-}E_{-}^{\ast}\mathcal{T}_{p}^{\ast}{({Y_{-}Y_{-}^{\ast}})}^{- 1}} \right\|_{2} \leq 2$. The last term in can be treated like the cross-term in Section 4.2, by applying Theorems 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification"), 3. ‣ 4.2 Cross-term error ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") and Lemma B.3. ‣ Appendix B Persistence of Excitation ‣ Finite Sample Analysis of Stochastic System Identification").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Kalman truncation error", "weight": 1.0} -->

It decreases with a rate of $\mathcal{O}\left( {1/\sqrt{N}} \right)$ up to logarithmic terms, so it is much smaller than the other terms. To keep the final bound simple, we select $N_{2}$ such that

<!-- chunk {"id": "body-0057", "role": "body", "section": "Kalman truncation error", "weight": 1.0} -->

with high probability--see also (C.3) for the definition of $N_{2}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Robustness of Balanced Realization", "weight": 1.0} -->

In this section, we analyze the robustness of the balanced realization. In particular, we upper bound the estimation errors of matrices $A,C,K$ in terms of the estimation error ${\|{G - \hat{G}}\|}_{2}$ obtained by Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification").

<!-- chunk {"id": "body-0059", "role": "body", "section": "Robustness of Balanced Realization", "weight": 1.0} -->

The respective matrices $\overline{C},\overline{K},\overline{A}$ are defined similarly, based on ${\overline{\mathcal{O}}}_{f},{\overline{\mathcal{K}}}_{p}$, as described in Section 3. The system matrices $\overline{C},\overline{K},\overline{A}$ are equivalent to the original matrices $C,K,A$ up to a similarity transformation $\overline{C} = {CS}$, $\overline{K} = {S^{- 1}K}$, $\overline{A} = {S^{- 1}AS}$ for some invertible $S$. For simplicity, we will quantify the estimation errors in terms of the similar $\overline{A},\overline{C},\overline{K}$ instead of the original $A,C,K$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Robustness of Balanced Realization", "weight": 1.0} -->

The next result follows the steps of and relies on Lemma 5.14 of and Theorem 4.1 of. Let $\sigma_{n}( \cdot )$ denote the $n -$th largest singular value.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The result states that if the error of the regression step is small enough, then the realization is robust. The singular value $\sigma_{n}(G)$ can be quite small. Hence, the robustness condition (36. ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Stochastic System Identification")) can be quite restrictive in practice. However, such a condition is a fundamental limitation of the SVD procedure. The gap between the singular values of $G$ and the singular values coming from the noise $G - \hat{G}$ should be large enough; this guarantees that the singular vectors related to small singular values of $G$ are separated from the singular vectors coming from the noise $G - \hat{G}$, which can be arbitrary. See also Wedin's theorem. Such robustness conditions have also appeared in model reduction theory. $\diamond$

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 4 (Total bounds)", "weight": 1.0} -->

The final upper bounds for the estimation of the system parameters $A,C,K$, as stated in Problem 1. ‣ 2 Problem formulation ‣ Finite Sample Analysis of Stochastic System Identification"), can be found by combining the finite sample guarantees of the regression step (Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) with the robustness analysis of the realization step (Theorem 4. ‣ 5 Robustness of Balanced Realization ‣ Finite Sample Analysis of Stochastic System Identification")). All matrix estimation errors depend linearly on the Hankel matrix estimation error ${\|{G - \hat{G}}\|}_{2}$. As a result, all matrix errors have the same statistical rate as the error of $G$, i.e. their estimation error decreases at least as fast as $\mathcal{O}\left( {1/\sqrt{N}} \right)$ up to logarithmic factors. $\diamond$

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

One of the main differences between the subspace algorithm considered in this paper and other stochastic subspace identification algorithms is the SVD step. The other algorithms perform SVD on $W_{1}GW_{2}$ instead of $G$, where $W_{1},W_{2}$ are full rank weighting matrices, possibly data dependent. From this point of view, the results of Section 4 (upper bound for $\|{G - \hat{G}}\|$ in Theorem 1. ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification") and persistence of excitation in Theorem 2. ‣ 4.1 Persistence of Excitation in Finite Time ‣ 4 Finite Sample Analysis of Regression ‣ Finite Sample Analysis of Stochastic System Identification")) are fundamental for understanding the finite sample properties of other subspace identification algorithms. Here, we studied the case ${W_{1} = I},{W_{2} = I}$, which is not the standard choice.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

It is subject of future work to explore how the choice of $W_{1},W_{2}$ affects the realization step, especially the robustness condition of the SVD step.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

We could also provide finite sample bounds for the estimation of the closed-loop matrix $A_{c} \triangleq {A - {KC}}$. This can be done in two ways. One option is to form matrix $\hat{A} - {\hat{K}\hat{C}}$ from the estimates $\hat{A},\hat{C},\hat{K}$. Alternatively, we could estimate $\hat{A_{c}}$ directly from ${\hat{\mathcal{K}}}_{p}$ in the same way that we estimated $\hat{A}$. However, we do not have finite sample guarantees for the stability of the closed-loop estimates $\hat{A} - {\hat{K}\hat{C}}$, $\hat{A_{c}}$. It would be interesting to address this in future work.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Another direction for future work is repeating the analysis when the Kalman filter has not reached steady-state, i.e. relax Assumption 2. Finally, in this work, we only considered upper bounds. It would be interesting to study lower bounds as well to evaluate the tightness of our upper bounds. In any case, from lower bounds for fully observed systems, the factor of $1/\sqrt{N}$ is tight.
