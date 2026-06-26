<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning

Topics include Prediction, Dynamic mode decomposition.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Tackles the problem of data-driven motion prediction by using a special kind of Dynamic Mode Decomposition (DMD), which comes from the Koopman operator theory, to learn a model of the agent motion. The model also produces uncertainty estimates, which is useful for downstream risk-aware planning & control. This paper combines a lot of smaller techniques (Hankel-DMD, Cadzow projection, Singular Value Hard Thresholding (SVHT), etc.) together into a rather intricate bells-and-whistles learner, but that in itself is nice as it provides the reader some clues into those techniques.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous systems often must predict the motions of nearby agents from partial and noisy data. This paper asks and answers the question: "can we learn, in real-time, a nonlinear predictive model of another agent's motions?" Our online framework denoises and forecasts such dynamics using a modified sliding-window Hankel Dynamic Mode Decomposition (Hankel-DMD). Partial noisy measurements are embedded into a Hankel matrix, while an associated Page matrix enables singular-value hard thresholding (SVHT) to estimate the effective rank. A Cadzow projection enforces structured low-rank consistency, yielding a denoised trajectory and local noise variance estimates. From this representation, a time-varying Hankel-DMD lifted linear predictor is constructed for multi-step forecasts. The residual analysis provides variance-tracking signals that can support downstream estimators and risk-aware planning. We validate the approach in simulation under Gaussian and heavy-tailed noise, and experimentally on a dynamic crane testbed. Results show that the method achieves stable variance-aware denoising and short-horizon prediction suitable for integration into real-time control frameworks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robotic systems often operate in the presence of other dynamic and non-coordinated agents. For example, autonomous cars must navigate around vehicles, pedestrians, and cyclists. In autonomous drone racing, drones must avoid crashing into other drones on the racecourse and in maritime robotics, a shipboard robotic arm or autonomous crane must plan for the payload's motion while compensating for the ship's sea-induced oscillations. In such settings, the other agent's dynamics and intentions are typically unknown, while onboard sensing provides noisy, partial observations of the agent motions. Safe, efficient behavior therefore hinges on accurate short-horizon prediction of agent motion under uncertainty to enable collision-free planning and real-time control. Thus, this paper introduces a data-driven framework for real-time learning and short-horizon prediction from noisy, partial observations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contribution", "weight": 1.0} -->

We propose an adaptive, denoising, sliding-window Hankel--DMD framework for real-time prediction from noisy partial measurements. At each time step, a finite data buffer fits a local model, balancing responsiveness to non-stationary behavior with enough samples for reliability. We first denoise via Cadzow's low-rank projection, with rank $\widehat{r}$ chosen by Singular Value Hard Thresholding (SVHT) on a Page matrix embedding. We prove that, under mild conditions, Page and Hankel matrices have the same finite-sample rank, so the SVHT rank transfers to the Hankel matrix for Cadzow denoising. The resulting denoised Hankel matrices yield a sequence of local models and noise-variance estimates for uncertainty-aware planning. We validate the framework in both simulation and hardware experiments under Gaussian and non-Gaussian correlated heavy-tailed noise. We show that the framework offers robust denoised predictions suitable for real-time control and planning tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Consider a robot that operates in the vicinity of another moving entity $\mathcal{O}$ whose behavior and dynamics are unknown. The robot's onboard sensors detect $\mathcal{O}$ and provide noisy, partial measurements of the obstacle state, denoted by $x_{t}\in\mathbb{R}^{n_{x}}$, which are sampled at a uniform interval $\Delta t\geq 0$, and capture kinematic quantities such as velocities or angular rates. While $x_{t}$ may not directly encode full Cartesian position, it carries sufficient temporal information to enable short-horizon motion prediction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The motion of $\mathcal{O}$ is governed by a discrete-time dynamical system with latent (unobserved) variables and unmeasured control inputs in the form: $z_{t+1}=\hat{f}(z_{t},u_{t})$ where $z_{t}$ denotes the state, which may include latent (unobserved) variables and $u_{t}$ an input from an unknown policy $u_{t}=c(z_{t})$. Under these assumptions, we have an autonomous system where measurement noise $\eta_{t}\in\mathbb{R}^{n_{x}}$ has an unknown distribution, and $C$ is the state-output map. This discrete time model generally arises from discretization of a continuous-time system. We maintain a sliding buffer of $N$ recent measurements $\mathcal{B}_{t}=\{x_{t-N+1},\ldots,x_{t}\}$ for online processing.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Problem Statement: Given streaming noisy observations $\{x_{t}\}$ from a single trajectory and a sliding data buffer of fixed length $N$, construct, in real time, a tractable and adaptive local model. This model generates multi-step forecasts $\{\bar{x}_{t+1},\ldots,\bar{x}_{t+N_{h}}\}$ over a prediction horizon $N_{h}\in\mathbb{N}$, suitable for downstream planning and control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Hankel and Page Matrices", "weight": 1.0} -->

