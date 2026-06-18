<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

QuadSwarm: A Modular Multi-Quadrotor Simulator for Deep Reinforcement Learning with Direct Thrust Control

Topics include Reinforcement learning, Robotics, Aerial robotics, Robustness, Control, Learning, QuadSwarm, Simulation samples per second, SPS.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning (RL) has shown promise in creating robust policies for robotics tasks. However, contemporary RL algorithms are data-hungry, often requiring billions of environment transitions to train successful policies. This necessitates the use of fast and highly-parallelizable simulators. In addition to speed, such simulators need to model the physics of the robots and their interaction with the environment to a level acceptable for transferring policies learned in simulation to reality. We present QuadSwarm, a fast, reliable simulator for research in single and multi-robot RL for quadrotors that addresses both issues. QuadSwarm, with fast forward-dynamics propagation decoupled from rendering, is designed to be highly parallelizable such that throughput scales linearly with additional compute. It provides multiple components tailored toward multi-robot RL, including diverse training scenarios, and provides domain randomization to facilitate the development and sim2real transfer of multi-quadrotor control policies. Initial experiments suggest that QuadSwarm achieves over 48,500 simulation samples per second (SPS) on a single quadrotor and over 62,000 SPS on eight quadrotors on a 16-core CPU. The code can be found in

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Deep reinforcement learning (RL) has shown promise in developing agile control policies for quadrotors. However, RL algorithms require a large number of environment transitions to train successful policies in simulation. This motivates building fast and highly-parallelizable simulators. Additionally, it is important for the simulator to be good enough that policies trained on it transfer to the real world in spite of unmodeled environment dynamics and the simplified physics assumptions it will inevitably entail.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We describe a simulator, QuadSwarm, to facilitate research in single and multi-robot RL for quadrotors that addresses the aforementioned issues. Specifically, QuadSwarm supports five main ingredients required to enable the development of RL control policies for real quadrotors: $(i)$ A reasonably accurate physics model of a popular existing hardware platform, Crazyflie 2.x, and sufficient domain randomization to account for unmodeled effects; $({ii})$ Supports per-rotor thrust control; $({iii})$ Fast single-threaded throughput, highly parallelizable, and scales with additional compute; $({iv})$ A diverse collection of learning scenarios for single and multi-quadrotor teams; $(v)$ 100$\%$ written in Python, which simplifies further development and experimentation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We evaluate the speed of QuadSwarm on a machine with AMD Ryzen 7 2700X CPU (16 CPU cores). QuadSwarm achieves $>$`<!-- -->`{=html}48,500 simulation samples per second (SPS) in an environment with a single quadrotor and $>$`<!-- -->`{=html}62,000 SPS in an environment with eight quadrotors, enabling collision simulation. In the environment with eight quadrotors, QuadSwarm receives eight samples per simulation step, which speeds up simulation even though additional computation is required for collision. We have demonstrated zero-shot transferability of RL control policies onto real hardware utilizing QuadSwarm in a single and multi-quadrotor scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "II-A1 AirSim and Air Learning", "weight": 1.0} -->

AirSim is a photo-realistic simulator for multiple vehicles, such as cars or quadrotors. However, there are three main limitations of using AirSim in RL research. First, AirSim's physics simulation is coupled with rendering, which limits its simulation speed and parallelization ability. Second, although AirSim supports multiple quadrotors, the physical simulation of collisions is overly simplified. This makes AirSim unsuitable for control tasks. Third, AirSim does not provide OpenAI Gym interface for multiple quadrotors. Air Learning, based on AirSim, focuses on system-level design to address the challenges of training RL policies and deploying them to resource-constrained quadrotors. Air Learning makes AirSim a better fit for learning by addressing several limitations of AirSim, such as using an environment generator to increase the generalization ability of trained policies. However, Air Learning still inherits the three main limitations of AirSim, mentioned above. Different from QuadSwarm, AirSim and Air Learning do not support direct per-rotor thrust control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A2 GymFC", "weight": 1.0} -->

GymFC focuses on tuning flight controllers and developing neuro-flight controllers via RL and supports per-rotor thrust control. While well-suited for developing and tuning single-robot controllers, there is very little support for multi-robot control policies and a lack of a diverse set of training scenarios for multi-robot teams.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A3 Flightmare", "weight": 1.0} -->

