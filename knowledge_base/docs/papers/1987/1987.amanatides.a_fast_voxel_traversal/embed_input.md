<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Fast Voxel Traversal Algorithm for Ray Tracing

Topics include Ray tracing, Voxel traversal, Uniform grids, Spatial subdivision, Digital differential analyzer.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces incremental traversal of a uniform 3D voxel grid along a ray using very few arithmetic operations per step. It also avoids repeated intersection tests for objects spanning multiple voxels.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A fast and simple voxel traversal algorithm through a 3D space partition is introduced. Going from one voxel to its neighbour requires only two floating point comparisons and one floating point addition. Also, multiple ray intersections with objects that are in more than one voxel are eliminated.
