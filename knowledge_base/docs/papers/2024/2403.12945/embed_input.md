<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

Topics include Robotics, Safety, Robustness, Datasets, Distributed systems, Generalization, Learning, DROID.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The creation of large, diverse, high-quality robot manipulation datasets is an important stepping stone on the path toward more capable and robust robotic manipulation policies. However, creating such datasets is challenging: collecting robot manipulation data in diverse environments poses logistical and safety challenges and requires substantial investments in hardware and human labour. As a result, even the most general robot manipulation policies today are mostly trained on data collected in a small number of environments with limited scene and task diversity. In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes and 84 tasks by 50 data collectors in North America, Asia, and Europe over the course of 12 months. We demonstrate that training with DROID leads to policies with higher performance and improved generalization ability. We open source the full dataset, policy learning code, and a detailed guide for reproducing our robot hardware setup.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

^††^footnotetext: Affiliations: ^1^Stanford University; ^2^University of California, Berkeley; ^3^Toyota Research Institute; ^4^Carnegie Mellon University; ^5^University of Texas, Austin; ^6^University of Montreal; ^7^University of Edinburgh; ^8^Princeton University; ^9^University of Washington; ^10^Korea Advanced Institute of Science & Technology (KAIST); ^11^University of California, San Diego; ^12^Google DeepMind; ^13^University of California, Davis; ^14^University of Pennsylvania; ^15^Columbia University; ^16^Yonsei University

<!-- chunk {"id": "body-0004", "role": "body", "section": "Scenes", "weight": 1.0} -->

13k222Fang et al. report 110k trajectories for RH20T, but count each camera stream separately – here we report the number of unique multi-view trajectories, to compare fairly to all other datasets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Scenes", "weight": 1.0} -->

A key feature of robot manipulation policies is their ability to generalize, i.e., their ability to perform a desired manipulation task under new lighting conditions, in new environments, or with new objects. Training policies that are robust to such variations is a crucial step towards the deployment of robots in everyday environments and may bring us closer to every roboticist's dream: robot models that can be downloaded and "just work" when tested on a new robot setup. A central ingredient for training such generalizable policies is diverse training data: in computer vision and natural language processing, training on large and diverse datasets scraped from the internet yields models that work in a wide range of new tasks. Similarly, in robot manipulation, a number of recent works have demonstrated that larger, more diverse robot training datasets enable us to push the envelope on policy generalization, including positive transfer to new objects, instructions, scenes, and embodiments. This suggests that an important stepping stone on the path toward more capable and robust robotic manipulation policies is the creation of large, diverse, high-quality robot manipulation datasets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Scenes", "weight": 1.0} -->

However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily scraped from the internet. Collecting robot manipulation data in diverse environments poses logistical and safety challenges when moving robots outside of controlled lab environments. Additionally, collecting data at scale requires substantial investments in hardware and human labour for supervision, particularly for collecting demonstration data. As a result, even the most general robot manipulation policies today are mostly trained on data collected in controlled, lab-like environments with limited scene and task diversity. To enable the next level of generalizable robot manipulation policy learning, the robot manipulation community needs more diverse datasets, collected across a wide range of environments and tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Scenes", "weight": 1.0} -->

In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see LABEL:fig:teaser). DROID consist of 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes, 52 buildings and 86 tasks. DROID was collected by 18 research labs in North America, Asia, and Europe over the course of 12 months. To streamline distributed data collection and ensure applicability of the final dataset to a wide range of research settings, all data is collected on the same robot hardware stack based on the popular Franka Panda robot arm. Each episode contains three camera views, depth information, camera calibration, and language annotations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Scenes", "weight": 1.0} -->

In experiments across 6 tasks and 4 locations, from labs to offices and real households, we find that DROID boosts policy performance, robustness and generalizability by 20% on average over state-of-the-art approaches that leverage existing large-scale robot manipulation datasets. We open-source the full DROID dataset under CC-BY 4.0 license, code for training policies using the dataset, and a detailed guide for reproducing our complete robot software and hardware setup.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Large datasets in machine learning", "weight": 1.0} -->

