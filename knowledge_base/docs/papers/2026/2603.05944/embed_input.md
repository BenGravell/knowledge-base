<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How to Model Your Crazyflie Brushless

Topics include Reinforcement learning, Neural networks, Accuracy, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Crazyflie quadcopter is widely recognized as a leading platform for nano-quadcopter research. In early 2025, the Crazyflie Brushless was introduced, featuring brushless motors that provide around 50% more thrust compared to the brushed motors of its predecessor, the Crazyflie 2.1. This advancement has opened new opportunities for research in agile nano-quadcopter control. To support researchers utilizing this new platform, this work presents a dynamics model of the Crazyflie Brushless and identifies its key parameters. Through simulations and hardware analyses, we assess the accuracy of our model. We furthermore demonstrate its suitability for reinforcement learning applications by training an end-to-end neural network position controller and learning a backflip controller capable of executing two complete rotations with a vertical movement of just 1.8 meters. This showcases the model's ability to facilitate the learning of controllers and acrobatic maneuvers that successfully transfer from simulation to hardware. Utilizing this application, we investigate the impact of domain randomization on control performance, offering valuable insights into bridging the sim-to-real gap with the presented model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We have open-sourced the entire project, enabling users of the Crazyflie Brushless to swiftly implement and test their own controllers on an accurate simulation platform.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Over the past decade, Crazyflie (CF) quadcopters have become state-of-the-art in indoor nano-quadcopter research and teaching, both for single quadcopters and quadcopter swarms -. At the beginning of 2025, a new version, the Crazyflie 2.1 Brushless (CFB), was released. In contrast to the original CF 2.1 quadcopter that features brushed motors, the CFB is equipped with brushless motors and electric speed controllers (ESCs). Consequently, the CFB boasts a significantly higher thrust-to-weight ratio of around 3:1 compared to the 2:1 ratio of the CF 2.1. This increase in power positions the CFB as a valuable platform for research and teaching focused on agile control of nano-quadcopters.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To facilitate method development involving the CFB, this work derives a dynamics model of the CFB. We identify This work has been supported by the German Federal Ministry of Research, Technology and Space (BMFTR) under the Robotics Institute Germany (RIG). The authors gratefully acknowledge the computing time provided to them at the NHR Center NHR4CES at RWTH Aachen University (project number p0021919). This is funded by the Federal Ministry of Education and Research, and the state governments participating on the basis of the resolutions of the GWK for national high performance computing at universities (www.nhr-verein.de/unsere-partner).

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

1 Alexander Gr¨ afe and Sebastian Trimpe are with the Institute for Data Science in Mechanical Engineering, RWTH Aachen University, Germany alexander.graefe@dsme.rwth-aachen.de, trimpe@dsme.rwth-aachen.de 2 Christoph Scherer and Wolfgang H¨ onig are with the Intelligent Multi-Robot Coordination Lab, TU Berlin, Germany c.scherer@tu-berlin.de, hoenig@tu-berlin.de key parameters such as thrust curves and motor time constants and provide guidelines for manually re-identifying parameters like moments of inertia, which become necessary when modifications are made to the quadcopter's setup. Furthermore, to demonstrate the model's effectiveness for control design, we employ it to train two end-to-end neural network (NN) controllers entirely in simulation based on the identified model using reinforcement learning (RL). The first controller is capable of performing position control, which is comparable to the controllers embedded in the CFB's firmware. The second controller can execute up to two consecutive backflips with a vertical movement of 1. 8 m.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We use this application of our model to assess the extent of necessary domain randomization, offering valuable insights into the sim-to-real gap.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- 1) We derive a dynamics model of the CFB, including motor dynamics, and offer practical guidelines for manual parameter identification. - 2) We evaluate the model in two ways: (a) by assessing its prediction accuracy and (b) by training end-to-end NN controllers for the CFB, deploying it on real Crazyflie Brushless hardware, and using it to analyze critical choices such as domain randomization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The codebase, including the model, its parameters and a simulator based on JAX and MuJoCo XLA (MJX) for highly parallelized simulations on GPUs, is available under github.com/Data-Science-in-MechanicalEngineering/CrazyflieBrushJAX. Additionally, an accompanying video demonstrating the hardware experiments is available at tiny.cc/CFBVideo.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this work is organized as follows. First, we review related research on modeling previous versions of the CF in Sec. II and give an overview of the components of the CF Brushless in Sec. III. Next, we derive the model and identify its parameters in Sec. IV. Subsequently, we evaluate the model's predictive performance in Sec. V and conduct experiments using end-to-end RL to explore the sim-to-real gap in Sec. VI.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Crazyflie Modeling", "weight": 1.0} -->

