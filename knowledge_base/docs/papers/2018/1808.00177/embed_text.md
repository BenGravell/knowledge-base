<!-- arxiv-full-text:v1 {"arxiv_id": "1808.00177", "source": "ar5iv"} -->

## Introduction

Figure 2: System Overview. (a) We use a large distribution of simulations with randomized parameters and appearances to collect data for both the control policy and vision-based pose estimator. (b) The control policy receives observed robot states and rewards from the distributed simulations and learns to map observations to actions using a recurrent neural network and reinforcement learning. (c) The vision based pose estimator renders scenes collected from the distributed simulations and learns to predict the pose of the object from images using a convolutional neural network (CNN), trained separately from the control policy. (d) To transfer to the real world, we predict the object pose from 3 real camera feeds with the CNN, measure the robot fingertip locations using a 3D motion capture system, and give both of these to the control policy to produce an action for the robot.

While dexterous manipulation of objects is a fundamental everyday task for humans, it is still challenging for autonomous robots. Modern-day robots are typically designed for specific tasks in constrained settings and are largely unable to utilize complex end-effectors. In contrast, people are able to perform a wide range of dexterous manipulation tasks in a diverse set of environments, making the human hand a grounded source of inspiration for research into robotic manipulation.

The Shadow Dexterous Hand is an example of a robotic hand designed for human-level dexterity; it has five fingers with a total of $24$ degrees of freedom. The hand has been commercially available since 2005; however it still has not seen widespread adoption, which can be attributed to the daunting difficulty of controlling systems of such complexity. The state-of-the-art in controlling five-fingered hands is severely limited. Some prior methods have shown promising in-hand manipulation results in simulation but do not attempt to transfer to a real world robot. Conversely, due to the difficulty in modeling such complex systems, there has also been work in approaches that only train on a physical robot. However, because physical trials are so slow and costly to run, the learned behaviors are very limited.

In this work, we demonstrate methods to train control policies that perform in-hand manipulation and deploy them on a physical robot. The resulting policy exhibits unprecedented levels of dexterity and naturally discovers grasp types found in humans, such as the tripod, prismatic, and tip pinch grasps, and displays contact-rich, dynamic behaviours such as finger gaiting, multi-finger coordination, the controlled use of gravity, and coordinated application of translational and torsional forces to the object. Our policy can also use vision to sense an object's pose --- an important aspect for robots that should ultimately work outside of a controlled lab setting.

Despite training entirely in a simulator which substantially differs from the real world, we obtain control policies which perform well on the physical robot. We attribute our transfer results to extensive randomizations and added effects in the simulated environment alongside calibration, memory augmented control polices which admit the possibility to learn adaptive behaviour and implicit system identification on the fly, and training at large scale with distributed reinforcement learning. An overview of our approach is depicted in Figure 2.

The paper is structured as follows. Section 2 gives a system overview, describes the proposed task in more detail, and shows the hardware setup. Section 3 describes observations for the control policy, environment randomizations, and additional effects added to the simulator that make transfer possible. Section 4 outlines the control policy training procedure and the distributed RL system. Section 5 describes the vision model architecture and training procedure. Finally, Section 6 describes both qualitative and quantitative results from deploying the control policy and vision model on a physical robot.

## Task and System Overview

Figure 3: (left) The "cage" which houses the robot hand, 16 PhaseSpace tracking cameras, and 3 Basler RGB cameras. (right) A rendering of the simulated environment.

In this work we consider the problem of in-hand object reorientation. We place the object under consideration onto the palm of a humanoid robot hand. The goal is to reorient the object to a desired target configuration in-hand. As soon as the current goal is (approximately) achieved, a new goal is provided until the object is eventually dropped. We use two different objects, a block and an octagonal prism. Figure 3 depicts our physical system as well as our simulated environment.

### Hardware

We use the Shadow Dexterous Hand, which is a humanoid robotic hand with $24$ degrees of freedom (DoF) actuated by $20$ pairs of agonist--antagonist tendons. We use a PhaseSpace motion capture system to track the Cartesian position of all five finger tips. For the object pose, we have two setups: One that uses PhaseSpace markers to track the object and one that uses three Basler RGB cameras for vision-based pose estimation. This is because our goal is to eventually have a system that works outside of a lab environment, and vision-based systems are better equipped to handle the real world. We do not use the touch sensors embedded in the hand and only use joint sensing for implementing low-level relative position control. We update the targets of the low level controller, which runs at roughly $1\ {kHz}$, with relative positions given by the control policy at roughly $12\ {Hz}$.

