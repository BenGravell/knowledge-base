## Introduction

Multi-agent motion planning in cluttered workspaces under stochastic uncertainty arising from both perception and actuation is a key challenge in designing reliable autonomous systems. The need for such planners, especially for quadrotors, arises in a variety of application areas including transportation, logistics, monitoring, and agriculture. Recently, motion planning using reinforcement learning (RL) has gained attention, due to its ability to leverage data to tackle generic dynamical systems and complex task specifications. A major challenge for such efforts is the lack of safety guarantees, since most of the existing RL-based approaches enforce safety constraints by soft constraints and are subject to training errors. Additionally, multi-agent RL is known to suffer from non-stationarity and scalability issues, which may prevent the training to converge. We propose *a tractable approach to safe, multi-agent motion planning in stochastic, cluttered workspaces that combines reinforcement learning and set-based methods for constrained control. Our approach yields a safe, real-time implementable, multi-agent motion planner that is simple to train and enforces safety with high probability, by means of chance constraints.*

Figure 1: Existing reinforcement learning-based motion planners can generate unsafe trajectories (yellow arrows), since they treat safety as soft constraints, which is undesirable in safety-critical applications. We propose a constrained-control-based safety filter that renders such motion planners safe (long green arrows) by enforcing safety as hard constraints. See https://youtu.be/QcCSYNwuuo8 for an overview and videos of the experiments.

In the deterministic setting, various approaches have been proposed for multi-agent motion planning such as centralized scheduling and coordination, roadmap and discrete search followed by trajectory refinement, sampling-based rapidly-exploring random trees, adaptive roadmaps, buffered Voronoi cells, mixed-integer programming, sequential convex programming, formal methods and finite transition systems, and control barrier functions. Recently, RL-based planners have been used in complex environments. A key advantage of learning-based planners is the ability to leverage past experience in future decision making. Consequently, such planners can tackle *complex* and *high-dimensional* motion planning tasks, while incorporating prior information about the planning task and accommodating uncertainty.

Our preliminary work considered *deterministic* safe multi-agent motion planning, where everything was known exactly. We proposed a two-step approach where a single-agent RL algorithm provided a *reference* command which was subsequently *filtered* (or corrected) by a constrained control module. The works closest to are that also follow a similar two-step process. However, need labelled data for supervised learning, and use multi-agent RL. Multi-agent RL trains multiple agents to collectively complete the task, and as a consequence, is harder to train than single-agent RL. Additionally, relies on solving a two-player game in problems with discrete state and action space. Our approach utilizes single-agent RL that is simpler to train, can accommodate continuous state and action spaces for stabilizable linear dynamics, is real-time implementable, and need not be retrained as the number of agents increase.

In the stochastic setting, the presence of probabilistic constraints makes the motion planning problem more challenging. Here, we must balance the conservativeness of the motion plans with the risk (the probability of violation of a desirable property), while ensuring the existence of a solution that satisfies other problem objectives. The authors of propose single-agent motion planners using chance constrained programming, but these approaches may become prohibitively expensive when extended to multi-agent systems. combined artificial potential fields with stochastic reachability theory to generate motion plans for a single-agent in stochastic, cluttered workspaces. Recently, proposed using a *reference* controller, such as an RL controller trained offline, followed by a constrained-control-based online filtering step to guarantee safety of the control action being applied to the system, which was applied to autonomous racing. However, to the best of our knowledge, these works do not consider a multi-agent setup. Another line of research for multi-agent motion planning in stochastic settings uses buffered Voronoi cells, where motion plans are restricted to safety sets computed based on the "best" separating hyperplane between two Gaussian distributions, further tightened by a safety buffer. Such an approach couples planning and safety control, yet it does not guarantee recursive feasibility.

We focus on safe multi-agent motion planning in applications where a *centralized* decision maker coordinates the actions of the agents for safety and performance. Examples of such applications include air traffic control and coordinated traffic control centers. The proposed centralized approach may impose additional communication and computational burden when compared to a decentralized method (for e.g., ). However, the ability to enforce coordination helps the proposed approach typically generate safer and more efficient trajectories for the overall system.

Contributions of this work: Since RL has been recently of interest to the robotics community, we propose a solution to address the lack of safety in RL-based planners, specifically in multi-agent motion planning settings. We propose an optimization-based safety filter that, when used in conjunction with RL, provides a safe, multi-agent motion planner in cluttered workspaces under stochastic uncertainty. The proposed safety filter uses convex optimization and set-based control to compute minimum-norm corrections to the RL-based motion plan and guarantee probabilistic collective safety of the multi-agent system. We use single-agent RL to learn from data, while avoiding issues like non-stationarity and scalability that affect multi-agent RL. We also describe how to design terminal state constraints for the constrained-control-based safety filter by using reachability to achieve recursive feasibility. Finally, we demonstrate our approach by both numerical simulations and experiments using quadrotors.

We note that while the proposed solution is discussed in the context of RL, our approach is general and can be used with another planner instead of RL. For instance, the single-agent planner could be sampling-based (e.g. RRT-based planners ), and the advantage of our architecture would be in the dimensionality reduction and reduced effort for collision checking with respect to applying the sampling-based planner to the full multi-agent problem.

Relationship with our preliminary work: In, we proposed a safe, multi-agent motion planner using reinforcement learning and optimization for deterministic dynamics and a known workspace. We generated continuous-time safety guarantees under the assumption that the safety filter's control input is constant across the entire horizon of the safety filter. In this work, we extend our preliminary work to stochastic workspace, dynamics, and sensing, and provide probabilistic safety guarantees for the overall system without relying on the constant control input assumptions. We also explicitly assess recursive feasibility of the safety filter, and investigate the importance of the RL controller, safety filter, and the terminal constraints in the proposed approach using extensive hardware and simulation experiments.

### I-A Notation

$0_{d}$ ($0_{n,m}$) is a vector (matrix) of zeros in ${\mathbb{R}}^{d}$ (${\mathbb{R}}^{d \times m}$), $I_{d}$ is the $d$-dimensional identity matrix, and ${\mathbb{N}}_{\lbrack a,b\rbrack}$ is the subset of natural numbers between (and including) ${a,b} \in {\mathbb{N}}$, $a \leq b$, and ${\mathbb{N}}_{\lbrack a,b\rbrack} = \varnothing$ when $a > b$. $\oplus, \ominus$ are the Minkowski sum and Pontyagrin difference, respectively, and $\parallel \cdot \parallel$ is the 2-norm of a vector. The support function of a convex and compact set $\mathcal{C}$ is ${S_{\mathcal{C}}{(\ell)}} \triangleq {\sup_{x \in \mathcal{C}}{\ell \cdot x}}$ for any $\ell \in {\mathbb{R}}^{d}$.

$(\Omega,\mathcal{F},{\mathbb{P}})$ is a probability space where $\Omega$ is the sample space, $\mathcal{F}$ is a $\sigma$-algebra of subsets of $\Omega$, and $\mathbb{P}$ is a probability measure on $\mathcal{F}$. We denote random vectors in bold ${\mathbf{x}}:{\Omega\rightarrow{\mathbb{R}}^{n}}$ and their mean $\overline{x} \triangleq {{\mathbb{E}}{\lbrack{\mathbf{x}}\rbrack}}$, where $\mathbb{E}$ is the expectation operator with respect to $\mathbb{P}$. We use $\hat{x}$ to denote a realization of a random vector $\mathbf{x}$. We use $\mathcal{N}{(\mu,\Sigma)}$ to denote a Gaussian random vector with mean $\mu$ and covariance $\Sigma$, and refer to $\mathcal{N}{(0_{n},I_{n})}$ as the standard Gaussian random vector. For a vector ${\mathbf{v}}{(t)}$, ${\mathbf{v}}{(\left. k \middle| t \right.)}$ is the predicted value at $k \geq t$ based on the information available at time $t$, and we denote ${{\mathbf{v}}{(\left. t \middle| t \right.)}} = {{\mathbf{v}}{(t)}}$. We use the same notation when referring to the distribution of ${\mathbf{v}}{(t)}$.

