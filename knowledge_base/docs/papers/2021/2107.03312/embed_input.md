<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SoundStream: An End-to-End Neural Audio Codec

Topics include Audio compression, End-to-end learning, Neural networks, Vector quantization, Latent, Generative adversarial network.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces an end-to-end neural audio codec built from a convolutional encoder/decoder and residual vector quantizer, trained with reconstruction and adversarial objectives. The quantizer-dropout mechanism is especially important because it makes one model support multiple bitrates while preserving real-time, low-latency operation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present SoundStream, a novel neural audio codec that can efficiently compress speech, music and general audio at bitrates normally targeted by speech-tailored codecs. SoundStream relies on a model architecture composed by a fully convolutional encoder/decoder network and a residual vector quantizer, which are trained jointly end-to-end. Training leverages recent advances in text-to-speech and speech enhancement, which combine adversarial and reconstruction losses to allow the generation of high-quality audio content from quantized embeddings. By training with structured dropout applied to quantizer layers, a single model can operate across variable bitrates from 3kbps to 18kbps, with a negligible quality loss when compared with models trained at fixed bitrates. In addition, the model is amenable to a low latency implementation, which supports streamable inference and runs in real time on a smartphone CPU. In subjective evaluations using audio at 24kHz sampling rate, SoundStream at 3kbps outperforms Opus at 12kbps and approaches EVS at 9.6kbps.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Moreover, we are able to perform joint compression and enhancement either at the encoder or at the decoder side with no additional latency, which we demonstrate through background noise suppression for speech.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Audio codecs can be partitioned into two broad categories: waveform codecs and parametric codecs. Waveform codecs aim at producing at the decoder side a faithful reconstruction of the input audio samples. In most cases, these codecs rely on transform coding techniques: a (usually invertible) transform is used to map an input time-domain waveform to the time-frequency domain. Then, transform coefficients are quantized and entropy coded. At the decoder side the transform is inverted to reconstruct a time-domain waveform. Often the bit allocation at the encoder is driven by a perceptual model, which determines the quantization process. Generally, waveform codecs make little or no assumptions about the type of audio content and can thus operate on general audio. As a consequence of this, they produce very high-quality audio at medium-to-high bitrates, but they tend to introduce coding artifacts when operating at low bitrates. Parametric codecs aim at overcoming this problem by making specific assumptions about the source audio to be encoded (in most cases, speech) and introducing strong priors in the form of a parametric model that describes the audio synthesis process.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The encoder estimates the parameters of the model, which are then quantized. The decoder generates a time-domain waveform using a synthesis model driven by quantized parameters. Unlike waveform codecs, the goal is not to obtain a faithful reconstruction on a sample-by-sample basis, but rather to generate audio that is perceptually similar to the original.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional waveform and parametric codecs rely on signal processing pipelines and carefully engineered design choices, which exploit in-domain knowledge on psycho-acoustics and speech synthesis to improve coding efficiency. More recently, machine learning models have been successfully applied in the field of audio compression, demonstrating the additional value brought by data-driven solutions. For example, it is possible to apply them as a post-processing step to improve the quality of existing codecs. This can be accomplished either via audio superresolution, i.e., extending the frequency bandwidth, via audio denoising, i.e., removing lossy coding artifacts, or via packet loss concealment.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other solutions adopt ML-based models as an integral part of the audio codec architecture. In these areas, recent advances in text-to-speech (TTS) technology proved to be a key ingredient. For example, WaveNet, a strong generative model originally applied to generate speech from text, was adopted as a decoder in a neural codec. Other neural audio codecs adopt different model architectures, e.g., WaveRNN in LPCNet and WaveGRU in Lyra, all targeting speech at low bitrates.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we propose *SoundStream*, a novel audio codec that can compress speech, music and general audio more efficiently than previous codecs, as illustrated in Figure 1. *SoundStream* leverages state-of-the-art solutions in the field of neural audio synthesis, and introduces a new learnable quantization module, to deliver audio at high perceptual quality, while operating at low-to-medium bitrates. Figure 2 illustrates the high level model architecture of the codec. A fully convolutional encoder receives as input a time-domain waveform and produces a sequence of embeddings at a lower sampling rate, which are quantized by a residual vector quantizer. A fully convolutional decoder receives the quantized embeddings and reconstructs an approximation of the original waveform. The model is trained end-to-end using both reconstruction and adversarial losses. To this end, one (or more) discriminators are trained jointly, with the goal of distinguishing the decoded audio from the original audio and, as a by-product, provide a space where a feature-based reconstruction loss can be computed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both the encoder and the decoder only use causal convolutions, so the overall architectural latency of the model is determined solely by the temporal resampling ratio between the original time-domain waveform and the embeddings.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, this paper makes the following key contributions: We propose *SoundStream*, a neural audio codec in which all the constituent components (encoder, decoder and quantizer) are trained end-to-end with a mix of reconstruction and adversarial losses to achieve superior audio quality.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a new residual vector quantizer, and investigate the rate-distortion-complexity trade-offs implied by its design. In addition, we propose a novel "quantizer dropout" technique for training the residual vector quantizer, which enables a single model to handle different bitrates.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that learning the encoder brings a very significant coding efficiency improvement, with respect to a solution that adopts mel-spectrogram features.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate by means of subjective quality metrics that *SoundStream* outperforms both Opus and EVS over a wide range of bitrates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design our model to support streamable inference, which can operate at low-latency. When deployed on a smartphone, it runs in real-time on a single CPU thread.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a variant of the *SoundStream* codec that performs jointly audio compression and enhancement, without introducing additional latency.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model", "weight": 1.0} -->