The rapid progress in machine learning has been closely tied to the construction of large and diverse datasets. Examples include ImageNet, Kitti, Ego4D and LAION in computer vision, Common Crawl and The Pile in natural language processing, and ShapeNet and Objaverse in 3D modeling. Key to their impact is their size and diversity: by enabling training on larger and more diverse data, they push the capabilities and robustness of machine learning models. With DROID we aim to continue this trend for robot manipulation and provide a large and diverse robot manipulation dataset to spur progress on generalizable policy learning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Robot learning datasets", "weight": 1.0} -->

A number of prior works introduce datasets for robot learning of various sizes and diversity levels (see Table I). Broadly, these can be categorized into datasets collected autonomously via scripted and semi-random behaviors or learned agents, and datasets collected via human teleoperation. Multiple works focus on increasing dataset diversity: RH20T collects data across 33 tasks in 7 table-top scenes and BridgeV2 collects data in 24 scenes.^11^1Note that prior works use various definitions for what constitutes a "task" and what constitutes a "scene". In this work, we use the number of unique *verbs* extracted from the language instructions to represent the number of tasks, which is more scalable than manually defining tasks yet often more reflective of the behavior diversity than e.g., counting the number of verb-object combinations (see Fig. 1 for DROID's verb distribution as an example).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Robot learning datasets", "weight": 1.0} -->

For scenes, we only count a scene as new if there is a substantial change of the robot's workspace, e.g., if it gets transported to a new corner of the kitchen or a new room altogether, but not if only the arrangement of objects in front of the robot or the table cloth changes. While these datasets increase diversity, most of their data is collected in a small number of scenes in a single research lab or building.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Robot learning datasets", "weight": 1.0} -->

More recently, there has been a larger effort on pooling existing robot datasets into a coherent format, the Open X-Embodiment dataset (OXE). Albeit larger in scale than prior robot datasets, the OXE dataset still consists of individual datasets with few scenes, thus totalling around 300 scenes at the time of writing. Our goal with the DROID dataset is to significantly increase the scene diversity as well as scene realism by collecting data across a wide array of real world buildings in a diverse set of geographic locations. As a result, DROID contains data from 564 scenes across 52 buildings, a substantial increase compared to any existing robot manipulation dataset.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Robot learning datasets", "weight": 1.0} -->

Collecting such data "in-the-wild" is more common for robot navigation and autonomous driving and enables training of policies that generalize zero-shot to new environments and even embodiments. With DROID, we take a step towards enabling similar generalization for robotic *manipulation* policies. Finally, there are some works that leverage cheap, off-the-shelf tools, such as reacher-grabber tools, for data collection, equipping robots with the same tools to allow for zero-shot transfer to the robot. While this simplifies the data collection process, it limits the data to wrist camera viewpoints and may suffer from morphology differences when transferring from human-arm-collected data to robot arm execution. Additionally, DROID has larger scene and task diversity than prior tool-based collection datasets.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Scalable robot policy learning", "weight": 1.0} -->

Learning robot policies from increasingly large and diverse datasets has been the focus of numerous efforts over the last few years. Initially, these efforts focused in large part on learning from scripted or autonomously collected data. The success of transformer models in natural language processing and computer vision motivated a number of recent works that collected large-scale demonstration datasets and trained transformer-based policies on them. Additionally, recent works suggest that diffusion denoising models are a powerful parametrization for multi-modal action output distributions that combine expressivity with scalability. Our focus with DROID is on introducing a new dataset, not a new policy learning algorithm. As such, we build on *existing* state-of-the-art diffusion policies for all of our policy learning experiments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "DROID Data Collection Setup", "weight": 1.0} -->

In this work, we introduce DROID (Distributed Robot Interaction Dataset), an open-source robot manipulation dataset that provides for very high diversity and variability of scenes, tasks, and objects (see Table I). Diverse and high-quality data is a key ingredient for training generalizable policies, and DROID is designed to deliver both quantity and quality: it contains 76k robot demonstration trajectories, spanning 86 tasks and 564 scenes. It was collected over the course of 12 months in a large, cross-institutional effort with 18 robots and 50 data collectors across 13 institutions. All data is collected on a shared, open-source robot platform.

