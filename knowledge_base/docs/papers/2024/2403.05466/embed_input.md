<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Grasping Trajectory Optimization with Point Clouds

Topics include Trajectory optimization, Robotics, Online algorithms, Optimization, Planning, Point cloud.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a new trajectory optimization method for robotic grasping based on a point-cloud representation of robots and task spaces. In our method, robots are represented by 3D points on their link surfaces. The task space of a robot is represented by a point cloud that can be obtained from depth sensors. Using the point-cloud representation, goal reaching in grasping can be formulated as point matching, while collision avoidance can be efficiently achieved by querying the signed distance values of the robot points in the signed distance field of the scene points. Consequently, a constrained nonlinear optimization problem is formulated to solve the joint motion and grasp planning problem. The advantage of our method is that the point-cloud representation is general to be used with any robot in any environment. We demonstrate the effectiveness of our method by performing experiments on a tabletop scene and a shelf scene for grasping with a Fetch mobile manipulator and a Franka Panda arm. The project page is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In robot manipulation, planning a robot trajectory to grasp an object is a fundamental research problem. The problem is challenging since it requires motion planning to avoid obstacles in the task space and grasp planning to decide how to grasp a target object. Traditionally, the motion planning problem and the grasp planning problem are tackled separately. Motion planning approaches focus on finding a collision-free path to reach a given end-effector goal. For example, sampling-based motion planning methods such as Rapidly exploring Random Trees (RRTs) and Fast Marching Tree (FMT) find robot trajectories by incrementally building configuration space filling trees through directed sampling. Optimization-based motion planning methods solve optimization problems to find robot trajectories that minimize some loss functions and obey certain constraints, such as joint limits.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since these motion planning algorithms need to have a given goal, they cannot be applied directly to robot grasping unless a grasping goal is given. On the other hand, grasp planning methods such as GraspIt!, 6D GraspNet and SE-DiffusionFields aim to synthesize grasps of robot grippers given 3D models or 3D point clouds of objects. These methods focus on planning the poses of robot grippers to grasp various objects. However, they do not consider the motion of the robotic arm to reach the planned grasps.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Combining grasp planning and motion planning can address the robot grasping problem. A straightforward approach is first to utilize a grasp planning method to generate grasps of a target object and then employ a motion planning method to plan a robot trajectory to reach one of the grasps. A naive way is to loop over all the planned grasps until the motion planner finds a collision-free path to reach one of the grasps. This naive approach is complete, that is, as long as there is one plausible grasp from the grasp planner, the method can find a path to reach it. However, it is very slow, especially when the number of planned grasps is large. Therefore, a number of approaches are proposed to address the problem of joint motion and grasp planning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similarly to motion planning methods, these joint motion and grasp planning methods can be categorized into sampling-based and optimization-based ones. Sampling-based methods bias a motion planner to sample nodes that are closer to better grasps, and the grasps are synthesized online. The main limitation of these approaches is that the online synthesized grasps may not be accurate enough for precise grasping, especially for objects with complicated shapes. To overcome this limitation, several goal-set-based trajectory optimization methods are proposed. These methods first utilize an offline grasp planner to generate grasps of objects, where well-designed grasp planners can be used, such as grasps synthesized from physics simulation. These generated grasps are treated as goals in a goal set. The joint motion and grasp planner optimizes a collision-free trajectory that can reach one of the goals in the goal set. The goal set introduces a constraint on the last configuration of the robot trajectory. Using high-quality grasps as goals, these approaches can handle various objects in grasping.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, motivated by the goal-set-based trajectory optimization framework for joint motion and grasp planning, we introduce a new trajectory optimization method for robotic grasping. Compared to previous methods, our method has the following advantages. First, we introduce a point-cloud representation of robots and task spaces for goal reaching and obstacle avoidance. Point clouds of robots are generated using the 3D meshes of the robot links, whereas point clouds of the task space can be obtained from depth sensors such as RGB-D cameras. Figure shows the point cloud representation with the planned trajectories of a Fetch robot and a Franka Panda arm. This representation is general and can be used with any robot and any task space. Second, we formulate a constrained trajectory optimization problem using point-cloud representation for joint motion and grasp planning. Given a set of grasping goals, solving the optimization problem generates a trajectory to reach one of the goals that minimizes the objective function subject to certain constraints, such as joint limits.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead of converting the constrained optimization problem into an unconstrained one and solving with first-order gradient descent-based techniques as, we utilize the Interior Point OPTimizer (Ipopt) to solve the large-scale nonlinear optimization problem for trajectory planning, which can find better solutions compared to first-order solvers. Finally, we empirically verify our method on two robot grasping environments in the PyBullet simulator, i.e., a tabletop scene and a shelf scene, and demonstrate a significant improvement over the OMG-Planner in terms of metrics on grasping success and collision avoidance. In addition, we conducted real-world grasping experiments according to the SceneReplica benchmark. Our method improves over a sampling-based baseline in real-world experiments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Manipulation Trajectory Optimization", "weight": 1.0} -->

