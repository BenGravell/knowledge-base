## Introduction

Variational Inference (VI) is a powerful tool for approximating the posterior distribution of the unobserved random variables. VI recasts the approximation problem as an optimization problem. Instead of directly approximating the target distribution $p{(\left. z \middle| x \right.)}$ of the latent variable $z$, VI minimizes the Kullback-Leibler (KL) divergence between a tractable variational distribution $q{(z)}$ and the target distribution. Due to its faster convergence and comparable performance to Markov Chain Monte Carlo sampling methods, VI has received increasing attention in machine learning and robotics.

VI has been applied to Stochastic Optimal Control (SOC) problems recently. In Okada and Taniguchi, the authors formulated the SOC problem as a VI problem by setting the desired policy distribution as the target distribution. The VI-SOC framework works directly in the space of policy distributions instead of specific policy parameterizations in most SOC and Reinforcement Learning (RL) frameworks. This gives rise to a unified derivation for a variety of parametric policy distributions, such as unimodal Gaussian and Gaussian mixture in Okada and Taniguchi. Lambert et al. derived the VI-SOC algorithm for non-parametric policy distribution using Stein variational gradient descent. Apart from the policy distribution, the VI-SOC framework is characterized by two components, the optimality likelihood function and distributional distance metric. The optimality likelihood function measures the likelihood of trajectory samples to be optimal and defines the cost/reward transform to allow for different algorithmic developments. The distributional distance metric is the measure of distance between the variational distribution and target distribution.

In existing VI-SOC works, the KL divergence is used as the distributional distance metric due to its simplicity. On the other hand, recent advances in VI research involve extending the framework to other statistical divergences, such as the $\alpha$-divergence and $\chi$-divergence. In Wang et al., Regli and Silva, the authors proposed variants of the $\alpha$-divergence to improve the performance and robustness of the inference algorithm. Wan et al. further extended the VI framework to $f$-divergence, which is a broad statistical divergence family that recovers the KL, $\alpha$ and $\chi$-divergence as special cases.

Tsallis divergence is another generalized divergence rooted in non-extensive statistical mechanics. Tsallis divergence and Tsallis entropy are generalizations of the KL divergence and Shannon entropy respectively. The Tsallis entropy is non-additive (hence non-extensive) in the sense that for a system composed of (probabilistically) independent subsystems, the total entropy differs from the sum of the entropies of the subsystems. Over the last two decades, an increasing number of complex natural, artificial and social systems have verified the predictions and consequences derived from the Tsallis entropy and divergence. Lee et al. demonstrated that Tsallis entropy regularization leads to improved performance and faster convergence in RL applications.

In this paper, we provide a generalized formulation of the VI-SOC framework using the Tsallis divergence and introduce a novel Model Predictive Control (MPC) algorithm. The main contribution of our work is threefold:

We propose the Tsallis VI-MPC algorithm, which allows for additional control of the shape of the cost transform compared to previous VI-MPC algorithms using KL divergence.

We provide a holistic view of connections between Tsallis VI-SOC and the state-of-the-art Model Predictive Path Integral (MPPI) control, Cross Entropy Method (CEM) and Stochastic Search (SS) methods.

We show, both analytically and numerically, that the proposed Tsallis VI-SOC framework achieves lower cost variance than MPPI and CEM. We further demonstrate the superior performance of Tsallis VI-SOC in mean cost and variance minimization on simulated systems from control theory and robotics for 3 different choices of policy distributions.

The rest of this paper is organized as follows: in Section II, we review KL VI-SOC and derive the Tsallis VI-SOC framework. In Section III, we discuss the connections between Tsallis VI-SOC and related works. A reparameterization and analysis of the framework is included in Section IV, and we propose the novel Tsallis VI-MPC algorithm in Section V. We showcase the performance of the proposed algorithm against related works in Section VI and conclude the paper in Section VII.

## Tsallis Variational Inference-Stochastic Optimal Control

In this section, we review the VI-SOC formulation using KL divergence and derive the novel Tsallis divergence VI-SOC framework.

### II-A SOC Problem Formulation

