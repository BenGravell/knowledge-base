Manipulator Inverse Kinematic Solutions Based on Vector Formulations and Damped Least-Squares Methods

Topics include Damped least squares, Inverse kinematics, Robot manipulators, Singularities, Numerical methods, Jacobian methods, Levenberg-Marquardt.

Wampler applies vector formulations and damped least-squares ideas to manipulator inverse kinematics, improving numerical behavior near singularities. The paper is a classic source for robust Jacobian-based inverse-kinematics solvers used in robotics when exact or undamped pseudoinverse methods become ill-conditioned.

Inverse kinematic solutions are used in manipulator controllers to determine corrective joint motions for errors in end-effector position and orientation. Previous formulations of these solutions, based on the Jacobian matrix, are inefficient and fail near kinematic singularities. Vector formulations of inverse kinematic problems are developed that lead to efficient computer algorithms. To overcome the difficulties encountered near kinematic singularities, the exact inverse problem is reformulated as a damped least-squares problem, which balances the error in the solution against the size of the solution. This yields useful results for all manipulator configurations.
