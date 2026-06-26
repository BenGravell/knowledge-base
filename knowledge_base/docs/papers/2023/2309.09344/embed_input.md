<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Belief Road Map for Planning under Uncertainty

Topics include Belief-space planning, Motion planning under uncertainty, Covariance control, Roadmap, Output feedback, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Builds a graph-based belief-space planner using covariance-control edges and road-map nodes with controlled uncertainty. The paper targets practical planning in narrow or uncertain environments where paths must manage both geometry and state-estimation quality.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robotic systems, particularly in demanding environments like narrow corridors or disaster zones, often grapple with imperfect state estimation. Addressing this challenge requires a trajectory plan that not only navigates these restrictive spaces but also manages the inherent uncertainty of the system. We present a novel approach for graph-based belief space planning via the use of an efficient covariance control algorithm. By adaptively steering state statistics via output state feedback, we efficiently craft a belief roadmap characterized by nodes with controlled uncertainty and edges representing collision-free mean trajectories. The roadmap's structured design then paves the way for precise path searches that balance control costs and uncertainty considerations. Our numerical experiments affirm the efficacy and advantage of our method in different motion planning tasks. Our open-source implementation can be found at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the challenging realm of robotic motion planning, uncertainty presents a critical hurdle for effective operation in dynamic and complex real-world environments. Historically, motion planning under uncertainty evolved from deterministic motion planning foundations, adopting one of two primary trajectories: the optimization-based approach and the sampling-based strategy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The trajectory optimization paradigm, extensively studied in works like and, transforms planning challenges into optimal control problems. This transformation necessitates the resolution of the Hamilton--Jacobi--Bellman equation through dynamic programming techniques. However, while this method promises precision, it faces significant scalability issues, often at the cost of local solutions or even infeasibility.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other end of the spectrum, sampling-based planning establishes motion planning as a search problem. By utilizing algorithms such as the probabilistic road maps (PRM) and rapidly exploring random trees (RRT), this approach leverages graph structures filled with random feasible states to pinpoint optimal paths. What sets this approach apart is its promise of probabilistically complete solutions, assuring an increasing likelihood of finding a feasible solution with more samples.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While deterministic motion planning offers a robust framework, introducing uncertainties complicates the scenario significantly. This led to the development of belief space planning. Essentially an expansion of traditional planning to incorporate uncertainties, this approach has seen a growing emphasis on belief road maps (BRM). Unlike the conventional nodes of deterministic states in PRM, BRM employs state distributions, bringing forth unique challenges, especially regarding computational efficiency.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the intersection of these challenges lies covariance steering, a discipline geared towards guiding distributions. Notably, in a series of studies, Chen et al. illustrated that linear system distribution steering can be achieved through closed-form solutions. More recent works expanded on this by integrating safety constraints and addressing nonlinear control-affine dynamics.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building upon these advances, our research introduces a nuanced covariance steering approach for graph-based motion planning. We tackle the BRM's existing challenges by proficiently crafting probabilistic graph edges. Incorporating state estimation further aligns our methodology with the broader belief space planning framework, drawing parallels to chance-constrained strategies like CC-RRT\*. Empirical evidence, as we will present, accentuates the advantages of our approach over existing methods, showcasing both its effectiveness and efficiency in managing uncertainties.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Belief space planning", "weight": 1.0} -->

Belief space planning addresses the challenge of making decisions with uncertain robot states where the belief state $b$ is a composite representation of the robot's state and its associated uncertainty. With new input $u$ and observation $z$, the state transition function $\tau$ updates the belief state $b^{'} = {\tau{(b,u,z)}}$. Instead of always choosing the shortest path, belief space planners leverage the belief information and search for a more conservative motion plan when the state estimation is uncertain, as shown in figure 1. A significant concern when planning in belief spaces is the computational challenge due to the high dimensionality of belief states. This problem can be addressed by sampling-based algorithms like PRM.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Belief space planning", "weight": 1.0} -->

