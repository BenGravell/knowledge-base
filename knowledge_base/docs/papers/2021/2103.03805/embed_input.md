<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Topological Linear System Identification via Moderate Deviations Theory

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Two dynamical systems are topologically equivalent when their phase-portraits can be morphed into each other by a homeomorphic coordinate transformation on the state space. The induced equivalence classes capture qualitative properties such as stability or the oscillatory nature of the state trajectories, for example. In this paper we develop a method to learn the topological class of an unknown stable system from a single trajectory of finitely many state observations. Using a moderate deviations principle for the least squares estimator of the unknown system matrix theta, we prove that the probability of misclassification decays exponentially with the number of observations at a rate that is proportional to the square of the smallest singular value of theta.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the discrete-time linear time-invariant system where $x_{t}\in\mathbb{R}^{n}$ and $w_{t}\in\mathbb{R}^{n}$ denote the state and the exogenous noise at time $t\in\mathbb{N}$, while $\theta$ represents the system matrix, and $\nu$ stands for the marginal distribution of the initial state $x_{0}$. Except for asymptotic stability we assume that nothing is known about $\theta$, and we aim to identify $\theta$ from a single trajectory of states $\{\widehat{x}_{t}\}_{t=0}^{T}$ generated. A simple estimator for $\theta$ is the least squares estimator which may take any value in $\mathbb{R}^{n\times n}$. It is therefore possible that $\widehat{\theta}_{T}$ is unstable even though $\theta$ is stable, in which case the estimator is of limited practical value.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternative estimators with attractive statistical properties that are guaranteed to be stable have been proposed in \[undef, undefa, undefb, undefc\]. However, stability is not the only property of $\theta$ that impacts the qualitative behavior of a linear system; see Figure 1. As optimal control laws are known to inherit important structural properties from the system matrix \[undefd, Theorem III.1\], one should aim to find estimators that are structurally equivalent to $\theta$. That is, if the least squares estimator $\widehat{\theta}_{T}$ is structurally different from $\theta$ itself, in a sense to be made precise later, then implementing optimal linear feedback designed for $\widehat{\theta}_{T}$ on $\theta$ results in a closed-loop system that is structurally different from the predicted closed-loop system, e.g., you predict a damper but get a spring. Capturing the correct qualitative behaviour in the scalar case translates to enforcing stability and to the need of estimating the sign of $\theta$ correctly.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generalizing this qualitative notion of topological equivalence to higher dimensions will be the main subject of Section II-A below.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work. Linear system identification---especially by means of least squares techniques---has a rich history \[undefe, undeff\]. In this paper we are, however, not only interested in finding estimators that fall into the vicinity of the unknown true model $\theta$. In addition, the estimators should display a qualitatively similar behavior as $\theta$. This requirement relates to some extent to the work on qualitative identification pioneered by \[undefg\]. More recently, the focus in linear system identification shifted towards ensuring the efficient use of data. General informativity of data is discussed in \[undefh\], which justifies the identification pipeline for a class of control problems. Moreover, sharp statistical characterizations of the effectiveness of the least squares estimator are presented in \[undefi, undefj\]. These statistical results usually quantify the likelihood that $\theta$ lies in some ball around $\widehat{\theta}_{T}$. However, the models residing within this ball may be qualitatively different.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging recent results from the theory of large and moderate deviations \[undefk, undefl, undefm\], we will be able to characterize the likelihood that the estimated system is qualitatively equivalent to the unknown true system.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regarding topological equivalence in the context of linear control systems, \[undefn\] stated in 1980 that "Because of the obvious... practical importance of these concepts,... there is no doubt that they will become standard vocabulary among practitioners." Although \[undefo\] later provided many additional insights, there has been little recent follow-up work on topological properties of control systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. A high-level aim of this work is to showcase how topological insights can benefit the control community. More specifically, we establish topological properties of the reverse $I$-projection $\mathcal{P}(\cdot)$ introduced in \[undefc\], which projects any matrix in $\mathbb{R}^{n\times n}$ onto the non-convex set of stable matrices with respect to an information divergence and can be evaluated highly efficiently. By exploiting tools from moderate deviations theory, we characterize here the probability that the reverse $I$-projection $\mathcal{P}(\widehat{\theta}_{T})$ of the least-squares estimator $\widehat{\theta}_{T}$ is topologically different from $\theta$. Formally, we show that where '$\overset{t}{\sim}$' denotes topological equivalence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, the probability that $\mathcal{P}(\widehat{\theta}_{T})$ misrepresents the topological properties of $\theta$ decays exponentially with $T$ at a rate $\propto\sigma_{\mathrm{min}}(\theta)^{2}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Topological equivalence of linear dynamical systems", "weight": 1.0} -->

