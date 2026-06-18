<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present V-JEPA 2.1, a family of self-supervised models that learn dense, high-quality visual representations for both images and videos while retaining strong global scene understanding. The approach combines four key components. First, a dense predictive loss uses a masking-based objective in which both visible and masked tokens contribute to the training signal, encouraging explicit spatial and temporal grounding. Second, deep self-supervision applies the self-supervised objective hierarchically across multiple intermediate encoder layers to improve representation quality. Third, multi-modal tokenizers enable unified training across images and videos. Finally, the model benefits from effective scaling in both model capacity and training data. Together, these design choices produce representations that are spatially structured, semantically coherent, and temporally consistent. Empirically, V-JEPA 2.1 achieves state-of-the-art performance on several challenging benchmarks, including 7.71 mAP on Ego4D for short-term object-interaction anticipation and 40.8 Recall@5 on EPIC-KITCHENS for high-level action anticipation, as well as a 20-point improvement in real-robot grasping success rate over V-JEPA-2 AC.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The model also demonstrates strong performance in robotic navigation (5.687 ATE on TartanDrive), depth estimation (0.307 RMSE on NYUv2 with a linear probe), and global recognition (77.7 on Something-Something-V2). These results show that V-JEPA 2.1 significantly advances the state of the art in dense visual understanding and world modeling.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

World models hold the promise of enabling agents to perceive, predict, and plan effectively in the physical world. At the core of these models lies the state-estimation problem: learning representations that reliably summarize the current world state from low-level, noisy perceptual inputs. Self-Supervised Learning (SSL) from video has recently emerged as a powerful route to this goal, because it can exploit large-scale, label-free data to learn representations that capture scene geometry, dynamics, and intrinsic physical properties.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite rapid progress, learning representations that simultaneously preserve *dense* spatio-temporal structure (needed for localization, geometry, and tracking) while also capturing *dynamics* and supporting *global* understanding (needed for high-level recognition) remains an open challenge. Among recent advances, Joint Embedding Predictive Architectures (JEPA) ---and in particular the V-JEPA family ---have demonstrated strong global video understanding, especially in settings that require modeling motion and dynamics, and have shown promise for enabling prediction and planning in embodied agents. However, as illustrated in Figure 1, their learned representations can be less amenable to extracting fine-grained local spatial structure. In contrast, other SSL approaches such as DINO yield high-quality dense features for detection and segmentation, but are primarily image-based and therefore do not directly learn temporal dynamics from video.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we study self-supervised learning with a latent mask-denoising objective, where the model predicts masked segments of an image or video directly in a learned representation space. Our central finding is that high-quality *dense* spatio-temporal features---preserving fine-grained spatial layout and motion dynamics---do not emerge reliably when the prediction loss is applied only to masked regions. Instead, extending the predictive loss to the *entire* input, both masked and unmasked segments, substantially improves the low-level (dense) representations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this insight, we introduce V-JEPA 2.1, a self-supervised approach for learning unified image and video representations. V-JEPA 2.1 uses a *dense predictive loss* applied to *all tokens* (both visible context and masked tokens), grounding each token in its spatio-temporal location and preventing visible tokens from acting as global aggregators---an effect that is key to *improving* dense feature quality (Figure 3). Additionally, we find that *deep self-supervision*---applying the loss hierarchically at multiple intermediate encoder layers to provide training signals throughout the network---yields consistent gains on both dense and global downstream tasks. To enable native joint training across modalities, we use modality-specific learned tokenizers for images and videos within a single shared encoder. Finally, we show these improvements scale with data and model capacity: expanding the image component from 1M to 142M images using VisionMix-163M and scaling the model from 300M to 2B parameters leads to systematic downstream gains.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We train and release a suite of V-JEPA 2.1 models (ViT-g/G, 1B/2B), along with two distilled, smaller variants (ViT-B/L, 80M/300M). Empirically, V-JEPA 2.1 achieves state-of-the-art performance on *predictive* video benchmarks spanning both fine-grained and semantic forecasting: it reaches 7.71 mAP on Ego4D short-term object-interaction anticipation, which requires predicting *where* and *when* interactions will occur (localized interaction regions and time-to-interaction), and 40.8 Recall@5 on EPIC-KITCHENS-100 action anticipation, which evaluates the ability to forecast upcoming actions from partial temporal context.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further show that better dense-features also improves performances on world modelling tasks. V-JEPA 2.1 dense-features leads to +20% success rate compared to VJEPA-2 AC on grasping when when deploy our model on real Franka arms in new environment zero-shot. V-JEPA 2.1 is also suitable for robot navigation where it achieves state-of-art performances (5.687 ATE on Tartan Drive) while having 10x faster planning speed compared to previous work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond prediction and planning, V-JEPA 2.1 also delivers strong performance in both *dense* and *global* understanding tasks. For dense tasks, V-JEPA 2.1 ViT-G sets a new state of the art in linear-probe monocular depth estimation (0.307 RMSE on NYUv2), achieves competitive linear-probe semantic segmentation (85.0 mIoU on Pascal VOC), and produces temporally consistent features for video object segmentation (72.7 $\mathcal{J}\&\mathcal{F}$-Mean on YouTube-VOS). At the global level, it also attains state-of-the-art accuracy in action recognition (77.7% on Something-Something-v2) and achieves competitive performances in Video Question Answering (VQA) tasks (83.1 accuracy on PerceptionTest).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We hope that these contributions will foster research in learning strong representations for physical world modelling, while empowering many applications in video understanding. We make our code and pretrained models publicly available to facilitate further research and applications.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Analysis of V-JEPA Features for Dense Vision Tasks", "weight": 1.0} -->

While V-JEPA has proven to be an effective approach for understanding global semantic information from video, predicting future actions, and planning to reach specific goals, previous works have not investigated the suitability of V-JEPA 2 features for dense vision tasks. To address this gap, we analyze the V-JEPA 2 feature maps through qualitative visualizations and dense downstream tasks evaluation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Analysis of V-JEPA Features for Dense Vision Tasks", "weight": 1.0} -->

For the qualitative visualizations, we compute the Principal Component Analysis (PCA) of patch features extracted from the V-JEPA 2 encoder, and we map the first three components to the RGB color channels. We assess the encoder performance on dense tasks using a linear probing protocol, in which we train a single linear layer on top of the frozen encoder features. We evaluate V-JEPA 2 on semantic segmentation using the ADE20K dataset and depth estimation on NYUv2. Refer to Appendix 8 for more details on the evaluation setup.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Observations and Hypothesis", "weight": 1.0} -->

