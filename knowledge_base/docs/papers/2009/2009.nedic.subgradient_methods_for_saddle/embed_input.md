<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Subgradient Methods for Saddle-Point Problems

Topics include Saddle-point problems, Subgradient methods, Convex optimization, Primal-dual methods, Nonsmooth optimization, Convergence analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes subgradient methods for convex-concave saddle-point problems, including convergence properties relevant to primal-dual optimization. The paper provides a foundational nonsmooth optimization reference for later first-order min-max algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study subgradient methods for computing the saddle points of a convex-concave function. Our motivation comes from networking applications where dual and primal-dual subgradient methods have attracted much attention in the design of decentralized network protocols. We first present a subgradient algorithm for generating approximate saddle points and provide per-iteration convergence rate estimates on the constructed solutions. We then focus on Lagrangian duality, where we consider a convex primal optimization problem and its Lagrangian dual problem, and generate approximate primal-dual optimal solutions as approximate saddle points of the Lagrangian function. We present a variation of our subgradient method under the Slater constraint qualification and provide stronger estimates on the convergence rate of the generated primal sequences. In particular, we provide bounds on the amount of feasibility violation and on the primal objective function values at the approximate solutions. Our algorithm is particularly well-suited for problems where the subgradient of the dual function cannot be evaluated easily (equivalently, the minimum of the Lagrangian function at a dual solution cannot be computed efficiently), thus impeding the use of dual subgradient methods.