Trajectory optimization techniques have been successfully applied to robot manipulation. Early work such as CHOMP and related methods optimize a cost functional using covariant gradient descent. STOMP uses stochastic sampling of noisy trajectories to optimize nondifferentiable costs. TrajOpt solves a sequential quadratic program, while GPMP2 formulates the problem as inference on a factor graph and finds the maximum a posteriori trajectory by solving a nonlinear least-squares problem. More recently, various trajectory optimization methods have been proposed to solve specific manipulation problems. For example, TORM is introduced to follow given end-effector paths. solves a trajectory optimization problem for the manipulation of deformable objects. solves a whole-body trajectory optimization for mobile manipulation. The advantage of trajectory optimization lies in its flexibility in introducing different cost functions and constraints for various problems. In this work, we solve a trajectory optimization problem for joint motion and grasp planning in robotic grasping.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Joint Motion and Grasp Planning", "weight": 1.0} -->

Traditionally, arm motion planning and grasp planning are tackled separately, which can result in suboptimal grasping trajectories. Since jointly optimizing trajectories and grasps is challenging, several approaches are proposed to solve a goal-constrained trajectory optimization problem for joint motion and grasp planning, where grasps from a grasp planner such as GraspIt! are used as goals. For example, projects the robot configuration of the last time step in the goal set during trajectory optimization. OMG-Planner iterates between goal selection and trajectory optimization based on CHOMP. Recently, SE-DiffusionFields learns a cost function for grasp planning based on a diffusion model and then solved a joint optimization problem for grasp and motion planning. Unlike these methods, we introduce a cost function for goal reaching using our point-cloud representation and solve a constrained optimization problem for joint motion and grasp planning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A A Point-Cloud Representation for Robots and Task Spaces", "weight": 1.0} -->

In robot motion planning, the goal is to generate a robot trajectory to reach a goal location while avoiding obstacles in the task space. The geometric representation of robots and the task space is a critical component of robot motion generation. A natural choice is to use 3D meshes of robots and objects in the task space. However, the limitation of using 3D meshes is that we cannot always obtain 3D meshes of objects, and collision checking between meshes is expensive. Another choice is to approximate robot links and obstacles in the task space with 3D shape primitives such as spheres, boxes, or cylinders. Using 3D shape primitives simplifies collision checking, but results in inaccurate collision checking, where motion plans can be conservative. In this work, we utilize a simple geometric representation of objects and the task space, i.e., point clouds, for robot motion planning based on trajectory optimization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A A Point-Cloud Representation for Robots and Task Spaces", "weight": 1.0} -->

Given a robot description using the Unified Robotics Description Format (URDF), each robot link has an associated 3D mesh model. To obtain a point-cloud representation of the robot, we simply sample 3D points from the vertices of the 3D meshes of the links. Figure shows two examples of a Fetch mobile manipulator and a Franka Panda arm with their 3D points sampled, respectively. The number of points for each link is a parameter to set. Using more points requires more computation in goal reaching and obstacle avoidance, but it can achieve more accurate collision checking. We simply sample 100 points for each link in our experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A A Point-Cloud Representation for Robots and Task Spaces", "weight": 1.0} -->

