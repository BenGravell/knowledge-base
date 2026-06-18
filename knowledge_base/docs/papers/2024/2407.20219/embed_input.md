Global Structure-from-Motion Revisited

Topics include Structure from motion, Global structure from motion, GLOMAP, Rotation averaging, Camera position averaging, COLMAP, Open source.

Revisits global SfM with a practical GLOMAP pipeline that makes global reconstruction competitive with incremental COLMAP-level accuracy while retaining much higher speed. The system emphasizes robust global estimation and open-source interoperability with COLMAP data.

Recovering 3D structure and camera motion from images has been a long-standing focus of computer vision research and is known as Structure-from-Motion (SfM). Solutions to this problem are categorized into incremental and global approaches. Until now, the most popular systems follow the incremental paradigm due to its superior accuracy and robustness, while global approaches are drastically more scalable and efficient. With this work, we revisit the problem of global SfM and propose GLOMAP as a new general-purpose system that outperforms the state of the art in global SfM. In terms of accuracy and robustness, we achieve results on-par or superior to COLMAP, the most widely used incremental SfM, while being orders of magnitude faster. We share our system as an open-source implementation at

## Introduction

Recovering 3D structure and camera motion from a collection of images remains a fundamental problem in computer vision that is highly relevant for a variety of downstream tasks, such as novel-view-synthesis or cloud-based mapping and localization. The literature commonly refers to this problem as Structure-from-Motion (SfM) \[\] and, over the years, two main paradigms for solving it have emerged: incremental and global approaches. Both of them start with image-based feature extraction and matching followed by two-view geometry estimation to construct the initial view graph of the input images....

Figure 1: Proposed GLOMAP produces satisfying reconstructions on various datasets. For (b), from left to right are estimated by Theia, COLMAP, GLOMAP. While baseline models fail to produce reliable estimations, GLOMAP achieves high accuracy.

## Conclusion

In summary, we proposed GLOMAP as a new global SfM pipeline. Previous systems within this category have been considered more efficient but less robust than incremental approaches. We revisited the problem and concluded that the key lies in the use of points in the optimization. Instead of estimating camera positions via ill-posed translation averaging and separately obtaining 3D structure from point triangulation, we merge them into a single global positioning step....

### Global Positioning of Cameras and Points

To combine the robustness of incremental and efficiency of global SfM, previous works have formulated hybrid systems. HSfM \[\] proposes to incrementally estimate camera positions with rotations. Liu *et al*. \[\] proposes a graph partitioning method by first dividing the whole set of images into overlapping clusters. Within each cluster, camera poses are estimated via a global SfM method. However, such methods are still not applicable when camera intrinsics are inaccurate according to their formulation. Our method overcomes this limitation by different modeling of the objective in the global positioning step.

The pipeline of the proposed method is summarized in Fig.. It consists of two major components: correspondence search and global estimation. For correspondence search, it starts with feature extractions and matching. Two-view geometry, including fundamental matrix, essential matrix, and homography, are estimated from the matches....
