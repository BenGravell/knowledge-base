<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stabilizing Receding Horizon Control of Nonlinear Systems: A Control Lyapunov Function Approach

Topics include Model predictive control, Receding horizon control, Control Lyapunov functions, Nonlinear systems, Stability guarantees, Terminal cost.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a stabilizing nonlinear receding-horizon controller whose terminal cost is chosen from a control Lyapunov function that upper-bounds the stabilizing controller's cost-to-go. The paper is part of the CLF-MPC line of work connecting finite-horizon optimal control with explicit stability certificates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A modified version of the receding horizon control of nonlinear systems is proposed. The approach is based on a finite horizon optimal control problem with a terminal cost. This method can be treated as an extension of results of De Nicolao et al.. To the case where a control Lyapunov function (CLF)-based stabilizing control law is available. The terminal cost is picked to be a CLF which is also an upper bound on the cost-to-go if the stabilizing control law is applied. The control law is computed a priori using a CLF. Effectiveness of the results is illustrated by applying this approach to the planar model of a ducted fan with a CLF obtained using quasi LPV methods.
