<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Multi-agent Motion Planning under Uncertainty for Drones Using Filtered Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of safe multi-agent motion planning for drones in uncertain, cluttered workspaces. For this problem, we present a tractable motion planner that builds upon the strengths of reinforcement learning and constrained-control-based trajectory planning. First, we use single-agent reinforcement learning to learn motion plans from data that reach the target but may not be collision-free. Next, we use a convex optimization, chance constraints, and set-based methods for constrained control to ensure safety, despite the uncertainty in the workspace, agent motion, and sensing. The proposed approach can handle state and control constraints on the agents, and enforce collision avoidance among themselves and with static obstacles in the workspace with high probability. The proposed approach yields a safe, real-time implementable, multi-agent motion planner that is simpler to train than methods based solely on learning. Numerical simulations and experiments show the efficacy of the approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-agent motion planning in cluttered workspaces under stochastic uncertainty arising from both perception and actuation is a key challenge in designing reliable autonomous systems. The need for such planners, especially for quadrotors, arises in a variety of application areas including transportation, logistics, monitoring, and agriculture. Recently, motion planning using reinforcement learning (RL) has gained attention, due to its ability to leverage data to tackle generic dynamical systems and complex task specifications. A major challenge for such efforts is the lack of safety guarantees, since most of the existing RL-based approaches enforce safety constraints by soft constraints and are subject to training errors. Additionally, multi-agent RL is known to suffer from non-stationarity and scalability issues, which may prevent the training to converge. We propose *a tractable approach to safe, multi-agent motion planning in stochastic, cluttered workspaces that combines reinforcement learning and set-based methods for constrained control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach yields a safe, real-time implementable, multi-agent motion planner that is simple to train and enforces safety with high probability, by means of chance constraints.* Figure 1: Existing reinforcement learning-based motion planners can generate unsafe trajectories (yellow arrows), since they treat safety as soft constraints, which is undesirable in safety-critical applications. We propose a constrained-control-based safety filter that renders such motion planners safe (long green arrows) by enforcing safety as hard constraints. See for an overview and videos of the experiments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the deterministic setting, various approaches have been proposed for multi-agent motion planning such as centralized scheduling and coordination, roadmap and discrete search followed by trajectory refinement, sampling-based rapidly-exploring random trees, adaptive roadmaps, buffered Voronoi cells, mixed-integer programming, sequential convex programming, formal methods and finite transition systems, and control barrier functions. Recently, RL-based planners have been used in complex environments. A key advantage of learning-based planners is the ability to leverage past experience in future decision making. Consequently, such planners can tackle *complex* and *high-dimensional* motion planning tasks, while incorporating prior information about the planning task and accommodating uncertainty.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our preliminary work considered *deterministic* safe multi-agent motion planning, where everything was known exactly. We proposed a two-step approach where a single-agent RL algorithm provided a *reference* command which was subsequently *filtered* (or corrected) by a constrained control module. The works closest to are that also follow a similar two-step process. However, need labelled data for supervised learning, and use multi-agent RL. Multi-agent RL trains multiple agents to collectively complete the task, and as a consequence, is harder to train than single-agent RL. Additionally, relies on solving a two-player game in problems with discrete state and action space. Our approach utilizes single-agent RL that is simpler to train, can accommodate continuous state and action spaces for stabilizable linear dynamics, is real-time implementable, and need not be retrained as the number of agents increase.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the stochastic setting, the presence of probabilistic constraints makes the motion planning problem more challenging. Here, we must balance the conservativeness of the motion plans with the risk (the probability of violation of a desirable property), while ensuring the existence of a solution that satisfies other problem objectives. The authors of propose single-agent motion planners using chance constrained programming, but these approaches may become prohibitively expensive when extended to multi-agent systems. combined artificial potential fields with stochastic reachability theory to generate motion plans for a single-agent in stochastic, cluttered workspaces. Recently, proposed using a *reference* controller, such as an RL controller trained offline, followed by a constrained-control-based online filtering step to guarantee safety of the control action being applied to the system, which was applied to autonomous racing. However, to the best of our knowledge, these works do not consider a multi-agent setup. Another line of research for multi-agent motion planning in stochastic settings uses buffered Voronoi cells, where motion plans are restricted to safety sets computed based on the "best" separating hyperplane between two Gaussian distributions, further tightened by a safety buffer.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such an approach couples planning and safety control, yet it does not guarantee recursive feasibility.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on safe multi-agent motion planning in applications where a *centralized* decision maker coordinates the actions of the agents for safety and performance. Examples of such applications include air traffic control and coordinated traffic control centers. The proposed centralized approach may impose additional communication and computational burden when compared to a decentralized method (for e.g., ). However, the ability to enforce coordination helps the proposed approach typically generate safer and more efficient trajectories for the overall system.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions of this work: Since RL has been recently of interest to the robotics community, we propose a solution to address the lack of safety in RL-based planners, specifically in multi-agent motion planning settings. We propose an optimization-based safety filter that, when used in conjunction with RL, provides a safe, multi-agent motion planner in cluttered workspaces under stochastic uncertainty. The proposed safety filter uses convex optimization and set-based control to compute minimum-norm corrections to the RL-based motion plan and guarantee probabilistic collective safety of the multi-agent system. We use single-agent RL to learn from data, while avoiding issues like non-stationarity and scalability that affect multi-agent RL. We also describe how to design terminal state constraints for the constrained-control-based safety filter by using reachability to achieve recursive feasibility. Finally, we demonstrate our approach by both numerical simulations and experiments using quadrotors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We note that while the proposed solution is discussed in the context of RL, our approach is general and can be used with another planner instead of RL. For instance, the single-agent planner could be sampling-based (e.g. RRT-based planners ), and the advantage of our architecture would be in the dimensionality reduction and reduced effort for collision checking with respect to applying the sampling-based planner to the full multi-agent problem.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relationship with our preliminary work: In, we proposed a safe, multi-agent motion planner using reinforcement learning and optimization for deterministic dynamics and a known workspace. We generated continuous-time safety guarantees under the assumption that the safety filter's control input is constant across the entire horizon of the safety filter. In this work, we extend our preliminary work to stochastic workspace, dynamics, and sensing, and provide probabilistic safety guarantees for the overall system without relying on the constant control input assumptions. We also explicitly assess recursive feasibility of the safety filter, and investigate the importance of the RL controller, safety filter, and the terminal constraints in the proposed approach using extensive hardware and simulation experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

