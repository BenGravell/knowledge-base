<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Forcing: Structure-First Generation with Controllable Semantic Trajectories

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Diffusion and flow-based generative models produce strong images, yet their controllability remains largely endpoint-centric: users specify conditions and receive final outputs, while the intermediate generative dynamics remain hidden. Recent methods have begun to exploit generation order and process decomposition to improve sample quality, but still treat intermediate states as internal computation rather than objects for interaction. We propose Trajectory Forcing (TF), a trajectory-centric framework that makes the generation path explicit, semantic, and editable. TF organizes synthesis as a sequence of semantically structured stages, progressing from global layout to object-, part-, and detail-level representations. Each stage produces a decodable latent state that can be inspected, evaluated, and locally edited before the next stage begins. To instantiate this path, we derive coarse-to-fine teacher hierarchies by clustering pretrained visual representations such as DINOv2, and train a hierarchy-conditioned one-step flow-matching model at each level. We further introduce trajectory-aware metrics that measure structural consistency and local controllability beyond endpoint quality metrics such as FID.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiments show that TF achieves competitive sample quality while exposing coherent intermediate states and supporting localized edits across semantic levels. By shifting the focus from final images to the generative path itself, TF opens a route toward controllable, trajectory-aware image synthesis.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

*To control generation, we must expose not only its destination, but also its path.* Modern image generators typically cast synthesis as a direct mapping from noise to a finished image. Although denoising traverses intermediate states, these states are not deliberately structured for human understanding or intervention; they are computational by-products discarded after the final output is produced. This contrasts with human visual creation, which is inherently coarse-to-fine: global composition is established before local details are refined, and each intermediate stage can be inspected and revised. We take this contrast as our starting point and ask whether generative trajectories themselves can be made interpretable, semantically structured, and editable.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works have begun to exploit trajectory structure in generation, showing that generation order and process decomposition can substantially affect output quality. However, these trajectories remain optimized for the final image: intermediate states are used as computational scratchpads, frequency components, or token-completion steps, rather than as semantic objects a user can inspect, compare, and redirect.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We therefore propose Trajectory Forcing (TF), a framework that organizes image synthesis as a sequence of semantically structured stages. Each stage produces an interpretable latent state that can be decoded, evaluated, and edited before the next stage begins. Rather than collapsing generation into a single opaque mapping from noise to image, TF exposes a coarse-to-fine hierarchy from global layout, through object-level structure, to fine-grained detail, making every intermediate level visually meaningful and amenable to controlled intervention.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Making this hierarchy operational requires a representation space whose geometry organizes semantic structure. Raw pixels entangle appearance, layout, and identity, whereas pretrained visual representations provide a more suitable substrate. Following the *representation alignment hypothesis*, we operate in DINOv2 feature space, where hierarchical clustering over latent tokens empirically recovers object-part-subpart decompositions (Sec. 4.1) that supervise our trajectory design.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural concern with multi-stage generation is inference cost: progressive formulations typically require network function evaluations (NFE) that scale as $L\times T$, where $L$ is the number of structural stages and $T$ the number of denoising steps per stage. TF addresses this by integrating one-step flow matching at each stage. Instead of iterative denoising at every level, each stage uses a single function evaluation to map noise to the current-level target, conditioned on the previous stage. This reduces inference to $L$-NFE, making TF comparable to modern few-step generators while preserving trajectory-level controllability.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are as follows: We propose Trajectory Forcing (TF), a generation framework that models image synthesis as a structured coarse-to-fine trajectory of interpretable semantic stages, enabling inspection and editing at every level.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a hierarchy-conditioned one-step flow formulation that extends one-step generation to multi-level trajectories via level-wise conditioning and structural consistency supervision.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design trajectory-aware metrics that go beyond FID to measure structural consistency and local controllability across generation levels.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate TF on class-conditional ImageNet generation, achieving competitive image quality and fast FID convergence while enabling interpretable multi-level trajectories and interactive editing.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Diffusion and Flow-Based Generation", "weight": 1.0} -->

