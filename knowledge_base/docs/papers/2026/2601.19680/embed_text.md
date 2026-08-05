<!-- arxiv-full-text:v1 {"arxiv_id": "2601.19680", "source": "arxiv-html"} -->

## Introduction

In image processing and analysis, the use of a similarity metric is essential when the goal is to quantify the similarity or dissimilarity between two images. This is useful in many tasks, such as evaluating a lossy compression algorithm or evaluating image generative models, where the goal is to evaluate the quality of an artificially generated image against the target image by providing a score.

The present study examines Image Quality Assessment (IQA) metrics from a perceptual perspective, understood as the ability of the metrics to assess image similarity based on the characteristics and cognitive mechanisms of the Human Visual System (HVS).

In the current state-of-the-art (SOTA), the most widely used similarity metrics are the Peak Signal-to-Noise Ratio (PSNR) and the Structural Similarity Index Measure (SSIM). However, as shown in Figure 1, they are not perceptual in nature. This is due to the fact that they do not align with human perception when it comes to assessing the similarity between two sets of images.

Figure 1: Comparison of human perceptual similarity and nonperceptual metrics. On a sample of the 2AFC dataset, the similarity metrics PSNR and SSIM assigned the highest similarity score between the reference image and the distorted one on the right, suggesting that, for both metrics, the reference image is more similar to the distorted image on the right than the distorted image on the left. However, a panel of five human judges unanimously agreed that based on their visual perception, the reference image is more similar to the left distorted image.

This has also been documented in several works, such as the work of Ebrahimi et al., which shows that PSNR is not a good perceptual metric. In the work of Wang et al., the authors show that PSNR is a poor indicator of subjective quality in the evaluation of JPEG compressed images. As an alternative, the authors propose a No-Reference quality measurement algorithm. The work of Wang et al., is the most comprehensive work in highlighting the difficulties of Mean Squared Error (MSE) as a measure of signal fidelity. The authors demonstrated the limitations of MSE by comparing an image with its distorted versions, measuring the distance between each pair of images, and showing that this metric does not accurately reflect signal fidelity. Since PSNR uses MSE in its equation, PSNR inherits these same problems.

Since PSNR has been shown not to be a perceptual metric, the SSIM metric was subsequently proposed; there are works in the literature showing that there are correlations between these two metrics, and furthermore, demonstrating that SSIM can also produce unexpected scores. Horé and Ziou showed that there is a direct mathematical relationship between PSNR and SSIM, demonstrating that PSNR can be derived as a function of SSIM. In addition to proving the mathematical connection, the authors performed empirical experiments to further demonstrate the similarity between PSNR and SSIM.

In recent years, SSIM has become the most widely used metric in a wide range of contexts. However, in the work of Nilsson and Akenine-Möller, the authors analyze the mathematical factors of SSIM and demonstrate that SSIM can produce unexpected, often undefined and non-intuitive results leading the user to erroneous conclusions; they affirm that this metric is being used for more than what it was created .

We have observed that despite the innovative high-level IQA metrics being closer to HVS, both PSNR and SSIM are now used as de facto standards, although the various works mentioned above have shown how in different contexts they are not the most appropriate metrics.

On the other hand, high-level deep learning-based metrics, such as Learned Perceptual Image Patch Similarity (LPIPS), have shown high correlations with human judgment; however, their inherent black-box nature significantly limits their transparency and interpretability, obscuring the specific visual components that determine similarity or difference.

In response to this limitation, this work proposes the Earth mover's Distance and Oklab Similarity (EDOKS) metric, which is based on the integration of low-level handcrafted features. This analytical approach is specifically designed to transparently and distinctly quantify the impact of both geometric (shape) and chromatic (color) distortions. Given the analytical and white-box nature of EDOKS, and considering that deep learning-based metrics achieve extremely high accuracy at the expense of transparency, our goal in this paper is to demonstrate that, compared to other low-level IQA metrics, EDOKS is more consistent with human perceptual evaluation.

We propose two terms of perceptual dissimilarity for evaluating differences between two images, one related to textures and the other to colors. Furthermore, we utilize these terms to attempt to define a unique index of perceptual similarity. The first term related to the texture is calculated using the Earth Mover's Distance (EMD), while the second term calculates the distances between colors in the Oklab color space. Finally, we propose the combination of these two terms creating the EDOKS index.

The vast majority of low-level SOTA metrics have been evaluated and optimized on datasets containing chromatic, noise, and a few compression distortions. We, instead, use the Berkeley-Adobe Perceptual Patch Similarity (BAPPS) Dataset because it contains more distortions, not only the classic ones, but also those generated by deep models, as well as distortions in shapes, textures, and other aspects.

Performing several experiments, we demonstrate that EDOKS behaves consistently with the perceptual similarity of color and textures between images, a behavior not always guaranteed by SOTA similarity metrics.