Feature map visualizations of V-JEPA 2 are shown in Figure 1 and Figure 3. We observe that feature maps are noisy and show only fragmented local spatial structure. Additionally, V-JEPA 2 features obtain limited performance on dense tasks when using a simple linear probing protocol, such as semantic segmentation (22.2 mIoU on ADE20K) or depth estimation (0.682 RMSE on NYUv2), as reported in Table 2.3. Overall, these results support the conclusion that local information about the visual scene is not easily extractable from the V-JEPA 2 representation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Observations and Hypothesis", "weight": 1.0} -->

We hypothesize that the absence of local structure in the feature maps is due to the lack of self-supervision on patches that are not masked, i.e. the context patches. The predictor $P_{\phi}{( \cdot )}$ takes as input the concatenation of context tokens computed by $E_{\theta}{(x)}$ and a set of mask tokens $\Delta_{y}$ that specify the masked positions to predict. The predictor outputs one token for each input, i.e., for both context and masked tokens. However, the original loss from V-JEPA 2 is applied only to the masked tokens, as Equation 1 shows. Therefore, the model has no incentive to encode local information within the context tokens and can instead devote this computation to aggregating global information to minimize $\mathcal{L}_{\text{prediction}}$, similarly to register tokens.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Context Self-Supervision", "weight": 1.0} -->

where $C$ is the set of indexed context tokens, and $\lambda_{i}$ is a patch-specific weighting parameter described in the next section. The model is trained to minimize $\mathcal{L}_{\text{predict}} + \mathcal{L}_{\text{ctx}}$. Figure 3 shows that adding $\mathcal{L}_{\text{ctx}}$ has a significant effect on the learned feature maps. With the context loss, local structure now clearly appears in the feature maps, and similar semantic parts (e.g., head of the dogs, wheel of the car) are mapped to the same PCA components. Additionally, adding $\mathcal{L}_{\text{ctx}}$ significantly improves performance on dense-prediction tasks, achieving $33.9$ mIoU on ADE20K (up from $22.2$), and $0.473$ RMSE on NYUv2 (down from $0.682$). Hence, those results validate that by explicitly supervising context tokens, the model learns features that encode coherent local structure.

<!-- chunk {"id": "body-0017", "role": "body", "section": "V-JEPA 2.1: Improving Dense Video SSL Features", "weight": 1.0} -->

Building on the previous observation, we introduce V-JEPA 2.1, a self-supervised training recipe for learning representations that combine high-quality dense local features with global semantic understanding. Our key algorithmic innovations are Dense Prediction loss that applies self-supervision on both masked and unmasked tokens (Section 2.3.1) and, Deep Self-Supervision of the encoder intermediate layers via a multi-level predictor (Section 2.3.2).

<!-- chunk {"id": "body-0018", "role": "body", "section": "V-JEPA 2.1: Improving Dense Video SSL Features", "weight": 1.0} -->

