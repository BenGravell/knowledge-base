<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Contingency Planning for Safety-Critical Autonomous Vehicles: A Review and Perspectives

Topics include Vehicles, Safety, Benchmarks, Out-of-distribution generalization, Planning, Control, Contingency plan.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Contingency planning is the architectural capability that enables autonomous vehicles (AVs) to anticipate and mitigate discrete, high-impact hazards, such as sensor outages and adversarial interactions. This paper presents a comprehensive survey of the field, synthesizing fragmented literature into a unified logic-conditioned hybrid control framework. Within this formalism, we categorize approaches into two distinct paradigms: Reactive Safety, which responds to realized hazards by enforcing safety constraints or executing fail-safe maneuvers; and Proactive Safety, which optimizes for future recourse by branching over potential modal transitions. In addition, we propose a fine-grained taxonomy that partitions the landscape into external contingencies (environmental and interactive hazards) and internal contingencies (system faults). Through a critical comparative analysis, we reveal a fundamental structural divergence: internal faults are predominantly addressed via reactive fail-safe mechanisms, whereas external interaction uncertainties increasingly require proactive branching strategies. Furthermore, we identify a critical methodological divergence: whereas physical hazards are typically managed with formal guarantees, semantic and out-of-distribution anomalies currently rely heavily on empirical validation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We conclude by identifying the open challenges in bridging the gap between theoretical guarantees and practical validation, advocating for hybrid architectures and standardized benchmarking to transition contingency planning from formulation to certifiable real-world deployment.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous vehicles (AVs) operate in dynamic, unpredictable environments where events like sensor failures or unexpected behaviors of other agents can compromise safety. In such challenging scenarios, human drivers naturally employ contingency reasoning to manage uncertainty. For example, when approaching an occluded crosswalk, a driver may prepare to brake in case a pedestrian unexpectedly emerges. Similarly, to ensure reliable operation under such conditions, AVs must move beyond nominal planning and integrate contingency planning: the capability to anticipate, model, and respond to possible but uncertain deviations from expected operating conditions (alsterda2021contingency; li2023marc).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We define a contingency as a discrete, low-frequency, high-impact event that can be formalized as a logic-driven discrete mode switch in safety (e.g., "if a pedestrian appears from occlusion"). Examples include an actuator malfunction (alsterda2019contingency), a vehicle suddenly emerging from an occlusion (zheng2025oacp), or an aggressive merge by another driver (chen2022interactive). Such events are typically "known unknowns": their structural forms are known at design time, but their occurrence time, likelihood, and trajectory remain uncertain. This discrete, event-driven nature distinguishes contingencies from continuous uncertainties, such as sensor noise. Contingency planning involves managing modal deviations and logical branches of potential future states, thereby requiring specialized approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of contingency planning is twofold: to ensure safety under such events, and to avoid overly conservative behavior that compromises efficiency (wang2023interactive). This safety--efficiency trade-off is especially critical for SAE Level 4+ AVs, which operate without human fallback (gyllenhammar2025road). Without effective contingency planning, systems may fail when faced with unexpected edge-case events.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper formalizes contingency planning methods as two primary paradigms, which we derive from a unified logic-conditioned control framework based on different assumptions: Reactive Safety Methods (e.g., fail-safe switching), which assume that a contingency has already occurred and trigger predefined policies in response (e.g., "if sensor failure is detected, activate the backup system"). These methods generally rely on real-time monitoring and local policy filtering.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Proactive Safety Methods (e.g., branching model predictive control (MPC)), which anticipate potential contingencies before they manifest. These methods predict plausible future scenarios by constructing scenario trees and optimizing over them in real time. A shared nominal trunk is maintained, along with multiple branches for proactive adaptation, as shown in Fig. 1(b).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Figures 1 and 2 illustrate this fundamental distinction in urban and highway scenarios, respectively. Crucially, these paradigms are not mutually exclusive: both can be considered viable enforcement strategies within a unified logic-conditioned control framework. Moreover, they can form a complementary cycle: Proactive planning can help generate reactive safety certificates, while Reactive monitoring ensures the feasibility of Proactive plans under runtime uncertainty. This synergistic relationship is detailed in Sections 2.5 and 5.1.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To advance the development of contingency planning and overcome the current fragmentation in the field, a comprehensive synthesis of existing research is essential. This paper presents the first unified review of contingency planning for safety-critical AVs. Our key contributions are as follows: We establish a rigorous mathematical definition of contingency events as discrete, logic-conditioned modal transitions within a stochastic hybrid system. This formalization clearly demarcates contingencies from standard continuous uncertainties (e.g., sensor noise), providing a precise theoretical basis for safety-critical planning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a unified logic-conditioned hybrid control framework that synthesizes disparate methodologies under a single theoretical umbrella. By deriving Reactive safety and Proactive safety as distinct computational approximations of this underlying problem, we elucidate the structural connections and complementary nature of these paradigms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We perform a systematic comparative analysis of the trade-offs between safety guarantees, computational tractability, and behavioral conservatism. This analysis reveals a critical structural divergence: while internal system faults are predominantly addressed via Reactive mechanisms, external interaction and semantic uncertainties increasingly drive the adoption of Proactive strategies to maintain recourse. This synthesis establishes the theoretical basis for hybrid architectures that integrate the rigorous safety of reactive filters with the strategic foresight of proactive planning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as visualized in Fig. 3.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

This paper reviews contingency planning for safety-critical AVs. A contingency is a future event or circumstance that is possible but cannot be predicted with certainty (alsterda2021contingency). We define a contingency as a "known unknown": a discrete, low-frequency event formalized as a stochastic transition in the system's logical mode $\sigma_{k}\in\Sigma$ (e.g., the onset of a sensor fault or the resolution of an occlusion). Notably, while the global safety specification for the system is time-invariant (e.g., no collision), the specific admissible states for the ego vehicle depend on the environment configuration governed by the logical mode.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Contingency Planning Problem", "weight": 1.0} -->

The core contingency planning problem is to find a policy that optimizes performance while ensuring that safety requirements are satisfied under the hybrid evolution. To express safety in a way that explicitly couples logical conditions with continuous constraints, we use a temporal-logic specification. Let $\phi_{\text{safe}}$ be the safety formula where $\mathbf{G}_{[0,\infty)}$ denotes the temporal "Globally" operator over an infinite horizon (baier2008principles). This condition states that whenever the system is in mode $\sigma$, its state must lie in the corresponding safe set.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Contingency Planning Problem", "weight": 1.0} -->

Let $\mathcal{I}_{k}$ denote the information set available at time $k$ (e.g., history of observations). A causal policy $\pi$ maps $\mathcal{I}_{k}$ to control inputs $u_{k}=\pi(\mathcal{I}_{k})$. The contingency planning problem is formulated as where the probability is taken over realization of $v_{k}$, and $\epsilon\in$ is a user-specified risk tolerance. $\models$ denotes the satisfaction relation between a trace and a formula. Condition (3d) enforces safety over an infinite horizon, while makes the logical structure explicit.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Contingency Planning Problem", "weight": 1.0} -->

Solving exactly is intractable due to the stochasticity of $v_{k}$ and the combinatorial complexity of mode sequences. Therefore, the two predominant paradigms are distinguished by how the logical uncertainty is addressed in (1b) when enforcing (3d).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Solution Paradigm I: Reactive Safety", "weight": 1.0} -->

This paradigm is derived from the problem under a critical simplifying assumption: the logical uncertainty is resolved. Specifically, it assumes the discrete mode $\sigma_{k}$ is known or reliably estimated (e.g., a detected fault or observed occlusion).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Solution Paradigm I: Reactive Safety", "weight": 1.0} -->

Under this assumption, the contingency problem collapses into a local, deterministic enforcement problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Solution Paradigm II: Proactive Safety", "weight": 1.0} -->

Proactive methods tackle by explicitly handling unresolved logical uncertainty. Instead of conditioning on a single realized mode, this paradigm computes a tractable, finite-horizon approximation of by constructing a finite scenario tree $\mathcal{S}_{\mathrm{tree}}$ of plausible mode sequences and optimizing a non-anticipative policy over all branches. Let $\mathcal{S}_{\mathrm{tree}}$ be a finite set of $S$ plausible mode sequences. Each scenario (or branch) $s\in\mathcal{S}_{\mathrm{tree}}$ is a path of modes $(\sigma_{0,s},\ldots,\sigma_{N,s})$, where $\sigma_{k,s}\in\Sigma$ is the discrete mode at time $k$ along scenario $s$. The Proactive problem is then formulated as a Risk-Constrained Branching Decision Process (RCB-DP): where $c(\cdot,\cdot)$ is the stage cost, and $V_{f}(\cdot)$ the terminal cost.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Solution Paradigm II: Proactive Safety", "weight": 1.0} -->

$\tau(s,s^{\prime})$ is the first time at which scenarios $s$ and $s^{\prime}$ become distinguishable from the available information $\mathcal{I}_{k}$. The hard safety constraint (6d) enforces safety for every scenario, providing sample-path guarantees that satisfy (3d) when $\mathcal{S}_{\text{tree}}$ sufficiently covers the uncertainty distribution. Notably, the scenario set $\mathcal{S}_{\text{tree}}$ is typically discrete and identifiable. The non-anticipativity constraint (6e) formally couples all scenarios. It enforces identical decisions across scenarios that share the same information history (i.e., $k<\tau(s,s^{\prime})$), creating the "common nominal trunk" (Figures 1(b) and 2(b)). This constraint ensures that the resulting plan is physically executable (as only one $u_{k}$ can be applied at the current time) and maintains decision consistency while reasoning over multiple, unresolved futures.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Connections Between Paradigms", "weight": 1.0} -->

As approximations of the contingency problem, the Reactive (2.3) and Proactive (2.4) paradigms are not competing. Instead, each provides a critical component that addresses a fundamental weakness in the other.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Connections Between Paradigms", "weight": 1.0} -->

The effectiveness of the Reactive supervisor hinges on the quality of its pre-computed "safety critic" (e.g., the invariant set $\mathcal{X}_{\mathrm{inv},\sigma}$ in ). The synthesis of a high-quality, non-conservative set $\mathcal{X}_{\mathrm{inv},\sigma}$ is a complex, long-horizon optimal control problem that must account for all future modes. This offline synthesis is itself a look-ahead/proactive computation. Proactive tools, such as Hamilton-Jacobi (HJ) reachability (borquez2024safety) or an offline version of the scenario-based optimization, serve as the engines to compute the invariant sets that the computationally cheap, online Reactive filter relies on for its formal guarantees.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Connections Between Paradigms", "weight": 1.0} -->

