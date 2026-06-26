<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Transformers in Time Series: A Survey

Topics include Robustness, Transformers, Computer vision, Classification, Time series, Series.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Transformers have achieved superior performances in many tasks in natural language processing and computer vision, which also triggered great interest in the time series community. Among multiple advantages of Transformers, the ability to capture long-range dependencies and interactions is especially attractive for time series modeling, leading to exciting progress in various time series applications. In this paper, we systematically review Transformer schemes for time series modeling by highlighting their strengths as well as limitations. In particular, we examine the development of time series Transformers in two perspectives. From the perspective of network structure, we summarize the adaptations and modifications that have been made to Transformers in order to accommodate the challenges in time series analysis. From the perspective of applications, we categorize time series Transformers based on common tasks including forecasting, anomaly detection, and classification. Empirically, we perform robust analysis, model size analysis, and seasonal-trend decomposition analysis to study how Transformers perform in time series. Finally, we discuss and suggest future directions to provide useful research guidance. To the best of our knowledge, this paper is the first work to comprehensively and systematically summarize the recent advances of Transformers for modeling time series data. We hope this survey will ignite further research interests in time series Transformers.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The innovation of Transformer in deep learning Vaswani et al. has brought great interests recently due to its excellent performances in natural language processing (NLP) Kenton and others, computer vision (CV) Dosovitskiy et al., and speech processing Dong et al.. Over the past few years, numerous Transformers have been proposed to advance the state-of-the-art performances of various tasks significantly. There are quite a few literature reviews from different aspects, such as in NLP applications Han et al., CV applications Han et al., and efficient Transformers Tay et al..

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Transformers have shown great modeling ability for long-range dependencies and interactions in sequential data and thus are appealing to time series modeling. Many variants of Transformer have been proposed to address special challenges in time series modeling and have been successfully applied to various time series tasks, such as forecasting Li et al.; Zhou et al., anomaly detection Xu et al.; Tuli et al., and classification Zerveas et al.; Yang et al.. Specifically, seasonality or periodicity is an important feature of time series Wen et al.. How to effectively model long-range and short-range temporal dependency and capture seasonality simultaneously remains a challenge Wu et al.; Wen et al.. We note that there exist several surveys related to deep learning for time series, including forecasting Lim and Zohren; Benidis et al.; Torres et al., classification Ismail Fawaz et al., anomaly detection Choi et al.; Blázquez-García et al., and data augmentation Wen et al., but there is no comprehensive survey for Transformers in time series.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As Transformer for time series is an emerging subject in deep learning, a systematic and comprehensive survey on time series Transformers would greatly benefit the time series community.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we aim to fill the gap by summarizing the main developments of time series Transformers. We first give a brief introduction about vanilla Transformer, and then propose a new taxonomy from perspectives of both network modifications and application domains for time series Transformers. For network modifications, we discuss the improvements made on both low-level (i.e. module) and high-level (i.e. architecture) of Transformers, with the aim to optimize the performance of time series modeling. For applications, we analyze and summarize Transformers for popular time series tasks including forecasting, anomaly detection, and classification. For each time series Transformer, we analyze its insights, strengths, and limitations. To provide practical guidelines on how to effectively use Transformers for time series modeling, we conduct extensive empirical studies that examine multiple aspects of time series modeling, including robustness analysis, model size analysis, and seasonal-trend decomposition analysis. We conclude this work by discussing possible future directions for time series Transformers, including inductive biases for time series Transformers, Transformers and GNN for time series, pre-trained Transformers for time series, Transformers with architecture level variants, and Transformers with NAS for time series.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, this is the first work to comprehensively and systematically review the key developments of Transformers for modeling time series data. We hope this survey will ignite further research interests in time series Transformers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Vanilla Transformer", "weight": 1.0} -->

The vanilla Transformer Vaswani et al. follows most competitive neural sequence models with an encoder-decoder structure. Both encoder and decoder are composed of multiple identical blocks. Each encoder block consists of a multi-head self-attention module and a position-wise feed-forward network while each decoder block inserts cross-attention models between the multi-head self-attention module and the position-wise feed-forward network.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Input Encoding and Positional Encoding", "weight": 1.0} -->

Unlike LSTM or RNN, the vanilla Transformer has no recurrence. Instead, it utilizes the positional encoding added in the input embeddings, to model the sequence information. We summarize some positional encodings below.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Absolute Positional Encoding", "weight": 1.0} -->

