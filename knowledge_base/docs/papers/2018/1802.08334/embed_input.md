<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning without Mixing: Towards a Sharp Analysis of Linear System Identification

Topics include System identification, Generalization, Learning, Mixing, Ordinary least squares, Linear systems, Linear dynamical system.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We prove that the ordinary least-squares (OLS) estimator attains nearly minimax optimal performance for the identification of linear dynamical systems from a single observed trajectory. Our upper bound relies on a generalization of Mendelson's small-ball method to dependent data, eschewing the use of standard mixing-time arguments. Our lower bounds reveal that these upper bounds match up to logarithmic factors. In particular, we capture the correct signal-to-noise behavior of the problem, showing that more unstable linear systems are easier to estimate. This behavior is qualitatively different from arguments which rely on mixing-time calculations that suggest that unstable systems are more difficult to estimate. We generalize our technique to provide bounds for a more general class of linear response time-series.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification---the problem of estimating the parameters of a dynamical system given a time series of its trajectories--- is a fundamental problem in time-series analysis, control theory, robotics, and reinforcement learning. Despite its importance, sharp, non-asymptotic analyses for the sample complexity of system identification are rare. In particular, it is not known how many trajectories required to identify the parameters of an unknown *linear* system. Properly characterizing this sample complexity would have profound implications, since accurate error bounds are indispensable for designing robust and high-performing control systems. It is important that the bounds be sharp, in the sense that they do not drastically *overestimate* the number of required measurements from system trajectories, which are often time-consuming and prohibitively expensive to collect. More broadly, a deeper understand of system identification would inform other statistical problems where one wishes to learn from non-i.i.d. or time-correlated data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on the problem of identifying a discrete-time *linear dynamical system* from an observed trajectory. Such systems are described by two parameter matrices $A_{\ast}$ and $B_{\ast}$, and the dynamics evolve according to the law $X_{t + 1} = {{A_{\ast}X_{t}} + {B_{\ast}u_{t}} + \eta_{t}}$, where $X_{t} \in {\mathbb{R}}^{d}$ is the state of the system, $u_{t}$ is the input of the system, and $\eta_{t} \in {\mathbb{R}}^{d}$ denotes unobserved process noise. Linear systems are fundamental in control theory, since they are able to capture the behavior of many natural systems and also able to accurately describe the evolution of an even broader class of systems near their equilibria.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the importance of understanding the statistical properties of system identification, the relationship between the matrix $A_{\ast}$ and the statistical rate for estimating this matrix remains poorly understood. We note that the larger the state vectors $X_{t}$ are in comparison to the process noise, the larger the *signal-to-noise ratio* for estimating $A_{\ast}$ is. As a result, larger matrices $A_{\ast}$ (larger in an appropriate sense, discussed later) lead to states $X_{t}$ of larger norm, which in turn should make the estimation of $A_{\ast}$ easier. However, it is difficult to theoretically formalize this intuition because the sequence of measurements $X_{0},X_{1},\ldots,X_{T - 1}$ used for estimation is not i.i.d. and it is dependent on the noise $\eta_{0},\eta_{1},\ldots,\eta_{T - 2}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even the computationally straightforward ordinary least-squares ($\mathsf{O}\mathsf{L}\mathsf{S}$) estimator is difficult to analyze. Standard analyses for $\mathsf{O}\mathsf{L}\mathsf{S}$ on random design linear regression cannot be used due to the dependency between the covariates $X_{t}$ and the process noise $\eta_{t}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the statistics and machine learning literature, correlated data is usually dealt with using mixing-time arguments, which relies on fast convergence to a stationary distribution that allows correlated samples to be treated roughly as if they were independent. While this approach has been successfully used to develop generalization bounds for time-series data, a fundamental limitation of mixing-time arguments is that the bounds deteriorate when the underlying process is slower to mix. In the case of linear systems, this behavior is qualitatively incorrect. For linear systems, the rate of mixing is intimately tied to the eigenvalues of the matrix $A_{\ast}$, specifically the *spectral radius* $\rho{(A_{\ast})}$. When ${\rho{(A_{\ast})}} < 1$ (i.e. when the system is *stable*), the process mixes to a stationary distribution at a rate that deteriorates as $\rho{(A_{\ast})}$ approaches the boundary of one.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, as discussed above, as $\rho{(A_{\ast})}$ increases we expect estimation to become easier due to better signal-to-noise ratio, and not harder as mixing-time arguments suggest. We note that recent work by Faradonbeh et al. studying the estimation problem for linear systems relies in the stable case on concentration of measure arguments which also degrade as the mixing-time of the system grows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address these difficulties and offer a new statistical analysis of the ordinary least-squares ($\mathsf{O}\mathsf{L}\mathsf{S}$) estimator of the dynamics $X_{t + 1} = {{A_{\ast}X_{t}} + \eta_{t}}$ with no inputs, when the spectral radius of $A_{\ast}$ is at most one (${\rho{(A_{\ast})}} \leq 1$, a regime known as *marginal stability*). Our results, detailed in Section 2, show that the statistical performance of $\mathsf{O}\mathsf{L}\mathsf{S}$ is determined by the minimum eigenvalue of the (finite-time) controllability Gramian $\Gamma_{T} = {\sum_{s = 0}^{T - 1}{A_{\ast}^{s}{(A_{\ast}^{\top})}^{s}}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The controllability Gramian is a fundamental quantity in the theory of linear systems; the eigenvalues of the Gramian quantify how much white process noise $\eta_{t}\overset{i.i.d}{\sim}\mathcal{N}{(0,{\sigma^{2}I})}$ can excite the system. We show that a larger $\lambda_{\min}{(\Gamma_{T})}$ leads to faster estimation of $A_{\ast}$ in operator norm, and we also prove that up to log factors the $\mathsf{O}\mathsf{L}\mathsf{S}$ estimator is minimax optimal. Furthermore, in Section 2.3 we offer similar statistical guarantees for a more general class of linear response time-series.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Results", "weight": 1.0} -->

