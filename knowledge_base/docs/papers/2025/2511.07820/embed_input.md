<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

Topics include Robustness, Foundation models, Vision-language models, Datasets, Real-time systems, Control, SONIC, Vision-language-action, Vision-language-action model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the rise of billion-parameter foundation models trained across thousands of GPUs, similar scaling gains have not been shown for humanoid control. Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs over several days. We show that scaling up model capacity, data, and compute yields a generalist humanoid controller capable of creating natural and robust whole-body movements. Specifically, we posit motion tracking as a natural and scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual reward engineering. We build a foundation model for motion tracking by scaling along three axes: network size (from 1.2M to 42M parameters), dataset volume (over 100M frames, 700 hours of high-quality motion data), and compute (9k GPU hours).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Beyond demonstrating the benefits of scale, we show the practical utility of our model through two mechanisms: a real-time universal kinematic planner that bridges motion tracking to downstream task execution, enabling natural and interactive control, and a unified token space that supports various motion input interfaces, such as VR teleoperation devices, human videos, and vision-language-action (VLA) models, all using the same policy. Scaling motion tracking exhibits favorable properties: performance improves steadily with increased compute and data diversity, and learned representations generalize to unseen motions, establishing motion tracking at scale as a practical foundation for humanoid control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the past decade, artificial intelligence has scaled rapidly: the GPT family of models is trained on 25,000+ GPUs with trillions of tokens; video and image-generation models leverage thousands of GPUs processing billions of images. These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve. Yet for sim-to-real humanoid control, similar scaling gains have not been achieved. State-of-the-art humanoid control policies are often small neural networks, e.g., three-layer MLPs, trained on a few GPUs for a single task. Manually engineered reward terms are designed per task and do not generalize across behaviors, fundamentally limiting the scalability of these approaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Why hasn't humanoid control scaled? The fundamental issue is task selection. Tasks like locomotion require extensive reward engineering for each scenario---walking forward naturally provides little signal for dancing, getting up from the ground, or teleoperation. Each new capability demands redesigned rewards and objectives, making scaling up difficult. Generative imitation methods such as AMP, ASE, and CALM provide a unified objective by combining matching motion distributions and simple task-specific rewards, but prior work has shown that their discriminator-based training signal is prone to mode collapse as the motion dataset grows in size and diversity. Even if we identify a scalable objective that can learn diverse behaviors, a second challenge emerges: how do we support the diverse range of real-world applications? A desired humanoid controller should handle teleoperation, goal-directed tasks, navigation, and even vision-language commands. Building a system that scales while remaining flexible for different task specifications is non-trivial.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we address both challenges by identifying motion tracking as the scalable foundational task for humanoid control. Motion tracking leverages human motion capture data, which provides dense, frame-by-frame supervision without reward engineering. Critically, humanoids benefit from decades of motion capture research---datasets covering walking, running, dancing, sports, and object interactions already exist at scale. While there exist prior works on motion tracking, they are mostly limited to showing whole-body motion tracking results on training data and have not demonstrated many downstream tasks beyond motion tracking or navigation. We supersize physics-based motion tracking to 100 million frames (at 50 fps) with 128-GPU training, achieving universal tracking capabilities across diverse human behaviors while maintaining real-time performance. In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions. First, we develop a universal kinematic motion generation system for interactive control, enabling goal-directed tasks such as interactive locomotion and game-like character control through kinematic planning in motion space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we design a universal token space that unifies heterogeneous motion sources, including VR teleoperation, vision-language-action models, and generative motion models that convert video, text, and music into motion, within a single control interface.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications. We achieve high-precision teleoperation and interactive control capabilities, including running, jumping, and crawling with natural human-like movement. Leveraging our universal token space, our controller can directly map estimated whole-body human motion to humanoid control signals, bypassing the need for explicit retargeting at runtime. We integrate our tracking policy with multi-modal human motion generation models, supporting video, text, and music control. Furthermore, we show that teleoperation data collected through our system can be used to train vision-language-action foundation models, establishing a complete pipeline from motion tracking at scale to foundation model-based humanoid control, including tasks that demand simultaneous hand-foot coordination for whole-body loco-manipulation. These results validate that large-scale motion tracking serves as a practical foundational task for diverse real-world humanoid applications.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We identify motion tracking as a scalable foundational task for humanoid control, demonstrating that it exhibits favorable scaling properties with both compute and data diversity. We scale up humanoid control to 21,000 GPU hours and 100 million frames of motion sequences, achieving universal tracking capabilities across diverse human behaviors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a real-time kinematic motion generator for interactive control and a universal token space with specialized encoders for robot, human, and hybrid motion inputs, all mapped into a shared quantized representation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a comprehensive evaluation demonstrating humanoid control scaling trends, zero-shot transfer to unseen motions, robust sim-to-real deployment on physical humanoid robots, and successful integration with foundation models. We show that the universal token space enables VLA-driven whole-body loco-manipulation, including tasks requiring coordinated hand grasping and precise foot placement, across five real-world tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Results", "weight": 1.0} -->

We use the Unitree G1 humanoid to demonstrate our supersizing humanoid motion tracking framework, SONIC. Video results are available at the project website. We demonstrate SONIC's motion tracking capabilities (Sec.˜2.1), interactive kinematic motion planning (Sec.˜2.2), multi-modal control (Sec.˜2.3), teleoperation (Sec.˜2.4), and loco-manipulation (Sec.˜2.5), shown in Fig.˜1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motion Tracking", "weight": 1.0} -->

SONIC, trained on 100 million frames of motion over 21,000 GPU hours (128 GPUs over 7 days), exhibits strong generalization to unseen motions. In this section, we evaluate the generalization capabilities of our tracker on large-scale, unseen motion datasets in simulation and the real world.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Metrics", "weight": 1.0} -->

