<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Collision-Affording Point Trees: SIMD-Amenable Nearest Neighbors for Fast Collision Checking

Topics include Motion planning, Robotics, Nearest neighbors, Real-time systems, Sampling-based methods, Planning, Control, Sampling, Collision-affording point tree, CAPT, Single-instruction multiple-data.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning against sensor data is often a critical bottleneck in real-time robot control. For sampling-based motion planners, which are effective for high-dimensional systems such as manipulators, the most time-intensive component is collision checking. We present a novel spatial data structure, the collision-affording point tree (CAPT): an exact representation of point clouds that accelerates collision-checking queries between robots and point clouds by an order of magnitude, with an average query time of less than 10 nanoseconds on 3D scenes comprising thousands of points. With the CAPT, sampling-based planners can generate valid, high-quality paths in under a millisecond, with total end-to-end computation time faster than 60 FPS, on a single thread of a consumer-grade CPU. We also present a point cloud filtering algorithm, based on space-filling curves, which reduces the number of points in a point cloud while preserving structure. Our approach enables robots to plan at real-time speeds in sensed environments, opening up potential uses of planning for high-dimensional systems in dynamic, changing, and unmodeled environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning underpins many applications of high-degree-of-freedom robots, allowing them to efficiently find collision-free trajectories between arbitrary poses. Modern motion planning methods capably solve problems with many obstacles for these high-dimensional robots, typically by either building and searching a graph or tree approximating the collision-free subset of the robot's state space (*i.e.*, sampling-based motion planning (sbmp) \[orthey2023sampling, LaValle2001, Kavraki1996\]) or by solving a numerical optimization problem (*i.e.*, trajectory optimization \[Schulman2014, Zucker2013, bhardwaj_storm_integrated_2021\]). The most time-consuming component of most motion planners---and sbmps in particular---is *state validation*, which ensures that a robot's state does not violate its constraints or collide with obstacles \[bialkowski_massively_parallelizing_2011, lavalle2006planning\].

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

State validators commonly assume knowledge of the precise geometries and positions of all obstacles in the environment---an assumption that does not hold for general real-world settings where only sensed representations of the world may be available. Earlier work that checks for collisions between robot geometries and point clouds \[Schauer2015, Hornung2013, Pan2012a, Pan2013, Danielczuk2021, Murali2023\] attempts to lift this assumption, but point cloud collision checking remains a relatively slow bottleneck for motion planning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work \[Thomason2023VAMP, sundaralingam2023curobo, Vasilopoulos2023, le2024accelerating\] has produced new approaches to hardware-accelerated motion planning that exploit parallelism in collision checking and other core planning operations to find complete trajectories in microseconds to milliseconds. This use of parallelism motivates the need for higher-throughput parallelism-friendly algorithms and data structures for efficiently planning collision-free motions in environments that are only perceived as point clouds, *e.g.*, from a common depth camera like the Intel RealSense. \ use gpu parallelism to allow batched querying of an approximate Euclidean Signed Distance Field (esdf) built from a series of sensor measurements \[Millane2023\]; similarly, \ perform a gpu-parallel brute-force sdf computation between a discretized set of points on the robot geometry and a dense point cloud.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although these gpu-based methods are promising for some applications, data synchronization costs between the gpu and cpu limit the direct applicability of these techniques for motion planning algorithms, many of which are cpu-based. Further, for applications of field robotics such as planetary rovers, agricultural robots, and others, the power requirements of an onboard gpu may be untenable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a data structure and associated construction and search algorithms for *exact* point cloud distance computation and collision checking. Our proposed data structure, the *collision-affording point tree* (capt), adapts and refines concepts from the classical $k$-d tree to support efficient parallel evaluation. The core insights guiding our design of the capt are that exploiting the spatial correlation present in sbmp edge validation collision queries allows for aggressive early-termination of batched queries without sacrificing correctness, and that many motion planning problems (*e.g.*, in manipulation) only need to represent a relatively small, *local* part of the environment for collision checking. This first insight extends ideas from \; the second enables us to rethink traditional assumptions about minimizing memory overhead in point cloud representations: we in fact duplicate select subsets of points to create a parallelism-friendly data model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

By combining these insights with a machine-sympathetic data structure and the use of data-level parallelism, capts can return collision results against an observed 3D point cloud in a mean time of under ten nanoseconds per query on a single core of a consumer desktop cpu^11^1The point clouds used to generate these collision-checking throughput results contained up to 50000 points and had mean dispersions between 7$mm$ and 2.2$cm$. For detailed analysis, refer to the results in Sec. VI-A1 and Sec. -C; for examples of such point clouds, see Fig. 1(c) and Fig. 3(b).. Although we focus on cpu-based *single-instruction, multiple-data* (simd) parallelism in this paper, our approach also applies to and may benefit gpu-based planners using a *single-instruction, multiple-thread* (simt) parallelism model. the collision-affording point tree (capt), a novel data structure for storing sensed point clouds for collision checking. efficient construction, branch-free parallel query, and collision check algorithms for capts.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

