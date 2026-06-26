## INTRODUCTION

Wheeled and legged robots have recently demonstrated remarkable dynamic capabilities, driven in large part by advances in Reinforcement Learning (RL) and motion imitation. By tracking demonstrations from motion capture, animal locomotion, or model-based controllers, robots can learn parkour and agile behaviors. However, if the original motion references are dynamically or kinematically infeasible, the imitation policy may fail to train or lead to unsafe behaviors not suitable for real-world deployment. Blindly tracking these infeasible references may exceed the robot's torque or joint limits or cause self-collisions.

Prior works have explored learning from imperfect demonstrations by reweighting trajectories according to confidence in their optimality, filtering out low-quality segments to extrapolate higher-quality behaviors, or using adversarial techniques for partial demonstrations. While effective to some extent, these approaches still treat imperfections as liabilities to be corrected offline and as a result, the final policy is still bounded by the static quality of the dataset.

In this work, we introduce Iterative Motion Imitation (IMI), an extension of motion imitation that iteratively transforms infeasible trajectories into feasible and agile behaviors. IMI begins by imitating an initial reference, which may be generated through manual control without safety constraints, trajectory optimization, or hand-crafted drawing, and is often physically infeasible. Once a policy is trained to follow this reference, its rollout is treated as a new reference for the next stage of training. Through this recursive process, imperfections in the reference are progressively removed, which allows the next policies to better satisfy safety-critical constraints. This allows us to use simple reward functions and constraints without relying on extensive reward shaping, and it enables feasible and agile behaviors.

Figure 1: UMV executing a front-flip learned via Iterative Motion Imitation.

We deploy IMI on Ultra-Mobility Vehicle (UMV), a bicycle robot equipped with a large articulated mass for acrobatic maneuvers as shown in Fig. 1. We focus on a front-flip, as its agility allows us to push the system to its mechanical limits. Beginning with an initial flip-down trajectory with simple imitation rewards, this iterative process allows the policy to generalize to scenarios beyond what the original reference was designed . We demonstrate this extended agility with ground-to-ground flips and ground-to-table flip-ups. We further confirm the robustness of the learned behaviors through hardware deployment.

To sum up, our contributions are: Iterative Motion Imitation (IMI), a method that refines imperfect references into agile policies via iterative imitation, yielding highly agile behaviors from simple tracking rewards.

Analysis of performance improvement and trajectory for both original flip stunts and adapted flip-up scenarios.

Hardware demonstration of acrobatic flip stunts on the UMV robot, validating the approach on a platform with unique dynamic stability challenges.

## RELATED WORK

### II-A Reinforcement Learning for Agile Locomotion

RL has emerged as a dominant paradigm for synthesizing policies that achieve dynamic locomotion skills beyond the reach of classical control. Recent works have enabled quadrupeds to reach record speeds, execute agile parkour, and generalize across terrains. These approaches are often "reference-free," relying solely on carefully engineered rewards. While powerful, the reliance on hand-tuned multi-term rewards can be a bottleneck, limiting scalability to diverse and extreme behaviors.

Motion imitation methods alleviate this challenge by leveraging demonstrations such as motion capture, video, or trajectory optimization. Along with publicly available motion capture datasets, motion imitation methods have accelerated the research in humanoid whole-body control. However, such datasets not only have motion artifacts, but the process of retargeting to robot morphologies also leads to artifacts, resulting in physically infeasible references.

### II-B Learning from Imperfect References

In practice, reference trajectories are rarely ideal, often suffering from noise, morphological mismatches, or dynamic infeasibility. Existing methods address this by treating imperfect demonstrations as a static dataset. For instance, trajectories may be weighted or ranked based on scores or demonstration quality. Trajectory optimization can also be used to refine the reference offline. While useful, these techniques cannot refine demonstrations through interaction, and optimization-based methods often require an accurate dynamics model. Moreover, these refinements cannot generate references that exceed the agility of the original demonstrations.

An alternative is the adversarial imitation framework, which can produce natural behaviors on real robots, even from partial demonstrations. Yet, these methods are known to be unstable during training and highly sensitive to hyperparameter tuning.

