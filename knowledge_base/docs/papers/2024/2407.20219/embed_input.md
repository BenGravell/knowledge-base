Global Structure-from-Motion Revisited

Topics include Structure from motion, Global structure from motion, GLOMAP, Rotation averaging, Camera position averaging, COLMAP, Open source.

Revisits global SfM with a practical GLOMAP pipeline that makes global reconstruction competitive with incremental COLMAP-level accuracy while retaining much higher speed. The system emphasizes robust global estimation and open-source interoperability with COLMAP data.

Recovering 3D structure and camera motion from images has been a long-standing focus of computer vision research and is known as Structure-from-Motion (SfM). Solutions to this problem are categorized into incremental and global approaches. Until now, the most popular systems follow the incremental paradigm due to its superior accuracy and robustness, while global approaches are drastically more scalable and efficient. With this work, we revisit the problem of global SfM and propose GLOMAP as a new general-purpose system that outperforms the state of the art in global SfM. In terms of accuracy and robustness, we achieve results on-par or superior to COLMAP, the most widely used incremental SfM, while being orders of magnitude faster. We share our system as an open-source implementation at

## Introduction

Recovering 3D structure and camera motion from a collection of images remains a fundamental problem in computer vision that is highly relevant for a variety of downstream tasks, such as novel-view-synthesis or cloud-based mapping and localization. The literature commonly refers to this problem as Structure-from-Motion (SfM) and, over the years, two main paradigms for solving it have emerged: incremental and global approaches. Both of them start with image-based feature extraction and matching followed by two-view geometry estimation to construct the initial view graph of the input images.

The main reason for the accuracy and robustness gap between incremental and global SfM lies in the global translation averaging step. Translation averaging describes the problem of estimating global camera positions from the set of relative poses in the view graph with the camera orientations recovered before by rotation averaging. This process faces three major challenges in practice. The first being scale ambiguity: relative translation from estimated two-view geometry can only be determined up to scale. As such, to accurately estimate global camera positions, triplets of relative directions are required.

## Limitations

Though generally achieving satisfying performance, there still remain some failure cases. The major cause is a failure of rotation averaging, *e.g*., due to symmetric structures. In such a case, our method could be combined with existing approaches like Doppelganger. Also, since we rely on traditional correspondence search, incorrectly estimated two-view geometries or the inability to match image pairs altogether (*e.g*., due to drastic appearance or viewpoint changes) will lead to degraded results or, in the worst case, catastrophic failures.

## Conclusion

In summary, we proposed GLOMAP as a new global SfM pipeline. Previous systems within this category have been considered more efficient but less robust than incremental approaches. We revisited the problem and concluded that the key lies in the use of points in the optimization. Instead of estimating camera positions via ill-posed translation averaging and separately obtaining 3D structure from point triangulation, we merge them into a single global positioning step.
