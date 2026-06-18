<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Universal Manipulation Interface: In-The-Wild Robot Teaching without In-The-Wild Robots

Topics include Robotics, Learning, Interface, Universal, Manipulation, UMI.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Universal Manipulation Interface (UMI) - a data collection and policy learning framework that allows direct skill transfer from in-the-wild human demonstrations to deployable robot policies. UMI employs hand-held grippers coupled with careful interface design to enable portable, low-cost, and information-rich data collection for challenging bimanual and dynamic manipulation demonstrations. To facilitate deployable policy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation. The resulting learned policies are hardware-agnostic and deployable across multiple robot platforms. Equipped with these features, UMI framework unlocks new robot manipulation capabilities, allowing zero-shot generalizable dynamic, bimanual, precise, and long-horizon behaviors, by only changing the training data for each task. We demonstrate UMI's versatility and efficacy with comprehensive real-world experiments, where policies learned via UMI zero-shot generalize to novel environments and objects when trained on diverse human demonstrations. UMI's hardware and software system is open-sourced at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

How should we demonstrate complex manipulation skills for robots to learn from? Attempts in the field have approached this question primarily from two directions: collecting targeted in-the-lab robot datasets via teleoperation or leveraging unstructured in-the-wild human videos. Unfortunately, neither is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment gap to robots.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, using sensorized hand-held grippers as a data collection interface has emerged as a promising middle-ground alternative -- simultaneously minimizing the embodiment gap while remaining intuitive and flexible. Despite their potential, these approaches still struggle to balance action diversity with transferability. While users can theoretically collect any actions with these hand-held devices, much of that data can not be transferred to an effective robot policy. As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping or quasi-static pick-and-place, lacking action diversity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

What prevents action transfer in previous work?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Insufficient visual context: While using a wrist-mounted camera is key for aligning the observation space and enhancing device portability, it restricts the scene's visual coverage. The camera's proximity to the manipulated object often results in heavy occlusions, providing insufficient visual context for action planning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Action imprecision: Most hand-held devices rely on monocular structure-from-motion (SfM) to recover robot actions. However, such methods often struggle to recover precise global action due to scale ambiguity, motion blur, or insufficient texture, which significantly restrict the precision of tasks for which the system can be employed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Latency discrepancies: During hand-held data collection, observation and action recording occur without latency. However, during inference, various latency sources, including sensor, inference, and execution latencies, arise within the system. Policies unaware of these latency discrepancies will encounter out-of-distribution input and in turn, generate out-of-sync actions. This issue is especially salient for fast and dynamic actions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Insufficient policy representation: Prior works often use simple policy representations (e.g., MLPs) with action regression loss, limiting their capacity to capture complex multimodal action distributions inherent in human data. Consequently, even with precisely recovered demonstrated actions and all discrepancies removed, the resulting policy could still struggle to fit the data accurately. This further hampers large-scale, distributed human data collection, as more demonstrators increase action multimodality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, we aim to identify the right physical interface for human demonstration that is intuitive and meanwhile able to capture all the information necessary for policy learning. Specifically, we use a Fisheye lens to increase the field of view and visual context, and add side mirrors on the gripper to provide implicit stereo observation. When combined with the GoPro's built-in IMU sensor, we can enable robust tracking under fast motion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we explore the right policy interface (i.e., observation and action representations) that could make the policy hardware-agnostic and thereby enable effective skill transfer. Concretely, we employ inference-time latency matching to handle different sensor observation and execution latency, use relative trajectory as action representation to remove the need for precise global action, and finally, apply Diffusion Policy to model multimodal action distributions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The final system, Universal Manipulation Interface (UMI), provides a practical and accessible framework to unlock new robot manipulation skills, allowing us to demonstrate any actions in any environment while maintaining high transferability from human demonstration to robot policy.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

With just a wrist-mounted camera on the hand-held gripper, we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only changing the training data for each task. Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable $70\%$ success rate in out-of-distribution tests, a level of generalizabilty seldomly observed in other behavior cloning frameworks. We open-source the hardware and software system at

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

A key enabler for any data-driven robotics system is the data itself. Here, we review a few typical data collection workflows in the context of robotic manipulation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Teleoperated Robot Data", "weight": 1.0} -->

