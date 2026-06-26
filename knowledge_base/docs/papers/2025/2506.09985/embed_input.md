<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

Topics include Robotics, Large language models, Language models, Self-supervised learning, Supervised learning, Datasets, Accuracy, Planning, Learning, V-JEPA 2.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on Something-Something v2) and state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100) surpassing previous task-specific models. Additionally, after aligning V-JEPA 2 with a large language model, we demonstrate state-of-the-art performance on multiple video question-answering tasks at the 8 billion parameter scale (e.g., 84.0 on PerceptionTest, 76.9 on TempCompass).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we show how self-supervised learning can be applied to robotic planning tasks by post-training a latent action-conditioned world model, V-JEPA 2-AC, using less than 62 hours of unlabeled robot videos from the Droid dataset. We deploy V-JEPA 2-AC zero-shot on Franka arms in two different labs and enable picking and placing of objects using planning with image goals. Notably, this is achieved without collecting any data from the robots in these environments, and without any task-specific training or reward. This work demonstrates how self-supervised learning from web-scale data and a small amount of robot interaction data can yield a world model capable of planning in the physical world.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Humans have the ability to adapt and generalize when taking on new tasks and operating in unfamiliar environments. Several cognitive learning theories suggest that humans learn an internal model of the world by integrating low-level sensory inputs to represent and predict future states, and they further posit that this world model shapes our perception at any given moment, playing a crucial role in informing our understanding of reality. Moreover, our ability to predict the effects of our actions on future states of the world is also essential for goal-oriented planning. Building artificial agents that learn a world model from sensory data, such as video, could enable them to *understand* the physical world, *predict* future states, and effectively --- like humans --- *plan* in new situations, resulting in systems capable of tackling tasks that have not been encountered before.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Previous works have explored the development of predictive world models from interaction data consisting of state-action sequences, often also relying on explicit reward feedback from the environment to infer goals. However, the limited availability of real-world interaction data constrains the scalability of these methods. To address this limitation, more recent works have leveraged both internet-scale video and interaction data towards training action-conditioned video generation models for robot control, but only demonstrate limited results in robot execution using model-based control. In particular, this line of research often emphasizes the evaluation of the faithfulness of the predictions and visual quality instead of planning capabilities, perhaps due to the computational cost of planning by generating video.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we build upon the self-supervised hypothesis as a means to learn world models that capture background knowledge of the world largely from observation. Specifically, we leverage the joint-embedding predictive architecture (JEPA), which learns by making predictions in a learned representation space. In contrast to approaches that focus on learning entirely from interaction data, self-supervised learning enables us to make use of internet-scale video --- depicting sequences of states without direct observations of the actions --- to learn to both represent video observations and learn a predictive model for world dynamics in this learned representation space. Furthermore, in contrast to approaches based on video generation, the JEPA approach focuses on learning representations for predictable aspects of a scene (e.g., the trajectory of an object in motion) while ignoring unpredictable details that generative objectives emphasize, since they make pixel-level predictions (e.g., the precise location of each blade of grass in a field, or each leaf on a tree).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By scaling JEPA pretraining, we demonstrate that it yields video representations with state-of-the-art understanding and prediction capabilities, and that such representations can be leveraged as a basis for action-conditioned predictive models and enable zero-shot planning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach, V-JEPA 2, utilizes a stage-wise training procedure, beginning with action-free pre-training on internet-scale video, followed by post-training with a small amount of interaction data (see Figure˜1). In the first stage, we use a mask-denoising feature prediction objective, where the model predicts masked segments of a video in a learned representation space. We train the V-JEPA 2 encoder with up to 1 billion parameters and with more than 1 million hours of video. Our experiments confirm that scaling self-supervised video pretraining enhances the encoder's ability to achieve visual understanding, including broad motion and appearance recognition capabilities, through probe-based evaluations and by aligning the encoder with a language model for video question-answering.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following pretraining on internet-scale video, we train an action-conditioned world model, V-JEPA 2-AC, on a small set of interaction data using the representations learned in the first stage. Our action-conditioned world model is a 300M-parameter transformer network employing a block-causal attention mechanism, which autoregressively predicts the representation of the next video frame conditioned on an action and previous states. With as little as 62 hours of unlabeled interaction data from the Droid dataset, we demonstrate the feasibility of training a latent world model that, given sub-goals, can be leveraged to plan actions on a Franka robot arm and perform prehensile manipulation tasks from a monocular RGB camera zero-shot in a new environment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To summarize, we show that joint-embedding predictive architectures learning from videos can be used to build a world model that enables *understanding* the physical world, *predicting* future states, and effectively *planning* in new situations; this is achieved by leveraging internet-scale video and a small amount of interaction data. Specifically: Understanding --- Probe-based Classification: Scaling self-supervised video pretraining results in video representations applicable to many tasks. V-JEPA 2 excels at encoding fine-grained motion information, achieving strong performance on tasks requiring motion understanding, such as Something-Something v2, with $77.3$ top-1 accuracy using an attentive probe.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Understanding --- Video Question-Answering: V-JEPA 2 encoder can be used to train a multi-modal large language model, to tackle video-question answering tasks. We observe state-of-the-art performance on 8B language model class on multiple benchmarks that require physical world understanding and temporal reasoning, such as MVP ($44.5$ paired accuracy), PerceptionTest ($84.0$ test set accuracy), TempCompass ($76.9$ multi-choice accuracy), TemporalBench ($36.7$ multi-binary short-QA accuracy) and TOMATO ($40.3$ accuracy). In particular, we show that a video encoder pre-trained without language supervision can be aligned with a language model and achieve state-of-the-art performance, contrary to conventional wisdom.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prediction: Large-scale self-supervised video pretraining enhances prediction capabilities. V-JEPA 2 achieves state-of-the-art performance on the Epic-Kitchens-100 human-action anticipation task using an attentive probe, with $39.7$ recall-at-5, which is a $44$% relative improvement over the previous best model.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning: We demonstrate that V-JEPA 2-AC, obtained by post-training V-JEPA 2 with only $62$ hours of unlabeled robot manipulation data from the popular Droid dataset, can be deployed in new environments to solve prehensile manipulation tasks using planning with given subgoals. Without training on any additional data from robots in our labs, and without any task-specific training or reward, the model successfully handles prehensile manipulation tasks, such as Grasp and Pick-and-Place with novel objects and in new environments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section˜2 describes the V-JEPA 2 pretraining procedure, including the key ingredients enabling scaling beyond the original V-JEPA recipe of Bardes et al.. Section˜3 then introduces our approach to training a task-agnostic action-conditioned world model, V-JEPA 2-AC, leveraging the pretrained V-JEPA 2 model. Section˜4 demonstrates using V-JEPA 2-AC for robot control via model-based planning. Because V-JEPA 2-AC models world dynamics in a learned representation space, its capabilities fundamentally depend on the information captured in the V-JEPA 2 representation space, and so we further explore the performance of V-JEPA 2 for video understanding in Section˜5 and prediction tasks in Section˜6. Finally, in Section˜7 we show that V-JEPA 2 can be aligned with a language model for video question answering. Section˜8 discusses related work, and we conclude in Section˜9.

<!-- chunk {"id": "body-0015", "role": "body", "section": "V-JEPA 2: Scaling Self-Supervised Video Pretraining", "weight": 1.0} -->

We pretrain V-JEPA 2 on a visual dataset that includes over 1 million hours of video. The self-supervised training task is based on mask denoising in representation space and builds upon the V-JEPA framework. In this paper, we extend the V-JEPA framework by exploring larger-scale models, increasing the size of the pretraining data, and introducing a spatial and temporal progressive resolution training strategy that enables us to efficiently pretrain models beyond short 16-frame video clips.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Mask-Denoising in Representation Space", "weight": 1.0} -->

