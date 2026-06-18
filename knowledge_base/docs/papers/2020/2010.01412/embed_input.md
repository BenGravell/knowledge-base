<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sharpness-Aware Minimization for Efficiently Improving Generalization

Topics include Gradient descent, Robustness, Datasets, Benchmarks, Generalization, Optimization, Learning, SAM, Sharpness-aware minimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In today's heavily overparameterized models, the value of the training loss provides few guarantees on model generalization ability. Indeed, optimizing only the training loss value, as is commonly done, can easily lead to suboptimal model quality. Motivated by prior work connecting the geometry of the loss landscape and generalization, we introduce a novel, effective procedure for instead simultaneously minimizing loss value and loss sharpness. In particular, our procedure, Sharpness-Aware Minimization (SAM), seeks parameters that lie in neighborhoods having uniformly low loss; this formulation results in a min-max optimization problem on which gradient descent can be performed efficiently. We present empirical results showing that SAM improves model generalization across a variety of benchmark datasets (e.g., CIFAR-10, CIFAR-100, ImageNet, finetuning tasks) and models, yielding novel state-of-the-art performance for several. Additionally, we find that SAM natively provides robustness to label noise on par with that provided by state-of-the-art procedures that specifically target learning with noisy labels. We open source our code .

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern machine learning's success in achieving ever better performance on a wide range of tasks has relied in significant part on ever heavier overparameterization, in conjunction with developing ever more effective training algorithms that are able to find parameters that generalize well. Indeed, many modern neural networks can easily memorize the training data and have the capacity to readily overfit. Such heavy overparameterization is currently required to achieve state-of-the-art results in a variety of domains. In turn, it is essential that such models be trained using procedures that ensure that the parameters actually selected do in fact generalize beyond the training set.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, simply minimizing commonly used loss functions (e.g., cross-entropy) on the training set is typically not sufficient to achieve satisfactory generalization. The training loss landscapes of today's models are commonly complex and non-convex, with a multiplicity of local and global minima, and with different global minima yielding models with different generalization abilities. As a result, the choice of optimizer (and associated optimizer settings) from among the many available (e.g., stochastic gradient descent, Adam, RMSProp (Hinton et al., ), and others ) has become an important design choice, though understanding of its relationship to model generalization remains nascent. Relatedly, a panoply of methods for modifying the training process have been proposed, including dropout, batch normalization, stochastic depth, data augmentation, and mixed sample augmentations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The connection between the geometry of the loss landscape---in particular, the flatness of minima---and generalization has been studied extensively from both theoretical and empirical perspectives. While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see; we include a more detailed discussion of prior work in Section 5).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present here a new efficient, scalable, and effective approach to improving model generalization ability that directly leverages the geometry of the loss landscape and its connection to generalization, and is powerfully complementary to existing techniques.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Sharpness-Aware Minimization (SAM), a novel procedure that improves model generalization by simultaneously minimizing loss value and loss sharpness. SAM functions by seeking parameters that lie in neighborhoods having uniformly low loss value (rather than parameters that only themselves have low loss value, as illustrated in the middle and righthand images of Figure 1), and can be implemented efficiently and easily.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show via a rigorous empirical study that using SAM improves model generalization ability across a range of widely studied computer vision tasks (e.g., CIFAR-{10, 100}, ImageNet, finetuning tasks) and models, as summarized in the lefthand plot of Figure 1. For example, applying SAM yields novel state-of-the-art performance for a number of already-intensely-studied tasks, such as ImageNet, CIFAR-{10, 100}, SVHN, Fashion-MNIST, and the standard set of image classification finetuning tasks (e.g., Flowers, Stanford Cars, Oxford Pets, etc).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that SAM furthermore provides robustness to label noise on par with that provided by state-of-the-art procedures that specifically target learning with noisy labels.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through the lens provided by SAM, we further elucidate the connection between loss sharpness and generalization by surfacing a promising new notion of sharpness, which we term m-sharpness.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 2 below derives the SAM procedure and presents the resulting algorithm in full detail. Section 3 evaluates SAM empirically, and Section 4 further analyzes the connection between loss sharpness and generalization through the lens of SAM. Finally, we conclude with an overview of related work and a discussion of conclusions and future work in Sections 5 and 6, respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sharpness-Aware Minimization (SAM)", "weight": 1.0} -->

