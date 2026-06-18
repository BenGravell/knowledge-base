Time-Optimal Path Tracking for Robots: A Convex Optimization Approach

Topics include Speed planning, Path tracking, Path following, Optimal control, Convex optimization, Convexification, Second-order cone program, Constraints.

Demonstrates how to write down a large optimal control problem (OCP) for time-optimal path tracking for a robotic manipulator, considering many constraints and the dynamics related to such systems. The resulting OCP is a convex second-order cone program, which can be solved with a variety of generic solvers. The value of the paper mostly comes from just the handwritten transcription of the OCP.

This paper focuses on time-optimal path tracking, a subproblem in time-optimal motion planning of robot systems. Through a nonlinear change of variables, the time-optimal path tracking problem is transformed here into a convex optimal control problem with a single state. Various convexity-preserving extension are introduced, resulting in a versatile approach for optimal path tracking. A direct transcription method is presented that reduces finding the globally optimal trajectory to solving a second-order cone program using robust numerical algorithms that are freely available. Validation against known examples and application to a more complex example illustrate the versatility and practicality of the new method.
