<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safely deploying robots in uncertain and dynamic environments requires a systematic accounting of various risks, both within and across layers in an autonomy stack from perception to motion planning and control. Many widely used motion planning algorithms do not adequately incorporate inherent perception and prediction uncertainties, often ignoring them altogether or making questionable assumptions of Gaussianity. We propose a distributionally robust incremental sampling-based motion planning framework that explicitly and coherently incorporates perception and prediction uncertainties. We design output feedback policies and consider moment-based ambiguity sets of distributions to enforce probabilistic collision avoidance constraints under the worst-case distribution in the ambiguity set. Our solution approach, called Output Feedback Distributionally Robust RRT^*(OFDR-RRT^*), produces asymptotically optimal risk-bounded trajectories for robots operating in dynamic, cluttered, and uncertain environments, explicitly incorporating mapping and localization error, stochastic process disturbances, unpredictable obstacle motion, and uncertain obstacle locations. Numerical experiments illustrate the effectiveness of the proposed algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

More sophisticated motion planning and control algorithms are needed for the robots to operate in increasingly dynamic and uncertain environments to ensure safe and effective autonomous behavior. Many widely used motion planning algorithms have been developed in deterministic settings. However, since motion planning algorithms must be coupled with the outputs of inherently uncertain perception systems, there is a crucial need for more tightly coupled perception and planning frameworks that explicitly incorporate perception uncertainties.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning under uncertainty has been considered in several lines of recent research Blackmore et al.; Agha-Mohammadi et al.; Luders et al.; Blackmore et al.; Liu and Ang; Zhu and Alonso-Mora. Many approaches make questionable assumptions of Gaussianity and utilize chance constraints, ostensibly to maintain computational tractability. However, this can cause significant miscalculations of risk, and the underlying risk metrics do not necessarily possess desirable coherence properties Rockafellar; Majumdar and Pavone. The emerging area of distributionally robust optimization (DRO) shows that stochastic uncertainty can be handled in much more sophisticated ways without sacrificing computational tractability Goh and Sim; Wiesemann et al.. These approaches allow modelers to explicitly incorporate inherent ambiguity in probability distributions, rather than making overly strong structural assumptions on the distribution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditionally, the perception and planning components in a robot autonomy stack are loosely coupled, in the sense that nominal estimates from the perception system may be used for planning, while inherent perception uncertainties are usually ignored. This paradigm is inherited in part from the classical separation of estimation and control in linear systems theory. However, in the presence of uncertainties and constraints, estimation and control should *not* be separated; there are needs and opportunities to explicitly incorporate perception uncertainties into planning, both to mitigate risks of constraint violation Blackmore et al.; Florence et al.; Luders et al.; Summers; Zhu and Alonso-Mora and to actively plan paths that improve perception Costante et al..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we take steps toward a tighter integration of perception and planning in autonomous robotic systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a distributionally robust incremental sampling-based motion planning framework that explicitly and coherently incorporates perception and prediction uncertainties. Our solution approach, called Output Feedback Distributionally Robust $\text{RRT}^{\ast}$ (OFDR-$\text{RRT}^{\ast})$ (Algorithm 1), produces asymptotically optimal risk-bounded trajectories for robots operating in dynamic, cluttered, and uncertain environments, explicitly incorporating mapping and localization error, stochastic process disturbances, unpredictable obstacle motion, and uncertain obstacle locations. We design output feedback policies and consider moment-based ambiguity sets of distributions to enforce probabilistic collision avoidance constraints under the worst-case distribution in the ambiguity set (Algorithm 2).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate via numerical simulation results that it gives a more sophisticated and coherent risk quantification compared to an approach that accounts for uncertainty using Gaussian assumption, without increasing the computation complexity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. The dynamical model of the robot and the uncertainty modeling in the motion planning problem is discussed in section 2. Then, the proposed OFDR-$\text{RRT}^{\ast}$ algorithm for motion planning is explained in section 3 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints"). The simulation results using a double integrator model are then presented in section 4. The paper is finally closed in section 5 with a summary of results and with directions for the future research.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Robot & Environment Modeling", "weight": 1.0} -->

