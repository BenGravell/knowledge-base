<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MolmoAct2: Action Reasoning Models for Real-world Deployment

Topics include Robotics, Vision-language models, Datasets, Benchmarks, Control, MolmoAct2, Action reasoning, Real-world, Deployment, Vision-language-action, Vision-language-action model, Together with quality-filtered Franka, DROID.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Physical intelligence is fundamentally organized around perception and action. Rather than reasoning over abstract internal computation, human think by constructing spatial representations, simulating actions, and interacting with the world through their bodies. Although we conflate today's robot foundation models as displaying such intelligence; from a cognitive science perspective, they remain incomplete models of intelligence. They often lack structured spatial representations Qu et al., rely on heavyweight internal reasoning processes that impede real-time interaction, and are difficult to adapt or extend due to limited openness.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work has shown promise that reasoning processes improve performance but the improvements come at the cost of high inference latency. Recent systems including MolmoAct and others have shown that grounded spatial reasoning, predicted goal images, point trajectories, or full world-model rollouts improve both action quality and interpretability. In current implementations, however, this reasoning dominates inference latency: hundreds of tokens or entire predicted frames must be generated before a single action is emitted; emerging world models compound the problem with heavyweight per-step rollouts. The very mechanism intended to make policies more reliable thus renders them too slow for closed-loop control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reasoning, by itself, is only as good as the underlying foundation model that uses the reasoning process. Most frontier robot policies remain closed off; open-source alternatives are embodiment-specific and hard to adapt to new tasks or embodiments. Frontier vision-language-action (VLA) models are effectively closed systems: their training data, recipes, and model weights are proprietary. The few exceptions release weights alone, withholding the data and training procedures needed to reproduce or extend them. This opacity both impedes scientific progress and prevents practitioners from adapting these models to their own robots or fine-tuning on in-house demonstrations. The few open-weights VLAs that can be run out-of-the-box are tied to expensive or specialized robot platforms beyond the reach of most academic labs and independent researchers. This constrains not only who can use these models, but also the diversity of settings in which they can be evaluated and improved. Zero-shot performance remains brittle, and even after task-specific fine-tuning, success rates on realistic tasks fall well below the threshold required for dependable deployment.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present MolmoAct2, an action reasoning model built for real-world deployment: fully open, deployable out-of-the-box on multiple embodiments, performant, and capable of fast, interpretable reasoning (Figure 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

MolmoAct2 improves over its predecessor MolmoAct along five axes vital for a strong action reasoning model: a stronger open embodied-reasoning VLM backbone, new open-source training datasets, MolmoAct2-FAST Tokenizer, an open-source multi-embodiment action tokenizer, a new VLA architecture design, and a new adaptive reasoning paradigm for efficient inference.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, we train Molmo2-ER (Sec. 2), a VLM specialized for spatial and embodied reasoning. General-purpose VLMs rarely train on or test the embodied skills a robot policy needs: they need to understand metric distances, free space, cross-view object tracking, and scene geometry. We address this by training Molmo2-ER on a 3.3M-sample spatial-embodied corpus using a specialize-then-rehearse recipe.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, existing open robot datasets remain fragmented across embodiments, uneven in quality, and too small or noisy to support reliable multi-embodiment action learning. To support training action models on top of our VLM backbone, we release three action datasets (Sec. 3) targeting three platforms across a low-to-medium cost range: MolmoAct2-BimanualYAM Dataset, 720 hours of teleoperated YAM trajectories spanning tabletop and household tasks-the largest open bimanual dataset to date; MolmoAct2-SO100/101 Dataset, a filtered subset of internet SO-100/101 data with mislabeled and low-quality trajectories removed; and MolmoAct2-DROID Dataset, a quality-filtered Franka subset of DROID. For the two filtered datasets, we also re-annotate the language instructions for improved diversity and accuracy.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, existing action tokenizers are either closed, tied to specific action spaces, or insufficiently documented, making it difficult to train reproducible discrete-action VLAs across embodiments. To make the trajectories in our data usable under a discrete autoregressive objective, we introduce MolmoAct2-FAST Tokenizer, an open-weight, open-data implementation following FAST. We train and release its weights along with the millions of trajectories across five embodiments used to train it. MolmoAct2-FAST Tokenizer compresses one second of 32-D continuous actions into a compact discrete sequence.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fourth, discrete-token VLMs provide strong reasoning grounding, but their native output space is poorly matched to the continuous, high-frequency trajectories required by robot control. A new architecture is therefore needed to connect the discrete reasoning capacity with smooth continuous actions. We design a new architecture that conditions each layer of the continuous action expert on the keys and values from the corresponding VLM layer. This design is in contrast to existing VLAs with action experts in two ways. First, we use a DiT-style transformer trained with flow matching objective, giving the continuous controller a modern denoising-transformer architecture that has proven more effective than many alternatives for diffusion and flow-based generative modeling. Second, instead of conditioning the expert on VLM hidden states, we condition each expert layer on the corresponding VLM keys and values. This preserves a similar compute profile while exposing the attention state used by the VLM itself, which has been shown to be more effective in our ablation studies.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fifth, prior reasoning-based VLAs improve action quality by generating dense intermediate representations at every step Lee et al., but this repeats nearly identical computation across largely static scenes and makes inference too slow for real-time control. We introduce MolmoAct2-Think, the reasoning variant of MolmoAct2, which performs adaptive depth reasoning by autoregressively predicting only the tokens for scene regions that change between timesteps. This exploits trajectory-level temporal redundancy to reduce latency proportional to the static scene fraction while retaining the geometric grounding that significantly improves model performance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To understand the capabilities of MolmoAct2 and assess its readiness for real-world deployment, we conduct the most extensive empirical study of any open VLA to date, spanning 7 environment benchmarks across both simulation and the real world. Across all of them, MolmoAct2, with MolmoAct2-Think, outperforms every strong baseline. We show that MolmoAct2 's fine-tuned checkpoints, MolmoAct2DROID and MolmoAct2-SO100/101, can be deployed out of the box on their respective embodiments without any additional fine-tuning, significantly surpassing π 0. 5 (Sec.6.2). We further demonstrate that MolmoAct2 is built on one of the strongest embodied-reasoning VLM backbones available: Molmo2-ER surpasses models such as GPT-5 and Gemini Robotics Embodied Reasoning (ER)-1.5 on 13 standard embodied-reasoning benchmarks (Sec.6.1).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

For rapid real-world deployment via efficient fine-tuning to new embodiments, MolmoAct2 opens large performance gaps over strong general-purpose VLAs such as π 0. 5 not only on the Sampling weights are the marginal proportion of each group within the non-robotics portion of the pretraining mixture.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Table1 MolmoAct2multimodalwebdatatrainingcorpus(combiningdatafromMolmo2,Molmo2-ER,andTulu-3). Sizes denote the number of samples used in our mixture (we subsample several datasets to balance the mixture).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

| | #Samples | Weight | | #Samples | Weight | two mainstream simulation benchmarks LIBERO and RoboEval, but also on a comprehensive evaluation suite of 8 real-world tasks on the bimanual YAM setup (Sec.6.3). Our ablations demonstrate that MolmoAct2-Think models yield further gains over MolmoAct2 while providing additional interpretability that aids both diagnosis and performance (Sec.6.4).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

MolmoAct2 is fully open in every respect, and beyond that, is capable of supporting real-world deployment for practical tasks: we release the model weights, training code, and the complete training dataset. We aim for MolmoAct2 to be more than an academic robotics foundation model; we want it to be a model that can be deployed in real-world workflows and deliver meaningful social impact.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Molmo2-ER", "weight": 1.0} -->

Existing VLM backbones are optimized for semantic image understanding rather than the metric, geometric, and temporally grounded reasoning required for robot control. We develop Molmo2-ER as a strong VLM backbone for embodied reasoning (ER). We finetune Molmo2 for specialized embodied perception skills that downstream action reasoning depends, including scene understanding, pixel-accurate pointing, multi-image and egocentric reasoning, exocentric correspondence, and video temporal reasoning. Molmo2-ER outperforms every open-weight baseline as well as the strongest closed-source models, including Gemini Robot-ER 1.5 Thinking and GPT-5, on 9 of 13 established embodied reasoning benchmarks (Table 3), reaching an overall average of 63. 8% and improving over its Molmo2 starting point by 17 points. The remainder of this section describes the new training data we introduce for Molmo2-ER (summarized in Table 1) and the two-stage training recipe used to inject these skills.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training data", "weight": 1.0} -->

On top of Molmo2 's original multimodal pre- and mid-training data, we curate a new embodied reasoning corpus of approximately 3. 3 M samples spanning six complementary capability pillars: single-image embodied QA, image pointing, image detection, video embodied QA, multi-image and ego-exo reasoning, and abstract embodied reasoning. Each pillar is covered by two or three datasets with diverse supervision sources (simulator ground truth, 3D-annotated real scans, template-generated QA, and a small amount of LLM-generated chain-of-thought), so that the model is exposed to a wide distribution of spatial reasoning phenomena rather than over-fitting to a single template style. The composition of this corpus is summarized in Table 1; we briefly describe each constituent below.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training data", "weight": 1.0} -->

Image embodied QA. We assemble a mixture of image QA sources chosen to cover complementary axes of spatial competence rather than to maximize any single one. SAT supplies simulator-grounded supervision for dynamic reasoning (egocentric motion, perspective taking, action consequences) that is hard to harvest from static web data. RoboPoint-QA contributes general VQA breadth to guard against forgetting base perception during spatial fine-tuning. RefSpatial bridges web images, real indoor scans, and procedural simulation, and is our main source of chain-of-thought referring-the bridge from spatial language to the pointing actions used downstream; we draw 250K multiple choice questions, 250K Chian-of-thought, and 80K pointing examples. VST-P normalizes inputs onto a uniform virtual camera, giving metric-consistent depth, distance, direction, and size supervision (200K single-image + 200K cross-view). VSI-590K extends coverage to in-the-wild robotics and tour footage via 3D-grounded label propagation (200K images and 300K videos). Together these span static/dynamic, synthetic/real, and single-/multi-view regimes.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training data", "weight": 1.0} -->

