<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

EFANNA: An Extremely Fast Approximate Nearest Neighbor Search Algorithm Based on kNN Graph

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Approximate nearest neighbor (ANN) search is a fundamental problem in many areas of data mining, machine learning and computer vision. The performance of traditional hierarchical structure (tree) based methods decreases as the dimensionality of data grows, while hashing based methods usually lack efficiency in practice. Recently, the graph based methods have drawn considerable attention. The main idea is that a neighbor of a neighbor is also likely to be a neighbor, which we refer as NN-expansion. These methods construct a k-nearest neighbor (kNN) graph offline. And at online search stage, these methods find candidate neighbors of a query point in some way (\eg, random selection), and then check the neighbors of these candidate neighbors for closer ones iteratively. Despite some promising results, there are mainly two problems with these approaches: 1) These approaches tend to converge to local optima. 2) Constructing a kNN graph is time consuming. We find that these two problems can be nicely solved when we provide a good initialization for NN-expansion. In this paper, we propose EFANNA, an extremely fast approximate nearest neighbor search algorithm based on kNN Graph.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Efanna nicely combines the advantages of hierarchical structure based methods and nearest-neighbor-graph based methods. Extensive experiments have shown that EFANNA outperforms the state-of-art algorithms both on approximate nearest neighbor search and approximate nearest neighbor graph construction. To the best of our knowledge, EFANNA is the fastest algorithm so far both on approximate nearest neighbor graph construction and approximate nearest neighbor search. A library EFANNA based on this research is released on Github.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nearest neighbor search plays an important role in many applications of data mining, machine learning and computer vision. When dealing with sparse data (*e.g*., document retrieval), one can use advanced index structures (*e.g*., inverted index) to solve this problem. However, for data with dense features, the cost for finding the exact nearest neighbor is $O{(N)}$, where $N$ is the number of points in the database. It's very time consuming when the data set is large. So people turn to Approximate Nearest neighbor (ANN) search in practice. Many work has been done to carry out the ANN search with high accuracy but low computational complexity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are mainly two types of methods in ANN search. The first type methods are hierarchical structure (tree) based methods, such as KD-tree,Randomized KD-tree, K-means tree. These methods perform very well when the dimension of the data is relatively low. However, the performance decreases dramatically as the dimension of the data increases. The second type methods are hashing based methods, such as Locality Sensitive Hashing (LSH), Spectral Hashing, Iterative Quantization and so. Please see for a detailed survey on various hashing methods. These methods generate binary codes for high dimensional real vectors while try to preserve the similarity among original real vectors. Thus, all the real vectors fall into different hashing buckets (with different binary codes). Ideally, if neighbor vectors fall into the same bucket or the nearby buckets (measured by the hamming distance of two binary codes), the hashing based methods can efficiently retrieve the nearest neighbors of a query point. However, there is no guarantee that all the neighbor vectors will fall into the nearby buckets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To ensure the high *recall* (the number of true neighbors within the returned points set divides by the number of required neighbors), one needs to examine many hashing buckets (*i.e*., enlarge the search radius in hamming space), which results a high computational complexity. Please see for a detailed analysis.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, graph based methods have drawn considerable attention. The essential idea behind these approaches is that *a neighbor of a neighbor is also likely to be a neighbor*, which we refer as *NN-expansion*. These methods construct a $k$-nearest neighbor ($k$NN) graph offline. And at online search stage, these methods find the candidate neighbors of a query point in some way (*e.g*., random selection ), and then check the neighbors of these candidate neighbors for closer ones iteratively. One problem of this approach is that the NN-expansion is easily to converge to local optima and result in a low recall. tries to solve this problem by providing better initialization for a query point. Instead of random selection, uses hashing based methods for initialization. This approach is named as Iterative Expanding Hashing (IEH) and achieves significant better results than the corresponding hashing based methods.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another challenge on using graph based methods is the high computational cost in building the $k$NN graph, especially when the database is large. There are many efforts that have been put into reducing the time complexity of $k$NN graph construction. try to speed up an exact $k$NN graph construction. However, these approaches are still not efficient enough in the context of big data. Instead of building an exact $k$NN graph, recent researchers try to build an approximated $k$NN graph efficiently. The *NN-expansion* idea again can be used to build an approximated $k$NN graph. proposed NN-descent to efficiently build an approximate $k$NN graph. try to build an approximate $k$NN graph in a divide-and-conquer manner. Their algorithms mainly contain three phrases. Firstly, they divide the whole data set into small subsets multiple times. Secondly, they do brute force search within the subsets and get lots of overlapping subgraphs. Finally, they merge the subgraphs and refine the graph with techniques similar to NN-expansion.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although an approximated $k$NN graph can be efficiently constructed, there are no formal study on how the performance of graph based search methods will be affected if one uses an approximated $k$NN graph instead of an exact $k$NN graph.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To tackle above problems, we propose a novel graph-based approximate nearest neighbor search framework EFANNA in this paper. EFANNA is an abbreviation for two algorithms: Extremely Fast Approximate $k$-Nearest Neighbor graph construction Algorithm and Extremely Fast Approximate Nearest Neighbor search Algorithm based on $k$NN graph. Our algorithm is based on a simple observation: the performance of both NN-expansion and NN-descent is very sensitive with the initialization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our EFANNA index contains two parts: the multiple randomized hierarchical structures (*e.g*., randomized truncated KD-tree) and an approximate $k$-nearest neighbor graph.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

