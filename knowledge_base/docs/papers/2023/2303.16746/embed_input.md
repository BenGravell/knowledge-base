<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FATROP: A Fast Constrained Optimal Control Problem Solver for Robot Trajectory Optimization and Control

Topics include Trajectory optimization, Constrained optimization, Optimal control, Riccati factorization, Real-time, CasADi, Acados.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents FATROP, a fast OCP solver based on Riccati factorization of the KKT conditions, achieving sub-2ms solve times with C++ code generation via CasADi integration (ships with CasADi ≥3.6.7 which is also accessible from acados).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization is a powerful tool for robot motion planning and control. State-of-the-art general-purpose nonlinear programming solvers are versatile, handle constraints effectively and provide a high numerical robustness, but they are slow because they do not fully exploit the optimal control problem structure at hand. Existing structure-exploiting solvers are fast, but they often lack techniques to deal with nonlinearity or rely on penalty methods to enforce (equality or inequality) path constraints. This work presents FATROP: a trajectory optimization solver that is fast and benefits from the salient features of general-purpose nonlinear optimization solvers. The speed-up is mainly achieved through the integration of a specialized linear solver, based on a Riccati recursion that is generalized to also support stagewise equality constraints. To demonstrate the algorithm's potential, it is bench-marked on a set of robot problems that are challenging from a numerical perspective, including problems with a minimum-time objective and no-collision constraints. The solver is shown to solve problems for trajectory generation of a quadrotor, a robot manipulator and a truck-trailer problem in a few tens of milliseconds.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The algorithm's C++-code implementation accompanies this work as open source software, released under the GNU Lesser General Public License (LGPL). This software framework may encourage and enable the robotics community to use trajectory optimization in more challenging applications.