VideoembodiedQA. To extend reasoning across time we pair two complementary sources. SIMS-VSI gives clean simulator labels for distance, direction, count, and temporal-order questions over agent trajectories (203K). RoboVQA covers the other end of the distribution: humanannotated long-horizon embodied video targeting planning, affordance, and future prediction-i.e. the question types that map most directly onto policy behavior; we use a 200K subset.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training data", "weight": 1.0} -->

Pointing and object detection. Pointing is our primary action interface, so we deliberately oversample pixel-accurate localization. Beyond RefSpatial's pointing split, we use the full RoboPoint procedural pointing corpus (700K normalized ( x, y ) targets for object reference and free-space selection) together with its 100K LVIS-sourced detection split, which ground spatial language directly in the coordinate format the policy consumes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training data", "weight": 1.0} -->

Multi-image and ego-exo correspondence. Embodied policies routinely reconcile multiple camera views and switch between first- and third-person frames, an ability under-served by single-image corpora. We therefore include SenseNova-SI (500K subset), whose distinguishing emphasis is multi-image and egocentric-exocentric correspondence, together with the 200K cross-view split of VST-P.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training data", "weight": 1.0} -->

Abstract embodied reasoning. Finally, we add two synthetic diagnostics to harden compositional reasoning in a low-bias setting. CLEVR (50K) targets compositional attribute-relation reasoning. GRiD-3D (100K) specifically isolates object-intrinsic relative direction (front/left of a referent's own frame, not the camera's)-a frame-of-reference distinction that matters for instruction following but is rarely labeled in natural data.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Specialize-then-rehearse training recipe", "weight": 1.0} -->

To avoid the redundant compute of re-running Molmo2 's full multimodal training with our new corpus integrated, we build on the released Molmo2 checkpoint with a two-stage specialize-then-rehearse recipe.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Specialize-then-rehearse training recipe", "weight": 1.0} -->

Stage 1: Embodied specialization. Starting from the Molmo2 -4B mid-training checkpoint, we fine-tune for 20 K steps on the Molmo2-ER corpus augmented with 8% Tulu-3 text-only data to preserve language competence, using sequence length 4, 200 and a global batch size of 64 (device batch size 4 across 2 nodes × 8 H100 GPUs). This stage rapidly moves the model onto the embodied data manifold: pointing accuracy, video embodied QA, and multi-image reasoning all improve sharply.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Specialize-then-rehearse training recipe", "weight": 1.0} -->

Stage 2: Joint refinement. We continue training the Stage 1 checkpoint for 1. 5 K additional steps on a mixture that interleaves our embodied corpus with Molmo2 's original multimodal mid-training data (general VQA, captioning, academic benchmarks, tracking, and Molmo2 pointing). Holding the NLP rate at 8%, the remaining 92% budget is split as p ⋅ 0. 92 embodied and ( 1 -p ) ⋅ 0. 92 general, with each side's internal proportions preserved. Sweeping p ∈ { 0. 30, 0. 50, 0. 70, 0. 90 }, we find p = 0. 5 yields the best Pareto trade-off between the embodied-reasoning benchmarks in Table 3 and Molmo2 's general benchmarks. To accommodate the long multi-image and long-video examples in the general mixture, Stage 2 uses a longer sequence length ( 16, 384 vs. 4, 200 in Stage 1) with per-device batch size reduced to 1; all other hyperparameters follow Molmo2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Data", "weight": 1.0} -->

Training a generalist vision-language-action model requires data that is simultaneously large in scale, diverse across embodiments, tasks, and scenes, and high in quality. The robotics community has released several substantial public corpora toward this goal-most notably the Open X-Embodiment (OXE) mixture, DROID, and a rapidly growing collection of LeRobot community datasets contributed by SO-10x users. While each is valuable, none of these resources individually, nor their union, is sufficient for training a model intended for real-world deployment. OXE offers breadth across embodiments but its constituent datasets vary widely in quality, control conventions, and language-annotation fidelity; DROID provides scale on a single Franka platform, but a substantial fraction of its episodes contain idle segments, failed attempts, or repetitive task instructions; and crowd-sourced LeRobot data, although rich in embodiment and scene diversity, frequently contains placeholder annotations such as 'lerobot\_test' alongside genuine demonstrations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data", "weight": 1.0} -->

Critically, no public corpus contains high-quality bimanual manipulation data on the platform we target for deployment, and the tasks that are covered are often collected with limited variation in scene configuration, object instances, or spatial variation that mimic the realistic of real-world tasks for deployment.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data", "weight": 1.0} -->

To close these gaps, we assemble MolmoAct2 's training mixture from three complementary sources, summarized in Fig. 2. First, we collect MolmoAct2-BimanualYAM Dataset, a new bimanual manipulation dataset emphasizing task repeatability and task, object, and scene diversity across a wide range of useful behaviors. Second, we curate and filter two large public corpora, MolmoAct2-SO100/101 Dataset (drawn from community LeRobot data) and MolmoAct2-DROID Dataset (drawn from DROID), using structural, licensing, and quality-based filtering pipelines, and re-annotate their language instructions to improve both accuracy and diversity. Third, we co-train with a targeted subset of academic robotics data for additional embodiment breadth, together with multimodal and embodied-reasoning data to preserve the broad visual and linguistic competence of the underlying VLM. The remainder of this section describes each component of the mixture in turn, together with the language re-annotation pipeline shared across our robot datasets.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data", "weight": 1.0} -->

MolmoAct2 is trained on a diverse set of datasets spanning robot data, multimodal reasoning, and embodied reasoning, summarized in Fig. 2. Additionally, we collected MolmoAct2-BimanualYAM Dataset, curated MolmoAct2-SO100/101 Dataset, and filtered MolmoAct2-DROID Dataset for use in pre-training and post-training. Below, we describe each dataset and detail its respective collection, curation, or filtering process.

<!-- chunk {"id": "body-0033", "role": "body", "section": "MolmoAct2-BimanualYAM Dataset", "weight": 1.0} -->

To support real-world deployment, we introduce MolmoAct2-BimanualYAM Dataset, an open-source robot manipulation dataset that emphasizes task repeatability, task diversity, and object diversity across a broad range of useful behaviors spanning household, factory, and coffee-shop settings. All data is collected on our custom bimanual YAM (Yet Another Manipulator) setup, shown in Figure 3. MolmoAct2-BimanualYAM Dataset is designed to deliver both scale and quality. It contains over 28 unique real-world tasks from folding clothes and untangling cables to bussing tables, scanning groceries, and packing medication, each captured with substantial variation in scene configuration, object instances, and object placement. In total, the dataset comprises 34.5k robot demonstrations totaling over 720 hours of robot data, collected over a two-month period. Data collection was supported by Cortex AI, with strict protocols governing the number of permitted failure retries and the maximum duration of no-op segments to ensure consistently high data quality. Further details on MolmoAct2-BimanualYAM Dataset are provided in the appendix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "MolmoAct2-SO100/101 Dataset", "weight": 1.0} -->

SO-100/101 is a low-cost robotic platform from Hugging Face that is accessible to a broad community of users. As a result, we utilize the diverse open-source SO-10x data collected by the community to improve our model's capability for deployment in the wild. Specifically, we curate MolmoAct2-SO100/101 Dataset from 1,222 public LeRobot datasets contributed by 377 users. This corpus contains 38,059 robot demonstration episodes, 19.8M frames, and approximately 184 hours of interaction data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "MolmoAct2-SO100/101 Dataset", "weight": 1.0} -->

To prioritize quality while preserving diversity, we apply a four-stage filtering pipeline: (i) structural validity checks (required schema fields, valid action/state tensors, no NaN/corrupt samples), (ii) removal of eval-style datasets, (iii) license/codebase eligibility checks, and (iv) a final TOPReward quality gate. In stage (iv), we keep datasets whose mean TOPReward over the last 3 sampled episodes is above a threshold obtained by averaging the TOPReward over a collection of human-audited high-quality datasets.

<!-- chunk {"id": "body-0036", "role": "body", "section": "MolmoAct2-SO100/101 Dataset", "weight": 1.0} -->

The filtered data spans both SO-100 and SO-101 embodiments, multiple camera configurations, varied object manipulation tasks, and diverse real-world collection environments. Compared with centrally collected robot datasets, this community-sourced corpus provides broader coverage of user setups, backgrounds, objects, and task annotations, making it a useful source of embodiment and environment diversity for improving real-world robustness.

<!-- chunk {"id": "body-0037", "role": "body", "section": "MolmoAct2-DROID Dataset", "weight": 1.0} -->

DROID (Distributed Robot Interaction Dataset) is a large-scale in-the-wild robot manipulation dataset, collected across a wide range of real-world deployment scenarios with a unified Franka robot setup. To ensure the quality of our training data, we leverage the supplementary annotations released in the accompanying HuggingFace repository to filter the original DROID release. Specifically, we use (i) the extended language annotations, which provide three natural-language instructions for 95% of the 75k successful episodes, and (ii) the provided idle-frame filter, which retains only contiguous non-idle action segments of at least one second. Furthermore, we did language re-annotation for the filtered DROID dataset before using for training. The resulting subset, which we refer to as MolmoAct2-DROID Dataset, contains 74,604 valid episodes comprising a total of 17,758,044 frames. Each episode in this subset is marked as successful, contains at least one valid language instruction, and is free of significant pauses.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Language annotation pipeline", "weight": 1.0} -->

Following standard practice in imitation learning, each demonstration in our datasets is paired with a language instruction that describes the task completed by the teleoperator. However, we find that these annotations often are imperfect along two key axes. First, datasets where a specific set of tasks is collected repeatedly at scale often have repetitive language instructions. For example, the dataset collected in Jang et al. contains 104 unique instructions for 39350 episodes, representing 0. 26% unique instructions in the dataset. Secondly, as found in prior work, crowd-sourced datasets like the MolmoAct2-SO100/101 Dataset often have inaccurate or meaningless task annotations, like "lerobot\_test" and "Test run".

<!-- chunk {"id": "body-0039", "role": "body", "section": "Language annotation pipeline", "weight": 1.0} -->

