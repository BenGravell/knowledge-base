## Introduction

Approaches based on deep convolutional neural networks have advanced the state-of-the-art across many standard datasets for vision problems since AlexNet. At the same time, the most prominent architecture of choice in sequence-to-sequence modelling (e.g. in natural language processing) is the transformer, which does not use convolutions, but is based on multi-headed self-attention. This operation is particularly effective at modelling long-range dependencies and allows the model to attend over all elements in the input sequence. This is in stark contrast to convolutions where the corresponding "receptive field" is limited, and grows linearly with the depth of the network.

The success of attention-based models in NLP has recently inspired approaches in computer vision to integrate transformers into CNNs, as well as some attempts to replace convolutions completely. However, it is only very recently with the Vision Transformer (ViT), that a pure-transformer based architecture has outperformed its convolutional counterparts in image classification. Dosovitskiy *et al*. closely followed the original transformer architecture of, and noticed that its main benefits were observed at large scale -- as transformers lack some of the inductive biases of convolutions (such as translational equivariance), they seem to require more data or stronger regularisation.

Inspired by ViT, and the fact that attention-based architectures are an intuitive choice for modelling long-range contextual relationships in video, we develop several transformer-based models for video classification. Currently, the most performant models are based on deep 3D convolutional architectures which were a natural extension of image classification CNNs. Recently, these models were augmented by incorporating self-attention into their later layers to better capture long-range dependencies.

Figure 1: We propose a pure-transformer architecture for video classification, inspired by the recent success of such models for images. To effectively process a large number of spatio-temporal tokens, we develop several model variants which factorise different components of the transformer encoder over the spatial- and temporal-dimensions. As shown on the right, these factorisations correspond to different attention patterns over space and time.

As shown in Fig. 1, we propose pure-transformer models for video classification. The main operation performed in this architecture is self-attention, and it is computed on a sequence of spatio-temporal tokens that we extract from the input video. To effectively process the large number of spatio-temporal tokens that may be encountered in video, we present several methods of factorising our model along spatial and temporal dimensions to increase efficiency and scalability. Furthermore, to train our model effectively on smaller datasets, we show how to reguliarise our model during training and leverage pretrained image models.

We also note that convolutional models have been developed by the community for several years, and there are thus many "best practices" associated with such models. As pure-transformer models present different characteristics, we need to determine the best design choices for such architectures. We conduct a thorough ablation analysis of tokenisation strategies, model architecture and regularisation methods. Informed by this analysis, we achieve state-of-the-art results on multiple standard video classification benchmarks, including Kinetics 400 and 600, Epic Kitchens 100, Something-Something v2 and Moments in Time.

## Related Work

Architectures for video understanding have mirrored advances in image recognition. Early video research used hand-crafted features to encode appearance and motion information. The success of AlexNet on ImageNet initially led to the repurposing of 2D image convolutional networks (CNNs) for video as "two-stream" networks. These models processed RGB frames and optical flow images independently before fusing them at the end. Availability of larger video classification datasets such as Kinetics subsequently facilitated the training of spatio-temporal 3D CNNs which have significantly more parameters and thus require larger training datasets. As 3D convolutional networks require significantly more computation than their image counterparts, many architectures factorise convolutions across spatial and temporal dimensions and/or use grouped convolutions. We also leverage factorisation of the spatial and temporal dimensions of videos to increase efficiency, but in the context of transformer-based models.

Concurrently, in natural language processing (NLP), Vaswani *et al*. achieved state-of-the-art results by replacing convolutions and recurrent networks with the transformer network that consisted only of self-attention, layer normalisation and multilayer perceptron (MLP) operations. Current state-of-the-art architectures in NLP remain transformer-based, and have been scaled to web-scale datasets. Many variants of the transformer have also been proposed to reduce the computational cost of self-attention when processing longer sequences and to improve parameter efficiency. Although self-attention has been employed extensively in computer vision, it has, in contrast, been typically incorporated as a layer at the end or in the later stages of the network or to augment residual blocks within a ResNet architecture.

