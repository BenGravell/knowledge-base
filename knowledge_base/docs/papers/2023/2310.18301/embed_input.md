<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interactive Joint Planning for Autonomous Vehicles

Topics include Autonomous driving, Interaction-aware planning, Trajectory prediction, Motion planning, Neural networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates autonomous-driving planning around ego-conditioned prediction so the planner accounts for how nearby agents may react to the ego plan. The paper contributes a joint planning structure that makes learned interaction models more directly usable in closed-loop decision making.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In highly interactive driving scenarios, the actions of one agent greatly influences those of its neighbors. Planning safe motions for autonomous vehicles in such interactive environments, therefore, requires reasoning about the impact of the ego's intended motion plan on nearby agents' behavior. Deep-learning-based models have recently achieved great success in trajectory prediction and many models in the literature allow for ego-conditioned prediction. However, leveraging ego-conditioned prediction remains challenging in downstream planning due to the complex nature of neural networks, limiting the planner structure to simple ones, e.g., sampling-based planner. Despite their ability to generate fine-grained high-quality motion plans, it is difficult for gradient-based planning algorithms, such as model predictive control (MPC), to leverage ego-conditioned prediction due to their iterative nature and need for gradient. We present Interactive Joint Planning (IJP) that bridges MPC with learned prediction models in a computationally scalable manner to provide us the best of both the worlds. In particular, IJP jointly optimizes over the behavior of the ego and the surrounding agents and leverages deep-learned prediction models as prediction priors that the join trajectory optimization tries to stay close to.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, by leveraging homotopy classes, our joint optimizer searches over diverse motion plans to avoid getting stuck at local minima. Closed-loop simulation result shows that IJP significantly outperforms the baselines that are either without joint optimization or running sampling-based planning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A cornerstone for safe motion planning for autonomous vehicles is the ability to reason about interactions between the ego vehicle and other traffic agents, such as human-driven vehicles and pedestrians. A standard approach to deal with interactive scenarios is to leverage prediction models---heuristic or data-driven ---to generate predictions of the traffic agents' future motions and plan the ego motion accordingly. In particular, various deep-learned prediction models now represent the state of the art in prediction. Modern deep learning prediction models widely use ego-conditioning, i.e., condition the prediction of adjacent agents' motion on the ego's future motion, to improve the prediction quality and capture the interaction between the ego and the agents. The resulting prediction is then consumed by a planner that aims to generate an ego motion plan that avoids collisions and makes progress towards the goal. Depending on how the prediction is consumed, there are two typical styles of planners: sampling-based planners and iterative planners. The former takes a bunch of ego motion samples, calls the prediction model to generate ego-conditioned predictions and searches for a motion plan. An iterative planner, on the other hand, iteratively refines the ego motion plan, with e.g. gradient or Bayesian optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the latter may achieve finer granularity for the ego motion due to iterative refinement, it needs to evaluate the ego motion plan significantly more times than a sampling-based counterpart and the evaluation cannot be parallelized. As a result, the computational complexity prohibits the use of complex deep-learned ego-conditioned prediction models together with an iterative planner---when a prediction model is used, it is typically limited to simple analytical models. In this paper, we propose a computationally tractable approach, called Interactive Joint Planning (IJP), which reasons about interactivity by combining deep-learned prediction models with iterative planners. IJP significantly outperforms other baselines yielding safer motion plans without sacrificing liveness and being overly conservative.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions and paper organization. We propose IJP, which is a model predictive control (MPC)-based planner that is compatible with any (deep learned) prediction model. The two main novelties are (i) IJP jointly optimizes over the ego vehicle and the nearby agents' motion with collision avoidance constraints while penalizing deviation from the unconditioned predicted trajectories of the agents. The "planned" motion for the agents then serve as the ego-conditioned trajectory predictions for those agents and are integrated in the gradient-based planner. (ii) To remedy the local minimum issue of nonconvex optimization, we introduce the novel concept of free-end homotopy that allows us to efficiently explore a diverse range of motions. In particular, free-end homotopy is an extension of homotopy to trajectories that do not share the same end point. We empirically show that IJP significantly outperforms a baseline without joint optimization and is superior to a sampling-based planner baseline in both performance and computation complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Related Works", "weight": 1.0} -->

