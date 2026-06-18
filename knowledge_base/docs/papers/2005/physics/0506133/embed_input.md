Uncovering the Overlapping Community Structure of Complex Networks in Nature and Society

Topics include Community detection, Clique percolation, Overlapping communities, Complex networks, Social networks, Biological networks, Network science, Graph clustering.

Introduces the clique percolation method for detecting overlapping communities, treating communities as chains of adjacent cliques rather than disjoint partitions. The paper is a landmark for networks where nodes naturally participate in multiple groups, such as collaboration and protein interaction networks.

Many complex systems in nature and society can be described in terms of networks capturing the intricate web of connections among the units they are made of. A key question is how to interpret the global organization of such networks as the coexistence of their structural subunits (communities) associated with more highly interconnected parts. Identifying these a priori unknown building blocks (such as functionally related proteins, industrial sectors and groups of people) is crucial to the understanding of the structural and functional properties of networks. The existing deterministic methods used for large networks find separated communities, whereas most of the actual networks are made of highly overlapping cohesive groups of nodes. Here we introduce an approach to analysing the main statistical features of the interwoven sets of overlapping communities that makes a step towards uncovering the modular structure of complex systems. After defining a set of new characteristic quantities for the statistics of communities, we apply an efficient technique for exploring overlapping communities on a large scale....

## Paper Body

Uncovering the overlapping\
community structure of complex\
networks in nature and society

Gergely Palla^†‡^, Imre Derényi^‡^, Illés Farkas^†^, and Tamás Vicsek^†‡^

The specific scaling of the community degree distribution is a novel signature of the hierarchical nature of the systems we study. We find that if we consider the network of communities instead of the nodes themselves, we still observe a degree distribution with a fat tail, but a characteristic scale appears, below which the distribution is exponential. This is consistent with our understanding of a complex system having different levels of organisation with units specific to each level....

With recent technological advances, huge sets of data are accumulating at a tremendous pace in various fields of human activity (including telecommunication, the internet, stock markets) and in many areas of life and social sciences (biomolecular assays, genetic maps, groups of web users, etc.). Understanding both the universal and specific features of the networks associated with these data has become an actual and important task. The knowledge of the community structure enables the prediction of some essential features of the systems under investigation....

When we are interested in the community structure around a particular node, it is advisable to scan through some ranges of $k$ and $w^{\ast}$, and monitor how its communities change. As an illustration, in Fig. 2 we are depicting the communities of three selected nodes of three large networks: (i) the social network of scientific collaborators, (ii) the network of word associations related to cognitive sciences, and (iii) the molecular-biological network of protein-protein interactions. These pictures can serve as tests or validations of the efficiency of our algorithm. In particular, the communities of the author G....

In general, each node $i$ of a network can be characterised by a *membership number* $m_{i}$, which is the number of communities the node belongs to. In turn, any two communities $\alpha$ and $\beta$ can share $s_{\alpha,\beta}^{ov}$ nodes, which we define as the *overlap size* between these communities. Naturally, the communities also constitute a *network* with the overlaps being their links. The number of such links of community $\alpha$ can be called as its *community degree*, $d_{\alpha}^{com}$....
