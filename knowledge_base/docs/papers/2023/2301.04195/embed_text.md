## Introduction

PhysX 4/FleX/Obi ThreeDWorld supports simulation of rigid bodies and deformable bodies based on whether PhysX 4 or FleX/Obi is enabled respectively. Thus, it is limited in simulating interactions between rigid and deformable bodies. ManiSkill2 supports a Warp-based Material Point Method (MPM) solver that helps simulate cutting and plastic deformations of soft objects. Currently, this feature is under development for Orbit.

TABLE I: Comparison between different simulation frameworks and Orbit. The check ( ✓) and cross ( X) denote presence or absence of the feature. In Robotic Platforms column, M stands for manipulator. In Scene Authoring column, G stands for game-based designing, M for mesh-scan scenes, and P for procedural-generation.

An ideal robot simulator needs to provide fast and accurate physics, high-fidelity sensor simulation, diverse asset handling, and easy-to-use interfaces for integrating new tasks and environments. However, existing platforms often need to make a trade-off between these aspects. For instance, simulators designed mainly for vision, such as Habitat or ManipulaTHOR, offer decent rendering throughput but simplify low-level interaction intricacies such as grasping. On the other hand, physics simulators for robotics, such as Isaac Gym or SAPIEN, provide fast and reasonably accurate rigid-body contact dynamics but do not include physically-based rendering (PBR), deformable objects simulation or ROS support out-of-the-box. Recently, Nvidia released a new simulator Omniverse Isaac Sim that aims to fulfill these gaps through GPU-accelerated real-time PBR and state-of-the-art physics engine.

This work presents Orbit, an open-source framework for robotics research that exploits the latest simulation capabilities through Isaac Sim to allow intuitive designing of tasks with photo-realistic scenes and state-of-the-art rigid and deformable body simulation. To prevent a scattering of efforts for building the necessary tooling to use the simulator for robot learning, we design a unified and modular framework that supports a wide variety of robotic platforms, sensors, and objects and allows designing tasks not only programmatically but also interactively through the GUI. We design the system bottom-up -- from incorporating user-defined models for the actuator dynamics to modularizing task specifications for learning with different levels of observations and action spaces. In Orbit, we also include a collection of features, such as different robot platforms, motion generators, and a suite of tasks that help serve not only as a benchmark but also as examples for designing a new task. Through this framework, we support various robotic applications, such as reinforcement learning (RL), learning from demonstrations (LfD), and motion planning, thereby providing a common platform for researchers in these communities to benefit from this consolidated effort.

Our main contributions are as follows: We design a unified and modular open-source framework for fast and flexible development, that leverages the latest advances in simulators for photo-realistic scenes and high-fidelity physics.

It provides a batteries-included experience for roboticists with models readily available for different robots and sensors. This helps reduce the entry barrier to using the framework and its features.

We include a suite of standardized tasks for benchmark purposes. These include eleven rigid object manipulation, thirteen deformable object manipulation, and two locomotion environments. Within each task, we allow switching robots, objects, and sensors easily.

Through experiments, we demonstrate the accuracy of the simulator for rigid and soft body simulation. Compared to existing frameworks, we show that Orbit is able to obtain up to $\sim 10$x and $\sim 3$x the throughput for rigid and deformable body manipulation tasks respectively. Additionally, we demonstrate the sim-to-real transfer of a locomotion policy for the quadruped robot, ANYmal.

In the remainder of the paper, we describe the available simulator choices (Sec. II), the framework's design decisions and abstractions (Sec. III), and its highlighted features (Sec. IV). We demonstrate the framework's applicability on different robotics workflows (Sec. V), show sim-to-real experiments for locomotion and manipulation, and evaluate the obtained accuracy and simulation throughput in Sec. V-E.

## Related Work

Recent years have seen several simulation frameworks, each specializing in particular robotic applications. In this section, we highlight the design choices crucial for building a unified simulation platform and how Orbit compares to other frameworks (also summarized in Table I).

### Physics Engine

Increasing the complexity and realism of physically simulated environments is essential for advancing robotics research. This includes improving the contact dynamics, having better collision handling for non-convex geometries (such as threads), stable solvers for deformable bodies, and high simulation throughput.