The V-JEPA objective aims to predict the learned representation of a video $y$ from a view $x$ of that video that has been masked, i.e., from which patches have been randomly dropped (Figure˜2, left). The task meta-architecture consists of an encoder, $E_{\theta}(\cdot)$, which extracts video representations, and a predictor, $P_{\phi}(\cdot)$, which predicts the representation of masked video parts. The encoder and predictor are trained simultaneously using the objective, where $\Delta_{y}$ is a learnable mask token that indicates the locations of the dropped patches. The loss uses a stop-gradient operation, $\text{sg}(\cdot)$, and an exponential moving average, $\overline{\theta}$, of the weights $\theta$ of the encoder network to prevent representation collapse. The loss is applied only to the predictions of the masked patches.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Architecture", "weight": 1.0} -->

The encoder, $E_{\theta}(\cdot)$, and predictor, $P_{\phi}(\cdot)$, are each parameterized as a vision transformer (or ViT). To encode relative position information in the vision transformer, we leverage RoPE (Rotary Position Embedding) instead of the absolute sincos position embedding used in Bardes et al.. We use a 3D extension of traditional 1D-RoPE by partitioning the feature dimension into three approximately equal segments (for the temporal, height, and width axes) and applying the 1D rotations separately to the segment for each axis. We found that using 3D-RoPE instead of absolute sincos position embeddings helps stabilize training for the largest models. To process a video with our transformer encoder, we first patchify it as a sequence of tubelets of size $2\times 16\times 16$ ($T\times H\times W$) and employ the same multiblock masking strategy as in Bardes et al..

<!-- chunk {"id": "body-0018", "role": "body", "section": "Key Scaling Ingredients", "weight": 1.0} -->

In this section we introduce and study four additional key ingredients which enable scaling the V-JEPA pre-training principle to obtain our V-JEPA 2 model.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Key Scaling Ingredients", "weight": 1.0} -->

*Data scaling:* We increase the dataset size from 2 million to 22 million videos by leveraging and curating additional data sources.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Key Scaling Ingredients", "weight": 1.0} -->

*Model scaling:* We scale the encoder architecture from 300 million to over 1 billion parameters, going from a ViT-L to a ViT-g.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Key Scaling Ingredients", "weight": 1.0} -->

*Longer training:* Adopting a warmup-constant-decay learning rate schedule simplifies hyperparameter tuning and enables us to extend training from 90 thousand up to 252 thousand iterations, effectively leveraging the additional data.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Key Scaling Ingredients", "weight": 1.0} -->

*Higher resolution:* We leverage the warmup-constant-decay schedule to efficiently scale to higher resolution video and longer video clips by training on shorter, lower-resolution clips during the warmup and constant phases, and then increasing resolution and/or clip-length during the final decay phase.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Key Scaling Ingredients", "weight": 1.0} -->

The remainder of this section describes each of these ingredients in further detail and also quantifies the impact of each ingredient using the evaluation protocol described next.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

Our goal with model pretraining is to infuse general visual understanding into our encoder. We therefore evaluate our model and data design choices by assessing the quality of the model's learned representation on a set of six motion and appearance classification tasks: Something-Something v2, Diving-48, Jester, Kinetics, COIN, and ImageNet. We use a frozen evaluation protocol: we freeze the encoder weights and train a task-specific 4-layers attentive probe on its representation to output a predicted class. In this section, we focus mainly on the average accuracy across the six understanding tasks. Refer to Section˜5 for additional details about the tasks, evaluation protocol, and results.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Scaling Self-Supervised Video Learning", "weight": 1.0} -->

We first present a summary of the key findings of our scaling analysis, where we investigate the impact of the four key ingredients on downstream task average performance. Figure˜3 illustrates the effects of these scaling interventions on average accuracy across 6 classification tasks, using a ViT-L/16 model pretrained on 2 million videos with the V-JEPA objective as our baseline. Increasing the dataset from 2 million to 22 million videos (VM22M) yields a 1.0-point improvement. Scaling the model from 300 million to 1 billion parameters (ViT-g/16) provides an additional 1.5-point gain. Extending training from 90K to 252K iterations contributes another 0.8-point improvement. Finally, enhancing both spatial resolution ($256\rightarrow 384$) and temporal duration ($16\rightarrow 64$ frames), during both pretraining and evaluation, boosts performance to 88.2%, representing a cumulative 4.0-point improvement over the ViT-L/16 baseline. Each individual change provides a positive impact, confirming the potential of scaling in video self-supervised learning (SSL).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Pretraining Dataset", "weight": 1.0} -->

Next, we describe the sources of videos and images that make up our pretraining dataset, and our approach to curating the dataset.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Scaling Dataset Size", "weight": 1.0} -->

We construct a large-scale video dataset by combining publicly available data sources. Using publicly-available sources in this work enables other researchers to reproduce these results. The overall dataset includes ego-centric videos from the Something-Something v2 dataset (SSv2) introduced in Goyal et al., exo-centric action videos from the Kinetics 400, 600, and 700 datasets, YouTube tutorial videos from HowTo100M, and general YouTube videos from YT-Temporal-1B, which we refer to as YT1B. We also include images from the ImageNet dataset to increase the visual coverage of the pretraining data. To enable joint image and video pretraining, we duplicate an image temporally and treat it as a 16-frame video where all frames are identical. During training, we sample from each data source with a weighting coefficient that we determined empirically via manual tuning. The resulting dataset, which we refer to as VideoMix22M (or VM22M), consists of 22 million samples. Table˜1 lists these data sources and their weights.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Scaling Dataset Size", "weight": 1.0} -->

Figure˜4 (Left) compares the performance of a ViT-L/16 pretrained on VM22M with a similar model trained on the smaller (2 million) VideoMix2M dataset from Bardes et al.. Training on VM22M leads to a $+1$ point improvement on average performance on visual understanding tasks, compared to VM2M. Performance improvement is more prominent on appearance-based tasks such as Kinetics-400, COIN, and ImageNet, showing the importance of increasing visual coverage for those tasks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Data Curation", "weight": 1.0} -->

YT1B is a large video dataset, consisting of 1.4 million video-hours, with no curation and minimal filtering compared to smaller video datasets (like Kinetics and Something-Something v2). Because uncurated and unbalanced data can hinder model performance, we filter YT1B by adapting an existing retrieval-based curation pipeline to handle videos. Specifically, we extract scenes from YT1B videos, compute an embedding vector for each scene, and then use a cluster-based retrieval process to select video scenes according to a target distribution, which is composed of the Kinetics, Something-Something v2, COIN and EpicKitchen training datasets. We describe the details of the dataset construction procedure in Section˜10.2. Similar to Oquab et al., we ensure that none of the videos from the target validation sets are contained in the initial, uncurated data pool.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data Curation", "weight": 1.0} -->

In Figure˜4 (Right), we compare the average performance on visual understanding evaluations between a ViT-L model pretrained on uncurated YT-1B data and a comparable model trained on our Curated-YT-1B dataset. Training with the curated dataset yields a $+1.4$ point average performance improvement over the uncurated baseline. Notably, the Curated-YT-1B-trained model achieves competitive performance relative to the full VM22M dataset at the ViT-L scale. However, larger-scale models benefit more from VM22M training (see Section˜10.2), suggesting that combining Curated-YT-1B with other data sources enhances scalability.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scaling Model Size", "weight": 1.0} -->

