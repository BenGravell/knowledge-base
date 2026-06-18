<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

JZ-Tree: GPU Friendly Neighbour Search and Friends-of-friends with Dual Tree Walks in JAX plus CUDA

Topics include Clustering, Distributed systems, JZ-Tree, HPC, Tree traversal, Compute unified device architecture.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Algorithms based on spatial tree traversal are widely regarded as among the most efficient and flexible approaches for many problems in CPU-based high-performance computing (HPC). However, directly transferring these algorithms to GPU architectures often yields substantially smaller performance gains than expected in light of the high computational throughput of modern GPUs. The branching nature of tree algorithms leads to thread divergence and irregular memory access patterns - both of which may severely limit GPU performance. To address these challenges, we propose a Morton (z-order) 'plane-based tree hierarchy' that is specifically designed for GPU architectures. The resulting flattened data layout enables efficient dual-tree traversal with collaborative execution across thread groups, leading to highly coalesced memory access patterns. Based on this framework we present implementations of two important spatial algorithms - exact k-nearest neighbour search and friends-of-friends (FoF) clustering. For both cases, we observe more than an order-of-magnitude performance improvement over the closest competing GPU libraries for large problem sizes (N >~ 10^), together with strong scaling to distributed multi-GPU systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an open-source implementation, 'JZ-Tree' (JAX z-order tree), which serves as a foundation for efficient GPU implementations of a broad class of tree-based algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-performance computing (HPC) applications are increasingly shifting from CPU-based implementations to graphics processing units (GPUs). This shift is motivated both by the high arithmetic throughput and by the favorable energy efficiency of GPUs, which typically provide substantially more floating-point operations per unit power than conventional CPUs. Further, the reduction in execution time enables classes of applications that require not just a single large simulation, but a large number of repeated evaluations -- for example simulation-based inference. In addition, recent software frameworks such as jax make it possible to combine accelerator-based performance with just-in-time compilation, automatic differentiation, and a high-level programming model, which is particularly attractive for modern scientific applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, GPUs differ fundamentally from CPUs in how performance is achieved. GPUs follow a throughput-oriented parallel execution model with large numbers of lightweight threads, which differs significantly from the latency-optimized design of CPUs. As a consequence, many algorithms that are state-of-the-art on CPUs perform poorly when transferred directly to GPUs without redesign. Efficient GPU implementations typically require minimizing host-device communication, reducing global memory traffic, limiting thread divergence, and maximizing memory coalescence. In particular, coalesced memory access (illustrated in Figure 1) is a primary performance consideration, as memory transactions are shared across threads within a warp. Similarly, divergent control flow within a warp can significantly degrade performance, since threads executing different branches must be serialized. In practice, these constraints favor algorithms with regular control flow, predictable memory access patterns, and a limited number of synchronization points.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Tree-based data structures are a particularly important example of this challenge. On CPUs, trees are a standard tool for reducing the complexity of spatial search and interaction problems. They are used in nearest-neighbour search, friends-of-friends clustering, $N$-body methods \[3 force-calculation algorithm")\], multipole schemes, and many related algorithms. Yet on GPUs, tree methods are often much less competitive than their asymptotic complexity would suggest. Tree construction is frequently expensive, traversal tends to induce thread divergence, and the associated memory access patterns are often highly irregular. While iterative traversal schemes can reduce some forms of control-flow divergence, they generally do not eliminate divergence in the number of traversal steps taken by different threads. Further, conventional tree layouts make it difficult for neighbouring threads to read memory collaboratively, so that even moderate divergence in traversal may quickly destroy memory coalescence.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

In particular, nearest neighbour search has been studied extensively, and a wide range of algorithmic approaches have been proposed. Classical exact methods are typically based on spatial tree structures such as KD-trees or ball trees, which enable logarithmic query complexity in low dimensions. Variants of dual-tree traversal further improve efficiency by processing interactions between groups of nodes jointly. Closely related approaches based on uniform grids or cell lists are widely used in particle simulations, where the domain is decomposed into regular bins to enable efficient neighbour queries with predictable memory access patterns. On modern hardware, particularly GPUs, brute-force approaches based on dense distance evaluations have become increasingly competitive due to their regular memory access patterns and high arithmetic intensity. In addition, a large body of work has focused on approximate nearest neighbour (ANN) methods, including hashing-based techniques and product quantization, as well as graph-based approaches such as nearest-neighbour graphs and navigable small-world structures. These methods often achieve significantly improved query times at the cost of approximation error.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Finally, a notable recent advancement for exact neighbour search on GPUs is clover, a spatio-graph-based method that constructs an index of random Voronoi partitions to prune the search space while maintaining high hardware utilization, outperforming prior tree methods by an order of magnitude for some setups.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

In this work we propose a novel tree framework designed specifically to address the constraints of GPU architectures. The presented hierarchy is based on Morton, or $z$-order, sorting and can be constructed efficiently in a bottom-up fashion. Rather than producing a deeply nested binary tree with irregular traversal depth, the construction yields a hierarchy of tree-planes with fixed and small depth. This makes tree walks highly predictable and allows them to be implemented through a small number of kernel launches. In addition, the hierarchy is organized such that the children of a node are stored contiguously and may be accessed with fully coalesced memory reads. Combined with a dual tree walk formulation, this allows interactions between groups of nodes to be processed collaboratively, reducing redundant memory access compared to more conventional traversal schemes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We demonstrate the benefits of the framework with two algorithms, $k$-nearest neighbour search and friends-of-friends (FoF) clustering. For both cases, we find significant performance improvements over the closest competiting libraries, reaching more than an order of magnitude improvement for sufficiently large problems. The presented framework is not specific to these two use cases. The same tree representation and traversal strategy can be extended naturally to a range of other tree-based algorithms, including density-based clustering methods such as DBSCAN, fast multipole methods, and correlation function estimation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

Our main optimization target is for low dimensions ($d \sim 3$), and large point counts $N \gg 10^{6}$ -- a regime that is highly relevant for many HPC simulation codes. We are less concerned with very high-dimensional settings or with small problem sizes, although we will show that the presented methods remain competitive outside of the primary target regime as well. Here, we only consider a Euclidean distance measure, but including other distance measures in the future would be viable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The remainder of this paper is structured as follows. In Section II we introduce the $z$-order based tree construction. We then describe the nearest neighbour algorithm and evaluate its performance in Section III and the FoF algorithm in Section IV. Finally, we conclude in Section V.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The publication is accompanied by an open-source implementation of the presented algorithms named 'jz-tree' (short for jax z-order tree) that is available on GitHub^11^1 and PyPI^22^2 with additional documentation and usage examples under^33^3

<!-- chunk {"id": "body-0014", "role": "body", "section": "Z-order trees", "weight": 1.0} -->

We construct a tree in two steps: A sort of the input position array in Morton / z-order and A search for splitting points on the position array to summarize points (and nodes) into coarser nodes. Both steps involve only GPU friendly operations on flat arrays so that the tree construction is significantly faster on GPUs than widely used top-down construction methods of KDTrees.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Z-order trees", "weight": 1.0} -->

We note that Peano-Hilbert (PH) order is often considered superior to z-order in terms of spatial locality. However, we prefer z-order here due to its simplicity and flexibility. In particular, z-order can be defined directly for all floating-point coordinates without requiring a predefined domain or refinement level. In contrast, PH order is typically constructed on discretized grids and becomes more complex to generalize across dimensions or to arbitrary floating-point data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

The most common and fastest approach to sorting position vectors in z-order is to sort by an integer key obtained by interleaving the bits of the coordinate components (Morton encoding ). However, for floating-point positions, defining such a key requires restricting the domain and truncating precision. An alternative approach is to define a custom comparison operator that directly compares full position vectors and to use a sorting algorithm that supports custom comparators, such as mergesort. Here, we adopt this approach, as it provides maximum generality -- allowing the construction of tree structures at full floating-point precision. As we show later, the associated performance overhead is negligible, since sorting is not a bottleneck in the presented algorithms.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

To define this comparison operator, let us assume that we have a function $\text{msb}_{\text{fixed}}$ available that extracts the most significant differing bit of two positive fixed-point numbers (normalized to exponent $0$). For example, for two numbers $a$ and $b$

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

the most significant differing bit is the first bit at which the two representations differ after their common prefix. We label bits by the power of two that they represent so that $\text{msb}_{\text{fixed}}$ would return $3$ in the example above. Such a function can easily be implemented by counting leading zeros on a bitwise exclusive or of $a$ and $b$. Given the function $\text{msb}_{\text{fixed}}$ we may define a more general function msb that acts on floating point numbers to extract the most significant bit that would differ if they were normalized as fixed point numbers with exponent 0.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

where EMAX is one larger than the maximum exponent value (e.g., $128$ for float32 and $1024$ for float64 in IEEE 754 standard ). The function msb can be implemented efficiently using bitwise operations (bit shifts and leading-zero counting), with special care required to handle subnormal numbers, where the mantissa representation differs from normalized values.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

where argmax selects the first occurrence of the maximum -- so that differences in earlier coordinates are more significant than those in later coordinates.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

In Figure 2 we show two examples of the z-sorted points on a regular grid (left) and for a uniform random distribution (right). For a regular grid, the traversal follows the characteristic Z-shaped (Morton) pattern.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

In jz-tree the z-order sort is implemented via a library call to the mergesort routine of the CUB library. For multi-GPU execution, we employ a sampling-based partitioning approach. In a first step, a subset of $N_{samp} \sim 1000$ points is sampled on each GPU, collected, sorted on a single device and broadcasted. Based on the sorted samples, a set of splitters is chosen such that the sampled points are evenly partitioned. Subsequently, all points are redistributed across GPUs according to these splitters and sorted locally, resulting in a globally consistent z-order.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Z-order sort", "weight": 1.0} -->

Assuming no duplicate keys, the expected relative imbalance scales as $O{(\sqrt{{\log{(N_{GPU})}}/N_{samp}})}$, leading to imbalances well below $10\%$ in all scenarios that we consider here. After sorting, domain boundaries can be adjusted for perfect load balance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Nodes", "weight": 1.0} -->

We define a node with center $\mathbf{c}$ and Morton level $\mathbf{l}\mathbf{v}\mathbf{l}$ as the set of all points whose hypothetically interleaved binary representations share the leading bits up to $\mathbf{l}\mathbf{v}\mathbf{l}$ with $\mathbf{c}$. Such a node corresponds to a contiguous segment in z-order.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Nodes", "weight": 1.0} -->

Given two points ${\mathbf{p},\mathbf{q}} \in {\mathbb{R}}^{d}$, let $k$ denote the dimension in which they differ most significantly in the Morton sense. The corresponding Morton level is

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Nodes", "weight": 1.0} -->

where the offset by one accounts for the fact that the common interval is larger than the position of the highest differing bit. We may further define per-dimension extent levels

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Nodes", "weight": 1.0} -->

so that $L_{i} = 2^{l_{i}}$ corresponds to the spatial extent of the node in the $i$th component and $2^{lvl}$ corresponds to the volume of a node. Extent levels may differ at most by one across dimensions, so that nodes can be rectangular with axis ratios of at most two.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

As a first step to constructing a tree hierarchy we calculate

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

for each consecutive pair of points $i - 1$ and $i$ in the sorted array. To simplify later calculations, we assume the existence of an additional vector with $- \infty$ components at index $- 1$ and $+ \infty$ components at index $N$, so that we obtain $N + 1$ values for $N$ points. It is useful to interpret these level values as being associated with the gaps between consecutive points (see Figure 3).

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

As a next step, we determine the range of points contained in the smallest node that includes points $i - 1$ and $i$. To this end, we perform a binary search to the left to find the smallest index $l_{b}$ that would be part of such a node

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

and a binary search to the right to find the smallest index $r_{b}$ that would be outside

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

If no such indices exist, we set $l_{b} = 0$ and $r_{b} = N$. The number of points contained in the node is then $n = {r_{b} - l_{b}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

The information contained within $l_{b}$ and $r_{b}$ is in principle sufficient to define a full binary tree, where the parent of each node is given by $l_{b}$ or $r_{b}$ depending on which one has the lower level ${argmin}{({lvl}_{l_{b}},{lvl}_{r_{b}})}$. However, walking such a binary tree on GPU architectures would lead to poor memory coalescence, since different threads may access very different locations in memory. We therefore choose a different approach here, where we allow nodes to have a variable number of children, but keep the depth of the resulting tree fixed.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

We define a *tree-plane* as a set of nodes that partitions the points $\mathbf{x}$, such that each point belongs to exactly one node (while empty regions of space may remain uncovered). A tree-plane may be parameterized through a set of $N_{{nodes} + 1}$ splitting points $\mathbf{s}\mathbf{p}\mathbf{l}$ in the z-order index space so that a node $i$ contains all points in the range $\lbrack{spl}_{i},{spl}_{i + 1})$. Recall that $n_{i}$ is the number of points that would need to be included in a node that contains points $i - 1$ and $i$. We construct a tree-plane by selecting all separation points with $n > N_{\max}$. Intuitively, each tree-plane partitions the points into the largest possible Morton cells subject to the constraint that each cell contains at most $N_{\max}$ points.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

In Figure 3 we illustrate the splitting points ${\mathbf{s}\mathbf{p}\mathbf{l}}^{}$ of leaf nodes created this way with $N_{\max}^{} = 2$ which we refer to as the '0th plane'.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

We may construct coarser tree-planes iteratively by applying the same procedure to the splitting points of the previous plane. That is, we retain only those splits between nodes of plane $p$ for which $n$ exceeds $N_{\max}^{({p + 1})}$. In Figure 4 we show an example of two tree-planes that are obtained with $N_{\max}^{} = 4$ and $N_{\max}^{} = 8$ for a uniform random distribution on a two-dimensional domain in the range $\lbrack{- 1},1\rbrack$ with $N = 100$ points.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

Space that doesn't contain points may or may not be part of a tree-node.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

Some nodes may only contain a single point and have zero extent.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

Nodes on the coarser plane may contain a flexible number of nodes of the finer plane.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

Some nodes on the coarser plane may have themselves as their own only child on the finer plane.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

Different children may have different extent.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

The tree has the same fixed depth everywhere.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

with defaults $N_{\max}^{} = 48$ and $c = 8$ which we find to be good choices performance wise. If we wanted to end up with a single root node, we could keep coarsening until $N_{\max}^{(p)} \geq N$ at which point we'd be guaranteed to have a single node that covers all points. However, on GPUs it is preferable to have a coarsest level that has already a notable number of nodes so that most streaming multiprocessors have work to do from the beginning. We define a target number $N_{target}$ (typically of order 1000) that we aim to obtain at the coarsest level.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

This typically overestimates the number of nodes, but it is not a strict upper bound, since in z-order a single high-$n$ node may block multiple low-$n$ nodes from merging. We stop coarsening when the estimated number of nodes is smaller than $N_{target}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "II-C Plane based tree-hierarchy", "weight": 1.0} -->

