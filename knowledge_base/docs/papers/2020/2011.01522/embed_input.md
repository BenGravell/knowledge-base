<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Higher-Order Moment-Based Anomaly Detection

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The identification of anomalies is a critical component of operating complex, and possibly large-scale and geo-graphically distributed cyber-physical systems. While designing anomaly detectors, it is common to assume Gaussian noise models to maintain tractability; however, this assumption can lead to the actual false alarm rate being significantly higher than expected. Here we design a distributionally robust threshold of detection using finite and fixed higher-order moments of the detection measure data such that it guarantees the actual false alarm rate to be upper bounded by the desired one. Further, we bound the states reachable through the action of a stealthy attack and identify the trade-off between this impact of attacks that cannot be detected and the worst-case false alarm rate. Through numerical experiments, we illustrate how knowledge of higher-order moments results in a tightened threshold, thereby restricting an attacker's potential impact.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

From critical infrastructures and industrial process control to autonomous driving and various biomedical applications, dynamical control systems are increasingly able to be instrumented with new sensing and actuation capabilities. These cyber-physical systems (CPS) comprise growing webs of interconnected feedback loops and must operate efficiently and resiliently in dynamic and uncertain environments. As these systems become large, devising both model-based and data-driven methods for detecting anomalies (such as component failures or malicious attacks) are critical for their robust and efficient operation. Such critically important cyber-physical networks have become an attractive target to attackers. These systems are large and complex and are often not monitored well enough, enabling attackers to manipulate the system without being detected and cause damage.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To simplify the analysis and design, often such complex cyber-networks are modeled as a discrete-time linear time invariant system with Gaussian noises. However, this can lead to a significant miscalculation of probabilities and risk if the underlying processes behave differently, for example due to various nonlinearities or malicious attacks. In the context of attacks, it is possible for an attacker to modify the sensor outputs and effectively generate aggressive and strategic noise profiles to sabotage the operation of the system. With stochastic optimization techniques, particularly using the emerging area of distributionally robust optimization (DRO) approaches, these limitations can be recognized and addressed. DRO enables modelers to explicitly incorporate inherent ambiguity in probability distributions into optimization problems. DRO approaches can be categorized based on the form of the ambiguity set. There are several different parameterizations, including those based on moments, support, directional derivatives, and Wasserstein balls. In practice, we have access to only a finite amount of historical data. However, it is possible to use finite historical data and guarantee resiliency in such critical cyber-physical networks. Here, we propose to use moment-based DRO methods to improve modeling and reduce false alarm rates in cyber-physical networks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In the context of attacks, the detector tuning has a direct implication on the effect an attacker can have while still remaining stealthy. A model-based approach to attack detection uses a detector that raises alarms when there is a large enough discrepancy between the actual and predicted measurements, a statistic termed the residual. The detector's sensitivity can be increased by decreasing the threshold of detection, but there is an inherent trade-off between sensitivity and the rate at which false alarms are generated. Keeping false alarms to a manageable level requires adjusting sensitivity and the tuning of the detector threshold is typically informed by the distribution of the residual. Authors in used Gaussian Mixture Model to approximate the arbitrary noise distributions and obtained a detector threshold corresponding to a desired false alarm rate.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, when noise distributions are only known to an ambiguity set, traditional tools and approximations no longer suffice to select the threshold and so we turn to a distributionally robust approach. Interest in a DRO-informed perspective on detector tuning is supported by recent work on using a Wasserstein metric. Our moment-based ambiguity set formulation includes all distributions with fixed moments up to some order. The problem of designing anomaly detector thresholds subject to moment constraints of system uncertainties can be addressed using Generalized Moment Problems described. Further, the conditions for a truncated (finite) moment sequence to represent a probability measure were studied. Authors in proposed semidefinite programs to compute a probability bound for a random variable lying in a set with known moments up to some order. These techniques can be utilized to design detector thresholds for residual distributions consistent with finite fixed moments up to some order.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper is a significant extension of our previous work where we used a moment-based ambiguity set formulation with fixed first two moments (Proposition 2) to obtain a detector threshold via generalized Chebyshev inequality.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We propose an approach to construct moment-based ambiguity sets with fixed moments up to $k$ order for the anomaly detection measure and design an anomaly detector threshold for CPSs that exhibit non-Gaussian uncertainties. The approach can utilize either residual moments obtained through a dynamic model or estimated directly from residual data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We use a semidefinite program (SDP) defined using higher-order moments of the detection measure to find a sharper probability bound for classifying the residual with an improved detector threshold (Theorem 4-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")).

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We illustrate empirically that inclusion of higher-order moments results in tightened threshold (Lemma 3-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")), thereby restricting an attacker's potential impact, and also prove that the volume of the attack-reachable set shrinks with a tightened threshold (Corollary 5).

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

While anomaly detection is widely studied in CPS literature, our distributionally robust approach using higher-order moments of the detection measure data marks the novel contribution of this paper. The rest of the paper is organized as follows. Section II formulates the problem using moment-based ambiguity sets. In Section III, the design of anomaly detector threshold is discussed. Section IV describes the procedure to find the boundary of the reachable sets obtained using distributionally robust tuned detector. Section V presents the numerical results with inferences. Finally, Section VI concludes and summarizes the future research directions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation Using Higher-Order Moment-Based Ambiguity Sets", "weight": 1.0} -->

In this section, we propose a framework for designing an anomaly detector threshold for cyberphysical systems. The approach can utilize either model-based propagation of residual moments or data-driven estimation of detection measure moments directly from data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

Here, we model an uncertain cyber-physical system as a stochastic discrete-time linear system

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

where ${x_{t} \in {\mathbb{R}}^{n}},{u_{t} \in {\mathbb{R}}^{m}}$ are the system state and input respectively at time $t$. The matrices $A$ and $B$ denote the system matrix and control input matrix, respectively. The output $y_{t} \in {\mathbb{R}}^{p}$ aggregates a linear combination of the states with the observation matrix $C \in {\mathbb{R}}^{p \times n}$. We assume that the pair $(A,C)$ is detectable and $(A,B)$ is stabilizable. The process noise $w_{t} \in {\mathbb{R}}^{n}$ and the sensor noise $v_{t} \in {\mathbb{R}}^{p}$ are modeled as zero-mean random vectors independent and identically distributed across time with covariance matrix $\Sigma_{w},\Sigma_{v}$ respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

The distributions $P_{w}$ of $w_{t}$ and $P_{v}$ of $v_{t}$ are unknown (and not necessarily Gaussian and possibly heavy-tailed^11^1For the purposes of this paper, we consider heavy-tailed distributions as those whose moments above a certain order may be infinite, in which case their tails are heavier than a Gaussian. We assume the moments up to order $k$ are finite.) and will be assumed to belong to the $k$-moments-based ambiguity sets of distributions $\mathcal{P}_{k}^{w}$ and $\mathcal{P}_{k}^{v}$ respectively defined as follows

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

When the actual measurement $y_{t}$ is corrupted by an additive attack, $\delta_{t} \in {\mathbb{R}}^{p}$, the true output of the system fed to the controller becomes

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

We utilize a steady-state Kalman filter to construct a state estimate ${\hat{x}}_{t}$ to minimize the squared norm of the estimation error $e_{t} = {x_{t} - {\hat{x}}_{t}}$ where,

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

and the estimation error evolves as

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

In the absence of attacks (that is, $\delta_{t} = 0$) and when the covariance matrices of the noises are fixed and known, the Kalman gain $L = {PC^{\top}{({{CPC^{\top}} + \Sigma_{v}})}^{- 1}}$ minimizes the steady state covariance matrix

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

Since $(A,C)$ is assumed to be detectable, the existence of $P$ is guaranteed and it can be found through the solution of an algebraic Ricatti equation. We define a residual sequence $r_{t}$ as the difference between the actual received output ${\overline{y}}_{t}$ and the predicted output $C{\hat{x}}_{t}$ as,

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

and in the attack free setting, $r_{t}$ falls according to a zero mean distribution with covariance

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

Since is linear, it is possible to obtain the fixed and first $k$ moments of the random variable $r_{t}$ by propagating the corresponding moments of the primitive random variables $w_{t},v_{t}$. Thus, the distribution $P_{r}$ of $r_{t}$ (not necessarily Gaussian) belongs to an ambiguity set $\mathcal{P}_{k}^{r}$ given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

We define detection measure $q_{t}$ as a quadratic function of $r_{t}$

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Model-based Problem Formulation", "weight": 1.0} -->

which will be compared to a threshold for anomaly detection.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Data-Driven Moment Estimation from Residual Data", "weight": 1.0} -->

An alternative to obtaining residual moments by propagating the moments of primitive random variables through the system model is to instead collect residual data $r_{t}$ (from attack-free operation) and estimate residual moments or the moments of $q_{t}$ directly from the data. Such a data-driven approach allows our proposed tuning approaches to be used in much broader settings where it is difficult to propagate moments through a model (or even to obtain a model), but where residual data is easily generated from sensors and a state estimator. Higher-order moments require increasingly more data to obtain accurate estimates. Determining the required amount of data is possible using finite-sample measure concentration results given as, but we leave such an analysis for future work. The proposed methods for setting thresholds for anomaly detection can be used together with ambiguity sets built upon data-driven residual estimates, although the false alarm rates will also be affected by sampling errors. Moment estimation uncertainty could be accommodated using the same generalized moment problem computations we propose here, but with assumed *bounds* on moment estimates rather than having them fixed to exact known values.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Data-Driven Moment Estimation from Residual Data", "weight": 1.0} -->

Such problems can also be reformulated in a computationally tractable manner, as described, e.g., Section 3 of, which incorporate uncertainty sets for estimated moments. These formulations would simply impose further constraints on our primal problem defined in subsection III.B of our revised manuscript. It is possible and would be interesting to explore how to use statistical confidence intervals for data-driven moment estimates to inform bounds used in the SDP and obtain end-to-end guarantees on false alarm rates associated with certain thresholds. This will be pursued in future work.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Data-Driven Moment Estimation from Residual Data", "weight": 1.0} -->

In either setting, the feasible first $k$ moment sequence of the distribution of $q_{t}$ denoted by $M_{q}^{k}$ is assumed to be known either from its primitive variables through the model-based approach or estimated from data. Then, the $k$-moments-based ambiguity set of the scalar random variable $q_{t}$ is defined as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Design of Anomaly Detector Thresholds", "weight": 1.0} -->

Given a threshold ^22^2The first and second subscripts in the threshold separated by a comma denote the random variable and number of moments respectively.$\alpha_{q,k} > 0$ and the distance measure $q_{t}$, alarm time(s) $t^{\star}$ are produced according to the following rules,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Design of Anomaly Detector Thresholds", "weight": 1.0} -->

Even in the absence of attacks, the detector is expected to generate false alarms due to the infinite support of $v_{t}$, because some values drawn from $P_{q}$ will exceed the threshold $\alpha_{q,k}$. If $P_{q}$ is known, then it is possible to extract an optimum threshold value $\alpha_{q}^{\ast}$ from the corresponding cumulative distribution function $F_{q}$ for a desired false alarm rate, $\mathcal{A}$. For example, if $r_{t}$ is Gaussian, $q_{t}$ would be a chi-squared random variable, and the optimum threshold $\alpha_{q}^{\star}$ corresponding to the desired false alarm rate $\mathcal{A} = \mathcal{A}^{\star}$ is then

<!-- chunk {"id": "body-0030", "role": "body", "section": "Design of Anomaly Detector Thresholds", "weight": 1.0} -->

where ${\mathbb{P}}^{- 1}{( \cdot, \cdot )}$ denotes the inverse regularized lower incomplete gamma function. When the complete distribution is not available, tuning methods using may design thresholds that generate actual false alarm rates significantly higher than what is desired. With the distributionally robust approach, we aim to achieve a false alarm rate less than $\mathcal{A}$, and the detector threshold $\alpha_{r,k}^{\star}$ is selected such that

<!-- chunk {"id": "body-0031", "role": "body", "section": "Design of Anomaly Detector Thresholds", "weight": 1.0} -->

When the first two moments $({k = 2})$ of $r_{t}$ are known, the following proposition using the generalized Chebyshev inequality explained in can be used to obtain the worst case detector threshold $\alpha_{r,2}^{\star}$ satisfying.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Improved Detector Threshold With Higher-Order Moments", "weight": 1.0} -->

It is possible to obtain a sharpened detector threshold than $\alpha_{r,2}^{\star}$, if higher-order moments are taken into account. For example, the skewness and kurtosis parameters convey asymmetry and heaviness of tails of the distribution, respectively. We can leverage such information about the true but unknown distribution revealed by the higher-order moments to tighten the required probability bound and thereby obtain an improved detector threshold. It is possible to use $r_{t}$ with higher order moments (first $k$ moments) to obtain a sharpened detector threshold $\alpha_{r,k}^{\star}$. However, it was shown in that for $r_{t} \in {\mathbb{R}}^{p}$ with support $\Omega = {\mathbb{R}}^{p}$ and $k \geq 4$, it is NP-hard to find tight bounds for the corresponding moment bound problem with rational problem data. On the other hand, they provide a semidefinite optimization problem in $k + 1$ dimension for the case of a univariate random variable with $k$ moments.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Improved Detector Threshold With Higher-Order Moments", "weight": 1.0} -->

Hence, rather looking for higher-order moments of $r_{t}$, instead we look for higher-order moments of scalar random variable $q_{t}$. Subsequently, we use a bisection algorithm to obtain a sharpened detection threshold $\alpha_{q,k}^{\star}$ for a given $\mathcal{A}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Estimating Probability Using ${(1,k,\\Omega)} -$Moment Bound", "weight": 1.0} -->

Given the first $k$ moments of random variable $q_{t}$ with support $\Omega = {\mathbb{R}}_{\geq 0}$ and the set $\mathcal{S}_{k} = {\mathbb{R}}_{> \alpha_{q,k}}$ representing an alarm event as shown in Figure 1-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection"), the infinite dimensional ${(1,k,\Omega)} -$moment bound primal problem is given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Estimating Probability Using ${(1,k,\\Omega)} -$Moment Bound", "weight": 1.0} -->

