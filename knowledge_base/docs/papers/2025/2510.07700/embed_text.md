## Introduction

Dynamic motion planning problems are often formulated as constrained trajectory optimization problems of the form These problems can be solved online using a numerical non-linear programming (NLP) solver, which performs optimization on an initial guess until convergence to locally optimal solutions, often using first or second order numerical algorithms such as Newton-Raphson, BFGS, etc.

While trajectory optimization has been successful for many systems, it struggles to optimize in the non-convex, non-smooth landscapes introduced by systems such as manipulators and legged robots. Feasible and performant trajectory optimization in these domains relies on hand-crafted initialization and contact schedules. Additionally, not all dynamic models or simulators are differentiable and thus can not provide derivative information for optimization. Recently, the robotics community has embraced learning-based methods such as imitation learning and reinforcement learning due to their empirically strong performance for problems on which trajectory optimization struggles.

Diffusion models, which have gained popularity for their ability to generate realistic images, have demonstrated impressive performance in representing learned control policies. However, the model-free nature of standard diffusion models discounts the knowledge we have about system dynamics and task objectives, which has led to the development of diffusion algorithms that incorporate model knowledge for trajectory optimization. These approaches can augment learning-based diffusion with model knowledge, or even run diffusion without any learning.

Compared to optimization approaches, these approaches provide multi-modal trajectory sampling, less susceptibility to local minima, the ability to incorporate learning, and optimize through non-smooth dynamics such as contact. Compared to learning-only diffusion models, they can incorporate knowledge of dynamics and objectives, benefiting generalization in new contexts, and offer flexible inference without retraining or gathering new data. Model-based diffusion (MBD) uses Monte Carlo approximations of the Stein score function to run a learning-free reverse diffusion process, providing a zeroth-order sampling-based alternative to traditional gradient-based optimization.

Figure 1: Our proposed method improves the performance of Model Based Diffusion by augmenting the underlying target distribution over the reverse process with a log barrier cost Motion planning problems often have constraints such as collision avoidance or dynamic safety, which gradient-based methods have mature ways to incorporate. In the MBD framework, infeasible solutions result in zero-probability regions on the support of the distribution. Although various methods for enforcing constraints on learning-based diffusion have been proposed, they do not translate to MBD due to its reliance on Monte Carlo sampling which is also affected by the constraints. When infeasible solutions cover a large part of the solution space, the score estimate's value is dominated by rare events on the Monte Carlo proposal distribution, degrading performance.

The contributions of this paper are: We show that MBD can suffer catastrophic performance degradation in highly constrained state spaces due to poor score estimation.

We propose Emerging Barrier MBD, which augments MBD with a time-varying barrier for constraint guidance towards higher-quality and guaranteed feasibility.

We analyse the sampling statistics of the EB-MBD process and study the design trade-offs of the barrier hyperparameters.

We compare EB-MBD to MBD and projection-based constrained diffusion methods in simulation experiments and show that it provides better performance at a fraction of the computational cost.

## Related Work

### II-A Diffusion Models

Diffusion Models simulate a noising diffusion process until a time where the distribution is stationary and easy to sample , and train a neural network to learn the score function (or a discretized equivalent) of the process. This allows generative modelling by sampling from the simpler stationary distribution and running the reverse processes to obtain samples from the target distribution.

Diffusion models have shown great capability in sampling from complex modalities and distributions such as images, videos, and text, but have been used in robotics for representing policies and planners via imitation learning and reinforcement learning. Compared to other types of policy representations, diffusion models excel at representing multi-modal distributions. For robotics, they also enable simple conditional guidance mechanisms to allow task-specific sampling.

While various attempts have been made to run diffusion models with constraints, they usually involve modifying the training process. uses log barriers for constrained diffusion to modify the diffusion step size through the Riemannian metric induced by the barrier's Hessian. However, this method is limited to convex constraints. Alternatively, they may try to enforce constraints on a pre-trained model during the denoising steps. Many of these approaches only focus on learned diffusion models and do not translate to Monte Carlo score estimation which brings additional challenges due to how they are affected by constraints. Additionally, many use computationally expensive operations like projections onto non-convex constraint sets or optimization problems which are passed to numerical NLP solvers whose solution quality and computation time can depend heavily on the initial guess and cost functions.

