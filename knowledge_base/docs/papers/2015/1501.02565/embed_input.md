EpicFlow: Edge-Preserving Interpolation of Correspondences for Optical Flow

Topics include Optical flow, EpicFlow, Sparse-to-dense interpolation, Edge-aware distance, Geodesic distance, Large displacement, Motion boundaries, Occlusion handling.

EpicFlow replaces fragile coarse-to-fine initialization with edge-preserving interpolation of sparse matches, then refines the result with a one-level variational method. The paper is a bridge between classical optical flow and learned matching pipelines because it shows how strong correspondences plus motion-boundary-aware interpolation can handle large displacement and occlusion better than standard pyramids.

We propose a novel approach for optical flow estimation, targeted at large displacements with significant occlusions. It consists of two steps: i) dense matching by edge-preserving interpolation from a sparse set of matches; ii) variational energy minimization initialized with the dense matches. The sparse-to-dense interpolation relies on an appropriate choice of the distance, namely an edge-aware geodesic distance. This distance is tailored to handle occlusions and motion boundaries - two common and difficult issues for optical flow computation. We also propose an approximation scheme for the geodesic distance to allow fast computation without loss of performance. Subsequent to the dense interpolation step, standard one-level variational energy minimization is carried out on the dense matches to obtain the final flow estimation. The proposed approach, called Edge-Preserving Interpolation of Correspondences (EpicFlow) is fast and robust to large displacements. It significantly outperforms the state of the art on MPI-Sintel and performs on par on Kitti and Middlebury.

## Introduction

Accurate estimation of optical flow from real-world videos remains a challenging problem, despite the abundant literature on the topic. The main remaining challenges are occlusions, motion discontinuities and large displacements, all present in real-world videos.

Effective approaches were previously proposed for handling the case of small displacements (*i.e*., less than a few pixels). These approaches cast the optical flow problem into an energy minimization framework, often solved using efficient coarse-to-fine algorithms. However, due to the complexity of the minimization, such methods get stuck in local minima and may fail to estimate large displacements, which often occur due to fast motion. This problem has recently received significant attention....

## Conclusion

This paper introduces EpicFlow, a novel state-of-the-art optical flow estimation method. EpicFlow computes a dense correspondence field by performing a sparse-to-dense interpolation from an initial sparse set of matches, leveraging contour cues using an edge-aware geodesic distance. The approach builds upon the assumption that contours often coincide with motion discontinuities. The resulting dense correspondence field is fed as an initial optical flow estimate to a one-level variational energy minimization. Experimental results show that EpicFlow outperforms current coarse-to-fine approaches....

## Experiments

### Fast approximation

Matches and interpolators. Table 1 compares the result of our sparse-to-dense interpolation, *i.e*., before energy minimization, and EpicFlow for different matches (DM and KPM) and for the two interpolation schemes: Nadaraya-Watson (NW) and locally-weighted affine (LA). The approximated geodesic distance is used in the interpolation, see Section 3.4.

Figure 1: Image edges detected with SED and ground-truth optical flow. Motion discontinuities appear most of the time at image edges.

Instead, we propose to simply interpolate a sparse set of matches in a dense manner to initiate the optical flow estimation. We then use this estimate to initialize a one-level energy minimization, and obtain the final optical flow estimation. This enables us to leverage recent advances in matching algorithms, which can now output quasi-dense correspondence fields....
