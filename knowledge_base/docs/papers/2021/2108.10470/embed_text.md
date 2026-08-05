<!-- arxiv-full-text:v1 {"arxiv_id": "2108.10470", "source": "ar5iv"} -->

## Introduction

Figure 1: Isaac Gym allows high performance training on a variety of robotics environments. We benchmark on 8 different environments that offer a wide range of complexity and show the strengths of the simulator in blazing fast policy training on a single GPU. Top: Ant, Humanoid, Franka-cube-stack, Ingenuity. Bottom: Shadow Hand, ANYmal, Allegro, TriFinger.

In recent years, reinforcement learning (RL) has become one of the most promising research areas in machine learning and has demonstrated great potential for solving sophisticated decision-making problems. Deep reinforcement learning (Deep RL) has achieved superhuman performance in very challenging tasks, ranging from classic strategy games such as Go and Chess, to real-time computer games like StarCraft and DOTA. It has also shown impressive results in robotic settings, including legged locomotion and dexterous manipulation.

Simulators play a key role in training robots improving both the safety and iteration speed in the learning process. Training a humanoid robot that walks up and down stairs in the real world can lead to damage to its machinery and the environment, including humans that are working on the robot. An alternative is to train inside simulators that offer an efficient and scalable platform via trial-and-error with no safety issues as observed in the real world. To date, most researchers have relied on a combination of CPUs and GPUs to run reinforcement learning system. Different parts of the computer tackle different steps of the physics simulation and rendering process. CPUs are used to simulate environment physics, calculate rewards, and run the environment, while GPUs are used to accelerate neural network models during training and inference as well as rendering if required.

However, switching back and forth between CPU cores optimized for sequential tasks and GPUs which offer large-scale parallelism is by nature inefficient, requiring data to be transferred between different parts of the system at multiple points during the training process. Therefore, scalability of deep reinforcement learning in robotics is faced with two critical bottlenecks: 1) enormous computational requirements and 2) limited simulation speed. These problems are especially challenging when learning long-horizon behaviours for robots with high degrees of freedom.

Popular physics engines like MuJoCo, PyBullet, DART, Drake, V-Rep etc. need large CPU clusters to solve challenging RL tasks naturally face these bottlenecks. For instance, , almost 30,000 CPU cores (920 worker machines with 32 cores each) were used to train a robot to solve the Rubik's Cube task using RL. In a similar task, used a cluster of 384 systems with 6144 CPU cores, plus 8 NVIDIA V100 GPUs, and required 30 hours of training for RL to converge.

One way to speed-up simulation and training is to make use of hardware accelerators. GPUs have enjoyed enormous success in computer graphics are also naturally suited for highly parallel simulations. This approach was taken , and showed very promising results running simulation on GPU, proving that it is possible to greatly reduce both training time as well as computational resources required to solve very challenging tasks using RL. However, some bottlenecks were still not addressed in the work -- simulation was on GPU but physics state was copied back to CPU. There, observations and rewards were calculated using optimized C++ code and later copied back to GPU where policy and value networks ran. Furthermore, only simplified physics-based scenarios were trained, rather than representative robotic environments, and no attempt was made to show sim2real.

To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform. It runs an end-to-end GPU accelerated training pipeline, which allows researchers to overcome the aforementioned limitations and achieves 2-3 orders of magnitude of training speed-up in continuous control tasks. Isaac Gym leverages NVIDIA PhysX to provide a GPU-accelerated simulation back-end, allowing it to gather experience data required for robotics RL at rates only achievable using a high degree of parallelism. It provides a PyTorch tensor-based API to access the results of physics simulation natively on the GPU. Observation tensors can be used as inputs to a policy network and the resulting action tensors can be directly fed back into the physics system. We note that others have recently begun attempting an approach similar to Isaac Gym with respect to running end-to-end training on hardware accelerators.

With the end-to-end approach, roll-outs of observation, reward, and action buffers can stay on the GPU for the entire learning process, eliminating the need to read data back from the CPU. This set-up permits tens of thousands of simultaneous environments on a single GPU, allowing researchers to easily run experiments locally on their desktops that previously required an entire data center and to solve previously out of reach tasks using just a small GPU server.

Isaac Gym provides a straightforward API for creating and populating a scene with robots and objects, supporting loading data from the common URDF and MJCF file formats. Each environment is duplicated as many times as needed, while preserving the ability for variations between copies (e.g. via Domain Randomization ). Environments are simulated simultaneously in parallel without interaction with other environments. Using a fully GPU-accelerated simulation and training pipeline can help lower the barrier for research, enabling solving of tasks with a single GPU that were previously only possible on massive CPU clusters. Isaac Gym also includes a basic Proximal Policy Optimization (PPO) implementation and a straightforward RL task system, but users may substitute alternative task systems or RL algorithms as desired. While the included examples use PyTorch, users should also be able to integrate with TensorFlow training libraries with further customization. An overview of the system is provided in Figure 2.

Figure 2: An illustration of the Isaac Gym pipeline. The Tensor API provides an interface to Python code to step the PhysX backend, as well as get and set simulator states, directly on the GPU, allowing a 100-1000x speedup in the overall RL training pipeline while providing high-fidelity simulation and the ability to interface with existing robot models.