In vanilla Transformer, for each position index $t$, encoding vector is given by where $\omega_{i}$ is the hand-crafted frequency for each dimension. Another way is to learn a set of positional embeddings for each position which is more flexible Kenton and others; Gehring et al..

<!-- chunk {"id": "body-0011", "role": "body", "section": "Relative Positional Encoding", "weight": 1.0} -->

Following the intuition that pairwise positional relationships between input elements is more beneficial than positions of elements, relative positional encoding methods have been proposed. For example, one of such methods is to add a learnable relative positional embedding to keys of attention mechanism Shaw et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Relative Positional Encoding", "weight": 1.0} -->

Besides the absolute and relative positional encodings, there are methods using hybrid positional encodings that combine them together Ke et al.. Generally, the positional encoding is added to the token embedding and fed to Transformer.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Multi-head Attention", "weight": 1.0} -->

With Query-Key-Value (QKV) model, the scaled dot-product attention used by Transformer is given by where queries $\mathbf{Q} \in \mathcal{R}^{N \times D_{k}}$, keys $\mathbf{K} \in \mathcal{R}^{M \times D_{k}}$, values $\mathbf{V} \in \mathcal{R}^{M \times D_{v}}$, $N,M$ denote the lengths of queries and keys (or values), and $D_{k},D_{v}$ denote the dimensions of keys (or queries) and values.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Feed-forward and Residual Network", "weight": 1.0} -->

The feed-forward network is a fully connected module as where $\mathbf{H}'$ is outputs of previous layer, $\mathbf{W}^{1} \in \mathcal{R}^{D_{m} \times D_{f}}$, $\mathbf{W}^{2} \in \mathcal{R}^{D_{f} \times D_{m}}$, $\mathbf{b}^{1} \in \mathcal{R}^{D_{f}}$, $\mathbf{b}^{2} \in \mathcal{R}^{D_{m}}$ are trainable parameters. In a deeper module, a residual connection module followed by a layer normalization module is inserted around each module. That is, where $SelfAttn{(.)}$ denotes self-attention module and $LayerNorm{(.)}$ denotes the layer normalization operation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Taxonomy of Transformers in Time Series", "weight": 1.0} -->

To summarize the existing time series Transformers, we propose a taxonomy from perspectives of network modifications and application domains as illustrated in Fig. 1. Based on the taxonomy, we review the existing time series Transformers systematically. From the perspective of network modifications, we summarize the changes made on both module level and architecture level of Transformer in order to accommodate special challenges in time series modeling. From the perspective of applications, we classify time series Transformers based on their application tasks, including forecasting, anomaly detection, and classification. In the following two sections, we would delve into the existing time series Transformers from these two perspectives.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Positional Encoding", "weight": 1.0} -->

As the ordering of time series matters, it is of great importance to encode the positions of input time series into Transformers. A common design is to first encode positional information as vectors and then inject them into the model as an additional input together with the input time series. How to obtain these vectors when modeling time series with Transformers can be divided into three main categories.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Positional Encoding", "weight": 1.0} -->

Vanilla Positional Encoding. A few works Li et al. simply introduce vanilla positional encoding (Section 2.2.1) used in Vaswani et al., which is then added to the input time series embeddings and fed to Transformer. Although this approach can extract some positional information from time series, they were unable to fully exploit the important features of time series data.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Positional Encoding", "weight": 1.0} -->

Learnable Positional Encoding. As the vanilla positional encoding is hand-crafted and less expressive and adaptive, several studies found that learning appropriate positional embeddings from time series data can be much more effective. Compared to fixed vanilla positional encoding, learned embeddings are more flexible and can adapt to specific tasks. Zerveas et al. introduces an embedding layer in Transformer that learns embedding vectors for each position index jointly with other model parameters. Lim et al. uses an LSTM network to encode positional embeddings, which can better exploit sequential ordering information in time series.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Positional Encoding", "weight": 1.0} -->

Timestamp Encoding. When modeling time series in real-world scenarios, the timestamp information is commonly accessible, including calendar timestamps (e.g., second, minute, hour, week, month, and year) and special timestamps (e.g., holidays and events). These timestamps are quite informative in real applications but hardly leveraged in vanilla Transformers. To mitigate the issue, Informer Zhou et al. proposed to encode timestamps as additional positional encoding by using learnable embedding layers. A similar timestamp encoding scheme was used in Autoformer Wu et al. and FEDformer Zhou et al..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Attention Module", "weight": 1.0} -->

