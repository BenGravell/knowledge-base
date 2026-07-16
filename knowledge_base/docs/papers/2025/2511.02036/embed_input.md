<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TurboMap: GPU-Accelerated Local Mapping for Visual SLAM

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In real-time Visual SLAM systems, local mapping must operate under strict latency constraints, as delays degrade map quality and increase the risk of tracking failure. GPU parallelization offers a promising way to reduce latency. However, parallelizing local mapping is challenging due to synchronized shared-state updates and the overhead of transferring large map data structures to the GPU. This paper presents TurboMap, a GPU-parallelized and CPU-optimized local mapping backend that holistically addresses these challenges. We restructure Map Point Creation to enable parallel Keypoint Correspondence Search on the GPU, redesign and parallelize Map Point Fusion, optimize Redundant Keyframe Culling on the CPU, and integrate a fast GPU-based Local Bundle Adjustment solver. To minimize data transfer and synchronization costs, we introduce persistent GPU-resident keyframe storage. Experiments on the EuRoC and TUM-VI datasets show average local mapping speedups of 1.3x and 1.6x, respectively, while preserving accuracy.
