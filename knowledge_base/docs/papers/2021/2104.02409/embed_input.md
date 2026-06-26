<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Estimate Hidden Motions with Global Motion Aggregation

Topics include Optical flow, GMA, Occlusion handling, Global motion aggregation, Transformers, Self-similarity, RAFT extension.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

GMA targets one of RAFT's weak spots: estimating motion for pixels that disappear or become occluded between two frames. By aggregating motion features globally using transformer-style dependencies, it propagates reliable motion information from visible regions to hidden ones without requiring extra frames.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Occlusions pose a significant challenge to optical flow algorithms that rely on local evidences. We consider an occluded point to be one that is imaged in the first frame but not in the next, a slight overloading of the standard definition since it also includes points that move out-of-frame. Estimating the motion of these points is extremely difficult, particularly in the two-frame setting. Previous work relies on CNNs to learn occlusions, without much success, or requires multiple frames to reason about occlusions using temporal smoothness. In this paper, we argue that the occlusion problem can be better solved in the two-frame case by modelling image self-similarities. We introduce a global motion aggregation module, a transformer-based approach to find long-range dependencies between pixels in the first image, and perform global aggregation on the corresponding motion features. We demonstrate that the optical flow estimates in the occluded regions can be significantly improved without damaging the performance in non-occluded regions.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This approach obtains new state-of-the-art results on the challenging Sintel dataset, improving the average end-point error by 13.6% on Sintel Final and 13.7% on Sintel Clean. At the time of submission, our method ranks first on these benchmarks among all published and unpublished approaches. Code is available at

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

How can we estimate the 2D motion of a point we only see once? This is the problem faced by optical flow algorithms for points that become occluded between frames. Estimating the optical flow, that is, the apparent motion of pixels in an image as the camera and scene move, is a classic problem in computer vision studied since the seminal work of Horn and Schunck. There are many factors that make optical flow prediction a hard problem, including large motions, motion and defocus blur, and featureless regions. Among these challenges, occlusion is one of the most difficult and under-explored. In this paper, we propose an approach that specifically targets the occlusion problem in the case of two-frame optical flow prediction.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We first define what we mean by occlusion in the context of optical flow estimation. In this paper, an occluded point is defined as a 3D point that is imaged in the reference frame but is not visible in the matching frame. This definition incorporates several different scenarios, such as the query point moving out-of-frame or behind another object (or itself), or another object moving in front of the query point, in the active sense. One particular case of occlusion is shown in Figure LABEL:fig:demo, where part of the blade moves out-of-frame.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Flow (Ground Truth) Figure 1: Recovering hidden motions. In row 1, the bottom left corner of the ground moves out-of-frame, but reasoning that it belongs to the background allows the motion to be recovered from other parts of the image. In row 2, the girl’s staff is mostly occluded in the second frame, but strong cues from the visible parts can resolve its motion. Our approach can estimate many hidden motions despite the presence of occlusions. The flow maps and the error maps have been fetched from the Sintel server. Best viewed in colour on a screen.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The challenge posed by occlusions can be understood by looking at the underlying assumptions of optical flow algorithms. Traditional optical flow algorithms apply the brightness constancy constraint, where pixels related by the flow field are assumed to have the same intensities. It is clear that occlusions are a direct violation of such a constraint. In the deep learning era, correlation (cost) volumes are used to give a matching cost for each potential displacement of a pixel. However, correlations of appearance features are unable to give meaningful guidance for learning the motion of occluded regions. Most existing approaches use smoothness terms in an MRF to interpolate occluded motions or use CNNs to directly learn the neighbouring relationships, hoping to learn to estimate occluded motions based on the neighbouring pixels. However, state-of-the-art methods still fail to estimate occluded motions correctly when occlusions are more significant and local evidence is insufficient to resolve the ambiguity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, humans are able to synthesise information from across the image and apply plausible motion models to accurately estimate occluded motions. This capability is valuable to emulate, because we fundamentally care about recovering the real 3D motion of objects in a scene, for which estimating occluded motion is necessary. Downstream applications, including tracking and activity detection, can also benefit from short-term predictions of the motion of occluded points, particularly if they reappear later or exhibit some characteristic of interest (*e.g*., high-velocity out-of-frame motions).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let us consider how to estimate these hidden motions for the two-frame case. When direct (local) matching information is absent, the motion information has to be propagated from other pixels. Using convolutions to propagate this information has the drawback of limited range since convolution is a local operation. We propose to aggregate the motion features with a non-local approach. Our design is based on the assumption that the motions of a single object (in the foreground or background) are often homogeneous. One source of information that is overlooked by existing works is self-similarities in the reference frame. For each pixel, understanding which other pixels are related to it, or which object it belongs to, is an important cue for accurate optical flow predictions. That is, the motion information of non-occluded self-similar points can be propagated to the occluded points. Inspired by the recent success of transformers, we introduce a global motion aggregation (GMA) module, where we first compute an attention matrix based on the self-similarities of the reference frame, then use that attention matrix to aggregate motion features.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use these globally aggregated motion features to augment the successful RAFT framework and demonstrate new state-of-the-art results in optical flow estimation, such as those examples in Figure 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key contributions of our paper are as follows. We show that long-range connections, implemented using the attention mechanism of transformer networks, are highly beneficial for optical flow estimation, particularly for resolving the motion of occluded pixels where local information is insufficient. We show that self-similarities in the reference frame provide an important cue for selecting the long-range connections to prioritise. We demonstrate that our global motion feature aggregation strategy leads to a significant improvement in optical flow accuracy in occluded regions, without damaging the performance in non-occluded regions, and analyse this extensively. We improve the average end-point error (EPE) by 13.6% (2.86 $\rightarrow$ 2.47) on Sintel Final and 13.7% (1.61 $\rightarrow$ 1.39) on Sintel Clean, compared to the strong baseline of RAFT. Our approach ranks first on both datasets at the time of submission.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Occlusions in optical flow", "weight": 1.0} -->