At offline stage, EFANNA divides the data set multiple times into a number of subsets in a fast and hierarchical way, producing multiple randomized hierarchical structures. Then EFANNA constructs an approximate $k$NN graph by conquering bottom-up along the structures. When conquering, EFANNA takes advantage of the structures to locate the closest possible neighbors, and use these candidates to update the graph, which reduces the computation cost than using all the points in the subtree. Finally we refine the graph similar to NN-descent, which is based on the NN-expansion idea and optimized with techniques like local join, sampling, and early termination.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

At online search stage, EFANNA first search in the hierarchical structures to get candidate neighbors for a given query. Then EFANNA refines the results using NN-expansion on the approximate $k$NN graph. Extensive experimental results show that our approach outperforms the the-state-of-the-art approximate nearest neighbor search algorithms significantly.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is worthwhile to highlight the contributions of our paper as follows: EFANNA outperforms state-of-the-art ANN search algorithms significantly. Particularly, EFANNA outperforms Flann, one of the most popular ANN search library, in index size, search speed and search accuracy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

EFANNA can build an approximate $k$NN graph with hundreds times speed-up over brute-force graph building on million scale datasets. Considering many unsupervised and semi-supervised machine learning algorithms are based on a nearest neighbor graph. EFANNA provides the possibility to examine the effectiveness of all these algorithms on large scale datasets.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show by experimental results that with an approximate $k$NN graph of low accuracy constructed by EFANNA, graph-based ANN search methods (*e.g*., EFANNA) still perform very good. This is because the "error" neighbors of approximate $k$NN graph constructed by EFANNA are actually neighbors a little farther. This property is never explored in the previous work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. In Section 2 we will introduce some related work. Our EFANNA algorithm is presented in section 3. In section 4, we will report the experimental results and show the performance of EFANNA comprehensively. In section 5 we will talk about our open library and in section 6 we will draw a conclusion.

<!-- chunk {"id": "body-0018", "role": "body", "section": "EFANNA Algorithms for ANN search", "weight": 1.0} -->

We will introduce our EFANNA algorithms in this section. EFANNA algorithms include offline index building part and online ANN search algorithm. The EFANNA index contains two parts: multiple hierarchical structures (*e.g*., randomized truncated KD-tree) and an approximate $k$NN graph. We will first show how to use EFANNA index to carry out online ANN search. Then we will show how to build the EFANNA index in a divide-conquer-refinement manner.

<!-- chunk {"id": "body-0019", "role": "body", "section": "EFANNA Algorithms for ANN search", "weight": 1.0} -->

1:the data set D, the number of trees T, the number of points in a leaf node K. 2:the randomized truncated KD-tree set S 5: if size of PointSet < K then 8: Randomly choose dimension d. 9: Calculate the mean m i d over P o i n t S e t on dimension d. 10: Divide P o i n t S e t evenly into two subsets, L e f t H a l f and R i g h t H a l f, according to m i d. Algorithm 2 EFANNA Tree Building Algorithm

<!-- chunk {"id": "body-0020", "role": "body", "section": "ANN search with EFANNA index", "weight": 1.0} -->

EFANNA is a graph based method. The main idea is providing better initialization for NN-expansion to improve the performance significantly. The multiple hierarchical structures is used for initialization and the approximate $k$NN graph is used for NN-expansion.

<!-- chunk {"id": "body-0021", "role": "body", "section": "ANN search with EFANNA index", "weight": 1.0} -->

There are many possible hierarchical structures (*e.g*. hierarchical clustering or randomized division tree ) can be used in our index structure. In this paper, we only report the results using randomized *truncated* KD-tree. The details on the difference between this structure and the traditional randomized KD-tree will be discussed in the next subsection. Based on this randomized truncated KD-tree, we can get the initial neighbor candidates given a query $q$. We then refine the result with NN-expansion, *i.e*., we check the neighbors of $q$'s neighbors according to the approximate $k$NN graph to get closer neighbors. Algorithm 1 shows the detailed procedure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "ANN search with EFANNA index", "weight": 1.0} -->

There are three essential parameters in our ANN search algorithm: the expansion factor $E$, the the candidate pool size $P$ and the iteration number $I$. In our experiment, we found $I = 4$ is enough and thus we fixed $I = 4$. The trade-off between search speed and accuracy can be made through tuning parameters $E$ and $P$. In other words, larger $E$ and larger $P$ sacrifice the search speed for high accuracy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "ANN search with EFANNA index", "weight": 1.0} -->

