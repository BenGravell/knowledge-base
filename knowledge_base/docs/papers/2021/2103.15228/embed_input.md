<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Anomaly Detection under Multiplicative Noise Model Uncertainty

Topics include Cyber-physical systems, Anomaly detection, Attack detection, Robust state estimation, Linear quadratic Gaussian control, Multiplicative noise, Model uncertainty, Stochastic systems, State-space models, Kalman filtering, Robust filtering, Sensor attacks, False data injection, Detection performance, Uncertainty-aware estimation, Resilient control systems, Secure control, Numerical simulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses the multiplicative-noise control design framework in order to control an uncertain system using output measurement feedback and monitor for excessive output residuals (anomaly detection).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

State estimators are crucial components of anomaly detectors that are used to monitor cyber-physical systems. Many frequently-used state estimators are susceptible to model risk as they rely critically on the availability of an accurate state-space model. Modeling errors make it more difficult to distinguish whether deviations from expected behavior are due to anomalies or simply a lack of knowledge about the system dynamics. In this research, we account for model uncertainty through a multiplicative noise framework. Specifically, we propose to use the multiplicative noise LQG based compensator in this setting to hedge against the model uncertainty risk. The size of the residual from the estimator can then be compared against a threshold to detect anomalies. Finally, the proposed detector is validated using numerical simulations. Extension of state-of-the-art anomaly detection in cyber-physical systems to handle model uncertainty represents the main novel contribution of the present work.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Cyber-Physical Systems (CPS) are physical processes that are tightly integrated with computation and communication systems for monitoring and control. Though advances in CPS design has equipped them with adaptability, resiliency, safety, and security features that exceed the simple embedded systems of the past, it often leaves open several points for attackers to strike. CPS security problems have attracted the attention of researchers worldwide recently; some state-of-the-art anomaly detection algorithms can be found.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common practice is to model a CPS as either a deterministic system or a stochastic system with additive Gaussian uncertainties. Motivated by the recent developments in distributionally robust optimization (DRO) techniques, authors in have developed DRO anomaly detectors that remove assumptions on specific functional forms of the uncertainties in the stochastic CPS model. On the other hand, it is a common practice to assume that the true CPS dynamics are known exactly. Unfortunately, modeling and sampling errors are inherent and significant in working with real systems due to nonlinearities, learned (system identification, machine learning) models, adaptive models, or simply due to changing environmental conditions or aging. A multiplicative noise framework for capturing model uncertainty offers several compelling advantages over additive noise models. It provides a statistical description of the uncertainty that depends on the control input and state. Using a multiplicative noise model, however, requires new tools to build and tune anomaly detectors that accommodate the more general functional form of the model.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

State estimation is a crucial component in any model-based anomaly detector design, which depends on a state-space model for the system dynamics. This dependency causes limitations on the usage of the classical Kalman filter as it critically relies on the availability of an accurate state-space model, making it susceptible to model risk. Robust Kalman filtering with additive uncertainties was explored, where the uncertain joint distribution of the states and outputs was accounted. Another robust Kalman filter design was developed using a $\tau$-divergence based family of distributions. In, a Wasserstein distributionally robust Kalman filter (W-DR-KF) was developed to account for distributional uncertainty. However, a procedure for jointly computing a pair of state estimator and feedback gain to guarantee stability in this setting remains unexplored.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although stochastic modeling of CPS with additive uncertainty is well studied, there are no works to the best of our knowledge which have considered both multiplicative and additive noises together in the CPS security literature. The evolution of non-Gaussian state distributions under the effect of multiplicative noise invalidates use of the standard Kalman filter, as the separation principle available in linear quadratic Gaussian (LQG) setting in no longer holds. Though considered both multiplicative and additive noises in an optimal control setting, a restrictive Gaussian assumption was imposed on the uncertainties. The approach in this paper builds on the foundation established, where the multiplicative noise-driven LQG (MLQG) problem was solved by posing a set of coupled algebraic Riccati equations, from which the optimal linear output feedback controller and estimator gains were jointly computed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Contributions:* This paper is part of our ongoing work to leverage powerful results in control theory and distributionally robust optimization to design robust anomaly detectors. Specifically, the detector threshold corresponding to a desired false alarm rate in the setting considered in this paper was computed through the moment-based approaches explained. In prior work we addressed detectors robust to non-Gaussian additive noise. In this work,

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design an anomaly detector for stochastic linear cyber-physical systems that is robust to modeling errors. To our knowledge, this is the first paper to consider tuning an anomaly detector for a system model that incorporates model uncertainty. We propose a multiplicative noise framework and integrate the MLQG compensator to compute the residual.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate our proposed approach using numerical simulations and show that multiplicative noises result in greater anomaly detector thresholds as long as mean square compensatability conditions are satisfied.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. In §II, the problem of monitoring an uncertain CPS with model uncertainty is formulated. Then, the multiplicative noise driven LQG compensator is discussed in §III. Subsequently, the anomaly detector design is presented in §IV. The proposed idea is then demonstrated using a numerical simulation in §V. Finally, the paper is closed in §VI along with directions for future research.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Uncertain CPS Model", "weight": 1.0} -->