a method for efficient point cloud down-sampling by exploiting properties of space-filling curves. proofs of correctness (*i.e.*, that using capts and our filtering algorithm does not modify planning problem feasibility). empirical evaluations for collision throughput and error against a set of competitive baselines. integration with a vectorized motion planner \[Thomason2023VAMP\], demonstrating the utility of capts for high-performance sbmp on a number of difficult and cluttered problems. a proof-of-concept demonstration with a depth camera and physical robot hardware. an open source implementation of capts^22^2Available at Figure 1: 1(a), 1(b): A cluttered tabletop scene, captured as RGB-D with an Intel Realsense D455 sensor. 1(c): The point cloud rendering of the same scene, filtered using our proposed space-filling curve method (Sec. IV-C).

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Planning from sensor data", "weight": 1.0} -->

Planning-amenable representations of sensor data usually take the form of some space-partitioning data structure. $k$-d trees \[Bentley1975\] are particularly relevant data structures for point cloud representation. They are often used for nearest-neighbor search in low-dimensional spaces \[Ram2019, Chen2019, Pinkham2020\], and allow for logarithmic-time collision-checking against points in a point cloud \[Schauer2015\]. These trees can also be augmented with a sphere covering \[Klein2004\] for efficient rejection of non-colliding geometry. Many efforts have been made to accelerate $k$-d tree queries by low-level optimization, including through parallel subtree search \[Chen2023a\] and dedicated instruction-set architectures \[E.Becker2023\]. flann \[muja2009flann, blanco2014nanoflann\] and Nigh \[ichnowski2018nigh\] are popular implementations of $k$-d trees; the former supports approximate nearest-neighbor search, while the latter is exact.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Planning from sensor data", "weight": 1.0} -->

