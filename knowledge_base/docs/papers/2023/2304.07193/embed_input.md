<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DINOv2: Learning Robust Visual Features without Supervision

Topics include Robustness, Foundation models, Computer vision, Self-supervised learning, Datasets, Benchmarks, Learning, DINOv2.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision. These models could greatly simplify the use of images in any system by producing all-purpose visual features, i.e., features that work across image distributions and tasks without finetuning. This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources. We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size. Most of the technical contributions aim at accelerating and stabilizing the training at scale. In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised literature. In terms of models, we train a ViT model with 1B parameters and distill it into a series of smaller models that surpass the best available all-purpose features, OpenCLIP on most of the benchmarks at image and pixel levels.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning task-agnostic pretrained representations have become the standard in Natural Language Processing (NLP). One can use these features "as they are", i.e., without fine-tuning, and achieve performances on downstream tasks that are significantly better than those produced by task-specific models. This success has been fueled by pretraining on large quantities of raw text using pretext objectives, such as language modeling or word vectors, that require no supervision.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following this paradigm shift in NLP, we expect similar "foundation" models to appear in computer vision. These models should generate visual features that work out of the box on any task, both at the image level, e.g., image classification, and pixel level, e.g., segmentation. Most promising efforts towards these foundation models focus on text-guided pretraining, i.e., using a form of textual supervision to guide the training of the features. This form of text-guided pretraining limits the information that can be retained about the image since captions only approximate the rich information in images, and complex pixel-level information may not surface with this supervision. Furthermore, these image encoders require aligned text-image corpora and hence, do not offer the flexibility of their text counterparts, that is, to learn from raw data alone.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative to text-guided pretraining is self-supervised learning where features are learned from images alone. These approaches are conceptually closer to pretext tasks such as language modeling and can capture information at the image and pixel level. Additionally, the features output by self-supervised models have been shown to exhibit various useful properties, and have enabled enabled a wide variety of applications. However, despite their potential to learn general-purpose features, most of the advances in self-supervised learning were made in the context of pretraining on a small curated dataset, ImageNet-1k. Some efforts on scaling these approaches beyond ImageNet-1k have been attempted, but they focused on uncurated datasets, which typically lead to a significant drop in the quality of the features. This is explained by the lack of control over the data quality and diversity, which are essential to produce good features.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we explore if self-supervised learning has the potential to learn general-purpose visual features if pretrained on a large quantity of curated data. We revisit existing discriminative self-supervised approaches that learn features at both the image and patch level, such as iBOT, and we reconsider some of their design choices under the lens of a larger dataset. Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes. These improvements make our approach around 2$\times$ faster and require 3$\times$ less memory than similar discriminative self-supervised methods, allowing us to leverage longer training with larger batch sizes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regarding pretraining data, we have built an automatic pipeline to filter and rebalance datasets from an extensive collection of uncurated images. This pipeline is inspired by pipelines used in NLP, where data similarities are used instead of external metadata and do not require manual annotation. A major difficulty when dealing with images in the wild is to rebalance concepts and avoid overfitting on a few dominant modes. In this work, a naive clustering approach works reasonably well to resolve this issue. We gathered a small but diverse corpus of 142M images to validate our approach.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we provide a variety of pretrained visual models, called DINOv2, trained with different Vision Transformers (ViT) architectures on our data. We release all the models and the code to retrain DINOv2 on any data. We validate the quality of DINOv2 on various computer vision benchmarks at both image and pixel levels as we scale them, as summarized in Fig. 2. We conclude that self-supervised pretraining alone is a good candidate for learning transferable frozen features that are competitive with the best openly available weakly-supervised models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Intra-image self-supervised training", "weight": 1.0} -->

A first family of self-supervised methods focuses on pretext tasks built from the image, i.e., extracting a signal from the image to be predicted from the rest of the image. This idea has become prevalent with the work of Doersch et al., where they train by predicting the context of a given patch. Many other pretext tasks were introduced based, for example, re-colorizing images, predicting transformations, inpainting or patch re-ordering. Recently, the emergence of patch-based architectures, like ViTs, has led to a revisit of inpainting for pre-training, potentially in feature space. Of particular interest, He et al. show that a masked auto-encoder (MAE) learns features that provide substantial improvements when finetuned on downstream tasks. This property of MAEs has been further validated on video, audio, and across other modalities. However, their features require supervised finetuning, while our features perform well out of the box.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Discriminative self-supervised learning", "weight": 1.0} -->

The second line of work, closer to ours, is using discriminative signals between images or groups of images to learn features. This family of methods has roots in early deep learning work but became popular with the emergence of instance classification methods. Several improvements were made based either on instance-level objectives or clustering. These methods provide performant frozen features on standard benchmarks like ImageNet, but they are hard to scale to larger model sizes. In this work, we revisit the training of these approaches in the context of large pretraining datasets and models. In particular, we build on top of Zhou et al. that we find particularly suited for scaling.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Scaling self-supervised pretraining", "weight": 1.0} -->

A growing body of work has focused on the scaling abilities of self-supervised learning in terms of data and model size. Most of these works use large quantities of uncurated data to train models without supervision. They show evidence that discriminative methods scale with data, but because of the poor quality of the pretraining data, most of the results are obtained by finetuning the features. Of particular interest, Goyal et al. have also shown that these methods benefit from scaling in model size given enough pretrained data. This line of work questions the ability of self-supervised methods to work on any data while we focus on producing the best pretrained encoders.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Automatic data curation", "weight": 1.0} -->

