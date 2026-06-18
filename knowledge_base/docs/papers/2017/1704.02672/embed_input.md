Quaternion Based Camera Pose Estimation from Matched Feature Points

Topics include Robustness, Pose estimation, Graphs, Accuracy, Online algorithms.

We present a novel solution to the camera pose estimation problem, where rotation and translation of a camera between two views are estimated from matched feature points in the images. The camera pose estimation problem is traditionally solved via algorithms that are based on the essential matrix or the Euclidean homography. With six or more feature points in general positions in the space, essential matrix based algorithms can recover a unique solution. However, such algorithms fail when points are on critical surfaces (e.g., coplanar points) and homography should be used instead. By formulating the problem in quaternions and decoupling the rotation and translation estimation, our proposed algorithm works for all point configurations. Using both simulated and real world images, we compare the estimation accuracy of our algorithm with some of the most commonly used algorithms. Our method is shown to be more robust to noise and outliers. For the benefit of community, we have made the implementation of our algorithm available online and free.

## Introduction

Many applications in computer vision and robotics require measurements of the rotation and translation (i.e., pose) changes of an object as it moves through an environment. In photogrammetry, for example, by knowing the pose changes of the camera, 3D model of a scene can be constructed from a set of 2D images. In robotics, pose estimated from images can be used for navigation, or fused with other sensor measurements (e.g., IMU and GPS) to increase the reliability and accuracy. Camera pose estimation has further applications in simultaneous localization and mapping (SLAM), autonomous vehicles, and augmented reality.

Camera pose estimation techniques are often based on image features (e.g., edges, corners, etc., in an image) that can be detected and matched in two or more images. Figure 1 shows an example where feature points are detected and matched as indicated by yellow lines in two images. Many existing methods use the coordinates of feature points on the image to construct the essential/fundamental matrix or the Euclidean homography matrix, from which relative rotation and translation of the camera can be recovered....

## Conclusion and Future Work

By using quaternion representation of rotation, we formulated the camera pose estimation problem and presented the QuEst algorithm to recover the relative pose between two camera views. Unlike the existing homography or essential matrix based methods, QuEst decouples the rotation and translation estimation, and recovers the pose correctly for both cases of general and coplanar points. QuEst can be used to initialize the bundle adjustment algorithm in applications such as SLAM without needing to resort to heuristic methods to detect the coplanarity of the points....

Consider the system of equations for 7 matched feature points. Since 7 points generate $\binom{7}{3} = 35$ equations, in this case $\mathbf{A}$ is a $35 \times 35$ matrix. Due to the mathematical multiplicity of solutions however, $\mathbf{A}$ cannot be full rank (otherwise, only one solution exists, which is a contradiction).

To recover the pose, we first eliminate the unknowns $u,v$ and $\mathbf{t}$, and derive a system of equations in terms of the quaternion elements. From solving this system all rotation solution candidates are found. Subsequently, the translation and depths of the points are recovered....
