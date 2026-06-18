VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

Topics include Self-supervised learning, Representation learning, Computer vision, VICReg, Variance regularization, Covariance regularization, Collapse prevention, Redundancy reduction, Non-contrastive learning.

VICReg decomposes non-contrastive representation learning into three explicit pressures: make paired augmentations agree, keep each embedding dimension's variance above a floor, and reduce covariance between dimensions. The variance term makes collapse prevention direct rather than architectural, and the paper usefully separates invariance, information preservation, and redundancy reduction into interpretable regularizers that can also stabilize other SSL methods.

Recent self-supervised methods for image representation learning are based on maximizing the agreement between embedding vectors from different views of the same image. A trivial solution is obtained when the encoder outputs constant vectors. This collapse problem is often avoided through implicit biases in the learning architecture, that often lack a clear justification or interpretation. In this paper, we introduce VICReg (Variance-Invariance-Covariance Regularization), a method that explicitly avoids the collapse problem with a simple regularization term on the variance of the embeddings along each dimension individually. VICReg combines the variance term with a decorrelation mechanism based on redundancy reduction and covariance regularization, and achieves results on par with the state of the art on several downstream tasks. In addition, we show that incorporating our new variance term into other methods helps stabilize the training and leads to performance improvements.

## Introduction

Self-supervised representation learning has made significant progress over the last years, almost reaching the performance of supervised baselines on many downstream tasks Bachman et al.; Misra & Maaten; He et al.; Tian et al.; Caron et al.; Grill et al.; Chen & He; Gidaris et al.; Zbontar et al.. Several recent approaches rely on a joint embedding architecture in which two networks are trained to produce similar embeddings for different views of the same image. A popular instance is the Siamese network architecture Bromley et al., where the two networks share the same weights.

## VICReg: intuition

We introduce VICReg (Variance-Invariance-Covariance Regularization), a self-supervised method for training joint embedding architectures based on the principle of preserving the information content of the embeddings.

Invariance: the mean square distance between the embedding vectors.

Variance: a hinge loss to maintain the standard deviation (over a batch) of each variable of the embedding above a given threshold. This term forces the embedding vectors of samples within a batch to be different.

## Conclusion

We introduced VICReg, a simple approach to self-supervised learning based on a triple objective: learning invariance to different views with a invariance term, avoiding collapse of the representations with a variance preservation term, and maximizing the information content of the representation with a covariance regularization term. VICReg achieves results on par with the state of the art on many downstream tasks, but is not subject to the same limitations as most other methods, particularly because it does not require the embedding branches to be identical or even similar.