To improve both the diversity and accuracy of the language instructions in our robotics datasets, we use an open-source VLM (Qwen3.5-27B) to re-annotate the datasets. We prompt the VLM with a sample of the frames and the original instruction. The VLM is asked to generate a instruction that describes the demonstration. To increase the diversity of prompts, we randomly sample a number and ask the VLM to make this instruction roughly that many words. Relabeling the robotics datasets through this pipeline doubles the unique labels in the overall from 71121 (22%) to 146485 (46%) in dataset. More details and the prompt can be found in Appendix D.2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Academic robotics datasets", "weight": 1.0} -->

To broaden the range of embodiments, camera layouts, task families, and control conventions seen during pre-training, we include additional public academic robotics data. This pool consists of a targeted subset of the Open X-Embodiment mixture, including BC-Z, BridgeData V2, and RT-1, together with MolmoAct Dataset from MolmoAct. These datasets are used as complementary sources rather than as the primary deployment embodiments, since YAM, SO-100/101, and DROID supply the majority of robot training examples.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Multimodal datasets", "weight": 1.0} -->

Past research on robotics foundation models has found benefits in incorporating multimodal data into the training mix along with robotics datasets. We co-train the VLA with a multimodal data mixture where 46% consists of the Molmo2-ER dataset mixture described in Sec. 2.1, 46% consists of the Molmo2 dataset mixture, and 8% consists of the text-only data from Tulu-3. The high level composition of this data can be seen in Table 1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "MolmoAct2", "weight": 1.0} -->

MolmoAct2 follows a three-stage training pipeline, with the post-training architecture summarized in Fig. 4. Pre-training (Sec. 4.1) adapts the Molmo2-ER vision-language backbone into a discrete autoregressive robot policy, using the MolmoAct2-FAST Tokenizer (Sec. 4.1.1) to map continuous trajectories into a compact action vocabulary under a unified next-token recipe (Sec. 4.1.2). Post-training (Sec. 4.2) attaches a flow-matching action expert with per-layer KV conditioning on the autoregressive backbone (Sec. 4.2.1), and co-trains discrete and continuous action supervision (Sec. 4.2.2) to produce continuous control. Deployment (Sec. 4.3) then covers embodiment-specific fine-tuning (Sec. 4.3.1) and inference optimization (Sec. 4.3.2). Shared implementation details for training infrastructure, packing, prompt formatting, and stage-level hyperparameters are provided in Appendix B.

<!-- chunk {"id": "body-0043", "role": "body", "section": "MolmoAct2", "weight": 1.0} -->

MolmoAct2 is designed around a practical tension: we want to preserve the scaling properties and general visual-language competence of a pretrained VLM, while producing precise continuous robot actions across heterogeneous embodiments. Directly training a VLM and a continuous action expert together from the beginning makes optimization unnecessarily difficult: the model must simultaneously learn a robot-aware token interface, align new state/action embeddings, and fit a flow-matching controller. We therefore use a three-stage pipeline. Pre-training first turns Molmo2-ER into an action-aware VLA using only autoregressive supervision, which gives the backbone aligned robot, state, and action-token embeddings under the same next-token objective used by the base VLM. Post-training then attaches the continuous action expert to this already action-aware backbone, allowing the flow-matching controller and its VLM conditioning interface to align quickly on a broad robot-data mixture.

<!-- chunk {"id": "body-0044", "role": "body", "section": "MolmoAct2", "weight": 1.0} -->

We keep post-training separate from embodiment-specific fine-tuning for efficiency: the post-training mixture is intentionally diverse across datasets, robots, control rates, camera layouts, and task families, so extending it until the model is directly deployment-ready for every target embodiment would require a long and expensive training stage. Instead, post-training produces a general continuous-control base model, and fine-tuning adapts that model quickly to a specific embodiment, environment, and use case while keeping the same architecture and output interfaces.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Pre-training", "weight": 1.0} -->

MolmoAct2-Pretrain adapts the Molmo2-ER vision-language backbone into a discrete autoregressive robot policy while keeping the Molmo2 token interface intact. Images and video frames are still encoded by a ViT, pooled and projected by the vision-language connector, and passed to the LLM together with text. Robot examples extend this sequence with two additional token streams: state tokens that describe the current robot configuration, and action tokens that describe the future one-second motion.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Pre-training", "weight": 1.0} -->

This subsection focuses on the two ingredients needed to make that formulation practical. First, we describe MolmoAct2-FAST Tokenizer, which converts continuous, embodiment-specific robot trajectories into compact discrete action tokens. Second, we describe the pre-training recipe that lets these robot sequences be mixed with standard multimodal data: single-crop visual inputs, a small number of sampled video frames, setup/control and action-output markers, state tokenization, and packed training sequences. Together, these choices preserve a single next-token prediction objective across text, vision-language, state, and action targets, without introducing a separate continuous action head at this stage.

<!-- chunk {"id": "body-0047", "role": "body", "section": "MolmoAct2-FAST Tokenizer", "weight": 1.0} -->

Robot actions are continuous, embodiment-specific, and often produced at different control rates, so they cannot be inserted into a language-model pre-training stream directly. We therefore train MolmoAct2-FAST Tokenizer, an open-weight and open-data action tokenizer following FAST. The goal is not to introduce a different tokenization principle, but to make this component fully inspectable and reproducible: existing FAST weights are useful, but their training data mixture is not fully specified. MolmoAct2-FAST Tokenizer fi lls this transparency gap by releasing both the tokenizer weights and the action mixture used to train it. It maps a one-second action trajectory into a compact sequence of discrete tokens by representing the trajectory with a frequency-domain transform, quantizing the resulting coefficients, and applying byte-pair encoding to produce tokens from a 2048-token action vocabulary.

<!-- chunk {"id": "body-0048", "role": "body", "section": "MolmoAct2-FAST Tokenizer", "weight": 1.0} -->

Table 2 Embodimentmixturefor MolmoAct2-FAST Tokenizer training. The tokenizer is trained on one million subsampled action sequences spanning the main robot embodiments used by MolmoAct2, plus smaller sources that broaden control-mode coverage.

<!-- chunk {"id": "body-0049", "role": "body", "section": "MolmoAct2-FAST Tokenizer", "weight": 1.0} -->

| Dataset | Mix | Robot | Action representation | Unlike the prior FAST tokenizer, whose released weights are not paired with a fully specified training distribution, MolmoAct2-FAST Tokenizer is trained from a transparent action mixture. We subsample one million action sequences across five embodiments, balancing the main MolmoAct2 deployment platforms with smaller sources that broaden the control vocabulary (Table 2). This gives MolmoAct2-FAST Tokenizer coverage over bimanual YAM, SO-100/101, DROID Franka, BC-Z, BridgeData V2, RT-1, and MolmoAct Dataset trajectories, including both absolute joint control and delta end-effector control.

<!-- chunk {"id": "body-0050", "role": "body", "section": "MolmoAct2-FAST Tokenizer", "weight": 1.0} -->

Before fitting the tokenizer, we put all raw robot telemetry into a common action format. Each training sequence corresponds to one second of robot motion, so the number of actions in a chunk is set by the control frequency of the source dataset. Each action in the chunk is padded to 32 dimensions, so embodiments with different action dimensionalities share the same tokenizer input space. Continuous dimensions are normalized with 1-99 percentile statistics, which limits the effect of outliers while preserving the useful dynamic range of each control dimension. Gripper commands are handled separately from this continuous normalization, since they are typically binary or narrow-range open/close signals. This standardized representation allows the same tokenizer to cover both joint-space and end-effector control across multiple robot platforms.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Pre-training recipe", "weight": 1.0} -->

Model. We initialize from the Molmo2-ER checkpoint and keep the Molmo2 vision-language architecture. Visual observations are encoded by the SigLIP2 ViT, converted into language-model tokens by the connector, and passed to the LLM together with the language instruction and robot-specific text. The connector uses the same Molmo2 design: features from the third-to-last and ninth-from-last ViT layers are pooled into compact image or video-frame tokens and projected into the LLM embedding space. Full backbone and added-token details are given in subsection A.1, with architecture hyperparameters in Table 15.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Pre-training recipe", "weight": 1.0} -->

Data. The training mixture combines multimodal examples with robot trajectories so that the model retains vision-language capability while learning to predict actions; we describe the data sources and curation in Sec. 3. We allocate 10% of sampling to multimodal data and 90% to robot trajectories. Within the robot portion, YAM, SO-100/101, and DROID each receive 30% of the robot sampling weight; the remaining 10% is split across smaller BC-Z, BridgeData V2, RT-1, and MolmoAct Dataset sources. For all visual inputs in this stage, we use a single resized crop rather than high-resolution tiled crops. For videos, we sample at most 8 frames at up to 2 FPS, and we skip examples that exceed the sequence budget, which primarily removes unusually long text examples and videos with long captions. We also apply the image augmentation described in Appendix B during pre-training, combining light geometric perturbations with color jitter and occasional blur. For multi-camera robot episodes, we randomize the input camera order at the episode level to prevent the model from relying on a fixed camera slot.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Pre-training recipe", "weight": 1.0} -->

Each robot example also includes setup and control strings using the same special-token wrappers used during training, e.g., <setup\_start>bimanual yam robotic arms in molmoact2<setup\_end>, and <control\_start>absolute joint pose<control\_end> or <control\_start>delta end-effector pose<control\_end>; the corresponding chat template and output trigger formatting are detailed in Appendix B.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Pre-training recipe", "weight": 1.0} -->

Action and state representation. This stage is deliberately limited to discrete autoregressive supervision: the model predicts action tokens, but does not yet train the continuous action expert used in post-training. Each robot target is represented as a one-second action chunk, so the number of raw actions in the chunk follows the control frequency of the source dataset. Before tokenization, continuous action and state dimensions are normalized with 1-99 percentile statistics; gripper commands are treated separately from this percentile scaling when they are represented as binary or narrow-range open/close signals. Action vectors are padded to a 32-dimensional space and then encoded with the 2048-token vocabulary of MolmoAct2-FAST Tokenizer. Proprioceptive state is represented separately: after normalization, each state value is uniformly discretized into one of 256 state tokens and appended to the prompt before the action target.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Pre-training recipe", "weight": 1.0} -->

