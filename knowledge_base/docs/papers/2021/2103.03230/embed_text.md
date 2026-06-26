## Introduction

Figure 1: Barlow Twins’s objective function measures the cross-correlation matrix between the embeddings of two identical networks fed with distorted versions of a batch of samples, and tries to make this matrix close to the identity. This causes the embedding vectors of distorted versions of a sample to be similar, while minimizing the redundancy between the components of these vectors. Barlow Twins is competitive with state-of-the-art methods for self-supervised learning while being conceptually simpler, naturally avoiding trivial constant (i.e. collapsed) embeddings, and being robust to the training batch size.

Self-supervised learning aims to learn useful representations of the input data without relying on human annotations. Recent advances in self-supervised learning for visual data show that it is possible to learn self-supervised representations that are competitive with supervised representations. A common underlying theme that unites these methods is that they all aim to learn representations that are invariant under different distortions (also referred to as 'data augmentations'). This is typically achieved by maximizing similarity of representations obtained from different distorted versions of a sample using a variant of Siamese networks. As there are trivial solutions to this problem, like a constant representation, these methods rely on different mechanisms to learn useful representations.

Contrastive methods like SimCLR define 'positive' and 'negative' sample pairs which are treated differently in the loss function. Additionally, they can also use asymmetric learning updates wherein momentum encoders are updated separately from the main network. Clustering methods use one distorted sample to compute 'targets' for the loss, and another distorted version of the sample to predict these targets, followed by an alternate optimization scheme like k-means in DeepCluster or non-differentiable operators in SwAV and SeLa. In another recent line of work, BYOL and SimSiam, both the network architecture and parameter updates are modified to introduce asymmetry. The network architecture is modified to be asymmetric using a special 'predictor' network and the parameter updates are asymmetric such that the model parameters are only updated using one distorted version of the input, while the representations from another distorted version are used as a fixed target. conclude that the asymmetry of the learning update, 'stop-gradient', is critical to preventing trivial solutions.

In this paper, we propose a new method, Barlow Twins, which applies *redundancy-reduction* --- a principle first proposed in neuroscience --- to self-supervised learning. In his influential article *Possible Principles Underlying the Transformation of Sensory Messages*, neuroscientist H. Barlow hypothesized that the goal of sensory processing is to recode highly redundant sensory inputs into a factorial code (a code with statistically independent components). This principle has been fruitful in explaining the organization of the visual system, from the retina to cortical areas (see for a review and for recent efforts), and has led to a number of algorithms for supervised and unsupervised learning. Based on this principle, we propose an objective function which tries to make the cross-correlation matrix computed from twin embeddings as close to the identity matrix as possible. Barlow Twins is conceptually simple, easy to implement and learns useful representations as opposed to trivial solutions. Compared to other methods, it does not require large batches, nor does it require any asymmetric mechanisms like prediction networks, momentum encoders, non-differentiable operators or stop-gradients. Intriguingly, Barlow Twins strongly benefits from the use of very high-dimensional embeddings. Barlow Twins outperforms previous methods on ImageNet for semi-supervised classification in the low-data regime (55% top-1 accuracy for 1% labels), and is on par with current state of the art for ImageNet classification with a linear classifier head, as well as for a number of transfer tasks of classification and object detection.

## Method

### Description of Barlow Twins

Like other methods for SSL, Barlow Twins operates on a joint embedding of distorted images (Fig. 1). More specifically, it produces two distorted views for all images of a batch $X$ sampled from a dataset. The distorted views are obtained via a distribution of data augmentations $\mathcal{T}$. The two batches of distorted views $Y^{A}$ and $Y^{B}$ are then fed to a function $f_{\theta}$, typically a deep network with trainable parameters $\theta$, producing batches of embeddings $Z^{A}$ and $Z^{B}$ respectively. To simplify notations, $Z^{A}$ and $Z^{B}$ are assumed to be mean-centered along the batch dimension, such that each unit has mean output 0 over the batch.

Barlow Twins distinguishes itself from other methods by its innovative loss function $\mathcal{L}_{\mathcal{B}\mathcal{T}}$: where $\lambda$ is a positive constant trading off the importance of the first and second terms of the loss, and where $\mathcal{C}$ is the cross-correlation matrix computed between the outputs of the two identical networks along the batch dimension: where $b$ indexes batch samples and $i,j$ index the vector dimension of the networks' outputs. $\mathcal{C}$ is a square matrix with size the dimensionality of the network's output, and with values comprised between -1 (i.e. perfect anti-correlation) and 1 (i.e. perfect correlation).

