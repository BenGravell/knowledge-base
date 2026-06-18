<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Live Music Models

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a new class of generative models for music called live music models that produce a continuous stream of music in real-time with synchronized user control. We release Magenta RealTime, an open-weights live music model that can be steered using text or audio prompts to control acoustic style. On automatic metrics of music quality, Magenta RealTime outperforms other open-weights music generation models, despite using fewer parameters and offering first-of-its-kind live generation capabilities. We also release Lyria RealTime, an API-based model with extended controls, offering access to our most powerful model with wide prompt coverage. These models demonstrate a new paradigm for AI-assisted music creation that emphasizes human-in-the-loop interaction for live music performance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Music exists in two complementary forms: as static recorded pieces ("music as a noun"), and as live performances collectively experienced in real time ("music as a verb"). This second form of *live* music is particularly tied to the fundamental human experiences of creative flow, embodied expression, and social connection. Despite this, modern generative AI systems for musical audio have had an overwhelming emphasis on offline, turn-based generation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Live music represents a new frontier for generative AI, one with numerous opportunities and technical challenges. In the conventional offline setting, users input control information, wait $L$ seconds (offline *latency*), and receive $T$ seconds of audio. In our proposed live setting, users continuously input control information, receiving $T$ seconds of an uninterrupted audio stream from $T$ seconds of interaction, with $D$ seconds of *delay* between their control inputs and their influence on the audio stream. Placing users in a continuous perception-action loop promotes more active creation, creates higher-bandwidth interaction, fosters personalized expression and emphasize the process as much as the product. However, meeting these rigid synchronization requirements while maintaining high quality audio generation is a challenging task for machine learning models. Some offline music generation systems have a Real Time Factor (RTF) r$\geq 1 \times$, i.e., they generate $T$ seconds of audio with latency $L \leq T$.^22^2RTF is commonly defined as both $L/T$ and $T/L$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we use $T/L$, i.e., higher RTF means faster. However, most are not well-suited for live performance, as they lack other necessary attributes. Specifically, we differentiate *live music models* as those which have all three of the following attributes: *real-time generation* with throughput RTF $\geq 1 \times$, *causal streaming* where audio generates continuously as a function of both user control inputs and past audio output, and *responsive controls* (delay $D$ is low, facilitating live interaction).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Open-weights models are particularly well-suited for live generative music because they can run locally on users' devices. On-device inference has numerous benefits in music, enabling *lower latency* by eliminating network requests, *higher reliability*, facilitating usage in real-world contexts, *privacy* guarantees, and *customization* by artists. Cloud-based APIs address complementary use cases, offering access to models running on specialized hardware that are more powerful than those that would run on edge devices, at the cost of some of the benefits of open-weights models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To allow users to navigate these tradeoffs based on their application goals, we introduce a pair of systems that span both paradigms: Magenta RT (open-weights, on-device) and Lyria RT (API, cloud-based). Both use the same core methodological framework, which centers around codec language modeling (Figure 1). Specifically, we train a language model (LM) to generate audio tokens from SpectroStream, using a method similar to to achieve live streaming.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus our subsequent discussion primarily on Magenta RT, which may be of higher interest to the AI research community for its ability to be finetuned with new controls or explored for transfer learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Magenta RT offers first-of-its-kind live generation among open-weights models. On automatic metrics of music quality, it outperforms existing offline open-weights music generation models like MusicGen (Large) and Stable Audio Open. Moreover, Magenta RT uses $38$% fewer parameters ($750$M) than Stable Audio Open ($1.2$B), and $77$% fewer than MusicGen Large ($3.3$B). Along with our codebase and model weights, we release a set of demos that run in real time on free-tier Colab TPUs (v2-8) and showcase three distinct use cases: live generation, finetuning, and a novel live audio input interaction that we call *audio injection* (Section 4.2).^33^3Audio samples and links to code, weights and demos are provided in the online supplement:\

<!-- chunk {"id": "body-0010", "role": "body", "section": "Method", "weight": 1.0} -->

