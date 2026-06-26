<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HAT: Hybrid Attention Transformer for Image Restoration

Topics include Image restoration, Image super-resolution, Vision transformers, Hybrid attention, Channel attention, Window attention, Overlapping cross-attention, Denoising, Compression artifact reduction, HAT.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This extended HAT paper generalizes the hybrid-attention transformer from super-resolution to a broader image-restoration family, including denoising and compression-artifact reduction. It is useful as the more complete HAT reference because it reports scaling behavior and broader restoration coverage.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Transformer-based methods have shown impressive performance in image restoration tasks, such as image super-resolution and denoising. However, we find that these networks can only utilize a limited spatial range of input information through attribution analysis. This implies that the potential of Transformer is still not fully exploited in existing networks. In order to activate more input pixels for better restoration, we propose a new Hybrid Attention Transformer (HAT). It combines both channel attention and window-based self-attention schemes, thus making use of their complementary advantages. Moreover, to better aggregate the cross-window information, we introduce an overlapping cross-attention module to enhance the interaction between neighboring window features. In the training stage, we additionally adopt a same-task pre-training strategy to further exploit the potential of the model for further improvement. Extensive experiments have demonstrated the effectiveness of the proposed modules. We further scale up the model to show that the performance of the SR task can be greatly improved. Besides, we extend HAT to more image restoration applications, including real-world image super-resolution, Gaussian image denoising and image compression artifacts reduction.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiments on benchmark and real-world datasets demonstrate that our HAT achieves state-of-the-art performance both quantitatively and qualitatively. Codes and models are publicly available at

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Image restoration (IR) is a classic problem in computer vision. It aims to reconstruct a high-quality (HQ) image from a given low-quality (LQ) input. Classic IR tasks encompass image super-resolution, image denoising, compression artifacts reduction, and etc. Image restoration plays an important role in computer vision and has widespread application in areas such as AI photography, surveillance imaging, medical imaging, and image generation. Since deep learning has been successfully applied to IR tasks, numerous methods based on the convolutional neural network (CNN) have been proposed and almost dominate this field in the past few years. Recently, due to the success in natural language processing, Transformer has attracted increasing attention in the computer vision community. After making rapid progress on high-level vision tasks, Transformer-based methods are also developed for low-level vision tasks. A sucessful example is SwinIR, which obtains a breakthrough improvement on IR tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its success, existing work has rarely discussed why Transformer outperforms CNN. An intuitive explanation provided in prior study is that Transformer benefits from the self-attention mechanism, allowing it to leverage long-range information. To verify whether this is indeed the case for image restoration, we take image super-resolution (SR) as an example task and employ an attribution analysis method --- Local Attribution Map (LAM) to examine the range of information used in SwinIR. Interestingly, we find that although SwinIR achieves higher average quantitative performance, it does NOT utilize more input pixels than CNN-based methods (e.g., RCAN ), as shown in Fig. 2. This contradicts the conclusion in LAM that there is a positive correlation between the range of information a network uses and its reconstruction performance. Since the aforementioned conclusion is primarily derived from networks of the same type (i.e., CNNs), we believe that the superior performance of SwinIR can be attributed to its stronger ability to model local information compared to CNN. However, it is also limited by the restricted range of information it utilizes, leading to inferior results on samples where broader contextual information could produce better outcomes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Additionally, we observe block artifacts in the intermediate features of SwinIR, as shown in Fig. 4, suggesting that the shifted window mechanism does not fully achieve cross-window information interaction. This may be one of the reasons why SwinIR does not achieve better long-range information utilization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the above-mentioned limitations of the existing IR Transformer and further develop the potential of such networks, we propose a Hybrid Attention Transformer, namely HAT. It combines channel attention and self-attention schemes, in order to take advantage of the former's capability in using global information and the powerful representative ability of the latter. Besides, we introduce an overlapping cross-attention module to achieve more direct interaction of adjacent window features. Benefiting from these designs, our model can activate more pixels for reconstruction and thus obtains significant performance improvement. Since Transformers do not have an inductive bias like CNNs, large-scale data pre-training is important to unlock the potential of such models. In this paper, we provide an effective same-task pre-training strategy. Different from IPT using multiple restoration tasks for pre-training and EDT utilizing multiple degradation levels of a specific task for pre-training, we directly perform pre-training using large-scale dataset on the same task. We believe that large-scale data is what really matters for pre-training. Experimental results show the superiority of our strategy.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Equipped with the above designs, HAT surpasses the state-of-the-art methods by a large margin on SR, as well as several other image restoration tasks, as shown in Fig. 1.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, our main contributions are four-fold: We design a Hybrid Attention Transformer (HAT) that combines self-attention, channel attention and a new overlapping cross-attention for high-quality image restoration.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose an effective same-task pre-training strategy to further exploit the potential of SR Transformer and show the importance of large-scale data pre-training.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method significantly outperforms existing state-of-the-art methods on the SR task. By further scaling up HAT to build a large model, we greatly extend the performance upper bound of the SR task.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method also achieves state-of-the-art performance on image denoising and compression artifacts reduction, showing its superiority on various image restoration tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

A preliminary version of this work was presented at CVPR2023. The present work expands upon the initial version in several significant ways. Firstly, we provide a theoretic illustration of LAM and augment the analysis with CEM results. This can facilitate readers' understanding of the motivation behind our method and the rationality of its design. Secondly, we investigate a flexible plain architecture of HAT for application to various IR tasks, allowing us to further explore the potential breadth of this method. Thirdly, we extend HAT to real-world image super-resolution based on practical degradation models. The promising results show the potential of HAT for real-world applications. Additionally, we further extend HAT for image denoising and compression artifacts reduction. Extensive experiments show that our method achieves state-of-the-art performance on several IR tasks.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Image Super-Resolution", "weight": 1.0} -->

