<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Data-Driven Approach to Synthesizing Dynamics-Aware Trajectories for Underactuated Robotic Systems

Topics include Optimal control, Trajectory optimization, Robotics, Aerial robotics, Online algorithms, Optimization, Planning, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider joint trajectory generation and tracking control for under-actuated robotic systems. A common solution is to use a layered control architecture, where the top layer uses a simplified model of system dynamics for trajectory generation, and the low layer ensures approximate tracking of this trajectory via feedback control. While such layered control architectures are standard and work well in practice, selecting the simplified model used for trajectory generation typically relies on engineering intuition and experience. In this paper, we propose an alternative data-driven approach to dynamics-aware trajectory generation. We show that a suitable augmented Lagrangian reformulation of a global nonlinear optimal control problem results in a layered decomposition of the overall problem into trajectory planning and feedback control layers. Crucially, the resulting trajectory optimization is dynamics-aware, in that, it is modified with a tracking penalty regularizer encoding the dynamic feasibility of the generated trajectory. We show that this tracking penalty regularizer can be learned from system rollouts for independently-designed low layer feedback control policies, and instantiate our framework in the context of a unicycle and a quadrotor control problem in simulation. Further, we show that our approach handles the sim-to-real gap through experiments on the quadrotor hardware platform without any additional training.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For both the synthetic unicycle example and the quadrotor system, our framework shows significant improvements in both computation time and dynamic feasibility in simulation and hardware experiments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modularity is a guiding principle behind the design of numerous autonomous platforms. For example, the autonomy stack of a typical robot consists of separate modules for perception, planning, and control. In spite of the requirement of safely executing tasks in real time with limited on board computational resources, such modules usually operate at different frequencies and levels of abstraction. Roughly speaking, higher levels of abstraction allow for faster decision making. However, if the degree of abstraction varies among the different modules beyond a suitable threshold, the system as a whole can behave in unexpected, unsafe ways. By and large, choosing the right level of abstraction in robotics applications has remained somewhat of an art. We focus on developing a quantitative method of bridging the potential mismatch between the trajectory planning and control modules in a data-driven manner.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although trajectory planning and control have been among the most extensively studied areas of robotics, numerous problems remain to be solved. In particular, graph-search-based path planning algorithms can find it challenging to account for complex nonlinear system dynamics. Similarly, real-time optimization-based methods for generating trajectories typically use a simplified or a reduced order dynamics model of the agent. In contrast, low-level feedback control policies often rely on more accurate, detailed dynamics of the system being controlled in order to track a reference trajectory planned by some of the aforementioned approaches. While intuitive and conceptually appealing, this layered approach only works well if the outputs of higher layers are compatible with the abilities of lower layers.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus on the interplay between trajectory generation and feedback control. Rather than imposing such a layered architecture on the control stack, we show that it can be *derived* via a suitable relaxation of a global nonlinear optimal control problem that jointly encodes both the trajectory generation and feedback control problems. Crucially, the resulting trajectory generation optimization problem is dynamics-aware, in that it is modified with a *tracking penalty regularizer* that encodes the dynamic feasibility of a generated trajectory. While this tracking penalty does not in general admit a closed-form expression, we show that it can be interpreted as a cost-to-go. Hence, it can be learned from system roll-outs for any feedback control policy by leveraging tools from the learning literature. Finally we evaluate our framework using unicycle and quadrotor control, and compare our approach in simulation to standard approaches to quadrotor trajectory generation. Our extensive experiments demonstrate that our data-driven dynamics-aware framework allows for faster computation of trajectories that can be tracked accurately in both simulation and hardware.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive a layered control architecture composed of a dynamics-aware trajectory generator top layer, and a feedback control low layer. In contrast to existing work, our trajectory generation problem is naturally dynamics-aware, and includes a tracking penalty regularizer that encodes the ability of the low-layer feedback control policy to track a given reference trajectory.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show how this tracking penalty can viewed as the cost-to-go for a particular system, and hence be learned from system rollouts.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply our data-driven dynamics-aware trajectory generation framework to both a unicycle and a quadrotor control problem. We demonstrate that our approach generates aggressive and easy to track trajectories compared to standard methods for the two systems in consideration.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In what follows, we first formulate the dynamics-aware trajectory planning problem in Section 3 and introduce the unicycle and waypoint tracking problem as running examples. In Section 4, we introduce a result that shows how a relaxation of the underlying nonlinear controls problem naturally leads to a trajectory optimization problem that includes a regularizer that captures the tracking cost of the given controller. We also describe our supervised learning approach to learn the cost-to-go function that characterizes the feedback control layer's ability to track a given reference trajectory. In Section 5.1, we apply our approach to dynamics-aware trajectory generation to both the unicycle and quadrotor systems. We present two compelling simulation experiments in Section 5 to show that our method leverages previous trajectory data to approximate the cost-to-go function and the learned function can be applied to generate easy-to-track trajectories before discussing the results and future work in Section 6.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Multi-rate and hierarchical control", "weight": 1.0} -->

