<!-- arxiv-full-text:v1 {"arxiv_id": "1609.07228", "source": "ar5iv"} -->

## Introduction

Nearest neighbor search plays an important role in many applications of data mining, machine learning and computer vision. When dealing with sparse data (*e.g*., document retrieval), one can use advanced index structures (*e.g*., inverted index) to solve this problem. However, for data with dense features, the cost for finding the exact nearest neighbor is $O{(N)}$, where $N$ is the number of points in the database. It's very time consuming when the data set is large. So people turn to Approximate Nearest neighbor (ANN) search in practice. Many work has been done to carry out the ANN search with high accuracy but low computational complexity.

There are mainly two types of methods in ANN search. The first type methods are hierarchical structure (tree) based methods, such as KD-tree,Randomized KD-tree, K-means tree. These methods perform very well when the dimension of the data is relatively low. However, the performance decreases dramatically as the dimension of the data increases. The second type methods are hashing based methods, such as Locality Sensitive Hashing (LSH), Spectral Hashing, Iterative Quantization and so . Please see for a detailed survey on various hashing methods. These methods generate binary codes for high dimensional real vectors while try to preserve the similarity among original real vectors. Thus, all the real vectors fall into different hashing buckets (with different binary codes). Ideally, if neighbor vectors fall into the same bucket or the nearby buckets (measured by the hamming distance of two binary codes), the hashing based methods can efficiently retrieve the nearest neighbors of a query point. However, there is no guarantee that all the neighbor vectors will fall into the nearby buckets. To ensure the high *recall* (the number of true neighbors within the returned points set divides by the number of required neighbors), one needs to examine many hashing buckets (*i.e*., enlarge the search radius in hamming space), which results a high computational complexity. Please see for a detailed analysis.

Recently, graph based methods have drawn considerable attention. The essential idea behind these approaches is that *a neighbor of a neighbor is also likely to be a neighbor*, which we refer as *NN-expansion*. These methods construct a $k$-nearest neighbor ($k$NN) graph offline. And at online search stage, these methods find the candidate neighbors of a query point in some way (*e.g*., random selection ), and then check the neighbors of these candidate neighbors for closer ones iteratively. One problem of this approach is that the NN-expansion is easily to converge to local optima and result in a low recall. tries to solve this problem by providing better initialization for a query point. Instead of random selection, uses hashing based methods for initialization. This approach is named as Iterative Expanding Hashing (IEH) and achieves significant better results than the corresponding hashing based methods.

Another challenge on using graph based methods is the high computational cost in building the $k$NN graph, especially when the database is large. There are many efforts that have been put into reducing the time complexity of $k$NN graph construction. try to speed up an exact $k$NN graph construction. However, these approaches are still not efficient enough in the context of big data. Instead of building an exact $k$NN graph, recent researchers try to build an approximated $k$NN graph efficiently. The *NN-expansion* idea again can be used to build an approximated $k$NN graph. proposed NN-descent to efficiently build an approximate $k$NN graph. try to build an approximate $k$NN graph in a divide-and-conquer manner. Their algorithms mainly contain three phrases. Firstly, they divide the whole data set into small subsets multiple times. Secondly, they do brute force search within the subsets and get lots of overlapping subgraphs. Finally, they merge the subgraphs and refine the graph with techniques similar to NN-expansion. Although an approximated $k$NN graph can be efficiently constructed, there are no formal study on how the performance of graph based search methods will be affected if one uses an approximated $k$NN graph instead of an exact $k$NN graph.

To tackle above problems, we propose a novel graph-based approximate nearest neighbor search framework EFANNA in this paper. EFANNA is an abbreviation for two algorithms: Extremely Fast Approximate $k$-Nearest Neighbor graph construction Algorithm and Extremely Fast Approximate Nearest Neighbor search Algorithm based on $k$NN graph. Our algorithm is based on a simple observation: the performance of both NN-expansion and NN-descent is very sensitive with the initialization.

Our EFANNA index contains two parts: the multiple randomized hierarchical structures (*e.g*., randomized truncated KD-tree) and an approximate $k$-nearest neighbor graph.

At offline stage, EFANNA divides the data set multiple times into a number of subsets in a fast and hierarchical way, producing multiple randomized hierarchical structures. Then EFANNA constructs an approximate $k$NN graph by conquering bottom-up along the structures. When conquering, EFANNA takes advantage of the structures to locate the closest possible neighbors, and use these candidates to update the graph, which reduces the computation cost than using all the points in the subtree. Finally we refine the graph similar to NN-descent, which is based on the NN-expansion idea and optimized with techniques like local join, sampling, and early termination.

At online search stage, EFANNA first search in the hierarchical structures to get candidate neighbors for a given query. Then EFANNA refines the results using NN-expansion on the approximate $k$NN graph. Extensive experimental results show that our approach outperforms the the-state-of-the-art approximate nearest neighbor search algorithms significantly.

It is worthwhile to highlight the contributions of our paper as follows: EFANNA outperforms state-of-the-art ANN search algorithms significantly. Particularly, EFANNA outperforms Flann, one of the most popular ANN search library, in index size, search speed and search accuracy.

EFANNA can build an approximate $k$NN graph with hundreds times speed-up over brute-force graph building on million scale datasets. Considering many unsupervised and semi-supervised machine learning algorithms are based on a nearest neighbor graph. EFANNA provides the possibility to examine the effectiveness of all these algorithms on large scale datasets.