Our dataset construction borrows from the image retrieval community. In particular, the use of retrieval to augment the training set has been studied in the context of semi-supervised learning. Similarly, others have used hashtags or other metadata or pretrained vision encoders to filter uncurated datasets. Unlike these works, we use no pretrained encoders, metadata nor supervision to filter images and leverage visual similarity between images. Our approach is inspired by text curation pipelines, where a language model is trained on Wikipedia to score texts extracted from an uncurated source.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Data Processing", "weight": 1.0} -->

We assemble our curated LVD-142M dataset by retrieving, from a large pool of uncurated data, images that are close to those in several curated datasets. We describe below the main components in our data pipeline including the curated/uncurated data sources, the image deduplication step and the retrieval system. Our pipeline does not require any metadata or text and directly works with images, as shown in Fig. 3. We refer the reader to appendix A for more details on our approach.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data Processing", "weight": 1.0} -->

Data sources. Our selection of curated datasets is detailed in the appendix (Table 15) and contains ImageNet-22k, the train split of ImageNet-1k, Google Landmarks and several fine-grained datasets. For the uncurated data source, we collect a raw unfiltered dataset of images from a publicly available repository of crawled web data. From each web page in the repository, we extract URL links of images from \ tags. We discard URLs that are unsafe or restricted by domains, and post-process the downloaded images (PCA hash deduplication, NSFW filtering, and blurring identifiable faces). This results in 1.2B unique images.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Data Processing", "weight": 1.0} -->

Deduplication. We apply the copy detection pipeline of Pizzi et al. to the uncurated data and remove near-duplicate images. This reduces redundancy and increases diversity among images. We also remove near-duplicates of images contained in the test or validation set of any benchmark used in this work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Data Processing", "weight": 1.0} -->

Self-supervised image retrieval. We build our curated pretraining dataset by retrieving images from our uncurated data source that are close to images in our curated sources. In order to do this, we first compute an image embedding using a self-supervised ViT-H/16 network pretrained on ImageNet-22k, and use cosine-similarity as a distance measure between images. Then, we perform k-means clustering of the uncurated data. Given a query dataset for retrieval, if it is large enough we retrieve $N$ (typically 4) nearest neighbors for each query image. If it is small, we sample $M$ images from the cluster corresponding to each query image. Although visual inspection seemed to indicate good retrieval quality for $N$ much larger than 4, this leads to more collisions (images that are nearest-neighbor retrievals of multiple queries). We choose $N=4$ as it provides a good tradeoff in that sense.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Data Processing", "weight": 1.0} -->

Implementation Details. The deduplication and retrieval stages of our pipeline rely on the Faiss library to efficiently index and compute batch searches of nearest embeddings. In particular, we heavily leverage its support for GPU-accelerated indices, using inverted file indices with product quantization codes. The whole processing is distributed on a compute cluster of 20 nodes equipped with 8 V100-32GB GPUs and takes less than two days to produce the LVD-142M dataset.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

We learn our features with a discriminative self-supervised method that can be seen as a combination of DINO and iBOT losses with the centering of SwAV. We also add a regularizer to spread features and a short high-resolution training phase. We rapidly introduce each of these approaches, but more details can be found in the related papers, or in our open-sourced code.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

Image-level objective. We consider the cross-entropy loss between the features extracted from a student and a teacher network. Both features are coming from the class token of a ViT, obtained from different crops of the same image. We pass the student class token through the student DINO head. This head is an MLP model outputting a vector of scores, that we call \"prototype scores\". We then apply a softmax to obtain $p_{s}$. Similarly, we apply the teacher DINO head to the teacher class token to obtain teacher prototype scores. We then apply a softmax followed by a centering with moving average (or a Sinkhorn-Knopp centering as detailed thereafter) to obtain $p_{t}$. The DINO loss term corresponds to: We learn the parameters of the student and build the teacher head with an exponential moving average of past iterates.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

Patch-level objective. We randomly mask some of the input patches given to the student, but not to the teacher. We then apply the student iBOT head to the student mask tokens. Similarly, we apply the teacher iBOT head to the (visible) teacher patch tokens corresponding to the ones masked in the student. We then apply the softmax and centering steps as above, and obtain the iBOT loss term:, where $i$ are patch indices for masked tokens. Similarly to above, we learn the parameters of the student, and build the teacher head through exponential moving average.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

Untying head weights between both objectives. Both the DINO and the iBOT loss use a learnable MLP projection head. It is applied to the output tokens and the loss is compute atop. In Zhou et al., an ablation study shows that sharing parameters between the DINO and iBOT heads leads to better performance. At scale, we observed that the opposite is true, and we therefore use two separate heads in all our experiments.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

Sinkhorn-Knopp centering. Ruan et al. recommend to replace the teacher softmax-centering step of DINO and iBot by the Sinkhorn-Knopp (SK) batch normalization of SwAV. We run the Sinkhorn-Knopp algorithm steps for 3 iterations. For the student, we apply the softmax normalization.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

KoLeo regularizer. The KoLeo regularizer derives from the Kozachenko-Leonenko differential entropy estimator (see Beirlant et al.; Delattre & Fournier) and encourages a uniform span of the features within a batch. Given a set of $n$ vectors $(x_{1},\dots,x_{n})$, it is defined as where $d_{n,i}=\min_{j\neq i}\|x_{i}-x_{j}\|$ is the minimum distance between $x_{i}$ and any other point within the batch. We also $\ell_{2}$-normalize the features before computing this regularizer.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discriminative Self-supervised Pre-training", "weight": 1.0} -->

