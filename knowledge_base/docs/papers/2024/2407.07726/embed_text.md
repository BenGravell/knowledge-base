## Introduction

Figure 1: PaliGemma’s architecture: a SigLIP image encoder feeds into a Gemma decoder LM.

PaliGemma is an open model, continuing the line of PaLI vision-language models in a combination with the Gemma family of language models.

PaLI is a series of state-of-the-art vision-language models, starting with the first PaLI showing promising scaling results up to 17 B, using classification pretrained ViT and mT5 language model. PaLI-X and PaLM-E then pushed this further, combining ViT-22 B and a 32 B UL2 language model or the 540 B PaLM language model, respectively, and getting further increased performance on vision-language tasks, albeit saturating performance on standard image classification and retrieval tasks. Finally, PaLI-3 demonstrates that through better pretraining with SigLIP and more careful multimodal data curation, a 2 B vision and 3 B language model (*i.e*. a 5 B vision-language model) matches the 10x larger PaLI-X and 100x larger PaLM-E across most benchmarks.

PaliGemma continues this trend, combining the 400 M SigLIP and the 2 B Gemma models into a sub-3 B VLM that still maintains performance comparable to PaLI-X, PaLM-E, and PaLI-3.

Gemma is a family of auto-regressive decoder-only open large language models built from the same research and technology used to create the Gemini models. The models come in different sizes (2 B, 7 B), both pretrained and instruction fine-tuned. PaliGemma uses the 2 B pretrained version.

The main goal of our work is to provide a versatile base VLM. Hence, we show that it reaches state-of-the-art results not only on standard COCO captions, VQAv2, InfographicVQA and others, but also on more exotic Remote-Sensing VQA, TallyVQA, several video captioning and QA tasks, as well as referring expression *segmentation* (see full task list in Appendix B).

## Related work

Over the course of the past few years, vision-language models have gained considerable importance in computer vision. The first generation, spearheaded by CLIP and ALIGN by scaling up ConVIRT and VirTex, is an extension of large-scale classification pretraining, to leverage all data from the web without the need for onerous human labeling, replacing a fixed and large set of classes by a caption embedding instead. The caption embeddings are mostly obtained using language encoders (similar to BERT ) and allow to open up the vocabulary of classification and retrieval tasks. The second generation, akin to T5 in language, is a unification of captioning and question-answering tasks via generative encoder-decoder modeling, often backed by the progress in generative language models. These were then further scaled up , among others, Flamingo, BLIP-2 and, PaLI. Finally, most recent works perform an additional "instruction tuning" step that is intended to make the raw model more user-friendly. In addition to building systems, several recent more systematic studies aim to find out what really matters in VLMs. PaliGemma is an open base VLM without instruction tuning, and this report answers a few more questions regarding what matters. More discussion in Appendix A.

## Model

In this section we present details about PaliGemma's architecture and training. Several of our decisions are further ablated in Section 5.

At a high level, PaliGemma is a VLM, taking as input one or more images, and a textual description of the task (the prompt or question, which we often refer to as the prefix). PaliGemma then autoregressively generates a prediction in the form of a text string (the answer, which we often refer to as the suffix).

This simple image+text , text out API is flexible enough to cover many standard tasks, such as image classification, captioning, visual question-answering and dialogue. Additionally, as shown in the literature, by converting more complex structured outputs into "text", this API can also cover more tasks such as: detection, instance segmentation, panoptic segmentation, depth prediction, colorization, and many more. This conversion can be hand-engineered and task-specific, such as done in pix2seq for detection, or learned as is the case for segmentation and dense output tasks in general.

During PaliGemma's pretraining, we limit ourselves to "text" covering natural language, object detection, and instance segmentation, but this API remains versatile and the pretrained models can be finetuned for other output types.

### Architecture

PaliGemma consists of three components: An image encoder, for which we use a publicly available SigLIP checkpoint, specifically the "shape optimized" ViT-So400m image encoder. This model was contrastively pretrained at large scale via the sigmoid loss, and has shown state-of-the-art performance, especially for its small size.

A decoder-only language model, for which we use the publicly available Gemma-2B v1.0 raw pretrained checkpoint, which strikes a great balance between performance and size. As we will show, this language model is good enough to match or surpass the performance of VLMs using much larger language models, including previous PaLIs.

A linear layer projecting SigLIP's output tokens into the same dimensions as Gemma-2B's vocab tokens, so they can be concatenated. In early experiments, we found that more complicated alternatives (*e.g*. MLPs) do not provide a clear advantage, and hence decided to use the simplest option (Sec 5.5).