Latent-space models. Latent Diffusion Models established the paradigm of performing generative dynamics in a compressed latent space, decoupling representation learning from the denoising process. Subsequent work scales the backbone with Transformers or revisits the representation interface through alternative autoencoding schemes.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diffusion and Flow-Based Generation", "weight": 1.0} -->

Pixel-space models. A parallel line of work revisits pixel-space generation, removing reliance on pretrained tokenizers. Recent approaches include flow-based pixel modeling, neural-field diffusion, and end-to-end training with self-supervised pretraining. JiT shows that direct clean-image prediction enables diffusion in high-dimensional pixel spaces, establishing a strong pixel-space baseline. While these works show that compression-based latents are not strictly necessary, our use of a representation space is motivated by semantic structure rather than compression: pretrained features support both hierarchy construction and visual decodability of intermediate states.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Diffusion and Flow-Based Generation", "weight": 1.0} -->

One and few-step models. Reducing inference cost is a major research direction. Distillation-based methods compress multi-step models. Consistency models learn to map arbitrary intermediate states to the ODE endpoint, with trajectory-aware extensions. More recently, shortcut parameterizations and reparameterized matching objectives, including Mean Flows and drifting-based formulations, enable one-step or few-step generation. Our work inherits the mean-flow framework and extends it with hierarchical conditioning and structural supervision.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Generation Ordering and Trajectory Design", "weight": 1.0} -->

The ordering of generation has recently emerged as an important design axis for controlling how information is revealed during synthesis.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Generation Ordering and Trajectory Design", "weight": 1.0} -->

Per-token noise scheduling. Diffusion Forcing assigns independent noise levels to individual tokens, enabling flexible generation orderings in sequential data. This idea is theoretically grounded: different conditioning orders can lead to exponential differences in the learnability of data distributions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Generation Ordering and Trajectory Design", "weight": 1.0} -->

Frequency-domain reordering. DeCo factorizes pixel diffusion along frequency components, using a lightweight decoder for high-frequency details while the main DiT specializes in low-frequency semantics. This decoupling improves both training efficiency and generation quality for pixel-space models.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Generation Ordering and Trajectory Design", "weight": 1.0} -->

Latent-pixel reordering. Latent Forcing jointly diffuses self-supervised latent features and pixels with separate time schedules. By revealing latent structure before pixel detail, it achieves the convergence benefits of latent diffusion while remaining end-to-end in pixel space. The generated latent features serve as a computational scratchpad and are discarded after generation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Generation Ordering and Trajectory Design", "weight": 1.0} -->

All of these methods use trajectory structure to improve *generation quality*, while intermediate states remain either implicit or disposable. In contrast, our work treats the structured trajectory as a user-facing interface: intermediate stages are designed to be semantically interpretable, decodable, and editable, enabling trajectory-level control that goes beyond endpoint optimization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Progressive and Hierarchical Generation", "weight": 1.0} -->

Autoregressive and masked models. Token-based approaches generate images by predicting discrete tokens or masked subsets, sometimes combined with diffusion-based training. These naturally expose partial intermediate samples, but progression is defined over token completion rather than continuous semantic refinement.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Progressive and Hierarchical Generation", "weight": 1.0} -->

Scale-level progression. Visual Autoregressive Modeling (VAR) and FlowAR organize generation along spatial resolution, predicting coarse structures first and refining at higher resolutions. Our hierarchy is orthogonal: levels correspond to semantic granularity (object, part, subpart) at a fixed spatial resolution, rather than resolution upscaling.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Progressive and Hierarchical Generation", "weight": 1.0} -->

