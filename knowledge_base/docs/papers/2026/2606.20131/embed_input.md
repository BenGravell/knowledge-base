<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TriFlow: Generating Artist-Like 3D Mesh Topology via Nearest-Vertex Vector Fields

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present TriFlow, a new generative approach for producing compact 3D meshes with artist-like triangle topology directly from input geometry conditions such as signed distance fields. Our key insight is to represent mesh topology as a nearest-vertex vector field (NVF) defined over the surface, where each point encodes its association to the nearest triangle vertex in the local barycentric frame. We train a latent flow-matching model to synthesize this field, enabling topology generation conditioned on the input geometry. To extract a coherent mesh, we cluster surface regions using the generated NVF and guide a constrained quadric error metric (QEM) mesh simplification with topology-aware optimization. This yields output meshes that closely match the input geometry while exhibiting structured, artist-like connectivity. Experiments demonstrate that TriFlow achieves stronger generalization and significantly improved topology quality compared to state-of-the-art learning-based approaches, alongside 90% lower Chamfer Distance and an 8x speedup.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Triangle meshes serve as a fundamental representation across computer graphics and vision, broadly used in surface-based modeling, rendering, animation, physical simulation, 3D reconstruction, digital content creation, and beyond. This prevalence stems from their computational efficiency, explicit surface structure, and direct compatibility with existing production tools. Beyond geometric accuracy, the *topology* of a mesh plays a crucial role: the organization of vertices, edges, and faces strongly influences performance and applicability in downstream applications such as deformation, editing, and simulation; poorly organized connectivity often leads to artifacts and costly manual cleanup. In practice, artists construct meshes with carefully designed topology, which we refer to as *artist-like topology*, characterized by compact face count, smooth vertex distribution, and edge alignment with salient geometric features.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works in 3D generative modeling demonstrate impressive advances in geometry creation. However, the discrete nature of the optimized topologies remains difficult to synthesize directly. These approaches produce high-fidelity geometry as implicit fields, requiring methods like Marching Cubes for mesh extraction, resulting in highly over-tessellated output meshes that are ill-suited for downstream workflows (e.g., real-time game rendering). To address this limitation, recent works have explored generating artist-like meshes directly as discrete triangle sequences in an autoregressive manner. While such methods demonstrate promising results, they suffer from slow token-by-token inference and error accumulation during autoregressive prediction, which often leads to incomplete or low-fidelity generations -- limiting their scalability and generalization. A significant gap still exists between high-fidelity 3D geometry modeling and robust, efficient, production-ready mesh topology generation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this, we propose TriFlow, a novel generative approach for creating meshes with artist-like topology. Our key insight is that mesh topology can be represented as a piecewise-continuous field defined over the surface, rather than as discrete connectivity. We thus introduce a nearest-vertex vector field (NVF) that has a bijective mapping to the mesh topology. This representation transforms the task of topology generation into vector-field modeling, thereby avoiding expensive autoregressive sequence modeling. As illustrated in Fig.˜1, given input geometry encoded as a signed distance field (SDF), we predict the NVF and then extract a mesh with topology aligned to the field prediction. Our approach is flexible and can handle any inputs that can be represented as SDFs, such as implicit fields from 3D generative methods, and fused signed distance grids from sensor measurements.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To recover meshes from the generated field, we develop a topology-aware extraction method that first clusters surface regions associated with respective target vertex positions using a watershed algorithm and then performs constrained quadric error metric (QEM) simplification guided by the predicted targets. This formulation not only preserves geometric fidelity but also effectively captures the topological characteristics in our generated NVF. To enhance robustness against noisy or irregular input geometry commonly encountered in scanning and generative modeling, we introduce randomized surface distortions as data augmentation during training.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments demonstrate that TriFlow significantly improves topology generation quality and generalization compared to the state of the art, while achieving more than $8\times$ speedup. By representing topology as a vector field, our method provides a new perspective on mesh generation that bridges geometry modeling and compact typology extraction. To facilitate reproducibility, we release our complete codebase for training and inference.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our contributions are: We introduce a novel representation of mesh topology using a nearest-vertex vector field (NVF) pointing towards the nearest vertex in the local triangle's barycentric frame.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a latent flow-matching approach for topology synthesis conditioned on input SDF geometry. We apply random surface distortion during training to enable the model to generalize to noisy or irregular geometry.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a robust topology-aware mesh extraction approach that combines a watershed algorithm with constrained QEM optimization to produce artist-like mesh outputs from our NVF prediction.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