More details on our hardware setup are available in Appendix B.

### Simulation

We simulate the physical system with the MuJoCo physics engine, and we use Unity^11^1Unity game engine website: to render the images for training the vision based pose estimator. Our model of the Shadow Dexterous Hand is based on the one used in the OpenAI Gym robotics environments but has been improved to match the physical system more closely through calibration (see Appendix C.3 for details).

Despite our calibration efforts, the simulation is still a rough approximation of the physical setup. For example, our model directly applies torque to joints instead of tendon-based actuation and uses rigid body contact models instead of deformable body contact models. Modeling these and other effects seen in the real world is difficult or impossible in a rigid body simulator. These differences cause a \"reality gap\" and make it unlikely for a policy trained in a simulation with these inaccuracies to transfer well.

We describe additional details of our simulation in Appendix C.1.

## Transferable Simulations

As described in the previous section, our simulation is a coarse approximation of the real world. We therefore face a dilemma: we cannot train on the physical robot because deep reinforcement learning algorithms require millions of samples; conversely, training only in simulation results in policies that do no transfer well due to the gap between the simulated and real environments. To overcome the reality gap, we modify the basic version of our simulation to a *distribution over many simulations* that foster transfer. By carefully selecting the sensing modalities and by randomizing most aspects of our simulated environment we are able to train policies that are less likely to overfit to a specific simulated environment and more likely to transfer successfully to the physical robot.

### Observations

We give the control policy observations of the fingertips using PhaseSpace markers and the object pose either from PhaseSpace markers or the vision based pose estimator. Although the Shadow Dexterous Hand contains a broad array of built-in sensors, we specifically avoided providing these as observations to the policy because they are subject to state-dependent noise that would have been difficult to model in the simulator. For example, the fingertip tactile sensor measures the pressure of a fluid stored in a balloon inside the fingertip, which correlates with the force applied to the fingertip but also with a number of confounding variables, including atmospheric pressure, temperature, and the shape of the contact and intersection geometry. Although it is straightforward to determine the existence of contacts in the simulator, it would be difficult to model the distribution of sensor values. Similar considerations apply to the joint angles measured by Hall effect sensors, which are used by the low-level controllers but not provided to the policy due to their tendency to be noisy and hard to calibrate.

### Randomizations

Following previous work on *domain randomization*, we randomize most of the aspects of the simulated environment in order to learn both a policy and a vision model that generalizes to reality. We briefly detail the types of randomizations below, and Appendix C.2 contains a more detailed discussion of the more involved randomizations and provides hyperparameters.

### Observation noise

To better mimic the kind of noise we expect to experience in reality, we add Gaussian noise to policy observations. In particular, we apply a correlated noise which is sampled once per episode as well as an uncorrelated noise sampled at every timestep.

### Physics randomizations

Physical parameters like friction are randomized at the beginning of every episode and held fixed. Many parameters are centered on values found during model calibration in an effort to make the simulation distribution match reality more closely. Table 1 lists all physics parameters that are randomized.

Scaling factor range Additive term range object and robot link masses surface friction coefficients robot joint damping coefficients actuator force gains (P term) gravity vector (each coordinate) Table 1: Ranges of physics parameter randomizations.

### Unmodeled effects

The physical robot experiences many effects that are not modeled by our simulation. To account for imperfect actuation, we use a simple model of motor backlash and introduce action delays and action noise before applying them in simulation. Our motion capture setup sometimes loses track of a marker temporarily, which we model by freezing the position of a simulated marker with low probability for a short period of time in simulation. We also simulate marker occlusion by freezing its simulated position whenever it is close to another marker or the object. To handle additional unmodeled dynamics, we apply small random forces to the object. Details on the concrete implementation are available in Appendix C.2.

### Visual appearance randomizations

We randomize the following aspects of the rendered scene: camera positions and intrinsics, lighting conditions, the pose of the hand and object, and the materials and textures for all objects in the scene. Figure 4 depicts some examples of these randomized environments. Details on the randomized properties and their ranges are available in Appendix C.2.

Figure 4: Simulations with different randomized visual appearances. Rows correspond to the renderings from the same camera, and columns correspond to renderings from 3 separate cameras which are simultaneously fed into the neural network.

