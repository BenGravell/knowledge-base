<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Do Better ImageNet Classifiers Assess Perceptual Similarity Better?

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Perceptual distances between images, as measured in the space of pre-trained deep features, have outperformed prior low-level, pixel-based metrics on assessing perceptual similarity. While the capabilities of older and less accurate models such as AlexNet and VGG to capture perceptual similarity are well known, modern and more accurate models are less studied. In this paper, we present a large-scale empirical study to assess how well ImageNet classifiers perform on perceptual similarity. First, we observe a inverse correlation between ImageNet accuracy and Perceptual Scores of modern networks such as ResNets, EfficientNets, and Vision Transformers: that is better classifiers achieve worse Perceptual Scores. Then, we examine the ImageNet accuracy/Perceptual Score relationship on varying the depth, width, number of training steps, weight decay, label smoothing, and dropout. Higher accuracy improves Perceptual Score up to a certain point, but we uncover a Pareto frontier between accuracies and Perceptual Score in the mid-to-high accuracy regime.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We explore this relationship further using a number of plausible hypotheses such as distortion invariance, spatial frequency sensitivity, and alternative perceptual functions. Interestingly we discover shallow ResNets and ResNets trained for less than 5 epochs only on ImageNet, whose emergent Perceptual Score matches the prior best networks trained directly on supervised human perceptual judgements. The checkpoints for the models in our study are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

ImageNet is the cornerstone of modern supervised learning and has enabled significant progress in computer vision. Features learnt via training on ImageNet transfer well to a number of downstream tasks, making ImageNet pretraining a standard recipe. Further, better accuracy on ImageNet usually implies better performance on a diverse set of downstream tasks such as robustness to common corruptions, adversarial robustness, out-of-distribution generalization, transfer learning on smaller classification datasets, pose estimation, domain adaptation, object detection and segmentation, and for predicting neural recordings and behaviors of primates on object recognition tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a remarkable side effect, ImageNet models can also capture a notion of similarity identical to humans, known as perceptual similarity. Designing distance metrics that correspond to human judgements is a well established problem in computer vision, and a number of low-level metrics have been introduced for this purpose. The first generation of ImageNet classifiers: AlexNet, VGG, and SqueezeNet can all measure perceptual similarity termed as Perceptual Scores (PS), as an emergent property, in a way that outperforms all prior pixel-level metrics and correlates better with human judgement.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we are motivated by the following questions: Considering ImageNet classification has progressed significantly since then, can we obtain a better perceptual similarity metric by using a better classifier directly? Since modern neural network training involves a large number of hyperparameters, are there design choices that can improve a classifier's perceptual similarity? Are there latent factors that govern the relationship between ImageNet accuracy and perceptual similarity?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We perform a suite of experiments on BAPPS, a large dataset of human-evaluated perceptual judgements. To the best of our knowledge, our work is the first empirical study to present a systematic investigation and rigorous deep dive into the relationship between ImageNet accuracy and perceptual similarity. We study the ImageNet accuracy/PS interplay of a wide variety of networks across many combinations of architectures and hyperparameters. Given the increasing interest in analyzing how representations of ImageNet classifiers transfer to other domains, our work adds another direction to this literature.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1 displays the ImageNet accuracy and PS of every ImageNet classifier in our study. While Zhang et al., show a positive correlation between PS and ImageNet accuracy, we observe that this holds only in the low-accuracy regime. In the mid-to-high accuracy regime, we uncover a counter-intuitive Pareto frontier between accuracy and PS. Modern networks, EfficientNets, Vision Transformers and ResNets, lie to the right, obtaining high accuracies and low PS. Contrary to prevailing evidence that suggests models with high validation accuracies on ImageNet are likely to transfer better to other domains, we find that representations from underfit ImageNet models with modest validation accuracies achieve the best PS. Our experiments further suggest that attaining the best PS is somewhat architecture agnostic. For example, ResNets trained with large amounts of weight decay or early stopped within a few epochs of training can match or outperform the PS of AlexNet and VGG.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we investigate if there are latent factors that govern the relationship between ImageNet accuracy and PS using the following hypotheses. Does the inverse-U persist with global perceptual functions? Are low PS models less sensitive to distortions? What are the contributions of skip connections in modern architectures to decreased PS, if any? Do lower layers of better classifiers have a higher PS than higher layers? What is the impact of ImageNet class granularity on PS? While the causatory latent factor that governs the relationship between accuracy and perceptual similarity remains unclear, our paper opens the door to further understanding of this phenomenon.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We systematically evaluate the PS of modern "out-of-the-box" networks, ResNets, EfficientNets and Vision Transformers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the variation of PS (and accuracy) as a function of width, depth, number of training steps, weight decay, label smoothing and dropout. Our large-scale study consists of 722 different ImageNet networks across the cross product of these 7 different hyperparameters and 5 architectures.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We explore the relationship between ImageNet accuracy and PS further using spatial frequency sensitivity, invariance to distortions, class granularity, and improved global perceptual functions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

