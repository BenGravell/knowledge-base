<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GMFlow: Learning Optical Flow via Global Matching

Topics include Optical flow, GMFlow, Global matching, Transformers, Feature matching, Softmax correlation, Efficient inference.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

GMFlow makes optical flow look more like global correspondence search than local cost-volume regression. It uses transformer-enhanced features and softmax global matching to reduce the need for many RAFT-style recurrent refinements, giving an efficient and conceptually clean large-displacement flow estimator.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning-based optical flow estimation has been dominated with the pipeline of cost volume with convolutions for flow regression, which is inherently limited to local correlations and thus is hard to address the long-standing challenge of large displacements. To alleviate this, the state-of-the-art framework RAFT gradually improves its prediction quality by using a large number of iterative refinements, achieving remarkable performance but introducing linearly increasing inference time. To enable both high accuracy and efficiency, we completely revamp the dominant flow regression pipeline by reformulating optical flow as a global matching problem, which identifies the correspondences by directly comparing feature similarities. Specifically, we propose a GMFlow framework, which consists of three main components: a customized Transformer for feature enhancement, a correlation and softmax layer for global feature matching, and a self-attention layer for flow propagation. We further introduce a refinement step that reuses GMFlow at higher feature resolution for residual flow prediction. Our new framework outperforms 31-refinements RAFT on the challenging Sintel benchmark, while using only one refinement and running faster, suggesting a new paradigm for accurate and efficient optical flow estimation. Code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the pioneering learning-based work, FlowNet, optical flow has been regressed with convolutions for a long time. To encode the matching information into the network, the cost volume (*i.e*., correlation) was shown to be an effective component and thus has been extensively used in popular frameworks. However, such regression-based approaches have one major intrinsic limitation. That is, the cost volume requires a predefined size, as the search space is viewed as the channel dimension for subsequent regression with convolutions. This requirement restricts the search space to a *local* range, making it hard to handle large displacements.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To alleviate the large displacements issue, RAFT proposes an iterative framework with a large number of iterative refinements where convolutions are applied to different local cost volumes at different iteration stages so as to gradually reach near-global search space, achieving outstanding performance on standard benchmarks. The current state-of-the-art methods are all based on such an iterative architecture. Despite the excellent performance, such a large number of sequential refinements introduce linearly increasing inference time, which makes it hard for speed optimization and hinders its deployment in real-world applications. This raises a question: Is it possible to achieve both high accuracy and efficiency without requiring such a large number of iterative refinements?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We notice that another visual correspondence problem, *i.e*., sparse matching between an image pair, which usually features a *large viewpoint change*, moves into a different track. The top-performing sparse methods (*e.g*., SuperGlue and LoFTR ) adopt *Transformers* to reason about the mutual relationship between feature descriptors, and the correspondences are extracted with an explicit *matching* layer (*e.g*., softmax layer ).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by sparse matching, we propose to completely remove the additional convolutional layers operating on a predefined local cost volume, and reformulate optical flow as a *global matching* problem, which is distinct from all previous learning-based optical flow methods. Fig. 1 provides a conceptual comparison of these two flow estimation approaches. Our flow prediction is obtained with a differentiable matching layer, *i.e*., correlation and softmax layer, by comparing feature similarities. Such a formulation calls for more discriminative feature representations, for which the Transformer becomes a natural choice.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We would like to point out that although our pipeline shares the conceptual major components (*i.e*., Transfromer and the softmax matching layer) with sparse matching, our motivation is originated from the development of optical flow methods and the challenges associated with formulating optical flow as a global matching problem are quite different. Optical flow focuses on dense correspondences for every pixel and modern learning-based architectures are mostly designed by regression from a local cost volume. The scale and complexity of optical flow are much higher. Moreover, optical flow needs to deal with occluded and out-of-boundary pixels, for which the simple softmax-based matching layer will not be effective.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a GMFlow framework to realize the global matching formulation for optical flow. Specifically, the dense features extracted from a convolutional backbone network are fed into a Transformer that consists of self-, cross-attentions and feed-forward network to obtain more discriminative features. We then compare the feature similarities by correlating all pair-wise features. After that, the flow prediction is obtained with a differentiable softmax matching layer. To address occluded and out-of-boundary pixels, we incorporate an additional self-attention layer to propagate the high-quality flow prediction from matched pixels to unmatched ones by exploiting the feature self-similarity. We further introduce a refinement step that reuses GMFlow at higher feature resolution for residual flow prediction. Our full framework achieves competitive performance and higher efficiency compared with the state-of-the-art methods. Specifically, with only one refinement, GMFlow outperforms 31-refinements RAFT on the challenging Sintel dataset, while running faster.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We completely revamp the dominant flow regression pipeline by reformulating optical flow as a global matching problem, which effectively addresses the long-standing challenge of large displacements.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a GMFlow framework to realize the global matching formulation, which consists of three main components: a Transformer for feature enhancement, a correlation and softmax layer for global feature matching, and a self-attention layer for flow propagation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further propose a refinement step to exploit higher resolution feature, which allows us to reuse the same GMFlow framework for residual flow estimation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