Here, $x_{k} \in {\mathbb{R}}^{n}$, $u_{k} \in {\mathbb{R}}^{m}$, and $y_{k} \in {\mathbb{R}}^{p}$ are the system state, control input, and output at time $k$. The next-state $x_{k + 1} \in {\mathbb{R}}^{n}$ is a random linear combination of the current state and process noise $w_{k}$, which is a zero-mean white noise process. Similarly, the output $y_{k} \in {\mathbb{R}}^{p}$ is a random linear combination of the states and the sensor noise $v_{k}$, which is a zero-mean white noise process. The initial state is a random variable $x_{0} \sim {{\mathbb{P}}_{x_{0}}{(0,\Sigma_{x_{0}})}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Uncertain CPS Model", "weight": 1.0} -->

The system matrices are decomposed as

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Review of Concepts", "weight": 1.0} -->

Here, we re-state some definitions from on the mean squared versions of stabilizability, detectability and the resulting compensatability of systems given by and.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Review of Concepts", "weight": 1.0} -->

Definition 2: The system in is *mean-square stabilizable* if there exists a control gain matrix $K \in {\mathbb{R}}^{m \times n}$ such that using controls $u_{k} = {Kx_{k}}$ makes mean-square stable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Review of Concepts", "weight": 1.0} -->

Definition 3: The system in and is *mean-square compensatable* if there exist control and filter gain matrices $K \in {\mathbb{R}}^{m \times n}$ and $L \in {\mathbb{R}}^{n \times p}$ such that the system

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Review of Concepts", "weight": 1.0} -->

The system given by and is *mean-square compensatable*.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Review of Concepts", "weight": 1.0} -->

The optimal state estimator at any time $k$ given and is an affine^22^2It is possible to design a nonlinear state estimator to outperform a given affine estimator in this setting. However, it is out of the scope of this paper. function of the output $y_{k}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Under the above assumptions for a given stochastic CPS model specified by obtain residual data from an appropriate state estimator module that accounts for both multiplicative and additive noises, and subsequently design an anomaly detector threshold such that the worst case false alarm rate does not exceed a desired value.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Residuals via Multiplicative Noise LQG", "weight": 1.0} -->

Due to the multiplicative noises in and, the state distribution will be non-Gaussian even when all primitive noise distributions are Gaussian. Further, the classical separation principle from the additive noise setting does not hold in presence of multiplicative noises. This necessitates a framework where the optimal controller and the estimator gains are computed *jointly*. Here, we elaborate on obtaining the residual from CPS using the multiplicative noise-driven LQG and show that the residual covariance is a function of both additive and multiplicative noise covariance matrices.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Designing Multiplicative Noise-Driven LQG", "weight": 1.0} -->

Under both multiplicative and additive noises in the system, the optimal linear output feedback controller can be exactly computed through the combination of a multiplicative noise KF with a multiplicative noise LQR as described.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Designing Multiplicative Noise-Driven LQG", "weight": 1.0} -->

where for notation simplicity, we denote

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Designing Multiplicative Noise-Driven LQG", "weight": 1.0} -->

Then, the associated optimal controller and estimator gains $(K,L)$ are given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Designing Multiplicative Noise-Driven LQG", "weight": 1.0} -->

Finally, the optimal linear compensator is

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Designing Multiplicative Noise-Driven LQG", "weight": 1.0} -->

It is necessary to account for the multiplicative noise to achieve the minimum quadratic cost; furthermore, it is straightforward to find systems in and which are *mean-square unstable* when controlled by (multiplicative-noise-ignorant) LQG, meaning that it is necessary to account for multiplicative noise to achieve mean-square stability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

We define the estimation error as $e_{k} = {x_{k} - {\hat{x}}_{k}}$. Then the estimation error evolves as follows

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

It is evident from above that estimation error is a function of the multiplicative noise terms. We now elaborate how to obtain the residual signal required for anomaly detection. Define the residual $r_{k} \in {\mathbb{R}}^{p}$ as

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

Then, $r_{k}$ is not necessarily Gaussian due to the multiplicative noise and has mean ${{\mathbb{E}}{\lbrack r_{k}\rbrack}} = {\overline{C}{\mathbb{E}}{\lbrack e_{k}\rbrack}}$ (it becomes zero mean ${\forall k} \geq 0$ if $e_{0} = 0$) with raw second moment matrix whose vectorized form is given by

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

To compute the steady state raw second moments of the residual $r_{k}$, we define

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

Then, it is straight forward to see that $\mathcal{X}_{k}$ evolves as follows

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

where the matrix $H$ in gathers all the resulting coefficients obtained while expanding the entries of the vector $\mathcal{X}_{k}$. The algebra resulting in the following expression of $H$ is available in the appendix of. Since the optimal gain matrices $K,L$ achieve mean-square compensation of the system and, the covariance of the estimation error will have a steady state value. Since by assumption, $\overline{A} - {L\overline{C}}$ is Schur stable, we see that ${{\mathbb{E}}{\lbrack e_{k}\rbrack}}\rightarrow 0$ as $k\rightarrow\infty$ regardless of the initial state-residual $e_{0}$ which in turn results in ${{\mathbb{E}}{\lbrack r_{k}\rbrack}}\rightarrow 0$ as $k\rightarrow\infty$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

This amounts to solving a (generalized) Lyapunov equation. Such an equation can be solved more efficiently by specialized solvers which do not require the inverse to be computed explicitly; for simplicity we present the equation and its solution in this form. However, the Schur stability of the matrix $H$ subject to the mean-square compensation achieved by the matrices $(K,L)$ determines whether the resulting $\mathcal{X}_{\infty}$ (which exists no matter whatever approach is used to compute it) can be employed to compute the steady state residual moments. For instance, in a strong multiplicative noise setting, the matrix $H$ defined using $(K,L)$ matrices that do not achieve mean-square compensation will *not* be Schur stable and the resulting $\mathcal{X}_{\infty}$ cannot be used meaning that steady state $\Sigma_{r}$ does not exist. Having obtained a valid $\mathcal{X}_{\infty}$, the steady state second moments of the state- and output-residuals can then be computed as

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Residual from Multiplicative Noise LQG", "weight": 1.0} -->

Finally, using the matrix reshaping operator $\text{mat}{( \cdot )}$, we retrieve the steady state $\Sigma_{r}$ as follows

<!-- chunk {"id": "body-0034", "role": "body", "section": "Anomaly Detector Design with Residual from MLQG Compensation", "weight": 1.0} -->

We now present how to analyze the residual obtained from the MLQG compensator and elaborate the procedure to construct the corresponding anomaly detector threshold in this section. Note that the covariance of the residual computed through is a function of covariance matrices of both the additive and multiplicative noises. This is in sharp contrast to the case, where the residual covariance was just a function of the additive noise covariance. Further, to account for the changes in the covariance of the residual, we form a quadratic distance measure as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Anomaly Detector Design with Residual from MLQG Compensation", "weight": 1.0} -->

This implies that (IV) is applicable only when mean-square compensation is achieved through properly designed $(K,L)$ matrix pair as the steady state $\Sigma_{r}$ is guaranteed to exist in that case. Then, for a given $q_{k}$ from and a threshold $\alpha \in {\mathbb{R}}_{> 0}$ corresponding to a desired false alarm rate $\mathcal{F}$, the anomaly detector can be designed such that alarm time(s) $k^{\star} \in {\mathbb{N}}$ are produced according to the following rules

<!-- chunk {"id": "body-0036", "role": "body", "section": "Anomaly Detector Design with Residual from MLQG Compensation", "weight": 1.0} -->

If ${\mathbb{P}}_{r_{k}}$ was Gaussian, then $q_{k}$ would follow the chi-squared distribution, meaning that for a given tail probability defined using $\mathcal{F}$, the chi-squared detector described as in can be used to obtain the required detector threshold. However, in our setting due to the multiplicative noises, ${\mathbb{P}}_{r_{k}}$ is *non-Gaussian* and thereby the chi-squared detector is *not* appropriate. We instead utilize a moment-based approach for constructing the threshold. We propose to use the higher-order moment based anomaly detector design proposed in to design the detector threshold in this setting.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Anomaly Detector Design with Residual from MLQG Compensation", "weight": 1.0} -->

The residual $q_{k}$ is collected for a sufficiently long period of time to form the $s$-moments based ambiguity set $\mathcal{P}_{q}^{s}:=\left\{ {\mathbb{P}}_{q}\mid{{{\mathbb{E}}{\lbrack q_{k}^{s}\rbrack}} = M_{q}^{s}} \right\}$. The optimal threshold $\alpha_{q,s}^{\star}$^33^3The two subscripts $q,s$ in $\alpha_{q,s}^{\star}$ denote the random variable and the number of moments considered respectively. satisfying

<!-- chunk {"id": "body-0038", "role": "body", "section": "Anomaly Detector Design with Residual from MLQG Compensation", "weight": 1.0} -->

can then be obtained by directly invoking Theorem 4 in corresponding to a given desired false alarm rate $\mathcal{F}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We consider an inverted pendulum with a torque-producing actuator whose dynamics have been linearized about the vertical equilibrium. That is, the pendulum of mass $m$ is suspended by a mass-less rod of length $l$ and the angle $\theta$ is measured from the downward vertical with positive counter clockwise direction. The corresponding nonlinear differential equation of the pendulum mass is

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

where $m_{c} = {- \frac{g}{l}}$ denotes the uncertain mass constant. Let us denote the state vector by $x = \begin{bmatrix}
\end{bmatrix} = \begin{bmatrix}
\theta & \overset{˙}{\theta}
\end{bmatrix}$ and the torque input by $u = \tau$. Then, the corresponding discrete time dynamics obtained through the forward Euler discretization of the linearized dynamics of around the equilibrium point $\overset{\sim}{x} = {(\pi,0)}$ with step size $\Deltat$ is

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Uncertainty on the mass constant $m_{c}$ corresponds to uncertainty on the matrix A. We consider an example where the true mass constant is $m_{c}$ = 10, but the nominal model underestimates it as $m_{c} = 5$. We take a step size ${\Deltat} = 0.1$. At discrete time instances, the sensor returns a noisy measurement of the angular position of pendulum. Hence the corresponding linearized noisy output model is,

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Both $w_{k}$ and $v_{k}$ are sampled from the multivariate Laplacian (which has heavier tails than Gaussian with same mean and covariance) with zero-mean and covariance $\Sigma_{w} = {2I_{n}}$, $\Sigma_{v} = {2I_{p}}$ respectively. The state and control penalty matrices are ${Q = I_{n}},{R = I_{m}}$ respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The multiplicative noise was considered to exist both in the $A$ and $C$ matrices, with the direction matrices being $\mathcal{A}_{1} = \begin{bmatrix}
\end{bmatrix}$ and $\mathcal{C}_{1} = \begin{bmatrix}
\end{bmatrix}$ with the multiplicative noise variances ${\gamma_{k,1} \sim {\mathcal{N}{(0,\sigma_{a,1}^{2})}}},{\kappa_{k,1} \sim {\mathcal{N}{(0,\sigma_{c,1}^{2})}}}$ respectively. The non-Gaussian additive primitive noises $w_{k},v_{k}$ along with these multiplicative noises render the traditional chi-squared detector to be ineffective as the system states will evolve to be *non-Gaussian* for all $t > 0$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Through simulation, we collected the quadratic distance measure $q_{k}$ data for $T = 10^{7}$ time steps for the above system with multiplicative noises under two different settings namely, 1) using the standard LQG, and 2) using multiplicative noise-driven LQG compensators. The $q_{k}$ data was then used to tune the anomaly detector for a desired false alarm rate of $\mathcal{F} = {5\%}$ using Theorem 4 in with $s = 4$ moments in and along with a bisection tolerance of $\epsilon = 10^{- 4}$. The resulting moment bound problem was solved using the SOSToolbox on MATLAB with the SeDuMi solver. The code is made publicly available at

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A LQG & MLQG with Low Multiplicative Noises", "weight": 1.0} -->