The belief-space variant of the PRM is called the Belief Roadmap (BRM). The primary idea of BRM is to sample both configurations and their distributions in the belief state space, test them for feasibility, and then attempt to connect nearby configurations to form a roadmap. The BRM can be mathematically represented as a graph $G = {(V,E)}$ where $V = {\{ b_{i}\}}$ is the set of nodes representing feasible belief states and $E$ is the set of edges indicating belief paths between adjacent nodes. To construct BRM, for each pair of belief nodes $(b_{i},b_{j})$, a local planner attempts to find a feasible path considering both the spatial constraints and the belief evolution. The belief evolution accounts for uncertainty propagation, influenced by robot dynamics and environmental factors. Once the belief roadmap is constructed with the cost associated with traversal and belief uncertainty, an optimal path can be found by graph search algorithms like $A^{\ast}$ and Dijkstra.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Covariance steering for control-affine systems", "weight": 1.0} -->

The covariance steering problem for nonlinear systems remains a challenge. Recent progress established in demonstrates an efficient algorithm tailored for control-affine systems. We present the main results in this section. The nonlinear system under consideration is where $X_{t} \in {\mathbb{R}}^{n}$ is the state vector, $u_{t} \in {\mathbb{R}}^{p}$ is the input vector and $f{(t,X_{t})}$ is the drift function. The input matrix ${B{(t)}} \in {\mathbb{R}}^{n \times p}$ is assumed to be full rank. $W_{t} \in {\mathbb{R}}^{p}$ represents a standard Wiener process, and $\epsilon > 0$ parameterizes the intensity of the disturbance. The covariance steering problem minimizes the control energy while seeking a state feedback policy to steer state statistics of the system from an initial value to a terminal one.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Covariance steering for control-affine systems", "weight": 1.0} -->

By leveraging the Girsanov theorem, problem can be transferred into a composite optimization problem which can be solved by the proximal gradient algorithm. From the results established, each proximal gradient iteration with step size $\eta$ amounts to solving the following linear covariance steering problem where ${A_{k}{(t)}},{a_{k}{(t)}}$ are the results from last iteration. Also, ${\overline{x}}_{k}{(t)}$ is the mean trajectory at $k$, ${\hat{A}}_{k}{(t)}$, ${\hat{a}}_{k}{(t)}$ are linearization matrices along ${\overline{x}}_{k}{(t)}$, and ${Q_{k}{(t)}},{r_{k}{(t)}}$ are the weighting matrices.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Covariance steering for control-affine systems", "weight": 1.0} -->

This result bridges the gap between the non-linear covariance steering problem and the linear covariance steering problem. The linear covariance steering problem in 3 enjoys a closed-form feedback solution in the form where $\Pi{(t)}$ satisfies a coupled Riccati equations. This closed-form solution for the proximal gradient update allows us to solve the covariance steering problem for the control-affine systems with a sublinear rate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In this work, we consider the motion planning problem under uncertainty. Uncertainty of the robot results from three sources: robot motion, robot state estimation, and environment. In our work, we assume the environment is deterministic and only considers the uncertainty of the robot itself. Robots are nonlinear control-affine systems whose dynamics and sensor models are Here, the notations follow the above Section 1 and $z{(t)}$ is the observation output with function $h$ and Gaussian noise $v{(t)}$. The dynamics and sensor model can be viewed as the belief transition function of the robot. For the uncertainty that stems from the robot motion and dynamic model, we denote $\Sigma$ as the covariance of the actual robot states $x$, which follows 4. $\Sigma$ describes the influence of noise $W_{t}$ on the ideal robot states which follow the uncorrupted dynamic model.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

