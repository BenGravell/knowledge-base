## Introduction

Transformers dominate modern perception, yet dense attention over long image sequences and large 3D search spaces remains a barrier to real-time deployment. In autonomous driving, where latency and safety are critical, the challenge is not only to *reduce* computation but to *allocate* it selectively. Vision Transformer (ViT) backbones and Detection Transformer (DETR) decoders achieve strong 3D perception but incur quadratic costs over tokens and queries, even though urban scenes are dominated by background (sky, road, buildings) and agents that are inconsequential for motion planning. Uniform computation is thus wasteful, treating all tokens and candidate objects as equally important and misaligning perception with the downstream prediction and planning.

Prior efficiency work focuses on one modality in isolation. ViT sparsity methods prune or merge *image tokens* for 2D tasks, while DETR variants suppress *encoder tokens* or *decoder queries* for 2D detection. For multi-view 3D detection, ToC3D compresses tokens using historical queries. None of these methods provides end-to-end sparsity over both 2D tokens and 3D queries or accounts for planner relevance, and benchmarks such as nuScenes weight all annotated agents equally, so errors on distant or non-interacting actors can dominate the metrics, and there is no way to focus evaluation on the most relevant agents.

We introduce SToRe3D, a *planner-aligned* sparsity framework that scores and routes both image tokens and 3D object queries with lightweight 2D--3D relevance heads. Existing transformer sparsity methods act only on *image tokens* in 2D ViT backbones or on *object queries* in DETR-style decoders, and do not jointly sparsify 2D tokens and 3D queries in a planner-aligned way. In contrast, SToRe3D learns a unified relevance function supervised by a planner-inspired future interaction corridor, routes high-relevance queries to deeper layers, and stores lower-relevance queries in feature buffers for selective reactivation. Relative to token compression approaches, this store--reactivate design avoids merge--unmerge overhead, works on the *first frame*, reduces both $\mathcal{O}{(N^{2})}$ backbone and decoder attention, and maintains accuracy under more aggressive sparsity budgets than previous methods.

Our contributions are: (i) Unified end-to-end sparsity that *jointly* prunes tokens and queries within a single architecture. (ii) Planning-aligned relevance supervised by *future interaction corridors* capturing short-horizon ego--agent proximity, aligning perception budgets with planning. (iii) Real-time ViTs at scale via store--reactivate buffers that preserve recoverability under aggressive sparsity, enabling further latency reduction. (iv) nuScenes-Relevance (nuScenes-R), a relevance-aware evaluation protocol on nuScenes that measures accuracy specifically on planning-critical agents defined by future interaction corridors. SToRe3D reduces latency by up to $3 \times$ with marginal accuracy loss, enabling real-time ViT-based multi-view 3D detection.

Figure 1: SToRe3D routes computation via relevance: tokens and queries above stage-wise thresholds are processed further, while the rest are stored for reactivation. The BEV plots and camera images show how queries are reduced across stages based on their relevance scores.

## Related Work

### Efficient multi-view 3D object detection

Early camera-only 3D detectors lifted multi-view image features into BEV space before aggregation. Transformer-based methods such as DETR3D, and PETR introduced 3D queries to attend across views, while BEVFormer, Sparse4D, SparseBEV, PointBEV, and StreamPETR further improved efficiency and performance through sparse feature sampling, BEV representations, deformable attention, and temporal aggregation. However, real-time deployment with large ViTs remains challenging. Prior works explore sparsity either in ViT backbones or in DETR-style encoder/decoders, but treat these axes largely in isolation. As summarized in Table 1, SToRe3D is, to our knowledge, the first to provide end-to-end query and key sparsity across both the ViT backbone and DETR3D decoder for multi-view 3D detection.

### ViT token sparsity

Transformer efficiency has been pursued via approximate attention, component pruning, and vision-specific inductive biases. For ViTs, token *pruning* approaches learn saliency to drop patches progressively, *learned tokenization* approaches select informative latent tokens, and *merging/fusion* approaches reduce redundancy by grouping similar tokens. Extensions to dense tasks such as detection exist. However, these methods operate on *image tokens only*, assume 2D salience, and provide no mechanism to coordinate with 3D object queries, which is essential for multi-view 3D detection.

