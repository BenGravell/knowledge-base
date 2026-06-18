FlowNet: Learning Optical Flow with Convolutional Networks

Topics include Optical flow, FlowNet, Convolutional networks, Supervised learning, Correlation layer, Flying chairs, Dense prediction.

FlowNet is the first major end-to-end convolutional network for dense optical flow. Beyond the architectures themselves, the paper's synthetic Flying Chairs training setup is a key contribution because it made supervised dense flow learning feasible before large real-world ground-truth datasets existed.

Convolutional neural networks (CNNs) have recently been very successful in a variety of computer vision tasks, especially on those linked to recognition. Optical flow estimation has not been among the tasks where CNNs were successful. In this paper we construct appropriate CNNs which are capable of solving the optical flow estimation problem as a supervised learning task. We propose and compare two architectures: a generic architecture and another one including a layer that correlates feature vectors at different image locations. Since existing ground truth data sets are not sufficiently large to train a CNN, we generate a synthetic Flying Chairs dataset. We show that networks trained on this unrealistic data still generalize very well to existing datasets such as Sintel and KITTI, achieving competitive accuracy at frame rates of 5 to 10 fps.

## Introduction

Convolutional neural networks have become the method of choice in many fields of computer vision. They are classically applied to classification, but recently presented architectures also allow for per-pixel predictions like semantic segmentation or depth estimation from single images. In this paper, we propose training CNNs end-to-end to learn predicting the optical flow field from a pair of images.

While optical flow estimation needs precise per-pixel localization, it also requires finding correspondences between two input images. This involves not only learning image feature representations, but also learning to match them at different locations in the two images. In this respect, optical flow estimation fundamentally differs from previous applications of CNNs.

## Conclusion

Building on recent progress in design of convolutional network architectures, we have shown that it is possible to train a network to directly predict optical flow from two input images. Intriguingly, the training data need not be realistic. The artificial Flying Chairs dataset including just affine motions of synthetic rigid objects is sufficient to predict optical flow in natural scenes with competitive accuracy. This proves the generalization capabilities of the presented networks. On the test set of the Flying Chairs the CNNs even outperform state-of-the-art methods like DeepFlow and EpicFlow....

The MPI Sintel dataset obtains ground truth from rendered artificial scenes with special attention to realistic image properties. Two versions are provided: the Final version contains motion blur and atmospheric effects, such as fog, while the Clean version does not include these effects. Sintel is the largest dataset available (1,041 training image pairs for each version) and provides dense ground truth for small and large displacement magnitudes.

Given a maximum displacement $d$, for each location $\mathbf{x}_{1}$ we compute correlations $c{(\mathbf{x}_{1},\mathbf{x}_{2})}$ only in a neighborhood of size $D:={{2d} + 1}$, by limiting the range of $\mathbf{x}_{2}$. We use strides $s_{1}$ and $s_{2}$, to quantize $\mathbf{x}_{1}$ globally and to quantize $\mathbf{x}_{2}$ within the neighborhood centered around $\mathbf{x}_{1}$.

For training CNNs we use a modified version of the caffe framework. We choose Adam as optimization method because for our task it shows...
