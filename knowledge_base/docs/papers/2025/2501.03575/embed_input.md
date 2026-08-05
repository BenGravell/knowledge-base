<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Cosmos World Foundation Model Platform for Physical AI

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Physical AI needs to be trained digitally first. It needs a digital twin of itself, the policy model, and a digital twin of the world, the world model. In this paper, we present the Cosmos World Foundation Model Platform to help developers build customized world models for their Physical AI setups. We position a world foundation model as a general-purpose world model that can be fine-tuned into customized world models for downstream applications. Our platform covers a video curation pipeline, pre-trained world foundation models, examples of post-training of pre-trained world foundation models, and video tokenizers. To help Physical AI builders solve the most critical problems of our society, we make Cosmos open-source and our models open-weight with permissive licenses available via

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Physical AI is an AI system equipped with sensors and actuators: the sensors allow it to observe the world, and the actuators allow it to interact with and modify the world. It holds the promise of freeing human workers from physical tasks that are dangerous, laborious, or tedious. While several fields of AI have advanced significantly thanks to data and compute scaling in the recent decade, Physical AI only inches forward. This is largely because scaling training data for Physical AI is much more challenging, as the desired data must contain sequences of interleaved observations and actions. These actions perturb the physical world and may cause severe damage to the system and the world. This is especially true when the AI is still in its infancy when exploratory actions are essential. A World Foundation Model (WFM), a digital twin of the physical world that a Physical AI can safely interact, has been a long-sought remedy to the data scaling problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pre-training: Diffusion WFM Pre-training: Autoregressive WFM Post-training: Camera Control Post-training: Robotic Manipulation Post-training: Autonomous Driving Figure 1: Cosmos World Foundation Models. Pre-trained Cosmos WFMs generate high-quality 3D consistent videos with accurate physics. The Cosmos suite of models includes both diffusion and autoregressive transformer models, which are trained using continuous and discrete latent representations of videos, respectively. Post-training these WFMs with specialized datasets enables them to be utilized in a wide range of Physical AI setups. Specifically, we present models with camera controllability, models capable of instruction-following for robotic manipulation, and models for autonomous driving scenarios. To check full videos and more video examples, please visit our website.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce the Cosmos World Foundation Model (WFM) Platform for building Physical AI. We are mainly concerned with the visual world foundation model, where the observations are presented as videos, and the perturbations can exist in various forms. As illustrated in Fig. 2, we present a pre-training-and-then-post-training paradigm, where we divide WFMs into pre-trained and post-trained WFMs. To build a pre-trained WFM, we leverage a large-scale video training dataset to expose the model to a diverse set of visual experiences to become a generalist. To build a post-trained WFM, we fine-tune the pre-trained WFM to arrive at a specialized WFM using a dataset collected from a particular Physical AI environment for the targeted, specialized Physical AI setup. Fig. 1 shows example results from our pre-trained and post-trained WFMs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data determines the ceiling of an AI model. To build a high-ceiling pre-trained WFM, we develop a video data curation pipeline. We use it to locate portions of videos with rich dynamics and high visual quality that facilitate learning of physics encoded in visual content. We use the pipeline to extract about 100M clips of videos ranging from 2 to 60 seconds from a 20M hour-long video collection. For each clip, we use a visual language model (VLM) to provide a video caption per 256 frames. Video processing is computationally intensive. We leverage hardware implementations of the H.264 video encoder and decoder available in modern GPUs for decoding and transcoding. Our video data curation pipeline leverages many pre-trained image/video understanding models. These models have different throughputs. To maximize the overall throughput for generating trainable video data, we build a Ray-based orchestration pipeline. The details are described in Sec. 3.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We explore two scalable approaches for building pre-trained WFMs discussed in Sec. 5. These approaches are transformer-based diffusion models and transformer-based autoregressive models. A diffusion model generates videos by gradually removing noise from a Gaussian noise video. An autoregressive model generates videos piece by piece, conditioned on the past generations following a preset order. Both approaches decompose a difficult video generation problem into easier sub-problems, making it more tractable. We leverage state-of-the-art transformer architectures for their scalability. In Sec. 5.1, we present a transformer-based diffusion model design that exhibits strong world-generation capabilities. In Sec. 5.2, we present a transformer-based autoregressive model design for world generation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both the transformer-based diffusion model and transformer-based autoregressive model use tokens as representations of videos, where the former uses continuous tokens in the form of vectors, and the latter uses discrete tokens in the form of integers. We note that tokenization for videos---a process that transforms videos into a set of tokens---is highly nontrivial. Video contains rich information about the visual world. However, to facilitate learning of the WFMs, we need to compress videos into sequences of compact tokens while maximally preserving the original contents in the videos as the computation complexity of world foundation model training grows with the token counts. In many ways, building a video tokenizer is similar to building a video codec. We develop an attention-based encoder-decoder architecture to learn video tokenization for both continuous and discrete tokens described in Sec. 4.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We fine-tune the pre-trained WFMs to arrive at post-trained WFMs for various Physical AI tasks in Sec. 6. In Sec. 6.1, we fine-tune our pre-trained diffusion WFM to make it camera pose conditional. This post-training creates a navigable virtual world where users can explore the created world by moving the virtual viewpoint around. In Sec. 6.2, we fine-tune our WFMs on various robotic tasks, which consist of video-action sequences. We show that by leveraging the pre-trained WFMs, we can better predict the future state of the world based on the action taken by the robot. In Sec. 6.3, we demonstrate how the pre-trained WFMs can be fine-tuned for various autonomous driving-related tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our intended use of the developed WFMs is for Physical AI builders. To better protect the developers when using the world foundation models, we develop a powerful guardrail system that consists of a pre-Guard to block harmful inputs and a post-Guard to block harmful outputs. The details are described in Sec. 7.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We aim to build a world foundation model platform to help Physical AI builders advance their systems. To achieve this goal, we make our pre-trained world foundation models and tokenizers available under the NVIDIA Open Model License at NVIDIA Cosmos. While this paper makes several improvements in world foundation model design, the world foundation model problem is still far from being solved. Additional research is required to advance the state-of-the-art further.

<!-- chunk {"id": "body-0012", "role": "body", "section": "World Foundation Model Platform", "weight": 1.0} -->

Let $x_{0:t}$ be a sequence of visual observations of the real world from time $0$ to $t$. Let $c_{t}$ be the perturbation to the world. As illustrated in Fig. 3, a WFM is a model $\mathcal{W}$ that predicts the future observation at time $t + 1$, ${\hat{x}}_{t + 1}$, based on the past observation $x_{0:t}$ and the current perturbation $c_{t}$. In our case, $x_{0:t}$ is an RGB video, while $c_{t}$ is a perturbation that can take many forms. It can be an action taken by the Physical AI, a random perturbation, a text description of the perturbation, etc.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Future Cosmos", "weight": 1.0} -->

We believe a WFM is useful to Physical AI builders in many ways, including (but not limited to) Policy evaluation. This refers to evaluating the quality of a policy model in a Physical AI system. Instead of evaluating a trained policy by deploying it to a Physical AI system operating in the real world, one could instead let the digital copy of the Physical AI system interact with the world foundation model. The WFM-based evaluation is more cost-effective and time-efficient. With the WFM, builders can deploy the policy model in unseen environments that are otherwise unavailable. WFMs can help developers rule out incapable policies quickly and focus the physical resources on a few promising ones.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Future Cosmos", "weight": 1.0} -->

Policy initialization. A policy model generates actions to be taken by the Physical AI system based on the current observations and the given task. A well-trained WFM, which models the dynamic patterns of the world based on the input perturbations, can serve as a good initialization of the policy model. This helps address the data scarcity problem in Physical AI.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Future Cosmos", "weight": 1.0} -->

Policy training. A WFM paired with a reward model can be a proxy for the physical world to provide feedback to the policy model in a reinforcement learning setup. The agent can gain proficiency in solving tasks by interacting with the WFM.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Future Cosmos", "weight": 1.0} -->

Planning or model-predictive control. A WFM can be used to simulate different future states following different action sequences taken by a Physical AI system. A cost/reward module can then be used to quantify the performance of these different action sequences based on the outcomes. The Physical AI can then execute the best action sequence based on the simulation results as a whole, as in planning algorithms or in a receding horizon manner, as in model-predictive control. The accuracy of the world model upper-bounds the performance of these decision-making strategies.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Future Cosmos", "weight": 1.0} -->

Synthetic data generation. A WFM can be used to generate synthetic data for training. It can also be fine-tuned to be conditioned on rendering metadata such as depth or semantic maps. One can use the conditional WFM for the Sim2Real use case.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Future Cosmos", "weight": 1.0} -->

While we list the possibilities, this paper does not include empirical results in applying Cosmos WFMs to them. We are eager to verify the claims in future work.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

Fig. 4 visualizes what is available in the Cosmos WFM platform in this paper, including video curator, video tokenization, world foundation model pre-training, world foundation model post-training, and guardrail.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

Video curator. We develop a scalable video data curation pipeline. Each video is split into individual shots without scene changes. A sequence of filtering steps is then applied to the clips to locate high-quality and dynamic information-rich subsets for training. These high-quality shots are then annotated using a VLM. We then perform semantic de-duplication to construct a diverse but compact dataset.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

Video tokenization. We develop a family of video tokenizers of different compression ratios. These tokenizers are causal. The token computation for the current frames is not based on future observation. This causal design has several benefits. On the training side, it makes joint image and video training possible since a causal video tokenizer is also an image tokenizer when the input is a single image. This is important for the video model to leverage image datasets for training, which contain rich appearance information of the worlds and tend to be more diverse. On the application side, causal video tokenizers are better aligned with Physical AI systems that live in the causal world.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

WFM pre-training. We explore two scalable approaches for building pre-trained world foundation models---the diffusion model and the autoregressive model. We use the transformer architecture for its scalability.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

For the diffusion-based WFM, the pre-training consists of two steps: 1) Text2World generation pre-training and 2) Video2World generation pre-training. Specifically, we train the model to generate a video world based on the input text prompt. We then fine-tune it to generate a future video world based on the past video and an input text prompt, which we refer to as the Video2World generation task.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

For the autoregressive-based WFM, the pre-training consists of two steps: 1) vanilla next token generation and 2) text-conditioned Video2World generation. We first train the model to generate a future video world based on the input of past video---foresight generation. We then fine-tune it to generate a future video world based on the past video and a text prompt.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

The video2world generation model is a pre-trained world model that generates the future based on the current observation (the past video) and control input (prompt). For both diffusion-based and autoregressive-based WFMs, we build a family of models with different capacities and study their effectiveness on various downstream applications.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

We further fine-tune our pre-trained diffusion WFM to arrive at a diffusion decoder to enhance the generation results of the autoregressive model. To better control the WFM, we also built a prompt upsampler based on a Large Language Model (LLM).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

World model post-training. We show applications of the pre-trained WFMs on several downstream Physical AI applications. We fine-tune a pre-trained WFM with the camera pose as the input prompt. This allows us to navigate freely in the created world. We also demonstrate how our pre-trained WFMs might be fine-tuned for humanoid and autonomous driving tasks.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Current Cosmos", "weight": 1.0} -->

Guardrail. For safe usage of the developed world foundation models, we develop a guardrail system where harmful inputs and outputs are blocked.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Data Curation", "weight": 1.0} -->

We describe our video curation pipeline, which produces high-quality training datasets for both tokenizers and WFMs. As shown in Fig. 5, our pipeline consists of 5 main steps: 1) splitting, 2) filtering, 3) annotation, 4) deduplication, and 5) sharding. Every step is tailored to improve the data quality and accommodate the requirements of model training. We first present our raw dataset and then describe each step in detail.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dataset", "weight": 1.0} -->

We use both proprietary video datasets and publicly available open-domain Internet videos to train our models. Our goal is to enable Physical AI developers. To this end, we curate the video training dataset to cover various Physical AI applications and target the following video categories: Hand motion and object manipulation (16%), Human motion and activity (10%), Spatial awareness and navigation (16%), First person point-of-view (8%), Dynamic camera movements (8%), Synthetically rendered (4%), and These videos offer a broad coverage of different visual objects and actions. Their diversity improves the generalization of our WFMs and helps the models handle different downstream tasks. The unstructured nature of these videos and their sheer volume creates many challenges to processing them efficiently from both an algorithmic and an infrastructural perspective. The videos can be encoded with a wide variety of codecs and have different aspect ratios, resolutions, lengths, \\etc. Many videos have also been post-processed or edited with different visual effects, which may induce unwanted artifacts in the generated videos and hurt the performance of the world models if not appropriately handled.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dataset", "weight": 1.0} -->

In total, we accumulate about 20M hours of raw videos with resolutions from 720p to 4k. However, a significant amount of the video data is either semantically redundant or does not contain useful information for learning the physics of the world. Hence, we design a sequence of data processing steps to find the most valuable parts of the raw videos for training. We also collect image data as joint-image-and-video training has been shown to improve the visual quality of the generated videos and accelerate the model training. Thanks to the modular design of our data curation pipeline, we can use it to process both image and video data and generate datasets for both pre-training and fine-tuning. We generate about $10^{8}$ video clips for pre-training and about $10^{7}$ for fine-tuning.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Splitting", "weight": 1.0} -->

Our videos have arbitrary lengths, and modern deep-learning models cannot directly consume very long videos. Also, many videos contain shot transitions. They can start from one scene and then transition to a different scene where the two scenes can be disconnected entirely, \\eg, from two people talking in a modern kitchen in New York City to a scene of lions chasing zebra in an African savanna. It is important to segment each video based on its shot changes and generate visually consistent video clips so that the model can learn visual content transitions that are physically plausible instead of artificially edited.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Shot Detection", "weight": 1.0} -->

Splitting aims to temporally segment raw videos of arbitrary lengths into clips without shot changes. It takes the raw videos as input and generates each shot's start and end frame indices. Clips shorter than 2s are discarded, as they could be shot transitions or visual effects. Clips longer than 60s are further split to have a maximal length of 60s. The subsequent filtering steps can then determine whether a clip contains useful information for learning the physics of the world.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Shot Detection", "weight": 1.0} -->

Shot boundary detection is a classical computer vision problem. Existing methods detect shot boundaries based on changes in the visual feature space, but they differ in how to learn visual features from video frames. We evaluate several algorithms for the task in Tab. 1: PySceneDetect, Panda70M, TransNetV2, and AutoShot.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Shot Detection", "weight": 1.0} -->

PySceneDetect is a popular library that detects shot changes by thresholding the temporal change of color histogram in HSV space. Note that it is also adopted by the recent MovieGen work. Panda70M augments PySceneDetect with CLIP-embedding-based stitching and filtering. TransNetV2 and AutoShot, on the other hand, are neural network-based, predicting a probability of each frame being a transition frame given a 100-frame rolling input window.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Shot Detection", "weight": 1.0} -->

It is critical to select an algorithm that can handle heavily edited videos well, as they often have complex shot changes compounded with various visual effects. This motivates us to build a dedicated benchmark to evaluate whether the method can generate clips with clean shot cuts from videos. Our benchmark includes existing datasets, such as RAI, BBC Planet Earth, ClipShots and SHOT. For ClipShots, we define the transition frame as the midpoint of the start and end of each shot annotation to be consistent with other datasets.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Shot Detection", "weight": 1.0} -->

Tab. 1 compares the different methods on ShotBench. We set the confidence threshold to 0.4 for both TransNetV2 and AutoShot. For Panda70M, we follow their implementation for splitting, excluding the filtering steps, for a fair comparison. End-to-end learning-based approaches (\\eg, TransNetV2 and AutoShot) perform much better than methods using hand-crafted features or heuristic rules (\\eg, PySceneDetect and Panda70M). Though TransNetV2 and AutoShot perform comparably on existing datasets, we found TransNetV2 works better on more challenging shot changes. Using an end-to-end neural network (\\ie, TransNetV2) also allows us to increase the throughput of splitting by leveraging modern GPUs for acceleration without the hurdle of hybrid approaches (such as Panda70M) that use complicated logic to combine PySceneDetect and ImageBind embeddings.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Transcoding", "weight": 1.0} -->