Adapting the resolution. Increasing image resolution is key to pixel-level downstream tasks such as segmentation or detection, where small objects disappear at low resolutions. However, training at high resolution is time and memory demanding, and instead, we increase the resolution of images to $518\times 518$ during a short period at the end of pretraining. This is also similar to UniViT training from Likhomanenko et al. and FlexiViT training from Beyer et al..

<!-- chunk {"id": "body-0025", "role": "body", "section": "Efficient implementation", "weight": 1.0} -->

We consider several improvements to train models at a larger scale. We train models on A100 GPUs using PyTorch 2.0. The code and pretrained models are made available under Apache 2.0 license ^11^1 The details of our models are in the appendix, Table 17. With the same hardware, compared to the iBOT implementation, the DINOv2 code runs around $2\times$ faster using only $1/3$ of the memory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Fast and memory-efficient attention", "weight": 1.0} -->

We implemented our own version of FlashAttention to improve memory usage and speed on the self-attention layers. Our version is on par with or better than the original on all cases considered, while covering more use-cases and hardware. Due to the GPU hardware specifics, the efficiency is best when the embedding dimension per head is a multiple of 64, and the matrix operations are even better when the full embedding dimension is a multiple of 256. As a consequence, our ViT-g architecture slightly differs from the architecture proposed by Zhai et al. in order to maximize compute efficiency, and we use an embedding dimension of 1536 with 24 heads (64 dim/head), rather than 1408 with 16 heads (88 dim/head). Our experiments did not show significant differences in final accuracy, and our ViT-g backbone counts 1.1B parameters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sequence packing", "weight": 1.0} -->

The DINO algorithm requires forwarding both large crops (at resolution 224) and small crops (resolution 98). When split into patches, these two groups are represented by token sequences of different lengths and cannot be forwarded together. In order to accelerate training, we use a trick called \"sequence packing,\" which originates from NLP. The idea is simple: we concatenate the sequences we must forward through the transformers into a single long sequence. We pass this sequence through the transformer blocks as usual. However, a block-diagonal mask is applied to the self-attention matrix in attention layers, preventing attention between different sequences. This way, the forward is strictly equivalent to forwarding each sequence separately. This trick gives us significant compute efficiency gains compared to using separate forward and backward passes, as in prior implementations. The lower-level components of our setup are available in the xFormers library^22^2 (Lefaudeux et al. ).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Efficient stochastic depth", "weight": 1.0} -->

We implement an improved version of stochastic depth that skips the computation of the dropped residuals rather than masking the result. This saves memory and compute in proportion approximately equal to the drop rate, thanks to specific fused kernels. With high drop rates ($d=40\%$ in this work), this allows a drastic improvement in compute efficiency and memory usage. The implementation consists of randomly shuffling the $B$ samples over the batch dimension, and slicing the first $(1-d)\times B$ samples for the computations in the block.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Fully-Sharded Data Parallel (FSDP)", "weight": 1.0} -->

Minimizing our objective with the AdamW optimizer requires 4 model replicas in float32 precision -- student, teacher, optimizer first moments, optimizer second moments. This sums to $16~\mathrm{GB}$ of memory for a billion-parameter model such as our ViT-g. In order to reduce this memory footprint per GPU, we split the model replicas across GPUs, i.e., sharding $16~\mathrm{GB}$ across GPUs using the PyTorch implementation of FSDP. Consequently, the model size is not bounded by the memory of a single GPU but by the total sum of GPU memory across compute nodes. The Pytorch implementation of FSDP brings a second advantage, which is to save on the cross-GPU communication costs: the weight shards are stored in float32 precision as required by the optimizer, but broadcasting weights and reducing gradients is done in float16 precision for the backbone (MLP heads gradients are reduced in float32 to avoid training instabilities).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Fully-Sharded Data Parallel (FSDP)", "weight": 1.0} -->

This leads to approximately 50% reduction in communication costs compared to the float32 gradient all-reduce operation used in DistributedDataParallel (DDP), which is used in other self-supervised pretraining methods. As a consequence, the training procedure scales more efficiently than DDP with float16 autocast when scaling the number of GPU nodes. Overall, Pytorch-FSDP mixed-precision is superior to DDP with autocast in virtually all cases we encountered.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Model distillation", "weight": 1.0} -->

Most of our technical improvements to the training loop aim at improving the training of large models over large quantities of data. For smaller models, we distill them from our largest model, the ViT-g, instead of training them from scratch. Knowledge distillation aims at reproducing the output of a large model with a smaller model by minimizing some distance between both outputs for a set of given inputs. Since our objective function is a form of distillation from the teacher network to the student network, we leverage the same training loop with a few exceptions: we use a larger model as a frozen teacher, keep a spare EMA of the student that we use as our final model, remove the masking and stochastic depth, and, apply the iBOT loss on the two global crops. In our ablations, we observe that this approach achieves better performance than training from scratch, even for a ViT-L. Our distillation method ends up close to the one described by Duval et al., except we do not modify the loss terms for distillation and evaluate the EMA of the student.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We present a set of ablations to empirically validate different components of our pipeline: the technical modifications described in Sec. 4, the pretraining data and the impact of model distillation. We consider various downstream tasks that are described in Sec. 7.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Improved Training Recipe", "weight": 1.0} -->