To explore the scaling behavior of our model, we trained a family of encoder models with parameter counts ranging from 300 million (ViT-L) to 1 billion (ViT-g) parameters. All encoder architecture details are provided in Table˜12 in the appendix. Note that each encoder uses the same predictor architecture, similar to a ViT-small. We report the average performance of these encoders on visual understanding tasks in Figure˜5 (Left). Scaling the model size from 300 million (ViT-L) to 1 billion (ViT-g) parameters yields a $+1.5$ points average performance improvement. Both motion and appearance understanding tasks benefit from scaling, with SSv2 improving by $+1.6$ points and Kinetics by $+1.5$ points (cf.Table˜4). These results confirm that self-supervised video pretraining effectively leverages larger model capacities, up to the 1B-parameter ViT-g.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Training Schedule", "weight": 1.0} -->

V-JEPA 2 model training employs a warmup-constant learning rate schedule followed by a cooldown phase. Similarly to Hägele et al., we found that this schedule performs comparably to a half-cosine schedule; it also makes exploring long training runs more cost-effective, since multiple cooldown runs can be started from different checkpoints of the constant phase. We simplified the recipe from Bardes et al. by maintaining fixed teacher EMA and weight decay coefficients instead of using ramp-up schedule, as these variations showed minimal impact on downstream understanding tasks. Figure˜3 shows that extending the training schedule from 90K to 252K iterations yields a +0.8 average performance improvement with ViT-g models, validating the benefits of extended training durations. This schedule also facilitates progressive training by incrementally increasing video resolution during the cooldown phase.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Efficient Progressive-Resolution Training", "weight": 1.0} -->

While most previous video encoders focus on short clips of 16 frames (roughly seconds), we explore training with longer clips of up to 64 frames (16 seconds) at higher spatial resolutions. However, training time increases dramatically with longer durations and higher resolutions --- training our ViT-g model on $64\times 384\times 384$ inputs would require roughly $60$ GPU-years (see Figure˜5, Middle). To reduce this, we adopt a progressive resolution strategy that boosts training efficiency while maintaining downstream performance. Our training process begins with a warmup phase where we train on 16-frame, $256\times 256$-resolution videos with linear learning rate warmup over 12K iterations, followed by a main training phase with a constant learning rate for 228K iterations. Then, during the cooldown phase, we increase video duration and resolution while linearly decaying the learning rate over 12K iterations. Hence the additional computational overhead associated with training on longer-duration, higher-resolution videos is only incurred during the final cooldown phase.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Efficient Progressive-Resolution Training", "weight": 1.0} -->

This approach enables efficient high-resolution training: as shown in Figure˜5 (Middle), we achieve an $8.4\times$ reduction in GPU time for a model that can ingest 64-frame, $384\times 384$ resolution inputs, compared to directly training such a model from scratch at full resolution throughout all phases of training. Furthermore, we still observe the benefits of a model that can process longer-duration and higher-resolution inputs as discussed next.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Scaling temporal and spatial video resolution", "weight": 1.0} -->

Figure˜5 examines how input video resolution affects downstream task performance. When increasing clip duration from 16 to 64 frames during pretraining while maintaining a fixed 16-frame evaluation duration, we observe a $+0.7$ percentage point average performance improvement (Figure˜5, Right). Additionally, we see that increasing the video duration and resolution during evaluation leads to a significant improvement across the tasks (refer to Table˜4 and Section˜10.4.2). These results demonstrate that video self-supervised pretraining benefits from increased temporal resolution during both training and evaluation. Although we experimented with scaling to even longer video clips (128 and 256 frames), we did not observe any further improvement beyond 64 frames on this set of understanding tasks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-JEPA 2-AC: Learning an Action-Conditioned World Model", "weight": 1.0} -->

After pre-training, the V-JEPA 2 model can make predictions about missing part in videos. However, these predictions do not directly take into account the causal effect of actions that an agent might take. In the next stage of training, described in this section, we focus on making the model useful for planning by leveraging a small amount of interaction data. To that end, we learn a frame-causal action-conditioned predictor on top of the frozen V-JEPA 2 video encoder (Figure˜2, right). We train our model on data from the Droid dataset consisting of data from experiments with a table-top Franka Panda robot arm collected through teleoperation. We refer to the resulting action-conditioned model as V-JEPA 2-AC, and in Section˜4 we show that V-JEPA 2-AC can be used within a model-predictive control planning loop to plan actions in new environments.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Action-Conditioned World Model Training", "weight": 1.0} -->

Our goal is to take the V-JEPA 2 model after pre-training and obtain a latent world model that can be used for control of an embodied agentic system via closed-loop model-predictive control. To achieve this, we train V-JEPA 2-AC, an autoregressive model that predicts representations of future video observations conditioned on control actions and proprioceptive observations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Action-Conditioned World Model Training", "weight": 1.0} -->

In this section we describe a concrete instantiation of this framework for a tabletop arm with a fixed exocentric camera, and where control actions correspond to end-effector commands. The model is trained using approximately 62 hours of unlabeled video from the raw Droid dataset, which consists of short videos, typically 3--4 seconds long, of a 7-DoF Franka Emika Panda arm equipped with a two-finger gripper. Here, *unlabeled* video refers to the fact that we do not use additional meta-data indicating any reward, what type of task was being performed in each demonstration, or whether the demonstration was successful or not in completing the task being attempted. Rather, we only use the raw video and end-effector state signals from the dataset (each video in the dataset is accompanied by meta-data indicating the end-effector state in each frame --- three dimensions for position, three for orientation, and one for the gripper state).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Model inputs", "weight": 1.0} -->

In each iteration of training we randomly sample a mini-batch of 4 second video clips from the Droid dataset, and, for simplicity, discard any videos shorter than 4 seconds, leaving us with a smaller subset of the dataset comprising under 62 hours of video. The video clips are sampled with resolution $256\times 256$ and a frame-rate of 4 frames-per-second (fps), yielding 16 frame clips denoted by $(x_{k})_{k\in}$, where each $x_{k}$ represents a single video frame. The robot's end-effector state in each observation is denoted by the sequence $(s_{k})_{k\in}$, where $s_{k}$ is a real-valued 7D vector defined relative to the base of the robot. The first three dimensions of $s_{k}$ encode the cartesian position of the end-effector, the next three dimensions encode its orientation in the form of extrinsic Euler angles, and the last dimension encodes the gripper state.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Model inputs", "weight": 1.0} -->

We construct a sequence of actions $(a_{k})_{k\in}$ by computing the change in end-effector state between adjacent frames. Specifically, each action $a_{k}$ is a real-valued 7-dimensional vector representing the change in end-effector state between frames $k$ and $k+1$. We apply random-resize-crop augmentations to the sampled video clips with the aspect-ratio sampled in the range (0.75, 1.35).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Loss function", "weight": 1.0} -->

We use V-JEPA 2 encoder $E(\cdot)$ as an image encoder and encode each frame independently in a given clip to obtain a sequence of feature maps $(z_{k})_{k\in}$, where $z_{k}\coloneqq E(x_{k})\in\mathbb{R}^{H\times W\times D}$ with $H\times W$ denoting the spatial resolution of the feature map, and $D$ the embedding dimension. In practice, our feature maps are encoded using the ViT-g encoder and have the shape $16\times 16\times 1408$. Note that the encoder is kept frozen during this post-training phase.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Loss function", "weight": 1.0} -->

The sequence of feature maps, end-effector states, and actions are temporally interleaved as $(a_{k},s_{k},z_{k})_{k\in}$ and processed with the transformer predictor network $P_{\phi}(\cdot)$ to obtain a sequence of next state representation predictions $(\hat{z}_{k+1})_{k\in}$. The scalar-valued teacher-forcing loss function is finally computed as with $T=15$. We also compute a two-step rollout loss to improve the model's ability to perform autoregressive rollouts at inference time.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Loss function", "weight": 1.0} -->

