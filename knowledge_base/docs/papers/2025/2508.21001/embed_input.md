<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Train-Once Plan-Anywhere Kinodynamic Motion Planning via Diffusion Trees

Topics include Motion planning, Robotics, Safety, Robustness, Diffusion models, Sampling-based methods, Search trees, Generalization, Planning, Learning, Sampling, Diffusion trees, Out-of-distribution, OOD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Kinodynamic motion planning is concerned with computing collision-free trajectories while abiding by the robot's dynamic constraints. This critical problem is often tackled using sampling-based planners (SBPs) that explore the robot's high-dimensional state space by constructing a search tree via action propagations. Although SBPs can offer global guarantees on completeness and solution quality, their performance is often hindered by slow exploration due to uninformed action sampling. Learning-based approaches can yield significantly faster runtimes, yet they fail to generalize to out-of-distribution (OOD) scenarios and lack critical guarantees, e.g., safety, thus limiting their deployment on physical robots. We present Diffusion Tree (DiTree): a provably-generalizable framework leveraging diffusion policies (DPs) as informed samplers to efficiently guide state-space search within SBPs. DiTree combines DP's ability to model complex distributions of expert trajectories, conditioned on local observations, with the completeness of SBPs to yield provably-safe solutions within a few action propagation iterations for complex dynamical systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate DiTree's power with an implementation combining the popular RRT planner with a DP action sampler trained on a single environment. In comprehensive evaluations on OOD scenarios, DiTree achieves on average a 30% higher success rate compared to standalone DP or SBPs, on a dynamic car and Mujoco's ant robot settings (for the latter, SBPs fail completely). Beyond simulation, real-world car experiments confirm DiTree's applicability, demonstrating superior trajectory quality and robustness even under severe sim-to-real gaps.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotic mobility has been a longstanding goal in artificial intelligence, pivotal for real-world applications such as autonomous driving, drones, and humanoid robots. Such systems are often underactuated, requiring motion planners to account not only for environmental constraints but also for the physical limitations and dynamics of the robot itself, in a problem called *kinodynamic motion planning* (KMP). Despite its importance, KMP remains challenging due to the complexity of searching high-dimensional state and action spaces with non-linear dynamics. Echoing Sutton's "Bitter Lesson", formidable challenges in Computer Science are often solved by large-scale general-purpose methods rather than specialized heuristics, with search and learning emerging as two approaches capable of arbitrary scaling, rendering them essential in tackling KMP.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A cornerstone of search approaches for KMP are sampling-based planners (SBPs). By sampling random actions and simulating them through the dynamic model, SBPs grow a collision-free tree that spans the state space. SBPs are valued for their simplicity, versatility, and strong theoretical foundations. However, their exhaustive exploration can be inefficient in high-dimensional spaces, particularly in environments densely cluttered with obstacles or involving complex dynamics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning-based approaches have emerged as a promising alternative for improving motion planning efficiency. Prominent among them, diffusion planning casts planning as a form of probabilistic inference and samples from the multi-modal distribution of expert behaviors to synthesize diverse and high-quality trajectories. Unfortunately, such models struggle to generalize to unseen environments, and inherently lack guarantees such as collision avoidance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution. Motivated by breakthroughs combining learning and search, e.g., AlphaGo and LLM reasoning, we propose a learning-meets-search strategy for KMP. We introduce *Diffusion Tree (DiTree)*, a novel framework that combines diffusion models (DMs) with sampling-based tree search for efficient KMP. DiTree leverages DMs as powerful, environment-aware motion priors to guide exploration toward promising trajectories. By integrating these priors with SBPs, DiTree ensures collision avoidance and dynamic feasibility, while successfully navigating unseen environments. We demonstrate that DiTree achieves substantial efficiency improvements and outperforms state-of-the-art methods across diverse tasks and robotic platforms. We explore the set of unique challenges and trade-offs entailed with employing a DM for tree search in our ablation studies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Organization. We first survey related work, provide background on KMP, SBPs, and DMs, and then introduce our DiTree framework. We then present implementation details and practical considerations, followed by a comprehensive evaluation. Sec. concludes with a discussion and future work, followed by limitations in Sec..

<!-- chunk {"id": "body-0009", "role": "body", "section": "Diffusion Tree Algorithm", "weight": 1.0} -->

