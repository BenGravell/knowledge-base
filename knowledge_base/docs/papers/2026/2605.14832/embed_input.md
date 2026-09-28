<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Direct Control Policies with Flow Matching for Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a flow-matching planner for autonomous driving that directly outputs actionable control trajectories defined by acceleration and curvature profiles. The model is conditioned on a bird's-eye-view (BEV) raster of the surrounding scene and generates control sequences in a small number of Ordinary Differential Equations (ODE) integration steps, enabling low-latency inference suitable for real-time closed-loop re-planning. We train exclusively on urban scenarios (real urban city streets, intersections and roundabouts of the city of Parma, Italy) collected from a 2D traffic simulator with reactive agents, and evaluate in closed-loop on both in-distribution and markedly out-of-distribution environments, including multi-lane highways and unseen urban scenarios. Our results show that the model generalizes reliably to these unseen conditions, maintaining stable closed-loop control and successfully completing scenarios that differ substantially from the training distribution. We attribute this to the BEV representation, which provides a geometry-centric view of the scene that is inherently less sensitive to distributional shifts, and to the flow-matching formulation, which learns a smooth vector field that degrades gracefully under distribution shift. We provide video demonstrations of closed-loop behavior at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Real-time trajectory generation under multi-modal uncertainty remains a central challenge in autonomous driving. Classical approaches decompose the problem into perception, prediction, and planning modules. While effective in structured settings, these pipelines often struggle to generalize to complex, interactive scenarios and require substantial engineering effort to handle conditions not seen during development.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep learning methods have gained significant traction, with generative models emerging as particularly expressive tools for capturing multi-modal future behaviors. Diffusion-based planners can produce diverse, realistic trajectories but their iterative denoising incurs considerable computational cost, limiting real-time applicability. Flow matching offers an attractive alternative: by directly parameterizing an ODE vector field that transports a simple initial distribution to the data distribution, it achieves comparable generative quality with substantially fewer integration steps and simpler training dynamics. These properties make flow matching well suited for autonomous driving, where low-latency re-planning is tightly coupled with safety.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common limitation of data-driven planners is the difficulty of evaluating them under realistic conditions. Open-loop metrics on held-out data do not capture compounding errors, while closed-loop evaluation in simulation with reactive agents provides a more faithful picture of real deployment. Furthermore, most prior work evaluates on the same scenario distribution used for training, leaving open the question of whether learned planners can handle situations outside their training distribution---a critical requirement for real-world driving, where the variety of road geometries, traffic patterns, and agent behaviors is effectively unbounded.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we adopt a conditional flow-matching formulation to generate short-horizon control trajectories conditioned on a BEV scene raster, and investigate the generalization capabilities of this approach through extensive closed-loop evaluation. Our contributions are: A BEV-conditioned flow-matching architecture that directly outputs actionable controls (acceleration and curvature), designed for real-time closed-loop re-planning with a lightweight iterative vector-field predictor.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A systematic study of out-of-distribution generalization: the model is trained exclusively on urban scenarios and roundabouts, and evaluated in closed-loop on new unseen urban scenarios and multi-lane highways. We show that the learned planner generalizes reliably to these conditions without any fine-tuning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extensive closed-loop evaluation in a simulated environment with reactive agents, using safety, progress, and comfort metrics aligned with standard planning benchmarks, accompanied by qualitative trajectory analysis and video demonstrations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our architecture is designed around a practical compute--latency trade-off: a BEV-based CNN performs a computationally intensive but one-time encoding of the environment, followed by a lightweight U-Net that is invoked multiple times during ODE integration to produce the final control sequence. This separation enables efficient real-time inference.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Planning in Autonomous Driving", "weight": 1.0} -->

Classical autonomous driving systems rely on modular pipelines comprising perception, prediction, and planning components, often using optimization-based planners with hand-crafted cost functions. While effective in many driving scenarios, these approaches require substantial engineering effort and lack generalization to novel situations. As the field matured, large-scale benchmarks enabled data-driven and hybrid methods to emerge, demonstrating the potential of learning-based planners to benefit from data volume and model capacity.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Flow Matching for Planning", "weight": 1.0} -->