Since SRCNN first introduces deep convolution neural networks (CNNs) to the image SR task and obtains superior performance over conventional SR methods, numerous deep networks have been proposed for SR to further improve the reconstruction quality. For instance, many methods apply more elaborate convolution module designs, such as residual block and dense block, to enhance the model representation ability. Several works explore more different frameworks like recursive neural network and graph neural network. To improve perceptual quality, introduce adversarial learning to generate more realistic results. By using attention mechanism, achieve further improvement in terms of reconstruction fidelity. Recently, a series of Transformer-based networks are proposed and constantly refresh the state-of-the-art of SR task, showing the powerful representation ability of Transformer.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Image Super-Resolution", "weight": 1.0} -->

To deepen the understanding of SR networks, several studies are conducted to analyze and interpret their working mechanism. LAM adopts the integral gradient method to explore which input pixels contribute to the final performance. DDR reveals the deep semantic representations in SR networks based on deep feature dimensionality reduction and visualization. FAIG is proposed to find discriminative filters for specific degradations in blind SR. introduces channel saliency map to show that Dropout can help prevent co-adapting for real SR networks. SRGA aims to evaluate the generalization ability of SR methods. CEM interprets the low-level vision models based on causal effect theory. In this work, we exploit LAM and CEM to analyze and understand the behavior of different networks.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Vision Transformer", "weight": 1.0} -->

Recently, Transformer has attracted the attention of computer vision community due to its success in the field of natural language processing. A series of Transformer-based methods have been developed for high-level vision tasks, including image classification, object detection, segmentation, etc. Although vision Transformer has shown its superiority on modeling long-range dependency, there are still many works demonstrating that the convolution can help Transformer achieve better visual representation. Due to the impressive performance, Transformer has also been introduced for low-level vision tasks. Specifically, IPT develops a ViT-style network and introduces multi-task pre-training for image processing. SwinIR proposes an image restoration Transformer based. VRT introduces Transformer-based networks to video restoration. EDT adopts self-attention mechanism and multi-related-task pre-training strategy to further refresh the state-of-the-art of SR. However, existing works still cannot fully exploit the potential of Transformer, while our method can activate more input pixels for better reconstruction.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Deep Networks for Image Restoration", "weight": 1.0} -->

Image restoration, which aims to recover high-quality images from degraded inputs, has seen significant progress with the rise of deep learning. Early successes are achieved in tasks like image super-resolution, image denoising, and compression artifact reduction. Numerous CNN-based networks have since been proposed for image restoration. Before the advent of Transformers in low-level vision tasks, CNNs dominated the field. For example, ARCNN employs stacked convolutional layers to address JPEG compression artifacts, and DnCNN combines convolution with batch normalization for image denoising. RDN introduces a residual dense CNN architecture, excelling in various restoration tasks. A comprehensive investigation of CNN-based methods for SR can be found. As Transformers have gained prominence in computer vision, Transformer-based image restoration methods have emerged. SwinIR, built on the Swin Transformer, demonstrates excellent performance on image super-resolution, denoising, and JPEG artifact reduction. Uformer introduces a U-Net-style Transformer for diverse restoration tasks, while Restormer innovates with transposed self-attention to achieve state-of-the-art results.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Deep Networks for Image Restoration", "weight": 1.0} -->

SCUNet combines CNNs and Transformers to create a highly effective denoising network. Transformer-based networks have demonstrated superior performance compared to previous CNN-based methods. In this paper, we introduce a hybrid attention mechanism, further improving the performance of image restoration Transformer.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Motivation", "weight": 1.0} -->

Swin Transformer has already demonstrated excellent performance in image restoration tasks. We are thus eager to understand what makes it superior to CNN-based methods and what its potential shortcomings are that could be improved. To explore these questions, we seek to derive insights using interpretability tools and visualization analysis. Given that existing IR Transformer shows remarkable advancements on SR, and that the analytical tools developed for SR are more mature, we focus our analysis primarily on SR. In this section, we present the motivation behind our approach. We begin by reviewing the LAM method, an attribution analysis tool for SR networks. Next, we apply LAM to several classical SR networks and augment the results with causal analysis using the Causal Effect Map (CEM). Finally, we present feature visualization results that provide additional insights.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A An Overview of LAM", "weight": 1.0} -->

Local Attribution Map (LAM) is an attribution analysis method tailored for image SR. It extends the classical integrated gradients by introducing a task-specific baseline and path function suited to the characteristics of SR networks, which focus on reconstructing high-frequency details such as textures and edges.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A An Overview of LAM", "weight": 1.0} -->

Formally, let $F:\mathbb{R}^{n}\rightarrow\mathbb{R}^{k}$ denote an SR network, $I$ be the input image, and $I^{\prime}$ be the baseline input. The path-integrated gradients along the $i$-th dimension are computed as: where $\lambda(\theta)$ defines a smooth interpolation from $I^{\prime}$ to $I$. Unlike classification tasks where $I^{\prime}$ is typically a black image, LAM defines $I^{\prime}$ as a blurred version of $I$: where $\omega(\sigma)$ is a Gaussian kernel with standard deviation $\sigma$, and $\otimes$ denotes convolution. The path function $\lambda_{\mathrm{pb}}(\theta)$ progressively reduces the blur: so that $\lambda_{\mathrm{pb}}=I^{\prime}$ and $\lambda_{\mathrm{pb}}=I$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A An Overview of LAM", "weight": 1.0} -->

To assess how input pixels contribute to the reconstruction of high-frequency details, LAM applies a gradient-based detector $D_{xy}$ (e.g., Gabor filter) to a patch centered at $(x,y)$: where $\nabla_{mn}I$ denotes the image gradient and $\mathcal{P}_{xy}$ is the local patch. The final attribution score for the $i$-th pixel is then: As illustrated in Fig. 2, LAM provides spatial heatmaps that visualize the importance of each input pixel to the reconstruction of structural details. To quantify the spatial extent of utilized information, LAM further defines the Diffusion Index (DI), a metric derived from the Gini coefficient, where a larger DI reflects a broader and more uniform use of input pixels, often correlating with better reconstruction quality.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A An Overview of LAM", "weight": 1.0} -->

While LAM is effective for SR, its extension to other restoration tasks such as denoising or compression artifact reduction remains an open challenge. This is because LAM depends on a well-defined baseline and a continuous degradation path, both of which are difficult to establish in tasks with stochastic or non-differentiable degradations (e.g., Gaussian noise). Defining a "more noisy" baseline and constructing a semantically meaningful interpolation path is non-trivial and may lead to unstable or unreliable attribution results. We thus conduct LAM experiments merely on SR.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Interpretability Analysis", "weight": 1.0} -->

