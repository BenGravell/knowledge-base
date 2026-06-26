<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo

Topics include Model predictive control, Predictive sampling, Derivative-free optimization, Real-time, MuJoCo, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces MJPC, an open-source framework for real-time predictive control built on MuJoCo physics, implementing iLQG, Gradient Descent, and a derivative-free Predictive Sampling baseline. Demonstrates that simple sampling-based methods are competitive with classical trajectory optimizers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-based approaches form the foundation of classical control and robotics. Since Kalman's seminal work \Kalman the *state* along with its dynamics and observation models has played a central role.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The classical approach is being challenged by learning-based methods, which forgo the explicit description of the state and associated models, letting internal representations emerge from the learning process \Lillicrap et al., [2015, Schulman et al., 2017, Salimans et al., 2017, Smith et al., 2022, Rudin et al., 2022\]. The flexibility afforded by learned representations makes these methods powerful and general, but the requirement for large amounts of data and computation makes them slow. In contrast, pure model-based methods, like the ones described below, can synthesise behaviour in real time \Tassa et al.,.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since both approaches ultimately generate behaviour by optimising an objective, there is reason to believe they can be effectively combined. Indeed, well-known discrete-domain breakthroughs like AlphaGo \Silver et al., are predicated on combining model-based search and learning-based value and policy approximation. We believe the same could happen for robotics and control, and describe our thinking on how this might happen in the Discussion (Section 5). However, before the community can rise to this challenge, a core problem must be overcome: Model-based optimisation is difficult to implement, often depends on elaborate optimisation algorithms, and is generally inaccessible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this deficit, we present MJPC, an open-source interactive application and software framework for predictive control, based on MuJoCo physics \Todorov et al. which lets the user easily author and solve complex tasks using predictive control algorithms in real time. The tool offers implementations of standard derivative-based algorithms: iLQG (second-order planner) and Gradient Descent (first-order planner). Additionally, it introduces *Predictive Sampling*, a simple zero-order, sampling-based algorithm that works surprisingly well and is easy to understand.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Importantly, the interactive simulation can be slowed down asynchronously, speeding up the planner with respect to simulation time. This means that behaviours can be generated on older, slower machines, leading to a democratisation of predictive control tooling.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

MJPC and Predictive Sampling advance our central goal of lowering the barriers to entry for predictive control in robotics research. An important secondary goal is to accelerate research velocity. When tweaking a parameter, a researcher should not need to wait hours or minutes, but should receive instantaneous feedback -- which will measurably enhance their own cognitive performance \Lu and Dosher,. We believe that flexible, interactive simulation with researcher-authored graphical user interface is not just a "nice to have", but a prerequisite for advanced robotics research.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Optimal control", "weight": 1.0} -->

Optimal Control means choosing actions in order to minimise future costs (equivalently, to maximise future returns). A dynamical system with *state* $x \in \mathbf{R}^{n}$, which takes a user-chosen *control* (or *action*) $u \in \mathbf{R}^{m}$, evolves according to the discrete-time^11^1The continuous-time formulation is generally equivalent, we choose discrete time for notation simplicity. dynamics: returning a new state, $y \in \mathbf{R}^{n}$. The behaviour of the system is encoded via the running cost: a function of state and control, where explicit time-dependence can be realised by folding time into the state. Future costs (a.k.a *cost-to-go* or *value*), can be defined in several ways.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Optimal control", "weight": 1.0} -->

The summation can continue to infinity, leading to the *average-cost* or *discounted-cost* formulations, favoured in temporal-difference learning, which we discuss in Section 5. Here we focus on the *finite-horizon* formulation, whereby the optimisation objective $J$ is given: where subscripts indicated discrete-time indices.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Trajectory optimisation", "weight": 1.0} -->

