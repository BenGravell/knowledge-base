<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Variational Inference MPC Using Tsallis Divergence

Topics include Model predictive path integral control, Variational inference, Tsallis divergence, Stochastic optimal control, Model predictive control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends variational inference MPC by replacing KL divergence with Tsallis divergence, yielding a broader family of sampling-based controllers that recovers MPPI as a special case and can better handle multimodal cost landscapes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we provide a generalized framework for Variational Inference-Stochastic Optimal Control by using thenon-extensive Tsallis divergence. By incorporating the deformed exponential function into the optimality likelihood function, a novel Tsallis Variational Inference-Model Predictive Control algorithm is derived, which includes prior works such as Variational Inference-Model Predictive Control, Model Predictive Path Integral Control, Cross Entropy Method, and Stein Variational Inference Model Predictive Control as special cases. The proposed algorithm allows for effective control of the cost/reward transform and is characterized by superior performance in terms of mean and variance reduction of the associated cost. The aforementioned features are supported by a theoretical and numerical analysis on the level of risk sensitivity of the proposed algorithm as well as simulation experiments on 5 different robotic systems with 3 different policy parameterizations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Variational Inference (VI) is a powerful tool for approximating the posterior distribution of the unobserved random variables. VI recasts the approximation problem as an optimization problem. Instead of directly approximating the target distribution $p{(\left. z \middle| x \right.)}$ of the latent variable $z$, VI minimizes the Kullback-Leibler (KL) divergence between a tractable variational distribution $q{(z)}$ and the target distribution. Due to its faster convergence and comparable performance to Markov Chain Monte Carlo sampling methods, VI has received increasing attention in machine learning and robotics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

VI has been applied to Stochastic Optimal Control (SOC) problems recently. In Okada and Taniguchi, the authors formulated the SOC problem as a VI problem by setting the desired policy distribution as the target distribution. The VI-SOC framework works directly in the space of policy distributions instead of specific policy parameterizations in most SOC and Reinforcement Learning (RL) frameworks. This gives rise to a unified derivation for a variety of parametric policy distributions, such as unimodal Gaussian and Gaussian mixture in Okada and Taniguchi. Lambert et al. derived the VI-SOC algorithm for non-parametric policy distribution using Stein variational gradient descent. Apart from the policy distribution, the VI-SOC framework is characterized by two components, the optimality likelihood function and distributional distance metric. The optimality likelihood function measures the likelihood of trajectory samples to be optimal and defines the cost/reward transform to allow for different algorithmic developments. The distributional distance metric is the measure of distance between the variational distribution and target distribution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In existing VI-SOC works, the KL divergence is used as the distributional distance metric due to its simplicity. On the other hand, recent advances in VI research involve extending the framework to other statistical divergences, such as the $\alpha$-divergence and $\chi$-divergence. In Wang et al., Regli and Silva, the authors proposed variants of the $\alpha$-divergence to improve the performance and robustness of the inference algorithm. Wan et al. further extended the VI framework to $f$-divergence, which is a broad statistical divergence family that recovers the KL, $\alpha$ and $\chi$-divergence as special cases.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Tsallis divergence is another generalized divergence rooted in non-extensive statistical mechanics. Tsallis divergence and Tsallis entropy are generalizations of the KL divergence and Shannon entropy respectively. The Tsallis entropy is non-additive (hence non-extensive) in the sense that for a system composed of (probabilistically) independent subsystems, the total entropy differs from the sum of the entropies of the subsystems. Over the last two decades, an increasing number of complex natural, artificial and social systems have verified the predictions and consequences derived from the Tsallis entropy and divergence. Lee et al. demonstrated that Tsallis entropy regularization leads to improved performance and faster convergence in RL applications.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we provide a generalized formulation of the VI-SOC framework using the Tsallis divergence and introduce a novel Model Predictive Control (MPC) algorithm.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose the Tsallis VI-MPC algorithm, which allows for additional control of the shape of the cost transform compared to previous VI-MPC algorithms using KL divergence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a holistic view of connections between Tsallis VI-SOC and the state-of-the-art Model Predictive Path Integral (MPPI) control, Cross Entropy Method (CEM) and Stochastic Search (SS) methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show, both analytically and numerically, that the proposed Tsallis VI-SOC framework achieves lower cost variance than MPPI and CEM. We further demonstrate the superior performance of Tsallis VI-SOC in mean cost and variance minimization on simulated systems from control theory and robotics for 3 different choices of policy distributions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tsallis Variational Inference-Stochastic Optimal Control", "weight": 1.0} -->

