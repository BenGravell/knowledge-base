<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

Topics include Imitation learning, Robotics, Generalization, Learning, BC-Z.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the grand challenges in robotics is to create a general-purpose robot capable of performing a multitude of tasks in unstructured environments based on arbitrary user commands. The key challenge in this endeavour is *generalization*: the robot must handle new environments, recognize and manipulate objects it has not seen before, and understand the intent of a command it has never been asked to execute. End-to-end learning from pixels is a flexible choice for modeling the behavior of such generalist robots, as it has minimal assumptions about the state representation of the world. With sufficient real-world data, these methods should in principle enable robots to generalize across new tasks, objects, and scenes without requiring hand-coded, task-specific representations. However, realizing this goal has generally remained elusive. In this paper, we study the problem of enabling a robot to generalize zero-shot or few-shot to new vision-based manipulation tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study this problem using the framework of imitation learning. Prior works on imitation learning have shown one-shot or zero-shot generalization to new objects and to new object goal configurations. However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) with diverse objects. Achieving such generalization depends on solving challenges relating to scaling up data collection and learning algorithms for diverse data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop an interactive imitation learning system with two key properties that enable high-quality data collection and generalization to entirely new tasks. First, our system incorporates shared autonomy into teleoperation to allow us to collect both raw demonstration data and human interventions to correct the robot's current policy. Second, our system flexibly conditions the policy on different forms of task specification, including a language instruction or a video of a person performing the task. Unlike discrete one-hot task identifiers, these continuous forms of task specification can in principle enable the robot to generalize zero-shot or few-shot to new tasks by providing a language or video command of the new task at test time. These properties have been explored previously; our aim is to empirically study whether these ideas scale to a broad range of real-world tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is an empirical study of a large-scale interactive imitation learning system that solves a breadth of tasks, including zero-shot and few-shot generalization to tasks *not seen* during training. Using this system, we collect a large dataset of 100 robotic manipulation tasks, through a combination of expert teleoperation and a shared autonomy process where the human operator "coaches" the learned policy by fixing its mistakes. Across 12 robots, 7 different operators collected 25,877 robot demonstrations that totaled 125 hours of robot time, as well as 18,726 human videos of the same tasks. At test time, the system is capable of performing 24 unseen manipulation tasks between objects that have never previously appeared together in the same scene. These closed-loop visuomotor policies perform asynchronous inference and control at 10Hz, amounting to well over 100 decisions per episode. We open-source the demonstrations used to train this policy at

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Setup and Method Overview", "weight": 1.0} -->

An overview of our imitation learning system is shown in Figure 1. Our goal is to train a conditional policy that can interpret RGB images, denoted $s \in \mathcal{S}$, together with a task command $w \in \mathcal{W}$, which might correspond to a language string or a video of a person. Different tasks correspond to completing distinct objectives; some example tasks and corresponding commands are shown in Figure 2. The policy is a mapping from images and commands to actions, and can be written as $\mu:{{\mathcal{S} \times \mathcal{W}}\rightarrow\mathcal{A}}$, where the action space $\mathcal{A}$ consists of the 6-DoF pose of the end effector as well as a 7$^{\text{th}}$ degree of freedom for continuous control of the parallel jaw gripper.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Setup and Method Overview", "weight": 1.0} -->

The policy is trained using a large-scale dataset collected via a VR-based teleoperation rig (see Figure 1, left) through a combination of direct demonstration and human-in-the-loop shared autonomy. In the latter, trained policies are deployed on the robot, and the human operator intervenes to provide corrections when the robot makes a mistake. This procedure resembles the human-gated DAgger (HG-DAgger) algorithm, and provides iterative improvement for the learned policy, as well as a continuous signal that can be used to track the policy's performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setup and Method Overview", "weight": 1.0} -->