Solving the finite-horizon optimal control problem, i.e., optimising a fixed-length trajectory, is commonly known as *planning* or *trajectory optimisation*. These algorithms \Von Stryk and Bulirsch, [1992, Betts, 1998\] have a rich history reaching back to the Apollo Program \NASA, [1971, Smith and Yound, 1967\]. An important distinction can be made between two classes of algorithms: *Direct* or *simultaneous* methods have both states and controls as decision variables and enforce the dynamics as constraints. These methods (e.g., Von Stryk) specify a large, sparse optimisation problem, which is usually solved with general-purpose software \Wächter and Biegler, [2006, Gill et al., 2005\]. They have the important benefit that non-physically-realisable trajectories can be represented, for example in order to clamp a final state, without initially knowing how to get to it.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Trajectory optimisation", "weight": 1.0} -->

*Shooting* methods like Differential Dynamic Programming \Jacobson and Mayne, use only the controls $u_{0:T}$ as decision variables and enforce the dynamics via forward simulation. In the shooting approach only physically-realisable trajectories can be considered, but they benefit from the reduced search space and from the optimiser not having to enforce the dynamics. The latter benefit is especially important for stiff systems like those with contact, where the difference between a physical and non-physical trajectory can be very small^22^2For example, consider the physical scenario of a free rigid box lying flat on a plane under gravity, and then consider the non-physical scenario of the same box hovering above the plane or penetrating it by a few microns.. Unlike *direct* methods which require dynamics derivatives, shooting methods can employ derivative-free optimisation, as discussed below.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Predictive control", "weight": 1.0} -->

1:Read the current action u from the nominal plan Π, apply it to the controlled system. 1:Measure the current state x. 2:Using the nominal Π to warm-start, optimise the finite-horizon objective J. Algorithm 1 Predictive Control (asynchronous) The key idea of Predictive Control, invented in the late 60s and first published in \Richalet et al. is to use trajectory optimisation in *real-time* as the system dynamics are evolving. This class of algorithm has been successfully deployed in numerous real-world settings including: chemical and nuclear process control \Na et al., [2003, Lopez-Negrete et al., 2013\], navigation for autonomous vehicles \Falcone et al. and whole-body control of humanoid robots \Kuindersma et al.,.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Predictive control", "weight": 1.0} -->

In the real-time setting, the current state $x$ needs to be estimated or measured, and the trajectory optimiser is required to return a set of optimal or near-optimal controls for the finite-horizon (here often called the *receding horizon*) problem, starting at $x$. We use $\mathbf{\Pi}$ to denote the *plan*, the finite-horizon policy. In the context of shooting methods $\mathbf{\Pi} = u_{0:T}$, though as we discuss later, in some cases it can be re-parameterised, rather than using the discrete-time control sequence directly. Predictive control is best thought of in terms of two asynchronous processes, the *agent* and the *planner*, see Algorithm 1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Predictive control", "weight": 1.0} -->

Predictive Control has the following notable properties: Faster computation improves performance. The reason for this is clear, the more optimisation steps the planner can take in one unit of time, the better the optimised control sequences will be.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Predictive control", "weight": 1.0} -->

Warmstarting has a large beneficial effect. By reusing the plan from the previous planning step, the optimiser only needs to make small modifications in order to correct for the changes implied by the new state. Warm-starting also leads to an amortisation of the optimisation process across multiple planning steps.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Predictive control", "weight": 1.0} -->

The optimisation is not required to converge, only to improve, see Section 5.1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Predictive control", "weight": 1.0} -->

Tasks with a behaviour timescale much longer than the planning horizon $T$ are often still solvable, though this property is task dependent.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Predictive control", "weight": 1.0} -->

Predictive controllers can easily get stuck in local minima, especially those using derivatives. This is due to the myopic nature of the optimisation, and can be addressed by terminating the rollout with a value function approximation, see Section 5.3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Derivative-free optimisation", "weight": 1.0} -->

