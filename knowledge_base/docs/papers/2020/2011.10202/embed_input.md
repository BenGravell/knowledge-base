CLIPPER: A Graph-Theoretic Framework for Robust Data Association

Topics include Robustness, Graphs, Accuracy, Optimization, CLIPPER.

We present CLIPPER (Consistent LInking, Pruning, and Pairwise Error Rectification), a framework for robust data association in the presence of noise and outliers. We formulate the problem in a graph-theoretic framework using the notion of geometric consistency. State-of-the-art techniques that use this framework utilize either combinatorial optimization techniques that do not scale well to large-sized problems, or use heuristic approximations that yield low accuracy in high-noise, high-outlier regimes. In contrast, CLIPPER uses a relaxation of the combinatorial problem and returns solutions that are guaranteed to correspond to the optima of the original problem. Low time complexity is achieved with an efficient projected gradient ascent approach. Experiments indicate that CLIPPER maintains a consistently low runtime of 15 ms where exact methods can require up to 24 s at their peak, even on small-sized problems with 200 associations. When evaluated on noisy point cloud registration problems, CLIPPER achieves 100% precision and 98% recall in 90% outlier regimes while competing algorithms begin degrading by 70% outliers....

## INTRODUCTION

Finding correct one-to-one correspondences between two sets of objects $\mathcal{A}\overset{\text{def}}{=}{\{ a_{1},\ldots,a_{n}\}}$ and $\mathcal{A}^{\prime}\overset{\text{def}}{=}{\{ a_{1}^{\prime},\ldots,a_{m}^{\prime}\}}$ is a fundamental problem in robotics, arising in a wide range of perception and estimation pipelines. In practice, observations of objects are "noisy" and "partial", i.e., when an unknown number of objects in $\mathcal{A}$ do not correspond to any object in $\mathcal{A}^{\prime}$ (outliers)....

When an attribute between objects in set $\mathcal{A}$ is the same as the attribute between their correctly associated objects in $\mathcal{A}^{\prime}$, these objects are considered geometrically consistent (e.g., see Fig. 2). Incorporating geometric consistency in data association ultimately leads to a combinatorial optimization, such as maximum clique, maximum consensus, or quadratic assignment formulations. Relaxations of this NP-hard problem exist, but exhibit poor performance in high-outlier regimes or for large problem size. In contrast, CLIPPER maintains high precision with low runtime across various outlier-regimes and problem sizes.

## CONCLUSION

We presented CLIPPER, a graph-theoretic framework for robust data association using the notion of geometric consistency. CLIPPER was shown to consistently execute with low runtime and to outperform the state of the art, achieving 100% precision, 80% recall in 99% outlier regimes. These gains were found by implementing an efficient projected gradient descent algorithm and by formulating the data association problem on weighted graphs rather than binary.

## CLIPPER Algorithm

When $M$ is binary (e.g., obtained by using the scoring function $r{(x)}$ in Fig. 2c) and has one diagonal entries, it is straightforward to show that simplifies to

Patch Clouds A cloud of planar patches, e.g., extracted from LiDAR using, additionally provides the centroid and area of each patch. Although neither the centroid nor area are guaranteed to be invariant across views (e.g., partial view), these values can be used to assign a similarity score to corresponding planar patches by weighting the diagonal entries of the affinity matrix $M$. Geometric consistency is scored based on pairs of normals as with plane clouds.
