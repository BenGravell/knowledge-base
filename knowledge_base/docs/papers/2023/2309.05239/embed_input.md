HAT: Hybrid Attention Transformer for Image Restoration

Topics include Image restoration, Image super-resolution, Vision transformers, Hybrid attention, Channel attention, Window attention, Overlapping cross-attention, Denoising, Compression artifact reduction, HAT.

This extended HAT paper generalizes the hybrid-attention transformer from super-resolution to a broader image-restoration family, including denoising and compression-artifact reduction. It is useful as the more complete HAT reference because it reports scaling behavior and broader restoration coverage.

Transformer-based methods have shown impressive performance in image restoration tasks, such as image super-resolution and denoising. However, we find that these networks can only utilize a limited spatial range of input information through attribution analysis. This implies that the potential of Transformer is still not fully exploited in existing networks. In order to activate more input pixels for better restoration, we propose a new Hybrid Attention Transformer (HAT). It combines both channel attention and window-based self-attention schemes, thus making use of their complementary advantages. Moreover, to better aggregate the cross-window information, we introduce an overlapping cross-attention module to enhance the interaction between neighboring window features. In the training stage, we additionally adopt a same-task pre-training strategy to further exploit the potential of the model for further improvement. Extensive experiments have demonstrated the effectiveness of the proposed modules. We further scale up the model to show that the performance of the SR task can be greatly improved.

## Introduction

Image restoration (IR) is a classic problem in computer vision. It aims to reconstruct a high-quality (HQ) image from a given low-quality (LQ) input. Classic IR tasks encompass image super-resolution, image denoising, compression artifacts reduction, and etc. Image restoration plays an important role in computer vision and has widespread application in areas such as AI photography, surveillance imaging, medical imaging, and image generation. Since deep learning has been successfully applied to IR tasks, numerous methods based on the convolutional neural network (CNN) have been proposed and almost dominate this field in the past few years.

To address the above-mentioned limitations of the existing IR Transformer and further develop the potential of such networks, we propose a Hybrid Attention Transformer, namely HAT. It combines channel attention and self-attention schemes, in order to take advantage of the former's capability in using global information and the powerful representative ability of the latter. Besides, we introduce an overlapping cross-attention module to achieve more direct interaction of adjacent window features. Benefiting from these designs, our model can activate more pixels for reconstruction and thus obtains significant performance improvement.

We propose an effective same-task pre-training strategy to further exploit the potential of SR Transformer and show the importance of large-scale data pre-training.

Our method significantly outperforms existing state-of-the-art methods on the SR task. By further scaling up HAT to build a large model, we greatly extend the performance upper bound of the SR task.

Our method also achieves state-of-the-art performance on image denoising and compression artifacts reduction, showing its superiority on various image restoration tasks.

## Conclusion

In this work, we propose a new Hybrid Attention Transformer, HAT, for image restoration. Our model combines channel attention and self-attention to activate more pixels for high-resolution reconstruction. Besides, we propose an overlapping cross-attention module to enhance the cross-window interaction. Moreover, we introduce a same-task pre-training strategy for image super-resolution. Extensive benchmark and real-world evaluations demonstrate that HAT outperforms the state-of-the-art methods for several image restoration tasks.
