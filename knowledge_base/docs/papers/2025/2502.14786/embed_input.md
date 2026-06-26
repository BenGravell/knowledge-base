<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce SigLIP 2, a family of new multilingual vision-language encoders that build on the success of the original SigLIP. In this second iteration, we extend the original image-text training objective with several prior, independently developed techniques into a unified recipe - this includes captioning-based pretraining, self-supervised losses (self-distillation, masked prediction) and online data curation. With these changes, SigLIP 2 models outperform their SigLIP counterparts at all model scales in core capabilities, including zero-shot classification, image-text retrieval, and transfer performance when extracting visual representations for Vision-Language Models (VLMs). Furthermore, the new training recipe leads to significant improvements on localization and dense prediction tasks. We also train variants which support multiple resolutions and preserve the input's native aspect ratio. Finally, we train on a more diverse data-mixture that includes de-biasing techniques, leading to much better multilingual understanding and improved fairness.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To allow users to trade off inference cost with performance, we release model checkpoints at four sizes: ViT-B (86M), L (303M), So400m (400M), and g (1B).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contrastive image-text embedding models trained on billion-scale datasets, as pioneered by CLIP and ALIGN, have become the mainstream approach for high-level, semantic understanding of visual data. These models enable fine-grained, zero-shot classification rivaling the quality of supervised methods and enable efficient text-to-image and image-to-text retrieval. Furthermore, they lead to excellent vision-language understanding capabilities when combined with Large Language Models (LLMs) to build Vision-Language Models (VLMs).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Developing on the success of CLIP, several improvements have been proposed such as re-captioning images, adding image-only self-supervised losses, and training with a small decoder for auxiliary tasks such as captioning and localization. At the same time, several groups have released model checkpoints for the open-source community. However, these releases do not include the full breadth of latest improvements into a single model, as they all relatively closely follow CLIP's original approach. Here, building on the SigLIP training recipe, we incorporate several improvements from prior work and release a new family of open models^11^1Model checkpoints are available at\big_vision/configs/proj/image_text/README_siglip2.md that both excel on CLIP's core capabilities-----zero-shot classification, retrieval, and feature extraction for VLMs---and improve areas where vanilla CLIP-style models lag behind, including localization and extracting dense, semantic representations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, SigLIP 2 models provide the following: Strong multilingual vision-language encoders: SigLIP 2 shows excellent performance on English-focused vision-language tasks while providing strong results on multilingual benchmarks with a single model. This enables use in a wide range of languages and cultural contexts.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dense features: We incorporate self-supervised losses as well as a decoder-based loss, which result in better dense features (e.g. for segmentation and depth estimation) and improve localization tasks (such as referring expression comprehension).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Backward compatibility: SigLIP 2 is designed to be backward compatible with SigLIP by relying on the same architecture. This allows existing users to simply swap out the model weights and tokenizer (which is now multilingual) to get improvements on a wide range of tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Native aspect ratio and variable resolution: SigLIP 2 also includes a NaFlex variant, which supports multiple resolutions and preserves the native image aspect ratio. These models have the potential to improve aspect sensitive applications such as document understanding.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Strong small models: SigLIP 2 further optimizes performance of smaller models (B/16 and B/32 models), by using techniques in distillation via active data curation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the next section we provide a detailed description of the SigLIP 2 training recipe. Sec. 3 presents evaluations of SigLIP 2 models and baselines across a variety of tasks and benchmarks. Finally, Sec. 4 gives a short overview of related work, and conclusions can be found in Sec. 5.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Training recipe", "weight": 1.0} -->

We combine the original SigLIP training recipe with decoder-based pretraining, in addition to self-distillation and masked prediction as in the DINO line of work (see Fig. 1 for an overview). Pretraining an image encoder with a language decoder for captioning and referring expression comprehension was shown to improve OCR capabilities and localization, whereas self-distillation and masked prediction leads to better features for dense prediction tasks, zero-shot classification and retrieval. Rather than combining all these techniques in a single run we follow a staged approach as outlined below to manage the computational and memory overhead compared to SigLIP training.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Training recipe", "weight": 1.0} -->