One of the main reasons for our initial focus on shooting methods is their ability to make use of derivative-free optimisation, also known as *sampling-based* optimisation \Audet and Hare,. Despite not leveraging problem structure or gradient information, this class of algorithms can discover complex behaviours \Salimans et al., [2017, Mania et al., 2018\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Derivative-free optimisation", "weight": 1.0} -->

Sampling-based methods maintain a search distribution over policy parameters and evaluate the objective at sampled points in order to find an improved solution. Popular algorithms include: random search \Matyas genetic algorithms \Holland and evolutionary strategies \Rechenberg including CMA-ES \Hansen and Ostermeier,.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Derivative-free optimisation", "weight": 1.0} -->

This class of algorithms has a number of desirable properties. First, because derivative information is not required, they are well-suited for tasks with non-smooth and discontinuous dynamics. Second, these methods are trivially parallelisable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Derivative-free optimisation", "weight": 1.0} -->

Sampling-based methods have been used in the predictive control context, but not very widely. Notable exceptions are Hämäläinen's work \Hämäläinen et al. which is an early precursor to MJPC, and the oeuvre of Theodorou including \Williams et al., and related papers. While these methods are usually considered to be sample inefficient, we explain below why, specifically in the predictive control context, they can be surprisingly competitive.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MuJoCo MPC (MJPC)", "weight": 1.0} -->

We introduce MJPC, an open-source interactive application and software framework for predictive control, that lets the user easily synthesise behaviours for complex systems using predictive control algorithms in real time. Behaviours are specified by simple, composable objectives that are risk-aware. The planners, including: Gradient Descent, Iterative Linear Quadratic Gaussian (iLQG), and Predictive Sampling are implemented in C++ and extensively utilise multi-threading for parallel rollouts. The framework is asynchronous, enabling simulation slow-down and emulation of a faster controller, allowing this tool to run on slow machines. An intuitive graphical user-interface enables real-time interactions with the environment and the ability to modify task parameters, planner and model settings, and to instantly see the effects of the modifications.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Physics Simulation", "weight": 1.0} -->

We build MJPC using the API of the open-source physics engine MuJoCo \Todorov et al.,. MuJoCo is a good infrastructure for an interactive framework for robotics algorithms for two main reasons: first, MuJoCo supports simulating multiple candidate future trajectories in parallel by offering a thread-safe API, which maximises the utilisation of modern multi-core CPU architectures; second, MuJoCo affords faster-than-realtime simulation of high-dimensional systems with many contacts --- for example, the humanoid (a 27-DoF system) can be simulated 4000 times faster than realtime on a single CPU thread.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Objective", "weight": 1.0} -->

MJPC provides convenient utilities to easily design and compose costs in order to specify an objective; as well as automatically and efficiently compute derivatives.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Costs", "weight": 1.0} -->

We use a "base cost" of the form: This cost is a sum of $M$ terms, each comprising: A nonnegative weight $w \in \mathbf{R}_{+}$ determining the relative importance of this term.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Costs", "weight": 1.0} -->

The residual $r \in \mathbf{R}^{p}$ is a vector of elements that are "small when the task is solved".

<!-- chunk {"id": "body-0030", "role": "body", "section": "Risk sensitivity", "weight": 1.0} -->

We augment the base cost (4 ‣ Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo")) with a risk-aware exponential scalar transformation, $\rho:{{\mathbf{R}_{+} \times \mathbf{R}}\rightarrow\mathbf{R}}$, corresponding to the classical risk-sensitive control framework \Jacobson, [1973, Whittle, 1981\]. The final running cost $c$ is given: The scalar parameter $R \in \mathbf{R}$ denotes risk-sensitivity. $R = 0$ (the default) is interpreted as risk-neutral, $R > 0$ as risk-averse, and $R < 0$ as risk-seeking. The mapping $\rho$ (see Figure 1 ‣ Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo")) has the following properties: Defined and smooth for any $R$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Risk sensitivity", "weight": 1.0} -->

If $R = 0$, is the identity ${\rho{(l;0)}} = l$ (in the limit).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Risk sensitivity", "weight": 1.0} -->

Non-negative: If $l \geq 0$ then ${\rho{(l;R)}} \geq 0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Risk sensitivity", "weight": 1.0} -->

