Finding Community Structure in Very Large Networks

Topics include Community detection, CNM algorithm, Fast greedy modularity, Modularity optimization, Hierarchical clustering, Agglomerative clustering, Large-scale graphs, Network science.

Introduces the CNM fast greedy algorithm, an agglomerative method that efficiently optimizes modularity and produces a community dendrogram. The paper was important because it moved modularity-based community detection toward networks with hundreds of thousands of nodes.

The discovery and analysis of community structure in networks is a topic of considerable recent interest within the physics community, but most methods proposed so far are unsuitable for very large networks because of their computational cost. Here we present a hierarchical agglomeration algorithm for detecting community structure which is faster than many competing algorithms: its running time on a network with n vertices and m edges is O(m d log n) where d is the depth of the dendrogram describing the community structure. Many real-world networks are sparse and hierarchical, with m ~ n and d ~ log n, in which case our algorithm runs in essentially linear time, O(n log^2 n). As an example of the application of this algorithm we use it to analyze a network of items for sale on the web-site of a large online retailer, items in the network being linked if they are frequently purchased by the same buyer. The network has more than 400,000 vertices and 2 million edges. We show that our algorithm can extract meaningful communities from this network, revealing large-scale patterns present in the purchasing habits of customers.

## Introduction

Many systems of current interest to the scientific community can usefully be represented as networks. Examples include the Internet and the world-wide web social networks, citation networks food webs, and biochemical networks;. Each of these networks consists of a set of nodes or vertices representing, for instance, computers or routers on the Internet or people in a social network, connected together by links or edges, representing data connections between computers, friendships between people, and so forth.

One network feature that has been emphasized in recent work is community structure, the gathering of vertices into groups such that there is a higher density of edges within groups than between them note. The problem of detecting such communities within networks has been well studied. Early approaches such as the Kernighan--Lin algorithm, spectral partitioning or hierarchical clustering work well for specific types of problems (particularly graph bisection or problems with well defined vertex similarity measures), but perform poorly in more general cases.

## Conclusions

We have described a new algorithm for inferring community structure from network topology which works by greedily optimizing the modularity. Our algorithm runs in time $O{({md{\log n}})}$ for a network with $n$ vertices and $m$ edges where $d$ is the depth of the dendrogram. For networks that are hierarchical, in the sense that there are communities at many scales and the dendrogram is roughly balanced, we have $d \sim {\log n}$. If the network is also sparse, $m \sim n$, then the running time is essentially linear, $O{({n{\log^{2}n}})}$....

Calculate the initial values of $\DeltaQ_{ij}$ and $a_{i}$ according to and, and populate the max-heap with the largest element of each row of the matrix $\DeltaQ$.

The operation of the algorithm involves finding the changes in $Q$ that would result from the amalgamation of each pair of communities, choosing the largest of them, and performing the corresponding amalgamation. One way to envisage (and implement) this process is to think of network as a multigraph, in which a whole community is represented by a vertex, bundles of edges connect one vertex to another, and edges internal to communities are represented by self-edges....

## Amazon.com purchasing network