Imitation learning learns policies from expert demonstrations. Behavior cloning (BC), utilizing teleoperated robot demonstrations, stands out for its direct transferability. However, teleoperating real robots for data collection poses significant challenges. Previous approaches utilized interfaces such as 3D spacemouse, VR or AR controllers, smartphones, and haptic devices for teleoperation. These methods are either very expensive or hard to use due to high latency and lack of user intuitiveness. While recent advancements in leader-follower (i.e. puppetting) devices such as ALOHA and GELLO offer promise with intuitive and low-cost interfaces, their reliance on real robots during data collection limits the type and number of environments the system can gain access to for "in-the-wild" data acquisition. Exoskeletons remove the dependence on real robots during data collection, however, require fine-tuning using teleoperated real robot data for deployment. Moreover, the resulting data and policy from aforementioned devices are embodiment-specific, preventing reusage for different robots.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Teleoperated Robot Data", "weight": 1.0} -->

In contrast, UMI eliminates the need for physical robots during data collection and offers a more portable interface for in-the-wild robot teaching, providing data and policies that are transferable to different robot embodiments (e.g., 6DoF or 7DoF robot arms).

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Visual Demonstrations from Human Video", "weight": 1.0} -->

There's a distinct line of work dedicated to policy learning from in-the-wild video data (e.g. YouTube videos). The most common way is to learn from diverse passive human demonstration videos. Utilizing passive human demonstrations, previous works learn task cost functions, affordance functions, dense object descriptors, action correspondences, and pre-trained visual representations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Visual Demonstrations from Human Video", "weight": 1.0} -->

However, this approach encounters three major challenges. Firstly, most video demonstrations lack explicit action information, crucial for learning generalizable policies. To infer action data from passive human video, previous works resort to hand pose detectors, or combining human videos with in-domain teleoperated robot data to predict actions. Second, the evident embodiment gap between humans and robots hinders action transfer. Efforts to bridge the gap include learning human-to-robot action mapping with hand pose retargetting or extracting embodiment-agnostic keypoints. Despite these attempts, the inherent embodiment differences still complicate policy transfer from human video to physical robots. Thirdly, the inherent observation gap induced by the embodiment gap in this line of work introduces inevitable mismatch between train/inference time observation data, exacerbating the transferability of the resulting policies, despite efforts in aligning demonstration observation with robot observation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Visual Demonstrations from Human Video", "weight": 1.0} -->

In contrast, data collected with UMI exhibit minimal embodiment gap both in action and observation spaces, enabled by precise manipulation action extraction via robust visual-inertial camera tracking and the shared Fisheye wrist-mounted cameras during teaching and testing. Consequently, this enables in-the-wild zero-shot policy transfer for dynamic, bimanual, precise, and long-horizon manipulation tasks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Hand-Held Grippers for Quasi-static Actions", "weight": 1.0} -->

Hand-held grippers minimize observation embodiment gaps in manipulation data collection, offering portability and intuitive interfaces for efficient data collection in the wild. However, accurately and robustly extracting 6DoF end-effector (EE) pose from these devices remains challenging, hindering the deployment of robot policies learned from these data on fine-grained manipulation tasks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Hand-Held Grippers for Quasi-static Actions", "weight": 1.0} -->

Prior works attempted to address this issue through various approaches, such as SfM which suffers from scale ambiguity; RGB-D fusion which requires expensive sensors and onboard compute; external motion tracking which is limited to lab settings. These devices, constrained to quasi-static actions due to low EE tracking accuracy and robustness, often necessitate cumbersome onboard computer or external motion capture (MoCap) systems, diminishing their feasibility for in-the-wild data collection. In contrast, UMI integrates state-of-the-art SLAM with built-in IMU data from GoPro, to accurately capture 6DoF actions at the global scale. The high-accuracy data enables trained BC policy to learn bimanual tasks. With thorough latency matching, UMI further enables real-world deployable policy for dynamic actions such as tossing.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Hand-Held Grippers for Quasi-static Actions", "weight": 1.0} -->

Recently, Dobb-E proposed a "reacher-grabber" tool mounted with an iPhone to collect single-arm demonstrations for the Stretch robot. Yet, Dobb-E only demonstrates policy deployment for quasi-static tasks and requires environment-specific policy fine-tuning. Conversely, using only data collected with UMI enables trained policy to zero-shot generalize to novel in-the-wild environments, unseen objects, multiple robot embodiments, for dynamic, bimanual, precise and long-horizon tasks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

Portable. The hand-held UMI grippers can be taken to any environment and start data collection with close-to-zero setup time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

Capable. The ability to capture and transfer natural and complex human manipulation skills beyond pick-and-place.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method", "weight": 1.0} -->