Granularity-level progression. Explicit semantic or object-level structure has been used to organize visual scenes in related settings. Most closely related to our hierarchical design, Next Visual Granularity (NVG) decomposes images into granularity levels by bottom-up clustering in VQ-VAE latent space, and autoregressively predicts structure maps and tokens at each level. While NVG demonstrates the value of explicit structure control, its hierarchy is constrained by greedy binary L2 merging ($k=2$) in VQ-VAE space, whose limited semantic geometry makes meaningful groupings, such as object-part-subpart, difficult. Consequently, its stages are tied to latent resolution (e.g., $\log_{2}(16{\times}16)=8$), its intermediates lack clear semantic abstractions (Fig. 2), and its discrete codebook limits intermediate-state flexibility and continuity.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Progressive and Hierarchical Generation", "weight": 1.0} -->

Our approach shares NVG's goal of making structure explicit in generation, but differs in substrate, dynamics, and interface: we build semantically grounded hierarchies by clustering geometrically regular pretrained representations (e.g., DINOv2 ), use one-step flow matching per level for $L$-NFE inference instead of $L{\times}T$, and keep all intermediate states continuously decodable and editable for interactive trajectory-level control.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Representation-Space Generation", "weight": 1.0} -->

Recent work has shown that pretrained visual representations can improve generative modeling. REPA aligns intermediate diffusion features with DINOv2 latents via an auxiliary loss, accelerating convergence. Representation Autoencoders (RAE) further train decoders to reconstruct images from DINOv2 features, enabling generation in a semantically structured and visually decodable representation space. This provides the two ingredients our framework relies: a geometry suitable for coarse-to-fine hierarchies, and a decoder that makes each intermediate level both semantic and visually interpretable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

We briefly review the progression from flow matching to one-step mean-flow generators, culminating in the backbone we build upon.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

Flow Matching. Flow Matching learns a velocity field that transports between a prior distribution and the data distribution. Given data $\mathbf{x}\sim p_{\text{data}}$ and noise $\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$, a flow path is defined by the linear interpolation with $t\in$. The conditional velocity is $\mathbf{v}=\boldsymbol{\epsilon}-\mathbf{x}$, and a network $\mathbf{v}_{\theta}$ is trained by minimizing $\mathcal{L}_{\text{FM}}=\mathbb{E}_{t,\mathbf{x},\boldsymbol{\epsilon}}\|\mathbf{v}_{\theta}(\mathbf{z}_{t},t)-\mathbf{v}\|^{2}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

Samples are generated by solving the ODE $\tfrac{d}{dt}\mathbf{z}_{t}=\mathbf{v}_{\theta}(\mathbf{z}_{t},t)$ from $t{=}1$ (noise) to $t{=}0$ (data), typically requiring many network evaluations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

Mean Flows. MeanFlow (MF) enables one-step generation by modeling an *average velocity* field. Viewing Flow Matching's $\mathbf{v}(\mathbf{z}_{t},t)$ as the *instantaneous* velocity, MF defines the average velocity over an interval $[r,t]$ as: Since directly evaluating this integral during training is intractable, MF differentiates both sides with respect to $t$ to derive the *MeanFlow Identity*: where the total derivative $\tfrac{d}{dt}\mathbf{u}$ is computed via a Jacobian-vector product (JVP). A network $\mathbf{u}_{\theta}(\mathbf{z}_{t},r,t)$ is trained to satisfy this identity using the conditional velocity $\mathbf{v}(\mathbf{z}_{t},t)$ as ground-truth signal and a stop-gradient on the JVP term, denoted $\mathrm{JVP}_{\text{sg}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

Improved MeanFlow (iMF) reformulates the objective as a $\mathbf{v}$-loss re-parameterized through $\mathbf{u}_{\theta}$, constructing a *compound* prediction $\mathbf{V}_{\theta}=\mathbf{u}_{\theta}+(t{-}r)\cdot\mathrm{JVP}_{\text{sg}}$ that is regressed against a *guided velocity* $\mathbf{v}_{g}$. This resolves a variance amplification issue in the original JVP computation. Furthermore, iMF incorporates classifier-free guidance (CFG) directly into training by constructing the guided velocity as: where $\omega$ is a guidance scale sampled at training time and provided to the network $\mathbf{u}_{\theta}$ alongside the class label $y$ and time interval $[r,t]$ as global conditioning. This enables flexible adjustment of the guidance strength at inference without retraining.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

