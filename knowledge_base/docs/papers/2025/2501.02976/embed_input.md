STAR: Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution

Topics include Video super-resolution, Real-world super-resolution, Image restoration, Text-to-video models, Diffusion models, Temporal consistency, Local information enhancement, Dynamic frequency loss, STAR.

STAR adapts text-to-video diffusion models to real-world video super-resolution, using local information enhancement and a dynamic frequency loss to improve detail recovery while preserving temporal coherence. It is useful as a recent example of moving super-resolution from per-frame image priors toward video-native generative priors.

Image diffusion models have been adapted for real-world video super-resolution to tackle over-smoothing issues in GAN-based methods. However, these models struggle to maintain temporal consistency, as they are trained on static images, limiting their ability to capture temporal dynamics effectively. Integrating text-to-video (T2V) models into video super-resolution for improved temporal modeling is straightforward. However, two key challenges remain: artifacts introduced by complex degradations in real-world scenarios, and compromised fidelity due to the strong generative capacity of powerful T2V models (\textit{e.g.}, CogVideoX-5B). To enhance the spatio-temporal quality of restored videos, we introduce\textbf{~\name} (\textbf{S}patial-\textbf{T}emporal \textbf{A}ugmentation with T2V models for \textbf{R}eal-world video super-resolution), a novel approach that leverages T2V models for real-world video super-resolution, achieving realistic spatial details and robust temporal consistency. Specifically, we introduce a Local Information Enhancement Module (LIEM) before the global attention block to enrich local details and mitigate degradation artifacts....

## Introduction

Real-world video super-resolution (VSR) aims to generate high-resolution (HR) videos with clear details and strong temporal consistency from low-resolution (LR) inputs with unknown degradations. Most VSR methods only focus on simple, known degradations like downsampling or camera-related issues \[\]. However, real-world scenarios often involve unexpected degradations such as noise, blur, and compression, making it difficult for models to capture both spatial and temporal information needed for high-quality, consistent restoration.

GAN-based methods are widely used in real-world VSR for improving details through adversarial learning. By incorporating optical flow maps, they also improve temporal consistency, yielding smooth motion across frames. However, their limited generative capacity often results in oversmoothing, as illustrated in Figure. Recently, image diffusion models \[\] have been applied to real-world VSR for realistic video generation. Methods like incorporate temporal blocks or optical flow maps to improve temporal information capture....

## Conclusion

In this paper, we present STAR, a real-world VSR framework that leverages T2V diffusion prior to restore videos with fewer artifacts, higher spatial fidelity, and stronger temporal consistency. Specifically, we introduce a Local Information Enhancement Module into the original T2V backbone to improve its ability to handle degradations and reconstruct fine details. Additionally, we propose a Dynamic Frequency Loss that guides the model to focus on restoring different frequency components at each diffusion step, thereby enhancing fidelity....

### Motivation

### Losses

Figure 8: Qualitative comparisons on temporal consistency in and OpenVid dataset. (Zoom-in for best view)

To fully leverage the T2V prior to enhance practical VSR, we introduce STAR, a novel Spatial-Temporal Augmentation approach for Real-world VSR that achieves realistic spatial details and robust temporal consistency. Specifically, $1$) To address artifacts, we introduce a Local Information Enhancement Module (LIEM) before global self-attention to evaluate its impact on T2V models for real-world VSR....
