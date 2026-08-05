<!-- arxiv-full-text:v1 {"arxiv_id": "2402.15391", "source": "arxiv-html"} -->

## Abstract

We introduce Genie, the first *generative interactive environment* trained in an unsupervised manner from unlabelled Internet videos. The model can be prompted to generate an endless variety of action-controllable virtual worlds described through text, synthetic images, photographs, and even sketches. At 11B parameters, Genie can be considered a *foundation world model*. It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model. Genie enables users to act in the generated environments on a frame-by-frame basis *despite training without any ground-truth action labels* or other domain-specific requirements typically found in the world model literature. Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.

### keywords

Generative AI, Foundation Models, World Models, Video Models, Open-Endedness

## 1. Introduction

The last few years have seen an emergence of *generative AI*, with models capable of generating novel and creative content. Driven by breakthroughs in architectures such as transformers, advances in hardware, and a recent focus on scaling models and datasets, we can now generate coherent, conversational language, as well as crisp and aesthetically pleasing images from a text prompt. Early signs indicate video generation will be yet another frontier, with recent results suggesting that such models may also benefit from scale. Still, there remains a gulf between the level of interactions and engagement of video generative models and language tools such as ChatGPT, let alone more immersive experiences.

What if, given a large corpus of videos from the Internet, we could not only train models capable of generating novel images or videos, but entire interactive experiences? We propose *generative interactive environments*, a new paradigm for generative AI whereby interactive environments can be generated from a single text or image prompt. Our approach, Genie, is trained from a large dataset of over 200,000 hours of publicly available Internet gaming videos and, despite training *without action or text annotations*, is controllable on a frame-by-frame basis via a learned latent action space (see Table˜1 for a comparison to other approaches). At 11B parameters, Genie exhibits properties typically seen in foundation models---it can take an unseen image as a prompt making it possible to create and play entirely imagined virtual worlds (e.g Figure˜1).

Figure 1: Diverse trajectories: Genie is a generative model that can be used as an interactive environment. The model can be prompted in various ways, either with a generated image (top) or a hand-drawn sketch (bottom). At each time step, the model takes a user-provided latent action to generate the next frame, producing trajectories with interesting and diverse character actions.

Genie builds on ideas from state-of-the-art video generation models, with a core design choice being spatiotemporal (ST) transformers which are used in all of our model components. Genie utilizes a novel video tokenizer, and extracts latent actions via a causal action model. Both the video tokens and latent actions are passed to a dynamics model, which autoregressively predicts the next frame using MaskGIT. We provide a rigorous scaling analysis of our architecture with respect to both batch and model size, which we vary from 40M to 2.7B parameters. The results show that our architecture scales gracefully with additional computational resources, leading to a final 11B parameter model. We train Genie on a filtered set of 30,000 hours of Internet gameplay videos from hundreds of 2D platformer games, producing a foundation world model for this setting.

To demonstrate the generality of our approach, we also train a separate model on action-free robot videos from the RT1 dataset, learning a generative environment with consistent latent actions. Finally, we show that latent actions learned from Internet videos can be used for inferring policies from unseen action-free videos of simulated reinforcement learning (RL) environments, indicating that Genie may hold the key to unlocking unlimited data for training the next generation of generalist agents.

Figure 2: Genie model training: Genie takes in T frames of video as input, tokenizes them into discrete tokens z via the video tokenizer, and infers the latent actions $\tilde{\bm{a}}$ between each frame with the latent action model. Both are then passed to the dynamics model to generate predictions for the next frames in an iterative manner.

Table 1: A new class of generative model: Genie is a novel video and world model that is controllable on a frame-by-frame basis, which requires only video data at train time.

## 2. Methodology

Genie is a generative interactive environment trained from video-only data. In this section we begin with preliminaries before explaining the main components of our model.

Several components in the Genie architecture are based on the Vision Transformer (ViT). Notably, the quadratic memory cost of transformers poses challenges for videos, which can contain up to $O(10^{4})$ tokens. We thus adopt a memory efficient ST-transformer architecture (inspired by Xu et al., see Figure˜3) across all model components, balancing model capacity with computational constraints.

Figure 3: ST-transformer architecture. The architecture is composed of L spatiotemporal blocks, each containing a spatial layer, temporal layer and feed-forward layer. Each color represents a single self-attention map, with the spatial layer attending over the H × W tokens from within a single time step, and temporal the same token from across the T time steps.

