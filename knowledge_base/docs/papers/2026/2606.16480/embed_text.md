<!-- arxiv-full-text:v1 {"arxiv_id": "2606.16480", "source": "arxiv-html"} -->

## Introduction

Robots deployed in the wild must plan motions across a spectrum of scenarios (e.g., varying layouts, dynamics, and task objectives) without per-scenario retuning. This multi-scenario setting is particularly challenging because the distribution of states, constraints, and disturbances can shift dramatically across environments, while planners must still produce safe, real-time behavior.

Reinforcement learning (RL) is an appealing approach to acquire policies directly from data, sidestepping the need to hand-engineer heuristics for each scenario. In principle, training on diverse environments can yield policies that generalize to unseen ones. In practice, however, end-to-end RL policies often exhibit unstable performance across scenarios due to long-horizon credit assignment, reward misspecification, and sensitivity to distribution shift and stochastic dynamics. These issues are exacerbated when learning directly in low-level action spaces (e.g., torques or fine-grained velocity commands), where policy-gradient variance is high.

Model predictive path integral (MPPI) control, in contrast, is a sample-based optimizer for online policy refinement. MPPI handles nonlinear dynamics without requiring gradients and exploits parallel sampling to meet real-time constraints. Its effectiveness, however, depends critically on the sampling prior, i.e., the distribution from which candidate control sequences are drawn. A well-shaped prior can dramatically improve sample efficiency and robustness, while a poor one wastes computation and degrades performance. Designing such priors by hand (e.g., scenario-specific trajectory libraries) does not scale to multi-scenario deployment.

This paper advocates a complementary decomposition: let learning supply scenario-robust, data-driven priors, and let online stochastic optimal control supply precise, constraint-aware refinement (see Figure 1). Moreover, we perform learning in a high-level action space that enables learning robust priors across multiple complex scenarios.. Offline, a high-level policy and a world model are trained on multi-scenario data. Online, the high-level policy and world model produce intention-level actions that are converted into a nominal low-level control sequence. MPPI samples around this prior, evaluates rollouts, and executes the first control of the optimized sequence.

Contributions. Our main contributions are as follows: We introduce HOLO-MPPI, a hierarchical, multi-scenario motion-planning framework that couples RL and MPPI through a learned sampling prior: the RL policy steers the search toward useful modes, while MPPI retains its exploration and constraint-aware refinement under the planner's full cost. This also decouples the RL reward from the MPC cost, letting each component use the objective it is best suited to optimize.

We learn the policy in an abstract action space designed to expose intent shared across scenarios, allowing a single planner to generalize across them without per-scenario retuning or handcrafted priors.

We instantiate HOLO-MPPI in a multi-scenario highway-driving benchmark, jointly training the high-level policy with a lightweight world model for online rollout. The high-level policy is more scenario-robust than direct low-level RL, and HOLO-MPPI further outperforms vanilla MPPI, end-to-end SAC, and the prior alone, with smoother control at real-time rates.

## Related Work

### II-A Sampling-based MPC and MPPI

Sampling-based MPC methods such as MPPI and the cross-entropy method (CEM) have proven to be effective for nonlinear control under uncertainty. MPPI updates a nominal control sequence using cost-weighted perturbations. Its practical performance depends heavily on the sampling distribution used to generate rollouts. Recent works improve MPPI via covariance shaping, adaptive control, and learned dynamics models. Despite these advances, many approaches still rely on heuristic or scenario-specific priors, which limit scalability to diverse multi-scenario settings.

### II-B Learning-based priors and initializations for MPC

