<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SwinIR: Image Restoration Using Swin Transformer

Topics include Image restoration, Image super-resolution, Vision transformers, Swin transformer, Residual Swin transformer blocks, Denoising, Compression artifact reduction, Lightweight super-resolution, SwinIR.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

SwinIR is a strong transformer baseline for low-level restoration, adapting Swin Transformer blocks to super-resolution, denoising, and JPEG artifact reduction. Its importance is partly architectural and partly practical: it helped make shifted-window transformers a standard choice for restoration tasks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Image restoration is a long-standing low-level vision problem that aims to restore high-quality images from low-quality images (e.g., downscaled, noisy and compressed images). While state-of-the-art image restoration methods are based on convolutional neural networks, few attempts have been made with Transformers which show impressive performance on high-level vision tasks. In this paper, we propose a strong baseline model SwinIR for image restoration based on the Swin Transformer. SwinIR consists of three parts: shallow feature extraction, deep feature extraction and high-quality image reconstruction. In particular, the deep feature extraction module is composed of several residual Swin Transformer blocks (RSTB), each of which has several Swin Transformer layers together with a residual connection. We conduct experiments on three representative tasks: image super-resolution (including classical, lightweight and real-world image super-resolution), image denoising (including grayscale and color image denoising) and JPEG compression artifact reduction.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experimental results demonstrate that SwinIR outperforms state-of-the-art methods on different tasks by textbf{up to 0.14\sim0.45dB}, while the total number of parameters can be reduced by textbfup to 67%.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Image restoration, such as image super-resolution (SR), image denoising and JPEG compression artifact reduction, aims to reconstruct the high-quality clean image from its low-quality degraded counterpart. Since several revolutionary work, convolutional neural networks (CNN) have become the primary workhorse for image restoration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most CNN-based methods focus on elaborate architecture designs such as residual learning and dense connections. Although the performance is significantly improved compared with traditional model-based methods, they generally suffer from two basic problems that stem from the basic convolution layer. First, the interactions between images and convolution kernels are content-independent. Using the same convolution kernel to restore different image regions may not be the best choice. Second, under the principle of local processing, convolution is not effective for long-range dependency modelling.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an alternative to CNN, Transformer designs a self-attention mechanism to capture global interactions between contexts and has shown promising performance in several vision problems. However, vision Transformers for image restoration usually divide the input image into patches with fixed size (*e.g*., 48$\times$`<!-- -->`{=html}48) and process each patch independently. Such a strategy inevitably gives rise to two drawbacks. First, border pixels cannot utilize neighbouring pixels that are out of the patch for image restoration. Second, the restored image may introduce border artifacts around each patch. While this problem can be alleviated by patch overlapping, it would introduce extra computational burden.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Swin Transformer has shown great promise as it integrates the advantages of both CNN and Transformer. On the one hand, it has the advantage of CNN to process image with large size due to the local attention mechanism. On the other hand, it has the advantage of Transformer to model long-range dependency with the shifted window scheme.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose an image restoration model, namely SwinIR, based on Swin Transformer. More specifically, SwinIR consists of three modules: shallow feature extraction, deep feature extraction and high-quality image reconstruction modules. Shallow feature extraction module uses a convolution layer to extract shallow feature, which is directly transmitted to the reconstruction module so as to preserve low-frequency information. Deep feature extraction module is mainly composed of residual Swin Transformer blocks (RSTB), each of which utilizes several Swin Transformer layers for local attention and cross-window interaction. In addition, we add a convolution layer at the end of the block for feature enhancement and use a residual connection to provide a shortcut for feature aggregation. Finally, both shallow and deep features are fused in the reconstruction module for high-quality image reconstruction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Compared with prevalent CNN-based image restoration models, Transformer-based SwinIR has several benefits: content-based interactions between image content and attention weights, which can be interpreted as spatially varying convolution. long-range dependency modelling are enabled by the shifted window mechanism. better performance with less parameters. For example, as shown in Fig. 1, SwinIR achieves better PSNR with less parameters compared with existing image SR methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Image Restoration", "weight": 1.0} -->