Flightmare balances simulation speed, photo-realism, and physical accuracy. It supports a large multi-modal sensor suite and supports two control modes: collective thrust and body rates, and per-rotor thrust. However, Flightmare does not directly support multi-robot RL.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Open-source Simulators that Support Multi-robot RL", "weight": 1.0} -->

To the best of our knowledge, gym-pybullet-drones is the only multi-drone simulator besides QuadSwarm that facilitates Deep RL research and development of multi-quadrotor teams. Compared with gym-pybullet-drones, QuadSwarm has three main features that gym-pybullet-drones does not have. First, QuadSwarm implements diverse training scenarios and provides a unified reward function for these scenarios, which increases the generalization ability of trained policies. Second, in multi-robot environments, QuadSwarm uses interaction-related rewards, such as the reward when two quadrotors collide with each other. The interaction-related rewards can provide extra information, besides post-collision dynamics, to quadrotors to learn collision avoidance behaviors. Third, QuadSwarm simulates non-ideal motors and sensor noise to decrease the sim2real gap.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Open-source Simulators that Support Multi-robot RL", "weight": 1.0} -->

Besides, in a multi-robot environment with $N$ quadrotors, QuadSwarm uses the relative position and the relative velocity of a fixed number $K$ of nearest robots to represent the neighbor information, where $K \ll N$ when N is large, such as 128, while gym-pybullet-drones uses a boolean distance adjacency matrix $A \in {\mathbb{R}}^{N \times N}$. Compared with policies trained in gym-pybullet-drones, policies trained in QuadSwarm are thus more easily scalable to larger teams.

<!-- chunk {"id": "body-0011", "role": "body", "section": "QuadSwarm", "weight": 1.0} -->

QuadSwarm is a modular quadrotor simulator that supports multiple quadrotors. Figure 2 shows six portable and easy-to-modify modules of the simulator.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Quadrotor Dynamics", "weight": 1.0} -->

where $\overset{¨}{x}$ is linear acceleration, $g$ is the gravity vector, $\mathbf{R}$ is the rotation matrix, $f$ is the total thrust force in the body frame, $m$ is the mass, ${\mathbf{ω}}_{\times}$ is the skew matrix of the $\omega$, $\mathbf{I}$ is the inertia matrix, $\tau$ is the total torque, $\tau_{p}$ is the torque along z-axis, $\tau_{th}$ is the torque produced by motor trusts.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Quadrotor Dynamics", "weight": 1.0} -->

The action of quadrotor $i$ is $a_{i} \in {\mathbb{R}}^{4}$, which represents the normalized thrust provided by each motor. Following, QuadSwarm models several aspects of real hardware in order to prevent policies from overfitting to the simulator and to facilitate sim2real transfer.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A1 Motor Lag", "weight": 1.0} -->