While modern classifiers outperform prior pixel-based metrics in PS, they under-perform moderate classifiers like AlexNet.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern ImageNet models that are much shallower, narrower, early-stopped within a few epochs of training and trained with larger values of weight decay attain significantly higher PS than their out-of-the-box counterparts.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In all of our hyperparameter sweeps with the exception of label smoothing and dropout, we discover an unexpected and previously unobserved tradeoff between accuracy and PS. In each hyperparameter sweep, there exists an optimal accuracy up to which improving accuracy improves PS. This optimum is fairly low and is attained quite early in the hyperparameter sweep. Beyond this point, better classifiers achieve worse PS.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Perceptual functions that rely on global image representations such as style achieve better PS than per-pixel perceptual functions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We do not find a correlation between PS of models and their sensitivity to distortions. Further, low Perceptual Score models are not necessarily more reliant on high-frequency spatial information for classification as compared to high PS models.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-level features found in the latter layers of residual networks, have better PS than low-level features found in the earlier layers.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we find particularly shallow, early-stopped ResNets trained only on ImageNet that attain an emergent Perceptual Score of 70.2. This matches the best Perceptual Scores across prior networks which were trained directly on BAPPS to match human judgements.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The BAPPS Dataset", "weight": 1.0} -->

The BAPPS Dataset is a dataset of 161k patches derived by applying exclusively low-level distortions to the MIT-Adobe 5k dataset for training and the RAISE1k dataset for validation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The BAPPS Dataset", "weight": 1.0} -->

Traditional Distortions: Random noise, blurring, spatial shifts, corruptions and compression artifacts. (1 family.)

<!-- chunk {"id": "body-0022", "role": "body", "section": "The BAPPS Dataset", "weight": 1.0} -->

CNN-based Distortions: Distortions created by CNN-based autoencoders trained on autoencoding, denoising, colorization and superresolution. (1 family.)

<!-- chunk {"id": "body-0023", "role": "body", "section": "The BAPPS Dataset", "weight": 1.0} -->

Outputs of Real algorithms: Outputs from state-of-the-art frame interpolation, video deblurring, colorization and superresolution models. The distortions created by each class of models is treated as a separate family. (4 families.)

<!-- chunk {"id": "body-0024", "role": "body", "section": "The BAPPS Dataset", "weight": 1.0} -->

Table 2 in Zhang et al. contains a comprehensive list of distortions. The train set consists of the traditional and CNN-based distortions and the validation set contains all 6 families. Given a family of distortions and a set of reference images, Zhang et al. generate the BAPPS dataset as follows. They select a reference patch $x$ and then apply two distortions at random to generate the target patches $x_{0}$ and $x_{1}$. They record the binary response of a human, indicating which of the target patches is closer to the reference patch. For a given image triplet, $(x_{0},x_{1},x)$, $p$ is the average of 2 and 5 human responses on the train and validation set respectively. Fig. 2 displays 3 sample image triplets from the BAPPS Dataset.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Perceptual Score", "weight": 1.0} -->

We first define the PS of a network, for which we adopt the "2AFC" scoring protocol. First, let $x_{0}$ and $x_{1}$ denote two images. Let ${\overset{\sim}{y_{0}}}^{l}$ and ${\overset{\sim}{y_{1}}}^{l}$ be the feature maps for $x_{0}$ and $x_{1}$ at the $l$th layer of a network, normalized across the channel dimension.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Perceptual Score", "weight": 1.0} -->

where $H_{l}$ and $W_{l}$ denote the height and width of the feature maps at layer $l$, respectively. $\mathcal{L}$ denotes the subset of layers which are used in the perceptual similarity; this subset is architecture specific. Given a reference image $x$ and two target images $x_{0}$ and $x_{1}$, BAPPS provides a ground truth soft-label $p$. $p$ can be interpreted as the probability a human rater would rate $x_{1}$ as more similar to $x$ than $x_{0}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dynamic Range of PS", "weight": 1.0} -->

