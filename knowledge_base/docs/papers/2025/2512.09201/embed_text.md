<!-- arxiv-full-text:v1 {"arxiv_id": "2512.09201", "source": "arxiv-html"} -->

## Introduction

Recent breakthroughs in 3D generation have enabled the creation of high-quality assets from simple prompts. However, while visually impressive, these outputs are often structurally unorganized, posing challenges for downstream applications like animation, rigging, and interactive editing. Primitive-based representations offer a compelling alternative by distilling complex geometry into a compact assembly of interpretable, analytic parts. This approach yields editable assets and aligns with cognitive findings that humans perceive objects as compositions of simpler forms, providing a structured understanding that dense representations lack. The central challenge is converting these unstructured 3D assets into meaningful, primitive-based designs.

Inferring a primitive assembly from a raw 3D shape, however, presents a fundamental trade-off between reconstruction fidelity and program parsimony. Approaches that prioritize high fidelity often yield dense, redundant assemblies of overlapping primitives. Conversely, methods that enforce parsimony may fail to capture fine geometric details or curved structures. Achieving a representation that is simultaneously expressive, compact, and editable remains an open challenge.

This persistent trade-off can be attributed to two factors. First, commonly used primitive families such as cuboids, superquadrics, or ellipsoids may require a large number of instances to model the rich shape variations in 3D assets. Second, the inference procedures themselves have distinct limitations. Methods that first commit to a complete segmentation of the input rely on a fixed partition that may not align with what the primitives can efficiently represent. This makes the process brittle, as any initial segmentation errors propagate directly to the final assembly. On the other hand, optimization-driven approaches that fit a large "soup" of primitives from scratch must navigate a highly non-convex loss landscape.

To address these limitations, we introduce a framework that marries a highly expressive primitive with a robust inference strategy. At the core of our approach is the SuperFrustum, an analytic primitive that fills a key gap in prior work: existing primitive families typically satisfy only one or two of the critical desiderata---expressivity, editability, and optimizability. In contrast, SuperFrustum spans common solids such as cylinders, cones, spheres, and their tapered or bent variants; is compactly parameterized with just 8 parameters; and admits a signed-distance field that is differentiable with respect to all parameters, enabling smooth blending and effective inverse modeling. Intriguingly, its design builds on analytic functions uncovered by the Shadertoy and Demoscene communities in their pursuit of highly expressive analytic forms with minimal description length. We find that, when carefully adapted, these formulations are exceptionally well-suited for inverse modeling.

To achieve parsimonious assemblies, an expressive primitive must be paired with an equally effective inference algorithm. We propose Residual Primitive Fitting (ResFit), an unsupervised procedure that tightly interleaves global shape analysis with local primitive optimization to better navigate the highly non-convex reconstruction loss. Instead of optimizing a large set of primitives jointly from scratch, ResFit first analyzes the input geometry to propose initial structures based on global cues. These primitives are then refined via gradient descent to conform to the local geometry. The resulting assembly is subtracted from the target shape, and the process repeats on the unexplained residual. By alternating between proposing global structure and optimizing local parameters, ResFit allows these two signals to mutually inform each other, producing assemblies that are both compact and high-fidelity.

Our approach sets a new state-of-the-art on diverse 3D benchmarks. It consistently produces higher-fidelity reconstructions---improving IoU by over 9 points---while using nearly half the primitives of prior work, demonstrating a fundamental shift in the fidelity-parsimony frontier. These results are enabled by our two primary contributions: The SuperFrustum: A single compact analytic primitive that spans a wide range of canonical volumetric forms while remaining differentiable and suitable for gradient-based optimization.

Residual Primitive Fitting (ResFit): An unsupervised inference procedure that alternates between global shape analysis and local primitive optimization to produce compact and accurate assemblies.

Beyond reconstruction, we demonstrate how this framework enables downstream applications including the generation of editable assets, the inference of structured CSG programs, and the enrichment of semantic part segmentations. Code will be open-sourced upon acceptance.

## Related Works

Inferring primitive assemblies. Existing approaches fall into three main categories. *Shape-analysis--driven methods* partition a shape into regions using geometric cues---such as curvature, thickness, or convexity---and then fit primitives to these regions. They produce structurally coherent decompositions when the partitions match the primitive family, but are often brittle across diverse shapes and sensitive to tuning. Since the decomposition is fixed and independent of what the primitives can represent, these methods struggle to balance fidelity and compactness. *Optimization-driven methods* directly adjust primitive parameters to minimize reconstruction error for a target shape or its renders. While effective on small assemblies, they often require many primitives for high fidelity, as reconstruction loss tends to dominate disentanglement and parsimony without strong initialization. *Learned methods* predict primitive parameters or part layouts using neural networks. Some methods train the network on supervised data while others formulate unsupervised reconstruction-based objectives to infer the assemblies. Such models achieve high reconstruction accuracy on domains similar to their training data but generalize poorly to novel or complex objects.