Guided by Takens' delay-embedding theorem (the dynamics of a system can be reconstructed from delay-coordinate maps of a single observable when the embedding dimension is sufficiently large), we apply delay embedding to the obstacle measurements to extract informative information about its dynamics. Given a sequence of $N$ measurements $\{x_{i-N+1},\ldots,x_{i}\}\subset\mathbb{R}^{n_{x}}$, we denote the associated (block) *Hankel* matrix $H^{\,L}_{i-N+1:i}\in\mathbb{R}^{(Ln_{x})\times(N-L+1)}$: The (block) *Page* ^11^1For $n_{x}=1$, the matrices $H^{L}_{i-N+1:i}$ and $P^{L}_{i-N+1:i}$ take Hankel and Page forms, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Hankel and Page Matrices", "weight": 1.0} -->

For $n_{x}>1$, they become block Hankel and block Page. For simplicity, we refer to both cases as Hankel and Page structures.matrix $P^{\,L}_{i-N+1:i}\in\mathbb{R}^{(Ln_{x})\times m}$ partitions the same sequence into $m$ non-overlapping blocks of length $L$ (with $m=N/L$)^22^2Note that, unlike the Hankel matrix, in the Page matrix, the buffer length $N$ must be a multiple of the embedding window length $L$.:

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Hankel-DMD", "weight": 1.0} -->

We review a variant of Hankel-DMD (cf.) suitable for our problem. It uses delay embedding on the measurements of obstacle's observables (II). Given a measurement sequence $\{x_{0},x_{1},\ldots,x_{n}\}$, form the one step shifted Hankel matrices $H_{0:n-1}^{L}$ and $H_{1:n}^{L}$ according to the Eq.. Note that the columns of $H_{1:n}^{L}$ are shifted one time step forward from the columns of $H_{0:n-1}^{L}$. To estimate the one-step dynamic prediction propagator, $A^{*}$, Hankel-DMD relies on the following least Frobenius-norm problem, The closed form solution for $A^{*}$ is Under standard assumptions of ergodicity and noise-free observables, Hankel-DMD can be used as a finite-dimensional approximation of the Koopman operator via delay embeddings.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Hankel-DMD", "weight": 1.0} -->

Our goal is to tackle the real-world cases where these assumptions do not hold.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-C Cadzow Algorithm for Denoising", "weight": 1.0} -->

Here, we review a variant of Cadzow's algorithm for denoising Hankel matrices. In the approximately linear lifted dynamics (e.g., Koopman-based approximations), noise-free data resides on a low-dimensional vector space. Hence, for a sufficiently large delay embedding window $L$, the noise-free Hankel trajectory matrix becomes low rank. However, with measurement noise, the observed Hankel matrix is generally full rank. Let Hankel matrix $H^{L}\in\real^{(L\,n_{x})\times(N-L+1)}$ be constructed from $N$ consecutive noisy measurements with embedding window $L$. Decompose $H^{L}$ as $H^{L}\;=\;\widehat{H}^{L}\;+\;\Delta$ with where $\Delta$ denotes measurement noise and $\widehat{H}^{\,L}$ is the noise-free Hankel matrix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Cadzow Algorithm for Denoising", "weight": 1.0} -->

