<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

Topics include Self-supervised learning, Representation learning, Computer vision, VICReg, Variance regularization, Covariance regularization, Collapse prevention, Redundancy reduction, Non-contrastive learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

VICReg decomposes non-contrastive representation learning into three explicit pressures: make paired augmentations agree, keep each embedding dimension's variance above a floor, and reduce covariance between dimensions. The variance term makes collapse prevention direct rather than architectural, and the paper usefully separates invariance, information preservation, and redundancy reduction into interpretable regularizers that can also stabilize other SSL methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent self-supervised methods for image representation learning are based on maximizing the agreement between embedding vectors from different views of the same image. A trivial solution is obtained when the encoder outputs constant vectors. This collapse problem is often avoided through implicit biases in the learning architecture, that often lack a clear justification or interpretation. In this paper, we introduce VICReg (Variance-Invariance-Covariance Regularization), a method that explicitly avoids the collapse problem with a simple regularization term on the variance of the embeddings along each dimension individually. VICReg combines the variance term with a decorrelation mechanism based on redundancy reduction and covariance regularization, and achieves results on par with the state of the art on several downstream tasks. In addition, we show that incorporating our new variance term into other methods helps stabilize the training and leads to performance improvements.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-supervised representation learning has made significant progress over the last years, almost reaching the performance of supervised baselines on many downstream tasks Bachman et al.; Misra & Maaten; He et al.; Tian et al.; Caron et al.; Grill et al.; Chen & He; Gidaris et al.; Zbontar et al.. Several recent approaches rely on a joint embedding architecture in which two networks are trained to produce similar embeddings for different views of the same image. A popular instance is the Siamese network architecture Bromley et al., where the two networks share the same weights. The main challenge with joint embedding architectures is to prevent a collapse in which the two branches ignore the inputs and produce identical and constant output vectors. There are two main approaches to preventing collapse: contrastive methods and information maximization methods. Contrastive Bromley et al.; Chopra et al.; He et al.; Hjelm et al.; Chen et al. methods tend to be costly, require large batch sizes or memory banks, and use a loss that explicitly pushes the embeddings of dissimilar images away from each other.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

They often require a mining procedure to search for offending dissimilar samples from a memory bank He et al. or from the current batch Chen et al.. Quantization-based approaches Caron et al. force the embeddings of different samples to belong to different clusters on the unit sphere. Collapse is prevented by ensuring that the assignment of samples to clusters is as uniform as possible. A similarity term encourages the cluster assignment score vectors from the two branches to be similar. More recently, a few methods have appeared that do not rely on contrastive samples or vector quantization, yet produce high-quality representations, for example BYOL Grill et al. and SimSiam Chen & He. They exploit several tricks: batch-wise or feature-wise normalization, a \"momentum encoder\" in which the parameter vector of one branch is a low-pass-filtered version of the parameter vector of the other branch Grill et al.; Richemond et al., or a stop-gradient operation in one of the branches Chen & He.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The dynamics of learning in these methods, and how they avoid collapse, is not fully understood, although theoretical and empirical studies point to the crucial importance of batch-wise or feature-wise normalization Richemond et al.; Tian et al.. Finally, an alternative class of collapse prevention methods relies on maximizing the information content of the embedding Zbontar et al.; Ermolov et al.. These methods prevent informational collapse by decorrelating every pair of variables of the embedding vectors. This indirectly maximizes the information content of the embedding vectors. The Barlow Twins method drives the normalized cross-correlation matrix of the two embeddings towards the identity Zbontar et al., while the Whitening-MSE method whitens and spreads out the embedding vectors on the unit sphere Ermolov et al..

