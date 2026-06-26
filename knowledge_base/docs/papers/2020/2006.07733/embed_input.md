<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning

Topics include Self-supervised learning, Representation learning, Computer vision, BYOL, Bootstrap learning, Non-contrastive learning, Momentum target network, ImageNet, Transfer learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

BYOL shows that strong image representations can be learned without explicit negative pairs by training an online network to predict the representation of a slowly averaged target network under a different augmentation. The paper is a key non-contrastive self-supervised learning result: its empirical strength forced later work to explain why collapse is avoided and made target-network bootstrapping a standard design pattern for vision SSL.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Bootstrap Your Own Latent (BYOL), a new approach to self-supervised image representation learning. BYOL relies on two neural networks, referred to as online and target networks, that interact and learn from each other. From an augmented view of an image, we train the online network to predict the target network representation of the same image under a different augmented view. At the same time, we update the target network with a slow-moving average of the online network. While state-of-the art methods rely on negative pairs, BYOL achieves a new state of the art without them. BYOL reaches 74.3% top-1 classification accuracy on ImageNet using a linear evaluation with a ResNet-50 architecture and 79.6% with a larger ResNet. We show that BYOL performs on par or better than the current state of the art on both transfer and semi-supervised benchmarks. Our implementation and pretrained models are given on GitHub.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning good image representations is a key challenge in computer vision as it allows for efficient training on downstream tasks. Many different training approaches have been proposed to learn such representations, usually relying on visual pretext tasks. Among them, state-of-the-art contrastive methods are trained by reducing the distance between representations of different augmented views of the same image ('positive pairs'), and increasing the distance between representations of augmented views from different images ('negative pairs'). These methods need careful treatment of negative pairs by either relying on large batch sizes, memory banks or customized mining strategies to retrieve the negative pairs. In addition, their performance critically depends on the choice of image augmentations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce Bootstrap Your Own Latent (BYOL), a new algorithm for self-supervised learning of image representations. BYOL achieves higher performance than state-of-the-art contrastive methods without using negative pairs. It iteratively bootstraps^44^4Throughout this paper, the term *bootstrap* is used in its idiomatic sense rather than the statistical sense. the outputs of a network to serve as targets for an enhanced representation. Moreover, BYOL is more robust to the choice of image augmentations than contrastive methods; we suspect that not relying on negative pairs is one of the leading reasons for its improved robustness. While previous methods based on bootstrapping have used pseudo-labels, cluster indices or a handful of labels, we propose to directly bootstrap the representations. In particular, BYOL uses two neural networks, referred to as online and target networks, that interact and learn from each other. Starting from an augmented view of an image, BYOL trains its online network to predict the target network's representation of another augmented view of the same image.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While this objective admits collapsed solutions, e.g., outputting the same vector for all images, we empirically show that BYOL does not converge to such solutions. We hypothesize (see Section 3.2) that the combination of (i) the addition of a predictor to the online network and (ii) the use of a slow-moving average of the online parameters as the target network encourages encoding more and more information within the online projection and avoids collapsed solutions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate the representation learned by BYOL on ImageNet and other vision benchmarks using ResNet architectures. Under the linear evaluation protocol on ImageNet, consisting in training a linear classifier on top of the frozen representation, BYOL reaches $74.3\%$ top-1 accuracy with a standard ResNet-$50$ and $79.6\%$ top-1 accuracy with a larger ResNet (Figure 1). In the semi-supervised and transfer settings on ImageNet, we obtain results on par or superior to the current state of the art. Our contributions are: (i) We introduce BYOL, a self-supervised representation learning method (Section 3) which achieves state-of-the-art results under the linear evaluation protocol on ImageNet without using negative pairs. (ii) We show that our learned representation outperforms the state of the art on semi-supervised and transfer benchmarks (Section 4). (iii) We show that BYOL is more resilient to changes in the batch size and in the set of image augmentations compared to its contrastive counterparts (Section 5).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, BYOL suffers a much smaller performance drop than SimCLR, a strong contrastive baseline, when only using random crops as image augmentations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Method", "weight": 1.0} -->

