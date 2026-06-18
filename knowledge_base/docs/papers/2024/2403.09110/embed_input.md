<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SINDy-RL: Interpretable and Efficient Model-Based Reinforcement Learning

Topics include Reinforcement learning, SINDy, Model-based reinforcement learning, Interpretable artificial intelligence, Data-driven methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines SINDy with model-based RL: a SINDy surrogate world model replaces the environment for policy training, yielding interpretable dynamics models and improved sample efficiency compared to black-box neural network surrogates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep reinforcement learning (DRL) has shown significant promise for uncovering sophisticated control policies that interact in complex environments, such as stabilizing a tokamak fusion reactor or minimizing the drag force on an object in a fluid flow. However, DRL requires an abundance of training examples and may become prohibitively expensive for many applications. In addition, the reliance on deep neural networks often results in an uninterpretable, black-box policy that may be too computationally expensive to use with certain embedded systems. Recent advances in sparse dictionary learning, such as the sparse identification of nonlinear dynamics (SINDy), have shown promise for creating efficient and interpretable data-driven models in the low-data regime. In this work, we introduce SINDy-RL, a unifying framework for combining SINDy and DRL to create efficient, interpretable, and trustworthy representations of the dynamics model, reward function, and control policy.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the effectiveness of our approaches on benchmark control environments and flow control problems, including gust mitigation on a 3D NACA 0012 airfoil at Re = 1000. SINDy-RL achieves comparable performance to modern DRL algorithms using significantly fewer interactions in the environment and results in an interpretable control policy orders of magnitude smaller than a DRL policy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

Deep reinforcement learning (DRL) has shown significant promise for uncovering sophisticated control policies that interact in complex environments, such as stabilizing a tokamak fusion reactor or minimizing the drag force on an object in a fluid flow. However, DRL requires an abundance of training examples and may become prohibitively expensive for many applications. In addition, the reliance on deep neural networks often results in an uninterpretable, black-box policy that may be too computationally expensive to use with certain embedded systems. Recent advances in sparse dictionary learning, such as the sparse identification of nonlinear dynamics (SINDy), have shown promise for creating efficient and interpretable data-driven models in the low-data regime. In this work we introduce SINDy-RL, a unifying framework for combining SINDy and DRL to create efficient, interpretable, and trustworthy representations of the dynamics model, reward function, and control policy. We demonstrate the effectiveness of our approaches on benchmark control environments and flow control problems, including gust mitigation on a 3D NACA 0012 airfoil at ${Re} = 1000$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

SINDy-RL achieves comparable performance to modern DRL algorithms using significantly fewer interactions in the environment and results in an interpretable control policy orders of magnitude smaller than a DRL policy.\

<!-- chunk {"id": "body-0007", "role": "body", "section": "Abstract", "weight": 1.5} -->

Keywords: reinforcement learning, sparse identification of nonlinear dynamics, model-based RL, deep reinforcement learning

<!-- chunk {"id": "body-0008", "role": "body", "section": "Abstract", "weight": 1.5} -->

^11^footnotetext: Corresponding author (nzolman@uw.edu)

<!-- chunk {"id": "body-0009", "role": "body", "section": "Abstract", "weight": 1.5} -->

Much of the success of modern technology can be attributed to our ability to control dynamical systems: designing safe biomedical implants for homeostatic regulation, gimbling rocket boosters for reusable launch vehicles, operating power plants and power grids, industrial manufacturing, among many other examples. Recently, advances in machine learning and optimization have rapidly accelerated our ability to tackle complicated data-driven tasks---particularly in the fields of computer vision and natural language processing. Reinforcement learning (RL) is at the intersection of both machine learning and optimal control, and the core ideas of RL date back to the infancy of both fields. An RL agent iteratively improves its control policy by interacting with an environment and receiving feedback about its performance on a task through a reward. Deep reinforcement learning (DRL) has shown particular promise for uncovering control policies in complex, high-dimensional spaces. DRL has been used to achieve super-human performance in games and drone racing, to control the plasma dynamics in a tokamak fusion reactor, to discover novel drugs, and for many applications in fluid mechanics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Abstract", "weight": 1.5} -->

However, these methods rely on neural networks and typically suffer from three major drawbacks: they are infeasible to train for many applications because they require millions---or even billions ---of interactions with the environment; they are challenging to deploy in resource-constrained environments (such as embedded devices and micro-robotic systems) due to the size of the networks and need for specialized software; and they are "black-box" models that lack interpretability, making them untrustworthy to operate in safety-critical systems or high-consequence environments. In this work we improve the sample efficiency of reinforcement learning algorithms, even for high-dimensional problems, by leveraging sparse dictionary learning. Specifically, we build small, interpretable surrogate models for the environment dynamics, reward, and policy.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Abstract", "weight": 1.5} -->