We collectively denote these *standard* conditions (class label, $[r,t]$, and $\omega$) as $\mathbf{c}$ hereafter, distinguishing them from the hierarchy-specific conditions introduced in Sec. 4.2. $\mathbf{x}$-prediction. Orthogonal to the training objective, the choice of prediction target also matters. Pixel MeanFlow (pMF) introduces a denoised-image field $\hat{\mathbf{x}}(\mathbf{z}_{t},r,t)\triangleq\mathbf{z}_{t}-t\cdot\mathbf{u}(\mathbf{z}_{t},r,t)$ and lets the network directly predict the denoised data $\hat{\mathbf{x}}$. The average velocity is recovered via $\mathbf{u}_{\theta}=\tfrac{1}{t}(\mathbf{z}_{t}-\hat{\mathbf{x}}_{\theta})$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Flow Matching and Mean Flows", "weight": 1.0} -->

This parameterization is motivated by the manifold hypothesis adopted from JiT: the denoised output $\hat{\mathbf{x}}$ lies approximately on a low-dimensional data manifold, making it a more tractable regression target than the noisy velocity field. This assumption extends naturally to our setting, where $\hat{\mathbf{x}}$ corresponds to DINOv2 features on a structured representation manifold. We therefore adopt $\mathbf{x}$-prediction combined with $\mathbf{v}$-loss objective as our generative backbone and extend it with hierarchical conditioning in Sec. 4.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Representation Autoencoders", "weight": 1.0} -->

Our framework operates in the feature space of a pretrained visual understanding encoder DINOv2. This choice is motivated by two properties. First, the *representation alignment hypothesis* posits that such feature spaces are geometrically well-organized: semantic factors of variation (e.g., object identity, part structure, spatial layout) are well-separated, so that simple unsupervised clustering over DINOv2 tokens reliably recovers object-part-subpart decompositions without any supervised annotations. We leverage this directly to construct the teacher hierarchies that guide our trajectory design (Sec. 4.1). Second, Representation Autoencoders (RAE) train a decoder that reconstructs images directly from DINOv2 features, making any point in this space visually decodable. Because our generation proceeds as a sequence of intermediate refinements in DINOv2 space, the RAE decoder renders every intermediate level as a visual output, enabling inspection and editing before generating the next stage.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Method", "weight": 1.0} -->

Artistic training and generative modeling. Human visual artists typically adopt a coarse-to-fine workflow, first establishing global structure and dominant color relationships before refining local details, as illustrated in Fig. 3. Across artistic training practices, beginners are repeatedly advised to avoid *chasing details* and instead focus on structural abstraction and global coherence. The recurrence of this principle across instructors and contexts suggests that it reflects a stable cognitive regularity: global organization precedes and constrains local articulation. Motivated by this observation, we incorporate this structural prior into our model design, translating the coarse-to-fine principle into a hierarchical generation framework where global consistency guides detail refinement.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Build Teacher Hierarchy", "weight": 1.0} -->

To enable hierarchical generation with intermediate control, we first construct a semantic hierarchy over latent tokens, which serves as a teacher signal for training. Rather than assuming access to human-annotated part hierarchies, we derive this structure directly from pretrained visual representations, leveraging their inherent semantic organization, as illustrated in Fig. 4(a).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Build Teacher Hierarchy", "weight": 1.0} -->

Given an input image, we extract dense latent features $\mathbf{z}=\{\mathbf{z}_{i}\}_{i=1}^{N}$ with $\mathbf{z}_{i}\in\mathbb{R}^{C}$, where $N{=}H{\times}W$ is the number of spatial tokens. We assign each token a hierarchical cluster index at three granularity levels: object/background, parts, and subparts, via unsupervised clustering, forming a fixed-depth hierarchy shared across all samples.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Build Teacher Hierarchy", "weight": 1.0} -->