We start by motivating our method before explaining its details in Section 3.1. Many successful self-supervised learning approaches build upon the cross-view prediction framework introduced. Typically, these approaches learn representations by predicting different views (e.g., different random crops) of the same image from one another. Many such approaches cast the prediction problem directly in representation space: the representation of an augmented view of an image should be predictive of the representation of another augmented view of the same image. However, predicting directly in representation space can lead to collapsed representations: for instance, a representation that is constant across views is always fully predictive of itself. Contrastive methods circumvent this problem by reformulating the prediction problem into one of discrimination: from the representation of an augmented view, they learn to discriminate between the representation of another augmented view of the same image, and the representations of augmented views of different images. In the vast majority of cases, this prevents the training from finding collapsed representations. Yet, this discriminative approach typically requires comparing each representation of an augmented view with many negative examples, to find ones sufficiently close to make the discrimination task challenging.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Method", "weight": 1.0} -->

In this work, we thus tasked ourselves to find out whether these negative examples are indispensable to prevent collapsing while preserving high performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

To prevent collapse, a straightforward solution is to use a fixed randomly initialized network to produce the targets for our predictions. While avoiding collapse, it empirically does not result in very good representations. Nonetheless, it is interesting to note that the representation obtained using this procedure can already be much better than the initial fixed representation. In our ablation study (Section 5), we apply this procedure by predicting a fixed randomly initialized network and achieve $18.8\%$ top-1 accuracy (Table 5(a)) on the linear evaluation protocol on ImageNet, whereas the randomly initialized network only achieves $1.4\%$ by itself. This experimental finding is the core motivation for BYOL: from a given representation, referred to as target, we can train a new, potentially enhanced representation, referred to as online, by predicting the target representation. From there, we can expect to build a sequence of representations of increasing quality by iterating this procedure, using subsequent online networks as new target networks for further training. In practice, BYOL generalizes this bootstrapping procedure by iteratively refining its representation, but using a slowly moving exponential average of the online network as the target network instead of fixed checkpoints.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Description of BYOL", "weight": 1.0} -->

BYOL's goal is to learn a representation $y_{\theta}$ which can then be used for downstream tasks. As described previously, BYOL uses two neural networks to learn: the *online* and *target* networks. The online network is defined by a set of weights $\theta$ and is comprised of three stages: an *encoder* $f_{\theta}$, a *projector* $g_{\theta}$ and a *predictor* $q_{\theta}$, as shown in Figure 2 and Figure 8. The target network has the same architecture as the online network, but uses a different set of weights $\xi$. The target network provides the regression targets to train the online network, and its parameters $\xi$ are an exponential moving average of the online parameters $\theta$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Description of BYOL", "weight": 1.0} -->