There has been significant research into reducing the amount of experience needed to train RL policies, such as offline RL, experience replay methods, transfer learning, and meta-learning. Training in a low-fidelity representation of the environment is perhaps the most common way to reduce the number of interactions in a full-order environment. However, there are many cases where an analytic reduced-order model does not exist and the dynamics must be learned from data to create a surrogate representation of the environment. Dyna-style model-based reinforcement learning (MBRL) algorithms iteratively switch between learning and improving a surrogate model of the environment and training model-free policies inside the surrogate environment by generating "imaginary" experience. Deep MBRL algorithms have shown significant promise for reducing sample complexity on benchmark environments by simultaneously training neural network models of the environment. Although neural network models have recently become popular and are gaining wide adoption over traditional modeling methods, they are still overparameterized, data-inefficient, and uninterpretable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Abstract", "weight": 1.5} -->

In contrast, sparse dictionary learning provides an efficient and interpretable alternative to learn models from data, as in the sparse identification of nonlinear dynamics (SINDy). Sparse dictionary learning is a type of symbolic regression that learns a representation of a function as a sparse linear combination of pre-chosen candidate dictionary (or "library") functions. A sparse, symbolic model lends itself naturally to interpretation and analysis---especially for physical systems where the dictionary terms have physical meaning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Abstract", "weight": 1.5} -->

Importantly, SINDy has been extended to systems with control and used to design model predictive control (MPC) laws. SINDy methods are incredibly efficient---both for model creation and deployment---making them promising for both online learning and resource-constrained control. In particular, SINDy has been used for online simultaneous dynamics discovery and optimal control. Recent work used a single SINDy model to accelerate DRL and demonstrated its use on simple DRL benchmarks. In this work, we generalize this DRL framework to include ensembles of dictionary models of both the dynamics and reward to accelerate learning in the low-data limit and quantify uncertainty.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

In this work, we develop methods at the intersection of sparse dictionary learning and DRL for creating trustworthy, interpretable, efficient, and generalizable models that operate in the low-data limit. Building on recent advances in ensemble dictionary learning, we first introduce a Dyna-style MBRL algorithm that fits an ensemble of SINDy models to approximate an environment's dynamics and uses modern model-free reinforcement learning to train agents in the surrogate environments. In systems where the reward is difficult to measure directly from the observed state (e.g. limited sensor information for flow control on an aircraft), we augment the Dyna-style algorithm by learning an ensemble of sparse dictionary models to form a surrogate reward function. Finally, after training a DRL policy, we use an ensemble of dictionary models to learn a lightweight, symbolic policy, which can be readily transferred to an embedded system. Figure provides a schematic of the SINDy-RL framework. We evaluate our methods on benchmark environments for continuous control from mechanical systems using the dm_control and gymnasium suites as well as fluid systems from HydroGym and HydroGym-GPU.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Improve sample efficiency by orders of magnitude for training a control policy by leveraging surrogate experience in an E-SINDy model of the environment.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Leverage the efficiency of the surrogate models to accelerate expensive hyperparameter tuning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Learn a surrogate reward when the reward is not directly measurable from observations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Reduce the complexity of a neural network policy by learning a sparse, symbolic surrogate policy, with comparable performance and smoother control.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Quantify the uncertainty of models and provide insight into the quality of the learned models.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

By leveraging sparse dictionary learning in combination with deep reinforcement learning, it can become feasible to rapidly train control policies in expensive, data-constrained environments while simultaneously obtaining interpretable representations of the dynamics, reward, and control policy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

Reinforcement learning (RL) comprises a family of methods where an agent learns a policy, $\pi$, to perform a task through repeated interaction with an environment, $\mathcal{E}$. Explicitly, at each environment state $\mathbf{x}$, the agent samples an action $\mathbf{u}_{n} \sim {\pi{(\mathbf{x}_{n})}}$ and executes it in the environment, producing a new state $\mathbf{x}_{n + 1}$ and reward $r_{n}$---an indication of how well the agent performed at that time. We define the value function to be the expected future return for taking actions from the policy, ${V_{\pi}{(\mathbf{x})}} = {{\mathbb{E}}\left( {\left. {\sum_{k = 0}^{\infty}{\gamma^{k}r_{k}}} \middle| \mathbf{x}_{0} \right.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

= \mathbf{x}} \right)}$ where $0 < \gamma \leq 1$ is the discount factor. RL methods seek a policy that maximizes this quantity, which can be a very challenging optimization problem, especially in the case of high-dimensional state-spaces, continuous action spaces, and nonlinear dynamics. Deep reinforcement learning (DRL) has made significant progress in addressing these problems by parameterizing functions as deep neural networks (DNNs), such as the policy ${\pi{(\mathbf{x})}} \approx {\pi_{\phi}{(\mathbf{x})}}$, and training on collected experiences.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dictionary Learning", "weight": 1.0} -->

