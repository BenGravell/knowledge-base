Near Linear Time Algorithm to Detect Community Structures in Large-Scale Networks

Topics include Community detection, Label propagation, Near-linear algorithms, Large-scale graphs, Graph clustering, Network science, Social networks, Biological networks.

Introduces label propagation, a simple iterative method where nodes adopt the most common label among their neighbors until labels stabilize into communities. Its importance is practical: it avoids an explicit objective function and brought community detection close to linear time for large networks.

Community detection and analysis is an important methodology for understanding the organization of various real-world networks and has applications in problems as diverse as consensus formation in social communities or the identification of functional modules in biochemical networks. Currently used algorithms that identify the community structures in large-scale real-world networks require a priori information such as the number and sizes of communities or are computationally expensive. In this paper we investigate a simple label propagation algorithm that uses the network structure alone as its guide and requires neither optimization of a pre-defined objective function nor prior information about the communities. In our algorithm every node is initialized with a unique label and at every step each node adopts the label that most of its neighbors currently have. In this iterative process densely connected groups of nodes form a consensus on a unique label to form communities. We validate the algorithm by applying it to networks whose community structures are known....

## Introduction

A wide variety of complex systems can be represented as networks. For example, the World Wide Web is a network of webpages interconnected by hyperlinks; social networks are represented by people as nodes and their relationships by edges; and biological networks are usually represented by bio-chemical molecules as nodes and the reactions between them by edges. Most of the research in the recent past focused on understanding the evolution and organization of such networks and the effect of network topology on the dynamics and behaviors of the system Albert and Barabási; Albert et al.; Barabási and Albert; Newman....

A community in a network is a group of nodes that are similar to each other and dissimilar from the rest of the network. It is usually thought of as a group where nodes are densely inter-connected and sparsely connected to other parts of the network Girvan and Newman; Newman; Wasserman and Faust. There is no universally accepted definition for a community, but it is well known that most real-world networks display community structures....

Figure 9: The cumulative probability distributions of community sizes (s) are shown for the WWW, co-authorship and actor collaboration networks. They approximately follow power-laws with the exponents as shown.

In the hierarchical agglomerative algorithm of Clauset et al Clauset et al., the partition that corresponds to the maximum $Q$ is taken to be the most indicative of the community structure in the network. Other partitions with high $Q$ values will have a structure similar to that of the maximum $Q$ partition, as these solutions are obtained by progressively aggregating two groups at a time. Our proposed label propagation algorithm on the other hand finds multiple significantly modular solutions that have some amount of dissimilarity....

Arrange the nodes in the network in a random order and set it to $X$.

Since many real-world complex networks are large in size, time efficiency of the community detection algorithm is an important consideration. When no *a priori* information is available about the likely communities in a given network, finding partitions that optimize a chosen measure of community strength is normally used....