Intuitively, the *invariance term* of the objective, by trying to equate the diagonal elements of the cross-correlation matrix to 1, makes the embedding invariant to the distortions applied. The *redundancy reduction term*, by trying to equate the off-diagonal elements of the cross-correlation matrix to 0, decorrelates the different vector components of the embedding. This decorrelation reduces the redundancy between output units, so that the output units contain non-redundant information about the sample.

More formally, Barlow Twins's objective function can be understood through the lens of information theory, and specifically as an instanciation of the *Information Bottleneck (IB)* objective. Applied to self-supervised learning, the IB objective consists in finding a representation that conserves as much information about the sample as possible while being the *least* possible informative about the specific distortions applied to that sample. The mathematical connection between Barlow Twins's objective function and the IB principle is explored in Appendix A.

Barlow Twins' objective function has similarities with existing objective functions for SSL. For example, the redundancy reduction term plays a role similar to the *contrastive term* in the infoNCE objective, as discussed in detail in Section 5. However, important conceptual differences in these objective functions result in practical advantages of our method compared to infoNCE-based methods, namely that our method does not require a large number of negative samples and can thus operate on small batches our method benefits from very high-dimensional embeddings. Alternatively, the redundancy reduction term can be viewed as a *soft-whitening* constraint on the embeddings, connecting our method to a recently proposed method performing a *hard-whitening* operation on the embeddings, as discussed in Section 5. However, our method performs better than current hard-whitening methods.

The pseudocode for Barlow Twins is shown as Algorithm 1.

### Implementation Details

## f: encoder network

## lambda: weight on the off-diagonal terms

## N: batch size

## dimensionality of the embeddings

## matrix-matrix multiplication

## off_diagonal: off-diagonal elements of a matrix

## eye: identity matrix

for x in loader: # load a batch with N samples

## two randomly augmented versions of x

## compute embeddings

## normalize repr. along the batch dimension

z_a_norm = (z_a - z_a.mean) / z_a.std # NxD z_b_norm = (z_b - z_b.mean) / z_b.std # NxD

## cross-correlation matrix

c = mm(z_a_norm.T, z_b_norm) / N # DxD

## loss

c_diff = (c - eye(D)).pow # DxD

## multiply off-diagonal elems of c_diff by lambda

off_diagonal(c_diff).mul_(lambda) loss = c_diff.sum

## optimization step

Algorithm 1 PyTorch-style pseudocode for Barlow Twins.

### Image augmentations

Each input image is transformed twice to produce the two distorted views shown in Figure 1. The image augmentation pipeline consists of the following transformations: random cropping, resizing to $224 \times 224$, horizontal flipping, color jittering, converting to grayscale, Gaussian blurring, and solarization. The first two transformations (cropping and resizing) are always applied, while the last five are applied randomly, with some probability. This probability is different for the two distorted views in the last two transformations (blurring and solarization). We use the same augmentation parameters as BYOL.

### Architecture

The encoder consists of a ResNet-50 network followed by a projector network. The projector network has three linear layers, each with 8192 output units. The first two layers of the projector are followed by a batch normalization layer and rectified linear units. We call the output of the encoder the 'representations' and the output of the projector the 'embeddings'. The representations are used for downstream tasks and the embeddings are fed to the loss function of Barlow Twins.

### Optimization

We follow the optimization protocol described in BYOL. We use the LARS optimizer and train for 1000 epochs with a batch size of 2048. We however emphasize that our model works well with batches as small as 256 (see Ablations). We use a learning rate of 0.2 for the weights and 0.0048 for the biases and batch normalization parameters. We multiply the learning rate by the batch size and divide it by 256. We use a learning rate warm-up period of 10 epochs, after which we reduce the learning rate by a factor of 1000 using a cosine decay schedule. We ran a search for the trade-off parameter $\lambda$ of the loss function and found the best results for $\lambda = {5 \cdot 10^{- 3}}$. We use a weight decay parameter of $1.5 \cdot 10^{- 6}$. The biases and batch normalization parameters are excluded from LARS adaptation and weight decay. Training is distributed across 32 V100 GPUs and takes approximately 124 hours. For comparison, our reimplementation of BYOL trained with a batch size of 4096 takes 113 hours on the same hardware.

## Results