There is a rich literature on combining trajectory generation with low-level control, see for example and references therein. While these results offer differing degrees of guarantees and generality, we note that none of them derive the layered control architecture that they propose. Rather, modification to either the trajectory generation or tracking problems are made to ensure that the chosen interplay between the two layers leads to desirable results. In contrast, we derive this layered structure, and show how this naturally leads to the inclusion of a tracking penalty regularizer in the trajectory generation problem. Our work is complementary to the existing literature due to the fact that modifying any of the proposed trajectory generation optimization problems in with our proposed regularizer will only lead to more dynamically feasible trajectories.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Multi-rate and hierarchical control", "weight": 1.0} -->

Another closely-related line of work in this spirit is the "Layering as Optimization Decomposition" framework proposed, which shows that network utility maximization problems can be suitably relaxed to recover the layered architecture of network control protocol stacks. This approach was extended to linear optimal control problems, but was limited to LQR control for which the tracking penalty admits a closed-form expression. In contrast, we significantly generalize these results to nonlinear dynamical systems and present a data-driven approach to approximating the tracking penalty.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Data-driven NMPC", "weight": 1.0} -->

Due to the underlying difficulty of solving a NMPC problem that jointly encodes trajectory generation and low-level control, data-driven approaches to improve controller performance on tracking tasks have emerged. Broadly, learning can be applied to: (i) directly obtain the control policy, (ii) learn uncertainties in the dynamics and the cost function used for NMPC, and (iii) learn a low dimensional state representation for NMPC from high dimensional data. Our work broadly fits into this overall line of work in that we propose a data-driven method to learn a tracking penalty regularizer that directly encodes the closed-loop dynamics' ability to track a generated trajectory using offline trajectories. To the best of our knowledge, ours is the first approach to suggest this compact encoding of the low layer closed-loop dynamics into a cost-to-go function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Trajectory generation for quadrotors", "weight": 1.0} -->

In general, trajectory generation for quadrotors is a computationally challenging problem. The landmark paper established differential flatness of quadrotor dynamics. It showed that trajectories of position and yaw angle of the quadrotor, i.e., the flat outputs, may be specified independently of one another, and that their time derivatives yield the underlying trajectory of states and inputs required to induce them. Additionally, initiated a line of work using piecewise polynomials to represent trajectories of flat outputs. Nevertheless, these approaches decouple trajectory generation and tracking control. As a consequence, there is no model of the specific hardware used for control introduced in the planning layer. Our current work, on the other hand, provides a principled way of generating trajectories cognizant of the dynamic capabilities of the closed-loop robotic system.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider a finite-horizon, discrete-time nonlinear dynamical system

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $\mathcal{C}:{\mathcal{X}^{N + 1}\rightarrow{\mathbb{R}}}$ is a trajectory cost function, $D_{0},D_{1},\ldots.,D_{N - 1} \in {\mathbb{R}}^{l \times k}$ are matrices that penalize control effort, and $\mathcal{R}$ defines the feaible region of $x_{0:N}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

OCPs of the form are an essential component of MPC schemes for robotic applications. In such settings, the trajectory cost function $\mathcal{C}$ is typically chosen to e.g., capture high-level task objectives or reward smooth trajectories, whereas the state constraint $\mathcal{R}$ is often used to encode e.g., obstacle avoidance, waypoint constraints, or other mission-specific requirements. In the generality stated above, the OCP is difficult to solve exactly except in the simplest of cases. Under suitable regularity assumptions, good heuristics exist for finding an approximate solution. However, due to their computational complexity, these heuristics typically lead to the solve time being unacceptably large for applications with fast dynamics such as quadrotor control.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A number of works in the robotics literature approach the computational complexity by using a *layered control architecture* to decompose OCP into tractable subproblems. For example, a two-layer approach would solve a reference trajectory generation problem at the *top planning layer* using simplified dynamics (typically at a slower frequency). This reference trajectory would then be sent to the *low tracking layer* where a feedback control policy, operating in real time, attempts to follow the reference trajectory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