Unlike accuracy that can vary from 0 to 100, PS has a narrow dynamic range. To provide intuition on this dynamic range, we plot the PS for ground truth ratings $p$ from BAPPS and simulated combinations of $(d_{0},d_{1})$ dependent on $p$. Let $\overset{\sim}{p} = {\mathbb{1}{\lbrack{p > 0.5}\rbrack}}$, i.e we convert the human ratings into binary labels. If $\overset{\sim}{p} = 1$, we sample $d_{0}$ and $d_{1}$ from truncated normal distributions, i.e ${d_{0} \sim {\phi{(1,\sigma,0,1)}}},{d_{1} \sim {\phi{(0,\sigma,0,1)}}}$ where 0 and 1 are the lower and upper bounds.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dynamic Range of PS", "weight": 1.0} -->

Conversely if $\overset{\sim}{p} = 0$, we sample ${d_{0} \sim {\phi{(0,\sigma,0,1)}}},{d_{1} \sim {\phi{(1,\sigma,0,1)}}}$. In Fig. 3, $\sigma$ models the noise in predicting $d$, as $\sigma$ is increased, the distances $(d_{0},d_{1})$ have a higher chance of being misaligned with $p$, and as expected PS smoothly decreases from the upper bound ($\sim 0.8$) to random choice ($0.5$).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dynamic Range of PS", "weight": 1.0} -->

On the actual BAPPS dataset, the previous best PS for low-level metrics was attained by FSIMc, a low-level hand crafted matching function with a value of 63.8. The previously reported lower and upper PS bounds for ImageNet networks were values of 64.3 and 68.9. These were achieved by a randomly initialized network and AlexNet respectively. VGG obtains a PS of 67.0. The human upper bound is 73.9, reflective of the entropy across human raters. Across all our experiments, we cover almost the entire prior dynamic PS range of trained networks, with the PS of our networks ranging from 65.0 to 69.7.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Architectures", "weight": 1.0} -->

We study two of the most popular classes of vision architectures: Convolutional Neural Networks (CNNs) and Transformers. As representative CNNs, we train ResNets and EfficientNets. For EfficientNets, we use model variants B0 to B5. For ResNets, we train networks with depths ranging from 6 to 200 layers. For Vision Transformers (ViT), we use the Base and Large variants, with patch sizes of 8 and 4, leading to four models (ViT-B/8, ViT-B/4, ViT-L/8 and ViT-L/4). We use smaller patch sizes than is common because we use lower resolution images (see the following Training section). However, any patch size smaller than 4 leads to poor generalization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training", "weight": 1.0} -->

We train our networks on ImageNet at a resolution of 64 $\times$ 64 and report their accuracies on the ImageNet validation set and PS on the BAPPS validation set. ImageNet 64 $\times$ 64 provides a cleaner test bed instead of the standard high-resolution (224 $\times$ 224 and above) for the following reasons.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Training", "weight": 1.0} -->

BAPPS is constructed using $64 \times 64$ images so that human raters can focus on low-level local changes as opposed to high-level semantic differences. ImageNet models pre-trained on high-resolution images classify $64 \times 64$ images poorly. Such models are sub-optimal for our analysis, because we are interested in the perceptual properties of classifiers that generalize reasonably well. An alternative option would be to resize $64 \times 64$ images to high-resolution images using linear interpolations. However, this can have the adverse side effect of blurring out or removing distortions from BAPPS images. Nonetheless, in Appendix A, we observe similar phenomena on models trained with high resolution images, with significantly worse PS.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Training", "weight": 1.0} -->

For all networks, we apply only random crops and flips and disable all other augmentations. We use the recommended hyperparameter settings given by the corresponding open-sourced training code. For the models where validation accuracy decreases during training, EffNet-B4 and EffNet-B5, we stop training just before this happens.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Representations", "weight": 1.0} -->

In prior work, Zhang et al. compute the PS of VGG using the outputs of every 2x2 max pooling layer, leading to 5 features in total. For the shallower AlexNet architecture, they employed the output of each of the 5 convolutions. Here, we describe the representations we use to compute the PS of modern networks, in this work.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Representations", "weight": 1.0} -->