Our approach improves over the iBOT method by combining it with several existing components described in Sec. 4. To evaluate their importance, we train multiple models where we successively add components to a baseline iBOT model. We report the Top-1 accuracy on the validation set of ImageNet-1k with a k-NN and a linear probe in Table 1. Generally, we observe that each component improves the performance on either k-NN or linear probing and even both in most cases. Only LayerScale and Stochastic Depth incur a performance drop in linear probing but significantly improve the training stability in our experience.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Improved Training Recipe", "weight": 1.0} -->

+LayerScale, Stochastic Depth +Tweak warmup schedules +Untying heads = DINOv2 Table 1: Ablation study of the training differences between iBOT and DINOv2. We optimize for k-NN performance, as in our experience, the linear probe performance is lower-bounded by the k-NN performance. Some modifications, like LayerScale and a high Stochastic Depth (rate=0.4), incur a decrease in linear probe performance, but have the benefits of increasing the stability of training by avoiding NaN loss values during training. Overall, these modifications allowed for the next set of improvements to be added. Experiments are run using the ViT-Large architecture on ImageNet-22k.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Pretraining Data Source", "weight": 1.0} -->

The quality of features is directly related to the quality of the pretraining data. In this experiment, we probe the impact of LVD-142M compared to ImageNet-22k, a commonly used pretraining dataset, or using directly raw and uncurated data. For the uncurated dataset, we randomly sample $142$ million images from the same data source as LVD-142M. We train a ViT-g/14 on each dataset for the same number of iterations. We also include a variant of ImageNet-22k obtained by removing the synsets of ImageNet-1k (INet-22k $\setminus$ INet-1k) for completeness. We report the comparisons in Table 2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Pretraining Data Source", "weight": 1.0} -->

The most salient observation is that training on a curated set of images works better on most benchmarks than training on uncurated data. This confirms the benefit of curating data, even in the case of self-supervised pretraining. When compared with models trained on ImageNet-22k, training on LVD-142M is also superior on all the benchmarks but ImageNet-1k. This confirms that training on a more diverse set of images improves the quality of the features in domains that are not covered by ImageNet-22k. We also see that training on our curated data increases the performances on domains that are not used for the curation process, proving that scale and diversity can benefit unseen domains. Overall, the conclusion of this ablation is that our dataset provides a good balance of different types of images that leads to the best performance overall.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model Size and Data", "weight": 1.0} -->

We quantify the importance of scaling data with the model size in Fig. 4. As the size of models grow, training on LVD-142M becomes more beneficial than training on ImageNet-22k. For instance, a ViT-g trained on LVD-142M matches the performance on ImageNet-1k of a model trained on ImageNet-22k while significantly outperforming it on the other benchmarks.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Loss Components", "weight": 1.0} -->

We validated the proposed technical improvements in Sec. 6.1 by adding them incrementally. This section analyzes the performance hit observed if we ablate specific loss terms, starting from our best-performing model. We ablate the importance of the KoLeo loss and the impact of the masked image modeling term. For both, we report performance on ImageNet-1k using a linear classifier, ADE-20k segmentation using a linear classifier, and nearest-neighbor image retrieval on Oxford-M. Table 3(a) shows the impact of using the KoLeo loss. We see that the instance retrieval performance improves by more than $8\%$, confirming that this term helps spread features in the output space. At the same time, the other metrics do not suffer from this regularization. In Table 3(b), we show the impact of using the masked image modeling term from iBOT. This term is critical for dense prediction tasks, leading to almost $3\%$ performance improvement.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Loss Components", "weight": 1.0} -->

(b) MIM objective in iBOT Table 3: (a) Effect of the KoLeo loss term. (b) Effect of the iBOT Masked Image Modeling (MIM) loss term. Evaluation performed on ImageNet-{1k,A} (classification with linear probe, accuracy %), ADE-20k (segmentation with linear layer, mIoU) and Oxford-M (image retrieval, mAP). Each model is trained on the same number of iterations, that is smaller than our final run. The KoLeo loss term improves nearest-neighbor search tasks (e.g. retrieval), and the MIM loss improves patch-level tasks (e.g. segmentation).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Impact of Knowledge Distillation", "weight": 1.0} -->

For small architectures, we distill larger models instead of training them from scratch. We use the distillation procedure described in Sec. 5. We evaluate the effectiveness of this approach by comparing a ViT-L/14 trained from scratch with one distilled from a ViT-g/14 over 12 benchmarks in Fig. 5. We also report the performance of the ViT-g/14 used for distillation as a topline. The distilled model outperforms the one trained from scratch on all 12 benchmarks, validating our pretraining approach for small models.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Impact of Knowledge Distillation", "weight": 1.0} -->

(a) Comparison on individual metrics (b) Averaged metrics on 8 vision tasks Figure 5: Effectiveness of knowledge distillation. Comparison between a ViT-L trained from scratch or distilled from DINOv2 using ViT-g/14. For reference, we also report the performance of the ViT-g/14 teacher. We show that a ViT-L model distilled from a frozen ViT-g outperforms a the same model trained from scratch on all benchmarks, sometimes even outperforming the distillation target.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Impact of Resolution", "weight": 1.0} -->