Additionally, we explore a Multi-Modal Tokenizer with modality-specific patch embeddings for images and videos (Section 2.3.4); Data Scaling through a more diverse and balanced image--video training distribution (Section 2.3.3); and Model Scaling to ViT-G (Section 2.3.5 and High-Resolution Cool-Down ‣ 2.3 V-JEPA 2.1: Improving Dense Video SSL Features ‣ 2 Methodology ‣ V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning")), enabling state-of-the-art downstream performance and effective distillation to smaller models (ViT-L, ViT-B, Section 3.10).

<!-- chunk {"id": "body-0019", "role": "body", "section": "VJEPA 2.1 Architecture", "weight": 1.0} -->

We illustrate the V-JEPA 2.1 architecture in Figure 4. An input, either an image or a video, is projected into a sequence of embedding vectors, or tokens, using a modality-specific patch embedding. Mask corruption is then applied to the sequence by randomly dropping patch tokens. The $x$-encoder processes the remaining visible context tokens and outputs representations from multiple encoder levels in addition to the final output. The multi-level representations are then concatenated along the channel axis and fed to an MLP to reduce their dimensionality. Context tokens are concatenated, along the sequence axis, with learnable mask tokens that carry spatio-temporal positional information of the masked patches. The predictor processes the combined sequence and produces multi-level predictions for each token. Training uses two different losses: (i) an L1 loss on masked-token predictions (the original V-JEPA objective), and (ii) a distance-weighted L1 loss for context tokens. Both use the $y$-encoder outputs as targets, which process the unmasked sequence of patches from the input images or videos.

<!-- chunk {"id": "body-0020", "role": "body", "section": "VJEPA 2.1 Architecture", "weight": 1.0} -->

Losses are applied to several intermediate representation levels in addition to the encoder output.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We follow the warmup-constant learning rate schedule of V-JEPA 2 and we train models for 135,000 iterations. We maintain the teacher EMA coefficient and weight decay at fixed values. Each video sample is a clip of 16 frames at a resolution of $256 \times 256$, and each image sample has a resolution of $256 \times 256$. Additionally, in a second stage we explore the effect of applying a cool-down phase, i.e., decaying the learning rate and increasing the input images and videos resolution. We further train our models for 12,000 iterations during this cool-down phase, increasing the input resolution: video clips now have 64 frames at a resolution of $384 \times 384$, and images have a resolution of $512 \times 512$. Ablation results are reported after the first training phase, whereas final downstream tasks results use the full warmup--constant--cooldown schedule. More details and all hyper-parameters are provided in Appendix 6.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Empirical Evaluation", "weight": 1.0} -->

To evaluate our design choice, we rely on a set of dense-vision tasks (ADE20K and NYUv2) using a linear probing evaluation protocol following Siméoni et al. and global recognition tasks (Something-Somethingv2 for action recognition and ImageNet for object recognition) with an attentive probing protocol following Assran et al.. We ablate the effect of each architecture component in Figure 5 and Table 2.3. In the following, we describe each component in more detail, as well as their impact on downstream performance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dense Prediction Loss", "weight": 1.0} -->

We propose applying our self-supervised loss to both masked and visible patches by minimizing $\mathcal{L}_{\text{dense}} = {\mathcal{L}_{\text{predict}} + \mathcal{L}_{\text{ctx}}}$, where $\mathcal{L}_{\text{predict}}$ is defined in Eq. 1 and $\mathcal{L}_{\text{ctx}}$ is defined in Eq. 2. Naive application of $\mathcal{L}_{\text{ctx}}$ loss leads to poor performance on global semantic tasks, as the system can potentially find trivial solutions, such as copying the context features. We therefore explore various weighting coefficients $\lambda_{i}$ in Eq. 2. Table 2.3 presents an ablation on various weighting schemes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dense Prediction Loss", "weight": 1.0} -->

First, we experiment with fixed values and set all $\lambda_{i}$ to a constant $\lambda$ and try values in the range $\lambda = {\lbrack 0.0,0.05,0.2,0.5,1.0\rbrack}$. We observe that as we increase $\lambda$, the performance in semantic segmentation in the dataset increases significantly up to certain point, but at the cost of the performance in action recognition in the SSv2 dataset decreases. We then introduce a progressive warm-up of $\lambda$ to restore action-recognition performance, with a schedule from epochs 50--100. We found empirically that it greatly stabilizes training. Following, we introduce a dynamic weighting scheme where $\mathcal{L}_{\text{ctx}}$ for a given patch $i$ is weighted by the inverse square root of its minimum spatio-temporal distance to any masked token in the video sequence: i.e. setting

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dense Prediction Loss", "weight": 1.0} -->

in $\mathcal{L}_{\text{ctx}}$ in Eq. 2, where $\text{d}_{\text{min}}$ is the distance, in number of blocks, between a context token and its closest mask token. This weighting emphasizes patches near masked regions by enforcing local continuity between masked and context areas, yielding a good trade-off between segmentation and action recognition performance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dense Prediction Loss", "weight": 1.0} -->

Introducing our novel context loss $\mathcal{L}_{ctx}$ with our weighted scheme improves the performance on dense vision tasks (22.2 $\rightarrow$ 33.9 mIoU, 0.682 $\rightarrow$ 0.473 RMSE on NYUv2). Qualitatively, this loss smooths the feature maps by removing noisy artifacts, as shown in Figure 3. However, Table 2.3 shows that there is still a degradation in video understanding (72.8 $\rightarrow$ 62.5 on SSv2) and image classification (82.2 $\rightarrow$ 72.6 on IN1K).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Deep Self-Supervision", "weight": 1.0} -->

We self-supervise the encoder representation not only at the output but also at multiple intermediate levels. We first concatenate, along the channel dimension, the outputs of three intermediate $x$-encoder blocks, in addition to the output layer. Then, a lightweight MLP fuses these multi-level representations and reduces their dimensionality before feeding them into the predictor. The predictor processes the fused multi-level sequence of context and mask tokens and produces four outputs corresponding to the four encoder layers. Both the prediction loss and the context loss are then applied at each one of these four levels.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Deep Self-Supervision", "weight": 1.0} -->

Deep Self-Supervision leads to significant improvement on downstream performance for both global and dense tasks, as shows Figure 5. Furthermore, it allows local information to flow towards the final layers, effectively removing the need for intermediate layers in dense downstream tasks as we show in Appendix 9.1. Deep Self-Supervision allows to recover the global understanding capabilities of V-JEPA 2 (72.0 on SSv2, 80.8 on IN1K) while improving on dense tasks with the context loss (38.6 mIoU on ADE20K, 0.463 RMSE on NYU).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scaling Image Data", "weight": 1.0} -->

DINOv2 introduced a cluster-based retrieval strategy to select images from a large pool of raw internet data, resulting in a curated set of 142 million images, referred to as the LVD-142M dataset. Using a similar approach, V-JEPA 2 collected and curated video scenes from YT1B videos, combined with other publicly available video datasets, yielding a large-scale collection of 19 million video samples from the internet, corresponding to $1.6$ million hours. Both works demonstrated the positive effect of data scaling for SSL pretraining.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling Image Data", "weight": 1.0} -->

Building on these insights, we construct our VisionMix163M Dataset, combining large-scale curated sources from these two prior works. As we show in Table LABEL:tab:\_datasets, we replace the 1M-image ImageNet subset from VJEPA-2 pretraining data with LVD-142M, providing a broader and more diverse appearance distribution. Since this extensive image collection already covers many static visual concepts, we shift the video sampling strategy towards more dynamic, motion-rich content, increasing the SSv2 sampling weight from 0.056 to 0.170. We also found beneficial to increase the contribution of YT-1B from 0.188 to 0.720, which contains much more heterogeneous video samples.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scaling Image Data", "weight": 1.0} -->

Rather than mixing images and videos within the same training batch, we leverage distributed training by assigning separate workers to each modality. After each iteration, gradients from video-only and image-only nodes are aggregated before updating the model. The image/video ratio is controlled through per-modality batch sizes. Empirically, we found optimal performance with 128 video clips (16 frames each) and 2,304 images per global batch. As we report in Table 2.3, the improvement of training on a more diverse and extend database is beneficial in all tasks (72.1 $\rightarrow$ 72.6 on SSv2, 80.8 $\rightarrow$ 81.6 on ImageNet, 38.6 $\rightarrow$ 40.8 on ADE20K, 0.463 $\rightarrow$ 0.418 RMSE on NYUv2).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Multi-Modal Tokenizer", "weight": 1.0} -->

Previous work exploring joint training on image and video, such as V-JEPA 2, was suboptimal: it employed a single 3D convolution as the patch-embedding layer. Images were duplicated temporally and treated as a 16-frame static video, which significantly increased their computational cost and introduced an incorrect representational bias (i.e., images were interpreted as static videos). Instead, we introduce a multi-modal tokenizer, which applies a 3D convolution of $16 \times 16 \times 2$ for processing videos and a 2D convolution of $16 \times 16$ for images. We also add a modality-learnable token to both the encoder and the predictor inputs, which explicitly encodes whether the input comes from the image or video pathway. These learnable tokens condition the processing on the input modality, helping the model disentangle stronger static appearance cues in images and temporal motion information in videos.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Multi-Modal Tokenizer", "weight": 1.0} -->

This design allows each modality to be processed in its native form, eliminating the need for temporal duplication of images and improving computational efficiency. Additionally, we observe that using the Multi-Modal Tokenizer has a positive effect on dense-task performance: it improves mIoU on ADE20K from $40.8$ to $41.4$, while performance on action or object recognition remains stable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Scaling Model Size to ViT-G (2B) and High-Resolution Cool-Down", "weight": 1.0} -->

Next, we explore the effect of model scaling and high-resolution cooldown. Scaling the V-JEPA encoder from a ViT-L with 300 million parameters to a ViT-G with 2 billion parameters leads to significant improvements on all downstream tasks (72.6 $\rightarrow$ 76.1 on SSv2, 81.6 $\rightarrow$ 84.8 accuracy on ImageNet, 41.4 $\rightarrow$ 47.1 mIoU on ADE20K, 0.415 $\rightarrow$ 0.365 RMSE on NYUv2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Scaling Model Size to ViT-G (2B) and High-Resolution Cool-Down", "weight": 1.0} -->

Additionally, introducing a cool-down phase for the learning rate, during which we increase both the spatial resolution of images (from $256 \times 256$ to $512 \times 512$) and the spatio-temporal resolution of videos (from 16 frames at $256 \times 256$ to 64 frames at $384 \times 384$), further improves performance on all tasks. This achieves an accuracy of $77.7$ on SSv2, $85.5$ on ImageNet, an mIoU of $47.9$ on ADE20K, and an RMSE of $0.307$ on NYUv2, resulting in our best performing model. The benefits of a cool-down training phase are particularly strong in depth estimation (0.365 $\rightarrow 0.307$ RMSE on NYUv2).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Model Distillation", "weight": 1.0} -->

We scaled the size of the model not only to achieve top-tier performance but also to enable effective compression of the model through distillation Hinton et al.. We distill our ViT-G (2B) model into smaller variants (ViT-B, 80M; ViT-L, 300M). The distillation protocol is adapted from our pretraining recipe, with key differences: i) we replace the Exponential-Moving-Average (EMA) of the target encoder by a frozen teacher model, ii) we keep an EMA copy of the student encoder, that is not used in the loss, but serves as the final model, iii) the distillation loss is identical to our pretraining loss, except it is only computed on the last layer of the teacher encoder, and it does not use deep self-supervision, iv) we use a predictor with only 12 blocks and a final linear layer matching the teacher embedding dimension. All other hyper-parameters---including masking ratios, cool-down schedules, learning rates, and data augmentations---remain identical to the original pretraining recipe.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model Distillation", "weight": 1.0} -->