### II-B Trajectory optimization

Trajectory optimization poses motion planning problems as non-linear programming problems. Trajectory optimization uses the rich theory of numerical optimization with the ability to specify and enforce constraints through various methods such as penalty methods, barrier methods, augmented Lagrangian methods, projected gradient descent, etc. Most relevant to this work, interior point methods use log barriers that enforce infinite cost at the boundary of the constraint and involve repeatedly solving the barrier-augmented optimization problem but with reducing the weight or "hardness" of the barrier until convergence to the true solution.

However, gradient-based optimization is difficult to parallelize, cannot deal with non-smooth objectives, and suffers from local minima. Gradient-free trajectory optimization has been studied to address some problems with gradient-based optimization. Sampling-based optimal control algorithms such as STOMP, MPPI and its variants have shown strong ability to deal with complex non-linear systems.

In recent literature, many works have started to augment diffusion algorithms with ideas from trajectory optimization. Various works have implemented this through guidance from model-based cost functions, or used Monte Carlo sampling to run diffusion algorithms in a similar vein to sampling-based trajectory optimization.

## Technical Background And Motivation

### III-A Diffusion Models

Diffusion models approach the problem of sampling from a target distribution with density $p(x)$ by setting it as $p_{0}(x)$, the initial distribution at time $t=0$, for a diffusion stochastic process which adds noise to the target distribution until it approaches a stationary distribution that is easy to sample. By sampling from this simple distribution and running the reverse process, we can recover samples from the original target distribution. For example, Denoising Diffusion Probabilistic Models (DDPM) has the following forward process which adds corrupting noise to samples from the target distribution during training and runs the reverse process to produce samples from the target distribution during inference where $\beta$, $\alpha$, $\bar{\alpha}$ and $\varsigma$ are parameters that depend on the noise schedule, which is a hyperparameter of the algorithm, and $z_{t}$ is drawn from a standard Gaussian. The term $\epsilon_{\theta}$ represents the mean of a denoising Gaussian term added in the reverse process, parametrized by a neural network with parameters $\theta$. In a "score-based" framework, this discretized reverse process can also be written as where the $\nabla\log p_{s}(x)$ is known as the Stein score and is generally approximated by a neural network. The forward process has a standard Gaussian distribution $\mathcal{N}(0,I_{N})$ as its stationary distribution, which can be tractably sampled. In general, neither the target distribution nor the score function is available for a given problem. Therefore, the score function (or denoising mean) is learned by taking available samples from the target distribution, running the forward process, and training a neural network to minimize an evidence lower bound or score matching loss.

### III-B Model-based Diffusion

Given an optimization problem to minimize $J(x)$ over decision variable $x$, we can construct a Boltzmann-Gibbs distribution, where the density $p(x)$ is higher where the cost is lower and temperature, $\lambda$, is a constant parameter, decreasing which concentrates the mass closer to the minima of the function. This turns optimization of $J(x)$ into sampling from unnormalized densities.

Model Based Diffusion performs sampling by running the underlying process behind the DDPM algorithm, which requires having access to the score function, $\nabla\log p_{s}(x_{s})$. In the learning-free setting, since we do not directly have access to the score function but do have access to an unnormalized $p_{0}(x)$, MBD uses Monte Carlo sampling to estimate the score where $\mathcal{X}_{s}=\{\hat{x}_{i}\}_{0}^{N}$ and $\hat{x}_{i}$ are realizations drawn from $X_{s}\sim\mathcal{N}(\frac{x_{s}}{\sqrt{\bar{\alpha}_{s-1}}},\sigma_{s}^{2}I)$ and $\sigma_{s}^{2}=\frac{1}{\sqrt{\bar{\alpha}_{s-1}}}-1$. This is similar to zeroth order optimization methods such as the cross-entropy method (CEM), random search, and model predictive path integral control. For a dynamic system, evaluating $p_{0}(\tau)$ for the trajectory, $\tau$, the trajectory can be parametrized by the actions $u_{0:T}$ and rolled out to calculate $J(\tau)$.