Our work departs from this perspective: rather than coping with reference imperfections, IMI recursively transforms them into feasible and robust guides for policy learning. This is done in the same framework, without re-tuning, and without designing complicated rewards.

### II-C Learning Bicycle Stunts

Bicycle control has long served as a benchmark for both model-based and learning-based robotics. Linear and nonlinear control strategies were studied on basic tasks such as balancing and target reaching. Early works on RL for bicycle control demonstrated that careful reward shaping can solve basic driving tasks.

Subsequent research has leveraged RL to push bicycle capabilities toward driving in complex environments. Hierarchical RL has been used to achieve robust path tracking and balancing on rough, unstructured terrain. Others have integrated their RL frameworks combining path planning, trajectory tracking, and balancing to navigate narrow corridors. This trend extends beyond bicycles, as demonstrated by Baltes et al., who trained a humanoid robot to steer and balance on a commercial scooter.

Beyond driving, dynamic stunts such as jumping have been studied. Learning-based methods have been successfully applied to control ramp jumps by optimizing for flight attitude and landing, while model-based approaches have provided complementary insights into the underlying physics using techniques like inverse kinematics and Bayesian optimization. Tan et al. significantly raised the bar of bicycle agility, employing neuro-evolution to successfully learn a diverse repertoire of acrobatic stunts, including bunny hops, wheelies, endos, and pivots.

While these studies showcase a range of dynamic behaviors, most of their results are confined to simulation, lacking validation on physical hardware. Our work builds on this foundation by not only tackling acrobatic flips---a maneuver of greater dynamic complexity than previously demonstrated---but also by successfully deploying the learned policy on a real-world robotic platform.

Figure 2: A 2D overview of the UMV model used in this work.

## The Ultra-Mobility Vehicle (UMV) Robot

UMV is a custom-built, two-wheeled robot with a bike base comparable in size to a children's bicycle (Fig. 2). A key feature that distinguishes the UMV from a conventional bicycle is a significant articulated mass, referred to as *boing*, mounted atop the bike-base frame.

The model of UMV used in this work consists of five joints and six links. The links are upper-body, lower-body, bike-base, fork, front-wheel, and rear-wheel. The joints are upper-body, lower-body, fork, front-wheel, and rear-wheel. UMV has four actuated joints in total. The upper-body and lower-body joints control the pitch of the upper body, and are the main joints to inject momentum to perform parkour behaviors. The fork joint controls the steering angle (yaw) of the front wheel. The rear-wheel provides driving torque. Consistent with standard bicycle design, the front wheel remains passive and unactuated.

Boing (the upper-body and lower-body links) houses the batteries and joint motors and is connected to the bike-base by two parallel revolute joints (the upper-body and lower-body joints). The axes of these joints are parallel to the wheel axles, allowing the upper-body to pitch forward and backward relative to the bike-base. This mechanism enables the robot to dramatically shift its center of mass, a critical capability for generating the angular momentum required for acrobatic maneuvers.

## METHOD

### IV-A The Iterative Motion Imitation (IMI)

Figure 3: An overview of IMI. The first iteration starts with an initial reference ξ0 used to train policy π1. Then, reference ξn − 1 generated by policy πn − 1 becomes the new more feasible reference used to train a new policy πn. This loop continues, progressively refining the motion until a high-performance, hardware-deployable policy is achieved.

The goal of IMI, depicted in Fig. 3 ‣ IV METHOD ‣ Flip Stunts on Bicycle Robots using Iterative Motion Imitation"), is to acquire robust and agile skills from an infeasible trajectory. The framework iteratively refines an initial, imperfect reference until a policy exhibiting the desired feasible behavior is achieved. This process involves three key steps Imitate: The policy is trained using constrained RL to track the current reference trajectory.

Generate: The learned policy is executed in simulation to generate a new, physically plausible trajectory.

Refine: The generated trajectory is set as the new reference for the next imitation cycle.

The kinematic reference trajectories are used exclusively during training and are progressively improved with each cycle. Experts can also manually trim the trajectory during the refine stage when the desired motion differs from the reference motion, such as adapting a flip-down trajectory to a flat-to-flat flip.

The learned policy is purely reactive, taking only proprioceptive state observations and a phase variable as input to produce joint-level PD targets, which are then tracked by a high-frequency low-level controller.

