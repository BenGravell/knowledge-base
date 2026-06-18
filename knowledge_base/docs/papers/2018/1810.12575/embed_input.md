Neural Nearest Neighbors Networks

Topics include Neural networks, Convolutional networks, Nearest neighbors, Classification, Rely on k-nearest neighbors, KNN, Convolutional neural network.

Non-local methods exploiting the self-similarity of natural signals have been well studied, for example in image analysis and restoration. Existing approaches, however, rely on k-nearest neighbors (KNN) matching in a fixed feature space. The main hurdle in optimizing this feature space w.r.t. application performance is the non-differentiability of the KNN selection rule. To overcome this, we propose a continuous deterministic relaxation of KNN selection that maintains differentiability w.r.t. pairwise distances, but retains the original KNN as the limit of a temperature parameter approaching zero. To exploit our relaxation, we propose the neural nearest neighbors block (N3 block), a novel non-local processing layer that leverages the principle of self-similarity and can be used as building block in modern neural network architectures. We show its effectiveness for the set reasoning task of correspondence classification as well as for image restoration, including image denoising and single image super-resolution, where we outperform strong convolutional neural network (CNN) baselines and recent non-local models that rely on KNN selection in hand-chosen features spaces.

## Introduction

The ongoing surge of convolutional neural networks (CNNs) has revolutionized many areas of machine learning and its applications by enabling unprecedented predictive accuracy. Most network architectures focus on local processing by combining convolutional layers and element-wise operations. In order to draw upon information from a sufficiently broad context, several strategies, including dilated convolutions or hourglass-shaped architectures, have been explored to increase the receptive field size. Yet, they trade off context size for localization accuracy. Hence, for many dense prediction tasks, *e....

In contrast, traditional algorithms in image restoration increase the receptive field size via non-local processing, leveraging the self-similarity of natural signals. They exploit that image structures tend to re-occur within the same image, giving rise to a strong prior for image restoration. Hence, methods like non-local means or BM3D aggregate information across the whole image to restore a local patch. Here, matching patches are usually selected based on some hand-crafted notion of similarity, *e. g.* the Euclidean distance between patches of input intensities....

## Conclusion

Non-local methods have been well studied, *e. g.*, in image restoration. Existing approaches, however, apply KNN selection on a hand-defined feature space, which may be suboptimal for the task at hand. To overcome this limitation, we introduced the first continuous relaxation of the KNN selection rule that maintains differentiability *w. r. t.* the pairwise distances used for neighbor selection. We integrated continuous nearest neighbors selection into a novel network block, called $\text{N}^{3}$ block, which can be used as a general building block in neural networks....

We now analyze the properties of our novel $\text{N}^{3}$Net and show its benefits over state-of-the-art baselines. We use image denoising as our main test bed as non-local methods have been well studied there. Moreover, we evaluate on single image super-resolution and correspondence classification.

In the limit of $t\rightarrow 0$, the expectation ${\overline{w}}^{1}$ of the first sampled index vector will approach a one-hot encoding of the index of the closest neighbor. As a consequence, the logit update in Eq. 9 will also converge to the hard update from Eq. 5....
