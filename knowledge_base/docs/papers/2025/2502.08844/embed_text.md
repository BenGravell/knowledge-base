## Introduction

Reinforcement learning (RL) with subsequent transfer to hardware (sim-to-real), is emerging as a leading paradigm in modern robotics. The benefits of simulation are obvious -- safety and cheap data. The recipe involves four steps: Create a simulated environment that matches the real world.

Encode desired robot behavior with a reward function.

Train a policy in simulation.

Deploy to the robot.

The key enabler of this approach is a simulator that is realistic, convenient, and fast.

The realism requirement is self-evident, the "digital twin" of step 1 demands a minimal level of fidelity. Convenience and usability are equally critical, streamlining the creation, modification, composition, and characterization (system identification) of simulated robots.

The importance of speed is less obvious -- why does it matter if training takes ten minutes or ten hours? The answer lies in reward design (step 2), which cannot be easily automated: what the robot *ought* to do is an expression of human preference. Even if reward design is semi-automated, the process remains iterative: RL excels at finding policies that obtain reward, but the resulting behavior is often irregular in unexpected ways. Since steps 2 and 3 (and occasionally step 4) must be repeated, *time-to-robot* becomes critical: the time from when you ask the robot to do something until you see what it thinks you meant.

RL is computationally intensive, requiring an enormous number of agent-environment interactions to train effective policies. GPU-based simulation can significantly accelerate this process for two key reasons. First, the median GPU is far more powerful than the median CPU, and while high core-count CPUs exist, they are uncommon. Second, by keeping the entire agent-environment loop on device, we can harness the high-throughput, highly parallel architecture. This is especially true for *on-policy* RL, which employs GPU-friendly, wide-batch operations. Locomotion and manipulation tasks which previously required days of training on multi-host setups, can now be solved within minutes or hours on a single GPU.

With this work, we aim to further advance and make sim-to-real robot learning even more accessible. We introduce MuJoCo Playground, a fully open-source framework for robot learning designed for rapid iteration and deployment of sim-to-real reinforcement learning policies. We build upon MuJoCo XLA (MJX), a JAX-based branch of the MuJoCo physics engine that runs on GPU, enabling training directly on device. Besides physics and learning, we leverage the open-source nature of our ecosystem to incorporate on-device rendering through the Madrona batch renderer, facilitating training of vision-based policies end-to-end, without teacher-student distillation. With a straightforward installation process (pip install playground) and cross-platform support, users can quickly train policies on a single GPU. The entire pipeline---from environment setup to policy optimization---can be executed in a single Colab notebook, with most tasks requiring only minutes of training time.

MuJoCo Playground's lightweight implementation greatly simplifies sim-to-real deployment, transforming it into an interactive process where users can quickly tweak parameters to refine robot behavior. In our experiments, we deployed both state- and vision-based policies across six robotic platforms in less than eight weeks. We hope that MuJoCo Playground becomes a valuable resource for the robotics community and expect it to continue building on MuJoCo's thriving open-source ecosystem.

Our work makes three main contributions: We develop a comprehensive suite of robotic environments using MJX, demonstrating sim-to-real transfer across diverse platforms including quadrupeds, humanoids, dexterous hands, and robot arms.

We integrate the open-source Madrona batch GPU renderer to enable end-to-end vision-based policy training on a single GPU device, achieving zero-shot transfer on manipulation tasks.

We provide a complete, reproducible training pipeline with notebooks, hyperparameters, and training curves, enabling rapid iteration between simulation and real-world deployment.

Figure 0: A preview of locomotion and manipulation environments available in MuJoCo Playground.

## Environments

MuJoCo Playground contains environments in 3 main categories: DeepMind (DM) Control Suite, Locomotion, and Manipulation, which we briefly describe in this section. Locomotion and manipulation environments are tailored to robotic use-cases and we show zero-shot sim-to-real transfer in many of the available environments. Playground directly utilizes MuJoCo Menagerie which offers a suite of robot assets and configurations tailored to run in MuJoCo.

### II-A DM Control Suite

The majority of RL environments from are re-implemented in MJX, and serve as entry-level tasks to familiarize users with MuJoCo Playground (Figure 1).

### II-B Locomotion

Locomotion environments in MuJoCo Playground are implemented for multiple quadrupeds and bipeds (Figure left). The quadrupeds include the Unitree Go1, Boston Dynamics Spot, and Google Barkour, while the humanoids include the Berkeley Humanoid, Unitree H1 and G1, Booster T1, and the Robotis OP3. For each robot embodiment, we implement a joystick environment that learns to track a velocity command consisting of base linear velocities in both the forward and lateral directions, as well as a desired yaw rate. On the Unitree Go1, we additionally implement fall recovery and handstand environments. A complete list of locomotion environments is provided in Table V in the appendix.