to form the linear model $\mathbf{Y} = {\mathbf{\Theta}{(\mathbf{X})}\mathbf{\Xi}}$, where $\mathbf{\Xi} \in {\mathbb{R}}^{d \times n}$ are the coefficients to be fit. Sparse dictionary learning assumes that the desired function can be well approximated by a small subset of terms in the library, i.e. $\mathbf{\Xi}$ is a sparse matrix. For dynamics discovery, such as SINDy (where $\mathbf{y} = {\frac{d}{dt}\mathbf{x}}$), a sparse library is physically motivated by the observation that the governing equations for most physical systems have relatively few terms.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dictionary Learning", "weight": 1.0} -->

where $|| \cdot ||_{F}$ is the Frobenius norm and $\mathcal{R}{(\mathbf{\Xi})}$ is a sparsity-promoting regularization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dictionary Learning", "weight": 1.0} -->

Ensemble-SINDy (E-SINDy) introduced a way to select a model from an ensemble of SINDy models and is more robust to noise than SINDy, particularly in the low-data limit. E-SINDy can be generalized to arbitrary dictionary models by considering ensembles: $\mathbf{Y}^{(k)} = {\mathbf{\Theta}^{(k)}{(\mathbf{X}^{(k)})}\mathbf{\Xi}^{(k)}}$, for $k = {1\ldotsN_{e}}$. Treating the coefficients, $\mathbf{\Xi}$, as random variables, the ensemble acts as an empirical approximation for the distribution of likely $\mathbf{\Xi}$ values. From this, one can derive an efficient framework for analytically approximating a model's pointwise variance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dictionary Learning", "weight": 1.0} -->

It is important to note that there have been many proposed variants of SINDy to make the algorithm more robust. These methods are generally compatible---if not synergetic---with E-SINDy; we therefore only present the simplest formulation in this work, though a practitioner may seek to amend our framework with a more specialized variant to best suit their purpose.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SINDy-RL: Sparse Dictionary Learning for RL", "weight": 1.0} -->

In this work, we introduce SINDy-RL, a unifying perspective for applying sparse dictionary learning to DRL control tasks. We separately approximate the environment dynamics, reward function, and the final learned neural network policy using ensemble sparse dictionary learning. We frequently use the "hat" notation to indicate a surrogate approximation of a function, i.e. ${\hat{f}{(x)}} \approx {f{(x)}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SINDy-RL: Sparse Dictionary Learning for RL", "weight": 1.0} -->

Input: ℰ ⊳ full-order environment Noff, Ncollect ⊳ # of off- and on-line policy steps nbatch ⊳ # of policy iters / SINDy update Θ ⊳ dictionary functions 𝒜 ⊳ policy optimization algorithm π0 ⊳ default policy
Step 1: Initialize Surrogate Environment
𝒟off = CollectData(ℰ, π0, Noff)
$\hat{\mathcal{E}}$ = Surrogate(Ξ)
Step 2: Model Improvement
while not done: do
π = $\mathcal{A}{(\hat{\mathcal{E}},\pi,n_{\text{batch}})}$
$\hat{\mathcal{E}}$ = Surrogate(Ξ)
Output:Optimized policy, π, and SINDy environment, $\hat{\mathcal{E}}$.
Algorithm 1 (Dyna-style SINDy-RL)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Approximating Dynamics", "weight": 1.0} -->

We propose a Dyna-style MBRL algorithm where we iteratively improve a dynamics model and learned policy. First, we collect offline data samples from the full-order environment by deploying a default policy \], etc.). We use the collected data to fit an ensemble of SINDy models to initialize a surrogate environment. Next we iteratively train a policy for a fixed number of policy updates using the surrogate environment with a policy optimization algorithm, such as proximal policy optimization, (PPO). By forcing the agent to only interact in the surrogate environment, we offload the majority of the expensive sample collection to the lightweight E-SINDy surrogate. Finally, we deploy the trained policy to the full-order environment and collect data for evaluation and use the newly collected data to update the E-SINDy models. We repeat this process, iteratively updating and improving both the E-SINDy model and policy. In this work, we specify a fixed number of policy iterations before evaluating the agent, though a practitioner may consider an adaptive number of updates based on training metrics in the surrogate environment. A full summary of this process can be found in Algorithm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Approximating Dynamics", "weight": 1.0} -->

Each dynamics model in the ensemble is fit using SINDy with control (SINDy-C) and STRidge. Either a continuous or discrete model can be fit; however, we learn discrete-time models where next-step updates are predicted explicitly, rather than integrating a continuous-time model forward in time, for ease of deploying in the environment. It is common for nonlinear dynamics models---especially learned models---to grow unbounded over long time horizons unless stability guarantees are enforced. To accommodate this limitation, we bound the state space and reset the surrogate environment during training if a trajectory exits the bounding box.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Approximating Rewards", "weight": 1.0} -->

