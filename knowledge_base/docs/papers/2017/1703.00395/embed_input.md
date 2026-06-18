Lossy Image Compression with Compressive Autoencoders

Topics include Autoencoders, Image compression, Joint photographic experts group, Joint photographic experts group 2000.

We propose a new approach to the problem of optimizing autoencoders for lossy image compression. New media formats, changing hardware technology, as well as diverse requirements and content types create a need for compression algorithms which are more flexible than existing codecs. Autoencoders have the potential to address this need, but are difficult to optimize directly due to the inherent non-differentiabilty of the compression loss. We here show that minimal changes to the loss are sufficient to train deep autoencoders competitive with JPEG 2000 and outperforming recently proposed approaches based on RNNs. Our network is furthermore computationally efficient thanks to a sub-pixel architecture, which makes it suitable for high-resolution images. This is in contrast to previous work on autoencoders for compression using coarser approximations, shallower architectures, computationally expensive methods, or focusing on small images.

## Introduction

Advances in training of neural networks have helped to improve performance in a number of domains, but neural networks have yet to surpass existing codecs in lossy image compression. Promising first results have recently been achieved using autoencoders -- in particular on small images -- and neural networks are already achieving state-of-the-art results in lossless image compression.

Using this approach, we achieve performance similar to or better than JPEG 2000 when evaluated for perceptual quality. Unlike JPEG 2000, however, our framework can be optimized for specific content (e.g., thumbnails or non-natural images), arbitrary metrics, and is readily generalizable to other forms of media. Notably, we achieve this performance using efficient neural network architectures which would allow near real-time decoding of large images even on low-powered consumer devices.

## Discussion

We have introduced a simple but effective way of dealing with non-differentiability in training autoencoders for lossy compression. Together with an incremental training strategy, this enabled us to achieve better performance than JPEG 2000 in terms of SSIM and MOS scores. Notably, this performance was achieved using an efficient convolutional architecture, combined with simple rounding-based quantization and a simple entropy coding scheme. Existing codecs often benefit from hardware support, allowing them to run at low energy costs.

While other trained algorithms have been shown to provide similar results as JPEG 2000, to our knowledge this is the first time that an end-to-end trained architecture has been demonstrated to achieve this level of performance on high-resolution images. An end-to-end trained autoencoder has the advantage that it can be optimized for arbitrary metrics. Unfortunately, research on perceptually relevant metrics suitable for optimization is still in its infancy.
