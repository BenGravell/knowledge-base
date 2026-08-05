<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Integral Sampler: A Stochastic Control Approach for Sampling

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Path Integral Sampler~(PIS), a novel algorithm to draw samples from unnormalized probability density functions. The PIS is built on the Schrödinger bridge problem which aims to recover the most likely evolution of a diffusion process given its initial distribution and terminal distribution. The PIS draws samples from the initial distribution and then propagates the samples through the Schrödinger bridge to reach the terminal distribution. Applying the Girsanov theorem, with a simple prior diffusion, we formulate the PIS as a stochastic optimal control problem whose running cost is the control energy and terminal cost is chosen according to the target distribution. By modeling the control as a neural network, we establish a sampling algorithm that can be trained end-to-end. We provide theoretical justification of the sampling quality of PIS in terms of Wasserstein distance when sub-optimal control is used. Moreover, the path integrals theory is used to compute importance weights of the samples to compensate for the bias induced by the sub-optimality of the controller and time-discretization. We experimentally demonstrate the advantages of PIS compared with other start-of-the-art sampling methods on a variety of tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are interested in drawing samples from a target density $\hat{\mu} = {Z\mu}$ known up to a normalizing constant $Z$. Although it has been widely studied in machine learning and statistics, generating asymptotically unbiased samples from such unnormalized distribution can still be challenging. In practice, variational inference (VI) and Monte Carlo (MC) methods are two popular frameworks for sampling.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Variational inference employs a density model $q$, from which samples are easy and efficient to draw, to approximate the target density. Two important ingredients for variational inference sampling include a distance metric between $q$ and $\hat{\mu}$ to identify good $q$ and the importance weight to account for the mismatch between the two distributions. Thus, in variational inference, one needs to access the explicit density of $q$, which restricts the possible parameterization of $q$. Indeed, explicit density models that provide samples and probability density such as Autoregressive models and normalizing flow are widely used in density estimation. However, such models impose special structural constraints on the representation of $q$. For instance, the expressive power of normalizing flows is constrained by the requirements that the induced map has to be bijective and its Jacobian needs to be easy-to-compute.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most MC methods generate samples by iteratively simulating a well-designed Markov chain (MCMC) or sampling ancestrally. Among them, Sequential Monte Carlo and its variants augmented with annealing trick are regarded as state-of-the-art in certain sampling tasks. Despite its popularity, MCMC methods may suffer from long mixing time. The short-run performance of MCMC can be difficult to analyze and samples often get stuck in local minima. There are some recent works exploring the possibility of incorporating neural networks to improve MCMC. However, evaluating existing MCMC empirically, not to say designing an objective loss function to train network-powered MCMC, is difficult. Most existing works in this direction focus only on designing data-aware proposals and training such networks can be challenging without expertise knowledge in sampling.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose an efficient sampler termed Path Integral Sampler (PIS) to generate samples by simulating a stochastic differential equation (SDE) in finite steps. Our algorithm is built on the Schrödinger bridge problem whose original goal was to infer the most likely evolution of a diffusion given its marginal distributions at two time points. With a proper prior diffusion model, this Schrödinger bridge framework can be adopted for the sampling task. Moreover, it can be reformulated as a stochastic control problem whose terminal cost depends on the target density $\hat{\mu}$ so that the diffusion under optimal control has terminal distribution $\hat{\mu}$. We model the control policy with a network and develop a method to train it gradually and efficiently. The discrepancy of the learned policy from the optimal policy also provides an evaluation metric for sampling performance. Furthermore, PIS can be made unbiased even with sub-optimal control policy via the path integral theorem to compute the importance weights of samples. Compared with VI that uses explicit density models, PIS uses an implicit model and has the advantage of free-form network design.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The explicit density models have weaker expressive power and flexibility compared with implicit models, both theoretically and empirically. Compared with MCMC, PIS is more efficient and is able to generate high-quality samples with fewer steps. Besides, the behavior of MCMC over finite steps can be analyzed and quantified. We provide explicit sampling quality guarantee in terms of Wasserstein distance to the target density for any given sub-optimal policy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our algorithm is based on Tzen & Raginsky, where the authors establish the connections between generative models with latent diffusion and stochastic control and justify the expressiveness of such models theoretically. How to realize this model with networks and how the method performs on real datasets are unclear in Tzen & Raginsky. Another closely related work is Wu et al.; Arbel et al., which extends Sequential Monte Carlo (SMC) by combining deterministic normalizing flow blocks with stochastic MCMC blocks. To be able to evaluate the importance weights efficiently, MCMC blocks need to be chosen based on annealed target distributions carefully. In contrast, in PIS one can design expressive architecture freely and train the model end-to-end without the burden of tuning MCMC kernels, resampling or annealing scheduling. We summarize our contributions as follows. 1). We propose Path Integral Sampler, a generic sampler that generates samples through simulating a target-dependent SDE which can be trained with free-form architecture network design. We derive performance guarantee in terms of the Wasserstein distance to the target density based on the optimality of the learned SDE. 2).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