IMI enhances the two primary guidance mechanisms of motion imitation, dense tracking rewards and Reference State Initialization (RSI), by progressively improving the reference trajectory itself. This iterative refinement makes the tracking reward more informative. Initially, an infeasible reference creates a conflicting objective, forcing the policy to deviate from the reference to satisfy physical constraints. As IMI generates more plausible references, the policy can achieve high tracking fidelity while respecting these constraints. Concurrently, RSI becomes more effective. Initializing from a refined, physically achievable reference places the agent in meaningful states that are closer to high-reward regions, accelerating learning and exploration.

### IV-B Initial Reference Trajectory Generation

The initial flip reference can be generated in various ways, but we opt to use a hand-crafted model-based controller without safety constraints in simulation. The robot starts on top of a table and moves forward using a driving controller to build forward linear momentum. As the robot reaches the edge of the table, a whole-body controller is used to track a certain angular momentum that is tuned to successfully flip down the table.

This orchestrated scenario was chosen intentionally. Starting on top of a table, reaching a certain forward momentum, and tracking and tuning a whole-body controller were engineered to provide an extended flight phase, giving the robot ample time and momentum to complete a 360-degree rotation.

While this procedure yields a reference trajectory that achieves a flip, it is not executable without switching mid-air to a separate landing controller. Moreover, this does not meet our desired agility of flipping from flat ground and also violates the desired safety limits. Thus, the initial reference serves only as a rough demonstration, and our method aims to refine this imperfect reference into an end-to-end deployable policy.

### IV-C Problem Formulation

We formulate the motion imitation task as a Constrained Markov Decision Process (CMDP), defined by the tuple $(\mathcal{S},\mathcal{A},\mathcal{P},r,\mathcal{C},\gamma)$. Here, $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $\mathcal{P}(s_{t+1}|s_{t},a_{t})$ is the state transition probability, $r(s_{t},a_{t})$ is the reward function, $\mathcal{C}=\{c_{1},...,c_{k}\}$ is a set of $k$ constraint functions, and $\gamma\in[0,1)$ is the discount factor. The objective is to find an optimal policy $\pi^{*}$ that maximizes the expected discounted sum of future rewards while satisfying a set of constraints. These constraints, $c_{i}(s_{t},a_{t})~\leq~0$, represent the physical and operational limits of the robot. The full objective is: We handle the constraints by terminating the episode upon any violation as used. This strategy effectively transforms the CMDP into a standard MDP, which we solve with RL: with a positive per-step reward design, any policy that violates constraints will inherently achieve a lower expected cumulative reward. Each iteration in IMI is solved using Proximal Policy Optimization (PPO).

### IV-D Control, Observations, and Actions

We use IsaacLab as our training environment. The policy operates at 50 Hz, outputting joint PD targets. These targets are tracked by a low-level PD controller running at 200 Hz in simulation, and at 1 kHz on the real robot.

The proprioceptive observations $o_{t}\in\mathcal{S}$ are defined as where $q\in\mathbb{R}^{3}$ are the actuated joint positions, $\dot{q}\in\mathbb{R}^{4}$ are the actuated joint velocities, $\omega\in\mathbb{R}^{3}$ is the base angular velocity, $g\in\mathbb{R}^{3}$ is the projected gravity vector in the robot's base frame, and $a_{t-1}\in\mathbb{R}^{4}$ is the previous action. The observations exclude the rear wheel's position, as it is an unbounded, continuously rotating joint. The phase variable $\theta\in\mathbb{R}^{1}$ increases linearly from 0 to 1 over the duration of the reference trajectory. The total episode duration is longer than the reference trajectory, and during this extra time, $\theta$ is held at 1, requiring the policy to learn a stable balancing behavior after the touchdown.

