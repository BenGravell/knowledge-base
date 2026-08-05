<!-- arxiv-full-text:v1 {"arxiv_id": "2208.14437", "source": "ar5iv"} -->

## Introduction

High-definition (HD) map is the high-precision map specifically designed for autonomous driving, composed of instance-level vectorized representation of map elements (pedestrian crossing, lane divider, road boundaries, *etc.*). HD map contains rich semantic information of road topology and traffic rules, which is vital for the navigation of self-driving vehicle.

Conventionally HD map is constructed offline with SLAM-based methods, incurring complicated pipeline and high maintaining cost. Recently, online HD map construction has attracted ever-increasing interests, which constructs map around ego-vehicle at runtime with vehicle-mounted sensors, getting rid of offline human efforts.

Figure 1: MapTR maintains stable and robust vectorized HD map construction quality in complex and various driving scenes.

Early works leverage line-shape priors to perceive open-shape lanes based on the front-view image. They are restricted to single-view perception and can not cope with other map elements with arbitrary shapes. With the development of bird's eye view (BEV) representation learning, recent works predict rasterized map by performing BEV semantic segmentation. However, the rasterized map lacks vectorized instance-level information, such as the lane structure, which is important for the downstream tasks (*e.g.*, motion prediction and planning). To construct vectorized HD map, HDMapNet groups pixel-wise segmentation results, which requires complicated and time-consuming post-processing. VectorMapNet represents each map element as a point sequence. It adopts a cascaded coarse-to-fine framework and utilizes auto-regressive decoder to predict points sequentially, leading to long inference time.

Current online vectorized HD map construction methods are restricted by the efficiency and not applicable in real-time scenarios. Recently, DETR employs a simple and efficient encoder-decoder Transformer architecture and realizes end-to-end object detection.

It is natural to ask a question: Can we design a DETR-like paradigm for efficient end-to-end vectorized HD map construction? We show that the answer is affirmative with our proposed Map TRansformer (MapTR).

Different from object detection in which objects can be easily geometrically abstracted as bounding box, vectorized map elements have more dynamic shapes. To accurately describe map elements, we propose a novel unified modeling method. We model each map element as a point set with a group of equivalent permutations. The point set determines the position of the map element. And the permutation group includes all the possible organization sequences of the point set corresponding to the same geometrical shape, avoiding the ambiguity of shape.

Based on the permutation-equivalent modeling, we design a structured framework which takes as input images of vehicle-mounted cameras and outputs vectorized HD map. We streamline the online vectorized HD map construction as a parallel regression problem. Hierarchical query embeddings are proposed to flexibly encode instance-level and point-level information. All instances and all points of instance are simultaneously predicted with a unified Transformer structure. And the training pipeline is formulated as a hierarchical set prediction task, where we perform hierarchical bipartite matching to assign instances and points in turn. And we supervise the geometrical shape in both point and edge levels with the proposed point2point loss and edge direction loss.

With all the proposed designs, we present MapTR, an efficient end-to-end online vectorized HD map construction method with unified modeling and architecture. MapTR achieves the best performance and efficiency among existing vectorized map construction approaches on nuScenes dataset. In particular, MapTR-nano runs at real-time inference speed ($25.1$ FPS) on RTX 3090, $8 \times$ faster than the existing state-of-the-art camera-based method while achieving $5.0$ higher mAP. Even compared with the existing state-of-the-art multi-modality method, MapTR-nano achieves $0.7$ higher mAP and $8 \times$ faster inference speed, and MapTR-tiny achieves $13.5$ higher mAP and $3 \times$ faster inference speed. As the visualization shows (Fig. 1), MapTR maintains stable and robust map construction quality in complex and various driving scenes.

Our contributions can be summarized as follows: We propose a unified permutation-equivalent modeling approach for map elements, *i.e.*, modeling map element as a point set with a group of equivalent permutations, which accurately describes the shape of map element and stabilizes the learning process.

