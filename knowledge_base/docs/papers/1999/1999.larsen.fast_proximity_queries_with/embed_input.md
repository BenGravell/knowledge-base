<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Proximity Queries with Swept Sphere Volumes

Topics include Collision detection, Distance computation, Swept sphere volumes, Bounding volume hierarchies, Computational geometry, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces swept-sphere-volume bounding volumes and traversal methods for fast collision and distance queries. The paper is useful as a bridge between geometric collision detection and practical planning/simulation workloads where approximate and exact distances are both needed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present novel algorithms for fast proximity queries using swept sphere volumes. The set of proximity queries includes collision detection and both exact and approximate separation distance computation. We introduce a new family of bounding volumes that correspond to a core primitive shape grown outward by some offset. The set of core primitive shapes includes a point, line, and rectangle. This family of bounding volumes provides varying tightness of fit to the underlying geometry. Furthermore, we describe efficient and accurate algorithms to perform different queries using these bounding volumes. We present a novel analysis of proximity queries that highlights the relationship between collision detection and distance computation. We also present traversal techniques for accelerating distance queries. These algorithms have been used to perform proximity queries for applications including virtual prototyping, dynamic simulation, and motion planning on complex models.
