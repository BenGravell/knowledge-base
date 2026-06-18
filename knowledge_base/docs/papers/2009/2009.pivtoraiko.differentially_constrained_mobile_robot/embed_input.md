<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Differentially Constrained Mobile Robot Motion Planning in State Lattices

Topics include Motion planning, Lattice methods, Graph search, State space search, Differential constraints, Mobile robots, Autonomous navigation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents state lattices as a deterministic search representation whose edges are feasible motion primitives for a differentially constrained robot. The key contribution is making graph search respect vehicle mobility constraints while retaining efficient cost evaluation and real-time planning behavior.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an approach to the problem of differentially constrained mobile robot motion planning in arbitrary cost fields. The approach is based on deterministic search in a specially discretized state space. We compute a set of elementary motions that connects each discrete state value to a set of its reachable neighbors via feasible motions. Thus, this set of motions induces a connected search graph. The motions are carefully designed to terminate at discrete states, whose dimensions include relevant state variables (e.g., position, heading, curvature, and velocity). The discrete states, and thus the motions, repeat at regular intervals, forming a lattice. We ensure that all paths in the graph encode feasible motions via the imposition of continuity constraints on state variables at graph vertices and compliance of the graph edges with a differential equation comprising the vehicle model. The resulting state lattice permits fast full configuration space cost evaluation and collision detection. Experimental results with research prototype rovers demonstrate that the planner allows us to exploit the entire envelope of vehicle maneuverability in rough terrain, while featuring real-time performance.