The image is passed through the image encoder, which turns it into a sequence of $N_{\text{img}}$ tokens. The text is converted into $N_{\text{txt}}$ tokens using Gemma's SentencePiece tokenizer, and embedded with Gemma's vocabulary embedding layer. The image tokens are projected with the (zero initialized) linear projection. Then the sequence of input tokens to the decoder is created as follows (and also as visible in Figure 2): tokens = [image tokens..., BOS, prefix tokens..., SEP, suffix tokens..., EOS, PAD...]

Figure 2: PaliGemma’s Prefix-LM masking: block attention throughout image and prefix, autoregressive attention on the suffix. Each square indicates whether the row can attend to the column.

We always resize the image to a fixed square size (224, 448, or 896 pixels). This leads to a fixed number of image tokens per model variant (respectively 256, 1024, or 4096 tokens), which we place in the front, making image tokens straightforward to interpret without the need for special location markers. The BOS token then marks the start of text tokens. We use \\n as SEP token, it does not appear in any of our prefixes. We also tokenize SEP separately to avoid it being merged (by the tokenizer) with either the end of the prefix or the beginning of the suffix. In order to maximize model capacity for such a small model, we have full (unmasked) attention on the whole input, *i.e*. the image and prefix tokens. In this way, image tokens can also \"lookahead\" at the task at hand (prefix) in order to update their representation. The suffix is our output and necessarily covered by an auto-regressive mask, including the PAD tokens. When we mention sequence length ($N_{\text{txt}}$), we typically mean prefix and suffix combined, ignoring image tokens.

### Pretraining

The training of PaliGemma follows the same steps as previous PaLI models, with only small modifications. Training consists of several stages, which we detail in this section: Stage0: Unimodal pretraining - we use existing off-the-shelf components.

Stage1: Multimodal pretraining - long pretraining on a carefully chosen mixture of multimodal tasks. Notably, nothing is frozen.

Stage2: Resolution increase - short continued pretraining at higher resolution.

Stage3: Transfer - turn the base model into a task-specific specialist.

### Stage0: Unimodal pretraining

First, the unimodal components of the model are pretrained individually, in order to benefit from their well-studied and scaled training recipes. For PaliGemma specifically, we do not perform any custom unimodal pretraining, instead relying on existing publicly available checkpoints.

Following PaLI-3's strong experimental results, we use a SigLIP image encoder. While PaLI-3 (and others ) use a large image model such as ViT-G, we use the much smaller but similarly strong "shape optimized" ViT-So400m model.

PaLI traditionally uses an encoder-decoder language model; however all recently publicly released language models are decoder-only Transformers. We opt for the Gemma-2B model, which strikes a good balance between size and performance. Larger language models, such as the popular 7 B or 70 B sizes, are often significantly better at tasks like mathematical reasoning. However, PaLI-3 has shown that across a wide range of vision-language tasks, a well-trained small 5 B model (2 B vision + 3 B language) can attain the same performance as the much larger 55 B PaLI-X (22 B vision + 32 B language) and 562 B PaLM-E (22 B vision + 540 B language), including tasks such as ScienceQA. With PaliGemma we continue this push for smaller models and show that we can keep the same performance with less than 3 B total parameters.

### Stage1: Multimodal pretraining

In this stage, we combine the unimodal models as explained in Section 3.1 and train the whole model on a broad mixture of large-scale vision-language tasks. Contrary to most recent VLMs, our core goal is to train a base model that fine-tunes well to a wide range of tasks, not merely to align the modalities. Intuitively, we want a mix of tasks which force the model to acquire a broad range of "skills", regardless of the task's user (or benchmark) friendliness out of the box. More on this in Section 3.2.5.

It is common practice, also followed by previous PaLI versions, to keep the image encoder frozen during the first multimodal pretraining stage. This is partially due to findings as in LiT reporting multimodal tuning of pretrained image encoders degrading their representations. However, more recent work such as CapPa and LocCa have shown that captioning and other harder-to-learn tasks can provide valuable signal to image encoders, allowing them to learn spatial and relational understanding capabilities which contrastive models like CLIP or SigLIP typically lack. Hence, again in the spirit of learning more skills during pretraining, we depart from common practice and do not freeze the image encoder. However, the challenges outlined in LiT remain. In order to avoid destructive supervision signal from the initially unaligned language model, we use a slow linear warm-up for the image encoder's learning-rate (Figure 3), which ensures that the image encoder's quality is not deteriorated from the initially misaligned gradients coming through the LLM.

