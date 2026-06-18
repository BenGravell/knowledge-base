<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MPPI-IPDDP: Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots

Topics include Trajectory optimization, Model predictive path integral control, Differential dynamic programming, Interior point, Collision avoidance, Hybrid trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Hybrid method combining MPPI for global, collision-free trajectory generation with Interior Point DDP (IPDDP) for smooth, dynamically optimal local refinement, leveraging the complementary strengths of sampling and gradient-based trajectory optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a hybrid trajectory optimization method designed to generate collision-free, smooth trajectories for autonomous mobile robots. By combining sampling-based Model Predictive Path Integral (MPPI) control with gradient-based Interior-Point Differential Dynamic Programming (IPDDP), we leverage their respective strengths in exploration and smoothing. The proposed method, MPPI-IPDDP, involves three steps: First, MPPI control is used to generate a coarse trajectory. Second, a collision-free convex corridor is constructed. Third, IPDDP is applied to smooth the coarse trajectory, utilizing the collision-free corridor from the second step. To demonstrate the effectiveness of our approach, we apply the proposed algorithm to trajectory optimization for differential-drive wheeled mobile robots and point-mass quadrotors. In comparisons with other MPPI variants and continuous optimization-based solvers, our method shows superior performance in terms of computational robustness and trajectory smoothness.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path planning is a critical problem for autonomous vehicles and robots. Several considerations need to be addressed simultaneously in robot path planning and navigation, such as specifying mission goals, ensuring dynamic feasibility, avoiding collisions, and considering internal constraints.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based methods for path planning can explicitly handle these tasks. Two popular optimal path planning methods for autonomous robots are gradient-based and sampling-based methods. Gradient-based methods assume that the objective and constraint functions in the planning problem are differentiable, allowing for a fast, locally optimal smooth trajectory. These methods typically rely on nonlinear programming solvers such as IPOPT and SNOPT. On the other hand, sampling-based methods do not require function differentiability, making them more suitable for modeling obstacles of various shapes. Additionally, they naturally perform exploration, helping escape local optima. However, derivative-free sampling-based methods often result in coarse (e.g., zigzag) trajectories. For example, RRT-based methods can generate coarse trajectories. To balance the pros and cons of both methods, a hybrid approach combining them, as proposed, can be considered.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimization-based trajectory generation architecture known as model predictive control (MPC) has been extensively applied to robotic trajectory generation and planning problems. Deep reinforcement learning-based trajectory generation for mobile robots is another popular approach. A comparison of the continuous optimal control and reinforcement learning frameworks for trajectory generation of autonomous drone racing is provided. Combining MPC with learning schemes has drawn noticeable attention to the robotics and control community. Using the property of differential flatness, a robotic trajectory optimization problem can be converted to finite-dimensional parametric optimization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper proposes a hybrid trajectory optimization method that modularly incorporates sampling-based and gradient-based methods. Fig. illustrates the structure of the proposed collision-free smooth path planning approach. Our method generates a coarse trajectory and path corridors using sampling-based optimization via variational inference (VI). Subsequently, a smooth trajectory is obtained through gradient-based optimization via the differential dynamic programming (DDP) scheme. We assume that a collision checker is available to determine whether a collision has occurred.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Variational inference (VI) refers to a class of optimization-based approaches for approximating posterior distributions, making Bayesian inference computationally efficient and scalable. The recently proposed model predictive path integral (MPPI) is a sampling-based planning method that uses the VI framework. In essence, MPPI samples random trajectories around a nominal trajectory, assigns weights based on cost, and updates the nominal trajectory using the weighted average. In this paper, MPPI is used to generate a coarse trajectory for exploration while avoiding collisions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While methods such as RRT and dynamic programming (DP) can achieve collision-free rough trajectory planning, we select MPPI control due to its suitability for real-time trajectory generation as a local planner, whereas RRT-like methods are often used as global planners. MPPI offers significant computational efficiency, allowing it to operate in real-time, which is critical for continuous control tasks. Additionally, MPPI inherently incorporates system dynamics within its rollout-based framework, providing a more seamless integration between trajectory planning and control. In contrast, RRT-like methods, while effective for finding rough trajectories, suffer from unpredictable computation times, which pose challenges for real-time controller design. This makes MPPI a better fit for our goal of real-time, dynamically feasible trajectory generation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To smooth the coarse trajectory with gradient-based optimization, we introduce the concept of path corridors, a popular scheme in the literature. Path corridors are collections of convex collision-free regions guiding a robot toward a goal position. Unlike previous works, we use simple sampling-based VI framework to construct these corridors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve a smooth trajectory, we apply the differential dynamic programming (DDP) framework for gradient-based optimization. DDP-based approaches, including the iterative linear quadratic regulator (iLQR), have become popular for nonlinear optimal control problems and have been applied in many contexts of planning and nonlinear model predictive control for autonomous systems. DDP relies on Bellman's principle of optimality and the necessary conditions for optimal control problems, assuming all functions defined in the problem are smooth or at least twice continuously differentiable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since original DDP approaches do not consider system state and input constraints, various methods have been developed to handle constraints efficiently in DDP. The augmented Lagrangian (AL) method is used, while the Karush-Kuhn-Tucker (KKT) condition is employed. In, a method combining the AL method with the KKT condition is proposed. The interior point differential dynamic programming (IPDDP) algorithm, used in this work, is based on the KKT condition. IPDDP, summarized in Section II, incorporates all Lagrangian and barrier terms into the Q-function and solves a minimax problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hybrid Path Planning Method: A novel hybrid path planning method is proposed. This method generates collision-free smooth trajectories by integrating sampling-based trajectory optimization using Model Predictive Path Integral (MPPI) and gradient-based smooth optimization (IPDDP).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Collision-Free Convex Path Corridors: WA new method for constructing collision-free convex path corridors is introduced. This method leverages sampling-based optimization with variational inference to ensure the path is safe from obstacles.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Effectiveness Demonstration: MPPI-IPDDP is demonstrated to be effective through two numerical case studies. These studies showcase the practical applicability and performance of the method in generating feasible and smooth trajectories.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Open-Sourced Codes: The C++ and MATLAB codes for the proposed MPPI-IPDDP solver are made available as open-source. This allows readers to replicate the results presented in the paper and customize the solution for their own robotic applications.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows: Section II reviews sampling-based optimization via variational inference and IPDDP. Section III presents our path planning method, MPPI-IPDDP, for generating collision-free smooth trajectories. In Section IV, the effectiveness of the proposed MPPI-IPDDP is demonstrated through simulations in various environments and compared with other MPPI variants and NLP-based solvers. Section V discusses the remaining challenges and practical limitations. Finally, Section VI concludes the paper with suggestions for future work.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Sampling-based Optimization via Variational Inference", "weight": 1.0} -->

