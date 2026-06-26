<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Hierarchical Text-Conditional Image Generation with CLIP Latents

Topics include Robustness, Diffusion models, Image generation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Contrastive models like CLIP have been shown to learn robust representations of images that capture both semantics and style. To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding. We show that explicitly generating image representations improves image diversity with minimal loss in photorealism and caption similarity. Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation. Moreover, the joint embedding space of CLIP enables language-guided image manipulations in a zero-shot fashion. We use diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress in computer vision has been driven by scaling models on large datasets of captioned images collected from the internet Desai and Johnson; Sariyildiz et al.; Zhang et al.; Radford et al.; Mu et al.; Fürst et al.. Within this framework, CLIP Radford et al. has emerged as a successful representation learner for images. CLIP embeddings have a number of desirable properties: they are robust to image distribution shift, have impressive zero-shot capabilities, and have been fine-tuned to achieve state-of-the-art results on a wide variety of vision and language tasks Shen et al.. Concurrently, diffusion models Sohl-Dickstein et al.; Song and Ermon; Ho et al. have emerged as a promising generative modeling framework, pushing the state-of-the-art on image and video generation tasks Dhariwal and Nichol; Ho et al.; Ho and Salimans. To achieve best results, diffusion models leverage a guidance technique Dhariwal and Nichol; Ho and Salimans which improves sample fidelity (for images, photorealism) at the cost of sample diversity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we combine these two approaches for the problem of text-conditional image generation. We first train a diffusion decoder to invert the CLIP image encoder. Our inverter is non-deterministic, and can produce multiple images corresponding to a given image embedding. The presence of an encoder and its approximate inverse (the decoder) allows for capabilities beyond text-to-image translation. As in GAN inversion Zhu et al.; Xia et al., encoding and decoding an input image produces semantically similar output images (Figure 3). We can also interpolate between input images by inverting interpolations of their image embeddings (Figure 4).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, one notable advantage of using the CLIP latent space is the ability to semantically modify images by moving in the direction of any encoded text vector (Figure 5), whereas discovering these directions in GAN latent space involves vibrant portrait painting of Salvador Dalí with a robotic half face a shiba inu wearing a beret and black turtleneck a close up of a handpalm with leaves growing from it an espresso machine that makes coffee from human souls, artstation panda mad scientist mixing sparkling chemicals, artstation a corgi’s head depicted as an explosion of a nebula a dolphin in an astronaut suit on saturn, artstation a propaganda poster depicting a cat dressed as french emperor napoleon holding a piece of cheese a teddy bear on a skateboard in times square Figure 1: Selected 1024 × 1024 samples from a production version of our model. luck and diligent manual examination. Furthermore, encoding and decoding images also provides us with a tool for observing which features of the image are recognized or disregarded by CLIP.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To obtain a full generative model of images, we combine the CLIP image embedding decoder with a prior model, which generates possible CLIP image embeddings from a given text caption. We compare our text-to-image system with other systems such as DALL-E Ramesh et al. and GLIDE Nichol et al., finding that our samples are comparable in quality to GLIDE, but with greater diversity in our generations. We also develop methods for training diffusion priors in latent space, and show that they achieve comparable performance to autoregressive priors, while being more compute-efficient. We refer to our full text-conditional image generation stack as unCLIP, since it generates images by inverting the CLIP image encoder.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Method", "weight": 1.0} -->

Our training dataset consists of pairs $(x,y)$ of images $x$ and their corresponding captions $y$. Given an image $x$, let $z_{i}$ and $z_{t}$ be its CLIP image and text embeddings, respectively. We design our generative stack to produce images from captions using two components: A prior $P{(\left. z_{i} \middle| y \right.)}$ that produces CLIP image embeddings $z_{i}$ conditioned on captions $y$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Method", "weight": 1.0} -->

A decoder $P{(\left. x \middle| {z_{i},y} \right.)}$ that produces images $x$ conditioned on CLIP image embeddings $z_{i}$ (and optionally text captions $y$).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Method", "weight": 1.0} -->

The decoder allows us to invert images given their CLIP image embeddings, while the prior allows us to learn a generative model of the image embeddings themselves. Stacking these two components yields a generative model $P{(\left. x \middle| y \right.)}$ of images $x$ given captions $y$: The first equality holds because $z_{i}$ is a deterministic function of $x$. The second equality holds because of the chain rule. Thus, we can sample from the true conditional distribution $P{(\left. x \middle| y \right.)}$ by first sampling $z_{i}$ using the prior, and then sampling $x$ using the decoder. In the following sections, we describe our decoder and prior stacks. For training details and hyperparameters, refer to Appendix C.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Decoder", "weight": 1.0} -->

