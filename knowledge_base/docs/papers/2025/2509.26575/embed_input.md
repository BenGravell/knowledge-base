<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Trajectory Bundle Method: Unifying Sequential-Convex Programming and Sampling-Based Trajectory Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a unified framework for solving trajectory optimization problems in a derivative-free manner through the use of sequential convex programming. Traditionally, nonconvex optimization problems are solved by forming and solving a sequence of convex optimization problems, where the cost and constraint functions are approximated locally through Taylor series expansions. This presents a challenge for functions where differentiation is expensive or unavailable. In this work, we present a derivative-free approach to form these convex approximations by computing samples of the dynamics, cost, and constraint functions and letting the solver interpolate between them. Our framework includes sample-based trajectory optimization techniques like model-predictive path integral (MPPI) control as a special case and generalizes them to enable features like multiple shooting and general equality and inequality constraints that are traditionally associated with derivative-based sequential convex programming methods. The resulting framework is simple, flexible, and capable of solving a wide variety of practical motion planning and control problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear dynamical systems of the form $x_{+}=Ax+Bu$ underpin many of the foundational methods in modern optimal control. Ideas such as the Linear-Quadratic Regulator (LQR) and convex trajectory optimization can reason about dynamical systems of this form in a way that is globally optimal. As a result, these techniques are often applied to nonlinear systems where the dynamics are locally approximated as linear around a linearization point. In many cases, this approximation is appropriate given the function is not being evaluated too far from where the approximation was formed. When used appropriately, this method of linearizing nonlinear systems can be extremely effective in practice, even for highly nonlinear systems. The two caveats here are that the nonlinear system must be both smooth and differentiable.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For many systems, such as robotic arms, quadrotors, and wheeled vehicles, this assumption of smooth differentiability is reasonable. For rigid-body dynamics, there are specialized methods for computing derivatives of the continuous-time dynamics in a fast and efficient way. However, for more complex dynamics models, there are scenarios where these derivatives are unavailable, prohibitively expensive to compute, or unreliable. If the dynamics model is learned from data, the approximation of the dynamics function may be good, while the approximation of the derivatives may be very poor. This scenario is often explored in the context of model-predictive path-integral (MPPI) control, where a learned simulator is only used to produce parallelized simulations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another scenario in which derivatives are unavailable or unusable is in the presence of systems that make or break contact. While there has been a lot of recent interest in making contact simulation differentiable, there remains a strong need for optimal control methods that do not rely on these derivatives at all.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A recent trend in robotic simulation is the introduction of simulators that can be run on accelerators for massively parallel simulation. Popular simulators like Isaac Sim, Brax, and MuJoCo XLA (MJX), are all capable of running thousands of simulations in parallel. This paper leverages the innovations in parallel simulation to motivate a new derivative-free optimal control paradigm where simulation rollouts are used to fully describe the dynamics and cost landscapes present in the problem. We introduce the trajectory bundle method for solving nonconvex trajectory optimization problems, which uses interpolated trajectories instead of derivative-based linearizations to approximate the cost, dynamics, and constraint functions in the problem. The result is a simple and robust trajectory optimization framework that can fully utilize parallelized simulation without requiring any derivatives.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our specific contributions in this paper are the following: A unified framework, which we refer to as the trajectory bundle method, for solving general trajectory optimization problems using derivative-free sequential-convex programming.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A method for approximating general nonlinear or non-convex cost and constraint functions through sampling and linear interpolation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A set of numerical experiments demonstrating the effectiveness of the trajectory bundle method and its equivalence to its SCP and MPPI counterparts.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows: we first review related literature on derivative-free optimization, sequential-convex programming, and MPPI in Section II. Next, we introduce relevant background on affine function approximation and its application to constrained optimization in Section III. In Section IV, we describe the trajectory bundle method in a general multiple-shooting framework and a single-shooting special case that is equivalent to MPPI. Finally, we present an array of numerical experiments in Section V and point avenues of future research in VI.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Derivative-Free Optimization", "weight": 1.0} -->

