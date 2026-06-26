<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ResShift: Efficient Diffusion Model for Image Super-Resolution by Residual Shifting

Topics include Image super-resolution, Real-world super-resolution, Diffusion models, Residual shifting, Efficient sampling, Blind restoration, Noise schedule, ResShift.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

ResShift reframes diffusion super-resolution as a residual-shifting process between low- and high-resolution images, allowing high-quality results with far fewer denoising steps. It is a useful counterpoint to heavier diffusion restoration systems because its main contribution is sampling efficiency rather than model scale.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Diffusion-based image super-resolution (SR) methods are mainly limited by the low inference speed due to the requirements of hundreds or even thousands of sampling steps. Existing acceleration sampling techniques inevitably sacrifice performance to some extent, leading to over-blurry SR results. To address this issue, we propose a novel and efficient diffusion model for SR that significantly reduces the number of diffusion steps, thereby eliminating the need for post-acceleration during inference and its associated performance deterioration. Our method constructs a Markov chain that transfers between the high-resolution image and the low-resolution image by shifting the residual between them, substantially improving the transition efficiency. Additionally, an elaborate noise schedule is developed to flexibly control the shifting speed and the noise strength during the diffusion process. Extensive experiments demonstrate that the proposed method obtains superior or at least comparable performance to current state-of-the-art methods on both synthetic and real-world datasets, even only with 15 sampling steps. Our code and model are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Image super-resolution (SR) is a fundamental problem in low-level vision, aiming at recovering the high-resolution (HR) image given the low-resolution (LR) one. This problem is severely ill-posed due to the complexity and unknown nature of degradation models in real-world scenarios. Recently, diffusion model, a newly emerged generative model, has achieved unprecedented success in image generation. Furthermore, it has also demonstrated great potential in solving several downstream low-level vision tasks, including image editing, image inpainting, image colorization. There is also ongoing research exploring the potential of diffusion models to tackle the long-standing and challenging SR task.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One common approach involves inserting the LR image into the input of current diffusion model (e.g., DDPM ) and retraining the model from scratch on the training data for SR. Another popular way is to use an unconditional pre-trained diffusion model as a prior and modify its reverse path to generate the expected HR image. Unfortunately, both strategies inherit the Markov chain underlying DDPM, which can be inefficient in inference, often taking hundreds or even thousands of sampling steps. Although some acceleration techniques have been developed to compress the sampling steps in inference, they inevitably lead to a significant drop in performance, resulting in over-smooth results as shown in Fig. 1, in which the DDIM algorithm is employed to speed up the inference. Thus, there is a need to design a new diffusion model for SR that achieves both efficiency and performance, without sacrificing one for the other.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let us revisit the diffusion model in the context of image generation. In the forward process, it builds up a Markov chain to gradually transform the observed data into a pre-specified prior distribution, typically a standard Gaussian distribution, over a large number of steps. Subsequently, image generation can be achieved by sampling a noise map from the prior distribution and feeding it into the reverse path of the Markov chain. While the Gaussian prior is well-suited for the task of image generation, it may not be optimal for SR, where the LR image is available. In this paper, we argue that the reasonable diffusion model for SR should start from a prior distribution based on the LR image, enabling an iterative recovery of the HR image from its LR counterpart instead of Gaussian white noise. Additionally, such a design can reduce the number of diffusion steps required for sampling, thereby improving inference efficiency.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following the aforementioned motivation, we propose an efficient diffusion model involving a shorter Markov chain for transitioning between the HR image and its corresponding LR one. The initial state of the Markov chain converges to an approximate distribution of the HR image, while the final state converges to an approximate distribution of the LR image. To achieve this, we carefully design a transition kernel that shifts the residual between them step by step. This approach is more efficient than existing diffusion-based SR methods since the residual information can be quickly transferred in dozens of steps. Moreover, our design also allows for an analytical and concise expression for the evidence lower bound, easing the induction of the optimization objective for training. Based on this constructed diffusion kernel, we further develop a highly flexible noise schedule that controls the shifting speed of the residual and the noise strength in each step. This schedule facilitates a fidelity-realism trade-off of the recovered results by tuning its hyper-parameters.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, the main contributions of this work are as follows: We present an efficient diffusion model for SR, which renders an iterative sampling procedure from the LR image to the desirable HR one by shifting the residual between them during inference. Extensive experiments demonstrate the superiority of our approach in terms of efficiency, as it requires only 15 sampling steps to achieve appealing results, outperforming or at least being comparable to current diffusion-based SR methods that require a long sampling process. A preview of our recovered results compared with existing methods is shown in Fig. 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We formulate a highly flexible noise schedule for the proposed diffusion model, enabling more precise control of the shifting of residual and noise levels during the transition.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methodology", "weight": 1.0} -->