The following abbreviations are used throughout the paper: iid (independent and identically distributed), MPC (model predictive control), QP (quadratic program), and PSD (positive semidefinite).

## Problem formulation

Dynamics: Consider $N \in {\mathbb{N}}$ homogeneous agents with the discrete-time linear dynamics at time $t$,

with state ${\mathbf{x}}_{i} \in {\mathbb{R}}^{n}$, input $u_{i} \in \mathcal{U} \subset {\mathbb{R}}^{m}$, process noise ${\mathbf{w}}_{i} \in {\mathbb{R}}^{n}$, state update matrix $A \in {\mathbb{R}}^{n \times n}$, and input matrix $B \in {\mathbb{R}}^{n \times m}$ for each agent $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$. The input set $\mathcal{U}$ is a convex and compact polytope, and the process noise is iid, zero-mean Gaussian ${\mathbf{w}}_{i} \sim \mathcal{N}{(0_{n},\Sigma_{w}}$) for some known PSD matrix $\Sigma_{w} \in {\mathbb{R}}^{n \times n}$. The position of the agent $i$ at time $t$ is given by,

for some $C \in {\mathbb{R}}^{d \times n}$, $d < m$. For $k \geq t$, the mean state of the agents is predicted according to the nominal dynamics,

${\overline{x}}_{i}{({k + \left. 1 \middle| t \right.})}$ $= {{A{\overline{x}}_{i}{(\left. k \middle| t \right.)}} + {Bu_{i}{(\left. k \middle| t \right.)}}}$ (3a)
${\overline{p}}_{i}{(\left. k \middle| t \right.)}$ ${= {C{\overline{x}}_{i}{(\left. k \middle| t \right.)}}}.$ (3b)

We assume that the nominal dynamics are stabilizable, i.e., there exists a stabilizing gain matrix $K \in {\mathbb{R}}^{m \times n}$ that ensures that all eigenvalues of $({A + {BK}})$ lie in the unit circle.

Measurement model: We assume that the initial state of each agent ${{\mathbf{x}}_{i}{}} = {x_{i}{}}$ is known, i.e., deterministic. However, for $t > 0$, we have access only to a noisy measurement of the true state ${\mathbf{x}}_{i}{(t)}$. Specifically, we assume that the measurements ${\hat{y}}_{i}{(t)}$ are a realization of a random vector ${\mathbf{y}}{(t)}$,

where ${\mathbf{η}}_{i} \sim \mathcal{N}{(0_{n},\Sigma_{\eta}}$) is a zero-mean Gaussian noise with a known PSD matrix $\Sigma_{\eta} \in {\mathbb{R}}^{n \times n}$.

Agent Representation: We consider agents with identical convex and compact rigid bodies, denoted by $\mathcal{A} \subset {\mathbb{R}}^{d}$, such that $0_{d} \in \mathcal{A}$. The rigid bodies of the agents are rotation-invariant. So, we only consider translations.

### Remark 1

We can generalize all the presented results to account for heterogeneous agents with heterogeneous linear dynamics, measurement models, and rigid bodies. We consider homogeneity in all of these aspects to simplify the presentation.

Workspace Representation: We represent the workspace using a convex and compact polytope $\mathcal{K} \subset {\mathbb{R}}^{d}$.

Obstacle Representation: The workspace has $N_{O}$ static obstacles, each with a convex and compact rigid body $\mathcal{O}_{j} \subset {\mathbb{R}}^{d}$ and $0_{d} \in \mathcal{O}_{j}$ ($j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$). The obstacle shapes are known *a priori*, but their positions are available only via a noisy measurement. Specifically, for each obstacle $j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$, the position of a representative point of the obstacle (e.g. the *center*) is denoted by ${\mathbf{c}}_{j} \in {\mathbb{R}}^{d}$ where ${\mathbf{c}}_{j}$ is an iid Gaussian random vector ${\mathbf{c}}_{j} \sim {\mathcal{N}{({\overline{c}}_{j},\Sigma_{c_{j}})}}$ with nominal position ${\overline{c}}_{j}$ and covariance matrix $\Sigma_{c_{j}} \in {\mathbb{R}}^{d \times d}$.

### II-A Safe multi-agent motion planning under uncertainty

Given target positions $q_{i} \in {\mathbb{R}}^{d}$, we want to design a motion planner that drives the agents towards their respective target positions, while ensuring safety of the agents at all times, despite the uncertainty in the dynamics and the noisy estimates of the agent and obstacle positions. Here, we formalize the required features of safety in the multi-agent motion planning problem by introducing the notion of *probabilistic collective safety*, inspired by existing literature.

### Definition 1 (Probabilistic Collective Safety)

The agents are said to be *probabilistically collectively safe* at time $t$ when all the following criteria are met:

*Static obstacle avoidance constraints*: The probability of collision of agent $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$ with obstacle $j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$ is less than a pre-specified risk bound $\alpha_{i,j,t} \in {}$,

*Inter-agent collision avoidance*: The probability of collision between agents ${{i,i^{\prime}} \in {\mathbb{N}}_{\lbrack 1,N\rbrack}},{i \neq i^{\prime}}$ is less than a pre-specified risk bound $\beta_{i,i^{\prime},k} \in {}$,

*Keep-in constraints*: The probability of agent $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$ exiting the keep-in set $\mathcal{K}$ is less than a pre-specified risk bound $\kappa_{i,k} \in {}$,

Next, we formulate the problem tackled in this paper.

### Problem 1 (Safe Multi-Agent Planning)

Given user-specified risk bounds $\alpha_{i,j,t},\beta_{i,i^{\prime},t},\kappa_{i,t}$, for every ${i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}},{{i^{\prime} \in {\mathbb{N}}_{\lbrack 1,{i - 1}\rbrack}},{j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}}}$ and $t \in {\mathbb{N}}$, design a multi-agent motion planner that navigates the agents with dynamics to their respective targets such that the agents are probabilistically collectively safe at all times $t$.

In the statement of Problem 1. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"), we specified a risk bound for every time step ($\alpha_{i,j,t},\beta_{i,i^{\prime},t},\kappa_{i,t}$). On the other hand, when a risk bound for the entire planned trajectory (e.g. $\alpha_{i,j}$) is given over a planning horizon $T \in {\mathbb{N}}$, one can arrive at $\alpha_{i,j,t}$ via *risk allocation* --- divide the risk equally across time steps with $\alpha_{i,j,t} = {\alpha_{i,j}/T}$ for every $t \in {\mathbb{N}}_{\lbrack 1,T\rbrack}$.

Figure 2: The proposed solution combines single-agent RL-based motion planning with a constrained-control-based safety filter for safe multi-agent motion planning. It computes a sequence of RL states and controls for the horizon T using a predict block. Next, it uses a safety filter to render these controls safe for each agent. The predict block uses a policy network (trained offline) and the nominal dynamics to compute the RL controls and states.

## Proposed Solution

We solve Problem 1. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") by the following two steps.

*RL training (Offline):* We train a neural network to drive a *single* agent with *nominal* (deterministic) dynamics from any initial state in the workspace to a final desired state. The resulting policy learns to perform static obstacle collision avoidance and remain within the workspace while transferring a single agent from its initial state to the final state.

*Safety Filter (Online):* We use a constrained-control-based safety filter that uses an online evaluation of the RL-based motion planner. The safety filter suitably modifies the motion plan to enforce probabilistic collective safety at all time steps. The safety filter solves a real-time implementable, convex, quadratic program to determine the modifications.

Figure 2 depicts the proposed solution. In the following, we describe the RL-based motion planner, provide details of constructing the safety filter to enforce probabilistic collective safety, and discuss various aspects of the proposed solution.

### III-A Reinforcement learning-based single-agent motion planner

We design a RL-based motion planner that drives the agent with nominal dynamics to a specified target position $q \in {\mathbb{R}}^{d}$ in presence of $N_{O}$ static obstacles located at nominal positions ${{\overline{c}}_{j}{\forall j}} \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$. Here, we train a *single-agent RL-based* planner in an environment devoid of other agents. After briefly discussing the motivations for such an approximation, we set up the Markov decision process used for training and characterize the neural policy obtained via single-agent RL training.