We train Stage1 at resolution 224px (hence, $N_{\text{img}} = 256$ image tokens) and sequence length $N_{\text{txt}} = 128$ for a total of 1 billion examples. While we provide an ablation in Section 5.1 showing that a 10x to 30x shorter Stage1 still provides good results on popular benchmarks, we wish to imbue as much visual knowledge to the base model as possible, and cover a broad set of concepts, cultures, and languages.

### Stage2: Resolution increase

The model resulting from Stage1 is already a useful base model for many tasks (see example images in Appendix B). However, it only understands images at $224 \times 224$ pixel resolution, which is too small for several tasks. For instance, detection and segmentation of smaller objects, and tasks related to reading smaller texts such as charts, infographics, or documents, all strongly benefit from higher resolution (see Table 1). Hence, we train two further model checkpoints for increased resolution, first to $448 \times 448$ and then to $896 \times 896$ pixel resolution.

Since stage1 took care of providing the model with a broad set of knowledge and skill, stage2 can focus on extending the model's ability to parse higher-resolution images. We thus run Stage2 with fewer total examples, while increasing the cost and information density of each example. For resolution 448, we train for an additional 50 M examples, and for resolution 896, we add another 10 M examples.

For simplicity, Stage2 consists of the exact same mixture of tasks and datasets as Stage1, but with significantly increased sampling of tasks that require high resolution. Additionally, these upweighted tasks all can be modified to provide much longer suffix sequence lengths. For instance, for OCR tasks, we can simply request the model to read *all* text on the image in left-to-right, top-to-bottom order. For detection and segmentation tasks, we can request the model to detect or segment *all* objects for which annotation is provided. Hence, we also increase the text sequence length to $N_{\text{txt}} = 512$ tokens.

While PaLI has always had this resolution increasing stage, and for image classification the importance of resolution is long known, several recent works have raised the importance of resolution in VLMs too. We add to this body of knowledge by providing several ablation studies regarding Stage2 in Section 5.7.

### Stage3: Transfer

The result of Stages 1 and 2 is a family of three PaliGemma checkpoints, at 224px, 448px, and 896px resolution, which are pre-equipped with broad visual knowledge. However, these checkpoints are not "user (or benchmark) friendly" as their pretraining has focused solely on density of learning signal, as opposed to usable interface.

These base models need to be transferred to serve their intended final purpose. That could take the form of fine-tuning on a specific, specialized task, such as COCO Captions, Remote Sensing VQA, Video Captioning, or InfographicQA. Adapt to new inputs such as multiple images (NLVR2) or bounding boxes draw in the image (WidgetCap). Or it could take the form of instruction or even chat tuning.

To show the effectiveness of the base models, we transfer them to a wide range of individual academic benchmarks, using a simple unified transfer recipe with few hyper-parameters. And to showcase the versatility beyond academic tasks, we also provide a "mix" transfer checkpoint, which transfers to a subset of these tasks at the same time, along with detailed captioning and long question-answering data. While this is not instruction tuning, it is a step in that direction.

We also transfer PaliGemma to tasks which take multiple images as input. NLVR2 is one such task, which asks one question about two images, and requires looking at both to give the correct answer. Other such tasks are standard short-video understanding tasks subsampled to 16 frames. In all these cases, we follow PaLI-3 and encode each image separately, then concatenate the image tokens without any special separator or embedding tokens. Thus, 16 frames at 224px resolution result in $N_{\text{img}} = 4096$ image tokens, the same amount as a single image at 896px resolution.

For all transfers, we perform fine-tuning of all the model parameters. The hyper-parameters we modify per-task are the following, in decreasing order of importance: Dropout in the LLM: 0.0, 0.1, 0.3.

Weight decay: 0.0 or 0.1 $\times$ learning-rate.

Freeze ViT: false, true.

Beam-search may benefit captioning.

The above are typical values we suggest exploring, with the recommended initial attempt value in bold. We provide the best setting for each individual task in Appendix J. We study the sensitivity to transfer hyper-parameters in Section 6.2, and the "transferability" in general in Section 6, showing that good results can be achieved with the aforementioned initial attempt values.

### Pretraining task mixture

Just like for previous PaLI models, the pretraining (Stage1 and Stage2) is designed to result in a model that transfers well, not necessarily a model that is usable out of the box ("0 shot"). The intuition here is that we want a mix of tasks which force the model to acquire a broad range of "skills". We prefix each task with its unique prefix to avoid conflicting learning signals across skills. At transfer time (Stage3), the model then merely needs to recognize which skill is useful for the task, and rewire itself to use that while following the output syntax and vocabulary of the task. In our experience, these can all be done relatively quickly and based on few examples (Section 6.3). We do not use any of our transfer datasets during pretraining, and furthermore remove all near-duplicates of their images from the pretraining datasets.

