MapTR: Structured Modeling and Learning for Online Vectorized HD Map Construction

Topics include High-definition map construction, Vectorized maps, Autonomous driving, Bird's-eye view perception, Transformers, Permutation-equivalent modeling, Hierarchical queries, Bipartite matching, NuScenes, MapTR.

Introduces a transformer architecture for online vectorized HD map construction that treats each map element as a point set with equivalent valid permutations. The permutation-equivalent representation, hierarchical query embeddings, and hierarchical bipartite matching make the method better suited to arbitrary map-element shapes while preserving real-time camera-only performance.

High-definition (HD) map provides abundant and precise environmental information of the driving scene, serving as a fundamental and indispensable component for planning in autonomous driving system. We present MapTR, a structured end-to-end Transformer for efficient online vectorized HD map construction. We propose a unified permutation-equivalent modeling approach, i.e., modeling map element as a point set with a group of equivalent permutations, which accurately describes the shape of map element and stabilizes the learning process. We design a hierarchical query embedding scheme to flexibly encode structured map information and perform hierarchical bipartite matching for map element learning. MapTR achieves the best performance and efficiency with only camera input among existing vectorized map construction approaches on nuScenes dataset. In particular, MapTR-nano runs at real-time inference speed (25.1 FPS) on RTX 3090, 8x faster than the existing state-of-the-art camera-based method while achieving 5.0 higher mAP.

## Introduction

High-definition (HD) map is the high-precision map specifically designed for autonomous driving, composed of instance-level vectorized representation of map elements (pedestrian crossing, lane divider, road boundaries, *etc.*). HD map contains rich semantic information of road topology and traffic rules, which is vital for the navigation of self-driving vehicle.

Conventionally HD map is constructed offline with SLAM-based methods, incurring complicated pipeline and high maintaining cost. Recently, online HD map construction has attracted ever-increasing interests, which constructs map around ego-vehicle at runtime with vehicle-mounted sensors, getting rid of offline human efforts.

It is natural to ask a question: Can we design a DETR-like paradigm for efficient end-to-end vectorized HD map construction? We show that the answer is affirmative with our proposed Map TRansformer (MapTR).

Different from object detection in which objects can be easily geometrically abstracted as bounding box, vectorized map elements have more dynamic shapes. To accurately describe map elements, we propose a novel unified modeling method. We model each map element as a point set with a group of equivalent permutations. The point set determines the position of the map element. And the permutation group includes all the possible organization sequences of the point set corresponding to the same geometrical shape, avoiding the ambiguity of shape.

We propose a unified permutation-equivalent modeling approach for map elements, *i.e.*, modeling map element as a point set with a group of equivalent permutations, which accurately describes the shape of map element and stabilizes the learning process.

## Conclusion

MapTR is a structured end-to-end framework for efficient online vectorized HD map construction, which adopts a simple encoder-decoder Transformer architecture and hierarchical bipartite matching to perform map element learning based on the proposed permutation-equivalent modeling. Extensive experiments show that the proposed method can precisely perceive map elements of arbitrary shape in the challenging nuScenes dataset. We hope MapTR can serve as a basic module of self-driving system and boost the development of downstream tasks (*e.g.*, motion prediction and planning).