For Dyna-style MBRL, it is assumed that the reward function can be directly evaluated from observations of the environment. However, there are cases in which the reward function cannot be readily evaluated because the system may only be partially observable due to missing sensor information---as is the case in many fluids systems. There has been significant work on creating proxy rewards for controls tasks using reward shaping and learning an objective function through inverse reinforcement learning. We propose learning a proxy reward, $\hat{R}{(\mathbf{x}_{k + 1},\mathbf{u}_{k})}$, with supervised sparse dictionary learning when there are offline evaluations of the reward available: $r_{k} = {R{(\mathbf{x}_{k + 1},\mathbf{u}_{k})}}$. Our implementation uses sparse ensemble dictionary learning under the assumption that there is a sparse deterministic relationship between the reward function and observations from the environment. We incorporate this into Algorithm by learning the reward function alongside the dynamics to create the surrogate environment.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Approximating Policies", "weight": 1.0} -->

Taking inspiration from behavior cloning algorithms in imitation learning, we fit a sparse dictionary model approximation of the final learned policy, $\pi_{\phi}$. While imitation learning attempts to mimic the policy of an expert actor with a neural network student, we instead use the learned neural network as our expert and the dictionary model as our student, resulting in a lightweight, symbolic approximation. A dictionary model is not as expressive as a neural network; however, there has been previous work indicating that even limiting to purely linear policies can be a competitive alternative to deep policy networks, showing that even complicated control tasks may have a simple controller. Likewise, there has been recent investigation into approximating neural networks with polynomials through Taylor expansion, which have shown to provide sufficiently robust approximations. These reduced representations can be orders of magnitude smaller than a fully-connected neural network and they can be efficiently implemented and deployed to resource-constrained environments, such as embedded systems.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Approximating Policies", "weight": 1.0} -->

Many model-free algorithms assume a stochastic policy for optimally interacting with a stochastic environment and encouraging exploration; we proceed with a sparse ensemble fit of the expectation: ${\hat{\pi}{(\mathbf{x})}} \approx {{\mathbb{E}}{\lbrack{\pi_{\phi}{(\mathbf{x})}}\rbrack}}$. Because there is no temporal dependence on $\pi_{\phi}$, we can assemble our data and label pairs $(\mathbf{x},{{\mathbb{E}}{\lbrack{\pi_{\phi}{(\mathbf{x})}}\rbrack}})$ by evaluating $\pi_{\phi}$ for any $\mathbf{x}$. To build such a dataset, we sample points from trajectories of the agent interacting in the environment, ensuring that the states are directly relevant to the controls task.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Approximating Policies", "weight": 1.0} -->

To avoid the cost of collecting more data from the full-order environment, $\mathcal{E}$, we propose sampling new trajectories from a learned ensemble of dynamics models. Explicitly, we sample $N_{\tau}$ trajectories by propagating the E-SINDy model

<!-- chunk {"id": "body-0035", "role": "body", "section": "Approximating Policies", "weight": 1.0} -->

and use the collected data $(\mathbf{x}_{k},\mathbf{u}_{k})$ from each $\tau$ to fit the dynamics model. During the DRL training, the neural network policy may overfit to specific regions of the space and bias our data collection; thus, we draw inspiration from tube MPC, where an MPC controller attempts to stay within some bounded region of a nominal trajectory. Instead of only sampling points from the surrogate trajectories, we can sample plausible points in a neighborhood of the trajectories to create a more accurate approximation while still avoiding regions of the space that can no longer be trusted.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate our methods on five environments depicted in Figure: dm_control swing-up balances a pole on a cart in the unstable upright position starting from the stable down position at rest, gymnasium Swimmer-v4 controls a 3-segment robot to travel as far as possible in the horizontal direction (along the $x$-axis) for a fixed time, HydroGym Cylinder reduces the drag force, $C_{D}$, of a rotating cylinder in an unsteady fluid flow at ${Re} = 100$ with measurements of the lift force, $C_{L}$, HydroGym Pinball reduces the net drag force $C_{D1} + C_{D2} + C_{D3}$ on the system of cylinders to stabilize the quasi-periodic flow at ${Re} = 100$, and HydroGym-GPU 3D Airfoil mitigates the effect of a large incoming gust in an unsteady flow at ${Re} = 1000$ by minimizing ${|{C_{L} - C_{L}^{ref}}|} +

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

For Pinball and 3D Airfoil, state information is obtained from a mesh of velocity probes in the flow, forming a 70- and 318-dimensional measurement space, respectively. This data is projected onto the leading singular value decomposition modes (SVD) and use the coefficients, $a_{i} = {\mathbf{v}_{i}^{T}\mathbf{x}}$, to form a 10- and 2-dimensional observation space for the respective systems. Details for each environment can be found in Supplementary §3. Whereas the swing-up reward is analytically expressible in terms of the observed variables, all other rewards are computed from environment information that cannot retrieved analytically from the observation. We treat the rewards as functions of the observations and actions by approximating them with an ensemble of sparse models.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