Since (19-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) is infinite dimensional, it is difficult to solve efficiently. However, we can use the linear programming duality theory to associate a dual variable ${{y_{r},r} = 0},{1,\ldots,k}$ with each equality constraint of (19-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) to get the corresponding dual problem

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Estimating Probability Using ${(1,k,\\Omega)} -$Moment Bound", "weight": 1.0} -->

The probability obtained as the solution to (20-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) is an upper bound to the probability associated with (19-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")). In general, if the moment vector ${\overline{\sigma}}_{k} = {(M_{q}^{0},M_{q}^{1},{\ldotsM_{q}^{k}})}$ is an interior point of the set $\mathcal{M}_{k}$ of all feasible moment vectors, then strong duality exists between (19-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) and (20-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) enabling us to obtain a *tight* bound on $P_{q}{({q_{t} \in \mathcal{S}_{k}})}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Estimating Probability Using ${(1,k,\\Omega)} -$Moment Bound", "weight": 1.0} -->

To achieve a desired false alarm rate $\mathcal{A}$, we can tune the threshold $\alpha_{q,k}$ defining the set $\mathcal{S}_{k}$ such that solution to (20-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) is $\mathcal{A}$. The following lemma establishes the general trend observed between the values of the tuned threshold $\alpha_{q,k}$ for increasing values of $k$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Discussion", "weight": 1.0} -->