Furthermore, given the lack of transparency in all SOTA IQA metrics, especially deep ones based on black-box architectures, we show that our metric is, instead, easily explainable. It provides maps of interest that highlight areas with significant differences between two images, ensuring transparency in its use.

## Related Works

Metrics for evaluating the quality of an image can be classified into three different categories: Full-Rreference (FR) methods evaluate the quality of an image by comparing it with the corresponding original target, so this class of metrics can only be used if the original signal is available.

Reduced-Reference (RR) methods are used when one does not have direct access to the original target images, but has a reduced and limited feature set.

No-Reference (NR) methods are used when the target image is not available; these are usually approximate methods and less accurate than the other classes of methods.

In this paper, we propose a metric that belongs to the class of FR methods; in the current SOTA, the most widely used FR similarity metrics are the PSNR and the SSIM.

The PSNR was originally created to evaluate the quality of images in compression of lossy type, thus with loss of information. PSNR calculates the ratio of the maximum pixel value to the MSE between two images, and expresses the result as a logarithmic quantity on the decibel (dB) scale. PSNR is based on local differences between pixels and is unable to evaluate regional information such as texture or shape.

The SSIM is proposed by Wang et al. as an alternative perceptual metric to PSNR, and is defined as a perceptual metric. In addition to evaluating luminance and contrast between two images, it also compares the structural information of the objects in the images because pixels have strong spatial dependencies.

In the basic version, SSIM is applied to only one channel, typically luminance. However, it can also be applied to RGB images or other color spaces. In this case, SSIM is calculated independently on each channel and then combined into a single score using a weighted sum. This method does not consider the more robust chromatic information.

Since the metrics just mentioned have been the standard for image quality assessment for years, several papers have proposed enhancements of PSNR and SSIM to try to achieve more accurate similarity assessments. For the PSNR, the PSNR Human Visual System Masking model (PSNR-HVS-M) was proposed, which consists of the calculation of the MSE between block Discrete Cosine Transform (DCT) coefficients; even in this version of PSNR, structural information such as shapes or textures is not considered. Instead of SSIM, Multi-Scale SSIM (MS-SSIM) was introduced as an enhancement, since SSIM strongly depends on the scale at which it is applied. It is proposed that SSIM be evaluated at different scales. The use of different scales allows image details to be evaluated at different resolutions. Another enhancement is Information Content Weighting SSIM (IW-SSIM), where the authors combine information content weighting with MS-SSIM. But even in these two latter cases, the metric is based on the evaluation of luminance between two images.

Other FR methods have been proposed in the literature. Firstly, we can recall here the feature similarity index (FSIM), that employs two features, the phase congruency and the gradient magnitude, to compute the local similarity map.

The authors claimed that the phase congruency and the gradient magnitude play complementary roles in characterizing the local image quality. At the quality score pooling stage of FSIM, phase congruency map is utilized again as a weighting function since it can roughly reflect how perceptually important a local patch is to the HVS, but it is not a metric designed to be robust to distortions in shapes or textures. Spectral Residual-based similarity (SR-SIM) is a metric that stands as a computationally faster alternative to IW-SSIM and FSIM. It consists of using spectral residual visual saliency both to extract feature maps on local image qualities and as a weight of the final score, but ignores color features and geometric shapes.

Visual Information Fidelity (VIF) metric models the image as a source of information passed through two channels, one representing the distortions introduced by the acquisition or compression system, and one modeling the HVS. VIF then calculates the mutual information between the original and distorted images in a wavelet domain. It does not distinguish well where the distortion occurs because it operates globally in the wavelet domain, and it was tested on simple datasets and fixed models, ignoring realistic distortion scenarios or new types of artifacts.

Gradient Magnitude Similarity Deviation (GMSD) is a metric that makes use of gradient-based similarity using only the luminance component, that is, it uses image gradients and a new pooling strategy to analyze similarity between images. Therefore, it is unable to effectively capture multiscale perceptual gradients or chromatic distortions. Multiscale and extended color versions of GMSD (MS-GMSD) were subsequently proposed precisely to overcome these limitations. However, both metrics are based exclusively on gradient maps and do not feature any explicit modeling of shape or structural coherence, thus remaining insensitive to geometric or spatial misalignments.

Visual Saliency-based Index (VSI) is a metric that uses saliency maps not only as a weight function for score pooling, but also as feature maps to characterize local image quality. VSI assumes that the chosen saliency map is suitable and stable for all types of distortions. However, the perception of saliency may change in the presence of certain artifacts or in complex visual contexts. This means that metrics such as VSI which assume standard conditions may have gaps in the following cases: extreme ambient light conditions, poorly calibrated displays, viewing in highly reflective environments, etc..

In the similarity of DCT subbands (DSS), the important features of human perception are measured by the variation of structural information in the subbands of the DCT domain. DSS' authors place greater weight on low subbands, so if the distortion is localized in a high band or manifests itself more as a localized artifact, the metric may "lose" sensitivity. Furthermore, DSS calculates contributions per subband and does not strongly incorporate spatial localization or the visual importance of regions.