Quadcopter dynamics are generally well understood and models feature varying levels of detail. These range from simple models that treat the quadcopter as a rigid body subject to external forces and torques to more complex models incorporating learned residual dynamics and even full fidelity fluid simulators -.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Crazyflie Modeling", "weight": 1.0} -->

For the CF 2.x, several studies have derived models all with similar levels of detail -. In these models, the CF is represented as a rigid body influenced by motor forces and reactive torques. The motor forces and torques are either modeled using static functions, or combined with a dynamic system where motor commands are processed through a first-order dynamic system to simulate motor dynamics.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Crazyflie Modeling", "weight": 1.0} -->

Building on these models, several simulators have been developed. We highlight three of the most common and recent ones: PyBullet-drones, which utilizes PyBullet to simulate multiple quadcopters for swarming simulations with vision support; CrazySim, based on Gazebo, offering software-in-the-loop simulations via CF firmware wrappers; and Crazyflow, currently under development for highly parallelized simulations of CF swarms using MJX.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Crazyflie Modeling", "weight": 1.0} -->

The presented models and simulators focus on the CF 2.x and to our knowledge, no comparable dynamics model of the new CF is openly accessible. To bridge this gap, this work introduces both a model and simulator specifically for the CFB. We maintain a similar level of detail as existing models, while basing our simulator on MJX, akin to Crazyflow.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Crazyflie Model Use Cases", "weight": 1.0} -->

Existing CF models have found extensive application in domains such as control design and multi-robot systems. For instance, Socas et al. used the model to design and evaluate periodic and event-based PID controllers, while Nguyen et al. leveraged a linearized model to develop an onboard model predictive control (MPC) for dynamic flight. For multi-robot systems, Gr¨ afe et al., evaluated a distributed MPC for swarms using PyBullet-drones and Wahba et al., used the model to design collaborative transport algorithms of cable-suspended payloads.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Crazyflie Model Use Cases", "weight": 1.0} -->

The models have also been widely adopted for RL. Applications use RL to optimize PID gains, manage swarms with high-level commands via multi-agent RL and learn end-to-end control policies,.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Crazyflie Model Use Cases", "weight": 1.0} -->

To demonstrate the capability of the CFB model proposed in this work, we use it to train an end-to-end NN controller with RL. This application serves as a test of model precision, as end-to-end learning is highly sensitive to model inaccuracies,. Furthermore, it enables an evaluation of the domain randomization required for successful sim-to-real transfer, which serves as a metric for the model's accuracy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SYSTEM MODEL", "weight": 1.0} -->

In this section, we first present the dynamics model in Sec. IV-A and then its parameters in Sec. IV-B. Finally, in Sec. IV-C, we give an overview of our simulator implementation based on MJX.

<!-- chunk {"id": "body-0019", "role": "body", "section": "First-principle model", "weight": 1.0} -->

When modeling the CFB, we preserve the same level of detail as existing models for the CF 2.x -, (cf. Sec. II-A). In Sec. V, we enumerate unmodeled effects that could become significant in research exploring the limits of CFB dynamics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "First-principle model", "weight": 1.0} -->

