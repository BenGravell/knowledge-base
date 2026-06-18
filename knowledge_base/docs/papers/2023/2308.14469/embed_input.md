<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization

Topics include Image super-resolution, Real-world super-resolution, Image restoration, Stable diffusion, Diffusion models, Pixel-aware attention, Image stylization, Degradation removal, PASD.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

PASD adds pixel-aware conditioning to Stable Diffusion so that its generative prior can be used for realistic super-resolution without losing local structure. The same conditioning design also lets the method act as a bridge between restoration and stylization by swapping the underlying diffusion model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Diffusion models have demonstrated impressive performance in various image generation, editing, enhancement and translation tasks. In particular, the pre-trained text-to-image stable diffusion models provide a potential solution to the challenging realistic image super-resolution (Real-ISR) and image stylization problems with their strong generative priors. However, the existing methods along this line often fail to keep faithful pixel-wise image structures. If extra skip connections between the encoder and the decoder of a VAE are used to reproduce details, additional training in image space will be required, limiting the application to tasks in latent space such as image stylization. In this work, we propose a pixel-aware stable diffusion (PASD) network to achieve robust Real-ISR and personalized image stylization. Specifically, a pixel-aware cross attention module is introduced to enable diffusion models perceiving image local structures in pixel-wise level, while a degradation removal module is used to extract degradation insensitive features to guide the diffusion process together with image high level information. An adjustable noise schedule is introduced to further improve the image restoration results.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

By simply replacing the base diffusion model with a stylized one, PASD can generate diverse stylized images without collecting pairwise training data, and by shifting the base model with an aesthetic one, PASD can bring old photos back to life. Extensive experiments in a variety of image enhancement and stylization tasks demonstrate the effectiveness of our proposed PASD approach. Our source codes are available .

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Real-world images often suffer from a mixture of complex degradations, such as low resolution, blur, noise, etc., in the acquisition process. While image restoration methods have achieved significant progress, especially in the era of deep learning, they still tend to generate over-smoothed details, partially due to the pursue of image fidelity in the methodology design. By relaxing the constraint on image fidelity, realistic image super-resolution (Real-ISR) aims to reproduce perceptually realistic image details from the degraded observation. The generative adversarial networks (GANs) and the adversarial training strategy have been widely used for Real-ISR and achieved promising results. However, GAN-based Real-ISR methods are still limited in reproducing rich and realistic image details and tend to generate unpleasant visual artifacts. Meanwhile, GAN-based methods have also been widely used in various image stylization tasks such as cartoonization and old-photo restoration. For example, Chen *et al*. proposed CartoonGAN to generate cartoon stylization by using unpaired data for training. However, different models need to be trained for different styles. Wan *et al*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

introduced a triplet domain translation network to restore old photos. While achieving promising results, the multi-stage procedure of this method makes it complex to use.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, denoising diffusion probabilistic models (DDPMs) have shown outstanding performance in tasks of image generation, and it has become a strong alternative to GAN due to its powerful capability in approximating diverse and complicated distributions. With DDPM, the pre-trained text-to-image (T2I) and text-to-video (T2V) latent diffusion models have been popularly used in numerous downstream tasks, including personalized image generation, image editing, image inpainting and conditional image synthesis. Diffusion models have also been adopted to solve image restoration tasks. A denoising diffusion restoration model (DDRM) is proposed to solve inverse problem by taking advantage of a pre-trained denoising diffusion generative model. However, DDRM assumes a linear image degradation model, limiting its application to more practical scenarios such as Real-ISR. Considering that the pre-trained T2I models such as Stable Diffusion (SD) can generate high-quality natural images, Zhang and Agrawala proposed ControlNet, which enables conditional inputs like edge maps, segmentation maps, etc., and demonstrated that the generative diffusion priors are also powerful in conditional image synthesis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, ControlNet is not suitable for pixel-wise conditional control. Qin *et al*. extended ControlNet by introducing UniControl to enable more diverse visual conditions. Liu *et al*. and Wang *et al*. demonstrated that pre-trained SD priors can be employed for image colorization and Real-ISR, respectively. However, they resorted to a skipped connection to pass pixel-level details for image restoration, requiring extra training in image space and limiting the model capability to tasks performed in latent space such as image stylization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we aim to develop a flexible model to achieve Real-ISR and personalized stylization by using pre-trained T2I models such as SD, targeting at reconstructing photo-realistic pixel-level structures and textures. Our idea is to introduce pixel-aware conditional control into the diffusion process so that robust and perceptually realistic outputs can be achieved. To this end, we present a pixel-aware cross attention (PACA) module to perceive pixel-level information without using any skipped connections. A degradation removal module is employed to reduce the impact of unknown image degradations, alleviating the burden of diffusion module to handle real-world low-quality images. We also demonstrate that the high-level classification/detection/captioning information extracted from the input image can further boost the Real-ISR performance. Inspired by recent works, we present an adjustable noise schedule to further boost the performance of Real-ISR and image stylization tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, the proposed method, namely pixel-aware stable diffusion (PASD), can perform personalized stylization tasks (*e.g*., caroonization and old photo restoration) by simply shifting the base model to a personalized one. Extensive experiments demonstrate the effectiveness and flexibility of PASD.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Pixel-Aware Stable Diffusion Network", "weight": 1.0} -->

