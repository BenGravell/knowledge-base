<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GAIA-1: A Generative World Model for Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous driving promises transformative improvements to transportation, but building systems capable of safely navigating the unstructured complexity of real-world scenarios remains challenging. A critical problem lies in effectively predicting the various potential outcomes that may emerge in response to the vehicle's actions as the world evolves. To address this challenge, we introduce GAIA-1 ('Generative AI for Autonomy'), a generative world model that leverages video, text, and action inputs to generate realistic driving scenarios while offering fine-grained control over ego-vehicle behavior and scene features. Our approach casts world modeling as an unsupervised sequence modeling problem by mapping the inputs to discrete tokens, and predicting the next token in the sequence. Emerging properties from our model include learning high-level structures and scene dynamics, contextual awareness, generalization, and understanding of geometry. The power of GAIA-1's learned representation that captures expectations of future events, combined with its ability to generate realistic samples, provides new possibilities for innovation in the field of autonomy, enabling enhanced and accelerated training of autonomous driving technology.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Predicting future events is a fundamental and critical aspect of autonomous systems. Accurate future prediction enables autonomous vehicles to anticipate and plan their actions, enhancing safety and efficiency on the road. To achieve this, the development of a robust model of the world is imperative and huge efforts have been made in the past to build such predictive world models for autonomous driving. A world model learns a structured representation and understanding of the environment that can be leveraged for making informed decisions when driving.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, current approaches have had significant limitations. World models have been successfully applied to control tasks in both simulation and to real-world robotics tasks. These methods often rely on labeled data, which is challenging to obtain at scale, and models that work on simulated data may not fully capture the complexities of real-world scenarios. Furthermore, due to their low-dimensional representations, these models may struggle to generate highly realistic samples of future events, posing challenges in achieving a high level of fidelity in predictions for complex real-world applications such as autonomous driving.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Meanwhile, progress in generative image and video generation has harnessed the power of self-supervised learning to learn from large quantities of real-world data to generate remarkably realistic video samples. Yet, a significant challenge persists in this domain: the difficulty of learning a representation that captures the expected future events. While such generative models excel at generating visually convincing content, they may fall short in learning representations of the evolving world dynamics that are crucial for precise future predictions and robust decision-making in complex scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we introduce GAIA-1, a method designed with the goal of maintaining the benefits of both world models and generative video generation. It combines the scalability and realism of generative video models with the ability of world models to learn meaningful representations of the evolution into the future. GAIA-1 works as follows. First, we partition the model into two components: the world model and the video diffusion decoder. The world model reasons about the scene's high-level components and dynamics, while the diffusion model takes on the responsibility of translating latent representations back into high-quality videos with realistic detail.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the world model, we use vector-quantized representations of video frames to discretize each frame, transforming them into a sequence of tokens. Subsequently, we reframe the challenge of predicting the future into predicting the next token in the sequence. This approach has been widely employed in recent years to train large language models, and it is recognized for its effectiveness in enhancing model performance through the scaling of model size and data. It is possible to generate samples within the latent space of the world model through autoregressive generation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second component is a multi-task video diffusion decoder that is able to perform high-resolution video rendering as well as temporal upsampling to generate smooth videos from the information autoregressively generated by the world model. Similarly to large language models, video diffusion models have demonstrated a clear correlation between scale of training and overall performance, making both components of GAIA-1 suitable for effective compound scaling.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

GAIA-1 is designed to be multimodal, allowing video, text and action to be used as prompts to generate diverse and realistic driving scenarios, as demonstrated in Figure 1. By training it on a large corpus of real-world UK urban driving data, GAIA-1 learns to understand and disentangle important concepts such as static and dynamic elements, including cars, buses, pedestrians, cyclists, road layouts, buildings, and even traffic lights. Further, it provides fine-grained control over both ego-vehicle behavior and other scene features through action and language conditioning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

GAIA-1 demonstrates the ability to manifest the generative rules of the real world. Emerging properties such as learning high-level structures, generalization, creativity, and contextual awareness indicate that the model can comprehend and reproduce the rules and behaviors of the world. Moreover, GAIA-1 exhibits understanding of 3D geometry, for example, by effectively capturing the intricate interplay of pitch and roll induced by road irregularities such as speed bumps. It showcases reactive behaviors of other agents demonstrating the ability to understand causality in decision making of road users. Surprisingly, it shows the capability to successfully extrapolate beyond the training data, for example to driving outside of the boundaries of the road. See Section 7 for a comprehensive list of examples.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The power of GAIA-1's learned representations to predict future events, paired with control over both ego-vehicle dynamics and scene elements, is an exciting advance that paves the way for improving embodied intelligence and providing synthetic data to accelerate training and validation. World models, such as GAIA-1, are the basis for the ability to predict what might happen next, which is fundamentally important for decision-making in autonomous driving.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model", "weight": 1.0} -->