## Learning Control Policies From State

### Policy Architecture

Many of the randomizations we employ persist across an episode, and thus it should be possible for a memory augmented policy to identify properties of the current environment and adapt its own behavior accordingly. For instance, initial steps of interaction with the environment can reveal the weight of the object or how fast the index finger can move. We therefore represent the policy as a recurrent neural network with memory, namely an LSTM with an additional hidden layer with ReLU activations inserted between inputs and the LSTM.

The policy is trained with Proximal Policy Optimiztion (PPO). We provide background on reinforcement learning and PPO in greater detail in Appendix A. PPO requires the training of two networks --- a policy network, which maps observations to actions, and a value network, which predicts the discounted sum of future rewards starting from a given state. Both networks have the same architecture but have independent parameters. Since the value network is only used during training, we use an Asymmetric Actor-Critic approach. Asymmetric Actor-Critic exploits the fact that the value network can have access to information that is not available on the real robot system.^22^2This includes noiseless observation and additional observations like joint angles and angular velocities, which we cannot sense reliably but which are readily available in simulation during training. This potentially simplifies the problem of learning good value estimates since less information needs to be inferred. The list of inputs fed to both networks can be found in Table 2.

×333We accidentally did not include the current object orientation in the policy observations but found that it makes little difference since this information is indirectly available through the relative target orientation. relative target orientation hand joints angles hand joints velocities object angular velocity Table 2: Observations of the policy and value networks, respectively.

### Actions and Rewards

Policy actions correspond to desired joints angles relative to the current ones^44^4The reason for using *relative* targets is that it is hard to precisely measure absolute joints angles on the physical robot. See Appendix B for more details. (e.g. rotate this joint by $10$ degrees). While PPO can handle both continuous and discrete action spaces, we noticed that discrete action spaces work much better. This may be because a discrete probability distribution is more expressive than a multivariate Gaussian or because discretization of actions makes learning a good advantage function potentially simpler. We discretize each action coordinate into $11$ bins.

The reward given at timestep $t$ is $r_{t} = {d_{t} - d_{t + 1}}$, where $d_{t}$ and $d_{t + 1}$ are the rotation angles between the desired and current object orientations before and after the transition, respectively. We give an additional reward of $5$ whenever a goal is achieved and a reward of $- 20$ (a penalty) whenever the object is dropped. More information about the simulation environment can be found in Appendix C.1.

### Distributed Training with Rapid

We use the same distributed implementation of PPO that was used to train OpenAI Five without any modifications. Overall, we found that PPO scales up easily and requires little hyperparameter tuning. The architecture of our distributed training system is depicted in Figure 5.

Figure 5: Our distributed training infrastructure in Rapid. Individual threads are depicted as blue squares. Worker machines randomly connect to a Redis server from which they pull new policy parameters and to which they send new experience. The optimizer machine has one MPI process for each GPU, each of which gets a dedicated Redis server. Each process has a Puller thread which pulls down new experience from Redis into a buffer. Each process also has a Stager thread which samples minibatches from the buffer and stages them on the GPU. Finally, each Optimizer thread uses a GPU to optimize over a minibatch after which gradients are accumulated across threads and new parameters are sent to the Redis servers.

In our implementation, a pool of $384$ worker machines, each with $16$ CPU cores, generate experience by rolling out the current version of the policy in a sample from distribution of randomized simulations. Workers download the newest policy parameters from the optimizer at the beginning of every epoch, generate training episodes, and send the generated episodes back to the optimizer. The communication between the optimizer and workers is implemented using the Redis in-memory data store. We use multiple Redis instances for load-balancing, and workers are assigned to an instance randomly. This setup allows us to generate about $2$ years of simulated experience per hour.

The optimization is performed on a single machine with $8$ GPUs. The optimizer threads pull down generated experience from Redis and then stage it to their respective GPU's memory for processing. After computing gradients locally, they are averaged across all threads using MPI, which we then use to update the network parameters.

The hyperparameters that we used can be found in Appendix D.1.

## State Estimation from Vision

The policy that we describe in the previous section takes the object's position as input and requires a motion capture system for tracking the object on the physical robot. This is undesirable because tracking objects with such a system is only feasible in a lab setting where markers can be placed on each object. Since our ultimate goal is to build robots for the real world that can interact with arbitrary objects, sensing them using vision is an important building block. In this work, we therefore wish to infer the object's pose from vision alone. Similar to the policy, we train this estimator only on synthetic data coming from the simulator.