We first employ LAM to perform attribution analysis on several classic SR networks, as shown in Fig. 2. Intuitively, SR networks that utilize more input information achieve superior reconstruction performance. This relationship is clearly observed in the comparison between EDSR and RCAN. However, this conclusion is the opposite in the comparison between RCAN and SwinIR. SwinIR achieves better reconstruction results despite utilizing significantly less input information. First, this LAM observation contradicts the intuition in existing literature, which suggests that Transformers perform better by more effectively modeling long-range dependency. Second, it means that SwinIR, which employs a window-based self-attention mechanism, excels at capturing local information and can achieve superior performance with less input information. Additionally, we observe that SwinIR produces incorrect texture reconstruction in case where RCAN successfully restores the texture, which may be attributed to SwinIR's limited information utilization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Interpretability Analysis", "weight": 1.0} -->

To further analyze these behaviors, we use the Causal Effect Map (CEM), which measures how each input patch affects the reconstruction of the region of interest (ROI), marked in green in Fig. 3. Patches with positive or negative causal effects are shown in red and blue, respectively. The pie chart indicates the distribution of effects, and the color bar reflects the magnitude. Although all examples in Fig. 3 share similar striped patterns, the amount of useful detail in the ROI of the LQ input varies. For reference, all examples are reconstructed from the same LQ image shown in the bottom-left of Fig. 2. In example (b), the ROI contains almost no visible texture in the input. The model must therefore rely on surrounding patches to infer the structure, resulting in many patches showing positive causal effects. In contrast, examples (a) and (c) contain clearer directional patterns in the ROI. In these cases, the model can mainly rely on local information, and using too much external context may introduce conflicting signals, leading to negative causal effects. This behavior aligns with causal reasoning: when the internal evidence is weak, external information supports the reconstruction; when internal evidence is strong, external input may act as a confounder.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Interpretability Analysis", "weight": 1.0} -->

Our HAT adapts well to both situations. It activates a wide range of input pixels when needed (e.g., example b), and focuses more locally when the ROI already contains useful information (e.g., examples a and c). This flexibility results in more accurate textures and sharper edges across diverse scenarios.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Interpretability Analysis", "weight": 1.0} -->

In conclusion, we posit that the performance of SR networks depends not only on the quantity of activated information but also on how effectively the model adapts to the local content. Enhancing both the usable spatial range and context-awareness is essential for developing more powerful SR models.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Feature Visualization", "weight": 1.0} -->

SwinIR, as a new architecture distinct from traditional CNN designs, motivates us to examine its intermediate features to gain further insights. As shown in Figure 4, we observe noticeable block artifacts in SwinIR. Interestingly, the size of these blocks coincides with the window size, suggesting that these artifacts are likely caused by the window partitioning mechanism. This indicates that the shifted window approach may be insufficient for effectively integrating information across windows. This limitation could be one of the reasons why SwinIR fails to utilize more pixels for reconstruction, as evidenced in Figures 2 and 3. Several studies on high-level vision tasks have also pointed out that enhancing connections between windows can improve window-based self-attention mechanisms. Consequently, we enhance the interaction of information across windows in our method. We can see that the block artifacts in the intermediate features of our HAT are significantly alleviated.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Methodology", "weight": 1.0} -->

Based on the above analysis, we aim to design a better image restoration network by enhancing the ability of the existing Transformer model to efficiently utilize more input information, integrating global information, and improving the cross-window interaction. In this section, we provide a detailed introduction to our approach, HAT, including the overall architecture, key module designs, training strategy, implementation details, as well as discussions with other methods.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Network Structure of HAT", "weight": 1.0} -->

The overall network structure of HAT follows the classic Residual in Residual (RIR) architecture similar to. As shown in Fig. 5, HAT consists of three parts, including shallow feature extraction, deep feature extraction and image reconstruction. Concretely, for a given low-quality (LQ) input image $I_{LQ}\in\mathbb{R}^{H\times W\times C_{in}}$, we use one $3\times 3$ convolution layer $H_{SF}(\cdot)$ to extract the shallow feature $F_{0}\in\mathbb{R}^{H\times W\times C}$ as: where $C_{in}$ and $C$ denote the channel number of the input and the intermediate feature, respectively. The shallow feature extraction can simply map the input from low-dimensional space to high-dimensional space, while achieving the high-dimensional embedding for each pixel token. Moreover, the early convolution layer can help learn better visual representation and lead to stable optimization.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Network Structure of HAT", "weight": 1.0} -->

We then perform deep feature extraction $H_{DF}(\cdot)$ to further obtain the deep feature $F_{DF}\in\mathbb{R}^{H\times W\times C}$ as: where $H_{DF}(\cdot)$ consists of $N_{1}$ residual hybrid attention groups (RHAG) and one $3\times 3$ convolution layer $H_{Conv}(\cdot)$. These RHAGs progressively process the intermediate features as: where $H_{RHAG_{i}}(\cdot)$ represents the $i$-th RHAG. Following, we also introduce a convolution layer at the tail of this part to better aggregate information of deep features. After that, we add a global residual connection to fuse shallow features and deep features, and then reconstruct the high-quality (HQ) result via a reconstruction module as: where $H_{Rec}(\cdot)$ denotes the reconstruction module.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Network Structure of HAT", "weight": 1.0} -->

We adopt the pixel-shuffle method to up-sample the fused feature for the SR task shown in Fig. 5(a), and use two convolutions for the tasks where have the input and output have the same resolution shown in Fig. 5(b). The key component RHAG consists of $N_{2}$ hybrid attention blocks (HAB), one overlapping cross-attention block (OCAB), one $3\times 3$ convolution layer, with a residual connection, as presented in Fig. 5(c).

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