We introduce a novel generative approach to create compact, artist-like mesh topologies from signed distance field (SDF) inputs. The SDF, denoted as $\mathcal{G}$, is used as the input geometry condition for its flexibility and ease of conversion from other representations. The surface, defined as the zero-level set of the SDF, is represented as $\mathcal{S}\subset\mathbb{R}^{3}$ containing all surface points.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

To efficiently predict the discrete mesh topology, we introduce a nearest-vertex vector field (NVF) to represent mesh connectivity, denoted as $\mathcal{T}=\{\boldsymbol{t}(\boldsymbol{p})\in\mathbb{R}^{3}\mid\forall\boldsymbol{p}\in\mathcal{S}\}$. Our mesh topology generation then follows a two-step pipeline: first generate $\mathcal{T}$ conditioned on $\mathcal{G}$; and then extract mesh $\mathcal{M}$ from the generated $\mathcal{T}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

An overview of our method is illustrated in Fig.˜2. We train a latent flow-matching model to generate the NVF $\mathcal{T}$, conditioned on the SDF latent of the input geometry $\mathcal{G}$. To extract mesh topology, the generated field $\mathcal{T}$ is first clustered via a watershed algorithm to identify regions associated with target mesh vertices. These regions are then used as constraints in the QEM simplification method applied to a proxy mesh representing $\mathcal{G}$ to produce the final output mesh $\mathcal{M}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "3.1", "weight": 1.0} -->

The NVF $\mathcal{T}$ is a vector field defined on the mesh $\mathcal{M}$, as illustrated in Fig.˜3(a). Given any surface point $\boldsymbol{p}\in\mathcal{S}$, the field value $\boldsymbol{t}(\boldsymbol{p})$ is the vector pointing towards the nearest mesh vertex of $\boldsymbol{p}$ in the local triangle's barycentric frame: $\boldsymbol{t}(\boldsymbol{p})=\boldsymbol{v}_{n}-\boldsymbol{p}$, where $\boldsymbol{v}_{n}$ denotes the nearest vertex.

<!-- chunk {"id": "body-0015", "role": "body", "section": "3.1", "weight": 1.0} -->

The nearest vertex index is determined by which assigns $\boldsymbol{p}$ to the vertex with the maximal barycentric weight in the local triangle.

<!-- chunk {"id": "body-0016", "role": "body", "section": "3.1", "weight": 1.0} -->

To enable efficient generative modeling, we discretize the surface $\mathcal{S}$ and the NVF $\mathcal{T}$ into a sparse voxel grid. As shown in Fig.˜3(c), for each voxel intersecting with $\mathcal{S}$, we take the voxel center $\boldsymbol{p}_{c}$ and find its nearest point $\boldsymbol{p}$ on the surface and the triangle $f_{n}$ containing $\boldsymbol{p}$. Then Eq.˜1 is used to determine the nearest vertex $\boldsymbol{v}_{n}$. The voxelized NVF at this voxel is defined as $\boldsymbol{t}_{c}(\boldsymbol{p}_{c})=\boldsymbol{v}_{n}-\boldsymbol{p}_{c}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "3.1", "weight": 1.0} -->

This representation partitions each triangle into three regions corresponding to its incident vertices, implicitly encoding topology. Points mapped to the same triangle vertex form a connected surface region, with region adjacency corresponding to the mesh vertex connectivity, as shown in Fig.˜3(b). Unlike the discrete vertex-face representation $(\mathcal{V},\mathcal{F})$, the NVF is piecewise continuous and suitable for neural modeling.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Latent Flow-Matching Model for NVF", "weight": 1.0} -->

We learn to generate mesh topology by predicting the latent representation of the NVF $\mathcal{T}$, conditioned on the input SDF $\mathcal{G}$. As shown in Fig.˜2, the model takes as input an SDF latent $z_{\text{SDF}}$ representing $\mathcal{G}$, together with user-controlled topology parameters, and generates a latent $z_{\text{NVF}}$ to be decoded into the NVF.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Latent Flow-Matching Model for NVF", "weight": 1.0} -->