Note that for negative $R$, the transformation $\rho$ creates costs that are similar to the bounded rewards commonly used in reinforcement learning. For example, when using the quadratic norm ${\text{n}{(r)}} = {r^{T}Wr}$ for some SPD matrix $W = \Sigma^{- 1}$ and a risk parameter $R = {- 1}$, we get an inverted-Gaussian cost $c = {1 - e^{- {r^{T}\Sigma^{- 1}r}}}$, whose minimisation is equivalent to maximum-likelihood maximisation of the Gaussian. This leads to the interesting interpretation of the bounded rewards commonly used in RL as *risk-seeking*. We do not investigate this relationship further in this paper.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Derivatives", "weight": 1.0} -->

MuJoCo provides a utility for computing finite-difference (FD) Jacobians of the dynamics, which is efficient in two ways. First, by avoiding re-computation where possible, for example when differencing w.r.t. controls, quantities that depend only on positions and velocities are not recomputed. Second, because FD computational costs scale with the dimension of the *input*, outputs can be added cheaply. MuJoCo's step function ${y,r} = {f{(x,u)}}$, computes both the next state $y$ and sensor values $r$, defined in the model. Because the FD approximation of the Jacobians, scales like the combined dimension of $x$ and $u$, adding more sensors $r$ is effectively "free". MJPC automatically and efficiently computes cost derivatives as follows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gradients", "weight": 1.0} -->

Cost gradients are computed: The norm gradients, $\partial{\text{n}/{\partial r}}$, are computed analytically.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Hessians", "weight": 1.0} -->

Second-order derivatives use the Gauss-Newton approximation, ignoring second derivatives of $r$: The norm Hessians, $\partial^{2}{\text{n}/{\partial r^{2}}}$, are computed analytically.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Splines", "weight": 1.0} -->

As we explain below, planners like iLQG require the *direct* control-sequence representation $u_{0:T}$ due to the requirements of the Bellman Principle. Without this constraint, controls can be "compressed" into a lower-dimensional object. There are many ways to do this, we picked the simplest: splines. Action trajectories are represented as a time-indexed set of knots, or control-points, parameterised by a sequence of monotonic time points $\tau_{0:P}$ and parameter values $\theta_{0:P}$, where we use the shorthand $\theta = \theta_{0:P}$. Given a query point $\tau$, the evaluation of the spline is given: We provide three spline implementations: traditional cubic Hermite splines, piecewise-linear interpolation, and zero-order hold. See (Fig. 2 ‣ Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo")) for an illustration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Splines", "weight": 1.0} -->

The main benefit of compressed representations like splines is that they reduce the search space. They also smooth the control trajectory, which is often desirable. Spline functions belong to the class of linear bases, which includes the Fourier basis and orthogonal polynomials. These are useful because they allow easy propagation of gradients from the direct representation $\partial\mathbf{\Pi}$ back to the parameter values $\partial\theta$. In our case this amounts to computing: which has a simple analytic formula (see code for details). Unlike other linear bases, splines have the convenient property that bounding the values $\theta$ also bounds the spline trajectory. This is exactly true for the zero and linear interpolations, and mostly-true for cubic splines. Bounding is important as most physical systems clamp controls to bounds, and there is no point searching outside of them. Expressions for cubic, linear and zero interpolations are provided in Appendix A.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Planners", "weight": 1.0} -->

MJPC includes two derivative-based planners.

<!-- chunk {"id": "body-0040", "role": "body", "section": "iLQG", "weight": 1.0} -->

1:initial state x0, nominal plan Π = u0: T 2:Roll out nominal trajectory from x0 using Π 3:Compute action improvements and feedback policy using Dynamic Programming. 4:Roll out parallel line search with feedback policy. 5:Best actions are new nominal actions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "iLQG", "weight": 1.0} -->