Prior frameworks using MuJoCo or Bullet focus mainly on rigid object manipulation tasks. Since their underlying physics engines are CPU-based, they need CPU clusters to achieve massive parallelization. On the other hand, frameworks for deformable bodies mainly employ Bullet or FleX, which use particle-based dynamics for soft bodies and cloth simulation. Recently, SofaGym, an RL framework specifically for soft robotics, shows the benefits of using finite-element-methods (FEM) for deformation models.. However, limited tooling exists in these frameworks compared to those for rigid object tasks. Orbit aims to bridge this gap by providing an integrated robotics framework that supports rigid and deformable body simulation via PhysX SDK 5. In contrast to other engines, PhysX SDK 5 features GPU-based hardware acceleration for high throughput, signed-distance field (SDF) collision checking, and more stable solvers based on FEM for deformable body simulation.

### Sensor simulation

Various existing frameworks use classic rasterization that limits the photo-realism in the generated images. Recent techniques simulate the interaction of rays with object's textures in a physically correct manner. These methods help capture fine visual properties such as transparency and reflection, thereby promising for bridging the sim-to-real visual domain gap. While recent frameworks include physically-based renderers, they mainly support camera-based sensors (RGB, depth). This is insufficient for certain mobile robot applications that need range sensors, such as LiDARs. Leveraging the ray-tracing technology in Nvidia Isaac Sim, Orbit supports all these modalities and includes APIs to obtain additional information such as semantic annotations.

Figure 1: Orbit’s abstractions comprise World, analogous to the real world, and Agent, the computation graph behind the embodied system. The nodes in the agent’s graph can perform observation-based or action-based processing. Through a graph-cut over this computation graph and specifying an extrinsic goal, it is feasible to design different tasks within the same World definition. For instance, to perform RL, this would define the task with ot, , and rt corresponding to the observation, action, and reward signals respectively.

### Scene designing and asset handling

Frameworks support scene creation procedurally, via mesh scans or through game-engine style interfaces. While mesh scans simplify generating large amounts of scenes, they often suffer from geometric artifacts and lighting problems. On the other hand, procedural generation allows leveraging object datasets for diverse scenes. While Isaac Sim mainly focuses on GUI-based scene designing, we choose to not be restrictive and build upon its interfaces to support all three methods for scene design.

## Orbit: Abstractions and Interfaces Design

At a high level, the framework design comprises a world and an agent, similar to the real world and the software stack running on the robot. The agent receives raw observations from the world and computes the actions to apply to the embodiment (robot). Typically in learning, it is assumed that all the perception and motion generation occurs at the same frequency. However, in the real world, that is rarely the case: sensors update at differing frequencies, depending on the control architecture, actions are applied at different time-scales, and unmodeled sources of delays and noises are present in the system. In Orbit, we thoughtfully design its interfaces and abstractions to support these functionalities and allow the inclusion of actuator and noise models to bridge the sim-to-real gap.

### World

Analogous to the real world, we define a world where robots, sensors, objects (static or dynamic), and visualization markers exist on the same stage. The world can be designed procedurally (script-based), via scanned meshes, or interactively through the game-based GUI of Isaac Sim, or a combination of them. This flexibility reaps the benefits of 3D reconstructed meshes, which capture various architectural layouts, with game-based designing, that simplifies the experience of creating and verifying the scene physics properties by playing the simulation.

Robots are a crucial component of the world since they serve as the embodiment for interaction. They consist of articulation, actuator models, and low-level joint controllers. We design these interfaces such that a single interface (such as LeggedRobot) supports a variety of robots belonging to the same category (such as ANYmal C or Unitree A1). This simplifies setting up a new robot with the simulator and using it in an existing World. The robot class loads the robot model from a USD file^11^1Universal Scene Description (USD) is a hierarchical file format, used in Omniverse, that allows storing assets, materials definitions, and various attributes (such as for physics, semantics, rendering) efficiently and flexibly. Orbit includes scripts to convert assets of different formats (URDF, obj, stl) into USD from the command line and adds various physics properties to them automatically, such as colliders and friction materials.. It creates and manages the necessary physics handles to set and read the simulation state. The actuator models play an important role in injecting real-world actuator characteristics into the simulation, such as delays or torque saturation. This can help facilitate the sim-to-real transfer of control policies on hardware (Sec. V-D). To apply actions on the robot, the joint-level controller processes input commands through actuator models before applying the desired joint position, velocity, or torque commands to the simulator (as shown in Fig. 2). Currently, we include actuator models for Direct Control (DC) motors and Series Elastic Actuators (SEA). However, it is easy for users to integrate the actuator model for their robot into Orbit after identifying its dynamics characteristics.