### Model Architecture

To resolve ambiguities and to increase robustness, we use three RGB cameras mounted with differing viewpoints of the scene. The recorded images are passed through a convolutional neural network, which is depicted in Figure 6. The network predicts both the position and the orientation of the object. During execution of the control policy on the physical robot, we feed the pose estimator's prediction into the policy, which in turn produces the next action.

Figure 6: Vision network architecture. Camera images are passed through a convolutional feature stack that consists of two convolutional layers, max-pooling, 4 ResNet blocks, and spatial softmax (SSM) layers with shared weights between the feature stacks for each camera. The resulting representations are flattened, concatenated, and fed to a fully connected network. All layers use ReLU activation function. Linear outputs from the last layer form the estimates of the position and orientation of the object.

### Training

We run the trained policy in the simulator until we gather one million states. We then train the vision network by minimizing the mean squared error between the normalized prediction and the ground-truth with minibatch gradient descent. For each minibatch, we render the images with randomized appearance before feeding them to the network. Moreover, we augment the data by modifying the object pose. We use 2 GPUs for rendering and 1 GPU for running the network and training.

Additional training details are available in Appendix D.2 and randomization details are in Appendix C.2.

## Results

In this section, we evaluate the proposed system. We start by deploying the system on the physical robot, and evaluating its performance on in-hand manipulation of a block and an octagonal prism. We then focus on individual aspects of our system: We conduct an ablation study of the importance of randomizations and policies with memory capabilities in order to successfully transfer. Next, we consider the sample complexity of our proposed method. Finally, we investigate the performance of the proposed vision pose estimator and show that using only synthetic images is sufficient to achieve good performance.

### Qualitative Results

During deployment on the robot as well as in simulation, we notice that our policies naturally exhibit many of the grasps found in humans (see Figure 7). Furthermore, the policy also naturally discovers many strategies for dexterous in-hand manipulation described by the robotics community such as finger pivoting, finger gaiting, multi-finger coordination, the controlled use of gravity, and coordinated application of translational and torsional forces to the object. It is important to note that we did not incentivize this directly: we do not use any human demonstrations and do not encode any prior into the reward function.

For precision grasps, our policy tends to use the little finger instead of the index or middle finger. This may be because the little finger of the Shadow Dexterous Hand has an extra degree of freedom compared to the index, middle and ring fingers, making it more dexterous. In humans the index and middle finger are typically more dexterous. This means that our system can rediscover grasps found in humans, but adapt them to better fit the limitations and abilities of its own body.

Figure 7: Different grasp types learned by our policy. From top left to bottom right: Tip Pinch grasp, Palmar Pinch grasp, Tripod grasp, Quadpod grasp, 5-Finger Precision grasp, and a Power grasp. Classified according to.

We observe another interesting parallel between humans and our policy in finger pivoting, which is a strategy in which an object is held between two fingers and rotate around this axis. It was found that young children have not yet fully developed their motor skills and therefore tend to rotate objects using the proximal or middle phalanges of a finger. Only later in their lives do they switch to primarily using the distal phalanx, which is the dominant strategy found in adults. It is interesting that our policy also typically relies on the distal phalanx for finger pivoting.

During experiments on the physical robot we noticed that the most common failure mode was dropping the object while rotating the wrist pitch joint down. Moreover, the vertical joint was the most common source of robot breakages, probably because it handles the biggest load. Given these difficulties, we also trained a policy with the wrist pitch joint locked.^55^5We had trouble training in this environment from scratch, so we fine-tuned a policy trained in the original environment instead. We noticed that not only does this policy transfer better to the physical robot but it also seems to handle the object much more deliberately with many of the above grasps emerging frequently in this setting. Other failure modes that we observed were dropping the object shortly after the start of a trial (which may be explained by incorrectly identifying some aspect of the environment) and getting stuck because the edge of an object got caught in a screw hole (which we do not model).

We encourage the reader to watch the accompanying video to get a better sense of the learned behaviors.^66^6Real-time video of $50$ successful consecutive rotations:

### Quantitative Results

In this section we evaluate our results quantitatively. To do so, we measure the number of *consecutive* successful rotations until the object is either dropped, a goal has not been achieved within 80 seconds, or until $50$ rotations are achieved. All results are available in Table 3.