In this section we describe the model architecture of the trainable components of GAIA-1. The general architecture is presented in Figure 2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Encoding Video, Text and Action", "weight": 1.0} -->

GAIA-1 can leverage three different input modalities (video, text, action), which are encoded into a shared $d$-dimensional space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Image tokens", "weight": 1.0} -->

Each image frame of a video is represented as discrete tokens. To achieve this, we use a pre-trained image tokenizer for discretization (for details about the pre-training see Section 2.2). Formally, let us consider a sequence of $T$ images $(\mathbf{x}_{1},\ldots,\mathbf{x}_{T})$, where each image $\mathbf{x}_{t}$ in this sequence is discretized into $n = 576$ discrete tokens using the pre-trained image tokenizer. We obtain a sequence denoted as $(\mathbf{z}_{1},\ldots,\mathbf{z}_{T})$, where each $\mathbf{z}_{t} = {(z_{t,1},\ldots,z_{t,n})} \in {\mathbb{R}}^{n}$ corresponds to $n = {\frac{H}{D} \times \frac{W}{D}}$ discrete tokens.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Image tokens", "weight": 1.0} -->

Here, $H$ and $W$ represent the height and width of the input image, while $D$ denotes the downsampling factor of the image tokenizer. These discrete tokens are then mapped to a $d$-dimensional space via an embedding layer that is trained alongside the world model.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Text tokens", "weight": 1.0} -->

At each time step $t$, we incorporate information from both text and action. Textual input is encoded using the pre-trained T5-large model, resulting in $m = 32$ text tokens per time step. These tokens are mapped to a $d$-dimensional space through a linear layer that is trained in conjunction with the world model. This process yields a text representation denoted as $\mathbf{c}_{t} = {(\mathbf{c}_{t,1},\ldots,\mathbf{c}_{t,m})} \in {\mathbb{R}}^{m \times d}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Action tokens", "weight": 1.0} -->

For actions, we consider $l = 2$ scalar values (representing speed and curvature). Each scalar is independently mapped to the $d$-dimensional space via a linear layer that is trained with the world model. Consequently, the action at time step $t$ is represented as $\mathbf{a}_{t} = {(\mathbf{a}_{t,1},\ldots,\mathbf{a}_{t,l})} \in {\mathbb{R}}^{l \times d}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Action tokens", "weight": 1.0} -->

For each time step, the input tokens are interleaved in the following order: text - image - action. The final input of the world model is therefore $(\mathbf{c}_{1},\mathbf{z}_{1},\mathbf{a}_{1},\ldots,\mathbf{c}_{T},\mathbf{z}_{T},\mathbf{a}_{T})$. To encode the position of the input tokens, we use a factorized spatio-temporal positional embedding. 1) A learnable temporal embedding is shared across all the tokens of a given time step, i.e. there are $T$ temporal embeddings. 2) A learnable spatial embedding indicates the position of a token within a time step, i.e. there are ${m + n + l} = 610$ spatial embeddings ($m$ text tokens, $n$ image tokens, and $l$ action tokens) of dimension $d = 4096$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

When modeling discrete input data with a sequence model, there is a trade-off between the sequence length and the vocabulary size. The sequence length refers to the number of discrete tokens that are needed to describe the data. The vocabulary size corresponds to the number of possible values a single token can take. For language, there are two obvious choices for tokens: characters and words. When using character-level tokens, the input data has a longer sequence length, and each individual token belongs to a smaller vocabulary, but conveys little meaning. When using word-level tokens, the input data has a shorter sequence length, and each token contains a lot of semantics but the vocabulary is extremely large. Most language models use byte-pair encoding (or equivalent) as a trade-off between character-level and word-level tokenization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

Likewise for video, we would like to reduce the sequence length of the input, while possibly making the vocabulary larger, but with tokens that are more semantically meaningful than raw pixels. We do this with a discrete image autoencoder. There are two objectives we would like to achieve in this first stage: Compress the information from raw pixels to make the sequence modeling problem tractable. Images contain a lot of redundant and noisy information. We would like to reduce the sequence length needed to describe the input data.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