We employ a comprehensive set of pose-based and physics-based metrics to measure motion imitation performance. The primary measure is the success rate (Succ), where a motion imitation is deemed unsuccessful if the humanoid deviates too far from the reference motion trajectory. We further report the local (root-relative) mean per-joint position error (MPJPE-L) $E_{\text{mpjpe}}$ (in mm), computed over 14 body links (pelvis, knees, ankles, torso, elbows, wrists), quantifying the accuracy of the imitation in the robot's local frame. To assess physical fidelity, we also calculate differences in acceleration ($E_{\text{acc}}$, mm/frame^2^) and velocity ($E_{\text{vel}}$, mm/frame) between the simulated humanoid and the reference human motion.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Evaluation Protocol and Dataset", "weight": 1.0} -->

We evaluate on three test sets (Tab.˜2). From our motion-capture dataset, we construct two held-out splits: test-content (6,998 clips, 15 hours) tests generalization to *novel motion content*, containing 182 sub-categories entirely absent from training; test-repetition (6,306 clips, 12 hours) tests robustness to *new performances/repetitions* of known motion types. For baseline comparisons, we additionally evaluate on PHUMA, a publicly available dataset of 68,000 motions from a different retargeting pipeline. Motion imitation is considered unsuccessful if the humanoid's root height or end-effector height deviates by more than 0.25 m from the reference or if the root orientation differs by more than 1 radian. Unlike prior work that defines success via global root position error (e.g., 0.5 m threshold), our tracker performs *local* motion tracking rather than following a global trajectory. Our metric, similar to, captures the physically meaningful failure modes (e.g., falling). See Sec.˜3.1 for dataset details.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Scaling Up Motion Tracking", "weight": 1.0} -->

In Fig.˜2 (top row), we analyze scaling along three axes. For data size, we compare training on 4M, 10M, 22M, and 100M frames (corresponding to 20k, 50k, 110k, and 310k motion clips); smaller subsets are created by uniformly sampling across motion sub-categories to preserve distribution diversity. For model size, we scale from 1.2M to 16M to 42M parameters. For compute, we train on 2, 4, and 16 nodes (16, 32, and 128 GPUs), all to 50k iterations, yielding approximately 2K, 9K, and 21K GPU hours. All evaluations use Isaac Lab, with models trained 50k iterations (when performance usually plateaus). Scaling yields consistent improvements on both test-content (out-of-distribution, OOD) and test-repetition: the largest model achieves 99.6% success with 23.8 mm MPJPE on test-content, compared to 98.0% success with 27.7 mm for the smallest (1.2M). Gains are most pronounced on OOD motions, confirming that scale improves generalization.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Scaling Up Motion Tracking", "weight": 1.0} -->

For compute, more GPUs yield better asymptotic performance at the same iteration count, as larger batch sizes improve optimization stability. Shaded regions denote $\pm$`<!-- -->`{=html}1 standard deviation across 6 evaluation checkpoints. Visualizations of out-of-distribution test motions, including successful and failed tracking cases, are provided in the Supplementary Materials (Fig.˜S1). We also demonstrate robustness to strong external perturbations in Fig.˜S3.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Comparison with Other Motion Trackers", "weight": 1.0} -->

We compare against state-of-the-art trackers: GMT, Any2Track, and BeyondMimic. These baselines are trained on different source datasets (Any2Track and BeyondMimic on LaFAN; GMT on AMASS); for single-motion trackers like BeyondMimic, we retrain for multi-motion tracking using the publicly released code. To maximize protocol consistency, all methods are evaluated in MuJoCo under the same termination criterion defined before (Fig.˜2(d--g)). Because the methods are not trained on the same source data or retargeting pipeline, this comparison should be interpreted primarily as evidence of cross-dataset generalization and scaling effects rather than as a fully data-matched benchmark. Under this setting, SONIC achieves 98.7%/99.6%/97.0% success on test-content/test-repetition/PHUMA, compared to 81.6%/85.8%/73.4% for BeyondMimic and 31.1%/38.4%/58.6% for Any2Track.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Comparison with Other Motion Trackers", "weight": 1.0} -->

On tracking accuracy, SONIC achieves 23.2 mm MPJPE-L, a 41% reduction over BeyondMimic (39.1 mm). The 97.0% on PHUMA is particularly notable because PHUMA aggregates motions from video-based pose estimation with a different retargeting pipeline, making it substantially more out-of-distribution than our own held-out splits.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Comparison with Specialist Baseline", "weight": 1.0} -->

To show that a universal tracker can match or exceed specialist controllers, we compare SONIC against OpenHomie, a state-of-the-art single-task locomotion controller optimized for upper body inverse kinematics control and lower-body velocity tracking. We evaluate both systems on sim-to-sim velocity tracking in MuJoCo across the 0--5 m/s command range (Fig.˜2(h--j)). SONIC achieves a 98.5% overall survival rate compared to OpenHomie's 43.0%. OpenHomie's survival rate collapses beyond $\sim$`<!-- -->`{=html}1.5 m/s, dropping below 20%, while SONIC maintains near-100% stability up to $\sim$`<!-- -->`{=html}4 m/s. Notably, OpenHomie was specifically designed and trained for locomotion; SONIC's universal policy, trained on diverse whole-body motion data combined with a motion generator, outperforms it.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Real-World Evaluation", "weight": 1.0} -->

We assess the real-world performance of SONIC by deploying it on 123 diverse motion sequences (Fig.˜S2). As presented in Fig.˜2(k--l), our policy achieves motion imitation in the real world that closely matches its simulation results. The real-world policy achieves 99.2% success rate compared to 100% in simulation, with an overall MPJPE-L of 25.7 mm (vs. 22.3 mm in sim). The sim-to-real gap is smallest for the upper body (22.2 mm real vs. 21.8 mm sim) and largest for the feet (53.7 mm vs. 29.0 mm), reflecting the difficulty of precise foot placement under real-world contact dynamics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Interactive Motion Control", "weight": 1.0} -->