Our method is based on generative diffusion priors. In particular, we utilize the powerful pre-trained SD model, while alternative diffusion models such as DALLE2 and Imagen can also be adopted. The architecture of our pixel-aware stable diffusion (PASD) network is depicted in Fig.. One can see that in addition to the pre-trained SD model, PASD has four main modules: a degradation removal module to extract degradation insensitive low-level control features, a high-level information extraction module to extract semantic control features, an adjustable noise schedule (ANS) and a pixel-aware cross-attention (PACA) module to perform pixel-level guidance for diffusion. In addition to the Real-ISR task, our PASD can be readily used for personalized stylization by simply switching the base diffusion model to a personalized one.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Degradation Removal Module", "weight": 1.0} -->

Real-world LQ images usually suffer from complex and unknown degradations. We thus employ a degradation removal module to reduce the impact of degradations and extract "clean" features from the LQ image to control the diffusion process. As shown in Fig., we adopt a pyramid network to extract multi-scale feature maps with 1/2, 1/4 and 1/8 scaled resolutions of the input LQ image. Intuitively, it is anticipated that these features can be used to approximate the HQ image at the corresponding scale as close as possible so that the subsequent diffusion module could focus on recovering realistic image details, alleviating the burden of distinguishing image degradations. Therefore, we introduce an intermediate supervision by employing a convolution layer "toRGB" to turn every single-scale feature maps into the HQ RGB image space.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Degradation Removal Module", "weight": 1.0} -->

We apply an $L_{1}$ loss on each resolution scale to force the reconstruction at that scale to be close to the pyramid decomposition of the HQ image: $\mathcal{L}_{\mathcal{D}\mathcal{R}} = {\sum_{s}{\|{\mathbf{I}_{hq}^{s} - \mathbf{I}_{sr}^{s}}\|}_{1}}$, where $\mathbf{I}_{hq}^{s}$ and $\mathbf{I}_{sr}^{s}$ represent the HQ ground-truth and ISR output at scale $s$. Note that this module is only required in the Real-ISR task.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Pixel-Aware Cross Attention (PACA)", "weight": 1.0} -->

The main challenge of utilizing pre-trained T2I diffusion priors for image restoration tasks lies in how to enable the diffusion process be aware of image details and textures in pixel-level. The well-known ControlNet can support task-specific conditions (*e.g*., edges, segmentation masks) well but fail for pixel-level control.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Pixel-Aware Cross Attention (PACA)", "weight": 1.0} -->

where $\overset{\sim}{\mathbf{x}}$ is the output feature map. The zero convolution is easy-to-implement. However, simply adding the feature maps from the two networks may fail to pass pixel-level precise information, leading to structure inconsistency between the input LQ and output HQ images. Fig. shows an example. One can see that by simply applying ControlNet to the LQ input, there are obvious structure inconsistencies in the output image by ControlNet.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Pixel-Aware Cross Attention (PACA)", "weight": 1.0} -->

