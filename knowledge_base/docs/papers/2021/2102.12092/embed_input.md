<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Zero-Shot Text-to-Image Generation

Topics include Transformers, Image generation, Datasets.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Text-to-image generation has traditionally focused on finding better modeling assumptions for training on a fixed dataset. These assumptions might involve complex architectures, auxiliary losses, or side information such as object part labels or segmentation masks supplied during training. We describe a simple approach for this task based on a transformer that autoregressively models the text and image tokens as a single stream of data. With sufficient data and scale, our approach is competitive with previous domain-specific models when evaluated in a zero-shot fashion.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern machine learning approaches to text to image synthesis started with the work of Mansimov et al., who showed that the DRAW Gregor et al. generative model, when extended to condition on image captions, could also generate novel visual scenes. Reed et al. later demonstrated that using a generative adversarial network, rather than a recurrent variational auto-encoder, improved image fidelity. Reed et al. showed that this system could not only generate objects with recognizable properties, but also could zero-shot generalize to held-out categories.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the next few years, progress continued using a combination of methods. These include improving the generative model architecture with modifications like multi-scale generators, integrating attention and auxiliary losses, and leveraging additional sources of conditioning information beyond just text.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Separately, Nguyen et al. propose an energy-based framework for conditional image generation that obtained a large improvement in sample quality relative to contemporary methods. Their approach can incorporate pretrained discriminative models, and they show that it is capable of performing text-to-image generation when applied to a captioning model pretrained on MS-COCO. More recently, Cho et al. also propose a method that involves optimizing the input to a pretrained cross-modal masked language model. While significant increases in visual fidelity have occurred as a result of the work since Mansimov et al., samples can still suffer from severe artifacts such as object distortion, illogical object placement, or unnatural blending of foreground and background elements.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances fueled by large-scale generative models suggest a possible route for further improvements. Specifically, when compute, model size, and data are scaled carefully, autoregressive transformers have achieved impressive results in several domains such as text, images, and audio.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) a tapir made of accordion. a tapir with the texture of an accordion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) an illustration of a baby hedgehog in a christmas sweater walking a dog (c) a neon sign that reads “backprop”. a neon sign that reads “backprop”. backprop neon sign (d) the exact same cat on the top as a sketch on the bottom Figure 2: With varying degrees of reliability, our model appears to be able to combine distinct concepts in plausible ways, create anthropomorphized versions of animals, render text, and perform some types of image-to-image translation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

By comparison, text-to-image generation has typically been evaluated on relatively small datasets such as MS-COCO and CUB-200. Could dataset size and model size be the limiting factor of current approaches? In this work, we demonstrate that training a 12-billion parameter autoregressive transformer on 250 million image-text pairs collected from the internet results in a flexible, high fidelity generative model of images controllable through natural language.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting system achieves high quality image generation on the popular MS-COCO dataset zero-shot, without using any of the training labels. It is preferred over prior work trained on the dataset by human evaluators 90% of the time. We also find that it is able to perform complex tasks such as image-to-image translation at a rudimentary level. This previously required custom approaches, rather emerging as a capability of a single, large generative model.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

Our goal is to train a transformer to autoregressively model the text and image tokens as a single stream of data. However, using pixels directly as image tokens would require an inordinate amount of memory for high-resolution images. Likelihood objectives tend to prioritize modeling short-range dependencies between pixels, so much of the modeling capacity would be spent capturing high-frequency details instead of the low-frequency structure that makes objects visually recognizable to us.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