1:the data set D, the k in approximate kNN graph, the randomized truncated KD-tree set S built with Algorithm 2, the conquer-to depth D e p. 2:approximate kNN graph G. 4:Using Algorithm 2 to build tree, which leads to the input S 8:for all point i in D do 10: for all binary tree t in S do 11: search in tree t with point i to the leaf node. 12: add all the point in the leaf node to C. 16: Depth-first-search in the tree t with point i to depth d. Suppose N is the non-leaf node on the search path with depth d. Suppose S i b is the child node of N. And S i b is not on the search path of point i. 17: Depth-first-search to the leaf node in the subtree of S i b with point i. Add all the points in the leaf node to C. 20: Reserve K closest points to i in C. Algorithm 3 Hierarchical Divide-and-Conquer Algorithm (kNN Graph Initialization)

<!-- chunk {"id": "body-0024", "role": "body", "section": "EFANNA Index Building Algorithms I: Tree Buidling", "weight": 1.0} -->

One part of the EFANNA index is a multiple hierarchical structures. There are many possible hierarchical structures (*e.g*. hierarchical clustering or randomized division tree ) can be used. In this paper, we only report the results using randomized *truncated* KD-tree. Please see Algorithm 2 for details on building randomized truncated KD-trees.

<!-- chunk {"id": "body-0025", "role": "body", "section": "EFANNA Index Building Algorithms I: Tree Buidling", "weight": 1.0} -->

The only difference between randomized *truncated* KD-tree and the traditional randomized KD-tree is that leaf node in our trees has $K$ ($K = 10$ in our experiments) points instead of 1. This change makes the tree building in EFANNA much faster than the the traditional randomized KD-tree. Please see Table IV in the experiments for details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "EFANNA Index Building Algorithms I: Tree Buidling", "weight": 1.0} -->

The randomized truncated KD-tree built in this step is used not only in the on-line search stage, but also in the approximate $k$NN graph construction stage. See the next section for details.

<!-- chunk {"id": "body-0027", "role": "body", "section": "EFANNA Index Building Algorithms II: Approximate $k$NN Graph Construction", "weight": 1.0} -->

Another part of the EFANNA index is an approximate $k$NN graph. We use the similar methodology to efficiently build the approximate $k$NN graph as with ANN search. It contains two stage. At first stage, we regard the trees built in the previous part as multiple overlapping divisions over the data set, and we perform the conquering step along the tree structures to get an initial $k$NN graph. At second stage, we use NN-descent to refine the $k$NN graph.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

uses a random $k$NN graph as the initialization and refined it with the NN-descent algorithm to get a $k$NN graph with high accuracy. Our idea is very simple. We try to provide a better initialization for NN-descent. A good initialization should produce an initial $k$NN graph with certain accuracy within short time.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

Divide-and-conquer is a good strategy to achieve this goal. A normal divide-and-conquer process first breaks the problem into subproblems recursively until the subproblem is small and easy enough to solve. Then the solutions of subproblems are combined to get a solution to the original problem. For approximate graph construction, the division part is easy. We can divide the data set as the way the tree was constructed (Section 3.2). Then we merge sibling nodes recursively upwards from leaf. With only one tree, we need to conquer to root to get a full connected graph. But if we directly conquer from leaf to root, the computational cost grows exponentially upwards and is no less than brute-force graph construction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

To reduce the computational complexity, we need to find a better conquer strategy and avoid conquering to root. We follow the inspiration of previous work, which said multiple randomized division can produce overlapping subsets. As a result, the conquer doesn't need to be carried out to root. In addition, our motivation on better conquer strategy is to reduce the number of points involved in conquering at each level and keep points' "quality" (we make sure that we always choose the closest possible points for conquer). For example, in Fig 1, if we know that point $q$ in node (or subset) $8$ is closer to the area of node $10$, then we just need to consider the points in node $10$ when conquering $4$ and $5$ at level $1$ with $q$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

In other words, when we conquer two sibling non-leaf nodes (sibling leaf nodes can be conquered directly), for some points in one subtree, we may just consider the "closest" possible leaf node in the sibling subtree. Because the rest leaf nodes are farther, the points in them are also likely to be farther, thus excluded from distance calculating. We can regard the tree as a multi-class classifier, each leaf node can be treated as a class. This classifier may divide the data space like the rectangle in Fig. 1 does and different colors represent different labels. Sometimes nearest neighbors (*e.g*. white points in area $8$ and area $10$) are close to each other, but fit in different area according to this classifier with a discriminative plane (*e.g*. node $2$) separating them. In Fig.1, suppose point $q$ will be assigned label $8$ when $q$ is input into the tree classifier. When conquering at level $1$, we need to know in subtree $5$ which area between node $10$ and $11$ is closer to $q$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