GMFlow outperforms 31-refinements RAFT on the challenging Sintel benchmark, while using only one refinement and running faster, suggesting a new paradigm for accurate and efficient flow estimation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Methodology", "weight": 1.0} -->

Optical flow is intuitively a matching problem that aims at finding corresponding pixels. To achieve this, one can compare the similarity of the features for each pixel, and identify the corresponding pixel that gives the highest similarity. Such a process requires the features to be discriminative enough to stand out. Aggregating the spatial contexts within the image itself and information from another image can intuitively alleviate ambiguities and improve their distinctiveness. Such design philosophies have enabled great achievement in sparse feature matching frameworks. The success of sparse matching, which usually features a large viewpoint change, motivates us to formulate optical flow as an explicit global matching problem in order to address the challenge of large displacements.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Methodology", "weight": 1.0} -->

In the following, we first provide a general description of our global matching formulation, and then present a Transformer-based framework to realize it.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Formulation", "weight": 1.0} -->

Given two consecutive video frames ${\mathbf{I}}_{1}$ and ${\mathbf{I}}_{2}$, we first extract downsampled dense features ${{\mathbf{F}}_{1},{\mathbf{F}}_{2}} \in {\mathbb{R}}^{H \times W \times D}$ with a weight-sharing convolutional network, where $H,W$ and $D$ denote height, width and feature dimension, respectively. Considering the correspondences in the two frames should share high similarity, we first compare the feature similarity for each pixel in ${\mathbf{F}}_{1}$ with respect to all pixels in ${\mathbf{F}}_{2}$ by computing their correlations.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Formulation", "weight": 1.0} -->

where each element in the correlation matrix $\mathbf{C}$ represents the correlation value between coordinates ${\mathbf{p}}_{1} = {(i,j)}$ in ${\mathbf{F}}_{1}$ and ${\mathbf{p}}_{2} = {(k,l)}$ in ${\mathbf{F}}_{2}$, and $\frac{1}{\sqrt{D}}$ is a normalization factor to avoid large values after the dot-product operation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Formulation", "weight": 1.0} -->

To identify the correspondence, one naïve approach is to directly take the location that gives the highest correlation. However, this operation is unfortunately non-differentiable, which prevents end-to-end training. To tackle this issue, we use a differentiable matching layer. Specifically, we normalize the last two dimensions of $\mathbf{C}$ with the softmax operation, which gives us a matching distribution

<!-- chunk {"id": "body-0019", "role": "body", "section": "Formulation", "weight": 1.0} -->

Finally, the optical flow $\mathbf{V}$ can be obtained by computing the difference between the corresponding pixel coordinates

<!-- chunk {"id": "body-0020", "role": "body", "section": "Formulation", "weight": 1.0} -->

Such a softmax-based approach can not only enable end-to-end training but also provide sub-pixel accuracy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Feature Enhancement", "weight": 1.0} -->

Key to our formulation lies in obtaining high-quality discriminative features for matching. Recall that the features ${\mathbf{F}}_{1}$ and ${\mathbf{F}}_{2}$ in Sec. 3.1 are extracted *independently* from a weight-sharing convolutional network. To further consider their mutual dependencies, a natural choice is Transformer, which is particularly suitable for modeling the mutual relationship between two sets with the attention mechanism, as demonstrated in sparse matching methods. Since ${\mathbf{F}}_{1}$ and ${\mathbf{F}}_{2}$ are only two sets of features, they have no notion of the spatial position, we first add the fixed 2D sine and cosine positional encodings (following DETR ) to the features. Adding the position information also makes the matching process consider not only the feature similarity but also their spatial distance, which can help resolve ambiguities and improve the performance (Table LABEL:tab:transformer).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Feature Enhancement", "weight": 1.0} -->

