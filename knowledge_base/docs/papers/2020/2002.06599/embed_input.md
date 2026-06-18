Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics

Informed sampling-based planning algorithms exploit problem knowledge for better search performance. This knowledge is often expressed as heuristic estimates of solution cost and used to order the search. The practical improvement of this informed search depends on the accuracy of the heuristic. Selecting an appropriate heuristic is difficult. Heuristics applicable to an entire problem domain are often simple to define and inexpensive to evaluate but may not be beneficial for a specific problem instance. Heuristics specific to a problem instance are often difficult to define or expensive to evaluate but can make the search itself trivial. This paper presents Adaptively Informed Trees (AIT*), an almost-surely asymptotically optimal sampling-based planner based on BIT*. AIT* adapts its search to each problem instance by using an asymmetric bidirectional search to simultaneously estimate and exploit a problem-specific heuristic. This allows it to quickly find initial solutions and converge towards the optimum. AIT* solves the tested problems as fast as RRT-Connect while also converging towards the optimum.

## Introduction

Path planning is the problem of finding a continuous sequence of valid states between a start and goal specification. Sampling-based planners, such as Probabilistic Roadmaps (PRM), approximate the state space by sampling discrete states and connecting them with edges. The resulting structure can then be processed by graph-search algorithms to find a sequence of states that connects the start to the goal.

Improving the accuracy of a heuristic directly improves the performance of informed search algorithms, and the search becomes trivial when a perfect heuristic is available.

Lazy sampling-based planners, such as Lazy PRM, reduce this computational cost by avoiding the evaluation of every edge. These algorithms first perform an inexpensive search on a simplified approximation without collision detection. This allows them to only evaluate the edges that are believed to be on an optimal path, and reduce the number of evaluated edges. This improves performance, especially for problems with computationally expensive edge evaluations, such as those considered in this paper.

This paper presents Adaptively Informed Trees (AIT\*), a lazy, almost-surely asymptotically optimal sampling-based planner that uses an asymmetric bidirectional search to simultaneously estimate and exploit an accurate, problem-specific heuristic. AIT\* estimates this heuristic by performing a lazy reverse search on the current sampling-based approximation. This heuristic is then used to order the forward search of this approximation while considering complete edge evaluations.

## Discussion & Future Work

AIT\* was designed for planning problems with expensive edge evaluations. These often occur when the search has to consider dynamic constraints (e.g., two-point boundary value problems) or complex robot and obstacle interactions (e.g., difficult collision detection) for each edge, as found on NASA/JPL-Caltech's Axel. In future work, Axel will consider tether-terrain interaction and physics-based stability checks based on the anchor history of the tether, which will further increase the edge evaluation cost.

These expensive edge evaluations were simulated in the abstract problems by increasing the collision detection resolution, providing a simple way to increase the edge evaluation cost and evaluate AIT\* on illustrative obstacle configurations.