Consider a robot operating in an uncertain environment, $\mathcal{X} \subset {\mathbb{R}}^{n}$ cluttered with $n_{0}$ obstacles. We denote the set of obstacles as $\mathcal{B} = {\{ 1,\ldots,n_{0}\}}$. The robot and the obstacles are modeled as a stochastic discrete-time linear system

<!-- chunk {"id": "body-0011", "role": "body", "section": "Robot & Environment Modeling", "weight": 1.0} -->

where $x_{t} \in {\mathbb{R}}^{n}$ is the robot state at time ${t,u_{t}} \in {\mathbb{R}}^{m}$ is the input at time $t$, and $A$ and $B$ are the system dynamics matrix and input matrix, respectively. The process noise $w_{r,t} \in {\mathbb{R}}^{n}$ is a zero-mean random vector independent and identically distributed across time. The initial condition $x_{0}$ is subject to an uncertainty model, with the distribution of $x_{0}$ belonging to an ambiguity set, $P_{x_{0}} \in \mathcal{P}^{x}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Robot & Environment Modeling", "weight": 1.0} -->

Moreover, $\mathcal{O}_{i}^{0} \subset {\mathbb{R}}^{n}$ represents the shape of obstacle $i$, $c_{it} \in {\mathbb{R}}^{n}$ is a random vector that represents an uncertain obstacle location and motion, not necessarily zero-mean, with unknown distribution $P_{it}^{c} \in \mathcal{P}_{it}^{c}$, and $\oplus$ denotes set translation. The obstacles ${\mathcal{O}_{it},i} \in \mathcal{B}$ are assumed to be convex polytopes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Robot & Environment Modeling", "weight": 1.0} -->