After adding the position information, we perform six stacked self-, cross-attentions and feed-forward network (FFN) to improve the quality of the initial features. Specifically, for self-attention, the query, key and value in the attention mechanism are the same feature. For cross-attention, the key and value are same but different from the query to introduce their mutual dependencies. This process is performed for both ${\mathbf{F}}_{1}$ and ${\mathbf{F}}_{2}$ symmetrically, *i.e*.,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Feature Enhancement", "weight": 1.0} -->

where $\mathcal{T}$ is a Transformer, $\mathbf{P}$ is the positional encoding, the first input of $\mathcal{T}$ is query and the second is key and value.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Feature Enhancement", "weight": 1.0} -->

One issue in the standard Transformer architecture is the quadratic computational complexity due to the pair-wise attention operation. To improve the efficiency, we adopt the shifted local window attention strategy from Swin Transformer. However, unlike Swin that uses *fixed window size*, we split the feature to *fixed number of local windows* to make the window size adaptive with the feature size. Specifically, we split the input feature of size $H \times W$ to $K \times K$ windows (each with size $\frac{H}{K} \times \frac{W}{K}$), and perform self- and cross-attentions within each local window independently. For every two consecutive local windows, we shift the window partition by $(\frac{H}{2K},\frac{W}{2K})$ to introduce cross-window connections. In our framework, we split to $2 \times 2$ windows (each with size $\frac{H}{2} \times \frac{W}{2}$), which represents a good speed-accuracy trade-off (Table LABEL:tab:split_attn).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Flow Propagation", "weight": 1.0} -->