Figure 2: Illustration of actuator groups for a legged mobile manipulator. This allows decomposing a complex system into sub-groups and defining of specific transmission models for each of them flexibly. The number inside (⋅) is the dimension of the command vector.

Figure 3: Overview of features included in Orbit. We provide models of different sensors, robotic platforms, objects from different datasets, motion generators, and teleoperation devices. Using RTX-accelerated ray-tracing, we can obtain high-fidelity images in real-time for different modalities such as RGB, depth, surface normal, instance, and semantic segmentation (pixel-wise and bounding boxes).

Sensors (proprioceptive or exteroceptive) may exist both for the robot or externally (such as third-person cameras). While Orbit relies on Isaac Sim for different physics-based (range, force, and contact sensor) and rendering-based (RGB, depth, normals) sensors, it unifies them under a common interface to simplify creating and configuring them into a scene at runtime. We diverge from the recommended USD practice in Isaac Sim where sensors are expected to be specified in a USD file and all of them are updated at every simulation step. While this practice doesn't cause a huge issue for the traditional robotics paradigm, it leads to significant overhead when having parallelized scenes as there would exist undesired sensors updating in the scene. Through a common sensor management system in the world, Orbit configures the sensors required only for a given task. To simulate sensing at different frequencies, each sensor instance has its own internal timer that governs the operating frequency for reading the simulator buffers. Between the timesteps, the sensor returns the previously obtained values.

Objects are passive entities in the world. While several objects may exist in the scene, the user can define objects of interest for a specified task and set and retrieve properties/states only for them. For any given object, we support the randomization of its textures and physics properties, such as friction material and joint parameters. Similar to the robots class, we also include interfaces to augment the simulator with models for active motion components in an object. For instance, in a refrigerator, the hinge joint is stiff initially due to a magnetic seal but becomes free once the seal is broken. Accounting for these hybrid models in the simulation allows for developing and verifying methods to deal with the varying object dynamics in the real world.

Addition to above, the world also constitutes visualization markers. We allow programmatic additions of various primitive shapes to the simulator's GUI, such as axes, spheres, and meshes. These are often useful for development purposes, such as displaying the goal state or visualizing different coordinate frames. We integrate these markers into different robots and controller interfaces to readily allow visualization of useful frames such as the feet or end-effector poses.

### Agent

An agent refers to the decision-making process ("intelligence") guiding the embodied system. While roboticists have embraced the modularity of ROS, most robot learning frameworks often focus only on the environment (or MDP) definition. This practice leads to code replication and adds friction to switching between different implementations.

Keeping modularity at its core, an agent in Orbit comprises various nodes that formulate a computation graph exchanging information between them. Broadly, we consider nodes are of two types: 1) perception-based i.e., they process inputs into another representation (such as RGB-D image to point-cloud/TSDF), or 2) action-based i.e., they process inputs into action commands (such as task-level commands to joint commands). Similar to sensors, nodes also contain their own internal timers that control their update frequency. Currently, the flow of information between nodes happens synchronously via Python, which avoids the data exchange overhead of service-client protocols.

### Learning task and agent

Paradigms such as RL require specifying a task, a world and may include some computation nodes of the agent. The task logic helps specify the goal for the agent, compute metrics (rewards) to evaluate the agent's performance, and manage resets. With this component as a separate module, it becomes feasible to use the same world definition for different tasks, similar to learning in the real world, where tasks are specified through extrinsic reward signals. The task definition may also contain different nodes of the agent. An intuitive way to formalize this is by considering that learning for a particular node happens through a graph cut on the agent's computation graph.

To further concretize the design motivation, consider the example of learning over task space instead of low-level joint actions for lifting a cube. In this case, the task-space controller, such as inverse kinematics (IK), would typically run at 50 Hz, while the joint controller requires commands at 1000 Hz. Although the task-space controller is a part of the agent's and not the world's computation, it is possible to encapsulate that into the task design. This functionality easily allows switching between motion generators, such as IK, operational space control (OSC), or reactive planners.

Figure 4: Demonstration of the designed tasks using hand-crafted state machines and task-space controllers. Leveraging recent advances in physics engines, we support high-fidelity simulation of rigid and deformable objects. We include environments that allow switching between robots, objects, observations, and action spaces through configuration files (videos).

## Orbit: Features