This section is mainly inspired by the work of Kuiper and Robbin \[undefp, undefq\]. In the following we denote by $f(x)=\theta x$ the state-dependent part of the dynamics, and we refer to the function $f$ as the time-one map. While all time-one maps considered in this paper are linear, our results naturally extend to nonlinear systems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Moderate deviations theory", "weight": 1.0} -->

Throughout the paper we assume that all random objects are defined on a measurable space $(\Omega,\mathcal{F})$ equipped with a probability measure $\mathbb{P}_{\theta}$ parametrized by the (asymptotically stable) system matrix $\theta\in\Theta$. We denote the expectation operator with respect to $\mathbb{P}_{\theta}$ by $\mathbb{E}_{\theta}[\cdot]$. From now on we impose the following assumption borrowed from \[undefc\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption II.4 (Linear system)", "weight": 1.0} -->

The system is asymptotically stable, i.e., $\theta\in\Theta$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption II.4 (Linear system)", "weight": 1.0} -->

For each $\theta\in\Theta$ the disturbances $\{w_{t}\}_{t\in\mathbb{N}}$ are independent and identically distributed (i.i.d.) and independent of $x_{0}$ under $\mathbb{P}_{\theta}$. The disturbances are unbiased ($\mathbb{E}_{\theta}[w_{t}]=0$) and non-degenerate ($S_{w}=\mathbb{E}_{\theta}[w_{t}w_{t}^{\mathsf{T}}]\succ 0$), and their probability density is everywhere positive.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption II.4 (Linear system)", "weight": 1.0} -->

Assumption II.4. ‣ II-B Moderate deviations theory ‣ II Preliminaries ‣ Topological Linear System Identification via Moderate Deviations Theory") implies that the linear system admits an invariant distribution $\nu_{\theta}$ \[undefv, § 10.5.4\] with zero mean and covariance matrix $S_{\theta}$, which is given by the unique positive definite solution of the discrete Lyapunov equation see, e.g., \[undefw, § 6.10 E\]. Next, we describe a method to characterize the probability of the least squares estimator $\widehat{\theta}_{T}$ deviating from $\theta$ by a prescribed threshold. To this end, we denote by $\Theta^{\prime}=\mathbb{R}^{n\times n}$ the space of all estimator realizations that are possible in view of Assumption II.4.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption II.4 (Linear system)", "weight": 1.0} -->

‣ II-B Moderate deviations theory ‣ II Preliminaries ‣ Topological Linear System Identification via Moderate Deviations Theory"), and we use the discrepancy function $I:\Theta^{\prime}\times\Theta\rightarrow[0,\infty]$ with to quantify the difference between an estimator realization $\theta^{\prime}\in\Theta^{\prime}$ and the system matrix $\theta\in\Theta$; see \[undefc\]. Here, the invariant state covariance matrix $S_{\theta}$ is defined as. Note that $S_{\theta}$ and thus also $I(\theta^{\prime},\theta)$ diverge as $\theta$ approaches the boundary of $\Theta$ and becomes unstable. Note also that since $S_{w}\succ 0$ and hence $S_{\theta}\succ 0$, $I(\theta^{\prime},\theta)$ vanishes if and only if $\theta^{\prime}=\theta$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption II.4 (Linear system)", "weight": 1.0} -->

In this sense $I$ behaves like a distance. Note, however, that $I(\theta^{\prime},\theta)$ is not symmetric in $\theta$ and $\theta^{\prime}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption II.4 (Linear system)", "weight": 1.0} -->