In this section, we present a diffusion model, ResShift, which is tailored for SR. For ease of presentation, the LR and HR images are denoted as ${\mathbf{y}}_{0}$ and ${\mathbf{x}}_{0}$, respectively. Furthermore, we assume ${\mathbf{y}}_{0}$ and ${\mathbf{x}}_{0}$ have identical spatial resolution, which can be easily achieved through pre-upsampling the LR image ${\mathbf{y}}_{0}$ using nearest neighbor interpolation if necessary.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model Design", "weight": 1.0} -->

The iterative generation paradigm of diffusion models has proven highly effective at capturing complex distributions, inspiring us to approach the SR problem iteratively as well. Our proposed method constructs a Markov chain that serves as a bridge between the HR and LR images as shown in Fig. 2. This way, the SR task can be accomplished by reverse sampling from this Markov chain given any LR image. Next, we will detail the process of building such a Markov chain specifically for SR.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model Design", "weight": 1.0} -->

The transition distribution is then formulated based on this shifting sequence as follows: where $\alpha_{t} = {\eta_{t} - \eta_{t - 1}}$ for $t > 1$ and $\alpha_{1} = \eta_{1}$, $\kappa$ is a hyper-parameter controlling the noise variance, $\mathbf{I}$ is the identity matrix. Notably, we show that the marginal distribution at any timestep $t$ is analytically integrable, namely The design of the transition distribution presented in Eq. is based on two primary principles. The first principle concerns the standard deviation, i.e., $\kappa\sqrt{\alpha_{t}}$, which aims to facilitate a smooth transition between ${\mathbf{x}}_{t}$ and ${\mathbf{x}}_{t - 1}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model Design", "weight": 1.0} -->

This is because the expected distance between ${\mathbf{x}}_{t}$ and ${\mathbf{x}}_{t - 1}$ can be bounded by $\sqrt{\alpha_{t}}$, given that the image data falls within the range of $\lbrack 0,1\rbrack$, i.e., where $\text{max}{\lbrack \cdot \rbrack}$ represents the pixel-wise maximizing operation. The hyper-parameter $\kappa$ is introduced to increase the flexibility of this design. The second principle pertains to the mean parameter, i.e., ${\mathbf{x}}_{0} + {\alpha_{t}{\mathbf{e}}_{0}}$, which induces the marginal distribution in Eq..

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model Design", "weight": 1.0} -->

Furthermore, the marginal distributions of ${\mathbf{x}}_{1}$ and ${\mathbf{x}}_{T}$ converges to $\delta_{{\mathbf{x}}_{0}}{(\cdot)}$^11^1$\delta_{\mathbf{μ}}{(\cdot)}$ denotes the Dirac distribution centered at $\mathbf{μ}$. and $\mathcal{N}{(\cdot;{\mathbf{y}}_{0},{\kappa^{2}{\mathbf{I}}})}$, which act as two approximate distributions for the HR image and the LR image, respectively. By constructing the Markov chain in such a thoughtful way, it is possible to handle the SR task by inversely sampling from it given the LR image ${\mathbf{y}}_{0}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model Design", "weight": 1.0} -->

Based on Eq., we simplify the objective function in Eq. as follows, where $w_{t} = \frac{\alpha_{t}}{2\kappa^{2}\eta_{t}\eta_{t - 1}}$. In practice, we empirically find that the omission of weight $w_{t}$ results in an evident improvement in performance, which aligns with the conclusion in Ho et al..

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model Design", "weight": 1.0} -->