To address this problem, some methods employ a skipped connection outside the U-Net to add image details. However, this introduces additional training in image feature domain, and limits the application of the trained network to tasks performed in latent space (*e.g*., image stylization). In this work, we introduce a simple pixel-aware cross attention (PACA) to solve this issue. We reshape $\mathbf{x}$ and $\mathbf{y}$ to $\mathbf{x}^{\prime} \in {\mathbb{R}}^{{h \ast w} \times c}$ and $\mathbf{y}^{\prime} \in {\mathbb{R}}^{{h \ast w} \times c}$, and consider $\mathbf{y}^{\prime}$ as the context input.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Pixel-Aware Cross Attention (PACA)", "weight": 1.0} -->

The conditional feature input $\mathbf{y}^{\prime}$ is of length $h \ast w$, which equals to the total number of pixels of latent feature $\mathbf{x}$. Since feature $\mathbf{y}^{\prime}$ has not been converted into the latent space by the Encoder, it preserves well the original image structures. Therefore, our PASD model can manage to perceive pixel-wise information from the conditional input $\mathbf{y}^{\prime}$ via PACA. As can be seen in the experimental result section, with the help of PACA, the output of our PASD network can reproduce realistic and faithful image structures and textures in pixel-level.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Adjustable Noise Schedule (ANS)", "weight": 1.0} -->

As discussed in previous works, the noise schedule used in SD suffers train-test discrepancy. In training, the noise schedule leaves some residual signal even at the terminal diffusion timestep $N$, leading to non-zero signal-to-noise ratio (SNR). This weakens the model performance at test time when we sample from random Gaussian noise without the signal information. To address this issue, we propose an adjustable noise schedule (ANS) by introducing signal information from the input image at test time.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Adjustable Noise Schedule (ANS)", "weight": 1.0} -->

The residual signals at training stage are from the HQ ground-truth data, which are unavailable at test time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Adjustable Noise Schedule (ANS)", "weight": 1.0} -->

where $\mathbf{z}_{N}$, $\mathbf{z}_{LR}$, ${\overline{\alpha}}_{N}$, $\mathbf{z}$ are respectively the latent input at timestep $N$, the LQ latent, the cumulative product of $\alpha$, and the initial random Gaussian noise. This remedy can partially alleviate the discrepancy issue and has been adopted. However, the train-test discrepancy still exists due to the different origins of residual signals, which can harm the restoration results when the LQ image suffers from severe degradations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Adjustable Noise Schedule (ANS)", "weight": 1.0} -->

In this way, by choosing a proper value of ${\overline{\alpha}}_{a}$, we can adjust the strength of the residual signal $\mathbf{z}_{LR}$ to enable flexible perception-fidelity trade-off.

<!-- chunk {"id": "body-0022", "role": "body", "section": "High-Level Information", "weight": 1.0} -->

Our method is based on the pre-trained SD model where text is used as the input, while in tasks such as Real-ISR, the LQ image is available as the input. Though some SD-based Real-ISR methods adopt the null-text prompt, it has been demonstrated that content-related captions could improve the synthesis results. As shown in Fig., we employ the pre-trained ResNet, YOLO and BLIP networks to extract image classification, object detection and image caption information from the LQ input, and employ the CLIP encoder to convert the text information into image-level features, providing additional semantic signal to control the diffusion process.

<!-- chunk {"id": "body-0023", "role": "body", "section": "High-Level Information", "weight": 1.0} -->

The unconditional $\epsilon$-prediction $\epsilon{(\mathbf{z}_{t},\mathbf{c}_{neg})}$ can be achieved with negative prompts. In practice, we empirically combine words like "noisy", "blurry", "low resolution" as negative prompts, which play a key role to trade off mode coverage and sample quality during inference. It is optional but could boost much the Real-ISR performance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Application to Personalized Stylization", "weight": 1.0} -->

