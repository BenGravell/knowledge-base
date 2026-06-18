HAT: Hybrid Attention Transformer for Image Restoration

Topics include Image restoration, Image super-resolution, Vision transformers, Hybrid attention, Channel attention, Window attention, Overlapping cross-attention, Denoising, Compression artifact reduction, HAT.

This extended HAT paper generalizes the hybrid-attention transformer from super-resolution to a broader image-restoration family, including denoising and compression-artifact reduction. It is useful as the more complete HAT reference because it reports scaling behavior and broader restoration coverage.

Transformer-based methods have shown impressive performance in image restoration tasks, such as image super-resolution and denoising. However, we find that these networks can only utilize a limited spatial range of input information through attribution analysis. This implies that the potential of Transformer is still not fully exploited in existing networks. In order to activate more input pixels for better restoration, we propose a new Hybrid Attention Transformer (HAT). It combines both channel attention and window-based self-attention schemes, thus making use of their complementary advantages. Moreover, to better aggregate the cross-window information, we introduce an overlapping cross-attention module to enhance the interaction between neighboring window features. In the training stage, we additionally adopt a same-task pre-training strategy to further exploit the potential of the model for further improvement. Extensive experiments have demonstrated the effectiveness of the proposed modules. We further scale up the model to show that the performance of the SR task can be greatly improved....

## Introduction

Image restoration (IR) is a classic problem in computer vision. It aims to reconstruct a high-quality (HQ) image from a given low-quality (LQ) input. Classic IR tasks encompass image super-resolution, image denoising, compression artifacts reduction, and etc. Image restoration plays an important role in computer vision and has widespread application in areas such as AI photography \[\], surveillance imaging \[\], medical imaging \[\], and image generation \[\]....

Figure 1: Performance comparison of the proposed HAT on various image restoration tasks with the state-of-the-art methods.

## Conclusion

In this work, we propose a new Hybrid Attention Transformer, HAT, for image restoration. Our model combines channel attention and self-attention to activate more pixels for high-resolution reconstruction. Besides, we propose an overlapping cross-attention module to enhance the cross-window interaction. Moreover, we introduce a same-task pre-training strategy for image super-resolution. Extensive benchmark and real-world evaluations demonstrate that HAT outperforms the state-of-the-art methods for several image restoration tasks.

For the structure of HAT, both the RHAG number and HAB number are set to 6. The channel number of the whole network is set to 180. The attention head number and window size are set to 6 and 16 for both (S)W-MSA and OCA. For the specific hyper-parameters of the proposed modules, we set the weighting factor of CAB output ($\alpha$), the squeeze factor between two convolution layers in CAB ($\beta$), and the overlapping ratio of OCA ($\gamma$) as 0.01, 3 and 0.5, respectively. For the large variant HAT-L, we double the depth of HAT by increasing the RHAG number from 6 to 12....

where $H_{DF}{( \cdot )}$ consists of $N_{1}$ residual hybrid attention groups (RHAG) and one $3 \times 3$ convolution layer $H_{Conv}{( \cdot )}$. These RHAGs progressively process the intermediate features as:

Figure 9: Quantitative comparison on PSNR(dB) of four different networks without and with the same-task pre-training on ×4 SR.

Despite its success, existing work has rarely discussed why Transformer outperforms CNN. An intuitive explanation provided in prior study is that Transformer benefits from the self-attention mechanism, allowing it to leverage long-range information \[\]....