Conversely, the Proactive method, as a finite-horizon approximation, has a primary weakness of guaranteeing safety and recursive feasibility after the horizon $N$. The Reactive paradigm provides the formal solution. By using the control-invariant set $\mathcal{X}_{\mathrm{inv},\sigma}$ from the reactive formulation as a terminal constraint in the proactive optimization, we guarantee recursive feasibility. The state constraints (6d) are strengthened: This constraint formally ensures that every branch of the Proactive plan terminates in a "safe anchor" state, from which the Reactive supervisor is provably able to maintain safety indefinitely.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Connections Between Paradigms", "weight": 1.0} -->

To characterize the fundamental limit of this safety guarantee, we define the backward reachable set of $\mathcal{F}_{\sigma}$, denoted $BRS(\mathcal{F}_{\sigma})$, as the inevitable failure set: the set of states from which entry into the failure set $\mathcal{F}_{\sigma}$ is unavoidable under any admissible control (mitchell2005time). Additionally, the complement of this inevitable failure set constitutes the maximal control-invariant set (blanchini1999set). Notably, Reactive safety will fail if the contingency happens in the region inside the inevitable failure set $BRS(\mathcal{F}_{\sigma})$. The Proactive planning can provide guidance by anticipating mode transitions and steering trajectories to avoid the inevitable failure set along the horizon, while anchors each branch in a control-invariant set.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reactive Safety Paradigms", "weight": 1.0} -->

The Reactive safety architecture employs hierarchical policies to ensure AVs maintain or transition to a safe state following a contingency. This paradigm operates under the assumption that the logical uncertainty has been resolved, such as a detected fault or imminent aggressive cut-in from another agent. This implies that the hazardous logical mode is not only currently identified but is assumed to persist deterministically over the immediate planning horizon.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reactive Safety Paradigms", "weight": 1.0} -->

The fundamental principle is recursive feasibility: at any time step $t$, an admissible control sequence must exist to keep all future states within the safe region $\mathcal{X}_{\mathrm{safe}}$. We formalize this through control-invariant sets $\mathcal{X}_{\mathrm{inv}}$ satisfying. If $x_{t}\in\mathcal{X}_{\mathrm{inv}}$, an admissible policy guarantees $x_{k}\in\mathcal{X}_{\mathrm{inv}}\subseteq\mathcal{X}_{\mathrm{safe}}$ for all $k\geq t$. This provides a recursive guarantee: if safety is maintainable at $t$, it remains maintainable indefinitely.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reactive Safety Paradigms", "weight": 1.0} -->

Within this framework, a nominal policy $\pi^{\mathrm{nom}}$ prioritizes task performance, while a safety supervisor $\pi^{\ell}$ monitors the state and intervenes according to the system dynamics. The supervised input is synthesized to ensure $x_{k+1}\in\mathcal{X}_{\mathrm{inv}}$, thereby preserving invariance. We categorize concrete supervisor realizations into two classes: task-preserving runtime filters (Section 3.1) and task-terminating fail-safe supervision (Section 3.2).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