Personalized stylization. Thanks to the open source of SD and the recently developed techniques such as DreamBooth and LORA, the community becomes highly prosperous. Contributors can upload a large amount of personalized models finetuned on SD with self-collected data. Since PASD is based on pretrained SD model and the pretrained weights are frozen during model training, it is easy to replace the base model with personalized ones at test time so that PASD can re-target the output domain and produce stylized results.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Application to Personalized Stylization", "weight": 1.0} -->

Unlike previous methods that achieve stylization ability by learning a pixel-to-pixel mapping function using adversarial training, our PASD approach decouples stylization generation and pixel-to-pixel mapping, opening a new door for image stylization. By fine-tuning personalized SD models with a batch of style images or downloading different personalized models from online communities ^11^1 one can easily generate various stylized results with our PASD method. In this paper, we use cartoonization as a typical stylization task in experiments.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Application to Personalized Stylization", "weight": 1.0} -->

Old photo restoration. Apart from cartoonization, another popular family of personalized models are the aesthetic ones, *i.e*., those trained on images with a particular aesthetic taste. One typical task of this kind is old photo restoration. By replacing the base model with an aesthetic one, PASD can improve the quality and aesthetics of the input old photo image simultaneously, as will be demonstrated in our experiments.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

In the model training, we first obtain the latent representation $\mathbf{z}_{0}$ of an HQ image, and progressively add noise to it to yield a noisy latent $\mathbf{z}_{t}$, where $t$ is a randomly sampled diffusion step. Given a number of conditions such as diffusion step $t$, LQ input $\mathbf{I}_{lq}$ and text prompt $\mathbf{c}$, we learn a PASD network $\epsilon_{\theta}$ to predict the noise added to the noisy latent $\mathbf{z}_{t}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

During the training of Real-ISR models, we jointly update the degradation removal module. The total loss is $\mathcal{L} = {\mathcal{L}_{{\mathcal{D}\mathcal{F}} - \epsilon} + {\gamma\mathcal{L}_{\mathcal{D}\mathcal{R}}}}$, where $\gamma$ is a balancing parameter. We simply set $\gamma = 1$ in the experiments. We freeze all the parameters in pre-trained SD, and only train the newly added modules, including the degradation removal module, ControlNet and PACA. The employed ResNet, YOLO and BLIP and CLIP networks for high-level information extraction are also fixed. During training, we randomly replace $50\%$ of the text prompts with null-text prompts. This encourages our PASD model to perceive semantic contents from input LQ images as a replacement of text prompts.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

We adopt the Adam optimizer to train PASD with a batch size of $4$. The learning rate is fixed as $5 \times 10^{- 5}$. The model is updated for $500K$ iterations with $8$ NVIDIA Tesla 32G-V100 GPUs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Training and testing datasets. For the Real-ISR task, we train PASD on DIV2K, Flickr2K, OST, and the first $10,000$ face images from FFHQ. We employ the degradation pipeline of Real-ESRGAN to synthesize LQ-HQ training pairs. We evaluate our approach on both synthetic and real-world datasets. The synthetic dataset is generated from the DIV2K validation set following the Real-ESRGAN degradation pipeline. For real-world test dataset, we use the RealSR and DRealSR for evaluation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

For the task of cartoonization, we simply reuse the PASD model trained for Real-ISR task and shift the base model with stylized ones obtained from online communities. We conduct comparisons on the first $100$ face images from FFHQ as well as the first $100$ images from Flicker2K.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

For the task of old photo restoration, we also adopt the pre-trained PASD model in the task of Real-ISR. Unlike cartoonization, we replace the base model with aesthetic ones. We collect $100$ old photos from Internet for testing.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Evaluation metrics. For quantitative evaluation of Real-ISR models, we employ the widely used perceptual metrics, including FID, LPIPS, DISTS, NIQE, MUSIQ and QAlign, to compare the competing Real-ISR models. The PSN and SSIM indices (evaluated on the Y channel in YCbCr space) are also reported for reference only because they are not suitable to evaluate generative models. For the tasks of cartoonization and old photo restoration, we employ FID, MUSIQ and QAlign for evaluation since the ground-truth images are unavailable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