We demonstrate sim-to-real transfer in two main sets of experiments. First, on the Unitree Go1, we deploy joystick, fall recovery, and handstand policies. Second, we demonstrate joystick-based locomotion on the Berkeley Humanoid, the Unitree G1, and the Booster T1. More details on these sim-to-real experiments can be found in Section IV-B.

### II-C Manipulation

Manipulation environments in MuJoCo Playground are implemented for both prehensile and non-prehensile tasks (Figure right). With the Leap Hand robot, we demonstrate contact-rich dexterous re-orientation of a block. Using the Franka Emika Panda and Robotiq gripper, we show re-orientation of a yoga block using high frequency torque control. We implement a simple vision-based pick-cube environment on a Franka arm using the Madrona batch renderer. A few additional environments, such as bi-arm peg-insertion with the Aloha robot, are also available. We refer to Table VIII in the appendix for a full set of environments.

We demonstrate sim-to-real transfer on the Leap Hand and Franka arm robots, including an environment trained from vision for the pick-cube task. More details on the sim-to-real experiments are available in Section IV-C.

## Batch Rendering with Madrona

MuJoCo Playground enables vision-based environments through an integration of MJX with Madrona. Madrona is a GPU-based entity-component-system (ECS), which contains GPU implementations of high throughput rendering. Madrona provides two rendering backends: a software-based batch ray tracer written in CUDA (used for the experiments in this work) and a Vulkan-based rasterizer. The raytracing backend supports features including complex lighting scenarios, shadows, textures, and geometry materials. See Figure 2 for examples of rendered images using the batch ray tracer. Some features such as deformable materials, moving lights, and terrain height fields will be added in the future.

The Madrona Batch Renderer is integrated with MJX through low-level JAX primitives that connect to the initialization and render functions exposed by Madrona. These JAX primitives allow for Madrona to interact seamlessly with JAX transformations such as jit and vmap. Mujoco Playground provides two examples: (cartpole-balance and PandaPickCubeCartesian) to showcase the implementation of vision-based environments and training of vision-based policies.

The Madrona MJX integration also supports customization of each environment instance, allowing for domain randomization of visual properties such as geometry size, color, lighting conditions, and camera pose. These randomizations play a crucial role in the sim-to-real transfer of vision-based policies, which we discuss more in Section IV-C3.

## Results

In this section, we report RL and sim-to-real results for environments in MuJoCo Playground. Sim-to-real experiments (see some examples in Figure 3) are performed for locomotion and manipulation environments from both proprioceptive state and from vision. We briefly discuss RL training on different hardware devices and RL libraries.

### IV-A DM Control Suite

We train state-based policies for all available tasks, with most environments training in under 10 minutes on a single GPU device. More details on the training process can be found in Section A.2. All available environments in the MJX port of the DM Control Suite, including any modifications, are detailed in Section A.1.

Using the batch renderer, we also implement pixel-based observations for the CartpoleBalance environment. These observations are generated on the GPU, allowing us to keep physics, rendering, and training entirely on-device. Although other DM Control Suite environments can also be rendered with Madrona, we demonstrate end-to-end RL training on only one task, leaving a more comprehensive exploration for future work. Appendix D provides more information on how CartpoleBalance was modified and trained for pixel observations.

Figure 1: Several DM Control Suite environments.

### IV-B Locomotion

We present sim-to-real locomotion results on both a quadruped (Unitree Go1) and three humanoid platforms (Berkeley Humanoid,Unitree G1, and Booster T1). Further details on the MDP formulation, including rewards, observation spaces, and action spaces, are provided in Appendix B.

### IV-B1 Quadruped Locomotion

Figure 2: Sample renders from the Madrona batch renderer for the Panda and Aloha environments. Left-most images are the original environments. The remaining images highlight the the support for lighting, shadows, textures, and colors, including the ability to domain randomize these parameters during training.

### Task definition

We implement a joystick locomotion task as , where the command is specified by three values indicating the desired forward velocity, lateral velocity, and turning rate of the robot's root body. Additionally, we design policies for handstand and footstand tasks, in which the robot balances on the front or hind legs, respectively, while minimizing actuator torque. For fall recovery, we follow, enabling the robot to return to a stable "home" posture from arbitrary fallen configurations.

### Hardware