We use diffusion models Ho et al.; Song and Ermon to produce images conditioned on CLIP image embeddings (and optionally text captions). Specifically, we modify the architecture described in Nichol et al. by projecting and adding CLIP embeddings to the existing timestep embedding, and by projecting CLIP embeddings into four extra tokens of context that are concatenated to the sequence of outputs from the GLIDE text encoder. We retained the text conditioning pathway present in the original GLIDE model, hypothesizing that it could allow the diffusion model to learn aspects of natural language that CLIP fails to capture (e.g. variable binding), but find that it offers little help in this regard (Section 7).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Decoder", "weight": 1.0} -->

While we can sample from the conditional distribution of the decoder directly, past work using diffusion models shows using guidance on the conditioning information Dhariwal and Nichol; Ho and Salimans; Nichol et al. improves sample quality a lot. We enable classifier-free guidance Ho and Salimans by randomly setting the CLIP embeddings to zero (or a learned embedding) 10% of the time, and randomly dropping the text caption 50% of the time during training.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Decoder", "weight": 1.0} -->

To generate high resolution images, we train two diffusion upsampler models Nichol and Dhariwal; Saharia et al.: one to upsample images from $64 \times 64$ to $256 \times 256$ resolution, and another to further upsample those to $1024 \times 1024$ resolution. To improve the robustness of our upsamplers, we slightly corrupt the conditioning images during training. For the first upsampling stage, we use gaussian blur Saharia et al., and for the second, we use a more diverse BSR degradation Rombach et al.; Zhang et al.. To reduce training compute and improve numerical stability, we follow Rombach et al. and train on random crops of images that are one-fourth the target size. We use only spatial convolutions in the model (i.e., no attention layers) and at inference time directly apply the model at the target resolution, observing that it readily generalizes to the higher resolution. We found no benefit from conditioning the upsamplers on the caption, and use unconditional ADMNets Dhariwal and Nichol with no guidance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Prior", "weight": 1.0} -->

While a decoder can invert CLIP image embeddings $z_{i}$ to produce images $x$, we need a prior model that produces $z_{i}$ from captions $y$ to enable image generations from text captions. We explore two different model classes for the prior model: Autoregressive (AR) prior: the CLIP image embedding $z_{i}$ is converted into a sequence of discrete codes and predicted autoregressively conditioned on the caption $y$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Prior", "weight": 1.0} -->

Diffusion prior: The continuous vector $z_{i}$ is directly modelled using a Gaussian diffusion model conditioned on the caption $y$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Prior", "weight": 1.0} -->

In addition to the caption, we can condition the prior on the CLIP text embedding $z_{t}$ since it is a deterministic function of the caption. To improve sample quality we also enable sampling using classifier-free guidance for both the AR and diffusion prior, by randomly dropping this text conditioning information 10% of the time during training.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Prior", "weight": 1.0} -->

To train and sample from the AR prior more efficiently, we first reduce the dimensionality of the CLIP image embeddings $z_{i}$ by applying Principal Component Analysis (PCA) Pearson. In particular, we find that the rank of the CLIP representation space is drastically reduced when training CLIP with SAM Foret et al. while slightly improving evaluation metrics. We are able to preserve nearly all of the information^11^1I.e., less than 1% average mean-squared error in reconstructing the image representations. by retaining only 319 principal components out of the original 1,024. After applying PCA, we order the principal components by decreasing eigenvalue magnitude, quantize each of the 319 dimensions into 1,024 discrete buckets, and predict the resulting sequence using a Transformer Vaswani et al. model with a causal attention mask. This results in a threefold reduction in the number of tokens predicted during inference, and improves training stability.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Prior", "weight": 1.0} -->

We condition the AR prior on the text caption and the CLIP text embedding by encoding them as a prefix to the sequence. Additionally, we prepend a token indicating the (quantized) dot product between the text embedding and image embedding, $z_{i} \cdot z_{t}$. This allows us to condition the model on a higher dot product, since higher text-image dot products correspond to captions which better describe the image. In practice, we find it beneficial to sample the dot product from the top half of the distribution.^22^2We swept over percentiles 50%, 70%, 85%, 95% and found 50% to be optimal in all experiments.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Prior", "weight": 1.0} -->