$0_{d}$ ($0_{n,m}$) is a vector (matrix) of zeros in ${\mathbb{R}}^{d}$ (${\mathbb{R}}^{d \times m}$), $I_{d}$ is the $d$-dimensional identity matrix, and ${\mathbb{N}}_{\lbrack a,b\rbrack}$ is the subset of natural numbers between (and including) ${a,b} \in {\mathbb{N}}$, $a \leq b$, and ${\mathbb{N}}_{\lbrack a,b\rbrack} = \varnothing$ when $a > b$. $\oplus, \ominus$ are the Minkowski sum and Pontyagrin difference, respectively, and $\parallel \cdot \parallel$ is the 2-norm of a vector.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

We denote random vectors in bold ${\mathbf{x}}:{\Omega\rightarrow{\mathbb{R}}^{n}}$ and their mean $\overline{x} \triangleq {{\mathbb{E}}{\lbrack{\mathbf{x}}\rbrack}}$, where $\mathbb{E}$ is the expectation operator with respect to $\mathbb{P}$. We use $\hat{x}$ to denote a realization of a random vector $\mathbf{x}$. We use $\mathcal{N}{(\mu,\Sigma)}$ to denote a Gaussian random vector with mean $\mu$ and covariance $\Sigma$, and refer to $\mathcal{N}{(0_{n},I_{n})}$ as the standard Gaussian random vector. For a vector ${\mathbf{v}}{(t)}$, ${\mathbf{v}}{(\left.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

k \middle| t \right.)}$ is the predicted value at $k \geq t$ based on the information available at time $t$, and we denote ${{\mathbf{v}}{(\left. t \middle| t \right.)}} = {{\mathbf{v}}{(t)}}$. We use the same notation when referring to the distribution of ${\mathbf{v}}{(t)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

The following abbreviations are used throughout the paper: iid (independent and identically distributed), MPC (model predictive control), QP (quadratic program), and PSD (positive semidefinite).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The input set $\mathcal{U}$ is a convex and compact polytope, and the process noise is iid, zero-mean Gaussian ${\mathbf{w}}_{i} \sim \mathcal{N}{(0_{n},\Sigma_{w}}$) for some known PSD matrix $\Sigma_{w} \in {\mathbb{R}}^{n \times n}$. The position of the agent $i$ at time $t$ is given, for some $C \in {\mathbb{R}}^{d \times n}$, $d < m$. For $k \geq t$, the mean state of the agents is predicted according to the nominal dynamics, We assume that the nominal dynamics are stabilizable, i.e., there exists a stabilizing gain matrix $K \in {\mathbb{R}}^{m \times n}$ that ensures that all eigenvalues of $({A + {BK}})$ lie in the unit circle.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Measurement model: We assume that the initial state of each agent ${{\mathbf{x}}_{i}{}} = {x_{i}{}}$ is known, i.e., deterministic. However, for $t > 0$, we have access only to a noisy measurement of the true state ${\mathbf{x}}_{i}{(t)}$. Specifically, we assume that the measurements ${\hat{y}}_{i}{(t)}$ are a realization of a random vector ${\mathbf{y}}{(t)}$, where ${\mathbf{η}}_{i} \sim \mathcal{N}{(0_{n},\Sigma_{\eta}}$) is a zero-mean Gaussian noise with a known PSD matrix $\Sigma_{\eta} \in {\mathbb{R}}^{n \times n}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Agent Representation: We consider agents with identical convex and compact rigid bodies, denoted by $\mathcal{A} \subset {\mathbb{R}}^{d}$, such that $0_{d} \in \mathcal{A}$. The rigid bodies of the agents are rotation-invariant. So, we only consider translations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We can generalize all the presented results to account for heterogeneous agents with heterogeneous linear dynamics, measurement models, and rigid bodies. We consider homogeneity in all of these aspects to simplify the presentation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Workspace Representation: We represent the workspace using a convex and compact polytope $\mathcal{K} \subset {\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Obstacle Representation: The workspace has $N_{O}$ static obstacles, each with a convex and compact rigid body $\mathcal{O}_{j} \subset {\mathbb{R}}^{d}$ and $0_{d} \in \mathcal{O}_{j}$ ($j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$). The obstacle shapes are known *a priori*, but their positions are available only via a noisy measurement.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Safe multi-agent motion planning under uncertainty", "weight": 1.0} -->

Given target positions $q_{i} \in {\mathbb{R}}^{d}$, we want to design a motion planner that drives the agents towards their respective target positions, while ensuring safety of the agents at all times, despite the uncertainty in the dynamics and the noisy estimates of the agent and obstacle positions. Here, we formalize the required features of safety in the multi-agent motion planning problem by introducing the notion of *probabilistic collective safety*, inspired by existing literature.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem 1 (Safe Multi-Agent Planning)", "weight": 1.0} -->

Given user-specified risk bounds $\alpha_{i,j,t},\beta_{i,i',t},\kappa_{i,t}$, for every ${i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}},{{i' \in {\mathbb{N}}_{\lbrack 1,{i - 1}\rbrack}},{j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}}}$ and $t \in {\mathbb{N}}$, design a multi-agent motion planner that navigates the agents with dynamics to their respective targets such that the agents are probabilistically collectively safe at all times $t$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem 1 (Safe Multi-Agent Planning)", "weight": 1.0} -->