The policy outputs a four-dimensional action vector $a_{t}~\in~\mathbb{R}^{4}$, corresponding to each joint's PD targets: Each action is scaled by its corresponding action scale. The action of the rear-wheel joint is defined as a velocity setpoint, while the actions of the upper-body, lower-body, and fork joints are defined as position setpoints. The setpoints are tracked by a PD controller with desired joint torques $\tau$ where $q_{\text{des}}$ and $\dot{q}_{\text{des}}$ are the desired position and velocity setpoints for every joint. exp (−αbase∥pbase − pbaseref∥2) exp (−αang∥dangle(qbase, qbaseref)∥2) exp (−αjoint∥qjoint − qjointref∥2) Body Joint Limits 𝕀(qjoint ∉ [qmin, qmax]) Post Tracking Terms Default Joint Positions exp (−αpd∥qbody joint∥2) TABLE I: Reward Structure with Tolerance

### IV-E Rewards

The reward is a weighted sum of tracking and penalty terms, detailed in Table I. The tracking rewards encourage the policy to follow the reference motion, and penalties discourage behaviors that are unsuitable for hardware execution. We do not track the fork and rear-wheel joint positions to grant the policy more freedom to discover strategies for balancing and momentum generation. We clip the tracking errors to certain tolerances so that the maximum reward can be achieved without the need to track the exact reference. After successfully tracking the reference (i.e., when the phase variable $\theta=1$), the *post-tracking terms* are triggered to promote a still, balanced state by rewarding a default joint posture while penalizing base velocity and joint jitter.

### IV-F Constraints and Terminations

To ensure the safe deployment of learned policies on hardware, we enforce critical physical limits as constraints. Similar to, we implement these constraints through termination conditions. Unlike approaches that use soft terminations to allow a policy to learn recovery behaviors, we employ hard terminations. This is because a constraint violation in our task represents an irrecoverable failure state. For instance, exceeding the current limit triggers a protective hardware shutdown, while an excessive touchdown velocity is an instantaneous event that can cause catastrophic hardware fracture. Based on that, an episode is terminated if any of the following conditions are met:\Touchdown Velocity: The landing vertical velocity of the wheels exceeds a certain threshold.\Mechanical Power: The total mechanical power of the joints exceeds a certain threshold $\sum\tau\dot{q}$. This serves as a proxy for the peak current limit.\Joint Position: The bounds of the joint position limits are reached. This prevents self-collisions and singularities.\Motor Torques: The motor torques exceed their torque limit.\Wheel Velocity: The wheel velocity exceeds a safety limit.\Early Termination: The robot's bike-base position or orientation deviates too much from the reference trajectory. Ground Collision: The upper-body, lower-body, or bike-base bodies collide with the ground.

To encourage early exploration during training, we introduce these hard constraints via a curriculum. The training process begins with relaxed constraint boundaries that are gradually tightened as the policy improves. This approach allows the agent to first learn the fundamental task before refining its behavior to operate within the strict physical limits, thereby preventing the learning process from stagnating.

Constraints can also be gradually introduced during different IMI iterations. For instance, we only enforce the joint position limits at the first iteration, leaving other constraints to be tightened in future iterations. For further iterations, the joint position limits were enforced from the beginning of training, and the rest of the terminations are applied as a curriculum.

### IV-G Sim2Real and Policy Training

Reference State Initialization. We use RSI to expose the policy to critical states early in training. 50% of the episodes begin from an initial state and the remaining 50% are initialized at random states sampled from the reference trajectory. We also ignore the last 10% of the data during touchdown.

Figure 4: Overlayed screenshots of UMV performing a front flip.

Domain Randomization. To bridge the sim-to-real gap, we apply domain randomization to various physical and system parameters during all stages of IMI. Specifically, we randomize physical properties such as mass, friction, and motor strength, as well as control-related parameters including actuator gains and actuation delay. We also introduce observation noise to joint positions, velocities, angular velocity, and projected gravity, and further apply external disturbances to the body velocity.

Furthermore, to handle varied contact scenarios such as premature ground impact, we add terrain randomization. In 50% of training episodes, we introduce a step obstacle with a height uniformly sampled from the range \[0 m, 0.2 m\]. Collectively, these randomizations encourage the policy to learn behaviors that are robust to modeling errors and unmodeled dynamics.

Network Architecture. The actor and critic networks are implemented as Multi-Layer Perceptrons (MLPs) with ELU activation functions and three hidden layers of size and, respectively. In addition to the actor's observations, the critic observes the bike-base's linear velocity and global position as privileged information during training. The policies are trained for 15,000 iterations.

## Results