In addition to training a set of models and adapting each model separately to different resolutions while distorting the aspect ratio, we also train variants which process images while largely preserving their native aspect ratio like NaViT and support different sequence lengths as FlexiViT. We call this variant NaFlex, described in Sec. 2.4.2 ‣ 2.4 Adaptation to different resolutions ‣ 2 Training recipe ‣ SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features").

<!-- chunk {"id": "body-0014", "role": "body", "section": "Training recipe", "weight": 1.0} -->

Finally, to improve the quality of the smallest models we fine-tune those with implicit distillation via active sample selection, following the approach.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Architecture, training data, optimizer", "weight": 1.0} -->

For the architecture, we follow SigLIP so that existing users can simply swap out the encoder weights. Specifically, the fixed-resolution variant relies on the standard ViT architecture with learned positional embedding. We use the same architecture for the image and text tower, except for the g-sized vision encoder which is paired with an So400m-sized text encoder. Vision and text representations are pooled using a MAP head (attention pooling). We set the text length to 64 and use the multilingual Gemma tokenizer with vocabulary size 256k, transforming the text to lower case before tokenization.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Architecture, training data, optimizer", "weight": 1.0} -->

We use the WebLI dataset containing 10 billion images and 12 billion alt-texts covering 109 languages. To strike a good balance between quality on English and multilingual vision-language benchmarks we compose the mixture such that 90% of the training image-text pairs is sourced from English web pages, and the remaining 10% from non-English web pages, as recommended. We further apply the filtering techniques from to mitigate data biases in representation and association with respect to sensitive attributes.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Architecture, training data, optimizer", "weight": 1.0} -->

Unless noted otherwise, we use the Adam optimizer with learning rate $10^{-3}$, decoupled weight decay $10^{-4}$, and gradient clipping to norm 1. We set the batch size to 32k and use a cosine schedule with 20k warmup steps, training for a total of 40B examples. Our models are trained on up to 2048 TPUv5e chips using a fully-sharded data-parallel strategy (FSDP ).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Training with Sigmoid loss and decoder", "weight": 1.0} -->

In the first step of pretraining, we combine SigLIP with LocCa by simply combining the two losses with equal weight. Unlike CLIP, which relies on a contrastive loss, SigLIP creates binary classification problems by combining every image embedding with every text embedding in the mini-batch and trains the embeddings to classify matching and non-matching pairs via logistic regression (sigmoid loss). We use the original implementation and refer to for details.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training with Sigmoid loss and decoder", "weight": 1.0} -->

For LocCa, we attach a standard transformer decoder with cross-attention to the un-pooled vision encoder representation (before applying the MAP head). The decoder follows the shapes of the text encoder except that we add cross-attention layers and reduce the number of layers by a factor of two. Besides image captioning, LocCa also trains for automatic referring expression prediction and grounded captioning. The former amounts to predicting bounding box coordinates for captions describing specific image regions, whereas the latter involves predicting region-specific captions given bounding box coordinates. Region-caption pairs are automatically annotated by first extracting n-grams from the alt-texts and then applying open-vocabulary detection using the recipe. Additionally, we use the fixed set of object categories from instead of n-grams. For each example, the decoder is trained to predict all three targets (amounting to three decoder forward-passes). The captioning target is predicted with parallel prediction with probability of 50%, i.e. all caption tokens are predicted in parallel from mask tokens, without causal attention mask. Please refer to for more detail.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training with Sigmoid loss and decoder", "weight": 1.0} -->

Finally, to reduce memory consumption due to the large vocabulary, we implement a chunked version of the decoder loss.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training with Sigmoid loss and decoder", "weight": 1.0} -->

For all model sizes, we set the vision encoder patch size to 16 and the image resolution to 256 (resulting in an image representation sequence length of 256). Finally, we note that the decoder only serves for representation learning here and is not part of the model release.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training with self-distillation and masked prediction", "weight": 1.0} -->

