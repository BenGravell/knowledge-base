<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Uncertainty Guided Exploratory Trajectory Optimization for Sampling-Based Model Predictive Control

Topics include Model predictive control, Predictive control, Trajectory optimization, Robustness, Uncertainty, Sampling-based methods, Optimization, Control, Sampling, UGE-TO.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization depends heavily on initialization. In particular, sampling-based approaches are highly sensitive to initial solutions, and limited exploration frequently leads them to converge to local minima in complex environments. We present Uncertainty Guided Exploratory Trajectory Optimization (UGE-TO), a trajectory optimization algorithm that generates well-separated samples to achieve a better coverage of the configuration space. UGE-TO represents trajectories as probability distributions induced by uncertainty ellipsoids. Unlike sampling-based approaches that explore only in the action space, this representation captures the effects of both system dynamics and action selection. By incorporating the impact of dynamics, in addition to the action space, into our distributions, our method enhances trajectory diversity by enforcing distributional separation via the Hellinger distance between them. It enables a systematic exploration of the configuration space and improves robustness against local minima. Further, we present UGE-MPC, which integrates UGE-TO into sampling-based model predictive controller methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiments demonstrate that UGE-MPC achieves higher exploration and faster convergence in trajectory optimization compared to baselines under the same sampling budget, achieving 72.1% faster convergence in obstacle-free environments and 66% faster convergence with a 6.7% higher success rate in the cluttered environment compared to the best-performing baseline. Additionally, we validate the approach through a range of simulation scenarios and real-world experiments. Our results indicate that UGE-MPC has higher success rates and faster convergence, especially in environments that demand significant deviations from nominal trajectories to avoid failures. The project and code are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization is a powerful concept in robotics for generating efficient robot motions under task-specific objectives. it has been successfully applied to applications including navigation, manipulation, and aerial robotics. Classical gradient-based methods focus on smooth settings, where differentiability can be exploited for efficient optimization, and have demonstrated strong performance in such settings -. However, their reliance on differentiability limits their direct use in complex multimodal environments. In contrast, sampling-based approaches relax these assumptions by allowing non-differentiable cost functions, making them applicable to a broader range of robotic systems and tasks. They are most commonly applied in Model Predictive Control (MPC) settings since they can handle nonlinear dynamics with arbitrary cost functions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these advantages, sampling-based methods remain highly sensitive to the selection of the underlying sampling distribution and the initialization. For example, Model Predictive Path Integral (MPPI) samples action sequences from a Gaussian distribution centered on the nominal trajectory, resulting in trajectories that are concentrated around it. As a result, when the distribution lacks sufficient diversity or the nominal trajectory is poorly initialized, the resulting trajectories may fail to cover promising areas of the configuration space. This often leads to convergence to local minima and reduces the controller's reliability in complex environments. Addressing this limitation is crucial to enhancing the robustness of sampling-based approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several methods have been proposed in the literature to enhance exploration, thereby improving the reliability of the methods. Early approaches directly modify the sampling distribution to encourage broader exploration. For example, Log-MPPI, which increases trajectory diversity by reshaping the underlying distribution. Another line of work is to incorporate entropy-based regularization terms into the objective to promote diversity in the resulting policies, thereby penalizing narrow policy distributions. More recently, multimodal approaches have been presented to capture a distribution over trajectories rather than a single solution. A class of approaches uses Stein Variational Gradient Descent (SVGD), which uses particles to approximate multimodal trajectory distributions by the repulsive feature of SVGD to maintain the diversity among trajectories, while shifting them toward low-cost regions. While these methods improve exploration, they often rely solely on action-space perturbation and may not fully capture the impact of system dynamics on trajectory diversity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present a new exploration technique that extends the idea of exploration via action perturbations by accounting for the impact of long-range system dynamics. Specifically, we introduce Uncertainty Guided Exploratory Trajectory Optimization (UGE-TO) that constructs probability distributions for trajectories by using uncertainty ellipsoids around trajectories. After the trajectory distributions are constructed, we enforce distributional separation using the Hellinger Distance to reduce overlap between the distributions. In other words, it will lead to exploration of the configuration space by forcing trajectories to visit distinct regions of the configuration space. We further present UGE-MPC, which integrates UGE-TO into a sampling-based MPC framework. In this setting, we use UGE-TO to generate diverse trajectory candidates and identify a better nominal trajectory, which helps the controller to perform a local search around low-cost regions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Uncertainty Guided Exploratory Trajectory Optimization (UGE-TO), which utilizes the distribution separation of trajectory probability distributions generated by uncertainty ellipsoids to effectively explore the configuration space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present UGE-MPC, a new sampling-based model predictive controller that utilizes UGE-TO to enhance exploration of representative trajectory rollouts and then performs a local search around the selected minimum cost one. By achieving high exploration of the configuration space, our method reduces the likelihood of becoming trapped in local minima.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate our approach in simulation and real-world scenarios, demonstrating improved exploration, faster convergence, and higher success rates compared to baselines, particularly in environments requiring significant deviations from nominal trajectories.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integrating UGE-TO into a sampling-based MPC (UGE-MPC) provides a systematic approach that augments exploration with local search to refine exploitation. We begin with an overview of the related work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Trajectory Optimization", "weight": 1.0} -->