Next we recall the notions of a rate function and a moderate deviation principle (MDP) such that we can review the key results of \[undefc\]. For a comprehensive introduction to moderate deviations theory we refer to \[undefl, undefm\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption II.7 (Light-tailed noise and stationarity)", "weight": 1.0} -->

The following hold for every $\theta\in\Theta$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption II.7 (Light-tailed noise and stationarity)", "weight": 1.0} -->

The initial distribution $\nu$ coincides with the invariant distribution $\nu_{\theta}$ of the linear system.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption II.7 (Light-tailed noise and stationarity)", "weight": 1.0} -->

We can now formally state the MDP for the estimators.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example II.9 (Scalar system identification and noise invariance)", "weight": 1.0} -->

Consider a scalar system with $S_{w}=\sigma_{w}^{2}>0$. As shown in \[undefc, Example 3.5\], Proposition II.8. ‣ II-B Moderate deviations theory ‣ II Preliminaries ‣ Topological Linear System Identification via Moderate Deviations Theory") implies that for any $\varepsilon>0$ and $T\in\mathbb{N}$. Thus, the decay rate on right hand side of the above expression is independent of the noise intensity $\sigma_{w}^{2}$. If $n>1$, define $Z(\theta^{\prime},\theta)=(\theta^{\prime}-\theta)\otimes(\theta^{\prime}-\theta)(I_{n^{2}}-\theta\otimes\theta)^{-1}$, where $\otimes$ denotes the Kronecker product. By \[undefx, p.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example II.9 (Scalar system identification and noise invariance)", "weight": 1.0} -->

265\], the rate function can then be recast as where $\mathrm{vec}(S_{w})\in\mathbb{R}^{n^{2}}$ represents the vector obtained by stacking the columns of $S_{w}$ on top of each other. This representation reveals that the rate function is indeed invariant under scaling of the noise covariance matrix, that is, it is independent of the overall noise level for all $n\in\mathbb{N}$. ∎ We finally highlight that the rate function can be used to construct a reverse $I$-projection defined through which maps any point $\theta^{\prime}\in\Theta^{\prime}$ to the nearest point in the non-convex set $\Theta$ of asymptotically stable matrices with respect to the $I$-distance; see \[undefc\].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example II.9 (Scalar system identification and noise invariance)", "weight": 1.0} -->

The reverse $I$-projection $\mathcal{P}(\widehat{\theta}_{T})$ of the least squares estimator $\widehat{\theta}_{T}$ provides an estimator for $\theta$ that is stable by construction, has desirable statistical properties and can be efficiently computed. Indeed, one can show that for some $p\geq 1$, where $\mathsf{dlqr}(\cdot)$ denotes the standard discrete-time LQR routine,^11^1 see \[undefc, §3.3\].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example II.9 (Scalar system identification and noise invariance)", "weight": 1.0} -->

In addition, the reverse $I$-projection preserves orientation, i.e., $\mathrm{or}(\mathcal{P}(\theta^{\prime}))=\mathrm{or}(\theta^{\prime})$ for any $\theta^{\prime}\in\mathsf{GL}(n,\mathbb{R})$, see, e.g., \[undefc, Corollary 3.12\] and \[undefd\]. In fact, the numerical approximation of $\mathcal{P}(\theta^{\prime})$ on the right hand side of without the error term $\mathcal{O}(\delta^{p})$ is also asymptotically stable and preserves orientation for any $\delta>0$. Due to its desirable statistical and computational properties, our proposed approach to estimate the topological class of $\theta\in\Theta$ will critically rely on the reverse $I$-projection $\mathcal{P}(\widehat{\theta}_{T})$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main results", "weight": 1.0} -->

To aid the presentation we assume from now on without much loss of generality that $\theta$ is invertible. We are now ready to demonstrate that the MDP of Proposition II.8. ‣ II-B Moderate deviations theory ‣ II Preliminaries ‣ Topological Linear System Identification via Moderate Deviations Theory") allows us via the reverse $I$-projection $\mathcal{P}(\widehat{\theta}_{T})$ to derive sharp bounds on the decay rate of the probability of the event $\mathcal{P}(\widehat{\theta}_{T})\not\overset{t}{\sim}\theta$. Recall from Lemma II.3. ‣ II-A Topological equivalence of linear dynamical systems ‣ II Preliminaries ‣ Topological Linear System Identification via Moderate Deviations Theory") that the two stable and ($\mathbb{P}_{\theta}$-almost surely) invertible matrices $\mathcal{P}(\widehat{\theta}_{T})$ and $\theta$ are topologically equivalent if and only if they have the same orientation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main results", "weight": 1.0} -->