For objects in the robot task space, we cannot obtain 3D models of them if we want the robot to work in arbitrary environments. Therefore, we rely on depth sensing to obtain a point-cloud representation of the task space. By equipping a RGB-D camera with a robot, the robot can capture a depth image of the scene. Depth pixels can be back-projected to the camera frame using the intrinsic parameters of the camera. Then we can obtain a point cloud of the scene. Given the camera extrinsic parameters, i.e., 3D rotation and 3D translation of the camera in the robot base frame, the point cloud can be transformed into the robot base frame. Figure (a) shows a tabletop scene and a Fetch robot in the PyBullet simulator, and Figure (b) illustrates the computed point cloud using a depth image captured by the robot camera. Since RGB-D cameras are commonly used in robotic applications, using 3D scene points makes our approach generalizable to various scenarios. Next, we describe how to use the point-cloud representation in our grasping trajectory optimization method.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Point Cloud-based Cost Function for Goal Reaching", "weight": 1.0} -->

In grasping trajectory optimization, we need to generate a trajectory for a robot from its current joint configuration to a goal configuration for grasping a target object. The task-space goal is defined as an end-effector configuration to grasp the target object. For two-finger grippers, a goal can be simplified to be a homogeneous transformation $\mathbf{T}_{g} = {(\mathbf{R}_{g},\mathbf{t}_{g})} \in {{\mathbb{S}}{\mathbb{E}}{}}$, where $\mathbf{R}_{g}$ and $\mathbf{t}_{g}$ are the 3D rotation and the 3D translation of the gripper link with respect to the robot base frame, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Point Cloud-based Cost Function for Goal Reaching", "weight": 1.0} -->

In our method, we optimize for a trajectory that is discretized into $T$ time steps. The trajectory is parameterized by $T$ joint positions $\mathcal{Q} = {(\mathbf{q}_{1},\ldots,\mathbf{q}_{T})}$, where $\mathbf{q}_{i}, \in {\mathbb{R}}^{n}$ for $i = {1,\ldots,T}$, and $n$ is the degree of freedom of the robot. The last configuration of the trajectory $\mathbf{q}_{T}$ must reach the goal $\mathbf{T}_{g}$ in the task space.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Point Cloud-based Cost Function for Goal Reaching", "weight": 1.0} -->

We can use forward kinematics to compute the end-effector pose of the robot at time step $T$: ${\mathbf{T}{(\mathbf{q}_{T})}} = {(\mathbf{R}_{T},\mathbf{t}_{T})} \in {{\mathbb{S}}{\mathbb{E}}{}}$. We wish to define a cost function $c_{\text{goal}}{({\mathbf{T}{(\mathbf{q}_{T})}},\mathbf{T}_{g})}$ to measure the distance between the gripper pose of the robot at the time step $T$ and the grasping goal. Consequently, minimizing this cost function can find a robot configuration to reach the goal.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Point Cloud-based Cost Function for Goal Reaching", "weight": 1.0} -->

Usually, the cost function is defined based on the distance between the two 3D rotations $(\mathbf{R}_{T},\mathbf{R}_{g})$ and the distance between the two 3D translations $(\mathbf{t}_{T},\mathbf{t}_{g})$. However, a weight must be adjusted to balance the two distances. Motivated by work on 6D object pose estimation, we utilize the point matching loss function as our cost function for goal reaching. Let $\mathcal{E} = {\{\mathbf{x}_{i}\}}_{i = 1}^{m}$ be a set of $m$ 3D points on the end-effector of the robot (see Figure (c)). Our cost function for goal reaching is defined as

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Point Cloud-based Cost Function for Goal Reaching", "weight": 1.0} -->

which minimizes the distance between two sets of point clouds undergone two homogeneous transformations. The advantage of using this cost function is that it eliminates the need to use a hyperparameter to balance rotation and translation. This cost function can also be generalized to grippers with high degrees of freedom, such as multi-finger grippers. Note that $\mathbf{T}{(\mathbf{q}_{T})}$ is a function of $\mathbf{q}_{T}$ in the loss function according to forward kinematics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Point Cloud-based Cost Function for Collision Avoidance", "weight": 1.0} -->

In addition to reaching the grasping goal, another requirement in robotic grasping is to avoid obstacles in the task space. We hope that the robot will not hit any object before grasping the target. For the example in Figure, the robot should avoid hitting the table and objects on the table during grasping. Instead of using 3D meshes or 3D shape primitives to represent obstacles, our method only has access to a point cloud of the scene. Therefore, we propose to compute a Signed Distance Field (SDF) of the robot task space using the point cloud for collision avoidance.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Point Cloud-based Cost Function for Collision Avoidance", "weight": 1.0} -->

