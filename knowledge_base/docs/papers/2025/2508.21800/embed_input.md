<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tree-Guided Diffusion Planner

Topics include Robotics, Diffusion models, Generalization, Planning, Control, Sampling, TDP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning with pretrained diffusion models has emerged as a promising approach for solving test-time guided control problems. Standard gradient guidance typically performs optimally under convex, differentiable reward landscapes. However, it shows substantially reduced effectiveness in real-world scenarios with non-convex objectives, non-differentiable constraints, and multi-reward structures. Furthermore, recent supervised planning approaches require task-specific training or value estimators, which limits test-time flexibility and zero-shot generalization. We propose a Tree-guided Diffusion Planner (TDP), a zero-shot test-time planning framework that balances exploration and exploitation through structured trajectory generation. We frame test-time planning as a tree search problem using a bi-level sampling process: diverse parent trajectories are produced via training-free particle guidance to encourage broad exploration, and sub-trajectories are refined through fast conditional denoising guided by task objectives. TDP addresses the limitations of gradient guidance by exploring diverse trajectory regions and harnessing gradient information across this expanded solution space using only pretrained models and test-time reward signals. We evaluate TDP on three diverse tasks: maze gold-picking, robot arm block manipulation, and AntMaze multi-goal exploration.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

TDP consistently outperforms state-of-the-art approaches on all tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Diffusion models offer a data-driven framework for planning, enabling the generation of coherent and expressive trajectories learning from offline demonstrations \[janner2022planningdiffusionflexiblebehavior, liang2023adaptdiffuserdiffusionmodelsadaptive, pmlrv202li23ad, chen2024simplehierarchicalplanningdiffusion\]. Compared to single-step model-free reinforcement learning (RL) methods \[kumar2020conservativeqlearningofflinereinforcement, kostrikov2021offlinereinforcementlearningimplicit\], diffusion planners are more effective for long-horizon planning by generating temporally extended trajectories through multi-step prediction. Without task-specific dynamics models, pretrained diffusion planners can be adapted for test-time planning through guidance functions that provide numerical scores for user requirements such as state conditions or physical constraints.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior studies in diffusion guidance algorithm (e.g., classifier guidance \[dhariwal2021diffusionmodelsbeatgans\]) have been successfully incorporated to generate conditional trajectory samples given test-time reward signals \[janner2022planningdiffusionflexiblebehavior, ajay2023conditionalgenerativemodelingneed\]. These guidance algorithms present an exploration-exploitation trade-off, balancing adherence to the pretrained model for feasibility against maximizing the external guide score, which may require exploring out-of-distribution trajectories.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As the main bottleneck in guided planning lies in the limited quality of trajectory samples produced by the pretrained models, prior works have primarily focused on improving general sample quality and mitigating planning artifacts, while the guidance algorithms themselves remain relatively underexplored. The majority of recent studies on diffusion planners emphasize advancing supervised planning capabilities \[liang2023adaptdiffuserdiffusionmodelsadaptive, pmlrv202li23ad, chen2024simplehierarchicalplanningdiffusion, chen2024diffusionforcingnexttokenprediction, yoon2025montecarlotreediffusion, zhou2025diffusionmodelpredictivecontrol\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

They are categorized into sequential \[chen2024diffusionforcingnexttokenprediction, yoon2025montecarlotreediffusion\], hierarchical \[pmlrv202li23ad, chen2024simplehierarchicalplanningdiffusion\], and fine-tuning \[liang2023adaptdiffuserdiffusionmodelsadaptive, zhou2025diffusionmodelpredictivecontrol\] approaches. These works improve the modeling of the underlying system dynamics from the static offline RL benchmarks. Recent works successfully solve challenging offline benchmarks by reformulating the training scheme, learning value estimator, and test-time scaling. Another recent research direction in diffusion planners aims to enhance zero-shot planning capabilities \[wang2025inferencetimepolicysteeringhuman\]. Test-time tasks are shifted from the training distribution, and planners are given access to a pretrained model along with dense reward signals to adapt to these unseen tasks effectively.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, test-time planning capabilities are often evaluated in relatively simple optimization tasks, such as minimizing the distance to optimal trajectories or matching the outputs of pretrained classifiers trained on expert demonstrations \[janner2022planningdiffusionflexiblebehavior, chen2024simplehierarchicalplanningdiffusion\], and predominantly within in-distribution trajectory settings \[liang2023adaptdiffuserdiffusionmodelsadaptive, chen2024simplehierarchicalplanningdiffusion\]. Typical benchmarks include maze navigation tasks \[chen2024diffusionforcingnexttokenprediction\] where agents minimize distance to a single goal, or block stacking tasks \[janner2022planningdiffusionflexiblebehavior\] where a unique target configuration maximizes reward. These tasks generally involve convex optimization problems, where a unique global optimal trajectory maximizes a smooth guide function.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, similar to model-free RL methods \[wang2020benchmarking\], guided planning often relies on a pretrained value estimator trained on supervised trajectory data; however, collecting optimal trajectories for each new task is often impractical or infeasible, particularly for tasks with complex dynamics or limited simulation control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we address a fundamental challenge of existing diffusion-based planners: while they excel at generating low-level action sequences, most real-world planning tasks require decision-making over high-level abstractions. These abstractions often introduce non-convex guide functions or non-differentiable constraints, making them incompatible with conventional test-time guidance methods that assume smooth, convex optimization landscapes. For example, maze navigation with intermediate goal bypassing \[liang2023adaptdiffuserdiffusionmodelsadaptive\] introduces a non-differentiable rule into the planning process. In multi-reward block stacking, the agent must reconcile multiple configuration-dependent reward signals to determine the most favorable block arrangement. These scenarios underscore the need for guided planning algorithms that flexibly accommodate complex test-time specifications while ensuring both trajectory feasibility and task-specific fitness.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, several training-free guidance algorithms have been proposed in the image domain \[chung2023diffusion, pmlrv202song23k, yu2023freedomtrainingfreeenergyguidedconditional, guo2024gradientguidancediffusionmodels\], but their capabilities are typically restricted to smooth differentiable guide functions. Since test-time guide functions can take any form, there is a need for a flexible planning algorithm that can handle a broad class of guide functions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose Tree-guided Diffusion Planner (TDP), which formulates test-time planning as a tree search problem that balances exploration via diverse trajectory samples and exploitation via guided sub-trajectories. While pretrained diffusion planners model underlying system dynamics, TDP samples high-reward (i.e., high guidance score for the test task) solution trajectories conditioned on the learned dynamics in a zero-shot manner. TDP equips the pretrained diffusion planner model with the ability to reason over higher-level objectives. TDP outperforms state-of-the-art planning methods on challenging tasks with non-convex guide functions and non-differentiable constraints across all test scenarios. TDP enables flexible task-aware planning without requiring expert demonstrations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Existing Diffusion Planners", "weight": 1.0} -->

Sequential approaches \[chen2024diffusionforcingnexttokenprediction, yoon2025montecarlotreediffusion\] explore one action at a time, which works well in single-goal convex tasks but struggles with multi-goal tasks where different goals have varying test-time priorities. In such settings, they often converge on local optima rather than discovering distant, high-priority goals. Furthermore, sequential approaches like MCTD \[yoon2025montecarlotreediffusion\] typically require training task-specific value estimators to guide their single-step decisions, limiting applicability to zero-shot scenarios where no task-specific training is available. In contrast, TDP performs multi-step exploration through diverse bi-level trajectory sampling, which better handles challenging multi-goal scenarios without requiring additional training components beyond the pretrained planner.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Existing Diffusion Planners", "weight": 1.0} -->

Hierarchical diffusion planners \[pmlrv202li23ad, chen2024simplehierarchicalplanningdiffusion\] rely on training-time supervision to learn sub-goal distributions. They perform well when both initial and goal states are given, but struggle on unlabeled zero-shot tasks such as the test-time gold-picking task \[liang2023adaptdiffuserdiffusionmodelsadaptive\]. In standard maze navigation benchmarks, Hierarchical Diffuser \[chen2024simplehierarchicalplanningdiffusion\] tends to generate shortest-path trajectories when initial and goal states are specified. However, the gold-picking task poses a fundamentally different challenge: the goal is *hidden* and often misaligned with the shortest path.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Existing Diffusion Planners", "weight": 1.0} -->

Diffusion model predictive control (D-MPC) \[zhou2025diffusionmodelpredictivecontrol\] adapts to changing dynamics via few-shot fine-tuning with expert demonstrations, but struggles with unseen long-horizon tasks and complex behaviors as standard dynamics models $p{(\left. s \middle| a \right.)}$ struggle to capture long-context reward structures effectively. In contrast, TDP models the joint distribution $p{(s,a)}$ to enable solving long-horizon and multi-goal tasks and is a fully zero-shot planner that operates without test-time demonstrations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Training-free Guidance", "weight": 1.0} -->

Training-free guidance methods leverage structural priors and domain knowledge for control without additional learning. Classical planners (e.g., A\*, potential fields) \[4082128, dijkstra1959note, 5565069, Geraerts2004, Cortés2005\] compute feasible trajectories through graph search or geometric reasoning. In continuous domains, trajectory optimization and model predictive control \[amos2019differentiablempcendtoendplanning, Schwenzer_Ay_Bergs_Abel_2021\] refine actions iteratively using known dynamics. Local search techniques (e.g., hill climbing), guided policy search, and reward shaping \[pmlr-v28-levine13, trott2019keepingdistancesolvingsparse, hu2020learningutilizeshapingrewards\] serve as strong baselines for structured, domain-specific control problems but typically lack the flexibility to generalize beyond narrow task settings. In contrast, diffusion-based test-time planning targets complex tasks that need out-of-distribution generalization and adaptability.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Tree-based Decision Making", "weight": 1.0} -->

Tree structures naturally represent hierarchical sequential decisions. Trajectory Aggregation Tree (TAT) \[feng2024resistingstochasticrisksdiffusion\] mitigates artifacts in diffusion-generated trajectories by aggregating similar states near the initial state, but it struggles with complex long-horizon dependencies due to its limited aggregation depth early in the trajectory. Monte Carlo Tree Search \[\_wiechowski_2022, hennes2015interplanetary, 9036915, NIPS2014_88bf0c64\] explores full-horizon trajectories via stochastic roll-outs, but its reliance on discrete actions and reward heuristics limits scalability in high-dimensional or continuous control tasks with external guidance. In contrast, TDP's bi-level tree framework integrates gradient-based guidance at both parent and child levels, enabling structured and adaptive planning under complex test-time objectives.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We consider the test-time reward maximization problem on a discrete-time dynamics system ${\mathbf{s}}_{t + 1} = {f{({\mathbf{s}}_{t},{\mathbf{a}}_{t})}}$ via a pretrained planner model, where the agent has access to the user-defined guide function $\mathcal{J}{({\mathbf{τ}})}$, which indicates the fitness of the generated trajectory $\mathbf{τ}$. As per-timestep reward does not guarantee the optimality of a low-level action (e.g., non-convex reward landscape), planning capability based on exploration is required to find the optimal trajectory $\hat{\mathbf{τ}}$ that maximizes $\mathcal{J}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Planning horizon $T_{\text{pred}}$ is determined by the choice of planner model. Model-free RL methods with single step execution \[kumar2020conservativeqlearningofflinereinforcement, kostrikov2021offlinereinforcementlearningimplicit\] predict a single action at each timestep so $T_{\text{pred}} = 1$, whereas diffusion planner \[janner2022planningdiffusionflexiblebehavior\] predicts a sequence of actions ${\mathbf{a}}_{1:T_{\text{pred}}}$ at once. As diffusion planners predict more future states, they benefit from capturing longer-term contextual information. For example, in a long-horizon multi-goal navigation task \[pitis2020maximumentropygainexploration\], an agent may encounter several intermediate suboptimal goals, but reaching a farther goal yields a substantially larger reward, requiring planning several steps rather than greedy pursuit of nearby rewards.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Planning over longer horizons can enhance performance on more challenging tasks, particularly when future rewards are more significant \[kaiser2024modelbasedreinforcementlearningatari, Schrittwieser_2020\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Test-time Guided Planning with Diffusion Models", "weight": 1.0} -->

The standard approach to guide diffusion planning in test time is to use naïve gradient guidance \[guo2024gradientguidancediffusionmodels\], which progressively refines the denoising process by combining the score estimate from the unconditional diffusion model with the auxiliary guide function \[janner2022planningdiffusionflexiblebehavior, chen2024simplehierarchicalplanningdiffusion\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Test-time Guided Planning with Diffusion Models", "weight": 1.0} -->

where $g = {{{\nabla_{\tau}\log}h}{({\mathbf{τ}}_{i})}}$ is the gradient of the guidance distribution \[sohldickstein2015deepunsupervisedlearningusing\], $\alpha$ is guidance strength, and $\mu,\Sigma$ are the mean and covariance of the pretrained reverse denoising process. On the other hand, classifier guidance (CG) \[dhariwal2021diffusionmodelsbeatgans\] and classifier-free guidance (CFG) \[ho2022classifierfreediffusionguidance\] are also broadly used in guided planning \[pmlrv202li23ad, ajay2023conditionalgenerativemodelingneed, zhou2023adaptive\]. However, they require access to expert demonstration data to train either a time-dependent classifier model or a conditional diffusion planner model based on trajectory rewards for a given task.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Test-time Guided Planning with Diffusion Models", "weight": 1.0} -->

Despite their simple yet powerful architecture, it is expensive to extend CG and CFG in test-time as it requires collecting expert demonstrations for each new task and retraining the model. The ultimate goal of test-time guided planning is *adaptive* planning, identifying trajectories that satisfy user requirements using a pretrained diffusion planner without additional expert supervision.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Challenges in Guided Planning", "weight": 1.0} -->

Guided planning has primarily been evaluated on simple tasks where expert demonstrations are available or the guide function is convex and differentiable. As a result, prior work has focused on improving the sampling quality of the pretrained diffusion model, which was the main bottleneck for test-time guidance in these simplified settings \[chen2024simplehierarchicalplanningdiffusion, lee2023refining\]. Despite the importance of improving trajectory sampling quality, there has been limited investigation into how guidance algorithms themselves adapt to increasing task complexity and respond to various forms of test-time objectives. In this section, we first study a fundamental challenge in guided planning: the exploitation-exploration trade-off, and then discuss the limitations of naïve gradient guidance, a standard test-time planning approach.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Challenges in Guided Planning", "weight": 1.0} -->

Exploration-Exploitation Trade-off. Test-time guided planning employs two distinct score functions: score estimate from the pretrained diffusion model and a user-defined guide score. Not only to generate a feasible trajectory but also to maximize its fitness, the agent is encouraged to balance the exploitation of the pretrained model and the exploration of novel trajectories. Gradient-based guidance typically requires selecting a guidance strength $\alpha$ to balance adherence to the guide signal and trajectory fidelity. However, $\alpha$ is highly task-dependent, and exhaustive tuning across tasks introduces significant overhead during evaluation. For example, Fig. illustrates several gold-picking tasks within a fixed maze map. The optimal value of $\alpha$ varies across tasks, depending on how far the gold location deviates from the unconditional navigation trajectory, which favors the shortest path (see the supplement for more details).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Challenges in Guided Planning", "weight": 1.0} -->

In-distribution Trajectory Preference. Diffusion models are capable of generating compositional behaviors \[janner2022planningdiffusionflexiblebehavior, du2020compositionalvisualgenerationinference\], but often get stuck in local optima due to insufficient exploration of the trajectory space. Most previous works on guided planning did not adequately address the exploration-exploitation trade-off, as they typically assume convex (or concave) guidance with a single optimal trajectory that globally maximizes the reward \[liang2023adaptdiffuserdiffusionmodelsadaptive, lu2025what\]. However, real-world tasks often involve multiple objectives with different priorities, where the agent must explore the trajectory space to avoid sub-optimality. Pretrained diffusion planners tend to favor generating in-distribution trajectories that align with previously seen data, rather than discovering novel compositional solutions \[chen2024simplehierarchicalplanningdiffusion\]. Consequently, gradient-based guidance algorithms do not effectively address this dilemma, as they often prioritize local optimal trajectories within the learned distribution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Challenges in Guided Planning", "weight": 1.0} -->

Non-differentiable Rule. Gradient-based guidance algorithms face significant challenges in planning tasks with non-differentiable constraints. Since diffusion planners are trained on trajectories with fixed start and end states, they struggle to generate feasible paths that incorporate additional intermediate goals. For example, as described in Fig. -b, navigation trajectories conditioned to test-time intermediate goal often result in suboptimal (left) or infeasible (right). This introduces a non-differentiable constraint from the planner's perspective, as the requirement to pass through a specific state imposes a discrete structural condition not reflected in the training distribution. Similar challenges arise in other domains of diffusion-based generation, such as enforcing chord progression in music generation \[huang2024symbolicmusicgenerationnondifferentiable\] or satisfying chemical rules in molecule generation \[shen2025chemistryinspired\]. Both introduce hard constraints that are difficult to optimize with standard gradient-based methods.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method", "weight": 1.0} -->

We introduce Tree-guided Diffusion Planner (TDP), a zero-shot test-time planning framework leveraging a pretrained diffusion planner for adaptive trajectory generation. While naïve gradient guidance often converges to local optima due to limited gradient signals, TDP addresses this by combining diverse trajectory samples (*exploration*) with gradient-guided sub-trajectories (*exploitation*) to identify optimal solutions. This tree structure enables coverage over a broad range of reward landscapes. By branching into diverse regions, TDP increases the chance of finding globally high-reward solutions that naïve gradient methods may miss.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Method", "weight": 1.0} -->

Appendix˜A, B outline the overall TDP pipeline and present the full algorithms. We detail the core modules of TDP: state decomposition (Sec. 4.1), parent branching (Sec. 4.2), and sub-tree expansion (Sec. 4.3).

<!-- chunk {"id": "body-0030", "role": "body", "section": "State Decomposition", "weight": 1.0} -->

Given a guide function for the test-time task, states are autonomously decomposed based on gradient signals: *observation* states receive non-zero gradients, while *control* states receive none. This gradient-based criterion enables scalable and domain-agnostic decomposition at planning time. *Observation* states are directly steered by the guide function, whereas *control* states are unaffected by the guide function but govern the underlying system dynamics that support high-level objectives.

<!-- chunk {"id": "body-0031", "role": "body", "section": "State Decomposition", "weight": 1.0} -->

For instance, the KUKA robot arm environment provides state vectors containing multiple features such as robot joint angles and block positions. Since TDP operates as a zero-shot planner, it does not have prior knowledge of the state category for each feature of the state vector. Given a test-time block stacking task with a distance-based guide function, TDP autonomously categorizes each feature value in the state vector using Algorithm˜1. It evaluates whether the gradient of the guide function with respect to the *i*th feature (i.e., $\frac{\partial\mathcal{J}}{\partial{\mathbf{s}}_{i}}$) is zero or non-zero. If non-zero, the *i*th feature is classified as an *observation* state; if zero, it is classified as a *control* state. Consequently, features related to robot physics are detected as *control* states. In contrast, block position (xy) features are detected as *observation* states, because the block-stacking guide function is only affected by the block positions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Parent Branching", "weight": 1.0} -->

In the first phase of our bi-level planning framework, *control* states are applied to fixed-potential particle guidance (PG) \[corso2024particle\] to explore diverse *control* trajectories. PG promotes diversity among generated samples within a batch. For instance, when moving a block to a target position, multiple *control* trajectories can accomplish this task. Standard gradient-based approaches often suffer from in-distribution bias and limited exploration, constraining trajectory diversity. In contrast, TDP enhances exploration through this procedure, generating what we term parent trajectories.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Parent Branching", "weight": 1.0} -->

Specifically, fixed-potential PG is implemented using the gradient of a radial basis function (RBF), denoted $\nabla\Phi$, which can be computed directly from all pairwise distances between *control* trajectories within a batch. Unlike conventional gradient guidance methods that pull samples toward high-reward regions, PG introduces repulsive forces that push samples apart in the data space. This leads to a broad coverage of dynamically feasible trajectories independent of task objectives. Although fixed-potential PG incurs some inference overhead from computing kernel values between all trajectory pairs, it is significantly more sample-efficient than learned-potential variants \[corso2024particle\], while remaining training-free and modular.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Parent Branching", "weight": 1.0} -->

where ${\mathbf{μ}}_{\text{control}}^{i}$ and ${\mathbf{μ}}_{\text{obs}}^{i}$ denote the *control* and *observation* components of the predicted mean of the denoising trajectory at timestep $i$. Particle guidance ${\nabla\Phi}{({\mathbf{μ}}_{\text{control}})}$ introduces repulsive updates among *control* states to diversify denoising paths. In contrast, gradient guidance ${\nabla\mathcal{J}}{({\mathbf{μ}}_{\text{obs}})}$ steers *observation* states toward task-relevant regions defined by the guide function. This enables a wide exploration in the *control* state space, which helps to discover diverse *observation* state configurations and exposes the planner to richer gradient signals from the guide function $\mathcal{J}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sub-Tree Expansion", "weight": 1.0} -->

In the second phase, we apply fast denoising with reduced steps $N_{f} \ll N$, where $N$ is the original number of diffusion steps, to refine parent trajectories using task gradient signals. For each parent trajectory, we select a random branch site and generate a child trajectory by denoising from a partially noised version of the parent, conditioned on the preceding segment.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sub-Tree Expansion", "weight": 1.0} -->

where $\mathbf{C}$ denotes the parent trajectory prefix, $q_{N_{f}}$ is the partial forward noising distribution with $N_{f}$ denoising steps, and ${\mathbf{τ}}_{\text{child}}^{N_{f}}$ is the partially noised trajectory from which the child trajectory is denoised during sub-tree expansion. These child trajectories enable fine-grained local search around the parent branch, improving alignment with the guide signal.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sub-Tree Expansion", "weight": 1.0} -->

Enhance dynamic feasibility of parent trajectories: Diverse parent trajectories benefit exploration, but perturbing the *control* states may lead to dynamically infeasible plans. During sub-tree expansion, perturbed *control* states are refined by a pretrained diffusion denoising process.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sub-Tree Expansion", "weight": 1.0} -->

Efficient Local search: Sub-Tree expansion refines *observation* states of parent trajectories with gradient guidance signal. Parent trajectories serve as initial points to guide child trajectories. Since parent trajectories are intended to cover a broad region of search space, local search conditioned on the parent trajectories is an efficient way to find better local optima.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Why is bi-level sampling necessary?", "weight": 1.0} -->

We investigate the role of our bi-level sampling framework in handling multi-reward structures, as illustrated in Fig.. We characterize problems with both local and global optima and demonstrate that bi-level trajectory generation avoids local optima. Consider trajectory data in a learned subspace, where the pretrained diffusion planner maps Gaussian noise back to data space via the reverse denoising process.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate TDP across diverse zero-shot planning tasks featuring non-convex and non-differentiable objectives. Our experiments assess zero-shot planning capabilities and robustness when addressing unseen test-time objectives. All experimental hyperparameters are reported in Appendix D.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

While existing diffusion planners (e.g., MCTD \[yoon2025montecarlotreediffusion\], Hierarchical Diffuser \[chen2024simplehierarchicalplanningdiffusion\]) excel on standard offline benchmarks, they suffer from zero-shot scenarios as discussed in Sec.. Consequently, we focus comparisons on recent zero-shot planning approaches, particularly Trajectory Aggregation Tree (TAT) \[feng2024resistingstochasticrisksdiffusion\], Monte-Carlo sampling \[lu2025what\], and stochastic sampling \[wang2025inferencetimepolicysteeringhuman\]. We design our benchmarks to challenge planners with unseen test-time objectives, in contrast to offline benchmarks that only test learned dynamics aligned with the training distribution.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

For completeness, we provide supplementary comparisons with sequential approaches (i.e., MCTD \[yoon2025montecarlotreediffusion\], Diffusion-Forcing \[chen2024diffusionforcingnexttokenprediction\]) on standard maze benchmarks in Appendix J. Notably, despite being designed specifically for zero-shot planning, TDP still surpasses these sequential approaches on standard benchmarks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

Diffuser \[janner2022planningdiffusionflexiblebehavior\]: Diffusion-based approach that plans by iteratively denoising complete trajectories.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

AdaptDiffuser \[liang2023adaptdiffuserdiffusionmodelsadaptive\]: Fine-tune pretrained Diffuser with synthetic expert demonstrations.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

Diffuser^$\gamma$^ (TAT) \[feng2024resistingstochasticrisksdiffusion\]: Aggregate diffusion samples into a tree structure, bounding trajectory artifacts. Although TAT equips the pretrained Diffuser with better performance in offline RL tasks, its zero-shot planning capability is strictly constrained by standard diffusion sampling.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

Monte-Carlo Sampling with Selection (MCSS) \[lu2025what\]: Sample multiple trajectories from the pretrained Diffuser and select the best trajectory based on the guidance score. Monte Carlo sampling methods effectively explore the solution space and approximate optimal trajectories \[SHAPIRO2003353\].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

Stochastic Sampling (MCSS+SS) \[wang2025inferencetimepolicysteeringhuman\]: MCMC-based, training-free guided planning method requiring $M$ times more computation than MCSS, where $M$ is the number of iterations in the inner loop of diffusion sampling. Following \[wang2025inferencetimepolicysteeringhuman\], we set $M = 4$ in all our experiments.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

TDP (w/o child): Remove the Sub-Tree Expansion phase from TDP, relying solely on parent trajectories generated by conditional PG sampling without further refinement through sub-trajectory sampling. This isolates the contribution of parent trajectories to overall planning performance.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Baselines and Ablations", "weight": 1.0} -->

TDP (w/o PG): Ablate the particle guidance step in Parent Branching, relying solely on gradient guidance to generate parent trajectories. This highlights PG's role in producing diverse parents that serve as initialization points for Sub-Tree Expansion.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Maze2d Gold-picking", "weight": 1.0} -->

We extend the single gold-picking example \[liang2023adaptdiffuserdiffusionmodelsadaptive\] in the Maze2D environment \[fu2021d4rldatasetsdeepdatadriven\] to a multi-task benchmark. The agent is initialized at a random position in the maze and has to find the gold at least once before it reaches the final goal position. As discussed in Sec. 3.3, the gold-picking task is a planning problem with a test-time non-differentiable constraint, where the agent must generate a feasible trajectory that satisfies an initial state, a final goal state, and an intermediate target (the gold position). In addition, the task is a *black-box* problem that requires inferring the intermediate goal (i.e., gold) location using only a distance-based guide function, without access to the gold's exact position.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Maze2d Gold-picking", "weight": 1.0} -->

While this approximate function is used for the gradient guidance sampling, the true guide function ${\mathcal{J}{({\mathbf{τ}})}} = {- {\min\limits_{i \in {\{ 1,\cdots,T_{\text{pred}}\}}}\left\| {{\mathbf{s}}_{i} - {\mathbf{s}}_{\text{gold}}} \right\|}}$ is used for selecting the best one from the generated candidates. We report the performance of TDP and baselines in Table˜1. TDP consistently outperforms both Diffuser^$\gamma$^ and MCSS across single- and multi-task settings. Notably, even TDP (w/o child) achieves approx. a 7% performance improvement over MCSS overall. TDP generates farther sub-trajectories through sub-tree expansion, allowing the planner to localize the gold position better and collect stronger gradient signals from the surrounding region to guide the trajectory effectively. This bi-level trajectory sampling approach enables the discovery of the *hidden* gold location within the map.

<!-- chunk {"id": "body-0052", "role": "body", "section": "KUKA Robot Arm Manipulation", "weight": 1.0} -->

We evaluate the test-time planning performance of TDP and baselines on robotic arm manipulation tasks. Diffusion planners are pretrained on arbitrary block stacking demonstrations collected from PDDLStream \[garrett2020pddlstreamintegratingsymbolicplanners\] and are typically evaluated on downstream tasks such as conditional stacking \[janner2022planningdiffusionflexiblebehavior\] and pick-and-place \[liang2023adaptdiffuserdiffusionmodelsadaptive\], where test-time goals are specified to the planner. Both tasks aim to place randomly initialized blocks into their corresponding target locations in a predetermined order. The pick-and-place task is more challenging because it requires placing each block at a unique target without access to expert demonstrations. To better isolate test-time planning capability, we evaluate a variant of the conditional stacking task \[liang2023adaptdiffuserdiffusionmodelsadaptive\] without using the pretrained classifier on expert data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "KUKA Robot Arm Manipulation", "weight": 1.0} -->

We refer to this variant as PnP (*stack*), and the original task is denoted as PnP (*place*). For both tasks, the pretrained diffusion planner is guided to generate 4 sequential manipulation trajectories, one for each block, toward its target location ${\mathbf{s}}_{\text{target}}$, using a naïve guidance objective defined as ${\mathcal{J}{({\mathbf{τ}})}} = {- {\sum_{i}\left\| {{\mathbf{s}}_{i} - {\mathbf{s}}_{\text{target}}} \right\|}}$. As shown in Table˜2, TDP achieves an average improvement of 10% over MCSS and 20% over TAT in two PnP tasks, demonstrating strong generalization to diverse task configurations. Notably, TDP (w/o PG) outperforms MCSS by 18% on PnP (*place*), underscoring the role of our sub-trajectory refinement mechanism in such out-of-distribution planning scenarios.

<!-- chunk {"id": "body-0054", "role": "body", "section": "KUKA Robot Arm Manipulation", "weight": 1.0} -->

Moreover, we carefully design a more challenging test-time manipulation task which extends PnP (*place*), namely pick-and*-where-to-*place (PnWP).

<!-- chunk {"id": "body-0055", "role": "body", "section": "KUKA Robot Arm Manipulation", "weight": 1.0} -->

Both ${\mathbf{s}}_{\text{global}}$ and ${\mathbf{s}}_{\text{local}}$ are equidistant from the robot arm's attachment point. Since the local optimum has a wide peak while the global optimum has a narrow peak, agents easily get trapped in local optima without sufficient exploration. While PnP requires fitting blocks into a target configuration, PnWP challenges planners to distinguish between globally optimal and suboptimal arrangements.

<!-- chunk {"id": "body-0056", "role": "body", "section": "KUKA Robot Arm Manipulation", "weight": 1.0} -->

We report the performance of TDP, baselines, and ablations in Table˜2. Mono-level guided sampling methods (i.e., AdaptDiffuser, MCSS(+SS), TAT, and TDP (w/o child)) tend to converge to local optima, often stacking all blocks at a single position, since a landscape of local optima is spread out in a broader range as shown in Fig.. In contrast, bi-level sampling approaches (i.e., TDP and TDP (w/o PG)), which combine parent branching and sub-trajectory refinement, are better able to identify globally optimal placements consistently. Notably, TDP outperforms AdaptDiffuser both on the standard benchmark (PnP) and on the custom task (PnWP). This demonstrates that TDP's test-time scalability and generalization enable zero-shot planning that surpasses the training-per-task approach.

<!-- chunk {"id": "body-0057", "role": "body", "section": "KUKA Robot Arm Manipulation", "weight": 1.0} -->

The key advantage of our method over the baselines comes from employing unconditional PG in the parent branching phase, enabling broad exploration of the trajectory space. Both TDP and its ablations produce diverse trajectories; however, TDP (w/o child) often fails to find the global optimal placement due to the use of conditional PG in parent branching, which can bias samples toward local optima. The mean pairwise trajectory distance decreases when PG is combined with sub-tree expansion, as the generated sub-trajectories share segments with their corresponding parent trajectories. Unconditional PG enables the generation of diverse, gradient-free parent trajectories. When combined with sub-tree expansion guided by the objective, this bi-level strategy supports compositional solutions that successfully stack blocks into global optimal placement. More detailed information on the evaluation metrics among these tasks is available in Appendix˜F.

<!-- chunk {"id": "body-0058", "role": "body", "section": "AntMaze Multi-goal Exploration", "weight": 1.0} -->

We finally evaluate test-time multi-goal exploration capability on AntMaze \[fu2021d4rldatasetsdeepdatadriven\], which is more challenging than Maze2D due to its high-dimensional observation space for controlling the embodied agent. Its complexity causes the pretrained diffusion planner to predict shorter horizons than the full trajectory length \[dong2024cleandiffuser\].

<!-- chunk {"id": "body-0059", "role": "body", "section": "AntMaze Multi-goal Exploration", "weight": 1.0} -->

If it subsequently visits $g_{1}$, $g_{4}$, and $g_{3}$ after $t = t_{3}$, it successfully reaches all four goals in the sequence $g_{2}\rightarrow g_{1}\rightarrow g_{4}\rightarrow g_{3}$. However, two precedence rules are violated ($g_{2}\rightarrow g_{1}$, $g_{4}\rightarrow g_{3}$) while the remaining four ($g_{2}\rightarrow g_{4}$, $g_{2}\rightarrow g_{3}$, $g_{1}\rightarrow g_{4}$, and $g_{1}\rightarrow g_{3}$) are satisfied. In this scenario, the agent achieves a goal completion score of 4/4 but only 4/6 priority sequence match accuracy. Maximum accuracy of 6/6 can only be achieved by visiting all goals in the correct prioritized order.

<!-- chunk {"id": "body-0060", "role": "body", "section": "timesteps per goal ↓", "weight": 1.0} -->

We report the performance of TDP, baselines, and ablations in Table˜3 using three metrics, with detailed definitions in Appendix˜F. TDP achieves about 11% improvements over MCSS in both the number of found goals and the sequence match score, while also reducing timesteps per goal. The ablations highlight complementary roles of the components: when PG is removed (TDP (w/o PG)), all three metrics degrade, confirming that PG is essential for both goal discovery and sequence alignment. In contrast, removing child branching (TDP (w/o child)) maintains performance on the first two metrics but requires more timesteps per goal, suggesting less efficient exploration in the environment.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In summary, we propose TDP, a flexible test-time planning framework that leverages a pretrained diffusion planner via a bi-level trajectory-sampling process without training. By balancing trajectory diversity and gradient-guided refinement via a branching structure of sampled trajectories, our method addresses key limitations of conventional test-time-guided planning. Empirical results across both structured and compositional manipulation tasks demonstrate consistent performance gains over existing baselines, particularly in scenarios that demand out-of-distribution generalization. Our experiments also highlight the robustness of the framework in handling non-convex, multi-objective guidance and non-differentiable constraint problems, where naïve gradient guided methods often fail.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Limitation and Future Work", "weight": 1.5} -->

While TDP outperforms existing planning approaches across a suite of challenging test-time control tasks, our bi-level trajectory generation process incurs additional computational cost due to the expanded search in trajectory space and the pairwise trajectory distance calculations. We analyze the additional computational time required for the two PnP tasks and the PnWP task in Appendix˜G. Future work may explore more efficient search strategies or learned priors to reduce overhead while ensuring sufficient exploration and preserving planning performance.
