Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics

Informed sampling-based planning algorithms exploit problem knowledge for better search performance. This knowledge is often expressed as heuristic estimates of solution cost and used to order the search. The practical improvement of this informed search depends on the accuracy of the heuristic. Selecting an appropriate heuristic is difficult. Heuristics applicable to an entire problem domain are often simple to define and inexpensive to evaluate but may not be beneficial for a specific problem instance. Heuristics specific to a problem instance are often difficult to define or expensive to evaluate but can make the search itself trivial. This paper presents Adaptively Informed Trees (AIT*), an almost-surely asymptotically optimal sampling-based planner based on BIT*. AIT* adapts its search to each problem instance by using an asymmetric bidirectional search to simultaneously estimate and exploit a problem-specific heuristic. This allows it to quickly find initial solutions and converge towards the optimum. AIT* solves the tested problems as fast as RRT-Connect while also converging towards the optimum.

## Introduction

Path planning is the problem of finding a continuous sequence of valid states between a start and goal specification. Sampling-based planners, such as Probabilistic Roadmaps (PRM), approximate the state space by sampling discrete states and connecting them with edges. The resulting structure can then be processed by graph-search algorithms to find a sequence of states that connects the start to the goal.

Informed graph-search algorithms, such as A\*, use knowledge about a problem domain to increase their efficiency. This knowledge is often captured in the form of a *heuristic function*, $\hat{h}$, which estimates cost-to-go, i.e., the cost to go from any state in the state space to the goal.

This approach is promising for path planning problems with expensive edge evaluations, such as those posed by NASA/JPL-Caltech's Axel. AIT\* outperforms existing sampling-based algorithms on the tested abstract problems by finding an initial solution quickly and converging to the optimum in an anytime manner. These problems show the robustness of AIT\* with respect to expensive edge evaluations and encourage more thorough evaluations of states which could be used in more advanced optimization objectives.

Information on the OMPL implementation of AIT\* is available at

### III-B Approximation

Lazy Shortest Path (LazySP) is a class of algorithms that reduces the number of edges checked for collisions. It first finds a path from the start to the goal using an inexpensive estimate of the edge costs. Once a path is found, it uses an edge selector function which determines the order in which these edges are checked for collision. An example of a LazySP algorithm is Lazy Receding Horizon A\* (LRHA\*).

2 xp ← arg min xi ∈ neighbors (x){ĥexp [xi]+ĉ (xi,x)}
6 $\mathcal{Q}_{R}\overset{+}{\leftarrow}\mathbf{x}$
9 $\mathcal{Q}_{R}\overset{-}{\leftarrow}\mathbf{x}$
Algorithm 6 update_state (x)

The properties of this heuristic directly affect the performance of the search algorithms. An *admissible* heuristic never overestimates the actual cost-to-go. A *consistent* heuristic satisfies a triangle-inequality, such that for any two states, $\mathbf{x}_{i},\mathbf{x}_{j}$, it satisfies ${\hat{h}\left( \mathbf{x}_{i} \right)} \leq {{p{(\mathbf{x}_{i},\mathbf{x}_{j})}} + {\hat{h}\left( \mathbf{x}_{j} \right)}}$, where $p{(\mathbf{x}_{i},\mathbf{x}_{j})}$ is the...