The policy architecture is divided into an encoder $q{(\left. z \middle| w \right.)}$, which processes the command $w$ into an embedding $z \in \mathcal{Z}$, and a control layer $\pi$, which processes $(s,z)$ to produce the action $a$, i.e. $\pi:{{\mathcal{S} \times \mathcal{Z}}\rightarrow\mathcal{A}}$. This decomposition is illustrated in Figure 2, with further details in Section 5. It provides our method with the ability to incorporate auxiliary supervision, such as pretrained language embeddings, which help to structure the latent task space and facilitate generalization. In our experiments, we will show that this enables generalization to tasks that were not seen during training, including novel compositions of verbs and objects.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Data Collection and Workflow", "weight": 1.0} -->

In order for an imitation learning system to generalize to new tasks with zero demonstrations of said task, we must be able to easily collect a diverse dataset, provide corrective feedback, and evaluate many tasks at scale. In this section, we discuss these components of our system.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Data Collection and Workflow", "weight": 1.0} -->

System Setup. Our teleoperation system uses an Oculus VR headset which is attached to the robot's onboard computer via USB cable and tracks two handheld controllers. The teleoperator stands behind the robot and uses the controllers to operate the robot with a line-of-sight 3rd-person view. The robot responds to the operator's movement in a 10 Hz non-realtime control loop. The relatively fast closed-loop control allows the operator to demonstrate a wide range of tasks with ease and quickly intervene if the robot is about to enter an unsafe state during autonomous execution. Further details on the user interface and data collection are in Appendices A and B.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Data Collection and Workflow", "weight": 1.0} -->

Environment and Tasks. We place each robot in front of a table with anywhere from 6 to 15 household objects with randomized poses. We collect demonstrations and videos of humans for 100 pre-specified tasks (listed in Tables 7 and 8), which span 9 underlying skills such as pushing and pick-and-place. The model is then evaluated on 29 *new* tasks using a new language description or video of that task. For the method to perform well on these held-out tasks, it must both correctly interpret the new task command and output actions that are consistent with that task.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Data Collection and Workflow", "weight": 1.0} -->

Shared Autonomy Data Collection. Data collection begins with an initial expert-only phase, where the human provides the demonstration of the task from start-to-finish. After an initial multi-task policy is learned from expert-only data, we continue collecting demonstrations in "shared autonomy" mode, where the current policy attempts the task while the human supervises. At any point the human may take over by gripping an "override" switch, which allows them to briefly take full control of the robot and perform necessary corrections when the policy is about to enter an unsafe state, or if they believe the current policy will not successfully complete the task. This setup enables HG-DAgger, where intervention data is then aggregated with the existing data and used to re-train the policy. For the multi-task manipulation tasks, we collect 11,108 expert-only demonstrations for the initial policies, then collected an additional 14,769 HG-DAgger demonstrations covering 16 iterations of policy deployment, where each iteration deploys the most recent policy trained on the aggregated dataset. This gives a total of 25,877 robot demos. We find in Table 4 that when controlling for the same number of total episodes, HG-DAgger improves performance substantially.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data Collection and Workflow", "weight": 1.0} -->

Shared Autonomy Evaluation. When success rates are low, resources are best spent on collecting more data to improve the policy; but evaluation is also important to debug problems in the workflow. As the expected degree of generalization increases, we need more trials to evaluate the extent of policy generalization. This creates a resource trade-off: how should robot time be allocated between measuring policy success rates and collecting additional demonstrations to improve the policy? Fortunately, shared autonomy data collection confers an additional benefit: the intervention rate, measured as the average number of interventions required per episode, can be used as an indication for policy performance. In Figure 5, we find that the intervention rate correlates negatively with overall policy success rate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning Algorithm", "weight": 1.0} -->