Flow matching has recently emerged as a compelling alternative to diffusion models for trajectory generation, offering comparable or superior sample quality with fundamentally faster inference. Where diffusion-based planners require many denoising steps or truncation strategies to achieve real-time operation, flow matching parameterizes a continuous-time ODE vector field that can be integrated in a small number of steps.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Flow Matching for Planning", "weight": 1.0} -->

Recent work has demonstrated the effectiveness of flow matching for driving. GoalFlow showed that high-quality planning can be achieved in a single forward pass via goal-conditioned flow. FlowDrive showed that careful data balancing combined with lightweight multi-step integration enables flow-based planners to match or exceed state-of-the-art diffusion systems. These results establish flow matching as a promising framework for real-time, safety-critical autonomous planning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Generalization in Learned Planners", "weight": 1.0} -->

A key challenge for data-driven planners is generalization beyond the training distribution. Models evaluated exclusively on in-distribution data may exhibit brittle behavior when encountering novel road geometries, unseen traffic patterns, or unfamiliar agent behaviors. While several works have studied distributional robustness in prediction and perception, the question of whether generative planners---and flow-matching planners in particular---can generalize across substantially different scenario types in closed-loop remains relatively underexplored. This work directly addresses this gap by training on a restricted urban distribution and systematically evaluating on held-out scenario categories.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Simulation Environment", "weight": 1.0} -->

All training and evaluation are conducted in an internally developed 2D traffic simulator that operates at object level on a high-definition (HD) map of the city of Parma, Italy (Figure 1). The HD map is derived from OpenStreetMap with manual refinements and encodes lane geometry, lane connectivity, speed limits, drivable area boundaries, stop lines, yield lines, and traffic light positions. All training data, evaluation scenarios, and the HD map will be made publicly available upon publication to enable reproducibility and comparison. Individual scenarios are created by cropping rectangular regions, each capturing a distinct road configuration. In total, we define $50$ real scenarios from the city of Parma spanning a variety of layouts: single- and dual-lane streets, T-intersections, four-way intersections with and without traffic lights, roundabouts of varying sizes, and highway segments with on- and off-ramps.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Simulation Environment", "weight": 1.0} -->

Of the $50$ scenarios, $40$ are in-distribution urban configurations (single-lane streets, roundabouts, intersections) used for both training data collection and in-distribution evaluation (red regions in Figure 1). The remaining $10$ scenarios---highway segments and held-out urban configurations from geographically disjoint map regions---are reserved exclusively for out-of-distribution evaluation (blue regions in Figure 1). For closed-loop testing, we define $10$ fixed initial conditions per scenario, yielding $400$ in-distribution and $100$ out-of-distribution evaluation episodes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Simulator Overview", "weight": 1.0} -->

The simulator supports multi-agent scenarios with heterogeneous traffic participants. At the start of each simulation, all feasible routes between scenario entry and exit points are precomputed, either based on scenario boundaries or defined manually for specific cases. Throughout the simulation, agents are continuously spawned and removed: each agent appears at a designated entry point, follows a route sampled uniformly from the precomputed set, and is removed upon completion. We refer to the agents whose data is recorded for training as *ego agents*, and to all other traffic participants as *non-ego agents*. Multiple ego agents can run in parallel within a single scenario, and multiple scenarios can run simultaneously to speed up data collection. In the closed-loop evaluation setting, a single ego agent is controlled by the learned model while all non-ego agents follow their rule-based policies (Section 3.2).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Simulator Overview", "weight": 1.0} -->

We define an *episode* as the interval between an agent's spawn and one of four terminal outcomes: *success* (the agent reaches its assigned destination), *out-of-route* (the agent deviates from its route), *timeout* (the episode exceeds a maximum duration), or *collision*. At each timestep, the ego agent records the poses, speeds, headings, and bounding-box dimensions of all agents in the scene, together with the positions and states of traffic regulations (stop lines, traffic lights). The ego agent also records the route assigned to it at the start of its episode. To ensure traffic diversity, agent-level parameters---initial speed, desired cruising speed, aggressiveness, merging assertiveness, and acceleration limits---are sampled independently for each agent. Traffic density is set per scenario and can vary over the course of a simulation to model different congestion levels. The resulting episodes cover a wide range of driving situations: lane following and adaptive cruise control, roundabout entry and navigation, highway merging and lane changes, intersection handling (with and without traffic lights), and avoidance of static or dynamic obstacles on the road.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Simulator Overview", "weight": 1.0} -->