The goal is to recover the (unknown) noise-free, low-rank Hankel matrix $\widehat{H}^{\,L}$ from $H^{\,L}$. Cadzow's algorithm aims for this objective by alternating projections of $H^{L}$ on the set of matrices with rank of at most $r$ with projections of the result back onto the set of Hankel matrices.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Cadzow Algorithm for Denoising", "weight": 1.0} -->

Given a target rank $r$, define the projection map $\Pi_{r}$ onto the set of rank-$\leq r$ matrices as where $H=U\Sigma V^{\top}$ is the SVD and $\Sigma_{r}$ is created by keeping the top $r$ singular values in $\Sigma$ while setting the rest to zero. The closed-form solution of is a direct consequence of Eckart--Young--Mirsky theorem. Similarly, we define the projection map $\Pi_{\mathsf{H}}$ onto the set of Hankel matrices as Interestingly, the optimization problem has a closed-form solution which can be calculated by replacing the members of each anti-diagonal of $M$ with their average. The procedure is as follows: decompose $M$ into $L$ by $N-L+1$ blocks similarly to the Hankel matrix^33^3Note that each block is a column vector with $n_{x}$ rows similarly to Eq.. And denote by $M_{i,j}$ the $ij$th block.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Cadzow Algorithm for Denoising", "weight": 1.0} -->

For each anti-diagonal offset $d=0,\ldots,N-1$, define: where $s_{d}\;=\;|\mathcal{I}_{d}|$ is number of elements in $\mathcal{I}_{d}$. Then, the anti-diagonal averaging can be computed as for $1\leq\ell\leq L,\;1\leq m\leq N{-}L{+}1$. The Cadzow algorithm successively applies the projections $\Pi_{r}$ and $\Pi_{\mathsf{H}}$ so that the sequence converges to a Hankel matrix, $\hat{H}^{L}$, that is approximately of rank $r$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Cadzow Algorithm for Denoising", "weight": 1.0} -->

Notably, since projections $\Pi_{r}$ and $\Pi_{\mathsf{H}}$ can be computed in closed form, the Cadzow algorithm is an attractive choice for real-time denoising, as only a few iterations are sufficient to yield a reasonable signal-to-noise ratio.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-D Singular Value Hard Thresholding (SVHT)", "weight": 1.0} -->

Here we review a variant of Gavish and Donoho's result. Consider a sequence (indexed by $a$) of noisy matrices $Y_{a}=X_{a}+Z_{a}/\sqrt{n_{a}}$ where $Y_{a}\in\mathbb{R}^{m_{a}\times n_{a}}$ denotes a noisy matrix, $X_{a}$ the \"true\" low-rank matrix, and $Z_{a}$ denotes the noise matrix whose entries are i.i.d. zero-mean, unit-variance entries with finite fourth moment.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D Singular Value Hard Thresholding (SVHT)", "weight": 1.0} -->

Gavish and Donoho showed that the Asymptotic Mean Squared Error (AMSE)-optimal threshold for the data singular values depends only on the matrix aspect ratio $\beta$ via a constant $\lambda^{\star}(\beta)$: For the noise standard deviation $\sigma$, the optimal threshold is: When $\sigma$ is unknown, the optimal threshold can be estimated using a data-driven approach through the Marchenko--Pastur (MP) law, which gives the limiting eigenvalue distribution of $(1/n_{a})\,{Z_{a}}{Z_{a}}^{\top}$ as $m_{a}/n_{a}\to\beta$: with $p_{\beta}(\delta)=0$ outside $[\delta_{-},\delta_{+}]$. The median of the MP distribution, denoted by $\mu_{\beta}$, depends only on $\beta$ and provides a normalization for estimating the noise level $\sigma$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-D Singular Value Hard Thresholding (SVHT)", "weight": 1.0} -->