We show by experimental results that with an approximate $k$NN graph of low accuracy constructed by EFANNA, graph-based ANN search methods (*e.g*., EFANNA) still perform very good. This is because the "error" neighbors of approximate $k$NN graph constructed by EFANNA are actually neighbors a little farther. This property is never explored in the previous work.

The remainder of this paper is organized as follows. In Section 2 we will introduce some related work. Our EFANNA algorithm is presented in section 3. In section 4, we will report the experimental results and show the performance of EFANNA comprehensively. In section 5 we will talk about our open library and in section 6 we will draw a conclusion.

## Related work

Nearest neighbor search has been a hot topic during the last decades. Due to the intrinsic difficulty of exact nearest neighbor search, the approximate nearest neighbor (ANN) search algorithms are widely studied and the researchers expect to sacrifice a little searching accuracy to lower the time cost as much as possible.

Hierarchical index based (tree based) algorithms, such as KD-tree, have gained early success on approximate nearest neighbor search problems. However, it's proved to be inefficient when the dimensionality of data grows high. Many new hierarchical structure based methods are presented to address this limitation. Randomized KD-tree and Kmeans tree are absorbed into a well-known open source library FLANN, which has gained wide popularity.

Hashing based algorithms aim at finding proper ways to generate binary codes for data points and preserve their similarity in original feature space. These methods can be treated as dividing the data space with multiple hyperplanes and representing each resulting polyhedron with a binary code. Learning the hashing functions with different constraints will result in different partition of data space. One of the most famous algorithms is Locality Sensitive Hashing (LSH), which is essentially based on random projection. Many other variants are proposed based on different constraints. And the constraints reflect what they think is the proper way to partition the data space.

Both the hashing based methods and tree based methods have the same goal. They expect to put neighbors into the same hashing bucket (or node). However, there is no theoretical guarantee of this expectation. To increase the search *recall* (the number of true neighbors within the returned points divides by the number of required neighbors), one needs to check the "nearby" buckets or nodes. With high dimensional data, one polyhedron may have a large amount of neighbor polyhedrons, (for example, a bucket with 32 bit hashing code has 32 neighbor buckets with 1 hamming radius distance), which makes locating true neighbors hard.

Recently graph based techniques have drawn considerable attention. The main idea of these methods is *a neighbor of a neighbor is also likely to be a neighbor*, which we refer as *NN-expansion*. At offline stage, they need to build a $k$NN graph, which can be regraded as a big table recording the top $k$ closest neighbors of each point in database. At online stage, given a query point, they first assign the query some points as initial candidate neighbors, and then check the neighbors of the neighbors iteratively to locate closer neighbors. Graph Nearest neighbor Search (GNNS) randomly generate the initial candidate neighbors while Iterative Expanding Hashing (IEH) uses hashing algorithms to generate the initial candidate neighbors.

Since all the graph based methods need a $k$NN graph as the index structure, how to build a $k$NN graph efficiently became a crucial problem, especially when the database is large. Many work has been done on building either exact or approximate $k$NN graph. try to build an exact $k$NN graph quickly. However, these approaches are still not efficient enough in the context of big data. Recently, researchers try to build an approximated $k$NN graph efficiently. Again, the NN-expansion idea can be used here. proposed an *NN-descent* algorithm to efficiently build an approximate $k$NN graph. The basic idea of NN-descent is similar to NN-expansion but the details are different. NN-descent uses many techniques (*e.g*., Local join and Sampling) to efficiently refine the graph. Please see for details.

Instead of initializing the $k$NN graph randomly, uses some divide-and-conquer methods. Their initialization contains two parts. Firstly, they divide the whole data set into small subsets multiple times. Secondly, they do brute force search within the subsets and get lots of overlapping subgraphs. These subgraphs can be merged together to serve as the initialization of $k$NN graph. The NN-expansion like techniques can then be used to refine the graph. The division step of is based on a spectral bisection and they proposed two different versions, overlap and glue division. use Anchor Graph Hashing to produce the division. uses recursive random division, dividing orthogonal to the principle direction of randomly sampled data in subsets. uses random projection trees to partition the datasets.

1:data set D, query vector q, the number K of required nearest neighbors, EFANNA index (including tree set St r e e and kNN graph G), the candidate pool size P, the expansion factor E, the iteration number I. 2:approximate nearest neighbor set A N N S of the query 6:suppose the maximal number of points of leaf node is Sl e a f 7:suppose the number of trees is Nt r e e 8:then the maximal node check number is Nn o d e = P ÷ Sl e a f ÷ Nt r e e + 1 9:for all tree i in St r e e do 10: Depth-first search i for top Nn o d e closest leaf nodes according to respective tree search criteria, add to N o d e L i s t 12:add the points belonging to the nodes in N o d e L i s t to C 13:keep E points in C which are closest to q. 16: for all point n in C do 17: Sn is the neighbors of point n based on G. 18: for all point n n in Sn do 19: if n n hasn’t been checked then 24: move all the points in C C to C and keep P points in C which are closest to q. 27:return A N N S as the closet K points to q in C. Algorithm 1 EFANNA Search Algorithm and claim to outperform NN-descent significantly. However, based on their reported results and our analysis, there seems a misunderstanding of NN-descent. Actually, NN-descent is quite different than NN-expansion. The method compared in and should be NN-expansion instead of NN-descent. Please see Section 3.3.3 for details.