Although previous works attempted to replace convolutions in vision architectures, it is only very recently that Dosovitisky *et al*. showed with their ViT architecture that pure-transformer networks, similar to those employed in NLP, can achieve state-of-the-art results for image classification too. The authors showed that such models are only effective at large scale, as transformers lack some of inductive biases of convolutional networks (such as translational equivariance), and thus require datasets larger than the common ImageNet ILSRVC dataset to train. ViT has inspired a large amount of follow-up work in the community, and we note that there are a number of concurrent approaches on extending it to other tasks in computer vision and improving its data-efficiency. In particular, have also proposed transformer-based models for video.

In this paper, we develop pure-transformer architectures for video classification. We propose several variants of our model, including those that are more efficient by factorising the spatial and temporal dimensions of the input video. We also show how additional regularisation and pretrained models can be used to combat the fact that video datasets are not as large as their image counterparts that ViT was originally trained . Furthermore, we outperform the state-of-the-art across five popular datasets.

## Video Vision Transformers

We start by summarising the recently proposed Vision Transformer in Sec. 3.1 ‣ 3 Video Vision Transformers ‣ ViViT: A Video Vision Transformer"), and then discuss two approaches for extracting tokens from video in Sec. 3.2. Finally, we develop several transformer-based architectures for video classification in Sec. 3.3 and 3.4.

### Overview of Vision Transformers (ViT)

Vision Transformer (ViT) adapts the transformer architecture of to process 2D images with minimal changes. In particular, ViT extracts $N$ non-overlapping image patches, $x_{i} \in {\mathbb{R}}^{h \times w}$, performs a linear projection and then rasterises them into 1D tokens $z_{i} \in {\mathbb{R}}^{d}$. The sequence of tokens input to the following transformer encoder is where the projection by $\mathbf{E}$ is equivalent to a 2D convolution. As shown in Fig. 1, an optional learned classification token $z_{cls}$ is prepended to this sequence, and its representation at the final layer of the encoder serves as the final representation used by the classification layer. In addition, a learned positional embedding, $\mathbf{p} \in {\mathbb{R}}^{N \times d}$, is added to the tokens to retain positional information, as the subsequent self-attention operations in the transformer are permutation invariant. The tokens are then passed through an encoder consisting of a sequence of $L$ transformer layers. Each layer $\ell$ comprises of Multi-Headed Self-Attention, layer normalisation (LN), and MLP blocks as follows: The MLP consists of two linear projections separated by a GELU non-linearity and the token-dimensionality, $d$, remains fixed throughout all layers. Finally, a linear classifier is used to classify the encoded input based on $z_{cls}^{L} \in {\mathbb{R}}^{d}$, if it was prepended to the input, or a global average pooling of all the tokens, $\mathbf{z}^{L}$, otherwise.

As the transformer, which forms the basis of ViT, is a flexible architecture that can operate on any sequence of input tokens $\mathbf{z} \in {\mathbb{R}}^{N \times d}$, we describe strategies for tokenising videos next.

### Embedding video clips

We consider two simple methods for mapping a video $\mathbf{V} \in {\mathbb{R}}^{T \times H \times W \times C}$ to a sequence of tokens $\overset{\sim}{\mathbf{z}} \in {\mathbb{R}}^{n_{t} \times n_{h} \times n_{w} \times d}$. We then add the positional embedding and reshape into ${\mathbb{R}}^{N \times d}$ to obtain $\mathbf{z}$, the input to the transformer.

### Uniform frame sampling

As illustrated in Fig. 2, a straightforward method of tokenising the input video is to uniformly sample $n_{t}$ frames from the input video clip, embed each 2D frame independently using the same method as ViT, and concatenate all these tokens together. Concretely, if $n_{h} \cdot n_{w}$ non-overlapping image patches are extracted from each frame, as , then a total of $n_{t} \cdot n_{h} \cdot n_{w}$ tokens will be forwarded through the transformer encoder. Intuitively, this process may be seen as simply constructing a large 2D image to be tokenised following ViT. We note that this is the input embedding method employed by the concurrent work of.

### Tubelet embedding

Figure 2: Uniform frame sampling: We simply sample nt frames, and embed each 2D frame independently following ViT.

