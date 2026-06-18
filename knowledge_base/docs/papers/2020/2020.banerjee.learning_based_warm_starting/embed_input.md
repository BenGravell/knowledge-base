<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning-based Warm-Starting for Fast Sequential Convex Programming and Trajectory Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sequential convex programming (SCP) has recently emerged as an effective tool to quickly compute locally optimal trajectories for robotic and aerospace systems alike, even when initialized with an unfeasible trajectory. In this paper, by focusing on the Guaranteed Sequential Trajectory Optimization (GuSTO) algorithm, we propose a methodology to accelerate SCP-based algorithms through warm-starting. Specifically, leveraging a dataset of expert trajectories from GuSTO, we devise a neural-network-based approach to predict a locally optimal state and control trajectory, which is used to warm-start the SCP algorithm. This approach allows one to retain all the theoretical guarantees of GuSTO while simultaneously taking advantage of the fast execution of the neural network and reducing the time and number of iterations required for GuSTO to converge. The result is a faster and theoretically guaranteed trajectory optimization algorithm.