More precisely, given a target decay rate $\tau \in {\lbrack 0,1\rbrack}$, after each training step we perform the following update, Given a set of images $\mathcal{D}$, an image $x \sim \mathcal{D}$ sampled uniformly from $\mathcal{D}$, and two distributions of image augmentations $\mathcal{T}$ and $\mathcal{T}'$, BYOL produces two augmented views $v{{{\lbrack{1pt}\rbrack}} = \Delta}{t{(x)}}$ and $v'{{{\lbrack{1pt}\rbrack}} = \Delta}{t'{(x)}}$ from $x$ by applying respectively image augmentations $t \sim \mathcal{T}$ and $t' \sim \mathcal{T}'$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Description of BYOL", "weight": 1.0} -->

Note that this predictor is only applied to the online branch, making the architecture asymmetric between the online and target pipeline. Finally we define the following mean squared error between the normalized predictions and target projections,^55^5While we could directly predict the representation $y$ and not a projection $z$, previous work have empirically shown that using this projection improves performance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Description of BYOL", "weight": 1.0} -->

We symmetrize the loss $\mathcal{L}_{\theta,\xi}$ in Equation 2 by separately feeding $v'$ to the online network and $v$ to the target network to compute ${\overset{\sim}{\mathcal{L}}}_{\theta,\xi}$. At each training step, we perform a stochastic optimization step to minimize $\mathcal{L}_{\theta,\xi}^{\text{BYOL}} = {\mathcal{L}_{\theta,\xi} + {\overset{\sim}{\mathcal{L}}}_{\theta,\xi}}$ with respect to $\theta$ only, but not $\xi$, as depicted by the stop-gradient in Figure 2. BYOL's dynamics are summarized as where $optimizer$ is an optimizer and $\eta$ is a learning rate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Description of BYOL", "weight": 1.0} -->

At the end of training, we only keep the encoder $f_{\theta}$; as. When comparing to other methods, we consider the number of inference-time weights only in the final representation $f_{\theta}$. The full training procedure is summarized in Appendix A, and python pseudo-code based on the libraries JAX and Haiku is provided in in Appendix J.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

As BYOL does not use an explicit term to prevent collapse (such as negative examples ) while minimizing $\mathcal{L}_{\theta,\xi}^{\text{BYOL}}$ with respect to $\theta$, it may seem that BYOL should converge to a minimum of this loss with respect to $(\theta,\xi)$ (*e.g.*, a collapsed constant representation). However BYOL's target parameters $\xi$ updates are not in the direction of $\nabla_{\xi}\mathcal{L}_{\theta,\xi}^{\text{BYOL}}$. More generally, we hypothesize that there is no loss $L_{\theta,\xi}$ such that BYOL's dynamics is a gradient descent on $L$ jointly over $\theta,\xi$. This is similar to GANs, where there is no loss that is jointly minimized w.r.t. both the discriminator and generator parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

There is therefore no a priori reason why BYOL's parameters would converge to a minimum of $\mathcal{L}_{\theta,\xi}^{\text{BYOL}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

While BYOL's dynamics still admit undesirable equilibria, we did not observe convergence to such equilibria in our experiments. In addition, when assuming BYOL's predictor to be optimal^66^6For simplicity we also consider BYOL without normalization (which performs reasonably close to BYOL, see Section F.6) nor symmetrization i.e., $q_{\theta} = q^{\star}$ with we hypothesize that the undesirable equilibria are unstable. Indeed, in this optimal predictor case, BYOL's updates on $\theta$ follow in expectation the gradient of the expected conditional variance (see Appendix H for details), where $z_{\xi,i}'$ is the $i$-th feature of $z_{\xi}'$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

Note that for any random variables $X,$ $Y,$ and $Z$, ${\operatorname{Var}{(\left. X \middle| {Y,Z} \right.)}} \leq {\operatorname{Var}{(\left. X \middle| Y \right.)}}$. Let $X$ be the target projection, $Y$ the current online projection, and $Z$ an additional variability on top of the online projection induced by stochasticities in the training dynamics: purely discarding information from the online projection cannot decrease the conditional variance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

In particular, BYOL avoids constant features in $z_{\theta}$ as, for any constant $c$ and random variables $z_{\theta}$ and $z_{\xi}'$, ${\operatorname{Var}{(\left. z_{\xi}' \middle| z_{\theta} \right.)}} \leq {\operatorname{Var}{(\left. z_{\xi}' \middle| c \right.)}}$; hence our hypothesis on these collapsed constant equilibria being unstable. Interestingly, if we were to minimize ${\mathbb{E}}{\lbrack{\sum_{i}{\operatorname{Var}{(\left. z_{\xi,i}' \middle| z_{\theta} \right.)}}}\rbrack}$ with respect to $\xi$, we would get a collapsed $z_{\xi}'$ as the variance is minimized for a constant $z_{\xi}'$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

Instead, BYOL makes $\xi$ closer to $\theta$, incorporating sources of variability captured by the online projection into the target projection.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Intuitions on BYOL's behavior", "weight": 1.0} -->

Furthemore, notice that performing a hard-copy of the online parameters $\theta$ into the target parameters $\xi$ would be enough to propagate new sources of variability. However, sudden changes in the target network might break the assumption of an optimal predictor, in which case BYOL's loss is not guaranteed to be close to the conditional variance. We hypothesize that the main role of BYOL's moving-averaged target network is to ensure the near-optimality of the predictor over training; Section 5 and Appendix I provide some empirical support of this interpretation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Image augmentations", "weight": 1.0} -->

BYOL uses the same set of image augmentations as in SimCLR. First, a random patch of the image is selected and resized to $224 \times 224$ with a random horizontal flip, followed by a color distortion, consisting of a random sequence of brightness, contrast, saturation, hue adjustments, and an optional grayscale conversion. Finally Gaussian blur and solarization are applied to the patches. Additional details on the image augmentations are in Appendix B.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Architecture", "weight": 1.0} -->