In this section, we demonstrate the scalability and robustness of SONIC in whole-body, real-time interactive control tasks. We present a kinematic runtime generative motion planner that guides the robot's policy through user interaction. Our approach employs an autoregressive framework that continually regenerates future kinematic motions conditioned on the previous states and incoming user commands. For each planning step, the model generates motion segments lasting between 0.8s and 2.4s, where the duration is automatically determined by the neural planner to maximize flexibility and robustness. The planner achieves inference times under 5 ms on a standard laptop and 12 ms on a Jetson Orin GPU. Replanning is triggered as frequently as every 100 ms, or immediately when user commands are updated, ensuring highly responsive control.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Interactive Motion Control", "weight": 1.0} -->

SONIC supports a variety of applications, including: navigation control with arbitrary velocity, direction, and style commands; interactive entertainment tasks such as boxing; locomotion skills such as squatting, crawling, kneeling, etc., which are useful for downstream applications like teleoperation, because both our kinematic planner and tracking policy are trained on the same large-scale dataset. Utilizing the scalable nature of SONIC, we note that all the applications above were specified after training, without retraining the planner or the tracking policy.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Interactive Motion Control", "weight": 1.0} -->

For navigation control, SONIC accepts velocity commands ranging from 0.0 m/s to 6.0 m/s, as well as arbitrary direction commands spanning 0 to 360 degrees. We note that 6.0 m/s represents the upper bound of the *command* range; the actual achievable velocity is limited by the tracker's capabilities and is filtered by a critically damped spring model (Sec.˜3.3). The actual commanded-vs-achieved velocity analysis is presented in Fig.˜2(h).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Interactive Motion Control", "weight": 1.0} -->

SONIC achieves scalable, responsive, and robust navigation control and supports different styles such as drunken walking, injured walking, happy walking, and stealth walking, as shown in the first two rows of Fig.˜3. The capacity of the model to generate robust inbetweening motions shows the flexibility of SONIC, and the potential for more natural human-robot interaction.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Interactive Motion Control", "weight": 1.0} -->

SONIC further extends its versatility to interactive entertainment tasks such as boxing, as illustrated in the last two rows of Fig.˜3. Existing academic solutions and industrial approaches often utilize a limited collection of boxing clips, requiring a switch between multiple expert models or action labels. This approach leads to discontinuous, unnatural transitions and even pauses. SONIC enables much more fluid, responsive, and natural motion generation while retaining the robot's full freedom of movement throughout the task.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Interactive Motion Control", "weight": 1.0} -->

To enable downstream manipulation or navigation in confined environments, skills such as squatting, kneeling, and crawling are essential. As illustrated in Fig.˜3, SONIC supports squatting, kneeling, and crawling. For squatting and kneeling, we allow the pelvis height to be smoothly controlled from 0.3 m to 0.8 m. For navigation in especially tight spaces, SONIC also enables crawling. The robot can move omnidirectionally using its elbows and knees at velocities from 0.0 m/s to 0.5 m/s.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Video Teleoperation and Multi-Modal Control", "weight": 1.0} -->

As shown in Fig.˜4 (top), SONIC also supports a real-time, multi-modal control framework, enabled by our universal control policy. A unified motion generation system based on GEM is designed to generate human motions from three input modalities: videos, natural-language commands, and music audio. The multi-modal motion generation system coordinates smooth transitions among modalities.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Video Teleoperation", "weight": 1.0} -->

For video control, the system supports both pre-recorded clips and live monocular webcam streams. Human motion is estimated at $\geq$ 60 frames per second (fps), enabling interactive teleoperation without specialized motion-capture hardware. Video control provides a higher-fidelity specification of pose and timing, yielding a precise imitation of movements.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Music and Text Control", "weight": 1.0} -->

For text control, the system accepts natural-language prompts and synthesizes target motions at $\geq$ 60 fps. An interactive graphical interface supports free-form prompting at any time with immediate on-robot responses (for example, "walk forward", "kick left foot", or "dance like a monkey"). For music control, GEM generates dance motions (which our tracking policy imitates) conditioned on melodic and rhythmic structure, tempo, and musical characteristics. Our system supports transitions between modalities. For example, users can initiate fine-grained control via video, switch to text for general control, and finally hand off to music for performance.

<!-- chunk {"id": "body-0031", "role": "body", "section": "VR-Based Teleoperation", "weight": 1.0} -->

We build two VR teleoperation interfaces on top of SONIC. *Whole-body teleoperation* uses a PICO headset, ankle trackers, and handheld controllers to stream full-body SMPL poses, encoded via the human motion encoder ${\mathcal{E}}_{h}$. *3-point teleoperation* uses only the headset and controllers (no ankle trackers), outputting three upper-body SE poses (head, both wrists), finger joints, waist height, and a navigation command; the kinematic planner generates the lower body. Both interfaces use the same universal token space; video-based teleoperation is also supported (Sec.˜2.3). We use the VR teleoperation interfaces to collect teleoperation data for training VLA foundation models. Full interface details are provided in the Supplementary Materials (Sec.˜S8).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

We connect a GR00T N1.5 VLA model to the universal token interface, enabling autonomous whole-body control (Fig.˜5, Tab.˜1). We evaluate on five loco-manipulation tasks of increasing complexity. The first task (apple to plate) uses the 3-point interface; the remaining four use the whole-body interface, where the VLA predicts a 78-dimensional action comprising a 64-dimensional universal motion token and 14-dimensional hand joints. We observe that predicting universal tokens produces smoother and safer behavior than predicting explicit SMPL poses, which result in jerky motions and poor directional control (see Sec.˜3.6 for an ablation). All success rates are strict binary outcomes over 10--20 trials per task (Tab.˜1).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

Apple to plate (3-point interface): The robot walks to a table, picks up an apple, and places it on a plate. Trained on 300 trajectories, achieving 90% success over 20 trials.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