However, this Monte Carlo approach poses problems in a constrained environment where a large part of the solution space violates constraints. We demonstrate that its performance catastrophically degrades as constraints become restrictive even on simple 2D systems. If the problem is heavily constrained, the target density $p(x)=0$ in much of the solution space and samples $\hat{x}_{i}$ are likely to have no contribution, leading to "dead" samples with no information. Figure 2 shows how increasing obstacle radius in an existing obstacle avoidance problem causes failure, which MBD otherwise performs well .

Figure 2: Increasing obstacle size in a 2D obstacle avoidance problem leads to catastrophic degradation in performance for MBD as the sampling efficiency of the score estimate suffers

## Emerging Barrier Model-Based Diffusion

Our motivating context is robotic motion planning where it is common to encounter highly constrained optimization problems. However, our contribution is more generally applicable as an optimization-by-sampling algorithm.

### IV-A Problem Statement

We aim to solve the constrained optimization problem We approximate this problem to one of sampling from distribution where $\mathds{1}_{g}(x)$ is an indicator function that is zero on the constraint violating set and one on the feasible set. Sampling from $p(x)$ provides high quality approximate solutions to the original problem. We perform sampling by setting the target distribution at $s=0$ as $p_{0}(x):=p(x)$, and running a DDPM process as in equation using a score approximation as in equation. MBD uses a non-stochastic form of DDPM where $\varsigma_{s}=0$ and the only stochasticity comes from Monte Carlo sampling and we follow that convention.

### IV-B Motion Planning

To apply our method to constrained motion planning, we work with the discrete time non-linear systems of the form where $\xi\in\mathbb{R}^{n}$, $u\in\mathbb{R}^{m}$ and $f(\cdot):\mathbb{R}^{n}\times\mathbb{R}^{m}\rightarrow\mathbb{R}^{n}$ represent general nonlinear dynamics.

We parameterize a trajectory, $\tau$, of the system via the actions taken, $\tau=\{u_{0:T}\}\in\mathbb{R}^{m\times T}$, where $T$ is the control time horizon length, which allows sampling feasible trajectories without enforcing equality constraints from the dynamics. We assume the availability of an oracle (such as a simulator) that can be queried with actions to run rollouts to find $\xi_{0:T+1}$.

We specify a planning task through a cost function that we seek to minimize where $J:\mathbb{R}^{n\times(T+1)}\times\mathbb{R}^{m\times T}\rightarrow\mathbb{R}$ is the total trajectory cost. We specify the constraint as an inequality $g(\tau)\geq 0$ where $g(\tau):\mathbb{R}^{m\times T}\rightarrow\mathbb{R}$. For example, for a collision avoidance problem, this might be a function mapping to the distance to the closest obstacle. Note that the diffusion process time index, $s\in[0\dots S]$, in $p_{s}(\tau)$ corresponds iterations of our diffusion process and is different, $t\in[0\dots T+1]$, the index for the temporal component of our trajectory.

### IV-C Emerging Barriers

Our proposed solution involves modifying the target distribution with a time-varying barrier that emerges over the process. Every iteration of the diffusion process, we run a DDPM style update as in equation. However, inspired by interior point methods for constrained optimization, we introduce a barrier cost function, where $\mu$ controls the "hardness" of the barrier term, $c_{s}$ is a positive time-varying offset that acts as a constraint relaxation term. We augment the problem cost and target distribution with $b(x,s)$ by defining a time-varying "target distribution", $\hat{p}_{0}(x,s)$, that varies over the diffusion time horizon where the barrier term helps approximate $\mathds{1}_{g}$. Intuitively, when the relaxed constraint $g(x)+c_{s}\leq 0$, the cost is infinite and thus $\hat{p}_{0}(x)=0$. When $c_{s}>\inf g(x)$, we have no "dead" samples. This allows us to start off with an unconstrained solution space with tightening constraints guided by the barrier. The final algorithm which we call Emerging Barrier MBD can be seen in Algorithm 1.

Figure 3: Evolution of relaxed constraint g(x) + cs, the time-varying cost function and the associated normalized density, for the constraint |x| ≤ 1 The barrier cost in the feasible region can be seen as a force that encourages distance away from the constraint boundary and moves with a moving constraint boundary. The emerging barrier can be thought of as complementary to the diffusion itself, which also assigns non-zero probability to zero probability regions in the target distribution by Gaussian smoothing.