Mean Deviation Similarity Index (MDSI) is a metric that consists of three terms: gradient similarity, chromaticity similarity and deviation pooling. MDSI uses local gradients on a single spatial scale and may fail to detect geometric distortions that alter the overall structure. Therefore, although it is effective for blurring, noise, and local contrast degradation, its sensitivity to global structural changes is limited.

In, the authors proposed Haar wavelet-based Perceptual Similarity Index (HaarPSI) a metric that uses the coefficients resulting from the Haar wavelet decomposition to evaluate the similarity between two images. This is a good similarity metric, similar to our approach in that it uses filters to extract information from the image. However, one limitation is its sensitivity to preprocessing, which causes the metric to behave unreliably.

For all the metrics in which coefficient optimization is required, the authors execute this process on datasets that do not adequately represent geometric distortions and artifacts generated by deep neural networks. Consequently, these methods are ineffective for contemporary applications, such as evaluating the output of deep models.

Furthermore, they were not developed with the intention of being transparent and explainable. They do not show which visual elements had the greatest impact on the computation of the similarity score between two images.

In generative AI models, where the generated artificial image must be compared with the target image, other FR similarity metrics have also been proposed. However, these metrics utilize black-box models to extract image features and evaluate the similarity between images. This makes it difficult to trace the elements and their positions in the image that led to the discrimination of the similarity score.

The primary similarity metric that leverages a deep architecture is the LPIPS, that measures the distance between two images in the feature space of deep neural networks pre-trained on visual recognition tasks. The activations of features from multiple layers of the network are compared and combined in a linear fashion using weights that have been learned. The purpose of this process is to approximate human perceptual judgments.

Unlike LPIPS, Perceptual image-error Assessment through Pairwise Preference (PieAPP) is trained on paired human judgments: the model learns to predict which of the two distorted images is perceptually closer to the target image. In this way, the neural network estimates a "perceptual error" consistent with human visual perception.

Another deep FR perceptual metric is Deep Image Structure and Texture Similarity (DISTS), which combines structure and texture using deep network features. Compared to LPIPS, it explicitly separates contributions from structures and textures, improving consistency with human perception and stability across different distortions.

Finally, TOPIQ uses a Transformer-based top-down approach that starts with semantic understanding of the image and ends with the evaluation of local distortions.

An alternative approach to the similarity metrics already mentioned is to use a human jury to evaluate the generated images, in which a similarity score must be assigned between two images without knowing which image is generated; this approach is known as Mean Opinion Score (MOS) metrics.

Figure 2: The following example illustrates the process of creating a signature from an image. The image is converted to grayscale and split into patches. Subsequently, Gabor’s filter dictionary is applied to each patch. The energy magnitudes are calculated for each Gabor response, resulting in a 4x6 matrix for each patch. To reduce the number of patches, the MengHee-Heng clustering algorithm is applied to the matrices, yielding k 24-dimensional centroids V and the corresponding frequencies W. V and W are then output to the S dictionary.

## Perceptual Terms

. From the works in the literature, discussed in the previous section, the lack of terms that can express a perceptual and transparent comparison between the textures and colors of two images stands out. Our goal is to have a perceptual similarity metric that is capable of justifying its score while ensuring transparency. In this section, we analyze the term based on the EMD to compare the dissimilarity between textures in two images; the term exploiting the Oklab color space to compare the perceptual dissimilarity between colors in two images; and EDOKS index as a combination of the two terms.

### III-A Texture Dissimilarity Term

To compare the textures of two images, we relied on the work of Rubner et al., where the authors propose an image retrieval method based on the use of EMD, that is a distance between two distributions used by Hitchcock to solve the Monge-Kantorovich transport problem. Histograms are typically used to represent the distribution of an image. In, it is shown that histograms are fixed-size structures and therefore do not have balance between expressiveness and efficiency. In fact, the authors propose the use of variable-size image signatures, obtained by clustering the responses achieved using a Gabor filter dictionary applied to image patches.

In our work, we exploited some steps of that allowed us to obtain consistent results for texture comparisons. In the Algorithm 1, we show pseudocode of how we obtain signatures $S$ by applying Gabor's filter dictionary to an image. Given an input colored image of size $M\times N\times 3$, we convert it to grayscale $I$ with size $M\times N$, because to evaluate shape dissimilarity it is sufficient to use only the intensity of pixels; moreover, we provide a dedicated term for color evaluation later. We divide the image into $l$ non-overlapping patches of size $p\times p$ where $p<<min(M,N)$, and apply Gabor's filter dictionary to each patch.