### DETR token sparsity

Efficiency in DETR-style detectors is typically achieved by sparsifying encoder tokens or decoder queries. Deformable DETR replaces global attention with sparse, reference-point sampling. Sparse-DETR, Focus-DETR, IMFA, and Salience-DETR further limit token or query processing through learned salience. DN-/DAB-/DINO-/RT-DETR variants primarily accelerate convergence via query initialization and denoising rather than structural sparsity. For multi-view 3D detection, FocalPETR selects foreground tokens for the decoder with a 2D auxiliary head, while ToC3D compresses backbone tokens using history-driven scores and merge--unmerge routing. These approaches remain largely *token-only*, focusing on the backbone or encoder while leaving decoder query redundancy under-exploited. ToC3D's reliance on temporal priors also limits first-frame efficiency, and its per-block regrouping introduces additional overhead. In contrast, SToRe3D applies *joint* 2D--3D sparsity, works from the first frame, and avoids merge--unmerge complexity via lightweight *store--reactivate* buffers.

Visual Sparsity Approaches

Table 1: Comparison of visual sparsity approaches. QS: query sparsity. KS: key sparsity. In ViTs, QS and KS operate on image tokens. In DETR decoders, QS sparsifies object queries and KS samples encoder image tokens. SToRe3D jointly sparsifies queries and keys in both the ViT backbone and DETR decoder.

### Planning- and safety-critical perception

Beyond efficiency, recent works align perception with downstream decision-making by emphasizing agents that matter most, including risk-object identification, planner-guided attention, and end-to-end perception--prediction--planing frameworks such as ForeSight, UniAD, and SparseDrive. These methods couple perception to planning objectives but lack a scalable *architectural* mechanism for token and query sparsity with ViTs. SToRe3D closes this gap by supervising sparsity with a *future interaction corridor* and evaluating on nuScenes-R.

## Method

SToRe3D applies *joint, hierarchical sparsity* to both image tokens and 3D object queries in a temporal multi-view 3D detector. At each stage, lightweight relevance heads assign each image token and 3D object query a scalar *relevance* score. We consider two ways to define and supervise this relevance: a *planning-aligned* variant $r^{\text{plan}}$, which focuses on objects the ego vehicle may need to react to in the near future (e.g., lead vehicles, crossing pedestrians), and a *detection-aligned* variant $r^{\text{det}}$, which aims to keep all foreground objects while rejecting background clutter. The most relevant tokens and queries are kept active and propagated to deeper layers, while low-relevance embeddings are written to lightweight *storage buffers* instead of being discarded. Buffered embeddings are later *reactivated*, yielding a *store--reactivate* form of sparsity that avoids irreversible pruning.

Figure 2: SToRe3D architecture builds on a ViT backbone and DETR3D-style decoder with relevance heads that score image tokens and 3D queries at each stage, enabling joint sparsity across backbone and decoder.

### Problem Formulation

We consider multi-view 3D detection with $V$ synchronized cameras over a temporal window $\{{t - T},\ldots,t\}$. Each view produces tokens $\mathbf{X}_{t,v}$ from a ViT backbone, concatenated as $\mathbf{X}_{t}$. The backbone interleaves global and windowed attention, and a feature pyramid network (FPN) provides multi-scale features. Detection object queries $\mathbf{Q}_{t}$ are anchored at 3D positions $\mathbf{p} = {(x,y,z)}$, initialized as $\mathbf{q}^{} = {{MLP}{({{PE}{(\mathbf{p})}})}}$, and refined by a multi-scale deformable DETR-style decoder that applies deformable cross-attention over the FPN features.

Following streaming detection and tracking works, top-$K$ queries propagate across frames, maintained in a temporal memory with temporal reference points transformed to the current ego frame. The active query set combines propagated and initialized queries, $N_{d} = {N_{prop} + N_{init}}$. For the first frame, additional initialized queries replace the propagated queries. This yields unified token $\mathbf{X}_{t}$ and query $\mathbf{Q}_{t}$ sets, which serve as input to the sparse relevance module.