Guide the compression towards meaningful representations, such as semantics, instead of high-frequency signals. The resulting input space for the world model will be simpler to compose, and less dominated by high-frequency signals that can considerably slow down the learning process.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

We reduce the sequence length of the input data by downsampling each input image by a factor $D = 16$ in both height and width. Each image $\mathbf{x}_{t}$ of size $H \times W$ is described by $n = {\frac{H}{D} \times \frac{W}{D}}$ tokens with a vocabulary size $K$. Inspired, we guide the compression towards meaningful representations by regressing to the latent features of a pre-trained DINO model, a self-supervised image model that is known to contain semantic information. See Figure 3 for a qualitative example.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

The discrete autoencoder is a fully convolutional 2D U-Net. The encoder $E_{\theta}$ quantizes the image features using nearest neighbor look-up from a learnable embedding table, resulting in image tokens $\mathbf{z}_{t} = {E_{\theta}{(\mathbf{x}_{t})}}$. Note that the decoder is only used to train the image autoencoder, solely the discrete encoder $E_{\theta}$ is part of the final GAIA-1 model. Due to the decoder being trained on single images it lacks temporal consistency when decoding to a video. For this reason we also train a video decoder that is described in Section 2.4.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

The training losses for the image autoencoder are the following: Image reconstruction loss. The image reconstruction loss is a weighted sum of $L_{1}$, $L_{2}$, perceptual loss $L_{\text{perceptual}}$, and GAN loss $L_{\text{GAN}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

Quantization loss. To update the embedding vectors, we use the embedding loss and the commitment loss. We adopted the linear projection of the embedding and $L_{2}$ normalization from as we found this helped increase vocabulary usage.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

Inductive bias loss. The quantized image features are encouraged to match the image features of a pre-trained DINO model with a cosine similarity loss. Distilling the information from DINO into the learned tokens is important as it allows them to benefit from the inductive biases of this model.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

(b) Base VQ-GAN tokens Figure 3: Increasing semantic content of image tokens through DINO distillation. Visualization shows the top 3 PCA components of token embeddings mapped to RGB values. DINO-distilled tokens corresponding to a semantic class (e.g. vehicle, road, or sky) have similar embeddings.

<!-- chunk {"id": "body-0028", "role": "body", "section": "World Model", "weight": 1.0} -->

As described in Section 2.1 the input of the world model is $(\mathbf{c}_{1},\mathbf{z}_{1},\mathbf{a}_{1},\ldots,\mathbf{c}_{T},\mathbf{z}_{T},\mathbf{a}_{T})$. The world model is an autoregressive transformer network that models the sequence input. Its training objective is to predict the next image token in the sequence conditioned on all past tokens, using causal masking in the attention matrix of the transformer blocks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "World Model", "weight": 1.0} -->

We randomly dropout conditioning tokens during training so that the world model can do (i) unconditional generation, (ii) action-conditioned generation, and (iii) text-conditioned generation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "World Model", "weight": 1.0} -->

To further reduce the sequence length of our world model we temporally subsample videos from 25Hz to 6.25Hz. This allows the world model to reason over longer periods without leading to intractable sequence lengths. To recover video predictions at full frame rate we perform temporal super-resolution using the video decoder described in Section 2.4.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

Following the recent advances in image and video generation we use denoising video diffusion models for the GAIA-1 decoder. A naive approach of independently decoding each frame-tokens to pixel space results in a temporally inconsistent video output. Modeling the problem as denoising a sequence of frames during the diffusion process, where the model can access information across time, greatly improves temporal consistency of the output video.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

We follow and use a 3D U-Net with factorized spatial and temporal attention layers. During training, our video diffusion model is conditioned on the image tokens obtained by discretizing input images with the pre-trained image tokenizer $E_{\theta}$. During inference, the diffusion model is conditioned on the predicted image tokens from the world model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

We train a single model jointly on both image and video generation tasks. Training on videos teaches the decoder to be temporally consistent, while training on images is crucial for the quality of individual frames as it teaches the model to extract information from conditioning image tokens. We disable temporal layers when training on images.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

