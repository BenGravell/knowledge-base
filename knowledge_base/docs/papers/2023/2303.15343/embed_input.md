<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sigmoid Loss for Language Image Pre-Training

Topics include Accuracy, Learning, SigLIP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a simple pairwise Sigmoid loss for Language-Image Pre-training (SigLIP). Unlike standard contrastive learning with softmax normalization, the sigmoid loss operates solely on image-text pairs and does not require a global view of the pairwise similarities for normalization. The sigmoid loss simultaneously allows further scaling up the batch size, while also performing better at smaller batch sizes. Combined with Locked-image Tuning, with only four TPUv4 chips, we train a SigLiT model that achieves 84.5% ImageNet zero-shot accuracy in two days. The disentanglement of the batch size from the loss further allows us to study the impact of examples vs pairs and negative to positive ratio. Finally, we push the batch size to the extreme, up to one million, and find that the benefits of growing batch size quickly diminish, with a more reasonable batch size of 32k being sufficient. We release our models at and hope our research motivates further explorations in improving the quality and efficiency of language-image pre-training.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contrastive pre-training using weak supervision from image-text pairs found on the web is becoming the go-to method for obtaining generic computer vision backbones, slowly replacing pre-training on large labelled multi-class datasets. The high-level idea is to simultaneously learn an aligned representation space for images and texts using paired data. Seminal works CLIP and ALIGN established the viability of this approach at a large scale, and following their success, many large image-text datasets became available privately and publicly.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The standard recipe to pre-train such models leverages the image-text contrastive objective. It aligns the image and Table 1: SigLiT and SigLIP results. Sigmoid loss is memory efficient, allows larger batch sizes (BS) that unlocks language image pre-training with a small number of chips. SigLiT model with a frozen public B/8 checkpoint, trained on the LiT image-text dataset using four TPUv4 chips for one day, achieves 79.7% 0-shot accuracy on ImageNet. The same setup with a g/14 checkpoint leads to 84.5% accuracy, trained for two days. With a public unlocked B/16 image checkpoint, trained on the WebLI dataset, SigLIP achieves 71.0% 0-shot accuracy using 16 TPU-v4 chips for three days. The last two rows show results with randomly initialized models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

| | Image | Text | BS | #TPUv4 | Days | INet-0 | ∗ We use a variant of the L model with 12 layers. text embeddings for matching (positive) image-text pairs while making sure that unrelated (negative) image-text pairs are dissimilar in the embedding space. This is achieved via a batch-level softmax-based contrastive loss, applied twice to normalize the pairwise similarity scores across all images, then all texts. A naive implementation of the softmax is numerically unstable; it is usually stabilized by subtracting the maximum input value before applying the softmax, which requires another pass over the full batch.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a simpler alternative: the sigmoid loss. It does not require any operation across the full batch and hence greatly simplifies the distributed loss implementation and boosts efficiency. Additionally, it conceptually decouples the batch size from the definition of the task. We compare the proposed sigmoid loss with the standard softmax loss across multiple setups. In particular, we investigate sigmoid-based loss with two promi- nent approaches for image-text learning: CLIP and LiT, which we call sigmoid language image pretraining ( SigLIP ) and sigmoid LiT ( SigLiT ), respectively. We find that the sigmoid loss performs significantly better than the softmax loss when the batch size is smaller than 16 k. As the train batch size grows, the gap closes. Importantly, the sigmoid loss is symmetric, requires just a single pass, and a typical implementation requires less memory than the softmax loss. This enables successful training of a SigLiT model at a batch size of one million. However, we find that the performance saturates with growing batch size, both for softmax and sigmoid.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The good news is that a reasonable batch size, i.e. 32 k, is sufficient for image-text pretraining. This conclusion also holds for multilingual SigLIP training on over 100 languages.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Table 1, we present setups for image-text pre-training that require a moderate amount of TPUv4 chips for training. SigLiT is surprisingly efficient, reaching 79.7% zero-shot accuracy on ImageNet in just a single day on four chips. SigLIP's more demanding from-scratch training reaches 73.4% zero-shot accuracy in 5 days with 32 TPUv4 chips. This compares favorably to prior works such as FLIP and CLIP, which require approximately 5 and 10 days respectively on 256 TPUv3 cores. When fine-tuning a pretrained vision backbone in SigLIP, denoted as in Table 1, we found that disabling the weight decay on the pre-trained backbone leads to better results (see Figure 4 for details). We hope our work paves the way for making the nascent language-image pre-training field more accessible.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Algorithm 1 Sigmoid loss pseudo-implementation", "weight": 1.0} -->