We consider a single channel recording $x \in {\mathbb{R}}^{T}$, sampled at $f_{s}$. The *SoundStream* model consists of a sequence of three building blocks, as illustrated in Figure 2: an encoder, which maps $x$ to a sequence of embeddings (see Section III-A), a residual vector quantizer, which replaces each embedding by the sum of vectors from a set of finite codebooks, thus compressing the representation with a target number of bits (see Section III-C), a decoder, which produces a lossy reconstruction $\hat{x} \in {\mathbb{R}}^{T}$ from quantized embeddings (see Section III-B).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model", "weight": 1.0} -->

The model is trained end-to-end together with a discriminator (see Section III-D), using the mix of adversarial and reconstruction losses described in Section III-E. Optionally, a conditioning signal can be added, which determines whether denoising is applied at the encoder or decoder side, as detailed in Section III-F.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Encoder architecture", "weight": 1.0} -->

The encoder architecture is illustrated in Figure 3 and follows the same structure as the streaming SEANet encoder described, but without skip connections. It consists of a 1D convolution layer (with $C_{\text{enc}}$ channels), followed by $B_{\text{enc}}$ convolution blocks. Each of the blocks consists of three residual units, containing dilated convolutions with dilation rates of 1, 3, and 9, respectively, followed by a down-sampling layer in the form of a strided convolution. The number of channels is doubled whenever down-sampling, starting from $C_{\text{enc}}$. A final 1D convolution layer with a kernel of length 3 and a stride of 1 is used to set the dimensionality of the embeddings to $D$. To guarantee real-time inference, all convolutions are *causal*. This means that padding is only applied to the past but not the future in both training and offline inference, whereas no padding is used in streaming inference.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Encoder architecture", "weight": 1.0} -->

We use the ELU activation and we do not apply any normalization. The number $B_{\text{enc}}$ of convolution blocks and the corresponding striding sequence determines the temporal resampling ratio between the input waveform and the embeddings. For example, when $B_{\text{enc}} = 4$ and using $$ as strides, one embedding is computed every $= /2 \cdot 4 \cdot 5 \cdot 8 = 320$ input samples. Thus, the encoder outputs ${\text{enc}{(x)}} \in {\mathbb{R}}^{S \times D}$, with $S = T/$/.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Decoder architecture", "weight": 1.0} -->

The decoder architecture follows a similar design, as illustrated in Figure 3. A 1D convolution layer is followed by a sequence of $B_{\text{dec}}$ convolution blocks. The decoder block mirrors the encoder block, and consists of a transposed convolution for up-sampling followed by the same three residual units. We use the same strides as the encoder, but in reverse order, to reconstruct a waveform with the same resolution as the input waveform. The number of channels is halved whenever up-sampling, so that the last decoder block outputs $C_{\text{dec}}$ channels. A final 1D convolution layer with one filter, a kernel of size 7 and stride 1 projects the embeddings back to the waveform domain to produce $\hat{x}$. In Figure 3, the same number of channels in both the encoder and the decoder is controlled by the same parameter, i.e., $C_{\text{enc}} = C_{\text{dec}} = C$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Decoder architecture", "weight": 1.0} -->