For training data, we retain only successful ego-agent episodes, ensuring that the model is trained exclusively on correct demonstrations of driving behavior. The resulting training set consists of ${\sim}19\text{K}$ successful episodes, corresponding to approximately $35$ hours of simulated driving. Although this may appear modest compared to large-scale driving datasets, our data is collected at $20\,\mathrm{Hz}$ re-planning frequency---substantially higher than typical benchmarks---and is actively curated for diversity: we discretize the state space of vehicle acceleration and curvature into bins and selectively store episodes that populate underrepresented regions, continuously monitoring the distribution during data collection. This ensures that the dataset is dense in informative driving situations rather than dominated by trivial straight-line driving.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Simulator Overview", "weight": 1.0} -->

As a 2D object-level simulator, the environment does not model sensor noise, occlusions, or localization errors. These simplifications are partially mitigated by the data augmentation applied dynamically over the raw data during training (Section 4), and we discuss remaining limitations in Section 8.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Agent Behavior Models", "weight": 1.0} -->

The simulator supports several categories of traffic participants: Vehicles (cars, trucks, buses, motorcycles): all vehicle agents share the same planning architecture, consisting of an Intelligent Driver Model (IDM) for longitudinal control and a Pure Pursuit controller for lateral path tracking. Each agent is parameterized with a configurable aggressiveness profile that modulates desired speed, following distance, merging assertiveness, and acceleration limits. Vehicle dynamics are governed by a kinematic bicycle model.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Agent Behavior Models", "weight": 1.0} -->

Pedestrians and cyclists: these agents follow a predefined route along the road boundary and may cross the road at crosswalks or random locations, traveling in the same or opposite direction as traffic.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Agent Behavior Models", "weight": 1.0} -->

Vehicle queues: sequences of stationary or slow-moving vehicles that model congestion at intersections or traffic lights.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Agent Behavior Models", "weight": 1.0} -->

Static obstacles: generic objects placed at the roadside or within the driving lane to simulate parked vehicles or unexpected/undefined obstructions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Data collection", "weight": 1.0} -->

During data collection, all agents---including the ego---have access to the full state of the environment as well as the future trajectories of other actors. This privileged information enables near-optimal behaviors, particularly in scenarios that require negotiation among agents (e.g., merging, intersection handling). Consequently, we can generate clean and consistent driving data from the ego agents, which are later used to train the planning model. To produce training data that is representative of real vehicle behavior, the ego agent's dynamics are simulated using a learned deep dynamic model as implemented in that approximates the response of our real testing car (Lexus RX 350h, Fig. 2), facilitating subsequent deployment on hardware.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Closed-loop evaluation", "weight": 1.0} -->

In the closed-loop setting, the ego agent no longer has access to the future routes of surrounding actors. Instead, it must implicitly infer their behavior from its observation of the environment (see Section 4) and predict the control action that best satisfies the driving objective, closely reflecting the conditions encountered during real-world deployment. All non-ego agents always remain *reactive*: their actions are recomputed at every timestep in response to the ego's actual driven trajectory (and the other agents in the scene), rather than replayed from pre-recorded data.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data Collection", "weight": 1.0} -->

Training data is collected by rolling out the rule-based agent policies described in Section 3 within the simulator. During the simulation, the ego-agent (running at 20Hz) records at each timestep the following information: The ego-agent target action $(a,\kappa)$, i.e. the acceleration and curvature command that is passed through the dynamic model to update the ego pose. This serves as the ground-truth supervision signal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data Collection", "weight": 1.0} -->

The poses and speeds of all agents in the scene (ego and non-ego), together with their object class (car, bus, bicycle, pedestrian, etc.), bounding-box dimensions (width, length), and heading.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Data Collection", "weight": 1.0} -->