\(i\) Object/background: At the coarsest level, we apply K-means with $K{=}2$ in the feature space to obtain two clusters; the cluster whose tokens are on average closer to the image center is designated as object (center prior), and the other as background. This yields a binary partition that serves as the foundation for finer-grained decomposition.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Build Teacher Hierarchy", "weight": 1.0} -->

\(ii\) Part and Subpart: We construct a hierarchy over object tokens only via agglomerative clustering with a combined semantic-spatial distance: where $\mathbf{p}_{i}$ is the normalized spatial coordinate of token $i$ and $\alpha$ controls the spatial regularization strength. This encourages semantically coherent, spatially contiguous clusters. From the resulting dendrogram, we extract a fixed-depth hierarchy by cutting at predefined *distance thresholds*: higher thresholds ($0.65$) yield finer subparts, lower thresholds ($0.35$) produce coarser parts.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Build Teacher Hierarchy", "weight": 1.0} -->

\(iii\) Output Hierarchy: The resulting hierarchy assigns each token a tuple of cluster indices (object/background, part, subpart). These indices are stored as dense maps aligned with the latent grid and serve as region assignments in subsequent stages.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Hierarchy-conditioned Denoising", "weight": 1.0} -->

Given the teacher hierarchies from Sec. 4.1, we train a hierarchy-conditioned one-step flow model that refines latent features across semantic levels, inducing structured and steerable denoising trajectories.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Level Targets", "weight": 1.0} -->

We construct a set of *level canvases* $\{\mathbf{z}^{(l)}\}_{l=0}^{L-1}$ that serve as denoising targets at each granularity. For levels $l=0,\ldots,L{-}2$, each token is replaced by the mean feature of its assigned region: where $R^{(l)}_{i}$ is the region assignment of token $i$ at level $l$. At the finest $l=L{-}1$, the canvas is the original feature: $\mathbf{z}^{(L-1)}=\mathbf{z}$. The resulting canvases progress from coarse, piecewise-constant representations to the full-resolution latent, naturally encoding a semantic trajectory from global structure to fine detail.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Level-wise Conditioning", "weight": 1.0} -->

A single shared network is trained across all hierarchy levels. During training, a level index $l$ is sampled uniformly at random for each batch element. Beyond the standard conditions $\mathbf{c}$, the network receives three hierarchy-specific inputs: the noised current-level canvas $\mathbf{z}^{(l)}(t)=(1{-}t)\,\mathbf{z}^{(l)}+t\,\boldsymbol{\epsilon}$, the previous-level canvas $\mathbf{z}^{(l-1)}$ as a spatial condition, and the level index $l$ as a global condition. For level $l{=}0$, the conditioning canvas is set to zero, making the coarsest level unconditional (aside from $\mathbf{c}$).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Level-wise Conditioning", "weight": 1.0} -->

A natural way to supply the previous-level canvas is *in-context conditioning*: the conditioning tokens are appended to the input token sequence so that the transformer attends over both, but this doubles the sequence length. For efficiency, we instead fuse the two inputs in the channel dimension: the noisy canvas and the previous-level canvas are independently embedded to $D$ dimensions, concatenated to $2D$, and projected back to $D$ via a linear fusion layer, preserving the original sequence length. The level index is encoded through a learned embedding table and injected as additional conditioning tokens alongside class and guidance embeddings.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Total Training Objective", "weight": 1.0} -->

The compound prediction $\mathbf{V}_{\theta}=\mathbf{u}_{\theta}+(t{-}r)\cdot\mathrm{JVP}_{\mathrm{sg}}$ is constructed and regressed against the guided velocity $\mathbf{v}_{g}$: \(ii\) Structural loss: To encourage the prediction to respect region structure, we penalize the deviation of each predicted token from the ground-truth mean of its assigned region. Let $\boldsymbol{\mu}^{(l)}_{k}$ denote the target region mean as in Eq.. For each token $i$ in region $k$, we compute the squared cosine distance between the predicted token $\hat{\mathbf{x}}_{\theta,i}$ and its region's target mean, averaged over all valid tokens and regions: where $K_{l}$ is the number of valid regions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Total Training Objective", "weight": 1.0} -->