1: function signature(Image I) 4: P← patches(I) ⊳ non-overlapped patches list 6: E ← empty_matrices(l, 4, 6) ⊳ energies list 11: Freal, Fimag ← gabor(Pz, si, oj) 12: $|F|\leftarrow\sqrt{F_{real}^{2}+F_{imag}^{2}}$ 17: S ← (V, W) ⊳ tuple of values and weights 18: return S ⊳ return signature of image I Algorithm 1 Texture signature extraction A single Gabor filter allows us to extract the texture features of a patch with respect to a precise scale and orientation. As a result, a dictionary of Gabor filters allows the extraction of texture features at different scales and orientations to try to extract the main patterns of the patch. In our setup, we define a dictionary of Gabor filters with the following four scales $s=\{0.1,0.2,0.3,0.4\}$ and the following six orientations $o=\{0^{\circ},30^{\circ},60^{\circ},90^{\circ},120^{\circ},150^{\circ}\}$, which then allows us to obtain a collection of twenty-four total filters for each patch. Each Gabor filter, with a scale $s_{i}$ and orientation $o_{j}$, applied to the $z$-th patch produces two responses $F_{real}$ and $F_{imag}$, which are produced by the real and imaginary components of the Gabor kernel convolved with the $z$-th patch, respectively. From the real and imaginary components we calculate the magnitude $|F|$ with the same size of the $z$-th patch $p\times p$. Afterwards, we calculate the energy of the magnitude $|F|$ as, corresponding to scale $i$ and orientation $j$, to be assigned to $E_{z,i,j}\in\mathbb{R}$. We get a list of $l$ four-by-six matrices $E$, normalized so that $\sum_{i,j}E_{z,i,j}=1$ for each $z$-th patch. Each element $E_{z,i,j}$ corresponds to a precise texture response of patch $P_{z}$ at a scale $s_{i}$ and orientation $o_{j}$.

Figure 2 illustrates an example of signature creation, where in the list of four-by-six matrices $E$, a dark pixel signifies a robust response to a specific scale and orientation. To use EMD, the distributions must be weighted, so as a final step in creating the signatures we apply a Meng-Hee Heng clustering algorithm, which takes as input the $l$ energies and returns as output two lists of $k$ centroids $V=\{v_{1},...,v_{k}\}\;|\;v_{i}\in\mathbb{R}^{24}$ and $k$ weights $W=\{w_{1},...,w_{k}\}\;|\;w_{i}\in\mathbb{R}$, where $k\leq l$. Each centroid $v_{i}$ represents a texture patch that appears frequently in the image $I$, $v_{i}$ is a four-by-six matrix or can be viewed as a single 24-dimensional vector. Each weight $w_{i}$ represents the frequency percentage of $v_{i}$ that appears in image $I$. Unlike, where they use K-means as the clustering algorithm, we preferred the Meng-Hee Heng variant, which automatically finds the suitable number of $k$ clusters. At the end, both the list of 24-dimensional centroids $V$ and the list of corresponding weights $W$ make up the $S$ signature of a single image $I$.

Let $S_{X}=(\{v_{x_{1}},...,v_{x_{n}}\},\{w_{x_{i}},...,w_{x_{n}}\})$ be the signature obtained from image $X$ with $n$ clusters, and $S_{Y}=(\{v_{y_{1}},...,v_{y_{m}}\},\{w_{y_{i}},...,w_{y_{m}}\})$ the signature obtained from image $Y$ with $m$ clusters, the next step is to calculate the EMD between the two signatures. Commonly in EMD, the two distributions can be seen as two land masses, where the first distribution is uniformly distributed in space and the second distribution is a set of holes in this same space. The goal of EMD is to measure the minimum amount of work to fill the holes in the second distribution using the ground of the first distribution.

Formally, the EMD is a distance between two weighted distributions $S_{X}$ and $S_{Y}$, with the following equation: where $d(v_{x_{i}},v_{y_{j}})$ is the ground distance between the two centroids of different signatures, by default is the L1 distance; and $f_{ij}$ is an element of flow matrix $F$ computed as.

The score obtained from the EMD equation is a dissimilarity value between the texture signatures of the two images $X$ and $Y$. If the images are equal, the score obtained is $0$, while the more dissimilar the two images are, the more the score tends to increase.

### III-B Color Perceptual Dissimilarity Term

Considering that the EMD term only compares texture signatures between two grayscale images, we believe that a good comparison between two images should be made by relating colors as well. For the color dissimilarity term, our goal is to make this index faithful to how humans perceive colors differences. Since the RGB representation is not uniformly perceptual, over the years, various color spaces have been proposed in image processing that mimic the human perceptual ability to recognize colors and their distributions.

Our choice as a color space to use falls on Oklab, which allows a perceptual color representation in a simple way. The other evaluated perceptual color spaces have the following problems: CIE XYZ is perceptually non-uniform; CIE Lab is approximately uniform, but uniformity and linearity of hue present problems in representing blue; LAB2000 is complex because it uses lookup tables to create a non-euclidean hyperspace by not solving non-uniformity problems in blue regions; IPT is specifically designed to be a linear space, sacrificing uniformity, in representing hues; -USC is a very complex, numerically unstable, and not always invertible color space.