A growing body of work integrates learning with MPC. Learning has been used to accelerate or initialize trajectory optimization by imitating MPC solutions, warm-starting MPC solvers, or learning high-level decision variables that parameterize MPC problems. Closer to our setting, recent work uses learned policies as MPPI sampling priors with learned value functions as terminal costs. differs in two key ways. First, it learns a high-level policy in an abstract action space designed to capture scenario-shared intent, enabling one planner to generalize across structurally distinct scenarios. Second, the learned policy is used only to shape the sampling distribution of MPPI, decoupling the RL reward from the MPC cost. Since RL typically needs reward shaping, an interpretable, constraint-aware MPC cost---often dictated by the problem---can be a poor RL reward; this decoupling lets each component use the objective it is best suited to optimize.

### II-C Combining RL and MPC at deployments

A separate line of work structurally combines RL and MPC at deployment. Some approaches place RL at the low level, training an RL policy to track or steer a model-based plan. Dual approaches place a learned high-level policy on top of a model-based low-level controller, or blend RL with MPC via a learned torque residual. Hierarchical decomposition has also been explored at the semantic level via vision-language models. most closely resembles the hierarchical pattern of high-level RL with low-level MPC, but differs in the high-level RL policy's role. Rather than producing a reference that the low-level controller deterministically tracks, the high-level policy parameterizes a sampling distribution over the low-level optimizer's solutions, allowing MPPI to explore around the prior under the planner's full cost.

## Preliminaries

### III-A Problem setup: multi-scenario motion planning

We consider a family of scenarios $\mathcal{S}$, where each scenario $s\in\mathcal{S}$ specifies the type of environment (e.g., merging or roundabout in autonomous driving). Our goal is to deploy a single planner that performs well across scenarios from $\mathcal{S}$.

At each initial state $x_{0}\in\mathcal{X}$ of the agent and the initial observation (or episode state) $o_{0}\in\mathcal{O}$, the planner solves a finite-horizon MPC problem for the control sequence $U:=u_{0:H-1}\!:=\!(u_{0},u_{1},\dots,u_{H-1})\in\mathcal{U}^{H}$ for planning horizon $H$: | | $\displaystyle\operatorname*{arg\,min}_{U\in\mathcal{U}^{H}}$ | $\displaystyle J_{s}(x_{0:H},o_{0:H},U)\!=\!\sum_{t=0}^{H-1}\!\ell_{s}(x_{t},o_{t},u_{t})+\Phi_{s}(x_{H},o_{H})$ | | \(1\) | | | | $\displaystyle o_{t+1}=F_{s}(x_{t},o_{t},u_{t}),\quad\quad t=0,\dots,H\!-\!1,$ | | | where $\ell_{s}$ is the stage cost, $\Phi_{s}$ is the terminal cost, $f$ is the dynamics of the agent, and $F_{s}$ is the (unknown) world dynamics for each scenario $s$. In a receding-horizon fashion, only the first action of the solution is executed before replanning at the next time step.

### III-B Model Predictive Path Integral

MPPI approximately solves the finite-horizon control problem in by evaluating control trajectories sampled around a nominal trajectory $\tilde{U}:=\tilde{u}_{0:H-1}\in\mathcal{U}^{H}$.

It considers an optimal stochastic policy (i.e., a distribution over $U$) for the following problem given covariance $\Sigma$: which yields the analytical solution: where $\eta_{1}$ is the normalization factor, and $q_{U,\Sigma}:=\mathcal{N}(\cdot|U,I_{H}\otimes\Sigma)$ denotes a multivariate Gaussian over the sequence of $H$ control inputs with mean $U$ and constant covariance $\Sigma$ at each timestep.

Since the optimal distribution $q^{*}_{\text{MPPI}}$ is not tractable, MPPI considers a controlled distribution $q_{U,\Sigma}$ and pushes it close to the optimal one by minimizing their distance: Then, it computes $U^{*}$ through importance sampling based on sampling distribution $q_{\tilde{U},\Sigma}$ around the nominal trajectory $\tilde{U}$: where $\eta_{2}$ is the normalization factor. In practice, MPPI approximates the expectation by drawing $K$ samples $\{U^{k}\}_{k=1}^{K}$ from the sampling distribution $q_{\tilde{U},\Sigma}$: In a receding-horizon fashion, MPPI executes the first action and uses the (zero-padded) remainder as the next prior $\tilde{U}$.

