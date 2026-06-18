<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-time Constrained Trajectory Optimization in Robotics: Theory, Implementation and Applications

Topics include Trajectory optimization, Robotics, Real-time, Real-time optimization, Real-time control, Augmented Lagrangian, Primal-dual, iLQR, Differential dynamic programming, Proximal differential dynamic programming, ProxDDP, Constraint programming, Constrained optimal control, Multiple shooting, Aligator, Library.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

PhD dissertation by Wilson Jallet covering the ProxDDP algorithm and the Aligator library. Good discussion on recent works in constrained DDP e.g. ALTRO, primal-dual iLQR, etc.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robotics has been a momentous field of research and development over the past sixty years, since the computer chip revolution in the 1960s. Realising the promise of the field entails research into motion planning and control of robotic systems in many scenarios: from fixed-base robots (e.g. industrial arms) to floating-base wheeled or legged robots. For such schemes to be able to deal with more complex robots, they must plan ahead and satisfy physical and operational constraints, and do so, hopefully, in a reactive manner. For many years, they were rather simple, limited to simple robots doing simple things. Greater complexity and capability was unlocked with more sophisticated planners and controllers, that had access to better models of their subservient systems (geometries, inertia, the existence of contact). An adequate framework to reconcile the domain's requirements is that of optimal control. It allows for predictive models of robot behaviour over given time horizons, and constraint satisfaction, while optimising for a given performance metric. As most optimal control problems cannot be solved in closed-form, we resort to numerical methods.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This numerical optimal control has a proven track record for online motion generation and control on legged robots with real-time requirements (albeit mostly while using simplified models of the robot and environment). However, it typically leads to large-scale mathematical optimisation problems with thousands of variables - a computationally expensive endeavour. Thus, its use in robotics has relied on two axes of progress: faster chips, and efficient, structure-exploiting algorithms (with carefully engineered implementations). This thesis focuses on the latter axis: development of more performant, real-time capable solvers for numerical optimal control, with the objective of "on-the-fly" complex motion generation the for predictive control of sophisticated robots.