Now that the whole tree can be treated as a multi-class classifier, any subtree of it can be a multi-class classifier, too. To know which area is closer, we simply let the classifier of subtree $5$ make the choice. By inputing $q$ to the classifier, we will obtain a label between 10 and 11 for q. Since $q$ is the white point in area $8$, from the rectangle in Fig. 1, it's obvious that $q$ will be labeled as $10$. Therefore for $q$, when conquering at level $1$, only points in node $10$ will be involved.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

1:an initial approximate k-nearest neighbor graph Gi n i t, data set D, maximum iteration number I, Candidate pool size P, new neighbor checking num L. 2:an approximate kNN graph G. 4:Graph Gn e w records all the new added candidate neighbors of each point. Gn e w = Gi n i t. 5:Graph Go l d records all the old candidate neighbors of each point at previous iterations. Go l d = ⌀ 6:Graph Gr n e w records all the new added reverse candidate neighbors of each point. 7:Graph Gr o l d records all the old reverse candidate neighbors of each point. 10: for all point i in D do 11: N Nn e w is the neighbor set of point i in Gn e w. 12: N No l d is the neighbor set of of point i in Go l d. 13: for all point j in N Nn e w do 14: for all point k in N Nn e w do 16: calculate the distance between j and k. 17: add k to j’s entry in G. mark k as n e w.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

18: add j to k’s entry in G and Gr n e w. 22: for all point l in N No l d do 23: calculate the distance between j and l. 24: add l to j’s entry in G. mark l as o l d. 25: add j to l’s entry in G and Gr o l d. 30: for all point i in D do 31: Reserve the closest P points to i in respective 35: for all point i in D do 36: l = 0. N N is the neighbor set of i in G. Algorithm 4 Approximate kNN Graph Refinement Algorithm In this way, for each point at each level, only the points in one closest leaf node will be considered, which reduces the computation complexity greatly and reserves accuracy. We perform our random divide-and-conquer process multiple times and get an initial graph.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Hierarchical Randomized Divide-and-Conquer", "weight": 1.0} -->

Again there is a trade-off between accuracy of initial graph and time cost in parameter tuning. When conquer-to depth $Dep$ is small (*i.e*. conquering to a level close to root), or when tree number $T_{c}$ is larger, the accuracy is higher but time cost is higher. In our experiments, we use the randomized KD-tree as the hierarchical divide-and-conquer structure. See Algorithm 3 for details on randomized KD-tree divide-and-conquer algorithm).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Graph Refinement", "weight": 1.0} -->

We use the NN-descent proposed by to refine the resulting graph we get from the divide-and-conquer step. The main idea is also to find better neighbors iteratively, however, different from NN-expansion, they proposed several techniques to get much better performance. We rewrite their algorithms to make it easy to understand. See Algorithm 4 for details.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Graph Refinement", "weight": 1.0} -->

The pool size $P$ and neighbor checking num $L$ are essential parameters of this algorithm. Usually, Larger $L$ and $P$ will result in better accuracy but higher computation cost.

<!-- chunk {"id": "body-0038", "role": "body", "section": "NN-expansion VS. NN-descent", "weight": 1.0} -->

Some approximate $k$NN graph construction methods claim to outperform NN-descent significantly. However, based on their reported results and our analysis, there seems a misunderstanding of NN-descent. Actually, NN-descent is quite different than NN-expansion. For given point $p$, NN-expansion assume the neighbors of $p$'s neighbors are likely to be neighbors of $p$. While NN-descent thinks that $p$'s neighbors are more likely to be neighbors of each other. Our experimental results have shown that NN-descent is much more efficient than NN-expansion in building approximate $k$NN graph. However, the NN-descent idea cannot be applied to ANN search.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Online index updating", "weight": 1.0} -->

EFANNA index building algorithm is easily to be extended to accept stream data. Firstly, when a new point arrived, we can insert it into the tree easily. And when the number of points in the inserted node exceeds given threshold, we just need to split the node. When the tree is unbalanced to some degree, we should adjust the tree structure, which is quite fast on large scale data. Secondly, the graph building algorithm can accept stream data as well, we can use the same algorithm we describe before. First we search in the tree for candidates, and use NN-descent to update the graph with the involved points. And this step is quite fast, too.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

To demonstrate the effectiveness of the proposed method EFANNA, extensive experiments on large-scale data sets are reported in this section.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data Set and Experiment Setting", "weight": 1.0} -->

The experiments were conducted on two popular real world data sets, SIFT1M and GIST1M^11^1Both two datasets can be downloaded at The detailed information on the data sets is listed in TABLE I. All the codes we used are written in C++ and compiled by g++4.9, and the only optimization option we allow is "O3" of g++. Parallelism and other optimization like SSE instruction are disabled. The experiment on SIFT1M is carried out on a machine with i7-3770K CPU and 16G memory, and GIST1M is on a machine with i7-4790K CPU and 32G memory.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

