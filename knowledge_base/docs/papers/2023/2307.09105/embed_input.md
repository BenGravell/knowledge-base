<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations

Topics include Model predictive path integral control, Motion planning, Trajectory optimization, Graphics processing unit, Parallelized, Isaac, Gym, IsaacGym, Robotics, Simulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses IsaacGym as a simulator for forward dynamics propagation within an MPPI framework.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a method for sampling-based model predictive control that makes use of a generic physics simulator as the dynamical model. In particular, we propose a Model Predictive Path Integral controller (MPPI), that uses the GPU-parallelizable IsaacGym simulator to compute the forward dynamics of a problem. By doing so, we eliminate the need for explicit encoding of robot dynamics and contacts with objects for MPPI. Since no explicit dynamic modeling is required, our method is easily extendable to different objects and robots and allows one to solve complex navigation and contact-rich tasks. We demonstrate the effectiveness of this method in several simulated and real-world settings, among which mobile navigation with collision avoidance, non-prehensile manipulation, and whole-body control for high-dimensional configuration spaces. This method is a powerful and accessible open-source tool to solve a large variety of contact-rich motion planning tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As robots become increasingly integrated into our daily lives, their ability to navigate and interact with the environment is becoming more important than ever. From collision avoidance to moving obstacles out of the way to pick up some objects, robots must be able to plan their motions while accounting for contact with their surroundings. At the same time, robotic platforms require many Degrees Of Freedom (DOF) to achieve agile and dexterous movements. All this poses many challenging problems to motion planners, such as collision-free navigation in complex and dynamic environments, high DOF mobile manipulation, contact-rich tasks such as picking and pushing, and in-hand manipulation. Solutions to these challenges exist but are often specialized and not easily transferable to different scenarios. Learning-based approaches, for example, can leverage physics simulators to train policies for complex tasks but require extensive training and resources. For instance, took years to develop, utilizing 6144 CPU cores and 50 hours of training to learn a policy for in-hand cube manipulation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, model-based approaches like Model Predictive Control (MPC) can solve challenging tasks. However, MPC often relies on constrained optimization, requiring constraint simplifications, precise modeling, and ad-hoc solutions to handle discontinuous dynamics in contact-rich tasks. While utilizing motion memory for warm-starting optimization can enhance performance, the above limitations still persist. Recently, Model Predictive Path Integral (MPPI) control and its information-theoretic counterpart addressed optimal control problems via importance sampling, mitigating challenges tied to constrained optimization algorithms dealing with non-convex constraints and discontinuous dynamics. However, substantial modeling remains necessary.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a training-free model-based framework for real-time control of complex systems, where one designs only a cost function, not the problem's dynamics and contact models. We introduce the idea of using a general GPU-parallelizable physics simulator, IsaacGym, as the dynamic model for MPPI. This creates a robust framework that generalizes to various tasks. An overview is given in Fig. 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

This section provides an overview of selected works focusing on motion planning and contact-rich tasks in robotics. Motion planning pipelines are categorized as global and local motion planning. Local motion planning encompasses approaches like operational space control, geometric methods such as Riemannian Motion Policies and Optimization Fabrics, and receding-horizon optimization formulations like Model Predictive Control (MPC) that may incorporate learned components. Most MPC algorithms rely on constrained optimization and assume smooth dynamics. However, contact-rich tasks pose challenges due to their non-smooth and hybrid nature, involving sticking and sliding frictions or entering contacts, requiring extensive modeling and ad-hoc solutions for pushing tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

In contrast, Model Predictive Path Integral (MPPI) control is a sampling-based MPC approach that approximates optimal control via parallel sampling of input sequences. MPPI is gradient-free and well-suited for systems with non-linear, non-convex, discontinuous dynamics and cost functions. It has successfully controlled high-degree-of-freedom manipulators in real-time, incorporating self-collision avoidance using trained neural networks and collision-checking functions. However, these approaches have limited interaction with the environment. In, the authors propose ensemble MPPI, a variation that handles complex tasks and adapts to parameter uncertainty. Still, the task modeling remains unclear, and no open-source implementation is available.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

To alleviate the problem of explicit modeling, some works have addressed the use of physics simulators for sampling-based MPC. In, the authors use the RaiSim simulator to sample waypoints for foot placement of a quadruped. Moreover, Howell et al. proposed a sampling-based MPC method that employs MuJoCo as a dynamic model for rolling out sampled input sequences. This offloads modeling efforts to the physics engine, simplifying controller design. However, MuJoCo's parallelization capabilities are constrained by the number of CPU threads, limiting real-time performance when many samples are required to solve a task. Moreover, results are presented only in simulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