The most popular approaches to representing sensor data for sbmp collision checking often use *occupancy maps* \[moravec_occupancy_1985, thrun1996integrating, Rusu2009\]. OctoMaps \[Hornung2013\] implement a probabilistic occupancy map using octrees \[meagher1982geometric\] of voxels, where each voxel is considered ?occupied? based on Bayesian updates computed upon each new point cloud inserted into the map. They allow for collision-checking based on bounding-volume hierarchies, which use a branch-and-prune search to limit the set of possible points for collision checking. OctoMaps are also integrated with collision checking libraries, *e.g.*, the Flexible Collision Library \[Pan2012a\], and popular planning frameworks such as MoveIt \[chitta2012moveit\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Planning from sensor data", "weight": 1.0} -->

They are a commonly used representation in practice, *e.g.*, for underwater vehicles \[VidalGarcia2019\], subterranean exploration \[dang2020graph\], autonomous vehicles \[badue2021self\], and aerial vehicles \[lu2018survey\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Planning from sensor data", "weight": 1.0} -->

Voxel-based approaches have also seen significant use recently due to many optimization-based planners \[Zucker2013, Vasilopoulos2023\] using signed distance fields for collision-checking---the representation of the signed-distance field is backed by a voxel representation \[Newcombe2011, Whelan2015\]. CuRobo \[sundaralingam2023curobo\] is an optimization-based planner which uses gpu parallelism for high-efficiency collision-checking, including against point clouds. It relies on the NVBlox \[Millane2023\] gpu-accelerated signed-distance field library for its collision-checking and optimization. VoxBlox \[Oleynikova2017\] and VoxGraph \[Reijgwart2020\] are also cpu-based sensor-based mapping tools for constructing signed-distance fields for collision-checking.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Planning from sensor data", "weight": 1.0} -->

Recently, there has also been interest in using implicit representations of the environment, such as neural radiance fields (n e rfs) \[Mildenhall2021\], which have been used for motion planning \[Adamkiewicz2022, Chen2023\]. However, constructing n e rfs, while relatively fast \[Mueller2022\], still take on the order of seconds to construct with gpu hardware, making them infeasible for online planning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Space-filling curves", "weight": 1.0} -->

Space-filling curves are continuous real bijections that map every point of a one-dimensional line to a higher-dimensional space, such as ${\mathbb{R}}^{3}$. Z-order curves \[morton1966computer\], also known as Morton curves, are a class of space-filling curve often used for nearest-neighbor applications. A point in a high-dimensional space can be projected onto a Z-order curve by interleaving the bits of the binary representation of its coordinates. If two points' projections onto the curve are close together, they are likely to also be near in the higher-dimensional pre-image space. \ used a Z-order curve to produce a low-discrepancy sub-sampling of a point cloud; however, their sub-sampling procedure does not guarantee that the overall point cloud structure is preserved. Likewise, \ used a Z-order sorting to accelerate construction of $k$-nearest-neighbor graphs by limiting their search to a single range of the space-filling curve.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C SIMD parallelism and planning", "weight": 1.0} -->

Parallel motion planning algorithms \[Thomason2023VAMP, sundaralingam2023curobo, Ichnowski2012, Plaku2005, amato_probabilistic_roadmap_1999, jacobs_scalable_method_2012, bialkowski_massively_parallelizing_2011, Pan2012, le2024accelerating\] require parallelizable collision-checking data structures. Further, to reap the benefits of early-termination in collision checking that enable simd-accelerated planning to plan at the microsecond scale, a simd-amenable data structure is required. However, the major data structures used in planning for sensor data representation are not amenable to this flavor of parallelism---hierarchical space-subdividing data structures (*e.g.*, OctoMaps, $k$-d trees, other voxel grids) require conditional-branch-heavy searches through large subtrees, which result in a highly sub-optimal memory access pattern: collision checks in these data structures must access potentially many fragmented segments of memory.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C SIMD parallelism and planning", "weight": 1.0} -->

Additionally, the branching nature of these searches makes them impractical to adapt to the branchless computation framework that simd parallelism best matches. To overcome these issues, we present a new data structure, designed with branchless, cache-friendly access in mind and demonstrate its effectiveness for efficient collision checking.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

capts redesign aspects of the classic $k$-d tree to make it amenable to high-throughput parallel querying for robot collision checking. The major problems with directly using a $k$-d tree for this purpose are cache-unfriendly random memory access patterns that arise from the tree's storage representation, and the inherently conditional-branch-heavy backtracking recursive algorithm used for normal $k$-d tree nearest-neighbor queries. Accordingly, the defining features of a collision-affording point tree, as opposed to a $k$-d tree, are its use of a memory layout that improves cache coherency during tree traversal, and that each leaf of a collision-affording point tree contains an *affordance set*, a conservative approximation of the possible nearest-neighbors to any point in the cell. This deceptively simple change allows the implementation of a search to avoid the backtracking stage of a search through a $k$-d tree, enabling branch-free, parallelism-friendly exact collision checking in a fraction of the time.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

To use a capt to check for robot collision, we first assume that the robot is made up of some set of spheres $S$ (as in other motion planning work, *e.g.*, \[Thomason2023VAMP, sundaralingam2023curobo, mukadam_continuoustime_gaussian_2018\]). Non-spherical robots can be approximated conservatively by constructing a spherical bounding volume hierarchy \[Bradshaw2004\] which contains all of their collision geometry. Let the smallest sphere of the robot's geometry have some known radius $r_{\text{min}}$ and the largest sphere of the robot's geometry have some known radius $r_{\text{max}}$. Then, given a query sphere with center $x$ and radius $r:{r_{\text{min}} \leq r \leq r_{\text{max}}}$, we can use the capt to check if the sphere is in collision. First, we search through the tree to find the leaf cell of the tree which contains $x$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method", "weight": 1.0} -->

If any point in the leaf's affordance set collides with the sphere, then the sphere is in collision; otherwise, the query sphere is not in collision.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Method", "weight": 1.0} -->

We begin by explaining the collision-affording point tree and its construction process in Secs. IV-A and IV-B. Next, we detail a point cloud filtering algorithm based upon space-filling curves in Sec. IV-C. Lastly, we describe our branch-free parallel collision-checking algorithm for capts in Sec. IV-D.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A The collision-affording point tree", "weight": 1.0} -->

In a capt, each leaf of the tree contains the affordance set for the leaf's corresponding cell, illustrated in Fig. 2. Given the cell $c$ corresponding to a leaf, that leaf's affordance set is the set of all points in $PC$ such that $c$ *affords* collision with $l$ at the radius $r_{\text{max}}$. A cell $c$ affords a point $p$ at radius $r$ if there exists some point $q \in c$ such that ${\|{p - q}\|} \leq r$, as depicted in Fig. 2(a). Intuitively, a point $p$ is afforded by a cell $c$ if a sphere of radius $r$ whose center is contained by $c$ could collide with $p$. Finally, each leaf is associated with a *second* axis-aligned bounding box. This bounding box is *not* the same as the cell; instead, it is the minimal bounding box containing all points in the leaf's affordance set, as shown in green in Fig. 2(a).

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A The collision-affording point tree", "weight": 1.0} -->

A capt is then the tuple $(T,A,P)$, such that the test sequence $T$ is an array of $n - 1$ test values in ${\mathbb{R}} \cup {\{\infty\}}$, $A$ is an array of $n$ axis-aligned bounding boxes over ${\mathbb{R}}^{k}$, and the affordance table $P$ is a ragged two-dimensional array of $n$ different affordance sets. This representation is *implicit*: the tree does not store any information about its branches other than in the test sequence $T$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A The collision-affording point tree", "weight": 1.0} -->

We arrange $T$ according to an Eytzinger layout, a class of array-backed implicit tree layout originally used for heaps \[williams1964heapsort\]. This layout reduces memory fragmentation by storing all data in a single contiguous block, and also improves performance by allowing for branch-free traversal. In such a layout, $T_{0}$ corresponds to the root branch of the tree: all points whose $x$-value is less than $T_{0}$ belong to the left sub-tree, while all others belong to the right sub-tree. Next, $T_{1}$ and $T_{2}$ correspond to the first branches in the left and right sub-trees about the $y$-value of each point.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A The collision-affording point tree", "weight": 1.0} -->

Recursively, if $T_{i}$ corresponds to a partition of the tree about the dimension $d$, then $T_{{2i} + 1}$ corresponds to the next branch in the left sub-tree, while $T_{{2i} + 2}$ corresponds to the next branch in the right sub-tree, both of which split on dimension ${d + 1}\operatorname{mod}k$. The value of $T_{i}$ at depth $d$ is the median value of $p{\lbrack{d\operatorname{mod}k}\rbrack}$ across all representative points $p$ in its sub-tree. Intuitively, each $T_{i}$ partitions the space by a new axis-aligned hyperplane, splitting the points in its subtree in half. For simplicity, we choose to partition on a repeating sequence of axes every time (first along the $x$-axis, then the $y$-axis, and so on), but could substitute other methods, such as randomly selecting an axis.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A The collision-affording point tree", "weight": 1.0} -->

Input: Point cloud PC containing n points of dimension k, minimum query radius rmin, maximum query radius rmax, axis-aligned bounding box c, affordance set z, uninitialized capt (T, A, P), index i, dimension index d 8 a← bounding box containing all points in PC; 13 Ti← median value of pd for all p ∈ PC; 17 shrink the upper bound of c1 on dimension d to Ti; 18 raise the lower bound of c2 on dimension d to Ti; 21 Construct(B1, rmin, rmax, c1, z1, (T, A, P), 2i + 1, (d + 1)mod k); 22 Construct(B2, rmin, rmax, c2, z2, (T, A, P), 2i + 2, (d + 1)mod k);

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Collision-affording point tree construction", "weight": 1.0} -->

To construct a capt, we apply the same recursive partitioning approach as in $k$-d tree construction, using quick-select \[hoare1961quickselect\] for an expected linear-time selection of the median value for each partition. The exact construction algorithm is specified in Alg. 1. At each step of the construction procedure, we retain two additional sets of information: the current cell $c$ and the current afforded set $z$. $c$ is initialized to the cell containing all of ${\mathbb{R}}^{k}$, while $z$ is initialized to the empty set. Every time we split the point cloud along a median plane, we split $c$ about the same median plane into two adjacent cells, $c_{1}$ and $c_{2}$. Next, we duplicate $z$ to produce two new affordance sets, $z_{1}$ and $z_{2}$. We expand $z_{1}$ to include all points in the cloud contained by $c_{2}$, and vice versa for $z_{2}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Collision-affording point tree construction", "weight": 1.0} -->

Finally, we filter out all points from $z_{1}$ which are not afforded by $c_{1}$, and likewise with $z_{2}$. This process can be thought of as maintaining the set of all points outside of a cell $c$ that are still close enough to $c$ that they may collide with a query sphere centered in $c$. Once each cell contains exactly one point, we determine the final affordance set of that cell's leaf as the union of the set containing the representative point and all points afforded by the leaf cell.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Collision-affording point tree construction", "weight": 1.0} -->

We can use knowledge of $r_{\text{min}}$ to prune the affordance set slightly more than the conservative approximation created by the construction procedure. If all points $x_{c} \in c$ are so close to the representative point $p$ that ${\|{x_{c} - p}\|} \leq r_{\text{min}}$, then all spheres with center $x \in c$ and radius $r \geq r_{\text{min}}$ will collide with $c$'s representative point $p$, as shown in Fig. 2(b). If this is the case, then there is no need to include any points outside of $c$ in the affordance set, since we know that any query sphere centered in $c$ is already in collision. Therefore, for these sufficiently small cells, we can simply store $\{ p\}$ as the affordance set, without including any other points.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

Not all points in an input point cloud are required for collision-checking, especially in extremely dense clouds, as there are many redundant points when conservatively approximating the colliding volume of the cloud. As the construction time of collision-affording point trees grows with the size of the point cloud, we introduce an efficient filtering procedure to significantly reduce the density of the cloud that also guarantees that it will not remove critical points.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

As the cloud is used for collision checking, it cannot remove a point $p$ unless there is another point $p^{\ast}$ in the cloud sufficiently close to $p$, such that $\|{p - p^{\ast}}\|$ is less than some threshold radius $r_{\text{filter}}$. This guarantees that the robot cannot penetrate further than $r_{\text{filter}}$ into the point cloud; alternately, all spheres of the robot may be padded by $r_{\text{filter}}$ to produce a conservative approximation of the cloud. Lastly, this filtering procedure must be computationally cheap: it must be significantly faster than the construction time of the capt to achieve any useful speedup.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

In order to verify that any removed point $p$ has a sufficiently close neighbor $p^{\ast}$, we must compute the distance between $p$ and $p^{\ast}$. A naive algorithm would compare every two points in $PC$, but this approach yields $O{(n^{2})}$ runtime, which is unacceptable for large point clouds. Instead, we reduce the candidate set of pairs by exclusively comparing points which are relatively near to one another, according to an arbitrary measure of locality.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

Space-filling curves (specifically in our implementation, Z-order curves \[morton1966computer\]) provide such a measure of locality: we use one to map all points in $PC$ to a one-dimensional space-filling curve. Once sorted in order of their position along the curve, points which are adjacent in the curve are also likely to be adjacent in their higher-dimensional space. Therefore, by exclusively checking the distance between neighboring points in the space-filling curve, we can dramatically reduce the point cloud size in $O{({n{\log n}})}$ time (Alg. 2).

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

However, nearby points in a higher-dimensional space are not guaranteed to be adjacent in a fixed space-filling curve. We mitigate this by checking for neighbors on multiple space-filling curves, one for each permutation of dimensions. If two points are near to each other, then it is likely that at least one such curve will place them adjacent to one another. Repeating the filtering process on each permutation of dimensions means that the filtering procedure scales with $O{({{k!}n{\log n}})}$, but for $k = 3$, there are only six such permutations, so the cost of extra filter checks is minimal compared to the savings in point cloud size.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

Input: list of points PC, filter radius rfilter Output: list of filtered points PC′ ⊆ PC 3foreach permutation X of dimensions do 5 sort PC′ along a Z-order curve by dimension order X; 8 if ∥PCi′ − PCj′∥ > r then Additionally, we filter out any points which we can prove will never be in collision with the robot. This process is simple for fixed-base arm robots: a point can only collide with a robot if its distance to the base link of the robot is less than the maximum extension length of the arm.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C Filtering", "weight": 1.0} -->

All together, this filter can achieve dramatic reductions in point cloud size even for small values of $r_{\text{filter}}$, filtering clouds with over a hundred thousand points to less than ten thousand in a few milliseconds. As shown in Fig. 3, relatively conservative values of $r_{\text{filter}}$ cull the point cloud by a dramatic amount; additionally, the filtering process significantly reduces point cloud density, reducing the expected colliding-set size and therefore improving tree construction and query times.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-D Collision querying", "weight": 1.0} -->

When collision-checking for a robot, a robot's configuration is valid only if all of the robot's physical geometry is not in collision with the environment. If any sphere of the robot's geometry is in collision with the environment, then the entire configuration is invalid. This provides us with an early-termination condition: we need only find a single colliding sphere to invalidate an entire configuration. By parallelizing collision checks across multiple query spheres, the entire search can terminate as soon as one collision is found.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-D Collision querying", "weight": 1.0} -->

The first step of a collision check is a search through the tree, as outlined in lines 1-7 of Alg. 3. Given some query sphere with center $x$ and radius $r$, the search begins with a test index $i = 0$ and dimension $d = 0$. Then, at each step of the search, if $x_{d} < T_{i}$, $i$ is updated to ${2i} + 1$, or ${2i} + 2$ otherwise, while $d$ is updated to ${d + 1}\operatorname{mod}k$. This is the same update rule for the Eytzinger layout as used during construction: index ${2i} + 1$ corresponds to the left sub-tree, while index ${2i} + 2$ corresponds to the right subtree. When the search completes, the final value of $i$ is an integer in the range $\lbrack{n - 1},{{2n} - 1})$, with each value corresponding to a unique leaf of the tree.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-D Collision querying", "weight": 1.0} -->

${i - n} + 1$ is an integer in the range $\lbrack 0,n)$ corresponding to each point stored at a leaf of the tree. This traversal can be performed branchlessly by converting the boolean value $x_{d} \geq T_{i}$ comparison into an integer $l$, assigning $i\leftarrow{{2i} + 1 + l}$. Since $n$ is a power of two, all traversals of the tree terminate in exactly the same number of iterations, and we do not need to test for reaching the end of the tree. Likewise, the memory access pattern of the traversal is extremely predictable: all accesses at a given iteration are restricted to a small set of possible values. The branchless traversal sequence allows for efficient simd parallelism: each lane of a single register contains a different test index, and each load, comparison, and index update is parallel, providing a large improvement in performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-D Collision querying", "weight": 1.0} -->