In this work, we consider both the specific problem of estimating linear dynamical systems, and a more general problem of linear estimation in time series. In both cases we measure the estimation error in the operator norm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Results", "weight": 1.0} -->

In Section 2.2, we show that these upper bounds are nearly optimal in many regimes of interest. Finally, Section 2.3 states a general result, Theorem 2.4, which applies to arbitrary covariate processes with linear responses.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Results", "weight": 1.0} -->

Notation: We let $\parallel \cdot \parallel_{op}$ denote the operator norm of a matrix, $\mathcal{S}^{d - 1}$ denote the unit sphere in ${\mathbb{R}}^{d}$. Given a symmetric matrix $A \in {\mathbb{R}}^{d \times d}$, we let $\lambda_{\max}$ and $\lambda_{\min}$ denote the largest, and smallest eigenvalue of $A$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear Dynamical Systems", "weight": 1.0} -->

Indeed, we can write $X_{t}$ explicitly as Hence, the expected covariance can be expressed in terms of the Gramians via ${{\mathbb{E}}{\lbrack{\sum_{t = 1}^{T}{X_{t}X_{t}^{\top}}}\rbrack}} = {\sigma^{2} \cdot {\sum_{t = 1}^{T}\Gamma_{t}}}$. As is standard in analyses of least-squares, "larger" covariates/covariance matrices correspond to faster rates of learning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 2 (Noise dependence)", "weight": 1.0} -->

The estimation guarantee provided by Theorem 2.1 does not depend on the variance $\sigma^{2}$ of the noise $\eta_{t}$. This surprising property holds because the size of the variance $\sigma^{2}$ directly influences the size of the states $X_{t}$ leading to a cancellation in the signal-to-noise ratio. For Gaussian noise with a general identity covariance $\eta_{t} \sim {\mathcal{N}{(0,\Sigma)}}$, one can rederive rates from our more general Theorem 2.4 to get a more precise dependence on $\Gamma_{t}$ and $\Sigma$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 3 (Learning with input sequences)", "weight": 1.0} -->

Non-white noise with covariance not equal to a multiple of the identity can be absorbed into $B_{\ast}$. Moreover, other non-Gaussian control input processes $u_{t}$ could just as easily be accommodated by our Theorem 2.4. When $B_{\ast}$ is unknown, Theorem 2.4 still implies that we can learn $(A_{\ast},B_{\ast})$; however, the guarantees are in terms of the operator norm of the concatenation of the errors, ${\parallel{({\hat{A} - A_{\ast}},{\hat{B} - B_{\ast}})}\parallel}_{op}$; in particular, the bound does not differentiate between the error of $\hat{A}$ and the error of $\hat{B}$. We believe that developing guarantees that delineate between the errors in $\hat{A}$ and in $\hat{B}$ is an exciting direction for future work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Lower Bounds for Linear System Identification", "weight": 1.0} -->