Derivative-Free Optimization (DFO) is a well-studied technique for solving optimization problems where derivatives are unavailable. John Dennis describes the DFO problem in as "finding the deepest point of a muddy lake, given a boat and a plumb line, when there is a price to be paid for each sounding." With modern accelerators capable of massively parallel dynamics, cost, and constraint evaluation, there is still a price to take soundings, but we can now "buy in bulk." In a seminal 1965 paper, the Nelder-Mead method for derivative-free function minimization was proposed, where a simplex of sample points is used to approximate the cost landscape instead of derivatives. Methods like Mesh Adaptive Direct Search (MADS) and NOMAD followed with improvements to the Nelder-Mead method.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Derivative-Free Optimization", "weight": 1.0} -->

Although there has been much work on general DFO, there are two notably similar approaches to the trajectory bundle method. The first is the Constrained Optimization by Linear Interpolation (COBYLA) solver, where the cost and constraint functions are approximated with linear interpolation, and the second is the Gauss-Newton method of, where samples are used for linear interpolation. The trajectory bundle method builds on these two methods and specializes to trajectory optimization problems where the decision variables at different time steps are only coupled via the dynamics constraints. By exploiting this problem-specific structure and massively parallel simulation, the trajectory bundle method is a simple and robust method for solving trajectory optimization problems to tight constraint and optimality tolerances.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Trajectory Optimization through Sequential-Convex Programming", "weight": 1.0} -->

Trajectory optimization provides a rigorous and powerful mathematical framework for solving general optimal control problems as nonlinear programs. The cost and constraint functions can be arbitrary nonlinear functions that describe the task objective, laws of physics, and physical limits that must be enforced. Assuming the cost and constraint functions are smooth and differentiable, this potentially nonlinear, non-convex problem can be solved by linearizing around a current iterate, forming a convex approximation of the original problem, and iterating until convergence. This method, known as Sequential Convex Programming (SCP), has been applied successfully to a wide variety of robotic systems such as rockets, orbital transfers, fixed-wing aircraft, rotorcraft, autonomous vehicles, and underwater vehicles.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Trajectory Optimization through Sequential-Convex Programming", "weight": 1.0} -->

The trajectory bundle method solves the trajectory optimization problem through sequential-convex programming in a similar fashion to existing work, but differs in the way in which a convex approximation of the problem is formed. Instead of approximating the nonlinear cost and constraint functions by linearizing around the current iterate, we approximate the cost and constraint functions in a derivative-free manner by linearly interpolating samples within a trust region.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Model-Predictive Path Integral Control", "weight": 1.0} -->

Model-predictive path integral control (MPPI) is a sampling-based method for trajectory optimization or model-predictive control in which derivatives of the dynamics and cost functions are not required. The MPPI algorithm was first derived using a path-integral approach then later re-derived from an information theoretic perspective, a stochastic search perspective, as well as through the use of mirror descent in an online learning context.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Model-Predictive Path Integral Control", "weight": 1.0} -->

Given the rise in parallel computer architectures (GPUs and multi-threaded CPUs), MPPI has become a popular approach for tackling challenging real-time optimal control problems because the most expensive part of the algorithm --- evaluating sampled rollouts and their corresponding costs --- can be done entirely in parallel. Additionally, MPPI can be extremely general and naturally amenable to black-box models learned from real-world data. Despite its empirical success, MPPI performs poorly on open-loop unstable systems due to its single-shooting nature, and is unable to directly reason about constraints.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Model-Predictive Path Integral Control", "weight": 1.0} -->

In this paper, we provide a new interpretation of MPPI as a sequential convex programming method and as a special case of the trajectory bundle method, and generalize sample-based optimal control to handle open-loop unstable systems and arbitrary constraints.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Affine Function Approximation", "weight": 1.0} -->

An arbitrary function $p:\mathbf{R}^{a}\rightarrow\mathbf{R}^{b}$ is affine if it can be represented in the following form: $p_{\text{aff}}(y)=d+Cy$, where $d\in\mathbf{R}^{b}$ and $C\in\mathbf{R}^{b\times a}$. The process of locally approximating a nonlinear function with an affine function around a point $\bar{y}$ is often referred to as linearization, with $\bar{y}$ denoted as the linearization point. In this section, the standard method of approximation by first-order Taylor series is presented, followed by a derivative-free method that involves linear interpolation of sampled points.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A1 Taylor Series", "weight": 1.0} -->

An affine approximation of this function ${p}(y)\approx\hat{p}(y)$ can be formed in the vicinity of an input value $\bar{y}$ through the use of the first-order Taylor series, where both the value and the Jacobian of $p$ are calculated at the point $\bar{y}$. This approximation is exact at $\bar{y}$, and, generally speaking, becomes less accurate farther from $\bar{y}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A2 Linear Interpolation", "weight": 1.0} -->