For the diffusion prior, we train a decoder-only Transformer with a causal attention mask on a sequence consisting of, in order: the encoded text, the CLIP text embedding, an embedding for the diffusion timestep, the noised CLIP image embedding, and a final embedding whose output from the Transformer is used to predict the unnoised CLIP image embedding. We choose not to condition the diffusion prior on $z_{i} \cdot z_{t}$ like in the AR prior; instead, we improve quality during sampling time by generating two samples of $z_{i}$ and selecting the one with a higher dot product with $z_{t}$. Instead of using the $\epsilon$-prediction formulation from Ho et al.,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Image Manipulations", "weight": 1.0} -->

Our approach allows us to encode any given image $x$ into a bipartite latent representation $(z_{i},x_{T})$ that is sufficient for the decoder to produce an accurate reconstruction. The latent $z_{i}$ describes the aspects of the image that are recognized by CLIP, while the latent $x_{T}$ encodes all of the residual information necessary for the decoder to reconstruct $x$. The former is obtained by simply encoding the image with the CLIP image encoder. The latter is obtained by applying DDIM inversion (Appendix F in Dhariwal and Nichol ) to $x$ using the decoder, while conditioning on $z_{i}$. We describe three different kinds of manipulations that are enabled by this bipartite representation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Variations", "weight": 1.0} -->

Given an image $x$, we can produce related images that share the same essential content but vary in other apects, such as shape and orientation (Figure 3). To do this, we apply the decoder to the bipartite representation $(z_{i},x_{T})$ using DDIM with $\eta > 0$ for sampling. With $\eta = 0$, the decoder becomes deterministic and will reconstruct the given image $x$. Larger values of $\eta$ introduce stochasticity into successive sampling steps, resulting in variations that are perceptually "centered" around the original image $x$. As $\eta$ increases, these variations tell us what information was captured in the CLIP image embedding (and thus is preserved across samples), and what was lost (and thus changes across the samples).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Interpolations", "weight": 1.0} -->

It is also possible to blend two images $x_{1}$ and $x_{2}$ for variations (Figure 4), traversing all of the concepts in CLIP's embedding space that occur between them. To do this, we rotate between their CLIP embeddings $z_{i_{1}}$ and $z_{i_{2}}$ using spherical interpolation, yielding intermediate CLIP representations $z_{i_{\theta}} = {\text{slerp}{(z_{i_{1}},z_{i_{2}},\theta)}}$ as $\theta$ is varied from 0 to 1. There are two options for producing the intermediate DDIM latents along the trajectory.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Interpolations", "weight": 1.0} -->

The first option involves interpolating between their DDIM inverted latents $x_{T_{1}}$ and $x_{T_{2}}$ (by setting $x_{T_{\theta}} = {\text{slerp}{(x_{T_{1}},x_{T_{2}},\theta)}}$), which yields a single trajectory whose endpoints reconstruct $x_{1}$ and $x_{2}$. The second option involves fixing the DDIM latent to a randomly-sampled value for all interpolates in the trajectory. This results in an infinite number of trajectories between $x_{1}$ and $x_{2}$, though the endpoints of these trajectories will generally no longer coincide with the original images. We use this approach in Figure 4.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Interpolations", "weight": 1.0} -->

a photo of a cat → an anime drawing of a super saiyan cat, artstation a photo of a victorian house → a photo of a modern house a photo of an adult lion → a photo of lion cub a photo of a landscape in winter → a photo of a landscape in fall Figure 5: Text diffs applied to images by interpolating between their CLIP image embeddings and a normalised difference of the CLIP text embeddings produced from the two descriptions. We also perform DDIM inversion to perfectly reconstruct the input image in the first column, and fix the decoder DDIM noise across each row.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Text Diffs", "weight": 1.0} -->

A key advantage of using CLIP compared to other models for image representations is that it embeds images and text to the same latent space, thus allowing us to apply language-guided image manipulations (i.e., text diffs), which we show in Figure 5. To modify the image to reflect a new text description $y$, we first obtain its CLIP text embedding $z_{t}$, as well as the CLIP text embedding $z_{t_{0}}$ of a caption describing the current image^33^3Instead of a description of the current image, we also experimented with using a dummy caption like "a photo" for the baseline, or removing it altogether. These also worked well.. We then compute a text diff vector $z_{d} = {\text{norm}{({z_{t} - z_{t_{0}}})}}$ from these by taking their difference and normalizing.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Text Diffs", "weight": 1.0} -->

