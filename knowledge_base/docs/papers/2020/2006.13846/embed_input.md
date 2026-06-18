<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Understanding SSIM

Topics include Neural networks, Deep learning, Learning, Structural similarity index measure.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The use of the structural similarity index (SSIM) is widespread. For almost two decades, it has played a major role in image quality assessment in many different research disciplines. Clearly, its merits are indisputable in the research community. However, little deep scrutiny of this index has been performed. Contrary to popular belief, there are some interesting properties of SSIM that merit such scrutiny. In this paper, we analyze the mathematical factors of SSIM and show that it can generate results, in both synthetic and realistic use cases, that are unexpected, sometimes undefined, and nonintuitive. As a consequence, assessing image quality based on SSIM can lead to incorrect conclusions and using SSIM as a loss function for deep learning can guide neural network training in the wrong direction.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The original SSIM paper has over $20,000$ citations on Google Scholar. Thousands of research papers have used it as a quality index when comparing images, and we are indeed authors of a few of those. In this paper, we provide a review and a deep inspection of SSIM, and we show that SSIM can deliver unexpected or invalid results in both simple use cases and for real image pairs. See Figure LABEL:fig_teaser. We start with an overview of SSIM.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The input color space of SSIM is never defined. As the reference Matlab script performs no color space transformations on inputs, our assumption throughout this paper is that all images are encoded in sRGB color space, i.e., approximately gamma encoded with an exponent $\approx 2.4$. Note that this means that an image that is loaded by the SSIM script is assumed to be viewed directly on screen as is. For two images A and B, the original formula for per-pixel SSIM is given by

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where A and B are inputs to all functions, but omitted for clarity. To compute mean, variance, and covariance in a patch around a pixel, they use Gaussian-weighted versions of these formulae with a filter kernel of $11 \times 11$ pixels and $\sigma = 1.5$. The luminance component, $l$, is then

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $w$ and $h$ are the width and height of the image. As can be seen, the term $\sigma_{\text{A}}\sigma_{\text{B}}$ is in the numerator in Equation 3 and in the denominator in Equation 4. To create a simplified expression, Wang et al. therefore proposed to use $\alpha = \beta = \gamma = 1$ and $C_{3} = {C_{2}/2}$, which results in

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Next, we review some related work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

The universal quality index (UQI), which was introduced by Wang and Bovik, is essentially SSIM as presented above, but without any of the constants $C_{i}$. These constants were added later to avoid division by zero. Multi-scale SSIM (MS-SSIM)^22^2Note the difference between MSSIM, which is the average SSIM value over an image pair, and MS-SSIM, which is the multi-scale variant of SSIM. was introduced as a means for including image details at different scales. MS-SSIM adds more components in the expression, where both the contrast and structure expressions are evaluated at five low-pass filtered and downsampled versions of the original images. However, the components have the same form as in SSIM.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

Sampat et al. introduce complex wavelet structural similarity (CW-SSIM), where the expression in Equation 6 is used, but where the components are replaced by complex wavelet coefficients. CW-SSIM is more tolerant to small translations and rotations, which may be a desired effect in some contexts. However, for rendered images, which often contain geometrical edges, it is most likely not a desired feature, since, for instance, a game designer usually wants the geometry to be precisely where he/she intends. 3D-SSIM is an extension of SSIM for video, where the formulae are evaluated for three-dimensional blocks of pixel values and multiplied with information content weights and local distortion weights. SSIM is still being adapted for new uses, e.g., spherical SSIM, where SSIM was adapted to handle a spherical projection, and for medical images.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

While mean square error (MSE) has been criticized for not delivering a truthful value compared to image error, Dosselman and Yang and Horé and Ziou have, at the same time, shown that there is a close relationship between MSE and SSIM. Whittle et al. evaluate image metrics for Monte Carlo rendered images with different levels of noise. Their conclusion is that MS-SSIM performs well for this task. Čadík et al. perform an extensive evaluation of image indices and metrics together with a user study, and find contradictory results for several of the algorithms, including SSIM, for various image distortions. Recently, SSIM has found uses as a loss function for deep learning, and is also included in tool kits such as Tensorflow.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