Largely following previous PaLI works, these are the pretraining tasks: We include the simple captioning objective on various datasets, including WebLI in over 100 languages, and CC3M-35L. Previous PaLIs use an encoder-decoder language model with the SplitCap objective, however for PaliGemma with the decoder-only language model, plain captioning is a more informative and simpler objective.

Concatenation (in raster order) of all text on the image transcribed by a public OCR system. Potentially skipping random snippets of OCR in order to fit sequence length without biasing recognition towards the beginning of raster order.

Generated VQA on CC3M-35L following with questions in 35 languages but English answers. Additionally, English-only object-centric questions on OpenImages following:\listing: What objects are in the image?,\presence: Is {thing} in the image?,\multi-object presence: Which of {thing}, {thing}\... are in the image?,\and newly, counting: How many {thing}?. question {lang} {English answer}\Generated VQG on CC3M-35L following generating questions in 35 languages, for a given English answer. detect {thing}; {thing}; \...\Multi-object detection similar to Pix2Seq on generated open-world data via pseudo-labeling as described in OWL-ViTv2. segment {thing}; {thing}; \...\Multi-object instance segmentation as in PaLI-3 on generated open-world data similar to OWL-ViTv2 and SAM. caption \<ymin\>\<xmin\>\<ymax\>\<xmax\>\Grounded captioning of what is in the box, following LocCa. The box is indicated by the same location tokens as used in detection and segmentation: normalized image coordinates binned to 1024 tokens.

Notably distinct from the widely used LLaVa's GPT-4 generated instruction following data, none of PaliGemma's pretraining tasks is the output of a larger commercial VLM.

Finally, we believe that it is important to detect and remove all images in our pretraining datasets which are near-duplicates of images in the transfer tasks we evaluate in this report, as well as a few more popular computer vision benchmarks. Doing so, we more accurately capture PaliGemma's capability to transfer to new tasks.

### Other pretraining details

Figure 3: Learning-rate schedule across stages.

Throughout pretraining, we use an \"infinite\" learning-rate schedule following, which provides a straightforward way of chaining several stages without decaying the learning-rate between them. Figure 3 shows the full schedule: pretraining is one continuous rsqrt curve for all stages. The transfer can then act as a cooldown, fully annealing the learning rate. We recommend transferring with a simple setup that tunes the full model using a cosine learning-rate schedule with a short linear warm-up and decaying to zero. This is not well represented by Figure 3 due to its comparatively short duration.

The model was entirely trained in the open-source big_vision codebase on Cloud TPUv5e. However, some of the pretraining datasets remain private. During training, we partition data, as well as model parameters and optimizer state (Zero-DP style ) across all available devices using JAX with GSPMD. This fully-sharded data-parallel (FSDP ) sharding strategy is achieved by constructing global arrays and annotating the sharding accordingly, with the XLA compiler taking care of the concrete implementation of the computation and communication between devices. We measured a model FLOPS utilization (MFU) of 55%, resulting in 5189 tokens/second/device. Model parameters and optimizer state are kept in float32 to guarantee stable training, but we verified that inference works just as well with bfloat16 model parameters.

One training run of the final PaliGemma model using TPUv5e-256 takes slightly less than 3 days for Stage1 and 15h for each Stage2. Stage1 sees slightly less than 350 B tokens, and both Stage2 combined about 90 B tokens. Transfers take between 20min and 10h on TPUv3-32, depending on the task.

In order to avoid model brittleness to different image processing details in different frameworks, we randomize the image preprocessing details such as resize method, JPEG encoding, and apply very slight inception_crop.

## Results

Visual question answering Table 1: Results (1 random run of 5) obtained with PaliGemma. Tasks marked with ⌞ indicate zero-shot evaluation of the transferred model above. Where numbers depend on server submissions we report standard deviation from validation splits. Highlighted rows indicate resolution sensitive tasks. Per-task details and hyper-parameters are in Appendix B and J.

In order to verify the transferability of PaliGemma to a wide variety of tasks, we transfer the pretrained models on more than 30 academic benchmarks via fine-tuning. Importantly, none of these tasks or datasets are part of the pretraining data mixture, and their images are explicitly removed from the web-scale pretraining data. Results are presented in Table 1.

To select the hyper-parameters for transfer, we first sweep the parameters mentioned in Section 3.2.4, starting from the recommended value. We do not necessarily perform the full cross-product, and we sometimes extend or supersample the range, if it seems promising. Importantly, we make any such decisions and hyper-parameter choices based on the transfer task's validation split, and if none is provided, we hold out a small "minival" set from the training data. Once we found good hyper-parameter values for a task, we re-train using the full training and validation data, and report final test numbers. Details on tasks, metrics, data splits are in Appendix B and final hyper-parameters in Appendix J. In Section 6.2 we show that a single recommended value for each hyper-parameter without any exploration works almost as well on most tasks.