Now, we can rotate between the image CLIP embedding $z_{i}$ and the text diff vector $z_{d}$ using spherical interpolation, yielding intermediate CLIP representations $z_{\theta} = {\text{slerp}{(z_{i},z_{d},\theta)}}$, where $\theta$ is increased linearly from 0 to a maximum value that is typically in $\lbrack 0.25,0.50\rbrack$. We produce the final outputs by decoding the interpolates $z_{\theta}$, fixing the base DDIM noise to $x_{T}$ throughout the entire trajectory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Text Diffs", "weight": 1.0} -->

Granny Smith: 100% iPod: 0% Pizza: 0% Granny Smith: 0.02% iPod: 99.98% Pizza: 0% Granny Smith: 94.33% iPod: 0% Pizza: 5.66% Figure 6: Variations of images featuring typographic attacks Goh et al. paired with the CLIP model’s predicted probabilities across three labels. Surprisingly, the decoder still recovers Granny Smith apples even when the predicted probability for this label is near 0%. We also find that our CLIP model is slightly less susceptible to the “pizza” attack than the models investigated in Goh et al..

<!-- chunk {"id": "body-0027", "role": "body", "section": "Probing the CLIP Latent Space", "weight": 1.0} -->

Our decoder model provides a unique opportunity to explore CLIP latent space by allowing us to directly visualize what the CLIP image encoder is seeing. As an example use case, we can revisit cases where CLIP makes incorrect predictions, such as typographic attacks Goh et al.. In these adversarial images, a piece of text is overlayed on top of an object, which causes CLIP to predict the object described by the text rather than the object depicted in the image. This piece of text essentially hides the original object in terms of output probabilities. In Figure 6, we show an example of this attack from Goh et al., wherein an apple can be misclassified as an iPod. Surprisingly, we find that our decoder still generates pictures of apples with high probability even though the predicted probability of "Granny Smith" is near zero. Even more notable, the model never produces pictures of iPods, despite the very high relative predicted probability of this caption.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Probing the CLIP Latent Space", "weight": 1.0} -->

PCA reconstructions offer another tool for probing the structure of the CLIP latent space. In Figure 7, we take the CLIP image embeddings of a handful of source images and reconstruct them with progressively more PCA dimensions, and then visualize the reconstructed image embeddings using our decoder with DDIM on a fixed seed. This allows us to see what semantic information the different dimensions encode. We observe that the early PCA dimensions preserve coarse-grained semantic information such as what types of objects are in the scene, whereas the later PCA dimensions encode finer-grained detail such as the shapes and exact form of the objects. For example, in the first scene, the earlier dimensions seem to encode that there is food and perhaps a container present, whereas the later dimensions encode tomatoes and a bottle specifically. Figure 7 also serves as a visualization of what the AR prior is modeling, since the AR prior is trained to explicitly predict these principal components in this order.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Probing the CLIP Latent Space", "weight": 1.0} -->

“A group of baseball players is crowded at the mound.” “an oil painting of a corgi wearing a party hat” “a hedgehog using a calculator” “A motorcycle parked in a parking space next to another motorcycle.” “This wire metal rack holds several pairs of shoes and sandals” Figure 8: Samples using different conditioning signals for the same decoder. In the first row, we pass the text caption to the decoder, and pass a zero vector for the CLIP embedding. In the second row, we pass both the text caption and the CLIP text embedding of the caption. In the third row, we pass the text and a CLIP image embedding generated by an autoregressive prior for the given caption. Note that this decoder is only trained to do the text-to-image generation task (without the CLIP image representation) 5% of the time.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Importance of the Prior", "weight": 1.0} -->

Although we train a prior to generate CLIP image embeddings from captions, the prior is not strictly necessary for caption-to-image generation. For instance, our decoder can condition on both CLIP image embeddings and captions, but the CLIP image embedding is dropped 5% of the time during training in order to enable classifier-free guidance. Therefore, at sampling time, we can condition on only the caption, although this underperforms a model trained fully in this way (this model is GLIDE, and we do a thorough comparison with GLIDE in Sections 5.2 and 5.3). Another possibility is to feed the decoder the CLIP text embedding as if it were an image embedding, as previously observed Zhou et al.; Wang et al.. The first two rows of Figure 8 depicts samples obtained in these two ways; the third row depicts samples obtained with a prior. Conditioning the decoder on just the caption is clearly worst, but conditioning on text embeddings zero-shot does produce reasonable results.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Importance of the Prior", "weight": 1.0} -->

Building on this observation, another approach would be to train the decoder to condition on CLIP text embeddings Crowson instead of CLIP image embeddings (although we would lose the capabilities mentioned in Section 4).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Importance of the Prior", "weight": 1.0} -->