In this section, we detail our proposed Hybrid Attention Block (HAB), illustrated in Fig. 5(d). HAB adopts a structure similar to the standard Swin Transformer block, preserving the window-based self-attention mechanism. However, we enhance the representative ability of self-attention and introduce a channel attention block to capture global information. As discussed in Sec.III, we aim to activate more input pixels for Transformer to achieve stronger reconstruction capability. Unlike convolution that expands the receptive field by stacking layers, self-attention possesses a global receptive field within its scope. Therefore, a natural approach to expand the range of information utilized by window-based self-attention is to enlarge the window size. Previous work limits the window size used for self-attention calculations to a small range (i.e., 7 or 8), relying on a shifted window mechanism to gradually expand the receptive field. While this method reduces computational cost, it compromises the effectiveness of self-attention. As discussed in Sec. V-A, we find that window size is a crucial factor influencing the ability of window-based self-attention to exploit information.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

Appropriately increasing the window size can significantly improve the Transformer's performance. Therefore, in HAB, we adopt a larger window size (i.e., 16).

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

In addition to window-based self-attention, global information can also be captured by incorporating channel attention. We think that global information may help for cases where many similar textures are present, as shown in Fig.3. Moreover, several studies have demonstrated that channel-wise dynamic mapping is beneficial for low-level vision tasks. Therefore, we introduce the channel attention mechanism into our network. Given the evidence that convolution can improve the visual representation of Transformer models and facilitate easier optimization, we incorporate a channel attention-based convolution block, referred to as the channel attention block (CAB), into the standard Transformer block to construct our HAB (see Fig. 5(f)). In addition, global information can be utilized when channel attention is adopted, as it is involved to calculate the channel attention weights. We think that the global information may help for cases where many similar textures exist, such as the examples given in Fig. 2. Besides, several works have demonstrated that the channel-wise dynamic mapping is beneficial for low-level vision tasks. Therefore, we want to introduce the channel attention mechanism to our network.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

Since many works have shown that convolution can help Transformer get better visual representation or achieve easier optimization, we incorporate a channel attention-based convolution block, i.e., the channel attention block (CAB) in Fig. 5(f), into the standard Transformer block to build our HAB.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

To avoid the possible conflict of CAB and MSA on optimization and visual representation, we combine them in parallel and set a small constant $\alpha$ to control the weight of the CAB output. Overall, for a given input feature $X$, the whole process of HAB is computed as: where $X_{N}$ and $X_{M}$ denote the intermediate features. $Y$ represents the output of HAB. LN represents the layer normalization operation and MLP denotes a multi-layer perceptron. (S)W-MSA means the standard and shifted window multihead self-attention modules. Especially, we treat each pixel as a token for embedding (i.e., set patch size as 1 for patch embedding following). For calculation of the self-attention module, given an input feature of size $H\times W\times C$, it is first partitioned into $\frac{HW}{M^{2}}$ local windows of size $M\times M$, then self-attention is calculated inside each window.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

For a local window feature $X_{W}\in\mathbb{R}^{M^{2}\times C}$, the query, key and value matrices are computed by linear mappings as $Q$, $K$ and $V$. Then the window-based self-attention is formulated as: where $d$ represents the dimension of query/key. $B$ denotes the relative position encoding and is calculated as. Besides, to build the connections between neighboring non-overlapping windows, we also use the shifted window partitioning approach, with the shift size set to half of the window size.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Hybrid Attention Block", "weight": 1.0} -->

A CAB consists of two standard convolution layers with GELU activation and a channel attention (CA) module, as shown in Fig.5(f). Since Transformer-based structures often require a large number of channels for token embedding, directly using convolutions with constant width would result in high computational costs. To address this, we compress the number of channels in the two convolution layers by a constant factor $\beta$. For an input feature with $C$ channels, the number of channels is reduced to $\frac{C}{\beta}$ after the first convolution layer, and then expanded back to $C$ channels through the second layer. Finally, a standard CA module is employed to adaptively rescale channel-wise features.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Overlapping Cross-Attention Block (OCAB)", "weight": 1.0} -->

We introduce OCAB to directly establish cross-window connections and enhance the representative ability for the window self-attention. Our OCAB consists of an overlapping cross-attention (OCA) layer and an MLP layer similar to the standard Swin Transformer block. But for OCA, as depicted in Fig. 6, we use different window sizes to partition the projected features. Specifically, for the $X_{Q},X_{K},X_{V}\in\mathbb{R}^{H\times W\times C}$ of the input feature $X$, $X_{Q}$ is partitioned into $\frac{HW}{M^{2}}$ non-overlapping windows of size ${M}\times{M}$, while $X_{K},X_{V}$ are unfolded to $\frac{HW}{M^{2}}$ overlapping windows of size ${M_{o}}\times{M_{o}}$. It is calculated as where $\gamma$ is a constant to control the overlapping size.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Overlapping Cross-Attention Block (OCAB)", "weight": 1.0} -->

To better understand this operation, the standard window partition can be considered as a sliding partition with the kernel size and the stride both equal to the window size $M$. In contrast, the overlapping window partition can be viewed as a sliding partition with the kernel size equal to $M_{o}$, while the stride is equal to $M$. Zero-padding with size $\frac{\gamma M}{2}$ is used to ensure the size consistency of overlapping windows. The attention matrix is calculated as Eq., and the relative position bias $B\in\mathbb{R}^{M\times M_{o}}$ is also adopted. Unlike WSA whose query, key and value are calculated from the same window feature, OCA computes key/value from a larger field where more useful information can be utilized for the query. Note that although Multi-resolution Overlapped Attention (MOA) module in performs similar overlapping window partition, our OCA is fundamentally different from MOA. MOA calculates global attention using window features as tokens, while OCA computes cross-attention inside each window using pixel tokens.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-D The Same-task Pre-training", "weight": 1.0} -->

Pre-training is proven effective on many high-level vision tasks. Recent works also demonstrate that pre-training is beneficial to low-level vision tasks. IPT emphasizes the use of various low-level tasks, such as denoising, deraining, SR and etc., while EDT utilizes different degradation levels of a specific task to do pre-training. These works focus on investigating the effect of multi-task pre-training for a target task. In contrast, we directly perform pre-training on a larger-scale dataset (i.e., ImageNet ) based on the same task, showing that the effectiveness of pre-training depends more on the scale and diversity of data. For example, when we want to train a model for $\times 4$ SR, we first train a $\times 4$ SR model on ImageNet, then fine-tune it on the specific dataset, such as DF2K. The proposed strategy, namely same-task pre-training, is simpler while bringing more performance improvements. It is worth mentioning that sufficient training iterations for pre-training and an appropriate small learning rate for fine-tuning are very important for the effectiveness of the pre-training strategy.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-D The Same-task Pre-training", "weight": 1.0} -->