To measure the performance of ANN search of different algorithms, we used the well known $average$ $recall$ as the accuracy measurement. Given a query point, all the algorithms are expected to return $k$ points. Then we need to examine how many points in this returned set are among the true $k$ nearest neighbors of the query. Suppose the returned set of $k$ points given a query is $R'$ and the true $k$ nearest neighbors set of the query is $R$, the $recall$ is defined as Then the $average$ $recall$ is averaging over all the queries. Since the sizes of $R'$ and $R$ are the same, the recall of $R'$ is the same as the accuracy of $R'$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

We compare the performance of different algorithms by requiring different number of nearest neighbors of each query point, including 1-NN and 100-NN. In other words, the size of $R$ (and $R'$) will be 1 and 100 respectively. Please see our technical report for more results on 10-NN and 50-NN.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

To demonstrate the effectiveness of the proposed EFANNA approach, the following four state-of-the-art ANN search methods and brute-force method are compared in the experiment. brute-force. We report the performance of brute-force search to show the advantages of using ANN search methods. To get different recall, we simply perform brute-force search on different percentage of the query number. For example, the brute-force search time on 90% queries of the origin query set stands for the brute-force search time of 90% average recall. flann. FLANN is a well-known open source library for ANN search. The Randomized KD-tree algorithm in FLANN provides state-of-the-art performance. In our experiments, we use 16 trees for both datasets. And we tune the "max-check" parameter to get the time-recall curve.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

GNNS. GNNS is the first ANN search method using $k$NN graph. Given a query, GNNS generates the initial candidates (neighbors) by random selection. Then GNNS uses the NN-expansion idea (*i.e*., check the neighbors of the neighbors iteratively to locate closer neighbors) to refine the result. The main parameters of GNNS are the size of the initial result and the iteration number. We fix the iteration number as 10 and tune the initial candidate number to get the time-recall curve. kGraph. kGraph is an open library for ANN search based on $k$NN graph. The author of kGraph is the inventor of NN-descent. The ANN search algorithm in kGraph is essentially the same as GNNS. The original Kgraph library implements with OpenMP (for parallelism) and SSE instructions for speed-up. We simply turn off the parallelism and SSE for fair comparison.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

IEH. IEH is a short name for Iterative Expanding Hashing. It is another ANN search method using $k$NN graph. Different from GNNS, IEH uses hashing methods to generate the initial result given a query. Considering the efficiency of hash coding, IEH-LSH and IEH-ITQ are compared in our experiment. The former uses LSH as the hashing method and the latter uses ITQ as the hashing method. Both hashing methods use 32 bit code. We also fix the iteration number as 10 and tune the initial result size to get the time-recall curve.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

Efanna. The algorithm proposed in this paper. We use 16 trees for both datasets and the iteration number in NN-expansion stage is fixed as 4. We tune the search-to depth parameter $S_{depth}$ and the candidate pool size $P$ to get the time-recall curve. tree (hash table) The index size here is the size in the memory, not the size on the disk.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

All the graph based methods need a pre-built $k$NN graph and we use a ground truth 10-NN graph.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

The time-recall curves of all the algorithms on two data sets can be seen in Fig. 2 and Fig. 3. The index size of various algorithms are shown in Table II. A number of interesting conclusions can be drawn as follows: Our Efanna algorithm significantly outperforms all the other methods at all the cases on both of two data sets. Even at a relatively high recall (*e.g*., 95%), Efanna is about 100x faster than the brute-force search on the SIFT1M and about 10x faster than the brute-force search on the GIST1M.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

The GIST1M is a harder dataset than the SIFT1M for ANN search. At a relatively high recall (*e.g*., 95%), all the ANN search methods are significantly faster than the brute-force search. However, on GIST1M some methods (flann, GNNS, kGrpah) are similar (or even slower) to the brute-force search. The reason may be the high dimensionality of the GIST1M.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

When the required number of nearest neighbors is large (*e.g*., 10, 50 and 100), all the graph based methods are significantly better than Flann's KD-tree. Since 10, 50 or 100 results are more common in practical search scenarios, the graph based methods have the advantage.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

GNNS and kGraph are essentially the same algorithm. The experimental results confirm this. The slight difference may due to the random initialization.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

We implement four graph based methods (GNNS, IEH-LSH, IEH-ITQ and Efanna) exactly with the same framework. The only difference is the initialization: GNNS uses the random selection, IEH uses the hashing and Efanna uses the truncated KD-tree. The performance gap between these methods indicates the effectiveness of different initialization methods. The truncated KD-tree is better than the hashing and these two are better than the random selection. And the ITQ is better than the LSH.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

The index size of GNNS and KGraph is smallest because they only need to store a $k$NN graph. Both IEH and Efanna sacrifice the index size (additional data structure for better initialization) for better search performance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

Considering both search performance and index size, graph based methods is a better choice than Flann's KD-tree.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiment on Approximate kNN Graph Construction", "weight": 1.0} -->

We show in last section that graph based methods can achieve very good performance on ANN search. However, the results above are based on a ground truth 10-NN graph. Table III shows the time cost to build the ground truth 10-NN graph for two datasets. It takes about 17 hours of CPU time on SIFT1M and about a week on GIST1M. Obviously, brute-force is not an acceptable choice. assume that the ground truth $k$NN graph exists. However, building the $k$NN graph is a step of indexing part of all the graph based methods. To make the graph based ANN search methods practically useful, we need to discuss how to build the $k$NN graph efficiently.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiment on Approximate kNN Graph Construction", "weight": 1.0} -->

In this section, we will compare the performance of several approximate $k$NN graph construction methods.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

We use the accuracy-time curve to measure the performance of different approximate $k$NN graph construction algorithms. Given a data set with $N$ points, an approximate $k$NN graph construction method should return $N$ groups of $k$ points, and each group of points stands for nearest neighbors the algorithm finds within the data set for the respective point. Suppose for point $i$, the returned point set of is $R_{i}'$ and the ground truth set is $R_{i}$. Then the accuracy of point $i$, $accuracy_{i}$, is defined as Then the $Accuracy$ of the returned graph is defined as the average accuracy over all the $N$ points: We compare the performance of all the algorithms on building a $10$-NN graph (*i.e*., the sizes of $R_{i}$ and $R_{i}'$ are 10).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

