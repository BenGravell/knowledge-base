<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning-Aided Warmstart of Model Predictive Control in Uncertain Fast-Changing Traffic

Topics include Nonconvex optimization, Model predictive control, Predictive control, Vehicles, Safety, Neural networks, Sampling-based methods, Control, Learning, Sampling, Monte Carlo methods.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model Predictive Control lacks the ability to escape local minima in nonconvex problems. Furthermore, in fast-changing, uncertain environments, the conventional warmstart, using the optimal trajectory from the last timestep, often falls short of providing an adequately close initial guess for the current optimal trajectory. This can potentially result in convergence failures and safety issues. Therefore, this paper proposes a framework for learning-aided warmstarts of Model Predictive Control algorithms. Our method leverages a neural network based multimodal predictor to generate multiple trajectory proposals for the autonomous vehicle, which are further refined by a sampling-based technique. This combined approach enables us to identify multiple distinct local minima and provide an improved initial guess. We validate our approach with Monte Carlo simulations of traffic scenarios.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) has established itself as a popular technique in Motion Planning and Control for autonomous driving. This is attributed to its inherent capability to simultaneously account for collision constraints, dynamic feasibility, actuator constraints, and comfort criteria, enabling the generation of optimal trajectories. A notable variant that we also use is Model Predictive Contouring Control (MPCC). It generates consistent lateral and longitudinal control signals and does not require a separate desired velocity specification. However, due to constrained computational resources, MPC relies on local optimization, employing simple models and limited planning horizons, potentially resulting in suboptimal or locally optimal (short-term) solutions. Conversely, learning-based approaches can excel where MPC falls short e.g., in efficiency and adaptability in complex tasks, without needing physical models. However, they face challenges in interpretability and reliability, especially in unexplored corner cases. This can potentially lead to hazardous behavior, hindering their suitability for critical applications. Hence, due to their complementary attributes, several methods propose approaches to combine MPC with learning-based approaches.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning-based MPC can be broadly categorized into two groups. The first group employs a learning-based system to substitute or enhance components of MPC. Simplest are approaches that learn the weights of the cost function, as these significantly impact MPC performance and can be challenging to tune manually. A similar technique is cost shaping which adjusts the cost function at each time step, mitigating MPC's limitation in finding only short-term optimal solutions. Other methods learn the state-space model or parts of it to handle unknown or complex dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach of a learning-based warmstart also falls into this group, together. Here, the learned system offers an initial guess to the MPC optimizer, which is then further optimized by the MPC. This concept is particularly compelling given the inherent limitations of Local Optimizers/MPC, that become apparent in the context of autonomous driving in complex scenarios. The first well-known deficiency of the local optimizer is that if the initial guess is far from the optimum, many steps are needed until it converges, or the optimization may not converge at all. The strategy of MPC to provide an initial guess is to use the optimal trajectory, which was calculated in the last timestep, assuming little change between the previous and current timestep. This strategy fails in uncertain and rapidly changing environments where the optimization problem can vary a lot between each timestep (s. Fig. 1). For instance, due to unknown intentions of human drivers, predictions of how traffic participants act may vary significantly between timesteps. These abrupt changes can lead the optimizer to struggle to recover or find a proper solution in time, potentially resulting in fatal behavior where e.g., collisions cannot be avoided.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the event of optimizer failure, a common approach is to use the same control input as in the last timestep. However, when the environment is changing rapidly, the scene can change even more in the time step after and now using the solution from two timesteps ago only exacerbates the problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second deficiency of only being able to find a local optimum is especially problematic in dense traffic with (moving) obstacles. These obstacles are generally the cause for non-convex problems with multiple local minima. Some of these minima lead to undesired behavior, such as overly conservative driving or peculiar overtaking maneuvers. This problem is often mitigated by decomposing the planning problem into a global and a local planner. In this setup, the global planner generates a rough trajectory with significant simplifications for real-time feasibility, potentially sacrificing optimality. Also, topology-based planners such as can address this weakness, from which we adopt the concept of homotopy classes. But, these planner also do not address the previously mentioned weakness of conventional warmstarting in fast-changing environments that our method tackles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, previous works for learning-based warmstarting are mainly designed for simple repeating tasks. For example, they do not consider constraints, especially moving obstacles, or are trained for a limited number of self-generated scenarios (which additionally require retraining when the weights of the MPC cost function change).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of our work are summarized as: Designing a Motion Planner based on Model Predictive Contouring Control with Artificial Potential Fields Developing a learning-aided warmstart strategy which improves convergence quality in fast-changing unknown scenarios and helps to prevent undesired local minima leveraging the concept of homotopy classes Devising a time-efficient framework with a novel trajectory refinement process which makes arbitrary multimodal trajectory predictors learned on real-world datasets easily deployable.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Baseline Model Predictive Contouring Control", "weight": 1.0} -->