Our major contributions include: • Development of high-fidelity GPU-accelerated robotics simulator for robot learning tasks. • A Tensor API in Python providing direct access to physics buffers by wrapping them into PyTorch tensors without going through any CPU bottlenecks. • Implementation of multiple highly complex robotic manipulation environments which can be simulated at hundreds of thousands of steps per second on a single GPU. • High-performance training results using Isaac Gym with Deep Reinforcement Learning on challenging robotic environments. Our major empirical results include: • We achieve significant speed-ups in training various simulated environments: Ant and Humanoid environments can achieve performant locomotion in 20 seconds and 4 minutes respectively, ANYmal in under 2 minutes, Humanoid character animation using AMP in 6 minutes and cube rotation with Shadow Hand in 35 minutes all on a single NVIDIA A100 GPU. • Additionally, we reproduce OpenAI Shadow Hand cube training setup with asymmetric actor-critic and domain randomization. We show that we can achieve similar performance to OpenAI results of 20 consecutive successes with feed forward and 37 consecutive successes with LSTM networks with a success tolerance of 0.4 rad in about 1 hour and 6 hours on an average respectively on A100. In contrast, OpenAI effort required 30 hours and 17 hours respectively on a combination of a CPU cluster (384 CPUs with 16 cores each) and 8 NVIDIA V100 GPUs with MuJoCo using a conventional RL training setup. It is worth mentioning that since OpenAI show results with only 1 seed, comparing our best seed we find that we achieve 37 consecutive successes with LSTMs in just 2.5 hours. • We also demonstrate sim-to-real transfer results on ANYmal and TriFinger which further showcases the ability of our simulator to perform high-fidelity contact rich manipulation.

## Background

### Parallelization Strategy

There are many approaches to parallelizing physics simulations. We outline these approaches here and justify our design decisions in the context of GPU-accelerated simulation tailored towards learning algorithms. Isaac Gym was developed to maximize the throughput of physics-based machine learning algorithms with particular emphasis on simulations that require large numbers of environment instances executing in parallel.

### CPU Simulations

When physics simulation runs on CPU, multiple threads can be used to distribute computation among the available cores. The most straightforward strategy is simulating one environment instance per thread. In this approach, scaling is limited by the number of physical cores in the system. On a 64-core hyper-threaded CPU, we could run up to 128 environments in parallel, but CPUs with a large number of cores are typically clocked lower to prevent overheating. Running tens or hundreds of threads comes with other potential pitfalls including synchronization, context-switching overhead, and memory bandwidth limitations. To scale further, we would need to use a multi-CPU setup or build a cluster, which introduces additional communication overhead.

Running a single environment instance per thread in its own dedicated physics scene can be inefficient. There is some overhead involved in setting up, executing, and gathering the results of each physics step. The simpler the environment, the more significant the overhead. To mitigate this, we can pack multiple environments into a single physics scene. For example, we could split 1024 environments into eight physics scenes with 128 environments each. Each scene can run in its own thread. Extra provisions are needed to ensure that environments in the same scene do not interact with each other physically, which can be done using contact filtering and other methods.

### GPU Simulations

Running the physics simulation on GPU can result in significant speedups, especially for large scenes with thousands of individual actors. On the GPU, the physics engine can parallelize computations at the level of individual shapes, bodies, or joints. High-end GPUs require many thousands of objects to effectively utilize their streaming multiprocessor architecture. This makes them a good match for running simulations with thousands of environment instances. On GPU, we don't need to worry about splitting the environments into multiple scenes. In fact, the opposite is generally true - we want to pack everything into a single scene to take advantage of the deep fine-grained parallelism and maximize the overall throughput.

Physics simulations on a GPU is not new. In previous work, we demonstrated good results with running GPU physics simulations for reinforcement learning. In this work, the GPU was used as a co-processor that accelerates the physics simulation, while the API for getting physics state and applying controls was CPU-based. There are, however, performance bottlenecks with this strategy. In a reinforcement learning pipeline, physics simulation is just one part of the system. After a physics step, we need to get the latest physics state to compute observations and rewards. If these computations are done on the CPU, we need to transfer the physics state from the GPU. While modern hardware architectures can achieve impressive data transfer speeds, large simulations can incur nontrivial overhead. Then, the raw physics state needs to be processed on the CPU to compute observations and rewards, which is subject to similar parallelization challenges as discussed above due to the limited number of CPU cores. Next, the observations and rewards need to be copied from system memory back to device memory for the reinforcement learning algorithm. After the learning step, a set of actions is generated by the policy network on the GPU. These actions need to be copied to the CPU so that they can be converted to physics simulation inputs. Those inputs end up being copied to the GPU again to run the next step of physics simulation on the device.

Isaac Gym eliminates those inefficiencies by keeping all of the computations on the GPU. Stepping physics, computing observations and rewards, and applying actions are performed on the GPU without ever copying large quantities of data between devices. Two new features were added to PhysX to facilitate this. First, PhysX GPU simulations can run without fetching the results to the CPU after every step. Second, a new direct GPU API was added to access the current state, submit state changes, and apply control inputs in GPU buffers. In Figure 3, we contrast the traditional RL experience collection pipeline with our high throughput fully GPU-based pipeline.