Our softmax-based flow estimation method implicitly assumes that the corresponding pixels are visible in both images and thus they can be matched by comparing their similarities. However, this assumption will be invalid for occluded and out-of-boundary pixels. To remedy this, by observing that the optical flow field and the image itself share high structure similarity, we propose to propagate the high-quality flow predictions in matched pixels to unmatched ones by measuring the feature self-similarity. This operation can be implemented efficiently with a simple self-attention layer (illustrated in Fig.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Flow Propagation", "weight": 1.0} -->

is the optical flow prediction from the softmax layer, which is obtained by substituting the stronger features in Eq. into the softmax matching layer in Sec. 3.1. Fig. 2 provides an overview of our GMFlow framework.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Flow Propagation", "weight": 1.0} -->

#blocks
Things (val, clean)
Sintel (train, clean)
Sintel (train, final)

<!-- chunk {"id": "body-0028", "role": "body", "section": "Refinement", "weight": 1.0} -->

The framework presented so far (based on $1/8$ features) can already achieve competitive performance (Table 3). It can be further improved by introducing additional higher resolution ($1/4$) feature for refinement. Specifically, we first upsample the previous $1/8$ flow prediction to $1/4$ resolution, and warp the second feature with the current flow prediction. Then the refinement task is reduced to the residual flow learning, where the same GMFlow framework depicted in Fig. 2 can be used but in a local range. Specifically, we split to $8 \times 8$ local windows (each with $1/32$ of the original image resolution) in the Transformer and perform a $9 \times 9$ local window matching for each pixel. After obtaining the flow prediction from the softmax layer, we perform a $3 \times 3$ local window self-attention operation for flow propagation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Refinement", "weight": 1.0} -->

Note that here we share the Transformer and self-attention weights in the refinement step with the global matching stage, which not only reduces parameters but also improves the generalization (Table LABEL:tab:refine). To generate the $1/4$ and $1/8$ features, we also share the backbone features. Specifically, we take a similar approach to TridentNet but use a weight-sharing convolution with strides $1$ and $2$, respectively. Such a weight-sharing design also leads to better performance than the feature pyramid network.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training Loss", "weight": 1.0} -->

where $N$ is the number of flow predictions including the intermediate and final ones, and $\gamma$ (set to 0.9) is the weight that is exponentially increasing to give higher weights for later predictions following RAFT.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training Loss", "weight": 1.0} -->

#splits
Things (val, clean)

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Datasets and evaluation setup. Following previous methods, we first train on the FlyingChairs (Chairs) and FlyingThings3D (Things) datasets, and then evaluate Sintel and KITTI training sets. We also evaluate on the Things validation set to see how the model performs on the same-domain data. Finally, we perform additional fine-tuning on Sintel and KITTI training sets and report the performance on the online benchmarks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Metrics. We adopt the commonly used metric in optical flow, *i.e*., the end-point-error (EPE), which is the average $\ell_{2}$ distance between the prediction and ground truth. For KITTI dataset, we also use *F1-all*, which reflects the percentage of outliers. To better understand the performance gains, we also report the EPE in different motion magnitudes. Specifically, we use $s_{0 - 10},s_{10 - 40}$ and $s_{40 +}$, to denote the EPE over pixels with ground truth flow motion magnitude falling to $0 - 10$, $10 - 40$ and more than $40$ pixels.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Implementation details. We implement our framework in PyTorch. Our convolutional backbone network is identical to RAFT's model, except that our final feature dimension is 128, while RAFT's is 256. We stack 6 Transformer blocks. To upsample the low-resolution flow prediction to the original image resolution, we use RAFT's convex upsampling method. We use AdamW as the optimizer. We first train the model on Chairs dataset for 100K iterations, with a batch size of 16 and a learning rate of 4e-4. We then fine-tune it on Things dataset for 200K iterations for ablation experiments, with a batch size of 8 and a learning rate of 2e-4. Our best model is fine-tuned on Things for 800K iterations. For the final fine-tuning process on Sintel and KITTI datasets, we report the details in Sec. 4.4. Further details are provided in the *supplementary material*.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Methodology Comparison", "weight": 1.0} -->

Flow estimation approach. We compare our Transformer and softmax-based flow estimation method with the cost volume and convolution-based approach. Specifically, we adopt the state-of-the-art cost volume construction method in RAFT that concatenates 4 local cost volumes at 4 scales, where each cost volume has a dimension of $H \times W \times {({{2R} + 1})}^{2}$, where $H$ and $W$ are image height and width, respectively, and the search range $R$ is set to 4 following RAFT. To regress flow, we stack different number of convolutional residual blocks to see how the performance varies. The final optical flow is obtained with a $3 \times 3$ convolution with 2 output channels. For our proposed framework, we stack different number of Transformer blocks for feature enhancement, where one Transformer block consists of self-, cross-attentions and a feed-forward network (FFN). The final optical flow is obtained with a global correlation and softmax layer. Both methods use bilinear upsampling in this comparison.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Methodology Comparison", "weight": 1.0} -->

Table 1 shows that the performance improvement of our method is more significant compared to the cost volume and convolution-based approach. For instance, our method with 2 Transformer blocks can already outperform 8 convolution blocks, especially for large motion ($s_{40 +}$). The performance can be further improved by stacking more layers, surpassing the cost volume and convolution-based approach by a large margin. We present more comparisons with all the possible combinations of different flow estimation approaches in the *supplementary material*, where our method is consistently better and has less parameters than other variants.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Methodology Comparison", "weight": 1.0} -->

Bidirectional flow prediction. Our framework also simplifies backward optical flow computation by directly transposing the global correlation matrix in Eq.. Note that during training we only predict unidirectional flow while at inference we can obtain bidirectional flow for free, without requiring to forward the network twice, unlike previous regression-based methods. The bidirectional flow can be used for occlusion detection with forward-backward consistency check (following ), as shown in Fig. 3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Methodology Comparison", "weight": 1.0} -->

#refine.
Things (val, clean)
Sintel (train, clean)
Sintel (train, final)

<!-- chunk {"id": "body-0039", "role": "body", "section": "Ablations", "weight": 1.0} -->

Transformer components. We ablate different Transformer components in Table LABEL:tab:transformer. The cross-attention contributes most, since it models the mutual relationship between two features, which is missing in the features extracted from the convolutional backbone network. Also, the position information makes the matching process position-dependent, and can be conducive to alleviate the ambiguities in pure feature similarity-based matching. Removing the feed-forward network (FFN) reduces a large number of parameters, while also leading to a moderate performance drop. The self-attention aggregates contextual cues within the same feature, bringing additional performance gains.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablations", "weight": 1.0} -->

Local window attention. We compare the speed-accuracy trade-off of splitting to different numbers of local windows for attention computation in Table LABEL:tab:split_attn. Recall that the extracted features from backbone is $1/8$ resolution, further splitting to ${{H/2} \times W}/2$ local windows (*i.e*., $1/16$ of the original resolution) represents a good trade-off between accuracy and speed, and thus is used in our framework.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablations", "weight": 1.0} -->

Matching Space. We replace our global matching with local matching in Table LABEL:tab:global_local_match and observe a significant performance drop, especially for large motion ($s_{40 +}$). Besides, the global matching can be computed efficiently with a simple matrix multiplication, while larger size for local matching will be slower due to the excessive sampling operation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablations", "weight": 1.0} -->

Flow propagation. Our flow propagation strategy results in significant performance gains in unmatched regions (including occluded and out-of-boundary pixels), as shown in Table LABEL:tab:prop. The structural correlation between the feature and flow provides a valuable clue to improve the performance of pixels that are challenging to match. Visual comparisons are provided in the *supplementary material*.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablations", "weight": 1.0} -->

Refinement. We compare whether to share the backbone when extracting $1/8$ and $1/4$ features, and whether to share the Transformer for matching at $1/8$ and $1/4$ resolutions. The results are shown in Table LABEL:tab:refine. Sharing Transformer and multi-scale features better regularizes the learning process, leading to better performance and less parameters.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablations", "weight": 1.0} -->

Training length. Our ablations thus far are based on 200K-iterations fine-tuning on Things dataset. In Table LABEL:tab:train_schedule, we show our framework benefits from more training iterations, consistent with the observations in previous vision Transformer works. We use 800K-iterations model as our final model in subsequent comparisons.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablations", "weight": 1.0} -->

We analyze the computational complexities of core components in our framework in the *supplementary material*.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison with RAFT", "weight": 1.0} -->

Sintel. Table 3 shows the results on Things validation set and Sintel clean and final training sets after training on Chairs and Things training sets. Without using any refinement, our method achieves better performance on Things and Sintel (clean) than RAFT with 11 refinements. By using an additional refinement, our method outperforms RAFT with 31 refinements, especially on large motion ($s_{40 +}$). Fig. 4 visualizes the results. Furthermore, our framework enjoys faster inference speed compared to RAFT and also does not require a large number of sequential processing. On the high-end A100 GPU, our framework gains more speedup compared with RAFT's sequential framework ($2.29 \times$ *vs*. $1.87 \times$, *i.e*., ours: $151\rightarrow 66$, RAFT: $170\rightarrow 91$), reflecting that our framework can benefit more from advanced hardware acceleration and showing its potential for further speed optimization.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison with RAFT", "weight": 1.0} -->

KITTI. Table 4 shows the generalization results on KITTI training set after training on Chairs and Things training sets. In this evaluation setting, our framework doesn't outperform RAFT, which is mainly caused by the gap between the synthetic training sets and the real-world testing dataset. One key reason behind our inferior performance is that RAFT, relying on fully convolutional neural networks, benefits from the inductive biases in convolution layers, which requires a relatively smaller size training data to generalize to a new dataset in comparison with Transformers. To substantiate this claim, we fine-tune both RAFT and our method on the additional Virtual KITTI 2 dataset. We can see from Table 4 that the performance gap becomes smaller when more data is available.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison on Benchmarks", "weight": 1.0} -->

Sintel. Following previous works, we further fine-tune our Things model on several mixed datasets that consist of KITTI, HD1K, FlyingThings3D and Sintel training sets. We perform fine-tuning for 200K iterations with a batch size of 8 and a learning rate of 2e-4. The results on Sintel test set are shown in Table 5. We achieve best performance among all the competitive state-of-the-art methods that only use two frames at inference. Although RAFT can also use last frame's prediction as initialization for subsequent refinement, we still achieve comparable performance in matched regions even without using multi-frame information. Qualitative comparisons between GMFlow and other state-of-the-art approaches on Sintel test set are shown in Fig. 5. More visual results on DAVIS dataset are given in the *supplementary material*.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison on Benchmarks", "weight": 1.0} -->

KITTI. We perform additional fine-tuning on the KITTI 2015 training set from the model trained on Sintel. We train GMFlow for 100K iterations with a batch size of 8 and a learning rate of 2e-4. Table 6 shows the evaluation results. For non-occluded (Noc) pixels, our performance is slightly inferior to RAFT. For all pixels that contain both non-occluded and occluded pixels, the performance gap becomes larger, which indicates that our inferior performance largely lies in occluded regions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Limitation and Discussion", "weight": 1.5} -->

Our framework still has room for future improvement in occluded regions, as can be seen from the KITTI results in Table 6. Besides, our framework may not generalize very well when the training data has significantly large gap with the test data (*e.g*., synthetic Things to real-world KITTI). Fortunately, there are many large-scale datasets available currently, *e.g*., Virtual KITTI, VIPER, REFRESH, AutoFlow and TartanAir, they can be used to enhance Transformer's generalization ability.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented a new global matching formulation for optical flow and demonstrated its strong performance. We hope our new perspective will pave a way towards a new paradigm for accurate and efficient optical flow estimation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Broader impact. Our proposed method might produce unreliable results in occluded regions, thus care should be taken when using the prediction results from our model, especially for safety-critical scenarios like self-driving cars.
