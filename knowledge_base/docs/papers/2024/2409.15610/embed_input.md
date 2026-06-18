<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing

Topics include Trajectory optimization, Model predictive path integral control, Diffusion, Locomotion, Model predictive control, Annealing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Takes a perspective of treating MPPI as a single step of a denoising diffusion process, and generalizes this process to a multi-step diffusion-style annealing process. DIAL-MPC starts optimizing the control sequence with smooth but inaccurate objectives and gradually shifts to more accurate local objectives.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by 13.4 times and outperforms reinforcement learning (RL) policies by 50% in challenging climbing tasks without any training.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Legged robots have demonstrated great potential in navigating through complex environments thanks to their agility and mobility \[parkHighspeedBoundingMIT2017, kimHighlyDynamicQuadruped2019, herdtOnlineWalkingMotion2010, khazoomTailoringSolutionAccuracy2024, koenemannWholebodyModelpredictiveControl2015, neunertWholeBodyNonlinearModel2018\]. However, the online control of articulated legged systems remains challenging because of their high-dimensional, underactuated and contact-rich nature, leads to non-convex and non-smooth optimization landscapes.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Reinforcement learning (RL) has become a popular approach for learning control policies for legged robots, thanks to its ease of implementation and strong performance in contact-rich problems \[radosavovicHumanoidLocomotionNext2024, heAgileSafeLearning, chengExtremeParkourLegged2024, mikiLearningRobustPerceptive2022, rudinLearningWalkMinutes, chenLearningTorqueControl2023, fuMinimizingEnergyConsumption2021\]. However, RL suffers from time-consuming training and tedious tuning, and the resulting policies heavily depend on the training setup, limiting their test-time generalization to unseen tasks and environments. In the meanwhile, NMPC \[neunertWholeBodyNonlinearModel2018, kuindersmaEfficientlySolvableQuadratic2014, koenemannWholebodyModelpredictiveControl2015\] is often limited to reduced-order models due to the intractability of solving full-order problems involving contacts and nonlinear dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Sampling-based MPC \[williamsAggressiveDrivingModel2016, yiCoVOMPCTheoreticalAnalysis2024, yinTrajectoryDistributionControl2022, williamsRobustSamplingBased2018\] has been applied to various nonlinear and hybrid dynamical systems because of its flexibility in handling arbitrary dynamics and constraints, as well as parallelizability. Nonetheless, these algorithms are sensitive to hyperparameters in high-dimensional and non-convex optimization problems, particularly the sampling kernel, leading to high variance and suboptimal performance. Specifically, a large sampling range provides better global coverage but may result in solutions far from the optimum, while a small sampling range enhances local search ability but is more susceptible to local minima and initial guesses, leading to increased variance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we address these challenges by unveiling the intrinsic connection between sampling-based MPC and diffusion processes. Following the key iterative refinement idea of the diffusion model, we introduce a novel sampling-based MPC method, Diffusion-Inspired Annealing for Legged Model Predictive Control (DIAL-MPC). DIAL-MPC optimizes control sequences iteratively in a dual-loop manner. Specifically, DIAL-MPC starts optimizing the control sequence with smooth but inaccurate objectives and gradually shifts to more accurate local objectives.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Compared with MPPI, DIAL-MPC enables on-the-fly, full-order torque-level locomotion control by effectively balancing global coverage and local convergence. We evaluate DIAL-MPC on a quadrupedal robot with full-order dynamics and show that it can achieve real-time 50Hz control with both robustness and efficiency. As a training-free and purely online method, DIAL-MPC enables precise jumping with payload and outperforms RL methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Novel Diffusion-Inspired Annealing Framework: We propose a diffusion-inspired annealing framework for sampling-based MPC by revealing the connection between sampling-based MPC and diffusion processes.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Full-Order Torque-Level Control of Legged Robot: We develop and implement DIAL-MPC for full-order torque-level control of legged robots based on the proposed annealing framework. To our knowledge, this is the first framework achieving both real-time flexibility and RL-level agility in legged locomotion.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Real-World Validation: We validate the performance of DIAL-MPC for quadruped control, showing that it achieves real-time 50 Hz control with robustness and efficiency.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Agility in Legged Locomotion", "weight": 1.0} -->