In the statement of Problem 1. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"), we specified a risk bound for every time step ($\alpha_{i,j,t},\beta_{i,i',t},\kappa_{i,t}$). On the other hand, when a risk bound for the entire planned trajectory (e.g. $\alpha_{i,j}$) is given over a planning horizon $T \in {\mathbb{N}}$, one can arrive at $\alpha_{i,j,t}$ via *risk allocation* --- divide the risk equally across time steps with $\alpha_{i,j,t} = {\alpha_{i,j}/T}$ for every $t \in {\mathbb{N}}_{\lbrack 1,T\rbrack}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Proposed Solution", "weight": 1.0} -->

We solve Problem 1. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") by the following two steps.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Proposed Solution", "weight": 1.0} -->

*RL training (Offline):* We train a neural network to drive a *single* agent with *nominal* (deterministic) dynamics from any initial state in the workspace to a final desired state. The resulting policy learns to perform static obstacle collision avoidance and remain within the workspace while transferring a single agent from its initial state to the final state.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Proposed Solution", "weight": 1.0} -->

*Safety Filter (Online):* We use a constrained-control-based safety filter that uses an online evaluation of the RL-based motion planner. The safety filter suitably modifies the motion plan to enforce probabilistic collective safety at all time steps. The safety filter solves a real-time implementable, convex, quadratic program to determine the modifications.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

We design a RL-based motion planner that drives the agent with nominal dynamics to a specified target position $q \in {\mathbb{R}}^{d}$ in presence of $N_{O}$ static obstacles located at nominal positions ${{\overline{c}}_{j}{\forall j}} \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$. Here, we train a *single-agent RL-based* planner in an environment devoid of other agents. After briefly discussing the motivations for such an approximation, we set up the Markov decision process used for training and characterize the neural policy obtained via single-agent RL training.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

The advantage of using a single-agent RL-based planner instead of the full multi-agent RL-based planner is in the ease of training. Specifically, a single-agent RL-based planner avoids some issues of multi-agent RL such as non-stationarity, scalability, and the diminished ability to accommodate potential changes in team size post training. Recall that in multi-agent RL, all agents learn concurrently and thus an action taken by an individual agent affects both the reward of the other agents and the evolution of the state of the system. From the agent's perspective the environment is non-stationary. By approximating the problem and eliminating the other agents, training a single-agent RL is a stationary problem which is key for convergence results of RL training and for the reduced training effort. Moreover, compared to multi-agent RL training, whose joint state space and joint action space grow rapidly in dimension with the number of agents, the state space and the action space dimensions are fixed and independent of the team size in the single-agent RL training.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

Finally, if the team size changes post training, the proposed single-agent RL-based planner in Figure 2 can still be used without any modifications as compared to a complete multi-agent RL-based planner, which may require re-training to handle changes in the team size.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

Consider a feedforward-feedback controller $\pi:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{m}}$ with where $K$ is a stabilizing gain matrix, $F \in {\mathbb{R}}^{m \times d}$ provides closed loop unitary gain with the nominal dynamics, i.e., ${C{({I - {({A + {BK}})}})}^{- 1}BF} = I_{d}$, and $r \in {\mathbb{R}}^{d}$ is the reference position command. We obtain the following stabilized, nominal, prediction model for the agent at any time $k \geq t$, by closing the loop of the dynamics with the controller. For the measurement model, the predicted measurements are ${\hat{y}{(\left. k \middle| t \right.)}} = {\overline{x}{(\left.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

k \middle| t \right.)}}$ for every $k \geq t$. By construction, the mean predicted position ${\overline{p}{(\left. k \middle| t \right.)}}\rightarrow r$ as $k\rightarrow\infty$ for a constant reference command ${r{(\left. k \middle| t \right.)}} = r$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