<!-- chunk {"id": "body-0016", "role": "body", "section": "DROID Data Collection Setup", "weight": 1.0} -->

We are releasing all resources to enable researchers to build upon DROID at This includes the full dataset under CC-BY 4.0 license, an interactive dataset visualizer, code for training generalizable policies on DROID, pre-trained policy checkpoints, and a detailed guide for reproducing our robot hardware setup and control stack. In this section, we introduce our hardware setup and the data collection protocol.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A DROID Robot Platform", "weight": 1.0} -->

A crucial component of building the DROID dataset was distributed data collection at 13 institutions around the world: it is what enabled us to collect manipulation data across a large diversity of scenes and tasks. A key challenge in this distributed setup is robot hardware: how can we ensure *consistent and reproducible* robot control across so many setups, locations and time zones? To streamline the distributed data collection process we designed the DROID robot platform (see Fig. ), a hardware platform for data collection that is shared between all institutions, allowing us to quickly set up new data collection units and roll out updates across the whole data collection fleet. It is designed to support easy transportation between scenes and quick adjustment to new scenes and tasks.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A DROID Robot Platform", "weight": 1.0} -->

We chose the Franka Emika Panda 7 DoF robot arm as the base of our setup since it is widely adopted in the robot research community, reliable, relatively affordable and was available at most participating institutions. The robot arm is equipped with a Robotiq 2F-85 gripper and is mounted on a height-adjustable standing desk with wheels so it can easily move between scenes and buildings. We record image observations with three synchronized stereo camera streams: two exterior Zed 2 cameras, table-mounted on adjustable tripods to quickly adapt to a new scene layout, and a wrist-mounted Zed-Mini camera. We use the Polymetis controller and record actions both in robot joint space and in end-effector space at a control frequency of 15Hz. The setup is completed with the Franka robot control box, a NUC that hosts the Polymetis server and an Alienware laptop that runs our data collection GUI (see Section III-B). Everything is powered with a single power cable to further simplify changes in location.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A DROID Robot Platform", "weight": 1.0} -->

For teleoperation, we use the controllers of a Meta Quest 2 headset to control the pose of the arm in 6D space as well as the gripper in continuous space. Over the course of this project we have replicated this setup 18 times across various locations in North America, Asia, and Europe. We provide a thoroughly tested guide to replicate the hardware and software of our setup. We found that the setup is well-suited for data collection and policy learning across a wide range of scenes and tasks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Data Collection Protocol", "weight": 1.0} -->

Our dataset is collected by 50 data collectors across various research institutions. A shared data collection protocol helps streamline data collection, particularly for inexperienced data collectors. When designing the collection protocol for DROID, we focused on the following objectives: preventing common data collection mistakes like "camera cannot see robot" or "teleoperator in camera view", encouraging collection of diverse data, allowing data collectors to creatively choose scenes and tasks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Data Collection Protocol", "weight": 1.0} -->

Every data collection session starts with moving the robot to a new scene. Data collectors were encouraged to choose scenes that include multiple interesting tasks, numerous interaction objects, and a healthy amount of clutter (see example scenes in Fig. 10). After setting up the robot in the new scene, the data collector chooses views for the 3rd person cameras that can capture a wide range of interesting behaviors in the scene. Then they perform extrinsic camera calibration using a checkerboard and the OpenCV calibration algorithm. Next, the data collector will enter all potential tasks for the current scene into a data collection GUI on the laptop attached to the robot, either by selecting from a list of task options or by typing in free-from task instructions (see Fig. 9 for screenshots of the GUI). During data collection the GUI will prompt the data collector with a *randomly* sampled task from this list for each new episode. This way we ensure that there is high coverage of diverse tasks and collection is not biased to easier tasks or closer objects.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Data Collection Protocol", "weight": 1.0} -->