(a) Traditional RL experience collection. (b) Isaac Gym experience collection. Figure 3: (a) Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. (b) In contrast, Isaac Gym not only runs physics on the GPU but also directly copies the physics data to the deep neural network framework using CUDA interoperatability without ever using CPU in the process. This massively improves the performance of RL training process leading to significantly faster training times.

### Simulation Setup

Isaac Gym provides a simple procedural API to create environments and populate them with actors. It supports loading assets from URDF and MJCF file formats. These assets can be instanced multiple times in simulation environments to create actors. In the underlying PhysX engine, single-body actors are created as rigid dynamics and multi-body actors are created as reduced coordinate articulations. During the setup phase, users can set initial actor poses, configure joint drives, and customize rigid body properties and physics materials. Most joint and rigid body properties can be changed during the simulation as well, which facilitates domain randomization without stopping and restarting the simulation. Below we provide definitions of some useful terms.

Actor: An entity composed of rigid bodies connected via joints. It can be created via direct loading of a URDF model or XML file composed of either meshes or primitive shapes.

Rigid Bodies: A primitive shape or a mesh model that comprises an actor is called a rigid body. The positions, rotations and velocities of a rigid body can be obtained via the API.

DOF States: Rigid bodies are connected by various joints. A joint can have 0 or more degrees of freedom. Fixed joints have no DOFs, revolute and prismatic joints have 1 DOF and spherical joints have 3 DOFs. The DOF states, which include joint position and velocity, can be obtained via the API.

The setup code runs on the CPU to allow flexibility in per-instance setup, but once the simulation starts Isaac Gym provides a tensor API that can be used to interact with the running simulation on either CPU or GPU. Users can specify the device to be used for the simulation and the tensor interface in the simulation parameters.

Figure 4: Tensors associated with the scene composed of multiple copies of the same environment simulating different variations all running in parallel. Each actor (e.g. table, box or franka) has various bodies and their corresponding positions, quaternions and velocities are stored directly in PyTorch tensors.

### Tensor API

Isaac Gym provides a data abstraction layer over the physics engine. This allows us to support multiple physics engines with a shared front-end API. In this work, the physics engine is PhysX, although some limited tensor API functionality is available with the FleX physics engine as well.

Instead of calling physics engine functions directly, users can access all of the physics data in flat buffers. This data-oriented approach allows us to eliminate a lot of overhead caused by looping over tens of thousands of individual simulation actors in user code. Physics state is exposed to Python users as global tensors. For example, all rigid body states can be found in a single rigid body state tensor. Figure 4 shows a typical Isaac Gym scene composed of various copies of the same environment simulating different variations all running in parallel and the corresponding tensors associated with it. Control inputs can be applied using global tensors as well. For example, applying forces to all rigid bodies in the simulation can be done using a single function call that takes a tensor containing all of the forces. Users can create custom views or slices of the global tensors to suit their needs. When multiple environment instances are packed into the simulation, it is possible to create custom views of the data with the environment index as one of the dimensions. This makes it easy to vectorize observation and reward computations by running GPU kernels on multiple environments in parallel.

### Python Interface

The core of Isaac Gym is implemented using C++ and CUDA. It is completely independent of any Python frameworks commonly used in machine learning. To make the data easily accessible to Python users, Isaac Gym provides utilities that can \"wrap\" the raw data buffers as tensor objects in common machine learning frameworks like PyTorch. The tensor-wrapping utilities make it possible to share the native CPU or GPU buffers with Python without any copying overhead.

A powerful feature of Isaac Gym is the ability to run the same code on either CPU or GPU by simply toggling a flag. Python users do not need to write custom CUDA or C++ kernels to compute observations, rewards, or actions. When physics state and control tensors are wrapped as PyTorch tensors, users can take advantage of TorchScript JIT to compile their Python functions to lower level scripts which orchestrate the training pipeline quickly.

### Physics State Tensors

Actor root state State of all actor root bodies (position, orientation, linear and angular velocity).

State of all degrees of freedom (position and velocity).

Rigid body state State of all rigid bodies (position, orientation, linear and angular velocity).

Net forces experienced at each degree of freedom.

Rigid body forces Rigid body forces and torques experienced at force sensor locations.

Net contact forces Net forces experienced by each rigid body.

Jacobian matrices for a homogeneous group of actors.

Generalized mass matrices for a homogeneous group of actors.

Table 1: Physics state tensors. NA is the total number of actors, NB is the total number of rigid bodies (including articulation links), ND is the total number of degrees of freedom, and NF is the total number of rigid body force sensors.

Physics state tensors are used to obtain state snapshots of a running simulation. Isaac Gym allows for interacting with the simulation using maximal and reduced coordinates. Physics state includes the kinematic state of rigid bodies and degrees of freedom (DOFs). Rigid body state consists of position, orientation (quaternion), linear velocity, and angular velocity. DOF state includes position and velocity. In the code snippet below we show how to access them through the API.

## Acquire tensor descriptors

## Raw storage buffer independent of client framework

## Storage will be on GPU if using GPU pipeline, CPU otherwise

## Same code for CPU and GPU just different device

root_state_desc = gym.acquire_actor_root_state_tensor(sim) dof_state_desc = gym.acquire_dof_state_tensor(sim)