For all but video tasks, we report results on at least two resolutions to provide an impression of which tasks benefit from increased resolution. We provide many resolution-related ablations in Section 5.7.

Notably, we have not found any significant benefit from data augmentation. We simply resize the input images to a square fixed resolution, even for tasks such as RefCOCO segmentation (more on that in Section 5.7 and Appendix C).

## Ablations

We conduct diverse ablations to gain deeper understanding of what matters for training and transferring VLMs. Unless noted otherwise, all ablations are run with the same setup as the main models, except for making the Stage1 pretraining 10x shorter (*i.e*. 100 M examples seen), and transfer results are reported on validation sets instead of withheld test-sets. For each experiment, we present only the salient result summary in the main text, but we provide a full per-task breakdown of results in the Appendix.

### Multimodal pretraining duration

Figure 4: Relative regret of transfers when varying the amount of pretraining during Stage 1. Per task plot in appendix LABEL:sec:app:pt_duration.

With its 1 B examples seen, our multimodal pretraining (Stage1) is on the longer side, similar to BLIP-2, InternVL, QwenVL, Idefics2 (all around 1 B), but unlike ShareGPT4-v, Mini-Gemini, LLaVa and its derivatives (around 1 M).

To the best of our knowledge, the benefits from longer pretraining have not been studied in isolation. We run pretrainings of various shorter durations, all the way down to completely skipping Stage1, and show the impact in Figure 4, with a complete break-down across tasks in the Appendix LABEL:sec:app:pt_duration. For the case of skipping Stage1, we use the best transfer result when sweeping over three learning-rates for each task.

The result shows that shorter training generally hurts, and skipping Stage1 entirely is the worst setting. Some task are affected significantly, while others only deteriorate a little, highlighting the need for a broad and diverse set of evaluation tasks. The $100$M pretraining duration appears to be a good trade-off for ablations: it is 10x shorter while not significantly hurting any task.

### Causal masking and learning objective

Figure 5: Learning setup for Stage1. Left: Where to apply the auto-regressive mask and loss. Middle and right: whether to include a task indicator.

We ablate several of our key choices in the pretraining learning objective in Figure 5, full per-task breakdown in Appendix LABEL:sec:app:learning.

First, we investigate design choices for auto-regressive masking. PaliGemma uses a prefix-LM strategy which allows full (bi-directional) attention on the "input" part of the data, *i.e*. the image and prefix tokens, see also Figure 2. The motivation is that it allows more tokens to actively participate in the "thinking" process from the start, as the image tokens now can attend to the prefix tokens which represent the query. This is empirically confirmed in Figure 5 (left), where the green bars also include the auto-regressive masking on the prefix tokens, and the orange bars further extend the auto-regressive mask to the image tokens. Both sets of bars work, but perform clearly worse than PaliGemma's prefix-LM setting represented by the blue bar.

Second, we apply the next-token-prediction loss on the suffix (the output) only. In principle, it can also be applied on the prefix tokens, once they are auto-regressively masked. This could provide more learning signal to the model by asking it to "guess the question" for example. Again, Figure 5 shows that while it works, doing so clearly reduces average performance.

Finally, we eased the multi-task learning by using task-prefixes. Figure 5 (middle) shows that after transfers, this choice of pretraining has no noticeable effect. However, it would be incorrect to conclude that it has no effect on the model's training. Indeed, pretraining validation perplexities on three representative tasks of pretraining are shown in Figure 5 (right): when the prefix makes the task obvious, such as in VQA, a task-prefix has no effect. For tasks where the prefix does not perfectly disambiguate the exact task, however, the model (expectedly) does become noticeably more uncertain in its predictions without task-prefix.

Overall, the prefix-LM with task-prefix and supervision only on the suffix tokens is an effective VLM pretraining objective.

### New token initialization

Figure 6: Initialization of new tokens matters. Left: distribution of embedding norms at init. Right: Top: initial loss is better with AvgEmb, but this changes after a few thousand steps. Bottom: the model pretrained with σ = 0.02 inits transfers better to a task heavily using the new tokens.

We add new tokens to Gemma's vocabulary to support PaliGemma's ability to perform more structured computer vision tasks. We add 1024 location tokens (\<loc0000\> to \<loc1023\>), which correspond to binned normalized image coordinates and are used in detection, referring expression, and grounded captioning tasks. We also add 128 VQVAE tokenized single-object mask tokens (\<seg000\> to \<seg127\>) to support referring expression segmentation.