Following SILC and TIPS, we augment the training setup described in Sec. 2.2 with local-to-global correspondence learning with self-distillation and masked prediction losses to improve the local semantics of the (un-pooled) feature representation. This representation is typically used for dense prediction tasks like segmentation, depth estimation etc. Concretely, we add two terms to the losses described in Sec. 2.2 as detailed next.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training with self-distillation and masked prediction", "weight": 1.0} -->

The first term is the local-to-global consistency loss, in which the vision encoder becomes the student network, which gets a partial (local) view of the training image, and is trained to match the teacher's representation, derived from the full image. This auxiliary matching task is performed in a high-dimensional feature space computed with a separate MLP head. As is common in the literature, the teacher parameters are obtained as an exponential moving average (EMA) of the student parameters over the previous iterations. We rely on a single global (teacher) view and 8 local (student) views and otherwise follow the augmentations, loss and hyper parameters.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training with self-distillation and masked prediction", "weight": 1.0} -->

The second loss term is the masked prediction objective. We replace 50% of the embedded image patches in the student network with mask tokens and train the student to match the features of the teacher at masked locations. The loss is then defined identically to the first term (consistency loss), but applied to per-patch features rather than the pooled, image-level representation. Further, both the student and the teacher see the same, global view (up to masking in the student).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training with self-distillation and masked prediction", "weight": 1.0} -->

We add these losses at 80% of training completion, initializing the teacher with the student parameters and the remaining additional parameters (heads, mask token and corresponding optimizer parameters) randomly. We use the original image for computing the SigLIP and LocCa losses from the previous section and apply the additional losses on additional augmented views. This is done to ensure that data augmentation does not negatively impact the image-text alignment as recommended. The weights of the first and the second loss terms are set to 1 and 0.25. Further, to balance model quality on global/semantic and dense tasks, we re-weight the two loss terms by another factor of 0.25, 0.5, 1.0, and 0.5 for the B, L, So400m and g, model sizes, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Fixed-resolution variant", "weight": 1.0} -->

To obtain fixed-resolution checkpoints at multiple resolutions, we resume the checkpoints (with sequence length 256 and patch size 16) at 95% of training, resize the positional embedding to the target sequences length (and in some cases the patch embedding from patch size 16 to 14 with the pseudoinverse (PI)-resize strategy from ), and resume the training at the target resolution with all losses. We opt for this approach as the common strategy of fine-tuning the final checkpoint with smaller learning rate and without weight decay did not lead to good results across all sizes and resolutions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Variable aspect and resolution (NaFlex)", "weight": 1.0} -->

NaFlex combines ideas from FlexiViT, i.e. supporting multiple, predefined sequence lengths with a single ViT model, and NaViT, namely processing images at their native aspect ratio. This enables processing different types of images at appropriate resolution, e.g. using a larger resolution to process document images, while at the same time minimizing the impact of aspect ratio distortion on certain inference tasks, e.g. on OCR.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Variable aspect and resolution (NaFlex)", "weight": 1.0} -->

Given a patch size and target sequence length, NaFlex preprocesses the data by first resizing the input image such that the height and width after resizing are multiples of the patch size, while 1) keeping the aspect ratio distortion as small as possible and 2) producing a sequence length of at most the desired target sequence length. The resulting distortion in width and height is at most (patch_size-1)/width and (patch_size-1)/height, respectively, which tends to be small for common resolutions and aspect ratios. Note that NaViT incurs the same type of distortion. After resizing, the image is split into a sequence of patches, and patch coordinates as well as a mask with padding information is added (to handle the case where the actual sequence length is smaller than the target length).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Variable aspect and resolution (NaFlex)", "weight": 1.0} -->

To process different sequence lengths (and aspect ratios) with a ViT, we bilinearly resize (with anti-aliasing) the learned positional embedding to the target, non-square patch grid for the resized input image. We set the length of the learned positional embedding to 256, assuming a $16\times 16$ patch grid before resizing. When the sequence length after resizing is smaller than the target sequence length, the attention layers (including the MAP head) are masked to ignore the extra padding tokens.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Variable aspect and resolution (NaFlex)", "weight": 1.0} -->