For the uncertainty that stems from the state estimation, we denote $P{(t)}$ as the state error-covariance of the estimation error $\overset{\sim}{x}$. It is worth noting that the covariance of the terminal state is required to be larger than the state error-covariance $\Sigma_{T} > {P{(T)}}$ when using state output as feedback. Denote estimated robot states as $\hat{x} = {x - \overset{\sim}{x}}$ and its covariance as $\hat{\Sigma} = {\Sigma - P}$. We hope to steer the state covariance $\Sigma$ by controlling the estimated state covariance $\hat{\Sigma}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We can state our control problem as for the given waypoints $x_{0},x_{T}$ and their estimated state covariance ${\hat{\Sigma}}_{0},{\hat{\Sigma}}_{T}$, finding a control sequence $u_{t}$ such that 1) control the mean of the robot states from $x_{0}$ to $x_{T}$, 2) control the covariance of the robot states from $\Sigma_{0}$ to terminal covariance $\Sigma_{T}$ via output feedback $\hat{x}$, 3) generate a collision-free mean trajectory and 4) minimize the objective function of expected control energy and a state cost

<!-- chunk {"id": "body-0018", "role": "body", "section": "belief space collision-avoiding covariance steering", "weight": 1.0} -->

We hope to build a BRM and solve problem by edge construction and graph search. Constructing edges in belief space is challenging in terms of computation since it involves steering state statistics under safety constraints using partially observable state information. We leverage the proximal gradient algorithm for problem with a collision-avoiding state cost to achieve the node connection in a BRM. In, ${hinge}{(\cdot)}$ represents the hinge loss function, and $S{(\cdot)}$ is a differentiable signed distance function to the obstacles. We showed in that the proposed proximal gradient algorithm in is effective and efficient in producing collision-free belief space trajectories.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Collision avoiding covariance steering", "weight": 1.0} -->

By employing the hinge loss function ${hinge}{( \cdot )}$, we can succinctly define our cost function as to penalize risky behaviors and circumvent obstacle collisions. For each iteration of the proximal gradient covariance steering algorithm associated, rather than detailing the intricate mathematics of deriving the weighting matrices $Q_{k}{(t)}$ and $r_{k}{(t)}$, it suffices to say that they are formulated based on the gradient and Hessian of the cost function. They integrate the effects of system dynamics, control inputs, and uncertainties.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Collision avoiding covariance steering", "weight": 1.0} -->

Upon solving within the paradigm of linear covariance steering, the optimal control policy is formulated as: This control policy, when injected into the closed-loop process, offers the subsequent update dynamics From this, we deduce the iterative update rules: To synchronize the evolution of ${\overline{x}}_{k}{(t)}$ and $\Sigma_{k}{(t)}$ at each iteration $k$, one can employ the aforementioned update rule, ensuring an efficient iterative process.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Collision avoiding covariance steering", "weight": 1.0} -->

In the following discourse, we showcase the state connection algorithm (as presented in Algorithm 1). Given the constructs $A_{k}{(t)}$ and $a_{k}{(t)}$ at the $k^{th}$ iteration, the algorithm commences by propagating the mean trajectory ${\overline{x}}_{k}{(t)}$ and subsequently estimating the state covariance along the path, as represented in Figure 2(a). Leveraging the updated nominal trajectory, the algorithm exploits the control-observation separation principle to compute both the Kalman gain and the state error-covariance $P_{k}{(t)}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Steering state statistics using partially-observed output", "weight": 1.0} -->

To initialize the state prediction for each sampled state, we set ${{\hat{x}}_{k}{(t_{0})}} = {{\mathbb{E}}{\lbrack{x_{k}{(t_{0})}}\rbrack}}$ and $P_{k}{(t_{0})}$ is sampled from a proper space. At each iteration, the continuous-time EKF propagates state error covariance $P_{k}{(t)}$ based on the linearized system dynamics model ${A_{k}{(t)}},{a_{k}{(t)}}$ and updates the near-optimal Kalman gain.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Steering state statistics using partially-observed output", "weight": 1.0} -->

