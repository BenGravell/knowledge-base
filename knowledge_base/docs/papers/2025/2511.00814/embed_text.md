## Introduction

Autonomous robotic systems often operate in the presence of other dynamic and non-coordinated agents. For example, autonomous cars must navigate around vehicles, pedestrians, and cyclists. In autonomous drone racing, drones must avoid crashing into other drones on the racecourse and in maritime robotics, a shipboard robotic arm or autonomous crane must plan for the payload's motion while compensating for the ship's sea-induced oscillations. In such settings, the other agent's dynamics and intentions are typically unknown, while onboard sensing provides noisy, partial observations of the agent motions. Safe, efficient behavior therefore hinges on accurate short-horizon prediction of agent motion under uncertainty to enable collision-free planning and real-time control. Thus, this paper introduces a data-driven framework for real-time learning and short-horizon prediction from noisy, partial observations.

### Related Work

Different approaches have been developed for integrating prediction and planning in dynamic environments where other agents' dynamics and intentions are unknown. Classical geometric planners such as the Velocity-Obstacle (VO) family, Reciprocal VO (RVO), Optimal Reciprocal Collision Avoidance (ORCA) and Acceleration Velocity Obstacles extensions (AVO)), embed simple relative-motion estimates to predict collisions and select controls outside forbidden sets. These methods are efficient but assume simplified behavior models and near-perfect state estimates. However, real agents often violate these assumptions. For instance, some thrown objects may be roughly ballistic, but aerodynamically complex bodies, e.g., frisbees, do not follow a simple ballistic model. Additionally, behavior-driven agents, e.g., pedestrians, require data-driven intent models to capture variability beyond constant-velocity assumptions. Lastly, the future trajectories of constraint-driven agents, e.g., autonomous vehicles, may be restricted by road geometry and traffic rules. Across all these examples, VO-style methods assume perfect knowledge of the moving agents' states and neglect measurement noise or sensing delays. This reliance on idealized assumptions highlights the gap between geometric formulations and the stochastic, nonlinear realities of robotics applications.

When other agents' dynamics are unknown, it is desirable to learn predictive models online from streaming observations. In practice, only partial and noisy measurements are available, while key latent states are unobserved, degrading forecasts and the safety of plans. Prior methods assume full-state observability for simplicity. This includes frameworks that learn dynamics directly from data *offline*, e.g., classical AutoRegressive Moving Average (ARMA) models \[26 modeling method for Gyro random noise using a Robust Kalman Filter")\], modern sequence learners such as Recurrent Neural Networks (RNNs), transformers, and tokenized representations. These off-line methods capture complex behavior but require large datasets and retraining and adapt poorly to distribution shift. *Online* variants (e.g., Kalman Filtering (KF), recursive least squares, and online Gaussian processes ) update models during deployment, but presume known or structured noise distributions.

Koopman theory is a complimentary alternative to learning these dynamic models. Formally, the Koopman operator models a nonlinear dynamical system via a *linear operator* on a vector space of functions. Since the operator acts on an infinite dimensional vector space, real-time analysis and prediction is intractable. A practical approach is to *approximate* the operator's action on a finite-dimensional subspace (which is typically of greater dimension than the state-space of the nonlinear system), enabling the use of well-developed methods from linear algebra and linear system theory. These approximations are often performed via orthogonal projections on the subspace of choice, also referred to as truncations of the operator's action. Dynamic Mode Decomposition (DMD) and its variant Extended-DMD (EDMD) are well-known examples of such projection-based algorithms. Hankel-DMD uses time-delay embedding to estimate an effective state-space dimension. Such truncated Koopman-based models offer computationally feasible approximations of nonlinear dynamics with proven utility in robotics for prediction and control. However, sensor measurements may be noisy, and since the fidelity of real-time Koopman predictors depends on data quality, noise degrades these learned models.

Existing denoising frameworks to resolve noisy measurements prior to model fitting include classical low-rank denoising techniques i.e., truncated Singular Value Decomposition (tSVD), Principal Component Analysis (PCA) and Proper Orthogonal Decomposition (POD). They provide optimal projections but rely on *ad hoc* rank selection. Structured Hankel denoising enforces temporal consistency but requires tuning and degrades under non-Gaussian noise. Scalable variants like randomized SVD improve efficiency but depend on problem-specific thresholds, while Eigensystem Realization Algorithm (ERA) and Singular Spectrum Analysis (SSA) remain sensitive to noise.

### Contribution

We propose an adaptive, denoising, sliding-window Hankel--DMD framework for real-time prediction from noisy partial measurements. At each time step, a finite data buffer fits a local model, balancing responsiveness to non-stationary behavior with enough samples for reliability. We first denoise via Cadzow's low-rank projection, with rank $\hat{r}$ chosen by Singular Value Hard Thresholding (SVHT) on a Page matrix embedding. We prove that, under mild conditions, Page and Hankel matrices have the same finite-sample rank, so the SVHT rank transfers to the Hankel matrix for Cadzow denoising. The resulting denoised Hankel matrices yield a sequence of local models and noise-variance estimates for uncertainty-aware planning. We validate the framework in both simulation and hardware experiments under Gaussian and non-Gaussian correlated heavy-tailed noise. We show that the framework offers robust denoised predictions suitable for real-time control and planning tasks.

### Notation