Compared to traditional image restoration methods which are generally model-based, learning-based methods, especially CNN-based methods, have become more popular due to their impressive performance. They often learn mappings between low-quality and high-quality images from large-scale paired datasets. Since pioneering work SRCNN (for image SR), DnCNN (for image denoising) and ARCNN (for JPEG compression artifact reduction), a flurry of CNN-based models have been proposed to improve model representation ability by using more elaborate neural network architecture designs, such as residual block, dense block and others. Some of them have exploited the attention mechanism inside the CNN framework, such as channel attention, non-local attention and adaptive patch aggregation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Vision Transformer", "weight": 1.0} -->

Recently, natural language processing model Transformer has gained much popularity in the computer vision community. When used in vision problems such as image classification, object detection, segmentation and crowd counting, it learns to attend to important image regions by exploring the global interactions between different regions. Due to its impressive performance, Transformer has also been introduced for image restoration. Chen *et al*. proposed a backbone model IPT for various restoration problems based on the standard Transformer. However, IPT relies on large number of parameters (over 115.5M parameters), large-scale datasets (over 1.1M images) and multi-task learning for good performance. Cao *et al*. proposed VSR-Transformer that uses the self-attention mechanism for better feature fusion in video SR, but image features are still extracted from CNN. Besides, both IPT and VSR-Transformer are patch-wise attention, which may be improper for image restoration. In addition, a concurrent work proposed a U-shaped architecture based on the Swin Transformer.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Network Architecture", "weight": 1.0} -->

As shown in Fig. 2, SwinIR consists of three modules: shallow feature extraction, deep feature extraction and high-quality (HQ) image reconstruction modules. We employ the same feature extraction modules for all restoration tasks, but use different reconstruction modules for different tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Shallow and deep feature extraction", "weight": 1.0} -->

Given a low-quality (LQ) input $I_{\text{LQ}} \in {\mathbb{R}}^{H \times W \times C_{in}}$ ($H$, $W$ and $C_{in}$ are the image height, width and input channel number, respectively), we use a $3 \times 3$ convolutional layer $H_{\text{SF}}{(\cdot)}$ to extract shallow feature $F_{0} \in {\mathbb{R}}^{H \times W \times C}$ as where $C$ is the feature channel number. The convolution layer is good at early visual processing, leading to more stable optimization and better results. It also provides a simple way to map the input image space to a higher dimensional feature space.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Shallow and deep feature extraction", "weight": 1.0} -->

Then, we extract deep feature $F_{\text{DF}} \in {\mathbb{R}}^{H \times W \times C}$ from $F_{0}$ as where $H_{\text{DF}}{(\cdot)}$ is the deep feature extraction module and it contains $K$ residual Swin Transformer blocks (RSTB) and a $3 \times 3$ convolutional layer. More specifically, intermediate features $F_{1},F_{2},\ldots,F_{K}$ and the output deep feature $F_{\text{DF}}$ are extracted block by block as where $H_{\text{RSTB}_{i}}{(\cdot)}$ denotes the $i$-th RSTB and $H_{\text{CONV}}$ is the last convolutional layer.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Shallow and deep feature extraction", "weight": 1.0} -->

Using a convolutional layer at the end of feature extraction can bring the inductive bias of the convolution operation into the Transformer-based network, and lay a better foundation for the later aggregation of shallow and deep features.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Image reconstruction", "weight": 1.0} -->

Taking image SR as an example, we reconstruct the high-quality image $I_{\text{RHQ}}$ by aggregating shallow and deep features as where $H_{\text{REC}}{(\cdot)}$ is the function of the reconstruction module. Shallow feature mainly contain low-frequencies, while deep feature focus on recovering lost high-frequencies. With a long skip connection, SwinIR can transmit the low-frequency information directly to the reconstruction module, which can help deep feature extraction module focus on high-frequency information and stabilize training. For the implementation of reconstruction module, we use the sub-pixel convolution layer to upsample the feature.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Image reconstruction", "weight": 1.0} -->

For tasks that do not need upsampling, such as image denoising and JPEG compression artifact reduction, a single convolution layer is used for reconstruction. Besides, we use residual learning to reconstruct the residual between the LQ and the HQ image instead of the HQ image. This is formulated as where $H_{\text{SwinIR}}{(\cdot)}$ denotes the function of SwinIR.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Loss function", "weight": 1.0} -->