For simplicity of exposition and with slight overloading of notation, let $P_{\phi}(\hat{a}_{1:T};s_{k},z_{k})\in\mathbb{R}^{H\times W\times D}$ denote the final predicted state representation obtained by autoregressively running V-JEPA 2-AC with an action sequence $(\hat{a}_{i})_{i\in[T]}$, starting from ($s_{k}$, $z_{k}$). We can now denote the rollout loss as: In practice we use $T=2$ for computing the rollout loss, such that we only differentiate the predictor through one recurrent step.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Loss function", "weight": 1.0} -->

The overall training objective is thus given by and is minimized with respect to the predictor weights $\phi$. For illustrative purposes, the training procedure is depicted in Figure˜6 with $T=4$ for both the teacher forcing and rollout loss.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Architecture", "weight": 1.0} -->

The predictor network $P_{\phi}(\cdot)$ is a $\sim$`<!-- -->`{=html}300M parameter transformer network with 24-layers, 16 heads, 1024 hidden dimension, and GELU activations. The action, end-effector state, and flattened feature maps input to the predictor are processed with separate learnable affine transformations to map them to the hidden dimension of the predictor. Similarly, the outputs of the last attention block of the predictor go through a learnable affine transformation to map them back to the embedding dimension of the encoder. We use our 3D-RoPE implementation to represent the spatiotemporal position of each video patch in the flattened feature map, while only applying the temporal rotary positional embeddings to the action and pose tokens. We use a block-causal attention pattern in the predictor so that each patch feature at a given time step can attend to the action, end-effector state, and other patch features from the same timestep, as well as those from previous time steps.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Energy minimization", "weight": 1.0} -->

Given an image of the goal state, we leverage V-JEPA 2-AC for downstream tasks by planning. Specifically, at each time step, we plan an action sequence for a fixed time horizon by minimizing a goal-conditioned energy function. We then execute the first action, observe the new state, and repeat the process. Let $s_{k}$ denote the current end-effector state, and $x_{k}$ and $x_{g}$ denote the current observed frame and goal image, respectively, which are separately encoded with the video encoder to obtain the feature maps $z_{k}$ and $z_{g}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Energy minimization", "weight": 1.0} -->

Given a planning horizon, $T$, we optimize a sequence of robot actions, $(a^{\star}_{i})_{i\in[T]}$, by minimizing a goal-conditioned energy function, such that $(a^{\star}_{i})_{i\in[T]}\coloneqq\text{argmin}_{\hat{a}_{1:T}}\ \mathcal{E}(\hat{a}_{1:T};\ z_{k},s_{k},z_{g})$. As illustrated in Figure˜7, the model infers an action sequence $(a^{\star}_{i})_{i\in[T]}$ by selecting a trajectory that minimizes the L1 distance between the world model's imagined state representation $T$ steps into the future and its goal representation. In practice, we minimize in each planning step using the Cross-Entropy Method, and only execute the first action on the robot before re-planning, as in receding horizon control.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Planning: Zero-shot Robot Control", "weight": 1.0} -->

In this section we demonstrate how V-JEPA 2-AC can be used to implement basic robot skills like reaching, grasping, and pick-and-place via model-predictive control. We focus on tasks with visual goal specification and show that V-JEPA 2-AC generalizes zero-shot to new environments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare the performance of V-JEPA 2-AC with two baselines, one vision-language-action model trained with behavior cloning, and one video generation-based world model.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Baselines", "weight": 1.0} -->

The first baseline is based on the Octo video-language-action model that allows for goal-image conditioning. We start from the open-source weights of the *octo-base-1.5* version of the model, which is pretrained on the *Open-X Embodiment* dataset containing over 1M trajectories.^11^1In comparison, we train V-JEPA 2-AC on 23k trajectories from Droid, including successes and failures. We fine-tune the Octo model with behaviour cloning on the entire Droid dataset using hindsight relabeling with image goals and end-effector states. In particular, we sample random segments of trajectories from the Droid dataset during training, and uniformly sample goal images up to 20 timesteps forward in the trajectory. We use the official open-source code for fine-tuning, including all standard Droid optimization hyperparameters, and leverage single side image view inputs at $256\times 256$ resolution, a context of two previous frames, and a horizon of 4 future actions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Baselines", "weight": 1.0} -->

The second baseline we compare with is based on the Cosmos video generation model. We start with the open-source weights for the action-free Cosmos model (latent diffusion-7B with continuous tokenizer), which was trained on 20M hours of video, and we fine-tune the model on Droid using the officially-released action-conditioned fine-tuning code.^22^2 To improve performance when training on Droid, we (i) lowered the learning rate to match that used in the video-conditioned Cosmos recipe, (ii) removed the dropout in the video conditioning to improve the training dynamics, and (iii) increased the noise level by a factor of $e^{2}$, as we observed that the model trained with a lower noise factor struggled to leverage the information in the conditioning frame. Although the Cosmos technical report mentions using world models for planning or model-predictive control as a future application, to the best of our knowledge this is the first reported attempt using Cosmos models for robot control.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Robot deployment", "weight": 1.0} -->

All models are deployed zero-shot on Franka Emika Panda arms with RobotiQ grippers, located in two different labs, neither of which appears in the Droid dataset. Visual input is provided through an uncalibrated low-resolution monocular RGB camera. The robots use the same exact model weights and inference code, and similar low-level controllers based on operational space control. We use blocking control for both the V-JEPA 2-AC world model and Cosmos world model (i.e., the system waits for the last commanded action to be completed before sending a new action to the controller) and experiment with both blocking and non-blocking control for Octo, and report the best performance across the two options. When planning with V-JEPA 2-AC and Cosmos, we constrain each sampled action to the L1-Ball of radius $0.075$ centered at the origin, which corresponds to a maximum end-effector displacement of approximately 13 cm for each individual action, since large actions are relatively out-of-distribution for the models.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Robot deployment", "weight": 1.0} -->

Start Frame Goal Frame Start Frame Goal Frame Start Frame Goal Frame Figure 8: Single-Goal Reaching. Single-goal reaching involves moving the end-effector to a desired location in space based on a single goal image. This task measures for a basic understanding of actions as well as a 3D spatial understanding of the scene, including depth, from the monocular RGB camera. In each step, we use V-JEPA 2-AC to plan a sequence of actions by minimizing the L1 distance between the model’s imagined future state representations and its representation of the goal frame. The first action is then executed before re-planning in the next time step. During planning, we only sample individual actions in the L1-Ball of radius 0.075 centered at the origin. Thus, the maximum achievable decrease in cartesian distance to the goal in a single step is 0.13 (∼13 cm).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Single-goal reaching", "weight": 1.0} -->

First, we evaluate on the task of single-goal reaching, which involves moving the end-effector to a desired location in space based on a single goal image. This task measures for a basic understanding of actions as well as a 3D spatial understanding of the scene (including depth) from the monocular RGB camera.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Single-goal reaching", "weight": 1.0} -->

Figure˜8 shows the Euclidean distance between the end-effector and its goal position during robot execution for three different single-goal reaching tasks. In all cases, the model is able to move the end-effector within less than 4 cm of its goal position, and select actions that lead to a monotonic decrease in the error. This can be seen as a form of visual servoing, wherein visual feedback from a camera is used to control a robot's motion. However, unlike classical approaches in visual servoing, V-JEPA 2-AC achieves this by training on unlabeled, real-world video data.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Single-goal reaching", "weight": 1.0} -->