Extension to Latent Space. To alleviate the computational overhead in training, we move the aforementioned model into the latent space of VQGAN, where the original image is compressed by a factor of four in spatial dimensions. This does not require any modifications on our model other than substituting ${\mathbf{x}}_{\mathbf{0}}$ and ${\mathbf{y}}_{0}$ with their latent codes. An intuitive illustration is shown in Fig. 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Noise Schedule", "weight": 1.0} -->

The proposed method employs a hyper-parameter $\kappa$ and a shifting sequence ${\{\eta_{t}\}}_{t = 1}^{T}$ to determine the noise schedule in the diffusion process. Specifically, the hyper-parameter $\kappa$ regulates the overall noise intensity during the transition, and its impact on performance is empirically discussed in Sec. 4.2. The subsequent exposition mainly revolves around the construction of the shifting sequence ${\{\eta_{t}\}}_{t = 1}^{T}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Noise Schedule", "weight": 1.0} -->

Combining with the additional constraint of $\eta_{1}\rightarrow 0$, we set $\eta_{1}$ to be the minimum value between ${({0.04/\kappa})}^{2}$ and $0.001$. For the final step $T$, we set $\eta_{T}$ as 0.999 ensuring $\eta_{T}\rightarrow 1$. For the intermediate timesteps, i.e., $t \in {\lbrack 2,{T - 1}\rbrack}$, we propose a non-uniform geometric schedule for $\sqrt{\eta_{t}}$ as follows: Note that the choice of $\beta_{t}$ and $b_{0}$ is based on the assumption of $\beta_{1} = 0$, $\beta_{T} = {T - 1}$, and $\sqrt{\eta_{T}} = {\sqrt{\eta_{1}} \times b_{0}^{T - 1}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Noise Schedule", "weight": 1.0} -->

The hyper-parameter $p$ controls the growth rate of $\sqrt{\eta_{t}}$ as shown in Fig. 3(h).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Noise Schedule", "weight": 1.0} -->

The proposed noise schedule exhibits high flexibility in three key aspects. First, for small values of $\kappa$, the final state ${\mathbf{x}}_{T}$ converges to a perturbation around the LR image as depicted in Fig. 3(c)-(d). Compared to the corruption ended at Gaussian noise, this design considerably shortens the length of the Markov chain, thereby improving the inference efficiency. Second, the hyper-parameter $p$ provides precise control over the shifting speed, enabling a fidelity-realism trade-off in the SR results as analyzed in Sec. 4.2. Third, by setting $\kappa = 40$ and $p = 0.8$, our method achieves a diffusion process remarkably similar to LDM. This is clearly demonstrated by the visual results during the diffusion process presented in Fig. 3(e)-(f), and further supported by the comparisons on the relative noise strength as shown in Fig. 3(g).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section presents an empirical analysis of the proposed ResShift and provides extensive experimental results to verify its effectiveness on one synthetic dataset and three real-world datasets. Following, our investigation specifically focuses on the more challenging $\times 4$ SR task. Due to page limitation, some experimental results are put in the Appendix B.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Training Details. HR images with a resolution of $256 \times 256$ in our training data are randomly cropped from the training set of ImageNet following LDM. We synthesize the LR images using the degradation pipeline of RealESRGAN. The Adam algorithm with the default settings of PyTorch and a mini-batch size of 64 is used to train ResShift. During training, we use a fixed learning rate of $5\text{e-}5$ and update the weight parameters for 500K iterations. As for the network architecture, we employ the UNet structure in DDPM. To increase the robustness of ResShift to arbitrary image resolution, we replace the self-attention layer in UNet with the Swin Transformer block.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Testing Datasets. We synthesize a testing dataset that contains 3000 images randomly selected from the validation set of ImageNet based on the commonly-used degradation model, i.e., ${\mathbf{y}} = {({{\mathbf{x}} \ast {\mathbf{k}}})} \downarrow {+ {\mathbf{n}}}$, where $k$ is the blurring kernel, $n$ is the noise, $\mathbf{y}$ and $\mathbf{x}$ denote the LR image and HR image, respectively. To comprehensively evaluate the performance of ResShift, we consider more complicated types of blurring kernels, downsampling operators, and noise types. The detailed settings on them can be found in Appendix B.1. It should be noted that we selected the HR images from ImageNet instead of the prevailing datasets in SR such as Set5 and Urban100. The rationale behind this setting is rooted in the fact that these datasets only contain very few source images, which fails to thoroughly evaluate the performance of various methods under different degradation types.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We name this dataset as ImageNet-Test for convenience.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Two real-world datasets are adopted to evaluate the efficacy of ResShift. The first is RealSR, containing 100 real images captured by Canon 5D3 and Nikon D810 cameras. Additionally, we collect another real-world dataset named. It comprises 35 LR images widely used in recent literature. The remaining 30 images were obtained from the internet by ourselves.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Compared Methods. We evaluate the effectiveness of ResShift in comparison to seven recent SR methods, namely ESRGAN, RealSR-JPEG, BSRGAN, RealESRGAN, SwinIR, DASR, and LDM. Note that LDM is a diffusion-based method with 1,000 diffusion steps. For a fair comparison, we accelerate LDM to the same number of steps with ResShift using DDIM and denote it as "LDM-A\", where "A\" indicates the number of inference steps. The hyper-parameter $\eta$ in DDIM is set to be 1 as this value yields the most realistic recovered images.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Metrics. The performance of various methods was assessed using five metrics, including PSNR, SSIM, LPIPS, MUSIQ, and CLIPIQA. It is worth noting that the latter two are non-reference metrics specifically designed to assess the realism of images. CLIPIQA, in particular, leverages the CLIP model that is pre-trained on a massive dataset (i.e., Laion400M ) and thus demonstrates strong generalization ability. On the real-world datasets, we mainly rely on CLIPIQA and MUSIQ as evaluation metrics to compare the performance of different methods.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

We analyze the performance of ResShift under different settings on the number of diffusion steps $T$ and the hyper-parameters $p$ in Eq. and $\kappa$ in Eq..

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

Diffusion Steps $T$ and Hyper-parameter $p$. The proposed transition distribution in Eq. significantly reduces the diffusion steps $T$ in the Markov chain. The hyper-parameter $p$ allows for flexible control over the speed of residual shifting during the transition. Table 1 summarizes the performance of ResShift on ImageNet-Test under different configurations of $T$ and $p$. We can see that both of $T$ and $p$ render a trade-off between the fidelity, measured by the reference metrics such as PSNR, SSIM, and LPIPS, and the realism, measured by the non-reference metrics, including CLIPIQA and MUSIQ, of the super-resolved results. Taking $p$ as an example, when it increases, the reference metrics improve while the non-reference metrics deteriorate. Furthermore, the visual comparison in Fig. 4 shows that a large value of $p$ will suppress the model's ability to hallucinate more image details and result in blurry outputs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

Hyper-parameter $\kappa$. Equation reveals that $\kappa$ dominates the noise strength in state ${\mathbf{x}}_{t}$. We report the influence of $\kappa$ to the performance of ResShift in Table 1. Combining with the visualization in Fig. 4, we can find that excessively large or small values of $\kappa$ will smooth the recovered results, regardless of their favorable metrics of PSNR and SSIM. When $\kappa$ is in the range of $\lbrack 1.0,2.0\rbrack$, our method achieves the most realistic quality indicated by CLIPIQA and MUSIQ, which is more desirable in real applications. We thus set $\kappa$ to be $2.0$ in this work.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

Efficiency Comparison. To improve inference efficiency, it is desirable to limit the number of diffusion steps $T$. However, this causes a decrease in the realism of the restored HR images. To compromise, the hyper-parameter $p$ can be set to a relatively small value. Therefore, we set $T = 15$ and $p = 0.3$, and yield our model named ResShift. Table 2 presents the efficiency and performance comparisons of ResShift to the state-of-the-art (SotA) approach LDM and three other GAN-based methodologies on ImageNet-Test dataset. It is evident from the results that the proposed ResShift surpasses LDM in terms of PSNR and LPIPS, and demonstrates a remarkable fourfold enhancement in computational efficiency when compared to LDM-100. Despite showing considerable potential in mitigating the efficiency bottleneck of the diffusion-based SR approaches, ResShift still lags behind current GAN-based methods in speed due to its iterative sampling mechanism.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

Therefore, it remains imperative to explore further optimizations of the proposed method to address this limitation, which we leave in our future work.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

Perception-Distortion Trade-off. There exists a well-known phenomenon called perception-distortion trade-off in the field of SR. In particular, the augmentation of the generative capability of a restoration model, such as elevating the sampling steps for a diffusion-based method or amplifying the weight of the adversarial loss for a GAN-based method, will result in a deterioration in fidelity preservation while concurrently enhancing the authenticity of restored images. That is mainly because the restoration model with powerful generation capability tends to hallucinate more high-frequency image structures, thereby deviating from the underlying ground truth. To facilitate a comprehensive comparison between our ResShift and current SotA diffusion-based method LDM, we plotted the perception-distortion curves of them in Fig. 7, wherein the perception and distortion are measured by LPIPS and mean square-error (MSE), respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Model Analysis", "weight": 1.0} -->

This plot reflects the perception quality and the reconstruction fidelity of ResShift and LDM across varying numbers of diffusion steps, i.e., 10, 15, 20, 30, 40, and 50. As can be observed, the perception-distortion curve of our ResShift consistently resides beneath that of the LDM, indicating its superior capacity in balancing perception and distortion.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation on Synthetic Data", "weight": 1.0} -->

We present a comparative analysis of the proposed method with recent SotA approaches on the ImageNet-Test dataset, as summarized in Table 3 and Fig. 5. Based on this evaluation, several significant conclusions can be drawn as follows: i) ResShift exhibits superior or at least comparable performance across all five metrics, affirming the effectiveness and superiority of the proposed method. ii) The notably higher PSNR ans SSIM values attained by ResShift indicate its capacity to better preserve fidelity to ground truth images. This advantage primarily arises from our well-designed diffusion model, which starts from a subtle disturbance of the LR image, rather than the conventional assumption of white Gaussian noise in LDM. iii) Considering the metrics of LPIPS and CLIPIQA, which gauge the perceptual quality and realism of the recovered image, ResShift also demonstrates evident superiority over existing methods. Furthermore, in terms of MUSIQ, our approach achieves comparable performance with recent SotA methods. In summary, the proposed ResShift exhibits remarkable capabilities in generating more realistic results while preserving fidelity. This is of paramount importance for the task of SR.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation on Real-World Data", "weight": 1.0} -->