Based on the novel modeling, we present MapTR, a structured end-to-end framework for efficient online vectorized HD map construction. We design a hierarchical query embedding scheme to flexibly encode instance-level and point-level information, perform hierarchical bipartite matching for map element learning, and supervise the geometrical shape in both point and edge levels with the proposed point2point loss and edge direction loss.

MapTR is the first real-time and SOTA vectorized HD map construction approach with stable and robust performance in complex and various driving scenes.

## Related Work

### HD Map Construction

Recently, with the development of 2D-to-BEV methods, HD map construction is formulated as a segmentation problem based on surround-view image data captured by vehicle-mounted cameras. Chen et al.; Zhou & Krähenbühl; Hu et al.; Li et al.; Philion & Fidler; Liu et al. generate rasterized map by performing BEV semantic segmentation. To build vectorized HD map, HDMapNet groups pixel-wise semantic segmentation results with heuristic and time-consuming post-processing to generate instances. VectorMapNet serves as the first end-to-end framework, which adopts a two-stage coarse-to-fine framework and utilizes auto-regressive decoder to predict points sequentially, leading to long inference time and the ambiguity about permutation. Different from VectorMapNet, MapTR introduces novel and unified modeling for map element, solving the ambiguity and stabilizing the learning process. And MapTR builds a structured and parallel one-stage framework with much higher efficiency.

### Lane Detection

Lane detection can be viewed as a sub task of HD map construction, which focuses on detecting lane elements in the road scenes. Since most datasets of lane detection only provide single view annotations and focus on open-shape elements, related methods are restricted to single view. LaneATT utilizes anchor-based deep lane detection model to achieve good trade-off between accuracy and efficiency. LSTR adopts the Transformer architecture to directly output parameters of a lane shape model. GANet formulates lane detection as a keypoint estimation and association problem and takes a bottom-up design. Feng et al. proposes parametric Bezier curve-based method for lane detection. Instead of detecting lane in the 2D image coordinate, Garnett et al. proposes 3D-LaneNet which performs 3D lane detection in BEV. STSU represents lanes as a directed graph in BEV coordinates and adopts curve-based Bezier method to predict lanes from monocular camera image. Persformer provides better BEV feature representation and optimizes anchor design to unify 2D and 3D lane detection simultaneously. Instead of only detecting lanes in the limited single view, MapTR can perceive various kinds of map elements of $360^{\circ}$ horizontal FOV, with a unified modeling and learning framework.

### Contour-based Instance Segmentation

Another line of work related to MapTR is contour-based 2D instance segmentation. These methods reformulate 2D instance segmentation as object contour prediction task, and estimate the image coordinates of the contour vertices. CurveGCN utilizes Graph Convolution Networks to predict polygonal boundaries. Lazarow et al.; Liang et al.; Li et al.; Peng et al. rely on intermediate representations and adopt a two-stage paradigm, *i.e.*, the first stage performs segmentation / detection to generate vertices and the second stage converts vertices to polygons. These works model contours of 2D instance masks as polygons. Their modeling methods cannot cope with line-shape map elements and are not applicable for map construction. Differently, MapTR is tailored for HD map construction and models various kinds of map elements in a unified manner. Besides, MapTR does not rely on intermediate representations and has an efficient and compact pipeline.

## MapTR

### Permutation-equivalent Modeling

Figure 2: Typical cases for illustrating the ambiguity of map element about start point and direction. (a) Polyline: for the lane divider between two opposite lanes, defining its direction is difficult. Both endpoints of the lane divider can be regarded as the start point and the point set can be organized in two directions. (b) Polygon: for the pedestrian crossing, each point of the polygon can be regarded as the start point, and the polygon can be connected in two opposite directions (counter-clockwise and clockwise).

MapTR aims at modeling and learning the HD map in a unified manner. HD map is a collection of vectorized static map elements, including pedestrian crossing, lane divider, road boundarie, *etc.* For structured modeling, MapTR geometrically abstracts map elements as closed shape (like pedestrian crossing) and open shape (like lane divider). Through sampling points sequentially along the shape boundary, closed-shape element is discretized into polygon while open-shape element is discretized into polyline.