Taking $\varsigma_{\mathrm{med}}$ as the median of the observed singular values, the data-driven AMSE--optimal threshold can thus be estimated as: which remains asymptotically optimal under general white noise (i.i.d., zero mean, unit variance, finite fourth moment) with the same risk as in the Gaussian case \[14, Sec. VI\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Adaptive Hankel-DMD for Noisy Data", "weight": 1.0} -->

We now address the problem outlined in Sec. II. To enable real-time obstacle dynamics learning and motion prediction, we consider the use of Hankel-DMD (cf. Sec. III-B). However, applying Hankel-DMD in real-time robotics applications presents two key challenges: Sensor noise: sensor signals are typically noisy, which contaminates matrices $H_{0:n-1}^{L}$ and $H_{1:n}^{L}$. In least-squares schemes such as, noise in both data matrices leads to biased or inconsistent estimators.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Adaptive Hankel-DMD for Noisy Data", "weight": 1.0} -->

Ergodicity and long trajectory data requirements: as noted in Sec. III-B, one must assume ergodicity and long data sequences to connect Hankel-DMD and the Koopman operator. Such assumptions rarely hold in robotics applications.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Adaptive Hankel-DMD for Noisy Data", "weight": 1.0} -->

To tackle the noise issue, we introduce a Hankel matrix denoising scheme. We then propose an adaptive sliding-window variation of Hankel-DMD that continually updates the model. This approach ensures that the predictive model remains accurate as the object's state evolves over time.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Denoising Hankel Matrices", "weight": 1.0} -->

Consider obstacle output measurements $\mathcal{B}_{t}=\{x_{t-N+1},\ldots,x_{t}\}$ for buffer size $N$, collected up to time $t$. We construct a Hankel matrix $H^{\,L}_{t-N+1:t}$ from $\mathcal{B}$ according to Eq.. Since the measurements are noisy, we seek to denoise the Hankel matrix $H^{\,L}_{t-N+1:t}$ via Cadzow's algorithm, as described in Sec. III-C. A key step in this algorithm is the low-rank projection $\Pi_{r}$ in Eq., which requires knowledge of the effective rank $r$ of the noise-free Hankel matrix. In practice, this typically unknown rank must be estimated. An rank estimat error can cause over-smoothing (if underestimated) or noise amplification (if overestimated).

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Denoising Hankel Matrices", "weight": 1.0} -->

To avoid these problems, we adopt a principled, data-driven rank selection strategy based on Singular Value Hard Thresholding (SVHT) (Sec. III-D ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")). However, the SVHT framework assumes i.i.d. noise, an assumption that is violated in Hankel matrices due to repeated entries. To address this, we employ Page matrices (Eq. ), whose partition of the measurement buffer into non-overlapping blocks avoids correlation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A1 Step I: Page-Hankel Rank Transfer", "weight": 1.0} -->

As a first step toward estimating the rank of the noise-free Hankel matrix using SVHT on Page matrices, we show that, under mild conditions, the Page and Hankel embeddings of the *same* noise-free measurement buffer share the same rank.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A2 Rank Estimation using SVHT", "weight": 1.0} -->

To apply the SVHT (cf. Sec. III-D ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")) on the Page matrix, the number of rows in the matrix should be less than or equal to the number of columns. Therefore, for the rest of the paper, we consider the buffer length $N=mLn_{x}$, with $m\geq Ln_{x}$. Note that this choice already satisfies the size condition in Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning").

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A2 Rank Estimation using SVHT", "weight": 1.0} -->

To construct the Page matrix $P^{\,L}_{t-N+1:t}\in\real^{Ln_{x}\times m}$ from the same data sequence used in $H^{\,L}_{t-N+1:t}$. By applying the SVHT formula in Eq.(11 ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")), on the Page matrix, we can estimate the singular value threshold $\tau^{*}$ and approximate the effective rank of $P^{\,L}_{t-N+1:t}$ as where $\{\varsigma_{i}\}_{i=1}^{Ln_{x}}$ are the singular values of $P^{\,L}_{t-N+1:t}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A2 Rank Estimation using SVHT", "weight": 1.0} -->

It is important to note that the rank $\widehat{r}$ estimated via Page SVHT is not fixed but evolves as the sliding window advances. As the buffer shifts, the local data distribution changes, and the singular spectrum captures the instantaneous richness of the underlying dynamics. Consequently, small fluctuations or occasional variations in $\widehat{r}$ are to be expected. Far from being a drawback, this adaptivity ensures that the thresholding remains sensitive to regime shifts and transient behaviors, ultimately producing more reliable models when the system exhibits greater dynamical complexity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A2 Rank Estimation using SVHT", "weight": 1.0} -->

Sec. III-D ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning") also yields a conservative local noise--variance estimate. Singular values below the cutoff in Eq. (11 ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")) are treated as noise, while those above define the rank via Eq.. Let $\varsigma_{\mathrm{med}}$ be the median singular value of the *Page* matrix with aspect ratio $\beta$ and $m$ columns, and let $\mu_{\beta}$ denote the median of the Marchenko--Pastur law at aspect ratio $\beta$. Then the noise variance $\widehat{\sigma}^{2}$ can be conservatively estimated as $\widehat{\sigma}^{2}\approx\varsigma_{\mathrm{med}}^{2}/\mu_{\beta}\,m$. Under the assumption of i.i.d.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A2 Rank Estimation using SVHT", "weight": 1.0} -->