In discrete time SOC, we work with trajectories $\tau ≔ {\{ X,U\}}$ of state, $X ≔ {\{ x_{0},x_{1},\ldots,x_{T}\}} \in {\mathbb{R}}^{{n_{x} \times T} + 1}$, and control, $U ≔ {\{ u_{0},u_{1},\ldots,u_{T - 1}\}} \in {\mathbb{R}}^{n_{u} \times T}$ over a finite time horizon $T > 0$. The goal in SOC problems is to minimize the expected cost defined by an arbitrary cost function $J:{{{\mathbb{R}}^{n_{x} \times T} \times {\mathbb{R}}^{{n_{u} \times T} - 1}}\rightarrow{\mathbb{R}}^{+}}$ with initial state distribution $p{(x_{0})}$ and state transition probability $p{(\left. x_{t + 1} \middle| {x_{t},u_{t}} \right.)}$ corresponding to stochastic dynamics $x_{t + 1} = {F{(x_{t},u_{t},\epsilon_{t})}}$ where $\epsilon_{t} \in {\mathbb{R}}^{n_{\epsilon}}$ is the system stochasticity.

### II-B KL VI-SOC

We can formulate the SOC problem as an inference problem and apply methods from VI. To apply VI to SOC, we introduce a dummy optimality variable $o \in {\{ 0,1\}}$ with $o = 1$ indicating that the trajectory $\tau = {\{ X,U\}}$ is optimal. Table I compares the differences in notation between conventional VI methods and SOC formulated as a VI problem.

The objective of VI-SOC is to sample from the posterior distribution

Here $p{(\left. x_{t + 1} \middle| {x_{t},u_{t}} \right.)}$ is the state transition probability, $p{(x_{0})}$ is the initial state distribution and $p{(u_{t})}$ is some prior control distribution (e.g. zero mean Gaussian or uniform distribution). For simplicity, we use $o$ to indicate $o = 1$ and $o^{\prime}$ for $o = 0$ from here on. We can now formulate the VI-SOC objective as minimizing the distance between a controlled distribution $q{(\tau)}$ and the target distribution $p{(\left. \tau \middle| o \right.)}$

where the constant $p{(o)}$ is dropped. The first term in the objective measures the likelihood of a trajectory being optimal while the second term serves as regularization. Splitting the expectation in the first term, we get

where $p{(U)}$ and $q{(U)}$ represent $\prod_{t = 0}^{T - 1}{p{(u_{t})}}$ and $\prod_{t = 0}^{T - 1}{q{(u_{t})}}$ respectively due to independence and ${p{(\left. X \middle| U \right.)}} = {p{(x_{0})}{\prod_{t = 0}^{T - 1}{p{(\left. x_{t + 1} \middle| {x_{t},u_{t}} \right.)}}}}$.

Optimality Likelihood: The optimality likelihood in Eq. 3 can be parameterized by a non-increasing function of the trajectory cost $J{(X,U)}$ as ${p{(\left. o \middle| \tau \right.)}} ≔ {f{({J{(X,U)}})}}$. The monotonicity requirement ensures that trajectories incurring higher costs are always less likely to be optimal. Common choices of $f$ include ${f{(x)}} = {\exp{({- x})}}$ and ${f{(x)}} = \mathbf{1}_{\{{x \leq \gamma}\}}$. In this paper, we choose ${f{(x)}} = {\exp{({- x})}}$ such that ${{\log p}{(\left. o \middle| \tau \right.)}} = {- {J{(X,U)}}}$. To avoid excessive notation, we abuse the notation to define ${J{(U)}} ≔ {{\mathbb{E}}_{p{({X|U})}}{\lbrack{J{(X,U)}}\rbrack}}$ and the $N$-sample empirical approximation of the expectation $J = {\sum_{n = 1}^{N}{\lbrack J^{(n)}\rbrack}}$. Hence, Eq. 3 takes the form

which can be interpreted as an application of the famous maximum entropy principle.

TABLE I: Notation comparison between Variational Inference and Variational Inference-Stochastic Optimal Control.