Existing approaches to local trajectory optimization can be divided into two branches: direct and indirect methods. One approach is to use direct methods that translate the optimization problem into a nonlinear problem and solve it with nonlinear solvers, such as IPOPT and SNOPT. On the other side, indirect methods aim to convert the problem into subproblems and solve for the local optimality conditions. Differential dynamic programming (DDP) and iterative Linear Quadratic Regulator (iLQR) are well-known examples of this method. A major limitation of both methods is their strong dependence on initialization. Since they seek to find a single local-optimal solution, this property increases the importance of the initialization. Later work combines maximum entropy policies with DDP and avoids local minima via exploration capacity of their multimodal policy,. Similarly, CSVTO uses Stein Variational Gradient Descent (SVGD) to generate a diverse set of trajectories to avoid possible local minima. Our work also aligns with this line of research by aiming to overcome the limitations of a single local solution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Trajectory Optimization", "weight": 1.0} -->

However, in contrast to these methods that rely on convexity or differentiability of the cost functions, we focus on sampling-based approaches that naturally handle non-convex and non-differentiable objectives. This allows us to enhance diversity and robustness in trajectory optimization without depending on restrictive assumptions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Sampling-Based Trajectory Optimization", "weight": 1.0} -->

Sampling-based approaches have gained popularity and become state-of-the-art for handling non-smooth cost landscapes by directly evaluating candidate control sequences drawn from their distributions. Early methods, such as the Cross-Entropy Method (CEM) and Model Predictive Path Integral control (MPPI), demonstrated strong performance across various robotic systems by iteratively adapting their action-sampling distributions based on rollout costs. However, similar to gradient-based methods, these approaches also struggle with local minima in the cost landscape due to their limited exploration in the configuration space. Recent works have sought to address these issues by improving sampling strategies. One line of research focused on directly modifying the sampling distribution. Log-MPPI leverages the Normal-Log-Normal (NLN) distribution to increase the sample diversity. Similarly, colored-noise-based variants use correlated noises to generate both smoother and diverse trajectories,. Although these methods have increased the exploration capabilities, they still rely on unimodal sampling strategies that lead to a single solution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Sampling-Based Trajectory Optimization", "weight": 1.0} -->

On the other hand, another class of methods introduces multimodal sampling distributions. In the SVGD-based approach, SV-MPC uses particle approximations of trajectories to represent a multimodal trajectory distribution with multiple particles. SV-MPC's MPPI extension, SVG-MPPI, guides trajectories to low-cost regions by modifying both the nominal trajectory and the covariances. Similarly, C-Uniform trajectory sampling has been presented to maintain uniform coverage of configurations over level sets, and that leads to high exploration over the configuration space. Its extension, CU-MPPI, incorporates C-Uniform trajectories for better nominal trajectory selection into the MPPI framework to avoid local minima. In contrast, UGE-MPC applies Hellinger distance--based separation directly in the space of trajectory distributions, ensuring diversity under both actions and dynamics. This approach avoids the scalability limitations of entropy-based grid methods, such as CU-MPPI, while providing more principled configuration-space clustering than action-level kernels, like SV-MPC.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Sampling-Based Trajectory Optimization", "weight": 1.0} -->