We provide more details on the distillation protocol in Appendix 7.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we evaluate the performance of V-JEPA 2.1 on a large variety of downstream tasks. Throughout the experiments, we employ V-JEPA 2.1 as a frozen encoder, demonstrating the versatility of its features. We first demonstrate the predictive capabilities of V-JEPA 2.1 in two forecasting tasks: short-term object interaction anticipation (Section 3.1) and action anticipation (Section 3.2). We then demonstrate that can leverage V-JEPA 2.1 to learn an action-condition world model and performs robot manipulation (Section 3.3) and navigation tasks (Section 3.4) in zero-shot setup. Then, we evaluate the quality of the learned dense features by assessing the V-JEPA 2.1 performance on single-image depth estimation and semantic segmentation (Section 3.5). Following, we analyze the temporal consistency of V-JEPA 2.1 representations through the video object segmentation task (Section 3.5). We also analyze V-JEPA 2.1 global understanding on two high-level understanding tasks: probe-based video classification and image classification (Section 3.7).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results", "weight": 1.0} -->

Finally, we present results for our smaller distilled models (Section 3.10). We provide more details on the experimental setup and all pretraining hyper-parameters in Appendices 6 and 8.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Short-Term Object Interaction Anticipation", "weight": 1.0} -->

Encoders using our same protocol

<!-- chunk {"id": "body-0041", "role": "body", "section": "Short-Term Object Interaction Anticipation", "weight": 1.0} -->

Short-Term object-interaction Anticipation (STA) consists in predicting future object interaction in a ego-centric scenario, predicting the next active object bounding box $b$, the object noun category $N$ the action verb $V$ and the time until contact ($\delta$). This formulation evaluates fine-grained 2D localization, semantic understanding of objects, temporal reasoning over video dynamics, and the ability to forecast user intentions. Using the Ego-4D STA benchmark, we show that V-JEPA 2.1 outperforms previous state-of-the-art performance by a significant margin due to its high-quality dense features and predictive capabilities.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Task", "weight": 1.0} -->

We evaluate V-JEPA 2.1 on the STA v2 split of Ego4D, which comprises 243 hours of annotated video clips spanning 128 noun and 81 verb categories, with a total of 98,276 training and 47,395 validation samples. We compare against state-of-the-art methods, and we further asses the performance of DINOv2 and DINOv3 image encoders using our proposed attentive probe. Following the evaluation protocol of Grauman et al., we report Top-5 Average Precision (AP) and Top-5 mean Average Precision (mAP) metrics. As in standard mAP, predictions are matched to ground-truth boxes using IoU \> 0.5 and additional class-specific criteria. For instance, the Top-5 mAP All variant requires a correct noun, correct verb, IoU above 0.5, and a time-to-contact $\delta$ prediction within a 0.25-second tolerance.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Task", "weight": 1.0} -->

To address the inherently multi-modal nature of future anticipation---where multiple plausible next-active objects may exist---the metric discounts up to four highest-scoring false positives per example, thereby avoiding penalties for plausible but unannotated predictions. Additionally, we report individual metrics to evaluate the temporal ($\delta$), spatial (bounding boxes), and semantic (noun and verb) dimensions of the task.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

The model receives as input a low-resolution video clip (384 px, 8 frames spanning 0.5 seconds) and a high-resolution image (1080 px) corresponding to the last frame of the clip. Using the frozen encoder of V-JEPA 2.1, we extract last-level features independently from both inputs using the respective patchifier (a 2D convolution for the high-resolution image and a 3D convolution for the video) and adding the corresponding modality embedding. For the video features, we train a four-layer attentive probe, followed by the frame-guided temporal pooling module from Mur-Labadia et al.. This module aggregates the 3D video tokens into a 2D representation that is spatially aligned with the spatial reference of the last frame. The pooled video features are then summed to the image features, and the resulting fused representation is rescaled into four multiscale feature maps, which serve as input to the detection head. To ensure a fair comparison with state-of-the-art methods, we adopt the same detection head utilized in these approaches.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

This head extends Faster R-CNN by adding linear layers to additionally predict the verb category and the time to contact.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

