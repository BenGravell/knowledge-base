SCTOMP: Spatially Constrained Time-Optimal Motion Planning

Topics include Motion planning, Time-optimal control, Trajectory optimization, Obstacle avoidance, Path planning, Path parameterization, Spatial planning.

Generalizes time-optimal path following by optimizing inside a spatial corridor instead of assuming a fixed collision-free reference path. SCTOMP combines corridor construction, smooth spline representation, and minimum-time optimization to produce dynamically feasible trajectories.

This paper focuses on spatial time-optimal motion planning, a generalization of the exact time-optimal path following problem that allows the system to plan within a predefined space. In contrast to state-of-the-art methods, we drop the assumption that a collision-free geometric reference is given. Instead, we present a two-stage motion planning method that solely relies on a goal location and a geometric representation of the environment to compute a time-optimal trajectory that is compliant with system dynamics and constraints. To do so, the proposed scheme first computes an obstacle-free Pythagorean Hodograph parametric spline, and second solves a spatially reformulated minimum-time optimization problem. The spline obtained in the first stage is not a geometric reference, but an extension of the environment representation, and thus, time-optimality of the solution is guaranteed. The efficacy of the proposed approach is benchmarked by a known planar example and validated in a more complex spatial system, illustrating its versatility and applicability.

## INTRODUCTION

Time-optimal motion planning within cluttered environments poses multiple challenges. The underlying motion planning scheme needs to compute a set of input commands that drive the system from its current state to a goal location in minimum-time, without compromising system constraints and spatial bounds. Thus, its solution implies a trading-off between time-optimality and spatial-awareness.

The de facto approach to solve this problem has been to decouple it into two stages. First, the *path planning* stage determines a collision-free geometric path according to high level -- task related -- commands. Second, the predefined path is (exactly) tracked either by *path tracking* or *path following*. The former computes a dynamically feasible timing law for traversing along the predetermined geometric path -- *when* to be *where* --, while the latter introduces the timing law and the (bounded) distance to the path as control freedoms.

## CONCLUSION

In this work, we presented a motion planning approach capable of computing time-optimal trajectories in spatially constrained environments. The time-optimal trajectories obtained by our method, not only exploit the system's actuation, but also the available free space. For this purpose, we rely on a spatial reformulation that allows for performing a singularity-free spatial transformation of the system dynamics, as well as the time minimization problem. To compute the underlying parametric functions required by this reformulation, we leverage Pythagorean Hodograph splines....

### III-B2 Efficiently computing collision-free PH splines

Given that our solution aims to be agnostic from a geometric reference, we perform a spatial transformation of the system dynamics in. To do so, we leverage the chain rule as follows:

s.t. ${{{\mathbf{x}}{(\xi_{0})}} = {\mathbf{x}}_{\mathbf{0}}},$ (13b)
${{\mathbf{x}}^{\prime} = \frac{f{({{\mathbf{x}}{(\xi)}},{{\mathbf{u}}{(\xi)}})}}{\overset{˙}{\xi}{({{\mathbf{x}}{(\xi)}},{\mathcal{Z}}_{k})}}},$ $\xi \in \left\lbrack \xi_{0},\xi_{f} \right\rbrack$ (13c)
${{{{\mathbf{x}}{(\xi)}} \in \mathcal{X}},{{{\mathbf{u}}{(\xi)}} \in \mathcal{U}}},$ $\xi \in \left\lbrack \xi_{0},\xi_{f} \right\rbrack$ (13d)
${{{\mathbf{y}}{(\xi_{f})}} = {\mathbf{y}}_{\mathbf{f}}}.$ (13f)
The resultant OCP is a finite horizon problem, and unlike the original problem, the integration interval...
