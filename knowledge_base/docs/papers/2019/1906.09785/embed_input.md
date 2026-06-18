An Efficient B-spline-Based Kinodynamic Replanning Framework for Quadrotors

Trajectory replanning for quadrotors is essential to enable fully autonomous flight in unknown environments. Hierarchical motion planning frameworks, which combine path planning with path parameterization, are popular due to their time efficiency. However, the path planning cannot properly deal with non-static initial states of the quadrotor, which may result in non-smooth or even dynamically infeasible trajectories. In this paper, we present an efficient kinodynamic replanning framework by exploiting the advantageous properties of the B-spline, which facilitates dealing with the non-static state and guarantees safety and dynamical feasibility. Our framework starts with an efficient B-spline-based kinodynamic (EBK) search algorithm which finds a feasible trajectory with minimum control effort and time. To compensate for the discretization induced by the EBK search, an elastic optimization (EO) approach is proposed to refine the control point placement to the optimal location. Systematic comparisons against the state-of-the-art are conducted to validate the performance....

## Introduction

Autonomous navigation for quadrotors in unknown environments has gained significant interest for its practical usage in various inspection and exploration tasks. To fulfill the need of fully autonomous exploration in unknown environments, trajectory replanning is of great significance. Replanning requires a real-time response to unexpected obstacles to guarantee safety while satisfying the low-level feasibility constraints induced by the non-trivial dynamics.

Many existing methods tackle this challenging problem using a hierarchical framework, which first finds a geometric path and then locally optimizes the path to a dynamically feasible trajectory with respect to a given time allocation. Although this framework is efficient, inadequacy exists between the path finding and the local path parameterization....

### Proof of Theorem 1

The correctness of the theorem follows from the convex hull property of the B-spline. For brevity, we only consider one control point span which consists of $k + 1$ control points, but can be generalized to a long control point sequence without any difficulty. The original tube of one control point span consists of $k + 1$ balls, and the connectivity is already guaranteed by the two-level inflation scheme. As such, there are $k$ intersection areas for the sequence of $k + 1$ control points. Note that here we only consider the intersection between the two balls associated with two neighboring control points....

### VI-B Elastic Optimization Formulation

Figure 6: Illustration of the construction process of 3-degree vertex tuples from an admissible path. Each vertex tuple is formed by combining four consecutive control points. ${\lbrack\overset{\sim}{\pi}\rbrack}_{0}^{3}$ and ${\lbrack\overset{\sim}{\pi}\rbrack}_{1}^{3}$ are two neighboring vertex tuples since they overlap for three vertices.

Figure 10: Comparisons of different kinodynamic planning approaches.

Figure 1: Illustration of the motivating example. The initial state has non-zero velocity (red arrow). The traditional geometric planner finds the shortest path (red squares) and then parameterizes it using a piecewise polynomial (blue). However, the local path parameterization is restricted to a homotopy class (blue area), and the resultant trajectory is jerky (even infeasible) with respect to the given time allocation....