We measure the impact of changing the resolution during the pretraining on the performance of image and patch-level features. We consider models trained from scratch using a fixed resolution of either $224\times 224$ or $416\times 416$, and a model trained from scratch at $224\times 224$, then resumed for 10k more iterations at $416\times 416$. High-resolution training is compute-intensive, so we conduct this ablation on a small setup: a ViT-L/16 trained on ImageNet1k. In Fig. 6, we report the performance of a linear probe on ImageNet-1k and ADE-20k, evaluated at various resolutions. The model trained on high-resolution images performs best across resolutions, but this comes at a high cost: training at $416$ is approximately $3\times{}$ more compute-intensive than training at $224$. On the other hand, training at high resolution for only 10k iterations at the end of the training is almost as good and only requiring a fraction of the compute. As a consequence, we include this step at the end of the training rather than training at a high resolution from scratch.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we present the empirical evaluation of our models on many image understanding tasks. We evaluate both global and local image representations, on category and instance-level recognition, semantic segmentation, monocular depth prediction, and action recognition. We detail the list of benchmarks in Appendix C. The goal of this evaluation is twofold. First, we show that our self-supervised features outperform the current state of the art by a very large margin. Second, we show that they match, or surpass the performance of weakly-supervised ones on a substantial number of tasks.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results", "weight": 1.0} -->

Baselines. In our comparisons, we use two kinds of models as baselines. We compare to the best performing self-supervised models that are openly available. First, we run our evaluations for MAE, DINO, SEERv2, MSN, EsViT, Mugs and iBOT. When several architectural variants were proposed for a given method, we report results for the one that leads to best top-1 accuracy on ImageNet-1k. Second, we report performance of open-source weakly-supervised models such as CLIP, OpenCLIP, and SWAG. When evaluating models on ImageNet-1k, we report the performance for each of the aforementioned methods. For all other evaluations, we report the four best-performing models amongst SSL ones. Also, for reference, we report the best performing OpenCLIP-G for weakly-supervised ones.

<!-- chunk {"id": "body-0045", "role": "body", "section": "ImageNet Classification", "weight": 1.0} -->

As a first evaluation, we probe the quality of the holistic image representation produced by the model on the ImageNet-1k classification dataset. We evaluate the quality of features by training a simple classifier over a frozen backbone, and do not perform finetuning of the backbone weights. Following previous work, we use a linear model for simplicity, ensuring a reproducible evaluation, despite the fact that classes may not be linearly separable. Because most SSL methods were developped using ImageNet-1k validation performance as a debugging signal, we also report the top-1 accuracy on ImageNet-ReaL and ImageNet-V2. In order to report this additional validation performance, for all models, we run the evaluation with our code. We compare our frozen features to the best publicly available SSL features in Table 4, regardless of architecture or pretraining data. We see the components proposed in this work lead to a very significant improvement ($+4.2\%$) over the previous state of the art (iBOT ViT-L/16 trained on ImageNet-22k) on linear evaluation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "ImageNet Classification", "weight": 1.0} -->

At the same time, we also see that the performance increase on the alternative test sets is larger for our method, indicating stronger generalization. We describe details of our linear evaluation in Appendix B.3.

<!-- chunk {"id": "body-0047", "role": "body", "section": "How far are we from weakly-supervised models?", "weight": 1.0} -->

We also want to validate that our features are competitive with state-of-the-art open-source weakly supervised models. To this end, we compare on ImageNet-1k, using the linear evaluation, to three off-the-shelf methods with several architectural variants. For all models, we run the linear evaluation using our code, after making sure that our numbers match those reported in technical reports and papers. We show the result of this evaluation in Table 4. We see that our backbone, surpases the performance of OpenCLIP with a ViT-G/14 architecture ($+0.3\%$) and EVA-CLIP with a ViT-g/14 ($+0.1\%$). At the same time, we also observe that our performance on the ImageNet-V2 test set is significantly better ($+1.1\%$ versus EVA-CLIP), indicating better generalization. For the remainder of this section, we report OpenCLIP-G as a reference for weakly-supervised models.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Can we finetune the encoders?", "weight": 1.0} -->

We question if the ability of our models to produce high quality frozen features impact their performance when finetuned with supervision on a specific dataset. While this is not core to this paper, this experiment is indicative of whether we have involuntarily specialized our models to the setting of linear evaluations of frozen features. To run this sanity check, we apply the finetuning pipeline from Touvron et al., without tweaking hyper-parameters. In Table 5, we show that the Top-1 accuracy on the validation set of ImageNet-1k improves by more than $+2\%$ when the backbone is finetuned. This is true both when using models at resolution $224$ and $448$. Further gains can be obtained by tuning the hyper-parameters of the finetuning, but this is beyond the goal of this sanity check. Nonetheless, our best finetuned performance ($88.9\%$) is only a couple of percent below ($-2.2\%$) the absolute state of the arts ($91.1\%$), obtained by Chen et al..

<!-- chunk {"id": "body-0049", "role": "body", "section": "Can we finetune the encoders?", "weight": 1.0} -->

As DINOv2 leads to features that are strong in both the linear and finetuning settings, a strong property of our approach is that finetuning is optional.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Robustness analysis", "weight": 1.0} -->

To complement our study, and probe the generalization of our features, we evaluate our ImageNet-1k models trained with linear classification heads on domain generalization benchmarks. We use the best performing linear classifier as described above and simply run inference on those benchmarks. Please note that most results in the literature are obtained with models that are finetuned end-to-end on ImageNet-1k. We show the result of this experiment in Table 6. When comparing with state-of-the-art SSL methods, our models shows drastically better robustness ($+29.6\%$ on A, $+22.1\%$ on R and $+23.0\%$ on Sketch compared to iBOT). Our model also improves upon the best weakly-supervised model on ImageNet-A while lagging behind on R and Sketch.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Additional Image and Video classification Benchmarks", "weight": 1.0} -->