Central to Transformer is the self-attention module. It can be viewed as a fully connected layer with weights that are dynamically generated based on the pairwise similarity of input patterns. As a result, it shares the same maximum path length as fully connected layers, but with a much less number of parameters, making it suitable for modeling long-term dependencies.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Attention Module", "weight": 1.0} -->

As we show in the previous section the self-attention module in the vanilla Transformer has a time and memory complexity of $\mathcal{O}{(N^{2})}$ ($N$ is the input time series length), which becomes the computational bottleneck when dealing with long sequences. Many efficient Transformers were proposed to reduce the quadratic complexity that can be classified into two main categories: explicitly introducing a sparsity bias into the attention mechanism like LogTrans Li et al. and Pyraformer Liu et al.; exploring the low-rank property of the self-attention matrix to speed up the computation, e.g. Informer Zhou et al. and FEDformer Zhou et al.. Table 1 shows both the time and memory complexity of popular Transformers applied to time series modeling, and more details about these models will be discussed in Section 5.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Attention Module", "weight": 1.0} -->

Crossformer Zhang and Yan $\mathcal{O}{({\frac{D}{L_{seg}^{2}}N^{2}})}$ Table 1: Complexity comparisons of popular time series Transformers with different attention modules.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Architecture-based Attention Innovation", "weight": 1.0} -->

To accommodate individual modules in Transformers for modeling time series, a number of works Zhou et al.; Liu et al. seek to renovate Transformers on the architecture level. Recent works introduce hierarchical architecture into Transformer to take into account the multi-resolution aspect of time series. Informer Zhou et al. inserts max-pooling layers with stride 2 between attention blocks, which down-sample series into its half slice. Pyraformer Liu et al. designs a $C$-ary tree-based attention mechanism, in which nodes at the finest scale correspond to the original time series, while nodes in the coarser scales represent series at lower resolutions. Pyraformer developed both intra-scale and inter-scale attentions in order to better capture temporal dependencies across different resolutions. Besides the ability to integrate information at different multi-resolutions, a hierarchical architecture also enjoys the benefits of efficient computation, particularly for long-time series.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Applications of Time Series Transformers", "weight": 1.0} -->

In this section, we review the applications of Transformer to important time series tasks, including forecasting, anomaly detection, and classification.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Transformers in Forecasting", "weight": 1.0} -->

Here we examine three common types of forecasting tasks here, i.e. time series forecasting, spatial-temporal forecasting, and event forecasting.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Time Series Forecasting", "weight": 1.0} -->

A lot of work has been done to design new Transformer variants for time series forecasting tasks in the latest years. Module-level and architecture-level variants are two large categories and the former consists of the majority of the up-to-date works.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

In the module-level variants for time series forecasting, their main architectures are similar to the vanilla Transformer with minor changes. Researchers introduce various time series inductive biases to design new modules. The following summarized work consists of three different types: designing new attention modules, exploring the innovative way to normalize time series data, and utilizing the bias for token inputs, as shown in Figure 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

The first type of variant for module-level Transformers is to design new attention modules, which is the category with the largest proportion. Here we first describe six typical works: LogTrans Li et al., Informer Zhou et al., AST Wu et al., Pyraformer Liu et al., Quatformer Chen et al., and FEDformer Zhou et al., all of which exploit sparsity inductive bias or low-rank approximation to remove noise and achieve a low-order calculation complexity. LogTrans Li et al. proposes convolutional self-attention by employing causal convolutions to generate queries and keys in the self-attention layer. It introduces sparse bias, a Logsparse mask, in self-attention model that reduces computational complexity from $\mathcal{O}{(N^{2})}$ to $\mathcal{O}{({N{\log N}})}$. Instead of using explicit sparse bias, Informer Zhou et al. selects dominant queries based on queries and key similarities, thus achieving similar improvements as LogTrans in computational complexity.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