We also investigate cases in which $C_{\text{enc}} \neq C_{\text{dec}}$, which results in a computationally lighter encoder and a heavier decoder, or vice-versa (see Section V-D).

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

Input: y = enc (x) the output of the encoder, vector quantizers Qi for i = 1..Nq Output: the quantized ŷ Algorithm 1 Residual Vector Quantization The goal of the quantizer is to compress the output of the encoder $\text{enc}{(x)}$ to a target bitrate $R$, expressed in bits/second (bps). In order to train *SoundStream* in an end-to-end fashion, the quantizer needs to be jointly trained with the encoder and the decoder by backpropagation. The vector quantizer (VQ) proposed in in the context of VQ-VAEs meets this requirement. This vector quantizer learns a codebook of $N$ vectors to encode each $D$-dimensional frame of $\text{enc}{(x)}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

The encoded audio ${\text{enc}{(x)}} \in {\mathbb{R}}^{S \times D}$ is then mapped to a sequence of one-hot vectors of shape $S \times N$, which can be represented using $S{\log_{2}N}$ bits.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

Limitations of Vector Quantization -- As a concrete example, let us consider a codec targeting a bitrate $R = 6000$bps. When using a striding factor $= /320$, each second of audio at sampling rate $f_{s} = 24000$Hz is represented by $S = 75$ frames at the output of the encoder. This corresponds to $r = {6000/75} = 80$ bits allocated to each frame. Using a plain vector quantizer, this requires storing a codebook with $N = 2^{80}$ vectors, which is obviously unfeasible.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

Residual Vector Quantizer -- To address this issue we adopt a Residual Vector Quantizer (a.k.a. multi-stage vector quantizer ), which cascades $N_{q}$ layers of VQ as follows. The unquantized input vector is passed through a first VQ and quantization residuals are computed. The residuals are then iteratively quantized by a sequence of additional $N_{q} - 1$ vector quantizers, as described in Algorithm 1. The total rate budget is uniformly allocated to each VQ, i.e., $r_{i} = {r/N_{q}} = {\log_{2}N}$. For example, when using $N_{q} = 8$, each quantizer uses a codebook of size $N = 2^{r/N_{q}} = 2^{80/8} = 1024$. For a target rate budget $r$, the parameter $N_{q}$ controls the tradeoff between computational complexity and coding efficiency, which we investigate in Section V-D.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

The codebook of each quantizer is trained with exponential moving average updates, following the method proposed in VQ-VAE-2. To improve the usage of the codebooks we use two additional methods. First, instead of using a random initialization for the codebook vectors, we run the k-means algorithm on the first training batch and use the learned centroids as initialization. This allows the codebook to be close to the distribution of its inputs and improves its usage. Second, as proposed, when a codebook vector has not been assigned any input frame for several batches, we replace it with an input frame randomly sampled within the current batch. More precisely, we track the exponential moving average of the assignments to each vector (with a decay factor of $0.99$) and replace the vectors of which this statistic falls below $2$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

Enabling bitrate scalability with quantizer dropout -- Residual vector quantization provides a convenient framework for controlling the bitrate. For a fixed size $N$ of each codebook, the number of VQ layers $N_{q}$ determines the bitrate. Since the vector quantizers are trained jointly with the encoder/decoder, in principle a different *SoundStream* model should be trained for each target bitrate. Instead, having a single bitrate scalable model that can operate at several target bitrates is much more practical, since this reduces the memory footprint needed to store model parameters both at the encoder and decoder side.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