SDF Condition Encoding. We voxelize the input SDF $\mathcal{G}$ on a $512^{3}$ grid and discard voxels with unsigned distances greater than $\nicefrac{{1}}{{128}}$ of the maximum extent of its bounding box, resulting in a sparse voxel representation. We train an autoencoder that encodes the SDF grid into a sparse latent grid $z_{\text{SDF}}$ of resolution $64^{3}$. The model is trained with an $\ell_{1}$ reconstruction loss: $\mathcal{L}_{\text{SDF}}=\|\hat{\text{SDF}}-\text{SDF}\|_{1}$. The resulting latent serves as a compact geometric condition for generating mesh topology.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Latent Flow-Matching Model for NVF", "weight": 1.0} -->

NVF Encoding and Decoding. The NVF $\mathcal{T}$ is voxelized at resolution $512^{3}$ and encoded using a variational autoencoder (VAE) into a sparse latent grid $z_{\text{NVF}}$ of size $64^{3}$. We parameterize the field $\mathcal{T}$ using its unit direction $\boldsymbol{d}=\nicefrac{{\mathcal{T}}}{{\|\mathcal{T}\|_{2}}}$ and the square root of its magnitude $s=\sqrt{\|\mathcal{T}\|_{2}}$, which are the direct output of the decoder. This decomposition prioritizes directional consistency in low-magnitude regions near mesh vertices, which is critical for accurate mesh extraction.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Latent Flow-Matching Model for NVF", "weight": 1.0} -->

We train the model using an $\ell_{1}$ loss on the reconstructed direction $\hat{\boldsymbol{d}}$ and scaled magnitude $\hat{s}$, alongside a KL-divergence loss weighted by $\lambda_{KL}$: Latent Flow Matching. Given the SDF latent $z_{\text{SDF}}$ and topology control parameters consisting of the target face count and quad-face ratio, which control the output mesh density and topological regularity, we train a latent flow-matching network to generate the NVF latent $z_{\text{NVF}}$. Training is performed along a linear interpolation path between a ground-truth latent $z_{0}$ and Gaussian noise $\epsilon$, which progressively transforms data samples into noise. The network learns a time-dependent velocity field $u$ that moves samples along this path toward the data distribution. The training follows the conditional flow-matching objective: where $c$ denotes the topology control parameters.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Latent Flow-Matching Model for NVF", "weight": 1.0} -->

The generated latent is finally decoded to obtain the voxelized NVF $\mathcal{T}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

To mitigate clustering ambiguity caused by prediction uncertainty, we first process the predicted NVF to obtain a spatially smooth field, ensuring that surface points are robustly grouped into consistent components. The topology intrinsic to the surface grouping is then transferred to a mesh as output. This process is also constrained by optimization objectives in accordance with QEM for geometry alignment.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

NVF Smoothing and Transfer. Given the voxelized NVF prediction from the flow-matching model, we first apply a bilateral filter to suppress noise in locally smooth regions inferred by the network. We extract an over-tessellated mesh $\mathcal{M}_{d}=(\mathcal{V}_{d},\mathcal{F}_{d})$ from the SDF $\mathcal{G}$ using marching cubes as a proxy whose vertices densely sample the surface of $\mathcal{G}$. We then transfer the voxelized NVF onto the vertices of $\mathcal{M}_{d}$ as follows.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

For each vertex $\boldsymbol{v}_{d}$ in $\mathcal{M}_{d}$, we locate its nearest voxel center $\boldsymbol{p}_{c_{n}}$ and assign an NVF vector according to where $\boldsymbol{t}_{c}(\boldsymbol{p}_{c_{n}})$ denotes the predicted NVF at the voxel center. This assignment ensures that the vector associated with $\boldsymbol{v}_{d}$ points toward the same target position indicated by the corresponding voxel prediction.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

Watershed Algorithm. Ideally, the NVF naturally groups surface points $\mathcal{S}$ into distinct clusters, where points in the same cluster share a common target vertex (Fig.˜3(b)). However, in practice, prediction noise and voxelization artifacts can cause clustering ambiguity. To robustly recover the connected components defined by the NVF prediction, we introduce a watershed algorithm that iteratively expands regions on the surface of $\mathcal{M}_{d}$. The algorithm consists of the following three steps: 1\) Region Root Initialization. Region roots are defined as vertices in $\mathcal{V}_{d}$ with small predicted displacement magnitudes, indicating they are spatially close to a target mesh vertex: where $\tau$ is a threshold. Each root seeds an initial cluster.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