sensor noise, we approximate the delay--state noise covariance as $\widehat{\nu}\approx\widehat{\sigma}^{2}I_{Ln_{x}}$. This approximation treats each delay state as being perturbed by independent, isotropic noise, which is appropriate in the i.i.d. setting but may underestimate correlations in more structured noise processes. A concrete example of leveraging such variance information within a risk-aware framework is provided.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A3 Cadzow Algorithm", "weight": 1.0} -->

Now, by using the rank estimate $\hat{r}$ in Eq. and utilizing Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning"), we can finally apply the Cadzow algorithm in Sec.III-C on Hankel matrix $H^{\,L}_{t-N+1:t}$ with effective rank $\hat{r}$ until we approximate a denoised Hankel matrix which we denote by $\widehat{H}^{\,L}_{t-N+1:t}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Online Identification and Multi-Step Prediction", "weight": 1.0} -->

With the denoised Hankel matrix $\hat{H}^{\,L}_{t-N+1:t}$ obtained, we proceed to model the system dynamics using Hankel-DMD. However, as mentioned earlier, to connect the behavior of the dynamics learned by Hankel-DMD in Eqs.- to the system's global behavior via Koopman operator, one often requires assumptions of ergodicity on the system and access to very long trajectories. These assumptions rarely hold in robotics applications. To circumvent this issue, we apply an adaptive sliding window strategy to build a linear model for each buffer and update it as we receive new data.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Online Identification and Multi-Step Prediction", "weight": 1.0} -->

Formally, let $\hat{H}^{\,L}_{t-N+1:t-1}$ and $\hat{H}^{\,L}_{t-N+2:t}$ be the Hankel matrices constructed by taking the first and last $N-L$ columns of $\hat{H}^{\,L}_{t-N+1:t}$ respectively.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Online Identification and Multi-Step Prediction", "weight": 1.0} -->

We then solve a least Frobenius-norm problem similar to Eq. as: with the closed-form solution We then define the local predictor dynamics as If we initialize the system by setting $\psi_{t}$ to be equal to the last column of $\hat{H}^{\,L}_{t-N+2:t}$ (which corresponds to the denoised version of the lifted state at the current time), we can forecast the future outputs of system (II) by running the predictor and extracting the last block of the delay embedded state as where $\psi_{t}^{*}$ is set to be the last column of $\hat{H}^{\,L}_{t-N+2:t}$ and matrix $D\in\real^{n_{x}\times Ln_{x}}$ is defined as $D=[0_{n_{x}\times(L-1)n_{x}},I_{n_{x}}]$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Online Identification and Multi-Step Prediction", "weight": 1.0} -->

At the next time step, we advance the buffer to $\mathcal{B}_{t+1}=\{x_{t-N+2},\ldots,x_{t+1}\}$ and repeat the aforementioned procedure to produce a time-varying sequence of linear predictors characterized by $\{\widehat{A}_{t}\}_{t\geq N}$. These predictors are well suited for Model Predictive Control (MPC) by providing linear predictions over the planning horizon. Algorithm 1 compiles the full sliding-window procedure.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Online Identification and Multi-Step Prediction", "weight": 1.0} -->