We use a convolutional residual network with 50 layers and post-activation (ResNet-$50{(1 \times )}$ v1) as our base parametric encoders $f_{\theta}$ and $f_{\xi}$. We also use deeper ($50$, $101$, $152$ and $200$ layers) and wider (from $1 \times$ to $4 \times$) ResNets, as. Specifically, the representation $y$ corresponds to the output of the final average pooling layer, which has a feature dimension of $2048$ (for a width multiplier of $1 \times$). As in SimCLR, the representation $y$ is projected to a smaller space by a *multi-layer perceptron* (MLP) $g_{\theta}$, and similarly for the target projection $g_{\xi}$. This MLP consists in a linear layer with output size $4096$ followed by batch normalization, rectified linear units (ReLU), and a final linear layer with output dimension $256$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Architecture", "weight": 1.0} -->

Contrary to SimCLR, the output of this MLP is not batch normalized. The predictor $q_{\theta}$ uses the same architecture as $g_{\theta}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimization", "weight": 1.0} -->

We use the LARS optimizer with a cosine decay learning rate schedule, without restarts, over $1000$ epochs, with a warm-up period of $10$ epochs. We set the base learning rate to $0.2,$ scaled linearly with the batch size ($\text{LearningRate} = {{0.2 \times \text{BatchSize}}/256}$). In addition, we use a global weight decay parameter of $1.5 \cdot 10^{- 6}$ while excluding the biases and batch normalization parameters from both LARS adaptation and weight decay. For the target network, the exponential moving average parameter $\tau$ starts from $\tau_{\text{base}} = 0.996$ and is increased to one during training.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimization", "weight": 1.0} -->

Specifically, we set $\tau \triangleq {1 - {{{({1 - \tau_{\text{base}}})} \cdot \left( {{\cos\left( {{\pik}/K} \right)} + 1} \right)}/2}}$ with $k$ the current training step and $K$ the maximum number of training steps. We use a batch size of $4096$ split over $512$ Cloud TPU v$3$ cores. With this setup, training takes approximately $8$ hours for a ResNet-$50{( \times 1)}$. All hyperparameters are summarized in Appendix J; an additional set of hyperparameters for a smaller batch size of $512$ is provided in Appendix G.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental evaluation", "weight": 1.0} -->

We assess the performance of BYOL's representation after self-supervised pretraining on the training set of the ImageNet ILSVRC-2012 dataset. We first evaluate it on ImageNet (IN) in both linear evaluation and semi-supervised setups. We then measure its transfer capabilities on other datasets and tasks, including classification, segmentation, object detection and depth estimation. For comparison, we also report scores for a representation trained using labels from the train ImageNet subset, referred to as Supervised-IN. In Appendix E, we assess the generality of BYOL by pretraining a representation on the Places365-Standard dataset before reproducing this evaluation protocol.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Linear evaluation on ImageNet", "weight": 1.0} -->

We first evaluate BYOL's representation by training a linear classifier on top of the frozen representation, following the procedure described, and section C.1; we report top-$1$ and top-$5$ accuracies in % on the test set in Table 1. With a standard ResNet-$50$ ($\times 1$) BYOL obtains $74.3\%$ top-$1$ accuracy ($91.6\%$ top-$5$ accuracy), which is a $1.3\%$ (resp. $0.5\%$) improvement over the previous self-supervised state of the art. This tightens the gap with respect to the supervised baseline of, $76.5\%$, but is still significantly below the stronger supervised baseline of, $78.9\%$. With deeper and wider architectures, BYOL consistently outperforms the previous state of the art (Section C.2), and obtains a best performance of $79.6\%$ top-$1$ accuracy, ranking higher than previous self-supervised approaches.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Linear evaluation on ImageNet", "weight": 1.0} -->

On a ResNet-$50$ ($4 \times$) BYOL achieves $78.6\%$, similar to the $78.9\%$ of the best supervised baseline in for the same architecture.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Semi-supervised training on ImageNet", "weight": 1.0} -->

Next, we evaluate the performance obtained when fine-tuning BYOL's representation on a classification task with a small subset of ImageNet's train set, this time using label information. We follow the semi-supervised protocol of detailed in Section C.1, and use the same fixed splits of respectively $1\%$ and $10\%$ of ImageNet labeled training data as. We report both top-$1$ and top-$5$ accuracies on the test set in Table 2. BYOL consistently outperforms previous approaches across a wide range of architectures. Additionally, as detailed in Section C.1, BYOL reaches $77.7\%$ top-$1$ accuracy with ResNet-50 when fine-tuning over $100\%$ of ImageNet labels.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Transfer to other classification tasks", "weight": 1.0} -->