Similar to VGG, for ResNets and EfficientNets, we use the outputs of the 4 reduction stages, where the spatial dimensions are reduced 2x via strided convolutions. Specifically, we obtain four 2D representations of resolution $16 \times 16$, $8 \times 8$, $4 \times 4$, and $2 \times 2$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Representations", "weight": 1.0} -->

For Vision Transformers, we use the global CLS representation of the image at the output of every encoder block. Our initial experiments on using features at the output of every layer instead of every block or reduction stage, as computed in AlexNet lead to worse PS across all architectures.

<!-- chunk {"id": "body-0037", "role": "body", "section": "ImageNet accuracy versus Perceptual Score", "weight": 1.0} -->

We train networks with their default hyperparameters five times and report the mean accuracy and PS (64 $\times$ 64) with error bars in Fig. 4. (Appendix M contains a list of default hyperparameters). All modern networks (red, green, and black) in Fig. 4 obtain a higher PS than FSIMc (63.8) and randomly initialized networks (64.3). Surprisingly though, representations of better ImageNet networks perform consistently worse. For example, ResNet-18 which achieves the best PS of 68.5 has a modest accuracy of 52.0% (64 $\times$ 64). EfficientNet B5 which has the worst PS of 67.2 achieves a much higher accuracy of 66.3%. Additionally, all networks perform worse than AlexNet (68.9).

<!-- chunk {"id": "body-0038", "role": "body", "section": "ImageNet accuracy versus Perceptual Score", "weight": 1.0} -->

Next, we push this observation to the limits. Our next experiment hopes to identify a much smaller network that achieves improved PS at the expense of extremely low accuracy. In Fig. 4, we report the accuracies and PS obtained by shallow ResNets with depths from 2 to 10 (ResNet, reduced depth). ResNet-10 and ResNet-6 obtain improved PS with reduced accuracies. However, the ResNets with a depth smaller than 6 incur losses in both accuracy and PS. Our results indicate that better classifiers produce better perceptual representations up until a certain "optimal accuracy". Above this optimal accuracy, ImageNet classifiers trade off better accuracies with worse PS. This phenomenon leads to some interesting observations: 1) ResNet-6 happens to achieve this optimal accuracy with a PS of 69.1, outperforming AlexNet. 2) Beyond the optimal accuracy, there is a strong inverse correlation between accuracy and PS (coefficient = -0.84). 3) ResNet-200 and ResNet-3 achieve similar PS, while having a an accuracy difference of 45%.

<!-- chunk {"id": "body-0039", "role": "body", "section": "How general is this relationship?", "weight": 1.0} -->

Section 5 indicates that an inverse-U relationship exists between accuracy and PS on varying the depth of residual networks. In this section, we attempt to generalize this relationship as a function of other implicit hyperparameters such as layer composition, width, depth and training hyperparameters of the considered architectures. In particular, we assess this relationship between accuracy and PS as a function of hyperparameters via 1D sweeps. We vary a single hyperparameter of a network (e.g. width) along a 1D grid which changes the network's accuracy and as an effect, the corresponding PS. In Appendix H, for all our sweeps, the validation accuracy does not decrease during training, indicating none of the networks overfit on the ImageNet train set. For a given sweep, we provide two sets of plots: 1) Scatter plots between PS/accuracy. 2) PS against the hyperparameter values. We choose 5 architectures: ResNets and ViTs with the best and worst PS, (ResNet-6, ResNet-200, ViT-B/8, ViT-L/4) plus a standard ResNet-50.

<!-- chunk {"id": "body-0040", "role": "body", "section": "How general is this relationship?", "weight": 1.0} -->

We sweep across the following hyperparamters: Number of training steps, network width, network depth, weight decay, dropout, and label smoothing. We define $p_{max}$ to be the optimal PS and $a{(p_{max})}$ to be the accuracy at which $p_{max}$ is reached. We observe the inverse-U relationship across all these hyperparameters with the exception of label smoothing and dropout. For these hyperparameter settings, we indicate $p_{max}$ and $a{(p_{max})}$ with dotted lines parallel to the x and y axes, respectively.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Number of train epochs", "weight": 1.0} -->

All networks exhibit the inverse-U shaped behaviour (Fig. 5a and 5c). $a{(p_{max})}$ is fairly consistent within a given family of architectures. ResNets have $a{(p_{max})}$ at low values between 15-25 % and ViTs have $a{(p_{max})}$ at moderate values between 40-50 %.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Number of train epochs", "weight": 1.0} -->