Sufficient. The collected data should contain sufficient information for learning effective robot policies and contain minimal embodiment-specific information that would prevent transfer.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Method", "weight": 1.0} -->

Reproducible: Researchers and enthusiasts should be able to consistently build UMI grippers and use data to train their own robots, even with different robot arms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method", "weight": 1.0} -->

The following sections describe how we enable the above goals through our hardware and policy interface design.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

UMI's data collection hardware takes the form of a trigger-activated, handheld 3D printed parallel jaw gripper with soft fingers, mounted with a GoPro camera as the only sensor and recording device (see HD1). For bimanual manipulation, UMI can be trivially extended with another gripper.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

*How can we capture sufficient information for a wide*

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

*variety of tasks with just a wrist-mounted camera?*

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Specifically, on the observation side, the device needs to capture sufficient visual context to infer action HD2 and critical depth information HD3. On the action side, it needs to capture precise robot action under fast human motion HD4, detailed subtle adjustments on griping width HD5, and automatically check whether each demonstration is valid given the robot hardware kinematics HD6. The following sections describe details on how we achieve these goals.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

HD1. Wrist-mounted cameras as input observation. We rely solely on wrist-mounted cameras, without the need for any external camera setups. When deploying UMI on a robot, we place GoPro cameras with the same location with respect to the same 3D-printed fingers as on the hand-held gripper.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Minimizing the observation embodiment gaps. Thanks to our hardware design, the videos observed in wrist-mount cameras are almost indistinguishable between human demonstrations and robot deployment, making the policy input less sensitive to embodiment.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Mechanical robustness. Because the camera is mechanically fixed relative to the fingers, mounting UMI on robots does not require camera-robot-world calibration. Hence, the system is much more robust to mechanical shocks, making it easy to deploy.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Portable hardware setup. Without the need for an external static camera or additional onboard compute, we largely simplify the data collection setup and make the whole system highly portable.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Camera motion for natural data diversification. A side benefit we observed from experiments is that when training with a moving camera, the policy learns to focus on task-relevant objects or regions instead of background structures (similar in effect to random cropping). As a result, the final policy naturally becomes more robust against distractors at inference time.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Avoiding use of external static cameras also introduce additional challenges for downstream policy learning. For example, the policy now needs to handle non-stationary and partial observations. We mitigated these issues by leveraging wide-FoV Fisheye Lens HD2, and robust visual tracking HD4, described in the following sections.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

HD2. Fisheye Lens for visual context. We use a 155-degree Fisheye lens attachment on wrist-mounted GoPro camera, which provides sufficient visual context for a wide range of tasks, as shown in Fig.. As the policy input, we directly use raw Fisheye images without undistortion since Fisheye effects conveniently preserve resolution in the center while compressing information in the peripheral view. In contrast, rectified pinhole image exhibits extreme distortions, making it unsuitable for learning due to the wide FoV. Beyond improving SLAM robustness with increased visual features and overlap, our quantitative evaluation (Sec V-A) shows that the Fisheye lens improves policy performance by providing the necessary visual context.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

HD3. Side mirrors for implicit stereo. To mitigate the lack of direct depth perception from the monocular camera view, we placed a pair of physical mirrors in the cameras' peripheral view which creates implicit stereo views all in the same image. As illustrated in Fig (a), the images inside the mirrors are equivalent to what can be seen from additional cameras reflected along the mirror plane, without the additional cost and weight. To make use of these mirror views, we found that digitally reflecting the crop of the images in the mirrors, shown in Fig (c), yields the best result for policy learning (Sec. V-A). Note that without digital reflection, the orientation of objects seen through side mirrors is the opposite of that in the main camera view.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

HD4. IMU-aware tracking. UMI captures rapid movements with absolute scale by leveraging GoPro's built-in capability to record IMU data (accelerometer and gyroscope) into standard mp4 video files. By jointly optimizing visual tracking and inertial pose constraints, our Inertial-monocular SLAM system based on ORB-SLAM3 maintains tracking for a short period of time even if visual tracking fails due to motion blur or a lack of visual features (e.g. looking down at a table). This allows UMI to capture and deploy highly dynamic actions such as tossing. In addition, the joint visual-inertial optimization allows direct recovery of real metric scale, important for action precision and inter-gripper pose proprioception PD2.3: a critical ingredient to enable bimanual policy.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