In jz-tree the distributed tree-construction is implemented in four steps: We first adjust the domain to ensure that no node of the coarsest tree-plane crosses domain boundaries. This is achieved by determining how far a node at a given Morton level would extend across the domain boundary. The domain then needs to be adjusted to the starting or end point of the largest node that contains $\leq N_{\max}^{({last})}$ points. The subsequent tree construction can be treated fully locally from this point. We extract leaf splitting points $N_{\max}^{}$ by checking where splitting points exceed $N_{\max}^{}$ through a range search of $N_{\max}^{}$ to the left and right of each splitting point. This step is optional, but tends to be faster for the leaf level than a binary search. We then determine $n$ for each leaf splitting point through the earlier described binary search and Extract splitting points for the full hierarchy.

<!-- chunk {"id": "body-0046", "role": "body", "section": "II-D Regularization", "weight": 1.0} -->

For many problem setups (e.g. uniform random distributions or particle distributions from cosmological simulations), the described tree structure is sufficient. However, for distributions that contain a small number of points far from the bulk -- e.g. multivariate Gaussian distributions -- summarizing nodes solely based on the number of contained points may produce a small number of nodes with very large extent. This is problematic for nearest-neighbour search, where at least a region of size comparable to the node must be explored, which in the worst case can include almost all points.