In Section 3.1, we use our method to train SINDy-RL agents using Dyna-style MBRL with surrogate dynamics and reward functions, and baseline sample efficiency against other approaches by comparing the amount data collected from the full-order environment. Sections 3.2 and 3.3 explore the evolution of the learned dynamics and rewards during training. In Section 3.4, we use the learned neural network policies from Algorithm to obtain surrogate dictionary policies. Finally, in Section, we examine how to quantify the variance of dictionary models and provide additional insight into learned models.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Benchmarking Sample Efficiency", "weight": 1.0} -->

For every algorithm and experiment, multiple independent instantiations are run to provide a distribution of performance across random seeds.^11^1Twenty instantiations were used for all environments, except 3D Airfoil where we are limited to four instantiations due to the computational demand of the environment. Specific details about the training, hyperparameters, and more can be found in Supplementary §4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Accelerating Training", "weight": 1.0} -->

In Figure, we compare our proposed SINDy-RL method from Algorithm with a quadratic dynamics library to four different baseline experiments: model-free proximal policy optimization (PPO), Algorithm with a linear SINDy library, Algorithm where SINDy models are replaced with neural network dynamics models (i.e. "Dyna-NN"), and RLlib's implementation of Model-Based Meta-Policy Optimization (MB-MPO). PPO is used as the policy optimization algorithm, $\mathcal{A}$, for all Dyna-style experiments with identical hyperparameters between comparisons. As shown in Figure, SINDy-RL with a quadratic library learns a control policy with $\mathbf{1}\mathbf{0}\mathbf{0} \times$ fewer interactions in the full-order environment compared to model-free RL and greatly outperforms other model-based approaches. The linear models are incapable of approximating the global dynamics since there are multiple fixed points.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Accelerating Training", "weight": 1.0} -->

In contrast, while neural network models should be more expressive, it appears that both the MB-MPO and Dyna-NN baselines fail to accurately capture the dynamics sufficient to achieve the task. For both comparisons, it is suspected that the dynamics may be captured with significantly larger data collections---as shown in previous work comparing SINDy with neural network models for MPC. An investigation of the $N_{\text{collect}}$ and $n_{\text{batch}}$ hyperparameters from our method can be found in Supplementary §4A.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Accelerating Training", "weight": 1.0} -->

The increased sample efficiency is particularly important for applications interacting with physical systems that require humans in-the-loop to monitor and reset environments or computationally expensive simulations---such as CFD solvers---that require significant time and resources to run. The benefits of reducing the sample efficiency can be seen using the fluid flow control environments. The 3D Airfoil environment uses the lattice Boltzmann method with over 72M cells, requiring 75GB of VRAM across four A100 GPUs. Even when using the GPUs, a single step in the full-order model takes on the order of 45s to update the environment. In comparison, the learned E-SINDy polynomials for the 3D Airfoil require less than 10kB of RAM on CPU, and a single step takes approximately 1-4 milliseconds using NumPy ---i.e. SINDy-RL experience collection is $\mathbf{1}\mathbf{0}^{\mathbf{4}} \times$ faster than the full-order CFD models.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Accelerating Training", "weight": 1.0} -->

The SINDy-RL agent was $14.47 \times$ more sample efficient for the 3D Airfoil environment; with only 25 dynamics updates, the median SINDy-RL agent reached the final median baseline agent performance. Physically, this was the difference between 14 hours of training using the SINDy-RL environment and 185 hours using the full-order environment, greatly reducing the total amount of time needed to learn capable policies. A comparison of clock times for different aspects of training the HydroGym environments can be found in Supplementary Table 4.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Accelerating Training", "weight": 1.0} -->

It is important to note the large variance in performance among the 20 trained SINDy-RL Cylinder agents depicted in the shaded region of Figure. After interacting with the full-order Cylinder environment 13,000 times, the top 50% performing SINDy-RL agents were able to surpass the best baseline performance---some achieving 11% drag reduction, comparable with optimized solutions from previous literature. However, the bottom 25% of agents performed poorly. Surrogate dynamics models can quickly diverge---especially early in training---which can provide misleading rewards. When these effects are further coupled with unfavorable policy network initializations, agent performance can severely degrade. The overall success of the majority of the agents indicates that methods like population-based training may be extremely effective at pruning these bad combinations of surrogate dynamics, rewards, and policies to quickly find exceptional policies using very few interactions in the full-order environment.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Accelerating Hyperparameter Tuning", "weight": 1.0} -->