1 # img_emb: image model embedding [n, dim] 2 # txt_emb: text model embedding [n, dim] 3 # t_prime, b: learnable temperature and bias 4 # n: mini-batch size 5 6 t = exp(t_prime) 7 zimg = l2_normalize(img_emb) 8 ztxt = l2_normalize(txt_emb) 9 logits = dot(zimg, ztxt.T) * t + b 10 labels = 2 * eye(n) -ones(n) # -1 with diagonal 1 11 l = -sum(log_sigmoid(labels * logits)) / n instead, while CoCa adds such a decoder to the discriminative CLIP/ALIGN setup, thus combining the pros and cons of both approaches into a single very capable model. BLIP further proposes CapFilt which uses the generative decoder to create better captions and the discriminative part of the model to filter pairs. Language-Image pre-training is a very active field and surveys rapidly become outdated.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Algorithm 1 Sigmoid loss pseudo-implementation", "weight": 1.0} -->

Efficient language-image pre-training On the other hand, few works have tried making language image pre-training more efficient. LiT and FLIP are notable attempts, the former requires a pre-trained and locked backbone, and the latter sacrifices quality by randomly dropping visual tokens. BASIC and LAION look at scaling batchsize but only go up to 16 k and 160 k respectively, by using many hundreds of chips, and for the former also mixing in a large private classification dataset. The recent Lion optimizer claims to be able to reduce the training cost to reach similar quality.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

In this section, we first review the widely-used softmaxbased contrastive loss. We then introduce the pairwise sigmoid loss and discuss its efficient implementation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

Given a mini-batch B = { ( I 1, T 1 ), ( I 2, T 2 ),... } of image-text pairs, the contrastive learning objective encourages embeddings of matching pairs ( I i, T i ) to align with each other, while pushing embeddings of unmatched pairs ( I i, T j = i ) apart. For practical purposes, it is assumed that for all images i, the text associated with a different image j is not related to i, and vice-versa. This assumption is usually noisy and imperfect.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Softmax loss for language image pre-training", "weight": 1.0} -->

When using the softmax loss to formalize this objective, an image model f (·) and a text model g (·) are trained to minimize the following objective: (a) Initially each device holds 4 image and 4 text representations. Each device needs to see the representations from other devices to calculate the full loss.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Softmax loss for language image pre-training", "weight": 1.0} -->

(b) They each compute the component of the loss (highlighted) for their representations, which includes the positives.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Softmax loss for language image pre-training", "weight": 1.0} -->

(c) Texts are swapped across the devices, so device 1 now has I 1:4 and T 5:8 etc. The new loss is computed and accumulated with the previous.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Softmax loss for language image pre-training", "weight": 1.0} -->

(d) This repeats till every image & text pair have interacted, e.g. device 1 has the loss of I 1:4 and T 1:12. A final cross-device sum brings everything together.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sigmoid loss for language image pre-training", "weight": 1.0} -->

Instead of the softmax-based contrastive loss, we propose a simpler alternative that does not require computing global normalization factors. The sigmoid-based loss processes every image-text pair independently, effectively turning the learning problem into the standard binary classification on the dataset of all pair combinations, with a positive labels for the matching pairs (I i, T i) and negative labels for all other pairs (I i, T j = i). It is defined as follows: where z ij is the label for a given image and text input, which equals 1 if they are paired and -1 otherwise. At initial- ization, the heavy imbalance coming from the many negatives dominates the loss, leading to large initial optimization steps attempting to correct this bias. To alleviate this, we introduce an additional learnable bias term b similar to the temperature t. We initialize t ′ and b to log 10 and -10 respectively. This makes sure the training starts roughly close to the prior and does not require massive over-correction. Algorithm 1 presents a pseudocode implementation of the proposed sigmoid loss for language image pre-training.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Efficient 'chunked' implementation", "weight": 1.0} -->

Contrastive training typically utilizes data parallelism. Computing the loss when data is split across D devices necessitates gathering all embeddings with expensive all-gathers and, more importantly, the materialization of a memory-intensive |B| × |B| matrix of pairwise similarities.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Efficient 'chunked' implementation", "weight": 1.0} -->