### II-C Tsallis VI-SOC

In this subsection, we use the Tsallis divergence as the regularization function and derive the Tsallis-VI-SOC algorithm. First, we define the deformed logarithm and exponential as

where ${( \cdot )}_{+} ≔ {\max{(0, \cdot )}}$ and $r > 0$. Using $\log_{r}$ and $\exp_{r}$ we can define the Tsallis entropy and the corresponding Tsallis divergence as

Note that as $r\rightarrow 1$, $\log_{r}\rightarrow\log$, $\exp_{r}\rightarrow\exp$, $\mathcal{D}_{r}\rightarrow\mathcal{D}_{KL}$ and $\mathcal{S}_{r}\rightarrow\mathcal{S}$, where $\mathcal{S}$ is the Shannon entropy, recovering the KL VI-SOC framework.

Versions of Tsallis Statistics: In our definition of the deformed logarithm and exponential in Eqs. 5 and 6, we use the variable $r$ instead of the $q$ used in most literature to avoid assigning multiple meanings to $q$. Also, our definition of $\log_{r}$ and $\exp_{r}$ differ from its original definitions, but the original can be recovered with $r^{\prime} = {2 - r}$, where $r^{\prime}$ corresponding to the value used in. Additionally, there are multiple formulations of the Tsallis entropy differing in their definitions of the internal energy and how expectations are taken. We have chosen to use the formulation from due to its simplicity in computing the expectation. However, as shown in, they are equivalent and can be recovered from each other via a change of variables.

We can now define a new objective by replacing the KL divergence regularizer in Eq. 4 with the Tsallis divergence and introducing a parameter $\lambda$ that multiplies the optimality likelihood to make the regularization strength tunable:

The controlled distribution has to satisfy the additional constraint of ${\int{q{(U)}\text{d}U}} = 1$. The optimal policy distribution $q^{\ast}$ can be explicitly solved for with the form

where $\overset{\sim}{\lambda} = {\alpha{({r - 1})}\lambda}$ with $\alpha$ being the Lagrange multiplier for the constraint that $q^{\ast}$ integrates to $1$. A detailed derivation can be found in Section SM-1 of the supplementary materials. We can now use Eq. 10 to obtain the optimal control distribution by transforming the prior distribution.

### II-D Update Laws

In general, it is computationally inefficient to sample from $q^{\ast}{(U)}$ via Eq. 10 directly. Instead, we can approximate $q^{\ast}{(U)}$ by some policy $\pi{(U)}$ lying in a class $\Pi$ of tractable distributions and solve for an iterative update law by minimizing the KL divergence between $\pi{(U)}$ and $q^{\ast}{(U)}$:

However, because one can only evaluate $q^{\ast}{(U)}$ at a finite number of points ${\{ U^{(n)}\}}_{n = 1}^{N}$, we instead approximate $q^{\ast}{(U)}$ by the empirical distribution ${\overset{\sim}{q}}^{\ast}{(U)}$ with weights $w^{(n)}$:

We now solve Eq. 11 for 3 different policy classes: unimodal Gaussian, Gaussian mixture and a nonparametric policy corresponding to Stein Variational Gradient Descent (SVGD). The full derivations for each can be found in the supplementary material in Section SM-2.

Unimodal Gaussian: For a unimodal Gaussian policy distribution with parameters $\Theta ≔ {\{{(\mu_{t},\Sigma_{t})}\}}_{t = 0}^{T - 1}$, the update laws for the $k + 1$th iteration take the form of

Gaussian Mixture: Alternatively, the policy distribution can be an $L$-mode mixture of Gaussian distribution with parameters $\Theta ≔ {\{\theta_{l}\}}_{l = 1}^{L}$ for $\theta_{l} ≔ {(\phi_{l},{\{\mu_{l,t},\Sigma_{l,t}\}}_{t = 0}^{T - 1})}$, where $\phi_{l}$ is the mixture weight for the $l$th component. Although it is not possible to directly solve Eq. 11 in this case, we draw from Expectation Maximization (EM) to derive an iterative update scheme for the $k + 1$th iteration with the form