It also designs a generative style decoder to produce long-term forecasting directly and thus avoids accumulative error in using one forward-step prediction for long-term forecasting. AST Wu et al. uses a generative adversarial encoder-decoder framework to train a sparse Transformer model for time series forecasting. It shows that adversarial training can improve time series forecasting by directly shaping the output distribution of the network to avoid error accumulation through one-step ahead inference. Pyraformer Liu et al. designs a hierarchical pyramidal attention module with a binary tree following the path, to capture temporal dependencies of different ranges with linear time and memory complexity. FEDformer Zhou et al. applies attention operation in the frequency domain with Fourier transform and wavelet transform. It achieves a linear complexity by randomly selecting a fixed-size subset of frequency. Note that due to the success of Autoformer and FEDformer, it has attracted more attention in the community to explore self-attention mechanisms in the frequency domain for time series modeling.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

Quatformer Chen et al. proposes learning-to-rotate attention (LRA) based on quaternions that introduce learnable period and phase information to depict intricate periodical patterns. Moreover, it decouples LRA using a global memory to achieve linear complexity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

The following three works focus on building an explicit interpretation ability of models, which follows the trend of Explainable Artificial Intelligence (XAI). TFT Lim et al. designs a multi-horizon forecasting model with static covariate encoders, gating feature selection, and temporal self-attention decoder. It encodes and selects useful information from various covariates to perform forecasting. It also preserves interpretability by incorporating global, temporal dependency, and events. ProTran Tang and Matteson and SSDNet Lin et al. combine Transformer with state space models to provide probabilistic forecasts. ProTran designs a generative modeling and inference procedure based on variational inference. SSDNet first uses Transformer to learn the temporal pattern and estimate the parameters of SSM, and then applies SSM to perform the seasonal-trend decomposition and maintain the interpretable ability.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

The second type of variant for module-level Transformers is the way to normalize time series data. To the best of our knowledge, Non-stationary Transformer Liu et al. is the only work that mainly focuses on modifying the normalization mechanism as shown in Figure 2. It explores the over-stationarization problem in time series forecasting tasks with a relatively simple plugin series stationary and De-stationary module to modify and boost the performance of various attention blocks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

The third type of variant for module-level Transformer is utilizing the bias for token input. Autoformer Wu et al. adopts a segmentation-based representation mechanism. It devises a simple seasonal-trend decomposition architecture with an auto-correlation mechanism working as an attention module. The auto-correlation block measures the time-delay similarity between inputs signal and aggregates the top-k similar sub-series to produce the output with reduced complexity. PatchTST Nie et al. utilizes channel-independent where each channel contains a single univariate time series that shares the same embedding within all the series, and subseries-level patch design which segmentation of time series into subseries-level patches that are served as input tokens to Transformer. Such ViT Dosovitskiy et al. alike design improves its numerical performance in long-time time-series forecasting tasks a lot. Crossformer Zhang and Yan proposes a Transformer-based model utilizing cross-dimension dependency for multivariate time series forecasting. The input is embedded into a 2D vector array through the novel dimension-segment-wise embedding to preserve time and dimension information.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Module-level variants", "weight": 1.0} -->

Then, a two-stage attention layer is used to efficiently capture the cross-time and cross-dimension dependency.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Architecture-level variants", "weight": 1.0} -->

Some works start to design a new transformer architecture beyond the scope of the vanilla transformer. Triformer Cirstea et al. design a triangular,variable-specific patch attention. It has a triangular tree-type structure as the later input size shrinks exponentially and a set of variable-specific parameters making a multi-layer Triformer maintain a lightweight and linear complexity. Scaleformer Shabani et al. proposes a multi-scale framework that can be applied to the baseline transformer-based time series forecasting models (FEDformerZhou et al., AutoformerWu et al., etc.). It can improve the baseline model's performance by iteratively refining the forecasted time series at multiple scales with shared weights.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remarks", "weight": 1.0} -->

Note that DLinear Zeng et al. questions the necessity of using Transformers for long-term time series forecasting, and shows that a simpler MLP-based model can achieve better results compared to some Transformer baselines through empirical studies. However, we notice that a recent Transformer model PatchTST Nie et al. achieves a better numerical result compared to DLinear for long-term time series forecasting. Moreover, there is a thorough theoretical study Yun et al. showing that the Transformer models are universal approximators of sequence-to-sequence functions. It is a overclaim to question the potential of any type of method for time series forecasting based solely on experimental results from some variant instantiations of such method, especially for Transformer models which already demonstrate the performances in most machine learning-based tasks. Therefore, we conclude that summarizing the recent Transformer-based models for time series forecasting is necessary and would benefit the whole community.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Spatio-Temporal Forecasting", "weight": 1.0} -->