<!-- chunk {"id": "body-0047", "role": "body", "section": "II-D Regularization", "weight": 1.0} -->

To improve performance in such scenarios, we introduce a simple regularization criterion. For each tree-plane $p$, we define a global maximum level ${lvl}_{\max}^{(p)}$ and retain all splitting points whose level satisfies ${lvl} > {lvl}_{\max}^{(p)}$. Intuitively, this prevents the formation of excessively large nodes in low-density regions by enforcing a global upper bound on node size. We define this maximum level so that the volume $V_{\max}^{(p)} = 2^{{lvl}_{\max}^{(p)}}$ of nodes never exceeds

<!-- chunk {"id": "body-0048", "role": "body", "section": "II-D Regularization", "weight": 1.0} -->

where we typically choose $f_{\max} \sim 50$. Here, $V_{90\%}^{(p)}$ denotes the point number weighted average volume of nodes on plane $p$, computed over the subset of smallest nodes that together contain $90\%$ of all points. This excludes a small number of very large nodes that may otherwise dominate the average.

<!-- chunk {"id": "body-0049", "role": "body", "section": "II-D Regularization", "weight": 1.0} -->

For the scenarios considered in this work, this simple regularization scheme is sufficient. However, we leave the possibility of incorporating more sophisticated techniques in jz-tree for future work.

<!-- chunk {"id": "body-0050", "role": "body", "section": "II-E Multiple point types", "weight": 1.0} -->

Some algorithms require treating multiple point types separately in the tree. For example, in nearest-neighbour search, one may wish to query the tree using a set of query points $\mathbf{x}_{query}$ distinct from the source points $\mathbf{x}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "II-E Multiple point types", "weight": 1.0} -->

The most common approach is to construct a separate tree for the query points and to treat query and source trees explicitly during the dual tree walk. However, this increases implementation complexity and may lead to suboptimal refinement, as the query tree is constructed independently of the source distribution.

<!-- chunk {"id": "body-0052", "role": "body", "section": "II-E Multiple point types", "weight": 1.0} -->

Instead, we construct a single tree jointly over all point types. This is achieved by concatenating the positions of all types into a single array prior to the $z$-order sort. During tree construction, we track the point counts of each type separately for every candidate node. Splitting points are then chosen such that the maximum count over all types does not exceed $N_{\max}^{(p)}$ for any node on tree-plane $p$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "II-E Multiple point types", "weight": 1.0} -->

After construction, points are separated again into type-specific arrays while preserving $z$-order. Only the leaf-level splits ${\mathbf{s}\mathbf{p}\mathbf{l}}^{}$ are defined separately for each type. This enables coalesced memory access within each species while maintaining a shared tree structure that adapts to all point distributions and keeps the tree traversal simple.

<!-- chunk {"id": "body-0054", "role": "body", "section": "II-F jax implementation details", "weight": 1.0} -->

Most computationally intensive parts of our implementation are realized as CUDA kernels, invoked via the foreign function interface (FFI) of jax. To maintain compatibility with jax's just-in-time (JIT) compilation, all memory allocations must have statically known sizes at jit-compile time.

<!-- chunk {"id": "body-0055", "role": "body", "section": "II-F jax implementation details", "weight": 1.0} -->