## Overview of HOLO-MPPI

, shown in Figure 1, is a hierarchical motion-planning framework for robots to operate across diverse scenarios without scenario-specific retuning. The central idea is to separate planning into two complementary layers: High-level offline policy learning: we learn a policy $\pi_{\theta}$ via reinforcement learning that produces an abstract, scenario-robust plan that captures task intent in a compact high-level action space $\mathcal{U}_{\text{high}}$.

Low-level online policy optimization: we refine the high-level plan online in the original low-level action space $\mathcal{U}$, enabling fast adaptation to local disturbances, model mismatch, and stochastic interactions.

This decomposition combines the strengths of learning and online optimization: RL provides a data-driven prior that generalizes across scenarios, while MPPI preserves the reactivity and constraint-awareness needed for real-time control.

The motivation for this design is that directly learning a policy that outputs low-level control actions is often difficult in multi-scenario settings. Low-level actions must account for fine-grained dynamics, long-horizon credit assignment, and highly variable local interactions, which can make training brittle and reduce transfer across environments. In contrast, a high-level action space can encode more stable and semantically meaningful decisions, such as subgoals, waypoints, motion primitives, mode switches, or other intention-level commands appropriate to the robotics domain. Learning in such an abstract space allows the policy to focus on decisions that are shared across scenarios, while deferring precise execution to the online optimizer.

Offline, HOLO-MPPI learns both the high-level policy $\pi_{\theta}:\mathcal{X}\times\mathcal{O}\rightarrow\mathcal{U}_{\text{high}}$ and the world model $F_{\phi}:\mathcal{X}\times\mathcal{O}\times\mathcal{U}\rightarrow\mathcal{O}$ from data collected across scenarios from simulation, logged experience, exploration, or demonstrations. The world model predicts observations needed to roll out the high-level policy during prior generation, while the high-level policy maximizes long-horizon return through reinforcement learning. Importantly, HOLO-MPPI does not require the high-level policy to be a perfect standalone controller. Its purpose is to generate a prior that places online optimization near useful solution modes across many scenarios.

At each planning step, given the initial state $x_{0}$ and observation $o_{0}$, we roll out the high-level actions from the learned policy $\pi_{\theta}$ and the learned model $F_{\phi}$. Then, we map the high-level actions into the original action space $\mathcal{U}$ through a known conversion function $g:\mathcal{X}\times\mathcal{O}\times\mathcal{U}_{\text{high}}\rightarrow\mathcal{U}$, which may correspond to a simple upsampling rule, a tracking controller for geometric references, or a structured controller that maps symbolic intent into dynamically feasible controls depending on the application.

Given the converted rollout $\tilde{U}\in\mathcal{U}^{H}$, MPPI performs real-time stochastic optimization in the low-level action space. Specifically, it samples candidate control sequences around the learned prior, $U^{k}\sim\mathcal{N}(\tilde{U},I_{H}\otimes\Sigma)$, evaluates the resulting rollouts under the task cost, and computes an importance-weighted update as . Crucially, the high-level policy steers MPPI toward promising regions of the control space, thereby improving sample efficiency and removing the need for handcrafted priors.

Input: Initial state x0; Initial observation o0 Output: Action sequence U = (u0, u1, ⋯, uH − 1).