Individual trials (sorted) Block (state, locked wrist) Octagonal prism (state) Block (state, locked wrist) Octagonal prism (state) Table 3: The number of successful consecutive rotations in simulation and on the physical robot. All policies were trained on environments with all randomizations enabled. We performed 100 trials in simulation and 10 trails per policy on the physical robot. Each trial terminates when the object is dropped, 50 rotations are achieved or a timeout is reached. For physical trials, results were taken at different times on the physical robot.

Our results allow us to directly compare the performance of each task in simulation and on the real robot. For instance, manipulating a block in simulation achieves a median of $50$ successes while the median on the physical setup is $13$. This is the overall trend that we observe: Even though randomizations and calibration narrow the reality gap, it still exists and performance on the real system is worse than in simulation. We discuss the importance of individual randomizations in greater detail in Section 6.3.

When using vision for pose estimation, we achieve slightly worse results both in simulation and on the real robot. This is because even in simulation, our model has to perform transfer because it was only trained on images rendered with Unity but we use MuJoCo rendering for evaluation in simulation (thus making this a sim-to-sim transfer problem). On the real robot, our vision model does slightly worse compared to pose estimation with PhaseSpace. However, the difference is surprisingly small, suggesting that training the vision model only in simulation is enough to achieve good performance on the real robot. For vision pose estimation we found that it helps to use a white background and to wipe the object with a tack cloth between trials to remove detritus from the robot hand.

We also evaluate the performance on a second type of object, an octagonal prism. To do so, we finetuned a trained block rotation control policy to the same randomized distribution of environments but with the octagonal prism as the target object instead of the block. Even though our randomizations were all originally designed for the block, we were able to learn successful policies that transfer. Compared to the block, however, there is still a performance gap both in simulation and on the real robot. This suggests that further tuning is necessary and that the introduction of additional randomization could improve transfer to the physical system.

We also briefly experimented with a sphere but failed to achieve more than a few rotations in a row, perhaps because we did not randomize any MuJoCo parameters related to rolling behavior or because rolling objects are much more sensitive to unmodeled imperfections in the hand such as screw holes. It would also be interesting to train a unified policy that can handle multiple objects, but we leave this for future work.

Obtaining the results in Table 3 proved to be challenging due to robot breakages during experiments. Repairing the robot takes time and often changes some aspects of the system, which is why the results were obtained at different times. In general, we found that problems with hardware breakage were one of the key challenges we had to overcome in this work.

### Ablation of Randomizations

Figure 8: Performance when training in environments with groups of randomizations held out. All runs show exponential moving averaged performance and 90% confidence interval over a moving window of the RL agent in the environment it was trained. We see that training is faster in environments that are easier, e.g. no randomizations and no unmodeled effects. We only show one seed per experiment; however, in general we have noticed almost no instability in training.

In Section 3.2 we detail a list of parameters we randomize and effects we add that are not already modeled in the simulator. In this section we show that these additions to the simulator are vital for transfer. We train 5 separate RL policies in environments with various randomizations held out: all randomizations (baseline), no observation noise, no unmodeled effects, no physics randomizations, and no randomizations (basic simulator, i.e. no domain randomization).

Adding randomizations or effects to the simulation does not come without cost; in Figure 8 we show the training performance in simulation for each environment plotted over wall-clock time. Policies trained in environments with a more difficult set of randomizations, e.g. all randomizations and no observation noise, converge much slower and therefore require more compute and simulated experience to train . However, when deploying these policies on the real robot we find that training with randomizations is critical for transfer. Table 4 summarizes our results. Specifically, we find that training with all randomizations leads to a median of $13$ consecutive goals achieved, while policies trained with no randomizations, no physics randomizations, and no unmodeled effects achieve only median of $0$, $2$, and $2$ consecutive goals, respectively.

Individual trials (sorted) All randomizations (state) No observation noise (state) No physics randomizations (state) No unmodeled effects (state) All randomizations (vision) No observation noise (vision) Table 4: The number of successful consecutive rotations on the physical robot of 5 policies trained separately in environments with different randomizations held out. The first 5 rows use PhaseSpace for object pose estimation and were run on the same robot at the same time. Trials for each row were interleaved in case the state of the robot changed during the trials. The last two rows were measured at a different time from the first 5 and used the vision model to estimate the object pose.