## EFANNA Algorithms for ANN search

We will introduce our EFANNA algorithms in this section. EFANNA algorithms include offline index building part and online ANN search algorithm. The EFANNA index contains two parts: multiple hierarchical structures (*e.g*., randomized truncated KD-tree) and an approximate $k$NN graph. We will first show how to use EFANNA index to carry out online ANN search. Then we will show how to build the EFANNA index in a divide-conquer-refinement manner.

1:the data set D, the number of trees T, the number of points in a leaf node K. 2:the randomized truncated KD-tree set S 5: if size of PointSet < K then 8: Randomly choose dimension d. 9: Calculate the mean m i d over P o i n t S e t on dimension d. 10: Divide P o i n t S e t evenly into two subsets, L e f t H a l f and R i g h t H a l f, according to m i d. Algorithm 2 EFANNA Tree Building Algorithm

### ANN search with EFANNA index

EFANNA is a graph based method. The main idea is providing better initialization for NN-expansion to improve the performance significantly. The multiple hierarchical structures is used for initialization and the approximate $k$NN graph is used for NN-expansion.

There are many possible hierarchical structures (*e.g*. hierarchical clustering or randomized division tree ) can be used in our index structure. In this paper, we only report the results using randomized *truncated* KD-tree. The details on the difference between this structure and the traditional randomized KD-tree will be discussed in the next subsection. Based on this randomized truncated KD-tree, we can get the initial neighbor candidates given a query $q$. We then refine the result with NN-expansion, *i.e*., we check the neighbors of $q$'s neighbors according to the approximate $k$NN graph to get closer neighbors. Algorithm 1 shows the detailed procedure.

There are three essential parameters in our ANN search algorithm: the expansion factor $E$, the the candidate pool size $P$ and the iteration number $I$. In our experiment, we found $I = 4$ is enough and thus we fixed $I = 4$. The trade-off between search speed and accuracy can be made through tuning parameters $E$ and $P$. In other words, larger $E$ and larger $P$ sacrifice the search speed for high accuracy.

1:the data set D, the k in approximate kNN graph, the randomized truncated KD-tree set S built with Algorithm 2, the conquer-to depth D e p. 2:approximate kNN graph G. 4:Using Algorithm 2 to build tree, which leads to the input S 8:for all point i in D do 10: for all binary tree t in S do 11: search in tree t with point i to the leaf node. 12: add all the point in the leaf node to C. 16: Depth-first-search in the tree t with point i to depth d. Suppose N is the non-leaf node on the search path with depth d. Suppose S i b is the child node of N. And S i b is not on the search path of point i. 17: Depth-first-search to the leaf node in the subtree of S i b with point i. Add all the points in the leaf node to C. 20: Reserve K closest points to i in C. Algorithm 3 Hierarchical Divide-and-Conquer Algorithm (kNN Graph Initialization)

### EFANNA Index Building Algorithms I: Tree Buidling

One part of the EFANNA index is a multiple hierarchical structures. There are many possible hierarchical structures (*e.g*. hierarchical clustering or randomized division tree ) can be used. In this paper, we only report the results using randomized *truncated* KD-tree. Please see Algorithm 2 for details on building randomized truncated KD-trees.

The only difference between randomized *truncated* KD-tree and the traditional randomized KD-tree is that leaf node in our trees has $K$ ($K = 10$ in our experiments) points instead of 1. This change makes the tree building in EFANNA much faster than the the traditional randomized KD-tree. Please see Table IV in the experiments for details.

The randomized truncated KD-tree built in this step is used not only in the on-line search stage, but also in the approximate $k$NN graph construction stage. See the next section for details.

### EFANNA Index Building Algorithms II: Approximate $k$NN Graph Construction

Another part of the EFANNA index is an approximate $k$NN graph. We use the similar methodology to efficiently build the approximate $k$NN graph as with ANN search. It contains two stage. At first stage, we regard the trees built in the previous part as multiple overlapping divisions over the data set, and we perform the conquering step along the tree structures to get an initial $k$NN graph. At second stage, we use NN-descent to refine the $k$NN graph.

Figure 1: An example for our hierarchical divide-and-conquer algorithm.

### Hierarchical Randomized Divide-and-Conquer

uses a random $k$NN graph as the initialization and refined it with the NN-descent algorithm to get a $k$NN graph with high accuracy. Our idea is very simple. We try to provide a better initialization for NN-descent. A good initialization should produce an initial $k$NN graph with certain accuracy within short time.

Divide-and-conquer is a good strategy to achieve this goal. A normal divide-and-conquer process first breaks the problem into subproblems recursively until the subproblem is small and easy enough to solve. Then the solutions of subproblems are combined to get a solution to the original problem. For approximate graph construction, the division part is easy. We can divide the data set as the way the tree was constructed (Section 3.2). Then we merge sibling nodes recursively upwards from leaf. With only one tree, we need to conquer to root to get a full connected graph. But if we directly conquer from leaf to root, the computational cost grows exponentially upwards and is no less than brute-force graph construction.

