<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MPPI-IPDDP: Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots

Topics include Trajectory optimization, Model predictive path integral control, Differential dynamic programming, Interior point, Collision avoidance, Hybrid trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Hybrid method combining MPPI for global, collision-free trajectory generation with Interior Point DDP (IPDDP) for smooth, dynamically optimal local refinement, leveraging the complementary strengths of sampling and gradient-based trajectory optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a hybrid trajectory optimization method designed to generate collision-free, smooth trajectories for autonomous mobile robots. By combining sampling-based Model Predictive Path Integral (MPPI) control with gradient-based Interior-Point Differential Dynamic Programming (IPDDP), we leverage their respective strengths in exploration and smoothing. The proposed method, MPPI-IPDDP, involves three steps: First, MPPI control is used to generate a coarse trajectory. Second, a collision-free convex corridor is constructed. Third, IPDDP is applied to smooth the coarse trajectory, utilizing the collision-free corridor from the second step. To demonstrate the effectiveness of our approach, we apply the proposed algorithm to trajectory optimization for differential-drive wheeled mobile robots and point-mass quadrotors. In comparisons with other MPPI variants and continuous optimization-based solvers, our method shows superior performance in terms of computational robustness and trajectory smoothness.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path or motion planning is a highly important problems for autonomous vehicles and robots. Many need to be simultaneously considered for robot path planning and navigation. For example, specification of mission objectives, examining the dynamical feasibility of a robot, ensuring collision avoidance, and considering the internal constraints of a robot.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based methods for path planning can explicitly perform the above-mentioned tasks. The two most well-known optimal path planning methods for autonomous robots: gradient- and sampling-based methods. The former frequently assume that objective and constraint functions in a given planning problem are differentiable; however, they can rapidly provide a locally optimal smooth trajectory. Obtaining a numerical solution typically relies on nonlinear programming solvers such as IPOPT and SNOPT. In contrast, sampling-based methods do not require differentiability of functions; therefore, they are more constructive than the former methods for modeling obstacles without concern about their shapes in constrained optimization for collision-free path planning. In addition, sampling-based methods naturally perform exploration, thereby avoiding a local optimum. However, derivative-free sampling-based methods generally produce coarse (e.g., zigzag) trajectories. For example, rapidly-exploring random trees-based methods generate coarse trajectories. To mitigate these drawbacks of gradient- and sampling-based methods while maintaining the advantages, a hybrid method combining them can be considered as proposed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this study, we propose a hybrid method of trajectory optimization by modularly incorporating sampling- and gradient-based methods. Fig. 1 depicts the structure of the proposed collision-free smooth path planning method. The hybrid method presented in this study generates a coarse trajectory and path corridors by using sampling-based optimization via variational inference (VI). Subsequently, a smooth trajectory is obtained by gradient-based optimization with a differential dynamic programming (DDP) scheme. It is assumed that a collision checker is available to indicate collision occurrence in a binary form, true or false.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