After determining which cell contains $x$, the search algorithm first performs an efficient collision check between the query sphere and the axis-aligned bounding box $A_{{i - n} + 1}$, which contains all points afforded by the cell. This step occurs in lines 8-9 of Alg. 3. This check does not change the final output of the search algorithm; instead, it simply filters out spheres which can be trivially proven not to collide with any points to reduce the number of expensive traversals through the affordance set. This step is once again parallelizable across multiple queries: for each simd lane of the processor, we can compute the distance from each query sphere to its leaf's bounding box in parallel instead of sequentially. During a parallel query, if spheres are not in collision with the bounding box, then they can be masked out from all remaining collision checks, reducing the overall search time. If no spheres in the query set collide with the axis aligned bounding box, then the query set is provably not in collision, and the search can terminate immediately.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-D Collision querying", "weight": 1.0} -->

Finally, the collision-checking procedure exhaustively checks for collision between the query sphere and all points $p \in P_{{i - n} + 1}$. If $x$ is nearer to any $p$ than $r$, then it is in collision. This step of collision-checking occurs in lines 10-13 of Alg. 3. We parallelize this step differently from the previous two: instead of parallelizing across the set of query spheres, we parallelize across the set of test points in each affordance set. This is all for cache locality: parallelizing across the test points means that all memory accesses are in the same contiguous region, instead of requiring inefficient gather instructions across multiple different affordance sets. Such parallelism would not be possible with a conventional $k$-d tree, as the set of possibly-colliding points is not known to the search until it explores each sub-tree.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-D Collision querying", "weight": 1.0} -->

