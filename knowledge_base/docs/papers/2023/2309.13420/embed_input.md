<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors

Topics include Robustness, Nearest neighbors, Clustering, Datasets, DenMune.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many clustering algorithms fail when clusters are of arbitrary shapes, of varying densities, or the data classes are unbalanced and close to each other, even in two dimensions. A novel clustering algorithm, DenMune is presented to meet this challenge. It is based on identifying dense regions using mutual nearest neighborhoods of size K, where K is the only parameter required from the user, besides obeying the mutual nearest neighbor consistency principle. The algorithm is stable for a wide range of values of K. Moreover, it is able to automatically detect and remove noise from the clustering process as well as detecting the target clusters. It produces robust results on various low and high-dimensional datasets relative to several known state-of-the-art clustering algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data clustering, which is the process of gathering similar data samples into groups/clusters, has been found useful in different fields such as medical imaging (to differentiate between different types of tissues medical_applications_2018 ), market research (to partition consumers into perceptual market segments customers_segmentation_2018 ), document retrieval (to find documents that are relevant to a user query in a collection of documents document_retrieval_2018 ), and fraud detection (to detect suspicious fraudulent patterns) fraud_detection_2019 ), as well as many others clustering_survey_2013.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Partitioning-based Clustering Algorithms", "weight": 1.0} -->

In this category, data objects are divided into non-overlapping subsets (clusters) such that each object lies in exactly one subset. The most well-known and commonly used algorithm in this class is K-means. K-means is heavily dependent on the initial cluster centers, which are badly affected by noise and outliers. A well known variant is K-medoid. K-medoid selects the most centrally located point in a cluster, namely its medoid, as its representative point. Another well-known variant of K-means is KMeans++. It chooses centers at random, but weighs them according to the square distance from the closest already chosen center.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Partitioning-based Clustering Algorithms", "weight": 1.0} -->

A recent algorithm in this area is RS algorithm rs_2018. It belongs to the class of swap-based clustering algorithms that aim at using a sequence of prototype swaps to deal with the inability of K-means in fine-tuning the cluster boundaries globally, although it succeeds locally. By adopting a random swap strategy the computational complexity is reduced and the results are better than those obtained by k-means. Its main limitation is that there is no clear rule how long the algorithm should be iterated.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Partitioning-based Clustering Algorithms", "weight": 1.0} -->

Another recent algorithm in this category is CBKM cbkm_2019. It investigates the extent to which using better initialization (poor initialization can cause the algorithm to get suck at an inferior local minimum) and repeats can improve the k-means algorithm. It is found that when the clusters overlap, furthest point heuristic(Maxmin)can reduce the number of erroneous clusters from 15

<!-- chunk {"id": "body-0007", "role": "body", "section": "Proximity-based Clustering Algorithms", "weight": 1.0} -->

Neighborhood construction is useful in discovering the hidden interrelations between connected patterns apollonius_2018. Proximity can be identified using k-nearest-neighbor (cardinality-based), or identified using $\epsilon$ -neighbourhood (distance-based).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Proximity-based Clustering Algorithms", "weight": 1.0} -->

A recent algorithm in this category is FastDP algorithm fastdp_2019. It focuses on improving the quadratic time complexity of the \"Density peaks\" popular clustering algorithm by using a fast and generic construction of approximate k-nearest neighbor graph both for density and for delta calculation (distance to the nearest point with higher density). The cluster centers are selected so that they have a high value of both delta and density. After that, the remaining points are allocated (joined) to the already formed clusters by merging with the nearest higher density point. The algorithm inherits the problems associated with the original \"Density peaks\" algorithm which include: how to select the initial k cluster centers based on dendity and delta. The algorithm adopts the gamma strategy (which uses the points with high product of the two features(density and delta). the problem of how to threshold the density and delta features.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Proximity-based Clustering Algorithms", "weight": 1.0} -->

Another recent algorithm is NPIR algorithm npir_2020. it finds the nearest neighbors for the points that are already clustered based on the Euclidean distance between them and cluster them accordingly. Different nearest neighbors are selected; from the kNN lists of the already clustered point; at different iterations of the algorithm. Therefore,the algorithm relies on the random and iterative behavior of the partitional clustering algorithms to give quality clustering results. It performs Election, Selection, and Assignment operations to assign data points to appropriate clusters. Therefore, three parameters should are needed: The number of clusters, The indexing ratio (controls the amount of possible reassignment of points) and the number of iterations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Proximity-based Clustering Algorithms", "weight": 1.0} -->