Preliminarily, both polygon and polyline can be represented as an ordered point set $V^{F} = {\lbrack v_{0},v_{1},\ldots,v_{N_{v} - 1}\rbrack}$ (see Fig. 3 (Vanilla)). $N_{v}$ denotes the number of points. However, the permutation of the point set is not explicitly defined and not unique. There exist many equivalent permutations for polygon and polyline. For example, as illustrated in Fig. 2 (a), for the lane divider (polyline) between two opposite lanes, defining its direction is difficult. Both endpoints of the lane divider can be regarded as the start point and the point set can be organized in two directions. In Fig. 2 (b), for the pedestrian crossing (polygon), the point set can be organized in two opposite directions (counter-clockwise and clockwise). And circularly changing the permutation of point set has no influence on the geometrical shape of the polygon. Imposing a fixed permutation to the point set as supervision is not rational. The imposed fixed permutation contradicts with other equivalent permutations, hampering the learning process.

To bridge this gap, MapTR models each map element with $\mathcal{V} = {(V,\Gamma)}$. $V = {\{ v_{j}\}}_{j = 0}^{N_{v} - 1}$ denotes the point set of the map element ($N_{v}$ is the number of points). $\Gamma = {\{\gamma^{k}\}}$ denotes a group of equivalent permutations of the point set $V$, covering all the possible organization sequences.

Figure 3: Illustration of permutation-equivalent modeling of MapTR. Map elements are geometrically abstracted and discretized into polylines and polygons. MapTR models each map element with (V, Γ) (a point set V and a group of equivalent permutations Γ), avoiding the ambiguity and stabilizing the learning process.

Specifically, for polyline element (see Fig. 3 (left)), $\Gamma$ includes $2$ kinds of equivalent permutations: For polygon element (see Fig. 3 (right)), $\Gamma$ includes $2 \times N_{v}$ kinds of equivalent permutations: By introducing the conception of equivalent permutations, MapTR models map elements in a unified manner and addresses the ambiguity issue. MapTR further introduces hierarchical bipartite matching (see Sec. 3.2 and Sec. 3.3) for map element learning, and designs a structured encoder-decoder Transformer architecture to efficiently predict map elements (see Sec. 3.4).

### Hierarchical Matching

MapTR parallelly infers a fixed-size set of $N$ map elements in a single pass, following the end-to-end paradigm of DETR. $N$ is set to be larger than the typical number of map elements in a scene. Let's denote the set of $N$ predicted map elements by $\hat{Y} = {\{{\hat{y}}_{i}\}}_{i = 0}^{N - 1}$. The set of ground-truth (GT) map elements is padded with $\varnothing$ (no object) to form a set with size $N$, denoted by $Y = {\{ y_{i}\}}_{i = 0}^{N - 1}$. $y_{i} = {(c_{i},V_{i},\Gamma_{i})}$, where $c_{i}$, $V_{i}$ and $\Gamma_{i}$ are respectively the target class label, point set and permutation group of GT map element $y_{i}$. ${\hat{y}}_{i} = {({\hat{p}}_{i},{\hat{V}}_{i})}$, where ${\hat{p}}_{i}$ and ${\hat{V}}_{i}$ are respectively the predicted classification score and predicted point set. To achieve structured map element modeling and learning, MapTR introduces hierarchical bipartite matching, *i.e.*, performing instance-level matching and point-level matching in order.

### Instance-level Matching