In Figure˜9, we visualize the V-JEPA 2-AC energy landscape from equation for the $\Delta y$ reaching task as a function of a single cartesian-control action, sweeping $\Delta x$ and $\Delta y$ while holding $\Delta z=0$ fixed. The energy function achieves its minimum near the ground-truth action, providing further evidence that the model has learned to reasonably infer the effect of actions without requiring precision sensing. It is also interesting to observe that the energy landscape induced by V-JEPA 2-AC is relatively smooth and locally convex, which should facilitate planning.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Prehensile manipulation", "weight": 1.0} -->

Next, we evaluate all models on more challenging prehensile object manipulation tasks, namely *grasp*, *reach with object*, and *pick-and-place*. Success rates are reported in Table˜2 and Table˜3, and averaged across 10 trials with various permutations to the task across trials (e.g., object location, starting pose, etc.). For the *grasp* and *reach with object* tasks the model is shown a single goal image. For the *pick-and-place* tasks we present two sub-goal images to the model in addition to the final goal. The first goal image shows the object being grasped, the second goal image shows the object in the vicinity of the goal position. The model first optimizes actions with respect to the first sub-goal for 4 time-steps before automatically switching to the second sub-goal for the next 10 time-steps, and finally the third goal for the last 4 time-steps. Examples of robot execution for the pick-and-place task are shown in Figure˜10. Start and goal frames for all individual tasks in Lab 1 are shown in Section˜11.2. The *grasp* task requires precise control from visual feedback to correctly grip the object.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Prehensile manipulation", "weight": 1.0} -->

The *reach with object* task requires the model to navigate while holding an object, which necessitates a basic understanding of intuitive physics to avoid dropping the object. Finally, the *pick-and-place* task tests for the ability to compose these atomic skills.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Prehensile manipulation", "weight": 1.0} -->

While all models achieve a high success-rate on *reach*, differences in performance are more apparent on tasks involving object interaction. We observe that the success-rate for all models depends on the type of object being manipulated. For instance, we find that the cup is mostly easily grasped by placing one finger inside the object and gripping around the rim, however if the control actions produced by the model are not accurate enough, the robot will miss the rim of the cup and fail to grasp the object. When manipulating the box, there are many more feasible grasping configurations, however, the model requires more precise gripper control to ensure that the fingers are open wide enough to grasp the object. We see that, for all models, the variation in success-rate with respect to the object type is due to the combination of sub-optimal actions and the unique challenges associated with manipulating each respective object. Nonetheless, we see that the V-JEPA 2-AC model achieves the highest success-rate across all tasks, highlighting the feasibility of latent planning for robot manipulation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Prehensile manipulation", "weight": 1.0} -->

In Table˜3, we compare planning performance when using V-JEPA 2-AC versus the Cosmos action-conditioned video generation model based on latent diffusion. In both cases we leverage the cross-entropy method for optimizing the sequence of actions using a single NVIDIA RTX 4090 GPU, and construct the energy function by encoding the goal frame in the latent space of the model, as in equation. With 80 samples, 10 refinement steps, and a planning horizon of 1, it takes 4 minutes to compute a single action in each planning step with Cosmos. While we achieve a high success rate of 80% on the *reach* tasks when using Cosmos, performance on object interaction tasks is weaker. Note that under a planning time of 4 minutes per action, a full pick & place trajectory requires over one hour of robot execution. By contrast, with 10$\times$ more samples in each refinement step, the V-JEPA 2-AC world model requires only 16 seconds per action and leads to higher performance across all considered robot skills.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Prehensile manipulation", "weight": 1.0} -->

We can potentially reduce the planning time for both models in future work by leveraging additional computing resources for planning, reducing the number of samples and refinement steps used at each time step, training a feed-froward policy in the world-models' imagination to initialize the planning problem, or potentially leveraging gradient-based planning in the case of V-JEPA 2-AC.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Prehensile manipulation", "weight": 1.0} -->

#Samples

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sensitivity to camera positioning", "weight": 1.0} -->

Since the V-JEPA 2-AC model is trained to predict representations of the next video frame given an end-effector Cartesian control action, without any explicit camera calibration, it must therefore implicitly infer the action coordinate axis from the monocular RGB camera input. However, in many cases, the robot base is not visible in the camera frame, and thus the problem of inferring the action coordinate axis is not well defined, leading to errors in the world model. In practice, we manually tried different camera positions before settling on one that worked well across all of our experiments. We conduct a quantitative analysis of the V-JEPA 2-AC world model's sensitivity to camera position in Section˜11.4.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Long horizon planning", "weight": 1.0} -->

Long horizon planning with world models is limited by a number of factors. First, autoregressive prediction suffers from error accumulation: the accuracy of the representation-space predictions decreases with longer autoregressive rollouts, thereby making it more difficult to reliably plan over long horizons. Second, long-horizon planning increases the size of the search space: the number of possible action trajectories increases exponentially given a linear increase in the planning horizon, thereby making it computationally challenging to plan over long horizons. On the other hand, long-horizon planning is necessary for solving non-greedy prediction tasks, e.g., pick-and-place without image sub-goals. Future work exploring world models for long-horizon planning will enable the solution of many more complex and interesting tasks.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Image goals", "weight": 1.0} -->

Following many previous works in goal-conditioned robot manipulation, our current formulation of the optimization target assumes that we have access to visual goals. However, when deploying robots in-the-wild, it may be more natural to express goals in other forms, such as with language. Future work that aligns latent action-conditioned world models with language models will step towards more general task specification via natural language.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Understanding: Probe-based Classification", "weight": 1.0} -->

The capabilities of a representation-space world model, such as V-JEPA 2-AC discussed above, are inherently limited by the state information encoded in the learned representation space. In this section and subsequent sections, we probe the representations learned by V-JEPA 2 and compare the V-JEPA 2 encoder to other vision encoders on visual classification.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Understanding: Probe-based Classification", "weight": 1.0} -->

Visual classification tasks can focus either on *appearance understanding* or *motion understanding*. While appearance understanding tasks can generally be solved using information visible in a single frame of an input video clip (even when the classification labels describe actions), motion understanding tasks require several frames to correctly classify a video. To ensure a balanced evaluation of both motion and appearance, we have selected three motion understanding tasks, namely Something-Something v2 (SSv2), Diving-48, and Jester, which require the model to understand human gestures and movements. For appearance understanding, we have chosen Kinetics400 (K400), COIN, and ImageNet (IN1K), which involve recognizing actions, scenes, and objects. Empirically, we show that V-JEPA 2 outperforms state-of-the-art visual encoders on motion understanding tasks, while being competitive on appearance understanding tasks.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Attentive Probe", "weight": 1.0} -->

We train an 4-layers attentive probe on top of the frozen encoder output using the training data from each task. Our attentive probe is composed of four transformer blocks, the last of which replaces standard self-attention with a cross-attention layer using a learnable query token. Following standard practice, several clips with a fixed number of frames are sampled from a video during inference. The classification logits are then averaged across clips. We keep the resolution similar to the one used for V-JEPA 2 pretraining. We ablate the number of layers of our attentive probe in Section˜12.2, and also provide full details on the number of clips, clip size, and other hyperparameters used in the downstream tasks.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Attentive Probe", "weight": 1.0} -->