We think that it is because Transformer requires more data and iterations to learn general knowledge for the task, but needs a small learning rate for fine-tuning to avoid overfitting to the specific dataset.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-E Discussions", "weight": 1.0} -->

In this part, we analyze the distinctions of our HAT and several relevant works, including SwinIR, EDT, SCUNet and HaloNet.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-E Discussions", "weight": 1.0} -->

Difference to SwinIR. SwinIR is the first work to successfully use Swin Transformer for low-level vision tasks. It builds an image restoration network by using the original Swin Transformer block. Our HAT is inspired by SwinIR and retains the core design of window-based self-attention. However, we address the problem of limited range of utilized information in SwinIR by enlarging the window size and introducing channel attention. At the same time, we introduce a newly designed OCA to further enhance the ability to implement cross-window interaction. This work aims to design a more powerful backbone for image restoration tasks.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-E Discussions", "weight": 1.0} -->

Difference to EDT. EDT builds an image restoration Transformer based on the shifted crossed local attention, which also calculates self-attention in the windows of fixed size. For a given feature map, it splits the feature into two parts and performs self-attention in an either horizontal or vertical rectangle window. In contrast, our HAT adopts the vanilla window-based self-attention and shifted window mechanism similar to Swin Transformer. EDT also studies the pre-training strategy and emphasizes the advantages of multi-related-task pre-training (i.e., performing pre-training on a specific task with multiple degradation levels). However, HAT shows that training on the same task but using a large-scale dataset is the key factor in the effectiveness of pre-training.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-E Discussions", "weight": 1.0} -->

Difference to SCUNet. SCUNet is also an image restoration network that integrates the strengths of Transformers and CNN. It utilizes the Swin Transformer block alongside a classic convolution block within its U-Net architecture, forming a Swin-Conv Block, and achieves excellent performance for denoising. Unlike our approach that originates from the SR task, SCUNet is primarily designed for denoising, with a focus on capturing multi-scale information. In contrast, our method emphasizes the benefits of window self-attention for local information fitting and addresses its limitations in cross-window interaction and global information acquisition. Therefore, the two methods differ significantly in motivation, overall architecture and the design details of key modules.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-E Discussions", "weight": 1.0} -->

Difference to HaloNet. HaloNet incorporates a similar window partition mechanism to our OCA, enabling the calculation of self-attention within overlapping window features. HaloNet employs this overlapping self-attention as the fundamental module to build the network, inevitably leading to a large computational cost. This design could impose a substantial computational burden and is not friendly to image restoration tasks. On the contrary, our HAT leverages only a limited number of OCA modules to augment the interaction between adjacent windows. This approach can effectively enhance the image restoration Transformer without incurring excessive computational costs.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-F Implementation Details", "weight": 1.0} -->

For the structure of HAT, both the RHAG number and HAB number are set to 6. The channel number of the whole network is set to 180. The attention head number and window size are set to 6 and 16 for both (S)W-MSA and OCA. For the specific hyper-parameters of the proposed modules, we set the weighting factor of CAB output ($\alpha$), the squeeze factor between two convolution layers in CAB ($\beta$), and the overlapping ratio of OCA ($\gamma$) as 0.01, 3 and 0.5, respectively. For the large variant HAT-L, we double the depth of HAT by increasing the RHAG number from 6 to 12. We also provide a small version HAT-S with fewer parameters and similar computation to SwinIR. For HAT-S, we set the channel number to 144 and set $\beta$ to 24 in CAB. When implementing the pre-training strategy, we adopt ImageNet as the pre-training dataset following. We conduct the main experiments and ablation study on image SR.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-F Implementation Details", "weight": 1.0} -->

Therefore, we use the DF2K dataset (DIV2K +Flicker2K ) as the training dataset, following. PSNR/SSIM calculated on the Y channel is reported for the quantitative metrics.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-A Effects of Different Window Sizes", "weight": 1.0} -->

As discussed in Sec. III, activating more input pixels for the restoration tends to achieve better performance. Enlarging window size for the window-based self-attention is an intuitive way to realize the goal. To examine how the window size in self-attention affects both performance and computational efficiency of Transformer models for image SR, we conduct a series of experiments directly on the preliminary version of SwinIR, without involving newly-introduced blocks (e.g., OCAB and CAB). As shown in Tab. I, enlarging the window size from $8\times 8$ to $16\times 16$ consistently improves performance across all benchmark datasets. Especially on Urban100, we observe a significant gain of 0.36dB (from 27.45dB to 27.81dB). We also provide the qualitative comparison in Fig. 7. The result produced by the model with a larger window size has much clearer textures. For LAM results, the model with window size of 16 utilizes much more input pixels than the model with window size of 8. Meanwhile, the increase in computational cost is moderate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-A Effects of Different Window Sizes", "weight": 1.0} -->

The model size grows slightly (from 11.9M to 12.1M parameters), and Multi-Adds (counted at the input size of 64 $\times$ 64) increase by $\sim$$\%19$ (from 53.6G to 63.8G). This suggests that enlarging window size is a highly cost-effective design for improving Transformer-based SR.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Ablation Study", "weight": 1.0} -->

Effectiveness of OCAB and CAB. To verify the effectiveness of the proposed CAB and OCAB. we conduct ablation study and complexity analysis based on $\times 4$ SR and show the results in Tab. II. On Urban100, compared with the baseline results, both OCAB and CAB bring the performance gain of 0.1dB. Benefiting from the two modules, the model obtains a further performance gain of 0.16dB. On Set5 and, the proposed OCAB and CAB can also bring considerable performance improvement. Besides, we investigate the computational complexity of OCAB and CAB. While OCAB introduces a modest increase in parameters and Multi-Adds, CAB is more computationally expensive. However, both modules bring stable and significant improvements. We think that the performance improvement comes from two aspects. On the one hand, improving the window interaction by OCAB and utilizing the global statistics by CAB both help the model better deal with the long-term patters (e.g., self-similarity of repeated textures). On the other hand, the two modules enrich and enhance the model ability by introducing cross-attention and convolution blocks.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Ablation Study", "weight": 1.0} -->