Alternatively, nonlinear functions can be approximated in a derivative-free manner by linearly interpolating between sampled function values. This is useful when the derivatives of a function are unavailable, challenging to compute, or unreliable.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A2 Linear Interpolation", "weight": 1.0} -->

For an affine function, any linear interpolation between two inputs is equal to the linear interpolation of the outputs. This means for an interpolation parameter $\theta\in$ and two inputs $y_{1}$ and $y_{2}$, the following holds: This concept can be extended to $m$ points with an interpolation vector $\alpha\in\mathbf{R}^{m}$ that belongs to a standard simplex: where again the convex combination of these $m$ inputs is equal to the same convex combination of the $m$ outputs, This means that we can locally approximate the original nonlinear function $p$ in the neighborhood of $\bar{y}$ by sampling $m$ points from a distribution centered around $\bar{y}$ with $y_{i}\sim\mathcal{D}(\bar{y})$, and constraining the inputs to this approximation to be a linear combination of the sample points.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A2 Linear Interpolation", "weight": 1.0} -->

For notational convenience, the lists of inputs and outputs are horizontally concatenated as columns of the matrices enabling the affine approximation $\hat{p}$ to be summarized as: We are effectively using the approximation $p(W_{y}\alpha)\approx W_{p}\alpha$, which is linear in $\alpha$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

We will now consider a general nonlinear optimization problem and examine how these linearization techniques can be utilized to form a convex approximation of the original problem. This approach is used in sequential convex programming (SCP) methods where nonconvex optimization problems are solved by iteratively approximating the problem as convex in the neighborhood of the local iterate and solving for a step direction.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

To demonstrate how an SCP method works with the two approximation techniques outlined, we examine a generic constrained optimization problem of the following form: | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle z}{\mathrm{subject~to}}$")][l]{\underset{\displaystyle z}{\mathrm{minimize}}}\quad\|r(z)\|_{2}^{2}\hfil\hfil\hfil\hfil$ | | \(9\) | | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle\phantom{z}}{\mathrm{subject~to}}$")][c]{{\mathrm{subject~to}}}\quad$ | $\displaystyle c(z)$ | $\displaystyle=0,$ | | | with a decision variable $z\in\mathbf{R}^{n_{z}}$, cost residual function

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

By approximating both of these functions as affine with a first-order Taylor series around a current iterate $\bar{z}$, we are left with the following convex optimization problem: | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle z}{\mathrm{subject~to}}$")][l]{\underset{\displaystyle z}{\mathrm{minimize}}}\quad\|\overbrace{r(\bar{z})+\frac{\partial r}{\partial z}(z-\bar{z})}^{\hat{r}(z)}\|_{2}^{2}\hfil\hfil\hfil\hfil$ | | \(10\) | | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle\phantom{z}}{\mathrm{subject~to}}$")][c]{{\mathrm{subject~to}}}\quad$ |

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

$\displaystyle\overbrace{c(\bar{z})+\frac{\partial c}{\partial z}(z-\bar{z})}^{\hat{c}(z)}$ | $\displaystyle=0.$ | | | While this approximate problem is convex and we are guaranteed to find a globally optimal solution if one exists, we do not have a guarantee of feasibility.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

There are circumstances in which the linearization of the constraint function results in infeasible approximate problems.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

In order to guarantee that this problem is always feasible, many sequential convex programming methods convert the constraint into a penalty and reformulate with an always-feasible variant, | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle z, s}{\mathrm{subject~to}}$")][l]{\underset{\displaystyle z,s}{\mathrm{minimize}}}\quad\|\overbrace{r(\bar{z})+\frac{\partial r}{\partial z}(z-\bar{z})}^{\hat{r}(z)}\|_{2}^{2}+\mu\|s\|_{1}\hfil\hfil\hfil\hfil$ | | \(11\) | | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle\phantom{z,

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

s}}{\mathrm{subject~to}}$")][c]{{\mathrm{subject~to}}}\quad$ | $\displaystyle\overbrace{c(\bar{z})+\frac{\partial c}{\partial z}(z-\bar{z})}^{\hat{c}(z)}+s$ | $\displaystyle=0.$ | | | where $\mu\in\mathbf{R}_{+}$ is a positive penalty weight and the $\ell_{1}$-norm discourages constraint violations. No matter the structure of the cost and constraint functions, the convex optimization problem in is guaranteed to always have a solution.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

