SoundStream: An End-to-End Neural Audio Codec

Topics include Audio compression, End-to-end learning, Neural networks, Vector quantization, Latent, Generative adversarial network.

Introduces an end-to-end neural audio codec built from a convolutional encoder/decoder and residual vector quantizer, trained with reconstruction and adversarial objectives. The quantizer-dropout mechanism is especially important because it makes one model support multiple bitrates while preserving real-time, low-latency operation.

We present SoundStream, a novel neural audio codec that can efficiently compress speech, music and general audio at bitrates normally targeted by speech-tailored codecs. SoundStream relies on a model architecture composed by a fully convolutional encoder/decoder network and a residual vector quantizer, which are trained jointly end-to-end. Training leverages recent advances in text-to-speech and speech enhancement, which combine adversarial and reconstruction losses to allow the generation of high-quality audio content from quantized embeddings. By training with structured dropout applied to quantizer layers, a single model can operate across variable bitrates from 3kbps to 18kbps, with a negligible quality loss when compared with models trained at fixed bitrates. In addition, the model is amenable to a low latency implementation, which supports streamable inference and runs in real time on a smartphone CPU. In subjective evaluations using audio at 24kHz sampling rate, SoundStream at 3kbps outperforms Opus at 12kbps and approaches EVS at 9.6kbps....

## Introduction

Audio codecs can be partitioned into two broad categories: waveform codecs and parametric codecs. Waveform codecs aim at producing at the decoder side a faithful reconstruction of the input audio samples. In most cases, these codecs rely on transform coding techniques: a (usually invertible) transform is used to map an input time-domain waveform to the time-frequency domain. Then, transform coefficients are quantized and entropy coded. At the decoder side the transform is inverted to reconstruct a time-domain waveform. Often the bit allocation at the encoder is driven by a perceptual model, which determines the quantization process....

Traditional waveform and parametric codecs rely on signal processing pipelines and carefully engineered design choices, which exploit in-domain knowledge on psycho-acoustics and speech synthesis to improve coding efficiency. More recently, machine learning models have been successfully applied in the field of audio compression, demonstrating the additional value brought by data-driven solutions. For example, it is possible to apply them as a post-processing step to improve the quality of existing codecs....

## Conclusions

We propose *SoundStream*, a novel neural audio codec that outperforms state-of-the-art audio codecs over a wide range of bitrates and content types. *SoundStream* consists of an encoder, a residual vector quantizer and a decoder, which are trained end-to-end using a mix of adversarial and reconstruction losses to achieve superior audio quality. The model supports streamable inference and can run in real-time on a single smartphone CPU. When trained with quantizer dropout, a single *SoundStream* model achieves bitrate scalability with a minimal loss in performance when compared with bitrate-specific models....

where $L$ is the number of internal layers, $\mathcal{D}_{k,t}^{(l)}$ ($l \in {\{ 1,\ldots,L\}}$) is the $t$-th output of layer $l$ of discriminator $k$, and $T_{k,l}$ denotes the length of the layer in the time dimension.

Input: y = enc (x) the output of the encoder, vector quantizers Qi for i = 1..Nq
Output: the quantized ŷ

Figure 6: Subjective evaluation results by content type. Error bars denote 95% confidence intervals.

Figure 1: SoundStream @3kbps vs. state-of-the-art codecs.