We also provide qualitative comparison to further illustrate the influence of OCAB and CAB, as presented in Fig. 8. We can observe that the model with OCAB has a larger scope of the utilized pixels and generate better-reconstructed results. When CAB is adopted, the used pixels even expand to almost the full image. Moreover, the result of our method with OCAB and CAB obtains the highest DI, which means our method utilizes the most input pixels.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Ablation Study", "weight": 1.0} -->

Effects of different designs of CAB. We conduct experiments to explore the effects of different designs of CAB. The results are reported on the Urban100 dataset. First, we investigate the influence of channel attention. As shown in Tab. III, the model using CA achieves a performance gain of 0.05dB compared to the model without CA, demonstrating the effectiveness of the CA in our network. We also conduct experiments to explore the effects of the weighting factor $\alpha$ of CAB. As presented in Sec. IV-B, $\alpha$ is used to control the weight of CAB features for feature fusion. A larger $\alpha$ means a larger weight of features extracted by CAB and $\alpha=0$ represents CAB is not used. As shown in Tab. IV, the model with $\alpha=0.01$ obtains the best performance. It indicates that CAB and self-attention may have potential optimization conflict, while a small weighting factor for our CAB can suppress this issue for better combination.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B Ablation Study", "weight": 1.0} -->

Effects of the overlapping ratio. In OCAB, we set a constant $\gamma$ to control the overlapping size for the overlapping cross-attention, as illustrated in Sec IV-C ‣ IV Methodology ‣ HAT: Hybrid Attention Transformer for Image Restoration"). To explore the effects of different overlapping ratios, we set a group of $\gamma$ from 0 to 0.75 to examine the performance change, as shown in Tab. V. Note that $\gamma=0$ means a standard Transformer block. It can be found that the model with $\gamma=0.5$ performs best. In contrast, when $\gamma$ is set to 0.25 or 0.75, the model has no obvious performance gain or even has a performance drop. It illustrates that inappropriate overlapping size cannot benefit the interaction of neighboring windows.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C Analysis of Model Complexity", "weight": 1.0} -->

We analyze the computational complexity of our method from two perspectives: the impact of different CAB sizes, and a comparison between our method and SwinIR under similar computational budgets. All experiments are conducted on Urban100 for $\times$`<!-- -->`{=html}4 SR, with the number of Multiply-Add operations counted at an input size of $64\times 64$. Pre-training is not used in any model, and all results are obtained under identical training settings. Since CAB seems to be computationally expensive, we first investigate the influence of the squeeze factor $\beta$ in CAB (mentioned in Sec IV-B), which controls the channel reduction ratio. As shown in Tab. VI, adding a small CAB whose $\beta$ equals 6 can bring considerable performance improvement. When we continuously reduce $\beta$, the performance increases but with larger model sizes. To balance the performance and computations, we set $\beta$ to 3 as the default setting.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-C Analysis of Model Complexity", "weight": 1.0} -->

To further validate the efficiency of our method, we compare HAT and SwinIR with the similar numbers of parameters and Multi-Adds under two settings, as presented in Tab. VII. First, we compare HAT-S with the original version of SwinIR. With less parameters and comparable computations, HAT-S significantly outperforms SwinIR. Second, we enlarge SwinIR by increasing the width and depth to achieve similar computations to HAT, denoted as SwinIR-L1 and SwinIR-L2. HAT achieves the best performance at the lowest computational cost. This demonstrates that HAT outperforms SwinIR in performance and computational efficiency.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-C Analysis of Model Complexity", "weight": 1.0} -->

Overall, Our experiments show that properly tuning the CAB size (via $\beta$) enables flexible trade-offs between performance and complexity. Compared with SwinIR, our HAT achieves higher performance under similar or lower computational costs, in both compact and large settings. These results validate the efficiency and scalability of our proposed method.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-D Study on the Pre-training Strategy", "weight": 1.0} -->

From Tab. IX, we can see that HAT can benefit greatly from the pre-training strategy, by comparing the performance of HAT and HAT^†^. To show the superiority of the proposed same-task pre-training, we also apply the multi-related-task pre-training to HAT for comparison using full ImageNet, under the same training settings as. As depicted as Tab. VIII, the same-task pre-training performs better, not only in the pre-training stage but also in the fine-tuning process. From this perspective, multi-task pre-training probably impairs the restoration performance of the network on a specific degradation, while the same-task pre-training can maximize the performance gain brought by large-scale data. To further investigate the influences of our pre-training strategy for different networks, we apply our pre-training to four networks: SRResNet (1.5M), RRDBNet (16.7M), SwinIR (11.9M) and HAT (20.8M), as shown in Fig. 9. First, we can see that all four networks can benefit from pre-training, showing the effectiveness of the proposed same-task pre-training strategy.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Study on the Pre-training Strategy", "weight": 1.0} -->

Second, for the same type of network (i.e., CNN or Transformer), the larger the network capacity, the more performance gain from pre-training. Third, although with less parameters, SwinIR obtains greater performance improvement from the pre-training compared to RRDBNet. It suggests that Transformer needs more data to exploit the potential of the model. HAT obtains the largest gain from pre-training, indicating the necessity of the pre-training strategy for such large models. Equipped with big models and large-scale data, we show that the performance upper bound of this task can be significantly extended.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D Study on the Pre-training Strategy", "weight": 1.0} -->

Note: For fair comparison, GRL’s SSIM values are recalculated using BasicSR based on its official results, as the original reported values differ significantly. TABLE IX: Quantitative comparison with state-of-the-art methods for classic image super-resolution on benchmark datasets. The best and second best results are marked in bold and underline. “†” indicates that methods adopt pre-training strategy on ImageNet.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-A Training Settings", "weight": 1.0} -->