PS peaks early during training across all networks (Fig. 5d and 5b). ResNet-50 and ResNet-200 peak at the first few epochs of training ($p_{max} = 69.7$) while the ViT models peak at lower values ($p_{max} = 68.4$) and later around 60 epochs. After the peak, PS of better classifiers decrease more drastically. ResNets are trained with a learning rate schedule that causes a step-wise increase in accuracy as a function of training steps. Interestingly, in Fig. 5b, they exhibit a step-wise decrease in PS that matches this step-wise accuracy increase.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Width and Depth", "weight": 1.0} -->

In Fig. 6a, we see that ResNet-6 achieves $p_{max} = 69.6$ at ${a{(p_{max})}} = {20\%}$ while ResNet-200 has $p_{max} = 67.6$ at ${a{(p_{max})}} = {65\%}$. As the model capacity is increased from ResNet-6 to ResNet-200, the peak shifts from the top left to the bottom right. Compound scaling is a model scaling technique that improves model accuracy efficiently by scaling the width and depth of a network together. We observe a peculiar "inverse compound scaling" phenomena; depth and width of networks have to be scaled down simultaneously to improve on PS significantly.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Width and Depth", "weight": 1.0} -->

$a{(p_{max})}$ on varying the width and depth of ViTs are at 20% to 30% and 45-50%, respectively. (Figs. 6e, 6c). A shallow ViT model of depth 2 gets close to 40% accuracy. Hence, there might just not be enough points between 20% to 40% in Fig. 6e. This could explain the shift of $a{(p_{max})}$ to the right in Fig. 6e when compared to Fig. 6c.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Width and Depth", "weight": 1.0} -->

Shallower and narrower architectures perform better as shown in Figs. 6d, 6f, and 6b. The optimal width of ViT-B/8 and ViT-L/4 are 6 and 12% of their default widths while their optimal depths are just 2 transformer blocks. ResNet-6 and ResNet-50 exhibit similar properties with the optimal width being 25% of their original widths. ResNet-200 is the outlier with a small peak at its original width.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Central Crop", "weight": 1.0} -->

Modern networks employ random crops of high-resolution rectangular images during training. This artificially increases the effective quantity of training data available to the network. Replacing random crops with central crops has been shown to increase shape bias and reduce the discrepancy of object scales between training and testing.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Central Crop", "weight": 1.0} -->

Fig. 7b shows the accuracies and PS of the 5 architectures trained with center crops. Each architecture moves towards the top-left with lower accuracies and higher PS. ViT-L/4 is the exception as it moves towards the bottom-right. It encounters a significant reduction in accuracy, lowering it below $a{(p_{max})}$, which could explain the decrease in its PS. All center-cropped architectures lie along an inverse-U, with ResNet-6 at the optimum.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Weight Decay", "weight": 1.0} -->

Figs. 8c and 8d display the impact of weight decay on PS. ViT-L/4 has minimal variation in accuracy as the weight decay factor is varied; so we omit ViT-L/4 from this study. ResNets and ViTs achieve their worst PS at the default weight decay around $10^{- 4}$ and 0.3, respectively. The PS increases on either side of this optimum. This correlates with their changes in accuracy as a function of weight decay. ResNets and ViTs achieve their best accuracies at these weight decay values and decrease in either direction.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Label Smoothing and Dropout", "weight": 1.0} -->

Across all our controlled settings, label smoothing and dropout are the only hyperparameters that decrease both PS and accuracy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Label Smoothing and Dropout", "weight": 1.0} -->

Varying label smoothing produces less drastic changes in accuracy as compared to other hyperparameters. In Fig. 9a, a very weak positive correlation exists between accuracy and PS for ResNet-50 and ResNet-200. In Fig. 9b, PS of ResNet-50 and ResNet 200 decrease with more label smoothing, while the Vision Transformers and ResNet-6 are almost invariant. Our results indicate that clean labels are necessary to obtain high PS. However, varying label smoothing does not change accuracy a great deal within each architecture class, so the dynamic range is insufficient to observe the inverse-U relationship.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Label Smoothing and Dropout", "weight": 1.0} -->

In Figs. 9f and 9h the PS consistently decreases as a function of dropout. In Fig. 9e and Fig. 9g, it also correlates with accuracies. Curiously, dropout is the only factor to negatively influence both accuracy and PS simultaneously.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In Fig. 1, we plot the accuracy and PS from all our above experiments. While their exact relationship is architecture and hyperparameter dependent, we uncover a global Pareto frontier between PS and accuracies, see Fig. 1. Up to a certain peak, better classifiers achieve PS and beyond this peak, better accuracy hurts PS.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Scaling down improves Perceptual Scores", "weight": 1.0} -->