Stein Variational Policy: The policy can also be a non-parametric distribution approximated by a set of particles $\Theta ≔ {\{\theta_{l}\}}_{l = 1}^{L}$ for some parametrized policy $\hat{\pi}{(U;\theta)}$. In, $\hat{\pi}$ is taken to be a unimodal Gaussian with fixed variance, where $\theta \in {\mathbb{R}}^{n_{x} \times {({T - 1})}}$ corresponds to the mean. The update law of each Stein particle for the $k + 1$th iteration has the form

where the $N$ is chosen such that $N = {LS}$, $\hat{k}$ is a kernel function, and $w^{(l,s)} = w^{({m + {L{({l - 1})}}})}$, where $S$ denotes the number of rollouts for each of the $L$ particle. As noted in, SVGD becomes less effective as the dimensionality of the particles increases due to the inverse relationship between the repulsion force in the update law and the dimensionality. Hence, we follow in choosing a sum of local kernel functions as our choice of $\hat{k}$.

Update Law for Unimodal Gaussian

$\theta_{t}^{k + 1} = {\sum_{n = 1}^{N}\frac{{\exp_{r}\left( {- {{\overset{\sim}{\lambda}}^{- 1}J^{n}}} \right)}s{(u_{t}^{n})}u_{t}^{n}}{\sum_{n^{\prime} = 1}^{N}{{\exp_{r}\left( {- {{\overset{\sim}{\lambda}}^{- 1}J^{n^{\prime}}}} \right)}s{(u_{t}^{n^{\prime}})}}}}$

$\theta_{t}^{k + 1} = {\sum_{n = 1}^{N}\frac{{\exp\left( {- {\lambda^{- 1}J^{n}}} \right)}s{(u_{t}^{n})}u_{t}^{n}}{\sum_{n^{\prime} = 1}^{N}{{\exp\left( {- {\lambda^{- 1}J^{n^{\prime}}}} \right)}s{(u_{t}^{n^{\prime}})}}}}$

$\theta_{t}^{k + 1} = {\theta_{t}^{k} + {\beta{\sum_{n = 1}^{N}\frac{S{(J^{n})}{({u_{t}^{n} - {\frac{1}{N}{\sum_{\overset{\sim}{n} = 1}^{N}u_{t}^{\overset{\sim}{n}}}}})}}{\sum_{n^{\prime} = 1}^{N}{S{(J^{n^{\prime}})}u_{t}^{n^{\prime}}}}}}}$

$\theta_{t}^{k + 1} = {{\alpha\theta_{t}^{k}} + {{({1 - \alpha})}{\sum_{n = 1}^{N}\frac{\mathbf{1}_{\{{J^{n} \leq \gamma}\}}u_{t}^{n}}{\sum_{n^{\prime} = 1}^{N}\mathbf{1}_{\{{J^{n^{\prime}} \leq \gamma}\}}}}}}$

TABLE II: Comparison of the objective and the update law for a unimodal Gaussian policy with fixed variance between different SOC approaches.

## Connections to Related Works

In this section, we compare VI-SOC with three sampling-based methods from optimization, thermodynamics, and information theory that have been applied to stochastic control problems. A comparison of problem formulations and update laws for different approaches with a unimodal Gaussian policy is in Table II.

### III-A Stochastic Search

SS is a stochastic optimization scheme and has also been applied to the SOC setting. SS-SOC parameterizes the control policy with a distribution from the exponential family during problem formulation and optimizes with respect to policy parameters whereas VI-SOC performs optimization at the distribution level. The SS-SOC framework formulates the problem as

where $S{( \cdot )}$ is a monotonically decreasing shape function. Note that in Eq. 24, the expectation taken with respect to $p{(\left. X \middle| U \right.)}$ is inside the shape function $S$ as opposed to outside as in Eq. 3. For convex shape/optimality likelihood functions, the objective in VI-SOC corresponds to an upper bound of that in SS-SOC, i.e.,

A detailed comparison of the two formulations can be found in.

The parameter update of SS-SOC has the form