The sigmoid loss, however, is particularly amenable to a memory efficient, fast, and numerically stable implementation that ameliorates both these issues. Denoting the perdevice batch size as b = |B| D, the loss is reformulated as: This is particularly simple for the sigmoid loss as each pair is an independent term in the loss. Figure 1 illustrates this method. In words, we first compute the component of the loss corresponding to the positive pairs, and b -1 negative pairs. We then permute representations across devices, so each device takes negatives from its neighbouring device (next iteration of sum B). The loss is then calculated with respect to this chunk (sum C). This is done independently in each device, such that each device computes the loss with respect to its local batch b. Losses can then simply be summed across all devices (sum A). Individual collective permutes (for sum B) are fast (and indeed D collective permutes is typically faster than two all-gathers between D devices), and the memory cost at any given moment is reduced from |B| 2 to b 2 (for sum C).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Efficient 'chunked' implementation", "weight": 1.0} -->

Usually b is constant as scaling |B| is achieved by increasing the number of accelerators. Due to being quadratic with respect to the batch size, the vanilla loss computation rapidly bottlenecks scaling up. This chunked approach enabled training with batch sizes over 1 million on relatively few devices.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we evaluate the proposed SigLiT and SigLIP models across a wide range of batch sizes. We discuss what can be achieved with a small number of accelerator chips, using both SigLiT and SigLIP recipes. We also briefly discuss the impact of batch size on multilingual language image pre-training. We ablate the importance of our large-batch stabilization modification and the introduced learned bias term and present a study on the effect of positive and negative pairs ratio in the sigmoid loss. Lastly, we explore SigLIP's data noise robustness.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results", "weight": 1.0} -->

To validate our models, we report zero-shot transfer results on the ImageNet dataset and zero-shot retrieval results across 36 languages on the XM3600 dataset. We use the ScalingViT-Adafactor optimizer by default for all our experiments.

<!-- chunk {"id": "body-0023", "role": "body", "section": "SigLiT: Scaling batch size to the limit", "weight": 1.0} -->

Following, we use the same precomputed embeddings for the images using a ViT-g vision model, and train a base size text tower from scratch with the same hyperparameters using the LiT image-text dataset.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SigLiT: Scaling batch size to the limit", "weight": 1.0} -->

We perform a study over a wide range of batch sizes, from 512 to 1 M, demonstrating the impact of batch size for contrastive learning. Results are presented in Figure 2 (left). When the batch size is smaller than 16 k, sigmoid loss outperforms softmax loss by a large margin. With growing batch sizes, we observe that softmax loss quickly catches up and potentially slightly underperforms sigmoid loss with a large enough batch size. Overall, we recommend using the SigLIP recipe for large batch sizes as well, due to the simplicity, compute savings, and straightforward memory efficient implementation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SigLiT: Scaling batch size to the limit", "weight": 1.0} -->

There is a consensus that contrastive learning benefits from large batch sizes, while most of the existing studies stop at 64 k batch size. We successfully trained an SigLiT model at one million batch size, to explore the limit of contrastive learning. To our surprise, the performance saturates at 32 k batch size, further scaling up the batch size only gives a minor boost, and the model peaks at Figure 3: SigLiT ImageNet 0-shot transfer results with different training durations. Large batch size results in a big performance boost, but needs a sufficiently long schedule to ramp up, as for short schedules, very large batch size results in a small number of gradient update steps.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SigLiT: Scaling batch size to the limit", "weight": 1.0} -->

256 k batch size. Our best SigLiT with a B -sized text mode achieves 84.7% zero-shot transfer accuracy on ImageNet, while the original LiT paper reports a slightly better 85.2% score with a 10 times larger g -sized text model. Figure 3 presents the impact of training duration for different batch sizes. It demonstrates that large, 262 k batch size significantly outperforms smaller 8 k batch size when trained for a sufficiently long time. Note, that for short training durations, large batch size leads to the fewer absolute number of update steps and thus needs more time to ramp up.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SigLIP: Sigmoid loss is beneficial for languageimage pre-training", "weight": 1.0} -->

We pre-train SigLIP models on the WebLI dataset, using only English image and text pairs. We use CLIP (WebLI) to denote the CLIP baseline pre-trained on WebLI with the standard softmax loss. We use moderately-sized models: B/16 ViT for image embeddings and B-sized transformer for text embeddings. The input images are resized to 224 × 224 resolution. The text is tokenized by a 32 k vocabulary sentencepiece tokenizer trained on the English C4 dataset, and a maximum of 16 text tokens are kept. Figure 2 middle plot shows SigLIP results, With less than 32 k batch size, SigLIP outperforms CLIP (WebLI) baselines. On the other end of the scale, the memory efficiency of the sigmoid loss enabled much larger batch sizes. For example, with four TPU-v4 chips, we could fit a batch size of 4096 with a Base SigLIP but only 2048 with a corresponding CLIP model. The two advantages together demonstrate significant benefits of the sigmoid loss for language image pre-training with fixed resources, which will be discussed in Section 4.5.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SigLIP: Sigmoid loss is beneficial for languageimage pre-training", "weight": 1.0} -->