HD5. Continuous gripper control. In contrast to the binary open-close action used in prior works, we found commanding gripper width continuously significantly expands the range of tasks doable by parallel-jaw grippers. For example, the tossing task requires precise timing for releasing objects. Since objects have different widths, binary gripper actions will be unlikely to meet the precision requirement. On UMI gripper, finger width is continuously tracked via fiducial markers. Using series-elastic end effectors principle, UMI can implicitly record and control grasp forces by regulating the deformation of soft fingers through continuous gripper width control.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

HD6. Kinematic-based data filtering. While the data collection process is robot-agnostic, we apply simple kinematic-based data filtering to select valid trajectories for different robot embodiments. Concretely, when the robot's base location and kinematics are known, the absolute end-effector pose recovered by SLAM allows kinematics and dynamics feasibility filtering on the demonstration data. Training on the filtered dataset ensures policies comply with embodiment-specific kinematic constraints.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-A Demonstration Interface Design", "weight": 1.0} -->

Putting everything together. The UMI gripper weighs 780g, with an external dimension of ${{{{L310mm} \times W}175mm} \times H}210mm$ and finger stroke of $80mm$. The 3D printed gripper has a BoM cost of \$73, while the GoPro camera and accessories total \$298. As shown in Fig., we can equip any robot arms with a compatible gripper and camera setup.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

With the collected demonstration data, we can train a visuomotor policy that takes in a sequence of synchronized observations (RGB images, 6 degrees-of-freedom end-effector pose, and gripper width) and produces a sequence of actions (end-effector pose and gripper width) as shown in Fig. (b). In this paper, we use Diffusion Policy for all of our experiments, while other frameworks such as ACT could potentially serve as a drop-in replacement.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

An important goal of UMI's policy interface design is to ensure the interface is agnostic to underlying robotic hardware platforms such that the resulting policy, trained on one data source (i.e., hand-held gripper), could be directly deployed to different robot platforms.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

Hardware-specific latency. The latency of various hardware (streaming camera, robot controller, industrial gripper) is highly variable across system deployments, ranging from single-digit to hundreds of milliseconds. In contrast, all information streams captured by UMI grippers have zero latency with respect to the image observation, thanks to GoPro's synchronized video, IMU measurements and the vision-based gripper width estimation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

Embodiment-specific proprioception. Commonly used proprioception observations such as joint angles and EE pose are only well-defined with respect to a specific robot arm and robot base placement. In contrast, UMI needs to collect data across diverse environments and be generalizable to multiple robot embodiments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

In the following sections, we will describe three policy interface designs that address these challenges.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD1. Inference-time latency matching. While UMI's policy interface assumes synchronized observation streams and immediate action execution, physical robot systems do not conform to this assumption. If not carefully handled, the timing mismatch between training and testing can cause large performance drops on dynamic manipulation tasks that require rapid movement and precise hand-eye coordination, demonstrated in Sec V-B.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD1.1) Observation latency matching. On real robotic systems, different observation streams (RGB image, EE pose, gripper width) are captured by distributed micro-controllers, resulting in different observation latency.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

For each observation stream, we individually measure their latency (details see §A.0-A1-A.0-A3). At inference time, we align all observations with respect to the stream with the highest latency (usually the camera). Specifically, we first temporally down-sample the RGB camera observations to the desired frequency (often 10-20Hz), and then use the capture timestamp of each image $t_{obs}$ to linearly interpolate gripper and robot proprioception streams. In bimanual systems, we soft-synchronize two cameras by finding the nearest neighbor frames, which can be off by a maximum of $\frac{1}{60}$ seconds. The result is a sequence of synchronized observations that conform to UMI policy, shown in Fig. (a).

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD1.2) Action latency matching. UMI policy assumes the output as a sequence of synchronized EE poses and gripper widths. However, in practice, robot arms and grippers can only track the desired pose sequence up to an execution latency, that varies across different robot hardware. To make sure the robots and grippers reach the desired pose at the desired time (given by the policy), we need to send commands ahead of time to compensate for execution latency, as shown in Fig. (c). See §A.0-A4 for execution latency calibration details.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