Input: Embedding window L Buffer Length N = mLnx with m ≥ Lnx Output: Denoised Hankel Ĥt − N + 1: t L Model Ât and Forecasts {x̄t + 1, …, x̄t + Nh} Noise covariance estimate ν̂ Page & SVHT: Form Pt − N + 1: t L per Eq. Compute SVD Pt − N + 1: t L = U diag(𝜍i) V⊤. Set β = (Lnx)/m and 𝜍med = median{𝜍i} Set cutoff $\tau^{\star}=\lambda^{\star}(\beta)/{\sqrt{\mu_{\beta}}}$ via Eq. r̂ ← #{i: 𝜍i ≥ τ⋆} per Eq.)

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Online Identification and Multi-Step Prediction", "weight": 1.0} -->

Cadzow Algorithm for J Iterations: Ĥt − N + 1: t L ← [ΠH ∘ Πr]J (Ht − N + 1: t L) Hankel Partitions and Predictor at t: Prediction (Nh steps): Let ψt⋆ be the last column of Ĥt − N + 2: t L. For j = 1, 2, …, Nh, x̄t + j = D(Ât)j ψt⋆ per Eq. Noise Variance Estimation: With m Page columns and MP median μβ, set σ̂2 = 𝜍med2/(μβ m) and ν̂ = σ̂2ILnx. Slide Window: ℬt + 1 ← {xt − N + 2, …, xt + 1} and repeat –. Algorithm 1 Adaptive Sliding-Window Page–Hankel DMD Predictor

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C Comparison with Alternative Online Prediction Methods", "weight": 1.0} -->

Classical online noise filtering approaches, such as the KF and its nonlinear variants, assume parametric dynamics and structured noise models. While online Gaussian processes and neural sequence models provide strong predictive capability, they can require significant offline training and careful tuning for online deployment. In contrast, DMD and EDMD are operator-theoretic system identification methods that approximate the Koopman operator from data. These formulations do not account for measurement noise and can exhibit bias under finite, noisy datasets, particularly when nonlinear lifting is used. Although noise-aware formulations and regularized variants exist, these methods mainly improve dynamical consistency rather than provide a framework for denoising streaming measurements in finite-data regimes. our proposed method explicitly performs structured low-rank denoising prior to short-horizon prediction. Designed for finite, streaming data with limited computational budgets, the framework combines adaptive rank selection with structured matrix embeddings to enable stable real-time performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulations and Experiments", "weight": 1.0} -->

We apply Algorithm 1 to validate out framework in simulations and real-world experiments. Our evaluation examines (i) signal--to-noise (SNR) separability, (ii) noise variance estimation, and (iii) multi-step prediction accuracy. Experiments consider open-loop, short-horizon prediction to assess the accuracy, stability and noise robustness of the learned dynamics model. These properties are critical for downstream planning and control frameworks.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Simulation: Noisy Unicycle", "weight": 1.0} -->

Consider a reference unicycle model $\dot{x}=u_{1}\cos\theta,\dot{y}=u_{1}\sin\theta,\dot{\theta}=u_{2}$ which serves as a dynamic obstacle moving along a figure-eight trajectory of amplitude $a=3\,\mathrm{m}$ and period $T=40\,\mathrm{s}$. An ego agent seeks to reach its goal while avoiding collisions with the unicycle, but has access to only noisy velocity measurements of the unicycle rather than the full state. Sampling the reference trajectory at $\Delta t=0.02\,\mathrm{s}$ yields the forward velocity profile $u_{1}^{\star}(t)$. We inject sensor noise from two distributions: (i) i.i.d.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Simulation: Noisy Unicycle", "weight": 1.0} -->

Denoising results (Gaussian): Fig. 1 demonstrates that our Page-Hankel SVHT framework achieves stable recovery of the ground-truth velocity profile under Gaussian sensor noise. The denoised estimate (red, top panel) tracks the ground truth (dashed black) without visible phase lag while suppressing high-frequency artifacts that often contaminate raw measurements. Over the $160$ s trajectory, the method delivered an SNR gain of $19.2$ dB and an average noise reduction of $89.0\%$ (call-out, top-left), corresponding to nearly an order-of-magnitude improvement over baseline. The zoomed view (bottom-left) highlights that turning points and low-curvature segments, often degraded by conventional low-pass filters, were preserved, while the log-scale absolute error confirms a $10$-$100\times$ reduction in residual magnitude. These results indicate that the method can denoise aggressively without compromising structural features critical for downstream control.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Simulation: Noisy Unicycle", "weight": 1.0} -->