Neither the UQI nor SSIM make any claim to be a *metric* in the mathematical sense, for which the triangle inequality, i.e., ${d{(x,z)}} \leq {{d{(x,y)}} + {d{(y,z)}}}$, must hold. It has, however, been shown that $\sqrt{1 - {l{(x,y)}}}$ and $\sqrt{1 - {c{(x,y)}s{(x,y)}}}$ do fulfill the triangle inequality, and thus are metrics. Interestingly, the derivation to transform a modified version of SSIM into a metric, also revealed subtle---while important---properties of the index.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

which can be seen as a normalized version of the root mean square error (RMSE).

<!-- chunk {"id": "body-0013", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

This is notable, since MSE is not a perception-based metric and the finding above has the implication that there could exist a direct relationship between SSIM and MSE, which has indeed been independently discovered by Dosselman and Yang and Horé and Ziou. Specifically, Dosselman and Yang show that there is a direct mathematical transform between $\text{SSIM}^{\ast}$ and $\text{MSE}^{\ast}$. $\text{SSIM}^{\ast}$ is SSIM with constants $C_{i} = 0$, which does not alter the validity of the analysis, while $\text{MSE}^{\ast}$ is a local MSE, using the same footprint as SSIM. They further show this empirically by correlating MSE versus SSIM for a range of images, using the coefficient of multiple determination, $R^{2}$, which is $0.0$ for no association between the variables and values closer to $1.0$ indicate strong degree of correspondence.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

It was found that $R^{2}$ was between $0.9322$ and $1.0$, which implies that $\text{SSIM}^{\ast}$ and $\text{MSE}^{\ast}$ perform similarly.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

For images of similar luminance, i.e., $\mu_{\text{A}} \approx \mu_{\text{B}}$, and SSIM values in the $\lbrack 0.2,0.8\rbrack$ range, this function is approximately linear, which indicates that for any other distortion than a luminance shift, $\text{SSIM}^{\ast}$ is qualitatively equivalent to PSNR.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The History of SSIM", "weight": 1.0} -->

These findings question the validity of claims that SSIM is a perception-based index, since MSE is not a perception-based metric. The small discrepancies in correlation between MSE and SSIM were shown to stem partly from the fact that SSIM is derived for a spatial subregion of the whole images, and an effect of the $C_{i}$ constants.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Mathematical Properties", "weight": 1.0} -->

This section will analyze the components of SSIM from a mathematical standpoint. The behavior of the quality index itself will be scrutinized in the next section.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Minimum Values of the SSIM Factors", "weight": 1.0} -->

To understand the workings of the components of SSIM, as we will see later in this section, and since it, to our knowledge, has not been done before, we explain how to minimize $l$, $c$, and $s$, one at a time. For $l{(x,y)}$, shown in Equation 2, we can differentiate and solve for zero, with the assumptions that ${\mu_{\text{A}},\mu_{\text{B}}} \in {\lbrack 0,L\rbrack}$. This gives us a minimum when $\mu_{\text{A}} = 0$ and $\mu_{\text{B}} = L$ (or vice versa).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Minimum Values of the SSIM Factors", "weight": 1.0} -->

As a result, SSIM=$c_{\min}$. Looking at the second row of Figure 2 with a low dot pitch, it is hard for the human visual system (HVS) to discern differences between the images, while SSIM values are close to zero, which indicates low quality contrary to the actual experience. The last row in Figure 2 achieves SSIM=$s_{\min}$ by using two inverted checkerboard images. Note that all three minima are independent of $L$, as expected, and it is clear that the range of SSIM is $({- 1},1\rbrack$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Minimum Values of the SSIM Factors", "weight": 1.0} -->

While most people use the simplified version (Equation 6) of SSIM, which is also what the reference implementation uses, the constants $\alpha$, $\beta$, and $\gamma$ have been used to find a more optimized SSIM expression for antialiasing detection in games, but also in MS-SSIM, and for optimizing SSIM parameters using machine learning. Therefore, it is important to take a look at the components in the full SSIM expression (Equation 1) as well and see what their ranges are. The $s$ component (Equation 4) deserves additional attention. If $C_{3}$ is zero, $s{(x,y)}$ is equivalent to the sample Pearson correlation coefficient, usually denoted $r_{xy}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Minimum Values of the SSIM Factors", "weight": 1.0} -->

We have found no scientific support that this coefficient correlates with human perception of "structure." As mentioned in the introduction, SSIM has selected $C_{3} = {C_{2}/2} = {{({K_{2}L})}^{2}/2} = {{({0.03 \cdot 1})}^{2}/2} = 0.00045$, for pixel values in the range $\lbrack 0,1\rbrack$. Since by definition we have $\sigma_{\text{A}} \geq 0$ and $\sigma_{\text{B}} \geq 0$, the denominator will always be positive. The covariance term $\sigma_{\text{A}\text{B}}$ can take on negative values, which means that $s{(x,y)}$ can be negative.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Minimum Values of the SSIM Factors", "weight": 1.0} -->

Note that raising a negative number to a positive, non-integer number, $\gamma$, results in a complex number (with a real and an imaginary part), which in practice, e.g., in programming languages, makes the result undefined. The std::pow function gives NaN (not a number) when a negative number is raised to a number (even to one). MS-SSIM uses non-integer $\gamma$-values, as do the work of Čadík et al. and Piórkowski & Mantiuk, so it seems that this is not well-known.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Minimum Values of the SSIM Factors", "weight": 1.0} -->

Undefined results (or complex numbers), unless properly defined, should not be an outcome of an image quality index. Even if the range of SSIM is allowed to be complex, there are no descriptions on how to interpret such values. To our knowledge, this problem has never been identified before and means that SSIM implementations can generate undefined results for some inputs and parameter settings.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Perceptual Properties", "weight": 1.0} -->

The purpose of deriving these minima is not only out of curiosity, but also hints at a deeper problem with the index itself and the claims of it being based on perception. Referring to the two bottom examples in Figure 2, it could be argued that detecting the difference between the images leading to a minimum value for $c$ and $s$ is hard (please look at the images in the supplemental material). Depending on the monitor dot pitch and viewing distance, any difference between the images $128/255$ and $\left. b \middle| w \right.$ can be indistinguishable to a human viewer. The same is true for the bottom row, images $\left. b \middle| w \right.$ and $\left. w \middle| b \right.$. This property will be further investigated in Section 4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Perceptual Properties", "weight": 1.0} -->

As far as we can see, the only perception related claims made in the SSIM paper is that the $l$ component is qualitatively consistent with Weber's law and that the $c$ component is consistent with the contrast-masking feature of the HVS. This is somewhat contradictory, since in the original UQI paper, the authors explicitly state that "the new index is mathematically defined and no human visual system model is explicitly employed." Weber's law states that the ratio between the difference in stimulus against a *background* signal, to achieve the same psychophysical sensation, is approximately constant ($\frac{\DeltaS}{S} = k$). Contrast-masking is the destructive interference between (transient) stimuli closely coupled in space and time. Both these psychophysical phenomena are well known. However, these effects are both defined only *within the same frame of reference*, i.e., when introducing stimuli onto some sort of background. Consequently, in the context of image comparisons, these effects hold true for a local pixel value against its background *within* the same image, and not true for variations *between* images.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Perceptual Properties", "weight": 1.0} -->

The claim that the $l$ factor is perceptually motivated is problematic. Evidence for this can easily be found and first, we point to Figure 4 to get a feel for this. To explain these results, we refer to Figure 3, which shows a plot of SSIM as a function of a constant colored image from black to white, against both a black and a white image. Note that, as before, $c = s = 1$. As can be seen, when the comparison is against a black image, A, and the image B is close to black, a minuscule change in B triggers a huge difference in $l$, and thus in SSIM. Furthermore, when A is black and $\text{B} > 0.2$, $l$ is always close to zero. The other case, when A is white, is not as radical, but for nearly white images B, relatively large changes in B do not change the SSIM value much. Section 4.1 reveals several interesting, nonintuitive results based on this diagram, and as a consequence, shows that the $l$ component is not perceptually based.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation", "weight": 1.0} -->

All results showing MSSIM values and the images of SSIM index maps were computed using the Matlab script (www.cns.nyu.edu/\~lcv/ssim/) of Wang et al. All images are made available as supplemental material, as well as the scripts to generate our results. Since images ideally should be viewed on a display at 100% scale, instead of in a PDF viewer or on paper, we urge the reader to look at the images in our supplemental material. $SSIM$ is visualized using a heatmap where white is ${SSIM} = 1$ (identical images), black is ${SSIM} = 0$, and SSIM values in $({- 1},0\rbrack$ map to $({red},{green}\rbrack$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Luminance", "weight": 1.0} -->

SSIM was designed so that ${{MSSIM}{(\text{A},\text{A})}} = 1$, that is, if the images are the same, MSSIM will be one, and in general, a value $\geq 0.99$ indicates that the images are indistinguishable. Here, we will explore how MSSIM behaves for images that only contain a single grayscale value. For such images, $c = 1$ and $s = 1$, and therefore, it is only the $l$ component that affects the values in this experiment. In Figure 4 we reveal some results that have previously been unknown (to the best of our knowledge).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Luminance", "weight": 1.0} -->

The first row compares a white ($255/255$) image against a nearly-white ($253/255$) image, and MSSIM is almost one, which makes sense, since it is hard to see any difference between these two images. The difference in grayscale values is $2/255$. On the second row, we do the same but for mid-gray images with difference $2/255$ and the result is similar. However, the third row compares a black image to a nearly-black ($2/255$) image, again with a difference of 2/255, and in this case, MSSIM values are low, indicating that the images are not similar, when, in fact, it is difficult to see any difference between the two.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Luminance", "weight": 1.0} -->

The fourth row is, perhaps, even more surprising, since MSSIM values indicate that the images are similar, while they visually are not. In the fifth row, the MSSIM values indicate that these two images are dissimilar, and when increasing the value from 26 up to 255, the MSSIM value decreases to 0.0. This means that for 90% of the range, MSSIM is close to zero, which unreasonably compresses the resolution of the index. Mathematically, this stems from the quadratic forms in the normalization denominator ($\mu_{\text{A}}^{2} + \mu_{\text{B}}^{2} + C_{1}$) of Equation 2, which exaggerates differences near black. Regardless, SSIM does not seem to be aligned with the HVS's ability to detect luminance differences. The orange and blue curves in Figure 3 predict the results shown in Figure 4, confirming that $l$ component of SSIM can be misleading.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Color", "weight": 1.0} -->

The SSIM authors present results using only JPEG and JPEG2000 color images, but add that using other color components does not significantly change the performance of the model. The index has still, nevertheless, been used on color images by first converting to grayscale values, using, for example, the color encoding standard Rec.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Color", "weight": 1.0} -->

It is well-known that there are many colors of equal luminance and furthermore that any mapping between $RGB$ and grayscale value is many-to-one. As a consequence, SSIM can generate a high value, indicating similarity, even though the colors are visibly dissimilar. This is visualized for three color pairs in Figure 5, where the original rgb2gray function in Matlab has been used. It is evident that simply converting from RGB to grayscale values can give erroneous SSIM results, as would any metric relying on a reduction function from color to grayscale. Even the original SSIM paper does this, and based on our findings here, we advise not to use SSIM with color images. A better solution would be to use a metric that inherently handles color.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gradients", "weight": 1.0} -->

Next, we compare an image containing a gradient against a horizontally mirrored version of the same image at different resolutions. The results are summarized in Figure 6. In all examples, $c = 1$ and the image of $l$ (not shown) contains vertical lines of constant values, starting with a low value at the left, peaking in the middle, and going down to a low value at the right. The $s$ component, which is not shown in the figure, starts at $0.86$ for the pair with $256 \times 256$ pixels, but goes down to $- 0.10$ for the middle row ($64 \times 64$), and even further down to $- 0.90$ for $16 \times 16$ pixels, which means that it is the $s$ component that makes MSSIM values in Figure 6 negative toward the bottom. This was surprising since the A images are similar at all resolutions, as are the B images. Assuming the $256 \times 256$ and the $16 \times 16$ gradients are part of a large image, the perceived error in the $16 \times 16$ region will surely be less glaring than in the $256 \times 256$ region.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Gradients", "weight": 1.0} -->

This is the opposite of the results, generated by SSIM, shown in Figure 6.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gradients", "weight": 1.0} -->

Recall that a negative $s$ to the power of a non-integer value generates a complex number or an undefined result (see the last part of Section 3.1), and this problem will occur for the two bottom rows in Figure 6. These examples might seem overly contrived, but serve to demonstrate that it is indeed possible, and not highly unlikely, for SSIM to generate negative values for simple distortions (see also Figure LABEL:fig_teaserc, LABEL:fig_teasere, and LABEL:fig_teaserf, which are discussed below).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Complex Images", "weight": 1.0} -->

The average MSSIM value has been correlated with the subjective quality (five levels, from "Bad" to "Excellent") of JPEG-compressed images. The resulting SSIM image has however, to our knowledge, never been evaluated with subjective observers. It is certainly true that SSIM in many cases finds image differences that are also detected by a human observer. Had it not, its use would have been less widespread. With well-behaved image pairs, the corresponding SSIM map tells a convincing story. Synthetic examples (seen above, for example) serve to clarify situations where SSIM behaves contradictory to human perception, and it can be challenged whether these situations arise for more general images with reasonable distortions. In the following, we will demonstrate several such cases. All observations have been carried out on a Dell UP3216Q monitor, calibrated for sRGB, with a D65 standard illuminant.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Complex Images", "weight": 1.0} -->

We start by discussing the images in Figure LABEL:fig_teaser in more detail. In image pair a, the surface of the moon has substantially different luminance, but that error is detected as lower than the text "Houston, we have a problem!', which is difficult to see for most people. As we have seen earlier, this can be explained using Figure 3. The test image in b has its chrominance shifted compared the reference, and it is clear that SSIM does not react much to this, and the explanation to this is given in Section 4.2. Image pair c is from the LocVis database and shows a situation where the SSIM values are high on the red door and on the red window shutters, while it is clear that there are differences. The explanation is that after grayscale conversion, the grayscale values on the door and window shutters are the same in the reference and test images.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Complex Images", "weight": 1.0} -->

Image pair d, from the CS-IQ database, shows that SSIM sometimes can generate high SSIM values on edges in images, even though the error is evenly spread out over the entire image. As can be seen below the SSIM images, the $l$, $c$, and $s$ components are all white on edges, so none of the terms detect the induced error. In image pair e, we have introduced a dithering that in a checkerboard pattern adds and subtracts 6 from the pixel (8-bit) grayscale value, clamped to 0 and 255, respectively. The test image uses the same, but inverse, dithering. To the human observer, we claim that these distortions have little, or no, visual impact. SSIM, however, finds these two images very dissimilar with many pixels generating negative (green) SSIM values. As seen in Section 3.1, a negative value to the power of a floating-point exponent is undefined in most programming languages or otherwise generates a complex number. Again, this is difficult to interpret in an image quality measure.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Complex Images", "weight": 1.0} -->

The images in Figure LABEL:fig_teaserf, with lowered contrast compared to reference, also from the CS-IQ database, show an SSIM image that is particularly counterintuitive---in the bright regions, where visible differences can be argued to be largest, the SSIM image is bright as well, while in the dark regions of the reference and test image, SSIM values are much lower. As can be seen below the SSIM image, it is mostly the $l$ component that makes this so, which has been explained in Section 4.1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Complex Images", "weight": 1.0} -->

Turning to Figure 7, image pair a is a path traced rendering with different sample counts per pixel, for which the SSIM values at first seems to correspond well with the actual image differences. Closer inspection reveals two important exceptions, namely, high similarity along all high contrast edges, and an unreasonable dissimilarity for darker regions, mainly attributed to the $c$ component. In Figure 8, we have zoomed in on the trash can in these images, to further illustrate how large the region around an edge is, with very high SSIM values. Image pair b, from LocVis, with different lighting conditions for reference and test, is noteworthy, since it demonstrates both a false positive (spot under the Buddha, nearly invisible) and a false negative (failure to detect luminance shift in the upper background) in the same image. The JPEG-compressed test image in c, from CS-IQ, is highly distorted in the detailed regions. A slight difference in gray level in the dark regions between the reference and test images, however, dominates the final output. Additionally, a few negative values show up for the $s$ component.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Complex Images", "weight": 1.0} -->

Another example of what we consider is a false negative, is the blotchy distortion of image d (from LocVis), which most notable on the green floor. SSIM fails to detect this disturbing variation in intensity. Turning to the heavily blurred test image in e, from CS-IQ, the different components of SSIM again highlights dark regions where the images only differ by a small amount. The large drop in intensity of the sun is nearly ignored and the indication of high similarity in its middle is exaggerated. For the synthetic image pair in f, from LocVis, the $c$ component shows dissimilarity around the edges of the circles, while the $l$ component, containing information about the intensity levels within the circles, shows high similarity. We consider the lower left circle in the test image to be significantly different from the reference image, but it does not show up much inside the circle. The final image pair g, from CS-IQ, is reported as strikingly dissimilar by SSIM across all dark regions, which is indicated by both the $l$ and $c$ components.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Complex Images", "weight": 1.0} -->

The additive noise distortion is spread evenly across the whole test image, but in our opinion, these errors are harder to detect in darker areas, which seems to be the inverse behavior of SSIM.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have demonstrated the mathematical properties of SSIM and shown that it is not adhering to properties of the human visual system. This is not surprising, as it was not a goal stated in the original work upon which SSIM is based. However, over time, the similarity index has grown in number of uses, and popular belief of the index's capabilities has significantly widened with respect to this original scope. The purpose of this paper is to moderate this belief, since it can guide research in the wrong direction. Even though SSIM generates useful results in some cases, it can generate counterintuitive results in many others, as we have seen. This opens the door to research improved metrics to describe how humans detect differences between images, be they synthetic, rendered, or natural.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusions", "weight": 1.0} -->

SSIM is at its core a statistical measure, a product of three local dissimilarity factors, namely, luminance, variance, and correlation. We have derived these factors' minima and shown how their ranges and normalization are creating nonintuitive results. This occurs, for example, for low luminance values or when the local distribution of pixel values visually differ very little, though regularly. We have also shown that the original SSIM formulation with certain parameters can output undefined results. For one of the major areas of use for SSIM, namely rendering, these results constitute the core of the index's weaknesses---both as a qualitative indication, using the pooled MSSIM value, and as a quantitative value, when using the SSIM map to understand the visual performance of rendering algorithms.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Current graphics and rendering research has a major focus on Monte Carlo ray tracing and denoising and reconstruction algorithms using neural networks. Such networks often introduce small variations during training and could potentially suffer disproportionately from the shortcomings of SSIM. We thus encourage further graphics research to employ the index with care and caution, or preferably replace it, since its use may distort or bias image quality assessment. The difference evaluator for alternating images ( F LIP), is a step toward such a replacement.