Magenta RT is a codec language model designed to generate high-fidelity stereo audio in real time based on acoustic style conditioning. To achieve this, we adopt a pipeline-based approach, using an encoder-decoder Transformer to model audio tokens from SpectroStream conditioned on style embeddings from our proposed MusicCoCa (Figure 1). See Appendix A for related work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Audio Tokenization via SpectroStream", "weight": 1.0} -->

Codec language modeling involves the use of a discrete audio codec to convert audio data into language-like *tokens*. A codec is a pair of functions, an encoder and decoder, that convert audio to and from a compressed space with minimal perceivable distortion. More formally, the encoder component Enc is a function mapping raw stereo audio waveforms $\mathbf{a} \in {\mathbb{R}}^{{Tf_{s}} \times 2}$ into sequences of discrete tokens ${\mathbb{V}}_{c}^{{Tf_{k}} \times d_{c}}$, where $T$ is the duration in seconds, $f_{s}$ the audio sampling rate, ${\mathbb{V}}_{c}$ the codec vocabulary, $f_{k}$ the token frame rate, and $d_{c}$ the RVQ depth.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Audio Tokenization via SpectroStream", "weight": 1.0} -->

The decoder module $\text{Dec} \approxeq \text{Enc}^{- 1}$ then performs the approximate inverse operation to reconstruct the waveform given the compressed representation, ensuring that the process is as perceptually lossless as possible.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Audio Tokenization via SpectroStream", "weight": 1.0} -->

Here we adopt the recently proposed SpectroStream codec, a full-band ($f_{s} = 48$kHz) multi-channel neural audio codec based on residual vector quantization (RVQ), with an overall bandwidth of $16$kbps ($f_{k} = 25$Hz, $d_{c} = 64$, ${|{\mathbb{V}}_{c}|} = 1024$). To facilitate live streaming, we reduce the bandwidth to $4$kbps by generating only the first $16$ RVQ levels (coarse and medium from Figure 3), yielding a live throughput target of $400$ tokens per second. See Section C.1 for more details.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Style Embeddings via MusicCoCa", "weight": 1.0} -->

We use a joint audio-text representation as a control mechanism for overall audio style. This is achieved by training a joint audio-text embedding model on music annotated with diverse textual descriptions. The text encapsulates musical characteristics useful for high-level control, which we collectively refer to as *style* (Section 4.1).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Style Embeddings via MusicCoCa", "weight": 1.0} -->

Our embedding model, MusicCoCa, builds upon MuLan and CoCa. It is a contrastive captioner (CoCa) consisting of two embedding towers, mapping each modality to a shared $768$-dimensional space. The audio embedding tower $M_{A}$ is a $12$-layer VisionTransformer (ViT). Its input is a log-mel spectrogram of a $10$s slice of $16$kHz audio ($128$ channels and length $992$; split into patches of size $16 \times 16$). The text embedding tower $M_{T}$ is a $12$-layer Transformer, which operates on tokenized text with a maximum sequence length of $128$ tokens. We use attention pooling to reduce the activations of each tower to a single $768$d embedding, which can be subsequently quantized into $12$ discrete tokens with codebook size ${|{\mathbb{V}}_{m}|} = 1024$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Style Embeddings via MusicCoCa", "weight": 1.0} -->

This tokenized representation (of audio or text) is then used as a conditioning signal in the LM encoder. Variable-length audio of duration $T$ may be embedded by zero padding to a multiple of $10$ seconds and then mean pooling across $\lceil\frac{T}{10}\rceil$ chunks.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Style Embeddings via MusicCoCa", "weight": 1.0} -->

In addition to the two embedding towers, MusicCoCa has a text decoder which can generate audio text captions. In our application this decoder is a shallow 3-layer Transformer which only serves a regularizing purpose. The MusicCoCa optimization objective, based on the CoCa framework, consists of contrastive and generative loss components which we weigh equally. We train the model using the Adafactor optimizer with a learning rate of $1 \times 10^{- 4}$ and $1,000$ warmup steps for a total of $16,000$ steps. The batch size is $1024$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Modeling Framework", "weight": 1.0} -->

