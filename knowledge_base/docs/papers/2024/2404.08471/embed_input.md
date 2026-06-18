<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Revisiting Feature Prediction for Learning Visual Representations from Video

Topics include Supervised learning, Unsupervised learning, Datasets, Learning, V-JEPA.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper explores feature prediction as a stand-alone objective for unsupervised learning from video and introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective, without the use of pretrained image encoders, text, negative examples, reconstruction, or other sources of supervision. The models are trained on 2 million videos collected from public datasets and are evaluated on downstream image and video tasks. Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model's parameters; e.g., using a frozen backbone. Our largest model, a ViT-H/16 trained only on videos, obtains 81.9% on Kinetics-400, 72.2% on Something-Something-v2, and 77.9% on ImageNet1K.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Humans possess the remarkable ability to map low-level signals originating from the retina into a semantic spatio-temporal understanding of the world; synthesizing notions such as objects and global motion. A long-standing goal of the machine learning community is to identify the principles or objectives that may guide such unsupervised learning in humans (Field Berkes and Wiskott Hinton, ). One related hypothesis is based on the *predictive feature principle*, which posits that representations of temporally adjacent sensory stimuli should be predictive of each other.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we revisit feature prediction as a stand-alone objective for unsupervised learning of visual representations from video. Numerous advances in the field --- such as the standard use of transformer architectures in vision, the maturing of masked autoencoding frameworks (Xie et al. Bao et al. He et al., ), query-based feature pooling, joint-embedding predictive architectures (JEPA), and larger datasets --- form a unique arsenal of tools, which we integrate in a modern and conceptually simple method, the *video joint-embedding predictive architecture* or V-JEPA, which is based solely on feature prediction, without using pretrained image encoders, text, negative examples, human annotations, or pixel-level reconstruction.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

> How effective is feature prediction as a stand-alone objective for unsupervised learning from video with modern tools?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To that end, we pretrain a family of V-JEPA models on a dataset of 2 million videos collected from publicly available datasets by combining a masked modeling prediction task with a joint-embedding predictive architecture. We measure performance on several downstream image and video tasks, using both frozen evaluation and end-to-end fine-tuning. Our findings suggest that feature prediction can indeed serve as an effective stand-alone objective for unsupervised learning from video, while using significantly shorter training schedules than pixel prediction methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Feature prediction leads to versatile visual representations that perform well across downstream image and video tasks without adaption of the model's weights; i.e., using a frozen backbone. V-JEPA achieves the best performance among methods we consider (+6% accuracy) on the SomethingSomething-v2 task, which requires fine-grained temporal understanding. V-JEPA is also competitive on tasks like Kinetics400, where appearance-based features are sufficient and hence state-of-the-art image models such as DINOv2 excel (Figure and Table ).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Models trained with feature prediction are superior to pixel prediction approaches under a frozen evaluation protocol (attentive probing) and are competitive with pixel prediction under full fine-tuning, while using significantly shorter training schedules (Tables and ).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Models trained with feature prediction are more label-efficient than pixel prediction approaches. Decreasing the available number of labeled examples results in an increase in the performance gap between V-JEPA and pixel-reconstruction models.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Slow Features", "weight": 1.0} -->

One way to encourage temporally adjacent representations to be predictive of each other is to ensure that they vary slowly over time. Early works targeting predictive features encouraged representations of individual video frames to be locally temporally invariant, while preventing representation collapse by using spectral methods, as in SFA, SSA, and Simulated Fixations. More recently, Goroshin et al.; Wang et al. train a siamese convolutional network to map the representations of two subsequent frames to the same point, while encouraging distant frames to have diverse representations via a pair-wise margin loss and a triplet loss, respectively. Other works (Oord et al. Surís et al. Feichtenhofer et al., ) implement temporal invariance using noise-contrastive estimation. Our exploration in this paper goes beyond temporal invariance and explores feature prediction using masked modeling.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Predictive Features", "weight": 1.0} -->