In addition, for all tasks we invite $15$ volunteers to conduct a user study on $40$ real-world images. Each volunteer is asked to choose the most preferred one among the outputs of all competing methods, which are presented to the volunteers in random order.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Effectiveness of the Adjustable Noise Schedule", "weight": 1.0} -->

We first use the task of Real-ISR to discuss the setting and advantages of our proposed ANS. In order to find out how ${\overline{\alpha}}_{a}$ affects the performance, we set ${\overline{\alpha}}_{a} \in {\{ 0,0.1,0.5,1\}}$) and perform experiments on the RealSR test dataset. The curves of PSNR/QAlign versus ${\overline{\alpha}}_{a}$ are plotted in Fig.. One can see that the PSNR performance increases while the QAlign score decreases as ${\overline{\alpha}}_{a}$ grows, demonstrating that the proposed ${\overline{\alpha}}_{a}$ can be employed to enable flexible perception-fidelity trade-off. Fig. visualizes Real-ISR results with different values of ${\overline{\alpha}}_{a}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Effectiveness of the Adjustable Noise Schedule", "weight": 1.0} -->

We can see that with the increase of ${\overline{\alpha}}_{a}$, PASD tends to improve the fidelity while generate less realistic details. In practice, we choose ${\overline{\alpha}}_{a}$ from the values of ${\overline{\alpha}}_{n}$, where $n \in {\{ 1,{2\ldots N}\}}$, for convenience. In all of our following experiments, we empirically set $n = 900$, *i.e*., ${\overline{\alpha}}_{900} = 0.1189$, to achieve a good balance between fidelity and perception quality.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Realistic image super-resolution. We compare the proposed PASD method with two categories of Real-ISR algorithms. The first category is GAN-based methods, including Real-ESRGAN, FeMaSR, and SwinIR. The second category is diffusion-based models, including ResShift, StableSR, DiffBIR, and SeeSR. The quantitative evaluation results on the test data are presented in Tab., from which we can have the following observations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

First, in term of fidelity measures PSNR/SSIM, the diffusion-based methods are not advantageous over GAN-based methods. This is because diffusion models have higher generative capability and hence may synthesize more perceptually realistic but less faithful details, resulting in lower PSNR/SSIM indices. Second, the diffusion-based methods, especially the proposed PASD, perform better than GAN-based methods in most perception metrics. This conforms to our observation on the visual quality of their Real-ISR output. Third, PASD achieves the best QAlign scores, which is a no-reference image quality assessment index based on large vision-language models, on all the three test datasets.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Fig. visualizes the Real-ISR results of competing methods. It can be seen that our PASD method can generate more realistic details with better visual quality (see the synthesized textures in fur, flowers, leaves, feathers, sea, etc.). Fig. 6(a) ‣ Figure 6 ‣ 4.1 Experiment Setup ‣ 4 Experiments ‣ Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization") presents the results of subjective user study. PASD receives the most rank-1 votes, confirming its superiority in generating realistic image details. More visual results can be found in the supplementary material.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Personalized cartoonization. Similar to the Real-ISR task, we compare the proposed PASD with two categories of stylization algorithms. The first category is GAN-based methods, including CartoonGAN, AnimeGAN and DCTNet. We re-train these models with a batch of stylized images generated by a personalized diffusion model, *i.e*., ToonYou ^22^2 The second category is diffusion-based algorithms, including InstructPix2Pix, SD img2img and ControlNet. We replace their base models with the personalized model for fair comparison. Tab. shows the quantitative evaluation results. It can be seen that PASD achieves the best or second best results in most indices.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Fig. shows some cartoonization results. One can see that compared with GAN-based methods, the results of PASD is much cleaner. Compared with the diffusion-based models, PASD can better preserve image details such as human hair. Due to the limited space, we only present results with the style of ToonYou here. Please note that PASD can generate various stylization results by simply switching the base diffusion model to a personalized one without any additional training procedure. More stylization results, including the results on image colorization, can be found in the supplementary materials.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