For $k = {1,2,3}$, the solution to (23-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) can be obtained in closed-form using Theorem 3.3 of with the corresponding moments data without explicitly solving the SDP in (23-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")). For $k = {1,2}$, we recover the Markov bound and a strictly improved Chebyshev bound respectively as the solution of (23-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")).

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Discussion", "weight": 1.0} -->

We omit the expression for the threshold $\alpha_{q,3}^{\star}$ for the sake of brevity.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Discussion", "weight": 1.0} -->

Further, the optimal threshold $\alpha_{q,k}^{\star}$ is tight for a given $\mathcal{P}_{k}^{q}$ up to a tolerance $\epsilon > 0$ specified by the bisection in Algorithm 1-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection").

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Discussion", "weight": 1.0} -->

The exact detector threshold (which we call $\alpha_{q}^{\star}$) corresponding to $P_{q}$ is obtained only asymptotically (or equivalently when true $P_{q}$ is known exactly). That is,

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Discussion", "weight": 1.0} -->

However, while determining how many moments are needed to get a close approximation of the exact threshold is difficult in general, we find that significant improvements can be obtained from a small number of moments. Given $k$ moments of $q_{t}$, the complexity of this higher-order moment based approach involves solving the SDP given by (23-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) with variables ${{X,Z} \in {\mathbb{R}}^{{({k + 1})} \times {({k + 1})}}},{{y_{r},r} = 0},{1,\ldots,k}$. For large $k$, it is advisable to use, e.g., the Legendre polynomial basis instead of the standard polynomial basis for obtaining the moment-based polynomial in (23-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) as the former has nice orthogonal properties that improve numerical stability.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Attack-Reachable Set Bounds", "weight": 1.0} -->