This loss is applied to $l\in\{0,\ldots,L-2\}$ and disabled at the finest level, where no region structure is imposed.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Total Training Objective", "weight": 1.0} -->

Overall objective. The full training loss is: where $\lambda$ controls the structural loss weight.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hierarchical Sampling", "weight": 1.0} -->

At inference, generation proceeds sequentially through the hierarchy from $l=0$ to $L{-}1$. At the coarsest level, the model generates from pure noise with zero spatial conditioning: $\hat{\mathbf{z}}^{}:=\hat{\mathbf{x}}_{\theta}(\boldsymbol{\epsilon},\,l{=}0,\,\mathbf{0};\,\mathbf{c})$. For each subsequent level $l>0$, fresh noise is drawn and the model generates conditioned on the output of the previous level: Each level requires a single network function evaluation (NFE), yielding a total cost of $L$-NFE for the complete hierarchy. Crucially, every intermediate output $\hat{\mathbf{z}}^{(l)}$ is decodable into a visual image via the RAE decoder, providing a meaningful preview at each generation stage.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Interactive Generation and Editing", "weight": 1.0} -->

Because generation is decomposed into discrete, interpretable levels, users can inspect, modify, and re-generate at any point along the trajectory.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Interactive Generation and Editing", "weight": 1.0} -->