$\mathbb{R}$ and $\mathbb{N}$ denote real and natural numbers. $I_{n}$ and $0_{m \times n}$ denote the $n \times n$ identity and $m \times n$ zero matrices, respectively. For matrix $A \in {\mathbb{R}}^{m \times n}$, $A^{\top}$, $A^{\dagger}$, and ${rank}{(A)}$ denote its transpose, Moore--Penrose pseudo-inverse, and rank respectively. We denote by ${diag}{(v)}$, the $n \times n$ diagonal matrix with elements of $v \in {\mathbb{R}}^{n}$ on its main diagonal. All linear combinations of vectors ${\{ v_{1},\ldots,v_{k}\}} \subset {\mathbb{R}}^{n}$ is denoted by ${span}{\{ v_{1},\ldots,v_{k}\}}$. We denote the variance of random variable $X$ by $\sigma_{X}^{2}$ and drop the subscript when the context is clear. For functions $f$ and $g$ with matching domain and co-domain, ${{f \circ g}{(x)}}:={f{({g{(x)}})}}$ denotes their composition.

## Problem Definition

Consider a robot that operates in the vicinity of another moving entity $\mathcal{O}$ whose behavior and dynamics are unknown. The robot's onboard sensors detect $\mathcal{O}$ and provide noisy, partial measurements of the obstacle state, denoted by $x_{t} \in {\mathbb{R}}^{n_{x}}$, which are sampled at a uniform interval ${\Deltat} \geq 0$, and capture kinematic quantities such as velocities or angular rates. While $x_{t}$ may not directly encode full Cartesian position, it carries sufficient temporal information to enable short-horizon motion prediction. The motion of $\mathcal{O}$ is governed by a discrete-time dynamical system with latent (unobserved) variables and unmeasured control inputs in the form: $z_{t + 1} = {\hat{f}{(z_{t},u_{t})}}$ where $z_{t}$ denotes the state, which may include latent (unobserved) variables and $u_{t}$ an input from an unknown policy $u_{t} = {c{(z_{t})}}$. Under these assumptions, we have an autonomous system

where measurement noise $\eta_{t} \in {\mathbb{R}}^{n_{x}}$ has an unknown distribution, and $C$ is the state-output map. This discrete time model generally arises from discretization of a continuous-time system. We maintain a sliding buffer of $N$ recent measurements $\mathcal{B}_{t} = {\{ x_{{t - N} + 1},\ldots,x_{t}\}}$ for online processing.

Problem Statement: Given streaming noisy observations $\{ x_{t}\}$ from a single trajectory and a sliding data buffer of fixed length $N$, construct, in real time, a tractable and adaptive local model. This model generates multi-step forecasts $\{{\overline{x}}_{t + 1},\ldots,{\overline{x}}_{t + N_{h}}\}$ over a prediction horizon $N_{h} \in {\mathbb{N}}$, suitable for downstream planning and control.

## Preliminaries

Here, we define key concepts that are leveraged in our method such as Hankel and Page embeddings, Hankel-DMD, Cadzow denoising, and Singular Value Hard Thresholding.

### III-A Hankel and Page Matrices

Guided by Takens' delay-embedding theorem (the dynamics of a system can be reconstructed from delay-coordinate maps of a single observable when the embedding dimension is sufficiently large ), we apply delay embedding to the obstacle measurements to extract informative information about its dynamics. Given a sequence of $N$ measurements ${\{ x_{{i - N} + 1},\ldots,x_{i}\}} \subset {\mathbb{R}}^{n_{x}}$, we denote the associated (block) *Hankel* matrix $H_{{{i - N} + 1}:i}^{L} \in {\mathbb{R}}^{{({Ln_{x}})} \times {({{N - L} + 1})}}$ :

The (block) *Page* ^11^1For $n_{x} = 1$, the matrices $H_{{{i - N} + 1}:i}^{L}$ and $P_{{{i - N} + 1}:i}^{L}$ take Hankel and Page forms, respectively. For $n_{x} > 1$, they become block Hankel and block Page. For simplicity, we refer to both cases as Hankel and Page structures.matrix $P_{{{i - N} + 1}:i}^{L} \in {\mathbb{R}}^{{({Ln_{x}})} \times m}$ partitions the same sequence into $m$ non-overlapping blocks of length $L$ (with $m = {N/L}$)^22^2Note that, unlike the Hankel matrix, in the Page matrix, the buffer length $N$ must be a multiple of the embedding window length $L$.:

### III-B Hankel-DMD

We review a variant of Hankel-DMD (cf. ) suitable for our problem. It uses delay embedding on the measurements of obstacle's observables (II). Given a measurement sequence $\{ x_{0},x_{1},\ldots,x_{n}\}$, form the one step shifted Hankel matrices $H_{0:{n - 1}}^{L}$ and $H_{1:n}^{L}$ according to the Eq.. Note that the columns of $H_{1:n}^{L}$ are shifted one time step forward from the columns of $H_{0:{n - 1}}^{L}$. To estimate the one-step dynamic prediction propagator, $A^{\ast}$, Hankel-DMD relies on the following least Frobenius-norm problem,

The closed form solution for $A^{\ast}$ is

Under standard assumptions of ergodicity and noise-free observables, Hankel-DMD can be used as a finite-dimensional approximation of the Koopman operator via delay embeddings. Our goal is to tackle the real-world cases where these assumptions do not hold.