We evaluate our representation on other classification datasets to assess whether the features learned on ImageNet (IN) are generic and thus useful across image domains, or if they are ImageNet-specific. We perform linear evaluation and fine-tuning on the same set of classification tasks used, and carefully follow their evaluation protocol, as detailed in Appendix D. Performance is reported using standard metrics for each benchmark, and results are provided on a held-out test set after hyperparameter selection on a validation set. We report results in Table 3, both for linear evaluation and fine-tuning. BYOL outperforms SimCLR on all benchmarks and the Supervised-IN baseline on $7$ of the $12$ benchmarks, providing only slightly worse performance on the $5$ remaining benchmarks. BYOL's representation can be transferred over to small images, e.g., CIFAR, landscapes, e.g., SUN397 or VOC2007, and textures, e.g., DTD.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

We evaluate our representation on different tasks relevant to computer vision practitioners, namely semantic segmentation, object detection and depth estimation. With this evaluation, we assess whether BYOL's representation generalizes beyond classification tasks.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

We first evaluate BYOL on the VOC2012 semantic segmentation task as detailed in Section D.4, where the goal is to classify each pixel in the image. We report the results in Table 4(a). BYOL outperforms both the Supervised-IN baseline ($+ 1.9$ mIoU) and SimCLR ($+ 1.1$ mIoU).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

Similarly, we evaluate on object detection by reproducing the setup in using a Faster R-CNN architecture, as detailed in Section D.5. We fine-tune on trainval2007 and report results on test2007 using the standard AP~50~ metric; BYOL is significantly better than the Supervised-IN baseline ($+ 3.1$ AP~50~) and SimCLR ($+ 2.3$ AP~50~).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

Finally, we evaluate on depth estimation on the NYU v2 dataset, where the depth map of a scene is estimated given a single RGB image. Depth prediction measures how well a network represents geometry, and how well that information can be localized to pixel accuracy. The setup is based on and detailed in Section D.6. We evaluate on the commonly used test subset of $654$ images and report results using several common metrics in Table 4(b): relative (rel) error, root mean squared (rms) error, and the percent of pixels (pct) where the error, $\max{({d_{gt}/d_{p}},{d_{p}/d_{gt}})}$, is below $1.25^{n}$ thresholds where $d_{p}$ is the predicted depth and $d_{gt}$ is the ground truth depth. BYOL is better or on par with other methods for each metric. For instance, the challenging pct.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

$< 1.25$ measure is respectively improved by $+ 3.5$ points and $+ 1.3$ points compared to supervised and SimCLR baselines.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

(a) Transfer results in semantic segmentation and object detection.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Transfer to other vision tasks", "weight": 1.0} -->

(b) Transfer results on NYU v2 depth estimation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Building intuitions with ablations", "weight": 1.0} -->

We present ablations on BYOL to give an intuition of its behavior and performance. For reproducibility, we run each configuration of parameters over three seeds, and report the average performance. We also report the half difference between the best and worst runs when it is larger than $0.25$. Although previous works perform ablations at $100$ epochs, we notice that relative improvements at $100$ epochs do not always hold over longer training. For this reason, we run ablations over $300$ epochs on $64$ TPU v$3$ cores, which yields consistent results compared to our baseline training of $1000$ epochs. For all the experiments in this section, we set the initial learning rate to $0.3$ with batch size $4096$, the weight decay to $10^{- 6}$ as in SimCLR and the base target decay rate $\tau_{\text{base}}$ to $0.99$. In this section we report results in top-$1$ accuracy on ImageNet under the linear evaluation protocol as in Section C.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Batch size", "weight": 1.0} -->

Among contrastive methods, the ones that draw negative examples from the minibatch suffer performance drops when their batch size is reduced. BYOL does not use negative examples and we expect it to be more robust to smaller batch sizes. To empirically verify this hypothesis, we train both BYOL and SimCLR using different batch sizes from $128$ to $4096$. To avoid re-tuning other hyperparameters, we average gradients over $N$ consecutive steps before updating the online network when reducing the batch size by a factor $N$. The target network is updated once every $N$ steps, after the update of the online network; we accumulate the $N$-steps in parallel in our runs.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Batch size", "weight": 1.0} -->