For a meaningful emerging barrier schedule, $c_{s}$ decreases over the reverse process, to enforce constraints as in Figure 3. $\mu_{s}$ can either decrease to $0$ or be kept at a tuned constant value (e.g. for a obstacle avoidance problem high $\mu_{s}$ encourages distance from obstacles). At $s=0$, $c_{s}=0$ and $\mu_{s}$ is small (such that $J(x)\gg b(x)$ for $g(x)<0$). We note that if $\mu,c\rightarrow$ as $s\rightarrow 0$, the target probability distribution converges pointwise to our true target distribution, Additionally, although the cost can become $\infty$, since the equations and directly use the probability density, which is $0$ for constraint-breaking samples, the operations taken every step are still well defined.

Input: Noise schedule βs, Barrier schedule (μs, cs), Diffusion steps S, Cost function J(x), Constraint g(x), Temperature λ // Compute scheduling variables $\bar{\alpha}_{s}\leftarrow\prod_{i=0}^{s}\alpha_{i}$ // Sample initial diffusion state // Sample around current state $\mathcal{X}_{s}\sim\mathcal{N}(\frac{x_{s}}{\sqrt{\bar{\alpha}_{s-1}}},\frac{I}{\sqrt{\bar{\alpha}_{s-1}}}-I)$ // Update barrier parameters $\hat{p}_{0}(x):=\exp\left(\frac{1}{\lambda}J(x)-\mu_{s}\log(g(x)+c_{s})\right)$ // Compute score approximation $\gamma\leftarrow-\frac{x_{s}}{1-\bar{\alpha}_{s}}+\frac{\sqrt{\bar{\alpha}_{s}}}{1-\bar{\alpha_{s}}}\left(\frac{\sum_{\hat{x}_{i}\in\mathcal{X}_{s}}\hat{x}_{i}\,\hat{p}_{0}(\hat{x}_{i})}{\sum_{\hat{x}_{i}\in\mathcal{X}_{s}}\hat{p}_{0}(\hat{x}_{i})}\right)$ // Run reverse diffusion step $x_{s-1}\leftarrow\frac{1}{\sqrt{\alpha_{s}}}\left[x_{s}+(1-\bar{\alpha}_{s})\gamma\right]$ Algorithm 1 Emerging Barrier MBD EB-MBD has schedules of the barrier offset $c_{s}$ and barrier softness $\mu_{s}$ as hyperparameters of the algorithm. The key challenge in tuning EB-MBD is maintaining "alive" samples throughout the process despite the constraint tightening over the process.

We may interpret the behavior of emerging barriers as occurring in two regimes which we refer to as the global regime and the local regime. At the beginning, model-based diffusion operates in the global regime, with high sampling noise and relaxed constraints. In this regime, EB-MBD explores many local minima e.g. attempting various modes of reaching the target in Figure 2a. Towards the end of the diffusion process, EB-MBD is in the local regime, where the sampling noise is small and the iterations closely approximate gradient ascent on the unmodified $p_{0}(x)$ -- this corresponds to refining a single trajectory in Figure 2a.

### IV-D Barrier analysis

As $c_{0}=0$, any schedule that reduces $c_{s}$ slowly early in the process must speed up proportionally later in the process and vice versa. A constraint that rapidly decreases $c_{s}$ in the beginning produces a larger number of "dead" infeasible samples, suffering from lack of gradient information, similar to MBD. A slow progression has higher quality gradient information but towards the end of the process, as $c_{s}$ is required to converge to $0$ quickly, the process may struggle with dead samples. This can mean infeasible solutions as the iterates cannot keep up with the progression of the barrier and remain dead permanently. This exposes a trade-off in the offset schedule as a design decision.

With some assumptions, we can analyze the worst-case behavior in the local regime of the EB-MBD process to lower-bound the probability of dead samples.

### Assumption 1

The constraint function $g(x)$ is a linear signed distance function $g(x)=w^{T}x+b$ with $||\nabla g(x)||=||w||=1$, where $w$ has the same dimensions as $x$ and $b$ is scalar We justify this as the first order Taylor series of $g(x)$ which is a valid approximation in the limit towards the end of the process, as we will be sampling $g(x_{s}+\varepsilon)$, where $\varepsilon$ is a perturbation with very small variance. We note that all SDFs are $1$-Lipschitz and almost everywhere $||\nabla g(x)||=1$.