Additionally, the GUI periodically prompts the data collector to perform randomly sampled "scene augmentations" like nudges to the mobile base, moving and re-calibrating the 3rd person cameras, changing the room lighting, and adding or removing items within the scene. For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various popular action spaces, a data collector ID, and the metadata entered in the GUI (see Appendix B for a detailed list of all features we record). The data collector also marks whether the collected sequence was a success, which we log as part of the metadata. DROID consists of 76k successful episodes; roughly 16k trajectories in our data collection were labeled as "not successful", which we include in our dataset release but *do not* count towards the size of DROID. A data collector will typically collect up to 100 trajectories or about 20 minutes of interaction data per scene before moving on to a new scene.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Data Collection Protocol", "weight": 1.0} -->

During post-processing, we label each episode with natural language commands using crowdsourcing via the tasq.ai data labeling platform. We provide up to three independently labeled instructions per episode from different crowd workers to ensure diversity of annotations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Data Collection Protocol", "weight": 1.0} -->

Since the initial extrinsic calibration parameters, provided through conventional calibration detailed above, may not always be accurate due to factors such as checkerboard misalignment, inconsistent lighting, or errors inherent to the OpenCV calibration method, we address these inaccuracies in Appendix G. We discuss in detail the automatic post-hoc calibration process and provide three comprehensive sets of camera calibration matrices for the DROID dataset, each accompanied by respective quality assessment metrics. These include camera-to-base calibrations for around 36k unique scenes with one camera calibrated relative to the base, camera-to-camera calibrations for all scenes, and a curated superset of 24k scenes covering all three calibration methods with both cameras calibrated relative to the base. These refined calibrations enhance the dataset's suitability for robust geometric understanding in robotics and 3D perception tasks. For more details, please see Sec. Appendix G.

<!-- chunk {"id": "body-0025", "role": "body", "section": "DROID Dataset Analysis", "weight": 1.0} -->

While we have so far referred to DROID and other large-scale robot manipulation datasets as "diverse," there is nuance in what constitutes a diverse robot dataset. Different axes of data diversity will affect the generalization abilities of models trained on the data differently: scene diversity may facilitate generalization to new scenes, while task or camera viewpoint diversity allows for greater generalization to new instructions and camera angles. We will analyze DROID along multiple important axes of diversity and compare it to existing large robot manipulation datasets.

<!-- chunk {"id": "body-0026", "role": "body", "section": "DROID Dataset Analysis", "weight": 1.0} -->

When deciding which axes of generalization to inspect for robot manipulation datasets, it is important to consider which aspects of the problem may change between the training and downstream usage scenarios, i.e., which axes we want manipulation policies to generalize over. This may involve aspects of the scene, task, and robot setup. We identify the following important axes of diversity for closer analysis: task diversity, object diversity, scene diversity, viewpoint diversity, and interaction location diversity. The latter refers to the diversity of 3D locations relative to the robot's base at which interactions with objects occur, an important factor when generalizing to new scene layouts where interactions often need to generalize to new table heights or new parts of the robot's workspace.

<!-- chunk {"id": "body-0027", "role": "body", "section": "DROID Dataset Analysis", "weight": 1.0} -->

We analyze DROID along these axes and compare it to existing large-scale robot manipulation datasets. For each dataset, we run our analysis using one randomly sampled third-person camera frame per episode and the provided language instruction annotations. We find that results are consistent across randomly sampled frames.

<!-- chunk {"id": "body-0028", "role": "body", "section": "DROID Dataset Analysis", "weight": 1.0} -->

We visualize the results of our analysis in Figs. 1, 2, 3 and 4. Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation datasets. A key reason is DROID's data collection protocol (see Section III-B): by collecting data with 50 data collectors in 52 buildings across three continents, switching scenes approximately every 20 minutes during collection and giving collectors the freedom to freely choose scene-appropriate tasks, we can substantially increase the diversity of scenes, tasks, and objects featured in the dataset. Next, we will describe our analysis for each category in more detail.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Task diversity", "weight": 1.0} -->

