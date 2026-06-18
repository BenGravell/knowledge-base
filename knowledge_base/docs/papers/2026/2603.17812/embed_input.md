ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation

Topics include Diffusion models, Control, ChopGrad.

Recent video diffusion models achieve high-quality generation through recurrent frame processing where each frame generation depends on previous frames. However, this recurrent mechanism means that training such models in the pixel domain incurs prohibitive memory costs, as activations accumulate across the entire video sequence. This fundamental limitation also makes fine-tuning these models with pixel-wise losses computationally intractable for long or high-resolution videos. This paper introduces ChopGrad, a truncated backpropagation scheme for video decoding, limiting gradient computation to local frame windows while maintaining global consistency. We provide a theoretical analysis of this approximation and show that it enables efficient fine-tuning with frame-wise losses.