First, we present the comprehensive set of equations that describe the quadcopter's dynamics. Subsequently, we will examine each equation and its parameters in a step-bystep manner. Our model follows common quadcopter models presented, e.g., in works -, -. We describe the CFB using a state-space model ˙ x = f (x, u), where x ∈ R 17 is the state and u ∈ 4 × 1 are the motor commands. In detail, the model is where v ∈ R 3 is the velocity, q ∈ S 3 are the quaternions representing orientation, ω ∈ R 3 is the angular velocity in the body frame, Ω ∈ R 4 are the rotation speeds of the motors and g = 9. 81 m s -2. The coordinate system is depicted in Fig. 1 and roll, pitch and yaw rates rotate around x, y and z axes respectively. These rotations are deemed positive when counter-clockwise. All parameters can be found in Table I. We now go through the equations explaining their parts.

<!-- chunk {"id": "body-0021", "role": "body", "section": "First-principle model", "weight": 1.0} -->

Rotational and Translational Dynamics -. The translational dynamics of the quadcopter are a standard model, summing up the influence of the motor's thrust (F m, τ m). The thrust that the motors generate is a nonlinear function of the motor rotational speed where R (q) ∈ R 3 × 3 is the rotation matrix and F thrust (Ω): R 4 × 1 → R 4 × 1 is an element-wise 3rd order polynomial with units rad s -1 → N (cf. Sec. IV-B).

<!-- chunk {"id": "body-0022", "role": "body", "section": "First-principle model", "weight": 1.0} -->

The torques from the motors in pitch and roll direction are the thrusts of the motors times the orthogonal distance to the center of mass. The torque around the z-axis is the reactive torque of the motor, which is the sum of the inertia torque J m ˙ Ω and the aerodynamic/friction torques on the motor τ f where we measured the element-wise 3rd order polynomial τ f (Ω): R 4 → R 4 with dimension rad s -1 → Nm (cf. Sec. IV-B) and where ℓ is the width of the quadcopter.

<!-- chunk {"id": "body-0023", "role": "body", "section": "First-principle model", "weight": 1.0} -->

While accounting for aerodynamic forces in the model could further enhance accuracy, accurately modeling these effects is challenging. Our current results indicate that effective performance in low speed scenarios TABLE I: Symbols, explanations and dimensions for the quadcopter model.

<!-- chunk {"id": "body-0024", "role": "body", "section": "First-principle model", "weight": 1.0} -->

| Symbol | Explanation | Dimension | Fig. 2: Comparison between measured and model-predicted thrust and torque characteristics. The propeller model accurately captures both thrust and torque behavior across the operating range.

<!-- chunk {"id": "body-0025", "role": "body", "section": "First-principle model", "weight": 1.0} -->

( ≤ 3 m s -1 ) can be achieved by solely modeling the rigidbody dynamics, motor dynamics and motor response.

<!-- chunk {"id": "body-0026", "role": "body", "section": "First-principle model", "weight": 1.0} -->

Motor Dynamics. The motor dynamics model summarizes the behavior of the dynamics of the motor rotational mass, the coils and the ESCs. However, developing a model of all this proves challenging, especially given the complicated behavior of the ESC's electronic commutation, rate limitation etc. We hence approximate the dynamics via a first-order linear system with time constant T and amplification K as done.

<!-- chunk {"id": "body-0027", "role": "body", "section": "System identification", "weight": 1.0} -->

We identify the parameters of the model in three different experiments. First, we measure the motor parameters with sensors measuring the motor's revolutions per minute (RPM). Then, we measure the thrust and reactive torques F a (Ω) and F thrust (Ω) and finally identify the remaining parameters (moment of inertia matrix) by fitting measured trajectories of the quadcopter to simulated ones.

<!-- chunk {"id": "body-0028", "role": "body", "section": "System identification", "weight": 1.0} -->

Motor Dynamics Identification. We identify the motor system dynamics by recording the motor commands and the RPM during flight. While we can directly assess the motor commands in the firmware of the quadcopter, we measure the RPM using a custom deck with a QRD1114 infrared sensor and a reflective band beneath the propeller as described. We then fit the time constant T and amplification K to the measured curves leading to T = 0. 05 s and K = 2900rads -1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "System identification", "weight": 1.0} -->