## PyTorch interop

## No data copying, just wrap the gym buffers as torch tensors

## The root state tensor captures the state of the root bodies of all actors

root_states = gymtorch.wrap_tensor(root_state_desc) dof_states = gymtorch.wrap_tensor(dof_state_desc)

## obtaining physics states

## Physics state includes kinematic states of rigid bodies and degrees of freedom (DOFs)

root_state_vec = root_states.view(num_envs, actors_per_env, 13) dof_state_vec = dof_states.view(num_envs, dofs_per_env, 13) root_p = root_states[..., 0:3] # positions of rigid bodies root_q = root_states[..., 3:7] # rotations, in quaternions, of rigid bodies root_v = root_states[..., 7:10] # linear velocities of rigid bodies root_a = root_states[..., 10:13] # angular velocities of rigid bodies dof_p = dof_state_vec[..., 0] # joint positions dof_v = dof_state_vec[..., 1] # joint velocities Obtaining state information by wrapping physics buffers into PyTorch tensors. CUDA interoperability allows copying the data directly without ever going through the host.

Revolute DOFs use radians and linear DOFs use meters for units. Additional state data includes contact forces, rigid body force sensors, and DOF force sensors. To support operational space control and inverse kinematics applications, Isaac Gym also provides Jacobian and generalized mass matrices which can be obtained for articulated actors.

The available state tensors are listed in Table 1. Most of the state tensors are read-only, except the root state tensor and the DOF state tensor. These two tensors play a special role, because they can be used to fully set the poses and velocities of actors. This can be used during environment resets, when new poses are generated or original poses need to be restored. The root state tensor captures the state of the root bodies of all actors. For single-body actors, the root state fully captures their poses and velocities in maximal coordinates. For articulated actors, the root state can be used to \"teleport\" them without changing the poses of the descendant articulation links. The DOF state tensor can be used to configure the descendant articulation links using reduced coordinates. Setting new DOF states does not affect the root state. For fixed-base articulated actors, such as mounted robotic arms, the DOF state tensor fully captures the articulation poses and velocities. Users can apply new root and DOF states for all actors at once or to a limited subset using an index buffer. This allows resetting a subset of environments without affecting the rest.

### Physics Control Tensors

Physics simulation inputs include forces, torques, and PD controls such as position and velocity targets. Forces and torques can be applied to rigid bodies and DOFs. PD targets are applied to DOFs that have been configured to use position or velocity drives. Users can configure the drive parameters like stiffness and damping using a separate API. Table 2 lists the available control tensors. The control tensors are typically created in a higher-level framework like PyTorch, but can be efficiently shared with Isaac Gym using the tensor-wrapping utilities.

DOF actuation forces Torques or linear forces to be applied to degrees of freedom. All actors or indexed subset DOF position targets PD position targets for degrees of freedom. All actors or indexed subset DOF velocity targets PD velocity targets for degrees of freedom. All actors or indexed subset Rigid body forces Forces to be applied to rigid bodies. All rigid bodies Rigid body torques Torques to be applied to rigid bodies. All rigid bodies Table 2: Physics control tensors. NB is the total number of rigid bodies (including articulation links) and ND is the total number of degrees of freedom.

## Physics Simulation

Robots are simulated using PhysX reduced coordinate articulations. Any individual rigid bodies may be simulated using either maximal coordinate rigid bodies or single-link reduced coordinate articulations. Articulations with a single link and rigid bodies are equivalent and interchangeable. We also support tendons to actuate degrees of freedom and they are simulated in PhysX using Fixed Tendon mechanics. The physics of tendons are described in detail in Section A.1. We tested the dynamics of tendons using the Shadow Hand simulation environment, described in Section 6.4.1.

We use the Temporal Gauss Seidel (TGS) solver to compute the future states of objects in our physics simulation. The TGS solver uses the observation that sub-stepping a simulation with a single gauss-seidel solver iteration yields significantly faster convergence than running larger steps with more solver iterations. It folds this process efficiently into the iteration process, calculating the velocity at the end of each iteration and accumulating these velocities (scaled by ${dt}/N$, where $N$ is the number of iterations) into a per-body accumulated delta buffer. This delta buffer is projected onto the constraint Jacobians and added to the bias terms in the constraints. This approach adds only a few additional operations to a more traditional Gauss-Seidel solver, producing almost identical performance cost per-iteration. However, it achieves the same effect on convergence as having sub-stepped the simulation without the computational expense. With positional joint constraints, an additional rotational term is calculated for joint anchors to improve handling of non-linear motion to avoid linearization artifacts. This term is not necessary (and in fact undesirable) to add to contacts. Various parameters exposed to the user to tune the simulator are described in Table 3.

Controls time-step size Controls the gravity in the scene Filters collisions between shapes Biased (velocity + positional error correcting) solver iterations Unbiased (velocity error only correcting) solver iterations Max bias coefficient Limits the magnitude of position error bias Friction Static/dynamic friction Static and dynamic friction coefficients Relative normal velocity limit below which restitution is ignored Distance at which shapes are held separated. Default is 0 but can be increased to hold objects at gap. Useful for thin objects.