As batch size increases, the gap between the sigmoid and the softmax losses diminish. SigLIP performs best at batch size 32 k, whereas the softmax loss required 98 k for optimal performance and still didn't outperform the sigmoid based variant. Scaling further, a larger batch size like 307 k hurts both losses.

<!-- chunk {"id": "body-0029", "role": "body", "section": "mSigLIP: Multi-lingual pre-training", "weight": 1.0} -->

We further scale up the training data by keeping all the 100 languages from the WebLI dataset. With multilingual data, one usually needs to use a larger international vocabulary. We first verify the impact of two tokenizers: a small multilingual vocabulary with 32 k tokens, and a large multilingual vocabulary with 250 k tokens. We train B-sized ViT and text models for 900 M total examples seen, and observe slightly more than 1% improvement when using a larger vocabulary.

<!-- chunk {"id": "body-0030", "role": "body", "section": "mSigLIP: Multi-lingual pre-training", "weight": 1.0} -->

However, the token embeddings become huge for very large vocabulary sizes. Following the standard setup, we would need to store a N × W token embedding lookup table to train the multilingual model, where N is the vocabulary size mentioned above and W is the embedding dimension of the text model. To save memory, we propose to use a 'bottlenecked' token embedding. We use N × K embedding matrix and additional K × W projection, where the bottleneck K is much smaller than W.

<!-- chunk {"id": "body-0031", "role": "body", "section": "mSigLIP: Multi-lingual pre-training", "weight": 1.0} -->

In our experiments, we observed that using a large multilingual vocabulary with a bottleneck can be scaled up as efficiently as using a small multilingual vocabulary. Specifically, by enabling the bottleneck of size K = 96 for Base architecture with W = 768, we only see about a half percent quality drop on ImageNet zero-shot transfer, compared to using the full 250 k vocabulary.

<!-- chunk {"id": "body-0032", "role": "body", "section": "mSigLIP: Multi-lingual pre-training", "weight": 1.0} -->

With the memory improvements, we train mSigLIP models for various batch sizes, for a total of 30 billion examples seen. Table 2 and Figure 2 (right plot) show the results. We were expecting a large batch size to improve multilingual pre-training, where the model sees more examples from the same language as hard negatives in a single mini-batch. However, we didn't observe clear improvements with a batch size larger than 32 k. A batch size of 32 k is sufficient for a multilingual setup as well. On the XM3600 cross-modal retrieval tasks, we found that going beyond 32 k batch size leads to worse results on average while on ImageNet zero-shot transfer it stays flat. mSigLIP sets the new state-of-the-art on XM3600 text to image retrieval task, with only a Base size model. Our best result is 34.9%, which is more than 6% higher than the previously reported result 28.5% with a standard LiT model using a much larger four billion ViT-e model. We further scale up mSigLIP training in Section 4.6.

<!-- chunk {"id": "body-0033", "role": "body", "section": "SigLiT with four TPU-v4 chips", "weight": 1.0} -->

For many practitioners, the important question usually is 'what can be trained with a limited amount of resources?' We explore the usage of SigLiT models in this section with only four TPU-v4 chips, as the memory efficient sigmoid loss is suitable for this application scenario.

<!-- chunk {"id": "body-0034", "role": "body", "section": "SigLiT with four TPU-v4 chips", "weight": 1.0} -->

We follow the same setup as in section 4.1. We use the publicly available ViT-AugReg-B/8 model as the frozen vision tower, and precompute embeddings to accelerate the training. The text model is a Large Transformer, but with a depth of only 12 layers (instead of 24). It is trained using the LION optimizer with decoupled weight decay 1 × 10 -7, linearly warm-up of learning rate over 6.5k steps up to a peak of 1 × 10 -4, followed by a cosine decay to 0. We train for a total of 65 000 steps with a batch size of 32k - this leads to just under one day of training. Table 1 shows the results when training a model on four chips for one day, achieving 79.7% 0-shot ImageNet classification accuracy; very competitive in this limited resource regime. With a ViT-g/14 model as the vision tower and a Large text tower, we can train at 20 k batch size on four chips for 107 k steps in under two days. This further pushes the 0-shot ImageNet classification accuracy up to 84.5%.