At timestep $t$, given actions $a^{(t)}$ from a policy sampled from an unconstrained Gaussian distribution, we constrain the actions to be in the range and use this to construct the normalized rotor angular velocity ${\hat{u}}^{(t)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A2 Motor Noise", "weight": 1.0} -->

At each timestep, we sample noise from a Gaussian distribution and apply it to the motor noise value produced on the previous timestep such that $\epsilon_{f}^{(t)} = {{\alpha_{nd}\epsilon_{f}^{({t - 1})}} + {\alpha_{ns}\mathcal{N}{}}}$, where $\epsilon_{f}^{(t)}$ is the motor noise at timestep $t$, $\alpha_{nd}$ is the decay ratio of the motor noise, $\alpha_{ns}$ is the scale factor for the motor noise, and $\mathcal{N}{}$ denotes the Gaussian distribution with zero mean and unit variance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Collision Simulation and Aerodynamics", "weight": 1.0} -->

Modeling accurate collisions is important for learning robust collision-avoidance policies but is a non-trivial task. In this section, we outline simple collision models used by default in QuadSwarm that is implemented in a modular way and can easily be swapped with a different collision model. Although these models are simple we demonstrated they are good enough to train successful policies.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B1 Quadrotor to Quadrotor", "weight": 1.0} -->

When two quadrotors collide, instead of modeling complex interactions, such as whether the propellers of two quadrotors touch, we implement a simple collision model based on the linear velocity and the angular velocity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B1 Quadrotor to Quadrotor", "weight": 1.0} -->

Where $x_{1},x_{2}$ are the positions of two quadrotors, $v_{1},v_{2}$ are the linear velocity of two quadrotors, $\alpha_{1},\alpha_{2}$ are the linear velocity decay factor of two quadrotors, $\epsilon_{v1},\epsilon_{v2}$ are the linear velocity noise of two quadrotors, and $\epsilon_{\omega 1},\epsilon_{\omega 2}$ are the angular velocity noise of two quadrotors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B2 Quadrotor to Wall or Ceiling", "weight": 1.0} -->

The collision model between a quadrotor and walls or ceiling is the same as the quadrotor-quadrotor collision model, except that the collision updates are only applied to the quadrotor.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B3 Quadrotor to Ground", "weight": 1.0} -->

We consider two situations of quadrotor interaction with the ground. When the quadrotor hits the ground we set the linear velocity, angular velocity, and acceleration to zero, regenerate the rotation matrix by setting the normal vector of the quadrotor upward, and reset all momenta. When the quadrotor is on the floor, and the thrust is not enough to allow the quadrotor to take off, we arrest motion on the floor with sufficiently high friction. When the linear velocity of the quadrotor is $0$, the friction direction is opposite to the thrust force direction in the $xy$ plane, and the final force function is: $f_{xy}\leftarrow{\max{({f_{xy} - {\mu{({{mg} - f_{z}})}}},0)}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B3 Quadrotor to Ground", "weight": 1.0} -->

When the linear velocity is bigger than $0$, the friction direction is opposite to the velocity direction in the $xy$ plane, and the final force function is: $f_{xy}\leftarrow{f_{xy} - {\mu{({{mg} - f_{z}})}}}$. In functions above, $f_{xy}$ is the thrust force in the $xy$ plane, $f_{z}$ is the thrust force in $z$ axis, $\mu$ is the friction coefficient, and $g$ is the gravity constant.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B4 Downwash", "weight": 1.0} -->

Our downwash model is a simplified version of the model proposed. We only model downwash effects when two quadrotors overlap in the $xy$ plane and within a pre-defined distance along the $z$ axis.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B4 Downwash", "weight": 1.0} -->

Where $\delta_{pos}$ is the relative distance between quadrotors, $\overset{˙}{\omega}$ is the change rate of angular velocity, which is used to simulate the aerodynamic disturbances, and ${k1},{k2},{b1}$ are constants, $\epsilon_{d},\epsilon_{\omega d}$ are Gaussian noise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Observations", "weight": 1.0} -->

where $\delta_{xi}$ represents the relative position between the quadrotor $i$ and its goal, $\overset{\sim}{x_{i⁢1}},\overset{\sim}{v_{i⁢1}}$ represent the relative position and relative velocity to the closest quadrotor, $\overset{\sim}{x_{i⁢K}},\overset{\sim}{v_{i⁢K}}$ represent the relative position and relative velocity to the Kth closest quadrotor. K is a hyperparameter. In the single quadrotor environment, $K$ is set to 0.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Observations", "weight": 1.0} -->

where $U$ represents the uniform distribution, $\mathcal{N}$ represents the Gaussian distribution, $\epsilon_{x}$ is the position noise, $\epsilon_{v}$ is the linear velocity noise, $\epsilon_{\omega}$ is the angular velocity noise.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Training Scenarios", "weight": 1.0} -->

To design diverse training scenarios, we use the quadrotor team's goals to construct several geometric formations, including a circle, grid, sphere, cylinder, and cube. We use this pool of geometric formations to design three groups of training scenarios.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D1 Static formations", "weight": 1.0} -->

Uniformly sample a geometric formation from the pool and randomly place it in the room.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D2 Dynamic formations", "weight": 1.0} -->

Change the positions and/or the geometric formation of goals after a random period of time within an episode.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D2 Dynamic formations", "weight": 1.0} -->

Dynamic goals: regenerate the positions and the geometric formation of goals after a random period of time.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D2 Dynamic formations", "weight": 1.0} -->

Swap goals: keep the geometric formation but shuffle the positions of goals after a random period of time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D2 Dynamic formations", "weight": 1.0} -->

Shrink $\&$ Expand: keep the geometric formation of goals, but change the formation size over time.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D2 Dynamic formations", "weight": 1.0} -->

Swarm-vs-Swarm: split quadrotors into two groups, and fix the formation center of each group. After a random period of time, resample the formation shape and swap the goals of the two groups.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D3 Evader Pursuit", "weight": 1.0} -->

Quadrotor(s) pursue one moving goal. We parameterize the trajectories in two ways - using a 3D Lissajous curve, and randomly sampled consecutive points connected by Bezier splines, respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Reward Components", "weight": 1.0} -->

We provide diverse reward components in the simulator. There are two groups of reward components. One is based on the quadrotor's state, and the other is based on the interactions with other objects. All $\alpha$ below are constants.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Reward Components", "weight": 1.0} -->

where reward components based on the distance to the goal, linear velocity, the normal vector in the z-axis, angular velocity, actions, change of actions, rotation, and yaw.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Reward Components", "weight": 1.0} -->

Interaction with Other Objects: We use a weighted combination of indicator functions for the conditions when the quadrotor hits the floor, stays on the floor, hits a wall, hits the ceiling, or hits other quadrotors. We also use a weighted combination of the relative distance between quadrotors for the condition when quadrotors are close to each other.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-F Reinforcement Learning Library Interface", "weight": 1.0} -->

We integrate Sample Factory, a fast RL library, with QuadSwarm to decrease the wall-clock training time. Sample Factory supports synchronous and asynchronous modes of policy proximal optimization (PPO) algorithms. For multi-agent RL, it currently supports Independent PPO.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulation Speed", "weight": 1.0} -->

To balance speed, readability, and flexibility, we decide to: $(i)$ use Python to implement the minimum requirements of physics simulation and rendering, $({ii})$ use Numba, a just-in-time compiler that is able to translate Python and NumPy code into machine code to speed up physics simulations, and $({iii})$ decouple rendering from physics simulations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulation Speed", "weight": 1.0} -->

We evaluate simulation speed on a machine with AMD Ryzen 7 2700X CPU (16 CPU cores). To fairly compare QuadSwarm with gym-pybullet-drones, we set both simulators with 100 Hz control frequency, 200 Hz simulation frequency, and 15 seconds episode duration time. In an environment with multiple quadrotors, each quadrotor has the same observation space, thus QuadSwarm receives multiple samples per simulation step.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulation Speed", "weight": 1.0} -->

Fig. 3 shows the simulation speed comparison between gym-pybullet-drones and QuadSwarm. In a single quadrotor setting, QuadSwarm approaches 48,589 SPS - $\sim$`<!-- -->`{=html}2.2x faster than gym-pybullet-drones. With multiple quadrotors and collision simulation, QuadSwarm approaches the fastest simulation speed, 62,042 SPS, when the number of quadrotors is eight - $\sim$`<!-- -->`{=html}2.0x faster than gym-pybullet-drones.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Examples", "weight": 1.0} -->

We used QuadSwarm as the main simulation platform in two projects that demonstrated the transfer of learned control policies on single and multiple quadrotors. For a single quadrotor, we show how to learn a policy to stabilize multiple different quadrotors with domain randomization. For multiple quadrotors, we show how to learn a policy to control up to 128 quadrotors to approach their goals while avoiding collisions in diverse scenarios.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We describe QuadSwarm, a simulator for Deep RL research on single and multi-quadrotor control policies and their sim2real transfer to real hardware. We demonstrate how QuadSwarm integrates five key ingredients: $(i)$ a reasonable physics model of Crazyflie 2.x, with domain randomization to account for unmodeled effects; $({ii})$ per-rotor thrust control; $({iii})$ fast, high parallelization, and scaling with additional compute; $({iv})$ a diverse collection of learning scenarios for single and multi-quadrotor teams; $(v)$ 100$\%$ written in Python. Our experiments suggest that QuadSwarm can be used to create robust quadrotor policies that successfully deploy to real hardware and that it is a useful and promising tool that will accelerate research in robust single and multi-quadrotor control policies for agile flight. We are working on extending QuadSwarm to support multiple obstacles, providing more accurate aerodynamic effects, and integrating with additional Deep RL libraries, such as PyMARL2.