Unlike a traditional transformer where every token attends to all others, an ST-transformer contains $L$ spatiotemporal blocks with interleaved spatial and temporal attention layers, followed by a feed-forward layer (FFW) as standard attention blocks. The self-attention in the spatial layer attends over the $1\times H\times W$ tokens within each time step, and in the temporal layer attends over $T\times 1\times 1$ tokens across the $T$ time steps. Similar to sequence transformers, the temporal layer assumes a causal structure with a causal mask. Crucially, the dominating factor of computation complexity (i.e. the spatial attention layer) in our architecture scales linearly with the number of frames rather than quadratically, making it much more efficient for video generation with consistent dynamics over extended interactions. Further, note that in the ST block, we include only one FFW after both spatial and temporal components, omitting the post-spatial FFW to allow for scaling up other components of the model, which we observe to improve results significantly.

### Model Components

As shown in Figure˜2, our model contains three key components: 1) a *latent action model* that infers the latent action $\bm{a}$ between each pair of frames and 2) a *video tokenizer* that converts raw video frames into discrete tokens $\bm{z}$ and 3) a *dynamics model* that, given a latent action and past frame tokens, predicts the next frame of the video. The model is trained in two phases following a standard autoregressive video generation pipeline: we train the video tokenizer first, which is used for the dynamics model. We then co-train the latent action model (directly from pixels) and the dynamics model (on video tokens).

Latent Action Model (LAM) To achieve controllable video generation, we condition each future frame prediction on the action taken at the previous frame. However, such action labels are rarely available in videos from the Internet and action annotation can be costly to obtain. Instead, we learn *latent actions* in a fully unsupervised manner (see Figure˜4).

Figure 4: Latent action model: learns actions at unsupervised from unlabelled video frames.

First, an encoder takes as inputs all previous frames $\bm{x}_{1:t}=(x_{1},\cdots x_{t})$ as well as the next frame $x_{t+1}$, and outputs a corresponding set of continuous latent actions $\tilde{\bm{a}}_{1:t}=(\tilde{a}_{1},\cdots\tilde{a}_{t})$. A decoder then takes all previous frames and latent actions as input and predicts the next frame $\hat{x}_{t+1}$.

To train the model, we leverage a VQ-VAE-based objective, which enables us to limit the number of predicted actions to a small discrete set of codes. We limit the vocabulary size $|A|$ of the VQ codebook, i.e. the maximum number of possible latent actions, to a small value to permit human playability and further enforce controllability (we use $|A|=8$ in our experiments). As the decoder only has access to the history and latent action, $\tilde{a}_{t}$ should encode the most meaningful changes between the past and the future for the decoder to successfully reconstruct the future frame. Note that this decoder exists only to give the LAM training signal. In fact, apart from the VQ codebook, the entire LAM is discarded at inference time and replaced with actions from the user.

We utilize our ST-transformer architecture for the latent action model. The causal mask in the temporal layer allows us to take the entire video $\bm{x}_{1:T}$ as input and generate all latent actions between each frame $\tilde{\bm{a}}_{1:T-1}$.

Video Tokenizer Following prior work, we compress videos into discrete tokens to reduce dimensionality and enable higher quality video generation (see Figure˜5). We again make use of VQ-VAE, which takes in $T$ frames of video $\bm{x}_{1:T}=(x_{1},x_{2},\cdots,x_{T})\in\mathbb{R}^{T\times H\times W\times C}$ as input, generating discrete representations for each frame $\bm{z}_{1:T}=(z_{1},z_{2},\cdots,z_{T})\in\mathbb{I}^{T\times D}$, where $D$ is the size of the discrete latent space. The tokenizer is trained using a standard VQ-VQAE objective over the entire video sequence.

Figure 5: Video tokenizer: a VQ-VAE with ST-transformer.

Unlike prior works that focus on spatial-only compression in the tokenization phase, we utilize the ST-transformer in both the encoder and decoder to incorporate temporal dynamics in the encodings, which improves the video generation quality. By the causal nature of the ST-transformer, each discrete encoding $z_{t}$ contains information from all previously seen frames of the video $\bm{x}_{1:t}$. Phenaki also uses a temporal-aware tokenizer, C-ViViT, but this architecture is compute intensive, as the cost grows quadratically with the number of frames---in comparison, our ST-transformer based tokenizer (ST-ViViT) is much more compute efficient with the dominating factor in its cost increasing linearly with the number of frames.