Table 4 presents a comparison with state-of-the-art methods on the Short Term Anticipation task. V-JEPA 2.1 demonstrates achieves the absolute state-of-the-art performance with an overall mAP of 7.71. This represents a relative improvement of approximately 35$\%$ over the previous best method, which introduces task-specific training components. As it is shown by the individual metrics, this gain is primarily driven by improved understanding of the next action 25.8 AP~b+V~ and the time to contact 20.20 AP~b+$\delta$~, 12.9 mAP ~b+$\delta$~. Furthermore, the high-quality V-JEPA 2.1 dense features enable the precise 2D detection of the next-active object bounding boxes, achieving 50.7 AP and surpassing DINOv3 ViT-7B in this category. Qualitative results are shown in Figure 7. V-JEPA 2.1 predicts plausible short-term interactions, with accurate bounding box localization, robust understanding of object categories, and plausible inference of the user next action intentions.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Action Anticipation", "weight": 1.0} -->

Action anticipation consists in predicting the future action given a contextual video clip leading up to some time before the action. Using the Epic-Kitchens-100 (EK100) benchmark, we show that V-JEPA 2.1 outperforms the action anticipation performance of V-JEPA 2, and sets a new state-of-the-art for the task.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Task", "weight": 1.0} -->

The EK100 dataset is comprised of 100 hours of cooking activities recorded from an egocentric perspective across 45 kitchen environments. Each video in EK100 is annotated with action segments, which include a start timestamp, an end timestamp, and an action label. There are 3,568 unique action labels, each consisting of a verb and a noun category, with a total of 97 verb categories and 300 noun categories. The EK100 action anticipation task involves predicting noun, verb, and action (i.e., predicting verb and noun jointly) from a video clip, referred to as context, that occurs before the start timestamp of an action segment. The interval between the end of the context and the beginning of the action segment is the anticipation time, which is set to 1 second by default. Given that different future actions may be possible from a given context, mean-class recall-at-5 is used as the metric to measure performance.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

We employ the same protocol as V-JEPA 2 and use an attentive probe trained on top of the frozen V-JEPA 2.1 encoder and predictor to anticipate future actions. Specifically, we sample a video clip that ends 1 second before an action starts. This video context is fed to the encoder. The predictor takes the encoder representation, along with the mask tokens corresponding to the frame 1 second into the future, and predicts the representation of the future video frame. The outputs of the predictor and encoder are concatenated along the token dimension and fed to an attentive probe with a similar architecture to those used in our probe-based video classification protocol, with the difference being that the anticipation probe's final cross-attention layer learns three query tokens (as opposed to one), and each query output is fed to a different linear classifier to predict the action category, the verb category, and the noun category respectively. A focal loss is applied to each classifier independently and then summed before back-propagating through the shared attention blocks of the probe.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

Table 5 summarizes the results on the validation set of the EK100 action anticipation benchmark. We compare V-JEPA 2.1 ViT-g 1B and ViT-G 2B encoders with V-JEPA 2 ViT-g 1B encoder. Both leverage 32 frames with 8 frames per second at resolution 384 × 384 as video context. V-JEPA 2.1 is comparable to V-JEPA 2 on the same 1B model size, but show scaling of the performance to the 2B models size, setting a new absolute state-of-the-art performance at 40.8 Action Recall@5, corresponding to a $+ {2.8\%}$ improvement.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Robotic Arm Planning", "weight": 1.0} -->

Next, we evaluate V-JEPA 2.1 for robot manipulation. To that end, we train a frame-causal action-conditioned predictor, following the protocol of Assran et al.. In particular, we use the public codebase from Assran et al. and modify it to compute features using our V-JEPA 2.1 video encoder; the predictor is an identical 24-layer transformer network containing approximately 300M parameters, and is trained on the Droid raw dataset using both a teacher-forcing and two-step rollout loss. The model is then deployed in our lab, zero-shot, on a table-top Franka Panda robot arm with a parallel-jaw gripper, and evaluated on reach, grasp, and pick-and-place tasks with visual goal specification via model-predictive control. We use the same exact task configuration files provided in Assran et al., and similar planning hyper-parameters.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Robotic Arm Planning", "weight": 1.0} -->

#Samples
Pick-&amp;-Place

<!-- chunk {"id": "body-0053", "role": "body", "section": "Robotic Arm Planning", "weight": 1.0} -->

Success rates are reported in Table 6. VJEPA 2.1 exhibits an improved depth understanding, leading to a 10% improvement in the success rate of Grasp compared to VJEPA 2 (cf. Figure 8). Moreover, we find that the VJEPA 2.1 model unlocks the benefit of planning with slightly longer rollouts, perhaps due to the improvement in dense features afforded by our model. In particular, by reducing the number of CEM samples and planning over 8 steps, we observe an additional improvement in the success rate on Grasp. By contrast, we actually observe a degradation in the success rate of VJEPA 2 when planning over longer horizons. Qualitatively, we further observe that task failures using the VJEPA 2.1 model on Pick-and-Place and Grasp are a result of poor planning over gripper actions, as opposed to failures in spatial understanding; e.g., closing the gripper too soon such that you cannot grasp the object, or slightly opening the gripper while in transit leading to the object being dropped.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Navigation Planning", "weight": 1.0} -->

Next, we evaluate the utility of V-JEPA 2.1 representations for short-term robotic navigation. Specifically, given an agent's most recent observation and a goal location specified by an image, we predict a 2-second navigation trajectory toward the goal. We adopt the navigation planning setup of NWM and train a latent world model on top of the V-JEPA 2.1 representations. We find that V-JEPA 2.1 enables more accurate planning while achieving $10 \times$ faster planning speed than the previously used SD-VAE. Results are reported in Table 7, with qualitative examples shown in Figure 9.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Navigation Planning", "weight": 1.0} -->

We train a Conditional Diffusion Transformer (CDiT) on top of the V-JEPA 2.1 representations, similarly to NWM. Our initial experiments indicate that directly training a diffusion model in the high-dimensional embedding space of the V-JEPA 2.1 is challenging: because the representations are high-dimensional (at least $80 \times$ larger than those of an SD-VAE), injecting noise in arbitrary directions can easily push samples off the data manifold. To improve robustness, we introduce two modifications. First, we train the model to predict a clean representation rather than noise. Second, we use DDIM sampling, which is less stochastic than DDPM and empirically improves stability.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Navigation Planning", "weight": 1.0} -->