First, the extent of the task space is determined by the extent of the point cloud in the task space, where we add some margin to the point cloud space. Second, the SDF is constructed by densely sampling a 3D grid within the extent of the task space. The resolution of the grid is a parameter that can be tuned as a trade-off between computational efficiency and accuracy of collision checking. Third, we compute the signed distance value for each vertex of the 3D grid, which is approximated by the distance between the vertex and the closest point in the point cloud of the scene. The sign of the distance is determined by checking if the vertex is behind the point cloud or not. Specifically, we project the vertex to the depth image using the camera parameters and compare the depth values of the vertex and the projected pixel to obtain the distance sign. Figure (d) illustrates the SDF of the task space, where the cyan vertices have negative distances. Finally, using the computed SDF, we can check the collision between the robot and the scene by checking the signed distance values of the 3D points on the surface of the robot in the task space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Point Cloud-based Cost Function for Collision Avoidance", "weight": 1.0} -->

In addition, we can define a cost function for collision avoidance using the SDF. For each joint configuration in the robot trajectory ${\mathbf{q}_{t} \in {\mathbb{R}}^{n}},{t = {1,\ldots,T}}$, let ${\mathbf{x}{(\mathbf{q}_{t})}} \in {\mathbb{R}}^{3}$ be a surface point on the robot transformed into the task space according to the joint configuration $\mathbf{q}_{t}$ using forward kinematics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Point Cloud-based Cost Function for Collision Avoidance", "weight": 1.0} -->

where $\varepsilon$ is a margin parameter and $d{(\mathbf{x})}$ is the signed distance of the 3D point. When the signed distance $d{(\mathbf{x})}$ is greater than $\varepsilon$, there is no cost in collision. Note that in our implementation, the SDF is precomputed using a 3D grid to speed up computation. Therefore, we simply find the voxel in which the 3D point $\mathbf{x}$ falls and use the signed distance value of the voxel as $d{(\mathbf{x})}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

With the designed cost functions for goal reaching and collision avoidance, we describe our trajectory optimization framework for joint motion and grasp planning. The task of a robot is to grasp a target object in a cluttered scene. We assume that there exists a grasp planner that can be used to synthesize grasps of the target. For example, in model-based grasping, GraspIt! can be used to synthesize grasps given the 3D model of the target object. In model-free grasping, learning-based approaches such as 6DGraspNet or Contact-GraspNet can be used to synthesize grasps of the target object given the segmented point cloud of the target. We denote the set of synthesized grasps as a goal set $\mathcal{G} = {\{\mathbf{T}_{i}\}}_{i = 1}^{K}$, where $\mathbf{T}_{i} \in {{\mathbb{S}}{\mathbb{E}}{}}$ is a homogeneous transformation of the robot gripper and $K$ is the number of planned grasps.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

Our goal is to find a collision-free trajectory for the robot to reach one of the grasps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

Intuitively, we want to have the last joint position $\mathbf{q}_{T}$ reach one of the grasps in the goal set $\mathcal{G}$. Meanwhile, the trajectory should be collision-free and subject to constraints of the robot dynamics and joint limits.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

where we minimize an objective function of $\mathcal{Q}$ and $\overset{˙}{\mathcal{Q}}$ subject to a set of constraints. Note that the objective function computes the minimum cost among all the grasping goals in the goal set $\mathcal{G}$. Consequently, solving the optimization problem will select the best goal from the goal set.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

First, the term $c_{\text{goal}}{({\mathbf{T}{(\mathbf{q}_{T})}},\mathbf{T}_{i})}$ is the goal reaching cost described in Eq. for the $i$th goal $\mathbf{T}_{i}$ in the goal set, where forward kinematics is used to compute the gripper pose given the robot configuration at the last time step $\mathbf{q}_{T}$. Second, in addition to reaching the goal in the last step, we introduce a cost term $c_{\text{standoff}}{({\mathbf{T}{(\mathbf{q}_{T - \delta})}},{\mathbf{T}_{i}\mathbf{T}_{\Delta}})}$ to ensure that the robot reaches a standoff pose for grasping before the goal.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