Figure 6: Dynamics model: takes in video tokens and action embeddings, and predicts future masked video tokens.

Dynamics Model The dynamics model is a decoder-only MaskGIT transformer (Figure˜6). At each time step $t\in[1,T]$, it takes in the tokenized video $\bm{z}_{1:t-1}$ and stopgrad latent actions $\tilde{\bm{a}}_{1:t-1}$ and predicts the next frame tokens $\hat{z}_{t}$. We again utilize an ST-transformer, whose causal structure enables us to use tokens from all $(T-1)$ frames $\bm{z}_{1:T-1}$ and latent actions $\tilde{\bm{a}}_{1:T-1}$ as input, and generate predictions for all next frames $\hat{\bm{z}}_{2:T}$. The model is trained with a cross-entropy loss between the predicted tokens $\hat{\bm{z}}_{2:T}$ and ground-truth tokens $\bm{z}_{2:T}$. At train time we randomly mask the input tokens $\bm{z}_{2:T-1}$ according to a Bernoulli distribution masking rate sampled uniformly between $0.5$ and $1$. Note that a common practice for training world-models, including transformer-based models, is to concatenate the action at time $t$ to the corresponding frame. However, we found that treating the latent actions as *additive embeddings* for both the latent action and dynamics models helped to improve the controllability of the generations.

### Inference: Action-Controllable Video Generation

Figure 7: Genie Inference: the prompt frame is tokenized, combined with the latent action taken by the user, and passed to the dynamics model for iterative generation. The predicted frame tokens are then decoded back to image space via the tokenizer’s decoder.

We now describe how to use Genie for action-controllable video generation at inference time (see Figure˜7). A player first prompts the model with an image $x_{1}$ that serves as the initial frame^11^1The model can be conditioned on a varying number of prompt frames. Here we start from one image as an example.. The image is tokenized using the video encoder, yielding $z_{1}$. The player then specifies a discrete latent action $a_{1}$ to take by choosing any integer value within $0,|A|)$.^22^2When first interacting with the model, it is unclear how each latent action will impact the next frame generation. However, we found that the meaning of each action *remained consistent* across different inputs. Hence, interpreting the mapping of latent actions is akin to learning the buttons on a new controller. The dynamics model takes the frame tokens $z_{1}$ and corresponding latent action $\tilde{a}_{1}$, which is obtained by indexing into the VQ codebook with the discrete input $a_{1}$, to predict the next frame tokens $z_{2}$. This process is repeated to generate the rest of the sequence $\hat{\bm{z}}_{2:T}$ in an autoregressive manner as actions continue to be passed to the model, while tokens are decoded into video frames $\hat{\bm{x}}_{2:T}$ with the tokenizer's decoder. Note that we can regenerate ground truth videos from the dataset by passing the model the starting frame and inferred actions from the video, or generate completely new videos (or trajectories) by changing the actions.

## 3. Experimental Results

Figure 8: Scaling results. Left: Training curves for different model sizes, Middle: Final training loss for each model size, averaged over the last 300 updates, Right: Final training loss for a 2.3B model with different batch sizes.

Datasets We train Genie on a large-scale dataset collected from publicly available Internet videos of 2D Platformer games (referred to from here on as "Platformers"). We construct the Platformers dataset by filtering publicly available videos for keywords relating to platformers, yielding 55M 16s video clips at 10FPS, with 160x90 resolution. The final dataset contains 6.8M 16s video clips (30k hours), within an order of magnitude of other popular Internet video datasets. More details can be found in Section˜B.1. Unless otherwise specified, results are with a 11B-parameter model trained on this dataset.

To verify the generality of our method, we also consider the robotics datasets used to train RT1 Brohan et al., combining their dataset of ${\sim}130k$ robot demonstrations with a separate dataset of simulation data and the 209k episodes of real robot data from prior work. Note that we do not use actions from any of these datasets, and simply treat them as videos. For simplicity, from here on we refer to this dataset as "Robotics".