For planning, given an initial context embedding and a goal, we use the Cross-Entropy Method to sample $N = 480$ candidate trajectories of length $2$ seconds at $4$ FPS. We select the best candidate by simulating it in the world model and choosing the trajectory that minimizes the distance to the goal embedding. To simplify the search, we plan in a reduced 3-DoF action space (translation and yaw rotation). With V-JEPA 2.1, we require only $8$ denoising steps, compared to the optimal SD-VAE setting which requires at least $128$ steps. This yields lower Absolute Trajectory Error (ATE) and Relative Trajectory Error (RTE) on the validation set while reducing planning time by $10 \times$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Depth Estimation and Semantic Segmentation", "weight": 1.0} -->

We evaluate the quality of the learned representations on semantic segmentation and depth estimation, two tasks that require fine-grained understanding of the image spatial structure.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Task", "weight": 1.0} -->

Semantic segmentation probes the model's ability to capture category-level semantics and object boundaries. We evaluate our model on PASCAL, ADE20K, and Cityscapes, reporting the mean Intersection over Union (mIoU). As in Siméoni et al., the input resolution of the images is adapted to 1024 patch tokens (${i.e}.$, $512 \times 512$ for patch size 16, $448 \times 448$ for patch size 14). On the other hand, depth estimation evaluates the model's understanding of the scene's geometric structure. For this task, we use the NYUv2 and KITTI benchmarks and report the Root Mean Squared Error (RMSE).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

Following the protocol of DINOv3, we train a dense linear projection on top of the frozen final-layer features of the V-JEPA 2.1 encoder using the image patchifier. Importantly, we do not utilize intermediate layers from the encoder. As V-JEPA 2.1 adopts a 3D RoPe for positional encoding, the frequencies are interpolated according to the image resolution.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results", "weight": 1.0} -->

Table 8 summarizes the performance of V-JEPA 2.1 and other visual encoders on depth estimation and single-image semantic segmentation. V-JEPA 2.1 ViT-G achieves state-of-the-art results on linear-probe monocular depth estimation, reaching 0.307 RMSE on NYUv2 and strong performance on KITTI with 2.461 RMSE, performing best across models that have less than 2 billion parameter. On NYUv2, V-JEPA 2.1 surpasses prior image encoders, including DINOv3 ViT-7B (0.309 RMSE on NYU) and PE~spatial~-G (0.362 RMSE on NYU), and it represents a significant improvement over video encoders such as InternVideo2-1B (0.471 RMSE) and V-JEPA 2 (0.642 RMSE). Figure 10 provides a qualitative comparison of the depth maps predicted by V-JEPA 2 and V-JEPA 2.1. While V-JEPA 2 captures the overall scene geometry, the inconsistencies of its local features lead to noisy depth maps.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results", "weight": 1.0} -->

In contrast, our novel V-JEPA 2.1 produces sharper and more coherent depth maps with well-defined object boundaries. We also visualize a more detailed qualitative comparative with DINOv3 ViT-H+ in Figure 12.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results", "weight": 1.0} -->

In semantic segmentation, V-JEPA 2.1 is also highly competitive with the state-of-the-art models, obtaining 85.0 mIoU, 73.5 mIoU on Cityscapes and 47.9 mIoU on ADE20K. Compared with its previous version V-JEPA 2, the gains are remarkable across all datasets: +23.4 points in ADE20K, +27.6 on Cityscapes, and + 20.7; showing the benefits of explicitly supervising the context tokens and incorporating the multi-level predictor.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results", "weight": 1.0} -->

Performance on ADE20K and Cityscapes remains slightly behind the best image encoders. These datasets contain numerous object classes spanning large scale variations, with cluttered scene layouts that impose strict demands on fine-grained segmentation. We hypothesize that VisionMix contains comparatively fewer highly cluttered scenes, limiting exposure to the level of granularity required by such benchmarks. Figure 11 illustrates segmentation predictions on Cityscapes and. V-JEPA 2.1 yields detailed and spatially accurate masks, capturing multi-scale structures and fine object contours with high fidelity, showing competitive performance with state-of-the-art methods such as DINOv3 ViT-H+.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Video Object Segmentation", "weight": 1.0} -->

We evaluate V-JEPA 2.1 on Video Object Segmentation (VOS) to assess the temporal consistency of its learned features.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Task", "weight": 1.0} -->

Video Object Segmentation consists, given the ground-truth object mask in the first frame, propagating this mask accurately across all subsequent frames. This task evaluates the model's ability to preserve long-range correspondences while remaining robust to camera motion, object deformation, and visual distractions. We evaluate on DAVIS 2017 and YouTube-VOS datasets, reporting the standard $\mathcal{J}\&\mathcal{F}$-mean metric that jointly measures the region similarity and contour accuracy.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

We adopt a non-parametric label propagation approach that matches local patch features across frames using cosine similarity in the embedding space. This procedure introduces no learnable parameters, making it a direct probe of the representation's temporal stability. Following Siméoni et al., input videos are resized to produce a consistent number of patch tokens (short side of 420 px for patch size 14, and 480 px for patch size 16). On the training split of each dataset, we conduct a systematic search of the best hyper-parameters: maximum context length, neighborhood mask size, number of top-$K$ nearest neighbors, and the temperature parameter used in similarity computation. The best configuration in DAVIS-S (15 context frames, circle mask of size 12, top-5 neighbors and temperature = 0.2), was applied to all the validation sets.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results", "weight": 1.0} -->

V-JEPA 2.1 achieves 69.0 $\mathcal{J}\&\mathcal{F}$ on DAVIS-17 and 72.7 $\mathcal{J}\&\mathcal{F}$ on YouTube-VOS datasets, obtaining the second best performance and surpassing all prior encoders except DINOv3, which attains a slightly higher score. These results highlight the temporal consistency of the V-JEPA 2.1 features, which enable stable object tracking despite significant appearance changes across frames. Figure 13 illustrates two qualitative examples: even under fast motion and substantial visual variations, V-JEPA 2.1 maintains consistent object segmentation masks throughout the sequence.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Video and Image Classification", "weight": 1.0} -->

Image Encoders Evaluated Using the Same Protocol

<!-- chunk {"id": "body-0069", "role": "body", "section": "Video and Image Classification", "weight": 1.0} -->

Video Encoders Evaluated Using the Same Protocol

<!-- chunk {"id": "body-0070", "role": "body", "section": "Video and Image Classification", "weight": 1.0} -->