### III-C Cadzow Algorithm for Denoising

Here, we review a variant of Cadzow's algorithm for denoising Hankel matrices. In the approximately linear lifted dynamics (e.g., Koopman-based approximations), noise-free data resides on a low-dimensional vector space. Hence, for a sufficiently large delay embedding window $L$, the noise-free Hankel trajectory matrix becomes low rank. However, with measurement noise, the observed Hankel matrix is generally full rank. Let Hankel matrix $H^{L} \in^{{({Ln_{x}})} \times {({{N - L} + 1})}}$ be constructed from $N$ consecutive noisy measurements with embedding window $L$. Decompose $H^{L}$ as $H^{L} = {{\hat{H}}^{L} + \Delta}$ with

where $\Delta$ denotes measurement noise and ${\hat{H}}^{L}$ is the noise-free Hankel matrix. The goal is to recover the (unknown) noise-free, low-rank Hankel matrix ${\hat{H}}^{L}$ from $H^{L}$. Cadzow's algorithm aims for this objective by alternating projections of $H^{L}$ on the set of matrices with rank of at most $r$ with projections of the result back onto the set of Hankel matrices.

Given a target rank $r$, define the projection map $\Pi_{r}$ onto the set of rank-$\leq r$ matrices as

where $H = {U\SigmaV^{\top}}$ is the SVD and $\Sigma_{r}$ is created by keeping the top $r$ singular values in $\Sigma$ while setting the rest to zero. The closed-form solution of is a direct consequence of Eckart--Young--Mirsky theorem. Similarly, we define the projection map $\Pi_{\mathsf{H}}$ onto the set of Hankel matrices as

Interestingly, the optimization problem has a closed-form solution which can be calculated by replacing the members of each anti-diagonal of $M$ with their average. The procedure is as follows: decompose $M$ into $L$ by ${N - L} + 1$ blocks similarly to the Hankel matrix^33^3Note that each block is a column vector with $n_{x}$ rows similarly to Eq.. And denote by $M_{i,j}$ the $ij$th block. For each anti-diagonal offset $d = {0,\ldots,{N - 1}}$, define:

where $s_{d} = {|\mathcal{I}_{d}|}$ is number of elements in $\mathcal{I}_{d}$. Then, the anti-diagonal averaging can be computed as

for ${1 \leq \ell \leq L},{\;1 \leq m \leq {{N - L} + 1}}$. The Cadzow algorithm successively applies the projections $\Pi_{r}$ and $\Pi_{\mathsf{H}}$ so that the sequence converges to a Hankel matrix, ${\hat{H}}^{L}$, that is approximately of rank $r$. The solution of the Cadzow algorithm on $H^{L}$ after $n$ iterations is ${\lbrack{\Pi_{\mathsf{H}} \circ \Pi_{r}}\rbrack}^{n}{(H^{L})}$ where ${\lbrack{\Pi_{\mathsf{H}} \circ \Pi_{r}}\rbrack}^{n}$ denotes the map created by composing $\Pi_{\mathsf{H}} \circ \Pi_{r}$, $n$-times with itself.

Notably, since projections $\Pi_{r}$ and $\Pi_{\mathsf{H}}$ can be computed in closed form, the Cadzow algorithm is an attractive choice for real-time denoising, as only a few iterations are sufficient to yield a reasonable signal-to-noise ratio.

### III-D Singular Value Hard Thresholding (SVHT)

Here we review a variant of Gavish and Donoho's result. Consider a sequence (indexed by $a$) of noisy matrices $Y_{a} = {X_{a} + {Z_{a}/\sqrt{n_{a}}}}$ where $Y_{a} \in {\mathbb{R}}^{m_{a} \times n_{a}}$ denotes a noisy matrix, $X_{a}$ the \"true\" low-rank matrix, and $Z_{a}$ denotes the noise matrix whose entries are i.i.d. zero-mean, unit-variance entries with finite fourth moment. As $a\rightarrow\infty$, the aspect ratio $m_{a}/n_{a}$ converge to $\beta \in {(0,1\rbrack}$^44^4Following, $a$ indexes a growing problem sequence with $Y_{a} \in {\mathbb{R}}^{m_{a} \times n_{a}}$, ${m_{a}/n_{a}}\rightarrow\beta$, and $Y_{a} = {X_{a} + {Z_{a}/\sqrt{n_{a}}}}$. Their AMSE--optimality results are asymptotic as $a\rightarrow\infty$..

Given the SVD $Y_{a} = {U\SigmaV^{\top}}$ and a threshold $\tau$, we approximate the true matrix $X_{a}$ by ${\hat{X}}_{a} = {U\Sigma_{\geq \tau}V^{\top}}$ where $\Sigma_{\geq \tau}$ is formed by zeroing the subthreshold elements of $\Sigma$.

Gavish and Donoho showed that the Asymptotic Mean Squared Error (AMSE)-optimal threshold for the data singular values depends only on the matrix aspect ratio $\beta$ via a constant $\lambda^{\star}{(\beta)}$:

For the noise standard deviation $\sigma$, the optimal threshold is:

When $\sigma$ is unknown, the optimal threshold can be estimated using a data-driven approach through the Marchenko--Pastur (MP) law, which gives the limiting eigenvalue distribution of ${({1/n_{a}})}Z_{a}{}_{}^{}$ as ${m_{a}/n_{a}}\rightarrow\beta$:

with ${p_{\beta}{(\delta)}} = 0$ outside $\lbrack\delta_{-},\delta_{+}\rbrack$. The median of the MP distribution, denoted by $\mu_{\beta}$, depends only on $\beta$ and provides a normalization for estimating the noise level $\sigma$. Taking $\varsigma_{med}$ as the median of the observed singular values, the data-driven AMSE--optimal threshold can thus be estimated as:

which remains asymptotically optimal under general white noise (i.i.d., zero mean, unit variance, finite fourth moment) with the same risk as in the Gaussian case \[14, Sec. VI\].

## Adaptive Hankel-DMD for Noisy Data

We now address the problem outlined in Sec. II. To enable real-time obstacle dynamics learning and motion prediction, we consider the use of Hankel-DMD (cf. Sec. III-B). However, applying Hankel-DMD in real-time robotics applications presents two key challenges:

Sensor noise: sensor signals are typically noisy, which contaminates matrices $H_{0:{n - 1}}^{L}$ and $H_{1:n}^{L}$. In least-squares schemes such as, noise in both data matrices leads to biased or inconsistent estimators.

Ergodicity and long trajectory data requirements: as noted in Sec. III-B, one must assume ergodicity and long data sequences to connect Hankel-DMD and the Koopman operator. Such assumptions rarely hold in robotics applications.

To tackle the noise issue, we introduce a Hankel matrix denoising scheme. We then propose an adaptive sliding-window variation of Hankel-DMD that continually updates the model. This approach ensures that the predictive model remains accurate as the object's state evolves over time.

### IV-A Denoising Hankel Matrices

Consider obstacle output measurements $\mathcal{B}_{t} = {\{ x_{{t - N} + 1},\ldots,x_{t}\}}$ for buffer size $N$, collected up to time $t$. We construct a Hankel matrix $H_{{{t - N} + 1}:t}^{L}$ from $\mathcal{B}$ according to Eq.. Since the measurements are noisy, we seek to denoise the Hankel matrix $H_{{{t - N} + 1}:t}^{L}$ via Cadzow's algorithm, as described in Sec. III-C. A key step in this algorithm is the low-rank projection $\Pi_{r}$ in Eq., which requires knowledge of the effective rank $r$ of the noise-free Hankel matrix. In practice, this typically unknown rank must be estimated. An rank estimat error can cause over-smoothing (if underestimated) or noise amplification (if overestimated). To avoid these problems, we adopt a principled, data-driven rank selection strategy based on Singular Value Hard Thresholding (SVHT) (Sec. III-D ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")). However, the SVHT framework assumes i.i.d. noise, an assumption that is violated in Hankel matrices due to repeated entries. To address this, we employ Page matrices (Eq. ), whose partition of the measurement buffer into non-overlapping blocks avoids correlation.

### IV-A1 Step I: Page-Hankel Rank Transfer

As a first step toward estimating the rank of the noise-free Hankel matrix using SVHT on Page matrices, we show that, under mild conditions, the Page and Hankel embeddings of the *same* noise-free measurement buffer share the same rank.

### Lemma 1 (Page--Hankel Rank Equivalence)

Consider a locally valid linear output model

with $z_{k} \in {\mathbb{R}}^{n_{z}}$, $A \in {\mathbb{R}}^{n_{z} \times n_{z}}$, and $C \in {\mathbb{R}}^{n_{x} \times n_{z}}$. Let ${\{{x_{0}\ldots},x_{N - 1}\}} \subset {\mathbb{R}}^{n_{x}}$ be the noise-free measurements generated by the system above from the initial condition $z_{0}$. Let $L \geq n_{z}$ be the embedding window and let $N = {dL}$, with $d \geq L$. Define^55^5To avoid confusion with superscript $L$, we use ${(A)}^{L}$ to denote the matrix created by raising $A$ to the power of $L$. $B = {(A)}^{L}$ and let $P^{L}$ and $H^{L}$ be the block Page and Hankel matrices constructed via the data. Then, ${{rank}{(P^{L})}} = {{rank}{(H^{L})}}$ if

### Proof of Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")

Given the definition of system and the initial condition, one can write $x_{i} = {C{(A)}^{i}z_{0}}$ for $i \in {\{ 0,\ldots,{N - 1}\}}$. Therefore, one can easily decompose the Page and Hankel matrices as

Note that by the hypothesis, ${{rank}{(F)}} = n_{z}$, which implies that $F$ has full row rank. Moreover, noting that $B = {(A)}^{L}$, one can easily see that all columns of $F$ are in the set of columns of $G$; hence, ${{rank}{(G)}} \geq {{rank}{(F)}} = n_{z}$. However, note that $G \in {\mathbb{R}}^{n_{z} \times {({{{({d - 1})}L} + 1})}}$ has more columns than rows; therefore, its rank can be at most $n_{z}$. Hence, one can conclude that both $F$ and $G$ have full row rank and

Moreover, using, the rank equality, and noting that ${{rank}{(E)}} \leq n_{z}$ (due to its size) one can write

On the other hand, Sylvester's rank inequality gives