An evaluation metric is provided to quantify the performance of learned PIS. By minimizing such evaluation metric, PIS can be trained end-to-end. This metric also provides an estimation of the normalization constants of target distributions. 3). PIS can generate samples without bias even with sub-optimal SDEs by assigning importance weights using path integral theory. 4). Empirically, PIS achieves the state-of-the-art sampling performance in several sampling tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sampling and stochastic control problems", "weight": 1.0} -->

We begin with a brief introduction to the sampling problem and the stochastic control problem. Throughout, we denote by $\tau = {\{{{\mathbf{x}_{t},0} \leq t \leq T}\}}$ a continuous-time stochastic trajectory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sampling problems", "weight": 1.0} -->

We are interested in drawing samples from a target distribution ${\mu{(\mathbf{x})}} = {{\hat{\mu}{(\mathbf{x})}}/Z}$ in ${\mathbf{R}}^{d}$ where $Z$ is the normalization constant. Many sampling algorithms rely on constructing a stochastic process that drives the random particles from an initial distribution $\nu$ that is easy to sample, to the target distribution $\mu$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sampling problems", "weight": 1.0} -->

In the variational inference framework, one seeks to construct a parameterized stochastic process to achieve this goal. Denote by $\Omega = {C{({\lbrack 0,T\rbrack};{\mathbf{R}}^{d})}}$ the path space consisting of all possible trajectories and by $\mathcal{P}$ the measure over $\Omega$ induced by a stochastic process with terminal distribution $\mu$ at time $T$. Let $\mathcal{Q}$ be the measure induced by a parameterized stochastic and denote its marginal distribution at $T$ by $\mu^{\mathcal{Q}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling problems", "weight": 1.0} -->

Then, by the data processing inequality, the Kullback-Leibler divergence (KL) between marginal distributions $\mu^{Q}$ and $\mu$ can be bounded by Thus, $D_{KL}{({\mathcal{Q} \parallel \mathcal{P}})}$ serves as a performance metric for the sampler, and a small $D_{KL}{({\mathcal{Q} \parallel \mathcal{P}})}$ value corresponds to a good sampler.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stochastic control", "weight": 1.0} -->

Consider a model characterized by a special stochastic differential equation (SDE) where $\mathbf{x}_{t},\mathbf{u}_{t}$ denote state and control input respectively, and $\mathbf{w}_{t}$ denotes standard Brownian motion. In stochastic control, the goal is to find an feedback control strategy that minimizes a certain given cost function.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stochastic control", "weight": 1.0} -->

The standard stochastic control problem can be associated with any cost and any dynamics. In this work, we only consider cost of the form where $\Psi$ represents the terminal cost. The corresponding optimal control problem can be solved via dynamic programming, which amounts to solving the Hamilton-Jacobi-Bellman (HJB) equation The space-time function $V_{t}{(\mathbf{x})}$ is known as cost-to-go function or value function. The optimal policy can be computed from $V_{t}{(\mathbf{x})}$ as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Path Integral Sampler", "weight": 1.0} -->

It turns out that, with a proper choice of initial distribution $\nu$ and terminal loss function $\Psi$, the stochastic control problem coincides with sampling problem, and the optimal policy drives samples from $\nu$ to $\mu$ perfectly. The process under optimal control can be viewed as the posterior of uncontrolled dynamics conditioned on target distribution as illustrated in Fig 1. Throughout, we denote by $\mathcal{Q}^{u}$ the path measure associated with control policy $\mathbf{u}$. We also denote by $\mu^{0}$ the terminal distribution of the uncontrolled process $\mathcal{Q}^{0}$. For the ease of presentation, we begin with sampling from a normalized density $\mu$, and then generalize the results to unnormalized $\hat{\mu}$ in Section 3.4.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Path Integral and value function", "weight": 1.0} -->

Thanks to the special cost structure, the nonlinear HJB eq 4 can be transformed into a linear partial differential equation (PDE) by logarithmic transformation ${V_{t}{(\mathbf{x})}} = {- {{\log\phi_{t}}{(\mathbf{x})}}}$. By the celebrated Feynman-Kac formula, the above has solution We remark that eq 7 implies that the optimal value function can be evaluated without knowing the optimal policy since the above expectation is with respect to the uncontrolled process $\mathcal{Q}^{0}$. This is exactly the Path Integral control theory. Furthermore, the optimal control at $(t,\mathbf{x})$ is meaning that $\mathbf{u}_{t}^{\ast}{(\mathbf{x})}$ can also be estimated by uncontrolled trajectories.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sampling as a stochastic optimal control problem", "weight": 1.0} -->

There are infinite choices of control strategy $\mathbf{u}$ such that eq 2 has terminal distribution $\mu$. We are interested in the one that minimizes the KL divergence to the prior uncontrolled process. This is exactly the Schrödinger bridge problem, which has been shown to have a stochastic control formulation with cost being control efforts. In cases where $\nu$ is a Dirac distribution, it is the same as the stochastic control problem in Section 2.2 with a proper terminal cost as characterized in the following result.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

Optimal Policy Representation: Consider the sampling strategy from a given target density by simulating SDE in eq 2 under optimal control. Even though the optimal policy is characterized by eq 8, only in rare case (Gaussian target distribution) it has an analytic closed-form.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

For more general target distributions, we can instead evaluate the value function eq 7 via empirical samples using Monte Carlo. The approach is essentially importance sampling whose proposal distribution is the uncontrolled dynamics. However, this approach has two drawbacks. First, it is known that the estimation variance can be intolerably high when the proposal distribution is not close enough to the target distribution. Second, even if the variance is acceptable, without a good proposal, the required samples size increases exponentially with dimension, which prevents the algorithm from being used in high or even medium dimension settings.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

To overcome the above shortcomings, we parameterize the control policy with a neural network $\mathbf{u}_{\theta}$. We seek a control policy that minimizes the cost The formula eq 14 also serves as distance metric between $\mathbf{u}_{\theta}$ and $\mathbf{u}^{\ast}$ as in eq 13.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

Gradient-informed Policy Representation: It is believed that proper prior information can significantly boost the performance of neural network. The score ${{\nabla\log}\mu}{(\mathbf{x})}$ has been used widely to improve the proposal distribution in MCMC and often leads to better results compared with proposals without gradient information. In the same spirit, we incorporate ${{\nabla\log}\mu}{(\mathbf{x})}$ and parameterize the policy as where $\text{NN}_{1}$ and $\text{NN}_{2}$ are two neural networks. Empirically, we also found that the gradient information leads to faster convergence and smaller discrepancy $D_{KL}{({\mathcal{Q}^{u} \parallel \mathcal{Q}^{\ast}})}$. We remark that PIS with policy eq 15 can be viewed as a modulated Langevin dynamics that achieves $\mu$ within finite time $T$ instead of infinite time.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

Optimize Policy: Optimizing $\mathbf{u}_{\theta}$ requires the gradient of loss in eq 14, which involves $\mathbf{u}_{t}$ and the terminal state $\mathbf{x}_{T}$. To calculate gradients, we rely on backpropagation through trajectories. We train the control policy with recent techniques of Neural SDEs, which greatly reduce memory consumption during training. The gradient computation for Neural SDE is based on stochastic adjoint sensitivity, which generalizes the adjoint sensitivity method for Neural ODE. Therefore, the backpropagation in Neural SDE is another SDE associated with adjoint states. Unlike the training of traditional deep MLPs which often runs into gradient vanishing/exploding issues, the training of Neural SDE/ODE is more stable and not sensitive the number of discretization steps. We augment the origin SDE with state $\int_{0}^{t}{\frac{1}{2}\left.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

\parallel\mathbf{u}_{s}\parallel \right.^{2}{ds}}$ such that the whole training can be conducted end to end. The full training procedure in provided in Algorithm 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

\parallel{\mathbf{u}_{\thetat}{(\mathbf{x}_{t})}}\parallel \right.^{2}}\rbrack}$, diffusion g (t, [xt, yt]) = xT, yT = sdeint (f, g, [x0, y0], [0, T]) # Integrate SDE from 0 to T with Neural SDE Gradient descent step $\nabla_{\theta}{\lbrack{y_{T} + {\log\frac{\mu^{0}{(\mathbf{x}_{T})}}{\mu{(\mathbf{x}_{T})}}}}\rbrack}$ # Optimize control policy Wasserstein distance bound: The PIS trained by Algorithm 1 can not generate unbiased samples from the target distribution $\mu$ for two reasons. First, due to the non-convexity of networks and randomness of stochastic gradient descent, there is no guarantee that the learned policy is optimal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimal control policy and sampler", "weight": 1.0} -->

