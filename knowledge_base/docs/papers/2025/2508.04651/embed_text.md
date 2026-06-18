## Introduction

Music exists in two complementary forms: as static recorded pieces ("music as a noun"), and as live performances collectively experienced in real time ("music as a verb") \[(https://arxiv.org/html/2508.04651v3#bib.bib1)\]. This second form of *live* music is particularly tied to the fundamental human experiences of creative flow \[(https://arxiv.org/html/2508.04651v3#bib.bib2), (https://arxiv.org/html/2508.04651v3#bib.bib3)\], embodied expression \[(https://arxiv.org/html/2508.04651v3#bib.bib4)\], and social connection \[(https://arxiv.org/html/2508.04651v3#bib.bib5)\]. Despite this, modern generative AI systems for musical audio have had an overwhelming emphasis on offline, turn-based generation \[(https://arxiv.org/html/2508.04651v3#bib.bib6), (https://arxiv.org/html/2508.04651v3#bib.bib7), (https://arxiv.org/html/2508.04651v3#bib.bib8), (https://arxiv.org/html/2508.04651v3#bib.bib9), (https://arxiv.org/html/2508.04651v3#bib.bib10), (https://arxiv.org/html/2508.04651v3#bib.bib11), (https://arxiv.org/html/2508.04651v3#bib.bib12), (https://arxiv.org/html/2508.04651v3#bib.bib13), (https://arxiv.org/html/2508.04651v3#bib.bib14), (https://arxiv.org/html/2508.04651v3#bib.bib15)\].

Live music represents a new frontier for generative AI, one with numerous opportunities and technical challenges. In the conventional offline setting, users input control information, wait $L$ seconds (offline *latency*), and receive $T$ seconds of audio. In our proposed live setting, users continuously input control information, receiving $T$ seconds of an uninterrupted audio stream from $T$ seconds of interaction, with $D$ seconds of *delay* between their control inputs and their influence on the audio stream. Placing users in a continuous perception-action loop promotes more active creation, creates higher-bandwidth interaction, fosters personalized expression and emphasize the process as much as the product. However, meeting these rigid synchronization requirements while maintaining high quality audio generation is a challenging task for machine learning models. Some offline music generation systems \[(https://arxiv.org/html/2508.04651v3#bib.bib16)\] have a Real Time Factor (RTF) r$\geq 1 \times$, i.e., they generate $T$ seconds of audio with latency $L \leq T$.^22^2RTF is commonly defined as both $L/T$ and $T/L$. Here we use $T/L$, i.e., higher RTF means faster. However, most are not well-suited for live performance, as they lack other necessary attributes. Specifically, we differentiate *live music models* as those which have all three of the following attributes: *real-time generation* with throughput RTF $\geq 1 \times$, *causal streaming* where audio generates continuously as a function of both user control inputs and past audio output, and *responsive controls* (delay $D$ is low, facilitating live interaction).

Open-weights models are particularly well-suited for live generative music because they can run locally on users' devices. On-device inference has numerous benefits in music \[(https://arxiv.org/html/2508.04651v3#bib.bib17)\], enabling *lower latency* by eliminating network requests, *higher reliability*, facilitating usage in real-world contexts, *privacy* guarantees, and *customization* by artists. Cloud-based APIs address complementary use cases, offering access to models running on specialized hardware that are more powerful than those that would run on edge devices, at the cost of some of the benefits of open-weights models.

To allow users to navigate these tradeoffs based on their application goals, we introduce a pair of systems that span both paradigms: Magenta RT (open-weights, on-device) and Lyria RT (API, cloud-based). Both use the same core methodological framework, which centers around codec language modeling \[(https://arxiv.org/html/2508.04651v3#bib.bib18), (https://arxiv.org/html/2508.04651v3#bib.bib19)\] ([Figure 1](https://arxiv.org/html/2508.04651v3#S1.F1 "In 1 Introduction ‣ Live Music Models")). Specifically, we train a language model (LM) to generate audio tokens from SpectroStream \[(https://arxiv.org/html/2508.04651v3#bib.bib20)\], using a method similar to \[(https://arxiv.org/html/2508.04651v3#bib.bib21), (https://arxiv.org/html/2508.04651v3#bib.bib22)\] to achieve live streaming \[(https://arxiv.org/html/2508.04651v3#bib.bib23)\].

We focus our subsequent discussion primarily on Magenta RT, which may be of higher interest to the AI research community for its ability to be finetuned with new controls \[(https://arxiv.org/html/2508.04651v3#bib.bib24)\] or explored for transfer learning \[(https://arxiv.org/html/2508.04651v3#bib.bib25)\].

Magenta RT offers first-of-its-kind live generation among open-weights models. On automatic metrics of music quality, it outperforms existing offline open-weights music generation models like MusicGen (Large) \[(https://arxiv.org/html/2508.04651v3#bib.bib9)\] and Stable Audio Open \[(https://arxiv.org/html/2508.04651v3#bib.bib14)\]. Moreover, Magenta RT uses $38$% fewer parameters ($750$M) than Stable Audio Open ($1.2$B), and $77$% fewer than MusicGen Large ($3.3$B). Along with our codebase and model weights, we release a set of demos that run in real time on free-tier Colab TPUs (v2-8) and showcase three distinct use cases: live generation, finetuning, and a novel live audio input interaction that we call *audio injection* (Section [4.2](https://arxiv.org/html/2508.04651v3#S4.SS2 "4.2 Audio Injection ‣ 4 Controllable Generation ‣ Live Music Models")).^33^3Audio samples and links to code, weights and demos are provided in the online supplement:\
[https://storage.googleapis.com/live-music-models/index.html](https://storage.googleapis.com/live-music-models/index.html)

Figure 1: Magenta RealTime is a live music model that generates an uninterrupted stream of music and responds continuously to user input. It generates audio in two-second chunks using a pipeline with three components: MusicCoCa, a style embedding model, SpectroStream, an audio codec model, and an encoder-decoder language model. For each chunk, a style embedding is computed via a weighted average of MusicCoCa embeddings of text and audio prompts from the user. Given this style embedding and 10 seconds (5 chunks) of past audio context, the language model decoder generates SpectroStream audio tokens for the new chunk, which is then decoded to audio.

## Method

Magenta RT is a codec language model \[(https://arxiv.org/html/2508.04651v3#bib.bib18), (https://arxiv.org/html/2508.04651v3#bib.bib19)\] designed to generate high-fidelity stereo audio in real time based on acoustic style conditioning. To achieve this, we adopt a pipeline-based approach, using an encoder-decoder Transformer \[(https://arxiv.org/html/2508.04651v3#bib.bib26)\] to model audio tokens from SpectroStream \[(https://arxiv.org/html/2508.04651v3#bib.bib20)\] conditioned on style embeddings from our proposed MusicCoCa ([Figure 1](https://arxiv.org/html/2508.04651v3#S1.F1 "In 1 Introduction ‣ Live Music Models")). See [Appendix A](https://arxiv.org/html/2508.04651v3#A1 "Appendix A Related Work ‣ Live Music Models") for related work.

### Audio Tokenization via SpectroStream

Codec language modeling involves the use of a discrete audio codec to convert audio data into language-like *tokens*. A codec is a pair of functions, an encoder and decoder, that convert audio to and from a compressed space with minimal perceivable distortion. More formally, the encoder component Enc is a function mapping raw stereo audio waveforms $\mathbf{a} \in {\mathbb{R}}^{{Tf_{s}} \times 2}$ into sequences of discrete tokens ${\mathbb{V}}_{c}^{{Tf_{k}} \times d_{c}}$, where $T$ is the duration in seconds, $f_{s}$ the audio sampling rate, ${\mathbb{V}}_{c}$ the codec vocabulary, $f_{k}$ the token frame rate, and $d_{c}$ the RVQ depth. The decoder module $\text{Dec} \approxeq \text{Enc}^{- 1}$ then performs the approximate inverse operation to reconstruct the waveform given the compressed representation, ensuring that the process is as perceptually lossless as possible.

Here we adopt the recently proposed SpectroStream codec \[(https://arxiv.org/html/2508.04651v3#bib.bib20)\], a full-band ($f_{s} = 48$kHz) multi-channel neural audio codec based on residual vector quantization (RVQ) \[(https://arxiv.org/html/2508.04651v3#bib.bib27)\], with an overall bandwidth of $16$kbps ($f_{k} = 25$Hz, $d_{c} = 64$, ${|{\mathbb{V}}_{c}|} = 1024$). To facilitate live streaming, we reduce the bandwidth to $4$kbps by generating only the first $16$ RVQ levels (coarse and medium from [Figure 3](https://arxiv.org/html/2508.04651v3#A4.F3 "In Predicting conditioning tokens ‣ D.2 Self-conditioning ‣ Appendix D Lyria RT and Advanced Controls ‣ Live Music Models")), yielding a live throughput target of $400$ tokens per second. See [Section C.1](https://arxiv.org/html/2508.04651v3#A3.SS1 "C.1 SpectroStream ‣ Appendix C Additional Methodological and Training Details ‣ Live Music Models") for more details.

### Style Embeddings via MusicCoCa

We use a joint audio-text representation as a control mechanism for overall audio style. This is achieved by training a joint audio-text embedding model on music annotated with diverse textual descriptions. The text encapsulates musical characteristics useful for high-level control, which we collectively refer to as *style* (Section [4.1](https://arxiv.org/html/2508.04651v3#S4.SS1 "4.1 Style Conditioning via Text and Audio ‣ 4 Controllable Generation ‣ Live Music Models")).

Our embedding model, MusicCoCa, builds upon MuLan \[(https://arxiv.org/html/2508.04651v3#bib.bib28)\] and CoCa \[(https://arxiv.org/html/2508.04651v3#bib.bib29)\]. It is a contrastive captioner (CoCa) consisting of two embedding towers, mapping each modality to a shared $768$-dimensional space. The audio embedding tower $M_{A}$ is a $12$-layer VisionTransformer (ViT) \[(https://arxiv.org/html/2508.04651v3#bib.bib30)\]. Its input is a log-mel spectrogram of a $10$s slice of $16$kHz audio ($128$ channels and length $992$; split into patches of size $16 \times 16$). The text embedding tower $M_{T}$ is a $12$-layer Transformer, which operates on tokenized text with a maximum sequence length of $128$ tokens. We use attention pooling to reduce the activations of each tower to a single $768$d embedding, which can be subsequently quantized into $12$ discrete tokens with codebook size ${|{\mathbb{V}}_{m}|} = 1024$. This tokenized representation (of audio or text) is then used as a conditioning signal in the LM encoder. Variable-length audio of duration $T$ may be embedded by zero padding to a multiple of $10$ seconds and then mean pooling across $\lceil\frac{T}{10}\rceil$ chunks.

In addition to the two embedding towers, MusicCoCa has a text decoder which can generate audio text captions. In our application this decoder is a shallow 3-layer Transformer which only serves a regularizing purpose. The MusicCoCa optimization objective, based on the CoCa framework \[(https://arxiv.org/html/2508.04651v3#bib.bib29)\], consists of contrastive and generative loss components which we weigh equally. We train the model using the Adafactor optimizer with a learning rate of $1 \times 10^{- 4}$ and $1,000$ warmup steps for a total of $16,000$ steps. The batch size is $1024$.

### Modeling Framework

Magenta RT operates on audio tokens from a discrete audio codec, following an established practice in audio modeling \[(https://arxiv.org/html/2508.04651v3#bib.bib18), (https://arxiv.org/html/2508.04651v3#bib.bib31), (https://arxiv.org/html/2508.04651v3#bib.bib8), (https://arxiv.org/html/2508.04651v3#bib.bib9)\]. Our model autoregressively predicts discrete audio tokens conditioned on both preceding audio and a shared audio-text embedding. This modeling mechanism partly mirrors the MusicLM architecture \[(https://arxiv.org/html/2508.04651v3#bib.bib8)\], itself based on AudioLM \[(https://arxiv.org/html/2508.04651v3#bib.bib31)\]. Similarly to MusicLM, we use a Transformer-based architecture \[(https://arxiv.org/html/2508.04651v3#bib.bib26)\] for the token prediction model and enable text conditioning by leveraging a joint audio-text embedding model, using the target audio signal at training time, and text inputs at inference time. To facilitate live generation, we propose two high-level changes relative to MusicLM: we replace the hierarchical cascade of multiple LMs with a single LM, using a recent method \[(https://arxiv.org/html/2508.04651v3#bib.bib23)\] similar to \[(https://arxiv.org/html/2508.04651v3#bib.bib21), (https://arxiv.org/html/2508.04651v3#bib.bib22)\] for efficiency, and we propose a chunk-based autogressive approach to allow for infinite streaming generation.

More formally, given audio $\mathbf{a}$, our goal is to model the probability $P_{\theta}{({{\text{Enc}{(\mathbf{a})}} \mid {M_{A}{(\mathbf{a})}}})}$ of the corresponding sequence of acoustic tokens given its associated style embedding. Here, Enc denotes the audio codec encoder and $M_{A}$ the MusicCoCa audio encoder. At inference, we sample from the model $\mathbf{e}\prime \sim P_{\theta}{( \cdot \mid \mathbf{c})}$, conditioning on a style embedding $\mathbf{c}$ obtained from an arbitrary mixture of audio and text prompts. Finally, we use the codec decoder to produce output audio, i.e., $\mathbf{a}\prime = \text{Dec}{(\mathbf{e}\prime)}$.

### Chunk-based autoregression with coarse context

In the live generation setting, we require our model to generate an infinite and uninterrupted stream of audio with a RTF $\geq 1 \times$. To achieve this, we propose two key techniques: chunk-based autoregression to enable infinite streaming, and the use of coarser RVQ tokens in the audio history.

In order to generate an infinite stream of audio, at inference time we must be able to predict an audio sequence with a length likely larger than what the model has seen during training. Such a mismatch in sequence length between training and inference is often found to result in unpredictable behavior and degraded performance \[(https://arxiv.org/html/2508.04651v3#bib.bib26), (https://arxiv.org/html/2508.04651v3#bib.bib32)\]. Previous work has addressed this issue via sliding attention windows with a relative positional encoding scheme \[(https://arxiv.org/html/2508.04651v3#bib.bib33), (https://arxiv.org/html/2508.04651v3#bib.bib34)\], informing the model about the relative distance between tokens instead of describing their absolute position within the sequence.

We instead propose *chunk-based autoregression*, where we operate on chunks of length $C = 2$ seconds, and, under a Markov assumption, predict each chunk based on a limited context of $H = 5$ previous chunks ($10$ seconds of history). This has several advantages: it reduces error accumulation and allows for stateless inference, eliminating the need to maintain a generation cache and simplifying model deployment. It also introduces flexibility during sampling, since conditioning is updated between calls without preserving information about controls beyond the context window.

To achieve RTF $\geq 1 \times$, we also propose to use a *coarse representation of the audio context*. Due to the hierarchical structure of RVQ, lower quantization levels capture the most salient acoustic information. While generating target tokens at the full RVQ depth ($d_{c} = 16$) is crucial to maintaining high fidelity, a lower resolution may be sufficient to represent the audio history. Therefore, we use a coarser representation consisting of the first $4$ RVQ tokens for conditioning on the previous chunks.

More formally, a *chunk* is a contiguous segment of audio tokens representing $C$ seconds of audio. For audio $\mathbf{a}$, we define $\text{Chunk}_{i} \triangleq {\text{Enc}{(\mathbf{a})}_{{Cf_{k}i}:{Cf_{k}{({i + 1})}}}}$, i.e., the span of tokens representing audio between $Ci$ and $C{({i + 1})}$ seconds and including the first $16$ RVQ tokens for each frame. We also define $\text{Coarse}_{i}$ as the first $4$ RVQ tokens over the same span of time. Our de facto modeling objective is thus $P_{\theta}{({\text{Chunk}_{i} \mid {\text{Coarse}_{{i - H}:i},\mathbf{c}_{i}}})}$, where $\mathbf{c}_{i} = {\text{Quantize}{({M_{A}{(\mathbf{a})}_{\lfloor\frac{Ci}{10}\rfloor}})}}$ is $12$ tokens representing the most recent quantized MusicCoCa audio embedding for chunk $i$.

### Encoder-Decoder Language Model

To model this distribution, we use an encoder-decoder Transformer \[(https://arxiv.org/html/2508.04651v3#bib.bib26)\] LM trained with T5X \[(https://arxiv.org/html/2508.04651v3#bib.bib35), (https://arxiv.org/html/2508.04651v3#bib.bib36)\]. We release pre-trained models using the T5 \[(https://arxiv.org/html/2508.04651v3#bib.bib35)\] Base and Large configurations.

### Encoder

The bidirectional encoder is responsible for processing the acoustic history and style control into an intermediate representation for generation. At chunk $i$, the encoder receives the concatenation of the acoustic history and style tokens $\mathbf{x}_{i} = {\text{Coarse}_{i - H} \oplus \cdots \oplus \text{Coarse}_{i - 1} \oplus \mathbf{c}_{i}}$, with a total length of $1012$ tokens (${4 \cdot C \cdot H \cdot f_{k}} = 1000$ audio + $12$ style tokens) and a vocabulary unified across the codec and quantized style tokens ${\mathbb{V}} = {{\{\text{},\text{}\}} \cup {\mathbb{V}}_{c} \cup {\mathbb{V}}_{m}}$.

### Decoder

A key differentiating factor compared to prior work is our imposed constraint of achieving RTF $\geq 1 \times$ generation to enable live interactive applications. Past work such as MusicLM \[(https://arxiv.org/html/2508.04651v3#bib.bib8)\] proposes a hierarchical cascade of language models to model tokens efficiently, while MusicGen \[(https://arxiv.org/html/2508.04651v3#bib.bib9)\] proposes a delay pattern---neither approach would achieve RTF $\geq 1 \times$ for full bandwidth audio tokens. Instead, based on \[(https://arxiv.org/html/2508.04651v3#bib.bib23)\], our decoder comprises two connected Transformer modules. The "temporal" module constructs a temporal context by processing acoustic frames, where RVQ tokens within each frame are embedded and aggregated to yield a single frame-level embedding. The "depth" module then performs autoregressive prediction of the RVQ indices conditioned on the previous temporal context. With this setup, we achieve RTF=$1.8$ on H100 GPU with the T5 Large configuration.

## Experiments

Live music models enable new types of interaction that are best assessed via direct human evaluation and extensive use. As such, many of our design choices were validated through play testing by team members and partner musicians, optimizing for how expressive and engaging the resulting instrument feels. A formalization of this interactive evaluation is presented in our user study in Appendix [F](https://arxiv.org/html/2508.04651v3#A6 "Appendix F User Study ‣ Live Music Models").

We complement this subjective measure with more constrained experiments to examine the effects of our controls and provide comparisons to existing models where possible. We focus these experiments on assessing core capabilities that are common to both live and offline music audio generation models, such as audio quality and adherence to text conditioning (Section [3.2.1](https://arxiv.org/html/2508.04651v3#S3.SS2.SSS1 "3.2.1 Audio quality and adherence to fixed text prompts ‣ 3.2 Results ‣ 3 Experiments ‣ Live Music Models")), alongside others that are unique to our live music models, such as the ability to generate musical transitions following changes in the conditioning signal (Section [3.2.2](https://arxiv.org/html/2508.04651v3#S3.SS2.SSS2 "3.2.2 Generating musical transitions ‣ 3.2 Results ‣ 3 Experiments ‣ Live Music Models")). In addition to our evaluation, we also note that, at the time of writing, Magenta RT is ranked as the top open-weights model on the Music Arena leaderboard \[(https://arxiv.org/html/2508.04651v3#bib.bib37)\], based on over 1k real-world user preferences.

### Experimental Set-up

### Training

We pretrain the LM at Base (220M parameters) and Large (770M parameters) size. The dataset comprises around $190,000$ hours of primarily instrumental stock music sourced from various providers. Each training example consists of a $12$-second audio clip randomly sampled from the raw data, structured as $10$-second context tokens and $2$-second target tokens. MusicCoCa tokens are derived from the target audio, of which the first $6$ RVQ levels are used for training. To mitigate the cold-start issue in streaming, we replace early context tokens with variable-length padding tokens.

Each model is trained for $1.86$ million steps using the Adafactor optimizer with batch size of $512$ and an inverse square root learning rate schedule with $10,000$ warmup steps. We use TPU-v6e (Trillium) hardware, with $128$ chips for the Base model and $256$ chips for the Large.

### Sampling parameters

For inference, prompts (text or audio) are embedded and tokenized by MusicCoca using the first $6$ RVQ levels to match training. We sample with classifier-free guidance (CFG) \[(https://arxiv.org/html/2508.04651v3#bib.bib38), (https://arxiv.org/html/2508.04651v3#bib.bib39), (https://arxiv.org/html/2508.04651v3#bib.bib40)\], using a temperature of $1.3$, a top-K of $40$, and a CFG weight of $5.0$.

### Results

Stable Audio Open

Table 1: Instrumental music generation results on the Song Describer Dataset. We compare to open models, using a fixed length of 47s for all samples, though our models are capable of arbitrary-length generation. For all prior models, we report results from.

### Audio quality and adherence to fixed text prompts

In this section, we compare Magenta RT to prior work under the offline text-to-music generation setting, where we keep the text conditioning fixed and sequentially generate chunks of audio up to a target length of $47$ seconds. While our model can generate audio of arbitrary length, we choose this duration for a fair comparison between models. Following the evaluation protocol in \[(https://arxiv.org/html/2508.04651v3#bib.bib14)\], we then assess the quality and text adherence of the resulting generations using three established metrics, the Fréchet Distance based on OpenL3 embeddings \[(https://arxiv.org/html/2508.04651v3#bib.bib42)\] (FD~openl3~), the Kullback--Leibler divergence (KL~passt~) and CLAP~score~.

We show the results in Table (https://arxiv.org/html/2508.04651v3#S3.T1 "Table 1 ‣ 3.2 Results ‣ 3 Experiments ‣ Live Music Models"). Magenta RT has the lowest FD~openl3~ and KL~passt~ scores, indicating that the generated audio is plausible and closely matches the eval reference audio, including at the level of semantic correspondence \[(https://arxiv.org/html/2508.04651v3#bib.bib14)\]. The CLAP~score~ measures how well generated audio adheres to the specified text prompt. On this metric, Magenta RT scores between the other two models. The higher score of Stable Audio Open may be related to the fact that their model uses CLAP embeddings during training, as opposed to our model which trains using MusicCoCa.

### Generating musical transitions

Figure 2: Prompt transition evaluation. Over 60s, we transition from embeddings of text prompt A to B by stepwise linear interpolation. Left: Cosine similarity compared to the initial (blue) and final (red) text embedding. Right: Cosine similarity to the interpolation between text embeddings provided to the model. In both plots, lines indicate the mean and shaded regions the standard deviation.

Live music models unlock the capability of responding dynamically to user inputs. To test this, we create a *prompt transition* evaluation. We pick pairs of text prompts and task the model with creating musical transitions between them. We linearly interpolate between MusicCoCa text embeddings of the start and end prompt over $60$ seconds ($6$ steps, $10$ seconds$/$step), and use this as style conditioning. We then measure cosine similarity between the audio embedding of the outputs and the conditioning embedding at that time. We perform transitions for $128$ prompt pairs (Appendix [G](https://arxiv.org/html/2508.04651v3#A7 "Appendix G Prompt Transitions ‣ Live Music Models")).

As seen in Figure (https://arxiv.org/html/2508.04651v3#S3.F2 "Figure 2 ‣ 3.2.2 Generating musical transitions ‣ 3.2 Results ‣ 3 Experiments ‣ Live Music Models") Magenta RT outputs maintain strong similarity to the target embedding throughout the transition (right panel), and effectively transitions from the initial to final prompt (left panel). The audio context conditioning lead to smooth transitions that blend styles by preserving elements of the initial prompts. While this leads to lower similarity at end of transition and a slight dip in mid-transition similarity, it also lets the music continuously evolve in a smooth and coherent way, and makes the time history of prompts an important and expressive part of performance.

## Controllable Generation

### Style Conditioning via Text and Audio

During inference, we can create a target conditioning vector $\mathbf{c}$ by computing a weighted average of the MusicCoCa embeddings corresponding to $N$ control prompts, provided as either text or audio $\mathbf{c} = {\sum_{i = 1}^{N}{{w_{i}M{(\mathbf{c}_{\mathbf{i}})}}/{\sum_{i}w_{i}}}}$, where $w_{i}$ controls the weight of each prompt. One advantage of using MusicCoCa embeddings instead of attending to text captions is the ability to perform embedding arithmetic to blend styles---e.g., a weighted sum of embed$($"techno"$)$ and embed$($"flute"$)$ gives a good approximation of embed$($"techno flute"$)$---while also controlling the relative influence of each concept.

Beyond this, a shared audio-text embedding space for conditioning allows for the use of audio prompts as a more direct way of achieving a specific musical style or instrumentation that may be difficult to express via text. Since audio prompts more closely match the training setting, where style conditioning is obtained from the target audio itself, this type of prompting is also expected to be more effective. Furthermore, we are able to mix multiple audio prompts to achieve interpolations of different styles, or mix combinations of text and audio prompts. Overall, this type of conditioning offers control over high-level characteristics such as genre, style, instrumentation, mood.

### Audio Injection

To allow users to continuously steer generation via a live audio stream, we propose an audio steering mechanism we call audio injection. At each generation step, we mix the user's input audio with the model's output, tokenize the resulting mix, and feed this as the context for the next generation. This is illustrated in Figure (https://arxiv.org/html/2508.04651v3#A5.F7 "Figure 7 ‣ Appendix E Audio Injection ‣ Live Music Models"). Note, user audio is never played back directly. Rather, the model predicts the continuation of a past context that *includes* the user audio. Depending on the specific audio injected and the target style, the model may "choose" to repeat or transform the user audio, or may be influenced by its features (dynamics, melody, harmony). See Appendix [E](https://arxiv.org/html/2508.04651v3#A5 "Appendix E Audio Injection ‣ Live Music Models") for details.

## Conclusion

In this work, we introduced live music models, a new class of generative systems designed for real-time, continuous music creation with synchronized user control. We presented two such systems: Magenta RealTime, a fully open-weights model, and Lyria RealTime, an API-based model with extended controls. These models facilitate a novel paradigm for AI-assisted music, emphasizing interactive, human-in-the-loop performance that prioritizes the creative process over just the end product. With future work, we aim to further decrease the control latency to unlock new interactive possibilities. Ultra-low latency could enable direct MIDI or audio control, akin to a new class of synthesizer or audio effect. Further, training on multi-stem audio would open the possibility for models to act as musical partners, jamming along with users and providing dynamic live accompaniment.

## Contributions and Acknowledgments

Within each Bolded Category of contribution type, contributors are listed alphabetically.

### Tech Leads

### Core Contributors

### Contributors

Cheng-Zhi Anna Huang\

### Lyria RealTime API

### Magenta RealTime Release

### Product Management

Myriam Hamed Torres

### Legal

### Program Management

### Executive Sponsors

Aäron van den Oord\
