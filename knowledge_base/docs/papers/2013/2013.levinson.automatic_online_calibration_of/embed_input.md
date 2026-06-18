<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Automatic Online Calibration of Cameras and Lasers

Topics include Autonomous driving, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends camera-laser calibration from offline batch processing to online monitoring and correction in arbitrary scenes. The paper contributes a probabilistic detector for sudden extrinsic miscalibration and a real-time optimizer for gradual drift, showing in vehicle experiments that small rotation and translation errors can be detected quickly and rotational drift can be tracked during operation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The combined use of 3D scanning lasers with 2D cameras has become increasingly popular in mobile robotics, as the sparse depth measurements of the former augment the dense color information of the latter. Sensor fusion requires precise 6-DOF transforms between the sensors, but hand-measuring these values is tedious and inaccurate. In addition, autonomous robots can be rendered inoperable if their sensors' calibrations change over time. Yet previously published camera-laser calibration algorithms are offline only, requiring significant amounts of data and/or specific calibration targets; they are thus unable to correct calibration errors that occur during live operation.