During execution, the UMI policy predicts the action sequence starting at the last step of observation $t_{obs}$. The first few actions predicted are immediately outdated due to observation latency $t_{input} - t_{obs}$, policy inference latency $t_{output} - t_{input}$ and execution latency $t_{act} - t_{output}$. We simply discard the outdated actions and only execute actions with the desired timestamp after $t_{act}$ for each hardware.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD2. Relative end-effector pose. End-effector (EE) pose is central to both UMI's observation and action space. To avoid dependence on embodiment/deployment-specific coordinates, we represent all EE poses relative to gripper's current EE pose.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD2.1) Relative EE trajectory as action representation. Prior works have shown the significant impact of action space selection on task performance, with experimental evidence favoring absolute positional actions over delta actions. However, we found that a relative trajectory representation, defined for an action sequence starting at $t_{0}$ as a sequence of $SE{}$ transforms denoting the desired pose at $t$ relative to the initial EE pose at $t_{0}$, allows the system to be more robust against tracking errors during data collection and camera displacements.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD2.2) Relative EE trajectory as proprioception. Similarly, we represent the proprioception of history EE poses as a relative trajectory. When observation horizon is set to 2, this representation effectively provides velocity information to the policy. Combined with our wrist-mounted camera observation space, relative trajectory allows our system to be calibration-free. Moving the robot base during execution will not affect task performance (Fig. (a)), as long as the objects are still within reach range, making the UMI framework applicable to mobile manipulators as well.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-B Policy Interface Design", "weight": 1.0} -->

PD2.3) Relative inter-gripper proprioception. When using UMI in a bimanual setup, we found that providing the policy with the relative pose between the two grippers to be critical for bimanual coordination and task success, as shown in Sec. V-C. The effect of inter-gripper proprioception is particularly large when the visual overlap between two cameras is small. The inter-gripper proprioception is enabled by our map-then-localize data collection scheme that constructs a scene-level global coordinate system HD4. For each new scene, we first collect a video that builds a map for the scene. Then, all demonstrations collected in this scene are relocalized to the same map, therefore sharing the same coordinate system. Despite the videos from each gripper being relocalized separately, the relative pose between two grippers at each time step can be calculated using their shared coordinates.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Capability: How well can we transfer UMI demonstrations to effective robot policy? Especially for complex, dynamic, bimanual, and long-horizon manipulation skills.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Generalization: Will data collected in the wild within diverse environments help the policy to generalize to unseen environments and objects?

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Data collection efficiency: How fast can we collect manipulation data with UMI? What's the accuracy of the SLAM system?

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluations", "weight": 1.0} -->

To access capability and generalization, we evaluate UMI on 4 real-world robotic tasks across both narrow domain and in-the-wild environments, shown in Fig.. To measure data collection efficiency, we compare the UMI gripper with human hand demonstration and a typical teleop interface. See §A.0-B for detailed data collection protocol.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Capability Experiments", "weight": 1.0} -->

We study UMI's ability to capture and transfer single-hand, bimanual, dynamic, and long-horizon manipulation skills with four tasks. For capability experiments, all tasks are evaluated in the same environment as data collection but with randomized robot and object initial states. To ensure a fair comparison, we use exactly the same initial state across all methods for both the robot and objects, by manually aligning the scene against pre-recorded images. See §A.0-C for detailed evaluation protocol and videos for all experiments.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

Task Place an espresso cup on the saucer with its handle facing to the left of the robot, Fig.. We defined task success as when the cup is placed upright on the saucer with its handle within $\pm {15{^\circ}}$ to the left.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

Capability (what makes the task difficult?) This task tests the system's ability to learn both prehensile (pick and place) and non-prehensile actions (i.e., pushing to reorientate the cup). When the handle faces straight away from the robot, the two equally valid solutions: rotation clockwise and counter-clockwise form a multi-modal action distribution. This task also tests UMI's ability to sense relative depth through monocular camera observation and side mirrors.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

Performance The training dataset contains 305 episodes collected by 2 demonstrators, evaluation includes 20 test cases, with the testing initial state distribution shown in Fig. (a). UMI can complete the task 20/20. The next paragraphs will discuss our ablation studies around our key design decisions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

Cross-robot generalization: To demonstrate UMI's cross-embodiment generality, we also deployed the same policy checkpoint on a Franka Emika FR2 robot, shown in Fig. and Fig.. This experiment achieves ${18/20} = {90\%}$ success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we had mounted the FR2 robot at a different location.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

No Fisheye lens [\[HD2\]]: To ablate the importance of having a wide field-of-view (FoV) Fisheye lens, we post-processed the dataset by rectifying and cropping each image to a square with $69{^\circ}$ horizontal and vertical FoV. This is a generous analogy of RealSense D415 ($69{^\circ}$ HFoV, $42{^\circ}$ VFoV) and iPhone wide camera ($69{^\circ}$ HFoV, $51{^\circ}$ VFoV). This baseline only achieves ${11/20} = {55\%}$ success rate. Beyond the expected failure mode where the cup is outside of camera view, we found this baseline policy to perform surprisingly poor even if the object is visible, with often jittery motions. We suspect that during training, the poor object visibility forced the policy to be unnecessarily multimodal.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