This poses the question of how to initialize the embeddings of these new tokens, given all other vocabulary tokens have already been trained as part of Gemma's pretraining. One option is to use a standard small Gaussian noise initialization ($\sigma = 0.02$, blue in Fig 6). However, argues for matching the average of the pretrained embeddings plus small noise (AvgEmb, mauve in Fig 6). We compare these strategies in Figure 6 and see that, while the AvgEmb strategy significantly improves initial perplexity of tasks using the new tokens (top-right zoom-, step 0), this gain vanishes after a thousand steps of training. The standard initialization strategy not only results in significantly better Stage1 perplexities at the end of pretraining (top-right, full plot), but also results in significantly better transfer of the model to tasks using these tokens, here RefCOCO segmentation MIoU (bottom right).

### To freeze or not to freeze?

The current common wisdom in VLMs is to keep the image encoder and sometimes the LLM frozen during multimodal pretraining (our Stage1). However, inspired by the positive results from CapPa and LocCa which show that pretraining an image encoder using captioning objectives essentially solves contrastive's blind spot to relation and localization, we pretrained PaliGemma with no frozen parts. We now ablate the effect of freezing or tuning various parts of the model during Stage1 in Figure 7, full per-task breakdown in Appendix LABEL:sec:app:freeze. Similar to concurrent works, we find not freezing any part of the model is indeed advantageous. First, after transfers, there is no difference to keeping the image encoder frozen (left, TT and TF). Second, however, the validation perplexity (hence, predictability) of tasks requiring spatial understanding (right, green) is significantly improved.

Further, we show that all other options that include freezing the language model are significantly worse. Finally, resetting (and training, R) any part of the model hurts performance dramatically, confirming that Stage0 (*i.e*. leveraging pre-trained components) is indeed crucial for attaining good results.

Figure 7: Training setup for Stage1. Left: The more is frozen or reset, the more performance deteriorates. Right: The effect of freezing ViT is most visible in some pretraining perplexities.

### Connector design

Throughout our experiments we use a linear connector to map SigLiP output embeddings to the inputs of Gemma. Given that an MLP connector is a popular choice in the VLM literature, we also ablate this choice.

We consider two connector choices: a linear connector and an MLP (1 hidden layer, with GeLU non-linearity). We also consider two Stage1 pretraining settings: tune all weights (TT), or freeze everything but the connector (FF).

When tuning all weights, average transfer score is nearly identical for linear vs MLP, achieving $77.2$ and $77.1$ points respectively. In the "all-frozen" scenario, linear vs MLP achieve $70.7$ vs $69.7$. Surprisingly, we observe a small performance deterioration with the MLP connector.

Overall, we conclude that in our case, the linear connector seems preferable to the MLP connector.

### Image encoder: with or without?

Figure 8: Not using a SigLiP image encoder at all and instead passing a linear projection of raw RGB patches to Gemma works, but is significantly less sample-efficient.

Most VLMs follow the setup of having an image encoder, such as CLIP/SigLIP (most works) or VQGAN (the Chameleon line of work ), to turn the image into soft tokens before passing them to the LLM. We are aware of only two works that attempt to simplify this overall setup by removing the image encoder entirely and passing raw image patches into a decoder-only LLM, namely Fuyu and EVE. Unfortunately, the former provides no training details or ablations. The latter, which is a concurrent work, provides some details about training and various ablations, but with mixed results.

Removing the SigLIP encoder in PaliGemma results in a model of the same unified decoder-only architecture. We run our Stage1 and transfers in this setting. Since the architecture significantly changed, we also re-tune the learning-rate of Stage1. Figure 8 (per-task breakdown in Appendix LABEL:sec:app:enc) shows that while this architecture still significantly lags behind, the scaling with pretraining duration seems potentially promising. This is especially noteworthy considering that PaliGemma's SigLIP encoder has seen 40 B image-text pairs during its Stage0 pre-training, while the Fuyu-style model sees images for the first time in the Stage1 pre-training shown here, and only sees up to 1 B of them in our experiment. This ablation confirms that such decoder-only VLMs might be a promising future direction towards simpler multimodal models, although they currently still suffer in training efficiency due to not being able to reuse vision components.

### Image resolution

Image resolution in VLMs is an important topic that has recently received increased attention. PaliGemma uses a very simple approach to deal with resolution: Stage1 is pretrained at relatively low and economical 224px resolution, and short Stage2 then "upcycles" this checkpoint to higher resolutions (448px and 896px). Hence, the final PaliGemma model comes with three different checkpoints for three different resolutions.