We follow standard practice and evaluate our representations by transfer learning to different datasets and tasks in computer vision. Our network is pretrained using self-supervised learning on the training set of the ImageNet ILSVRC-2012 dataset (without labels). We evaluate our model on a variety of tasks such as image classification and object detection, and using fixed representations from the network or finetuning it. We provide the hyperparameters for all the transfer learning experiments in the Appendix.

### Linear and Semi-Supervised Evaluations on ImageNet

### Linear evaluation on ImageNet

We train a linear classifier on ImageNet on top of fixed representations of a ResNet-50 pretrained with our method. The top-1 and top-5 accuracies obtained on the ImageNet validation set are reported in Table 1. Our method obtains a top-1 accuracy of $73.2\%$ which is comparable to the state-of-the-art methods.

Barlow Twins (ours) Table 1: Top-1 and top-5 accuracies (in %) under linear evaluation on ImageNet. All models use a ResNet-50 encoder. Top-3 best self-supervised methods are underlined.

### Semi-supervised training on ImageNet

We fine-tune a ResNet-50 pretrained with our method on a subset of ImageNet. We use subsets of size $1\%$ and $10\%$ using the same split as SimCLR. The semi-supervised results obtained on the ImageNet validation set are reported in Table 2. Our method is either on par (when using $10\%$ of the data) or slightly better (when using $1\%$ of the data) than competing methods.

Barlow Twins (ours) Table 2: Semi-supervised learning on ImageNet using 1% and 10% training examples. Results for the supervised method are. Best results are in bold.

### Transfer to other datasets and tasks

Barlow Twins (ours) Table 3: Transfer learning: image classification. We benchmark learned representations on the image classification task by training linear classifiers on fixed features. We report top-1 accuracy on Places-205 and iNat18 datasets, and classification mAP. Top-3 best self-supervised methods are underlined.

Image classification with fixed features We follow the setup from and train a linear classifier on fixed image representations, *i.e*., the parameters of the ConvNet remain unchanged. We use a diverse set of datasets for this evaluation - Places-205 for scene classification, for multi-label image classification, and iNaturalist2018 for fine-grained image classification. We report our results in Table 3. Barlow Twins performs competitively against prior work, and outperforms SimCLR and MoCo-v2 on most datasets.

Object Detection and Instance Segmentation We evaluate our representations for the localization based tasks of object detection and instance segmentation. We use the +12 and COCO datasets following the setup in which finetunes the ConvNet parameters. Our results in Table 4 indicate that Barlow Twins performs comparably or better than state-of-the-art representation learning methods for these localization tasks.

COCO instance seg Table 4: Transfer learning: object detection and instance segmentation. We benchmark learned representations on the object detection task on +12 using Faster R-CNN and on the detection and instance segmentation task on COCO using Mask R-CNN. All methods use the C4 backbone variant and models on COCO are finetuned using the 1× schedule. Best results are in bold.

## Ablations

For all ablation studies, Barlow Twins was trained for 300 epochs instead of 1000 epochs in the previous section. A linear evaluation on ImageNet of this baseline model yielded a $71.4\%$ top-1 accuracy and a $90.2\%$ top-5 accuracy. For all the ablations presented we report the top-1 and top-5 accuracy of training linear classifiers on the $2048$ dimensional res5 features using the ImageNet train set.

### Loss Function Ablations

We alter our loss function (eqn. 1) in several ways to test the necessity of each term of the loss function, and to experiment with different practices popular in other loss functions for SSL, such as infoNCE. Table 5 recapitulates the different loss functions tested along with their results on a linear evaluation benchmark of Imagenet. First we find that removing the invariance term (on-diagonal term) or the redundancy reduction term (off-diagonal term) of our loss function leads to worse/collapsed solutions, as expected. We then study the effect of different normalization strategies. We first try to normalize the embeddings along the feature dimension so that they lie on the unit sphere, as it is common practice for losses measuring a cosine similarity. Specifically, we first normalize the embeddings along the batch dimension (with mean subtraction), then normalize the embeddings along the feature dimension (without mean subtraction), and finally we measure the (unnormalized) covariance matrix instead of the (normalized) cross-correlation matrix in eqn. 2. The performance is slightly reduced. Second, we try to remove batch-normalization operations in the two hidden layers of the projector network MLP. The performance is barely affected. Third, in addition to removing the batch-normalization in the hidden layers, we replace the cross-correlation matrix in eqn. 2 by the cross-covariance matrix (which means the features are no longer normalized along the batch dimension). The performance is substantially reduced. We finally try a cross-entropy loss with temperature, for which the on-diagonal term and off-diagonal term is controlled by a temperature hyperparameter $\tau$ and coefficient $\lambda$: $\mathcal{L} = {{- {\log{\sum_{i}{\exp{({\mathcal{C}_{ii}/\tau})}}}}} + {\lambda\log{\sum_{i}{\sum_{j \neq i}{\exp{({{\max{(\mathcal{C}_{ij},0)}}/\tau})}}}}}}$. The performance is reduced.