Metrics We examine the video generation performance of Genie via two factors, namely *video fidelity*, i.e. the quality of video generation, and *controllability*, i.e. how much impact the latent actions have in video generation. For video fidelity we use the Frechet Video Distance (FVD), a video-level metric, which has been shown to have a high level of alignment to human evaluation on video quality. For controllability, we devise a metric based on peak signal-to-noise ratio (PSNR) which we call $\Delta_{t}\text{PSNR}$, that measures how much the video generations differ when conditioned on latent actions inferred from ground-truth ($\hat{x}_{t}$) vs. sampled from a random distribution ($\hat{x}_{t}^{\prime}$): where $x_{t}$ denotes the ground-truth frame at time $t$, $\hat{x}_{t}$ denotes the frame from latent actions $\tilde{\bm{a}}_{1:t}$ inferred from ground-truth frames, and $\hat{x}_{t}^{\prime}$ the same frame generated from a sequence of latent actions randomly sampled from a categorical distribution. As such, the greater $\Delta_{t}\text{PSNR}$ is, the more the video generated from random latent actions differs from ground-truth, which indicates a higher level of controllability from the latent actions. For all experiments we report $\Delta_{t}\text{PSNR}$ with $t=4$.

Training Details Our video tokenizer uses 200M parameters, a patch size of 4 and a codebook with embedding size 32 and 1024 unique codes, which we found to be the most effective given the trade-off between reconstruction quality of the tokenizer and downstream performance of video prediction. The latent action model has 300M parameters, a patch size of 16, and a codebook with embedding size 32 and 8 unique codes (latent actions). For all modelling components we use a sequence length of 16 frames with an FPS of 10. Further, we employ bfloat16 and QK norm for training our dynamics model, which has been shown to stabilize training at large scale. At inference time, we perform 25 MaskGIT steps for the sampling of each frame with a temperature of 2 using random sampling. See Appendix˜C for more details.

### Scaling Results

In this section, we investigate the scaling behavior of our model. To this end, we conduct studies that explore the impact of both model size and batch size. See Appendix˜D for more details on architecture and compute usage.

Figure 9: Playing from Image Prompts: We can prompt Genie with images generated by text-to-image models, hand-drawn sketches or real-world photos. In each case we show the prompt frame and a second frame after taking one of the latent actions four consecutive times. In each case we see clear character movement, despite some of the images being visually distinct from the dataset.

Scaling Model Size Given a fixed video tokenizer and action model architecture, we train a series of dynamics models ranging from 40M to 2.7B parameters. Figure˜8 shows our architecture scales gracefully with model parameters, with each increase in size corresponding to a consistent decrease in the final training loss. This is a strong indication that our approach benefits from scaling, which we exploit with our main Genie model.

Scaling Batch Size We also investigate the effect of scaling the batch size, considering a 2.3B model with batch sizes of 128, 256, and 448, equating to 1.9M, 3.8M and 6.6M tokens. As shown in Figure 8, increasing the batch size leads to a similarly favorable gain in terms of model performance.

Genie Model It is clear that increasing both model size and batch size helps improve model performance. As a result, for our final model, we train a 10.1B dynamics model with a batch size of 512, for a total of 125k steps, using 256 TPUv5p. When combined with the tokenizer and action model this brings the total to 10.7B parameters, trained on 942B tokens, which we refer to as the Genie model. For our website, we train a larger decoder mapping tokens to 360p videos, adding additional parameters.

### Qualitative Results

We now present qualitative results from the Genie model. We showcase a 11B parameter model trained on the Platformers dataset and a smaller model trained on the Robotics dataset. Our model generates high-quality, controllable videos across diverse domains. Notably, we qualitatively evaluate our Platformers-trained model using *only out-of-distribution (OOD) image prompts*, including those generated from text-to-image models, hand-drawn sketches, and even realistic photos. The ability to generalize to such significantly OOD inputs underscores the robustness of our approach and the value of training on large-scale data, which would not have been feasible with real actions as input.

Figure 10: Learning to simulate deformable objects: we show frames from a ten step trajectory in the model, taking the same action. Genie is capable of learning the physical properties of objects such as bags of chips.

Platformers-trained model Figure˜9 showcases examples of our model's generations prompted from OOD images, including (top row) images generated from Imagen2, (second row) hand-drawn sketches and (bottom row) real-world photos. Genie is able to bring these imagined worlds to life, as we see game-like behaviour when interacting with each example. We showcase more generations by our model in Appendix˜A, additionally highlighting the consistency of the latent actions.