A high number of samples is particularly crucial in tasks such as non-prehensile manipulation with robot manipulators. Traditional approaches often involve sampling end-effector trajectories on a plane, relying on additional controllers for robot actuation and learned models for predictions. For instance, Arruda et al. use a forward-learned model trained on 326 real robot pushes. This model is employed by an MPPI controller to plan push manipulations as end-effector trajectories. Cong et al. train a Long Short-Term Memory-based model to capture push dynamics using a dataset of 300 randomized objects. End-effector trajectories are sampled within a rectangular 2D workspace. Both methods require a separate controller to convert cartesian motions into joint commands, and both perform push manipulation through a sequence of pushes, resulting in discontinuous motion. These methods are not easily transferable to other robots, particularly non-holonomic mobile pushing.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

This paper presents a novel open-source implementation of Model Predictive Path Integral (MPPI) control with a generic physics simulator as the dynamical model. This enables the method to solve many contact-rich motion planning problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The integration of the MPPI controller with the GPU-parallelizable simulator IsaacGym, distinguishing our approach from prior works in MPPI. Our method facilitates collision checking and contact-rich manipulation tasks leveraging the contact models and rigid body interactions included in the simulator without requiring gradients. Our solution allows smooth real-time control of real-world systems with high degrees of freedom, efficiently computing hundreds of rollouts in parallel.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

A versatile method applicable to various motion planning challenges, including collision avoidance, prehensile and non-prehensile manipulation, and whole-body control with diverse robots. We provide an open-source implementation that can be readily reused and extended to heterogeneous robots and tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We perform many contact-rich tasks with several robotic platforms and real-world experiments. We include omnidirectional and differential drive robots and fixed or mobile manipulators and compare against many specialized baselines.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sampling-based MPC via parallelizable physics simulations", "weight": 1.0} -->

In this section we describe the integration of MPPI with IsaacGym, which enables real-time control of complex contact-rich robotic systems with minimal modeling.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Background theory on MPPI", "weight": 1.0} -->

In this section, we give an overview of the background theory of MPPI. For more theoretical insights, please refer to the original publications. MPPI is a method to solve stochastic optimal control problems for discrete-time dynamical systems such as

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Background theory on MPPI", "weight": 1.0} -->

where the nonlinear state-transition function $f$ describes how the state $x$ evolves over time $t$ with a control input $v_{t}$. MPPI samples $K$ noisy input sequences $V_{k}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Background theory on MPPI", "weight": 1.0} -->

Given the state trajectories $Q_{k}$ and a designed cost function $C$ to be minimized, the total state-cost $S_{k}$ of an input sequence $V_{k}$ is computed by functional composition $S_{k} = {C{(Q_{k})}}$. Then, each rollout is weighted by importance sampling weights $w_{k}$, computed via an inverse exponential of $S_{k}$ with tuning parameter $\beta$, normalized by $\eta$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Background theory on MPPI", "weight": 1.0} -->

The parameter $\beta$ is also known as inverse temperature.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Background theory on MPPI", "weight": 1.0} -->

and demonstrate the approach taken to approximate the optimal control. represents a weighted average of sampled control inputs, while assigns exponentially higher weights to less costly inputs. The first input $u_{0}^{\ast}$ of the sequence $U^{\ast}$ is applied to the system. Then the process is repeated.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Proposed algorithm", "weight": 1.0} -->

We now describe how we use MPPI with IsaacGym, summarized in Algorithm 1. We initialize an input sequence $U_{init}$ as a vector of zeroes with a length of $T$, where $T$ is the time horizon in steps. We then sample $K$ sequences of additive input noise $\mathcal{E}_{k}$ for exploring the input space around $U_{init}$. The key concept is that, instead of explicitly defining a nonlinear transition function $f$, we use IsaacGym to compute the next state $x_{t + 1}$ given $x_{t}$ and control input $v_{t}$. This is done by reading the current state of the environment, resetting the state of the simulator to the observed values, and then applying the noisy control input sequence to simulate the state trajectories in IsaacGym. Note that these $K$ state trajectories can be computed independently of each other. We use this property to forward and simulate all the rollouts in parallel, leveraging the parallelization capabilities of IsaacGym.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Proposed algorithm", "weight": 1.0} -->