In this section we justify our approach and the necessity for providing three separate checkpoints, and compare it to a recently popular "windowing" approach. For the ablation studies, we consider resolutions 224px and 448px, and restrict evaluation to single-image tasks where resolution has significant impact on performance according to Table 1, which we call "Resolution-sensitive" tasks.

### Resolution or sequence length?

Figure 9: Increasing resolution has two effects: increased information content of the input image, and increased model capacity via sequence length. For tasks that benefit from increased resolution, both of these effects contribute roughly equally to the overall gain.

We generally see either neutral or improved performance across tasks when increasing the resolution of the input image (see Table 1). However, it is unclear whether this improvement comes from the fact that the image has higher resolution and therefore more information, or whether it is thanks to the resulting longer sequence length and thus increased model FLOPs and capacity. We disentangle these by running Stage2 and transfers at 448 px resolution, *but downscaling each image to 224 px before resizing it to 448 px*. Thus, the model gets to see the information content of a low-res (224 px) image but with the model capacity of the high-res (448 px) setting.

The result in Fig 9 shows that, for those tasks for which resolution has an effect at all, the reason for the improved performance is split roughly equally between these two causes. This is true for every individual task and not just an effect of averaging, see Appendix LABEL:sec:app:res_or_seqlen.

### Need resolution-specific checkpoints?

Figure 10: Different ways of increasing resolution. While resolution during transfers works (orange), it is not the best setup. Using “windows” works better (mauve, sw means image resolution s with window-size w), but simply running Stage2 at increased resolution with no tricks works best, justifying the need to provide multiple checkpoints. Per-task breakdown in Appendix LABEL:sec:app:res_window.

PaliGemma provides one checkpoint per resolution. But is this really needed? Could we not provide just a single, maybe high-resolution checkpoint, and adapt it as needed during transfers?

Figure 10 shows clearly that providing either only a 224 px or only a 448 px checkpoint would not be sufficient: Transferring the 448 px checkpoint at 224 px resolution (first bar, orange) leads to significantly worse results than using the 224 px checkpoint (second bar, zero), even though the latter had slightly less pretraining. Similarly, transferring the 224 px checkpoint at resolution 448 px (third bar, orange), while improving the results significantly, still lags far behind transferring the checkpoint whose native resolution is 448 px (last bar, green).

Thus, in the absence of flexible-resolution modeling tricks such as FlexiViT or NaViT, we recommend running extended pretraining for increasing resolution (Stage2) and providing separate checkpoints for all supported resolutions.

### To resize or to window?

Another recently common way of increasing input resolution is by "windowing" the models, *i.e*. applying the same model on windows of the model's native resolution from the higher-resolution image. We evaluate the simplest variant of this alternative: the 448 px resolution image is cut into four pieces, each one passed through the SigLIP image encoder separately. All four sets of 256 image embedding tokens are then concatenated and passed to Gemma. This is also related to using windowed attention in a ViT taking the full image. We experimented with adding extra "window ID" position embeddings to indicate which window tokens come , but this did not significantly change any of the results.

The mauve bars in Figure 10 correspond to windowing settings. While overall the performance is worse than that of a native 448px model, the windowing approach can be a promising way of transferring a model to a higher resolution *when no higher-resolution checkpoint is made available*, and when running a Stage2-like continued pretraining is not feasible.

Windowing might still seem preferable for speed reasons. However, we only observed at most a 5% speedup in training across various setups from windowing. This is explained by Gemma being significantly larger than ViT-So400m, and the Gemma part of the model is unaffected by windowing.

### Stage2 mixture re-weighting

Finally, the pretraining mixture changes between Stage1 and Stage2. While previous PaLI versions change the mixture makeup, for PaliGemma we always use the full set of tasks, only changing their weighting, sampling "resolution-related" tasks (OCR, detection, segmentation) more frequently at higher resolutions. As an ablation, we run a Stage2 training with the same mixture ratios as Stage1. After transfers, this checkpoint is significantly worse on only three tasks (DocVQA, ChartQA, XM3600), but otherwise within per-task variance (Full results in Appendix LABEL:sec:app:s2_reweight).

Thus, while changing the mixing ratio helped a little, it seems that when the intent is to train a base model for fine-tuning, the precise mixture ratios might not be as important as when training a model intended for sampling zero-shot, where it would significantly affect sampling frequencies.

## Transferability

To show that PaliGemma is suitable for transfer under different scenarios, we run experiments that quantify its repeatability, sensitivity to hyper-parameters, and number of transfer examples.