Figure 11: Emulating parallax, a common feature in platformer games. From this initial text-generated image, the foreground moves more than the near and far middle ground, while the background moves only slightly.

Another emergent capability of our model is its ability to understand 3D scenes and emulate parallax, which is commonly seen in platformer games. In Figure˜11 we show an image generated by Imagen2, where taking a latent action moves the foreground at a different rate to the background (as indicated by the length of different colored arrows).

Figure 12: Controllable, consistent latent actions in Robotics: trajectories beginning from three different starting frames from our Robotics dataset. Each column shows the resulting frame from taking the same latent action five times. Despite training without action labels, the same actions are consistent across varied prompt frames and have semantic meaning: down, up and left.

Robotics-trained model We trained a 2.5B-parameter model on the Robotics dataset using the same hyperparameters found to be best on Platformers, achieving an FVD of 82.7 on the test split. As shown in Figure˜12, this model successfully learns distinct and consistent actions from video data, requiring neither text nor action labels (as in e.g. Yang et al. ). Notably, our model learns not only the controls of the robotic arm but also the interactions and deformations of various objects (Figure˜10). We believe this shows our approach presents a path to using larger video datasets from the Internet to create a foundational world model for robotics, with low-level controllable simulation that could be used for a variety of applications.

### Training Agents

We believe Genie could one day be used as a foundation world model for training generalist agents. In Figure 13 we show that the model can already be used for generating diverse trajectories in unseen RL environments given starting frames. We further investigate if latent actions learnt from Internet videos can be used for imitating behaviors from unseen videos. We use a frozen LAM to label a sequence of expert videos from a target environment with discrete latent actions and then train a policy that predicts the likelihood of the expert taking a latent action given an observation. We then use a small dataset with expert ground-truth actions for mapping latent to real actions (see Appendix˜E for more details).

Figure 13: Playing from RL environments: Genie can generate diverse trajectories given an image of an unseen RL environment.

We evaluate in both hard and easy settings of a procedurally generated 2D-platformer environment, CoinRun, and compare against an oracle behavioral cloning (BC) model that has access to expert actions as an upper bound, and a random agent as a lower bound (Figure 14). The LAM-based policy achieves the same score as the oracle given as few as 200 expert samples to adapt, despite almost certainly never seeing CoinRun before. This provides evidence that the learnt latent actions are consistent and meaningful for transfer, as the mapping from latent to real contains no information about the current observation.

Figure 14: BC results. Mean percentage of levels solved out of 100 samples, averaged over 5 seeds with 95% confidence intervals.

### Ablation Studies

Design choices for latent action model In designing our latent action model, we carefully considered the type of input to use. While we ultimately chose to use the original images (pixels), we evaluated this choice against the alternative of using tokenized images (replacing x with z in Figure˜4). We refer to this alternative approach as the "token-input\" model (see Table˜2).

While this model achieved a slightly lower FVD score on the Platformers dataset, it did not maintain this advantage on the Robotics dataset. More importantly, in both environments, the token-input model exhibited worse controllability (as measured by $\Delta_{t}\text{PSNR}$). This suggests that some information about video dynamics and movement might have been lost during tokenization, and as a result it is beneficial for the latent action model to take in raw videos as input.

#Params

Table 2: Latent action model input ablation. We see that Genie achieves higher controllability.

Tokenizer architecture ablations We compare the performance of three choices of tokenizers, including 1) (spatial-only) ViT, 2) (spatial-temporal) ST-ViViT and 3) (spatial-temporal) C-ViViT (Table˜3). For comparison we use similar number of parameters for all tokenizers, with patch size 10, batch size 128 and sequence length 16. We then train the same dynamics and latent action model on these three different tokenizers, and report their FVD as well as $\Delta_{t}\text{PSNR}$.

#Params

Table 3: Tokenizer architecture ablation: Our ST-ViViT architecture results in the best performing tokenizer.

Our proposed ST-ViViT architecture provides both improved video generation (FVD) and $\Delta_{t}\text{PSNR}$, for a reasonable trade-off in memory, as compared to to C-ViViT and the spatial-only ViT. This demonstrates its ability to generate videos of high fidelity and controllability, respectively. While C-ViViT employs a full space-time attention mechanism, resulting in significantly higher memory consumption compared to the other two architectures at the same parameter count, this does not translate to improved performance. In fact, C-ViViT exhibits a tendency towards overfitting, necessitating strong regularization during training, which might explain its considerably lower performance.