We use the following Markov decision process for training: *Observation space*: We define the observation vector $o \in {\mathbb{R}}^{n + d + {N_{O}d}}$ as the concatenated vector containing the current measurement of the agent $\hat{y} \in {\mathbb{R}}^{n}$, the displacement of the agent's current measured position to the target ${({p - q})} \in {\mathbb{R}}^{d}$ and to the $N_{O}$ static obstacles ${({p - {\overline{c}}_{j}})} \in {\mathbb{R}}^{d}$, for all $j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$, where $p = {C\hat{y}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

*Action space*: The action $a \in \mathcal{A} \subset {\mathbb{R}}^{d}$ determines the reference position as a perturbation $a$ to the target $q$, $r = {q + a}$. The set $\mathcal{A}$ is compact.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

*Step function*: The next predicted measurement${\hat{y}{({t + \left. 1 \middle| t \right.})}} = {\overline{x}{({t + \left. 1 \middle| t \right.})}}$ is given.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

*Reward function*: The instantaneous reward function is with reward parameters ${\zeta_{\text{obs}},\zeta_{\text{tgt}}} \leq 0$ and $\gamma_{j} \geq 0$. Here, $\gamma_{j}$ is the radius of the smallest volume ball that covers the set $\mathcal{O}_{j} \oplus {({- \mathcal{A}})}$ for each $j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$. We terminate an episode when the agent either reaches the target or violates the *nominal single-agent* safety conditions, namely the static obstacle avoidance and keep-in constraints.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

These constraint violations are given: When the episode terminates, we add a terminal reward or penalty as follows: with $o_{\infty}$ and $p_{\infty}$ denoting as the observation and position vectors upon termination respectively, $R_{\text{target}} \geq 0$, and ${P_{\text{keep-in}},P_{\text{obstacle}}} \leq 0$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A Reinforcement learning-based single-agent motion planner", "weight": 1.0} -->