### Lemma 1

Suppose Assumption 1 holds, then a given $x_{s}$, the probability that a random sample of $X_{s}$ is alive is lower bounded by where $\sigma^{2}$ is the sampling variance of the MBD process, and $\Phi(\cdot)$ is the univariate Gaussian cumulative distribution function.

The proof for this lemma is provided in Appendix -B. A sample $x$ is alive if $g(x)+c_{s}\geq 0$, for which we get the probability by MBD samples from $X_{s}\sim\mathcal{N}(\frac{x_{s}}{\sqrt{\bar{\alpha}_{s-1}}},\sigma_{s}^{2}I)$. We can arrive at Lemma 1 by expanding and applying Assumption 1. We can interpret this as the probability increasing with $g(x_{s})$ -- which is a distance from constraint boundary for an SDF --, our offset $c_{s}$, and with increasing sampling variance, $\sigma_{s}$.

Lemma 1 provides some insight but it depends critically on the location of $x_{s}$. For an active constraint, the barrier provides a repulsive force that pushes iterates away from the constraint while the objective function does the opposite. This forms a "boundary layer" where the diffusion state will tend to be attracted. To provide further insight we next assume that $x_{s}$ is at the local minimum of $J(x,s+1)$ at this boundary layer.

### Assumption 2

This is a common assumption in optimization and is met by common costs such as quadratic functions.

### Assumption 3

The local minima, $x^{\star}$ of $\hat{J}(x,s)$ is bounded $||x^{\star}||\leq R$ A reasonable bound for the target distribution $X_{0}$ is often known, e.g. due to actuator limits, and the source distribution's optimum is bounded as $X_{S}\sim N(0,I_{d})$. Thus, we are assuming the diffusion process that interpolates between the two distributions keeps bounded minima.

### Corollary 1

Assumption 2 implies that $J(x)$ is $L_{J}$-Lipschitz continuous within the domain $\{x:||x||\leq R\}$, where $L_{J}=||\nabla J||+M_{J}R$

### Assumption 4

$x_{s}$ is located at the local minimum of the $\hat{J}(x,s+1)$ where $\nabla J(x^{\star}_{s+1})+\nabla b(x^{\star}_{s+1},s+1)=0$.

This can be justified as MBD's optimization process on annealed the target density occurring on a faster time scale than the change in the barrier. The tight tracking of the local minima by MBD is visible experimentally in the original work. We refer to \[16")\] for a convergence analysis of similar algorithms.

### Theorem 1

Suppose assumptions 1-4 hold, then $\mathbb{P}(X_{s}\text{ alive})$, the probability that a sample drawn from $X_{s}$ is alive, is lower bounded by

### Proof

We can find the location of the minima by solving By taking the norm, and using Assumption 1 and 2 Using assumption 4, we substitute $g(x_{s})=g(x^{\star}_{s+1})$ into Lemma 1, we arrive at the final statement. ∎ Based on Theorem 1, there is a simple relationship that governs the behavior of solutions in the local regime of EB-MBD. In particular, $\mu$ governs a distance from the constraint boundary. A smaller $\mu$ leads to lower cost solutions but it also leads to reduced probability of sampling live solutions. This can be counteracted by reducing $(c_{s}-c_{s+1})$, which is the rate of emergence. We note that the barrier emergence rate in this late stage of the the process can be reduced by either performing emergence earlier in the process, or by increasing number of diffusion iterations so that the emergence budget is spread over more iterations. On the other hand, if we desire fewer diffusion iterations for faster runtime, to avoid EB-MBD returning infeasible solutions -- which is possible due to dead samples with too quick barrier emergence (See experimental results in V-A) -- we can increase $\mu$.

## Experimental Results

We implement Emerging Barrier MBD using the JAX Python package and demonstrate results for both a 2D obstacle avoidance environment, and a 3D high DOF underwater mobile manipulator system using the MuJoCo MJX as the underlying simulator^11^1Code can be found at MJX allows simulation rollouts to be parallelized on a GPU. All experiments were conducted on a PC with an i7-13700K, and RTX 3070 GPU and 32 GB of memory.