In this section we study the generalization of our features on downstream classification benchmarks. We consider two sets of evaluations in that context. On one hand, we use large and finegrained datasets such as iNaturalist and Places205. On the other, we use the 12 image classification tasks originally proposed in SimCLR. For iNaturalist 2018, iNaturalist 2021, and Places205, we train a linear classifier with data augmentations as in Sec. 7.1 We report top-1 accuracy for those three datasets in Table 7. Interestingly, our model significantly outperforms OpenCLIP ViT-G/14 on both variants of iNaturalist, and lags slightly behind on Places 205 ($-2.3\%$).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Additional Image and Video classification Benchmarks", "weight": 1.0} -->

In a second set of evaluations, we measure the performance of our model on video action recognition even though our features were not trained on videos.. We evaluated features on three datasets, namely UCF-101, Kinetics-400 and Something-Something v2. For this evaluation, we pick $8$ evenly spaced frames in the video and train a linear classifier on the average of the features for UCF and K-400. For SSv2, we opt for concatenation to retain more temporal information than with feature averaging. For each dataset, we measure average accuracy and report the results in Table 7. We see that amongst self-supervised approaches, our model clearly sets a new state of the art. Moreover, our model matches the accuracy of the OpenCLIP features on UCF and Kinetics ($+0.1\%$ and $+0.5\%$ respectively) and clearly outperforms them on SSv2 ($+2.5\%$). This is particularly interesting, as SSv2 requires a much richer understanding of the video frames.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Additional Image and Video classification Benchmarks", "weight": 1.0} -->

Finally, in Table 8, we compare selected frozen features on 12 transfer classification benchmarks initially proposed by Chen et al.. This benchmark covers scenes, objects (food, cars, planes), and textures. We replace the Birdsnap dataset with CUB because the former was not publicly available in its entirety. We follow the experimental protocol as outlined by Chen et al., namely training a logistic regression on precomputed features. Our model significantly outperforms state-of-the-art SSL models, with most notable differences on Stanford Cars ($+14.8\%$ versus DINO ViT-B/8) and FGVC Aircraft ($+14.8\%$ versus iBOT ViT-L/16). Even though these benchmarks favor text-guided pretraining, our features are still competitive with OpenCLIP on most classification benchmarks, with the exception of a few datasets, especially SUN ($-5.3\%$) and Cars ($-4.7\%$).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Instance Recognition", "weight": 1.0} -->

In this experiment, we probe our model on the task of instance-level recognition using a non-parametric approach. Images from a database are ranked according to their cosine similarity with a query image. We evaluated our model and compare to baselines on Paris and Oxford, that are landmark recognition benchmarks. We also evaluated on Met, a dataset of artworks from the Metropolitan museum, and AmsterTime, containing street view images matched to archival images of Amsterdam. We measure performance by computing the mean average precision and report our results in Table 9. We see that our features significantly outperform both SSL ($+41\%$ mAP on Oxford-Hard), and weakly-supervised ($+34\%$ mAP on Oxford-Hard) ones. It is interesting to see that our features perform well across task granularities, both at the category-level and instance-level. This is a desirable property for strong off-the-shelf computer vision features.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Dense Recognition Tasks", "weight": 1.0} -->

We probe the quality of patch-level features extracted from our network on several dense downstream tasks. We consider semantic image segmentation and monocular depth estimation in several settings and we conduct evaluations on multiple datasets for each.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Semantic segmentation", "weight": 1.0} -->

For our semantic segmentation evaluation, we consider two different setups. Linear: a linear layer is trained to predict class logits from a patch tokens. It is used to produce a low-resolution logit map (eg 32x32 for a model with patch size 16), which is then upsampled to full resolution (512x512) to obtain a segmentation map. This procedure is extremely simple but cannot easily produce high-resolution segmentations. +ms: a boosted version of the linear setup. We concatenate the patch tokens of the 4 last layers, use a larger image resolution of 640, and use multiscale test-time augmentations to improve the predictions. We report the performance of our model variants as well as the baselines on three datasets under the two setups in Table 10.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Semantic segmentation", "weight": 1.0} -->

Our models show very good performance on all datasets and for all setups. Interestingly, our evaluation using +ms is on par with fully finetuning MAE with an Upernet decoder ($53.0$ versus $53.6$ mIoU). This is surprising because we use a significantly simpler predictor. Also, our best model, when evaluated using the boosted recipe, almost matches the state of the art on Pascal VOC ($86.2$ versus $89.0$ mIoU).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Frozen backbone in a SOTA pipeline", "weight": 1.0} -->

In a final experiment, we freeze our backbone, and plug it into a ViT-Adapter Chen et al. with a Mask2former head. We tune the weights of the adapter and head, but keep the backbone frozen, meaning 66% of the weights are frozen. This allows for a lighter segmentation training than full end-to-end fine-tuning. With this setup, we reach $60.2$ mIoU, close to the competitive state of the art, standing at 62.9 mIoU. Although our setup for this experiment doesn't makes use of the optimisations described in Sec. 5, the segmentation training in this experiment took 28 hours on 16 V100 GPUs.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Depth estimation", "weight": 1.0} -->