Figure 5: Comparison of training from scratch (ξ0) versus using refined reference (ξ1). Each run uses 3 seeds. The solid line is the mean and the shaded area is the standard deviation.

We evaluate IMI through simulations and experiments on UMV, and show that it can transform an initially infeasible reference trajectory into a robust policy that transfers to the real world as shown in Fig. 4. We first detail the importance of iterative imitation on the sim-to-real transfer of our front-flip policy. Then, we conduct an ablation study to analyze the effect of iterative refinement, showing its ability to adapt to a harder maneuver such as a front-flip onto a table.

### V-A Refinement of Flip Trajectories

Figure 6: The evolution of trajectories ξ over two iterations. The time is aligned at the peak height (t = 0) and the interval is ±0.5 s around that peak. (a) bike-base X-Z position, (b) lower-body and upper-body joint angles, (c) bike-base vertical velocity, and (d) bike-base vertical acceleration.

We train IMI with two iterations. The first iteration trains a policy $\pi_{1}$ with the initial trajectory generated by the model-based controller (i.e., $\xi_{0}$). The second iteration trains a policy $\pi_{2}$ with the trajectory generated from the first iteration (i.e., $\xi_{1}$). Using the policy from the second iteration $\pi_{2}$, we generate a third trajectory for comparison (i.e., $\xi_{2}$).

Since the initial reference $\xi_{0}$ starts with the robot on a table, we translated the base pose so that the robot is initialized on the ground. For all references in the iteration, we trim the trajectory from the moment the robot acquires forward velocity until ground touchdown.

Fig. 6 illustrates the evolution of these trajectories $\xi$. The initial trajectory $\xi_{0}$ exhibits undesired behavior after the peak height: as shown in Fig. 6(b), the robot reaches its joint limits, leading to a self-collision. The landing is also unregulated, with the horizontal impact velocity and acceleration ( Fig. 6(c,d)) being the largest among the three iterations.

In contrast, $\xi_{2}$ demonstrates improved landing characteristics over $\xi_{1}$. Its peak horizontal velocity and acceleration at touchdown are reduced (Fig. 6(c,d)), leading to a smoother and less damaging impact.

Figure 7: Three hardware flip experiments of UMV. The time is aligned at the peak height (t = 0) and the interval is ±0.5 s around that peak. (a) bike-base X-Z position, (b) lower-body and upper-body joint angles, (c) bike-base vertical velocity, and (d) bike-base vertical acceleration. The vertical dashed line indicates the time at take-off.

### V-B Hardware Experiments

We deployed policy $\pi_{2}$ on two different UMV s. Figure 4 shows the hardware experiment from one robot, and Fig. 7 shows the outcome of three different runs on another.

The robot successfully performed multiple front flips on multiple different hardware, demonstrating the policy's robustness and the effectiveness of our methodology. From Fig. 7(c,d), we observe that this agile maneuver is completed within 0.8 s of flight time, achieving a full 360-degree rotation while providing sufficient time to prepare for a controlled smooth landing with low vertical velocity and acceleration. From Fig. 7(b), we observe that the robot extends its joints before take-off, tucks its boing to gain angular momentum and untucks again for smooth landing, and then transitions to the default joint positions, all without reaching any joint limits.

### V-C Ablation: Iterative vs. Single-Shot Imitation

Here, we compare two settings: IMI, which iteratively refines motion imitation sequences, against a single-iteration motion imitation baseline. To do so, we train two different policies with identical settings except that the first policy is trained with the initial reference $\xi_{0}$ while the second policy is trained with the reference from the previous IMI iteration $\xi_{1}$. In other words, we compare training from a refined reference trajectory $\xi_{1}$ against a baseline trained using an initial reference trajectory $\xi_{0}$.

Figure 5 summarizes the comparison between the two settings, averaged over three runs with different seeds. Fig. 5(a) shows the success rate, where success is defined as episodes that end in time-outs. Fig. 5(b,c) reports the number of environments (out of 4096) terminated at each step due to body joint limit and motor torque violations, respectively. Fig. 5(d) shows terminations caused by touchdown velocity limit. Sudden drops in the success rate are moments when the termination curriculum was enforced.