These steps are coupled in continuous time and governed by the following Riccati equations where noise covariance $Q = {\epsilon{\mathbb{I}}_{n}}$ and $F{(t)}$ and $H{(t)}$ represent the Jacobian matrices of the system dynamics function and measurement function, respectively, as The target uncertainty of the robot state is known from the sampling stage. With the uncertainty from sensing calculated, we are able to compute the terminal error covariance of the Kalman filter state and use it as output state feedback to control the covariance of the path in the next iteration. ${{\hat{A}}_{k}{(t)}},{{\hat{a}}_{k}{(t)}}$ represent the Gaussian Markov process approximation of the trajectory at the current iteration, which can be calculated by linearizing the system with respect to the nominal trajectory.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Entropy regularized edge cost", "weight": 1.0} -->

For every trajectory between states, the cost is calculated using the sum of control energy, collision cost, and entropy cost. Entropy cost is defined as A smaller entropy cost indicates the trajectory allows higher tolerance in the robot uncertainty and requires less sensing and control effort to control the uncertainty. Leveraging the duality between stochastic control and variational inference, the objectives for the linearized system in each step of our edge construction problem formulation is equivalent to an entropy-regularized motion planning where $J$ denotes a composite cost involving a prior process-induced cost and the collision cost and $q$ is the joint Gaussian distribution induced by the stochastic process after linearization. In other words, optimizing the problem is equivalently optimizing an entropy-regularized motion planning objective for the path distribution. We found that a trajectory distribution with a smaller entropy cost is safer than one with a higher cost in a probability sense.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Entropy regularized edge cost", "weight": 1.0} -->

In the same spirit, we define the total cost for the $\text{i}^{th}$ trajectory $z_{k}^{i}$ is the weighted sum of the control energy along the mean trajectory and the entropy cost By setting $\alpha$ differently, the planner can return different optimal paths with lower control effort or lower risks.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-D Uncertainty-aware State Sampler", "weight": 1.0} -->

We utilize BRM to divide the original problem into several easier state connection subproblems. To leverage the PGCS state connection Algorithm 1, it is important to provide a meaningful covariance to represent the uncertainty for each sample state. Define the distance $d_{obs}$ between an obstacle region $\mathcal{X}_{obs}$ and sampled state $x_{s}$ as the minimum distance from $x$ to any point $p_{obs} \in \mathcal{X}_{obs}$, and the corresponding point in $\mathcal{X}_{obs}$ is the closet point $p_{obs}^{c}$ to $x$. For $n$ dimensional spatial state space, we hope to find $n$ such points $p_{obs}^{c}$ and form a covariance ellipsoid with the center point $x_{s}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-D Uncertainty-aware State Sampler", "weight": 1.0} -->

The covariance for spatial states can be calculated from the parameter for this ellipsoid and a given confidence level $P_{conf}$, such that the actual state $x$ distribution satisfies We assume a constant velocity and covariance at each sampled state. The direction of the velocity can align with the direction of the current node and adjacent node.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-E Main algorithm", "weight": 1.0} -->

The implementation of the PGCS-BRM algorithm is summarized in Algorithm 2. To calculate the hinge loss of obstacles, a signed distance field is used which, together with the start, and target states, are initialized by the user. Then the uncertainty-aware sampler samples a certain number of states in the state space and their covariance matrices determined by the environment. The main loop starts in line 11, where each feasible sampled state is looped through and whose nearest neighbors are found. The number of neighbors found is determined by a preset neighbor distance and the total number of sampled states. Next, we connect the current state with all its feasible neighbors using the state connection Algorithm 1. For each state pair, the nonlinear covariance steering connection algorithm is run twice to generate two trajectories from two different directions. To ensure the connection algorithm returns a feasible solution, we need the estimated robot state error-covariance $\hat{\Sigma} > 0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-E Main algorithm", "weight": 1.0} -->

Red dashed ellipsoids represents the estimated state covariances P (t) propagated using, and light blue ellipsoids are the state covariances Σ (t). Notice that PT is expected to be less than ΣT at every end of an edge.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiment", "weight": 1.0} -->