Alternatively, a linear interpolant such as that shown in can be used to approximate the cost and constraint functions. To do this, $m$ sample points centered around the current iterate $\bar{z}$ are used to evaluate the cost and constraint functions. These values are then horizontally concatenated into the following matrices: The interpolation vector $\alpha\in\mathbf{R}^{m}$ is used to interpolate between these samples and their corresponding cost and constraint values.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Approximation for Optimization", "weight": 1.0} -->

It is important to note the similarities between and, where the only difference is the method to approximate the cost, residual, and constraint functions. Another key difference between these methods is the implicit trust region present in the simplex constraint on $\alpha$. Since $\alpha\in\Delta^{m-1}$, the solution is restricted to the convex hull of the sample points. Using a sampling scheme that only samples points within a set trust region, the solution to is guaranteed to stay within the trust region.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Trajectory Bundle Method", "weight": 1.0} -->

In this section, we outline a canonical trajectory optimization problem specification and use linearly interpolated trajectory bundles to approximate the cost and constraint functions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Trajectory Bundle Method", "weight": 1.0} -->

Trajectories will be represented in discrete time as a list of vectors. For a dynamical system with a state $x\in\mathbf{R}^{n_{x}}$ and control $u\in\mathbf{R}^{n_{u}}$, the discrete-time dynamics function $x^{(k+1)}=f(x^{(k)},u^{(k)})$ maps the state and control at time-step $k$ to the state at $k+1$. A trajectory comprised of $N$ time steps is represented by $(x^{(1:N)},\,u^{(1:N-1)})$, such that numerical optimization can be used to solve for these values.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Trajectory Optimization", "weight": 1.0} -->

We will assume that all relevant constraints are expressed in this form, including initial and goal constraints, state and control limits, and other general stage-wise constraints.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Trajectory Optimization", "weight": 1.0} -->

The problem format in is often referred to as multiple shooting, where both the state and control histories are optimized over, and the trajectory only becomes dynamically feasible at convergence. This differs from single shooting, where only the controls are optimized over, and a rollout is performed to recover the states. One important distinction between these two methods is that in single shooting, the discrete-time dynamics must be evaluated sequentially $N-1$ times during the rollout, while in multiple shooting, the $N-1$ dynamics constraints can be evaluated entirely in parallel. This is especially relevant with GPU-based physics simulation, where the speed of a single simulation can be comparable to thousands of simulations run in parallel.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Solving Multiple Shooting with Trajectory Bundles", "weight": 1.0} -->

The trajectory bundle method is able to reason about the trajectory optimization problem in without having to differentiate any of the cost, dynamics, or constraint functions. Instead of using derivatives to approximate these functions with their first-order Taylor series, sampled trajectories near the current iterate are used to evaluate these functions for approximation with linear interpolation. This idea is shown in III-A Given an initial guess or current iterate $(\bar{x}^{(1:N)},\bar{u}^{(1:N-1)})$, the costs, constraints, and dynamics functions are computed for each of the $M$ samples surrounding each knot points. To demonstrate this, let us examine a single knot point, $k$, where the current iterate is $(\bar{x}^{(k)},\bar{u}^{(k)})$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Solving Multiple Shooting with Trajectory Bundles", "weight": 1.0} -->

From here, $m$ points are sampled near the iterate, and these samples are horizontally concatenated into the following matrices: after which, all of the cost, dynamics, and constraint functions are computed and stored in a similar fashion, where $r_{i}^{(k)}=r(x^{(k)}_{i},u^{(k)}_{i})$, $f_{i}^{(k)}=f(x^{(k)}_{i},u^{(k)}_{i})$, and $c_{i}^{(k)}=c(x^{(k)}_{i},u^{(k)}_{i})$. These matrices are computed for time-steps $1\rightarrow N$, with time-step $N$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Solving Multiple Shooting with Trajectory Bundles", "weight": 1.0} -->

Together, these matrices can be used to locally approximate the potentially nonconvex optimization problem in as the following convex optimization problem: | | |

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Solving Multiple Shooting with Trajectory Bundles", "weight": 1.0} -->

Each time this problem is solved, the new iterates $(x^{(1:N)},u^{(1:N-1)})$ are used to generate $m$ new samples, and the problem is formed and solved again. This SCP-based algorithm repeats until convergence which, in this particular case, is synonymous with constraint satisfaction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C MPPI as a Trajectory Bundle Problem", "weight": 1.0} -->