In this experiment, we evaluate our patch-level features on three monocular depth estimation benchmarks: NYUd, KITTI and zero-shot transfer from NYUd to SUN3d. We follow the evaluation protocol of Li et al.. We consider three different setups for this evaluation. lin. 1: we extract the last layer of the frozen transformer and concatenate the \[CLS\] token to each patch token. Then we bi-linearly upsample the tokens by a factor of 4 to increase the resolution. Finally we train a simple linear layer using a classification loss by dividing the depth prediction range in 256 uniformly distributed bins and use a linear normalization following Bhat et al.. lin. 4: we use the same protocol that we use with one layer, but concatenate the tokens from layers $l=\{3,6,9,12\}$ for ViT-S/B, $l=\{5,12,18,24\}$ for ViT-L, and $l=\{10,20,30,40\}$ for ViT-g.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Depth estimation", "weight": 1.0} -->

DPT: we use the DPT decoder on top of our frozen models and setup a regression task. We scale the size of the head following the dimension of the features for each architecture. We show results for all baselines, all datasets and all setups in Table 11.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Depth estimation", "weight": 1.0} -->

From this table, we see that our features clearly surpass the best SSL and WSL features available. It is interesting to see that iBOT features extracted from a ViT-L outperform the ones of OpenCLIP with a ViT-G. This observation supports the intuition that caption-based feature learning fails to learn subtle patterns like this one. Also, our model, with the DPT decoder and frozen backbone, matches or exceeds the performance of the recent work of Li et al.. Finally, the out-of-domain generalization result on SUN-RGBd shows that our features allow very good transfer between domains. A depth prediction module trained on indoor scenes from NYUd generalizes pretty well to the outdoor examples of SUN-RGBd.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Depth estimation", "weight": 1.0} -->

NYUd → SUN RGB-D Table 11: Depth estimation with frozen features. We report performance when training a linear classifier on top of one (lin. 1) or four (lin. 4) transformer layers, as well, as the DPT decoder (DPT) of Ranftl et al.. We report the RMSE metric on the 3 datasets. Lower is better. For reference, we report state-of-the-art results taken from Li et al. on each benchmark on top of the Table.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In this final section of the empirical evaluation of our features, we propose a few qualitative analyses.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Semantic Segmentation and Depth Estimation", "weight": 1.0} -->

We show some qualitative results for our dense prediction evaluations: segmentation on ADE20K in Fig. 7 and depth estimation on NYUd, KITTI and SUN RGB-D in Fig. 7. We compare DINOv2 with OpenCLIP with a linear classifier on each dataset. While not perfect, the linear segmentation model using our DINOv2 backbone produces good results and behaves much better than the OpenCLIP one under this evaluation setup. Indeed, the segmentation mask produced by OpenCLIP-G shows many artifacts and disconnected components. The qualitative results on depth estimation clearly illustrate the quantitative gap between OpenCLIP and DINOv2. These results highlight that our features, as well as the features extracted from OpenCLIP, are able to linearly separate complex information such as depth, even though neither was trained with this type of information. However, our features lead to a much smoother depth estimation, with less artifacts. Some objects such as the chair on the SUN RGB-D image are completely ignored by OpenCLIP and correctly positioned using our features.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Out-of-distribution generalization", "weight": 1.0} -->

We show a few examples of applying the depth prediction and segmentation linear classifiers to out-of-distribution examples in Fig. 8. The qualitative results support our claim that our features transfer between domains. The quality of the depth and segmentation predicted for pictures of animals, or paintings is very good, even though the domains are very different.

<!-- chunk {"id": "body-0066", "role": "body", "section": "PCA of patch features", "weight": 1.0} -->

We show the results of the principal component analysis (PCA) performed on the patch features extracted by our model. We keep only patches with a positive value after we threshold the first component. This procedure turns out to separate the image's main object from the background. We compute a second PCA on the remaining patches across three images depicting the same category. We color the three first components with three different colors and present the results in Fig. 1 and 9. There are two interesting observations: first, our unsupervised foreground / background detector, based on detecting the highest variance direction, performs very well and is capable of delineating the boundary of the main object in the picture. Second, the other components correspond to \"parts\" of objects and match well for images of the same category. This is an emerging property -- our model was not trained to parse parts of objects.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Patch matching", "weight": 1.0} -->

Finally, we explore what type of information our patch-level features contain by matching them across images. We start by detecting the foreground object using the procedure described above. Then, we compute the euclidean distance between patch features extracted from two images and map them by solving an assignment problem. In order to reduce the number of matches, we then apply a non-maximum suppression to keep only the salient ones. In Fig. 10, we show some examples of such matchings.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Patch matching", "weight": 1.0} -->

We observe that the features seem to capture information about semantic regions that serve similar purpose in different objects or animals. For instance, the wing of a plane matches the wing of a bird. We also observe that the model is robust to style (image versus drawing), and to large variation of poses (see the elephant).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Fairness and Bias Analysis", "weight": 1.0} -->

We conduct two fairness evaluations of our models. We probe for geographical fairness and potential harmful label associations. For both evaluations, we experiment with our largest ViT-g model.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Geographical Fairness", "weight": 1.0} -->

We evaluate geographical fairness on the Dollar Street dataset introduced in De Vries et al. using the evaluation protocol of Goyal et al.. This benchmark compares performance across countries and income levels. It contains 16,073 images from 289 households across 54 countries. The task is to recognize 94 concepts that vary visually between households based on income or location. In Table 12, we compare our model with SEERv2, a model trained on a geographically diverse set of images. Our model is slightly fairer across regions and incomes than the SEERv2 model and significantly better than the supervised baseline reported by Goyal et al.. However, we still observe a significant difference between regions, particularly in Africa, where our model performance drops by 25.7% compared to Europe. This shows that our model is still biased toward Western countries. Similarly, our model performs significantly better on high-income households than low-income ones, with a difference of 31.7%. Despite improvements, we observe significant biases in our models toward wealthy households from Western countries.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Gender, Skintones and Age", "weight": 1.0} -->

