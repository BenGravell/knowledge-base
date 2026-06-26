<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gated Transformer Networks for Multivariate Time Series Classification

Topics include Deep learning, Convolutional networks, Transformers, Attention mechanisms, Computer vision, Classification, Time series classification, Time series, Datasets, Learning, Named gated transformer networks, GTN.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep learning model (primarily convolutional networks and LSTM) for time series classification has been studied broadly by the community with the wide applications in different domains like healthcare, finance, industrial engineering and IoT. Meanwhile, Transformer Networks recently achieved frontier performance on various natural language processing and computer vision tasks. In this work, we explored a simple extension of the current Transformer Networks with gating, named Gated Transformer Networks (GTN) for the multivariate time series classification problem. With the gating that merges two towers of Transformer which model the channel-wise and step-wise correlations respectively, we show how GTN is naturally and effectively suitable for the multivariate time series classification task. We conduct comprehensive experiments on thirteen dataset with full ablation study. Our results show that GTN is able to achieve competing results with current state-of-the-art deep learning models. We also explored the attention map for the natural interpretability of GTN on time series modeling. Our preliminary results provide a strong baseline for the Transformer Networks on multivariate time series classification task and grounds the foundation for future research.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are surrounded by the time series data such as physiological data in healthcare, financial records or various signals captured the sensors. Unlike univariate time series, multivariate time series has much richer information correlated in different channels at each time step. The classification task on univariate time series has been studied comprehensively by the community whereas multivariate time series classification has shown great potential in the real world applications. Learning representations and classifying multivariate time series are still attracting more and more attention.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As some of the most traditional baseline, distance-based methods work directly on raw time series with some pre-defined similarity measures such as Euclidean distance and Dynamic Time Warping (DTW)Keogh to perform classification. With k-nearest neighbors as the classifier, DTW is known to be a very efficient approach as a golden standard for decades. Following the scheme of well designed feature, distance metric and classifiers, the community proposed a lot of time series classification methods based on different kinds of feature space like distance, shapelet and recurrence, etc. These approaches kept pushing the performance and advanced the research of this field.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the recent success of deep learning approaches on different tasks on the temporal data like speech, video and natural language, learning the representation from scratch to classify time series has been attracted more and more studies. For example, Zheng et al. proposed a multi-scale convolutional networks for univariate time series classification. The author combines well-designed data augmentation and engineering approach like down sampling, skip sampling and sliding windows to preprocess the data for the multiscale settings, though the heavy preprocessing efforts and a large set of hyperparameters make it complicated and the proposed window slicing method for data augmentation is not scalable. Wang et al. firstly proposed two simple but efficient end-to-end models based on convolutions and achieved the state-of-the-art performance for univariate time series classification. Thereafter, convolution based models demonstrate superior performance on time series classification tasks Ismail Fawaz et al..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by the recent success of the Transformer networks on NLP Vaswani et al.; Devlin et al., we proposed a transformer based approach for multivariate time series classification. By simply scaling the traditional Transformer model by the gating that merges two towers, which model the channel-wise and step-wise correlations respectively, we show that how the proposed Gated Transformer Networks (GTN) is naturally and effectively suitable for the multivariate time series classification task. Specifically, our contributions are the following: We explored an extension of current Transformer networks with gating, named Gated Transformer Networks for the multivariate time series classification problem. By exploiting the strength where the Transformers processes data in parallel with self-attention mechanisms to model the dependencies in the sequence, we showed the gating that merges two towers of Transformer Networks that model the channel-wise and step-wise correlations is very effective for time series classification task.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluated GTN on the thirteen multivariate time series benchmark datasets and compared with other state-of-the-art deep learning models with comprehensive ablation studies. The experiments showed that GTN achieves competing performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We qualitatively studied the feature learned by the model by visualization to demonstrate the quality of the feature extraction of GTN.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We preliminary explored the interpretability of the attention map of GTN on time series modeling to study how self-attention helps on channel-wise and step-wise feature extraction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Gated Transformer Networks", "weight": 1.0} -->

Traditional Transformer has encoder and decoder stacking on the word and positional embedding for sequence generation and forecasting task. As for multivariate time series classification, we have three extension simply to adapt the Transformer for our need - embedding, two towers and gating. The overall architecture of Gated Transformer Networks is shown in Figure 1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Embedding", "weight": 1.0} -->

In the original Transformers, the tokens are projected to a embedding layer. As time series data is continuous, we simply change the embedding layer to fully connected layer. Instead of linear projection, we add a non-linear activation $tanh$. Following Vaswani et al., the positional encoding is added with the non-linearly transformed time series data to encode the temporal information, as self-attention is hard to utilize the sequential correlation of time step.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Two-tower Transformer", "weight": 1.0} -->