Our approach combines the strengths of analysis- and optimization-driven paradigms: rather than committing to a single decomposition or a fixed primitive set, we *interleave* analysis and optimization so that each informs the other. This bidirectional formulation adapts the decomposition to the representational capacity of the primitives, producing assemblies that remain both compact and geometrically faithful.

Primitive representations. Primitive design has progressed from simple analytic forms to more expressive but increasingly complex parameterizations. Early methods used cuboids or cylinders, which are interpretable but limited in expressivity. Superquadrics and algebraic surfaces enlarge the shape space but sacrifice editability and cannot exactly reproduce canonical solids such as cubes or cones---common in manufactured objects. Recent generalized-cylinder--based primitives increase flexibility yet still fall short in reconstruction fidelity. Neural implicit part representations offer high expressivity but are opaque, costly, and difficult to control or reuse.

In parallel, the graphics and demoscene communities have explored unified analytic primitives that morph between basic shapes within a single functional form. These formulations were developed to minimize scene-description size and enable real-time rendering, not for inverse modeling or differentiable fitting. SuperFrustum draws inspiration from this work, extending it to a broader shape space and demonstrating its effectiveness for high-fidelity primitive assembly inference.

## Method

Figure 3: ResFit infers parsimonious assemblies by interleaving shape analysis and primitive optimization. Shape decomposition provides initial primitives, which are refined with decomposition-aware optimization. Residual unexplained volumes are then extracted and seeded with new primitives.

We define the primitive assembly inference task as follows: given a 3D shape $x$, our goal is to infer a primitive assembly $z$ composed of analytic primitives whose execution $E(z)$ reconstructs the input shape. Each program $z$ defines a sequence of primitives $\{f_{\theta_{i}}\}_{i=1}^{|z|}$ combined through compositional operators to yield a closed surface $E(z)$. Following Occam's razor, we seek programs that are both accurate and compact. Formally, we aim to maximize the following objective: where $\mathcal{R}$ measures the reconstruction accuracy between the input shape $x$ and the program execution $E(z)$, $|z|$ denotes the program complexity (or number of primitives in the program), and $\alpha$ controls the trade-off between accuracy and compactness. Maximizing $\mathcal{O}$ thus favors concise programs that explain the geometry with a small set of expressive parts.

We now summarize the components of our method. Section 3.1 introduces ResFit, our iterative fitting procedure. Section 3.2 defines SuperFrustum, the unified analytic primitive used in all assemblies. Section 3.3 describes our MSD-based initialization strategy, and Section 3.4 details the optimization process that balances geometric fidelity with parsimony.

### ResFit: Residual Primitive Fitting

Figure 4: Morphological Shape Decomposition (MSD) iteratively extracts connected regions of similar thickness. Top: successive MSD partitions of a input mesh. Bottom: MSD yields regions that form suitable initialization seeds for SuperFrusta —capturing non-convex structures such as bicycle tires (left), a cat’s curved tail (center), and bowl rims (right). In contrast, CoACD over-partitions these regions into many convex fragments, often using axis-aligned cuts that produce semantically misaligned parts.

Purely optimization-based methods often produce entangled reconstructions, while analysis-based approaches partition shapes without considering the primitive family's representational capacity. This creates a disconnect between the geometric analysis (top-down) and the primitive representation (bottom-up). Residual Primitive Fitting (ResFit) bridges this divide by interleaving shape analysis and assembly optimization, allowing each phase to inform the other and yielding assemblies that are both compact and geometrically faithful.

Our procedure alternates between analysis and optimization (Fig. 3). The analysis stage decomposes the current residual volume into regions that seed new primitives. The optimization stage then adjusts parameters to maximize $\mathcal{O}$ (Eq. 1), separating explained geometry from remaining residuals. This cycle repeats until $\mathcal{O}$ saturates or a fixed iteration budget $K$ is reached.