To train such a model, we modify Algorithm 1 in the following way: for each input example, we sample $n_{q}$ uniformly at random in $\lbrack 1;N_{q}\rbrack$ and only use quantizers $Q_{i}$ for $i = {1\ldotsn_{q}}$. This can be seen as a form of structured dropout applied to quantization layers. Consequently, the model is trained to encode and decode audio for all target bitrates corresponding to the range $n_{q} = {1\ldotsN_{q}}$. During inference, the value of $n_{q}$ is selected based on the desired bitrate. Previous models for neural compression have relied on product quantization (wav2vec 2.0 ), or on concatenating the output of several VQ layers. With such approaches, changing the bitrate requires either changing the architecture of the encoder and/or the decoder, as the dimensionality changes, or retraining an appropriate codebook.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Residual Vector Quantizer", "weight": 1.0} -->

A key advantage of our residual vector quantizer is that the dimensionality of the embeddings does not change with the bitrate. Indeed, the additive composition of the outputs of each VQ layer progressively refines the quantized embeddings, while keeping the same shape. Hence, no architectural changes are needed in neither the encoder nor the decoder to accommodate different bitrates. In Section V-C, we show that this method allows one to train a single *SoundStream* model, which matches the performance of models trained specifically for a given bitrate.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Discriminator architecture", "weight": 1.0} -->

To compute the adversarial losses described in Section III-E, we define two different discriminators: i) a wave-based discriminator, which receives as input a single waveform; ii) an STFT-based discriminator, which receives as input the complex-valued STFT of the input waveform, expressed in terms of real and imaginary parts. Since both discriminators are fully convolutional, the number of logits in the output is proportional to the length of the input audio.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Discriminator architecture", "weight": 1.0} -->

For the wave-based discriminator, we use the same multi-resolution convolutional discriminator proposed in and adopted. Three structurally identical models are applied to the input audio at different resolutions: original, 2-times down-sampled, and 4-times down-sampled. Each single-scale discriminator consists of an initial plain convolution followed by four grouped convolutions, each of which has a group size of 4, a down-sampling factor of 4, and a channel multiplier of 4 up to a maximum of 1024 output channels. They are followed by two more plain convolution layers to produce the final output, i.e., the logits.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Discriminator architecture", "weight": 1.0} -->

The STFT-based discriminator is illustrated in Figure 4 and operates on a single scale, computing the STFT with a window length of $W = 1024$ samples and a hop length of $H = 256$ samples. A 2D-convolution (with kernel size $7 \times 7$ and 32 channels) is followed by a sequence of residual blocks. Each block starts with a $3 \times 3$ convolution, followed by a $3 \times 4$ or a $4 \times 4$ convolution, with strides equal to $$ or $$, where $(s_{t},s_{f})$ indicates the down-sampling factor along the time axis and the frequency axis. We alternate between $$ and $$ strides, for a total of 6 residual blocks. The number of channels is progressively increased with the depth of the network.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Discriminator architecture", "weight": 1.0} -->

At the output of the last residual block, the activations have shape ${{T/{({H \cdot 2^{3}})}} \times F}/2^{6}$, where $T$ is the number of samples in the time domain and $F = {W/2}$ is the number of frequency bins. The last layer aggregates the logits across the (down-sampled) frequency bins with a fully connected layer (implemented as a ${1 \times F}/2^{6}$ convolution), to obtain a 1-dimensional signal in the (down-sampled) time domain.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Training objective", "weight": 1.0} -->