As in the task of Real-ISR, we also conducted a user study for subjective assessment on the image stylization performance. Fig. 6(b) ‣ Figure 6 ‣ 4.1 Experiment Setup ‣ 4 Experiments ‣ Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization") shows the results. Clearly, PASD is preferred by most subjects.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Old photo restoration. We compare PASD with Wan *et al*. and several real-world SR methods, including RealESRGAN, FeMaSR, SwinIR, StableSR, and DiffBIR. We re-use the PASD model trained for Real-ISR task but replace its base model with an aesthetic one,*i.e*. majicMIX realistic ^33^3

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Tab. shows the quantitative evaluation results. It can be seen that PASD achieves the best results in all three indices. Fig. visualizes some old photo restoration results. Compared with the competing methods, PASD can better recover vivid image details such as human hair. Fig. 6(c) ‣ Figure 6 ‣ 4.1 Experiment Setup ‣ 4 Experiments ‣ Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization") presents the results of subjective user study. Clearly, PASD is preferred by the majority of subjects. More visual results can be found in the supplementary material.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We perform a series of ablation studies of the proposed PASD network, including the importance of PACA, the role of degradation removal module, and the role of high-level information. We visualize the Real-ISR results of different variants of PASD in Fig., and report the quantitative results and runtime in Tab..

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Importance of PACA. We evaluate a variant of PASD by excluding the PACA module from it, *i.e*., the features $\mathbf{y}$ extracted from ControlNet are simply added to features $\mathbf{x}$. As shown in Fig. (b), the output becomes inconsistent with the LQ input in colors and structures, etc. This verifies the importance of PACA in perceiving pixel-wise local structures.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Role of degradation removal module. To evaluate the effect of degradation removal module, we remove the "toRGB" modules as well as the pyramid $\mathcal{L}_{DR}$ loss during model training. As can be seen in Fig. (c) and Tab., removing the degradation removal module leads to dirty outputs and worse PSNR, FID and LPIPS indices.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Role of high-level information. The high-level information and negative prompt are optional but very useful for PASD. We simply replace them with null-text prompt to evaluate their effects. As shown in Fig. (d), replacing both high-level information and negative prompt with null-text prompt results in dirty outputs with less realistic details, which is also verified by the worse FID and LPIPS indices in Tab.. Abandoning high-level information leads to over-smoothed results, as illustrated in Fig. (e). The output can become dirty without negative prompt (see Fig. (f)). Our full model takes advantages of both high-level information and negative prompt, and achieves a good balance between clean-smooth and detailed-dirty outputs (see Fig. (g) and the best FID score in Tab. ).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Runtime analysis on different modules. The runtime is reported as the average over $10$ runs to process a $256 \times 256$ image on a NVIDIA Tesla 32G-V100 GPU. We use the DDIM sampler for $20$ steps. By comparing Exps. (a) and (e) in Tab., one can see that the degradation removal module has little effect on the runtime. Without the negative prompt module, the runtime nearly cuts in half because the classifier-free guidance can be removed (see Exps.(c) and (e)). Finally, the high-level information module only increase a little the runtime (see Exps.(d) and (e)).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

We proposed a pixel-aware diffusion network, namely PASD, for realistic image restoration and personalized stylization. By introducing a pixel-aware cross attention module, PASD succeeded in perceiving image local structures in pixel-level and achieved robust and perceptually realistic Real-ISR results. An adjustable noise schedule was also proposed, which helped PASD to achieve flexible perception-fidelity trade-off during the inference stage. By replacing the base model to a personalized one, PASD could produce diverse stylization results with highly consistent semantic contents with the input. The proposed PASD was simple to implement, and our extensive experiments demonstrated its effectiveness and flexibility across different tasks, showing its great potentials for handling complex image restoration and stylization tasks.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

Though PASD can achieve pixel-level enhancement, it still suffers from the balance between fidelity and perception. In addition, it may fail to reproduce faithful details when the input image is heavily degraded or the semantic information is inaccurate. A more robust degradation estimation module can be designed, and more precise semantic information can be extracted to further improve the performance of PASD, which will be considered in our future work.