Several design choices ensure that the iterative loop can correct both over- and under-parameterization. To prevent over-parameterization, we seed few primitives per round and employ parsimony-aware optimization: a soft regularizer penalizes redundancy during fitting, while hard pruning removes parts that degrade $\mathcal{O}$. To address under-parameterization, primitives are optimized based on their local support, and the full assembly is re-optimized in each round. This enables self-correction as new parts are added, allowing the system to converge toward a compact and coherent structure.

### Expressive, Editable & Optimizable Primitive

An ideal primitive for inverse graphics must be *expressive* enough for diverse forms, *editable* via intuitive controls, and robustly *optimizable*. As existing families often fall short, we introduce SuperFrusta, a unified analytic primitive designed to meet all three desiderata.

A SuperFrustum is the zero-level set of a signed distance function with parameters $\theta=(\mathbf{s},r,d,t,b,o)$. These 8 scalars intuitively control anisotropic scale ($\mathbf{s}$), profile rounding ($r$), dilation ($d$), taper ($t$), bulge ($b$), and onion/shell thickness ($o$), as shown in Fig. 2 (further implementation details and the reference code are provided in the supplementary). Its continuous, piecewise-$C^{1}$ formulation spans a wide range of shapes including cuboids, cylinders, cones, and tori, and is differentiable almost everywhere, enabling stable gradient-based fitting.

The complete primitive assembly $z=E(z)$ is formed by composing transformed SuperFrusta. Each instance $i$ has a pose $(R_{i},t_{i})$ and shape parameters $\theta_{i}$, yielding a signed distance $g_{i}(\mathbf{p})=f(R_{i}^{\top}(\mathbf{p}-t_{i});\theta_{i})$. The final implicit field $\mathcal{F}$ is obtained by recursively applying a smooth union operator $U$: | | $\displaystyle\mathcal{F}_{1}(\mathbf{p})$ | $\displaystyle=g_{1}(\mathbf{p}),$ | | \(4\) | | | $\displaystyle\mathcal{F}_{k+1}(\mathbf{p})$ | $\displaystyle=U\!\big(\mathcal{F}_{k}(\mathbf{p}),\,g_{k+1}(\mathbf{p});\,\beta_{k}\big),$ | | | where $\beta_{k}$ controls blend sharpness. The final surface is the zero level set of $\mathcal{F}$.

### Shape Decomposition for SuperFrusta

ResFit initializes primitives from the volumetric regions produced by a shape decomposition method, and its performance improves when the chosen decomposition strategy aligns with the primitive family's expressiveness. While recent work adapt Approximate Convex Decomposition (ACD) for initializing primitives, we find an adapted variant of Morphological Shape Decomposition (MSD) is more suitable for initializing SuperFrusta.

MSD is an iterative "peel the thickest part first" technique. At each step, it finds the largest connected region of roughly uniform thickness, extracts it, removes it from the shape, and repeats on the residual. This process yields a thickness-ordered set of volumetric regions for primitive initialization, as shown in Figure 4.

Formally, given a signed distance field $f(\mathbf{p})$, each iteration $k$ identifies the thickest interior region $\Gamma_{k}$ by finding the connected component (cc) that survives erosion up to a radius $|\tau|$: The threshold $\tau\leq 0$ is the minimum value such that $\mathrm{Vol}(\Gamma_{k})$ meets a volume fraction $\kappa$. To recover its full spatial extent, we dilate $\Gamma_{k}$ back by the same radius, $R_{k}=\Gamma_{k}\oplus B_{|\tau|}$. This part $R_{k}$ is recorded and subtracted from the shape by updating the residual field: Repeating this process produces a sequence of candidate regions $\{R_{k}\}$ ordered by decreasing thickness.

MSD offers two key advantages over ACD for this task. First, ACD's convexity constraint over-partitions non-convex structures that a single SuperFrustum can model, such as the bent and hollow forms shown in Figure 4 (bottom). Second, MSD is substantially more robust to the noisy surface artifacts present in the residual volumes generated during our iterative fitting loop, making it better suited for ResFit.

For each decomposed part volume, we instantiate a SuperFrustum. We initialize its parameters by using PCA on points sampled within the volume. Cylindricity score along the different PCA axis is used to select a canonical direction. Pose $(R,t)$ and Scale is then inferred w.r.t the canonical axis. Refer to the supplementary for further details.

### Decomposition-Aware Optimization

We optimize the assembly parameters to maximize the objective $\mathcal{O}$ (Eq. 1) in two stages. First, a differentiable phase minimizes a corresponding loss via gradient descent. Second, a discrete pruning phase removes primitives that degrade $\mathcal{O}$. The differentiable loss comprises three components addressing reconstruction fidelity, program parsimony, and program quality.