Going beyond local invariance, a family of works trains a predictor network to map the representation of a frame or clip at one time-step to a distinct representation at another time-step. Srivastava et al.; Vondrick et al.; Wang et al. train such a video feature predictor network on top of a frozen pretrained image or video encoder. Unfreezing the target feature extractor, several methods train the video encoder and the predictor network simultaneously, while preventing collapse by using a supervised action forecasting loss, or by using the representations of distant clips as negative samples in a contrastive loss (Han et al. Tan et al., ), often focusing on small convolutional encoders (Han et al. ). The idea of learning a representation by predicting missing information in feature space is also core to the joint-embedding predictive architecture (JEPA), which combines a siamese encoder with a predictor network. JEPAs have been successfully instantiated in several modalities, such as with audio data and image data (Zhou et al. Oquab et al. Assran et al., ).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Predictive Features", "weight": 1.0} -->

In this work, we extend this paradigm to video data by leveraging recent advances in self-supervised learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Advances in Self-Supervised Learning", "weight": 1.0} -->

The use of vision transformers (Dosovitskiy et al. Li et al., ) has become standard practice in self-supervised learning with joint-embedding architectures (Chen et al. Caron et al. Oquab et al. Zhou et al. Assran et al., ), and unlocked masked image modeling in pixel space by parameterizing the pixel decoder as a transformer with learnable mask tokens (Dosovitskiy et al. Xie et al. He et al. Bao et al., ), demonstrating a step-change in the representation quality of autoencoding methods. This line of generative methods was subsequently extended to video data using spatio-temporal masking. It was also recently shown that the representations of masked image autoencoders could be significantly improved by using learnable pooling mechanisms based on cross-attention. Finally, through careful selection of design choices, the non-contrastive collapse prevention strategy in BYOL was recently made to work with image feature prediction methods, which demonstrated the ability to learn representations that can be leveraged for various downstream tasks without relying on invariance to hand-crafted image transformations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Feature Prediction versus Pixel Reconstruction", "weight": 1.0} -->

Approaches that predict in pixel space must dedicate significant model capacity and compute to capture all the low-level detail in the visual input. By contrast, approaches that predict in latent space have the flexibility to eliminate irrelevant or unpredictable pixel-level details from the target representation. Predicting in representation space has been shown to lead to versatile representations that perform well across many downstream tasks through linear probing or low-shot adaptation (Assran et al. Oquab et al. Assran et al., ), while demonstrating an efficiency gain during pretraining compared to pixel level reconstruction. The works of Baevski et al. additionally show that predicting in representation space results in competitive end-to-end fine-tuning performance in the image, audio and text domains. In this work, we extend these findings to the video modality.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Methodology: Video-JEPA", "weight": 1.0} -->

Our goal is to explore the effectiveness of feature prediction as a stand-alone objective for learning visual representations from video. To that end, we use a joint-embedding predictive architecture (JEPA); see Figure. The main idea behind a JEPA is to learn by predicting the representation of an input $y$ from the representation of another input $x$. The basic architecture is made up of an encoder, $E_{\theta}{( \cdot )}$, which computes the representation of the inputs, and a predictor, $P_{\phi}{( \cdot )}$, which predicts the representation of $y$ from the representation of $x$, conditioned on a variable $z$ indicating the transformation (or corruption) between $x$ and $y$. Conditioning on $z$ enables the generation of distinct predictions for various transformations of $x$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Training Objective", "weight": 1.0} -->

We train our visual encoder $E_{\theta}{( \cdot )}$ to satisfy the constraint that representations computed from one part of the video, $y$, should be predictable from representations computed from another part of the video, $x$. The predictor network $P_{\phi}{( \cdot )}$, which maps the representation of $x$ to the representation of $y$, is trained simultaneously with the encoder, and is provided specification of the spatio-temporal positions of $y$ through the conditioning variable $z\leftarrow\Delta_{y}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Training Objective", "weight": 1.0} -->

Naively implementing the objective using the regression

<!-- chunk {"id": "body-0018", "role": "body", "section": "Training Objective", "weight": 1.0} -->

would admit a trivial solution, where the encoder outputs a constant representation, regardless of its input. In practice, we use the following modified objective to prevent representation collapse,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training Objective", "weight": 1.0} -->