While various robotic benchmarks have been proposed, the right choice of necessary and sufficient tasks to demonstrate "intelligent" behaviors remains an open question. Instead of being prescriptive about tasks, we provide Orbit as a platform to easily design new tasks. To facilitate the same, we include a diverse set of supported robots, peripheral devices, and motion generators and a large set of tasks for rigid and soft object manipulation for essential skills such as folding cloth, opening the dishwasher, and screwing a nut into a bolt. Each task showcases aspects of physics and renderer that we believe will facilitate answering crucial research questions, such as building representations for deformable object manipulation and learning skills that generalize to different objects and robots.

### Robots

We support 4 mobile platforms (one omnidirectional drive base and three quadrupeds), 7 robotic arms (two 6-DoF and five 7-DoF), and 6 end-effectors (four parallel-jaw grippers and two robotic hands). We provide tools to compose different combinations of these articulations into a complex robotic system such as a legged mobile manipulator. This provides a large set of robot platforms, each of which can be switched in the World.

### I/O Devices

Devices define the interface to peripheral controllers that teleoperate the robot in real-time. The interface reads the input commands from an I/O device and parses them into control commands for subsequent nodes. This helps not only in collecting demonstrations but also in debugging the task designs. Currently, we include support for Keyboard, Gamepad (Xbox controller), and Spacemouse.

### Motion Generators

Motion generators transform high-level actions into lower-level commands by treating input actions as reference tracking signals. For instance, inverse kinematics (IK) interprets commands as the desired end-effector poses and computes the desired joint positions. Employing these controllers, particularly in task space, has been shown to help sim-to-real transferability of robot manipulation policies.

With Orbit, we include GPU-based implementations for differential IK, operational-space control, and joint-level control, which compute commands for several robots efficiently. Additionally, we provide CPU implementation of state-of-the-art model-based planners such as RMP-Flow for fixed-arm manipulators and OCS2 for whole-body control of mobile manipulators. To facilitate research in legged robot navigation, such as traversability estimation and path-planning, we also include pre-trained policies for legged locomotion that track base velocity commands.

### Rigid- and Deformable-body Tasks

Orbit includes a suite of tasks for deformable and rigid object manipulation, as well as legged robot control and in-hand manipulation. These tasks serve not only as benchmarks for robotics research but also as examples for users to design new tasks easily. While some of these tasks have existed in prior works, we enhance them using the framework's interfaces to simplify switching between different robots, objects, motion generators, observations, and domain randomization. We also extend manipulation tasks for fixed-arm robots to mobile manipulators. Currently, the tasks mainly focus on a diverse set of skills such as grasping, screwing, stacking, pushing/pulling, pouring, folding, and walking (shown in Fig. 4). A complete and growing list of environments is available on our website.

## Exemplar Workflows with Orbit

Orbit is a unified simulation infrastructure that provides both pre-built environments and easy-to-use interfaces that enables extendability and customization. Owing to high-quality physics, sensor simulation, and rendering, Orbit is useful for multiple robotics challenges in both perception and decision-making. We outline a subset of such use cases through exemplar workflows.

### V-A Reinforcement Learning

Since the framework primarily stores data as tensors, the data needs to be formatted and converted to data types for different learning frameworks. We provide wrappers to rl-games, RSL-rl, and stable-baselines-3. These wrappers make the underlying environment RL framework agnostic and provide users access to a larger set of algorithms for research.

In Fig. 5, we show the training of Franka-Reach and Franka-Cabinet-Opening with PPO using different RL frameworks and action spaces. Although we ensure the same parameter settings for PPO in the frameworks, we notice a difference in their performance and training time due to implementation differences. Since RSL-rl and rl-games are optimized for GPU, we observe a training speed of 50,000-75,000 frames per second (FPS) with 2048 environments, while with stable-baselines3, we receive 6,000-18,000 FPS.

### V-B Teleoperation and Imitation Learning

Many manipulation tasks are computationally expensive or beyond the reach of current RL algorithms. In these scenarios, bootstrapping from user demonstrations provides a viable path to skill learning. Orbit provides a data collection interface that is useful for interacting with environments using I/O devices and collecting data similar to roboturk. We also support storing the data in the format desired by robomimic, which provides access to training various imitation learning (IL) models through it.

Figure 5: Example showing RL integration. We include wrappers to various RL frameworks. Additionally, it is possible to easily switch action spaces for training policies with different controllers. The plot shows the mean of the average return over five seeds.