As explained in Section II, we use the distribution of de-duplicated verbs in a dataset's instructions as a scalable indicator for behavioral diversity. We use a semantic parsing algorithm to extract verbs and referenced objects from the language instructions. We then use GPT4 to de-duplicate the verbs, i.e., remove synonyms and typos. We plot the distribution of verbs for DROID in Fig. 1, top. DROID features a wide variety of verbs with a long-tailed distribution. We use a logarithmic scale for these visualizations, since diversity is about covering a wide range of tasks, rather than having a high concentration of many episodes on only a handful of tasks -- that is, it is less important if a task has 1000 vs. 2000 trajectories than whether it has 0 vs. 10. We also visualize the corresponding verb distributions for existing large manipulation datasets, and find that only Bridge V2 has a comparable long tail of verb classes, although in a more restricted set of scenes (see scene diversity analysis below). Fig. 16 shows a detailed view of the verb distributions for all datasets.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Object diversity", "weight": 1.0} -->

A dataset that includes manipulations for a large variety of objects facilitates generalization to new objects downstream. We analyze the objects the robot manipulates for each episode in DROID from the language instruction labels using the same semantic parsing pipeline and show the distribution in Fig. 1, bottom (best viewed zoomed, or see Fig. 17 for an enlarged version). DROID contains interactions with a wide range of everyday objects, spanning a diverse set of categories. We also plot the *joint* distribution of the most common verbs and interacted objects in Fig. 18. It shows that DROID not only contains diverse objects, but also a diverse range of interactions with most objects.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scene diversity", "weight": 1.0} -->

We define 10 scene types (see Fig. 2) and use GPT-4V to determine the scene type for a given episode in DROID (see Appendix C for the used prompt). We find that this leads to high-quality scene type annotations (see Fig. 10 for example scenes and their categorization). For existing robot datasets we manually determine the scene types for each scene due to the small number of total scenes. DROID contains 564 unique scenes, an order of magnitude more than existing large robot manipulation datasets. The scenes cover a wide spectrum of scene types, from office environments to households. Qualitatively, the scenes in DROID reflect realistic real world scenarios with naturally occuring objects and backgrounds. We highly encourage the reader to inspect qualitative examples of scenes in Fig. 10 and the supplementary videos.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Viewpoint diversity", "weight": 1.0} -->

Existing large-scale robot learning datasets often only contain a limited set of camera viewpoints because the cameras are mounted in a fixed location relative to the scene or robot. In contrast, DROID varies camera viewpoints significantly during data collection and thus has a broad coverage of viewpoints (see Fig. 3) with 1417 unique view points in the dataset.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Interaction location diversity", "weight": 1.0} -->

Another subtle yet important aspect of robot datasets is the diversity of interaction locations: are tasks always executed in the same narrow slice of the workspace, e.g., at the same table height, or does the data cover interactions across a large fraction of the work space? We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the 3D location of these interaction points for different datasets in Fig. 4. DROID features interactions in a wider range of the workspace than existing robot manipulation datasets that typically focus interactions on a table surface in front of the robot.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

The analysis in the previous section highlighted the diversity of tasks, objects, scenes, and viewpoints in the DROID dataset. In this section, we investigate whether this diverse data resource can be used to boost policy performance and robustness across a wide spectrum of robot manipulation tasks and environments. To this end, we train policies across 6 tasks in 4 different locations including lab, office, and household settings, to reflect the diversity of real world robotic research use cases (see Fig. 5). All experiments use representative, state of the art robot policy learning approaches. Across the board, we find that DROID improves policy success rate while increasing robustness to scene changes like distractors or novel object instances.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Tasks", "weight": 1.0} -->

As illustrated in Fig. 5, we choose 6 tasks in 4 locations that span a representative range of real robot learning use cases: from simple pick-place tasks to multi-stage cooking tasks; from clean lab settings to real households. All experiments use the DROID hardware stack for policy evaluations. Concretely, we evaluate on the following 6 tasks, each with their own out-of-distribution variants: Closing Waffle Maker: A short horizon task in a lab setting (70 demonstrations), where the task is to close a waffle maker. The waffle maker position is randomized between episodes. The out of distribution variant consists of adding several distractor objects on the table.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Tasks", "weight": 1.0} -->

Place Chips on Plate: A short horizon task in a lab setting (50 demonstrations), where the task is to pick and place a bag of Doritos chips onto a plate, with two distractor objects on the table. All objects and the plate position are randomized between episodes on the table. The out of distribution variant consists of (a) changing the type of chips or (b) adding more distractor objects to the table.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Tasks", "weight": 1.0} -->