where $\text{sg}{( \cdot )}$ denotes a stop-gradient operation, which does not backpropagate through its argument, and ${\overline{E}}_{\theta}{( \cdot )}$ is an exponential moving average of the network $E_{\theta}{( \cdot )}$. The use of an exponential-moving average feature extractor along with a stop-gradient and a predictor has been used as a collapse prevention strategy for image pretraining, and studied empirically and theoretically. In fact, the objective in equation is similar to the loss of Assran et al. used for image pretraining, but we modify it to use an $\ell_{1}$ regression, which we found to be more stable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Theoretical motivation", "weight": 1.0} -->

A theoretical motivation for the effectiveness of this collapse prevention strategy was proposed in Grill et al. for the BYOL method. We provide a simple adaptation of their analysis for our $\ell_{1}$ loss. For ease of exposition, we will disregard the effect of the conditioning variable $z$ and consider one dimensional representations. Denote the representation ${\overline{E}}_{\theta}{(y)}$ by a random variable $Y$. The optimal predictor under equation is thus given by the following functional expression,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Theoretical motivation", "weight": 1.0} -->

Substituting this expression for the optimal predictor into the loss function and evaluating the expected gradient of the encoder gives

<!-- chunk {"id": "body-0022", "role": "body", "section": "Theoretical motivation", "weight": 1.0} -->

where $\text{MAD}{( \cdot |E_{\theta}{(x)})}$ is the median absolute deviation of a random variable conditioned on $E_{\theta}{(x)}$. Thus, in the case where the predictor is optimal, the encoder must learn to capture as much information about the video as possible to minimize the deviation of the target. The hypothesis is that incorporating an exponential moving average to compute the representation of $y$ ensures that the predictor evolves faster than the encoder and remains close to optimal, thereby preventing collapse.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Prediction Task: Predicting $y$ from $x$", "weight": 1.0} -->

The feature prediction task is based on a masked modeling formulation (He et al. Tong et al., ); i.e., regions $x$ and $y$ from the video are sampled using masking. To sample $y$ from a video, we sample several (possibly overlapping) spatially continuous blocks with various aspect ratios and repeat the spatial blocks across the entire temporal dimension of the video; $x$ is taken to be the complement. Masking a large continuous block that covers the full temporal dimension limits information leakage due to the spatial and temporal redundancy of videos, and results in a harder prediction task.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Prediction Task: Predicting $y$ from $x$", "weight": 1.0} -->

We leverage two types of masks: short-range masks, where we take the union of $8$ randomly sampled target blocks covering 15% of each frame, and long-range masks, where we take the union of $2$ randomly sampled target blocks covering 70% of each frame. In both cases, the aspect ratio for all sampled blocks is randomly chosen in the range $(0.75,1.5)$. Given that both short-range and long-range masks are produced by sampling many blocks and taking their union, the result is an average masking ratio of $\sim {90\%}$. We refer to our masking strategy as multi-block, and compare it to other possible masking strategies in Section.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Network Parameterization", "weight": 1.0} -->

We use a Vision Transformer (ViT) (Dosovitskiy et al. Arnab et al., ) as our video backbone. To process a video with a transformer network, we split the video clip into a 3D grid of $L$ spatio-temporal patches, where a patch consists of a $16 \times 16$ pixel block spanning $2$ consecutive frames; we refer to these spatio-temporal patches as tokens. This sequence of tokens is then directly processed by the stack of transformer blocks. Inputs $x$ and $y$ correspond to masked regions of a video, we apply the video masks by simply dropping a subset of the tokens. We apply masking at the input of the $x$-encoder, and at the output of the $y$-encoder to construct contextualized targets. The encoder is parameterized using standard ViT networks, while the predictor is a narrow transformer implemented using $12$ blocks with an embedding dimension of $384$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Network Parameterization", "weight": 1.0} -->

Taking inspiration from masked autoencoders, our predictor takes as input the sequence of embeddings produced by the $x$-encoder as well as a sequence of learnable mask tokens with positional embeddings indicating the spatio-temporal positions of the $y$ tokens. The output of the predictor is an embedding vector for each mask token; see Figure and refer to Appendix for more details.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Network Parameterization", "weight": 1.0} -->

#Samples

<!-- chunk {"id": "body-0028", "role": "body", "section": "Pretraining", "weight": 1.0} -->