The advantage of using a single-agent RL-based planner instead of the full multi-agent RL-based planner is in the ease of training. Specifically, a single-agent RL-based planner avoids some issues of multi-agent RL such as non-stationarity, scalability, and the diminished ability to accommodate potential changes in team size post training. Recall that in multi-agent RL, all agents learn concurrently and thus an action taken by an individual agent affects both the reward of the other agents and the evolution of the state of the system. From the agent's perspective the environment is non-stationary. By approximating the problem and eliminating the other agents, training a single-agent RL is a stationary problem which is key for convergence results of RL training and for the reduced training effort. Moreover, compared to multi-agent RL training, whose joint state space and joint action space grow rapidly in dimension with the number of agents, the state space and the action space dimensions are fixed and independent of the team size in the single-agent RL training. Finally, if the team size changes post training, the proposed single-agent RL-based planner in Figure 2 can still be used without any modifications as compared to a complete multi-agent RL-based planner, which may require re-training to handle changes in the team size.

Consider a feedforward-feedback controller $\pi:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{m}}$ with

where $K$ is a stabilizing gain matrix, $F \in {\mathbb{R}}^{m \times d}$ provides closed loop unitary gain with the nominal dynamics, i.e., ${C{({I - {({A + {BK}})}})}^{- 1}BF} = I_{d}$, and $r \in {\mathbb{R}}^{d}$ is the reference position command. We obtain the following stabilized, nominal, prediction model for the agent at any time $k \geq t$,

by closing the loop of the dynamics with the controller. For the measurement model, the predicted measurements are ${\hat{y}{(\left. k \middle| t \right.)}} = {\overline{x}{(\left. k \middle| t \right.)}}$ for every $k \geq t$. By construction, the mean predicted position ${\overline{p}{(\left. k \middle| t \right.)}}\rightarrow r$ as $k\rightarrow\infty$ for a constant reference command ${r{(\left. k \middle| t \right.)}} = r$.

We use the following Markov decision process for training:

*Observation space*: We define the observation vector $o \in {\mathbb{R}}^{n + d + {N_{O}d}}$ as the concatenated vector containing the current measurement of the agent $\hat{y} \in {\mathbb{R}}^{n}$, the displacement of the agent's current measured position to the target ${({p - q})} \in {\mathbb{R}}^{d}$ and to the $N_{O}$ static obstacles ${({p - {\overline{c}}_{j}})} \in {\mathbb{R}}^{d}$, for all $j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$, where $p = {C\hat{y}}$.

*Action space*: The action $a \in \mathcal{A} \subset {\mathbb{R}}^{d}$ determines the reference position as a perturbation $a$ to the target $q$, $r = {q + a}$. The set $\mathcal{A}$ is compact.

*Step function*: The next predicted measurement${\hat{y}{({t + \left. 1 \middle| t \right.})}} = {\overline{x}{({t + \left. 1 \middle| t \right.})}}$ is given by.

*Reward function*: The instantaneous reward function is

with reward parameters ${\zeta_{\text{obs}},\zeta_{\text{tgt}}} \leq 0$ and $\gamma_{j} \geq 0$. Here, $\gamma_{j}$ is the radius of the smallest volume ball that covers the set $\mathcal{O}_{j} \oplus {({- \mathcal{A}})}$ for each $j \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$. We terminate an episode when the agent either reaches the target or violates the *nominal single-agent* safety conditions, namely the static obstacle avoidance and keep-in constraints. These constraint violations are given by:

When the episode terminates, we add a terminal reward or penalty as follows:

with $o_{\infty}$ and $p_{\infty}$ denoting as the observation and position vectors upon termination respectively, $R_{\text{target}} \geq 0$, and ${P_{\text{keep-in}},P_{\text{obstacle}}} \leq 0$.

We have set up the Markov decision process to consider deterministic nominal dynamics instead of the original stochastic dynamics in order to simplify the RL training. Our numerical and hardware experiments show that the restriction to deterministic nominal dynamics does not affect the proposed solution severely.

### Remark 2

Our approach can also accommodate a known, time-varying target and biased measurement models $\overline{\mathbf{η}} \neq 0$. We have considered a time-invariant target $q$ and an unbiased measurement model here to simplify the presentation. Additionally, we use the minimum volume balls with radius $\gamma_{j}$ in instead of $\mathcal{O}_{j} \oplus {({- \mathcal{A}})}$ to simplify the collision detection while training the RL-based motion planner.

Upon completion of training, most of the existing RL algorithms return a policy $\nu:{{\mathbb{R}}^{n + d + {N_{O}d}}\rightarrow\mathcal{A}}$ that provides the action to apply given an observation vector, e.g., by a neural network. Additionally, we can "rollout" the policy network $\nu$ to obtain a trajectory based on the RL motion planner for a planning horizon $T \in {\mathbb{N}}$. Consider any agent $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$ that starts with the measurement ${\hat{y}}_{i}{(t)}$. We compute the RL motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$, where ${x_{i}^{\text{RL}}{(\left. t \middle| t \right.)}} = {{\hat{y}}_{i}{(t)}}$, by alternating between finding the control $u_{i}^{RL}{(\left. k \middle| t \right.)}$ given the predicted RL state $x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}$ and predicted observation vector $o_{i}{(\left. k \middle| t \right.)}$ at some time $k \geq t$ using $\pi$,

and predicting the next RL state $x_{i}^{\text{RL}}{({k + \left. 1 \middle| t \right.})}$ using and the corresponding predicted observation vector $o_{i}{({k + \left. 1 \middle| t \right.})}$.

The generated motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$ does not satisfy probabilistic collective safety, since RL cannot guarantee collision-free trajectories (it only penalizes collisions and is subject to training errors), and the generated RL motion plan completely ignores inter-agent collision avoidance and the effect of the process and measurement noises.

### III-B Safety Filter

We now generate corrections to the RL-based motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$ using a constrained-control-based safety filter that ensures the satisfaction of probabilistic collective safety at all times. Consider the following optimization problem with the stochastic information,

$\min\limits_{{\{{U_{i}^{s}{(t)}}\}}_{i=1}^{N}}$ $\sum\limits_{k \in {\mathbb{N}}_{\lbrack t,{{t + T} - 1}\rbrack}}\sum\limits_{i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}}\lambda_{i,k} \parallel u_{i}^{RL}{(k|t)} - u_{i}^{safe}{(k|t)} \parallel^{2}$ (12a)
${s.t}.$ Dynamics and with $u = u^{safe}$, (12b)
${{{{\mathbf{x}}_{i}{(\left. t \middle| t \right.)}} = {{{\hat{y}}_{i}{(t)}} - {{\mathbf{η}}{(t)}}}},{{\forall i} \in {\mathbb{N}}_{\lbrack 1,N\rbrack}}},$ (12c)
${{{u_{i}^{safe}{(\left. k \middle| t \right.)}} \in \mathcal{U}},{{{\forall k} \in {\mathbb{N}}_{\lbrack t,{{t + T} - 1}\rbrack}},{{\forall i} \in {\mathbb{N}}_{\lbrack 1,N\rbrack}}}},$ (12d)
${{{\text{Probabilistic collective safety (12e)
at~}k},{\forall k}} \in {\mathbb{N}}_{\lbrack t,{t + T}\rbrack}},$
$\text{Terminal constraints for recursive feasibility},$ (12f)