Interactive Planning. Interactive / social-aware planning has been studied extensively in the literature. Some of the early approaches modeled the uncontrolled agents' behavior as Gaussian uncertainty without consideration for the impact of ego behavior on nearby agents. Ignoring the ego's impact can lead to overly conservative motion plans as was famously shown in the freezing robot problem. This led to a plethora of research on navigating crowds while accounting for the reactivity of other agents, such as the joint optimization via Gaussian Process (GP) approach in and the reinforcement learning (RL) approach.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related Works", "weight": 1.0} -->

Reactive Behavior Modeling. The crux of interactive planning is to properly model other agents' reactive behavior. Inverse reinforcement learning (IRL) is an obvious choice, e.g. and it is used subsequently in optimization over the ego motion. Another popular formulation leverages game theory, which assumes that every agent tries to maximize its own utility; however, the computational complexity of equilibrium solving remains a challenge and it is not straightforward to combine game theory with data-driven methods. Partially-observable Markov Decision Process (POMDP)-based methods were applied to interactive planning and inferring the hidden intention of surrounding agents, but similar to the game-theoretic approaches, POMDPs also suffer from high computational complexity and they are typically hand-crafted, making them difficult to scale. Other analytical models such as Intelligent Driver Models (IDM) and Probabilistic Graphic Models (PGM) have also been applied to intention estimation and interactive planning, however, they are limited to simple scenarios, such as highway driving. The idea of joint optimization has been studied for conflict resolution, yet assumes knowledge about the other agent's cooperativeness.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

Deep-Learned Prediction. The above-mentioned methods, though very different in nature, all make assumptions (e.g. rationality) about the surrounding agents' decision processes, and the planner then leverages the assumptions to make the planning problem tractable. In contrast, modern prediction methods are predominantly deep-learned phenomenological models, i.e., models trained with data to match the ground truth without a clear explanation of the decision process. While they achieve good prediction accuracy and are capable of ego-conditioned prediction, working with downstream interactive planner remains difficult, as pointed out previously. The expensive inference of ego-conditioned prediction under a large number of ego plans made it prohibitive to evaluate fine-grained ego plans. In the authors use a linear system to represent the ego-conditioned prediction compactly, but the performance is limited by the simplicity of linear systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Homotopy Planning. Homotopy planning has been widely studied for motion planning of autonomous systems. To distinguish among homotopy classes of trajectories, uses the relative lateral position (i.e., left or right) between two vehicles, partition the free space into sub-regions, construct homotopy-invariant words, while use a magnetic-field inspired approach. All these approaches require the start and end points of all candidate trajectories to coincide for homotopy classes to be well-defined---there exists no concept in the literature on homotopy that accommodates distinguishing trajectories that do not share the same end point. In this paper, we generalize homotopy to rigorously develop the notion of free-end homotopy which provides the same benefits as homotopy to motion planning, but for trajectories that *do not* share the same end point.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Free-end Homotopy Classes", "weight": 1.0} -->

In this section, we will introduce the notion of free-end homotopies that will facilitate faster planning by reducing the number of trajectory initializations for the joint optimization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 1", "weight": 1.0} -->

It should be clarified that homotopy is not enforced in an open-ended trajectory optimization problem and it is the limitation of gradient-based optimization that causes the local miminum issue. Nonetheless, studying homotopy offers an intuitive way to partition the solution space into disjoint subsets.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Directly checking Definition 1 ‣ III-A Background: Introduction to Homotopy ‣ III Free-end Homotopy Classes ‣ Interactive Joint Planning for Autonomous Vehicles") to verify if two trajectories belong to the same homotopy class is not straightforward. Multiple approximation methods and work-arounds have been proposed in the literature. use the relative lateral position (left or right) when two vehicles longitudinal location coincides to determine the homotopy class, yet the criteria is ambiguous as the direction of longitudinal and lateral is not clear in scenarios with curving roads and intersections. In the authors partition the free space into non-intersecting polytopes and use the order of region traversing to identify homotopy classes. However, free space partitioning is expensive and only works for static environments. A more common implicit approach is to use multiple trajectory samples as initialization for the gradient-based planner and hoping that one of the solutions is the global optimum. However, it is generally inefficient with random initialization as many optimization instances will converge to the same local minimum.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1", "weight": 1.0} -->