## 4. Related Work

World models Generative interactive environments can be considered a class of *World Models*, which enable next-frame prediction that is conditioned on action inputs. Such models can be useful for training agents, as they can be used for learning policies without direct environment experience at agent training time. However, learning the models themselves typically requires action-conditioned data obtained directly from the environment. In contrast, our approach seeks to learn a world model in an unsupervised fashion from videos alone. Recently, there has been renewed emphasis on scaling world models. GAIA-1 and UniSim learn world models for autonomous driving and robotic manipulation respectively. These approaches require both text and action labels, while we focus on training from video-only data from publicly available Internet videos.

Video models Our work is related to *video models*, which typically condition on initial frames (or text) and predict the remaining frames in a video. Our approach most resembles recent transformer based models such as Phenaki, TECO and MaskViT, as we use MaskGIT and an ST-Transformer over tokenized images. While video models are becoming increasingly controllable (e.g. ), we seek a more agentic goal and explicitly learn a *latent action space* from data, allowing users or agents to "play" the model using latent action-conditioned predictions.

Playable Video Generation Genie generalizes beyond Playable Video Generation (PVG), where latent actions are used for controlling world models learnt directly from videos. In contrast to Genie, PVG considers domain-specific static examples, rather than generating entirely new environments via prompting. Thus, scaling beyond this setting required non-trivial architectural changes, dropping inductive biases in exchange for a general method.

Environment generation Our work is also related to *Procedural Content Generation* where machine learning has proven highly effective for generating game levels, recently via language models that directly write game code. Language models themselves can also be considered to be interactive environments, albeit lacking a visual component. By contrast in our setting the levels can be learnt and generated directly from pixels, which enables us to utilize the diversity of Internet video data.

Training agents with latent actions Prior works have used latent actions for imitation from observation, planning and pre-training RL agents. These approaches have similar objectives to our latent action model, though have not been applied at scale. VPT is a recent approach that uses an inverse dynamics model learnt from human-provided action labeled data, to label Internet-scale videos with actions that can then be used for training a policy. We showed, in contrast, that we can use *latent* actions learnt from Internet videos to infer policies for arbitrary environments, avoiding the need for ground-truth actions that are costly and may not generalize.

## 5. Conclusion and Future Work

We proposed Genie, a new form of generative AI that enables anyone, even children, to dream up, create, and step into generated worlds as we can with human-designed simulated environments. Genie can be prompted to generate a diverse set of interactive and controllable environments despite training from video-only data.

There are clear improvements that can be made to the model. Genie inherits some of the weaknesses of other autoregressive transformer models, and can hallucinate unrealistic futures. And while we have made progress with spatiotemporal representations, we are still limited to 16 frames of memory which makes it challenging to get consistent environments over long horizons. Finally, Genie currently operates around 1FPS and requires future advances to achieve an efficient frame rate for interaction.

Still, we believe Genie opens up vast potential for future research. Given its generality, the model could be trained from an even larger proportion of Internet videos to simulate diverse, realistic, and imagined environments. Furthermore, we only briefly touched upon the capabilities of using Genie for training agents, but given that the lack of rich and diverse environments is one of the key limitations in RL, we could unlock new paths to creating more generally capable agents.

## Broader Impact

Societal Impact Genie could enable a large amount of people to generate their own game-like experiences. This could be positive for those who wish to express their creativity in a new way, for example children who could design and step into their own imagined worlds. We also recognize that with significant advances, it will be critical to explore the possibilities of using this technology to amplify existing human game generation and creativity---and empowering relevant industries to utilize Genie to enable their next generation of playable world development.

Training Data and Weights: We have chosen not to release the trained model checkpoints, the model's training dataset, or examples from that data to accompany this paper or the website. We would like to have the opportunity to further engage with the research (and video game) community and to ensure that any future such releases are respectful, safe and responsible.

Reproducibility: We understand that it may be challenging for researchers with fewer computational to reproduce our main results. In order to mitigate this issue, we describe a smaller scale, fully reproducible example in Appendix˜F that can run on a single mid-range TPU (or GPU). Given that many design choices translate between the two settings, we believe this will make it possible for the broader community to investigate future architectural improvements as well as additional research directions resulting from our work.
