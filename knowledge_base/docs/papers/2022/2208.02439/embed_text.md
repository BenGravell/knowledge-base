## Introduction

Path planning is a critical problem for autonomous vehicles and robots. Several considerations need to be addressed simultaneously in robot path planning and navigation, such as specifying mission goals, ensuring dynamic feasibility, avoiding collisions, and considering internal constraints.

Optimization-based methods for path planning can explicitly handle these tasks. Two popular optimal path planning methods for autonomous robots are gradient-based and sampling-based methods. Gradient-based methods assume that the objective and constraint functions in the planning problem are differentiable, allowing for a fast, locally optimal smooth trajectory. These methods typically rely on nonlinear programming solvers such as IPOPT \[(https://arxiv.org/html/2208.02439v2#bib.bib1)\] and SNOPT \[(https://arxiv.org/html/2208.02439v2#bib.bib2)\]. On the other hand, sampling-based methods do not require function differentiability, making them more suitable for modeling obstacles of various shapes. Additionally, they naturally perform exploration, helping escape local optima. However, derivative-free sampling-based methods often result in coarse (e.g., zigzag) trajectories. For example, RRT-based methods can generate coarse trajectories \[(https://arxiv.org/html/2208.02439v2#bib.bib3)\]. To balance the pros and cons of both methods, a hybrid approach combining them, as proposed in \[(https://arxiv.org/html/2208.02439v2#bib.bib4)\], can be considered.

The optimization-based trajectory generation architecture known as model predictive control (MPC) has been extensively applied to robotic trajectory generation and planning problems \[(https://arxiv.org/html/2208.02439v2#bib.bib5), (https://arxiv.org/html/2208.02439v2#bib.bib6)\]. Deep reinforcement learning-based trajectory generation for mobile robots is another popular approach \[(https://arxiv.org/html/2208.02439v2#bib.bib7)\]. A comparison of the continuous optimal control and reinforcement learning frameworks for trajectory generation of autonomous drone racing is provided in \[(https://arxiv.org/html/2208.02439v2#bib.bib8)\]. Combining MPC with learning schemes has drawn noticeable attention to the robotics and control community \[(https://arxiv.org/html/2208.02439v2#bib.bib9), (https://arxiv.org/html/2208.02439v2#bib.bib10), (https://arxiv.org/html/2208.02439v2#bib.bib11)\]. Using the property of differential flatness, a robotic trajectory optimization problem can be converted to finite-dimensional parametric optimization \[(https://arxiv.org/html/2208.02439v2#bib.bib12)\].

This paper proposes a hybrid trajectory optimization method that modularly incorporates sampling-based and gradient-based methods. Fig. (https://arxiv.org/html/2208.02439v2#S1.F1 "Figure 1 ‣ I Introduction ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") illustrates the structure of the proposed collision-free smooth path planning approach. Our method generates a coarse trajectory and path corridors using sampling-based optimization via variational inference (VI). Subsequently, a smooth trajectory is obtained through gradient-based optimization via the differential dynamic programming (DDP) scheme. We assume that a collision checker is available to determine whether a collision has occurred.

Variational inference (VI) refers to a class of optimization-based approaches for approximating posterior distributions, making Bayesian inference computationally efficient and scalable \[(https://arxiv.org/html/2208.02439v2#bib.bib13), (https://arxiv.org/html/2208.02439v2#bib.bib14)\]. The recently proposed model predictive path integral (MPPI) is a sampling-based planning method that uses the VI framework \[(https://arxiv.org/html/2208.02439v2#bib.bib15), (https://arxiv.org/html/2208.02439v2#bib.bib16)\]. In essence, MPPI samples random trajectories around a nominal trajectory, assigns weights based on cost, and updates the nominal trajectory using the weighted average. In this paper, MPPI is used to generate a coarse trajectory for exploration while avoiding collisions.

While methods such as RRT and dynamic programming (DP) can achieve collision-free rough trajectory planning, we select MPPI control due to its suitability for real-time trajectory generation as a local planner, whereas RRT-like methods are often used as global planners. MPPI offers significant computational efficiency, allowing it to operate in real-time, which is critical for continuous control tasks. Additionally, MPPI inherently incorporates system dynamics within its rollout-based framework, providing a more seamless integration between trajectory planning and control. In contrast, RRT-like methods, while effective for finding rough trajectories, suffer from unpredictable computation times, which pose challenges for real-time controller design. This makes MPPI a better fit for our goal of real-time, dynamically feasible trajectory generation.

To smooth the coarse trajectory with gradient-based optimization, we introduce the concept of path corridors, a popular scheme in the literature \[(https://arxiv.org/html/2208.02439v2#bib.bib17), (https://arxiv.org/html/2208.02439v2#bib.bib4), (https://arxiv.org/html/2208.02439v2#bib.bib18)\]. Path corridors are collections of convex collision-free regions guiding a robot toward a goal position. Unlike previous works, we use simple sampling-based VI framework to construct these corridors.

To achieve a smooth trajectory, we apply the differential dynamic programming (DDP) framework for gradient-based optimization. DDP-based approaches, including the iterative linear quadratic regulator (iLQR), have become popular for nonlinear optimal control problems and have been applied in many contexts of planning and nonlinear model predictive control for autonomous systems \[(https://arxiv.org/html/2208.02439v2#bib.bib19), (https://arxiv.org/html/2208.02439v2#bib.bib20)\]. DDP relies on Bellman's principle of optimality and the necessary conditions for optimal control problems, assuming all functions defined in the problem are smooth or at least twice continuously differentiable.

Since original DDP approaches do not consider system state and input constraints, various methods have been developed to handle constraints efficiently in DDP. The augmented Lagrangian (AL) method is used in \[(https://arxiv.org/html/2208.02439v2#bib.bib21)\], while the Karush-Kuhn-Tucker (KKT) condition is employed in \[(https://arxiv.org/html/2208.02439v2#bib.bib22)\]. In \[(https://arxiv.org/html/2208.02439v2#bib.bib20)\], a method combining the AL method with the KKT condition is proposed. The interior point differential dynamic programming (IPDDP) algorithm \[(https://arxiv.org/html/2208.02439v2#bib.bib23)\], used in this work, is based on the KKT condition. IPDDP, summarized in Section [II](https://arxiv.org/html/2208.02439v2#S2 "II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"), incorporates all Lagrangian and barrier terms into the Q-function and solves a minimax problem.

Figure 1: A method for collision-free smooth path planning. The contents in the red box are subjects in this paper.

The main contributions of this paper can be summarized as follows:

Hybrid Path Planning Method: A novel hybrid path planning method is proposed. This method generates collision-free smooth trajectories by integrating sampling-based trajectory optimization using Model Predictive Path Integral (MPPI) and gradient-based smooth optimization (IPDDP).

Collision-Free Convex Path Corridors: WA new method for constructing collision-free convex path corridors is introduced. This method leverages sampling-based optimization with variational inference to ensure the path is safe from obstacles.

Effectiveness Demonstration: MPPI-IPDDP is demonstrated to be effective through two numerical case studies. These studies showcase the practical applicability and performance of the method in generating feasible and smooth trajectories.

Open-Sourced Codes: The C++ and MATLAB codes for the proposed MPPI-IPDDP solver are made available as open-source. This allows readers to replicate the results presented in the paper and customize the solution for their own robotic applications.

The remainder of this paper is organized as follows: Section [II](https://arxiv.org/html/2208.02439v2#S2 "II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") reviews sampling-based optimization via variational inference and IPDDP. Section [III](https://arxiv.org/html/2208.02439v2#S3 "III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") presents our path planning method, MPPI-IPDDP, for generating collision-free smooth trajectories. In Section [IV](https://arxiv.org/html/2208.02439v2#S4 "IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"), the effectiveness of the proposed MPPI-IPDDP is demonstrated through simulations in various environments and compared with other MPPI variants and NLP-based solvers. Section [V](https://arxiv.org/html/2208.02439v2#S5 "V Discussion and Future Work ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") discusses the remaining challenges and practical limitations. Finally, Section [VI](https://arxiv.org/html/2208.02439v2#S6 "VI Conclusions ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") concludes the paper with suggestions for future work.

## Preliminaries

### II-A Sampling-based Optimization via Variational Inference

An optimization problem can be reformulated as an inference problem and solved using the variational inference method \[(https://arxiv.org/html/2208.02439v2#bib.bib24), (https://arxiv.org/html/2208.02439v2#bib.bib25)\]. To achieve this, we introduce a binary random variable $o$ that indicates optimality, where $p{({o = 1})}$ represents the probability of optimality. For simplicity, we denote this probability as $p{(o)}$.

In this paper, we consider two different cases of variational inference (VI) for stochastic optimal control: VI for finite-dimensional optimization, where the decision variable is a parameter vector, and VI for trajectory optimization, where the goal is to generate an optimal trajectory for a control system. The baseline methodology for these VI approaches is based on Model Predictive Path Integral (MPPI) control, which serves as a sampling-based framework for stochastic control problems \[(https://arxiv.org/html/2208.02439v2#bib.bib15), (https://arxiv.org/html/2208.02439v2#bib.bib16), (https://arxiv.org/html/2208.02439v2#bib.bib26)\]. MPPI leverages importance sampling techniques to iteratively update control policies, making it well-suited for handling the probabilistic nature of the control tasks in both finite-dimensional optimization and trajectory optimization contexts.

### II-A1 VI for Finite-dimensional Optimization

Let $\theta$ be a vector of decision variables. For variational inference corresponding to stochastic optimization or optimal control, the goal is to find the target distribution $q^{\ast}$^11^1We will abuse the terminology of distributions (probability measure) and probability density functions. defined as

Let ${L{(\theta)}} = {p{(\left. o \middle| \theta \right.)}}$ be the likelihood function and ${\overset{\sim}{q}}^{\ast}$ be the empirical approximation of $q^{\ast}$ that is computed from samples ${\{\theta_{1},\ldots,\theta_{N}\}} \sim {p{(\theta)}}$ that are drawn from the prior $p{(\theta)}$. Then, ${\overset{\sim}{q}}^{\ast}$ can be represented as

where $\delta$ is the Dirac delta function, and $N$ is the number of samples. Replacing $q^{\ast}$, we approximate ${\overset{\sim}{q}}^{\ast}$ with the forward KL divergence:

If a normal distribution is chosen for parameterizing the policy $\pi$, then we get the closed-form solution for the optimal policy $\pi^{\ast} = {\mathcal{N}{(\mu,\Sigma)}}$ where

In this paper, this VI-based stochastic optimization method is used for constructing collision-free convex path-corridors in Section [III-B](https://arxiv.org/html/2208.02439v2#S3.SS2 "III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots").

### II-A2 VI for Trajectory Optimization

Let $\tau = {(X,U)}$ be a trajectory consisting of a sequence of controlled states $X = {(x_{0},\ldots,x_{T})}$ and a sequence of control inputs $U = {(u_{0},\ldots,u_{T - 1})}$ over a finite time-horizon $T$. The goal is to find the target distribution ${q^{\ast}{(\tau)}} = {p{(\left. X \middle| U \right.)}q^{\ast}{(U)}}$ where $p{(\left. X \middle| U \right.)}$ represents stochastic dynamics:

Let ${L{(U)}} = {{\mathbb{E}}_{X \sim {p{({X|U})}}}\left\lbrack {{\log p}{(\left. o \middle| \tau \right.)}} \right\rbrack}$. Then $q^{\ast}{(\tau)}$ can be rewritten as

The closed-form solution for the above optimization is given by

Let ${\overset{\sim}{q}}^{\ast}$ be the empirical distribution of $q^{\ast}$ approximated with samples ${\{ U_{1},\ldots,U_{N}\}} \sim {p{(U)}}$ drawn from the prior $p{(U)}$. Then, ${\overset{\sim}{q}}^{\ast}$ can be represented as

Replacing $q$, we approximate ${\overset{\sim}{q}}^{\ast}$ with the forward KL divergence.

If the normal distribution is chosen for $\pi$, then we get the closed form solution of $\pi^{\ast} = {\mathcal{N}{(\mu,\Sigma)}}$ where

In this paper, this VI-based trajectory optimization is applied for MPPI \[(https://arxiv.org/html/2208.02439v2#bib.bib15), (https://arxiv.org/html/2208.02439v2#bib.bib16)\] to generate a locally optimal trajectory in Section [III-A](https://arxiv.org/html/2208.02439v2#S3.SS1 "III-A Model Predictive Path Integral ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots").

### II-A3 Additional Notes

One of the most common choices for the likelihood function is ${p{(\left. o \middle| \cdot \right.)}} = {\exp{({- {\gamma J{( \cdot )}}})}}$ where $J{( \cdot )}$ is a cost function and $\gamma > 0$ is known as the inverse temperature. With this likelihood function, the weight $w_{i}$ in Sections [II-A1](https://arxiv.org/html/2208.02439v2#S2.SS1.SSS1 "II-A1 VI for Finite-dimensional Optimization ‣ II-A Sampling-based Optimization via Variational Inference ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") and [II-A2](https://arxiv.org/html/2208.02439v2#S2.SS1.SSS2 "II-A2 VI for Trajectory Optimization ‣ II-A Sampling-based Optimization via Variational Inference ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") can be interpreted as the likelihood ratio corresponding to the sampled candidate $\theta_{i}$ or $U_{i}$, respectively. This implies that the lower the value of $J$ the higher the likelihood of being optimal at an exponential rate.

Since this sampling-based optimization scheme is iterative, the distribution $\pi$ should influence the prior $p$ in the next iteration, ensuring that $\pi$ eventually reaches a locally optimal point. In this paper, we assume normal distributions for both the prior and posterior, propagating only the mean $\mu$ while using a fixed covariance $\Sigma$. We do not perform empirical adaptation as outlined in ((https://arxiv.org/html/2208.02439v2#S2.E4 "In II-A1 VI for Finite-dimensional Optimization ‣ II-A Sampling-based Optimization via Variational Inference ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) and ((https://arxiv.org/html/2208.02439v2#S2.E10 "In II-A2 VI for Trajectory Optimization ‣ II-A Sampling-based Optimization via Variational Inference ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")).

### II-B Interior Point Differential Dynamic Programming

IPDDP introduced in \[(https://arxiv.org/html/2208.02439v2#bib.bib23)\] can be used to solve a standard discrete-time optimal control problem (OCP) given as

where the variables $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the system state and the control input vector at time-step $t$, respectively, and $x_{init}$ is the initial condition for the control system. Let denote the decision vector as $U:=u_{0:{T - 1}} = {\lbrack u_{0}^{\top},u_{1}^{\top},\cdots,u_{T - 1}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{nT}$ that is the concatenation of sequential control inputs over a time horizon $T$. The real-valued functions $l_{f}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and $l_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ are the final and stage cost functions, respectively, and $f_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ defines the controlled state transitions. The vector-valued function $g_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{k}}$ defines inequality constraints where $k$ denotes the number of constraints. All functions defined in ((https://arxiv.org/html/2208.02439v2#S2.E11 "In II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) are assumed to be twice continuously differentiable.

In dynamic programming perspectives, the OCP ((https://arxiv.org/html/2208.02439v2#S2.E11 "In II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) can be converted into the Bellman equation form at time $t$ with a given state $x_{t}$ as follows:

where $V_{t + 1}$ is a value function for the next state and $s_{t} = {\lbrack s^{1},\ldots,s^{k}\rbrack}_{t}^{\top} \in {\mathbb{R}}^{k}$ are slack variables. At the final stage, the value function is defined as ${V_{T}{(x_{T})}} = {l_{f}{(x_{T})}}$.

For notational convenience, we drop the time index $t$ in the remainder of this section, with the understanding that all functions and variables remain time-dependent. The relaxed Lagrangian with the log-barrier terms of $s$ is defined by the following $Q$-function:

where $\mu > 0$ is the barrier parameter and $y$ is the Lagrangian multiplier. The relaxed value function $V{(x)}$ is defined by a saddle point of the $Q$-function:

### II-B1 Backward Pass

As in the standard DDP scheme, $Q$ is perturbed up to the quadratic terms at the current nominal points:

where $e \in {\mathbb{R}}^{k}$ is an all-ones vector and $S:={\text{diag}{(s)}} \in {\mathbb{R}}^{k \times k}$ is a diagonal matrix associated with the vector $s \in {\mathbb{R}}^{k}$. By setting ${\delta s^{\top}{({\mu S^{- 2}})}\delta s} = {\delta s^{\top}{({S^{- 1}Y})}\delta s}$ where $Y:={\text{diag}{(y)}}$, the step direction that satisfy the extremum condition corresponding to the first-order optimality is determined by the following primal-dual KKT system:

Solving the KKT system ((https://arxiv.org/html/2208.02439v2#S2.E25 "In II-B1 Backward Pass ‣ II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) for ${\delta u},{\delta s},{\delta y}$, we obtain

where the coefficient matrices and vectors are defined as

with the intermediate parameters and vectors

Here, $r_{p}$ and $r_{d}$ are known as the primal and dual residuals, respectively. The KKT variables $\delta s$ and $\delta y$ can be rewritten as

Substituting ${\delta s},{\delta y}$ above into the quadratic form $\delta Q$ in ((https://arxiv.org/html/2208.02439v2#S2.E20 "In II-B1 Backward Pass ‣ II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) and setting ${\delta s^{\top}{({\mu S^{- 2}})}\delta s} = {\delta s^{\top}{({S^{- 1}Y})}\delta s}$ result in another representation for the perturbed quadratic form:

where ${\overset{\sim}{Q}}_{x} = {Q_{x} + {Q_{xy}S^{- 1}r}}$ and ${\overset{\sim}{Q}}_{xx} = {Q_{xx} + {Q_{xy}S^{- 1}YQ_{yx}}}$.

Finally, we obtain the perturbed value function as follows:

where the coefficients are given as

This perturbed value function $\delta V$ is recursively used for $\delta V^{\prime}$ at the next backward step.

### II-B2 Forward Pass

After calculating the perturbations in the backward pass, the nominal points are updated as follows: ${u\leftarrow{u + {\alpha\delta u}}},{{s\leftarrow{s + {\alpha\delta s}}},{y\leftarrow{y + {\alpha\delta y}}}}$ where $\alpha \in {(0,1\rbrack}$ represents the step size. In IPDDP, the value of $\alpha$ is determined by the filter line-search method \[(https://arxiv.org/html/2208.02439v2#bib.bib1)\]. This method starts with a step size of 1 and reduces $\alpha$ incrementally. pdates are accepted as soon as they decrease either the cost or the violations of constraints. If no suitable $\alpha$ is found, the forward pass is terminated and deemed unsuccessful.

### II-B3 Convergence

The barrier parameter $\mu$ is monotonically decreased whenever the local convergence to the central path has been achieved. The criterion for the local convergence is ${\max{({\| Q_{u}\|}_{\infty},{\| r_{p}\|}_{\infty},{\| r_{d}\|}_{\infty})}} < {\kappa\mu}$ for some $\kappa > 1$. The global convergence agrees with the sufficiently small $\mu$.

### II-B4 Regularization

To guarantee that ${\overset{\sim}{Q}}_{uu}^{- 1}$ is invertible in ([II-B1](https://arxiv.org/html/2208.02439v2#S2.Ex2 "II-B1 Backward Pass ‣ II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")), the regularization parameter $\rho \geq 0$ is added: $Q_{uu}\leftarrow{Q_{uu} + {\rho I_{m}}}$. The parameter $\rho$ increases when it is not invertible or the failure has occurred in the forward pass. If $\rho$ reaches some upper bound $\rho_{\max}$, IPDDP is terminated for failure.

## Collision-free Smooth Trajectory Generation

This section considers the following OCP:

where the variables $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the system state and the control input vector at time-step $t$, respectively, and $x_{init}$ is the initial condition for the control system. $p_{t} \in x_{t}$ is the position of a robot, and $\mathcal{O}$ is the set of positions at which obstacles occupy. The functions $l_{f}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, $l_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$, and $f_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ are defined as ((https://arxiv.org/html/2208.02439v2#S2.E11 "In II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")). Notice that, unlike in ((https://arxiv.org/html/2208.02439v2#S2.E11 "In II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")), the joint state-control constraints ${g_{t}{(x_{t},u_{t})}} \leq 0$ are decoupled into the state constraint ${g_{t}^{x}{(x_{t})}} \leq 0$ and the input (control) constraint ${g_{t}^{u}{(u_{t})}} \leq 0$.

The proposed algorithm for solving ((https://arxiv.org/html/2208.02439v2#S3.E33 "In III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) has three steps: searching for a feasible coarse trajectory using MPPI, constructing path corridors, and smoothing the coarse trajectory by IPDDP.

### III-A Model Predictive Path Integral

We first generate a coarse trajectory using MPPI. The cost function $J$ is defined as

where the indicator function is defined as

ensuring obstacle avoidance and the sequence of the states $x_{0:T}$ are determined by the initial state $x_{0} = x_{init}$, the dynamics $x_{t + 1} = {f_{t}{(x_{t},u_{t})}}$, and the controls $U$.

To satisfy the control constraints in ((https://arxiv.org/html/2208.02439v2#S3.E33 "In III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")), each $i$th sample of control sequence vector $U_{i}$ is projected onto the constraint set, i.e. $U_{i}\leftarrow{\Pi_{u}{(U_{i})}}$ where $\Pi_{u}$ is a projection operator onto the feasible set of controls $\mathcal{U} = \left. \{{u_{0:{T - 1}} \in {\mathbb{R}}^{mT}} \middle| {{g_{t}^{u}{(u_{t})}} \leq {0{\text{for all~}t}}}\} \right.$. We assume that the set $\mathcal{U}$ is compact and convex, ensuring that the projection is well-defined. This assumption allows us to leverage analytical solutions for projection, particularly in cases involving simple constraints like box constraints or second-order conic constraints.

With the method described in Section [II-A2](https://arxiv.org/html/2208.02439v2#S2.SS1.SSS2 "II-A2 VI for Trajectory Optimization ‣ II-A Sampling-based Optimization via Variational Inference ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"), locally optimal controls and corresponding states are obtained. Let ${\overline{p}}_{0:T}$ be the resulting position of a robot from MPPI.

### III-B Path Corridors

(a) A maximally inflated path corridor

Figure 2: Schematics of for collision-free path corridors.

To construct corridors around the path ${\overline{p}}_{0:T}$, the following optimization problem is considered:

where the indicator function for a radial collision-free corridor is defined as

The parameters ${\lambda_{c},\lambda_{r}} > 0$ are the weights, and $r_{\max}$ is the maximum value of $r$. Although the shape of the corridors can be arbitrary, here we choose a Euclidean ball $\mathcal{B}_{r}{(c)}$ which is represented by two variables: center $c$ and radius $r$. The optimization problem ((https://arxiv.org/html/2208.02439v2#S3.E36 "In III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) is designed to enlarge the ball and have the center $c$ close to $\overline{p}$ while containing $\overline{p}$ inside the ball without intersection with obstacles (see Fig. (https://arxiv.org/html/2208.02439v2#S3.F2 "Figure 2 ‣ III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")). If there are no obstacles around $\overline{p}$, then the solution is $c = \overline{p}$ and $r = r_{\max}$.

We use the method described in Section [II-A1](https://arxiv.org/html/2208.02439v2#S2.SS1.SSS1 "II-A1 VI for Finite-dimensional Optimization ‣ II-A Sampling-based Optimization via Variational Inference ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") with $\theta = {\lbrack c^{\top},r\rbrack}^{\top}$ to solve the optimization problem ((https://arxiv.org/html/2208.02439v2#S3.E36 "In III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) at each stage of path planning to compute a sequence of collision-free corridors that are represented by $C = {\lbrack c_{0}^{\top},\ldots,c_{T - 1}^{\top}\rbrack}^{\top}$ and $R = {\lbrack r_{0},\ldots,r_{T - 1}\rbrack}^{\top}$. As in MPPI, the constraints on $r$ in ((https://arxiv.org/html/2208.02439v2#S3.E36 "In III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) can be met by projection that is defined as $r\leftarrow{\Pi_{z}{(r)}} = {\min{\{ r_{\max},{\max{\{ 0,r\}}}\}}}$.

### III-C Trajectory Smoothing

In our final step of trajectory optimization for path planning, we consider the following OCP for smoothing the coarse trajectory generated by MPPI:

where $p_{t} \in x_{t}$ is, again, the position of a robot, $(c_{t},r_{t})$ are the center and radius of the path corridor computed in ((https://arxiv.org/html/2208.02439v2#S3.E36 "In III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")), and $Q$ is a weight matrix penalizing deviations from the center of the corridor. We include the constraint in the last row of ((https://arxiv.org/html/2208.02439v2#S3.E38 "In III-C Trajectory Smoothing ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) to to keep a robot staying inside the collision-free corridors.

We use IPDDP introduced in Section [II-B](https://arxiv.org/html/2208.02439v2#S2.SS2 "II-B Interior Point Differential Dynamic Programming ‣ II Preliminaries ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") to solve ((https://arxiv.org/html/2208.02439v2#S3.E38 "In III-C Trajectory Smoothing ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) and obtain a smooth trajectory. At the time, the coarse trajectory from MPPI can be used for an initial guess, i.e., a warm start for local optimization, which can much accelerate the convergence of IPDDP.

1:Input: initial state x0, collision checker
2:Output: locally optimal controls U*
4:while not terminated do

5:$\overline{J}\leftarrow{\min_{i}J_{i}}$
10:$\overline{w}\leftarrow{\sum_{i = 1}^{N_{u}}w_{i}}$
11:$U\leftarrow{\sum_{i = 1}^{N_{u}}{\left( w_{i}/\overline{w} \right){\hat{U}}_{i}}}$

### III-D Algorithms

Algorithm (https://arxiv.org/html/2208.02439v2#alg1 "Algorithm 1 ‣ III-C Trajectory Smoothing ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") outlines the proposed trajectory optimization method, named MPPI-IPDDP, which is designed to generate collision-free, smooth trajectories. The algorithm includes three subroutines. First, MPPI employs a derivative-free variational inference approach to search for a dynamically feasible but coarse trajectory. Second, Corridor also utilizes derivative-free variational inference to construct collision-free circular corridors around the coarse trajectory. Lastly, IPDDP uses a recursive method to smooth the coarse trajectory within these corridors. As demonstrated in the supplementary video, the proposed MPPI-IPDDP method has been verified to be capable of online replanning for low-speed robots.

1:${\overline{p}}_{0:T}\leftarrow{\text{extract positions from~}X}$
2:$c_{t}\leftarrow{{\overline{p}}_{t}{\text{for every~}{t = {0,\ldots,{T - 1}}}}}$
6: while not inflated enough do
11: $\overline{J}\leftarrow{\min_{i}J_{i}}$
16: $\overline{w}\leftarrow{\sum_{i = 1}^{N_{z}}w_{i}}$
17: $z_{t}\leftarrow{\sum_{i = 1}^{N_{z}}{\left( w_{i}/\overline{w} \right){\hat{z}}_{i}}}$

1:while not converged globally and not max iteration do
2: evaluate all derivatives needed;
3: try the backwardpass; ⊳ Section II-B1
4: try the forwardpass; ⊳ Section II-B2
5: if any failures occured then ⊳ Section II-B4
6: increase the regularization parameter ρ;
8: break; ⊳ Solver failed
12: decrease the regularization parameter ρ;
13: update the nominal trajectory;
15: if locally converged then ⊳ Section II-B3
16: decrease the barrier parameter μ;
17: reinitialize the filter;

## Case Studies

### IV-A Wheeled Mobile Robot

Figure 3: The iterations of the MPPI-IPDDP algorithm for generating a collision-free path from to. In the figure, black dots represent the positions of the robot, red circles denote the path corridors, and gray areas indicate obstacles. During the early iterations, the constraints are violated (as the black dots are outside the corridors) because the IPDDP struggled with the infeasible starting point and was terminated by the user-defined maximum iteration limit, as illustrated in ①∼③. However, as the MPPI-IPDDP algorithm continues to iterate, it eventually finds the optimal collision-free trajectory, as shown in ⑧.

(a) Coarse controls by MPPI

(b) Smooth controls by IPDDP

(a) The terminal state cost of the trajectory reduces over iterations.

(b) The maximum value of the primal residuals approaches 0, meaning that the constraints are satisfied.

Figure 4: A comparison of control inputs obtained from MPPI and IPDDP.
Figure 5: Cost reduction and convergence rate over MPPI-IPDDP iterations.

For an example of path planning in 2D space, we consider a scenario that a differential wheeled robot arrives at a given target pose without collision. Consider the robot kinematics\

where ${(x_{t},y_{t})} \in {\mathbb{R}}$ are the positions of the x-axis and y-axis respectively, $\theta_{t} \in {\mathbb{R}}$ is the angle of the orientation, ${v_{t},w_{t}} \in {\mathbb{R}}$ are velocity and angular velocity respectively, and $\Delta t$ is the time interval. The vectors ${\lbrack x_{t},y_{t},\theta_{t}\rbrack}^{\top}$ and ${\lbrack v_{t},w_{t}\rbrack}^{\top}$ are states and controls respectively. We set the initial states as ${\lbrack 0,0,{\pi/2}\rbrack}^{\top}$ and sampling-time interval ${\Delta t} = 0.1$.

The constraints of the corresponding OCP for trajectory generation are defined as

where $\mathcal{O}$ is the set of obstacles shown in Fig. (https://arxiv.org/html/2208.02439v2#S4.F3 "Figure 3 ‣ IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") in gray. The cost functions of the corresponding OCP for trajectory generation are defined as

where ${\lbrack 0,6,{\pi/2}\rbrack}^{\top}$ is the target pose. The parameters for the MPPI-IPDDP method are given in Tab. [I](https://arxiv.org/html/2208.02439v2#S4.T1 "Table I ‣ IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots").

Fig. (https://arxiv.org/html/2208.02439v2#S4.F3 "Figure 3 ‣ IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") shows the processing results of generating a smooth trajectory. Fig. (https://arxiv.org/html/2208.02439v2#S4.F5 "Figure 5 ‣ IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") gives a comparison between the zigzaging controls obtained from MPPI and the smoother ones by IPDDP. Fig. (https://arxiv.org/html/2208.02439v2#S4.F5 "Figure 5 ‣ IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") shows that the cost and constraint violations reduce over MPPI-IPDDP iterations.

Table I: Parameters for trajectory optimization of a wheeled mobile robot in Section IV-A.

Table II: Parameters for trajectory optimization of a quadrator in Section IV-B.

### IV-B Quadrotor without Attitude

Figure 6: The iterations for generating an optimal collision-free path from to by MPPI-IPDDP. The black dots are position of the quadrotor, the red spheres are the path corridors, and the gray represents obstacles. The optimal trajectory passes the small hole and reaches the destination. Details can be found in accompanying video.

(a) Coarse controls by MPPI

(b) Smooth controls by IPDDP

(a) The terminal state cost of the trajectory reduces over iterations.

(b) The maximum value of the primal residuals approaches 0, meaning that the constraints are satisfied.

Figure 7: A comparison of control inputs obtained from MPPI and IPDDP.
Figure 8: Cost reduction and convergence rate over MPPI-IPDDP iterations.

For an example of path planning in 3D space, we consider a scenario that a quadrotor arrives at a given target position without collision. We assume that the quadrotor can be modeled as a point mass. The kinematics is given by

where ${x_{t},v_{t}} \in {\mathbb{R}}^{3}$ are position and velocity respectively, $a_{t} = {\lbrack a_{x,t},a_{y,t},a_{z,t}\rbrack}^{\top} \in {\mathbb{R}}^{3}$ is acceleration, $g = 9.81$ is the gravitational acceleration, and $e_{3} = {\lbrack 0,0,1\rbrack}^{\top}$ is the vector of $z$-axis. ${\lbrack x_{t}^{\top},v_{t}^{\top}\rbrack}^{\top}$ and $a_{t}$ are the state and control respectively. We set the initial state as ${\lbrack 0,0,0,0,0,0\rbrack}^{\top}$ and ${\Delta t} = 0.05$.

The constraints of the corresponding OCP for trajectory generation are defined as $x_{t} \notin \mathcal{O}$ and $a_{t} \in \mathcal{K}$ with

where $a_{\max} = 20$ and $\theta_{\max} = 60^{\circ}$ are the maximum value of acceleration and thrust angle, respectively. This ensures the acceleration vector of the quadrotor remain within a defined conic region $\mathcal{K}$, and $\mathcal{O}$ is the set of obstacles shown in Fig. (https://arxiv.org/html/2208.02439v2#S4.F6 "Figure 6 ‣ IV-B Quadrotor without Attitude ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") in gray. When the projection is performed to satisfy the conic constraint $\mathcal{K}_{2}$ in ((https://arxiv.org/html/2208.02439v2#S4.E42 "In IV-B Quadrotor without Attitude ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")), we consider the following projection operator for the second-order cone ${\overset{\sim}{\mathcal{K}}}_{2} = {\{{{(u,s)} \in {\mathbb{R}}^{m + 1}}:{{\| u\|}_{2} \leq {\kappa s}}\}}$ with $m = 3$ and $\kappa = {1/{\cos{(60^{\circ})}}} > 0$:

for $\overset{\sim}{u} = {\lbrack u^{\top},s\rbrack}^{\top} \in {\mathbb{R}}^{m + 1}$ where $u \in {\mathbb{R}}^{m}$ and $s \in {\mathbb{R}}$ are a vector of a compatible dimension and a scalar. Notice that a projection ${\overset{\sim}{u}}^{\prime} = {\lbrack u^{\prime\top},s^{\prime}\rbrack}^{\top} = {\Pi_{{\overset{\sim}{\mathcal{K}}}_{2}}{(\overset{\sim}{u})}}$ might result in $u^{\prime} \notin {\overset{\sim}{\mathcal{K}}}_{2}$ if $s^{\prime} > u_{m}^{\prime}$. To handle this, we actually introduce a slack variable $s \in {\mathbb{R}}$ and consider the constraints in an extended space: $\overset{\sim}{\mathcal{K}} = {{\overset{\sim}{\mathcal{K}}}_{1} \cap {\overset{\sim}{\mathcal{K}}}_{2} \cap {\overset{\sim}{\mathcal{K}}}_{3}} \subset {\mathbb{R}}^{m + 1}$ where ${\overset{\sim}{\mathcal{K}}}_{1} = {\{{{(u,s)} \in {\mathbb{R}}^{m + 1}}:{{\| u\|}_{2} \leq 20}\}}$ and ${\overset{\sim}{\mathcal{K}}}_{3} = {\{{{(u,s)} \in {\mathbb{R}}^{m + 1}}:{{e_{m}^{\top}u} = s}\}}$.

The cost functions of the corresponding OCP for trajectory generation are defined as

where ${\lbrack 0,4,2\rbrack}^{\top}$ is the target position. The parameters for the MPPI-IPDDP method are given in Tab. [II](https://arxiv.org/html/2208.02439v2#S4.T2 "Table II ‣ IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots").

Fig. (https://arxiv.org/html/2208.02439v2#S4.F6 "Figure 6 ‣ IV-B Quadrotor without Attitude ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") illustrates the process of generating a smooth trajectory. Fig. (https://arxiv.org/html/2208.02439v2#S4.F8 "Figure 8 ‣ IV-B Quadrotor without Attitude ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") compares the noisy control inputs generated by MPPI with the smoothed controls produced by IPDDP. Fig. (https://arxiv.org/html/2208.02439v2#S4.F8 "Figure 8 ‣ IV-B Quadrotor without Attitude ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") demonstrates how the cost and constraint violations decrease over successive iterations of the MPPI-IPDDP method.

### IV-C Comparative Study with Other MPPI Variants

Considering the same scenario of a wheeled mobile robot given in Section [IV-A](https://arxiv.org/html/2208.02439v2#S4.SS1 "IV-A Wheeled Mobile Robot ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"), we compare the proposed MPPI-IPDDP with other existing MPPI methods (vanilla MPPI \[(https://arxiv.org/html/2208.02439v2#bib.bib15)\], Log-MPPI \[(https://arxiv.org/html/2208.02439v2#bib.bib27)\] and Smooth-MPPI \[(https://arxiv.org/html/2208.02439v2#bib.bib28)\]) in terms of the computing time and smoothness.

To evaluate smoothness of generated trajectory, the following Mean Squared Curvature (MSC) was used:

At every step of open-loop trajectory generation, we defined the success condition in terms of the computing time $({\leq \tau_{\max}})$ and the distance from the target pose $x_{\text{tg}}$, $\left\| {x_{T} - x_{\text{tg}}} \right\|_{2} \leq d_{\epsilon}$ where $\tau_{\max} = {10\sec}$ and $d_{\epsilon} = 0.1$ are predefined thresholds.

(a) Average computing time

(b) Mean squared curvature

Figure 9: Performance comparisons for MPPI methods.

Avg comp time [sec]

* Q1, Q2, and Q3 represent the first, second (median), and third quartiles, respectively, of the average computing time and mean squared cost (MSC), calculated from data consisting only of successful simulations.
Table III: Comparison of computing time and smoothness for different MPPI methods.

Figure 10: Performance comparisons of the success rates, average computing time, trajectory MSC for MPPI methods.

Table IV: Performance comparison of MPPI methods in the BARN dataset.

For statistical comparisons of algorithmic performances, numerous simulations with varying parameters of MPPI algorithms were conducted. The number of MPPI samples ($N_{u}$) increased from 100 to 25600 by doubling at each step. The covariance matrix of control $\left( \Sigma_{u} \right)$ varied from $0.1I$ to $0.9I$, where $I$ is the identity matrix of a compatible dimension. Fig. (https://arxiv.org/html/2208.02439v2#S4.F10 "Figure 10 ‣ IV-C Comparative Study with Other MPPI Variants ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") shows the overall performance comparisons of four MPPI methods in terms of the success rate, computing time and trajectory smoothness with different number of samples $N_{u}$ and control covariance $\Sigma_{u}$.

Based on the simulation-based statistical analysis presented in Tab. [III](https://arxiv.org/html/2208.02439v2#S4.T3 "Table III ‣ IV-C Comparative Study with Other MPPI Variants ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") and Fig. (https://arxiv.org/html/2208.02439v2#S4.F9 "Figure 9 ‣ IV-C Comparative Study with Other MPPI Variants ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"), although the first quartile (Q1) statistics of computing time were relatively slow, our MPPI-IPDDP method outperformed the other three MPPI methods in both computing time and the smoothness of trajectory generation. This implies that while the MPPI-IPDDP may have a slower start in some cases, it ultimately provides superior performance overall, achieving faster computations and smoother trajectories compared to the alternative MPPI methods. In addition, the performance of MPPI-IPDDP is less sensitive to changes in the MPPI parameters $N_{u}$ and $\Sigma_{u}$. This means that the method is more robust and reliable across different settings of these parameters, as illustrated in Fig. (https://arxiv.org/html/2208.02439v2#S4.F10 "Figure 10 ‣ IV-C Comparative Study with Other MPPI Variants ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots").

We also tested the proposed MPPI-IPDDP in 300 different scenarios of the BARN dataset \[(https://arxiv.org/html/2208.02439v2#bib.bib29)\] and compared it with other MPPI methods in terms of success rate, computing time and trajectory MSC. The parameter values of $N_{u}$ and $\Sigma_{u}$ were customized for each method to optimize its performance. This extensive testing allowed us to assess the robustness and efficiency of the MPPI-IPDDP approach across a wide variety of challenging environments, ensuring that the method was evaluated under diverse conditions. The customized parameters helped each method perform at its best, providing a fair and comprehensive comparison.

The time horizon was set to $T = 100$, the maximum velocity of $v_{t}$ was reduced to 1.0, and each state was defined as $x_{\text{init~}} = {\lbrack 1.5,0,{\pi/2}\rbrack}^{\top}$ and $x_{\text{tg}} = {\lbrack 1.5,5,{\pi/2}\rbrack}^{\top}$. We expanded the map to be ${{5m} \times 3}m$ from ${{3m} \times 3}m$ with additional free space to prevent collision in initial and finish states. The map was also inflated to account for the size of the robot. To properly correspond with the cost calculation $\mathcal{I}^{PC}{(c,r)}$ in the Corridor, a distance field was also calculated on the map.

Based on the results of the parameter variation tests, we selected the optimal parameters that yielded the best performance in terms of success rate and smoothness. The results with the BARN dataset indicate that MPPI-IPDDP can generate smooth trajectories in various environments. Although it is more time-consuming than MPPI and Log-MPPI, MPPI-IPDDP produces the smoothest trajectories while using less time compared to Smooth-MPPI.

### IV-D Comparative Study with NLP-based Solvers

(a) Env. 1: IPOPT fails to generate a collision-free trajectory.

(b) Env. 2: All methods succeed.

(c) Open loop control trajectories of Env. 2 in Fig 11b.

Figure 11: Comparisons with continuous optimization-based solvers.

Comp time [sec]

Table V: Comparison of computing time and smoothness with NLP-based Solvers.

In addition to comparisons with other MPPI variants, we also evaluated our hybrid trajectory optimization method against existing state-of-the-art (SOTA) NLP-based methods from a local planning perspective using a receding horizon scheme. Specifically, we compared our method with two baselines: IPOPT \[(https://arxiv.org/html/2208.02439v2#bib.bib1)\] and IPDDP \[(https://arxiv.org/html/2208.02439v2#bib.bib23)\]. For this comparison, we formulated a point-to-point 2D navigation problem for a simple unicycle model in a cluttered environment.^22^2To ensure a fair comparison, we used MATLAB for all three methods. Specifically, since IPOPT \[(https://arxiv.org/html/2208.02439v2#bib.bib1)\] and IPDDP \[(https://arxiv.org/html/2208.02439v2#bib.bib23)\] were implemented using a MATLAB interface, we also employed a MATLAB version of the MPPI-IPDDP algorithm instead of a C++ version. IPOPT is written in C++ and uses a MATLAB interface for problem formulation, while the MPPI-IPDDP used in the comparisons for Tab. [V](https://arxiv.org/html/2208.02439v2#S4.T5 "Table V ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") and Fig. (https://arxiv.org/html/2208.02439v2#S4.F11 "Figure 11 ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") is entirely implemented in MATLAB. Similarly, IPDDP is also written in MATLAB, which leads to slower execution times compared to C++ implementations.

We treated the obstacle avoidance sub-problem as a constraint for the two gradient-based solvers, considering $\mathcal{C}^{2}$ smooth ball-type obstacles. We set the same iteration limit and horizon length with random initial guesses for both solvers and our method. Simulations were conducted until the robot reached the desired position in two environments, as shown in Figs. [11a](https://arxiv.org/html/2208.02439v2#S4.F11.sf1 "In Figure 11 ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") and [11b](https://arxiv.org/html/2208.02439v2#S4.F11.sf2 "In Figure 11 ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"). Both figures depict closed-loop position trajectories resulting from the implementation of a receding horizon scheme. Due to the dependency of NLP-based solvers on initial guesses, the robot sometimes failed to reach the goal point. Fig. [11a](https://arxiv.org/html/2208.02439v2#S4.F11.sf1 "In Figure 11 ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") illustrates that gradient-based solvers can fail in cases of conflicting gradients, whereas our method can escape these trapped situations regardless of the initial guesses.

To ensure a fair evaluation of computational time and smoothness, we compared the methods in the same environment (Fig. [11b](https://arxiv.org/html/2208.02439v2#S4.F11.sf2 "In Figure 11 ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")). Comparisons of the average, minimum, and maximum computing times, as well as the MSC as a smoothness index, are presented in Tab. [V](https://arxiv.org/html/2208.02439v2#S4.T5 "Table V ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots"). We calculated the MSC for both closed-loop position trajectories and open-loop control input trajectories, particularly for angular velocity. The results show that our method is computationally stable and produces smoother control input trajectories compared to the other methods, as also illustrated in Fig. [11c](https://arxiv.org/html/2208.02439v2#S4.F11.sf3 "In Figure 11 ‣ IV-D Comparative Study with NLP-based Solvers ‣ IV Case Studies ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots").

## Discussion and Future Work

### V-A Remaining Challenges

There are still several remaining issues that should be further challenged.

### Real-time implementation

The proposed algorithm involves three iterative stages, making computation time demanding on a CPU. However, using a GPU for the MPPI stage to leverage massive parallel computation can significantly reduce processing time. The number of iterations needed for IPDDP is relatively low because the initial trajectory input is close to a local optimal solution.

### Potential algorithmic failure in dense crowd navigation

The closer a robot is to obstacles, the higher the likelihood of failure in generating corridors. When a robot makes close contact with obstacles, it becomes challenging to sample a corridor that includes the robot but excludes the obstacle. Alternatively, a soft constraint to keep the robot inside the corridor can be adaptively relaxed by reducing the weight $\lambda_{r}$ in ((https://arxiv.org/html/2208.02439v2#S3.E36 "In III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")), whenever the robot gets close to an obstacle.

### Planning with uncertainty

For more precise planning of safety-critical missions, uncertainties induced by modeling errors and external disturbances should be explicitly considered. In our MPPI-IPDDP framework, uncertainties could be addressed in the MPPI, Corridor, or IPDDP steps: (a) In MPPI with uncertainty, the cost evaluation of ((https://arxiv.org/html/2208.02439v2#S3.E34 "In III-A Model Predictive Path Integral ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) in Alg. (https://arxiv.org/html/2208.02439v2#alg2 "Algorithm 2 ‣ III-C Trajectory Smoothing ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") should include a risk-sensitive term that accounts for uncertainties in dynamics and obstacles; (b) In the Corridor step with uncertainty, the cost evaluation of ((https://arxiv.org/html/2208.02439v2#S3.E36 "In III-B Path Corridors ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots")) in Alg. (https://arxiv.org/html/2208.02439v2#alg3 "Algorithm 3 ‣ III-D Algorithms ‣ III Collision-free Smooth Trajectory Generation ‣ MPPI-IPDDP: A Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots") should be modified to account for uncertainties in obstacle configurations; and (c) In IPDDP with uncertainty, approaches similar to those used in tube-based robust MPC \[(https://arxiv.org/html/2208.02439v2#bib.bib30)\] and chance-constrained stochastic MPC \[(https://arxiv.org/html/2208.02439v2#bib.bib31), (https://arxiv.org/html/2208.02439v2#bib.bib32)\] could be employed to handle uncertainties in planning. However, this may result in conservative constraints due to increasing uncertainty propagation over the horizon.

### Planning in dynamic environment

At the current stage, our focus is on single-robot trajectory optimization, not multi-robot motion planning. In the future, we plan to extend the proposed method to multi-robot trajectory optimization in both cooperative and competitive settings.

## Conclusions

In this paper, we introduced MPPI-IPDDP, a new hybrid optimization-based local path planning method designed to generate collision-free, smooth, and optimal trajectories. Through two case studies, we demonstrated the effectiveness of the proposed MPPI-IPDDP in environments with complex obstacle layouts. However, there is still room for improvement. As discussed, incorporating Stein Variational Gradient Descent (SVGD) could enhance exploration capabilities. Additionally, addressing planning under uncertainty remains a key challenge. Future work will focus on applying the MPPI-IPDDP algorithm in real-world hardware implementations and integrating it with a global planner.