Second, even if the learned policy is optimal, the time-discretization error in simulating SDEs is inevitable. Fortunately, the following theorem quantifies the Wasserstein distance between the sampler and the target density. (More details and a formal statement can be found in appendix C)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

The training procedure for PIS does not guarantee its optimality. To compensate for the mismatch between the trained policy and the optimal policy, we introduce importance weight to calibrate generated samples. The importance weight can be calculated by (more details in appendix B) Input: Vector: x0 = 0, Scalar: y0 = 0 Output: Samples with weights $y_{i} = {y_{i - 1} + {\mathbf{u}'\Delta\mathbf{w}} + {\frac{1}{2}\left.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

\parallel\mathbf{u}\parallel \right.^{2}\Deltat}}$ Outputs: $\mathbf{x}_{N},{\exp{({{- y_{N}} - {\log\frac{\mu^{0}{(\mathbf{x}_{N})}}{\mu{(\mathbf{x}_{N})}}}})}}$ We note eq 17 resembles training objective eq 14. Indeed, eq 14 is the average of logarithm of eq 17. If the trained policy is optimal, that is, $\mathcal{Q}^{u} = \mathcal{Q}^{\ast}$, all the particles share the same weight. We summarize the sampling algorithm in Algorithm 2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Importance Sampling", "weight": 1.0} -->

