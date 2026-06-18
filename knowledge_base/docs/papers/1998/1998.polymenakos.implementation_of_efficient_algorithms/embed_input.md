<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Implementation of Efficient Algorithms for Globally Optimal Trajectories

Topics include Shortest path, Trajectory optimization, Optimal control, Label-correcting methods, Dynamic programming, Continuous-space planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Implements label-correcting methods for discretized continuous-space shortest-path problems arising in globally optimal trajectory computation. The paper builds on Tsitsiklis-style Dijkstra methods and shows that small-label-first variants can terminate finitely while outperforming Jacobi, Gauss-Seidel, and Dijkstra-like baselines in practice.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider a continuous space shortest path problem in a two-dimensional plane. This is the problem of finding a trajectory that starts at a given point, ends at the boundary of a compact set of /spl Rfr//sup 2/, and minimizes a cost function of the form /spl int//sub O//sup T/ r(x(t)) dt+q(x(T)). For a discretized version of this problem, a Dijkstra-like method that requires one iteration per discretization point has been developed by Tsitsiklis. Here we develop some new label correcting-like methods based on the small label first methods of Bertsekas and Bertsekas et al.. We prove the finite termination of these methods, and present computational results showing that they are competitive and often superior to the Dijkstra-like method and are also much faster than the traditional Jacobi and Gauss-Seidel methods.