We present our DiTree approach for leveraging diffusion models (DMs) for efficient kinodynamic motion planning (KMP) and discuss its theoretical implications.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Action Sampling with Diffusion Policy", "weight": 1.0} -->

Our framework enhances methods compatible with Alg., by implementing its action selection procedure (Line 4) using a context-aware sampling procedure. Instead of sampling a single action from a uniform distribution, we sample a sequence of $N$ actions $u_{1:N}$, drawn from a distribution informed by the planning context. Inspired by recent advances in diffusion-based planning, we implement action sampling $u_{1:N} \sim {p\left( {u_{1:N} \mid {x_{\text{near}},x_{\text{target}},\mathcal{X}_{\text{obs}}^{\text{near}}}} \right)}$ as inference from a *conditional diffusion policy*.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Action Sampling with Diffusion Policy", "weight": 1.0} -->

The policy is trained on expert trajectories and conditioned on three key inputs: the current tree state $x_{\text{near}}$, a target state (which is either a goal or an exploration-guiding state) $x_{\text{target}}$, and local obstacle information $\mathcal{X}_{\text{obs}}^{\text{near}}$ with respect to $x_{\text{near}}$. During training, $x_{\text{target}}$ is set to the scenario's goal state, reinforcing goal-directed behavior. However, at test time, we introduce a *diffusion goal bias (DGB)* to promote exploration, replacing the goal state with a randomly sampled intermediate state $x_{\text{rand}}$. This encourages the policy to explore alternative regions of the space, generating more diverse actions and improving search coverage.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Action Sampling with Diffusion Policy", "weight": 1.0} -->