Table 4 lists the comparative evaluation using CLIPIQA and MUSIQ of various methods on two real-world datasets. Note that CLIPIQA, benefiting from the powerful representative capability inherited from CLIP, performs stably and robustly in assessing the perceptional quality of natural images. The results in Table 4 show that the proposed ResShift evidently surpasses existing methods in CLIPIQA, meaning that the restored outputs of ResShift better align with human visual and perceptive systems. In the case of MUSIQ evaluation, ResShift achieves the competitive performance when compared to current SotA methods, namely BSRGAN, SwinIR, and RealESRGAN. Collectively, our method shows promising capability in addressing the real-world SR problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluation on Real-World Data", "weight": 1.0} -->

We display four real-world examples in Fig. 6. More examples can be found in Fig. 10 and Fig. 11 of the Appendix. We consider diverse scenarios, including comic, text, face, and natural images to ensure a comprehensive evaluation. A noticeable observation is that ResShift produces more naturalistic image structures, as evidenced by the patterns on the beam in the third example and the eyes of a person in the fourth example. We note that the recovered results of LDM are excessively smooth when compressing the inference steps to match with the proposed ResShift, specifically utilizing 15 steps, largely deviating from the training procedure's 1,000 steps. Even though other GAN-based methods may also succeed in hallucinating plausible structures to some extent, they are often accompanied by obvious artifacts.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have introduced an efficient diffusion model named ResShift for SR. Unlike existing diffusion-based SR methods that require a large number of iterations to achieve satisfactory results, our proposed method constructs a diffusion model with only 15 sampling steps, thereby significantly improving inference efficiency. The core idea is to corrupt the HR image toward the LR image instead of the Gaussian white noise, which can effectively cut off the length of the diffusion model. Extensive experiments on both synthetic and real-world datasets have demonstrated the superiority of our proposed method. We believe that our work will pave the way for the development of more efficient and effective diffusion models to address the SR problem.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgement. This study is supported under the RIE2020 Industry Alignment Fund -- Industry Collaboration Projects (IAF-ICP) Funding Initiative, as well as cash and in-kind contribution from the industry partner(s).