Friction offset threshold Distance at which friction anchors are discarded (static friction depends on friction anchor caching) Solver offset slop An epsilon value used to correct for round-off errors in contact gen. Corrects small skew effects with rolling spheres or capsules.

Friction correlation distance Distance at which contacts are merged into a single Per-body and per-contact force limits Positional error correction coefficient of a PD controller Velocity error correction coefficient of a PD controller Per-joint frictional term. Simulates dry friction in a joint.

Per-joint armature term - simulates motor inertia.

Body/link Damping World-space linear/angular damping on each body/link Linear/angular velocity limits per-body Table 3: Parameters exposed to tune the simulator.

## Environments

We implemented a diverse set of environments covering different application areas. Here we describe a subset of representative examples and key points related to the training. Benchmark results on the simulation performance and training results are presented in the subsequent sections.

All environments are trained using the Proximal Policy Optimization algorithm, using rl_games, a highly-optimized GPU end-to-end implementation. This implementation vectorizes observations and actions on GPU allowing us to take advantage of the parallelization provided by the simulator. We list the environments used in our experiments below: 1\. Locomotion Environments • Ant • Humanoid • Ingenuity • ANYmal 2. Franka Cube Stacking 3. Humanoid Character Animation 4. Robotic Hands • Shadow • Allegro • Trifinger While Ant and Humanoid are relatively simple environments popularised by MuJoCo continuous control benchmarks, the strength of our simulator really shines when training on environments that are rich in complexity particularly robotic hands. Various meta-data related to simulation setup for these environments is in Table 4.

### Key Experimental Details

Unless stated otherwise, all experiments are done on a system with a single NVIDIA A100 GPU and a single 3.7GHz Intel i7-8700K CPU All training runs for each environment are averaged over 5 seeds. The reward curves are plotted with $\mu \pm \sigma$ regions.

All the environments by default follow symmetric actor-critic approach with shared observations as well as shared network for policy and value functions. Sharing the network allows faster forward passes and improves training.

Moreover, for Shadow Hand and TriFinger, we also use an asymmetric actor critic approach with policy observations that are closest to real world settings while value function receives privileged state information from simulation as well as the observations received by the policy. This approach is naturally suited for sim-to-real transfers.

For all environments trained with feed forward networks we use a discount factor of $\gamma = 0.99$ while LSTM networks use $\gamma = 0.998$. We use a GAE discount factor, $\lambda = 0.95$ and clipping $\epsilon = 0.2$. Also, we use an adaptive learning rate and varying KL thresholds per environment.

Detailed hyper-parameters for each training task are shown in Table 17. Rewards and observations for each environment we used can be found in Appendix A.2.

Rigid Body Forces Joint Position Targets Franka Cube Stacking Operation Space Control Shadow Hand Standard Joint Position Targets Shadow Hand OpenAI Joint Position Targets Joint Position Targets Table 4: Simulation setup for the environments.

## Characterising Simulation Performance

We first characterise the simulation performance as a function of number of environments. As we vary this number, we aim to keep the overall experience an RL agent observes constant by decreasing the horizon length proportionally (i.e. number of steps in PPO) for a fair comparison. While we provide detailed training studies for many environments later, we characterise simulation performance only for Ant, Humanoid and Shadow Hand as they are sufficiently complex to test the limits of the simulation and also represent a gradual increase in the complexity. All three environments use feed forward networks for training.

### Ant

(a) Rewards (b) Total number of environment steps per second Figure 5: Rewards and effective FPS with respect to number of parallel environments for the Ant experiment. Best training time is achieved with 8192 environments and a horizon lengths of 16.

We first experiment with the standard Ant environment where the agent is trained to run on a flat ground. We find that as the number of agents is increased, the training time, as expected, is reduced i.e. changing the number of environments from 256 to 8192 --- an increase by 5 orders of magnitude --- leads to a reduction in training time to reach 7000 reward by an order of magnitude from 1000 seconds (\~16.6 minutes) to 100 seconds (\~1.6 minutes). However, note that Ant reaches performant locomotion at 3000 reward in just 20 seconds on a single GPU.

Since Ant is one of the simplest environments to simulate, the number of parallel environment steps per second as depicted in the Figure 5(b) can go as high as 700K. We do not observe gains when increasing the number of environments from 8192 to 16384 due to reduced horizon length.

### Humanoid

The Humanoid environment has more degrees of freedom and requires the agent to discover the gait that lets itself balance on two feet and walk on the ground. As observed in Figure 6 and Figure 7, the training times are increased by an order of magnitude compared to the Ant in Figure 5.

(a) Rewards (b) Total number of environment steps per second Figure 6: Rewards and effective FPS with respect to number of parallel environments for the Humanoid experiment. Best training time is achieved with 4096 environments and a horizon lengths of 32.

(a) Rewards (b) Total number of environment steps per second Figure 7: Rewards and effective FPS with respect to number of parallel environments for the Humanoid experiment. Best training time is achieved with both 4096 and 8192 environments and horizon lengths of 64 and 32 respectively.

We also note in Figure 6 that as the number of agents is increased, in this case, from 256 to 4096, the training time needed to reach the highest reward of 7000 is reduced by an order of magnitude from $10^{4}$ seconds (\~2.7 hours) to $10^{3}$ seconds (\~17 minutes). However, performant locomotion starts happening at around a reward of 5000 at a training time of just 4 minutes. Going beyond 4096 environments for this set up resulted in no further gains and in fact led to both increase in training time and sub-optimal gaits. We attribute this to the complexity of the environment that makes it challenging to learn walking at such small horizon lengths.