1:Planning horizon H; Number of samples K; Sampling covariance matrix Σ; stage cost ℓ; terminal cost Φ; dynamics f; action-conversion model g; MPPI temperature scalar λ 2:Phase 0: High-level offline policy learning 3:Learn high-level policy πθ via reinforcement learning 4:Learn world model Fϕ 5:Phase 1: Low-level online policy optimization 6:(1.1) Roll out a nominal action prior using the high-level policy 11:(1.2) Sample and evaluate trajectories around the prior in parallel 13: Sample a control sequence Uk = u0: H − 1k ∼ 𝒩(Ũ, IH ⊗ Σ) 20:(1.3) Compute importance weights and update the action sequence 22:$\eta\leftarrow\Sigma_{k=1}^{K}\exp\left(-\frac{1}{\lambda}\left(J^{k}-\beta\right)\right)$ 24: $\omega^{k}\leftarrow\frac{1}{\eta}\exp\left(-\frac{1}{\lambda}\left(J^{k}-\beta\right)\right)$ 25:return $\sum_{k=1}^{K}\omega^{k}U^{k}$ Algorithm 1 summarizes the resulting procedure. At each control cycle, HOLO-MPPI first queries the high-level policy using the current observation and goal, then converts the predicted abstract plan into a nominal low-level action sequence $\tilde{U}$, and finally runs MPPI around this learned prior to produce the control that is executed on the robot. is a general framework: the same architecture admits different modeling choices depending on the robotic platform and available prior knowledge. In particular, it is compatible with both on-policy RL in simulation and off-policy RL from logged data. For rollout-based evaluation, it can incorporate analytic models, learned models, or hybrid combinations of the two. When accurate dynamics are available, the ego system can use the known model with analytic or learned predictions for the surroundings.

In the next section, we describe HOLO-MPPI in more detail, focusing on the prominent application of autonomous driving. We instantiate its task-dependent ingredients, such as the MPC formulation , the design of the high-level action model with its corresponding action conversion mechanism, and the training process of the high-level policy and the world model.

## HOLO-MPPI in Autonomous Driving

Figure 2: Four highway driving scenarios:. The initial position of the ego vehicle and the goal position are randomly generated in the marked area. We randomize lane numbers, spawn/goal locations, and traffic behaviors.

We instantiate HOLO-MPPI in a multi-scenario highway-driving benchmark that we built on the Highway-Env simulator. Each episode samples one scenario from Straight, Merge, Roundabout, and Intersection (see Figure 2), which exposes a common observation interface to both the learned policy and the online planner. In addition to vehicle states, BEV images, and the ego-frame goal, the planner has access to the local lane graph in the ego neighborhood, including lane center-lines and connectivity. This local map information is treated as part of the driving interface, as in standard map or perception-based autonomous driving stacks. It does not provide scenario labels, expert trajectories, or scenario specific tuning. The observation $o\in\mathcal{O}$ contains (i) kinematic states $o^{\text{kin}}\in\mathbb{R}^{10\times 7}$ for up to ten vehicles, with per-vehicle features $[{\rm presence},x,y,v_{x},v_{y},\cos\psi,\sin\psi]$, (ii) an $80\times 80$ grayscale bird's-eye-view image $o^{\text{img}}\in\mathbb{R}^{80\times 80}$, and (iii) the goal position $o^{\text{goal}}\in\mathbb{R}^{2}$ expressed in the ego frame. The online planner operates on low-level actions $u_{t}=[a_{t},\delta_{t}]$, where $a_{t}$ is longitudinal acceleration and $\delta_{t}$ is steering angle.

### V-A MPC formulation

At test time, MPPI optimizes a horizon-$H$ sequence of low-level controls around a learned prior. The state of the ego vehicle is propagated with a kinematic bicycle model with control period $\Delta t=0.2s$. Writing the ego state as $x_{t}=[p_{x,t},p_{y,t},\psi_{t},v_{t}]$, the dynamics $f$ is represented as where $\beta_{t}=\arctan\!\left(\frac{\tan\delta_{t}}{2}\right)$ is the slip angle, and $l$ is the half length of the ego vehicle used by the simulator.