CMUNE cmune, a predecessor of DPC, uses the MNN graph to calculate the density of each point and select the high-density points (also called strong points) as the seeds from which clusters may grow up. A cutoff parameter is also needed to differentiate between strong and weak points. Similar to DPC, the constructed clusters are very sensitive to variations in this parameter. The notion of weak/isolated points has been introduced in to define points which are prone to be classified as noise and, consequently, excluded from the clusters' formation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Hierarchical Clustering Algorithms", "weight": 1.0} -->

In this category, data objects are organized into a tree of group-of-objects. The tree is constructed either from top to bottom or from bottom to top leading to divisive or agglomerative type of algorithms, respectively. Hierarchical clustering has been extensively applied in pattern recognition. Some known examples are Chameleon chameleon and CURE cure. The scalability of hierarchical methods is generally limited due to their time complexity. To address this issue, fast_HC_2018 proposed a fast hierarchical clustering algorithm based on topology training. PHA pha_2013 uses both local and global data distribution information during the clustering process. It can deal with overlapping clusters, clusters of non-spherical shapes and clusters containing noisy data, by making good use of the similarity between the iso-potential contours of a potential field and hierarchical clustering. A more successful variant of hierarchical density is HDBSCAN hdbscan_2017. HDBSCAN provides a clustering hierarchy from which a simplified tree of significant clusters is constructed, then a flat partition composed of clusters extracted from optimal local cuts through the cluster tree.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Hierarchical Clustering Algorithms", "weight": 1.0} -->

Unlike DBSCAN, It can find clusters of variable densities.\RCC rcc_2017 is a clustering algorithm that achieves high accuracy across multiple domains and scales efficiently to high dimensions and large datasets. it optimizes a smooth continuous objective function that allows the algorithm to be extended to perform joint clustering and dimensionality reduction.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Hierarchical Clustering Algorithms", "weight": 1.0} -->

A recent algorithm in this category is FINCH algorithm finch_2019. It is fully parameter-free (i.e. does not require any user defined parameters such as similarity thresholds, number of clusters or a priori knowledge about the data distribution) clustering algorithm.The algorithm is based on the clustering equation which defines an adjacency link matrix that links two points i and j if j is the first neighbor of i or i is the first neighbor of j or both i and j have (share) the same first nearest neighbor. The algorithm belongs to the family of hierarchical agglomerative methods, has low computational overhead and is fast.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Hierarchical Clustering Algorithms", "weight": 1.0} -->

In this paper, a novel clustering algorithm DenMune is presented for the purpose of finding complex clusters of arbitrary shapes and densities in a two-dimensional space. Higher dimensional spaces are first reduced to 2-D using the t-sne algorithm. It can be considered as a variation of the CMUNE algorithm cmune. DenMune requires only one parameter from the user across its two-phases. Other advantages include its ability in automatically detecting, removing and excluding noise from the clustering process. It adopts a voting-system where all data points are voters but only those that receive highest votes are considered clusters' constructors. Moreover, it automatically detects the target clusters and produces robust results with no cutoff parameter needed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Basic Definitions and Mechanisms Underlying the Proposed Algorithm", "weight": 1.0} -->

In this section we describe the basic concepts used in the proposed algorithm and its underlying mechanisms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "K-Mutual-Neighbors Consistency", "weight": 1.0} -->

The principle of K-Mutual-Neighbors (K-MNN) consistency disconnectivity; which states that for any data points in a cluster its MNN should also be in the same cluster; is stronger than the K-nearest Neighbors (KNN) consistency concept. In CMune and CSharp ( cmune, csharp ) the concept of K-MNN is used to develop a clustering framework based on \"Reference Points\", defined in section 2.2, in which dense regions are identified using mutual nearest neighborhoods of size $K$, where $K$ is a user-parameter. Next, sets of points sharing common mutual nearest neighborhoods are considered in an agglomerative process to form the final clusters. This process is controlled by two threshold parameters. In contrast, by properly partitioning the data points into classes (section 2.3) and guided by the principle of K-Mutual-Neighbors consistency (K-MNN), DenMune is able to get rid of these threshold parameters in performing its clustering task (section 2.6).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Refer-To-List, Reference-List and Reference Point", "weight": 1.0} -->