The standoff pose $\mathbf{T}_{i}\mathbf{T}_{\Delta}$ is computed by a displacement $\mathbf{T}_{\Delta} \in {{\mathbb{S}}{\mathbb{E}}{}}$ of the grasping pose $\mathbf{T}_{i}$ along the forward axis of the gripper as illustrated in Figure. The main reason of introducing the standoff pose is because optimizing the trajectory directly to reach the grasping pose may result in a collision between the robot and the target object. In these cases, the robot will knock down the target object and cannot grasp it. Adding the standoff pose in the trajectory optimization makes the problem simpler. In our objective function, we require that the robot gripper pose $\mathbf{T}{(\mathbf{q}_{T - \delta})}$ at time step $T - \delta$ to reach the standoff pose, where $\delta$ is a parameter to set.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

Finally, the objective function contains a cost term for collision avoidance and a cost term to penalize large velocities, where $\lambda_{1}$ and $\lambda_{2}$ are two weights to balance the costs. The collision cost for the time step $t$ is defined as

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

where ${\mathbf{x}_{i}{(\mathbf{q}_{t})}} \in {\mathbb{R}}^{3}$ is a 3D point on the robot at the robot configuration $\mathbf{q}_{t}$ and $M$ is the total number of points on the robot. The collision cost is computed according to Eq. using our SDF representation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Constrained Trajectory Optimization for Joint Motion and Grasp Planning", "weight": 1.0} -->

Next, we describe the constraints in the optimization problem. 1) $\mathbf{q}_{1} = \mathbf{q}_{0}$, where $\mathbf{q}_{0}$ denotes the current configuration of the robot. This constraint ensures that the trajectory starts from the current configuration of the robot. 2) ${{\overset{˙}{\mathbf{q}}}_{1} = \mathbf{0}},{{\overset{˙}{\mathbf{q}}}_{T} = \mathbf{0}}$ ensure that the starting velocity and the ending velocity of the robot are zero. 3) $\mathbf{q}_{t + 1} = {\mathbf{q}_{t} + {{\overset{˙}{\mathbf{q}}}_{t}dt}}$ ensures that the robot state follows the kinematics of the robot, where $dt$ is the time interval between two time steps. 4) The last two constraints in Eqs.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-E Initialization for Grasping Trajectory Optimization", "weight": 1.0} -->

The optimization problem in Eq. is a large-scale constrained nonlinear programming problem. For example, a Franka panda arm has $n = 7$ DOFs. If we set the number of time steps of the trajectory $T = 50$, the optimization problem has ${7 \times 2 \times 50} = 700$ variables. We utilize the Interior Point OPTimizer (Ipopt) interfaced with the CasADi framework to solve it. Ipopt can only find local solutions that are sensitive to the initialization of the variables. To obtain a good local solution and speed up the optimization, we use the following strategy to initiate the optimization. 1) Given a set of grasping poses $\mathcal{G} = {\{\mathbf{T}_{i}\}}_{i = 1}^{K}$ of a target, we first filter out grasps that are in-collision with other objects in the scene.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-E Initialization for Grasping Trajectory Optimization", "weight": 1.0} -->

This collision checking can be achieved by checking the signed distance values of the 3D points on the robot gripper of a given pose as described in Section III-C. 2) For the remaining grasps, we check if an inverse kinematics (IK) solution exists.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Initialization for Grasping Trajectory Optimization", "weight": 1.0} -->

where we use $\mathbf{q}_{T}$ to denote the variable in IK, and the objective function is the point matching cost function defined in Eq.. After finding a local solution $\mathbf{q}_{T}^{\ast}$, we compute the pose error between $\mathbf{T}{(\mathbf{q}_{T}^{\ast})}$ and the goal $\mathbf{T}_{g}$ using a rotation error and a translation error. If both errors are smaller than some pre-defined thresholds, we claim that an IK solution is found. Otherwise, there is no IK solution for $\mathbf{T}_{g}$. In this way, we can filter out grasps without IK solutions. 3) For each remaining grasp with an IK solution, we interpolate a trajectory of the robot from the current configuration of the robot to the IK configuration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Initialization for Grasping Trajectory Optimization", "weight": 1.0} -->