For the objective optimized by the planner, we use the same cost across all scenarios: where $v^{\star}=9$ m/s is the desired cruising speed and $d_{\rm lat}(x_{t})$ is the lateral offset from the closest valid lane centerline. A rollout is terminated early when the ego reaches the goal, collides, or leaves the road; in the code, the arrival threshold is 1.5 m from the goal. The terminal cost is configurable and includes the options where $g_{H}$ is the goal vector in the ego frame. In our experiments, we use $w_{v}=w_{a}=w_{\delta}=w_{\rm lat}=0.1,w_{\rm off}=w_{\rm col}=100$, and $w_{\rm term}\in\{1,5,10\}$. For MPPI hyperparameters, we use $H=8$ with $K=1000$ samples, sampling covariance $\Sigma=\text{diag}(0.8^{2},0.157^{2})$ and temperature $\lambda=0.01$.

### V-B High-level action model

We construct a compact high-level action space $\mathcal{U}_{\text{high}}$ by adapting the simulator's discrete meta-action model to preserve the Markov property needed for reinforcement learning. At each decision step, the policy selects one semantic driving command from $\mathcal{U}_{\text{high}}=\{\texttt{\scalebox{0.8}[0.95]{IDLE}},\texttt{\scalebox{0.8}[0.95]{FASTER}},\texttt{\scalebox{0.8}[0.95]{SLOWER}},\texttt{\scalebox{0.8}[0.95]{LANE_LEFT}},\texttt{\scalebox{0.8}[0.95]{LANE_RIGHT}}\}$. Each high-level action $h\in\mathcal{U}_{\text{high}}$ is then converted into a low‑level acceleration and steering action, for the ego state $x=[p_{x},p_{y},\psi,v]\in\mathcal{X}$ and observation $o\in\mathcal{O}$.

For longitudinal control, the current speed $v$ is first mapped to the nearest target speed in a discrete grid $\mathcal{V}=(v^{i})_{i=1}^{M}=(0,4.5,9)$. The FASTER and SLOWER actions increase or decrease the target-speed index by one, while all other commands keep the current target-speed index unchanged: where $\Delta(h):=\mathds{1}[h=\texttt{\scalebox{0.8}[0.95]{FASTER}}]-\mathds{1}[h=\texttt{\scalebox{0.8}[0.95]{SLOWER}}]$ is the index shift, and $\operatorname*{clip}_{[1,M]}z:=\min\left(M,\max(0,z)\right)$. The resulting target speed $v^{*}(v,h)=v^{i^{*}(v,h)}$ is then tracked by a proportional controller: where $K_{a}=1/0.6$ and $a_{\max}=5\ {\rm m/s^{2}}$.

For lateral control, LEFT_LANE and RIGHT_LANE select the closest feasible adjacent lane in the commanded direction using the local lane graph available to the planner. This conversion utilizes the local lane graph introduced above without any scenario-specific controller parameters or maneuver libraries. The lane selection respects lane boundaries and road connectivity. If no feasible adjacent lane exists, the target lane remains the current lane. Non-lane-change actions also keep the current lane as the target.

The target lane is tracked with a cascaded lateral controller for smooth and bounded steering commands. Let $(s_{\ell}(p),d_{\ell}(p))$ be the local longitudinal and lateral coordinates of the ego position $p=[p_{x},p_{y}]$ in lane $\ell$, and let $\theta_{\ell}(s)$ be the lane heading at longitudinal coordinate $s$. For the selected target lane $\ell_{\text{tar}}$, we use a short lookahead heading $\theta_{\rm fut}=\theta_{\ell_{\rm tar}}\bigl(s_{\ell_{\text{tar}}}(p)+v\tau_{p}\bigr)$ with $\tau_{p}=0.1$s. The controller then converts lane-tracking error into steering through three steps. First, the lateral offset to the target lane is converted into a desired lateral velocity $v_{\rm lat}=-K_{\text{lat}}d_{\ell_{\text{tar}}}(p)$ with $K_{\text{lat}}=0.5$. Then, this velocity is converted into a bounded heading correction relative to the lookahead lane heading: where $\bar{\psi}=\pi/4$, and $\operatorname{nz}(v):=\operatorname{sign}(v)\max(|v|,10^{-2})$ avoids division by zero. Third, the resulting heading error is converted into a desired yaw rate and then into a steering command through the bicycle-model geometry: where $K_{\psi}=3.0,\delta_{\max}=\pi/3$, and $\epsilon=10^{-3}$ prevents numerical singularities of evaluating $\tan(\cdot)$ at $\pm\pi/2$.