Avg. Traj. Len TABLE II: Showcase of collecting demonstrations using teleoperation and performing imitation learning with them. We evaluate the trained policies for Franka-LiftCube in the same setting (No Change), changing initial states (I), goal states (G), and changing both initial and goal states (Both). The success rate and trajectory lengths are reported over 100 trials.

As an example, we show LfD for the Franka-LiftCube task. For each of the four settings of initial and desired object positions (fixed or random start and desired positions), we collect 2000 trajectories. Using these demonstrations, we train policies using Behavior Cloning (BC) and BC with an RNN policy (BC-RNN), and show their performance in Table II.

### V-C Motion planning

Motion planning is one of the well-studied domains in robotics. The traditional Sense-Model-Plan-Act (SMPA) methodology decomposes the complex problem of reasoning and control into possible sub-components. Orbit supports doing this both procedurally and interactively via the GUI.

### Hand-crafted policies

We create a state machine for a given task to perform sequential planning as a separate node in the agent. It provides the goal states for reaching a target object, closing the gripper, interacting with the object, and maneuvering to the next target position. We demonstrate this paradigm for several tasks in Fig. 4. These hand-crafted policies can also be utilized for collecting expert demonstrations for challenging tasks such as cloth manipulation.

### Interactive motion planning

We define a system of nodes for grasp generation, teleoperation, task-space control, and motion previewing (shown in Fig. 6). Through the GUI, the user can select an object to grasp and view the possible grasp poses and the robot motion sequences generated using the RMP controller. After confirming the grasp pose, the robot executes the motion and lifts the object. Following this, the user obtains teleoperation control of the robot.

Figure 6: Interactive grasp and motion planning demonstration using Orbit. The World comprises objects for table-top manipulation. The user can select an object from the GUI to grasp. This triggers an image-based grasp generator and allows previewing of the generated grasps and the robot motion sequence. The user can then choose the grasp and execute the motion on the robot.

Figure 7: Using the simulator as a digital twin to compute and apply the same commands on the simulated and real robot via ZMQ connection. We show the Franka Panda arm with an Allegro hand lifting two objects simultaneously, showcasing the realism in contact simulation. For videos, please check the website.

### V-D Deployment on real robot

Deploying an agent on a real robot faces various challenges, such as dealing with real-time control and safety constraints. Different data transport layers, such as ROSTCP or ZeroMQ (ZMQ), exist for connecting a robotic stack to a real platform. We showcase how these mechanisms can be used with Orbit to run policies on a real robot.

### Using ZMQ

To maintain lightweight and efficient communication, we use ZMQ to send joint commands from Orbit to a computer running the real-time kernel for Franka Emika robot. To abide by the real-time safety constraints, we use a quintic interpolator to upsample the 60 Hz joint commands from the simulator to 1000 Hz for execution on the robot (shown in Fig. 7).

We run experiments on two configurations of the Franka robot: one with the Franka Emika hand and the other with an Allegro hand. For each configuration, we showcase three tasks: 1) teleoperation using a Spacemouse device, 2) deployment of a state machine and 3) waypoint tracking with obstacle avoidance. The modular nature of the agent makes it easy to switch between different control architectures for each task while using the same interface for the real robot.

### Using ROS

A variety of existing robots come with their ROS software stack. In this demonstration, we focus on how policies trained using Orbit can be exported and deployed on a robotic platform, particularly for the quadrupedal robot from ANYbotics, ANYmal-D.

We train a locomotion policy entirely in simulation using an actuator network for the legged base. To make the policy robust, we randomize the base mass ($22 \pm 5$ kg) and add simulated random pushes. We use the contact reporter to obtain the contact forces and use them in reward design. The learned policy is deployed on the robot using the ANYmal ROS stack, (Fig. 8). This sim-to-real transfer indicates the viability of the simulated contact dynamics and its suitability for contact-rich tasks in Orbit.

Figure 8: Deployment of an RL policy on ANYmal-D robot using ROS connection (video). The policy is trained in simulation and runs at 50 Hz while the actuator net functions at 200 Hz.

Figure 9: Comparison of real and simulated data for a clamped beam scenario. The real data is collected using motion markers (shown on left). The simulated data is obtained using the FEM-solver in Isaac Sim over different hexahedral mesh resolutions (m).

### V-E Simulation Evaluation and Comparison

### Evaluation of simulation accuracy

Quantitatively measuring the accuracy of physics solvers is an arduous task due to the large variations and unknown mechanics of the real world. Thus, prior frameworks resort to qualitatively comparing the simulation to the physical world by rolling out the same action sequences. While Sec. V-D follows a similar practice to show realism in the rigid body simulation, we discuss the accuracy of deformable body simulation through a controlled experiment.

