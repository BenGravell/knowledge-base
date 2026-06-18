<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sharpness Continuous Path Optimization and Sparsification for Automated Vehicles

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a path optimization approach that ensures driveability while considering a vehicle’s lateral dynamics. The lateral dynamics are non-holonomic; therefore, a vehicle cannot follow a path with abrupt changes even with infinitely fast steering. The curvature and sharpness, i.e., the rate change of curvature with respect to the traveled distance, must be continuous to track a defined reference path efficiently. Existing path optimization techniques typically include sharpness limitations but not sharpness continuity. The sharpness discontinuity is especially problematic for heavy-duty vehicles because their actuator dynamics are even slower than cars. We propose an algorithm that constructs a sparsified sharpness continuous path for a given reference path considering the limits on sharpness and its derivative, which subsequently addresses the torque restrictions of the actuator. The sharpness continuous path needs less steering effort and reduces mechanical stress and fatigue in the steering unit. We compare and present the outcomes for each of the three different types of optimized paths. Simulation results demonstrate that computed sharpness continuous path profiles reduce lateral jerks, enhancing comfort and driveability.