To quantify the effectiveness of these alternate approaches, we train two models: a small decoder conditioned on CLIP text embeddings, and a small unCLIP stack (diffusion prior and decoder). We then compare samples from the text-embedding decoder, samples from the unCLIP stack, and samples obtained from feeding text embeddings to the unCLIP decoder zero-shot, sweeping across guidance scales for all models. We find that these approaches respectively score FIDs of 9.16, 7.99, and 16.55 on a test set, suggesting the unCLIP approach is best. We also run human evaluations comparing the first two settings, sweeping over sampling hyperparameters for each using our human evaluation proxy model (Appendix A). We find that humans prefer the full unCLIP stack 57.0% $\pm$ 3.1% of the time for photorealism and 53.1% $\pm$ 3.1% of the time for caption similarity.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Importance of the Prior", "weight": 1.0} -->

Given the importance of the prior, it is worth evaluating different approaches for training it. We compare both the AR and diffusion priors throughout our experiments. In all cases (Sections 5.2, 5.4, and 5.5), we find that the diffusion prior outperforms the AR prior for comparable model size and reduced training compute.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Human Evaluations", "weight": 1.0} -->

We observe in Figure 1 that unCLIP is capable of synthesizing complex, realistic images. While we can compare sample quality to past models using FID, it is not always aligned with human judgment. To better gauge the generation capabilities of our system, we conduct systematic human evaluations comparing unCLIP to GLIDE for photorealism, caption similarity, and sample diversity.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Human Evaluations", "weight": 1.0} -->

We follow the protocol of Ramesh et al.; Nichol et al. for the first two evaluations: for photorealism, users are presented with pairs of images and must choose which looks more photorealistic; for caption similarity, users are additionally prompted with a caption, and must choose which image better matches the caption. In both evaluations, there is a third "Not sure" option. For diversity, we propose a new evaluation protocol in which humans are presented with two $4 \times 4$ grids of samples and must choose which is more diverse (with a third option, "Not sure"). For this evaluation, we produce sample grids using 1,000 captions from the MS-COCO validation set, and always compare sample grids for the same caption. Before running human comparisons, we swept over sampling hyperparameters for each model using a CLIP linear probe trained to be a proxy for human photorealism evaluations (Appendix A). These hyperparameters are fixed across all three types of evaluation.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Human Evaluations", "weight": 1.0} -->

We present our results in Table 1. In general, the diffusion prior performs better than the AR prior in pairwise comparisons against GLIDE. We find that humans still slightly prefer GLIDE to unCLIP in terms of photorealism, but the gap is very small. Even with similar photorealism, unCLIP is strongly preferred over GLIDE in terms of diversity, highlighting one of its benefits.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Improved Diversity-Fidelity Trade-off with Guidance", "weight": 1.0} -->

Compared to GLIDE, we qualitatively observe that unCLIP is able to generate more diverse images while leveraging the guidance technique to improve sample quality. To understand why, consider Figure 9 where we increase guidance scale for both GLIDE and unCLIP. For GLIDE, the semantics (camera angle, color, size) converge as we increase guidance scale, whereas for unCLIP the semantic information of the scene is frozen in the CLIP image embedding and therefore does not collapse when guiding the decoder.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Improved Diversity-Fidelity Trade-off with Guidance", "weight": 1.0} -->

In Section 5.2, we observed that unCLIP achieves similar photorealism as GLIDE while maintaining more diversity, but that its caption matching capabilities were slightly worse. It is natural to ask whether GLIDE's guidance scale can be lowered to obtain the same diversity level as unCLIP while maintaining better caption matching. In Figure 10, we conduct a more careful study of this question by performing human evaluations across several GLIDE guidance scales. We find that GLIDE at guidance scale 2.0 is very close to the photorealism and caption similarity of unCLIP, while still producing less diverse samples.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improved Diversity-Fidelity Trade-off with Guidance", "weight": 1.0} -->

Finally, in Figure 11 we compute MS-COCO zero-shot FID Heusel et al. while sweeping over guidance scale for both unCLIP and GLIDE, finding that guidance hurts the FID of unCLIP much less so than for GLIDE. In this evaluation, we fix the guidance scale of the unCLIP prior and only vary the guidance scale of the decoder. This is another indication that guidance hurts the diversity of GLIDE much more than unCLIP, since FID heavily penalizes non-diverse generations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Comparison on MS-COCO", "weight": 1.0} -->