For classic image super-resolution, we use DF2K (DIV2K + Flicker2K) with 3450 images as the training dataset when training from scratch. The low-resolution images are generated from the ground truth images by the "bicubic" down-sampling in MATLAB. We set the input patch size to $64\times 64$ and use random rotation and horizontally flipping for data augmentation. The mini-batch size is set to 32 and total training iterations are set to 500K. The learning rate is initialized as 2e-4 and reduced by half at \[250K,400K,450K,475K\]. For $\times$`<!-- -->`{=html}4 SR, we initialize the model with pre-trained $\times$`<!-- -->`{=html}2 SR weights and halve the iterations for each learning rate decay as well as total iterations. We adopt Adam optimizer with $\beta_{1}=0.9$ and $\beta_{2}=0.99$ to train the model.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-A Training Settings", "weight": 1.0} -->

When using the same-task pre-training, we exploit the full ImageNet dataset with 1.28 million images to pre-train the model for 800K iterations. The initial learning rate is also set to 2e-4 but reduced by half at \[300K,500K,650K,700K,750k\]. Then, we adopt DF2K dataset to fine-tune the pre-trained model. For fine-tuning, we set the initial learning rate to 1e-5 and halve it at \[125K,200K,230K,240K\] for total 250K iterations.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-A Training Settings", "weight": 1.0} -->

For real-world image super-resolution, we train HAT models based on two simulated real-world degradation models, i.e., BSRGAN and Real-ESRGAN. The total batch size is set to 32 and the input patch size is set to $64\times 64$. The network structure is the same as the basic version of HAT for classic image super-resolution. Follwing Real-ESRGAN, we first train the MSE-based model and introduce the generative adversarial training to fine-tune the GAN-based model. More training and degradation details can refer to and.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-A Training Settings", "weight": 1.0} -->

For image denoising and JPEG compression artifacts reduction, we directly use the combination of DIV2K, Flickr2K, BSD500 and WED images datasets to train the models^11^1ImageNet pre-training has limited impact on the performance of these two tasks. Similar conclusions are also mentioned., following. The network is the same as the basic version for classic image super-resolution without up-sampling. Noisy images are generated by adding additive white Gaussian noises with noise level $\sigma$ and compressed images are obtained by the MATLAB JPEG encoder with JPEG level $q$. To speed up the training, we first train models with the batch size of 32 and the patch size of $64\times 64$ for 800 iterations. We then proceed to fine-tune models with the batch size of 8 and the patch size of $128\times 128$ for 500 iterations.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-B Classic Image Super-Resolution", "weight": 1.0} -->

Quantitative results. Tab. IX shows the quantitative comparison of our approach with the state-of-the-art methods: EDSR, RCAN, SAN, IGNN, HAN, RCAN-it, GRL as well as approaches using ImageNet pre-training, i.e., IPT and EDT. We can see that our method significantly outperforms the other methods on all five benchmark datasets. Concretely, with the same depth and width, HAT surpasses SwinIR by 0.48dB$\sim$`<!-- -->`{=html}0.64dB on Urban100 and 0.34dB$\sim$`<!-- -->`{=html}0.45dB on Manga109. When compared with the approaches using pre-training, HAT^†^ also has large performance gains of more than 0.5dB against EDT on Urban100 for all three scales. Besides, HAT equipped with pre-training outperforms SwinIR by a huge margin of up to 1dB on Urban100 for $\times$`<!-- -->`{=html}2 SR.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-B Classic Image Super-Resolution", "weight": 1.0} -->

Moreover, the large model HAT-L can even bring further improvement and greatly expands the performance upper bound of this task. HAT-S with fewer parameters and similar computation can also significantly outperforms the state-of-the-art method SwinIR. (Detailed computational complexity comparison can be found in Sec. V-C.) Note that the performance gaps are much larger on Urban100, as it contains more structured and self-repeated patterns that can provide more useful pixels for reconstruction when the utilized range of information is enlarged. All these results show the effectiveness of our method.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-B Classic Image Super-Resolution", "weight": 1.0} -->

Visual comparison. We provide the visual comparison of different approaches. As shown in Fig. 10, HAT successfully recovers the clear lattice content for the images "img 002", "img 011", "img 030", "img 044" and "img 073" in the Urban100 dataset. In contrast, the other approaches cannot restore correct textures or suffer from severe blurry effects. We can also observe similar behaviors on "PrayerHaNemurenai" in the Manga109 dataset. When recovering the characters in the image, HAT obtains much clearer textures than the other methods. The visual results also demonstrate the superiority of our approach on classic image super-resolution.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-B Classic Image Super-Resolution", "weight": 1.0} -->

LAM comparison. We provide more visual results with LAM to compare the state-of-the method SwinIR and our HAT. As shown in Fig. 11, the utilized pixels for reconstruction of HAT expands to the almost full image, while that of SwinIR only gathers in a limited range. For the quantitative metric, HAT also obtains a much higher DI value than SwinIR. These results demonstrate that our method can activate more pixels to reconstruct the low-resolution input image. As a result, SR results generated by our method have higher PSNR/SSIM and better visual quality. We can observe that HAT restores much clearer textures and edges than SwinIR.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-C Real-world Image Super-Resolution", "weight": 1.0} -->

Quantitative results. Table X presents a quantitative comparison of our method with state-of-the-art approaches: ESRGAN, BSRGAN, Real-ESRGAN, DASR, and SwinIR. All models are GAN-based, and our HAT models are trained using the BSRGAN degradation model (i.e., HAT-1) and Real-ESRGAN degradation model (i.e., HAT-2). For compared methods, we utilize the officially released models and evaluate them on four datasets. Real-SR-cano and Real-Nikon feature real-world data pairs from specific cameras. AIM2019-val, from the AIM2019 challenge, is a synthetic dataset with realistic, unknown degradations^22^2We use paired data of the validation set from this challenge. The competition officials do not release the degradation model.. Additionally, we construct a synthetic dataset using 100 DIV2K valid images with a high-order degradation model, following DASR. We use PSNR and LPIPS as metrics, with PSNR measuring fidelity and LPIPS assessing perceptual quality.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-C Real-world Image Super-Resolution", "weight": 1.0} -->