<!-- chunk {"id": "body-0035", "role": "body", "section": "SigLIP with a small amount of TPU-v4 chips", "weight": 1.0} -->

It's resource demanding to train a CLIP model fromscratch in general, with SigLIP it's possible to fit a larger train batch size with fewer amount of chips. In this section, we explore ways to train SigLIP models efficiently with pretrained weights. We use pre-trained weights to initialize the image model to accelerate the pre-training, which was orig- inally discussed. We use the public and unlocked ViT-AugReg-B/16 model to initialize our vision tower and fine-tune on the same WebLI English data as used for SigLIP. In all the experiments, we apply a 0.1 learning rate multiplier to the pre-trained image tower to make it suitable for fine-tuning.

<!-- chunk {"id": "body-0036", "role": "body", "section": "SigLIP with a small amount of TPU-v4 chips", "weight": 1.0} -->

We hypothesize that the default weight decay applied to the pre-trained weights reduces their effectiveness. Motivated by the fine-tuning recipe, that uses no weight decay, we also propose disabling weight decay on the pre-trained weights for SigLIP training. Weight decay is therefore only applied to the randomly initialized weights in the text model. This simple modification significantly improved SigLIP results. Figure 4 shows that with our improved recipe, SigLIP reaches 71% 0-shot accuracy on ImageNet, using 16 k batch size, trained on 16 chips for three days. We also present from-scratch results in the bottom rows of Table 1: with 32 TPUv4 chips for only two days, SigLIP achieves 72.1% 0-shot accuracy. This presents a significant training cost reduction e.g. compared to CLIP (approx. 2500 TPUv3-days for 72.6%) reported.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Scaling up SigLIP and mSigLIP", "weight": 1.0} -->

In this section, we scale up SigLIP by 'overtraining' the model. We present results in Table 3 using ViT-B, ViT-L or So-400m as the vision encoder, with a text encoder of the same size (B, L and So-400m respectively). Following the recipe described in Section 4.2, we train both models for 40 billion examples seen at batch size 32 k, but use (256 / 16) 2 = 256 image patches and 64 text tokens (instead of 16). To get SigLIP models for different resolutions, we train for 5 billion more examples at the target resolution, with a 100x smaller learning rate and no weight decay. In Table 3, we report zero-shot classification results on ImageNet, ObjectNet, ImageNet-v2, ImageNet ReaL, and zero-shot image-to-text (I → T) retrieval, textto-image (I → T) retrieval results on MSCOCO.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Scaling up SigLIP and mSigLIP", "weight": 1.0} -->

We also scale up the multilingual mSigLIP ViT-B model in the same way. We report image-text retrieval results across 36 languages on the XM3600 benchmark. The scaled-up mSigLIP ViT-B model achieves the state-of-theart 42.6% image retrieval recall@1 and 54.1% text retrieval recall@1 for a Base model. This is slightly outperformed by the Large model in getting 42.96% image retrieval recall@1. Detailed results are provided in Appendix Table 9 and Figure 8, denoted as *32 k.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Stabilizing large-batch training", "weight": 1.0} -->

As we move to large batch sizes, the language image pretraining using transformers becomes increasingly more unstable, even when using a modestly-sized model (e.g. Base size). The reason for these instabilities is large spikes in the gradient norms, which translate to large-magnitude changes in the weights that may destabilize the training process, see Figure 5. We observe that reducing β 2 in Adam and AdaFactor from its default 0.999 to 0.95 (which was suggested in ) is enough to stabilize the training. Intuitively, this allows recovering from gradient spikes quicker. We opt for setting β 2 = 0. 95 for all our experiments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Stabilizing large-batch training", "weight": 1.0} -->

| Method | Image Encoder | Image Encoder | ImageNet-1k | ImageNet-1k | ImageNet-1k | ImageNet-1k | COCO R@1 | COCO R@1 |

<!-- chunk {"id": "body-0041", "role": "body", "section": "Negative ratio in sigmoid loss", "weight": 1.0} -->