An optimization problem can be reformulated as an inference problem and solved using the variational inference method. To achieve this, we introduce a binary random variable $o$ that indicates optimality, where $p{({o = 1})}$ represents the probability of optimality. For simplicity, we denote this probability as $p{(o)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Sampling-based Optimization via Variational Inference", "weight": 1.0} -->

In this paper, we consider two different cases of variational inference (VI) for stochastic optimal control: VI for finite-dimensional optimization, where the decision variable is a parameter vector, and VI for trajectory optimization, where the goal is to generate an optimal trajectory for a control system. The baseline methodology for these VI approaches is based on Model Predictive Path Integral (MPPI) control, which serves as a sampling-based framework for stochastic control problems. MPPI leverages importance sampling techniques to iteratively update control policies, making it well-suited for handling the probabilistic nature of the control tasks in both finite-dimensional optimization and trajectory optimization contexts.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A1 VI for Finite-dimensional Optimization", "weight": 1.0} -->

Let $\theta$ be a vector of decision variables. For variational inference corresponding to stochastic optimization or optimal control, the goal is to find the target distribution $q^{\ast}$^11^1We will abuse the terminology of distributions (probability measure) and probability density functions. defined as

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A1 VI for Finite-dimensional Optimization", "weight": 1.0} -->

where $\delta$ is the Dirac delta function, and $N$ is the number of samples.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A1 VI for Finite-dimensional Optimization", "weight": 1.0} -->

If a normal distribution is chosen for parameterizing the policy $\pi$, then we get the closed-form solution for the optimal policy $\pi^{\ast} = {\mathcal{N}{(\mu,\Sigma)}}$ where

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A1 VI for Finite-dimensional Optimization", "weight": 1.0} -->

In this paper, this VI-based stochastic optimization method is used for constructing collision-free convex path-corridors in Section III-B.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

Let $\tau = {(X,U)}$ be a trajectory consisting of a sequence of controlled states $X = {(x_{0},\ldots,x_{T})}$ and a sequence of control inputs $U = {(u_{0},\ldots,u_{T - 1})}$ over a finite time-horizon $T$. The goal is to find the target distribution ${q^{\ast}{(\tau)}} = {p{(\left. X \middle| U \right.)}q^{\ast}{(U)}}$ where $p{(\left. X \middle| U \right.)}$

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

The closed-form solution for the above optimization is given by

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

Replacing $q$, we approximate ${\overset{\sim}{q}}^{\ast}$ with the forward KL divergence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

If the normal distribution is chosen for $\pi$, then we get the closed form solution of $\pi^{\ast} = {\mathcal{N}{(\mu,\Sigma)}}$ where

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-A2 VI for Trajectory Optimization", "weight": 1.0} -->

In this paper, this VI-based trajectory optimization is applied for MPPI to generate a locally optimal trajectory in Section III-A.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-A3 Additional Notes", "weight": 1.0} -->

One of the most common choices for the likelihood function is ${p{(\left. o \middle| \cdot \right.)}} = {\exp{({- {\gamma J{( \cdot )}}})}}$ where $J{( \cdot )}$ is a cost function and $\gamma > 0$ is known as the inverse temperature. With this likelihood function, the weight $w_{i}$ in Sections II-A1 and II-A2 can be interpreted as the likelihood ratio corresponding to the sampled candidate $\theta_{i}$ or $U_{i}$, respectively. This implies that the lower the value of $J$ the higher the likelihood of being optimal at an exponential rate.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-A3 Additional Notes", "weight": 1.0} -->

Since this sampling-based optimization scheme is iterative, the distribution $\pi$ should influence the prior $p$ in the next iteration, ensuring that $\pi$ eventually reaches a locally optimal point. In this paper, we assume normal distributions for both the prior and posterior, propagating only the mean $\mu$ while using a fixed covariance $\Sigma$. We do not perform empirical adaptation as outlined in and.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Interior Point Differential Dynamic Programming", "weight": 1.0} -->

IPDDP introduced can be used to solve a standard discrete-time optimal control problem (OCP) given as

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Interior Point Differential Dynamic Programming", "weight": 1.0} -->

where the variables $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the system state and the control input vector at time-step $t$, respectively, and $x_{init}$ is the initial condition for the control system. Let denote the decision vector as $U:=u_{0:{T - 1}} = {\lbrack u_{0}^{\top},u_{1}^{\top},\cdots,u_{T - 1}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{nT}$ that is the concatenation of sequential control inputs over a time horizon $T$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B Interior Point Differential Dynamic Programming", "weight": 1.0} -->

For notational convenience, we drop the time index $t$ in the remainder of this section, with the understanding that all functions and variables remain time-dependent.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B Interior Point Differential Dynamic Programming", "weight": 1.0} -->

where $\mu > 0$ is the barrier parameter and $y$ is the Lagrangian multiplier.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

Solving the KKT system for ${\delta u},{\delta s},{\delta y}$, we obtain

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

where the coefficient matrices and vectors are defined as

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

with the intermediate parameters and vectors

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

Here, $r_{p}$ and $r_{d}$ are known as the primal and dual residuals, respectively. The KKT variables $\delta s$ and $\delta y$ can be rewritten as

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

where the coefficients are given as

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-B1 Backward Pass", "weight": 1.0} -->

This perturbed value function $\delta V$ is recursively used for $\delta V^{\prime}$ at the next backward step.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-B2 Forward Pass", "weight": 1.0} -->

After calculating the perturbations in the backward pass, the nominal points are updated as follows: ${u\leftarrow{u + {\alpha\delta u}}},{{s\leftarrow{s + {\alpha\delta s}}},{y\leftarrow{y + {\alpha\delta y}}}}$ where $\alpha \in {(0,1\rbrack}$ represents the step size. In IPDDP, the value of $\alpha$ is determined by the filter line-search method. This method starts with a step size of 1 and reduces $\alpha$ incrementally. pdates are accepted as soon as they decrease either the cost or the violations of constraints. If no suitable $\alpha$ is found, the forward pass is terminated and deemed unsuccessful.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-B3 Convergence", "weight": 1.0} -->

The barrier parameter $\mu$ is monotonically decreased whenever the local convergence to the central path has been achieved. The criterion for the local convergence is ${\max{({\| Q_{u}\|}_{\infty},{\| r_{p}\|}_{\infty},{\| r_{d}\|}_{\infty})}} < {\kappa\mu}$ for some $\kappa > 1$. The global convergence agrees with the sufficiently small $\mu$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-B4 Regularization", "weight": 1.0} -->

To guarantee that ${\overset{\sim}{Q}}_{uu}^{- 1}$ is invertible in (II-B1), the regularization parameter $\rho \geq 0$ is added: $Q_{uu}\leftarrow{Q_{uu} + {\rho I_{m}}}$. The parameter $\rho$ increases when it is not invertible or the failure has occurred in the forward pass. If $\rho$ reaches some upper bound $\rho_{\max}$, IPDDP is terminated for failure.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Collision-free Smooth Trajectory Generation", "weight": 1.0} -->

The proposed algorithm for solving has three steps: searching for a feasible coarse trajectory using MPPI, constructing path corridors, and smoothing the coarse trajectory by IPDDP.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

We first generate a coarse trajectory using MPPI. The cost function $J$ is defined as

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

where the indicator function is defined as

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

ensuring obstacle avoidance and the sequence of the states $x_{0:T}$ are determined by the initial state $x_{0} = x_{init}$, the dynamics $x_{t + 1} = {f_{t}{(x_{t},u_{t})}}$, and the controls $U$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

To satisfy the control constraints, each $i$th sample of control sequence vector $U_{i}$ is projected onto the constraint set, i.e. $U_{i}\leftarrow{\Pi_{u}{(U_{i})}}$ where $\Pi_{u}$ is a projection operator onto the feasible set of controls $\mathcal{U} = \left. \{{u_{0:{T - 1}} \in {\mathbb{R}}^{mT}} \middle| {{g_{t}^{u}{(u_{t})}} \leq {0{\text{for all~}t}}}\} \right.$. We assume that the set $\mathcal{U}$ is compact and convex, ensuring that the projection is well-defined. This assumption allows us to leverage analytical solutions for projection, particularly in cases involving simple constraints like box constraints or second-order conic constraints.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-A Model Predictive Path Integral", "weight": 1.0} -->

With the method described in Section II-A2, locally optimal controls and corresponding states are obtained. Let ${\overline{p}}_{0:T}$ be the resulting position of a robot from MPPI.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B Path Corridors", "weight": 1.0} -->

where the indicator function for a radial collision-free corridor is defined as

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B Path Corridors", "weight": 1.0} -->

The parameters ${\lambda_{c},\lambda_{r}} > 0$ are the weights, and $r_{\max}$ is the maximum value of $r$. Although the shape of the corridors can be arbitrary, here we choose a Euclidean ball $\mathcal{B}_{r}{(c)}$ which is represented by two variables: center $c$ and radius $r$. The optimization problem is designed to enlarge the ball and have the center $c$ close to $\overline{p}$ while containing $\overline{p}$ inside the ball without intersection with obstacles. If there are no obstacles around $\overline{p}$, then the solution is $c = \overline{p}$ and $r = r_{\max}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B Path Corridors", "weight": 1.0} -->

We use the method described in Section II-A1 with $\theta = {\lbrack c^{\top},r\rbrack}^{\top}$ to solve the optimization problem at each stage of path planning to compute a sequence of collision-free corridors that are represented by $C = {\lbrack c_{0}^{\top},\ldots,c_{T - 1}^{\top}\rbrack}^{\top}$ and $R = {\lbrack r_{0},\ldots,r_{T - 1}\rbrack}^{\top}$. As in MPPI, the constraints on $r$ in can be met by projection that is defined as $r\leftarrow{\Pi_{z}{(r)}} = {\min{\{ r_{\max},{\max{\{ 0,r\}}}\}}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-C Trajectory Smoothing", "weight": 1.0} -->

where $p_{t} \in x_{t}$ is, again, the position of a robot, $(c_{t},r_{t})$ are the center and radius of the path corridor computed, and $Q$ is a weight matrix penalizing deviations from the center of the corridor. We include the constraint in the last row of to to keep a robot staying inside the collision-free corridors.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-C Trajectory Smoothing", "weight": 1.0} -->

We use IPDDP introduced in Section II-B to solve and obtain a smooth trajectory. At the time, the coarse trajectory from MPPI can be used for an initial guess, i.e., a warm start for local optimization, which can much accelerate the convergence of IPDDP.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-C Trajectory Smoothing", "weight": 1.0} -->

1:Input: initial state x0, collision checker
2:Output: locally optimal controls U*
4:while not terminated do

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-D Algorithms", "weight": 1.0} -->

Algorithm outlines the proposed trajectory optimization method, named MPPI-IPDDP, which is designed to generate collision-free, smooth trajectories. The algorithm includes three subroutines. First, MPPI employs a derivative-free variational inference approach to search for a dynamically feasible but coarse trajectory. Second, Corridor also utilizes derivative-free variational inference to construct collision-free circular corridors around the coarse trajectory. Lastly, IPDDP uses a recursive method to smooth the coarse trajectory within these corridors. As demonstrated in the supplementary video, the proposed MPPI-IPDDP method has been verified to be capable of online replanning for low-speed robots.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-D Algorithms", "weight": 1.0} -->

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

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

(a) The terminal state cost of the trajectory reduces over iterations.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

(b) The maximum value of the primal residuals approaches 0, meaning that the constraints are satisfied.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

For an example of path planning in 2D space, we consider a scenario that a differential wheeled robot arrives at a given target pose without collision. Consider the robot kinematics\

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

where ${(x_{t},y_{t})} \in {\mathbb{R}}$ are the positions of the x-axis and y-axis respectively, $\theta_{t} \in {\mathbb{R}}$ is the angle of the orientation, ${v_{t},w_{t}} \in {\mathbb{R}}$ are velocity and angular velocity respectively, and $\Delta t$ is the time interval. The vectors ${\lbrack x_{t},y_{t},\theta_{t}\rbrack}^{\top}$ and ${\lbrack v_{t},w_{t}\rbrack}^{\top}$ are states and controls respectively. We set the initial states as ${\lbrack 0,0,{\pi/2}\rbrack}^{\top}$ and sampling-time interval ${\Delta t} = 0.1$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

The constraints of the corresponding OCP for trajectory generation are defined as

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

where $\mathcal{O}$ is the set of obstacles shown in Fig. in gray. The cost functions of the corresponding OCP for trajectory generation are defined as

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

where ${\lbrack 0,6,{\pi/2}\rbrack}^{\top}$ is the target pose. The parameters for the MPPI-IPDDP method are given in Tab. I.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A Wheeled Mobile Robot", "weight": 1.0} -->

Fig. shows the processing results of generating a smooth trajectory. Fig. gives a comparison between the zigzaging controls obtained from MPPI and the smoother ones by IPDDP. Fig. shows that the cost and constraint violations reduce over MPPI-IPDDP iterations.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

(a) The terminal state cost of the trajectory reduces over iterations.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

(b) The maximum value of the primal residuals approaches 0, meaning that the constraints are satisfied.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

For an example of path planning in 3D space, we consider a scenario that a quadrotor arrives at a given target position without collision. We assume that the quadrotor can be modeled as a point mass. The kinematics is given by

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

The constraints of the corresponding OCP for trajectory generation are defined as $x_{t} \notin \mathcal{O}$ and $a_{t} \in \mathcal{K}$ with

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

where $a_{\max} = 20$ and $\theta_{\max} = 60^{\circ}$ are the maximum value of acceleration and thrust angle, respectively. This ensures the acceleration vector of the quadrotor remain within a defined conic region $\mathcal{K}$, and $\mathcal{O}$ is the set of obstacles shown in Fig. in gray.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

The cost functions of the corresponding OCP for trajectory generation are defined as

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

where ${\lbrack 0,4,2\rbrack}^{\top}$ is the target position. The parameters for the MPPI-IPDDP method are given in Tab. II.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-B Quadrotor without Attitude", "weight": 1.0} -->

Fig. illustrates the process of generating a smooth trajectory. Fig. compares the noisy control inputs generated by MPPI with the smoothed controls produced by IPDDP. Fig. demonstrates how the cost and constraint violations decrease over successive iterations of the MPPI-IPDDP method.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

Considering the same scenario of a wheeled mobile robot given in Section IV-A, we compare the proposed MPPI-IPDDP with other existing MPPI methods (vanilla MPPI, Log-MPPI and Smooth-MPPI ) in terms of the computing time and smoothness.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

At every step of open-loop trajectory generation, we defined the success condition in terms of the computing time $({\leq \tau_{\max}})$ and the distance from the target pose $x_{\text{tg}}$, $\left\| {x_{T} - x_{\text{tg}}} \right\|_{2} \leq d_{\epsilon}$ where $\tau_{\max} = {10\sec}$ and $d_{\epsilon} = 0.1$ are predefined thresholds.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

* Q1, Q2, and Q3 represent the first, second (median), and third quartiles, respectively, of the average computing time and mean squared cost (MSC), calculated from data consisting only of successful simulations.
Table III: Comparison of computing time and smoothness for different MPPI methods.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

For statistical comparisons of algorithmic performances, numerous simulations with varying parameters of MPPI algorithms were conducted. The number of MPPI samples ($N_{u}$) increased from 100 to 25600 by doubling at each step. The covariance matrix of control $\left( \Sigma_{u} \right)$ varied from $0.1I$ to $0.9I$, where $I$ is the identity matrix of a compatible dimension. Fig. shows the overall performance comparisons of four MPPI methods in terms of the success rate, computing time and trajectory smoothness with different number of samples $N_{u}$ and control covariance $\Sigma_{u}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

Based on the simulation-based statistical analysis presented in Tab. III and Fig., although the first quartile (Q1) statistics of computing time were relatively slow, our MPPI-IPDDP method outperformed the other three MPPI methods in both computing time and the smoothness of trajectory generation. This implies that while the MPPI-IPDDP may have a slower start in some cases, it ultimately provides superior performance overall, achieving faster computations and smoother trajectories compared to the alternative MPPI methods. In addition, the performance of MPPI-IPDDP is less sensitive to changes in the MPPI parameters $N_{u}$ and $\Sigma_{u}$. This means that the method is more robust and reliable across different settings of these parameters, as illustrated in Fig..

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

We also tested the proposed MPPI-IPDDP in 300 different scenarios of the BARN dataset and compared it with other MPPI methods in terms of success rate, computing time and trajectory MSC. The parameter values of $N_{u}$ and $\Sigma_{u}$ were customized for each method to optimize its performance. This extensive testing allowed us to assess the robustness and efficiency of the MPPI-IPDDP approach across a wide variety of challenging environments, ensuring that the method was evaluated under diverse conditions. The customized parameters helped each method perform at its best, providing a fair and comprehensive comparison.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

The time horizon was set to $T = 100$, the maximum velocity of $v_{t}$ was reduced to 1.0, and each state was defined as $x_{\text{init~}} = {\lbrack 1.5,0,{\pi/2}\rbrack}^{\top}$ and $x_{\text{tg}} = {\lbrack 1.5,5,{\pi/2}\rbrack}^{\top}$. We expanded the map to be ${{5m} \times 3}m$ from ${{3m} \times 3}m$ with additional free space to prevent collision in initial and finish states. The map was also inflated to account for the size of the robot. To properly correspond with the cost calculation $\mathcal{I}^{PC}{(c,r)}$ in the Corridor, a distance field was also calculated on the map.

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-C Comparative Study with Other MPPI Variants", "weight": 1.0} -->

Based on the results of the parameter variation tests, we selected the optimal parameters that yielded the best performance in terms of success rate and smoothness. The results with the BARN dataset indicate that MPPI-IPDDP can generate smooth trajectories in various environments. Although it is more time-consuming than MPPI and Log-MPPI, MPPI-IPDDP produces the smoothest trajectories while using less time compared to Smooth-MPPI.

<!-- chunk {"id": "body-0082", "role": "body", "section": "IV-D Comparative Study with NLP-based Solvers", "weight": 1.0} -->

(a) Env. 1: IPOPT fails to generate a collision-free trajectory.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IV-D Comparative Study with NLP-based Solvers", "weight": 1.0} -->

(c) Open loop control trajectories of Env. 2 in Fig 11b.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IV-D Comparative Study with NLP-based Solvers", "weight": 1.0} -->

In addition to comparisons with other MPPI variants, we also evaluated our hybrid trajectory optimization method against existing state-of-the-art (SOTA) NLP-based methods from a local planning perspective using a receding horizon scheme. Specifically, we compared our method with two baselines: IPOPT and IPDDP. For this comparison, we formulated a point-to-point 2D navigation problem for a simple unicycle model in a cluttered environment.^22^2To ensure a fair comparison, we used MATLAB for all three methods. Specifically, since IPOPT and IPDDP were implemented using a MATLAB interface, we also employed a MATLAB version of the MPPI-IPDDP algorithm instead of a C++ version. IPOPT is written in C++ and uses a MATLAB interface for problem formulation, while the MPPI-IPDDP used in the comparisons for Tab. V and Fig. is entirely implemented in MATLAB. Similarly, IPDDP is also written in MATLAB, which leads to slower execution times compared to C++ implementations.

<!-- chunk {"id": "body-0085", "role": "body", "section": "IV-D Comparative Study with NLP-based Solvers", "weight": 1.0} -->

We treated the obstacle avoidance sub-problem as a constraint for the two gradient-based solvers, considering $\mathcal{C}^{2}$ smooth ball-type obstacles. We set the same iteration limit and horizon length with random initial guesses for both solvers and our method. Simulations were conducted until the robot reached the desired position in two environments, as shown in Figs. 11a and 11b. Both figures depict closed-loop position trajectories resulting from the implementation of a receding horizon scheme. Due to the dependency of NLP-based solvers on initial guesses, the robot sometimes failed to reach the goal point. Fig. 11a illustrates that gradient-based solvers can fail in cases of conflicting gradients, whereas our method can escape these trapped situations regardless of the initial guesses.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-D Comparative Study with NLP-based Solvers", "weight": 1.0} -->

To ensure a fair evaluation of computational time and smoothness, we compared the methods in the same environment (Fig. 11b). Comparisons of the average, minimum, and maximum computing times, as well as the MSC as a smoothness index, are presented in Tab. V. We calculated the MSC for both closed-loop position trajectories and open-loop control input trajectories, particularly for angular velocity. The results show that our method is computationally stable and produces smoother control input trajectories compared to the other methods, as also illustrated in Fig. 11c.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-A Remaining Challenges", "weight": 1.0} -->

There are still several remaining issues that should be further challenged.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Real-time implementation", "weight": 1.0} -->

The proposed algorithm involves three iterative stages, making computation time demanding on a CPU. However, using a GPU for the MPPI stage to leverage massive parallel computation can significantly reduce processing time. The number of iterations needed for IPDDP is relatively low because the initial trajectory input is close to a local optimal solution.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Potential algorithmic failure in dense crowd navigation", "weight": 1.0} -->

The closer a robot is to obstacles, the higher the likelihood of failure in generating corridors. When a robot makes close contact with obstacles, it becomes challenging to sample a corridor that includes the robot but excludes the obstacle. Alternatively, a soft constraint to keep the robot inside the corridor can be adaptively relaxed by reducing the weight $\lambda_{r}$, whenever the robot gets close to an obstacle.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Planning with uncertainty", "weight": 1.0} -->

For more precise planning of safety-critical missions, uncertainties induced by modeling errors and external disturbances should be explicitly considered. In our MPPI-IPDDP framework, uncertainties could be addressed in the MPPI, Corridor, or IPDDP steps: (a) In MPPI with uncertainty, the cost evaluation of in Alg. should include a risk-sensitive term that accounts for uncertainties in dynamics and obstacles; (b) In the Corridor step with uncertainty, the cost evaluation of in Alg. should be modified to account for uncertainties in obstacle configurations; and (c) In IPDDP with uncertainty, approaches similar to those used in tube-based robust MPC and chance-constrained stochastic MPC could be employed to handle uncertainties in planning. However, this may result in conservative constraints due to increasing uncertainty propagation over the horizon.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Planning in dynamic environment", "weight": 1.0} -->

At the current stage, our focus is on single-robot trajectory optimization, not multi-robot motion planning. In the future, we plan to extend the proposed method to multi-robot trajectory optimization in both cooperative and competitive settings.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we introduced MPPI-IPDDP, a new hybrid optimization-based local path planning method designed to generate collision-free, smooth, and optimal trajectories. Through two case studies, we demonstrated the effectiveness of the proposed MPPI-IPDDP in environments with complex obstacle layouts. However, there is still room for improvement. As discussed, incorporating Stein Variational Gradient Descent (SVGD) could enhance exploration capabilities. Additionally, addressing planning under uncertainty remains a key challenge. Future work will focus on applying the MPPI-IPDDP algorithm in real-world hardware implementations and integrating it with a global planner.