To train our video diffusion decoder for multiple inference tasks we take inspiration from where we can perform multiple tasks by masking certain frames or the conditioning image tokens. We choose to train a single video diffusion model for all tasks as it has been shown that multi-task training improves performance on individual tasks. The tasks include image generation, video generation, autoregressive decoding, and video interpolation. Each task is sampled equally. For example, for the autoregressive generation task, we provide previously generated past frames as context and conditioning image tokens for frames we want to predict. We include both forward and backward autoregressive tasks. See Figure 4 for examples of each task. We also apply a conditioning dropout by randomly masking out each conditioning image token with probability $p = 0.15$ as it helps the model generalize beyond relying on tokens for information and improves temporal consistency.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

The video decoder is trained on the noise prediction objective. More specifically, we use the $\mathbf{v}$-parameterization as proposed in because it avoided unnatural color shifts and maintained long-term consistency as similarly found. In practice, we use a weighted average of $L_{1}$ and $L_{2}$ losses. The video decoder loss $L_{\text{video}}$ is: $\epsilon_{\theta}$ is the denoising video model. $\epsilon$ is the denoising target, which uses the $\mathbf{v}$-parameterization. $t' \sim {U{}}$ is the sampled discrete diffusion time. $\mathbf{x} = {(\mathbf{x}_{1},\ldots,\mathbf{x}_{T'})}$ is a video sequence of length $T'$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data", "weight": 1.0} -->

Our training dataset consists of 4,700 hours at 25Hz of proprietary driving data collected in London, UK between 2019 and 2023. This corresponds to approximately 420M unique images. During training we balance over a customizable set of features to control the distribution of data (Figure 5). We achieve this by sampling individual data points with weighting inversely proportional to the (binned and precomputed) empirical distribution of a given feature. For a given example we take the joint probability across all features to balance and stochastically decide whether to include or discard that example. We can control the strength of balancing by raising the sampling weight to an exponent, where an exponent of 0 would result in the empirical distribution (no balancing) and an exponent of 1 would result in a uniformly balanced distribution. We used an exponent of 0.5 for all features as a compromise between final balancing achieved and the severity of discarding samples for training efficiency.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data", "weight": 1.0} -->

For the tokenizer we balanced over (latitude, longitude, weather category) to account for geography and visually distinct weather conditions ensuring our tokenizer can adequately represent a diverse range of scenes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data", "weight": 1.0} -->

For the world model and the video diffusion model we balanced over (latitude, longitude, weather category, steering behavior category, speed behavior category), additionally considering speed and steering behaviors to ensure the dynamics of different behaviors are captured and sufficiently modeled by the world model and the temporal decoder.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data", "weight": 1.0} -->

Our validation dataset contains 400 hours of driving data from runs not included in the training set. The runs selected for validation are those that pass through predetermined geofences as well as a selection of randomly selected runs. We further split our validation set into strict geofences in order to analyze only those samples strictly within the validation geofence (i.e., roads never seen during training) and another geofence around our main data collection routes (i.e., roads seen during training) as a way to monitor overfitting and generalization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Training Procedure", "weight": 1.0} -->

In this section, we describe how the three trainable components of GAIA-1 were optimized. We provide details of hyperparameter configurations, hardware used and training times.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

The image tokenizer (0.3B parameters) was trained on images of resolution ${H \times W} = {288 \times 512}$ ($9/16$ ratio). The spatial downsampling of the encoder is $D = 16$, therefore each image is encoded as $n = {18 \times 32} = 576$ discrete tokens with a vocabulary size $K = 8192$. The bit compression is $\frac{288 \times 512 \times 3 \times 8}{18 \times 32 \times 13} \approx 470$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Image Tokenizer", "weight": 1.0} -->

The model was trained for 200k steps in 4 days with a batch size equal to 160, split across 32 A100 80GB GPUs. We used 5k of linear warm-up and 10k of cosine decay to a final learning rate of $1 \times 10^{- 5}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "World Model", "weight": 1.0} -->

The world model (6.5B parameters) was trained on video sequences of size $T = 26$ at $6.25\ {Hz}$, which correspond to 4s-long videos. The text was encoded as $m = 32$ text tokens per time step, and the action as $l = 2$ tokens. The total sequence length of the world model is therefore ${T \times {({m + n + l})}} = 15860$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "World Model", "weight": 1.0} -->

The world model was optimized with AdamW and a learning rate of $1 \times 10^{- 4}$, weight decay $0.1$, beta coefficients $(0.9,0.95)$, norm gradient clipping $1.0$. Training examples were either unconditioned, action-conditioned, or text conditioned. The ratios of these respective conditioning modes were 20%/40%/40%.