Training. We train for 200K steps with a maximum sequence length of 4200 tokens. Examples vary substantially in length: a text-only example may use only a few hundred tokens, while multi-camera robot examples must carry images, states, and action targets. We therefore use on-the-fly packing to combine multiple short examples into one 4200-token sequence. Packed examples share the same forward pass, but their text, visual tokens, state tokens, and action targets remain separated by the training attention mask, so the model does not condition one example on another. Appendix B gives the implementation details for this packing procedure and the shared training stack. We train the vision encoder, connector, language model, and newly added tokens' embeddings with a global batch size of 128 across 64 H100 GPUs for around 5,760 GPU hours. The vision encoder and connector use a learning rate of 5 × 10 -6, and the language model uses 1 × 10 -5. This produces a discrete VLA checkpoint that can later be adapted to continuous control.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Post-training", "weight": 1.0} -->

MolmoAct2-Pretrain learns a robot policy through the same autoregressive interface used by the VLM: given language, visual observations, setup/control descriptors, and state tokens, it predicts discrete action tokens produced by MolmoAct2-FAST Tokenizer. This makes large-scale robot pre-training simple and stable, but the deployed policy should output continuous action trajectories directly. Post-training therefore adds a flow-matching action expert to the pre-trained VLM, producing the final MolmoAct2 model.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Post-training", "weight": 1.0} -->

This section describes the two parts of that adaptation. First, we introduce the action expert and its per-layer KV conditioning on the VLM, which lets the continuous controller condition on the full visual-language attention state without replacing the backbone. Second, we describe the post-training recipe: how we keep the pre-training data construction, co-train discrete and continuous action supervision, mask padded or targetleaking tokens, and adjust packing and sequence lengths for the added action-expert compute. Additional model hyperparameters and implementation details are given in subsection A.2, with shared training-system details in Appendix B.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Action expert and per-layer KV conditioning", "weight": 1.0} -->

Post-training adds a continuous action expert on top of the pre-trained autoregressive VLM. We use a DiT-style transformer expert because flow matching and diffusion models have shown that denoising transformers scale well for continuous generation, and because action trajectories are naturally represented as short continuous sequences rather than as text-like token streams. This choice separates responsibilities: the VLM provides visual-language grounding and robot-state context, while the expert models the continuous velocity field needed to transform noisy action chunks into executable trajectories.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Action expert and per-layer KV conditioning", "weight": 1.0} -->

The key architectural question is how this expert should receive VLM context. A shallow projection of the final hidden state compresses the backbone into a single residual-stream representation. Instead, MolmoAct2 conditions the expert on the VLM at every layer. Each action-expert block cross-attends to the corresponding VLM layer's keys and values, after lightweight learned projections map the VLM attention state into the expert's cross-attention width. This gives the continuous controller access to the same attention state used by the VLM itself, while preserving a modular interface between the backbone computation and the newly trained action expert.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Action expert and per-layer KV conditioning", "weight": 1.0} -->

Given a normalized target action chunk a, Gaussian noise ϵ, and a sampled time t ∈, we interpolate between noise and data, The expert f θ predicts the target velocity u ⋆ from the noisy action chunk, the time embedding, and the VLM context c, which contains the task, visual observations, setup/control descriptors, and discrete state tokens: where m masks padded action steps and padded action dimensions. At inference, we start from Gaussian noise and integrate the predicted velocity field to produce a continuous action trajectory.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Action expert and per-layer KV conditioning", "weight": 1.0} -->

Architecturally, the expert has the same depth as the VLM, where both of them use L = 36 layers. The expert first embeds the current noisy action sequence. Each block then applies action self-attention, cross-attention to the VLM, and an MLP, with the time embedding producing DiT-style shift, scale, and gate parameters for all three residual branches. Schematically, block ℓ computes The action expert uses per-layer KV conditioning rather than hidden-state conditioning. For each VLM layer ℓ, we collect the keys and values (K vlm ℓ, V vlm ℓ) produced by that layer's self-attention. We then project them into the action-expert width with learned adapter projections P K and P V: Here, P K and P V are linear VLM-to-expert adapter layers that align the VLM KV dimensionality with the expert's cross-attention width; they are separate from the VLM self-attention projections that produced the keys and values. After projection, the conditioning context is organized into the expert's attention heads.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Action expert and per-layer KV conditioning", "weight": 1.0} -->

The cross-attention in expert block ℓ attends to the projected keys and values from the corresponding VLM layer: where d h is the expert head dimension. This per-layer KV conditioning gives every action-expert block direct access to the visual-language attention state at the same depth in the backbone. During post-training we detach this conditioning path from the VLM, so the flow loss trains the expert and its adapter projections without sending gradients back through the VLM keys and values.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

Overview. Post-training starts from the 200K-step MolmoAct2-Pretrain checkpoint and turns it into the final MolmoAct2 model. We keep the VLM architecture and pre-training data construction from Sec. 4.1.2, including the image augmentation described in Appendix B. The main change is that robot examples now supervise both output interfaces: the LLM continues to predict discrete action tokens, while the action expert described in Sec. 4.2.1 learns to generate continuous action chunks.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

Multiple flow samples. For each robot action chunk, we evaluate the flow objective at multiple noise levels. Let a be a normalized continuous action chunk and c be the VLM context for the corresponding robot prompt. For each training example we draw K independent pairs {(ϵ i, t i)} K i = 1, form x t i = (1 -t i) ϵ i + t i a, and train the expert to predict a -ϵ i: We use K = 4, so each robot sample contributes four points on the same flow trajectory while reusing the same visual-language context. We didn't use K = 8 as in the fine-tuning stage (Sec. 4.3.1) mainly due to GPU memory constraints.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

Padding and packing. Post-training retains a common action tensor shape across embodiments. Continuous actions are right-padded to a maximum horizon of 30 steps and a maximum width of 32 dimensions. The horizon mask removes padded time steps from the flow loss, and the dimension mask zeroes padded action dimensions in the noisy inputs, targets, and predictions before averaging the loss over valid dimensions. This lets datasets with different control rates and action widths share the same expert without training on artificial padded coordinates.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

Packing is also extended to the continuous expert. A packed language sequence can contain multiple robot examples; each action chunk is paired with the sub-example that produced it, and the expert attends only to that example's VLM context. To keep memory use stable when packed batches contain different numbers of robot chunks, we pad the packed action-chunk axis up to a small fixed cap of five chunks per packed sequence when possible. Padded chunk rows are marked invalid and excluded from the flow loss; sequences with more chunks are still used, but processed without this fixed-cap padding.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

Training objectives. The post-training objective combines the autoregressive loss from pre-training with the flow-matching loss: The language-model loss is applied to the same next-token targets used in pre-training, including discrete action tokens for robot examples and text tokens for VLM examples. The flow loss is applied only to continuous robot action chunks. Since robot examples contain both the discrete action target and the continuous action target, we mask the discrete action-token span out of the expert's VLM conditioning path. The expert therefore conditions on the task, observations, setup/control descriptors, and state tokens, but not on the target action tokens it is supposed to predict.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

We also apply knowledge insulation, where the VLM is isolated from the continuous-action loss. The expert conditions on the VLM keys and values, but these tensors are detached before they enter the expert, so Lfl ow updates the action expert and its adapter projections without back-propagating through the VLM. The VLM is still updated by L LM.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Post-training recipe", "weight": 1.0} -->

Training. Robot batches use a sequence length of 2100 tokens, while the non-robot VLM batches keep the 4200-token context length from pre-training. We use this split because robot batches additionally run the action expert and four flow samples per action chunk, whereas VLM batches only train the autoregressive model. We train for 100K updates with a global batch size of 128 and a device batch size of 2 across 64 H100 GPUs for around 2,304 GPU hours. The VLM learning rates match pre-training: 5 × 10 -6 for the vision encoder and connector, and 1 × 10 -5 for the language model. The action expert is trained with a larger learning rate of 5 × 10 -5.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

Shared recipe. Embodiment-specific fine-tuning starts from the post-trained MolmoAct2-Post checkpoint and keeps the same VLM-action-expert architecture described in Sec. 4.2. We continue to co-train the discrete autoregressive action output and the continuous flow-matching action expert, use the same 32-dimensional padded action width, and keep the same learning rates as post-training: 5 × 10 -6 for the vision encoder and connector, 1 × 10 -5 for the language model, and 5 × 10 -5 for the action expert. We also keep single resized crops, packed sequences, setup/control descriptors, discrete state tokens, and the same action-token vocabulary, using the shared prompt, image-augmentation, and packing implementation described in Appendix B.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

The fine-tuning stage differs from post-training in four ways. First, each run is robot-only: we do not include the multimodal VLM mixture or a separate VLM dataloader. Second, we increase the number of sampled flow times from 4 to 8 per action chunk, which gives the action expert denser supervision along the same flow trajectory. Third, we do not use knowledge insulation during fine-tuning: gradients from the flow loss are allowed to update the VLM through the action-expert conditioning path, since we did not observe a consistent performance gain from detaching this path at this stage. Finally, for the main embodiment checkpoints below, we do not tune the added-token input embeddings. As in standard VLM fine-tuning, we assume that the token embeddings learned during pre-training and post-training are already well placed, and tune the language-model output head and final normalization instead.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

Bimanual YAM. The MolmoAct2-BimanualYAM checkpoint is fine-tuned on the bimanual YAM mixture. The camera order is fixed as top, left, and right, matching the data collection setup. We use annotated language instructions, absolute joint-pose actions, and a 30-step action chunk, corresponding to the 30 Hz control rate of the dataset. We train with a sequence length of 2100, global batch size 128, and 100K updates on 64 H100 GPUs, for roughly 2,304 GPU hours.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