Since all of the methods are GAN-based, the PSNR performance of different models on various datasets is not consistent. Nevertheless, similar PSNR values suggest comparable fidelity among the methods. Notably, HAT-1 achieves the best balance between PSNR and LPIPS among the three methods. HAT-2 obtains the best performance on all four datasets, indicating that it generates the results with the best perceptual quality.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-C Real-world Image Super-Resolution", "weight": 1.0} -->

Visual comparison. We show the visual results from different methods on real-world low-resolution images in Fig. 12. We adopt the RealSRSet+5images as the test set, which is commonly used for evaluating real-world SR models. As different degradation models from BSRGAN and Real-ESRGAN may produce varied visual properties, we present results for both models, denoted as HAT-1 and HAT-2. In the first and second rows of visual comparisons, our HAT produces much clearer branches and whiskers than other methods. In the third row, results from different degradation models exhibit significant variation. BSRGAN-based models show notable differences in color and texture. The details of BSRGAN results are relatively smooth. SwinIR generates clear textures but with obvious color deviations. In contrast, HAT achieves a relatively good balance. It handles the details well, and its larger receptive field also enhances the processing accuracy of low-frequency information. Using the degradation model from Real-ESRGAN, we can see that the result of HAT appear neater and more brick-like. Overall, our method produces visually appealing results with sharp, clear edges, demonstrating its potential for real-world applications.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VI-D1 Grayscale Image Denoising", "weight": 1.0} -->

Tab. XI shows the quantitative comparison on grayscale image denoising of our approach with the state-of-the-art method: DnCNN, IRCNN, FFDNet, NLRN, MWCNN, DRUNet, SwinIR, Restormer, GRL and SCUNet. Compared to SwinIR, HAT achieves better performance on all datasets with multiple noise levels. On Urban100, HAT achieves the largest performance gain by up to 0.64dB for $\sigma$ 50. Compared to current state-of-the-art methods Restormer and SCUNet, HAT can still outperform the former and obtains comparable performance with the latter.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-D1 Grayscale Image Denoising", "weight": 1.0} -->

We provide the visual results of different methods in Fig. 13. For "09", our HAT restores clear lines while other approaches suffers from severe blurs. For "test021" in and "img 061" in Urban100, HAT reconstructs much sharper edges than other methods. For "img 076" in Urban100, the results produced by HAT have the clearest textures. Overall, HAT obtains the best visual quality among all methods.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-D2 Color Image Denoising", "weight": 1.0} -->

Tab. XII shows the quantitative comparison results on color image denoising of our approach with the state-of-the-art methods: DnCNN, IRCNN, FFDNet, RNAN, RDN, IPT, DRUNet, SwinIR, Restormer and SCUNet. We can observe that HAT achieves the best performance on almost all four benchmark datasets. Specifically, HAT outperforms SwinIR from 0.24dB to 0.38dB and surpasses SCUNet by a large margin of 0.19dB on Urban100 with $\sigma=15$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-D2 Color Image Denoising", "weight": 1.0} -->

We present the visual results of different methods in Fig. 14. For images "img 039", "img 042" and "img 074" on Urban100, HAT reconstructs complete and clear edges, whereas other methods cannot produce complete lines or suffer from severe blurring effects. For the image "img 085", our method successfully restores the correct shape and clear texture, while other methods all fail. All these results demonstrate the superiority of the proposed HAT on image denoising.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VI-D3 Real-world Image Denoising", "weight": 1.0} -->

We also evaluate our proposed method for real-world image denoising based on the SIDD dataset. The compared methods include MPRNet, UFormer, MAXIM, HINet, Restormer, and NAFNet. The quantitative and qualitative results are shown in Tab. 16 and Fig. XIV. Our method achieves the highest PSNR/SSIM scores and clearest results, demonstrating superior performance in real-world scenarios.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-E JPEG Compression Artifacts Reduction", "weight": 1.0} -->

Tab. XIII shows the quantitative comparison results on JPEG compression artifacts reduction of our approach with the state-of-the-art methods: ARCNN, DnCNN, RNAN, DRUNet, FBCNN, SwinIR. On Classic5 and LIVE1, HAT only achieves comparable performance to SwinIR. We consider this is because the demand for the model fitting ability of this task has approached saturation, particularly for low-resolution images. We further provide the performance comparison on Urban100. Then we can see that HAT achieves considerable performance gains over SwinIR, up to 0.18dB for JPEG quality $q=40$. This can be attributed to the presence of a large number of regular textures and repeating patterns in the images of the Urban100 dataset. HAT is capable of activating more pixels for restoration. With a larger receptive field, it can restore sharper edges and textures.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-E JPEG Compression Artifacts Reduction", "weight": 1.0} -->

We also provide the visual results of different approaches in Fig. 15. For the image "buildings" in LIVE1, HAT obtains much clearer textures than other methods. For the self-repeated textures that appear in the images "img 033" and 'img 091" of Urban100, our HAT successfully restores the correct results. All the quantitative and visual results demonstrate the superiority of our method on compression artifacts reduction.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-F Image Deblurring", "weight": 1.0} -->

We conduct experiments to further validate the effectiveness of our method on image deblurring. Specifically, we evaluate several representative deblurring methods on the GoPro dataset. The compared methods include MPRNet, HINet, MAXIM, Restormer, Uformer, NAFNet, and GRL. As shown in Tab. XV, our HAT achieves the best performance among all compared approaches, with a PSNR of 33.96 dB. In addition, as illustrated in Fig. 17, HAT successfully reconstructs sharp and clear human silhouettes and portraits, recovering visually plausible details from heavily blurred inputs. These results confirm that our method not only achieves state-of-the-art performance in tasks such as SR, denoising, and compression artifact reduction, but also generalizes effectively to image deblurring. This further validates the superiority of our design.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we propose a new Hybrid Attention Transformer, HAT, for image restoration. Our model combines channel attention and self-attention to activate more pixels for high-resolution reconstruction. Besides, we propose an overlapping cross-attention module to enhance the cross-window interaction. Moreover, we introduce a same-task pre-training strategy for image super-resolution. Extensive benchmark and real-world evaluations demonstrate that HAT outperforms the state-of-the-art methods for several image restoration tasks.
