Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques

Path planning is an active area of research essential for many applications in robotics. Popular techniques include graph-based searches and sampling-based planners. These approaches are powerful but have limitations. This paper continues work to combine their strengths and mitigate their limitations using a unified planning paradigm. It does this by viewing the path planning problem as the two subproblems of search and approximation and using advanced graph-search techniques on a sampling-based approximation. This perspective leads to Advanced BIT*. ABIT* combines truncated anytime graph-based searches, such as ATD*, with anytime almost-surely asymptotically optimal sampling-based planners, such as RRT*. This allows it to quickly find initial solutions and then converge towards the optimum in an anytime manner. ABIT* outperforms existing single-query, sampling-based planners on the tested problems in R^ and R^, and was demonstrated on real-world problems with NASA/JPL-Caltech.

## Introduction

Popular path planning algorithms in robotics include graph-based searches, such as A^∗^ and Dijkstra's, and sampling-based planners, such as Rapidly-exploring Random Trees (RRT) and Probabilistic Roadmaps (PRM). Both graph- and sampling-based approaches have characteristic strengths and limitations. Previous work has separated search and approximation in single-query, almost-surely asymptotically optimal sampling-based planning to combine their strengths and mitigate their limitations. This separation can be leveraged to use advanced graph-based search techniques on an anytime sampling-based approximation to further improve performance.

An important strength of graph-based approaches is their strong theoretical guarantees. A\* is *resolution-optimal* (and *resolution-complete*) as well as *optimally efficient*. Any other algorithm guaranteed to find the optimal solution must expand at least as many vertices as A\*, given the same problem information. This efficiency is achieved by always expanding the state with the highest potential solution quality but requires an ordering of the search that does not provide any solutions until the optimum is found.

ABIT\* also shows the benefits of using advanced graph-search techniques in sampling-based planning on real-world path planning problems posed by Axel, a NASA/JPL-Caltech rover specialized for navigation on challenging terrain.

Information on the OMPL implementation of ABIT\* is available at

After adding an edge, the child state is expanded unless it has already been expanded during the current search, in which case it is added to the set of inconsistent vertices (lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")--1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")).

Fully exploiting every RGG approximation by finding the resolution-optimal path is computationally expensive. ABIT\* avoids this by truncating its search as soon as it can guarantee that it has found a solution whose cost is within a factor of the resolution-optimal cost. This allows ABIT\* to balance the exploitation of its approximation (i.e., repairing the search) with the exploration of the state space (i.e., increasing the density of the approximation).