Given a set of points $P =$ {${p_{1},p_{2}},$...$p_{n - 2},p_{n - 1},p_{n}$ }, let ${KNN_{p_{i}\rightarrow}} = {\{ p_{1},p_{2},p_{3},\ldots,p_{k}\}}$ be the K-nearest neighbors of point $p_{i}$. In this paper, we consider that points in a $KNN$ set are sorted, ascendingly, according to their distances from a given reference point. Therefore, $KNN_{p_{i}\rightarrow}$ represents the ordered list of points that $p_{i}$ refers-to, namely, the \"Refer-To List\". If $p_{i} \in$ $KNN_{p_{j}\rightarrow}$, then $p_{i}$ is referred-to by $p_{j}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Refer-To-List, Reference-List and Reference Point", "weight": 1.0} -->

In this case, $p_{j} \in$ $KNN_{p_{i}\leftarrow}$, the set of points considering $p_{i}$ among their K-nearest neighbors. The set ${KNN_{p_{i}\rightarrow}} \cap {KNN_{p_{i}\leftarrow}}$, is the set $MNN_{p_{i}}$ of mutual nearest neighbors of $p_{i}$. It represents a set of dense points associated with point $p_{i}$. Point $p_{i}$ is said to be the \"Representative-Point\" or \"Reference-Point\" of $MNN_{p_{i}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Refer-To-List, Reference-List and Reference Point", "weight": 1.0} -->

As shown in Fig. 1, although the Euclidean distance is a symmetric metric, from the SNN snn perspective (and considering $K = 4$), point $A$ is in $KNN_{B_{\rightarrow}}$, however, $B$ is not in $KNN_{A_{\rightarrow}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "DenMune classification of data points into Strong, Weak and Noise Points", "weight": 1.0} -->

According to the value of the non-negative ratio $r = \frac{|{KNN_{p\leftarrow}}|}{|{KNN_{p\rightarrow}}|} = \frac{|{KNN_{p\leftarrow}}|}{K}$, since ${|{KNN_{p\rightarrow}}|} = K$ (by definition), from DenMune point of view, each data point 'p' in a dataset, belongs to one of the types described in Eq.: Figure 2: Fuzziness of the set W of weak points. N and S denote the noise (r = 0) and strong (r ≥ 1) points, respectively. T is some threshold that partitions the set W into WN and WS. Both sets are automatically detected by DenMune.

<!-- chunk {"id": "body-0021", "role": "body", "section": "DenMune classification of data points into Strong, Weak and Noise Points", "weight": 1.0} -->

Strong Points: satisfy the condition ${|{KNN_{p\leftarrow}}|} \geq {|{KNN_{p\rightarrow}}|}$, or ${|{KNN_{p\leftarrow}}|} \geq K$. This implies that ${|{MNN_{p}}|} =$\| $KNN_{p\rightarrow}$ $\cap$ $KNN_{p\leftarrow}|$ $=$ K. Strong points are also called seed points. Seed points that share non-empty MNN-sets of seeds are the clusters' constructors in the proposed algorithm.

<!-- chunk {"id": "body-0022", "role": "body", "section": "DenMune classification of data points into Strong, Weak and Noise Points", "weight": 1.0} -->

Weak points: satisfy the condition ${|{KNN_{p\leftarrow}}|} < {|{KNN_{p\rightarrow}}|}$. From Eq., it is clear that the boundaries of the set defining the weak points are fuzzy. Fig. 2 illustrates the idea that in DenMune, a weak point either succeeds in joining a cluster or it is considered as noise. For this reason, weak-points are called non-strong (non-seed) points. Hence, the following lemma can be concluded: Lemma: The set of weak points is a fuzzy set. Its boundaries with the sets of strong and noise points are fuzzy. The rule governing the assignment of a weak point to a cluster or rejecting it as noise is, in general, data as well as algorithm dependent.

<!-- chunk {"id": "body-0023", "role": "body", "section": "DenMune classification of data points into Strong, Weak and Noise Points", "weight": 1.0} -->

Noise points, represent points either with empty $MNN$s (corresponding to $r = 0$, which are removed early in phase \\@slowromancapi@ of DenMune algorithm, named as noise of type-1), or weak points that fail to merge with any formed cluster (corresponding to $r \ll 1$, which are removed in phase \\@slowromancapii@ of the algorithm, named as noise of type-2).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Proposed Algorithm: Overview", "weight": 1.0} -->

DenMune is based on a voting system framework where points that receive the largest number of votes (i.e. they belong to the K-nearest neighbors of at least K other points), are marked as dense/ seed points and are used to construct the backbone of the target clusters in phase \\@slowromancapi@ of the algorithm. Points that receive no votes are considered as noise of type-1 and are eliminated from the clustering process. Phase \\@slowromancapii@ deals with the weak points that either survive by merging with the existing clusters, or are eliminated by being considered as noise of type-2.\Table 1 shows the distribution of strong/ seeds and weak/ non-seeds points among the Chameleon's DS7 dataset which includes 10,000 data points, while Fig. 3 illustrates how strong points determine the shapes/ structures of the clusters where weak points can only merge with them.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Proposed Algorithm: Overview", "weight": 1.0} -->