Instead of sampling from a Gaussian distribution, we follow the strategy of a recent paper that proposes to sample Halton Splines instead for better exploration and smoother trajectories. Similar to, we fit B-Splines to inputs sampled from a Halton sequence using standard Python modules and then we evaluate the spline at regular intervals to retrieve $\mathcal{E}_{k}$. Unlike, we do not update the variance of the sampling distribution. Instead, we keep it as a tuning parameter, constant during execution. Updating the variance as can lead to better convergence to a goal, but it also leads to stagnation of the control over time, which is harmful in the contact-rich tasks considered in this paper. Once the task begins, we reset our $K$ simulation environments on IsaacGym to the current observed world state $x$. In parallel, we can now roll out the sampled input sequences $V_{k}$ into state trajectories $Q_{k}$ using $K$ simulation environments on IsaacGym and compute their corresponding cost $S_{k}$ using the designed cost function $C$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Proposed algorithm", "weight": 1.0} -->

Next, we can compute the importance sampling weights $w_{k}$ as. The normalization factor $\eta$ is a useful metric to monitor, as it indicates the number of samples assigned significant weights.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Proposed algorithm", "weight": 1.0} -->

Empirically, we observed in all performed tasks that setting $5 < \eta < 10$ is a good balance for smooth behavior. Finally, an approximation of the optimal control sequence $U^{\ast}$ can now be computed via a weighted average of the sampled inputs. $U_{init}$ is now updated with $U^{\ast}$, time-shifted backward of one timestep so that it can be used as a warm-start for the next iteration, $U_{init} = {\lbrack u_{1}^{\ast},\ldots,u_{T - 1}^{\ast},u_{T - 1}^{\ast}\rbrack} \in {\mathbb{R}}^{T}$. The second last input in the shifted sequence is propagated to the last input as well. From the sequence $U^{\ast}$, only the first input $u_{0}^{\ast}$ is applied to the system, and the next iteration starts.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Exploiting the physics simulator features", "weight": 1.0} -->

IsaacGym provides useful information and general models that are particularly useful for robot control in contact-rich tasks. Besides being useful to simulate the physical interaction of rigid bodies, we leverage IsaacGym for collision checking and tackling model uncertainty with domain randomization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C1 Collision checking", "weight": 1.0} -->

Collision checking in robotics can be challenging for a number of reasons, one of them being computational complexity. This is particularly true if the task requires continuous collision checking as the robot moves in dense environments with complex object shapes. To overcome this problem, approximations are often introduced with the convexification of the space. However, this requires several heuristics and can hinder robot motions in complex scenes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C1 Collision checking", "weight": 1.0} -->

Instead, we propose to tackle the problem of collision checking by using the already available contact forces tensor from IsaacGym, which is available for each simulation step.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C1 Collision checking", "weight": 1.0} -->

where $F_{obst}$ are the contact forces exerted on the different obstacles. This allows us to perform continuous collision checking at each time step over the horizon $T$, with arbitrary complex shapes. By heavily penalizing contacts with obstacles, the robot will avoid collisions. On the other hand, by relaxing the weight $\omega_{c}$ one can allow for certain contacts required for the task, such as rolling a ball against a wall (Section III-C2).

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C2 Tackling model uncertainty", "weight": 1.0} -->

IsaacGym is designed to easily support domain randomization. We use this feature to randomize the object properties in each environment in case of contact-rich tasks, such that uncertainty is incorporated in every rollout for the MPPI. Effectively, this allows to account for uncertainty in environment perception. Specifically, starting from nominal physics properties, in every rollout objects are spawned with uncertainty on mass and friction nominal values, sampled from a uniform distribution. Additionally, the object size is also randomized with additive Gaussian noise, see Section III for experiment-specific details. Therefore, every simulation is different from the others, and all simulations are different from the world such that we can account for model mismatch. In a sense, we perform a sort of domain randomization in real-time to address the challenge of model uncertainty and imperfect perception.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

We perform several experiments in three different categories: 1) motion planning and collision avoidance, 2) whole-body control of high DOF systems in contact-rich settings, and 3) non-prehensile manipulation. Experiments and simulations are conducted on an Alienware Laptop with Nvidia 3070 Ti graphics card. The software implementation consists of our open-source Python package that can easily be installed, tested, and extended to new robots and tasks. In real-world tests, we used a Robot Operating System (ROS) wrapper to connect the robot to the planner and a motion capture system to determine the pose of manipulated objects. Our implementation allows for position, velocity, and torque control. In this paper, all robots are velocity-controlled except for the mobile manipulator in Section III-B, which is torque-controlled.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Motion planning and collision avoidance", "weight": 1.0} -->