Based on Fig. 5, with IMI, the training converges substantially faster compared to the training from the initial reference. Furthermore, IMI achieved a success rate of 93 %, whereas training from the initial reference reaches only 49 %. The most prominent cause of failure was due to joint limits (Fig. 5(b)). For a successful flip maneuver, the robot needs to tuck its boing as close to its limit as possible to achieve maximum angular velocity. Then, it needs to quickly untuck to prepare for a smooth landing. Doing this complicated maneuver in a limited flight time is prone to joint position and motor torque violations without rich reference guidance. The refined trajectory $\xi_{1}$ already anticipates the need to open its body in preparation for a safe landing compared to $\xi_{0}$, where smooth landing was not taken into consideration. Another prominent cause of failure was due to touch down velocity (Fig. 5(c)), which occurs due to limited time for extending posture for smooth landing.

### V-D Task Adaptation: Flip Up a Box

Figure 8: Overlay of UMV flipping up a 70 cm box.

Figure 9: Flipping up 70 cm (ξ2, 70′) and 26 cm (ξ2, 26′) boxes, each learned by imitating the reference trajectory ξ1. (a) bike-base trajectory in the global frame, with the shaded region indicating the table position. (b) bike-base vertical trajectory aligned at peak height.

To showcase IMI's effectiveness beyond safety-focused refinement, we task the robot to do a harder maneuver of flipping up a box. Starting from the refined reference of $\xi_{1}$, we train a separate policy $\pi_{2}^{\prime}$ with a modified terrain. This training includes a 70 cm (as shown in Fig. 8) or a 26 cm box in front of the robot. As shown in Fig. 8, the robot was able to successfully perform a flip-up stunt over a 70 cm box using IMI. Figure 9 (a,b) shows how the robot deviates from its reference depending on the task difficulty.

TABLE II: Flip-up performance from ξ0, ξ1, and ξ2.

For quantitative analysis, we perform a third IMI iteration, where the policy is trained to execute a flip-up by imitating a trajectory generated from the second-iteration of a ground-to-ground flip $\xi_{2}$. As shown in the first row of Table II, this three-iteration process enhances flip-up performance in terms of both success rate measured from the start and average return. Furthermore, the 70 cm flip-up stunt could not be achieved by directly imitating the initial reference $\xi_{0}$ (i.e., non-iterative motion imitation), which lacks sufficient angular momentum and height clearance.

## Limitations and Future Work

While successfully demonstrating robust flipping maneuvers, we acknowledge several limitations of IMI. The iterative refinement process relies on human judgment to decide when to initiate additional iterations. The operator qualitatively assesses the simulated trajectory's performance and feasibility, and if the outcome is unsatisfactory, a new iteration is triggered. Furthermore, the learned policy is specialized to a single skill. While robust within that skill, the resulting controller cannot perform other acrobatic maneuvers without training a separate policy, requiring the re-iteration of the process to guide to a different direction.

These limitations suggest promising directions for future work. To reduce reliance on human assessment, one could design automated stopping criteria that detect when the performance improvements plateau (e.g., landing stability or energy efficiency). Moreover, an ambitious extension would be to replace the discrete iteration loop with a continuous refinement process, potentially leveraging Reinforcement Learning from Human Feedback (RLHF) to incorporate the operator's preferences in a more structured and scalable manner. To generalize beyond a single skill, we plan to extend IMI to learn command-conditioned policies that learn from a library of refined skills, as well as investigate ways to automatically generate initial reference trajectories from high-level task objectives.

## Conclusion

In this paper, we introduced Iterative Motion Imitation (IMI), a reinforcement learning framework that learns agile and physically robust robotic behaviors by iteratively refining an imperfect initial reference. We demonstrated that by iteratively imitating trajectories generated by its own predecessor policies, IMI effectively transforms a dynamically infeasible motion into a high-performance policy that respects hardware limits. Our key insight is that this recursive process naturally amplifies the effectiveness of standard motion imitation techniques such as Reference State Initialization (RSI) and reward shaping, enabling robust learning without complex reward engineering.

We validated our approach on the UMV, a bicycle robot. The IMI-trained policy successfully executed unassisted front flips on hardware, marking the first demonstration of such acrobatic stunts on this platform.