In MPPI, control policies are sampled and used to generate simulated rollouts with associated costs, and a weighted average based on these costs is used to "blend" the sampled policies, with this process at each controller call, the nominal control policy is converging to local optimality.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C MPPI as a Trajectory Bundle Problem", "weight": 1.0} -->

A single iteration of MPPI starts with $m$ sampled control policies $U^{(1:m)}$ from a distribution centered around a nominal policy $\bar{U}$. Each of these samples is used in a forward dynamics rollout from an initial condition $x_{0}$ and an associated cost $J_{i}$ is computed using the rollout from sample $i$. Using the costs from these rollouts, $J_{1:m}\in\mathbf{R}^{m}$, weights $\alpha\in\mathbf{R}^{m}$ are computed with the softmax function: where $\lambda$ is a non-negative temperature parameter. Using these weights, the resulting updated control policy is a weighted average of the samples, computed as In the limit $\lambda\rightarrow 0$, the MPPI update selects the single best control sequence among the samples, which is also known as predictive sampling.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C MPPI as a Trajectory Bundle Problem", "weight": 1.0} -->

The MPPI update rule can also be derived as a special case of the trajectory bundle method, where the trajectory is represented with single shooting and there are, therefore, no explicit dynamics constraints.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C MPPI as a Trajectory Bundle Problem", "weight": 1.0} -->

Given the $m$ control samples and associated costs, a convex optimization problem solving for the convex combination of trajectories that minimizes the interpolated cost along with a negative entropy regularizer is the following: | | | $\displaystyle\mathmakebox[width("$\underset{\displaystyle\alpha}{\mathrm{subject~to}}$")][l]{\underset{\displaystyle\alpha}{\mathrm{minimize}}}\quad\overbrace{w_{J}^{T}\alpha}^{\hat{J}(u)}-\overbrace{\lambda\sum_{i=1}^{m}\alpha_{i}\log\alpha_{i}}^{\text{entropy regularization}}\hfil\hfil\hfil\hfil$ | | \(25\) | | | |

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C MPPI as a Trajectory Bundle Problem", "weight": 1.0} -->

$\displaystyle\mathmakebox[width("$\underset{\displaystyle\phantom{\alpha}}{\mathrm{subject~to}}$")][c]{{\mathrm{subject~to}}}\quad$ | $\displaystyle\alpha$ | $\displaystyle\in\Delta^{m-1}.$ | | | where $\lambda$ is the regularization parameter, and the convexity of the negative entropy term makes this a convex optimization problem.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C MPPI as a Trajectory Bundle Problem", "weight": 1.0} -->

The solution to this problem can be computed in closed form as. Just like in MPPI, $\lambda\rightarrow 0$ corresponds to the unregularized bundle problem, where the solution is simply the best sample as no linear combination of the samples can produce a lower cost. This interpretation of MPPI gives a new perspective through the lens of convex optimization, which can both provide a deeper understanding of the algorithm and provide opportunities for future work.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Sampling Strategies", "weight": 1.0} -->

We implement multiple sampling strategies, including Gaussian and uniform distributions, but found that performance was largely independent of the distribution. The experiments in the paper use a simple deterministic coordinate-wise perturbation scheme: where $\bar{z}$ is the current iterate, $\Delta z$ defines the trust region, and $e_{i}$ is the unit vector in the $i$-th coordinate direction, and $z_{2n+1}=\bar{z}$. We leave detailed analysis on sampling strategies for future work.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

In this section, we solve several example motion planning and control problems with the trajectory bundle method. In particular, we show that, in *a unified framework*, the trajectory bundle method solves challenging problems typically only associated with *either* derivative-based SCP (Sec. V-A, V-B, V-D1) *or* derivative-free sampling-based (Sec. V-D2) methods. Additionally, we show that the trajectory bundle method combines the strengths of both classes of algorithms by solving a class of problem neither method alone can solve (Sec. V-C).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

Unless otherwise noted, the convex optimization problems are solved with Clarabel^11^1For the examples in V-D, we temporarily used GUROBI due to a CVXPY bug in transcribing large problems to Clarabel. We are working with the CVXPY developers to resolve this issue for the camera-ready version. through CVXPY and we consider TBM to be converged when the maximum constraint violation reaches below $10^{-4}$. An open-source implementation of the solver and experiments will be made available upon publication.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