Magenta RT operates on audio tokens from a discrete audio codec, following an established practice in audio modeling. Our model autoregressively predicts discrete audio tokens conditioned on both preceding audio and a shared audio-text embedding. This modeling mechanism partly mirrors the MusicLM architecture, itself based on AudioLM. Similarly to MusicLM, we use a Transformer-based architecture for the token prediction model and enable text conditioning by leveraging a joint audio-text embedding model, using the target audio signal at training time, and text inputs at inference time. To facilitate live generation, we propose two high-level changes relative to MusicLM: we replace the hierarchical cascade of multiple LMs with a single LM, using a recent method similar to for efficiency, and we propose a chunk-based autogressive approach to allow for infinite streaming generation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Modeling Framework", "weight": 1.0} -->

More formally, given audio $\mathbf{a}$, our goal is to model the probability $P_{\theta}{({{\text{Enc}{(\mathbf{a})}} \mid {M_{A}{(\mathbf{a})}}})}$ of the corresponding sequence of acoustic tokens given its associated style embedding. Here, Enc denotes the audio codec encoder and $M_{A}$ the MusicCoCa audio encoder. At inference, we sample from the model $\mathbf{e}\prime \sim P_{\theta}{( \cdot \mid \mathbf{c})}$, conditioning on a style embedding $\mathbf{c}$ obtained from an arbitrary mixture of audio and text prompts. Finally, we use the codec decoder to produce output audio, i.e., $\mathbf{a}\prime = \text{Dec}{(\mathbf{e}\prime)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Chunk-based autoregression with coarse context", "weight": 1.0} -->

In the live generation setting, we require our model to generate an infinite and uninterrupted stream of audio with a RTF $\geq 1 \times$. To achieve this, we propose two key techniques: chunk-based autoregression to enable infinite streaming, and the use of coarser RVQ tokens in the audio history.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Chunk-based autoregression with coarse context", "weight": 1.0} -->

In order to generate an infinite stream of audio, at inference time we must be able to predict an audio sequence with a length likely larger than what the model has seen during training. Such a mismatch in sequence length between training and inference is often found to result in unpredictable behavior and degraded performance. Previous work has addressed this issue via sliding attention windows with a relative positional encoding scheme, informing the model about the relative distance between tokens instead of describing their absolute position within the sequence.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Chunk-based autoregression with coarse context", "weight": 1.0} -->

We instead propose *chunk-based autoregression*, where we operate on chunks of length $C = 2$ seconds, and, under a Markov assumption, predict each chunk based on a limited context of $H = 5$ previous chunks ($10$ seconds of history). This has several advantages: it reduces error accumulation and allows for stateless inference, eliminating the need to maintain a generation cache and simplifying model deployment. It also introduces flexibility during sampling, since conditioning is updated between calls without preserving information about controls beyond the context window.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Chunk-based autoregression with coarse context", "weight": 1.0} -->

To achieve RTF $\geq 1 \times$, we also propose to use a *coarse representation of the audio context*. Due to the hierarchical structure of RVQ, lower quantization levels capture the most salient acoustic information. While generating target tokens at the full RVQ depth ($d_{c} = 16$) is crucial to maintaining high fidelity, a lower resolution may be sufficient to represent the audio history. Therefore, we use a coarser representation consisting of the first $4$ RVQ tokens for conditioning on the previous chunks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Chunk-based autoregression with coarse context", "weight": 1.0} -->

More formally, a *chunk* is a contiguous segment of audio tokens representing $C$ seconds of audio. For audio $\mathbf{a}$, we define $\text{Chunk}_{i} \triangleq {\text{Enc}{(\mathbf{a})}_{{Cf_{k}i}:{Cf_{k}{({i + 1})}}}}$, i.e., the span of tokens representing audio between $Ci$ and $C{({i + 1})}$ seconds and including the first $16$ RVQ tokens for each frame. We also define $\text{Coarse}_{i}$ as the first $4$ RVQ tokens over the same span of time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Encoder-Decoder Language Model", "weight": 1.0} -->

To model this distribution, we use an encoder-decoder Transformer LM trained with T5X. We release pre-trained models using the T5 Base and Large configurations.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Encoder", "weight": 1.0} -->

The bidirectional encoder is responsible for processing the acoustic history and style control into an intermediate representation for generation. At chunk $i$, the encoder receives the concatenation of the acoustic history and style tokens $\mathbf{x}_{i} = {\text{Coarse}_{i - H} \oplus \cdots \oplus \text{Coarse}_{i - 1} \oplus \mathbf{c}_{i}}$, with a total length of $1012$ tokens (${4 \cdot C \cdot H \cdot f_{k}} = 1000$ audio + $12$ style tokens) and a vocabulary unified across the codec and quantized style tokens ${\mathbb{V}} = {{\{\text{},\text{}\}} \cup {\mathbb{V}}_{c} \cup {\mathbb{V}}_{m}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Decoder", "weight": 1.0} -->

A key differentiating factor compared to prior work is our imposed constraint of achieving RTF $\geq 1 \times$ generation to enable live interactive applications. Past work such as MusicLM proposes a hierarchical cascade of language models to model tokens efficiently, while MusicGen proposes a delay pattern---neither approach would achieve RTF $\geq 1 \times$ for full bandwidth audio tokens. Instead, based, our decoder comprises two connected Transformer modules. The "temporal" module constructs a temporal context by processing acoustic frames, where RVQ tokens within each frame are embedded and aggregated to yield a single frame-level embedding. The "depth" module then performs autoregressive prediction of the RVQ indices conditioned on the previous temporal context. With this setup, we achieve RTF=$1.8$ on H100 GPU with the T5 Large configuration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

Live music models enable new types of interaction that are best assessed via direct human evaluation and extensive use. As such, many of our design choices were validated through play testing by team members and partner musicians, optimizing for how expressive and engaging the resulting instrument feels. A formalization of this interactive evaluation is presented in our user study in Appendix F.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

We complement this subjective measure with more constrained experiments to examine the effects of our controls and provide comparisons to existing models where possible. We focus these experiments on assessing core capabilities that are common to both live and offline music audio generation models, such as audio quality and adherence to text conditioning (Section 3.2.1), alongside others that are unique to our live music models, such as the ability to generate musical transitions following changes in the conditioning signal (Section 3.2.2). In addition to our evaluation, we also note that, at the time of writing, Magenta RT is ranked as the top open-weights model on the Music Arena leaderboard, based on over 1k real-world user preferences.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training", "weight": 1.0} -->

We pretrain the LM at Base (220M parameters) and Large (770M parameters) size. The dataset comprises around $190,000$ hours of primarily instrumental stock music sourced from various providers. Each training example consists of a $12$-second audio clip randomly sampled from the raw data, structured as $10$-second context tokens and $2$-second target tokens. MusicCoCa tokens are derived from the target audio, of which the first $6$ RVQ levels are used for training. To mitigate the cold-start issue in streaming, we replace early context tokens with variable-length padding tokens.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training", "weight": 1.0} -->

Each model is trained for $1.86$ million steps using the Adafactor optimizer with batch size of $512$ and an inverse square root learning rate schedule with $10,000$ warmup steps. We use TPU-v6e (Trillium) hardware, with $128$ chips for the Base model and $256$ chips for the Large.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sampling parameters", "weight": 1.0} -->

For inference, prompts (text or audio) are embedded and tokenized by MusicCoca using the first $6$ RVQ levels to match training. We sample with classifier-free guidance (CFG), using a temperature of $1.3$, a top-K of $40$, and a CFG weight of $5.0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Audio quality and adherence to fixed text prompts", "weight": 1.0} -->

In this section, we compare Magenta RT to prior work under the offline text-to-music generation setting, where we keep the text conditioning fixed and sequentially generate chunks of audio up to a target length of $47$ seconds. While our model can generate audio of arbitrary length, we choose this duration for a fair comparison between models. Following the evaluation protocol, we then assess the quality and text adherence of the resulting generations using three established metrics, the Fréchet Distance based on OpenL3 embeddings (FD~openl3~), the Kullback--Leibler divergence (KL~passt~) and CLAP~score~.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Audio quality and adherence to fixed text prompts", "weight": 1.0} -->

We show the results in Table. Magenta RT has the lowest FD~openl3~ and KL~passt~ scores, indicating that the generated audio is plausible and closely matches the eval reference audio, including at the level of semantic correspondence. The CLAP~score~ measures how well generated audio adheres to the specified text prompt. On this metric, Magenta RT scores between the other two models. The higher score of Stable Audio Open may be related to the fact that their model uses CLAP embeddings during training, as opposed to our model which trains using MusicCoCa.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Generating musical transitions", "weight": 1.0} -->

Live music models unlock the capability of responding dynamically to user inputs. To test this, we create a *prompt transition* evaluation. We pick pairs of text prompts and task the model with creating musical transitions between them. We linearly interpolate between MusicCoCa text embeddings of the start and end prompt over $60$ seconds ($6$ steps, $10$ seconds$/$step), and use this as style conditioning. We then measure cosine similarity between the audio embedding of the outputs and the conditioning embedding at that time. We perform transitions for $128$ prompt pairs (Appendix G).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Generating musical transitions", "weight": 1.0} -->

As seen in Figure Magenta RT outputs maintain strong similarity to the target embedding throughout the transition (right panel), and effectively transitions from the initial to final prompt (left panel). The audio context conditioning lead to smooth transitions that blend styles by preserving elements of the initial prompts. While this leads to lower similarity at end of transition and a slight dip in mid-transition similarity, it also lets the music continuously evolve in a smooth and coherent way, and makes the time history of prompts an important and expressive part of performance.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Style Conditioning via Text and Audio", "weight": 1.0} -->

During inference, we can create a target conditioning vector $\mathbf{c}$ by computing a weighted average of the MusicCoCa embeddings corresponding to $N$ control prompts, provided as either text or audio $\mathbf{c} = {\sum_{i = 1}^{N}{{w_{i}M{(\mathbf{c}_{\mathbf{i}})}}/{\sum_{i}w_{i}}}}$, where $w_{i}$ controls the weight of each prompt. One advantage of using MusicCoCa embeddings instead of attending to text captions is the ability to perform embedding arithmetic to blend styles---e.g., a weighted sum of embed$($"techno"$)$ and embed$($"flute"$)$ gives a good approximation of embed$($"techno flute"$)$---while also controlling the relative influence of each concept.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Style Conditioning via Text and Audio", "weight": 1.0} -->

Beyond this, a shared audio-text embedding space for conditioning allows for the use of audio prompts as a more direct way of achieving a specific musical style or instrumentation that may be difficult to express via text. Since audio prompts more closely match the training setting, where style conditioning is obtained from the target audio itself, this type of prompting is also expected to be more effective. Furthermore, we are able to mix multiple audio prompts to achieve interpolations of different styles, or mix combinations of text and audio prompts. Overall, this type of conditioning offers control over high-level characteristics such as genre, style, instrumentation, mood.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Audio Injection", "weight": 1.0} -->

To allow users to continuously steer generation via a live audio stream, we propose an audio steering mechanism we call audio injection. At each generation step, we mix the user's input audio with the model's output, tokenize the resulting mix, and feed this as the context for the next generation. This is illustrated in Figure. Note, user audio is never played back directly. Rather, the model predicts the continuation of a past context that *includes* the user audio. Depending on the specific audio injected and the target style, the model may "choose" to repeat or transform the user audio, or may be influenced by its features (dynamics, melody, harmony). See Appendix E for details.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduced live music models, a new class of generative systems designed for real-time, continuous music creation with synchronized user control. We presented two such systems: Magenta RealTime, a fully open-weights model, and Lyria RealTime, an API-based model with extended controls. These models facilitate a novel paradigm for AI-assisted music, emphasizing interactive, human-in-the-loop performance that prioritizes the creative process over just the end product. With future work, we aim to further decrease the control latency to unlock new interactive possibilities. Ultra-low latency could enable direct MIDI or audio control, akin to a new class of synthesizer or audio effect. Further, training on multi-stem audio would open the possibility for models to act as musical partners, jamming along with users and providing dynamic live accompaniment.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Contributions and Acknowledgments", "weight": 1.0} -->

Within each Bolded Category of contribution type, contributors are listed alphabetically.