As for the fixed-resolution, adapted variants, we start from the default checkpoints trained with the setup described in Sec. 2.2, i.e. with non-aspect preserving resize to 256px, resulting in a sequence length of 256. We take the checkpoint at 90% training completion, then switch to aspect-preserving resizing and uniformly sampling a sequence length from $\{128,256,576,784,1024\}$ per mini-batch. At the same time we stretch the learning rate schedule corresponding to the last 10% by a factor $3.75$ to ensure that each resolution is trained for sufficiently many examples. For the largest sequence length we further half the batch size and double the number of training steps to avoid out-of-memory errors.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Variable aspect and resolution (NaFlex)", "weight": 1.0} -->

To keep implementation and computation complexity manageable, we do not apply self-distillation and masked prediction from Sec. 2.3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Distillation via active data curation", "weight": 1.0} -->

To maximize performance of the smallest fixed-resolution models (ViT-B/16 and ViT-B/32), we distill knowledge from a teacher (reference) model during a short fine-tuning stage. We lower the learning rate to $10^{-5}$, remove weight-decay, and continue training these models for an additional 4B examples using just the sigmoid image-text loss. During this stage, we perform implicit "distillation through data" using the ACID method proposed. Briefly, at every training step, the teacher model and the current learner model are used to score examples by their "learnability". These scores are then used to jointly select an optimal batch of size 32k from a larger super-batch. Here, we select data with a filtering ratio of 0.5 (i.e. super-batch size of 64k) to balance gains from curation with training compute. For the B/32 model, we find leveraging a filtering ratio of 0.75 is worth the extra cost.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Distillation via active data curation", "weight": 1.0} -->

We note that the authors in suggest that the best performance is achieved with ACED, a method that combines ACID with explicit softmax-distillation (using a second teacher trained on more diverse data). However, here we propose a way to adapt ACID to capture these benefits without the need for explicit distillation, saving significant amounts of compute. Specifically, instead of utilizing two separate teacher models, we take a single strong teacher trained on the diverse data (in this case, the SigLIP 2 So400m model) and fine-tune it for 1B examples on the high-quality curated dataset. We then use this fine-tuned teacher model in the ACID method, as described above. Because this teacher blends diverse knowledge of concepts from pretraining, with knowledge of what is high-quality (from the curated dataset), the implicit distillation of ACID alone is sufficient to recover the benefits of ACED.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Zero-shot classification and retrieval", "weight": 1.0} -->

In Table 1 we report the performance of SigLIP 2 along with baselines on common zero-shot classification (ImageNet ObjectNet, ImageNet-v2, ImageNet ReaL ) and image-text retrieval benchmarks. SigLIP 2 performs better than SigLIP and other (open-weight) baselines across the board, despite supporting many languages unlike the baselines (except mSigLIP ). Note that DFN, which comes closest to SigLIP 2 on these benchmarks, uses a network fine-tuned on ImageNet, COCO, and Flickr (i.e. the main benchmarks in Table 1) as a filter to improve data quality. SigLIP 2's improvements over the baselines are particularly significant for the B-sized models owing to distillation (Sec. 2.5). Moreover, we observe the common scaling trends as a function of image resolution and model size.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Zero-shot classification and retrieval", "weight": 1.0} -->

Table 1 and Figure 2 ‣ 2.4 Adaptation to different resolutions ‣ 2 Training recipe ‣ SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features") further show the multilingual retrieval performance on Crossmodal-3600 (XM3600) covering 36 languages. SigLIP 2's recall exceeds that of SigLIP by a large margin, while only lagging slightly behind mSigLIP, which in turn performs substantially worse than SigLIP and SigLIP 2 on English-focused benchmarks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "NaFlex variant", "weight": 1.0} -->

Fig. 3 ‣ 2.4 Adaptation to different resolutions ‣ 2 Training recipe ‣ SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features") compares the fixed-resolution square-aspect ratio (standard) SigLIP 2 with the aspect-preserving NaFlex variant (one checkpoint for all sequence lengths) as a function of the sequence length. In addition to the retrieval benchmarks listed in the previous section, we add a range of OCR/document/screen-focused image-text benchmarks, namely TextCaps, HierText, SciCap and Screen2Words. The NaFlex variant outperforms the standard variant on the majority of these retrieval benchmarks, in particular for small sequence lengths (and hence resolutions) which tend to suffer more from aspect ratio distortion. On benchmarks predominantly based on natural images, the standard B-sized variant outperforms NaFlex, arguably thanks to the distillation step, whereas for the So400m architecture the two are on par. This is remarkable since the standard variant also benefits from the self-distillation stage (Sec. 2.3).

