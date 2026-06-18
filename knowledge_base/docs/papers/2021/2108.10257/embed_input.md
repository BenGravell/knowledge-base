SwinIR: Image Restoration Using Swin Transformer

Topics include Image restoration, Image super-resolution, Vision transformers, Swin transformer, Residual Swin transformer blocks, Denoising, Compression artifact reduction, Lightweight super-resolution, SwinIR.

SwinIR is a strong transformer baseline for low-level restoration, adapting Swin Transformer blocks to super-resolution, denoising, and JPEG artifact reduction. Its importance is partly architectural and partly practical: it helped make shifted-window transformers a standard choice for restoration tasks.

Image restoration is a long-standing low-level vision problem that aims to restore high-quality images from low-quality images (e.g., downscaled, noisy and compressed images). While state-of-the-art image restoration methods are based on convolutional neural networks, few attempts have been made with Transformers which show impressive performance on high-level vision tasks. In this paper, we propose a strong baseline model SwinIR for image restoration based on the Swin Transformer. SwinIR consists of three parts: shallow feature extraction, deep feature extraction and high-quality image reconstruction. In particular, the deep feature extraction module is composed of several residual Swin Transformer blocks (RSTB), each of which has several Swin Transformer layers together with a residual connection. We conduct experiments on three representative tasks: image super-resolution (including classical, lightweight and real-world image super-resolution), image denoising (including grayscale and color image denoising) and JPEG compression artifact reduction....

## Introduction

Image restoration, such as image super-resolution (SR), image denoising and JPEG compression artifact reduction, aims to reconstruct the high-quality clean image from its low-quality degraded counterpart. Since several revolutionary work, convolutional neural networks (CNN) have become the primary workhorse for image restoration.

Most CNN-based methods focus on elaborate architecture designs such as residual learning and dense connections. Although the performance is significantly improved compared with traditional model-based methods, they generally suffer from two basic problems that stem from the basic convolution layer. First, the interactions between images and convolution kernels are content-independent. Using the same convolution kernel to restore different image regions may not be the best choice. Second, under the principle of local processing, convolution is not effective for long-range dependency modelling.

## Conclusion

In this paper, we propose a Swin Transformer-based image restoration model SwinIR. The model is composed of three parts: shallow feature extraction, deep feature extraction and HR reconstruction modules. In particular, we use a stack of residual Swin Transformer blocks (RSTB) for deep feature extraction, and each RSTB is composed of Swin Transformer layers, convolution layer and a residual connection....

Next, a multi-layer perceptron (MLP) that has two fully-connected layers with GELU non-linearity between them is used for further feature transformations. The LayerNorm (LN) layer is added before both MSA and MLP, and the residual connection is employed for both modules. The whole process is formulated as

### Loss function

Table 1 shows four residual connection variants in RSTB: no residual connection, using $1 \times 1$ convolution layer, using $3 \times 3$ convolution layer and using three $3 \times 3$ convolution layers (channel number of the intermediate layer is set to one fourth of network channel number). From the table, we can have following observations. First, the residual connection in RSTB is important as it improves the PSNR by 0.16dB. Second, using $1 \times 1$ convolution brings little improvement maybe because it cannot extract local neighbouring information as $3 \times 3$ convolution does....