<!-- chunk {"id": "body-0007", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

We introduce VICReg (Variance-Invariance-Covariance Regularization), a self-supervised method for training joint embedding architectures based on the principle of preserving the information content of the embeddings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

Invariance: the mean square distance between the embedding vectors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

Variance: a hinge loss to maintain the standard deviation (over a batch) of each variable of the embedding above a given threshold. This term forces the embedding vectors of samples within a batch to be different.

<!-- chunk {"id": "body-0010", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

Covariance: a term that attracts the covariances (over a batch) between every pair of (centered) embedding variables towards zero. This term decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated.

<!-- chunk {"id": "body-0011", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

Variance and Covariance terms are applied to both branches of the architecture separately, thereby preserving the information content of each embedding at a certain level and preventing informational collapse independently for the two branches. The main contribution of this paper is the Variance preservation term, which explicitly prevents a collapse due to a shrinkage of the embedding vectors towards zero. The Covariance criterion is borrowed from the Barlow Twins method and prevents informational collapse due to redundancy between the embedding variables Zbontar et al.. VICReg is more generally applicable than most of the aforementioned methods because of fewer constraints on the architecture.

<!-- chunk {"id": "body-0012", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

does not require that the weights of the two branches be shared, not that the architectures be identical, nor that the inputs be of the same nature;

<!-- chunk {"id": "body-0013", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

does not require a memory bank, nor contrastive samples, nor a large batch size;

<!-- chunk {"id": "body-0014", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

does not require batch-wise nor feature-wise normalization; and

<!-- chunk {"id": "body-0015", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

does not require vector quantization nor a predictor module.

<!-- chunk {"id": "body-0016", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

Other methods require asymmetric stop gradient operations, as in SimSiam Chen & He, weight sharing between the two branches as in classical Siamese nets, or weight sharing through exponential moving average dampening with stop gradient in one branch, as in BYOL and MoCo He et al.; Grill et al.; Chen et al., large batches of contrastive samples, as in SimCLR Chen et al., or batch-wise and/or feature-wise normalization Caron et al.; Grill et al.; Chen & He; Zbontar et al.; Ermolov et al.. One of the most interesting feature of VICReg is the fact that the two branches are not required to share the same parameters, architecture, or input modality. This opens the door to the use of non-contrastive self-supervised joint-embedding for multi-modal signals, such as video and audio. We demonstrate the effectiveness of the proposed approach by evaluating the representations learned with VICReg on several downstream image recognition tasks including linear head and semi-supervised evaluation protocols for image classification on ImageNet Deng et al., and other classification, detection, instance segmentation, and retrieval tasks.

<!-- chunk {"id": "body-0017", "role": "body", "section": "VICReg: intuition", "weight": 1.0} -->

Furthermore, we show that incorporating variance preservation into other self-supervised joint-embedding methods yields better training stability and performance improvement on downstream tasks. More generally, we show that VICReg is an explicit and effective, yet simple method for preventing collapse in self-supervised joint-embedding learning.

<!-- chunk {"id": "body-0018", "role": "body", "section": "VICReg: detailed description", "weight": 1.0} -->

VICReg follows recent trends in self-supervised learning Caron et al.; Grill et al.; Chen & He; Zbontar et al.; Chen et al. and is based on a joint embedding architecture. Contrary to many previous approaches, our architecture may be completely symmetric or completely asymmetric with no shared structure or parameters between the two branches. In most of our experiments, we use a Siamese net architecture in which the two branches are identical and share weights. Each branch consists of an encoder $f_{\theta}$ that outputs the representations (used for downstream tasks), followed by an expander $h_{\phi}$ that maps the representations into an embedding space where the loss function will be computed. The role of the expander is twofold: eliminate the information by which the two representations differ, expand the dimension in a non-linear fashion so that decorrelating the embedding variables will reduce the dependencies (not just the correlations) between the variables of the representation vector.

<!-- chunk {"id": "body-0019", "role": "body", "section": "VICReg: detailed description", "weight": 1.0} -->

The loss function uses a term $s$ that learns invariance to data transformations and is regularized with a variance term $v$ that prevents norm collapse and a covariance term $c$ that prevents informational collapse by decorrelating the different dimensions of the vectors. After pretraining, the expander is discarded and the representations of the encoder are used for downstream tasks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method", "weight": 1.0} -->

Given an image $i$ sampled from a dataset $\mathcal{D}$, two transformations $t$ and $t^{\prime}$ are sampled from a distribution $\mathcal{T}$ to produce two different views $x = {t{(i)}}$ and $x^{\prime} = {t^{\prime}{(i)}}$ of $i$. These transformations are random crops of the image, followed by color distortions. The distribution $\mathcal{T}$ is described in Appendix C.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Method", "weight": 1.0} -->

We describe here the variance, invariance and covariance terms that compose our loss function. The images are processed in batches, and we denote $Z = {\lbrack z_{1},\ldots,z_{n}\rbrack}$ and $Z^{\prime} = {\lbrack z_{1}^{\prime},\ldots,z_{n}^{\prime}\rbrack}$ the two batches composed of $n$ vectors of dimension $d$, of embeddings coming out of the two branches of the siamese architecture. We denote by $z^{j}$ the vector composed of each value at dimension $j$ in all vectors in $Z$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method", "weight": 1.0} -->

$\gamma$ is a constant target value for the standard deviation, fixed to $1$ in our experiments, $\epsilon$ is a small scalar preventing numerical instabilities. This criterion encourages the variance inside the current batch to be equal to $\gamma$ along each dimension, preventing collapse with all the inputs mapped on the same vector. Using the standard deviation and not directly the variance is crucial. Indeed, if we take ${S{(x)}} = {{Var}{(x)}}$ in the hinge function, the gradient of $S$ with respect to $x$ becomes close to 0 when $x$ is close to $\overline{x}$. In this case, the gradient of $v$ also becomes close to 0 and the embeddings collapse.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

This term encourages the off-diagonal coefficients of $C{(Z)}$ to be close to $0$, decorrelating the different dimensions of the embeddings and preventing them from encoding similar information. Decorrelation at the embedding level ultimately has a decorrelation effect at the representation level, which is a non trivial phenomenon that we study in Appendix D.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

where $\lambda$, $\mu$ and $\nu$ are hyper-parameters controlling the importance of each term in the loss. In our experiments, we set $\nu = 1$ and perform a grid search on the values of $\lambda$ and $\mu$ with the base condition $\lambda = \mu > 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

where $Z^{I}$ and $Z^{\prime I}$ are the batches of embeddings corresponding to the batch of images $I$ transformed by $t$ and $t^{\prime}$. The objective is minimized for several epochs, over the encoder parameters $\theta$ and expander parameters $\phi$. We illustrate the architecture and loss function of VICReg in Figure 1.\

<!-- chunk {"id": "body-0026", "role": "body", "section": "Implementation details", "weight": 1.0} -->

Implementation details for pretraining with VICReg on the 1000-classes ImagetNet dataset without labels are as follows. Coefficients $\lambda$ and $\mu$ are $25$ and $\nu$ is 1 in Eq., and $\epsilon$ is $0.0001$ in Eq.. We give more details on how we choose the coefficients of the loss function in Appendix D.4. The encoder network $f_{\theta}$ is a standard ResNet-50 backbone He et al. with 2048 output units. The expander $h_{\phi}$ is composed of two fully-connected layers with batch normalization (BN) Ioffe & Szegedy and ReLU, and a third linear layer. The sizes of all 3 layers were set to 8192. As with Barlow Twins, performance improves when the size of the expander layers is larger than the dimension of the representation. The impact of the expander dimension on performance is studied in Appendix D.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Implementation details", "weight": 1.0} -->

The training protocol follows those of BYOL and Barlow Twins: LARS optimizer You et al.; Goyal et al. run for 1000 epochs with a weight decay of $10^{- 6}$ and a learning rate ${lr} = {{{{batch\_size}/256} \times b}ase\_lr}$, where $batch\_size$ is set to $2048$ by default and $base\_lr$ is a base learning rate set to $0.2$. The learning rate follows a cosine decay schedule Loshchilov & Hutter, starting from $0$ with $10$ warmup epochs and with final value of $0.002$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we evaluate the representations obtained after self-supervised pretraining of a ResNet-50 He et al. backbone with VICReg during 1000 epochs, on the training set of ImageNet, using the training protocol described in section 4. We also pretrain on pairs of image and text data and evaluate on retrieval tasks on the MS-COCO dataset.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluation on ImageNet", "weight": 1.0} -->

Following the ImageNet Deng et al. linear evaluation protocol, we train a linear classifier on top of the frozen representations of the ResNet-50 backbone pretrained with VICReg. We also evaluate the performance of the backbone when fine-tuned with a linear classifier on a subset of ImageNet's training set using 1% or 10% of the labels, using the split of Chen et al.. We give implementation details about the optimization procedure for these tasks in Appendix C. We have applied the training procedure described in section 4 with three different random initialization. The numbers reported in Table 1 for VICReg are the mean scores, and we have observed that the difference between worse and best run is lower than 0.1% accuracy for linear classification, which shows that VICReg is a very stable algorithm. Lack of time has prevented us from doing the same for the semi-supervised classification experiments, and the experiments of section 5.2 and 6, but we expect similar conclusion to hold. We compare in Table 1 our results on both tasks against other methods on the validation set of ImageNet.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluation on ImageNet", "weight": 1.0} -->

The performance of VICReg is on par with the state of the art without using the negative pairs of SimCLR, the clusters of SwAV, the bag-of-words representations of OBoW, or any asymmetric networks architectural tricks such as the momentum encoder of BYOL and the stop-gradient operation of SimSiam. The performance is comparable to that of Barlow Twins, which shows that VICReg's more explicit way of constraining the variance and comparing views has the same power than maximizing cross-correlations between pairs of twin dimensions. The main advantage of VICReg is the modularity of its objective function and the applicability to multi-modal setups.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Transfer to other downstream tasks", "weight": 1.0} -->

Following the setup from Misra & Maaten, we train a linear classifier on top of the frozen representations learnt by our pretrained ResNet-50 backbone on a variety of different datasets: the Places205 Zhou et al. scene classification dataset, the Everingham et al. multi-label image classification dataset and the iNaturalist2018 Horn et al. fine-grained image classification dataset. We then evaluate the quality of the representations by transferring to other vision tasks including +12 Everingham et al. object detection using Faster R-CNN Ren et al. with a R50-C4 backbone, and COCO Lin et al. instance segmentation using Mask-R-CNN He et al. with a R50-FPN backbone. We report the performance in Table 2, VICReg performs on par with most concurrent methods, and better than Barlow Twins, across all classification tasks, but is slightly behind the top-3 on detection tasks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Multi-modal pretraining on MS-COCO", "weight": 1.0} -->

One fundamental difference of VICReg compared to Barlow Twins is the way the branches are regularized. In VICReg, both branches are regularized independently, as the covariance term is applied on each branch separately, which works better in the scenarios where the branches are completely different, have different types of architecture and process different types of data. Indeed, the statistics of the output of the two branches can be very different, and the amount of regularization required for each may vary a lot. In Barlow Twins, the regularization is applied on the cross-correlation matrix, which favors the scenarios where the branches produce outputs with similar statistics. We demonstrate the capabilities of VICReg in a multi-modal experiment where we pretrain on pairs of images and corresponding captions on the MS-COCO dataset. We regularize each branch with a different coefficient, which is not possible with Barlow Twins, and we show that VICReg outperforms Barlow Twins on image and text retrieval downstream tasks. Table 3 reports the performance of VICReg against the contrastive loss proposed by VSE++ Faghri et al., and against Barlow Twins, in the identical setting proposed in Faghri et al..

<!-- chunk {"id": "body-0033", "role": "body", "section": "Multi-modal pretraining on MS-COCO", "weight": 1.0} -->

VICReg outperforms the two by a significant margin.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this section we study how the different components of our method contribute to its performance, as well as how they interact with components from other self-supervised methods. We also evaluate different scenarios where the branches have different weights and architecture. All reported results are obtained on the linear evaluation protocol, using a ResNet-50 backbone if not mentioned otherwise, and 100 epochs of pretraining, which gives results consistent with those obtained with 1000 epochs of pretraining. The optimization setting used for each experiment is described in Appendix C.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Analysis", "weight": 1.0} -->

Asymmetric networks. We study the impact of different components used in asymmetric architectures and the effects of adding variance and covariance regularization, in terms of performance and training stability. Starting from a simple symmetric architecture with an encoder and an expander without batch normalization, which correspond to VICReg without batch normalization in the expander, we progressively add batch normalization in the inner layers of the expander, a predictor, a stop-gradient operation and a momentum encoder. We use the training protocol and architecture of SimSiam Chen & He when a stop-gradient is used and the training protocol and architecture of BYOL Grill et al. when a momentum encoder is used. The predictor as used in SimSiam and BYOL is a learnable module $g_{\psi}$ that predicts the embedding of a view given the embedding of the other view of the same image.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis", "weight": 1.0} -->

If $z$ and $z^{\prime}$ are the embeddings of two views of an image, then $p = {g_{\psi}{(z)}}$ and $p^{\prime} = {g_{\psi}{(z^{\prime})}}$ are the predictions of each view. The invariance loss function of Eq.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis", "weight": 1.0} -->

where $D$ is a distance function that depends on the method used. BYOL uses the mean square error between $l_{2}$-normalized vectors, SimSiam uses the negative cosine similarity loss and VICReg uses the mean square error without $l_{2}$-normalization. The variance and covariance terms are regularizing the output $Z$ and $Z^{\prime}$ of the expander, which we empirically found to work better than regularizing the output of the predictor. We compare different settings in Table 4, based on the default data augmentation, optimization and architecture settings of the original BYOL, SimSiam and VICReg methods. In all settings, the absence of BN indicates that BN is also removed in the predictor when one is used.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis", "weight": 1.0} -->

We analyse first the impact of variance regularization (VR) in the different settings. When using VR, adding a predictor (PR) to VICReg does not lead to a significant change of the performance, which indicates that PR is redundant with VR. In comparison, without VR, the representations collapse, and both stop-gradient (SG) and PR are necessary. Batch normalization in the inner layers of the expander (BN) in VICReg leads to a 1.0% increase in the performance, which is not a big improvement considering that SG and PR without BN is performing very poorly at 35.1%.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analysis", "weight": 1.0} -->

Finally, incorporating VR with SG or ME further improves the performance by small margins of respectively 0.2% and 0.9%, which might be explained by the fact that these architectural tricks that prevent collapse are not perfectly maintaining the variance of the representations, i.e. very slow collapse is happening with these methods. We explain this intuition by studying the evolution of the standard deviation of the representations during pretraining for BYOL and SimSiam in Appendix D. We then analyse the impact of adding additional covariance regularization (CR) in the different settings, along with variance regularization. We found that optimization with SG and CR is hard, even if our analysis of the average correlation coefficient of the representations during pretraining in Appendix D shows that both fulfill the same objective.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Analysis", "weight": 1.0} -->

The performance of BYOL and SimSiam slightly drops compared to VR only, except when PR is removed, where SG becomes useless. BN is still useful and improves the performance by 1.3%. Finally with CR, PR does not harm the performance and even improves it by a very small margin. VICReg+PR with 1000 epochs of pretraining exactly matches the score of VICReg (73.2% on linear classification).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Analysis", "weight": 1.0} -->

Weight sharing. Contrary to most self-supervised learning approaches based on Siamese architectures, VICReg has several unique properties: weights do not need to be shared between the branches, each branch's weights are updated independently of the other branch's weights; the branches are regularized independently, the variance and covariance terms are computed on each branch individually; no predictor is necessary unlike with methods where one branch predicts outputs of the other branch. We compare the robustness of VICReg against other methods in different scenarios where the weights of the branches can be shared (SW), not shared (DW), and where the encoders can have different architectures (DA). Among other self-supervised methods, SimCLR and Barlow Twins are the only ones that can handle these scenarios. The asymmetric methods that are based on a discrepancy between the branches requires either the architecture or the weights to be shared between the branches. The performance drops by 2.1% with VICReg and 4.5% with Barlow Twins, between the shared weights scenario (SW) and the different weight scenario (DW).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Analysis", "weight": 1.0} -->

The difference between VICReg and Barlow Twins is also significant in scenarios with different architectures, in particular VICReg performs better than Barlow Twins by 2.8% with ResNet-50/ResNet-101 and better by 2.3% with ResNet-50/ViT-S Dosovitskiy et al.. This shows that VICReg is more robust than Barlow Twins in these kind of scenarios. The performance of SimCLR remains stable across scenarios, but is significantly worse than the performance of VICReg. Importantly, the ability of VICReg to function with different parameters, architectures, and input modalities for the branches widens the applicability to joint-embedding SSL to many applications, including multi-modal signals.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced VICReg, a simple approach to self-supervised learning based on a triple objective: learning invariance to different views with a invariance term, avoiding collapse of the representations with a variance preservation term, and maximizing the information content of the representation with a covariance regularization term. VICReg achieves results on par with the state of the art on many downstream tasks, but is not subject to the same limitations as most other methods, particularly because it does not require the embedding branches to be identical or even similar.