In spatio-temporal forecasting, both temporal and spatio-temporal dependencies are taken into account in time series Transformers for accurate forecasting.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Spatio-Temporal Forecasting", "weight": 1.0} -->

Traffic Transformer Cai et al. designs an encoder-decoder structure using a self-attention module to capture temporal-temporal dependencies and a graph neural network module to capture spatial dependencies. Spatial-temporal Transformer Xu et al. for traffic flow forecasting takes a step further. Besides introducing a temporal Transformer block to capture temporal dependencies, it also designs a spatial Transformer block, together with a graph convolution network, to better capture spatial-spatial dependencies. Spatio-temporal graph Transformer Yu et al. designs an attention-based graph convolution mechanism that is able to learn a complicated temporal-spatial attention pattern to improve pedestrian trajectory prediction. Earthformer Gao et al. proposes a cuboid attention for efficient space-time modeling, which decomposes the data into cuboids and applies cuboid-level self-attention in parallel. It shows that Earthformer achieves superior performance in weather and climate forecasting. Recently, AirFormer Liang et al. devises a dartboard spatial self-attention module and a causal temporal self-attention module to efficiently capture spatial correlations and temporal dependencies, respectively.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Spatio-Temporal Forecasting", "weight": 1.0} -->

Furthermore, it enhances Transformers with latent variables to capture data uncertainty and improve air quality forecasting.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Event Forecasting", "weight": 1.0} -->

Event sequence data with irregular and asynchronous timestamps are naturally observed in many real-life applications, which is in contrast to regular time series data with equal sampling intervals. Event forecasting or prediction aims to predict the times and marks of future events given the history of past events, and it is often modeled by temporal point processes (TPP) Yan et al.; Shchur et al..

<!-- chunk {"id": "body-0041", "role": "body", "section": "Event Forecasting", "weight": 1.0} -->

Recently, several neural TPP models incorporate Transformers in order to improve the performance of event prediction. Self-attentive Hawkes process (SAHP) Zhang et al. and Transformer Hawkes process (THP) Zuo et al. adopt Transformer encoder architecture to summarize the influence of historical events and compute the intensity function for event prediction. They modify the positional encoding by translating time intervals into sinusoidal functions such that the intervals between events can be utilized. Later, a more flexible named attentive neural datalog through time (A-NDTT) Mei et al. is proposed to extend SAHP/THP schemes by embedding all possible events and times with attention as well. Experiments show that it can better capture sophisticated event dependencies than existing methods.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Transformers in Anomaly Detection", "weight": 1.0} -->

Transformer based architecture also benefits the time series anomaly detection task with the ability to model temporal dependency, which brings high detection quality Xu et al.. Besides, in multiple studies, including TranAD Tuli et al., MT-RVAE Wang et al., and TransAnomaly Zhang et al., researchers proposed to combine Transformer with neural generative models, such as VAEs Kingma and Welling and GANs Goodfellow et al., for better performance in anomaly detection. We will elaborate on these models in the following part.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Transformers in Anomaly Detection", "weight": 1.0} -->

TranAD Tuli et al. proposes an adversarial training procedure to amplify reconstruction errors as a simple Transformer-based network tends to miss small deviation of anomaly. GAN style adversarial training procedure is designed by two Transformer encoders and two Transformer decoders to gain stability. Ablation study shows that, if Transformer-based encoder-decoder is replaced, F1 score drops nearly 11%, indicating the effect of Transformer architecture on time series anomaly detection.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Transformers in Anomaly Detection", "weight": 1.0} -->

MT-RVAE Wang et al. and TransAnomaly Zhang et al. combine VAE with Transformer, but they share different purposes. TransAnomaly combines VAE with Transformer to allow more parallelization and reduce training costs by nearly 80%. In MT-RVAE, a multiscale Transformer is designed to extract and integrate time-series information at different scales. It overcomes the shortcomings of traditional Transformers where only local information is extracted for sequential analysis.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Transformers in Anomaly Detection", "weight": 1.0} -->