We compare the performance of the proposed method in a pure local motion planning setting, i.e. no interaction with the environment. This aims to showcase the fact that our method is comparable to state-of-the-art techniques when no contact is involved. The main focus is the quantitative analysis of the method compared to two baselines, specifically optimization fabrics as presented in and a simple MPC formulation solved with ForcesPro. We make use of an already available benchmark setup, the localPlannerBench. We present results for two cases, namely a holonomic robot, and a robotic arm (Franka Emika Panda). For all experiments, we randomize five obstacles and the goal positions in $N = 100$ runs, see Fig. 2 for some examples. Solutions by the three methods are assessed using four metrics, e.g. time to reach the goal, path length, solver time, and minimum clearance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Motion planning and collision avoidance", "weight": 1.0} -->

The compared methods show minimal differences in path length clearance for both examples (Fig. 3). However, our method consistently reaches the goal faster. This is attributed to the perfect representation of the robot's collision shapes used in our method, compared to the enclosing spheres in the ForcesPro MPC and optimization fabrics. It should be noted that our approach incurs higher computational times (Table I) due to the physics simulations performed by IsaacGym. Despite this, our method remains competitive in motion planning applications and offers significant advantages in contact-rich tasks, as demonstrated in the following sections.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Prehensile manipulation with whole-body control", "weight": 1.0} -->

Our approach scales well with the complexity of the robot. In Fig. 5, the task is to relocate an object from a table to an $\lbrack x,y,z\rbrack$ location using a mobile manipulator with 12 DOF.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Prehensile manipulation with whole-body control", "weight": 1.0} -->

Although this is arguably a complex task for a robot, which usually requires manual engineering of a sequence of movements, such as navigation to a specific base goal, and pre-post grasps, the solution is rather simple with our method.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Prehensile manipulation with whole-body control", "weight": 1.0} -->

where we consider the Euclidean distance of the end-effector to the object and the object to the goal: $C_{dist} = {{\omega_{t}{\|{p_{EE} - p_{O}}\|}} + {\omega_{O_{p}}{\|{p_{G} - p_{O}}\|}}}$. We give an incentive to keep the robot in a comfortable pose by penalizing deviations from a desired arm and gripper pose, end-effector orientation, as well as imposing a minimum end-effector height $C_{pose} = {C_{Parm} + C_{Pgrip} + C_{Oee} + C_{Hee}}$. We minimize collisions penalizing the forces on the table $C_{coll}$. Lastly, we penalize high arm and base velocities $C_{vel} = {C_{Varm} + C_{Vbase}}$ since, in this experiment, we torque-control the robot.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Prehensile manipulation with whole-body control", "weight": 1.0} -->

By sampling all the DOF at once, including the base and the gripper, we achieve a fluid motion from start to end with no added heuristics for pick positions. We performed ten pick-and-deliver tasks, and the time taken was 15.67 $\pm$ 7.21s. The high standard deviation is because sometimes the cube falls, but the robot can recover by picking it up again from the floor.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Prehensile manipulation with whole-body control", "weight": 1.0} -->

For smooth whole-body motions of high DOF systems like this, many samples are required. Empirically, when the number of samples exceeds 50, a GPU pipeline is computationally cheaper than a CPU and scales better. Using IsaacGym, we can compute all the 750 samples required for mobile manipulation in parallel, computing the next control input online at $25Hz$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Non-prehensile manipulation", "weight": 1.0} -->

One advantage of using a physics simulator is that one can leverage generic physics rules for contacts, thus eliminating the need for learning or engineering specialized contact models. We demonstrate this in non-prehensile manipulation tasks involving a 7-DOF arm (Fig. 6) and two different mobile robots (Fig. 7, LABEL: LABEL: and ). In Section III-C1, we apply our method to the two pushing tasks tackled, and we compare with their final results. Additionally, in Section III-C2, we demonstrate the ease of transferring our approach to different robots, including differential-drive.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