where ${U_{i}^{s}{(t)}} = {\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ for each $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$, and $\lambda_{i,k} \geq 0$ are pre-specified weights on the deviations $\parallel u_{i}^{RL}{(k|t)} - u_{i}^{safe}{(k|t)} \parallel^{2}$ for $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$ and $k \in {\mathbb{N}}_{\lbrack t,{{t + T} - 1}\rbrack}$.

$z_{ij}^{\text{obs}} \cdot {({{{\overline{p}}_{i}{(\left. k \middle| t \right.)}} - {\overline{c}}_{j}})}$
≥ S𝒪j(zi jobs) + S(−𝒜)(zi jobs) − ∥ (Σpi(k|t)+Σcj)1/2zi jobs ∥ Φ−1(αi, j, t),

$z_{ij}^{\text{agt}} \cdot {({{{\overline{p}}_{i}{(\left. k \middle| t \right.)}} - {{\overline{p}}_{j}{(\left. k \middle| t \right.)}}})}$
≥ S𝒜(zi jagt) + S(−𝒜)(zi jagt) − ∥ (Σpi(k|t)+Σpj(k|t))1/2zi jagt ∥ Φ−1(βi, j, t),

${h_{j} \cdot {\overline{p}}_{i}}{(\left. k \middle| t \right.)}$

The safety filter takes the RL control sequence ${\{{u_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ that is generated using the RL-based single-agent motion planner, and computes safe control inputs ${\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ within the control set (12d) that minimally deviate from the corresponding RL control inputs (12a), while enforcing probabilistic collective safety constraints (12e). The constraint (12c) defines the distribution of the noisy current state ${\mathbf{x}}{(\left. t \middle| t \right.)}$ from the current measurement $\hat{y}{(t)}$ and the measurement model. Additionally, to avoid computing control actions $u_{i}^{\text{safe}}$ that may render the optimization problem in the safety filter infeasible in the future, we include terminal state constraints (12f) that, when designed as explained later, provide recursive feasibility. Only the first safe control $u_{i}^{\text{safe}}{(\left. t \middle| t \right.)}$ is applied for each agent $i$, and then is solved again at time $t + 1$ in an MPC-like fashion.

The safety filter is a nonlinear, non-convex, and stochastic optimization problem due to (12e) and (12f), and as a consequence in general not real-time implementable. Therefore, we reformulate by convexifying the constraints and replacing the chance constraints by deterministic risk-tightened constraints, which we describe next.

### III-C Convexified constraints for probabilistic collective safety

We now present a convex, deterministic reformulation of (12e) that relies on well-known properties of Gaussian random vectors and the generated motion plan ${\{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}\}}_{k = t}^{t + T}$.

### Lemma 1 (Gaussian random vectors \[41, Sec. 4.4.2\])

1\) Let $N_{I} \in {\mathbb{N}}$. Given $n$-dimensional Gaussian random vectors $\mathbf{y}_{i} \sim {\mathcal{N}{({\overline{y}}_{i},\Sigma_{y_{i}})}}$ with ${\overline{y}}_{i} \in {\mathbb{R}}^{n}$, $\Sigma_{y_{i}} \in {\mathbb{R}}^{n \times n}$, and matrices $Y_{i} \in {\mathbb{R}}^{m \times n}$ for each $i \in {\mathbb{N}}_{\lbrack 1,N_{I}\rbrack}$, then the random vector $\mathbf{y} = {\sum_{i = 1}^{N_{I}}{Y_{i}\mathbf{y}_{i}}}$ is also Gaussian, with

2\) Given $\mathbf{y} \sim {\mathcal{N}{(\overline{y},\Sigma_{y})}}$ with ${\overline{y} \in {\mathbb{R}}^{n}},{\Sigma_{y} \in {\mathbb{R}}^{n \times n}}$, $a \in {\mathbb{R}}^{n}$, $b \in {\mathbb{R}}$, and the risk bound $\alpha$, then

${{\mathbb{P}}{({{a \cdot {\mathbf{y}}} \leq b})}} \leq \alpha$ ${\Leftrightarrow{{a \cdot \overline{y}} \geq {b - {{\|{\Sigma_{y}^{1/2}a}\|}\Phi^{- 1}{(\alpha)}}}}},$ (15a)
${{\mathbb{P}}{({{a \cdot {\mathbf{y}}} \geq b})}} \leq \alpha$ ${\Leftrightarrow{{a \cdot \overline{y}} \leq {b - {{\|{\Sigma_{y}^{1/2}a}\|}\Phi^{- 1}{({1 - \alpha})}}}}},$ (15b)

where $\Phi^{- 1}$ is the inverse cumulative distribution function of a standard Gaussian random variable.

Figure 3: Probabilistic collective safety constraints (Definition 1) enforced as linear constraints — (Left) Keep-in constraint (black) tightened by the support of 𝒜 (red). (Right) Inter-agent collision avoidance constraint uses the support of 𝒜 ⊕ − 𝒜 (red). Both red constraints are tightened by the chance constraint term resulting in a new constraint (dashed green).

From (12c) and, ${{\mathbf{x}}{(t)}} \sim {\mathcal{N}{({{\hat{y}}_{i}{(t)}},\Sigma_{\eta})}}$. For every agent $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$, the predicted state and position at any time $k > t$,

${\mathbf{x}}_{i}{(\left. k \middle| t \right.)}$ ${\sim {\mathcal{N}{({{\overline{x}}_{i}{(\left. k \middle| t \right.)}},{\Sigma_{x_{i}}{(\left. k \middle| t \right.)}})}}},$ (16a)
${\mathbf{p}}_{i}{(\left. k \middle| t \right.)}$ ${\sim {\mathcal{N}{({{\overline{p}}_{i}{(\left. k \middle| t \right.)}},{\Sigma_{p_{i}}{(\left. k \middle| t \right.)}})}}},$ (16b)
${\overline{x}}_{i}{(\left. k \middle| t \right.)}$ ${= {{A^{k - t}{\hat{y}}_{i}{(t)}} + {\sum\limits_{j = t}^{k - 1}{A^{k - {({j + 1})}}Bu_{i}^{safe}{(\left. j \middle| t \right.)}}}}},$ (16c)
${\overline{p}}_{i}{(\left. k \middle| t \right.)}$ ${= {C{\overline{x}}_{i}{(\left. k \middle| t \right.)}}},$ (16d)
$\Sigma_{x_{i}}{({k + \left. 1 \middle| t \right.})}$ ${= {{A\Sigma_{x_{i}}{(\left. k \middle| t \right.)}A^{\top}} + \Sigma_{w}}},$ (16e)
$\Sigma_{p_{i}}{(\left. k \middle| t \right.)}$ ${= {C\Sigma_{x_{i}}{(\left. k \middle| t \right.)}C^{\top}}}.$ (16f)

using the stochastic dynamics, (12c), and (15a. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) in Lemma 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"). We observe that ${\overline{x}}_{i}{(\left. k \middle| t \right.)}$ and ${\overline{p}}_{i}{(\left. k \middle| t \right.)}$ depend on the decision variables $u_{i}^{safe}$, but $\Sigma_{x_{i}}{(\left. k \middle| t \right.)}$ and $\Sigma_{p_{i}}{(\left. k \middle| t \right.)}$ do not. Thus, $\Sigma_{x_{i}}{(\left. k \middle| t \right.)}$ and $\Sigma_{p_{i}}{(\left. k \middle| t \right.)}$ may be computed offline.

### Proposition 1 (Risk-Tightened Sufficient Safety Constraints)

Given a polytope$\mathcal{K} = {\cap_{i \in {\mathbb{N}}_{\lbrack 1,N_{\mathcal{K}}\rbrack}}\left\{ {p \in {\mathbb{R}}^{d}}:{{h_{i} \cdot p} \leq g_{i}} \right\}}$ with $N_{\mathcal{K}} \in {\mathbb{N}}$ halfspaces characterized by ${\{ h_{i},g_{i}\}}_{i = 1}^{N_{\mathcal{K}}}$, $h_{i} \in {\mathbb{R}}^{d}$ and $g_{i} \in {\mathbb{R}}$, and user-defined unit vectors ${z_{ij}^{\text{obs}},z_{ij}^{\text{agt}}} \in {\mathbb{R}}^{d}$. Then, for every $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$ and $k \in {\mathbb{N}}_{\lbrack t,{t + T}\rbrack}$, is sufficient for (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")), (6. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")), and (7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) to hold.

We provide the proof of Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") in Appendix VI.

The reformulation in Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") follows from applying computational geometry arguments to convexify the chance constraints (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"))--(7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) using supporting hyperplanes defined by user-specified vectors $z_{ij}^{\text{obs}},z_{ij}^{\text{agt}}$, and then applying Lemma 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and Boole's law to arrive at. From (16c) and (16d), the constraints in Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") are linear inequalities in the decision variables ${\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ for every $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$. Figure 3 illustrates the reformulated constraints of Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning").