where $T{( \cdot )}$ denotes the sufficient statistic for the corresponding parameter and $\beta$ is the step size. In the case of a unimodal Gaussian policy, the update in Eq. 26 is equivalent to Eqs. 14 and 15 with ${S{(J)}} = {\exp_{r}{({- {{\overset{\sim}{\lambda}}^{- 1}J}})}}$.

### III-B Cross Entropy Method

CEM is a widely used algorithm in reinforcement learning and optimal control problems. The objective function of CEM minimizes the expected cost ${\mathbb{E}}{\lbrack J\rbrack}$. The policy update law for CEM corresponds to that of SS-SOC in Eq. 26 with shape function ${S{(J)}} = \mathbf{1}_{\{{J \leq \gamma}\}}$ where $\gamma$ is the elite threshold. As will be shown in Section IV-A, CEM is also a special case of the reparameterized Tsallis VI-SOC with $r\rightarrow\infty$.

### III-C Model Predictive Path Integral Control

MPPI is another approach closely related to VI-SOC and SS-SOC. The framework solves for the controls by minimizing the KL divergence between a controlled distribution and the optimal control distribution

The optimal distribution achieves the free energy lower bound, $\mathcal{F} = {- {\lambda{\log{\mathbb{E}}_{p{(U)}}}{\lbrack{\exp{({- {\frac{1}{\lambda}J}})}}\rbrack}}}$, which has been shown to be the solution of the Hamilton-Jacobi-Bellman equation. The optimal distribution here is equivalent to Eq. 10 when $r\rightarrow 1$. The corresponding update law can also be obtained from the SS-SOC framework with ${S{(J)}} = {\exp{({- {\lambda^{- 1}J}})}}$.

## Analysis

Figure 1: Reparameterized expr (). Left: r is varied with fixed γ = 1. It is clear that expr→ CEM as r → ∞. Right: γ is adjusted accordingly such that expr→ MPPI as r → 1.

### IV-A Effect of $\exp_{r}$

To facilitate the analysis, we focus on the $\exp_{r}$ term in Eq. 10. Reparametrizing $\overset{\sim}{\lambda} = {{({r - 1})}\gamma}$, we get

where $\gamma$ is now the threshold beyond which the optimality weight is set to 0. The reparameterization adjusts the original parameter $\overset{\sim}{\lambda}$ at every iteration to maintain the same threshold $\gamma$, which is a more intuitive parameter. In addition, we have observed that the reparameterized framework is easier to tune and achieves better performance than the original formulation. Therefore, we focus our analysis and simulations on only the reparameterized version hereon after. Note that in practice, it is easier to define an elite fraction, which adjusts $\gamma$ based on the scale of the costs, instead of using $\gamma$ for easier tuning.

Figure 1 illustrates the shapes of the function corresponding to different $r$ and $\gamma$ values. For $J < \gamma$, as $r\rightarrow\infty$, ${\exp_{r}{({- {{\overset{\sim}{\lambda}}^{- 1}J}})}}\rightarrow 1$. Hence, $\exp_{r}{({- {{\overset{\sim}{\lambda}}^{- 1}J}})}$ converges pointwise to the step function $\mathbf{1}_{\{{J \leq \gamma}\}}$ with $r\rightarrow\infty$. On the other hand, for any $0 < \frac{J}{\gamma} < 1$, we have that

which tends to 0 as $r\rightarrow 1$. Hence, $\exp\left( {\frac{1}{r - 1}{\log\left( {1 - \frac{J}{\gamma}} \right)}} \right)$ converges to $\mathbf{1}_{\{{J = 0}\}}$ as $r\rightarrow 1$.

### IV-B Variance Reduction

With the connection to SS, the effect of Tsallis divergence can be analyzed through the equivalent problem formulation in optimization. In Section III-A, it is shown that Tsallis VI-SOC corresponds to an upper bound of SS-SOC with objective

The variance reduction effect can be analyzed through the coefficient of Absolute Risk Aversion (ARA)

for the optimization problem