Oklab, on the other hand, is designed to ensure uniformity and perceptual linearity in hue, so that it does not have problems such as misrepresentation of the blue region. In addition, among its many features, Oklab guarantees that the coordinates are perceptually orthogonal, the space is numerically simple, easily invertible, scale-independent, and it is the color space that best approximates Munsell space.

Oklab has the same color representation structure as CIE Lab, a color is represented by the three components (L, a, b) where: L represents the perceived brightness in the range of 0 (black) and 1 (white); while a and b are the axes of the opposite space, they are theoretically unbounded, but in practice, if we convert from the RGB color space, where the values are discrete and finite, as shown in Figure 3, the a axis goes in the range of -$0.23$ (green) to +$0.27$ (light magenta) and the b axis ranges from -$0.31$ (blue) to +$0.19$ (yellow).

Figure 3: Displacement of all 2563 possible RGB color combinations in the Oklab perceptual color space.

The properties of perceptually uniform and linear hue permit the calculation of the perceptual distance $\Delta E$ between two color points $p_{1}=(L_{1},a_{1},b_{1})$ and $p_{2}=(L_{2},a_{2},b_{2})$ in Oklab space via the straightforward Euclidean distance between the components of $p_{1}$ and $p_{2}$.

In our notion of perceptual color dissimilarity, we extend this distance to all the pixels of the two images that are the subject of the comparison. Let X and Y be two RGB images of size $M\times N\times 3$, we convert both images to the Oklab color space obtaining $\hat{X}$ and $\hat{Y}$ respectively, and then apply the following dissimilarity equation: where $\hat{X}_{i,j}$ and $\hat{Y}_{i,j}$ are two pixels in the Oklab color space of image $X$ and $Y$ respectively; distances in Oklab space fall in the range between $0$ and $1$, where $0$ corresponds to perfect equality and $1$ to maximum dissimilarity between the colors.

### III-C EDOKS

In addition to the dissimilarity terms, we also propose here a single global similarity metric EDOKS, which is derived from the two dissimilarity terms EMD and OK. We suggest a single overall index that exhibits an average behavior with respect to the two proposed indices. We hypothesize that this may facilitate its utilization by users.

The energy-based normalization process for the generation of signatures, as outlined in algorithm 1, enables signatures within the range of 0 and 1. However, it should be noted that EMD can surpass 1, as the combination with the flow matrix in certain instances can exceed 1. Conversely, the OK term is constrained within the limits of 0 and 1.

Given that both terms function within a comparable scale, the proposed equation aims to encapsulate the mean behavior between the two terms, striving to assign equal weight to both. Given two images $X$ and $Y$ to compare, the EDOK term is calculated with the following equation: where $S_{X}$ and $S_{Y}$ are the signatures of the $X$ and $Y$ images respectively, $\hat{X}$ and $\hat{Y}$ are the $X$ and $Y$ images in the Oklab color space respectively, and $\alpha$ is a weight between 0 and 1 that is used to weigh the two terms based on the context, so that greater priority can be given to the appropriate term.

Considering that EDOK continues to be a dissimilarity term, we present the term EDOKS which is the similarity term obtained as the reciprocal of EDOK: TABLE I: IQA metrics execution times when comparing, at different resolutions, two images of the LIUK4-v2 Dataset distorted with Gaussian Blur. Tests performed on Intel® Xeon® Gold 5215 CPU. The reported times are in sec. where $c$ is a very small constant to avoid performing a division by zero, which might happen when $X$ and $Y$ are equal; because when images are equal EDOK returns 0 as the dissimilarity score.

Although EDOKS is a single performance score, we suggest not only to use it, but also to evaluate the EMD and OK indices at the same time, in order to evaluate in detail the quality of textures and colors, which would not be possible with the average EDOKS overall.

### III-D Computational Analysis

A fundamental aspect that needs to be clarified, given the modularity of our metric, is the computational complexity of EDOKS.

Assuming that each image has $P$ pixels, the most expensive operations of the Oklab term are the conversion to another color space, which requires $O(P)$, and the calculation of the similarity distance for each pair of pixels, which has a cost of $O(P)$.

Regarding the application of the Gabor filter bank, each filter is applied with a convolution that has a cost of $O(PG^{2})$, where $G$ is the size of the Gabor kernel. As the number of filters increases, the complexity of this operation remains unchanged. This is because the application of the 24 Gabor filters has been parallelized across multiple CPU or GPU cores. The subsequent clustering operation has a cost of $O(l^{3})$, where $l$ is the number of patches in the image.

Finally, for EMD we used the implementation of, where the most expensive operation is the loop to find the optimal solution, which has a computational cost of $O(K^{2})$, where $K$ is the size of the two signatures corresponding to the number of clusters, which generally limits the number of elements.

Although some terms have high asymptotic computational complexity, in practical terms it should be noted that the calculation of the EDOKS value is usually applied to images with limited dimensionality. As shown in Table I, we calculated the times on one image of the Large-scale Ideal Ultra high definition 4K version 2 (LIUK4-v2) dataset at different resolutions compared to its Gaussian blurred version, obtaining a runtime consistent with other SOTA IQA metrics.

