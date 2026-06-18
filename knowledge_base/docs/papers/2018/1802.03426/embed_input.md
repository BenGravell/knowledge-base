<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction

Topics include Learning, UMAP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

UMAP (Uniform Manifold Approximation and Projection) is a novel manifold learning technique for dimension reduction. UMAP is constructed from a theoretical framework based in Riemannian geometry and algebraic topology. The result is a practical scalable algorithm that applies to real world data. The UMAP algorithm is competitive with t-SNE for visualization quality, and arguably preserves more of the global structure with superior run time performance. Furthermore, UMAP has no computational restrictions on embedding dimension, making it viable as a general purpose dimension reduction technique for machine learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dimension reduction plays an important role in data science, being a fundamental technique in both visualisation and as pre-processing for machine learning. Dimension reduction techniques are being applied in a broadening range of fields and on ever increasing sizes of datasets. It is thus desirable to have an algorithm that is both scalable to massive data and able to cope with the diversity of data available. Dimension reduction algorithms tend to fall into two categories; those that seek to preserve the pairwise distance structure amongst all the data samples and those that favor the preservation of local distances over global distance. Algorithms such as PCA, MDS, and Sammon mapping fall into the former category while t-SNE, Isomap, LargeVis, Laplacian eigenmaps and diffusion maps all fall into the latter category.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we introduce a novel manifold learning technique for dimension reduction. We provide a sound mathematical theory grounding the technique and a practical scalable algorithm that applies to real world data. UMAP (Uniform Manifold Approximation and Projection) builds upon mathematical foundations related to the work of Belkin and Niyogi on Laplacian eigenmaps. We seek to address the issue of uniform data distributions on manifolds through a combination of Riemannian geometry and the work of David Spivak in category theoretic approaches to geometric realization of fuzzy simplicial sets. t-SNE is the current state-of-the-art for dimension reduction for visualization. Our algorithm is competitive with t-SNE for visualization quality and arguably preserves more of the global structure with superior run time performance. Furthermore the algorithm is able to scale to significantly larger data set sizes than are feasible for t-SNE. Finally, UMAP has no computational restrictions on embedding dimension, making it viable as a general purpose dimension reduction technique for machine learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based upon preliminary releases of a software implementation, UMAP has already found widespread use in the fields of bioinformatics, materials science, and machine learning among others.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is laid out as follows. In Section 2 we describe the theory underlying the algorithm. Section 2 is necessary to understand both the theory underlying why UMAP works and the motivation for the choices that where made in developing the algorithm. A reader without a background (or interest) in topological data analysis, category theory or the theoretical underpinnings of UMAP should skip over this section and proceed directly to Section 3.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

That being said, we feel that strong theory and mathematically justified algorithmic decisions are of particular importance in the field of unsupervised learning. This is, at least partially, due to plethora of proposed objective functions within the area. We attempt to highlight in this paper that UMAPs design decisions were all grounded in a solid theoretic foundation and not derived through experimentation with any particular task focused objective function. Though all neighbourhood based manifold learning algorithms must share certain fundamental components we believe it to be advantageous for these components to be selected through well grounded theoretical decisions. One of the primary contributions of this paper is to reframe the problem of manifold learning and dimension reduction in a different mathematical language allowing pracitioners to apply a new field of mathemtaics to the problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 3 we provide a more computational description of UMAP. Section 3 should provide readers less familiar with topological data analysis with a better foundation for understanding the theory described in Section 2. Appendix C contrasts UMAP against the more familiar algorithms t-SNE and LargeVis, describing all these algorithms in similar language. This section should assist readers already familiar with those techniques to quickly gain an understanding of the UMAP algorithm though they will grant little insite into its theoretical underpinnings.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 4 we discuss implementation details of the UMAP algorithm. This includes a more detailed algorithmic description, and discussion of the hyper-parameters involved and their practical effects.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 5 we provide practical results on real world datasets as well as scaling experiments to demonstrate the algorithm's performance in real world scenarios as compared with other dimension reduction algorithms.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 6 we discuss relative weakenesses of the algorithm, and applications for which UMAP may not be the best choice.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, in Section 7 we detail a number of potential extensions of UMAP that are made possible by its construction upon solid mathematical foundations. These avenues for further development include semi-supervised learning, metric learning and heterogeneous data embedding.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Theoretical Foundations for UMAP", "weight": 1.0} -->

The theoretical foundations for UMAP are largely based in manifold theory and topological data analysis. Much of the theory is most easily explained in the language of topology and category theory. Readers may consult, and for background. Readers more interested in practical computational aspects of the algorithm, and not necessarily the theoretical motivation for the computations involved, may wish to skip this section. Readers more familiar with traditional machine learning may find the relationships between UMAP, t-SNE and Largeviz located in Appendix C enlightening. Unfortunately, this purely computational view fails to shed any light upon the reasoning that underlies the algorithmic decisions made in UMAP. Without strong theoretical foundations the only arguments which can be made about algorithms amount to empirical measures, for which there are no clear universal choices for unsupervised problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Theoretical Foundations for UMAP", "weight": 1.0} -->

At a high level, UMAP uses local manifold approximations and patches together their local fuzzy simplicial set representations to construct a topological representation of the high dimensional data. Given some low dimensional representation of the data, a similar process can be used to construct an equivalent topological representation. UMAP then optimizes the layout of the data representation in the low dimensional space, to minimize the cross-entropy between the two topological representations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Theoretical Foundations for UMAP", "weight": 1.0} -->

The construction of fuzzy topological representations can be broken down into two problems: approximating a manifold on which the data is assumed to lie; and constructing a fuzzy simplicial set representation of the approximated manifold. In explaining the algorithm we will first discuss the method of approximating the manifold for the source data. Next we will discuss how to construct a fuzzy simplicial set structure from the manifold approximation. Finally, we will discuss the construction of the fuzzy simplicial set associated to a low dimensional representation (where the manifold is simply ${\mathbb{R}}^{d}$), and how to optimize the representation with respect to our objective function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Uniform distribution of data on a manifold and geodesic approximation", "weight": 1.0} -->

The first step of our algorithm is to approximate the manifold we assume the data (approximately) lies. The manifold may be known apriori (as simply ${\mathbb{R}}^{n}$) or may need to be inferred from the data. Suppose the manifold is not known in advance and we wish to approximate geodesic distance on it. Let the input data be $X = {\{ X_{1},\ldots,X_{N}\}}$. As in the work of Belkin and Niyogi on Laplacian eigenmaps, for theoretical reasons it is beneficial to assume the data is uniformly distributed on the manifold, and even if that assumption is not made (e.g ) results are only valid in the limit of infinite data. In practice, finite real world data is rarely so nicely behaved. However, if we assume that the manifold has a Riemannian metric not inherited from the ambient space, we can find a metric such that the data is approximately uniformly distributed with regard to that metric.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Uniform distribution of data on a manifold and geodesic approximation", "weight": 1.0} -->