To reduce the computational complexity, we need to find a better conquer strategy and avoid conquering to root. We follow the inspiration of previous work, which said multiple randomized division can produce overlapping subsets. As a result, the conquer doesn't need to be carried out to root. In addition, our motivation on better conquer strategy is to reduce the number of points involved in conquering at each level and keep points' "quality" (we make sure that we always choose the closest possible points for conquer). For example, in Fig 1, if we know that point $q$ in node (or subset) $8$ is closer to the area of node $10$, then we just need to consider the points in node $10$ when conquering $4$ and $5$ at level $1$ with $q$.

In other words, when we conquer two sibling non-leaf nodes (sibling leaf nodes can be conquered directly), for some points in one subtree, we may just consider the "closest" possible leaf node in the sibling subtree. Because the rest leaf nodes are farther, the points in them are also likely to be farther, thus excluded from distance calculating. We can regard the tree as a multi-class classifier, each leaf node can be treated as a class. This classifier may divide the data space like the rectangle in Fig. 1 does and different colors represent different labels. Sometimes nearest neighbors (*e.g*. white points in area $8$ and area $10$) are close to each other, but fit in different area according to this classifier with a discriminative plane (*e.g*. node $2$) separating them. In Fig.1, suppose point $q$ will be assigned label $8$ when $q$ is input into the tree classifier. When conquering at level $1$, we need to know in subtree $5$ which area between node $10$ and $11$ is closer to $q$. Now that the whole tree can be treated as a multi-class classifier, any subtree of it can be a multi-class classifier, too. To know which area is closer, we simply let the classifier of subtree $5$ make the choice. By inputing $q$ to the classifier, we will obtain a label between 10 and 11 for q. Since $q$ is the white point in area $8$, from the rectangle in Fig. 1, it's obvious that $q$ will be labeled as $10$. Therefore for $q$, when conquering at level $1$, only points in node $10$ will be involved.

1:an initial approximate k-nearest neighbor graph Gi n i t, data set D, maximum iteration number I, Candidate pool size P, new neighbor checking num L. 2:an approximate kNN graph G. 4:Graph Gn e w records all the new added candidate neighbors of each point. Gn e w = Gi n i t. 5:Graph Go l d records all the old candidate neighbors of each point at previous iterations. Go l d = ⌀ 6:Graph Gr n e w records all the new added reverse candidate neighbors of each point. 7:Graph Gr o l d records all the old reverse candidate neighbors of each point. 10: for all point i in D do 11: N Nn e w is the neighbor set of point i in Gn e w. 12: N No l d is the neighbor set of of point i in Go l d. 13: for all point j in N Nn e w do 14: for all point k in N Nn e w do 16: calculate the distance between j and k. 17: add k to j’s entry in G. mark k as n e w. 18: add j to k’s entry in G and Gr n e w. 22: for all point l in N No l d do 23: calculate the distance between j and l. 24: add l to j’s entry in G. mark l as o l d. 25: add j to l’s entry in G and Gr o l d. 30: for all point i in D do 31: Reserve the closest P points to i in respective 35: for all point i in D do 36: l = 0. N N is the neighbor set of i in G. Algorithm 4 Approximate kNN Graph Refinement Algorithm In this way, for each point at each level, only the points in one closest leaf node will be considered, which reduces the computation complexity greatly and reserves accuracy. We perform our random divide-and-conquer process multiple times and get an initial graph.

Again there is a trade-off between accuracy of initial graph and time cost in parameter tuning. When conquer-to depth $Dep$ is small (*i.e*. conquering to a level close to root), or when tree number $T_{c}$ is larger, the accuracy is higher but time cost is higher. In our experiments, we use the randomized KD-tree as the hierarchical divide-and-conquer structure. See Algorithm 3 for details on randomized KD-tree divide-and-conquer algorithm).

### Graph Refinement

We use the NN-descent proposed by to refine the resulting graph we get from the divide-and-conquer step. The main idea is also to find better neighbors iteratively, however, different from NN-expansion, they proposed several techniques to get much better performance. We rewrite their algorithms to make it easy to understand. See Algorithm 4 for details.

The pool size $P$ and neighbor checking num $L$ are essential parameters of this algorithm. Usually, Larger $L$ and $P$ will result in better accuracy but higher computation cost.

### NN-expansion VS. NN-descent

Some approximate $k$NN graph construction methods claim to outperform NN-descent significantly. However, based on their reported results and our analysis, there seems a misunderstanding of NN-descent. Actually, NN-descent is quite different than NN-expansion. For given point $p$, NN-expansion assume the neighbors of $p$'s neighbors are likely to be neighbors of $p$. While NN-descent thinks that $p$'s neighbors are more likely to be neighbors of each other. Our experimental results have shown that NN-descent is much more efficient than NN-expansion in building approximate $k$NN graph. However, the NN-descent idea cannot be applied to ANN search.

### Online index updating

EFANNA index building algorithm is easily to be extended to accept stream data. Firstly, when a new point arrived, we can insert it into the tree easily. And when the number of points in the inserted node exceeds given threshold, we just need to split the node. When the tree is unbalanced to some degree, we should adjust the tree structure, which is quite fast on large scale data. Secondly, the graph building algorithm can accept stream data as well, we can use the same algorithm we describe before. First we search in the tree for candidates, and use NN-descent to update the graph with the involved points. And this step is quite fast, too.

## Experiments