The iLQG^33^3Equivalently, "iLQR", since we don't make use of the noise-sensitive term for which iLQG was originally developed \Li and Todorov,. We keep the name "iLQG" due to its provenance. planner \Tassa et al. a Gauss-Newton approximation of the DDP algorithm \Jacobson and Mayne utilises first- and second-order derivative information to take an approximate Newton step over the open-loop control sequence $u_{0:T}$ via dynamic programming \Kalman producing a time-varying linear feedback policy: The *nominal*, or current best trajectory, is denoted with overbars ($\overline{}$), $K$ is a feedback gain matrix, and $k$ is an improvement to the current action trajectory. A parallel line search over the step size $\alpha \in {\lbrack\alpha_{\text{min}},1\rbrack}$ is performed to find the best improvement. Additional enhancements include a constrained backward pass \Tassa et al., that enforces action limits and adaptive regularisation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "iLQG", "weight": 1.0} -->

The details of iLQG are too involved to restate here, we refer the reader to the references above for details.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Gradient descent", "weight": 1.0} -->

1:initial state x0, nominal plan Π (θ) 2:Roll out nominal from x0 using Π (θ) 5:Roll out parallel line-search with 6:Pick the best one: θ ← argmin (J (θ(i))) Algorithm 3 Gradient Descent This first-order planner, known as Pontryagin's Maximum Principle \Mangasarian utilises gradient information to improve action sequences, here represented as splines. The gradient of the total return is used to update the spline parameters, using a parallel line search over the step size $\alpha \in {\lbrack\alpha_{\text{min}},\alpha_{\text{max}}\rbrack}$: The total gradient is given: where the spline gradient $\partial{\mathbf{\Pi}/{\partial\theta}}$ is given by (10 ‣ Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo")), while $\partial{J/{\partial\mathbf{\Pi}}}$ is computed with the Maximum Principle.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Gradient descent", "weight": 1.0} -->

Letting $\lambda$ denote the *co-state*, the gradients with respect to $u$ are given: The primary advantage of this first-order method compared to a computationally more expensive method like iLQG is that optimisation is performed over the smaller space of spline parameters, instead of the entire (non-parametric) sequences of actions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Predictive Sampling", "weight": 1.0} -->

Parameters: N rollouts, noise scale σ 1:initial state x0, nominal plan Π (θ) 3:Including θ, roll out all N samples from x0 4:Pick the best one: θ ← argmin (J (θ(i))) Algorithm 4 Predictive Sampling This is a trivial, zero-order, sampling-based Predictive Control method that works well and is easy to understand. Designed as an elementary baseline, this algorithm turned out to be surprisingly competitive with the more elaborate derivative-based algorithms.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm", "weight": 1.0} -->

A nominal sequence of actions, represented with spline parameters, is iteratively improved using random search \Matyas,. At each iteration, $N$ candidate splines are evaluated: the nominal itself and $N - 1$ noisy samples from a Gaussian with the nominal as its mean and fixed standard deviation $\sigma$. After sampling, the actions are clamped to the control limits by clamping the spline parameters $\theta$. Each candidate's total return is evaluated and the nominal is updated with the best candidate. See Algorithm 4 ‣ Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo") and pseudocode in Appendix C. Predictive Sampling is not innovative or performant, but is presented as a simple baseline, see Discussion below.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

We provide a short textual description of our graphical user interface (GUI) for three example tasks. They are best understood by viewing the associated video at dpmd.ai/mjpc or better yet, by downloading the software and interacting with it.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Graphical User Interface", "weight": 1.0} -->

The MJPC GUI, shown and described in Fig. 3, provides an interactive simulation environment, as well as modules containing live plots and parameters that can be set by the researcher. The intuitive interface makes policy design easy by enabling the researcher to interactively change cost parameters or planner settings and immediately see the results in both the simulation environment and live plots, allowing fast debugging and an enhanced understanding of the factors that influence behaviour.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Examples", "weight": 1.0} -->

(a) Humanoid standing up off the floor.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Examples", "weight": 1.0} -->

(b) Quadruped rolling off its back to stand up.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Examples", "weight": 1.0} -->

(c) Hand manipulating a cube to a goal orientation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Examples", "weight": 1.0} -->