Thrust Measurements. We place the quadcopter on a force/torque measurement testbed we built using a scale and a rotating arm. We increase the motor command of only one motor in steps and once it has reached a steady state, we measure the force/torque. Afterwards, we fit a polynomial through the points measured leading to with σ = 2. 9 · 10 3 for numerical stability.

<!-- chunk {"id": "body-0030", "role": "body", "section": "System identification", "weight": 1.0} -->

Fitting Measured Trajectories. All remaining parameters are measured by manually fitting simulated trajectories to measured ones (Table II). We emphasize that especially the moments of inertia are dependent on the additional payload of the quadcopter, e.g., whether equipped with propeller guards, motion capture system markers and decks. The given ones should, however, give a good starting ground to quickly identify the parameters for the CFB in a specific application using the following procedures on a flying quadcopter.

<!-- chunk {"id": "body-0031", "role": "body", "section": "System identification", "weight": 1.0} -->

For the inertias around x and y axis, the quadcopter should perform a maneuver where it rotates around its x and y axes. This can be achieved by swapping from a stabilizing controller to a policy that gives each motor different motor commands such that they create torques around the x and y axis. After a short amount of time (around 500 ms ), the quadcopter swaps back to the stabilizing controller to avoid crashing. This allows us to fit the moments of inertia around x and y axis by aligning the simulated and measured rotation rates around x and y axis, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "System identification", "weight": 1.0} -->

Similarly, for the moment of inertia around z axis and J m, we perform an experiment, where we keep the motor command of three motors low and give a high command to one, which causes the yaw rotation rate to rise fast. This yaw rotation rate can be used to fit the parameters.

<!-- chunk {"id": "body-0033", "role": "body", "section": "MJX Simulator", "weight": 1.0} -->

We implement the derived model inside MJX. Although the differential equation of the drone could also be solved using a suitable solver, MJX allows to reuse the simulator for complex tasks that involve e.g., contacts. MuJoCo itself takes care of the translational and rotational dynamics. We place the motor model outside of MuJoCo and solve it separately at each step. As the dynamics are linear, this can be done exactly. From Ω, we then calculate the thrust reactive torque of the motor and give this to the MuJoCo model as input. We simplify the dynamics of the Kalman filter, the sensor low-pass filters and the delay of communication with the motion capture system via Crazyswarm with a fixed delay of 8 ms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "EVALUATION: MODEL ACCURACY", "weight": 1.0} -->

This section evaluates the predictive capabilities of the model by comparing simulated and measured trajectories.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Method", "weight": 1.0} -->

We will evaluate the model on two different maneuvers flown by the CFB. First, a maneuver, where the CFB changes from hovering to a horizontal flight. And second, a maneuver, where we disturb the yaw orientation and let the CFB control itself back to the original position. During these maneuvers, we measure the estimated state of the CFB and its motor commands. The simulation then receives these motor commands along with the initial state and then generates the simulated trajectories. We did not use these maneuvers to fit model parameters. To also assess the effect of parameter uncertainties, we simulate the CFB 4096 times with different inertia and amplify/reduce the thrust and torque of the motors. The randomly sampled parameters deviate at maximum 2 % from the identified ones. Furthermore, we change the center of gravity by at maximum 2 mm, which can be achieved by changing the matrix L and apply velocity and angular noise per simulation step ( 4 ms ) of 0. 001 m s -1 and 0. 001 rad s -1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 3 demonstrates that our model can capture the behavior of the CFB in a horizon of 200 ms. Over time, the predictions of the model increasingly deviate from the real behavior. We also noticed larger differences between measured and simulated velocities in z-direction especially during the second maneuver.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