Since the number of nodes per tree-plane is data-dependent, we allocate one contiguous buffer for each node property (e.g. splitting points, particle counts, node centers, node levels) and store all tree-planes within this buffer using data-dependent offsets.

<!-- chunk {"id": "body-0056", "role": "body", "section": "II-F jax implementation details", "weight": 1.0} -->

The required allocation size is estimated as

<!-- chunk {"id": "body-0057", "role": "body", "section": "II-F jax implementation details", "weight": 1.0} -->

where typically $\text{alloc\_fac\_nodes} \sim {1\text{–}2}$ is sufficient in practice. If the allocated size is insufficient, a runtime error is raised indicating the required increase.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Nearest neighbour search", "weight": 1.0} -->

We describe how to implement a $k$-nearest neighbour search based on the plane-based tree hierarchy that we have described in Section II. The neighbour search happens conceptually in two steps: A dual tree walk on the tree hierarchy to determine per leaf an interaction list of other leaves that need to be checked to guarantee that all candidate neighbours required for an exact $k$-nearest neighbour search are considered. A neighbour search that traverses the leaf-leaf interaction list collaboratively among points in the same leaf.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-A Interaction lists", "weight": 1.0} -->

We parameterize an interaction list as a tuple ${\mathbf{i}\mathbf{l}\mathbf{i}\mathbf{s}\mathbf{t}} = {({\mathbf{i}\mathbf{s}\mathbf{r}\mathbf{c}},{\mathbf{i}\mathbf{s}\mathbf{p}\mathbf{l}})}$ of two arrays: a set of source indices $\mathbf{i}\mathbf{s}\mathbf{r}\mathbf{c}$ and a set of splitting points $\mathbf{i}\mathbf{s}\mathbf{p}\mathbf{l}$. The interaction list is sorted by receiving nodes so that a receiving node $i$ has to interact with the $\mathbf{i}\mathbf{s}\mathbf{r}\mathbf{c}$ indices in the range from ${ispl}_{i}$ up to ${ispl}_{i + 1} - 1$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-A Interaction lists", "weight": 1.0} -->

A dense interaction list where every node out of $N_{nodes}$ interacts with every other node can be initialized as

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

0: For each plane p = 0, …, P − 1: node splits spl(p), source point count n(p), node centers c(p), and Morton levels lvl(p). Source positions x and leaf splits spl. Query positions xq and splits splq.
1: spl(P) ← Range (0,Ntopnodes,NGR)
2: ilist ← DenseInteractionList (⌈Ntopnodes/NGR⌉)
4: ilist ← NodeToNode (ilist,spl(p+1),n(p),c(p),lvl(p))
6: return LeafToLeaf (ilist,spl,x,splq,xq)
Algorithm 1 Dual tree walk for nearest neighbour search

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

We sketch the necessary steps for the dual tree walk in Algorithm 1. As a first step, we group the top level nodes into 'pseudo' super nodes where NGR denotes the grouping size. This grouping is necessary because an entry in the interaction list represents interactions between all children of the receiving node and all children of the source node. Grouping ensures that this assumption remains valid at the top level. A dense interaction list is then initialized on these super nodes so that effectively every top-node will interact with every other top-node. The precise value of NGR is not critical and we typically choose $\text{NGR} = 32$. Subsequently, we evaluate a node-node interaction function on every plane to move the interaction list from plane $p + 1$ to $p$ and finally evaluate the leaf-leaf interaction list.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

Given two nodes with centers $\mathbf{c}_{1}$ and $\mathbf{c}_{2}$ and per-dimension extent vectors $\mathbf{L}_{1}$ and $\mathbf{L}_{2}$ (that may be calculated from the Morton level $\mathbf{l}\mathbf{v}\mathbf{l}$), we can define a lower distance $d_{low}$ and an upper distance $d_{up}$ as

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

It is guaranteed that every point in node 1 includes all points from node 2 at a radius $R_{\max} \geq d_{up}$. Further, it is guaranteed that no point of node 2 lies within a radius smaller than $d_{low}$ from any point in node 1. We can therefore use $d_{up}$ to find guaranteed upper bounds for the radius in which neighbours need to be checked and $d_{low}$ for efficient pruning of interactions.