In this section, we review the VI-SOC formulation using KL divergence and derive the novel Tsallis divergence VI-SOC framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

We can formulate the SOC problem as an inference problem and apply methods from VI. To apply VI to SOC, we introduce a dummy optimality variable $o \in {\{ 0,1\}}$ with $o = 1$ indicating that the trajectory $\tau = {\{ X,U\}}$ is optimal. Table I compares the differences in notation between conventional VI methods and SOC formulated as a VI problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

The objective of VI-SOC is to sample from the posterior distribution

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

Here $p{(\left. x_{t + 1} \middle| {x_{t},u_{t}} \right.)}$ is the state transition probability, $p{(x_{0})}$ is the initial state distribution and $p{(u_{t})}$ is some prior control distribution (e.g. zero mean Gaussian or uniform distribution). For simplicity, we use $o$ to indicate $o = 1$ and $o^{\prime}$ for $o = 0$ from here. We can now formulate the VI-SOC objective as minimizing the distance between a controlled distribution $q{(\tau)}$ and the target distribution $p{(\left. \tau \middle| o \right.)}$

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

where the constant $p{(o)}$ is dropped. The first term in the objective measures the likelihood of a trajectory being optimal while the second term serves as regularization. Splitting the expectation in the first term, we get

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

Optimality Likelihood: The optimality likelihood in Eq. 3 can be parameterized by a non-increasing function of the trajectory cost $J{(X,U)}$ as ${p{(\left. o \middle| \tau \right.)}} ≔ {f{({J{(X,U)}})}}$. The monotonicity requirement ensures that trajectories incurring higher costs are always less likely to be optimal. Common choices of $f$ include ${f{(x)}} = {\exp{({- x})}}$ and ${f{(x)}} = \mathbf{1}_{\{{x \leq \gamma}\}}$. In this paper, we choose ${f{(x)}} = {\exp{({- x})}}$ such that ${{\log p}{(\left. o \middle| \tau \right.)}} = {- {J{(X,U)}}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

To avoid excessive notation, we abuse the notation to define ${J{(U)}} ≔ {{\mathbb{E}}_{p{({X|U})}}{\lbrack{J{(X,U)}}\rbrack}}$ and the $N$-sample empirical approximation of the expectation $J = {\sum_{n = 1}^{N}{\lbrack J^{(n)}\rbrack}}$. Hence, Eq. 3 takes the form

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B KL VI-SOC", "weight": 1.0} -->

which can be interpreted as an application of the famous maximum entropy principle.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Tsallis VI-SOC", "weight": 1.0} -->

In this subsection, we use the Tsallis divergence as the regularization function and derive the Tsallis-VI-SOC algorithm. First, we define the deformed logarithm and exponential as

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Tsallis VI-SOC", "weight": 1.0} -->

where ${( \cdot )}_{+} ≔ {\max{(0, \cdot )}}$ and $r > 0$. Using $\log_{r}$ and $\exp_{r}$ we can define the Tsallis entropy and the corresponding Tsallis divergence as

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Tsallis VI-SOC", "weight": 1.0} -->

Versions of Tsallis Statistics: In our definition of the deformed logarithm and exponential in Eqs. 5 and 6, we use the variable $r$ instead of the $q$ used in most literature to avoid assigning multiple meanings to $q$. Also, our definition of $\log_{r}$ and $\exp_{r}$ differ from its original definitions, but the original can be recovered with $r^{\prime} = {2 - r}$, where $r^{\prime}$ corresponding to the value used. Additionally, there are multiple formulations of the Tsallis entropy differing in their definitions of the internal energy and how expectations are taken. We have chosen to use the formulation from due to its simplicity in computing the expectation. However, as shown, they are equivalent and can be recovered from each other via a change of variables.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Tsallis VI-SOC", "weight": 1.0} -->

We can now define a new objective by replacing the KL divergence regularizer in Eq.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Tsallis VI-SOC", "weight": 1.0} -->

The controlled distribution has to satisfy the additional constraint of ${\int{q{(U)}\text{d}U}} = 1$. The optimal policy distribution $q^{\ast}$ can be explicitly solved for with the form

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Tsallis VI-SOC", "weight": 1.0} -->

where $\overset{\sim}{\lambda} = {\alpha{({r - 1})}\lambda}$ with $\alpha$ being the Lagrange multiplier for the constraint that $q^{\ast}$ integrates to $1$. A detailed derivation can be found in Section SM-1 of the supplementary materials. We can now use Eq. 10 to obtain the optimal control distribution by transforming the prior distribution.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

In general, it is computationally inefficient to sample from $q^{\ast}{(U)}$ via Eq. 10 directly.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

We now solve Eq. 11 for 3 different policy classes: unimodal Gaussian, Gaussian mixture and a nonparametric policy corresponding to Stein Variational Gradient Descent (SVGD). The full derivations for each can be found in the supplementary material in Section SM-2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

Unimodal Gaussian: For a unimodal Gaussian policy distribution with parameters $\Theta ≔ {\{{(\mu_{t},\Sigma_{t})}\}}_{t = 0}^{T - 1}$, the update laws for the $k + 1$th iteration take the form of

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

Gaussian Mixture: Alternatively, the policy distribution can be an $L$-mode mixture of Gaussian distribution with parameters $\Theta ≔ {\{\theta_{l}\}}_{l = 1}^{L}$ for $\theta_{l} ≔ {(\phi_{l},{\{\mu_{l,t},\Sigma_{l,t}\}}_{t = 0}^{T - 1})}$, where $\phi_{l}$ is the mixture weight for the $l$th component. Although it is not possible to directly solve Eq. 11 in this case, we draw from Expectation Maximization (EM) to derive an iterative update scheme for the $k + 1$th iteration with the form

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

Stein Variational Policy: The policy can also be a non-parametric distribution approximated by a set of particles $\Theta ≔ {\{\theta_{l}\}}_{l = 1}^{L}$ for some parametrized policy $\hat{\pi}{(U;\theta)}$. In, $\hat{\pi}$ is taken to be a unimodal Gaussian with fixed variance, where $\theta \in {\mathbb{R}}^{n_{x} \times {({T - 1})}}$ corresponds to the mean. The update law of each Stein particle for the $k + 1$th iteration has the form

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

where the $N$ is chosen such that $N = {LS}$, $\hat{k}$ is a kernel function, and $w^{(l,s)} = w^{({m + {L{({l - 1})}}})}$, where $S$ denotes the number of rollouts for each of the $L$ particle. As noted, SVGD becomes less effective as the dimensionality of the particles increases due to the inverse relationship between the repulsion force in the update law and the dimensionality. Hence, we follow in choosing a sum of local kernel functions as our choice of $\hat{k}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-D Update Laws", "weight": 1.0} -->

Update Law for Unimodal Gaussian

<!-- chunk {"id": "body-0033", "role": "body", "section": "Connections to Related Works", "weight": 1.0} -->

In this section, we compare VI-SOC with three sampling-based methods from optimization, thermodynamics, and information theory that have been applied to stochastic control problems. A comparison of problem formulations and update laws for different approaches with a unimodal Gaussian policy is in Table II.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Stochastic Search", "weight": 1.0} -->

SS is a stochastic optimization scheme and has also been applied to the SOC setting. SS-SOC parameterizes the control policy with a distribution from the exponential family during problem formulation and optimizes with respect to policy parameters whereas VI-SOC performs optimization at the distribution level. The SS-SOC framework formulates the problem as

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Stochastic Search", "weight": 1.0} -->

where $S{( \cdot )}$ is a monotonically decreasing shape function. Note that in Eq. 24, the expectation taken with respect to $p{(\left. X \middle| U \right.)}$ is inside the shape function $S$ as opposed to outside as in Eq. 3. For convex shape/optimality likelihood functions, the objective in VI-SOC corresponds to an upper bound of that in SS-SOC, i.e.,

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Stochastic Search", "weight": 1.0} -->

A detailed comparison of the two formulations can be found.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Stochastic Search", "weight": 1.0} -->

The parameter update of SS-SOC has the form

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Stochastic Search", "weight": 1.0} -->

where $T{( \cdot )}$ denotes the sufficient statistic for the corresponding parameter and $\beta$ is the step size. In the case of a unimodal Gaussian policy, the update in Eq. 26 is equivalent to Eqs. 14 and 15 with ${S{(J)}} = {\exp_{r}{({- {{\overset{\sim}{\lambda}}^{- 1}J}})}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Cross Entropy Method", "weight": 1.0} -->

CEM is a widely used algorithm in reinforcement learning and optimal control problems. The objective function of CEM minimizes the expected cost ${\mathbb{E}}{\lbrack J\rbrack}$. The policy update law for CEM corresponds to that of SS-SOC in Eq. 26 with shape function ${S{(J)}} = \mathbf{1}_{\{{J \leq \gamma}\}}$ where $\gamma$ is the elite threshold. As will be shown in Section IV-A, CEM is also a special case of the reparameterized Tsallis VI-SOC with $r\rightarrow\infty$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Model Predictive Path Integral Control", "weight": 1.0} -->

MPPI is another approach closely related to VI-SOC and SS-SOC. The framework solves for the controls by minimizing the KL divergence between a controlled distribution and the optimal control distribution

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Model Predictive Path Integral Control", "weight": 1.0} -->

The optimal distribution achieves the free energy lower bound, $\mathcal{F} = {- {\lambda{\log{\mathbb{E}}_{p{(U)}}}{\lbrack{\exp{({- {\frac{1}{\lambda}J}})}}\rbrack}}}$, which has been shown to be the solution of the Hamilton-Jacobi-Bellman equation. The optimal distribution here is equivalent to Eq. 10 when $r\rightarrow 1$. The corresponding update law can also be obtained from the SS-SOC framework with ${S{(J)}} = {\exp{({- {\lambda^{- 1}J}})}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Effect of $\\exp_{r}$", "weight": 1.0} -->

To facilitate the analysis, we focus on the $\exp_{r}$ term in Eq. 10. Reparametrizing $\overset{\sim}{\lambda} = {{({r - 1})}\gamma}$, we get

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Effect of $\\exp_{r}$", "weight": 1.0} -->

where $\gamma$ is now the threshold beyond which the optimality weight is set to 0. The reparameterization adjusts the original parameter $\overset{\sim}{\lambda}$ at every iteration to maintain the same threshold $\gamma$, which is a more intuitive parameter. In addition, we have observed that the reparameterized framework is easier to tune and achieves better performance than the original formulation. Therefore, we focus our analysis and simulations on only the reparameterized version hereon after. Note that in practice, it is easier to define an elite fraction, which adjusts $\gamma$ based on the scale of the costs, instead of using $\gamma$ for easier tuning.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Variance Reduction", "weight": 1.0} -->

With the connection to SS, the effect of Tsallis divergence can be analyzed through the equivalent problem formulation in optimization. In Section III-A, it is shown that Tsallis VI-SOC corresponds to an upper bound of SS-SOC with objective

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-B Variance Reduction", "weight": 1.0} -->

The variance reduction effect can be analyzed through the coefficient of Absolute Risk Aversion (ARA)

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Variance Reduction", "weight": 1.0} -->

where Tsallis VI-SOC corresponds to ${S{(J)}} = {\exp_{r}{({- {{\overset{\sim}{\lambda}}^{- 1}J}})}}$). The ARA coefficient measures a scaled ratio of terms corresponding to the mean and variance terms in the Taylor series expansion of the objective. Negative value of the coefficient corresponds to a risk-averse objective, and positive value of the coefficient corresponds to risk-seeking behavior.^11^1ARA is originally used for utility maximization, where a larger ARA corresponds to greater risk aversion. This is the opposite in our case when we are performing cost minimization.The ARA coefficient of Tsallis VI-SOC is

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Variance Reduction", "weight": 1.0} -->

The ARA coefficients for MPPI and CEM are

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Variance Reduction", "weight": 1.0} -->

Since $A_{\text{MPPI}}$ is a positive constant, it corresponds to a risk-seeking algorithm. For a cost below the elite threshold, $J < \gamma$, $A_{\text{CEM}} = {- \infty}$ and $A_{\text{Tsallis}} \lessgtr 0$ for $r \lessgtr 2$. This leads to the Tsallis VI-SOC framework achieving lower variance than MPPI. For the same elite threshold $\gamma$ and a properly selected $r$, we hypothesize that Tsallis VI-SOC results in lower mean cost than CEM since CEM penalizes variance infinitely harder than the mean and assigns equal weights to all elite samples. A more detailed analysis and the derivation of ARA coefficient are included in Section SM-3 of the supplementary material.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

1: Given: p (x0): initial state distribution; N: number of policy samples; M: number of state samples; T: MPC horizon; T′: number of MPC steps; K: optimization iterations per MPC step
Algorithm 1 Tsallis Variational Inference MPC

<!-- chunk {"id": "body-0050", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

With the update laws in Section II-D and a choice of the optimality likelihood function $f$, we propose the novel Tsallis VI-MPC algorithm, summarized in Algorithm 1.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

Given the initial state distribution $p{(x_{0})}$ and a prior policy distribution, $N \times M$ initial states are sampled. Given the initial states, $N$ control trajectories are sampled from the policy distribution. For each control trajectory sample, $M$ state trajectories are propagated for a total of $N \times M$ rollouts. The state transitions at each timestep are sampled from the stochastic dynamics $F{(x,u,\epsilon)}$ where $\epsilon$ corresponds to system stochasticity (zero mean Gaussian $\epsilon \sim {\mathcal{N}{(0,{\sigma_{\epsilon}^{2}\mathbf{I}})}}$ used in this paper). The cost of each trajectory is normalized to $\lbrack 0,1\rbrack$ for numerical stability and easier tuning. Depending on the choice of policy distribution class, the policy parameters are updated based on the update laws in Section II-D.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

Cost (Std Dev)
Mean Control Error

<!-- chunk {"id": "body-0053", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

For the first iteration, we perform additional warm-up iterations by running the optimization loop (line 5 to 14) for a larger $K_{\text{warmup}}$ iterations before executing the first control and performing $K$ optimization iterations in the ensuing MPC steps.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

Control Selection: With the optimized policy distribution from the VI-SOC framework, the control to be executed on the real system is selected differently based on the choice of policy class. For the unimodal Gaussian policy, the mean of the distribution is used. For the Gaussian mixture policy, the mean of the model with the highest mixture weight is executed. In terms of the Stein policy, the Stein particle with the highest weight is used.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Model Predictive Control Algorithm", "weight": 1.0} -->

Receding Horizon: After the control execution, the policy distribution is shifted to warm start the optimization at the next MPC timestep. Let $\theta^{\prime}$ be the next iteration's starting sequence and $\theta$ be the current iteration's sequence and set $\theta_{t}^{\prime} = \theta_{t + 1}$ for $t = {0,\ldots,{T - 2}}$. Finally, set the last item in the new sequence as $\theta_{T - 1}^{\prime} = \theta_{T - 1}$. This is known as the receding horizon technique in MPC. Note that in Algorithm 1, $\Theta = {\{\theta_{0},\cdots,\theta_{T - 1}\}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we compare the proposed Tsallis VI-MPC algorithm against MPPI and CEM, which represent state-of-the-art sampling-based SOC algorithms. Since in practice, the shape functions used in SS-SOC corresponds to the ones which result in MPPI and CEM, we have chosen to only compare to MPPI and CEM. We first validate our analysis on a simple numerical experiment. We then showcase the scalability and performance of the Tsallis VI-MPC algorithm on 2D point mass, quadcopter, ant, manipulator and humanoid systems in simulation under the 3 aforementioned policy distributions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-A Numerical Analysis", "weight": 1.0} -->

where $\xi \sim {\mathcal{N}{}}$, $erf$ is the corresponding error function, the constants $\lambda$ and $\sigma$ are chosen to be ${\lambda = 0.2},{\sigma = 2.5}$, and $c$ and $d$ are chosen such that the noiseless objective function is normalized between $0$ and $1$ for $u \in {\lbrack{- 5},5\rbrack}$. Figure 3 plots the objective function near its minimum and the noisy objective values.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-A Numerical Analysis", "weight": 1.0} -->

To ensure that only the weight computation of the three methods is tested, we sample $64$ instances of $u$ uniformly from $\lbrack{- 5},5\rbrack$ and use the same set of samples for all three methods. We use the update law corresponding to the unimodal Gaussian with fixed variance for each algorithm and compare the resulting mean and standard deviation of the cost obtained from each method after a single optimization iteration. A grid search is performed over $4096$ different hyperparameters, and the optimization metric is computed as the cost averaged over $4096$ random seeds. The results for the best performing hyperparameters are shown in Table III and agree with our intuition that the objective function of Tsallis VI-SOC should result in a lower variance compared to MPPI and a lower mean compared to CEM. In addition, in Fig. 2, we observe that mean cost increases slower as the elite fraction decreases from the optimal value than when increases, while the opposite is true for cost standard deviation.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B Controls and Robotics Systems", "weight": 1.0} -->

The dynamics for the planar navigation and quadcopter tasks are solved via an Euler discretization. Details of the dynamics can be found in Section SM-4. For the manipulator, ant, and humanoid tasks, we use the GPU-accelerated Isaac-Gym to sample trajectory rollouts in parallel. Additional system stochasticity is injected to each system through the controls channel such that ${F{(x_{t},u_{t},\epsilon_{t})}} = {F{(x_{t},{u_{t} + \epsilon_{t}})}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-B Controls and Robotics Systems", "weight": 1.0} -->

The hyperparameters and system configurations for all simulations are included in Section SM-4. To ensure fair comparisons, all hyperparameters for each method are tuned using a combination of the TPE algorithm from the Neural Network Intelligence (NNI) AutoML framework and hand tuning.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-B1 Planar Navigation", "weight": 1.0} -->

We first test the different algorithms on a point-mass planar navigation problem. The task is for the point-mass with double-integrator stochastic dynamics to navigate through an obstacle field to reach the target location. The dynamics and obstacle field are set up the same way as. If a crash occurs, a crash cost is incurred and no further movement is allowed.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-B2 Quadcopter", "weight": 1.0} -->

We also set up a quadcopter 3-D navigation task. The task is for the quadcopter to reach a target location while avoiding obstacles. The quadcopter dynamics are taken. The quadcopter task is similiar to the planar navigation task, where the system is expected to fly through a randomly generated forest to reach the target location. If a crash occurs, a crash cost is incurred and no further movement is allowed.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-B3 Franka Manipulator", "weight": 1.0} -->

We next test on the Franka manipulator modified to have 7-DOF by removing the last joint and fixing the fingers. The objective of this task is to move the end effector around the obstacles to the goal. An illustration of the task is in Fig. 4. It is worth noting that no crash cost is in place for the Franka manipulator. Instead, contact is included as a part of the simulation dynamics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-B4 Ant", "weight": 1.0} -->

We also consider the task of locomotion. We test on the ant system, which has $29$ state dimensions, $8$ control dimensions, and is a widely used testbed for RL algorithms.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B5 Humanoid", "weight": 1.0} -->

Finally, we test our approach on the complex humanoid locomotion task. The humanoid system has $56$ state dimensions, $21$ control dimensions, and has very unstable dynamics.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-C Discussion", "weight": 1.0} -->

In Table IV, we can see the results of each experiment summarized between each robotic system, policy parameterization, and choice of SOC framework. Across all systems we can see Tsallis VI-MPC results in lower means and variances in most policy parameterizations. The trend continues even as the complexity of the dynamics increases showing that the flexibility provided by the VI-MPC framework is useful even in high dimensional systems.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-C Discussion", "weight": 1.0} -->

First in the planar navigation case, we see that Tsallis VI-MPC outperforms the other algorithms in almost all policy parameterizations. During testing, there was high variability in the trajectories computed by each algorithm. The best performing algorithms would have a large increase in velocity towards the goal state, and would have enough variation in sampled trajectories to "see" obstacles via large costs in order to avoid them. When comparing the trajectories computed through the GM policy parameterization we tend to see a reduced ability to stabilize at the goal resulting in larger costs overall when compared to other parameterizations. For these systems, the Stein policy results in longer trajectories to the goal. Next in the Quadcopter experiments, we observe that the Tsallis VI-MPC outperforms both MPPI and CEM in mean cost for the unimodal Gaussian and Stein policies. When looking at the high dimensional simulation environments, we see the same trend of Tsallis VI-MPC reducing the mean and variance in comparison to CEM and MPPI holds even for complex systems with contact dynamics.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-C Discussion", "weight": 1.0} -->

The performance of the Tsallis VI-MPC can be attributed to the ability of the algorithm to sample policies that are low cost (via the elite fraction), but then improve beyond the CEM by performing the cost weighted averaging similar to MPPI. These characteristics of Tsallis VI-MPC are additionally heavily related to the choice of hyperparameters. From hand tuning, we observe that reducing the elite fraction generally results in lower mean cost but higher standard deviation and vice versa. As the cost transform approaches that of CEM or MPPI, the mean and standard deviation approaches their corresponding value. This verifies that the Tsallis VI-SOC framework can be thought of as an interpolation between CEM and MPPI to a certain degree. The best performing configuration is usually somewhere in between these two extremes.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-C Discussion", "weight": 1.0} -->

Finally note that even though the Tsallis VI-SOC framework is typically used over multiple iterations in optimization schemes where the parameters can evolve as the optimization progresses, we have shown the benefits even in MPC mode, where a single iteration of optimization is performed, reiterating the empirical result that a single step has higher reduction in mean cost and variance compared to traditional MPC methods.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present a generalized Variational Inference-Stochastic Optimal Control framework using Tsallis divergence, which allows for additional control of the cost/reward transform and results in lower cost/reward variance. We provide a unifying study of the connections between Tsallis VI-SOC, MPPI, CEM, and SS methods. The performance and variance reduction benefits of the proposed Tsallis VI-SOC framework is verified analytically and numerically. We further showcase advantages of the Tsallis VI-MPC algorithm against MPPI and CEM on 5 different systems with 3 different policy distributions. We leave 2 extensions of this work as future research directions: 1. Implementation of the proposed algorithm on real systems; 2. Comparison against VI-MPC algorithms using other generalized divergences.