brute-force: We report the performance of brute-force graph construction to show the advantages of using approxiamate $k$NN graph construction methods. To get different graph accuracy, we simply perform brute-force graph construction on different percentage of the data points.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

SGraph: We refer to the algorithm proposed in as SGraph. SGraph build the graph with three steps. First they generates initial graph by randomly dividing the data set into small ones iteratively and the dividing is carried out many times. Then they do brute-force graph construction within each subsets and combine all the subgraph into a whole. Finally they refine the graph using a technique similar to NN-expansion.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

FastKNN: We refer to the algorithm proposed in as FastKNN. The last two steps of their graph building process is similar to SGraph. While FastKNN uses hashing method (specifically, AGH) to generate the initial graph.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

NN-expansion: The main idea of building approximate $k$NN graph with NN-expansion is to cast the graph construction problem as $N$ ANN search problems, where $N$ is the data size. However, NN-expansion is proposed for ANN search while not for AKNN graph construction. The reason we add it to the compared algorithms in this section is that some previous works claim to outperform NN-descent. While we find there may be misunderstanding that they may actually compared with NN-expansion rather than NN-descent.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

NN-descent: This algorithm first initializes the graph randomly. Then NN-descent refine it iteratively with techniques like local join and sampling. Local join is to do brute-force searching within a point $q$'s neighbors which is irrelevant to $q$. Sampling is to ensure number of points involved in the local join is small, but the algorithm is still efficient. kGraph: kGraph is an open source library for approximate $k$NN graph construction and ANN search. The author of kGraph is the author of NN-descent. The approximate $k$NN graph algorithm implemented in kGraph library is exactly NN-descent. kGraph implements with OpenMP and SSE instruction for speed-up. For faire comparison, we disable the parallelism and SSE instruction.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

LargeVis: This algorithm is proposed for high dimension data visualization. The first step of LargeVis is to build an approximate $k$NN graph. LargeVis uses random projection tree and NN-expansion to build this graph.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Comparison Algorithms", "weight": 1.0} -->

Efanna: The algorithm proposed in this paper. We use hierarchical divide-and-conquer to get an initial graph. And then use NN-descent to refine the graph. In this experiments, we use 8 randomized truncated KD-trees to initialize the graph.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Results", "weight": 1.0} -->

The time-accuracy curves of different algorithms on two data sets are shown in Fig. 4 and Fig. 5 receptively. A number of interesting conclusions can be made.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results", "weight": 1.0} -->

EFANNA outperforms all the other algorithms on approximate $k$NN graph building. It can achieve more than 300 times speed-up over brute-force construction to reach 95% accuracy. Without parallelism, it takes a week to build a 10-NN graph on GIST1M using brute-force search. Now the time can be reduced to less than an hour by using EFANNA.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Results", "weight": 1.0} -->

We didn't get the source code of SGraph and FastKNN. So we implement their algorithms on our own. However, the performances shown in the two figures are quite different from what the original papers claim. One of the reasons may be the implementation. In the original FastKNN paper, the authors fail to add the hashing time into the total graph building time but actually should do. Fortunately, reported that SGraph achieved 100 times speed-up over brute-force on the SIFT1M at 95% accuracy. And SGraph got 50 times speed-up over brute-force on the gist1M (384 dimensions) at 90% accuracy. While EFANNA achieves over 300 times speed-up on both SIFT1M and GIST1M (960 dimensions).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Results", "weight": 1.0} -->

LargeVis achieve significant better result than NN-expansion. However, NN-descent is better than LargeVis, especially when we want an accurate graph. This results confirm our assumption that many previous works had the misunderstanding of NN-descent. The result reported in their paper is actually NN-expansion rather than NN-descent. kGraph and NN-descent are actually the same algorithm. The only difference is that we implement NN-descent by ourselves and kGraph is an open library. The performance difference of these two methods should due to the implementation.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Results", "weight": 1.0} -->

