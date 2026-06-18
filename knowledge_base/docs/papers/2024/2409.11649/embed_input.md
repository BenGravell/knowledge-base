<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Second-Order Constrained Dynamic Optimization

Topics include Differential dynamic programming, Second-order methods, Constrained optimization, Trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Comparative study over the variations of differential dynamic programming for constrained trajectory optimization problems, including interior-point, augmented Lagrangian, primal-dual, and sequential quadratic programming techniques.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper provides an overview, analysis, and comparison of second-order dynamic optimization algorithms, i.e., constrained Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP). Although a variety of these algorithms have been proposed and used successfully, there exists a gap in understanding the key differences and advantages, which we aim to provide in this work. For constrained DDP, we choose methods that incorporate nonlinear programming techniques to handle state and control constraints, including Augmented Lagrangian (AL), Interior Point, Primal-Dual Augmented Lagrangian (PDAL), and Alternating Direction Method of Multipliers (ADMM). Both DDP and SQP are provided in single- and multiple-shooting formulations, where constraints that arise from dynamics are encoded implicitly and explicitly, respectively. As a byproduct of the review, we propose a single-shooting PDAL DDP that has more favorable properties than the standard AL variant, such as the robustness to the growth of penalty parameters. We perform extensive numerical experiments on a variety of systems with increasing complexity to investigate the quality of the solutions, the levels of constraint violation, and the sensitivity of final solutions with respect to initialization, as well as targets.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The results show that single-shooting PDAL DDP and multiple-shooting SQP are the most robust methods. For multiple-shooting formulation, both DDP and SQP can enjoy informed initial guesses, while the latter appears to be more advantageous in complex systems. It is also worth highlighting that DDP provides favorable computational complexity and feedback gains as a byproduct of optimization as is.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second-order dynamic optimization methods are powerful optimization techniques used for optimal control of systems with nonlinear dynamics and non-quadratic cost functions. Dynamic systems with these characteristics can be found in robotics, aerospace and transportation systems, economics, biology and computational neuroscience, etc. There exist two main families of methods for dynamic optimization, namely Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP). Both approaches are iterative and rely on first/second-order approximations of the dynamics and the cost computed along the trajectories corresponding to each iteration. This paper provides an in-depth overview of how state and control constraints are incorporated into second-order dynamic optimization algorithms. Such constraints appear in almost all applications of trajectory optimization and iterative optimal control methods (Tassa et al. Howell et al., ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

Using Bellman's principle of optimality, dynamic programming (DP) divides the original optimization problem into a sequence of smaller subproblems at each time step. Nevertheless, DP is known to suffer from "curse of dimensionality" because its computational and memory demands explode as the dimension of the problem increases. DDP solves this issue by considering a local approximation around the nominal trajectory. Moreover, DDP can implicitly satisfy dynamic constraints thanks to its backward and forward nature. Furthermore, DDP provides feedback gains as a byproduct of optimization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

In practical applications, state and control constraints are of great importance. These include actuation limits and obstacles in robotics and autonomy, flow constraints in transportation systems, and positivity constraints in biology and computational neuroscience. To handle these constraints, variants of DDP have been extensively studied in the literature. In early work, active constraints were captured in the value and state-action $Q$ function during the backward pass of DDP. In the same spirit, control-limited DDP was proposed by Tassa et al., which can strictly satisfy the box control constraints by solving a Quadratic Programming (QP) in the backward pass. This method sets the feedback gains to zero when the nominal control sequence hits the control limit. As a result, these gains are not as reliable as those of normal DDP. As an extension, Xie et al. presented both state- and control-constrained DDP. This method solves a similar QP with a trust region in the forward pass to surely satisfy the constraints. Consequently, the algorithm discards the feedback gains obtained in the backward pass. Moreover, due to the trust region, a good initial guess is required to achieve a task.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

Another approach to handling constraints is applying Nonlinear Programming (NLP) techniques to DDP. This includes the penalty barrier (Frisch Fiacco and McCormick., ), Augmented Lagrangian (AL) (D. Hestenes, ), Interior Point (IP) (Byrd et al. Wächter and Biegler ), Primal-Dual Augmented Lagrangian (PDAL) (Gill and Robinson Robinson, ), and Alternating Direction Method of Multipliers (ADMM). We note that these techniques can be used to solve dynamic optimization for robotic applications, such as Vanroye et al..

<!-- chunk {"id": "body-0009", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

The combination of DDP and the $\log$ barrier penalty method was proposed in Grandia et al., where the barrier function is relaxed to allow constraint violations. The penalty function's coefficient, known as a penalty parameter, is driven to zero in the original formulation but is fixed in this DDP approach. Almubarak et al. uses a similar approach with an exact barrier function. Despite these approximations, they are shown to work sufficiently well in practice. AL DDP is the most widely used among these combinations of NLP with DDP for inequality constraints (Plancher et al. Pellegrini and Russell, ) and equality constraints. The method is quite robust in terms of cost reduction, but it can violate constraints especially in the early stage of optimization, where Lagrangian multipliers are inaccurate or penalty parameters are not large enough. Moreover, it can take many iterations to achieve strict feasibility. To alleviate this problem, the researchers proposed extensions in which algorithms switch from AL DDP to other methods when a trajectory approaches convergence (Lantoine and Russell Howell et al. Aoyama et al., ).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

IP DDP optimizes control variables, Lagrangian multipliers, and slack variables as the original IP method using DDP. PDAL DDP was proposed most recently. This method is similar to the AL DDP, but the Lagrangian multipliers are also optimized using DDP in contrast to the AL variant.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

Both AL and PDAL use penalty parameters that are increased during optimization. In AL, large penalty parameters are known to interrupt optimization, whereas PDAL is more robust to them as described in Robinson. The PDAL DDP is presented in multiple-shooting formulation, which we elaborate on in the next paragraph. Using the Alternating Direction Method of Multipliers (ADMM), several variations of constrained DDP have been presented such as in Sindhwani et al.; Zhou and Zhao, which split the problem into smaller subproblems that are solved sequentially. Distributed ADMM-based DDP algorithms have also been proposed for handling constrained multi-agent control problems by utilizing the parallelizable nature of ADMM (Saravanos et al. Huang et al., ).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

In DDP, there exist single- and multiple-shooting formulations, which are named after the work by Bock and Plitt. Single-shooting DDP is a normal DDP whose decision variables are the control sequence of the system. In this formulation, the constraints of dynamics are implicitly satisfied. On the other hand, in the multiple-shooting variant, the dynamics are handled as equality constraints or residuals that can be violated. This property allows users to initialize the algorithm with good initial guesses in both the state and control trajectories. There exist two types of multiple-shooting DDPs. In the first type, the constraints from dynamics are encoded as part of the objective and captured by the state-action $Q$ function of DDP (Jallet et al.; Pellegrini and Russell; Jallet et al. ). This type has both state and control of the system as decision variables. In the second type, the constraints are not absorbed in the cost but handled separately as residuals and the decision variables are control sequence as the single-shooting (normal) DDP.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Differential Dynamic Programming", "weight": 1.0} -->

Giftthaler et al. first introduced this formulation with residuals using a linear update law of dynamics in both the state and the control. Mastalli et al. further analyzed and improved the method with a nonlinear update law to solve complex tasks with high-dimensional dynamics, such as the dynamic maneuver of robots with contacts. Mastalli et al. introduced a control limit to the method. Although these methods can successfully handle complex dynamics, state constraints, such as obstacles, are not presented in contrast to the first type.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sequential Quadratic Programming", "weight": 1.0} -->

SQP was introduced as a constrained optimization technique in Wilson, showing its power in many fields including robotics (Yunt and Glocker Yunt Kuindersma et al. Posa et al., ), aerospace (Kenway and Martins Kamyar and Taheri, ) and chemical engineering. The approach relies on sequentially solving QP subproblems with quadratically approximated objectives and linearized constraints, generating new nominal trajectories. For dynamical systems, SQP encodes the constraints that arise from linearized dynamics at every time step as equality constraints. SQP also has single-shooting and multiple-shooting formulations. The multiple-shooting variant has state and controls as decision variables. The single-shooting variant has some variations. It can be achieved by solving the same subproblem as the multiple-shooting variant and propagating the state using the system's dynamics. A technique called condensing can also be used to eliminate the state variables from the subproblems. There exists a significant amount of SQP variants that have been proposed in the literature recently for nonlinear optimal control and model predictive control (MPC).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sequential Quadratic Programming", "weight": 1.0} -->

One of the main difficulties of the SQP approach was its computational demands to solve QP subproblems. To alleviate this problem Pantoja and Mayne proposed a stage-wise version of SQP under control inequality constraints. In the same spirit of DDP, this approach solves smaller subproblems at every time step, rather than solving a problem for a whole time horizon. Another approach for improving the time complexity is to exploit the special sparse structure of the constraints arising from dynamics while solving QP. The growth of computational complexity with respect to time horizon can be reduced from cubic to linear, which is as good as DDP. This approach was proposed with active-set, IP, and barrier methods. The same reduction is achieved by Riccati-based recursion for Linear Quadratic Regulator (LQR) problems (Dohrmann and Robinett Rao et al. Jørgensen et al., ). Note that this technique is available only for multiple-shooting SQP because the sparse structure is lost by condensing. It is worth noting that the recursion provides feedback gains as byproducts, as in DDP, although the gains have not been actively used.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sequential Quadratic Programming", "weight": 1.0} -->

In the single-shooting variant, rather than working on the complexity, Singh et al. incorporates the DDP-style closed loop rollout, achieving a faster convergence speed. Recently, Jordana et al. proposed an approach similar to the multiple-shooting SQP, showing its superiority over single- and multiple-shooting DDPs in tasks without state constraints. This work uses LQR and ADMM to solve QP subproblems efficiently and to enforce constraints. Inspired by Stellato et al., the matrices used in QP are not updated every iteration to improve computational efficiency.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Other Methods", "weight": 1.0} -->

The most straightforward approach for dynamic optimization is collocation methods, which discretize the problem in time and treat (possibly nonlinear) dynamics as equality constraints. The discretization process and the time step, where equality constraints are applied, are known as transcription and collocation points, respectively. Any solver can be used to solve the transcribed problem. Since the method does not have any requirements for the representation of dynamics, such as an integration scheme, it is less restrictive than those we present in this paper. However, a naive implementation does not scale well with the size of the problem. This paper focuses on methods that can take advantage of the problem structure in dynamic optimization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contribution", "weight": 1.0} -->

Although DDP and SQP have a wealth of literature separately, there exist only few works comparing the two approaches. In the unconstrained case - where SQP coincides with Newton's method with line search - the early works by Liao and Shoemaker; Murray and Yakowitz had made a comparison of the two approaches. DDP was noted to have the same quadratic convergence properties as Newton's method, but with the advantage of solving linear equations whose size remains constant w.r.t. the time horizon. However, given the variety of constrained DDP methods available, a thorough comparison of how these methods compare with SQP-based methods is still missing. A comparison between AL DDP and an SQP-based solver SNOPT has been made in Howell et al., where SQP was shown to converge slower in wall clock time. Sindhwani et al., compared ADMM DDP with control-limited DDP Tassa et al. and SQP under only control constraints. Xie et al. also compared their constrained DDP and SQP (SNOPT) using state and control constrained robotic tasks under a time budget, showing the superiority of DDP.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contribution", "weight": 1.0} -->

However, the details of SQP, including single- or multiple-shooting etc., are not presented.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contribution", "weight": 1.0} -->

To better understand the modern landscape of algorithms and how they relate to each other and the optimization literature, we compare these algorithms from derivations to performance in this paper. In addition, we propose single-shooting PDAL DDP that inherits the merit of PDAL over AL, that is, the robustness to the large penalty parameter, and add it to the comparison.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contribution", "weight": 1.0} -->

Our thorough numerical experiments with simple to complex dynamical systems reveal the difference of the algorithms in terms of the quality of solutions, the levels of constraint violation, iterations for convergence, and the sensitivity of the final solutions with respect to initialization. The results indicate that DDP frequently shows its capability to find better local minima, whereas SQP generally performs better in satisfying constraints. It is also shown that although both DDP and SQP have multiple-shooting formulations that can enjoy informed initial guesses, the SQP variant tends to work more reliably in complex systems. Furthermore, our analysis shows that single-shooting DDPs can offer lower computational complexity, especially when the system is underactuated and the problem has a long time horizon. This computational efficiency is one of the main motivations for users to choose DDP.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Contribution", "weight": 1.0} -->

We summarize the different methods we discuss in Table. In the table, Single and Multi. represent the single and multiple shooting formulation. $✓$ and $-$ indicate whether the property is satisfied or not. For the satisfaction of the constraints, $✓$ indicates that the constraints may be violated during optimization but eventually satisfied upon convergence. In contrast, $✓✓$ means that the trajectory is always feasible even before convergence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contribution", "weight": 1.0} -->

This work is organized as follows: section includes an overview of nonlinear programming optimization techniques for static problems, including $\log$ barrier, AL, IP, PDAL, ADMM, and SQP. In section, we review unconstrained DDP. Section provides the derivation of constrained DDP techniques, and section gives the SQP approach for dynamic optimization. Section analyzes time complexity of the algorithms. Section presents the results of numerical experiments to compare dynamic optimization algorithms. Finally, the conclusion is drawn in section.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Contribution", "weight": 1.0} -->

There exist infeasible (✓) and feasible (✓ ✓) formulations in Pavlov et al.. We modify the infeasible one due to its better performance.
We modify the line-search filter in section 4.3.
Proposed in this paper.
When proper method is used as mentioned in section 1.2 and 5.2.
Although there exist multiple variants, here we use single-shooting with condensing. It cannot enjoy the reduction available in the multiple-shooting variant but can be reduced from N3 m3 to N2 m3.
Originally N3 (n+m)3, but the dependency on N can be reduced to linear with the sparse structure as mentioned in section 1.2 and 5.2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Nonlinear Programming Preliminaries", "weight": 1.0} -->

In this section, we review NLP methods for static optimization problems that are relevant to DDP and SQP variations for constrained dynamic optimization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Log Barrier methods", "weight": 1.0} -->

Consider the constrained optimization problem

<!-- chunk {"id": "body-0027", "role": "body", "section": "Log Barrier methods", "weight": 1.0} -->

where $f_{0}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and $g:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{w}}$. Barrier methods solve the problem above by minimizing a sequence of new objectives that are a sum of the original objective and a barrier function associated with the constraints. Barrier functions are parameterized by a scalar nonnegative penalty (barrier) parameter $\mu$ Frisch; Fiacco and McCormick.. Here, we consider a logarithmic barrier function and a new objective denoted by $\mathcal{P}$ as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Log Barrier methods", "weight": 1.0} -->

Observe that $\mathcal{P}$ increases as $g{(x)}$ gets closer to the boundary of constraints and becomes infinity when ${g{(x)}} \geq 0$. Thus, this method can only handle inequality constraints. The function $\mathcal{P}{(x;\mu)}$ is minimized over $x$ iteratively with a fixed $\mu$ through Newton's method. A new $x$ is obtained as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Log Barrier methods", "weight": 1.0} -->

where $\deltax^{\ast}$ is the solution of Newton's method and $\alpha \in {(0,1\rbrack}$ is a step size which reduces the penalty function. By ensuring that the cost is finite, the constraints remain satisfied for all iterations. After each update of $x$, $\mu$ is reduced to make the minimizer of $\mathcal{P}$ closer to the true minimizer of.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Log Barrier methods", "weight": 1.0} -->

The Hessian of the penalty function $\mathcal{P}$ used in Newton's method is given by

<!-- chunk {"id": "body-0031", "role": "body", "section": "Log Barrier methods", "weight": 1.0} -->

which is required to be Positive Definite (PD). In the Hessian, the first term $\nabla_{xx}f_{0}$ is PD when the objective $f_{0}{(x)}$ is convex, and the third term is Positive SemiDefinite (PSD) by construction. However, the second term may not be. By eliminating the second term, we guarantee a PD approximation of the Hessian of $\mathcal{P}$, which corresponds to the Gauss-Newton (GN) approximation of the Hessian.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

Consider an optimization problem similar to, but with equality constraints explicitly included

<!-- chunk {"id": "body-0033", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

where $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{W}}$. The Powell-Hestenes-Rockafellar (PHR) augmented Lagrangian (D. Hestenes Rockafellar, ) is given as follows,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

where $\lambda \in {\mathbb{R}}^{w}$ and $\nu \in {\mathbb{R}}^{W}$ are Lagrange multipliers associated with the inequality and equality constraints, respectively. Here, the penalty parameters $\rho_{I}$ and $\rho_{E}$ can be scalar or vectors of size ${\mathbb{R}}^{w}$ and ${\mathbb{R}}^{W}$, respectively - the latter is used for generality. We denote ${\lbrack \cdot \rbrack}_{+}$ as the projection to the nonnegative orthant, i.e.,

<!-- chunk {"id": "body-0035", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

The AL method has an inner and an outer loop. In the inner loop, $\mathcal{L}_{A}$ is minimized over $x$ with fixed penalty parameters and Lagrangian multipliers, until $\left\| {\nabla\mathcal{L}_{A}} \right\| \leq \epsilon_{AL}$ is achieved, where $\epsilon_{AL}$ is a prescribed tolerance. Since the inner loop problem is a minimization problem of $\mathcal{L}_{A}$ on a single variable $x$, DDP can be easily used. In the outer loop, the Lagrangian multipliers are updated based on the constraint satisfaction and optimality conditions. The gradient and Hessian of $\mathcal{L}_{A}$ are given by

<!-- chunk {"id": "body-0036", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

The subscript $\mathcal{A}$ denotes the projection onto the coordinates corresponding to the active constraints, that is, elements of the indices where is positive. The update laws for multipliers $\lambda_{i},\nu_{j}$ are

<!-- chunk {"id": "body-0037", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

which are obtained by comparing the gradient of $\mathcal{L}_{A}$ and that of the (normal) Lagrangian $\mathcal{L} = {{f_{0}{(x)}} + {\lambda^{\mathsf{T}}g{(x)}} + {\nu^{\mathsf{T}}h{(x)}}}$. The penalty parameters $\rho$ are increased if the constraint satisfaction after the inner loop is not satisfactory, determined by a tolerance for constraint satisfaction $\eta_{I}$ as below.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Augmented Lagrangian methods", "weight": 1.0} -->

with $\beta > 1$. The parameter $\rho_{E}$ follows the similar law where it is updated when $\left\| {h{(x)}} \right\| \geq \eta_{E}$. The tolerance for the inner loop $\epsilon_{AL}$ starts at a moderate value and decreases as the optimization progresses to avoid local minima. This is because convergence with small penalty parameters and suboptimal multipliers does not lead to an optimal solution of the original problem. Moreover, too many iterations with these parameters may get the algorithm "trapped" at poor local minima, e.g., a small objective with a significant constraint violation. When inner loop minimization is successful, that is, the constraint violation is sufficiently small after the inner loop, $\epsilon_{AL}$ is reduced to allow for more inner loop iterations. Otherwise, the tolerance is kept, reset, or conservatively reduced. The constraint satisfaction tolerance $\eta$ is updated in a similar manner.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

Consider the problem. Introducing the slack variable $s \in {\mathbb{R}}^{w}$, the problem is reformulated as

<!-- chunk {"id": "body-0040", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

The KKT conditions for the problem in are given by

<!-- chunk {"id": "body-0041", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

Note that (10a) is derived from the original problem, not from the one with slack variables. The complementary slackness (10b) is relaxed by the parameter $\mu$, i.e., ${s_{i}\lambda_{i}} = {\mu\mspace{7mu}{({> 0})}}$. The parameter biases $s$ and $\lambda$ toward the feasible region, i.e., ${s_{i},\lambda_{i}} \geq 0$, which is known as the central path. The relaxed condition of can also be obtained by adding constraints for $s$ to the objective, forming a modified problem

<!-- chunk {"id": "body-0042", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

similar to. The equality constraint ${{g{(x)}} + s} = 0$ can be violated during the optimization process as long as $s \geq 0$ unlike the log barrier method. Thus, can be seen as a relaxation of it. By applying Newton's method, the primal-dual system is obtained as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

where $S = {{diag}{\lbrack s\rbrack}}$, $\overline{\Lambda} = {{diag}{\lbrack\lambda\rbrack}}$, and $e = {\lbrack 1,\cdots,1\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{w}$. To guarantee that the direction obtained by solving is a descent direction, the matrix on the LHS, called primal-dual matrix, must have $n + w$ positive, $w$ negative, and no zero eigenvalues. When this condition is not met, the matrix can be modified, the details of which are found in Nocedal and Wright; Wächter and Biegler. As in AL, optimization is performed iteratively by solving and updating the decision variables via

<!-- chunk {"id": "body-0044", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

where the maximum step sizes $\alpha_{s}$ and $\alpha_{\lambda}$ are given by the fraction-to-the-boundary rule,

<!-- chunk {"id": "body-0045", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

where $\tau\mspace{7mu}{({\leq 0.995})}$ is a constant. $\alpha_{\lambda}$ is used directly to update $\lambda$. For $s$ and $x$, after determining the maximum step size, a backtracking line search is performed until both sufficient cost reduction and constraint satisfaction are achieved using a filter formed by a modified objective in and constraint violation $\left\| {{g{(x)}} + s} \right\|$. After the update, a new problem is solved. This process is repeated until the norm on the RHS of is smaller than some predetermined tolerance $\epsilon_{IP}$, that is,

<!-- chunk {"id": "body-0046", "role": "body", "section": "Interior Point methods", "weight": 1.0} -->

When the condition above is satisfied, $\mu$ is reduced for the next iteration, making the relaxed complementary slackness close to the actual one. There is an important mechanism implemented in IP-based packages such as IPOPT Wächter and Biegler, which is known as feasibility restoration. When the line search cannot find an acceptable step size, even when the candidate step is smaller than a threshold, the feasibility restoration phase is invoked. In this phase, the algorithm focuses on minimizing infeasibility to find a solution that the filter can accept.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Primal-Dual Augmented Lagrangian methods", "weight": 1.0} -->

In this section, we first introduce PDAL (Gill and Robinson Robinson, ) and its formulation with slack variables. Then, we outline a method for reducing the slack variables from the objective, namely PDAL.

<!-- chunk {"id": "body-0048", "role": "body", "section": "PDAL with slack variables", "weight": 1.0} -->

Consider the problem with constraints ${h{(x)}} = 0$ as. The Primal-Dual Augmented Lagrangian (PDAL) with slack variables is given by

<!-- chunk {"id": "body-0049", "role": "body", "section": "PDAL with slack variables", "weight": 1.0} -->

where $\lambda_{e}$ and $\nu_{e}$ are Lagrangian multiplier estimates for $\lambda$ and $\nu$ respectively. We take $\mu_{I} = {1/\rho_{I}}$ and $\mu_{E} = {1/\rho_{E}}$ as scalars for simplicity, but they can also be vectors of the corresponding size. Note that PDAL penalizes not only the violation of constraints but also the deviation of multipliers from the trajectory of the minimizers. Therefore, PDAL $\mathcal{L}_{PD}$ is minimized for all variables, including Lagrangian multipliers, in contrast to simple AL, where the inner loop performs optimization with fixed multipliers. We now wish to minimize $\mathcal{L}_{PD}$ for $x,s,\lambda,\nu$. For this purpose, we first obtain the optimal $s$ denoted by $s^{\ast}$ for other variables.

<!-- chunk {"id": "body-0050", "role": "body", "section": "PDAL with slack variables", "weight": 1.0} -->

To keep the notation simple and compact, we only consider inequality constraints during the derivation of $s^{\ast}$, reducing $\mu_{I}$ and $\mu_{E}$ to $\mu$. Since the equality constraint terms are not affected by $s$, the complete form with inequalities is easily recovered after computing $s^{\ast}$. Completing the square of $\mathcal{L}_{PD}$ in terms of $s$ yields

<!-- chunk {"id": "body-0051", "role": "body", "section": "PDAL with slack variables", "weight": 1.0} -->

From this form, $s^{\ast}$ is obtained as

<!-- chunk {"id": "body-0052", "role": "body", "section": "PDAL with slack variables", "weight": 1.0} -->

Plugging this back in (without equality constraint terms) gives the PDAL without $s$ as

<!-- chunk {"id": "body-0053", "role": "body", "section": "Minimization of PDAL", "weight": 1.0} -->

As in the case of AL, PDAL method also has an inner and an outer loop. In the inner one, $L_{PD}$ is minimized over $x$, $\lambda$, and $\nu$ with fixed $\lambda_{e}$, $\nu_{e}$ and $\mu$. In the outer loop, $\lambda_{e}$ and $\nu_{e}$ are updated. The parameter $\mu$ ($\rho$) is monotonically decreased (increased) when the constraint violation is not satisfactory. Newton's method minimizes PDAL in the inner loop as other methods. In the optimization process, systems of equations

<!-- chunk {"id": "body-0054", "role": "body", "section": "Minimization of PDAL", "weight": 1.0} -->

is iteratively solved. Here, the active constraints denoted by $\mathcal{A}$ is similar to the case of AL, but with

<!-- chunk {"id": "body-0055", "role": "body", "section": "Minimization of PDAL", "weight": 1.0} -->

The matrix on the LHS becomes numerically unstable as $\mu$ in the denominators becomes small. This instability can be alleviated by the transformation given in the original work Robinson. Considering the gradient of the Lagrangian $\mathcal{L} = {f_{0} + {\lambda_{e}^{\mathsf{T}}g} + {\nu_{e}^{\mathsf{T}}h}}$, and that of $\mathcal{L}_{PD}$, ${\lbrack{{2\pi_{I}} - \lambda}\rbrack}_{+}$ and ${2\pi_{E}} - \nu$ can be seen as a new estimate of Lagrangian multipliers, which gives the update law of multipliers in the outer loop as

<!-- chunk {"id": "body-0056", "role": "body", "section": "Alternating Direction Method of Multipliers", "weight": 1.0} -->

Consider the following optimization problem

<!-- chunk {"id": "body-0057", "role": "body", "section": "Alternating Direction Method of Multipliers", "weight": 1.0} -->

Here, we have two sets of variables $x$, $z$. ADMM iteratively minimizes the objective by minimizing the Augmented Lagrangian

<!-- chunk {"id": "body-0058", "role": "body", "section": "Alternating Direction Method of Multipliers", "weight": 1.0} -->

where $\lambda$ is a Lagrangian multiplier. The optimization process is performed by repeating the following three updates.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Alternating Direction Method of Multipliers", "weight": 1.0} -->

where $l$ in the superscripts of variables indicates $l$ th iteration. The violation of the constraint given by $r^{l}$ above is also known as the primal residual. The dual residual $d$ is derived from the first order optimality condition of (23a)

<!-- chunk {"id": "body-0060", "role": "body", "section": "Alternating Direction Method of Multipliers", "weight": 1.0} -->

As in other methods, the penalty parameter $\rho$ can be updated during optimization. However, the update is not based on the constraint violation, but on the relationship of the primal and dual residuals. When the primal feasibility is greater than the dual counterpart, $\rho$ is increased to make the relative significance of constraint violation higher in $\mathcal{L}_{A}$. On the other hand, when the dual residual is higher, $\rho$ is decreased to prioritize the optimality of the original objective.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Sequential Quadratic Programming", "weight": 1.0} -->

Consider, again. SQP transforms this problem to a QP with linearized constraints around current $x$, yielding

<!-- chunk {"id": "body-0062", "role": "body", "section": "Sequential Quadratic Programming", "weight": 1.0} -->

where $H$ is Hessian of Lagrangian $\mathcal{L}$, i.e., $\mathcal{L} = {{f_{0}{(x)}} + {\lambda^{\mathsf{T}}g{(x)}}}$, and $H = {\nabla_{xx}\mathcal{L}}$. In practice, an approximation of $H$ is used instead of the exact one. $H$ is required to be PD as in other methods. is known as a QP subproblem, whose solution is used to update $x$ with a step size $\alpha$. The updated $x$ leads to a new QP subproblem. SQP repeats solving the QP subproblem and updating $x$ sequentially.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sequential Quadratic Programming", "weight": 1.0} -->

To find an appropriate step size $\alpha$, AL is used as a merit function that achieves cost reduction and constraint satisfaction. Since SQP solves QP under linearized constraints, it may violate the original constraints if it attempts a large $\alpha$. The detailed derivation of the SQP based on Gill et al. is provided in the appendix B.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

This section provides a brief review of the derivation and implementation of unconstrained DDP. More details can be found in Jacobson and Mayne. Consider the discrete-time optimal control problem

<!-- chunk {"id": "body-0065", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

where $x_{k} \in {\mathbb{R}}^{n}$, $u_{k} \in {\mathbb{R}}^{m}$ denote the state and control input of the system at the time instant $t_{k}$, respectively, and $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ corresponds to the transition dynamics function. The scalar-valued functions $l$, $\Phi$, $J$ denote the running, terminal, and total cost of the problem, respectively. We also let

<!-- chunk {"id": "body-0066", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

be the state and control trajectory over the horizon $N$. The cost-to-go at time $k = i$, i.e., the cost starting from $k = i$ to the end of the time horizon $N$ is given by

<!-- chunk {"id": "body-0067", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

Note that the value function is a function of $x_{k}$ due to the minimization with respect to $U_{k}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

The DDP algorithm finds locally optimal solutions to by expanding both sides of around given nominal trajectories, $\overline{X}$, $\overline{U}$. Specifically, let us define the $Q$ function as the argument of $\min$ on the RHS of,

<!-- chunk {"id": "body-0069", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

If we take quadratic expansions of both sides of, then the LHS expansion around ${\overline{x}}_{k}$, ${\overline{u}}_{k}$ gives

<!-- chunk {"id": "body-0070", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

Mapping the terms of both sides of the expanded gives

<!-- chunk {"id": "body-0071", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

where $\cdot$ in the second-order terms is tensor contraction along the first dimension. After plugging and into, we can explicitly optimize the value function with respect to $\deltau_{k}$ by taking a partial derivative and setting it to zero, obtaining the locally optimal control update

<!-- chunk {"id": "body-0072", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

where $\kappa_{k}$ and $K_{k}$ are known as feedforward and feedback gains, respectively. Note that we have dropped the time indices for $Q$ to lighten the notation. To ensure convergence, $Q_{uu}$ must be regularized when it is not PD, which is achieved with

<!-- chunk {"id": "body-0073", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

This is equivalent to adding a cost that penalizes a large $\deltau_{k}$. Observe that $\deltau_{k}^{\ast}$ is computed using $V_{x,{k + 1}}$ and $V_{{xx},{k + 1}}$. To propagate these back in time, we plug the minimizer of, i.e., $u_{k}^{\ast}$ back to the right-hand side of quadratically expanded, and map the terms, obtaining

<!-- chunk {"id": "body-0074", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

where regularized $Q_{uu}$ is captured in $\kappa$ and $K$. These equations are propagated backward in time with a terminal condition ${V_{N}{(x_{N})}} = {\Phi{(x_{N})}}$, which is known as a backward pass. Then, a new state and control sequence is determined by propagating dynamics forward in time, typically with a backtracking line search. This propagation is called a forward pass. In the line search, a trial control sequence is applied to the system, generating a new state sequence

<!-- chunk {"id": "body-0075", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

and candidate cost. Starting from step size $\alpha = 1$, $\alpha$ is decreased until cost reduction is achieved. A pair of new state and control trajectories that achieves cost reduction is used new nominal pair for the next iteration. DDP repeats the backward and the forward pass until some convergence criteria are satisfied. In practice, when the cost is not reduced with small $\alpha$, the gains in the current iteration are discarded, and a new backward pass with larger $\tau$ is invoked. As it can be seen, too large $\tau$ vanishes the information of $Q_{uu}^{- 1}$ in the gains. Therefore, a proper choice of $\tau$ is important. An efficient scheduling technique is found in Tassa et al..

<!-- chunk {"id": "body-0076", "role": "body", "section": "Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

Although the original DDP is introduced with second-order expansion of dynamics, in this work we consider only the first-order expansions as it is computationally cheaper and tends to be more numerically stable. In fact, many practitioners neglect the second-order terms, resulting in the so-called iLQR family of algorithms: Tassa et al.; Giftthaler et al.; Boutselis and Theodorou.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Constrained Differential Dynamic Programming", "weight": 1.0} -->

In this section, we present the main constrained variations of DDP which emerge through combinations with NLP techniques. For all algorithms, we demonstrate the impact of constraints on the objective function $J$ and then examine how the $Q$ functions are modified compared to the unconstrained DDP. For notational brevity, we use the concatenated variable $y_{k} = {\lbrack u_{k}^{\mathsf{T}},x_{k}^{\mathsf{T}}\rbrack}^{\mathsf{T}}$, which allows us to write

<!-- chunk {"id": "body-0078", "role": "body", "section": "Constrained Differential Dynamic Programming", "weight": 1.0} -->

Adding inequality constraints $g \leq 0$ to, we consider

<!-- chunk {"id": "body-0079", "role": "body", "section": "Constrained Differential Dynamic Programming", "weight": 1.0} -->

Note that in the final time step, the constraint is a function of only $x_{N}$. To simplify our argument, we keep the dimension of ${g_{N}{(x_{N})}} \in {\mathbb{R}}^{w}$, which is the same as that of $g{(x_{k},u_{k})}$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Log Barrier DDP", "weight": 1.0} -->

First, we show how problem can be addressed through combining DDP and $\log$ barrier method. Following, by incorporating the inequality constraints in the objective, we have a modified problem with cost $\hat{J}$ as

<!-- chunk {"id": "body-0081", "role": "body", "section": "Log Barrier DDP", "weight": 1.0} -->

which modifies the value function as

<!-- chunk {"id": "body-0082", "role": "body", "section": "Log Barrier DDP", "weight": 1.0} -->

On the RHS, the second term is added compared to. Let the argument for the $\min$ operator be $\hat{Q}$. The derivatives of $\hat{Q}$ are

<!-- chunk {"id": "body-0083", "role": "body", "section": "Log Barrier DDP", "weight": 1.0} -->

where the second term of ${\hat{Q}}_{uu}$ can be omitted for the GN approximation as in section 2.2. This approximation was rederived by augmenting the barrier term as an additional element of the state in dynamics in Almubarak et al.. In this work, only the first-order derivatives of constraints contribute to the second-order derivatives of $Q$. The approximation is also indirectly regularizing the Hessian, making the optimization problem more well-conditioned for DDP. There exist techniques that relax the $\log$ barrier to facilitate optimization, accepting constraint violation Grandia et al.. In this paper, however, we use the exact (not relaxed) barrier function because it can keep trajectories always feasible even before convergence. This is a unique algorithm property that distinguishes the method from others. As mentioned in section 2.2, $\mu$ needs to be reduced as optimization progresses. However, as reported in previous work, a single small value of $\mu$ is sufficient in most cases Almubarak et al..

<!-- chunk {"id": "body-0084", "role": "body", "section": "Augmented Lagrangian DDP", "weight": 1.0} -->

In this section, we first introduce two constrained DDP formulations, that is, single- and multiple-shooting DDPs. Then, we derive AL DDP in both formulations.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Single and multiple shooting constrained DDP", "weight": 1.0} -->

Single-shooting DDP is the normal DDP explained in section, where the decision variables are only control variables. In this formulation, equality constraints arise from the dynamics are implicitly satisfied. On the other hand, in multiple-shooting DDP, the constraints from dynamics can be violated and treated as residual in dynamics, or constraint violation penalized in the cost. Since the algorithm can violate the dynamics, computing an initial trajectory of the state is easy in contrast to the case of single-shooting. In a reaching task of a vehicle, for example, one can draw its trajectory by linearly interpolating the initial point to the target, or one could use sampling-based algorithms, e.g., rapidly exploring random tree. We test the multiple-shooting DDP by feeding these initial guesses later in section.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Single and multiple shooting constrained DDP", "weight": 1.0} -->

As mentioned in section, two types of multiple-shooting DDP exist. In the first type, the decision variables are a pair of current control and next state, i.e., $u_{k}$ and $x_{k + 1}$, which are related by equality constraints from the dynamics. In this formulation, the infeasibility of equality constraints is penalized as part of the cost. The linear update law updates all variables, including state and control. Inequality constraints, such as obstacles, can easily be added as part of the cost. However, in the second type, the infeasibility of the equality constraints, also known as residual or defect, is not part of the cost. Instead, they are captured in $Q$ functions in the backward pass through dynamics and reduced in the forward pass, with the linear or nonlinear update law. In these methods, in the second type, decision variables are only control variables, which differs from the methods of the first type. Nevertheless, they still have the property of multiple-shooting because they can accept dynamically infeasible trajectories. They show their power in solving problems with complex dynamics, such as humanoid robots with contacts.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Single and multiple shooting constrained DDP", "weight": 1.0} -->

However, state constraints such as obstacles have not been presented. We use the first type as a representative of multiple-shooting DDP because we are more interested in environments with constraints.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Inequality constrained DDP with single shooting", "weight": 1.0} -->

Here, we derive the AL DDP with the single shooting-method, where only the inequality constraints $g$ are considered. Following, by adding penalty terms from constraints to the objective, we have from that

<!-- chunk {"id": "body-0089", "role": "body", "section": "Inequality constrained DDP with single shooting", "weight": 1.0} -->

for fixed penalty parameter $\rho_{k} \in {\mathbb{R}}^{w}$ and Lagrangian multiplier $\lambda_{k} \in {\mathbb{R}}^{w}$. In the inner loop, DDP is used to solve with modified $Q$ functions whose derivatives are given below.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Inequality constrained DDP with single shooting", "weight": 1.0} -->

where $P_{k} = {{diag}{\lbrack\rho_{k}\rbrack}}$. In the outer loop, the multipliers and penalty parameters are updated by and. Note that in our implementation, we vary $\rho$ for the constraints but keep the same throughout the time horizon, that is, $\rho_{k} = \rho$ for all $k$. This is because even if a large constraint violation exists at time step $k$ in an iteration, this may not be the case in the next iteration at the same time step. Rather, the same constraint is more likely to be violated. The tolerance for the constraint satisfaction, $\eta \in {\mathbb{R}}^{w}$, is used to determine whether the satisfaction of the constraints is sufficient. Let $i_{s}$ and $i_{f}$ be indices of sufficient and insufficient constraint satisfaction. i.e.,

<!-- chunk {"id": "body-0091", "role": "body", "section": "Inequality constrained DDP with single shooting", "weight": 1.0} -->

where the subtraction in the second equation is for sets. Initialized by $\eta_{0}$, using these, $\eta$ is updated by

<!-- chunk {"id": "body-0092", "role": "body", "section": "Inequality constrained DDP with single shooting", "weight": 1.0} -->

where ${\alpha_{\eta},\beta_{\eta}} \in {}$. The tolerance of the inner loop $\epsilon_{AL}$ in 2.3 is updated when the inner loop is successful. The inner loop is considered successful when it satisfies the following conditions,

<!-- chunk {"id": "body-0093", "role": "body", "section": "Inequality constrained DDP with single shooting", "weight": 1.0} -->

i.e., the largest constraint violation is below the specified tolerance. We also reduce the $\epsilon_{AL}$ even when the inner loop is not successful to let the inner loop run more as optimization proceeds as in AL for static problems.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Inequality and equality constrained DDP with multiple shooting", "weight": 1.0} -->

with $e = {\lbrack 1,\cdots,1\rbrack} \in {\mathbb{R}}^{1 \times n}$. Equality constraints from dynamics are given as follows.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Inequality and equality constrained DDP with multiple shooting", "weight": 1.0} -->

Replacing constraints from dynamics with these and using augmented control, the problem in is modified as

<!-- chunk {"id": "body-0096", "role": "body", "section": "Inequality and equality constrained DDP with multiple shooting", "weight": 1.0} -->

As in the single shooting case, we handle the constraints as a part of the cost. Here, the running cost, value function, and constraints are functions of ${\overset{\sim}{u}}_{k}$, which gives derivatives as

<!-- chunk {"id": "body-0097", "role": "body", "section": "Inequality and equality constrained DDP with multiple shooting", "weight": 1.0} -->

where we drop time index $k$ and use $x^{\prime} = x_{k + 1}$ for simplicity. The $Q$ function for this problem is now

<!-- chunk {"id": "body-0098", "role": "body", "section": "Inequality and equality constrained DDP with multiple shooting", "weight": 1.0} -->

By changing $u$ to $\overset{\sim}{u}$, DDP can be used for optimization. One key difference is the update law in the forward pass, where both state and control variables are updated by the following linear update law

<!-- chunk {"id": "body-0099", "role": "body", "section": "Inequality and equality constrained DDP with multiple shooting", "weight": 1.0} -->

The rest of the parameters are updated in the same manner as in the single-shooting case.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

In this section, we derive and modify IP DDP based on Pavlov et al.. We consider the single-shooting DDP variation with inequality constraints. In particular, we minimize the Lagrangian over control $u$ and maximize it over multiplier $\lambda$ to compute the optimal value of the original problem. Introducing slack variables, and removing the equality constraints from dynamics, we get a new objective

<!-- chunk {"id": "body-0101", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

where $\Lambda$ is a sequence of multipliers similar to. Here, we cannot simply add terms to $Q$ due to additional decision variables $\lambda_{k}$ and $s_{k}$. Instead, we define

<!-- chunk {"id": "body-0102", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

The existence of constraints modifies the derivatives of $Q$, and $\lambda$ introduces new derivatives as

<!-- chunk {"id": "body-0103", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

The constraint term in ${\hat{Q}}_{yy}$ can be excluded for better conditioning, that is, ${\hat{Q}}_{uu} \approx Q_{uu}$. In order to derive the backward pass, the optimality condition for $\hat{Q}$ under constraints is considered. Partial derivative of quadratic approximation of $\hat{Q}$ with respect to $\deltau_{k}$, first order expansion of complementary slackness, and that of slack variable give

<!-- chunk {"id": "body-0104", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

where $S = {{diag}{\lbrack s_{k}\rbrack}}$, $\overline{\Lambda} = {{diag}{\lbrack\lambda_{k}\rbrack}}$ and $e$ is given. Solving the system above, we obtain the deviation of decision variables with gains as

<!-- chunk {"id": "body-0105", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

By plugging $\deltau_{k}$ and $\delta\lambda_{k}$ into the quadratic expansion of $\hat{Q}$ and mapping terms of $\deltax_{k}$ s with $V_{k}$, derivatives of the value function are obtained by

<!-- chunk {"id": "body-0106", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

We note that the approach described here differs from the one in the original work, which excludes the gains of $\lambda_{k}$ from the recursion of the value function and excludes constraints in the final time step. We provide further details about this difference in Appendix C. In the forward pass, $u_{k},s_{k}$ and $\lambda_{k}$ are updated using the gains in and based on as

<!-- chunk {"id": "body-0107", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

Observe that $u_{k},s_{k}$ and $\lambda_{k}$ are updated with different step sizes $\alpha_{s}$, $\alpha_{\lambda} \in {(0,1\rbrack}$. The values of $\alpha_{s}$ and $\alpha_{\lambda}$ are determined by the line search filter method so that they satisfy. Although both merit function and filter-based line search approaches can be used in the IP method, the authors of the original work use a filter-based approach similar to the one of the popular IPOPT package.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

for $k = {{1\cdotsN} - 1}$. The step size for $\lambda$ is obtained without the line search because it does not affect the filter. Unfortunately, applying this rule to DDP is not as straightforward as applying a similar rule to IP for static problems due to the existence of feedback terms in DDP. Because search directions are defined via the linear feedback equations in DDP as (4.3), $\alpha_{\lambda}$ is affected by $\alpha_{s}$ through $\deltax_{k}$. In the original work, without setting the max. values of each $\alpha$ s, the line search is performed with a common parameter for $\alpha_{s}$ and $\alpha_{\lambda}$, making the line search unnecessarily conservative. This is because each step size is affected by that of the paired variable. To alleviate this problem, we propose applying the rule with different $\alpha$ for $s$ and $\lambda$ as in the original formulation of the IP method. We first find $\alpha_{s}^{\max}$ using dynamics.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Interior Point DDP", "weight": 1.0} -->

Since there is no closed-form solution for $\alpha_{s}^{\max}$, we rely on a line search to find $\alpha_{s}^{\max}$. Next, the line search filter is performed, setting $\alpha_{s}^{\max}$ as the upper bound. Inside of this line search, the inner line search for $\alpha_{\lambda}$ is also performed, using $\deltax_{k}$ generated with $\alpha_{s}$ from the outer line search. The IP DDP algorithm used in section is implemented with this modified line search filter. Finally, we note that the feasibility restoration mechanism explained in 2.4 is not implemented with DDP.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Primal-Dual Augmented Lagrangian DDP", "weight": 1.0} -->

This section shows the derivation of single- and multiple- shooting PDAL DDP.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

Following, and using $\rho = \frac{1}{\mu}$, we have PDAL, which is the objective of PDAL DDP as

<!-- chunk {"id": "body-0112", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

This objective modifies $Q$ and its derivatives as follows.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

and projection. ${\lbrack I_{w}\rbrack}_{\mathcal{A}}$ is a modified identity matrix whose $i$ th diagonal element is 1 if $g_{i}$ is active (positive after projection in ) and zero otherwise. First-order optimality condition for quadratic approximation of $\hat{Q}$ gives

<!-- chunk {"id": "body-0114", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

The matrix on the left-hand side is ill-conditioned as $\rho_{I}$ ($\mu_{I}$) gets large (small) due to the last term in ${\hat{Q}}_{yy}$, which is avoided by a similar transformation mentioned in section 2.5.2. See appendix D for details. Using this transformation, we have a transformed symmetric system

<!-- chunk {"id": "body-0115", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

When the constraints are not active, the system gives the same solution as normal uncostrained DDP for $\deltau_{k}$. For $\delta\lambda_{k}$, the solution makes $\lambda_{k}^{new}$ zero. We use a similar update law proposed in Jallet et al., which makes $\lambda_{k}$ strictly zero for inactive constraints as below.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

where $\mathcal{A}^{c}$ denotes the inactive set of constraints. The positive orthant projection for $\lambda$ is ensuring that $\lambda$ is nonnegative. The gains lead to recursion for the value function as below.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

After performing the DDP presented above, $\lambda_{e}$ is updated by the law. The penalty parameters and tolerances for constraint satisfaction and DDP are updated in the same way as in the AL DDP provided in section 4.2.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Single-shooting", "weight": 1.0} -->

A key advantage of PDAL over the standard AL method is its robustness to changes in the penalty parameter. When the parameter is updated to improve constraint satisfaction, a new objective is defined, and a corresponding search direction is computed. By accounting for the interaction between the penalty parameter and the dual variables, PDAL can provide a more effective search direction than standard AL following the updates.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Multiple-shooting", "weight": 1.0} -->

Due to the limited space, we omit the form of an objective and recursion. Following the same the procedure as AL DDP and single shooting PDAL, we have

<!-- chunk {"id": "body-0120", "role": "body", "section": "Multiple-shooting", "weight": 1.0} -->

Using the multiple-shooting DDP with these $\hat{Q}$ followed by updating multipliers, penalty parameters, and tolerances for inner DDP and constraints, the problem is solved by multiple-shooting PDAL DDP.

<!-- chunk {"id": "body-0121", "role": "body", "section": "ADMM DDP", "weight": 1.0} -->

This section introduces the ADMM-based variaton of constrained DDP following Sindhwani et al..

<!-- chunk {"id": "body-0122", "role": "body", "section": "Introducing Copy Variables", "weight": 1.0} -->

Let us introduce a copy of the variables of $X$ and $U$, denoted by $X^{c}$, and $U^{c}$, respectively. These copy variables are intended to strictly satisfy the additional state/control constraints, except for the dynamics ones. Original variables ($X,U$) minimize the original cost only under dynamic constraints. We assume that the constraints can be divided into state- and control-dependent parts as follows.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Introducing Copy Variables", "weight": 1.0} -->

Hence, the problem can be reformulated as follows

<!-- chunk {"id": "body-0124", "role": "body", "section": "Introducing Copy Variables", "weight": 1.0} -->

where we use the same vector $\rho$ across time.

<!-- chunk {"id": "body-0125", "role": "body", "section": "ADMM DDP", "weight": 1.0} -->

The ADMM DDP algorithm consists of the following updates that happen in a sequential manner.

<!-- chunk {"id": "body-0126", "role": "body", "section": "ADMM DDP", "weight": 1.0} -->

Using the $Y^{new}$ obtained by DDP, the copy variables are updated by

<!-- chunk {"id": "body-0127", "role": "body", "section": "ADMM DDP", "weight": 1.0} -->

which can be decomposed for each time instant as

<!-- chunk {"id": "body-0128", "role": "body", "section": "ADMM DDP", "weight": 1.0} -->

This requires solving an optimization problem with a quadratic objective under constraints ${g{(y^{c})}} \leq 0$. This optimization is performed without considering dynamics, and the resulting trajectory may be dynamically infeasible. As a special case, when the constraint has the simple form of $y^{c} \leq y_{b}$, the problem is solved by clamping. Finally, the multiplier is updated by

<!-- chunk {"id": "body-0129", "role": "body", "section": "ADMM DDP", "weight": 1.0} -->

ADMM DDP repeats the three update processes in and until the residuals mentioned in section 2.6 become small enough. Upon convergence, the original and copy variables will reach to consensus, and as a result, the final solution will be optimal while satisfying all constraints. It is well known however, that ADMM might require many iterations until reaching high accuracy Boyd et al..

<!-- chunk {"id": "body-0130", "role": "body", "section": "Analysis of AL-based DDPs", "weight": 1.0} -->

In this section, we analyze AL-based DDPs. Specifically, we analyze the difference between ADMM DDP and others, including AL and PDAL DDPs. As in the case of ADMM for static problems, ADMM DDP also requires long iterations to achieve an accurate solution. This can be understood by investigating how the $Q$ function of DDP captures information on cost and constraints. In AL and PDAL DDP, the active constraints are directly captured in the $Q$ functions of DDP. See for AL DDP and for PDAL DDP. This information of constraints enables algorithms to satisfy them effectively while reducing the original cost. However, in ADMM DDP, the $Q$ function has information on constraints only through the distance from safe copies (see ). In addition, safe copies may not be dynamically feasible, making the problem in difficult. A canonical example is when the DDP for solving problem commands a control sequence that exceeds its limits in many time steps. In this situation, staying close to the safe copies (clamped control) and completing the task conflict with each other, slowing down cost reduction and constraint satisfaction.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Analysis of AL-based DDPs", "weight": 1.0} -->

Indeed, in our experiment in section 7.1 How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"), we observe that ADMM DDP cannot handle problems where the control constraints are tight, and a control sequence needs to hit its limit in many time steps.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Analysis of AL-based DDPs", "weight": 1.0} -->

Another difference can be found in the role of the penalty parameter $\rho$. In AL and PDAL DDPs, the product of $\rho$ and active constraints modifies $Q$ functions. Therefore, when the constraints are not active, $\rho$s does not affect $Q_{uu}$. In ADMM DDP, $\rho$ is added to $Q_{uu}$ regardless of the status of the constraints as if the regularizer. This seems appealing for the conditioning of $Q_{uu}$, but too large $\rho$ can slow down optimization, as mentioned in section. In AL and PDAL DDPs, too large $\rho$ also interrupts optimization, but what we would like to emphasize here is that in ADMM, $\rho$ always affects $Q_{uu}$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "SQP for dynamical systems", "weight": 1.0} -->

This section presents a concise overview and derivation of SQP for dynamical systems, considering both the single- and multiple-shooting approaches based on Gill et al..

<!-- chunk {"id": "body-0134", "role": "body", "section": "SQP for dynamical systems", "weight": 1.0} -->

Consider the constrained optimal control problem. Here, we have the sequence of state and control as long vectors as in and a deviated trajectory as in a similar manner as in section, i.e., ${X = {\overline{X} + {\deltaX}}},{U = {\overline{U} + {\deltaU}}}$. Both single- and multiple-shooting SQP have linearized dynamics as constraints. The difference is whether the constraints are implicit or explicit. The constraints from the dynamics are linearized as below.

<!-- chunk {"id": "body-0135", "role": "body", "section": "SQP for dynamical systems", "weight": 1.0} -->

In the single-shooting formulation, the state is updated via the system dynamics, satisfying the equality constraints on the nominal trajectory. Therefore, the first terms of both sides of the equations cancel out. Therefore, the deviation of state and control are tied with a matrix $F \in {\mathbb{R}}^{{{nN} \times m}{({N - 1})}}$ by

<!-- chunk {"id": "body-0136", "role": "body", "section": "SQP for dynamical systems", "weight": 1.0} -->

In the multiple-shooting case, however, the equality constraint from dynamics might be violated. Consequently, the first terms of both sides of might not cancel out. Thus, the constraints on each time step take the following form.

<!-- chunk {"id": "body-0137", "role": "body", "section": "SQP for dynamical systems", "weight": 1.0} -->

$k = {1,{{\cdotsN} - 1}}$. $x_{init}$ is a given initial state where the control sequence cannot affect, and thus ${{\overline{x}}_{1} - x_{init}} = 0$. The equality constraints with nominal terms are given in matrix-vector form by

<!-- chunk {"id": "body-0138", "role": "body", "section": "Single-shooting SQP", "weight": 1.0} -->

From, the SQP subproblem of the problem in is given by

<!-- chunk {"id": "body-0139", "role": "body", "section": "Single-shooting SQP", "weight": 1.0} -->

with $J_{X} \in {\mathbb{R}}^{nN}$ and $J_{U} \in {\mathbb{R}}^{m{({N - 1})}}$. By eliminating $\deltaX$ using the equality constraints, single-shooting SQP for is formulated as

<!-- chunk {"id": "body-0140", "role": "body", "section": "Single-shooting SQP", "weight": 1.0} -->

The $X$ trajectory is updated using $\deltaU^{\ast}$ which is the solution of, and the dynamics of the system with an appropriate step size similar to the DDP in but in open-loop fashion. We perform a line search with the AL merit function to determine the step size, whose detail is given in appendix B. When an appropriate step size cannot be found in the line search, we regularize the Hessian as in the case of DDP and resolve the QP subproblem. We note that computing the exact Hessian of can be expensive and may not even be worth computing when it is not PD. There exists an iterative Hessian approximation scheme, which is known as the BFGS update (Broyden Fletcher Goldfarb Shanno, ). This update rule can approximate a PD Hessian based on the Hessian in the previous iteration.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Multiple shooting-SQP", "weight": 1.0} -->

Using equality constraints, instead of, and augmented variable $Y$, the multiple-shooting formulation is obtained as

<!-- chunk {"id": "body-0142", "role": "body", "section": "Multiple shooting-SQP", "weight": 1.0} -->

whose step size $\alpha$ is determined by the line search with the AL merit function as in the single-shooting method. Another update strategy that strictly satisfies the dynamics is possible, as presented in Tenny et al.. Here, the jacobians from the dynamics given by ${\hat{F}}_{Y}$ in has a sparse structure due to the recursion in the dynamics. Several methods that can exploit this structure and reduce computational complexity of SQP have been proposed (Dohrmann and Robinett Rao et al. Jørgensen et al. Wang and Boyd, ). Note that the sparse structure is available only in the multiple-shooting formulation.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Theoretical Time Complexity", "weight": 1.0} -->

In this section, we compare the theoretical per-iteration time complexities of DDP and SQP. We note that for SQP, the reported complexity corresponds to one iteration of solving the inner QP subproblem, rather than the overall solution of the outer nonlinear problem. This is because with inequality constraints, we cannot tell the number of iterations required to solve the inner subproblem. All complexities are summarized in Table.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Theoretical Time Complexity", "weight": 1.0} -->

In unconstrained DDP, the computational bottleneck is inverting $Q_{uu}$. Reference Liao and Shoemaker has a detailed breakdown of the computational complexity of unconstrained DDP, which includes matrix inversion, as well as matrix multiplication operations. Matrix multiplication is a highly parallelizable operation, and therefore it can be optimized very effectively, while matrix inversion remains a much harder operation to optimize and accelerate. When $n \gg m$, matrix multiplications involving $Q_{xx}$ and $V_{xx}$, are theoretically more expensive than inverting $Q_{uu}$. However, these operations can be accelerated, whereas inversion of $Q_{uu}$ still requires a cubic time complexity. The inversion is performed $N - 1$ times in the backward pass. Therefore, the complexity is $\mathcal{O}{({Nm^{3}})}$, in single-shooting and $\mathcal{O}{({N{({n + m})}^{3}})}$ in multiple-shooting.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Theoretical Time Complexity", "weight": 1.0} -->

The barrier, AL, and ADMM DDPs follow the same complexity because the number of decision variables (of inner loops) is the same as in standard DDP. In IP DDP, the coefficient matrix of the system of equations in has size ${({m + {2w}})} \times {({m + {2w}})}$. This system can be reduced to a smaller one by eliminating the slack variable, whose coefficient matrix has the size of ${({m + w})} \times {({m + w})}$. Further reduction can be performed by eliminating the multiplier, giving a system with a coefficient matrix of $m \times m$. Therefore, the time complexity with respect to the decision variables is cubic. The same analysis can be applied to PDAL DDPs.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Theoretical Time Complexity", "weight": 1.0} -->

In SQPs, the bottleneck is solving the QP subproblems, whose Hessian has the size of ${{{({N - 1})}m} \times {({N - 1})}}m$ in single- and ${\{{{{({N - 1})}m} + {Nn}}\}} \times {\{{{{({N - 1})}m} + {Nn}}\}}$ in multiple-shooting. These large Hessians lead to $\mathcal{O}{({N^{3}m^{3}})}$ and $\mathcal{O}{({N^{3}{({m + n})}^{3}})}$ for single- and multiple-shooting, respectively for one iteration of QP subproblem. However, as mentioned in section 5.2, several methods in structure-exploiting multiple-shooting SQP that can reduce the QP's complexity are available.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Theoretical Time Complexity", "weight": 1.0} -->

For methods based on Riccati recursion, the matrix to be inverted has size $m \times m$. Hence, the complexity is $\mathcal{O}{({Nm^{3}})}$, following the same reasoning as in DDP. For methods that uses factorization, the complexity can be reduced to $\mathcal{O}{({N{({n + m})}^{3}})}$. In single-shooting, dependency on $N$ can reduced to not linear, but quadratic $\mathcal{O}{({N^{2}n^{3}})}$. From a computational point of view, the single-shooting variant is useful for a problem with a short time horizon $N$ and a large state dimension $n$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Theoretical Time Complexity", "weight": 1.0} -->

With a long time horizon $N$, DDP and multiple-shooting SQP are favorable due to the linear growth of complexity in $N$. Among these, single-shooting DDPs and multiple-shooting SQP with Riccati recursion are the most efficient because of the small number of decision variables. Their advantages are especially important in underactuated systems, e.g., systems with $n \gg m$, which are the most typical ones in robotics. Although multiple-shooting SQP can achieve the same time complexity, this corresponds only to a single iteration of its QP subproblem. Assuming that they require a similar number of outer iterations, DDP remains advantageous.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We wish to answer the following three research questions to understand each method's relative strengths and weaknesses.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

How fast does each algorithm converge in terms of cost and constraints?

<!-- chunk {"id": "body-0151", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

How robust is each algorithm to varying initial conditions and targets?

<!-- chunk {"id": "body-0152", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

How effectively can we steer multiple shooting methods to avoid poor local minima via initial guess?

<!-- chunk {"id": "body-0153", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

To answer these three questions, we compare the constrained DDPs and SQPs on four different dynamical systems, that is, an inverted pendulum, a 2D quadrotor with a pendulum (quadpend) based on Singh et al., a tadpole-like swimmer as in Tassa et al., and, Franka Emika Panda robotic arm simulated in Brax with mjx backend Freeman et al.; Zakka et al.. For investigating (R1), we use all systems, while for (R2), we use the quadpend and Panda. In (R3), we focus on the quadpend. The state $x$ of the inverted pendulum consists of the angle and angular velocity of the pendulum as $x = {\lbrack\theta,\overset{˙}{\theta}\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{2}$ and the control $u \in {\mathbb{R}}$ is the torque applied to the pendulum.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

The state of the quadpend consists of the 2D position and orientation of the quadrotor, the angle of the pendulum, and the time derivative of them, which leads to $x \in {\mathbb{R}}^{8}$. We control the force that the two rotors generate, and therefore $u \in {\mathbb{R}}^{2}$. We choose this example because of the nonlinearity of the constraints by the pendulum part. The swimmer is a more complex system consisting of five links, whose control is torque is applied in the four joints. The dynamics of the swimmer are found in Tassa et al.. The state consists of the 2D position of the nose, four joint angles and their time derivatives. Hence, the state is $x \in {\mathbb{R}}^{12}$. The control $u \in {\mathbb{R}}^{4}$ is the torques generated in the joints. The robotic arm Panda has seven joints. The state has the angles of joints and its derivatives, which gives state $x \in {\mathbb{R}}^{14}$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

The control $u \in {\mathbb{R}}^{7}$ is a command of the joints. The angles and commands have limits. Details of the dynamics of the systems and parameters are provided in Appendix E. All experiments except for Panda were performed with MATLAB. The Panda experiment is implemented with JAX.

<!-- chunk {"id": "body-0156", "role": "body", "section": "(R1) How fast does each algorithm converge in terms of cost and constraints?", "weight": 1.0} -->

We first explain how we evaluate the progress of optimization. Subsequently, the results are demonstrated.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Progress of Optimization", "weight": 1.0} -->

To monitor the progress of optimization, we keep track of the cost gradient over iterations. In unconstrained DDP, the gradient can be obtained by differentiating the cost-to-go at time step $k$ in w.r.t. $u_{k}$ as

<!-- chunk {"id": "body-0158", "role": "body", "section": "Progress of Optimization", "weight": 1.0} -->

The second term is computed recursively in the backward pass of DDP as

<!-- chunk {"id": "body-0159", "role": "body", "section": "Progress of Optimization", "weight": 1.0} -->

with boundary condition $J_{x,N} = \Phi_{x,N}$. We used

<!-- chunk {"id": "body-0160", "role": "body", "section": "Progress of Optimization", "weight": 1.0} -->

as a representative of the gradient of the cost of a trajectory. In a constrained setting, the gradient of $J$ changes to a gradient of the modified objective depending on the algorithm, as shown in the left column of Table How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). For SQP, we use the gradient of the Lagrangian. We note that this is intended for monitoring the optimization of one algorithm, but not for comparing the value across algorithms. We also note that the gradient of the $\log$ barrier DDP has a different property due to the barrier term. In other methods, the gradient may be used as an exit criterion, but in barrier DDP, it is not. Nevertheless, we present it for completeness. We also monitor the values presented in the right column of the table, all of which are related to constraint violation, the residual of optimality condition for dual variables (if the method takes them into account), and penalty parameters (if the method includes any and changes them over iterations). The norm here is the infinity norm taken over all the time steps, e.g.,

<!-- chunk {"id": "body-0161", "role": "body", "section": "Results", "weight": 1.0} -->

To compare the performance of each algorithm, we let all algorithms solve the same tasks, comparing cost reduction and constraint violation.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Results", "weight": 1.0} -->

Single Shooting: $\log$ barrier, AL, IP, PDAL ADMM DDPs, and SQP.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Results", "weight": 1.0} -->

Multiple Shooting: AL with exact Hessian, AL with GN approximation, PDAL DDPs, and SQP.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Results", "weight": 1.0} -->

The optimization stops when either max. iteration is reached, or the regularizer in exceeds the prespecified value.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Results", "weight": 1.0} -->

Inverted pendulum: In this task, the goal is to swing up the pendulum while satisfying the constraints ${{- 0.8} \leq u_{k} \leq 0.8},{{- 1.5} \leq \overset{˙}{\theta} \leq 1.5}$. The results are provided in Fig. How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). In the right column of each figure, we present the progress of optimization with the gradient of the cost and the other metrics given in Table How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). The vertical dotted lines in AL, PDAL, and ADMM DDP represent different outer loops. In the left column, graphs showing the evolution of $\theta$, $\overset{˙}{\theta}$ and control $u$ are illustrated. The constraints and targets are given as dotted lines and circles, respectively. Since constraints are linear in this problem, the Hessian of the constraints is zero.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Results", "weight": 1.0} -->

Thus, the exact Hessian and that with the GN approximation are identical. See AL multi exact and AL multi approx. in Fig. ). $\log$ barrier and IP DDP terminate earlier than other methods because the descent direction cannot be found with a large regularizer. Fig. 2(a) How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") shows the evolution of cost (original cost $J$ in ). The largest constraint violation (if any) over iterations is shown in Fig. 2(b) How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). We observe that most methods are able to complete the task with low $({< 10^{- 5}})$ constraint violation. In multiple-shooting DDPs, inequality and equality constraints exhibit comparable magnitudes, contrasting with multiple-shooting SQP, where inequality constraints consistently maintain feasibility. We postulate that this phenomenon arises from the property of SQP, that is, solving QP under constraints, rather than incorporating all elements into the $Q$ function as in DDP.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Results", "weight": 1.0} -->

Although both SQP and DDP rely on line search to find a proper step size, SQP seems to better capture the information of constraints. The $\log$ barrier method can keep the trajectory always feasible and therefore does not appear in Fig. 2(b) How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). However, its cost is higher than those of the other DDP methods. This is due to the fixed penalty parameter $\mu$ in (4.1). In exchange for a simple implementation, this fixed $\mu$ makes the algorithm only approximately solve the problem, resulting in a higher cost in this experiment. In this problem, the controller needs to hit its limit over many time steps to complete the task. This makes the problem difficult for ADMM DDP, as we analyzed in section 4.6. In Appendix E.6, we further relax the control limit to $u \in {\lbrack{- 0.9},0.9\rbrack}$ and observe that ADMM DDP is able to handle problems with less tight constraints.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Results", "weight": 1.0} -->

For SQP, the multiple shooting version performs similarly to other successful DDP methods, whereas the single shooting variant performs poorly. This difference comes from the fact that the cost function in the multiple-shooting SQP is strictly quadratic in the decision variables (state and control); on the other hand, in single-shooting, the cost is not exactly quadratic in control due to the elimination of state via linearized dynamics.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Results", "weight": 1.0} -->

Quadpend: The quadpend is navigated to reach the target $x_{g} = {\lbrack 2.5,{- 1},0,{\pi/2},0,0,0,0\rbrack}^{\mathsf{T}}$ (pendulum upright) from the initial state $x_{0} = {\lbrack{- 2},1,0,0,0,0,0,0\rbrack}^{\mathsf{T}}$ (pendulum down) while avoiding four obstacles under box control constraints. The initial trajectory is shown in Fig. LABEL:fig:quad_init_last, which is obtained with single-shooting PDAL DDP. We show the results of single and multiple shooting methods in Fig. How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). In this experiment, multiple-shooting AL DDPs reached maximum iteration by reaching a plateau where the inner loops could not find a descent direction.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Results", "weight": 1.0} -->

The multiple-shooting SQP algorithm terminated due to failure in the line search to find a descent direction even after regularizing the Hessian as explained in Section 5.1. Here, the GN approximation makes a difference because of nonlinear constraints. Indeed, we observe the effectiveness of the approximation as multiple-shooting AL DDP fails without the approximation, getting stuck at a poor local minimum with a large constraint violation. Other than the multiple-shooting AL DDP with exact Hessian, all algorithms can let the quadpend hit the target with the pendulum up, although the solutions vary. This is because the algorithms are local methods that use the local approximation of the cost and dynamics.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 4(b) How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") and Fig. 4(c) How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") compare the cost and constraint violation. Again, we note that in Fig. 4(c) How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"), some algorithms do not appear when their trajectories are feasible. AL-based DDPs (AL, PDAL, and ADMM) show rapid cost reduction with constraint violation. They hit the target first and then gradually satisfy the constraints, where ADMM shows the slowest improvement in constraint satisfaction. The other two DDP methods, IP and barrier DDP, can keep the trajectory feasible during optimization. IP DDP's slowness comes from the nature of the IP method, where the trajectory is biased to follow the central path as. In this experiment, $\log$ barrier DDP is a good option that balances cost reduction and constraint satisfaction.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Results", "weight": 1.0} -->

For SQP, as in the previous case, the multiple-shooting DDP is comparable to other DDP methods or even better in constraint satisfaction, but the shingle-shooting method performs poorly.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Results", "weight": 1.0} -->

Swimmer: Starting from the initial position, with its nose in the origin and its tail straight, the swimmer tries to hit the target $\lbrack 5,{- 1}\rbrack$ with its nose. The initial control sequence is zeros, which keeps the swimmer in the initial place. The results are shown in Fig. How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") and Fig. How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"), where the difference in the algorithm's performance becomes more evident than in the previous examples. The $\log$ barrier DDP method gets stuck before hitting the target due to the approximation. IP DDP shows slow progress and cannot hit the target. Although single-shooting AL and PDAL DDP can complete the task in a similar order of constraint violation $(10^{- 5})$, PDAL achieves a lower cost.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Results", "weight": 1.0} -->

In this example, multiple-shooting DDPs struggled to solve the problem. Specifically, they can hit the target with a significant equality constraint violation (especially dynamics) early in the optimization process. However, to satisfy the constraints, they start to show conservative motions and finally end up staying at the initial position with the initial state at a high cost. This is because the equality constraints are always satisfied if they do not move. To alleviate the issue, we regularize the state part of $Q_{\overset{\sim}{u}\overset{\sim}{u}}$ similar to and the technique, which prevent $x$s from moving too far from the current trajectory. The results presented here are obtained with this regularization strategy. This modification works in AL DDP with approximated Hessian, making the swimmer move forward. Multiple-shooting SQP can achieve the task with the lowest constraint violation among all methods that can complete the task. Overall, single-shooting AL, PDAL DDPs, and multiple-shooting SQP can complete the task with a similar order of constraint violation.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Results", "weight": 1.0} -->

PDAL single-shooting DDP achieves the best cost, followed by AL single-shooting DDP, and multiple-shooting SQP.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Results", "weight": 1.0} -->

Panda: The task of the arm is to place the end effector on the target position and stop, while avoiding four spherical obstacles, and satisfying the joint and its command limit. In this example, the second-order information of dynamics is not stably available from the simulator. Therefore, we drop the corresponding terms of constraints in AL and PDAL multiple-shooting DDPs. Consequently, the AL multiple-shooting method only has an approximate version. The initial position of the arm is given by the joint angles from the base link as $x_{0} = {\lbrack 0,0,0,{- {\pi/2}},0,{\pi/2},{- {\pi/4}}\rbrack}$. The initial control command maintains the initial state. The results are presented in Fig. How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") and Fig How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). The algorithms find different local solutions, as in the quadpend.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Results", "weight": 1.0} -->

Similarly to the swimmer example, $\log$-barrier and IP DDP get stuck and cannot hit the target, while other single-shooting DDPs can complete the task. An addition of the feasibility restoration mechanism could improve the performance of IP DDP. AL and PDAL show similar performance, while ADMM has high constraint violation. This is because we use a small penalty parameter to prioritize hitting the target rather than satisfying constraints in ADMM DDP. For multiple-shooting DDPs, although both AL and PDAL can reduce constraint violations over iterations, only PDAL can achieve the task. SQPs show a tendency similar to that in other experiments. The multiple-shooting one can complete the task with a similar magnitude of constraint violation as other successful DDPs, while the single-shooting one performs poorly.

<!-- chunk {"id": "body-0178", "role": "body", "section": "(R2) How robust is each algorithm to varying initial conditions and targets?", "weight": 1.0} -->

Initial conditions: To examine robustness while varying the initial conditions, we use the quadpend system and initialize the algorithms with ten different initial hovering trajectories with the pendulum down. The hovering trajectory is achieved by an initial control sequence $u_{1:{N - 1}} = {0.5{({m_{q} + m_{p}})}g_{0}{\lbrack 1,1\rbrack}^{\mathsf{T}}}$, where $m_{q}$, $m_{p}$, and $g_{0}$ are the mass of the quadrotor part, the mass of the pendulum part, and the gravitational acceleration, respectively. The algorithms solve the same task as in Section 7.1 How fast does each algorithm converge in terms of cost and constraints? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). Tables How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") and How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess?

<!-- chunk {"id": "body-0179", "role": "body", "section": "(R2) How robust is each algorithm to varying initial conditions and targets?", "weight": 1.0} -->

‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") present the results of the single- and multiple-shooting algorithms, respectively. A successful run is defined as the quadpend hitting the target. With $m$ and $\sigma$, we denote the mean and standard deviation of the values specified by their subscripts $J$, $I$, and $E$, which denote the cost, inequality, and equality constraint violation. When all trajectories are feasible, the symbol $✓$ is used. The arrows in the table represent the preferred value. For example, we have $\uparrow$ next to the success rate because a robust algorithm can hit many targets. To provide an overview of the experiment, we show the resulting trajectories in Fig. How robust is each algorithm to varying initial conditions and targets? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") obtained by multiple-shooting SQP.

<!-- chunk {"id": "body-0180", "role": "body", "section": "(R2) How robust is each algorithm to varying initial conditions and targets?", "weight": 1.0} -->

Among single-shooting methods, PDAL DDP achieves the lowest mean and standard deviation in cost. Although its constraint violation is not as small as that of AL DDP, it is sufficiently small. The $\log$ barrier and IP DDP methods achieve strict feasibility but have higher costs than AL and PDAL. ADMM has a large constraint violation in the mean cost caused by two infeasible trajectories. Overall, all single-shooting DDP methods are robust to the initial condition. Among the multiple-shooting methods, SQP performs best, achieving the best value on almost all items.

<!-- chunk {"id": "body-0181", "role": "body", "section": "(R2) How robust is each algorithm to varying initial conditions and targets?", "weight": 1.0} -->

Different targets: To evaluate the robustness of the algorithms across different targets and tasks, we design three obstacle fields, containing one, two, and four obstacles, respectively. For each field, we conduct one, four, and five experiments with varying target configurations. In total, we have ten experiments. We note that one of these environments, i.e, a pair of an obstacle field and a target, is the same as the one used in the previous example. The results are provided in Table How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") and Table How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). The overview of the experiments is shown in Fig. How robust is each algorithm to varying initial conditions and targets? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization") and Extension 1.

<!-- chunk {"id": "body-0182", "role": "body", "section": "(R2) How robust is each algorithm to varying initial conditions and targets?", "weight": 1.0} -->

In single-shooting methods, $\log$ barrier and IP DDPs show conservative behavior to take distance from constraints through the barrier function. As a result, their performance decreases in cluttered environments. Among the single-shooting algorithms, PDAL DDP has the highest success rate with sufficiently small constraint violation. The multiple-shooting SQP outperforms it in terms of success rate with equality constraint violation. In Fig. How robust is each algorithm to varying initial conditions and targets? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"), we compare a failed trajectory from single-shooting PDAL DDP and a successful trajectory from multiple-shooting SQP in the same task. In the early time steps, both of them draw similar trajectories. However, only SQP can successfully hit the target by rotating a joint close to the base. In contrast, a local minimum captures PDAL DDP, where it continues to bend the arm without incorporating the rotation observed in SQP. Panda can locate the end effector close to the target in this local solution, but cannot hit it. Although single-shooting DDP failed in this example, it can achieve a lower mean cost compared to multiple-shooting SQP.

<!-- chunk {"id": "body-0183", "role": "body", "section": "(R2) How robust is each algorithm to varying initial conditions and targets?", "weight": 1.0} -->

We conclude from these results that when constraint violation is the most critical factor, $\log$ barrier DDP is the best method. However, it might not be able to complete the task, especially in high-dimensional systems and cluttered environments. If users can accept small constraint violations, single-shooting PDAL DDP or multiple-shooting SQP has a higher success rate. In our example, SQP shows a slightly better success rate, whereas PDAL DDP achieves a lower mean cost. A key difference between these two algorithms is that PDAL DDP can always satisfy dynamics, whereas SQP has small violations.

<!-- chunk {"id": "body-0184", "role": "body", "section": "(R3) How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess?", "weight": 1.0} -->

One key advantage of multiple-shooting methods over single-shooting ones is that they can enjoy good initial guesses, which was not demonstrated in previous experiments. In the multiple-shooting formulation, an arbitrary state sequence can be used as an initial state trajectory as explained in Sections 4.2.3 and 5.2, which can help guide the algorithm away from poor local minima. To showcase this ability, we test multiple-shooting algorithms with a new task where the quadpend flies through a narrow gap of obstacles and reaches a target behind them with ten different initial points. When initialized with hovering states and controls at a single starting point, as in the previous experiment, the performance of all methods is decremented. They cannot complete the task, i.e., hitting the target with a significant constraint violation, and getting stuck before hitting it, etc. We show typical failure trajectories in Fig. LABEL:fig:quad_fail_through.

<!-- chunk {"id": "body-0185", "role": "body", "section": "(R3) How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess?", "weight": 1.0} -->

To circumvent this problem, we could solve a sequence of subproblems with intermediate targets and a short time horizon so that the quadpend can detour rather than get stuck at local minima. However, using the multiple shooting method with an informed initial guess, the problem should be solved without solving subproblems because the trajectory can be biased towards the right solution. To verify this idea, we initialize the multiple shooting algorithms with a state sequence, one of which is shown in the left figure of Fig. 10(b) How robust is each algorithm to varying initial conditions and targets? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). This trajectory is obtained by linear interpolation of four points such that the state trajectory does not hit obstacles. This initial guess leads to a reasonable solution presented in the right figure in Fig. 10(b) How robust is each algorithm to varying initial conditions and targets? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). The same strategy as this interpolation is used for all ten different initial points to obtain informed initial trajectories.

<!-- chunk {"id": "body-0186", "role": "body", "section": "(R3) How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess?", "weight": 1.0} -->

The control sequence is initialized with the hover sequence presented in 7.2 How robust is each algorithm to varying initial conditions and targets? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"), which means that the equality constraints are violated on the initial trajectory.

<!-- chunk {"id": "body-0187", "role": "body", "section": "(R3) How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess?", "weight": 1.0} -->

The results of this task are shown in Table How effectively can we steer multiple shooting methods to avoid bad local minima via the initial guess? ‣ 7 Numerical experiments ‣ Second-Order Constrained Dynamic Optimization"). The multiple-shooting method, except for the AL DDP with exact Hessian can complete the task. SQP is the most successful method among them, achieving the lowest cost and constraint violation.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we have reviewed two families of algorithms for constrained dynamic optimization: constrained DDP derived based on NLP techniques and SQP for dynamical systems. We have also discussed two distinct representations of these methods, namely, single- and multiple-shooting formulations. In addition, we derived a novel single-shooting PDAL DDP and added it to the comparison. Working towards our goal to systematize the research on second-order constrained dynamic optimization, we performed extensive benchmarking and analyzed algorithms based on criteria such as objective function minimization, task completion rate, and constraint satisfaction. Among the different methods, the single-shooting PDAL DDP and multiple-shooting SQP algorithms stand out due to their consistent performance and robust numerical behavior across different systems and tasks. Both algorithms handle the high-dimensionality and non-convexity of trajectory optimization tasks in robotics well. When a small violation of dynamics is allowed, multiple-shooting SQP is the most stable method that can achieve the highest success rate of tasks. Another advantage of the method is that it can accept good initial guesses that help guide the optimization process to the desired trajectory.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Conclusion", "weight": 1.5} -->

On the other hand, when the infeasibility of dynamics is not allowed, the single-shooting PDAL DDP is suitable. This is because the method inherits the dynamical feasibility of the single-shooting DDP. From a computational perspective, PDAL DDP has an advantage over multi-shooting SQP. This advantage originates from the fact that, in SQP, the inner constrained QP problem may typically require additional iterations to achieve convergence. In PDAL DDP and its backward pass, internal QPs are unconstrained and therefore maintain their closed-form representation in which only the inversion of $Q_{uu}$ is required. This is due to the way of how constraints are handled in PDAL DDP via the use of the Augmented Lagrangian. The PDAL DDP has similar performance to the single-AL variant when the problem is simple, but starts to show its superiority as the problem becomes more complex. These two AL-based DDP methods can also be formulated in multiple-shooting formulations, which can take advantage of informed initial guesses.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, we would like to note that although $\log$ barrier DDP struggles to complete tasks, it can be the algorithm of choice when feasibility is prioritized.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

Yuichiro Aoyama: Conceptualization, Formal analysis, Investigation, Software, Methodology, Writing-original draft. Oswin So: Conceptualization, Formal analysis, Investigation, Methodology, Software, Writing-review & editing. Augustinos Saravanos: Investigation, Methodology, Writing-review & editing. Evangelos Theodorou: Conceptualization, Supervision, Project administration, Writing-review & editing.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Ethical considerations", "weight": 1.0} -->

This article does not contain any studies with human or animal participants.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Consent to participate", "weight": 1.0} -->

This article does not contain any studies with human or animal participants.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Consent for publication", "weight": 1.0} -->

Not applicable. {dci} The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article. {funding} The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: Augustinos D. Saravanos and Evangelos A. Theodorou were supported by ARO Award \[grant number W911NF2010151\]; Augustinos D. Saravanos was supported by the A. Onassis Foundation Scholarship.
