Zero-Shot Text-to-Image Generation

Topics include Transformers, Image generation, Datasets.

Text-to-image generation has traditionally focused on finding better modeling assumptions for training on a fixed dataset. These assumptions might involve complex architectures, auxiliary losses, or side information such as object part labels or segmentation masks supplied during training. We describe a simple approach for this task based on a transformer that autoregressively models the text and image tokens as a single stream of data. With sufficient data and scale, our approach is competitive with previous domain-specific models when evaluated in a zero-shot fashion.

## Introduction

Modern machine learning approaches to text to image synthesis started with the work of Mansimov et al., who showed that the DRAW Gregor et al. generative model, when extended to condition on image captions, could also generate novel visual scenes. Reed et al. later demonstrated that using a generative adversarial network, rather than a recurrent variational auto-encoder, improved image fidelity. Reed et al. showed that this system could not only generate objects with recognizable properties, but also could zero-shot generalize to held-out categories.

Over the next few years, progress continued using a combination of methods. These include improving the generative model architecture with modifications like multi-scale generators, integrating attention and auxiliary losses, and leveraging additional sources of conditioning information beyond just text.

Separately, Nguyen et al. propose an energy-based framework for conditional image generation that obtained a large improvement in sample quality relative to contemporary methods. Their approach can incorporate pretrained discriminative models, and they show that it is capable of performing text-to-image generation when applied to a captioning model pretrained on MS-COCO. More recently, Cho et al. also propose a method that involves optimizing the input to a pretrained cross-modal masked language model.

By comparison, text-to-image generation has typically been evaluated on relatively small datasets such as MS-COCO and CUB-200. Could dataset size and model size be the limiting factor of current approaches? In this work, we demonstrate that training a 12-billion parameter autoregressive transformer on 250 million image-text pairs collected from the internet results in a flexible, high fidelity generative model of images controllable through natural language.

## Conclusion

We investigate a simple approach for text-to-image generation based on an autoregressive transformer, when it is executed at scale. We find that scale can lead to improved generalization, both in terms of zero-shot performance relative to previous domain-specific approaches, and in terms of the range of capabilities that emerge from a single generative model. Our findings suggest that improving generalization as a function of scale may be a useful driver for progress on this task.
