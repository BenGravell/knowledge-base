<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Constrained Global Path Optimization for Articulated Steering Vehicles

Topics include Path planning, Articulated vehicles, Bezier curves, Motion primitives, A* search, Gradient optimization, Nonlinear programming.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Plans paths for articulated steering vehicles by pre-computing quintic Bezier motion primitives offline, then searching over them with A*, with online gradient-based smoothing. Combines the tractability of A* over discrete motion primitives with the geometric smoothness of Bezier curves for non-holonomic articulated vehicles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper proposes a new efficient path-planning algorithm for articulated steering vehicles operating in semi-structured environments, in which obstacles are detected online by the vehicle's sensors. The first step of the algorithm is offline and computes a finite set of feasible motions that connect discrete robot states to construct a search space. The motion primitives are parameterized using Bezier curves and optimized as a nonlinear programming problem (NLP) equivalent to the constrained path planning problem. Applying the A* search algorithm to the search space produces the shortest paths as a sequence of these primitives. Online path smoothing, which uses a gradient-based method, is applied to solve another NLP.
