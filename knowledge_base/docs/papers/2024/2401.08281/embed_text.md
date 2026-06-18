## Introduction

The emergence of deep learning has induced a shift in how complex data is stored and searched, noticeably by the development of *embeddings*. Embeddings are vector representations, typically produced by a neural network, that map (embed) the input media item into a vector space, where the locality encodes the semantics of the input. Embeddings are extracted from various forms of media: words \[(https://arxiv.org/html/2401.08281v4#bib.bib59), (https://arxiv.org/html/2401.08281v4#bib.bib10)\], text \[(https://arxiv.org/html/2401.08281v4#bib.bib24), (https://arxiv.org/html/2401.08281v4#bib.bib40)\], images \[(https://arxiv.org/html/2401.08281v4#bib.bib15), (https://arxiv.org/html/2401.08281v4#bib.bib69)\], users and items for recommendation \[(https://arxiv.org/html/2401.08281v4#bib.bib65)\]. They can even encode object relations, for instance multi-modal text-image or text-audio relations \[(https://arxiv.org/html/2401.08281v4#bib.bib31), (https://arxiv.org/html/2401.08281v4#bib.bib70)\].

Embeddings are employed as an intermediate representation for further processing, e.g. self-supervised image embeddings are input to shallow supervised image classifiers \[(https://arxiv.org/html/2401.08281v4#bib.bib14), (https://arxiv.org/html/2401.08281v4#bib.bib15)\]. They are also leveraged as a pretext task for self-supervision \[(https://arxiv.org/html/2401.08281v4#bib.bib18)\]. In fact, embeddings are a compact intermediate representation that can be re-used for several purposes.

In this paper, we consider embeddings used directly to compare media items. The embedding extractor is designed so that the distance between embeddings reflects the similarity between their corresponding media. As a result, conducting neighborhood search in this vector space offers a direct implementation of similarity search between media items.

Similarity search is also popular for tasks where end-to-end learning would not be cost-efficient. For example, a k-nearest-neighbor classifier is more efficient to upgrade with new training samples than a classification neural net. This explains why the usage of industrial database management systems (DBMS), that offer a vector storage and search functionality, has increased in the last years. These DBMS are at the junction of traditional databases and Approximate Nearest Neighbor Search (ANNS) algorithms. Until recently, the latter were mostly considered for specific use-cases or in research.

From a practical perspective, the embedding extraction and the vector search algorithm are bound by an "embedding contract" on the embedding distance:

The embedding extractor, typically a neural network in modern systems, is trained so that distances between embeddings are aligned with the task to perform.

The vector index performs neighbor search among the embedding vectors as accurately as possible w.r.t. exact search results given the agreed distance metric.

Faiss is a library for ANNS. The core library is a collection of C++ source files without external dependencies. Faiss also provides a comprehensive Python wrapper for its C++ core. It is designed to be used both from simple scripts and as a building block of a DBMS. In contrast with other libraries that focus on a single indexing method, Faiss is a toolbox that contains a variety of indexing methods that commonly involve a chain of components (preprocessing, compression, non-exhaustive search, etc.). In this paper, we show that there exists a choice between a dozen index types, and the optimal one usually depends on the problem's constraints.

To summarize what Faiss is *not*: Faiss does not extract features -- it only indexes embeddings that have been extracted by a different mechanism; Faiss is not a service -- it only provides functions that are run as part of the calling process on the local machine; Faiss is not a database -- it does not provide concurrent write access, load balancing, sharding, transaction management or query optimization. The scope of the library is intentionally limited to ANNS algorithmic implementation.

The basic structure of Faiss is an *index* that can have multiple implementations described in this paper. An index can store a number of *database vectors* that are progressively added to it. At search time, a *query vector* is submitted to the index. The index returns the database vector that is closest to the query vector w.r.t. the Euclidean distance. There are many variants of this functionality: instead of just the nearest neighbor, $k$ nearest neighbors are returned; instead of a fixed number of neighbors, only the vectors within a certain range are returned; batches of vectors can be searched in parallel; other metrics besides the Euclidean distance are supported; the search can use either CPUs or GPUs.

Since its open-source release in 2017, Faiss has emerged as one of the most popular vector search libraries, boasting 37k GitHub stars and more than 5200 citations of its GPU implementation paper \[(https://arxiv.org/html/2401.08281v4#bib.bib47)\]. The Faiss packages have been downloaded 6M times. Major vector database companies, such as Zilliz and Pinecone, either rely on Faiss as their core engine or have reimplemented Faiss algorithms.

This paper exposes the design principles of Faiss. A similarity search library has to trade off between different constraints (Section (https://arxiv.org/html/2401.08281v4#S3 "3 Performance axes of a vector search library ‣ The Faiss Library")) using two main tools: vector compression (Section (https://arxiv.org/html/2401.08281v4#S4 "4 Compression levels ‣ The Faiss Library")) and non-exhaustive search (Section (https://arxiv.org/html/2401.08281v4#S5 "5 Non-exhaustive search ‣ The Faiss Library")). We also review a few applications of Faiss for trillion-scale indexing, text retrieval, data mining, and content moderation (Section (https://arxiv.org/html/2401.08281v4#S7 "7 Faiss applications ‣ The Faiss Library")). The appendix discusses how Faiss is structured and engineered to be flexible and usable from other tools. Throughout the paper, we refer to functions or classes in the Faiss codebase^11^1[https://github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss) as well as the documentation^22^2[https://faiss.ai/](https://faiss.ai/) using this specific style.

## Related work

### Indexing methods

Over the past decade, a steady stream of papers about indexing methods has been published. Faiss encompasses a broad range of algorithms, catering to a diverse spectrum of use cases.

One of the most popular approaches in the industry is to employ Locality Sensitive Hashing (LSH) as a way to compress embeddings into compact codes. In particular, the cosine sketch \[(https://arxiv.org/html/2401.08281v4#bib.bib16)\] produces binary vectors such that the Hamming distance is an estimator of the cosine similarity between the original embeddings. The compactness of these sketches enables storing and searching very large databases of media content \[(https://arxiv.org/html/2401.08281v4#bib.bib54)\], without the requirement to store the original embeddings. We refer the reader to the early survey by \[(https://arxiv.org/html/2401.08281v4#bib.bib91)\] for research on binary codes.

Since the original work introducing product quantization search \[(https://arxiv.org/html/2401.08281v4#bib.bib44)\], quantization-based ANN has emerged as a powerful alternative to binary codes \[(https://arxiv.org/html/2401.08281v4#bib.bib90)\]. We refer the reader to the survey by \[(https://arxiv.org/html/2401.08281v4#bib.bib58)\] that discusses numerous research works related to quantization-based compact codes.

The term LSH can also refer to indexing with multiple partitions, such as E2LSH \[(https://arxiv.org/html/2401.08281v4#bib.bib22)\]. However, we do not consider this scenario as the performance is generally inferior to that of learnt partitions \[(https://arxiv.org/html/2401.08281v4#bib.bib66)\]. Early data-aware methods that proved successful on large datasets include multiple partitions based on kd-tree or hierarchical k-means \[(https://arxiv.org/html/2401.08281v4#bib.bib62)\]. They are often combined with compressed-domain representation and are especially appropriate for very large-scale settings \[(https://arxiv.org/html/2401.08281v4#bib.bib43), (https://arxiv.org/html/2401.08281v4#bib.bib44)\].

After the introduction of NN-descent \[(https://arxiv.org/html/2401.08281v4#bib.bib26)\], graph-based ANN algorithms have emerged as a viable alternative to space partitioning methods. Notably, HNSW, currently the most popular indexing method \[(https://arxiv.org/html/2401.08281v4#bib.bib55)\] for medium-sized dataset, has been implemented in HNSWlib.

### Software packages

Most of the research works on vector search have been open-sourced, and some of these evolved in relatively comprehensive software packages for vector search. For instance, FLANN includes several index types and a distributed implementation described extensively in \[(https://arxiv.org/html/2401.08281v4#bib.bib62)\]. The first implementation of product quantization relied on the Yael library \[(https://arxiv.org/html/2401.08281v4#bib.bib27)\], that already had a few of the Faiss principles: optimized primitives for clustering methods (GMM and k-means), scripting language interface (Matlab and Python) and benchmarking operators. NMSlib, a package originally designed for text retrieval, was the first to include HNSW \[(https://arxiv.org/html/2401.08281v4#bib.bib11)\]. It also provides several index types. The HNSWlib library later became the reference implementation of HNSW \[(https://arxiv.org/html/2401.08281v4#bib.bib55)\]. Google's SCANN library is a thoroughly optimized implementation of IVFPQ \[(https://arxiv.org/html/2401.08281v4#bib.bib44)\] on SIMD and includes several index variants for various database scales. SCANN was open-sourced but the accompanying paper \[(https://arxiv.org/html/2401.08281v4#bib.bib36)\] omits to mention the engineering optimizations that underpin the library's remarkable speed. DiskANN \[(https://arxiv.org/html/2401.08281v4#bib.bib79)\] is Microsoft's foundational graph-based vector search library. It was originally built to leverage hybrid RAM/flash memory, but now offers a RAM-only version and was later extended to perform efficient updates \[(https://arxiv.org/html/2401.08281v4#bib.bib78)\], out-of-distribution search \[(https://arxiv.org/html/2401.08281v4#bib.bib42)\] and filtered search \[(https://arxiv.org/html/2401.08281v4#bib.bib34)\].

Faiss was open-sourced concurrently with a publication \[(https://arxiv.org/html/2401.08281v4#bib.bib47)\] that details the GPU implementation of several index types. The present paper complements this previous work by describing the library as a whole.

Concurrently, various software libraries from the database world were extended or developed to do vector search. Milvus \[(https://arxiv.org/html/2401.08281v4#bib.bib89)\] uses its Knowhere library, which relies on Faiss as one of its core engines. Pinecone \[(https://arxiv.org/html/2401.08281v4#bib.bib12)\] initially relied on Faiss, although the engine was later rewritten in Rust. Weaviate \[(https://arxiv.org/html/2401.08281v4#bib.bib86)\] is a composite retrieval engine that includes vector search among other methods.

### Theoretical guarantees

Several approximate algorithms were inspired by the Johnson-Lindenstrauss lemma, which stipulates that one can embed a set of high-dimensional points into a lower-dimensional space while almost preserving the distances. For instance, under certain assumptions about the data distribution, LSH algorithms based on random partitioning (e.g. projection) provide statistical guarantees for the range search problem. As this objective is only a proxy to the problem of nearest neighbor search, there are no formal guarantees w.r.t. any metrics such as nearest-neighbor recall. In practice, algorithms based on random partitioning are significantly outperformed by data-aware partitioning \[(https://arxiv.org/html/2401.08281v4#bib.bib66), (https://arxiv.org/html/2401.08281v4#bib.bib2)\]. Similarly, graph-based algorithms are difficult to compare from a theoretical perspective if the data distribution is unknown.

Techniques based on vector compression, either with binary sketches or quantization, often correspond to estimators of the target distance. For some of these methods, the variance of the estimator can be computed in closed form \[(https://arxiv.org/html/2401.08281v4#bib.bib16), (https://arxiv.org/html/2401.08281v4#bib.bib44)\], characterizing the distance estimation error. Again, the quality of the estimator is only a proxy for the actual k-nearest-neighbor problem.

Considering these factors and the importance of execution speed, the quality of ANN search is typically evaluated by experimental comparisons on publicly available benchmarks.

### Benchmarks and competitions

The leading benchmark for million-scale datasets is ANN-benchmarks \[(https://arxiv.org/html/2401.08281v4#bib.bib3)\]. It compares about 50 implementations of ANNS. The big-ANN \[(https://arxiv.org/html/2401.08281v4#bib.bib76)\] challenge introduced large-scale settings, with 6 datasets containing 1 billion vectors each. Faiss was used as a baseline for the challenge and multiple submissions were derived from it. The 2023 edition of the challenge is at a smaller scale (10M vectors) but introduces more complex tasks, including a filtered track where Faiss served as a baseline method \[(https://arxiv.org/html/2401.08281v4#bib.bib75)\].

### Datasets

Early datasets are based on keypoint features like SIFT \[(https://arxiv.org/html/2401.08281v4#bib.bib53)\] used in image matching. We use BIGANN \[(https://arxiv.org/html/2401.08281v4#bib.bib46)\], a dataset of 128-dimensional SIFT features. Later, when global image descriptors produced by neural nets became popular, the Deep1B dataset was released \[(https://arxiv.org/html/2401.08281v4#bib.bib6)\], with 96-dimensional image features extracted with Google LeNet \[(https://arxiv.org/html/2401.08281v4#bib.bib82)\]. For this paper, we introduce a dataset of 768-dimensional Contriever text embeddings \[(https://arxiv.org/html/2401.08281v4#bib.bib40)\] that are compared using inner product similarity. The embeddings are computed with English Wikipedia passages. The higher dimension of these embeddings is representative of contemporary applications.

Each dataset has 10k query vectors and 20M to 350M training vectors. We indicate the size of the database explicitly, for example "Deep1M" means the database contains the 1M first vectors of Deep1B. The training, database and query vectors are sampled randomly from the same distribution: we do not address out-of-distribution data \[(https://arxiv.org/html/2401.08281v4#bib.bib42), (https://arxiv.org/html/2401.08281v4#bib.bib8)\] in this work.

## Performance axes of a vector search library

ith database vector

number of requested results

radius for range search

number of centroids for quantization

Table 1: Common notations used throughout the paper.

Vector search is a well-defined, unambiguous operation. In its simplest formulation, given a set of database vectors ${\{ x_{i},i = 1..N\}} \subset {\mathbb{R}}^{d}$ and a query vector $q \in {\mathbb{R}}^{d}$, it computes

The minimum can be computed with a direct algorithm by iterating over all database vectors: this is *brute force search*. A slightly more general and complex operation is to compute the $k$ nearest neighbors of $q$:

where $argsort$ returns the indices of the array to sort it by increasing distances and $\ast$ means that an output is ignored. This is what the search method of a Faiss index returns. A related operation is to find all the elements that are within some $\varepsilon$ distance to the query:

which is computed with the range_search method.

### Distance measures

In the equations above, we leave the definition of the distance undefined. Faiss aims at supporting a range of distance metrics, but in order to avoid overloading the library, it leaves out metrics that are equivalent up to a monotonous transformation of distances (like Euclidean vs. squared Euclidean) or up to a preprocessing of the input vectors (like Mahalanobis or cosine, see below). The full list of metrics is in Appendix [A.6](https://arxiv.org/html/2401.08281v4#A1.SS6 "A.6 Faiss metric types ‣ Appendix A Appendix ‣ The Faiss Library").

The most commonly used distances in Faiss are the L2 distance, the cosine similarity and the inner product similarity (for the latter two, the $argmin$ should be replaced with an $argmax$). These measures have useful analytical properties: for example, they are invariant under $d$-dimensional rotations.

In terms of applications, the Euclidean distance is the default for comparing vectors \[(https://arxiv.org/html/2401.08281v4#bib.bib53)\]. When vectors are obtained by metric learning, the cosine similarity is often used to avoid collapsing or exploding embeddings \[(https://arxiv.org/html/2401.08281v4#bib.bib23)\]. Maximum inner product search (MIPS) is most often used for recommendation systems that require to compare user and item embeddings \[(https://arxiv.org/html/2401.08281v4#bib.bib65)\].

These measures can be made equivalent by preprocessing transformations on the query and/or the database vectors. Table (https://arxiv.org/html/2401.08281v4#S3.T2 "Table 2 ‣ Distance measures. ‣ 3 Performance axes of a vector search library ‣ The Faiss Library") summarizes the preprocessing transformations mapping different measures. To our knowledge, some of these were already identified \[(https://arxiv.org/html/2401.08281v4#bib.bib7), (https://arxiv.org/html/2401.08281v4#bib.bib37)\], while others are new.

Note that vectors transformed in this manner have a very anisotropic distribution \[(https://arxiv.org/html/2401.08281v4#bib.bib60)\]: the additional dimension incurred for many transformations is not homogeneous w.r.t. other dimensions. This can make indexing more difficult, in particular using product or scalar quantization methods. See Section [4.2](https://arxiv.org/html/2401.08281v4#S4.SS2 "4.2 Vector preprocessing ‣ 4 Compression levels ‣ The Faiss Library") for mitigations.

{x^{\prime} = {\lbrack x;{- {\alpha/2}}\rbrack}} \\
{y^{\prime} = {\lbrack y;{{\| y\|}^{2}/\alpha}\rbrack}}
{x^{\prime} = {\lbrack x;{- {\alpha/2}};0\rbrack}} \\
{y^{\prime} = {\lbrack\beta y;\beta \parallel y \parallel^{2}/\alpha;}} \\

{x^{\prime} = {\lbrack x;0\rbrack}} \\
{y^{\prime} = {\lbrack y;\sqrt{\alpha^{2} - {\| y\|}^{2}}\rbrack}}
{x^{\prime} = {\lbrack x;0\rbrack}} \\
{y^{\prime} = {\lbrack{\alphay};\sqrt{1 - {\|{\alphay}\|}^{2}}\rbrack}}

Table 2: One wants to compare a query vector x and a database vector y given a particular metric (rows). The table indicates how to preprocess (x,y) ↦ (x′,y′) so that an index with another metric (columns) returns the nearest neighbors for the source metric. Some cases require adding 1 or 2 extra dimensions to the original vectors, as is denoted by the vector concatenation symbol [.;.]. The positive scalar parameters α and β are arbitrary and chosen to avoid negative values under a square root.

### Brute force search

Developing an efficient implementation of brute force search is not trivial \[(https://arxiv.org/html/2401.08281v4#bib.bib21), (https://arxiv.org/html/2401.08281v4#bib.bib47)\]. It requires an efficient way of computing the distances and an efficient way of keeping track of the $k$ smallest distances.

Computing distances in Faiss is performed either by direct distance computations, or, when query vectors are provided in large enough batches, using a matrix multiplication decomposition \[(https://arxiv.org/html/2401.08281v4#bib.bib47), Equation 2\]. The corresponding Faiss functions are exposed in knn and knn_gpu for CPU and GPU, respectively.

Collecting the top-$k$ smallest distances is usually done via a binary heap on CPU \[(https://arxiv.org/html/2401.08281v4#bib.bib27), section 2.1\] or a sorting network on GPU \[(https://arxiv.org/html/2401.08281v4#bib.bib47), (https://arxiv.org/html/2401.08281v4#bib.bib63)\]. For larger values of $k$, it is more efficient to use a reservoir: an unordered result buffer of size $k^{\prime} > k$ that is resized to $k$ when it overflows.

Faiss's IndexFlat implements brute force search. However, for large datasets this approach becomes too slow. In low dimensions, there are branch-and-bound methods that yield exact search results. However, in large dimensions they provide no speedup over brute force search \[(https://arxiv.org/html/2401.08281v4#bib.bib93)\].

Besides, for some applications, small variations in distances are not significant enough to distinguish application-level positive and negative items \[(https://arxiv.org/html/2401.08281v4#bib.bib83)\]. In these cases, approximate nearest neighbor search (ANNS) becomes interesting.

### Metrics for Approximate Nearest Neighbor Search

With ANNS, the user accepts imperfect results, which opens the door to a new solution design space. With exact search, the database is represented as a plain matrix. For ANNS, the database may be preprocessed into an indexing structure, more simply referred to as an *index* in the following.

### Accuracy metrics

In ANNS the accuracy^33^3Metrics involved in a tradeoff are indicated in a specific font. is measured as a discrepancy with the exact search results from ((https://arxiv.org/html/2401.08281v4#S3.E2 "In 3 Performance axes of a vector search library ‣ The Faiss Library")) and ((https://arxiv.org/html/2401.08281v4#S3.E3 "In 3 Performance axes of a vector search library ‣ The Faiss Library")). Note that this is an intermediate goal: the end-to-end accuracy depends on how well the distance metric correlates with the item matching objective and the quality of ANNS, which is what we measure here.

Accuracy of k-nearest neighbor search is generally evaluated with "$n$-recall@$k$", which is the fraction of the $n$ ground-truth nearest neighbors that are in the $k$ first search results (with $n \leq k$). Most often $k$ $=$ $1$ or $n$ $=$ $k$ (in which case the measure is a.k.a. "intersection measure"). When $n$ = $k$ = $1$, the recall measure and intersection are the same, and the recall is called "accuracy". In some publications \[(https://arxiv.org/html/2401.08281v4#bib.bib44)\], recall@$k$ means 1-recall@$k$, while in others \[(https://arxiv.org/html/2401.08281v4#bib.bib77)\] it corresponds to $k$-recall@$k$.

For range search, the exact search result is obtained by applying ((https://arxiv.org/html/2401.08281v4#S3.E3 "In 3 Performance axes of a vector search library ‣ The Faiss Library")), using threshold $\varepsilon$. To yield result list $\hat{R}$, the approximate search uses a (possibly different) threshold $\varepsilon^{\prime}$. Thus, standard retrieval metrics can be computed: precision $P = {{|{R \cap \hat{R}}|}/{|\hat{R}|}}$ and recall $R = {{|{R \cap \hat{R}}|}/{|R|}}$. By sweeping $\varepsilon^{\prime}$ from small to large, the result list $\hat{R}$ increases, producing a precision-recall curve. The area under the PR-curve is the mean average precision score of range search \[(https://arxiv.org/html/2401.08281v4#bib.bib76)\]. Setting $\varepsilon^{\prime} \neq \varepsilon$ is relevant when approximate vector representations distort the distance metric (more on this in Section (https://arxiv.org/html/2401.08281v4#S4 "4 Compression levels ‣ The Faiss Library")).

For vector encoder-decoder pairs, the standard metric is the mean squared error (MSE) between the original vector and the reconstructed vector \[(https://arxiv.org/html/2401.08281v4#bib.bib44), (https://arxiv.org/html/2401.08281v4#bib.bib4), (https://arxiv.org/html/2401.08281v4#bib.bib39)\]. For an encoder $C$ and a decoder $D$, the MSE is:

### Resource metrics

The other axes of the trade-off are related to computing resources. During search, the search time and memory usage are the main constraints. If compression is used, then, the memory usage can be smaller than what is required to store the original vectors.

The index may need to store training data, which incurs a constant memory overhead before any vector is added to the index. The index can also add per-vector memory overhead to the memory used to store each vector. This is the case for graph indexes, that need to store graph edges for each vector. The memory usage is more complex for settings with hybrid storage such as RAM + flash or GPU memory + RAM.

The index building time is also a resource constraint. It may be decomposed into a training time, which is independent of the number of vectors added to the index, and the addition time per vector.

In distributed settings or flash-backed storage, the relevant metric is the number of I/O operations (IOPS), as each read operation fetches a whole page. Data layouts that minimize IOPs \[(https://arxiv.org/html/2401.08281v4#bib.bib79)\] are more efficient than small random accesses. Another possibly limiting factor is the amount of extra memory needed to pre-compute lookup tables used to speed up search.

### Tradeoffs

Most often only a subset of metrics matter. For example, when a very large number of searches are performed on a fixed index, the index building time does not matter. Or when the number of vectors is so small that the raw database fits in RAM multiple times, then the memory usage does not matter. We refer to the metrics that we care about as the *active constraints*. Note that accuracy is always an active constraint because if it did not matter, returning random results would be sufficient (Faiss does actually provide an IndexRandom used in some benchmarking tasks).

In the following sections, we consider that the active constraints are speed, memory usage and accuracy. As such, we measure the speed and accuracy of several index types and hyperparameter settings under a fixed memory budget.

### Exploring search-time settings

Figure 1: Example of exploration of a parameter space with 3 parameters (an IndexIVFPQ with polysemous codes and HNSW coarse quantizer, running on the Deep100M dataset). The total number of configurations is 5808, but only 398 experiments are run. We also show the set of operating points obtained with just 50 experiments.

For a fixed index, there are often one or several search-time hyperparameters that trade off speed with accuracy. For example, the nprobe hyperparameter for an IndexIVF, see Section (https://arxiv.org/html/2401.08281v4#S5 "5 Non-exhaustive search ‣ The Faiss Library"). In general, we define hyperparameters as discrete scalar values such that when the value is higher, the speed decreases and the accuracy increases. We can then keep only the Pareto-optimal settings, defined as settings that are the fastest for a given accuracy, or equivalently, that have the highest accuracy for a given time budget \[(https://arxiv.org/html/2401.08281v4#bib.bib80)\].

Exploring the Pareto-optimal frontier when there is a single hyper-parameter consists in sweeping over its values with a certain level of granularity, and measuring the corresponding speed and accuracy.

For multiple hyperparameters, the Pareto frontier can be recovered by exhaustively testing the Cartesian product of these parameters. However, the number of settings to test grows exponentially with the number of parameters.

### Pruning the parameter space

one can leverage the monotonous nature of the hyperparameters for efficient pruning. We note a tuple of $n$ hyper-parameters $\pi = {(p_{1},\ldots,p_{n})} \in \mathcal{P} = {\mathcal{P}_{1} \times \ldots \times \mathcal{P}_{n}}$, and $\leq$ a partial ordering on $\mathcal{P}$: ${(p_{1},..,p_{n})} \leq {(p_{1}^{\prime},..,p_{n}^{\prime})}\Leftrightarrow\forall i,p_{i} \leq p_{i}^{\prime}$. Let $S{(\pi)}$ and $A{(\pi)}$ be the speed and accuracy obtained with this tuple of parameters. $\mathcal{P}^{\ast} \subset \mathcal{P}$ is the set of Pareto-optimal settings:

Since the individual parameters have a monotonic effect on speed and accuracy, we have

Thus, if a subset $\hat{\mathcal{P}} \subset \mathcal{P}$ of settings is already evaluated, the following upper bounds hold for a new setting $\pi \in \mathcal{P}$:

If any previous evaluation Pareto-dominates these bounds, the setting $\pi$ does not need to be evaluated:

In practice, we evaluate settings from $\mathcal{P}$ in a random order. The pruning becomes more and more effective throughout the process. It is also more effective when the number of parameters is larger. Figure (https://arxiv.org/html/2401.08281v4#S3.F1 "Figure 1 ‣ 3.4 Exploring search-time settings ‣ 3 Performance axes of a vector search library ‣ The Faiss Library") shows an example with ${|\mathcal{P}|} = 5808$ combined parameter settings. The pruning from ((https://arxiv.org/html/2401.08281v4#S3.E9 "In Pruning the parameter space. ‣ 3.4 Exploring search-time settings ‣ 3 Performance axes of a vector search library ‣ The Faiss Library")) reduces this to 398 experiments, out of which ${|\mathcal{P}^{\ast}|} = 87$ are optimal. The Faiss OperatingPoints object implements this pruning.

### Refining (IndexRefine)

One can combine a fast but inaccurate index with a slower, more accurate search. \[(https://arxiv.org/html/2401.08281v4#bib.bib46), (https://arxiv.org/html/2401.08281v4#bib.bib79), (https://arxiv.org/html/2401.08281v4#bib.bib36)\]. This is done by querying the fast index to retrieve a shortlist of results. The more accurate search then computes more accurate results only for the shortlist. This requires the accurate index to allow efficient random access to database vectors. Some implementations use a slower storage (e.g. flash) for the second index \[(https://arxiv.org/html/2401.08281v4#bib.bib79), (https://arxiv.org/html/2401.08281v4#bib.bib81)\].

For the first-level index, the relevant accuracy metric is the recall at a rank equal to the shortlist size. Thus, 1-recall@1000 can be a relevant metric, even if the end application does not use the 1000^th^ neighbor.

Several methods based on this refining principle do not use two separate indexes. Instead, they use two ways of interpreting the same compressed vectors: a fast and inaccurate decoding and a slower but more accurate decoding \[(https://arxiv.org/html/2401.08281v4#bib.bib28), (https://arxiv.org/html/2401.08281v4#bib.bib29), (https://arxiv.org/html/2401.08281v4#bib.bib61), (https://arxiv.org/html/2401.08281v4#bib.bib1), (https://arxiv.org/html/2401.08281v4#bib.bib39)\] are based on this principle. The polysemous codes method \[(https://arxiv.org/html/2401.08281v4#bib.bib28)\] is implemented in Faiss's IndexIVFPQ.

## Compression levels

Faiss supports various vector codecs: these are methods to compress vectors so that they take up less memory. A compression method $C:{{\mathbb{R}}^{d}\rightarrow{\{ 1,\ldots,K\}}}$, a.k.a. a quantizer, converts a continuous multi-dimensional vector to an integer. This integer is equivalent to a bit string of code size $\lceil{\log_{2}K}\rceil$. The decoder $D:{{\{ 1,\ldots,K\}}\rightarrow{\mathbb{R}}^{d}}$ reconstructs an approximation of the vector from the integer. The decoder can only reconstruct a finite number, $K$, of distinct vectors.

The search of ((https://arxiv.org/html/2401.08281v4#S3.E1 "In 3 Performance axes of a vector search library ‣ The Faiss Library")) becomes approximate:

where the codes $C_{i} = {C{(x_{i})}}$ are precomputed and stored in the index. This is the asymmetric distance computation (ADC) \[(https://arxiv.org/html/2401.08281v4#bib.bib44)\]. The symmetric distance computation (SDC) corresponds to the case when the query vector is also compressed:

Most Faiss indexes perform ADC as it is more accurate: no accuracy is lost on the query vectors. SDC is useful when there is also a storage constraint on the queries or for indexes where SDC is faster to compute than ADC. The naive computation of ((https://arxiv.org/html/2401.08281v4#S4.E10 "In 4 Compression levels ‣ The Faiss Library")) decompresses the vectors, which has an impact on speed. In most cases, the distance can be computed in the compressed domain.

### The vector codecs

### The k-means vector quantizer (Kmeans)

The ideal vector quantizer minimizes the MSE between the original and the decompressed vectors. This is formalized in the Lloyd necessary conditions for the optimality of a quantizer \[(https://arxiv.org/html/2401.08281v4#bib.bib52)\].

The k-means algorithm directly implements these conditions. The $K$ centroids of k-means are an explicit enumeration of all possible vectors that can be reconstructed.

The k-means vector quantizer is very accurate but the memory usage and encoding complexity grow exponentially with the code size. Therefore, k-means is impractical to use beyond roughly 3-byte codes, corresponding to 16M centroids.

### Scalar quantizers

Scalar quantizers encode each dimension of a vector independently.

A very classical and simple scalar quantizer is LSH (IndexLSH), where each vector component is encoded in a single bit by comparing it to a threshold. The threshold can be fixed to 0 or trained. Faiss supports efficient SDC search of binary vectors via the IndexBinary objects, see Section [4.5](https://arxiv.org/html/2401.08281v4#S4.SS5 "4.5 Binary indexes ‣ 4 Compression levels ‣ The Faiss Library").

The ScalarQuantizer also supports uniform quantizers that encode a vector component into 8, 6 or 4 bits -- referred to as `SQ8`, `SQ6`, `SQ4`. A scale and offset determine which values are reconstructed. They can be set separately for each dimension on the whole vector. The IndexRowwiseMinMax stores vectors with per-vector normalizing coefficients. Lower-precision 16-bit floating point representations are also considered as scalar quantizers, `` and ``.

### Multi-codebook quantizers

Faiss contains several multi-codebook quantization (MCQ) options. They are built from $M$ vector quantizers that can reconstruct $K$ distinct values each. The codes produced by these methods are of the form ${(c_{1},\ldots,c_{M})} \in {\{ 1,\ldots,K\}}^{M}$, i.e. each code indexes one of the quantizers. The number of reconstructed vectors is $K^{M}$ and the code size is thus $M{\lceil{\log_{2}{(K)}}\rceil}$.

The product quantizer (ProductQuantizer, also noted PQ) is a simple MCQ that splits the input vector into $M$ sub-vectors and quantizes them separately \[(https://arxiv.org/html/2401.08281v4#bib.bib44)\] with a k-means quantizer. At reconstruction time, the individual reconstructions are concatenated to produce the final code. In the following, we will use the notation `PQ6x10` for a product quantizer with 6 sub-vectors each encoded in 10 bits ($M = 6$, $K = 2^{10}$).

Additive quantizers are a family of MCQ where the reconstructions from sub-quantizers are summed up together. Finding the optimal encoding for a vector given the codebooks is NP-hard \[(https://arxiv.org/html/2401.08281v4#bib.bib4)\], so, in practice, additive quantizers use heuristics to find near-optimal codes.

Faiss supports two types of additive quantizers. The residual quantizer (ResidualQuantizer) proceeds sequentially, by encoding the difference (residual) of the vector to encode and the one that is reconstructed by the previous sub-quantizers \[(https://arxiv.org/html/2401.08281v4#bib.bib19)\]. The local search quantizer (LocalSearchQuantizer) starts from a sub-optimal encoding of the vector and locally explores neighbording codes in a simulated annealing process \[(https://arxiv.org/html/2401.08281v4#bib.bib56), (https://arxiv.org/html/2401.08281v4#bib.bib57)\]. We use notations `LSQ6x10` and `RQ6x10` to refer to additive quantizers with 6 codebooks of size $2^{10}$.

Faiss also supports a combination of PQ and additive quantizer, ProductResidualQuantizer. In that case, the vector is split in sub-vectors that are encoded independently with additive quantizers \[(https://arxiv.org/html/2401.08281v4#bib.bib5)\]. The codes from the sub-quantizers are concatenated. We use the notation `PRQ2x6x10` to indicate that vectors are split in 2 and encoded independently with `RQ6x10`, yielding a total of 12 codebooks of size $2^{10}$.

### Hierarchy of quantizers

Although this is not by design, there is a strict ordering between the quantizers described before. This means that quantizer $i + 1$ can have the same set of reproduction values as quantizer $i$: it is more flexible and more data adaptive. The hierarchy of quantizers is:

the binary representation with bits +1 and -1 can be represented as a scalar quantizer with 1 bit per component;

the scalar quantizer is a product quantizer with 1 dimension per sub-vector and uniform per-dimension quantizer;

the product quantizer is a product-additive quantizer where the additive quantizer has a single level;

the product additive quantizer is an additive quantizer where within each codebook all components outside one sub-vector are set to 0 \[(https://arxiv.org/html/2401.08281v4#bib.bib4)\];

the additive quantizer is the general case where the codebook entries correspond to all possible reconstructions obtained by adding elements from the subquantizers.

The implications of this hierarchy are the degrees of freedom for the reproduction values of quantizer $i + 1$ are larger than for $i$, so it is more accurate quantizer $i + 1$ has a higher capacity so it consumes more resources in terms of training time and storage overhead than $i$. In practice, the product quantizer often offers a good trade-off, which explains its wide adoption. The corresponding Faiss Quantizer objects are listed in Appendix [A.7](https://arxiv.org/html/2401.08281v4#A1.SS7.SSS0.Px2 "Quantizer objects. ‣ A.7 API index of the Faiss library ‣ Appendix A Appendix ‣ The Faiss Library").

Figure 2: Comparison of additive quantizers in terms of encoding time vs. accuracy (MSE). Lower values are better for both. We consider two different regimes: Deep1M (low-dimensional) to 8-bytes codes and Contriever1M (high dimensional) to 64-byte codes. For some RQ variants, we indicate the beam size setting at which that trade-off was obtained.

### Vector preprocessing

Applying transformations to input vectors before encoding can enhance the effectiveness of certain quantizers. In particular, $d$-dimensional rotations are commonly used, as they preserve comparison metrics like cosine, L2 and inner product.

Scalar quantizers assign the same number of bits per vector component. However, for distance comparisons, if specific vector components have a higher variance, they have more impact on the distances. In other works, a variable number of bits are assigned per component \[(https://arxiv.org/html/2401.08281v4#bib.bib71)\]. However, it is simpler to apply a random rotation to the input vectors, which in Faiss can be done with a RandomRotationMatrix. The random rotation spreads the variance over all the dimensions without changing the measured distances.

An important transform is the Principal Component Analysis (PCA), that reduces the number of dimensions $d$ of the input vectors to a user-specified $d^{\prime}$. This operation (PCAMatrix) is the orthogonal linear mapping that best preserves the variance of the input distribution. It is often beneficial to apply PCA to large input vectors before quantizing them as k-means quantizers are more likely to "fall" in local minima in high-dimensional spaces \[(https://arxiv.org/html/2401.08281v4#bib.bib51), (https://arxiv.org/html/2401.08281v4#bib.bib45)\].

The OPQ transformation \[(https://arxiv.org/html/2401.08281v4#bib.bib33)\] is a rotation of the input space that decorrelates the distribution of each sub-vector of a product quantizer^44^4In Faiss terms, OPQ and ITQ are preprocessings. The actual quantization is performed by a subsequent product quantizer or binarization step.. This makes PQ more accurate in the case where the variance of the data is concentrated on a few components. The Faiss implementation OPQMatrix combines OPQ with a dimensionality reduction. The ITQ transformation \[(https://arxiv.org/html/2401.08281v4#bib.bib35)\] similarly rotates the input space prior to binarization (ITQMatrix).

### Faiss additive quantization options

Additive quantizers exist in two main variants: the residual quantizer and local search quantizer. They are more complex than most quantizers because the index building time must be taken into account. In fact, the accuracy of an additive quantizer of a certain size can always be increased at the cost of an increased encoding time (and training time).

Additive quantizers are based on $M$ codebooks $T_{1},{\ldotsT_{M}}$ of size $K$. The decoding of code ${C{(x)}} = {(c_{1},\ldots,c_{M})}$ is

Thus, decoding is unambiguous. However, there is no practical way to encode vectors optimally, let alone train the codebooks. Enumerating all possible encodings is of exponential complexity in $M$.

### The residual quantizer (RQ)

RQ encodes a vector $x$ sequentially. At stage $m$, RQ picks the entry that best reconstructs the residual of $x$ w.r.t. the previous encoding steps:

This greedy approach tends to get trapped in local minima. As a mitigation, the encoder maintains a beam of max_beam_size of possible codes and picks the best code at stage $M$. This parameter adjusts the trade-off between encoding time and accuracy.

To speed up the encoding, the norm of ((https://arxiv.org/html/2401.08281v4#S4.E13 "In The residual quantizer (RQ). ‣ 4.3 Faiss additive quantization options ‣ 4 Compression levels ‣ The Faiss Library")) can be decomposed into the sum of:

${\|{T_{m}{\lbrack j\rbrack}}\|}^{2}$ is precomputed and stored;

$\left\| {{\sum_{i = 1}^{m - 1}{T_{i}{\lbrack c_{i}\rbrack}}} - x} \right\|^{2}$ is the encoding error of the previous step $m - 1$;

$- {2{\langle{T_{m}{\lbrack j\rbrack}},x\rangle}}$ is computed on entry to the encoding (it is the only computation complexity that depends on $d$);

$2{\sum_{\ell = 1}^{m - 1}{\langle{T_{m}{\lbrack j\rbrack}},{T_{\ell}{\lbrack c_{\ell}\rbrack}}\rangle}}$ is also precomputed.

This decomposition is used when use_beam_LUT is set. It is interesting only if $d$ is large and when $M$ is small because the storage and compute requirements of the last term grow quadratically with $M$.

### The local search quantizer (LSQ)

At encoding time, LSQ starts from a suboptimal encoding of the vector and proceeds with a simulated annealing optimization to refine the codes. At each optimization step, LSQ randomly flips codes and then uses Iterated Conditional Mode (ICM) to optimize the new encoding. The number of optimization steps is set with encode_ils_iters. The LSQ codebooks are trained via an expectation-maximization procedure (similar to k-means).

Figure 3: Accuracy vs. code size trade-off for different codecs on the Deep1M and Contriever1M datasets. We show Pareto-optimal variants with larger dots and indicate the quantizer in text for some of them. Note that contriever vectors can be encoded to MSE=2 ⋅ 10−4 in 768 bytes with SQ8 (that setting is widely out-of-range for the plot).

### Compressed-domain search

The distances are computed without decompressing the stored vectors. It is acceptable to perform pre-computations on the query vector $q$ because the cost of these pre-computations is amortized over many query-to-code distance comparisons.

Additive quantizer inner products can be computed in the compressed domain:

The lookup tables ${LUT}_{m}$ are computed when a query vector comes in, similar to product quantizer search \[(https://arxiv.org/html/2401.08281v4#bib.bib44)\].

This decomposition does not work to compute L2 distances. As a workaround, Faiss uses the decomposition \[(https://arxiv.org/html/2401.08281v4#bib.bib4)\]

Thus, the term ${\| x^{\prime}\|}^{2}$ must be available at search time. Using the AdditiveQuantizer.search_type configuration, it can be appended in the stored code (ST_norm_float32), possibly compressed (ST_norm_qint8, ST_norm_qint4,...). It can also be computed on the fly (ST_norm_from_LUT) with

There, the norms and dot products are stored in the same lookup tables as the one used for beam search. Therefore, it trades off search time for memory overhead to store codes.

Figure (https://arxiv.org/html/2401.08281v4#S4.F2 "Figure 2 ‣ Hierarchy of quantizers. ‣ 4.1 The vector codecs ‣ 4 Compression levels ‣ The Faiss Library") shows the trade-off between encoding time and MSE. Given a code size, it is more accurate to use a smaller number of sub-quantizers $M$ and a higher $K$. GPU encoding for LSQ does not help systematically. The LUT-based encoding of RQ is interesing for RQ/PRQ quantization when the beam size is larger. In the 64-byte regime, we observe that LSQ is not competitive with RQ. PLSQ and PRQ progressively become more competitive for larger memory budgets. They are also faster, since they operate on smaller vectors.

### Vector compression benchmark

Figure (https://arxiv.org/html/2401.08281v4#S4.F3 "Figure 3 ‣ The local search quantizer (LSQ). ‣ 4.3 Faiss additive quantization options ‣ 4 Compression levels ‣ The Faiss Library") shows the trade-off between code size and accuracy for many variants of the codecs. Additive quantizers are the best options for small code sizes. For larger code sizes, it is beneficial to independently encode several sub-vectors with product-additive quantizers. LSQ is more accurate than RQ for small codes, but does not scale well to longer codes. Note that product quantizers are a bit less accurate than additive quantizers, but given their low encoding time they remain an attractive option. The scalar quantizers perform well for very long codes and are even faster. The 2-level PQ options are what an IVFPQ index uses as encoding: a first-level coarse quantizer and a second level refinement of the residual (more about this in Section [5.1](https://arxiv.org/html/2401.08281v4#S5.SS1.SSS0.Px2 "Encoding residuals. ‣ 5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library")).

### Binary indexes

Binary quantization with symmetric distance computations is a pattern that has been commonly used \[(https://arxiv.org/html/2401.08281v4#bib.bib91), (https://arxiv.org/html/2401.08281v4#bib.bib13)\]. In this setup, distances are computed in the compressed domain as Hamming distances. ((https://arxiv.org/html/2401.08281v4#S4.E11 "In 4 Compression levels ‣ The Faiss Library")) reduces to:

where ${{C{(q)}},C_{i}} \in {\{ 0,1\}}^{d}$. Hamming distances are integers in $\{ 0..d\}$. Although they are crude approximations for continuous domain distances, they are fast to compute, do not require any specific context, and are easy to calibrate in practice.

The IndexBinary indexes support addition and search directly from binary vectors. They offer a compact representation and leverage optimized instructions for distance computations.

The simplest IndexBinaryFlat index performs exhaustive search. Three options are offered for non-exhaustive search:

IndexBinaryIVF is a binary counterpart for the inverted-list IndexIVF index described in [5.1](https://arxiv.org/html/2401.08281v4#S5.SS1 "5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library").

IndexBinaryHNSW is a binary counterpart for the hierarchical graph-based IndexHNSW index described in [5.2](https://arxiv.org/html/2401.08281v4#S5.SS2 "5.2 Graph based ‣ 5 Non-exhaustive search ‣ The Faiss Library").

IndexBinaryHash uses prefix vectors as hashes to cluster the database (rather than spheroids as with inverted lists), and searches only the clusters with closest prefixes.

Finally, theIndexBinaryFromFloat is provided for convenience. It wraps an arbitrary index and offers a binary vector interface for its operations.

## Non-exhaustive search

Non-exhaustive search is the cornerstone of fast search implementations for datasets larger than around $N$=10k vectors. In that case, the aim of the indexing method is to quickly focus on a subset of database vectors that are most likely to contain the search results.

A method to do this is Locality Sensitive Hashing (LSH). It amounts to projecting the vectors on a random direction \[(https://arxiv.org/html/2401.08281v4#bib.bib22)\]. The offsets on that direction are then discretized into buckets where the database vectors are stored. At search time, only the nearest buckets to the query vector's projection are visited. In practice, *several* projection directions are needed to make it accurate, at the cost of search time and memory usage. A fundamental drawback of this method is that it is not data-adaptive, although some improvements are possible \[(https://arxiv.org/html/2401.08281v4#bib.bib66)\].

An alternative way of pruning the search space is to use tree-based indexing. In that case, the dataset is stored in the leaves of a tree \[(https://arxiv.org/html/2401.08281v4#bib.bib62)\]. When querying a vector, the search starts at the root node. At each internal node, the search descends into one of the child nodes depending on a decision rule. The decision rule depends on how the tree was built: for a KD-tree it is the position w.r.t. a hyperplane, for a hierarchical k-means, it is the proximity to a centroid.

LSH and tree-based methods both aim to extend classical database search structures to vector search, because they have a favorable complexity (constant or logarithmic in $N$). However, these methods do not scale well for dimensions above 10.

Faiss implements two non-exhaustive search approaches that operate at different memory vs. speed trade-offs: inverted file and graph-based.

### Inverted files

IVF indexing is a technique that clusters the database vectors at indexing time. This clustering uses a vector quantizer (the *coarse quantizer*) that outputs $K_{IVF}$ distinct indices (the nlist field of the IndexIVF object). The coarse quantizer's $K_{IVF}$ reproduction values are called *centroids*. The vectors of each cluster (possibly compressed) are stored contiguously into inverted lists, forming an inverted file (IVF). At search time, only a subset of $P_{IVF}$ clusters are visited (a.k.a. nprobe). The subset is formed by searching the $P_{IVF}$ nearest centroids, as in ((https://arxiv.org/html/2401.08281v4#S3.E2 "In 3 Performance axes of a vector search library ‣ The Faiss Library")).

### Setting the number of lists

The $K_{IVF}$ parameter is central. In the simplest case, when $P_{IVF}$ is fixed, the coarse quantizer is exhaustive, the inverted lists contain uncompressed vectors, and the inverted lists are all the same size, then the number of distance computations is

reaching a minimum when $K_{IVF} = \sqrt{P_{IVF}N}$. This yields the usual recommendation to set $P_{IVF}$ proportional to $\sqrt{N}$.

In practice, this is just a rough approximation because the $P_{IVF}$ has to increase with the number of lists in order to keep a fixed accuracy the inverted lists sizes are not balanced often the coarse quantizer is not exhaustive itself, so the quantization uses fewer than $K_{IVF}$ distance computations, for example it is common to use a non-exhaustive HNSW index to perform the coarse quantization.

The *imbalance factor* is the relative variance of inverted list sizes \[(https://arxiv.org/html/2401.08281v4#bib.bib84)\]. At search time, if the inverted lists all have the same length, this factor is 1. If they are unbalanced, the expected number of distance computations is multiplied by this factor.

Figure (https://arxiv.org/html/2401.08281v4#S5.F4 "Figure 4 ‣ Setting the number of lists. ‣ 5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library") shows the optimal settings of $K_{IVF}$ for various database sizes. For a small $K_{IVF} = 4096$, the coarse quantization runtime is negligible and the search time increases linearly with the database size. On larger datasets, it is beneficial to increase $K_{IVF}$. As in ((https://arxiv.org/html/2401.08281v4#S5.E18 "In Setting the number of lists. ‣ 5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library")), the ratio $K_{IVF}/\sqrt{N}$ is roughly 15 to 20. Note that this ratio depends on the data distribution and the target accuracy. Interestingly, in a regime where $K_{IVF}$ is larger than the optimal setting for $N$ (e.g. $K_{IVF} = 2^{18}$ and $N =$`<!-- -->`{=html}5M), the $P_{IVF}$ needed to reach the target accuracy *decreases* with the dataset size, and so does the search time. This is because when $K_{IVF}$ is fixed and $N$ increases, for a given query vector, the nearest database vector is either the same or a new one that is closer, so it is more likely to be found in a quantization cluster nearer to the query.

With a faster non-exhaustive coarse quantizer (e.g. HNSW) it is even more useful to increase $K_{IVF}$ for larger databases, as the coarse quantization becomes relatively cheap. At the limit, when $K_{IVF} = N$, then all the work is done by the coarse quantizer. In this scenario, the limiting factor becomes the memory overhead of the coarse quantizer.

By fitting a model of the form $t = {t_{0}N^{\alpha}}$ to the timings of the fastest index in Figure (https://arxiv.org/html/2401.08281v4#S5.F4 "Figure 4 ‣ Setting the number of lists. ‣ 5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library"), we can derive a scaling rule for the IVF indexes:

Thus, with this model, the search time increases faster for higher accuracy targets, but $\alpha < 0.5$, so the runtime dependence on the database size is below $\sqrt{N}$. This empirical complexity analysis has been used before for graph-based indices \[(https://arxiv.org/html/2401.08281v4#bib.bib92)\].

Figure 4: Search time as a function of the database size N for BigANN1B with different KIVF settings. The PIVF is set so that the 1-recall@1 is 90%. The full lines indicate that the coarse quantizer is exact, the dashed lines rely on a HNSW coarse quantizer. For some setting we indicate the ratio $K_{IVF}/\sqrt{N}$

### Encoding residuals

In general, it is more accurate to compress the residuals of the database vectors w.r.t. the centroids \[(https://arxiv.org/html/2401.08281v4#bib.bib44), Eq. \]. This is either because the norm of the residuals is lower than that of the original vectors, or because residual encoding is a way to take into account a-priori information from the coarse quantizer. In Faiss, this is controlled via the IndexIVF.by_residual flag, which is set to true by default.

Figure (https://arxiv.org/html/2401.08281v4#S5.F5 "Figure 5 ‣ Encoding residuals. ‣ 5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library") shows that encoding residuals is beneficial for shorter codes. For larger codes, the contribution of the residual is less important. Indeed, as the original data is 96-dimensional, it can be compressed to 64 bytes relatively accurately. Note that using higher $K_{IVF}$ also improves the accuracy of the quantizer with residual encoding. From a pure encoding point of view, the additional bits of information brought by the coarse quantizer (${\log_{2}{(K_{IVF})}} = 10$ or $14$) improve the accuracy more when used in this residual encoding than if they would added to increase the size of a PQ.

Figure 5: Comparing IVF indexes with and without residual encoding for KIVF ∈ {210, 214} on the Deep1M dataset (d=96 dimensions), with different product quantization settings. We measure the recall that can be achieved within 3000 distance comparisons.

### Spherical clustering for inner product search

Efficient indexing for maximum inner product search (MIPS) faces multiple issues: the distribution of query vectors is often different from the database vector distribution, most notably in recommendation systems \[(https://arxiv.org/html/2401.08281v4#bib.bib65)\]; the MIPS datasets are diverse, an algorithm that obtains a good performance on some dataset will perform badly on another. Besides, \[(https://arxiv.org/html/2401.08281v4#bib.bib60)\] show that using the preprocessing formulas in Section (https://arxiv.org/html/2401.08281v4#S3.SS0.SSS0.Px1 "Distance measures. ‣ 3 Performance axes of a vector search library ‣ The Faiss Library") is a suboptimal way of indexing for MIPS.

Several specialized clustering and indexing methods were developed for MIPS \[(https://arxiv.org/html/2401.08281v4#bib.bib36), (https://arxiv.org/html/2401.08281v4#bib.bib60)\]. Instead, Faiss implements a modification of k-means clustering, spherical k-means \[(https://arxiv.org/html/2401.08281v4#bib.bib25)\], which normalizes the IVF centroids at each iteration. One of the MIPS issues is due to database vectors of very different norms (when they are normalized, MIPS is equivalent to L2 search). High-norm centroids "attract" the database vectors in their clusters, which increases the imbalance factor. Spherical k-means is designed to avoid this issue.

Figure (https://arxiv.org/html/2401.08281v4#S5.F6 "Figure 6 ‣ Spherical clustering for inner product search. ‣ 5.1 Inverted files ‣ 5 Non-exhaustive search ‣ The Faiss Library") shows that for the Contriever MIPS dataset, the imbalance factor is high. It is reduced by using IP assignment instead of L2, and even more with spherical k-means.

Figure 6: Precision vs. speed trade-off for the MIPS contriever1M dataset. The compared settings are whether the coarse quantizer assignement is done using L2 distance (default) or IP assignment and whether the k-means clustering does a normalization at each iteration (spherical, IP and L2 assignment are equivalent in that case). The imbalance factors are indicated for each setting.

### Big batch search

A common use case for ANNS is search with very large query batches. This appears for applications such as large-scale data deduplication. In this case, rather than loading an entire index in memory and processing queries one small batch at a time, it can be more memory-efficient to load only the quantizer, quantize the queries, and then iterate over the index by loading it one chunk at a time. Big-batch search is implemented in the module contrib.big_batch_search.

### Graph based

Graph-based indexing consists in building a directed graph whose nodes are the vectors to index. At search time, the graph is explored by following the edges towards the nodes that are closest to the query vector. In practice, the search is not greedy but maintains a priority queue with the most promising edges to explore. Thus, the trade-off at search time is given by the number of exploration steps: higher is more accurate but slower.

A graph-based algorithm is a general framework that can encompass many variants. In particular, tree-based search or IVF can be seen as special cases of graphs. One can see graphs as a way to precompute neighbors for the database vectors, then match the query to one of the vertices and follow the neighbors from there. However, they can also be built to handle out-of-distribution queries \[(https://arxiv.org/html/2401.08281v4#bib.bib42), (https://arxiv.org/html/2401.08281v4#bib.bib17)\].

Given this search algorithm, relying on a pure k-nearest neighbor graph is not optimal because neighbors are redundant. Therefore, the graph building heuristic consists in balancing edges to nearest neighbors and edges that reach more distant nodes. Most graph methods fix the number of outgoing edges per node, which adjusts the trade-off between search speed and memory usage. The memory usage per vector breaks down into the possibly compressed vector and the outgoing edges for that vector \[(https://arxiv.org/html/2401.08281v4#bib.bib29)\].

Faiss implements two graph-based algorithms: HNSW and NSG, respectively in the IndexHNSW and IndexNSG classes.

### HNSW

The hierarchical navigable small world graph \[(https://arxiv.org/html/2401.08281v4#bib.bib55)\] is a search structure where some randomly selected vertices are promoted to be hubs that are explored first. A notable advantage of HNSW is its ability to add vectors on-the-fly.

### NSG

The Navigating Spreading-out Graph \[(https://arxiv.org/html/2401.08281v4#bib.bib32)\] is built from a k-nearest neighbor graph that must be provided on input. At building time, some short-range edges are replaced with longer-range edges. The input k-nn graph can be built with a brute force algorithm or with a specialized method such as NN-descent \[(https://arxiv.org/html/2401.08281v4#bib.bib26)\] (NNDescent). Unlike HNSW, NSG does not rely on multi-layer graph structures, but uses long connections to achieve fast navigation. In addition, NSG starts from a fixed center point when searching.

Figure 7: Comparison of graph-based indexing methods HNSW (full lines) and NSG (dashes) to index Deep1M. We sweep the trade-offs between speed and accuracy by varying the number of graph traversal steps (indicated for some of the curves).

### Discussion

Figure (https://arxiv.org/html/2401.08281v4#S5.F7 "Figure 7 ‣ NSG. ‣ 5.2 Graph based ‣ 5 Non-exhaustive search ‣ The Faiss Library") compares the speed-accuracy trade-off for the NSG and HNSW indexes. Their main build-time hyperparameter is the number of edges per node, so we tested several settings (for HNSW this is the number of edges on the base level of the hierarchical graph). The main search-time parameter is the number of graph traversal steps during search (parameter efSearch for HNSW and search_L for NSG), which we vary to plot each curve. Increasing the number of edges improves the results until 64 edges, beyond which performance deteriorates. NSG obtains better trade-offs in general, at the cost of a longer build time. Building the k-NN graph with NN-descent for 1M vectors takes 37 s, and about the same time with exact, brute force search on a GPU. The NSG graph is frozen after the first batch of vectors is added, there is no easy way to add more vectors afterwards.

### How to choose an index

Figure 8: Comparison between the Faiss two other vector search libraries (SCANN and Diskann/vamana) when Deep10M in the ann-benchmarks setup (batch mode).

In most cases, choosing an appropriate index can be done by following a process delineated in Appendix [A.5](https://arxiv.org/html/2401.08281v4#A1.SS5 "A.5 How to choose an index ‣ Appendix A Appendix ‣ The Faiss Library"). First, one has to decide whether indexing is needed at all: indeed, in some cases a direct brute force search is the best option. Otherwise, the choice is between IVF and graph-based indexes.

### IVF vs. graph-based

Graph-based indices are a good option for indexes where there is no constraint on memory usage, typically for indexes below 1M vectors. Beyond 10M vectors, the construction time typically becomes the limiting factor. For larger indexes, where compression is required to even fit the database vectors in memory, IVF indexes are the only option.

The decision tree of Figure (https://arxiv.org/html/2401.08281v4#A1.F10 "Figure 10 ‣ A.5 How to choose an index ‣ Appendix A Appendix ‣ The Faiss Library") provides intial directions. The Faiss wiki^55^5[https://github.com/facebookresearch/faiss/wiki/Indexing-1G-vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1G-vectors) features comprehensive benchmarks for various database sizes and memory budgets. To refine the index parameters, benchmarking should be used.

### Benchmarking indexes

Faiss includes a benchmarking framework (bench_fw) that optimizes index types and parameters to explore accuracy, memory usage and search time operating points. The benchmark generates candidate index configurations to evaluate, sweeps both construction-time and search-time parameters, and measures these metrics.

### Decoupling encoding and non-exhaustive search options

Beyond a certain scale, search time is determined by the number of distance computations performed between the query vector and database vectors.

As shown in Sections (https://arxiv.org/html/2401.08281v4#S5 "5 Non-exhaustive search ‣ The Faiss Library") and (https://arxiv.org/html/2401.08281v4#S4 "4 Compression levels ‣ The Faiss Library"), Faiss indexes are built as a combination of pruning and compression, see Table (https://arxiv.org/html/2401.08281v4#A1.T4 "Table 4 ‣ A.7 API index of the Faiss library ‣ Appendix A Appendix ‣ The Faiss Library"). To evaluate index configurations efficiently, the benchmarking framework takes advantage of this compositional design. The training of vector transformations and k-means clustering for IVF coarse quantizers are factored out and reused when possible. Coarse quantizers and IVF indices are first trained and evaluated separately, the parameter space is pruned as described in the previous section, and only the combinations of Pareto-optimal components are benchmarked together.

### Comparison with other libraries

ANN-benchmarks \[(https://arxiv.org/html/2401.08281v4#bib.bib3)\] is a codebase that compares several ANNS implementations. We use this setup to compare Faiss with SCANN \[(https://arxiv.org/html/2401.08281v4#bib.bib36)\] and Vamana \[(https://arxiv.org/html/2401.08281v4#bib.bib79)\], two other industry-standard packages for vector search. We run the search in the following setting: batch search on the Deep10M dataset with 10-recall@10 as the metric, where the training is performed on the database vectors. This differs slightly from the evaluation protocol used originally for this dataset.

Figure (https://arxiv.org/html/2401.08281v4#S5.F8 "Figure 8 ‣ 5.3 How to choose an index ‣ 5 Non-exhaustive search ‣ The Faiss Library") shows that Faiss is faster than SCANN and about on-par with Vamana, depending on the operating point. For Faiss we used IVF with a Product Residual Quantizer optimized for SIMD (see Appendix [A.3](https://arxiv.org/html/2401.08281v4#A1.SS3.SSS0.Px2 "CPU vectorization. ‣ A.3 Optimization ‣ Appendix A Appendix ‣ The Faiss Library")), followed by re-ranking (Section [3.5](https://arxiv.org/html/2401.08281v4#S3.SS5 "3.5 Refining (IndexRefine) ‣ 3 Performance axes of a vector search library ‣ The Faiss Library")).

## Database operations

In the experiments above, the indexes are built in one go with all the vectors, while search operations are performed with one batch containing all query vectors. In real settings, the index evolves over time, vectors may be dynamically added or removed, searches may have to take into account metadata, etc. In this section we show how Faiss supports some of these operations. Specific APIs are available to interface with external storage (Appendix [A.4](https://arxiv.org/html/2401.08281v4#A1.SS4 "A.4 Interfacing with external storage ‣ Appendix A Appendix ‣ The Faiss Library")) if fine-grained control is required.

### Identifier-based operations

Faiss indexes support two types of identifiers: sequential and arbitrary ids. Sequential ids are based on the order of additions in the index. Alternatively, the user can provide arbitrary 63-bit integer ids associated to each vector (the sign bit is reserved for invalid results). The corresponding addition methods for the index are add and add_with_ids. Unlike e.g. Usearch \[(https://arxiv.org/html/2401.08281v4#bib.bib87)\], Faiss does not store arbitrary metadata with the vectors.

### Index updates

The Faiss API includes methods to remove vectors (remove_ids) and update them (update_vectors) by passing the corresponding ids.

Note that if the vector *distribution* changes significantly because of additions/removals or updates, then the efficiency of any technique that fits the data distribution degrades. This includes IVF and PQ compression. This degradation can be addressed by explicit updates of the index structure \[(https://arxiv.org/html/2401.08281v4#bib.bib8)\].

### Flat indexes

Sequential indexes (IndexFlatCodes) store vectors as an array. They support only sequential ids. When arbitrary ids are needed, the index can be embedded in a IndexIDMap, that translates sequence numbers to arbitrary ids using a `int64` array. This enables add_with_ids and returns the arbitrary ids at search time. IndexIDMap2 in addition maps arbitrary ids back to sequential ids using a hash table. The graph indexes rely on an embedded IndexFlatCodes to store the actual vectors. To use them with non-sequential ids, they should be wrapped with the same mapping objects.

### IVF indexes

The IVF indexing structure supports user-provided ids natively at addition and search time. However, id-based access may require a sequential scan, as the entries are stored in an arbitrary order in the inverted lists. Therefore, the IVF index can optionally maintain a DirectMap, which maps user-visible ids to the inverted list and the offset they are stored in. It supports lookup, removal and update by ids. The map can be an array, which is appropriate for sequential ids, or a hash table, for arbitrary 63-bit ids. The direct map incurs a memory overhead and an add-time computation overhead, therefore, it is disabled by default.

### Graph indexes

The graph index HNSW does not support suppression and mutation, and NSG does not even support adding vectors incrementally. Supporting this requires heuristics to rebuild the graph when it is mutated, which are implemented in HNSWlib and FreshDiskANN \[(https://arxiv.org/html/2401.08281v4#bib.bib78)\] but suboptimal indexing-wise.

### Filtered search

Vector filtering consists in returning only database vectors based on some search-time criterion, other vectors are ignored. Faiss has basic support for vector filtering: the user can provide a predicate (IDSelector callback), and if the predicate returns false on the vector id, the vector is ignored.

Therefore, if metadata is needed to filter the vectors, the callback function needs to do an indirection to the metadata table, which is inefficient. Another approach is to exploit the unused bits of the identifier. If $N$ documents are indexed with sequential ids, $63 - {\lceil{\log_{2}{(N)}}\rceil}$ bits are unused.

This is sufficient to store enumerated types (e.g. country codes, music genres, license types, etc.), dates (as days since some origin), version numbers, etc. However, it is insufficient for more complex metadata. In the example use case below, we use the available bits to implement more complex filtering.

### Filtering with bag-of-word vectors

In the filtered search track of the BigANN 2023 competition \[(https://arxiv.org/html/2401.08281v4#bib.bib75)\], each query and database vector is associated with a few terms from a fixed vocabulary of size $v$ (for the queries there are only 1 or 2 words). The filtering consists in considering only the database vectors that include all the query terms.. This metadata is given as a sparse matrix $M_{meta} \in {\{ 0,1\}}^{N \times v}$.

The basic implementation of the filter starts from query vector $q$ and the associated words ${w_{1},w_{2}} \in {\{{1\ldotsv}\}}$. Before computing a distance to a vector with id $i$, it fetches row $i$ of $M_{meta}$ to verify that $w_{1}$ and $w_{2}$ are in it. This predicate is slow because it requires to access $M_{meta}$, which causes cache misses and it performs an iterative binary search in the sparse matrix structure. Since the callback is called in the tightest inner loop of the search function, and since the IVF search tends to perform many vector comparisons, this has non negligible performance impact.

To speed up the predicate, we can use bit manipulations. In this example, $N = 10^{7}$, so we use only ${\lceil{\log_{2}N}\rceil} = 24$ bits of the ids, leaving ${63 - 24} = 39$ bits that are always 0. We associate to each word $j$ a 39-bit signature $S{\lbrack j\rbrack}$, and to each set of words the binary "or" of these signatures. The query is represented by $s_{q} = {{S{\lbrack w_{1}\rbrack}} \vee {S{\lbrack w_{2}\rbrack}}}$. Database entry $i$ with words $W_{i}$ is represented by $s_{i} = {\vee_{w \in W_{i}}{S{\lbrack w\rbrack}}}$. Then the following implication holds: if ${\{ w_{1},w_{2}\}} \subset W_{i}$ then all 1 bits of $s_{q}$ are also set to 1 in $s_{i}$:

This binary test costs only a few machine instructions on data that is already in machine registers. It can thus be used as a pre-filter before applying the predicate computation. This is implemented in the module bow_id_selector^66^6[https://github.com/harsha-simhadri/big-ann-benchmarks/tree/main/neurips23/filter/faiss](https://github.com/harsha-simhadri/big-ann-benchmarks/tree/main/neurips23/filter/faiss).

The remaining degree of freedom is how to choose the binary signatures, because this rule's filtering ability depends on the choice of the signatures $S$. We experimented with i.i.d. Bernoulli bits with varying $p$: the best setting avoids running the full predicate more than 4/5 times.

### Vector-first or metadata-first search

There are two possible approaches to filtered search: *vector-first*, which is described above, and *metadata-first*, where only vectors with appropriate metadata are considered in vector search. The metadata-first filtering generates a subset of vectors to compare with that can then be compared using brute force search. Brute force search is slow but acceptable if the subset size is small, and the results are exact.

Therefore, in the context of the BigANN competition \[(https://arxiv.org/html/2401.08281v4#bib.bib75)\], the decision to use vector-first or metadata-first depends on how large the subset is. To this end, we map each word $w$ to the list of items that contain $w$, of size $L_{w}$.

If there is a single query word $\{ w_{1}\}$ then the subset size is directly accessible as $S = L_{w_{1}}$. With two query words $\{ w_{1},w_{2}\}$, finding the subset size requires intersecting the inverted lists for $w_{1}$ and $w_{2}$, which is slow. Instead, one can estimate the size of the subset using the empirical probability of each word to appear ${P{(w)}} = {L_{w}/N}$. Assuming independent draws, the probability of both words to appear is $P{(w_{1})}P{(w_{2})}$. Therefore, the expected size of the intersection is $S \approx {NP{(w_{1})}P{(w_{2})}} = {{L_{w_{1}}L_{w_{2}}}/N}$. If ${S/N} < {3 \times 10^{- 4}}$ (an empirical threshold), then the subset is sufficiently small that metadata-first can be applied. Of course, if metadata-first is selected, the actual intersection has to be computed. Most participants to the competition used similar heuristics.

## Faiss applications

Faiss is widely used across the industry, with numerous applications leveraging its capabilities. The following examples highlight notable use cases that demonstrate exceptional scalability or significant impact.

### Trillion scale index

In this example, we index 1.5 trillion vectors in 144 dimensions. The indexing needs to be accurate, therefore the compression of the vectors is limited to 54 bytes with a PCA to 72 dimensions and 6-bit scalar quantizer (`,SQ6`).

A HNSW coarse quantizer with 10M centroids is used for the IndexIVFScalarQuantizer, trained with a simple distributed GPU k-means (implemented in faiss.clustering).

Once the training is completed, the index is built in the following three phases:

shard over ids: add the input vectors in 2000 shards independently, producing 2000 indexes (each one fits in 256 GB RAM);

shard over lists: build the 100 indexes corresponding each to a subset of 100k inverted lists. This is done on 100 different machines, each reading from the 2000 sharded indices, and writing the results directly to a distributed file system;

load the shards: memory-map all 100 indexes on a central machine as 100 OnDiskInvertedLists (a memory map of 83 TiB).

Steps 1 and 2 are organized to be performed as independent cluster jobs on a few hundred servers (64 cores, 256G RAM). Otherwise, the code is written in standard Faiss in Python.

The central machine that handles searches performs the coarse quantization and loads the inverted lists from the distributed disk partition. The limiting factor is the network bandwidth of this central machine. Therefore, it is more efficient to distribute the search on 20 intermediate servers to spread the load. This brings the search time down to roughly 1 s per query.

### Text retrieval

Faiss is commonly used for knowledge intensive natural language processing tasks. In particular, ANNS is relevant for information retrieval \[(https://arxiv.org/html/2401.08281v4#bib.bib85), (https://arxiv.org/html/2401.08281v4#bib.bib67)\], with applications such as fact checking, entity linking, slot filling or open-domain question answering: these often rely on retrieving relevant content across a large-scale corpus. To that end, embedding models have been optimized for text retrieval \[(https://arxiv.org/html/2401.08281v4#bib.bib40), (https://arxiv.org/html/2401.08281v4#bib.bib49)\].

Finally, \[(https://arxiv.org/html/2401.08281v4#bib.bib41)\], \[(https://arxiv.org/html/2401.08281v4#bib.bib50)\], \[(https://arxiv.org/html/2401.08281v4#bib.bib74)\] and \[(https://arxiv.org/html/2401.08281v4#bib.bib48)\] consist of language models that have been trained to integrate textual retrieval in order to improve their accuracy, factuality or compute efficiency.

### Data mining

Another recurrent application of ANNS and Faiss is in the mining and curation of large datasets. In particular, Faiss has been used to mine bilingual texts across very large text datasets retrieved from the web \[(https://arxiv.org/html/2401.08281v4#bib.bib72), (https://arxiv.org/html/2401.08281v4#bib.bib9)\], or to organize a language model's training corpus in order to group together series of documents covering similar topics \[(https://arxiv.org/html/2401.08281v4#bib.bib73)\].

In the image domain, \[(https://arxiv.org/html/2401.08281v4#bib.bib64)\] leverages Faiss to remove duplicates from a dataset containing 1.3B images. It then relies on efficient indexing in order to mine a curated dataset whose distribution matches the distribution of a target dataset.

### Content Moderation

One of the major applications of Faiss is the detection and remediation of harmful content at scale. Human-labeled examples of policies violating images and videos are embedded with models such as SSCD \[(https://arxiv.org/html/2401.08281v4#bib.bib69)\] and stored in a Faiss index. To decide if a new image or video would violate some policies, a multi-stage classification pipeline first embeds the content and searches the Faiss index for similar labeled examples, typically utilizing range queries. The results are aggregated and processed through additional machine classification or human verification. Since the impact of mistakes is high, good representations should discriminate perceptually similar and different content, and accurate similarity search is required even at billion to trillion scale. The former problem motivated the Image and Video Similarity Challenges \[(https://arxiv.org/html/2401.08281v4#bib.bib30), (https://arxiv.org/html/2401.08281v4#bib.bib68)\].

## Conclusion

Throughout the years, Faiss continuously expanded its focus to include the most relevant vector indexing techniques from research. We continue doing this to include novel quantization techniques \[(https://arxiv.org/html/2401.08281v4#bib.bib39)\], better hardware support for some indexes \[(https://arxiv.org/html/2401.08281v4#bib.bib63)\] and new indexing forms, such as associative vector memories for transformer architectures \[(https://arxiv.org/html/2401.08281v4#bib.bib20), (https://arxiv.org/html/2401.08281v4#bib.bib94)\].
