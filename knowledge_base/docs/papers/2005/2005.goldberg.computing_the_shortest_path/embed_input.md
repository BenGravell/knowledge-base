<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Computing the Shortest Path: A* Search Meets Graph Theory

Topics include Shortest path, A* search, Landmarks, Triangle inequality, Bidirectional search, Road networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces ALT, combining A* with precomputed landmark distances and triangle-inequality lower bounds to accelerate exact point-to-point shortest paths in directed graphs. It develops bidirectional variants and landmark selection strategies and evaluates them on road networks and synthetic graphs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose shortest path algorithms that use A* search in combination with a new graph-theoretic lower-bounding technique based on landmarks and the triangle inequality. Our algorithms compute optimal shortest paths and work on any directed graph. We give experimental results showing that the most efficient of our new algorithms outperforms previous algorithms, in particular A* search with Euclidean bounds, by a wide margin on road networks and on some synthetic problem families.
