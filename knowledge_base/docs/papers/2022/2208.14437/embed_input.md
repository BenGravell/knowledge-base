MapTR: Structured Modeling and Learning for Online Vectorized HD Map Construction

Topics include High-definition map construction, Vectorized maps, Autonomous driving, Bird's-eye view perception, Transformers, Permutation-equivalent modeling, Hierarchical queries, Bipartite matching, NuScenes, MapTR.

Introduces a transformer architecture for online vectorized HD map construction that treats each map element as a point set with equivalent valid permutations. The permutation-equivalent representation, hierarchical query embeddings, and hierarchical bipartite matching make the method better suited to arbitrary map-element shapes while preserving real-time camera-only performance.

High-definition (HD) map provides abundant and precise environmental information of the driving scene, serving as a fundamental and indispensable component for planning in autonomous driving system. We present MapTR, a structured end-to-end Transformer for efficient online vectorized HD map construction. We propose a unified permutation-equivalent modeling approach, i.e., modeling map element as a point set with a group of equivalent permutations, which accurately describes the shape of map element and stabilizes the learning process. We design a hierarchical query embedding scheme to flexibly encode structured map information and perform hierarchical bipartite matching for map element learning. MapTR achieves the best performance and efficiency with only camera input among existing vectorized map construction approaches on nuScenes dataset. In particular, MapTR-nano runs at real-time inference speed (25.1 FPS) on RTX 3090, 8x faster than the existing state-of-the-art camera-based method while achieving 5.0 higher mAP....

## Introduction

High-definition (HD) map is the high-precision map specifically designed for autonomous driving, composed of instance-level vectorized representation of map elements (pedestrian crossing, lane divider, road boundaries, *etc.*). HD map contains rich semantic information of road topology and traffic rules, which is vital for the navigation of self-driving vehicle.

Conventionally HD map is constructed offline with SLAM-based methods, incurring complicated pipeline and high maintaining cost. Recently, online HD map construction has attracted ever-increasing interests, which constructs map around ego-vehicle at runtime with vehicle-mounted sensors, getting rid of offline human efforts.

## Conclusion

MapTR is a structured end-to-end framework for efficient online vectorized HD map construction, which adopts a simple encoder-decoder Transformer architecture and hierarchical bipartite matching to perform map element learning based on the proposed permutation-equivalent modeling. Extensive experiments show that the proposed method can precisely perceive map elements of arbitrary shape in the challenging nuScenes dataset. We hope MapTR can serve as a basic module of self-driving system and boost the development of downstream tasks (*e.g.*, motion prediction and planning).

where $\lambda$, $\alpha$ and $\beta$ are the weights for balancing different loss terms.

Figure 3: Illustration of permutation-equivalent modeling of MapTR. Map elements are geometrically abstracted and discretized into polylines and polygons. MapTR models each map element with (V,Γ) (a point set V and a group of equivalent permutations Γ), avoiding the ambiguity and stabilizing the learning process.

### Map Decoder

Figure 1: MapTR maintains stable and robust vectorized HD map construction quality in complex and various driving scenes.

Early works leverage line-shape priors to perceive open-shape lanes based on the front-view image. They are restricted to single-view perception and can not cope with other map elements with arbitrary shapes. With the development of bird's eye view (BEV) representation learning, recent works predict rasterized map by performing BEV semantic segmentation. However, the rasterized map lacks vectorized instance-level information, such as the lane structure, which is important for the downstream tasks (*e.g.*, motion prediction and planning)....
