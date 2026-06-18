Fast Unfolding of Communities in Large Networks

Topics include Community detection, Louvain method, Modularity optimization, Graph clustering, Network science, Complex networks, Hierarchical clustering, Large-scale graphs, Heuristic optimization, Web graph.

This paper introduces the Louvain method, a fast greedy heuristic for community detection that alternates local modularity-improving node moves with aggregation of discovered communities into a coarser network. Its key contribution is making modularity-based community detection practical on very large graphs while naturally producing a hierarchy of communities across successive aggregation levels.

We propose a simple method to extract the community structure of large networks. Our method is a heuristic method that is based on modularity optimization. It is shown to outperform all other known community detection method in terms of computation time. Moreover, the quality of the communities detected is very good, as measured by the so-called modularity. This is shown first by identifying language communities in a Belgian mobile phone network of 2.6 million customers and by analyzing a web graph of 118 million nodes and more than one billion links. The accuracy of our algorithm is also verified on ad-hoc modular networks..

## Introduction

Social, technological and information systems can often be described in terms of complex networks that have a topology of interconnected nodes combining organization and randomness. The typical size of large networks such as social network services, mobile phone networks or the web now counts in millions when not billions of nodes and these scales demand new methods to retrieve comprehensive information from their structure. A promising approach consists in decomposing the networks into sub-units or communities, which are sets of highly inter-connected nodes.

The problem of community detection requires the partition of a network into communities of densely connected nodes, with the nodes belonging to different communities being only sparsely connected. Precise formulations of this optimization problem are known to be computationally intractable. Several algorithms have therefore been proposed to find reasonably good partitions in a reasonably fast way. This search for fast algorithms has attracted much interest in recent years due to the increasing availability of large network data sets and the impact of networks on every day life.

## Conclusion and discussion

We have introduced an algorithm for optimizing modularity that allows to study networks of unprecedented size. The limitation of the method for the experiments that we performed was the storage of the network in main memory rather than the computation time. This change of scales, i.e., from around 5 millions nodes for previous methods to more than 100 millions nodes in our case, opens exciting perspectives as the modular structure of complex systems such as whole countries or huge parts of the Internet can now be unraveled.

By construction, our algorithm unfolds a complete hierarchical community structure for the network, each level of the hierarchy being given by the intermediate partitions found at each pass. In this paper, however, we have only verified the accuracy of the top level of this hierarchy, namely the final partition found by our algorithm, and the accuracy of the intermediate partitions has still to be shown. Several points suggest, however, that these intermediate partitions make sense.
