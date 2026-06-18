<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Local Trajectory Planning and Tracking of Autonomous Vehicles, Using Clothoid Tentacles Method

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In general, autonomous navigation requires three key steps, the perception of the environment surrounding the vehicle, the trajectory planning and the actuators control. Numerous works on the localization, perception, generation of occupancy grids and control of vehicles were developed within the ASER team at Heudiasyc laboratory. The work presented in this paper covers, essentially, trajectory planning and is based on the results of these works. The challenge is to avoid static and dynamic obstacles at high speed, using real time algorithms. The planning method developed in this work uses an empirical approach for local path planning. This approach consists on drawing clothoid tentacles in the ego-centered reference frame related to the vehicle. An occupancy grid represents the environment surrounding the vehicle and is considered to be ego-centered around it. Using the information of the occupancy grid, each tentacle is classified as navigable or not navigable. Among the navigable tentacles, only one tentacle is chosen as the vehicle reference trajectory using several criteria. The chosen tentacle is then applied to the vehicle using a lateral controller based on Immersion and Invariance principle (I&I).
