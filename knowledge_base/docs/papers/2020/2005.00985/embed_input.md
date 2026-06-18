<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Constrained Differential Dynamic Programming Revisited

Topics include Differential dynamic programming, Constrained optimization, Augmented Lagrangian, Trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Revisits constrained DDP with augmented Lagrangian methods, improving constraint handling within the DDP backward-forward pass framework. Contemporary with ALTRO, but from a different group with a different perspective on convergence.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Differential Dynamic Programming (DDP) has become a well established method for unconstrained trajectory optimization. Despite its several applications in robotics and controls, however, a widely successful constrained version of the algorithm has yet to be developed. This paper builds upon penalty methods and active-set approaches towards designing a Dynamic Programming-based methodology for constrained optimal control. Regarding the former, our derivation employs a constrained version of Bellman's principle of optimality, by introducing a set of auxiliary slack variables in the backward pass. In parallel, we show how Augmented Lagrangian methods can be naturally incorporated within DDP, by utilizing a particular set of penalty-Lagrangian functions that preserve second-order differentiability. We demonstrate experimentally that our extensions (individually and combinations thereof) enhance significantly the convergence properties of the algorithm, and outperform previous approaches on a large number of simulated scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization problems arise very frequently in robotics and controls applications. Examples include finding suitable motions for robotic grasping and manipulation tasks, or minimizing fuel for orbital transfers. Mathematically speaking, such problems require computing a state/control sequence that minimizes a specified cost function, while satisfying the dynamics constraints of the agent. Common methodologies for trajectory optimization rely on optimal control and/or optimization theory. The former approach provides fundamental principles for obtaining solutions (based, for example, on Dynamic Programming or the Hamilton-Jacobi-Bellman equation), which, however, do not scale well with high-dimensional, nonlinear problems. In contrast, standard direct optimization methods can be used for discrete optimal control. The main drawback of these works is that feasibility with respect to dynamics has to be explicitly imposed, thus slowing down the optimization process.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the most successful trajectory optimization algorithms is Differential Dynamic Programming (DDP), originally developed by Jacobson and Mayne. DDP is an indirect method which utilizes Bellman's principle of optimality to split the problem into "smaller" optimization subproblems at each time step. Under mild assumptions on the cost and dynamics, it can be shown that DDP achieves locally quadratic convergence rates. While the original method relies on second-order derivatives, one of its variations, iterative-Linear-Quadratic-Regulator (iLQR), uses only Gauss-Newton approximations of the cost Hessians as well as first-order expansions of the dynamics, which is often numerically advantageous. The aforementioned algorithms have been employed in various applications such as robotic manipulation, bipedal walking and model-based reinforcement learning, to name a few.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While unconstrained DDP has been widely tested and used over the past decades, its constrained counterpart has yet to be properly established. Since most practical applications in controls and robotics include state and/or control constraints (e.g., navigating through obstacles, respecting joint/actuator limits, etc.), off-the-shelf optimization solvers still remain the most popular tool for trajectory optimization among scientists and practitioners. A few works have attempted to extend the DDP framework to the constrained case. considered the case of control bounds by solving several quadratic programs over the trajectory, and dealt with equality constraints only via projection techniques. The works in utilized the Karush-Kuhn-Tucker (KKT) conditions when both state and control constraints are present, with in particular, solving successive quadratic programs in the forward pass of the method., also discussed combining DDP with an Augmented Lagrangian (AL) approach; updated the Lagrange multipliers via forward/backward passes, while, utilized schemes from the standard Powell-Hestenes-Rockafellar (PHR) methodology with first-order approximations of the Hessians.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we build upon the works in to develop a state- and control-constrained version of DDP in discrete time. Specifically, we extend by introducing a slack variable formulation into Bellman's principle, and thus avoid assumptions regarding the active constraints of the problem. Moreover, we propose an Augmented Lagrangian-inspired algorithm, by considering a set of penalty functions that preserves smoothness of the transformed objective function. This property was not satisfied, but is required to establish the convergence properties of DDP. These two methodologies can be used separately, or be properly combined for improved numerical performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will save the in-depth discussion about technical differences between our methods and previous papers for subsequent sections. Nevertheless, we note that a comparison among different constrained optimization methods on various simulated scenarios will be provided, which will highlight the efficiency and generalizability of our approach; something which has been lacking from previous DDP-related schemes. To the best of the authors' knowledge, such an extensive experimental study on constrained trajectory optimization has not been conducted in the past. We believe that the current work is a key step towards the development of a numerically robust, constrained version of Differential Dynamic Programming, and opens up multiple directions for research and further improvements.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remaining of this paper is organized as follows: Section II gives some basics on unconstrained DDP and constrained optimization theory. In Section III we explain our KKT-based DDP algorithm with slack variables (S-KKT), while Section IV discusses our AL-inspired method, as well as a combination thereof. Numerical experiments and in-depth comparisons between our methodologies and previous implementations are provided in Section V. Section VI concludes the paper and discusses possible extensions of the current work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