A key feature of planning for AVs is that the motion plan may not have a fixed end point. For instance, if we require the AV to progress along the road while avoiding obstacles, a particular goal state is not prescribed to the planner. To account for this, we will introduce the notion of free-end homotopy by using magnetic-field homotopy introduced.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Introduction to Magnetic-Field-Based Homotopy", "weight": 1.0} -->

The magnetic field approach for homotopy class verification is based on Ampere's law: which states that the line integral of magnetic field around a closed curve is equal to the product of the magnetic constant $\mu_{0}$ and the current enclosed $I_{\text{enc}}$. Ampere's law establishes an equivalence condition among all closed curves that encloses the same current, which can also be extended to curves sharing the same starting and ending position. Applying this to homotopy classes in motion planning, the authors in let obstacles carry current and calculate the Ampere circuit integral along the robot's trajectory, which is then used to categorize trajectories into different homotopy classes.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Introduction to Magnetic-Field-Based Homotopy", "weight": 1.0} -->

In 2D space, all obstacles can be viewed as having genus (number of holes) 0 and the imaginary current can be set perpendicular to the X-Y plane crossing the center of the obstacle. Furthermore, the path integral of the magnetic field is easy to compute in 2D; specifically, using Biot-Savart law, the magnetic field near an infinitely long wire at point $p$ with current $I$ perpendicular to the X-Y plane is given by and the direction follows the right-hand law. It follows that the path integral of the magnetic filed along a directional curve that does not intersect with $p$ is simply $\frac{\mu_{0}I}{2\pi}\Delta\theta$, where $\Delta\theta$ is the angular distance from the start to the end. Fig. 1 illustrates an example where the obstacle is marked in green and the imaginary current that goes through its center $p$, generating a magnetic field $\mathbf{B}$, visualized with the dashed lines. The path integral is then proportional to the angular distance from the start to the end point of the curve.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Introduction to Magnetic-Field-Based Homotopy", "weight": 1.0} -->

Note that the angular distance is directional and can be negative; when the curve circles $p$ counter-clockwise /clockwise once, the angular distance increases/decreases by $2\pi$, respectively. The angular distance provides two major benefits: (i) it is easy to compute and enforce as a constraint, and (ii) it can be easily extended to moving obstacles, as discussed next.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Free-end Homotopy", "weight": 1.0} -->

As mentioned above, the motion planning problem for AV may not have a fixed end point. Homotopy classes are not well-defined for two curves with different ending points. To resolve this issue, we introduce free-end homotopy, an extension of homotopy, for trajectories that share the same initial point but different end point. The overarching objective is to develop an equivalence class of trajectories, which we call free-end homotopy classes, whose members execute the same relative motion with respect to other agents (e.g., overtake from left of agent 1 and stay behind agent 2) while being continuously transformable to any other member in the class. Free-end homotopy classes facilitate efficient planning by allowing us to downsample motion plan candidates to only those that belong to different free-end homotopy classes, i.e., ones with different relative motions with respect to obstacles.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Free-end Homotopy", "weight": 1.0} -->

Let $\mathbf{x}$ be the trajectory of the ego and $\mathbf{x}^{o}$ be the trajectory of a particular obstacle. We begin by defining the *mode* $m:{{(\mathbf{x},\mathbf{x}^{o})}\mapsto{m{(\mathbf{x},\mathbf{x}^{o})}} \in {\mathbb{Z}}}$ of a trajectory with respect to a particular obstacle using the angular distances $\Delta\theta$: where $\hat{\theta}$ is a suitably large threshold for differentiating between the three modes. We refer to these three classes as clockwise (CW), stationary (S), and counter-clockwise (CCW), as illustrated in Fig. 2. In CW mode, the ego vehicle moves clockwise relative to the object, in CCW the ego vehicle moves counter-clockwise relative to the object, while in S, the ego vehicle remains roughly static relative to the object.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Modes with more refined quantization, e.g. consider ${\Delta\theta} \in {\lbrack{k\pi},{{({k + 1})}\pi}\rbrack}$, can be chosen. We chose only three categories as they were found to be sufficient to cover the typical driving scenarios.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 2", "weight": 1.0} -->