We have seen in Theorem 2.1 and in the subsequent examples that the estimation of linear dynamical systems is easier for systems which are easily excitable. It is natural to ask what is the best possible estimation rate one can hope to achieve. To make explicit the dependence of the lower bounds on the spectrum of $\Gamma_{t}$, we consider the minimax rate of estimation over the set ${\rho \cdot O}{(d)}$, where $\rho \in {\mathbb{R}}$ and $O{(d)}$ denotes the orthogonal group. In this case, we can define an *scalar* Gramian ${\gamma_{t}{(\rho)}}:={\sum_{s = 0}^{t - 1}{|\rho|}^{2s}}$, and so that $\Gamma_{t}:={{\gamma_{t}{(\rho)}} \cdot I}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Lower Bounds for Linear System Identification", "weight": 1.0} -->

We now show that the estimation rate of the $\mathsf{O}\mathsf{L}\mathsf{S}$ provided in Theorem 2.1

<!-- chunk {"id": "body-0019", "role": "body", "section": "General Time Series with Linear Responses", "weight": 1.0} -->

To capture the excitation behavior observed in the case of linear systems we introduce a general martingale small-ball condition which quantifies the growth of the covariates $X_{t}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Analysis Techniques", "weight": 1.0} -->

We upper bound ${\parallel{\mathbf{U}^{\top}\mathbf{E}}\parallel}_{op}$ with Lemma 4.14, a martingale-Chernoff bound that gives precise control on the deviations of sub-Gaussian martingale sequences in terms of random variance proxies. We explain this argument in more detail at the end of Section 4.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

In this paper, we analyzed the the performance of the $\mathsf{O}\mathsf{L}\mathsf{S}$ estimator for the estimation of linear dynamics $X_{t + 1} = {{A_{\ast}X_{t}} + \eta_{t}}$ from a single trajectory $X_{0},X_{1},\ldots,X_{T}$, as a special case of linear estimation in time series. We show that, up to logarithmic factors, the $\mathsf{O}\mathsf{L}\mathsf{S}$ estimator attains an information-theoretic lower bound for ${\rho{(A_{\ast})}} < 1$, provided that $T \gtrsim \frac{d}{1 - {\rho{(A_{\ast})}}}$. Moreover, we present an analysis that eschews both mixing and concentration arguments for estimation in time series.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

We believe that there are several promising directions for future work: Our lower and upper bounds do not perfectly match, even when ${\rho{(A_{\ast})}} < 1$. We believe resolving these indiscrepancies may shed greater insight into learning in dynamical systems.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

While our analysis can accomodate an unknown $B_{\ast}$, the rates do not distinguish between the error in the estimation of $A_{\ast}$ and that of $B_{\ast}$. In future, we hope to develop sharp error rates for $A_{\ast}$ and $B_{\ast}$ individually, similar to Dean et al. in the independent covariates setting.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

While our guarantees are stated in the operator norm, control applications may require more granular notions of error which vary for different modes of $A_{\ast}$. Developing error bounds which capture the error rate at each mode may result in more applicable bounds for control applications downstream.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

Our convergences rates degrade for systems with ${\rho{(A_{\ast})}} > 1$, whereas we know from Faradonbeh et al. that these systems are still identifiable with $\mathsf{O}\mathsf{L}\mathsf{S}$. Is there a unified analysis for systems with stable and unstable modes?

<!-- chunk {"id": "body-0026", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

In many systems, we do not observe $X_{t}$ directly, but only view $CX_{t}$ for a short matrix $C \in {\mathbb{R}}^{n_{o} \times n}$, where $n_{0} \leq n$. Hazan et al. provide filtering techniques to minimize regret for diagonalizable matrices; it would be interesting to understand the sample complexity for estimating arbitrary matrices with these limited observations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

Ultimately, we would like to understand what sequences of control inputs $u_{t}$ yield the most accurate estimation of the system $(A_{\ast},B_{\ast})$. This would inform adaptive algorithms which adjust the sequence $u_{t}$ in a sequential fashion, and online algorithms which ensure low regret relative to a given cost functional over time.