Our results in Section 6 prescribe a simple strategy to make an architecture's PS better: Scale down the model to reduce its accuracy till $a{(p_{max})}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Scaling down improves Perceptual Scores", "weight": 1.0} -->

Table 1 summarizes the improvements in PS obtained by scaling down each model across every hyperparameter. With the exception of ViT-L/4, across all architectures, early stopping yields the highest improvement in PS. In addition, early stopping is the most efficient strategy as there is no need for an expensive grid search.

<!-- chunk {"id": "body-0055", "role": "body", "section": "How much does PS improvement cost in terms of accuracy?", "weight": 1.0} -->

Fig. 10 shows the accuracy-PS Pareto frontier for ResNet-200 and ViT-B/8. Each point on the Pareto frontier denotes the maximum possible achievable accuracy for a given PS. The gray line is the reference Pareto-frontier obtained from training networks with their default settings. Except for Width + ViT-B/8 that lies below the reference Pareto frontier, all curves lie very close to the reference Pareto frontier. Early-stopping any of the architectures to improve their PS, as seen in Table 1, greatly reduces their accuracy.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The inverse-U phenomenon persists with improved perceptual similarity functions", "weight": 1.0} -->

We first posit that the perceptual similarity function is suboptimal, and an alternative would not yield an inverse-U relationship.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The inverse-U phenomenon persists with improved perceptual similarity functions", "weight": 1.0} -->

The perceptual similarity function in averages per-pixel differences across the spatial dimensions of the image. This assumes a direct correspondence between pixels, which may not hold for warped, translated or rotated images. For a similarity function that compares global representations of images, the inverse-U relationship may no longer exist. We investigate two such functions in two different settings: 1) Out-of-the-box ResNets and EfficientNets. 2) ResNet-200 as a function of train steps.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Mean Pool", "weight": 1.0} -->

In Figs. 11a and 11b, we present scatter plots between accuracy and PS with the style and mean pool similarity functions. Fig. 11a displays the accuracy and PS of ResNets and EfficientNets trained with their default hyperparameters. Each point in Fig. 11b represents a ResNet-200 model at a different epoch during the course of training.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Mean Pool", "weight": 1.0} -->

Both functions yield better PS than the baseline ("Local"). In Fig. 11a ResNet-6 with its Mean Pool and Style variants outperform the baseline (local) 69.1 with scores of 69.7 and 69.5 respectively. In Fig. 11b for an early-stopped ResNet-200 model, the mean pool and style functions improve upon the baseline score of 69.5 with 69.8 and 69.7 respectively.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Mean Pool", "weight": 1.0} -->

We additionally observe that the optimal early-stopped ResNet-6 from Table 1 further improves its performance with its mean pool variant achieving a PS of 70.2. This matches the best reported PS, where the AlexNet model is trained from scratch on the BAPPS train set. Note that none of our networks have seen the BAPPS train set during ImageNet training.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Mean Pool", "weight": 1.0} -->

However, although the improved perceptual functions attain better PS as compared to the baseline, the inverse-U correlation is still prominent. Therefore, we can conclude that while the per-pixel comparison function is suboptimal, it is not the main cause of the inverse correlation between accuracy and PS.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Learned linear layer on pretrained features", "weight": 1.0} -->

Lastly we investigate what happens if the similarity function is learned on supervised data. Although the main goal of our paper is to assess the inherent perceptual properties of ImageNet models, we may also train a linear layer on top of pretrained ImageNet features to match supervised human judgements on BAPPS. The PS gap between ResNet-6 and ResNet-200 narrows down from 1.5 to 0.8, but even after training, the ResNet-6 still outperforms the ResNet-200. See Appendix C for more details.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Low PS models are not necessarily less sensitive to distortions", "weight": 1.0} -->

Here, we explore whether sensitivity to distortions is the common latent factor influencing both PS and accuracy. Intuitively, better networks will be less sensitive to the distortions in the BAPPS dataset, since the class will not change under these distortions. This intuition is supported by results that show that accuracy under distribution shifts (including artificial corruptions) correlates strongly with "clean" ImageNet accuracy. Therefore, if decreased sensitivity is related to poorer PS, due to inability to distinguish different class-preserving perturbations, then this could explain our observations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Low PS models are not necessarily less sensitive to distortions", "weight": 1.0} -->