Let $\mathcal{G}{(x)} = \text{dec}{(Q{(\text{enc}{(x)})}}$ denote the *SoundStream* generator, which processes the input waveform $x$ through the encoder, the quantizer and the decoder, and $\hat{x} = {\mathcal{G}{(x)}}$ be the decoded waveform. We train *SoundStream* with a mix of losses to achieve both signal reconstruction fidelity and perceptual quality, following the principles of the perception-distortion trade-off discussed.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Training objective", "weight": 1.0} -->

The adversarial loss is used to promote perceptual quality and it is defined as a hinge loss over the logits of the discriminator, averaged over multiple discriminators and over time. More formally, let $k \in {\{ 0,\ldots,K\}}$ index over the individual discriminators, where $k = 0$ denotes the STFT-based discriminator and $k \in {\{ 1,\ldots,K\}}$ the different resolutions of the waveform-based discriminator ($K = 3$ in our case). Let $T_{k}$ denote the number of logits at the output of the $k$-th discriminator along the time dimension.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-E Training objective", "weight": 1.0} -->

The discriminator is trained to classify original vs. decoded audio, by minimizing while the adversarial loss for the generator is To promote fidelity of the decoded signal $\hat{x}$ with respect to the original $x$ we adopt two additional losses: i) a "feature" loss $\mathcal{L}_{\mathcal{G}}^{\text{feat}}$, computed in the feature space defined by the discriminator(s); ii) a multi-scale spectral reconstruction loss $\mathcal{L}_{\mathcal{G}}^{\text{rec}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-E Training objective", "weight": 1.0} -->

More specifically, the feature loss is computed by taking the average absolute difference between the discriminator's internal layer outputs for the generated audio and those for the corresponding target audio. where $L$ is the number of internal layers, $\mathcal{D}_{k,t}^{(l)}$ ($l \in {\{ 1,\ldots,L\}}$) is the $t$-th output of layer $l$ of discriminator $k$, and $T_{k,l}$ denotes the length of the layer in the time dimension.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-E Training objective", "weight": 1.0} -->

The multi-scale spectral reconstruction loss follows the specifications described: where $\mathcal{S}_{t}^{s}{(x)}$ denotes the $t$-th frame of a 64-bin mel-spectrogram computed with window length equal to $s$ and hop length equal to $s/4$. We set $\alpha_{s} = \sqrt{s/2}$ as.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-E Training objective", "weight": 1.0} -->

The overall generator loss is a weighted sum of the different loss components: In all our experiments we set $\lambda_{\text{adv}} = 1$, $\lambda_{\text{feat}} = 100$ and $\lambda_{\text{rec}} = 1$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-F Joint compression and enhancement", "weight": 1.0} -->

In traditional audio processing pipelines, compression and enhancement are typically performed by different modules. For example, it is possible to apply an audio enhancement algorithm at the transmitter side, before audio is compressed, or at the receiver side, after audio is decoded. In this setup, each processing step contributes to the end-to-end latency, e.g., due to buffering the input audio to the expected frame length determined by the specific algorithm adopted. Conversely, we design *SoundStream* in such a way that compression and enhancement can be carried out jointly by the same model, without increasing the overall latency.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-F Joint compression and enhancement", "weight": 1.0} -->

The nature of the enhancement can be determined by the choice of the training data. As a concrete example, in this paper we show that it is possible to combine compression with background noise suppression. More specifically, we train a model in such a way that one can flexibly enable or disable denoising at inference time, by feeding a conditioning signal that represents the two modes (denoising enabled or disabled). To this end, we prepare the training data to consist of tuples of the form: $(\text{inputs},\text{targets},\text{denoise})$. When $\text{denoise} = \text{false}$, $\text{targets} = \text{inputs}$; when $\text{denoise} = \text{true}$, targets contain the clean speech component of the corresponding inputs. Hence, the network is trained to reconstruct noisy speech if the conditioning signal is disabled, and to produce a clean version of the noisy input if it is enabled. Note that when inputs consist of clean audio (speech or music), $\text{targets} = \text{inputs}$ and denoise can be either true or false.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-F Joint compression and enhancement", "weight": 1.0} -->

This is done to prevent *SoundStream* from adversely affecting clean audio when denoising is enabled.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-F Joint compression and enhancement", "weight": 1.0} -->

To process the conditioning signal, we use Feature-wise Linear Modulation (FiLM) layers in between residual units, which take network features as inputs and transform them as where $a_{n,c}$ is the $n^{th}$ activation in the $c^{th}$ channel. The coefficients $\gamma_{n,c}$ and $\beta_{n,c}$ are computed by a linear layer that takes as input a (potentially time-varying) two-dimensional one-hot encoding that determines the denoising mode. This allows one to adjust the level of denoising over time.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-F Joint compression and enhancement", "weight": 1.0} -->

In principle, FiLM layers can be used anywhere throughout the encoder and decoder architecture. However, in our preliminary experiments, we found that applying conditioning at the bottleneck either at the encoder or at the decoder side (as illustrated in Figure 3) was effective and no further improvements were observed by applying FiLM layers at different depths. In Section V-E, we quantify the impact of enabling denoising at either the encoder or decoder side both in terms of audio quality and bitrate.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

We train SoundStream on three types of audio content: clean speech, noisy speech and music, all at $24$kHz sampling rate. For clean speech, we use the LibriTTS dataset. For noisy speech, we synthesize samples by mixing speech from LibriTTS with noise from Freesound. We apply peak normalization to randomly selected crops of 3 seconds and adjust the mixing gain of the noise component sampling uniformly in the interval $\lbrack{- {30\text{dB}}},{0\text{dB}}\rbrack$. For music, we use the MagnaTagATune dataset. We evaluate our models on disjoint test splits of the datasets above. In addition, we collected a real-world dataset, which contains both near-field and far-field (reverberant) speech, with background noise in some of the examples. Unless stated otherwise, objective and subjective metrics are computed on a set of 200 audio clips 2-4 seconds long, with 50 samples from each of the four datasets listed above (i.e., clean speech, noisy speech, music, noisy/reverberant speech).

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Evaluation metrics", "weight": 1.0} -->

To evaluate *SoundStream*, we perform subjective evaluations by human raters. We have chosen a crowd-sourced methodology inspired by MUSHRA, with a hidden reference but no lowpass-filtered anchor. Each of the 200 samples of the evaluation dataset, which include clean, noisy and reverberant speech, as well as music, was rated 20 times. The raters were required to be native English speakers and be using headphones. Additionally, to avoid noisy data, a post-screening was put in place to exclude ratings by listeners who rated the reference below 90 more than 20% of the time or rated non-reference samples above 90 more than 50% of the time.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Evaluation metrics", "weight": 1.0} -->

For development and hyperparameter selection, we rely on computational, objective metrics. Numerous metrics have been developed in the past for assessing the perceived similarity between a reference and a processed audio signal. The ITU-T standards PESQ and its replacement POLQA are commonly used metrics. However, both are inconvenient to use owing to licensing restrictions. We choose the freely available and recently open-sourced ViSQOL metric, which has previously shown comparable performance to POLQA. In early experiments, we found this metric to be strongly correlated with subjective evaluations. We thus use it for model selection and ablation studies.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Baselines", "weight": 1.0} -->

Opus is a versatile speech and audio codec supporting signal bandwidths from 4 kHz to 24 kHz and bitrates from 6 kbps to 510 kbps. Since its standardization by the IETF in 2012 it has been widely deployed for speech communication over the internet. As the audio codec in applications such as Zoom and applications based on WebRTC, such as Microsoft Teams and Google Meet, Opus has hundreds of millions of daily users. Opus is also one of the main audio codecs used in YouTube for streaming. Enhanced Voice Services (EVS) is the latest codec standardized by the 3GPP and was primarily designed for Voice over LTE (VoLTE). Like Opus, it is a versatile codec operating at multiple signal bandwidths, 4 kHz to 20 kHz, and bitrates, 5.9 kbps to 128 kbps. It is replacing AMR-WB and retains full backward operability. In this paper we utilize these two systems as baselines for comparison with the SoundStream codec. For the lowest bitrates, we also compare the performance of the recently presented Lyra codec which is an autoregressive generative codec operating at 3 kbps.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-C Baselines", "weight": 1.0} -->

We provide audio processed by *SoundStream* and baselines at different bitrates on a public webpage^11^1

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Objective quality metrics", "weight": 1.0} -->

We also investigate the rate-quality tradeoff achieved when encoding different content types, as illustrated in Figure 7b. Unsurprisingly, the highest quality is achieved when encoding clean speech. Music represents a more challenging case, due to its inherent diversity of content.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Bitrate scalability", "weight": 1.0} -->

We investigate the bitrate scalability provided by training a single model that can serve different bitrates. To evaluate this aspect, for each bitrate $R$ we consider three *SoundStream* configurations: a) a non-scalable model trained and evaluated at bitrate $R$ (bitrate specific); b) a non-scalable model trained at 18 kbps and evaluated at bitrate $R$ by using only the first $n_{q}$ quantizers during inference (18 kbps - no dropout); c) a scalable model trained with quantizer dropout and evaluated at bitrate $R$ (bitrate scalable). Figure 7c shows the ViSQOL scores for these three scenarios. Remarkably, a model trained specifically at 18 kbps retains good performance when evaluated at lower bitrates, even though the model was not trained in these conditions. Unsurprisingly, the quality drop increases as the bitrate decreases, i.e., when there is a more significant difference between training and inference.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Bitrate scalability", "weight": 1.0} -->