First, we need to find an optimal instance-level label assignment $\hat{\pi}$ between predicted map elements $\{{\hat{y}}_{i}\}$ and GT map elements $\{ y_{i}\}$. $\hat{\pi}$ is a permutation of $N$ elements ($\hat{\pi} \in \Pi_{N}$) with the lowest instance-level matching cost: $\mathcal{L}_{{ins}_{match}}{({\hat{y}}_{\pi{(i)}},y_{i})}$ is a pair-wise matching cost between prediction ${\hat{y}}_{\pi{(i)}}$ and GT $y_{i}$, which considers both the class label of map element and the position of point set: $\mathcal{L}_{Focal}{({\hat{p}}_{\pi{(i)}},c_{i})}$ is the class matching cost term, defined as the Focal Loss between predicted classification score ${\hat{p}}_{\pi{(i)}}$ and target class label $c_{i}$. $\mathcal{L}_{position}{({\hat{V}}_{\pi{(i)}},V_{i})}$ is the position matching cost term, which reflects the position correlation between the predicted point set ${\hat{V}}_{\pi{(i)}}$ and the GT point set $V_{i}$ (refer to Sec. B for more details). Hungarian algorithm is utilized to find the optimal instance-level assignment $\hat{\pi}$ following DETR.

### Point-level Matching

After instance-level matching, each predicted map element ${\hat{y}}_{\hat{\pi}{(i)}}$ is assigned with a GT map element $y_{i}$. Then for each predicted instance assigned with positive labels ($c_{i} \neq \varnothing$), we perform point-level matching to find an optimal point2point assignment $\hat{\gamma} \in \Gamma$ between predicted point set ${\hat{V}}_{\hat{\pi}{(i)}}$ and GT point set $V_{i}$. $\hat{\gamma}$ is selected among the predefined permutation group $\Gamma$ and with the lowest point-level matching cost: $D_{Manhattan}{({\hat{v}}_{j},v_{\gamma{(j)}})}$ is the Manhattan distance between the $j$-th point of the predicted point set $\hat{V}$ and the $\gamma{(j)}$-th point of the GT point set $V$.

### Training Loss

MapTR is trained based on the optimal instance-level and point-level assignment ($\hat{\pi}$ and $\{\hat{\gamma_{i}}\}$). The loss function is composed of three parts, classification loss, point2point loss and edge direction loss: where $\lambda$, $\alpha$ and $\beta$ are the weights for balancing different loss terms.

### Classification Loss

With the instance-level optimal matching result $\hat{\pi}$, each predicted map element is assigned with a class label. The classification loss is a Focal Loss term formulated as:

### Point2point Loss

Point2point loss supervises the position of each predicted point. For each GT instance with index $i$, according to the point-level optimal matching result ${\hat{\gamma}}_{i}$, each predicted point ${\hat{v}}_{{\hat{\pi}{(i)}},j}$ is assigned with a GT point $v_{i,{{\hat{\gamma}}_{i}{(j)}}}$. The point2point loss is defined as the Manhattan distance computed between each assigned point pair:

### Edge Direction Loss

Point2point loss only supervises the node point of polyline and polygon, not considering the edge (the connecting line between adjacent points). For accurately representing map elements, the direction of the edge is important. Thus, we further design edge direction loss to supervise the geometrical shape in the higher edge level. Specifically, we consider the cosine similarity of the paired predicted edge ${\hat{\mathbf{e}}}_{{\hat{\mathbf{π}}{({\mathbf{i}})}},{\mathbf{j}}}$ and GT edge ${\mathbf{e}}_{{\mathbf{i}},{{\hat{\mathbf{γ}}}_{\mathbf{i}}{({\mathbf{j}})}}}$: Figure 4: The overall architecture of MapTR. MapTR adopts an encoder-decoder paradigm. The map encoder transforms sensor input to a unified BEV representation. The map decoder adopts a hierarchical query embedding scheme to explicitly encode map elements and performs hierarchical matching based on the permutation-equivalent modeling. MapTR is fully end-to-end. The pipeline is highly structured, compact and efficient.

### Architecture

MapTR designs an encoder-decoder paradigm. The overall architecture is depicted in Fig. 4.

### Input Modality

MapTR takes surround-view images of vehicle-mounted cameras as input. MapTR is also compatible with other vehicle-mounted sensors (*e.g.*, LiDAR and RADAR). Extending MapTR to multi-modality data is straightforward and trivial. And thanks to the rational permutation-equivalent modeling, even with only camera input, MapTR significantly outperforms other methods with multi-modality input.

### Map Encoder