Additionally, we record the route assigned to the ego agent at the start of each episode. The training set comprises $2{,}524{,}298$ frames collected exclusively from urban and roundabout scenarios. No separate held-out test set is used: all evaluation is performed in closed-loop (Section 6), where the model drives the ego vehicle in real time within the simulator. Table 1 summarizes the training data composition.

<!-- chunk {"id": "body-0029", "role": "body", "section": "BEV Representation", "weight": 1.0} -->

The vectorized scene information recorded during data collection---agent poses, speeds, bounding-box dimensions, object classes, ego-agent route and HD map geometry---is rasterized into a bird's-eye-view (BEV) tensor at training time. Each training sample is therefore a tuple $(\mathbf{B},z)$ where $\mathbf{B}\in\mathbb{R}^{4\times h\times w}$ is the BEV raster and $z\in\mathbb{R}^{n\times 2}$ is the ground-truth control sequence. The BEV raster has spatial resolution $h=w=768$ at $0.25\,\mathrm{m}$ per pixel, covering a $192\,\mathrm{m}\times 192\,\mathrm{m}$ area centered on the ego agent ($96\,\mathrm{m}$ in each direction).

<!-- chunk {"id": "body-0030", "role": "body", "section": "BEV Representation", "weight": 1.0} -->

The four channels (Figure 3) encode: Obstacles: The ego-agent's bounding box is rendered with a constant value; other agents are rasterized with pixel values proportional to their speed.

<!-- chunk {"id": "body-0031", "role": "body", "section": "BEV Representation", "weight": 1.0} -->

Drivable area: Drivable road surface with pixel values encoding the speed limit.

<!-- chunk {"id": "body-0032", "role": "body", "section": "BEV Representation", "weight": 1.0} -->

Ego route: The planned route rendered as the union of drivable lanes that compose the ego-agent's route, with pixel values encoding the ego's current speed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "BEV Representation", "weight": 1.0} -->

Regulations: A single channel indicating stop locations (yield lines, stop signs, traffic lights) with different pixel values for different types of regulations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "BEV Representation", "weight": 1.0} -->

To improve robustness to the imperfect perception that would be encountered in a real-world system, we apply data augmentation during training by randomly perturbing the poses and speeds of non-ego agents in the BEV raster. This injects noise that approximates real-world perception errors and encourages the model to learn policies that are less sensitive to small inaccuracies in the observed scene. On our autonomous vehicle the BEV representation is based on data retrieved from perception and localization modules. Future work will aim at fusing these modules for real-world evaluation of the model.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Control Representation", "weight": 1.0} -->

The ground-truth control sequence $z\in\mathbb{R}^{n\times 2}$ consists of $n=64$ future timesteps at $20\,\mathrm{Hz}$ (a horizon of $3.2\,\mathrm{s}$). The two control dimensions are acceleration $a\in\,\mathrm{m/s^{2}}$ and curvature $\kappa=1/r\in[-0.2,0.2]\,\mathrm{m^{-1}}$, where $r$ is the turning radius. Both are normalized before being fed to the model.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Dataset Statistics and Distribution", "weight": 1.0} -->

Understanding the composition of the training data is important for interpreting the generalization results. Table 1 summarizes the key statistics and Figure 4 shows control and speed distributions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Dataset Statistics and Distribution", "weight": 1.0} -->

Total training frames Table 1: Training dataset statistics.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dataset Statistics and Distribution", "weight": 1.0} -->

The training distribution is dominated by straight driving and gentle acceleration, with sharp steering and strong braking events being substantially rarer. This imbalance reflects realistic urban driving conditions, where the majority of time is spent in steady-state lane following, but can be easily rebalanced with a custom data sampler to enhance the importance of rarer control sequences. The curvature distribution is concentrated near zero, with a long tail corresponding to roundabout and turn maneuvers.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conditional Flow Matching", "weight": 1.0} -->