We combine several public datasets to construct an unsupervised video pretraining dataset, which we refer to as VideoMix2M. Specifically, we combine the videos from HowTo100M (HT), Kinetics-400/600/700 (K710), and Something-Something-v2 (SSv2), and remove any overlap with the validation sets of Kinetics-400/600/700 and Something-Something-v2, resulting in approximately 2 million videos. We train a ViT-L/16, a ViT-H/16, and a ViT-H/16~384~ transformer model on VideoMix2M. We use a batch size of 3072 for the ViT-L/16 and ViT-H/16 models, and a batch size of 2400 for the ViT-H/16~384~ model. Each model takes as input a video clip of 16 frames sampled with a frame-skip of 4, corresponding to roughly 3 second clips on average.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Pretraining", "weight": 1.0} -->

The ViT-L/16 and ViT-H/16 process the video at a spatial resolution of 224, while the ViT-H/16~384~ uses an input resolution of 384; cf. Appendix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Pretrained models are evaluated on downstream video and image tasks. On video tasks, we use a subset of the VideoGLUE benchmark to test for various capabilities; specifically, we investigate action recognition on Kinetics-400 (K400), motion classification on Something-Something-v2 (SSv2), and action localization on AVA. Action classification on Kinetics evaluates the appearance-based understanding of the model, as many action classes in the dataset can be inferred from the presence of specific objects in the video. Motion classification on Something-Something-v2 evaluates the temporal understanding of the model, as action classes in the dataset are decoupled from the appearance/presence of specific objects in the video. Finally, action localization on AVA evaluates the ability of the model to understand and localize motions in the video. We follow standard practice and report accuracy on K400 and SSv2 by sampling several spatial and temporal views. For static image tasks, we explore object recognition on ImageNet, scene classification on Places205, and fine-grained recognition on iNaturalist 2021.

<!-- chunk {"id": "body-0031", "role": "body", "section": "What Matters for Learning Representations from Video?", "weight": 1.0} -->

In this section we isolate the contributions of several design choices, including: a) the use of a feature prediction versus pixel prediction objective, b) the construction of the pretraining data distribution, c) the feature pooling strategy for leveraging the model's representations in downstream tasks, and d) the masking strategy, towards identifying: what to predict from what?

<!-- chunk {"id": "body-0032", "role": "body", "section": "Predicting Representations versus Pixels", "weight": 1.0} -->

We first ablate the effect of computing the prediction loss in representation space. We train a pair of ViT-L/16 models using either a V-JEPA feature prediction loss, or a mean-squared error loss with the normalized pixel values, as in masked autoencoders, and perform a sweep over the learning rate and weight decay schedules for both approaches. All models are pretrained on VideoMix2M for 90K iterations with a batch size of 3072 using multi-block masking. We examine performance on Kinetics-400 (K400), Something-Something-v2 (SSv2), and ImageNet-1K (IN1K), using a frozen backbone with an attentive probe, and report top-1 accuracy using a single center view. We also examine end-to-end fine-tuning performance of the models on Kinetics-400.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Predicting Representations versus Pixels", "weight": 1.0} -->

Results of this comparison are reported in Table and indicate that predicting in feature space provides a consistent performance improvement over pixel space prediction in both frozen evaluation of the video backbone, as well as end-to-end fine-tuning.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Pretraining Data Distribution", "weight": 1.0} -->

Next we study the impact of the pretraining data distribution in Table. Leveraging large scale datasets has been critical for enabling the surge of advancements in other modalities, such as text and images (Kaplan et al. Cherti et al., ). We investigate whether a similar trend holds for video data. To control for the possible confounding variable of compute budget, we pretrain all models in Table for 90K iterations using a batch-size of 3072. We report downstream results on K400, SSv2, and IN1K using a frozen backbone with an attentive probe, and report top-1 accuracy using a single center view.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Pretraining Data Distribution", "weight": 1.0} -->

Table shows that average performance across tasks monotonically increases as we increase the size of the pretraining dataset, but the best task-specific performance is obtained by independently selecting the pretraining data for each specific downstream task. For instance, the L/16 obtains its best SSv2 performance when pretrained on K710+SSv2, its best K400 performance when pretrained only on K710, and its best IN1K performance when pretrained only on K710+HT. The best average performance across all tasks is achieved by pretraining VideoMix2M, which combines all the data sources. Similarly, the H/16 pretrained on K710+SSv2 achieves a greater K400 score than the H/16 pretrained on VideoMix2M, however, the top performing H/16 on average is pretrained on VideoMix2M.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation: Attentive Probing", "weight": 1.0} -->