Occlusion poses a key challenge in optical flow estimation due to its violation of the brightness constancy constraint. Most traditional optical flow algorithms treat occlusions as outliers and so develop and optimise robust objective functions. In continuous optimisation for optical flow, Brox *et al*. used the $L^{1}$ norm due to its robustness to outliers caused by occlusions or large brightness variations. Zach *et al*. added total variation regularisation and proposed an efficient numerical scheme to optimise the energy functional. This formulation was later improved by Wedel *et al*.. Later work introduced additional robust optimisation terms, including the Charbonnier potential and the Lorentzian potential.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Occlusions in optical flow", "weight": 1.0} -->

More recently, discrete optimisation approaches, especially Markov Random Fields (MRFs), have been used to estimate optical flow. These algorithms first estimate the forward and backward flows separately using a robust, truncated data term. They then conduct a forward--backward consistency check to determine the occluded regions. Lastly, as a post-processing step, they use interpolation methods to fill in the optical flow of the occluded regions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Occlusions in optical flow", "weight": 1.0} -->

Other work incorporates occlusion estimation as a joint objective together with optical flow estimation. Alvarez *et al*. use forward--backward consistency as an optimisation objective, thus estimating time-symmetric optical flow. In addition to forward--backward consistency, MirrorFlow incorporates occlusion--disocclusion symmetry in the energy function and achieves performance improvements. Since occlusions are caused by 3D motions, other works explicitly model local depth relationships into layers and reason about occlusions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Occlusions in optical flow", "weight": 1.0} -->

Contrary to the above approaches, we do not overload the loss function with explicit occlusion reasoning. Instead, we adopt a learning approach, similar to other supervised deep optical flow learning approaches. Rather than estimating an occlusion map explicitly, our goal is to improve the optical flow accuracy at occluded regions. We take an implicit approach to globally aggregate motion features, which provides extra information to correctly predict flow at occluded regions. Our approach can be thought of as a non-local interpolation approach, in contrast to local interpolation approaches. In the deep learning literature, the occlusion problem has been addressed in an unsupervised learning setting, however, existing supervised learning approaches all rely on convolutions to interpolate in occluded regions, which are prone to failure for more significant occlusions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Self-attention and transformers", "weight": 1.0} -->

Our design principle is inspired by the recent successes of the transformer literature. The transformer architecture was first successful in natural language processing (NLP), due to its ability to model long-range dependencies and its scalability for GPU parallel processing. Among various modules in the transformer achitecture, self-attention is the key design feature that make transformers work. Recently, researchers have introduced the transformer and related attention ideas to the vision community, mostly in high-level tasks such as image classification and semantic segmentation. To the best of our knowledge, we are the first to use the idea of attention to solve the optical flow problem. Different from many existing works in the transformer literature, we do not use self-attention in our work. Self-attention refers to the query, key and value vectors coming from the same features. In our case, query and key vectors come from the context features modelling the appearance of the image while value vectors come from the motion features, which is an encoding of the correlation volume.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Overview", "weight": 1.0} -->