The map encoder of MapTR extracts features from images of multiple vehicle-mounted cameras and transforms the features into a unified feature representation, *i.e.*, BEV representation. Given multi-view images $\mathcal{I} = {\{ I_{1},\ldots,I_{K}\}}$, we leverage a conventional backbone to generate multi-view feature maps $\mathcal{F} = {\{ F_{1},\ldots,F_{K}\}}$. Then 2D image features $\mathcal{F}$ are transformed to BEV features $\mathcal{B} \in {\mathbb{R}}^{H \times W \times C}$. By default, we adopt GKT as the basic 2D-to-BEV transformation module, considering its easy-to-deploy property and high efficiency. MapTR is compatible with other transformation methods and maintains stable performance, *e.g.*, CVT, LSS, Deformable Attention and IPM. Ablation studies are presented in Tab. 4.

### Map Decoder

We propose a hierarchical query embedding scheme to explicitly encode each map element. Specifically, we define a set of instance-level queries ${\{ q_{i}^{ins}\}}_{i = 0}^{N - 1}$ and a set of point-level queries ${\{ q_{j}^{pt}\}}_{j = 0}^{N_{v} - 1}$ shared by all instances. Each map element (with index $i$) corresponds to a set of hierarchical queries ${\{ q_{ij}^{hie}\}}_{j = 0}^{N_{v} - 1}$. The hierarchical query of $j$-th point of $i$-th map element is formulated as: The map decoder contains several cascaded decoder layers which update the hierarchical queries iteratively. In each decoder layer, we adopt MHSA to make hierarchical queries exchange information with each other (both inter-instance and intra-instance). We then adopt Deformable Attention to make hierarchical queries interact with BEV features, inspired by BEVFormer. Each query $q_{ij}^{hie}$ predicts the 2-dimension normalized BEV coordinate $(x_{ij},y_{ij})$ of the reference point $p_{ij}$. We then sample BEV features around the reference points and update queries.

Map elements are usually with irregular shapes and require long-range context. Each map element corresponds to a set of reference points ${\{ p_{ij}\}}_{j = 0}^{N_{v} - 1}$ with flexible and dynamic distribution. The reference points ${\{ p_{ij}\}}_{j = 0}^{N_{v} - 1}$ can adapt to the arbitrary shape of map element and capture informative context for map element learning.

The prediction head of MapTR is simple, consisting of a classification branch and a point regression branch. The classification branch predicts instance class score. The point regression branch predicts the positions of the point sets $\hat{V}$. For each map element, it outputs a $2N_{v}$-dimension vector, which represents normalized BEV coordinates of the $N_{v}$ points.

## Experiments

### Dataset and Metric

We evaluate MapTR on the popular nuScenes dataset, which contains 1000 scenes of roughly 20s duration each. Key samples are annotated at $2$Hz. Each sample has RGB images from $6$ cameras and covers $360^{\circ}$ horizontal FOV of the ego-vehicle. Following the previous methods, three kinds of map elements are chosen for fair evaluation -- pedestrian crossing, lane divider, and road boundary. The perception ranges are $\lbrack{- {15.0m}},{15.0m}\rbrack$ for the $X$-axis and $\lbrack{- {30.0m}},{30.0m}\rbrack$ for the $Y$-axis. And we adopt average precision (AP) to evaluate the map construction quality. Chamfer distance $D_{Chamfer}$ is used to determine whether the prediction and GT are matched or not. We calculate the ${AP}_{\tau}$ under several $D_{Chamfer}$ thresholds (${\tau \in T},{T = {\{ 0.5,1.0,1.5\}}}$), and then average across all thresholds as the final AP metric:

### Implementation Details

MapTR is trained with $8$ NVIDIA GeForce RTX 3090 GPUs. We adopt AdamW optimizer and cosine annealing schedule. For MapTR-tiny, we adopt as the backbone. We train MapTR-tiny with a total batch size of $32$ (containig 6 view images). All ablation studies are based on MapTR-tiny trained with $24$ epochs. MapTR-nano is designed for real-time applications. We adopt as the backbone. More details are provided in Appendix A.