Flow matching provides a framework for transforming a simple initial distribution $p_{\text{init}}$ into a data distribution $p_{\text{data}}$ via an ODE. A trajectory $X:\to\mathbb{R}^{d}$ is defined as the solution of where $u_{t}^{\theta}$ is a learned vector field. Sampling reduces to drawing $X_{0}\sim p_{\text{init}}$ and integrating numerically (e.g. Euler: $X_{t+h}=X_{t}+h\,u_{t}^{\theta}(X_{t})$).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conditional Flow Matching", "weight": 1.0} -->

Following, we choose a linear interpolation schedule $\alpha_{t}=t$, $\beta_{t}=1-t$, yielding the interpolated state $x_{t}=tz+(1-t)\epsilon$ with $z\sim p_{\text{data}}$ and $\epsilon\sim\mathcal{N}(0,I)$. The conditional flow matching objective simplifies to: where $t\sim\mathcal{U}$. The training target $z-\epsilon$ is independent of $t$, producing straight-line trajectories between noise and data, which reduces the number of integration steps needed for accurate sampling.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conditional Flow Matching", "weight": 1.0} -->

In our setting, the data distribution corresponds to ground-truth control sequences $z\in\mathbb{R}^{n\times 2}$ (acceleration and curvature), and the model generates control sequences by integrating Eq. from an initial state $X_{0}$. For reproducibility, we initialize all inference from the mean of the Gaussian prior, i.e. $X_{0}=\mathbf{0}$, rather than sampling stochastically. This yields deterministic outputs for a given BEV input.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Architecture", "weight": 1.0} -->

Since our goal is real-time closed-loop deployment, we design the architecture around a separation of concerns: a heavy one-time encoding of the scene, followed by a lightweight iterative generator (Figure 5).

<!-- chunk {"id": "body-0043", "role": "body", "section": "BEV encoder", "weight": 1.0} -->

The BEV raster $\mathbf{B}\in\mathbb{R}^{4\times h\times w}$ is processed by a CNN to produce a compact spatial embedding $c=\text{CNN}_{\text{BEV}}(\mathbf{B})\in\mathbb{R}^{m}$. This encoding is computed once per planning cycle and reused across all ODE integration steps.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Vector-field U-Net", "weight": 1.0} -->

The vector field $u_{t}^{\theta}(\cdot\mid c)$ is parameterized by a U-Net that takes the noisy control sequence $x_{t}$ and the interpolation time $t$ as input, and is conditioned on the BEV embedding $c$ via cross-attention, following the conditioning paradigm of. The U-Net consists of two down-blocks, a middle block, and two up-blocks, with cross-attention layers placed at the skip connections and in the mid-block for effective multi-scale fusion. The full model contains approximately $15$M parameters, of which roughly $85\%$ reside in the BEV CNN. The U-Net is deliberately kept lightweight because it is executed at every ODE integration step during inference.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Training", "weight": 1.0} -->

The BEV encoder and the vector-field U-Net are trained jointly end-to-end from scratch with the CFM objective (Eq. ). We use AdamW ($\beta_{1}=0.9$, $\beta_{2}=0.999$, weight decay $0.1$) at a peak learning rate of $5\times 10^{-4}$. Training runs for $300$k steps with a batch size of $32$, using a linear warmup over the first $5\%$ of steps followed by cosine annealing. On a single NVIDIA RTX A6000, training completes in approximately three days.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Closed-Loop Protocol", "weight": 1.0} -->

At each ego-agent timestep ($20\,\mathrm{Hz}$), the evaluation loop proceeds as follows: (i) a BEV raster is rendered from the current ego state, all other agent states, the local HD map geometry and the ego-agent route; (ii) the flow-matching model generates a control sequence by integrating the learned ODE from the zero initial state; (iii) only the first predicted control $(a_{1},\kappa_{1})$ is applied to update the ego vehicle's state via the deep dynamic model; (iv) all non-ego agents update their states according to their reactive rule-based policies (Section 3); (v) the process repeats from (i).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Closed-Loop Protocol", "weight": 1.0} -->

Unlike replay-based evaluation, where non-ego agents follow pre-recorded trajectories regardless of the ego's behavior, non-ego agents re-plan at every timestep in response to the ego's actual driven trajectory, as explained in Section 3. This makes the evaluation substantially more challenging and realistic, as the ego must handle situations that emerge from the interaction between its own actions and the adaptive responses of other traffic participants.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Closed-Loop Protocol", "weight": 1.0} -->