For image SR, we optimize the parameters of SwinIR by minimizing the $L_{1}$ pixel loss where $I_{\text{RHQ}}$ is obtained by taking $I_{\text{LQ}}$ as the input of SwinIR, and $I_{\text{HQ}}$ is the corresponding ground-truth HQ image. For classical and lightweight image SR, we only use the naive $L_{1}$ pixel loss as same as previous work to show the effectiveness of the proposed network. For real-world image SR, we use a combination of pixel loss, GAN loss and perceptual loss to improve visual quality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Loss function", "weight": 1.0} -->

For image denoising and JPEG compression artifact reduction, we use the Charbonnier loss where $\epsilon$ is a constant that is empirically set to $10^{- 3}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Residual Swin Transformer Block", "weight": 1.0} -->

As shown in Fig. 2(a), the residual Swin Transformer block (RSTB) is a residual block with Swin Transformer layers (STL) and convolutional layers. Given the input feature $F_{i,0}$ of the $i$-th RSTB, we first extract intermediate features $F_{i,1},F_{i,2},\ldots,F_{i,L}$ by $L$ Swin Transformer layers as where $H_{\text{STL}_{i,j}}{(\cdot)}$ is the $j$-th Swin Transformer layer in the $i$-th RSTB. Then, we add a convolutional layer before the residual connection. The output of RSTB is formulated as where $H_{\text{CONV}_{i}}{(\cdot)}$ is the convolutional layer in the $i$-th RSTB. This design has two benefits.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Residual Swin Transformer Block", "weight": 1.0} -->

First, although Transformer can be viewed as a specific instantiation of spatially varying convolution, covolutional layers with spatially invariant filters can enhance the translational equivariance of SwinIR. Second, the residual connection provides a identity-based connection from different blocks to the reconstruction module, allowing the aggregation of different levels of features.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Swin Transformer layer", "weight": 1.0} -->

Swin Transformer layer (STL) is based on the standard multi-head self-attention of the original Transformer layer. The main differences lie in local attention and the shifted window mechanism. As shown in Fig. 2(b), given an input of size $H \times W \times C$, Swin Transformer first reshapes the input to a $\frac{HW}{M^{2}} \times M^{2} \times C$ feature by partitioning the input into non-overlapping $M \times M$ local windows, where $\frac{HW}{M^{2}}$ is the total number of windows. Then, it computes the standard self-attention separately for each window (*i.e*., local attention).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Swin Transformer layer", "weight": 1.0} -->

For a local window feature $X \in {\mathbb{R}}^{M^{2} \times C}$, the query, key and value matrices $Q$, $K$ and $V$ are computed as where $P_{Q}$, $P_{K}$ and $P_{V}$ are projection matrices that are shared across different windows. Generally, we have ${Q,K,V} \in {\mathbb{R}}^{M^{2} \times d}$. The attention matrix is thus computed by the self-attention mechanism in a local window as where $B$ is the learnable relative positional encoding. In practice, following, we perform the attention function for $h$ times in parallel and concatenate the results for multi-head self-attention (MSA).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Swin Transformer layer", "weight": 1.0} -->

Next, a multi-layer perceptron (MLP) that has two fully-connected layers with GELU non-linearity between them is used for further feature transformations. The LayerNorm (LN) layer is added before both MSA and MLP, and the residual connection is employed for both modules. The whole process is formulated as However, when the partition is fixed for different layers, there is no connection across local windows. Therefore, regular and shifted window partitioning are used alternately to enable cross-window connections, where shifted window partitioning means shifting the feature by $({\lfloor\frac{M}{2}\rfloor},{\lfloor\frac{M}{2}\rfloor})$ pixels before partitioning.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For classical image SR, real-world image SR, image denoising and JPEG compression artifact reduction, the RSTB number, STL number, window size, channel number and attention head number are generally set to 6, 6, 8, 180 and 6, respectively. One exception is that the window size is set to 7 for JPEG compression artifact reduction, as we observe significant performance drop when using 8, possibly because JPEG encoding uses $8 \times 8$ image partions. For lightweight image SR, we decrease RSTB number and channel number to 4 and 60, respectively. Following, when self-ensemble strategy is used in testing, we mark the model with a symbol "+", *e.g*., SwinIR+. Due to page limit, training and evaluation details are provided in the supplementary.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Ablation Study and Discussion", "weight": 1.0} -->

For ablation study, we train SwinIR on DIV2K for classical image SR ($\times 2$) and test it on Manga109.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Impact of channel number, RSTB number and STL number", "weight": 1.0} -->