Another method closely related to our work is U-MPPI, which utilizes the unscented transform to enhance state-space exploration. Compared with U-MPPI, our method also uses uncertainty ellipsoids, but unlike U-MPPI, we explicitly represent trajectories as probability distributions and separate them distributionally using the Hellinger Distance-based metric. This property explicitly prevents overlap between trajectory distributions, which promotes exploration and reduces the likelihood of collapsing into a local minimum.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We begin by formulating trajectory optimization as a general stochastic optimal control problem, where $\mathbf{x}_{t} \in {\mathbb{R}}^{n}$ denotes the system state and $\mathbf{u}_{t} \in {\mathbb{R}}^{m}$ denotes the control input at discrete time step $t$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $f$ represents nonlinear dynamics, and $\mathbf{\epsilon}_{t}$ captures process noise modeled as zero-mean Gaussian distribution with covariance Q.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $c{( \cdot, \cdot )}$ is the running cost and $\phi_{T}{( \cdot )}$ is the terminal cost. While the above formulation formulates the general setting, solving it requires systematic exploration. To this end, we introduce Uncertainty Guided Exploratory Trajectory Optimization (UGE-TO).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Uncertainty Guided Exploratory Trajectory Optimization", "weight": 1.0} -->

In this section, we explain the core concepts of UGE-TO. It has two main stages. First, a set of candidate trajectories is generated by perturbing the nominal control sequence. Then, each trajectory is represented as a distribution by propagating its mean state and uncertainty ellipsoids through the system dynamics. This propagation captures both process noise and action selection. In the second stage, these trajectories are refined through a distributional separation step, where the Hellinger distance is used to measure the overlap between distributions. Fig. 2 demonstrates how these distributions are getting separated through time. Minimizing this overlap encourages diversity in trajectories, allowing them to cover more unique areas in the configuration space while maintaining their dynamic feasibility. Alg. 1 shows the pseudocode of a single iteration of the optimization method. Finally, the resulting set of trajectories will be used as a nominal trajectory selection for the sampling-based MPC, which is explained in detail in Sec. V. We start with the formulation of trajectory distribution modeling.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Trajectory Distribution Modeling", "weight": 1.0} -->

We approximate trajectory uncertainty by propagating the covariance forward using the linearized dynamics. With $A_{t}^{(i)} = \left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Distributional Separation", "weight": 1.0} -->

which yield trajectory distributions $\mathcal{T}^{(i,m)}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Distributional Separation", "weight": 1.0} -->

Each candidate is evaluated by measuring its dissimilarity to the other trajectories. We use the squared Hellinger distance to quantify distributional overlap because it is symmetric and bounded in $\lbrack 0,1\rbrack$, unlike KL-type divergences, which can be unbounded.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Distributional Separation", "weight": 1.0} -->

This separation procedure is repeated for $K$ iterations to enhance the diversity of the trajectory set.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

We now incorporate the proposed UGE-TO into a sampling-based Model Predictive Controller. We use the Model Predictive Path Integral (MPPI) algorithm as the baseline, and augment it with the UGE-TO.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

We start with the initialization of a nominal control sequence $\overline{\mathbf{U}} = {\{{\overline{\mathbf{u}}}_{0},\ldots,{\overline{\mathbf{u}}}_{T - 1}\}}$. It is either initialized as a zero control sequence or it is obtained from the previous iteration. After the initialization, we apply the UGE-TO procedure described in Alg. 1 to the nominal trajectory to generate distributionally separated trajectories that remain diverse and explore a broad region of the state space.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