Results Reported in the Literature Image Encoders Evaluated Using the Same Protocol Video Encoders Evaluated Using the Same Protocol Table 4: Action and Object Classification. We report the classification performance of V-JEPA 2 models pretrained on 64 frames at resolution 256 × 256 for all models, except V-JEPA 2 ViT-g384 which was pretrained at resolution 384 × 384, on action and object classification, and compare their performance with state-of-art image and video encoders. All models follow the same evaluation protocol except for V-JEPA 2 ViT-g384. We use 256 × 256 resolution with 16 × 2 × 3 inputs for SSv2 (16 frames clip, 2 temporal crops, 3 spatial crops), 16 × 8 × 3 for K400, 32 × 8 × 3 for COIN and 32 × 4 × 3 for Diving-48 and Jester. V-JEPA 2 ViT-g384 uses a higher resolution of 384 × 384 for all six tasks, and additionally uses 64 × 2 × 3 inputs for SSv2 and 32x8x3 inputs for COIN.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Attentive Probe", "weight": 1.0} -->

Our V-JEPA 2 ViT-g significantly outperforms other vision encoders on motion understanding tasks and is competitive on appearance tasks. It achieves the best average performance of 87.5 across all image and videos encoders. V-JEPA 2 ViT-g384 further improves results consistently across tasks, reaching 88.2 average performance. *: PEcoreG achieves an accuracy 89.8% on ImageNet using an attentive probe and input resoluton of 448px. We use an input resolution of 256px and a different probe architecture in our case.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

We compare the performance of V-JEPA 2 on motion and appearance tasks with several other visual encoders: DINOv2 with registers is the current state-of-the-art model for self-supervised learning with images, while SigLIP2 and the Perception Encoder PE~core~G are two state-of-the-art models for image-text contrastive pretraining. We also consider two video encoders: the self-supervised V-JEPA, and InternVideo2~s2~-1B which relies primarily on vision-text contrastive pretraining.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

We use the same evaluation protocol for every baseline and for V-JEPA 2, learning an attentive probe on top of the frozen encoder, similar to Bardes et al.. We adapt image-based models to video following the procedure used in Oquab et al., concatenating the features of each input frame. For InternVideo2~s2~-1B, we use its image positional embedding for the ImageNet task, and for video tasks we interpolate its positional embedding from 4 frames to 8, producing a token count similar to V-JEPA 2. Despite using a common evaluation protocol, the baseline encoders are trained on different data (e.g., DINOv2 on LVD-142M, PE~core~G on MetaCLIP) and are thus not directly comparable. We can therefore only compare different approaches at a system level; i.e., with a consistent evaluation protocol despite differences in training protocol and data. We also include existing results from the literature using a similar frozen protocol, but with potentially different attentive head architecture.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

In particular, we share reported results of VideoMAEv2, InternVideo-1B and 6B, and VideoPrism on the classification tasks we consider, when available. We provide complete evaluation and hyperparameters in Section˜12.1.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Results", "weight": 1.0} -->

Table˜4 reports the classification performance of V-JEPA 2, the other encoders we evaluated, and other notable results reported in the literature. V-JEPA 2 ViT-g (at 256 resolution) significantly outperforms other vision encoders on motion understanding tasks. It achieves a top-1 accuracy of 75.3 on SSv2 compared to 69.7 for InternVideo and 55.4 for PE~Core~G. V-JEPA 2 is also competitive on appearance tasks, reaching 84.6 on ImageNet (a $+4.6$ point improvement over V-JEPA). Overall, V-JEPA 2 obtains the best average performance across all six tasks, compared to other video and image encoders. The higher-resolution, longer-duration V-JEPA 2 ViT-g~384~ shows further improvement across all tasks, reaching $88.2$ average performance.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Prediction: Probe-based Action Anticipation", "weight": 1.0} -->

Action anticipation consists in predicting the future action given a contextual video clip leading up to some time before the action. Using the Epic-Kitchens-100 (EK100) benchmark, we demonstrate that V-JEPA 2 action anticipation performance increases consistently with model size. Furthermore, despite only using an attentive probe trained on top of V-JEPA 2 representations, we show that V-JEPA 2 significantly outperforms prior state-of-the-art approaches that were specifically designed for this task.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Task", "weight": 1.0} -->

The EK100 dataset is comprised of 100 hours of cooking activities recorded from an egocentric perspective across 45 kitchen environments. Each video in EK100 is annotated with action segments, which include a start timestamp, an end timestamp, and an action label. There are 3,568 unique action labels, each consisting of a verb and a noun category, with a total of 97 verb categories and 300 noun categories. The EK100 action anticipation task involves predicting noun, verb, and action (i.e., predicting verb and noun jointly) from a video clip, referred to as context, that occurs before the start timestamp of an action segment. The interval between the end of the context and the beginning of the action segment is the anticipation time, which is set to 1 second by default. Given that different future actions may be possible from a given context, mean-class recall-at-5 is used as the metric to measure performance.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Anticipation Probe", "weight": 1.0} -->

An attentive probe is trained on top of the frozen V-JEPA 2 encoder and predictor to anticipate future actions. Specifically, we sample a video clip that ends 1 second before an action starts. This video context is fed to the V-JEPA 2 encoder. The predictor takes the encoder representation, along with the mask tokens corresponding to the frame 1 second into the future, and predicts the representation of the future video frame. The outputs of the predictor and encoder are concatenated along the token dimension and fed to an attentive probe with a similar architecture to those used in Section˜5, with the difference being that the anticipation probe's final cross-attention layer learns three query tokens (as opposed to one), and each query output is fed to a different linear classifier to predict the action category, the verb category, and the noun category respectively. A focal loss is applied to each classifier independently and then summed before backpropagating through the shared attention blocks of the probe. We provide additional details and evaluation hyperparameters in Section˜13.1.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare our model with three baselines that are trained specifically for action anticipation: InAViT is a a supervised approach that leverages explicit hand-object interaction modeling, and Video-LLaMA and PlausiVL are both approaches that leverage a large language model, with up to 7 billion parameters.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Results", "weight": 1.0} -->

Table˜5 summarizes the results on the EK100 action anticipation benchmark. We compare V-JEPA 2 ViT-L, ViT-H and ViT-g encoders, increasing parameter count from 300 millions to 1 billion. All three leverage 32 frames with 8 frames per second at resolution $256\times 256$ as video context. We also report results of ViT-g~384~ which uses a resolution of $384\times 384$. V-JEPA 2 demonstrates a linear scaling behavior with respect to model size, in terms of action prediction recall-at-5. V-JEPA 2 ViT-L with $300$ million parameters achieves $32.7$ recall-at-5. Increasing the size of the model to 1 billion parameters leads to a $+5.3$ point improvement with an action recall-at-5 of $38.0$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Results", "weight": 1.0} -->

Furthermore, V-JEPA 2 benefits from using a context with higher resolution, and V-JEPA 2 ViT-g~384~ at resolution $384\times 384$ improves recall-at-5 by an additional $+1.7$ points over the other models using $256\times 256$ resolution.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results", "weight": 1.0} -->

V-JEPA 2 outperforms the previous state-of-the-art model PlausiVL by a significant margin, even with its 300 million parameters compared to the 8 billion parameters used in PlausiVL. In particular, V-JEPA 2 ViT-g~384~ demonstrates a $+12.1$ points improvement over PlausiVL on action recall-at-5, corresponding to a $44\%$ relative improvement.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Results", "weight": 1.0} -->

In Figure˜11 we visualize V-JEPA 2 predictions on three samples from the EK100 validation set, two where the model is successful and one where the model fails. For both successful examples, V-JEPA 2 not only retrieves the correct action correctly with top 1 confidence, but also proposes coherent top 2 to 5 actions, based on the given context. For example, in the top row, the correct action is \"wash sink\", but \"turn on water\" or \"clean wall\" would both have been valid actions given the presence of a tap and a wall. The model also predicts \"rinse sponge\", which is the current action being performed, probably assuming that this action could still be going on after 1 second. For the failure case, V-JEPA 2 still proposes coherent actions such as \"close door\" and \"put down spices package\", but misses the exact nature of the object: \"tea package\".