To foster generalization in our approach, we simplify the learning problem through two key strategies: As effective planning should be agnostic to arbitrary global coordinates, we represent $x_{\text{target}}$ relative to the chosen state $x_{\text{near}}$, introducing *translation and rotation invariance*. As training a sampler that effectively conditions on all obstacles in a scene across arbitrary scenarios requires a highly diverse and extensive dataset, we condition instead the DP on a *localized, state-dependent subset* of obstacles, denoted as $\mathcal{X}_{\text{obs}}^{\text{near}}$, extracted relative to the frame of $x_{\text{near}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Action Sampling with Diffusion Policy", "weight": 1.0} -->

After action sampling, a new edge for tree expansion is generated by executing the sequence $u_{1:N}$ via forward propagation, where each action $u_{i}$ is applied for some $dt$. The resulting trajectory segment is accepted only if it passes collision checking, otherwise it is discarded. To ensure full information utilization during edge generation---despite relying only on local observations---we employ DM as an MPC policy during forward propagation. I.e., the policy iteratively resamples actions based on the updated local observations, enabling a flexible generation of arbitrarily long edges by perpetual sampling and forward propagation even with a very local view. The process continues until a termination condition is met, such as reaching a predefined propagation duration.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Action Sampling with Diffusion Policy", "weight": 1.0} -->

Action sampling with diffusion models is substantially more time-consuming than other components of Alg., becoming the primary bottleneck in per-iteration runtime. This challenges their integration into sampling-based planners (SBPs), which require frequent sampling to drive exploration. Unlike standalone MPC-style diffusion policies, where the number of denoising steps is tuned to match a target control frequency, tree-based planners have no natural temporal anchor for setting the sampling schedule. Instead, the objective is to maximize planning success within a fixed time budget, requiring a careful balance between sampling speed and action quality. Fast sampling enables exploration of multiple branches, while not sacrificing the quality needed to capture the multimodal distribution of feasible edges. In Sec., we empirically investigate this trade-off and demonstrate that flow matching offers an effective balance between efficiency and performance. Consequently, hyperparameters such as the number of denoising steps must be reconsidered for the unique demands of tree-based search.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Theoretical Guarantees", "weight": 1.0} -->

Some SBPs have guarantees such as *probabilistic completeness* (PC) and *asymptotic optimality* (AO), which rely on the *full support* of uniform random action sampling. Although DiTree uses non-uniform diffusion-based samples from a learned distributions, we demonstrate that the favorable SBP properties can be transferred to our approach, based on our proof that diffusion models posses full support. We prove the following result for RRT-style node selection (line 3).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

To assess generalization and performance, we test DiTree against several baselines across 15 distinct scenarios on unseen maps, using two robot types. Each method is run for 20 trials per scenario with a 120-second time limit. Performance is measured by the success rate (i.e., the proportion of trials that result in a collision-free path) and the average planning time over successful trials.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments", "weight": 1.0} -->

We implement an instance of DiTree in Python. As an SBP backbone we build upon RRT due to its simplicity and popularity. For the diffusion policy we adopt single-step flow matching (FM), due to a favorable trade-off between speed and quality compared to diffusion models. As a single planning query could require running inference hundreds of times, we prioritize inference speed over absolute quality, but explore this trade-off in our ablation study. While more elaborate methods for single-step inference exist, they introduce a more complex training pipeline. For our local observations we use an occupancy grid. Transformers are widely used and generally yield superior results, yet they are also highly sensitive to hyperparameters. We leave their integration for future work and instead use UNet.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

Robots. We evaluate our method on two robotic domains: our custom CarMaze (implemented using the CasADi framework ) and D4RL's AntMaze (part of the D4RL benchmark; based on the MuJoCo physics engine ), both operating within 2D maze layouts. CarMaze relies on a 6D non-holonomic ground vehicle modeled using a single-track dynamic system, controlled via the throttle rate and steering rate. AntMaze consists of a 29D quadruped robot with a 8D action space specifying joint torques. See App. Appendix B: Robot Dynamics for more details. For each robot type, an FM policy is trained on an offline dataset collected from a *single* environment, D4RL's Large maze. To encourage relevant planning behaviors, we filter out states in close proximity to obstacles. Training and testing were conducted on an RTX 3090 GPU. Training lasts 2 hours.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baselines. We compare DiTree against the two classical SBPs RRT and SST, which are implemented in OMPL ---a leading C++ implementation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

For a learning-based baseline, as far as we know there are currently no available implementations of kinodynamic methods that could be trained on a single environment and generalize to others. Therefore, we compare against a standalone DP, using the same model checkpoint as DiTree. This baseline highlights the difference between direct trajectory generation and action sampling in an SBP. For the DP setup, the policy employs the dynamic model for forward propagation of sampled action sequences, but implements search by repeatedly generating rollouts until either the goal is reached without collision or timing out.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Results", "weight": 1.0} -->

Our results, show that DiTree achieves a strong performance across a range of out-of-distribution (OOD) scenarios, combining the speed of learned policies with the reliability of structured search. DiTree matches the runtime of DP--4× faster than classical SBPs---while outperforming both in terms of success rate (on average). On CarMaze, DiTree achieves a 26% higher success rate compared to all other methods, while in the AntMaze domain---where classical SBPs fail to produce any valid trajectories---it outperforms DP by a margin of 28%. While this work does not tackle optimal planning, a comparison of relative trajectory lengths shows DiTree discovers 25-50% shorter trajectories compared to RRT, underscoring its strength in producing efficient solutions and showing promising potential for integration of asymptotically-optimal SBPs as the planning backbone. These results demonstrate the advantage of integrating learned priors with guided exploration, particularly in environments characterized by complex dynamics and constrained, narrow passages.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results", "weight": 1.0} -->

There are a few CarMaze scenarios where DiTree underperforms. In the Corridor scenario, for example, DiTree achieves only a 10% success rate compared to 100% for all other methods. Examining the search tree reveals that most of the tree nodes have reached configurations from which the car cannot possibly navigate towards the goal without collision. Upon sampling of such nodes, precious iterations are wasted in such local traps. This inefficiency could potentially be mitigated by incorporating pruning and advanced node selection strategies.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

We conduct an ablation study using our validation scenarios to assess the impact of key design choices specific to our framework. Results are presented in Fig. First, we vary the number of *denoising iterations* used to generate a sample with FM model, exploring the trade-off between sampling speed and action quality. Surprisingly, we find a *single diffusion iteration* yields the best overall performance, which we subsequently chose for our main experiments. This stands in contrast to traditional diffusion-based planners, where even SOTA FM policies require several iterations to produce high-quality actions necessary for successful rollouts. In DiTree, however, faster, coarser samples are preferable, as they provide timely guidance for tree expansion without incurring the computational cost of multiple denoising steps. These results highlight a key distinction in how generative models are used within our framework: not to execute entire trajectories, but to prioritize promising search directions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Next, we ablate the effect of a key hyperparameter of DiTree, *propagation duration* ($N$). The propagation duration is defined as the length of the action sequence forming a tree edge. A shorter duration limits per-edge advancement---quickly shifting focus between nodes to broaden overall exploration---whereas a longer duration can cover more ground but risk inefficiency if a collision occurs. We compare several strategies for setting $N$: (i) a random selection between 32--128 steps per iteration, (ii) fixed values of 32, 64, or 128 steps, and (iii) a scheduled approach that gradually shortens edge length $({128\rightarrow 96\rightarrow 64})$ upon repeated node visits. Our experiments show a fixed value of 64 gave the best average results across our scenarios by a slight margin.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Finally, we examine the role of *diffusion goal bias* (DGB)^11^1Not to be confused with RRT's node selection goal bias.---a hyperparameter controlling the ratio of conditioning the FM on $x_{\text{rand}}$ versus the final goal $x_{\text{goal}}$. We find that setting DGB to either 0% or 85% yields the highest overall success rates. We observe complex scenarios benefit from a DGB of 0% due to the extensive exploration, however, simpler scenarios fall short as excessive random exploration leads to markedly longer and less efficient trajectories. Thus, in our experiments we opt for 85% promoting rapid expansion toward the goal while maintaining sufficient exploration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Real-World Applicability", "weight": 1.0} -->

We demonstrate integration with a physical robot by comparing DiTree to RRT in a sharp-corner turning car scenario. For deployment, output trajectories are smoothed and tracked using a pure-pursuit controller, without further optimization. Each planner is tested over ten runs (Appendix Appendix D: Full Experimental Results). During execution, RRT encounters eight collisions, while DiTree consistently steers clear of obstacles. As the underlying algorithm is identical for both methods, this highlights the robustness and quality of sampling learned from the expert dataset, whose trajectories inherently maintain a safety margin---mirroring the strong performance of diffusion-based approaches in driving tasks demonstrated by prior work.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced DiTree---a novel framework that integrates diffusion models with sampling-based tree search to address the challenges of KMP. By leveraging learned, environment-aware priors for action sampling, DiTree balances the strengths of generative models and classical planners---achieving fast, generalizable, and collision-free planning, while preserving guarantees of the underlying planner.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We aim for this work to lay the groundwork for safer, more general, data-driven motion planners in robotics. Future work includes inference optimization using distillation and quantization. Other potential improvements involve learning other SBP components like node selection, as well as better leveraging GPU parallelization during search. As our work diverts the computational bottleneck of SBPs from collision detection to action sampling via DM (Appendix D.1.2), it motivates the development of new tailored models that exploit the problem structure to facilitate faster solutions of multiple queries.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Limitations", "weight": 1.5} -->

Although DiTree demonstrates strong performance, several assumptions limit its ability to reach its full potential in more complex settings.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Limitations", "weight": 1.5} -->

First, we assume full knowledge of all obstacles at planning time, including their geometry. This restricts applicability in dynamic or partially observed settings. One remedy is to extend Alg. to support partial knowledge of the environment and replan over short horizons using updated observations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Limitations", "weight": 1.5} -->

Second, in our implementation, we rely on an approximation of the dynamic model, which could lead to reduced performance in practice, especially for complex real-world systems with chaotic dynamics or modeling uncertainty. Those issues could mitigated by learning a more accurate representation of the model, or designing a learned controller explicitly reasoning about dynamic residual between the simulation and the real world.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Limitations", "weight": 1.5} -->

Third, our workspace is strictly two-dimensional, as is represented via occupancy grids. While sufficient for planar navigation tasks, it does not capture the full geometry of 3D environments; incorporating richer modalities such as depth images or point clouds could address this limitation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Limitations", "weight": 1.5} -->

Fourth, our diffusion model is trained on pre-collected expert demonstrations. This enables straightforward training but limits applicability in environments lacking demonstration data. Extending our approach to learn behaviors from scratch using reinforcement learning is a promising direction.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Limitations", "weight": 1.5} -->

Lastly, we employ a bare-bone implementation of sampling-based planners that lack optimization and fine-grained parallelism, limiting our ability to fully exploit batch inference in diffusion models. Incorporating recent parallelized frameworks such as could significantly improve runtime efficiency.