Only invariance term (on-diag term) Only red. red. term (off-diag term) Normalization along feature dim.

Cross-entropy with temp.

Table 5: Loss function explorations. We ablate the invariance and redundancy terms in our proposed loss and observe that both terms are necessary for good performance. We also experiment with different normalization schemes and a cross-entropy loss and observe reduced performance.

### Robustness to Batch Size

The infoNCE loss that draws negative examples from the minibatch suffer performance drops when the batch size is reduced (e.g. SimCLR ). We thus sought to test the robustness of Barlow Twins to small batch sizes. In order to adapt our model to different batch sizes, we performed a grid search on LARS learning rates for each batch size. We find that, unlike SimCLR, our model is robust to small batch sizes (Fig. 2), with a performance almost unaffected for a batch as small as 256. In comparison the accuracy for SimCLR drops about $4$ p.p. for batch size 256. This robustness to small batch size, also found in non-contrastive methods such as BYOL, further demonstrates that our method is not only conceptually (see Discussion) but also empirically different than the infoNCE objective.

Figure 2: Effect of batch size. To compare the effect of the batch size across methods, for each method we report the difference between the top-1 accuracy at a given batch size and the best obtained accuracy among all batch size tested. BYOL: best accuracy is 72.5% for a batch size of 4096 (data from fig. 3A). SimCLR: best accuracy is 67.1% for a batch size of 4096 (data from fig. 9, model trained for 300 epochs). Barlow Twins: best accuracy is 71.7% for a batch size of 1024.

### Effect of Removing Augmentations

We find that our model is not robust to removing some types of data augmentations, like SimCLR but unlike BYOL (Fig. 3). While this can be seen as a disadvantage of our method compared to BYOL, it can also be argued that the representations learned by our method are better controlled by the specific set of distortions used, as opposed to BYOL for which the invariances learned seem generic and intriguingly independent of the specific distortions used.

Figure 3: Effect of progressively removing data augmentations. Data for BYOL and SimCLR (repro) is from fig 3b.

### Projector Network Depth & Width

For other SSL methods, such as BYOL and SimCLR, the projector network drastically reduces the dimensionality of the ResNet output. In stark contrast, we find that Barlow Twins performs better when the dimensionality of the projector network output is very large. Other methods rapidly saturate when the dimensionality of the output increases, but our method keeps improving with all output dimensionality tested (Fig. 4). This result is quite surprising because the output of the ResNet is kept fixed to 2048, which acts as a dimensionality bottleneck in our model and sets the limit of the intrinsic dimensionality of the representation. In addition, similarly to other methods, we find that our model performs better when the projector network has more layers, with a saturation of the performance for 3 layers.

Figure 4: Effect of the dimensionality of the last layer of the projector network on performance. The parameter λ is kept fix for all dimensionalities tested. Data for SimCLR is from fig 8; Data for BYOL is from Table 14b.

### Breaking Symmetry

Many SSL methods (e.g. BYOL, SimSiam, SwAV) rely on different symmetry-breaking mechanisms to avoid trivial solutions. Our loss function avoids these trivial solutions by construction, even in the case of symmetric networks. It is however interesting to ask whether breaking symmetry can further improve the performance of our network. Following SimSiam and BYOL, we experiment with adding a predictor network composed of 2 fully connected layers of size 8192 to one of the network (with batch normalization followed by a ReLU nonlinearity in the hidden layer) and/or a stop-gradient mechanism on the other network. We find that these asymmetries slightly decrease the performance of our network (see Table 6).

Table 6: Effect of asymmetric settings BYOL with a larger projector/predictor/embedding For a fair comparison with BYOL, we also evaluated BYOL with a wider and/or deeper projector head (3-layer MLP), a wider and/or deeper predictor head, and a larger dimensionality of the embedding. BYOL did not improve under these conditions (see Table 7).

3 layer proj, 2 layer pred, 256-d repr.

3 layer proj, 3 layer pred, 256-d repr.