Nonlinear Model Predictive Control (NMPC), particularly gradient-based methods, has demonstrated significant success in real-time control of legged locomotion with closed-loop stability \[parkHighspeedBoundingMIT2017, grandiaPerceptiveLocomotionNonlinear2022, neunertWholeBodyNonlinearModel2018, sleimanUnifiedMPCFramework2021\]. These approaches typically employ reduced-order models to mitigate the burden of planning over full-order hybrid dynamics, necessitating lower-level whole-body controllers for motion execution \[kuindersmaEfficientlySolvableQuadratic2014, herdtOnlineWalkingMotion2010, kimHighlyDynamicQuadruped2019, koenemannWholebodyModelpredictiveControl2015\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Agility in Legged Locomotion", "weight": 1.0} -->

However, reduced-order models can lead to sub-optimal performance and constraint violations, particularly under high agility demands. For instance, \[khazoomTailoringSolutionAccuracy2024\] introduces a tailored solver for full-order NMPC online, yet remains constrained by predefined contact sequences, limiting motion agility and robustness. In contrast, our method enables full-order model MPC without redundant constraints, allowing adaptation to real-time feedback and environmental interactions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Agility in Legged Locomotion", "weight": 1.0} -->

Model-free Reinforcement Learning (RL) has also been explored to address full-order control by learning optimal policies directly from high-fidelity simulations \[heOmniH2OUniversalDexterous, fuHumanPlusHumanoidShadowing, zhangWoCoCoLearningWholeBody, heLearningHumanHumanoidRealTime2024, rudinLearningWalkMinutes, fuMinimizingEnergyConsumption2021\]. While these approaches eliminate the need for explicit modeling, they suffer from limited generalization to new tasks and dynamic environments.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Agility in Legged Locomotion", "weight": 1.0} -->

Goal-conditioned RL \[ghoshLearningActionableRepresentations2019, atanassovCurriculumBasedReinforcementLearning2024\] enhances task-level generalization but still struggles with unseen dynamics and novel task classes. Our approach overcomes these limitations by enabling rapid motion generation through training-free online optimization, thereby combining the agility of RL with the robustness and generalization capabilities of MPC.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Sampling-Based Optimization", "weight": 1.0} -->

Sampling-based or zeroth-order optimization methods, including Bayesian Optimization \[frazierTutorialBayesianOptimization2018, sohl-dicksteinDeepUnsupervisedLearning2015\], the Cross-Entropy Method \[mannorCrossEntropyMethod\], and Evolutionary Algorithms \[wierstraNaturalEvolutionStrategies2008\], are widely utilized for solving non-convex and non-smooth optimization problems. They differ from first-order methods as the gradient information is no longer required. These methods are particularly effective in applications such as hyperparameter tuning \[snoekPracticalBayesianOptimization2012, hernandez-lobatoParallelDistributedThompson2017\] and generative modeling \[songDenoisingDiffusionImplicit2020\].

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Sampling-Based Optimization", "weight": 1.0} -->

In the context of real-time robot control, Model Predictive Path Integral (MPPI) control \[williamsAggressiveDrivingModel2016\] and its variants \[yiCoVOMPCTheoreticalAnalysis2024, yinTrajectoryDistributionControl2022, williamsRobustSamplingBased2018\] have gained popularity for online motion planning \[pravitraL1AdaptiveMPPIArchitecture2020, sacksDeepModelPredictive2023, howellPredictiveSamplingRealtime2022\], due to their inherent parallelizability and flexibility. Given a high-stiffness problem like legged locomotion, zeroth-order methods including policy gradient \[suttonPolicyGradientMethods1999\] have shown better convergence properties both empirically and theoretically \[suhDifferentiableSimulatorsGive2022\] from their smoothing nature.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Sampling-Based Optimization", "weight": 1.0} -->

Despite their advantages, sampling-based methods are plagued by the curse of dimensionality and high variance, especially under constrained online sampling budgets. This is particularly problematic in high-dimensional, contact-rich environments.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Parallel Robot Simulation", "weight": 1.0} -->

Massively parallelizable simulation environments, such as Isaac Gym \[makoviychukIsaacGymHigh2021\], Brax \[freemanBraxDifferentiablePhysics2021\], and MuJoCo \[MuJoCoPhysicsEngine\], have become essential tools in the development of zeroth-order optimization methods for robot control. These simulators facilitate the rapid generation of data required by sample-hungry algorithms like PPO \[schulmanProximalPolicyOptimization2017\], enabling efficient training of complex policies.

<!-- chunk {"id": "body-0021", "role": "body", "section": "METHOD", "weight": 1.0} -->

In this section, we present our method by establishing the equivalence between MPPI and a single-stage diffusion process (section III-A). The connection then explains why the annealing process in diffusion helps MPPI to optimize over a non-smooth landscape, as discussed in section III-B. Leveraging this equivalence, we introduce a diffusion-inspired annealing technique for MPPI in section III-C.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Sampling-Based MPC as Single-stage Diffusion", "weight": 1.0} -->

where $x_{t + h}$ is the state at time $t + h$, $u_{t + h}$ is the control input at time $t + h$, $f$ is the system dynamics, $c$ and $c_{f}$ are the cost function and terminal cost function, $\mathcal{X}$ and $\mathcal{U}$ are the state and control constraints, respectively.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Sampling-Based MPC as Single-stage Diffusion", "weight": 1.0} -->

MPPI estimates the optimal control sequence through the following steps: First, draw $N_{W}$ perturbations from a Gaussian distribution ${{\lbrack W\rbrack}_{i} \sim {\mathcal{N}{(0,\Sigma_{t:{t + H}})}}},{i = {1,\ldots,N_{W}}}$ (which we collectively denote as ${\lbrack W\rbrack}_{1:N_{W}})$. Then the cost function $J{(u_{t:{t + H}})}$ is evaluated for each sampled control sequence by rolling out the system dynamics and cumulatively summing the cost.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Sampling-Based MPC as Single-stage Diffusion", "weight": 1.0} -->

For each perturbed control sequence $U + {\lbrack W\rbrack}_{i}$, where $U = u_{t:{t + H}}$, evaluate the cost function $J{({U + {\lbrack W\rbrack}_{i}})}$ by simulating the system dynamics and accumulating the costs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Sampling-Based MPC as Single-stage Diffusion", "weight": 1.0} -->

MPPI as a single-stage Diffusion. The optimization problem can be reframed in a sampling context. Define the target distribution ${p_{0}{(U)}} \propto {\exp\left( {- \frac{J{(U)}}{\lambda}} \right)}$. As $\lambda\rightarrow 0$, samples from $p_{0}{(U)}$ concentrate around the optimal control sequence $U^{\ast}$ as illustrated in fig. 2. However, directly sampling from $p_{0}{(U)}$ is impractical due to its narrow support.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Sampling-Based MPC as Single-stage Diffusion", "weight": 1.0} -->

To facilitate the sampling, we convolve $p_{0}{(U)}$ with a Gaussian noise kernel $\phi{( \cdot )}$, i.e., the density of $\mathcal{N}{(0,\Sigma)}$ to get the corrupted distribution ${p_{1}{( \cdot )}} \propto {{({p_{0} \ast \phi})}{( \cdot )}}$ as depicted in fig. 4.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

Given that MPPI is a single-stage diffusion that moves particles toward the stationary point of ${p_{1}{( \cdot )}} = {{({p_{0} \ast \phi})}{( \cdot )}}$ (proposition 1 ‣ III-A Sampling-Based MPC as Single-stage Diffusion ‣ III METHOD ‣ Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing")), a natural question arises: What are the pros and cons of optimizing $p_{1}$ compared to directly solving for the optimum of $p_{0}$?

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

Coverage and convergence trade-off. The advantages and disadvantages highlight a fundamental trade-off between exploration and exploitation in MPPI: a larger $\det\Sigma$ promotes greater exploration (i.e., coverage) by widening the sampling distribution, which helps to avoid suboptimal local minima.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

However, a larger $\det\Sigma$ may compromise optimality(i.e., convergence) as it will introduce a larger optimality gap. In contrast, a smaller $\det\Sigma$ improves local optimality at the risk of getting trapped in local minima.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

This trade-off becomes more pronounced in contact-rich tasks such as legged locomotion, where the optimization landscape is non-smooth, non-convex, and high-dimensional. The cost function $J$ and the distribution $p_{0}$ often have sharp and asymmetric peaks. In such cases, even a small increase in $\det\Sigma$ can degrade performance, and global optimality cannot be guaranteed through score ascent on $p_{1}{(U)}$ due to the small convolution kernel.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

By fixing the sampling kernel size, MPPI may either over-explore or over-exploit, failing to balance exploration and convergence effectively. This concern is illustrated in fig. 4, which shows how different kernel sizes affect the performance of MPPI. Therefore, designing an effective sampling strategy that balances coverage and convergence is crucial to unlocking the potential of MPPI in real-world legged locomotion tasks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

Fortunately, diffusion processes, known for their powerful sampling capabilities from complex distributions, offer a way to balance coverage and convergence through an annealing strategy. This strategy involves sampling iteratively at decreasing noise levels, effectively reversing the forward corruption process.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

Annealing in diffusion process. Instead of sampling solely from $p_{1}{( \cdot )}$, the forward process in diffusion defines a sequence of distributions with increasing noise levels: ${p_{1}{( \cdot )}},\ldots,{p_{N - 1}{( \cdot )}},{p_{N}{( \cdot )}}$, where $N$ is the total number of diffusion stages. Each density is defined as ${p_{i}{( \cdot )}} = {{({p_{0} \ast \phi_{i}})}{( \cdot )}}$ with ${\phi_{i}{( \cdot )}} \sim {\mathcal{N}{(0,\Sigma^{i})}}$. Sampling proceeds in reverse order. Starting from a higher noise level $\Sigma^{N}$, the sampling distribution $p_{N}{( \cdot )}$ is highly spread out, ensuring good global exploration.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

As the noise level decreases, the sampling distributions $p_{i}{(U)}$ become more concentrated, refining the search towards the target distribution $p_{0}{(U)}$ and improving convergence to the optimal solution.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

where $\beta$ is the temperature parameter for the annealing process, and $N$ is the number of iterations for the annealing process, $d$ is the dimension of the sampling space.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Diffusion-Inspired Annealing", "weight": 1.0} -->

Given that MPPI corresponds to a single-stage diffusion process, we can naturally incorporate this multi-stage annealed diffusion approach to design an improved sampling strategy for MPPI. In section III-C, we discuss how to implement this diffusion-inspired annealing process within the MPPI framework in a receding horizon manner.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

4: Get diffusion noise kernel Σt: t + Hi.
6: Rollout ut: t + H + [W]1: NW and evaluate the cost function J(ut: t + H+[W]1: NW).
7: Estimate Score ∇log pi(⋅).
10: Receding horizon ut + 1: t + H + 1 ← shift(ut: t + H)
Algorithm 1 Diffusion-Inspired Annealing for Legged MPC

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

Combining MPPI with multi-stage annealing, we propose DIAL-MPC (algorithm 1) that leverages the receding horizon structure of MPC and introduces a dual-loop covariance design. This design comprises two annealing procedures: an outer-loop trajectory-level annealing and an inner-loop action-level annealing, which we detail below.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

Dual-loop annealing. In a receding horizon MPC framework with a horizon length $H$ and $N$ update iterations for each control sequence at each timestep $t$, $u_{H}$ (the last element of $u_{0:H}$) is first updated at time $0$ by $N$ times using convolution kernel ${\Sigma_{H}^{N}\ldots},\Sigma_{H}^{1}$. After $u_{0}$ is applied to the system, the control sequence shifts forward. At the next time step $t = 1$, $u_{H}$ is updated again $N$ times, now with kernel $\Sigma_{H - 1}^{N},\ldots,\Sigma_{H - 1}^{1}$ as $u_{H}$ becomes the second-to-last element of the updated control sequence $u_{1:{H + 1}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

This procedure continues, and by the time $u_{H}$ is applied to the system at $t = H$, it will have undergone $NH$ updates with convolution kernels: ${\Sigma_{H}^{N}\ldots},\Sigma_{H}^{1};\Sigma_{H - 1}^{N},\ldots,\Sigma_{H - 1}^{1};\ldots;{\Sigma_{0}^{N}\ldots},\Sigma_{0}^{1}$ as shown in the last graph of fig. 1. Essentially, each control action $u_{h}$ is updated in a dual-loop manner before being applied to the system.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

This motivates the design of two annealing procedures: the outer loop is a trajectory-level annealing schedule for all the control sequence at a certain stage $i$ (i.e. designing the overall size of $\Sigma_{t:{t + H}}^{i}$ for a given $i$) and the inner loop is an action-level annealing schedule for different control at different horizons (i.e. the size of $\Sigma_{t + h}^{i}$ for $h = {0,\ldots,H}$).

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

where $\beta_{1}$ is the temperature parameter for the trajectory-level annealing, and $d_{u}$ is the dimension of a single control. The covariance matrix decreases over time as $i$ decreases, progressively narrowing the sampling distribution towards the target distribution $p_{0}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

where $\beta_{2}$ is the temperature parameter for action-level annealing. The covariance matrix increases with time as $h$ increases, allowing for a larger sampling region for future control actions that have been updated fewer times compared to those at the front of the horizon.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

Note that and specify only the overall size (i.e., the determinant) of the convolution kernels, leaving flexibility in designing the exact covariance matrices $\Sigma_{t + h}^{i}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C Diffusion-Inspired Annealing for Sampling-Based MPC", "weight": 1.0} -->

where $I$ is the identity matrix. This design combines both the outer-loop and inner-loop annealing schedules, adjusting the covariance matrices to ensure appropriate exploration and exploitation at each iteration and horizon step.

<!-- chunk {"id": "body-0046", "role": "body", "section": "EXPERIMENT", "weight": 1.0} -->

In this section, we demonstrate the advantages of DIAL-MPC in terms of: convergence and coverage, efficiency in test-time generalizability, and robustness to real-world model mismatch. We compare DIAL-MPC against MPPI and another sampling-based optimization method, CMA-ES \[akimotoTheoreticalFoundationCMAES2012\]. In addition, we provide goal-conditioned reinforcement learning (GCRL) as a performance reference. Our results show that DIAL-MPC reduces the tracking error by $3.9$ times in walking tasks compared to MPPI and outperforms GCRL on all tasks requiring both precision and agility, especially in the presence of significant model mismatch.

<!-- chunk {"id": "body-0047", "role": "body", "section": "EXPERIMENT", "weight": 1.0} -->

We design a set of agile locomotion tasks to showcase the performance of DIAL-MPC: Walking Tracking: a quadruped robot^22^2Detailed information of the hardware setup can be found in Appendix A-A. is tasked with tracking a desired linear velocity and a desired yaw rate, requiring precise control of the torso. Sequential Jumping: a quadruped robot must jump onto a series of small circular platforms placed randomly, each with a radius of $10\ {{cm}\text{/}}$. Crate Climbing: a quadruped robot is tasked with climbing a crate with a height of $60\ {{cm}\text{/}}$, which is more than twice the height of the robot. We leave the specific details of the tasks' implementation in Appendix A-B.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Convergence and Coverage", "weight": 1.0} -->

To answer the question of whether DIAL-MPC is a better solver for the legged MPC problems, we compare the performance of DIAL-MPC with vanilla MPPI, CMA-ES and NMPC. Since vanilla MPPI only uses a single kernel size, we tested both MPPI with large kernel size $0.2$ (MPPI-explore) and small kernel $0.05$ (MPPI-exploit). Compared with DIAL-MPC, CMA-ES optimizes the sampling covariance in an evolutionary way. For all sampling-based MPC methods, we use the same number of samples $N_{W} = 2048$ and optimization steps $H = 20$ ($0.4\ {s\text{/}}$) to ensure a fair comparison. For NMPC, we use Mujoco MPC \[howellPredictiveSamplingRealtime2022\] as our baseline. As a reference, we also include the performance of GCRL, which is trained using PPO \[schulmanProximalPolicyOptimization2017\] over 500 million steps, which takes approximately 31 minutes.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Convergence and Coverage", "weight": 1.0} -->

We share the same reward functions for all methods. Due to unstable exploration in GCRL, we added two additional reward terms to regularize the policy, whereas DIAL-MPC only requires six reward terms.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Convergence and Coverage", "weight": 1.0} -->

Convergence of DIAL-MPC. As shown in table I, DIAL-MPC achieves the best performance across all tasks. Compared with other sampling-based MPC methods (namely MPPI and CMA-ES), DIAL-MPC generates better solutions, with $13.4$ times lower tracking error and $107.7\%$ higher contact reward, thanks to its diffusion-inspired annealing process. For the crate climbing task, DIAL-MPC is the only sampling-based MPC that consistently generates feasible solutions, improving the success rate by $3$ times compared to the best MPPI scheduling. This highlights the superior coverage of the solution space by DIAL-MPC. Compared with NMPC, DIAL-MPC is able to solve tasks requiring higher agility and non-smooth costs, such as sequential jumping and crate climbing, where NMPC is more likely to get stuck in local minima and fail to converge.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Convergence and Coverage", "weight": 1.0} -->

The superior convergence of DIAL-MPC is further demonstrated when compared with GCRL, where DIAL-MPC consistently outperforms GCRL in all tasks even if we use a lower-level leg position controller for RL and DIAL-MPC directly outputs the torque. Although DIAL-MPC is training-free, making a direct comparison potentially unfair, these results showcase the advantage of the annealing process in generating finer solutions compared to the Gaussian exploration in RL.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Convergence and Coverage", "weight": 1.0} -->

Coverage of DIAL-MPC. DIAL-MPC is also capable of searching for non-trivial solutions and generating diverse motions. As examples, we visualize the solutions in the crate climbing task and a humanoid jogging task in Figure 5. DIAL-MPC generates diverse solutions in high-dimensional spaces, thanks to the annealing process.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Test-Time Generalizability", "weight": 1.0} -->

As a training-free method, DIAL-MPC offers better test-time generalizability. Given a new task or model, DIAL-MPC can generate solutions in real time without finetuning.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Test-Time Generalizability", "weight": 1.0} -->

Task-level generalizability. Compared with GCRL, DIAL-MPC reduces the tracking error by $3.9$ times in the walking task and improves the contact reward by $3.5\%$ given different goals. Figure 6 visualizes the tracking performance of both methods. DIAL-MPC achieves higher tracking accuracy thanks to its explicit conditioning on each task, whereas GCRL uses a universal policy for all tasks.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Test-Time Generalizability", "weight": 1.0} -->

Dynamic-level generalizability. Another advantage of DIAL-MPC is its explicit conditioning on the dynamics model, enabling better adaptation to new dynamics given updated models. Figure 6 illustrates the tracking performance of both methods with a $10\ {{kg}\text{/}}$ payload attached to the robot's base. The crate-climbing task is deprecated due to the heavy payload leads to infeasible solutions. The GCRL policy is augmented with domain randomization of mass, actuator gain, and friction to improve robustness to model parameters. Table II shows the performance comparison of GCRL and DIAL-MPC under a $10\ {{kg}\text{/}}$ payload. Without explicit conditioning on the physical parameters, GCRL performs poorly in tracking and completely fails after adding the payload. In contrast, DIAL-MPC outperform GCRL with a larger margin in the jumping task, demonstrating the advantage of explicitly conditioning on the dynamics model. While RL can be enhanced by conditioning on physical parameters or history, this requires additional training time and engineering effort. Conversely, the training-free DIAL-MPC can be instantly deployed with an updated model.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C Robustness to Model Mismatch", "weight": 1.0} -->

When dealing with unknown dynamics models, DIAL-MPC 's robustness stems from the noise injection process in the diffusion-inspired annealing. By controlling the final noise level, we can achieve a suboptimal but robust solution given a mismatched model. Since the sampling-based MPC baselines fail to operate effectively in the real world, we compare the performance of DIAL-MPC with the baseline in simulation with mismatched mass parameters. Table III shows the performance comparison of different methods under $2\ {{kg}\text{/}}$ base mass mismatch in simulation, where DIAL-MPC still outperforms the best sampling-based MPC baselines by $92\%$ in the walking task and $126\%$ in the jumping.

<!-- chunk {"id": "body-0057", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

This work presents DIAL-MPC, a sampling-based MPC method with a diffusion-inspired annealing process to balance coverage and convergence in real-world legged locomotion. DIAL-MPC can solve the full-order control problem efficiently with the help of diffusion process and is generalizable to various tasks and dynamics in a training-free manner. One limitation is that DIAL-MPC requires fast simulation to generate samples, which limits the application of DIAL-MPC in longer planning horizon tasks. In the future, we plan to further accelerate and improve the sample efficiency by learning a nominal policy, value function and model as what has been done in model-base RL.