To demonstrate the effectiveness of the proposed method EFANNA, extensive experiments on large-scale data sets are reported in this section.

### Data Set and Experiment Setting

The experiments were conducted on two popular real world data sets, SIFT1M and GIST1M^11^1Both two datasets can be downloaded at The detailed information on the data sets is listed in TABLE I. All the codes we used are written in C++ and compiled by g++4.9, and the only optimization option we allow is "O3" of g++. Parallelism and other optimization like SSE instruction are disabled. The experiment on SIFT1M is carried out on a machine with i7-3770K CPU and 16G memory, and GIST1M is on a machine with i7-4790K CPU and 32G memory.

TABLE I: information on experiment data sets

### Experiments on ANN Search

### Evaluation Protocol

To measure the performance of ANN search of different algorithms, we used the well known $average$ $recall$ as the accuracy measurement. Given a query point, all the algorithms are expected to return $k$ points. Then we need to examine how many points in this returned set are among the true $k$ nearest neighbors of the query. Suppose the returned set of $k$ points given a query is $R'$ and the true $k$ nearest neighbors set of the query is $R$, the $recall$ is defined as Then the $average$ $recall$ is averaging over all the queries. Since the sizes of $R'$ and $R$ are the same, the recall of $R'$ is the same as the accuracy of $R'$.

We compare the performance of different algorithms by requiring different number of nearest neighbors of each query point, including 1-NN and 100-NN. In other words, the size of $R$ (and $R'$) will be 1 and 100 respectively. Please see our technical report for more results on 10-NN and 50-NN.

Figure 2: ANN search results of 10,000 queries on SIFT1M. We use a 10-NN ground truth graph for all graph based methods.

Figure 3: ANN search results of 1,000 queries on GIST1M. We use a 10-NN ground truth graph for all graph based methods.

### Comparison Algorithms

To demonstrate the effectiveness of the proposed EFANNA approach, the following four state-of-the-art ANN search methods and brute-force method are compared in the experiment. brute-force. We report the performance of brute-force search to show the advantages of using ANN search methods. To get different recall, we simply perform brute-force search on different percentage of the query number. For example, the brute-force search time on 90% queries of the origin query set stands for the brute-force search time of 90% average recall. flann. FLANN is a well-known open source library for ANN search. The Randomized KD-tree algorithm in FLANN provides state-of-the-art performance. In our experiments, we use 16 trees for both datasets. And we tune the "max-check" parameter to get the time-recall curve.

GNNS. GNNS is the first ANN search method using $k$NN graph. Given a query, GNNS generates the initial candidates (neighbors) by random selection. Then GNNS uses the NN-expansion idea (*i.e*., check the neighbors of the neighbors iteratively to locate closer neighbors) to refine the result. The main parameters of GNNS are the size of the initial result and the iteration number. We fix the iteration number as 10 and tune the initial candidate number to get the time-recall curve. kGraph. kGraph is an open library for ANN search based on $k$NN graph. The author of kGraph is the inventor of NN-descent. The ANN search algorithm in kGraph is essentially the same as GNNS. The original Kgraph library implements with OpenMP (for parallelism) and SSE instructions for speed-up. We simply turn off the parallelism and SSE for fair comparison.

IEH. IEH is a short name for Iterative Expanding Hashing. It is another ANN search method using $k$NN graph. Different from GNNS, IEH uses hashing methods to generate the initial result given a query. Considering the efficiency of hash coding, IEH-LSH and IEH-ITQ are compared in our experiment. The former uses LSH as the hashing method and the latter uses ITQ as the hashing method. Both hashing methods use 32 bit code. We also fix the iteration number as 10 and tune the initial result size to get the time-recall curve.

Efanna. The algorithm proposed in this paper. We use 16 trees for both datasets and the iteration number in NN-expansion stage is fixed as 4. We tune the search-to depth parameter $S_{depth}$ and the candidate pool size $P$ to get the time-recall curve. tree (hash table) The index size here is the size in the memory, not the size on the disk.

TABLE II: Index Size of Different Algorithms Among the five compared ANN methods, Flann's KD-tree is the hierarchical structure (tree) based method. The other four compared methods are all graph based methods. We do not compare with hashing based methods because shows the significant improvement of IEH over the corresponding hashing methods.

All the graph based methods need a pre-built $k$NN graph and we use a ground truth 10-NN graph.

### Results

The time-recall curves of all the algorithms on two data sets can be seen in Fig. 2 and Fig. 3. The index size of various algorithms are shown in Table II. A number of interesting conclusions can be drawn as follows: Our Efanna algorithm significantly outperforms all the other methods at all the cases on both of two data sets. Even at a relatively high recall (*e.g*., 95%), Efanna is about 100x faster than the brute-force search on the SIFT1M and about 10x faster than the brute-force search on the GIST1M.

The GIST1M is a harder dataset than the SIFT1M for ANN search. At a relatively high recall (*e.g*., 95%), all the ANN search methods are significantly faster than the brute-force search. However, on GIST1M some methods (flann, GNNS, kGrpah) are similar (or even slower) to the brute-force search. The reason may be the high dimensionality of the GIST1M.

When the required number of nearest neighbors is large (*e.g*., 10, 50 and 100), all the graph based methods are significantly better than Flann's KD-tree. Since 10, 50 or 100 results are more common in practical search scenarios, the graph based methods have the advantage.

GNNS and kGraph are essentially the same algorithm. The experimental results confirm this. The slight difference may due to the random initialization.

We implement four graph based methods (GNNS, IEH-LSH, IEH-ITQ and Efanna) exactly with the same framework. The only difference is the initialization: GNNS uses the random selection, IEH uses the hashing and Efanna uses the truncated KD-tree. The performance gap between these methods indicates the effectiveness of different initialization methods. The truncated KD-tree is better than the hashing and these two are better than the random selection. And the ITQ is better than the LSH.

TABLE II shows the index size of different algorithms. Flann consumes the largest memory size. The index size of Efanna is slightly larger than IEH. To reduce the index size, one can use less trees in Efanna but maintain the high performance. We will discuss this in the section 4.5.

The index size of GNNS and KGraph is smallest because they only need to store a $k$NN graph. Both IEH and Efanna sacrifice the index size (additional data structure for better initialization) for better search performance.

Considering both search performance and index size, graph based methods is a better choice than Flann's KD-tree.

### Experiment on Approximate kNN Graph Construction

We show in last section that graph based methods can achieve very good performance on ANN search. However, the results above are based on a ground truth 10-NN graph. Table III shows the time cost to build the ground truth 10-NN graph for two datasets. It takes about 17 hours of CPU time on SIFT1M and about a week on GIST1M. Obviously, brute-force is not an acceptable choice. assume that the ground truth $k$NN graph exists. However, building the $k$NN graph is a step of indexing part of all the graph based methods. To make the graph based ANN search methods practically useful, we need to discuss how to build the $k$NN graph efficiently.

In this section, we will compare the performance of several approximate $k$NN graph construction methods.

### Evaluation Protocol

We use the accuracy-time curve to measure the performance of different approximate $k$NN graph construction algorithms. Given a data set with $N$ points, an approximate $k$NN graph construction method should return $N$ groups of $k$ points, and each group of points stands for nearest neighbors the algorithm finds within the data set for the respective point. Suppose for point $i$, the returned point set of is $R_{i}'$ and the ground truth set is $R_{i}$. Then the accuracy of point $i$, $accuracy_{i}$, is defined as Then the $Accuracy$ of the returned graph is defined as the average accuracy over all the $N$ points: We compare the performance of all the algorithms on building a $10$-NN graph (*i.e*., the sizes of $R_{i}$ and $R_{i}'$ are 10).