where Tsallis VI-SOC corresponds to ${S{(J)}} = {\exp_{r}{({- {{\overset{\sim}{\lambda}}^{- 1}J}})}}$). The ARA coefficient measures a scaled ratio of terms corresponding to the mean and variance terms in the Taylor series expansion of the objective. Negative value of the coefficient corresponds to a risk-averse objective, and positive value of the coefficient corresponds to risk-seeking behavior.^11^1ARA is originally used for utility maximization, where a larger ARA corresponds to greater risk aversion. This is the opposite in our case when we are performing cost minimization.The ARA coefficient of Tsallis VI-SOC is

The ARA coefficients for MPPI and CEM are

Since $A_{\text{MPPI}}$ is a positive constant, it corresponds to a risk-seeking algorithm. For a cost below the elite threshold, $J < \gamma$, $A_{\text{CEM}} = {- \infty}$ and $A_{\text{Tsallis}} \lessgtr 0$ for $r \lessgtr 2$. This leads to the Tsallis VI-SOC framework achieving lower variance than MPPI. For the same elite threshold $\gamma$ and a properly selected $r$, we hypothesize that Tsallis VI-SOC results in lower mean cost than CEM since CEM penalizes variance infinitely harder than the mean and assigns equal weights to all elite samples. A more detailed analysis and the derivation of ARA coefficient are included in Section SM-3 of the supplementary material.

## Model Predictive Control Algorithm

1: Given: p (x0): initial state distribution; N: number of policy samples; M: number of state samples; T: MPC horizon; T′: number of MPC steps; K: optimization iterations per MPC step
Algorithm 1 Tsallis Variational Inference MPC

With the update laws in Section II-D and a choice of the optimality likelihood function $f$, we propose the novel Tsallis VI-MPC algorithm, summarized in Algorithm 1.

Given the initial state distribution $p{(x_{0})}$ and a prior policy distribution, $N \times M$ initial states are sampled. Given the initial states, $N$ control trajectories are sampled from the policy distribution. For each control trajectory sample, $M$ state trajectories are propagated for a total of $N \times M$ rollouts. The state transitions at each timestep are sampled from the stochastic dynamics $F{(x,u,\epsilon)}$ where $\epsilon$ corresponds to system stochasticity (zero mean Gaussian $\epsilon \sim {\mathcal{N}{(0,{\sigma_{\epsilon}^{2}\mathbf{I}})}}$ used in this paper). The cost of each trajectory is normalized to $\lbrack 0,1\rbrack$ for numerical stability and easier tuning. Depending on the choice of policy distribution class, the policy parameters are updated based on the update laws in Section II-D.

Figure 2: Comparison of mean cost and cost variance for the numerical analysis system Eq. 36. The cost achieved using the updated u from a single update step, averaged over 4096 different seeds, is shown over the entire range of the hyperparameter set for CEM, MPPI and Tsallis VI-SOC. The hyperparameters which minimize the mean and standard deviation of the cost are shown as a cyan and orange star respectively.

Cost (Std Dev)
Mean Control Error

TABLE III: Comparison on a simple single stage stochastic optimization problem Eq. 36. The best values are boldfaced.

Figure 3: A comparison of the updated means for CEM, MPPI and Tsallis VI-SOC using the best set of hyperparameters on a single realization of 64 noisy samples of u (green) for the numerical analysis system. Each sample is a noisy realization.

For the first iteration, we perform additional warm-up iterations by running the optimization loop (line 5 to 14) for a larger $K_{\text{warmup}}$ iterations before executing the first control and performing $K$ optimization iterations in the ensuing MPC steps.

Control Selection: With the optimized policy distribution from the VI-SOC framework, the control to be executed on the real system is selected differently based on the choice of policy class. For the unimodal Gaussian policy, the mean of the distribution is used. For the Gaussian mixture policy, the mean of the model with the highest mixture weight is executed. In terms of the Stein policy, the Stein particle with the highest weight is used.

