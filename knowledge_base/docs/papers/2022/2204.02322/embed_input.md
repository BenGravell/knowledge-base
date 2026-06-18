On Global and Local Convergence of Iterative Linear Quadratic Optimization Algorithms for Discrete Time Nonlinear Control

Topics include Trajectory optimization, iLQR, Differential dynamic programming, Convergence analysis, Nonlinear control.

Analyzes both global and local convergence properties of iterative LQR/DDP algorithms for discrete-time nonlinear control, providing theoretical convergence guarantees under specific regularity conditions.

A classical approach for solving discrete time nonlinear control on a finite horizon consists in repeatedly minimizing linear quadratic approximations of the original problem around current candidate solutions. While widely popular in many domains, such an approach has mainly been analyzed locally. We provide detailed convergence guarantees to stationary points as well as local linear convergence rates for the Iterative Linear Quadratic Regulator (ILQR) algorithm and its Differential Dynamic Programming (DDP) variant. For problems without costs on control variables, we observe that global convergence to minima can be ensured provided that the linearized discrete time dynamics are surjective, costs on the state variables are gradient dominated. We further detail quadratic local convergence when the costs are self-concordant. We show that surjectivity of the linearized dynamics hold for appropriate discretization schemes given the existence of a feedback linearization scheme. We present complexity bounds of algorithms based on linear quadratic approximations through the lens of generalized Gauss-Newton methods....

### Introduction

We consider nonlinear control problems in discrete time of the form

where at the time index $t$, $x_{t}$ is the state of the system, $u_{t}$ is the control applied to the system, $f_{t}$ is the discretized nonlinear dynamic, $h_{t}$ is the cost applied to the system state and the control variable, and ${\overline{x}}_{0}$ is a given fixed initial state.

We have detailed computational complexities of the ILQR and IDDP algorithms for discrete time nonlinear control problems. Our analysis decomposes at several scales. At the scale of the whole trajectory, the problem can be summarized as a compositional objective and analyzed as a Gauss-Newton type algorithm. The trajectories can be detailed at the scale of the dynamic, which reveals the low computational cost of the optimization oracles. Finally, the dynamics can further be detailed in terms of the discretization scheme in order to ensure sufficient conditions for convergence of the algorithms towards global optima.

The sufficient conditions for global convergence are restricted to problems without costs or constraints on the control variables. Moreover, they may not be applicable in usual scenarios with costs that are not subsampled. As future work, one may analyze constraints on the control variables while ensuring a gradient dominating-like property on the objective. Analyzing further the links between feedback linearization schemes and sufficient conditions for global optimality may also reveal the impact of the discretization stepsize on the overall condition number of the problem.

If the costs are strongly convex then they satisfy a gradient dominating property and are self-concordant. To satisfy condition, the regularization can then be chosen to be proportional to the norm of the gradient of the costs at the current iterate, i.e., $\nu_{k} = {{\overline{\nu}}_{k}{\|{{\nabla h}{({g{({\mathbf{u}}^{(k)})}})}}\|}_{2}}$ for ${\overline{\nu}}_{k}$ bounded above by a constant which ensures that $\nu_{k}$ tends to 0 with the iterations $k$. By satisfying condition, we can ensure global convergence, while by having $\nu_{k}\rightarrow 0$, we can ensure local quadratic convergence.

### Lemma 7

### Total Complexity

Problems of the form have been tackled in various ways, from direct approaches using nonlinear optimization to convex relaxations using semidefinite optimization....