2\) Iterative Region Expansion. Let $\boldsymbol{x}(\boldsymbol{v}_{d})=\boldsymbol{v}_{d}+\boldsymbol{t}_{d}(\boldsymbol{v}_{d})$ denote the predicted target position for a vertex $\boldsymbol{v}_{d}\in\mathcal{V}_{d}$. Starting from the region roots, cluster labels are propagated over the mesh adjacency graph of $\mathcal{M}_{d}$ using a priority queue, iteratively growing the seed regions. At each step, an unlabeled neighboring vertex joins the cluster of the root $\boldsymbol{r}\in\mathcal{R}$ that offers the closest predicted target position in Euclidean distance: Vertices are processed in ascending order of this cost, producing a watershed-like expansion that favors spatially coherent regions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

3\) Updating NVF. Once all vertices are assigned to clusters, we update the NVF on $\mathcal{M}_{d}$ according to the predicted position of region roots: Constrained QEM. While the NVF captures the desired artist-like connectivity, the predicted vertex positions often exhibit small misalignments with $\mathcal{G}$. To achieve high geometric fidelity, we "snap" the topology to $\mathcal{G}$ via a geometry-aware optimization. Therefore, we utilize the proxy mesh $\mathcal{M}_{d}$ for the geometry $\mathcal{G}$. Optimizing $\mathcal{M}_{d}$ by combining topology constraints derived from the NVF and the vanilla QEM quadrics results in a mesh aligned to both the intended topology and the original geometry $\mathcal{G}$. The vanilla QEM simplifies a mesh by iteratively collapsing vertex pairs while maintaining surface error approximations using quadric matrices.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

Each vertex is associated with a symmetric $4\times 4$ matrix $Q_{\text{geom}}$ that encodes the incident triangle set. Each edge is assigned a cost computed from the vertex quadrics, measuring the geometric distortion induced by collapsing the edge. Edges with costs below a certain threshold are collapsed to obtain a simplified mesh while preserving the overall geometry. However, the vanilla QEM does not faithfully respect artist-like mesh topology.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mesh Extraction from NVF", "weight": 1.0} -->

Our key idea is to restrict edge collapses according to the predicted topology. Specifically, an edge collapse is rejected if the two vertices have different region roots, as determined by the watershed algorithm. This prevents undesirable merging of distinct regions and aligns the resulting topology with the NVF prediction. When a valid edge collapse involves root vertices, we bias the resulting contraction point toward the corresponding vertex position predicted by the generative model. We achieve this by augmenting the geometric quadric with an additional positional constraint $Q_{t}$. The resulting quadric is defined as where $\mathrm{mean}(Q_{\text{geom}})$ denotes the average geometric quadrics accumulated at the two vertices of the edge, $Q_{t}$ is a quadratic penalty encouraging the vertex position to remain close to the target $\boldsymbol{x}(\boldsymbol{v}_{d})=(x_{t},y_{t},z_{t})^{\intercal}$, and $\lambda_{t}$ controls the constraint strength.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Geometric Data Augmentation", "weight": 1.0} -->

To improve robustness against noise and irregularity common in generated or scanned geometry, we apply a random 3D distortion field to the training data. By randomly perturbing the geometry and its corresponding NVF fields, we force the model to learn stable topological predictions even in the presence of significant local surface noise or geometric distortions. More details, including the definition of the distortion field, are provided in the supplementary material.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

The training dataset contains 656k Objaverse samples. The SDF autoencoder is built from fine-tuning the VAE of Direct3D-S2 for 170k iterations with a batch size of 16 on 8$\times$A6000 GPUs for 8 days. The NVF VAE adopts the same architecture, and is trained with $\lambda_{\text{KL}}=0.001$ for 252k iterations with batch size 32 on 8$\times$H100 GPUs for 11 days. The latent dimension of both SDF and NVF is $16$. We build our conditional latent flow matching model based on the TRELLIS architecture. The model is trained for 179k iterations with a batch size 64 on 8$\times$H100 GPUs for 12 days. All evaluations and runtime measurements are conducted on a single A6000 GPU with 4 CPU cores. Please refer to the supplementary material for more details.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Metrics and Baselines", "weight": 1.0} -->