Figure 3: Tubelet embedding. We extract and linearly embed non-overlapping tubelets that span the spatio-temporal input volume.

An alternate method, as shown in Fig. 3, is to extract non-overlapping, spatio-temporal "tubes" from the input volume, and to linearly project this to ${\mathbb{R}}^{d}$. This method is an extension of ViT's embedding to 3D, and corresponds to a 3D convolution. For a tubelet of dimension $t \times h \times w$, $n_{t} = {\lfloor\frac{T}{t}\rfloor}$, $n_{h} = {\lfloor\frac{H}{h}\rfloor}$ and $n_{w} = {\lfloor\frac{W}{w}\rfloor}$, tokens are extracted from the temporal, height, and width dimensions respectively. Smaller tubelet dimensions thus result in more tokens which increases the computation. Intuitively, this method fuses spatio-temporal information during tokenisation, in contrast to "Uniform frame sampling" where temporal information from different frames is fused by the transformer.

### Transformer Models for Video

As illustrated in Fig. 1, we propose multiple transformer-based architectures. We begin with a straightforward extension of ViT that models pairwise interactions between all spatio-temporal tokens, and then develop more efficient variants which factorise the spatial and temporal dimensions of the input video at various levels of the transformer architecture.

### Model 1: Spatio-temporal attention

This model simply forwards all spatio-temporal tokens extracted from the video, $\mathbf{z}^{0}$, through the transformer encoder. We note that this has also been explored concurrently by in their "Joint Space-Time" model. In contrast to CNN architectures, where the receptive field grows linearly with the number of layers, each transformer layer models all pairwise interactions between all spatio-temporal tokens, and it thus models long-range interactions across the video from the first layer. However, as it models all pairwise interactions, Multi-Headed Self Attention (MSA) has quadratic complexity with respect to the number of tokens. This complexity is pertinent for video, as the number of tokens increases linearly with the number of input frames, and motivates the development of more efficient architectures next.

### Model 2: Factorised encoder

Figure 4: Factorised encoder (Model 2). This model consists of two transformer encoders in series: the first models interactions between tokens extracted from the same temporal index to produce a latent representation per time-index. The second transformer models interactions between time steps. It thus corresponds to a “late fusion” of spatial- and temporal information.

