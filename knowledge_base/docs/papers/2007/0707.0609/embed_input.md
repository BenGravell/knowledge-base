Maps of Random Walks on Complex Networks Reveal Community Structure

Topics include Community detection, Infomap, Map equation, Random walk, Information theory, Flow-based clustering, Directed networks, Weighted networks, Network science.

Introduces the map equation and Infomap, framing community detection as compression of random-walk flows on a network. This shifted part of the field from purely density- or modularity-based partitions toward flow-based communities, especially useful for directed and weighted networks.

To comprehend the multipartite organization of large-scale biological and social systems, we introduce a new information theoretic approach that reveals community structure in weighted and directed networks. The method decomposes a network into modules by optimally compressing a description of information flows on the network. The result is a map that both simplifies and highlights the regularities in the structure and their relationships. We illustrate the method by making a map of scientific communication as captured in the citation patterns of more than 6000 journals. We discover a multicentric organization with fields that vary dramatically in size and degree of integration into the network of science. Along the backbone of the network - including physics, chemistry, molecular biology, and medicine - information flows bidirectionally, but the map reveals a directional pattern of citation from the applied fields to the basic sciences.

## Abstract

To comprehend the multipartite organization of large-scale biological and social systems, we introduce a new information theoretic approach that reveals community structure in weighted and directed networks. The method decomposes a network into modules by optimally compressing a description of information flows on the network. The result is a map that both simplifies and highlights the regularities in the structure and their relationships. We illustrate the method by making a map of scientific communication as captured in the citation patterns of more than 6000 journals....

complex networks \| clustering \| information theory \| compression

When a cartographer designs a map, the scale or scope of the map influences the choice of which objects are represented. A regional map omits many of the details that appear on a city map. Similarly, in the approach that we have developed here, the appropriate size or resolution of the modules depends on the universe of nodes that are included in the network. If we compare the map of a network to a map of a subset of the same network, we would expect to see the map of the subset to reveal finer divisions, with modules composed of fewer nodes....

The additional level of detail in the more narrowly focused map would have been clutter on the full map of science. When we design maps to help us comprehend the world, we must find that balance where we eliminate extraneous detail but highlight the relationships among important structures. Here we have shown how to formalize this cartographer's precept using the mathematical apparatus of information theory.

For all but the smallest networks, it is infeasible to check all possible partitions to find the one that minimizes the description length in the map equation (Eq. 1). Instead we use computational search. We first compute the fraction of time each node is visited by a random walker using the power method, and using these visit frequencies we explore the space of possible partitions using a deterministic greedy search algorithm. We refine the results with a simulated annealing approach using the heat-bath algorithm (see supporting online material for more details).

### Huffman coding

The two equations and reflect two different senses of what it means to have a network. The former, which we pursue here, finds the essence of a network in the patterns of...