Input: capt (T, A, P) containing n points in ℝk, sphere s with center x and radius r Output: Whether s collides with any point in the tree 12if Ai − n + 1 does not intersect s then

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Runtime", "weight": 1.0} -->

The runtime of the construction procedure is dictated by two sub-procedures: the partitioning of the space, which is the same as a $k$-d tree at $O{({kn{\log n}})}$ for a point cloud with $n$ points; and the construction of the final affordance set, which requires $O{({ka})}$ time for each point, where $a$ is the maximum size of an affordance set. Therefore the total runtime of construction is $O{({{kn{\log n}} + {kna}})}$. When the dispersion of the point cloud is high, $a$ tends to be small, so the construction runtime is $O{({kn{\log n}})}$. However, for extremely low-dispersion point clouds, all points in the point cloud are afforded by each cell, so $a = {O{(n)}}$, yielding a much larger construction runtime of $O{({kn^{2}})}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Runtime", "weight": 1.0} -->

In total, a capt consumes $O{({kna})}$ memory, which may be as much as $O{({kn^{2}})}$ for extremely low-dispersion clouds.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Runtime", "weight": 1.0} -->

In total, each collision query against the collision-affording point tree performs $O{({\log n})}$ comparisons while traversing the tree, then $O{(a)}$ checks evaluating the distance to each point $p \in P_{i}$, where $a$ is the maximum size of any affordance set $P_{i}$. Therefore the total search procedure requires $O{({{\log n} + {ka}})}$ steps.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