<!-- chunk {"id": "body-0083", "role": "body", "section": "Limitations", "weight": 1.5} -->

V-JEPA 2 and the EK100 benchmark have several limitations. First, V-JEPA 2 does not fully solve EK100, there are failure cases where the model either gets the verb, the noun, or both wrong. We study the distribution of these failures in Section˜13.2. Second, we focus here on predicting actions with a 1 second anticipation time. The accuracy of V-JEPA 2 degrades when predicting at longer time horizons, see Section˜13.2. Third, the EK100 benchmark is limited to kitchen environments, with a closed well-defined vocabulary, and we do not know how well V-JEPA 2 generalizes to other environments. This limits the utility and applicability of models trained on EK100. Lastly, actions in EK100 are chosen from a fixed set of categories, making it impossible to generalize to action categories not present in the training set.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Understanding: Video Question Answering", "weight": 1.0} -->

In this section, we explore V-JEPA 2's ability to perform open-language video question answering (VidQA). To enable language capabilities, we train a Multimodal Large Language Model (MLLM) using V-JEPA 2 as the visual encoder in the non-tokenized early fusion setup popularized by the LLaVA family of models. In this family of MLLMs, a visual encoder is aligned with a large language model by projecting the output patch embeddings of the vision encoder to the input embedding space of the LLM. The MLLM is then trained either end-to-end, or with a frozen vision encoder. The majority of the encoders used in MLLMs for VidQA are typically image encoders, which are applied independently per-frame for video inputs. Popular instances of such encoders are CLIP, SigLIP, and Perception Encoder, which are chosen primarily due to their semantic alignment with language, obtained by pretraining with image-caption pairs.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Understanding: Video Question Answering", "weight": 1.0} -->

To the best of our knowledge, our work is the first to use a video encoder that is pretrained without any language supervision, to train an MLLM for VidQA.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Understanding: Video Question Answering", "weight": 1.0} -->

MLLM performance on downstream tasks is also highly dependent on the alignment data. In these experiments we use a dataset of 88.5 million image- and video-text pairs, similar to what was used to train PerceptionLM. To demonstrate the effectiveness of the V-JEPA 2 encoder, first we compare V-JEPA 2 with other state-of-the-art vision encoders in a controlled data setup in Section˜7.2, using a subset of 18 million samples. Then, in the same controlled setup, we show that scaling the vision encoder and input resolution size both consistently improve VidQA performance in Section˜7.3. Finally, we scale the alignment data, using the full 88.5 million samples to test the limits of language alignment with V-JEPA 2 in Section˜7.4. Our results demonstrate that in a controlled data setup, V-JEPA 2 obtains competitive performance on open-ended VidQA tasks compared to other vision encoders. Upon scaling the alignment data, V-JEPA 2 achieves state-of-the-art performance on several VidQA benchmarks.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Video Question Answering Tasks", "weight": 1.0} -->

We evaluate on PerceptionTest, which assesses model performance across different skills such as memory, abstraction, physics, and semantics. Additionally, we evaluate on the MVP dataset for physical world understanding, which utilizes a minimal-video pair evaluation framework to mitigate text and appearance biases. We also evaluate on TempCompass, TemporalBench and TOMATO to investigate temporal understanding, and memory capabilities of models. Finally, we report results on general understanding ability using MVBench, which has a bias towards single-frame appearance features, and TVBench, which is proposed in the literature as an alternative for general and temporal understanding, mitigating those biases.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Visual Instruction Tuning", "weight": 1.0} -->

To evaluate the V-JEPA 2 representations on visual-question answering tasks, we align V-JEPA 2 with an LLM using the visual instruction tuning procedure from the LLaVA framework. This process involves converting the visual encoder outputs (or visual tokens) into LLM inputs using a learnable projector module, which is typically an MLP. We train MLLMs through a progressive three-stage process following Liu et al.: Stage 1, where we train the projector solely on image captioning data; Stage 2, where we train the full model on large-scale image question answering, and Stage 3, where we further train the model on large-scale video captioning and question answering. Through this staged training approach, the LLM incrementally improves its understanding of visual tokens. The vision encoder can either be frozen or finetuned along with the rest of the MLLM. We explore both settings as freezing the vision encoder gives a cleaner signal about the quality of the visual features, while finetuning the vision encoder yields better overall performance. Further details of the visual instruction training are described in Section˜14.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Visual Instruction Tuning", "weight": 1.0} -->

Params Enc / LLM Off-the-shelf image encoders Table 6: Comparison between off-the-shelf image encoders and V-JEPA 2 in frozen encoder setting. All experiments use the same LLM backbone (Qwen2-7B-Instruct), data, and training setup with a frozen vision encoder. PerceptionTest accuracy is reported on the validation set post SFT.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Visual Instruction Tuning", "weight": 1.0} -->

Params Enc / LLM Table 7: Scaling Vision Encoder Size and Resolution. We scale the vision encoder from 300 million to 1 billion parameters and input resolution from 256 pixels to 512 pixels. All experiments use the same LLM backbone (Qwen2-7B-Instruct), data, and end-to-end training (unfrozen vision encoder) setup. PerceptionTest accuracy is reported on the validation set post SFT. Increasing V-JEPA 2 encoder scale and resolution improve average performances on VidQA tasks.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Comparing with Image Encoders", "weight": 1.0} -->

To isolate the contribution of vision encoders to MLLM performance and compare with V-JEPA 2, we introduce a controlled setup: we train individual MLLMs with different state-of-the-art encoders using the same LLM backbone and training setup. In this controlled setup, we use Qwen2-7B-Instruct and freeze the vision encoder. We use 18 million image and video-text aligned samples. We first compare V-JEPA 2, pretrained at resolution 512$\times$`<!-- -->`{=html}512 with DINOv2, SigLIP-2, and Perception Encoder.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Comparing with Image Encoders", "weight": 1.0} -->

We observe that V-JEPA 2 exhibits competitive performance in the frozen setup, outperforming DINOv2, SigLIP, and Perception Encoder (PE) in all of the tested benchmarks (Table 6) except PerceptionTest where V-JEPA 2 slightly underperforms SigLIP and PE. The improvement is especially noticeable on MVP, TemporalBench, and TVBench --- benchmarks that are primarily focused on temporal understanding. Additionally, since we only change the vision encoder, we provide evidence that a video encoder trained without language supervision can outperform encoders trained with language supervision, in contrast to conventional wisdom. The results also indicate that using a video encoder instead of an image encoder for VidQA improves spatiotemporal understanding, highlighting the need to develop better video encoders.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Scaling Vision Encoder Size and Input Resolution", "weight": 1.0} -->

Prior work suggests that scaling the vision encoder and input resolution significantly improves VQA performance for self-supervised image encoders. Thus, we scale V-JEPA 2 from 300M to 1B parameters and the input resolution from 256 to 512 pixels, and show the results in Table 7. When increasing vision encoder capacity from 300M to 1B parameters for a fixed input resolution of 256 pixels, we observe improvements of 0.9 points on PerceptionTest, 3.3 points on TVBench, and 1.2 points on MVBench. Additionally, increasing the input resolution to 512 pixels yields further improvements across all downstream tasks, such as an improvement of 2.2 points on PerceptionTest, 4.0 points on TemporalBench, and 3.3 points on TVBench. These results suggest that further scaling the vision encoder and input resolution is a promising direction for improving VidQA performance.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Scaling Vision Encoder Size and Input Resolution", "weight": 1.0} -->