Inequalities (IV-A1)-(IV-A1) in conjunction with lead to ${{rank}{(P^{L})}} = {{rank}{(H^{L})}} = {{rank}{(E)}}$ concluding the proof. ∎

Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning") provides a convenient way to connect the rank of Page and Hankel embedding of noise-free measurement buffers. Before proceeding to rank estimation, we briefly explain that the conditions of Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning") are mild. First, it is worth noting that with a sufficiently high sampling frequency, the system states associated with a given measurement buffer cluster within a small region of the state space, where a local linear model can accurately approximate the system's behavior^66^6This suggests that the buffer window size and sampling frequency should be chosen jointly to balance fidelity and sensitivity. An excessively large buffer reduces sensitivity to low-rank structures that capture local behavior, whereas an overly small buffer risks discarding expressive information about the system dynamics.. In addition, the condition ${{span}{\{ z_{0},{Bz_{0}},\ldots,{{(B)}^{d - 1}z_{0}}\}}} = {\mathbb{R}}^{n_{z}}$ is generic^77^7If the elements of $A$ (with $B = {(A)}^{L}$) and $z_{0}$ in Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning") are drawn from a reasonable distribution, the condition holds with probability one. and holds for almost all matrices $B$ and vectors $z_{0}$.

Now, with Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning") at our disposal, we can estimate the rank of the noise-free Hankel matrix associated with $H_{{{t - N} + 1}:t}^{L}$ by applying SVHT on the Page matrix constructed with the same data sequence.

### IV-A2 Rank Estimation using SVHT

To apply the SVHT (cf. Sec. III-D ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")) on the Page matrix, the number of rows in the matrix should be less than or equal to the number of columns. Therefore, for the rest of the paper, we consider the buffer length $N = {mLn_{x}}$, with $m \geq {Ln_{x}}$. Note that this choice already satisfies the size condition in Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning").

To construct the Page matrix $P_{{{t - N} + 1}:t}^{L} \in^{{Ln_{x}} \times m}$ from the same data sequence used in $H_{{{t - N} + 1}:t}^{L}$. By applying the SVHT formula in Eq.(11 ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")), on the Page matrix, we can estimate the singular value threshold $\tau^{\ast}$ and approximate the effective rank of $P_{{{t - N} + 1}:t}^{L}$ as

where ${\{\varsigma_{i}\}}_{i = 1}^{Ln_{x}}$ are the singular values of $P_{{{t - N} + 1}:t}^{L}$.

It is important to note that the rank $\hat{r}$ estimated via Page SVHT is not fixed but evolves as the sliding window advances. As the buffer shifts, the local data distribution changes, and the singular spectrum captures the instantaneous richness of the underlying dynamics. Consequently, small fluctuations or occasional variations in $\hat{r}$ are to be expected. Far from being a drawback, this adaptivity ensures that the thresholding remains sensitive to regime shifts and transient behaviors, ultimately producing more reliable models when the system exhibits greater dynamical complexity.

Sec. III-D ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning") also yields a conservative local noise--variance estimate. Singular values below the cutoff in Eq. (11 ‣ III Preliminaries ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning")) are treated as noise, while those above define the rank via Eq.. Let $\varsigma_{med}$ be the median singular value of the *Page* matrix with aspect ratio $\beta$ and $m$ columns, and let $\mu_{\beta}$ denote the median of the Marchenko--Pastur law at aspect ratio $\beta$. Then the noise variance ${\hat{\sigma}}^{2}$ can be conservatively estimated as ${\hat{\sigma}}^{2} \approx {{\varsigma_{med}^{2}/\mu_{\beta}}m}$. Under the assumption of i.i.d. sensor noise, we approximate the delay--state noise covariance as $\hat{\nu} \approx {{\hat{\sigma}}^{2}I_{Ln_{x}}}$. This approximation treats each delay state as being perturbed by independent, isotropic noise, which is appropriate in the i.i.d. setting but may underestimate correlations in more structured noise processes. A concrete example of leveraging such variance information within a risk-aware framework is provided .

### IV-A3 Cadzow Algorithm

Now, by using the rank estimate $\hat{r}$ in Eq. and utilizing Lemma 1. ‣ IV-A1 Step I: Page-Hankel Rank Transfer ‣ IV-A Denoising Hankel Matrices ‣ IV Adaptive Hankel-DMD for Noisy Data ‣ Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning"), we can finally apply the Cadzow algorithm in Sec.III-C on Hankel matrix $H_{{{t - N} + 1}:t}^{L}$ with effective rank $\hat{r}$ until we approximate a denoised Hankel matrix which we denote by ${\hat{H}}_{{{t - N} + 1}:t}^{L}$.

### IV-B Online Identification and Multi-Step Prediction

With the denoised Hankel matrix ${\hat{H}}_{{{t - N} + 1}:t}^{L}$ obtained, we proceed to model the system dynamics using Hankel-DMD. However, as mentioned earlier, to connect the behavior of the dynamics learned by Hankel-DMD in Eqs.- to the system's global behavior via Koopman operator, one often requires assumptions of ergodicity on the system and access to very long trajectories. These assumptions rarely hold in robotics applications. To circumvent this issue, we apply an adaptive sliding window strategy to build a linear model for each buffer and update it as we receive new data.

Formally, let ${\hat{H}}_{{{t - N} + 1}:{t - 1}}^{L}$ and ${\hat{H}}_{{{t - N} + 2}:t}^{L}$ be the Hankel matrices constructed by taking the first and last $N - L$ columns of ${\hat{H}}_{{{t - N} + 1}:t}^{L}$ respectively.

