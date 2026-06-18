<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LQR-Trees: Feedback Motion Planning via Sums-of-Squares Verification

Topics include Linear quadratic regulator trees, Feedback motion planning, Sum-of-squares optimization, Lyapunov functions, Regions of attraction, Nonlinear control, Trajectory stabilization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces LQR-trees as a feedback motion-planning method that stitches locally stabilized trajectories together using verified regions of attraction. The important step is coupling sampling-based tree expansion with SOS/Lyapunov certificates, so the resulting policy probabilistically covers the controllable portion of the state space rather than merely producing an open-loop path.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Advances in the direct computation of Lyapunov functions using convex optimization make it possible to efficiently evaluate regions of attraction for smooth non-linear systems. Here we present a feedback motion-planning algorithm which uses rigorously computed stability regions to build a sparse tree of LQR-stabilized trajectories. The region of attraction of this non-linear feedback policy “probabilistically covers” the entire controllable subset of state space, verifying that all initial conditions that are capable of reaching the goal will reach the goal. We numerically investigate the properties of this systematic non-linear feedback design algorithm on simple non-linear systems, prove the property of probabilistic coverage, and discuss extensions and implementation details of the basic algorithm.