The success of DRL to find effective control policies can often depend on the neural network initialization and choice of hyperparameters, otherwise training might lead to a suboptimal policy. To address this, it is common to use different random initializations for the network and hyperparameter tuning, and software packages have been created to facilitate these searches, such as Ray Tune. While these tuning algorithms can be effective for uncovering sophisticated policies, they generally rely on parallelizing training and significant compute usage. Previous benchmarks have shown that the Swimmer-v4 environment is particularly challenging to train with PPO and it has been suggested that learned policies for Swimmer-v4 are especially sensitive to certain hyperparameters and tuning can achieve superior performance. We pursue this idea by comparing population-based training (PBT) to improve policies for agents interacting in the full-order Swimmer-v4 environment and a SINDy-RL environment with dictionary surrogates for the dynamics and reward. Both experiments used a population of 20 policies and periodically evaluated the policies using the rollouts from the full-order model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Accelerating Hyperparameter Tuning", "weight": 1.0} -->

As shown in Figure, the SINDy-RL training is able to achieve nearly 30% better maximal performance than the baseline using $\mathbf{5}\mathbf{0} \times$ fewer samples from the full-order environment. This indicates that SINDy-RL can provide a convenient way to accelerate hyperparameter tuning in more sophisticated environments. Additional training details for PBT can be found in Supplementary §4B.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Generalization", "weight": 1.0} -->

It has been well-documented that while DNNs are excellent at performing on unseen data sampled from the same data distribution used for training, i.e. interpolation, they often fail at extrapolation to data beyond the convex hull of the training set. In Figure, we investigate the ability of top-performing Pinball agents trained at ${Re} = 100$ for $20$-second segments to extrapolate to unseen dynamics at ${{Re} = {150,250}},$ and $350$ for a $100$-second evaluation. It is well-known that the dynamics of the Pinball system undergo a bifurcation at around ${Re} = 115$ where the dynamics transition from being quasi-periodic to chaotic; thus, the dynamics are fundamentally different at these $Re$ values, which can be qualitatively seen---especially at ${Re} = 350$---in the initial conditions shown in Figure (b). Despite these fundamental differences, the SINDy-RL policy is able to reasonably extrapolate.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Generalization", "weight": 1.0} -->

While performance does degrade compared to ${Re} = 100$, the agent is able to obtain a much better cumulative return of reward over the long trajectory compared to the baseline neural network counterpart.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Surrogate Dictionary Dynamics", "weight": 1.0} -->

We now examine the SINDy dynamics learned from agents during the training outlined above. We utilize a polynomial library for each dynamics model. Despite none of the environments having a polynomial representation of the dynamics, the surrogate dynamics provide a sufficient representation of the environment to learn a control policy through repeated interaction. A thorough investigation of the learned dynamics from each environment can be found in Supplementary §5.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Surrogate Dictionary Dynamics", "weight": 1.0} -->

We find that for most systems, it is imperative to periodically refit the dynamics while the agent explores control strategies. For example, with the swing-up dynamics, the agent has no information about the goal state at the unstable equilibrium early in training. In Supplementary Fig. 13, we show that the first dynamics model provides a reasonable representation of the phase portrait, but the learned unstable fixed point is offset from the ground-truth position. Without refitting the dynamics, the agent would learn to drive the system to the wrong point and never stabilize the true system. However, by deploying the learned policy on the full-order system and gathering new data, the quality of the dynamics model improves and the agent is able to complete the task both using the surrogate and full-order dynamics. Finally, unlike a neural network representation of the dynamics, our approach provides a symbolic representation of the learned dynamics.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Surrogate Dictionary Dynamics", "weight": 1.0} -->

In Supplementary §5, we provide the learned coefficients $\mathbf{\Xi}$ and show that the swing-up dynamics model is well-represented by an Eulearian integration scheme: $\mathbf{x}_{k + 1} = {\mathbf{x}_{k} + {\Deltatf{(\mathbf{x}_{k})}}}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Surrogate Dictionary Dynamics", "weight": 1.0} -->

It is important to note a limitation of using dictionary dynamics; for large observation spaces, the size of a polynomial dictionary increases combinatorially. For example, a quadratic dynamics library with a 318-dimensional state would have over 16M parameters ^22^2A library of monomials with degree $\leq d$ in $m$ variables has $\binom{m + d}{d}$ terms; dynamics regression consists of $m$ equations, for a total of $m \cdot \binom{m + d}{d}$ parameters.. Therefore for large spaces, dimensionality reduction is critical. We demonstrate the viability of this approach for both the Pinball and 3D Airfoil environments by linearly projecting the 70- and 318-dimensinoal observations onto the dominant SVD modes of the system and found this to be sufficient for purposes of training. For more complicated dynamics, autoencoders have been found to be useful for finding nonlinear projections.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Surrogate Dictionary Rewards", "weight": 1.0} -->