If there are $M$ obstacles in the scene, then the *mode vector* $h$ for an ego trajectory $\mathbf{x}$ is defined as the cartesian product of the modes with respect to each obstacle in the scene, i.e., ${h{(\mathbf{x},{\{\mathbf{x}_{i}^{o}\}}_{i = 1}^{M})}}:={({m{(\mathbf{x},\mathbf{x}_{1}^{o})}},\cdots,{m{(\mathbf{x},\mathbf{x}_{M}^{o})}})}$; Fig. 3 illustrates $h$ with an example scene with two cars near the ego vehicle and three example trajectories. With this, we are now ready to define free-end homotopy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D Applying free-end homotopy classes in motion planning", "weight": 1.0} -->

When initializing a motion planner, a naive choice is to consider all possible free-end homotopy classes, however, the number of free-end homotopy classes grows exponentially with the number of nearby objects and many of the classes are not realistic. For example, in the situation depicted in Fig. 3, CCW for the blue vehicle is not viable as there is not enough space to pass by its right side. For faraway objects, the free-end homotopy class is most likely S due to a small angular distance within the planning horizon.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Applying free-end homotopy classes in motion planning", "weight": 1.0} -->

To identify the promising free-end homotopy classes, we take a sampling approach. Specifically, we use a trajectory sampler to generate $N$ trajectory samples for the ego vehicle. Then we invoke a trajectory predictor to provide scene-centric trajectory predictions for all $M$ objects in the scene. Together there are $N \times M$ free-end homotopy class candidates that are expressed as mode vectors, as described in Section III-C. Among these $N \times M$ mode vectors, many result in repeated mode vectors. Leveraging Theorem 1 ‣ III-C Free-end Homotopy ‣ III Free-end Homotopy Classes ‣ Interactive Joint Planning for Autonomous Vehicles"), we only retain the trajectory with the highest reward among all trajectories sharing the same mode vector as a representative for the corresponding free-end homotopy class. The reward function can be any scalar-valued function that scores the performance of the ego trajectory sample amidst the objects' prediction.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Applying free-end homotopy classes in motion planning", "weight": 1.0} -->

Now that we are left with $K$ trajectories out of the $N \times M$ candidates, each with a unique free-end homotopy class for the whole scene, an ego trajectory sample and predictions for the objects. These $K$ trajectories are used to initialize the gradient-based motion planner in two ways: (i) the nonlinear planning problem is linearized around the ego and the objects' trajectories to create an efficiently-solvable sequential quadratic program (SQP), and (ii) the free-end homotopy class of the trajectory is enforced as a constraint in the planning problem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method", "weight": 1.0} -->

As discussed in the introduction, modern trajectory planners for autonomous vehicles rely on predictions for nearby agents, and ego-conditioning has been shown to improve the planning performance yet is expensive to run. The proposed IJP does not require ego-conditioned predictions, but replaces them with a joint optimization. Specifically, we invoke a prediction module to forecast the non-ego-conditioned future trajectories of the surrounding agents and pass them to the MPC planner. Intuitively, this prior supplies the optimizer with the non-ego agents' intent. The MPC planner then plans for both the ego vehicle and the surrounding agents to minimize the cost function, which we shall discuss in detail later, while enforcing collision avoidance constraint. In reality, the AV can only control its owm motion, thus assuming control over surrounding agents without any limitation is obviously naive. To remedy this, the cost contains two terms, a term that penalizes nearby agents' deviation from the predicted trajectories, and a term that penalizes their acceleration and jerk. These two terms are interpreted as the price for the ego to force nearby agents away from their nominal path.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Method", "weight": 1.0} -->

The resulting "planned" trajectories of nearby agents can be viewed as the ego-conditioned prediction that roughly centers around the unconditioned trajectory prediction. Fig. 9 illustrates the joint optimization as ego-conditioned prediction. The dashed line shows the unconditioned prediction for the blue agent, which comes from the trajectory predictor; the joint optimization then choose to let the ego (red) change lane and let the blue agent swerve to avoid a collision with the ego, which is viewed as the ego-conditioned prediction, and the deviation from the unconditioned prediction is penalized.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method", "weight": 1.0} -->

Since the prediction model is only called once without ego-conditioning, the inference time decreases significantly. Moreover, the joint optimization result provides a much finer granularity compared to running ego-conditioned prediction on ego trajectory samples.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Method", "weight": 1.0} -->