Receding Horizon: After the control execution, the policy distribution is shifted to warm start the optimization at the next MPC timestep. Let $\theta^{\prime}$ be the next iteration's starting sequence and $\theta$ be the current iteration's sequence and set $\theta_{t}^{\prime} = \theta_{t + 1}$ for $t = {0,\ldots,{T - 2}}$. Finally, set the last item in the new sequence as $\theta_{T - 1}^{\prime} = \theta_{T - 1}$. This is known as the receding horizon technique in MPC. Note that in Algorithm 1, $\Theta = {\{\theta_{0},\cdots,\theta_{T - 1}\}}$.

## Simulations

In this section, we compare the proposed Tsallis VI-MPC algorithm against MPPI and CEM, which represent state-of-the-art sampling-based SOC algorithms. Since in practice, the shape functions used in SS-SOC corresponds to the ones which result in MPPI and CEM, we have chosen to only compare to MPPI and CEM. We first validate our analysis on a simple numerical experiment. We then showcase the scalability and performance of the Tsallis VI-MPC algorithm on 2D point mass, quadcopter, ant, manipulator and humanoid systems in simulation under the 3 aforementioned policy distributions.

### VI-A Numerical Analysis

We verify the analysis in Section IV-B that Tsallis VI-SOC results in greater variance reduction by comparing the $\exp_{r}$ cost transform with the CEM and MPPI cost transforms on the following simple single-stage stochastic optimization problem:

where $\xi \sim {\mathcal{N}{}}$, $erf$ is the corresponding error function, the constants $\lambda$ and $\sigma$ are chosen to be ${\lambda = 0.2},{\sigma = 2.5}$, and $c$ and $d$ are chosen such that the noiseless objective function is normalized between $0$ and $1$ for $u \in {\lbrack{- 5},5\rbrack}$. Figure 3 plots the objective function near its minimum and the noisy objective values.

To ensure that only the weight computation of the three methods is tested, we sample $64$ instances of $u$ uniformly from $\lbrack{- 5},5\rbrack$ and use the same set of samples for all three methods. We use the update law corresponding to the unimodal Gaussian with fixed variance for each algorithm and compare the resulting mean and standard deviation of the cost obtained from each method after a single optimization iteration. A grid search is performed over $4096$ different hyperparameters, and the optimization metric is computed as the cost averaged over $4096$ random seeds. The results for the best performing hyperparameters are shown in Table III and agree with our intuition that the objective function of Tsallis VI-SOC should result in a lower variance compared to MPPI and a lower mean compared to CEM. In addition, in Fig. 2, we observe that mean cost increases slower as the elite fraction decreases from the optimal value than when increases, while the opposite is true for cost standard deviation.

### VI-B Controls and Robotics Systems

The dynamics for the planar navigation and quadcopter tasks are solved via an Euler discretization. Details of the dynamics can be found in Section SM-4. For the manipulator, ant, and humanoid tasks, we use the GPU-accelerated Isaac-Gym to sample trajectory rollouts in parallel. Additional system stochasticity is injected to each system through the controls channel such that ${F{(x_{t},u_{t},\epsilon_{t})}} = {F{(x_{t},{u_{t} + \epsilon_{t}})}}$.

The hyperparameters and system configurations for all simulations are included in Section SM-4. To ensure fair comparisons, all hyperparameters for each method are tuned using a combination of the TPE algorithm from the Neural Network Intelligence (NNI) AutoML framework and hand tuning.

TABLE IV: Comparisons of mean and standard deviation of cost against MPPI and CEM on different systems and policy classes. The policy classes are defined as Unimodal Gaussian (UG), Gaussian Mixture (GM), and Stein (S). Note that the negative of the reward is used for the locomotion tasks (ant and humanoid). The best mean cost and cost variance for each system-policy distribution pair is boldfaced. The mean and standard deviation reduction percentages are included to the right where positive values correspond to a reduction.

### VI-B1 Planar Navigation

We first test the different algorithms on a point-mass planar navigation problem. The task is for the point-mass with double-integrator stochastic dynamics to navigate through an obstacle field to reach the target location. The dynamics and obstacle field are set up the same way as. If a crash occurs, a crash cost is incurred and no further movement is allowed.

### VI-B2 Quadcopter

