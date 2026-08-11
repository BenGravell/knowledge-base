<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Automatic Online Calibration of Cameras and Lasers

Topics include Camera-LIDAR calibration, Online calibration, Extrinsic calibration, Sensor fusion, Calibration monitoring, Sensor drift, Autonomous robots, Markerless calibration.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends camera-laser calibration from offline batch processing to online monitoring and correction in arbitrary scenes. The paper contributes a probabilistic detector for sudden extrinsic miscalibration and a real-time optimizer for gradual drift, showing in vehicle experiments that small rotation and translation errors can be detected quickly and rotational drift can be tracked during operation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The combined use of 3D scanning lasers with 2D cameras has become increasingly popular in mobile robotics, as the sparse depth measurements of the former augment the dense color information of the latter. Sensor fusion requires precise 6-DOF transforms between the sensors, but hand-measuring these values is tedious and inaccurate. In addition, autonomous robots can be rendered inoperable if their sensors' calibrations change over time. Yet previously published camera-laser calibration algorithms are offline only, requiring significant amounts of data and/or specific calibration targets; they are thus unable to correct calibration errors that occur during live operation. In this paper, we introduce two new real-time techniques that enable camera-laser calibration online, automatically, and in arbitrary environments. The first is a probabilistic monitoring algorithm that can detect a sudden miscalibration in a fraction of a second. The second is a continuous calibration optimizer that adjusts transform offsets in real time, tracking gradual sensor drift as it occurs. Although the calibration objective function is not globally convex and cannot be optimized in real time, in practice it is always locally convex around the global optimum, and almost everywhere else.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Thus, the local shape of the objective function at the current parameters can be used to determine whether the sensors are calibrated, and allows the parameters to be adjusted gradually so as to maintain the global optimum. In several online experiments on thousands of frames in real markerless scenes, our method automatically detects miscalibrations within one second of the error exceeding.25 deg or 10cm, with an accuracy of 100%. In addition, rotational sensor drift can be tracked in real-time with a mean error of just.10 deg. Together, these techniques allow significantly greater flexibility and adaptability of robots in unknown and potentially harsh environments.