Effective Sample Size: The Effective Sample Size (ESS), $\text{ESS}^{u} = \frac{1}{{\mathbb{E}}_{\mathcal{Q}^{u}}{\lbrack{(w^{u})}^{2}\rbrack}}$, is a popular metric to measure the variance of importance weights. ESS is often accompanied by resampling trick to mitigate deterioration of sample quality. ESS is also regarded as a metric for quantifying goodness of sampler based on importance sampling. Low ESS means that estimation or downstream tasks based on such sampling methods may suffer from a high variance. ESS of most importance samplers is decreasing along the time. Thanks to the adaptive control policy in PIS, we can quantify the ESS of PIS based on the optimality of learned policy. For the sake of completeness, the proof in provided in appendix D.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we present empirical evaluations of PIS and the comparisons to several baselines. We also provide details of practical implementations. Inspired by Arbel et al., we conduct experiments for tasks of Bayesian inference and normalization constant estimation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider three types of relevant methods. The first category is gradient-guided MCMC methods without the annealing trick. It includes the Hamiltonian Monte Carlo (HMC) and No-U-Turn Sampler (NUTS). The second is Sequential Monte Carlo with annealing trick (SMC), which is regarded as state-of-the-art sampling algorithm in terms of sampling quality. We choose a standard instance of SMC samplers and the recently proposed Annealed Flow Transport Monte Carlo (AFT). Both use a default 10 temperature levels with a linear annealing scheme. We note that there are optimized SMC variants that achieve better performance. Since the introduction of advanced tricks, we exclude the comparison with those variants for fair comparison purpose. We note PIS can also be augmented with annealing trick, possible improvement for PIS can be explored in the future. Last, the variational normalizing flow (VI-NF) is also included for comparison. We note that another popular line of sampling algorithms use Stein-Variational Gradient Descent (SVGD) or other particle-based variational inference approaches. We include the comparison and more discussions on SGVD in Section F.4 due to its significant difference.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