### III-D Ensuring recursive feasibility using reachability

We now turn our attention to (12f) that is designed to ensure that remains feasible in subsequent control time steps. For recursive feasibility (12f), we enforce the existence of a terminal set and a control ${u_{i}^{\text{recurse}}{(k)}} \in \mathcal{U}$ for all $k \geq {t + T}$ for each agent $i$ such that the following constraints hold for all $k \geq {t + T}$,

${\mathbb{P}}{({{{({{{\mathbf{p}}_{i}{(\left. k \middle| t \right.)}} \oplus \mathcal{A}})} \cap {({{\mathbf{c}}_{j} \oplus \mathcal{O}_{j}})}} \neq \varnothing})}$ ${\leq \delta},$ (17a)
${\mathbb{P}}{({{{({{{\mathbf{p}}_{i}{(\left. k \middle| t \right.)}} \oplus \mathcal{A}})} \cap {({{{\mathbf{p}}_{j}{(\left. k \middle| t \right.)}} \oplus \mathcal{A}})}} \neq \varnothing})}$ ${\leq \delta} $ (17b)
${\mathbb{P}}{({{({{{\mathbf{p}}_{i}{(\left. k \middle| t \right.)}} \oplus \mathcal{A}})} \nsubseteq \mathcal{K}})}$ ${\leq \delta},$ (17c)

where $\delta \in {}$ is a (small) user-specified risk threshold.

Existing literature in constrained control typically enforces recursive feasibility using control invariant or positive invariant sets. However, characterization of such sets can be challenging in our setting due to the inherent non-convexity of the probabilistic collective safety constraints. Alternatively, one can approximately enforce these constraints by truncating the recursive feasibility criterion to a finite but long horizon, and then utilizing stochastic reachability.

For the sake of tractability, we enforce approximately by imposing chance constraints on the terminal states, while ignoring the stochasticity in the future time steps. We characterize these constraints using appropriately defined *avoid sets* (also known as *inevitable collision states* or *capture sets* ) and *viability sets* (also known as *controlled invariant sets*).

### Definition 2 (Avoid set and viability set \[40\])

For a (bad) set $\mathcal{B} \subset {\mathbb{R}}^{n}$, linear dynamics, and a control constraint set $\mathcal{U}$, we define an avoid set as follows,

For a (good) set $\mathcal{G} \subset {\mathbb{R}}^{n}$, we define a viability set as follows,

Informally, ${AvoidSet}{(\mathcal{B})}$ is the set of mean initial states from which the mean trajectory of enters the bad set $\mathcal{B}$ at some time $t$, irrespective of the control choices. On the other hand, ${ViabilitySet}{(\mathcal{G})}$ is the set of mean initial states from which the mean trajectory of remains within the good set $\mathcal{G}$ for all time $t$, by some appropriate choice of control actions.

For any time $t$, assume that the agents evolve by stochastic dynamics with imperfect measurements according to during the planning interval ($k \in {\mathbb{N}}_{\lbrack t,{{t + T} - 1}\rbrack}$), and they evolve by nominal dynamics with perfect measurements beyond the planning horizon ($k \geq {t + T}$). Since the safety filter solves at every $t$ based on the new measurement, the impact of this assumption is mild for sufficiently long planning horizon $T$. Under this assumption, we construct the following approximation of using Definition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"),

${\mathbb{P}}{({{({{{\mathbf{x}}_{i}{({k + \left. T \middle| k \right.})}} - {{\mathbf{c}}_{j}^{\text{lift}}{({k + \left. T \middle| k \right.})}}})} \in {{AvoidSet}{({\mathcal{O}_{j} \oplus {({- \mathcal{A}})}})}}})}$ ${\leq \delta},$ (25a)
${\mathbb{P}}{({{({{{\mathbf{x}}_{i}{({k + \left. T \middle| k \right.})}} - {{\mathbf{x}}_{j}{({k + \left. T \middle| k \right.})}}})} \in {{AvoidSet}{({\mathcal{A} \oplus {({- \mathcal{A}})}})}}})}$ ${\leq \delta},$ (25b)
${\mathbb{P}}{({{{\mathbf{x}}_{i}{({k + \left. T \middle| k \right.})}} \notin {{ViabilitySet}{({\mathcal{K} \ominus \mathcal{A}})}}})}$ ${\leq \delta},$ (25c)

where ${\mathbf{c}}_{j}^{\text{lift}} \in {\mathbb{R}}^{n}$ is obtained by lifting the position to ${\mathbb{R}}^{n}$ with added components set to zero, since the obstacles are static. (25c) uses (24. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) for ease in implementation. Informally, (25a) and (25b) require the agents to be in configurations that lead to collision with static obstacles or each other with at most a probability of $\delta$, and (25c) requires the probability that the agents are in configurations from which they can not remain within the workspace is at most $\delta$.

$\ell_{ij}^{\text{obs}} \cdot {({{{\overline{x}}_{i}{({t + \left. T \middle| t \right.})}} - {\overline{c}}_{j}^{\text{lift}}})}$
≥ S𝒜𝒪j(ℓi jobs) − ∥ (Σxi(t+T|t)+Σcjlift)1/2ℓi jobs ∥ Φ−1(δ),

$\ell_{ij}^{\text{agt}} \cdot {({{{\overline{x}}_{i}{({t + \left. T \middle| t \right.})}} - {{\overline{x}}_{j}{({t + \left. T \middle| t \right.})}}})}$

${{\underset{¯}{h}}_{j} \cdot {\overline{x}}_{i}}{({t + \left. T \middle| t \right.})}$
$\leq {\underset{¯}{g}}_{j} - \parallel \Sigma_{x_{i}}^{1/2}{(t + T|t)}{\underset{¯}{h}}_{j} \parallel \Phi^{- 1}\left( 1 - {(\delta/N_{\mathcal{V}})} \right).$

The constraints are tractable when the sets ${AvoidSet}{({\mathcal{A} \oplus {({- \mathcal{A}})}})}$, ${AvoidSet}{({\mathcal{A} \oplus {({- \mathcal{O}_{j}})}})}$, and ${ViabilitySet}{({\mathcal{K} \ominus \mathcal{A}})}$ are convex. Recall that ${AvoidSet}{(\mathcal{B})}$ is typically non-convex, even when $\mathcal{B} \in {\{{\mathcal{A} \oplus {({- \mathcal{A}})}},{\mathcal{A} \oplus {({- \mathcal{O}_{j}})}}\}}$ is a convex polytope. This complicates the enforcement of (25a) and (25b). For the sake of tractability and ensuring conservativeness, we propose Algorithm 1 to compute an ellipsoidal outer-approximation of ${AvoidSet}{(\mathcal{B})}$. Outer-approximations of $AvoidSet$ are also sufficient to enforce (25a) and (25b). On the other hand, Algorithm 2 provides an exact approach to compute ${ViabilitySet}{({\mathcal{K} \ominus \mathcal{A}})}$ for convex and compact polytopes $\mathcal{K}$ and $\mathcal{A}$. All operations in Algorithms 1 and 2 can be easily accomplished using computational geometry tools and convex optimization, see for more details.

11:Linear dynamics, control constraint set 𝒰,convex and compact polytope ℬ.
44:while CurrentSet is non-empty
66: Append CurrentSet to ListOfSets
77:ConvexHullOfList← convex hull of ListOfSets
8:AvoidSet+(ℬ)← minimum volume ellipsoid containing ConvexHullOfList (see [41, Sec. 8.4.1])
Algorithm 1 Computation of AvoidSet+(ℬ) (See [40, Sec. 10.2] for recursion)

11:Linear dynamics, control constraint set 𝒰, convex and compact polytope 𝒢.
44:while CurrentSet is not equal to PrevSet
Algorithm 2 Computation of ViabilitySet(𝒢)

We conclude this section by characterizing a set of linear constraints that are sufficient to enforce. The proof of Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") uses the same arguments as that seen in Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning").

### Proposition 2 (Risk-Tightened Sufficient Terminal Recursive Feasibility Constraints)