Params Enc / LLM ≤ 8B Video Language Models Results Reported in the Literature V-JEPA 2 ViT-g384 LLama 3.1 8B Table 8: Comparison with state-of-the-art. We use the full 88.5M-sample alignment dataset and train using the same methodology as PLM 8B Cho et al., using a Llama 3.1 backbone. We observe significant improvements in downstream evaluations, obtaining state-of-the-art results in the 8B model class. PerceptionTest accuracy is reported on the test set with SFT for V-JEPA 2; all other results are zero-shot.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Improving the State-of-the-art by Scaling Data", "weight": 1.0} -->

After developing a better understanding of the capabilities of V-JEPA 2 for training an MLLM in the controlled setup, we study the effect of increasing alignment dataset size to improve the state-of-the-art of VidQA. Step changes on downstream task performance are often achieved by increasing the scale of the training data, as observed by Cho et al.. To that end, we increase the scale of MLLM training data from 18 million to the full 88.5 million (4.7$\times$). While increasing the model resolution helps in downstream performance, it comes with the challenge of accommodating a large number of visual tokens in the LLM input. We therefore choose V-JEPA 2 ViT-g~384~, leading to 288 visual tokens per frame. We follow the same recipe as Cho et al. to train V-JEPA 2 ViT-g~384~, using Llama 3.1 as the backbone. To simplify the training process, we use an MLP projector without pooling. Details on the scaling training setup are described in Section˜14.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Improving the State-of-the-art by Scaling Data", "weight": 1.0} -->

Scaling the data uniformly improves the downstream benchmark performance, resulting in state-of-the-art results (Table 8) on multiple benchmarks --- PerceptionTest, MVP, TempCompass, TemporalBench and TOMATO. Compared to the current state-of-the-art PerceptionLM 8B, we observe an increase of 1.3 points on accuracy for PerceptionTest test set, 4.8 points on paired accuracy for MVP, 4.2 points on accuracy for TempCompass, 8.4 points on Multi-binary accuracy for short-QA segment for TemporalBench and 7.1 points on accuracy for TOMATO. V-JEPA 2 does not outperform PerceptionLM on TVBench and MVBench, however it still significantly outperforms other related baselines (InternVL 2.5, Qwen2VL and Qwen2.5VL). These results underscore the need to scale training data for vision-language alignment and provide evidence that an encoder pretrained without language supervision, such as V-JEPA 2, can achieve state-of-the-art results with sufficient scale.

<!-- chunk {"id": "body-0097", "role": "body", "section": "World models and planning", "weight": 1.0} -->

As early as the work of Sutton and Barto and Chatila and Laumond, AI researchers have sought to build agents that use internal models of the world --- modeling both dynamics of the world, as well as mapping the static environment --- to enable efficient planning and control. Previous work has investigated world models in simulated tasks, as well as real-world locomotion and manipulation tasks. World model approaches either learn predictive models directly in pixel-space, in a learned representation space, or utilizing more structured representation spaces such as keypoint representations. Previous approaches that have demonstrated real world performance on robotics tasks have trained task-specific world models, and they rely on interaction data from the environment in which the robot is deployed. Evaluation is focused on demonstrating performance of world modeling approaches within the explored task space, instead of generalization to new environments or unseen objects. In this work we train a task-agnostic world model, and demonstrate generalization to new environments and objects.

<!-- chunk {"id": "body-0098", "role": "body", "section": "World models and planning", "weight": 1.0} -->

Some recent works leverage both internet-scale video and interaction data towards training general purpose (task-agnostic) action-conditioned video generation models for autonomous robots. However, thus far these approaches only demonstrate the ability to generate visually valid-looking plans given actions of the robot, but they have not demonstrated the ability to use those models to actually control the robot.

<!-- chunk {"id": "body-0099", "role": "body", "section": "World models and planning", "weight": 1.0} -->

Other works have explored the integration of generative modeling into policy learning. Differently from this line of work, our goal is to leverage a world model through model-predictive control instead of policy learning to avoid the imitation learning phase that requires expert trajectories. Both approaches are orthogonal and could be combined in future works. Closest to our work, Zhou et al.; Sobal et al. show that you can learn a world model stage-wise or end-to-end and use it to solve planning tasks zero-shot. While those previous works focus on small-scale planning evaluation, we show that similar principles can be scaled and used to solve real-world robotic tasks.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Vision-Language-Action models for Robotic Control", "weight": 1.0} -->

Recent imitation learning approaches in real-world robotic control have made significant progress towards learning policies that show increasingly good generalization capabilities. This is achieved by leveraging video-languange models that have been pre-trained on internet scale video and text data, which are then fine-tuned (or adapted) to also predict actions by using behavior cloning from expert demonstrations. Although these approaches show promising generalization results, it is unclear whether they will be able to learn to predict behaviors that were not demonstrated in the training data since they lack an explicit predictive model of the world and do leverage inference-time computation for planning. They require high-quality large scale teleoperation data, and can only utilize successful trajectories. In contrast, we focus on leveraging any interaction data whether it comes from a successful or failed interaction with the environment.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Vision Foundation Models", "weight": 1.0} -->

Video foundation models in computer vision have shown that large-scale observation datasets comprised of images and/or videos can be leveraged to learn generalist vision encoders that perform well along a wide range of downstream tasks using self-supervised learning approaches from images, videos, with weak language supervision, or a combination thereof. Previous works, however, tend to focus on understanding evaluation using probe-based evaluation or visual question answering tasks after aligning with a large-language model. While such tasks have served to drive progress, it remains an important goal of a visual system to enable an agent to interact with the physical world. Beyond results on visual understanding tasks, we investigate how large-scale self-supervised learning from video can enable solving planning tasks in new environments in a zero-shot manner.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This study demonstrates how joint-embedding predictive architectures, learning in a self-supervised manner from web-scale data and a small amount of robot interaction data, can yield a world model capable of understanding, predicting, and planning in the physical world. V-JEPA 2 achieves state-of-art performances on action classification requiring motion understanding and human action anticipation. V-JEPA 2 also outperforms previous vision encoders on video questions-answering tasks when aligned with a large-language model. Additionally, post-training an action-conditioned world model, V-JEPA 2-AC, using V-JEPA 2's representation, enables successful zero-shot prehensile manipulation tasks, such as Pick-and-Place, with real-world robots. These findings indicate V-JEPA 2 is a step towards developing advanced AI systems that can effectively perceive and act in their environment.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Future work", "weight": 1.5} -->

There are several important avenues for future work to address limitations of V-JEPA 2. First, in this work we have focused on tasks requiring predictions up to roughly 16 seconds into the future. This enables planning for simpler manipulation tasks, like grasp and reach-with-object, from a single goal image. However, to extend this to longer-horizon tasks such as pick-and-place or even more complex tasks, without requiring sub-goals will require further innovations in modeling. Developing approaches for hierarchical models capable of making predictions across multiple spatial and temporal scales, at different levels of abstraction, is a promising direction.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Future work", "weight": 1.5} -->

Second, as mentioned in Section˜4, V-JEPA 2-AC currently relies upon tasks specified as image goals. Although this may be natural for some tasks, there are other situations where language-based goal specification may be preferable. Extending the V-JEPA 2-AC to accept language-based goals, e.g., by having a model that can embed language-based goals into the V-JEPA 2-AC representation space, is another important direction for future work. The results described in Section˜7, aligning V-JEPA 2 with a language model, may serve as a starting point.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Future work", "weight": 1.5} -->

Finally, in this work we scaled V-JEPA 2 models up to a modest 1B parameters. The results in Section˜2 demonstrated consistent performance improvements while scaling to this level. Previous work has investigated scaling vision encoders to as large as 20B parameters. Additional work is needed in this direction to develop scalable pre-training recipes that lead to sustained performance improvements with scale.