As shown in Figure 3(a), the performance of SimCLR rapidly deteriorates with batch size, likely due to the decrease in the number of negative examples. In contrast, the performance of BYOL remains stable over a wide range of batch sizes from $256$ to $4096$, and only drops for smaller values due to batch normalization layers in the encoder.^77^7The only dependency on batch size in our training pipeline sits within the batch normalization layers.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Batch size", "weight": 1.0} -->

(a) Impact of batch size (b) Impact of progressively removing transformations Figure 3: Decrease in top-1 accuracy (in % points) of BYOL and our own reproduction of SimCLR at 300 epochs, under linear evaluation on ImageNet.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Image augmentations", "weight": 1.0} -->

Contrastive methods are sensitive to the choice of image augmentations. For instance, SimCLR does not work well when removing color distortion from its image augmentations. As an explanation, SimCLR shows that crops of the same image mostly share their color histograms. At the same time, color histograms vary across images. Therefore, when a contrastive task only relies on random crops as image augmentations, it can be mostly solved by focusing on color histograms alone. As a result the representation is not incentivized to retain information beyond color histograms. To prevent that, SimCLR adds color distortion to its set of image augmentations. Instead, BYOL is incentivized to keep any information captured by the target representation into its online network, to improve its predictions. Therefore, even if augmented views of a same image share the same color histogram, BYOL is still incentivized to retain additional features in its representation. For that reason, we believe that BYOL is more robust to the choice of image augmentations than contrastive methods.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Image augmentations", "weight": 1.0} -->

Results presented in Figure 3(b) support this hypothesis: the performance of BYOL is much less affected than the performance of SimCLR when removing color distortions from the set of image augmentations ($- 9.1$ accuracy points for BYOL, $- 22.2$ accuracy points for SimCLR). When image augmentations are reduced to mere random crops, BYOL still displays good performance ($59.4\%$, *i.e.* $- 13.1$ points from $72.5\%$ ), while SimCLR loses more than a third of its performance ($40.3\%$, *i.e.* $- 27.6$ points from $67.9\%$). We report additional ablations in Section F.3.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Bootstrapping", "weight": 1.0} -->

BYOL uses the projected representation of a target network, whose weights are an exponential moving average of the weights of the online network, as target for its predictions. This way, the weights of the target network represent a delayed and more stable version of the weights of the online network. When the target decay rate is $1$, the target network is never updated, and remains at a constant value corresponding to its initialization. When the target decay rate is $0$, the target network is instantaneously updated to the online network at each step. There is a trade-off between updating the targets too often and updating them too slowly, as illustrated in Table 5(a). Instantaneously updating the target network ($\tau = 0$) destabilizes training, yielding very poor performance while never updating the target ($\tau = 1$) makes the training stable but prevents iterative improvement, ending with low-quality final representation. All values of the decay rate between $0.9$ and $0.999$ yield performance above $68.4\%$ top-$1$ accuracy at $300$ epochs.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Bootstrapping", "weight": 1.0} -->

Constant random network Moving average of online Moving average of online Moving average of online Stop gradient of online† (a) Results for different target modes. †In the stop gradient of online, τ = τbase = 0 is kept constant throughout training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Bootstrapping", "weight": 1.0} -->

(b) Intermediate variants between BYOL and SimCLR.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablation to contrastive methods", "weight": 1.0} -->

In this subsection, we recast SimCLR and BYOL using the same formalism to better understand where the improvement of BYOL over SimCLR comes. Let us consider the following objective that extends the InfoNCE objective (see Section F.4), where $\alpha > 0$ is a fixed temperature, $\beta \in {\lbrack 0,1\rbrack}$ a weighting coefficient, $B$ the batch size, $v$ and $v'$ are batches of augmented views where for any batch index $i$, $v_{i}$ and $v_{i}'$ are augmented views from the same image; the real-valued function $S_{\theta}$ quantifies pairwise similarity between augmented views.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation to contrastive methods", "weight": 1.0} -->