We will briefly cover here the derivation and implementation of Differential Dynamic Programming (DDP). More details can be found.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

Consider the discrete-time optimal control problem

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

Of paramount importance is the concept of the value function, which represents the minimum cost-to-go at each state and time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

DDP finds local solutions to by expanding both sides of about given nominal trajectories, $\overline{\mathbf{X}}$, $\overline{\mathbf{U}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

After plugging into, we can explicitly optimize with respect to $\delta{\mathbf{u}}$ and compute the locally optimal control deviations. These will be given by

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

Finally, observe that $\delta{\mathbf{u}}^{\ast}$ requires knowledge of the value function on the nominal rollout.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

The equations above are propagated backwards in time, since at the final horizon the value function equals the terminal cost. After the backward pass is complete, a new state-control sequence is determined in a forward pass, and this trajectory is then treated as the new nominal trajectory for the next iteration. The procedure is then repeated until certain convergence criteria are satisfied.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Unconstrained Differential Dynamic Programming", "weight": 1.0} -->

To ensure convergence, $Q_{{\mathbf{u}}{\mathbf{u}}}$ must be regularized, when its positive definiteness cannot be guaranteed. Typically, line-search on $\delta{\mathbf{u}}^{\ast}$ is also performed with respect to the total cost in the forward pass. We finally note that in this paper we consider only first-order expansions of the dynamics as, which tends to be less computationally expensive and more numerically stable than using second-order terms.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Constrained optimization theory", "weight": 1.0} -->

We present here preliminaries on constrained optimization. Due to space limitations, we only consider inequality constraints, though similar results hold for equality constraints.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B1 KKT conditions", "weight": 1.0} -->

for a real vector ${\mathbf{λ}} \in {\mathbb{R}}^{w}$. The Karush--Kuhn--Tucker (KKT) conditions are necessary optimality conditions for problems of the type, and state that a local solution must satisfy \[17, Section 12\]

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B1 KKT conditions", "weight": 1.0} -->

where $\lambda$ now corresponds to the Lagrange multipliers. For this result, we need to assume differentiability of $f$ and $\mathbf{g}$, as well as linear independence of the gradients of active constraints.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B2 Augmented Lagrangian", "weight": 1.0} -->

Let us define the Augmented Lagrangian function corresponding to as

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B2 Augmented Lagrangian", "weight": 1.0} -->

where $\mathbf{λ}$, $\mathbf{μ}$ correspond to the Lagrange multipliers and penalty parameters respectively, while $\mathcal{P}{( \cdot )}$ is the penalty function for inequalities. When $\mathcal{P}{( \cdot )}$ satisfies certain properties, it can be shown that minimization of can give a solution to, under mild assumptions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B2 Augmented Lagrangian", "weight": 1.0} -->

Loosely speaking, the corresponding optimization process can be divided into an inner and outer loop. In the inner loop, a local minimizer is found for by an unconstrained optimization methodology. At the outer loop, the Lagrange multipliers are updated as: $\lambda_{i}\leftarrow{\mathcal{P}^{\prime}{(g_{i},\lambda_{i},\mu_{i})}}$, where ${\mathcal{P}^{\prime}{(y,\lambda,\mu)}}:={\frac{\partial}{\partial y}\mathcal{P}{(y,\lambda,\mu)}}$. Moreover, the penalty parameters are increased monotonically, when constraint improvement is not satisfactory.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B2 Augmented Lagrangian", "weight": 1.0} -->

The most popular Augmented Lagrangian algorithm uses the penalty function $P{(y,\lambda,\mu)} = \frac{1}{2\mu}{(\max{(0,\lambda + \mu y)}^{2} - \lambda^{2})}$ and is known as the Powell-Hestenes-Rockafellar (PHR) method. Despite its success, one key drawback is that the objective function of each subproblem is not twice differentiable, which may cause numerical instabilities when used within second-order algorithms.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B2 Augmented Lagrangian", "weight": 1.0} -->

For completeness, we give the required properties for $\mathcal{P}$ in the appendix, and refer the interested reader to \[17, Section 17\] and.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Constrained DDP using KKT conditions and slack variables", "weight": 1.0} -->

Note that we did not include equality constraints above only for compactness. Our results can be readily extended to this case as well.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Similar to normal unconstrained DDP, the backward pass operates on quadratic approximations of the $Q$ functions about the nominal rollouts (see eqs. ).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

${\overset{\sim}{\mathbf{g}}}_{k}$ above is associated with the constraints influenced directly by states and controls at time instance $t_{k}$. We will discuss later the selection of such constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

We proceed by linearizing the constraints, as well as incorporating the approximate $Q$ function. We have

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

where we have dropped the time index on the constraints and $Q$ derivatives for simplicity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

We will now rewrite the above conditions by considering a set of slack variables, such that ${s_{i} + g_{i}} = 0$ and $s_{i} \geq 0$. Hence, eq. becomes

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

To proceed, we will consider perturbations of the slack variables and Lagrange multipliers about their (given) nominal values. Hence we obtain

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

By omitting the second-order terms, we get

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Moreover, the slack formulation of the inequality constraints will give

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Overall, the obtained KKT system can be written in matrix form as

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

We optimize this system using primal-dual interior point method \[17, chapter 18\]. $\overline{\mathbf{λ}}$ is initialized as $\overline{\mathbf{λ}} = {\mathbf{e}}$ ($\mathbf{\Lambda} = {\mathbf{I}}$) since Lagrange multipliers are required to be positive. For slack variables $s$, they are initialized as

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

where $\epsilon$ is a small positive number to keep $s_{i}$ positive and numerically stable. We used $\epsilon = 10^{- 4}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

It is known that if we use the pure Newton direction obtained by $\mu = 0$, we can take only a small step $\alpha$ before violating ${{\mathbf{s}}^{\mathsf{T}}{\mathbf{λ}}} \geq 0$. To make the direction less aggressive, and the optimization process more effective we reduce $s_{i}\lambda_{i}$ to a certain value based on the average value of elementwise product $s_{i}\lambda_{i}$, instead of zero. Note that $\mu$ is an average value of $s_{i}\lambda_{i}$ and $\mu$ must converge to zero over the optimization process. We satisfy this requirement by multiplying $\sigma$ ($0 < \sigma < 1$) \[17, Chapter 19\].\

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Our goal is to solve the above system analytically, which, as we will find, requires the inversion of $\mathbf{S}$ and $\mathbf{\Lambda}$. It might be the case, however, that these matrices are close to being singular; for example, elements of $\mathbf{S}$ will be close to zero when the corresponding constraints approach their boundaries. To tackle this problem we will perform the following change of variables

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Then the new KKT system can be obtained as

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

We can now avoid singularity issues, since ${\mathbf{\Lambda}{\mathbf{S}}}\rightarrow{\mu_{k}\sigma_{k}}$ (instead of 0) with our new formulation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Now notice that in the backward pass of DDP, we do not have $\delta{\mathbf{x}}$. Hence, our strategy will be to first solve the KKT system on the nominal rollout by substituting ${\delta{\mathbf{x}}} = \mathbf{0}$, and then use our optimal values of $\mathbf{s}$ and $\mathbf{λ}$ as our $\overline{\mathbf{s}}$ and $\overline{\mathbf{λ}}$ for the next KKT iteration.\

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

The step size $\alpha$ must be determined to keep ${\mathbf{s}}_{k}$ and ${\mathbf{λ}}_{k}$ non-negative. The following strategy is also used in interior point methods \[17, Chapter 16\].

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

When there are no negative elements in $\delta{\mathbf{s}}$ or $\delta{\mathbf{λ}}$, the corresponding step sizes are taken to be $\alpha_{s} = 1$ and $\alpha_{\lambda} = 1$. Using this step size, we also update the linearized constraint function and the $Q$ function. For convenience, we write the new ${\overline{\mathbf{u}}}_{k}$ as ${\overline{\mathbf{u}}}_{k} + {\alpha\delta{\mathbf{u}}_{k}^{j - 1}}$. $j - 1$ implies that $\delta{\mathbf{u}}$ is form one iteration before.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Therefore the updated nominal constraint function is

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

For $Q$ function, we expand them around nominal trajectory considering small perturbation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Using this new $\mathbf{Q}$ function we construct Lagrangian as,

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Comparing the above equation with on the nominal trajectory (${\delta{\mathbf{x}}_{k}} = \mathbf{0}$), the new $Q_{\mathbf{u}}$ can be obtained as

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

and the KKT system is iteratively solved, updating $\overline{\mathbf{s}},\overline{\mathbf{λ}}$, and $\mu_{k}$, until the duality measure $\mu_{k}$ is improved to a certain threshold. In this paper we used 0.01 as the threshold.\

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-A Backward Pass", "weight": 1.0} -->

Stacking $\mathbf{g}$, $\mathbf{C}$, and $\mathbf{D}$, we have the linearized constraints

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B Forward Pass", "weight": 1.0} -->

Again, one or two time step propagation of $\mathbf{g}$ shown in backward pass is important, because otherwise ${\mathbf{C}}_{k}$ might be zero, and ${\mathbf{u}}_{k}$ does not show up in the linearized constraint. At time step $N$, constraints ${\mathbf{g}}_{N + 2}^{p}$ are not available because the time horizon ends at time step $N + 1$. Hence, we solve the QP under box constraints

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B Forward Pass", "weight": 1.0} -->

$\mathbf{\Delta}$ is a vector of an adaptive trust region initialized by a relatively large positive value. If the solution is not feasible, $\mathbf{\Delta}$ is made to be smaller by

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-B Forward Pass", "weight": 1.0} -->

This makes the new trajectory closer to the trajectory one iteration before, which is feasible. The trust region is made smaller repeatedly until the solution of the QP becomes feasible.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-C Regularization", "weight": 1.0} -->

In DDP, regularization plays a big role and highly affects the convergence. We use the regularization scheme and scheduling technique proposed.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-C Regularization", "weight": 1.0} -->

Both $\nu_{1}$ and $\nu_{2}$ are positive values. $\nu_{1}$ makes the new trajectory closer to the previous one, while $\nu_{2}$ makes the control step conservative and makes $Q_{{\mathbf{u}}{\mathbf{u}}}$ positive definite.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A AL-DDP and penalty function", "weight": 1.0} -->

Here, we will be using the Augmented Lagrangian approach to extend DDP for solving. We call this technique AL-DDP. The main idea is to observe that partial elimination of constraints can be used on the inequality constraints $\mathbf{g}$ of. This means that the penalty function $\mathcal{P}$ from section II-B2 can only be applied to the inequality state constraints, while the dynamics are implicitly satisfied due to DDP's problem formulation. We will thus be considering the following problem

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-A AL-DDP and penalty function", "weight": 1.0} -->

where $\lambda_{i}^{k}$, $\mu_{i}^{k}$ denote Lagrange multipliers and penalty parameters respectively. We will thus be using the approach discussed in section II-B2, using specifically unconstrained DDP to optimize, followed by an update on the Lagrange multipliers and the penalty parameters.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A AL-DDP and penalty function", "weight": 1.0} -->

Since DDP requires $L_{A}{( \cdot )}$ to be twice differentiable, we selected the penalty function as

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A AL-DDP and penalty function", "weight": 1.0} -->

which can be viewed as a smooth approximation to the Powell-Hestenes-Rockafellar method.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Combination of AL-DDP and KKT frameworks", "weight": 1.0} -->

The Augmented Lagrangian approach is typically robust to initializations of the algorithm, but displays oscillatory behavior near the (local) solution. This can be readily explained from optimization theory, since Multiplier methods generally converge only linearly.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B Combination of AL-DDP and KKT frameworks", "weight": 1.0} -->

The idea here is to combine the two approaches: We begin by using the AL-DDP formulation until a pre-specified precision of the cost and constraints, and subsequently switch to the KKT-based approach of section III. If sufficient improvement is not observed within a few iterations, we switch back to the Augmented Lagrangian method, and reduce the aforementioned tolerances for the "switching" mechanism. We also have one more reason for the combination. By applying the control limited DDP technique in the backward pass of the Augmented Lagrangian method, we can handle the control limits as a hard box constraint. In the control limited DDP method, the feedforward gain ${\mathbf{k}}_{k}$ is obtained as

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B Combination of AL-DDP and KKT frameworks", "weight": 1.0} -->

where ${\mathbf{u}}_{l}$ is the lower and ${\mathbf{u}}_{u}$ is the upper limit of control. For the feedback gain ${\mathbf{K}}_{k}$, corresponding rows to the active control limits are set to be zero. As we will discuss in Section III, our KKT-based method can not handle a situation when state and control constraints conflict with each other. This situation typically happens when initial state is far from desired state and a large control is required. By providing a good initial trajectory from AL for the KKT-based method, our method can successfully handle both state and control constraints.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results", "weight": 1.0} -->

In this section we provide simulation results and comparisons between our method and prior work. We call our method "S-KKT" named after the slack variable and KKT conditions. We also test a slightly different version from S-KKT, in which we use the active set method instead of slack variables, but still use one and two time step forward expansion of the constraint function. More precisely, in this method, constraints are took into account only when they are close to active, and they are linerarized under an assumption that active constraints in current iteration remains to be active in next iteration, that is

<!-- chunk {"id": "body-0064", "role": "body", "section": "Results", "weight": 1.0} -->

Using this assumption, constraints are written as

<!-- chunk {"id": "body-0065", "role": "body", "section": "Results", "weight": 1.0} -->

and QP is solved under this equality constraints instead of. The purpose of showing this algorithm here is to see the effect of slack variables and the assumption. We call this method the "active set method". We evaluate these methods and compare them with the former method. The next step is to combined our methods with other optimization algorithms and evaluate the performance.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-A S-KKT", "weight": 1.0} -->

We evaluate our constrained DDP algorithms in two different systems, a simplified 2D car and a quadrotor.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A1 2D car", "weight": 1.0} -->

. The car has state ${\mathbf{x}} = {\lbrack x,y,\theta,v\rbrack}^{\mathsf{T}}$, and control $u^{\theta}$ on the steering angle and $u_{v}$ on the velocity. We consider a reaching task to ${\mathbf{x}}_{g} = {\lbrack 3,3,\frac{\pi}{2},0\rbrack}^{\mathsf{T}}$ while avoiding three obstacles.The obstacles are formulated as

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-A1 2D car", "weight": 1.0} -->

Fig. 1 shows the result of the task starting from several initial points per algorithm. Optimization starts with six different initial points with no control. Fig. 2 shows the result of starting from initial trajectories. From left to right, a feasible trajectory, slightly infeasible trajectory, and close to the optimal trajectory were used as initial trajectories.\
In the S-KKT algorithm, as we explained in eq. 23 and Algorithm 1, $\overline{\mathbf{s}}$ is initialized by a positive value $\epsilon$. This means that the algorithm regards the initial trajectory feasible even though it is not. We experimentally confirmed that this is fine as long as the violation is small. In fact, this means S-KKT is able to handle initial trajectories that are slightly infeasible, which is something previous constrainted DDP algorithms cannot handle.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-A1 2D car", "weight": 1.0} -->

The procedure of the experiment is as follows. We made several initial trajectories with different amounts of violations by changing the radii of obstacles and used them as initial trajectories of the original problem. In our 2D car setting, original radii of obstacles are 0.5 m. We changed radius to 0.4 and ran the algorithm to get an optimized trajectory. Then, we used this trajectory as an initial trajectory with 0.1 violation for the original problem whose obstacles have 0.5 radii. Our algorithm could successfully handle an initial violation up to 0.3.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A1 2D car", "weight": 1.0} -->

Fig. 3 shows the relationship between cost, max. value of constrained function $\mathbf{g}$ and iteration initialized with several start points. Fig. 4 shows that of starting with initial trajectories. We specified the number of maximum outer iterations to be 15. The algorithm stops either when the max iteration is reached, when the regularizers are larger than the criteria, or the gradient of objective is very small. Introducing the slack variable in our method makes the trajectory smoother and we obtain the lowest converged cost. Our method could also get out of the prohibited region.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A2 Quadroter", "weight": 1.0} -->

We test our algorithm on a quadroter system. The quadroter reaches a goal ${\mathbf{x}}_{g} = {\lbrack 1,5,5\rbrack}^{\mathsf{T}}$ avoiding three obstacles. Fig. 5 shows trajectories starting with four different initial hovering points from three different algorithms, that is, former KKT algorithm, active set method, and S-KKT. And Fig. 6 shows the cost and max. value of the constrained function $\mathbf{g}$. Again, S-KKT has the best performance.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-B1 Control constraints", "weight": 1.0} -->

Because S-KKT can take constraints in consideration only two time steps forward, sometimes state and control constraints conflict with each other. In the 2D car case, for example, a car is trying to reach the target and suddenly finds an obstacle. If the control is not limited, the car can quickly steer to dodge the obstacle. However, if the control is limited, it cannot perform a sudden turn and makes a collision, making the trajectory infeasible. Fig. 7 shows how the control changes over iterations when the control is not limited. In this example, a 2D car starts from a static point with $\mathbf{0}$ initial control and reaches ${\mathbf{x}}_{g}$ explained in Section V-A1. In early iterations, large control spikes are observed. These spikes get smaller in future iterations, because the high control is penalized in the cost function. We can expect the optimizer to make the control spikes smaller than the arbitrary control limits, but there is no guarantee. Therefore S-KKT cannot explicitly apply control constraints to a trajectory as it is.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B1 Control constraints", "weight": 1.0} -->

We solve this problem by combining AL-DDP and S-KKT. Using the control limited DDP technique in the backward pass, AL-DDP can apply control constraints to a trajectory. AL-DDP is very fast for the first few iterations but gets slow when it comes close to the boundary of constraints and sometimes violates the constraints.\
Usually the trajectory oscillates around the boundary. Whereas S-KKT takes relatively a longer time for one iteration, but can keep feasibility. Though S-KKT can not handle a problem in which state and control constraints conflict each other. Typically the conflict happens when the initial state is far from the goal state and it needs to be changed a lot. However, given a good initial trajectory, S-KKT is good at pushing it close to boundary as shown in Fig. 2. We feed S-KKT with the output of AL-DDP and optimize it under the expectation that large control is not required. The concept of the combination is shown in Fig 8. After receiving an optimized trajectory from AL-DDP, S-KKT solves the QP problem in its forward pass shown in eq. with additional box control constraints,

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B1 Control constraints", "weight": 1.0} -->

If the QP problem is infeasible at time step $t_{k}$, we make the control more conservative by multiplying $0 < \eta < 1$ to the box constraints as we do,

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B1 Control constraints", "weight": 1.0} -->

and resolve the QP problem again from $t_{0}$ until the problem can be solved over the entire time horizon. This strategy, making a trajectory closer to a former one until it becomes feasible, is not good when the initial trajectory is far from desired one, and/or large control is required to dodge the obstacles as shown in Fig. 7. In our case, however, thanks to a good initial trajectory from AL-DDP, this strategy fits well with S-KKT.\

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-B2 2D car", "weight": 1.0} -->

To examine the performance of the combination, we used the same problem setting of the 2D car in Section V-A1, and applied control limit as,

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-B2 2D car", "weight": 1.0} -->

The results and comparison between unconstrained control case are shown in Fig. 9. The algorithm could successfully handle both state and control constraints.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B2 2D car", "weight": 1.0} -->

We observed that when the steering control constraint was too tight, the car could only satisfy the desired angle (see pink trajectory in Fig. 9(a)). In its control graph in Fig. 9(b), we can see that maximum steering control was applied to dodge the obstacle and to reach the goal but it was not enough. As shown in the green trajectory in Fig. 9(a), it reached the goal, dodging the first obstacle from the top. Whereas in the control unconstrained case in Fig. 1, it could make a sharp turn and dodge the first obstacle from the bottom. This change can be also seen by comparing Fig. 9(b) and Fig. 9(d). In the constrained case,

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-B2 2D car", "weight": 1.0} -->

(a) Trajectories reaching a goal ${\lbrack 3,3,\frac{\pi}{2},0\rbrack}^{\mathsf{T}}$ starting from static initial points.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C Performance Analysis", "weight": 1.0} -->

Next we perform a thorough analysis between five algorithms, SQP, S-KKT based DDP, AL-DDP, AL-DDP with SQP, and AL-DDP with S-KKT. The SQP algorithm used in this comparison is the one available through Matlab's Optimization Toolbox. For the rest of the algorithms, we have implemented them ourselves. In the five algorithms, the last two, AL-DDP with SQP and AL-DDP with S-KKT are a combination of two different optimization algorithms. In these two combination methods, the algorithms start optimizing using AL-DDP and switch to SQP or S-KKT as explained in IV-B. We compare the five algorithms in terms of performance metrics, namely cost, time, and feasibility, in three systems, cart pole, 2D car, and quadroter. We also specify different time horizons for the same examples. Here the time horizon $H$ is the number of time steps and the time step size $dt$ is fixed in each example. Furthermore, we perform experiments with a time budget as well as letting the algorithms run until they have reached the convergence criteria.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-C Performance Analysis", "weight": 1.0} -->

All of the simulations are performed in Matlab 2019b on a CPU architecture of i7-4820K (3.7 GHz).

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-C Performance Analysis", "weight": 1.0} -->

Note we divide feasibility of the solution into two parts, one is feasibility with respect to the constraint function $\mathbf{g}$ and the other is with respect to the dynamics $\mathbf{f}$. SQP handles them as inequalities (for $\mathbf{g}$) and equalities (for $\mathbf{f}$) constraints, whereas DDP-based methods can implicitly satisfy dynamics since they are used during the optimization process.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-C1 Exit criteria", "weight": 1.0} -->

The exit condition of optimization was based on two criteria as shown in Table I. One was constraint satisfaction, where $1 \times 10^{- 7}$ was used for all the algorithms. The other was an optimality criterion. For the DDP based methods, we used the change in the optimization objective between iterations, set to $8 \times 10^{- 2}$. For SQP, we used an optimality condition shown in the first equation of (II-B1). This condition was set by choosing the Matlab fmincon option OptimalityTolerance to be $1 \times 10^{- 2}$. We first set the value to be $8 \times 10^{- 2}$ which is the same as that of other DDP based methods. However, SQP stopped its optimization process reaching local minima in the early iterations for several examples, which kept the cost of SQP relatively much higher. In the 2D car and the quadroter case for example, the cost was about a hundred times higher than S-KKT. Therefore, we made the criteria smaller to further the SQP optimization process.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-C1 Exit criteria", "weight": 1.0} -->

When using the change of objective function instead of the optimality tolerance in SQP, we observed that the condition was also satisfied in the early iterations of the optimization, but with a large constraint violation. This means that only the constraint satisfaction was working effectively as the exit condition. Thus, we decided to use the optimality tolerance for SQP. For AL-SQP and AL-S-KKT, we also have conditions on exiting the AL optimization scheme and switching to the next scheme as shown in Table I(b)). In lieu of fairness, we decided to keep this "switching condition" and other AL parameters the same between both algorithms even if they may have benefited with different conditions for the overall convergence requirements. For these AL schemes, the constraint satisfaction tolerance was $1 \times 10^{- 2}$ and the bound on the change of the cost was $1$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-C1 Exit criteria", "weight": 1.0} -->

