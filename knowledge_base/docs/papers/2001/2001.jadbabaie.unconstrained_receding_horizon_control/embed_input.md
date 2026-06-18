<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Unconstrained Receding-horizon Control of Nonlinear Systems

Topics include Model predictive control, Receding horizon control, Control Lyapunov functions, Nonlinear systems, Terminal cost, Stability analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows how unconstrained finite-horizon optimal control can stabilize nonlinear systems when a control Lyapunov function approximates the infinite-horizon tail cost. The paper removes terminal constraints from the receding-horizon formulation while preserving stability guarantees through an improvement property and horizon-dependent region-of-operation analysis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It is well known that unconstrained infinite-horizon optimal control may be used to construct a stabilizing controller for a nonlinear system. We show that similar stabilization results may be achieved using unconstrained finite horizon optimal control. The key idea is to approximate the tail of the infinite horizon cost-to-go using, as terminal cost, an appropriate control Lyapunov function. Roughly speaking, the terminal control Lyapunov function (CLF) should provide an (incremental) upper bound on the cost. In this fashion, important stability characteristics may be retained without the use of terminal constraints such as those employed by a number of other researchers. The absence of constraints allows a significant speedup in computation. Furthermore, it is shown that in order to guarantee stability, it suffices to satisfy an improvement property, thereby relaxing the requirement that truly optimal trajectories be found. We provide a complete analysis of the stability and region of attraction/operation properties of receding horizon control strategies that utilize finite horizon approximations in the proposed class.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It is shown that the guaranteed region of operation contains that of the CLF controller and may be made as large as desired by increasing the optimization horizon (restricted, of course, to the infinite horizon domain). Moreover, it is easily seen that both CLF and infinite-horizon optimal control approaches are limiting cases of our receding horizon strategy. The key results are illustrated using a familiar example, the inverted pendulum, where significant improvements in guaranteed region of operation and cost are noted.