As shown by the results obtained, it can be seen that models considered to be more performant, such as deep architectures, require longer execution times.

## Results

To evaluate the robustness of our metric to human perception, we conducted experiments on datasets in which the similarity between images is assessed by humans, as in BAPPS datasets. We used the Just Noticeable Difference (JND) and Two Alternative Forced Choice (2AFC) subsets, contained in BAPPS, to conduct our experiments. We show that our metric is closer to human perception than the SOTA metrics. In our experiments, we chose not to use popular datasets such as LIVE, TID2008, CSIQ, and TID2013. This is because, as demonstrated , they are outdated and contain a few types of distortions.

For all experiments performed in this section, the EDOKS parameters were initialized as follows: $p=128$ to achieve a good compromise in the extraction of regional patterns, $\alpha=0.5$ to obtain the same contribution from both terms, and $c$ as the minimum float value representable in Python, which provides an excessive contribution to the equation 5 and prevents division by zero.

Figure 4: Correspondences of similarity metrics with the 2AFC dataset. The horizontal axis represents the perceptual similarity of humans who labeled the 2AFC dataset, as reported . The results show that, compared with other low-level FR methods, EDOKS is the closest similarity metric to human perceptual similarity, while it is close to the results of other deep metrics.

Figure 5: Average scores responses obtained by EDOKS and the SOTA metrics calculated on the JND dataset at the pairs of images rated same (green) and not same (red) by humans. The discrepancy in scores between same and not same subsets obtained by our EDOKS metric shows behavior more consistent with human perception than the scores obtained by other low level metrics, while it is close to the results of other deep metrics.

### IV-A Datasets

Our goal is to evaluate perceptual similarity, to do so we need a dataset that contains a significant number of distortions that are as varied as possible. We therefore opted to use the BAPPS dataset as it contains countless distortions, including artifacts generated by deep CNN models and geometric distortions. BAPPS is patch-oriented, with images distorted at the patch level to appreciate local distortions.

We used the validation subset containing images obtained from the RAISE1k dataset and including both traditional and CNN-based distortions.

The 2AFC dataset contains the assessments of a 5-person jury. Each sample submitted to the jury consists of a patch $x$ derived from an original image of the RAISE1k dataset and two distorted versions $x_{1}$ and $x_{2}$ of the same. The jury had to decide which of the two distorted patches, $x_{1}$ or $x_{2}$, was perceptually most similar to the original $x$ patch.

The JND dataset was created to be more objective than the 2AFC dataset. The three-person jury had less time to look at the images and provide a judgment. Only two images are shown to create this dataset: the reference image and a distorted version of it. The jury is then asked whether the images are the same or not same. The two images are shown for 1 second each, with an interval of 250 ms between them, so that the jury can answer immediately based solely on their perception without being biased.

### IV-B Accuracy

Using the human-labeled 2AFC and JND datasets, we evaluated the similarity of the samples with our EDOKS metric. We compared its values to those obtained with the state-of-the-art (SOTA) metrics to assess which metric best aligns with human perception.

Specifically, since each sample in the 2AFC dataset is a triplet ($x$, $x_{1}$, $x_{2}$), where the jury evaluated which of $x_{1}$ and $x_{2}$ is closer to $x$, we also used our metric in our experiments to evaluate the similarity between $x_{1}$ and $x$ and between $x_{2}$ and $x$ in order to determine which of the two pairs is more similar. Qualitative comparisons were calculated as in and, in Figure 4, the histogram shows how many times the similarity metrics agree with the decisions of the jury that evaluated the 2AFC dataset. The results show that our metric has more perceptual behavior than other low-level metrics, while it is close to the results of other deep metrics. Our goal was not to obtain a total match with human perception, but to show that our metric is more perceptual than the others.

We exploited JND to assess how much the metric penalizes or perceptually rewards similarity between images. Therefore, from the entire JND dataset, we performed a pre-processing by extracting two subsets: same and not same. The subset same contained all pairs of images in which the jury unanimously agrees that the pairs of images have a high level of similarity. The second subset, not same, contained all image pairs in which the jury unanimously agrees in rating the images in each pair as different. From the JND dataset, therefore, all pairs in which the jury's opinions were discordant were excluded. As shown in Figure 5, we averaged the scores of the EDOKS and the SOTA metrics over the two subsets; remember that when the same subset has a lower average value than the not same subset, it is because the metric evaluated is a dissimilarity metric.

This experiment was useful to be able to assess how much the scores of the metrics differ by changing subsets. It is found that EDOKS clearly distinguishes same image pairs from not same image pairs, assigning on average very different scores.

Moreover the low level metrics show difficulty in perceptually distinguishing the two subsets, while deep metrics can clearly distinguish between the two subsets.

Furthermore, this is a good indicator of what value EDOKS should take when two images in this dataset are similar.