When the system was simulated with low multiplicative noise variances $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} \leq 0.10$, the resulting $(K,L)$ matrix pair from both the LQG and the MLQG compensators had similar values and the anomaly detectors from both compensators had similar good performances. However, the performance of MLQG started getting better with $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} > 0.10$ and the results with $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} = 0.06$ are shown in Figure 2. The histograms of the $q_{k}$ data using the MLQG and LQG estimators are shown in red and cyan colors respectively.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A LQG & MLQG with Low Multiplicative Noises", "weight": 1.0} -->

The mean-square compensation of the MLQG compensator was verified via the convergence of the coupled Riccati equations and subsequently the corresponding collected $q_{k}$ data resulted in an optimal detector threshold $\alpha_{q,4}^{\star} = 8.247$ with false alarm rate being $0.89\%$. Similarly, when the $q_{k}$ data collected from the standard LQG was evaluated against a similarly computed threshold $\alpha_{q,4}^{\star} = 8.422$, it resulted in $0.86\%$ false alarms. Though both MLQG and LQG achieve mean-square compensation at a lower noise setting, the MLQG results in a tighter threshold than the LQG.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A LQG & MLQG with Low Multiplicative Noises", "weight": 1.0} -->

Further, the resulting $H$ matrix from LQG compensator *ceased* to be Schur stable for $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} > 0.11$ agreeing with results in Table I. Supposedly, if we used the unstable $H$ matrix in the LQG case, it resulted in ${\hat{\mathbb{E}}{\lbrack q_{k}\rbrack}}\rightarrow\infty$ when the variances became stronger and thereby restricted us from using even the simplest Markov bound in this case to obtain the detector threshold.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Effect of Multiplicative Noise Variance on the Worst Case False Alarm Rate", "weight": 1.0} -->

