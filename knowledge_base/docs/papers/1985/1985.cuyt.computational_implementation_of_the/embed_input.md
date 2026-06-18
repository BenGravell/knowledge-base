Computational Implementation of the Multivariate Halley Method for Solving Nonlinear Systems of Equations

Topics include Halley method, Nonlinear systems, Automatic differentiation, Cubic convergence, Numerical software, Newton's method, Second derivatives.

Cuyt and Rall implement the multivariate Halley method for nonlinear systems using automatic differentiation to compute the first- and second-derivative information needed for cubic convergence. The paper is an early example of combining higher-order nonlinear solvers with automatic differentiation in numerical software.

Cubically convergent iterative methods for the solution of nonlinear systems, such as the multivariate Halley method, require first and second partial derivatives of the functions comprising the system. Automatic differentiation is used to automate the Halley method by supplying routines for the required operators and functions. A Pascal-SC program implements this method in a single-step iteration mode. The program is applied to nonlinear systems, and the results are compared with Newton's method.