In contrast to the data-collection phase, where scenario parameters (starting positions, speeds, aggressiveness profiles) are sampled randomly, evaluation episodes use fixed initial conditions. This ensures that each scenario is fully reproducible in every evaluation run.

<!-- chunk {"id": "body-0049", "role": "body", "section": "In-Distribution vs. Out-of-Distribution Scenarios", "weight": 1.0} -->

We evaluate the model in two regimes. *In-distribution* episodes use scenario types present in the training data---urban streets, intersections, and roundabouts---but with fixed initial conditions. *Out-of-distribution* (OOD) episodes use scenario types never seen during training, drawn from geographically disjoint map regions (see Figure 1) to eliminate any risk of train--test leakage.

<!-- chunk {"id": "body-0050", "role": "body", "section": "In-Distribution vs. Out-of-Distribution Scenarios", "weight": 1.0} -->

The primary source of distribution shift in the OOD set is the inclusion of highway scenarios. These differ from the training distribution in several important ways: (i) target speeds for both ego and non-ego agents are substantially higher (up to $90\,\mathrm{km/h}$ vs. the urban speeds seen during training), so that speed-encoded pixel values in the BEV raster occupy a region never encountered during training; (ii) the vehicle dynamics at highway speeds---longer braking distances, different steering sensitivity---have never been experienced by the model; and (iii) the combination of high speeds and a forward field of view limited to $96\,\mathrm{m}$ (half the $192\,\mathrm{m}$ BEV extent) means that oncoming agents appear and close in much more quickly, possibly requiring faster reactions with less planning horizon.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Metrics", "weight": 1.0} -->

We adopt metrics aligned with established closed-loop planning benchmarks such as nuPlan and NAVSIM, adapted to our simulation setup. All metrics are computed on driven trajectories produced by the model in closed-loop and reported in Table 2.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Metrics", "weight": 1.0} -->

Collision rate (CR): fraction of episodes in which the ego vehicle collides with any other agent or static obstacle.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Metrics", "weight": 1.0} -->

Drivable area compliance (DAC): fraction of episodes in which the ego vehicle remains within the drivable road surface at all times. An episode is marked as non-compliant if any corner of the ego bounding box exits the drivable area.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Metrics", "weight": 1.0} -->

Route progress (RP): fraction of the planned route completed by the ego vehicle, averaged across episodes. This captures partial success even when the ego does not reach the final goal.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Metrics", "weight": 1.0} -->

To evaluate ride quality, we define two complementary jerk-based metrics computed directly from the predicted controls. Let $f=20\,\mathrm{Hz}$ denote the simulation and re-planning framerate.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Metrics", "weight": 1.0} -->

Predicted-sequence jerk ($J_{\text{seq}}$): at each re-planning step, the model outputs a sequence of $n$ future controls. We compute the longitudinal jerk as the finite difference of successive accelerations, $j_{i}=(a_{i+1}-a_{i})\cdot f$, and report the mean absolute jerk across all timesteps and episodes. This measures the smoothness of the *planned* control profile.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Metrics", "weight": 1.0} -->

Executed jerk ($J_{\text{exec}}$): across successive re-planning steps, only the first control $(a_{1}^{(t)},\kappa_{1}^{(t)})$ is actually applied. We compute the longitudinal jerk of the *executed* trajectory as $j^{(t)}=(a_{1}^{(t+1)}-a_{1}^{(t)})\cdot f$ and report the mean absolute value. This captures the smoothness of the actual driving behavior as experienced by passengers, including inconsistencies between successive re-planning outputs.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Metrics", "weight": 1.0} -->

Only for qualitative evaluation, we apply a bicycle model to convert the predicted controls into vehicle poses, which are used to visualize predicted future trajectories in the supplementary videos.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Integration Steps and Solver Selection", "weight": 1.0} -->