### Comparisons with State-of-the-Art Methods

In Tab. 1, we compare MapTR with state-of-the-art methods. MapTR-nano runs at real-time inference speed ($25.1$ FPS) on RTX 3090, $8 \times$ faster than the existing state-of-the-art camera-based method (VectorMapNet-C) while achieving $5.0$ higher mAP. Even compared with the existing state-of-the-art multi-modality method, MapTR-nano achieves $0.7$ higher mAP and $8 \times$ faster inference speed, and MapTR-tiny achieves $13.5$ higher mAP and $3 \times$ faster inference speed. MapTR is also a fast converging method, which demonstrate advanced performance with 24-epoch schedule.

Table 1: Comparisons with state-of-the-art methods on nuScenes val set. “C” and “L” respectively denotes camera and LiDAR. “Effi-B0” and “PointPillars” respectively correspond to Tan & Le and Lang et al.. The APs of other methods are taken from the paper of VectorMapNet. The FPS of VectorMapNet-C is provided by its authors and measured on RTX 3090. Other FPSs are measured on the same machine with RTX 3090. “-” means that the corresponding results are not available. Even with only camera input, MapTR-tiny significantly outperforms multi-modality counterparts (+13.5 mAP). MapTR-nano achieves SOTA camera-based performance and runs at 25.1 FPS, realizing real-time vectorized map construction for the first time.

### Ablation Study

To validate the effectiveness of different designs, we conduct ablation experiments on nuScenes val set. More ablation studies are in Appendix B.

### Effectiveness of Permutation-equivalent Modeling

In Tab. 2, we provide ablation experiments to validate the effectiveness of the proposed permutation-equivalent modeling. Compared with vanilla modeling method which imposes a unique permutation to the point set, permutation-equivalent modeling solves the ambiguity of map element and brings an improvement of $5.9$ mAP. For pedestrian crossing, the improvement even reaches $11.9$ AP, proving the superiority in modeling polygon elements. We also visualize the learning process in Fig. 5 to show the stabilization of the proposed modeling.

Table 2: Ablations about modeling method. Vanilla modeling method imposes a unique permutation to the point set, leading to ambiguity. MapTR introduces permutation-equivalent modeling to avoid the ambiguity, which stabilizes the learning process and significantly improves performance ( +5.9 mAP).

### Effectiveness of Edge Direction Loss

Table 3: Ablations about the weight β of edge direction loss.

Ablations about the weight of edge direction loss are presented in Tab. 3. $\beta = 0$ means that we do not use edge direction loss. $\beta = {5e^{- 3}}$ corresponds to appropriate supervision and is adopted as the default setting.

### 2D-to-BEV Transformation

Table 4: Ablations about 2D-to-BEV transformation methods. MapTR is compatible with various 2D-to-BEV methods and achieves stable performance.

In Tab. 4, we ablate on the 2D-to-BEV transformation methods (*e.g.*, IPM, LSS, Deformable Attention and GKT ). We use an optimized implementation of LSS. And for fair comparison with IPM and LSS, GKT and Deformable Attention both adopt one-layer configuration. Experiments show MapTR is compatible with various 2D-to-BEV methods and achieves stable performance. We adopt GKT as the default configuration of MapTR, considering its easy-to-deploy property and high efficiency.

### Qualitative Visualization

We show the predicted vectorized HD map results of complex and various driving scenes in Fig. 1. MapTR maintains stable and impressive results. More qualitative results are provided in Appendix C. We also provide videos (in the supplementary materials) to show the robustness.

## Conclusion

MapTR is a structured end-to-end framework for efficient online vectorized HD map construction, which adopts a simple encoder-decoder Transformer architecture and hierarchical bipartite matching to perform map element learning based on the proposed permutation-equivalent modeling. Extensive experiments show that the proposed method can precisely perceive map elements of arbitrary shape in the challenging nuScenes dataset. We hope MapTR can serve as a basic module of self-driving system and boost the development of downstream tasks (*e.g.*, motion prediction and planning).