Object pickup (carrot, scrub; whole-body interface): The robot walks to a table, locates a target object, and grasps it under randomized table heights (24--30 inches) and starting positions. Trained on 3,900 trajectories (300 per object, 13 objects), the policy achieves 75% (carrot) and 95% (scrub) success.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

Open trash can (whole-body interface): The robot navigates to a trash can and steps on a pedal to open the lid, requiring precise foot placement and dynamic single-leg balance under closed-loop VLA control. Trained on 200 trajectories, achieving 70% success. This task requires the VLA to coordinate full-body dynamics, using feet as manipulators.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

Soda can to trash can (whole-body interface): The most complex task, combining five sequential skills: walk to the table, pick up the can with one hand, navigate to the trash can, open the lid by stepping on the pedal with one foot while balancing on the other, and throw the can inside. This requires simultaneous hand manipulation, foot manipulation, and dynamic balance within a single action sequence. Trained on 1,000 multi-object trajectories, achieving 60% success.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

Drill and box relocation (whole-body interface): A multi-stage task where the robot picks up a drill, places it in a box, and carries the box to a shelf with both hands. Trained on 300 trajectories, achieving 70% success.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Foundation-Model-Driven Loco-manipulation", "weight": 1.0} -->

Across all five tasks (10--20 trials each), the VLA achieves 75% average success using the universal token action space. The soda-can and trash-can tasks illustrate autonomous whole-body loco-manipulation with coordinated hand and foot placement, a capability that would be difficult to realize with action spaces that decouple upper-body control from locomotion.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

We cast motion tracking as a scalable task for learning a single, versatile humanoid controller. By training SONIC on 100 million+ motion frames with up to 128 GPUs, we obtain a single policy that produces natural, robust whole-body behaviors across diverse conditions. Equally important, we build the practical system that makes tracking usable in real deployments: a real-time kinematic motion planner that converts intent into short-horizon reference motions, and a universal token space that unifies heterogeneous interfaces (teleoperation, video, text, and music) within one policy.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

We observe consistent improvements as data, model capacity, and compute increase, with generalization to unseen motions in simulation and real-world deployments. These findings support motion tracking as a practical route to acquire broad, transferable whole-body priors without per-task reward engineering.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Why does motion tracking scale", "weight": 1.0} -->

We attribute the favorable scaling properties of motion tracking to its dense, per-frame supervisory signal. Each training frame provides an explicit target pose, so the learning signal remains informative as the dataset grows in size and diversity. This stands in contrast to adversarial imitation methods (AMP, ASE ), where a discriminator must distinguish real from generated motions across the full distribution; as diversity increases, the discriminator's task becomes harder and its feedback less informative, leading to mode collapse. It also contrasts with task-specific reward engineering (e.g., locomotion controllers like OpenHomie ), where each behavior requires a tailored objective that does not generalize. Our comparison with OpenHomie demonstrates this concretely: even on velocity tracking, SONIC's universal tracker achieves 98.5% survival versus OpenHomie's 43.0%, showing that data diversity benefits a universal tracker more than specialization benefits a narrow one. Furthermore, OpenHomie's velocity tracking performance plateaus when scaling beyond 8 GPUs (Fig.˜S4), whereas SONIC continues to improve with additional compute.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Why does motion tracking scale", "weight": 1.0} -->

Since the token space represents the full body, VLAs can control the entire kinematic chain, including the feet. Our VLA experiments demonstrate tasks requiring coordinated hand grasping and precise foot placement within a single action sequence.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Why does motion tracking scale", "weight": 1.0} -->

Limitations include the lack of formal treatment of safety and energy efficiency for extended deployments. The tracker is robust to noisy planner output through domain randomization on motion commands during training and the critically damped spring model that filters unrealistic commands at deployment, but under more extreme conditions or very dynamic motions, the tracker may lose balance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Why does motion tracking scale", "weight": 1.0} -->

In summary, scaling motion tracking yields reliable, general whole-body control; pairing it with a planner, a universal token space, and an efficient onboard stack makes it usable as a system. We expect SONIC to serve as a practical foundation upon which higher-level perception and reasoning can be built to advance general-purpose humanoid autonomy.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Study Design", "weight": 1.0} -->

We evaluate whether physics-based motion tracking scales favorably with data, model size, and compute for humanoid whole-body control. We train policies in simulation (Isaac Lab ) and test them in both simulation and the real world. We systematically vary data size, model size, and compute (Sec.˜2.1) and evaluate on three held-out test sets with predefined splits (Tab.˜2): two from our dataset (test-content, test-repetition) and one external benchmark (PHUMA). Scaling curves report mean $\pm$`<!-- -->`{=html}1 standard deviation across 6 evaluation checkpoints per configuration. Real-world evaluation covers 123 motion sequences (one trial per sequence). VLA task success rates (Tab.˜1) are measured over 10--20 trials per task. All training runs use the same hyperparameters (Tab.˜S2) and reward function (Tab.˜S3).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Humanoid Motion Dataset", "weight": 1.0} -->

Our motion dataset is built from a large-scale motion-capture collection with a balanced mix of male and female performers. The dataset spans a broad spectrum of everyday human behaviors, including locomotion, daily activities, gesturing, and a diverse set of combat motions with varied stylistic expressions. Clip durations range from 1 to 180 seconds. In total, the collection covers thousands of unique motion behaviors, with most actions performed by multiple subjects across multiple takes, providing rich intra- and inter-subject variation, as can be seen in Fig.˜6. The source dataset contains approximately 700 hours of human motion. After retargeting to the Unitree G1 using GMR and PyRoki, we filter out physically implausible motions (e.g., stair climbing, seated activities) that cannot be executed on the target robot, yielding 611 hours of training data (100+ million frames at 50 Hz).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Dataset Diversity and Splits", "weight": 1.0} -->