When holding out *observation noise* randomizations, the performance gap is less clear than for the other randomization groups. We believe that is because our motion capture system has very little noise. However, we still include this randomization because it is important when the vision and control policies are composed. In this case, the pose estimate of the object is much more noisy, and, therefore, training with observation noise should be more important. The results in Table 4 suggest that this is indeed the case, with a drop from median performance of $11.5$ to $3.5$ if the observation noise randomizations are withheld.

The vast majority of training time is spent making the policy robust to different physical dynamics. Learning to rotate an object in simulation without randomizations requires about 3 years of simulated experience, while achieving the same performance in a fully randomized simulation requires about 100 years of experience. This corresponds to a wall-clock time of around 1.5 hours and 50 hours in our simulation setup, respectively.

### Effect of Memory in Policies

We find that using memory is helpful to achieve good performance in the randomized simulation. In Figure 9 we show the simulation performance of three different RL architectures: the baseline which has a LSTM policy and value function, a feed forward (FF) policy and a LSTM value function, and both a FF policy and FF value function. We include results for a FF policy with LSTM value function because it was plausible that having a more expressive value function would accelerate training, allowing the policy to act robustly without memory once it converged. However, we see that the baseline outperforms both variants, indicating that it is beneficial to have some amount of memory in the actual policy.

Moreover, we found out that LSTM state is predictive of the environment randomizations. In particular, we discovered that the LSTM hidden state after 5 seconds of simulated interaction with the block allows to predict whether the block is bigger or smaller than average in $80\%$ of cases.

Figure 9: Performance when comparing LSTM and feed forward (FF) policy and value function networks. We train on an environment with all randomizations enabled. All runs show exponential moving averaged performance and 90% confidence interval over a moving window for a single seed. We find that using recurrence in both the policy and value function helps to achieve good performance in simulation.

To investigate the importance of memory-augmented policies for transfer, we evaluate the same three network architectures as described above on the physical robot. Table 5 summarizes the results. Our results show that having a policy with access to memory yields a higher median of successful rotations, suggesting that the policy may use memory to adapt to the current environment.^77^7When training in an environment with no randomizations, the FF and LSTM policy converge to the same performance in the same amount of time. This shows that a FF policy has the capacity and observations to solve the non-randomized task but cannot solve it reliably with all randomizations, plausibly because it cannot adapt to the environment. Qualitatively we also find that FF policies often get stuck and then run out of time.

Individual trials (sorted) LSTM policy / LSTM value (state) FF policy / LSTM value (state) FF policy / FF value (state) Table 5: The number of successful consecutive rotations on the physical robot of 3 policies with different network architectures trained on an environment with all randomizations. Results for each row were collected at different times on the physical robot.

### Sample Complexity & Scale

In Figure 10 we show results when varying the number of CPU cores and GPUs used in training, where we keep the batch size per GPU fixed such that overall batch size is directly proportional to number of GPUs. Because we could linearly slow down training by simply using less CPU machines and having the GPUs wait longer for data, it is more informative to vary the batch size. We see that our default setup with an 8 GPU optimizer and 6144 rollout CPU cores reaches 20 consecutive achieved goals approximately 5.5 times faster than a setup with a 1 GPU optimizer and 768 rollout cores. Furthermore, when using 16 GPUs we reach 40 consecutive achieved goals roughly 1.8 times faster than when using the default 8 GPU setup. Scaling up further results in diminishing returns, but it seems that scaling up to 16 GPUs and 12288 CPU cores gives close to linear speedup.

Figure 10: We show performance in simulation when varying the amount of compute used during training versus wall clock training time (left) and years of experience consumed (right). Batch size used is proportional to the number of GPUs used, such that time per optimization step should remain constant apart from slow downs due to gradient syncing across optimizer machines.

### Vision Performance

In Table 3 we show that we can combine a vision-based pose estimator and the control policy to successfully transfer to the real robot without embedding sensors in the target object. To better understand why this is possible, we evaluate the precision of the pose estimator on both synthetic and real data. Evaluating the system in simulation is easy because we can generate the necessary data and have access to the precise object's pose to compare against. In contrast, real images had to be collected by running a state-based policy on our robot platform. We use PhaseSpace to estimate the object's pose, which is therefore subject to errors. The resulting collected test set consists of $992$ real samples.^88^8A sample contains 3 images of the same scene. We removed a few samples that had no object in them after it being dropped. For simulation, we use test sets rendered using Unity and MuJoCo. The MuJoCo renderer was not used during training, thus the evaluation can be also considered as an instance of sim-to-sim transfer. Table 6 summarizes our results.