We benchmarked collision-checking throughput on an amd Ryzen™ 9 7950X cpu clocked at 4.5GHz against six different collision-checking and nearest-neighbor implementations. We compared against OctoMaps \[Hornung2013\], a voxel-based method, backed by fcl \[Pan2012a\]; Nigh \[ichnowski2018nigh\] and Nanoflann \[blanco2014nanoflann\], $k$-d tree implementations; gnat \[brin1995gnat\], a hyperplane partitioning tree (as implemented in the Open Motion Planning Library \[Sucan2012\]); and flann \[muja2009flann\], an approximate nearest-neighbor library. Our approach was implemented in C++ and integrated with an existing vector-accelerated motion planning framework \[Thomason2023VAMP\]. This planner represents the robot as a hierarchy of spheres, so all robot-environment collision-checking was performed using the capt. We also implemented a collision-checking backend using sequential queries against the tree.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

Here, sequential refers to collision checking each of the $n$ spheres packed into a simd vector sequentially, rather than using simd intrinsics to evaluate, thus demonstrating the benefits of simd parallelism. Sequential queries are used as well for Nanoflann and OctoMap collision checking.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

We benchmark planning performance on the challenging MotionBenchMaker \[chamzas2021mbm\] dataset, with 3 robots (the 6-d o f UR5, the 7-d o f Panda, and the 8-d o f Fetch) in 7 scenes (*table pick*, *table under pick*, *box*, *cage*, *bookshelf small*, *bookshelf tall*, and *bookshelf thin*) each, performing 100 different planning problems per scene.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments", "weight": 1.0} -->

All motion planning was performed on a single thread, using an implementation of a dynamic-domain \[Jaillet2005\] balanced \[kuffner2005balanced\] RRT-Connect \[Kuffner2000\] limited to 1 million iterations. All plans used the same sequence of randomly sampled configurations, so any difference in performance is from collision-checking speed, not from sampling order. All code was compiled with `clang 16.0.6` using the `-O3` compiler optimization level along with native cpu optimizations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-1 Collision query throughput", "weight": 1.0} -->

We began by evaluating collision-checking throughput on all of the possible backends. First, we recorded the set of all collision-checking queries made by a motion planner using ground-truth primitive geometry on each scene from the MotionBenchMaker \[chamzas2021mbm\] dataset. We then generated point clouds for each scene by uniform random sampling of the geometry's surface, then filtered each point cloud with $r_{\text{filter}} \in {\lbrack{1{mm}},{10{cm}}\rbrack}$ to reach a desired size. All collision-checking throughput experiments were performed on the same set of point clouds. Finally, we executed the exact same queries on each collision-checking method, recording the total timing for collision-checking and avoiding any other timing overhead from other steps in the motion planning process. capts were constructed with $r_{\text{min}} = {1{cm}}$ and $r_{\text{max}} = {8{cm}}$. OctoMaps were constructed with a resolution of 1$cm$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-1 Collision query throughput", "weight": 1.0} -->

FLANN indices were created with 4 $k$-d trees. All experiments were performed on a single cpu thread.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-2 Motion planning performance", "weight": 1.0} -->

