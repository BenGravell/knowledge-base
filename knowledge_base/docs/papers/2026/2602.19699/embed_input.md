<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CACTO-BIC: Scalable Actor-Critic Learning via Biased Sampling and GPU-Accelerated Trajectory Optimization

Topics include Reinforcement learning, Optimal control, Trajectory optimization, Robotics, Robustness, Scalability, Real-time systems, Optimization, Control, Learning, Sampling, CACTO-BIC, TO.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory Optimization (TO) and Reinforcement Learning (RL) offer complementary strengths for solving optimal control problems. TO efficiently computes locally optimal solutions but can struggle with non-convexity, while RL is more robust to non-convexity at the cost of significantly higher computational demands. CACTO (Continuous Actor-Critic with Trajectory Optimization) was introduced to combine these advantages by learning a warm-start policy that guides the TO solver towards low-cost trajectories. However, scalability remains a key limitation, as increasing system complexity significantly raises the computational cost of TO. This work introduces CACTO-BIC to address these challenges. CACTO-BIC improves data efficiency by biasing initial-state sampling leveraging a property of the value function associated with locally optimal policies; moreover, it reduces computation time by exploiting GPU acceleration. Empirical evaluations show improved sample efficiency and faster computation compared to CACTO. Comparisons with PPO demonstrate that our approach can achieve similar solutions in less time. Finally, experiments on the AlienGO quadruped robot demonstrate that CACTO-BIC can scale to high-dimensional systems and is suitable for real-time applications.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Trajectory Optimization (TO) is a widely used and flexible technique for solving robotic control problems. In TO, the high-level task is formulated as a constrained Optimal Control Problem (OCP), where the optimization variables are the system's state and control trajectories. Constraints enforce compliance with system dynamics and kinematics, actuator limits, and task-specific requirements. However, OCPs are typically highly non-convex, making gradient-based solvers prone to converge to poor local minima. While global methods based on the Hamilton–Jacobi–Bellman equation or Dynamic Programming[bellman1954theory]exist, their applicability is limited by the curse of dimensionality.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Deep Reinforcement Learning (RL) emerged as an alternative framework, particularly for continuous state and action spaces. Algorithms such as DDPG [DDPG], SAC [SAC], and PPO [PPO]have demonstrated strong performance in robotic control tasks. Due to their exploratory nature, RL methods are generally less sensitive to local minima but they typically suffer from high sample complexity and long training times.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To overcome the complementary limitations of TO and RL, hybrid approaches combining the two have recently gained significant research attention.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A popular choice is to rely on TO imitation: policies are trained to mimic TO or model predictive control (MPC) solutionsthrough value-based or action-based imitationto reduce online computational costs and to leverage sensor feedback [carius2020mpc, ghezzi2023imitation]. However, these methods neither improve TO solution's quality, nor guarantee constraint satisfaction. Accounting for policy approximation errors in the TO problem can lead to better results [levine2013guided, lidec2022enforcing], but it inherits the same limitations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Other methods use learned policies or value functions to warm-start TO or to define terminal costs, thereby accelerating optimization and guiding the solver toward improved solutions [reiter2024ac4mpc, ceder2024bird]. While effective for TO, these approaches provide no benefits for RL training.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An increasingly prominent class of approaches embeds TO directly within the RL framework to improve training efficiency. These methods can be classified based on where TO is included: post-policy, pre-policy, or as a residual policy. Post-policy methods evaluate TO after the policy. Some methods learn cost or constraint parameters [romero2024actor, zarrouki2024safe], leveraging MPC's safety and stability guarantees, but require solving TO online and face convergence challenges. Others use TO as actor and learn its terminal cost [lowrey2018plan, jordana2025infinite], accelerating training and improving constraint handling, yet potentially yielding suboptimal solutions or neglecting sensor feedback. Another variant initializes TO with an RL policy [CACTO,morgan2021model], improving convergence speed and solution quality, yet still does not exploit sensor feedback. In pre-policy methods, TO generates reference trajectories or auxiliary information that are inputted to the RL policy, effectively speeding up training [jenelten2024dtc].

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Residual methods instead learn a residual policy to improve TO-generated control inputs with learned corrections[silver2018residual].While both pre-policy and residual methods accelerate training, they require online TO and depend on its ability to find high-quality solutions; moreover, learned policies may violate constraints even when TO does not.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we extend CACTO [CACTO,alboni2024cacto], a post-policy algorithm that exploits the interplay between TO and RL to accelerate training. The actor policy generates the initial guess for TO, leveraging the exploratory nature of RL to avoid convergence to poor local minima, while TO guides the learning process of the RL agent.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The primary limitation of CACTO is scalability. As the system complexity increases, TO becomes more expensive, and actor–critic training requires more iterations to converge. We investigate strategies to reduce the computational burden in both TO and RL phases.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- A method to identify state-space regions where an improvement of the actor policy is more likely. - A new version of CACTO's algorithm, called CACTO-BIC, that exploits biased initial conditions (BIC) and GPU-based computation to achieve improved sample and time efficiency. - A JAX-based[jax2018github] open-source implementation of CACTO-BIC that exploits GPUs to solve TO problems and train neural networks. - The first validation of CACTO on real hardware through experiments on a quadruped robot.