Next we explore the feature pooling strategy for applying the model's representations in downstream tasks. Since the prediction objective in equation is unnormalized, there is no a priori reason for the encoder to yield a linearly separable subspace. Thus, rather than using a linear operation (averaging) to pool the features output of the frozen backbone, we explore a learnable non-linear pooling strategy. Specifically, when evaluating the frozen pretrained backbone on downstream tasks, we learn a cross-attention layer with a learnable query token. The output of the cross-attention layer is then added back to the query token (residual connection), and then fed into two-layer MLP with a single GeLU activation, followed by a LayerNorm, and finally a linear classifier.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluation: Attentive Probing", "weight": 1.0} -->

In Table we see that using adaptive pooling with a learnable cross-attention layer leads to a significant improvement of $+ 17$ points on K400 and $+ 16.1$ points on SSv2. Using an attentive-probe is also beneficial for other baseline models as reported in Appendix.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Prediction Task: Predicting $y$ from $x$", "weight": 1.0} -->

We conduct an ablation on the masking strategy used in V-JEPA pretraining. We examine the following masking strategies: random-tube\[r\] in which $x$ is obtained by removing a random fraction $r$ of tubes (spatial patches extended across the entire temporal duration) from the video, causal multi-block\[p\] in which $x$ is restricted to the first $p$ frames of the 16-frame video, which are then masked with a random set of spatio-temporal blocks, and multi-block in which $x$ obtained by masking a random set of spatio-temporal blocks from the entire video. Spatio-temporal blocks are sampled using the parameters described in Section 3.2; an ablation on the size and quantity of masked spatio-temporal blocks is provided in Appendix 12.4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Prediction Task: Predicting $y$ from $x$", "weight": 1.0} -->

Table indicates that the best results are obtained by sampling $x$ using a multi-block strategy, wherein the network is forced to make predictions after removing large continuous blocks in the video. When $x$ is only sampled from the first few frames of the video, as in the causal multi-block strategy, we observe a decrease in downstream performances. Finally, the random-tube strategy, wherein 90% of the tubes in the video are randomly masked, leads to features of low-semantic quality when combined with our feature prediction objective.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Prediction Task: Predicting $y$ from $x$", "weight": 1.0} -->

#Samples

<!-- chunk {"id": "body-0041", "role": "body", "section": "Prediction Task: Predicting $y$ from $x$", "weight": 1.0} -->

Methods pretrained using pixel prediction

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison with Prior Work", "weight": 1.0} -->

In Section 5.1, we investigate the impact of feature prediction by comparing V-JEPA with video approaches that rely on pixel prediction, while using a similar architecture for all baselines. Subsequently, in Section 5.2, we remove the architectural constraint and report the best performance across architectures for self-supervised video and image pretraining approaches. Finally, we explore the label-efficiency of V-JEPA relative to other self-supervised video pretraining approaches in Section 5.3. We further detail the evaluation setup in Appendix.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison with Pixel Prediction", "weight": 1.0} -->

To investigate the effectiveness of feature prediction pretraining, we first compare V-JEPA to video masked modeling models relying on a pixel prediction loss. We control for the possible confounding factor of model architecture by evaluating all models using either a ViT-L/16 encoder, or a Hiera-L encoder, which has a similar number of parameters. For the pixel prediction baselines we consider VideoMAE, which trains vision transformer autoencoders exclusively on video, Hiera, which trains a hierarchical transformer autoencoder on video, and OmniMAE, which trains a vision transformer autoencoder on static images and video simultaneously.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison with Pixel Prediction", "weight": 1.0} -->

Table examines both frozen evaluation with an attentive probe on downstream video and image tasks, as well as end-to-end fine-tuning. In frozen evaluation, V-JEPA outperforms the baselines on all downstream tasks, except ImageNet, where we achieve $74.8\%$ compared to $75.1\%$ of an OmniMAE model trained directly on ImageNet; hence, V-JEPA achieves comparable ImageNet performance despite only pretraining on video.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison with Pixel Prediction", "weight": 1.0} -->