TABLE III: Time of building the ground truth 10-NN graph on GIST1M and SIFT1M using brute-force search Figure 4: 10-NN approximate graph construction results on SIFT1M Figure 5: 10-NN approximate graph construction results on GIST1M

### Comparison Algorithms

brute-force: We report the performance of brute-force graph construction to show the advantages of using approxiamate $k$NN graph construction methods. To get different graph accuracy, we simply perform brute-force graph construction on different percentage of the data points.

SGraph: We refer to the algorithm proposed in as SGraph. SGraph build the graph with three steps. First they generates initial graph by randomly dividing the data set into small ones iteratively and the dividing is carried out many times. Then they do brute-force graph construction within each subsets and combine all the subgraph into a whole. Finally they refine the graph using a technique similar to NN-expansion.

FastKNN: We refer to the algorithm proposed in as FastKNN. The last two steps of their graph building process is similar to SGraph. While FastKNN uses hashing method (specifically, AGH) to generate the initial graph.

NN-expansion: The main idea of building approximate $k$NN graph with NN-expansion is to cast the graph construction problem as $N$ ANN search problems, where $N$ is the data size. However, NN-expansion is proposed for ANN search while not for AKNN graph construction. The reason we add it to the compared algorithms in this section is that some previous works claim to outperform NN-descent. While we find there may be misunderstanding that they may actually compared with NN-expansion rather than NN-descent.

NN-descent: This algorithm first initializes the graph randomly. Then NN-descent refine it iteratively with techniques like local join and sampling. Local join is to do brute-force searching within a point $q$'s neighbors which is irrelevant to $q$. Sampling is to ensure number of points involved in the local join is small, but the algorithm is still efficient. kGraph: kGraph is an open source library for approximate $k$NN graph construction and ANN search. The author of kGraph is the author of NN-descent. The approximate $k$NN graph algorithm implemented in kGraph library is exactly NN-descent. kGraph implements with OpenMP and SSE instruction for speed-up. For faire comparison, we disable the parallelism and SSE instruction.

LargeVis: This algorithm is proposed for high dimension data visualization. The first step of LargeVis is to build an approximate $k$NN graph. LargeVis uses random projection tree and NN-expansion to build this graph.

Efanna: The algorithm proposed in this paper. We use hierarchical divide-and-conquer to get an initial graph. And then use NN-descent to refine the graph. In this experiments, we use 8 randomized truncated KD-trees to initialize the graph.

Figure 6: Approximate nearest neighbor search results of 10,000 queries on SIFT1M. We use a 60% ∼ 100% accuracy 10-NN graphs for EFANNA respectively; Both EFANNA and flann-kdtrees use 16 trees.

Figure 7: Approximate nearest neighbor search results of 1,000 queries on GIST1M. We use a 57% ∼ 100% accuracy 10-NN graphs for EFANNA respectively; Both EFANNA and flann-kdtrees use 16 trees.