DROID. The MolmoAct2-DROID checkpoint is fine-tuned on the filtered DROID mixture. DROID provides two exterior cameras and one wrist camera. For DROID-style two-view evaluation, we use a fixed exterior-then-wrist ordering; when training variants expose both exterior choices as alternatives, the loader samples one exterior camera and pairs it with the wrist camera during training. We use absolute joint-pose actions with a 15-step action chunk, matching DROID's 15 Hz control rate. We do not use the additional language annotations in this fine-tune, to keep the comparison with prior DROID-trained models fair. We train with a sequence length of 2100, global batch size 64, and 100K updates on 32 H100 GPUs, for roughly 1,152 GPU hours.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

SO-100/101. The MolmoAct2-SO100/101 checkpoint is fine-tuned on the SO-100/101 mixture. Because this data is aggregated from internet demonstrations with diverse and inconsistent camera layouts, we randomize the input camera order at the episode level rather than imposing a fixed view naming convention.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

We use annotated language instructions, absolute joint-pose actions, and a 30-step action chunk for the 30 Hz control rate. We train with a sequence length of 2100, global batch size 64, and 100K updates on 32 H100 GPUs, for roughly 1,152 GPU hours.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

LIBERO. The MolmoAct2-LIBERO checkpoint is fine-tuned on the full LIBERO training mixture, combining the Spatial, Object, Goal, and Long suites rather than training a separate model for each suite. The camera order is fixed as front view followed by wrist view. We do not use annotated language instructions. LIBERO uses relative end-effector control at 10 Hz, so we train with a 10-step action chunk. We use a sequence length of 2100, global batch size 64, and train for 50K updates on 32 H100 GPUs, for roughly 1,152 GPU hours; for evaluation, we select the best-performing checkpoint, which occurs at 40K updates.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Embodiment-specific fine-tuning", "weight": 1.0} -->

Otherevaluationfine-tunes. For smaller task- or benchmark-specific fine-tunes used in downstream evaluation, we follow the same recipe unless otherwise noted. These runs use fixed metadata camera order rather than camera-order randomization, no language annotations, 2100-token sequences, packing, 8 sampled flow times, and robot-only data. The action horizon is set to the dataset control frequency, and the control representation follows the dataset, either joint pose or end-effector pose. Real-world evaluation runs use 8 H100 GPUs, global batch size 16, and 50K updates, and we choose the best-performing checkpoint for evaluation.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Inference optimization", "weight": 1.0} -->

For the MolmoAct2 model, inference is dominated by the continuous action expert, which integrates a fixed-step flow-matching trajectory conditioned on the VLM context. Within one action chunk, this context is invariant across flow steps, while only the noisy action state and flow time evolve. We therefore cache reusable action-expert intermediates, including context-dependent cross-attention states and fixed position-dependent terms, and reuse them throughout the flow loop. We further capture the fixed-shape flow loop with CUDA Graphs, reducing Python and kernel-launch overhead during repeated action generation.

<!-- chunk {"id": "body-0079", "role": "body", "section": "MolmoAct2-Think", "weight": 1.0} -->

Robotic manipulation depends on spatial information that is only indirectly supervised by action imitation: object distance, free space, occlusion, and surface layout all affect the action, but standard behavior-cloning objectives do not ask the model to make this structure explicit before acting. MolmoAct addressed this problem by adding depth-token prediction as an intermediate reasoning step. MolmoAct2Think extends the same idea to MolmoAct2: before producing an action, the model predicts a compact discrete depth representation that conditions the action expert through per-layer KV conditioning.

<!-- chunk {"id": "body-0080", "role": "body", "section": "MolmoAct2-Think", "weight": 1.0} -->

The depth representation is intentionally lightweight. Each observation depth map is quantized into a 10 × 10 grid, giving 100 spatial code positions, and each position takes one of 128 learned depth-code values. These codes are represented as ordinary autoregressive tokens, which makes depth reasoning compatible with the same next-token interface used throughout MolmoAct2 while exposing an interpretable intermediate prediction.

<!-- chunk {"id": "body-0081", "role": "body", "section": "MolmoAct2-Think", "weight": 1.0} -->

The main distinction from MolmoAct is that MolmoAct2-Think makes depth prediction adaptive across time. Robot trajectories contain substantial temporal redundancy: many cells in a scene-level depth grid remain unchanged from one control step to the next. Instead of re-predicting every depth code at every step, MolmoAct2-Think reuses cached codes for static regions and autoregressively predicts only the cells whose RGB evidence changes. The result is a depth-aware policy whose geometric reasoning cost scales with scene change rather than with the full 100-token grid.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Adaptive depth perception data", "weight": 1.0} -->

For every robotics dataset used by MolmoAct2-Think in the mixtures described in section 3, we attach depth annotations to the policy observation stream. We use the same camera stream that is presented to the policy for depth reasoning: single-view datasets use their canonical observation camera, and multi-view datasets use the first policy view with available depth annotations. For heterogeneous LeRobot datasets, when a camera is not specified explicitly, the video feature is selected from the dataset metadata.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Adaptive depth perception data", "weight": 1.0} -->

For each RGB frame, we estimate a dense monocular depth map with Depth Anything V2. We then quantize that depth map with the trained depth VQ-VAE used by MolmoAct, following the tokenization scheme of Ning et al.. The VQ-VAE operates on a 320 × 320 depth image with a downsampling factor of 32, producing a 10 × 10 grid of codebook indices in { 0,..., 127 }.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Adaptive depth perception data", "weight": 1.0} -->

The same preprocessing pass also constructs the adaptive-depth side channels used during training and inference. Let d t ∈ { 0,..., 127 } 100 be the full VQ depth codes for frame t, flattened in raster order. We maintain a buffer b t and update mask m t ∈ { 0, 1 } 100. For the first frame of an episode, all positions are updated and b 1 = d 1. For later frames, the RGB image is resized to 320 × 320, divided into the same 10 × 10 grid of 32 × 32 patches, and each patch is compared to the corresponding patch in the previous frame by cosine similarity. A cell is marked updated when the similarity is below 0.996: Thus each frame stores the full depth codes d t, the carried-forward depth buffer b t, and the binary update mask m t. The model is supervised on the buffer codes, matching the representation it will maintain during adaptive inference.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Training", "weight": 1.0} -->

Post-training. MolmoAct2-Think starts from the same 200K-step MolmoAct2-Pretrain checkpoint as the standard MolmoAct2 post-training stage. We keep the post-training recipe in subsection 4.2: the same data construction, action expert, per-layer KV conditioning, sequence lengths, optimizer settings, 100K training updates, global batch size of 128, and 64 H100 GPUs. On top of MolmoAct2, we added depth-related special tokens for training MolmoAct2-Think, where the full depth-token interface is in subsection A.3.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Training", "weight": 1.0} -->

Within robot data, post-training uniformly samples three tasks: action prediction, depth prediction, and depth-and-action prediction. The action task trains the usual discrete and continuous action objectives. The depth task trains autoregressive prediction of the 100 depth-buffer tokens. In the depth-and-action task, the model first predicts depth tokens, then predicts discrete action tokens autoregressively while the action expert conditions on the input context and predicted depth state to generate continuous actions. The prompt templates and assistant-side triggers for these output styles are given in Appendix B. As in subsection 4.2, the target action-token span is masked from the expert conditioning path, so the expert can use the task, observations, state, and depth tokens, but not the discrete action target it is trained to predict.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Training", "weight": 1.0} -->

Fine-tuning. The MolmoAct2-Think-LIBERO checkpoint is fine-tuned from the depth-aware post-trained checkpoint using the same full-LIBERO recipe and compute budget as subsubsection 4.3.1: robot-only training on the combined Spatial, Object, Goal, and Long suites, with front-view then wrist-view camera order, 2100-token sequences, global batch size 64, 32 H100 GPUs, and 50K updates. We select the best checkpoint at 30K updates for evaluation.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Training", "weight": 1.0} -->

Fine-tuning differs from depth post-training in three targeted ways. First, we sample only action and depth-and-action examples, again uniformly, and remove the pure depth-prediction style. Second, because inference conditions on depth tokens predicted by the model rather than oracle depth tokens, we inject noise into the teacher-forced depth prefix during training: 10% of depth-code input tokens are replaced by uniformly sampled depth codes, while the prediction targets remain unchanged. Third, we add a learned per-layer gate on the depth portion of the action expert's per-layer KV conditioning. For action-expert layer ℓ, let M t = 1 denote positions belonging to the depth-output trigger, depth delimiters, or depth-code tokens, and let A t denote valid context positions.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Training", "weight": 1.0} -->

The gate is computed from the non-depth context of the corresponding VLM layer, and then applied only to depth-token keys and values: The gated (¯ K vlm ℓ, ¯ V vlm ℓ) are then projected into the action expert as in subsection 4.2. The gate is initialized with bias -4, so fine-tuning begins close to the standard action-conditioning path and learns how strongly each expert layer should use the depth prefix. Additional model-level details for the depth extension are summarized in subsection A.3.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Adaptive depth inference", "weight": 1.0} -->

Inference pipeline. At inference, MolmoAct2-Think uses the depth-and-action output style. Given the task, current observation, and proprioceptive state, the prompt requests <depth\_output><action\_output>. The model first performs a prefill over the prompt and images. If no depth cache is available, as at the beginning of a rollout or after a reset, it autoregressively predicts the full depth sequence: <depth\_start>, 100 depth-code tokens, and <depth\_end>.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Adaptive depth inference", "weight": 1.0} -->

When a depth cache is available, the model compares the current first observation image to the cached previous image using the same 10 × 10 RGB-patch cosine threshold described in subsection 5.1. Updated cells are generated by argmax decoding from the depth-token logits. Unchanged cells are replayed from the previous predicted depth buffer and consumed by the model as known depth-token inputs. Consecutive unchanged spans are replayed together, whereas changed spans are decoded token by token. After all 100 cells are filled, the model emits <depth\_end> and stores the current image and the newly filled 100-code depth buffer as the cache for the next control step.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Adaptive depth inference", "weight": 1.0} -->

The action is then generated from the depth-conditioned state. For continuous control, the action expert receives the VLM keys and values corresponding to the prompt plus the filled depth prefix and integrates the flow-matching velocity field to produce the action chunk. Adaptive depth changes only how the intermediate depth prefix is produced. The action interface remains the same as the depth-and-action training objective.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Adaptive depth inference", "weight": 1.0} -->

