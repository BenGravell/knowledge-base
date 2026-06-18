Deep Clustering via Joint Convolutional Autoencoder Embedding and Relative Entropy Minimization

Topics include Convolutional networks, Autoencoders, Computer vision, Clustering, Regression, Scalability, Optimization, Learning, Deep embedded clustering, DEPICT.

Image clustering is one of the most important computer vision applications, which has been extensively studied in literature. However, current clustering methods mostly suffer from lack of efficiency and scalability when dealing with large-scale and high-dimensional data. In this paper, we propose a new clustering model, called DEeP Embedded RegularIzed ClusTering (DEPICT), which efficiently maps data into a discriminative embedding subspace and precisely predicts cluster assignments. DEPICT generally consists of a multinomial logistic regression function stacked on top of a multi-layer convolutional autoencoder. We define a clustering objective function using relative entropy (KL divergence) minimization, regularized by a prior for the frequency of cluster assignments. An alternating strategy is then derived to optimize the objective by updating parameters and estimating cluster assignments. Furthermore, we employ the reconstruction loss functions in our autoencoder, as a data-dependent regularization term, to prevent the deep embedding function from overfitting....

## Introduction

Figure 1: Visualization to show the discriminative capability of embedding subspaces using MNIST-test data. (a) The space of raw data. (b) The embedding subspace of non-joint DEPICT using standard stacked denoising autoencoder (SdA). (c) The embedding subspace of joint DEPICT using our joint learning approach (MdA).

Clustering is one of the fundamental research topics in machine learning and computer vision research, and it has gained significant attention for discriminative representation of data points without any need for supervisory signals. The clustering problem has been extensively studied in various applications; however, the performance of standard clustering algorithms is adversely affected when dealing with high-dimensional data, and their time complexity dramatically increases when working with large-scale datasets....

## Conclusion

In this paper, we proposed a new deep clustering model, DEPICT, consisting of a soft-max layer stacked on top of a multi-layer convolutional autoencoder. We employed a regularized relative entropy loss function for clustering, which leads to balanced cluster assignments. Adopting our autoencoder reconstruction loss function enhanced the embedding learning. Furthermore, a joint learning framework was introduced to train all network layers simultaneously and avoid layer-wise pretraining....

where ${\overset{\sim}{\mathbf{z}}}^{l}$ are the noisy features of the $l$-th layer, $Dropout$ is a stochastic mask function that randomly sets a subset of its inputs to zero, $g$ is the activation function of convolutional or fully connected layers, and $\mathbf{W}_{e}^{l}$ indicates the weights of the $l$-th layer in the encoder. Note that the first layer features, ${\overset{\sim}{\mathbf{z}}}^{0}$, are equal to the noisy input data, $\overset{\sim}{\mathbf{x}}$.

where $f_{k}$ can be considered as the soft frequency of cluster assignments in the target distribution. Using this empirical distribution, we are able to enforce our preference for having balanced assignments by adding the following KL divergence to the loss function.

## Samples
## Classes
## Dimensions

However, dealing with real-world image data, existing clustering algorithms suffer from different issues: 1) Using inflexible hand-crafted features, which do not depend on the input data distribution; 2) Using shallow and linear embedding...