VI refers to a class of optimization-based approaches of finding posterior distribution approximations of unknowns, and it makes Bayesian inference computationally efficient and scalable. Recently proposed model predictive path integral (MPPI) is a sampling-based planning method that uses a VI framework. Briefly, it samples random trajectories around a nominal trajectory and assigns weights to them in order of producing low costs. Subsequently, it updates the nominal trajectory with the weighted average. In this study, MPPI was used for generating a coarse trajectory for exploration while avoiding collision.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For smoothing the coarse trajectory with a gradient-based optimization, we introduced the concept of the path corridors, which is a well-known scheme reported in the literature. Path corridors are collections of convex collision-free regions guiding a robot toward an aimed position. In this study, unlike the investigations mentioned above, a simple sampling-based optimization method was used to construct corridors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To produce a smooth trajectory, a differential dynamic programming (DDP) framework can be applied in gradient-based optimization. DDP-based approaches, including iterative linear quadratic regulator, for nonlinear optimal control problems, have recently become commonly used in many applications of planning and nonlinear model predictive control for autonomous systems. DDP is based on Bellman's principle of optimality and the necessary condition for optimal control problem. In addition, all functions defined in the optimal control problem are assumed to be smooth or at least twice continuously differentiable.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because the original DDP approaches do not consider any constraints of the system state and inputs, many studies have been conducted to deal with constraints in DDP efficiently. The augmented Lagrangian (AL) method and the Karush-Kuhn-Tucker (KKT) condition were used in and, respectively. In, a method combining the AL method with the KKT condition was proposed. The interior point differential dynamic programming (IPDDP) algorithm, employed in the present study, is based on the KKT condition. IPDDP, which is described in Section II-B, takes all Lagrangian and barrier terms into the so-called Q-function and solves a min-max problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this study are summarized as follows: We propose a hybrid path planning method that generates collision-free smooth trajectories by combining sampling-based trajectory optimization (MPPI) and gradient-based smooth optimization (IPDDP).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a method to construct collision-free convex path corridors by sampling-based optimization using VI.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present two numerical case studies for real-time path planning by which the effectiveness of the proposed method, MPPI-IPDDP, was demonstrated in the present research.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section II reviews sampling-based optimization by VI and IPDDP. Section III describes the proposed path planning method, called MPPI-IPDDP, which produces collision-free smooth trajectories. In Section IV, two-dimensional (2D) and three-dimensional (3D) case studies are presented to show the effectiveness of the proposed method. Section V concludes the paper and suggests directions for future studies.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Sampling-based Optimization by Variational Inference", "weight": 1.0} -->