<!-- chunk {"id": "body-0045", "role": "body", "section": "World Model", "weight": 1.0} -->

The model was trained for 100k steps in 15 days, with 2.5k of linear warm-up and 97.5k of cosine decay reducing the learning rate by a factor of 10 over the course of training. The batch size was 128 split across 64 A100 80GB GPUs. We used the FlashAttention v2 implementation in the transformer module, as it offered significant advantages in terms of both memory utilization and inference speed. To optimize distributed training, we used the Deepspeed ZeRO-2 training strategy with activation checkpointing.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

The video decoder (2.6B) was trained on sequences of $T' = 7$ images of resolution ${H \times W} = {288 \times 512}$ sampled from the dataset at either $6.25\ {Hz}$, $12.5\ {Hz}$ or $25\ {Hz}$. The training tasks (Figure 4) were sampled with equal probability. We used a cosine $\beta$-noise schedule.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

The video decoder was optimized with AdamW and a learning rate of $5 \times 10^{- 5}$, weight decay $0.01$, beta coefficients $(0.9,0.99)$, norm gradient clipping $1.0$. The model was trained for 300k steps in 15 days, with 2.5k of linear warm-up and 5k of cosine decay to a final learning rate of $1 \times 10^{- 6}$. We used a weighted average of $L_{1}$ and $L_{2}$ losses with weights $\lambda_{L_{1}} = 0.1$ and $\lambda_{L_{2}} = 1.0$. The batch size was 64 split across 32 A100 80GB GPUs. We used an exponential moving average for the parameters with a decay of $0.999$. The training strategy was also Deepspeed ZeRO-2 with activation checkpointing.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Inference", "weight": 1.0} -->

In this section, we describe in more detail the inference procedure of the world model and the video decoder.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Sampling", "weight": 1.0} -->

The world model autoregressively predicts the next image token, conditioned on previous text, image and action tokens. Given the past tokens we perform $n$ forward steps to generate one new image frame. At each step we must sample a token from the predicted logits to select the next token in our sequence. Empirically we observed that maximization-based sampling (i.e. argmax) generates futures that get stuck in a repetitive loop, similarly to language models. Conversely, if we simply sample from the logits, the selected token can come from the unreliable tail of the probability distribution, which throws the model out-of-distribution, see Figure 6.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Sampling", "weight": 1.0} -->

To encourage diversity as well as realism we employ top-k sampling to sample the next image token from the top-k most likely choices. The chosen value of k is a function of the number of tokens that constitute an image frame as well as the pre-learnt codebook (vocabulary) size.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Sampling", "weight": 1.0} -->

Our world model can be used to roll out possible futures given starting context as well as generating futures from scratch without any starting context. For long video generation, if the length of the video exceeds the context length of the world model, we employ a sliding window.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Text-conditioning", "weight": 1.0} -->

The video prediction can be prompted, and thus directed, with text. At training time, we condition our video sequences with text coming from either online narration or offline metadata sources. Because these text sources are imperfect, to improve the alignment between generated futures and the text prompt, we employ classifier-free guidance at inference time. The effect of guidance is to increase text-image alignment by decreasing the diversity of possible samples. More precisely, for each next token to predict, we compute logits conditioned on text as well as logits with no conditioning (unconditioned). At inference, we can then amplify the differences between the unconditioned and the text-conditioned logits with a scale factor to give the final logits used for sampling.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Text-conditioning", "weight": 1.0} -->

By substituting the unconditioned logits with those conditioned on another text prompt, we can perform "negative" prompting. Pushing the logits away from the negative prompt and towards the positive one encourages the future tokens to include the "positive" prompt features while removing the "negative" ones.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Text-conditioning", "weight": 1.0} -->

We found it was important to schedule the scale factor used for guidance over tokens as well as frames. Scheduling over tokens allows some to be sampled with high guidance (hence adhering strongly to the prompt) and others to be sampled with low guidance (hence increasing sample diversity). Scheduling over frames allows for controlling the transition from earlier frames as well as mitigating compounding guidance over subsequent consecutive frames. In Figure 7 we show an example guidance schedule over twelve frames. Typically we used a schedule that sampled tokens with linearly decreasing guidance over tokens and we lowered the guidance over future frames with a cosine decay, with or without an initial plateau. We note that guidance scale and schedule are hyperparameters to be tuned to particular use cases.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Text-conditioning", "weight": 1.0} -->