In his first paper from 1976, Geoffrey Hinton wrote that "local ambiguities have to be resolved by finding the best global interpretation". This idea still holds true in the modern deep learning era. To resolve ambiguities caused by occlusions, our core idea is to allow the network to reason at a higher level, that is, to globally aggregate the motion features of similar pixels, having implicitly reasoned about which pixels are similar in appearance feature space. We hypothesise that the network will be able to find points with similar motions by looking for points with similar appearance in the reference frame. This is motivated by the observation that the motions of points on a single object are often homogeneous. For example, the motion vectors of a person running to the right have a bias towards the right, which holds even if we do not see where a large part of the person ends up in the matching frame due to occlusion. We can use this statistical bias to propagate motion information from non-occluded pixels, with high (implicit) confidence, to occluded pixels, with low confidence.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Overview", "weight": 1.0} -->

Here, confidence can be interpreted as whether there exists a distinct matching, *i.e*., a high correlation value at the correct displacement.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overview", "weight": 1.0} -->

With these ideas, we take inspiration from transformer networks, which are known for their ability to model long-range dependencies. Different from the self-attention mechanism in transformers, where query, key and value come from the same feature vectors, we use a generalized variant of attention. Our query and key features are projections of the context feature map, which are used to model the appearance self-similarities in frame 1. The value features are projections of the motion features, which themselves are an encoding of the 4D correlation volume. The attention matrix computed from the query and key features is used to aggregate the value features which are hidden representations of motions. We name this a Global Motion Aggregation (GMA) module. The aggregated motion features are concatenated with the local motion features as well as the context features, which is to be decoded by the GRU. A detailed diagram of GMA is shown in Figure 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Mathematical Formulation", "weight": 1.0} -->

Let $\mathbf{x} \in {\mathbb{R}}^{N \times D_{\text{c}}}$ denote the context (appearance) features and $\mathbf{y} \in {\mathbb{R}}^{N \times D_{\text{m}}}$ denote the motion features, where $N = {HW}$ and $H$ and $W$ are the height and width of the feature map, $D$ refers to the channel dimension of the feature map. The $i^{\text{th}}$ feature vector is denoted $\mathbf{x}_{i} \in {\mathbb{R}}^{D_{\text{c}}}$. Our GMA module computes the feature vector update as an attention-weighted sum of the projected motion features.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Mathematical Formulation", "weight": 1.0} -->