A key practical consideration for flow-matching planners is the number of function evaluations (NFE) used during ODE integration at inference time. Each NFE requires one forward pass through the vector-field U-Net, so the NFE directly determines the latency of control generation. We compare several ODE solvers across different NFE values.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Integration Steps and Solver Selection", "weight": 1.0} -->

We observed no meaningful difference in closed-loop behavior between the Euler method and higher-order solvers (Heun, RK4), so we adopt Euler for its simplicity. At $\text{NFE}=10$ the total forward computation time is around $25\,\mathrm{ms}$ (Figure 6), which is well within the real-time latency budget that would be required for closed-loop re-planning on an NVIDIA RTX A6000 GPU.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Integration Steps and Solver Selection", "weight": 1.0} -->

Based on this analysis, we select the Euler solver with $\text{NFE}=10$ as our primary configuration for all closed-loop experiments. We additionally report results with $\text{NFE}=1$ (single-step generation) in Table 2 to quantify the impact of the number of integration steps on closed-loop performance.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Closed-Loop Performance", "weight": 1.0} -->

Table 2 reports closed-loop metrics for both NFE configurations across in-distribution and OOD episodes. With $\text{NFE}=10$, the model achieves low collision rates, high drivable area compliance, and near-complete route progress in both regimes. Increasing from $\text{NFE}=1$ to $\text{NFE}=10$ yields consistent improvements across all metrics, confirming that the performance increase of multi-step ODE integration translates to improved closed-loop control quality.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Closed-Loop Performance", "weight": 1.0} -->

A notable observation is that OOD performance is comparable to---and in some metrics slightly better than---in-distribution performance. This is because highway scenarios involve fewer complex decision points (merges, tight turns, intersection negotiations) that require precise control, and the lower density of close-range interactions reduces the probability of collisions caused by aggressive non-ego agents. However, as discussed below, this quantitative advantage masks qualitative differences in driving behavior at highway speeds.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Closed-Loop Performance", "weight": 1.0} -->

The comfort metrics reveal a striking gap between the predicted-sequence jerk $J_{\text{seq}}$ and the executed jerk $J_{\text{exec}}$: $J_{\text{seq}}$ is nearly two orders of magnitude lower. This indicates that the model produces smooth, internally consistent control sequences at each re-planning step, but exhibits higher sensitivity to frame-to-frame variations in the BEV input, leading to larger differences between successive first-step controls. Addressing this gap---for instance by conditioning on temporal sequences of BEV rasters rather than single frames---is an interesting direction for future work.

<!-- chunk {"id": "body-0065", "role": "body", "section": "In-distribution scenarios", "weight": 1.0} -->

The model reliably follows the assigned route across all in-distribution scenario types, including lane following, adaptive cruise control (following a lead vehicle), left and right turns, and roundabout entry and exit. In standard driving situations the behavior is smooth and closely resembles the expert demonstrations. The $J_{\text{exec}}$ metric is in all settings below $2.5$ m/s^3^, which is a good indication of smooth driving behavior and below commonly accepted thresholds for ride comfort.

<!-- chunk {"id": "body-0066", "role": "body", "section": "In-distribution scenarios", "weight": 1.0} -->

The main difficulty arises in tight maneuvers: on sharp turns, the model tends to cut the corner slightly and then overshoot, suggesting that it cannot reach the high curvature values needed for these situations. This is consistent with the training distribution, where high-curvature frames are slightly underrepresented (Section 4).

<!-- chunk {"id": "body-0067", "role": "body", "section": "In-distribution scenarios", "weight": 1.0} -->

The occasional drivable-area violations visible in the DAC metric can be attributed to the simulator's representation of road boundaries: there is no explicit distinction between lane markings and physical curbs, so boundaries are effectively "soft." The expert planner used for data collection treats them as such---occasionally cutting corners, particularly in tight turns---and the learned model reproduces this behavior. This is compounded by the well-known tendency of the Pure Pursuit controller (used in data collection) to cut trajectories on curved paths. In future work, we will investigate the impact of different data-collection deterministic controllers on the model's behavior.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Out-of-distribution scenarios", "weight": 1.0} -->