This gap vanishes when using the quantizer dropout strategy described in Section III-C. Surprisingly, the bitrate scalable model seems to marginally outperform bitrate specific models at 9 kbps and 12 kbps. This suggests that quantizer dropout, beyond providing bitrate scalability, may act as a regularizer.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Bitrate scalability", "weight": 1.0} -->

We confirm these results by including the bitrate scalable variant of *SoundStream* in the MUSHRA subjective evaluation (see Figure 5). When operating at $3$kbps, the bitrate scalable variant of *SoundStream* is only slightly worse than the bitrate specific variant. Conversely, both at 6 kbps and 12 kbps it matches the same quality as the bitrate specific variant.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

We carried out several additional experiments to evaluate the impact of some of the design choices applied to *SoundStream*. Unless stated otherwise, all these experiments operate at $6$kbps.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

Advantage of learning the encoder -- We explored the impact of replacing the learnable encoder of *SoundStream* with a fixed mel-filterbank, similarly to Lyra. We learned both the quantizer and the decoder and observed a significant drop in objective quality, with ViSQOL going from 3.96 to 3.33. Note that this is significantly worse than what can be achieved when learning the encoder and halving the bitrate (i.e., ViSQOL equal to 3.76 at $3$kbps). This demonstrates that the additional complexity of having a learnable encoder translates to a very significant improvement in the rate-quality trade-off.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