Alternative action spaces [\[PD2\]]: As alternatives to our relative trajectory as action representation, we also consider absolute and delta action spaces as illustrated in Fig. Since the SLAM system outputs pose relative to the first frame of the mapping video (details in §A.0-D), we can only calculate relative and delta actions directly using SLAM output. To compute absolute actions in the robot base frame, we calibrate both SLAM coordinates and the robot with respect to the same fiducial markers placed on the table.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

The delta action baseline achieves ${16/20} = {80\%}$ success rate. The absolute action baseline performs surprisingly poorly with only ${5/20} = {25\%}$ success rate, demonstrating a noticeable bias in action selection, likely due to inaccurate calibration between the SLAM and robot base coordinate frames (Fig. (b)). While theoretically the performance of this baseline could approach that of relative trajectory with better calibration, this experiment underscores the difficulty of obtaining action data with absolute coordinates, even in controlled lab settings.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Cup Arrangement", "weight": 1.0} -->

Effect of side mirrors [\[HD3\]]: To our surprise, directly providing mirror images decreases the performance from ${18/20} = {90\%}$ (no mirror) to ${17/20} = {85\%}$. To fully take advantage of side mirrors, we need to digitally reflect the content inside mirrors and swap left and right mirror images, which achieves a ${20/20} = {100\%}$ success rate. We hypothesize that without digital reflection, the opposite motions observed in the main and mirrored images might confuse vision encoders, especially those with translational equivariance.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-B Dynamic Tossing", "weight": 1.0} -->

Task The robot is tasked to sort 6 objects from the YCB object set randomly placed on a table by tossing them to the corresponding bin. The 3 spherical objects (baseball, orange, apple) should be tossed into the round bin, while the 3 Lego Duplo pieces go into the rectangular bin. The bins are placed beyond the robot's kinematic reach range to highlight the necessity of dynamic action for this task.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B Dynamic Tossing", "weight": 1.0} -->

Capability: The dynamic tossing task demonstrates UMI's ability to capture and transfer fluid and rapid human motions, precise hand-eye coordination (between RGB and proprioception) and timing alignment (between robot and gripper).

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B Dynamic Tossing", "weight": 1.0} -->

Performance: We collected 280 demonstration episodes for this task, with mixed multi and single-object picking and tossing. Our policy (with inference time latency matching) achieves ${105/120} = {87.5\%}$ success rate, counted by the number of objects successfully tossed to their corresponding bin.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B Dynamic Tossing", "weight": 1.0} -->

No Latency Matching [\[PD1\]]: With the same trained policy, we disable inference-time latency matching by setting the measured latencies for all observation and action streams to 0. We visually observe the policy's movement is much more jittery due to the out-of-sync observations and executions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-B Dynamic Tossing", "weight": 1.0} -->

While the jitteriness minimally affects grasping, its impact on tossing performance is notable as it disrupts the robot motion to achieve the desired tossing velocity, as illustrated in the elbow joint velocity curve in Fig.. In addition, the misalignment between the gripper and robot action (due to their different execution latency) leads to suboptimal object release during tossing. As a result, the final success rate decreased to ${69/120} = {57.5\%}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-C Bimanual Cloth Folding", "weight": 1.0} -->

Task Two robot arms need to coordinate and fold the sweater's sleeves inward, fold up the bottom hem, rotate 90 degrees, and finally fold the sweater in half again. See §A.0-C for detailed evaluation protocol.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-C Bimanual Cloth Folding", "weight": 1.0} -->

Capability Manipulating high degrees of freedom deformable objects is challenging due to their complex dynamics and underactuation. In addition, this task requires tight coordination between arms. For example, lifting the bottom hem requires two arms to pick it up at the same time, and if one of the arm is just slightly too fast or slow this step will fail.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C Bimanual Cloth Folding", "weight": 1.0} -->

Performance We collected 250 demonstrations from two demonstrators, with randomized initial states by translating/rotating the shirt and folding the sleeves. We use a single centralized policy to generate actions for both robot arms and grippers. Our policy achieves ${14/20} = {70\%}$ success rate.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C Bimanual Cloth Folding", "weight": 1.0} -->