<!-- chunk {"id": "body-0013", "role": "body", "section": "BIASED INITIAL STATES SAMPLING", "weight": 1.0} -->

Identifying regions of the state space with high potential for policy improvement is a challenging problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "BIASED INITIAL STATES SAMPLING", "weight": 1.0} -->

Exploration strategies in RL can be broadly categorized into undirected and directed approaches. Undirected exploration relies on stochastic action selection, such as $\epsilon$-greedy policies, to explore the state space without explicitly accounting for uncertainty or novelty. Directed exploration, in contrast, uses signals derived from the agent’s learning process or auxiliary models to guide behavior toward less familiar or more uncertain regions. A common class of directed methods employs intrinsic rewards or exploration bonuses, including count-based or approximate count methods [bellemare2016unifying], uncertainty metrics [lowrey2018plan], and curiosity-driven approaches such as prediction-error bonuses and random network distillation [pathak2017curiosity,burda2018exploration]. Several works have also explored initial-state or restart-based exploration. These approaches often assign scores to states to prioritize which ones to explore further. Criteria for scoring include the system’s sensitivity[parsa2023where2start], the familiarity[schenke2021improved], the uncertainty[yin2023sample], or the TD error [tavakoli2018exploring].

<!-- chunk {"id": "body-0015", "role": "body", "section": "BIASED INITIAL STATES SAMPLING", "weight": 1.0} -->

[messikommer2024contrastive], proposes a structured replay buffer that groups states by task relevance and prioritizes sampling from unmastered sub-tasks. When available, prior or expert knowledge can also be leveraged to further guide exploration.

<!-- chunk {"id": "body-0016", "role": "body", "section": "BIASED INITIAL STATES SAMPLING", "weight": 1.0} -->

We address the exploration problem by leveraging the insight that the value function $\bar{V}(x)$ associated with locally optimal solutions is generally piecewise continuous.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivating Example: Discontinuous Value Function", "weight": 1.0} -->

Let us illustrate how the structure of the value function associated with a locally optimal policy can help us tackle the exploration problem. We focus on a toy problem with a 1D state, single integrator dynamics, and a cost with two local minima (see Fig.[fig:f1]). Solving TO problems with a naive initial guess, highlights the presence of two basins of attraction, $\mathcal{R}_1$, and $\mathcal{R}_2$, each corresponding to a different local minimum (see Fig.[fig:f1]).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivating Example: Discontinuous Value Function", "weight": 1.0} -->

Cost and Value obtained with TO using a naive initial guess. The critic smooths the Value's discontinuities.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivating Example: Discontinuous Value Function", "weight": 1.0} -->

Within each basin, the real Value $\bar{V}$ is continuous, but it is discontinuous at the shared boundary $\mathcal{R}_1 \cap \mathcal{R}_2 \triangleq \partial \mathcal{R}$. In the neighborhood of $\partial \mathcal{R}$, $\bar{V}$ is lower (i.e. better) in $\mathcal{R}_1$ than in $\mathcal{R}_2$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Motivating Example: Discontinuous Value Function", "weight": 1.0} -->