Next, we break down the key components of the joint MPC.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Dynamic constraints", "weight": 1.0} -->

We use a Dubin's car model for all vehicles and cyclists in the scene (including the ego vehicle). where $X,Y$ are the longitudinal and lateral coordinates, $v$ and $\overset{˙}{v}$ are the longitudinal velocity and acceleration, $\psi$ and $\overset{˙}{\psi}$ are the heading angle and yaw rate.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Dynamic constraints", "weight": 1.0} -->

The pedestrians follow a double integrator model with the following dynamics: These dynamic models are linearized around an initial guess of $x,u$ pair generated by a trajectory sampler as mentioned in Section III. The initial guess satisfies the nonlinear dynamic equations, and the linearized dynamic model takes the form $x^{+} = {{Ax} + {Bu} + C}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Dynamic constraints", "weight": 1.0} -->

Furthermore, we impose dynamic constraints on state and inputs of the agents. Specifically, for all vehicles, where $\lbrack v^{\min},v^{\max}\rbrack$ is the velocity range, $a_{y}^{\max}$ is the maximum lateral acceleration, $a_{x}^{\min}$ and $a_{x}^{\max}$ are the lower and upper bounds for longitudinal acceleration, $\delta^{\max}$ is the maximum steering angle and $l$ is the distance between the front and rear axles. All pedestrians follow a simple norm bound on velocity and acceleration: The dynamic constraints are linearized (especially so that the effect of velocity is accounted for) and the linearized constraints is written as ${{G_{x}^{d}x} + {G_{u}^{d}u}} \leq g^{d}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Safety constraints", "weight": 1.0} -->

Safety constraints mainly consist of two parts, collision avoidance constraints and lane boundary constraints.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Safety constraints", "weight": 1.0} -->

All vehicles are modeled as rectangles with varying size (including the ego) and the pedestrians are modeled as a circle with varying radius. The collision avoidance between the ego (rectangle) and pedestrians (circles) is encoded by checking the three cases where the maximum margin is achieved on the X axis, Y axis, and corners of the vehicle, as shown in Fig. 5. For two vehicles, we analytically calculate the 4 polytopic free spaces around one of the vehicles, as shown in Fig. 5, and enforce linear constraints that the other vehicle's 4 corners and center point all lie in one of the free spaces. Then we do the same after reversing the role of the two vehicles.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Safety constraints", "weight": 1.0} -->

Lane boundaries are given as polylines (sequence of waypoints with headings), the lane boundary constraints are enforced by projecting the vehicle centers to the polylines and calculate the distance margins, as shown in Fig. 6.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C Costs and MPC QP setup", "weight": 1.0} -->

The cost function consists of 5 terms: Penalty on ego vehicle's tracking error w.r.t. the reference trajectory Penalty on ego vehicle's acceleration and jerk Penalty on nearby agents' deviation from their unconditioned trajectory prediction Penalty on nearby agents' acceleration and jerk Putting all components together, the joint MPC solves the following QP: where $x_{e}$ is the future state of the ego vehicle, $x_{o_{i}}$ is the future state of agent $i$, $A,B,C$ are the matrices corresponding to the dynamic equality constraints, $G_{x}^{d},G_{u}^{d},g^{d}$ are matrices corresponding to the input and state bounds, $G_{e}^{s},G_{o}^{s},g^{s}$ define the safety constraints, including collision avoidance, lane boundary, and the homotopy constraint.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Costs and MPC QP setup", "weight": 1.0} -->

The costs include $\mathcal{J}_{\text{ref}}$ that prompts the ego vehicle to track the desired trajectory, $\mathcal{J}_{\text{u}}$ that penalizes acceleration and jerk (both angular and linear), and $\mathcal{J}_{\text{dev}}$ that penalizes agents' deviation from their predictions. $\eta_{e}$ and $\eta_{o}$ determine the distribution of emphasis on the ego vehicle and the agents. A large $\eta_{e}$ leads to more selfish and intrusive behavior of the ego and a small $\eta_{e}$ leads to more altruistic ego behavior.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-D Interactive Joint Planning", "weight": 1.0} -->

