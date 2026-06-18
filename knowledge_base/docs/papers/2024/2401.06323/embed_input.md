<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kimera2: Robust and Accurate Metric-Semantic SLAM in the Real World

Topics include Metric-semantic simultaneous localization and mapping, Visual-inertial odometry, Pose graph optimization, Robust optimization, Graduated non-convexity, Mesh optimization, Open-source software, Multimodal sensing, Kimera, Kimera2.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Updates Kimera into a more robust and practical metric-semantic SLAM stack by improving feature tracking, keyframe selection, input modality support, and robust pose-graph and mesh optimization. The paper is useful as both a system paper and a real-world evaluation of Kimera across drones, quadrupeds, wheeled robots, and driving-style settings.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present improvements to Kimera, an open-source metric-semantic visual-inertial SLAM library. In particular, we enhance Kimera-VIO, the visual-inertial odometry pipeline powering Kimera, to support better feature tracking, more efficient keyframe selection, and various input modalities (eg monocular, stereo, and RGB-D images, as well as wheel odometry). Additionally, Kimera-RPGO and Kimera-PGMO, Kimera's pose-graph optimization backends, are updated to support modern outlier rejection methods - specifically, Graduated-Non-Convexity - for improved robustness to spurious loop closures. These new features are evaluated extensively on a variety of simulated and real robotic platforms, including drones, quadrupeds, wheeled robots, and simulated self-driving cars. We present comparisons against several state-of-the-art visual-inertial SLAM pipelines and discuss strengths and weaknesses of the new release of Kimera. The newly added features have been released open-source at