Input: Nominal sequence $\overline{\mathbf{U}}$, horizon T, refinement size N, M, rollout size L, covariances Σu, Q, temperature λ Output: Updated nominal control sequence $\overline{\mathbf{U}}$ 2Apply UGE-TO($\overline{\mathbf{U}},T,N,M,\Sigma_{u},Q)\quad\leftarrow Alg.$ 3 Evaluate J (U(i)) for all i 4 Select the best rollout: i⋆ = arg miniJ (U(i)) 5 Update nominal: $\overline{\mathbf{U}}\leftarrow\mathbf{U}^{(i^{\star})}$ 8 Sample ${\mathbf{U}^{(l)} = {\overline{\mathbf{U}} + \eta^{(l)}}},{\eta^{(l)} \sim {\mathcal{N}{(0,\Sigma_{u})}}}$ 9

<!-- chunk {"id": "body-0028", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

Propagate U(l) through dynamics f to obtain X(l) 12Compute weights w(l) = exp (−J (U(l))/λ) 13 Update nominal: $\overline{\mathbf{U}}\leftarrow{\overline{\mathbf{U}} + \frac{\sum_{l}{w^{(l)}\eta^{(l)}}}{\sum_{l}w^{(l)}}}$ Algorithm 2 Uncertainty-Guided Exploratory MPC (UGE-MPC)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

After refinement, each trajectory $\mathbf{U}^{(i)}$ is evaluated using the cost function in Eq. 2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

This emphasizes that the nominal trajectory is directly related to the lowest-cost feasible rollout after diversity enforcement. After the new nominal control sequence.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

Each sequence is propagated through the dynamics $f$ in Eq. 1 obtain trajectories $\mathbf{X}^{(l)}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Uncertainty Guided Exploratory Model Predictive Control", "weight": 1.0} -->

Since UGE-TO only affects the nominal control sequence, we kept the MPPI update rule unchanged. Finally, after obtaining the MPPI solution, we apply the first control ${\overline{\mathbf{u}}}_{0}$ to the system, as in general MPC practice, and then shift the control sequence horizon. This procedure repeats until the stopping conditions are met.

<!-- chunk {"id": "body-0033", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We evaluate the UGE-MPC algorithm by studying the following questions through experiments.

<!-- chunk {"id": "body-0034", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Can the UGE-MPC converge to a solution when initialized from a poor warm start, including cases where the initial control sequence drives the system in a direction opposite to the goal? (Sec. VI-B)

<!-- chunk {"id": "body-0035", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Can the UGE-MPC algorithm adapt and perform reliably in dynamic and complex environments in both simulation and real-world end-to-end navigation scenarios? (Secs. VI-C, VI-D)

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A1 Baselines", "weight": 1.0} -->

To evaluate our approach, we compare against three baseline controllers of increasing complexity: Model Predictive Path Integral control (MPPI), MoG-MPPI, and Stein Variational MPC (SV-MPC). MPPI samples action sequences through a unimodal Gaussian distribution. MoG-MPPI extends this by introducing multiple Gaussian components to capture multimodality. Finally, SV-MPC adds a repulsion term among particles to encourage diversity. This progression of baselines demonstrates the incremental effects of adding multimodality and repulsion, and provides a benchmark for assessing our distributional separation in the configuration space. All methods use the same trajectory sampling budget. We evaluate every method with a fixed number of trajectory samples to ensure a fair comparison. MoG-MPPI and SV-MPC use $16$ particles, each with $128$ samples. We adopt the same particle settings but adjust the sample allocations proportionally to the number of iterations, ensuring that the total budget remains constant while accounting for iterative updates. All baselines are implemented based.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A2 Cost Function", "weight": 1.0} -->

The cost function $J$ has two main components: The state cost $\mathcal{C}_{\text{state}}{(x_{t})}$, which includes both obstacle $\mathcal{C}_{\text{obs}}{(x_{t})}$ and distance-to-goal cost $\mathcal{C}_{\text{dist}}{(x_{t},x_{\text{goal}})}$. On the other hand, the second term is the action regulator $\mathcal{C}_{\text{u}}{(u_{t})}$, which smoothes the action to reduce jitter in the resulting trajectory. Corresponding weights are assigned to each component to give relative importance to each term.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A2 Cost Function", "weight": 1.0} -->

where the indicator variable acts as a switch, if a state is in a collision, it will turn the remaining part of the trajectory into a collision, and the distance to goal value of the collided state is used as the distance-to-goal cost for the remaining part of the trajectory. $\mathcal{C}_{\text{collided}} = 10^{3}$ is the maximum collision cost, and $\mathcal{C}_{\text{obs}}{(\mathbf{x}_{t}^{\tau})}$ calculates the cost of the robot footprint of the state based on the local costmap. The term $\mathcal{C}_{\text{dist}}$ denotes the distance-to-goal cost of the state where the collision occurred along a trajectory $\tau$. It is important to note that if any state in a trajectory $\tau$ reaches the goal, we stop the cost calculation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-A2 Cost Function", "weight": 1.0} -->

This means the trajectory cost is measured only up to the goal-reaching state and terminal cost is calculated as ${\phi{(\mathbf{x}_{T})}} = {\mathcal{C}_{\text{state}}{(\mathbf{x}_{g}^{\tau},\mathbf{x}_{\text{G}})}}$ where $\mathbf{x}_{g}$ is the first goal reaching state along a trajectory $\tau$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-B Trajectory Optimization", "weight": 1.0} -->

In this experiment, we evaluate the performance of the proposed approach compared to baseline methods in settings where the goal is reachable within the prediction horizon. This setting transforms the MPC formulation into a full, dynamically feasible trajectory optimization problem.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B Trajectory Optimization", "weight": 1.0} -->

We consider two 8x8 m environments: (i) an obstacle-free space and (ii) a cluttered environment. Fig. 3 demonstrates the cluttered environment and the goal positions. The kinematic bicycle model is used for the dynamics. The start configuration is ${\lbrack x,y,\theta\rbrack} = {\lbrack 0,0,0\rbrack}$ and the goal positions are selected in a circular manner to enforce nontrivial and challenging steering and velocity profiles. The nominal trajectory is initialized as a straight-line trajectory along the $+ x$ direction, with a linear velocity $v = {{0.5m}/s}$, and a steering angle, $\delta = 0$. The trajectory horizon is $T = {4s}$ with the time discretization, ${\Deltat} = {0.05s}$. Method parameters are set as follows: the temperature value for MPPI iterations is $\alpha = 0.001$, and the epsilon value for SV-MPC is $\epsilon = 1.0$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Trajectory Optimization", "weight": 1.0} -->

In this experiment, we use the cost function $J$ as in Eq. 14 without the action regularization term. The weights for the state and obstacle cost are assigned as follows: $\lambda_{\text{obs}} = 50$, and $\lambda_{\text{dist}} = 10$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Trajectory Optimization", "weight": 1.0} -->

We run 10 trials for each start-goal pair for every method. The maximum number of iterations is set to 100. If a method does not find a solution that reaches the goal within this limit, the trial is considered a failure. In Table I, we report the average success rates and the average first goal reaching time. We highlight the best-performing methods in bold. The results indicate that, in the obstacle-free setting, every method can successfully generate trajectories that reach the goals. UGE-MPC outperforms all baselines in terms of average goal reaching time. This performance directly highlights that configuration space exploration helps find a candidate trajectory that reaches the goal more quickly than all baselines. Among the baselines, MPPI outperforms the other two multimodal methods in open-environment settings, where it selects a single mode, whereas the other baselines spend more time exploring multiple modes before converging.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Trajectory Optimization", "weight": 1.0} -->

Fig. 4 demonstrates the trajectories generated by each method in the cluttered environment. Each start and goal pair's trajectories are colored differently, where dashed lines show the corresponding unsuccessful runs. In the cluttered environment scenario, UGE-MPC has achieved a higher success rate and lower average time compared to the baselines. On the other hand, in contrast to open space, now multimodal methods overperform the MPPI. Due to the unimodal structure of MPPI, it struggles to explore the environment, especially when the nominal trajectory is far from the optimal trajectory (The left-center goal in Fig. 3). At the same time, other baselines can shift their trajectories. Overall, these results demonstrate that our method, UGE-MPC, achieves high success rates while comparably lower goal-reaching time, making it both efficient and robust in complex environments.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-C Model Predictive Control in Cluttered Environments", "weight": 1.0} -->

In this experiment, we analyzed the performance of our method against baselines in unknown cluttered environments. No prior map information was provided. We evaluated a point-to-point navigation task performance in settings where the vehicle only uses the local costmap derived from the lidar sensor footprint as a sensory input. To increase complexity, each environment (20x20m) was generated with concave polygonal obstacles, which introduced local traps in the environment. The start ($\lbrack 2,2,{\pi/2}\rbrack$) and goal ($\lbrack 18,18\rbrack$) positions are fixed for this experiment. The lidar sensor range was set to 10m, and each controller was run 10 times per environment to capture its behavior. Similarly to the previous trajectory optimization setting, we use trajectories with a $T = {4s}$ horizon with $0.05s$ as the time discretization. We set method-based hyperparameters as follows: $\alpha = 10^{- 3}$ for the MPPI temperature parameters.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-C Model Predictive Control in Cluttered Environments", "weight": 1.0} -->

The cost function Eq. 14 without the action regularization term is used for this experiment, and the corresponding weights for obstacle and state cost are selected by $\lambda_{\text{obs}} = 10^{3}$, and $\lambda_{\text{dist}} = 10$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-C Model Predictive Control in Cluttered Environments", "weight": 1.0} -->

Fig. 5 shows an instance where UGE-TO helps to generate diverse trajectories and shifts the nominal trajectory to one that avoids failure. Among these methods, UGE-MPC explored alternative configurations more effectively by explicitly encouraging distributional separation. That produces shorter and more direct trajectories. Table II summarizes the average success rate and goal-reaching time across successful runs.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-D Real-World Experiments", "weight": 1.0} -->

We further evaluated our approach on a real-world point-to-point navigation task in a cluttered, unknown environment with fixed start and goal positions. We compared our method against two baselines, MPPI and log-MPPI, with five trials per method under a fixed sample budget of $N = 512$. We allocated $126$ samples for the final MPPI iterations, using the remaining budget to generate $6$ candidate particles with $8$ iterations of UGE-TO. MPPI and log-MPPI covariances are both set to $\Sigma = {\lbrack 1.0,10^{\circ}\rbrack}$. Since log-MPPI uses a normal-log-normal distribution, it has higher exploration than MPPI. All controllers were run at 10 Hz to match the frequency of the onboard Slamtec R2 LiDAR. The $1/5$-scale vehicle and the environment are shown in Fig. 7. Since SV-MPC and MoG-MPPI could not be executed consistently at the LiDAR frequency, they were excluded from the trials.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-D Real-World Experiments", "weight": 1.0} -->

In all trials, MPPI became trapped in a local minimum and failed to reach the goal. Both log-MPPI and UGE-MPC consistently succeeded with average times $14.13s$ and $13.33s$, respectively. Under this setup, we did not observe a significant performance gap between log-MPPI and our approach.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-D Real-World Experiments", "weight": 1.0} -->

In summary, we conclude that the diversification of candidate nominal trajectories provided by our method is a viable approach to improve MPPI performance and avoid local minima.

<!-- chunk {"id": "body-0051", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this work, we introduced Uncertainty Guided Exploratory Trajectory Optimization (UGE-TO) and its integration into a sampling-based model predictive control framework, UGE-MPC. We modeled trajectories as probability distributions and corresponding uncertainty ellipsoids. By distributionally separating them using a metric based on the Hellinger distance, our method enables systematic exploration of the configuration space beyond what existing action-space perturbation techniques can achieve. Through simulation and real-world experiments, we demonstrated that in most cases, UGE-MPC achieves higher success rates and faster convergence compared to MPPI, MoG-MPPI, and SV-MPC under the same sampling budget. In our future work, we aim to demonstrate UGE-MPC in much higher-dimensional systems, such as humanoid robots.
