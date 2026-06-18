A Simple Proof of Thue's Theorem on Circle Packing

Topics include Circle packing, Delaunay triangulation, Discrete geometry, Packing density, Thue theorem, Geometric proof.

Gives a short proof of Thue's circle-packing theorem using density analysis on the Delaunay triangulation of saturated circle centers. The note is useful as a compact geometric route to the optimality of hexagonal circle packing.

A simple proof of Thue theorem on Circle Packing is given. The proof is only based on density analysis of Delaunay triangulation for the set of points that are centers of circles in a saturated circle configuration.

Thue's theorem states that the regular hexagonal packing is the densest circle packing in the plane. The density of this circle configuration is

In geometry, circle packing refers to the study of the arrangement of unit circles on the plane such that no overlapping occurs, which is the 2-dimensional analog of Kepler's sphere packing problem proposed in 1611. A circle configuration which refers to the centers of circles is a set of points such that the distance between any two points in the set is greater than or equal to $2$. Imagine filling a large container with small unit circles inside. The density of the arrangement is the proportion of the area of the container that is taken up by the circles.

A circle configuration is called saturated if it is not a proper subset of another circle configuration. Given a circle configuration $\mathcal{C}$, any saturated circle configuration containing $\mathcal{C}$ is called a saturation of $\mathcal{C}$. Since the density of a circle configuration $\mathcal{C}$ is always less than or equal to the density of any saturation of $\mathcal{C}$. Hence, we only need to consider the saturated circle configurations instead of all circle configurations.

A Delaunay triangulation in the plane with circumcircles shown. From

In computational geometry, a point set triangulation, i.e., a triangulation $T{(\mathcal{C})}$ of a discrete set of points $\mathcal{C}$ on the plane is a subdivision of the convex hull of the points into triangles such that any two triangles intersect in a common edge or not at all and the set of points that are vertices of the triangles coincides with $\mathcal{C}$. The Delaunay triangulation for a set $\mathcal{C}$ of points in the plane is a triangulation $DT{(\mathcal{C})}$ such that no point in the set $\mathcal{C}$ is inside the circumcircle of any triangle in $DT{(\mathcal{C})}$. Delaunay invented such triangulations in 1934.
