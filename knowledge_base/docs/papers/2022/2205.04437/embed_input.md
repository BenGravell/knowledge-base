Activating More Pixels in Image Super-Resolution Transformer

Topics include Image super-resolution, Image restoration, Vision transformers, Hybrid attention, Channel attention, Window attention, Overlapping cross-attention, Same-task pretraining, HAT.

This paper introduces HAT for single-image super-resolution, diagnosing limited input-pixel usage in prior transformer restorers and addressing it with channel attention, window self-attention, overlapping cross-window attention, and same-task pretraining. It is the super-resolution-focused conference version of the HAT line.

Transformer-based methods have shown impressive performance in low-level vision tasks, such as image super-resolution. However, we find that these networks can only utilize a limited spatial range of input information through attribution analysis. This implies that the potential of Transformer is still not fully exploited in existing networks. In order to activate more input pixels for better reconstruction, we propose a novel Hybrid Attention Transformer (HAT). It combines both channel attention and window-based self-attention schemes, thus making use of their complementary advantages of being able to utilize global statistics and strong local fitting capability. Moreover, to better aggregate the cross-window information, we introduce an overlapping cross-attention module to enhance the interaction between neighboring window features. In the training stage, we additionally adopt a same-task pre-training strategy to exploit the potential of the model for further improvement. Extensive experiments show the effectiveness of the proposed modules, and we further scale up the model to demonstrate that the performance of this task can be greatly improved....

## Introduction

Single image super-resolution (SR) is a classic problem in computer vision and image processing. It aims to reconstruct a high-resolution image from a given low-resolution input. Since deep learning has been successfully applied to the SR task, numerous methods based on the convolutional neural network (CNN) have been proposed and almost dominate this field in the past few years. Recently, due to the success in natural language processing, Transformer has attracted the attention of the computer vision community....

Figure 1: Performance comparison on PSNR(dB) of the proposed HAT with the state-of-the-art methods SwinIR and EDT. HAT-L represents a larger variant of HAT. Our approach can surpass the state-of-the-art methods by 0.3dB∼1.2dB.

Table 7: Quantitative results on PSNR(dB) of HAT using two kinds of pre-training strategies on ×4 SR under the same training setting. The full ImageNet dataset is adopted to perform pre-training and DF2K dataset is used for fine-tuning.

Figure 9: Quantitative comparison on PSNR(dB) of four different networks without and with the same-task pre-training on ×4 SR.

We introduce OCAB to directly establish cross-window connections and enhance the representative ability for the window self-attention. Our OCAB consists of an overlapping cross-attention (OCA) layer and an MLP layer similar to the standard Swin Transformer block. But for OCA, as depicted in Fig. 5 ‣ 3.2 Network Architecture ‣ 3 Methodology ‣ Activating More Pixels in Image Super-Resolution Transformer"), we use different window sizes to partition the projected features....

### The Overall Structure

Figure 6: Qualitative comparison of different window sizes.

Despite the success, "why Transformer is better than CNN" remains a mystery. An intuitive explanation is that this kind of network can benefit from the self-attention mechanism and utilize long-range information. Thus, we employ the attribution analysis method LAM to examine the involved range of utilized information for reconstruction in SwinIR. Interestingly, we find that SwinIR does NOT exploit more input pixels than CNN-based methods (e.g., RCAN ) in super-resolution, as shown in Fig. 2....

To address the above-mentioned limitations and further develop the potential of Transformer for SR, we propose a Hybrid Attention Transformer, namely HAT....