Task-preserving filters instantiate the supervisor $\pi^{\ell}$ to monitor a performance-oriented policy $\pi^{\mathrm{nom}}$, intervening to modify commands only when necessary. For safety-critical AVs, a natural unifying viewpoint is to encode safety through a scalar safety value function $V_{\sigma}(x):\mathcal{X}\to\mathbb{R}$. For a fixed mode $\sigma$, the zero-superlevel set of this function, $\mathcal{S}_{{\sigma}}:=\{x\in\mathcal{X}\mid V_{{\sigma}}(x)\geq 0\}\subseteq\mathcal{X}_{\mathrm{safe},{\sigma}}$, defines the region of safe operation. The core mechanism of the filter is to enforce the forward invariance of $\mathcal{S}_{{\sigma}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

Contingency events, such as cut-ins or the appearance of occluded traffic, are modeled as discrete mode switches in the hybrid system model. These switches can induce instantaneous discontinuities in the safety landscape, drastically altering the feasible control space.^11^1Mathematically, a state $x_{k}$ that is safe under the current mode $\sigma$ (i.e., $V_{\sigma}(x_{k})\geq 0$) may immediately become unsafe under the new mode $\sigma^{\prime}$ (i.e., $V_{\sigma^{\prime}}(x_{k})<0$) before any continuous state evolution occurs. Conventional continuous-time safety certificates do not natively guarantee invariance across such arbitrary discrete jumps without robust pre-computation. As a result, the reactive supervisor must react immediately upon detecting a mode change, updating its control decision to account for the new safety landscape.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

Two prominent methods that adopt this reactive constraint-enforcement viewpoint are control barrier functions (CBFs) (ames2019control) and Hamilton-Jacobi (HJ) reachability analysis (choi2021robust).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

However, it is crucial to note that invariance is not guaranteed if the transition occurs in an inevitable collision state (e.g., a cut-in that is "too fast to stop"). In such cases, the supervisor may need to intervene preemptively---before the mode switch physically manifests---if the state approaches the boundary of the safe set for a predicted future mode. ^22^2This necessitates coupling the supervisor with a predictive module, bridging the gap to proactive paradigms discussed in Sec. 4.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

CBFs, which can be viewed as special instantiations of safety value functions, offer a geometric approach to enforce safety by establishing the forward invariance of a safe set $\mathcal{C}_{\sigma}\subseteq\mathcal{S}_{\sigma}$ (ames2019control). This is enforced by constraining the time derivative of the safety function $V_{{\sigma}}(x)$ (typically denoted $h_{{\sigma}}(x)$ in CBFs). The handcrafted, typically low-dimensional parametrization nature of CBFs provides a significant advantage: it enables explicit, interpretable safety specifications that encode domain knowledge and ensure robust, verifiable safety guarantees. However, this design flexibility introduces fundamental challenges. Constructing a valid CBF, that guarantees persistent feasibility under system dynamics and input constraints, remains difficult for complex driving scenarios. An invalid CBF can lead to optimization infeasibility during critical contingencies (e.g., aggressive cut-ins), rendering the safe control set empty (wabersich2023data).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

Moreover, even when valid, CBFs typically yield conservative safe sets that are subsets of the maximal control-invariant set. This inherent conservatism restricts the system from operating within a reduced safe region, potentially limiting operational efficiency.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

On the other hand, HJ reachability formulates the reachability of a target set as an optimal control problem. In this way, the safe value function $V_{{\sigma}}(x)$ is obtained by solving a Hamilton-Jacobi-Isaacs partial differential equation (PDE), explicitly accounting for worst-case disturbances or adversarial interactions (bansal2017hamilton; fisac2019general). The zero-superlevel set of the viscosity solution typically recovers the maximal control-invariant set $\mathcal{S}_{\infty}$, providing the least conservative formal guarantee. However, exact computation of this PDE suffers from the "curse of dimensionality," rendering it intractable for high-dimensional AV states (e.g., $\geq$ 5D) without strong decoupling assumptions. Practical implementations typically resort to low-dimensional abstractions, decoupling assumptions, and offline precomputation, which can limit applicability in complex contingency driving scenarios. Moreover, the resulting safe control policy tends to be overly conservative, leading to defensive driving behaviors even in nominal scenarios.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

These limitations have motivated recent efforts to synthesize more tractable and less conservative value functions, such as the Control Barrier-Value Function (CBVF) (choi2021robust). The CBVF is the viscosity solution to a modified Hamilton-Jacobi-Isaacs variational inequality that introduces a discount rate $\gamma\geq 0$, structurally embedding a CBF-like decay constraint within the reachability formulation. This yields the maximal safe set while enabling a less conservative optimal policy that permits approaching the safety boundary at a controlled rate $\gamma$. While this yields a less conservative policy, CBVF typically relies on grid-based PDE solvers and thus suffers from the same scalability issues as standard HJ. To address this computational bottleneck, recent research has pivoted toward data-driven approximations reviewed in (dawson2023safe; wabersich2023data).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

Connections: The safe set induced by a valid CBF ($\mathcal{C}_{{\sigma}}$) is strictly a subset of the maximal control-invariant set ($\mathcal{S}_{\infty}$) derived from HJ analysis ($\mathcal{C}_{{\sigma}}\subseteq\mathcal{S}_{\infty}$). Consequently, a valid CBF can be viewed as a computationally tractable but conservative lower bound on the optimal safety value function. Practically, a significant research trend focuses on the learning-based convergence of these paradigms to mitigate their respective limitations---specifically, the manual design complexity of valid CBFs and the curse of dimensionality inherent to HJ PDEs. Recent works leverage neural networks as universal function approximators to synthesize high-dimensional safety certificates.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Core Idea: The Unified Value Function", "weight": 1.0} -->

For instance, physics-informed frameworks like DeepReach (bansal2021deepreach), learn a neural value function $V_{\theta}(x)$ that approximates the HJ PDE solution while Neural CBFs optimize network parameters to maximize the safe set volume subject to validity constraints (dawson2023safe; liu2022safe2). To mitigate the black-box nature of the learned value functions, recent work introduces formal verification to prove the correctness of these functions (yang2025scalable). While this synthesis effectively shifts the computational burden offline, formally certifying that these learned representations provide rigorous safety guarantees for contingency events in safety-critical AVs remains a significant open problem. For a broader treatment of safe control methods, see related surveys (hsu2024safety; wabersich2023data; dawson2023safe).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation Strategies", "weight": 1.0} -->

Building on these principles, implementation strategies generally fall into two categories based on how they modulate the nominal policy: optimization-based filtering (minimally invasive) and policy switching. Both designs fit a unified supervisory architecture: a logical contingency predicate is monitored, and when it is triggered, the supervisor ensures that the system remains inside a zero-superlevel safe set of $V_{{\sigma}}(x)$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Implementation Strategies", "weight": 1.0} -->

Minimally Invasive Filters: These mechanisms actively modulate the nominal control input to satisfy safety constraints while minimizing deviation from the intended performance. This is most commonly instantiated as a CBF-based formulation, which is typically posed as a Quadratic Program (QP) that constrains the evolution of the safety function: where $\dot{h}_{{\sigma}}(x,u)=\nabla h_{{\sigma}}(x)\cdot f_{{\sigma}}(x,u)$ represents the evolution of the safety margin (where $\sigma$ remains fixed during the continuous interval between discrete transitions), and $\alpha$ is a class-$\mathcal{K}$ function tuning the allowable approach rate to the boundary.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implementation Strategies", "weight": 1.0} -->

In discrete-time AV implementations, this is typically enforced as a discrete barrier condition $h_{{\sigma}}(x_{k+1})\geq(1-\gamma)h_{{\sigma}}(x_{k})$ with $\gamma\in(0,1]$, ensuring asymptotic convergence to or invariance of the safe set.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation Strategies", "weight": 1.0} -->

Switching Filters: Alternatively, supervision can be implemented as an explicit policy switch. Consistent with the value-function viewpoint, the control law is: where $\delta>0$ serves as a buffered safety margin. The supervisor permits the nominal policy while the state remains in the interior of the mode-specific invariant set and triggers the dedicated backup policy $\pi^{\mathrm{safe}}$ (e.g., emergency braking) as the state approaches the boundary.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implementation Strategies", "weight": 1.0} -->

In practice, advanced AV safety architectures typically hybridize these patterns, prioritizing minimally invasive filtering for local deviations while reserving discrete mode switching for critical contingencies where safety constraints render the nominal optimization infeasible.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

This section maps common AV contingencies to the unified hybrid formulation established in Section 2, categorizing them by the specific system component that undergoes a discrete shift.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

The most fundamental class of contingencies involves discrete shifts in the system's dynamics $f_{\sigma}$ (Eq. (1a)), arising from physical faults or controller failures. To address physical component failures, zhang2025safe developed Fault-Tolerant CBFs (FT-CBFs) for nonlinear systems to guarantee safety despite actuator failures. They validated this framework on a Boeing 747 lateral control system, demonstrating that flight safety can be maintained even under severe rudder servo failures. For broader operational faults, singletary2022onboard addressed the contingency of radio communication failure. Here, the loss of the pilot's link represents a discrete transition to an unactuated mode; the onboard supervisor minimally modifies the pilot's last known commands to strictly enforce geofence boundaries during this blind phase. Similarly, when the nominal planner is a learning agent (e.g., end-to-end RL) or a fallible human operator, a policy failure manifests as a dynamics mismatch contingency---where the actual closed-loop evolution diverges from the supervisor's nominal model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

A general HJ reachability framework for this was developed by fisac2019general, where a value function characterizes the set of states from which constraint violations are avoidable. This framework can override a learning controller when dynamics mismatches are detected, as demonstrated in an aerial vehicle tracking task under sudden wind disturbances. Extending this to human-in-the-loop systems, oh2025safety proposed a Human-Centered Safety Filter (HCSF) for high-speed racing vehicles to handle the contingency of a human driver losing control (e.g., missing a braking point). While effective for safeguarding black-box policies, these methods suffer from a fundamental model-mismatch issue: the shield's safety guarantees are only as reliable as its underlying model (lu2025safe; goodall2023approximate; odriozola2023fear). Safety can be compromised whenever a contingency (e.g., an icy road) is unmodeled in both the nominal agent and the shield.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Furthermore, relying on supervisors for these internal failures can induce "skill degradation," as noted by oh2025safety, where the nominal agent fails to learn robust behaviors because the filter systematically masks its errors.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

In contrast to internal dynamics faults or nominal controller failures, environmental contingencies are governed by the logical mode $\sigma$ in Eq. (1b). In this context, a mode switch does not alter the physical capability of the AV but fundamentally contracts the admissible safe set $\mathcal{X}_{\mathrm{safe},\sigma}$ (e.g., due to obstacles or agent intent). For unexpected spatial constraints, strasser2024collision applied a minimalist intervention, velocity saturation, to autonomous e-scooters, clamping the speed command when a sudden obstacle contracts the available braking envelope. For AV navigation in unknown environments, bajcsy2019efficient addressed the contingency of sudden detection of a previously occluded obstacle, triggering a switch to a conservative safe kernel based on HJ analysis.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

To further account for active agents, liu2016enabling actively tracked the intention of other road participants and used an idea similar to CBF-QP to address contingencies (e.g., cut-in) in freeway driving; leung2020infusing applied HJ reachability to autonomous traffic weaving, treating any human action that eliminates a collision-free "escape maneuver" as a contingency. Similarly, hu2023deception addressed "deception games," where the contingency is a mismatch between the AV's belief and the human's actual hidden intent. To safeguard learning agents against these external hazards, wang2024safe and raeesi2025safe shield RL agents by constructing reachable sets that veto unsafe actions, ensuring safe driving within unpredictable traffic flows. While worst-case formulations like leung2020infusing provide rigorous guarantees, they can induce the "Frozen Robot Problem" (trautman2010unfreezing). Probabilistic relaxations hu2024active mitigate this by intervening only when risk exceeds a threshold, but they introduce a validity gap if the underlying belief model is miscalibrated.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Another challenging class involves the degradation of observability (Eq. (1c)), rendering the ego state $x_{k}$ uncertain. For example, chen2021safe used approximate reachability to handle ego-vision errors that corrupt safety boundary estimations in autonomous racing. Addressing direct hardware faults, laine2020eyesclosed proposed an "Eyes-Closed Safety Kernel" for visual-inertial navigation, which switches to a proprioceptive (IMU)-only fallback policy when vision fails. However, these approaches rely on idealized fault detection, assuming the system can instantly identify the onset of a sensor fault or occlusion. In practice, faults are typically gradual or ambiguous (e.g., calibration drift), leading to reactive latency or chattering between modes. Moreover, binary fallback policies tend to be excessively conservative for highway speeds. Moving beyond binary switching, yun2025atom introduced an adaptive CBF (ATOM-CBF) that continuously adjusts the safety margin based on real-time epistemic uncertainty.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

This allows the filter to gracefully degrade performance in the presence of out-of-distribution (OOD) measurements, maintaining safety without triggering abrupt maneuvers. While this mitigates the latency of binary detection, it introduces a critical dependency on uncertainty calibration. If the learned uncertainty estimate is miscalibrated (e.g., underestimating the risk of an OOD sample), the resulting safety margin will be insufficient to guarantee invariance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Across these examples, task-preserving runtime safety filters are typically analyzed under simplified dynamics and idealized contingency predicates provided by upstream modules. However, safety filters must interface with perception and prediction systems that expose complex, learned uncertainties in deployed AV stacks. Additionally, they must also operate under tight real-time and hardware constraints. Systematically quantifying how these filter guarantees compose with upstream perception uncertainty remains a critical open challenge.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Task-terminating Fail-safe Supervision", "weight": 1.0} -->

While task-preserving filters enforce stepwise safety during nominal operation, contingencies such as severe sensor degradation, mechanical failure, or unresolvable environmental conflicts may render the mission infeasible. In such cases, the system must execute a deliberate transition to a safe terminal state. This task-terminating regime is the domain of fail-safe supervision, a specialized safety filter typically residing at the highest level of the control hierarchy.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Task-terminating Fail-safe Supervision", "weight": 1.0} -->

Fail-safe supervision prescribes fallback maneuvers and specifies their triggering conditions, with the primary objective of achieving a *Minimal Risk Condition* (MRC), such as safely stopping on the road shoulder (stolte2021taxonomy; iso4804_2020). The mathematical objective shifts from *invariance* to *convergence*. Unlike task-preserving methods which maintain $x_{t}\in\mathcal{X}_{\text{inv}}$, fail-safe supervision seeks a policy $\pi^{\mathrm{fs}}$ that ensures finite-time convergence to a terminal safe set $\mathcal{X}_{\text{MRC}}\subset\mathcal{X}_{\text{safe}}$ while maintaining safety constraints throughout the transition. In practice, this terminal set $\mathcal{X}_{\text{MRC}}$ typically corresponds to a static "stop" state (i.e., zero velocity), ensuring the vehicle remains passively safe indefinitely.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Task-terminating Fail-safe Supervision", "weight": 1.0} -->

Formally, the set of valid fail-safe policies is defined as: A primary challenge in this domain is the online synthesis of verified, dynamically feasible, safe backup trajectories. We categorize existing approaches by their abstraction level: continuous trajectory synthesis, discrete logical supervision, and system-level safety architectures.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Task-terminating Fail-safe Supervision", "weight": 1.0} -->

The primary algorithmic challenge is synthesizing a dynamically feasible trajectory that terminates in $\mathcal{X}_{\text{MRC}}$. Early approaches relied on infinite-horizon invariant sets (blanchini1999set), which are typically computationally prohibitive for real-time applications. To address this, Pek2018SafeStates proposed under-approximating invariant sets online. Building on this, Pek2021Failsafe introduced an online verification framework based on convex optimization. By verifying that a valid trajectory to a safe state always exists within a finite horizon, this method ensures recursive feasibility without computing the full maximal invariant set. Safe stochastic MPC has extended these ideas by explicitly planning safe backup trajectories, accounting for operational uncertainties through set-based reachability analysis (Brudigam2023). However, recursive feasibility in these frameworks relies on the assumption that surrounding agents adhere to modeled behaviors (e.g., traffic rules). This limits robustness in non-compliant scenarios where the fail-safe maneuver itself might provoke a collision.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Task-terminating Fail-safe Supervision", "weight": 1.0} -->

For discrete system failures (e.g., GNSS signal loss or software process crashes), fail-safe logic is typically synthesized using formal methods (schurmann2017ensuring; Krook2019; krook2020formal). For instance, when considering ego-vehicle localization failures, such as GNSS faults, specifications formalized in linear temporal logic (LTL) have been used to verify a supervisory controller that manages scenario switches between nominal planners and safe-stop trajectory planners (Krook2019). Building on this, automated synthesis techniques have been explored. krook2020formal utilized supervisory control theory and reactive synthesis to generate correct-by-construction tactical planners. By shifting the effort from manual implementation and verification to formal requirement specification, these methods generate correct-by-construction supervisory controllers that guarantee the system transitions to the correct fallback mode upon fault detection. A fundamental limitation here is the abstraction gap. Formal synthesis typically operates on a discrete abstraction of the system. Mapping these discrete guarantees to the continuous, non-linear dynamics of a vehicle executing a high-speed emergency stop remains a significant validation challenge.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Task-terminating Fail-safe Supervision", "weight": 1.0} -->

Complementing algorithmic supervision, system-level research focuses on hardware and software architectures with inherent fault tolerance (julitz2023computer; grubmuller2019fault). For example, julitz2023computer proposed fault-tolerant hardware architectures for AVs, emphasizing redundancy, diversity, separation, self-diagnosis, and reconfiguration to enhance system reliability. Real-world implementations, such as the Mercedes-Benz DRIVE PILOT, integrate redundancy in braking and steering to ensure controllability during component outages (mercedesbenz2022). While redundancy provides the highest robustness, it incurs high cost and weight penalties. Moreover, managing the "handover" logic between redundant systems (e.g., voting schemes) introduces its own complexity and potential failure modes, which are typically under-represented in algorithmic safety literature.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

In practice, the selection of a fail-safe strategy is driven by the specific nature of the contingency event.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Actuation and Dynamics Faults: For critical hardware failures, research concentrates on fault-mitigating control algorithms and redundant system architectures designed to preserve basic vehicle controllability for emergency maneuvers (yue2019automated; boudali2018emergency; khelladi2020emergency; lodder2023optimization; duerr2020realtime; li2023novel). For example, li2023novel; li2020shared proposed a trust-based shared control framework to address tire blowouts on highways. This framework dynamically allocates steering authority based on the driver's panic level to prevent destabilizing inputs. For power steering failures, lodder2023optimization utilized nonlinear MPC to compute safe-stop trajectories that explicitly account for limited steering torque. Expanding to simultaneous fault detection and control, lee2022adaptive applied an adaptive sliding mode control (SMC) scheme to AVs. This approach enables real-time compensation for actuator loss of effectiveness while maintaining lateral stability.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Environmental and Interactive Hazards: For contingencies arising from interactive uncertainty (e.g., the unpredictable intentions of other agents), techniques leveraging reachability analysis and online verification are preferred to ensure robust, worst-case compliant maneuvers (Althoff2013; Magdici2016; schurmann2017ensuring; Pek2021Failsafe; Brudigam2023). In conditional automation scenarios, the challenge extends to human-vehicle interaction. Addressing this, Xue2023Shared; Xue2022Override developed shared control frameworks that estimate driver intention during critical failures. These systems utilize real-time risk assessment to determine the feasibility of a safe driver takeover, facilitating a manual transition only when the automated system's capabilities are exceeded.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Observability and Perception Failures: In contrast, sensor and localization faults, such as GNSS or LiDAR failures, require discrete logic to switch state estimators. The focus shifts to strategies for fault detection, sensor isolation, and fallback localization to maintain a reliable state estimate (Krook2019; Viana2022; grubmuller2019fault). Addressing extreme power blackouts where all external positioning is lost, jonasson2020 validated a "Blind Safe Stop" application relying exclusively on wheel-speed and pinion-angle sensors. Similarly, perception system malfunctions are mitigated through methods that employ virtual sensors or revert to conservative, predefined environmental assumptions (Xue2019Virtual; Xue2018Fallback). Specifically, these methods project phantom obstacles into the undetected area, forcing the fail-safe planner to execute conservative avoidance maneuvers as if the blind spot were occupied.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Concrete Examples in AV Contingency Scenarios", "weight": 1.0} -->

Despite these advances, fail-safe supervision remains an open research problem. Most methods operate under idealized assumptions regarding fault detection, actuation, and communication. Constructing backup trajectories robust to tracking errors, actuator saturation, and noisy fault indicators is critical. Furthermore, current architectures rarely link formal fail-safe concepts to regulatory definitions of MRCs or rigorously analyze the coupling between fail-safe actions and upstream perception modules. Bridging these gaps is essential for translating algorithmic prototypes into certifiable safety architectures.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Proactive Safety Paradigms", "weight": 1.0} -->

The Reactive safety paradigms discussed in Section 3 operate on the premise that the logical contingency mode is resolved or reliably estimated. While this architecture offers rigorous safety guarantees with low online computational cost, its fundamental limitation is the inability to reason about unresolved logical uncertainty. Lacking a mechanism to anticipate future mode transitions, Reactive methods typically default to worst-case assumptions to ensure invariance. This leads to excessive conservatism. For example, a false-positive pedestrian detection may trigger unnecessary braking, compromising task efficiency.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Proactive Safety Paradigms", "weight": 1.0} -->

This motivates Proactive contingency planning frameworks that explicitly reason about multiple possible futures rather than filtering a single plan post hoc. In such frameworks, the evolution of logical modes is represented by a scenario tree. A single non-anticipative policy is optimized over this tree, enforcing identical actions for scenarios that remain informationally indistinguishable.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Proactive Safety Paradigms", "weight": 1.0} -->

We formalize this perspective as an RCB-DP, as introduced in Section 2.4. The framework provides an optimization-based approach for Proactive contingency planning, supporting pre-defined or dynamically generated branches. Crucially, it enables sequential branching decisions that defer final action commitments until key uncertainties are resolved, reducing conservatism while maintaining operational safety throughout.

<!-- chunk {"id": "body-0067", "role": "body", "section": "From Min-Max MPC to Contingency MPC", "weight": 1.0} -->

Min-max MPC has long served as a fundamental framework for robust control under bounded uncertainty. scokaert1998min; batkovic2021robust distinguished between open-loop and closed-loop variants: the former generates a single control sequence that hedges against all admissible disturbance realizations, typically resulting in overly conservative behavior, whereas the latter leverages feedback to adapt actions in response to realized disturbances. In classical formulations, uncertainty is represented as bounded disturbances acting on the system dynamics (scokaert1998min).

<!-- chunk {"id": "body-0068", "role": "body", "section": "From Min-Max MPC to Contingency MPC", "weight": 1.0} -->

Early open-loop min--max schemes optimize a fixed control sequence across all possible disturbance sequences, disregarding the fact that a receding-horizon controller naturally re-optimizes as new measurements become available (Zheng1993). This mismatch typically led to excessive conservatism and infeasibility in practice. In contrast, feedback-aware (closed loop) min-max MPC (scokaert1998min; lucia2013multi) represents the evolution of uncertainty using a scenario tree, as illustrated in Fig. 6(a). Each tree branch corresponds to a possible realization of future disturbances, and non-anticipativity constraints (rockafellar1976nonanticipativity) ensure that decisions remain identical across branches until the uncertainties are resolved. This tree structure can handle multiple disturbance realizations within a single optimization problem. However, its exhaustive coverage of all admissible disturbance combinations leads to exponential growth in complexity. To reduce the computational burden, as shown in Fig. 6(a), the scenario tree stops branching after a certain time step.

<!-- chunk {"id": "body-0069", "role": "body", "section": "From Min-Max MPC to Contingency MPC", "weight": 1.0} -->

Contingency MPC, a specialized form of scenario-tree-based MPC, has been applied to AV planning due to its capability to handle uncertainty and constraints. For example, an AV may experience a sudden loss of traction or the emergence of unexpected obstacles (alsterda2021contingency), or face interaction dilemmas, such as whether a nearby vehicle will yield (zhan2016non). In such settings, worst-case optimization across incompatible outcomes can hinder responsiveness and produce inconsistent plans (elango2025deferred).

<!-- chunk {"id": "body-0070", "role": "body", "section": "From Min-Max MPC to Contingency MPC", "weight": 1.0} -->

To address this limitation, contingency MPC explicitly plans over a finite set of plausible future scenarios while maintaining a feedback-aware receding-horizon structure (alsterda2019contingency). Rather than committing to a single trajectory, it constructs a compact scenario tree consisting of a shared trunk for immediate execution and multiple branch-specific tails as safe alternatives (hardy2010contingency; geurts2025contingency). This preserves decision consistency and feasibility while enabling timely adaptation to unfolding events. In contrast to the scenario tree used in min-max MPC, the tree in contingency MPC, as illustrated in Figs. 6(b) and 6(c), often exhibits various structures, which are customized to suit different applications.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

The foundational concepts of contingency MPC were established by early works addressing well-specified contingency scenarios. These studies introduced a formal "Plan-B" concept for specific vehicle-state hazards, such as unexpected loss of road friction, which induces a switch in the system dynamics (1a) (alsterda2019contingency; alsterda2021contingency). Other studies have focused on uncertainty in logical modes, including the resolution of binary interaction dilemmas (e.g. "yield versus go" at intersections), and the development of optimization-based planners that handle mutually exclusive obstacle predictions by optimizing multiple contingency paths with a shared initial segment under probabilistic collision constraints (hardy2013contingency).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

Subsequent approaches extended this multi-hypothesis principle to handle multi-modal predictions of other agents (RosoliaBMPC2023; BouzidiBMPC2024). In these methods, the motion of the other agents, predicted by rule-based or learned models, is typically nonreactive. To better account for interactions, qiu2020latent and hu2024active incorporated interaction-aware models and belief propagation into a tree-structured planning framework, allowing the planner to automatically balance trajectory cost reduction with information gathering. In safety-critical domains such as autonomous driving, risk-aware approaches have also been proposed to manage low-probability, high-impact outcomes during scenarios such as merging, cut-ins, and highway driving. These methods address such challenges by incorporating risk-sensitive objectives, many of which are based on Conditional Value at Risk (CVaR), as demonstrated in approaches such as Branch MPC (chen2022interactive), MARC (li2023marc), and EraBMPC (ZhangEraBMPC2024).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

Other notable risk-aware frameworks include the interaction-aware branch MPC by wang2023interactive, which employs smooth sigmoid approximations of chance constraints to reduce conservatism while maintaining safety in discrete multi-modal scenarios. Additionally, RACP (mustafa2024racp) introduced custom probabilistic metrics based on the product of collision probability and severity, enabling a more nuanced risk assessment. Such planning is typically coupled with high-level decision-making frameworks, such as Partially Observable Markov Decision Processes (POMDPs), to ensure the branching structure is guided by a robust, long-term belief state (ulfsjoo2022integrating).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

Most existing contingency-planning schemes lack explicit occlusion assessment. To further account for potential phantom vehicles in occluded driving environments, an occlusion-aware contingency game was introduced within a receding-horizon planning framework (qiu2024inferring). Alternatively, nyberg2025hope integrated formal reachability analysis into a tree-based motion planner. By over-approximating the forward reachable sets of occluded agents, this framework guarantees the existence of a valid braking contingency without the excessive conservatism of assuming the object is always present. Despite such advancements, scaling contingency planners to real-time operation in multi-vehicle settings remains challenging, especially in dense and partially observable traffic scenarios. To enhance computational efficiency, distributed optimization techniques such as the Alternating Direction Method of Multipliers (ADMM) offer a promising solution. By iteratively solving decoupled subproblems, ADMM achieves better computational efficiency compared to traditional optimization methods (boyd2011distributed).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

For example, recent consensus ADMM-based formulations have generated safe contingency plans around occlusions where multiple agents may appear unexpectedly in partially observed environments (zheng2025safe; zheng2025oacp).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

Formal safety guarantees for contingency MPC have been an active area of research. A key research direction focuses on the integration of formal methods to provide verifiable safety against the worst-case outcomes of multi-modal predictions. This includes the use of reachability analysis to certify that all planned branches are safe (bouzidi2025reachability), with some approaches leveraging online event-triggered learning for less conservative safety barriers while maintaining feasibility in interactive dense traffic (yang2025safe). To ensure persistent feasibility during planning, other methods used control-invariant sets $\mathcal{X}_{\mathrm{inv}}$, which guarantee that the vehicle can always be steered back into a pre-computed safe state during aggressive maneuvers in mixed traffic (chen2023invariant; schweidel2022driver). Building on this, geurts2025contingency proposed a multi-horizon contingency MPC framework for safe learning that formally establishes robust recursive feasibility by employing control-invariant terminal sets, specifically using the union of two disjoint robust control-invariant sets for merging behind or ahead of other vehicles.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

Likewise, contingency-aware nonlinear MPC provided a unified formulation for complex driving maneuvers, achieving practical stability and recursive feasibility in dynamic traffic by enforcing control-invariant terminal sets with an LQR fallback (lin2025contingency).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Contingency MPC and Applications", "weight": 1.0} -->

While such algorithmic advances addressed the tractability of solving a given scenario tree, a key formulation challenge remains in determining the optimal branching point (bouzidi2025reachability). Fixing this branching point a priori, as is common, prevents adaptation to dynamic uncertainties and can induce either overly conservative behavior or unsafe reactive latency. Recent studies (tas2018decision; bouzidi2025reachability) proposed adaptive strategies that determine the branching time online using information-based or reachability-based criteria. The adaptive‑branching mechanisms arising from these developments are further discussed in Section 5.3.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Game-Based Contingency Planning", "weight": 1.0} -->

While scenario-tree MPC handles discrete contingencies, game-based contingency planning enhances this capability by reasoning about strategic interactions among agents (paden2016survey). Unlike approaches that treat other agents as passive participants following fixed predictions, game-theoretic planners assume that all agents are rational decision-makers optimizing their own objectives. This assumption enables the AV to anticipate and influence the behavior of other agents in interactive scenarios. Early work typically adopted Stackelberg leader-follower models, where the AV acts as the leader and optimizes its trajectory, assuming that others respond optimally as rational followers. While effective in generating socially aware behaviors, such models typically assume a single deterministic response from other agents, limiting their ability to capture multi-modal interactions or prepare for contingencies.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Game-Based Contingency Planning", "weight": 1.0} -->

To overcome this limitation, recent studies have integrated game-theoretic models into the framework of contingency planning, thereby explicitly accounting for multiple possible future scenarios. For instance, in complex negotiation scenarios such as lane merging, a matrix game can be formulated and solved to obtain multiple equilibria that capture the diverse driving decisions of other agents. These equilibria define the branches of a scenario tree, allowing a branch MPC to generate contingency plans over plausible outcomes (zhang2024automated). A more integrated approach was introduced as contingency games for multi-agent interaction, which directly embeds multi-policy reasoning into the game problem (peters2024contingency). In this framework, each agent selects from a discrete set of high-level policies (e.g., "yield" or "maintain speed"), and solves for a shared trunk trajectory that remains feasible and safe across all policy combinations. To facilitate high computational efficiency, recent work further modeled interactions as pairwise games, where the strategy space itself forms a trajectory tree, allowing the game solution to directly yield a branching contingency plan in real-time (ma2025trajectory).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Game-Based Contingency Planning", "weight": 1.0} -->

Furthermore, huang2025fast introduced a Bayesian game-based formulation to address intentional uncertainty in contingency planning. By modeling agent intentions probabilistically, this approach casts interactions as potential games, where the Bayesian Nash Equilibrium provides an optimal solution for interactive trajectory planning under uncertainty. To improve scalability, the authors employ a dual consensus ADMM algorithm for parallel optimization, making real-time interactive contingency planning feasible even in complex, multi-agent urban traffic scenarios.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Game-Based Contingency Planning", "weight": 1.0} -->

Additionally, game theory can be leveraged to address contingencies arising from partial observability, such as the presence of agents in occluded driving areas (Zhan-RSS-21). By formulating the problem as a dynamic game with imperfect information, the planner can reason about the worst-case actions of a potential hidden agent in occluded urban interactions (qiu2024inferring). The resulting trajectory remains robust against the potential emergence of occluded agents, thereby intrinsically generating a contingency plan for high-risk occlusions.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Game-Based Contingency Planning", "weight": 1.0} -->

Despite their theoretical promise, game-based contingency methods face several practical challenges. First, their performance is highly sensitive to the accuracy of the assumed or learned cost functions of other agents. Moreover, solving multi-agent dynamic games, especially those involving branching structures or imperfect information, remains computationally demanding, which constrains real-time applicability in dense traffic settings. Critically, these methods only address logical modes that alter the safety specification (e.g., resolving ambiguity in intent that defines the admissible safe set), rather than modes governing internal system faults (e.g., dynamics degradation or sensor outages)

<!-- chunk {"id": "body-0084", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Learning-based methods expand contingency planning beyond traditional analytical models, enabling AVs to predict, adapt, and react to open-world uncertainties using data-driven approaches. These methods generally fall into three categories: (i) behavioral topology and structured interaction modeling, (ii) multi-future prediction and contingency-policy learning, and (iii) foundation-model-driven anomaly detection and fallback planning.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Topology-aware representations provide a structural foundation for branching-based contingency planning by encoding the qualitative modes of multi-agent interaction to impose behavioral consistency. Mavrogiannis et al. (mavrogiannis2019multi; mavrogiannis2024abstracting) have modeled social navigation as braid-theoretic equivalence classes of joint trajectories, capturing whether one agent yields, overtakes, or merges relative to another. While these studies focus on a single plan, they provide a foundation for representing interaction modes. Behavioral Topology (BeTop) (liu2024reasoning) extended this topological modeling into a learning-based branching framework. Rather than treating interaction as generic complexity, BeTop utilizes topological invariants to discretize multi-agent behaviors into a finite set of logical modes. In this framework, the contingency is formalized as the uncertainty over which topological class (e.g., a specific yield" vs. cut-in" braid) will materialize. By constructing a behavioral prior derived from braid theory, BeTop aligns prediction with planning via its BeTopNet, thereby improving coherence across interacting agents in dense traffic.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Consequently, the branching structure of BeTopNet enables the planner to effectively manage the uncertainty inherent in multi-agent interactions.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

While topological methods define the abstract structure of interactions, the second category addresses contingency reasoning as a data-driven inference problem. Early sampling-based approaches, such as LookOut (cui2021lookout), introduced end-to-end multi-future prediction and planning frameworks that construct explicit contingency branches through stochastic rollouts and collision-set pruning. However, this approach assumes that non-ego agents follow fixed, independent forecasts. To address this limitation, chen2023tree proposed Tree-Structured Policy Planning, which combines the ego motion sampler and the ego-conditioned prediction model to generate multi-stage motion plans. Huang2024DTPP advanced this line of work by unifying tree-structured planning and prediction through a query-centric Transformer model with learnable cost functions. Subsequent works, such as Contingencies from Observations (rhinehart2021contingencies), Active Visual Planning (packer2023anyone), and Conditional Behavior Prediction (tolstaya2021identifying), learn contingency-aware policies directly from raw observations, allowing adaptation to occluded or unobserved agents.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Leveraging generative models, CoPlanner (zhong2025coplanner) advances this direction with a diffusion-based motion planner that jointly generates interactive multi-agent trajectories, enforcing a shared short-term segment for stability and diverse long-horizon branches for contingency. However, CoPlanner lacks recursive feasibility guarantees and relies on fixed branching and uniform scenario weighting, which limits adaptability to diverse driving contexts. These learning-based approaches move contingency planning from fixed scenario enumeration toward adaptive, probabilistic reasoning over learned future distributions.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

When AVs encounter scenes that differ significantly from the training data, they may experience OOD semantic failures that traditional contingency planners do not anticipate. To address this, recent work uses the general knowledge of foundation models to interpret and react to unforeseen high-level hazards. sinha2024real introduced a two-stage large language model (LLM)-based framework: a fast anomaly test in an LLM embedding space triggers a slower generative stage that decides how to respond, while the branch MPC maintains feasible fallback trajectories to ensure safety during the generative latency. The fast stage runs at real-time rates on embedded hardware, and the approach has been validated in driving scenarios under AV perception failures in CARLA, as well as on quadrotor landing tasks. Moving from reactive fallback selection to proactive failure prevention, ganai2025real proposed FORTRESS, a framework that uses multi-modal foundation models to anticipate semantic failure modes and generate new, dynamically feasible fallback plans for AVs in real time.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

This approach enhances robustness by synthesizing strategies adapted to unforeseen hazards (e.g., road closures, urban disruptions, and semantically unsafe regions) rather than relying on predefined sets. These large-model-driven systems represent a significant evolution in contingency planning, combining low-level dynamic safety with high-level semantic reasoning to achieve more robust autonomy.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Reactive Paradigm (Section 3) Proactive Paradigm (Section 4) State-Based Invariance or Convergence. Guarantees state constraints (x ∈ 𝒳inv) or finite-time safe termination (xT ∈ 𝒳MRC) for all bounded disturbances. Sample-Path Safety. Guarantees safety for the finite set of modeled scenarios. Subject to risk if the realized scenario lies outside the modeled tree support.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

High. Typically assumes the environment is adversarial to ensure a valid fallback exists at all times. Tends to be overly cautious as the fallback policy relies on precomputed offline synthesis. Reduced (Recourse-Aware). Optimizes a shared nominal trunk that remains feasible for multiple futures. Reduces conservatism by deferring the commitment to a specific branch.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Offline-Heavy (Synthesis) / Online-Light (Execution). Relies on precomputed safety critics (e.g., value functions, invariant sets). Runtime is typically a fast algebraic check or QP. Online-Heavy. Solves large-scale optimization problems (e.g., Scenario Trees) at every timestep. Requires specialized solvers (e.g., ADMM, Riccati) for real-time performance.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Dimension-Limited. Runtime execution scales well with agent count, but synthesizing a high-fidelity invariant set suffers from the “curse of dimensionality,” limiting methods to low-dimensional systems. Scenario-Limited. Complexity scales with the tree size (branching factor × depth). Managing combinatorial uncertainty from multiple contingency events or long horizons requires aggressive pruning.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Learning-Based Contingency Planning", "weight": 1.0} -->

Triggered Response. Intervenes only when the safety margin is depleted, or a fault is detected. Lacks the foresight to avoid the “point of no return.” Anticipatory Recourse. Proactively preserves future options. Enables information-seeking actions to resolve uncertainty before branching.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Computational Methods", "weight": 1.0} -->

The computational burden of contingency planning arises primarily from the dimensionality introduced by branching trajectories and the nonconvex constraints associated with safety-critical environments.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Computational Methods", "weight": 1.0} -->

Trajectory planning problems are generally formulated as nonlinear optimization problems and solved using general-purpose solvers, such as IPOPT (wachter_implementation_2006), SNOPT (gill_snopt_2005), and Knitro (pardalos_knitro_2006). To efficiently solve the planning problem, a solver must leverage the sparsity pattern introduced by system dynamics. In these general-purpose solvers, sparsity is typically detected and exploited by sparse linear solvers. Alternatively, customized numerical optimal control solvers, such as acados (Verschueren2021), FORCESPRO (FORCESNLP), Crocoddyl (mastalli20crocoddyl), CFS (liu2018convex), and Aligator (jallet2025), can explicitly leverage the sparsity pattern via Riccati recursion. These solvers differ primarily in their approaches to constraint handling.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Computational Methods", "weight": 1.0} -->

Similarly, trajectory planning problems with tree structures can also be solved using the aforementioned general-purpose solvers or numerical optimal control solvers. However, one additional computational challenge arises from the increased dimensionality of the decision variables due to the use of scenario trees. Therefore, a high-performance solver must leverage the sparsity pattern introduced by the scenario tree. Yet, this pattern is typically not fully exploited by the sparse linear solvers used in general-purpose solvers and has not been supported by common numerical optimal control solvers. This motivates the development of tailored Riccati recursion methods (FRISON201714399) and matrix factorization techniques (Klintberg2017; schwan2025piqp_multistage). These customized methods typically involve performing multiple independent factorizations along the scenario tree paths, potentially in parallel, followed by an additional factorization to satisfy causality constraints near the tree root.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Computational Methods", "weight": 1.0} -->

Another category of approaches applies the so-called dual decomposition technique to the scenario-tree problem (Klintberg2016Dual; kouzoupis_dual_2019; kouzoupis_dual_2018). The subproblems can be addressed in parallel and subsequently coordinated by solving a dual Newton system. Beyond these structure-specific techniques, consensus ADMM provides a general decomposition framework for efficient distributed computation (boyd2011distributed; ghadimi2015optimal). By reformulating the nonlinear program into a series of low-dimensional subproblems with consensus constraints, it enables scalable decomposition in contingency planning (phiquepal2021control; zheng2025safe; yang2025safe; huang2025fast). Recent studies by zheng2025occlusion; zheng2025oacp have demonstrated that such formulations can achieve real-time performance in dense, occlusion-aware driving scenarios on both simulation and hardware AV platforms, with runtimes on the order of tens of milliseconds.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Computational Methods", "weight": 1.0} -->

Nevertheless, the convergence speed remains sensitive to the tuning of penalty parameters, and inappropriate choices may increase iteration counts or degrade solution quality, which limits robustness in safety-critical applications.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we comparatively analyze the two primary contingency planning paradigms: Reactive and Proactive planning. We first synthesize their shared scientific principles and core trade-offs regarding safety, efficiency, and scalability. Subsequently, we examine the critical challenge of dynamically determining the branching point within these frameworks.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Reactive safety methods operate on the assumption that contingencies have already occurred, whereas Proactive methods anticipate unobserved future events. Table 1 summarizes these differences, emphasizing the factors that influence the choice between Reactive and Proactive approaches.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Safety vs. Conservatism The most critical trade-off lies between the strength of the safety guarantee and behavioral conservatism. Reactive methods offer strong, safety guarantees because they typically enforce invariance against the worst-case boundary of the control-invariant safe set (typically synthesized offline). However, this comes at the cost of high conservatism and sub-optimality. Once triggered, a Reactive planner treats every potential hazard as an immediate threat, typically forcing the AVs to behave abruptly. Additionally, by intervening only at the constraint boundary, these methods can induce control chattering---a high-frequency switching behavior that degrades passenger comfort and control smoothness. Proactive methods mitigate these issues by modeling future recourse---the ability to adapt in the future (birge2011introduction). By verifying safety for specific branches in a scenario tree, Proactive planners optimize a "shared trunk" trajectory in a receding horizon fashion. This look-ahead capability allows for smoother, more optimal maneuvers that defer the commitment to a specific mode until the branching time, leveraging online information to mitigate the sub-optimality of purely reactive interventions.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Computation vs. Scalability Reactive methods typically shift the complexity offline (e.g., synthesizing value functions or barrier certificates). This makes them highly scalable at runtime (e.g., QP or lookup), capable of filtering high-frequency control loops (e.g., $>100$ Hz). In contrast, Proactive methods address the complexity online. While this offers greater flexibility to handle changing environments, it introduces a bottleneck: the size of the scenario tree limits scalability. Handling dense traffic (e.g., with $>10$ interacting agents) typically requires heuristic pruning, which forces a trade-off between tractability and the risk of discarding critical scenarios.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Synthesis: The Hybrid Architecture This comparative analysis reinforces the "synergistic integration" outlined in Section 2.5. The high online computational cost and finite-horizon limitations of Proactive methods can be mitigated by imposing offline synthesized invariant sets as terminal constraints on scenario-tree branches. By anchoring short-horizon branches into provably safe invariant sets, the planner guarantees recursive feasibility without requiring a computationally prohibitive deep tree, thereby decoupling near-term strategic adaptation from long-term stability. Conversely, the conservatism inherent in Reactive methods is reduced by utilizing offline optimal control computation to synthesize high-performance safety critics. Tools such as HJ reachability, learning-based MPC, or differential dynamic programming fisac2019general; hsu2024safety synthesize safety value functions, yielding the least-conservative invariant sets for online execution. Furthermore, Reactive filters can serve as a runtime "safety net" for Proactive planners, intervening only when the planner's modeling assumptions (e.g., linearized dynamics or bounded disturbance margins) are violated.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Consequently, future robust architectures will likely layer these paradigms, utilizing a Proactive planner for low-frequency strategic guidance and a Reactive filter for high-frequency safety enforcement.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Reactive Approaches (Sec. 3) Proactive Approaches (Sec. 4) I. External Contingencies (Environmental & Interactive) Static Hazards & Geometry • Task-Preserving Filter (Minimally Invasive): strasser2024collision[ℱ] • Contingency MPC: hardy2010contingency; hardy2013contingency; tas2018decision; phiquepal2021control[𝒫], zheng2025safe[ℱ] • Robust Min-Max MPC: batkovic2021robust[ℱ] • Scenario-Tree MPC: Schildbach2015[𝒫] • Task-Preserving Filter (Switching): he2021rule[ℱ], leung2020infusing[ℱ] • Belief-Aware Shield: hu2024active; hu2023deception[𝒫] • Fail-Safe Supervision (MRC): Althoff2013; Magdici2016; Pek2021Failsafe; schurmann2017ensuring; Brudigam2023[ℱ] • Fail-Safe Supervision (Shared Control): Xue2022Override; Xue2023Shared[ℰ] •

<!-- chunk {"id": "body-0108", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

bajcsy2019efficient[ℱ] chen2021safe[ℱ] • Contingency MPC (Occlusion): nyberg2025hope; zheng2025safe; zheng2025occlusion[ℱ], zheng2025oacp[𝒫] • Game-Based Contingency: Zhan-RSS-21[ℱ]; qiu2024inferring[𝒫] • Learning-Based (Active): packer2023anyone[ℰ] Semantic & OOD Anomalies • Task-Preserving Filter (Latent Safety): seo2025uncertainty[𝒫] • Learning-Based (Foundation Models): sinha2024real; ganai2025real[𝒫] • Dynamic Branching (Deferred): elango2025deferred[𝒫] II.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Internal Contingencies (Ego-System Faults & Policy Failure) Sensor & Localization Failure (e.g., GNSS signal loss, LiDAR faults, Camera blindness) • Task-Preserving Filter (Minimally Invasive): singletary2022onboard[ℱ], • Task-Preserving Filter (Adaptive): yun2025atom[𝒫] • Task-Preserving Filter (Switching): laine2020eyesclosed[ℱ] • Fail-Safe Supervision (Fallback): Xue2019Virtual; Xue2018Fallback; jonasson2020[ℰ], chakraborty2025system; Viana2022[ℰ] • Fail-Safe Supervision (Formal Logic): Krook2019; krook2020formal[ℱ] • (Typically handled via reactive approaches rather than pre-planned branches) Actuation & Dynamics Faults (e.g., Tire blowouts, Electric motor malfunctions) • Task-Preserving Filter (Fault-Tolerant): zhang2025safe[ℱ] • Task-Preserving Filter (Model Reliability Monitor): fisac2019general[ℱ] • Fail-Safe Supervision (Control

<!-- chunk {"id": "body-0110", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Alloc.): yue2019automated; yu2019fallback; boudali2018emergency; khelladi2020emergency; duerr2020realtime; lodder2023optimization[ℰ], lee2022adaptive[ℱ] • Shared Control (Faults): li2023novel; li2020shared[ℰ] • Fail-Safe Supervision (System Redundancy): julitz2023computer[𝒫]; mercedesbenz2022; pechinger2020hardware[ℰ] • Contingency MPC (Friction): alsterda2019contingency; alsterda2021contingency[ℱ] Table 2: Classification of representative literature in contingency planning.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Relationships and Connections", "weight": 1.0} -->

Approaches are categorized by the nature of the contingency and the planning paradigm. Guarantee Key: ℱ = Formal/Robust Invariance; 𝒫 = Probabilistic/Stochastic; ℰ = Empirical/Heuristic.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Paradigm Suitability and Methodological Maturity", "weight": 1.0} -->

Beyond the theoretical trade-offs, the classification in Table 2 reveals distinct structural trends governed by the nature of the contingency. First, we observe a strong correlation between the contingency source and the preferred planning paradigm. Specifically, internal contingencies, such as actuator faults or sensor failures, are predominantly addressed via Reactive methods. This is attributable to the abrupt, binary nature of system faults; when a component fails, the immediate priority is stabilization or safe termination (i.e., reaching an MRC), a task well-suited to low-latency fail-safe supervision rather than strategic lookahead. Conversely, external contingencies involving interactive agents are increasingly addressed by Proactive branching methods. In these scenarios, uncertainty stems from the evolving intent of other agents. Proactive planning allows the AV to influence this evolution and maintain recourse, whereas the Reactive filter tends to induce "frozen" behavior by treating potential interactions as immediate worst-case hazards.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Paradigm Suitability and Methodological Maturity", "weight": 1.0} -->

Second, there is a clear methodological divergence regarding safety assurance, which fundamentally reflects the trade-off between the rigor of guarantees and the restrictiveness of modeling assumptions. Contingencies rooted in physical dynamics, whether kinematic hazards or interactive agents, are largely addressed by methods with formal guarantees $[\mathcal{F}]$ (e.g., invariant sets). However, these rigorous guarantees are predicated on strict, often idealized assumptions, such as bounded disturbance sets and perfectly known differential equations, which can be brittle in unstructured real-world environments.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Paradigm Suitability and Methodological Maturity", "weight": 1.0} -->

In contrast, contingencies rooted in semantic understanding and OOD anomalies (e.g., encountering unrecognized hazards (sinha2024real)) rely heavily on Empirical $[\mathcal{E}]$ or Probabilistic $[\mathcal{P}]$ approaches. While lacking formal proofs, these methods operate under more relaxed assumptions regarding environmental structure, facilitating easier transfer to open-world scenarios where strict error bounds are undefinable. This dichotomy highlights a critical "Verification Gap": while the field has developed rigorous formalisms to guarantee the vehicle will not violate physical constraints, these methods are predominantly state-based, relying on the assumption of bounded estimation errors.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Paradigm Suitability and Methodological Maturity", "weight": 1.0} -->

Recent advances in formal methods have attempted to extend verification to the perception stack. Notable frameworks like VerifAI (dreossi2019verifai) enable closed-loop verification of perception-driven systems, while specialized techniques have been developed to certify the robustness of neural classifiers (e.g., for traffic sign detection) (weng2018towards; shi2020robustness) and, more recently, 6D pose estimation (luo2025certifying). However, these rigorous guarantees are predominantly predicated on bounded perturbation models, typically limited to defined $L_{p}$-norm pixel noise, convex approximations of semantic perturbations, or constrained geometric transformations. Consequently, strict safety guarantees are typically lost when accounting for the potentially unbounded and semantically complex perception errors inherent in open-world OOD anomalies, where the magnitude of distribution shifts cannot be predefined.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Paradigm Suitability and Methodological Maturity", "weight": 1.0} -->

Thus, the field currently lacks equivalent formal frameworks to guarantee the correct interpretation of complex semantic scenarios, necessitating the future development of verified runtime monitors for learning-based components.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Dynamic Branching Point Determination", "weight": 1.0} -->

Determining when to branch is a central challenge in Proactive contingency planning, as it directly balances safety assurance against operational efficiency. Notably, this timing is equally critical for Reactive methods that rely on value function approximations synthesized from predictive control data (e.g., Learning-based MPC). Branching early reduces conservatism but introduces significant safety risks if critical uncertainty remains unresolved by the branching time. In contrast, branching late enhances robustness but typically results in excessive conservatism, as the vehicle must maintain a valid fallback for conflicting futures over an extended horizon. Theoretically, the branching time $t_{b}$ serves as a continuum connecting Reactive and Proactive safety paradigms. Branching immediately ($t_{b}\to 0$) reduces the formulation to standard Reactive control conditioned on the current logical mode, assuming total uncertainty resolution. Conversely, postponing branching indefinitely ($t_{b}\to\infty$) reduces the formulation into robust control form (i.e., accounting for all possible modes.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Dynamic Branching Point Determination", "weight": 1.0} -->

To mediate this trade-off, recent work has shifted toward adaptive strategies that dynamically determine the branching time based on real-time scene context and the level of prediction uncertainty.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Dynamic Branching Point Determination", "weight": 1.0} -->

Heuristic-based strategies offer computationally efficient solutions by triggering branches through interpretable indicators. One common class monitors spatial divergence across predicted trajectories. For instance, the MARC framework (li2023marc) identifies the latest time at which the ego vehicle's trajectories for different behavior modes remain within a predefined deviation threshold, defining a dynamic branching point from this "scene-level divergence." Another class leverages information-theoretic criteria to postpone decisions until predicted futures become statistically distinguishable. This concept was demonstrated by tas2018decision, and later refined by bouzidi2024motion, which used the Bhattacharyya distance to quantify the separation between scenario probability distributions. In the Bhattacharyya-based approach, the vehicle continues on a common path until the predicted outcome distributions diverge beyond a threshold, triggering a branch only once the futures are sufficiently distinct. While these heuristic triggers are lightweight and interpretable, they depend on carefully tuned threshold values, which may limit their robustness and generalizability across scenarios.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Dynamic Branching Point Determination", "weight": 1.0} -->

A more formal approach defines the branching point based on safety boundaries, focusing on the latest possible moment at which a decision can be made without compromising future safety. This is typically achieved through reachability analysis, which computes the maximum decision latency, the last moment at which the shared trunk trajectory still allows a safe and feasible continuation for all possible future scenarios (bouzidi2025reachability). Theoretically, this reachability-based boundary corresponds to the edge of the robust maximal control-invariant set (accounting for all logical modes), defining the state space region where the system retains valid recourse against the worst-case realization of uncertainty. While providing strong safety guarantees, this approach can be conservative as it is based on worst-case feasibility. To operate more efficiently within this safe window, elango2025deferred cast the branching point itself as a decision variable within trajectory optimization. A key contribution in this direction is Deferred-Decision Trajectory Optimization, which jointly optimizes both the continuous trajectory and the discrete branching time. This allows the planner to "wait and see," dynamically committing to a branch only when informative cues appear.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Dynamic Branching Point Determination", "weight": 1.0} -->

By integrating uncertainty-aware cost terms that implicitly model the value of information, these formulations quantify the benefit of delayed decision-making while maintaining robustness.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Dynamic Branching Point Determination", "weight": 1.0} -->

Despite these advances, key challenges remain. The computational complexity of optimizing over dynamically branching scenario trees hinders real-time deployment, especially in dense, multi-agent settings. Furthermore, these methods rely heavily on the accuracy and calibrated uncertainty of upstream prediction modules. Promising future directions lie in hybrid frameworks that use formal reachability analysis to define a certified safe decision window, within which advanced optimization or learning-based planners can flexibly determine the optimal time to branch. This hybrid approach enables a principled trade-off between safety, efficiency, and scalability in dynamic environments.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Summary and Future Prospects", "weight": 1.0} -->

In this paper, we presented contingency planning as a cornerstone for the safe and reliable deployment of high-autonomy, safety-critical AVs. This capability is essential for managing multimodal uncertainty while maintaining operational safety. We introduced a logic-conditioned problem formulation and a comprehensive taxonomy of contingency planning approaches, categorizing existing methods into Reactive safety paradigms and Proactive safety paradigms. For each class, we discussed foundational concepts, representative algorithms, safety guarantees, and deployment challenges. Table 2 provides a comprehensive classification of the literature reviewed in this survey. Complementing this taxonomy, Table 1 synthesizes the trade-offs between paradigms regarding safety guarantees, behavioral conservatism, computational complexity, scalability, and adaptivity.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Summary and Future Prospects", "weight": 1.0} -->

Across these methodologies, a common goal emerges: enabling safe decision making under uncertainty---the ability of AVs to respond robustly to rare and unpredictable situations while preserving natural and efficient driving behavior. Strategies vary significantly: some emphasize pre-validated fallback trajectories as safety filters, while others adopt scenario branching and dynamic replanning. Recent methods increasingly leverage learning-based prediction and planning to enhance behavioral richness. Despite their diversity, the field is converging toward hybrid solutions that combine multiple paradigms to overcome individual limitations.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Summary and Future Prospects", "weight": 1.0} -->

However, bridging the gap between formal safety guarantees and real-world robustness remains a core challenge. We conclude by identifying critical areas that currently limit the practical deployment of contingency planning methods.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Robust and Scalable Modeling", "weight": 1.0} -->

A critical challenge lies in building models that are both robust and scalable across diverse driving scenarios. Many existing planners depend on simplified dynamics, such as kinematic bicycle or point-mass models, which typically overlook important physical phenomena like roll, pitch, terrain interaction, or actuator degradation. These low-fidelity approximations reduce robustness, especially in unstructured environments or under fault conditions where accurate modeling is crucial for safe fallback behavior.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Robust and Scalable Modeling", "weight": 1.0} -->

To ensure formal safety guarantees, many methods assume strict structural priors. Specifically, control-theoretic approaches often assume control-affine structures to enable convex synthesis (e.g., QP-based CBFs), while reachability analysis relies on Lipschitz continuity (smooth dynamics) to bound tracking errors. Additionally, learning-based certificates typically assume representative offline datasets (i.i.d. distributions) and bounded uncertainty to derive statistical guarantees. These assumptions typically fail in complex, high-dimensional scenarios, such as deformable terrain or adversarial traffic. A promising direction involves detecting modeling errors and combining physics-informed priors with real-time data-driven adaptation. Emerging techniques, such as online system identification, neural differential equations, and latent state abstractions, enable planners to adapt to environmental variability while retaining physical interpretability. Although higher-fidelity models can be computationally demanding, methods like model-order reduction and accelerated simulation help mitigate this cost.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Robust and Scalable Modeling", "weight": 1.0} -->

Complementing system-level modeling is necessary to manage uncertainty from upstream modules, particularly perception and prediction. Many planners assume reliable maps, accurate intent estimation, and calibrated forecasting of other agents. In open-world deployments, these white-box assumptions are typically violated. While black-box methods (e.g., scenario sampling) attempt to circumvent these modeling errors by relying on data-driven distributions, they trade the "validity gap" for a "coverage gap," suffering from sample inefficiency and the inability to guarantee safety against rare, unobserved events (corso2021survey).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Robust and Scalable Modeling", "weight": 1.0} -->

To address this gap, robust planners are increasingly adopting learned world models and calibrated uncertainty estimates while actively monitoring assumption violations. Effective strategies include: (i) detecting distribution shifts and adjusting branching strategies accordingly (sinha2024real; ganai2025real); (ii) embedding intent uncertainty diagnostics to guide belief updates and information-seeking actions (mustafa2024racp; liu2024reasoning); and (iii) utilizing confidence-based triggers to activate conservative fallback policies (seo2025uncertainty), leveraging conformal prediction to enforce distribution-free probabilistic safety guarantees during these transitions (lindemann2025formal). These mechanisms reduce the brittleness of high-level assumptions without defaulting to overly pessimistic, worst-case designs.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Synthesis of Invariant Sets for Scalable Learning-Based Safety", "weight": 1.0} -->

Control-invariant sets define regions of the state space where safety-preserving controls are guaranteed to exist. They form the foundation for fallback policy design and are essential for establishing asymptotic safety guarantees in learning-based systems. In this context, invariant sets are not auxiliary tools but fundamental building blocks for scalable and verifiable safety synthesis in high-dimensional, partially known, or data-driven environments.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Synthesis of Invariant Sets for Scalable Learning-Based Safety", "weight": 1.0} -->

A major challenge is synthesizing such sets under relaxed assumptions, where complete model knowledge, low dimensionality, or tractable dynamics can no longer be assumed. This challenge is especially significant for high-dimensional AVs under uncertain terrains or multi-agent human-robot interactions. Classical tools like reachability analysis or convex optimization typically face scalability limitations in these contexts.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Synthesis of Invariant Sets for Scalable Learning-Based Safety", "weight": 1.0} -->

Recent work investigates implicit safety representations, such as value functions or neural approximators, which trade formal guarantees for greater flexibility (seo2025uncertainty; bansal2021deepreach). In particular, latent value representations, learned through neural ODEs, encoder--decoder architectures, or contrastive objectives, offer compact abstractions that support policy generalization in complex, partially observable domains.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Synthesis of Invariant Sets for Scalable Learning-Based Safety", "weight": 1.0} -->

Complementing these value-based approaches, conditional generative modeling frameworks (e.g., diffusion models, flow-matching networks) offer a novel paradigm for implicitly characterizing high-dimensional safe manifolds through sampling. Rather than constructing geometric boundaries, these methods integrate CBFs or safety constraints directly into the generative vector fields or denoising processes (dai2025safe; huang2025sad; xiao2025safediffuser). By aligning the generative flow with invariance conditions, this approach transforms the safety synthesis problem from geometric computation to constrained distribution learning. This yields a potent generative safety prior capable of efficient sampling in high-dimensional spaces, providing the necessary mathematical foundation for the runtime execution.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Runtime Safety Assurance: From Abstraction to Execution", "weight": 1.0} -->

Achieving scalable and generalizable safety guarantees remains one of the central challenges in contingency planning. While the synthesis methods discussed above provide theoretical safety envelopes (e.g., neural value functions or generative manifolds), deploying these abstractions under real-world uncertainty introduces a distinct verification gap. Although risk-constrained formulations can enforce local invariance, extending these guarantees to long-horizon multimodal tasks under perception uncertainty is nontrivial.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Runtime Safety Assurance: From Abstraction to Execution", "weight": 1.0} -->

The core difficulty lies in translating formal safety abstractions into runtime mechanisms that remain effective despite perception noise, sensor latency, or uncertainty in human interactions. AVs operate in highly dynamic environments where failures in perception or actuators can be difficult to detect and mitigate. Therefore, runtime monitors must operate at frequencies significantly higher than the main planning stack ($>100$ Hz) to identify these faults and intervene before they propagate to unsafe states. Even when failures are detected, planners may not have sufficient time to replan a safe trajectory under degraded information conditions (chakraborty2025system).

<!-- chunk {"id": "body-0136", "role": "body", "section": "Runtime Safety Assurance: From Abstraction to Execution", "weight": 1.0} -->

One promising direction is to use context-conditioned control-invariant sets, where the safe region adapts dynamically to latent environmental factors (seo2025uncertainty; oh2025safety), through a dual-role mechanism for both real-time monitoring and fallback planning. As runtime monitors, they utilize the learned implicit representations (e.g., value functions $V(x)$ or diffusion likelihoods) to track proximity to constraint boundaries and trigger corrective actions when violations are imminent. As planning primitives, they define verifiable terminal regions that support adaptive, certifiable contingency trajectories. Integrating these dual roles within hybrid architectures, linking design-time synthesis, runtime monitoring, and fallback control, builds a continuous pipeline from modeling to execution, forming the basis for verifiable safety assurance.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Socially-Aware and Ethical Contingency Planning", "weight": 1.0} -->

Beyond physical safety, contingency planning must also account for the social and ethical dimensions of autonomous driving. AVs operate in highly interactive environments, where decisions depend on interpreting human intent, complying with traffic standards, and maintaining mutual predictability (krugel2024risk). Effective planners must reason about behavioral context to ensure that actions are interpretable and acceptable to surrounding road users.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Socially-Aware and Ethical Contingency Planning", "weight": 1.0} -->

Embedding ethical reasoning introduces new challenges. Real-world driving presents moral trade-offs, such as balancing risk among participants or minimizing unavoidable harm, that require formalization into tractable specifications (evans2020ethical). Recent research has explored symbolic logic constraints, socially compliant utility functions, and multi-objective decision frameworks to encode principles of fairness, courtesy, and harm minimization. Fundamentally, these considerations reshape how safety specifications are defined, transforming them from rigid hard constraints into prioritized objectives. Unlike the fixed state constraints assumed in the standard hybrid framework reviewed in this survey, ethical reasoning often necessitates solving hierarchical optimization problems over conflicting specifications (e.g., prioritizing preserving life over adhering to traffic rules). Consequently, while the core Reactive and Proactive paradigms remain applicable as the foundational execution layer, ethical contingency planners should be viewed as advanced decision modules built on top of these methodologies, dynamically modulating constraints to satisfy complex social contracts.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Socially-Aware and Ethical Contingency Planning", "weight": 1.0} -->

Ultimately, ethically aligned contingency planning aims to connect formal safety guarantees with societal expectations. Realizing this goal requires not only reliable and adaptive planning but also transparency and fairness across cultural and situational contexts. This represents a key frontier in building socially compatible and trustworthy autonomous systems.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Standardized Benchmarking and Evaluation", "weight": 1.0} -->

To transition contingency planning from theoretical formulations to deployable systems, the community must adopt standardized benchmarking that moves beyond ad-hoc simulations. Critically, the choice of evaluation platform must be dictated by the nature of the contingency.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Standardized Benchmarking and Evaluation", "weight": 1.0} -->

Platform Selection by Contingency Type For contingencies involving fundamental kinematic limits and rule compliance, benchmarks must provide explicit analytical models (e.g., white-box dynamics) to rigorously validate constraint satisfaction. Platforms such as CommonRoad (althoff2017commonroad) provide standardized, composable scenarios ideal for assessing the feasibility and conservatism of Reactive filters without the confounding variables of perception noise. Conversely, contingencies stemming from intent uncertainty require data-driven evaluation. Log-replay platforms like Waymax (gulino2023waymax) and nuPlan (caesar2021nuplan) offer large-scale, real-world trajectory data, which is essential for validating whether Proactive branching strategies can robustly handle realistic human unpredictability. Finally, for "zero-order" observability failures or vehicle dynamics faults, high-fidelity physics engines are necessary. CARLA (dosovitskiy2017carla), supported by Unreal Engine physics, allows for the injection of raw sensor noise and mechanical degradation, enabling the evaluation of empirical fail-safe triggers against photorealistic distribution shifts.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Standardized Benchmarking and Evaluation", "weight": 1.0} -->

A Hierarchy of Standardized Metrics Standard safety metrics, such as collision rate, are insufficient for evaluating contingency planners, as catastrophic failures are rare by definition. To rigorously dissect performance, evaluation must prioritize worst-case safety margins. Rather than reporting abstract value functions $V(x)$ that vary across methods, it is ideal for benchmarks to additionally report the minimum physical signed distance to the failure set boundary during critical events.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Standardized Benchmarking and Evaluation", "weight": 1.0} -->

Complementing this, the cost of conservatism can be assessed by measuring the performance degradation (e.g., velocity loss) relative to a non-contingency oracle in nominal scenarios. For Proactive planners, we recommend reporting the branch realization ratio---the proportion of planned contingency maneuvers that are actually executed. This metric helps distinguish between prudent anticipation and excessive caution, avoiding the pitfall of penalizing planners for hedging against risks that do not materialize. Conversely, the intrusiveness of Reactive filters is often captured via intervention frequency and induced jerk, ensuring that safety enforcement does not destabilize the vehicle or degrade passenger comfort. Finally, for fail-safe supervision, a critical metric involves the time-to-MRC, quantifying the system's latency in transitioning from a fault injection to a verified safe state.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Standardized Benchmarking and Evaluation", "weight": 1.0} -->

Synthesizing these disparate indicators, ranging from formal safety bounds to empirical comfort measures, into a unified evaluation framework remains a significant open challenge. Simply aggregating them into a scalar score risks obscuring critical nuances. A more rigorous path forward may lie in characterizing the Pareto frontier between safety guarantees (e.g., distance to failure) and operational efficiency (e.g., branch realization). Ultimately, establishing this multi-faceted metric suite serves as a necessary precursor to rigorous cross-paradigm comparison and certification.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Declaration of Generative AI and AI-assisted technologies in the manuscript preparation process", "weight": 1.0} -->

During the preparation of this work the author(s) used Google's Gemini in order to improve the language and readability of the manuscript. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.