The dataset spans 33 motion categories (Tab.˜2), including basic and advanced locomotion, dance (hip-hop, Latin, vogue, fila), gestures, combat (sword, martial arts, magic), object manipulation (one-handed and two-handed at varying heights and object sizes), tool use (valves, levers, chainsaws, brooms), injured-gait, stylistic variations (drunk, zombie, stealth), role-play, and more. Each motion is captured from multiple subjects and is mirrored, yielding paired left/right variants. We construct explicit train/test splits to enable rigorous evaluation (Tab.˜2). The training set covers 8,447 unique motion sub-categories (611 hours). The test-content split isolates *novel motion content* (sub-categories entirely absent from training), while test-repetition isolates *novel repetitions* of known content (different takes and actor performances).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Public Data Release", "weight": 1.0} -->

A substantial portion of our motion-capture dataset has been publicly released as the BONES-SEED dataset, available on Hugging Face. BONES-SEED contains 142,220 annotated motion sequences (288 hours) from 522 actors in SOMA and Unitree G1 formats, with natural language descriptions, temporal segmentation labels, and actor information.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Public Data Release", "weight": 1.0} -->

Combat (sword, martial arts, etc.)

<!-- chunk {"id": "body-0050", "role": "body", "section": "Universal Humanoid Motion Tracking", "weight": 1.0} -->

Fig.˜7 provides an overview of our approach, SONIC, a universal humanoid motion tracking framework that employs a unified control policy to track diverse motion commands from multiple input formats. A key innovation is its ability to seamlessly handle robot motion, human motion, and hybrid motion (combining upper-body keypoints with lower-body robot motions) through a shared latent representation. We use various motion generators (kinematic motion planner, VR motion generator, human motion generator (GEM)) to generate motion commands, which enable diverse applications including interactive gamepad control, VR 3-point teleoperation, whole-body teleoperation, video-based teleoperation, and multi-modal control from text and music.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Motion Tracking Formulation", "weight": 1.0} -->

We formulate humanoid motion tracking as a Markov Decision Process $\mathcal{M} = {\langle{\mathcal{S}},{\mathcal{A}},{\mathcal{T}},\mathcal{R},\gamma\rangle}$, comprising state space, action space, transition function, reward function, and discount factor $\gamma$. We train the policy using proximal policy optimization (PPO) to maximize the expected cumulative discounted return ${\mathbb{E}}\left\lbrack {\sum_{t = 1}^{T}{\gamma^{t - 1}r_{t}}} \right\rbrack$. Our environment design follows the general motion tracking formulation, and we adapt the well-tuned environmental settings from as the basis for scaling up humanoid motion tracking.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Motion Tracking Formulation", "weight": 1.0} -->

The motion command ${\mathbf{s}}_{t}^{\text{g}}$ has three types: robot motion ${\mathbf{g}}_{r}$, human motion ${\mathbf{g}}_{h}$, or hybrid motion ${\mathbf{g}}_{m}$ (combining upper-body keypoints with lower-body robot motions), where we drop the subscript $t$ for brevity. All state quantities are expressed in the robot's local frame to ensure rotation invariance. We use the 6D rotation representation throughout.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Motion Tracking Formulation", "weight": 1.0} -->

Actions. The policy $\pi$ outputs target joint positions ${\mathbf{a}}_{t}$ as actions, which are tracked by proportional-derivative (PD) controllers at each joint. For PD gain settings, we follow prior art Raibert and Farshidian; Liao et al. that has proven effective in training high-quality tracking policies.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Motion Tracking Formulation", "weight": 1.0} -->