### Defining Object Relevance

Intuitively, we call an agent *planning-critical* if the ego vehicle may need to react to it in the near future, for example, if the agent will pass close to any plausible ego trajectory over the next few seconds. We formalize this by defining a *future interaction corridor* in BEV around the ego vehicle's candidate motion and labeling agents that enter this corridor as relevant. Let $\mathcal{B}_{ego}{(\tau)}$ and $\mathcal{B}_{i}{(\tau)}$ denote oriented boxes for ego and agent-$i$ at $t + \tau$. Swept sets over a horizon $H$ are defined by the convex hull of the union of future boxes:

An agent is *relevant* if the closest distance between its swept polygon and the ego swept polygon is within a margin $d_{\min}$:

This polygonal corridor captures translation and orientation over discrete *future* steps for $H = 5$ seconds, and the labels $\{ y_{i}^{rel}\}$ supervise relevance. The same definitions apply to nuScenes-R metrics (Section 4).

### Unified 2D-3D Relevance Prediction

We predict planning-aligned relevance for both modalities using *mutual gating*: queries are scored in the context of tokens and vice versa. Query relevance is supervised by corridor labels, while token relevance is aggregated from query attention. For object query $\mathbf{q}_{j}$, we compute a context vector from deformable cross-attended tokens and optionally an ego embedding $\mathbf{e}_{t}$,

where $\phi$ is a small MLP, $\oplus$ indicates optional concatenation for planning relevance, $\sigma$ is the sigmoid function, and ${CrossAttn}_{\text{def}}$ denotes the same multi-scale deformable cross-attention used in the detection decoder, attending to a sparse set of FPN features around the query reference points. The ego term lets $r^{qry}$ condition relevance on ego--agent motion. Image token relevance $r_{i}^{img}$ aggregates attention from top-$K$ relevant queries:

yielding a query-aware token relevance that emphasizes regions supported by high-relevance 3D queries. The scores $r_{j}^{qry}$ and $r_{i}^{img}$ serve as routing signals for stage-wise sparsification (Section 3.4). We supervise $r^{qry}$ with binary labels $y^{rel}$ from the interaction corridors (Section 3.2).

### Hierarchical Token Storage