Zero-shot FID (filt) unCLIP (Diffusion prior) Table 2: Comparison of FID on MS-COCO 256 × 256. We use guidance scale 1.25 for the decoder for both the AR and diffusion prior, and achieve the best results using the diffusion prior.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison on MS-COCO", "weight": 1.0} -->

In the text-conditional image generation literature, it has become standard practice to evaluate FID on the MS-COCO Lin et al. validation set. We present results on this benchmark in Table 2. Like GLIDE and DALL-E, unCLIP is not directly trained on the MS-COCO training set, but can still generalize to the validation set zero-shot. We find that, compared to these other zero-shot models, unCLIP achieves a new state-of-the-art FID of 10.39 when sampling with the diffusion prior. In Figure 12, we visually compare unCLIP to various recent text-conditional image generation models on several captions from MS-COCO. We find that, like the other methods, unCLIP produces realistic scenes that capture the text prompts.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Aesthetic Quality Comparison", "weight": 1.0} -->

We additionally perform automated aesthetic quality evaluations comparing unCLIP to GLIDE. Our goal with this evaluation is to assess how well each model produces artistic illustrations and photographs. To this end, we generated 512 "artistic" captions using GPT-3 Brown et al. by prompting it with captions for existing artwork (both real and AI generated). Next, we trained a CLIP linear probe to predict human aesthetic judgments using the AVA dataset Murray et al. (Appendix A). For each model and set of sampling hyperparameters, we produce four images for each prompt, and report the mean predicted aesthetic judgment over the full batch of 2048 images.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Aesthetic Quality Comparison", "weight": 1.0} -->

In Figure 13, we present results on our aesthetic quality evaluation. We find that guidance improves aesthetic quality for both GLIDE and unCLIP. For unCLIP, we only guide the decoder (we found that guiding the prior hurt results). We also plot the aesthetic quality against Recall^44^4Recall is computed with respect to the training dataset., since guidance typically induces a trade-off AAAA Real Image AAAA unCLIP (prod.)

<!-- chunk {"id": "body-0044", "role": "body", "section": "Aesthetic Quality Comparison", "weight": 1.0} -->

“a green train is coming down the tracks” “a group of skiers are preparing to ski down a mountain.” “a small kitchen with a low ceiling” “a group of elephants walking in muddy water.” “a living area with a television and a table” Figure 12: Random image samples on MS-COCO prompts. between fidelity and diversity. Interestingly, we find that guiding unCLIP does not decrease Recall while still improving aesthetic quality according to this metric.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Limitations and Risks", "weight": 1.5} -->

Although conditioning image generation on CLIP embeddings improves diversity, this choice does come with certain limitations. In particular, unCLIP is worse at binding attributes to objects than a corresponding GLIDE model. In Figure 14, we find that unCLIP struggles more than GLIDE with a prompt where it must bind two separate objects (cubes) to two separate attributes (colors). We hypothesize that this occurs because the CLIP embedding itself does not explicitly bind attributes to objects, and find that reconstructions from the decoder often mix up attributes and objects, as shown in Figure 15. A similar and likely related issue is that unCLIP struggles at producing coherent text, as illustrated in Figure 16; it is possible that the CLIP embedding does not precisely encode spelling information of rendered text. This issue is likely made worse because the BPE encoding we use obscures the spelling of the words in a caption from the model, so the model needs to have independently seen each token written out in the training images in order to learn to render it.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Limitations and Risks", "weight": 1.5} -->

We also note that our stack still has a hard time producing details in complex scenes (Figure 17). We hypothesize that this is a limitation of our decoder hierarchy producing an image at a base resolution of $64 \times 64$ and then upsampling it. Training our unCLIP decoder at a higher base resolution should be able to alleviate this, at the cost of additional training and inference compute.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Limitations and Risks", "weight": 1.5} -->

As discussed in the GLIDE paper, image generation models carry risks related to deceptive and otherwise harmful content. unCLIP's performance improvements also raise the risk profile over GLIDE. As the technology matures, it leaves fewer traces and indicators that outputs are AI-generated, making it easier to mistake generated images for authentic ones and vice versa. More research is also needed on how the change in architecture changes how the model learns biases in training data.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Limitations and Risks", "weight": 1.5} -->

The risks of these models should be assessed in relation to the particular deployment context, which includes training data, guardrails in place, the deployment space, and who will have access. A preliminary analysis of these issues in the context of the DALL·E 2 Preview platform (the first deployment of an unCLIP model), can be found in Mishkin et al..