This action model exposes a small set of interpretable driving intentions to the high-level policy while guaranteeing bounded, dynamically meaningful low-level controls. Because the target speed and target lane are deterministic functions of the current state, observation, action, and local lane graph, the resulting high-level decision process remains Markov with respect to the planner's available information.

### V-C Reinforcement learning of high-level policy

We train the high-level policy with DQN across all driving scenarios. We use a dense reward that encourages fast goal reaching while penalizing accidents (collisions or off-road events), lane deviation, and control effort: where $\mathds{1}\{\cdot\}$ is the indicator function for an event, and $r_{\text{speed}}=\text{clip}\big(\frac{v-4.5}{4.5},-1,1\big),r_{\text{lane}}=\min\big(\frac{d_{\text{lane}}^{2}}{5},1\big),r_{\text{control}}=\big[(\frac{a}{5})^{2}+(\frac{\delta}{\pi/3})^{2}\big]$. Episodes terminate on goal reaching, collision, off-road departure, or timeout.

Figure 3: Architecture of the high-level policy model. A permutation-invariant attention-based vehicle-state encoder, a BEV image encoder, and a goal encoder are fused to generate a high-level driving intention that can be mapped to a nominal low-level action.

The policy network follows the architecture in Fig. 3. We utilize an ego-centric attention module as in to reflect the permutation-invariant structure of the vehicles' states. Separate embeddings are applied for the ego and neighboring vehicles, followed by two-head attention over the set of observed vehicles. The BEV image is encoded by a three-layer convolutional network, and the goal vector is encoded by a small multilayer perceptron. These three embeddings are concatenated and passed to the MLP head. In the configuration used in our experiments, the kinematic, image, and goal branches output 64, 64, and 16 features, respectively, followed by a $$ multilayer head. We train with 40 parallel environments for 7M environment steps, replay-buffer size 0.5M, batch size 1024, learning rate $3\times 10^{-4}$, discount factor $0.99$, and an $\epsilon$-greedy schedule with exploration fraction $0.2$ and final $\epsilon=0.05$.

### V-D World model

Our online rollout model is hybrid rather than fully learned. Ego kinematics are propagated analytically with the bicycle model above, while neighboring vehicles follow a constant-velocity model in the world frame for simplicity and speed. Learning the behavior of neighboring vehicles as part of the world model is a natural extension for more accurate prediction in complex settings such as urban driving, where interactive and less structured behaviors are more prevalent.

We additionally train a learned predictor for the next BEV image. Given the current observation and low-level action, the current image is first shifted through a map $T$ according to the ego translation, and the network $F_{\phi}^{\text{img}}$ predicts only the residual correction: The predictor uses the same kinematic, image, and goal encoders as the policy, adds an action encoder, and decodes the fused latent through a skip-connected deconvolutional network. Training data are drawn directly from the replay buffer used for RL, augmented with the executed low-level actions. The loss is a weighted pixelwise reconstruction objective over multi-step rollouts: where the per-pixel weights increase on foreground and edge: In our implementation, $\lambda_{\rm fg}=4.0$, $\lambda_{\rm edge}=2.0$, $\tau_{\rm fg}=0.55$, and $\tau_{\rm edge}=0.08$. We train with Adam with a learning rate $3\times 10^{-4}$, batch size 512, four-step rollout loss, and a teacher-forcing ratio linearly decayed from $1.0$ to $0.25$.