We consider a clamped beam made of highly deformable silicone elastomer. Following the setup used , we attach motion capture markers to the beam to collect deformation data under gravity's effect. In the simulation, we create a similar scenario by attaching a soft beam to a rigid wall and setting the same material properties (Young's modulus, density, and incompressibility) as the physical beam. As shown in Fig. 9, we observe that the damped oscillations in the simulated data follow closely to the collected real-world data. This showcases the solver's accuracy and indicates its potential for sim-to-real deformable body manipulation.

### Comparison of simulation throughput

We compare the throughput of the tasks in Orbit with those in other frameworks for rigid (robosuite, Maniskill2, IsaacGymEnvs) and deformable body interactions (DEDO). To ensure a fair comparison, we adapt the environments to have the same action space, simulation frequency, and control decimation. The evaluation is performed on a workstation with a 16-core AMD Ryzen 5950X, 64 GB RAM, and NVIDIA 3090RTX.

Figure 10: Simulation throughput for rigid body tasks333For rigid object environments, the numbers were computed using robosuite v1.4, ManiSkill2 v0.4, Isaac Gym Preview 4, and Isaac Sim 2022.1. For the cloth environment, we used DEDO v0.1 and Isaac Sim 2022.2.. CPU-based vectorization is limited to the available memory and scales poorly compared to GPU-accelerated simulation. Orbit performs at par with IsaacGym since they use the same physics engine.

Figure 11: Simulation throughput for cloth hanging task2. Orbit obtains 3× the throughput than DEDO while using PBD solver. However, increasing the number of nodes or points (pts) in the cloth mesh adversely affects its performance. The dotted line shows where the system ran out of memory.

Frameworks that rely on CPU-vectorization show an increase in throughput with the number of environments. However, at around 200-300 environments, their programs crash due to insufficient memory. In contrast, GPU-based parallelization scales better to a larger number of environments and achieves a throughput of $\sim 10$x faster for rigid body environments (Fig. 3) and $\sim 3$x faster for deformable body environments (Fig. 11). For the cloth task, we also examine the impact of using meshes of different resolutions on the throughput. We observe that a higher mesh resolution produces more accurate simulation but requires more computation time. To address this challenge, we intend to provide best practices for tuning the simulation and various sim-ready assets.

## Discussion

In this paper, we proposed Orbit: an interactive and intuitive framework to simplify environment designing, enable easy task specifications, and lower the entry barrier into robotics and robot learning. Orbit exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the simulation, and advance sensors, actuators, and motion generators at varying operating frequencies. It readily comes with different robotic platforms, sensors, CPU and GPU-based motion generators, and benchmark tasks that aim to provide a batteries-included experience for roboticists. The breadth of environments and robotic paradigms possible, as demonstrated in part in Sec. IV and Sec. V, make Orbit useful for a broad set of research questions in robotics. Through experiments, we show a significant throughput improvement on tasks designed in Orbit with respect to those in other frameworks, and its potential to facilitate sim-to-real transfer.

By open-sourcing this framework^44^4 Nvidia Isaac Sim is free with an individual license. Orbit is open-sourced on GitHub and available at we aim to reduce the overhead for developing new applications and provide a unified platform for robot learning research. As we continue to enhance and incorporate more features into the framework, we encourage researchers to contribute to transforming it into a comprehensive solution for robotics research.

## Future Work

Orbit can notably simulate physics at up to 125,000 FPS; however, camera rendering is currently bottlenecked to a total of 270 FPS for ten cameras rendering $640 \times 480$ images on an RTX 3090. While this number is comparable to other frameworks, we are actively improving the rendering speed through GPU-based acceleration.

While our experiments demonstrate the effectiveness of rigid-contact modeling and FEM for soft bodies, quantitatively studying the fidelity of the entire simulator (such as rendering, sensors, and physics) remains an area for future exploration. It is important to note that robotics research, particularly in deformable-body manipulation, has infrequently used sim-to-real due to difficulties in achieving fast and accurate simulation and realistic rendering. We believe that Orbit can help address these challenges and facilitate answering open research questions in these fields.

Further enhancements to the framework include integrating tactile sensors and 6-axis force-torque sensors. Additionally, we plan to add support for loading assets directly in their native formats (such as URDF and OBJ) instead of USDs to make the framework more versatile and user-friendly.