GTA Chen et al. combines Transformer with graph-based learning architecture for multivariate time series anomaly detection. Note that, MT-RVAE is also for multivariate time series but with few dimensions or insufficient close relationships among sequences where the graph neural network model does not work well. To deal with such challenge, MT-RVAE modifies the positional encoding module and introduces feature-learning module. Instead, GTA contains a graph convolution structure to model the influence propagation process. Similar to MT-RVAE, GTA also considers "global" information, yet by replacing vanilla multi-head attention with a multi-branch attention mechanism, that is, a combination of global-learned attention, vanilla multi-head attention, and neighborhood convolution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Transformers in Anomaly Detection", "weight": 1.0} -->

AnomalyTrans Xu et al. combines Transformer and Gaussian prior-Association to make anomalies more distinguishable. Sharing similar motivation as TranAD, AnomalyTrans achieves the goal in a different way. The insight is that it is harder for anomalies to build strong associations with the whole series while easier with adjacent time points compared with normality. In AnomalyTrans, prior-association and series-association are modeled simultaneously. Besides reconstruction loss, the anomaly model is optimized by the minimax strategy to constrain the prior- and series- associations for more distinguishable association discrepancy.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Transformers in Classification", "weight": 1.0} -->

Transformer is proved to be effective in various time series classification tasks due to its prominent capability in capturing long-term dependency. GTN Liu et al. uses a two-tower Transformer with each tower respectively working on time-step-wise attention and channel-wise attention. To merge the feature of the two towers, a learnable weighted concatenation (also known as 'gating') is used. The proposed extension of Transformer achieves state-of-the-art results on 13 multivariate time series classifications. Rußwurm and Körner studied the self-attention based Transformer for raw optical satellite time series classification and obtained the best results compared with recurrent and convolutional neural networks. Recently, TARNet Chowdhury et al. designs Transformers to learn task-aware data reconstruction that augments classification performance, which utilizes attention score for important timestamps masking and reconstruction and brings superior performance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Transformers in Classification", "weight": 1.0} -->

Pre-trained Transformers are also investigated in classification tasks. Yuan and Lin studies the Transformer for raw optical satellite image time series classification. The authors use self-supervised pre-trained schema because of limited labeled data. Zerveas et al. introduced an unsupervised pre-trained framework and the model is pre-trained with proportionally masked data. The pre-trained models are then fine-tuned in downstream tasks such as classification. Yang et al. proposes to use large-scale pre-trained speech processing model for downstream time series classification problems and generates 19 competitive results on 30 popular time series classification datasets.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experimental Evaluation and Discussion", "weight": 1.0} -->

We conduct preliminary empirical studies on a typical challenging benchmark dataset ETTm2 Zhou et al. to analyze how Transformers work on time series data. Since classic statistical ARIMA/ETS Hyndman and Khandakar models and basic RNN/CNN models perform inferior to Transformers in this dataset as shown in Zhou et al.; Wu et al., we focus on popular time series Transformers with different configurations in the experiments.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Robustness Analysis", "weight": 1.0} -->

A lot of works we describe above carefully design attention modules to lower the quadratic calculation and memory complexity, though they practically use a short fixed-size input to achieve the best result in their reported experiments. It makes us question the actual usage of such an efficient design. We perform a robust experiment with prolonging input sequence length to verify their prediction power and robustness when dealing with long-term input sequences in Table 2.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Robustness Analysis", "weight": 1.0} -->

As in Table 2, when we compare the prediction results with prolonging input length, various Transformer-based model deteriorates quickly. This phenomenon makes a lot of carefully designed Transformers impractical in long-term forecasting tasks since they cannot effectively utilize long input information. More works and designs need to be investigated to fully utilize long sequence input for better performance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Model Size Analysis", "weight": 1.0} -->

Before being introduced into the field of time series prediction, Transformer has shown dominant performance in NLP and CV communities Vaswani et al.; Kenton and others; Han et al.. One of the key advantages Transformer holds in these fields is being able to increase prediction power through increasing model size. Usually, the model capacity is controlled by Transformer's layer number, which is commonly set between 12 to 128. Yet as shown in the experiments of Table 3, when we compare the prediction result with different Transformer models with various numbers of layers, the Transformer with 3 to 6 layers often achieves better results. It raises a question about how to design a proper Transformer architecture with deeper layers to increase the model's capacity and achieve better forecasting performance.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Seasonal-Trend Decomposition Analysis", "weight": 1.0} -->

