Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning

Topics include Self-supervised learning, Representation learning, Computer vision, BYOL, Bootstrap learning, Non-contrastive learning, Momentum target network, ImageNet, Transfer learning.

BYOL shows that strong image representations can be learned without explicit negative pairs by training an online network to predict the representation of a slowly averaged target network under a different augmentation. The paper is a key non-contrastive self-supervised learning result: its empirical strength forced later work to explain why collapse is avoided and made target-network bootstrapping a standard design pattern for vision SSL.

We introduce Bootstrap Your Own Latent (BYOL), a new approach to self-supervised image representation learning. BYOL relies on two neural networks, referred to as online and target networks, that interact and learn from each other. From an augmented view of an image, we train the online network to predict the target network representation of the same image under a different augmented view. At the same time, we update the target network with a slow-moving average of the online network. While state-of-the art methods rely on negative pairs, BYOL achieves a new state of the art without them. BYOL reaches 74.3% top-1 classification accuracy on ImageNet using a linear evaluation with a ResNet-50 architecture and 79.6% with a larger ResNet. We show that BYOL performs on par or better than the current state of the art on both transfer and semi-supervised benchmarks. Our implementation and pretrained models are given on GitHub.

## Introduction

Figure 1: Performance of BYOL on ImageNet (linear evaluation) using ResNet-50 and our best architecture ResNet-200 (2×), compared to other unsupervised and supervised (Sup​.​) baselines.

Learning good image representations is a key challenge in computer vision as it allows for efficient training on downstream tasks. Many different training approaches have been proposed to learn such representations, usually relying on visual pretext tasks. Among them, state-of-the-art contrastive methods are trained by reducing the distance between representations of different augmented views of the same image ('positive pairs'), and increasing the distance between representations of augmented views from different images ('negative pairs')....

## Broader impact

The presented research should be categorized as research in the field of unsupervised learning. This work may inspire new algorithms, theoretical, and experimental investigation. The algorithm presented here can be used for many different vision applications and a particular use may have both positive or negative impacts, which is known as the dual use problem. Besides, as vision datasets could be biased, the representation learned by BYOL could be susceptible to replicate these biases.

Next, we evaluate the performance obtained when fine-tuning BYOL's representation on a classification task with a small subset of ImageNet's train set, this time using label information. We follow the semi-supervised protocol of detailed in Section C.1, and use the same fixed splits of respectively $1\%$ and $10\%$ of ImageNet labeled training data as in. We report both top-$1$ and top-$5$ accuracies on the test set in Table 2. BYOL consistently outperforms previous approaches across a wide range of architectures....

Furthemore, notice that performing a hard-copy of the online parameters $\theta$ into the target parameters $\xi$ would be enough to propagate new sources of variability. However, sudden changes in the target network might break the assumption of an optimal predictor, in which case BYOL's loss is not guaranteed to be close to the conditional variance. We hypothesize that the main role of BYOL's moving-averaged target network is to ensure the near-optimality of the predictor over training; Section 5 and Appendix I provide some empirical support of this interpretation.

### Batch size