3 layer proj, 2 layer pred, 512-d repr.

3 layer proj, 3 layer pred, 512-d repr. same proj as BT, 2 layer pred, 8192-d repr.

Table 7: Wider and/or deeper projector and predictor heads and larger dimensionality of the embedding did not improve the performance of BYOL.

Sensitivity to $\lambda$. We also explored the sensitivity of Barlow Twins to the hyperparameter $\lambda$, which trades off the desiderata of invariance and informativeness of the embeddings. We find that Barlow Twins is not very sensitive to this hyperparameter (Fig. 5).

Figure 5: Sensitivity of Barlow Twins to the hyperparameter λ

## Discussion

Barlow Twins learns self-supervised representations through a joint embedding of distorted images, with an objective function that maximizes similarity between the embedding vectors while reducing redundancy between their components. Our method does not require large batches of samples, nor does it require any particular asymmetry in the twin network structure. We discuss next the similarities and differences between our method and prior art, both from a conceptual and an empirical standpoint. For ease of comparison, all objective functions are recast with a common set of notations. The discussion ends with future directions.

### Comparison with Prior Art

### infoNCE

The InfoNCE loss, where NCE stands for Noise-Contrastive Estimation, is a popular type of contrastive loss function used for self-supervised learning (e.g.). It can be instantiated as: where $z^{A}$ and $z^{B}$ are the twin network outputs, $b$ indexes the sample in a batch, $i$ indexes the vector component of the output, and $\tau$ is a positive constant called temperature in analogy to statistical physics.

For ready comparison, we rewrite Barlow Twins loss function with the same notations: Both Barlow Twins' and InfoNCE's objective functions have two terms, the first aiming at making the embeddings invariant to the distortions fed to the twin networks, the second aiming at maximizing the variability of the embedding learned. Another common point between the two losses is that they both rely on batch statistics to measure this variability. However, the InfoNCE objective maximizes the variability of the embeddings by maximizing the pairwise distance between all pairs of samples, whereas our method does so by decorrelating the components of the embeddings vectors.

The contrastive term in InfoNCE can be interpreted as a non-parametric estimation of the entropy of the distribution of embeddings. An issue that arises with non-parametric entropy estimators is that they are prone to the curse of dimensionality: they can only be estimated reliably in a low-dimensional setting, and they typically require a large number of samples.

In contrast, our loss can be interpreted as a *proxy* entropy estimator of the distribution of embeddings under *a Gaussian parametrization* (see Appendix A). Thanks to this simplified parametrization, the variability of the embedding can be estimated from much fewer samples, and on very large-dimensional embeddings. Indeed, in the ablation studies that we perform, we find that our method is robust to small batches unlike the popular InfoNCE-based method SimCLR, and our method benefits from using very large dimensional embeddings, unlike InfoNCE-based methods which do not see a benefit in increasing the dimensionality of the output.

Our loss presents several other interesting differences with infoNCE: In infoNCE, the embeddings are typically normalized along the feature dimension to compute a cosine similarity between embedded samples. We normalize the embeddings along the batch dimension instead.

In our method, there is a parameter $\lambda$ that trades off how much emphasis is put on the invariance term vs. the redundancy reduction term. This parameter can be interpreted as the trade-off parameter in the *Information Bottleneck* framework (see Appendix A). This parameter is not present in infoNCE. infoNCE also has a hyperparameter, the temperature, which can be interpreted as the width of the kernel in a non-parametric kernel density estimation of entropy, and practically weighs the relative importance of the hardest negative samples present in the batch.

A number of alternative methods to ours have been proposed to alleviate the reliance on large batches of the infoNCE loss. For example, MoCo builds a dynamic dictionary of negative samples with a queue and a moving-averaged encoder. This enables building a large and consistent dictionary on-the-fly that facilitates contrastive unsupervised learning. MoCo typically needs to store $> {60,000}$ sample embeddings. In contrast, our method does not require such a large dictionary, since it works well with a relatively small batch size (e.g. 256).

### Asymmetric Twins