As shown in Fig. 4, this model consists of two separate transformer encoders. The first, spatial encoder, only models interactions between tokens extracted from the same temporal index. A representation for each temporal index, $h_{i} \in {\mathbb{R}}^{d}$, is obtained after $L_{s}$ layers: This is the encoded classification token, $z_{cls}^{L_{s}}$ if it was prepended to the input (Eq. 1 ‣ 3 Video Vision Transformers ‣ ViViT: A Video Vision Transformer")), or a global average pooling from the tokens output by the spatial encoder, $\mathbf{z}^{L_{s}}$, otherwise. The frame-level representations, $h_{i}$, are concatenated into $\mathbf{H} \in {\mathbb{R}}^{n_{t} \times d}$, and then forwarded through a temporal encoder consisting of $L_{t}$ transformer layers to model interactions between tokens from different temporal indices. The output token of this encoder is then finally classified.

This architecture corresponds to a "late fusion" of temporal information, and the initial spatial encoder is identical to the one used for image classification. It is thus analogous to CNN architectures such as which first extract per-frame features, and then aggregate them into a final representation before classifying them. Although this model has more transformer layers than Model 1 (and thus more parameters), it requires fewer floating point operations (FLOPs), as the two separate transformer blocks have a complexity of $\mathcal{O}{({{({n_{h} \cdot n_{w}})}^{2} + n_{t}^{2}})}$ compared to $\mathcal{O}{({({n_{t} \cdot n_{h} \cdot n_{w}})}^{2})}$ of Model 1.

### Model 3: Factorised self-attention

Figure 5: Factorised self-attention (Model 3). Within each transformer block, the multi-headed self-attention operation is factorised into two operations (indicated by striped boxes) that first only compute self-attention spatially, and then temporally.

This model, in contrast, contains the same number of transformer layers as Model 1. However, instead of computing multi-headed self-attention across all pairs of tokens, $\mathbf{z}^{\ell}$, at layer $l$, we factorise the operation to first only compute self-attention spatially (among all tokens extracted from the same temporal index), and then temporally (among all tokens extracted from the same spatial index) as shown in Fig. 5. Each self-attention block in the transformer thus models spatio-temporal interactions, but does so more efficiently than Model 1 by factorising the operation over two smaller sets of elements, thus achieving the same computational complexity as Model 2. We note that factorising attention over input dimensions has also been explored , and concurrently in the context of video by in their "Divided Space-Time" model.

This operation can be performed efficiently by reshaping the tokens $\mathbf{z}$ from ${\mathbb{R}}^{{1 \times n_{t}} \cdot n_{h} \cdot n_{w} \cdot d}$ to ${\mathbb{R}}^{{n_{t} \times n_{h}} \cdot n_{w} \cdot d}$ (denoted by $\mathbf{z}_{s}$) to compute spatial self-attention. Similarly, the input to temporal self-attention, $\mathbf{z}_{t}$ is reshaped to ${\mathbb{R}}^{{{n_{h} \cdot n_{w}} \times n_{t}} \cdot d}$. Here we assume the leading dimension is the "batch dimension". Our factorised self-attention is defined as We observed that the order of spatial-then-temporal self-attention or temporal-then-spatial self-attention does not make a difference, provided that the model parameters are initialised as described in Sec. 3.4. Note that the number of parameters, however, increases compared to Model 1, as there is an additional self-attention layer (cf. Eq. 7). We do not use a classification token in this model, to avoid ambiguities when reshaping the input tokens between spatial and temporal dimensions.

### Model 4: Factorised dot-product attention

Figure 6: Factorised dot-product attention (Model 4). For half of the heads, we compute dot-product attention over only the spatial axes, and for the other half, over only the temporal axis.

Finally, we develop a model which has the same computational complexity as Models 2 and 3, while retaining the same number of parameters as the unfactorised Model 1. The factorisation of spatial- and temporal dimensions is similar in spirit to Model 3, but we factorise the multi-head dot-product attention operation instead (Fig. 6). Concretely, we compute attention weights for each token separately over the spatial- and temporal-dimensions using different heads. First, we note that the attention operation for each head is defined as In self-attention, the queries $\mathbf{Q} = {\mathbf{X}\mathbf{W}}_{q}$, keys $\mathbf{K} = {\mathbf{X}\mathbf{W}}_{k}$, and values $\mathbf{V} = {\mathbf{X}\mathbf{W}}_{v}$ are linear projections of the input $\mathbf{X}$ with ${\mathbf{X},\mathbf{Q},\mathbf{K},\mathbf{V}} \in {\mathbb{R}}^{N \times d}$. Note that in the unfactorised case (Model 1), the spatial and temporal dimensions are merged as $N = {n_{t} \cdot n_{h} \cdot n_{w}}$.

The main idea here is to modify the keys and values for each query to only attend over tokens from the same spatial- and temporal index by constructing ${\mathbf{K}_{s},\mathbf{V}_{s}} \in {\mathbb{R}}^{{n_{h} \cdot n_{w}} \times d}$ and ${\mathbf{K}_{t},\mathbf{V}_{t}} \in {\mathbb{R}}^{n_{t} \times d}$, namely the keys and values corresponding to these dimensions. Then, for half of the attention heads, we attend over tokens from the spatial dimension by computing $\mathbf{Y}_{s} = {{Attention}{(\mathbf{Q},\mathbf{K}_{s},\mathbf{V}_{s})}}$, and for the rest we attend over the temporal dimension by computing $\mathbf{Y}_{t} = {{Attention}{(\mathbf{Q},\mathbf{K}_{t},\mathbf{V}_{t})}}$. Given that we are only changing the attention neighbourhood for each query, the attention operation has the same dimension as in the unfactorised case, namely ${\mathbf{Y}_{s},\mathbf{Y}_{t}} \in {\mathbb{R}}^{N \times d}$. We then combine the outputs of multiple heads by concatenating them and using a linear projection, $\mathbf{Y} = {{{Concat}{(\mathbf{Y}_{s},\mathbf{Y}_{t})}}\mathbf{W}_{O}}$.

### Initialisation by leveraging pretrained models

ViT has been shown to only be effective when trained on large-scale datasets, as transformers lack some of the inductive biases of convolutional networks. However, even the largest video datasets such as Kinetics, have several orders of magnitude less labelled examples when compared to their image counterparts. As a result, training large models from scratch to high accuracy is extremely challenging. To sidestep this issue, and enable more efficient training we initialise our video models from pretrained image models. However, this raises several practical questions, specifically on how to initialise parameters not present or incompatible with image models. We now discuss several effective strategies to initialise these large-scale video classification models.

### Positional embeddings

A positional embedding $\mathbf{p}$ is added to each input token (Eq. 1 ‣ 3 Video Vision Transformers ‣ ViViT: A Video Vision Transformer")). However, our video models have $n_{t}$ times more tokens than the pretrained image model. As a result, we initialise the positional embeddings by "repeating" them temporally from ${\mathbb{R}}^{{n_{w} \cdot n_{h}} \times d}$ to ${\mathbb{R}}^{{n_{t} \cdot n_{h} \cdot n_{w}} \times d}$. Therefore, at initialisation, all tokens with the same spatial index have the same embedding which is then fine-tuned.

### Embedding weights, $\mathbf{E}$

When using the "tubelet embedding" tokenisation method (Sec. 3.2), the embedding filter $\mathbf{E}$ is a 3D tensor, compared to the 2D tensor in the pretrained model, $\mathbf{E}_{\text{image}}$. A common approach for initialising 3D convolutional filters from 2D filters for video classification is to "inflate" them by replicating the filters along the temporal dimension and averaging them as We consider an additional strategy, which we denote as "central frame initialisation", where $\mathbf{E}$ is initialised with zeroes along all temporal positions, except at the centre $\lfloor\frac{t}{2}\rfloor$, Therefore, the 3D convolutional filter effectively behaves like "Uniform frame sampling" (Sec. 3.2) at initialisation, while also enabling the model to learn to aggregate temporal information from multiple frames as training progresses.

### Transformer weights for Model 3

The transformer block in Model 3 (Fig. 5) differs from the pretrained ViT model, in that it contains two multi-headed self attention (MSA) modules. In this case, we initialise the spatial MSA module from the pretrained module, and initialise all weights of the temporal MSA with zeroes, such that Eq. 5 behaves as a residual connection at initialisation.

## Empirical evaluation

We first present our experimental setup and implementation details in Sec. 4.1, before ablating various components of our model in Sec. 4.2. We then present state-of-the-art results on five datasets in Sec. 4.3.

### Experimental Setup

### Network architecture and training

Our backbone architecture follows that of ViT and BERT. We consider ViT-Base (ViT-B, $L$=$12$, $N_{H}$=$12$, $d$=$768$), ViT-Large (ViT-L, $L$=$24$, $N_{H}$=$16$, $d$=$1024$), and ViT-Huge (ViT-H, $L$=$32$, $N_{H}$=$16$, $d$=$1280$), where $L$ is the number of transformer layers, each with a self-attention block of $N_{H}$ heads and hidden dimension $d$. We also apply the same naming scheme to our models (e.g., ViViT-B/16x2 denotes a ViT-Base backbone with a tubelet size of ${h \times w \times t} = {16 \times 16 \times 2}$). In all experiments, the tubelet height and width are equal. Note that smaller tubelet sizes correspond to more tokens at the input, and thus more computation.

We train our models using synchronous SGD and momentum, a cosine learning rate schedule and TPU-v3 accelerators. We initialise our models from a ViT image model trained either on ImageNet-21K (unless otherwise specified) or the larger JFT dataset. We implement our method using the Scenic library and have released our code and models.

### Datasets

We evaluate the performance of our proposed models on a diverse set of video classification datasets: *Kinetics* consists of 10-second videos sampled at 25fps from YouTube. We evaluate on both Kinetics 400 and 600, containing 400 and 600 classes respectively. As these are dynamic datasets (videos may be removed from YouTube), we note our dataset sizes are approximately 267 000 and 446 000 respectively.

*Epic Kitchens-100* consists of egocentric videos capturing daily kitchen activities spanning 100 hours and 90 000 clips. We report results following the standard "action recognition" protocol. Here, each video is labelled with a "verb" and a "noun" and we therefore predict both categories using a single network with two "heads". The top-scoring verb and action pair predicted by the network form an "action", and action accuracy is the primary metric.

*Moments in Time* consists of 800 000, 3-second YouTube clips that capture the gist of a dynamic scene involving animals, objects, people, or natural phenomena.

*Something-Something v2* (SSv2) contains 220 000 videos, with durations ranging from 2 to 6 seconds. In contrast to the other datasets, the objects and backgrounds in the videos are consistent across different action classes, and this dataset thus places more emphasis on a model's ability to recognise fine-grained motion cues.

Uniform frame sampling Table 1: Comparison of input encoding methods using ViViT-B and spatio-temporal attention on Kinetics. Further details in text.

### Inference

The input to our network is a video clip of 32 frames using a stride of 2, unless otherwise mentioned, similar to. Following common practice, at inference time, we process multiple views of a longer video and average per-view logits to obtain the final result. Unless otherwise specified, we use a total of 4 views per video (as this is sufficient to "see" the entire video clip across the various datasets), and ablate these and other design choices next.

### Ablation study

### Input encoding

We first consider the effect of different input encoding methods (Sec. 3.2) using our unfactorised model (Model 1) and ViViT-B on Kinetics 400. As we pass 32-frame inputs to the network, sampling 8 frames and extracting tubelets of length $t = 4$ correspond to the same number of tokens in both cases. Table 1 shows that tubelet embedding initialised using the "central frame" method (Eq. 9) performs well, outperforming the commonly-used "filter inflation" initialisation method by 1.6%, and "uniform frame sampling" by 0.7%. We therefore use this encoding method for all subsequent experiments.

Model 2: Fact. encoder Model 3: Fact. self-attention Model 4: Fact. dot product Model 2: Ave. pool baseline Table 2: Comparison of model architectures using ViViT-B as the backbone, and tubelet size of 16 × 2. We report Top-1 accuracy on Kinetics 400 (K400) and action accuracy on Epic Kitchens (EK). Runtime is during inference on a TPU-v3.

Table 3: The effect of varying the number of temporal transformers, Lt, in the Factorised encoder model (Model 2). We report the Top-1 accuracy on Kinetics 400. Note that Lt = 0 corresponds to the “average pooling baseline”.

### Model variants

We compare our proposed model variants (Sec. 3.3) across the Kinetics 400 and Epic Kitchens datasets, both in terms of accuracy and efficiency, in Tab. 2. In all cases, we use the "Base" backbone and tubelet size of $16 \times 2$. Model 2 ("Factorised Encoder") has an additional hyperparameter, the number of temporal transformers, $L_{t}$. We set $L_{t} = 4$ for all experiments and show in Tab. 3 that the model is not sensitive to this choice.

The unfactorised model (Model 1) performs the best on Kinetics 400. However, it can also overfit on smaller datasets such as Epic Kitchens, where we find our "Factorised Encoder" (Model 2) to perform the best. We also consider an additional baseline (last row), based on Model 2, where we do not use any temporal transformer, and simply average pool the frame-level representations from the spatial encoder before classifying. This average pooling baseline performs the worst, and has a larger accuracy drop on Epic Kitchens, suggesting that this dataset requires more detailed modelling of temporal relations.

As described in Sec. 3.3, all factorised variants of our model use significantly fewer FLOPs than the unfactorised Model 1, as the attention is computed separately over spatial- and temporal-dimensions. Model 4 adds no additional parameters to the unfactorised Model 1, and uses the least compute. The temporal transformer encoder in Model 2 operates on only $n_{t}$ tokens, which is why there is a barely a change in compute and runtime over the average pooling baseline, even though it improves the accuracy substantially (3% on Kinetics and 4.9% on Epic Kitchens). Finally, Model 3 requires more compute and parameters than the other factorised models, as its additional self-attention block means that it performs another query-, key-, value- and output-projection in each transformer layer.

Random crop, flip, colour jitter Table 4: The effect of progressively adding regularisation (each row includes all methods above it) on Top-1 action accuracy on Epic Kitchens. We use a Factorised encoder model with tubelet size 16 × 2.

Figure 7: The effect of the backbone architecture on (a) accuracy and (b) computation on Kinetics 400, for the spatio-temporal attention model (Model 1).

Figure 8: The effect of varying the number of temporal tokens on (a) accuracy and (b) computation on Kinetics 400, for different variants of our model with a ViViT-B backbone.

### Model regularisation

Pure-transformer architectures such as ViT are known to require large training datasets, and we observed overfitting on smaller datasets like Epic Kitchens and SSv2, even when using an ImageNet pretrained model. In order to effectively train our models on such datasets, we employed several regularisation strategies that we ablate using our "Factorised encoder" model in Tab. 4. We note that these regularisers were originally proposed for training CNNs, and that have recently explored them for training ViT for image classification.

Each row of Tab. 4 includes all the methods from the rows above it, and we observe progressive improvements from adding each regulariser. Overall, we obtain a substantial overall improvement of 5.3% on Epic Kitchens. We also achieve a similar improvement of 5% on SSv2 by using all the regularisation in Tab. 4. Note that the Kinetics-pretrained models that we initialise from are from Tab. 2, and that all Epic Kitchens models in Tab. 2 were trained with all the regularisers in Tab. 4. For larger datasets like Kinetics and Moments in Time, we do not use these additional regularisers (we use only the first row of Tab. 4), as we obtain state-of-the-art results without them. The appendix contains hyperparameter values and additional details for all regularisers.

### Varying the backbone

Figure 7 compares the ViViT-B and ViViT-L backbones for the unfactorised spatio-temporal model. We observe consistent improvements in accuracy as the backbone capacity increases. As expected, the compute also grows as a function of the backbone size.

Table 5: The effect of spatial resolution on the performance of ViViT-L/16x2 and spatio-temporal attention on Kinetics 400.

### Varying the number of tokens

We first analyse the performance as a function of the number of tokens along the temporal dimension in Fig. 8. We observe that using smaller input tubelet sizes (and therefore more tokens) leads to consistent accuracy improvements across all of our model architectures. At the same time, computation in terms of FLOPs increases accordingly, and the unfactorised model (Model 1) is impacted the most.

We then vary the number of tokens fed into the model by increasing the spatial crop-size from the default of 224 to 320 in Tab. 5. As expected, there is a consistent increase in both accuracy and computation. We note that when comparing to prior work we consistently obtain state-of-the-art results (Sec. 4.3) using a spatial resolution of 224, but we also highlight that further improvements can be obtained at higher spatial resolutions.

Methods with large-scale pretraining (d) Epic Kitchens 100 Top 1 accuracy Table 6: Comparisons to state-of-the-art across multiple datasets. For “views”, x × y denotes x temporal crops and y spatial crops. We report the TFLOPs to process all spatio-temporal views. “FE” denotes our Factorised Encoder model.

Figure 9: The effect of varying the number of frames input to the network and increasing the number of tokens proportionally. We use ViViT-L/16x2 Factorised Encoder on Kinetics 400. A Kinetics video contains 250 frames (10 seconds sampled at 25 fps) and the accuracy for each model saturates once the number of equidistant temporal views is sufficient to “see” the whole video clip. Observe how models processing more frames (and thus more tokens) achieve higher single- and multi-view accuracy.

### Varying the number of input frames

In our experiments so far, we have kept the number of input frames fixed at 32. We now increase the number of frames input to the model, thereby increasing the number of tokens proportionally.

Figure 9 shows that as we increase the number of frames input to the network, the accuracy from processing a single view increases, since the network incorporates longer temporal context. However, common practice on datasets such as Kinetics is to average results over multiple, shorter "views" of the same video clip. Figure 9 also shows that the accuracy saturates once the number of views is sufficient to cover the whole video. As a Kinetics video consists of 250 frames, and we sample frames with a stride of 2, our model which processes 128 frames requires just a single view to "see" the whole video and achieve its maximum accuarcy.

Note that we used ViViT-L/16x2 Factorised Encoder (Model 2) here. As this model is more efficient it can process more tokens, compared to the unfactorised Model 1 which runs out of memory after 48 frames using tubelet length $t = 2$ and a "Large" backbone. Models processing more frames (and thus more tokens) consistently achieve higher single- and multi-view accuracy, in line with our observations in previous experiments (Tab. 5, Fig. 8). Moroever, observe that by processing more frames (and thus more tokens) with Model 2, we are able to achieve higher accuracy than Model 1 (with fewer total FLOPs as well).

Finally, we observed that for Model 2, the number of FLOPs effectively increases linearly with the number of input frames as the overall computation is dominated by the initial Spatial Transformer. As a result, the total number of FLOPs for the number of temporal views required to achieve maximum accuracy is constant across the models. In other words, ViViT-L/16x2 FE with 32 frames requires 995.3 GFLOPs per view, and 4 views to saturate multi-view accuracy. The 128-frame model requires 3980.4 GFLOPs but only a single view. As shown by Fig. 9, the latter model achieves the highest accuracy.

### Comparison to state-of-the-art

Based on our ablation studies in the previous section, we compare to the current state-of-the-art using two of our model variants. We primarily use our Factorised Encoder model (Model 2), as it can process more tokens than Model 1 to achieve higher accuracy.

### Kinetics

Tables 6(a) and 6(c) show that our spatio-temporal attention models outperform the state-of-the-art on Kinetics 400 and 600 respectively. Following standard practice, we take 3 spatial crops (left, centre and right) for each temporal view, and notably, we require significantly fewer views than previous CNN-based methods.

We surpass the previous CNN-based state-of-the-art using ViViT-L/16x2 Factorised Encoder (FE) pretrained on ImageNet, and also outperform who concurrently proposed a pure-transformer architecture. Moreover, by initialising our backbones from models pretrained on the larger JFT dataset, we obtain further improvements. Although these models are not directly comparable to previous work, we do also outperform who pretrained on the large-scale, Instagram dataset. Our best model uses a ViViT-H backbone pretrained on JFT and significantly advances the best reported results on Kinetics 400 and 600 to 84.9% and 85.8%, respectively.

### Moments in Time

We surpass the state-of-the-art by a significant margin as shown in Tab. 6(c). We note that the videos in this dataset are diverse and contain significant label noise, making this task challenging and leading to lower accuracies than on other datasets.

### Epic Kitchens 100

Table 6(e) shows that our Factorised Encoder model outperforms previous methods by a significant margin. In addition, our model obtains substantial improvements for Top-1 accuracy of "noun" classes, and the only method which achieves higher "verb" accuracy used optical flow as an additional input modality. Furthermore, all variants of our model presented in Tab. 2 outperformed the existing state-of-the-art on action accuracy. We note that we use the same model to predict verbs and nouns using two separate "heads", and for simplicity, we do not use separate loss weights for each head.

### Something-Something v2 (SSv2)

Finally, Tab. 6(e) shows that we achieve state-of-the-art Top-1 accuracy with our Factorised encoder model (Model 2), albeit with a smaller margin compared to previous methods. Notably, our Factorised encoder model significantly outperforms the concurrent TimeSformer method by 2.9%, which also proposes a pure-transformer model, but does not consider our Factorised encoder variant or our additional regularisation.

SSv2 differs from other datasets in that the backgrounds and objects are quite similar across different classes, meaning that recognising fine-grained motion patterns is necessary to distinguish classes from each other. Our results suggest that capturing these fine-grained motions is an area of improvement and future work for our model. We also note an inverse correlation between the relative performance of previous methods on SSv2 (Tab. 6(e)) and Kinetics (Tab. 6(a)) suggesting that these two datasets evaluate complementary characteristics of a model.

## Conclusion and Future Work

We have presented four pure-transformer models for video classification, with different accuracy and efficiency profiles, achieving state-of-the-art results across five popular datasets. Furthermore, we have shown how to effectively regularise such high-capacity models for training on smaller datasets and thoroughly ablated our main design choices. Future work is to remove our dependence on image-pretrained models. Finally, going beyond video classification towards more complex tasks is a clear next step.
