Learning to Estimate Hidden Motions with Global Motion Aggregation

Topics include Optical flow, GMA, Occlusion handling, Global motion aggregation, Transformers, Self-similarity, RAFT extension.

GMA targets one of RAFT's weak spots: estimating motion for pixels that disappear or become occluded between two frames. By aggregating motion features globally using transformer-style dependencies, it propagates reliable motion information from visible regions to hidden ones without requiring extra frames.

Occlusions pose a significant challenge to optical flow algorithms that rely on local evidences. We consider an occluded point to be one that is imaged in the first frame but not in the next, a slight overloading of the standard definition since it also includes points that move out-of-frame. Estimating the motion of these points is extremely difficult, particularly in the two-frame setting. Previous work relies on CNNs to learn occlusions, without much success, or requires multiple frames to reason about occlusions using temporal smoothness. In this paper, we argue that the occlusion problem can be better solved in the two-frame case by modelling image self-similarities. We introduce a global motion aggregation module, a transformer-based approach to find long-range dependencies between pixels in the first image, and perform global aggregation on the corresponding motion features. We demonstrate that the optical flow estimates in the occluded regions can be significantly improved without damaging the performance in non-occluded regions....

### Introduction

How can we estimate the 2D motion of a point we only see once? This is the problem faced by optical flow algorithms for points that become occluded between frames. Estimating the optical flow, that is, the apparent motion of pixels in an image as the camera and scene move, is a classic problem in computer vision studied since the seminal work of Horn and Schunck. There are many factors that make optical flow prediction a hard problem, including large motions, motion and defocus blur, and featureless regions. Among these challenges, occlusion is one of the most difficult and under-explored....

We first define what we mean by occlusion in the context of optical flow estimation. In this paper, an occluded point is defined as a 3D point that is imaged in the reference frame but is not visible in the matching frame. This definition incorporates several different scenarios, such as the query point moving out-of-frame or behind another object (or itself), or another object moving in front of the query point, in the active sense. One particular case of occlusion is shown in Figure LABEL:fig:demo, where part of the blade moves out-of-frame.

### Conclusion

Occlusions have long been considered a significant challenge and a major source of error in optical flow estimation. Inspired by the recent success of transformers, we introduce a global motion aggregation module to globally aggregate motion features based on appearance self-similarity of the first image. This has been validated by experiments that show significantly improved optical flow predictions for occluded regions, particularly the large reduction of EPE on Sintel Clean and Final....

where $\mathbf{p}_{j - i}$ denotes the relative positional embedding vector indexed by the pixel offset $j - i$. Separate embedding vectors are learned for the vertical and horizontal offsets and are summed to obtain $\mathbf{p}_{j - i}$. If it is useful to suppress pixels that are very close or very far from the query point when aggregating the motion vectors, then this positional embedding has the capacity to learn this behaviour.

### Overview

To verify the effectiveness of our proposed GMA module at estimating the motion of occluded points, we make use of the occlusion maps provided in the Sintel training set, which partition the pixels into non-occluded (Noc) and occluded (Occ) pixels....