#Params

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

The main drawback of using a learnable encoder is the computational cost of the neural architecture, which can be significantly higher than computing fixed, non-learnable features such as mel-filterbanks. For *SoundStream* to be competitive with traditional codecs, not only should it provide a better perceptual quality at an equivalent bitrate, but it must also run in real-time on resource-limited hardware. Table I shows how computational efficiency and audio quality are impacted by the number of channels in the encoder $C_{\text{enc}}$ and the decoder $C_{\text{dec}}$. We measured the real-time factor (RTF), defined as the ratio between the temporal length of the input audio and the time needed for encoding/decoding it with *SoundStream*. We profiled these models on a single CPU thread of a Pixel4 smartphone. We observe that the default model ($C_{\text{enc}} = C_{\text{dec}} = 32$) runs in real-time (RTF $> 2.3 \times$).

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

Decreasing the model capacity by setting $C_{\text{enc}} = C_{\text{dec}} = 16$ only marginally affects the reconstruction quality while increasing the real-time factor significantly (RTF $> 7.1 \times$). We also investigated configurations with asymmetric model capacities. Using a smaller encoder, it is possible to achieve a significant speedup without sacrificing quality (ViSQOL drops from 3.96 to 3.94, while the encoder RTF increases to $18.6 \times$). Instead, decreasing the capacity of the decoder has a more significant impact on quality (ViSQOL drops from 3.96 to 3.84). This is aligned with recent findings in the field of neural image compression, which also adopt a lighter encoder and a heavier decoder.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

Vector quantizer depth and codebook size -- The number of bits used to encode a single frame is equal to $N_{q}{\log_{2}N}$, where $N_{q}$ denotes the number of quantizers and $N$ the codebook size. Hence, it is possible to achieve the same target bitrate for different combinations of $N_{q}$ and $N$. Table II shows three configurations, all operating at $6$kbps. As expected, using fewer vector quantizers, each with a larger codebook, achieves the highest coding efficiency at the cost of higher computational complexity. Remarkably, using a sequence of 80 1-bit quantizers leads only to a modest quality degradation. This demonstrates that it is possible to successfully train very deep residual vector quantizers without facing optimization issues. On the other side, as discussed in Section III-C, growing the codebook size can quickly lead to unmanageable memory requirements.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

Thus, the proposed residual vector quantizer offers a practical and effective solution for learning neural codecs operating at high bitrates, as it scales gracefully when using many quantizers, each with a smaller codebook.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Ablation studies", "weight": 1.0} -->