In the following examples, we demonstrate the ability to synthesise complex locomotion and manipulation behaviours for a variety of high-dimensional systems in simulation on a single CPU. Further, we demonstrate that the behaviours are robust to disturbances and mismatch between the simulation and planning model, and can adapt extremely quickly in new scenarios. For all of the examples, the total planning time for a single update is between 1 and 20 milliseconds. We highlight three examples below and provide additional examples with the software. Experimental details for objectives and planner settings are found in the Appendix B.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Humanoid", "weight": 1.0} -->

This 27-DOF human-like system, from DeepMind Control Suite \Tunyasuvunakool et al. has 21 actions and is tasked with standing. The system can be initialised on the floor and quickly stands in a manner that is robust to large disturbances. If a sufficiently large disturbance knocks the humanoid onto the floor, the system will stand back up (Fig. 4(a)).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Quadruped", "weight": 1.0} -->

A Unitree A1 quadruped \Unitree from MuJoCo Menagerie \MuJoCo Menagerie Contributors exhibits agile behaviour to traverse uneven terrain which includes walking over a steep slope. On slower machines, the quadruped often struggles to ascend. In this scenario, the simulation slow down can be effectively utilised to provide the planner with addition simulation time to plan a successful climb. The system is also capable of rolling off its back and standing up (Fig. 4(b)). In order to perform long-horizon tasks like continuously navigating the terrain, a series of target poses are set. Once a goal is reached, an automatic transition occurs and the next target is set.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Hand", "weight": 1.0} -->

A Shadow Hand \Tuffield and Elias also from MuJoCo Menagerie, performs in-hand manipulation of a cube to a desired orientation (Fig. 4(c)), where this goal can be set by the researcher in real-time by interactively setting the target orientation. In-hand reorientation---a high-DoF system with complex contact dynamics---is considered difficult to solve \Chen et al., and to the best of our knowledge has not previously been solved from scratch, in real time.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion", "weight": 1.5} -->

The thrust of this paper is to make predictive control accessible via customisable, interactive, open-source tooling. We believe that responsive, GUI-based tools are a prerequisite for accelerated robotics research, and that due to their importance, these tools should be modifiable and the inner workings transparent to the researcher. We hope that our MJPC project will be embraced by the community, and look forward to improving and extending it together.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Predictive Sampling", "weight": 1.0} -->

The effectiveness of this simple method suggests that fast, approximate optimisation can be competitive with more sophisticated methods which return better solutions but at a lower rate. Does the higher planning rate completely explain this surprising effectiveness? We believe there is another, subtler reason. Predictive Control is not well-described by the tenets of traditional optimisation. For example, it usually makes no sense to take more than one step of optimisation. Once a single iteration is complete, it is more important to measure a new value of the state and re-plan, than it is to continue to converge to the minimum of an already-outdated problem. The constant shifting of the optimisation landscape makes Predictive Control a *qualitatively different problem*, more like surfing than mountain climbing. The goal is not to find the minimum, but to *remain in the basin-of-attraction of the minimum*. This is a different, weaker criterion, at which simple algorithms fair better than when measured by the traditional yardstick of convergence.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Predictive Sampling", "weight": 1.0} -->

To be clear, Predictive Sampling is not a novel algorithm; instead, it is a baseline. A corner-case of many existing methods, it can variously be described as "MPPI with infinite temperature", "CEM with a non-adaptive distribution" or just "trivial random search". Better algorithms exist, but none are so easy to describe or implement. We are introducing Predictive Sampling not because it is good, but because it is *not good*. It is the simplest possible sampling-based shooting method, and therefore establishes a *lower bound* for performance baselines.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Use cases", "weight": 1.0} -->

Before we discuss limitations and their possible resolutions, it is worth asking how can MJPC be used *now*, as it is described above?

<!-- chunk {"id": "body-0060", "role": "body", "section": "Use cases", "weight": 1.0} -->