On highway scenarios, the model successfully maintains lane following and adapts its speed to surrounding traffic despite never having seen these speeds or road geometries during training. Quantitatively, OOD metrics are slightly better than in-distribution, mainly because highway driving involves fewer complex interactions and less exposure to aggressive non-ego behavior. Also the jerk metrics are slightly lower on OOD episodes, which can be attributed to the lower variation of road geometry (and in turn, BEV raster inputs) during the episode, with highways consisting of long straight lines or low and constant curvature long turns.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Out-of-distribution scenarios", "weight": 1.0} -->

However, the supplementary videos reveal qualitative differences: at highway speeds the ego vehicle struggles more to maintain precise lane centering, likely due to the unfamiliar vehicle dynamics at high speed and the higher sensitivity of lateral position to small curvature errors. On the other hand, the absence of sharp turns in highway scenarios means the model never drives out of the drivable area, explaining the higher DAC on OOD episodes.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Failure Analysis", "weight": 1.0} -->

The dominant failure mode across both in-distribution and OOD episodes is *aggressive non-ego behavior*. This manifests in two ways: non-ego agents spawned immediately behind the ego with a large speed differential whose aggressive driving policy does not brake strongly enough to avoid a rear-end collision, and non-ego agents that cut into the ego's lane during merging or turning maneuvers with an insufficient gap. In both cases, the collision is largely unavoidable regardless of the ego's actions. Because our planner is purely frame-based---it observes a single BEV snapshot with no temporal history---it cannot anticipate such maneuvers long before they materialize, at which point it is often too late to react. A planner with temporal context or explicit agent-intent modeling could mitigate some of these failures, but this falls outside the scope of the present work.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Generalization properties", "weight": 1.0} -->

Our results indicate that a flow-matching planner trained on a restricted urban distribution can generalize to substantially different driving conditions in closed-loop. We hypothesize that this arises from two factors. First, the BEV representation abstracts away scenario-specific visual details and presents the model with a structured, geometry-centric view of the scene, allowing it to learn spatial relationships (e.g., "slow down near obstacles," "follow the drivable area") that transfer across road types. Second, the flow-matching objective, by learning a smooth vector field over the space of control sequences, may produce robust representations that only slightly degrade when the input distribution shifts, rather than failing catastrophically. We note that all results are obtained in a 2D object-level simulator; validating the sim-to-real transfer of these findings remains an important direction for future work.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Near-misses", "weight": 1.0} -->

As discussed in Section 7.4, the main source of collisions is aggressive non-ego behavior that leaves the ego no feasible avoidance strategy. A promising direction to reduce this failure mode is to improve the deterministic planner used for data collection so that it explicitly handles near-miss situations---e.g., by braking defensively or yielding preemptively when an aggressive agent approaches. This would increase the proportion of successful episodes in the training data even under adversarial non-ego conditions, providing the learned model with demonstrations of robust defensive driving and likely improving its collision avoidance in closed-loop evaluation.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Interactive agents", "weight": 1.0} -->

The rule-based agents used in our simulator, while reactive, follow relatively simple policies. Real-world traffic involves more diverse and less predictable behaviors. It remains to be seen whether the generalization we observe extends to environments with more complex agent interactions, such as aggressive merging, jaywalking pedestrians, or adversarial behavior.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a conditional flow-matching planner that generates control trajectories for autonomous driving from BEV scene rasters. The model produces actionable acceleration and curvature sequences in real time via lightweight ODE integration, and is trained end-to-end with the standard flow-matching objective.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our central finding is that this approach generalizes beyond its training distribution: trained exclusively on urban scenarios and roundabouts, the model successfully navigates multi-lane highways and unseen urban scenarios in closed-loop simulation with reactive agents, while maintaining low predicted-sequence jerk that indicates smooth and comfortable planned control profiles.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We see several directions for future work. First, incorporating richer scene representations---such as temporal BEV sequences or vectorized map encodings---may further improve the model's ability to reason about dynamic interactions. Second, evaluating sim-to-real transfer, particularly the impact of noisy or imperfect BEV inputs, is essential for understanding real-world applicability. Finally, integrating the approach with established public benchmarks would enable direct comparison with existing planners and strengthen the empirical foundation of the generalization findings reported here.
