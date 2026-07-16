<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Continuous Occupancy Mapping in Dynamic Environments Using Particles

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Particle-based dynamic occupancy maps were proposed in recent years to model the obstacles in dynamic environments. Current particle-based maps describe the occupancy status in discrete grid form and suffer from the grid size problem, wherein a large grid size is unfavorable for motion planning, while a small grid size lowers efficiency and causes gaps and inconsistencies. To tackle this problem, this paper generalizes the particle-based map into continuous space and builds an efficient 3D egocentric local map. A dual-structure subspace division paradigm, composed of a voxel subspace division and a novel pyramid-like subspace division, is proposed to propagate particles and update the map efficiently with the consideration of occlusions. The occupancy status of an arbitrary point in the map space can then be estimated with the particles' weights. To further enhance the performance of simultaneously modeling static and dynamic obstacles and minimize noise, an initial velocity estimation approach and a mixture model are utilized. Experimental results show that our map can effectively and efficiently model both dynamic obstacles and static obstacles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compared to the state-of-the-art grid-form particle-based map, our map enables continuous occupancy estimation and substantially improves the performance in different resolutions.