Rewards. We define the reward as $r_{t} = {{\mathcal{R}{({\mathbf{s}}_{t}^{\text{p}},{\mathbf{s}}_{t}^{\text{g}})}} + {\mathcal{P}{({\mathbf{s}}_{t}^{\text{p}},{\mathbf{a}}_{t})}}}$, combining tracking reward and penalty terms. The tracking term $\mathcal{R}$ minimizes errors in root position, root orientation, body link positions (relative to the root), body link orientations (relative to the root), body link linear velocities, and body link angular velocities between the robot state ${\mathbf{s}}_{t}^{\text{p}}$ and the target ${\mathbf{s}}_{t}^{\text{g}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Motion Tracking Formulation", "weight": 1.0} -->

We additionally include an end-effector position reward that directly optimizes end-effector position errors on key body points (head, both wrists, both ankles). We also include anti-shake (angular velocity on the head and wrists) and foot acceleration penalties to encourage smooth foot contacts. Detailed reward design is presented in Table S3.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Motion Tracking Formulation", "weight": 1.0} -->

Domain Randomization. To enhance robustness and generalization across diverse scenarios, we apply systematic domain randomization during training. We randomize physical parameters, which include friction coefficients ($\mu_{s}$, $\mu_{d}$), the restitution coefficient ($e$), first-frame joint positions (${\mathbf{q}}_{0}$), and the base center-of-mass position. We also periodically apply random perturbations to the robot's root linear and angular velocities to simulate external pushes. Additionally, we apply motion perturbation to the target motion commands ${\mathbf{s}}_{t}^{\text{g}}$ during training to improve robustness. All domain randomization parameters are detailed in Table S4.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Universal Control Policy", "weight": 1.0} -->

A distinguishing characteristic of our tracking framework is its ability to accommodate multiple motion command types from different embodiments through a unified encoder-decoder architecture. We accomplish this via specialized encoders that process heterogeneous inputs from both human and robot motion formats into a shared latent representation. This representation undergoes quantization to yield a universal token, which subsequently drives a common robot control decoder to generate motor commands. This design enables the policy to leverage motion data from diverse sources---both robot demonstrations and human motion---allowing the robot to imitate human movements despite morphological differences. An auxiliary robot motion decoder is also used to facilitate feature learning and serve as an implicit retargeting module from human to robot embodiment.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Universal Control Policy", "weight": 1.0} -->

Encoders. Three specialized encoders process distinct motion command types: robot motion encoder ${\mathcal{E}}_{r}$ encodes robot joint positions and velocities over $F_{r}$ future frames with a frame interval $\Deltat_{r}$, human motion encoder ${\mathcal{E}}_{h}$ encodes 3D human joint positions over $F_{h}$ future frames with a frame interval $\Deltat_{h}$, and hybrid motion encoder ${\mathcal{E}}_{m}$ encodes sparse upper-body keypoints (head and hands) of the current frame (for real-time upper-body tracking), combined with lower-body robot motion over $F_{m}$ future frames with a frame interval $\Deltat_{m}$. Multi-frame inputs enable anticipatory behavior and improve the robustness of the policy.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Universal Control Policy", "weight": 1.0} -->

All encoders are implemented as multi-layer perceptrons (MLPs; architecture details in Table S1) that map commands ${\mathbf{g}}_{r},{\mathbf{g}}_{h},{\mathbf{g}}_{m}$ into a shared latent space, enabling aligned representations across input modalities.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Universal Control Policy", "weight": 1.0} -->

Quantizer. The encoded latent representation is quantized into a universal token $\mathbf{z}$ using a vector quantizer. Specifically, we use Finite Scalar Quantization (FSQ) as our vector quantizer. We use two tokens, each a $D_{z}$-dimensional vector with $L_{z}$ quantization levels per dimension. We choose FSQ over VQ-VAE because FSQ avoids codebook collapse (a failure mode where large portions of the codebook go unused), requires no auxiliary commitment loss or codebook EMA updates, and provides clean straight-through gradient estimation that is compatible with joint PPO optimization. We validate these design choices in Sec.˜3.6, including FSQ vs. VQ-VAE, quantizer configuration (levels and dimensions), and multi-encoder alignment.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Universal Control Policy", "weight": 1.0} -->

Decoders. The universal token $\mathbf{z}$ is decoded through two separate decoders. First, a robot control decoder ${\mathcal{D}}_{c}$ transforms the universal token into motor commands that control the robot's joints. ${\mathcal{D}}_{c}$ takes as input the concatenation of the universal token $\mathbf{z}$ and the proprioceptive state ${\mathbf{s}}_{t}^{\text{p}}$, i.e., ${\mathbf{a}}_{t} = {{\mathcal{D}}_{c}{({\mathbf{z}},{\mathbf{s}}_{t}^{\text{p}})}}$, where all quantities are expressed in the local frame as defined above. The same input representation is used identically during training in simulation and real-world deployment.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Universal Control Policy", "weight": 1.0} -->

Second, a robot motion decoder ${\mathcal{D}}_{r}$ reconstructs the robot motion command, providing auxiliary supervision to improve the latent space and enhance feature learning. ${\mathcal{D}}_{r}$ takes only the universal token as input, i.e., ${\hat{\mathbf{g}}}_{r} = {{\mathcal{D}}_{r}{({\mathbf{z}})}}$. Both decoders are implemented as MLPs (Table S1).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Training", "weight": 1.0} -->

We prepare synchronized motion data across all three command types. Each command type ${\mathbf{g}}_{r},{\mathbf{g}}_{h},{\mathbf{g}}_{m}$ is encoded via its respective encoder and quantized to produce universal tokens ${\mathbf{z}}_{r},{\mathbf{z}}_{h},{\mathbf{z}}_{m}$. For each token, the control decoder ${\mathcal{D}}_{c}$ generates motor commands, while the motion decoder ${\mathcal{D}}_{r}$ reconstructs the robot motion command.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Training", "weight": 1.0} -->

where $\mathcal{L}_{\text{ppo}}$ denotes the standard PPO loss. $\mathcal{L}_{\text{recon}}$ represents the reconstruction loss for the robot motion command across different input modalities. Notably, when the input command is human motion ${\mathbf{g}}_{h}$, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and $\mathcal{L}_{\text{recon}}$ serves as a retargeting loss that enables learning from human motion data. $\mathcal{L}_{\text{token}}$ enforces pairwise alignment between all three encoder outputs, ensuring that the same motion produces similar tokens for robot motion, human SMPL poses, or hybrid teleop commands when the source motion is the same.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Training", "weight": 1.0} -->

$\mathcal{L}_{\text{cycle}}$ is a cycle consistency loss between the original robot token ${\mathbf{z}}_{r}$ and the token produced by re-encoding the reconstructed robot motion from the human token, i.e., ${\mathcal{E}}_{r}{({{\mathcal{D}}_{r}{({\mathbf{z}}_{h})}})}$. This loss further reinforces latent space coherence, ensuring that the translation from human to robot motion and back preserves the essential motion characteristics.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Training", "weight": 1.0} -->

All four losses are optimized jointly in a single end-to-end training loop. We use asymmetric actor-critic training: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and noise-free observations) during training, while the actor operates solely on deployment-available observations (noisy proprioceptive sensing and motion commands). The PPO loss updates the encoders, quantizer, and control decoder ${\mathcal{D}}_{c}$ (as well as the critic network); the reconstruction, token alignment, and cycle consistency losses update the encoders, quantizer, and motion decoder ${\mathcal{D}}_{r}$. Gradients propagate through the FSQ quantizer via straight-through estimation, allowing PPO to shape the encoder representations. In practice, the auxiliary losses regularize the latent space by enforcing multi-encoder alignment and reconstruction fidelity, which stabilizes PPO optimization rather than destabilizing it. We did not observe training instabilities from the coupling of quantization with RL in any of our experiments across model scales.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Training", "weight": 1.0} -->

We employ bin-based adaptive motion sampling that partitions the dataset into fixed-duration bins and weights sampling by capped failure rates, balancing targeted practice on challenging motions with uniform coverage. We train using distributed training powered by Gugger et al. and von Werra et al. across multiple compute nodes in Isaac Lab. Training hyperparameters are provided in Table S2.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Tasks and Applications", "weight": 1.0} -->