Multivariate time series has multiple channels where each channel is a univariate time series. The common assumption is that there exists hidden correlation between different channels at current or warping time step. Capturing both the step-wise (temporal) and channel-wise (spatial) information is the key for multivariate time series research. One common approach is to exploit convolutions. That is, the reception field integrates both step-wise and channel-wise by the 2D kernels or the 1D kernels with fixed parameter sharing. Different from other works that leverage the original Transformer for time series classification and forecasting, we designed a simple extension of the two-tower framework, where the encoders in each tower explicitly capture the step-wise and channel-wise correlation by attention and masking, as shown in Figure 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Two-tower Transformer", "weight": 1.0} -->

Step-wise Encoder. To encode the temporal feature, we use the self-attention with mask to attend on each point cross all the channels by calculating the pair-wise attention weights among all the time steps. In the multi-head self-attention layers, the scaled dot-product attention formulates the attention matrix on all time step. Like the original Transformer architecture, position-wise fully connected feed-forward layers is stacked upon each multi-head attention layers for the enhanced feature extraction. The residual connection around each of the two sub-layers is also kept to direct information and gradient flow, following by the layer normalization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Two-tower Transformer", "weight": 1.0} -->

Channel-wise Encoder. Likewise, the Channel-wise encoder calculates the attention weights among different channels across all the time step. Note that position of channel in the multivariate time series has no relative or absolute correlation, as if we switch the order of channels, the time series should has no changes. Therefore, we only add positional encoding in the Step-wise Encoder. Attention layers with the masking on all the channels is expected to explicitly capture the correlation among channels across all time step. Note that it is pretty straight-forward to implement both encoders by simply transpose the channel and time axis when feeding the time series for each encoders.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gating", "weight": 1.0} -->

To merge the feature of the two towers which encodes step-wise and channel-wise correlations, a simple way is to concatenate all the features from two towers, which compromises the performance of both as shown in our ablation study.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gating", "weight": 1.0} -->

Instead, we proposed a simple gating mechanism to learn the weight of each tower. After getting the output of each tower, which had a fully connect layer after each output of both encoders with non-linear activation as $C$ and $S$, we packed them into vector by concatenation followed by a linear projection layer to get $h$. After the softmax function, the gating weight are computed as $g_{1}$ and $g_{2}$. Then each gating weight is attending on the corresponding tower's output and packed as the final feature vector.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

We test GTN on the same subset of the Baydogan archive Baydogan, which contains 13 multivariate time series datasets. All the datasets have been split into training and testing by default, and there is no preprocessing for these time series. We choose the following deep learning models as the benchmarks.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Fully Convolutional Networks (FCN) and Residual Networks (ResNet) Wang et al.. These are reported to be among the best deep learning models in the multivariate time series classification task Ismail Fawaz et al.. Multi-layer Perception (MLP) is also included as a simple baseline in our comparison.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Universal Neural Network Encoder (Encoder) Serrà et al..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Multi-scale Convolutional Neural Network (MCNN) Cui et al..

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Multi Channel Deep Convolutional Neural Network (MCDCNN) Zheng et al..

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Time Convolutional Neural Network (Time-CNN) Zhao et al..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Time Warping Invariant Echo State Network (TWIESN) Tanisaro and Heidemann.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

The Gated Transformer Network is trained with Adagrad with learning rate 0.0001 and dropout = 0.2. The categorical cross-entropy is used as the loss function. Learning rate schedule on plateau Wang et al.; Ismail Fawaz et al. is applied to train the GTN. We test on the training set and the test set every certain number of iterations, the best test results and its super parameters would be recorded. For fair comparison, we choose to report the test accuracy on the the model with the best training loss as Ismail Fawaz et al..^22^2The codes are available at

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

The results are shown in Table 1. GTN achieved comparable results with the FCN and ResNet. Note that the results has no statistical significant difference among these three models, though on NetFlow and KickvsPunch datasets, GTN shows superior performance. The drawback of GTN is comparably leaning to overfitting. Unlike FCN and ResNet where no dropout is used, the GTN has dropout binding with layer norm to reduce the risk of overfitting.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