We conducted several numerical experiments to validate the proposed method. All experiments are conducted on a machine with CPU of i7-12700KF and 16GiB memory.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Effect on Changing $\\alpha$", "weight": 1.0} -->

(a) α = 0.2 Penalize control energy cost more than entropy cost. PGCS-BRM returns a shorter path but more risky path.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Effect on Changing $\\alpha$", "weight": 1.0} -->

(b) α = 0.6 Penalize entropy cost more than control energy cost. PGCS-BRM returns a longer but less risky path.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Effect on Changing $\\alpha$", "weight": 1.0} -->

(c) Control energy cost and entropy cost with different α. With an increasing α, the entropy wins over the control energy costs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Effect on Changing $\\alpha$", "weight": 1.0} -->

To demonstrate how $\alpha$ impacts the returned path and the ability of PGCS-BRM to handle non-linear systems, we conduct experiments on 2-D planning for a risky area. We consider the same nonlinear dynamical system used in 1,000 states are sampled and more than 10,000 trajectories are generated for state connection. In the search phase, $A^{\ast}$, a best-first search algorithm, is deployed to find a path to the given goal state with minimum total cost. In Figure 4(a) and 4(b), we show that by changing the weighting factor $\alpha$, PGCS-BRM is able to build belief graphs and find a path with less control cost or less entropy cost.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Evaluation of Running Time", "weight": 1.0} -->

We compare the proposed method with the CS-BRM method in using a linear double integrator dynamics We use a map of 5 rectangular obstacles to compare these two methods. In each experiment with a different number of nodes, the same sampling setup is deployed and we used the same start and goal states for the graph building. For PGCS-BRM, each edge building is set to execute 50 iterations of the proximal gradient with step size $\eta = 0.001$ and discretized into 50 timesteps. We recorded the times for constructing the belief space graph after node sampling and repeated each experiment three times. Both algorithms are able to build a belief roadmap, however, due to the high computation cost in performing Monte-Carlo collision checking and solving optimization problems, CS-BRM requires higher computation time. On the other hand, PGCS-BRM is able to penalize collision in the cost function and directly solve the nonlinear covariance steering with a sublinear rate. PGCS-BRM is around 100 times faster and only requires 3.38s to build a roadmap with 30 nodes, compared to CS-BRM which needs 782s on average.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C 3D Experiment", "weight": 1.0} -->

We conduct experiments in an obstacle-clustered 3-D environment for a 3-D point robot model to demonstrate the generalizability of the proposed methods in higher-dimension space. The visualization result is shown in Figure 6. We record the average time for building a PGCS-BRM with 25, 50, 75, and 100 nodes and different numbers of edges. On average, PGCS takes 0.23-0.48s to build an edge in 3D space under 100 max iterations. It is worth noticing that the actual run times vary because different states are sampled in each experiment.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

This work presents an efficient belief space roadmap (PGCS-BRM) for planning under uncertainty. The proposed method models the belief as state distributions and leverages nonlinear covariance steering with safety constraints for edge construction. We also include an entropy cost in the edge costs to account for robustness under uncertainty. Experiments show that the proposed method effectively constructs BRMs in different dimensions and outperforms state-of-the-art sampling-based belief space planning methods. Though PGCS-BRM shows promising results in building a belief roadmap with controlled covariance, the generated trajectory is still rough and not smooth. This is mainly the result of the lack of reasonable velocity sampling. Unlike spatial states, there are no explicit constraints on velocity in the sampling stage, and poorly selected velocity might result in a non-smooth trajectory. Developing a better velocity sampling algorithm and smoothing algorithm can greatly enhance the performance of the current algorithms. Another future direction worth exploring is to deploy such an algorithm in time-varying environments. The ability to control the uncertainty in planning and quickly replan the route is essential in such scenarios.