### IV-C Statistical comparison

For the statistical analysis of our similarity metric, a comparison with MOS is required, since the dataset used does not directly provide MOS values. We obtained them implicitly from the votes of the jury that labeled the dataset.

Specifically, our MOS scale includes four possible rating levels, where 0 indicates that no judge considers two images to be the same, while 1 indicates that all judges agreed on the similarity of two images.

To evaluated the performance of image quality metrics, we used three correlation measures: Spearman Rank Order Correlation Coefficient (SROCC), Kendall Rank Order Correlation Coefficient (KROCC), and Pearson Linear Correlation Coefficient (PLCC).

SROCC and KROCC can measured the prediction monotonicity of a metric, while the PLCC measured the linear relationship between predicted and reference scores. To compute the PLCC we applied a nonlinear regression analysis, we used the following mapping function as suggested: where $\beta_{i},i=1,2,...,5$, are parameters to be fitted.

For all these three coefficients, the higher the value, the better the correlation.

TABLE II: Overall Performances of Low-Level IQA Indices on the JND Dataset TABLE III: Overall Performances of EDOKS and Deep IQA Indices on the JND Dataset Table II shows that our EDOKS metric significantly outperforms the SOTA low-level metrics. Meanwhile, Table III shows that EDOKS is close to deep metrics, which, although more accurate, lack transparency.

Figure 6: SROCC value as the alpha weight of Eq. 4 varies. The scores were calculated on the JND subset, and the optimal value in this case is α = 0.21. The SROCC values were calculated by varying α from 0 to 1 in increments of 0.01.

### IV-D Ablation Study

In this subsection, we seek to analyze the impact of the combination of our two terms on the final results of EDOKS. The necessity to integrate a term that assesses textures and a term that evaluates colors is discussed.

In the course of our experimental investigations, we eliminated the contributions of the EMD term and the OK term by appropriately adjusting the weight parameter, designated as $\alpha$, within the Eq. 4. The tests conducted in this chapter are analogous to those in the preceding chapter, with the distinction that the individual terms are compared with the combination of the two.

In Figure 6, we can see the usefulness of the coefficient $\alpha$. As $\alpha$ changes, the weights of the individual terms in the equation change and so do the contributions they make to the final score. To illustrate this phenomenon, we computed the SROCC on the JND dataset as the parameter $\alpha$ varies. It can be seen that with $\alpha$ tending towards 0, the absence or small contribution of the EMD term in the formula had a significant impact on the SROCC obtained on the JND dataset.

After showing the behavior of the metric as $\alpha$ varies, we analyze the extreme cases, in which the EDOKS score is obtained with the sole contribution of the EMD term or with the sole contribution of the OK term.

Table IV shows the scores of the various experiments, demonstrating that the combination of the two terms yields a better result than the use of the individual terms.

In general, it should be noted that distortions can occur in both colors and shapes. As demonstrated by our results, using only one of the two terms is not sufficient to evaluate both types of distortion. However, in a specific case where the type of distortion applied is known (e.g., only color distortions), we allow the possibility of configuring the weight $\alpha$ to obtain an analysis that is as consistent as possible with the case study.

The average scores (AVG) TABLE IV: Study of the ablation of the edoks metric by evaluating its individual terms against itself. The AVG scores and statistical metrics (SROCC, KROCC, PLCC) were obtained from the JND dataset, while the accuracy values refer to the 2AFC dataset.

## Interpretability Validation

EDOKS overall map Figure 7: Examples of explainability provided by EDOKS. The first four rows show images from the LIU4K_v2 dataset, and the last row shows a publicly licensed image. The first two columns contain pairs of images to be compared: the original image and its distorted version. The third column shows the map of average magnitude differences extracted for the EMD term. The fourth column shows heatmaps of color differences calculated from the OK term. The fifth column shows the combination of the two maps provided by the two terms. EDOKS scores for these five images: 4.58; 2; 4.18; 26.65 and 3.99 The SOTA metrics discussed in this paper provide a similarity score, but they were not designed to justify the provided score. In fact, studies show that metrics such as PSNR do not consistently readjust their score when the degree of distortion is altered. Without a heatmap highlighting the perceptual differences between two images according to the IQA metric, it is difficult for users to understand what affected the similarity score. This forces users to conduct appropriate experiments to extrapolate the discriminatory and perceptual behavior of the IQA metric.

Meanwhile, we developed EDOKS with the aim of providing a perceptual score and maps of interest showing the discriminative areas that the metric extracts and uses to determine its score.

Figure 7 shows examples of EDOKS's ability to identify discriminatory areas with the greatest difference between two images $X$ and $Y$, providing maps of interest based on differences in shapes and colors.

The EMD difference column highlights the points where the two images differ in shape. The difference in magnitude $|F|$ between the two images is shown, averaging the magnitude differences across all scales $s$ and orientations $o$.