Rendered images (Unity) Rendered images (MuJoCo) Table 6: Performance of a vision based pose estimator on synthetic and real data.

Our results show that the model achieves low error for both rotation and position prediction when tested on synthetic data.^99^9For comparison, PhaseSpace is rated for a position accuracy of around $20$ $\mu$m but requires markers and a complex setup. On the images rendered with MuJoCo, there is only a slight increase in error, suggesting successful sim-to-sim transfer. The error further increases on the real data, which is due to the gap between simulation and reality but also because the ground truth is more challenging to obtain due to noise, occlusions, imperfect marker placement, and delayed sensor readings. Despite that the prediction error is bigger than the observation noise used during policy training (Table 7), the vision-based policy performs well on the physical robot (Table 3).

## Related Work

In order to make it easier to understand the state-of-the-art in dexterous in-hand manipulation we gathered a representative set of videos from related work, and created a playlist^1010^10Related work playlist: out of them.

### Dexterous Manipulation

Dexterous manipulation has been an active area of research for decades. Many different approaches and strategies have been proposed over the years. This includes rolling, sliding, finger gaiting, finger tracking, pushing, and re-grasping. For some hand types, strategies like pivoting, tilting, tumbling, tapping, two-point manipulation, and two-palm manipulation are also options. These approaches use planning and therefore require exact models of both the hand and object. After computing a trajectory, the plan is typically executed open-loop, thus making these methods prone to failure if the model is not accurate.^1111^11Some methods use iterative re-planning to partially mitigate this issue.

Other approaches take a closed-loop approach to dexterous manipulation and incorporate sensor feedback during execution, e.g. tactile sensing. While those approaches allow to correct for mistakes at runtime, they still require reasonable models of the robot kinematics and dynamics, which can be challenging to obtain for under-actuated hands with many degrees of freedom.

Deep reinforcement learning has also been used successfully to learn complex manipulation skills on physical robots. Guided policy search learns simple local policies directly on the robot and distills them into a global policy represented by a neural network. An alternative is to use many physical robots simultaneously in order to be able to collect sufficient experience.

### Dexterous In-Hand Manipulation

Since a very large body of past work on dexterous manipulation exists, we limit the more detailed discussion to setups that are most closely related to our work on dexterous in-hand manipulation.

Mordatch et al. and Bai et al. propose methods to generate trajectories for complex and dynamic in-hand manipulation, but results are limited to simulation. There has also been significant progress in learning complex in-hand dexterous manipulation and even tool use using deep reinforcement learning but those approaches were only evaluated in simulation as well.

In contrast, multiple authors learn policies for dexterous in-hand manipulation directly on the robot. Hoof et al. learn in-hand manipulation for a simple 3-fingered gripper whereas Kumar et al. and Falco et al. learn such policies for more complex humanoid hands. While learning directly on the robot means that modeling the system is not an issue, it also means that learning has to be performed with only a handful of trials. This is only possible when learning very simple (e.g. linear or local) policies that, in turn, do not exhibit sophisticated behaviors.

### Sim to Real Transfer

*Domain adaption* methods, progressive nets, and learning inverse dynamics models were all proposed to help with sim to real transfer. All of these methods assume access to real data. An alternative approach is to make the policy itself more adaptive during training in simulation using *domain randomization*. Domain randomization was used to transfer object pose estimators and vision policies for fly drones. This idea has also been extended to dynamics randomization to learn a robust policy that transfers to similar environments but with different dynamics. Domain randomization was also used to plan robust grasps and to transfer learned locomotion and grasping policies for relatively simple robots. Pinto et al. propose to use *adversarial training* to obtain more robust policies and show that it also helps with transfer to physical robots.

## Conclusion

In this work, we demonstrate that in-hand manipulation skills learned with RL in a simulator can achieve an unprecedented level of dexterity on a physical five-fingered hand. This is possible due to extensive randomizations of the simulator, large-scale distributed training infrastructure, policies with memory, and a choice of sensing modalities which can be modelled in the simulator. Our results demonstrate that, contrary to a common belief, contemporary deep RL algorithms can be applied to solving complex real-world robotics problems which are beyond the reach of existing non-learning-based approaches.