The only difference between EFANNA and NN-descent (kGraph) is the initialization. EFANNA uses randomized truncated KD-tree to build the initial graph while NN-descent (kGraph) use random initialization.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Results", "weight": 1.0} -->

The performance advantage of EFANNA over NN-descent is larger on the SIFT1M than on the GIST1M. The reason maybe the GIST1M (960 dimensions) has higher dimensionality than the SIFT1M (128 dimensions). The KD-tree initialization becomes less effective when dimensions becomes high. The similar phenomena happens when we compare EFANNA and LargeVis. Since LargeVis uses random projection trees for initialization, this suggests random projection trees meybe better than KD-tree when the dimensions is high. Using random projection trees as the hierarchical structures of EFANNA can be the future work.

<!-- chunk {"id": "body-0072", "role": "body", "section": "EFANNA with Approximate kNN Graphs", "weight": 1.0} -->

The experimental results in the last section show that EFANNA can build an approximate $k$NN graph efficiently. However, there are no published results on the performance of graph based ANN search methods on an approximate $k$NN graph.

<!-- chunk {"id": "body-0073", "role": "body", "section": "EFANNA with Approximate kNN Graphs", "weight": 1.0} -->

In this section, we evaluate the performance of EFANNA on approximate $k$NN graphs with various accuracy. The results on two data sets are shown in Fig.6 and 7 respectively.

<!-- chunk {"id": "body-0074", "role": "body", "section": "EFANNA with Approximate kNN Graphs", "weight": 1.0} -->

From these two figures, we can see that the ANN search performance of EFANNA suffers from very little decrease in performance even when the graph is only "half right". Specifically, the ANN search preformance of EFANNA with a 60% accurate 10-NN graph is still significant better than Flann-kdtree on SIFT1M. On GIST1M, EFANNA with a 57% accurate 10-NN graph is significant better than Flann-kdtree.

<!-- chunk {"id": "body-0075", "role": "body", "section": "EFANNA with Approximate kNN Graphs", "weight": 1.0} -->

These results are significant because building a less accurate $k$NN graph using EFANNA is very efficient. Table IV shows the indexing time of EFANNA and Flann-kdtree. If a 60% accurate graph is used, the indexing time of EFANNA is similar to that of Flann-kdtree. Combing the results in Table II, we can see that comparing with Flann-kdtree, EFANNA takes similar indexing time, smaller index size and significant better ANN search performance.

<!-- chunk {"id": "body-0076", "role": "body", "section": "EFANNA with Approximate kNN Graphs", "weight": 1.0} -->

Why EFANNA can get such a good ANN search performance even with a "half right" graph? Table V may explain the reason. The accuracy defined in Eqn. 2 uses the size of $R$ and $R'$. The former is the true nearest neighbors set while the latter is the returned nearest neighbors set of an algorithm. In the previous experiments, we fix the sizes of both $R$ and $R'$ as 10. Table V reports the results by varying the size of $R$ form 10 to 100. We cam see that a 60% accurate 10-NN graph constructed by EFANNA in SIFT1M means 60% of all the neighbors are true 10-nearest neighbors. And the remaining 40% neighbors are not randomly select from the whole dataset. Actually, 98.9% of the neighbors are true 100-nearest neighbors. These results show that the approximate $k$NN graphs constructed by EFANNA are very good approximation of the ground truth $k$NN graph.

<!-- chunk {"id": "body-0077", "role": "body", "section": "EFANNA with Different Number of Trees", "weight": 1.0} -->

In the previous experiments, EFANNA uses 16 truncated kd-trees for search initialization. Table II shows that these trees consume a large number of memory space. In this experiment, we want to explore how the number of trees will influence the performance of EFANNA on ANN search. Throughout this experiment, we use the 10-NN ground truth graph.

<!-- chunk {"id": "body-0078", "role": "body", "section": "EFANNA with Different Number of Trees", "weight": 1.0} -->

The ANN search results on SIFT1M and GIST1M are shown in Fig. 8 and FIg. 9 respectively. We simply compare with IEH-ITQ and FLANN, because IEH-ITQ is the second best algorithm on ANN search in our previous experiment while FLANN also has the tree number parameter.

<!-- chunk {"id": "body-0079", "role": "body", "section": "EFANNA with Different Number of Trees", "weight": 1.0} -->

From Fig. 8 and 9, we can see that with less number of trees, the ANN search performances of both EFANNA and Flann decrease. However, with only 4 trees, EFANNA still significantly better than IEH-ITQ (especially on the GIST1M data set). While the index sizes can be significantly reduced as suggested by Table VI. With 4 trees, the index size of EFANNA is smaller than that of IEH-ITQ.

<!-- chunk {"id": "body-0080", "role": "body", "section": "EFANNA with Different Number of Trees", "weight": 1.0} -->

The results in this section show the flexibility of EFANNA over other graph based ANN search methods. One can easily make trade-off between index size and search performance.