To clearly state the performance gain from each module in the GTN, we performed a comprehensive study as shown in Table 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Following the traditional Transformer, masking helps to ensure that the predictions for position $i$ can depend only on the known previous outputs and also helps the attention to not attend to the padding position. This benefits holds not only on the language but also on the time series data, as the tower-only transformer with mask are overall a bit better than the one without masks.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Channel-wise only transformer outperforms step-wise only transformer on the majority of the dataset. This preliminary result supports our assumption that for multivariate time series, the correlation between different channels across all time step is an important differentiator with the univariate time series. The attention with mask is able to catch the channel-wise feature better.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Different time series data might show different leaning on channel-wise and step-wise information. For example, on the dataset PEMS, the step-wise Transformer model works better. On the dataset, the channel-wise Transformer model outperforms.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Following the above point, exploiting both towers is a straight-forward solution. However, simple concatenation of the two towers sometimes works, but the performance always fall on the middle ground or even worse. Like on the dataset PEMS and, step-wise model and channel-wise model works best for each cases. After concatenation of both towers' feature, the results becomes even worse.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

By adding the gating weights before simple (equally-weighted) concatenation, the model is able to learn when to rely on a specific tower more by a pure data-driven way, thus show the best performance in this study.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Visualization and Analysis of the Attention Map", "weight": 1.0} -->

Note that the smaller DTW does not mean two sequence are similar. Like shown on the channel-wise DTW, block $c$ indicates very small DTW distance between $c3$ and $c11$. Actually $c11$ and $c3$ are very different in trends and shapelet. Our preliminary analysis shows that the channel-wise attention also tends to grab the similar sequences where DTW shows no clear differentiated factors.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Visualization and Analysis of the Attention Map", "weight": 1.0} -->

As the step is fixed across channel for the step-wise attention, Euclidean distance is the special case of DTW at the same step, thus we choose Euclidean distance as the metric. Through the analysis of step-wise attention map and the Euclidean distance matrix, the distance between the time series and the similarity of the shapelet have an impact on who GTN calculates the attention scores, though the impact are not that obvious which deserves a deep dive in the future work.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Analysis on the Gating Weight", "weight": 1.0} -->

GTN has two towers to encode the step-wise and channel-wise information with self-attention respectively. With the gating method, the model learns to assign different weights to attend to these two Transformers. In the ablation study, we show that gating achieved better results compared with concatenation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Analysis on the Gating Weight", "weight": 1.0} -->

By observing the gate weights assigned to the two tower on the AULSAN data set, we found that for different sample, the gating weights assigned to step-wise and channel-wise tower are tends to be different, like $\{ 0.9899,0.0101\}$ and $\{ 0.0443,0.5557\}$ for two sample time series respectively. However, the gating weights overall show the trends to be skewed towards the step-wise tower, with the average gating weights of $\{ 0.7786,0.2214\}$. As shown in Table 2, the step-wise Transformer outperforms the channel-wise Transformer, thus overall the gating learns to assign more weights to the step-wise tower, the gating behavior and the results in the ablation study are consistent. The gating shows the capability to learn the weights from the data-driven manner to attend on each towers for different samples and dataset to improve the classification performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

As each time step are transformed to a dense vector through the embedding layer, we use the t-SNE Maaten and Hinton to reduce the dimension of the output from the embedding layer on AUSLAN. The result is shown in graph 4. The graph shows that all the points are clustered together on the specific manifold. We roughly labeled those clusters with five different colors.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

As shown in Figure 5, we mapped each color back to the raw time series. Interestingly, the time step from each cluster are consistent and overall each cluster shows different shapelet.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

The green shapelet indicates a deep M shape.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

The light blue shapelet is a sharp trending-up sub-sequence.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

The dark blue shapelet is a plateau followed by a deep down like $7$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

The magenta shapelet is like a recovering from the deep down with a bit trending up.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Analysis of the Embedding Output", "weight": 1.0} -->

By a closer look at the visualization of the embedding on each time step, the near points that forms some interesting shapelet has relatively smaller distance in the vector space. Like Liu and Wang, where the author discover interesting shapelet by a well designed Markov transition matrix with the clustering on the transformed complex network graph, GTN shows the potential by learning the interesting pattern of some specific sub-sequences from scratch, which will be an interesting future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented the Gated Transformer Network (GTN) as a simple extension of multidimensional time series using gating. With the gating that merges two towers of transformer networks which model the channel-wise and step-wise correlations respectively GTN is able to explicitly learn both channel-wise and step-wise correlations. We conducted comprehensive experiments on thirteen dataset and the preliminary results show that GTN is able to achieve competing performance with current state-of-the-art deep learning models. The ablation study shows how different modules work to together to achieve the improved performance. We also qualitatively analyzed the attention map and other components with visualization to better understand the interpretability of out model. Our preliminary results ground a solid foundation for the study of Transformer Network on the time series classification task in future research.