(a) Backbone-constructors (points that receive high votes), also known as strong points. (b) Weak points. (c) DenMune merges some of the weak points in Fig. 2(b) with their nearest clusters. (d) Noise points. Figure 3: Phases of DenMune

<!-- chunk {"id": "body-0026", "role": "body", "section": "Proposed Algorithm: Steps", "weight": 1.0} -->

DenMune involves the following steps: Canonical ordering: Clustering results obtained by DenMune are deterministic, as it orders the set of points $P$ according to $|{KNN_{p\leftarrow}}|$ in a descending order.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Proposed Algorithm: Steps", "weight": 1.0} -->

Noise Removal: Noise points of type-1 as well as those of type-2 are detected and removed in phase \\@slowromancapi@ and phase \\@slowromancapii@, of the algorithm, respectively, as illustrated in Table 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Proposed Algorithm: Steps", "weight": 1.0} -->

Skeleton Construction and Propagation: after removal of type-1 noise points, the remaining points are partitioned into two groups: dense points (seeds) and low-dense points (non-seeds). Only seed points are eligible to construct the skeleton of the target clusters (i.e. the number of seed points represent an upper bound on the number of clusters), while low-dense points are considered in the next phase.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Proposed Algorithm: Steps", "weight": 1.0} -->

To further illustrate the process of clusters propagation, Chameleon's dataset DS7 \\chameleondatasets is used. Several snapshots of the clustering process, are shown in Fig. 4, to illustrate how clusters propagate agglomeratively, and in parallel, in CSharp and DenMune.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Proposed Algorithm: Steps", "weight": 1.0} -->

(a) CSharp: at the 10th iteration (b) DenMune: at the 10th iteration (c) CSharp: at the 50th iteration (d) DenMune: at the 50th iteration (e) CSharp: at the 250th iteration (f) DenMune: at the 250th iteration (g) CSharp: at the 1000th iteration (h) DenMune: at the 1000th iteration (i) CSharp: at the last iteration, 6734th (j) DenMune: at last iteration, 9329th Figure 4: Clusters formation and propagation in DenMune and CSharp. Clusters seeds in DenMune are sparser but their propagation speed is slower. Also, DenMune results are more noise free.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conservative Nature of DenMune", "weight": 1.0} -->

Clusters formation in Phase \\@slowromancapi@: Fig. 5(a), illustrates the evolution of the number of clusters with the number of iterations for Chameleon's dataset. DenMune merges clusters conservatively in contrast to CSharp which is eager to merge clusters. Table 1, indicates that 5858 strong points are found by DenMune during this phase. Therefore, the process of clusters formation stabilizes after $5858$ iterations at the end of phase \\@slowromancapi@, after which no more clusters can be constructed.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conservative Nature of DenMune", "weight": 1.0} -->

Slow Merging of Weak Points in Phase \\@slowromancapii@: weak points are merged one by one, each to the cluster with which it shares the largest number of $MNN$-seeds. Table 1, indicates that out of the $4142$ $({3471 + 671})$ weak points, 3471 of them succeed in merging with the clusters formed in the first phase. The remaining 671 points are considered as noise points of type-2. It is worth to note that DenMune overcomes the lack of the noise threshold $L$ and the merge parameter $M$, used in CSharp, by strengthening the $MNN$ relationship to involve only seed points, the propagation process considers the weak points individually, i.e. one by one, weak points that fail to merge with the formed clusters are detected and removed as noise. As shown in Fig. 5(b), for the DS7 dataset, after 1000 iterations, CSharp clustered 80% of the data points, while DenMune clustered only 50% of them.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conservative Nature of DenMune", "weight": 1.0} -->

This is due to the fact that clusters in DenMune are initially sparse, as shown in Fig. 5(b).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conservative Nature of DenMune", "weight": 1.0} -->

(a) Number of clusters vs number of iterations. (b) Number of clustered data points vs number of iterations. Figure 5: DenMune vs CSharp:(a) Number of clusters and (b) number of clustered data points vs number of iterations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "DenMune Algorithm", "weight": 1.0} -->

Algorithm 1 describes the proposed algorithm, followed by a detailed discussion of its time complexity.