Table 3 Embodied reasoning results. We evaluate on benchmarks across spatial reasoning, pointing, and embodied QA tasks. The best-performing open-weight model on each benchmark is in bold, and the second best is underlined.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Adaptive depth inference", "weight": 1.0} -->

| Models/Benchmarks | Point-Bench | RefSpatial | RoboSpatial-Poi | Where2Place | BLINK | CV-Bench | ERQA | EmbSpatial | MindCube | RoboSpatial-VQ | SAT | OpenEQA | VSI-Bench | Overall Avg. | Inferenceoptimization. Adaptive depth inference introduces a different systems challenge from the continuous action expert: each frame can contain a different mixture of regenerated depth cell and replayed cached cells, so the overall decode schedule is data-dependent. Capturing the full adaptive loop would require a separate graph for each update pattern. We therefore keep the adaptive scheduler eager, including span-level replay for unchanged cells, while using a preallocated static KV cache to make the decode state stable across steps. For regenerated depth tokens, we capture the fixed-shape transformer work from post-attention through the next layer's pre-attention as CUDA Graph stages, and leave attention itself eager because its effective KV length changes throughout decoding. This preserves adaptive depth reuse while reducing the launch bubbles in the repeated one-token decode path.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experimental evaluation comprises one of the most extensive suites of studies of MolmoAct2, benchmarked against a diverse set of strong generalist baseline models. Specifically, we assess MolmoAct2 across three main categories of evaluation: (i) we examine how Molmo2-ER performs relative to generalist VLM models used as training backbones for VLAs, and quantify the performance gains attributable to a stronger backbone; (ii) we evaluate the out-of-the-box deployment capabilities of MolmoAct2 across a variety of embodiments; and (iii) we investigate the ease and efficiency with which MolmoAct2 can be adapted to novel tasks and unseen embodiments via fine-tuning.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Experiments", "weight": 1.0} -->

Hence, we evaluate MolmoAct2 across a comprehensive range of scenarios in both simulation and the real world, addressing the following research questions: 1. HowwelldoesMolmo2-ERperformonestablished industry benchmarks for embodied reasoning in VLMs? We address this question by benchmarking Molmo2-ER against strong open-source and proprietary VLMs across 13 established embodied reasoning benchmarks. 2. Howwell does MolmoAct2 perform out-of-the-box? We investigate this by evaluating MolmoAct2 on three benchmarks: two simulation benchmarks, MolmoBot and Molmo- Table 4 Results across MolmoSpace tasks. We evaluate all models on four manipulation skill categories-Pick, Pick & Place, Open, and Close-and report mean success rate (%) with standard error across three independent evaluation runs. Bold denotes the best and underline the second-best per task. MolmoAct2-DROID achieves the highest overall average (37.7), outperforming the strongest prior baseline π 0.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Experiments", "weight": 1.0} -->

5 -DROID (34.5) by +3.2 points, with particularly large gains on Pick (+7.3) and Pick & Place (+13.1), where contact-rich, multi-stage reasoning is required. On Close, MolmoAct2-DROID also sets a new best at 70.8, while on Open it trails the leading methods, suggesting that articulated-object interaction remains a direction for further improvement. Standard errors remain comparable across methods (≤ 3. 2), indicating that the observed gains are stable across runs rather than artifacts of evaluation variance.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Experiments", "weight": 1.0} -->

| Models/Tasks | Pick | Pick &Place | Open | Close | Average | Table5 Evaluationonsimulationheld-outenvironments. Simulation success rates are evaluated over 1000 episodes per task. For pick-and-place tasks, we report both oracle success (first number, which is the success conditions being fulfilled at any timestep) and success at end (second number, the success conditions being fulfilled at the final timestep). The delta between captures both unstable/unsuitable placement and the inability of policies to determine when a specified task is already completed, e.g. by repeatedly picking up an object which has already been placed correctly. We additionally report the half-width of the 95% confidence interval bounds for each result. Bold denotes the best and underline the second-best per task.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Experiments", "weight": 1.0} -->

| Models/Tasks | PickMSProc | Pick Classic | Pick | Pick Rand.-Cam. | Pick&Place | PnPNext-To | PnPColor | Avg. | Spaces, and a series of real-world zero-shot evaluations across two embodiments (DROID and SO-100/101 setups) against strong baselines pretrained or fine-tuned on the DROID and large-scale SO-100/101 datasets. 3. Howeffectively can MolmoAct2 be fine-tuned for new tasks and embodiments? We study this by finetuning MolmoAct2 on custom datasets collected across three benchmarks: two simulation benchmarks, RoboEval and LIBERO, and one large-scale real-world evaluation suite consisting of in-the-wild bimanual YAM tasks. 4. Doadaptive depth-perception tokens improve the performance of MolmoAct2-Think? We investigate this question by comparing MolmoAct2 against MolmoAct2-Think on LIBERO, MolmoSpace, and the MolmoBot Benchmark.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Experiments", "weight": 1.0} -->

5. Howrobust is MolmoAct2 under out-of-distribution perturbations? To investigate this, we fine-tune MolmoAct2-Post checkpoint on 4 tasks from the real-world Bimanual YAM benchmark and evaluate each task under 4 distinct out-of-distribution variants. 6. What is the quality of MolmoAct2's trajectory rollouts beyond raw success rate? For real-world deployment, trajectory quality matters beyond task success (e.g., stability, smoothness). We therefore evaluate MolmoAct2 against strong generalist baselines on RoboEval to assess the quality of the trajectories it generates while solving the tasks. 7. Which components contributed the largest performance gains to MolmoAct2? We investigate this question through systematic component-level ablations on the MolmoAct2 architecture and training configurations to understand how each of our novel improvements contributes to the model's performance, and we verify our findings on LIBERO for reproducibility.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Experiments", "weight": 1.0} -->

Table 6 Success rates (%) across manipulation tasks. Each cell reports the percentage of successful trajectories out of 15 trials. Bold denotes the best and underline the second-best per task.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Experiments", "weight": 1.0} -->

| Models/Tasks | Apple onplate | Pipette in tray | Redcubeintaperoll | Knife in box | Objects in bowl | Average | Table 7 Success rates (%) across manipulation tasks on the SO-100 platform. Each cell reports the mean score over 15 trials, where partial credit is awarded for sub-task completion (0.25 for reaching, 0.5 for pickup, 1.0 for successful placement). Bold denotes the best and underline the second-best per task.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Experiments", "weight": 1.0} -->

| Models/Tasks | Fork onplate | Stack blocks | Tissues in basket | Penonnotebook | Block in box | Average | 8. How fast is MolmoAct2 at inference? We measure end-to-end inference latency and control rate for MolmoAct2 and MolmoAct2-Think on LIBERO, and evaluate the impact of our caching and CUDA Graph optimizations.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Molmo2-ERevaluation", "weight": 1.0} -->

Evaluation setup. We evaluate Molmo2-ER on 13 established vision-language benchmarks that are widely used to measure the embodied reasoning capabilities of VLMs: Point-Bench, RefSpatial, RoboSpatial-Point, Where2Place, BLINK, CV-Bench, ERQA, EmbSpatial, MindCube, SAT, OpenEQA, and VSI-Bench. Together, these benchmarks span visual question answering, 2D pointing, multi-image reasoning, ego-exo understanding, and video-based spatial reasoning.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Molmo2-ERevaluation", "weight": 1.0} -->

Baselines. We compare Molmo2-ER against a diverse set of proprietary VLMs, reasoning-oriented VLMs, and open-weight VLMs, including the Gemini family, the GPT-5 family, LLaVA-OneVision, the Qwen3-VL family, and InternVLA. We additionally compare against Molmo2, the base model from which Molmo2-ER is trained.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Molmo2-ERevaluation", "weight": 1.0} -->

Results. Molmo2-ER outperforms all baseline VLMs on 9 of the 13 benchmarks and achieves the highest overall average score of 63.8%, exceeding the runner-up, Gemini-ER 1.5 Thinking, by 2.5 points. Notably, Molmo2-ER improves over its base model Molmo2 by 17%, demonstrating the substantial gains in embodied reasoning capability conferred by our approach.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Out-of-the-box deployment", "weight": 1.0} -->

Evaluation setup and baselines. To verify the out-of-the-box deployment capability of MolmoAct2, we evaluate it in both simulation and real-world settings. In simulation, we evaluate the MolmoAct2-DROID checkpoint on two benchmarks: MolmoSpaces and MolmoBot. Both target single-cycle pick-and-place tasks across diverse objects and environments, with MolmoBot featuring more challenging objects and scenarios. Each benchmark replicates the original DROID setup, enabling zero-shot evaluation of any policy pretrained or fine-tuned on the DROID dataset. On MolmoSpaces, we compare MolmoAct2-DROID against LAP-VLA, StereoVLA, π 0 -DROID, and π 0. 5 -DROID; on MolmoBot, we compare against LAP-VLA, π 0. 5 -DROID, and X-VLA. All simulation evaluations strictly follow the protocols, trial counts, and procedures of the respective original papers. Further details are provided in the Appendix.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Out-of-the-box deployment", "weight": 1.0} -->

In the real world, we test MolmoAct2-DROID and MolmoAct2-SO100/101 on their respective pretrained embodiment setups under challenging out-of-distribution conditions: camera poses are randomly initialized without conforming to any dataset visual distribution, using two cameras (wrist and a single allocentric view); all objects are unseen during training; and the environments themselves are out-of-distribution relative to the training data. For the DROID embodiment, we compare MolmoAct2-DROID against π 0. 5 -DROID, fine-tuned on the DROID dataset, and MolmoBot, fine-tuned on the large-scale MolmoSpaces dataset. We evaluate on five tasks ranging from single- to multi-object pick-and-place: apple\_on\_plate, pipette\_in\_tray, red\_cube\_in\_tape\_roll, knife\_in\_box, and objects\_in\_bowl.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Out-of-the-box deployment", "weight": 1.0} -->