<!-- chunk {"id": "body-0065", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

0: Interaction list ilist, node splits spl(p+1), point count n(p), centers c(p), and Morton levels lvl(p).
1: Rmax ← FindRmax (ilist,spl(p+1),n(p),c(p),lvl(p))
2: icount ← Count (ilist,spl(p+1),c(p),lvl(p),Rmax)
3: ispl ← CumulativeSumPrep0 (icount)
4: isrc ← Insert (ilist,spl(p+1),c(p),lvl(p),Rmax,ispl)
5: return Interaction list (isrc,ispl)
Algorithm 2 Node to Node interaction function.

<!-- chunk {"id": "body-0066", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

The node-to-node interaction function is sketched in Algorithm 2. It works in four steps, each of which requires a separate kernel launch: Determine for each node a maximum radius $\mathbf{R}_{\max}$ that guarantees that it contains the k-th nearest neighbour of all points inside the node. For each node, count the number of nodes for which $d_{low} \leq R_{\max}$. Calculate the cumulative sum (and prepend 0). Insert the interaction source indices using $\mathbf{i}\mathbf{s}\mathbf{p}\mathbf{l}$ as relative offsets in the array.

<!-- chunk {"id": "body-0067", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

Steps, and share very similar traversal logic, so we will only discuss step in detail to highlight how the presented data structures can be used to define a CUDA kernel with a good memory access pattern. The prefix sum in step can be implemented through a library call to CUB.

<!-- chunk {"id": "body-0068", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

0: par_i, (isrc,ispl) = ilist, spl(p+1), n(p), c(p), lvl(p)
1: for group step node_i = spl [par_i] up to spl [par_i + 1] − 1 do
2: read node data of node_i into registers
3: H← empty neighbour heap with counts
4: for int = ispl [par _ i] up to ispl [par _ i + 1] − 1 do
5: par_j ← isrc [int]
6: read node data in range spl [par_j] … spl [par_j + 1] − 1 into shared memory
7: for node_j = spl [par_j] up to spl [par_j + 1] − 1 do
8: r ← dup (node _ i,node _ j)
10: insert (r,n [node _ j]) into H
14: Rmax [node_i] ← RadiusOfCount (H,k)
Algorithm 3 Conceptual outline for FindRmax kernel.

<!-- chunk {"id": "body-0069", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

The kernel for determining $R_{\max}$ is outlined in Algorithm 3. Each thread block is assigned a parent node $\text{par}_{i}$, determined by the CUDA block index. The outer loop assigns child nodes $\text{node}_{i}$ of the parent $\text{par}_{i}$ to individual threads. If the number of children exceeds the number of threads, multiple iterations are required. Subsequently, the interaction list is traversed over source parent nodes par_j. To minimize global memory access, the data of all child nodes of $\text{par}_{j}$ is loaded collaboratively into shared memory. Finally, the loop in line 7 iterates over all child nodes (for each thread) to insert the upper node-node distance into the neighbour heap $H$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

The heap data structure $H$ is implemented fully in registers -- following. It keeps track of a static number of $N_{r}$ distances and counts. RadiusOfCount gives a preliminary estimate of $R_{\max}$ as the smallest radius for which the cumulative count exceeds or equals $k$. If the total count is smaller than $k$, this estimate is set to $\infty$. New entries are inserted into the heap to maintain order, discarding the last element. However, if discarding the last element would lead to the heap holding a total count smaller than $k$, then we instead add the new count to the first element with larger radius.

<!-- chunk {"id": "body-0071", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

The memory access pattern of the FindRmax kernel is ideal for GPU architectures: The global memory accesses in line 2 and line 6 are perfectly coalesced. Further, evaluating interactions between the parent nodes requires only reading each of their children once. This significantly reduces memory access compared to conventional tree walks based on Euler tours where such interactions may be encountered at separate points in time. However, it is worth noting that some threads may be idle if the number of children in par_i is smaller than the number of threads in the group. E.g. if we choose a coarsening factor of $8$, we'd expect typical nodes to have 8 children which is notably smaller than the minimal number of threads in a group of $32$. In principle, this aspect could be further optimized by assigning multiple threads to the same node and then collaboratively inserting neighbours into a joint heap among those threads. However, we do not attempt this optimization here, because it is only a minor concern for leaf-leaf interactions (where $N_{\max}^{} \sim {32 - 64}$) which tend to dominate the cost of the neighbour search.

<!-- chunk {"id": "body-0072", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

The Count and Insert kernels follow the same structural pattern, but instead of maintaining a heap, they simply count the number of node-node interactions with ${d_{low}{(\text{node\_i},\text{node\_j})}} \leq R_{\max}$ and insert the corresponding node_j indices into the interaction list.

<!-- chunk {"id": "body-0073", "role": "body", "section": "III-B Dual Tree Walk", "weight": 1.0} -->

Finally, the implementation of the LeafToLeaf kernel is again similar to the FindRmax kernel. In this case the outer loop runs over query points (assigning one query point per thread) and the inner loop runs over source points. The neighbour heap structure in this case keeps track of $k_{\max}$ radii and point indices that are written out at the end of each query point iteration. To limit register pressure we choose $k_{\max} \leq 32$ and call the kernel multiple times if $k > k_{\max}$, filtering additionally by a minimum radius $R_{\min}$ (and an equality breaking index offset) that excludes points that were found in previous iterations.

<!-- chunk {"id": "body-0074", "role": "body", "section": "III-C Multi-GPU", "weight": 1.0} -->

Adapting the presented algorithm to multi-GPU scenarios is relatively straightforward. The main idea is that each GPU maintains the local receiving nodes and their corresponding interaction list. Remote source nodes that need to be interacted with are requested once for the evaluation of each plane.

<!-- chunk {"id": "body-0075", "role": "body", "section": "III-C Multi-GPU", "weight": 1.0} -->

Concretely, the main required additions are as follows: We need to additionally store a tuple of two arrays ${\mathbf{o}\mathbf{r}\mathbf{i}\mathbf{g}\mathbf{i}\mathbf{n}} = {({\mathbf{r}\mathbf{a}\mathbf{n}\mathbf{k}},{\mathbf{i}\mathbf{d}\mathbf{x}})}$ that saves the origin rank and index for each (unique) source node that appears in the interaction list. When initializing the dense interaction list and super nodes in lines 1-2 of Algorithm 1, $N_{topnodes}$ includes all (local or remote) top-nodes and $\mathbf{o}\mathbf{r}\mathbf{i}\mathbf{g}\mathbf{i}\mathbf{n}$ must be initialized appropriately.

<!-- chunk {"id": "body-0076", "role": "body", "section": "III-C Multi-GPU", "weight": 1.0} -->

Before line 4 in Algorithm 1 the remote child data $\mathbf{n}^{(p)}$, $\mathbf{c}^{(p)}$, ${\mathbf{l}\mathbf{v}\mathbf{l}}^{(p)}$ must be requested for each remote $\mathbf{o}\mathbf{r}\mathbf{i}\mathbf{g}\mathbf{i}\mathbf{n}$. The corresponding remote splits ${\mathbf{s}\mathbf{p}\mathbf{l}}^{({p + 1})}$ must be communicated as well. The received data is then rearranged such that ${\mathbf{s}\mathbf{p}\mathbf{l}}^{({p + 1})}$ correctly indexes contiguous locally available memory.

<!-- chunk {"id": "body-0077", "role": "body", "section": "III-C Multi-GPU", "weight": 1.0} -->

In addition, $\mathbf{o}\mathbf{r}\mathbf{i}\mathbf{g}\mathbf{i}\mathbf{n}$ is propagated to the child level. After line 4 in Algorithm 1 all source indices that appear 0 times in the final interaction list can be removed from $\mathbf{o}\mathbf{r}\mathbf{i}\mathbf{g}\mathbf{i}\mathbf{n}$. Before line 6 of Algorithm 1 we need to do a similar request of leaf splits and source point data.

<!-- chunk {"id": "body-0078", "role": "body", "section": "III-C Multi-GPU", "weight": 1.0} -->

The strength of this approach is that remote source nodes required for interactions are requested only once, the number of communication points in the algorithm remains small and predictable and the remaining functions remain exactly identical to the single-GPU case. In the scenarios that we have tested, we find that the additionally required remote data is O(10% - 60%) of the local receiving node data with a notable dependence on the problem setup and the number of source points per GPU (more data tends to imply better balance). Since it is difficult to foresee all the complications that may arise with more complicated setups and at very large GPU counts, we consider the distributed kNN implementation in jz-tree to be experimental and preliminary.

<!-- chunk {"id": "body-0079", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

We enhance the presented algorithms with an additional component that allows more efficient early pruning in the iteration through interaction lists. For each interaction we additionally store the interaction radius $\mathbf{r}_{low}$ -- corresponding to the lower node-node distance of the interaction. For each receiving node we sort $\mathbf{r}_{low}$ (after line 4 in Algorithm 2) using a bitonic sort network applied to the corresponding segments. We simply initialize these radii to $0$ at the top-node level.

<!-- chunk {"id": "body-0080", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

This improves the performance for two reasons: Since close-by interactions are encountered earlier, the preliminary estimate of $R_{\max}$ in Algorithm 3 is better and more candidate radii can be discarded early (rather than triggering a more expensive insertion into the neighbour heap). It allows to define an early exit after line 5 of Algorithm 3 and all other kernels that follow a similar structure: If the maximum current estimate of $R_{\max}$ across all threads is smaller than $\mathbf{r}_{low}$, we can discard all remaining interactions. In practice, this prunes on the order of $50\%$ of evaluated interactions.

<!-- chunk {"id": "body-0081", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

Finally, we note again that we need to predict allocation sizes at compile time to enable jit-compilation in jax. The main additional allocation that we need to predict here is the size of the interaction list source indices $\mathbf{i}\mathbf{s}\mathbf{r}\mathbf{c}$ (and radii $\mathbf{r}_{low}$).

<!-- chunk {"id": "body-0082", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

For $d = 3$ dimensions, we find that $\text{alloc\_fac\_ilist} \sim 200$ is typically enough, but we note that it is advisable to choose slightly larger values to decrease the chance that the jit-compiled function needs to be aborted due to insufficient available space.

<!-- chunk {"id": "body-0083", "role": "body", "section": "III-D Implementation Details", "weight": 1.0} -->

Our primary focus in this article is to optimize performance and memory coalescence to point out a path forward to more GPU friendly tree algorithms. However, it is worth noting that the approach at hand does come at a notable memory cost: With $N_{\max}^{} \sim 48$ and ${{alloc}\_{fac}\_{ilist}} \sim 200$ the $\mathbf{i}\mathbf{s}\mathbf{r}\mathbf{c}$ and $\mathbf{r}_{low}$ arrays each require the allocation of about $10 \cdot N$ integer / floating point numbers. If only a small number of neighbours $k \lesssim 10$ is requested, this may be the peak contribution to the total required allocation. Further, jax's memory management system makes it difficult to guarantee that no unnecessary copies of arrays are created. Our implementation in jz-tree is therefore relatively memory-intensive -- something that we aim to improve in future releases.

<!-- chunk {"id": "body-0084", "role": "body", "section": "III-E Performance breakdown", "weight": 1.0} -->

All performance measurements throughout this article are run on the booster nodes of the Leonardo cluster at CINECA. Each node has a single 32 core Intel Xeon Platinum 8358 processor, four NVIDIA Ampere A100-64 GPUs and 200 Gbps NVIDIA Mellanox HDR InfiniBand connection. Tests with up to 4 GPUs run on a single node, and larger tests run across several nodes (if $N_{GPU} \geq 4$). For CPU codes we consider tests for a single core and a 32 core setup on a single node.

<!-- chunk {"id": "body-0085", "role": "body", "section": "III-E Performance breakdown", "weight": 1.0} -->

In Figure 5 we break down the execution time of different steps of a self-neighbour search for a uniform random distribution in three dimensions for a single-GPU and a multi-GPU scenario. The single-GPU case highlights the very low cost of the sorting and the tree construction (about $20\%$ of the total). The most expensive part of the algorithm are the leaf-to-leaf interactions -- comprising approximately $50\%$ of the total execution time. This is expected due to the high computational intensity of this step.

<!-- chunk {"id": "body-0086", "role": "body", "section": "III-E Performance breakdown", "weight": 1.0} -->

However, for the multi-GPU scenario the costs of several steps increases significantly: The z-sort due to the required exchange of points, the tree construction due to the communication step required for regularization and the node-to-node interactions due to multiple required all-to-all communications and the cost of removing unused nodes from the interaction list. Noteworthily, the leaf-to-leaf interactions only require slightly more time, since they only need a single communication with relatively low volume (thanks to efficient pruning from higher levels). The cumulative effect of these steps is an approximate factor 2 decrease in efficiency.

<!-- chunk {"id": "body-0087", "role": "body", "section": "III-E Performance breakdown", "weight": 1.0} -->

However, the most significant increase in execution time is due to the final reordering. This is not too surprising, since bringing the neighbour list into input order requires an extremely high volume communication (recall that these are $k = 16$ radii and indices per point). Fortunately, in many applications of neighbour search, it is possible to perform a reduction operation while maintaining the neighbour list in z-order and then only communicate back some small summary statistic per point. We provide a simple interface for this recommended usage pattern in jz-tree and we output points in z-order for further multi-GPU benchmarks, staying representative of such uses cases.

<!-- chunk {"id": "body-0088", "role": "body", "section": "III-F Performance comparisons", "weight": 1.0} -->

We compare the performance of jz-tree for a kNN-search against other publicly available (exact kNN) libraries in Figure 6 for a single GPU setup. The benchmark is to find the $k = 30$ nearest neighbours^44^4In general we use $k = 16$ as a baseline in benchmarks, but here we use $k = 30$ to allow comparison with the default setup in clover. for a uniform random distribution of points on the range ${\lbrack 0,1\rbrack}^{d}$ in $d = 3$ dimensions for $N$ separate source and query points at float32 precision. In each case we include preparation steps (e.g. sorting and tree building) in the performance measurement, so that this represents fairly the total time that is needed to evaluate one set of source points with one set of query points. However, we exclude the jit compilation time that is necessary in jax and cupy implementations.

<!-- chunk {"id": "body-0089", "role": "body", "section": "III-F Performance comparisons", "weight": 1.0} -->

The libraries that we compare to are: scipy-ckdtree -- a CPU based kd-tree library implemented as a C++ extension within SciPy, operating on NumPy arrays. We include measurements for usage of $1$ and $32$ worker threads. The FAISS library that provides efficient implementations of brute force neighbour search. cupy-knn that implements neighbour search through a one-sided traversal of kd-trees in CUDA kernels. Similarly, jaxkd-cuda based on the cudaKDTree library, but offering a convenient jax interface. clover which traverses a graph based on a random voronoi tessellation.

<!-- chunk {"id": "body-0090", "role": "body", "section": "III-F Performance comparisons", "weight": 1.0} -->

jz-tree outperforms all competitor libraries by a significant margin for nearly all problem sizes (except the brute-force approach of FAISS at very small problem sizes $N \lesssim 10^{4}$ where the cost of the many kernel launches leads to an irreducible overhead of $\sim 1$ms.) For $N \lesssim 10^{6}$ clover remains the closest competitor (within about a factor 2), but at larger problem sizes $N \gg 10^{6}$ clover starts scaling quadratically making it more than an order of magnitude slower at $N \sim 10^{7}$. The kd-tree based libraries all exhibit the same (close to linear) asymptotic scaling as jz-tree, but with much larger asymptotic constants. The CPU based scipy-ckdtree turns out more than two orders of magnitude slower than jz-tree and the GPU based kd-tree libraries are more than an order of magnitude slower at $N \gtrsim 10^{6}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "III-F Performance comparisons", "weight": 1.0} -->

This improvement may be largely attributed to several key differences in the tree implementation: The much reduced cost of building a tree in a bottom up approach. The reduced algorithmic cost of a dual (versus one-sided) tree walk and the reduced memory access through warp collaborative evaluation and the improved memory coalescence.

<!-- chunk {"id": "body-0092", "role": "body", "section": "III-G Performance across domains", "weight": 1.0} -->

To demonstrate that the performance benefits are relatively independent of the problem domain, we show in Figure 7(a) performance benchmarks of jz-tree for a variety of different setups. In every case we use query points equal to the source points and look for $k = 16$ neighbours in $d = 3$ dimensions. The considered scenarios include a uniform grid, the uniform random distribution, a multivariate normal distribution and the final particle distribution from realistic cosmological simulations. The cosmological simulations were run with DISCO-DJ in a Planck cosmology with a number of particle-mesh cells and the volume of the box chosen proportionally to the particle count. Specifically we choose the box size as $\sqrt{N}h^{- 1}\text{Mpc}$ so that the mass-resolution stays fixed with increasing problem size. For the cosmological simulation we consider two separate scenarios -- one where we appropriately include periodic wrapping in the distance calculation of the kNN -- and one where we don't. For all scenarios we have verified the correctness of the returned neighbour lists against scipy-ckdtree.

<!-- chunk {"id": "body-0093", "role": "body", "section": "III-G Performance across domains", "weight": 1.0} -->

It is evident that jz-tree generalizes well over different problem setups with problem-specific performance differences staying well below a factor of two. We note that the most expensive setup -- the cosmological simulation with periodic wrapping -- owes its $20 - {30\%}$ reduction in efficiency primarily to the extra-cost in the wrapping calculation (and not so much to the clustering). If we evaluate the same setup without periodic wrapping, the performance is virtually identical to the uniform random distribution at $N \gtrsim 10^{7}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "III-G Performance across domains", "weight": 1.0} -->

In Figure 7(b) we evaluate the scaling of the multi-GPU implementation of jz-tree for a self-query of $k = 16$ for a uniform random distribution in $d = 3$ dimensions. In this test we output the $16$ output indices and radii per point in z-order. Importantly, the horizontal axis of the plot shows the number of points per GPU so that e.g. the 64 GPU case with ${N\text{~per GPU}} = 10^{8}$ evaluates $1.0 \cdot 10^{11}$ neighbours (16 neighbours for each of $64 \cdot 10^{8}$ points) in about 1.3 seconds.

<!-- chunk {"id": "body-0095", "role": "body", "section": "III-G Performance across domains", "weight": 1.0} -->

The method scales well to a large number of GPUs. The biggest drop in the number of evaluations per GPU per second is seen when going from one to two GPUs leading to an increase in evaluation time at $10^{8}$ from $585\text{ms}$ up to $928\text{ms}$ -- close to a factor of two. This increase comes from the additional algorithmic steps that need to be taken for the distributed computing (like rearranging points, sample sort, adjusting domain boundaries and communication). However, scaling from $2$ to $64$ GPUs exhibits only an additional decrease in efficiency of $30\%$ (928ms for two GPUs versus 1256ms for 64 at $10^{8}$).

<!-- chunk {"id": "body-0096", "role": "body", "section": "III-G Performance across domains", "weight": 1.0} -->

For completeness, we provide additional scaling tests with dimension number, neighbour count and query versus source counts in Appendix A.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Friends-of-friends clustering", "weight": 1.0} -->

As a second example algorithm we describe an efficient implementation of FoF clustering here. The implementation follows very closely the previously outlined dual-tree-traversal pattern plus a well known approach for handling linking relations. We have tested it well in $d = 2$ and $d = 3$ dimensions and for periodic and non-periodic boundary conditions, but the implementation should cleanly generalize to higher dimensional setups as well.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Friends-of-friends clustering", "weight": 1.0} -->

The goal of a FoF algorithm is to find the connected components of a graph where each point is a node and edges exist between every pair of nodes that is closer than the linking length $R_{link}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Friends-of-friends clustering", "weight": 1.0} -->

where $V$ is the volume of the simulation box and $\alpha$ is a parameter that is typically chosen to be $\sim 0.2$, e.g..

<!-- chunk {"id": "body-0100", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

The connected components of the FoF graph can be conveniently represented through a pointer $\mathbf{i}\mathbf{g}\mathbf{r}\mathbf{o}\mathbf{u}\mathbf{p}$ that is defined per point. If the pointer points to a point itself ${igroup}_{i} = i$, we call $i$ 'a root'. Otherwise, it must point to a point that is of the same group and has a lower index. The root of a point's group can be found by dereferencing the pointer multiple times until it points to itself. All points that have the same root belong to the same group (and vice versa).

<!-- chunk {"id": "body-0101", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

The FoF implementation follows the same dual tree walk pattern that is outlined in Algorithm 1. However, in addition to the interaction list, the group pointer ${\mathbf{i}\mathbf{g}\mathbf{r}\mathbf{o}\mathbf{u}\mathbf{p}}^{(p)}$ is carried through the tree-walk and advected from parent to child nodes on every level. It is initialized on the super-node level as a self-pointer. Before the NodeToNode pass, we perform a ParentToNode pass that evaluates

<!-- chunk {"id": "body-0102", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

so that for linked nodes it will point to the first child of the root of its parent node. For unlinked nodes it will simply point to the point itself. A root is considered self-linked if it was linked with any other node or if its diagonal extent is smaller than the linking length.

<!-- chunk {"id": "body-0103", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

The node-to-node interaction distinguishes three cases: If both nodes already point to the same root or if $d_{low} > R_{link}$, the interaction is discarded. If $d_{up} \leq R_{link}$, the other node falls fully inside of the linking length and the nodes are linked together. Otherwise the interaction needs to be evaluated at the child level and is inserted into the interaction list.

<!-- chunk {"id": "body-0104", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

When two nodes are linked together, we first find their roots and then update the higher index root to point towards the lower index root -- thereby linking all points in the two groups together. On GPU it is important to protect against data races in this update (between finding the roots and the update, one of the roots may have changed) with atomic compare and swap operations and a repeat on failure.

<!-- chunk {"id": "body-0105", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

We first launch a kernel to update $\mathbf{i}\mathbf{g}\mathbf{r}\mathbf{o}\mathbf{u}\mathbf{p}$ in this way and afterwards contract the $\mathbf{i}\mathbf{g}\mathbf{r}\mathbf{o}\mathbf{u}\mathbf{p}$ relation in a separate kernel. This is simply done by setting every pointer in $\mathbf{i}\mathbf{g}\mathbf{r}\mathbf{o}\mathbf{u}\mathbf{p}$ to its root. Finally, we count and insert the interactions that need to be checked on the next level.

<!-- chunk {"id": "body-0106", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

The point-point interactions in the leaf-to-leaf kernel only need to distinguish between two scenarios $d > R_{link}$ -- where the interaction is discarded -- and $d \leq R_{link}$ -- where the points' groups are linked together. After evaluating these interactions the graph is contracted one final time to obtain a unique label for each group.

<!-- chunk {"id": "body-0107", "role": "body", "section": "IV-A Implementation", "weight": 1.0} -->

The multi-GPU implementation of the FoF requires some additional effort to distinguish between links that can be resolved locally immediately and those that need to be saved to be resolved globally at a later point (involving communication). However, these details are not very relevant with respect to the focus of this paper, so they will be described in Appendix B.

<!-- chunk {"id": "body-0108", "role": "body", "section": "IV-B Catalogue reduction", "weight": 1.0} -->

After the group identification, we bring points into group order. That means we perform a stable sort based on the group index, so that the roots of groups remain in z-order with respect to other roots and points in each group form a contiguous block that is internally in z-order. The last group on each device may continue on subsequent devices. Bringing points into group order is useful to make subsequent reduction steps simpler and to make it simple to read the points in different FoF groups separately if the particle data is dumped.

<!-- chunk {"id": "body-0109", "role": "body", "section": "IV-B Catalogue reduction", "weight": 1.0} -->

Finally, we calculate summary statistics like the total mass, the inertia radius, the center of mass position and the the center of mass velocity (if particle velocities were provided as input). This step can be done almost entirely locally, except for a small communication step related to the last/first group on each task. We provide the option to filter the resulting catalogues by a minimum particle count and choose $20$ for this -- as is common in the computational cosmology literature -- in the following performance tests.

<!-- chunk {"id": "body-0110", "role": "body", "section": "IV-C Performance", "weight": 1.0} -->

We evaluate the time that is required to obtain the FoF catalogue for the particle distribution from a cosmological simulation (as described in Section III-G). This includes all the necessary steps, i.e. sorting, tree building, the tree walk, the reordering into group order and the final reduction steps. However, we don't include disk write time in this benchmark.

<!-- chunk {"id": "body-0111", "role": "body", "section": "IV-C Performance", "weight": 1.0} -->

For comparison we test against the single CPU FoF implementation of hfof, the MPI implementation in Gadget4 and the single GPU implementation of jfof. For hfof we only benchmark the labelling step, since no catalogue reduction is provided -- so results are slightly skewed in its favour. For Gadget4, we read in an hdf5 snapshot that we created with DISCODJ and run only the FoF algorithm. Here, we use the timings that are written into stdout, excluding the initial reading of the input, the initial domain decomposition^55^5We exclude this, since the input is read initially from a single snapshot onto a single task and is very imbalanced through this until after the first domain decomposition. and the final writing of the output. We run Gadget once with 1 MPI task and once with 32 MPI tasks on a 32 core node. jfof is the only other pure GPU FoF code that we are aware of and it is a research-level implementation to enable differentible halo finding. It uses jax-kd\[CUDA\] to iteratively link points together by traversing their neighbour graph.

<!-- chunk {"id": "body-0112", "role": "body", "section": "IV-C Performance", "weight": 1.0} -->

The benchmarks required padding with an additional particle to avoid CUDA memory access errors -- as suggested by the authors.

<!-- chunk {"id": "body-0113", "role": "body", "section": "IV-C Performance", "weight": 1.0} -->

The resulting measurements are found in Figure 8(a). Similar to the nearest neighbour search, jz-tree scales linearly with the problem size once the GPU is fully saturated $N \gtrsim 10^{7}$. The performance of jz-tree compares favourably with respect to the alternatives. For $512^{3}$ the evaluation takes $1.2s$ which is about 5 times faster than Gadget4 with 32 cores (5.3s), 18 times faster than jfof (22s), 66 times faster than hfof (82s) and 116 times faster than Gadget 4 with one core (144s).

<!-- chunk {"id": "body-0114", "role": "body", "section": "IV-C Performance", "weight": 1.0} -->

Finally, we show in Figure 8(b) benchmarks for different GPU counts. The efficiency takes the biggest reduction when jumping from 1 node ($\leq 4$ GPUs) to multiple nodes ($> 4$ GPUs) where the communication becomes less efficient. The most relevant factor here is probably the increased communication latency in the distributed link insertion and contraction steps. However, the efficiency only decreases in total by a factor $2 - 3$ when scaling from 1 to 64 GPUs, allowing us to calculate FoF group catalouges on $2048^{3}$ points on 64 GPUs in about $3s$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Here we have presented a novel approach to construct a plane-based tree hierarchy to enable GPU friendly dual tree walks. Unlike more conventional kd-trees or oct-trees, this tree structure does not partition all of space, has the same depth everywhere and may exhibit a varying number of unequal sized children. It can be constructed in a bottom-up approach with very little additional performance cost after sorted along a Morton z-order curve.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The plane hierarchy allows to implement dual tree walks with good thread collaboration and coalescing memory access patterns. We have demonstrated this on two example applications, nearest neighbour search and FoF clustering -- yielding order of magnitude performance improvements over existing GPU codes with great scaling to distributed computation with large numbers of GPUs.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The presented algorithms are implemented in the jz-tree library, publicly available on GitHub (reference) and PyPI (reference). They can readily be used in HPC simulation schemes that rely on these components like smoothed particle hydrodynamics, self-interacting dark matter simulations and halo finding in cosmological simulations.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Finally, we emphasize that jz-tree forms a suitable framework for developing efficient GPU implementations of other algorithms that rely on tree representations, such as the fast multipole method which we will discuss in an upcoming publication.