Recall also that $\mathrm{or}(\mathcal{P}(\widehat{\theta}_{T}))=\mathrm{or}(\widehat{\theta}_{T})$ because the reverse $I$-projection preserves orientation. Checking whether $\mathcal{P}(\widehat{\theta}_{T})$ is topologically equivalent to $\theta$ is thus tantamount to checking whether the determinants of $\widehat{\theta}_{T}$ and $\theta$ have the same signs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Implications of Theorem III.1. ‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory\")", "weight": 1.0} -->

As the rate $r$ derived in Theorem III.1. ‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory") is a function of $\theta$, the properties of the unknown system matrix $\theta$ determine the likelihood of topological misclassification. In high-performance applications where some eigenvalues of $\theta$ are close to $0$, for example, the sign of the determinant of $\theta$ and therefore the topological class of the underlying system are difficult to estimate. As such applications are usually safety-critical, however, inferring the correct topological class is of utmost importance. In the context of Figure 1, designing a controller tailored to a damper might be detrimental if the true system is a spring. Theorem III.1. ‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory") indicates that designing a system for high performance in the sense of constructing some eigenvalues of $\theta$ to be close to $0$ is in conflict with the reliable and fast identification of the system's topological class.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Implications of Theorem III.1. ‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory\")", "weight": 1.0} -->

Quantitative notions of stability and controllability, which strengthen the standard qualitative notions of stability and controllability, respectively, offer further insights into (9b. ‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory")).

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A1 Tuning $\\sigma_{\\mathrm{min}}(\\theta^{\\circ})$ and the noise covariance matrix", "weight": 1.0} -->

‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory"). Next, assume that $\theta$ is diagonalizable, i.e., $\theta=V\Lambda V^{-1}$ for some diagonal matrix $\Lambda$ and invertible matrix $V$. As $\sigma_{\mathrm{min}}(\theta^{\circ})\leq\lambda_{\mathrm{min}}(\theta^{\circ})=\lambda_{\mathrm{min}}(\theta)$, the preferred noise covariance matrix for which $\sigma_{\mathrm{min}}(\theta^{\circ})$ matches the bound $\lambda_{\mathrm{min}}(\theta)$ (which is independent of $S_{w}$) is given by $S_{w}=\alpha VV^{\mathsf{T}}$ for any $\alpha>0$. As already pointed out in Example II.9.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A1 Tuning $\\sigma_{\\mathrm{min}}(\\theta^{\\circ})$ and the noise covariance matrix", "weight": 1.0} -->

‣ II-B Moderate deviations theory ‣ II Preliminaries ‣ Topological Linear System Identification via Moderate Deviations Theory") the magnitude of $S_{w}$ is not important, its principal axes are.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A3 Minimizing interconnections", "weight": 1.0} -->

Consider a separable and an interconnected system with for some $Y\in\Theta$, respectively. One can show that $\sigma_{\mathrm{min}}(\theta_{1})\geq\sigma_{\mathrm{min}}(\theta_{2})$, which aligns with intuition: if possible, identify subsystems individually.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

We now compare the theoretical decay rate of topological misclassification derived in Theorem III.1. ‣ III Main results ‣ Topological Linear System Identification via Moderate Deviations Theory") against the empirical decay rate for the nominal least squares estimator $\widehat{\theta}_{T}$ and its reverse $I$-projection $\mathcal{P}(\widehat{\theta}_{T})$. Concurrently, we exemplify the insights from Section III-A3. To this end, we set and simulate system for both $\theta_{1}$ and $\theta_{2}$ defined as in Section III-A3 starting from $E=10^{3}$ initial conditions $x_{0}\overset{i.i.d.}{\sim}\mathcal{N}(0,I_{4})$ with $S_{w}=I_{4}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

Each initial condition leads to a trajectory under both $\theta_{1}$ and $\theta_{2}$ from which we construct the corresponding least squares estimators $\widehat{\theta}^{(i)}_{j,T}$, $i=1,\dots,E$, $T=1,\dots,10^{3}$, $j\in\{1,2\}$. Averaging over the $E$ simulation runs yields the empirical probability that $\widehat{\theta}_{j,T}$ or its reverse $I$-projection are topologically equivalent to the true system matrix $\theta_{j}$.