We then solve a least Frobenius-norm problem similar to Eq. as:

with the closed-form solution

We then define the local predictor dynamics as

If we initialize the system by setting $\psi_{t}$ to be equal to the last column of ${\hat{H}}_{{{t - N} + 2}:t}^{L}$ (which corresponds to the denoised version of the lifted state at the current time), we can forecast the future outputs of system (II) by running the predictor and extracting the last block of the delay embedded state as

where $\psi_{t}^{\ast}$ is set to be the last column of ${\hat{H}}_{{{t - N} + 2}:t}^{L}$ and matrix $D \in^{{n_{x} \times L}n_{x}}$ is defined as $D = {\lbrack 0_{{n_{x} \times {({L - 1})}}n_{x}},I_{n_{x}}\rbrack}$.

At the next time step, we advance the buffer to $\mathcal{B}_{t + 1} = {\{ x_{{t - N} + 2},\ldots,x_{t + 1}\}}$ and repeat the aforementioned procedure to produce a time-varying sequence of linear predictors characterized by ${\{{\hat{A}}_{t}\}}_{t \geq N}$. These predictors are well suited for Model Predictive Control (MPC) by providing linear predictions over the planning horizon. Algorithm 1 compiles the full sliding-window procedure.

Input: Embedding window L
Buffer Length N = m L nx with m ≥ L nx
Output: Denoised Hankel Ĥt − N + 1: tL
Model Ât and Forecasts $\{{\overline{x}}_{t + 1},\ldots,{\overline{x}}_{t + N_{h}}\}$
Noise covariance estimate ν̂
Page &amp; SVHT: Form Pt − N + 1: tL per Eq.
Compute SVD Pt − N + 1: tL = U diag (𝜍i) V⊤.
Set β = (L nx)/m and 𝜍med = median {𝜍i}
Set cutoff $\tau^{\star} = {{\lambda^{\star}{(\beta)}}/\sqrt{\mu_{\beta}}}$ via Eq. r̂ ← # {i: 𝜍i ≥ τ⋆} per Eq. )

Cadzow Algorithm for J Iterations: Ĥt − N + 1: tL ← [ΠH ∘ Πr]J (Ht − N + 1: tL)
Hankel Partitions and Predictor at t:
Prediction (Nh steps): Let be the last column of Ĥt − N + 2: tL. For j = 1, 2, …, Nh, ${\overline{x}}_{t + j} = {D{({\hat{A}}_{t})}^{j}{}_{}^{}}$ per Eq.
Noise Variance Estimation: With m Page columns and MP median μβ, set σ̂2 = 𝜍med2/(μβ m) and ν̂ = σ̂2 IL nx.
Slide Window: ℬt + 1 ← {xt − N + 2, …, xt + 1} and repeat –.
Algorithm 1 Adaptive Sliding-Window Page–Hankel DMD Predictor

### IV-C Comparison with Alternative Online Prediction Methods

Classical online noise filtering approaches, such as the KF and its nonlinear variants, assume parametric dynamics and structured noise models. While online Gaussian processes and neural sequence models provide strong predictive capability, they can require significant offline training and careful tuning for online deployment. In contrast, DMD and EDMD are operator-theoretic system identification methods that approximate the Koopman operator from data. These formulations do not account for measurement noise and can exhibit bias under finite, noisy datasets, particularly when nonlinear lifting is used. Although noise-aware formulations and regularized variants exist, these methods mainly improve dynamical consistency rather than provide a framework for denoising streaming measurements in finite-data regimes. our proposed method explicitly performs structured low-rank denoising prior to short-horizon prediction. Designed for finite, streaming data with limited computational budgets, the framework combines adaptive rank selection with structured matrix embeddings to enable stable real-time performance.

## Simulations and Experiments

We apply Algorithm 1 to validate out framework in simulations and real-world experiments. Our evaluation examines (i) signal--to-noise (SNR) separability, (ii) noise variance estimation, and (iii) multi-step prediction accuracy. Experiments consider open-loop, short-horizon prediction to assess the accuracy, stability and noise robustness of the learned dynamics model. These properties are critical for downstream planning and control frameworks.

### V-A Simulation: Noisy Unicycle

Consider a reference unicycle model ${\overset{˙}{x} = {u_{1}{\cos\theta}}},{{\overset{˙}{y} = {u_{1}{\sin\theta}}},{\overset{˙}{\theta} = u_{2}}}$ which serves as a dynamic obstacle moving along a figure-eight trajectory of amplitude $a = {3m}$ and period $T = {40s}$. An ego agent seeks to reach its goal while avoiding collisions with the unicycle, but has access to only noisy velocity measurements of the unicycle rather than the full state. Sampling the reference trajectory at ${\Deltat} = {0.02s}$ yields the forward velocity profile $u_{1}^{\star}{(t)}$. We inject sensor noise from two distributions: (i) i.i.d. Gaussian, $\eta_{k} \sim {\mathcal{N}{(0,\sigma_{x}^{2})}}$ with $\sigma_{x} = {{0.25m}/s}$ and (ii) correlated heavy-tailed AR--Laplace, ${\eta_{t} = {{\rho\eta_{t - 1}} + w_{t}}},{{w_{t} \sim {{Laplace}{(0,b)}}},{{|\rho|} < 1}}$. For fair comparison, $b$ is chosen so that the stationary variance matches the Gaussian case, ${{Var}{\lbrack\eta_{t}\rbrack}} = \sigma_{x}^{2}$, i.e. $b = \sqrt{{{({1 - \rho^{2}})}\sigma_{x}^{2}}/2}$. In both cases, the noisy measurement stream is $v_{t} = {{u_{1}^{\star}{(t)}} + \eta_{t}}$.