We now consider the case where the exact rewards are not analytically expressible from the observations. In this setting, we periodically fit the surrogate dictionary reward $\hat{r} = {\hat{R}{(\mathbf{x},\mathbf{u})}}$ alongside and independent of the SINDy dynamics. For Swimmer-v4, the rewards in the full-order environment are given by the agent's body-centered horizontal velocity. However, this quantity is not provided by the observation space. It has been well-documented that---even with access to the exact rewards---solving the Swimmer-v4 task is a considerable challenge because of the placement of the velocity sensors; researchers have even created their own modified versions of the environment when performing benchmarks. Our method identified that a sparse reward of $\hat{r} \approx v_{x}$---the horizontal velocity of the leading segment (not the body)---was a suitable surrogate and remained stable throughout the entirety of the population-based training described in Section 3.1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Surrogate Dictionary Rewards", "weight": 1.0} -->

In contrast to the Swimmer-v4 environment, the HydroGym environments are governed by a nonlinear PDE, where the rewards are scalar measurements evolving with the dynamics on the domain and are not analytically expressible in terms of the provided observations. The lack of available information makes modeling the environment and the reward a very challenging task. Just as in the discussion in Section 3.2, Figure (i) demonstrates the necessity of periodically updating the surrogate models. At the beginning of training, the learned reward is actually anti-correlated with the full-order reward; however, the learned reward becomes well-correlated after subsequent updates. Despite the inability to learn the exact reward in the fluid environments, the surrogate reward provides a sufficient enough learning signal for training a comparable control policy when having access to the exact rewards. We also highlight the interpretability of our method in Figure (ii); the learned reward function is a quadratic polynomial of the observations, and we can analyze the explicit influence of the control. The bowl-shaped function (given by the quadratic) gradually shifts in response to the increasingly positive control.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Surrogate Dictionary Rewards", "weight": 1.0} -->

Furthermore, it is clear that the drag is minimized (i.e. reward is maximized) for large values of $|u|$, indicating that an optimal control strategy would apply maximal control input to stay in the bowl's minimum. For the Pinball and 3D Airfoil environments, the sparse sensors in the flow are not sufficient to describe the net forces acting on surfaces; indeed, the discovered reward functions are dominated primarily by terms coupling the actuation (local information) to the sensors. The learned rewards and a detailed investigation for each environment can be found in Supplementary §6.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Surrogate Dictionary Policy", "weight": 1.0} -->

While DNN policies can find solutions to complicated control problems, they are typically over-parameterized, black-box models that lack interpretability. There have been several approaches to combine symbolic regression and DNNs to improve interpretability, but they tend to focus on discovering the dynamics rather than a symbolic form for a controller. Here, we discover a lightweight model of the control with sparse dictionary learning using the behavioral cloning method described in Section; for each environment, we leverage the E-SINDy dynamics and the neural network policy obtained from Algorithm 1 to collect data for fitting the dictionary model.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Surrogate Dictionary Policy", "weight": 1.0} -->

However, the Cylinder environment provides an example where this method may struggle; the surrogate policy only reduces drag by about 3.7% compared to the neural network policy's 8.7% reduction. The original neural network agent learned a bang-bang control policy; this is very difficult to approximate with a smooth polynomial due to the bounded derivatives. One of the key challenges that supervised imitation learning faces (e.g. behavior cloning) is the issue of compounding errors during policy deployment. Because our policy approximation is a type of behavior cloning, our method inherits this challenge; the approximate policy slowly drifts away from the state-action pairs it was trained on and ultimately performs suboptimally. A detailed investigation of the learned dictionary policies for each environment (including a comparison of different data sampling strategies used for the behavior cloning) can be found in Supplementary §7.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Uncertainty Quantification", "weight": 1.0} -->

From Equation, we have a way of using the structure of the dictionary model to efficiently compute the pointwise variance from an ensemble of trained models. We now demonstrate how we can use this as a tool to investigate our learned functions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Uncertainty Quantification", "weight": 1.0} -->

In Figure, we visualize the evolution of the uncertainty landscape for the swing-up dynamics when training the dynamics and policy with SINDy-RL. At the beginning of training, the dynamics are confined to a narrow band of low-variance states where data has been previously collected. During training, the variance landscape changes in response to new, on-policy data. By the time the agent has learned to solve the swing-up task, the learned dynamics have become more certain and the agent takes trajectories over regions that have less variance.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Uncertainty Quantification", "weight": 1.0} -->

In this work we only use variance to inspect the learned dictionary functions, although there are further opportunities to exploit the variance. There is a trade-off in sample efficiency between refining the learned dynamics and improving the policy early in training. With a poor representation of the surrogate dynamics, we risk overfitting to the surrogate and discovering policies that do not generalize well to the real environment. Analogous to curiosity-driven learning, the estimated uncertainty of the dynamics and reward models may strategically guide the exploration of the environment and rapidly improve them---making it less necessary to query the environment later. Likewise, we may encourage "risk-averse" agents by penalizing regions with high-uncertainty---encouraging agents to take trajectories where the dynamics are trusted and agree with the full-order model.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion", "weight": 1.5} -->