The multi-encoder design enables diverse applications through the same policy: interactive gamepad control via the kinematic planner and ${\mathcal{E}}_{r}$; VR whole-body and 3-point teleoperation via ${\mathcal{E}}_{h}$ and ${\mathcal{E}}_{m}$ respectively; VLA-driven autonomous control by predicting universal tokens (Sec.˜2.5); and multi-modal control (video, text, music) via GEM and ${\mathcal{E}}_{h}$ (Sec.˜3.4).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Generative Kinematic Motion Planner", "weight": 1.0} -->

Our generative kinematic motion planner is a large-scale latent generative model, trained on the same natural whole-body motion data as the motion tracking policy. At a high level, the planning process is formulated as an autoregressive motion in-betweening generation task. The context keyframes capture historical robot states, such as joint positions and root positions, while target keyframes are either navigation guidance keyframes generated from user commands such as velocity, direction, and style, or skill-specific targets for actions such as squatting, crawling, boxing, etc.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Motion Representation", "weight": 1.0} -->

During training, we sample motion segments of length between 0.8s and 2.4s, extracting the keyframes at both endpoints to serve as the context and target keyframes. Our motion representation is mathematically equivalent to the humanoid pose configuration $q_{t}$ as introduced in Sec.˜3.2. Specifically, we represent kinematic motion using the pelvis-relative joint positions and global joint rotations. During training, we randomly rotate the training samples to enable planning in all initial orientations. Incorporating global rotation instead of local, canonicalized rotation is essential for generating motions such as squatting and crawling, where the notion of heading is ill-defined and affects the quality of motion planning. We refer readers to Meng et al. and Meng et al. for similar insights and additional discussion.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Generative Neural Backbone in Latent Space", "weight": 1.0} -->

where $p_{t}$ and $r_{t}$ denote the pose configuration and root position at frame $t$, respectively. In practice, the encoder operates with a downsampling rate of 4. The latent token sequence is encoded by models such as Transformers or Conv1D networks to capture temporal consistency.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Generative Neural Backbone in Latent Space", "weight": 1.0} -->

The inbetweening process in the token space is guided by two constraints: the starting and target keyframes, denoted as $\left\{ p_{t},r_{t} \right\}_{t = 1}^{4}$ and $\left\{ p_{t},r_{t} \right\}_{t = {T - 4}}^{T}$ respectively. Rather than training the network to predict the entire sequence of tokens from these sparse constraints in a single pass, we adopt a masked token prediction approach.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Generative Neural Backbone in Latent Space", "weight": 1.0} -->

This process is iterative, in which $\mathcal{F}{( \cdot )}$ denotes the neural backbone, and $h$ represents the logits for each token position. Token probabilities are computed by applying a softmax function $\sigma{( \cdot )}$ to the logits. At the first iteration, all latent tokens are unknown, and we initialize the latent embedding with a learnable mask embedding, $z_{\text{masked}}$. During training, the proportion of masked tokens is uniformly sampled from the range $\lbrack{100\%},{0\%}\rbrack$. During inference, a cosine schedule determines the proportion of tokens to finalize at each iteration, specifically $1.0 - {\cos\left( {\frac{\pi}{2} \cdot \frac{L}{L_{\max}}} \right)}$, where $L$ is the current iteration and $L_{\max}$ is the maximum number of iterations.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Generative Neural Backbone in Latent Space", "weight": 1.0} -->

After finalization of all tokens, the predicted tokens are used to reconstruct the kinematic motions and generate the robot control signals.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Root trajectory spring model", "weight": 1.0} -->

where $x_{T}$ denotes the target value, $x_{0}$ the initial value, $v_{0}$ the initial velocity, and $c$ the damping coefficient. We apply this critically damped spring model to three quantities: 1) the pelvis position along the x-axis, 2) the pelvis position along the y-axis, and 3) the projected heading angle of the pelvis. Damping coefficients of $5{\ln{}}$ and $20{\ln{}}$ are used for position and heading respectively. The target values may be obtained directly from the controllers. Alternatively, if the controller only specifies a desired velocity, we can compute the expected target positions after 1.0s using the desired velocity. The target keyframes are then placed at the position and heading with $x{(1.0)}$, as computed by the spring model in Eq.˜8. In practice, we find that our generative kinematic motion planner is robust to the choice of damping coefficients.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Root trajectory spring model", "weight": 1.0} -->

In fact, the spring model could often be omitted entirely, as the planner's ability to generate motions of variable length (ranging from 0.8s to 2.4s) and its strong inbetweening capability make it adaptable to a wide range of root trajectory commands. Nevertheless, incorporating the spring model improves behavioral predictability and helps safeguard against unrealistic commands, such as abruptly reversing direction from 6.0 m/s to $-$`<!-- -->`{=html}6.0 m/s.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Keyframe Module and Application Integration", "weight": 1.0} -->

Traditional motion planning methods often rely on complex target keyframe generation, such as detailed footstep planning. In contrast, our system provides keyframes in a more intuitive manner, requiring limited manual effort for keyframe specification.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Keyframe Module and Application Integration", "weight": 1.0} -->

For navigation control, target keyframes are generated by placing a randomly selected segment from the navigation clips of the desired style at the target root trajectory. Despite this simplicity, our model consistently produces natural and smooth motions that align well with the specified style. We attribute this to the model's flexible, variable-length motion generation and its robust inbetweening capabilities. Additionally, the autoregressive replanning ensures that the generated motion is continually refreshed before reaching the end of any given clip, thus minimizing dependence on the specific spatial details of the chosen target keyframes. This approach generalizes to other motion styles such as walking, running, and crawling.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Keyframe Module and Application Integration", "weight": 1.0} -->

For entertainment tasks such as boxing, target keyframes are determined by selecting the most expressive segment (e.g., the frames with maximal arm extension for a punch) from motion clips that match the desired style. We also support motion layering, where the upper body is specified and the lower body is generated accordingly by the planner, enabling predefined behaviors.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Keyframe Module and Application Integration", "weight": 1.0} -->