(a) Exit criteria for single algorithms.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-C1 Exit criteria", "weight": 1.0} -->

(b) Exit criteria for combination algorithms.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-C2 Cart Pole", "weight": 1.0} -->

Table II shows the results of the simulations for balancing a cart pole system. The system has four dimension of state $\mathbf{x}$, that is position of the cart $x$, its velocity $\overset{˙}{x}$, angle of the pendulum $\theta$, and angular velocity $\overset{˙}{\theta}$. The control of the system is thrust force $u$ applied to the cart.

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-C2 Cart Pole", "weight": 1.0} -->

where $M$ is a mass of the cart, $m$ is that of pendulum, $l$ is a length of the arm of the pendulum, $g$ is gravitational acceleration, and $b$ is a coefficient of friction between the car and the floor.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-C2 Cart Pole", "weight": 1.0} -->

Pure SQP performed the slowest with dynamics violation, although it achieved a very low cost. It required a much longer time for a longer time horizon compared to other methods. This is understandable because in SQP, a longer time horizon corresponds to a larger matrix (which needs to be inverted) containing the equality constraints for the dynamics. S-KKT also takes time and it accrues a high cost compared to SQP. However, it does satisfy feasibility. AL-DDP on its own cannot reach the same levels of constraint satisfaction as S-KKT, which makes sense since the AL approach oscillates near the constraint bounds, but converges faster. When pairing AL with SQP, there is no significant change compared to original SQP. Pairing AL with S-KKT, however, we see an improvement. In the case of $H = 100$, compared to S-KKT, AL-S-KKT converges faster to an almost equally low cost. In the case of $H = 200$, AL-S-KKT takes slightly longer time, but converges to a lower cost. Compared to AL, AL-S-KKT takes a long time, but satisfies feasibility.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-C2 Cart Pole", "weight": 1.0} -->

