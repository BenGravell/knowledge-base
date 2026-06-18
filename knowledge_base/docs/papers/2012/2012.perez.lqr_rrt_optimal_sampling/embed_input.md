LQR-RRT*: Optimal Sampling-Based Motion Planning with Automatically Derived Extension Heuristics

Topics include Kinodynamic planning, Rapidly-exploring random tree star, Linear quadratic regulator, Steering function, Underactuated systems.

Uses a linear-quadratic approximation for both the steering function and the cost-to-go extension heuristic in RRT*, automatically deriving these heuristics by locally linearizing system dynamics.

The RRT* algorithm has recently been proposed as an optimal extension to the standard RRT algorithm. However, like RRT, RRT* is difficult to apply in problems with complicated or underactuated dynamics because it requires the design of two domain-specific extension heuristics: a distance metric and node extension method. We propose automatically deriving these two heuristics for RRT* by locally linearizing the domain dynamics and applying linear quadratic regulation (LQR). The resulting algorithm, LQR-RRT*, finds optimal plans in domains with complex or underactuated dynamics without requiring domain-specific design choices. We demonstrate its application in domains that are successively torque-limited, underactuated, and in belief space.