TABLE IV: Indexing Time of Efanna and flann TABLE V: Efanna graph accuracy VS. k Figure 8: Approximate nearest neighbor search results of 10,000 queries on SIFT1M. We use 4 ∼ 64 trees for EFANNA and flann-kdtrees respectively; The 10-NN ground truth graph is used for EFANNA and ITQ.

Figure 9: Approximate nearest neighbor search results of 1,000 queries on GIST1M. We use 8 ∼ 64 trees for EFANNA and flann-kdtrees respectively; The 10-NN ground truth graph is used for EFANNA and ITQ.

TABLE VI: Index Size of Efanna and Flann with Different Number of Trees

### Results

The time-accuracy curves of different algorithms on two data sets are shown in Fig. 4 and Fig. 5 receptively. A number of interesting conclusions can be made.

EFANNA outperforms all the other algorithms on approximate $k$NN graph building. It can achieve more than 300 times speed-up over brute-force construction to reach 95% accuracy. Without parallelism, it takes a week to build a 10-NN graph on GIST1M using brute-force search. Now the time can be reduced to less than an hour by using EFANNA.

We didn't get the source code of SGraph and FastKNN. So we implement their algorithms on our own. However, the performances shown in the two figures are quite different from what the original papers claim. One of the reasons may be the implementation. In the original FastKNN paper, the authors fail to add the hashing time into the total graph building time but actually should do. Fortunately, reported that SGraph achieved 100 times speed-up over brute-force on the SIFT1M at 95% accuracy. And SGraph got 50 times speed-up over brute-force on the gist1M (384 dimensions) at 90% accuracy. While EFANNA achieves over 300 times speed-up on both SIFT1M and GIST1M (960 dimensions).

LargeVis achieve significant better result than NN-expansion. However, NN-descent is better than LargeVis, especially when we want an accurate graph. This results confirm our assumption that many previous works had the misunderstanding of NN-descent. The result reported in their paper is actually NN-expansion rather than NN-descent. kGraph and NN-descent are actually the same algorithm. The only difference is that we implement NN-descent by ourselves and kGraph is an open library. The performance difference of these two methods should due to the implementation.

The only difference between EFANNA and NN-descent (kGraph) is the initialization. EFANNA uses randomized truncated KD-tree to build the initial graph while NN-descent (kGraph) use random initialization.

The performance advantage of EFANNA over NN-descent is larger on the SIFT1M than on the GIST1M. The reason maybe the GIST1M (960 dimensions) has higher dimensionality than the SIFT1M (128 dimensions). The KD-tree initialization becomes less effective when dimensions becomes high. The similar phenomena happens when we compare EFANNA and LargeVis. Since LargeVis uses random projection trees for initialization, this suggests random projection trees meybe better than KD-tree when the dimensions is high. Using random projection trees as the hierarchical structures of EFANNA can be the future work.

Figure 10: Approximate nearest neighbor search results of 10,000 queries on SIFT1M. We use kNN graphs with various k from 10 to 40 for for EFANNA respectively; Both EFANNA and flann-kdtrees use 16 trees.

Figure 11: Approximate nearest neighbor search results of 1,000 queries on GIST1M. We use kNN graphs with various k from 10 to 40 for for EFANNA respectively; Both EFANNA and flann-kdtrees use 16 trees.

TABLE VII: Index Size of Efanna with Different Number of k for kNN Graph

### EFANNA with Approximate kNN Graphs

The experimental results in the last section show that EFANNA can build an approximate $k$NN graph efficiently. However, there are no published results on the performance of graph based ANN search methods on an approximate $k$NN graph.

In this section, we evaluate the performance of EFANNA on approximate $k$NN graphs with various accuracy. The results on two data sets are shown in Fig.6 and 7 respectively.

From these two figures, we can see that the ANN search performance of EFANNA suffers from very little decrease in performance even when the graph is only "half right". Specifically, the ANN search preformance of EFANNA with a 60% accurate 10-NN graph is still significant better than Flann-kdtree on SIFT1M. On GIST1M, EFANNA with a 57% accurate 10-NN graph is significant better than Flann-kdtree.

These results are significant because building a less accurate $k$NN graph using EFANNA is very efficient. Table IV shows the indexing time of EFANNA and Flann-kdtree. If a 60% accurate graph is used, the indexing time of EFANNA is similar to that of Flann-kdtree. Combing the results in Table II, we can see that comparing with Flann-kdtree, EFANNA takes similar indexing time, smaller index size and significant better ANN search performance.

Why EFANNA can get such a good ANN search performance even with a "half right" graph? Table V may explain the reason. The accuracy defined in Eqn. 2 uses the size of $R$ and $R'$. The former is the true nearest neighbors set while the latter is the returned nearest neighbors set of an algorithm. In the previous experiments, we fix the sizes of both $R$ and $R'$ as 10. Table V reports the results by varying the size of $R$ form 10 to 100. We cam see that a 60% accurate 10-NN graph constructed by EFANNA in SIFT1M means 60% of all the neighbors are true 10-nearest neighbors. And the remaining 40% neighbors are not randomly select from the whole dataset. Actually, 98.9% of the neighbors are true 100-nearest neighbors. These results show that the approximate $k$NN graphs constructed by EFANNA are very good approximation of the ground truth $k$NN graph.

Figure 12: ANN search results of 10,000 queries on SIFT1M. All the four ANN search methods used the same index size as shown in the table (VIII).