An optimization problem can be reconstructed as an inference problem, which can be solved by the VI method. To this end, in this study, a binary random variable $o$ indicating optimality was introduced where specifically, $p{({o = 1})}$ is the probability of optimality. For brevity, we write it as $p{(o)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Sampling-based Optimization by Variational Inference", "weight": 1.0} -->

We considered two different cases of VI for stochastic optimal control: VI for finite-dimensional optimization, in which the decision variable is a parameter vector, and VI for trajectory optimization, in which generating the optimal trajectory of a control system is considered.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A1 VI for Finite-dimensional Optimization", "weight": 1.0} -->

Let $\theta$ be a vector of decision variables. For VI corresponding to stochastic optimization or optimal control, the objective is to find the target distribution, $q^{\ast}$^11^1We exploited the terminologies of distributions (probability measures) and probability density functions. defined as Let ${L{(\theta)}} = {p{(\left. o \middle| \theta \right.)}}$ be the likelihood function and ${\overset{\sim}{q}}^{\ast}$ be the empirical approximation of $q^{\ast}$ that is computed from samples ${\{\theta_{1},\ldots,\theta_{N}\}} \sim {p{(\theta)}}$ drawn from prior $p{(\theta)}$. Thus, ${\overset{\sim}{q}}^{\ast}$ can be represented as where $\delta$ is the Dirac delta function and $N$ is the number of samples.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A1 VI for Finite-dimensional Optimization", "weight": 1.0} -->

Replacing $q^{\ast}$, ${\overset{\sim}{q}}^{\ast}$ is approximated using the forward Kullback-Leibler (KL) divergence as follows: If a normal distribution is chosen for parameterizing the policy, $\pi$, then a closed-form solution for the optimal policy, $\pi^{\ast} = {\mathcal{N}{(\mu,\Sigma)}}$, is obtained, where In this study, this VI-based stochastic optimization method was used for constructing collision-free convex path corridors, as described in Section III-B.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

Let $\tau = {(X,U)}$ be a trajectory consisting of a sequence of controlled states $X = {(x_{0},\ldots,x_{T})}$ and a sequence of control inputs $U = {(u_{0},\ldots,u_{T - 1})}$ over a finite time-horizon $T$. The objective is to find the target distribution, ${q^{\ast}{(\tau)}} = {p{(\left. X \middle| U \right.)}q^{\ast}{(U)}}$, where $p{(\left. X \middle| U \right.)}$ represents stochastic dynamics as follows: Let ${L{(U)}} = {{\mathbb{E}}_{X \sim {p{({X|U})}}}\left\lbrack {{\log p}{(\left. o \middle| \tau \right.)}} \right\rbrack}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

Thus, $q^{\ast}{(\tau)}$ can be rewritten as The closed-form solution for the above optimization is expressed as Let ${\overset{\sim}{q}}^{\ast}$ be the empirical distribution of $q^{\ast}$ approximated with samples ${\{ U_{1},\ldots,U_{N}\}} \sim {p{(U)}}$ drawn from prior $p{(U)}$. Thus, ${\overset{\sim}{q}}^{\ast}$ can be represented as Replacing $q$, ${\overset{\sim}{q}}^{\ast}$ is approximated with the forward KL divergence.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

If a normal distribution is chosen for $\pi$, then a closed form solution of $\pi^{\ast} = {\mathcal{N}{(\mu,\Sigma)}}$ is obtained, where In this study, this VI-based trajectory optimization method was used in MPPI to generate a locally optimal trajectory, as presented in Section III-A.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A3 Additional Notes", "weight": 1.0} -->

One of the most common choices for the likelihood function is ${p{(\left. o \middle| \cdot \right.)}} = {\exp{({- {\gammaJ{( \cdot )}}})}}$, where $J{( \cdot )}$ is the cost function and $\gamma > 0$ is known as the inverse temperature. Using this likelihood function, weight $w_{i}$, as discussed in Sections II-A1 and II-A2 can be interpreted as the likelihood ratio corresponding to the sampled candidate, $\theta_{i}$ or $U_{i}$, respectively. Specifically, a low value of $J$ implies a high likelihood of optimality at an exponential rate.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A3 Additional Notes", "weight": 1.0} -->

Because this sampling-based optimization scheme is an iterative method, the distribution, $\pi$, affects the prior, $p$, at the next iteration; therefore, $\pi$ eventually reaches a locally optimal point. In this study, we considered normal distributions for the prior and posterior, and only propagated the mean, $\mu$, and used a fixed covariance $\Sigma$ without empirical adaptation, as expressed and.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A3 Additional Notes", "weight": 1.0} -->

In, the Stein variational gradient descent (SVGD) method was proposed to directly approximate a target distribution $q^{\ast}$ by the reverse KL divergence, without using an empirical distribution ${\overset{\sim}{q}}^{\ast}$. In addition, it can deal with complex multi-modal distributions and achieve more exploration; consequently, a global optimum is more probable to be found. Although SVGD can be used as, in this study, an empirical distribution and the forward KL divergence were employed for convenience.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Interior Point Differential Dynamic Programming", "weight": 1.0} -->

IPDDP introduced in can be used to solve a standard discrete-time optimal control problem (OCP) expressed as where variables $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the system state and the control input vector at time step $t$, respectively, and $x_{init}$ is the initial condition of the control system. Let the decision vector be denoted as $U:=u_{0:{T - 1}} = {\lbrack u_{0}^{\top},u_{1}^{\top},\cdots,u_{T - 1}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{nT}$, which is a concatenation of sequential control inputs over a time horizon $T$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Interior Point Differential Dynamic Programming", "weight": 1.0} -->

In dynamic programming, the OCP can be converted into Bellman's equation form at time $t$ with a given state $x_{t}$ as follows: where $V_{t + 1}$ is a value function for the next state and $s_{t} = {\lbrack s^{1},\ldots,s^{k}\rbrack}_{t}^{\top} \in {\mathbb{R}}^{k}$ are slack variables. At the final stage, the value function is defined as ${V_{T}{(x_{T})}} = {l_{f}{(x_{T})}}$. For notational convenience, index $t$ is not shown in the remainder of this section. The relaxed Lagrangian with the log-barrier terms of $s$ is defined by the following $Q$-function: where $\mu > 0$ is the barrier parameter and $y$ is the Lagrangian multiplier.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

As in the standard DDP scheme, $Q$ is perturbed up to the quadratic terms at the current nominal points: where $e \in {\mathbb{R}}^{k}$ is an all-ones vector and $S:={\text{diag}{(s)}} \in {\mathbb{R}}^{k \times k}$ is a diagonal matrix associated with vector $s \in {\mathbb{R}}^{k}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

By setting ${\deltas^{\top}{({\muS^{- 2}})}\deltas} = {\deltas^{\top}{({S^{- 1}Y})}\deltas}$, where $Y:={\text{diag}{(y)}}$, the step direction that satisfies the extremum condition corresponding to the first-order optimality is determined using the following primal-dual KKT system as follows: Solving the KKT system expressed in for $\deltau$, $\deltas$, and $\deltay$, yields where the coefficient matrices and the vectors are defined as and the intermediate parameters and vectors are Above, $r_{p}$ and $r_{d}$ are the primal and dual residuals, respectively.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

Finally, the perturbed value function is obtained as follows: where the coefficients are This perturbed value function, $\deltaV$, is recursively used for $\deltaV'$ in the next backward step.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B2 Forward Pass", "weight": 1.0} -->

After calculating the perturbations in the backward pass, the nominal points are updated as follows: $u\leftarrow{u + {\alpha\deltau}}$, $s\leftarrow{s + {\alpha\deltas}}$, and $y\leftarrow{y + {\alpha\deltay}}$, where $\alpha \in {(0,1\rbrack}$ is the step size. In IPDDP, $\alpha$ is determined using the filter line-search method. While reducing the step size, $\alpha$, starting from $1$, the filter line-search method accepts those updates that reduce either the cost or constraint violations. If no $\alpha$ is found acceptable, the forward pass is terminated for failure.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B3 Convergence", "weight": 1.0} -->

The barrier parameter, $\mu$, is monotonically decreased whenever the local convergence to the central path is achieved. The criterion for local convergence is ${\max{({\| Q_{u}\|}_{\infty},{\| r_{p}\|}_{\infty},{\| r_{d}\|}_{\infty})}} < {\kappa\mu}$, where $\kappa > 1$. The global convergence agrees with the sufficiently small $\mu$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B4 Regularization", "weight": 1.0} -->

To guarantee that ${\overset{\sim}{Q}}_{uu}^{- 1}$ is invertible in (II-B1), regularization parameter $\rho \geq 0$ is added: $Q_{uu}\leftarrow{Q_{uu} + {\rhoI_{m}}}$. $\rho$ increases when it is not invertible or failure occurs in the forward pass. If $\rho$ reaches some upper bound $\rho_{\max}$, IPDDP is terminated for failure.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Collision-free Smooth Trajectory Generation", "weight": 1.0} -->

This study considers the following OCP associated with trajectory optimization for path planning: where $p_{t} \in x_{t}$ is the position of a robot and $\mathcal{O}$ is the set of positions occupied by obstacles. Different, the joint constraints on states and controls are decoupled. The proposed algorithm for solving has three steps: searching for a feasible coarse trajectory using MPPI, constructing path corridors, and smoothing the coarse trajectory by IPDDP.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

First, a coarse trajectory using MPPI is generated. The cost function, $J$, is defined as where the indicator function for collision avoidance is defined as and the sequence of states $x_{0:T}$ is determined by the initial state, $x_{0} = x_{init}$, dynamics $x_{t + 1} = {f{(x_{t},u_{t})}}$, and controls $U$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

To satisfy the control constraints, the samples of controls, $U_{i}$, are projected onto the constraint set, i.e. $U_{i}\leftarrow{\Pi{(U_{i})}}$, where $\Pi$ is a projection operator applied to the feasible set of controls $\left. \{{u_{0:{T - 1}} \in {\mathbb{R}}^{mT}} \middle| {{h{(u_{i})}} \leq {0{\text{for all~}i}}}\} \right.$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

Using the method described in Section II-A2, locally optimal controls and corresponding states are obtained. Let ${\overline{p}}_{0:T}$ be the resulting position of a robot obtained by MPPI.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Path Corridors", "weight": 1.0} -->

Although the shape of the corridors can be arbitrary, we selected a Euclidean ball $\mathcal{B}_{r}{(c)}$ represented by two variables: center $c$ and radius $r$. The problem as expressed in is designed to enlarge the ball and ensure the center, $c$, close to $\overline{p}$ while containing $\overline{p}$ inside the ball without intersection with obstacles (see Fig. 2). If there are no obstacles around $\overline{p}$, the optimal solutions are $c = \overline{p}$ and $r = r_{\max}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Path Corridors", "weight": 1.0} -->

The method described in Section II-A1 was used with $\theta = {\lbrack c^{\top},r\rbrack}^{\top}$ to solve the optimization problem in at each stage of the path planning to compute a sequence of collision-free corridors, which are represented by $C = {\lbrack c_{0}^{\top},\ldots,c_{T - 1}^{\top}\rbrack}^{\top}$ and $R = {\lbrack r_{0},\ldots,r_{T - 1}\rbrack}^{\top}$. As in MPPI, the constraints on $c,r$ in can be met by projection.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Path Corridors", "weight": 1.0} -->

(a) Maximally inflated path corridor Figure 2: Schematics for collision-free path corridors.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Trajectory Smoothing", "weight": 1.0} -->

In the final step of the proposed trajectory optimization for path planning, the following OCP is considered for smoothing the coarse trajectory generated by MPPI: where $p_{t} \in x_{t}$ is, again, the position of a robot, $(c_{t},r_{t})$ are the center and radius of the path corridor computed using, and $Q$ is a weight matrix penalizing the deviations from the center of a corridor. The constraint in the last row of is included to ensure the robot remains inside the collision-free corridors.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Trajectory Smoothing", "weight": 1.0} -->

IPDDP introduced in Section II-B was adopted to solve and obtain a smooth trajectory. At the time, the coarse trajectory from the MPPI can be used for the initial guess, i.e., a warm start for local optimization; this can considerably accelerate the convergence rate of IPDDP.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Algorithms", "weight": 1.0} -->

Algorithm 1 summarizes the proposed trajectory optimization method, MPPI-IPDDP, for generating collision-free smooth trajectories. The algorithm consists of three subroutines. First, MPPI uses a derivate-free VI to search a dynamically feasible but coarse trajectory. Second, Corridor also uses a derivate-free VI to construct collision-free circular corridors around the coarse trajectory. Finally, IPDDP employs a recursive method to smooth the coarse trajectory within the corridors. As demonstrated in the supplementary video available at the proposed MPPI-DDP is verified to be capable of online replanning.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D Algorithms", "weight": 1.0} -->

$\overline{J}\leftarrow{\min_{i}J_{i}}$ 15: $\overline{w}\leftarrow{\sum_{i = 1}^{N_{z}}w_{i}}$ 16: $Z\leftarrow{\sum_{i = 1}^{N_{z}}{\left(w_{i}/\overline{w} \right){\hat{Z}}_{i}}}$ 1:while not converged globally and not max iteration do 2: evaluate all derivatives needed; 3: try backwardpass; ⊳ Section II-B1 4: try forwardpass; ⊳ Section II-B2 5: if any failure occurs then ⊳ Section II-B4 6: increase regularization parameter ρ; 8: break; ⊳ Solve failed 12: decrease regularization parameter ρ; 13: update nominal trajectory; 15: if locally converged then ⊳ Section II-B3 16: decrease barrier parameter μ;

<!-- chunk {"id": "body-0044", "role": "body", "section": "Case Studies", "weight": 1.0} -->

In this section, we present two simulation results of trajectory optimization conducted to demonstrate the effectiveness of the proposed MPPI-IPDDP. The first case is of a wheeled mobile robot, and the second case considers a point-mass quadrotor.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

(a) Coarse controls by MPPI (b) Smooth controls by IPDDP (a) Cost of trajectory reduces over iterations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

(b) Maximum value of primal residual approaches zero, indicating that constraints are satisfied.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

For an example of 2D path planning, a scenario in which a differential wheeled robot arrives at a given target pose without collision was considered. The kinematic model of the robot is defined as where ${(x_{t},y_{t})} \in {\mathbb{R}}$ are the positions on the x- and y-axis respectively; $\theta_{t} \in {\mathbb{R}}$ is the angle of orientation; ${v_{t},w_{t}} \in {\mathbb{R}}$ are the velocity and angular velocity, respectively; and $\Deltat$ is the time interval. Vectors ${\lbrack x_{t},y_{t},\theta_{t}\rbrack}^{\top}$ and ${\lbrack v_{t},w_{t}\rbrack}^{\top}$ are the states and the controls, respectively.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

We set the initial states as ${\lbrack 0,0,{\pi/2}\rbrack}^{\top}$ and the sampling time interval as ${\Deltat} = 0.1$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

The constraints of the corresponding OCP for trajectory generation are defined as where $\mathcal{O}$ is the set of obstacles shown in Fig. 3 in gray. The cost functions of the corresponding OCP for trajectory generation are defined as where ${\lbrack 0,6,{\pi/2}\rbrack}^{\top}$ is the target pose. The parameters for the MPPI-IPDDP method are listed in Table I.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

Fig. 3 shows the processing results of generating a smooth trajectory. In Fig. 5, the zigzag controls obtained by MPPI and the smoother ones by IPDDP are compared. Fig. 5 shows that the cost and constraint violations reduce with increasing MPPI-IPDDP iterations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Quadrotor Without Attitude", "weight": 1.0} -->

(a) Coarse controls by MPPI (b) Smooth controls by IPDDP (a) Cost of trajectory reduces over iterations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Quadrotor Without Attitude", "weight": 1.0} -->

(b) Maximum value of primal residual approaches zero, indicating that constraints are satisfied.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Quadrotor Without Attitude", "weight": 1.0} -->

As an example of 3D path planning, a scenario in which a quadrotor arrives at a given target position without collision was considered. it was assumed that the quadrotor can be modeled as a point mass. The kinematics of the quadrotor is given by where $x_{t} \in {\mathbb{R}}^{3}$ and $v_{t} \in {\mathbb{R}}^{3}$ are the position and the velocity, respectively, $a_{t} \in {\mathbb{R}}^{3}$ is the acceleration, $g = 9.81$ is the gravitational acceleration, and $e_{3} = {\lbrack 0,0,1\rbrack}^{\top}$ is the vector of z-axis. ${\lbrack x_{t}^{\top},v_{t}^{\top}\rbrack}^{\top}$ and $a_{t}$ are the states and the controls, respectively.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Quadrotor Without Attitude", "weight": 1.0} -->

The initial state is set as ${\lbrack 0,0,0,0,0,0\rbrack}^{\top}$, and ${\Deltat} = 0.05$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Quadrotor Without Attitude", "weight": 1.0} -->

The constraints of the corresponding OCP for trajectory generation are defined as where the first two constraints represent that the acceleration of the quadrotor must be inside a cone and $\mathcal{O}$ is the set of obstacles shown in Fig. 7 in gray. When projections are performed to satisfy the conic constraint, the following projection operator was applied for obtaining a second-order cone: for $u = {\lbrack{v^{\top}s}\rbrack}^{\top}$, where $v$ and $s$ are a vector of a compatible dimension and a scalar, respectively. The cost functions of the corresponding OCP for trajectory generation are defined as where ${\lbrack 0,4,2\rbrack}^{\top}$ is the target position. The parameters for the MPPI-IPDDP method are listed in Table II.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Quadrotor Without Attitude", "weight": 1.0} -->

Fig. 6 shows the processing results of generating a smooth trajectory. Fig. 9 compares the noisy controls obtained by MPPI and the smooth ones obtained by IPDDP. Fig. 9 shows that the cost and constraint violations reduce with increasing MPPI-IPDDP iterations.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this study, we established a new optimization-based hybrid local path planning method, MPPI-IPDDP, to generate a collision-free smooth optimal trajectory for path planning. Based on two case studies of ground and aerial robot path planning, we demonstrated the effectiveness of the proposed MPPI-IPDDP, even in a 3D environment with a complex layout of obstacles, provided that an efficient collision checker is available. The proposed algorithm can be further improved. As previously mentioned, SVGD can be used for improving the exploration. Planning under uncertainty needs to be considered. Future studies will be conducted on real-world applications of the MPPI-IPDDP algorithm incorporating a global planner.