<!-- chunk {"id": "body-0037", "role": "body", "section": "SigLIP 2 as a vision encoder for VLMs", "weight": 1.0} -->

A popular use case for vision encoders like CLIP and SigLIP is to extract visual representations for VLMs. The common paradigm combines a pretrained vision encoder with a pretrained LLM and does multimodal training on a rich mixture of vision language tasks. To evaluate the performance of SigLIP 2 in this application, we develop a recipe similar to that of PaliGemma 2. Concretely, we combine SigLIP 2 vision encoders and baselines with the Gemma 2 2B LLM and train the LLM on 50M examples of the Stage 1 training mix from involving captioning, OCR, grounded captioning, visual question answering, detection, and instance segmentation (the annotations for the last 4 tasks are machine-generated, see \[7, Sec. 3.2.5\] for details). We keep the vision encoder frozen (which has essentially no impact on quality \[7, Sec. 5.4\]) and reduce training duration to reflect a typical open model use case. The resulting VLM is then fine-tuned on a broad range of downstream tasks with the transfer settings.

<!-- chunk {"id": "body-0038", "role": "body", "section": "SigLIP 2 as a vision encoder for VLMs", "weight": 1.0} -->

To understand the effect of the input resolution we perform experiments at resolution 224 or 256 (for models with patch size 14 and 16, respectively, to extract 256 image tokens) and 384px, but unlike we repeat stage 1 at 384px rather than starting from the 224px variant.

<!-- chunk {"id": "body-0039", "role": "body", "section": "SigLIP 2 as a vision encoder for VLMs", "weight": 1.0} -->

Fig. 4 shows the results after fine-tuning for each dataset. Overall, SigLIP 2 clearly outperforms SigLIP across resolutions and model size. For an L-sized vision encoder, SigLIP 2 also outperforms the recently released AIMv2 model. The data from Fig. 4 can also be found in Table 6.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Semantic segmentation, depth estimation, surface normal estimation", "weight": 1.0} -->

We adopt the evaluation protocol from and probe the frozen SigLIP 2 representation, either with a linear layer or with a DPT decoder, on six benchmarks spanning semantic segmentation, monocular depth estimation, and surface normal estimation (see \[38, Sec. 4.1\] for details on the protocol and hyper parameters). Note, we make one (necessary) change: where the original method concatenates the CLS token to each of the patch feature vectors, we concatenate the output embedding of the MAP head instead, as we use a MAP head instead of a CLS token. The results in Table 2 indicate that SigLIP 2 outperforms several previous open, CLIP-style vision encoders, including SigLIP, often by a significant margin.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Open-vocabulary segmentation", "weight": 1.0} -->

Open-vocabulary segmentation aims to develop models that can segment any novel classes beyond a fixed training vocabulary. Here, we evaluate SigLIP 2's performance on this task. We use Cat-Seg as a framework and compare performance across different models as proposed. We train Cat-Seg on COCO-Stuff-164k with 172 classes and then test it on various representative datasets with different vocabularies: with 847 or 150 classes (A-847/A-150), Pascal Context (PC-459/PC-59), and Pascal VOC (VOC-20/VOC-21). The results can be found in Table 3. We observe that the SigLIP 2 at L/16 improves on SigLIP and even surpasses the much bigger OpenCLIP G/14 model.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Referring expression comprehension", "weight": 1.0} -->