After training the critic with the first batch of TO episodes, the network smooths out the discontinuity (see Fig. [fig:f1]) in a region $\mathcal{N}$ around $\partial \mathcal{R}$, where the critic either underestimates or overestimates the true value $\bar{V}$: V(\bar{x} | \theta_V) > \bar{V}(\bar{x}) \qquad \forall \bar{x} \in \mathcal{N} \cap \mathcal{R}_1 \\V(\bar{x} | \theta_V) < \bar{V}(\bar{x}) \qquad \forall \bar{x} \in \mathcal{N} \cap \mathcal{R}_2 Therefore in $\mathcal{N}$ the critic's gradient will point towards $\mathcal{R}_2$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motivating Example: Discontinuous Value Function", "weight": 1.0} -->

Due to this gradient, during the policy improvement phase the actor can improve in $\mathcal{N} \cap \mathcal{R}_2$, learning to steer the state toward $\mathcal{R}_1$ rather than $\mathcal{R}_2$. This example reveals that the regions near value function's discontinuities hold great potential for policy improvement.

<!-- chunk {"id": "body-0022", "role": "body", "section": "General case: Discontinuous Value Function", "weight": 1.0} -->

The phenomenon shown in Section[sec:1Dex] frequently occurs in problems with multiple local minima. Each local minimum defines a basin of attraction where the value function is continuous, while discontinuities typically appear at the boundaries between basins. These discontinuities highlight regions with great potential for policy improvement. In contrast, sampling initial states far from such discontinuities likely leads the actor to simply imitate TO.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Detecting Informative Regions via Critic Uncertainty", "weight": 1.0} -->

Approximating the value function close to the discontinuities is particularly challenging for the critic network, which cannot accurately represent abrupt changes due to its continuous activation functions. As a result, the critic tends to incur larger errors near these boundaries. We suggest leveraging the uncertainty estimation of the critic's output to identify the value's discontinuities. An additional neural network, referred to as std-critic, is introduced to predict the standard deviation of the critic. Following[stdlearning], this network is trained at the end of each actor–critic update phase by minimizing the negative log-likelihood of a normal distribution: (V^std(x|^std)) + 1 2(V - V(x|^V))^2 V^std(x|^std)^2 where $V^{\text{std}}(\cdot)$ and $\theta^{\text{std}}$ are the std-critic network and its parameters.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Detecting Informative Regions via Critic Uncertainty", "weight": 1.0} -->

The first term of this loss pushes $V^{std}$ to be small everywhere, while the second term pushes $V^{\text{std}}$ to increase when the critic's error is large. We train this network after the critic to avoid issues during the early stages of learning. The initial states with the highest potential for policy improvement are then selected according to their predicted uncertainty $V^{\text{std}}(\tilde{x})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Accounting for discountinuous optimal value functions", "weight": 1.0} -->

In some problems, the globally optimal value function may naturally exhibit discontinuities, as in the classic swing-up task for a single pendulum. The initial states sampled near these discontinuities are as informative as the ones sampled far from the basins' boundaries since the policy in the proximity of the discontinuity is already globally optimal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Accounting for discountinuous optimal value functions", "weight": 1.0} -->

To avoid selecting initial states near discontinuities that arise in the globally optimal value function due to the inherent nature of the problem being analyzed, an additional metric is introduced to evaluate the discrepancy between the critic's output and the TD target computed with the policy: $$V_{TD}(\tilde{x}) = l(x,\mu(\tilde{x}|\theta^\mu)) + V(f(x,\mu(\tilde{x}|\theta^\mu))|\theta^V)$$ This metric measures the difference between the actions computed by the actor and TO, according to how much they impact the Value. When the actor and TO compute the same actions, this discrepancy should be nullbut in practice it may not be null due to errors in the critic. After the actor is updated, the discrepancy between $V(\tilde{x})$ and $V_{TD}(\tilde x)$is typically reduced. Therefore, a copy of the actor network from the previous iteration is used to compute this score.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Accounting for discountinuous optimal value functions", "weight": 1.0} -->

A high mismatch indicates regions where TO and the actor differ the most, signaling opportunities for improvement.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Accounting for discountinuous optimal value functions", "weight": 1.0} -->