We suspect multiple sources for the remaining deviation of our model. First, uncertainties have an increasingly large effect over the prediction horizon. Within this context, we observed that inaccuracies in the center of gravity position exert a particularly large influence. Second, the measured values from the CFB are taken from its Kalman filter (cf. Sec. III) and might not necessarily represent the actual ground-truth values, they hence have their own errors and uncertainties. This is especially true for the velocity as there is no direct sensor for it (position, attitude and angular rates are measured by the motion capture system and the IMU). Third, our model neglects aerodynamics, particularly the complex aerodynamics of the motors, whose thrust changes during movement. Modeling these effects is non-trivial, and represents an exciting topic for future work. Fourth, during flight, we cannot measure the motor speeds and thus estimate their initial value, adding uncertainty. Other potential factors include disturbances, like subtle air movements.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 3: Comparison of hardware measurements (dotted lines) versus simulation (solid lines). The simulation incorporated 4096 quadcopters with different mass, moment of inertia and thrust/torque scalings (differing at maximum 2 % from the nominal ones). The line in the middle denotes the mean, whereas the shaded areas the minimum and maximum. We excluded position in the plots as it is almost constant.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results", "weight": 1.0} -->

To contextualize the performance of our model, we compared the PyBullet-drones model for the CF 2.1 against real flight data from a CF 2.1 (Fig. 4). The results show that the PyBullet-drones model significantly deviates from the real behavior, demonstrating that our CFB model achieves substantially higher accuracy than this established baseline.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

While the presented model captures the fundamental behavior of the CFB, some discrepancies remain. To address this, we investigate the effect of domain randomization on RL performance in the following. The required degree of domain randomization for successful sim-to-real transfer serves as an additional metric for evaluating the accuracy of the dynamics model and the uncertainties in its key parameters.

<!-- chunk {"id": "body-0041", "role": "body", "section": "EVALUATION: SIMULATION-BASED REINFORCEMENT LEARNING", "weight": 1.0} -->

The previous section assessed the model's accuracy. In this section, we demonstrate the model's suitability for learning end-to-end NN controllers by designing and evaluating a simulation-based RL pipeline. Additionally, we use this pipeline to examine the impact of domain randomization, uncertainties applied to model parameters during training, which provides insights into the sim-to-real gap. A video accompanying this section is available at tiny.cc/CFBVideo.

<!-- chunk {"id": "body-0042", "role": "body", "section": "EVALUATION: SIMULATION-BASED REINFORCEMENT LEARNING", "weight": 1.0} -->

Fig. 4: Comparison of hardware measurements (dotted lines) versus simulation (solid lines) of angular rates for the CF 2.1. We use the model parameters used in PyBullet-drones for baselines comparisons.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Method", "weight": 1.0} -->

We train quadcopters on two distinct tasks. First, we focus on training a quadcopter to fly and maintain a specified target position. Second, we design a controller specifically for executing backflips.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Method", "weight": 1.0} -->

Baselines. We compare the learned target controller with the firmware's PID and Mellinger controller using parameters provided by the firmware.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Method", "weight": 1.0} -->

Learning Algorithm. We employ proximal policy optimization (PPO) for learning, utilizing BRAX's PPO implementation and its interface to MJX allowing the entire training to run on the GPU. To assess the sim-to-real gap, no dedicated fine-tuning is performed on hardware.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Method", "weight": 1.0} -->

Controller. The controller is a fully connected NN with four hidden layers, each containing 32 neurons. Although the CFB provides estimates of position, attitude, velocity and angular rates, it cannot measure motor rotation speeds Ω. Therefore, past estimates and actions are also included in the controller's input as a state representation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Method", "weight": 1.0} -->

Reward. We use sums of triangular shaped rewards where e is a deviation from a target value (e.g. p -p target) and e max is the maximum interval on which we want to give a reward. This function helps to normalize the reward making the RL training better conditioned. We also add a large negative reward in case of a failure (e.g., crash to the ground or too high angular velocities). The next paragraphs give the exact formulation for the specific controller.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Method", "weight": 1.0} -->

