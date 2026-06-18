<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Combining Two-View Constraints for Motion Estimation

Topics include Structure from motion, Motion averaging, Two-view geometry, Epipolar constraints, Global motion estimation, Camera calibration, Multi-view reconstruction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses redundant pairwise two-view constraints to estimate globally consistent camera motion, anticipating later motion-averaging and global-SfM formulations. Its key contribution is to move beyond chaining local estimates by solving a linear consistency problem over many image pairs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we describe two methods for estimating the motion parameters of an image sequence. For a sequence of images, the global motion can be described by n - 1 independent motion models. On the other hand, in a sequence there exist as many as n(n - 1)/2 pairwise relative motion constraints that can be solve for efficiently. In this paper we show how to linearly solve for consistent global motion models using this highly redundant set of constraints. In the first case, our method involves estimating all available pairwise relative motions and linearly fitting a global motion model to these estimates. In the second instance, we exploit the fact that algebraic (ie. epipolar) constraints between various image pairs are all related to each other by the global motion model. This results in an estimation method that directly computes the motion of the sequence by using all possible algebraic constraints. Unlike using reprojection error, our optimisation method does not solve for the structure of points resulting in a reduction of the dimensionality of the search space. Our algorithms are used for both 3D camera motion estimation and camera calibration. We provide real examples of both applications.