<!-- chunk {"id": "body-0036", "role": "body", "section": "DenMune Algorithm", "weight": 1.0} -->

Input: Data points P = {p1, p2…, pn}, K // size of the neighborhood of a point Output: C // set of generated clusters Construct distance matrix D // Construct the Refer-To-List, KNNpi→, for each point pi ∈ P KNNpi→ ← {j|d(pi, pj) ≤ d(pi, pk)} // For each point pi construct KNNpi← by scanning KNNpj→ and selecting points j having point i in their KNNpj→ // From KNNpi→ and KNNpi←, construct MNNpi 8 MNNpi ← KNNpi→ ∩ KNNpi← Remove the set O, of noise points pi of type-1, satisfying |MNNpi| = 0 Form the sorted list P, The sorting is in a descending order according to |KNNpi←| // P = P - O Form the sorted list S ⊂ P = {pi|pi satisfies |KNNpi←| ≥ |KNNpi→|} Form the set Q of non-seed points, where Q = P − S // Note that Q ⊂ P = {pi|pi

<!-- chunk {"id": "body-0037", "role": "body", "section": "DenMune Algorithm", "weight": 1.0} -->

satisfies |KNNpi←|< |KNNpi→|} CreateClustersSkeleton(S) // Phase \@slowromancapi@ of the algorithm AssignWeakPoints(Q) // Phase \@slowromancapii@ of the algorithm Algorithm 1 DenMune Algorithm Input: Sorted list S of Seed points Output: Sorted list L of the m generated clusters // Loop through all seed points and create clusters skeleton from seeds that share non-empty sets of MNN-seeds L ← ϕ // List of clusters so far ℓ(s ∈ Cj) ← j // label each seed point in Cj as belonging to cluster j // Output the set of generated clusters, m the number of clusters and label each seed point s belonging to a cluster Cj by its corresponding cluster index Input: Sorted lists L of m clusters and Q of non-seed points.

<!-- chunk {"id": "body-0038", "role": "body", "section": "DenMune Algorithm", "weight": 1.0} -->

Output: Updated list L of the m generated clusters. // Loop through all non-seed points and assign each of them to the cluster with which it shares the largest number of MNN-seeds i ← 1 // i is an index for non-seed points 2 Select j such that |{qi ∪ MNNqi} ∩ Cj| is maximum, where j = 1, 2, ⋯, m and Cj ∈ L; ℓ(qi) ← j // label non-seed point qi as belonging to cluster Cj Output the formed clusters. The remaining unlabeled points are noise of type-2.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Time Complexity", "weight": 1.0} -->

Given $N$ the number of data points, $K$ the number of nearest neighbors, $D$ the number of dimensions and $C$ the number of constructed clusters, the time complexity for computing the similarity matrix, between the data points, is ${O{(N^{2})}}*D$ = $O{(N^{2})}$, since $D = 2$ (after dimensionality reduction). This complexity can be reduced to $O{({N{\log N}})}$, by the use of a data structure such as a k-d tree kd-tree-2013 and optimized-quantization_2017, which works efficiently with low dimensional data. The space complexity of this preprocessing phase is $O{({ND})}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Time Complexity", "weight": 1.0} -->

The time complexity of the algorithm can be analyzed as follows: line 2, finding $KNN_{p_{i}\rightarrow}$: needs K iterations for each data point, hence it has a complexity of $O{({NK})}$ lines 3-6, finding $KNN_{p_{i}\leftarrow}$: needs K iterations for each of the N data points, hence it has a complexity of $O{({KN})}$ line 7, finding $MNN$ for each of the N data points, a search for mutual neighborhood is done within the K-nearest neighbors of each point. line 9, sorting points: has a complexity of $O{({N{\log N}})}$, using binary sort.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Time Complexity", "weight": 1.0} -->