The state $\mathcal{X}_{it}$ of obstacle $i$ is defined by a set function $\Phi:{2^{{\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{l}}$ that maps the obstacle set $\mathcal{O}_{it}$ to a finite vector describing the location, motion, and shape of each obstacle relative to the uncertain trajectory $c_{it}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

We concatenate both the robot's state and the obstacle states at time $t$ to form the environmental state

<!-- chunk {"id": "body-0015", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

where $\mathcal{X}_{\mathcal{O}_{t}} = \begin{bmatrix}
\mathcal{X}_{1t} & \mathcal{X}_{2t} & \ldots & \mathcal{X}_{n_{0}t}
\end{bmatrix}^{\top}$ represents the concatenated states of all the $n_{0}$ obstacles at time $t$. Then the dynamics of the environmental state can be written as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

where $G_{z} =$ diag$(G,I)$ and $w_{\mathcal{O},t} \in {\mathbb{R}}^{n}$ is an obstacle process noise and can be derived from $c_{it}$. The distribution $P_{w_{t}}$ of $w_{t}$ is unknown and will be assumed to belong to an ambiguity set $\mathcal{P}^{w}$ of distributions satisfying

<!-- chunk {"id": "body-0017", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

At time $t$, the state of the robot can be extracted from the environmental state $\mathcal{Z}_{t}$ as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

In an autonomous robot, the environmental state $\mathcal{Z}_{t}$ must be estimated with a perception system from noisy on-board sensor measurements. We assume that a high-level perception system, such as Semantic SLAM described in Sünderhauf et al., processes high dimensional raw data $\Theta_{t} \in {\mathbb{R}}^{N}$ to recognize obstacles and produce noisy joint measurements of their state and the robot state. In particular, we define feature vectors $\mathcal{Y}_{xt} \in {\mathbb{R}}^{r}$ and $\mathcal{Y}_{it} \in {\mathbb{R}}^{q}$ for $i \in \mathcal{B}$ obtained through

<!-- chunk {"id": "body-0019", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

where $\Upsilon_{x}:{{\mathbb{R}}^{N}\rightarrow{\mathbb{R}}^{r}}$ and $\Upsilon_{\mathcal{O}}:{{\mathbb{R}}^{N}\rightarrow{\mathbb{R}}^{qn_{0}}}$ are mappings defined by the SLAM algorithm to process the raw sensor data. We then represent these features as noisy measurements of the robot and obstacle states using an assumed linear (or linearized) output model

<!-- chunk {"id": "body-0020", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

where ${y_{t} \in {\mathbb{R}}^{p + s}},$ and ${y_{x,t} \in {\mathbb{R}}^{p}},{y_{\mathcal{O},t} \in {\mathbb{R}}^{s}}$ are the output vectors corresponding to the robot and the obstacles respectively. The matrices $C,C_{\mathcal{O}},H_{x},H_{\mathcal{O}}$ are of appropriate dimensions. The function $\mathcal{C}$ maps the feature vectors $\mathcal{Y}_{xt},\mathcal{Y}_{\mathcal{O}t}$ to produce outputs $y_{xt},y_{\mathcal{O}t}$ respectively as a linear function of the environmental state $\mathcal{Z}_{t}$ with additive measurement noises $v_{t}$ which is a zero-mean random variable.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

For simplicity, we assume that $w_{t}$ and $v_{t}$ are independent. The distribution $P_{v_{t}}$ of $v_{t}$ is assumed to belong to an ambiguity set, $\mathcal{P}^{v}$ satisfying

<!-- chunk {"id": "body-0022", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

The robot is nominally subject to constraints on the state and input of the form, ${\forall t} = {0,\ldots,{T - 1}}$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Integrated Perception & Motion Planning", "weight": 1.0} -->

where the environment $\mathcal{X} \subset {\mathbb{R}}^{n}$, and $\mathcal{U} \subset {\mathbb{R}}^{m}$ are assumed to be convex polytopes, The obstacles ${\mathcal{O}_{it},i} \in \mathcal{B}$ are described, and the operator $\backslash$ denotes set subtraction. The set $\mathcal{B}$ represent a set of $n_{0}$ obstacles in the environment to be avoided.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Distributionaly Robust Motion Planning Problem", "weight": 1.0} -->

We seek a dynamic output feedback control policy $\pi = {\lbrack\pi_{0},\ldots,\pi_{T - 1}\rbrack}$ with $u_{t} = {\pi_{t}{(y_{0:t},u_{0:{t - 1}})}}$, where $y_{0:t}$ and $u_{0:{t - 1}}$ are the output and input histories available to make control decisions at time $t$, that produces a feasible and minimum cost trajectory from an initial state $x_{0}$ to a goal set $\mathcal{X}_{goal} \subset {\mathbb{R}}^{n}$. In particular, we seek to (approximately) solve the distributionally robust constrained stochastic optimal control problem

<!-- chunk {"id": "body-0025", "role": "body", "section": "Distributionaly Robust Motion Planning Problem", "weight": 1.0} -->

where $\mathcal{P}^{\mathcal{Z}}$ is an ambiguity set of marginal state distributions and $\alpha \in {(0,0.5\rbrack}$ is a user-prescribed risk parameter. The stage cost functions $\ell_{t}{( \cdot )}$ quantify the robot's distance to the goal set and actuator effort, and are assumed to be expressed in terms of the environmental state mean ${\mathbb{E}}{\lbrack\mathcal{Z}_{t}\rbrack}$, so that all the stochasticity appears in the constraints. Two key features distinguish our problem formulation. First, the state constraints are expressed as *distributionally robust chance constraints*. This means that the nominal constraints $x_{t} \in \mathcal{X}_{t}^{\text{free}}$ are enforced with probability $\alpha$ under the worst-case distribution in the ambiguity set. Second, since information about the environmental state is obtained only from noisy measurements, we optimize over dynamic output feedback policies.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Distributionaly Robust Motion Planning Problem", "weight": 1.0} -->

Our proposed solution framework, detailed in the next section, combines a dynamic state estimator with a full-state kinodynamic motion planning under uncertainty algorithm. This combination and explicit incorporation of state estimation uncertainty into the motion planning and control takes a step toward tighter integration of perception, planning, and control, which are nearly always separated in state-of-the-art robotic systems.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Output Feedback Distributionally Robust $\\text{RRT}^{\\ast}$ (OFDR-$\\text{RRT}^{\\ast}$)", "weight": 1.0} -->

We propose to use a distributionally robust, kinodynamic variant of the $\text{RRT}^{\ast}$ motion planning algorithm with dynamic output feedback policies. $\text{RRT}^{\ast}$ adds a rewiring operation to RRT to obtain asymptotic optimality. Our proposed algorithm grows trees of state and state estimate distributions, rather than merely trees of states, and incorporates distributionally robust probabilistic constraints to build risk-constrained state trajectories and feedback policies.

<!-- chunk {"id": "body-0028", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

Sampling based motion planning algorithms require a steering law to steer the robot from a noide in the tree to a feasible sampled point in the free space. Since the environment state is not directly observed and must be estimated from noisy output measurements, our proposed steering law $\pi = {\lbrack\pi_{0},\ldots,\pi_{T - 1}\rbrack}$ with $u_{t} = {\pi_{t}{(y_{0:t},u_{0:{t - 1}})}}$ comprises a combination of dynamic state estimator and state feedback control law. Here we utilize a Kalman filter (which has been used in seminal SLAM algorithms for joint estimation of robot and environmental states Dissanayake et al. ) for state estimation together with a finite horizon optimal linear quadratic state feedback controller. It is also possible within our framework to more sophisticated estimation and control components (e.g., extended/unscented Kalman filters or particle filters and stochastic model predictive controllers), which will be explored in future work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

The output feedback control policy has the form

<!-- chunk {"id": "body-0030", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

where ${\overset{\sim}{\mathcal{Z}}}_{t}$ is the Kalman filter estimate of the environmental state, and $K_{t}$ and $k_{t}$ are linear and constant feedback gains to be derived with dynamic programming for a finite-horizon LQR problem.

<!-- chunk {"id": "body-0031", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

Kalman Filter: The Kalman filter equations with gain $\mathcal{L}_{t}$ are

<!-- chunk {"id": "body-0032", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

Together with the control law (22 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) we can write the combined dynamics for the true unknown state $\mathcal{Z}_{t}$ and the state estimate ${\overset{\sim}{\mathcal{Z}}}_{t}$ as

<!-- chunk {"id": "body-0033", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

For analysis purposes, the unknown environmental state mean and covariance can then be extracted as

<!-- chunk {"id": "body-0034", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

Optimal Finite-Horizon LQR Control: Define the error $e_{t} = {{C_{xr}{\overset{\sim}{\mathcal{Z}}}_{t}} - x_{s}}$, where $x_{s}$ represents a sample of the free space to be steered to. Then the optimal control gains in (22 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) can be obtained by minimizing the cost function

<!-- chunk {"id": "body-0035", "role": "body", "section": "LQG Control Based Steering Law", "weight": 1.0} -->

via dynamic programming with the following backward in time recursion from $t = {T,\ldots,1}$

<!-- chunk {"id": "body-0036", "role": "body", "section": "Moment-Based Ambiguity Set To Model Uncertainty", "weight": 1.0} -->

Unlike most stochastic motion planning algorithms that often assume a functional form (often Gaussian) for probability distributions to model uncertainties, we will focus here on uncertainty modeling using moment-based ambiguity sets. Based on the ambiguity sets for the primitive random variables (namely, the process noise $w$, the measurement noise $v$, and the analogous one for the initial state and state estimate $Z_{0}$), and based on the estimator and control law, the combined environmental state and state estimate and covariance propagate according to (30 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) and (31 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")). Since the primitive distributions are not assumed to be Gaussian, then neither are the marginal state and state estimate distributions distributions $P_{Z_{t}}$. The ambiguity set defining the combined environmental state and state estimate is

<!-- chunk {"id": "body-0037", "role": "body", "section": "Moment-Based Ambiguity Set To Model Uncertainty", "weight": 1.0} -->

and the ambiguity set for the true environmental state is

<!-- chunk {"id": "body-0038", "role": "body", "section": "Distributionally Robust Collision Check", "weight": 1.0} -->

The control law returned by the steering function should also satisfy the state constraints which are expressed as distributionally robust chance constraints. In particular, the nominal state constraints, ${C_{xr}\mathcal{Z}_{t}} \in \mathcal{X}_{t}^{\text{free}}$, are required to be satisfied with probability $1 - \alpha$, under the worst case probability distribution in the ambiguity set. Let the moment-based ambiguity set for obstacle motion be defined using ${\mathbf{E}{\lbrack c_{it}\rbrack}} = {\hat{c}}_{it}$ and ${\mathbf{E}{\lbrack{{({c_{it} - {\hat{c}}_{it}})}{({c_{it} - {\hat{c}}_{it}})}^{\top}}\rbrack}} = \Sigma_{it}^{c}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Distributionally Robust Collision Check", "weight": 1.0} -->

Now, under the moment-based ambiguity set defined by (40 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")), a constraint on the worst-case probability of violating the $j^{th}$ constraint of obstacle $i \in \mathcal{B}$

<!-- chunk {"id": "body-0040", "role": "body", "section": "Distributionally Robust Collision Check", "weight": 1.0} -->

is equivalent to the linear constraint on the state mean ${\hat{\mathcal{Z}}}_{t}$

<!-- chunk {"id": "body-0041", "role": "body", "section": "Distributionally Robust Collision Check", "weight": 1.0} -->

where $D_{{\hat{x}}_{t}} = {C_{xr}\Sigma_{\mathcal{Z}_{t}}C_{xr}^{\top}}$ and $\alpha_{i}$ is the user prescribed risk parameter for obstacle $i \in \mathcal{B}$. Obstacle risks are allocated such that their sum does not exceed the constraint risk $\alpha$. The scaling constant $\sqrt{\frac{1 - \alpha_{i}}{\alpha_{i}}}$ in the deterministic tightening of the nominal constraint is larger than the Gaussian one, leading to a stronger tightening that reflects the weaker assumptions about the uncertainty distributions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

The OFDR-$\text{RRT}^{\ast}$ tree expansion procedure, similar to the CC-$\text{RRT}^{\ast}$ algorithm developed in Luders et al., is presented in Algorithm 1 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints"). The OFDR-$\text{RRT}^{\ast}$ tree is denoted by $\mathcal{T}$, consisting of $|\mathcal{T}|$ nodes. Each node $N$ of the tree $\mathcal{T}$ consists of a sequence of state distributions, characterized by a distribution mean $\hat{x}$ and covariance $D$. A sequence of means and covariances is denoted by $\overline{\sigma}$ and $\overline{\Pi}$, respectively. The final mean and covariance of a node's sequence are denoted by $x{\lbrack N\rbrack}$ and $D{\lbrack N\rbrack}$, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

For the state distribution sequence $(\overline{\sigma},\overline{\Pi})$, the notation $\DeltaJ{(\overline{\sigma},\overline{\Pi})}$ denotes the cost of that sequence. If $(\overline{\sigma},\overline{\Pi})$ denotes the trajectory of node $N$ with parent $N_{parent}$, then we denote by $J{\lbrack N\rbrack}$, the entire path cost from the starting state to the terminal state of node $N$, constructed recursively as

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

In the first step, a random sample $x_{rand}$ is taken from the feasible state set, $\mathcal{X}_{t}^{\text{free}}$. Then the tree node, $N_{nearest}$ that is nearest to the sample is selected (line 3 of Algorithm 1 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) according to an optimal cost-to-go function without the obstacle constraints, in order to efficiently explore the reachable set of the dynamics and increase the likelihood of generating collision-free trajectories (similar to what is done in Frazzoli et al. ). Attempts are then made to steer the robot from the nearest tree node to the random sample using the steering law explained in subsection 3.1 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints") (line 4). The control policy obtained is then used to propagate the state mean and covariance, and the entire trajectory $(\overline{\sigma},\overline{\Pi})$ is returned by the steer function.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

Each state distribution in the trajectory is then checked for distributionally robust probabilistic constraint satisfaction given by (42 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) and further the line connecting subsequent state distributions in the trajectory are also checked for collision with the obstacle sets ${\mathcal{O}_{it},i} \in \mathcal{B}$. An outline of the DR-Feasible subroutine is shown in Algorithm 2 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints"). If the entire trajectory $(\overline{\sigma},\overline{\Pi})$ is probabilistically feasible, a new node $N_{min}$ with that distribution sequence $(\overline{\sigma},\overline{\Pi})$ is created (line 7) but not yet added to $\mathcal{T}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

Instead, nearby nodes are identified for possible connections via the NearNodes function (line 8), which returns a subset of nodes $\mathcal{N}_{near} \subseteq \mathcal{T}$, if they are within a search radius ensuring probabilistic asymptotic optimality guarantees specified in Luders et al.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

where $\mathcal{N}_{t}$ refers to the number of nodes in the tree at time $t$, $\mu_{max} > 0$ is the maximum radius specified by the user, $\gamma$ refers to the planning constant based on the $d$ dimensional environment. Then we seek to identify the lowest-cost, probabilistically feasible connection from the $\mathcal{N}_{near}$ nodes to $x_{rand}$ (lines 10-14). For each possible connection, a distribution sequence is simulated via the steering law (line 11). If the resulting sequence is probabilistically feasible, and the cost of that node represented as $c_{rand} = J{\lbrack N_{near}\rbrack} + \Delta J{(\overline{\sigma},\overline{\Pi}}$, is lower than the cost of $N_{min}$ denote by $J{\lbrack N_{min}\rbrack}$, then a new node with this sequence replaces $N_{min}$ (line 14).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

The lowest-cost node is ultimately added to $\mathcal{T}$ (line 15).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

Finally, edges are rewired based on attempted connections from the new node $N_{min}$ to nearby nodes $\mathcal{N}_{near}$ (lines 17-22), ancestors excluded (line 17). A distribution sequence is simulated via the steering law from $N_{min}$ to the terminal state of each nearby node $N_{near} \in \mathcal{N}_{near}$ (line 18). If the resulting sequence is probabilistically feasible, and the cost of that node $c_{near}$ is lower than the cost of $N_{near}$ given by $J{\lbrack N_{near}\rbrack}$ (line 19), then a new node with this distribution sequence replaces $N_{near}$ (lines 21-22). The tree expansion procedure is then repeated until a node from the goal set is added to the tree. At that point, a distributionally robust feasible trajectory is obtained from the tree root to $\mathcal{X}_{goal}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

1:Inputs: Current Tree 𝒯, time step t 4:${(\overline{\sigma},\overline{\Pi})}\leftarrow$ Steer(x̂ [Nn e a r e s t],D [Nn e a r e s t],xr a n d) 5: // Check if sequence $(\overline{\sigma},\overline{\Pi})$ is DR-Feasible 6:if DR-Feasible$(\overline{\sigma},\overline{\Pi})$ then 7: Create node $N_{min}{\{\overline{\sigma},\overline{\Pi}\}}$ 9: // Connect along a minimum-cost path 11: ${(\overline{\sigma},\overline{\Pi})}\leftarrow$ Steer(x̂ [Nn e a r],D [Nn e a r],xr a n d) 12: cr a n d← J${\lbrack x_{near}\rbrack} +

<!-- chunk {"id": "body-0051", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

{\DeltaJ{(\overline{\sigma},\overline{\Pi})}}$ 13: if DR-Feasible$(\overline{\sigma},\overline{\Pi})$ &amp; cr a n d &lt; J [Nm i n] then 14: Replace Nm i n with $N_{min}{\{\overline{\sigma},\overline{\Pi}\}}$ 16: // Re-Wire the Tree 17: for each Nn e a r ∈ 𝒩n e a r∖ Ancestors(Nm i n) do 18: ${(\overline{\sigma},\overline{\Pi})}\leftarrow$ Steer(x̂ [Nm i n],D [Nm i n],x̂ [Nn e a r]) 19: cn e a r← J${\lbrack N_{min}\rbrack} + {\DeltaJ{(\overline{\sigma},\overline{\Pi})}}$ 20: if

<!-- chunk {"id": "body-0052", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

DR-Feasible$(\overline{\sigma},\overline{\Pi})$ &amp; cn e a r &lt; J [Nn e a r] then 22: Add new node $N_{new}{\{\overline{\sigma},\overline{\Pi}\}}$ to 𝒯 Algorithm 1 OFDR-RRT*- Tree Expansion Procedure

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sample-Based Motion Planning Algorithm", "weight": 1.0} -->

${\text{Input:~}\mathbf{T}} - {\text{time step distribution sequence}{(\overline{\sigma},\overline{\Pi})}}$
(x̂t,Dx̂t)← t element in $(\overline{\sigma},\overline{\Pi})$ sequence
4: 𝕃← Line connecting position block of x̂t − 1 to x̂t
Algorithm 2 DR-Feasible Subroutine

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We demonstrate our proposed framework using a double integrator robot moving in a bounded and cluttered environment. While the proposed framework can handle dynamic and uncertain obstacles, for simplicity of illustration we assume the obstacles are static and deterministic $({w_{\mathcal{O}_{t}} = {0,{\forall t}}})$, so that all uncertainty in this example comes from the unknown initial state, robot process disturbance, and measurement noise. The robot dynamics matrices are

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

where ${dt} = {0.1s}$ and the states are the two dimensional position and velocity with two dimensional force inputs. The environmental state dynamics matrices $A_{z},B_{z},G_{z}$ are formed accordingly using with the above robot dynamics matrices. We assume the robot to start from the origin with zero initial velocity, and that the initial state and noise covariance matrices are

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The robot is treated as a point mass without loss of generality, since a known geometry can be easily handled by a fixed tightening of the state constraints. The 2D position of the robot is sampled uniformly within the bounds of the feasible 2D environment whose boundaries are not treated probabilistically. The search radius used in the Algorithm 1 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints") uses a maximum radius of $\mu_{max} = 1$ and the environment based planning constant $\gamma = 20$. The output filter dynamics matrices are

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We define the error $e_{t} = {{C_{xr}\mathcal{Z}_{t}} - x_{s}}$ for $i = {0,\ldots,T}$, with $T = 5$. A dynamic output feedback policy $u_{t}$ of the form given by (22 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) that minimizes the cost function

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

is computed using dynamic programming to steer the robot from a tree node state $x_{t}$ to a random feasible sample $x_{s}$. The matrices ${Q = \begin{bmatrix}
\end{bmatrix}},{R = {0.02I}}$ are used to penalize the state and control deviations respectively. The distributionally robust state constraints are enforced with probabilistic satisfaction parameter $\alpha = 0.05$. Three different simulations using the above double integrator system are performed namely: 1) deterministic collision check where uncertainties are not accounted, 2) chance constrained collision check where the system noises are assumed to be Gaussian distributed and, 3) distributionally robust collision check assuming the noises belong to their respective ambiguity sets. For all the simulations, the chance constrained $\text{RRT}^{\ast}$ algorithm with the corresponding collision check procedure is run for 1200 iterations, with 1-$\sigma$ position uncertainty ellipses from the covariance matrix being drawn at the end of each trajectory.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

The tree generated by an $\text{RRT}^{\ast}$ algorithm using a deterministic collision check where uncertainties are not accounted for is shown in Figure 1. It can be seen that highly risky trajectories around the obstacles are generated, since the uncertainty in the state due to the initial localization and system dynamics uncertainties are not explicitly incorporated. Assuming Gaussian noises and using risk parameter $\alpha = 0.05$, the chance constrained variant of $\text{RRT}^{\ast}$ generates more conservative trajectories as shown in Figure 2. However, the actual perception uncertainties in robotic systems often do not match well with a Gaussian assumption, so this approach can still significantly underestimate risks of constraint violation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

The OFDR-$\text{RRT}^{\ast}$ tree as shown in Figure 3 generates more conservative trajectories around the obstacles than the Gaussian chance constrained counterpart, by explicitly incorporating the uncertainty in the state due to the initial localization, system dynamics, and measurement uncertainties in the form of ambiguity sets. It produces trajectories that satisfy the chance constraints under the worst-case distribution in the ambiguity sets. Clearly, the feasible set is smaller with the distributionally robust constraints, and certain nominally feasible paths from the initial state to the goal are deemed too risky in the presence of the uncertainties, e.g., the relatively narrow gaps to the right and below the goal region. These trajectories, with a more sophisticated and coherent quantification of risk, are generated with the same computational complexity as with Gaussian chance constraints.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we presented a methodological framework aimed towards tighter integration of perception and planning in autonomous robotic systems. The environmental state is estimated from sensor data to propagate both estimates and uncertainties of both robot and obstacles. Risk constraints are posed in a meaningful and coherent manner through distributionally robust chance constraints. Using a dynamic output feedback controller together with the distributionally robust risk constraints, a new algorithm called OFDR-$\text{RRT}^{\ast}$ is shown to produce risk bounded trajectories with coherent risk assessment. Future research involves studying distribution propagation for nonlinear systems with higher order moments and considering Kalman filter variations (e.g., unscented) along with more sophisticated steering methods to explicitly incorporate the nearby obstacle constraints. Also, the combination of moment- and data-based distribution parameterizations for uncertainty modeling could be used to combine their relative advantages.