For the SO-100/101 setup, we use the SO-100 robot, retaining the wrist camera and adding a third-person external camera with a randomly initialized position. We compare MolmoAct2SO100/101 against SmolVLA and π 0 -SO100/101, a variant of π 0 that we fine-tuned on MolmoAct2-SO100/101 Dataset. Both baselines are pretrained or fine-tuned at scale on the SO-100/101 dataset. We evaluate five pick-and-place tasks with novel objects and randomly initialized camera poses. Every real-world policy is assessed over 15 trials, with partial credit awarded for near-successful executions. Further details are provided in the Appendix.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Out-of-the-box deployment", "weight": 1.0} -->

Results. MolmoAct2-DROID achieves strong zero-shot performance on all DROID-style setups, in both simulation and the real world. In simulation, MolmoAct2-DROID is the state-of-the-art VLA model across MolmoSpaces and MolmoBot, outperforming all baselines on both benchmarks. π 0. 5 -DROID is the runner-up on each, with MolmoAct2 achieving an absolute gain of + 10. 6% on MolmoBot and + 3. 2% on MolmoSpaces, averaged across tasks; trial counts in every case are sufficient for statistical significance. In real-world evaluation on the DROID setup, which is substantially more out-of-distribution given the random camera initialization and entirely novel scenes and objects relative to the DROID dataset, MolmoAct2 again attains the highest performance, reaching 87. 1% and surpassing the runner-up MolmoBot by 38. 7%. On the second zero-shot embodiment, SO-100/101, MolmoAct2-SO100/101 reaches 56. 7%, an 11.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Out-of-the-box deployment", "weight": 1.0} -->

4% gain over our open implementation of π 0 on SO-100/101, demonstrating affordable deployment on low-cost robots such as the SO-100/101.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Effective fine-tuning", "weight": 1.0} -->

Evaluationsetupsandbaselines. For rapid real-world deployment on novel tasks and embodiments, VLAs must adapt from only a handful of demonstrations. To assess MolmoAct 's capacity for such efficient adaptation, we benchmark it against several strong VLA baselines on downstream tasks, domains, and embodiments unseen during training. In all fine-tuning experiments, we initialize from the MolmoAct2-Post checkpoint and fine-tune on the benchmark-specific training data.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Effective fine-tuning", "weight": 1.0} -->

Table8 LIBERObenchmarksuccessrates across four task categories (Spatial, Object, Goal, and Long-horizon) along with the average performance. MolmoAct2 achieves the highest overall average success rate of 97.2%, outperforming all strong baselines, with strong performance across all categories, particularly scoring 100% on the LIBERO-Object tasks. Furthermore improvement could be seem going from MolmoAct2 to MolmoAct2-Think. Bold denotes the best and underline the second-best per task.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Effective fine-tuning", "weight": 1.0} -->

| Baseline | Spatial | Object | Goal | Long | Average | In simulation, we evaluate on two benchmarks. RoboEval comprises a bimanual Franka Emika Panda setup with human-expert demonstrations across 8 tasks requiring bimanual coordination. LIBERO, following prior work, consists of four task suites-LIBEROSpatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long-each containing 500 demonstrations across 10 tasks. We fully fine-tune MolmoAct2 and compare it against state-of-the-art VLAs trained under similar protocols, including TraceVLA, OpenVLA, SpatialVLA, CoT-VLA, π 0, ThinkAct, MolmoAct, GR00T-N1, π 0. 5, and NORA-1.5.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Effective fine-tuning", "weight": 1.0} -->

For real-world evaluation, we conduct a large-scale, systematic study on both a bimanual YAM setup and a mobile bimanual YAM setup, covering 8 tasks that span static laboratory settings, in-the-wild environments (kitchen, study room, pantry, and wet labs), and mobile manipulation. The tasks-stack\_cups, store\_test\_-tubes, store\_candy, hang\_tools, store\_toys, shelf\_cups, prepare\_pipette, and make\_popcorn -are each evaluated over 50 trials, with three spatial variants per task used for data collection. We fine-tune from the MolmoAct2-Post checkpoint for every task and compare against four strong VLA and world-model baselines: Cosmos Policy, X-VLA, OpenVLA-OFT, and π 0. 5 -DROID.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Effective fine-tuning", "weight": 1.0} -->

Results. On LIBERO, MolmoAct2 achieves an average success rate of 97.2%, the highest among all compared methods-reaching 100% on LIBERO-Object and improving over our previous MolmoAct-7B-D by 10.6%. This trend is reinforced on RoboEval, where MolmoAct2 attains a 44.3% success rate, surpassing the second-best model, π 0. 5, by 3.8%. In the real-world evaluation, MolmoAct2 outperforms all baselines on 7 of 8 deployment tasks, achieving an average success rate of 50.1%-15% above the runner-up, OpenVLA-OFT. Hence, MolmoAct2 demonstrate its effectiveness for rapid adaptation to new tasks, domains, and embodiments.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Performance of MolmoAct2-Think", "weight": 1.0} -->

To isolate the contribution of MolmoAct2-Think, we fine-tuned it with the adaptive-depth training pipeline and compared it against MolmoAct2, fine-tuned from MolmoAct2-Post under the standard recipe on Real-world evaluation on Bimanual YAM tasks LIBERO. MolmoAct2-Think improves over MolmoAct2 on three of the four task suites and matches it on the fourth, where the baseline is already saturated at 100%. Crucially, the largest gain (+2.2%) appears on the most challenging suite, where the baseline leaves the most headroom (93.2%), while gains on the easier suites are correspondingly smaller as performance approaches ceiling. Averaged across all suites and 2,000 rollouts, MolmoAct2-Think achieves 98.1% versus 97.2%, a +0.9% improvement that is consistent in sign and concentrated where the task is hardest which indicates that the adaptive-depth pipeline yields a real, non-incidental gain rather than noise around saturation.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Robustness of MolmoAct2 to out-of-distribution shifts", "weight": 1.0} -->

Evaluation setup and baselines. To investigate how robustly MolmoAct2 transfers after parameter-efficient fine-tuning on a new dataset, we select 4 of the 8 real-world bimanual tasks ( stack\_cups, store\_test\_tubes, store\_candy, and prepare\_pipette ) and fine-tune a separate checkpoint for each on top of MolmoAct2Post. At test time, we evaluate each checkpoint under four out-of-distribution variants: spatial, in which we place the target objects at locations outside the training distribution; lighting, in which we alter the illumination of the scene; language variants, in which we rephrase the language instruction in three different ways; and distractors, in which we add unseen distractor objects while keeping the original in-distribution spatial layout. We compare MolmoAct2 to strong baselines such as π 0. 5, Cosmos Policy, X-VLA, and OpenVLA-OFT.For each task each set, we will evaluate 20 trials, 5 trials for each perturbation.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Robustness of MolmoAct2 to out-of-distribution shifts", "weight": 1.0} -->

Results. Based on the evaluation, we find that MolmoAct2 is substantially more robust to perturbations than all other evaluated models, achieving a 50.7% average success rate across all perturbation types, with a margin of ∼ 10.8% over the second-best model, OpenVLA-OFT. While MolmoAct2 leads on every perturbation category, its advantage is narrowest on Distractor (a 5.8% margin over OpenVLA-OFT), and it attains its lowest absolute score on Spatial Variance (26.25%), indicating room for improvement on fine-grained spatial generalization.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Robustness of MolmoAct2 to out-of-distribution shifts", "weight": 1.0} -->

Table 9 Robustness of MolmoAct2 under environmental perturbations. We evaluate MolmoAct2 against four baselines on out-of-distribution scenarios spanning spatial variation, lighting, language rephrasing, and visual distractors. MolmoAct2 is the most robust, achieving an average success rate of 50.69% across all perturbation types-a 10.80% absolute improvement over the next-best model. Values report average success rates (%); bold = best, underline = second-best.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Robustness of MolmoAct2 to out-of-distribution shifts", "weight": 1.0} -->

| Model | Spatial Var. | Lighting | Language | Distractor | Overall |

<!-- chunk {"id": "body-0122", "role": "body", "section": "Quality of MolmoAct2 trajectories for real-world deployment", "weight": 1.0} -->

While task success is a necessary measure of performance, it is insufficient for assessing readiness for real-world deployment. In practical settings, trajectory quality directly impacts efficiency, stability, and safety. We therefore evaluate MolmoAct2 fi ne-tuned on RoboEval for beyond success rates using a suite of behavioral and outcome metrics from RoboEval, summarized in Fig. 6B. Across tasks, MolmoAct2 demonstrates consistent improvements in efficiency-related metrics. For example, on Stack Two Blocks, MolmoAct2 reduces completion time from 5. 87 s ( π 0. 5 ) and 7. 27 s (Diffusion) to 4. 70 s, while also reducing joint path length from 2. 16 to 1. 04 (approximately 2 × shorter). Similar trends hold on longer-horizon tasks such as Rotate Valve, where MolmoAct2 achieves the lowest completion time ( 8. 51 s vs. 9. 69 s for π 0. 5 ), along with reduced trajectory length.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Quality of MolmoAct2 trajectories for real-world deployment", "weight": 1.0} -->

In addition to efficiency, MolmoAct2 exhibits strong performance on stability-related metrics. As shown in Fig. 6B, MolmoAct2 consistently operates near the best normalized value across both Cartesian and joint-space measures, indicating smoother and more stable trajectories compared to baselines. In contrast, other methods exhibit greater variability across these metrics, suggesting less consistent control behavior. Together, these results show that MolmoAct2 not only improves task success, but also produces shorter, more stable, and more efficient trajectories, which are critical properties for real-world deployment.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

We ablate the main design choices in MolmoAct2 on LIBERO to isolate where the performance gains come. Unless otherwise noted, all variants use the same data, image augmentation, action normalization, action horizon, and evaluation protocol as the corresponding LIBERO fine-tuning run. For the full-suite ablations, each row is evaluated on Spatial, Object, Goal, and Long, and the average is computed across the four suites.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