CreateClustersSkeleton algorithm has a complexity of $O{({{|S|}*{|R|}*{\log K}})}$, where R is an upper bound on the number of temporarily generated clusters, $m \leq R \leq {|S|}$. Letting O(R) $\approx {|S|}$ and O(\|S\|) $\approx N$, then this complexity becomes $\approx {O{({N^{2}{\log K}})}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Time Complexity", "weight": 1.0} -->

Similarly AssignWeakPoints algorithm has a complexity of $O{({{|Q|}*{|R|}*K})}$, since we iterate through each of the $Q$ weak data points, searching for the maximum intersection between its MNN and each of the formed clusters. Therefore, this complexity becomes $\approx {O{({N^{2}K})}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Time Complexity", "weight": 1.0} -->

The overall time complexity for DenMune algorithm is O($N^{2}K$) and its space complexity is $O{({NK})}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The Euclidean distance has been adopted as a similarity metric for all datasets.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Dimensionality Reduction", "weight": 1.0} -->

Datasets often contain a large number of features, which may even outnumber the observations as in the Arcene dataset. Due to the computational and theoretical challenges associated with high dimensional data, reducing the dimension while maintaining the structure of the original data is desirable dimensionality_reduction. Also, high dimensional data may contain many irrelevant dimensions that suppress each others. These issues can confuse any clustering algorithm by hiding clusters, especially in noisy data. For these reasons, all datasets have been reduced to two dimensions, using the t-sne algorithm tsne-2014, before applying the examined algorithms on them. DenMune has been examined on the ten real datasets listed in Table 3, using various dimensionality reduction techniques. In general, as shown in Table 5, the algorithm performance on a dataset projected to 2-D is better than its performance on the same dataset in its high dimension version. Table 4 shows that DenMune attains its best performance when t-sne is used for dimensionality reduction. t-sne outperforms Principal Component Analysis (PCA), Factor Analysis (FA) and Non-negative Matrix Factorization (NMF) by a large margin.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Agorithms' Implementation and Parameters' setting", "weight": 1.0} -->

For HDBSCAN, Spectral Clustering and Kmeans++ the implementations provided by SKlearn\\sklearnhave been adopted. All other algorithms, NBIR, CBKM, RS, FINCH, FastDP and RCC implementations are provided by authors themselves. DenMune algorithm has been implemented in C++ and integrated with SKlearn, to benefit from its libraries in computing various validation indexes.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Agorithms' Implementation and Parameters' setting", "weight": 1.0} -->

The parameters for each algorithm have been selected according to each algorithm defaults and recommendations. for NPIR, the IR parameter is selected in the range \[0.01, 0.05, 0.10, 0.15, 0.20\], with ten iterations for each run. for HDBSCAN, The primary parameter and the most intuitive parameter is min-cluster-size is selected in the range \[2..100\], for Spectral clustering and KMeans++ the default parameters in SKlearn have been adopted. The number of clusters is set equal to the ground truth. Each algorithm is run 100 times for each dataset and the best performance is recorded, for DenMune, the only used parameter, $K$ is selected in the range \[1..50\] for small datasets and \[1..200\] for big datasets. For MNIST dataset, NPIR failed to scale to adapt to this big dataset even on a cloud server with 128 GB memory, thus all MNIST results were removed from the ranking process for all other algorithms.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

The twenty-one synthetic datasets, listed in Table 3, have been used to demonstrate the efficiency of our proposed algorithm. All datasets are 2-D except DIM datasets which are reduced from 32, 128 and 512 to 2-D to make them easy to visualize. They are of different sizes (G2 and DIM datasets). They have clusters of different densities, shapes (Spiral, Compound, Flame and Pathbased datasets) and degree of overlapping (S1 and G2 datasets). Revealing the inherent structure of these datasets is challenging for most heuristic algorithms. Three metrics have been recorded The F1 scores are recorded in Tables 6 and 7 for synthetic and real datasets, respectively. The Normalized Mutual Information, NMI is recorded in Tables 8 and 9 for synthetic and real datasets, respectively, and the Adjusted Rand Index, ARI is recorded in Tables 10 and 11 for synthetic and real datasets, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

We adopt a ranking system to order algorithms, based on their clustering performance, as measured by F1, NMI and ARI scores. The lower the rank of an algorithm, the better its clustering quality for the datasets examined. Three ranking values are added to the bottom of Tables (6: 11) as follows: Total rank: sum of the ranks of an algorithm over the examined datasets Average rank: Total rank divided by the number of datasets and rank: the algorithm ranking among the set of examined algorithms, given in ascending order (lower ranks preferred).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

The ground truth for all datasets are visualised using the t-sne algorithm as shown in Fig. (14 and 15) for synthetic and real datasets, respectively.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

In general, the results show that DenMune outperforms all other algorithms for the majority of the datasets examined. Denmune has the lowest rank values for each of the three validity indexes used in the assessment for both synthetic, Tables( 6, 8 and 10) and real datasets, Tables( 7, 9 and 11).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Based on F1-score, Denmune outperforms the other algorithms for twenty-eight out of the thirty-six datasets. For the remaining datasets.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

\(1\) Arcene dataset: all algorithms (except for Finch and RCC algorithms) outperform Denmune (+8%). G2-2-50 dataset: CBKM, RS and FastDP algorithms outperform DenMune (+2%). Iris dataset: NPIR, CBKM, RS and Spectral outperform DenMune (+1%: +8%). Glass dataset: Spectral Clustering outperforms DenMune slightly (+2%). SCC dataset: RS algorithm outperforms all other algorithms for this dataset with noticable F1-score (84%) then comes RCC with (77%), while Denmune scores only 68%. Seeds dataset: NPIR and CBKM outperform DenMune (+1%: +2%).. WDBC dataset: NPIR, RS and FastDP outperform DenMune (+2%: +7%) Yeast dataset: CBKM, FINCH, RCC, KMeans++ outperform DenMune (+1%: +5%).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

We are going to investigate why DenMune outperform for the majority of datasets, then we will ilusterate why some algorithms outperform DenMune for some datasets.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

DenMune has a noticeable better performance over other algorithms for many datasets such as A1 dataset (+33%), A2 dataset (+14%), Compound dataset (+8%), D31 dataset (+34%), Dim-128 dataset (+20%), Pathbased dataset (+10%), S1 dataset (+22%), S2 datset (+25%), Optical-digits dataset (+27%), Pendigits dataset (+24%), Ecoli dataset (+6%) and MNIST datasets (+6%). This is due to the framework DenMune adopts in its clustering process which allows it to distinguish real clusters in noisy data, even if they are attached to each others or overlapped as long as they are of distinguishable densities.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

On contrary to DenMune, density-based algorithms such as HDBSCAN fails when clusters have different densities, that is why HDBSCAN performs badly on Compound and Pathbased datsets, Fig. 9(i) ‣ Figure 10 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors") and Fig. 11(i) ‣ Figure 12 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors"), respectively. Also, on Aggregation dataset it merges some spherical shapes incorrectly due to the strong linkage between them, Fig. 7(i) ‣ Figure 8 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors"). nevertheless, it performs well on spiral dataset, Fig.8(i) ‣ Figure 9 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors") since clusters are well separated.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