We consider two baselines for non-prehensile pushing. In the first one, tackles the problem of pushing a relatively small object to a target pose with either $0$ (Pose 1) or $90\deg$ (Pose 2). They also consider sequences of push actions starting far from the object. In the second baseline, considers 5 relatively big objects and assumes the robot's end effector is close to the object during execution. Since we do not have access to the same hardware, and the authors of the considered baselines do not provide their models and data, we only compare against their final results. We set up our simulation to match as close as possible the tasks in the baseline using the available information from the papers. Finally, we tune our method for the two tasks separately for a fair comparison with the individual baselines. The approach utilizes an MPPI in combination with a learned model for predicting pushing effects on an object. The authors sample 2D end-effector trajectories and then rely on inverse kinematic solvers, achieving push manipulation as a sequence of disconnected pushes. In contrast, we use MPPI to sample the control input directly as joint velocities in IsaacGym.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

By doing so, we achieve smooth continuous pushes where end-effector repositioning emerges naturally, and learning is not required.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

where $p_{G}$ and $\psi_{G}$ are the goal's position and orientation, while $p_{R}$ and $p_{O}$ denote the end-effector tip and block positions, respectively. The cost function $C_{pushalign}$ promotes keeping the object between the robot and the goal.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

The cost is minimized when the end-effector is close to the block at a certain height and orientation, and the block is between the end-effector and the goal at the desired goal pose^11^1Tuning: $\omega_{t} = 1$, $\omega_{O_{p}} = 16$, $\omega_{O_{r}} = 2$, $\omega_{ee_{h}} = 8$, $\omega_{ee_{r}} = 0.5$, $\omega_{a} = 0.8$, ${dt} = 0.04$, $T = 8$, $K = 500$..

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

We perform the same task as and compare the final results of pushing a squared object on a table surface to two poses (Pose 1 and 2) with a robot arm equipped with a stick. In Table II, we report our findings, with our method showing double the accuracy. Our approach performs continuous pushes, unlike the baseline that stops for replanning after each short push. Thus, we complete either task in approximately 8 seconds, while the baseline takes approximately 4 minutes. We used the same evaluation metric of for the final cost that is a weighted average of position and orientation errors: ${1.5{({{|{p_{G_{x}} - p_{O_{x}}}|} + {|{p_{G_{y}} - p_{O_{y}}}|}})}} + {0.01{|{\psi_{O} - \psi_{G}}|}}$. For every run, the object is also randomized in the same way as the rollouts. See the accompanying video for the actual behavior.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

We further compare our approach in terms of the success rate of non-prehensile manipulation. Particularly, we consider the same task settings, pushing 5 different objects to 3 different goal poses. To do so we simply change the objects in the simulation and slightly re-tune the MPPI^22^2Tuning: $\omega_{t} = 5$, $\omega_{O_{p}} = 25$, $\omega_{O_{r}} = 21$, $\omega_{ee_{h}} = 30$, $\omega_{ee_{r}} = 0.3$, $\omega_{a} = 45$, ${dt} = 0.04$, $T = 8$, $K = 500$..

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

Since the trained models are not provided, we only compare the final results, reported in Table III. Again, thanks to the continuous pushes, our method takes about 3 seconds per task, while the baseline needs about 24 seconds. We performed 10 pushes per object, totaling 150 pushes. For the non-prehensile manipulation task with the robot arm, the mass and friction of manipulated objects have 30% uncertainty, and table friction has 90% uncertainty on the nominal value, sampled uniformly. Size is randomized with zero-mean additive Gaussian noise with a 2 mm standard deviation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C1 Comparison with baselines for pushing with a robot arm", "weight": 1.0} -->

Our method outperforms both baselines in terms of time to completion, accuracy, and success rate, except for one manipulated object. We achieve this without limiting the sampling to 2D end-effector trajectories, without needing learned models, and without requiring inverse kinematics solvers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C2 Extension to different robots", "weight": 1.0} -->

Our method is also easily extensible to different robot platforms and objects because it does not require specialized models or controllers that are robot specific, as opposed to the baselines considered. We chose to use an omnidirectional base, and a differential drive robot, to push a box or a sphere to a goal from different initial configurations. To do so, we only need to change the environment and robot URDF in IsaacGym, and re-tune the cost function for pushing due to different hardware.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Omnidirectional push of a box", "weight": 1.0} -->

The first task is the non-prehensile pushing of a box with an omnidirectional base, see Fig. 7. Success is defined when the box is placed at the goal within 5cm in the $x - y$ direction and within 0.17 radians in rotation. The robot cannot touch obstacles. The cost function for the MPPI is the same as, re-tuned without considering end effector height and orientation since we now operate on a plane.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Omnidirectional push of a sphere", "weight": 1.0} -->

