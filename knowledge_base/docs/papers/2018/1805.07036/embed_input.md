LiteFlowNet: A Lightweight Convolutional Neural Network for Optical Flow Estimation

Topics include Optical flow, LiteFlowNet, Convolutional networks, Lightweight models, Feature warping, Cascaded flow inference, Flow regularization.

LiteFlowNet pushes learned optical flow toward smaller and faster models by combining feature pyramids, feature warping, cascaded refinement, descriptor matching, and learned local regularization. It is useful as a counterpoint to FlowNet2: many of the accuracy gains can be retained without a very large stacked network.

FlowNet2, the state-of-the-art convolutional neural network (CNN) for optical flow estimation, requires over 160M parameters to achieve accurate flow estimation. In this paper we present an alternative network that outperforms FlowNet2 on the challenging Sintel final pass and KITTI benchmarks, while being 30 times smaller in the model size and 1.36 times faster in the running speed. This is made possible by drilling down to architectural details that might have been missed in the current frameworks: We present a more effective flow inference approach at each pyramid level through a lightweight cascaded network. It not only improves flow estimation accuracy through early correction, but also permits seamless incorporation of descriptor matching in our network. We present a novel flow regularization layer to ameliorate the issue of outliers and vague flow boundaries by using a feature-driven local convolution. Our network owns an effective structure for pyramidal feature extraction and embraces feature warping rather than image warping as practiced in FlowNet2. Our code and trained models are available at

## Introduction

Optical flow estimation is a long-standing problem in computer vision. Due to the well-known aperture problem, optical flow is not directly measurable. Hence, the estimation is typically solved by energy minimization in a coarse-to-fine framework. This class of techniques, however, involves complex energy optimization and thus it is not scalable for applications that demand real-time estimation.

FlowNet and its successor FlowNet2, have marked a milestone by using CNN for optical flow estimation. Their accuracies especially the successor are approaching that of state-of-the-art energy minimization approaches, while the speed is several orders of magnitude faster. To push the envelop of accuracy, FlowNet2 is designed as a cascade of variants of FlowNet that each network in the cascade refines the preceding flow field by contributing on the flow increment between the first image and the warped second image. The model, as a result, comprises over 160M parameters, which could be formidable in many applications....

## Conclusion

We have presented a compact network for accurate flow estimation. LiteFlowNet outperforms FlowNet and is on par with or outperforms the state-of-the-art FlowNet2 on public benchmarks while being faster in runtime and 30 times smaller in model size. Pyramidal feature extraction and feature warping (f-warp) help us to break the de facto rule of accurate flow network requiring large model size. To address large-displacement and detail-preserving flows, LiteFlowNet exploits short-range matching to generate pixel-level flow field and further improves the estimate to sub-pixel accuracy in the cascaded flow inference....

where "$\ast$" denotes convolution, $f{(x,y,c)}$ is a $w \times w$ patch centered at position $(x,y)$ of channel $c$ in $F$, $g{(x,y,c)}$ is the corresponding $w \times w$ regularization filter, and $f_{g}{(x,y,c)}$ is a scalar output for $\mathbf{x} = {(x,y)}^{\top}$ and $c = {1,2,\ldots,C}$. To be specific for regularizing flow field ${\overset{˙}{\mathbf{x}}}_{s}$ from the cascaded flow inference, we replace $F$ to ${\overset{˙}{\mathbf{x}}}_{s}$. Flow regularization module $R$ is defined as follows:

### Cascaded Flow Inference

Table 1: AEE on the Chairs testing set. Models are trained on the Chairs training set.