As the possible form of $c_{s}$ is a large class of functions, we parametrize $c_{s}$ with to study the trade-off between early and late emergence, where $\kappa$ is a positive parameter controlling the trade-off. At $\kappa=1$, the constraint offset progresses linearly. As the effect of $\mu$ and $\kappa$ on liveliness is coupled, we keep $\mu$ fixed for all experiments to highlight its effects.

At $\kappa>1$, the offset progresses slowly at first and faster towards the end, and vice versa for $\kappa<1$. We use the DDPM noise schedule of $\beta_{1}=10^{-4}$ and $\beta_{T}=0.02$ with linear spacing for all experiments. $c_{\text{max}}$ is chosen to be the maximum value $g(x)$ could take .

### V-A 2D Obstacle Avoidance

We show the performance of EB-MBD on a simple 2D obstacle avoidance problem. The dynamics and cost are where $\xi_{r}$ is a target position, and $\texttt{sigmoid}(x)=\frac{1}{1+e^{-x}}$. $g(\tau)$ is the signed distance to the closest obstacle encountered over the trajectory. MBD struggles due to dead samples.

Figure 4 shows how EB-MBD performs better than than MBD, with every trajectory reaching near the goal, while maintaining diverse solutions. In comparison, none of the MBD solutions reach the target. We notice that there are many constraint violating trajectories for MBD which is where all samples were constraint violating throughout the diffusion process.

Figure 4: Left: Planned trajectories are noisy for MBD due to inefficient sampling. Right: EB-MBD successfully generates trajectories from diverse high quality modes, all of which reach the vicinity of the target Lower $\kappa$ values result in local poor minima, similar to MBD. Increasing $\kappa$ generally shows improvement; however, the tightening constraint boundary can overshoot the current solution leading to the diffusion process dying permanently (see $\kappa>1$ in Figure 5) as the current iterate gets stuck inside the moving constraint boundary, resulting in infeasible solutions. This can be improved by increasing $\mu$ to increase the boundary layer distance as explained in SectionIV-D.

Figure 5: Percentage of samples that violate constraints over diffusion time over various κ values. κ being too high leads to 100% constraint violations and infeasible outputs

### V-B Comparison to projection-based methods

The most commonly proposed method for enforcing constraints on diffusion models and sampling-based trajectory optimization involves projections onto the constraint satisfying set performed at each iteration.

A projection of the trajectory $\tau_{d}$ onto the feasible set defined by $g(\tau)\geq 0$ is denoted $\Pi_{g}(\tau_{d})$ These projections are cast as NLP problems and are not uniquely defined for non-convex sets. The authors of DPCC proposed using iteratively-tightening constraint for a diffusion-based MPC algorithm which is conceptually similar to progressive barriers. However, for MBD, simply ensuring constraints are satisfied after each step is not sufficient as when variance is high, most samples are still infeasible. Additionally, projections have a large computational burden as each iteration requires rollouts and taking derivatives. They also have variable runtime due to the varying convergence time of the optimizer. In comparison, MBD and EB-MBD have effectively a constant solve time -- although the hyperparameters may need to be tuned for the system.

Figure 6: Typical trajectories from MBD, EB-MBD (Ours), Projected MBD and DPCC-MBD. EB-MBD performs substantially better than projection methods and is the only one that reaches the goal We compare against projections to the constraint set and to DPCC-style tightening constraints in Table I. We show that simply applying projection-based methods to MBD is not successful since the sampling statistics around the feasible iterate after each projection are still poor early on in the process. Projections were implemented through SciPy's SLSQP solver with analytical derivatives provided through JAX's autodifferentiation, and constraint relaxation was done similar to EB-MBD by enforcing $g(\tau)+c_{s}\geq 0$.

EB-MBD is able to produce significantly lower cost trajectories and lower terminal distance to the target end point, all while taking orders of magnitude less time. Unlike the projection methods, EB-MBD also does not require taking derivatives of rollouts or the constraint function.

Mean Final Distance TABLE I: Comparison of EB-MBD on the 2D obstacle avoidance over 50 trajectories

### V-C Underwater Vehicle Manipulator System