We verified this by training on another set of environment and horizon length combinations where horizon length was increased by a factor of 2 compared to Figure 6. As shown in the Figure 7, the humanoid is able to walk even with 8192 and 16384 environments which have small horizon lengths of 32 and 16 respectively but sufficiently long to enable learning.

Also worth noting that due to the increased degrees of freedom the number of parallel environment steps per second is reduced from 700K for Ant to 200K for Humanoid as shown in Figures 6 and 7.

### Shadow Hand

(a) Rewards. (b) Total number of environment steps per second Figure 8: Rewards and effective FPS with respect to number of parallel environments for the Shadow Hand experiment. Best training time is achieved with both 8192 and 16384 environments and horizon lengths of 16 and 8 respectively.

Lastly, we experiment with Shadow Hand to learn to rotate a cube resting on the palm to a target orientation using the fingers and the wrist. This task is challenging due to the number of DoFs involved and the contacts that are made and broken during the process of rotation. Our results with Shadow Hand environment follow similar trends. As the number of agents is increased, in this case, from 256 to 16384, the training time is reduced by an order of magnitude from $5 \times 10^{4}$ seconds (\~14 hours) to $3 \times 10^{3}$ seconds (\~1 hour). We find that the environment reaches performant dexterity of 10 consecutive successes at reward of 3000 in just 5 minutes.^11^1The experiments used Shadow Hand Standard variant as explained in Section 6.4.1. Further performance improvements continue to happen as more experience is collected. Additionally, we find that the horizon length of 8 for 16384 agents still allows learning re-posing the cube. The maximum effective frame-rate of 150K number of parallel environment steps per second was achieved with 16384 agents.

## Characterising Environment Performance

We now provide details and performance metrics for individual environments mentioned in Section 4 trained using a PPO implementation that operates on vectorised states and actions.

Figure 9: Locomotion environments and the corresponding reward curves.

### Locomotion environments

### Ant

The Ant model has four legs with two degrees of freedom per leg. On A100 with 4096 agents simulated in parallel we find that ant can learn to run and achieve a reward above 3000 in just 20 seconds, and fully converge in under 2 minutes. The average simulation performance achieved during training is 540K environment steps per second. The results are shown in Figure 9(a). For details of the reward function used, we refer to Appendix A.2.1 and for the observations used, we refer to Appendix A.2.1.

### Humanoid

The Humanoid environment has 21 DOFs and on a A100 with 4096 agents simulated in parallel we can train it to run --- a reward threshold of 5000 --- in less than 4 minutes. This is 4x faster than our previous results in obtained using the same threshold. As shown in Figures 6 and 7, we achieve peak performance for this environment at 4096 agents. Figure 9(b) shows the evolution of reward as a function of time. For details of the reward function used, we refer to Appendix A.2.1 and for the observations used, we refer to Appendix A.2.1.

### Ingenuity

We train a simplified model of NASA's Ingenuity helicopter to navigate to a target that periodically teleports to different locations. The environment with trained with 4096 agents and achieves a reward of 5000 in just under 30 seconds. Forces are applied directly to the two rotors on the chassis, rather than simulating aerodynamics. We use a gravity value of -3.721 $m/s^{2}$ to simulate martian gravity. In Figure 9(c) we show how the reward increases as a function of time.

### ANYmal Robot Locomotion

ANYmal is a robot developed by ANYbotics for industrial maintenance. It is a four-legged dog-like robot, and has been used for experiments on navigation of rough and variable terrain. We train the robot to follow target X, Y, and yaw base velocities while minimizing joint torques. The target velocities are randomized at each reset and are provided as observations alongside the positional and angular velocities of the base, the measured gravity vector, most recent actions, and DOF positions and velocities. With 4096 agents simulating in parallel, we find that the robot is able to follow the targets in under 2 minutes as shown in Figure 9(d). The reward function is defined in A.2.2

### ANYmal Sim-to-real on Uneven Terrain

In addition to the simple flat terrain environment, we have developed a rough terrain locomotion task for ANYmal and validated the approach by transferring trained policies to the real robot. The robot learns to walk on uneven surfaces, slopes, stairs and obstacles. In addition to the observations of the flat terrain environment it receives terrain height measurements around the robot's base. For sim-to-real transfer we extend the reward function, add noise to the observations, randomize the friction coefficient of the ground, randomly push the robots during the episode and add an actuator network to the simulation. Following the approach used , the actuator network is trained to model the complex dynamics of the series elastic actuators of the real robot.

Figure 10: Trained policy for ANYmal on rough terrain tested in simulation and on the real robot.

We implement an automatic curriculum of increasing terrain difficulties. The robots start to learn on simple versions of the terrains, and when they are able to solve a certain level the difficulty is automatically increased. In order to avoid costly terrain generation during training, we create a single mesh with all terrain types and levels and change the robots' reset location depending on their progress. With 4096 environments, we can train the full task on NVIDIA RTX A6000 and transfer to the real robot in under 20 minutes. We refer to for more details.