The architectural latency /of the model is defined by the product of the strides, as explained in Section III-A. In our default configuration, $= /2 \cdot 4 \cdot 5 \cdot 8 = 320$ samples, which means that one frame corresponds to 13.3$ms$ of audio at $24$kHz. The bit budget allocated to the residual vector quantizer needs to be adjusted based on the target architectural latency. For example, when operating at $6$kbps, the residual vector quantizer has a budget of 80 bits per frame. If we double the latency, one frame corresponds to 26.6$ms$, so the per-frame budget needs to be increased to 160 bits. Table III compares three configurations, all operating at $6$kbps, where the budget is adjusted by changing the number of quantizers, while keeping the codebook size fixed. We observe that these three configurations are equivalent in terms of audio quality. At the same time, increasing the latency of the model significantly increases the real-time factor, as encoding/decoding of a single frame corresponds to a longer audio sample.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-E Joint compression and enhancement", "weight": 1.0} -->

We evaluate a variant of *SoundStream* that is able to jointly perform compression and background noise suppression, which was trained as described in Section III-F. We consider two configurations, in which the conditioning signal is applied to the embeddings: i) one where the conditioning signal is added at the encoder side, just before quantization; ii) another where it is added at the decoder side. For each configuration, we train models at different bitrates. For evaluation we use $1000$ samples of noisy speech, generated as described in Section IV-A and compute ViSQOL scores when denoising is enabled or disabled, using clean speech references as targets. Figures 8 shows a substantial improvement of quality when denoising is enabled, with no significant difference between denoising either at the encoder or at the decoder. We observe that the proposed model, which is able to flexibly enable or disable denoising at inference time, does not incur a cost in performance, when compared with a model in which denoising is always enabled. This can be seen comparing Figure 8c with Figure 8a and Figure 8b.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-E Joint compression and enhancement", "weight": 1.0} -->

We also investigate whether denoising affects the potential bitrate savings that would be achievable by entropy coding. To evaluate this aspect, we first measured the empirical probability distributions ${{p_{i}^{(q)},i} = {1\ldotsN}},{q = {1\ldotsN_{q}}}$ on 3200 samples of training data. Then, we measured the empirical distribution $r_{i}^{(q)}$ on the $1000$ test samples and computed the cross-entropy ${H{(r,p)}} = {- {\sum_{i,q}{r_{i}^{(q)}{\log_{2}p_{i}^{(q)}}}}}$, as an estimate of the bitrate lower bound needed to encode the test samples. Figure 8 shows that both the encoder-side denoising and fixed denoising offer substantial bitrate savings when compared with decoder-side denoising. Hence, applying denoising before quantization leads to a representation that can be encoded with fewer bits.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-F Joint vs. disjoint compression and enhancement", "weight": 1.0} -->

We compare the proposed model, which is able to perform joint compression and enhancement, with a configuration in which compression is performed by *SoundStream* (with denoising disabled) and enhancement by a dedicated denoising model. For the latter, we adopt SEANet, which features a very similar model architecture, with the notable exception of skip connections between encoder and decoder layers and the absence of quantization. We consider two variants: i) one in which compression is followed by denoising (i.e., denoising is applied at the decoder side); ii) another one in which denoising is followed by compression (i.e., denoising is applied at the encoder side).

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-F Joint vs. disjoint compression and enhancement", "weight": 1.0} -->

We evaluate the different models using the VCTK dataset, which was neither used for training *SoundStream* nor SEANet. The input samples are $2$s clips of noisy speech cropped to reduce periods of silence and resampled at $24$kHz. For each of the four input signal-to-noise ratios ($0$dB, $5$dB, $10$dB and $15$dB), we run inference on $1000$ samples and compute ViSQOL scores. As shown in Table IV, one single model trained for joint compression and enhancement achieves a level of quality that is almost on par with using two disjoint models. Also, the former requires only half of the computational cost and incurs no additional architectural latency, which would be introduced when stacking disjoint models. We also observe that the performance gap decreases as the input SNR increases.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We propose *SoundStream*, a novel neural audio codec that outperforms state-of-the-art audio codecs over a wide range of bitrates and content types. *SoundStream* consists of an encoder, a residual vector quantizer and a decoder, which are trained end-to-end using a mix of adversarial and reconstruction losses to achieve superior audio quality. The model supports streamable inference and can run in real-time on a single smartphone CPU. When trained with quantizer dropout, a single *SoundStream* model achieves bitrate scalability with a minimal loss in performance when compared with bitrate-specific models. In addition, we show that it is possible to combine compression and enhancement in a single model without introducing additional latency.