Real-world video reasoning requires recognizing static visual cues (i.e, objects, textures, scene layouts) as well as dynamic patterns (i.e, gestures, hand-object interactions, camera motion, long-term temporal evolution). To capture this dual nature, we evaluate the representations learned during pretraining on four complementary classification datasets. Something-Something v2 and Diving-48 assess motion-centric understanding, as their labels require modeling multi-frame dynamics to correctly identify the action. In contrast, Kinetics-400 and ImageNet-1K primarily measure appearance-based recognition, since many of their classes can be predicted from a single frame, even when the label describes an action.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Task", "weight": 1.0} -->

We compare the video classification performance of V-JEPA 2.1 against a broad set of visual encoders. For image-based self-supervised models, we include DINOv2 with registers and the more recent DINOv3, both representing state-of-the-art in image-only pretraining. We further evaluate against leading image--text contrastive approaches, including SigLIP2 and the Perception Encoder PE~core~G. For video models, we benchmark against the previous V-JEPA and V-JEPA 2, as well as InternVideo2s2-1B, a state-of-the-art video encoder trained primarily through vision--text contrastive objectives.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Task", "weight": 1.0} -->

In addition, we report comparisons with results available in the literature for VideoMAEv2, InternVideo2-1B, VideoPrism, and DINOv3. Note that these models are evaluated under similar frozen-probe protocols, but their attentive heads differ from ours. For instance, DINOv3 augments its probe with explicit spatial and temporal positional embeddings and applies a 3D factorized RoPE across its attention blocks. In contrast, our V-JEPA 2.1 encoder already encodes spatio--temporal structure in its features, allowing our probe to operate without such additional components.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

Following the protocol proposed by Assran et al., we train a 4-layers attentive probe on top of the frozen encoder features using the respective training data from each task. The attentive probe consists of four transformer blocks followed by a final cross-attention mechanism that employs a learnable query token. At inference, we sampled several clips with a fixed number of frames from the video, and we averaged the classification logits across clips.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Results", "weight": 1.0} -->

Table 9 summarizes the global video understanding performance of V-JEPA 2.1, previous V-JEPA models, and other strong visual encoders. V-JEPA 2.1 ViT-G achieves a top-1 accuracy of 77.7 on SSv2, setting a new absolute state-of-the-art on the task compared to 77.5 for InternVideo2 full fine-tuning, 77.3 for V-JEPA 2, 70.1 for DINOv3 ViT-7B and 69.7 for InternVideo2 using the same protocol, demonstrating a strong understanding of video dynamics. Our model is also highly-competitive in appearance-based tasks, reaching 87.7 on K400 and 85.5 on IN1K. These results show that properly designing the loss over context tokens, together with deep self-supervision, enables fine-grained dense features that also capture strong global scene understanding. We also observe consistent improvements with model scaling from ViT-g to ViT-G with an average improvement of +0.6 points.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Video Question Answering", "weight": 1.0} -->

In this section, we evaluate V-JEPA 2.1 on Video Question Answering (VidQA), by training a Video Large Language Model (VidLLM) using V-JEPA 2.1 encoder and Llama 3.1 8B LLM as the backbone, following the recipe proposed by Assran et al..

<!-- chunk {"id": "body-0076", "role": "body", "section": "Video Question Answering", "weight": 1.0} -->

≤ 8 B Video Language Models Results Reported in the Literature

<!-- chunk {"id": "body-0077", "role": "body", "section": "Video Question Answering", "weight": 1.0} -->

Models trained in this paper using filtered Perception LM data

<!-- chunk {"id": "body-0078", "role": "body", "section": "Task", "weight": 1.0} -->

We compare the VidQA performance of V-JEPA 2.1 with popular open-source multimodal models reported in the literature, where the LLM backbone size is $\leq$ 8B. Following the protocol set of Assran et al., we report performance on video understanding benchmarks which require rich visual and temporal understanding, such as PerceptionTest, Minimal Video Pairs (MVP), TempCompass, TemporalBench, TOMATO and MVBench.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

We train our Video-LLM model using a subset of PerceptionLM that is publicly available. Starting with this data, we perform data quality filtering using domain filters, vision-text misalignment filters, and an external multimodal LLM, Qwen3VL, as a data-quality judge, assigning scores to each data samples. This process resulted us to filter out and remove 18% of the training data. It is important to note that we do not rephrase any data from PerceptionLM using this setup - we only filter the data based on the model's judgement.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Evaluation protocol", "weight": 1.0} -->

We reproduced LLM alignment of VJEPA 2 on this new data, and compare our model, VJEPA 2.1, with it. We follow the same three-stage training procedure from Assran et al. to train VJEPA 2.1 LLM, starting from image-text captioning to progressively training on higher quality image and video-text captioning and QA data. We further add a fourth stage of alignment, where we expand the context length of the base LLM to support 64 frames of video input, compared to 32 frames supported by VJEPA 2. We primarily use VJEPA 2.1 in video-only mode in our experiments, to better compare with VJEPA 2. Interestingly, we find adding a final post-training stage using PerceptionTest training set further improves performance on all downstream tasks.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results", "weight": 1.0} -->

Table 10 summarizes the results on VidQA evaluation tasks. Comparing VJEPA 2 and VJEPA 2.1 on the same data, we find on average VJEPA 2.1 to be slightly better, with significant improvements on PerceptionTest, Minimal Video Pairs, and crucially, improvement on datasets requiring rich visual semantics - MVBench and TVBench. We observe VJEPA 2.1 to be worse on TemporalBench and TOMATO - both datasets requiring understanding of the motion events, but on shorter videos.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Results", "weight": 1.0} -->

Compared to results reported in the literature, VJEPA 2.1 slightly underperforms results reported Assran et al. which uses significantly alignment data (88.5 million samples in vs 72.5 million samples in VJEPA 2.1) Nevertheless, VJEPA 2.1 is competitive with state-of-the-art, outperforming most open-source multimodal LLMs with similar model size.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Family of distilled models", "weight": 1.0} -->