Here, we show how the variances $\sigma_{a,1}^{2},\sigma_{c,1}^{2}$ of the multiplicative noises $\gamma_{k,1},\kappa_{k,1}$ respectively affect the resulting anomaly detector's worst case false alarm rate. Starting from $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} = 0.15$, we simulated the system by increasing the variances and the results are in Table II. It is evident that MLQG compensator was capable of mean-square compensate the system with increasing covariances by resulting in finite mean (equal to 1 and thereby agreeing with (IV)). Starting from $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} \geq 0.45$, numerical issues started accompanying the threshold calculations due to exploding values of the moments (can be addressed using orthogonal basis such as the Legendre polynomial basis to provide numerical stability).

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Effect of Multiplicative Noise Variance on the Worst Case False Alarm Rate", "weight": 1.0} -->

Specifically, when the variances were increased beyond $\sigma_{a,1}^{2} = \sigma_{c,1}^{2} \geq 3.77$, the coupled Riccatti equations corresponding to the MLQG stopped converging as mean-square compensation was lost for such higher variance multiplicative noises. The effect of increasing variance also affected the resulting false alarm rates when the residuals from the MLQG compensator was compared against its respective threshold. The resulting optimal threshold $\alpha_{q,4}^{\star}$ increased when the multiplicative noise variances increased. For this reason, in this problem setting the false alarm rate of MLQG happened to decrease with increased multiplicative noise variance; there is a nontrivial relation between the multiplicative noise variances and the threshold designed by the detection scheme, which depends e.g. on the coupled Riccati equation solution.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Effect of Multiplicative Noise Variance on the Worst Case False Alarm Rate", "weight": 1.0} -->

As shown in Table II, the MLQG with finite set of $s = 4$ empirical moments starting from $\hat{\mathbb{E}}{\lbrack q_{k}\rbrack}$ guaranteed that the resulting worst case false alarm rate are always upper bounded by the desired value of $\mathcal{F} = {5\%}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

An extension of the state-of-the-art anomaly detection algorithms for CPS with modeling errors via the multiplicative noise framework was discussed in this paper. The multiplicative noise-driven LQG being a robust state estimator was used to hedge against the model risk to construct the state estimate. The proposed method was demonstrated using a numerical simulation. Future work seeks to investigate the setting where the multiplicative noise distributions are unknown and to obtain online estimates of the system dynamics through system identification technique combined with the above compensator for implementing data-driven distributionally robust anomaly detection for vulnerable CPS.
