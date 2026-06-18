## Introduction

Many robotics tasks are framed as constrained optimization problems. For example, inverse kinematics (IK) seeks a robot configuration that matches a desired pose while respecting constraints like joint limits or stability. Motion planning and optimal control aim to determine trajectories or control commands that satisfy task-specific dynamics and environmental constraints. Model predictive control (MPC) solves real-time optimal control problems by addressing simplified, short-horizon constrained optimization problems.

Several second-order solvers such as SNOPT \[(https://arxiv.org/html/2506.14865v1#bib.bib1)\], SLSQP \[(https://arxiv.org/html/2506.14865v1#bib.bib2)\], LANCELOT \[(https://arxiv.org/html/2506.14865v1#bib.bib3)\], and IPOPT \[(https://arxiv.org/html/2506.14865v1#bib.bib4)\]---are commonly used to solve general constrained optimization problems. In robotics, however, most research focuses on solvers tailored to specific problems. For instance, constrained versions of differential dynamic programming (DDP) \[(https://arxiv.org/html/2506.14865v1#bib.bib5)\], iterative linear quadratic regulator (iLQR) \[(https://arxiv.org/html/2506.14865v1#bib.bib6)\], TrajOpt \[(https://arxiv.org/html/2506.14865v1#bib.bib7)\], and CHOMP \[(https://arxiv.org/html/2506.14865v1#bib.bib8)\] are used for motion planning. However, many of these solvers are not open-source, making them difficult to benchmark and improve. Moreover, adapting them for real-time feedback applications, such as closed-loop IK and MPC, often requires significant tuning.

Figure 1: Chess robot setup. SPG-based IK solver validated on a publicly available 5-DOF chess-playing robot, successfully determines correct pick poses autonomously with 100% accuracy.

We address these challenges by proposing a simple yet powerful solver that can be easily implemented without requiring large memory resources. This solver exploits geometric constraints inherent to many robotic tasks, which can be described using geometric set primitives (see Table [I](https://arxiv.org/html/2506.14865v1#S3.T1 "Table I ‣ III Problem Formulation ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")). Examples include joint limits, center-of-mass stability, and avoiding or reaching geometric shapes (e.g., spheres or convex polytopes). These constraints can often be framed as projections rather than full constraint formulations. We argue that leveraging these projections, rather than treating constraints generically, can significantly improve solver performance.

One of the simplest algorithms for handling such projections is projected gradient descent, where the gradient is projected to ensure the next iterate remains inside the constraint set. A more advanced version, spectral projected gradient descent (SPG), has demonstrated strong practical performance and is considered a competitive alternative to second-order solvers in various fields \[(https://arxiv.org/html/2506.14865v1#bib.bib9)\]. Extensions of SPG to handle additional constraints using augmented Lagrangian methods have been explored in \[(https://arxiv.org/html/2506.14865v1#bib.bib10), (https://arxiv.org/html/2506.14865v1#bib.bib11), (https://arxiv.org/html/2506.14865v1#bib.bib12)\]. However, the application of these projection-based methods to popular second-order solvers in robotics has not been widely explored \[(https://arxiv.org/html/2506.14865v1#bib.bib13)\], resulting in a missed opportunity to fully exploit the potential of projections in this domain.

This paper makes the following contributions:

We propose an efficient projection-based optimization method that leverages geometric constraints in robotics tasks and extend Augmented Lagrangian Spectral Projected Gradient Descent (ALSPG) with a direct shooting method to handle multiple nonlinear constraints.

We introduce and integrate various geometric projections including Euclidean projections, polytopic projections, and learning-based projections, into the ALSPG.

We validate our approach through numerical simulations on planar arm systems, Franka robot arms, humanoid robots, and autonomous vehicles, providing performance benchmarks and analysis against baseline methods. We further assess the effectiveness of our method through real-world experiments on 6-axis and 7-axis robotic arms and a 1:10 scale car.

## Related work

In optimization, Euclidean projections and the analytical expressions for various projections are fundamental for efficiently solving constrained optimization problems. The general theory for projecting onto a level set of an arbitrary function using KKT conditions is discussed in \[(https://arxiv.org/html/2506.14865v1#bib.bib14)\]. Extensive studies on projection methods and their properties can be found in \[(https://arxiv.org/html/2506.14865v1#bib.bib15)\], which provides a comprehensive theoretical background. In \[(https://arxiv.org/html/2506.14865v1#bib.bib16)\], Usmanova *et al.* propose an efficient algorithm for projecting onto arbitrary convex constraint sets, demonstrating that exploiting projections in optimization can significantly improve performance. Further, Bauschke and Koch \[(https://arxiv.org/html/2506.14865v1#bib.bib17)\] discuss and benchmark algorithms for projecting onto the intersection of convex sets, with Dykstra's alternating projection algorithm \[(https://arxiv.org/html/2506.14865v1#bib.bib18)\] being a key method for this task.

The simplest algorithm exploiting projections is projected gradient descent, which performs well in many settings. SPG improves upon this by exploiting curvature information via its spectral stepsizes, leading to faster convergence in many problems. A detailed review of SPG is provided in \[(https://arxiv.org/html/2506.14865v1#bib.bib11)\], highlighting its success in constrained optimization tasks. In \[(https://arxiv.org/html/2506.14865v1#bib.bib19)\], Torrisi *et al.* propose to use a projected gradient descent algorithm to solve the subproblems of sequential quadratic programming (SQP). They show that their method can solve MPC of an inverted pendulum faster than SNOPT. Our work is closest to theirs with the differences that we use SPG instead of a vanilla projected gradient descent to solve the subproblems of augmented Lagrangian instead of SQP. Additionally, we propose a direct way of handling multiple projections and inequality constraints, which is not trivial in \[(https://arxiv.org/html/2506.14865v1#bib.bib19)\].

In \[(https://arxiv.org/html/2506.14865v1#bib.bib20)\], Giftthaler and Buchli propose a projection of the updated direction of the control input onto the nullspace of the linearized constraints in iLQR. This approach can only handle simple equality constraints (for example, velocity-level constraints of second-order systems) and cannot treat position-level constraints for such systems, which is a very common and practical class of constraints in real world applications.

## Problem Formulation

$l \leq {\frac{1}{2}{\mathbf{x}}^{\top}{\mathbf{x}}} \leq u$

x &amp; {{\text{if~}l} \leq x \leq u} \\
{\mathbf{x}} &amp; {{\text{if~}l} \leq {{\mathbf{a}}^{\top}{\mathbf{x}}} \leq u} \\
{{\mathbf{x}} - \frac{{\mathbf{a}}{({{{\mathbf{a}}^{\top}{\mathbf{x}}} - u})}}{{\parallel{\mathbf{a}}\parallel}_{2}^{2}}} &amp; {{\text{if~}{\mathbf{a}}^{\top}{\mathbf{x}}} &gt; u} \\
{{\mathbf{x}} - \frac{{\mathbf{a}}{({{{\mathbf{a}}^{\top}{\mathbf{x}}} - l})}}{{\parallel{\mathbf{a}}\parallel}_{2}^{2}}} &amp; {{\text{if~}{\mathbf{a}}^{\top}{\mathbf{x}}} &lt; l}
{\mathbf{x}} &amp; {{\text{if~}l} \leq {\frac{1}{2}{\mathbf{x}}^{\top}{\mathbf{x}}} \leq u} \\
\frac{{\mathbf{x}}\sqrt{2u}}{\parallel{\mathbf{x}}\parallel} &amp; {{\text{if~}\frac{1}{2}{\mathbf{x}}^{\top}{\mathbf{x}}} &gt; u} \\
\frac{{\mathbf{x}}\sqrt{2l}}{\parallel{\mathbf{x}}\parallel} &amp; {{\text{if~}l} &gt; {\frac{1}{2}{\mathbf{x}}^{\top}{\mathbf{x}}}}
{{({\mathbf{x}},t)},} &amp; {{\text{if~}{\parallel{\mathbf{x}}\parallel}} \leq t} \\
{{(\mathbf{0},0)},} &amp; {{\text{if~}{\parallel{\mathbf{x}}\parallel}} \leq {- t}} \\
{\frac{{\parallel{\mathbf{x}}\parallel} + t}{2}{(\frac{\mathbf{x}}{\parallel{\mathbf{x}}\parallel},1)}} &amp; \text{otherwise}

TABLE I: Projections onto bounded domains, affine hyperplane, quadric and second-order cone.

In this section, we present the definitions of projections used in robotic problems to formulate constraints such as constrained inverse kinematics, obstacle avoidance and other manipulation planning problems.

### III-A Euclidean Projections

Figure 2: Geometric Projections. Projecting outside of a set can be utilized for collision avoidance while projecting inside or onto a set can be employed for goal reaching. a) Analytical circle projection. b) Analytical box projection. c) Polytopic projection. d) Implicit projection.

The solution ${\mathbf{x}}^{\ast}$ to the following constrained optimization problem

is called an Euclidean projection of the point ${\mathbf{x}}_{0}$ onto the set $\mathcal{C}$ and is denoted as ${\mathbf{x}}^{\ast} = {\Pi_{\mathcal{C}}{({\mathbf{x}}_{0})}}$. This operation determines the point ${\mathbf{x}} \in \mathcal{C}$ that is closest to ${\mathbf{x}}_{0}$ in Euclidean sense. For many sets $\mathcal{C}$, $\Pi_{\mathcal{C}}{( \cdot )}$ admits analytical expressions that are given in [Table I](https://arxiv.org/html/2506.14865v1#S3.T1 "In III Problem Formulation ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"). Even though, usually, these sets are convex (e.g. bounded domains), some nonconvex sets also admit analytical solution(s) that are easy to compute (e.g. being outside of a sphere). In cases $\mathcal{C}$ is non-convex, multiple feasible solutions may exist. In such situations, either a strategy for selecting the solution or a convex decomposition method may be required. Note that many of these sets are frequently used in robotics, from joint/torque limits and avoiding spherical/square obstacles to satisfying virtual fixtures defined in the task space of the robot.

### III-B Polytopic Projections

The geometries of mobile robots often vary, and they can be represented as polytopes defined by hyperplanes. When considering the robot's geometry, Euclidean projections may not always be applicable. It becomes necessary to account for projections between the robot (modeled as a polytope) and obstacles. Let the robot's shape be convex, with its occupied space denoted as the set $\mathcal{C}_{r}$. The geometric center of the polytopic robot, denoted ${\mathbf{p}} \in {\mathbb{R}}^{n}$, serves as the point of interest for control and collision avoidance. We consider the obstacles or goal regions as convex polytopes in ${\mathbb{R}}^{n}$ (with $n = 2$ or $3$). If the shapes are not convex, the convex-hulls or convex-decomposition can be employed to approximate them as a collection of convex polytopes. The Minkowski sum $\mathcal{M}$ between robot and polytopic set $\mathcal{C}$ is defined as:

where $\mathcal{M}$ is the configuration space obstacle for translation movements of robots. If the geometric center $p \in \mathcal{M}$, the robot and the polytope object intersect. The problem of projections between two polytopic sets then reduces to projections between the geometric center $\mathbf{p}$ and the Minkowski sum $\mathcal{M}$, since $\mathcal{M}$ is composed of hyperplanes, projecting a point out of a polytope, ${\mathbf{x}}^{\ast} = {\Pi_{\mathcal{M}}{({\mathbf{x}}_{0})}}$, can be resolved using the method outlined [I](https://arxiv.org/html/2506.14865v1#S3.T1 "Table I ‣ III Problem Formulation ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"), as shown in [Fig. 2](https://arxiv.org/html/2506.14865v1#S3.F2 "In III-A Euclidean Projections ‣ III Problem Formulation ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"). The robot's rotational movements can be accounted for by augmenting the Minkowski set with an additional dimension.

### III-C Implicit Projections

When the shape of the object is implicit and cannot be expressed using hyperplanes, learning-based techniques can be employed to design the projections. Bernstein polynomial basis functions are efficient for learning the implicit shape. The advantage of this approach lies in the availability of analytical and smooth gradient information. Assuming the order of the polynomials is $r$ and there are $c$ control points, the matrix form of the implicit shape is $\mathcal{S}:={{\mathbf{t}}^{\top}{\mathbf{M}}\Phi}$, where ${\mathbf{t}} \in {\mathbb{R}}^{r}$ is the time vector, and ${\mathbf{M}} \in {\mathbb{R}}^{r \times c}$ is the characteristic matrix and $\Phi \in {\mathbb{R}}^{c}$ represents the control points. The analytical gradient $\nabla_{t}\mathcal{S}$ can be computed efficiently. The implicit projection is demonstrated in [Fig. 2](https://arxiv.org/html/2506.14865v1#S3.F2 "In III-A Euclidean Projections ‣ III Problem Formulation ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization").

## Augmented Lagrangian Spectral Projected Gradient Descent for Robotics

This section gives the SPG algorithm along with the non-monotone line search procedure. These algorithms are easy to implement without big memory requirements and yet result in powerful solvers. Next, we give the ALSPG algorithm based on geometric projections. Finally, the direct shooting approach is adopted to formulate the constrained optimization problems for robotics.

### IV-A Spectral Projected Gradient Descent

SPG is an improved version of a vanilla projected gradient descent using spectral stepsizes. Its excellent numerical results even in comparison to second-order methods have been a point of attraction in the optimization literature \[(https://arxiv.org/html/2506.14865v1#bib.bib9)\]. SPG tackles constrained optimization problems in the form of

by constructing a local quadratic model of the objective function

and by minimizing it subject to the constraints as

whose solution is an Euclidean projection as described in ((https://arxiv.org/html/2506.14865v1#S3.E1 "Eq. 1 ‣ III-A Euclidean Projections ‣ III Problem Formulation ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")) and given by $\Pi_{\mathcal{C}}{({{\mathbf{x}}_{k} - {\gamma_{k}{\nabla f}{({\mathbf{x}}_{k})}}})}$. The local search direction ${\mathbf{d}}_{k}$ for SPG is then given by

which is used in a non-monotone line search ([Algorithm 1](https://arxiv.org/html/2506.14865v1#algorithm1 "In IV-A Spectral Projected Gradient Descent ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")) with ${\mathbf{x}}_{k + 1} = {{\mathbf{x}}_{k} + {\alpha_{k}{\mathbf{d}}_{k}}}$, to find $\alpha_{k}$ satisfying ${f{({\mathbf{x}}_{k + 1})}} \leq {f_{\text{max}} + {\alpha_{k}\gamma_{k}{\nabla f}{({\mathbf{x}}_{k})}^{\top}{\mathbf{d}}_{k}}}$, where $f_{\text{max}} = {\max{\{{\left. {f{({\mathbf{x}}_{k - j})}} \middle| \:0 \right. \leq j \leq {\min{\{ k,{M - 1}\}}}}\}}}$. Non-monotone line search allows for increasing objective values for some iterations $M$ preventing getting stuck at bad local minima. A typical value for $M$ is $10$. When $M = 1$, it reduces to a monotone line search.

2 fmax = max {f(xk − j)|0 ≤ j ≤ min {k, M − 1}}
5 $\overline{\alpha} = {- {0.5\alpha^{2}c\left( {{f{({{\mathbf{x}}_{k} + {\alpha{\mathbf{d}}_{k}}})}} - {f{({\mathbf{x}}_{k})}} - {\alpha c}} \right)^{- 1}}}$
6 if $0.1 \leq \overline{\alpha} \leq 0.9$ then
7 $\alpha = \overline{\alpha}$
Algorithm 1 Non-monotone line search

3 Find a search direction by dk = Π𝒞(xk−γk∇f(xk)) − xk
4 Do non-monotone line search using Algorithm 1 to find xk + 1 = xk + αkdk
7 $\gamma^{} = \frac{{\mathbf{s}}_{k + 1}^{\top}{\mathbf{s}}_{k + 1}}{{\mathbf{s}}_{k + 1}^{\top}{\mathbf{y}}_{k + 1}}$ and $\gamma^{} = \frac{{\mathbf{s}}_{k + 1}^{\top}{\mathbf{y}}_{k + 1}}{{\mathbf{y}}_{k + 1}^{\top}{\mathbf{y}}_{k + 1}}$
12 $\gamma_{k + 1} = {\gamma^{} - {\frac{1}{2}\gamma^{}}}$
Algorithm 2 Spectral Projected Gradient Descent

The choice of $\gamma_{k}$ affects the convergence properties significantly since it introduces curvature information to the solver. Note that when choosing $\gamma_{k} = 1$, SPG is equivalent to the widely known projected gradient descent. SPG uses spectral stepsizes obtained by a least-square approximation of the Hessian matrix by $\gamma_{k}{\mathbf{I}}$. These spectral stepsizes are computed by proposals

where ${\mathbf{s}}_{k} = {{\mathbf{x}}_{k} - {\mathbf{x}}_{k - 1}}$ and ${\mathbf{y}}_{k} = {{{\nabla f}{({\mathbf{x}}_{k})}} - {{\nabla f}{({\mathbf{x}}_{k - 1})}}}$ \[(https://arxiv.org/html/2506.14865v1#bib.bib9)\]. In the case of the quadratic objective function in the form of ${\mathbf{x}}^{\top}{\mathbf{Q}}{\mathbf{x}}$, these two values correspond to the maximum and minimum eigenvalues of the matrix $\mathbf{Q}$. The initial spectral stepsize can be computed by setting ${\overline{\mathbf{x}}}_{0} = {{\mathbf{x}}_{0} - {\gamma_{\text{small}}{\nabla f}{({\mathbf{x}}_{0})}}}$ where $\gamma_{\text{small}}$ is $10^{- 4}$, and computing ${\overline{\mathbf{s}}}_{0} = {{\overline{\mathbf{x}}}_{0} - {\mathbf{x}}_{0}}$ and ${\overline{\mathbf{y}}}_{0} = {{{\nabla f}{({\overline{\mathbf{x}}}_{0})}} - {{\nabla f}{({\mathbf{x}}_{0})}}}$. Note that this heuristic operation costs one more gradient computation. The final algorithm is given by [Algorithm 2](https://arxiv.org/html/2506.14865v1#algorithm2 "In IV-A Spectral Projected Gradient Descent ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization").

### IV-B Augmented Lagrangian spectral projected gradient descent

SPG alone is usually not sufficient to solve problems in robotics with complicated nonlinear constraints. In \[(https://arxiv.org/html/2506.14865v1#bib.bib12)\], Jia *et al.* provides an augmented Lagrangian framework to solve problems with constraints ${{\mathbf{g}}{({\mathbf{x}})}} \in \mathcal{C}$ and ${\mathbf{x}} \in \mathcal{D}$, where ${\mathbf{g}}{( \cdot )}$ is a convex function, $\mathcal{C}$ is a convex set, and $\mathcal{D}$ is a closed nonempty set, both equipped with easy projections.

In this section, we build on the work in \[(https://arxiv.org/html/2506.14865v1#bib.bib12)\] with the extension of multiple projections and additional general equality and inequality constraints. The general optimization problem that we are tackling here is

where ${\mathbf{g}}_{i}{( \cdot )}$ are assumed to be arbitrary nonlinear functions. Note that even though the convergence results in \[(https://arxiv.org/html/2506.14865v1#bib.bib12)\] apply to the case when these are convex functions and convex sets, we found in practice that the algorithm is powerful enough to extend to more general cases.

We use the following augmented Lagrangian function

whose derivative w.r.t. $\mathbf{x}$ is given by

using the property of convex Euclidean projections derivative $\nabla{\parallel{\mathbf{g}}{({\mathbf{x}})} - \Pi{({\mathbf{g}}{({\mathbf{x}})})}\parallel}_{2}^{2} = \nabla{\mathbf{g}}{({\mathbf{x}})}^{\top}\left( {\mathbf{g}}{({\mathbf{x}})} - \Pi\left. ({\mathbf{g}}{({\mathbf{x}})} \right) \right.$, see \[(https://arxiv.org/html/2506.14865v1#bib.bib15)\] for details. $\mathbf{λ}$ is vector of the Lagrangian multipliers and $\rho$ is the penalty parameter. This way, we obtain a formulation that does not need the gradient of the projection function $\Pi_{\mathcal{C}_{i}}{( \cdot )}$. One iteration of ALSPG optimizes the subproblem ${{\mathsf{a}\mathsf{r}\mathsf{g}}{\mathsf{m}\mathsf{i}\mathsf{n}}}_{{\mathbf{x}} \in \mathcal{D}}{\mathcal{L}{({\mathbf{x}},{\{{\mathbf{λ}}^{\mathcal{C}_{i}},\rho^{\mathcal{C}_{i}}\}}_{i = 1}^{p})}}$ given ${\{{\mathbf{λ}}^{\mathcal{C}_{i}},\rho^{\mathcal{C}_{i}}\}}_{i = 1}^{p}$, and then updates these according to the next iterate. Defining the auxiliary function ${V{({\mathbf{x}},{\mathbf{λ}}^{\mathcal{C}_{i}},\rho^{\mathcal{C}_{i}})}} = \left. \parallel{{{\mathbf{g}}_{i}{({\mathbf{x}})}} - {\Pi_{\mathcal{C}_{i}}\left( {{{\mathbf{g}}_{i}{({\mathbf{x}})}} + \frac{{\mathbf{λ}}^{\mathcal{C}_{i}}}{\rho^{\mathcal{C}_{i}}}} \right)}}\parallel \right.$, the algorithm is summarized in [Algorithm 3](https://arxiv.org/html/2506.14865v1#algorithm3 "In IV-B Augmented Lagrangian spectral projected gradient descent ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"). Note that one can define and tune many heuristics around augmented Lagrangian methods with possible extensions to primal-dual methods.

3 xk + 1 = argminx ∈ 𝒟ℒ(x,{λ𝒞i, ρ𝒞i}i = 1p) with SPG in Algorithm 2
6 $\lambda_{k + 1}^{\mathcal{C}_{i}} = {\rho^{\mathcal{C}_{i}}\left( {{{{\mathbf{g}}_{i}{({\mathbf{x}})}} + \frac{{\mathbf{λ}}^{\mathcal{C}_{i}}}{\rho^{\mathcal{C}_{i}}}} - {\Pi_{\mathcal{C}_{i}}\left( {{{\mathbf{g}}_{i}{({\mathbf{x}})}} + \frac{{\mathbf{λ}}^{\mathcal{C}_{i}}}{\rho^{\mathcal{C}_{i}}}} \right)}} \right)}$

### IV-C Optimal Control with ALSPG

We consider the following generic constrained optimization problem

where the state trajectory ${\mathbf{x}} = \begin{bmatrix}
{{\mathbf{x}}_{1}^{\top},{\mathbf{x}}_{2}^{\top},\ldots,{\mathbf{x}}_{t}^{\top},\ldots,{\mathbf{x}}_{T}^{\top}}
\end{bmatrix}^{\top}$, the control trajectory ${\mathbf{u}} = \begin{bmatrix}
{{\mathbf{u}}_{0}^{\top},{\mathbf{u}}_{1}^{\top},\ldots,{\mathbf{u}}_{t}^{\top},\ldots,{\mathbf{u}}_{T - 1}^{\top}}
\end{bmatrix}^{\top}$ and the function ${\mathbf{F}}{( \cdot, \cdot )}$ correspond to the forward rollout of the states using a dynamics model ${\mathbf{x}}_{t + 1} = {{\mathbf{f}}{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}$. We use a direct shooting approach and transform [Eq. 8](https://arxiv.org/html/2506.14865v1#S4.E8 "In IV-C Optimal Control with ALSPG ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") into a problem in $\mathbf{u}$ only by considering

which is exactly in the form of [Eq. 7](https://arxiv.org/html/2506.14865v1#S4.E7 "In IV-B Augmented Lagrangian spectral projected gradient descent ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"), if ${{\mathbf{g}}_{1}{({\mathbf{u}})}} = {{\mathbf{F}}{({\mathbf{x}}_{0},{\mathbf{u}})}}$ and ${{\mathbf{g}}_{2}{({\mathbf{u}})}} = {{\mathbf{h}}{({{\mathbf{F}}{({\mathbf{x}}_{0},{\mathbf{u}})}},{\mathbf{u}})}}$. The unconstrained version of this problem can be solved with least-square approaches. However, assuming ${\mathbf{x}}_{t} \in {\mathbb{R}}^{m}$, ${\mathbf{u}}_{t} \in {\mathbb{R}}^{n}$, this requires the inversion of a matrix of size ${{Tn} \times T}n$, whereas here we only work with the gradients of the objective function and the functions ${\mathbf{g}}_{i}{( \cdot )}$. The component that requires a special attention is ${\nabla{\mathbf{F}}}{({\mathbf{x}}_{0},{\mathbf{u}})}$ and in particular, its transpose product with a vector. It turns out that this product can be efficiently computed with a recursive formula (as also described in \[(https://arxiv.org/html/2506.14865v1#bib.bib19)\]), resulting in fast SPG iterations. Denoting ${\mathbf{A}}_{t} = {{\nabla_{{\mathbf{x}}_{t}}{\mathbf{f}}}{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}$, ${\mathbf{B}}_{t} = {{\nabla_{{\mathbf{u}}_{t}}{\mathbf{f}}}{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}$, and ${{\nabla_{\mathbf{u}}{\mathbf{F}}}{({\mathbf{x}}_{0},{\mathbf{u}})}^{\top}{\mathbf{y}}} = {\mathbf{z}}$ with ${\mathbf{y}} = \begin{bmatrix}
{{\mathbf{y}}_{0},{\mathbf{y}}_{1},\ldots,{\mathbf{y}}_{t},\ldots,{\mathbf{y}}_{T - 1}}
\end{bmatrix}$, ${\mathbf{z}} = \begin{bmatrix}
{{\mathbf{z}}_{0},{\mathbf{z}}_{1},\ldots,{\mathbf{z}}_{t},\ldots,{\mathbf{z}}_{T - 1}}
\end{bmatrix}$, one can show that the matrix vector product ${\nabla_{\mathbf{u}}{\mathbf{F}}}{({\mathbf{x}}_{0},{\mathbf{u}})}^{\top}{\mathbf{y}}$ can be written as

where the terms in parantheses can be computed recursively backward by ${\overline{\mathbf{z}}}_{t + 1} = {({{\mathbf{y}}_{t + 1} + {{\mathbf{A}}_{t}^{\top}{\overline{\mathbf{z}}}_{t}}})}$, ${\mathbf{z}}_{t} = {{\mathbf{B}}_{t - 1}^{\top}{\overline{\mathbf{z}}}_{t}}$ and ${\overline{\mathbf{z}}}_{T - 1} = {\mathbf{y}}_{T - 1}$, without having to construct the big matrix ${\nabla_{\mathbf{u}}{\mathbf{F}}}{({\mathbf{x}}_{0},{\mathbf{u}})}^{\top}$. Note that when there are no constraints on the state and ${{\mathbf{h}}{( \cdot )}} = 0$, [Eq. 9](https://arxiv.org/html/2506.14865v1#S4.E9 "In IV-C Optimal Control with ALSPG ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") can be solved directly with the SPG algorithm.

## Experiments

In this section, we perform extensive simulations and real-world experiments on multiple robotic tasks, including IK problems, motion planning, MPC for a contact-rich pushing task, autonomous navigation and parking tasks. Real-world evaluations were conducted on a 7-axis Franka robot, a 6-axis P-Rob robot, and a 1:10 scale car. The motivation behind these experiments is to show that: 1) the proposed way of solving these robotics problems can be faster than the second-order methods such as iLQR and IPOPT; and 2) exploiting projections whenever we can, instead of leaving the constraints for the solver to treat them as generic constraints, increases the performance significantly.

### V-A Inverse kinematics

We first evaluate the performance of SPG compared to iLQR^11^1The implementation and code of iLQR can refer to [RCFS](https://calinon.ch/codes.htm). in a reach planning task using a 7-axis manipulator without constraints. iLQR is implemented with dynamic programming. SPG is implemented as detailed in the previous section. Both implementations are in Python. The control input is $\overset{¨}{q} \in {\mathbb{R}}^{7}$ and the states are joint velocities and positions ${(\overset{˙}{q},q)} \in {\mathbb{R}}^{14}$. The results on [Fig. 3(b)](https://arxiv.org/html/2506.14865v1#S5.F3.sf2 "In Fig. 3 ‣ V-A Inverse kinematics ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") show that the convergence time scales linearly with the planning horizons due to the growing number of decision variables. Notably, SPG scales more efficiently than iLQR, demonstrating its potential for real-time applications.

Figure 3: Comparison of iLQR and SPG in terms of convergence time evolution vs the number of horizons.

Num. of fun. eval.
Num of Jac. eval.

Talos IK without Proj.

Talos IK with Proj.

TABLE II: Comparison of constrained inverse kinematics with and without projections.

A Constrained inverse kinematics problem can be described in many ways using projections. One typical way is to find a feasible ${\mathbf{q}} \in \mathcal{C}_{\mathbf{q}}$ that minimizes a cost to be away from a given initial configuration ${\mathbf{q}}_{0}$ while respecting general constraints ${{\mathbf{h}}{({\mathbf{q}})}} = \mathbf{0}$ and projection constraints ${{\mathbf{f}}{({\mathbf{q}})}} \in \mathcal{C}_{\mathbf{x}}$

where ${\mathbf{f}}{( \cdot )}$ can represent entities such as the end-effector pose or the center of mass for which the constraints are easier to be expressed as projections onto $\mathcal{C}_{\mathbf{x}}$, and $\mathcal{C}_{\mathbf{q}}$ can represent the configuration space within the joint limits. [Fig. 4](https://arxiv.org/html/2506.14865v1#S5.F4 "In V-A Inverse kinematics ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") shows a 3-axis planar manipulator with ${\mathbf{f}}{( \cdot )}$ representing the end-effector position and $\mathcal{C}_{\mathbf{x}}$ denoting feasible regions.

Figure 4: Projection view of inverse kinematics problem. (a) Reaching a point (standard IK problem): 𝒞x = {x|x = xd}. (b) Reaching under/above/on a plane (in the halfspace): 𝒞x = {x|a⊤x + b = 0}. (c) Reaching inside/outside/on a circle: 𝒞x = {x| ≤ ri2 ≤ ∥ x − xd∥22 ≤ ro2}. (d) Reaching inside/outside/on a rectangle: 𝒞x = {x| ∥ x − xd∥∞, W ≤ L}.

Talos IK: We tested our algorithm on a high-dimensional (32 DoF) IK problem for the TALOS robot (see [Fig. 5(a)](https://arxiv.org/html/2506.14865v1#S5.F5.sf1 "In Fig. 5 ‣ V-A Inverse kinematics ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")), subject to the following constraints: i) the center of mass must remain inside a box; ii) the end-effector must lie within a sphere; and iii) the foot position and orientation are fixed. We compared two versions of the ALSPG algorithm: 1) by casting these constraints as projections onto $\mathcal{C}_{\mathbf{x}}$; and 2) by embedding all constraints within the function ${\mathbf{h}}{( \cdot )}$ to assess the direct advantages of exploiting projections in ALSPG. The algorithm was run from 1000 different random initial configurations for both versions, and we compared the number of function and Jacobian evaluations. The results, shown in Table [II](https://arxiv.org/html/2506.14865v1#S5.T2 "Table II ‣ V-A Inverse kinematics ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"), demonstrate that using projections significantly improves efficiency.

Robust IK: In this experiment, we would like to achieve a task of reaching and staying in the half-space under a plane whose slope is stochastic because, for example, of the uncertainties in the measurements of the vision system. The constraint can be written as ${{\mathbf{a}}^{\top}{\mathbf{f}}{({\mathbf{q}})}} \leq 0$, where ${\mathbf{a}} \sim {\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}}$. We can transform it into a chance constraint to provide some safety guarantees probabilistically. The idea is to find a joint configuration $\mathbf{q}$ such that it will stay under a stochastic hyperplane with a probability of $\eta \geq 0.5$. This inequality can be written as a second-order cone constraint wrt ${\mathbf{f}}{({\mathbf{q}})}$ as ${{{\mathbf{μ}}^{\top}{\mathbf{f}}{({\mathbf{q}})}} + {\Psi^{- 1}{(\eta)}{\parallel{\mathbf{\Sigma}^{\frac{1}{2}}{\mathbf{f}}{({\mathbf{q}})}}\parallel}_{2}}} \leq 0$, where $\Psi{( \cdot )}$ is the cumulative distribution function of zero mean unit variance Gaussian variable. Defining ${{\mathbf{g}}{({\mathbf{q}})}} = \begin{bmatrix}
{({\mathbf{\Sigma}^{\frac{1}{2}}f{({\mathbf{q}})}})}^{\top} & {{\mathbf{μ}}^{\top}{\mathbf{f}}{({\mathbf{q}})}}
\end{bmatrix}^{\top}$, the optimization problem can then be defined as

which can be solved efficiently without using second-order cone (SOC) gradients, by using the proposed algorithm. We tested the algorithm on the 3-axis robot shown in [Fig. 5(b)](https://arxiv.org/html/2506.14865v1#S5.F5.sf2 "In Fig. 5 ‣ V-A Inverse kinematics ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") by optimizing for a joint configuration with a probability of $\eta = 0.8$ and then computing continuously the constraint violation for the last 1000 time steps by sampling a line slope from the given distribution. We obtained a constraint violation percentage of around 80%, as expected.

Figure 5: Inverse kinematics and motion planning problems solved with the proposed algorithm. (a) Talos inverse kinematics problem with foot pose, center of mass stability (red point inside yellow rectangular prism) and end-effector inside a (pink) sphere constraints. (b) Robust inverse kinematics solution with $\mathcal{C}_{\mathbf{p}} = {\{{\mathbf{p}}|{\mathbf{μ}}^{\top}{\mathbf{p}} + \Psi^{- 1}{(\eta)}{\parallel\mathbf{\Sigma}^{\frac{1}{2}}{\mathbf{p}}\parallel}_{2} \leq 0}$}. (c) Motion planning problem in the presence of 4 scaled and rotated rectangular obstacles.

### V-B Motion planning and MPC on planar push

Non-prehensile manipulation has been widely studied as a challenging task for model-based planning and control, with the pusher-slider system as one of the most prominent examples \[(https://arxiv.org/html/2506.14865v1#bib.bib21)\] (see [Fig. 6](https://arxiv.org/html/2506.14865v1#S5.F6 "In V-B Motion planning and MPC on planar push ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")). The reasons include hybrid dynamics with various interaction modes, underactuation and contact uncertainty. In this experiment, we study motion planning and MPC on this planar push system, without any constraints, to compare to a standard iLQR implementation. The cost function includes the control effort and the $L2$ norm measuring the difference between the final and target configurations. [Fig. 6(b)](https://arxiv.org/html/2506.14865v1#S5.F6.sf2 "In Fig. 6 ‣ V-B Motion planning and MPC on planar push ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") illustrates the cost convergence for iLQR and ALSPG across 10 different targets for statistical analysis. Although iLQR seems to converge to medium accuracy faster than ALSPG, because of the difficulties in the task dynamics, it seems to get stuck at local minima very easily. On the other hand, ALSPG performs better in terms of variance and local minima. We applied MPC with iLQR and ALSPG with a horizon of 60 timesteps and stopped the MPC as soon as it reached the goal position with a desired precision. [Table III](https://arxiv.org/html/2506.14865v1#S5.T3 "In V-B Motion planning and MPC on planar push ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") shows this comparison in terms of convergence time (s), number of function evaluations and number of Jacobian evaluations. According to these findings, ALSPG performs better than a standard iLQR, even when there are no constraints in the problem.

Num. of fun. eval.
Num. of Jac. eval.

TABLE III: Comparison of MPC with iLQR and ALSPG for planar push.

(a) Pusher-slider system path optimized by the proposed algorithm to go from the state to (0.1,0.1,π/3). Optimal control solved with SPG results in a smooth path for the pusher-slider system.

(b) Convergence error mean and variance plot for iLQR and ALSPG motion planning algorithm for 10 different goal conditions starting from the same initial positions and control commands.

Figure 6: ALSPG algorithm applied to a pusher-slider system.

### V-C Motion planning with obstacle avoidance

Num. of fun. eval.
Num. of Jac. eval.

ALSPG with Proj.

SLSQP with Proj.

ALSPG without Proj.

TABLE IV: Comparison of MPC with iLQR and ALSPG for planar push.

Obstacle avoidance problems are usually described using geometric constraints. In autonomous parking tasks, obstacles and cars are usually described as 2D rectangular objects. In this experiment, we take a 2D double integrator point car reaching a target pose in the presence of rectangular obstacles (see [Fig. 5(c)](https://arxiv.org/html/2506.14865v1#S5.F5.sf3 "In Fig. 5 ‣ V-A Inverse kinematics ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")). We apply the ALSPG algorithm with and without projections to illustrate the main advantages of having an explicit projection function over direct constraints. The main difference is without projections, the solvers need to compute the gradient of the constraints, whereas with projections, this is not necessary. In order to understand the differences between first-order and second-order methods, we also compared ALSPG-Proj to AL-SLSQP with projections (SLSQP-Proj.), which is the same algorithm except the subproblem is solved by a second-order solver SLSQP from Scipy \[(https://arxiv.org/html/2506.14865v1#bib.bib22)\]. The box obstacles allow analytical projections and distance computation. We performed 5 experiments, each with different settings of 4 rectangular obstacles and compared the convergence properties. The results are given in [Table IV](https://arxiv.org/html/2506.14865v1#S5.T4 "In V-C Motion planning with obstacle avoidance ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"). The comparison, with and without projections, reports a clear advantage of using projections instead of plain constraints in the convergence properties. Although the convergence time comparison is not necessarily fair for SPG implementations as the SLSQP solver calls C++ functions, the comparison of ALSPG-Proj. and SLSQP-Proj. shows that ALSPG-Proj. still achieves lower convergence time. Additionally, we compare it against the optimization-based collision avoidance (OBCA) algorithm \[(https://arxiv.org/html/2506.14865v1#bib.bib23)\] that is based on distance computation and IPOPT. The bicycle model is used ${{\overset{˙}{c}}_{x} = {v{\cos\theta}}},{{{\overset{˙}{c}}_{y} = {v{\sin\theta}}},{{\overset{˙}{\theta} = {\frac{v}{L}{\tan\delta}}},{\overset{˙}{v} = a}}}$. where $L = 2.7$ m is the wheelbase length. The system control inputs ${\mathbf{u}} = \lbrack\delta,a\rbrack$. Other parameters remain the same as the baseline. As shown in Table [V](https://arxiv.org/html/2506.14865v1#S5.T5 "Table V ‣ V-C Motion planning with obstacle avoidance ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"), the results further validate the efficiency of our approach.

TABLE V: Comparison between IPOPT and ALSPG on 100 random parking tests.

### V-D Autonomous Navigation on a 1:10 Scale Car

To further assess the effectiveness of our approach, we tested the ALSPG algorithm on a 1:10 scale vehicle executing a navigation task. The experiment was conducted on a 1:10 car, using an Intel ProU7 as the onboard computer. The sensor suite includes a Hokuyo UST-10LX LiDAR with a maximum scan frequency of 40 Hz. Odometry is provided by the VESC. Sensor fusion combines data from the LiDAR, the IMU embedded in the VESC, and odometry, utilizing the Cartographer to localize the vehicle and obtain its state. A pure-pursuit controller is implemented to track the given trajectory. The projections are constructed through polytopic projections and convex decomposition from section [IV](https://arxiv.org/html/2506.14865v1#S4 "IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"). The results shown in Fig. (https://arxiv.org/html/2506.14865v1#S5.F7 "Fig. 7 ‣ V-D Autonomous Navigation on a 1:10 Scale Car ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization") demonstrate the effectiveness of our method.

Figure 7: ALSPG: Navigation snapshots in an obstacle-cluttered environment. a) The car enters the passage. b) The car avoids non-convex and triangular obstacles. c) A box-shaped obstacle blocks the left side. d-e) The car navigates avoiding the box obstacle to reach the goal.

### V-E MPC for Real-Time Tracking on 7-axis Manipulator

Figure 8: Error in the objective and the squared norm of the box constraint value during 1 min execution of MPC on Franka robot.

Figure 9: MPC setup for tracking an object subject to box constraints.

We tested the ALSPG algorithm on the MPC problem of tracking an object with box constraints on the end-effector position of a Franka robot (see [Fig. 9](https://arxiv.org/html/2506.14865v1#S5.F9 "In V-E MPC for Real-Time Tracking on 7-axis Manipulator ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")). An Aruco marker on the object is tracked by a camera held by another robot. In this experiment, the goal is to show the real-time applicability of the proposed algorithm for a constrained problem in the presence of disturbances. In [Fig. 8](https://arxiv.org/html/2506.14865v1#S5.F8 "In V-E MPC for Real-Time Tracking on 7-axis Manipulator ‣ V Experiments ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"), the error of the constraints and the objective function using formulation ((https://arxiv.org/html/2506.14865v1#S4.E8 "Eq. 8 ‣ IV-C Optimal Control with ALSPG ‣ IV Augmented Lagrangian Spectral Projected Gradient Descent for Robotics ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization")) is given for 1 min. time period of MPC with a short horizon of 50 timesteps. Between 20s and 30s, the robot is disturbed by the user thanks to the compliant torque controller run on the robot. We can see that the algorithm drives smoothly the error to zero, see the accompanying video.

### V-F Chess Robot

We validated our algorithm through a three-month experimental study using a 6-axis P-Rob robot from F$\&$P Robotics to solve an inverse kinematics problem (position and orientation) with one degree of freedom (DoF) in orientation left unconstrained. The task involved grasping chess pieces, where the robot autonomously determined its orientation around the z-axis using SPG, compensating for workspace limitations that prevented full 6-DoF positioning, as shown in Fig. (https://arxiv.org/html/2506.14865v1#S1.F1 "Fig. 1 ‣ I Introduction ‣ Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization"). The quaternion error, expressed via log-mapping, introduced nonlinearity and complexity, while joint limit projections ensured feasibility. After three months of public demonstrations, the system achieved a $100\%$ success rate.

## Conclusion

In this work, we presented a fast first-order constrained optimization framework based on geometric projections, and applied it to various robotics problems ranging from inverse kinematics to motion planning. We showed that many of the geometric constraints can be rewritten as a logical combination of geometric primitives onto which the projections admit analytical expressions. We built an augmented Lagrangian method with spectral projected gradient descent as a subproblem solver for constrained optimization. We demonstrated: 1) the advantages of using projections when compared to setting up the geometric constraints as plain constraints with gradient information to the solvers; and 2) the advantages of using spectral projected gradient descent based motion planning compared to a standard second-order iLQR and IPOPT algorithm through different robot experiments. Sample-based MPC have been increasingly popular in recent years thanks to their fast practical implementations, despite their lack of theoretical guarantees. In contrast, second-order methods for MPC require a lot of computational power but with somewhat better convergence guarantees. We argue that ALSPG, being already in between these two methodologies in terms of these properties, promises great future work to combine it with sample-based MPC to further increase its advantages on both sides.