One can easily extend the example above to different objects with very different dynamics. We chose a sphere instead of a box, and we simply change the object spawned in the simulation. For this task, we want to put the ball in between the two walls, Fig. 8. We considered multiple runs from two different starting poses, A and B. Results are summarized in Table IV and the execution can be seen in the accompanying video.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Omnidirectional push of a sphere", "weight": 1.0} -->

(a) Pushing straight to the goal on the right.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Omnidirectional push of a sphere", "weight": 1.0} -->

(b) Pushing to the goal on the left with 90∘ rotation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Differential drive non-prehensile pushing", "weight": 1.0} -->

We perform differential drive non-prehensile pushing, see Fig. 9, with the same cost function as before but re-tuned. One can change the robot for the task by changing the URDF, neglecting all the additional contact modeling required in a classical model-based MPC. The time taken to push the box to the goal was 18.31s. In the mobile non-prehensile pushing experiments, objects to manipulate are spawned with 30% uncertainty on mass and friction sampled uniformly, while object size is randomized with Gaussian noise with a standard deviation of 5mm.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-D Real-world experiments", "weight": 1.0} -->

To demonstrate the applicability of our approach, we transfer to the real world a subset of the non-prehensile manipulation tasks previously presented in Section III-C with both the robot manipulator and the omnidirectional base. In particular, in Fig. 10, we show the results of the 7 DOF manipulator pushing a product to two different goals, similar to the simulations corresponding to Table II. As presented in Fig. 1, the samples are rolled out in $K = 500$ simulated environments in IsaacGym, which, at each timestep, are initialized to the state of the real world. Based on this, the optimal control is estimated and applied to the real system.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-D Real-world experiments", "weight": 1.0} -->

When transferring to the real world, compared to the experiments in Section III-C1, only the cost function weights were re-tuned. The horizon, control frequency, number of samples, structure of the cost function, and randomization of the sampled environments remained unchanged.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-D Real-world experiments", "weight": 1.0} -->

From the experimental evaluation on the real robot, we observe that the time to complete the pushing tasks and the final position errors are comparable to the results in the simulation from Table II. Importantly, these results are achieved without making assumptions on specific contact points. Thus, the robot can naturally re-position itself and change contact location autonomously. Additionally, our method allows us to sample joint velocities directly; thus, we do not restrict the sampling to 2D end-effector trajectories to be translated into joint commands, as often seen in other approaches.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-D Real-world experiments", "weight": 1.0} -->

Lastly, to demonstrate robustness, we disturb the execution of pushing tasks by hand with the manipulator and the omnidirectional base (Fig. 11). Since we do not assume the robot to be behind the object to be pushed for successful execution, and since the planning and execution happen in real-time at $25Hz$, we can largely perturb the task and let the robot compensate.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we discuss key aspects and potential future work related to our solution. First, the computational demands of planning and control with our method can be high when extending the time horizon to several seconds. To keep the time horizon limited for real-time control while preventing being trapped in local minima, future work should incorporate global planning techniques such as A\*, RRT, and Probabilistic Roadmaps (PRM) to guide the local planner. Similarly to warm starting predictive controllers, one could make use of motion libraries of previous executions or learned policies along with random rollouts, to improve the sampling efficiency and exploration. Second, in real-world scenarios, uncertainties and discrepancies between simulated and actual environments could present challenges for achieving precise movements and manipulation. We utilized randomization of object properties in the rollouts to address some uncertainties. However, online system identification to converge to the true model parameters is not performed. Enhancing the robustness of the MPPI algorithm itself by reducing model uncertainty, as demonstrated, could further improve performance. Third, tuning control algorithms for optimal performance is time-consuming. Implementing autotuning techniques can automate the process and reduce manual effort.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, incorporating additional sensor support, such as lidars and signed distance fields, could be beneficial.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented a way to perform Model Predictive Path Integral controller (MPPI) that uses a physics simulator as the dynamic model. By leveraging the GPU-parallelizable IsaacGym simulator for parallel sampling of forward trajectories, we have eliminated the need for explicit encoding of robot dynamics, contacts, and rigid-body interactions for MPPI. This makes our method easily adaptable to different objects and robots for a wide range of contact-rich motion-planning tasks. Through a series of simulations and real-world experiments, we have demonstrated the effectiveness of this approach in various scenarios, including motion planning with collision avoidance, non-prehensile manipulation, and whole-body control. We showed how our method can compete with state-of-the-art motion planners in case of no interactions, and how it outperforms by a margin other approaches for contact-rich tasks. In addition, we provided an open-source implementation that can be used to reproduce the presented results, and that can be adapted to new tasks and robots.