Reconstruction. The reconstruction loss is a differentiable surrogate for $\mathcal{R}$ in Eq. 2. We supervise the predicted occupancy field $\hat{o}(\mathbf{p})=\sigma(-\beta\,\mathcal{F}(\mathbf{p}))$ of the current assembly against the ground-truth occupancy $o(\mathbf{p})$. Samples $\mathbf{p}$ are drawn uniformly from the shape's volume and densely near its surface. To better reconstruct thin, high-curvature structures, each point is weighted by the principal curvature $\kappa(\mathbf{p})$ of the target mesh. The loss is evaluated only within a spatial mask $\mathcal{M}=\{\mathbf{p}\mid\mathcal{F}(\mathbf{p})<\tau\}$ to focus optimization on signals from the assembly's vicinity.

| | $\displaystyle w(\mathbf{p})$ | $\displaystyle=1+\sigma(\kappa(\mathbf{p})),$ | | \(7\) | | | $\displaystyle\mathcal{L}_{\text{rec}}$ | $\displaystyle=\frac{1}{|\mathcal{M}|}\sum_{\mathbf{p}\in\mathcal{M}}w(\mathbf{p})\big(\hat{o}(\mathbf{p})-o(\mathbf{p})\big)^{2}.$ | | | Parsimony. To encourage compact assemblies, each primitive $i$ is assigned a stochastic existence variable $q_{i}\in$ sampled via a Gumbel-Softmax distribution. Its signed distance field is then modulated as $f_{i}^{*}(\mathbf{p})=q_{i}\,f_{i}(\mathbf{p})+(1-q_{i}),$ which smoothly erodes primitives with low existence probability. The parsimony loss penalizes the expected number of active primitives: $\mathcal{L}_{\text{count}}=\sum_{i}q_{i}.$ Quality. To improve editability and prevent geometrically entangled or overly blended assemblies, we add a structural regularizer that combines overlap and smooth-union consistency losses: where $\hat{o}_{i}$ is the occupancy of primitive $i$. The $\mathcal{L}_{\text{overlap}}$ term penalizes regions where multiple primitives are simultaneously active, discouraging redundant coverage. The $\mathcal{L}_{\text{union}}$ term penalizes regions that are occupied by the smooth union assembly but not by any of the independent primitives, discouraging excessive blending.

The total differentiable loss is the weighted sum of these components: Pruning. After the differentiable optimization converges, a discrete pruning step further simplifies the assembly. Primitives with negligible volume or contribution are tested for removal, and deletions are greedily accepted if they improve the primary objective $\mathcal{O}$.

## Experiments

#Prims (↓)

Table 1: Evaluation on 3DGen-Prim and Toys4K datasets. Our method achieves the best reconstruction and program quality scores simultaneously—improving IOU by 6–9 points while using roughly half as many primitives. Gold = best, Silver = second best.

Datasets. We evaluate on two datasets capturing generated and real-world assets. As the *3DGen-Prim* dataset is not public, we recreate it using 510 prompts from 3DGen-Bench with the Hunyuan3D-2.1 generator. Our second dataset contains 500 geometrically diverse shapes from Toys4K, selected via farthest-point sampling.

Metrics. We evaluate *reconstruction accuracy* and *program quality*. For accuracy, we use standard metrics: voxel IoU ($128^{3}$), Chamfer Distance (CD), and Earth Mover's Distance (EMD) over 2048 randomly sampled surface points. We also report a *Bidirectional Surface IoU (BiSurfIoU)* to better capture surface fidelity, computed as the mean of IoU scores from near-surface points sampled on both the target and reconstructed shapes, with the latter surface extracted via dual contouring of the SDF. For program quality, we introduce four metrics. Program length ($|z|$) and *Overlap Ratio* (the volumetric percentage of the shape covered by multiple primitives) measure parsimony and redundancy. To quantify semantic coherence, we use two metrics based on PartField features. After associating surface points on the target mesh to their nearest primitive, we compute: *IntraPrim*, the mean feature variance within each primitive (lower is better), and *InterPrim*, the average nearest-neighbor distance between primitive feature centroids (higher is better). These scores are aggregated using a size-weighted average.