(a) Guidance scale factor Figure 7: Classifier-free guidance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

To decode a sequence of generated tokens from the world model, we use the following video decoding method: Decode the first $T' = 7$ frames, conditioned on the corresponding $T'$ image tokens.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

Autoregressively decode the next $T' - 2$ frames, using 2 past overlapping frames as image context, and the following $T' - 2$ image tokens.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

Repeat the autoregressive process until the $N$ frames have been generated at $6.25\ {Hz}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

Temporally upsample the $N$ frames from $6.25\ {Hz}$ to $12.5\ {Hz}$ Temporally upsample the ${2N} - 1$ frames from $12.5\ {Hz}$ to $25.0\ {Hz}$ We use the DDIM sampler with $50$ diffusion steps. During autoregressive decoding, we see a trade-off between reflecting token information content in the generated video and temporal consistency. To balance between these two objectives, we calculate a weighted average of the two tasks. where function $\epsilon_{\theta}^{\pi}{(\mathbf{x}^{t'},t',\mathbf{z},\mathbf{m})}$ denoises each frame individually as images and function $\epsilon_{\theta}{(\mathbf{x}^{t'},t',\mathbf{z},\mathbf{m})}$ denoises the sequence of frames jointly as a video. In practice, we simply switch on and off the temporal layers.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

We apply this weighted average randomly for each diffusion step with probability $p = 0.25$ and weight $w = 0.5$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Video Decoder", "weight": 1.0} -->

While exploring different inference approaches for video decoding we found that decoding video frames autoregressively backwards starting from the end of the sequence led to more stable objects and less flickering on the horizon. In our overall video decoding method, we thus decode the last $T'$ frames and autoregressively decodes the remaining frames backward from there.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Scaling", "weight": 1.0} -->

(a) The final performance of the GAIA-1 world model could be predicted with smaller models trained with less than 20× the compute.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Scaling", "weight": 1.0} -->

(b) Training loss curves for world models up to 10,000x smaller. We used an exponential moving average to smooth the training loss curves.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Scaling", "weight": 1.0} -->

The formulation of the world modeling task in GAIA-1 shares a commonality with the approach frequently used in large language models (LLMs). In both instances, the task is streamlined to focus on predicting the next token. Although this approach is adapted for world modeling in GAIA-1 rather than the traditional language tasks seen in LLMs, it is intriguing to observe that scaling laws, analogous to those observed in LLMs, are also applicable to GAIA-1. This suggests the broader applicability of scaling principles in modern AI models across diverse domains, including autonomous driving.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Scaling", "weight": 1.0} -->

To explore scaling laws with GAIA-1, we predicted the final performance of the world model using models trained with less than $20 \times$ the compute. We evaluated those models on a held-out geofenced validation set by measuring cross-entropy. A power-law of the form ${f{(x)}} = {c + {({x/a})}^{b}}$ was then fitted to the data points. In Figure 8(a) we can see that the final cross-entropy of GAIA-1 could be predicted with high accuracy.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Scaling", "weight": 1.0} -->

The models used to fit the power-law ranged from 10,000x to 10x smaller models in terms of parameters (0.65M to 650M), as visualized in Figure 8(b). Similarly to, the compute was estimated as a function of the parameter count. If we denote by $C$ the compute and by $N$ the parameter count (excluding embedding layers), the number of floating point operations for a forward-backward pass of a single token is given by $C = {6N}$. To obtain the total amount of compute, this value is multiplied by the number of training tokens.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Scaling", "weight": 1.0} -->

It is worth noting that our extrapolation leads us to the conclusion that there is substantial potential for further improvement through the expansion of both data and computational resources.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Capabilities and Emerging Properties", "weight": 1.0} -->

In this section we showcase the capabilities and emerging properties of GAIA-1 through a series of qualitative examples. The comprehensive list of video examples can be found here. Figure 9 shows the variety of scenarios that can be generated by our model. As evidenced by the examples presented in the rest of this section, GAIA-1 exhibits a level of understanding and summarization of the generative rules of the world through the following emergent properties: Learning high-level structures and scene dynamics: it generates coherent scenes with objects positioned in plausible locations and exhibiting realistic object interactions, such as traffic lights, rules of the road, give ways, etc. This suggests that the model is not just memorizing statistical patterns but is understanding the underlying rules that govern the arrangement and behavior of objects in the world (see Section 7.1).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Capabilities and Emerging Properties", "weight": 1.0} -->

Generalization and creativity: it can generate novel and diverse videos that go beyond specific instances in the training set. It can produce unique combinations of objects, movements, and scenes that were not explicitly present in the training data, demonstrating remarkable extrapolation capabilities. This demonstrates a certain level of generalization and creativity, which suggests an understanding of the underlying generative rules that govern video sequences (see Section 7.2).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Capabilities and Emerging Properties", "weight": 1.0} -->

Contextual awareness: GAIA-1 can capture contextual information and generate videos that reflect this understanding. For example, it can generate coherent actions and responses in videos based on the initial conditions or the context provided. Moreover, GAIA-1 exhibits the understanding of 3D geometry, effectively capturing the intricate interplay of pitch and roll induced by road irregularities (e.g. speed bumps). This contextual awareness suggests that the models are not merely reproducing statistical patterns but are actively processing and summarizing the given information to generate appropriate video sequences (see Section 7.3).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Generation of Long Driving Scenarios", "weight": 1.0} -->

GAIA-1 can generate stable long videos (minutes) entirely from imagination (Figure 10). In order to do this, the model leverages its learned implicit prior distribution of the world to generate fully-imagined realistic driving scenarios, with complex road layouts, buildings, cars, pedestrians, and more. This is a demonstration that GAIA-1 understands the rules that underpin the world we inhabit and its structures and dynamics.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Generation of Multiple Plausible Futures", "weight": 1.0} -->

GAIA-1 has the ability to generate a variety of distinct future scenarios based on a single initial prompt. When presented with a brief video as context, it can generate numerous plausible and diverse outcomes by repeatedly sampling. GAIA-1 accurately models multiple potential future scenarios in response to the video prompt while maintaining consistency with the initial conditions observed in the video. As seen in Figure 11, the world model can reason about (i) dynamic interactions with road users (e.g. giving way or not giving way), (ii) multimodal ego-behaviors (e.g. going straight or turning at a roundabout), and (iii) multimodal dynamic scene (e.g. variable traffic density and types of road users such as pedestrians, cyclists, motorcyclists, vehicles) and static scene (e.g. road layout, buildings, vegetation).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Fine-Grained Control of the Ego-Vehicle Behavior and Driving Scenes", "weight": 1.0} -->

GAIA-1 can generate videos from text prompts only, completely imagining the scene. To demonstrate this we showcase how we can generate driving scenarios from text prompts that guide the model towards specific weather or lighting conditions in Figure 12.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Fine-Grained Control of the Ego-Vehicle Behavior and Driving Scenes", "weight": 1.0} -->

Next, we present compelling examples where the model exhibits fine-grained control over the vehicle dynamics in the video. By leveraging this control, we can prompt the model to generate videos depicting scenarios that lie outside the bounds of the training data. This shows that GAIA-1 is able to disentangle the ego-vehicle dynamics from the surrounding environment and effectively generalize to unfamiliar scenarios. It provides explicit ability to reason about the impact of our actions on the environment (safety), it allows richer understanding of dynamic scenes (intelligence), it unlocks model-based policy learning (planning in the world model), and it enables exploration in closed-loop (by considering the world model as a neural simulator). To showcase this, we make GAIA-1 generate futures where the ego-vehicle steers left or right, deviating from its lane (Figure 13). GAIA-1 would never have seen these incorrect behaviors in the expert driving dataset used to train it, indicating that it can extrapolate driving concepts previously unseen in the training data. We also see realistic reactions of other agents to the ego-vehicle's controlled behavior.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Fine-Grained Control of the Ego-Vehicle Behavior and Driving Scenes", "weight": 1.0} -->

Finally we demonstrate the ability of GAIA-1 to leverage both text and action to fully imagine a driving scenario. In this particular case we prompt the model to generate a bus in front of the ego-vehicle and then we force its actions to overtake the bus (see Figure 1).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Video generative models", "weight": 1.0} -->

Video generative models are neural networks that can generate realistic video samples. They can be grouped in four categories: VAE-based (variational autoencoder, GAN-based (generative adversarial network ), diffusion-based, and autoregressive-based.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Video generative models", "weight": 1.0} -->

Latent-variable video models (VAE-based) try to infer the underlying latent process that generated the videos. One known limitation of those models is that they tend to generate blurry outputs due to limited representational power, inadequate choice of prior distribution, and the optimization of a lower-bound instead of the true likelihood. GAN-based methods produce more realistic videos but are known to suffer from training instability and a lack of generation diversity. Diffusion-based methods have yielded significant enhancements in realism, controllability, and temporal consistency. They can operate either at the pixel level or in the latent space of a pre-trained image tokenizer. Diffusion models are expressive neural networks that can fit complex data distributions, but rely on a long Markov chain of diffusion steps to generate samples. Lastly, autoregressive-based methods are conceptually simple and rely on tractable exact likelihood optimization (fits the entire data distribution). Likewise, they can operate at the pixel level, or in a discrete learned token space. A known limitation is the slow generation speed, but this issue could be alleviated by future research on parallel sampling, reducing the number of latent variables, and improvements in hardware accelerators.

<!-- chunk {"id": "body-0078", "role": "body", "section": "World models", "weight": 1.0} -->

A world model is a predictive model of the future that learns a general representation of the world in order to understand the consequences of its actions. The main use cases are: pure representation learning, planning (look-ahead search), or learning a policy in the world model (neural simulator).

<!-- chunk {"id": "body-0079", "role": "body", "section": "World models", "weight": 1.0} -->

World modeling has been used as a pre-training task to learn a compact and general representation in a self-supervised way. Subsequently, using this representation as a state for traditional reinforcement learning (RL) algorithms significantly accelerated convergence speed. World models can also be utilized for look-ahead search, in order to plan by imagining the outcomes of future actions. They have proven to be highly effective in game environments or board games. Additionally, world models can be a solution to the sample efficiency issues of RL algorithms by acting as a simulator of the environment, although this assumes the world model is an accurate model of the environment.

<!-- chunk {"id": "body-0080", "role": "body", "section": "World models", "weight": 1.0} -->

A recent line of work suggests casting world modeling as a single sequence model, treating states, actions and rewards as simply a stream of data. The advantage of such a perspective is that world models can benefit from scaling properties of high-capacity sequence model architectures applied to large-scale unsupervised training. This is the approach that GAIA-1 takes, leveraging those scaling properties to model complex environments such as real-world driving scenes.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Scaling", "weight": 1.0} -->

Large language models have shown clear benefits in scaling model size and data. In particular, showed predictable relationships between model/data size and loss over multiple orders of magnitude. derived power laws for transformer based language models in order to optimally allocate the compute budget between the model and data size. Those laws were then refined by by adapting the learning rate schedule when changing the dataset size. Another direction of research to improve the training efficiency of language models is data quality. showed that the quality of the training data plays a critical role in the performance of language models in downstream tasks.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Scaling", "weight": 1.0} -->

Transferring the scaling principles from large language models to the visual domain holds the potential for delivering consistent and expected performance improvements. In this work, by casting the problem of world modeling as unsupervised sequence modeling, we have shown that similar scaling trends from language models also applied to world models.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

GAIA-1 is a generative world model for autonomous driving. The world model uses vector-quantized representations to turn the task of future prediction into a next token prediction task, a technique that has been successfully employed in large language models. GAIA-1 has demonstrated its capability to acquire a comprehensive understanding of the environment, distinguishing between various concepts such as cars, trucks, buses, pedestrians, cyclists, road layouts, buildings, and traffic lights --- all through self-supervision. Further, GAIA-1 harnesses the capabilities of video diffusion models to generate realistic driving scenarios, thereby functioning as an advanced neural simulator. GAIA-1 is a multimodal approach that enables the control of the ego-vehicle's actions and other scene attributes through a combination of textual and action-based instructions.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

While our method demonstrated promising results that have the potential to push the boundaries of autonomous driving, it is important to acknowledge current limitations. For instance, the autoregressive generation process, while highly effective, does not yet run at real-time. Nevertheless, it is noteworthy that this process lends itself well to parallelization, allowing for the concurrent generation of multiple samples.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

The significance of GAIA-1 extends beyond its generative capabilities. World models represent a crucial step towards achieving autonomous systems that can understand, predict, and adapt to the complexities of the real world. Furthermore, by incorporating world models into driving models, we can enable them to better understand their own decisions and ultimately generalize to more real-world situations. Lastly, GAIA-1 can also serve as a valuable neural simulator, allowing the generation of unlimited data, including adversarial examples, for training and validating autonomous driving systems.\
