EFANNA : An Extremely Fast Approximate Nearest Neighbor Search Algorithm Based on kNN Graph

Approximate nearest neighbor (ANN) search is a fundamental problem in many areas of data mining, machine learning and computer vision. The performance of traditional hierarchical structure (tree) based methods decreases as the dimensionality of data grows, while hashing based methods usually lack efficiency in practice. Recently, the graph based methods have drawn considerable attention. The main idea is that a neighbor of a neighbor is also likely to be a neighbor, which we refer as NN-expansion. These methods construct a k-nearest neighbor (kNN) graph offline. And at online search stage, these methods find candidate neighbors of a query point in some way (\eg, random selection), and then check the neighbors of these candidate neighbors for closer ones iteratively. Despite some promising results, there are mainly two problems with these approaches: 1) These approaches tend to converge to local optima. 2) Constructing a kNN graph is time consuming. We find that these two problems can be nicely solved when we provide a good initialization for NN-expansion. In this paper, we propose EFANNA, an extremely fast approximate nearest neighbor search algorithm based on kNN Graph....

## Introduction

Nearest neighbor search plays an important role in many applications of data mining, machine learning and computer vision. When dealing with sparse data (*e.g*., document retrieval), one can use advanced index structures (*e.g*., inverted index) to solve this problem. However, for data with dense features, the cost for finding the exact nearest neighbor is $O{(N)}$, where $N$ is the number of points in the database. It's very time consuming when the data set is large. So people turn to Approximate Nearest neighbor (ANN) search in practice. Many work has been done to carry out the ANN search with high accuracy but low computational complexity.

There are mainly two types of methods in ANN search. The first type methods are hierarchical structure (tree) based methods, such as KD-tree,Randomized KD-tree, K-means tree. These methods perform very well when the dimension of the data is relatively low. However, the performance decreases dramatically as the dimension of the data increases. The second type methods are hashing based methods, such as Locality Sensitive Hashing (LSH), Spectral Hashing, Iterative Quantization and so on. Please see for a detailed survey on various hashing methods....

## Conclusion

The goal of this research is to provide a fast solution, EFANNA, for both ANN search and approximate $k$NN graph construction problems. On ANN search, we use hierarchical structures to provide better initialization for NN-expansion. And on graph construction, we use a divide-and-conquer way to construct an initial graph and refine it with NN-descent. Extensive experiments shows that EFANNA outperforms previous algorithms significantly both in approximate $k$NN graph construction and ANN search. Meanwhile, EFANNA also shows great flexibility for different scenarios.

### Results

### Online index updating

kGraph: kGraph is an open source library for approximate $k$NN graph construction and ANN search. The author of kGraph is the author of NN-descent. The approximate $k$NN graph algorithm implemented in kGraph library is exactly NN-descent. kGraph implements with OpenMP and SSE instruction for speed-up. For faire comparison, we disable the parallelism and SSE instruction.

Recently, graph based methods have drawn considerable attention. The essential idea behind these approaches is that *a neighbor of a neighbor is also likely to be a...
