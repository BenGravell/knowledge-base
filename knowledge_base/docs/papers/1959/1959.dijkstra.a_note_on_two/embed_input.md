<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Note on Two Problems in Connexion with Graphs

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Dijkstra's 1959 note presents two foundational graph algorithms: a greedy method for finding a minimum spanning tree and, more famously, the shortest-path algorithm now called Dijkstra's algorithm. Its most consequential impact was showing that core network optimization problems could be solved by simple, efficient label-setting/greedy procedures, shaping algorithms for routing, transportation, operations research, compilers, robotics, and countless later graph-search methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider n points (nodes), some or all pairs of which are connected by a branch; the length of each branch is given. We restrict ourselves to the case where at least one path exists between any two nodes. We now consider two problems. Problem 1. Construct the tree of minimum total length between the n nodes. (A tree is a graph with one and only one path between every two nodes.) Problem 2. Find the path of minimum total length between two given nodes P and Q. We use the fact that, if R is a node on the minimal path from P to Q, knowledge of the latter implies the knowledge of the minimal path from P to R. In the solution presented, the minimal paths from P to the other nodes are constructed in order of increasing length until Q is reached.