Under the fine-tuning protocol, V-JEPA also achieves the best performance of any model trained with a ViT-L/16, and matches the performance of the Hiera-L on SSv2, which benefits from a hierachical prior. The V-JEPA models achieve this result while processing significantly fewer samples during pretraining, demonstrating the efficiency of feature prediction as a learning principle.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison with State-of-the-Art", "weight": 1.0} -->

Next, in Table, we inspect how the V-JEPA models pretrained on video stack up next to the largest state-of-the-art self-supervised image and video models when freezing the backbone encoder and training an attentive probe on top. Our image pretrained baselines include OpenCLIP, DINOv2, and I-JEPA. The OpenCLIP model is trained with a contrastive image-text alignment objective, DINOv2 and I-JEPA are trained with self-supervision. These models are known to excel in their frozen-evaluation performance; i.e., their ability to produce visual features that can be applied to many downstream tasks simultaneously, without end-to-end fine-tuning, and thus provide highly competitive baselines. Our video pretrained baselines include VideoMAE, OmniMAE, Hiera, VideoMAEv2, and MVD. The OpenCLIP, DINOv2 and VideoMAEv2 models are parameterized as Giant/Gigantic vision transformer architectures containing over 1B parameters trained on large-scale image or video datasets.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison with State-of-the-Art", "weight": 1.0} -->

(∼29 samples per class)
(∼58 samples per class)
(∼287 samples per class)
(∼48 samples per class)
(∼96 samples per class)
(∼440 samples per class)

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison with video models", "weight": 1.0} -->

Compared to large-scale video baselines, the V-JEPA models outperform all previous models on every downstream video and image task with notable margin. Our H/16 model outperforms the largest publicly available VideoMAE, VideoMAEv2, OmniMAE, MVD, and Hiera models by at least $+ 5$ points in motion understanding (Something-Something-v2), $+ 2$ points in action recognition (Kinetics-400), $+ 5$ points on action detection (AVA), $+ 1$ point on object recognition (ImageNet-1K), $+ 2$ points in scene recognition (Places205), and $+ 0.2$ points on fine-grained recognition (iNaturalist). Moreover, when comparing pretraining wallclock time in Figure, we see that V-JEPA achieves this performance with a roughly $2 \times$ speedup compared to the large pixel prediction models.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison with image models", "weight": 1.0} -->

On tasks that require a fine-grained understanding of motion (Something-Something-v2), the V-JEPA models provide a major improvement (over $+ 21$ points) compared to large-scale image baselines, such as DINOv2, OpenCLIP, and I-JEPA. Self-supervised pretraining from videos allows to model dynamic concepts that are not easily learned from static image datasets. Similarly, we observe that the V-JEPA models outperform image-based pretraining on action localization.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison with image models", "weight": 1.0} -->

On Kinetics-400, we find image models to perform well; e.g., while DINOv2 previously reported $78.4\%$ on K400 with a linear probe, we improve the frozen evaluation of the g/14 model to $83.4\%$ by using an attentive probe. In this case, our H/16 model achieves $82.0\%$ top-1 accuracy. It is worth noting that the label for many Kinetics videos can be inferred using appearance-based cues, without requiring an understanding of motion.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparison with image models", "weight": 1.0} -->

The V-JEPA models narrow the gap with image models on image classification tasks. In particular, V-JEPA achieves a score of $77.4\%$ on ImageNet using a one-layer attentive probe, which can be further improved to $77.9\%$ using a two-layer attentive probe. More generally, we hypothesize that the datasets used to train V-JEPA and other video models are too constrained and lack the visual diversity of the internet-scale pretraining data used by the images models; as such, there is value in focusing future work on building diverse publicly available video datasets.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Label-efficiency", "weight": 1.0} -->

We examine the label-efficiency of V-JEPA compared to other self-supervised video models by measuring the ability of the pretrained backbones to adapt to downstream tasks with few labels. Specifically, we investigate the performance of the frozen models on Kinetics-400 and Something-Something-v2 as we vary the percentage of labeled examples from each dataset available for training the attentive probe. We train the probes in several low-shot settings: using either 5% of the train set, 10%, or 50%, and take 3 random splits in each setting to obtain more robust metrics, resulting in 9 different evaluation experiments for each model. Table reports the mean performances and standard deviation using the K400 and SSv2 validation sets.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Label-efficiency", "weight": 1.0} -->