No relative inter-gripper proprioception [\[PD2.3\]]: Without inter-gripper proprioception information (during both training and eval), the coordination between the two arms becomes significantly worse. The most salient failure case is when the two arms lift the bottom hem of the shirt, where the baseline policy often misses one of the grasps due to asynchronous grasp action (Fig. (b)). As a result, the baseline policy only achieves success rate of ${6/20} = {30\%}$. In contrast, UMI policy synchronizes the grasp by first reaching the pre-grasp pose and waiting until both arms are in position before simultaneously grasping and folding.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-D Dish Washing", "weight": 1.0} -->

Task The robot needs to execute 7 steps of sequentially dependent actions (turn on faucet, grasp plate, pick up sponge, wash and wipe plate until ketchups are removed, place plate, place the sponge and turn off faucet), shown in Fig.. See §A.0-C for detailed evaluation protocol.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-D Dish Washing", "weight": 1.0} -->

Capability This task pushes the boundaries of robot manipulation capability from several fronts: 1) it is an ultra-long horizon task where each step's success depends on the previous one; 2) the robot needs to perceive and manipulate complex fluid including both Newtonian fluid (i.e., water) and non-Newtonian fluid (i.e., ketchup). 3) the wiping motion requires using a deformable tool (i.e., sponge) while coordinating both arms with reference to the water stream; 4) manipulating constrained articulated object (i.e., turning on and off faucet) requires mechanical compliance provided by soft fingers; 5) the policy also need to be semantically robust to the concept of "cleanliness". When additional ketchup is added during washing or even after the washing phase is done, the robot needs to resume washing and wiping.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-D Dish Washing", "weight": 1.0} -->

Performance A single demonstrator collected 258 demonstrations with randomized initial states including, ketchup patterns, position of the plate and sponge, along with water faucet angle. The collected demo also include explicit demonstrations of recovery behavior when additional ketchup is added. For this task, we train diffusion policy by fine-tuning a CLIP pretrained ViT-B/16 vision encoder. Overall, UMI achieves ${14/20} = {70\%}$ success rate. In addition, we demonstrate the robustness of our policy against various distractors, and types of sauce (mustard, chocolate syrup, caramel syrup), as well as robustness against perturbations, see Fig. and video on our website for details.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-D Dish Washing", "weight": 1.0} -->

No CLIP-pretrained ViT vision encoder. For this visually complex task, we found training ResNet-34 from scratch to be insufficient. Specifically, the baseline policy with ResNet-34 learned an non-reactive behavior and ignored any variation in plate or sponge position. As a result, it cannot perform the task, ${0/10} = {0\%}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

Prior works in behavior cloning typically only evaluate in the same environment as data collection, often limited by their inability to collect sufficiently diverse dataset to allow generalization. By not relying on teleoperation with real robots, UMI enables low-cost data collection in any environment, which we refer to as in-the-wild data.