While conceptually appealing, the above approach has several shortcomings. The critical one is the lack of guarantees that the generated reference trajectories can be adequately tracked by the feedback control policy. This could be due to unmodelled dynamics, saturation limits, etc., of the hardware in use for control. In this paper, we address this shortcoming by *deriving* a layered architecture via a relaxation of the original OCP, that naturally leads to a *closed-loop dynamics-aware* trajectory generation problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Layering as Optimal Control Decomposition", "weight": 1.0} -->

We show how a suitable relaxation of the OCP naturally results in a layered control architecture. Such an optimization decomposition approach to layered control was first introduced in for linear-quadratic control. In this section, we extend it to general nonlinear systems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "An augmented Lagrangian relaxation", "weight": 1.0} -->

We first introduce a redundant reference trajectory variable $r_{0:N}$ constrained to equal the state trajectory, i.e.,

<!-- chunk {"id": "body-0022", "role": "body", "section": "An augmented Lagrangian relaxation", "weight": 1.0} -->

where the weight $\rho > 0$ specifies the soft-penalty associated with the constraint $r_{0:N} = x_{0:N}$. Furthermore, we have strategically grouped terms to highlight the nested structure of the resulting optimization problem. Immediately, problem admits a layered interpretation: the inner minimization over state and input trajectories $x_{0:N}$ and $u_{0:{N - 1}}$ is a traditional feedback control problem, seeking to optimally track the reference trajectory $r_{0:N}$. The outer optimization over the trajectory $r_{0:N}$ seeks to optimally "plan" a reference trajectory for the inner minimization to follow. To further highlight the layered nature of the resulting relaxation, we define the tracking penalty

<!-- chunk {"id": "body-0023", "role": "body", "section": "An augmented Lagrangian relaxation", "weight": 1.0} -->

The tracking penalty $g_{\rho}^{track}{(x_{0},r_{0:N})}$ captures how well a given trajectory $r_{0:N}$ can be tracked by a low layer control sequence $u_{0:{N - 1}}$ given the initial condition $x_{0}$, and is naturally interpreted as the cost-to-go associated with an augmented system (see §4.2). We observe that the optimal control problem defining the tracking cost is a standard nonlinear reference tracking problem with quadratic cost, and can be approximately solved using tools from nonlinear feedback control. We therefore let $\pi{(x_{t},r_{0:N})}$ denote the feedback control policy which (approximately) solves problem, and use $g_{\rho,\pi}^{track}{(x_{0},r_{0:N})}$ to denote the resulting cost-to-go that it induces.

<!-- chunk {"id": "body-0024", "role": "body", "section": "An augmented Lagrangian relaxation", "weight": 1.0} -->

While a closed-form expression for the tracking penalty $g_{\rho,\pi}^{track}{(x_{0},r_{0:N})}$ is only available in special cases, e.g., see for the linear quadratic control case, we show in §4.2 that it can be learned from data.

<!-- chunk {"id": "body-0025", "role": "body", "section": "An augmented Lagrangian relaxation", "weight": 1.0} -->