Our videos use many different codecs with various settings, which poses challenges to data curation. We re-encode each video clip from shot detection into a consistent, high-quality mp4 format. This simplifies the subsequent data curation process. With a unified video codec, the stability and efficiency of our dataloader for model training are also greatly improved. We use the h264_nvenc codec with a high bitrate and stress test our setting using videos with fast motion and high-frequency texture to ensure no perceptible visual degradation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Transcoding", "weight": 1.0} -->

We thoroughly evaluate different hardware and software configurations for transcoding to maximize the throughput in Tab. 2. Modern GPUs provide hardware-accelerated video encoding and decoding capabilities. NVIDIA L40S has hardware accelerators for both decoding (NVDEC) and encoding (NVENC), whereas NVIDIA H100 only has NVDEC. We compensate H100 with the maximum available CPU cores (28 instead of 1) for a fair comparison with L40S in Tab. 2. L40S has about 17% higher throughput than H100 (0.0674 \\vs0.0574). For software configurations, switching from libx264 to h264_nvenc and transcoding multiple clips from the same video in batches significantly boost the throughput. We observe issues with ffmpeg fully utilizing NVDEC/NVENC accelerators, especially on multi-GPU nodes. Replacing ffmpeg with PyNvideoCodec for video stream transcoding leads to much higher accelerator utilization and the biggest throughput improvement (0.3702 \\vs0.1026).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Transcoding", "weight": 1.0} -->

We only keep ffmpeg for audio remixing and use PyNvideoCodec to better leverage the computing power in the GPUs. We achieve a $\sim 6.5 \times$ increase in throughput when combining all the improvements together.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Filtering", "weight": 1.0} -->

The video clips produced from the splitting step are noisy, with vastly different qualities covering various topics. We design the filtering step to 1) remove video clips whose visual quality fails to meet our minimal requirements, 2) select high-quality video clips suitable for fine-tuning, and 3) tailor the data distribution for building WFMs. We achieve the above goal by doing motion filtering, visual quality filtering, text filtering, and video type filtering.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Motion Filtering", "weight": 1.0} -->

We have two main goals in motion filtering: 1) remove videos that are static or with random abrupt camera motion (usually from hand-held cameras) and 2) tag videos with different types of camera motion (\\eg, pan, zoom, tilt, \\etc), which can provide additional information to guide model training.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Motion Filtering", "weight": 1.0} -->

We build a lightweight classifier for motion filtering. The input to the classifier is a sequence of motion vectors or optical flow extracted from a video clip. The classifier is based on the ViT architecture and is trained with labeled videos. We experiment with motion vectors from h264 codec, the Farneback optical flow algorithm, and an NVIDIA TensorRT-accelerated optical flow estimation network. We find that the classifier built on top of the NVIDIA TensorRT-accelerated optical flow estimation works the best, producing high classification accuracy for motion filtering.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Visual Quality Filtering", "weight": 1.0} -->

We consider two criteria, distortion and appearance quality, for visual quality-based filtering. First, we remove video clips with distortions, such as artifacts, noise, blur, low sharpness, overexposure, underexposure, \\etc. We use a video quality assessment model trained on human-rated videos based on DOVER. This gives a perceptual quality score per clip, and we use the scores to remove clips that are in the bottom $15\%$. Second, we filter out video clips with low appearance quality. We apply an image aesthetic model on sampled frames from an input clip. We set a conservative threshold, \\ie, $3.5$, since aesthetics are less important for Physical AI.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Text Overlay Filtering", "weight": 1.0} -->

Some of our videos are post-processed to add text to include additional information for the viewer. We also find that text tends to co-occur with different visual effects. Our goal is to learn the physics of the world. It is crucial to remove videos with such excessive text. Note that we focus on text added in post-processing instead of text in the original scene from which the video is created, such as the street names in driving videos.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Text Overlay Filtering", "weight": 1.0} -->

We train an MLP-based binary classifier to detect such videos. The input to the classifier is a video embedding extracted using InternVideo2. We use a proprietary VLM to build the training set to label positive and negative videos. Our trained model achieves high prediction accuracy in the validation set.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Video Type Filtering", "weight": 1.0} -->

To adjust the training data distribution and filter out unwanted video types, we design a comprehensive taxonomy that categorizes videos based on their content type and visual style. We train a classifier to label each video clip with categories from the taxonomy. We refine our data by excluding specific video types that could lead to poor generation quality or unrealistic dynamics, such as abstract visual patterns, video game footage, animated content, \\etc. We further adjust the data distribution by upsampling from categories that are more relevant to WFMs (\\eg, human action, human and object interaction, \\etc) and downsampling on categories that are less important (\\eg, nature or landscape videos).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Video Type Filtering", "weight": 1.0} -->

Given the absence of pre-existing labeled datasets matching our taxonomy, we leverage a proprietary VLM to create training and evaluation data for the classifier. For each video clip, we prompt the VLM with eight uniformly sampled frames and query for the most appropriate taxonomy label. Using the annotated data, we train an MLP classifier on the same InternVideo2 embeddings from text filtering.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Annotation", "weight": 1.0} -->

Text descriptions are usually paired with image and video data to provide supervision and conditions for world model training. We use a VLM to generate high-quality and consistent captions for each video clip. We configure the VLM in a way such that it focuses on the material facts and details in the videos. Using this approach to provide descriptions of videos instead of relying on Alt text also eases the burden of learning for world models as we do not need to adapt to different text styles or formats during training.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Annotation", "weight": 1.0} -->

We test several SOTA methods (\\ie, VFC, Qwen2-VL, VILA ) for caption generation on our videos, and find VILA generates more accurate descriptions based on a small-scale human evaluation. We use an internal VILA model with 13B parameters, fine-tuned for video captioning. It has an enlarged context window suitable for processing long, multi-frame contexts, with a max input and output token length of 5904 and 256, respectively. To improve the inference efficiency, we use an FP8-quantized TensorRT-LLM engine, resulting in a 10 $\times$ speed-up in throughput compared to a PyTorch half-precision baseline, as shown in Tab. 3. We prompt VILA with "Elaborate on the visual and narrative elements of the video in detail" and feed it 8 uniformly sampled frames from the input clip. The average length of captions is 559 characters or 97 words.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Deduplication", "weight": 1.0} -->

Given the sheer volume of our videos, there could be duplicated or near-duplicated samples in the training set. It is critical to deduplicate the data to create a more balanced and diverse data distribution. It also improves the efficiency of training and reduces the chance of memorizing specific training samples.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Deduplication", "weight": 1.0} -->

We adopt the approach from SemDeDup and DataComp for scalable semantic deduplication. We reuse the InternVideo2 embeddings computed during filtering and cluster the embeddings using a multi-node GPU-accelerated implementation of k-means with $k = {10,000}$. We compute the pairwise distances within each cluster of embeddings to identify duplicates. When duplicated videos are detected, we choose the video with the highest resolution to ensure no quality is lost due to deduplication. To avoid storing the entire pairwise distance matrix in GPU memory, we calculate on-the-fly the necessary upper-triangular matrix and argmax reduction in blocks of 256. We remove about $30\%$ of training data during deduplication.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Deduplication", "weight": 1.0} -->

We also leverage the extracted InternVideo2 embeddings and clustering results to build a visual search engine that supports querying the whole training dataset with free-form text and videos. The search engine is useful for debugging issues in our data and understanding the gap between the pre-training dataset and downstream applications.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sharding", "weight": 1.0} -->

This step aims to package the processed video clips into webdatasets that our model trainer can directly consume for training. We shard the videos based on their resolution, aspect ratio, and length to align with our training curriculum. Besides pre-training datasets, we also create fine-tuning datasets with even higher quality by leveraging the different filters described above.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Our data processing infrastructure uses AnyScale Ray to implement a streaming pipeline system for geographically distributed clusters, addressing two key challenges in large-scale ML workflows: efficient resource utilization across homogeneous nodes and robust operation over high-latency connections to data sources. By decoupling data transfer from computation, pipelines operate efficiently with remote data storage while maintaining memory requirements that scale with pipeline complexity rather than dataset size, enabling unbounded stream processing.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Our architecture enables concurrent utilization of complementary hardware resources through parallel pipeline stages, for instance, simultaneously using network bandwidth for data ingestion, NVDEC units for video decoding, and GPUs for compute-intensive transformations. We extend the Fragmentation Gradient Descent algorithm to optimize this multi-resource allocation, with our scheduler automatically scaling individual stages to maintain balanced throughput across specialized hardware accelerators.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

Tokenizers are fundamental building blocks of modern large-scale models. They transform raw data into more efficient representations by learning a bottle-necked latent space discovered in an unsupervised manner. Specifically, visual tokenizers map raw and redundant visual data---such as images and videos---into compact semantic tokens, making them crucial for handling high-dimensional visual data. This ability not only enables efficient training of large-scale transformer models but also democratizes their inference on limited computational resources. Fig. 6 schematically illustrates the tokenization training pipeline where the goal is to train the encoder and decoder so that the bottleneck token representation maximally preserves visual information in the input.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

Tokenizers come in two types: continuous and discrete (see Fig. 7 for illustrations). Continuous tokenizers encode visual data into continuous latent embeddings, as in latent diffusion models like Stable Diffusion or VideoLDM. These embeddings are suitable for models that generate data by sampling from continuous distributions. Discrete tokenizers encode visual data into discrete latent codes, mapping them into quantized indices, as seen in autoregressive transformers such as VideoPoet. This discrete representation is necessary for models such as GPT that are trained with the cross-entropy loss. Fig. 7 illustrates the two types of tokens.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

The success of tokenizers largely relies on their ability to deliver high compression rates without compromising their subsequent visual reconstruction quality. On one hand, high compression reduces storage and computational demands. On the other hand, excessive compression can lead to the loss of essential visual details. This trade-off presents a significant challenge in tokenizer design.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

We present Cosmos Tokenizer, a suite of visual tokenizers that includes both continuous and discrete tokenizers for images and videos. Cosmos Tokenizer offers exceptional visual reconstruction quality and inference efficiency. It offers a range of compression rates to accommodate diverse computational constraints and application needs. Tab. 4 presents a comparison of different visual tokenizers and their capabilities.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

We design Cosmos Tokenizer using a lightweight and computationally efficient architecture with a temporally causal mechanism. Specifically, we employ causal temporal convolution layers and causal temporal attention layers to preserve the natural temporal order of video frames, ensuring seamless tokenization of images and videos using a single unified network architecture.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

We train our tokenizers directly on high-resolution images and long-duration videos without limiting the categories or aspect ratios. Unlike existing tokenizers that focus on specific data categories and sizes, the Cosmos Tokenizer operates across various aspect ratios---including 1:1, 3:4, 4:3, 9:16, and 16:9. They are temporally length-agnostic during inference, capable of tokenizing beyond the temporal length on which it was trained.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

We also evaluate our tokenizers on standard image and video benchmarking datasets, including MS-COCO 2017, ImageNet-1K, and DAVIS. To facilitate the video tokenization study for Physical AI applications, we curate a video dataset that covers many video categories for Physical AI, ranging from fish-eye, robotics, driving, human activities, and spatial navigation. The dataset is available at github.com/NVlabs/TokenBench.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Tokenizer", "weight": 1.0} -->

As shown in Fig. 8, our evaluation results demonstrate Cosmos Tokenizer significantly outperforms existing tokenizers by a large margin---for instance, achieving a +4 dB PSNR improvement in reconstruction quality on DAVIS videos. It runs up to $12 \times$ faster and can encode videos up to 8 seconds at 1080p and 10 seconds at 720p in one shot without running out of memory on a single NVIDIA A100 GPU with 80GB memory.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Architecture", "weight": 1.0} -->