Utilizing $L_{\mathcal{S}}{({\mathbf{w}})}$ as an estimate of $L_{\mathcal{D}}{({\mathbf{w}})}$ motivates the standard approach of selecting parameters $\mathbf{w}$ by solving ${\min_{\mathbf{w}}L_{\mathcal{S}}}{({\mathbf{w}})}$ (possibly in conjunction with a regularizer on $\mathbf{w}$) using an optimization procedure such as SGD or Adam. Unfortunately, however, for modern overparameterized models such as deep neural networks, typical optimization approaches can easily result in suboptimal performance at test time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sharpness-Aware Minimization (SAM)", "weight": 1.0} -->

In particular, for modern models, $L_{\mathcal{S}}{({\mathbf{w}})}$ is typically non-convex in $\mathbf{w}$, with multiple local and even global minima that may yield similar values of $L_{\mathcal{S}}{({\mathbf{w}})}$ while having significantly different generalization performance (i.e., significantly different values of $L_{\mathcal{D}}{({\mathbf{w}})}$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sharpness-Aware Minimization (SAM)", "weight": 1.0} -->

Motivated by the connection between sharpness of the loss landscape and generalization, we propose a different approach: rather than seeking out parameter values $\mathbf{w}$ that simply have low training loss value $L_{\mathcal{S}}{({\mathbf{w}})}$, we seek out parameter values whose entire neighborhoods have uniformly low training loss value (equivalently, neighborhoods having both low loss and low curvature).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Empirical Evaluation", "weight": 1.0} -->

In order to assess SAM's efficacy, we apply it to a range of different tasks, including image classification from scratch (including on CIFAR-10, CIFAR-100, and ImageNet), finetuning pretrained models, and learning with noisy labels. In all cases, we measure the benefit of using SAM by simply replacing the optimization procedure used to train existing models with SAM, and computing the resulting effect on model generalization. As seen below, SAM materially improves generalization performance in the vast majority of these cases.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

We first evaluate SAM's impact on generalization for today's state-of-the-art models on CIFAR-10 and CIFAR-100 (without pretraining): WideResNets with ShakeShake regularization and PyramidNet with ShakeDrop regularization. Note that some of these models have already been heavily tuned in prior work and include carefully chosen regularization schemes to prevent overfitting; therefore, significantly improving their generalization is quite non-trivial. We have ensured that our implementations' generalization performance in the absence of SAM matches or exceeds that reported in prior work

<!-- chunk {"id": "body-0017", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

All results use basic data augmentations (horizontal flip, padding by four pixels, and random crop). We also evaluate in the setting of more advanced data augmentation methods such as cutout regularization and AutoAugment, which are utilized by prior work to achieve state-of-the-art results.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

SAM has a single hyperparameter $\rho$ (the neighborhood size), which we tune via a grid search over $\{ 0.01,0.02,0.05,0.1,0.2,0.5\}$ using 10% of the training set as a validation set^33^3We found $\rho = 0.05$ to be a solid default value, and we report in appendix C.3 the scores for all our experiments, obtained with $\rho = 0.05$ without further tuning.. Please see appendix C.1 for the values of all hyperparameters and additional training details.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

As each SAM weight update requires two backpropagation operations (one to compute $\hat{\mathbf{\epsilon}}{({\mathbf{w}})}$ and another to compute the final gradient), we allow each non-SAM training run to execute twice as many epochs as each SAM training run, and we report the best score achieved by each non-SAM training run across either the standard epoch count or the doubled epoch count^44^4Training for longer generally did not improve accuracy significantly, except for the models previously trained for only 200 epochs and for the largest, most regularized model (PyramidNet + ShakeDrop).. We run five independent replicas of each experimental condition for which we report results (each with independent weight initialization and data shuffling), reporting the resulting mean error (or accuracy) on the test set, and the associated 95% confidence interval.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

Our implementations utilize JAX, and we train all models on a single host having 8 NVidia V100 GPUs^55^5Because SAM's performance is amplified by not syncing the perturbations, data parallelism is highly recommended to leverage SAM's full potential (see Section 4 for more details).. To compute the SAM update when parallelizing across multiple accelerators, we divide each data batch evenly among the accelerators, independently compute the SAM gradient on each accelerator, and average the resulting sub-batch SAM gradients to obtain the final SAM update.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

As seen in Table 1, SAM improves generalization across all settings evaluated for CIFAR-10 and CIFAR-100. For example, SAM enables a simple WideResNet to attain 1.6% test error, versus 2.2% error without SAM. Such gains have previously been attainable only by using more complex model architectures (e.g., PyramidNet) and regularization schemes (e.g., Shake-Shake, ShakeDrop); SAM provides an easily-implemented, model-independent alternative. Furthermore, SAM delivers improvements even when applied atop complex architectures that already use sophisticated regularization: for instance, applying SAM to a PyramidNet with ShakeDrop regularization yields 10.3% error on CIFAR-100, which is, to our knowledge, a new state-of-the-art on this dataset without the use of additional data.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

Beyond CIFAR-{10, 100}, we have also evaluated SAM on the SVHN and Fashion-MNIST datasets. Once again, SAM enables a simple WideResNet to achieve accuracy at or above the state-of-the-art for these datasets: 0.99% error for SVHN, and 3.59% for Fashion-MNIST. Details are available in appendix B.1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

To assess SAM's performance at larger scale, we apply it to ResNets of different depths trained on ImageNet. In this setting, following prior work, we resize and crop images to 224-pixel resolution, normalize them, and use batch size 4096, initial learning rate 1.0, cosine learning rate schedule, SGD optimizer with momentum 0.9, label smoothing of 0.1, and weight decay 0.0001. When applying SAM, we use $\rho = 0.05$ (determined via a grid search on ResNet-50 trained for 100 epochs). We train all models on ImageNet for up to 400 epochs using a Google Cloud TPUv3 and report top-1 and top-5 test error rates for each experimental condition (mean and 95% confidence interval across 5 independent runs).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Image Classification From Scratch", "weight": 1.0} -->

As seen in Table 2, SAM again consistently improves performance, for example improving the ImageNet top-1 error rate of ResNet-152 from 20.3% to 18.4%. Furthermore, note that SAM enables increasing the number of training epochs while continuing to improve accuracy without overfitting. In contrast, the standard training procedure (without SAM) generally significantly overfits as training extends from 200 to 400 epochs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Finetuning", "weight": 1.0} -->

Transfer learning by pretraining a model on a large related dataset and then finetuning on a smaller target dataset of interest has emerged as a powerful and widely used technique for producing high-quality models for a variety of different tasks. We show here that SAM once again offers considerable benefits in this setting, even when finetuning extremely large, state-of-the-art, already high-performing models.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Finetuning", "weight": 1.0} -->

In particular, we apply SAM to finetuning EfficentNet-b7 (pretrained on ImageNet) and EfficientNet-L2 (pretrained on ImageNet plus unlabeled JFT; input resolution 475). We initialize these models to publicly available checkpoints^66^6 trained with RandAugment (84.7% accuracy on ImageNet) and NoisyStudent (88.2% accuracy on ImageNet), respectively. We finetune these models on each of several target datasets by training each model starting from the aforementioned checkpoint; please see the appendix for details of the hyperparameters used. We report the mean and 95% confidence interval of top-1 test error over 5 independent runs for each dataset.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Finetuning", "weight": 1.0} -->

As seen in Table 3, SAM uniformly improves performance relative to finetuning without SAM. Furthermore, in many cases, SAM yields novel state-of-the-art performance, including 0.30% error on CIFAR-10, 3.92% error on CIFAR-100, and 11.39% error on ImageNet.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robustness to Label Noise", "weight": 1.0} -->

The fact that SAM seeks out model parameters that are robust to perturbations suggests SAM's potential to provide robustness to noise in the training set (which would perturb the training loss landscape). Thus, we assess here the degree of robustness that SAM provides to label noise.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Robustness to Label Noise", "weight": 1.0} -->

In particular, we measure the effect of applying SAM in the classical noisy-label setting for CIFAR-10, in which a fraction of the training set's labels are randomly flipped; the test set remains unmodified (i.e., clean). To ensure valid comparison to prior work, which often utilizes architectures specialized to the noisy-label setting, we train a simple model of similar size (ResNet-32) for 200 epochs, following Jiang et al.. We evaluate five variants of model training: standard SGD, SGD with Mixup, SAM, and "bootstrapped" variants of SGD with Mixup and SAM (wherein the model is first trained as usual and then retrained from scratch on the labels predicted by the initially trained model). When applying SAM, we use $\rho = 0.1$ for all noise levels except 80%, for which we use $\rho = 0.05$ for more stable convergence. For the Mixup baselines, we tried all values of $\alpha \in {\{ 1,8,16,32\}}$ and conservatively report the best score for each noise level.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Robustness to Label Noise", "weight": 1.0} -->

As seen in Table 4, SAM provides a high degree of robustness to label noise, on par with that provided by state-of-the art procedures that specifically target learning with noisy labels. Indeed, simply training a model with SAM outperforms all prior methods specifically targeting label noise robustness, with the exception of MentorMix. However, simply bootstrapping SAM yields performance comparable to that of MentorMix (which is substantially more complex).

<!-- chunk {"id": "body-0031", "role": "body", "section": "$m$-sharpness", "weight": 1.0} -->

Though our derivation of SAM defines the SAM objective over the entire training set, when utilizing SAM in practice, we compute the SAM update per-batch (as described in Algorithm 1 ‣ Sharpness-Aware Minimization for Efficiently Improving Generalization")) or even by averaging SAM updates computed independently per-accelerator (where each accelerator receives a subset of size $m$ of a batch, as described in Section 3). This latter setting is equivalent to modifying the SAM objective (equation 1 ‣ Sharpness-Aware Minimization for Efficiently Improving Generalization")) to sum over a set of independent $\epsilon$ maximizations, each performed on a sum of per-data-point losses on a disjoint subset of $m$ data points, rather than performing the $\epsilon$ maximization over a global sum over the training set (which would be equivalent to setting $m$ to the total training set size). We term the associated measure of sharpness of the loss landscape $m$-sharpness.

<!-- chunk {"id": "body-0032", "role": "body", "section": "$m$-sharpness", "weight": 1.0} -->

To better understand the effect of $m$ on SAM, we train a small ResNet on CIFAR-10 using SAM with a range of values of $m$. As seen in Figure 3 (middle), smaller values of $m$ tend to yield models having better generalization ability. This relationship fortuitously aligns with the need to parallelize across multiple accelerators in order to scale training for many of today's models.

<!-- chunk {"id": "body-0033", "role": "body", "section": "$m$-sharpness", "weight": 1.0} -->

Intriguingly, the $m$-sharpness measure described above furthermore exhibits better correlation with models' actual generalization gaps as $m$ decreases, as demonstrated by Figure 3 (right)^77^7We follow the rigorous framework of Jiang et al., reporting the mutual information between the $m$-sharpness measure and generalization on the two publicly available tasks from the Predicting generalization in deep learning NeurIPS2020 competition. In particular, this implies that $m$-sharpness with $m < n$ yields a better predictor of generalization than the full-training-set measure suggested by Theorem 1 in Section 2 above, suggesting an interesting new avenue of future work for understanding generalization.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hessian Spectra", "weight": 1.0} -->

Motivated by the connection between geometry of the loss landscape and generalization, we constructed SAM to seek out minima of the training loss landscape having both low loss value and low curvature (i.e., low sharpness). To further confirm that SAM does in fact find minima having low curvature, we compute the spectrum of the Hessian for a -10 trained on CIFAR-10 for 300 steps both with and without SAM (without batch norm, which tends to obscure interpretation of the Hessian), at different epochs during training. Due to the parameter space's dimensionality, we approximate the Hessian spectrum using the Lanczos algorithm of Ghorbani et al..

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

In this work, we have introduced SAM, a novel algorithm that improves generalization by simultaneously minimizing loss value and loss sharpness; we have demonstrated SAM's efficacy through a rigorous large-scale empirical evaluation. We have surfaced a number of interesting avenues for future work. On the theoretical side, the notion of per-data-point sharpness yielded by $m$-sharpness (in contrast to global sharpness computed over the entire training set, as has typically been studied in the past) suggests an interesting new lens through which to study generalization. Methodologically, our results suggest that SAM could potentially be used in place of Mixup in robust or semi-supervised methods that currently rely on Mixup (giving, for instance, MentorSAM). We leave to future work a more in-depth investigation of these possibilities.