With the attacker assumed to have perfect knowledge of the system dynamics, the Kalman filter, control inputs, measurements along with read and write access to all the sensors at each time step, we show that the volume of the attack-reachable set shrinks with the tightened threshold. We define a zero-alarm attack, which generates attack sequences so that no alarms are raised during attack.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Attack-Reachable Set Bounds", "weight": 1.0} -->

where the noise threshold $\overline{w}$ obtained using satisfies,

<!-- chunk {"id": "body-0045", "role": "body", "section": "Attack-Reachable Set Bounds", "weight": 1.0} -->

and ${\hat{A} = \begin{bmatrix}
\end{bmatrix}},{\hat{B} = \begin{bmatrix}
\end{bmatrix}}$. Using the geometric approach presented in with $H_{i} = {A_{cl}^{i} - A^{i}}$, the reachable set of states is the Minkowski sum of the following ellipsoidal bound

<!-- chunk {"id": "body-0046", "role": "body", "section": "Attack-Reachable Set Bounds", "weight": 1.0} -->

Specifically, theorem 1 of provides us the exact boundary of Minkowski sum in using an analytical formula. The following corollary highlights the effects of the tightened threshold on the size of the reachable set.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

We consider an empirical system under study with the detector tuned to a false alarm rate $\mathcal{A} = 0.05$ ($5$%). We demonstrate here simulation results when the uncertainties are zero-mean Gaussian. We compare the size of the reachable set boundary computed using for thresholds $\alpha_{q,1}^{\star},\alpha_{q,2}^{\star},\alpha_{q,4}^{\star}$. We assume that the modeler is unaware of the functional form of the uncertainties and has to arrive at a detector threshold satisfying the desired false alarm rate. The SDP in (23-Moment Bound ‣ III Design of Anomaly Detector Thresholds ‣ Higher-Order Moment-Based Anomaly Detection")) was solved with $\epsilon = 10^{- 4}$ using SOSToolbox in Matlab with SeDuMi solver.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

When the noises $w_{t}$ and $v_{t}$ are truly Gaussian, it is evident from Fig. 2 that the reachable set corresponding to the thresholds $\alpha_{q,1}^{\star} = \alpha_{r,2}^{\star} = 40$ is conservative and ensures that the false alarm does not exceed 5% but this also provides the attacker with the ability to launch a larger attack. However, with the knowledge of additional moments, the detector thresholds $\alpha_{q,2}^{\star} = 10.7684$, $\alpha_{q,4}^{\star} = 9.1315$ get tightened with $\alpha_{q,4}^{\star} \leq \alpha_{q,2}^{\star} \leq \alpha_{q,1}^{\star}$ as shown in Fig. 3.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

Further, this threshold tightening limits the attacker's ability to launch a larger attack which is depicted through the reachable sets corresponding to the thresholds $\alpha_{q,1}^{\star},\alpha_{q,2}^{\star},\alpha_{q,4}^{\star}$ as shown in Fig. 2. Subsequently, the false alarm rate corresponding to the threshold $\alpha_{\chi^{2}}$ was 5% as expected and with the thresholds $\alpha_{q,4}^{\star},\alpha_{q,2}^{\star},\alpha_{q,1}^{\star}$, it dropped to ${1\%},{0.45\%},{0\%}$ respectively.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

When noises are truly multi-variate Laplacian (which has heavier tails than normal distribution with same mean and covariance), it resulted in thresholds $\alpha_{q,1}^{\star} = 39.83$, ${\alpha_{q,2}^{\star} = 17.23},{\alpha_{q,4}^{\star} = 16.54}$ with false alarm rates ${0\%},{0.9\%},{1\%}$ respectively. Thus, no matter what distributions satisfying, govern the noises $w_{t}$, $v_{t}$ respectively, the inclusion of higher-order moments restricts the attacker's potential impact through a tightened detector threshold.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

We have proposed a distributionally robust approach to form the $k$ moments based ambiguity set for the detection measure data and used it to tune the anomaly detectors for a desired false alarm rate. We found a detector threshold which guaranteed that the false alarm rate did not exceed a desired value using a semidefinite program. We have demonstrated the effectiveness of our proposed approach with a numerical example. Further, our approach using higher-order moments restricted the attacker's potential impact. Future works include addressing the problems associated with the data-driven formulation with moment estimation uncertainty and securing nonlinear cyberphysical systems with distributionally robust unscented Kalman filter based state estimation.