Evaluation Metrics. We evaluate both geometric fidelity and topological quality using complementary metrics. Geometric accuracy is evaluated using Chamfer Distance between the input and output surfaces after normalizing meshes to a unit cube. We uniformly sample 10k surface points from each mesh to compute the distance. We report Fréchet Inception Distance (FID) between shaded renderings of generated and ground-truth meshes to quantify visual geometric similarity. Additionally, we introduce perceptual ratings from vision-language models (VLMs) on mesh geometry and topology to evaluate the visual coherency with artist-created meshes. We also let VLMs compare wireframe renderings and report pairwise preferences of our method against baseline methods. We further conduct a human perceptual study where participants rate and compare outputs from different approaches.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Metrics and Baselines", "weight": 1.0} -->

Baselines. We compare against both classical mesh simplification methods and recent learning-based approaches. Classical baselines include vanilla QEM and QuadriFlow, which represent widely used geometry-driven mesh simplification and remeshing techniques. We also include TreeMeshGPT and MeshMosaic as state-of-the-art learning-based methods that model priors of artist-created topology. Together, these baselines enable a comprehensive evaluation of topology quality, geometric preservation, and generalization.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Evaluation Data. We conduct evaluation on two datasets. The first consists of $\sim 1000$ test samples from Objaverse, chosen to guarantee single-component meshes with clean, artist-like topology. The second dataset contains $65$ shapes generated by TRELLIS, which exhibit challenging geometries with artifacts commonly observed in generative approaches, such as bumpy surfaces. Evaluation on TRELLIS data demonstrates the practicality and generalization of our method in real-world 3D content creation pipelines.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Target Face Counts. For Objaverse samples, we set the target number of faces for all capable methods --- including Ours, QEM, and QuadriFlow --- to match the ground-truth mesh. For TRELLIS samples, we set the target to $\sim 6000$ faces.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Method-Specific Settings. For the part-based baseline MeshMosaic, Objaverse shapes are treated as single-part meshes. Following their recommended pipeline, TRELLIS shapes are decomposed into $20$ parts using PartField. QuadriFlow requires manifold meshes as input, and thus non-manifold samples are excluded when computing evaluation metrics for QuadriFlow to ensure a fair comparison. We use the target quad-face ratio of $0.95$, the root threshold $\tau$ as $\nicefrac{{1}}{{2}}$ voxel size, and the topology weight $\lambda_{t}=0.1$ in our method. The impact of these parameters is discussed in the supplementary material.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

Ours vs. QEM QuadriFlow MeshMosaic TreeMeshGPT VLM-Geometry 70.7% 81.8% 93.0% 82.9% VLM-Topology 65.9% 84.8% 74.4% 92.7% VLM-Preference 68.3% 84.8% 76.7% 92.7% Human-Geometry 76.5% 95.7% 84.4% 97.9% Human-Topology 80.2% 94.9% 96.1% 95.0% Human-Preference 83.3% 97.1% 90.8% 97.9% Table 2: Perceptual preferences of our method compared to baselines, based on VLMs and human participants. Our method is consistently preferred in both geometry and topology quality.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

We compare TriFlow against classical approaches and learning-based methods on Objaverse and TRELLIS -generated shapes. Objaverse serves as an in-domain benchmark, as the learning-based methods are trained on its distribution. In contrast, TRELLIS-generated shapes provide out-of-distribution validation, serving as a practical test of converting over-tessellated 3D generations to compact, production-ready mesh structures. Quantitative results are summarized in Tab.˜1, perceptual preference studies are reported in Tab.˜2, and qualitative comparisons are shown in Fig.˜4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

Overall, TriFlow consistently outperforms prior approaches: across TRELLIS shapes and Objaverse, our method obtains either the best or tied-best Chamfer Distance while simultaneously achieving the lowest FID and the highest perceptual geometry and topology scores. The preference study in Tab.˜2 further supports this trend, where both VLM-based evaluation and human judgments consistently favor meshes produced by TriFlow across geometry, topology, and overall preference.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

A notable observation is the limited generalizability of learning-based baselines when evaluated beyond their training distribution, denoted by their performance gap between Objaverse and TRELLIS shapes in Tab.˜1. We attribute this to two fundamental design limitations. First, these approaches represent meshes as ordered token sequences. As a result, a significant portion of model capacity is spent on modeling sequence ordering, reducing the effective capacity for modeling geometric and topological relations. Second, autoregressive generation introduces accumulated errors: under out-of-distribution inputs such as TRELLIS geometry, errors accumulate faster, leading to more failures, as reflected in Fig.˜4. In contrast, TriFlow avoids sequential dependency during generation, enabling more stable predictions and consistent performance across both datasets.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