In our experiments, the number of steps $N$ of MCMC algorithms and the number of SDE time-discretization steps for PIS work as a proxy for benchmarking computation times.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also investigate the effects of two different network architectures for Path Integral Sampler. The first one is a time-conditioned neural network without any prior information, which we denote as PIS-NN, while the second one incorporates the gradient information of the given energy function as in eq 15, denoted as PIS-Grad. When we have an analytical form for the ground truth optimal policy, the policy is denoted as PIS-GT. The subscript RW is to distinguish PIS with path integral importance weights eq 17 that use eq 19 to estimate normalization constants from the ones without importance weights that use the bound in eq 18 to estimate $Z$. For approaches without the annealing trick, we take default $N = 100$ unless otherwise stated. With annealing, $N$ steps are the default for each temperature level, thus AFT and SMC rougly use 10 times more steps compared with HMC and PIS. We include more details about hyperparameters, training time, sampling efficiency, and more experiments with large $N$ in appendices F and G.

<!-- chunk {"id": "body-0034", "role": "body", "section": "PIS-Grad vs PIS-NN: Importance of gradient guidance", "weight": 1.0} -->

We observed that the advantage of PIS-Grad over PIS-NN is clearer when the target density has multiple modes as in the toy example shown in Fig 2. The objective $D_{KL}{({\mathcal{Q} \parallel \mathcal{Q}^{\ast}})}$ is known to have zero forcing. In particular, when the modes of the density are well separated and $\mathcal{Q}$ is not expressive enough, minimizing $D_{KL}{({\mathcal{Q} \parallel \mathcal{Q}^{\ast}})}$ can drive $\mathcal{Q}{(\tau)}$ to zero on some area, even if ${\mathcal{Q}^{\ast}{(\tau)}} > 0$. PIS-NN and VI-NF generate very similar samples that almost cover half the inner ring. The training objective function of VI-NF can also be viewed as minimizing KL divergence between two trajectory distributions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "PIS-Grad vs PIS-NN: Importance of gradient guidance", "weight": 1.0} -->

The added noise during the process can encourage exploration but it is unlikely such noise only can overcome the local minima. On the other hand, the gradient information can help cover more modes and provide exploring directions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Benchmarking datasets", "weight": 1.0} -->

Mode-separated mixture of Gaussian: We consider the mixture of Gaussian in 2-dimension. We notice that when the Gaussian modes are not far away from each other, all methods work well. However, when we reduce the variances of the Gaussian distributions and separate the modes of Gaussian, the advantage of PIS becomes clear even in this low dimension task. We generate 2000 samples from each method and plot their kernel density estimate (KDE) in Fig 4. PIS generates samples that are visually indistinguishable from the target density.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Benchmarking datasets", "weight": 1.0} -->

Funnel distribution: We consider the popular testing distribution in MCMC literature, the 10-dimensional Funnel distribution charaterized by This distribution can be pictured as a funnel - with $x_{0}$ wide at the mouth of funnel, getting smaller as the funnel narrows.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Benchmarking datasets", "weight": 1.0} -->

Log Gaussian Cox Process: We further investigate the normalization constant estimation problem for the challenging log Gaussian Cox process (LGCP), which is designed for modeling the positions of Finland pine saplings. In LGCP, an underlying field $\lambda$ of positive real values is modeled using an exponentially-transformed Gaussian process. Then $\lambda$ is used to parameterize Poisson points process to model locations of pine saplings. The posterior density is where $d$ denotes the size of discretized grid and $y_{i}$ denotes observation information. The modeling parameters, including normal distribution and $\alpha$, follow Arbel et al. (See appendix F).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Benchmarking datasets", "weight": 1.0} -->

Tab 1 clearly shows the advantages of PIS for the above three datasets, and supports the claim that importance weight helps improve the estimation of log normalization constants, based on the comparison between PIS~RW~ and PIS. We also found that PIS-Grad trained with gradient information outperforms PIS-NN. The difference is more obvious in datasets that have well-separated modes, such as MG and LGCP, and less obvious on unimodal distributions like Funnel.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Benchmarking datasets", "weight": 1.0} -->