Given a collection of user-defined unit vectors ${\ell_{ij}^{\text{obs}},\ell_{ij}^{\text{agt}}} \in {\mathbb{R}}^{n}$, let $\mathcal{A}_{\mathcal{O}_{j}} \triangleq {{AvoidSet}^{+}{({\mathcal{O}_{j} \oplus {({- \mathcal{A}})}})}}$ and $\mathcal{A}_{\mathcal{A}} \triangleq {{AvoidSet}^{+}{({\mathcal{A} \oplus {({- \mathcal{A}})}})}}$ denote ellipsoidal outer-approximations of the corresponding avoid sets, and $\mathcal{V} \triangleq {{ViabilitySet}{({\mathcal{K} \ominus \mathcal{A}})}}$ denote a polytope with $N_{\mathcal{V}}$ halfspace constraints, $\mathcal{V} = {\cap_{i \in {\mathbb{N}}_{\lbrack 1,N_{\mathcal{V}}\rbrack}}\left\{ {x \in {\mathbb{R}}^{n}}:{{{\underset{¯}{h}}_{i} \cdot x} \leq {\underset{¯}{g}}_{i}} \right\}}$. Then, for every $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$, is sufficient for to hold.

Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") characterizes linear constraints that are sufficient to enforce. For (25a) and (25b), the sufficient condition is obtained by tightening the complement of a supporting halfspace of the convex outer-approximations of the avoid set. For (25c), the sufficient condition utilizes Boole's inequality and uniform risk allocation.

### III-E Reformulated Risk-Tightened MPC Safety Filter

Following the reformulations discussed in Sections III-C and III-D, we obtain a quadratic program,

where ${U_{i}^{s}{(t)}} = {\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ for each $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$. uses the mean states and positions of the agents, and the deterministic linear constraints characterized in Propositions 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") for probabilistic collective safety and recursive feasibility. A solution of is a feasible (but not necessarily optimal) solution of.

From the setting of, it is evident that the specialization of the RL-based motion planner to the deterministic nominal dynamics does not affect the proposed solution adversely. Motivated by the superposition principle, we have used a simpler RL-based motion planner that considers deterministic dynamics instead of the stochastic dynamics, and delegated the responsibility of probabilistic collective safety under to the safety filter.

### III-F Discussion

### III-F1 Choice of Dynamics

Our primary targets are quadrotors as we describe in Section IV. Waypoint tracking for quadrotors using on-board controllers is now well-known. Consequently, assuming linear dynamics is appropriate since the safety filter can generate safe waypoints that deviates minimally from the RL-based motion plan.

Theoretically, it is possible to apply the proposed solution to nonlinear dynamics. However, the construction of terminal sets for collision avoidance and recursive feasibility, similar to the sets proposed in Section III-D, become more challenging On the other hand, our approach achieves recursive feasibility in the presence of stochastic process noises. Using process noise to (conservatively) model the linearization error when using linear models for nonlinear dynamics, we can use the proposed approach to provide (conservative) safety guarantees.

### III-F2 Gaussian Noise Assumption

In our problem statement, we assumed Gaussian noise and imposed chance constraints. Alternatively, we can use other risk metrics based on axiomatic risk theory and more generalized noise distributions. However, most of these approaches either do not admit closed-form deterministic reformulations resulting in high computational costs, or are overly conservative. For example, our assumptions on $\mathbf{w}$ and $\mathbf{η}$ having a Gaussian distribution can be relaxed to any probability distribution that has a pre-specified mean and covariance. In this case, the reformulated constraints are similar to and but with $\Phi^{- 1}{(\alpha)}$ terms replaced by the Chebychev bound $\sqrt{\frac{1 - \alpha}{\alpha}}$. However, the resulting deterministic sufficient conditions are far more conservative than those in Propositions 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") \[53, Fig. 2\].

### III-F3 Ellipsoidal Convex Set Usage

We recommend using ellipsoidal representations (or outer-approximations) for various convex sets, primarily due to the convexification step presented in Section III-D. Ellipsoids ${\mathcal{E}{(c,Q)}} = \left. \{ x \middle| {{{({x - c})} \cdot {({Q^{- 1}{({x - c})}})}} \leq 1}\} \right.$ admit a closed form solution for the support function ${\rho_{\mathcal{E}{(c,Q)}}{(\ell)}} = {{\ell \cdot c} + \sqrt{\ell \cdot {({Q\ell})}}}$, and the supporting hyperplane changes smoothly along the set boundary with changing $\ell$. Compared to that, the support function of a polytope requires solving a linear program, and may change abruptly when changing $\ell$.

### III-F4 Safety Filtering with Other Motion Planners

We use the proposed safety filter in conjunction with single-agent RL motion planning, since RL-based planners have become popular in recent literature (see discussion in Section I) but lack safety guarantees especially in terms of enforcing (hard) constraints. While the proposed combination of RL and safety filter can provide hard constraint satisfaction guarantees, the safety filter's applicability is not limited to single-agent RL-based planners. As illustrated in Figure 2 and as seen from the derivations, the safety filter only requires the agents' reference state and control trajectories. These inputs may also be obtained from many other planners, including more traditional ones such as sampling-based. For example, RRT-based planners can be used for single-agent motion planning while avoiding static obstacles in the environment. The multi-agent plans can then be obtained by combining separate single-agent RRT-based plans using the proposed safety filter to guarantee inter-agent collision avoidance. This allows more efficient computations and memory reduction with respect to applying sampling-based planning to the multi-agent problem due to the smaller dimension and reduced number of collisions to be checked.

### III-F5 Intermediate multi-agent RL-based planners

The proposed approach can also be applied to the intermediate case of a planner for multiple agents $N_{\text{few}}$, but less than the total number $N$. In this case, multiple planners generate plans each for $N_{\text{few}}$ agents up to the total number $N$. Each group of $N_{\text{few}}$ may be collision-free, but the safety filter is applied to ensure safety between agents in different groups. Overall, the fundamental idea behind our approach is to take a challenging motion planning problem, approximate it by a problem that is significantly simpler to solve, at the price of losing safety due to the approximation, and then recovering it by the safety filter. In the case of multi-agent planning, approximation is done by reducing the amount of agents, hence here we discussed the largest possible reduction that provides the largest simplification, that is only one agent is considered in planning, but the approach will also work for any intermediate case.

## Implementation Details and Experiment Setup

Dynamics: We used the Crazyflie 2.1 quadrotors as our target platform. We flew all the quadrotors at the same height of $0.95$ m to make the collision avoidance problem more challenging. While it would be possible to resolve collisions by flying the drones at different heights, this solution does not generalize to other systems where more spatial dimensions do not exist (e.g. ground robots), and would not scale well to increasing number of robots or physically constrained environments.

We approximated the 2D motion of the quadrotors using 2D double integrator dynamics, and thus, $A,B,C$ are given by

with sampling time $T_{s} = 0.1$. We model the quadrotors as circles ($\mathcal{A}$ is a circle of radius $r_{A} = 0.1$) to include the $0.092$ m Crazyflie diameter as well as leave extra margin for aerodynamic effects and a safety padding.

Hardware setup: We used six quadrotors ($N = 6$) in our experiments. We relied on the Crazyswarm platform to communicate and control the quadrotors at 10Hz. The drones are equipped with IR-reflective markers detected by an OptiTrack motion capture system running at 120Hz. The Crazyswarm package tracked the Crazyflies using the raw point-cloud data from the OptiTrack motion capture system, and it issued desired waypoints at a nominal $10$ Hz update frequency over radio. The Crazyflies tracked those waypoints using their standard on-board controllers. In addition to the uncertainty in the Crazyflie position estimate induced by the Crazyswarm tracking algorithm, we added a position estimation noise $\mathbf{η}$ defined in. Such measurement noises affects the safety filter, but is not visualized in the plotted physical experiment trajectories.

Workspace: We considered a $3 \times 3$ meter workspace with seven circular obstacles and two goal regions. The obstacles are depicted by black circles and the goal regions are depicted by transparent circles with a star at the center (see Figure 7). We also added position estimation noise to the nominal obstacle locations.

Safety filter parameters: We used Gaussian noise with the following covariances: $\Sigma_{w} = \Sigma_{\eta} = {{diag}{(10^{- 4},0,10^{- 4},0)}}$ and $\Sigma_{c_{j}} = {{diag}{(10^{- 4},10^{- 4})}{\forall j}} \in {\mathbb{N}}_{\lbrack 1,N_{O}\rbrack}$. As for the risk bounds, we used $\kappa_{i} = \alpha_{i,j} = \beta_{i,i^{\prime}} = 0.01$ and divided them equally across the planning horizon $T = 10$. We used $\delta = 0.1$ for the terminal constraints. For the purposes of constructing the terminal sets, we select velocity bounds of $1$ m/s in the simulation, and $0.2$ m/s in the experiments.

Computer setup: We used an Ubuntu 20.04 LTS workstation with an AMD Ryzen 9 9590X 16-core CPU, a Nvidia GeForce GTX TITAN Black GPU, and 128GB of RAM for all training, simulation, and hardware experiments.

RL training: We used Stable-Baselines3's implementation of the PPO (proximal policy optimization) algorithm to train the RL agents. We ran two training sessions, one for each goal, for $10$ million time steps each. We used the default parameters of Stable-Baselines3 with the following modifications: $0.01$ entropy coefficient, $2021$ seed, and cpu device. We use ${\zeta_{\text{obs}} = {- 0.001}},{{\zeta_{\text{tgt}} = {- 0.1}},{{R_{\text{target}} = 10^{4}},{P_{\text{keep-in}} = {- 10^{4}}}}}$, and $P_{\text{obstacle}} = {- 500}$ for the reward function parameters.

After training, we selected the trained policy at about $9.7$ million steps and $9.44$ million steps for the two targets respectively. Each training session took just over $11$ hours.

Choice of unit vectors in Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"), 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning"): Inspired by, we used the following unit vectors:

$z_{ij}^{\text{obs}}{(\left. k \middle| t \right.)}$ ${\triangleq \frac{{p_{i}^{\text{RL}}{(\left. k \middle| t \right.)}} - {\overline{c}}_{j}}{\parallel p_{i}^{\text{RL}}{(k|t)} - {\overline{c}}_{j} \parallel}},{{z_{ij}^{\text{agt}}{(\left. k \middle| t \right.)}} \triangleq \frac{{p_{i}^{\text{RL}}{(\left. k \middle| t \right.)}} - {p_{j}^{\text{RL}}{(\left. k \middle| t \right.)}}}{\parallel p_{i}^{\text{RL}}{(k|t)} - p_{j}^{\text{RL}}{(k|t)} \parallel}}$ (38a)
$\ell_{ij}^{\text{obs}}{(\left. k \middle| t \right.)}$ ${\triangleq \frac{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}} - {\overline{c}}_{j}^{\text{lift}}}{\parallel x_{i}^{\text{RL}}{(k|t)} - {\overline{c}}_{j}^{\text{lift}} \parallel}},{{\ell_{ij}^{\text{agt}}{(\left. k \middle| t \right.)}} \triangleq \frac{{x_{i}^{\text{RL}}{(\left. k \middle| t \right.)}} - {x_{j}^{\text{RL}}{(\left. k \middle| t \right.)}}}{\parallel x_{i}^{\text{RL}}{(k|t)} - x_{j}^{\text{RL}}{(k|t)} \parallel}}$ (38b)

where ${p_{i}^{\text{RL}}{(\left. k \middle| t \right.)}} = {Cx_{i}^{\text{RL}}{(\left. k \middle| t \right.)}}$. Such a choice used the predicted RL states and positions and the nominal obstacle locations to produce a heuristic for the computation of the safe halfspace polytopes. For the 2D double integrator dynamics, the lifted state is the position vector with zeros appended for the velocity components, i.e. ${\overline{c}}_{j}^{\text{lift}} = {\lbrack{{\overline{c}}_{j}^{\top}0_{2}^{\top}}\rbrack}^{\top}$.

Solving the QP: We modeled the QP associated with the safety filter in Python 3.7 using CVXPY, utilizing parameters for values in that change at every control time step, and solved it using ECOS in experiments, and GUROBI in simulations.

## Experiments

We present results of the experimental validation of our approach on a quadrotor testbed. We show that the trained, single-agent RL-based motion planner generalizes well when used with the proposed safety filter. We also compare the proposed approach with a MPC-based multi-agent motion planner in simulation to emphasize the benefits of the RL step as well as the effects of the terminal constraints. We conclude with a demonstration of the scalability of our approach.

### V-A Experimental validation

Figure 4 shows snapshots of two experiments and their reconstructed plots. In these experiments, we compare the proposed solution with a safety-filtered baseline controller. Here, the baseline controller is a proportional controller that regulates the drones to the target while ignoring all static and dynamic obstacles, which are handled by the safety filter.

In Figure 4, the top two rows are for the proposed solution with the RL controller and the proposed safety filter while the bottom two rows use the baseline controller instead of the RL controller. In both cases, the proposed safety filter ensures that the agents remain safe. In the RL case, the agents manage to reach their goals more rapidly, while the baseline controller case, the agents take significantly longer to reach their goals. In fact, when using the baseline controller instead of the RL controller, we found that the pink agent typically gets stuck between two obstacles and fails to reach its goal (see the bottom two rows of Figure 4).

Figure 4: Safe multi-agent motion planning using the proposed safety filter in conjunction with the RL-based controller and a classical proportional controller (baseline). (Top two rows) Snapshots and reconstructed illustrations of the hardware experiment’s trajectories when using the RL-based controller with the safety filter at 7, 14, and 21 seconds. (Bottom two rows) Trajectories of the hardware experiment when using the baseline controller with the safety filter at times 13, 21, and 70 seconds. The black circles and boundary are the obstacles and keep-in set. Transparent starred circles depict the targets. Colored circles denote the agents’ starting and goal positions. The colored paths indicate the trajectory and the shaded regions are the static obstacle-free positions at the current control time step (determined via convexification).

Figure 5: Clearance between the agents during the physical experiment with RL controller, where a clearance (distance to collision) accounts for the physical dimensions of the agents. A negative clearance indicates a collision. Stars indicate one of the two agents reaching the target.

Figure 5 shows the clearances between each agent ($15$ pairs for the six agents) during the physical experiment. Specifically, it plots the inter-agent distances *minus* twice the agent radius, i.e. ${{{\|{{p_{i}{(t)}} - {p_{j}{(t)}}}\|} - {2r{\forall i}}},j,i} \neq j$. Thus, a negative distance indicates a collision. Due to the use of probabilistic constraints, the distances are always positive, which shows that the system is collectively safe.

Figure 6 shows the QP setup time (blue) and the total time for setting up and solving the QP (orange) over the RL experiment's duration. The total time spent setting up and solving for six agents was on average $0.05$ seconds. Since the time spent was always less than $0.06$ seconds, we had a sufficient margin to the $0.1$ control sampling period.

Figure 6: Problem setup and solution durations to solve the quadratic program in the experiment using CVXPY and ECOS.

Figure 7 shows the reconstruction of the agent trajectories for both the RL and baseline controllers based on the data collected during the experiments. As expected, the final trajectories for both RL and baseline controllers remain sufficiently far from the obstacles and the keep-in set bounds. While avoiding the red padding, which represents the enlargement of the obstacle rigid body by the agent's radius, is sufficient for collision avoidance, the chance constraints prevent the trajectories from getting too close and hence result in the additional virtual padding around the obstacles.

Figure 7: Reconstruction of the RL (left) and baseline (right) trajectories from the experiments. The red padding around the keep-in set and obstacles, representing the agent radius, is never crossed and hence all trajectories are safe.

### V-B Evaluation of the RL motion planner

The deterministic evaluation of the learned policy over a $100 \times 100$ grid is presented in Figure 8 (top row).