Put Apple in Pot: A medium horizon task in a lab setting (60 demonstrations), where the task is to pick and place an apple into a pot and then put a lid on the pot. The apple, pot, and lid position are randomized between episodes on the table. The out of distribution variant involves placing a distractor plate on the table.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Tasks", "weight": 1.0} -->

Toasting: A medium horizon task in a lab setting (150 demonstrations), where the task is to put an object on a toaster oven tray, then close the toaster oven. The object and toaster position are randomized between episodes on the table. The out of distribution variant consists of toasting novel objects.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Tasks", "weight": 1.0} -->

Clean up Desk: A long horizon task in an office setting (50 demonstrations), where the task is to open a drawer, pick and place an eraser into the drawer, and then close the drawer. The eraser position is fixed. The out of distribution variant consists of adding distractor objects on the desk and in the drawer.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Tasks", "weight": 1.0} -->

Cook Lentils: A long horizon task in a kitchen setting (50 demonstrations), where the task is to remove the lid off a pan, pour lentils into the pan, and turn on the stove. The object positions are fixed. The out of distribution variant consists of adding several distractor objects and a camera shift.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Tasks", "weight": 1.0} -->

Additional details about each evaluation task can be found in Appendix E. All data is collected using the DROID teleoperation setup and training uses the same standardized policy learning backbone.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Policy training", "weight": 1.0} -->

The goal of this work is to introduce a new robot manipulation dataset, *not* to introduce a new policy learning method. Thus, during experimental evaluations we aim to leverage a well-adopted, state-of-the-art policy learning pipeline. To this end, we use diffusion policies, which leverage denoising diffusion models for action prediction and have recently demonstrated strong performance across a range of applications. We build on the implementation of diffusion policies in Robomimic, which provides high quality open-source implementations of a number of different imitation learning and offline RL algorithms. Concretely, all of our policies are conditioned on a language instruction, use the RGB camera streams from the two external cameras and the robot proprioception as input, and produce absolute robot end-effector translation, rotation, and gripper actions. We first downsample the camera observations to a resolution of $128 \times 128$ and use a ResNet-50 visual encoder pre-trained on ImageNet to encode both visual inputs. We then concatenate these visual embeddings with a frozen DistilBERT language embedding and the robots proprioceptive state.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Policy training", "weight": 1.0} -->

These concatenated features are then fed through an MLP and passed to a U-Net diffusion head which generates action trajectories. In line with prior work, we train the diffusion policy to generate 16-step action sequences, and during rollouts, step 8 actions open loop before re-running policy inference. For leveraging DROID during policy training, we simply mix training batches at a 50/50 ratio between the small in-domain dataset and the complete DROID dataset but excluding trajectories marked as "not successful", which we find to work well in practice. Additional details about the policy training can be found in Appendix F.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Does DROID Improve Policy Performance and Robustness?", "weight": 1.0} -->

To study if co-training with DROID can enable improved policy learning, we train separate policies for each evaluation task and compare all policies head-to-head in A/B evaluations using 10 rollouts for each task setting and method. To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of tasks in the in-domain demonstrations with noise added to the initial robot and object positions, and "out-of-distribution" (OOD), which tests policy robustness e.g., by introducing distractor objects or switching the manipulated object. We evaluate the following approaches: No Co-training: Trains a diffusion policy using the in-domain demonstrations only DROID (Ours): Trains a diffusion policy, but mixes batches 50/50 between in-domain demonstrations and DROID demonstrations OXE: Trains a diffusion policy, but mixes batches 50/50 between in-domain demonstrations and trajectories from the Open X-Embodiment dataset (OXE).

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Does DROID Improve Policy Performance and Robustness?", "weight": 1.0} -->

OXE contains most of the existing large robot manipulation datasets we compared DROID to in Section IV, as well as a large number of other robot datasets, spanning 22 robot embodiments and approximately 300 scenes total.^33^3We use a curated split of OXE based on Octo Model Team et al., which has been shown to work well for policy learning in prior work. We remove the Language Table dataset, equivalent to 5% of the Octo training mix, due to its repetitive scene layouts and tasks, and its raw size, which proved challenging to handle for our training infrastructure.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Does DROID Improve Policy Performance and Robustness?", "weight": 1.0} -->