Baselines. We compare our method against two state-of-the-art approaches. *Primitive Anything (PA)* is a learning-based method trained on a large dataset of manually annotated shapes to predict assemblies of cuboids, cylinders, and ellipsoids from point cloud inputs. Following the original work, we also report its test-time optimization variant, *PA (TTO)*, which refines its predictions using Chamfer Distance. *Marching Primitives (MPS)* serves as a strong optimization-based baseline that directly optimizes a superquadric-based assembly from an SDF grid to achieve state-of-the-art reconstruction fidelity. We run MPS at 128 voxel resolution to match our input. We omit comparisons to methods outperformed by MPS or those without public code.

Implementation Details. All experiments use a fixed set of hyperparameters unless stated otherwise. ResFit runs for a maximum of 10 fitting rounds or until convergence, with each round applying 7 iterations of MSD. The high-level objective $\mathcal{O}$ (Eq. 1) combines curvature-weighted surface IoU with a program-length penalty ($\alpha=10^{-3}$). During optimization, the loss weights are set to $\lambda_{\text{count}}=10^{-3}$ and $\lambda_{\text{qual}}=10^{-2}$ (Eq. 8). Additional optimization details and ablations are provided in the supplementary material.

### Parsimonious High fidelity Assemblies

Table 1 summarizes the reconstruction and program quality metrics on both datasets. Across all reconstruction measures, our method improves IoU scores by $+6.1$ points on 3DGen-Prim and $+9.3$ points on Toys4K over prior work. We attribute this performance to the expressivity of the SuperFrustum primitive and the iterative analysis-optimization loop of ResFit.

These reconstruction gains are accompanied by improved program quality. Our assemblies use approximately half as many primitives as Marching Primitives while reducing volumetric overlap by over $3\times$. The inferred primitives also demonstrate high semantic coherence: our method achieves the lowest *IntraPrim* scores, indicating high semantic purity within primitives, and among the highest *InterPrim* scores, reflecting meaningful distinctions between parts. These results demonstrate that ResFit produces assemblies that are simultaneously more accurate, compact, and semantically interpretable.

Qualitative comparisons in Figure 5 corroborate these findings. Our assemblies exhibit higher geometric fidelity and are more interpretable, using a compact set of non-overlapping, semantically aligned primitives. In contrast, baseline reconstructions can show lower fidelity on complex structures and tend to produce assemblies with greater primitive overlap.

Figure 5: Our method reconstructs target shapes with high geometric fidelity and produces more interpretable assemblies, using compact, minimally-overlapping primitives. In contrast, Primitive Anything (PA) and Marching Primitives (MPS) often lose fine structure and generate assemblies with substantial primitive overlap.

### Ablative Analysis

Primitive Assembly Design. Table 2 compares different primitive families and composition operators. Our full SuperFrustum formulation achieves the highest reconstruction fidelity. Disabling smooth unions reduces accuracy and increases overlap, as continuous volumes must then be formed by intersecting primitives rather than by smooth blending. Superprimitive, a variant of our primitive without tapering or bending also lowers accuracy, confirming these degrees of freedom are important for capturing curved and non-uniform structures. Substituting our primitive with cuboids or superquadrics (SQs) further degrades performance. SQs are particularly susceptible to poor local minima when their axes misalign with the target geometry---an issue that methods like MPS mitigate via non-differentiable heuristics such as periodic axis-flipping, which are excluded from our controlled comparison.

#Prims

Table 2: Primitive representation ablation: SuperFrustum delivers superior performance over Cuboids, Superquadrics (SQ) and SuperPrimitive(SP) (ref. Section 4.2). Combining SuperFrustum with smooth union further improves performance.

Decomposition and Fitting Strategy. Table 3 compares our iterative ResFit procedure against a single-shot fitting baseline, using both MSD and CoACD for initialization. The single-shot approach optimizes all primitives simultaneously after the initial decomposition. This makes it sensitive to the initial partition, as it has no mechanism to reallocate capacity to unexplained regions, resulting in less accurate and less compact assemblies.

In contrast, ResFit uses multiple refinement rounds to progressively reallocate primitives toward residual errors and prune where unnecessary. This iterative process achieves higher fidelity with fewer primitives and lower overlap. When comparing decomposition strategies, MSD consistently outperforms CoACD. MSD's ability to produce non-convex partitions provides better initializations for our primitives, especially on the curved, hollow, and branching geometries as shown in Figure 4.

#Prims

Table 3: Fitting and decomposition ablation: ResFit, which interleaves analysis and optimization, outperforms a single-shot fitting approach (cf. Section 4.2). Moreover, pairing ResFit with MSD yields better results than using CoACD.

### Timing