We deploy on the Unitree Go1, which is a quadruped robot with four legs, each possessing three degrees of freedom. Trained policies run on real-world outdoor terrain (grass and concrete) and indoor surfaces with different friction properties.

### Training

We domain randomize for sensor noise, dynamics properties and task uncertainties. We firstly train the policy in flat ground with restricted command ranges within 5 minutes (2x RTX 4090). and finetune it in rough terrain with wider ranges. See Appendix B for more detail.

### Results

All four policies (joystick, handstand, footstand, and fall recovery) transfer robustly from simulation to reality, coping with uneven terrain and moderate external perturbations without additional fine-tuning. Videos of these deployments are provided on our project website.

Figure 3: Footage from four of our deployed policies. a) Go1 joystick policy recovering from a kick while travelling at ∼ 2m/s, b) Berkeley humanoid joystick policy tracking an angular velocity command on a slippery surface. c) In-Hand Cube Reorientation transitioning between two target poses. d) Non-prehensile policy issuing torque commands to rotate a block by 180 degrees.

### IV-B2 Humanoid Locomotion

### Task definition

We implement the same joystick locomotion task as shown for the quadruped environment.

### Hardware

We perform sim-to-real experiments on three different humanoid platforms: a) Berkeley Humanoid, a low-cost, lightweight bipedal robot with 6 DoF per leg, b) Unitree G1, a humanoid robot featuring 29 DoF in total, and c) Booster T1, a small-scale humanoid robot with 23 Dof. All systems are evaluated in indoor environments, with slight variations in surface friction and ground compliance.

### Training

We follow the domain randomization and finetuning strategies of the quadruped robot. Training on flat ground lasts under 15 minutes for the Berkeley Humanoid, and under 30 minutes for the Unitree G1 and the Booster T1 on two RTX 4090.

### Results

We successfully deploy joystick-based locomotion on the Berkeley Humanoid, demonstrating robust tracking of velocity commands on surfaces ranging from rigid floors to soft and slippery terrains. On the Unitree G1 and Booster T1, our zero-shot policy similarly achieves stable walking and turning on standard indoor floors. Although minor tuning for each platform's unique dynamics may further enhance performance, these results confirm that our approach generalizes across a range of legged robot morphologies.

### IV-C Manipulation

In this section, we present sim-to-real results for a broad range of manipulation tasks, including dexterous in-hand manipulation, non-prehensile manipulation, and vision-based grasping. These tasks illustrate Playground's ability to address a diverse segment of the manipulation spectrum and highlight its robust deployment in real-world settings.

### IV-C1 In-Hand Cube Reorientation

### Task definition

We implement an in-hand cube reorientation task using the low-cost, dexterous LEAP hand platform, closely following previous works on in-hand manipulation. The task involves reorienting a 7 cm cube repeatedly from random initial poses to new target orientations in SE without dropping it. Further task details are provided in Section C.4.

### Hardware

We employ the same hardware configuration as , mounting the LEAP hand on an 80/20 frame with a 3D-printed bracket that tilts the palm downward by 20°. A single Intel RealSense D415 camera, positioned above the workspace, provides pose estimates of the cube via a pretrained detector. Although occlusions can introduce observation noise, we leave multi-camera extensions to future work. The policy operates at 20 Hz, which remains comfortably below the USB-Dynamixel control bandwidth.

### Training

To promote sim-to-real transfer, we apply domain randomization on the robot parameters as well as cube mass and friction. We also include sensor noise, and we finetune with a progressive curriculum to increase both noisy pose estimates and action regularization. The policy trains within 30 min on two RTX 4090 GPUs. Further training details are provided in Section C.4.

### Results

As summarized in Table I, our learned policy demonstrates early signs of robust in-hand reorientation with MuJoCo Playground. The most frequent failure occurs when the cube becomes wedged in the space present between the fingers and the palm of the LEAP hand, causing the policy to stall. Although less common, we also observe accidental interlocking of the index and thumb, attributed to physical flex in the low-cost hardware. Videos of real-world deployments can be found on our project page. We note that improved camera coverage and more accurate collision geometries could mitigate these edge-case failures, which we leave for future work.

## Rotations

TABLE I: In-hand reorientation results on the LEAP hand over 10 trials, reporting the number of consecutive successful rotations before failure. The final two columns show the median and mean of the #Rotations metric.

### IV-C2 Non-Prehensile Block Reorientation

### Task definition

We present a sim-to-real setup for non-prehensile reorientation of a yoga block on a commonly available Franka Emika Panda robot arm with a Robotiq gripper, achieving high zero-shot success. The task involves moving a yoga block from a random initial pose in the robot's workspace to a fixed goal pose. A trial is deemed successful if the agent reorients the block within 3 cm of the goal position and within 10° of the desired orientation.