Bootstrap-Your-Own-Latent (aka BYOL) and SimSiam are two recent methods which use a simple cosine similarity between twin embeddings as an objective function, without *any* contrastive term: Surprisingly, these methods successfully avoid trivial solutions by introducing some asymmetry in the architecture and learning procedure of the twin networks. For example, BYOL uses a predictor network which breaks the symmetry between the two networks, and also enforces an exponential moving average on the target network weights to slow down the progression of the weights on the target network. Combined together, these two mechanisms surprisingly avoid trivial solutions. The reasons behind this success are the subject of recent theoretical and empirical studies. In particular, the ablation study shows that the moving average is not necessary, but that stop-gradient on one of the branch and the presence of the predictor network are two crucial elements to avoid collapse. Other works show that batch normalization or alternatively group normalization could play an important role in avoiding collapse.

Like our method, these asymmetric methods do not require large batches, since in their case there is no interaction between batch samples in the objective function.

It should be noted however that these asymmetric methods cannot be described as the optimization of an overall learning objective. Instead, there exists trivial solutions to the learning objective that these methods avoid via particular implementation choices and/or the result of non-trivial learning dynamics. In contrast, our method avoids trivial solutions by construction, making our method conceptually simpler and more principled than these alternatives (until their principle is discovered, see for an early attempt).

### Whitening

In a concurrent work, propose W-MSE. Acting on the embeddings from identical twin networks, this method performs a differentiable whitening operation (via Cholesky decomposition) of each batch of embeddings before computing a simple cosine similarity between the whitened embeddings of the twin networks. In contrast, the redundancy reduction term in our loss encourages the whitening of the batch embeddings as a soft constraint. The current W-MSE model achieves 66.3% top-1 accuracy on the Imagenet linear evaluation benchmark. It is an interesting direction for future studies to determine whether improved versions of this hard-whitening strategy could also lead to state-of-the-art results on these large-scale computer vision benchmarks.

### Clustering

These methods, such as DeepCluster, SwAV, SeLa, perform contrastive-like comparisons without the requirement to compute all pairwise distances. Specifically, these methods simultaneously cluster the data while enforcing consistency between cluster assignments produced for different distortions of the same image, instead of comparing features directly as in contrastive learning. Clustering methods are also prone to collapse, *e.g*., empty clusters in k-means and avoiding them relies on careful implementation details. Online clustering methods like SwAV can be trained with large and small batches but require storing features when the number of clusters is much larger than the batch size. Clustering methods can also be combined with contrastive learning to prevent collapse.

### Noise As Targets

This method learns to map samples to fixed random targets on the unit sphere, which can be interpreted as a form of whitening. This objective uses a single network, and hence does not leverage the distortions induced by twin networks. Predefining random targets might limit the flexibility of the representation that can be learned.

### IMAX

In the early days of SSL, proposed a loss function between twin networks given: where $||$ denotes the determinant of a matrix, $\mathcal{C}_{({Z^{A} - Z^{B}})}$ is the covariance matrix of the difference of the outputs of the twin networks and $\mathcal{C}_{({Z^{A} + Z^{B}})}$ the covariance of the sum of these outputs. It can be shown that this objective maximizes the information between the twin network representations under the assumptions that the two representations are noisy versions of the same underlying Gaussian signal, and that the noise is independant, additive and Gaussian. This objective is similar to ours in the sense that there is one term that encourages the two representations to be similar and another term that encourages the units to be decorrelated. However, unlike IMAX, our objective is not directly an information quantity, and we have an extra trade-off parameter $\lambda$ that trades off the two terms of our loss. The IMAX objective was used in early work so it is not clear whether it can scale to large computer vision tasks. Our attempts to make it work on ImageNet were not successful.

### Future Directions

We observe a steady improvement of the performance of our method as we increase the dimensionality of the embeddings (i.e. of the last layer of the projector network). This intriguing result is in stark contrast with other popular methods for SSL, such as SimCLR and BYOL, for which increasing the dimensionality of the embeddings rapidly saturates performance. It is a promising avenue to continue this exploration for even higher dimensional embeddings ($> {16,000}$), but this would require the development of new methods or alternative hardware to accommodate the memory requirements of operating on such large embeddings.

Our method is just one possible instanciation of the *Information Bottleneck* principle applied to SSL. We believe that further refinements of the proposed loss function and algorithm could lead to more efficient solutions and even better performances. For example, the redundancy reduction term is currently computed from the off-diagonal terms of the cross-correlation matrix between the twin network embeddings, but alternatively it could be computed from the off-diagonal terms of the auto-correlation matrix of a single network's embedding. Our preliminary analyses seem to indicate that this alternative leads to similar performances (not shown). A modified loss could also be applied to the (unnormalized) cross-covariance matrix instead of the (normalized) cross-correlation matrix (see Ablations for preliminary analyses).