Editing workflow. Given a fully generated trajectory $\{\hat{\mathbf{z}}^{(l)}\}_{l=0}^{L-1}$, a user inspects the decoded output at level $l^{*}$ and produces an edited canvas $\tilde{\mathbf{z}}^{(l^{*})}$. Generation then resumes from this edit: levels $l>l^{*}$ are re-generated conditioned on the modified output, while all coarser levels $l<l^{*}$ remain unchanged. This workflow supports two complementary editing operations: \(i\) Feature editing: The user replaces the mean feature of a selected region in $\hat{\mathbf{z}}^{(l^{*})}$ with a feature sourced from another region or image (e.g., swapping one part's semantics with another), then propagates forward through subsequent levels. Because semantically similar content maps to nearby features in DINOv2 space, this transfers the semantic identity of the source region to the target.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Interactive Generation and Editing", "weight": 1.0} -->

\(ii\) Shape editing: The user modifies the spatial extent of a region by reassigning tokens at the boundary between adjacent regions in $\hat{\mathbf{z}}^{(l^{*})}$, then propagates forward. This changes *where* a region is without altering its feature content, for example, enlarging or shrinking a part, or reshaping its contour.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Interactive Generation and Editing", "weight": 1.0} -->

A key property underlying both operations is editing *scope control*. Since generation is Markov (each level conditioned only on the preceding one), an edit at level $l^{*}$ propagates through levels $l>l^{*}$ but leaves coarser levels untouched. This gives users predictable control over editing scope: coarser edits cascade through more stages and have broader semantic impact, while finer edits remain spatially localized. These editing operations motivate the trajectory-aware evaluation metrics introduced in Sec. 5.

<!-- chunk {"id": "body-0052", "role": "body", "section": "ImageNet Experiments", "weight": 1.0} -->

We evaluate on ImageNet at $256{\times}256$ resolution. Following the hierarchical sampling of Sec. 4.3, each image is produced in $L{=}4$ one-step denoising stages in DINOv2 feature space, with every intermediate output decodable via a pre-trained ViT-XL decoder. We report FID and IS on 50k samples.

<!-- chunk {"id": "body-0053", "role": "body", "section": "ImageNet Experiments", "weight": 1.0} -->

Our backbone is a DiT transformer shared across all levels, with patch size $16{\times}16$ (denoted TF/16). By default, we train TF with structural loss weight $\lambda{=}1$ and the Muon optimizer at a constant learning rate of $1e-2$. Implementation details, full hyperparameters, scalability across model sizes, and $\lambda$ ablation are provided in the supplementary material.

<!-- chunk {"id": "body-0054", "role": "body", "section": "ImageNet Experiments", "weight": 1.0} -->

Multi-step pixel diffusion/flow Multi-step latent diffusion/flow Autoregressive latent diffusion/flow 1-NFE diffusion/flow TF-B/16+FD-loss‡ (ours) TF-L/16+FD-loss‡ (ours) TF-H/16+FD-loss‡ (ours) *NVG requires 184 NFEs total; see text Sec. 5.1 for breakdown.

<!-- chunk {"id": "body-0055", "role": "body", "section": "ImageNet Experiments", "weight": 1.0} -->

†Results reported from the original MeanFlow paper (trained from scratch).

<!-- chunk {"id": "body-0056", "role": "body", "section": "ImageNet Experiments", "weight": 1.0} -->

‡Inception-space FD-loss post-training; see text App. 0.A.1 for details.

<!-- chunk {"id": "body-0057", "role": "body", "section": "System-level Comparison", "weight": 1.0} -->

We compare with prior methods in Tab. 1. Since work on hierarchical latent generation is scarce, we include representative pixel-space as well as latent-space baselines, spanning both multi-step and one-step diffusion/flow approaches. Unless otherwise noted, we report results for models trained from scratch.

<!-- chunk {"id": "body-0058", "role": "body", "section": "System-level Comparison", "weight": 1.0} -->

At $80$ training epochs, TF shows rapid convergence relative to baselines that typically require several hundred epochs. We note that these are early-training results; the primary contribution of TF is not FID optimization but trajectory-level controllability, which no other method in the table provides.

<!-- chunk {"id": "body-0059", "role": "body", "section": "System-level Comparison", "weight": 1.0} -->

Relation to prior work. The most related prior work is NVG, which also performs hierarchical generation; we discuss conceptual differences in Sec. 2. From a practical standpoint, two differences are worth highlighting: (i) NVG requires training a custom multi-granularity VQ-VAE to support its resolution-based hierarchy, whereas TF operates directly in pretrained DINOv2 features without a task-specific tokenizer; (ii) NVG's structure generation relies on a multi-step rectified flow model at each stage ($9$ content steps + $7\times 25$ Euler steps = $184$ NFEs); moreover, its discrete nature makes it difficult to leverage recent one-step advances, whereas TF naturally integrates one-step matching and produces each level in a single evaluation ($L{=}4$ NFEs total).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluation beyond FID", "weight": 1.0} -->

Standard metrics such as FID evaluate distributional quality, but do not capture the controllability and structural faithfulness central to TF. To measure these properties, we introduce trajectory-aware metrics along two complementary axes: (i) spatial locality of edits and (ii) structural coherence across levels.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluation beyond FID", "weight": 1.0} -->

(a) Local Invariance Score (LIS) (b) Structural Consistency (PMR) Figure 6: Trajectory-aware evaluation. (a) LIS shows coarser edits propagate more strongly, while finer edits remain localized. (b) Both spatial and feature PMR remain low, indicating hierarchical consistency across levels. We evaluate on TF alone as no baseline produces semantic-region intermediates (NVG uses binary splits over discrete tokens without region structure).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Local Invariance under Manipulation", "weight": 1.0} -->

We evaluate whether editing at level $\ell^{*}$ introduces unintended changes to regions that are not explicitly modified. Let $\hat{\mathbf{z}}^{(\ell)}$ denote the generated latent at level $\ell$ before manipulation and $\hat{\mathbf{z}}^{\prime(\ell)}$ the corresponding latent after re-generation from the edited canvas. Given a spatial mask $\mathbf{M}\in\{0,1\}^{H\times W}$ indicating edited tokens ($M_{ij}{=}1$), we define the Latent Invariance Score (LIS) as the average cosine distance over unedited tokens: where $\Omega_{\text{unedit}}=\{(i,j)\mid M_{ij}{=}0\}$. Lower scores indicate stronger local invariance.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Local Invariance under Manipulation", "weight": 1.0} -->

We evaluate LIS at each downstream level $\ell\geq\ell^{*}$ to study how edits propagate through subsequent generation stages. Fig. 6(a) shows a clear scale-dependent behavior: coarser edits produce larger downstream deviations, whereas finer edits remain more localized. Object/background edits yield the highest LIS at the final level, followed by parts and subparts edits. This confirms that TF exposes a controllable hierarchy where the spatial extent of changes can be modulated by the editing level.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Structural Consistency across Levels", "weight": 1.0} -->

Beyond editing invariance, we evaluate structural coherence between consecutive levels: each child-level region should be spatially contained within a single parent region; a child straddling multiple parents signals structural drift.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Structural Consistency across Levels", "weight": 1.0} -->

Since a child region may partially overlap multiple parent regions near boundaries, we assign each child a parent by spatial majority: This induces a token-level expected parent: every token $n$ in child region $j$ inherits $\mathrm{parent}(j)$ as its expected parent. We define two complementary token-level Parent Misrouting Rates (PMR): \(i\) Spatial PMR. The fraction of tokens whose parent-level cluster assignment disagrees with the majority-voted parent of their child region: where $j_{n}$ denotes the child region containing token $n$. This measures whether child regions are cleanly contained within single parent regions.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Structural Consistency across Levels", "weight": 1.0} -->

\(ii\) Feature PMR. The fraction of tokens whose feature is closer to an incorrect parent center than to the assigned one: This captures whether generation has shifted token features away from their assigned parent's semantic mode.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Structural Consistency across Levels", "weight": 1.0} -->

Lower values indicate stronger structural consistency; both metrics are evaluated at each consecutive level pair. Fig. 6(b) shows that spatial PMR remains near zero across levels, indicating that child regions are largely contained within their parent regions. Feature PMR is slightly higher and increases at deeper levels due to finer semantic partitioning, but remains low overall. These results indicate that TF preserves hierarchical consistency while progressively refining semantic detail.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Structural Consistency across Levels", "weight": 1.0} -->

Edit effectiveness and decoded-space checks. The metrics above verify that edits do not disrupt unedited regions and that generation is structurally coherent. We additionally evaluate whether edits achieve their intended effect in the target region, and verify that latent-level properties translate to pixel space by decoding intermediate outputs via the frozen RAE decoder. Editing examples and decoded-space analysis are provided in the supplementary material.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Structural Consistency across Levels", "weight": 1.0} -->

Why a shared decoder? A natural question is whether a single decoder suffices for all levels, since intermediate canvases differ in distribution from the final latent. We deliberately avoid per-level finetuning for two reasons: first, a shared decoder ensures that decoded images across levels live in a consistent visual space, which is essential for editing: a user must be able to compare the output at level $\ell^{*}$ with the final image; second, no ground-truth intermediate images exist, as level canvases are piecewise-constant abstractions in feature space, making per-level supervision unavailable by construction.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

We presented Trajectory Forcing, an approach that treats the generative trajectory as a first-class, user-facing object rather than a hidden computational process. By operating in a semantically structured representation space and combining hierarchical conditioning with one-step flow matching, TF produces a coarse-to-fine sequence of decodable, editable intermediate states in $L{=}4$ NFE.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

Limitations. Our hierarchy is derived from unsupervised clustering with a fixed depth and a center prior for object/background separation, which may not generalize well to images without a centered dominant object. Because each level is conditioned only on the immediately preceding one, coarser-level information reaches finer levels indirectly through the chain rather than via direct conditioning. Current results are reported at 40/80 training epochs; longer training and scaling analysis are deferred to the supplementary material.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

Future work. Natural extensions include replacing the fixed clustering pipeline with richer hierarchy sources (such as model segmentations ), adaptive hierarchy depth per image, and extending TF to text-conditional generation.