We model the motion of the AV by a differential equation ${\overset{˙}{\mathbf{z}}{(t)}} = {f{({{\mathbf{z}}{(t)}},{{\mathbf{u}}{(t)}})}}$ using the kinematic bicycle model: where ${\mathbf{z}} = {\lbrack x,y,\psi,v,a,\delta\rbrack}^{\top}$ is the state vector, ${\mathbf{u}} = {\lbrack j,\overset{˙}{\delta}\rbrack}^{\top}$ is the control input vector and the velocity, acceleration, steering angle, jerk, steering angle rate, and wheelbase are denoted as $v,a,\delta,j,\overset{˙}{\delta},l$, respectively.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Baseline Model Predictive Contouring Control", "weight": 1.0} -->

For the MPC-formulation, the dynamic model is discretized to ${\mathbf{z}}_{k + 1} = {f{({\mathbf{z}}_{k},{\mathbf{u}}_{k})}}$ with the sampling time $T_{s}$. The MPCC aims to maximize path progress while minimizing path error, balancing between the two objectives. For that, we approximate the arclength (i.e. progress on the path) $\theta_{k}$, the lag error ${\hat{e}}_{k}^{l}$ and the contouring error ${\hat{e}}_{k}^{c}$ (s.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Baseline Model Predictive Contouring Control", "weight": 1.0} -->

Fig 2): where ${\Delta{\mathbf{p}}_{ref}} = {\lbrack{x - {x_{ref}\left(\theta_{k} \right)}},{y - {y_{ref}\left(\theta_{k} \right)}}\rbrack}^{\top}$ and $v_{k}^{p}$ is the virtual speed on the path. Eq. 2 is augmented to the dynamic model, i.e. $v_{k}^{p}$ is an additional control input and $\theta_{k}$ a further state. This is utilized to define the running cost: where $Q,q_{v},R$ are the respective weights. We extend the formulation of to account for moving obstacles and lanes using the Potential Field method.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Baseline Model Predictive Contouring Control", "weight": 1.0} -->

where ${\Delta x_{k}^{i}},{\Delta y_{k}^{i}}$ are the distances to the respective obstacle, $d_{lm}^{l}$ is the signed distance from the reference path to the respective $L$ lane marker, $\sigma$ a scaling factor and $l^{i},w^{i}$ a conservative estimation of the length and width of the obstacle and $q_{ob},q_{lm}$ are the respective weights. Additionally, for the hard constraints we employ ellipses to approximate the occupied area by the obstacles and utilize a union of three circles to approximate the ego's occupied space. With that, we approximate the Minkowsky sum as described. The trajectories of the obstacles are provided by the prediction module which will be introduced in the next section.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Baseline Model Predictive Contouring Control", "weight": 1.0} -->

To ensure that the AV stays within the road boundaries, we impose linear constraints Box constraints are imposed on the control inputs $j_{k} \in {\lbrack j_{\text{min}},j_{\text{max}}\rbrack}$ and ${\overset{˙}{\delta}}_{k} \in {\lbrack{\overset{˙}{\delta}}_{\text{min}},{\overset{˙}{\delta}}_{\text{max}}\rbrack}$. Additionally, we limit $\delta$, $a$, and the lateral acceleration to ensure that the trajectories are feasible for the vehicle. This leaves us with the nonconvex optimization problem: where $\mathcal{Z}$ is set of state constraints imposed by road boundaries, obstacles, and lateral acceleration, $\mathcal{U}$ is the set of box constraints on the control inputs and $J_{N}{({\mathbf{z}}_{N})}$ is the terminal cost.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Motion Predictor for Trajectory Proposals", "weight": 1.0} -->

Motion prediction models reason about the map, the historical trajectories of objects, and their interactions to forecast objects' future movement. However, determining the intentions of other traffic participants considering the various choices an agent can make (e.g. whether a car will overtake or follow a leading vehicle) is challenging. To address this challenge, many learning-based motion prediction models opt to provide *multimodal* predictions. Motion Transformer (MTR) and Wayformer, are examples of such multi-modal predictors trained on large-scale motion prediction datasets, such as Waymo Open Motion (WO). In our method, we employ MTR which outputs a Gaussian Mixture Model (GMM) for the object's future position $\mathcal{N}{({\mathbf{μ}}^{m},\mathbf{\Sigma}_{in}^{m})}$ at every timestep. Each component $m \in \mathcal{M}$ of this mixture corresponds to one predicted mode.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Motion Predictor for Trajectory Proposals", "weight": 1.0} -->