Meanwhile, the OK heatmap column highlights the color difference $\Delta E(\hat{X}_{i,j},\hat{Y}_{i,j})$ between all pixels of the two images in the Oklab space.

The last column shows an overlay of the two maps calculated on shapes and colors, providing a general overview of the elements that influenced the EDOKS calculation.

The areas that influenced the score coincide with the distorted areas between the two images. Furthermore, the analysis shows that EDOKS is not influenced by distractors because it never highlights the subject of the image and does not present any type of distortion. In fact, the EDOKS map in the first row shows that EDOKS does not identify any color or texture alterations on the butterfly.

Figure 8: Examples of explainability provided by EDOKS in a borderline case. The heatmaps provided by EDOKS and the scores calculated by other metrics are shown.

Another interesting point is the necessity of using both EMD and OK terms in the EDOKS equation. Alterations were created ad hoc in some areas of the image to stress and challenge the metric. Some areas are more noticeable with one term than the other.

For instance, the difference between the green and magenta backgrounds in the first row is more noticeable with the term "OK" than with the term "EMD", which, like some metrics that convert color to grayscale intensity by assuming similar values, loses information about the clear difference between the two colors. Similarly, the OK term fails to capture geometric differences while the EMD term does.

This demonstrates that using a single term is necessary to capture a type of distortion but insufficient for a comprehensive analysis of perceptual similarity.

The second row presents Gaussian smoothing and image negation as distortion. From the maps provided by EDOKS, it can be seen that the metric detects many differences in shape. This is caused by Gaussian smoothing, which erodes all the edges in the image, while the color differences are due to image negativization. It can be seen that all the dark areas become super bright, becoming the areas where the metric highlights the greatest differences.

In the third row, there is a sinusoidal wave warping distortion. From the maps, it can be seen that the texture map highlights the distortion on the shapes, while the color heatmap shows that the color difference highlighted by the metric is only present on the distorted edges and that the image does not show any other color distortions.

The fourth row contains an occlusive element that the metric identifies in both heatmaps. This highlights the only difference between the two images.

For the fifth row, we tested EDOKS with a nocturnal image featuring elastic warping. The maps of interest demonstrate that EDOKS can highlight differences and justify the provided score in terms of both shapes and colors.

In Figure 8, the EDOKS metric and the other metrics discussed in this document were tested on a freely licensed image for road signs.

Image $X$ is a no-entry sign for bicycles because it contains a circle with a red border, while image $Y$, although not completely blue, resembles a mandatory sign used for cycle paths due to the presence of this color. The opposite meanings of the two road signs would cause a serious road safety problem.

We show the scores of all the metrics, as well as the EDOKS maps of interest. Our goal is to demonstrate the usefulness of having visible evidence of what the metric considers when providing a score.

Many metrics, such as SSIM, PSNR-HVSM, VIF, DSS, and SSIM variants, provided a maximum similarity score. This means that, for these metrics, the two images are identical, even if they have a color distortion that is obvious to the human eye. So why do they perform this way?

Without a module that makes them transparent and shows their behavior, it is difficult to determine. Scrutinizing their operations, they convert color images to grayscale using the ITU-R BT.601 standard, so that only the luminance is used. The problem is that many color combinations, such as this shade of red and blue, are converted to the same gray intensity, resulting in two identical images for metrics that adopt this conversion.

Meanwhile, EDOKS provides a similarity score of 13.511, and $\Delta|F|_{XY}$ shows that it has not detected any distortions in the shapes, while the $\Delta E_{XY}$ heatmap highlights color differences in the area where the distortion is applied. We believe that this helps users to evaluate their images beyond simply using numerical scores.

## Conclusions

In this paper, we aimed to highlight the difficulties of SOTA FR-IQA metrics in the perceptual evaluation of images. Therefore, we proposed a new similarity metric, EDOKS, which solves these problems and stands as an alternative to existing metrics in the literature.

Unlike other similarity indices based on the use of black-box models, such as the LPIPS metric, our proposed metric is interpretable. This means that it is possible to understand why EDOKS provides a similarity score by analyzing the individual terms EMD and OK, which are themselves interpretable because they do not use black-box models, but provide information, respectively, on the dissimilarity of the textures and colors of the compared images through filtering algorithms.

For future developments we believe it may be useful, depending on contexts, to modify parameters such as patch size $p$, Gabor filtering, clustering algorithm or distance used in OK. We would also investigate the addition of terms to analyze other types of characteristics in the image that could be indispensable in contexts other than the shape distortions we have analyzed in this work. Furthermore, we evaluate the possibility of exploring the Pareto front for $\alpha$ optimization in Eq. 4.

Following the experiments and discussions, we recommend using EDOKS; we have demonstrated that, especially in the presence of geometric distortion, the EDOKS metric is a more valid perceptual metric compared to the others.

## Code Availability

We hope that our perceptual metric will be of interest to the scientific community.

To support the reproducibility of our results, the implementation of the proposed similarity metric is made publicly available :
