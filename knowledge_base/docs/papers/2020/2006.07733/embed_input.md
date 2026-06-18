Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning

Topics include Self-supervised learning, Representation learning, Computer vision, BYOL, Bootstrap learning, Non-contrastive learning, Momentum target network, ImageNet, Transfer learning.

BYOL shows that strong image representations can be learned without explicit negative pairs by training an online network to predict the representation of a slowly averaged target network under a different augmentation. The paper is a key non-contrastive self-supervised learning result: its empirical strength forced later work to explain why collapse is avoided and made target-network bootstrapping a standard design pattern for vision SSL.

We introduce Bootstrap Your Own Latent (BYOL), a new approach to self-supervised image representation learning. BYOL relies on two neural networks, referred to as online and target networks, that interact and learn from each other. From an augmented view of an image, we train the online network to predict the target network representation of the same image under a different augmented view. At the same time, we update the target network with a slow-moving average of the online network. While state-of-the art methods rely on negative pairs, BYOL achieves a new state of the art without them. BYOL reaches 74.3% top-1 classification accuracy on ImageNet using a linear evaluation with a ResNet-50 architecture and 79.6% with a larger ResNet. We show that BYOL performs on par or better than the current state of the art on both transfer and semi-supervised benchmarks. Our implementation and pretrained models are given on GitHub.

## Introduction

Learning good image representations is a key challenge in computer vision as it allows for efficient training on downstream tasks. Many different training approaches have been proposed to learn such representations, usually relying on visual pretext tasks. Among them, state-of-the-art contrastive methods are trained by reducing the distance between representations of different augmented views of the same image ('positive pairs'), and increasing the distance between representations of augmented views from different images ('negative pairs').

In this paper, we introduce Bootstrap Your Own Latent (BYOL), a new algorithm for self-supervised learning of image representations. BYOL achieves higher performance than state-of-the-art contrastive methods without using negative pairs. It iteratively bootstraps^44^4Throughout this paper, the term *bootstrap* is used in its idiomatic sense rather than the statistical sense. the outputs of a network to serve as targets for an enhanced representation.

We evaluate the representation learned by BYOL on ImageNet and other vision benchmarks using ResNet architectures. Under the linear evaluation protocol on ImageNet, consisting in training a linear classifier on top of the frozen representation, BYOL reaches $74.3\%$ top-1 accuracy with a standard ResNet-$50$ and $79.6\%$ top-1 accuracy with a larger ResNet (Figure 1). In the semi-supervised and transfer settings on ImageNet, we obtain results on par or superior to the current state of the art.

## Conclusion

We introduced BYOL, a new algorithm for self-supervised learning of image representations. BYOL learns its representation by predicting previous versions of its outputs, without using negative pairs. We show that BYOL achieves state-of-the-art results on various benchmarks. In particular, under the linear evaluation protocol on ImageNet with a ResNet-$50$ ($1 \times$), BYOL achieves a new state of the art and bridges most of the remaining gap between self-supervised methods and the supervised learning baseline of.