Cosmos Tokenizer is designed as an encoder-decoder architecture. Given an input video $x_{0:T} \in {\mathbb{R}}^{{({1 + T})} \times H \times W \times 3}$, with $H$, $W$, $T$ being the height, width, and number of frames, the encoder ($\mathcal{E}$) tokenizes the inputs into a token video $z_{0:T'} \in {\mathbb{R}}^{{({1 + T'})} \times H' \times W' \times C}$, with a spatial compression factor of $s_{HW} = \frac{H}{H'} = \frac{W}{W'}$ and a temporal compression factor of $s_{T} = \frac{T}{T'}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Architecture", "weight": 1.0} -->

The decoder ($\mathcal{D}$) then reconstructs the input video from these tokens, resulting in the reconstructed video ${\hat{x}}_{0:T} \in {\mathbb{R}}^{{({1 + T})} \times H \times W \times 3}$, mathematically given: Our architecture employs a temporally causal design, ensuring that each stage processes only current and past frames, independent of future frames. Unlike common approaches, our tokenizer operates in the wavelet space, where inputs are first processed by a 2-level wavelet transform. Specifically, the wavelet transform maps the input video $x_{0:T}$ in a group-wise manner to downsample the inputs by a factor of four along $x$, $y$, and $t$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Architecture", "weight": 1.0} -->

The groups are formed as: ${\{ x_{0},x_{1:4},x_{5:8},\ldots,x_{{({T - 3})}:T}\}}\rightarrow{\{ g_{0},g_{1},g_{2},\ldots,g_{T/4}\}}$. Subsequent encoder stages process the frames in a temporally causal manner as ${\{ g_{0},g_{0:1},g_{0:2},\ldots\}}\rightarrow{\{\xi_{0},\xi_{1},\xi_{2},\ldots\}}$. Successive encoder stages follow a similar scheme, finally outputting the tokens $z_{0:T'}$. The causal design helps adapt models built on top of the tokenizer to downstream Physical AI applications that often operate on the temporal causal setting.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Architecture", "weight": 1.0} -->

The wavelet transform allows us to operate on a more compact video representation that eliminates redundancies in pixel information, allowing the remaining layers to focus on more semantic compression.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Architecture", "weight": 1.0} -->

Our encoder stages (post wavelet transform) are implemented using a series of residual blocks interleaved with downsampling blocks. In each block, we employ a spatio-temporal factorized 3D convolution, where we first apply a 2D convolution with a kernel size of $1 \times k \times k$ to capture spatial information, followed by a temporal convolution with a kernel size of $k \times 1 \times 1$ to capture temporal dynamics. We use left padding of $k - 1$ to ensure causality. To capture long-range dependencies, we utilize a spatio-temporal factorized causal self-attention with a global support region---for instance, $1 + T'$ for the last encoder block. We use the Swish activation function for non-linearity. We leverage Layer Normalization (LayerNorm) instead of Group Normalization (GroupNorm), which prevents large magnitudes from appearing in specific regions of the latent space or reconstructed outputs. The decoder mirrors the encoder, replacing the downsampling blocks with an upsampling block. Fig. 9 depicts an overview of the overall Cosmos Tokenizer architecture.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Architecture", "weight": 1.0} -->

(a) Temporal Causality: Illustration of the temporal causality mechanism, where inputs x0, x1, …, x12 are processed through grouped intermediate outputs g0, g1, …, and further refined by spatio-temporal convolution and attention operations.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Architecture", "weight": 1.0} -->

(b) Network Architecture: The encoder-decoder network structure includes a 3D Haar wavelet, causal residual, causal downsampling, and causal spatio-temporal attention blocks. The decoder mirrors the encoder’s structure, replacing downsampling with upsampling.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Architecture", "weight": 1.0} -->

We employ the vanilla autoencoder (AE) formulation to model the continuous tokenizer's latent space. For discrete tokenizers, we adopt the Finite-Scalar-Quantization (FSQ) as the latent space quantizer. The latent dimension for the continuous tokenizers is $16$, whereas for the discrete tokenizers, it is $6$, which represents the number of the FSQ levels, which are $$. This configuration corresponds to a vocabulary size of $64,000$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We employ a joint training strategy by alternating mini-batches of images and videos at a preset frequency. We only supervise the final output of our tokenizer's decoder. We do not use auxiliary losses tapped into the latent spaces, such as commitment or KL prior losses. For example, if a VAE formulation were used for continuous tokenizers instead of the vanilla AE, one would need to have the KL prior loss. If a VQ-VAE were used for discrete quantization instead of the FSQ, one would need to have the commitment loss.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We employ a two-stage training scheme. In the first stage, we optimize with the L1 loss that minimizes the pixel-wise RGB difference between the input and reconstructed video (${\hat{x}}_{0:T}$), given by and the perceptual loss based on the VGG-19 features, given, where ${\text{VGG}_{l}{(\cdot)}} \in {\mathbb{R}}^{H \times W \times C}$ is the features from the $l$-th layer of a pre-trained VGG-19 network, $L$ is the number of layers considered, and $\alpha_{l}$ is the weight of the $l$-th layer.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

In the second stage, we use the optical flow (OF) loss to handle the temporal smoothness of reconstructed videos, and the Gram-matrix (GM) loss to enhance the sharpness of reconstructed images, Additionally, we use adversarial loss in the fine-tuning stage to further enhance reconstruction details, particularly at large compression rates.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We train the image tokenizers (denoted as CI and DI) at two compression rates: $8 \times 8$ and $16 \times 16$. Similarly, we train the video tokenizers (denoted as CV and DV) at three compression rates: $4 \times 8 \times 8$, $8 \times 8 \times 8$, and $8 \times 16 \times 16$. Here, the compression rates are expressed as $H \times W$ for images and $T \times H \times W$ for videos, where $T$ represents the temporal dimension, and $H$ and $W$ represent the spatial dimensions.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

For the video tokenizers, we create two variants: Cosmos-0.1-Tokenizer: Trained using mini-batches sampling a smaller number of 720p video frames (49 frames for CV and 17 frames for DV).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cosmos-Tokenize1: Trained using mini-batches sampling a larger number of 360p or 720p video frames (121 frames for CV and 49 frames for DV).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

This approach ensures flexibility in handling varying temporal and spatial resolutions for image and video data. Our experiments indicate that the tokenizers generalize well to resolutions they were trained on and maintain strong quality at higher resolutions.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Results", "weight": 1.0} -->

We extensively evaluate our Cosmos Tokenizer suite on various image and video benchmark datasets. For the evaluation of image tokenizers, we follow prior art to evaluate MS-COCO 2017 and ImageNet-1K. We use the MS-COCO 2017 validation subset of $5,000$ images, and ImageNet-1K validation subset of $50,000$ images as image evaluation benchmark.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results", "weight": 1.0} -->

TokenBench. For video tokenizer evaluation, there is not yet a standard benchmark for high-resolution and long-duration videos. To this end, we introduce a benchmark called *TokenBench* to cover a wide variety of domains, including robotic manipulation, driving, egocentric, and web videos, and standardize the evaluation. We resort to existing video datasets that are commonly used for various tasks, including BDD100K, EgoExo-4D, BridgeData V2, and Panda-70M. We randomly sample $100$ videos from each dataset and preprocess them by taking the first $10$ seconds and resizing the short size to $1080$. For Panda-70M, we manually filter out the videos with low-quality content and small motions. For EgoExo-4D, we randomly pick $100$ scenes and sample one egocentric video and one exocentric video. This results in a total of $500$ videos. Some examples of *TokenBench* can be found in Fig. 10. We release *TokenBench* at the github.com/NVlabs/TokenBench.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Results", "weight": 1.0} -->

In addition to *TokenBench*, we also evaluate our video tokenizers on the DAVIS dataset at $1080$p resolution.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Results", "weight": 1.0} -->

Baselines and evaluation metrics. We evaluate our tokenizers at various compression rates to showcase their effectiveness for different computational needs. We compare each of these tokenizers with state-of-the-art image and video tokenizers. Tab. 4 presents the specific SOTA tokenizers we compared against in various settings. The evaluation metrics include Peak Signal-to-Noise Ratio (PSNR), Structural Similarity (SSIM), reconstruction Fréchet Inception Distance (rFID) for images, and reconstruction Fréchet Video Distance (rFVD) for videos.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Results", "weight": 1.0} -->

Quantitative results. Tabs. 6 and 6 summarize the average quantitative metrics of continuous and discrete video tokenizers on various benchmarks. As shown in both tables, Cosmos Tokenizer achieves state-of-the-art performance in all the metrics compared to prior arts on both the DAVIS video dataset and *TokenBench*, with a spatial-temporal compression ratio of $4 \times 8 \times 8$. Moreover, even with $2 \times$ and $8 \times$ higher compression ratios (\\ie, $8 \times 8 \times 8$ and $8 \times 16 \times 16$), Cosmos Tokenizer still achieves better quality than prior art, showcasing an excellent compression-quality trade-off.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Results", "weight": 1.0} -->

Tabs. 8 and 8 summarize the average quantitative metrics of continuous and discrete image tokenizers on various image benchmarks, covering a wide range of image types. As shown, compared to prior arts, Cosmos Tokenizer consistently achieves state-of-the-art results with a compression ratio of $8 \times 8$. More importantly, at a $4 \times$ larger compression ratio of $16 \times 16$, the image quality of Cosmos Tokenizer is often comparable or even better than prior art at $8 \times 8$ compression ratio, as shown in Tabs. 8 and 8.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Results", "weight": 1.0} -->

These quantitative results on a variety of image and video benchmark datasets confirm that Cosmos Tokenizer is able to better represent visual content with large spatial-temporal compression.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Results", "weight": 1.0} -->

Runtime performance. Tab. 9 shows the number of parameters and the averaged encoding and decoding times per image or per video frame, measured on a single A100 80GB GPU. In comparison, we also list the parameters and the average speeds of prior state-of-the-art tokenizers. As shown, for both image and video tokenizers, Cosmos Tokenizer is $2 \times \sim 12 \times$ faster while maintaining the smallest model size compared to prior arts, showing that Cosmos Tokenizer has high efficiency for encoding and decoding visual content.

<!-- chunk {"id": "body-0088", "role": "body", "section": "World Foundation Model Pre-training", "weight": 1.0} -->

Pre-trained WFMs are generalists that capture general knowledge of real-world physics and natural behaviors. We exploit two different scalable deep learning paradigms, diffusion models and autoregressive models, to build two families of WFMs. Both diffusion models and autoregressive models break a difficult generation problem into a sequence of easier sub-problems and have been turbo-charging the development of generative models. In the case of diffusion models, the difficult generation problem is divided into a sequence of denoising problems. In the case of autoregressive models, the difficult generation problem is divided into a sequence of next-token prediction problems. We discuss how we scale these deep learning paradigms using various parallelization techniques tailored for modern GPUs in our endeavor of building pre-trained WFMs. We train all of the WFM models reported in the paper using a cluster of $10,000$ NVIDIA H100 GPUs in a time span of three months.

<!-- chunk {"id": "body-0089", "role": "body", "section": "World Foundation Model Pre-training", "weight": 1.0} -->

1. Cosmos-Predict1- 7B-Text2World → Cosmos-Predict1- 7B-Video2World 1. Cosmos-Predict1- 4B → Cosmos-Predict1- 5B-Video2World 2. Cosmos-Predict1- 14B-Text2World → Cosmos-Predict1- 14B-Video2World 2. Cosmos-Predict1- 12B → Cosmos-Predict1- 13B-Video2World Cosmos-UpsamplePrompt1-12B-Text2World Cosmos-Predict1-7B-Decoder- DV8×16×16ToCV8×8×8-720p Table 10: Maps of Cosmos World Foundation Model. We have two sets of WFMs. One is based on diffusion models, while the other is based on autoregressive models. For each family, we build two base models and two derivative models. To achieve the best generation quality, we also build a prompt upsampler for the diffusion models and a diffusion decoder for the autoregressive models.

<!-- chunk {"id": "body-0090", "role": "body", "section": "World Foundation Model Pre-training", "weight": 1.0} -->

In Tab. 10, we present a map of our pre-trained WFMs and their companions. For the diffusion-based WFM family, we start by building two Text2World models of 7B and 14B, respectively, which render Cosmos-Predict1-7B-Text2World and Cosmos-Predict1-14B-Text2World. These models can map text prompts to videos of visual worlds. We then fine-tune the Text2World models to take additional video input, representing the current observation. The result is a Video2World model where the future video is predicted based on the current observation (input video) and the perturbation (text prompt). These diffusion models are latent diffusion models that take continuous tokens. We use Cosmos-Tokenize1-CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p to produce the visual tokens. The training text prompts for the WFMs are produced by a VLM through video description generation. These descriptions follow a different distribution of human descriptions of videos.

<!-- chunk {"id": "body-0091", "role": "body", "section": "World Foundation Model Pre-training", "weight": 1.0} -->

To mitigate the domain gap, we build Cosmos-UpsamplePrompt1-12B-Text2World based on the Mistral-NeMo-12B-Instruct model to help convert human text prompts to those preferred by our diffusion-based WFMs.

<!-- chunk {"id": "body-0092", "role": "body", "section": "World Foundation Model Pre-training", "weight": 1.0} -->

For the autoregressive-based WFM family, we first build two base models that are 4B and 12B in size, respectively, to predict future videos purely based on the current video observation. We name them Cosmos-Predict1-4B and Cosmos-Predict1-12B, respectively. These are Llama3-style GPT models trained from scratch for the video prediction task and bear no language understanding. To enable autoregressive-based WFMs to utilize textual information for next token prediction, we incorporate T5 embeddings of the input text prompt into the WFMs through cross-attention layers added to the transformer blocks. These autoregressive WFMs use Cosmos-Tokenize1-DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16-720p, which maps an input video to a few integers. The heavy compression of the tokenizer can sometimes lead to undesired distortions.

<!-- chunk {"id": "body-0093", "role": "body", "section": "World Foundation Model Pre-training", "weight": 1.0} -->

To address the problem, we build a diffusion decoder (Cosmos-Predict1-7B-Decoder-DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16ToCV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p) through fine-tuning the Cosmos-Predict1-7B-Text2World model to map discrete tokens in the DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16 space to continuous tokens in the CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8 space.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Diffusion-based World Foundation Model", "weight": 1.0} -->

Our diffusion-based WFMs are latent diffusion models that operate within a learned latent space of a tokenizer, enabling a compact, reduced-dimensional representation of videos. This design choice offers several advantages: it reduces computational costs during both training and inference while simplifying the denoising task. To tokenize videos into latent representations, we employ Cosmos-Tokenize1-CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Formulation", "weight": 1.0} -->

To train our diffusion WFMs, we adopt the approach outlined in EDM. The denoising score matching loss for the denoiser $D_{\theta}$, evaluated at a noise level $\sigma$, is defined as where $\mathbf{x}_{0} \sim p_{data}$ is a clean image or video sampled from the training set, $\mathbf{n} \sim {\mathcal{N}\left(\mathbf{0},{\sigma^{2}\mathbf{I}} \right)}$ is i.i.d. Gaussian noise, and $D_{\theta}$ is a noise-conditioned neural network tasked with denoising the corrupted sample $\mathbf{x}_{0} + \mathbf{n}$. We adhere to the preconditioning design introduced in EDM for parameterizing $D_{\theta}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Formulation", "weight": 1.0} -->

The overall training loss is defined as a weighted expectation of $\mathcal{L}{(D_{\theta};\sigma)}$ over the noise levels: where the distribution of noise levels $\sigma$ is controlled by hyperparameters $P_{\text{mean}}$ and $P_{\text{std}}$. $\sigma_{\text{data}}$ is the standard deviation of the training data, and the weighting function $\lambda{(\sigma)}$ ensures equal contribution of each noise level at the beginning of the training. However, as training progresses, this balance may deteriorate. To mitigate this issue, we treat the optimization over various noise levels as a form of multi-task learning. We utilize the uncertainty-based weighting approach by introducing $u{(\sigma)}$ as a continuous uncertainty function quantifying the uncertainty for the denoising objective $\mathcal{L}{(D_{\theta},\sigma)}$ at noise level $\sigma$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Formulation", "weight": 1.0} -->

We use a simple MLP to parameterize $u{(\sigma)}$ and minimize the overall loss $\mathcal{L}{(D_{\theta})}$ during training. Intuitively, the contribution of loss at noise level $\sigma$ is weighted down if the model is uncertain about the task, \\ie, if $u{(\sigma)}$ is high. At the same time, the model is penalized for this uncertainty, encouraging $u{(\sigma)}$ to be as low as possible.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Formulation", "weight": 1.0} -->

Compared to recent video generative models that adopt the Gaussian flow matching formulation, our work is derived from the diffusion score matching perspective. However, as shown by Gao et al., these frameworks are theoretically equivalent, sharing fundamental similarities in their objectives and training procedures. Our EDM-based formulation aligns with these insights, mainly differing in the choice of preconditioning designs and hyperparameters. In practice, we have not encountered any performance limitations with the EDM formulation.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Architecture", "weight": 1.0} -->

In this section, we describe the design of our denoiser network $D_{\theta}$ that builds upon DiT, which was originally designed for label-conditioned image generation. We adapt its architecture to better suit our goal of controllable video generation. We visualize the overall network design in Fig. 11.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Architecture", "weight": 1.0} -->

3D patchification. The input to our network is a latent representation of shape $T \times C \times H \times W$ for both image and video data, with images differentiated by a video with a single frame. To prepare inputs for our denoiser network, we first "patchify" the state using a linear layer and subsequently flatten it. This process involves projecting non-overlapping cubes of shape $(p_{t},p_{h},p_{w})$ into individual token inputs for the network. Consequently, after patchification, an image or video is reshaped into a one-dimensional, spatiotemporal sequence of length ${THW}/{({p_{t}p_{h}p_{w}})}$. We use ${p_{t} = 1},{p_{h} = p_{w} = 2}$ for our denoiser network.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Architecture", "weight": 1.0} -->

Hybrid positional embedding with FPS-aware 3D RoPE and learnable embedding. We employ a 3D-factorized Rotary Position Embedding (RoPE) to allow the generation of arbitrary size, aspect ratio, and video length. Specifically, we partition the feature dimension into three approximately equal chunks, each applying RoPE with positional information along the temporal, height, and width axes, respectively. In practice, this can be implemented efficiently without splitting and concatenation in each block by concatenating frequency embeddings in their respective axes and reusing RoPE kernels optimized for Large Language Models (LLMs). To further support video synthesis with varying frame rates, we rescale temporal frequencies based on the training video's Frames Per Second (FPS). Due to RoPE's relative positional encoding property and our 3D factorization design, the FPS-aware design is compatible with our joint image-video training. An additional benefit of RoPE is evident during progressive training when we alter resolution or video length. By leveraging Neural Tangent Kernel (NTK)-RoPE, we observe rapid model convergence, achieving reasonable performance even within $5,000$ training steps.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Architecture", "weight": 1.0} -->

Additionally, we find that adding an extra learnable absolute positional embedding per transformer block can further enhance the model, reduce training loss, and reduce morphing artifacts in generated videos.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Architecture", "weight": 1.0} -->

Cross-attention for text conditioning. We rely on cross-attention layers in our network for incorporating linguistic information. Each transformer block consists of sequential self-attention, cross-attention, and feed-forward layers. While self-attention operates over spatiotemporal tokens, cross-attention integrates semantic context using T5-XXL embeddings as keys and values, enabling effective text conditioning.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Architecture", "weight": 1.0} -->

Query-key normalization. In the early stages of training, we observe instability in the growth of attention logits, leading to a collapse of attention entropy. We follow existing literature to normalize query $Q$ and key $K$ before the attention operation. We use Root Mean Square Normalization (RMSNorm) with learnable scales for all self-attention and cross-attention layers within our network.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Architecture", "weight": 1.0} -->

AdaLN-LoRA. We find that DiT's adaptive layer normalization (AdaLN) layers account for a significant portion of the model parameters while contributing negligibly to the computational complexity in terms of FLOPs. Inspired by W.A.L.T, we implement Low-Rank Adaptation (LoRA) to decompose the dense linear projections in these layers into low-rank approximations. For Cosmos-Predict1-7B, this architectural optimization achieves a 36% reduction in parameter count (from 11B to 7B parameters) while maintaining performance parity across all evaluation metrics, demonstrating the effectiveness of our parameter-efficient design.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Architecture", "weight": 1.0} -->

FFN Hidden Dimension Number of Attention Heads Number of Key / Value Heads Hybrid positional embedding Text; FPS; Frames Text; FPS; Frames Base Learning Rate Learning Rate Warmup Linear scheduler with 2, 500 iterations AdamW momentum and ϵ Table 11: Configuration details of Cosmos-Predict1 models.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

This section outlines the methodologies employed to train our models on datasets spanning multiple modalities, resolutions, aspect ratios, and conditioning inputs.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Joint image and video training. To leverage the vast abundance of high-quality, diverse image datasets in model training, we implement an alternating optimization strategy that interleaves batches of image and video data. To facilitate cross-modal knowledge transfer between image and video domains, we adopt a domain-specific normalization scheme that aligns the latent distributions using sufficient statistics estimated independently for image and video data. This approach is motivated by the observation that reducing the distributional shift between image and video latent representations improves generation quality. Furthermore, we observe non-stationary statistics across temporal and channel dimensions in video latent representations. To address this heterogeneity, we employ a normalization strategy that applies frame-wise and channel-wise standardization to video latent representations, effectively encouraging them to better approximate an isotropic Gaussian prior distribution.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Beyond cross-modality knowledge transfer, our normalization scheme provides an important theoretical benefit: scale invariance in the signal-to-noise ratio during training. Consider two zero-mean latent representations with different scales: one standardized to unit variance, and another with variance 4. When adding Gaussian noise $\mathcal{N}{(0,\sigma^{2})}$ to achieve a desired signal-to-noise ratio for the standardized representation, we must scale the noise to $\mathcal{N}{(0,{4\sigma^{2}})}$ for the unnormalized representation to maintain the same ratio. By standardizing all latent representations, we ensure consistent signal-to-noise ratios across different scales, facilitating model adaptation even when the underlying tokenizer is updated during training.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

To maintain computational efficiency, we balance image and video batch sizes to ensure comparable memory utilization across GPUs. However, we observe that the video batch denoising loss exhibits slower convergence compared to the image batch loss. We attribute this to the inherent temporal redundancy in video frames, which results in smaller gradient magnitudes for video batches. Drawing inspiration from recent advances in multi-resolution image training, we address this convergence discrepancy by scaling the video batch noise levels by the square root of the frame count relative to image batch noise levels. 10, 240 (the context length) is computed as: 640 (width) ÷8 (tokenize) ÷2 (patchify) ×512 (height) ÷8 (tokenize) ÷2 (patchify) ×[(57 − 1) ÷ 8 + 1] (tokenize frames). 56, 320 (the context length) is computed as: 1280 (width) ÷8 (tokenize) ÷2 (patchify) ×704 (height) ÷8 (tokenize) ÷2 (patchify) ×[(121 − 1) ÷ 8 + 1] (tokenize frames).

<!-- chunk {"id": "body-0111", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Progressive training. We adopt a progressive training strategy, with the specifics of each stage detailed in Tab. 12. The initial stage involves training on videos and images at a resolution of 512 pixels, using videos composed of 57 frames. Subsequently, we transition to the target resolution of 720 pixels, increasing the video length to 121 frames. After pre-training on massive data, we fine-tune the model on a high-quality subset for $\mathcal{O}{({10k})}$ iterations with a linearly decaying learning rate. Consistent with findings from Dai et al., we also find that fine-tuning can improve the quality of the generated videos.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Multi-aspect training. To accommodate content with varying aspect ratios, we organize the data into five distinct buckets corresponding to ratios of 1:1, 3:4, 4:3, 9:16, and 16:9, assigning each image or video to the bucket with the closest aspect ratio. During training, each data parallel process group samples from one bucket, allowing different buckets across different parallel process groups. We implement longest-side resizing to maximally preserve the original content information described in the prompt. For batch processing, we apply reflection padding to missing pixels and supply the padding mask to the diffusion backbone, enabling precise control during inference.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Mixed-precision training. We maintain two copies of the model weights: one in and another. During the forward and backward passes, the weights are used to improve training efficiency, resulting in gradients and activations also in format. For parameter updates, the weights are updated in to ensure numerical stability. The updated parameters are then copied and cast to for the next iteration. To further stabilize training, we scale the loss of denoising score matching in Eq. 5 by a factor of 10. We also find that lower betas and eps coefficients in AdamW significantly reduce loss spikes. For our 14B diffusion model training, we rarely encountered loss spikes, and there were no non-recoverable loss spikes.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Text conditioning. For our Text2World models, we employ T5-XXL as the text encoder. We zero-pad T5 embeddings to maintain a fixed sequence length of 512. To enhance text-context alignment, we adopt classifier-free guidance. Unlike prior works that randomly zero out text embeddings, we omit this step due to the effectiveness of negative prompts during inference. Notably, as a text-to-image generator, our model excels in generating high-fidelity images even without guidance, a capability we attribute to the high-quality training dataset. While classifier-free guidance typically promotes mode-seeking behavior for preferred visual content, we find that careful data selection achieves a similar effect. However, for video generation, the lack of comparable high-quality data leads to suboptimal results under low guidance settings. Consequently, higher guidance values are required to produce satisfactory content in video-generation tasks.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Image and video conditioning. We extend our Text2World models to build Video2World models that support image and video conditioning by incorporating previous frame(s) into the generation process. Specifically, the conditional frame(s) are concatenated with the generated frames along the temporal dimension. To improve robustness against variations in input frame(s) during inference, we introduce augmented noise to the conditional frames during training. The sigma value for this augmented noise is sampled with ${P_{\text{mean}} = {- 3.0}},{P_{\text{std}} = 2.0}$. Additionally, the input to the diffusion model is concatenated along the channel dimension with a binary mask that distinguishes conditional frames from generated frames. The loss function excludes contributions from the locations of conditional frames, focusing exclusively on the generated output. To improve generalization, we randomly vary the number of conditional frames during training. During inference, the model can flexibly operate with either a single conditional frame (image) or multiple previous frames as input.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Here, we outline the techniques that enable efficient scaling of our diffusion WFMs. We analyze the memory requirements of our models, discuss parallelism strategies, and compare our training setup against other video diffusion models and state-of-the-art LLMs.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Activations (Tensor Shape) 2 × 3 × seq_len × d_model2 seq_len × batch_size × d_model a 2 × seq_len × batch_size × d_model b 2 × seq_len2 × d_model 2 × seq_len2 × d_model seq_len × batch_size × d_model e 2 × seq_len × d_model2 seq_len × batch_size × d_model 2 × seq_len × d_model2 seq_len × batch_size × d_model seq_len × batch_size × d_model f 2 × seq_len × d_model2 seq_len × batch_size × d_model 4 × seq_len × d_model2 seq_len × batch_size × d_model 4 × seq_len × batch_size × d_model 4 × seq_len × d_model2 seq_len × batch_size × d_model seq_len × batch_size × d_model The shared input is stored. The query Q and key K are stored.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

The normalized query Q and key K are recomputed. The attention scores (A = Q@KT) are recomputed. The value V is stored. The normalized attention weights (A′ = Softmax(A)) are recomputed. In cross-attention, only query Q is counted; key K has much shorter sequence length and is thus negligible. In cross-attention, the value V has much shorter sequence length and is thus negligible. The input is recomputed from GELU. The input is recomputed from LayerNorm.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Memory requirements. The four major components that consume the GPU memory are: Model parameters: 10 bytes per parameter. Our mixed precision training stores model parameters in both and, alongside Exponential Moving Average (EMA) weights.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Gradients: 2 bytes per parameter. We store the gradients.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Optimizer states: 8 bytes per parameter. We use AdamW as our optimizer and store the optimizer states (\\ie, first and second moments).

<!-- chunk {"id": "body-0122", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Activations: $({2 \times \text{number_of_layers} \times 15 \times \text{seq_len} \times \text{batch_size} \times \text{d_model}})$ bytes. We store the activations. Tab. 13 provides details of the stored activations for major operations within the network. To optimize memory usage, we implement selective activation checkpointing, recomputing activations for memory-limited layers such as normalization functions.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

For instance, our 14B model (Cosmos-Predict1-14B-Text2World) requires approximately 280 GB for model parameters, gradients, and optimizer states, alongside 310 GB for activations during high-resolution pre-training. Given the 80GB HBM3 limit of NVIDIA H100 GPUs, we employ Fully Sharded Data Parallelism (FSDP) and Context Parallelism (CP) to distribute memory demands across multiple GPUs.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Fully Sharded Data Parallelism (FSDP). FSDP improves memory efficiency by sharding model parameters, gradients, and optimizer states across devices. It gathers parameters only when needed during computation and releases them afterward. Unlike standard data parallelism, which duplicates parameters across devices, FSDP distributes parameters, gradients, and optimizer states, with each device managing only its shard. This approach minimizes memory usage to the largest temporarily unsharded parameter set alongside its shard of parameters, gradients, and optimizer states. For our implementation, we utilize a sharding factor of 32 for the 7B model and 64 for the 14B model to balance memory and communication latency.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Context Parallelism (CP). Scaling transformers for long-context settings introduces challenges with increased FLOPs and activation memory. CP addresses these challenges by distributing computation and activations across multiple GPUs. It works by splitting both the query $Q$ and the key-value $(K,V)$ along their sequence dimensions into CP_SIZE chunks, where CP_SIZE is the number of GPUs within a CP group. Each GPU processes one chunk of $Q$ and iteratively accumulates partial attention outputs using blocks of $(K,V)$ stored in the same CP group. Different implementations of CP utilize different communication primitives, including all-gather, P2P, and all-to-all. We employ the P2P variant from TransformerEngine, which overlaps computation and communication by transferring $(K,V)$ blocks between GPUs while simultaneously processing attention. When block sizes are carefully chosen, this overlap effectively hides data transfer latency. We organize CP groups within NVLink-connected GPUs and overlap CP ranks with FSDP ranks for optimal utilization. For image iterations with shorter contexts, CP is disabled to improve throughput.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Cross-attention layers do not use CP due to the shorter sequence lengths of $(K,V)$, which results in insufficient computation to mask communication latency.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Using Cosmos-Predict1-14B as an instance, employing FSDP with a sharding factor of 64 reduces memory requirements for parameters, gradients, and optimizer states, bringing them down from 280 GB to approximately ${280/64} \approx {4\text{GB per GPU}}$. Similarly, employing CP with $\text{CP_SIZE} = 8$ decreases activation memory from 310 GB to roughly ${310/8} \approx {40\text{GB per GPU}}$. It is important to note that these calculations are underestimations; in practice, additional memory is consumed by the tokenizer and unsharded parameters. Overlapping communication and computation in CP also necessitates each GPU to retain multiple chunks of $(K,V)$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Comparison with other video generative models. Our parallelism strategy is deliberately streamlined compared to approaches outlined in HunyuanVideo and MovieGen, which incorporate Tensor Parallelism (TP) and its extension, Sequence Parallelism (SP). Despite excluding TP/SP, our setup achieves comparable Model FLOPs Utilization (MFU). While TP/SP remains valuable in certain scenarios, such as larger models or alternative network topologies, a detailed analysis of tradeoffs is left for future work.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Prompt: Hands firmly grasp the handle of a steam iron, expertly gliding it over a wrinkled shirt. With each pass, the iron releases gentle clouds of steam, effortlessly smoothing the fabric and erasing wrinkles to reveal a crisp, neat finish. The iron moves with precision and care, transforming the shirt with each stroke. A subtle scent of fresh linen permeates the air, adding to the serene ambiance. Soft light filters through a nearby window, highlighting the fabric’s newly smooth texture and creating a tranquil atmosphere as this meticulous task unfolds.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Prompt: The video depicts a robotic arm holding a wine glass filled with red wine. The robotic arm, equipped with multiple joints and mechanical components, appears to be designed for precision tasks. The glass is held delicately, showcasing the robot’s capability to handle fragile objects. The background is minimalistic, emphasizing the interaction between the robot and the wine glass.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Prompt: The video depicts the interior of a large industrial facility, likely a factory or warehouse. The space is expansive with high ceilings and metal framework. Overhead cranes and various machinery are visible, indicating a setting for heavy manufacturing or assembly. The floor is mostly empty, with some scattered debris and marked lines. Safety signs and barriers are present, emphasizing the industrial environment. The lighting is natural, streaming through the high windows, illuminating the workspace.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Comparison with large language models. Unlike LLMs, which are typically pre-trained with shorter context lengths, long-context settings significantly increase FLOPs due to the quadratic cost of self-attention. While FLOPs for LLMs are commonly calculated as $6 \times \text{seq_len} \times P$, where $P$ is the number of parameters, we note that this formula is inaccurate for our diffusion WFMs. We provide the forward pass FLOPs of each key operation in Tab. 13.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Prompt Upsampler", "weight": 1.0} -->

During training, our WFMs use detailed video descriptions as input text prompts to produce high-quality videos. However, during inference, user prompts may vary in length, structure, and style, often being much shorter. To bridge this gap between training and inference text prompts, we develop a prompt upsampler to transform original input prompts into more detailed and enriched versions. It can improve the prompts by adding more details and maintaining a consistent description structure, which leads to higher quality output.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Prompt Upsampler", "weight": 1.0} -->

The main requirements for the prompt upsampler are: Fidelity to the input prompts: The upsampled prompt must faithfully preserve the key elements of the original user input, including the main characters, actions or motions, key attributes, and overall intent.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Prompt Upsampler", "weight": 1.0} -->

Alignment with training distribution: The upsampled prompt should closely resemble the distribution of training prompts of WFMs in terms of length, language structure, and style.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Prompt Upsampler", "weight": 1.0} -->

Enhanced visual details: The upsampled prompt should be designed to prompt the WFMs to generate more accurate imagery.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Prompt Upsampler", "weight": 1.0} -->

Prompt upsampler for Text2World model. We fine-tune Mistral-NeMo-12B-Instruct to build our prompt upsampler. To obtain paired data, that is, short prompts simulating user input and the corresponding long prompts reflecting the distribution of training prompts, we use a VLM to generate short captions based on our training long prompts and corresponding videos. This long-to-short data creation strategy is effective in preserving the authentic video content and distribution from detailed training prompts of WFMs and ensuring fidelity between the short and long prompts. The resulting prompt upsampler is termed Cosmos-UpsamplePrompt1-12B-Text2World.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Prompt Upsampler", "weight": 1.0} -->

Prompt upsampler for Video2World model. For the Video2World model, the input consists of video conditions and a user text prompt. To enhance the user prompt, we utilize an open-source VLM, Pixtral-12B, combined with zero-shot prompt engineering, to upsample the prompt into a detailed description that considers both the video conditions and the user prompt. We found the vanilla Pixtral-12B model works well out of the box and did not proceed to perform a similar fine-tuning described above.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Results", "weight": 1.0} -->

In Fig. 12, we present qualitative results generated by our Cosmos-Predict1-7B-Text2World and Cosmos-Predict1-14B-Text2World models. Both models produce videos of high visual quality, motion dynamics, and text alignment. Compared to the 7B model, the 14B model is able to generate videos capturing more complex visual details and intricate motions.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Results", "weight": 1.0} -->

We show generated videos from Video2World 7B and 14B models in Fig. 13. The Video2World models support both image and video conditioning and can generate extended videos in an autoregressive manner. As demonstrated in Fig. 13, our Video2World models produce photorealistic videos with good motion dynamics and visual fidelity. The 14B model, again, generates better videos in terms of scene richness and motion stability.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Autoregressive-based World Foundation Model", "weight": 1.0} -->

In autoregressive WFMs, we formulate world simulation generation as a next-token prediction task similar to language modeling. We start by converting a video into a sequence of discrete video tokens $\mathcal{V} = {\{ v_{1},v_{2},\ldots,v_{n}\}}$ using the Cosmos Discrete Tokenizer introduced in Sec. 4. Then we train a Transformer decoder to predict the next video token using past video tokens as context, similar to large language models (LLMs). Specifically, the training objective is to minimize the following negative log-likelihood (NLL) loss: where the conditional probability $P$ of the predicted next video token $v_{i}$ is modeled by a Transformer decoder with parameters $\Theta$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Architecture", "weight": 1.0} -->

Our autoregressive-based WFM architecture is illustrated in Fig. 14. We make several modifications to the standard transformer model architecture tailored for our video generation task, including adding 1) 3D-aware positional embeddings, 2) cross-attention to enable textual inputs for better control, and 3) QK-Normalization.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Architecture", "weight": 1.0} -->

3D positional embeddings. Similar to our diffusion-based WFM (Sec. 5.1.2), we incorporate two complementary positional embedding mechanisms: 3D factorized Rotary Position Embedding (RoPE) for relative positions and 3D factorized absolute positional embedding (APE) for absolute coordinates. These mechanisms work in concert to provide comprehensive spatial and temporal information throughout the network.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Architecture", "weight": 1.0} -->

3D Rotary Position Embedding (RoPE). We apply 3D RoPE to our model to encode relative positional information across the temporal, height, and width dimensions. During training, we adopt a multi-stage training strategy in which the sequence length of videos increases as the training progresses. To adapt the 3D RoPE to the changing temporal duration, we use YaRN, a compute-efficient technique designed to extend the context window of RoPE. We apply YaRN extension only along the temporal axis as the video sequence length increases only along the temporal dimension. By utilizing YaRN, our model can extrapolate to context lengths longer than those encountered during the initial stages of training.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Architecture", "weight": 1.0} -->

3D Absolute Positional Embedding (APE). In addition to 3D RoPE, we incorporate a 3D APE within each transformer block to complement the relative positional encoding. This APE encodes positional information using sinusoidal embeddings factorized across temporal, height, and width dimensions, ensuring the model is aware of absolute positions. The embedding is added directly to the input tensor at each stage, enriching the positional context for the transformer. We find combining absolute and relative positional encodings enhances model performance, reduces training loss, and minimizes morphing artifacts in generated videos. Notably, while our diffusion-based WFM (Sec. 5.1.2) employs learnable embeddings, we adopt sinusoidal-based embeddings for APE in our autoregressive-based WFM.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Architecture", "weight": 1.0} -->

Vocabulary. Tokenization is a crucial step that turns input text into a sequence of discrete tokens in large language models (LLMs). In LLMs, the vocabulary of possible tokens is determined by the LLM's tokenizer (\\eg, tiktoken introduced by OpenAI ) trained on a large corpus of text with algorithms such as Byte Pair Encoding (BPE).

<!-- chunk {"id": "body-0147", "role": "body", "section": "Architecture", "weight": 1.0} -->

For our autoregressive models, we use our Cosmos-Tokenize1-DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16-720p as the tokenizer. As introduced in Sec. 4, we leverage the Finite-Scalar-Quantization (FSQ) to quantize the $6$-dimensional latent space into $$ levels. This quantization leads to a vocabulary size of ${8 \times 8 \times 8 \times 5 \times 5 \times 5} = {64,000}$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Architecture", "weight": 1.0} -->

Cross-attention for text conditioning. In addition to the self-attention blocks present in the transformer architecture, we add cross-attention layers to enable the model to condition on input text. Similar to diffusion-based WFM(Sec. 5.1.2), cross-attention is applied between the features of the transformer model and text embeddings obtained from a pre-trained text encoder (T5-XXL). In our experiments, we add cross-attention blocks after every self-attention layer.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Architecture", "weight": 1.0} -->

Query-key normalization. In order to enhance training stability, we incorporate Query-Key Normalization (QKNorm). QKNorm addresses instability in attention mechanisms by normalizing the query ($Q$) and key ($K$) vectors before computing their dot product, thereby preventing the softmax function from saturating and ensuring more effective learning. After normalization, the dot product is scaled by a learnable parameter $\gamma$ instead of the fixed $1/\sqrt{d_{k}}$. This learnable scaling factor allows the model to adaptively control the magnitude of the attention scores, enhancing flexibility and expressivity.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Architecture", "weight": 1.0} -->

Z-loss. To further improve training stability, we introduce a stabilization term known as the z-loss into our training objective. The z-loss penalizes deviations of the logits from zero, effectively discouraging the model from generating excessively large logit values that could result in numerical instability or gradient explosions. The z-loss is defined as the sum of the squared logits as $\mathcal{L}_{\text{z-loss}} = {\lambda \cdot {\sum_{i}z_{i}^{2}}}$. We found z-loss to be critical in maintaining gradient norms to a healthy range, especially when scaling the training to a large number of GPU nodes. Empirically, we found that the z-loss coefficient $\lambda = {3 \times 10^{- 4}}$ strikes an optimal balance, effectively stabilizing training without adversely affecting model performance.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

This section describes the techniques that enable efficient scaling of our autoregressive WFMs. We briefly analyze the memory consumption of our models, discuss parallelism strategies, and compare our training setup with other autoregressive models.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Memory requirements. During training, GPU memory is mainly consumed: Model parameters: 6 bytes per parameter. We store the model parameters in both and.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Gradients: 2 bytes per parameter. We store the gradients.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Optimizer states: 8 bytes per parameter. We store the first and second moments of AdamW both.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Activations: Approximately $({2 \times \text{number_of_layers} \times 17 \times \text{seq_len} \times \text{batch_size} \times \text{d_model}})$ bytes. We refer readers to Korthikanti et al. for a detailed analysis of activation memory of state-of-the-art autoregressive models.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

For instance, our 12B model (Cosmos-Predict1-12B) demands approximately 192 GB of memory for its parameters, gradients, and optimizer states combined. As this is beyond a single NVIDIA H100 GPU's 80GB HBM3 capacity, we leverage tensor parallelism (TP) and its extension, sequence parallelism (SP), to distribute the memory requirements and computation across multiple GPUs.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Tensor Parallelism (TP). Tensor Parallelism (TP) splits the weights of linear layers along either the input or output feature dimensions, with the choice guided by the goal of minimizing inter-GPU communication. For example, in a two-layer feedforward network, the weights of the first layer are partitioned along the output feature dimension, while those of the second layer are partitioned along the input feature dimension. This arrangement allows intermediate activations to be processed locally without requiring communication between GPUs. The final outputs are then combined using all-reduce communication. By employing TP, each GPU stores only a fraction, specifically $1/\text{TP_SIZE}$, of the weights for linear layers. However, the default implementation of TP still replicates activations along the sequence dimension for operations like LayerNorm, resulting in redundancy.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Sequence Parallelism (SP). SP extends Tensor Parallelism by further partitioning the context along the sequence dimension. This approach is applicable to operators, such as LayerNorm and Dropout in self-attention layers, where each element in the sequence can be processed independently. With SP enabled. Each GPU stores only a fraction, specifically $1/\text{TP_SIZE}$, of the activations.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Scaling Up", "weight": 1.0} -->

Comparison with other autoregressive models. Compared to popular LLMs, our model doesn't leverage memory-saving attention variants such as MQA or GQA. Otherwise, our autoregressive model is deliberately designed to closely resemble the architecture of LLMs, as this alignment offers flexibility and scalability. Experiments that leverage more parallelisms, such as context parallelism and pipeline parallelism, to further scale up the model sizes and context lengths are left for future works.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We perform pre-training of our autoregressive WFMs in multiple stages.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Stage 1: In the first stage, the model is trained using the video prediction objective. Given the first frame as the input condition, the model is trained to predict future video frames. A context length of 17 frames is used for this task, \\ie, the model predicts 16 future frames with the first frame as input.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Stage 1.1: This stage performs video prediction but with an increased context length of 34 frames. We use the YaRN extension on the temporal dimension to increase the context length of RoPE.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Stage 2: In stage 2 of our training, we introduce text conditioning to our model. Text embeddings are incorporated using newly initialized cross-attention layers. The model is trained with a 34-frame context. To improve text-to-video generation ability, the model is trained using joint image and video data as described in Sec. 5.1.3. When image batches are used, we use a larger batch size as the context length for images is much smaller than that of videos.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

All our models are trained with a fixed spatial resolution of $640 \times 1024$.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cooling down. After pre-training, we conduct a "cooling-down" phase with high-quality data, similar to LLM training practices. During this phase, we linearly decay the learning rate to $0$ while training on high-quality image-video pairs. The cooling-down phase is carried out over $30,000$ iterations.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cross Attention Layers Base Learning Rate Learning Rate Warmup Linear scheduler with 5, 000 iterations FFN Hidden Dimension Number of Attention Heads Number of Key / Value Heads Table 14: Configuration details of Cosmos-Predict1 models.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We train two sets of autoregressive-based WFMs. We start by building two base models: one with a 4B capacity and the other with a 12B capacity. These are pure next-video token predictors that do not take text prompts as input. We then derive a Video2World version from each of the base models, where we add cross-attention layers to them to leverage text prompt inputs for next video token prediction.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cosmos-Predict1-4B: a 4B transformer model for next video token prediction. This model is trained using stage 1 and stage 1.1 of the multi-stage training objective.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cosmos-Predict1-5B-Video2World: a 5B transformer model derived from our Cosmos-Predict1-4B and trained additionally with stage 2 of the multi-stage training objective.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cosmos-Predict1-12B: a 12B transformer model for next video token prediction. This model is trained using stage 1 and stage 1.1 of the multi-stage training objective.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

Cosmos-Predict1-13B-Video2World: a 13B transformer model derived from Cosmos-Predict1-12B and trained additionally with stage 2 of the multi-stage training objective.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Inference Optimization Towards Real-Time Generation", "weight": 1.0} -->

Our Cosmos Autoregressive WFMs share architectural similarities with LLMs, enabling us to leverage established LLM inference optimization techniques to address the sequential decoding bottleneck. We implement a combination of key-value caching, tensor parallelism, and torch.compile, following the gpt-fast^33^3 implementation in PyTorch.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Inference Optimization Towards Real-Time Generation", "weight": 1.0} -->

Speculative decoding. To further accelerate our autoregressive WFMs, we apply the Medusa speculative decoding framework. Unlike common speculative decoding approaches that require a separate draft model or training-free methods with limited speedup, Medusa extends the transformer backbone with extra decoding heads to predict multiple subsequent tokens in parallel. It then verifies these speculated tokens with rejection sampling. The inference is thus accelerated by alleviating the bottleneck of one-token-at-a-time processing. We demonstrate the potential of the Medusa technique in visual autoregressive acceleration without compromising the quality of generated outputs.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Inference Optimization Towards Real-Time Generation", "weight": 1.0} -->

In our implementation, we fine-tune our pre-trained autoregressive WFMs by introducing Medusa heads into the architecture. These heads are strategically inserted after the last transformer hidden states, where all backbone parameters and the final unembedding layer are shared across different heads. Each Medusa head is a single-layer FFN with SiLU activation and residual connection. We further merge the weight matrices of multiple Medusa heads into a unified FFN to maximize parallelism during token prediction. Note that we do not use the tree-based attention mechanism from Cai et al..

<!-- chunk {"id": "body-0175", "role": "body", "section": "Inference Optimization Towards Real-Time Generation", "weight": 1.0} -->

To investigate the optimal Medusa setup for our autoregressive WFMs, we conduct an in-depth study from two aspects: which transformer layers to fine-tune and how many Medusa heads to add. For the first problem, we compare between full fine-tuning and selective layer freezing. We observe that only fine-tuning the Medusa heads gives poor multi-token prediction, while full fine-tuning incurs quality degradation. We empirically identify that unfreezing the last two transformer layers and the final unembedding layer while keeping the backbone frozen yields the best performance. This strategy ensures our Medusa training achieves decent speculative decoding accuracy without suffering from catastrophic forgetting.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Inference Optimization Towards Real-Time Generation", "weight": 1.0} -->

Medusa Head Number Token Throughput (tokens/s)

<!-- chunk {"id": "body-0177", "role": "body", "section": "of Forward Passes", "weight": 1.0} -->

To explore the optimal number of Medusa heads, we calculate the model token throughput and forward pass count with different numbers of Medusa heads. The ablation studies are conducted on 8 $\times$ H100 GPUs and evaluated on 50 unseen test videos of $640 \times 1024$ resolution. The results in Tab. 15 suggest that our Medusa framework can effectively accelerate inference, with up to $2.0 \times$ token throughput and $4.6 \times$ less forward pass for the 4B model, and up to $3.2 \times$ token throughput and $6.1 \times$ less forward pass for the 5B model. We show that though more Medusa heads can reduce the number of forward passes needed to generate, it may slow down the overall token throughput. We find that $9$ Medusa heads yield the best trade-off between computational efficiency and model performance.

<!-- chunk {"id": "body-0178", "role": "body", "section": "of Forward Passes", "weight": 1.0} -->

The table reports the average inference time (in seconds) and VRAM utilization of various Cosmos Autoregressive WFMs under different settings. Inference time is reported for generating 32 frames with a single conditioning frame as input. No DD: Time without diffusion decoder. No DD+Medusa: Time without diffusion decoder but with Medusa heads. With DD: Time with diffusion decoder. With DD+Medusa: Time with diffusion decoder and Medusa heads. VRAM: Video RAM usage in gigabytes.

<!-- chunk {"id": "body-0179", "role": "body", "section": "of Forward Passes", "weight": 1.0} -->

In Tab. 16, we show performance analysis of autoregressive WFMs with Medusa integration. This analysis was conducted on H100 GPUs and evaluated on test videos of $640 \times 1024$ resolution in the precision. Results show that the Medusa implementation consistently accelerates inference for both 4B and 5B models under different GPU configurations.

<!-- chunk {"id": "body-0180", "role": "body", "section": "of Forward Passes", "weight": 1.0} -->

Low-resolution adaptation for real-time inference. We pursue real-time inference by adapting our model to a lower spatial resolution of $320 \times 512$, which results in a lower number of tokens per video. Specifically, we first fine-tune the discrete video tokenizer (Cosmos-Tokenize1-DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16-720p in Sec. 4) on 320p low-resolution videos using videos from the target Physical AI domain. Then, we fine-tune our autoregressive WFM that is pre-trained in $640 \times 1024$ resolution (Cosmos-Predict1-4B in Sec. 5.2.3) with this low-resolution tokenizer on videos of $320 \times 512$ resolution from the target Physical AI domain. Finally, we add the Medusa heads to the fine-tuned low-resolution autoregressive WFM.

<!-- chunk {"id": "body-0181", "role": "body", "section": "of Forward Passes", "weight": 1.0} -->

Token Throughput (tokens/s) Video Throughput (frames/s) Cosmos-Predict1-4B (with Medusa) Table 17: Decoding throughput of Cosmos-Predict1-4B with low-resolution adaptation, benchmarked on 8 × H100 80GB GPUs using 10-FPS videos of 320 × 512 resolution from the Physical AI domain.

<!-- chunk {"id": "body-0182", "role": "body", "section": "of Forward Passes", "weight": 1.0} -->

We conducted inference benchmarking on 8 $\times$ H100 GPUs using torch.compile's "max-autotune" mode in precision, and evaluated with 10-FPS input videos from the target Physical AI domain. In Tab. 17, we report the average token throughput and frame generation speed achieved in this setup. We observe that our model can generate 10 video frames in less than 1 second, demonstrating that we can achieve real-time video generation at 10 FPS.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

Our Cosmos tokenizer uses a lightweight encoder-decoder architecture to perform aggressive compression, which reduces the number of tokens for our WFM training. As a result of aggressive compression, it could sometimes lead to blurriness and visible artifacts in video generation, especially in the autoregressive WFM setting, where only a few integers are used to represent a rich video through discrete tokenization. We resort to the diffusion decoder design to address the limitation. Specifically, we build a more powerful tokenizer decoder by fine-tuning Cosmos-Predict1-7B-Text2Video in Sec. 5.1.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

Fig. 16 illustrates how we train a diffusion decoder for our autoregressive WFMs. For each training video, we use Cosmos-Tokenize1-CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p and Cosmos-Tokenize1-DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16-720p to compute a continuous token video and a corresponding discrete token video, respectively.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

We note that Cosmos-Tokenize1-CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p can produce higher quality video outputs than Cosmos-Tokenize1-DV8$\times$`<!-- -->`{=html}16$\times$`<!-- -->`{=html}16-720p thanks to the more gentle continuous tokenization process and the less aggressive compression scheme ($8 \times 8 \times 8$ instead of $8 \times 16 \times 16$).

<!-- chunk {"id": "body-0186", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

The discrete token video is treated as the conditional input to the denoiser of the Cosmos-Predict1-7B model. To compute the conditional input, we first embed each discrete token of the discrete token video into a 16-dimensional vector based on a learnable vocabulary embedding layer. We then upsample the embedding $2 \times$ along the $x$ and $y$ directions so that the conditional input will be of the same size as the noisy input to the denoiser from the continuous token video. We concatenate the noisy continuous inputs with the conditional inputs along the channel dimension, which becomes the input to the diffusion denoiser. The first layer of the denoiser is channel-dimension expanded to accommodate the new input shape. We fine-tune the updated Cosmos-Predict1-7B by removing the added noise. As the discrete token video is not noise-corrupted, the denoiser learns to leverage the residing information in the conditional input for denoising. The result is a higher-quality decoder for the tokenizer that decodes the discrete token by solving a reserve diffusion problem.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

Fig. 16 illustrates the inference. The output discrete token video (under $8 \times 16 \times 16$ discrete compression) from our autoregressive WFM is decoded into a video through two steps. First, we roll out the conditional denoiser to generate a continuous token video (under $8 \times 8 \times 8$ continuous compression) based on the autoregressive WFM output. Next, the continuous token video is decoded by Cosmos-Tokenize1-CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p to produce the resulting RGB video.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

Prompt: The video of a car moving forward, passing under a large overpass. The road is clear, and there are a few other cars visible in the distance. The weather appears to be sunny, and the time of day is daytime. The scene is set on a busy highway with concrete structures and greenery on the sides.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Diffusion Decoder", "weight": 1.0} -->

Output of Cosmos-Predict1-13B-Video2World Output of Cosmos-Predict1-13B-Video2World + diffusion decoder Figure 18: Diffusion decoder comparison. In the top panel, we show the video generation results with Cosmos-Predict1-13B-Video2World model. In the bottom panel, we show the enhanced video after the output from the autoregressive model is passed through the diffusion decoder. We observe that the autoregressive model alone produces blurry results, while the diffusion decoder can enhance the sharpness of videos while preserving the content.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Results", "weight": 1.0} -->

In Fig. 17, we show qualitative results of our autoregressive WFMs using different model sizes. In the unprompted setting, comparing Cosmos-Predict1-4B and Cosmos-Predict1-12B model, we observe that the 12B model generates videos with better motion and sharper details. Similarly, in the prompted setting, comparing Cosmos-Predict1-5B-Video2World and Cosmos-Predict1-13B-Video2World reveals that the 13B model gets better motion than the 5B model.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Results", "weight": 1.0} -->

In Fig. 18, we show the enhancements obtained when using the diffusion decoder. The outputs of the autoregressive model are blurry mainly due to the lossy compression in our discrete tokenizer. The use of the diffusion decoder can enhance details while preserving the content.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Results", "weight": 1.0} -->

We empirically find the outputs of the autoregressive-based Text2World WFMs do not improve with upsampled prompts from the prompt upsampler discussed in Sec. 5.1.5. We hypothesize this is possibly due to the fact that these WFMs are pretrained with pure video generation tasks for most of the training. They are not forced hard enough to leverage text inputs.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Results", "weight": 1.0} -->

Video Conditioning (9 frames) Cosmos-Predict1-5B-Video2World Cosmos-Predict1-13B-Video2World Table 18: Failure rate analysis of Cosmos Autoregressive models.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Limitations", "weight": 1.5} -->

One notable failure case observed in the generated videos of our autoregressive WFMs is objects unexpectedly appearing from below. Fig. 19 illustrates an example of this issue. To understand the failure rate of our models, we conduct a systematic study by creating an evaluation set of $100$ Physical AI inputs to our autoregressive WFMs. We generate videos with all our models using two input modes---image (single-frame) conditioning and video (9-frame) conditioning. For all generated videos, we manually inspect the failure cases and report the failure rate in Tab. 18. We observe that the smaller models Cosmos-Predict1-4B and Cosmos-Predict1-5B-Video2World show a higher corruption rate in single frame conditioning, while the larger models Cosmos-Predict1-12B and Cosmos-Predict1-13B-Video2World are more robust. Generation with $9$-frame video conditioning is stable for all models, with a failure rate lower than $2\%$.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Pre-trained WFMs are generalists of visual world simulation. Their capabilities should be measured across multiple aspects. Here, we evaluate our models on two aspects. First, we evaluate the 3D consistency of the generated videos. An ideal WFM should generate video simulations from geometrically plausible 3D worlds. Second, we evaluate the physics alignment of the generated videos. We calculate how well the rendered dynamics adhere to the laws of physics. Evaluation of WFMs is a highly nontrivial task. We acknowledge that there are several other important aspects required for evaluation. We leave a more comprehensive evaluation as future work.

<!-- chunk {"id": "body-0196", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

WFMs are designed to simulate 3D worlds through video generation, and it is essential to evaluate how well the generated videos are consistent with the 3D structure of the visual world. In addition to appearing realistic, the generated videos should maintain coherence with the physical principles of scenes through time, a key requirement for downstream Physical AI applications.

<!-- chunk {"id": "body-0197", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

Test data and baseline model. We focus on the scenario of static scenes in order to effectively measure 3D consistency of videos with existing tools based on multi-view geometry. We curate a dataset of 500 videos randomly chosen from the test set of the RealEstate10K dataset. We additionally caption the videos using a proprietary VLM to obtain text prompts that describe the videos as static scenes, so one does not need to consider scene motions for metric computation. We compare against VideoLDM as the baseline method.

<!-- chunk {"id": "body-0198", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

Metrics. Generated videos are effectively 2D projections of the underlying 3D visual worlds. We design the following metrics to measure the 3D consistency of generated videos.

<!-- chunk {"id": "body-0199", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

Geometric consistency. We evaluate the 3D consistency of our generated worlds by quantifying how the epipolar geometry constraints are satisfied, including the Sampson error and the success rate of camera pose estimation algorithms on the generated videos.

<!-- chunk {"id": "body-0200", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

View synthesis consistency. We evaluate the ability of world foundation models to synthesize images at interpolated novel viewpoints while maintaining coherence with the underlying 3D structure.

<!-- chunk {"id": "body-0201", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

The Sampson error is the first-order approximation of the distance from one interest point to its corresponding epipolar line in another view. Given $N$ point correspondences (represented in homogeneous coordinates) ${\{\left({\overline{\mathbf{x}}}_{i},{\overline{\mathbf{y}}}_{i} \right)\}}_{i = 1}^{N}$ in a given frame pair, we define the Sampson error as and $\mathbf{F}$ is the fundamental matrix estimated from the correspondences. We use the square root version of the error function to make the metric more intuitive in pixel units. We use a combination of SuperPoint and LightGlue to detect and match keypoint correspondences from a frame pair and estimate $\mathbf{F}$ using OpenCV's 8-point RANSAC algorithm. We normalize the average error by the diagonal length of the frame with respect to a $960 \times 540$ canvas.

<!-- chunk {"id": "body-0202", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

We also evaluate 3D consistency of a generated video with its ability to self-synthesize novel viewpoints. Following the common practice of novel view synthesis literature, we hold out every 8 frames as the test frames and fit a 3D Gaussian splatting model with the rest of the training frames using the default settings from the Nerfstudio library. We report the Peak Signal-to-Noise Ratio (PSNR), Structural Similarity (SSIM), and LPIPS as the metrics to quantify the quality of the synthesized test views.

<!-- chunk {"id": "body-0203", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

View Synthesis Consistency Cosmos-Predict1-7B-Text2World Cosmos-Predict1-7B-Video2World Cosmos-Predict1-5B-Video2World Real Videos (Reference) Table 19: Evaluation of 3D consistency on base Cosmos models.

<!-- chunk {"id": "body-0204", "role": "body", "section": "3D Consistency", "weight": 1.0} -->

Results. We present the quantitative evaluation results in Tab. 19. The Cosmos WFMs achieve significantly better 3D consistency than our baseline model in terms of both geometric and view synthesis consistency. Not only are the interest points from Cosmos WFMs more 3D-consistent, but the camera pose estimation success rate is also notably higher, reflecting both improved overall quality and enhanced 3D consistency, even reaching the level of real-world videos. Among the cases where camera poses were successfully estimated, the synthesized held-out views demonstrate higher quality across all image synthesis metrics. These results highlight the capability of our Cosmos WFMs to generate 3D-consistent videos, establishing them as effective world simulators.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

An ideal WFM should exhibit a strong understanding of the laws of physics and produce future observations that respect them. While our pre-trained WFMs exhibit a certain level of physics understanding and advance the state-of-the-art, one can still easily generate examples that do not obey the law of physics. We believe additional steps in data curation where physically implausible videos are removed are required, as well as improved model design. While we leave a strong physics-aligned WFM as future work, we are still interested in measuring how much intuitive physics naturally emerges from large-scale data-driven pre-training.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

To explore this, we design acontrolled benchmark dataset using a physics simulation engine, taking inspiration. We generate physics-grounded simulations to test the adherence of our pre-trained WFMs to Newtonian physics and rigid body dynamics. Specifically, we use simulation to generate physically correct photorealistic videos of test scenarios specific to physical laws of interest. These reference "ground truth" videos are then compared with "predicted" videos produced by a WFM given shared context (past observations and perturbation).

<!-- chunk {"id": "body-0207", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Synthetic data generation. Using PhysX and Isaac Sim, we design eight 3D scenarios aimed at evaluating different physical effects: Free-falling object(s): objects dropping on a plane (gravity, collision, \\etc) Tilted planar slope: objects rolling down an incline (gravity, moment of inertia, \\etc) U-shaped slope: objects rolling down a U-shaped slope (potential, kinetic energy, \\etc) Stable stack: a stack of objects in equilibrium (balanced forces) Unstable stack: a stack of objects in imbalance (gravity, collision, \\etc) Dominoes: sequence of rectangular bricks falling in sequence (transfer of momentum, collision, \\etc) Seesaw: objects on either side of a seesaw (torque, rotational inertia, \\etc) Gyroscope: a spinning top on a flat surface (angular momentum, precession, \\etc) For each scenario, we randomize the number and type of dynamic objects (varying sizes, textures, shapes), selecting from Omniverse assets, as well as the background appearance. We simulate the kinematic state of objects over time and render the output videos from 4 different static camera views.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

In total, we render 800 1080p videos of 100 frames in length. The objects in each simulation roll-out are positioned so that they are all visible from the first frame to avoid any existence ambiguity.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Tilted planar slope - An object rolling down an inclined plane U-shaped slope - Two objects rolling down from either ends of a curved slope Unstable stack - An unstable stack of objects falling down due to imbalanced forces Figure 20: Physics-scenario rollouts in simulation \vspre-trained WFM. We demonstrate three exemplar scenarios of increasing complexity as obtained from the reference (physically correct) simulation (first row in each group) and Cosmos-Predict1-7B-Video2World rollouts (second row in each group). We condition the WFM on 9 frames and a prompt focusing on the kinematic state of the simulated objects. We show one tracked object (blue bounding box and mask) per example used to compute our object-level metrics (average IOU).

<!-- chunk {"id": "body-0210", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Metrics. We are interested in assessing the adherence to physical laws by comparing the simulated ground-truth video to the output directly generated by the WFM. Therefore, to produce future observations, we condition our WFMs on the first few frames (either 1 or 9 frames) of the ground truth video. When applicable, we additionally condition a WFM on a text prompt (obtained using a proprietary VLM by captioning the conditioning frames), focusing on the kinematic state of the objects being simulated in the past observations. Please refer to Fig. 20 for some examples of simulated versus predicted scenarios. For evaluation, we use the following metrics: Pixel-level metrics. For a pixel-level comparison, we compute the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM) to compare a predicted frame from the WFM rollout with the reference frame from the ground truth video.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Feature-level metrics. For a slightly higher-level semantic comparison, we calculate DreamSim similarity scores, a feature similarity metric, between the predicted and reference frames.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Object-level metrics. Finally, since we care most about how objects of interest are impacted by the ongoing physical phenomenon, we use tracking to compute object-level metrics that eliminate confounders (background changes, visual quality, \\etc). Since the test conditions are synthetically generated, we have access to the ground-truth instance segmentation masks of the dynamic objects in the scenes. Using SAMURAI, we propagate the ground-truth instance masks in the first frame through the rest of the predicted video frames to extract tracks, allowing us to quantify object-level metrics. We compute the intersection-over-union (IoU) between ground truth and predicted object masks for each frame and object of interest.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

We average these metrics across frames in a video, across videos in the evaluation set, and across four random seeds for rollouts. PSNR and SSIM are computed on all frames, excluding the ones used for conditioning.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Cosmos-Predict1-7B-Video2World Cosmos-Predict1-7B-Video2World Cosmos-Predict1-14B-Video2World Cosmos-Predict1-14B-Video2World Cosmos-Predict1-5B-Video2World Cosmos-Predict1-5B-Video2World Cosmos-Predict1-13B-Video2World Cosmos-Predict1-13B-Video2World Table 20: Physics alignment results. We compare different variants of Cosmos WFMs in terms of accurate future prediction of a physical scenario using the pixel-level, feature-level, and object-level metrics. Metrics are calculated over 33 frames, the maximum length supported by the autoregressive variants of the Cosmos WFMs.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

Results. Quantitative results on physical alignment are outlined in Tab. 20. Based on quantitative and qualitative results, we make the following observations. Unsurprisingly, the models are able to better predict the overall object kinematics with more frames as conditioning input (which allows us to better infer 1st and 2nd order quantities such as speed and acceleration).

<!-- chunk {"id": "body-0216", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

From the table, we also find that our diffusion WFMs perform better in pixel-level prediction than our autoregressive WFMs on the 9-frame conditional setting. This correlates with our visual observation that the diffusion-based WFMs render videos with higher visual quality. We also note that our results do not suggest that the larger model performs better on our physics alignment. While we observe larger models render videos with higher visual quality, all the WFMs equally struggle with physics adherence and require better data curation and model design.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Physics Alignment", "weight": 1.0} -->

More generally, we observe that the rigid-body simulations described above already test the limits of our WFMs, serving as valuable tools for identifying specific failure cases. These range from low-level issues like object impermanence (spontaneous appearance and disappearance of objects) and deformation (shape changes) to more complex problems such as implausible kinematics, violation of gravity, \\etc. We believe such structured simulations offer a useful methodology to test physics alignment. We, therefore, intend to improve them over time by incorporating more complex scenarios, enhancing photorealism to bridge the sim-to-real gap (since WFM pre-training data consists of real videos), and refining our evaluation metrics for a more comprehensive assessment of physical understanding.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Post-trained World Foundation Model", "weight": 1.0} -->

In this section, we demonstrate how our Cosmos WFMs can be fine-tuned to support diverse Physical AI applications. We include examples from post-training our WFM with camera control to achieve 3D navigable visual world generation, post-training our WFM with action control on two different robotic setups for two different robotic manipulation tasks, and post-training our WFM with multi-view support for training autonomous driving agents.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Post-trained World Foundation Model", "weight": 1.0} -->

Cosmos-Predict1-7B-Video2World-Sample-CameraCond Text + Image + Cameras Cosmos-Predict1-7B-Video2World-Sample-Instruction Cosmos-Predict1-7B-Video2World-Sample-Instruction Cosmos-Predict1-7B-Video2World-Sample-ActionCond Cosmos-Predict1-7B-Video2World-Sample-ActionCond Cosmos-Predict1-7B-Text2World-Sample-MultiView Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond Cosmos-Predict1-7B-Video2World-Sample-MultiView Table 21: A map of Post-trained WFMs discussed in Sec. 6.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Post-trained World Foundation Model", "weight": 1.0} -->

Tab. 21 provides a list of the discussed post-trained WFMs in different subsections of this section. We also list the conditional inputs to highlight the operation mode. Note that for each model, we add "-Sample" to emphasize our goal is to provide sample applications of our pre-trained WFMs. Those models are by no means a complete system or a production model for any real-world applications. The developer would need to fine-tune the WFMs on their custom datasets for their Physical AI setups for their target applications.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Post-training WFM for Camera Control", "weight": 1.0} -->

Through camera pose conditioning, we integrate camera control into Cosmos-Predict1-7B-Video2World, making it an effective 3D world simulator. We term the result post-trained WFM as Cosmos-Predict1-7B-Video2World-Sample-CameraCond. We focus on generating 3D worlds from a single reference input image, leveraging camera control to produce temporally coherent and 3D-consistent video simulations from the specified camera trajectories, where changes in perspective align with the underlying 3D structure of the scene.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Dataset", "weight": 1.0} -->

We use DL3DV-10K, a large-scale video dataset of static scenes, for this task. As a preprocessing step, we chunk all videos into clips with 256 frames. To obtain camera pose annotations densely for all frames within a clip, we run structure-from-motion on the chunked clips using GLOMAP. We set the camera pose of the first frame to be the identity transform and compute the relative camera poses for all subsequent frames. We also use a proprietary VLM to caption the videos to obtain text prompts that describe the videos as static scenes.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

We add camera control conditioning by concatenating the sampled latent embeddings with Plücker embeddings, which has the same spatial dimensions as the latent embeddings. Specifically, given the camera pose, we compute the Plücker coordinates via where $\mathbf{c}$ is the camera center location and $\mathbf{d}$ is the unit ray direction of each latent pixel (where the latent embedding is treated as a downsampled image). All the camera poses are relative with respect to the initial frame. The Cosmos-Tokenize1-CV8$\times$`<!-- -->`{=html}8$\times$`<!-- -->`{=html}8-720p used by Cosmos-Predict1-7B-Video2World models has a temporal compression rate of $8 \times$, and thus for every 8 frames, we use the Plücker embedding at the 4th frame to concatenate with the corresponding latent representation.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

We resized the input frames of our training videos to $704 \times 1252$ and padded them to $704 \times 1280$ with reflection. We sample 57 frames during training. The training objective and other hyper-parameters are the same as the base Diffusion WFM training (Sec. 5.1.3).

<!-- chunk {"id": "body-0225", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We assume a single reference image of the world is given and generate the future rollout as a video from the input image. We compare against CamCo, the state-of-the-art model for camera-controllable video generation under this setup. For a fair comparison, we use the CamCo model that was also fine-tuned on the DL3DV-10K training set. As our post-trained WFM generates 57 frames and CamCo can only generate 14 frames, we compare the same 57-frame trajectories where we temporally downsample by $4 \times$ for CamCo. The video resolution from CamCo is limited to $256 \times 256$. We additionally maximally center-crop the input image and test frames for evaluation.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Evaluation", "weight": 1.0} -->

For the test data, we use the same 500 samples from the RealEstate10K test set previously described in Sec. 5.3.1. We use the initial frame as the reference image and camera trajectories provided by the dataset as the camera control input, which we additionally rescale such that the distance between two ends of trajectories is normalized to 1.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Metrics. Following Xu et al., we evaluate the camera controllability of the post-trained world model in two aspects: video generation quality and 3D consistency. For video quality, we use the Fréchet Inception Distance (FID) and the Fréchet Video Distance (FVD) to assess the qualities at the frame and video levels, respectively. We use the same test data as the reference videos to compute the metrics (note that they are not used for pixel-level comparisons).

<!-- chunk {"id": "body-0228", "role": "body", "section": "Evaluation", "weight": 1.0} -->

For 3D consistency, we evaluate via the ability of structure-from-motion libraries to re-estimate the camera poses, and we compare the results against the input camera control trajectories. Given $N$ frames in the video, we quantify the camera trajectory error into two terms: the average rotation error $\epsilon_{\text{rot}}$ and translation error $\epsilon_{\text{trans}}$, defined respectively as where $\mathbf{R}_{i}$ and $\mathbf{t}_{i}$ are the input rotation and translation of the $i$-th frame (serving as ground truth), and ${\hat{\mathbf{R}}}_{i}$ and ${\hat{\mathbf{t}}}_{i}$ are the re-estimated quantities. To account for ambiguities from camera pose estimation results up to a similarity transformation, we follow Lin et al. and run Procrustes analysis on the predicted camera trajectories to align against the ground truth.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Camera Trajectory Alignment Video Generation Quality Cosmos-Predict1-7B-Video2World- Table 22: Quantitative comparison of post-trained WFM with camera control.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Comparisons. We present the results in Tab. 22. First, our post-trained WFM can generate realistic and coherent 3D worlds. This is evidenced by the lower FID/FVD scores (higher visual quality) and the higher camera pose estimation success rate. Cosmos-Predict1-7B-Video2World-Sample-CameraCond demonstrates better camera control, as the camera trajectory re-estimation is significantly closer to the original control input.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We also provide visual comparisons in Fig. 21. While CamCo struggles to generate content beyond the input image, Cosmos-Predict1-7B-Video2World-Sample-CameraCond effectively generates visuals that adhere to the structure of a 3D world. Note that both models were post-trained on DL3DV-10K and evaluated on the RealEstate10K dataset, which introduces a significant distribution shift between training and testing. The Cosmos model successfully overcomes this distribution shift while also demonstrating its capability to generalize to unseen input camera trajectories.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Generated video frames Generated video frames Generated video frames Figure 22: Cosmos-Predict1-7B-Video2World-Sample-CameraCond results with joystick control. For each input frame (left-most column), we apply 4 different camera trajectories created with joystick-like control: moving forward, moving backward, rotating left, and rotating right. We visualize frames 14, 28, 42, and 57 from the generated videos.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Generated frames with various seeds (moving backward) Generated frames with various seeds (rotating right) Generated frames with various seeds (moving backward) Generated frames with various seeds (rotating right) Generated frames with various seeds (moving backward) Generated frames with various seeds (rotating right) Figure 23: Cosmos-Predict1-7B-Video2World-Sample-CameraCond results with different seeds. We show the capability of simulating diverse futures with our camera control model given the same input image and camera condition. For each group, we apply the same input frame and camera condition created with joystick. The first group shows moving backward and second group shows rotating right. Within each group, we show the generated videos with 3 different random seeds in each column. We visualize frames 19, 38, and 57 from the generated videos.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Qualitative results. Fig. 22 shows our results from joystick-like control input on the camera, including *moving forward*, *moving backward*, *rotating left*, and *rotating right*. This demonstrates the use case where one can navigate the simulated world using a joystick to control the model in generating future video frames. A Physical AI agent could also use such control to predict the future of the world under different scenarios.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Evaluation", "weight": 1.0} -->

To show the diversity of the generation, we show generation results from the same input image and camera control with different random seeds in Fig. 23. Cosmos-Predict1-7B-Video2World-Sample-CameraCond is able to generate different worlds while still maintaining 3D spatial and temporal coherence in the videos. This could be used to simulate different possible futures given the current states.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Post-training WFM for Robotic Manipulation", "weight": 1.0} -->

A world model has the potential to serve as a powerful planner and simulator for robotic manipulation. Here, we demonstrate how we fine-tune our pre-trained WFMs for two tasks: instruction-based video prediction and action-based next-frame generation. For instruction-based video prediction, the input is the current video frame of a robot as well as a text instruction, and the output is a predicted video of the robot following the instruction. For action-based next-frame prediction, the input is the current video frame of a robot as well as an action vector between the current and next frame, and the output is the predicted next frame showing the result of the robot performing the specified action. Given a sequence of actions, the model can be run autoregressively to predict a video of the robot executing the given actions.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Datasets", "weight": 1.0} -->

We curate two datasets for the two tasks described above. For instruction-based video prediction, we created an internal dataset called the Cosmos-1X dataset. It comprises approximately 200 hours of egocentric videos captured by EVE, a humanoid robot from 1x.Tech performing a variety of tasks, including navigation, folding clothes, cleaning tables, picking up objects, \\etc. From the raw videos, we selected approximately $12,000$ episodes ranging from 1 to 9 seconds. Each episode is labeled with a one-sentence instruction, which is later upsampled with a proprietary VLM. The videos are captured at 30 FPS with a resolution of $512 \times 512$.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Datasets", "weight": 1.0} -->

For action-based next-frame generation, we used a public dataset called Bridge, with the same configuration as a prior work for comparison. The Bridge dataset includes approximately $20,000$ episodes of third-person views of a robot arm performing different tasks in a kitchen environment, with videos of $320 \times 256$ resolution captured at 5 FPS. For each video frame, the corresponding action is defined as a 7-dimensional vector in the gripper coordinate space $({\Delta x},{\Delta y},{\Delta z},{\Delta\theta_{r}},{\Delta\theta_{p}},{\Delta\theta_{y}},{\Delta\text{Gripper}})$ as in OpenVLA.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

We fine-tune both our Cosmos-Predict1-7B-Video2World (Sec. 5.1) and Cosmos-Predict1-5B-Video2World (Sec. 5.2) for instruction-based video prediction and action-based next-frame prediction tasks.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

For instruction-based video prediction, we build two models based on the base WFMs. The first is called Cosmos-Predict1-7B-Video2World-Sample-Instruction, and the second is called Cosmos-Predict1-5B-Video2World-Sample-Instruction. We compute the T5 embedding of the instruction, which is added to the finetuing of the base model via cross-attention.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

For action-based next-frame prediction, we also build two models based on the base WFMs. The first one is called Cosmos-Predict1-7B-Video2World-Sample-ActionCond, and the second one is called Cosmos-Predict1-5B-Video2World-Sample-ActionCond.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

Since action is a new modality not encountered during pre-training, we introduce additional modules inside our models for conditioning. For Cosmos-Predict1-5B-Video2World-Sample-ActionCond, we add an action embedder MLP to project the action vector into a tensor, which is then incorporated into the model via cross-attention. For Cosmos-Predict1-7B-Video2World-Sample-ActionCond, we also add an action embedder MLP to predict the action into a tensor but instead, incorporate it into the model by adding it to the timestamp embedding of the DiT modules.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Prompt: Organize books by placing them vertically on a shelf.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Prompt: Grip and elevate a green object from a box on a tidy worktable.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Prompt: Fold a green fabric item on a table.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Prompt: Retrieve a box from a storage shelf using its articulated hands in a warehouse setting.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Cosmos-Predict1-7B-Video2World-Sample-Instruction Cosmos-Predict1-5B-Video2World-Sample-Instruction Figure 25: Instruction-based video prediction samples on the Cosmos-1X dataset. The left are the results of Cosmos-Predict1-7B-Video2World-Sample-Instruction model, and the right are the results of Cosmos-Predict1-5B-Video2World-Sample-Instruction model.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Cosmos-Predict1-7B-Video2World-Sample-ActionCond Cosmos-Predict1-5B-Video2World-Sample-ActionCond Figure 26: Action-based next-frame prediction samples on the Bridge dataset. The left is the results of the Cosmos-Predict1-7B-Video2World-Sample-ActionCond model, and the right is the results of the Cosmos-Predict1-5B-Video2World-Sample-ActionCond model. As shown, the predicted video frames closely match the GT video frames for both models.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Evaluation", "weight": 1.0} -->

For instruction-based video prediction, we fine-tune VideoLDM on the Cosmos-1X dataset and obtained VideoLDM-Instruction as a baseline for comparison. To evaluate the video generation performance of the models, we define the following dimensions: Instruction following: Is the generated video aligned with the input language instruction?

<!-- chunk {"id": "body-0250", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Object permanence: Do objects present in the scene remain throughout the generated video?

<!-- chunk {"id": "body-0251", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Verity: Does the generated video faithfully represent the real world without unexpected imaginary objects?

<!-- chunk {"id": "body-0252", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Overall: Is the generated video reasonable for the robot to plan accordingly?

<!-- chunk {"id": "body-0253", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Human evaluators are tasked to observe a pair of anonymous videos generated by different models but with the same language instruction and compare them along the dimensions listed above. A group of ten human evaluators performed the evaluation over 23 test episodes. The statistical results are summarized in Fig. 24.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Evaluation", "weight": 1.0} -->

As shown, we find that both Cosmos-Predict1-7B-Video2World-Sample-Instruction and Cosmos-Predict1-5B-Video2World-Sample-Instruction perform better than VideoLDM-Instruction along the four evaluation dimensions. Cosmos-Predict1-7B-Video2World-Sample-Instruction achieved $78.3\%$ overall preference compared to $13.0\%$ for VideoLDM-Instruction. Cosmos-Predict1-5B-Video2World-Sample-Instruction has also achieved better performance than diffusion-based VideoLDM-Instruction. Some predicted video frames for both fine-tuned WFMs are presented in Fig. 25, which shows the quality of the predicted videos.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Evaluation", "weight": 1.0} -->

For action-based next frame prediction, we fine-tuned our models on the Bridge dataset. As a baseline, we fine-tune IRASim to derive an action-based next-frame prediction model IRASim-Action. We perform the next-frame prediction autoregressively to generate videos. To evaluate video generation quality, we compare the generated videos against ground truth videos over 100 episodes randomly selected from the official Bridge test set.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Cosmos-Predict1-5B-Video2World- Sample-ActionCond Cosmos-Predict1-7B-Video2World- Sample-ActionCond Table 23: Evaluation of action-based next-frame prediction on Bridge dataset.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Evaluation", "weight": 1.0} -->

The computed metrics are summarized in Tab. 23, including PSNR, SSIM, Latent L2, and FVD. As shown, both Cosmos-Predict1-5B-Video2World-Sample-ActionCond and Cosmos-Predict1-7B-Video2World-Sample-ActionCond models outperform the baseline model (IRASim-Action). Some predicted video frames are presented in Fig. 26, which shows the quality of the predicted videos compared to the ground truth.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Post-training WFM for Autonomous Driving", "weight": 1.0} -->

A world model for in-the-wild driving scenes has the potential to serve as a powerful simulation engine for training autonomous driving agents. As most autonomous vehicles are equipped with multiple cameras viewing different directions, an ideal world model for an autonomous vehicle should also be a multi-view one, preferably matching the precise setup of the sensors in the target vehicle. Here, we demonstrate how we fine-tune our pre-trained WFM to create a multi-view world model for autonomous driving tasks.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Dataset", "weight": 1.0} -->

We curate an internal dataset called the Real Driving Scene (RDS) dataset. It comprises approximately 3.6 million 20-second surround-view video clips (equivalent to approximately $20,000$ hours of data) captured using an NVIDIA internal driving platform. Each clip is recorded from six camera views: front, left, right, rear, rear-left, and rear-right. In addition, the dataset includes ego-motion information that we use to construct the trajectory data. We use the recorded timestamps of the front camera video to synchronize the frames of all other views.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Dataset", "weight": 1.0} -->

This dataset was selected from a large labeled data corpus to match a target distribution of data attributes. The specific attribute tags include: Contender vehicle density (\\eg, none, low, medium, high) Weather (\\eg, clear, raining, snowing, fog) Illumination (\\eg, day, night) Ego vehicle speed (\\eg, standing, low, local, highway speeds) Ego vehicle behavior (\\eg, high, medium, low curvature trajectories and accelerations) Road type/population density (based on OpenStreetMap definitions: rural, residential, urban).

<!-- chunk {"id": "body-0261", "role": "body", "section": "Dataset", "weight": 1.0} -->

Additionally, the dataset was augmented through a second data-mining run to ensure a minimum number of clips containing rare road structures (\\eg, tollbooths, bridges, tunnels, speed bumps, \\etc). Finally, videos from each camera view are captioned separately, starting with a template text string: "The video is captured from a camera mounted on a car. The camera is facing forward\|left\|right\|backward\|rear-left\|rear-right."

<!-- chunk {"id": "body-0262", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

We fine-tune our Cosmos-Predict1-7B-Text2World (Sec. 5.1) into a multiple-view world model using the RDS dataset. To ensure consistent video generation across multiple views, we slightly modify the architectural design described in Sec. 5.1 and fine-tune the WFM to generate videos from all six cameras simultaneously.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

We build three multi-view world models, summarized in Tab. 21. The first one is called Cosmos-Predict1-7B-Text2World-Sample-MultiView, which is a multi-view world model that can generate six camera views based on a text prompt input. The second one is called Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond. This model is built on top of Cosmos-Predict1-7B-Text2World-Sample-AV-MultiView and takes an additional trajectory input as the conditional input signal. The final model, Cosmos-Predict1-7B-Video2World-Sample-MultiView, is fine-tuned from the Diffusion-7B-Video2World-Sample-MultiView model to support video-based conditioning. It achieves this by incorporating previous frames into the generation process. Cosmos-Predict1-7B-Video2World-Sample-MultiView can take the video output from Cosmos-Predict1-7B-Text2World-Sample-MultiView and generate its extension. All three models output 6 views of 57 frames of video at a resolution of $848 \times 480$.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

View-independent positional embedding and view embedding. Instead of extending the FPS-aware 3D RoPE Positional Embedding to include an additional view dimension, we opt to use the same positional embedding described in Sec. 5.1 independently to each view. To represent view differences, we modify the denoising function $D_{\theta}$ to take an additional view embedding as input. That is, the camera view information is supplied through global view embeddings instead of positional embedding.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

View-dependent cross-attention. In our multi-view setting, each of the six views of the same scene would have a different video description. While we treat all six views as a whole as the state of the diffusion process and perform self-attention among all the elements in the six views for denoising, we find it beneficial to employ view-dependent cross-attention for textual inputs. Specifically, the cross-attention operation for each view only attends to the textual description for the specific view. Note that each view has a different video description in our dataset. With the view embedding and view-dependent cross-attention, we derive Cosmos-Predict1-7B-Text2World-Sample-MultiView from fine-tuning Cosmos-Predict1-7B-Text2World.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

Trajectory control condition. Optionally, in addition to the text condition, we fine-tune the model to produce videos that conform to the given future trajectory paths to enable more precise control of the agent. This enables the generation of unique driving scenarios that adhere to both driving trajectories recorded by real-world data and driving environments specified by the input text descriptions. The fine-tuned model is Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

We define a trajectory as a sequence of 64 points in the 3D space, representing a sequence of translations of the agent from the initial position $$ to the final destination, with each point separated by a 0.1-second interval. We compute the embedding of the trajectory input and make the result a conditional input to the denoiser of the fine-tuned Cosmos-Predict1-7B-Video2World model. We note that it is possible to achieve more fine-grained control signals by giving a per-interval action vector, following prior works or as in the robotic manipulation task (Sec. 6.2). We leave such extensions for future work.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

Prompt: The video captures a highway scene with a white truck in the foreground, moving towards the camera. The truck has a large cargo area and is followed by a motorcyclist wearing a full-face helmet. The road is marked with white lines and has a metal guardrail on the right side. The sky is partly cloudy, and there are green trees and bushes visible on the roadside. The video is taken from a moving vehicle, as indicated by the motion blur and the changing perspective of the truck and motorcyclist. Prompt: The footage shows a multi-car pile-up on a foggy highway. Visibility is severely reduced due to thick fog, with only the taillights of vehicles ahead visible. Suddenly, brake lights flash, and cars begin to swerve and stop abruptly. The highway is cluttered with stopped and crashed vehicles. The surroundings are obscured by fog, adding to the chaos and confusion of the scene.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Fine-tuning", "weight": 1.0} -->

Prompt: There are towering, intricately designed ice castle illuminated from within. Ahead, the sky showcases a vibrant sunset and a luminous moon positioned to the left of the castle, casting a blue hue across the scene. Fast-moving, dark, and dramatic clouds add to the otherworldly atmosphere. The 3D realistic art style focuses on lighting and texture, creating a striking visual effect. Prompt: The footage captures a coastal area where the ocean meets a rugged, rocky cliff. Ahead, vibrant blue waves crash against the rocks, creating white foam. The cliff is a mix of brown and green hues, indicating vegetation and possibly moss or algae.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Cosmos-Predict1-7B-Text2World- Sample-MultiView Cosmos-Predict1-7B-Text2World- Sample-MultiView-TrajectoryCond Real Videos (Reference) Table 24: Evaluation on post-trained multi-view world models for multi-view driving video generation.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Cosmos-Predict1-7B-Text2World- Sample-MultiView Cosmos-Predict1-7B-Text2World- Sample-MultiView-TrajectoryCond Real Videos (Reference) Table 25: Trajectory consistency evaluation on post-trained multi-view world models for multi-view driving video generation. The numbers of TAE are scaled by 102 for convenience, and the unit for TFE is cm.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We first present text-conditioned qualitative results in Fig. 27. Using Cosmos-Predict1-7B-Text2World-Sample-MultiView, we generate a 57-frame video with six views, which is then extended to 201 frames using the Cosmos-Predict1-7B-Video2World-Sample-MultiView model. In Fig. 28, we demonstrate how the pre-trained world model enhances generalization, enabling the generation of rare or out-of-domain scenes from the RDS dataset, such as driving on a river. Lastly, Fig. 29 showcases the results from Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond, where the ego car accurately follows the input trajectory.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Evaluation", "weight": 1.0} -->

For quantitative results, as a baseline, we followed the same fine-tuning recipe to fine-tune VideoLDM to derive a multi-view world model called VideoLDM-MultiView. We use a set of evaluation metrics measuring video generation quality, multi-view consistency, and trajectory following accuracy. To evaluate video generation quality, we use 1000 samples to compute the scores. For consistency-related metrics, to better understand different models' behaviors under different scenarios, we categorize the ground-truth trajectories into four types: moving forward, turning left, turning right, and others (including static or complex movements). For each category, we gathered 200 samples and their corresponding prompts and conditions, totaling 800 samples. Below, we provide detailed descriptions of the metrics and the results.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Visualized Trajectory Input Figure 29: Trajectory-conditioned generated samples from Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond. Given the trajectory inputs on the left-most column, we generate multiview videos that follow the given trajectory. We visualize the front camera view in this figure.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Generation quality. We utilize Fréchet Inception Distance (FID) and Fréchet Video Distance (FVD) to measure the quality of the generated videos relative to the real ones. We first calculate a score per view by extracting 16 frames from each video. We then report the average score across all views per method. As shown in Tab. 24, we find both Cosmos-Predict1-7B-Text2World-Sample-MultiView and Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond significantly outperform VideoLDM-MultiView on both metrics, demonstrating the superior quality of our pre-trained 7B Diffusion-based WFM over the VideoLDM-MultiView baseline.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Multi-view consistency. We use an extended version of the Sampson error formulated in Sec. 5.3.1 to quantify the geometry consistency of the generated multi-view videos. As the ground-truth videos in our RDS dataset share similar fisheye camera intrinsic parameters, we use the median calibration to undistort the keypoints to a regular pinhole camera with a uniform size of $960 \times 540$ and 120 degrees of horizontal FoV. Under this setting, two metrics are computed for the generated multi-view video: *Temporal Sampson Error (TSE)* measures whether the content generated for each camera is consistent over time. It is the median Sampson error of adjacent frames for each of the views.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Evaluation", "weight": 1.0} -->

*Cross-view Sampson Error (CSE)* measures whether multi-view consistency is preserved over time. It is the Sampson error across different generated views averaged in time. The fundamental matrix used in CSE is estimated using the keypoints accumulated across all temporal frames.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Evaluation", "weight": 1.0} -->

As shown in Tab. 24, we find that both Cosmos-Predict1-7B-Text2World-Sample-MultiView and Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond render better multi-view geometry consistency over VideoLDM-MultiView. The overall geometric plausibility of the generated videos is much better for a world model fine-tuned from our WFM. We also note that, with the trajectory control condition, such consistency is further improved thanks to the explicit 3D guidance as Cosmos-Predict1-7B-Text2World-Sample-MultiView-TrajectoryCond is ranked the best.

<!-- chunk {"id": "body-0279", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Trajectory consistency: Trajectory Agreement Error (TAE). We design a robust multi-view camera pose estimation pipeline similar to the one used in Liang et al. based on the formulation of Teed and Deng. Such a pose estimation pipeline features an online dynamic mask generation module and a highly efficient dense bundle adjustment module, reaching a robust and real-time performance for estimating multi-view camera poses. We use this pipeline to estimate the camera poses of the front camera, separately using two multi-view camera configurations that consider "front + left-front" cameras and "front + right-front" cameras. We then calculate their trajectory errors to show their agreement, reflecting the consistency of the multi-view generation. Specifically, we compute the Absolute Trajectory Error (ATE) and Relative Pose Error for both the translational component (RPE-t) and the rotational component (RPE-R). We normalize the length of the trajectories to 1.0 for fair comparison and exclude the cases with minor camera movements (\\eg, a car stopped at a red light).

<!-- chunk {"id": "body-0280", "role": "body", "section": "Evaluation", "weight": 1.0} -->

As shown in Tab. 25, the results echo the findings from the multi-view geometry consistency, where the trajectory consistency of the world models fine-tuned from the Cosmos WFM is much better than that from the VideoLDM-MultiView. We note that the post-trained Cosmos world models have trajectory consistency that is close to real-world videos.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Trajectory consistency: Trajectory Following Error (TFE). Furthermore, for the model where we have trajectory control conditions being fed into the model, we use the same camera pose estimation pipeline used above to compute the poses of the front camera using multi-view information and compare the predicted trajectory with respect to the ground truth trajectory condition. This measures how well the model follows the given trajectory path. As shown in Tab. 25, the trajectory error estimated using the generated videos from our Cosmos post-trained world models is only $<$`<!-- -->`{=html}7cm less precise than the ground-truth oracle. Such a considerably slight margin shows that our model is able to accurately follow the given trajectory path, which is crucial for training autonomous driving agents.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Objects tracking consistency. Finally, we applied object detection and tracking using on the generated 8-second videos. Human annotators were tasked with identifying instances where the tracking algorithm misinterpreted physically impossible scenarios, such as two distinct objects (\\eg, a person and a car) merging incorrectly into a single tracked entity. To evaluate this, we provided annotators with a random sample of 20 generated videos containing 157 objects. Remarkably, none of the 157 objects exhibited any physically impossible scenarios, demonstrating the physical consistency and object permanence of our generated driving videos.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Guardrails", "weight": 1.0} -->

For the safe use of our WFMs, we develop a comprehensive guardrail system. It consists of two stages: the pre-Guard stage and the post-Guard stage. The pre-Guard stage leverages Aegis and a keyword list to block harmful prompts. The post-Guard stage blocks harmful visual outputs using a video content safety classifier and a face blur filter. The pipeline is illustrated in Fig. 30.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Pre-Guard", "weight": 1.0} -->

Our pre-Guard is a text-domain guardrail comprising an LLM-based guardrail for semantically complex prompts and a simple blocklist-based checker for explicitly unsafe keywords.

<!-- chunk {"id": "body-0285", "role": "body", "section": "Keyword Blocking", "weight": 1.0} -->

The blocklist heuristic will act as the first line of defense to mitigate the risk of generating unsafe content. This is designed to block explicitly harmful generations by doing a keyword search on the prompt against a hard-coded blocklist of a large corpus of explicit and objectionable words. Input words are lemmatized using *WordNetLemmatizer*, a tool that uses a lexical database of the English language to extract the root word from its variants. For example, the root word of "abacii" is "abacus". These lemmatized words are then compared to the words in the hard-coded blocklist, and the entire prompt is rejected if any profanity is found. We use a comprehensive set of keywords to maximally protect our users.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Aegis Guardrail", "weight": 1.0} -->

As the second line of defense, we use *Aegis-AI-Content-Safety-LlamaGuard-LLM-Defensive-1.0*, which is a fine-tuned version of *Llama-Guard* trained on NVIDIA's Aegis Content Safety Dataset covering NVIDIA's broad taxonomy of 13 critical safety risk categories. There are two versions of AEGIS 1.0, the defensive version and the permissive version. The defensive version adopts a tighter permission boundary than the permissive version. Cosmos uses the defensive version of Aegis to block potentially harmful user prompts that attempt to generate harmful content. If the input prompt is categorized as unsafe by this prompt filter, the video is not generated, and an error message is displayed.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Aegis Guardrail", "weight": 1.0} -->

For using Aegis as a prompt filter, we classify the prompt as unsafe if it falls into the following categories: violence, sexual, criminal planning, weapons, substance abuse, suicide, child sexual abuse material, hatred, harassment, threat, and profanity. Any prompt that does not fall into the above categories is considered safe from the prompt-filtering standpoint.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Post-Guard", "weight": 1.0} -->

Our post-Guard is a vision-domain guardrail comprising a video content safety filter and a face blur filter for the generated output.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Video Content Safety Filter", "weight": 1.0} -->

The Video Content Safety Filter is a frame-level multi-class classifier trained on our video dataset and generation results. Among the classes, some are considered safe, while others are unsafe. A major challenge in training the classifier is in balancing false positives, where safe content is mistakenly flagged as unsafe, and false negatives, where unsafe content is wrongly classified as safe. To minimize classification errors, we carefully balanced the data during training.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Video Content Safety Filter", "weight": 1.0} -->

We collect three kinds of ground truth annotated data. First, we sample a large set of videos from our dataset, extract frames, and determine its class using a VLM. Next, we generate synthetic videos with our WFMs using a set of prompts to ensure coverage of corner cases and least-represented content categories. Finally, human annotators provide the "gold standard" labels for a portion of our dataset, adding a vital layer of validation and helping us continuously refine the accuracy of our classifier. We extract the SigLIP embedding for each video frame and train a simple MLP classifier on the embeddings. ing inference, we generate a SigLIP embedding for every frame and then apply the classifier. The entire video is flagged as unsafe if any frame is classified as unsafe

<!-- chunk {"id": "body-0291", "role": "body", "section": "Face Blur Filter", "weight": 1.0} -->

We use RetinaFace, a state-of-the-art face detection model, to identify facial regions with high confidence scores. For any detected face region larger than $20 \times 20$ pixels, we apply pixelation to obscure the regions while preserving the overall scene composition for Physical AI applications.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Red Team Effort", "weight": 1.0} -->

We employ a dedicated red team to actively probe the system using both standard and adversarial examples that are collected in an internal attack prompt dataset. These video outputs are annotated by a team of expert annotators, who were specially trained for our task, to classify the generated video on a scale of 1-5 on multiple categories of harm related to the taxonomy in Sec. 7.1.2. These annotations also specify the start and end-frames where the unsafe content is detected, thereby generating high-quality annotations. The red team also probed each guardrail component independently with targeted examples to identify weaknesses and improve performance in edge cases. As of the date of publication, the red team has tested and annotated over $10,000$ distinct prompt-video pairs that were carefully crafted to cover a broad range of unsafe content.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Conclusions and Discussions", "weight": 1.0} -->

The Cosmos World Foundation Models mark a significant step towards building general-purpose simulators for the physical world. This work outlines our comprehensive approach, including the data curation pipeline, the design of continuous and discrete tokenizers, the architecture of diffusion and autoregressive world foundation models, and the fine-tuning process for diverse downstream Physical AI tasks. Notably, we demonstrate the adaptability of our pre-trained world models to critical applications, including 3D world navigation, robotic manipulation, and autonomous vehicle systems, which demand both 3D consistency and action controllability.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Conclusions and Discussions", "weight": 1.0} -->

Limitations. Despite the progress, the development of world foundation models is still in the early stages. Current models, including ours, fall short as reliable simulators of the physical world. We observe that our models still suffer from issues, including the lack of object permanence, inaccuracies in contact-rich dynamics, and inconsistency in instruction following. Additionally, the realism of the generated videos does not always reflect adherence to fundamental physical principles, such as gravity, light interactions, and fluid dynamics.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Conclusions and Discussions", "weight": 1.0} -->

Evaluation presents another significant challenge. Defining robust rubrics for humans to evaluate physical fidelity is hard as such assessments are often influenced by personal biases, backgrounds, and other subjective factors. Moreover, these evaluations may not align positively with metrics used in downstream Physical AI tasks. In order to address these challenges, promising directions include the development of automated evaluators powered by multi-modal LLMs and leveraging existing physical simulators to enable reproducible and interactive evaluation, thereby reducing dependence on human evaluation.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Conclusions and Discussions", "weight": 1.0} -->

Autoregressive \\vsDiffusion WFMs. Our evaluation results in 3D consistency (Sec. 5.3.1) and video generation for robotics (Sec. 6.2) indicate that diffusion-based WFMs currently deliver better generation quality. Through fine-tuning, diffusion-based WFMs are able to incorporate diverse control signals, including camera pose, end-effector positions, or autonomous vehicle trajectories, and generate outputs of novel formats like multi-view videos. However, autoregressive-based WFMs possess significant untapped potential. They could leverage pre-trained weights from large language models (LLMs) to inherit extensive world knowledge and enable faster generation through the use of advanced inference optimization techniques designed for causal attention. If these capabilities are fully realized, autoregressive WFMs may become particularly well-suited for applications requiring interactive control or real-time processing, such as planning and simulation in robotics. Importantly, the boundary between diffusion and autoregressive models is not rigid.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Conclusions and Discussions", "weight": 1.0} -->

Recent advancements have shown that diffusion transformers with bidirectional attention can be distilled into student transformers with causal attention, enabling support for key-value caching during inference. Similarly, autoregressive models can incorporate locally bidirectional attention to generate images via diffusion heads. Exploring these hybrid approaches and their trade-offs remains an active and promising area of research. We plan to investigate these formulations further and provide a comprehensive analysis in future work.
