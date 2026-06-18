Community Structure in Social and Biological Networks

Topics include Community detection, Girvan-Newman algorithm, Edge betweenness, Divisive clustering, Social networks, Biological networks, Network science, Graph clustering, Hierarchical clustering.

Introduces a divisive community detection method based on repeatedly removing edges with high edge betweenness. The paper helped make community structure a central network science problem and established a benchmark algorithm for finding boundaries between densely connected groups.

A number of recent studies have focused on the statistical properties of networked systems such as social networks and the World-Wide Web. Researchers have concentrated particularly on a few properties which seem to be common to many networks: the small-world property, power-law degree distributions, and network transitivity. In this paper, we highlight another property which is found in many networks, the property of community structure, in which network nodes are joined together in tightly-knit groups between which there are only looser connections. We propose a new method for detecting such communities, built around the idea of using centrality indices to find community boundaries. We test our method on computer generated and real-world graphs whose community structure is already known, and find that it detects this known structure with high sensitivity and reliability. We also apply the method to two networks whose community structure is not well-known - a collaboration network and a food web - and find that it detects significant and informative community divisions in both cases.

## Introduction

Many systems take the form of networks, sets of nodes or vertices joined together in pairs by links or edges. Examples include social networks such as acquaintance networks and collaboration networks, technological networks such as the Internet, the World-Wide Web and power grids and biological networks such as neural networks, food webs, and metabolic networks;. Recent research on networks among mathematicians and physicists has focused on a number of distinctive statistical properties that most networks seem to share....

A third property that many networks have in common is clustering, or network transitivity, which is the property that two vertices that are both neighbors of the same third vertex have a heightened probability of also being neighbors of one another. In the language of social networks, two of your friends will have a greater probability of knowing one another than will two people chosen at random from the population, on account of their common acquaintance with you. This effect is quantified by the clustering coefficient $C$ defined by

A number of extensions or improvements of our method may be possible. First, we hope to generalize the method to handle both weighted and directed graphs. Second, we hope that it may be possible to improve the speed of the algorithm. At present, the algorithm runs in time $O{(n^{3})}$ on sparse graphs, where $n$ is the number of vertices in the network. This makes it impractical for very large graphs. Detecting communities in, for instance, the large collaboration networks or subsets of the Web graph that have been studied recently, would be entirely unfeasible....

We hope that the ideas and methods presented here will prove useful in the analysis of many other types of networks. Possible further applications range from the determination of functional clusters within neural networks to analysis of communities on the World-Wide Web, as well as others not yet thought of. We hope to see such applications in the future.

In this section we present a number of tests of our algorithm on computer-generated graphs and on real-world networks for which the community structure is already known. In each case we find that our algorithm reliably detects the known structure.

Vertex "betweenness" has been studied in the past as a measure of the centrality and influence of nodes in networks....