Denoising results (Heavy tailed, correlated noise): To probe robustness under non-Gaussian disturbances, we injected temporally correlated AR-Laplace noise (Fig. 2). Despite heavy tails and temporal correlation, we observed an SNR gain of $6.9$ dB and an average noise reduction of $54.4\%$, with no visible phase lag. While performance is lower than under Gaussian noise, as to be expected, the degradation remains gradual. Crucially, the low-rank Hankel structure proved distribution-agnostic i.e., SVHT adaptively trims singular values inflated by heavy-tailed noise requiring explicit Gaussian assumptions on the noise statistics.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Simulation: Noisy Unicycle", "weight": 1.0} -->

Comparison with Extended Kalman Filter (EKF)-based denoising: For reference, we evaluated an EKF as a denoising pipeline under the same Gaussian disturbance conditions defined in Sec. V-A. When the process and measurement covariance matrices are carefully tuned using approximate knowledge of the noise moments, the EKF achieves moderate reconstruction quality, yielding an SNR of approximately $0.6$ dB. However, even in this tuned setting the EKF exhibits a noticeable phase delay (Fig. 3, top), which increases the point-wise reconstruction error used in the SNR calculation and may be problematic for downstream control pipelines that require temporally aligned state estimates for stable feedback and prediction. In contrast, the proposed Page/Hankel-based method achieves an SNR of $19.2$ dB under the same disturbance conditions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Simulation: Noisy Unicycle", "weight": 1.0} -->

In practical robotic systems, the true measurement noise statistics are typically unknown and may vary over time. Since the EKF relies on explicit specification of these noise moments to compute the Kalman gain, its performance is sensitive to covariance mismatch. Under mild mismatch in the assumed noise statistics, reconstruction quality yields an SNR of approximately $10.0$ dB (Fig. 3, bottom). Our proposed Page/Hankel framework estimates the noise structure directly from the data through low-rank structure and adaptive SVHT thresholding, avoiding explicit noise variance specification while maintaining consistent reconstruction performance across noise regimes.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

This section experimentally validates the complete method in a setup (Fig. 4) motivated by a naval application. Currently, payloads are loaded into their silos by a ship-board crane while the ship docks in a port, where no ocean swells affect the safety of the loading process. It would be desirable to load these payloads while the ship is underway, potentially in heavy seas. In active sea states, the ship sways in response to ocean swells. Anticipating deck motion via a learned predictive model would enable the crane controller to compensate during payload delivery.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

The testbed is a scaled crane mounted on an *E2M eMove eM6-300-1500* five-DoF Stewart platform that can reproduce wave-induced ship deck motions. A VN-100 IMU measures orientation (quaternion) and angular velocity of the simulated moving base at 30 Hz. These measurements correspond to the platform (deck) motion only, which is modeled as a time-varying base motion input to the crane-payload system. Using these IMU data, the framework generates a $31$-step horizon open-loop forecast ($\approx$`<!-- -->`{=html}1.0 s) of the platform motion. Payload and crane dynamics are not directly predicted and are instead assumed to evolve downstream in response to the predicted base motion.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

This setup enables two evaluations: (i) whether the variance-stable denoising observed in simulation persists under real IMU noise and (ii) whether short-horizon sliding window Hankel-DMD predictions remain within a bounded threshold suitable for MPC integration. Fig. 5 (top) shows a representative trajectory where $N=250$ sample context buffer (gray) feeds the pipeline, generating $31$-step forecasts (red) aligned with the ground truth (dashed black). The open-loop predictor achieves an RMSE of $0.012$ m/s.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