From Table III, we can see the longer time horizon decreases the performance of SQP in terms of speed and constraint satisfaction, where AL-S-KKT is not affected as much. In S-KKT, there is a small violation of constraint possibly from the linearization error of the constraint function. The solution may satisfy the linearized constraint, but not the original one. The error decreases as $\delta{\mathbf{u}}$ decreases, but if we use a time budget and stop the optimization process before convergence, there is a possibility that the solution has a small violation.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-C3 2D car", "weight": 1.0} -->

We use the same problem setting as V-A1. For these metrics we initialize the problem with six different starting points and take the average of the cost, time, and feasibility. The time step used was ${dt} = 0.02$ s. Table IV shows the result when we let run the algorithm until convergence, and Table V shows the result under time budget. In the case of $H = 100$, time budget was 3 s, and when $H = 200$, it was 6 s. In this example algorithms behave similarly as the example of a cart pole, and combination methods show their performance more clearly in terms of speed.

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-C4 Quadroter", "weight": 1.0} -->

In this example, we used same problem setting as Section V-A2 initialized with four different static hovering points, and take the average of performance metrics as we did in the 2D car example. We set a time step of ${dt} = 0.01$. As we can see from the results shown in Table VI, SQP suffers from increase of dimension of the problem resulting in a much longer computational time. AL in the case of $H = 300$, could not get out from its inner optimization loop, and could not converge. We filled the corresponding table with "N/A". Our S-KKT and AL-S-KKT, however could keep its stability and feasibility. In addition, they achieved a low cost in a short time. Table VII shows the result from the same problem under a time budget. For $H = 200$, the time budget was 6 s and for $H = 300$ it was 10 s. Single SQP took such a long time that it could not perform one single iteration, resulting in very high cost. We have observed that our AL-S-KKT lost its speed performance affected by the first AL optimization process.

<!-- chunk {"id": "body-0093", "role": "body", "section": "V-C4 Quadroter", "weight": 1.0} -->

AL consumed most of the time budget, allowing S-KKT only one or two iterations. We believe that more investigation or tuning of AL will make our AL-S-KKT much better.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we have introduced novel constrained trajectory optimization methods that outperform previous versions of constrained DDP. Some key ideas in this paper rely on the combination of slack variables together with augmented Lagrangian method and the KKT conditions. In particular,

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Slack variables are an effective way to get lower cost with respect to alternative algorithms relying on the active set method.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The S-KKT method is able to handle both state and control constraints in cases where the feasibility set is small.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The S-KKT methods is more robust to initial conditions of the state trajectory.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conclusion", "weight": 1.5} -->

AL is very fast for first few iterations but get slow when it comes close to constraints and sometimes violate constraints. Whereas S-KKT takes time in one iteration, but can keep feasibility in a few iterations. By combining them we may be able to compensate for weakness of both and have a better algorithm.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future directions will include mechanisms for uncertainty representations and learning, and development of chance constrained trajectory optimization algorithms that have the benefits of the fast convergence of the proposed algorithms.