In a second set of evaluations, we question how our model classifies images of people of different gender, skin tone, and age (all self-reported). We follow the protocol of Goyal et al., where we train a multiclass classifier on a subset of 619 classes of ImageNet-22k. We group the 619 classes into four broader categories: Human, Possibly Human, Non-Human, or Crime. Non-Human and Crime are considered harmful. Using this classifier, we run inference on 2955 images from the Casual Conversations dataset and keep all labels in the top-5 that are assigned a probability of 0.1 or more. Because of that, we can assign multiple classes to each image. We make one modification to the original evaluation protocol: we do not backpropagate gradients to the backbone and keep it frozen. We compare our model to SEERv2 in Table 13.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Gender, Skintones and Age", "weight": 1.0} -->

Our model often classifies images of all groups as Human without large deviations across skin tones. Neither SEERv2 nor DINOv2 predict harmful labels from the Non-Human or Crime meta-categories (except for two instances where the background contains bars visually similar to prison bars). We see that our model triggers the Possibly-Human classes often. This class is constructed from objects in ImageNet-22k that are often related to Humans, such as Scarf, Glasses, or Beard. Our model often predicts the Possibly-Human class for men because of the prevalence of the Beard class. No clear pattern indicates a bias against a particular group in this study. While this is encouraging, we also acknowledge that a more thorough evaluation of biases may reveal flaws in our model.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Estimating the Environmental Impact of Training our Models", "weight": 1.0} -->

Training foundation models consumes a significant amount of energy, resulting in carbon dioxide emissions. Patterson et al. propose a methodology to report an estimation of the carbon emitted during the training of a model based on the specifics of the data center and its power grid. This computation informs the design of the data center used for the training of models and the choice of location for data centers. This methodology requires to know the specifics of the data center used for training, which can be complex when multiple data centers are involved over time. Additionally, these specifics are most often not in the control of the AI practitioner, and hence, this methodology is less helpful when practioners make technical decisions about future trainings. Instead, in this section, we follow an alternative that reports the potential carbon emission of retraining a similar model in an average data center located in the US. This methodology was used in previous work in natural language processing to establish an apple-to-apple comparison between pretraining schemes.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Estimating the Environmental Impact of Training our Models", "weight": 1.0} -->

More precisely, we fix the value of all exogenous variables, i.e., the Power Usage Effectiveness (PUE) and carbon intensity factor of a power grid to the same values as in Touvron et al., that is, a PUE of 1.1 and the carbon intensity factor to the US average of 0.385 kg CO~2~eq/KWh. We use the same formula as in Patterson et al. to estimate the potential energy consumption and the carbon emission. For the power consumption of an A100-80GB, we take the thermal design power for NVLink systems, which is 400W. We report the potential carbon emission of retraining a DINOv2 ViT-g in Table 14. For comparison, retraining an OpenCLIP ViT-L or OpenCLIP ViT-G would require 22.4 MWh and 118.9 MWh, respectively, if run in the same data center. This is 10$\times$ more carbon emission. Note that this comparison is not fair to them, since they also train a text encoder in parallel, and we thus do not report them in the table.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Estimating the Environmental Impact of Training our Models", "weight": 1.0} -->

However, it gives a reasonable guideline for those who are interested in training only visual features: in this context, training a self-supervised model is preferable in terms of carbon emission. Training a text-guided model still makes sense when planning to reuse the text encoder.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Carbon footprint of the whole project", "weight": 1.0} -->

Additionally, we estimate the footprint of the whole project to be between $0.5$k and $1$k tCO~2~eq using the same grid as presented above ^33^3For context, a full Boeing 777 return flight between London and New York corresponds to approximately 560 tCO~2~eq.. This carbon footprint represents in the order of $200$k GPU-days. The primary sources of emissions are the self-supervised pre-trainings of the models. For example, a single pre-training of a ViT-g model (22k GPU-hours) emits 3.7 tons of CO~2~eq, while a finetuning on ImageNet-1k (1k GPU-hours) emits 0.2 tons. This estimate only considers the GPUs' electricity consumption and ignores other emissions, such as their manufacturing and disposal.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Future work and Discussion", "weight": 1.5} -->

In this work, we present DINOv2, a new series of image encoders pretrained on large curated data with no supervision. This is the first SSL work on image data that leads to visual features that close the performance gap with (weakly) supervised alternatives across a wide range of benchmarks and without the need for finetuning. We can attribute the strong performance of the DINOv2 family of models to several factors: i) an improved training recipe with better hyperparameters and regularization (Table 1), ii) a larger model scale with improved results regardless of the data used for training (Fig. 4), iii) a larger dataset (Fig. 4) and iv) the distillation process that makes smaller models benefit from the performance of the strongest ViT-g model (Fig. 5). A few properties emerge from these models, such as an understanding of object parts and scene geometry regardless of the image domains. We expect that more of these properties will emerge at larger scales of models and data, akin to instruction emergence in large language models, and plan to continue scaling along these axes.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Future work and Discussion", "weight": 1.5} -->

This paper also demonstrates that these visual features are compatible with classifiers as simple as linear layers - meaning the underlying information is readily available. In future work, we plan to leverage this ability to train a a language-enabled AI system that can process visual features as if they were word tokens, and extract the required information to ground the system.