Figure 1: Gaussian noise: Top: noisy (gray), denoised (red) and ground truth (black dashed); call-outs show SNR improvement and average noise reduction. Bottom: zoomed segment and log-scale error.

Denoising results (Gaussian): Fig. 1 demonstrates that our Page-Hankel SVHT framework achieves stable recovery of the ground-truth velocity profile under Gaussian sensor noise. The denoised estimate (red, top panel) tracks the ground truth (dashed black) without visible phase lag while suppressing high-frequency artifacts that often contaminate raw measurements. Over the $160$ s trajectory, the method delivered an SNR gain of $19.2$ dB and an average noise reduction of $89.0\%$ (call-out, top-left), corresponding to nearly an order-of-magnitude improvement over baseline. The zoomed view (bottom-left) highlights that turning points and low-curvature segments, often degraded by conventional low-pass filters, were preserved, while the log-scale absolute error confirms a $10$-$100 \times$ reduction in residual magnitude. These results indicate that the method can denoise aggressively without compromising structural features critical for downstream control.

Figure 2: AR-Laplace noise: The denoising algorithm remains effective under heavy-tailed, correlated disturbances: call-outs: SNR + 6.9 dB and 54.4% noise reduction.

Denoising results (Heavy tailed, correlated noise): To probe robustness under non-Gaussian disturbances, we injected temporally correlated AR-Laplace noise (Fig. 2). Despite heavy tails and temporal correlation, we observed an SNR gain of $6.9$ dB and an average noise reduction of $54.4\%$, with no visible phase lag. While performance is lower than under Gaussian noise, as to be expected, the degradation remains gradual. Crucially, the low-rank Hankel structure proved distribution-agnostic i.e., SVHT adaptively trims singular values inflated by heavy-tailed noise requiring explicit Gaussian assumptions on the noise statistics.

Comparison with Extended Kalman Filter (EKF)-based denoising: For reference, we evaluated an EKF as a denoising pipeline under the same Gaussian disturbance conditions defined in Sec. V-A. When the process and measurement covariance matrices are carefully tuned using approximate knowledge of the noise moments, the EKF achieves moderate reconstruction quality, yielding an SNR of approximately $0.6$ dB. However, even in this tuned setting the EKF exhibits a noticeable phase delay (Fig. 3, top), which increases the point-wise reconstruction error used in the SNR calculation and may be problematic for downstream control pipelines that require temporally aligned state estimates for stable feedback and prediction. In contrast, the proposed Page/Hankel-based method achieves an SNR of $19.2$ dB under the same disturbance conditions.

In practical robotic systems, the true measurement noise statistics are typically unknown and may vary over time. Since the EKF relies on explicit specification of these noise moments to compute the Kalman gain, its performance is sensitive to covariance mismatch. Under mild mismatch in the assumed noise statistics, reconstruction quality yields an SNR of approximately $10.0$ dB (Fig. 3, bottom). Our proposed Page/Hankel framework estimates the noise structure directly from the data through low-rank structure and adaptive SVHT thresholding, avoiding explicit noise variance specification while maintaining consistent reconstruction performance across noise regimes.

Figure 3: Comparison of Page/Hankel denoising and EKF filtering under temporally correlated Gaussian noise (AR). Top: EKF with tuned covariance matrices (call-outs: SNR + 0.6 dB). Bottom: EKF under covariance mismatch (cal-outs: + 10.0 dB).

### V-B System Hardware and Experiments

This section experimentally validates the complete method in a setup (Fig. 4) motivated by a naval application. Currently, payloads are loaded into their silos by a ship-board crane while the ship docks in a port, where no ocean swells affect the safety of the loading process. It would be desirable to load these payloads while the ship is underway, potentially in heavy seas. In active sea states, the ship sways in response to ocean swells. Anticipating deck motion via a learned predictive model would enable the crane controller to compensate during payload delivery.

The testbed is a scaled crane mounted on an *E2M eMove eM6-300-1500* five-DoF Stewart platform that can reproduce wave-induced ship deck motions. A VN-100 IMU measures orientation (quaternion) and angular velocity of the simulated moving base at 30 Hz. These measurements correspond to the platform (deck) motion only, which is modeled as a time-varying base motion input to the crane-payload system. Using these IMU data, the framework generates a $31$-step horizon open-loop forecast ($\approx$`<!-- -->`{=html}1.0 s) of the platform motion. Payload and crane dynamics are not directly predicted and are instead assumed to evolve downstream in response to the predicted base motion.

Figure 4: Stewart‐platform testbed. Left: Moving‐base crane with target, obstacle, payload, and arm/tip cameras. Right: Base-mounted VectorNav VN-100 IMU supplying orientation and angular rates to the sliding window Hankel-DMD predictor.