Reasoning over long horizons Non-differentiable costs and constraints TABLE I: Comparison of different trajectory optimization methods.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A Double Integrator Collision Avoidance", "weight": 1.0} -->

To demonstrate the ability of the trajectory bundle method to handle nonlinear/nonconvex constraints, a collision avoidance example is shown in Fig. 3. In this scenario, an acceleration-limited double integrator ($u=\ddot{x}$) must find a collision-free path to the goal. Without derivative information from these nonconvex constraints, the trajectory bundle method converges to a feasible collision-free trajectory in fewer than 40 iterations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Quatrotor Figure Eight Tracking", "weight": 1.0} -->

In Fig. 4, a quadrotor with rotor-velocity control is tasked with tracking a skewed figure eight path through space over a five-second horizon. The trajectory is discretized into 100 time-steps, and the resulting optimal trajectory smoothly tracks this aggressive reference while maintaining a smooth control commands. The angular velocity of the quadrotor can reach over 200 degrees per second, where the attitude dynamics are highly nonlinear. In fewer than 60 iterations, the trajectory bundle method can solve this problem to the given constraint tolerance. In comparison, even after millions of simulation steps, MPPI fails to stabilize this open-loop unstable system over a long horizon, resulting in an unrecoverable crash.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Quatrotor Figure Eight Tracking", "weight": 1.0} -->

The problems in Sec. V-A and V-B are highly nonlinear/non-convex, highly constrained, and deal with long trajectories. These all present challenges to single-shooting methods like MPPI due to unstable rollouts, a problem noticeably absent from multiple shooting formulations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Cartpole Swingup with a Neural Dynamics Model", "weight": 1.0} -->

Many robotics simulators are unable to produce smooth and reliable derivatives; this can be a result of nonsmooth impact events, but also if the dynamics are represented with a nonsmooth neural network. In the latter case, it is not uncommon for a learned dynamics model to match the values of the real model well, but not the derivatives. In Fig. 5, we solve the canonical cartpole swingup trajectory optimization problem with a neural network dynamics model. In this problem, a horizontal cart with an attached pole must swing itself from its stable equilibrium at the bottom to the unstable equilibrium at the top in 2.5 seconds. The problem is discretized into $50$ time steps. Control bounds and goal constraints are also applied. Using simulated MuJoCo dynamics data, we train a 2-layer multilayer perceptron (MLP) with 64 units per layer and ReLU activation functions to predict the next robot state $x^{(k+1)}$ given the current state $x^{(k)}$ and control $u^{(k)}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Cartpole Swingup with a Neural Dynamics Model", "weight": 1.0} -->

Despite the discontinuous MLP dynamics, TBM successfully solves the problem to tight ($10^{-6}$) tolerance in under $100$ iterations. On the other hand, IPOPT, a standard nonlinear optimization solver relying on derivative information, fails to converge to an optimal solution even after $10,000$ iterations due to the nonsmoothness of the ReLU network. We only show the first $200$ iterations in Fig. 5 for visual clarity.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C Cartpole Swingup with a Neural Dynamics Model", "weight": 1.0} -->

While sample-based MPPI naturally incorporates potentially nonsmooth learned black-box models, it cannot reason over long horizons or about the general state and goal constraints required in many robotics problems like those described in Sec. V-A, V-B, and V-C. As a derivative-free trajectory optimization method, TBM is also amendable to these black-box dynamics models and can handle general (potentially black-box) costs and constraints.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-D Race Car Min-Time Optimization and Local Planning", "weight": 1.0} -->

To demonstrate the capability of TBM in generating both SCP and MPPI solutions in a more complex and highly constrained dynamical system, we focus on a state-of-the-art 1:43 scale autonomous car racing example. This case study has been extensively explored in prior research, and its time-optimality properties are well-established.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-D Race Car Min-Time Optimization and Local Planning", "weight": 1.0} -->

Building on this foundation, we adopt a similar approach to and, utilizing a slip-free bicycle model to describe the vehicle dynamics. The model is defined by the state vector $x=\left[p_{x},p_{y},\psi,v,D,\delta\right]\in\mathbb{R}^{6}$ and the input vector $u=\left[\dot{D},\dot{\delta}\right]\in\mathbb{R}^{2}$, where $\{p_{x},p_{y},\psi,v,D,\delta\}\in\mathbb{R}$ represent the car's position, yaw angle, longitudinal velocity, throttle, and steering angle, respectively. For the full equations of motion and model coefficients, we refer the reader to eq..

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-D Race Car Min-Time Optimization and Local Planning", "weight": 1.0} -->