Conceptually, we split tokens and queries into two groups at each stage: a small active set that continues through the network, and a temporarily inactive set that is cached in a buffer rather than discarded. Joint sparsity is applied to both the *backbone token stream* and the *query stream* within the backbone and encoder. After each stage $\ell$, we *filter* tokens/queries using the relevance scores from Section 3.3, *store* the remainder in buffers, and later *reintroduce* them at the final layer. For stage-wise filtering and storage, let $N_{\ell}$ and $Q_{\ell}$ be the numbers of tokens and queries at stage $\ell$. We keep fractions ${\rho_{\ell}^{img},\rho_{\ell}^{qry}} \in {(0,1\rbrack}$ via Gumbel-softmax top-$k$, and the filtered items are written to buffers:

The fractions ${\rho_{\ell}^{img},\rho_{\ell}^{qry}} \in {(0,1\rbrack}$ follow a non-increasing *hierarchical schedule* with depth and are regularized toward targets in Section 3.5. Let ${\overline{\mathcal{K}}}_{\ell}^{img}$ and ${\overline{\mathcal{K}}}_{\ell}^{qry}$ be complements of the kept indices. We write filtered features to buffers immediately after filtering and before the next stage:

Training under aggressive sparsity is non-trivial: as the number of active tokens and queries shrinks, the model receives fewer supervised examples per layer, making it harder to learn stable relevance scores and high-quality features. Naively pruning hard from the beginning often leads to collapsed solutions or severe underfitting. To mitigate information loss, we *reactivate* stored image tokens and object queries for the final attention layer of the backbone and decoder using the updated context. We use a two-level storage schedule: (i) *depth-wise* budgets $(\rho_{\ell}^{img},\rho_{\ell}^{qry})$ are non-increasing with $\ell$; (ii) *training-time* pruning is introduced gradually (linear schedule from dense to target budgets) to maintain stability at high sparsity without finetuning. This preserves global context without restoring all pruned items and adds negligible cost.

### Optimization Approach

The overall framework is trained end-to-end with a multi-task objective over detection, relevance, and auxiliary ROI supervision. For detection, we use a combination of focal loss for classification and L1 loss for bounding box regression with Hungarian bipartite matching. Query relevance is trained with a Gaussian focal loss on predicted scores $r^{\text{qry}}$ and binary relevance labels $y^{rel}$. For the planning-aligned variant, we supervise $r^{\text{plan}}$ using labels derived from the future interaction corridor defined in Section 3.2: agents that enter the corridor are labeled relevant, all others irrelevant. For the detection-aligned variant, we instead supervise $r^{\text{det}}$ using standard foreground/background labels from the 3D detection head (e.g., treating queries matched to ground-truth boxes as relevant). To prevent the relevance heads from interfering with feature learning in the main detector, we stop gradients from the relevance heads at the input object queries and image tokens. Therefore, end-to-end gradients to tokens and queries flow only through the detection loss. In addition, an auxiliary loss is used to supervise ROI feature extraction, with classification and regression terms on 2D image-space targets. The joint loss is

where $\lambda_{\text{rel}}$ and $\lambda_{\text{aux}}$ are balancing weights and $\mathcal{L}_{\text{det}}$ includes focal and L1 losses with Hungarian matching. Token relevance is indirectly supervised through cross-attention with the queries. Gumbel-TopK provides differentiable routing, with the pruning budget linearly increased over training iterations from dense (no sparsity) to the target sparsity.

## Benchmarking Relevance

### Why relevance

Conventional detectors expend equal compute on all agents, inflating latency and misaligning perception with planning, even though many urban objects (e.g., parked vehicles, distant pedestrians) are inconsequential for near-term driving. We therefore evaluate perception under a *relevance-driven* lens: prioritize agents that matter for planning. To quantify this, we vary the number of detected agents provided to a fixed pretrained motion-planning network used only for analysis, not during SToRe3D training or inference. Performance saturates with only $10$--$20$ agents (Figure 3), indicating substantial headroom to reduce compute without harming planning.

### Planning-relevant labels

Ground-truth relevance follows the future interaction corridors defined in Section 3.2. For ego and agent-$i$, we construct swept sets $\mathcal{S}_{ego}{(H)}$ and $\mathcal{S}_{i}{(H)}$ over a horizon $H = 5$ seconds and label an agent relevant if the closest distance between the buffered corridors is below a margin $d_{\min}$. We fix a single operating point by choosing $d_{\min}$ as the 10th percentile of ego--agent distances on nuScenes, yielding $d_{\min} \approx 1.2$ m, $\sim$`<!-- -->`{=html}3 relevant agents per frame on average, and at most $\sim$`<!-- -->`{=html}30. Labels are generated using ground truth trajectories, convexifying swept polygons, and applying the buffered-intersection test (Figure 4).

Figure 3: Planner performance vs. retained agents using a fixed pretrained motion-planning network for analysis only. Planning performance saturates with a subset of agents, motivating relevance-based compute allocation.

### Relevance metrics

Standard detection metrics, mean average precision (mAP) and nuScenes detection score (NDS), treat all agents equally, regardless of planning importance. We instead define relevance via a *future interaction corridor*: 5-second swept polygons for ego and each agent. An agent is labeled relevant if the closest distance $d_{C}$ between its corridor and the ego's corridor is below a buffer $d_{RM}$. Empirically, $d_{RM} = 1.2$ m selects $\sim$`<!-- -->`{=html}10% of agents, or about 3 relevant objects per frame on average. This definition underlies our benchmark, nuScenes-R.

Figure 4: Relevant object labeling example geometry.

Figure 5: Latency-accuracy curves for SToRe3D under varying sparsity, compared to alternatives. Each point corresponds to a different keep ratio. Increasing sparsity moves models toward higher FPS with only modest drops in mAP.

We report two variants: *relevant motion* (RM) filtered metrics (NDS-RM), which apply the RM filter as described above, and *relevant area* filtered metrics (mAP-RA, NDS-RA), which use a fixed detection area around the vehicle for evaluation. Because RM relies on privileged future information, detections are matched to RM-filtered ground truth for true positives and false positives, but false negatives are difficult to compute. Together, RM and RA ensure that SToRe3D's relevance-adaptive sparsity is evaluated fairly, measuring whether accuracy is preserved on *planning-critical* agents while enabling substantial efficiency gains.

## Experiments

### Experiment Setup

### Dataset

We evaluate on the nuScenes 3D detection benchmark, which contains 1,000 $\sim$`<!-- -->`{=html}20s scenes at 20 Hz with six surround cameras per sample, calibrated with known intrinsics and extrinsics. Annotations are provided every 0.5 s, yielding 28k/6k/6k samples for train/val/test over ten classes. We report standard nuScenes metrics (mAP, NDS) and relevance-filtered metrics on planning-critical agents using nuScenes-R (Section 4), including Relevant-Area (RA) and Relevant-Motion (RM) variants.

### Implementation Details

We use six synchronized cameras with standard calibration. Unless noted otherwise, SToRe3D is implemented and evaluated with ViT-B and ViT-L backbones initialized from EVA-02. ResNet-50/101 and V2-99 appear only as reproduced baselines reported from prior work. Unless stated otherwise, input resolution is $320 \times 800$; we also report $256 \times 704$, $512 \times 1408$, and $800 \times 1600$ for accuracy--speed trade-offs. The detector follows a DETR-style design with multi-scale features, embedding dimension $D = 256$, and $L = 6$ decoder layers. The baseline uses 644 detection queries and 256 temporal queries (900 total) with four frames of memory. Denoising is applied during training. Models are trained for 24 epochs on 8$\times$A100 GPUs (batch size 16); inference latency is measured at batch size 1 on a single RTX3090. We use AdamW with cosine decay and mixed precision. Relevance heads are two-layer MLPs with GELU and $TopK$ gating that use differentiable Gumbel-softmax. We report three operating points, SToRe3D-1/2, SToRe3D-1/3, and SToRe3D-1/10, corresponding to hierarchical schedules that retain roughly half, one-third, and one-tenth of tokens/queries.

Table 2: Detection performance on nuScenes and nuScenes-R validation set against SOTA methods. Methods are grouped based on comparable latency. Backbone ×W and -S are the image width and sparsity level, respectively. StreamPETR, ToC3D, SparseBEV, Sparse4Dv2, SOLOFusion, BEVFormer, and Sparse4D are as reported.

### Main Results

### Accuracy--efficiency trade-offs

Figure 5 plots the speed---accuracy frontier of SToRe3D across sparsity regimes, alongside StreamPETR. Jointly pruning 2D tokens and 3D queries yields monotonic FPS gains with negligible accuracy loss at low sparsity and only small losses at higher sparsity. Notably, SToRe3D-1/10 enables *real-time* ViT-based multi-view 3D detection, running at $\sim$`<!-- -->`{=html}18 FPS with ViT-B while remaining SOTA among methods at similar latency. Under matched ViT backbone comparisons (Table 2), SToRe3D consistently improves the accuracy--latency trade-off over dense StreamPETR and token-only ToC3D operating points. As the hierarchical keep ratio decreases, inference time drops monotonically while mAP/NDS degrade smoothly, with a clear knee at mid sparsity. Pushing beyond this regime is challenging, since extreme sparsity drastically reduces the number of supervised tokens and queries per batch, SToRe3D's store--reactivate buffers and gradual pruning warm-up are key to maintaining stable training in this high-sparsity setting.

### Comparison to baselines

We compare the detection-aligned SToRe3D variant ($r^{\text{det}}$) to prior multi-view 3D detectors using standard detection metrics, and the planning-aligned variant ($r^{\text{plan}}$) using nuScenes-R. Table 2 shows that SToRe3D is competitive with strong published baselines across a range of latency regimes. The controlled matched-backbone comparisons show that, relative to StreamPETR and ToC3D under the same ViT backbone family, joint token--query sparsity yields a stronger accuracy--latency trade-off than token-only compression.

### Ablation Study

Table 3: Ablation of sparsity approaches at matched total keep ratios (TKR).

On nuScenes-R, where evaluation is restricted to agents within the future interaction corridor (RM) or a fixed area around the ego (RA), SToRe3D retains strong mAP-RA/NDS-RM on planning-critical agents while running faster than dense baselines. For example, SToRe3D-1/10 (ViT-L) achieves 0.521 mAP, 0.607 NDS, 0.478 NDS-RM, and 5.2 FPS, compared to StreamPETR (ViT-L) at 0.521 mAP, 0.608 NDS, 0.463 NDS-RM, and 2.7 FPS. This indicates that SToRe3D's relevance-driven sparsity preserves accuracy where it matters most for safety-critical planning while significantly reducing latency.

### Sparsity approach

Table 3 compares alternative sparsification strategies at matched total keep ratios against our joint token--query sparsity. At $\rho = 0.5$ and $\rho = 0.3$, SToRe3D consistently achieves equal or higher accuracy at similar or lower latency than token-only approaches. The extra speedup is primarily from added query sparsity in the decoder, which ViT image token-only methods cannot realize, while tying token pruning to object queries preserves accuracy under stronger sparsity.

The store--reactivate buffers introduce modest runtime memory overhead while avoiding additional attention or recomputation. For SToRe3D-1/2 with ViT-B, the buffers store 64,200 pruned image/query embeddings (256-dim), adding approximately 20 MB of runtime memory while reducing compute by 397 GFLOPs. This corresponds to a 2.1% memory overhead for a 28% compute reduction.

### Pruning design

Table 4 ablates design choices within SToRe3D. Joint pruning of image tokens *and* object queries (I&O) outperforms pruning either stream alone, reducing latency in both the backbone and decoder. Retaining filtered items in *store* buffers with reactivation is superior to hard *pruning*, indicating that retrieval paths mitigate early pruning errors. Finally, a linear schedule (warming up from dense to target keep ratios) is more stable than flat query-reduced fine-tuning, which often fails to converge at high sparsity due to the reduced learning signal from very few active queries.

Table 4: Ablation of design decisions on nuScenes validation set using ViT-L backbone for the SToRe3D-1/10 variant. I: image tokens. O: object queries.

### Qualitative Results

Figure 6 qualitatively compares SToRe3D to StreamPETR in challenging driving scenarios. SToRe3D suppresses background false positives by pruning low-relevance tokens and preserves detections for agents inside the interaction corridor, reducing critical false negatives and yielding more focused detections on planning-critical agents. Additional qualitative results are provided in the supplementary material.

Figure 6: Visualization of false negatives for the baseline StreamPETR-R50 (top) and SToRe3D-1/10-ViT-B at similar latency (bottom).

## Conclusion

We introduced SToRe3D, a planner-aligned sparsity framework for multi-view 3D detection with ViTs. SToRe3D applies joint, hierarchical pruning to image tokens and 3D queries, replacing hard drops with filter-and-store buffers that allow selective reactivation. Relevance is supervised by a future interaction corridor, and nuScenes-R evaluates accuracy specifically on planning-critical agents. On nuScenes, SToRe3D reduces latency by up to $3 \times$ with marginal accuracy loss; at aggressive sparsity (SToRe3D-1/10) it reaches *real-time* throughput ($\sim$`<!-- -->`{=html}18 FPS with ViT-B) while achieving state-of-the-art performance among methods with similar latency. Since nuScenes-R depends on corridor hyperparameters $(H,d_{\min})$, future work includes tighter coupling of relevance with planning, LiDAR fusion, and closed-loop evaluation.