The IJP planner is summarized in Algorithm 1. The inputs are the reference trajectory for the ego vehicle given by some high-level planner, scene context $\mathbf{C}$, lane information $\mathbf{L}$, and the current state of the ego and surrounding agents.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-D Interactive Joint Planning", "weight": 1.0} -->

Firstly, IJP calls the trajectory prediction model to generate predictions for the $M$ surrounding agents from the scene context $\mathbf{C}$. IJP can work with any prediction model that generates dynamically feasible trajectories for the agents involved. It is preferred that the prediction is scene-centric, i.e., predicting joint trajectories for all agents involved. We use Agentformer as our default predictor because it is scene-centric, and is shown to work well with the downstream planner.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-D Interactive Joint Planning", "weight": 1.0} -->

1:procedure IJP(xref, C, L, xe0, xo0) 2: {xo, jpred}j = 1M ← Traj_pred (C) 3: {xe, isample}i = 1N ← Ego_sampling (xe0, L) 4: {(xe, k, xo, k, hk)}k = 1K ← Hom_sel ({xe, isample}i = 1N, xopred) 7: QPk ← Linearize (xref, xe, k, xo, k, hk, xe0, xo0, L) 11: return xe associated with the best homotopy class.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-D Interactive Joint Planning", "weight": 1.0} -->

Ego_sampling takes the ego state and lane information to generate ego trajectory samples with a spline sampler introduced, which is then used to identify promising homotopies with the predicted trajectories of the surrounding agents in Hom_sel. With the homotopies selected, IJP uses automatic differentiation to linearize the costs, constraints, and dynamics to formulate a quadratic program. JAX is used for auto-differentiation, and thanks to its powerful parallelization functionality and Just-In-Time (JIT) compilation, the linearization can be done simultaneously for all homotopy classes. The generated QP is solved with 3rd party QP solvers such as GUROBI and Forces Pro. In a sequential quadratic programming (SQP) manner, the nonlinear trajectory optimization problem is linearized and solved as a QP for multiple rounds, each round takes the solution from the last round as the updated linearization point. A proximal constraint is also added to limit the difference of solutions in between rounds to stabilize the SQP.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3", "weight": 1.0} -->

When the trajectory prediction module outputs multimodal predictions of the surrounding agents, the criteria for selecting the optimal solution among the candidate homotopy classes should also take into account the likelihood of the prediction modes, however, we observed that the mode probabilities predicted by the prediction module is usually of bad quality and thus we ignore the mode probability in the final solution selection and simply choose the mode with the lowest cost. We shall investigate how to incorporate prediction likelihood in solution selection in future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Simulation evaluation setup", "weight": 1.0} -->

We conduct closed-loop simulation in nuPlan to evaluate the proposed approach. The closed-loop planner consists of three modules, a trajectory predictor that generates the unconditioned trajectory prediction, a route planner that distills lane information and reference trajectory from the lane graph, and IJP that plans the trajectory, as shown in Fig. 8.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Simulation evaluation setup", "weight": 1.0} -->

We use AgentFormer as the trajectory predictor without ego-conditioning, which generates 4 samples of predicted future trajectories lasting for 3 seconds.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Simulation evaluation setup", "weight": 1.0} -->

Route planner. The route planner takes the lane graph and the ego state as input, and performs a depth-first search to identify the optimal lane sequence. In nuplan simulation, no goal location is provided, instead the lane segments are labeled as "on-route" or "not on-route". The route planner's search criteria is to find the an on-route lane sequence (up to a certain depth) that balances (i) distance to the ego vehicle (ii) length of the lane plan and (iii) total curvature of the lane plan. With a lane sequence selected, the reference trajectory is generated by projecting the ego's current position to the lane centerline and interpolating given the desired ego velocity.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Simulation evaluation setup", "weight": 1.0} -->

To keep the QP complexity tractable, IJP only include a subset of nearby agents in the joint optimization, denoted as EC agents; the rest of the agents are denoted as non-EC agents and IJP simply encode collision avoidance constraint with their predicted trajectories. The assignment of EC and non-EC agents is based on their minimum distance to the ego vehicle along their predicted trajectories. When there are less agents than the prescribed number, the MPC QP is padded with dummy agents.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Simulation evaluation setup", "weight": 1.0} -->