<!-- chunk {"id": "body-0081", "role": "body", "section": "EFANNA with Different Number of $k$ in $k$NN Graph", "weight": 1.0} -->

The EFANNA index contains two parts: the truncated kd-trees and the $k$NN graph. If we regard the $k$NN graph as an $N \times k$ matrix, we can use the "width" of the graph to denote $k$. In the previous section, we have checked the performance of EFANNA with different number of trees. Now we will show how the "width" of $k$NN graph influences ANNS performance of EFANNA.

<!-- chunk {"id": "body-0082", "role": "body", "section": "EFANNA with Different Number of $k$ in $k$NN Graph", "weight": 1.0} -->

Fig.10 and 11 show the ANNS performance of EFANNA with graph 10NN, 20NN, 40NN on SIFT1M and GIST1M. The index size are showed in TABLE VII respectively. From TABLE VII we can see that, from 10NN to 40NN, the size of EFANNA index grows gradually. Besides, in Fig.10, 11, the performance of increase with the growing of graph 'width'.

<!-- chunk {"id": "body-0083", "role": "body", "section": "EFANNA with Different Number of $k$ in $k$NN Graph", "weight": 1.0} -->

Compared with Fig. 8, 9, we can get a conclusion that widening the graph provides more boost on ANNS performance of EFANNA than add more trees. And from the comparison between TABLE VI and VII, we find that with equal extra memory cost, widening graph is a better choice then using more trees.

<!-- chunk {"id": "body-0084", "role": "body", "section": "EFANNA with Different Number of $k$ in $k$NN Graph", "weight": 1.0} -->

However, we should also notice that the performance boost does not increase linearly with the 'width' of the graph. In other words, there may exists an upper bound of performance boost by increasing EFANNA index size, either from the aspect of tree or graph.

<!-- chunk {"id": "body-0085", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

The results in previous section suggest the comparisons in section 4.2 is not quite fair due to different index size of different algorithms. In this section, we try to compare different algorithms with (almost) equal index size.

<!-- chunk {"id": "body-0086", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

We reported the performance of EFANNA, IEH-ITQ, GNNS and flann's KD-tree. We do not compare with IEH-LSH simply because IEH-ITQ is better than IEH-LSH. We do not compare with kGraph because GNNS is almost identical with kGraph.

<!-- chunk {"id": "body-0087", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

We restrict the index size of each algorithm to about 265 MB. Finally, we use 4 trees for flann's KD-tree; 4 trees and 40NN graph for EFANNA; 1 table and 40NN graph for IEH-ITQ; 60NN graph for GNNS. See TABLE VIII for details on how we organize the index to get almost equal size. Fig. 12, 13 show the performance of these algorithms on SIFT1M and GIST1M.

<!-- chunk {"id": "body-0088", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

On both two datasets, graph based methods achieve over 20x speed up over flann's KD-tree with the same index size. Particularly, EFANNA is about 30x faster than flann's KD-tree. This suggests the advantage of graph based methods over traditional tree structure based methods.

<!-- chunk {"id": "body-0089", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

Compared with the results in Fig. 2 and 3, we can find that the performance gain achieved by EFANNA over IEH-ITQ and GNNS (kGraph) becomes smaller as the "width" of graph grows. This indicates the impact of good initialization for NN-expansion becomes small as the "width" of graph grows.

<!-- chunk {"id": "body-0090", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

With the same index size, EFANNA and IEH-ITQ still have small advantage than GNNS on SIFT1M when the recall is low. At a high recall level (*e.g*., 95%), the performances of three algorithms are almost the same. Particularly, when we search for 100NN, the performance of GNNS (random initialization) is better than EFANNA and IEH-ITQ at 95% recall level. This is actually expected because good initializations require additional time. If the information provided by the $k$NN graph is enough, random initialization is the best choice.

<!-- chunk {"id": "body-0091", "role": "body", "section": "ANN Search Comparison with Same Index Size", "weight": 1.0} -->

On GIST1M, EFANNA still have the advantage over IEH-ITQ and GNNS (kGraph), which again suggest that GIST1M is a "harder" dataset for ANNS problem. We surprisingly find that GNNS is better than IEH-ITQ which suggests truncated KD-tree (used in EFANNA) is a better choice than hashing (ITQ) used for initialization. It's interesting to investigate better initialization algorithms.

<!-- chunk {"id": "body-0092", "role": "body", "section": "The EFANNA Library", "weight": 1.0} -->

The work in this paper is released as an open source library. Please access the code at Github^22^2

<!-- chunk {"id": "body-0093", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The goal of this research is to provide a fast solution, EFANNA, for both ANN search and approximate $k$NN graph construction problems. On ANN search, we use hierarchical structures to provide better initialization for NN-expansion. And on graph construction, we use a divide-and-conquer way to construct an initial graph and refine it with NN-descent. Extensive experiments shows that EFANNA outperforms previous algorithms significantly both in approximate $k$NN graph construction and ANN search. Meanwhile, EFANNA also shows great flexibility for different scenarios.