This setup enables two evaluations: (i) whether the variance-stable denoising observed in simulation persists under real IMU noise and (ii) whether short-horizon sliding window Hankel-DMD predictions remain within a bounded threshold suitable for MPC integration. Fig. 5 (top) shows a representative trajectory where $N = 250$ sample context buffer (gray) feeds the pipeline, generating $31$-step forecasts (red) aligned with the ground truth (dashed black). The open-loop predictor achieves an RMSE of $0.012$ m/s.

Given a fixed error-tolerance $\varepsilon = 0.04$^88^8The tolerance $\varepsilon$ is chosen based on prior operational constraints of the experimental platform. In earlier implementations using a baseline constant-velocity predictor, prediction errors up to $0.08$ m were acceptable for reliable payload insertion. We therefore set $\varepsilon = 0.04$ as a conservative threshold that remains consistent with the hardware constraints., we define a violation-duration metric on the prediction error $e_{t}$ as

where $N_{h}$ defines the prediction horizon, ${\overline{x}}_{t}$ the prediction forecast, $x_{t}$ the measured ground truth, $\Deltat$ the sample period, and $\mathbf{1}{( \cdot )}$ the indicator (1 if the condition holds, 0 otherwise). In Fig. 5 (bottom), $J_{t} = 89.0$ s ($1.6\%$ of horizon^99^9The fraction of the horizon spent above threshold, $\%\text{violating} = \;100 \times \frac{J_{t}}{T_{hor}},T_{hor}:=N_{h}\Delta t.$), certifying that prediction errors are bounded within the tolerance for $98.4\%$ of the time.

Further investigation of Fig. 5 (top) reveals occasional transient spikes in the predicted trajectory, after which the forecasts quickly return to a nominal accuracy. These anomalies arise when the local embedding window captures a regime shift or abrupt disturbance, briefly mis-aligning the rank estimate. Importantly, such events are short-lived and self-correct as the sliding buffer refreshes, with the subsequent predictions re-stabilizing around the future measurements. This highlights both the adaptivity and the finite-sample sensitivity of the method, i.e., while transient outliers can occur, the framework consistently recovers without persistent drift.

Figure 5: Top: context buffer (N = 250, gray) and 31-step forecasts (red) overlaid with ground truth (black dashed). Bottom: absolute prediction error |et| (blue) compared to threshold ε (red dashed).

Fig. 6 illustrates the evolution of the eigenvalues of the learned predictors across sliding windows. As the system behavior changes along the trajectory, the models adapt accordingly, and the eigenvalues shift smoothly while consistently remaining within the unit circle, ensuring Schur stability. The gradual evolution of the spectrum highlights the stability and time-varying nature of the local Hankel-DMD models throughout the experiment.

Figure 6: Evolution of eigenvalue across sliding windows: full spectra with iteration-colored progression.

Together, these results demonstrate that our framework not only denoises real sensor streams but also yields stable and bounded predictions that are suitable for downstream planning and control applications. A real-time demonstration of the moving-base prediction and MPC integration is shown in the supplementary video.

### V-C Parameter Sensitivity and Computational Analysis

While Sec.V-B validates hardware performance using a selected configuration of the hyper-parameters ($N = 250$, $L = 10$, $J = 20$), we now examine the sensitivity of the prediction accuracy and computational cost to the embedding length $L$ and the number of Cadzow iterations $J$.

TABLE I: Effect of Cadzow iterations J on runtime and prediction error (N = 250, L = 10). Cadzow time corresponds to the iterative Cadzow projection up to a maximum of J iterations, with early termination when the relative tolerance tol = 10−6 is satisfied.

Cadzow iterations $J$: Based on Table I, with $N = 250$ and $L = 10$ fixed, increasing the number of Cadzow iterations improves prediction accuracy up to $J = 20$, reducing RMSE from $0.0129$ ($J = 1$) to $0.0115$ ($J = 20$). Beyond this point, additional iterations provide negligible accuracy gains while increasing computational cost approximately linearly. These results indicate that moderate Cadzow iterations provide a favorable trade-off between accuracy and runtime.

Embedding length $L$: As evidenced in Table II with $N = 250$ and $J = 20$ fixed, the prediction accuracy improves as the $L$ increases up to an intermediate value. RMSE decreases from $0.060$ at $L = 4$ to $0.0108$ at $L = 12$, with a slight degradation at $L = 13$. This reflects a finite-data trade-off where larger embeddings increase model expressivity but reduce the number of snapshot pairs of $N/L$, which may degrade the matrix conditioning and stability of the locally linear dynamical model. Runtime grows moderately with $L$, with the Cadzow projection constituting the dominant over the total computational time. A comprehensive ablation study analyzing the sensitivity of RMSE, Cadzow runtime, and total computation time to the hyper-parameters is summarized in the Appendix (Table III).

TABLE II: Effect of embedding length L on total computation time and prediction error (N = 250, J = 20). Cadzow time corresponds to the iterative Cadzow projection up to a maximum of J iterations, with early termination when the relative tolerance tol = 10−6 is satisfied.

## Conclusion And Future Work

We introduced a Page--Hankel SVHT framework for learning short-horizon predictive models of moving obstacles from noisy data streams. Simulations (Gaussian and heavy-tailed noise) showed good variance-stable, distribution-agnostic performance, and hardware tests with IMU data produce reliable forecasts that can support downstream control. Future work will explore online adaptation, tensorized delayed embeddings for multi-axis consistency, and integration within an MPC-based prediction framework.
