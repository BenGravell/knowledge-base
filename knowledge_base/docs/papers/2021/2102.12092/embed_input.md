Zero-Shot Text-to-Image Generation

Topics include Transformers, Image generation, Datasets.

Text-to-image generation has traditionally focused on finding better modeling assumptions for training on a fixed dataset. These assumptions might involve complex architectures, auxiliary losses, or side information such as object part labels or segmentation masks supplied during training. We describe a simple approach for this task based on a transformer that autoregressively models the text and image tokens as a single stream of data. With sufficient data and scale, our approach is competitive with previous domain-specific models when evaluated in a zero-shot fashion.

## Introduction

Modern machine learning approaches to text to image synthesis started with the work of Mansimov et al., who showed that the DRAW Gregor et al. generative model, when extended to condition on image captions, could also generate novel visual scenes. Reed et al. later demonstrated that using a generative adversarial network, rather than a recurrent variational auto-encoder, improved image fidelity. Reed et al. showed that this system could not only generate objects with recognizable properties, but also could zero-shot generalize to held-out categories.

Over the next few years, progress continued using a combination of methods. These include improving the generative model architecture with modifications like multi-scale generators, integrating attention and auxiliary losses, and leveraging additional sources of conditioning information beyond just text.

## Conclusion

We investigate a simple approach for text-to-image generation based on an autoregressive transformer, when it is executed at scale. We find that scale can lead to improved generalization, both in terms of zero-shot performance relative to previous domain-specific approaches, and in terms of the range of capabilities that emerge from a single generative model. Our findings suggest that improving generalization as a function of scale may be a useful driver for progress on this task.

### Mixed-Precision Training

The use of $1 \times 1$ convolutions at the end of the encoder and the beginning of the decoder. We found that reducing the receptive field size for the convolutions around the relaxation led to it generalizing better to the true ELB.

Minimizing instances in which we zero out the error buffers (e.g., due to nonfinite values encountered during mixed-precision backpropagation, or when resuming training from a checkpoint).

Figure 1: Comparison of original images (top) and reconstructions from the discrete VAE (bottom). The encoder downsamples the spatial resolution by a factor of 8. While details (e.g., the texture of the cat’s fur, the writing on the storefront, and the thin lines in the illustration) are sometimes lost or distorted, the main features of the image are still typically recognizable. We use a large vocabulary size of 8192 to mitigate the loss of information.