We show the effects of channel number, RSTB number and STL number in a RSTB on model performance in Figs. 3(a), 3(b) and 3(c), respectively. It is observed that the PSNR is positively correlated with these three hyper-parameters. For channel number, although the performance keeps increasing, the total number of parameters grows quadratically. To balance the performance and model size, we choose 180 as the channel number in rest experiments. As for RSTB number and layer number, the performance gain becomes saturated gradually. We choose 6 for both of them to obtain a relatively small model.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Impact of patch size and training image number; model convergence comparison", "weight": 1.0} -->

We compare the proposed SwinIR with a representative CNN-based model RCAN to compare the difference of Transformer-based and CNN-based models. From Fig. 3(d), one can see that SwinIR performs better than RCAN on different patch sizes, and the PSNR gain becomes larger when the patch size is larger. Fig. 3(e) shows the impact of the number of training images. Extra images from Flickr2K are used in training when the percentage is larger than 100% (800 images). There are two observations. First, as expected, the performance of SwinIR rises with the training image number. Second, different from the observation in IPT that Transformer-based models are heavily relied on large amount of training data, SwinIR achieves better results than CNN-based models using the same training data, even when the dataset is small (*i.e*., 25%, 200 images). We also plot the PSNR during training for both SwinIR and RCAN in Fig. 3(f).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Impact of patch size and training image number; model convergence comparison", "weight": 1.0} -->

It is clear that SwinIR converges faster and better than RCAN, which is contradictory to previous observations that Transformer-based models often suffer from slow model convergence.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Impact of residual connection and convolution layer in RSTB", "weight": 1.0} -->

Table 1 shows four residual connection variants in RSTB: no residual connection, using $1 \times 1$ convolution layer, using $3 \times 3$ convolution layer and using three $3 \times 3$ convolution layers (channel number of the intermediate layer is set to one fourth of network channel number). From the table, we can have following observations. First, the residual connection in RSTB is important as it improves the PSNR by 0.16dB. Second, using $1 \times 1$ convolution brings little improvement maybe because it cannot extract local neighbouring information as $3 \times 3$ convolution does. Third, although using three $3 \times 3$ convolution layers can reduce the number of parameters, the performance drops slightly.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results on Image SR", "weight": 1.0} -->

Urban100 (4×):img_012 HR VDSR EDSR RDN OISR SAN RNAN IGNN IPT SwinIR (ours) Figure 4: Visual comparison of bicubic image SR (×4) methods. Compared images are derived. Best viewed by zooming.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results on Image SR", "weight": 1.0} -->

#Params

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results on Image SR", "weight": 1.0} -->

#Mult-Adds

<!-- chunk {"id": "body-0035", "role": "body", "section": "Classical image SR", "weight": 1.0} -->

Table 2 shows the quantitative comparisons between SwinIR (middle size) and state-of-the-art methods: DBPN, RCAN, RRDB, SAN, IGNN, HAN, NLSA and IPT. As one can see, when trained on DIV2K, SwinIR achieves best performance on almost all five benchmark datasets for all scale factors. The maximum PSNR gain reaches 0.26dB on Manga109 for scale factor 4. Note that RCAN and HAN introduce channel and spatial attention, IGNN proposes adaptive patch feature aggregation, and NLSA is based on the non-local attention mechanism. However, all these CNN-based attention mechanisms perform worse than the proposed Transformer-based SwinIR, which indicates the effectiveness of the proposed model. When we train SwinIR on a larger dataset (DIV2K+Flickr2K), the performance further increases by a large margin (up to 0.47dB), achieving better accuracy than the same Transformer-based model IPT, even though IPT utilizes ImageNet (more than 1.3M images) in training and has huge number of parameters (115.5M).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Classical image SR", "weight": 1.0} -->

In contrast, SwinIR has a small number of parameters (11.8M) even compared with state-of-the-art CNN-based models (15.4$\sim$`<!-- -->`{=html}44.3M). As for runtime, representative CNN-based model RCAN, IPT and SwinIR take about 0.2, 4.5s and 1.1s to test on a $1,{024 \times 1},024$ image, respectively. Visual comparisons are show in Fig. 4. SwinIR can restore high-frequency details and alleviate the blurring artifacts, resulting in sharp and natural edges. In contrast, most CNN-based methods produces blurry images or even incorrect textures. IPT generates better images compared with CNN-based methods, but it suffers from image distortions and border artifact.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Lightweight image SR", "weight": 1.0} -->