We present the results of our policy evaluations in Fig. 6. Across all tasks, we find that DROID substantially improves policy performance compared to the diffusion policy trained on in-domain data only. Policies co-trained with DROID also perform better than policies that leverage diverse, existing robot datasets in Open X-Embodiment (OXE). Notably, when testing out of distribution performance, the No Co-training baseline performs quite poorly while the co-trained policies are much more effective. This difference is especially notable when co-training with DROID, which has the strongest overall performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Does DROID Improve Policy Performance and Robustness?", "weight": 1.0} -->

Qualitatively, we find that policies that leverage DROID during training are notably smoother and precise than other comparisons, particularly in the more challenging out-of-distribution evaluations. For instance, in the OOD setting of the Waffle Closing task, DROID is the only method that consistently reaches for the waffle maker, while the other methods get confused about the task. Similarly, in the multi-step Cook Lentils task, baselines tend to fail after two or sometimes just one step, while co-training with DROID is the only method able to consistently finish all three steps See Fig. 7 for examples of qualitative task rollouts.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C How important is the scene diversity in DROID?", "weight": 1.0} -->

One of the unique benefits of DROID compared to existing robot datasets is its amount of *scene diversity*. Indeed we see in Figure 2 that DROID contains far more scene diversity than the next most diverse robot manipulation dataset. While we've seen the benefits of co-training with DROID, *can we quantify how much of a role scene diversity plays in improved policy robustness?* To test this, we design an experiment that uses the challenging OOD versions of the evaluation tasks from Section V-A, but compares: DROID (7k, 20 Scenes): Selects for the 20 scenes from DROID with the most demonstrations each, resulting in 7362 trajectories with comparatively little scene diversity.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C How important is the scene diversity in DROID?", "weight": 1.0} -->

DROID (7k, Diverse Scenes): Uniform random sample of 7362 successful demonstrations from the DROID dataset, which matches dataset size to the previous method while retaining high scene diversity.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C How important is the scene diversity in DROID?", "weight": 1.0} -->

These comparisons use the same 50/50 co-training paradigm with individual task data used in the previous experiment. Hence, this helps establish whether the scene diversity of DROID results in better policy performance than just using 20 scenes while controlling for dataset size.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C How important is the scene diversity in DROID?", "weight": 1.0} -->

In Figure 8 we observe that using the split of the dataset with more diverse scenes yields better performance in the OOD evaluation setting. By comparing Figure 8's individual task performances with the corresponding tasks in Figure 6, we also see that the performance of co-training with the full DROID dataset matches or outperforms the performance with the subsampled dataset on all three tasks. These results suggest that the strength of DROID lies in its size and especially in its *diversity*.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we introduced DROID (Distributed Robot Interaction Dataset), a new robot manipulation dataset with a large diversity of scenes, tasks, objects and viewpoints. Our dataset analysis in Section IV showed that DROID has an order of magnitude larger scene diversity than existing large robot manipulation datasets, a wide range of tasks, many interaction objects, and diverse viewpoints. Our policy learning evaluations show that DROID is a valuable data resource for improving policy performance and robustness, even in comparison to existing large robot data sources like the Open X-Embodiment dataset.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

We hope that DROID can be a catalyst for research on general-purpose robot manipulation policies that are able to generalize to a broad range of tasks and scenes. In this work, we showed one example for leveraging DROID to boost policy performance, but there are many open questions about how to best make use of such diverse data: how should we combine DROID with existing large-scale robot datasets and how can we train policies that perform tasks in new scenes without *any* in-domain data? Can the diverse interaction data in DROID be used to learn better visual representations for robotic control? And in what situations is it helpful to train on the full dataset vs. slices of the data? We hope that DROID can accelerate research on these questions and are excited for how the community will leverage the dataset! We also hope that our open-sourced hardware platform, which already exists in 18 labs around the globe and is easy to reproduce, can improve reproducibility of robot learning research and facilitate future additions to the DROID dataset.