### Hardware

The policy receives estimates of the block's position and orientation from an open-source camera tracker. We use direct high-frequency torque control at 200 Hz, where the RL policy outputs motor torques for the arm's seven joints (with the gripper closed). By learning to control torques rather than joint positions, the agent develops smooth, compliant behavior that transfers effectively to hardware, delivering superior performance even when direct torque control at high frequencies poses learning challenges. This recipe, therefore, holds broad value for practitioners.

### Training

Robust zero-shot transfer is enabled by stochastic delays and progressive curriculum learning. Each training episode injects randomization into initial poses, joint positions, and velocities, while also imposing action and observation stochastic delays to mirror practical hardware latency. A simple curriculum gradually increases the block's displacement and orientation range upon each success, preventing overfitting to easier conditions. Training takes 10 minutes on 16x A100 devices.

### Results

These techniques, combined with 200 Hz direct torque control, produce a policy resilient to real-world perturbations. The agent reliably reorients the block on hardware with no additional fine-tuning as shown in Table II. Videos of real-world deployments are provided on our project website. Additional implementation details are given in Section C.5.

Mean ± 95% Confidence Interval TABLE II: Sim-to-real reorientation performance on the Franka Emika Panda robot, evaluated across 35 hardware trials. Each metric is reported as the median and mean (with a 95% confidence interval). The success rate is bolded to highlight final task performance. The training was done on 16x A100 GPUs.

### IV-C3 Pick-Cube from Pixels

### Task definition

We demonstrate sim-to-real transfer with pixel-based policies on a Franka Emika Panda robot. The robot must reliably grasp and lift a small 2 $\times$ 2 $\times$ 3 cm block from a random location on the table and move it 10 cm above the surface. The policy receives a $64 \times 64$ RGB image as input and outputs a Cartesian command, which is processed by a closed-form inverse kinematics solution to yield joint commands. To simplify the task, we restrict the end-effector to a 2D Y-Z plane (while always pointing downward) and provide a binary jaw open/close action.

### Hardware

We use a Franka Emika Panda robot with a single Intel RealSense D435 camera mounted to capture top-down RGB images. The policy operates at 15 Hz, and we run inference on an RTX 3090 GPU. Our setup ensures that the block starts within the field of view over a 20 cm range along the y-axis.

### Training

To bridge the sim-to-real gap, we apply domain randomization across visual properties such as lighting, shadows, camera pose, and object colors. We also add random brightness post-processing, and introduce a stochastic gripping delay of up to 250 ms. We choose a reduced action dimension of three (Y-movement, Z-movement, and discrete jaw control) for training sample efficiency, but we have found that the task can also be solved in full Cartesian or joint space given additional camera perspectives and more training samples. Training in simulation takes ten minutes on a single RTX 4090.

### Results

Our policy achieves a 100% success rate in 12 real-world trials, robustly grasping the block and lifting it clear of the table. It demonstrates resilience to moderate variations in lighting and minor camera shaking, as shown in the videos on our project website. These findings highlight MuJoCo Playground's capacity for training pixel-based policies that transfer reliably to real hardware in a zero-shot manner. Additional implementation details are described in Appendix D.

### IV-D Training Throughput

Figure 4: Training wallclock time for LeapCubeReorient on different GPU device topologies. 1x 4090 takes ∼ 2080 (s) to train and 8x H100 takes ∼ 670 (s) to train. All runs use the same hyperparams (e.g. 8192 num envs); we leave tuning hyperparams per topology as a future exercise.

Across our sim-to-real studies, we used several GPU hardware setups and topologies, including NVIDIA RTX 4090, A100, and H100 GPUs. In Figure 4, we break down the training performance of the LeapCubeReorient environment on different configurations for a fixed set of RL hyper-parameters, demonstrating that MJX is effective on both consumer-grade and datacenter graphics cards. We see that GPUs with higher theoretical performance and larger topologies can reduce training time by a factor of 3x on a contact-rich task like in-hand reorientation. We leave optimization of topology-specific hyper-parameters as future work (e.g. the number of environments should ideally increase for larger topologies to maximize throughput, as long as the RL algorithm can utilize the increase in data per epoch). In Table IV, Table VII, and Table IX in the appendix, we report RL training throughput for all environments in MuJoCo Playground on a single A100 GPU.

### IV-D1 Training Throughput with Batch Rendering

Figure 5: Environment steps per second on the single-camera CartpoleBalance and PandaPickCubeCartesian environments with pixel-based observations from our on-device renderer.