The initial states with the highest potential for policy improvement are then selected according to the following score, which multiplies the Value's uncertainty and the actor-TO's discrepancy: $$s(\tilde{x}) = V^{\text{std}}(\tilde{x}) \cdot ||V(\tilde{x}) - V_{TD}(\tilde{x})||$$

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithm Overview", "weight": 1.0} -->

An overview of the CACTO-BIC (Biased Initial Conditions) algorithm is illustrated in Fig.[fig:CACTO\_scheme].

<!-- chunk {"id": "body-0030", "role": "body", "section": "Algorithm Overview", "weight": 1.0} -->

Overview of CACTO-BIC with biased initial-state sampling.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithm Overview", "weight": 1.0} -->

During the first iteration, as in the original CACTO framework[CACTO], initial states for the TO problems are sampled uniformly at random. From the second iteration onward, a set of $10N$ candidate initial states is sampled and ranked based on $V^{\text{std}}$. The top $N$ samples are then selected for the next TO batch. Moreover, since trajectories starting from these initial states provide more information, we can reduce the number of problems solved from the second iteration (see Section[ssec:bics\_results]for details).

<!-- chunk {"id": "body-0032", "role": "body", "section": "GPU-based computation", "weight": 1.0} -->

To reduce the computation time of the algorithm by leveraging GPUs, the entire framework was migrated to JAX, a Python library for accelerator-oriented array computation and program transformation[jax2018github]. The migration is beneficial in two ways: first, migrating to GPU the neural network trainingaccounting for about 90% of CACTO’s total computation timeyields significant speedups; second, performing TO directly on GPU eliminates any CPU-GPU data-transfer overhead, in addition to reducing TO's computation time, which significantly grows with the complexity of the system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "GPU-based computation", "weight": 1.0} -->

Migrating to GPU-based computation required some adaptations to meet the constraints of parallel processing: GPUs require fixed-size arrays and uniform computation across batches to enable efficient vectorization, leading to the following two key challenges.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Variable horizon", "weight": 1.0} -->

In CACTO, the time horizon of each TO problem is randomized to ensure the exploration of the state-time space. However, when solving TO problems on a GPU we must use a fixed time horizon for all the problems in the same batch. Therefore, we have modified the cost function so that it becomes zero after a certain timestep $T$, which is randomly sampled for each episode: By doing so we effectively get a variable horizon with a fixed-horizon TO problem. This leads to unnecessary computation, which however are largely compensated for by the speedup coming from massive parallelization.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Fixed number of iterations", "weight": 1.0} -->

Because GPUs execute batched computations in parallel, all TO problems in a batch must undergo the same number of optimization iterations. Consequently, the maximum number of iterations, $max_iter$, becomes a crucial hyperparameter. Setting this value too low may lead to premature termination, and hence to collect too few or insufficiently informative samples. In contrast, setting it too large can cause longer runtimes, since hard-to-converge problems dominate the batch’s overall computation time, slowing the entire pipeline. Moreover, the ideal number of iterations may vary as the policy improves, as better initial guesses generally lead to faster convergence.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Fixed number of iterations", "weight": 1.0} -->

To determine the maximum number of iterations, we suggest to solve a large set of problems using a naive warm-start and a high iteration limit ($max_iter=1000$), generating a dataset of the iterations needed to converge. The maximum number of iterations can then be set to the 99th percentile of iteration counts for the first iteration of CACTO (where the naive warm-start is used) and to the 50th percentile for subsequent iterations (where CACTO’s actor provides the warm-start).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regularization for matrix inversion", "weight": 1.0} -->

In iLQR[jacobson1970differential], it is crucial to regularize the Hessian of the value function so that it is positive definite.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regularization for matrix inversion", "weight": 1.0} -->

The standard regularization consists in increasing the local control-cost Hessian with a diagonal term: where $\mu$ plays the role of a Levenberg-Marquardt parameter. During the backward pass, if the line search fails, $\mu$ is increased and the backward pass is retried, otherwise, $\mu$ is decreased.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regularization for matrix inversion", "weight": 1.0} -->