To probe the referring expression comprehension capabilities of SigLIP 2 on different RefCOCO variants we apply the evaluation protocol. We attach a 6-layer transformer decoder to the un-pooled, frozen vision encoder representation via cross-attention and train it from scratch on a mix of all RefCOCO variants (see for details). The results in Table 5 show that SigLIP 2 outperforms SigLIP as well as CLIP and pretraining via image captioning (Cap) by a large margin, across resolutions and model sizes. This can be attributed to the decoder-based pretraining, as described in Sec. 2.2. SigLIP 2 is only outperformed LocCa, which we hypothesize might be due to the fact that SigLIP 2 is pretrained on multilingual data. LocCa, on the other hand, is trained on text only from English web sites. Finally, note that we expect significant improvements when using the decoder from pretraining as observed for LocCa.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Open-vocabulary detection", "weight": 1.0} -->

OWL-ViT is a popular method to adapt CLIP-style vision-language models to open-vocabulary detection. Here, we apply this approach to SigLIP and SigLIP 2 models, closely following the data and optimizer configuration. The results in Table 4 show that SigLIP 2 achieves better performance than SigLIP on the two popular benchmarks COCO and LVIS. The relative improvement is most pronounced for the LVIS rare categories. Further, the results here are better than those in which is likely because used CLIP rather than SigLIP.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Cultural diversity and fairness", "weight": 1.0} -->

Besides the improvement in model quality in SigLIP 2 compared to its predecessor, SigLIP 2 is also more inclusive in two aspects. First, we follow the recommendations of and utilize a training mixture comprising both English and multilingual data to enhance cultural diversity. Second, to address potential societal biases in the training data, we integrate the data de-biasing techniques. These techniques are applied to mitigate biases in both first-order statistics, such as disparities in gender representation, and second-order statistics, such as biased associations between gender and occupation. Next, we present the evaluation results.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Cultural Diversity", "weight": 1.0} -->

To evaluate for cultural diversity, we report the zero-shot classification accuracy results using Dollar Street, GeoDE, and Google Landmarks Dataset v2 (GLDv2). We also include 10-shot geolocalization using Dollar Street and GeoDE, as proposed. For zero-shot evaluation on Dollar Street, we implement the methodology outlined, mapping 96 topics within the dataset to corresponding ImageNet classes. This process results in a subset of 21K images for our analysis.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Cultural Diversity", "weight": 1.0} -->

Fig. 5 shows a set of representative results (full results are shown in Appendix C). We observe an improvement in these metrics in SigLIP 2 compared to SigLIP for the same model size and resolution, and the improvements are particularly significant in geolocalization tasks. For instance, 10-shot geolocalization accuracy in GeoDE (region) improves from 36.2% for SigLIP L/16 at 256px to 44.4% in SigLIP 2. Similarly, 0-shot accuracy on Dollar Street improves from 52.1% to 55.2% in the same models.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Fairness", "weight": 1.0} -->

In terms of fairness, we report two metrics. The first is "representation bias," as defined, which measures the tendency in the model to associate a random object (such as cars) with a particular gender group. As shown in Fig. 6, SigLIP 2 is *significantly* better than SigLIP. For instance, while SigLIP L/16 at 256px has a representation bias of about 35.5%---meaning it prefers to associate random images with "men" over "women" more than 85.5% of the time---SigLIP 2 of the same size and resolution has a representation bias of 7.3% only. In addition, larger models tend to exhibit less representation bias than smaller models, in agreement with the earlier findings.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Fairness", "weight": 1.0} -->

We also investigate the Dollar Street 0-shot results by income level and the GeoDE results by geographic region as. However, in this context we only observe very minor benefits, or no benefits when comparing SigLIP and SigLIP 2 models of matching size and resolution (some results shown in Table 9).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduced SigLIP 2, a family of open-weight multilingual vision-language encoders that builds on the success of SigLIP. By incorporating a combination of techniques such as decoder-based pretraining, self-supervised losses, and active data curation, SigLIP 2 achieves significant improvements in zero-shot classification, transfer performance as a vision encoder in VLMs, and in localization and dense prediction tasks. Furthermore, thanks to training on multilingual data and applying de-biasing filters, SigLIP 2 attains more balanced quality across culturally diverse data. Finally, the NaFlex variant enables the model to support multiple resolutions with a single model checkpoint, while preserving the native image aspect ratio. We hope that our SigLIP 2 release will enable many exciting applications within the open-source community.
