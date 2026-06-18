Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)

Topics include Motion planning, Sampling-based planning, High-dimensional planning, Anytime planning, Asymptotic optimality, FCIT*, BIT*, Single-instruction multiple-data, Hardware acceleration.

Use SIMD instructions to evaluate edge costs to every neighbor (hence eliminating expensive nearest neighbor routine) in Informed RRT*. Gives huge empirical computational end-to-end planning time.

Improving the performance of motion planning algorithms for high-degree-of-freedom robots usually requires reducing the cost or frequency of computationally expensive operations. Traditionally, and especially for asymptotically optimal sampling-based motion planners, the most expensive operations are local motion validation and querying the nearest neighbours of a configuration. Recent advances have significantly reduced the cost of motion validation by using single instruction/multiple data (SIMD) parallelism to improve solution times for satisficing motion planning problems. These advances have not yet been applied to asymptotically optimal motion planning. This paper presents Fully Connected Informed Trees (FCIT*), the first fully connected, informed, anytime almost-surely asymptotically optimal (ASAO) algorithm. FCIT* exploits the radically reduced cost of edge evaluation via SIMD parallelism to build and search fully connected graphs.

## Introduction

Planning low-cost motions for high- degree-of-freedom (DoF) robots quickly is a fundamental area of research in robotics. These high-DoF robots are described by a continuous *configuration space*, but motion planning requires both a discrete approximation of this space and the ability to efficiently search this approximation. Graph-based planners, such as Dijkstra's algorithm and A\*, require the configuration space (i.e., search space) to be discretized a priori, and both their planning time and the quality of their solution depends on the resolution of this discretization.

Sampling-based motion planners, such as Probabilistic Roadmaps (PRM), Rapidly-exploring Random Trees (RRT), and RRT-Connect, avoid this a priori discretization by incrementally sampling the search space which constructs a random geometric graph (RGG) online as a discrete approximation of this search space. Anytime ASAO sampling-based motion planners, such as RRT\* and Batch Informed Trees (BIT\*), extend sampling-based motion planning by continually improving their sampled approximations even after finding an initial solution in order to converge probabilistically towards an optimal solution.

The original VAMP work did not address ASAO motion planning. This paper shows that its radically decreased edge evaluation cost can also guide algorithmic advances on this class of problems. Specifically, we revisit the assumptions that edge evaluations are computationally expensive, and consequently that fully connected graphs are prohibitively expensive to search because of their high branching factor and the resulting large number of edges to evaluate.

## Discussion

FCIT\* revisits fundamental assumptions about ASAO planning in light of the computationally inexpensive local motion validation introduced by VAMP. Planners traditionally seek to reduce the number of edges in their approximation by setting connectivity near a theoretical lower bound. This requires maintaining a computationally expensive nearest-neighbours structure. Moreover, this limits the connectivity of the resulting graph, preventing solutions from being found without additional sampling. FCIT\* is able to avoid this lower bound because of the reduced cost of edge evaluation, instead searching a fully connected approximation.