We capitalize on the necessity of the predictor for obstacle prediction^11^1In this study, we use the most probable obstacle prediction. Planning with multimodal obstacle predictions remains future work. and reutilize it for predicting the ego trajectory. The aim of our approach is to leverage the multimodal output of the predictor to identify multiple local optima and select the best one. To elaborate on that, we introduce the concept of homotopy classes in the context of motion planning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Several of the predicted modes do not share the same homotopy class and cover a subset of the existing homotopy classes $h \in \mathcal{H}$, i.e. ${|{\left. \{{\lbrack m\rbrack} \middle| {m \in \mathcal{M}}\} \right. \cap \mathcal{H}}|} \geq 2$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The covariance of the components of the GMMs i.e. for the respective mode is small enough such that trajectories drawn from the same components correspond to the same homotopy class (s. Fig. 4).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Subsequently, we introduce how to utilize and further refine these provided modes to be able to select the best one (in terms of cost) as a warmstart.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Bezier Curve Fitting", "weight": 1.0} -->

Typical trajectory predictors such as MTR predict only the object position distributions at every prediction timestamp. However, we require the complete state and control input trajectories for our warmstart. Furthermore, our method is required to sample realistic trajectories from the given distribution to further refine the predictor trajectory.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Bezier Curve Fitting", "weight": 1.0} -->

We select 5th-degree Bezier Curves to fit the predicted positions. They represent the optimal solutions in terms of travel time, control effort, and jerk and thus are close to the optimal vehicle trajectories outputted by the MPC. This smooths the often jerky predictions and allows us to calculate derivatives analytically. Further, we can perform this fit in such a way as to match current kinematic state. This continuity constraint is not directly enforced by MTR. We perform the fitting using Bayesian Linear Regression (BLR) to output a distribution over the curve parameters from which we can sample in the next step.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Bezier Curve Fitting", "weight": 1.0} -->

The 5th-degree Bezier Curve ${\mathbf{c}}{(t)}$ can be expressed as a linear combination of 6 control points ${\mathbf{P}}_{j} \in {\mathbb{R}}^{2}$ and the Bernstein polynomials ${\phi_{j}{(t)}}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$: From the temporal derivatives of the Bezier curve, we can then calculate the state and control input trajectories.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Bezier Curve Fitting", "weight": 1.0} -->

Hence, we first need to estimate the control points ${\mathbf{P}}_{j}^{m}$ from the output of the predictor for each mode. The initial guess should ideally satisfy the continuity constraint ${\mathbf{z}}_{0} = {{\mathbf{z}}{}}$. For this, we exploit the property of the Bezier curve that the initial conditions can be determined from the control points.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Bezier Curve Fitting", "weight": 1.0} -->

In other words, the first three elements of ${\mathbf{P}}^{m,0}$ correspond to eq. III-B, and $\mathbf{\Sigma}^{m,0}$ are derived from the tracked uncertainty of the states from the on-board sensors. As for the remaining three elements in ${\mathbf{P}}^{m,0}$, we employ an uninformed prior.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Control Point Sampling and Cost-Weighted Averaging", "weight": 1.0} -->

Simply calculating the states and control inputs from each outputted modes of the predictor leads often to an ineffective warmstart. Even if the best homotopy class is chosen from these modes, it can still lead to a solution far from the optimum, resulting in a prolonged convergence time.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Control Point Sampling and Cost-Weighted Averaging", "weight": 1.0} -->

Furthermore, recall Assumption 2, i.e.; consequently, we assume the samples are in the attractive vicinity of a local minimum. Provided the samples are well distributed around the region of convexity of this local optimum, taking the weighted average of the trajectories gives us a value inside the area spanned by the sample points. Hence, the output results generally in a trajectory closer to the minimum.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Control Point Sampling and Cost-Weighted Averaging", "weight": 1.0} -->

We execute this process for each mode. Subsequently, the costs for each mode are compared, and the best one is employed as the warmstart. While this still does not guarantee the selection of the homotopy class of the global optimum, it allows us to choose a satisfactory local minimum at least. In autonomous driving, various maneuvers are often similarly satisfactory, and only undesired local minima must be prevented.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Control Point Sampling and Cost-Weighted Averaging", "weight": 1.0} -->

The detailed steps of the trajectory refinement are outlined in Algorithm 1. It is important to note that this approach supports parallel computation due to the parallel nature of sampling and the independence of each trajectory from one another, i.e., it can take advantage of the parallel processing capabilities of modern GPUs, making it highly efficient.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Control Point Sampling and Cost-Weighted Averaging", "weight": 1.0} -->

Input: Measured state values zk = [xk, yk, ψk, vk, ak, δk, θk]⊤, optimal traj.last timestep Zk − 1*, Uk − 1*, map information Mr, reference path 𝒫ref, pose history ηok ∀ Agents o with o = 0 denoting the ego vehicle Output: Initial Guess for MPCC Z0, U0 Initialize # refinement samples S, # used modes M // Fit predicted ego trajs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Control Point Sampling and Cost-Weighted Averaging", "weight": 1.0} -->