Embodied-reasoning backbone. We first test whether the Molmo2-ER backbone improves action learning even before the continuous action expert is introduced. We directly fine-tune Molmo2 and Molmo2-ER with the same discrete-action architecture on the single LIBERO Long task suite, using action tokens produced by MolmoAct2-FAST Tokenizer and no continuous action expert. Both models are trained for 60,000 steps with the same configuration. As shown in Table 10, replacing Molmo2 with Molmo2-ER improves success from 77.6% to 83.6%, a 6.0-point gain. This confirms that the embodied-reasoning specialization is not only useful for VLM benchmarks, but also transfers directly into action-token prediction.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

Table 10 Backboneablation on LIBERO Long. Both variants are trained directly from the VLM checkpoint with only discrete action prediction using MolmoAct2-FAST Tokenizer. The final row is marked in pink, which is what we initialize with for MolmoAct2-Pretrain.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

| Backbone | Action objective | Long | VLM-to-expert conditioning. We next ablate how the continuous action expert receives context from the VLM. All variants start from MolmoAct2-Pretrain, attach an action expert directly, and use the same LIBERO training configuration. We compare hidden-state conditioning, standard per-layer KV conditioning, and a per-head per-layer KV conditioning variant. In the standard design, the VLM key and value heads at each token are flattened before learned projections map them into the action expert cross-attention space. In the per-head variant, the VLM keys and values remain separated by head, and each head is projected into the corresponding action-expert head. This preserves the head structure, but requires the number of VLM KV heads to match the number of action-expert KV heads; we use 8 for both in all settings. The standard per-layer KV conditioning is strongest on average, reaching 95.9%, compared with 94.8% for the per-head variant and 94.0% for hidden-state conditioning (Table 11). Hidden-state conditioning is competitive on Spatial, but it drops more on Object, Goal, and Long.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

This supports the architectural choice in Sec. 4.2.1, where the action expert consumes the same attention state used by the VLM rather than a single residual-stream representation.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

Table 11 Ablation of the VLM-to-action-expert conditioning source on LIBERO. All variants are trained from MolmoAct2-Pretrain with the same configuration. Bold denotes the best result per column. The final row is marked in pink, which is what we use in all MolmoAct2 and MolmoAct2-Think post-training and fine-tuning runs.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

| Conditioning source | Spatial | Object | Goal | Long | Average | Multiple flow samples. We then vary the number of flow samples K per action chunk while holding per-layer KV conditioning and all other training settings fixed. These runs also start from MolmoAct2-Pretrain without a prior post-training stage. Table 12 shows that increasing K generally improves average performance. K = 1 is the weakest overall at 94.15%, while K = 8 gives the best average at 95.90%. The effect is not monotonic on every suite, because Long benefits strongly from two flow samples, but the aggregate trend favors denser supervision along the flow trajectory.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

Table 12 Ablation of the number of flow samples on LIBERO. All rows use per-layer KV conditioning and are trained from MolmoAct2-Pretrain with the same configuration. Bold denotes the best result per column. The final row is marked in pink, which is what we stick to in all of MolmoAct2 and MolmoAct2-Think fi ne-tuning runs.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

| K | Spatial | Object | Goal | Long | Average | Fine-tuningdesign. Table 13 compares the final MolmoAct2 fi ne-tuning recipe against targeted alternatives along three axes: whether we co-train the discrete autoregressive action loss, whether we apply knowledge insulation to the flow-matching loss, and which parameters are updated. Removing discrete action co-training yields a similar average but shifts performance across suites, improving Long while reducing Spatial and Object. Adding knowledge insulation is also close but slightly worse than the final recipe. LoRA remains strong, especially on Spatial, but loses 2.8 points on Long relative to full fine-tuning. Tuning only the action expert is the clearest failure mode, dropping the average to 93.05%. Overall, full-model adaptation with discrete and continuous action co-training provides the best average outcome.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

Table 13 Ablation of MolmoAct2 fine-tuning design choices on LIBERO. Component columns indicate whether each design choice is enabled: ✓ denotes enabled and ✗ denotes disabled. Bold denotes the best result per column. The final row is the MolmoAct2-LIBERO recipe, where its training design is marked in pink, which is what we stick to in all of MolmoAct2 fi ne-tuning runs.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

| Discrete co-training | Knowledge insulation | Training type | Spatial | Object | Goal | Long | Average | Depth-awarefine-tuning. Finally, we ablate the MolmoAct2-Think depth fine-tuning recipe. The baseline uses both 10% depth-token noise and the learned per-layer depth gate described in Sec. 5.2, while uniformly mixing action-only and depth-and-action examples. Removing the depth-token noise and per-layer depth gate reduces the average from 98.10% to 97.65%, mostly through a 1.8-point drop on Goal. Removing mixed training as well, so that training uses only depth-and-action examples, reduces the average further to 97.50%. These results show that the depth pathway is most useful when it is regularized for imperfect inference-time depth predictions and when the policy retains a strong action-only path.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

Table 14 Ablation of MolmoAct2-Think depth fine-tuning choices on LIBERO. Mixed training denotes uniform sampling of action-only and depth-and-action examples. ✓ denotes enabled and ✗ denotes disabled. Bold denotes the best result per column. The final all-enabled row is the MolmoAct2-Think-LIBERO recipe, where its training design is marked in pink, which is what we stick to in all of MolmoAct2-Think fi ne-tuning runs.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Systematic analysis", "weight": 1.0} -->

| Mixed training | Noise injection | Depth gate | Spatial | Object | Goal | Long | Average |

<!-- chunk {"id": "body-0137", "role": "body", "section": "Inference speed", "weight": 1.0} -->

We measure end-to-end action-generation latency on LIBERO using a single H100 GPU and an action horizon of 10, and report the amortized control rate as action horizon divided by latency. We compare three inference paths: the original implementation, an optimized eager path using reusable-cache optimizations, and the same optimized path with CUDA Graph replay enabled.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Inference speed", "weight": 1.0} -->

As shown in Figure 8, caching alone improves MolmoAct2 from 23.02 Hz to 27.39 Hz and MolmoAct2Think from 8.04 Hz to 9.72 Hz. Enabling CUDA Graphs gives the larger gain: MolmoAct2 reaches 55.79 Hz, a 2.42 × speedup over the original path, while MolmoAct2-Think reaches 12.71 Hz, a 1.58 × speedup. MolmoAct2 benefits substantially from CUDA Graph replay: its fixed-shape flow-matching steps form a regular, repeated computation pattern whose runtime is dominated by kernel launch overhead, which graph replay largely eliminates. MolmoAct2-Think sees a smaller gain, since its adaptive-depth stage performs autoregressive decoding, whose sequential dependencies and variable-length execution are less amenable to graph capture.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Inference speed", "weight": 1.0} -->

Measured on H100 with action horizon 10 on LIBERO.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Inference speed", "weight": 1.0} -->

MolmoAct2 also exposes a discrete action path, in which the VLM autoregressively decodes action tokens for the entire action chunk. We measured this path under the same optimized graph as above. MolmoAct2 runs at 14.17 Hz and MolmoAct2-Think at 6.82 Hz i.e., 3. 94 × and 1. 86 × slower than the corresponding continuous path. This gap comes from the large VLM decoding overhead, while the action expert emits the entire chunk in a small fixed number of flow matching steps through a smaller cross-attention head, with the VLM cache reused across steps. We therefore use the continuous path as the default deployment option.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced MolmoAct2, a family of fully open action reasoning models built for real-world deployment across heterogeneous robot platforms. Building upon a spatially specialized Molmo2-ER backbone, MolmoAct2 produces performant and geometrically grounded behaviors across diverse manipulation tasks. We additionally release MolmoAct2 -Think, a thinking variant equipped with adaptive depth reasoning that delivers interpretable, depth-aware control with efficient inference. Our evaluations across simulation and real-world settings demonstrate that MolmoAct2 consistently outperforms strong VLA baselines out-of-thebox, fine-tunes efficiently from a handful of demonstrations, and transfers across three structurally different embodiments spanning the low-to-medium cost range. We release all model weights, training code, and data, including MolmoAct2-BimanualYAM Dataset, the largest open bimanual manipulation dataset to date, alongside MolmoAct2-DROID Dataset and MolmoAct2-SO100/101 Dataset, to enable reproducibility and foster community-driven research toward open foundation models that researchers and practitioners can both build on and deploy in the real world.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Author contributions", "weight": 1.0} -->

- Haoquan Fang: Led the design and implementation of the MolmoAct2 model, training, and inference pipelines and infrastructure; contributed to data curation, evaluations, and writing. - Jiafei Duan: Led the project and core method design; proposed and curated MolmoAct2-BimanualYAM Dataset; led paper writing and the design of all simulation and real-world evaluations.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Author contributions", "weight": 1.0} -->

All other contributors are also deeply appreciated for their effort, which is critical to the success of the MolmoAct2 project.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Author contributions", "weight": 1.0} -->

- DonovanClay: Led the training and curation of MolmoAct2-FAST Tokenizer - SamWang: Led the curation and filtering of the pre-training data mixture for MolmoAct2 - Weikai Huang: Led the curation and training of Molmo2-ER - Xiang Fan: Led the development of MolmoAct2-Think - Shirui Chen: Led the curation of MolmoAct2-SO100/101 Dataset - Shanli Xing: Led the inference optimization of MolmoAct2 and MolmoAct2-Think - For real-world robot infrastructure: Shuo Liu, Wei-Chuan Tsai, Ying-Chun Lee, Shanli Xing, Angad Wadhwa and Rose Hendrix - For real-world data collection, curation, and evaluation: Jiafei Duan, Donovan Clay, Angad Wadhwa, Suveen Ellawela, Lucas Ngoo, Cole Harrison and Sam Wang - For simulation training and evaluation: Yi Ru Wang, Haoquan Fang, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, and Peter Sushko - For paper writing and figures: Jiafei

<!-- chunk {"id": "body-0145", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Duan, Haoquan Fang, Zhongzheng Ren, Shirui Chen, Jaemin Cho, Cole Harrison, Donovan Clay, Sam Wang, Shuo Liu, Xiang Fan, Winson Han, and Eli VanderBilt - For project management: Karen Farley. - For research advisory: Ranjay Krishna, Dieter Fox, Joyce Chai, Zhongzheng Ren, and Ali Farhadi. - Project PI: Ranjay Krishna