At planning time, image prediction is only needed for generating the nominal action prior. Once the prior is generated, the planner rolls out only the kinematic branches analytically and skips image prediction entirely for evaluating the sample control sequences around the prior.

### V-E Collision evaluation

We check collision by testing pairwise overlap between the ego vehicle and each neighboring vehicle using the separating axis theorem (SAT). SAT guarantees that two convex polygons do not intersect if there exists an axis along which their projections are disjoint. Vehicles are modeled as oriented rectangles. For each ego--neighbor pair, the algorithm evaluates the ego longitudinal and lateral axes together with the neighbor longitudinal and lateral axes.

Let $T\in\mathbb{R}^{2}$ denote the center displacement and let $v_{1},w_{1},v_{2},w_{2}\in\mathbb{R}^{2}$ be the two body-fixed axes of the ego and neighbor vehicles. Each ego--neighbor pair is declared separated if any of the four projections satisfy where $r_{(\cdot)}(a)$ is the projected half-extent on axis $a$. Otherwise, the pair intersects. We evaluate all MPPI samples and neighbors in parallel, enabling real-time planning.

## Experiments

### VI-A Experimental setup

We evaluate HOLO-MPPI on the benchmark introduced in Section V across all four scenarios. Each method is tested over 400 episodes (100 per scenario) We compare HOLO-MPPI against the following baselines.

SAC: RL policy trained via SAC acting directly in the original low-level action space $\mathcal{U}$.

Prior: Our high-level policy trained via DQN that is used as a sampling-prior generator for HOLO-MPPI.

FHP: Filtered high-level policy instances. Since the high-level policy is trained offline, collapsed training runs can be identified and excluded before deployment.

MPPI: Generic MPPI employing the previous plan as a prior (the initial prior is zero).

SAC/FHP ​+​ MPPI: MPPI with a prior generated by SAC or FHP as an ablation study.

We report the success rate (goal reached without collisions or going off-road) along with per-step control effort and comfort, defined as the squared sum of control action and its first-order difference, respectively.

### VI-B Reinforcement learning of high-level priors

Figure 4: Learning curves over 10 training runs for low-level (SAC) and the high-level policy (Prior). The top row shows episode reward and average success rate over training, while the bottom row breaks down success rate by scenario. Among the 10 high-level-policy runs, 3 collapsed during offline training and are reported separately as FHP.

Figure 4 compares the learning dynamics of the low-level policy (SAC) and the high-level policy (Prior) that is later used to parameterize MPPI's sampling distribution. SAC improves more rapidly during the early stage of training, suggesting that it quickly exploits the easier modes of the scenario distribution. However, the per-scenario curves on the lower left plot show that its performance is highly uneven: SAC achieves strong results on the simpler ( Straight and Merge ) scenarios, but remains much weaker on the more complex ( Intersection and Roundabout ) scenarios. In contrast, the high-level policy improves more gradually, yet ultimately attains a higher overall reward and average success rate while exhibiting a substantially more balanced performance profile across scenarios.

This distinction is important for HOLO-MPPI. The learned policy is not the final controller, but it is used as a sampling-prior generator for the downstream MPPI planner. In this role, broad competence across the scenarios is more valuable than near-optimal performance on only a subset of tasks. A prior that is consistently reasonable across scenarios provides a better warm start for MPPI and reduces the likelihood that online optimization begins from a poor mode. We therefore use our designed high-level policy as the nominal prior generator in the downstream HOLO-MPPI experiments.

### VI-C Main results

TABLE I: Performance evaluated over 400 episodes (100 per scenario) with mean ± std over 10 trained RL models. achieves the highest overall success rate while maintaining smoother control.

SAC ​+​ MPPI (mean) SAC ​+​ MPPI (best) FHP ​+​ MPPI (mean) FHP ​+​ MPPI (best) TABLE II: Success rate (%) evaluated over 400 episodes (100 per scenario) with mean ± std over 10 trained RL models from three different train steps. For the methods with MPPI refinements, we report the mean and best performances across the six terminal cost settings.