<!-- chunk {"id": "body-0086", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

We evaluate UMI's ability to produce generalizable visuomotor policies by scaling up the cup arrangement task Sec. V-A to novel environments and novel objects. Within 12 person-hours, 3 demonstrators collected 1400 demonstrations for the cup arrangement task across 30 diverse physical locations, including homes, offices, restaurants, and outdoor environments. The demonstrations involved 15 espresso cups of different colors, shapes (cylindrical and tapered), and materials (ceramic, glass, and metal). To ensure model capacity, we increased the vision encoder further to CLIP pretrained ViT-L/14.

<!-- chunk {"id": "body-0087", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

Cafe table is a metal table in the outdoor seating area of a busy cafe where a large number of pedestrians serve as natural distractors. We tested 5 cups in the training set and 2 testing (unseen) cups, with 5 initial poses each, 35 experiments in total.

<!-- chunk {"id": "body-0088", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

Water fountain is a black cubic water fountain, with a thin film of water constantly flowing from the center, covering the entire top surface. This environment is notably out-of-distribution since all of our demonstrations are collected on non-black tables, not to mention changes in surface dynamics due to the presence of water. We tested 3 training and 2 testing cups, with 5 initial poses each, 25 experiments in total.

<!-- chunk {"id": "body-0089", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

We selected the 2 testing cups such that one has an out-of-distribution color (dark blue), while the other has an unseen texture (brown rings). For each test case, we vary the initial pose of both the cup and the saucer.

<!-- chunk {"id": "body-0090", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

Our UMI policy has ${28/40} = {70\%}$ success rate on training cups and ${15/20} = {75\%}$ success rate on testing cups, with a combined success rate of ${43/60} = {71.7\%}$. More qualitative and quantitative results are shown in Fig..

<!-- chunk {"id": "body-0091", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

No in-the-wild data. To validate the generalization ability comes from in-the-wild data, instead of pretrained vision backbone, we trained another model that only uses data from our narrow-domain experiment collected in the same lab environment (described in Sec. V-A) with the same pretrained ViT vision backbone. In the same unseen environments, as shown in Fig. (b), the robot with the baseline policy doesn't even move toward the cup. As a result, its success rate is 0%.

<!-- chunk {"id": "body-0092", "role": "body", "section": "In-the-wild Generalization Experiments", "weight": 1.0} -->

Takeaway. This result indicates that finetuning a large pre-trained model with narrow-domain data is insufficient for producing an in-the-wild deployable policy. Therefore collecting diverse, in-the-wild data is still critical for effective generalization to novel environments and objects.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Data Collection Throughput and Accuracy", "weight": 1.0} -->

Throughput. UMI's improved ergonomics and intuitiveness over teleoperations also lead to improved data collection throughput. To demonstrate this effect, we record the number of demonstrations that can be collected within 15 minutes by the same operation using 3 different methods: 1) Human hand demonstration 2) UMI gripper 3) Spacemouse-based teleoperation, which is a typical teleoperation interface used in many learning from demonstration works. We measure the data throughput on two tasks: 1) cup arrangement 2) dynamic tossing. Note that the time taken to reset the environment, randomize objects, and handle robot faults (such as self-collisions) are also counted in this experiment to accurately represent the real-world data collection throughput.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Data Collection Throughput and Accuracy", "weight": 1.0} -->

On the cup arrangement task, the UMI gripper is more than $3 \times$ faster than teleportation, at $48\%$ speed of the human hand, shown in Fig. (d). Note that human is significantly faster on reset and randomization, due to their proximity to the objects. On the dynamic tossing task, the UMI gripper is at $64\%$ speed of the human hand, while the teleportation method failed to produce a single successful demonstration in 15 minutes.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Data Collection Throughput and Accuracy", "weight": 1.0} -->

Accuracy. To independently assess the accuracy of our SLAM-based tracking system, we collected a SLAM benchmark dataset with MoCap ground truth. The dataset contains 7 single-gripper tasks and 7 bimanual tasks, all with a variety of movable objects in view as well as natural and rapid human motion. As shown in Fig., our SLAM system has a mean Absolute Trajectory Error (ATE) of $6.1mm$ for position and $3.5{^\circ}$ for rotation. Since both grippers are localized with the same map, we can also obtain the relative pose between two grippers (i.e. inter-gripper pose PD2.3). The mean Relative Pose Error (RPE) between two grippers is $10.1mm$ for position and $0.8{^\circ}$ for rotation.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Limitations and Future Works", "weight": 1.5} -->

While UMI demonstrates policy efficacy across a wide range of tasks and scenarios, a few limitations remain. First, since the kinematics limits of the downstream deployment robots are unknown at the time of data collection, we rely on data filtering to ensure the kinematic feasibility of the resulting policy. Future works could develop an embodiment-aware policy learning framework that can transfer skills from valid but hardware-infeasible actions.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Limitations and Future Works", "weight": 1.5} -->

Second, our SLAM-based action recovery system inherits visual SLAM's requirement for sufficient texture in the environment. Future works could leverage static third-person-view cameras, coupled with additional fiducial markers on UMI grippers to recover action even in texture-deficient environments like rooms with pure white walls.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Limitations and Future Works", "weight": 1.5} -->

Third, collecting data with UMI grippers is still less efficient than human hand demonstration, as shown in Sec. VII. This is in part due to the gripper's weight and bulkiness, and in part due to the reduced degrees of freedom compared to human hands. Future works could explore lighter materials and further improve UMI gripper's mechanical design and ergonomics, or alternatively, build sufficiently capable dexterous robotic hands and policies that can directly transfer from human motions.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present Universal Manipulation Interface (UMI), a framework that enables learning capable and generalizable manipulation policies directly from in-the-wild human demonstrations. The UMI gripper, a hand-held demonstration interface, captures sufficient information to learn some challenging manipulation tasks, including washing a dirty dish, bimanual sweater folding, and dynamic object tossing and sorting. At the same time, UMI remains highly scalable for in-the-wild data collection with its portability, cost-effectiveness, and operational simplicity. By recording all information in a single, standardized MP4 file, UMI's data can be easily shared over the Internet, allowing geographically distributed data collection from a large pool of nonexpert demonstrators. Our goal with UMI is to democratize robotic data collection, fostering a vast, diverse, and decentralized dataset to emerge from the robotics community