For interactive modes needed in manipulation tasks, such as squatting or kneeling, keyframes are retrieved online from the motion clip library according to the desired height. Unlike traditional approaches that require an extensive motion library, our system needs only a single clip to generate the full distribution of transitional motions for a given skill.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Multi-modal Motion Generation", "weight": 1.0} -->

For multi-modal control (video, text, music), we adopt GEM, a unified generalist model that handles both motion estimation and generation by treating estimation as constrained generation. GEM accepts mixed, time-varying conditions (text, audio, video) and produces human motion sequences via a diffusion-based prior. We integrate GEM with our system using sliding windows with overlap and inpainting-based transitions for low-latency generation. The generated human motions are fed into SONIC via the human motion encoder ${\mathcal{E}}_{h}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Deployment", "weight": 1.0} -->

Experiments are conducted on a Unitree G1 platform (29 actuated joints). All inference runs *onboard* a Jetson Orin GPU using TensorRT with CUDA Graph acceleration, yielding 1--2 ms per policy forward pass and $\sim$`<!-- -->`{=html}12 ms for motion generation. The system uses a multi-rate architecture with four concurrent loops: policy inference at 50 Hz, command streaming at 500 Hz, operator input at 100 Hz, and kinematic planning at 10 Hz. The encoder-decoder design allows seamless switching between input interfaces (keyboard, gamepad, VR, network streams) by changing the active encoder, with no retraining required. All real-world experiments deploy the largest model (42M parameters). Full deployment details, including the multi-rate architecture, observation gathering pipeline, safety mechanisms, and usage modes, are provided in the Supplementary Materials (Sec.˜S7, Fig.˜S5). Code is available at

<!-- chunk {"id": "body-0083", "role": "body", "section": "Validation of Key Design Choices", "weight": 1.0} -->

In this section, we validate key design choices through ablations on the test-content (out-of-distribution) and test-repetition splits (Tab.˜4), a VLA action space comparison (Tab.˜3), latent space alignment analysis (Fig.˜8), and kinematic planner validation.

<!-- chunk {"id": "body-0084", "role": "body", "section": "FSQ Tokens vs. Explicit Poses for VLA", "weight": 1.0} -->

A key motivation for quantization is downstream VLA learning. We compare two action spaces (Tab.˜3): the VLA predicts FSQ tokens (78-dim: 64-dim token + 14-dim hands), decoded by the universal control policy, vs. the VLA directly predicts SMPL whole-body poses and hand joints (81-dim total). FSQ tokens outperform SMPL by +42 percentage points on average (68% vs. 27%), with the gap widening on complex tasks (60% vs. 0% on soda-can-to-trash-can). We attribute this to the compactness of the quantized latent space: FSQ tokens provide a low-dimensional, discrete action space that is easier for the VLA to learn from teleoperated demonstrations, whereas the high-dimensional continuous SMPL pose space amplifies small prediction errors into large tracking failures.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Quantizer Design and Configuration", "weight": 1.0} -->

We choose Finite Scalar Quantization (FSQ) over VQ-VAE because FSQ avoids codebook collapse, a failure mode where large portions of a learned codebook are unused. Under our diverse motion distribution (33 categories, 8,447 sub-categories), this is a significant concern. For a fair comparison, we use a multi-head VQ-VAE with comparable capacity (4 heads, codebook size 512, 2 tokens). As shown in Tab.˜4(a), FSQ outperforms VQ-VAE by 8.7 mm MPJPE-L on test-content. We also study the effect of quantizer capacity (Tab.˜4(b)) by varying per-token levels and dimensions (all configurations use two tokens). Due to compute constraints, this sweep is run on 32 GPUs rather than 128. For example, FSQ-16-16 denotes 16 quantization levels and 16 dimensions per token. Increasing capacity consistently improves performance, with token dimension having a larger effect than quantization levels, suggesting that representational capacity matters more than quantization granularity for diverse motion tracking.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Quantizer Design and Configuration", "weight": 1.0} -->

We use FSQ-32-32 as our default configuration throughout the paper.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Quantizer Design and Configuration", "weight": 1.0} -->

(b) FSQ configurations (32 GPUs, 2 tokens each)

<!-- chunk {"id": "body-0088", "role": "body", "section": "Multi-Encoder Performance and Consistency Losses", "weight": 1.0} -->

Our multi-encoder design maps three heterogeneous input types (robot motion, human SMPL poses, and hybrid teleop commands) into a shared token space, aligned by the consistency losses $\mathcal{L}_{\text{token}}$ and $\mathcal{L}_{\text{cycle}}$. As shown in Tab.˜4(c), all three encoders maintain $>$`<!-- -->`{=html}99.2% success, with the human encoder showing only a +0.6 mm MPJPE-L gap from the robot encoder despite operating on a different input format. The hybrid encoder shows a larger MPJPE-L (26.5 mm, +2.7 mm from the robot encoder) due to partial observability (only sparse upper-body keypoints). Removing the consistency losses causes an $8 \times$ increase in cross-encoder divergence (Fig.˜8), confirming they are necessary for cross-encoder alignment.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Multi-Encoder Performance and Consistency Losses", "weight": 1.0} -->

This alignment is critical for downstream VLA learning: since the VLA directly predicts tokens, teleoperation data collected via different encoders (human, hybrid, or robot) should occupy the same latent space to provide the VLA with a consistent training distribution.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Role of the Kinematic Motion Planner", "weight": 1.0} -->

The kinematic planner (Sec.˜3.3) is an application layer that converts high-level user intent into short-horizon kinematic references. While the tracker is source-agnostic and compatible with alternative planners, ours unifies 25+ distinct skills and styles with a single real-time generative model, each requiring only one representative motion clip and no retraining. The tracker is independently validated on pre-recorded reference motions (Sec.˜2.1), and its robustness extends to planner-generated references through domain randomization on motion commands during training and the spring model that filters unrealistic commands at deployment.