Table I summarizes performance across the four scenarios. Overall, HOLO-MPPI achieves the highest success rate while maintaining competitive control smoothness. Vanilla MPPI attains the lowest control effort, but this is unsurprising: without a learned prior, it tends to produce conservative, low-magnitude actions that fail to make progress when more aggressive motion is required, as seen in the Intersection scenario where turning maneuvers are necessary. The learned high-level policy alone (Prior) is already competitive, confirming that the abstract action space captures useful scenario-level intent. Coupling it with online MPPI further improves both success rate and control smoothness. We note that although these gaps appear to fall within the error bounds, the comparison is paired: MPPI is applied to the same models on the same episodes, so the gaps reflect a genuine gain from planning rather than evaluation noise.

The per-scenario breakdown reveals a complementary pattern. On the simpler scenarios ( Straight and Merge ), SAC and SAC + MPPI achieve the highest success rates, consistent with their tendency to overfit to easier modes of the scenario distribution. However, these gains come at the cost of substantially harsher control than HOLO-MPPI. Moreover, they collapse on the more challenging scenarios ( Intersection and Roundabout ), where success rates drop below 25%, while HOLO-MPPI maintains success rates above 50%.

Table II shows that this advantage persists across terminal-cost settings and how it develops as the high-level policy is trained. When the high-level policy is only partially trained (3.5M steps), HOLO-MPPI is competitive but not yet uniformly dominant, suggesting that MPPI cannot fully compensate for an immature prior. As the prior improves, however, the benefits of the hierarchical decomposition become more pronounced. At 7M steps, HOLO-MPPI clearly outperforms all baselines and remains robust to cost tuning.

The qualitative results are consistent with these quantitative trends. In Figure 5, vanilla MPPI and the SAC-based variants select poor turning modes in the intersection example and go off-road, whereas the learned high-level policy captures the correct maneuver. HOLO-MPPI then refines that intention into a trajectory that stays closer to the lane geometry and reaches the goal more cleanly than the prior alone. Figure 6 further shows that the learned world model preserves the coarse scene structure well enough to support rollout-based evaluation, although visible drift remains over longer rollouts.

Finally, Table III shows that the additional computation for prior generation and action conversion still leaves runtime compatible with 5Hz real-time control.

TABLE III: Planning time comparison. All methods are real-time capable with 5Hz operation.

Figure 5: 20-step (10 s) trajectory comparison in an intersection scenario. Starting from the same initial state, vanilla MPPI and SAC-based variants select poor turning modes and go off-road, whereas the learned high-level policy indentifies the correct maneuver. further refines this high-level intention via online MPPI, yielding a lower-cost trajectory that reaches the goal more efficiently while executing a smoother, lower-curvature turn.

Figure 6: Qualitative comparison of the learned world model over a rollout horizon in scenarios. For each scenario, the top row shows the evolution of the predicted BEV images, and the bottom row shows the corresponding ground-truth rollout. The model preserves coarse scene structure, but visible drift accumulates over longer horizons.

## Conclusion

We presented HOLO-MPPI, a hierarchical framework for multi-scenario motion planning that pairs a high-level learned prior with low-level online MPPI refinement. By learning in an abstract action space and refining in the original control space at test time, HOLO-MPPI achieves robust performance across diverse scenarios without per-scenario retuning. In our autonomous-driving experiments, this combination improves the success rate over vanilla MPPI and end-to-end RL baselines while maintaining smooth, real-time control.

Several directions remain for future work. Extending the world model to learn neighbor behavior could improve rollouts in interactive, less structured environments such as urban driving. Scaling to a broader set of scenarios and evaluating on held-out scenario types would further test the generalization of the learned prior. End-to-end training with differentiable MPPI in the loop could align the high-level policy more directly with downstream refinement. Finally, applying HOLO-MPPI to other robotic domains would test the generality of the hierarchical design.
