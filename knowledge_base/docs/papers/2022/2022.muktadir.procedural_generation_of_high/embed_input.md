<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Procedural Generation of High-Definition Road Networks for Autonomous Vehicle Testing and Traffic Simulations

Topics include Procedural generation, Autonomous driving, Road networks, Simulation, OpenDRIVE.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces JunctionArt, a procedural generator for diverse OpenDRIVE road and intersection geometries, and evaluates its expressive range and interoperability with driving simulators.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Effective simulation-based testing of autonomous vehicles requires the exploration of vehicle performance against a wide variety of rare and unusual road and intersection geometries. We present a high-definition road and intersection generator called JunctionArt. JunctionArt takes as input a series of control lines and generates a series of roads and intersections which conforms to them. Roads exhibit different types of lane types such as turn lanes, one-way streets, and multiple lanes, while intersections feature a range of incident roads (three to seven incident roads), leading to a variety of geometries and interior connecting lanes. These roads are output in the OpenDRIVE format and, hence, are interoperable with a wide range of tools and simulation environments. Multiple metrics are computed over generated roads—field of view (FOV), maximum turn curvature (maxCurvature), corner deviation angle (cornerDeviation), complexity, conflictArea, and the number of interior connection lanes—and are used to perform an expressive range analysis. This analysis finds that JunctionArt is capable of creating rare and unusual intersection situations, i.e., representatives of the long tail of infrequent road configurations.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interoperability with third-party simulation tools and environments RoadRunner, Carla, and esmini is demonstrated.