On the Toys4K test set, the full ten-round version of ResFit takes 652.6 s per shape on average. However, even a two-round variant offers a strong quality--time trade-off: it runs in 184.1 s while achieving 86.54 IOU with only 15.54 primitives. This matches---and slightly exceeds---the reconstruction accuracy of MPS at $256^{3}$ resolution (86.30 IOU) while using *over $5\times$ fewer* primitives and a comparable runtime (194.6 s). PA (58.3 s) and MPS (37.9 s at $128^{3}$) are faster but produce lower-quality assemblies. We note that ResFit is not yet optimized for speed; dedicated CUDA kernels for SuperFrustum may reduce runtime.

## Applications

Our representation enables several downstream uses that combine visual quality, editability, and analytic structure. We highlight four such applications and provide implementation details in the supplementary.

### Editable and Deployable Asset Generation

Our primitives are simultaneously compact, editable, and capable of high-fidelity reconstruction, allowing them to serve directly as deployable 3D assets. To produce textured assemblies, we associate each primitive with a local 2D spherical texture map that we optimize against the target textured mesh. The resulting textured assemblies can be directly deployed in real-time sphere traced scenes, while remaining editable (see Fig. 6).

Figure 6: Assigning per-primitive spherical 2D textures & optimizing it against a textured mesh, begets Edtiable & Deployable assets.

#Prims

Table 4: CSG inference on the ABC dataset: Our method achieves comparable reconstruction accuracy to CAPRI-Net while using significantly fewer primitives.

### Inferring Canonical CSG Programs

Although our framework is designed for smooth, soft-union assemblies, it can also infer discrete Constructive Solid Geometry (CSG) programs composed of canonical solids. We achieve this by constraining the parameters of SuperFrustum to be a barycentric interpolation of parameters to fetch canonical shapes---cuboid, cylinder, cone, and sphere---within the SuperFrustum formulation. Despite the lack of subtraction as a compositional operator, our primitive space natively contains "subtracted" shapes via the onion operator, which we include in the list of canonical shapes. Fitting under these constraints yields solid CSG programs that remain compact and interpretable. In Table 4, we compare this constrained version of our method, named "solid" to CAPRI-Net on a randomly sampled subset of the ABC dataset containing 100 samples. Our approach achieves nearly the same CSG reconstruction accuracy as CAPRI-Net while using roughly two-third as many primitives. As shown in Fig. 6, our inferred programs produce cleaner, less entangled assemblies---owing to the analytic expressivity of our primitives and the structured refinement in ResFit.

### Image to primitive

Our method can seamlessly be combined with 3D generative models to achieve image to primitive assembly. In Figure 8, we use Hunyuan3D-2.1 with ResFit on samples from the 3DGen-Bench suite.

Figure 7: Our method can infer CSG programs using canonical solids (e.g., cylinders, cuboids; cf. Sec. 5), producing far more parsable and structured trees than CAPRI-Net.

Figure 8: Our method can infer primitive assemblies from images by leveraging Text-2-3D models (Hunyuan3D-2.1 ).

### Semantic Segmentation Enrichment

Manually annotating parts can be quite expensive - as a result datasets often provide coarse grained annotations. ResFit can help to annotate finer parts. In Figure 9, we intersect coarse semantic labels from the PartObjVerse dataset with our primitive assemblies to enhance segmentation granularity. As a result, we subdivide large parts into functionally meaningful subcomponents without drifting outside their semantic boundaries. This suggests a promising direction for integrating analytic decomposition as a prior for open-world part segmentation tasks.

## Conclusion

We introduced a framework for converting 3D shapes into compact and editable assemblies of analytic primitives. Our method combines two contributions: SuperFrustum, an expressive, compact, and optimizable analytic primitive; and Residual Primitive Fitting, an iterative inference algorithm that couples shape analysis with primitive optimization to recover parsimonious yet accurate assemblies. Together, they shift the reconstruction--parsimony Pareto frontier, achieving state-of-the-art performance across benchmarks while producing high-fidelity, editable shape programs. Despite its expressiveness, ResFit is still restricted by its purely additive composition; shapes requiring subtractive operations remain challenging. Future work includes extending our decomposition strategies (e.g., tree-of-shapes) and developing richer applications in CSG modeling, interactive editing, and structured scene understanding.

Figure 9: ResFit enables finer, semantically consistent part segmentation. Row 1 shows the coarse semantic regions provided in PartObjVerse. Row 2 shows the primitive assemblies inferred by ResFit. Intersecting each coarse region with its corresponding assembly (Row 3) yields meaningful sub-parts—capturing functional structure while remaining strictly within the original semantic boundaries.