Formally, let $\mathcal{M}$ be the manifold we assume the data to lie, and let $g$ be the Riemannian metric on $\mathcal{M}$. Thus, for each point $p \in \mathcal{M}$ we have $g_{p}$, an inner product on the tangent space $T_{p}\mathcal{M}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Fuzzy topological representation", "weight": 1.0} -->

We will use functors between the relevant categories to convert from metric spaces to fuzzy topological representations. This will provide a means to merge the incompatible local views of the data. The topological structure of choice is that of simplicial sets. For more details on simplicial sets we refer the reader to or. Our approach draws heavily upon the work of Michael Barr and David Spivak, and many of the definitions and theorems below are drawn or adapted from those sources. We assume familiarity with the basics of category theory. For an introduction to category theory readers may consult or.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Fuzzy topological representation", "weight": 1.0} -->

To start we will review the definitions for simplicial sets. Simplicial sets provide a combinatorial approach to the study of topological spaces. They are related to the simpler notion of simplicial complexes -- which construct topological spaces by gluing together simple building blocks called simplices -- but are more general. Simplicial sets are most easily defined purely abstractly in the language of category theory.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimizing a low dimensional representation", "weight": 1.0} -->

Let $Y = {\{ Y_{1},\ldots,Y_{N}\}} \subseteq {\mathbb{R}}^{d}$ be a low dimensional ($d \ll n$) representation of $X$ such that $Y_{i}$ represents the source data point $X_{i}$. In contrast to the source data where we want to estimate a manifold on which the data is uniformly distributed, a target manifold for $Y$ is chosen apriori (usually this will simply be ${\mathbb{R}}^{d}$ itself, but other choices such as $d$-spheres or $d$-tori are certainly possible). Therefore we know the manifold and manifold metric apriori, and can compute the fuzzy topological representation directly. Of note, we still want to incorporate the distance to the nearest neighbor as per the local connectedness requirement. This can be achieved by supplying a parameter that defines the expected distance between nearest neighbors in the embedded space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimizing a low dimensional representation", "weight": 1.0} -->

Given fuzzy simplicial set representations of $X$ and $Y$, a means of comparison is required. If we consider only the 1-skeleton of the fuzzy simplicial sets we can describe each as a fuzzy graph, or, more specifically, a fuzzy set of edges. To compare two fuzzy sets we will make use of fuzzy set cross entropy. For these purposes we will revert to classical fuzzy set notation. That is, a fuzzy set is given by a reference set $A$ and a membership strength function $\mu:{A\rightarrow{\lbrack 0,1\rbrack}}$. Comparable fuzzy sets have the same reference set.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

To understand what computations the UMAP algorithm is actually making from a practical point of view, a less theoretical and more computational description may be helpful for the reader. This description of the algorithm lacks the motivation for a number of the choices made. For that motivation please see Section 2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

The theoretical description of the algorithm works in terms of fuzzy simplicial sets. Computationally this is only tractable for the one skeleton which can ultimately be described as a weighted graph. This means that, from a practical computational perspective, UMAP can ultimately be described in terms of, construction of, and operations, weighted graphs. In particular this situates UMAP in the class of k-neighbour based graph learning algorithms such as Laplacian Eigenmaps, Isomap and t-SNE.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

As with other k-neighbour graph based algorithms, UMAP can be described in two phases. In the first phase a particular weighted k-neighbour graph is constructed. In the second phase a low dimensional layout of this graph is computed. The differences between all algorithms in this class amount to specific details in how the graph is constructed and how the layout is computed. The theoretical basis for UMAP as described in Section 2 provides novel approaches to both of these phases, and provides clear motivation for the choices involved.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Finally, since t-SNE is not usually described as a graph based algorithm, a direct comparison of UMAP with t-SNE, using the similarity/probability notation commonly used to express the equations of t-SNE, is given in the Appendix C.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

In section 2 we made a few basic assumptions about our data. From these assumptions we made use of category theory to derive the UMAP algorithms. That said, all these derivations assume these axioms to be true.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

There exists a manifold on which the data would be uniformly distributed.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

The underlying manifold of interest is locally connected.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Preserving the topological structure of this manifold is the primary goal.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

The topological theory of Section 2 is driven by these axioms, particularly the interest in modelling and preserving topological structure. In particular Section 2.1 highlights the underlying motivation, in terms of topological theory, of representing a manifold as a k-neighbour graph.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

As highlighted in Appendix C any algorithm that attempts to use a mathematical structure akin to a k-neighbour graph to approximate a manifold must follow a similar basic structure.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Apply some transform on the edges to ambient local distance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Deal with the inherent asymmetry of the k-neighbour graph.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Define an objective function that preserves desired characteristics of this k-neighbour graph.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Find a low dimensional representation which optimizes this objective function.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

Many dimension reduction algorithms can be broken down into these steps because they are fundamental to a particular class of solutions. Choices for each step must be either chosen through task oriented experimentation or by selecting a set of believable axioms and building strong theoretical arguments from these. Our belief is that basing our decisions on a strong foundational theory will allow for a more extensible and generalizable algorithm in the long run.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Computational View of UMAP", "weight": 1.0} -->

We theoretically justify using the choice of using a k-neighbour graph to represent a manifold in Section 2.1. The choices for our kernel transform an symmetrization function can be found in Section 2.2. Finally, the justifications underlying our choices for our graph layout are outlined in Section 2.3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

The first phase of UMAP can be thought of as the construction of a weighted k-neighbour graph. Let $X = {\{ x_{1},\ldots,x_{N}\}}$ be the input dataset, with a metric (or dissimilarity measure) $d:{{X \times X}\rightarrow{\mathbb{R}}_{\geq 0}}$. Given an input hyper-parameter $k$, for each $x_{i}$ we compute the set $\{ x_{i_{1}},\ldots,x_{i_{k}}\}$ of the $k$ nearest neighbors of $x_{i}$ under the metric $d$. This computation can be performed via any nearest neighbour or approximate nearest neighbour search algorithm. For the purposes of our UMAP implemenation we prefer to use the nearest neighbor descent algorithm of.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

and set $\sigma_{i}$ to be the value such that