We observe that the RL agents learned to navigate to the goal starting from most initial conditions. As expected, the learned policy is not perfect and sometimes results in collisions with the obstacles or the workspace (Rows $1$ and $3$). Nevertheless, the combination of RL and the safety filter ensures safe motion planning (Rows $2$ and $4$). For less than $2\%$ of the initial conditions, the RL policy did not reach the target within $800$ time steps ($80$ s), which we mark as "loiter", i.e., static/dynamic deadlock, but safety was still guaranteed. In practice, it is usually possible to recover from such deadlock conditions by small state perturbations. We plan to investigate formal methods for avoiding and recovering from such deadlocks in future studies.

Figure 8: Evaluation of the learned policy for a single agent over a 100 × 100 grid of initial positions. (Left column) policy for target 1. (Right column) policy for target 2. From top to bottom: (Row 1) RL policy, no noise; (Row 2) RL+Filter, no noise; (Row 3) RL policy, with noise; (Row 4) RL+Filter, with noise. We observe that the combination of safety filter and single-agent RL controller achieves the highest generalization, with and without noise.

Task completion time
Min. obstacle separation
Min. agent separation

Failed at control time step

TABLE I: Comparison of the proposed safety filter with a pure MPC-based motion planner. The proposed approach completes the motion planning task for more percentage of trials. We report the -percentiles of the results of the subset of 100 Monte-Carlo simulations that completed the task successfully.

### V-C Simulation study: Impact of RL and terminal constraints

Next, we compare our approach with a pure MPC-based motion planner in simulation. Specifically, we solved, where the objective (12a) is replaced with a set point regulation cost, which results in the optimization problem,

with ${U_{i}^{s}{(t)}} = {\{{u_{i}^{safe}{(\left. k \middle| t \right.)}}\}}_{k = t}^{{t + T} - 1}$ for each $i \in {\mathbb{N}}_{\lbrack 1,N\rbrack}$, pre-specified weights $\lambda_{i,t} \geq 0$ on the deviations $\parallel {\overline{p}}_{i}{(k|t)} - q_{i} \parallel^{2}$, and a penalty for inputs $\varepsilon > 0$.

Problem is a convex quadratic program, thanks to the convexification step (Propositions 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") and 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) that uses a modified version of. Recall that the constraints of included constraints and that required user-specified unit vectors $z_{ij}^{\text{obs}},z_{ij}^{\text{agt}},\ell_{ij}^{\text{obs}}$, and $\ell_{ij}^{\text{agt}}$, which were defined using the RL trajectory in. When formulating, we defined these vectors using the baseline controller trajectory instead of the RL trajectory for a fair comparison. One can view as an extension of existing single-agent motion planners under uncertainty (for example, ) for multi-agent motion planning, with the addition of terminal constraints for recursive feasibility proposed in Section III-D. Note that enables explicit coordination between agents as they move towards their goal, while the proposed safety filter only minimizes deviations from RL-based single-agent motion planners. We now study the RL block and the terminal constraints (Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) by comparing the performances of the proposed approach and a pure MPC approach, with and without terminal constraints (Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")).

Table I summarizes the performance of both the approaches in $100$ Monte-Carlo simulations. We observe that the proposed approach completed the motion planning task for a significantly larger number of simulations than a pure MPC approach ($99\%$ vs $55\%$ success), illustrating the benefits of including RL. The sources of failure in these simulations include collisions with static or dynamic obstacles (safety is enforced in probability) as well as numerical issues for the solver. For the proposed approach, the use of terminal constraints for recursive feasibility (Proposition 2. ‣ III-D Ensuring recursive feasibility using reachability ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) typically resulted in a larger minimum separation between agents and obstacles, and among agents. The use of terminal constraints also led to smaller task completion time, possibly due to the larger minimum separations. On the other hand, the use of similar terminal constraints in the MPC approach made the problem considerably harder and led to numerical issues in all trials, possibly because the trajectory of the baseline controller may not be as informative as the RL trajectory for the convexification step. Finally, we observe that the proposed approach takes longer to complete the motion planning task than the pure MPC approach without the terminal constraints, when the latter does not result in safety violations. This is expected since the terminal constraints impose additional restriction on the generated trajectory to achieve recursive feasibility. The single agent motion planner combined with safety filter is suboptimal when applied to a multi-agent motion planning problem and is more conservative due to the terminal constraints, but guarantees safety. Thus, there is a trade-off between safety and performance.

### V-D Scalability study of the proposed approach

Figure 9: Computation times (in percentiles) of the safety filter show a modest increase as the number of agents increases. The computation times were collected from 1000 control time steps of the simulated workspace. We used GUROBI to solve the quadratic program.

To perform scalability analysis of the safety filter, we reduced $r_{A}$ to $0.01$, reduced the noise covariance from $10^{- 4}$ to $10^{- 6}$, and collected computational times for the safety filter for $1000$ control time steps starting from randomly initialized locations for the agents in simulation.

Figure 9 shows the computation time to solve, where the number of agents ranges from $2$ to $24$. The compute time of the safety filter increases only moderately with the number of agents, thanks to the convex quadratic program structure of. Compared to our preliminary work in the deterministic setting, needs a larger computational effort, possibly due to the larger number of decision variables and larger number of constraints. Specifically, computes time-varying control commands over the planning horizon compared to constant input approach used in, and includes additional constraints for recursive feasibility.

## Conclusion

We presented a solution for the multi-agent motion planning problem that combines reinforcement learning and constrained control. We utilize single-agent RL to train a policy for traversing a cluttered workspace while ignoring inter-agent collision avoidance, and use a real-time implementable, constrained-control-based safety filter to account for inter-agent collision avoidance and ensure probabilistic collective safety of the agents. The formulated QP includes chance constraints to achieve safety under process and measurement noise as well as probabilistic recursive feasibility constraints. We demonstrated the efficacy of our approach via numerical simulations, and validated our approach on a hardware testbed using quadrotors.

In our future work, we will investigate the application of the proposed approach in a decentralized setting, consider safe multi-agent motion planning for agents with nonlinear dynamics, and evaluate RL-based planning with a subset of the multiple agents larger than one.

Proof of Proposition 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")

Static obstacle collision avoidance ((13a) $\Rightarrow$ (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")))*:* Using computational geometry arguments, (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) is a non-convex chance constraint, and is equivalent to

To convexify it, we use a separating hyperplane for $({{{\overline{p}}_{i}{(\left. k \middle| t \right.)}} - {\overline{c}}_{j}})$ and $\mathcal{O}_{j} \oplus {({- \mathcal{A}})}$ along the direction of a user-specified direction $z_{ij}^{\text{obs}}$. Thus,

We use (15a. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) in Lemma 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") to reformulate the left hand side of the above implication to arrive at (13a). Thus, (5. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) holds, if (13a) holds.

Inter-agent collision avoidance ((13b) $\Rightarrow$ (6. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")))*:* Using arguments similar to the above with $z_{ij}^{\text{agt}},{{\overline{p}}_{j}{(\left. k \middle| t \right.)}},{\Sigma_{p_{j}}{(\left. k \middle| t \right.)}}$ instead of $z_{ij}^{\text{obs}},{\overline{c}}_{j},\Sigma_{c_{j}}$, we can show that (6. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) holds, if (13b) holds.

Keep-in constraint ((13c) $\Rightarrow$ (7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")))*:* From the definition of Pontryagin difference, (7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) is equivalent to

Here, $\mathcal{K} \ominus \mathcal{A}$ is easy to compute \[37, Thm 2.3\]. Specifically, ${\mathcal{K} \ominus \mathcal{A}} = {\cap_{i \in {\mathbb{N}}_{\lbrack 1,N_{\mathcal{K}}\rbrack}}{\{ p:{{h_{i} \cdot p} \leq {g_{i} - {S_{\mathcal{A}}{(h_{i})}}}}\}}}$. Using Boole's inequality and assuming that the risk bound is divided equally across all halfspaces, we have

We use (15b. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) in Lemma 1. ‣ III-C Convexified constraints for probabilistic collective safety ‣ III Proposed Solution ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning") to reformulate the left hand side of the above implication to arrive at (13c). Thus, (7. ‣ II-A Safe multi-agent motion planning under uncertainty ‣ II Problem formulation ‣ Safe multi-agent motion planning under uncertainty for drones using filtered reinforcement learning")) holds, if (13c) holds. ∎