We then compute the collision cost of the trajectory $\sum_{t = 1}^{T}{c_{\text{collision}}{(\mathbf{q}_{t})}}$ to rank these trajectories. 4) Finally, we initialize the optimization with the trajectory that has the minimum collision cost. In the case of tie-breaking, e.g., multiple non-collision trajectories, we use the trajectory whose last configuration is closer to the current configuration of the robot. We empirically found that the above initialization process can speed up the convergence of the optimization to find a good local solution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conducted experiments on 6DoF robotic grasping to evaluate our method in both simulation and in the real world. Two types of scenes are used for evaluation: a tabletop scene and a shelf scene as illustrated in Figure in the Pybullet simulator. In these scenes, 16 YCB objects are used for grasping. The objects in the tabletop scenes are arranged according to the SceneReplica benchmark, and we sample object locations for the shelf scenes with 6 objects in each scene. Two robots, i.e., a Fetch mobile manipulator and a Franka Panda arm, are used for evaluation. The main evaluation metric is the success rate of grasping. If an object is successfully lifted by the robot, we count it as a success. In addition, we evaluate collisions during grasping.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Implementation Details", "weight": 1.0} -->

First, grasps of the 16 YCB objects are generated using GraspIt!, with 100 grasps for each object. Therefore, the size of the goal set is 100. Second, the trajectory optimization is implemented based on the OpTaS library, which provides an interface to Ipopt solver using the CasADi framework. Third, the hyper-parameters in the method are set as follows. For each robot link, we sample 100 surface points. The margin $\varepsilon = 0.02$ in computing the collision cost (Eq. ). The grid resolution of the signed distance field is 5cm. In the optimization problem Eq., $\lambda_{1} = 10$, $\lambda_{2} = 0.01$ and $\delta = 10$. The standoff pose for grasping is set as 10cm and 20cm from the grasping pose for the tabletop scenes and the shelf scenes, respectively. The number of time steps is $T = 50$, and the time span of a trajectory is set to 10 seconds. Therefore, ${dt} = 0.2$ in Eq..

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Implementation Details", "weight": 1.0} -->

Tabletop (success ↑ / collision ↓)
Shelf (success ↑ / collision ↓)

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Implementation Details", "weight": 1.0} -->

Tabletop (success ↑ / collision ↓)
Shelf (success ↑ / collision ↓)

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B The Effect of Point Matching for Goal Reaching", "weight": 1.0} -->

We evaluated the effectiveness of our point cloud-based representation for goal reaching. We solve the inverse kinematics optimization problem in Eq. with three different cost functions and compare their performance. The first one is the point-matching cost function in Eq. to measure the difference between two transformations $\mathbf{T}_{T}$ and $\mathbf{T}_{g}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B The Effect of Point Matching for Goal Reaching", "weight": 1.0} -->

where the distance between two quaternions measures the angular distance between the two rotations.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B The Effect of Point Matching for Goal Reaching", "weight": 1.0} -->

Using the three cost functions, we solve IK for each grasp of each object in the tabletop scenes and the shelf scenes. Table I presents the statistics of this experiment, where we count the number of successful IK solutions among all the trials. We consider an IK solution to be found after optimization if the translation error is less than 1 cm and the rotation error is less than 5 degrees. From the table, we can see that using the point matching cost function finds the maximum number of IK solutions, which validates the effectiveness our point-cloud based representation. Using distances between Euler angles is not a good choice due to the discontinuity between $- \pi$ and $\pi$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

The results of our grasping experiments in PyBullet are presented in Table II, where we compare our approach to the OMG-Planner. The OMG-Planner is a trajectory optimization method based on first-order gradient descent for joint motion and grasp planning. It alternates between goal selection and fixed-goal trajectory optimization. Grasps of the 16 YCB objects are generated using GraspIt!. In the simulation, we query the object poses directly and then transform the grasps according to the object poses. We evaluate the number of successful grasps and the number of collisions during grasping. Using our point-cloud representation, we treat a grasping trajectory as in collision if there are 5 surface points of the robot with negative signed distances.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Simulation Results", "weight": 1.0} -->