<!-- chunk {"id": "body-0040", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

The selection of $\rho_{i}$ derives from the local-connectivity constraint described in Section 2.2. In particular it ensures that $x_{i}$ connects to at least one other data point with an edge of weight 1; this is equivalent to the resulting fuzzy simplicial set being locally connected at $x_{i}$. In practical terms this significantly improves the representation on very high dimensional data where other algorithms such as t-SNE begin to suffer from the curse of dimensionality.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

The selection of $\sigma_{i}$ corresponds to (a smoothed) normalisation factor, defining the Riemannian metric local to the point $x_{i}$ as described in Section 2.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

We can now define a weighted directed graph $\overline{G} = {(V,E,w)}$. The vertices $V$ of $\overline{G}$ are simply the set $X$. We can then form the set of directed edges $E = {\{{(x_{i},x_{i_{j}})}\mid{{1 \leq j \leq k},{1 \leq i \leq N}}\}}$, and define the weight function $w$ by setting

<!-- chunk {"id": "body-0043", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

For a given point $x_{i}$ there exists an induced graph of $x_{i}$ and outgoing edges incident on $x_{i}$. This graph is the 1-skeleton of the fuzzy simplicial set associated to the metric space local to $x_{i}$ where the local metric is defined in terms of $\rho_{i}$ and $\sigma_{i}$. The weight associated to the edge is the membership strength of the corresponding 1-simplex within the fuzzy simplicial set, and is derived from the adjunction of Theorem 1 using the right adjoint (nearest inverse) of the geometric realization of a fuzzy simplicial set. Intuitively one can think of the weight of an edge as akin to the probability that the given edge exists. Section 2 demonstrates why this construction faithfully captures the topology of the data. Given this set of local graphs (represented here as a single directed graph) we now require a method to combine them into a unified topological representation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

We note that while patching together incompatible finite metric spaces is challenging, by using Theorem 1 to convert to a fuzzy simplicial set representation, the combining operation becomes natural.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

Let $A$ be the weighted adjacency matrix of $\overline{G}$, and consider the symmetric matrix

<!-- chunk {"id": "body-0046", "role": "body", "section": "Graph Construction", "weight": 1.0} -->

where $\circ$ is the Hadamard (or pointwise) product. This formula derives from the use of the probabilistic t-conorm used in unioning the fuzzy simplicial sets. If one interprets the value of $A_{ij}$ as the probability that the directed edge from $x_{i}$ to $x_{j}$ exists, then $B_{ij}$ is the probability that at least one of the two directed edges (from $x_{i}$ to $x_{j}$ and from $x_{j}$ to $x_{i}$) exists. The UMAP graph $G$ is then an undirected weighted graph whose adjacency matrix is given by $B$. Section 2 explains this construction in topological terms, providing the justification for why this construction provides an appropriate fuzzy topological representation of the data -- that is, this construction captures the underlying geometric structure of the data in a faithful way.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Graph Layout", "weight": 1.0} -->

In practice UMAP uses a force directed graph layout algorithm in low dimensional space. A force directed graph layout utilizes of a set of attractive forces applied along edges and a set of repulsive forces applied among vertices. Any force directed layout algorithm requires a description of both the attractive and repulsive forces. The algorithm proceeds by iteratively applying attractive and repulsive forces at each edge or vertex. This amounts to a non-convex optimization problem. Convergence to a local minima is guaranteed by slowly decreasing the attractive and repulsive forces in a similar fashion to that used in simulated annealing.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Graph Layout", "weight": 1.0} -->

Repulsive forces are computed via sampling due to computational constraints. Thus, whenever an attractive force is applied to an edge, one of that edge's vertices is repulsed by a sampling of other vertices. The repulsive force is given by

<!-- chunk {"id": "body-0049", "role": "body", "section": "Graph Layout", "weight": 1.0} -->

$\epsilon$ is a small number to prevent division by zero (0.001 in the current implementation).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Graph Layout", "weight": 1.0} -->

The algorithm can be initialized randomly but in practice, since the symmetric Laplacian of the graph $G$ is a discrete approximation of the Laplace-Beltrami operator of the manifold, we can use a spectral layout to initialize the embedding. This provides both faster convergence and greater stability within the algorithm.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Graph Layout", "weight": 1.0} -->

The forces described above are derived from gradients optimising the edge-wise cross-entropy between the weighted graph $G$, and an equivalent weighted graph $H$ constructed from the points ${\{\mathbf{y}_{\mathbf{i}}\}}_{i = 1..N}$. That is, we are seeking to position points $y_{i}$ such that the weighted graph induced by those points most closely approximates the graph $G$, where we measure the difference between weighted graphs by the total cross entropy over all the edge existence probabilities. Since the weighted graph $G$ captures the topology of the source data, the equivalent weighted graph $H$ constructed from the points ${\{\mathbf{y}_{\mathbf{i}}\}}_{i = 1..N}$ matches the topology as closely as the optimization allows, and thus provides a good low dimensional representation of the overall topology of the data.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Implementation and Hyper-parameters", "weight": 1.0} -->

Having completed a theoretical description of the approach, we now turn our attention to the practical realization of this theory. We begin by providing a more detailed description of the algorithm as implemented, and then discuss a few implementation specific details. We conclude this section with a discussion of the hyper-parameters for the algorithm and their practical effects.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

In overview the UMAP algorithm is relatively straightforward (see Algorithm 1). When performing a fuzzy union over local fuzzy simplicial sets we have found it most effective to work with the probabilistic t-conorm (as one would expect if treating membership strengths as a probability that the simplex exists). The individual functions for constructing the local fuzzy simplicial sets, determining the spectral embedding, and optimizing the embedding with regard to fuzzy set cross entropy, are described in more detail below.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

## Construct the relevant weighted graph
top-rep ← ⋃x ∈ Xfs-set [x] # We recommend the probabilistic t-conorm

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

## Perform optimization of the graph layout
Y← OptimizeEmbedding(top-rep, Y, min-dist, n-epochs)
Algorithm 1 UMAP algorithm

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

The inputs to Algorithm 1 are: $X$, the dataset to have its dimension reduced; $n$, the neighborhood size to use for local metric approximation; $d$, the dimension of the target reduced space; min-dist, an algorithmic parameter controlling the layout; and n-epochs, controlling the amount of optimization work to perform.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Algorithm 2 describes the construction of local fuzzy simplicial sets. To represent fuzzy simplicial sets we work with the fuzzy set images of $\lbrack 0\rbrack$ and $\lbrack 1\rbrack$ (i.e. the 1-skeleton), which we denote as $\text{fs-set}_{0}$ and $\text{fs-set}_{1}$. One can work with higher order simplices as well, but the current implementation does not. We can construct the fuzzy simplicial set local to a given point $x$ by finding the $n$ nearest neighbors, generating the appropriate normalised distance on the manifold, and then converting the finite metric space to a simplicial set via the functor $\mathsf{F}\mathsf{i}\mathsf{n}\mathsf{S}\mathsf{i}\mathsf{n}\mathsf{g}$, which translates into exponential of the negative distance in this case.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

knn, knn-dists ← ApproxNearestNeighbors(X, x, n)
ρ← knn-dists # Distance to nearest neighbor
σ← SmoothKNNDist(knn-dists, n, ρ) # Smooth approximator to knn-distance
for all y∈ knn do
fs-set1 ← fs-set1 ∪ ([x, y],exp (−dx, y))
Algorithm 2 Constructing a local fuzzy simplicial set

<!-- chunk {"id": "body-0059", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Rather than directly using the distance to the $n^{\text{th}}$ nearest neighbor as the normalization, we use a smoothed version of knn-distance that fixes the cardinality of the fuzzy set of 1-simplices to a fixed value. We selected $\log_{2}{(n)}$ for this purpose based on empirical experiments. This is described briefly in Algorithm 3.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

function SmoothKNNDist(knn-dists, n, ρ)
Binary search for σ such that ${\sum_{i = 1}^{n}{\exp{({- {{({\text{knn-dists}_{i} - \rho})}/\sigma}})}}} = {\log_{2}{(n)}}$
Algorithm 3 Compute the normalizing factor for distances σ

<!-- chunk {"id": "body-0061", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Spectral embedding is performed by considering the 1-skeleton of the global fuzzy topological representation as a weighted graph and using standard spectral methods on the symmetric normalized Laplacian. This process is described in Algorithm 4.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

function SpectralEmbedding(top-rep, d)
A← 1-skeleton of top-rep expressed as a weighted adjacency matrix
D← degree matrix for the graph A
evec← Eigenvectors of L (sorted)
Y ← evec[1..d + 1] # 0-base indexing assumed
Algorithm 4 Spectral embedding for initialization

<!-- chunk {"id": "body-0063", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

The final major component of UMAP is the optimization of the embedding through minimization of the fuzzy set cross entropy. Recall that fuzzy set cross entropy, with respect given membership functions $\mu$ and $\nu$, is given by

<!-- chunk {"id": "body-0064", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

The first sum depends only on $\mu$ which takes fixed values during the optimization, thus the minimization of cross entropy depends only on the second sum, so we seek to minimize

<!-- chunk {"id": "body-0065", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Following both and, we take a sampling based approach to the optimization. We sample 1-simplices with probability $\mu{(a)}$ and update according to the value of $\nu{(a)}$, which handles the term $\mu{(a)}{\log{({\nu{(a)}})}}$. The term ${({1 - {\mu{(a)}}})}{\log{({1 - {\nu{(a)}}})}}$ requires negative sampling -- rather than computing this over all potential simplices we randomly sample potential 1-simplices and assume them to be a negative example (i.e. with membership strength 0) and update according to the value of $1 - {\nu{(a)}}$. In contrast to the above formulation provides a vertex sampling distribution of

<!-- chunk {"id": "body-0066", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

for negative samples, which can be reasonably approximated by a uniform distribution for sufficiently large data sets.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

It therefore only remains to find a differentiable approximation to $\nu{(a)}$ for a given 1-simplex $a$ so that gradient descent can be applied for optimization.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Implementation", "weight": 1.0} -->

Practical implementation of this algorithm requires (approximate) $k$-nearest-neighbor calculation and efficient optimization via stochastic gradient descent.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Implementation", "weight": 1.0} -->

Efficient approximate $k$-nearest-neighbor computation can be achieved via the Nearest-Neighbor-Descent algorithm of. The error intrinsic in a dimension reduction technique means that such approximation is more than adequate for these purposes. While no theoretical complexity bounds have been established for Nearest-Neighbor-Descent the authors of the original paper report an empirical complexity of $O{(N^{1.14})}$. A further benefit of Nearest-Neighbor-Descent is its generality; it works with any valid dissimilarity measure, and is efficient even for high dimensional data.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Implementation", "weight": 1.0} -->

In optimizing the embedding under the provided objective function, we follow work of; making use of probabilistic edge sampling and negative sampling. This provides a very efficient approximate stochastic gradient descent algorithm since there is no normalization requirement. Furthermore, since the normalized Laplacian of the fuzzy graph representation of the input data is a discrete approximation of the Laplace-Betrami operator of the manifold \[\[, see\]\]belkin2002laplacian, belkin2003laplacian, we can provide a suitable initialization for stochastic gradient descent by using the eigenvectors of the normalized Laplacian. The amount of optimization work required will scale with the number of edges in the fuzzy graph (assuming a fixed negative sampling rate), resulting in a complexity of $O{({kN})}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Implementation", "weight": 1.0} -->

Combining these techniques results in highly efficient embeddings, which we will discuss in Section 5. The overall complexity is bounded by the approximate nearest neighbor search complexity and, as mentioned above, is empirically approximately $O{(N^{1.14})}$. A reference implementation can be found at and an R implementation can be found at

<!-- chunk {"id": "body-0072", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

$n$, the number of neighbors to consider when approximating the local metric;

<!-- chunk {"id": "body-0073", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

min-dist, the desired separation between close points in the embedding space; and

<!-- chunk {"id": "body-0074", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

n-epochs, the number of training epochs to use when optimizing the low dimensional representation.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

The effects of the parameters $d$ and n-epochs are largely self-evident, and will not be discussed in further detail here. In contrast the effects of the number of neighbors $n$ and of min-dist are less clear.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

One can interpret the number of neighbors $n$ as the local scale at which to approximate the manifold as roughly flat, with the manifold estimation averaging over the $n$ neighbors. Manifold features that occur at a smaller scale than within the $n$ nearest-neighbors of points will be lost, while large scale manifold features that cannot be seen by patching together locally flat charts at the scale of $n$ nearest-neighbors may not be well detected. Thus $n$ represents some degree of trade-off between fine grained and large scale manifold features --- smaller values will ensure detailed manifold structure is accurately captured (at a loss of the "big picture" view of the manifold), while larger values will capture large scale manifold structures, but at a loss of fine detail structure which will get averaged out in the local approximations. With smaller $n$ values the manifold tends to be broken into many small connected components (care needs to be taken with the spectral embedding for initialization in such cases).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

In contrast min-dist is a hyperparameter directly affecting the output, as it controls the fuzzy simplicial set construction from the low dimensional representation. It acts in lieu of the distance to the nearest neighbor used to ensure local connectivity. In essence this determines how closely points can be packed together in the low dimensional representation. Low values on min-dist will result in potentially densely packed regions, but will likely more faithfully represent the manifold structure. Increasing the value of min-dist will force the embedding to spread points out more, assisting visualization (and avoiding potential overplotting issues). We view min-dist as an essentially aesthetic parameter, governing the appearance of the embedding, and thus is more important when using UMAP for visualization.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

In Figure 1 we provide examples of the effects of varying the hyperparameters for a toy dataset. The data is uniform random samples from a 3-dimensional color-cube, allowing for easy visualization of the original 3-dimensional coordinates in the embedding space by using the corresponding RGB colour. Since the data fills a 3-dimensional cube there is no local manifold structure, and hence for such data we expect larger $n$ values to be more useful. Low values will interpret the noise from random sampling as fine scale manifold structure, producing potentially spurious structure^11^1See the discussion of the constellation effect in Section 6.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

In Figure 2 we provides examples of the same hyperparamter choices as Figure 1, but for the PenDigits dataset^22^2See Section 5 for a description of the PenDigits dataset. In this case we expect small to medium $n$ values to be most effective, since there is significant cluster structure naturally present in the data. The min-dist parameter expands out tightly clustered groups, allowing more of the internal structure of densely packed clusters to be seen.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Hyper-parameters", "weight": 1.0} -->

Finally, in Figure 3 we provide an equivalent example of hyperparameter choices for the MNIST dataset^33^3See section 5 for details on the MNIST dataset. Again, since this dataset is expected to have signifcant cluster structure we expect medium sized values of $n$ to be most effective. We note that large values of min-dist result in the distinct clusters being compressed together, making the distinctions between the clusters less clear.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Practical Efficacy", "weight": 1.0} -->

While the strong mathematical foundations of UMAP were the motivation for its development, the algorithm must ultimately be judged by its practical efficacy. In this section we examine the fidelity and performance of low dimensional embeddings of multiple diverse real world data sets under UMAP.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Practical Efficacy", "weight": 1.0} -->

Pen digits is a set of 1797 grayscale images of digits entered using a digitiser tablet. Each image is an 8x8 image which we treat as a single 64 dimensional vector, assumed to be in Euclidean vector space.\
COIL 20 is a set of 1440 greyscale images consisting of 20 objects under 72 different rotations spanning 360 degrees. Each image is a 128x128 image which we treat as a single 16384 dimensional vector for the purposes of computing distance between images.\
COIL 100 is a set of 7200 colour images consisting of 100 objects under 72 different rotations spanning 360 degrees. Each image consists of 3 128x128 intensity matrices (one for each color channel). We treat this as a single 49152 dimensional vector for the purposes of computing distance between images.\
Mouse scRNA-seq is profiled gene expression data for 20,921 cells from an adult mouse. Each sample consists of a vector of 26,774 measurements.\
Statlog (Shuttle) is a NASA dataset consisting of various data associated to the positions of radiators in the space shuttle, including a timestamp.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Practical Efficacy", "weight": 1.0} -->

The dataset has 58000 points in a 9 dimensional feature space.\
MNIST is a dataset of 28x28 pixel grayscale images of handwritten digits. There are 10 digit classes (0 through 9) and 70000 total images. This is treated as 70000 different 784 dimensional vectors.\
F-MNIST or Fashion MNIST is a dataset of 28x28 pixel grayscale images of fashion items (clothing, footwear and bags). There are 10 classes and 70000 total images. As with MNIST this is treated as 70000 different 784 dimensional vectors.\
Flow cytometry is a dataset of flow cytometry measurements of CDT4 cells comprised of 1,000,000 samples, each with 17 measurements.\
GoogleNews word vectors is a dataset of 3 million words and phrases derived from a sample of Google News documents and embedded into a 300 dimensional space via word2vec.\

<!-- chunk {"id": "body-0084", "role": "body", "section": "Practical Efficacy", "weight": 1.0} -->

For all the datasets except GoogleNews we use Euclidean distance between vectors. For GoogleNews, as per, we use cosine distance (or angular distance in t-SNE which does support non-metric distances, in contrast to UMAP).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Qualitative Comparison of Multiple Algorithms", "weight": 1.0} -->

We compare a number of algorithms--UMAP, t-SNE, LargeVis, Laplacian Eigenmaps, and Principal Component Analysis --on the, MNIST, Fashion-MNIST, and GoogleNews datasets. The Isomap algorithm was also tested, but failed to complete in any reasonable time for any of the datasets larger than.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Qualitative Comparison of Multiple Algorithms", "weight": 1.0} -->

The Multicore t-SNE package was used for t-SNE. The reference implementation was used for LargeVis. The scikit-learn implementations were used for Laplacian Eigenmaps and PCA. Where possible we attempted to tune parameters for each algorithm to give good embeddings.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Qualitative Comparison of Multiple Algorithms", "weight": 1.0} -->

Historically t-SNE and LargeVis have offered a dramatic improvement in finding and preserving local structure in the data. This can be seen qualitatively by comparing their embeddings to those generated by Laplacian Eigenmaps and PCA in Figure 4. We claim that the quality of embeddings produced by UMAP is comparable to t-SNE when reducing to two or three dimensions. For example, Figure 4 shows both UMAP and t-SNE embeddings of the, MNIST, Fashion MNIST, and Google News datasets. While the precise embeddings are different, UMAP distinguishes the same structures as t-SNE and LargeVis.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Qualitative Comparison of Multiple Algorithms", "weight": 1.0} -->

It can be argued that UMAP has captured more of the global and topological structure of the datasets than t-SNE. More of the loops in the dataset are kept intact, including the intertwined loops. Similarly the global relationships among different digits in the MNIST digits dataset are more clearly captured with 1 (red) and 0 (dark red) at far corners of the embedding space, and 4,7,9 (yellow, sea-green, and violet) and 3,5,8 (orange, chartreuse, and blue) separated as distinct clumps of similar digits. In the Fashion MNIST dataset the distinction between clothing (dark red, yellow, orange, vermilion) and footwear (chartreuse, sea-green, and violet) is made more clear. Finally, while both t-SNE and UMAP capture groups of similar word vectors, the UMAP embedding arguably evidences a clearer global structure among the various word clusters.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Quantitative Comparison of Multiple Algorithms", "weight": 1.0} -->

We compare UMAP, t-SNE, LargeVis, Laplacian Eigenmaps and PCA embeddings with respect to the performance of a $k$-nearest neighbor classifier trained on the embedding space for a variety of datasets. The $k$-nearest neighbor classifier accuracy provides a clear quantitative measure of how well the embedding has preserved the important local structure of the dataset. By varying the hyper-parameter $k$ used in the training we can also consider how structure preservation varies under transition from purely local to non-local, to more global structure. The embeddings used for training the $k$NN classifier are for those datasets that come with defined training labels: PenDigits, COIL-20, Shuttle, MNIST, and Fashion-MNIST.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Quantitative Comparison of Multiple Algorithms", "weight": 1.0} -->

We divide the datasets into two classes: smaller datasets (PenDigits and COIL-20), for which a smaller range of $k$ values makes sense, and larger datasets, for which much larger values of $k$ are reasonable. For each of the small datasets a stratified 10-fold cross-validation was used to derive a set of 10 accuracy scores for each embedding. For the Shuttle dataset a 10-fold cross-validation was used due to constraints imposed by class sizes and the stratified sampling. For MNIST and Fashion-MNIST a 20-fold cross validation was used, producing 20 accuracy scores.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Quantitative Comparison of Multiple Algorithms", "weight": 1.0} -->

In Table 1 we present the average accuracy across the 10-folds for the PenDigits and COIL-20 datasets. UMAP performs at least as well as t-SNE and LargeVis (given the confidence bounds on the accuracy) for $k$ in the range 10 to 40, but for larger $k$ values of 80 and 160 UMAP has significantly higher accuracy on COIL-20, and shows evidence of higher accuracy on PenDigits. Figure 5 provides swarm plots of the accuracy results across the COIL-20 and PenDigits datasets.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Quantitative Comparison of Multiple Algorithms", "weight": 1.0} -->

In Table 2 we present the average cross validation accuracy for the Shuttle, MNIST and Fashion-MNIST datasets. UMAP performs at least as well as t-SNE and LargeVis (given the confidence bounds on the accuracy) for $k$ in the range 100 to 400 on the Shuttle and MNIST datasets (but notably underperforms on the Fashion-MNIST dataset), but for larger $k$ values of 800 and 3200 UMAP has significantly higher accuracy on the Shuttle dataset, and shows evidence of higher accuracy on MNIST. For $k$ values of 1600 and 3200 UMAP establishes comparable performance on Fashion-MNIST. Figure 6 provides swarm plots of the accuracy results across the Shuttle and MNIST and Fashion-MNIST datasets.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Quantitative Comparison of Multiple Algorithms", "weight": 1.0} -->

As evidenced by this comparison UMAP provides largely comparable perfomance in embedding quality to t-SNE and LargeVis at local scales, but performs markedly better than t-SNE or LargeVis at non-local scales. This bears out the visual qualitative assessment provided in Subsection 5.1.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Embedding Stability", "weight": 1.0} -->

Since UMAP makes use of both stochastic approximate nearest neighbor search, and stochastic gradient descent with negative sampling for optimization, the resulting embedding is necessarily different from run to run, and under sub-sampling of the data. This is potentially a concern for a variety of uses cases, so establishing some measure of how stable UMAP embeddings are, particularly under sub-sampling, is of interest. In this subsection we compare the stability under subsampling of UMAP, LargeVis and t-SNE (the three stochastic dimension reduction techniques considered).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Embedding Stability", "weight": 1.0} -->

To measure the stability of an embedding we make use of the normalized Procrustes distance to measure the distance between two potentially comparable distributions. Given two datasets $X = {\{ x_{1},\ldots,x_{N}\}}$ and $Y = {\{ y_{1},\ldots,y_{N}\}}$ such that $x_{i}$ corresponds to $y_{i}$, we can define the Procustes distance between the datasets $d_{P}{(X,Y)}$ in the following manner. Determine $Y^{\prime} = {\{{}_{}^{},\ldots,{}_{}^{}\}}$ the optimal translation, uniform scaling, and rotation of $Y$ that minimizes the squared error $\sum_{i = 1}^{N}{({x_{i} - {}_{}^{}})}^{2}$, and define

<!-- chunk {"id": "body-0096", "role": "body", "section": "Embedding Stability", "weight": 1.0} -->

Since any measure that makes use of distances in the embedding space is potentially sensitive to the extent or scale of the embedding, we normalize the data before computing the Procrustes distance by dividing by the average norm of the embedded dataset. In Figure 7 we visualize the results of using Procrustes alignment of embedding of sub-samples for both UMAP and t-SNE, demonstrating how Procrustes distance can measure the stability of the overall structure of the embedding.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Embedding Stability", "weight": 1.0} -->

Given a measure of distance between different embeddings we can examine stability under sub-sampling by considering the normalized Procrustes distance between the embedding of a sub-sample, and the corresponding sub-sample of an embedding of the full dataset. As the size of the sub-sample increases the average distance per point between the sub-sampled embeddings should decrease, potentially toward some asymptote of maximal agreement under repeated runs. Ideally this asymptotic value would be zero error, but for stochastic embeddings such as UMAP and t-SNE this is not achievable.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Embedding Stability", "weight": 1.0} -->

We performed an empirical comparison of algorithms with respect to stability using the Flow Cytometry dataset due its large size, interesting structure, and low ambient dimensionality (aiding runtime performance for t-SNE). We note that for a dataset this large we found it necessary to increase the default `n_iter` value for t-SNE from 1000 to 1500 to ensure better convergence. While this had an impact on the runtime, it significantly improved the Procrustes distance results by providing more stable and consistent embeddings. Figure 8 provides a comparison between UMAP and t-SNE, demonstrating that UMAP has signifcantly more stable results than t-SNE. In particular, after sub-sampling on 5% of the million data points, the per point error for UMAP was already below any value achieved by t-SNE.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

Benchmarks against the real world datasets were performed on a Macbook Pro with a 3.1 GHz Intel Core i7 and 8GB of RAM for Table 3, and on a server with Intel Xeon E5-2697v4 processors and 512GB of RAM for the large scale benchmarking in Subsections 5.4.1, 5.4.2, and 5.4.3.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

For t-SNE we chose MulticoreTSNE, which we believe to be the fastest extant implementation of Barnes-Hut t-SNE at this time, even when run in single core mode. It should be noted that MulticoreTSNE is a heavily optimized implementation written in C++ based on Van der Maaten's `bhtsne` code.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

As a fast alternative approach to t-SNE we also consider the FIt-SNE algorithm. We used the reference implementation, which, like MulticoreTNSE is an optimized C++ implementation. We also note that FIt-SNE makes use of multiple cores.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

LargeVis was benchmarked using the reference implementation. It was run with default parameters including use of 8 threads on the 4-core machine. The only exceptions were small datasets where we explicitly set the -samples parameter to `n_samples`/100 as per the recommended values in the documentation of the reference implementation.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

The Isomap and Laplacian Eigenmaps implementations in scikit-learn were used. We suspect the Laplacian eigenmaps implementation may not be well optimized for large datasets but did not find a better performing implementation that provided comparable quality results. Isomap failed to complete for the Shuttle, Fashion-MNIST, MNIST and GoogleNews datasets, while Laplacian Eigenmaps failed to run for the GoogleNews dataset.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

To allow a broader range of algorithms to run some of the datasets where subsampled or had their dimension reduced by PCA. The Flow Cytometry dataset was benchmarked on a 10% sample and the GoogleNews was subsampled down to 200,000 data points. Finally, the Mouse scRNA dataset was reduced to 1,000 dimensions via PCA.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Computational Performance Comparisons", "weight": 1.0} -->

Timing were performed for the, COIL100, Shuttle, MNIST, Fashion-MNIST, and GoogleNews datasets. Results can be seen in Table 3. UMAP consistently performs faster than any of the other algorithms aside from on the very small Pendigits dataset, where Laplacian Eigenmaps and Isomap have a small edge.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Scaling with Embedding Dimension", "weight": 1.0} -->

UMAP is significantly more performant than t-SNE^44^4Comparisons were performed against MulticoreTSNE as the current implementation of FIt-SNE does not support embedding into any dimension larger than 2. when embedding into dimensions larger than 2. This is particularly important when the intention is to use the low dimensional representation for further machine learning tasks such as clustering or anomaly detection rather than merely for visualization. The computation performance of UMAP is far more efficient than t-SNE, even for very small embedding dimensions of 6 or 8 (see Figure 9). This is largely due to the fact that UMAP does not require global normalisation (since it represents data as a fuzzy topological structure rather than as a probability distribution). This allows the algorithm to work without the need for space trees ---such as the quad-trees and oct-trees that t-SNE uses ---. Such space trees scale exponentially in dimension, resulting in t-SNE's relatively poor scaling with respect to embedding dimension. By contrast, we see that UMAP consistently scales well in embedding dimension, making the algorithm practical for a wider range of applications beyond visualization.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Scaling with Embedding Dimension", "weight": 1.0} -->

(a) A comparison of run time for UMAP, t-SNE and LargeVis with respect to embedding dimension on the Pen digits dataset. We see that t-SNE scales worse than exponentially while UMAP and LargeVis scale linearly with a slope so slight to be undetectable at this scale.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Scaling with Embedding Dimension", "weight": 1.0} -->

(b) Detail of scaling for embedding dimension of six or less. We can see that UMAP and LargeVis are essentially flat. In practice they appear to scale linearly, but the slope is essentially undetectable at this scale.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Scaling with Ambient Dimension", "weight": 1.0} -->

Through a combination of the local-connectivity constraint and the approximate nearest neighbor search, UMAP can perform effective dimension reduction even for very high dimensional data (see Figure 13 for an example of UMAP operating directly on 1.8 million dimensional data). This stands in contrast to many other manifold learning techniques, including t-SNE and LargeVis, for which it is generally recommended to reduce the dimension with PCA before applying these techniques (see for example).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Scaling with Ambient Dimension", "weight": 1.0} -->

To compare runtime performance scaling with respect to the ambient dimension of the data we chose to use the Mouse scRNA dataset, which is high dimensional, but is also amenable to the use of PCA to reduce the dimension of the data as a pre-processing step without losing too much of the important structure^55^5In contrast to COIL100, on which PCA destroys much of the manifold structure. We compare the performance of UMAP, FIt-SNE, MulticoreTSNE, and LargeVis on PCA reductions of the Mouse scRNA dataset to varying dimensionalities, and on the original dataset, in Figure 10.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Scaling with Ambient Dimension", "weight": 1.0} -->

While all the implementations tested show a significant increase in runtime with increasing dimension, UMAP is dramatically more efficient for large ambient dimensions, easily scaling to run on the original unreduced dataset. The ability to run manifold learning on raw source data, rather than dimension reduced data that may have lost important manifold structure in the pre-processing, is a significant advantage. This advantage comes from the local connectivity assumption which ensures good topological representation of high dimensional data, particularly with smaller numbers of near neighbors, and the efficiency of the NN-Descent algorithm for approximate nearest neighbor search even in high dimensions.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Scaling with Ambient Dimension", "weight": 1.0} -->

Since UMAP scales well with ambient dimension the python implementation also supports input in sparse matrix format, allowing scaling to extremely high dimensional data, such as the integer data shown in Figures 13 and 14.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Scaling with the Number of Samples", "weight": 1.0} -->

For dataset size performance comparisons we chose to compare UMAP with FIt-SNE, a version of t-SNE that uses approximate nearest neighbor search and a Fourier interpolation optimisation approach; MulticoreTSNE, which we believe to be the fastest extant implementation of Barnes-Hut t-SNE; and LargeVis. It should be noted that FIt-SNE, MulticoreTSNE, and LargeVis are all heavily optimized implementations written in C++. In contrast our UMAP implementation was written in Python --- making use of the numba library for performance. MulticoreTSNE and LargeVis were run in single threaded mode to make fair comparisons to our single threaded UMAP implementation.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Scaling with the Number of Samples", "weight": 1.0} -->

We benchmarked all four implementations using subsamples of the GoogleNews dataset. The results can be seen in Figure 11. This demonstrates that UMAP has superior scaling performance in comparison to Barnes-Hut t-SNE, even when Barnes-Hut t-SNE is given multiple cores. Asymptotic scaling of UMAP is comparable to that of FIt-SNE (and LargeVis). On this dataset UMAP demonstrated somewhat faster absolute performance compared to FIt-SNE, and was dramatically faster than LargeVis.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Scaling with the Number of Samples", "weight": 1.0} -->

The UMAP embedding of the full GoogleNews dataset of 3 million word vectors, as seen in Figure 12, was completed in around 200 minutes, as compared with several days required for MulticoreTSNE, even using multiple cores.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Scaling with the Number of Samples", "weight": 1.0} -->

To scale even further we were inspired by the work of John Williamson on embedding integers, as represented by (sparse) binary vectors of their prime divisibility. This allows the generation of arbitrarily large, extremely high dimension datasets that still have meaningful structure to be explored. In Figures 13 and 14 we show an embedding of 30,000,000 data samples from an ambient space of approximately 1.8 million dimensions. This computation took approximately 2 weeks on a large memory SMP. Note that despite the high ambient dimension, and vast amount of data, UMAP is still able to find and display interesting structure. In Figure 15 we show local regions of the embedding, demonstrating the fine detail structure that was captured.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Scaling with the Number of Samples", "weight": 1.0} -->

(b) Lower right spiral and starbursts

<!-- chunk {"id": "body-0118", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

While we believe UMAP to be a very effective algorithm for both visualization and dimension reduction, most algorithms must make trade-offs and UMAP is no exception. In this section we will briefly discuss those areas or use cases where UMAP is less effective, and suggest potential alternatives.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

For a number of use cases the interpretability of the reduced dimension results is of critical importance. Similarly to most non-linear dimension reduction techniques (including t-SNE and Isomap), UMAP lacks the strong interpretability of Principal Component Analysis (PCA) and related techniques such a Non-Negative Matrix Factorization (NMF). In particular the dimensions of the UMAP embedding space have no specific meaning, unlike PCA where the dimensions are the directions of greatest variance in the source data. Furthermore, since UMAP is based on the distance between observations rather than the source features, it does not have an equivalent of factor loadings that linear techniques such as PCA, or Factor Analysis can provide. If strong interpretability is critical we therefore recommend linear techniques such as PCA, NMF or pLSA.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

One of the core assumptions of UMAP is that there exists manifold structure in the data. Because of this UMAP can tend to find manifold structure within the noise of a dataset -- similar to the way the human mind finds structured constellations among the stars. As more data is sampled the amount of structure evident from noise will tend to decrease and UMAP becomes more robust, however care must be taken with small sample sizes of noisy data, or data with only large scale manifold structure. Detecting when a spurious embedding has occurred is a topic of further research.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

UMAP is derived from the axiom that local distance is of more importance than long range distances (similar to techniques like t-SNE and LargeVis). UMAP therefore concerns itself primarily with accurately representing local structure. While we believe that UMAP can capture more global structure than these other techniques, it remains true that if global structure is of primary interest then UMAP may not be the best choice for dimension reduction. Multi-dimensional scaling specifically seeks to preserve the full distance matrix of the data, and as such is a good candidate when all scales of structure are of equal importance. PHATE is a good example of a hybrid approach that begins with local structure information and makes use of MDS to attempt to preserve long scale distances as well. It should be noted that these techniques are more computationally intensive and thus rely on landmarking approaches for scalability.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

It should also be noted that a significant contributor to UMAP's relative global structure preservation is derived from the Laplacian Eigenmaps initialization (which, in turn, followed from the theoretical foundations). This was noted, for example,. The authors of that paper demonstrate that t-SNE, with similar initialization, can perform equivalently to UMAP in a particular measure of global structure preservation. However, the objective function derived for UMAP (cross-entropy) is significantly different from that of t-SNE (KL-divergence), in how it penalizes failures to preserve non-local and global structure, and is also a significant contributor^66^6The authors would like to thank Nikolay Oskolkov for his article (tSNE vs. UMAP: Global Structure) which does an excellent job of highlighting these aspects from an empirical and theoretical basis..

<!-- chunk {"id": "body-0123", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

It is worth noting that, in combining the local simplicial set structures, pure nearest neighbor structure in the high dimensional space is not explicitly preserved. In particular it introduces so called "reverse-nearest-neighbors" into the classical knn-graph. This, combined with the fact that UMAP is preserving topology rather than pure metric structures, mean that UMAP will not perform as well as some methods on quality measures based on metric structure preservation -- particularly methods, such as MDS -- which are explicitly designed to optimize metric structure preservation.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

UMAP attempts to discover a manifold on which your data is uniformly distributed. If you have strong confidence in the ambient distances of your data you should make use of a technique that explicitly attempts to preserve these distances. For example if your data consisted of a very loose structure in one area of your ambient space and a very dense structure in another region region UMAP would attempt to put these local areas on an even footing.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Weaknesses", "weight": 1.0} -->

Finally, to improve the computational efficiency of the algorithm a number of approximations are made. This can have an impact on the results of UMAP for small (less than 500 samples) dataset sizes. In particular the use of approximate nearest neighbor algorithms, and the negative sampling used in optimization, can result in suboptimal embeddings. For this reason we encourage users to take care with particularly small datasets. A slower but exact implementation of UMAP for small datasets is a future project.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Future Work", "weight": 1.5} -->

Having established both relevant mathematical theory and a concrete implementation, there still remains significant scope for future developments of UMAP.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Future Work", "weight": 1.5} -->

A comprehensive empirical study which examines the impact of the various algorithmic components, choices, and hyper-parameters of the algorithm would be beneficial. While the structure and choices of the algorithm presented were derived from our foundational mathematical framework, examining the impacts that these choices have on practical results would be enlightening and a significant contribution to the literature.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Future Work", "weight": 1.5} -->

As noted in the weaknesses section there is a great deal of uncertainty surrounding the preservation of global structure among the field of manifold learning algorithms. In particular this is hampered by the lack clear objective measures, or even definitions, of global structure preservation. While some metrics exist, they are not comprehensive, and are often specific to various downstream tasks. A systematic study of both metrics of non-local and global structure preservation, and performance of various manifold learning algorithms with respect to them, would be of great benefit. We believe this would aid in better understanding UMAP's success in various downstream tasks.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Future Work", "weight": 1.5} -->

Making use of the fuzzy simplicial set representation of data UMAP can potentially be extended to support (semi-)supervised dimension reduction, and dimension reduction for datasets with heterogeneous data types. Each data type (or prediction variables in the supervised case) can be seen as an alternative view of the underlying structure, each with a different associated metric -- for example categorical data may use Jaccard or Dice distance, while ordinal data might use Manhattan distance. Each view and metric can be used to independently generate fuzzy simplicial sets, which can then be intersected together to create a single fuzzy simplicial set for embedding. Extending UMAP to work with mixed data types would vastly increase the range of datasets to which it can be applied. Use cases for (semi-)supervised dimension reduction include semi-supervised clustering, and interactive labelling tools.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Future Work", "weight": 1.5} -->

The computational framework established for UMAP allows for the potential development of techniques to add new unseen data points into an existing embedding, and to generate high dimensional representations of arbitrary points in the embedded space. Furthermore, the combination of supervision and the addition of new samples to an existing embedding provides avenues for metric learning. The addition of new samples to an existing embedding would allow UMAP to be used as a feature engineering tool as part of a general machine learning pipeline for either clustering or classification tasks. Pulling points back to the original high dimensional space from the embedded space would potentially allow UMAP to be used as a generative model similar to some use cases for autoencoders. Finally, there are many use cases for metric learning; see or for example.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Future Work", "weight": 1.5} -->

There also remains significant scope to develop techniques to both detect and mitigate against potentially spurious embeddings, particularly for small data cases. The addition of such techniques would make UMAP far more robust as a tool for exploratory data analysis, a common use case when reducing to two dimensions for visualization purposes.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Future Work", "weight": 1.5} -->

Experimental versions of some of this work are already available in the referenced implementations.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have developed a general purpose dimension reduction technique that is grounded in strong mathematical foundations. The algorithm implementing this technique is demonstrably faster than t-SNE and provides better scaling. This allows us to generate high quality embeddings of larger data sets than had previously been attainable. The use and effectiveness of UMAP in various scientific fields demonstrates the strength of the algorithm.