Figure 13: ANN search results of 1,000 queries on GIST1M. All the four ANN search methods used the same index size as shown in the table (VIII). tree (hash table) The index size here is the size in the memory, not the size on the disk.

TABLE VIII: Index Size of Different Algorithms

### EFANNA with Different Number of Trees

In the previous experiments, EFANNA uses 16 truncated kd-trees for search initialization. Table II shows that these trees consume a large number of memory space. In this experiment, we want to explore how the number of trees will influence the performance of EFANNA on ANN search. Throughout this experiment, we use the 10-NN ground truth graph.

The ANN search results on SIFT1M and GIST1M are shown in Fig. 8 and FIg. 9 respectively. We simply compare with IEH-ITQ and FLANN, because IEH-ITQ is the second best algorithm on ANN search in our previous experiment while FLANN also has the tree number parameter.

From Fig. 8 and 9, we can see that with less number of trees, the ANN search performances of both EFANNA and Flann decrease. However, with only 4 trees, EFANNA still significantly better than IEH-ITQ (especially on the GIST1M data set). While the index sizes can be significantly reduced as suggested by Table VI. With 4 trees, the index size of EFANNA is smaller than that of IEH-ITQ.

The results in this section show the flexibility of EFANNA over other graph based ANN search methods. One can easily make trade-off between index size and search performance.

### EFANNA with Different Number of $k$ in $k$NN Graph

The EFANNA index contains two parts: the truncated kd-trees and the $k$NN graph. If we regard the $k$NN graph as an $N \times k$ matrix, we can use the "width" of the graph to denote $k$. In the previous section, we have checked the performance of EFANNA with different number of trees. Now we will show how the "width" of $k$NN graph influences ANNS performance of EFANNA.

Fig.10 and 11 show the ANNS performance of EFANNA with graph 10NN, 20NN, 40NN on SIFT1M and GIST1M. The index size are showed in TABLE VII respectively. From TABLE VII we can see that, from 10NN to 40NN, the size of EFANNA index grows gradually. Besides, in Fig.10, 11, the performance of increase with the growing of graph 'width'.

Compared with Fig. 8, 9, we can get a conclusion that widening the graph provides more boost on ANNS performance of EFANNA than add more trees. And from the comparison between TABLE VI and VII, we find that with equal extra memory cost, widening graph is a better choice then using more trees.

However, we should also notice that the performance boost does not increase linearly with the 'width' of the graph. In other words, there may exists an upper bound of performance boost by increasing EFANNA index size, either from the aspect of tree or graph.

### ANN Search Comparison with Same Index Size

The results in previous section suggest the comparisons in section 4.2 is not quite fair due to different index size of different algorithms. In this section, we try to compare different algorithms with (almost) equal index size.

We reported the performance of EFANNA, IEH-ITQ, GNNS and flann's KD-tree. We do not compare with IEH-LSH simply because IEH-ITQ is better than IEH-LSH. We do not compare with kGraph because GNNS is almost identical with kGraph.

We restrict the index size of each algorithm to about 265 MB. Finally, we use 4 trees for flann's KD-tree; 4 trees and 40NN graph for EFANNA; 1 table and 40NN graph for IEH-ITQ; 60NN graph for GNNS. See TABLE VIII for details on how we organize the index to get almost equal size. Fig. 12, 13 show the performance of these algorithms on SIFT1M and GIST1M.

On both two datasets, graph based methods achieve over 20x speed up over flann's KD-tree with the same index size. Particularly, EFANNA is about 30x faster than flann's KD-tree. This suggests the advantage of graph based methods over traditional tree structure based methods.

Compared with the results in Fig. 2 and 3, we can find that the performance gain achieved by EFANNA over IEH-ITQ and GNNS (kGraph) becomes smaller as the "width" of graph grows. This indicates the impact of good initialization for NN-expansion becomes small as the "width" of graph grows.

With the same index size, EFANNA and IEH-ITQ still have small advantage than GNNS on SIFT1M when the recall is low. At a high recall level (*e.g*., 95%), the performances of three algorithms are almost the same. Particularly, when we search for 100NN, the performance of GNNS (random initialization) is better than EFANNA and IEH-ITQ at 95% recall level. This is actually expected because good initializations require additional time. If the information provided by the $k$NN graph is enough, random initialization is the best choice.

On GIST1M, EFANNA still have the advantage over IEH-ITQ and GNNS (kGraph), which again suggest that GIST1M is a "harder" dataset for ANNS problem. We surprisingly find that GNNS is better than IEH-ITQ which suggests truncated KD-tree (used in EFANNA) is a better choice than hashing (ITQ) used for initialization. It's interesting to investigate better initialization algorithms.

## The EFANNA Library

The work in this paper is released as an open source library. Please access the code at Github^22^2

## Conclusion

The goal of this research is to provide a fast solution, EFANNA, for both ANN search and approximate $k$NN graph construction problems. On ANN search, we use hierarchical structures to provide better initialization for NN-expansion. And on graph construction, we use a divide-and-conquer way to construct an initial graph and refine it with NN-descent. Extensive experiments shows that EFANNA outperforms previous algorithms significantly both in approximate $k$NN graph construction and ANN search. Meanwhile, EFANNA also shows great flexibility for different scenarios.
