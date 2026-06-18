Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding

Topics include Conic optimization, Operator splitting, Homogeneous self-dual embedding, Alternating-direction method of multipliers, First-order methods, SCS, Infeasibility certificates, Large-scale optimization.

Introduces SCS, a first-order cone solver that applies operator splitting to a homogeneous self-dual embedding of the cone program. The design trades high-accuracy interior-point behavior for scalability and robustness: the same iterations can return primal or dual solutions or infeasibility certificates, support several cone families, and solve large SOCP, SDP, exponential-cone, and power-cone problems with direct or indirect linear algebra.

We introduce a first order method for solving very large convex cone programs. The method uses an operator splitting method, the alternating directions method of multipliers, to solve the homogeneous self-dual embedding, an equivalent feasibility problem involving finding a nonzero point in the intersection of a subspace and a cone. This approach has several favorable properties. Compared to interior-point methods, first-order methods scale to very large problems, at the cost of requiring more time to reach very high accuracy. Compared to other first-order methods for cone programs, our approach finds both primal and dual solutions when available or a certificate of infeasibility or unboundedness otherwise, is parameter-free, and the per-iteration cost of the method is the same as applying a splitting method to the primal or dual alone. We discuss efficient implementation of the method in detail, including direct and indirect methods for computing projection onto the subspace, scaling the original problem data, and stopping criteria....

## Introduction

In this paper we develop a method for solving convex cone optimization problems that can (a) provide primal or dual certificates of infeasibility when relevant and (b) scale to large problem sizes. The general idea is to use a first-order method to solve the homogeneous self-dual embedding of the primal-dual pair; the homogeneous self-dual embedding provides the necessary certificates, and first-order methods scale well to large problem sizes.

The homogeneous self-dual embedding is a single convex feasibility problem that encodes the primal-dual pair of optimization problems. Solving the embedded problem involves finding a nonzero point in the intersection of two convex sets, a convex cone and a subspace. If the original pair is solvable, then a solution can be recovered from any nonzero solution to the embedding; otherwise, a certificate of infeasibility is generated that proves that the primal or dual is infeasible (and the other one unbounded). The homogeneous self-dual embedding has been widely used with interior-point methods Ye:11; sedumi; SY:12.

We presented an algorithm that can return primal and dual optimal points for convex cone programs when possible, and certificates of primal or dual infeasibility otherwise. The technique involves applying an operator splitting method, the alternating direction method of multipliers, to the homogeneous self-dual embedding of the original optimization problem. This embedding is a feasibility problem that involves finding a point in the intersection of an affine set and a convex cone, and each iteration of our method solves a system of linear equations and projects a point onto the cone....

We provide a reference implementation of our algorithm in C, which we call SCS. We show that this solver can solve large instances of cone problems to modest accuracy quickly and is particularly well suited to solving large cone problems outside of the reach of standard interior-point methods. As far as we know, the problems reported in Sect. 6.6 are the largest general purpose cone problems solved to date.

for any $\gamma > 0$. Expanding and setting

with variables $u$ and $v$. The KKT conditions for this problem are

The original residuals can be expressed in terms of the scaled data as