### Humanoid Character Animation

We evaluate the performance of Isaac Gym on adversarial imitation learning tasks using an implementation of adversarial motion priors (AMP). This technique enables physically simulated humanoid character to imitate complex behaviors from reference motion data. Instead of a manually engineered imitation objective, as is commonly used in prior systems, AMP learns an imitation objective using an adversarial discriminator trained to differentiate between motion from the dataset and motions produced by the policy.

Figure 11: Humanoid character trained using AMP to imitate a spin-kick.

Our character is modelled as a 34-DOF humanoid, and all motion clips are recorded from human actors using motion capture. Table 12 in Appendix A.2.2 details the observation features. The adversarial training process enables the character to closely imitate a diverse corpus of motions, ranging from common locomotion behaviors, such as walking and running, to more athletic behaviors, such as spin-kicks and dancing. Effective policies can be learned with approximately 39 million samples, requiring approximately 6 minutes with 4096 environments. The implementation provided by Peng et al., 2021 requires about 1 day (30 hours) on 16 CPU cores to simulate a similar number of samples in PyBullet. Therefore, Isaac Gym provides 300x or 2.48 orders of magnitude improvement in the training time.

### Franka Cube Stacking

Figure 12: The Franka Cube Stacking environment and the corresponding reward curves.

We use 16384 agents to train a Franka robot to stack a cube on top of an other. In this environment, we use a slightly different choice of action space, Operation Space Control (OSC), for learning. OSC is a task-space compliant controller that has been shown to enable faster policy learning compared to joint-space controllers and learn contact-rich tasks. Our OSC implementation is fully differentiable in Isaac Gym and we obtain convergence with this controller in under 25 minutes. Figure 12 shows the training results.

### Robotic Hands

Figure 13: The three in-hand manipulation environments implemented in Isaac Gym: Shadow Hand, Trifinger, and Allegro.

(d) Allegro Hand Standard Figure 14: Reward curves for the three in-hand manipulation environments implemented in Isaac Gym. These results are obtained with (a) Shadow Hand with OpenAI observation and LSTMs, (b) Shadow Hand with OpenAI observation and feed forward networks (c) Shadow Hand with Standard observations and (d) Allegro Hand with Standard observations. Shadow Hand OpenAI is trained with asymmetric actor-critic and domain radomisation while Shadow Hand Standard and Allegro Hand Standard are trained with standard observations and symmetric actor-critic with no domain randomisation.

Large-scale simulation has the ability to solve not just individual instances but whole classes of problems in robotics, by leveraging the generality of the model-free reinforcement learning framework. Dexterous manipulations is one of the most challenging problems in robotics.

To show the performance of our simulator and the ability to realistically model contact we implemented 3 different hand training environments as shown . Shadow Hand and Allegro Hand are trained to learn cube orientation while TriFinger learns to repose the cube in 6 degrees-of-freedom involving rotation and translation. We now focus on the specific training details for these environments.

Firstly, the Shadow Dexterous Hand. We follow the standard formulation where policy and value function both receive the same input as well as OpenAI observations with asymmetric formulation and domain randomisation . Secondly, the TriFinger robot, which shows the ability to do 6-DoF manipulation by reposing the cube to a desired position and orientation, a task which has previously shown to be challenging for model-free reinforcement learning. We use asymmetric actor-critic and domain randomisation for TriFinger and demonstrate sim-to-real transfer on a real robot. Finally, we reuse system from the Shadow Hand to the Allegro hand with minimal changes to show the generality of our approach. These three environments are depicted in Figure 13 and the corresponding reward curves in Figure 14.

### Shadow Hand

As mentioned, the task with Shadow Hand is to manipulate the cube to achieve a specific target orientation and is inspired by OpenAI et al.. We train with multiple variants on the Shadow Hand environment and describe them below:

### Shadow Hand Standard

In this setting, we use a standard formulation for training where the policy and the value function use feed forward networks and receive the same input observations. The default observations we used for the Shadow Hand Standard include joint position, velocities, forces, force-torque sensors reading from each fingertip, manipulated object position and orientation, linear and angular velocities, goal orientation, relative rotation between the current object and target rotations, actions applied on the previous step. For a detailed overview of observation and reward, see Appendix A.4. Also note that this variant does not use any randomisations.

### Shadow Hand OpenAI

We also reproduce results with OpenAI Shadow Hand experiments in Isaac Gym with observations used in dexterity work from OpenAI et al.. A key difference between this and the Shadow Hand Standard variant is that it uses asymmetric observations. The policy receives only the input observations that are possible to obtain in the real world settings while the value function receives the same observations in addition to the other privileged information available from the simulator. This variant should make it possible to transfer the policy to the real world, mimicking the setup . The observations for the policy and value function are provided in Table 14. We experiment with both feed forward networks (SH OpenAI FF) and LSTMs (SH OpenAI LSTM). The LSTM networks are trained with a sequence length of 4.

It is worth noting that only networks trained with OpenAI observations use domain randomisation to closely match the results in OpenAI dexterity work.