This approach is computationally efficient when solving problems sequentially on a CPU. However, it becomes impractical when solving multiple problems in parallel on a GPU, where such iterative tuning can significantly slow down the batched computation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Regularization for matrix inversion", "weight": 1.0} -->

This issue is addressed through regularization based on the eigenvalue decomposition. The eigenvalues $S$ and corresponding eigenvectors $W$ of the state-cost Hessian and the control-cost Hessian are computed, the eigenvalues are clipped from below by a user-defined constant $\epsilon>0$, $S^\prime = \max(S,\epsilon)$, and the matrices are reconstructed: Q_+ &= W \, \text{diag}(S^\prime) \, W^T, \quad This procedure handles poorly-conditioned Hessians, while avoiding additional iterative steps. As a result, it is better suited for large-batch processing on GPUs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

The system dynamics and cost functions, implemented using the CasADi library[casadi] in CACTO-SL[alboni2024cacto], were converted into JAX-compatible functions through the Jaxadi library[jaxadi2024]. For TO, we replaced the previous solver with an iLQR implementation from the Trajax library[trajax], which provides the additional benefit of computing the gradient of the value function (used for training the critic network) while solving the optimal control problem. The neural networks were implemented using the Flax library[flax2020github], allowing the entire pipeline to remain on the GPU. Our new implementation is open-source and available on the page of the project.

<!-- chunk {"id": "body-0042", "role": "body", "section": "RESULTS", "weight": 1.0} -->

This section presents our evaluation of CACTO-BIC. First, we assess the impact of the biased initial-state sampling on data efficiency (Section[ssec:bics\_results]). Second, we analyze the computational benefits of the GPU-based implementation (Section[ssec:gpu\_results]). Third, we compare CACTO-BIC with a state-of-the-art RL algorithm (Section[ssec:ppo\_results]). Finally, we demonstrate the scalability of the approach through experiments on a high-dimensional quadruped robot, AlienGO[aliengo] (Section[ssec:aliengo\_results]).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Biased Initial State Sampling", "weight": 1.0} -->

We evaluate the proposed exploration method on the same benchmark scenarios used in[CACTO, alboni2024cacto]. The task consists in minimizing the distance between the robot’s end-effector and a target, while avoiding three elliptical obstacles (encoded with large penalties) and minimizing control effort. An additional reward is provided in the neighborhood of the target, as shown in Fig.[fig:CostFunction\_comp].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Biased Initial State Sampling", "weight": 1.0} -->

Cost function excluding the control effort term, with target set at $$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Biased Initial State Sampling", "weight": 1.0} -->

When the system starts from the Hard Region (highlighted in Fig.[fig:CostFunction\_comp]), it becomes challenging for a gradient-based solver to converge to the globally optimal solution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Biased Initial State Sampling", "weight": 1.0} -->

We consider three systems of increasing complexity: a point mass with state $(x, y, v_x, v_y, t) \in \mathbb{R}^5$ and control $(a_x, a_y) \in \mathbb{R}^2$, a jerk-controlled version of the Dubins car model [dubins] with state $(x,y,\theta,v,a,t) \in \mathbb{R}^6$ and control $(\omega,j) \in \mathbb{R}^2$, and a 3-degree-of-freedom (DoF) planar manipulator with a 7-dimensional state space and a 3-dimensional control input.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Biased Initial State Sampling", "weight": 1.0} -->

- CACTO as presented in[alboni2024cacto]; - CACTO-BIC: CACTO with biased initial-state sampling and a reduced number of TO episodes (25%) from the 2nd iteration onward; - CACTO with reduced TO episodes (as CACTO-BIC), but without biased initial-state sampling.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Biased Initial State Sampling", "weight": 1.0} -->

All algorithms run for the same number of learning iterations (i.e. updates of the neural networks). Fig. [fig:CACTO-SL-BICScomparison] shows the median (across 5 runs) of the mean cost (across initial conditions) as a function of the number of TO episodes. The results show that CACTO-BIC achieves comparable performance using $30-40\%$ of the number of TO episodes. However, this improvement comes with increased training time due to the additional std-critic network. With CACTO-BIC, the percentage of computation time devoted to training the networks rises to $93-94\%$. This motivates moving to the GPU.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