For the table, we can see that 1) our method improves over the OMG-Planner in both the tabletop scenes and the shelf scenes. Our method achieves higher grasping success rates and lower collision rates. The main advantage of our method is that we solve a constrained nonlinear optimization problem with an advanced solver (Ipopt) compared to a gradient descent-based optimization. In addition, our point-cloud representation enables more accurate goal reaching and collision avoidance. 2) The Fetch robot achieves higher success rates compared to the Panda robot, largely due to its greater reachability and wider gripper. We cannot run the OMG-Planner for the Fetch robot since its implementation is tightly coupled with the Panda robot. In contrast, our implementation can be easily applied to different robots, where it only requires an URDF of a robot as input. 3) Some objects are more difficult to grasp. These are small or flat objects such as the tuna fish can, the scissors, the large marker, and the extra large clamp. Nonprehensile grasping strategies might be needed to grasp these objects successfully, which can be explored in future work.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Model-free Grasping in the Real World", "weight": 1.0} -->

Lastly, we conduct grasping experiments in the real world to evaluate our trajectory optimization method. We consider the task of model-free grasping, where we do not have 3D models of objects for perception and motion planning. Model-free grasping is applicable to diverse environments, and our approach does not rely on 3D object models. Figure illustrates the perception, planning, and control pipeline for model-free grasping.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Model-free Grasping in the Real World", "weight": 1.0} -->

We utilized the MSMFormer to segment unseen objects in an input RGB-D image for tabletop scenes. For shelf scenes, we found that MSMFormer cannot successfully segment objects in the shelf since it is not trained with similar scenes. Therefore, we used Grounding DINO with text prompt "objects" to detect generic objects, and then used SAM to segment objects inside the bounding boxes from Grounding DINO. To synthesize grasps for a target object, we used Contact-GraspNet, which takes a segmented point cloud of an object as input and generates grasping poses of a parallel jaw gripper. These planned grasps are treated as goals in the goal set for joint motion and grasp planning. To execute a planned trajectory on a real robot, we also need to generate accelerations of the robot joints on the trajectory. Since our method does not solve for joint accelerations, we apply the path parameterization method to reparameterize the planned trajectory.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Model-free Grasping in the Real World", "weight": 1.0} -->

We compare our method with an OMPL -based planning baseline in the SceneReplica benchmark. This baseline algorithm simply loops over all goals in the goal set and checks if there is a collision-free motion plan to reach a goal. The comparison results are presented in Table III. Our method achieves a better grasping success rate and a better pick-and-place success rate. Detailed evaluation statistics for each YCB object are presented in Table IV, where we classify pick-and-place failures into perception failures, planning failures, and execution failures. A detailed description of these failure types can be found. Most failures are due to errors in object segmentation, grasp planning, and grasping goal selection. Because stable grasp is critical for pick-and-place success. By solving the trajectory optimization problem, our method benefits from better goal selection compared to the baseline algorithm. Figure shows some examples of successful grasping in the real world. Grasping videos can be found on the project page and in the supplementary material.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-E Planning Time", "weight": 1.0} -->

Our approach has demonstrated a significant improvement in planning efficiency over the OMPL-based baseline in the experiments conducted using the SceneReplica Benchmark. On average, our method achieves a planning time of 15.4 seconds, which includes the computation time for the grasp collision checking, the IK checking, and the trajectory optimization. However, the OMPL-based baseline takes 45.6 seconds to find a grasp trajectory for a target object. In contrast, the OMG-Planner achieves 3.2 seconds planning time by solving parallel IKs and using GPUs for acceleration. We consider speeding up our method for future work.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

We introduce a new trajectory optimization method for joint motion and grasp planning. The core component of our method is a point cloud-based representation for robots and task spaces. This representation is generalizable to different robots and different environments. We formulate goal reaching and collision avoidance in the trajectory optimization using the point-cloud representation. By solving a constrained nonlinear optimization problem using the Ipopt solver, our method can generate robot trajectories for grasping. Experiments are conducted in simulation and in the real world to demonstrate the effectiveness of our method.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

One limitation of our method is that trajectory optimization is slow when relying on an external solver. Future work includes speeding up the optimization. One direction is to explore using GPUs for parallel computing. Another direction is to explore model predictive control with our point-cloud representation for robotic grasping. To further improve the grasp success rate, a grasp planner that considers force closure or grasp stability will be helpful.