We have set up the Markov decision process to consider deterministic nominal dynamics instead of the original stochastic dynamics in order to simplify the RL training. Our numerical and hardware experiments show that the restriction to deterministic nominal dynamics does not affect the proposed solution severely.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Our approach can also accommodate a known, time-varying target and biased measurement models $\overline{\mathbf{η}} \neq 0$. We have considered a time-invariant target $q$ and an unbiased measurement model here to simplify the presentation. Additionally, we use the minimum volume balls with radius $\gamma_{j}$ in instead of $\mathcal{O}_{j} \oplus {({- \mathcal{A}})}$ to simplify the collision detection while training the RL-based motion planner.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Upon completion of training, most of the existing RL algorithms return a policy $\nu:{{\mathbb{R}}^{n + d + {N_{O}d}}\rightarrow\mathcal{A}}$ that provides the action to apply given an observation vector, e.g., by a neural network. Additionally, we can "rollout" the policy network $\nu$ to obtain a trajectory based on the RL motion planner for a planning horizon $T \in {\mathbb{N}}$. Consider any agent $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$ that starts with the measurement ${\hat{y}}_{i}{(t)}$. We compute the RL motion plan ${\{{x_{i}^{\text{RL}}{(\left.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2", "weight": 1.0} -->

1 \middle| t \right.})}$ using and the corresponding predicted observation vector $o_{i}{({k + \left. 1 \middle| t \right.})}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The generated motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$ does not satisfy probabilistic collective safety, since RL cannot guarantee collision-free trajectories (it only penalizes collisions and is subject to training errors), and the generated RL motion plan completely ignores inter-agent collision avoidance and the effect of the process and measurement noises.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Safety Filter", "weight": 1.0} -->

We now generate corrections to the RL-based motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$ using a constrained-control-based safety filter that ensures the satisfaction of probabilistic collective safety at all times. Consider the following optimization problem with the stochastic information, where ${U_{i}^{s}{(t)}} = {\{{u_{i}^{safe}{(\left.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Safety Filter", "weight": 1.0} -->

k \middle| t \right.)}$ The safety filter takes the RL control sequence ${\{{u_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ that is generated using the RL-based single-agent motion planner, and computes safe control inputs ${\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ within the control set (12d) that minimally deviate from the corresponding RL control inputs (12a), while enforcing probabilistic collective safety constraints (12e). The constraint (12c) defines the distribution of the noisy current state ${\mathbf{x}}{(\left. t \middle| t \right.)}$ from the current measurement $\hat{y}{(t)}$ and the measurement model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Safety Filter", "weight": 1.0} -->

Additionally, to avoid computing control actions $u_{i}^{\text{safe}}$ that may render the optimization problem in the safety filter infeasible in the future, we include terminal state constraints (12f) that, when designed as explained later, provide recursive feasibility. Only the first safe control $u_{i}^{\text{safe}}{(\left. t \middle| t \right.)}$ is applied for each agent $i$, and then is solved again at time $t + 1$ in an MPC-like fashion.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Safety Filter", "weight": 1.0} -->

The safety filter is a nonlinear, non-convex, and stochastic optimization problem due to (12e) and (12f), and as a consequence in general not real-time implementable. Therefore, we reformulate by convexifying the constraints and replacing the chance constraints by deterministic risk-tightened constraints, which we describe next.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C Convexified constraints for probabilistic collective safety", "weight": 1.0} -->

We now present a convex, deterministic reformulation of (12e) that relies on well-known properties of Gaussian random vectors and the generated motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-D Ensuring recursive feasibility using reachability", "weight": 1.0} -->

We now turn our attention to (12f) that is designed to ensure that remains feasible in subsequent control time steps. For recursive feasibility (12f), we enforce the existence of a terminal set and a control ${u_{i}^{\text{recurse}}{(k)}} \in \mathcal{U}$ for all $k \geq {t + T}$ for each agent $i$ such that the following constraints hold for all $k \geq {t + T}$, where $\delta \in {}$ is a (small) user-specified risk threshold.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-D Ensuring recursive feasibility using reachability", "weight": 1.0} -->

Existing literature in constrained control typically enforces recursive feasibility using control invariant or positive invariant sets. However, characterization of such sets can be challenging in our setting due to the inherent non-convexity of the probabilistic collective safety constraints. Alternatively, one can approximately enforce these constraints by truncating the recursive feasibility criterion to a finite but long horizon, and then utilizing stochastic reachability.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-D Ensuring recursive feasibility using reachability", "weight": 1.0} -->

For the sake of tractability, we enforce approximately by imposing chance constraints on the terminal states, while ignoring the stochasticity in the future time steps. We characterize these constraints using appropriately defined *avoid sets* (also known as *inevitable collision states* or *capture sets* ) and *viability sets* (also known as *controlled invariant sets*).

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-E Reformulated Risk-Tightened MPC Safety Filter", "weight": 1.0} -->

Following the reformulations discussed in Sections III-C and III-D, we obtain a quadratic program, where ${U_{i}^{s}{(t)}} = {\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ for each $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$. uses the mean states and positions of the agents, and the deterministic linear constraints characterized in Propositions 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") for probabilistic collective safety and recursive feasibility. A solution of is a feasible (but not necessarily optimal) solution of.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-E Reformulated Risk-Tightened MPC Safety Filter", "weight": 1.0} -->

From the setting of, it is evident that the specialization of the RL-based motion planner to the deterministic nominal dynamics does not affect the proposed solution adversely. Motivated by the superposition principle, we have used a simpler RL-based motion planner that considers deterministic dynamics instead of the stochastic dynamics, and delegated the responsibility of probabilistic collective safety under to the safety filter.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-F1 Choice of Dynamics", "weight": 1.0} -->

Our primary targets are quadrotors as we describe in Section IV. Waypoint tracking for quadrotors using on-board controllers is now well-known. Consequently, assuming linear dynamics is appropriate since the safety filter can generate safe waypoints that deviates minimally from the RL-based motion plan.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-F1 Choice of Dynamics", "weight": 1.0} -->

Theoretically, it is possible to apply the proposed solution to nonlinear dynamics. However, the construction of terminal sets for collision avoidance and recursive feasibility, similar to the sets proposed in Section III-D, become more challenging On the other hand, our approach achieves recursive feasibility in the presence of stochastic process noises. Using process noise to (conservatively) model the linearization error when using linear models for nonlinear dynamics, we can use the proposed approach to provide (conservative) safety guarantees.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-F2 Gaussian Noise Assumption", "weight": 1.0} -->

In our problem statement, we assumed Gaussian noise and imposed chance constraints. Alternatively, we can use other risk metrics based on axiomatic risk theory and more generalized noise distributions. However, most of these approaches either do not admit closed-form deterministic reformulations resulting in high computational costs, or are overly conservative. For example, our assumptions on $\mathbf{w}$ and $\mathbf{η}$ having a Gaussian distribution can be relaxed to any probability distribution that has a pre-specified mean and covariance. In this case, the reformulated constraints are similar to and but with $\Phi^{- 1}{(\alpha)}$ terms replaced by the Chebychev bound $\sqrt{\frac{1 - \alpha}{\alpha}}$. However, the resulting deterministic sufficient conditions are far more conservative than those in Propositions 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and 2.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-F2 Gaussian Noise Assumption", "weight": 1.0} -->

‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") \[53, Fig. 2\].

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-F3 Ellipsoidal Convex Set Usage", "weight": 1.0} -->

We recommend using ellipsoidal representations (or outer-approximations) for various convex sets, primarily due to the convexification step presented in Section III-D. Ellipsoids ${\mathcal{E}{(c,Q)}} = \left. \{ x \middle| {{{({x - c})} \cdot {({Q^{- 1}{({x - c})}})}} \leq 1}\} \right.$ admit a closed form solution for the support function ${\rho_{\mathcal{E}{(c,Q)}}{(\ell)}} = {{\ell \cdot c} + \sqrt{\ell \cdot {({Q\ell})}}}$, and the supporting hyperplane changes smoothly along the set boundary with changing $\ell$. Compared to that, the support function of a polytope requires solving a linear program, and may change abruptly when changing $\ell$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-F4 Safety Filtering with Other Motion Planners", "weight": 1.0} -->

We use the proposed safety filter in conjunction with single-agent RL motion planning, since RL-based planners have become popular in recent literature (see discussion in Section I) but lack safety guarantees especially in terms of enforcing (hard) constraints. While the proposed combination of RL and safety filter can provide hard constraint satisfaction guarantees, the safety filter's applicability is not limited to single-agent RL-based planners. As illustrated in Figure 2 and as seen from the derivations, the safety filter only requires the agents' reference state and control trajectories. These inputs may also be obtained from many other planners, including more traditional ones such as sampling-based. For example, RRT-based planners can be used for single-agent motion planning while avoiding static obstacles in the environment. The multi-agent plans can then be obtained by combining separate single-agent RRT-based plans using the proposed safety filter to guarantee inter-agent collision avoidance. This allows more efficient computations and memory reduction with respect to applying sampling-based planning to the multi-agent problem due to the smaller dimension and reduced number of collisions to be checked.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-F5 Intermediate multi-agent RL-based planners", "weight": 1.0} -->

The proposed approach can also be applied to the intermediate case of a planner for multiple agents $N_{\text{few}}$, but less than the total number $N$. In this case, multiple planners generate plans each for $N_{\text{few}}$ agents up to the total number $N$. Each group of $N_{\text{few}}$ may be collision-free, but the safety filter is applied to ensure safety between agents in different groups. Overall, the fundamental idea behind our approach is to take a challenging motion planning problem, approximate it by a problem that is significantly simpler to solve, at the price of losing safety due to the approximation, and then recovering it by the safety filter. In the case of multi-agent planning, approximation is done by reducing the amount of agents, hence here we discussed the largest possible reduction that provides the largest simplification, that is only one agent is considered in planning, but the approach will also work for any intermediate case.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Dynamics: We used the Crazyflie 2.1 quadrotors as our target platform. We flew all the quadrotors at the same height of $0.95$ m to make the collision avoidance problem more challenging. While it would be possible to resolve collisions by flying the drones at different heights, this solution does not generalize to other systems where more spatial dimensions do not exist (e.g. ground robots), and would not scale well to increasing number of robots or physically constrained environments.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

We approximated the 2D motion of the quadrotors using 2D double integrator dynamics, and thus, $A,B,C$ are given by with sampling time $T_{s} = 0.1$. We model the quadrotors as circles ($\mathcal{A}$ is a circle of radius $r_{A} = 0.1$) to include the $0.092$ m Crazyflie diameter as well as leave extra margin for aerodynamic effects and a safety padding.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Hardware setup: We used six quadrotors ($N = 6$) in our experiments. We relied on the Crazyswarm platform to communicate and control the quadrotors at 10Hz. The drones are equipped with IR-reflective markers detected by an OptiTrack motion capture system running at 120Hz. The Crazyswarm package tracked the Crazyflies using the raw point-cloud data from the OptiTrack motion capture system, and it issued desired waypoints at a nominal $10$ Hz update frequency over radio. The Crazyflies tracked those waypoints using their standard on-board controllers. In addition to the uncertainty in the Crazyflie position estimate induced by the Crazyswarm tracking algorithm, we added a position estimation noise $\mathbf{η}$ defined. Such measurement noises affects the safety filter, but is not visualized in the plotted physical experiment trajectories.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Workspace: We considered a $3 \times 3$ meter workspace with seven circular obstacles and two goal regions. The obstacles are depicted by black circles and the goal regions are depicted by transparent circles with a star at the center (see Figure 7). We also added position estimation noise to the nominal obstacle locations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Safety filter parameters: We used Gaussian noise with the following covariances: $\Sigma_{w} = \Sigma_{\eta} = {{diag}{(10^{- 4},0,10^{- 4},0)}}$ and $\Sigma_{c_{j}} = {{diag}{(10^{- 4},10^{- 4})}{\forall j}} \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$. As for the risk bounds, we used $\kappa_{i} = \alpha_{i,j} = \beta_{i,i'} = 0.01$ and divided them equally across the planning horizon $T = 10$. We used $\delta = 0.1$ for the terminal constraints. For the purposes of constructing the terminal sets, we select velocity bounds of $1$ m/s in the simulation, and $0.2$ m/s in the experiments.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Computer setup: We used an Ubuntu 20.04 LTS workstation with an AMD Ryzen 9 9590X 16-core CPU, a Nvidia GeForce GTX TITAN Black GPU, and 128GB of RAM for all training, simulation, and hardware experiments.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

RL training: We used Stable-Baselines3's implementation of the PPO (proximal policy optimization) algorithm to train the RL agents. We ran two training sessions, one for each goal, for $10$ million time steps each. We used the default parameters of Stable-Baselines3 with the following modifications: $0.01$ entropy coefficient, $2021$ seed, and cpu device. We use ${\zeta_{\text{obs}} = {- 0.001}},{{\zeta_{\text{tgt}} = {- 0.1}},{{R_{\text{target}} = 10^{4}},{P_{\text{keep-in}} = {- 10^{4}}}}}$, and $P_{\text{obstacle}} = {- 500}$ for the reward function parameters.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

After training, we selected the trained policy at about $9.7$ million steps and $9.44$ million steps for the two targets respectively. Each training session took just over $11$ hours.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Choice of unit vectors in Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"), 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"): Inspired, we used the following unit vectors: where ${p_{i}^{\text{RL}}{(\left. k \middle| t \right.)}} = {Cx_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}$. Such a choice used the predicted RL states and positions and the nominal obstacle locations to produce a heuristic for the computation of the safe halfspace polytopes.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

For the 2D double integrator dynamics, the lifted state is the position vector with zeros appended for the velocity components, i.e. ${\overline{c}}_{j}^{\text{lift}} = {\lbrack{{\overline{c}}_{j}^{\top}0_{2}^{\top}}\rbrack}^{\top}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Implementation Details and Experiment Setup", "weight": 1.0} -->

Solving the QP: We modeled the QP associated with the safety filter in Python 3.7 using CVXPY, utilizing parameters for values in that change at every control time step, and solved it using ECOS in experiments, and GUROBI in simulations.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experiments", "weight": 1.0} -->

We present results of the experimental validation of our approach on a quadrotor testbed. We show that the trained, single-agent RL-based motion planner generalizes well when used with the proposed safety filter. We also compare the proposed approach with a MPC-based multi-agent motion planner in simulation to emphasize the benefits of the RL step as well as the effects of the terminal constraints. We conclude with a demonstration of the scalability of our approach.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-A Experimental validation", "weight": 1.0} -->

In Figure 4, the top two rows are for the proposed solution with the RL controller and the proposed safety filter while the bottom two rows use the baseline controller instead of the RL controller. In both cases, the proposed safety filter ensures that the agents remain safe. In the RL case, the agents manage to reach their goals more rapidly, while the baseline controller case, the agents take significantly longer to reach their goals. In fact, when using the baseline controller instead of the RL controller, we found that the pink agent typically gets stuck between two obstacles and fails to reach its goal (see the bottom two rows of Figure 4).

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B Evaluation of the RL motion planner", "weight": 1.0} -->

The deterministic evaluation of the learned policy over a $100 \times 100$ grid is presented in Figure 8 (top row).

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B Evaluation of the RL motion planner", "weight": 1.0} -->

We observe that the RL agents learned to navigate to the goal starting from most initial conditions. As expected, the learned policy is not perfect and sometimes results in collisions with the obstacles or the workspace (Rows $1$ and $3$). Nevertheless, the combination of RL and the safety filter ensures safe motion planning (Rows $2$ and $4$). For less than $2\%$ of the initial conditions, the RL policy did not reach the target within $800$ time steps ($80$ s), which we mark as "loiter", i.e., static/dynamic deadlock, but safety was still guaranteed. In practice, it is usually possible to recover from such deadlock conditions by small state perturbations. We plan to investigate formal methods for avoiding and recovering from such deadlocks in future studies.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-B Evaluation of the RL motion planner", "weight": 1.0} -->

Task completion time Min. obstacle separation Min. agent separation Failed at control time step TABLE I: Comparison of the proposed safety filter with a pure MPC-based motion planner. The proposed approach completes the motion planning task for more percentage of trials. We report the -percentiles of the results of the subset of 100 Monte-Carlo simulations that completed the task successfully.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-C Simulation study: Impact of RL and terminal constraints", "weight": 1.0} -->

Next, we compare our approach with a pure MPC-based motion planner in simulation. Specifically, we solved, where the objective (12a) is replaced with a set point regulation cost, which results in the optimization problem, with ${U_{i}^{s}{(t)}} = {\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ for each $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$, pre-specified weights $\lambda_{i,t} \geq 0$ on the deviations $\parallel {\overline{p}}_{i}{(k|t)} - q_{i} \parallel^{2}$, and a penalty for inputs $\varepsilon > 0$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-C Simulation study: Impact of RL and terminal constraints", "weight": 1.0} -->

Problem is a convex quadratic program, thanks to the convexification step (Propositions 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) that uses a modified version of. Recall that the constraints of included constraints and that required user-specified unit vectors $z_{ij}^{\text{obs}},z_{ij}^{\text{agt}},\ell_{ij}^{\text{obs}}$, and $\ell_{ij}^{\text{agt}}$, which were defined using the RL trajectory. When formulating, we defined these vectors using the baseline controller trajectory instead of the RL trajectory for a fair comparison.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C Simulation study: Impact of RL and terminal constraints", "weight": 1.0} -->

One can view as an extension of existing single-agent motion planners under uncertainty (for example, ) for multi-agent motion planning, with the addition of terminal constraints for recursive feasibility proposed in Section III-D. Note that enables explicit coordination between agents as they move towards their goal, while the proposed safety filter only minimizes deviations from RL-based single-agent motion planners. We now study the RL block and the terminal constraints (Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) by comparing the performances of the proposed approach and a pure MPC approach, with and without terminal constraints (Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")).

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C Simulation study: Impact of RL and terminal constraints", "weight": 1.0} -->

Table I summarizes the performance of both the approaches in $100$ Monte-Carlo simulations. We observe that the proposed approach completed the motion planning task for a significantly larger number of simulations than a pure MPC approach ($99\%$ vs $55\%$ success), illustrating the benefits of including RL. The sources of failure in these simulations include collisions with static or dynamic obstacles (safety is enforced in probability) as well as numerical issues for the solver. For the proposed approach, the use of terminal constraints for recursive feasibility (Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) typically resulted in a larger minimum separation between agents and obstacles, and among agents. The use of terminal constraints also led to smaller task completion time, possibly due to the larger minimum separations. On the other hand, the use of similar terminal constraints in the MPC approach made the problem considerably harder and led to numerical issues in all trials, possibly because the trajectory of the baseline controller may not be as informative as the RL trajectory for the convexification step.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-C Simulation study: Impact of RL and terminal constraints", "weight": 1.0} -->

Finally, we observe that the proposed approach takes longer to complete the motion planning task than the pure MPC approach without the terminal constraints, when the latter does not result in safety violations. This is expected since the terminal constraints impose additional restriction on the generated trajectory to achieve recursive feasibility. The single agent motion planner combined with safety filter is suboptimal when applied to a multi-agent motion planning problem and is more conservative due to the terminal constraints, but guarantees safety. Thus, there is a trade-off between safety and performance.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-D Scalability study of the proposed approach", "weight": 1.0} -->

To perform scalability analysis of the safety filter, we reduced $r_{A}$ to $0.01$, reduced the noise covariance from $10^{- 4}$ to $10^{- 6}$, and collected computational times for the safety filter for $1000$ control time steps starting from randomly initialized locations for the agents in simulation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a solution for the multi-agent motion planning problem that combines reinforcement learning and constrained control. We utilize single-agent RL to train a policy for traversing a cluttered workspace while ignoring inter-agent collision avoidance, and use a real-time implementable, constrained-control-based safety filter to account for inter-agent collision avoidance and ensure probabilistic collective safety of the agents. The formulated QP includes chance constraints to achieve safety under process and measurement noise as well as probabilistic recursive feasibility constraints. We demonstrated the efficacy of our approach via numerical simulations, and validated our approach on a hardware testbed using quadrotors.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In our future work, we will investigate the application of the proposed approach in a decentralized setting, consider safe multi-agent motion planning for agents with nonlinear dynamics, and evaluate RL-based planning with a subset of the multiple agents larger than one.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Proof of Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") Static obstacle collision avoidance ((13a) $\Rightarrow$ (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")))*:* Using computational geometry arguments, (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) is a non-convex chance constraint, and is equivalent to To convexify it, we use a separating hyperplane for $({{{\overline{p}}_{i}{(\left.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion", "weight": 1.5} -->

k \middle| t \right.)}} - {\overline{c}}_{j}})$ and $\mathcal{O}_{j} \oplus {({- \mathcal{A}})}$ along the direction of a user-specified direction $z_{ij}^{\text{obs}}$. Thus, We use (15a. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) in Lemma 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") to reformulate the left hand side of the above implication to arrive at (13a). Thus, (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) holds, if (13a) holds.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Inter-agent collision avoidance ((13b) $\Rightarrow$ (6. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")))*:* Using arguments similar to the above with $z_{ij}^{\text{agt}},{{\overline{p}}_{j}{(\left. k \middle| t \right.)}},{\Sigma_{p_{j}}{(\left. k \middle| t \right.)}}$ instead of $z_{ij}^{\text{obs}},{\overline{c}}_{j},\Sigma_{c_{j}}$, we can show that (6. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) holds, if (13b) holds.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Keep-in constraint ((13c) $\Rightarrow$ (7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")))*:* From the definition of Pontryagin difference, (7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) is equivalent to Here, $\mathcal{K} \ominus \mathcal{A}$ is easy to compute \[37, Thm 2.3\].

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Specifically, ${\mathcal{K} \ominus \mathcal{A}} = {\cap_{i \in {\mathbb{N}}_{\lbrack 1,N_{\mathcal{K}}\rbrack}}{\{ p:{{h_{i} \cdot p} \leq {g_{i} - {S_{\mathcal{A}}{(h_{i})}}}}\}}}$. Using Boole's inequality and assuming that the risk bound is divided equally across all halfspaces, we have We use (15b. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) in Lemma 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") to reformulate the left hand side of the above implication to arrive at (13c). Thus, (7.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusion", "weight": 1.5} -->

‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) holds, if (13c) holds. ∎