FastDP speeds up the clustering process by building an approximate k-nearest neighbor (kNN) graph using an iterative algorithm. Its main advantage is that it removes the quadratic time complexity limitation of density peaks and allows clustering of very large datasets. FastDP can not select the right cluster centers on Pathbased and Spiral datasets Fig. (11(f) ‣ Figure 12 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors") and 8(f) ‣ Figure 9 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors")) respectively. Its performance goes down when working on datasets with extremely uneven distributions as in Compound dataset, Fig. 9(f) ‣ Figure 10 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors"). On contrary to the speed achieved by the algorithm, results obtained showed lower clustering quality. This is obvious from the validity indexes values achieved by the algorithm.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Centroid based algorithms fail when the centroid of a cluster is closer to other data points rather than the data points of its representative cluster, That is why KMeans++ and spectral clustering perform badly on arbitrary shaped data. They can detect clusters of globular shapes specifically when clusters are well separated as in DIM datasets. Datasets with varying clusters' overlap degrade validations scores even if the clusters are of globular shapes as in G2 datasets. Although,they have an advantage over traditional KMmeans, they perform badly on noisy or data with overlapping clusters.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

NPIR uses an indexing ratio, IR to control the amount of possible reassignment of points. The higher IR value means that the assigned points have more possibility for reassignment. The reassignment process does not guarantee algorithm to assign points to the correct clusters specifically when data are noisy as in A1 and A2 datasets (F1= 0.48 and 0.40 respectively) or clusters with different degree of cluster overlap as in S1 and S1 datasets (F1= 0.43 and 0.41 respectively). It is obvious that NPIR performs badly when data are noisy or clusters are of different densities and attached to each other. It performs better when clusters are well separated even if they are of different densities as in Jain and Aggregation datasets Fig.10(c) ‣ Figure 11 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors") and Fig.7(c) ‣ Figure 8 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors"), respectively.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

A noticeable issue we experienced during examining the algorithm is that it could not scale when working on the MNIST dataset and failed to run even on a cloud server with 128 GB memory. We tested NPIR for IR in the range \[0.01, 0.05, 0.10, 0.15, 0.20.\]. We found that NPIR performs well when IR is set to 0.01. However, it achieved its highest score for some datasets such as Mouse, Ecoli and Compound datasets for IR=0.15 and for Flame dataset on IR=0.20. Tuning NPIR to yield the best results is not an easy task.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