Task design. MJPC makes it easy to add new tasks, expose task parameters to the GUI, and quickly generate the desired behaviour. The task can then be re-implemented in any other framework of choice. While we have not yet implemented time-dependent tasks, it is possible and easy; we expect MJPC to work especially well for motion-tracking tasks.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Use cases", "weight": 1.0} -->

Data generation. MJPC can be used to generate data for learning-based approaches, i.e., it can act like an "expert policy". In this context, it is often the case that the model and task from which the data is generated do not have to exactly match the one used by the learner, and the data can likely be useful for a wide range of setups.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Use cases", "weight": 1.0} -->

Predictive Control research. For researchers interested in Predictive Control itself, MJPC provides an ideal playground. MJPC can switch planners on-the-fly, and its asynchronous design affords a fair comparison by correctly accounting for and rewarding faster planners.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Can only control what MuJoCo can simulate", "weight": 1.0} -->

This is a general limitation of Predictive Control and is in fact stronger since one can only control what can be simulated *much faster than real-time*. For example, it is difficult to imagine any simulation of a very-high-DoF system, like fluid, cloth or soft bodies advancing so fast. One solution is improved simulation using a combination of traditional physics modeling and learning, e.g., \Ladicky et al.,. Another possibility is to entirely learn the dynamics from observations. This approach, often termed Model Based Reinforcement Learning is showing great promise \Heess et al., [2015, Nagabandi et al., 2020, Wu et al., 2022\]. We would recommend that where possible, when attempting Predictive Control using learned dynamics models, a traditional simulator be employed as a fallback as in \Schrittwieser et al. to disambiguate the effects of modeling errors.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Myopic", "weight": 1.0} -->

The core limitation of Predictive Control is that it is *myopic* and cannot see past the fixed horizon. This can be ameliorated in three conceptually straightforward ways: Learned policies. By adding a learned policy, information from past episodes can propagate to the present via policy generalisation \Byravan et al.,. This approach is attractive since it can only *improve* performance: when rolling out samples, one also rolls out the proposal policy. If the rollout is better, it becomes the new nominal. A learned policy is also expected to lead to more stereotypical, periodic behaviours, which are important in locomotion.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Myopic", "weight": 1.0} -->

Value functions. Terminating the rollout with a learned value function which estimates the remaining cost-to-go is the obvious way by which to increase the effective horizon. Combining learned policies and value functions with model-based search would amount to an "AlphaGo for control" \Silver et al., [2016, Springenberg et al., 2020\].

<!-- chunk {"id": "body-0066", "role": "body", "section": "Myopic", "weight": 1.0} -->

High-level agent. A predictive controller could be used as the low-level module in a hierarchical control setup. In this scenario, the actions of the high-level agent have the semantics of setting the cost function of the predictive controller. The predictive controller remains myopic while the high-level agent contains the long-horizon "cognitive" aspects of the task. A benefit of this scenario is that the high-level actions have a much lower frequency than required for low-level control (e.g., torques).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Hardware", "weight": 1.0} -->

MJPC is aimed at robotics research, which raises the question, can it be used to control hardware?

<!-- chunk {"id": "body-0068", "role": "body", "section": "Hardware", "weight": 1.0} -->

Transfer learning. As mentioned in 5.2, using MJPC to generate data which can then be transferred to a real robot is already possible.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Hardware", "weight": 1.0} -->

Estimation. The most obvious yet difficult route to controlling hardware is to follow in the footsteps of classic control and couple MJPC to an estimator providing real-time state estimates. In the rare cases where estimation is easy, for example with fixed-base manipulators and static objects, controlling a robot directly with MJPC would be a straightforward exercise. The difficult and interesting case involves free-moving bodies and contacts, as in locomotion and manipulation. For certain specific cases, like locomotion on flat, uniform terrain, reasonable estimates should not be difficult to obtain. For the general case, we believe that contact-aware estimation is possible following the approach of \Lowrey et al. but that remains to be seen. Relatedly, we believe that high-quality estimators also require the same kind of interactive, GUI-driven interface used by MJPC.
