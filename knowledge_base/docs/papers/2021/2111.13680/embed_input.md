GMFlow: Learning Optical Flow via Global Matching

Topics include Optical flow, GMFlow, Global matching, Transformers, Feature matching, Softmax correlation, Efficient inference.

GMFlow makes optical flow look more like global correspondence search than local cost-volume regression. It uses transformer-enhanced features and softmax global matching to reduce the need for many RAFT-style recurrent refinements, giving an efficient and conceptually clean large-displacement flow estimator.

Learning-based optical flow estimation has been dominated with the pipeline of cost volume with convolutions for flow regression, which is inherently limited to local correlations and thus is hard to address the long-standing challenge of large displacements. To alleviate this, the state-of-the-art framework RAFT gradually improves its prediction quality by using a large number of iterative refinements, achieving remarkable performance but introducing linearly increasing inference time. To enable both high accuracy and efficiency, we completely revamp the dominant flow regression pipeline by reformulating optical flow as a global matching problem, which identifies the correspondences by directly comparing feature similarities. Specifically, we propose a GMFlow framework, which consists of three main components: a customized Transformer for feature enhancement, a correlation and softmax layer for global feature matching, and a self-attention layer for flow propagation. We further introduce a refinement step that reuses GMFlow at higher feature resolution for residual flow prediction....

## Introduction

Since the pioneering learning-based work, FlowNet, optical flow has been regressed with convolutions for a long time. To encode the matching information into the network, the cost volume (*i.e*., correlation) was shown to be an effective component and thus has been extensively used in popular frameworks. However, such regression-based approaches have one major intrinsic limitation. That is, the cost volume requires a predefined size, as the search space is viewed as the channel dimension for subsequent regression with convolutions. This requirement restricts the search space to a *local* range, making it hard to handle large displacements.

Figure 1: Conceptual comparison of flow estimation approaches. Most previous methods regress optical flow from a local cost volume (i.e., correlation) with convolutions, while we perform global matching with a Transformer and differentiable matching layer (i.e., correlation and softmax).

We have presented a new global matching formulation for optical flow and demonstrated its strong performance. We hope our new perspective will pave a way towards a new paradigm for accurate and efficient optical flow estimation.

Broader impact. Our proposed method might produce unreliable results in occluded regions, thus care should be taken when using the prediction results from our model, especially for safety-critical scenarios like self-driving cars.

The framework presented so far (based on $1/8$ features) can already achieve competitive performance (Table 3). It can be further improved by introducing additional higher resolution ($1/4$) feature for refinement. Specifically, we first upsample the previous $1/8$ flow prediction to $1/4$ resolution, and warp the second feature with the current flow prediction. Then the refinement task is reduced to the residual flow learning, where the same GMFlow framework depicted in Fig. 2 can be used but in a local range....

Finally, the optical flow $\mathbf{V}$ can be obtained by computing the difference between the corresponding pixel coordinates

Bidirectional flow prediction. Our framework also simplifies backward optical flow computation by directly transposing the global correlation matrix in Eq.. Note that during training we only predict unidirectional flow while at inference we can obtain bidirectional flow for free, without requiring to forward the network twice,...