Given a fixed error-tolerance $\varepsilon=0.04$^88^8The tolerance $\varepsilon$ is chosen based on prior operational constraints of the experimental platform. In earlier implementations using a baseline constant-velocity predictor, prediction errors up to $0.08$ m were acceptable for reliable payload insertion. We therefore set $\varepsilon=0.04$ as a conservative threshold that remains consistent with the hardware constraints., we define a violation-duration metric on the prediction error $e_{t}$ as where $N_{h}$ defines the prediction horizon, $\bar{x}_{t}$ the prediction forecast, $x_{t}$ the measured ground truth, $\Delta t$ the sample period, and $\mathbf{1}(\cdot)$ the indicator (1 if the condition holds, 0 otherwise).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

In Fig. 5 (bottom), $J_{t}=89.0$ s ($1.6\%$ of horizon^99^9The fraction of the horizon spent above threshold, $\%\text{violating}\;=\;100\times\frac{J_{t}}{T_{\mathrm{hor}}},\qquad T_{\mathrm{hor}}:=N_{h}\,\Delta t.$), certifying that prediction errors are bounded within the tolerance for $98.4\%$ of the time.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

Further investigation of Fig. 5 (top) reveals occasional transient spikes in the predicted trajectory, after which the forecasts quickly return to a nominal accuracy. These anomalies arise when the local embedding window captures a regime shift or abrupt disturbance, briefly mis-aligning the rank estimate. Importantly, such events are short-lived and self-correct as the sliding buffer refreshes, with the subsequent predictions re-stabilizing around the future measurements. This highlights both the adaptivity and the finite-sample sensitivity of the method, i.e., while transient outliers can occur, the framework consistently recovers without persistent drift.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

Fig. 6 illustrates the evolution of the eigenvalues of the learned predictors across sliding windows. As the system behavior changes along the trajectory, the models adapt accordingly, and the eigenvalues shift smoothly while consistently remaining within the unit circle, ensuring Schur stability. The gradual evolution of the spectrum highlights the stability and time-varying nature of the local Hankel-DMD models throughout the experiment.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B System Hardware and Experiments", "weight": 1.0} -->

Together, these results demonstrate that our framework not only denoises real sensor streams but also yields stable and bounded predictions that are suitable for downstream planning and control applications. A real-time demonstration of the moving-base prediction and MPC integration is shown in the supplementary video.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Parameter Sensitivity and Computational Analysis", "weight": 1.0} -->

While Sec.V-B validates hardware performance using a selected configuration of the hyper-parameters ($N=250$, $L=10$, $J=20$), we now examine the sensitivity of the prediction accuracy and computational cost to the embedding length $L$ and the number of Cadzow iterations $J$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C Parameter Sensitivity and Computational Analysis", "weight": 1.0} -->

Cadzow iterations $J$: Based on Table I, with $N=250$ and $L=10$ fixed, increasing the number of Cadzow iterations improves prediction accuracy up to $J=20$, reducing RMSE from $0.0129$ ($J=1$) to $0.0115$ ($J=20$). Beyond this point, additional iterations provide negligible accuracy gains while increasing computational cost approximately linearly. These results indicate that moderate Cadzow iterations provide a favorable trade-off between accuracy and runtime.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-C Parameter Sensitivity and Computational Analysis", "weight": 1.0} -->

Embedding length $L$: As evidenced in Table II with $N=250$ and $J=20$ fixed, the prediction accuracy improves as the $L$ increases up to an intermediate value. RMSE decreases from $0.060$ at $L=4$ to $0.0108$ at $L=12$, with a slight degradation at $L=13$. This reflects a finite-data trade-off where larger embeddings increase model expressivity but reduce the number of snapshot pairs of $N/L$, which may degrade the matrix conditioning and stability of the locally linear dynamical model. Runtime grows moderately with $L$, with the Cadzow projection constituting the dominant over the total computational time. A comprehensive ablation study analyzing the sensitivity of RMSE, Cadzow runtime, and total computation time to the hyper-parameters is summarized in the Appendix (Table III).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion And Future Work", "weight": 1.5} -->

We introduced a Page--Hankel SVHT framework for learning short-horizon predictive models of moving obstacles from noisy data streams. Simulations (Gaussian and heavy-tailed noise) showed good variance-stable, distribution-agnostic performance, and hardware tests with IMU data produce reliable forecasts that can support downstream control. Future work will explore online adaptation, tensorized delayed embeddings for multi-axis consistency, and integration within an MPC-based prediction framework.