### Repeatability (variance)

Figure 11: For most tasks, the standard deviation of final metric values between re-runs with different seeds is below 0.5. This is true both for Stage1 (top, single transfers of three 100M runs), as well as for transfers (bottom, values from Table 1).

In the main results (Table 1), we show the standard deviation across 5 transfer reruns using the best hyper-parameter (listed in J). It is generally very small across most tasks, meaning transfer from the pretrained checkpoint is highly repeatable. In Figure 11 ‣ 6 Transferability ‣ PaliGemma: A versatile 3B VLM for transfer") we further show that the standard deviation of transferring from three reruns of Stage1 falls within the same range, meaning pretraining itself is also highly repeatable.

### Transfer hyper-parameter sensitivity

All other tasks Table 2: Relative regret of using the suggested hyper-parameter setting for all tasks instead of performing hyper-parameter search. Per task plot in Appendix LABEL:sec:app:transfer_simple.

However one question a reader may have is whether the choice of transfer hyper-parameter is important. To ablate that we run all tasks at 224px and under a single and simple hyper-parameter setup, which was also highlighted in bold in Section 3.2.4: lr=1e-5, bs=256, no dropout, no label smoothing, no weight decay, and not freezing anything. The only task dependent parameter is the number of epochs for which we use each task's best one but cap it at 10.

The results (Table 2) show that this simplified and single setup works very well for the majority of the tasks. The main exceptions we found were for tasks like RefCOCO and SciCap tasks which seem to benefit significantly from increasing the number of epochs while enabling label smoothing and dropout.

### Transfer with limited examples

Figure 12: Relative regret of using a limited number of transfer examples. Thick line represents the median. Per task plot in appendix LABEL:sec:app:transfer_lowdata.

To analyze how many examples are needed to make PaliGemma solve a new task, we finetune PaliGemma with limited number of examples. We sweep transfer with varying learning rates, epochs and batch size and report the best number without separate minival, to indicate the potential.

We run every setting with 5 different seeds, which also affect which examples are used. We found this important, as finetuning with limited examples exhibits high variance for some tasks (*e.g*. RefCOCO mIOU varied within 10%-30%). As a note, this variance also occurs when repeating with the same examples, but different batch order. Importantly, seed selection is not overfitting to the metric as the selected model performs equally well in the validation and test splits.But it does allows us to draw conclusions without needing to solve the open problem of making few-example fine-tuning stable.

Overall, when comparing the best runs of each hyper-parameter and seed with the results obtained with the full dataset, Figure 12 shows that it is not necessary to have a transfer dataset in the order of 10 k examples. The majority of the tasks can reach within 10% of the full-data score when using 4 k examples and 20% when using only 256 examples. In many cases the score with 64 transfer examples are good enough to prototype using PaliGemma for a new application.

## Noteworthy tidbits

We also briefly discuss several small but interesting discoveries or we made, providing more details on each in the Appendix.

Plain resize to square for segmentation. We found simple resize to square ($224 \times 224$) to work just as well as popular aspect-ratio preserving zoom and crop augmentations. (Appendix C) Counting: introducing CountBenchQA. Due to skewed number distribution and varying image quality, we found TallyQA lacking in its ability to assess current VLM's ability to count. This is why we introduce CountBenchQA, a VLM-ready version of the CountBench dataset. (Appendix D).

Issues in published WidgetCaps numbers. We found issues in at least three previous work's evaluation of WidgetCaps, rendering numerical comparisons invalid. (Appendix E).

Image annotations work as well as prompts. Marking the widget to be captioned with a red box in the image gives the same results as indicating it with \<loc\> tokens in the prompt. (Appendix F) RoPE interpolation unnecessary for upscaling. For Stage2, we tried interpolating the RoPE position indices for the image tokens to preserve their semantics from Stage1. However, we saw no benefit from doing so.

Zero-shot generalization to 3D renders. Although never explicitly trained for it, PaliGemma generalizes surprisingly well to 3D renders form Objaverse without fine-tuning. (Appendix G) Our MMVP result is SOTA by a large margin. PaliGemma at 224px achieves 47.3% paired accuracy, while GPT4-V and Gemini achieve 38.7% and 40.7%, respectively, and all other models including LLaVa perform below chance.

## Conclusion

PaliGemma is a new, small, open base VLM that shines when transferred to a broad range of tasks. Our results show that VLMs on the "smaller" side can provide state-of-the-art performance across a wide variety of benchmarks. We also hope that providing the base model without instruction tuning serves as a useful starting point for further research in instruction tuning, specific applications, and encourages clearer separation of base models and fine-tunes in VLM research.