From the BAPPS dataset, we retain only the examples, where the human raters unanimously agree that one of the target patches is closer to the reference patch than the other, i.e $p = 1.0$ or $p = 0.0$. For each such triplet ($x_{0},x,x_{1}$) where $p = 1.0$ or $p = 0.0$, we denote $x_{f}$ to be the farther patch and $x_{n}$ to be the nearer patch. Concretely, in Eq 2, when ${p = 1.0},{{x_{f} = x_{0}},{x_{n} = x_{1}}}$ or ${p = 0.0},{{x_{f} = x_{1}},{x_{n} = x_{0}}}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Low PS models are not necessarily less sensitive to distortions", "weight": 1.0} -->

We measure distortion sensitivity using the distance margin ${{\mathbb{E}}_{x,x_{f}}d{(x,x_{f})}} - {{\mathbb{E}}_{x,x_{n}}d{(x,x_{n})}}$. We expect this margin to be larger for a distortion sensitive network. In Fig. 12a, among out-of-the-box classification networks, there exists no positive correlation between distortion sensitivity and PS. As another experiment, in Fig. 12b, we plot ${\mathbb{E}}_{x,x_{f}}d{(x,x_{f})}$ (Farther Patch) and ${\mathbb{E}}_{x,x_{n}}d{(x,x_{n})}$ (Nearer Patch) as a function of training epochs (ResNet-200). From Fig. 5b, we know that PS decreases as a function of epochs after it reaches a peak.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Low PS models are not necessarily less sensitive to distortions", "weight": 1.0} -->

However in Fig. 12b, the distance margin between the farther and nearer patch remains fairly constant as a function of epochs. Hence, low PS models are not necessarily less sensitive to distortions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Sub-optimal features are not a cause of the inverse-U relationship", "weight": 1.0} -->

Remember, PS is averaged over many layers, see Eq 2. However, it might be the case that optimal features for PS are buried in specific layers for better classifiers (e.g. lower layers), while other layers (e.g. high layers) exhibit different behaviour more optimal for classification. Therefore, we look at the best PS across layers.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Sub-optimal features are not a cause of the inverse-U relationship", "weight": 1.0} -->

The optimal $l$ for all depths is 3, and larger depths attain worse PS even at this optimal $l$. We additionally see that in Fig. 13b, ResNet-200 under-performs the optimal layer-wise PS of its early-stopped variant at $l = 3$. Therefore, we can conclude that sub-optimal features are not a cause of the inverse-U relationship.

<!-- chunk {"id": "body-0069", "role": "body", "section": "ImageNet class granularity cannot explain why ResNet-6 outperforms ResNet-200 on PS", "weight": 1.0} -->

ImageNet is a 1000 class classification problem that includes fine-grained classes. A classifier that models such classes successfully could have a reduced PS, since it could compromise on learning general features. The low accuracy of ResNet-6 implies that its capacity is sufficient to model only a subset of these classes, and its inability to model tougher classes might explain its high PS. We create random subsets having number of classes ranging from 50 to 900 and train ResNet-6 and ResNet-200 networks on each of these subsets. In Fig. 14, the PS gap between ResNet-200 and ResNet-6 reduces as the number of classes are decreased. But, ResNet-200 still underperforms ResNet-6. Therefore, class granularity cannot fully explain why a less-accurate ResNet-6 significantly outperforms ResNet-200 on PS. In Appendix E, we show similar results with a class subset selection strategy guided by a pretrained ResNet-6.

<!-- chunk {"id": "body-0070", "role": "body", "section": "High PS features do not necessarily have high entropy", "weight": 1.0} -->

Wang et al. show that ResNets are not suitable for style transfer due to the presence of skip connections. Skip connections result in features with low entropy which prevent capturing all style modes from a ground-truth style image. We explore if the mean entropy of activations can explain the inverse-U phenomenon between PS and accuracy. As done in Wang et al., we convert intermediate activations $x \in \mathcal{R}^{H \times W \times C}$ into a probability distribution across $H \times W \times C$ values by applying a softmax transformation. We then report the average normalized entropy of this distribution across four 2-D representations on the BAPPS validation set.

<!-- chunk {"id": "body-0071", "role": "body", "section": "High PS features do not necessarily have high entropy", "weight": 1.0} -->