We implemented full motion-planning backends using OctoMaps and NanoFLANN (as it had the the next-highest throughput, after capts, of any collision-checking method). Each backend was used as part of the same motion planning system, so all speedups are due to collision-checking speed, not sampling order or other aspects of planner efficiency. We compared the relative performance of $\text{capt}s$, using both sequential and parallelized simd queries, with these two backends. All point clouds were filtered with $r_{\text{filter}} = {2{cm}}$; although this filter radius is greater than that suggested by Lemma V.2, it was empirically tested to strike an appropriate balance between performance and fidelity, *i.e.*, not allowing invalid plans. See Sec. -A for further experiments on the effect of $r_{\text{filter}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-2 Motion planning performance", "weight": 1.0} -->

capts were constructed with $r_{\text{min}}$ and $r_{\text{max}}$ derived from robot geometry; $(r_{\text{min}},r_{\text{max}})$ was equal to $({1.5{cm}},{8{cm}})$, $({1.2{cm}},{6{cm}})$, and $({1.2{cm}},{5.5{cm}})$ for the UR5, Panda, and Fetch respectively. OctoMaps were constructed with a resolution of 1$cm$. Once again, these tests were performed exclusively on a single cpu thread to isolate per-thread performance; we leave thread-level parallelization to future work.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-A1 Collision query throughput", "weight": 1.0} -->

Fig. 4 presents timing results for capt construction times and average query throughput times for three different classes of tests: all-colliding queries are a set of queries where each sphere in the query set collides; non-colliding queries have no sphere in collision, and mixed queries are a mix of all-colliding, non-colliding, and partially-colliding queries. Queries against the point cloud were created by recording the set of all queries made by a motion planner in the scene, then recording the runtime of checking the same sequence of queries against each collision-checking system. We observe that capt construction is significantly slower than other tree-based nearest neighbor data structures, but is still faster than an OctoMap for construction on point cloud data. The construction procedure exhibits significantly superlinear scaling, showing that point cloud filtering is necessary to use a capt effectively.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-A1 Collision query throughput", "weight": 1.0} -->

Collision queries against the tree are overwhelmingly faster than any other data structure, running nearly ten times faster than the nearest data structures for collision checking, for an average performance of 9.89 nanoseconds per query---in comparison, the next best performing approach, Nanoflann, takes on average 309 nanoseconds per query. Remarkably, collision checks against an OctoMap are over three orders of magnitude slower than against a capt (averaging 0.01 milliseconds per query). This demonstrates a need for the field to reevaluate methods for planning with sensor data: it is possible to achieve extremely high performance gains with a different data structure.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-A2 Motion planning performance", "weight": 1.0} -->

Table I shows some critical statistics for filtering, collision checking data structure construction, planning, simplification, and total time for the 6-d o f UR5, 7-d o f Panda, and 8-d o f Fetch over the MotionBenchMaker dataset, as described above. These benchmarks show a dramatic improvement in performance over baseline approaches, with simd collision checking with a capt demonstrating planning times on par with the ground-truth primitive-based planner. For both the UR5 and Panda arms, the 95% quantile of total time end-to-end (filtering, building the capt, planning, and simplification) takes less than 16 milliseconds, faster than a 60FPS camera can refresh and provide a new pointcloud. We also highlight that capts provide such an enormous speedup that motion generation is no longer the most expensive step. Instead, other steps in the planning pipeline dominate planning times: point cloud filtering and capt construction account for the lion's share of planning time.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B Planning from real sensor data", "weight": 1.0} -->

Finally, we applied our planning system to point clouds observed from a real-world scene with an Intel RealSense D455 RGB-D camera. Fig. 1 shows an example of these data.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B1 Static scene", "weight": 1.0} -->

We first created a planning problem in a static snapshot of this scene, requiring a UR5 robot to move from its initial pose to a ?reach? point across the table. The original point cloud contained 166587 points; applying our space-filling curve filter (Sec. IV-C) with $r_{\text{filter}} = {2{cm}}$ reduced the cloud down to 2732 points. In this experiment, we used a minimum radius $r_{\text{min}} = {1.5{cm}}$ to match the geometry of our model of the UR5. As in Sec. VI-A2, we chose to use a larger $r_{\text{filter}}$ than suggested by Lemma V.2 because it empirically did not reduce plan quality; for timings with different values of $r_{\text{filter}}$, see Sec. -A. Running on the same machine as our other experiments, we observe a median planning time of 215 microseconds, with a simplified path returned in a total of 575 microseconds.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B1 Static scene", "weight": 1.0} -->

The total duration from the start of point cloud filtering through capt construction, planning, and simplification was a median of 7.166 milliseconds---corresponding to a complete planning rate of roughly 140Hz.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-B2 Dynamic scene", "weight": 1.0} -->

We additionally evaluated our planning system in a live control loop on the UR5, tasking it with moving between a sequence of preset goal waypoints while dodging unmodeled dynamic obstacles (*i.e.*, pool noodles moved by humans to obstruct the robot). Planned trajectories are passed to a simple velocity interpolation controller for time parameterization and execution, and are replaced and updated on every new point cloud. We observe that the system is able to plan at or above the 60FPS camera frame rate; qualitatively, this speed enables the robot to reactively dodge obstacles and effectively maneuver in the scene, despite a lack of motion forecasting or obstacle modeling. We report additional statistics on planning performance and point cloud properties for this experiment in Sec. -C; please also see the supplementary material for a video showing the robot in action.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Planning from sensor data is a crucial component of autonomous robotics. In this paper, we present a novel data structure for motion planning with observed point clouds, demonstrating an order-of-magnitude speedup compared to state-of-the-art techniques. We also present a unique filtering algorithm to reduce the density of a point cloud while still providing safety guarantees on collision detection. Combined, these two contributions enable a robot to plan from sensor data in milliseconds on a single CPU core, allowing the robot to plan faster than standard 60FPS camera refresh rates. This means that *robots can now use sampling-based motion planning in real time on purely sensed environments, using only general-purpose low-power hardware.* The primary limitation of a capt is that it is an immutable data structure. After construction, no points in the tree can be inserted or deleted. Since depth-camera images are streamed on a frame-by-frame basis, this is not a problem for collision-checking in dynamic environments, since we can reconstruct the capt from scratch for each frame. However, the capt's immutability precludes use of a capt for the state-space nearest-neighbor search required by most sampling-based planning algorithms.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future extensions to the capt structure could enable incremental updating, which would allow it to be used for nearest-neighbor search in the state space during sampling-based planning. Unlike OctoMaps \[Hornung2013\], the capt does not distinguish between free and unobserved space. This may be problematic for cluttered environments due to occlusions, and in future work we are interested in extending the capt to more directly model visibility and occlusion, as well as to better handle perceptual uncertainty by *e.g.*, modeling points as probabilistic particles.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As well, although our choice to duplicate potentially colliding points to construct the affordance sets enables capts to avoid branches and effectively exploit parallelism, it also limits their capacity for scaling to massive point clouds, such as those constructed by autonomous vehicles. In future work, we would be interested in exploring techniques for compressing or otherwise de-duplicating affordance sets. Perhaps more promising is the potential for using capts as a secondary collision data structure paired with another form of spatial subdivision, such as a spatial hash or voxel grid \[Oleynikova2017, Millane2023\]. This hierarchical fused data structure would allow a set of capts to each be "responsible" for only a local neighborhood of a large point cloud while maintaining efficient and parallelizable queries over the entire cloud.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, our performance results challenge conventional assumptions about the nature of planning. We have demonstrated that judicious application of parallelism and insights into the core problems of collision checking against sensor data enables extraordinary improvements in planning time, so much so that motion planning from sensor data could now be seen as a cheap primitive operation, instead of a time-consuming bottleneck.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Empirical impact of filter radii", "weight": 1.0} -->

We ran the simulated planning experiments from Sec. VI-A2 for the Panda robot with different values for the $r_{\text{filter}}$ parameter to Alg. 2 to investigate its effect on capt construction times, planning performance, and problem feasibility. These results are shown in Table IV. We note that, although the capt is sensitive to the value of $r_{\text{filter}}$ in its construction time in particular, even for conservative values of $r_{\text{filter}}$ (*e.g.*, matching or less than the bound suggested by Lemma V.2), our planning times are always faster than any baseline, and our total times are competitive or fastest. Note also that the baselines are only evaluated with the most aggressive value of $r_{\text{filter}}$, and would also be slowed in planning and total time for more conservative values. Finally, Table IV also validates that, for all values of $r_{\text{filter}}$, the paths we find are valid with respect to the exact, primitive geometric obstacles, evaluated post hoc.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Empirical dispersion of point clouds", "weight": 1.0} -->

We recorded the values of dispersion $\delta{(O,{PC})}$ as discussed in Lemma V.2 across the point clouds used for our simulation collision query throughput and planning performance experiments. We compute dispersion by using a standard nearest-neighbors data structure to query the distance to the closest neighbor of each point in each point cloud for each scene, and recording basic summary statistics, as shown in Table II. We note that $\delta{(O,{PC})}$ is often quite small for well-observed obstacles; further, as argued in the proof sketch for Lemma V.2, the increase in dispersion resulting from applying Alg. 2 is bounded by $r_{\text{filter}} + {\delta{(O,{PC})}}$. Therefore, selecting an $r_{\text{filter}}$ in the same order of magnitude as $r_{\text{min}}$ is a reasonable choice.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Real-robot planning experiments", "weight": 1.0} -->

We evaluate the impact of the value of $r_{\text{filter}}$ via the real-robot demonstration of planning with capts discussed in Sec. VI-B. We collected 300 observed point clouds from sequential frames of RGB-D video generated by an Intel Realsense D455 sensor, and computed the mean post-filter point cloud sizes and essential timing statistics (*i.e.*, timing for applying the filter, building a capt on the filtered point cloud, solving a motion planning problem with the capt, and simplifying the solution found---which requires further collision-checking) for a range of values of $r_{\text{filter}}$, keeping the values of $r_{\text{min}}$ and $r_{\text{max}}$ constant at 1.5$cm$ and 8$cm$ respectively. Table III shows these quantitative results, demonstrating that although capts remain fast at conservatively small values of $r_{\text{filter}}$, increasing $r_{\text{filter}}$ dramatically decreases both point cloud size and capt construction time.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Real-robot planning experiments", "weight": 1.0} -->

Crucially, we also qualitatively find that, for any $r_{\text{filter}} \leq {2{cm}}$, the generated trajectories are valid and do not intersect or contact any obstacles. As such, broadly speaking, a user can vary the value of $r_{\text{filter}}$ to trade fidelity of representation for performance, and reasonable balances of the two are easy to find.