One question which arises when shifting the perspective from the softmax's 'pick the right class' view to the sigmoid's 'rate this pair' view, is the imbalance in positive versus negative pairs. For a batch size |B|, the batch contains |B| positive pairs, but |B| 2 - |B| negative examples. In the modest batch-size of 16 k, there are actually 268 M negative examples for only 16 k positive ones. At the same time, because the sigmoid loss decomposes into a sum of per-example losses, we can perform controlled experiments to study the effect of the mini-batch composition and dis- tribution of examples visited. We run experiments in the SigLiT setup at batch-size 16 k for 900 M steps and vary the composition of the batch by masking out ( i.e.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Negative ratio in sigmoid loss", "weight": 1.0} -->

- Random: Randomly choose negative pairs to mask. - Hard: Keep hardest negative pairs (highest loss). - Easy: Keep easiest negatives pairs (lowest loss). - Hard + matching total pairs seen: Masking examples while training for a fixed number of steps does decrease the total number of pairs seen during training. Hence in the matched pairs setting, we increase the number of training steps by the masking ratio in order to keep the number of pairs seen constant.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Negative ratio in sigmoid loss", "weight": 1.0} -->

We also look at the value of the learned bias at the end of training as well as the average logit value for positive and negative examples across these settings, and find the result mostly follows what one would expect: as fewer negatives are present, the bias and logits become more positive overall. Interestingly, when training with more hard negative pairs, the average logits of positive pairs stays mostly flat.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Negative ratio in sigmoid loss", "weight": 1.0} -->

This study confirms that the imbalance does not seem to be a major reason for concern, while at the same time coming up with an efficient way of including more negative examples can be promising but is not trivial.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Bias term in sigmoid loss", "weight": 1.0} -->

We ablate the bias term in the loss function, using the Base architecture with an 8 k batch size, trained for 900M examples with the SigLIP setup. Zero-shot transfer results are reported on ImageNet, Oxford-iiit pet and Cifar100. Table 4 presents results with and without a bias term in the sigmoid loss.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Bias term in sigmoid loss", "weight": 1.0} -->

Enabling the bias term with a -10 initialization consistently improves performance across all tasks. This is because the bias term ensures that the training starts close to the prior, preventing dramatic over-correction in early optimization. In contrast, a randomly chosen bias term initialization, such as the 0 initialization in Table 4, fails to address the over-correction issue, leading to significantly worse results. This effect is particularly noticeable when using a small temperature t ′ initialization. We set the bias and temperature initialization to b = -10 and t ′ = log 10 (hence t = 10 ) as the default for all experiments.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Label noise robustness", "weight": 1.0} -->

Prior works demonstrated improved robustness against label noise when using the sigmoid loss for classification models. This property would be particularly useful here in the face of the famously noisy nature of popular largescale image-text datasets. In order to study this for SigLIP, we train M/16 image models alongside an M text model at batch size 16384 for 3.6 billion seen examples.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Label noise robustness", "weight": 1.0} -->

- Image: With probability p, replace the image with uniform random noise. - Text: With probability p, replace tokenized text with a new sequence of randomly sampled tokens, up to some (sampled) sequence length. - Batch alignment: Randomly shuffle the ordering of p %of the batch. - Image & text: Apply both with probability p each. - Image, text & batch: Alongside, also shuffle fraction p of alignments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Label noise robustness", "weight": 1.0} -->

Results from varying the likelihood of the corruption are shown in Figure 7. Models trained with sigmoid loss are increasingly robust to all kinds of added noise.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conducted a study on two language-image pretraining instances that used the sigmoid loss: SigLiT and SigLIP. Our results demonstrate that the sigmoid loss performs better than the softmax baseline, particularly for small train batch sizes. This loss function is also more memory efficient, which allows larger train batch sizes without requiring additional resources. We performed a thorough investigation of the batch size in contrastive learning. Surprisingly, we found that a relatively modest batch size of 32 k yielded nearly optimal performance. Further studies have been performed to understand better the introduced bias term in the sigmoid loss, robustness to data noises and the impact of positive and negative pairs ratio in the sigmoid loss. We hope this work will facilitate language-image pretraining research with limited resources.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgements. We thank Daniel Keysers, Ilya Tolstikhin, Olivier Bousquet and Michael Tschannen for their valuable feedback and discussions on this paper. We thank Joan Puigcerver, Josip Djolonga and Black Hechtman for discussions on efficient implementations of the chunked contrastive loss. We thank Kaiming He and Xinlei Chen for the discussion of β 2 to stabilize the training. We also thank Ross Wightman for spotting a mistake in the pseudocode in the first version of this paper, Boris Dayma and Krzysztof Maziarz for spotting typos in the second and third versions which made t vs t ′ confusing. We thank the Google Deepmind team for providing a supportive research environment. We use the big vision codebase for all experiments in this project.
