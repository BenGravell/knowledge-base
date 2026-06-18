<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Simple Proof of Thue's Theorem on Circle Packing

Topics include Circle packing, Delaunay triangulation, Discrete geometry, Packing density, Thue theorem, Geometric proof.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives a short proof of Thue's circle-packing theorem using density analysis on the Delaunay triangulation of saturated circle centers. The note is useful as a compact geometric route to the optimality of hexagonal circle packing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A simple proof of Thue theorem on Circle Packing is given. The proof is only based on density analysis of Delaunay triangulation for the set of points that are centers of circles in a saturated circle configuration.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Thue's theorem states that the regular hexagonal packing is the densest circle packing in the plane. The density of this circle configuration is

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In geometry, circle packing refers to the study of the arrangement of unit circles on the plane such that no overlapping occurs, which is the 2-dimensional analog of Kepler's sphere packing problem proposed in 1611. A circle configuration which refers to the centers of circles is a set of points such that the distance between any two points in the set is greater than or equal to $2$. Imagine filling a large container with small unit circles inside. The density of the arrangement is the proportion of the area of the container that is taken up by the circles. In order to maximize the number of circles in the container, you need to find an arrangement with the highest possible density, so that the circles are packed together as closely as possible. Hence, the density of a circle configuration is the asymptotic limit on density with the container getting bigger and bigger. In 1773, Lagrange proved that the minimal density is $\pi/\sqrt{12}$ by assuming that the circle configurations are lattices. In 1831, Gauss proved that the minimal density of sphere packing is $\pi/\sqrt{18}$ by assuming that the sphere configurations are lattices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Without the lattice assumption, the first proof of circle packing problem was made by Axel Thue. However, it is generally believed that Thue's original proof was incomplete and that the first complete and flawless proof of this fact was produced by L. F. Toth. Later, different proofs were proposed by Segre and Mahler, Davenport, and Hsiang.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A circle configuration is called saturated if it is not a proper subset of another circle configuration. Given a circle configuration $\mathcal{C}$, any saturated circle configuration containing $\mathcal{C}$ is called a saturation of $\mathcal{C}$. Since the density of a circle configuration $\mathcal{C}$ is always less than or equal to the density of any saturation of $\mathcal{C}$. Hence, we only need to consider the saturated circle configurations instead of all circle configurations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A Delaunay triangulation in the plane with circumcircles shown. From

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In computational geometry, a point set triangulation, i.e., a triangulation $T{(\mathcal{C})}$ of a discrete set of points $\mathcal{C}$ on the plane is a subdivision of the convex hull of the points into triangles such that any two triangles intersect in a common edge or not at all and the set of points that are vertices of the triangles coincides with $\mathcal{C}$. The Delaunay triangulation for a set $\mathcal{C}$ of points in the plane is a triangulation $DT{(\mathcal{C})}$ such that no point in the set $\mathcal{C}$ is inside the circumcircle of any triangle in $DT{(\mathcal{C})}$. Delaunay invented such triangulations in 1934. The uniqueness and existence of Delaunay triangulations are both uncertain. For example, there is no Delaunay triangulation for a set of points on a straight line.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The Delaunay triangulations for four points on a circle are not unique; it is obvious that there are two possible triangulations for a cocircular quadrilateral splitting into two triangles. However, there always exists a Delaunay triangulation for a saturated circle configuration. To find the Delaunay triangulation of a set of points in the plane can be converted to find the convex hull of a set of points in $3$-dimensional Euclidean space, by giving every point $p$ in a saturated circle configuration an extra coordinate equal to ${|p|}^{2}$, taking the convex hull, and mapping back to the Euclidean plane by forgetting the last coordinate. A facet of the convex hull not being a triangle implies that at least $4$ of the original points lay on the same circle, which makes the triangulation not unique.