We recover the BYOL loss when using a predictor and a target network, *i.e.,* ${\phi{(u_{1})}} = {p_{\theta}\left({z_{\theta}{(u_{1})}} \right)}$ and ${\psi{(u_{2})}} = {z_{\xi}{(u_{2})}}$ with $\beta = 0$. To evaluate the influence of the target network, the predictor and the coefficient $\beta$, we perform an ablation over them. Results are presented in Table 5(b) and more details are given in Section F.4.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation to contrastive methods", "weight": 1.0} -->

The only variant that performs well without negative examples (i.e., with $\beta = 0$) is BYOL, using both a bootstrap target network and a predictor. Adding the negative pairs to BYOL's loss without re-tuning the temperature parameter hurts its performance. In Section F.4, we show that we can add back negative pairs and still match the performance of BYOL with proper tuning of the temperature.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation to contrastive methods", "weight": 1.0} -->

Simply adding a target network to SimCLR already improves performance ($+ 1.6$ points). This sheds new light on the use of the target network in MoCo, where the target network is used to provide more negative examples. Here, we show that by mere stabilization effect, even when using the same number of negative examples, using a target network is beneficial. Finally, we observe that modifying the architecture of $S_{\theta}$ to include a predictor only mildly affects the performance of SimCLR.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Network hyperparameters", "weight": 1.0} -->

In Appendix F, we explore how other network parameters may impact BYOL's performance. We iterate over multiple weight decays, learning rates, and projector/encoder architectures to observe that small hyperparameter changes do not drastically alter the final score. We note that removing the weight decay in either BYOL or SimCLR leads to network divergence, emphasizing the need for weight regularization in the self-supervised setting. Furthermore, we observe that changing the scaling factor in the network initialization did not impact the performance (higher than $72\%$ top-$1$ accuracy).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Relationship with Mean Teacher", "weight": 1.0} -->

Another semi-supervised approach, Mean Teacher (MT), complements a supervised loss on few labels with an additional consistency loss. In, this consistency loss is the $\ell_{2}$ distance between the logits from a student network, and those of a temporally averaged version of the student network, called teacher. Removing the predictor in BYOL results in an unsupervised version of MT with no classification loss that uses image augmentations instead of the original architectural noise (e.g., dropout). This variant of BYOL collapses (Row 7 of Table 5) which suggests that the additional predictor is critical to prevent collapse in an unsupervised scenario.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Importance of a near-optimal predictor", "weight": 1.0} -->

Table 5(b) already shows the importance of combining a predictor and a target network: the representation does collapse when either is removed. We further found that we can remove the target network without collapse by making the predictor near-optimal, either by (i) using an optimal *linear* predictor (obtained by linear regression on the current batch) before back-propagating the error through the network ($52.5\%$ top-1 accuracy), or (ii) increasing the learning rate of the predictor ($66.5\%$ top-1). By contrast, increasing the learning rates of both projector *and* predictor (without target network) yields poor results ($\approx {25\%}$ top-1). See Appendix I for more details. This seems to indicate that keeping the predictor near-optimal at all times is important to preventing collapse, which may be one of the roles of BYOL's target network.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced BYOL, a new algorithm for self-supervised learning of image representations. BYOL learns its representation by predicting previous versions of its outputs, without using negative pairs. We show that BYOL achieves state-of-the-art results on various benchmarks. In particular, under the linear evaluation protocol on ImageNet with a ResNet-$50$ ($1 \times$), BYOL achieves a new state of the art and bridges most of the remaining gap between self-supervised methods and the supervised learning baseline of. Using a ResNet-$200$ $(2 \times )$, BYOL reaches a top-$1$ accuracy of $79.6\%$ which improves over the previous state of the art ($76.8\%$) while using $30\%$ fewer parameters.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Nevertheless, BYOL remains dependent on existing sets of augmentations that are specific to vision applications. To generalize BYOL to other modalities (e.g., audio, video, text,...) it is necessary to obtain similarly suitable augmentations for each of them. Designing such augmentations may require significant effort and expertise. Therefore, automating the search for these augmentations would be an important next step to generalize BYOL to other modalities.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Broader impact", "weight": 1.0} -->

The presented research should be categorized as research in the field of unsupervised learning. This work may inspire new algorithms, theoretical, and experimental investigation. The algorithm presented here can be used for many different vision applications and a particular use may have both positive or negative impacts, which is known as the dual use problem. Besides, as vision datasets could be biased, the representation learned by BYOL could be susceptible to replicate these biases.