We follow the same protocol to evaluate our distilled ViT-L and ViT-B models. Table 11 presents our results, where we observe a significant improvement in all our benchmarks between the ViT-L trained from scratch and the ViT-L distilled from ViT-G, almost closing the gap with ViT-G performance. On action recognition on SSv2, performance improves from 74.2% to 76.5%, almost reaching 77.7% from ViT-G. In image segmentation, performance improves from 42.0 mIoU to 46.7 mIoU. In depth estimation and video segmentation, the ViT-L distilled is even closer to ViT-G, with 2.490 RMSE on KITTI, close to 2.461 RMSE, and 68.7 $\mathcal{J}\&\mathcal{F}$-Mean on DAVIS, close to 67.0 $\mathcal{J}\&\mathcal{F}$-Mean. Finally, our ViT-B offers competitive performance with our ViT-L trained from scratch.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Family of distilled models", "weight": 1.0} -->

#Params

<!-- chunk {"id": "body-0085", "role": "body", "section": "Self-Supervised Learning", "weight": 1.0} -->

Early SSL approaches in vision focus on simple pretext tasks such as predicting the relative position of image patches, reordering shuffled patches, inpainting missing regions, re-colorizing grayscale images, or predicting applied image transformations. Beyond hand-crafted tasks, view-invariant approaches proposed to use a joint-embedding architecture to learn invariances to visual transformations, which led to significant advances in SSL, with contrastive approaches, non-contrastive approaches, or clustering-based techniques. Later, the adoption of vision transformers became the standard in self-supervised learning, first by revisiting existing view-invariant approaches, and then with masked image modeling approaches, which can operate in pixel space, or in the latent space of the transformer. Most powerful approaches employ a combination of view-invariant and masked image-modeling techniques. The concept of learning representations by predicting missing information in latent space is formalized by the Joint-Embedding Predictive Architecture (JEPA), which have been successfully applied across multiple modalities, including audio, images, and video.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Video Models", "weight": 1.0} -->

Motion cues from videos have inspired many early video pretext tasks. Early methods predicted camera transformations between image pairs or future frames from ego-motion. Others brought consecutive frame patches closer in feature space or used unsupervised object retrieval for segmentation. The rise a large labeled video datasets such as Kinetics changed the focus of the community towards supervised video models. Early approaches used image sequences with late fusion or 3D convolutions, but 3D ConvNets are computationally expensive. Recent work improves efficiency with 2D spatial and 1D temporal convolutions, dual-pathways, and vision transformers adapted for video. Despite rapid progress, supervised learning requires extensive labeled data and may not fully exploit temporal information, and the focus went back to self-supervised learning.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Video Models", "weight": 1.0} -->

Early self-supervised learning methods focused on temporal order verification, contrastive learning, and future prediction. Recent masked modeling approaches, like VideoMAE, extend image-based masking to video. Other advances include masked modeling in CLIP space, joint image-video training (OmniMAE ), and architectural innovations such as hierarchical transformers and decoupled encoders/decoders. Despite progress, defining optimal pretext tasks and efficient video processing remain open challenges.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Video Models", "weight": 1.0} -->

Scaling existing approaches, both in terms of data and model size, has demonstrated that generalist video encoders can be learned from extensive observation datasets of videos using self-supervised learning. In particular, Joint-Embedding Predictive architectures show promising efficiency gains at large scale compared to generative approaches, and open the door to applications in world modeling. Self-supervised models can also incorporated weak language supervision, unlocking language-based tasks.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Learning dense features", "weight": 1.0} -->

Learning dense features is often achieved through designing local loss functions and objectives, such as leveraging spatio-temporal consistency in videos, spatial alignment between image crops, and patch consistency. Contrastive learning approaches such as DetCon and ORL use region proposals, while newer methods relax this requirement. Recent distillation-based methods combine strengths from multiple encoders, such as AM-RADIO, Perception Encoder, and DINOv3, using objectives like cosine similarity and Gram matrix regularization to improve dense features. Some works focus on post-hoc improvements, including fine-tuning with clustering objectives, patch alignment, and patch-sorting. Others enhance features without fine-tuning, such as STEGO and feature augmentation.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Learning dense features", "weight": 1.0} -->

Beyond playing with the loss function, the standard Vision Transformer (ViT) can be adapted for dense prediction tasks, Ranftl et al. introduced the Dense Prediction Transformer (DPT), evolving from their prior CNN-based work on MiDaS. DPT solved the token-to-pixel problem using a \"reassemble\" operation that converts the 1D ViT sequence into multi-scale 2D feature maps, which are then fused by a convolutional decoder adapted from RefineNet. This design, which leverages the global receptive field of the transformer backbone, proved effective for obtaining structural coherence, moving beyond the limitations of purely hierarchical CNNs. The work also catalyzed parallel research, including the development of purely transformer-based decoders like Segmenter and hierarchical transformer backbones like the Swin Transformer and the Multiscale Vision Transformer. DPT architectural framework has proven to be the most influential design for scaling up, serving as the basis for current state-of-the-art foundation models like Depth Anything.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Conclusion and Future work", "weight": 1.5} -->

This work demonstrates how Joint-Embedding Predictive Architectures and Self-Supervised Learning from video unlock high-quality dense local features with strong global semantic understanding. Our key ingredient is a novel deep spatio-temporal self-supervision, composed by a weighted context loss and a multi-level predictor that enables supervision across the intermediate encoder layers. This design unlocks high-quality dense features that are spatially structured, semantically coherent and temporally consistent, as evidenced by PCA visualizations. Beyond the training objective, we demonstrate the importance of modality-specific tokenizers, large-scale and balanced image--video data curation, and scaling to ViT-G, which together enable an effective distillation to compact models. Our V-JEPA 2.1 ViT-G achieves absolute state-of-the-art performance in short-term object interaction anticipation, action anticipation and action recognition, showcasing its excellent predictive and motion understanding capabilities. Moreover, the dense feature maps achieve linear-probe state-of-the-art performance in monocular depth estimation and strong results in semantic segmentation and video object tracking. We hope these findings encourage further research on predictive physical world modeling.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Future work", "weight": 1.5} -->

Future work will focus on several promising directions. First, scaling along two axes: a) model size, we observe a very positive trend scaling from 1B to 2B and other work such as DINOv3 showed the benefit of scaling to 7B in vision; b) data size, our work on data curation highlighted that video self-supervised learning really benefit from large-scale datasets. Second, this work focus on learning better representation, whereas V-JEPA 2 showed the potential of building world models on top of these representations. Future work in this direction will explore world modeling aspects with the prism of learning dense prediction capabilities. Finally, world models with dense understanding and prediction abilities will unlock many applications in robotics and autonomous agents, where a precise estimation of the state down to the pixel level is required, for example navigation in challenging real world environment, or fine-grained manipulation.
