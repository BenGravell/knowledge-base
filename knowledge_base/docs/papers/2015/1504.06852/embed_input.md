FlowNet: Learning Optical Flow with Convolutional Networks

Topics include Optical flow, FlowNet, Convolutional networks, Supervised learning, Correlation layer, Flying chairs, Dense prediction.

FlowNet is the first major end-to-end convolutional network for dense optical flow. Beyond the architectures themselves, the paper's synthetic Flying Chairs training setup is a key contribution because it made supervised dense flow learning feasible before large real-world ground-truth datasets existed.

Convolutional neural networks (CNNs) have recently been very successful in a variety of computer vision tasks, especially on those linked to recognition. Optical flow estimation has not been among the tasks where CNNs were successful. In this paper we construct appropriate CNNs which are capable of solving the optical flow estimation problem as a supervised learning task. We propose and compare two architectures: a generic architecture and another one including a layer that correlates feature vectors at different image locations. Since existing ground truth data sets are not sufficiently large to train a CNN, we generate a synthetic Flying Chairs dataset. We show that networks trained on this unrealistic data still generalize very well to existing datasets such as Sintel and KITTI, achieving competitive accuracy at frame rates of 5 to 10 fps.

## Introduction

Convolutional neural networks have become the method of choice in many fields of computer vision. They are classically applied to classification, but recently presented architectures also allow for per-pixel predictions like semantic segmentation or depth estimation from single images. In this paper, we propose training CNNs end-to-end to learn predicting the optical flow field from a pair of images.

While optical flow estimation needs precise per-pixel localization, it also requires finding correspondences between two input images. This involves not only learning image feature representations, but also learning to match them at different locations in the two images. In this respect, optical flow estimation fundamentally differs from previous applications of CNNs.

Since it was not clear whether this task could be solved with a standard CNN architecture, we additionally developed an architecture with a correlation layer that explicitly provides matching capabilities. This architecture is trained end-to-end. The idea is to exploit the ability of convolutional networks to learn strong features at multiple levels of scale and abstraction and to help it with finding the actual correspondences based on these features. The layers on top of the correlation layer learn how to predict flow from these matches.

Leveraging an efficient GPU implementation of CNNs, our method is faster than most competitors. Our networks predict optical flow at up to $10$ image pairs per second on the full resolution of the Sintel dataset, achieving state-of-the-art accuracy among real-time methods.

## Conclusion

Building on recent progress in design of convolutional network architectures, we have shown that it is possible to train a network to directly predict optical flow from two input images. Intriguingly, the training data need not be realistic. The artificial Flying Chairs dataset including just affine motions of synthetic rigid objects is sufficient to predict optical flow in natural scenes with competitive accuracy. This proves the generalization capabilities of the presented networks. On the test set of the Flying Chairs the CNNs even outperform state-of-the-art methods like DeepFlow and EpicFlow.
