<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Rapidly-exploring Random Trees: A New Tool for Path Planning

Topics include Motion planning, Path planning, Sampling-based, Rapidly-exploring random tree.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces RRTs for sampling-based motion planning in high-dimensional configuration spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class of path planning problems. While they share many of the beneficial properties of existing randomized planning techniques, RRTs are specifically designed to handle nonholonomic constraints (including dynamics) and high degrees of freedom. An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, as opposed to requiring point-to-point convergence, as in the probabilistic roadmap approach. Several desirable properties and a basic implementation of RRTs are discussed. To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom.