We now analyze the speedup achieved through the new GPU-accelerated implementation of CACTO-BIC. The number of TO problems solved in parallel was 300, 500, and 550 in the first iteration for the point mass, Dubins car and manipulator, respectively. From the second iteration onward, the batch size was reduced to 25%. The initial time is set to 0 in each TO instance. Table[tab:comp\_comp\_time] reports the computation times to perform the same updates using three versions of CACTO-BIC: a single-thread CPU version, a multi-thread CPU version, and the novel GPU version.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

Comparison between CPU and GPU versions of CACTO-BIC. GPU runtimes do not include the warm-up phase required for the JIT compilation of the TO solver.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

| System (nb. of updates) | 2c|CPU | GPU | | This test was performed on a workstation equipped with an AMD Ryzen 9 7950X CPU, 192 GB of RAM, and an NVIDIA RTX 6000 GPU with 48 GB VRAM, running on Ubuntu 22.04.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

The results show that using 10 cores to parallelize the TO problems has little effect on the total computation time as most time is spent for training the neural networks. The novel GPU version of CACTO-BIC achieves instead remarkable speedups ($\approx$30x for the point mass and Dubins car, and $\approx$56x for the manipulator).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

Although GPUs have far more cores than CPUs, the resulting speedups are smaller than this hardware difference suggests. Several factors contribute to this limitation. First, the TO problems are solved in batches on the GPU. Therefore a few hard instances may dominate the total computation time and cap the achievable speedup. Second, computations rely on reduced numerical precision. Although this improves raw throughput, it can introduce numerical instability and increase the number of required iterations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

By analyzing the time spent in the TO phase (creating the warm-start and solving TO problems) and in the RL phase (training networks), we observe that their relative contribution varies across systems, but remains comparatively balanced. Specifically, the TO and RL phases account for approximately 42% and 53% of the total time in the point mass, 61% and 37% in the Dubins car, and 22% and 75% in the manipulator.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

(see Table[tab:comp\_time\_cycle\_GPU]).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

Computation time allocated to the main blocks of CACTO. Values in parentheses indicate the percentage of the total computation time.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Computational Efficiency of GPU Computation", "weight": 1.0} -->

| | Point Mass | Dubins Car | Manipulator | AlienGO no rot | It follows that the speedup comes mainly from training the networks on the GPU, which is 51-85$\times$ faster than on the CPU in our tests.In contrast, the speedup in the TO phase is modest (3-5$\times$) for the Dubins car and point mass, but it becomes significant (19$\times$) for the most complex system.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Comparison with PPO", "weight": 1.0} -->

To evaluate CACTO-BIC w.r.t. state-of-the-art RL, we selected Proximal Policy Optimization (PPO) [PPO] as a benchmark. For a fair comparison, we employed the fully GPU-based implementation of PPO provided by BRAX [brax2021github]. Our analysis focuses on two aspects: first, learning a warm-start policy for a problem that exhibits local minima; second, learning a control policy for a classic benchmark problem, a customized version of the Reacher environment. Fig.[fig:comparison\_WS] reports the mean cost obtained using CACTO-BIC's and PPO's policies as warm-start for TO in the Point Mass and Manipulator environments. CACTO-BIC converged in one-third of the time in the first environment and in just 7% in the second one.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Comparison with PPO", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n\n\\definecolor{darkgray176}{RGB}{176,176,176}\n\\definecolor{lightgray204}{RGB}{204,204,204}\n\\definecolor{mediumturquoise64181195}{RGB}{64,181,195}\n\n\\begin{axis}[\nwidth=1\\linewidth,\nheight=3.5cm,\nlegend cell align={left},\nlegend style={fill opacity=0.8, draw opacity=1, text opacity=1, draw=lightgray204},\ntick align=outside,\ntick pos=left,\nx grid style={darkgray176},\nxmajorgrids,\nxmin=-5, xmax=105,\nxtick style={color=black},\ny grid

<!-- chunk {"id": "body-0060", "role": "body", "section": "Comparison with PPO", "weight": 1.0} -->