The data collection procedure above results in a large multi-task dataset. For each task $i$, this dataset contains expert data ${(s,a)} \in \mathcal{D}_{e}^{i}$, human video data $w_{h} \in \mathcal{D}_{h}^{i}$, and one language command $w_{\ell}^{i}$. We now discuss how we use this data to train the encoder $q{(\left. z \middle| w \right.)}$ and the control layer $\pi{(\left. a \middle| {s,z} \right.)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Language and Video Encoders", "weight": 1.0} -->

Our encoder $q{(\left. z \middle| w \right.)}$ takes either a language command $w_{\ell}^{i}$ or a video of a human $w_{h}$ as input and produces a task embedding $z$. If the command is a language command, we use a pretrained multilingual sentence encoder ^11^1Checkpoint from as our encoder, producing a 512-dim language vector for each task. Despite the simplicity, we find that these encoders work well in our experiments.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Language and Video Encoders", "weight": 1.0} -->

When task commands are instead a video of a human performing the task, we use a convolutional neural network to produce $z$, specifically a ResNet-18 based model. Inspired by recent works, we train this network in an end-to-end manner. We collected a dataset of 18,726 videos of humans doing each training task, in a variety of home and office locations, camera viewpoints, and object configurations. Using paired examples of a human video $w_{h}^{i}$ and corresponding demonstration demo ${\{{(s,a)}\}}^{i}$, we encode the human video $z^{i} \sim q{( \cdot \mid w_{h}^{i})}$, then pass the embedding to the control layer $\pi{(\left. a \middle| {s,z^{i}} \right.)}$, and then backpropagate gradient of the behavior cloning loss to both the policy and encoder parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Language and Video Encoders", "weight": 1.0} -->

Visualizations of learned embeddings in Appendix E indicate that by itself, this end-to-end approach tends to overfit to initial object scenes, learn poor embeddings, and show poor task generalization. To help align the video embeddings more semantically, we therefore further introduce an auxiliary language regression loss. Concretely, this auxiliary loss trains the video encoder to predict the embedding of the task's language command with a cosine loss.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Language and Video Encoders", "weight": 1.0} -->

where $D_{\text{cos}}$ denotes the cosine distance. Since robot demos double as videos of the task, we also train encoded robot videos to match to the language vector. This language loss is critical to learning a more organized embedding space. Additional architecture and training details are in Appendix E.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Training", "weight": 1.0} -->

Given a fixed task embedding, we train $\pi{(\left. a \middle| {s,z} \right.)}$ via Huber loss on XYZ and axis-angle predictions, and log loss for the gripper angle. During training, images are randomly cropped, downsampled, and subjected to standard photometric augmentations. Below we describe two additional design choices that we found to be helpful. Additional training details such as learning rates, batch sizes, pseudocode, and further hyperparameters are discussed in Appendix D.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy Training", "weight": 1.0} -->

Open-Loop Auxiliary Predictions. The policy predicts the action the robot would take, as well as an open-loop trajectory of the next 10 actions the policy would take if it were operating in an open-loop manner. At inference time, the policy operates closed-loop, only executing the first action based on the current image. The open-loop prediction confers an auxiliary training objective, and provides a way to visually inspect the quality of a closed-loop plan in an offline manner (see Figure 1, right).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy Training", "weight": 1.0} -->

State Differences as Actions. In standard imitation learning implementations, actions taken at demonstration-time are used directly as target labels to be predicted from states. However, cloning expert actions at 10Hz resulted in the policy learning very small actions, as well as dithering behavior. To address this, we define actions as state differences to target poses $N > 1$ steps in the future, using an adaptive algorithm to choose $N$ based on how much the arm and gripper move. We provide ablation studies for this design choice in Section 6.3 and further details in Appendix C

<!-- chunk {"id": "body-0023", "role": "body", "section": "Network Architecture", "weight": 1.0} -->

We model the policy using a deep neural network, shown in Figure 3. The policy network processes the camera image with a "torso", which branches from the last mean-pool layer into multiple "action heads". Each head is a multilayer perceptron with two hidden layers of size 256 each and ReLU activations, and models part of the end-effector action, specifically the delta XYZ, delta axis-angle, and normalized gripper angle. The policy is conditioned on a 512-dim task embedding $z$, through FiLM layers. Following Perez et al., the task conditioning is linearly projected to channel-wise scales and shifts for each channel of each of the 4 ResNet blocks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Our experiments aim to evaluate BC-Z in large-scale imitation learning settings. We start with an initial validation of BC-Z on single-task visual imitation learning. Then, our experiments will aim to answer the following questions: Can BC-Z enable zero-shot and few-shot generalization to new tasks from a command in the form of language or a video of a human? Is the performance of BC-Z bottlenecked by the task embedding or by the policy? How important are different components of BC-Z, including HG-DAgger data collection and adaptive state diffs? We present experiments aimed at these questions in this section.

<!-- chunk {"id": "body-0025", "role": "body", "section": "BC-Z on Single-Task Imitation Learning", "weight": 1.0} -->

We first aim to verify that BC-Z can learn individual vision-based tasks before considering the more challenging multi-task setting. We choose two tasks: a bin-emptying task where the robot must grasp objects from a bin and drop them into an adjacent bin, and a door opening task where the robot must push open a door while avoiding collisions. Both tasks use the architecture in Figure 3, except that the door opening task involves predicting the forward and yaw velocity of the base instead of controlling the arm. The bin-emptying dataset has 2,759 demonstrations, while the door opening dataset has 12,000 demonstrations collected across 24 meeting rooms and 36,000 demonstrations across 5 meeting rooms in simulation. Further task and dataset details are in Appendix I.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Runs", "weight": 1.0} -->

In Table 1, we see that the BC-Z model is able to reach a pick-rate of 3.4 picks per minute, over half the speed of a human teleoperator. Further, we see that BC-Z reaches a success rate of $87\%$ on the training door scenes and $94\%$ on held-out door scenes. These results validate that the BC-Z model and data collect system can achieve good performance on both training and held-out scenes in the single-task setting. Additional analysis is provided in Appendix H.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

Next, we aim to test whether BC-Z can achieve generalization to new tasks. Demonstrations are collected across 100 different manipulation tasks, comprising two disjoint sets of objects. Using disjoint sets of objects allows us to specifically test generalization to combinations of object-object pairs and object-action pairs that are not seen together during training. For the first set of objects, demonstrations are collected across 21 different tasks, listed in Table 7, which cover a wide range of skills, from pick-and-place tasks to skills that require positioning the object in a certain way, like "stand the bottle upright". For the second set of objects, demonstrations are collected for 79 different tasks, including pick-and-place, surface wiping, and object stacking. The latter family has a smaller variety of manipulation behaviors, but is defined over a larger object set with more clutter. Object sets are shown in Appendix B and a full list of train task sentences are in Appendix J.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

We evaluate BC-Z on 29 held-out tasks. Language conditioned policies are given a novel sentence, while video conditioned policies are given the average embedding of a few human videos of the new task. Four held-out tasks use objects in the 79-task family, whereas 25 tasks are generated by mixing objects between the 21-task family and 79-task family. Thus, the first 4 held-out tasks do not require cross-object set generalization, so they are easier to generalize to. Even so, we find that each of these 4 tasks are sufficiently challenging that training single-task policies on 300+ held-out demos with DAgger interventions completely fails, achieving 0% task success. This provides a degree of calibration on the difficulty of these tasks. We hypothesize that a major contributing factor to this challenge is the wide range of locations, objects, and distractors that the skills must generalize to in our settings, as well as the wide range of these factors in the training data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

In Table 2, we see that language-conditioned BC-Z is able to generalize zero-shot to both kinds of held-out tasks, averaging at 32% success and showing non-zero success on 24 held-out tasks. Among the 24 hold-out tasks with non-zero success rates, BC-Z achieves an average success of 44% when conditioned on language embeddings it has never seen. When conditioning on videos of humans, we find that generalization is much more difficult, but that BC-Z is still able to generalize to nine novel tasks with a non-zero success rate, particularly when the task does not involve novel object combinations. Qualitatively, we observe that the language-conditioned policy usually moves towards the correct objects, clearly indicating that the task embedding is reflective of the correct task, as we further illustrate in the supplementary video. The most common source of failures are "last-centimeter" errors: failing to close the gripper, failing to let go of objects, or a near miss of the target object when letting go of an object in the gripper.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘place white sponge in purple bowl’

<!-- chunk {"id": "body-0031", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘place metal cup in red bowl’

<!-- chunk {"id": "body-0032", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘drag grapes across the table’

<!-- chunk {"id": "body-0033", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘wipe table surface with banana’

<!-- chunk {"id": "body-0034", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘wipe tray with white sponge’

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘wipe ceramic bowl with brush’

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘push purple bowl across the table’

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘push tray across the table’

<!-- chunk {"id": "body-0038", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

‘push red bowl across the table’

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

Is Performance Bottlenecked on the Encoder or the Policy? Now that we see that BC-Z can generalize to a substantial number of held-out tasks to some degree, we ask whether the performance is

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluating Zero-Shot and Few-Shot Task Generalization", "weight": 1.0} -->

limited more by the generalization of the encoder $q{(\left. z \middle| w \right.)}$, the control layer $\pi{(\left. a \middle| {s,z} \right.)}$, or both. To disentangle these factors, we measure the policy success rate on the training tasks conditioned in three ways: a one-hot task identifier, language embeddings of the training task commands, and video embeddings of held-out human videos of the training tasks. This comparison is in Table 3. The similar performance between one-hot and language suggests the latent language space is sufficient, and that language-conditioned performance on held-out tasks is bottlenecked on the control layer more than the embedding. The more significant drop in performance of video-conditioned policies suggests inferring tasks from videos is much more difficult, particularly for held-out tasks.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablation Studies and Comparisons", "weight": 1.0} -->

We validate the importance of several BC-Z design decisions using the (training) 21-task family. Our first set of ablations evaluate on the "place the bottle in ceramic bowl" command, which has the most demos of any task. We first test whether multi-task training is helpful for performance: we compare the multi-task system trained on 25,877 demos across all tasks, to a single-task policy trained on just the 1000 demos for the target task. In Table 4 (left), the single-task baseline achieves just 5% success. The low number is consistent with the low single-task performance on holdout tasks from Section 6.2: collecting data over several robots and operators likely makes the task harder to learn. Only when pooling data across many tasks does BC-Z learn to solve the task. We ablate the adaptive state diff scheme described in Section 5.3 and find that it is important; when naively choosing the $N = 1$ future state to compute the expert actions, the policy fits the noise and moves too slowly, resulting in state drift away from good trajectories.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablation Studies and Comparisons", "weight": 1.0} -->

We next ablate the use of HG-DAgger while keeping the total amount of data fixed. Specifically, we compare performance of policies trained using 50% expert demos and 50% HG-DAgger interventions, versus using 100% expert demos. In Table 4 (right), we find that HG-DAgger significantly improves task performance over cloning expert demonstrations on both the 'place bottle in ceramic bowl' task and 7 other training tasks. Further details on this comparison are in Appendix K. Finally, in Figure 5, we evaluate whether measuring HG-DAgger interventions can give us a live proxy of policy performance. We see that intervention frequency is inversely correlated with policy success, as measured by the fraction of successful episodes not requiring intervention. This result suggests that we can indeed use this metric with HG-DAgger for development purposes.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

We presented a multi-task imitation learning system that combines flexible task embeddings with large-scale training on a 100-task demonstration dataset, enabling it to generalize to entirely new tasks that were not seen in training based on user-provided language or video commands. Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes. The key conclusion of our empirical study is that simple imitation learning approaches can be scaled in a way that facilitates generalization to new tasks with zero additional robot data of those tasks. That is, we learn that we do not need more complex approaches to attain task-level generalization. Through the experiments, we also learn that 100 training tasks is sufficient for enabling generalization to new tasks, that HG-DAgger is important for good performance, and that frozen, pre-trained language embeddings make for excellent task conditioners without any additional training.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our system does have a number of limitations. First, the performance on novel tasks varies significantly. However, even for tasks that are less successful, the robot often exhibits behavior suggesting that it understands at least part of the task, reaching for the right object or performing a semantically related motion. This suggests that an exciting direction for future work is to use our policies as a general-purpose initialization for finetuning of downstream tasks, where additional training, perhaps with autonomous RL, could lead to significantly better performance. The structure of our language commands follows a simple "(verb) (noun)" structure. A direction to address this limitation is to relabel the dataset with a variety of human-provided annotations, which could enable the system to handle more variability in the language structure. Another limitation is the lower performance of the video-conditioned policy, which encourages future research on improving the generalization of video-based task representations and enhancing the performance of imitation learning algorithms as a whole, as low-level control errors are also a major bottleneck.