Assuming that an accurate estimate of the tracking penalty can be obtained, the OCP can now be reduced to the *static* optimization problem (i.e.,

<!-- chunk {"id": "body-0026", "role": "body", "section": "An augmented Lagrangian relaxation", "weight": 1.0} -->

We may view as a family of trajectory optimization problems parametrized by $\rho$. In the limit as $\left. \rho\nearrow\infty \right.$, optimal trajectories prioritize the reference tracking performance. On the other hand, in the limit as $\left. \rho\searrow 0 \right.$, the optimal trajectories minimize the $\mathcal{C}$ cost oblivious to the dynamics constraints.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

Computing the tracking penalty $g_{\rho}^{track}$ for general nonlinear dynamics and experimental hardware platforms with black-box feedback control policies is intractable. We therefore propose a supervised learning approach to learning the tracking penalty from data as shown in Figure 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

Here $Z \in {\{ 0,1\}}^{{{Nn} \times N}n}$ is the block-upshift operator, i.e., a block matrix with $I_{n}$ along the first block super-diagonal, and zero elsewhere. The state $\mu_{t}^{x} = x_{t}$ evolves in exactly the same way as in the true dynamics, whereas the reference trajectory $\mu_{t}^{r}:=r_{t:{t + N}}$ is shifted forward in time via ${Z\mu_{t}^{r}} = r_{{t + 1}:{t + 1 + N}}$. Fixing policy $\pi{(\mu_{t})}$, we define the policy dependent tracking cost

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

We note that this corresponds exactly to the objective function defining the tracking penalty evaluated under the control sequence ${u_{t} = {\pi{(\mu_{t})}}}.$ As such, the policy dependent tracking cost $g_{\rho,\pi}^{track}{(x_{0},r_{0:N})}$ is naturally viewed as an upper-bound to the true optimal tracking cost, where the sub-optimality is dependent on the quality of the chosen policy $\pi$. In particular, we have that $g_{\rho,\pi^{\star}}^{track} = g_{\rho}^{track}$ for any optimal policy $\pi^{\star}$ that solves the optimal control problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

Noting that the policy dependent tracking penalty is defined in terms of stage-wise costs, we can interpret $g_{\rho,\pi}^{track}{(x_{0},r_{0:N})}$ as a cost-to-go function associated with the Markov Decision Process defined by the cost, dynamics, and policy $\pi$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

We therefore use Monte Carlo sampling to generate a set of $\mathcal{T}$ trajectories of horizon length $N$ given by ${(x_{0:N}^{(i)},u_{0:{N - 1}}^{(i)},r_{0:N}^{(i)})}_{i = 1}^{\mathcal{T}}$, where $x_{0:N}^{(i)}$ and $u_{0:{N - 1}}^{(i)}$ are the $i$-th state and input trajectories collected from applying feedback control policy $\pi$ to track reference trajectories $r^{(i)}$. We also compute the associated tracking cost labels $y^{(i)}:={g_{\rho,\pi}^{track}{(x_{0}^{(i)},r_{0:N}^{(i)})}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

We then used supervised learning to approximate the policy dependent tracking penalty by solving the following supervised learning problem

<!-- chunk {"id": "body-0033", "role": "body", "section": "Learning the tracking penalty through policy evaluation", "weight": 1.0} -->

over a suitable function class $\mathcal{G}$, e.g., feedforward neural networks, see §5 for more details.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Dynamics-Aware Trajectory Generation for Under-Actuated Robotic Systems", "weight": 1.0} -->

We showed the flexibility of our framework by applying it to both a unicycle and a quadrotor control problem. For each platform, we formulated a global planning and control problem, which is then subsequently relaxed according to the methods proposed in §4 to yield a dynamics-aware planning problem and a feedback control layer. We now evaluate our methods experimentally and demonstrate their effectiveness in simulation and in real-world experiments.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

We consider the continuous time unicycle dynamics

<!-- chunk {"id": "body-0036", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

where ${(x_{1},x_{2})} \in {\mathbb{R}}^{2}$ are the system's Cartesian coordinates, $\theta$ is the heading angle, and $v$, $\omega$ are the instantaneous linear and angular velocities, respectively. Letting $x = {(x_{1},x_{2},\theta)}$ and $u = {(v,\omega)}$, we can compactly write the dynamics as $\overset{˙}{x} = {g^{cts}{(x)}u}$, for suitably defined ${g{(x)}} \in {\mathbb{R}}^{3 \times 2}$. Letting $x_{t + 1} = {f_{uni}{(x_{t},u_{t})}}$ be the rk4 discretization of these continuous dynamics, we can then pose the global problem

<!-- chunk {"id": "body-0037", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

where $w_{\tau}$ such that $\tau \in \mathcal{T}_{w} \subseteq {\{ 0,\ldots,N\}}$ are waypoints that the unicycle should traverse at time $\tau$, and $R > 0$ is a positive definite control cost matrix.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

To instantiate the layering framework proposed in §4, we fix a low layer continuous time feedback control policy as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

We then define a new control input, ${\Deltar} = \overset{˙}{r}$, to obtain the continuous time closed-loop dynamics

<!-- chunk {"id": "body-0040", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

Letting ${\overline{x}:={(x,r)}},$ we compactly rewrite the continuous time closed-loop dynamics as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

for an appropriately defined $f_{\pi,{uni}}^{cts}$. Finally, we obtain the discrete time dynamics $f_{\pi,{uni}}{({\overline{x}}_{t},{\Deltar_{t}})}$ used in the experiments below via a rk4 discretization of the continuous time dynamics.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Unicycle Control", "weight": 1.0} -->

Given the fixed closed-loop dynamics using the policy $\pi_{uni}$, the dynamics-aware trajectory generation problem is then given by

<!-- chunk {"id": "body-0043", "role": "body", "section": "Data collection", "weight": 1.0} -->

In order to estimate the policy dependent tracking penalty $g_{\rho,\pi_{uni}}^{track}{(x_{0},r_{0:N})}$, we sample reference trajectories and roll them out on the closed-loop system. In order to appropriately shape the landscape of the learned penalty, we sample both easy and difficult to track reference trajectories. Towards that end, we generate *easy to track* reference trajectories by using Iterative LQR (ilqr) to approximately solve the finite horizon constrained optimal control problem

<!-- chunk {"id": "body-0044", "role": "body", "section": "Data collection", "weight": 1.0} -->

where $R_{w}$ is a positive definite matrix penalizing variations in the reference trajectory. Additionally, we also generate state independent polynomial reference trajectories that are oblivious to the low layer closed-loop dynamics of the system and only satisfy the initial and terminal state constraints. This strikes a balance between having low cost but hard to compute ilqr trajectories and high cost but easy to compute polynomial trajectories. At inference, we solve a constrained optimization by applying gradient descent on the dynamics-aware trajectory generation problem.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Data collection", "weight": 1.0} -->

We generate $500$ trajectories by sampling initial and goal locations from a uniform distribution over ${\lbrack 0,2\rbrack}^{2}$ and ${\lbrack 1,3\rbrack}^{2}$, respectively. Between each initial location and goal, we sample one waypoint by choosing a convex combination of the two points. The heading angles for the initial state is sampled at random from a uniform distribution on the interval $\lbrack 0,\pi\rbrack$ and the goal heading angles are set to 0. As described in Section 5.1, we run the constrained ilqr algorithm on the closed loop dynamics until convergence enforcing the initial and terminal state constraints. Additionally, we augment the training dataset with $500$ polynomial reference trajectories with randomly sampled initial, waypoint and goal conditions from the fixed intervals mentioned above. In this way, we include both easy to track trajectories (generated by ilqr) and difficult to track trajectories (polynomial) in order to appropriately shape the optimization landscape of the learned tracking penalty.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Data collection", "weight": 1.0} -->

For testing, we generate $50$ trajectories with one or two waypoints each from the fixed intervals using the polynomial reference generation method described above.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Training", "weight": 1.0} -->

We train a multi-layer perceptron network with $3$ hidden layers of $\{ 1000,500,200\}$ neurons, respectively, with Exponential Linear Unit (ELU) activation functions. ---see Network Parameterization and Training for more details. We train a separate network for each value of $\rho$ using a batch size of $64$, learning rate $10^{- 4}$ and run for $2500$ epochs. The entire network is setup using the optimized JAX, Optax and Flax libraries. The loss function is optimized using stochastic gradient descent (SGD) with momentum set to $0.9$. At test time, i.e., when we compute trajectories to be tracked by the low-level controller, we freeze the weights of the network and run projected gradient descent (PGD) using jaxopt to locally solve the dynamics-aware trajectory planning problem. We set the maximum number of iterations for projected gradient descent to $50$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

We provide two types of evaluations on the learned policy dependent tracking penalty. First, we evaluate the network predictions for different values of relaxation weight $\rho$ on a test dataset consisting of $50$ trajectories generated independently and in an identical way to the training dataset. Next, we plot the relative tracking cost in Figure 2, where we compute the ratio of the tracking errors incurred by the trajectories returned by the dynamics-aware problem to those incurred by polynomial interpolating (i.e., not dynamics-aware) trajectories---we emphasize these tracking costs are computed via rollouts of the actual closed-loop system on the trajectories. The lower the value of the relative cost, the more significant the tracking performance gain obtained from using our approach. Our results indicate that for appropriately chosen tracking weight $\rho > 0$ the trajectories generated using our method are on average easier to track than polynomial interpolating trajectories.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

In Figure 3, we show the performance of our network ($\rho = 0.1$) in planning reference trajectories that are of lower tracking cost (from the closed-loop dynamics simulation) with each gradient step. We also evaluated the average run time of our approach on $200$ trajectories and found that our algorithm is almost twice as fast as compared to the run time of the ilqr algorithm. Our network on average takes $6.9 \pm 0.7$ seconds to converge compared to ilqr which takes $11.4 \pm 0.5$ seconds. We conjecture that the results can be further improved by using convex parameterizations for the tracking penalty, such as input-convex-neural-networks (ICNN): we leave exploring this direction to future work. We also note that the approach is sensitive to the number of gradient steps based on the choice of $\rho$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Quadrotor Control", "weight": 1.0} -->

We consider the waypoint following problem where one is given a sequence of times ${(\tau_{i})}_{i = 0}^{W} \in {{\lbrack 0,T\rbrack} \cap {\mathbb{Z}}}$ and waypoints $\mathcal{W} = {\{{(p_{i},\psi_{i})}\}}_{i = 0}^{W} \subseteq {{\mathbb{R}}^{3} \times S^{1}}$, each specifying the desired position and yaw angle of the quadrotor. The goal is to generate a trajectory that passes through the waypoints at corresponding times. These conditions can be formulated in the OCP problem by encoding the state constraints

<!-- chunk {"id": "body-0051", "role": "body", "section": "Quadrotor Control", "weight": 1.0} -->

within the constraint set $\mathcal{R}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Quadrotor Control", "weight": 1.0} -->

Here, the state $x$ of the agent consists of its position ($p \in {\mathbb{R}}^{3}$), velocity ($v \in {\mathbb{R}}^{3}$), and orientation ($R \in {SO{}}$) with respect to the world frame, while the control input $u = {(c,\omega)}$ consist of total thrust, $c \in {\mathbb{R}}$, and angular velocity, $\omega \in {\mathbb{R}}^{3}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Quadrotor Control", "weight": 1.0} -->

To instantiate the layering framework proposed in §4, we fix a tracking control policy $\pi_{q}{(x_{t},r_{t:{t + N}})}$ for the given dynamics $f_{q}{(x_{t},u_{t})}$, and a way to collect data on this tracking policy. In the experiments that follow, we use an SE geometric controller, but any tracking controller, e.g., a PID, or even an RL-based controller, can be equally accommodated by our framework. Fixing the policy $\pi_{q}$, we can define the resulting closed-loop dynamics $x_{t + 1} = {f_{\pi,q}{(x_{t},r_{t:{t + N}})}}$ and corresponding policy dependent tracking penalty $g_{\rho,\pi_{q}}^{track}{(x_{0},r_{0:N})}$ as.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Quadrotor Control", "weight": 1.0} -->

We now describe how to use the penalty $g_{\rho,\pi_{q}}^{track}{(x_{0},r_{0:N})}$ to generate dynamics-aware trajectories that interpolate the waypoints $(p_{i},\psi_{i})$. First, we note that from differential flatness, it suffices for us to generate trajectories for $x,y,z$, and $\psi$. We take the widely-adopted approach of parameterizing trajectories as piecewise polynomials of order $k_{r}$ that smoothly interpolates between waypoints. Specifically, each segment is parametrized by a polynomial where $c_{i,k}^{j}$ denotes the $k$-th coefficient of polynomial $i$ for the dimension $j \in {\{ x,y,z,\psi\}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Quadrotor Control", "weight": 1.0} -->

where $r_{0:N}$ is a linear map of the polynomial coefficients.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Data Collection", "weight": 1.0} -->

We generate $125$ trajectories by sampling the $x,y,z,\psi$ amplitudes of the Lissajous curves from a uniform distribution on the intervals ${\lbrack{- 0.65},0.65\rbrack},{\lbrack{- 0.55},0.55\rbrack},{\lbrack{- 0.55},0.55\rbrack},{\lbrack{- {0.6\pi}},{0.6\pi}\rbrack}$, respectively.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Data Collection", "weight": 1.0} -->

where the time period of each trajectory is $3s$ and each second is discretized into 100 time steps. The discretization interval is selected based on the frequency of the feedback layer $SE{}$ tracking controller, and $N = 300$ is our planning horizon. We generate piece-wise polynomial reference trajectories $r_{t} \in {\mathbb{R}}^{4}$ denoting $x,y,z$ positions and $\psi$, for each segment between waypoints by minimizing the sum of squares of jerk and yaw angular velocity. We forward simulate the tracking controller using a state-of-the-art real-time quadrotor physics simulator on the ROS platform to record the system rollouts.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Training", "weight": 1.0} -->

We train a multi-layer perceptron composed of 3 hidden layers with $\{ 500,400,200\}$ neurons, respectively, and ELU activation functions. ---see Network Parameterization and Training for more details. Similar to the unicycle setup, we train a separate neural network for each value of $\rho$ using a batch size of 64, learning rate $10^{- 3}$, and run for $2000$ epochs. The network implementation uses Optax, Flax, and JAX libraries for optimization and the loss function used is SGD with momentum set to be $0.9$. At test time, we use the 'L-BFGS-B' solver from jaxopt to locally solve the dynamics-aware trajectory planning problem where the objective function represents a trade-off between satisfying waypoints and the tracking cost of the $SE{}$ geometric controller. We do no additional training for the hardware experiments.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate the policy-dependent tracking penalty on trajectories generated independently and in an identical way to the training dataset, however, we allow for replanning after every $300$ time steps. We compare the tracking performance of our dynamics-aware framework with two trajectory generation methods, the standard minimum-jerk based planner satisfying constraints described in equations and polynomial trajectories that satisfy waypoint constraints but no smoothness constraints. Figure 5 shows the full path of the trajectory in blue, the replanned trajectories for every $300$ time steps in green and the red arrows correspond to the odometry states from the simulator. On the top left are results from using the minimum jerk planner, the bottom left shows the polynomial trajectories without smoothness constraints and on the right we show our dynamics-aware planner that solves the trajectory generation. Our planner is able to recover trajectories of low tracking cost by replanning with the learned tracking penalty every $300$ time steps. We also evaluate the tracking cost from the $SE{}$ dynamics for different values of $\rho$, as shown in Figure 4.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results", "weight": 1.0} -->

We observe that the learned tracking penalty faithfully approximates the tracking cost function of the low layer $SE{}$ feedback controller and that the dynamics-aware trajectories synthesized using the learned tracking penalty achieve a significant reduction in the tracking cost for every tracking weight value $\rho > 0$ that we tested. Finally, as shown in Figure 6, we demonstrate our dynamics-aware trajectories on the Qualcomm-Snapdragon based hardware platform to show that our method handles the sim-to-real gap without any additional training.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Hardware", "weight": 1.0} -->

We use the hummingbird quadrotor platform running a VOXL Flight - PX4 Autonomy controller with on-board visual inertial odometry and inertial measurement unit (IMU) sensors for localization. We treat the quadrotor system as a remote work station and establish a communication interface using the ROS platform from a laptop to transmit the position commands for the low layer $SE{}$ feedback controller. The position commands are $14$-dimensional vectors composed of position, velocity, acceleration, jerk, yaw angles and yaw angular speed computed using $x,y,z,\psi$ references. We generate trajectories online using our dynamics-aware planner and transmit the commands over WiFi to the quadrotor for execution and record the reference trajectory and the odometry states from each run. We plot the $x,y,z$ co-ordinates of the reference trajectories and odometry measurements across time as shown in Figure 6. We note that our dynamics-aware framework is able to generate trajectories that are safe to be deployed and tracked by the $SE{}$ controller even without enforcing smoothness constraints.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Hardware", "weight": 1.0} -->

In future work, we would like to eliminate latencies arising from communicating the commands over a network and aim towards running the dynamics-aware framework using the limited onboard compute of the quadrotor platform.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We showed that the familiar two layer architecture composed of a trajectory planning layer and a low-layer tracking controller can be derived via a suitable relaxation of a global optimization problem. The result of this relaxation is a regularized trajectory planning problem, wherein the original state objective function is augmented with a tracking penalty which captures the low layer closed-loop system's ability to track a given reference trajectory. We further observed that this penalty can be interpreted as the cost-to-go of an augmented system, and showed how it could be learned from data. We demonstrated our results on waypoint tracking problems for a unicycle system and a quadrotor system in simulation and hardware. In both cases, our method yielded significantly easier to track trajectories than simple polynomial interpolations between waypoints. Future work will look to develop more systematic approaches to collecting trajectory data for training the tracking penalty, and to derive statistical guarantees for the learned tracking penalty.