To ensure the validity of the system dynamics, we impose constraints on the throttle, steering angle, and their respective time derivatives. Furthermore, to uphold the slip-free assumption---which neglects lateral forces acting on the car---we enforce constraints on the longitudinal and lateral accelerations $\{a_{\parallel},a_{\perp}\}\in\mathbb{R}$. Unlike the state and input constraints, the acceleration constraints are nonlinear functions of the states. All relevant numerical values for these constraints, along with their classification by type, are summarized in Table II.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-D Race Car Min-Time Optimization and Local Planning", "weight": 1.0} -->

Having defined the model, we proceed to demonstrate how TBM is capable of retrieving both SCP and MPPI solutions. To achieve this, we divide our experimental analysis into two parts. First, we focus on a trajectory optimization problem, which is typically solved using SCP. Second, we introduce obstacles to the racetrack to formulate a local planning problem, a scenario commonly addressed with MPPI. Through these two experiments, we aim to show that TBM can match the solutions obtained by both the aforementioned methods in highly constrained and complex systems.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

In this section, we focus on offline *trajectory optimization*, where the objective is to compute the minimum-time lap. Originally, this problem is an infinite horizon problem, meaning the integration interval over which the optimization is solved depends on the decision variables. Additionally, the solution to this problem is a trajectory that optimally balances the car dynamics and the track constraints. This involves pushing the throttle and steering to the limits of the tires---reaching the edge of the friction circle where the tires begin to slide---while ensuring the car stays within the track boundaries.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

Due to these factors, the problem is highly non-convex and nonlinear. The success of local gradient-based methods are reliant on careful initialization of the problem and the use of problem-specific heuristics. These heuristics are necessary to ensure that the validity of the gradients is not compromised by taking excessively large steps. In contrast, TBM is gradient-free and does not require such heuristics, making it easier to implement even in the context of such a challenging problem.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

More specifically, the problem is discretized into $N=254$ time steps. The car is initialized in a very simple manner: it is placed at the center of the race track, standing still, and facing forward. The initial state is fully constrained, meaning the car is positioned at the start of the lap with zero velocity. However, for the final state, only the car's position is constrained, while the remaining states (such as velocity and orientation) are left free. This allows the optimization to exploit these degrees of freedom to minimize the lap time. The standard deviations used to generate samples at each iteration are $\sigma_{x}=\left[0.06,0.06,0.17,0.5,0.5,0.17,0.01\right]$ for the state variables and $\sigma_{u}=\left[1,0.5\right]$ for the control inputs.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

Additionally, to explicitly minimize the trajectory's time, the vehicle states are augmented by including the time step $\Delta t$ as an additional variable. This provides direct access to the time variable, enabling the reformulation of the cost function in 22 as: where $\mu=1\times 10^{7}$ is the penalty coefficient that ensures the satisfaction of the state, input, and nonlinear constraints listed in Table II.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

The obtained trajectory, along with the evolution of the solution across different iterations, is illustrated in Fig. 6. Specifically, in Panel A (left side of the figure), we demonstrate how the trajectories evolve from their initial configuration along the centerline of the track to the time-optimal trajectory over 130 iterations. At the bottom of these plots, the evolution of the lap time and constraint violation is displayed. As expected, both metrics decrease until convergence is achieved at iteration 130.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

To further analyze the converged solution, Panel B (right side of Fig. 6) provides a detailed view of the obtained trajectory. Consistent with racing scenarios, the time-optimal trajectory approaches corners from the inner side and exits toward the outside. The lower part of Panel B displays the longitudinal and lateral accelerations, as well as the throttle and steering inputs. These plots reveal that the car's actuation consistently operates at its physical limits, with at least one acceleration component remaining saturated throughout most of the trajectory, ensuring a motion profile that effectively minimizes lap time.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-D1 Trajectory optimization: An SCP case-study", "weight": 1.0} -->