The aggregated motion features are given by where $\alpha$ is a learned scalar parameter initialised to zero, $\theta$, $\phi$ and $\sigma$ are the projection functions for the query, key, and value vectors, and $f$ is a similarity attention function given by The projection functions for the query, key and value vectors are given by where ${\mathbf{W}_{\text{qry}},\mathbf{W}_{\text{key}}} \in {\mathbb{R}}^{D_{\text{in}} \times D_{\text{c}}}$ and $\mathbf{W}_{\text{val}} \in {\mathbb{R}}^{D_{\text{m}} \times D_{\text{m}}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Mathematical Formulation", "weight": 1.0} -->

The final output is $\lbrack{\mathbf{y}{|\hat{\mathbf{y}}|}\mathbf{x}}\rbrack$, a concatenation of the three feature maps. The GRU decodes this to obtain the residual flow. Concatenation allows the network to intelligently select from or combine the motion vectors, modulated by the global context feature, without prescribing exactly how it is to do this. It is plausible that the network learns to encode some notion of uncertainty, and decodes the aggregated motion vector only when the model cannot be certain of the flow from the local evidence.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Mathematical Formulation", "weight": 1.0} -->

We also explore the use of a 2D relative positional embedding, allowing the attention map to depend on both the feature self-similarity and the relative position from the query point. For this, we compute the aggregated motion vector as where $\mathbf{p}_{j - i}$ denotes the relative positional embedding vector indexed by the pixel offset $j - i$. Separate embedding vectors are learned for the vertical and horizontal offsets and are summed to obtain $\mathbf{p}_{j - i}$. If it is useful to suppress pixels that are very close or very far from the query point when aggregating the motion vectors, then this positional embedding has the capacity to learn this behaviour.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Mathematical Formulation", "weight": 1.0} -->

We also investigated computing the attention map from only the query vectors and positional embedding vectors, without any notion of self-similarity. That is, This can be regarded as learning long-range aggregation without reasoning about the image content. It is plausible that positional biases in the dataset could be exploited by such a scheme. In Table 2, the results for and are denoted as Ours (+p) and Ours (p only).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We follow the standard optical flow training procedure of first pre-training our model on FlyingChairs for 120k iterations with a batch size of 8 and then on FlyingThings for another 120k iterations with a batch size of 6. We then fine-tune on a combination of FlyingThings, Sintel, KITTI 2015 and HD1K for 120k iterations for Sintel evaluation and 50k on KITTI 2015 for KITTI evaluation. A batch size of 6 is set for fine-tuning. We train our model on two 2080Ti GPUs with the PyTorch library using the mixed precision strategy. We adopt the same hyperparameters as RAFT for the base network. We adopt the one-cycle learning rate policy with the highest learning rate set to $2.5 \times 10^{- 4}$ for FlyingChairs then $1.25 \times 10^{- 4}$ for the rest.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For GMA, we choose channel dimensions ${D_{\text{in}} = D_{\text{c}} = D_{\text{m}} = 128}.$ The main evaluation metric we use is average end-point error (AEPE), which refers to the mean pixelwise flow error. KITTI also uses the Fl-All (%) metric which refers to the percentage of optical flow vectors whose end-point error is larger than 3 pixels or over $5\%$ of ground truth.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The Sintel dataset has been created with different rendering passes that have different levels of complexity. For training and test evaluation on the Sintel server, we used the Clean and Final passes. The Clean pass is rendered with illumination including smooth shading and specular reflections. The Final pass is created with full rendering, which includes motion blur, camera depth-of-field blur, and atmospheric effects.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

In the Sintel training set, they also provided the Albedo pass, which is rendered without illumination effects and has roughly piecewise-constant colours. An example is shown in Figure 4. We do not use this set for training, but reserve it as an evaluation dataset. The motivation for doing so is that the Albedo set adheres to brightness constancy everywhere apart from occluded regions. By evaluating and analysing on the occluded regions and non-occluded regions separately, we can clearly see how well our method performs when addressing the occlusion problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Occlusion Analysis", "weight": 1.0} -->

To verify the effectiveness of our proposed GMA module at estimating the motion of occluded points, we make use of the occlusion maps provided in the Sintel training set, which partition the pixels into non-occluded (Noc) and occluded (Occ) pixels. We further divide the occluded pixels into in-frame ('Occ-in') and out-of-frame ('Occ-out') occlusions, depending on whether the ground-truth flow vector points inside or outside the image frame. An example is shown in Figure 4.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Occlusion Analysis", "weight": 1.0} -->

We evaluated on all three rendering passes of Sintel, where the results for Clean and Final are training set errors and those for Albedo are test set errors. We evaluated the AEPE for different regions, results of which are shown in Table 1. We observe that the relative improvement of our method compared to RAFT is predominantly attributable to better predictions of the flow for occluded points. This is reinforced by the results on the Albedo dataset where the brightness constancy assumption holds exactly for non-occluded points, removing confounding factors. Finally, out-of-frame occlusions are more challenging than in-frame occlusions for both models, but we still observe a significant improvement for these pixels. We hypothesise that the improvement in non-occluded regions is due to GMA's ability to resolve ambiguities caused by other brightness variations, for example specular reflections, blurs, and other sources. This result strongly supports our claim that global aggregation can help resolve ambiguities caused by occlusion.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Comparison with Prior Works", "weight": 1.0} -->

Having shown that our approach can improve optical flow estimates for occluded regions, we compare against prior works on the overall performance. We evaluate our approach on the Sintel dataset and the KITTI 2015 optical flow dataset. At the time of submission, we have obtained the best results on both the Sintel Final and Clean benchmarks among all submitted results published and unpublished. Compared with our baseline approach RAFT, we have improved the AEPE from $2.86$ to $2.47$ ($13.6\%$ improvement) on Sintel Final and $1.61$ to $1.39$ ($13.7\%$ improvement) on Sintel Clean. This significant improvement over RAFT validates our claim that our approach can improve flow prediction for occluded regions without damaging the performance of non-occluded regions. The Sintel server also reports the metric 'EPE unmatched', which measures the endpoint error over regions that are visible only in one frame, predominantly caused by occlusion. Our approach also ranks first under this metric in both Clean and Final, with a margin of 0.9 EPE on Clean (2.2 w.r.t.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Comparison with Prior Works", "weight": 1.0} -->

RAFT) and 1.3 EPE on Final (1.7 w.r.t. RAFT). Overall, our model achieves a new state-of-the-art result in optical flow estimation, which demonstrates the usefulness of addressing the occlusion problem in optical flow.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Comparison with Prior Works", "weight": 1.0} -->

On the KITTI 2015 test set, our results are on par with RAFT. 'Ours (p only)', which uses positional attention only, outperforms RAFT, while 'Ours', which uses content self-similarity attention, slightly underperforms. It is likely that the lack of improvement on this dataset is due to having insufficient training data (only 200 pairs of images) for the network to learn high-level appearance feature similarities.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Qualitative results are shown in Figure 1 for two examples in the Sintel Clean dataset. The optical flow error in regions of the image that move out-of-frame or behind another object is significantly reduced compared to RAFT. These scenes are highly challenging with lots of motion and occlusion. For example, it is not unreasonable that RAFT is unable to keep track of the wooden staff that becomes partially occluded in the second image, given that it is well-camouflaged in a forest, fast-moving, and very thin. However, our model is able to very accurately predict the staff's motion, despite these challenges.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

We also present visualisations of the learned attention maps for two examples in Figure 5. To train effectively, the network should learn to attend to pixels that share similar motion vectors. For foreground points, we expect this to be most easily achieved by attending to points on the same object, while for background points it may be sufficient to attend to any other background point. These examples justify this expectation and provide support for the argument that appearance (and higher-order) self-similarity is being learned by the network, and that this is helpful for estimating the flow of the occluded points.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Ablation Results", "weight": 1.0} -->

To verify our design, we conducted the following ablation experiments. We first compare the performance of the tested variants of the model, where positional attention replaces (p only) or adds to (+p) the self-similarity attention, as presented in Table 2. We find that self-similarity is sufficient to achieve the performance improvements, with the positional encoding only helping for the KITTI dataset. This coincides with our intuition that long-range connections are helpful and that distance-based suppression is unnecessary. In addition, we ablate over three design choices: learning the scalar parameter $\alpha$ vs fixing it at $1$, concatenating with local motion features vs replacing local motion features, and using a residual connection (adding the output of the aggregator to the local motion features) vs not using residual connection (directly concatenating the output of the aggregator with the motion features and context features). The results are shown in Table 3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Ablation Results", "weight": 1.0} -->

The key experiment here is showing that concatenation is an important part of the network design. The hypothesis was that the network should learn how to select or combine the local and globally-aggregated features, based on some implicit measure of uncertainty. That is, it is not helpful to replace local features in most non-occluded regions, where they may be more reliable and precise than the aggregated features. While the residual connection may also be able to handle this, using both mechanisms leads to the best performance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Timing, Parameter Counts and Memory", "weight": 1.0} -->

We demonstrate that the computational overhead of GMA is low relative to the performance improvement, as shown in Table 4. The parameter count for our model is 5.9M compared to RAFT which is 5.3M. We tested the inference time on a single RTX 3090 GPU, with RAFT taking 60ms on average and ours taking 72ms for a single pair of image in the Sintel dataset. The image size is 436$\times$`<!-- -->`{=html}1024. The GRU iteration number is set to 12. We also tested the GPU memory consumption for training. When training on FlyingChairs on a single 3090 card, with a random crop of 368$\times$`<!-- -->`{=html}496 and batch size of 8, RAFT takes 16.0GB memory while our network takes 17.2GB memory. We can see that overall the computational overhead is modest while the improvement in results is significant.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have demonstrated empirically that long-range connections, weighted by image self-similarities, are very effective at resolving the optical flow of occluded 3D points. The intuition is that if the network can determine which non-occluded points are moving in the same way, this information can be transmitted to 'in-paint' the motion of the occluded points. Determining which points have similar motion characteristics is a non-trivial task and relies on the exploitation of statistical biases. Similar flow vectors are frequently observed for points belonging to the same class, due to the homogeneous motion in 3D. This suggests that we should enable the network to aggregate over motions of the same scene objects, which motivates our choice to explicitly expose the self-similarity of image features to our GMA module. However, additive aggregation of this kind is only helpful when the flow field of the attended locations is approximately homogeneous. This does not hold exactly for general object and camera motions, where the flow fields may be far from homogeneous, even on the same rigid object. An example is an object that is directly in front of the camera and rotating about the optical axis, where the flow vectors are in opposite directions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

To deal with such scenarios, one possible future work is to first transform the motion features based on the relative positions and perform aggregation afterwards.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Occlusions have long been considered a significant challenge and a major source of error in optical flow estimation. Inspired by the recent success of transformers, we introduce a global motion aggregation module to globally aggregate motion features based on appearance self-similarity of the first image. This has been validated by experiments that show significantly improved optical flow predictions for occluded regions, particularly the large reduction of EPE on Sintel Clean and Final. Our approach of aggregating information over long-range connections using self-similarity is a simple and effective way to introduce higher-order reasoning into the optical flow problem and is applicable to any supervised flow network. We expect that further development of aggregation mechanisms or alternatives would lead to additional performance improvements.
