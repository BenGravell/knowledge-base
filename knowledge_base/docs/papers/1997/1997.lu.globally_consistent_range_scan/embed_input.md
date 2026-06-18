<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Globally Consistent Range Scan Alignment for Environment Mapping

Topics include Simultaneous localization and mapping, Range scan alignment, Pose graph optimization, Maximum likelihood estimation, Spatial uncertainty, Scan matching, Loop closure, Environment mapping.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces one of the earliest pose-graph-style formulations for globally consistent 2D range-scan mapping. Rather than repeatedly merging scans into a single accumulating map, it keeps local frames and relative pose constraints, then solves all poses jointly by maximum likelihood.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A robot exploring an unknown environment may need to build a world model from sensor measurements. In order to integrate all the frames of sensor data, it is essential to align the data properly. An incremental approach has been typically used in the past, in which each local frame of data is aligned to a cumulative global model, and then merged to the model. Because different parts of the model are updated independently while there are errors in the registration, such an approach may result in an inconsistent model. In this paper, we study the problem of consistent registration of multiple frames of measurements (range scans), together with the related issues of representation and manipulation of spatial uncertainties. Our approach is to maintain all the local frames of data as well as the relative spatial relationships between local frames. These spatial relationships are modeled as random variables and are derived from matching pairwise scans or from odometry. Then we formulate a procedure based on the maximum likelihood criterion to optimally combine all the spatial relations. Consistency is achieved by using all the spatial relations as constraints to solve for the data frame poses simultaneously. Experiments with both simulated and real data will be presented.