To validate the solution, we compared the TBM trajectory against a benchmark solution obtained from SL1QP, a widely-used gradient-based solver. The results, illustrated by the dotted line in Panel B (upper section), demonstrate remarkable agreement between the two methods. The minimal difference in lap time --just 5ms-- can be attributed to variations in numerical precision and solver tolerances. This close correspondence validates that TBM can generate solutions equivalent to traditional gradient-based methods, even when applied to large-scale problems with complex constraints.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-D2 Local Planning: A MPPI case-study", "weight": 1.0} -->

As discussed in Section IV-C, TBM yields the same solution as MPPI control when an entropy regularization term is added to the cost function. To illustrate this equivalence, we adapt the earlier example of autonomous racing to a common case study where MPPI is frequently applied. Specifically, we introduce $9$ randomly placed obstacles along the race track. This modification renders the previously computed offline trajectory invalid, necessitating the design of a *local planner* capable of completing a lap while avoiding collisions with the obstacles.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-D2 Local Planning: A MPPI case-study", "weight": 1.0} -->

In line with standard MPPI practices and in contrast to traditional gradient-based MPC approaches, predictions are generated by sampling over the solely the control sequence (the derivatives of throttle $\dot{D}$ and steering $\dot{\delta}$). To ensure smoothness and adherence to input bounds, we parameterize these inputs using B-Splines and sample over their control points. This approach leverages the property that every point on a B-Spline curve lies within the convex hull of its control points, thereby guaranteeing that the input constraints are satisfied.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-D2 Local Planning: A MPPI case-study", "weight": 1.0} -->

Once the inputs are sampled, they are simulated in parallel rollouts, and each trajectory is evaluated using a cost function designed to maximize progress along the race track. Due to the single-shooting nature of MPPI---where only inputs are sampled---we lack the ability to directly impose state constraints. To address this limitation, we reject any samples that violate the constraints outlined in Table II, collide with obstacles, or deviate from the track boundaries. This ensures that only feasible trajectories are considered when computing the weighted average of the sampled inputs.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-D2 Local Planning: A MPPI case-study", "weight": 1.0} -->

For this study, we model the system inputs using B-Splines with $100$ control points, generating $m=200$ samples, each comprising $N=20$ time steps. To facilitate a fair comparison between TBM and MPPI, we implement a single-shooting version of TBM by sampling exclusively over the inputs and incorporating the entropy regularization term into the cost function. The temperature parameter for the entropy term is set to $\lambda=1\times 10^{-7}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-D2 Local Planning: A MPPI case-study", "weight": 1.0} -->

Following the mathematical derivations in Section IV-C, the Trajectory Bundle Method (TBM) and Model Predictive Path Integral (MPPI) control produce identical trajectories, depicted by the magenta trajectory in Fig. 7. To provide further insight into this solution, the car's motion is illustrated sequentially using magenta boxes. Each frame also displays the sampled trajectories in gray, along with the TBM/MPPI solution highlighted in red. In Fig. 7, the car successfully completes the lap while avoiding all the obstacles represented as yellow boxes. This example serves as a clear demonstration of the equivalence between TBM and MPPI, showcasing how TBM can achieve the same results as MPPI in practice.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this work, we present the trajectory bundle method, a derivative-free trajectory optimization technique capable of solving nonconvex constrained optimization problems with strong constraint satisfaction. Instead of approximating the nonconvex functions with first-order Taylor series, the trajectory bundle method samples points locally and computes the cost, dynamics, and constraint functions for each of these samples in what we refer to as bundles. These bundles are used to linearly interpolate between these sampled values to approximate the cost, dynamics, and constraint functions. After the computation of these highly parallelizeable function calls, a convex optimization problem is solved where the nonconvex functions are replaced with linear interpolants, and the solution is used to generate new samples for the bundles. The effectiveness of this method is demonstrated on a variety of robotics platforms.

<!-- chunk {"id": "body-0073", "role": "body", "section": "limitations", "weight": 1.5} -->

While the trajectory bundle method is a flexible and capable framework for solving trajectory optimization problems, it is not without limitations. Firstly, while you can readily compute constraint violations for these problems, a reliable metric for optimality is still an open question since derivatives are required to compute optimality conditions. Another challenge has been identifying the ideal distribution to draw samples, while uniform and Gaussian distributions have been sufficient for the examples shown in this paper, there are certainly opportunities to use more expressive and potentially learned distributions for better convergence. The last is a robust convergence rate guarantee, one that will likely require an adaptive penalty $\mu$ and adaptation of the trust region. We leave these challenges open for future work in the area.
