CLIPPER+: A Fast Maximal Clique Algorithm for Robust Global Registration

Topics include Robotics, Robustness, Graphs, Computational complexity, Benchmarks, Accuracy, NP-hardness.

We present CLIPPER+, an algorithm for finding maximal cliques in unweighted graphs for outlier-robust global registration. The registration problem can be formulated as a graph and solved by finding its maximum clique. This formulation leads to extreme robustness to outliers; however, finding the maximum clique is an NP-hard problem, and therefore approximation is required in practice for large-size problems. The performance of an approximation algorithm is evaluated by its computational complexity (the lower the runtime, the better) and solution accuracy (how close the solution is to the maximum clique). Accordingly, the main contribution of CLIPPER+ is outperforming the state-of-the-art in accuracy while maintaining a relatively low runtime. CLIPPER+ builds on prior work (CLIPPER and PMC ) and prunes the graph by removing vertices that have a small core number and cannot be a part of the maximum clique. This will result in a smaller graph, on which the maximum clique can be estimated considerably faster. We evaluate the performance of CLIPPER+ on standard graph benchmarks, as well as synthetic and real-world point cloud registration problems.

## Introduction

Data association is broadly defined as the correspondence of identical/similar elements across sets of data, and is a key component of many robotics and computer vision applications, such as localization and mapping, point cloud registration, shape alignment, object detection, data fusion, and multi-object tracking. In these applications, it is crucial that data association is solved correctly and fast.

In point cloud registration, for example, we seek to find the rigid transformation (rotation/translation) that aligns two sets of 3D points. This requires associating points in one set with their corresponding points in the other set. Local registration techniques such as the Iterative Closest Point (ICP) algorithm associate points based on their nearest neighbor. These associations are generally wrong if the point clouds are not aligned well initially, leading to wrong registration.

To address these issues, we present the CLIPPER+ algorithm. CLIPPER+ formulates the data association problem as a graph, in which the inlier/correct associations are the maximum clique. This formulation is robust to high outlier ratios and applicable to any problem that admits invariants (see Section III) such as point, line, and plane could registration. To address the high computational complexity of finding the maximum clique (NP-hardness), CLIPPER+ finds an approximate solution instead, which is obtained from combining an improved version of our prior work, CLIPPER, and the greedy maximal clique algorithm.

In

## Conclusion and Future Directions

We presented CLIPPER+, a maximal-clique-finding algorithm for unweighted graphs that enables robust global registration in robotics and computer vision applications. Future work includes investigating alternative optimization methods such as second-order or quasi-Newton methods, and an extension to the weighted graphs based on our previous work (designed for weighted graphs) and an extension of core numbers to weighted settings. We also plan to integrate the algorithm in point cloud registration pipelines as the outlier rejection module to improve the runtime and outlier rejection capacity.