To avoid frequent JIT compilation, the number of EC agents and non-EC agents are fixed so that the MPC QP maintains a fixed problem dimension. When the number of nearby obstacles is larger than the sum of the prescribed number of EC and non-EC agents, far away obstacles are simply ignored.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Simulation evaluation setup", "weight": 1.0} -->

We compare the performance of IJP to two baselines: (i) non-EC MPC: IJP without joint optimization, which only plan the ego behavior and try to avoid collision with the predicted trajectories of nearby agents. (ii) TPP: a sampling-based planner using ego-conditioned prediction, similar to TPP but without multi-layer policy planning.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4", "weight": 1.0} -->

For fairness of comparison, the non-EC MPC considers a fixed number of non-EC agents, and the number is equal to the sum of EC agents and non-EC agents considered by IJP. The TPP planner instead considers all agents detected as the sampling-based algorithm does not require a fixed number of agents.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Simulation result", "weight": 1.0} -->

Fig. 9 shows an example snapshot from the nuPlan simulation of IJP where the two plots are the MPC solutions under two homotopy classes. The only difference between the two homotopy classes is the homotopy w.r.t. the circled vehicle: S (static) in the left case and CW (clockwise) in the right case. The blue curve is the solution of the EC agents' trajectories "planned" by IJP. In the right plot, as the ego (red) change lane, the trailing vehicle changes lane to the right to avoid collision with the ego vehicle, which is indeed similar to an ego-conditioned prediction.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Simulation result", "weight": 1.0} -->

Quantitatively, we run closed-loop simulation of 50 scenes from nuPlan's Boston dataset which include many interesting interactive scenarios with sophisticated road geometry. We compare key metrics such as collision rate and progress, all collected from the nuPlan simulator under IJP and the baselines, shown in Table I.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Simulation result", "weight": 1.0} -->

It is counter-intuitive that the non-EC MPC result in worse safety performance given that it fully "respects" the prediction. We suspect that the main reason is when there are multiple agents near the ego vehicle, the prediction makes the motion planning problem infeasible (without slack), and when the prediction is of poor quality, the planner overreact, causing the performance to deteriorate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Simulation result", "weight": 1.0} -->

Table II shows the computation time of IJP and the baselines. Agentformer runs on a Nvidia 3090 GPU and the MPC QP runs on the CPU with Forces Pro QP solver. We separate the build and solve time of the MPC QP because the build process generates all MPC QP instances under different homotopy classes in parallel, while the solve time corresponds to solving one of the QP instances. Comparing to the non-EC MPC, IJP takes longer to build and solve as the QP problem is larger. Comparing to TPP, while IJP takes longer to solve, it saves more time on the prediction phase as no ego-conditioned prediction is needed.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 5", "weight": 1.0} -->

TPP without ego-conditioning would have the same prediction time as IJP, but the final score dropped to 0.64 due to more safety violations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 6", "weight": 1.0} -->

The computation time of IJP can be further improved in at least two ways: parallelizing the solving process of MPC QP under multiple homotopy classes, and utilizing the sparsity pattern in the QP. It is promising that IJP can run at a sufficiently high frame rate for real-time planning with these two improvement.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion and discussion", "weight": 1.5} -->

We presented a new planning method, IJP, that can reason about the impact of the ego's actions on the behavior of other traffic agents by combining gradient-based joint planning for all agents with modern deep learning-based predictors. The key idea behind IJP is viewing joint optimization solutions as ego-conditioned predictions and penalizing deviations from the unconditional predictions to regularize the EC predictions. It should be pointed out that the EC predictions currently lack statistical grounding, i.e., no supervision is added in the prediction model training process to force the result of the subsequent joint optimization to match the ego-conditioned ground truth. The main missing piece is counterfactual traffic data, which is not available in general. The behavior of IJP largely depends on hyper-parameters such as $\eta_{e}$ and $\eta_{o}$, and currently they are hand-tuned. Nonetheless, the closed-loop performance of IJP turned out significantly better than the baselines, and we believe the main reasons are the free-end homotopy that diversifies the search space, and the fine granular solution achieved by the joint optimization.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and discussion", "weight": 1.5} -->

For future work, we will focus on providing a solid probabilistic grounding for the joint optimization solution viewed as ego-conditioned prediction by differentiating through the optimization and training the prediction-planning modules end-to-end.