We also set up a quadcopter 3-D navigation task. The task is for the quadcopter to reach a target location while avoiding obstacles. The quadcopter dynamics are taken from. The quadcopter task is similiar to the planar navigation task, where the system is expected to fly through a randomly generated forest to reach the target location. If a crash occurs, a crash cost is incurred and no further movement is allowed.

### VI-B3 Franka Manipulator

We next test on the Franka manipulator modified to have 7-DOF by removing the last joint and fixing the fingers. The objective of this task is to move the end effector around the obstacles to the goal. An illustration of the task is in Fig. 4. It is worth noting that no crash cost is in place for the Franka manipulator. Instead, contact is included as a part of the simulation dynamics.

Figure 4: Task setup for Franka manipulator. The goal is to reach the red block while avoiding the pink and green obstacles.

### VI-B4 Ant

We also consider the task of locomotion. We test on the ant system, which has $29$ state dimensions, $8$ control dimensions, and is a widely used testbed for RL algorithms.

### VI-B5 Humanoid

Finally, we test our approach on the complex humanoid locomotion task. The humanoid system has $56$ state dimensions, $21$ control dimensions, and has very unstable dynamics.

### VI-C Discussion

In Table IV, we can see the results of each experiment summarized between each robotic system, policy parameterization, and choice of SOC framework. Across all systems we can see Tsallis VI-MPC results in lower means and variances in most policy parameterizations. The trend continues even as the complexity of the dynamics increases showing that the flexibility provided by the VI-MPC framework is useful even in high dimensional systems.

First in the planar navigation case, we see that Tsallis VI-MPC outperforms the other algorithms in almost all policy parameterizations. During testing, there was high variability in the trajectories computed by each algorithm. The best performing algorithms would have a large increase in velocity towards the goal state, and would have enough variation in sampled trajectories to "see" obstacles via large costs in order to avoid them. When comparing the trajectories computed through the GM policy parameterization we tend to see a reduced ability to stabilize at the goal resulting in larger costs overall when compared to other parameterizations. For these systems, the Stein policy results in longer trajectories to the goal. Next in the Quadcopter experiments, we observe that the Tsallis VI-MPC outperforms both MPPI and CEM in mean cost for the unimodal Gaussian and Stein policies. When looking at the high dimensional simulation environments, we see the same trend of Tsallis VI-MPC reducing the mean and variance in comparison to CEM and MPPI holds even for complex systems with contact dynamics.

The performance of the Tsallis VI-MPC can be attributed to the ability of the algorithm to sample policies that are low cost (via the elite fraction), but then improve beyond the CEM by performing the cost weighted averaging similar to MPPI. These characteristics of Tsallis VI-MPC are additionally heavily related to the choice of hyperparameters. From hand tuning, we observe that reducing the elite fraction generally results in lower mean cost but higher standard deviation and vice versa. As the cost transform approaches that of CEM or MPPI, the mean and standard deviation approaches their corresponding value. This verifies that the Tsallis VI-SOC framework can be thought of as an interpolation between CEM and MPPI to a certain degree. The best performing configuration is usually somewhere in between these two extremes.

Finally note that even though the Tsallis VI-SOC framework is typically used over multiple iterations in optimization schemes where the parameters can evolve as the optimization progresses, we have shown the benefits even in MPC mode, where a single iteration of optimization is performed, reiterating the empirical result that a single step has higher reduction in mean cost and variance compared to traditional MPC methods.

## Conclusion

We present a generalized Variational Inference-Stochastic Optimal Control framework using Tsallis divergence, which allows for additional control of the cost/reward transform and results in lower cost/reward variance. We provide a unifying study of the connections between Tsallis VI-SOC, MPPI, CEM, and SS methods. The performance and variance reduction benefits of the proposed Tsallis VI-SOC framework is verified analytically and numerically. We further showcase advantages of the Tsallis VI-MPC algorithm against MPPI and CEM on 5 different systems with 3 different policy distributions. We leave 2 extensions of this work as future research directions: 1. Implementation of the proposed algorithm on real systems; 2. Comparison against VI-MPC algorithms using other generalized divergences.