This work developed a unifying framework for combining SINDy (i.e., sparse dictionary learning) with deep reinforcement learning to learn efficient, interpretable, and trustworthy representations of the environment dynamics, the reward function, and the control policy, using significantly fewer interactions with the full environment. We demonstrate the effectiveness of SINDy-RL on several challenging benchmark control environments, including performing gust mitigation of NACA 0012 airfoil at ${Re} = 1000$ in a 3D, unsteady environment.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion", "weight": 1.5} -->

By learning a sparse representation of the dynamics, we developed a Dyna-style MBRL algorithm that could be $10 - 100 \times$ more sample efficient than a model-free approach, while maintaining a significantly smaller model representation than a black-box neural network model. When the reward function for an objective is not easily measurable from the observations---e.g. with only access to sparse sensor data---SINDy-RL can simultaneously learn dictionary models of the reward and dynamics from the environment for sample-efficient DRL. We also demonstrated that SINDy-RL can learn a sparse dictionary representation of the control policy for certain tasks; the resulting sparse policy is orders of magnitude smaller than the original neural network policy, has smoother structure, and is inherently more interpretable. With a lightweight polynomial representation of the control policy, it becomes more feasible to transition to embedded systems and resource-limited applications. The interpretable representation of the dictionary policy also facilitates classical sensitivity analysis of the dynamics and control, such as quantifying stability regions and providing robust bounds---an especially important quality in high-consequence and safety critical environments.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, we have shown that for dictionary models, it is possible to analytically compute the point-wise variance of the model to efficiently estimate the uncertainty from an ensemble, which can provide insight into the trustworthiness of the model and possibly be used for active learning by intelligently steering the system into areas of high-uncertainty.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion", "weight": 1.5} -->

A key ingredient for successfully applying DRL is to learn over long time-horizons. This posed a significant challenge to SINDy-RL (and Dyna-style learning more broadly) because the learned dynamics models are not guaranteed to be stable or converge---especially under the presence of control. We address this by incorporating known constraints, such as resetting the environment if a predicted state value exits a bounding box and projecting the state-space back onto the appropriate manifold after each step. There has been substantial work constraining dictionary dynamics models with structured priors---such as conservation laws, symmetry, stability regions, and other forms of domain knowledge ---which further offer many promising avenues for practitioners to encourage agents to stably interact over long time horizons.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion", "weight": 1.5} -->

Due to the combinatorial scaling of the library, dictionary learning is challenging to apply directly to high-dimensional spaces. In this work, we have demonstrated that projecting onto a low-dimensional linear subspace using the SVD can be sufficient to make this tractable. After an initial preprint of this work, SINDy-RL was applied to controlling PDEs by using the SINDy autoencoder framework to discover nonlinear projections of the observation and action spaces onto a low-dimensional manifold. Discovering a coordinate system where the dynamics are smooth and globally defined may also help address the challenges that dictionary approaches face when the model discovery is piecewise or discontinuous. Partial observability of the environment also poses challenges for this framework. We have shown that sometimes there is sufficient information available to model the reward function from observations, but in practice this will not always be the case. Recent work has investigated deep delay embeddings to identify governing dynamics when there is substantial missing information, which is an opportunity for future investigation.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion", "weight": 1.5} -->

While we have restricted our attention in this work to using SINDy for Dyna-style MBRL by exploiting a model-free DRL algorithm, it is important to note that there are further opportunities to combine SINDy with control. Instead of DRL, a gradient-free policy optimization such as evolutionary algorithms could completely replace a model-free DRL optimizer. Furthermore SINDy provides an analytic, differentiable representation of the dynamics, thus SINDy can act as a differentiable physics engine for control and used for directly calculating gradients of RL objectives. For example, by modeling the dynamics and value functions as dictionary models, the differentiable structure was utilized with the Hamilton-Jacobi-Bellman equations to directly calculate the optimal control of a system. Finally, there may be a way to bypass the use of a policy network all-together by representing the policy directly as a sparse dictionary model for policy gradient optimization.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Materials, Data, and Code Availability", "weight": 1.0} -->

All experiments, with the exception of the 3D Airfoil environment, were performed using a single-node, Linux engineering workstation consisting of a total of 40 CPUs (Intel$^{\text{®}}$ Xeon$^{\text{®}}$ Gold 6230). The 3D Airfoil experiments used NVIDIA A100 GPUs on JUWELS Booster and JURECA at the Jülich Supercomputing Centre (JSC) / Forschungszentrum Jülich.