Fig. 15a plots the normalized entropy of each of the four ResNet-200 reduction stages (marked 1 - 4) across training. As seen in Wang et al., representations closer to the output at later reduction stages have a much lower entropy than representations closer to the input at earlier reduction stages. The entropy also decreases as a function of train steps. For the first few training epochs, where the entropy is between 0.9 and 1.0, there is a negative correlation between PS and mean activation entropy. Note that the maximum entropy is at initialization and not after a few training epochs where ResNet-200 obtains its highest PS. After the first few epochs, there is a positive correlation where entropy and PS both decrease during training. Fig 15a suggests that there is a optimal entropy as a function of train steps, where the PS peaks.

<!-- chunk {"id": "body-0072", "role": "body", "section": "High PS features do not necessarily have high entropy", "weight": 1.0} -->

However, Fig. 15d shows that there is almost no correlation between entropy and PS across ResNets with various depths. ResNet-6 achieves the highest PS at a mean entropy of $\approx 0.5$ while ResNet-50 features have the highest entropy around 0.7 and have a much lower PS of 68.0. Therefore, entropy does not fully explain the observed effect.

<!-- chunk {"id": "body-0073", "role": "body", "section": "High PS features do not necessarily have high entropy", "weight": 1.0} -->

We remove all skip connections in the ResNets to increase the entropy of the intermediate features as done in Wang et al.. Note that the maximum depth that we are able to successfully train without skip connections is 50. In Fig. 16a, removing skip connections increase the entropy across all depths. Specifically, ResNet-50 has a huge increase in entropy, making the activations close to a uniform distribution. Even after removing the skip connections in Fig. 16b and Fig. 16c, ResNet-6 and early-stopped ResNets attain the highest PS respectively similar to the baseline ResNets. While increasing the entropy of intermediate features can improve results of ResNets on style transfer, they don't improve PS.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Low PS models are not necessarily more reliant on high frequency information for classification", "weight": 1.0} -->

Networks that rely more on high-frequency information for classification could be less robust to high-frequency distortions or removal of high frequencies from an image, and as an effect have low PS. We analyze the relationship between spatial frequency sensitivity of different networks and their PS. A low-pass square filter of side $r$ filters out the high frequencies in an image outside a square with edge length $r$ in its Fourier spectrum. We measure the "normalized accuracy", which is the accuracy on low-pass filtered images divided by its accuracy on clean images as a function of $r$. A model more reliant on high frequency information will have a higher "normalized accuracy" slope at high values of $r$. ResNet-6 has a higher "normalized accuracy" slope at a high $r = 40$ to $50$ as compared to ResNet-6 (Fig. 17b). Despite being more reliant on higher spatial frequencies, ResNet-6 achieves a higher PS compared to ResNet-200. Similarly, ResNet 200 becomes more reliant on higher spatial frequencies if it is early stopped (Fig. 17a), while also increasing its PS (Fig. 5b).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Low PS models are not necessarily more reliant on high frequency information for classification", "weight": 1.0} -->

These results indicate that models that have low PS are not necessarily more reliant on high frequency information for classification.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Code Release", "weight": 1.0} -->

We release ResNet-6, ResNet-50 and ResNet-200 checkpoints at every 1000 steps over here. The models were trained using the opensource TPU codebase with the following changes on 64x64 ImageNet.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we explore the question if better classifiers can serve as better feature extractors for perceptual metrics. To answer this question, we conduct experiments across ResNets and ViTs across many different hyperparameters. Except for label smoothing and dropout, we see that PS exhibits an inverse-U relationship with accuracy across the hyperparameters we considered. We then probe a number of explanations for the inverse-U relationship involving skip connections, Global Similarity Functions, Distortion Sensitivity, Layer-wise Perceptual Scores, Spatial Frequency, Sensitivity, and ImageNet Class Granularity. While none of these explanations can offer an explanation for the observed tradeoff between ImageNet accuracy and perceptual similarity, we hope our paper opens the door for further research in this area.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Broader Impact Statement", "weight": 1.0} -->

Our results are based on BAPPS, which consists of exclusively low-level distortions as opposed to high-level semantic differences. We believe low-level distortions such as gaussian blur and color distortions are less likely to be susceptible to bias across different human categories as compared to high-level semantic features such as facial features. It is an open and interesting question whether different categories of humans like race and gender perceive low-level distortions differently. Increasing the diversity of both distortions and human labels in future perceptual similarity datasets is another interesting direction that might help to mitigate human biases.