-40.7187514359301\n};\n\\addlegendentry{CACTO-BIC}\n\\addplot [semithick, mediumturquoise64181195, mark=*, mark size=1, mark options={solid}]\ntable {%\n0 9.42714165015654\n25 -18.5943375934254\n50 -34.3337478150021\n75 -39.7950518022884\n100 -39.7950527830557\n};\n\\addlegendentry{PPO (Brax)}\n\\end{axis}\n\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Warm-start provider comparison: Median (across 5 runs) of the mean cost (across initial conditions) starting from the Hard Region for the point mass (top), and the manipulator (bottom).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Comparison with PPO", "weight": 1.0} -->

Shaded areas represent first and third quartiles.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Comparison with PPO", "weight": 1.0} -->

In Fig.[fig:comparison\_policy] we compare CACTO-BIC and PPO in the Reacher Environment. Also in this case, CACTO-BIC achieves a similar cost in $\approx$10% of the computation time.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Comparison with PPO", "weight": 1.0} -->

Policy comparison: Median (across 5 runs) of the mean cost (across initial conditions) for a customized Reacher environment. Shaded areas represent first and third quartiles.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Hardware experiments", "weight": 1.0} -->

To evaluate CACTO's scalability and its potential for real-time applications we tested it on AlienGO, a quadrupedal robot featuring 12 degrees of freedom[aliengo]. We address the problem of navigation in confined environments, with even terrain, and the presence of a moving obstacle. The robot must reach a moving target (see Fig.[fig:setup]) while avoiding collisions with both the moving obstacle (a sphere of radius 0.5 m) and the walls of the room (a rectangle with sides ranging from 2 m to 10 m). We consider a fixed trotting gait with alternating diagonal leg pairs making contact with the ground.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Hardware experiments", "weight": 1.0} -->

Since legged robots have non-differentiable dynamics [wensing2023optimization], which are not compatible with gradient-based TO, we adopt a hierarchical approach. We combine a high-level policy relying on a simplified differentiable model, with a low-level policy using the complete robot dynamics. The high-level policy is trained with CACTO-BIC, while the low-level policy is trained with the RL algorithm CAT[chane2024cat], which can handle non-differentiable dynamics. In practice, CACTO-BIC's actor is used as a standalone policy to provide reference trajectories to the low-level policy.

<!-- chunk {"id": "body-0066", "role": "body", "section": "High-level policy", "weight": 1.0} -->

To train this policy, we employed a nonlinear version of the Linear Inverted Pendulum Model[kajita2003biped]. The state $x \in \mathbb{R}^{15}$ comprises the 2D offsets of the front and rear support feet relative to the associated shoulders $\Delta p_f$ and $\Delta p_r$, the Center of Mass (CoM) position $c \in \mathbb{R}^2$ and velocity $\dot{c} \in \mathbb{R}^2$ on the horizontal plane, the step index $s_{idx} \in \mathbb{N}$, which encodes both the current contact phase and time, the obstacle position $c_{obs} \in \mathbb{R}^2$ and the location of the four walls, expressed as offsets with respect to the global reference frame $\Delta_{walls} \in \mathbb{R}^4$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "High-level policy", "weight": 1.0} -->

$$x \triangleq (\Delta p_f, \Delta p_r, c, \dot{c}, s_{idx}, c_{obs}, \Delta_{walls}) \in \mathbb{R}^{15}.$$ The target position is assumed to be the origin.

<!-- chunk {"id": "body-0068", "role": "body", "section": "High-level policy", "weight": 1.0} -->

Assuming a trotting gait and constant Center of Pressure (CoP) during each contact phase, the control vector $u \in \mathbb{R}^6$ includes the offsets of front and rear support feet w.r.t. the associated shoulder in the next contact phase, $\Delta p_f ^ +, \Delta p_r ^ + \in \mathbb{R}^2$, a scalar $\alpha \in $ that expresses the CoP as a convex combination of the support foot positions, and the contact phase duration $\delta t$: $$u \triangleq (\Delta p_f^+, \Delta p_r^+, \alpha, \delta t) \in \mathbb{R}^{6}$$ The cost function penalizes the CoM-target distance, the CoM velocities, and a barrier-like cost penalizes CoM velocities beyond prescribed bounds. A smooth logarithmic reward is used to encourage reaching a narrow region around the target.