We demonstrate EB-MBD on a high-dimensional motion planning problem in simulation for a Underwater Vehicle Manipulator System (UVMS), consisting of a BlueROV Heavy platform with a Reach Alpha manipulator, with $9$ kinematic DOF and an $11$ dimensional action space. The MuJoCo MJX simulator was used as the oracle to roll out actions and the task was to minimize a weighted combination of the quadratic cost associated with distance from the wrist of the manipulator to a target point, the actions, and the orientation of the ROV body. The target position is in a hollow box with an opening, and the constraint is to avoid the box. The cost is and $J(\tau)=\ell_{T}(\xi_{T+1})+\sum_{t=0}^{T}\ell(\xi_{t},u_{t})$, where $\xi_{w}$ is the wrist position component of $\xi$, $r_{t}$ is the target wrist position, $\Lambda$ is a diagonal weighting matrix and $q$ is an orientation quaternion. This problem is challenging due to its high dimensionality and the complex motion required; the base is required to move and multiple joints need to coordinate together without the inertia of the robot causing a collision later in the trajectory. Figure 7 (a) shows how EB-MBD is able to successfully plan for the motion and 7 (b) shows how MBD trajectories get stuck in a poor local minima when EB-MBD finds early trajectories through the obstacle which get pushed out to better trajectories over iterations. Table II shows how EB-MBD achieves lower mean cost and higher success rates -- which we define as the percentage of time the end effector was inside the box without collision. We were unable to run projection methods in a reasonable amount of computational time on the UVMS due to increase in complexity. We emphasize the scalability of EB-MBD as computational time only grows with the extra evaluations of $g(x)$, as opposed to the complexity of the non-linear program which often grows more rapidly for complex systems.

Figure 7: (a) With EB-MBD, the UVMS reaches the target point while avoiding the obstacle. (b) Intermediate end effector trajectories over a single inference of EB-MBD and MBD, with curves increasing in linewidth and redness towards the end of the process.

TABLE II: Comparison of EB-MBD on 3D UVMS system over 50 trajectories

## Conclusion

We addressed the performance degradation of model-based diffusion (MBD) for motion planning in highly constrained environments, a problem arising from poor score estimation when infeasible regions cover a large part of the solution space. We proposed Emerging-Barrier MBD, which applies an interior point-inspired time-varying barrier function, to guide solutions. This approach avoids catastrophic performance degradation and significantly improves solution quality for highly constrained problems. Our method was demonstrated on robotics collision avoidance problems, where it maintained good sample complexity and solution diversity. We analyzed the barrier schedule and its effect on solution liveliness statistics. We compare against projection-based constrained diffusion methods and show substantially better performance at orders of magnitude faster computational time.

While EB-MBD exhibited strong performance in our experiments, it does have some limitations. EB-MBD does not guarantee good solutions and good performance relies on barrier schedules well tuned for the problem. If a poor schedule is chosen, the output solutions can be entirely infeasible. Our analysis also assumes timescale separation of the diffusion process local convergence and the barrier emergence. Future work may involve adaptive barrier schedules that prevent permanently dead samples without additional barrier tuning, and further analysis of EB-MBD under milder assumptions.

### A Half-space Integral of a Gaussian

For a Gaussian distribution with density $f_{X}(\cdot)$, where $x,\mu\in\mathbb{R}^{n},\Sigma\in\mathbb{R}^{n\times n}$.

If $\Sigma=\sigma^{2}I$, with $\sigma^{2}\in\mathbb{R}$, then the integral over a half-space, where $\Phi(x)$ is the 1D Gaussian CDF.

### B Proof of Lemma 1

### Proof

A sample is alive if the relaxed constraint $(g(x)+c_{s}\geq 0)$ is met. MBD samples from $X_{s}\sim\mathcal{N}(\frac{x_{s}}{\sqrt{\bar{\alpha}_{s-1}}},\sigma_{s}^{2}I)$. If $x_{s}$ is known, and $\varepsilon$ refers to the zero mean perturbation with the same variance as $X_{s}$, then we find where we make make use of Assumption 1. Using Lipschitz continuity of $g(x)$ and using Appendix -A to write in terms of one dimensional Gaussian cumulative distribution function,