Target Control. Goal of target control is to steer the quadcopter to the origin. We change the target position the quadcopter should fly to by subtracting it from the position estimate. We use the following reward function to encourage proximity to the target position while penalizing high rotation speeds, angular velocities and generated torques (to ensure smooth maneuvers) where fail is one when the quadcopter's velocity exceeds 10 m s -1 or its angular velocity ω is above 30 rad s -1. In this case, we terminate the episode.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Method", "weight": 1.0} -->

Backflips. For backflips, we use a multi-phase approach similar to. First, we use the controller from the last section to accelerate the quadcopter upwards and then switch to a second NN controller (called flip-controller in the following) that controls the quadcopter to have a constant angular rate around its x-axis and a given velocity along its local frame's z-axis. After some time, we switch back to the stabilizing controller that catches the quadcopter and steers its back towards its starting position. The possibility to vary angular rate and velocity setpoints v target, ˙ θ target and the time points on which we switch the controllers allows us to change the behavior of the drone during the backflip, generating looping of different sizes and speeds.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Method", "weight": 1.0} -->

The NN controller for the second phase is trained via the following reward where the first part rewards keeping the velocity, the second keeping the quadcopter's attitude close to its rotation axis and the third rewarding controlling it to the pitch rate.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Method", "weight": 1.0} -->

Domain Randomization. We randomized key model parameters: mass ( ± 10 % ), inertia and motor dynamics ( ± 20 % ), motor thrusts and torques scalings ( ± 20 % ) and center of gravity position ( ± 1 cm ), sampling from uniform distributions across these intervals. Additionally, we introduced random offsets in attitude measurements ( ± 15 ◦ ) to simulate real-world misalignment between the drone's local coordinate frame, the global motion capture system frame and the direction of gravity.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Method", "weight": 1.0} -->

We quantify the effect of domain randomization in Sec. VI-D by training NN controllers with varying magnitudes of randomization, defined as a factor for the interval size. A magnitude of 1.0 corresponds to the full intervals specified above, while 0.5 and 0.0 correspond to halfintervals and no randomization, respectively.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Evaluation: Target Control", "weight": 1.0} -->

Fig. 5 illustrates a maneuver executed by the CFB, flying between two positions 6 m away. The quadcopter successfully reaches its target within 2 s, achieving a maximum velocity of around 5 m s -1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation: Target Control", "weight": 1.0} -->

In Table III, we compare the learned controller for different domain randomization magnitudes with the PID and Mellinger controllers from the firmware. We conducted a hover test for 6 s, assessing mean distance to target position and motor command standard deviation to evaluate motor command smoothness.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluation: Target Control", "weight": 1.0} -->

The PID has the best positional accuracy, followed by the NN controller with domain randomization magnitude 1.0 and then the Mellinger controller. The NN controller performs slightly better in motor command smoothness.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluation: Target Control", "weight": 1.0} -->

Fig. 5: Target controller flying back and forth between two points 6 m apart. The NN controller guides the CFB to its target with an accuracy of a few cm (cf. Table III), achieving velocities of approximately 5 m s -1 during the maneuver.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluation: Target Control", "weight": 1.0} -->

Fig. 6: Performance of the position controller with respect to domain randomization. Each configuration represents a different magnitude of domain randomization trained over five random seeds to test the robustness of the trained policy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation: Target Control", "weight": 1.0} -->

These results demonstrate the RL pipeline's ability to learn a controller using our model, whose stationary behavior is comparable to the firmware's controllers. We want to note that we used the PID and Mellinger controller's standard parameters and tuning of these controllers could potentially improve their performance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluation: Backflips", "weight": 1.0} -->

Single Backflips. Fig. 7 illustrates various backflips executed by the NN controllers. The shape of each backflip varies according to the setpoint velocity and roll rate. As the CFB cannot control its velocity when inverted, the velocity is not kept exactly. However, the adjustable setpoints still allow the users to customize the backflips to their preferences.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluation: Backflips", "weight": 1.0} -->

