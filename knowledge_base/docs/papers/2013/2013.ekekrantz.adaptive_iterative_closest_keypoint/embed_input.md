<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Adaptive Iterative Closest Keypoint

Topics include RGB-D registration, Iterative closest point, Keypoint matching, 3D perception, Simultaneous localization and mapping, Object recognition, Point cloud.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Adaptive Iterative Closest Keypoint, a lightweight RGB-D registration method that updates keypoint correspondences in an ICP-like loop while adapting which matches are trusted. The paper is useful for robotics perception because it targets fast registration of overlapping 3D views, improving robustness for object recognition and SLAM without requiring a heavy global optimization pipeline.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finding accurate correspondences between overlapping 3D views is crucial for many robotic applications, from multi-view 3D object recognition to SLAM. This step, often referred to as view registration, plays a key role in determining the overall system performance. In this paper, we propose a fast and simple method for registering RGB-D data, building on the principle of the Iterative Closest Point (ICP) algorithm. In contrast to ICP, our method exploits both point position and visual appearance and is able to smoothly transition the weighting between them with an adaptive metric. This results in robust initial registration based on appearance and accurate final registration using 3D points. Using keypoint clustering we are able to utilize a non exhaustive search strategy, reducing runtime of the algorithm significantly. We show through an evaluation on an established benchmark that the method significantly outperforms current methods in both robustness and precision.