We also provide comparison of SwinIR (small size) with state-of-the-art lightweight image SR methods: CARN, FALSR-A, IMDN, LAPAR-A and LatticeNet. In addition to PSNR and SSIM, we also report the total numbers of parameters and multiply-accumulate operations (evaluated on a $1280 \times 720$ HQ image) to compare the model size and computational complexity of different models. As shown in Table 3, SwinIR outperforms competitive methods by a PSNR margin of up to 0.53dB on different benchmark datasets, with similar total numbers of parameters and multiply-accumulate operations. This indicates that the SwinIR architecture is highly efficient for image restoration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Real-world image SR", "weight": 1.0} -->

The ultimate goal of image SR is for real-world applications. Recently, Zhang *et al*. proposed a practical degradation model BSRGAN for real-world image SR and achieved surprising results in real scenarios^11^1 To test the performance of SwinIR for real-world SR, we re-train SwinIR by using the same degradation model as BSRGAN for low-quality image synthesis. Since there is no ground-truth high-quality images, we only provide visual comparison with representative bicubic model ESRGAN and state-of-the-art real-world image SR models RealSR, BSRGAN and Real-ESRGAN. As shown in Fig. 5, SwinIR produces visually pleasing images with clear and sharp edges, whereas other compared methods may suffer from unsatisfactory artifacts. In addition, to exploit the full potential of SwinIR for real applications, we further propose a large model and train it on much larger datasets. Experiments show that it can deal with more complex corruptions and achieves even better performance on real-world images than the current model. Due to page limit, the details are given in our project page

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results on JPEG Compression Artifact Reduction", "weight": 1.0} -->

Table 4 shows the comparison of SwinIR with state-of-the-art JPEG compression artifact reduction methods: ARCNN, DnCNN-3, QGAC, RNAN, RDN and DRUNet. All of compared methods are CNN-based models. Following, we test different methods on two benchmark datasets (Classic5 and LIVE1 ) for JPEG quality factors 10, 20, 30 and 40. As we can see, the proposed SwinIR has average PSNR gains of at least 0.11dB and 0.07dB on two testing datasets for different quality factors. Besides, compared with the previous best model DRUNet, SwinIR only has 11.5M parameters, while DRUNet is a large model that has 32.7M parameters.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results on Image Denoising", "weight": 1.0} -->

We show grayscale and color image denoising results in Table 5 and Table 6, respectively. Compared methods include traditional models BM3D and WNNM, CNN-based models DnCNN, IRCNN, FFDNet, N3Net, NLRN, FOCNet, RNAN, MWCNN and DRUNet. Following, the compared noise levels include 15, 25 and 50. As one can see, our model achieves better performance than all compared methods. In particular, it surpasses the state-of-the-art model DRUNet by up to 0.3dB on the large Urban100 dataset that has 100 high-resolution testing images. It is worth pointing out that SwinIR only has 12.0M parameters, whereas DRUNet has 32.7M parameters. This indicates that the SwinIR architecture is highly efficient in learning feature representations for restoration. The visual comparison for grayscale and color image denoising of different methods are shown in Figs. 6 and 7. As we can see, our method can remove heavy noise corruption and preserve high-frequency image details, resulting in sharper edges and more natural textures.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results on Image Denoising", "weight": 1.0} -->

By contrast, other methods suffer from either over-smoothness or over-sharpness, and cannot recover rich textures.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose a Swin Transformer-based image restoration model SwinIR. The model is composed of three parts: shallow feature extraction, deep feature extraction and HR reconstruction modules. In particular, we use a stack of residual Swin Transformer blocks (RSTB) for deep feature extraction, and each RSTB is composed of Swin Transformer layers, convolution layer and a residual connection. Extensive experiments show that SwinIR achieves state-of-the-art performance on three representative image restoration tasks and six different settings: classic image SR, lightweight image SR, real-world image SR, grayscale image denoising, color image denoising and JPEG compression artifact reduction, which demonstrates the effectiveness and generalizability of the proposed SwinIR. In the future, we will extend the model to other restoration tasks such as image deblurring and deraining.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgements This paper was partially supported by the ETH Zurich Fund (OK), a Huawei Technologies Oy (Finland) project, the China Scholarship Council and an Amazon AWS grant. Special thanks goes to Yijue Chen.
