<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Fast Algorithm for Incremental Distance Calculation

Topics include Collision detection, Distance queries, Convex polyhedra, Motion planning, Computational geometry, Closest points.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents an incremental closest-feature method for distance queries between convex polyhedra, exploiting temporal coherence so repeated distance computations can often be updated in near-constant time. The idea became a practical primitive for collision checking and motion-planning systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A simple and efficient algorithm for finding the closest points between two convex polyhedra is described. Data from numerous experiments tested on a broad set of convex polyhedra in R3 show that the running time is roughly constant for finding closest points when nearest points are approximately known and is linear in total number of vertices if no special initialization is done. This algorithm can be used for collision detection, computation of the distance between two polyhedra in three-dimensional space, and other robotics problems. It forms the heart of the motion planning algorithm previously presented by the authors.