<!-- chunk {"id": "body-0069", "role": "body", "section": "High-level policy", "weight": 1.0} -->

Control regularization discourages deviations from nominal values: zero foot displacements, centered CoP ($\alpha=0.5$), and nominal contact-phase duration ($\delta t=0.375$ s). Obstacle avoidance is enforced through smooth logarithmic penalties. The algorithm took $\approx$109 s to converge. In this scenario, leveraging the GPU for solving the TO problems yields a substantial speedup, roughly 345$\times$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Low-level policy", "weight": 1.0} -->

The low-level policy is trained using a constrained RL algorithm [chane2024cat], which builds upon PPO [PPO], employing Isaac Gym for GPU simulation. The goal of this policy is to track the references generated by the high-level policy. During training, the high-level policy is rolled out in open loop, and updated only at the beginning of each new contact phase to enhance stability and robustness[villa2017model].

<!-- chunk {"id": "body-0071", "role": "body", "section": "Low-level policy", "weight": 1.0} -->

The low-level policy receives as observations: the base state (position and orientation, linear and angular velocity, and projected gravity), the target base position and linear velocity, yaw orientation error, foot placement errors, a binary flag indicating the active diagonal contact pair, the remaining time in the current gait phase, joint positions, velocities and the previous action.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Low-level policy", "weight": 1.0} -->

The reward function encourages accurate tracking of base position and orientation, linear and angular velocity, and the desired foot contact locations. Regularization terms are included to improve smoothness.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Low-level policy", "weight": 1.0} -->

All safety and style-related constraints are divided into soft constraints (which define a termination probability as a function of the constraint violation) and hard constraints (which cause immediate termination of the episode).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Aliengo Simulation and Hardware results", "weight": 1.0} -->

The experiments are conducted in an indoor area of 4 m$\times$4 m (see Fig.[fig:setup]). The obstacle and the target are either stationary or manually actuated, depending on the experiment.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Aliengo Simulation and Hardware results", "weight": 1.0} -->

Experimental setup: The lines define a 4 m $\times$ 4 m operational area.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Aliengo Simulation and Hardware results", "weight": 1.0} -->

State feedback is obtained from a motion capture system, which measures position and orientation of the robot, the obstacle and the target. Velocities are estimated by finite differencing and low-pass filtering.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Aliengo Simulation and Hardware results", "weight": 1.0} -->

Representative robot trajectories with fixed obstacle and target are shown in Fig.[fig:static].

<!-- chunk {"id": "body-0078", "role": "body", "section": "Aliengo Simulation and Hardware results", "weight": 1.0} -->

AlienGO’s CoM trajectories starting from random initial positions in the presence of a static obstacle and target. [Andrea: To save space in the caption use a legend to say that dashed lines represent reference trajectories, while solid lines represent real trajectories.]

<!-- chunk {"id": "body-0079", "role": "body", "section": "Aliengo Simulation and Hardware results", "weight": 1.0} -->

Results are shown in the accompanying video.

<!-- chunk {"id": "body-0080", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This paper presented CACTO-BIC, an extension of CACTO designed to improve scalability and computational efficiency in combined TO-RL framework by biasing the initial-state sampling using value function properties and leveraging GPU acceleration.

<!-- chunk {"id": "body-0081", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Experimental results demonstrate that the proposed sampling strategy effectively identifies state-space regions where actor policy improvement is more likely, leading to a $2.5-3.5\times$ increase in sample efficiency. In addition, GPU-based computation achieves 30-250$\times$ speedup compared to CACTO, with increasing benefits as system complexity grows. When compared to PPO, CACTO-BIC achieves similar final costs requiring only $7-30\%$ of the training time. Finally, experiments on the AlienGO quadruped robot show that CACTO-BIC scales to high-dimensional robotic systems and can be effectively used for real robot control.

<!-- chunk {"id": "body-0082", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Future works will focus on extending the proposed approach to handle constraints using augmented Lagrangian formulations [crl]. In addition, we will explore the integration of sampling-based optimization techniques, such as MPPI [mppi], to tackle non-differentiable dynamics. Finally, applying domain randomization may improve robustness to uncertain dynamics enhancing generalization to real-world systems [domrand].