In recent studies, researchers Wu et al.; Zhou et al.; Lin et al.; Liu et al. begin to realize that the seasonal-trend decomposition Cleveland et al.; Wen et al. is a crucial part of Transformer's performance in time series forecasting. As an experiment shown in Table 4, we adopt a simple moving average seasonal-trend decomposition architecture proposed in Wu et al. to test various attention modules. It can be seen that the simple seasonal-trend decomposition model can significantly boost model's performance by 50 % to 80%. It is a unique block and such performance boosting through decomposition seems a consistent phenomenon in time series forecasting for Transformer's application, which is worth further investigating for more advanced and carefully designed time series decomposition schemes.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Future Research Opportunities", "weight": 1.0} -->

Here we highlight a few directions that are potentially promising for future research of Transformers in time series.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Inductive Biases for Time Series Transformers", "weight": 1.0} -->

Vanilla Transformer does not make any assumptions about data patterns and characteristics. Although it is a general and universal network for modeling long-range dependencies, it also comes with a price, i.e., lots of data are needed to train Transformer to improve the generalization and avoid data overfitting. One of the key features of time series data is its seasonal/periodic and trend patterns Wen et al.; Cleveland et al.. Some recent studies have shown that incorporating series periodicity Wu et al. or frequency processing Zhou et al. into time series Transformer can enhance performance significantly. Moreover, it is interesting that some studies adopt a seemly opposite inductive bias, but both achieve good numerical improvement: Nie et al. removes the cross-channel dependency by utilizing a channel-independent attention module, while an interesting work Zhang and Yan improves its experimental performance by utilizing cross-dimension dependency with a two-stage attention mechanism. Clearly, we have noise and signals in such a cross-channel learning paradigm, but a clever way to utilize such inductive bias to suppress the noise and extract the signal is still desired.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Inductive Biases for Time Series Transformers", "weight": 1.0} -->

Thus, one future direction is to consider more effective ways to induce inductive biases into Transformers based on the understanding of time series data and characteristics of specific tasks.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Transformers and GNN for Time Series", "weight": 1.0} -->

Multivariate and spatio-temporal time series are becoming increasingly common in applications, calling for additional techniques to handle high dimensionality, especially the ability to capture the underlying relationships among dimensions. Introducing graph neural networks (GNNs) is a natural way to model spatial dependency or relationships among dimensions. Recently, several studies have demonstrated that the combination of GNN and Transformers/attentions could bring not only significant performance improvements like in traffic forecasting Cai et al.; Xu et al. and multi-modal forecasting Li et al., but also better understanding of the spatio-temporal dynamics and latent causality. It is an important future direction to combine Transformers and GNNs for effectively spatial-temporal modeling in time series.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Pre-trained Transformers for Time Series", "weight": 1.0} -->

Large-scale pre-trained Transformer models have significantly boosted the performance for various tasks in NLP Kenton and others; Brown et al. and CV Chen et al.. However, there are limited works on pre-trained Transformers for time series, and existing studies mainly focus on time series classification Zerveas et al.; Yang et al.. Therefore, how to develop appropriate pre-trained Transformer models for different tasks in time series remains to be examined in the future.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Transformers with Architecture Level Variants", "weight": 1.0} -->

Most developed Transformer models for time series maintain the vanilla Transformer's architecture with modifications mainly in the attention module. We might borrow the idea from Transformer variants in NLP and CV which also have architecture-level model designs to fit different purposes, such as lightweight Wu et al.; Mehta et al., cross-block connectivity Bapna et al., adaptive computation time Dehghani et al.; Xin et al., and recurrence Dai et al.. Therefore, one future direction is to consider more architecture-level designs for Transformers specifically optimized for time series data and tasks.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Transformers with NAS for Time Series", "weight": 1.0} -->

Hyper-parameters, such as embedding dimension and the number of heads/layers, can largely affect the performance of Transformers. Manual configuring these hyper-parameters is time-consuming and often results in suboptimal performance. AutoML technique like Neural architecture search (NAS) Elsken et al.; Wang et al. has been a popular technique for discovering effective deep neural architectures, and automating Transformer design using NAS in NLP and CV can be found in recent studies So et al.; Chen et al.. For industry-scale time series data which can be of both high dimension and long length, automatically discovering both memory- and computational-efficient Transformer architectures is of practical importance, making it an important future direction for time series Transformers.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have provided a survey on time series Transformers. We organize the reviewed methods in a new taxonomy consisting of network design and application. We summarize representative methods in each category, discuss their strengths and limitations by experimental evaluation, and highlight future research directions.