Figure 5 highlights the throughput of stepping two of our environments with pixel observations at different resolutions. By pairing MJX physics with Madrona batch rendering, our Cartpole and Franka environments unroll at roughly 403,000 and 37,000 steps per second respectively. Note that our Franka physics are over 20x more costly than Cartpole's, resulting in the lower sensitivity of FPS to image resolution.

Computationally, pixel-based policy training generally involves four main components: physics simulation, observation rendering, policy inference and policy updates. Figure 5 only encapsulates the former two and is not fully indicative of overall training throughput.

We find that in the context of a PPO training loop, physics, rendering, and inference together only comprise 9% and 43% of the Cartpole and Franka total training times, respectively, with most of the time spent updating the expensive CNN-based networks. Hence, compared to traditional on-policy training pipelines, we have shifted our bottleneck from collecting data to processing it. Training bottlenecks are further discussed in Section D.3 under Table X and Table XI. Further performance benchmarking and a rough comparison against prior simulators are in Section D.2.

### IV-D2 RL Libraries

Figure 6: Reward curves for PPO trained with RSL-RL and brax on an RTX-4090 GPU for 3 seeds each on the Unitree Go1.

While MuJoCo Playground primarily uses a JAX-based physics simulator, practitioners are able to use both JAX and torch-based RL libraries for training RL agents. In Figure 6, we show reward curves for PPO agents trained using both Brax and RSL-RL implementations. Each corresponding RL library is trained with custom hyperparameters tailored to the corresponding PPO implementation. Both libraries are able to achieve successful rewards and gaits within similar wallclock times. All other results in this paper were obtained using the Brax PPO and SAC implementations.

## Related Work

### Physics simulation on GPU

The PhysX GPU implementation has been heavily relied on for robotic sim-to-real workloads via IsaacGym and more recently Isaac Lab. The PhysX GPU implementation, however, is closed-source and researchers lack the ability to extend the simulator for their specific tasks or workloads. Several GPU-based physics engines are open-source, such as MJX, Brax, Warp, and Taichi. Only a limited set of robot environments leverage these open-source counterparts, in contrast to the wide range of robotic sim-to-real results that were achieved with IsaacGym and Isaac Lab. Most recently, Genesis provides a rigid-body implementation similar to MJX implemented using Taichi, that allows for dynamic constraints/contacts. However, sim-to-real results are still limited to a few locomotion policies.

### Sim-to-real RL

A variety of locomotion and manipulation policies have successfully been deployed in the real world zero-shot. We complement these results by demonstrating zero-shot sim-to-real on the Leap Hand, Unitree Go1, Berkeley Humanoid, Unitree G1, Booster T1, and Franka arm using MuJoCo rather than closed-source simulators. Similar to, we provide code for environments and training.

### Vision-based RL

State-of-the-art algorithms such as DrQ, RL from Augmented Data (RAD), Dreamerv3, TD-MPC2, and EfficientZeroV2 have pushed pixel-based RL performance over the years. Transferring these advances to the real world is appealing, as visual control loops offer precise positioning and robust behaviour in uncontrolled in-the-wild scenarios. The limitation of training directly from pixel data is the large visual sim-to-real gap between simulation and reality, which is often overcome using domain randomization. However, such training methods require exponentially more training samples. As as result, policies are typically trained with proprioceptive observations in simulation and subsequently distilled into vision-based policies offline, or trained with smaller exteroceptive observations. With Madrona, we are able to train vision-based policies directly in simulation without a distillation step using high-throughput batch rendering, similar to and.

## Limitations

MuJoCo Playground inherits the limitations of MJX due to constraints imposed by JAX. First, just-in-time (JIT) compilation can be slow (1-3 minutes on Playground's tasks). Second, computation time related to contacts does not scale like the number of *active* contacts in the scene, but like the number of *possible* contacts in the scene. This is due to JAX's requirement of static shapes at compile time. This limitation can be overcome by using more flexible frameworks like Warp and Taichi. This upgrade is an active area of development. Finally we should note that the vision-based training using Madrona is still at an early stage.

## Conclusion

MuJoCo Playground is a library built upon the open-source MuJoCo simulator and Madrona batch renderer with implementations across several reinforcement learning and robotics environments. We demonstrate policy training on various GPU topologies using JAX and pytorch-based reinforcement learning libraries. We also demonstrate sim-to-real deployment on several robotic tasks and embodiments, from locomotion to both dexterous and non-prehensile manipulation from proprioceptive state and from pixels. We look forward to seeing the community put this resource to use in advancing robotics research and its applications.