(d) Allegro Hand Standard Figure 15: Consecutive successes per episode for (a) Shadow Hand with OpenAI observation and LSTMs, (b) Shadow Hand with OpenAI observation and feed forward networks (c) Shadow Hand with Standard observations and (d) Allegro Hand with Standard observations. Shadow Hand Standard and Allegro Hand Standard both use feed forward networks for policy and value functions.

### Randomizations

For domain randomization we closely followed the approach proposed in and applied correlated and uncorrelated noise to observations, actions, as well as randomized cube size and all the key physics properties -- masses, inertia tensors, friction, restitution, joint limits, stiffness and damping. Full details of these are available in Appendix A.4.1.

We outline a few important differences between our setup and the one used in the OpenAI work below: While OpenAI used a success tolerance of 0.4 rad^22^2page 22, section C.1, paragraph Goals, we use both 0.4 rad and a tighter tolerance of 0.1 rad. We focus on results with 0.4 rad in this section and provide results with 0.1 tolerance in Appendix A.4.2 We use a continuous as opposed to a discrete control space used.

Our results are averaged with 5 seeds while OpenAI show results with only 1 seed^33^3page 11, section 6.3, Ablation of Randomizations, Figure 8 .

The randomizations used in our work do not include action delay and motor backlash.

We use an LSTM layer of 1024 hidden units after the input followed by an MLP layer of 512 hidden units. On the other hand OpenAI et al. used an MLP layer of size 1024 after the input followed by an LSTM layer of size 512 hidden units. We found our setting performs better with Isaac Gym.

We use a somewhat different reward function to OpenAI as shown in Appendix A.2.3.

Our experiments are only in simulation and unlike we do not attempt any sim-to-real transfer for the Shadow Hand experiment.

Figure 14(a), (b) and (c) show the reward curves for various settings we used for Shadow Hand. Shadow Hand Standard --- trained with no randomization and uses symmetric actor critic setting with a feed forward network --- is the fastest to reach a reward of 6000. This setting achieves 20 consecutive successes in under 35 minutes. Important to remember that this setting is not suitable for sim-to-real transfer as it includes some observations that may not be directly available in the real world.

We now focus on experiments with OpenAI observations and asymmetric feed-forward actor-critic. This setting is suited for sim-to-real transfer and the policy uses only the observations that are possible to obtain in the real world. As shown in Figure 15(b), we achieved more than 20 consecutive successes in less than 1 hour. In contrast, for the same performance it takes 30 hours on the OpenAI setup consisting of CPU based simulation and training setup running MuJoCo simulator on a cluster of 384 16-core CPUs with 6144 CPU cores in total and using 8 NVIDIA V100 GPUs for training. In Figure 15(a) we show that using LSTM networks, the performance increases and we can reach 37 consecutive successes in just under than 6 hours while OpenAI et al. achieve same performance in \~17 hours. Since OpenAI et al. show results only with 1 seed, comparing their result with our best seed we note that 37 consecutive successes with LSTM experiments can be achieved in just 2.5 hours. We provide the results for Shadow Hand OpenAI experiment with success tolerance of 0.1 in the Appendix A.4.

Figure 16: TriFinger reward and the corresponding success rate.

### TriFinger

The TriFinger manipulation task, originating , involves picking a cube lying on a flat surface and repositioning it to a desired 6-degrees-of-freedom pose. The manipulator has 3 fingers each with three degrees of freedom. In, it was shown that Isaac Gym training combined with Domain Randomization allows sim-to-real transfer. The environment is shown in Figure 13.

We use an asymmetric actor-critic formulation for this system as that allows to design a policy that uses input observations that are possible to obtain in the real world and therefore enable sim-to-real transfer. We show the reward and success rate in simulation in Figure 16. We also transfer results from simulation to the real world and note that our mean success rate in the real world is 55%. We refer to for more detailed analysis.

In particular, this example shows the ability of policies learned using Isaac Gym's physics to generalize to the real world. Some of the behaviours leaned by the policy are shown in the Figure 17. It is worth noting that the robot is situated in a different location and therefore the sim-to-real transfer was done remotely.

Figure 17: Trifinger learns a variety of dexterous manipulation behaviours in order to move the cube to the correct position and orientation. These results are obtained on the real TriFinger robot hosted .

### Allegro Hand

We learn cube orientation with Allegro Hand and use the same reward as for the Shadow Hand as well similar observation scheme, with the only difference --- smaller number of observations because of the different number of fingers in Allegro Hand --- that it has 4 fingers instead of 5 and fewer degrees of freedom as a result, shown in Appendix A.2.3.

Figure 14(d) shows the reward curves for Allegro Hand and Figure 15(d) shows consecutive successes achieved. Interestingly, despite having fewer degrees of freedom this hand does not achieve as high consecutive successes as Shadow hand. This is because the wrist is fixed and fingers are slightly longer. We observed in Shadow hand experiment that having a movable wrist allows for better manipulation when reorienting the cube.

## Summary

We show that Isaac Gym is a high performance and high-fidelity framework that allows blistering fast training on many challenging simulated robotic environments on a single NVIDIA A100 GPU that previously would have required large heterogeneous clusters of CPUs and GPUs using a conventional RL setup with CPU-only simulators. Moreover, the simulation backend is also suited for learning contact-rich manipulations as confirmed by our sim-to-real transfer demonstrations with ANYmal locomotion and TriFinger cube reposing.