${{\mathbf{Z}}^{m},{\mathbf{U}}^{m},J^{m}}\leftarrow{\mathcal{J}{({\overline{\mathbf{P}}}^{\mathbf{m}},\mathcal{P}_{ref},{\mathbf{ξ}}_{1:O}^{0})}}$ // Select mode with minimal cost m* ← arg min mJm if Jm* ≤ Cost of Zk − 1*, Uk − 1* at timestep k then Algorithm 1 Learning-aided Warmstart Average Solving time (std) TABLE I: Results of experiment III. Comparison of Baseline and the learning-aided Framework using Monte Carlo analysis

<!-- chunk {"id": "body-0031", "role": "body", "section": "Performance Evaluation", "weight": 1.0} -->

Experiment $I$ involves a scenario with two lanes, where the left lane accommodates oncoming traffic but allows for overtaking. This scenario is well-suited to showcase the capability of our framework in escaping undesired local minima, as the presence of other traffic participants introduces non-convexity to the optimization problem. In, it is demonstrated that a planner in this scenario may converge towards several distinct local minima/homotopy classes. In our case, our learning-aided warmstart leads to a different behavior compared to the MPCC without warmstart (s. Fig. 5); i.e., the two planners converge towards two distinct local optima. The costs for our planner are significantly lower than those for the baseline planner (s. Fig. 5). This figure also provides a comparison of the control input trajectories and the minimum time-to-collision (TTC) for both planners in this scene, displaying the shortcomings of the local minima the baseline converged to.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Performance Evaluation", "weight": 1.0} -->

Experiment II involves a scenario where an obstacle crosses the path of the ego vehicle. Initially, the ego vehicle is unaware of this occurrence for the first few moments, causing a sudden shift in the optimization problem for the planner. Such a situation can arise in various scenarios, for instance, when the obstacle is initially occluded or when predictions change (due to unknown intentions of traffic participants or a new decision of an object). In this case, the planner must be capable of finding a solution for the new optimization problem in real-time, even though it differs distinctly from the last timestep. Hence, we impose a maximum solving time constraint. However, we set this limit relatively high with $t_{\text{max}} = {0.5s}$ since there is potential to accelerate the MPC runtime through alternative implementations and hardware enhancements, etc. Despite this high maximum solving time, the baseline planner is unable to converge in time when the change occurs (from the new event at $t_{e} = 1.6$ in Fig. 6). The red curve depicts the velocity trajectory outputted by the solver. This trajectory fails to satisfy both collision constraints and the initial condition.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Performance Evaluation", "weight": 1.0} -->

In such cases, it is customary to utilize the solution from the last time step, which, in this example, leads to further acceleration of the ego. This behavior ultimately results in an unavoidable collision. In contrast, Fig. 6 depicts that our approach can directly provide an appropriate warmstart after the event.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Performance Evaluation", "weight": 1.0} -->

For experiment III, we consider a highway merging scenario (s. Fig. 1) and utilize the Intelligent Driver Model to simulate the behavior of the traffic participants. We generate 100 test runs by randomly sampling the parameters of the IDM model (such as desired velocity, minimum headway, etc.), as well as the initial positions and velocities for the ego vehicle and the other vehicles. As a result, we compare the rate of successful mergings, the percentage of the ego getting stuck in the entrance lane, and collisions. Additionally, we assess the convergence quality in terms of the percentage of successful convergence, failed convergence due to reaching the time limit, and failed convergence due to converging to a point of infeasibility. Further benchmarking parameters are the average cost and solving time^22^2Solving time data is for comparative purposes only and should not be taken as absolute. The significant performance improvement to the baseline becomes evident when considering highway merging. Firstly, each gap between traffic participants potentially corresponds to a local minimum where one can clearly be better than the other e.g., due to gap size.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Performance Evaluation", "weight": 1.0} -->

Secondly, shifts in motion predictions of the traffic participants during merging often substantially impact the ego vehicle's plan e.g., if a prediction changes the acceleration slightly, the optimal plan for the ego may shift from merging in front to merging behind.

<!-- chunk {"id": "body-0036", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

A Learning-aided Warmstart Framework is proposed to address the problem of Model Predictive Control with local minima and convergence issues if using the conventional warmstart strategy in fast-changing, uncertain environments. This framework leverages a multimodal predictor that predicts trajectories for traffic participants and the ego vehicle, respectively. The different ego trajectory modes are used to identify multiple homotopy classes, each associated with an attractive vicinity of a different local optimum. To achieve this, we introduced a novel sampling-based trajectory refinement approach using Bayesian Linear Regression for Bezier Curve Fitting to efficiently optimize the trajectories before selecting the best one as an initial guess. Our Monte Carlo analysis demonstrates that our framework significantly improves the convergence quality in highway merging scenarios.