We address these issues by using a two-stage training procedure, similar to: Stage 1. We train a discrete variational autoencoder (dVAE)^11^1 to compress each $256 \times 256$ RGB image into a $32 \times 32$ grid of image tokens, each element of which can assume $8192$ possible values. This reduces the context size of the transformer by a factor of $192$ without a large degradation in visual quality (see Figure 1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

Stage 2. We concatenate up to 256 BPE-encoded text tokens with the ${32 \times 32} = 1024$ image tokens, and train an autoregressive transformer to model the joint distribution over the text and image tokens.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

The overall procedure can be viewed as maximizing the evidence lower bound (ELB) on the joint likelihood of the model distribution over images $x$, captions $y$, and the tokens $z$ for the encoded RGB image. We model this distribution using the factorization ${p_{\theta,\psi}{(x,y,z)}} = {p_{\theta}{(\left. x \middle| {y,z} \right.)}p_{\psi}{(y,z)}}$, which yields the lower bound $q_{\phi}$ denotes the distribution over the $32 \times 32$ image tokens generated by the dVAE encoder given the RGB image $x$^22^2We assume that $y$ is conditionally independent of $x$ given $z$.; $p_{\theta}$ denotes the distribution over the RGB images generated by the dVAE decoder given the image tokens; and $p_{\psi}$ denotes the joint distribution over the text and image tokens modeled by the transformer.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

Note that the bound only holds for $\beta = 1$, while in practice we find it helpful to use larger values. The following subsections describe both stages in further detail.^33^3In preliminary experiments on ImageNet, we attempted to maximize the ELB with respect to $\phi$, $\theta$, and $\psi$ jointly, but were unable to improve on two-stage training.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stage One: Learning the Visual Codebook", "weight": 1.0} -->

In the first stage of training, we maximize the ELB with respect to $\phi$ and $\theta$, which corresponds to training a dVAE on the images alone. We set the initial prior $p_{\psi}$ to the uniform categorical distribution over the $K = 8192$ codebook vectors, and $q_{\phi}$ to be categorical distributions parameterized by the $8192$ logits at the same spatial position in the $32 \times 32$ grid output by the encoder.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stage One: Learning the Visual Codebook", "weight": 1.0} -->

The ELB now becomes difficult to optimize: as $q_{\psi}$ is a discrete distribution, and we cannot use the reparameterization gradient to maximize it. Oord et al.; Razavi et al. address this using an online cluster assignment procedure coupled with the straight-through estimator. We instead use the gumbel-softmax relaxation, replacing the expectation over $q_{\phi}$ with one over $q_{\phi}^{\tau}$, where the relaxation becomes tight as the temperature $\tau\rightarrow 0$. The likelihood for $p_{\theta}$ is evaluated using the log-laplace distribution (see Appendix A.3 for a derivation).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stage One: Learning the Visual Codebook", "weight": 1.0} -->

The relaxed ELB is maximized using Adam with exponentially weighted iterate averaging. Appendix A.2 gives a complete description of the hyperparameters, but we found the following to be especially important for stable training: Specific annealing schedules for the relaxation temperature and step size. We found that annealing $\tau$ to $1/16$ was sufficient to close the gap between the relaxed validation ELB and the true validation ELB with $q_{\phi}$ intsead of $q_{\phi}^{\tau}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stage One: Learning the Visual Codebook", "weight": 1.0} -->

The use of $1 \times 1$ convolutions at the end of the encoder and the beginning of the decoder. We found that reducing the receptive field size for the convolutions around the relaxation led to it generalizing better to the true ELB.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stage One: Learning the Visual Codebook", "weight": 1.0} -->

Multiplication of the outgoing activations from the encoder and decoder resblocks by a small constant, to ensure stable training at initialization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stage One: Learning the Visual Codebook", "weight": 1.0} -->

We also found that increasing the KL weight to $\beta = 6.6$ promotes better codebook usage and ultimately leads to a *smaller* reconstruction error at the end of training.^44^4This is contrary to the usual tradeoff between the two terms. We speculate that for smaller values of $\beta$, the noise from the relaxation causes the optimizer to reduce codebook usage toward the beginning of training, resulting in worse ELB at convergence.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stage Two: Learning the Prior", "weight": 1.0} -->

In the second stage, we fix $\phi$ and $\theta$, and learn the prior distribution over the text and image tokens by maximizing the ELB with respect to $\psi$. Here, $p_{\psi}$ is represented by a 12-billion parameter sparse transformer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stage Two: Learning the Prior", "weight": 1.0} -->

Given a text-image pair, we BPE-encode the lowercased caption using at most 256 tokens^55^5During training, we apply 10% BPE dropout, whose use is common in the neural machine translation literature. with vocabulary size $16384$, and encode the image using ${32 \times 32} = 1024$ tokens with vocabulary size $8192$. The image tokens are obtained using argmax sampling from the dVAE encoder logits, without adding any gumbel noise.^66^6Strictly speaking, Equation 1 requires us to sample from the categorical distribution specified by the dVAE encoder logits, rather than taking the argmax. In preliminary experiments on ImageNet, we found that this was a useful regularizer in the overparameterized regime, and allows the transformer to be trained using soft targets for the cross-entropy loss. We decided against this here since the model in consideration is in the underparameterized regime. Finally, the text and image tokens are concatenated and modeled autoregressively as a single stream of data.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stage Two: Learning the Prior", "weight": 1.0} -->

The transformer is a decoder-only model in which each image token can attend to all text tokens in any one of its 64 self-attention layers. The full architecture is described in Appendix B.1. There are three different kinds of self-attention masks used in the model. The part of the attention masks corresponding to the text-to-text attention is the standard causal mask, and the part for the image-to-image attention uses either a row, column, or convolutional attention mask.^77^7We found using a single attention operation for all three interactions -- "text attends to text", "image attends to text", and "image attends to image" -- to perform better than using separate attention operations that are independently normalized.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Stage Two: Learning the Prior", "weight": 1.0} -->

We limit the length of a text caption to 256 tokens, though it is not totally clear what to do for the "padding" positions in between the last text token and the start-of-image token. One option is to set the logits for these tokens to $- \infty$ in the self-attention operations. Instead, we opt to learn a special padding token separately for each of the 256 text positions. This token is used only when no text token is available. In preliminary experiments on Conceptual Captions, we found that this resulted in higher validation loss, but better performance on out-of-distribution captions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stage Two: Learning the Prior", "weight": 1.0} -->

We normalize the cross-entropy losses for the text and image tokens by the total number of each kind in a batch of data. Since we are primarily interested in image modeling, we multiply the cross-entropy loss for the text by $1/8$ and the cross-entropy loss for the image by $7/8$. The objective is optimized using Adam with exponentially weighted iterate averaging; Appendix B.2 describes the training procedure in more detail. We reserved about $606000$ images for validation, and found no signs of overfitting at convergence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data Collection", "weight": 1.0} -->

Our preliminary experiments for models up to $1.2$ billion parameters were carried out on Conceptual Captions, a dataset of 3.3 million text-image pairs that was developed as an extension to MS-COCO.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Data Collection", "weight": 1.0} -->

To scale up to $12$-billion parameters, we created a dataset of a similar scale to JFT-300M by collecting 250 million text-images pairs from the internet. This dataset does not include MS-COCO, but does include Conceptual Captions and a filtered subset of YFCC100M. As MS-COCO was created from the latter, our training data includes a fraction of the MS-COCO validation images (but none of the captions). We control for this in the quantitative results presented in Section 3 and find that it has no appreciable bearing on the results. We provide further details about the data collection process in Appendix C.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mixed-Precision Training", "weight": 1.0} -->

To save GPU memory and increase throughput, most parameters, Adam moments, and activations are stored in 16-bit precision. We also use activation checkpointing and recompute the activations within the resblocks during the backward pass. Getting the model to train in 16-bit precision past one billion parameters, without diverging, was the most challenging part of this project.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mixed-Precision Training", "weight": 1.0} -->

We believe the root cause of this instability to be underflow in the 16-bit gradients. Appendix D presents a set of guidelines we developed to avoid underflow when training large-scale generative models. Here, we describe one of these guidelines: per-resblock gradient scaling.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Mixed-Precision Training", "weight": 1.0} -->

Similar to prior work, we found that the norms of the activation gradients from the resblocks decrease monotonically as we move from the earlier resblocks to the later ones.^88^8It is possible that better initialization schemes might be able to avoid this, but we did not have success with alternative schemes in our experiments. As the model is made deeper and wider, the true exponents of the activation gradients for later resblocks can fall below the minimum exponent of the 16-bit format. Consequently, they get rounded to zero, a phenomenon called *underflow*. We found that eliminating underflow allowed for stable training to convergence.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Mixed-Precision Training", "weight": 1.0} -->

Standard loss scaling is able to avoid underflow when the range spanned by the smallest and largest activation gradients (in absolute value) fits within the exponent range of the 16-bit format. On NVIDIA V100 GPUs, this exponent range is specified by five bits. While this is sufficient for training vanilla language models of the same size, we found the range to be too small for the text-to-image model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Mixed-Precision Training", "weight": 1.0} -->

Our fix, which is shown in Figure 4, involves using a separate "gradient scale" for each resblock in the model. This can be seen as a practical alternative to a more general framework for mixed-precision training called Flexpoint, with the advantage that specialized GPU kernels are not required. We found that Sun et al. had independently developed similar procedure for training convolutional networks in 4-bit precision.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

Effective Parameter Count Table 1: We show the relationship between model size and the minimum compression rank for the gradients (up to a multiple of 128) necessary to avoid a gap in the training loss during the first 10% of training. These results suggest that in our setting, we can achieve a compression rate of about 85%, independent of model size.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

Our 12-billion parameter model consumes about 24 GB of memory when stored in 16-bit precision, which exceeds the memory of a 16 GB NVIDIA V100 GPU. We address this using parameter sharding. As shown in Figure 5, parameter sharding allows us to almost completely hide the latency of the intra-machine communication by overlapping it with compute-intensive operations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

On the cluster used to train the model, the bandwidth between machines is much lower than the bandwidth among GPUs on the same machine. This makes the cost of the operation used to average the gradient among the machines (all-reduce) the main bottleneck during training. We were able to drastically reduce this cost by compressing the gradients using PowerSGD.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

In our implementation, each GPU in a machine computes the low-rank factors for its parameter shard gradients independently of its neighboring GPUs.^99^9There is still intra-machine communication for other operations; what we mean is that the low-rank factors across the shards, when concatenated, are not regarded as collectively approximating the gradient for the full parameter matrix. Once the low-rank factors are computed, each machine sets its error buffer to the residual between the uncompressed gradient averaged over its eight GPUs (obtained from reduce-scatter), and the decompressed gradient obtained from the low-rank factors.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

PowerSGD replaces the large communication operation for an uncompressed parameter gradient with two, much smaller communication operations for its low-rank factors. For a given compression rank $r$ and transformer activation size $d_{model}$, the compression rate is given by $1 - {{5r}/{({8d_{\text{model}}})}}$ (see Appendix E.1). Table 1 shows that we can achieve a compression rate of about $85\%$, independent of model size.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

In Appendix E.2, we describe various details that were necessary to get PowerSGD to perform well at scale. These include: Saving memory by accumulating the gradient into the error buffers during backpropagation, rather than allocating separate buffers.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

Minimizing instances in which we zero out the error buffers (e.g., due to nonfinite values encountered during mixed-precision backpropagation, or when resuming training from a checkpoint).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

Improving numerical stability by using Householder orthogonalization instead of Gram-Schmidt, together with the addition of a small multiple of the identity matrix to the input.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

Avoiding underflow by using a custom 16-bit floating point format for the error buffers, their low-rank factors, and the all-reduce communication operations involving them.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Distributed Optimization", "weight": 1.0} -->

We also found the warm-start procedure for the $Q$ matrix described in Vogels et al. to be unnecessary: we were able to get equivalent results by fixing $Q$ to a random gaussian matrix at the start of training, and never updating it.^1010^10We verified that the error in reconstructing the true gradient is higher when $Q$ is fixed as opposed to being updated using warm-starting, so it is interesting that this does not affect the loss. By contrast, resampling $Q$ at every update causes a large performance hit.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sample Generation", "weight": 1.0} -->

Similar to Razavi et al., we rerank the samples drawn from the transformer using a pretrained contrastive model. Given a caption and a candidate image, the contrastive model assigns a score based on how well the image matches the caption. Figure 6 shows the effect of increasing the number of samples $N$ from which we select the top $k$ images. This process can be seen as a kind of language-guided search, and is also similar to the auxiliary text-image matching loss proposed by Xu et al.. Unless otherwise stated, all samples used for both qualitative and quantitative results are obtained without temperature reduction (i.e., using $t = 1$) (except for Figure 2) and use reranking with $N = 512$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

We evaluate our model zero-shot by comparing it to three prior approaches: AttnGAN, DM-GAN, and DF-GAN, the last of which reports the best Inception Score and Fréchet Inception Distance on MS-COCO. Figure 3 qualitatively compares samples from our model to those from prior work.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

We also conduct a human evaluation similar to the one used in Koh et al. to compare our approach to DF-GAN, the results of which are shown in Figure 7. Given a caption, the sample from our model receives the majority vote for better matching the caption 93% of the time. It also receives the majority vote for being more realistic 90% of the time.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Training the transformer on the tokens from the dVAE encoder allows us to allocate its modeling capacity to the low-frequency information that makes images visually recognizable to us. However, it also disadvantages the model, since the heavy compression renders it unable to produce high-frequency details. To test the effect of this on the quantitative evaluations, we compute the FID and IS in Figure 9(a) after applying a Gaussian filter with varying radius to both the validation images and samples from the models. Our approach achieves the best FID by a margin of about 6 points with a slight blur of radius 1. The gap between our approach and others tends to widen as the blur radius is increased. We also obtain the highest IS when the blur radius is greater than or equal to two.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

(a) FID and IS on MS-COCO as a function of blur radius.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

(b) FID and IS on CUB as a function of blur radius.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

(c) FID and IS on MS-COCO as a function of the sample size used for reranking.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Finally, Figure 9(c) shows clear improvements in FID and IS for MS-COCO as the sample size used for reranking with the contrastive model is increased. This trend continues up to a sample size of 32, after which we observe diminishing returns.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Data Overlap Analysis", "weight": 1.0} -->

We used the deduplication procedure described in Radford et al. to determine which images to remove. For each validation image, we find the closest image in the training data using a contrastive model specifically trained for this task. We then sort the images in descending order by closeness to their nearest matches in the training data. After inspecting the results by hand, we determine the images to remove by manually selecting a conservative threshold designed to minimize the false negative rate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Qualitative Findings", "weight": 1.0} -->

We found that our model has the ability to generalize in ways that we did not originally anticipate. When given the caption "a tapir made of accordion..." (Figure 2a), the model appears to draw a tapir with an accordion for a body, or an accordion whose keyboard or bass are in the shape of a tapir's trunk or legs. This suggests that it has developed a rudimentary ability to compose unusual concepts at high levels of abstraction.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Qualitative Findings", "weight": 1.0} -->

Our model also appears to be capable of combinatorial generalization, such as when rendering text (Figure 2b) or when probed on sentences like "an illustration of a baby hedgehog in a christmas sweater walking a dog" (Figure 2c). Prompts like the latter require the model to perform variable binding -- it is the hedgehog that is in the christmas sweater, not the dog. We note, however, that the model performs inconsistently on the task, sometimes drawing both animals with christmas sweaters, or drawing a hedgehog walking a smaller hedgehog.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Qualitative Findings", "weight": 1.0} -->

To a limited degree of reliability, we also find our model to be capable of zero-shot image-to-image translation controllable by natural language (Figure 2d). When the model is given the caption "the exact same cat on the top as a sketch at the bottom" and the top $15 \times 32$ part of the image token grid for a photo of a cat, it is able to draw a sketch of a similar looking cat on the bottom.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Qualitative Findings", "weight": 1.0} -->

This works with several other kinds of transformations, including image operations (e.g., changing the color of the image, converting it to grayscale, or flipping it upside-down) and style transfer (e.g., drawing the cat on a greeting card, a postage stamp, or a cell phone case). Some transformations, such as those that involve only changing the color of the animal, suggest that the model is capable of performing a rudimentary kind of object segmentation. We provide additional examples of zero-shot image-to-image translation in Section G.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We investigate a simple approach for text-to-image generation based on an autoregressive transformer, when it is executed at scale. We find that scale can lead to improved generalization, both in terms of zero-shot performance relative to previous domain-specific approaches, and in terms of the range of capabilities that emerge from a single generative model. Our findings suggest that improving generalization as a function of scale may be a useful driver for progress on this task.
