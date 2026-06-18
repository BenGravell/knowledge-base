<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Constrained Linear Quadratic Regulation

Topics include Linear quadratic regulation, Constrained optimization, Model predictive control, Stability, Optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates constrained LQR as a finite-horizon QP, establishes closed-loop stability under receding-horizon implementation, and characterizes the relationship between the constrained optimal cost and unconstrained LQR performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The paper is a contribution to the theory of the infinite-horizon linear quadratic regulator (LQR) problem subject to inequality constraints on the inputs and states, extending an approach first proposed by Sznaier and Damborg. A solution algorithm is presented, which requires solving a finite number of finite-dimensional positive definite quadratic programs. The constrained LQR outlined does not feature the undesirable mismatch between open-loop and closed-loop nominal system trajectories, which is present in the other popular forms of model predictive control (MPC) that can be implemented with a finite quadratic programming algorithm. The constrained LQR is shown to be both optimal and stabilizing. The solution algorithm is guaranteed to terminate in finite time with a computational cost that has a reasonable upper bound compared to the minimal cost for computing the optimal solution. Inherent to the approach is the removal of a tuning parameter, the control horizon, which is present in other MPC approaches and for which no reliable tuning guidelines are available. Two examples are presented that compare constrained LQR and two other popular forms of MPC.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The examples demonstrate that constrained LQR achieves significantly better performance than the other forms of MPC on some plants, and the computational cost is not prohibitive for online implementation.