We find V-JEPA to be more label-efficient than other self-supervised video models: decreasing the available number of labeled examples for training the attentive probe results in an increase in the performance gap between V-JEPA and the other models. In particular, the performance of the largest V-JEPA model on K400 drops by 12% to 68.2% top-1 when we reduce the number of labeled examples by a factor of $10 \times$ (from roughly 287 examples per class to 29 examples per class). By contrast, VideoMAEv2 drops by 30% to 37.0% top-1, VideoMAE drops by 15.9% to 62.3% top-1, and MVD drops by 14.6% to 62.6% top-1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Label-efficiency", "weight": 1.0} -->

Similar observations hold on SSv2. The performance of the largest V-JEPA model on SSv2 drops by 13.9% to 54.0% top-1 when we reduce the number of labeled examples by a factor of $10 \times$ (from roughly 440 examples per class to 48 examples per class). By contrast, VideoMAEv2 drops by 26% to 28.0% top-1, VideoMAE drops by 19.1% to 41.4% top-1, and MVD drops by 18.1% to 42.9% top-1.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluating the Predictor", "weight": 1.0} -->

Next, we seek to qualitatively inspect the V-JEPA models. Recall that the predictor network in V-JEPA predicts the representations of a masked spatio-temporal region $y$ from a visible region $x$, given the positional information of the masked regions. To qualitatively investigate the grounding of the feature-space predictions, we freeze the pretrained encoder and predictor networks and train a conditional diffusion decoder to map the V-JEPA predictions to interpretable pixels. Notably, the decoder is only fed the representations predicted for the missing regions of the video, and does not have access to the unmasked regions of the video (see Figure 6(a) ‣ Figure 6 ‣ 6 Evaluating the Predictor ‣ Revisiting Feature Prediction for Learning Visual Representations from Video")).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluating the Predictor", "weight": 1.0} -->

(a) Visualization Methodology. We train a conditional diffusion model to decode the V-JEPA feature-space predictions to interpretable pixels; the pretrained V-JEPA encoder and predictor networks are kept frozen in this process. The decoder is only fed the representations predicted for the missing regions of the video, and does not have access to the unmasked regions of the video.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluating the Predictor", "weight": 1.0} -->

(b) Visualizations. First Row: Masked videos used as input to the V-JEPA models (a pretrained ViT-H/16 encoder and its corresponding predictor network). Other rows: Bounding boxes contain various samples from the decoder overlayed on the original video. V-JEPA is not a generative model and the decoder does not have access to the context (first row), so we do not expect samples to exactly match the input. This experiment qualitatively illustrates what information is encoded and predicted by V-JEPA. In particular, characteristics that are common across samples represent information that is encoded in the V-JEPA predictions. V-JEPA generates predictions that are spatially and temporally coherent with unmask region of the video. The predictions also capture consistent motion through time.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluating the Predictor", "weight": 1.0} -->

Given a masked video, we use the V-JEPA pretrained models to predict the representations of the missing regions, and then use the decoder to project the representations to pixel space. Figure 6(b) ‣ Figure 6 ‣ 6 Evaluating the Predictor ‣ Revisiting Feature Prediction for Learning Visual Representations from Video") shows decoder outputs for various random seeds. Qualities that are common across samples represent information that is contained in the predictor representation.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we explored the effectiveness of feature prediction as a stand-alone objective for unsupervised learning from video and introduced V-JEPA, a collection of vision models trained solely using a self-supervised feature prediction objective. The V-JEPA models demonstrate the ability to solve various downstream image and video tasks without adaption of the model parameters, and outperform previous video representation learning approaches in frozen evaluation on action recognition, spatio-temporal action detection, and image classification tasks. Additionally, we show that pretraining V-JEPA on videos is particularly effective for solving downstream tasks requiring fine-grained motion understanding, while large-scale image models trained on internet scale datasets fall short on such tasks. Finally, we empirically observed that V-JEPA models are label-efficient learners, and exhibit good performance on downstream tasks, even when only few labeled examples are available.