Level-of-Detail (LOD) Topology. Level-of-detail (LOD) is required in modern graphics pipelines, where meshes must remain visually consistent under varying computational budgets and viewing distances. We therefore evaluate TriFlow's performance across multiple simplification levels and compare it with QEM. As shown in Fig.˜5, TriFlow excels in shape abstraction at low LODs, producing regular edge flows that mirror the desirable topology of artist-crafted low-poly models. At higher resolutions, TriFlow yields a dense, structured tessellation characteristic of artist-like polygonal modeling. While QEM offers competitive shape preservation, it produces highly irregular triangular meshes that may pose challenges to downstream editing and lead to artifacts in rendering pipelines. In contrast, TriFlow introduces a learned topology prior without compromising geometric fidelity, providing LOD meshes that feature both well-preserved geometry and optimized topology.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

Runtime. While autoregressive learnable baselines are capable of generating a large amount of triangles, they are fundamentally limited by the latency of token-by-token generation. Consequently, processing a single sample takes $2.2$ hours with MeshMosaic and $4.3$ minutes with TreeMeshGPT. In contrast, by representing topology as a vector field, TriFlow achieves significantly accelerated generation: processing a sample takes only $31$ seconds.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablations", "weight": 1.0} -->

(a) Using Barycentric Coordinates (b) Using Euclidean Distance Figure 6: Analysis of using barycentric weights in NVF. This simple example shows that defining a nearest-vertex vector field with barycentric weights (a) faithfully represents the topology, compared to the naive Euclidean distance (b).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablations", "weight": 1.0} -->

We ablate design choices and individual contribution components of our pipeline, covering NVF formulation, watershed grouping, QEM optimization, and geometric data augmentation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablations", "weight": 1.0} -->

Defining NVF with Barycentric Frames. We first analyze our NVF formulated with barycentric coordinates vs. Euclidean distances. As illustrated in Fig.˜6, computing nearest vertices naively by Euclidean distance fails to respect mesh connectivity, particularly for structures like those in Fig.˜6.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablations", "weight": 1.0} -->

Watershed Grouping Enforces Topology Alignment. We ablate the watershed algorithm and apply constrained QEM to NVF predictions by directly adding positional quadrics $Q_{t}$ to all vertex quadrics in QEM. This penalizes large displacements between vertices $\boldsymbol{v}_{d}$ and their predicted target positions $\boldsymbol{x}(\boldsymbol{v}_{d})$ (Sec.˜3.3). The QEM is also performed without rejecting edge collapse across watershed groups. Tab.˜3 (w/o Watershed) shows performance degradation in geometric and topological quality, and Fig.˜7 visualizes the irregular triangulation, confirming the utility of the watershed algorithm in enforcing topology alignment to the network prediction.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablations", "weight": 1.0} -->

Constrained QEM Prevents Topological Artifacts and Enforces Geometry Preservation. Replacing the constrained QEM optimization with a naive iterative vertex-flow (driven solely by the NVF) results in significant topological artifacts and discontinuities (Tab.˜3 w/o QEM). As shown in Fig.˜7, the absence of geometric constraints leads to "missing" geometry, highlighting the necessity of geometric constraints during mesh extraction.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablations", "weight": 1.0} -->

Geometric Data Augmentation Enables Robust Generalization. Without the distortion augmentation, the trained model fails to generalize to local surface variations (Tabs.˜3 and 7, w/o Augmentation), leading to a failed topology prediction in those regions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablations", "weight": 1.0} -->

Limitations. The primary limitation of our approach is the reliance on a voxelized representation, which poses challenges for scaling to large-scale scenes. Future work could address this by adopting a multi-resolution, coarse-to-fine generation strategy or a chunk-based pipeline to enable efficient artist-like topology generation of expansive 3D environments.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we present TriFlow, a generative approach that models mesh topology as a nearest-vertex vector field to enable structured mesh generation from geometric observations. By representing topology as a piecewise continuous field rather than a discrete sequence, our approach avoids the high computational costs and error accumulation issues in autoregressive mesh generation methods. Experiments show that TriFlow achieves state-of-the-art performance in producing compact, artist-like topology while maintaining high geometric fidelity at low computational cost, demonstrating improved generalization over prior learning-based baselines. We believe this work provides a new perspective on bridging the gap between neural geometry synthesis and the topological requirements in practical 3D creation workflows.
