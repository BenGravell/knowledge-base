<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CCosmo: A Conic First-Order Solver

Topics include Conic optimization, Convex optimization, Alternating-direction method of multipliers, First-order methods, Operator splitting, Quadratic programming, Second-order cone programming, Warm-starting, Model predictive control, Graphs of convex sets.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces an ADMM-based conic solver family implemented in C++ with Python bindings, configurable precision, and sparse or dense linear algebra. Benchmarks compare its QP and SOCP performance with existing solvers, demonstrate effective MPC warm starts, and show advantages of avoiding an extra homogeneous embedding for graph-of-convex-sets relaxations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In robotics, convex optimization solvers frequently appear inside larger loops that repeatedly solve closely related problems and only require moderate accuracy. This operating regime favors first-order methods that are easily warm started and have predictable memory requirements. We present CCosmo, a family of general-purpose conic optimization solvers based on the alternating direction method of multipliers. CCosmo is written in C++ with a Python interface. It supports both single- and double-precision arithmetic and can dispatch to either sparse or dense linear algebra backends. It implements the same base algorithm as COSMO.jl for conic programs and reduces to OSQP when solving a QP. We evaluate CCosmo on standard QP and SOCP benchmarks and find that CCosmo is broadly competitive with the open-source baselines on every family. On a synthetic MPC benchmark, CCosmo gives the fastest warm-starting performance, beating out SCS, another popular first-order solver, and Clarabel, an interior point solver. Finally, on a benchmark of Graph of Convex Sets relaxations, we show the benefit of avoiding SCS's homogeneous embedding when the original problem is already homogeneous.