In all cases, PIS~RW~-Grad is better than AFT and SMC. Interestingly, even without annealing and gradient information of target density, PIS~RW~-NN can outperform SMC with annealing trick and HMC kernel for the Funnel distribution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Advantage of the specialized sampling algorithm", "weight": 1.0} -->

From the perspective of particles dynamics, most existing MCMC algorithms are invariant to the target distribution. Therefore, particles are driven by gradient and random noise in a way that is independent of the given target distribution. In contrast, PIS learns different strategies to combine gradient information and noise for different target densities. The specialized sampling algorithm can generate samples more efficiently and shows better performance empirically in our experiments. The advantage can be showed in various datasets, from unimodal distributions like the Funnel distribution to multimodal distributions. The benefits and efficiency of PIS are more obvious in high dimensional settings as we have shown.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Alanine dipeptide", "weight": 1.0} -->

Building on the success achieved by flow models in the generation of asymptotically unbiased samples from physics models, we investigate the applications in the sampling of molecular structure from a simulation of Alanine dipeptide as introduced in Wu et al.. The target density of molecule is $\hat{\mu} = {\exp{({{- {E{(\mathbf{x}_{\lbrack{0:65}\rbrack})}}} - {\frac{1}{2}\left. \parallel\mathbf{x}_{\lbrack{66:131}\rbrack}\parallel \right.^{2}}})}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Alanine dipeptide", "weight": 1.0} -->

We compare PIS with popular variational approaches used in generating samples from the above model. More specifically, we consider VI-NF, and Stochastic Normalizing Flow (SNF). SNF is very close to AFT. Both of them couple deterministic normalizing flow layers and MCMC blocks except SNF uses an amortized structure. We include more details of MCMC kernel and modification in appendix F.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sampling in Variational Autoencoder latent space", "weight": 1.0} -->

In this experiment we investigate sampling in the latent space of a trained Variational Autoencoder (VAE). VAE aims to minimize $D_{KL}{(q{(\mathbf{x})}q_{\phi}{(\mathbf{z}|\mathbf{x})} \parallel p{(\mathbf{z})}p_{\theta}{(\mathbf{x}|\mathbf{z})})}$, where $q_{\phi}{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ represents encoder and $p_{\theta}$ for a decoder with latent variable $\mathbf{z}$ and data $\mathbf{x}$. We investigate the posterior distribution The normalization constant of such target unnormalized density function $p{(\mathbf{z})}p_{\theta}{(\left.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Sampling in Variational Autoencoder latent space", "weight": 1.0} -->

\mathbf{x} \middle| \mathbf{z} \right.)}$ is exactly the likelihood of data points $p_{\theta}{(\mathbf{x})}$, which serves as an evaluation metric for the trained VAE. $\sqrt{\text{B}^{2} + \text{S}^{2}}$ Table 3: Estimation of log pθ (x) of a trained VAE.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Sampling in Variational Autoencoder latent space", "weight": 1.0} -->

We investigate a vanilla VAE model trained with plateau loss on the binary MNIST dataset. For each distribution, we regard the average estimation from 10 long-run SMC with 1000 temperature levels as the ground truth normalization constant. We choose 100 images randomly and run the various approaches on estimating normalization of those posterior distributions in eq 21 and report the average performance in Tab 3. PIS has a lower bias and variance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Contributions. In this work, we proposed a new sampling algorithm, Path Integral Sampler, based on the connections between sampling and stochastic control. The control can drive particles from a simple initial distribution to a target density perfectly when the policy is optimal for an optimal control problem whose terminal cost depends on the target distribution. Furthermore, we provide a calibration based on importance weights, ensuring sampling quality even with sub-optimal policies.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations. Compared with most popular non-learnable MCMC algorithms, PIS requires training neural networks for the given distributions, which adds additional computational overhead, though this can be mitigated with amortization. Besides, the sampling quality of PIS in finite steps depends on the optimality of trained network. Improper choices of hyperparameters may lead to numerical issues and failure modes as discussed in Section G.2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reproducibility Statement", "weight": 1.0} -->

The detailed discussions on assumptions and proofs of theorems presented in the main paper are included in appendices A, C, D and E. The training settings and implementation tips of the algorithms are included in appendices F and G. An implementation based on PyTorch of PIS can be found in