Double Backflips. Fig. 8 depicts the trajectory of a CFB executing a backflip with two rotations. This maneuver is performed requiring only 1. 8 m movement in zdirection. The quadcopter reduces its rotational velocity from 1000 deg / s in 0. 35 s and its vertical velocity from 3. 5 m s -1 TABLE III: Comparison of the learned NN controllers for different domain randomization magnitudes (denoted in parentheses, cf. Sec. VI-A) against the PID and Mellinger controllers from the firmware. The first column is the mean differences from setpoint position measured for 5 s and the second mean of motor command standard deviations (std) over the four motors.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluation: Backflips", "weight": 1.0} -->

| Controller | Mean Distance (mm) | Motor command std | Fig. 7: Trajectory in YZ plane for four flip maneuvers. Depending on the hyperparameters of the maneuver (more specifically duration of the liftoff and roll rate), the shape changes. to zero in 0. 6 s, demonstrating the CFB's capacity for agile, high-thrust maneuvers.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluation: Backflips", "weight": 1.0} -->

In summary, RL using the presented model enables the CFB to execute high-performance aerial acrobatics.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Effect of Domain Randomization", "weight": 1.0} -->

To assess the impact of domain randomization, we trained the target controller using various randomization magnitudes. The results of these experiments are presented in Table III and Fig. 6.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Effect of Domain Randomization", "weight": 1.0} -->

Low magnitudes of domain randomization reduce positional accuracy, primarily in the z-direction. Nevertheless, even with low or no randomization, the drone maintains a level and stable flight. Conversely, excessively high domain randomization significantly degrades controller performance, as the increased demand for robustness comes at the expense of optimal performance. These findings suggest that the rotational dynamics are less sensitive to low domain randomization than the vertical dynamics. We hypothesize that this is due to slight discrepancies in mass and thrust between the model and the real quadcopter, combined with reduced controller robustness to these parameters when trained with limited randomization.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Effect of Domain Randomization", "weight": 1.0} -->

We note that the reward functions were not explicitly tuned for different randomization magnitudes. Such tuning could potentially improve performance. Alternatively, the loss of accuracy in the z-direction might be mitigated by removing mass compensation from the NN controller and instead compensating for it with a constant offset to the motor commands.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Effect of Domain Randomization", "weight": 1.0} -->

Fig. 8: Double backflip maneuver showing trajectory in YZ plane and roll angle over time.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Effect of Domain Randomization", "weight": 1.0} -->

In summary, our experiments demonstrate that the presented model is accurate enough to successfully train NN controllers in simulation that can be successfully deployed on a real CFB. To enhance robustness against model-toreal-world discrepancies, we recommend domain randomization of ± 10 % to ± 20 % for mass, inertia, motor model and thrust/torque scaling. For controllers designed primarily for attitude control, where translational dynamics are less critical, a reduced amount or even the omission of domain randomization may be sufficient.

<!-- chunk {"id": "body-0068", "role": "body", "section": "CONCLUSION AND OUTLOOK", "weight": 1.5} -->

This work derived a dynamics model of the recently released CFB, to support future research with this new version of the popular Crazyflie platform. Specifically, we identified the parameters of the dynamics model and provided procedures to quickly re-identify the inertias when payloads are added or removed. Evaluations of the model's prediction capabilities demonstrated that the model is accurate with minor discrepancies due to unmodeled effects such as aerodynamics and observer dynamics. Additionally, we demonstrated the model's effectiveness by training end-to-end NN controllers through RL that transfer from simulation to real world. Our experiments revealed that domain randomization between 10 % -20 % effectively bridges the sim-to-real gap for RL, allowing end-to-end NN controllers that generalize from simulation to real-world deployment on the CFB.

<!-- chunk {"id": "body-0069", "role": "body", "section": "CONCLUSION AND OUTLOOK", "weight": 1.5} -->

To our knowledge, this is the first openly available model of the new CFB, effective for common tasks like RL. Future work could extend this model by identifying the CFB's aerodynamics, for instance using methods like those, which is particularly relevant for high-speed applications like quadcopter racing. Another interesting direction is modeling the aerodynamic interactions between multiple CFB, as explored, to facilitate the development of highperformance swarms.
