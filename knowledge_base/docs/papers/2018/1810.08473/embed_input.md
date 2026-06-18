From Louvain to Leiden: Guaranteeing Well-connected Communities

Topics include Benchmarks, Leiden, Community structure.

Community detection is often used to understand the structure of large and complex networks. One of the most popular algorithms for uncovering community structure is the so-called Louvain algorithm. We show that this algorithm has a major defect that largely went unnoticed until now: the Louvain algorithm may yield arbitrarily badly connected communities. In the worst case, communities may even be disconnected, especially when running the algorithm iteratively. In our experimental analysis, we observe that up to 25% of the communities are badly connected and up to 16% are disconnected. To address this problem, we introduce the Leiden algorithm. We prove that the Leiden algorithm yields communities that are guaranteed to be connected. In addition, we prove that, when the Leiden algorithm is applied iteratively, it converges to a partition in which all subsets of all communities are locally optimally assigned. Furthermore, by relying on a fast local move approach, the Leiden algorithm runs faster than the Louvain algorithm. We demonstrate the performance of the Leiden algorithm for several benchmark and real-world networks.

## Introduction

In many complex networks, nodes cluster and form relatively dense groups---often called communities Fortunato; Porter *et al.*. Such a modular structure is usually not known beforehand. Detecting communities in a network is therefore an important problem. One of the best-known methods for community detection is called modularity Newman and Girvan. This method tries to maximise the difference between the actual number of edges in a community and the expected number of such edges. We denote by $e_{c}$ the actual number of edges in community $c$.

where $\gamma > 0$ is a resolution parameter Reichardt and Bornholdt. Higher resolutions lead to more communities, while lower resolutions lead to fewer communities.

In this paper, we show that the Louvain algorithm has a major problem, for both modularity and CPM. The algorithm may yield arbitrarily badly connected communities, over and above the well-known issue of the resolution limit Fortunato and Barthélemy (Section II.1). Communities may even be internally disconnected. To address this important shortcoming, we introduce a new algorithm that is faster, finds better partitions and provides explicit guarantees and bounds (Section III).

## Discussion

Community detection is an important task in the analysis of complex networks. Finding communities in large networks is far from trivial: algorithms need to be fast, but they also need to provide high-quality results. One of the most widely used algorithms is the Louvain algorithm Blondel *et al.*, which is reported to be among the fastest and best performing community detection algorithms Lancichinetti and Fortunato; Yang *et al.*. However, as shown in this paper, the Louvain algorithm has a major shortcoming: the algorithm yields communities that may be arbitrarily badly connected. Communities may even be disconnected.

To overcome the problem of arbitrarily badly connected communities, we introduced a new algorithm, which we refer to as the Leiden algorithm. This algorithm provides a number of explicit guarantees. In particular, it yields communities that are guaranteed to be connected. Moreover, when the algorithm is applied iteratively, it converges to a partition in which all subsets of all communities are guaranteed to be locally optimally assigned.