We can observe easily that the performance of all clustering algorithms decrease for datasets with clusters' overlap as in S1, S2, A1 and A2 datasets except for DenMune algorithm. DenMune can deal with overlaping clusters as long as they are of distinguishable densities. DenMune outperformed the other algorithms, for these datasets, with a remarkable margin.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

RCC performs well on some datasets such as G2, Spiral and R15 datatsets, but it performs too badly on DIM datasets, a high-dimensional datasets where clusters are well separated even in the higher dimensional space, Fig(13(f) ‣ Figure 14 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors"):13(h) ‣ Figure 14 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors")).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

For synthetic datasets, FINCH has the closest F1-score to DenMune while being faster. However, for the same datasets, its performance based on the NMI and ARI metrics (Tables 9 and 11 as well as Figs 7(e) ‣ Figure 8 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors") to 12(e) ‣ Figure 13 ‣ Acknowledgement ‣ DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors") ) is bad. The same applies for real datasets.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

RS algorithm adopts a randomized search strategy, which is simple to implement and efficient. It archived good quality clustering, and if iterated longer, it would finds the correct clustering with high probability. CBKM algorithm uses a better initialization technique and/or repeating (restarting) the algorithm to improve the quality clustering of KMeans to overcome issues with clusters overlap and clusters of unbalanced sizes. Authors of CBKM observed that choosing an initialization technique like Maxmin can compensate for the weaknesses of k-means and recommended that repeating k-means 10--100 times; each time taking a random point as the first centroids and selecting the rest using the Maxmin heuristic would improve the quality clustering. We believe that increasing the number of runs (from 100 to say 1000) would slightly increase the clustering quality of RS, CBKM and NBIR since they have random initial states. We found that RS and CBKM algorithms have the most reasonable results achieved for both real and synthetic datasets assessed by F1, NMI and ARI scores. In general, they have the closest rank to DenMune.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Also, we found that DenMune performs moderately for small size datasets where DenMune has not enough chance to build robust $KNN$ framework to distinguish clusters, this is the case for Iris and Arcene datasets.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Finally, we recorded the Homogeneity and Completeness of DenMune in Tables(12 and 13). A clustering result satisfies homogeneity if each cluster contains only members of a single class, while it satisfies completeness if all members of a given class are assigned to the same cluster. It is easy to observe that DenMune has high homogeneity and completeness scores, which explain the goodness of its clustering quality.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Speed Performance", "weight": 1.0} -->

The speed of DenMune has been compared to the speed of CMune and CSharp, as shown in Fig.6a. The data set considered is the MNIST dataset (with 70000 patterns), after dividing it into subsets, each of size 1000 patterns. The subsets are added incrementally, and the speed of the algorithm is recorded with each increment. The time considered is the time required for running the core clustering algorithms, excluding the pre-processing time for computing the proximity matrix and dimensionality reduction. The time is measured in seconds. The adopted algorithms as well as the proposed algorithm have been executed on a cloud with the following configuration: Intel E5 Processor, up to 128 GB RAM, and running Linux operating system (Ubuntu 18.04 LTS). Another test is conducted to examine speed versus the number of K-nearest neighbors used, as shown in Fig.6b (a) DenMune speed performance (b) DenMune: Speed vs number of K- nearest neighbors. Figure 6: (a) Speed of DenMune compared to the speed of CMune and CSharp on the MNIST dataset.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Speed Performance", "weight": 1.0} -->

(b) Speed of DenMune vs number of K- nearest neighbors.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, a novel shared nearest neighbors clustering algorithm DenMune, is presented. It utilizes the MNN size to calculate the density of each point and chooses the high-density points as the seeds from which clusters may grow up. In contrast to recent similar algorithms, such as DPC and CMune, no cut-off parameter is needed from the user of DenMune. Guided by the principle of Mutual Nearest-Neighbors (MNN) consistency, DenMune prioritizes points according to a voting system and partitions them into seeds and non-seeds. Seed points determine the number as well as the skeleton of the clusters while non-seed points either merge with the formed clusters or are considered as noise. It has the ability to automatically detect the number of clusters and has shown robustness for datasets of different shapes and densities.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We examined the sensitivity of DenMune to changes in K, the number of nearest neighbors (the only parameter required by the algorithm) on three real datasets with $K$ in the range \[1..200\] and recorded the NMI for each dataset as shown in Fig. 7. The stability of DenMune, with respect to K, makes it a good candidate for data exploration and visualization since it works in a two-dimensional feature space. Algorithms that rely on several parameters such as CSharp, CMune, HDBSCAN and DPC can offer more flexibility than single parameter algorithms such as DenMune, but at the expense of the time needed for their tuning.
